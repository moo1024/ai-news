#!/usr/bin/env python3
"""AI 뉴스 하루치 수집기 — LLM 을 부르지 않는다. 긁어서 파일로 떨군다.

    python3 collect.py            오늘
    python3 collect.py 2026-08-17 그 날짜 기준(그 날 + 전날치)

산출물 ~/ai-news/<날짜>/
    _수집.json      항목 메타 목록 (아카이빙 단계가 읽는 입력)
    원문/<id>.md    확보한 전문 (Source Library 에 그대로 들어갈 정본)
    _수집로그.md    어느 출처가 몇 건 나왔고 뭐가 실패했나

설계 원칙
  - 출처 하나가 죽어도 파이프라인은 계속 간다. 실패는 로그에 남기고 넘어간다.
  - 중복은 URL 정규화 + 제목으로 여기서 걷어낸다. 노션 조회로 거는 중복은 그 다음 층.
  - 점수는 '무엇을 먼저 정리할지'의 힌트일 뿐, 자르는 칼이 아니다. 전량 남긴다.
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from xml.etree import ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36"

# curl_cffi 는 X(syndication) 에만 필요하다. 없으면 X 만 건너뛴다.
try:
    from curl_cffi import requests as cffi_requests  # type: ignore
except Exception:
    cffi_requests = None

AI_KEYWORDS = [
    "ai", "llm", "gpt", "claude", "anthropic", "openai", "gemini", "deepmind",
    "llama", "mistral", "qwen", "deepseek", "transformer", "diffusion", "agent",
    "rag", "fine-tun", "inference", "neural", "machine learning", "ml model",
    "chatbot", "copilot", "cursor", "prompt", "embedding", "multimodal",
    "인공지능", "생성형", "챗봇", "클로드", "오픈AI", "제미나이",
]

로그: list[str] = []


def 기록(줄: str) -> None:
    로그.append(줄)
    print(줄, flush=True)


# ---------------------------------------------------------------- 공통 유틸

def _디코드(raw: bytes) -> str:
    for enc in ("utf-8", "euc-kr", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def curl가져오기(url: str, timeout: int = 30) -> str:
    """`curl` 바이너리로 받는다.

    파이썬 urllib/curl_cffi 는 둘 다 403 을 맞는데 curl 은 통과하는 곳이 있다
    (2026-08-18 실측: r.jina.ai — urllib 403 / curl_cffi 403 / curl 200).
    그래서 마지막 수단이 아니라 특정 대상의 '정규 경로'로 쓴다.
    """
    import subprocess
    p = subprocess.run(
        ["curl", "-sL", "--compressed", "--max-time", str(timeout),
         "-A", UA, "-w", "\n__HTTP__%{http_code}", url],
        capture_output=True, timeout=timeout + 10)
    본문 = _디코드(p.stdout)
    코드 = 본문.rsplit("__HTTP__", 1)[-1].strip() if "__HTTP__" in 본문 else "000"
    본문 = 본문.rsplit("\n__HTTP__", 1)[0]
    if 코드 != "200":
        raise OSError(f"curl HTTP {코드}")
    return 본문


def 가져오기(url: str, timeout: int = 20) -> str:
    """urllib 우선, 차단(403/429)이면 curl 로 한 번 더."""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "*/*",
        "Accept-Language": "ko,en;q=0.8",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return _디코드(r.read())
    except urllib.error.HTTPError as e:
        if e.code in (403, 429, 503):
            return curl가져오기(url, timeout=timeout + 10)
        raise


def 태그정리(s: str) -> str:
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    s = re.sub(r"<br\s*/?>|</p>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = html.unescape(s)
    return re.sub(r"[ \t]{2,}", " ", s).strip()


def URL정규화(url: str) -> str:
    """추적 파라미터·앵커를 떼서 같은 글을 같은 것으로 본다."""
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return url
    q = [(k, v) for k, v in urllib.parse.parse_qsl(p.query)
         if not k.lower().startswith(("utm_", "ref", "fbclid", "gclid", "mc_"))]
    return urllib.parse.urlunsplit((
        p.scheme.lower(), p.netloc.lower().removeprefix("www."), p.path.rstrip("/"),
        urllib.parse.urlencode(q), "",
    ))


def 고유ID(url: str) -> str:
    """URL 에서 사람이 알아볼 수 있는 고유 조각을 뽑는다. 노션 중복조회 키."""
    import hashlib
    n = URL정규화(url)
    꼬리 = re.sub(r"[^a-zA-Z0-9]+", "-", n.rsplit("/", 1)[-1])[:40].strip("-")
    해시 = hashlib.sha1(n.encode()).hexdigest()[:8]
    return f"{꼬리}-{해시}" if 꼬리 else 해시


def AI관련(*조각: str) -> bool:
    본문 = " ".join(조각).lower()
    return any(k in 본문 for k in AI_KEYWORDS)


def 시각파싱(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.strip()
    for 형식 in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z",
                 "%a %b %d %H:%M:%S %z %Y",  # X(트위터) created_at
                 "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S.%f%z",
                 "%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            d = datetime.strptime(s.replace("Z", "+0000"), 형식)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
    except Exception:
        return None


def 항목(출처: str, 제목: str, url: str, 발행: datetime | None,
        요약: str = "", 반응: int = 0, weight: float = 1.0, 원저자: str = "") -> dict:
    return {
        "id": 고유ID(url),
        "출처": 출처,
        "제목": 태그정리(제목)[:300],
        "url": url,
        "정규url": URL정규화(url),
        "발행": 발행.astimezone(timezone.utc).isoformat() if 발행 else None,
        "요약": 태그정리(요약)[:1200],
        "반응": 반응,
        "원저자": 원저자,
        "_weight": weight,
        "본문파일": None,
        "본문상태": "미확보",
    }


# ---------------------------------------------------------------- 출처별 수집

def RSS파싱(xml: str) -> list[dict]:
    """RSS 2.0 과 Atom 을 한 함수로 읽는다."""
    out = []
    try:
        root = ET.fromstring(xml.lstrip())
    except ET.ParseError:
        return out
    ns = {"a": "http://www.w3.org/2005/Atom", "c": "http://purl.org/rss/1.0/modules/content/"}

    for it in root.iter():
        꼬리 = it.tag.split("}")[-1]
        if 꼬리 not in ("item", "entry"):
            continue

        def 값(*이름: str) -> str:
            for n in 이름:
                el = it.find(n) if "}" not in n else None
                if el is None:
                    for child in it:
                        if child.tag.split("}")[-1] == n:
                            el = child
                            break
                if el is not None and (el.text or "").strip():
                    return el.text.strip()
            return ""

        제목 = 값("title")
        링크 = 값("link")
        if not 링크:
            for child in it:
                if child.tag.split("}")[-1] == "link" and child.get("href"):
                    링크 = child.get("href", "")
                    break
        if not (제목 and 링크):
            continue
        요약 = 값("description", "summary", "content", "encoded")
        발행 = 시각파싱(값("pubDate", "published", "updated", "date"))
        out.append({"제목": 제목, "링크": 링크, "요약": 요약, "발행": 발행})
    return out


def 수집_rss(설정: dict, 하한: datetime) -> list[dict]:
    결과 = []

    def 하나(피드: dict) -> list[dict]:
        try:
            xml = 가져오기(피드["url"], timeout=25)
        except Exception as e:
            기록(f"  ✗ RSS {피드['이름']}: {type(e).__name__} {e}")
            return []
        엔트리 = RSS파싱(xml)
        모음 = []
        for e in 엔트리:
            if e["발행"] and e["발행"] < 하한:
                continue
            if not AI관련(e["제목"], e["요약"], 피드["이름"]):
                continue
            모음.append(항목(피드["이름"], e["제목"], e["링크"], e["발행"],
                            e["요약"], weight=피드.get("weight", 1.0)))
        # 구글뉴스 같은 검색 피드는 99건씩 쏟아져 다른 출처를 덮는다. 피드당 상한을 건다.
        상한 = int(피드.get("상한", 설정.get("피드당상한", 15)))
        잘림 = max(0, len(모음) - 상한)
        모음 = 모음[:상한]
        기록(f"  · RSS {피드['이름']}: {len(모음)}건 (전체 {len(엔트리)}"
             + (f", {잘림}건 잘림)" if 잘림 else ")"))
        return 모음

    with ThreadPoolExecutor(max_workers=8) as ex:
        미래 = [ex.submit(하나, f) for f in 설정["피드"]]
        for f in as_completed(미래):
            결과 += f.result()
    return 결과


def 수집_hn(설정: dict, 하한: datetime) -> list[dict]:
    결과 = []
    try:
        ids = json.loads(가져오기("https://hacker-news.firebaseio.com/v0/topstories.json"))[:120]
        ids += json.loads(가져오기("https://hacker-news.firebaseio.com/v0/newstories.json"))[:80]
    except Exception as e:
        기록(f"  ✗ HN 목록: {type(e).__name__} {e}")
        return 결과

    def 하나(i: int) -> dict | None:
        try:
            it = json.loads(가져오기(f"https://hacker-news.firebaseio.com/v0/item/{i}.json", timeout=12))
        except Exception:
            return None
        if not it or it.get("type") != "story":
            return None
        제목 = it.get("title", "")
        if not AI관련(제목):
            return None
        점수 = it.get("score", 0)
        if 점수 < 설정.get("최소점수", 30):
            return None
        발행 = datetime.fromtimestamp(it.get("time", 0), tz=timezone.utc)
        if 발행 < 하한:
            return None
        url = it.get("url") or f"https://news.ycombinator.com/item?id={i}"
        return 항목("Hacker News", 제목, url, 발행,
                   요약=태그정리(it.get("text", "")),
                   반응=점수, weight=설정.get("weight", 1.3))

    with ThreadPoolExecutor(max_workers=12) as ex:
        for f in as_completed([ex.submit(하나, i) for i in dict.fromkeys(ids)]):
            r = f.result()
            if r:
                결과.append(r)

    결과.sort(key=lambda x: -x["반응"])
    결과 = 결과[: 설정.get("최대건수", 20)]
    기록(f"  · Hacker News: {len(결과)}건")
    return 결과


def 수집_arxiv(설정: dict, 하한: datetime) -> list[dict]:
    결과 = []
    for 분야 in 설정.get("분야", []):
        url = ("http://export.arxiv.org/api/query?"
               f"search_query=cat:{분야}&sortBy=submittedDate&sortOrder=descending"
               f"&max_results={설정.get('분야당건수', 8)}")
        try:
            xml = 가져오기(url, timeout=30)
        except Exception as e:
            기록(f"  ✗ arXiv {분야}: {type(e).__name__} {e}")
            time.sleep(1.2)
            continue
        n = 0
        for e in RSS파싱(xml):
            if e["발행"] and e["발행"] < 하한:
                continue
            결과.append(항목(f"arXiv {분야}", e["제목"], e["링크"], e["발행"],
                            e["요약"], weight=설정.get("weight", 1.0)))
            n += 1
        기록(f"  · arXiv {분야}: {n}건")
        time.sleep(1.2)  # 3req/s 제한
    return 결과


def 수집_reddit(설정: dict, 하한: datetime) -> list[dict]:
    결과 = []

    # .json 은 WAF 로 403, Atom 만 통한다. 그리고 동시에 때리면 통째로 429 다
    # (2026-08-18 실측: 6개 병렬 → 5개가 429). 순차 + 2초 간격으로만 간다.
    for sub in 설정.get("서브레딧", []):
        xml = None
        for 시도 in range(2):
            try:
                xml = 가져오기(f"https://www.reddit.com/r/{sub}/hot.rss", timeout=25)
                break
            except Exception as e:
                if 시도 == 1:
                    기록(f"  ✗ Reddit r/{sub}: {type(e).__name__} {e}")
                else:
                    time.sleep(15)  # 레딧은 IP 단위로 세게 막는다. 짧게 쉬면 또 429.
        if xml is None:
            continue
        n = 0
        for e in RSS파싱(xml)[: 설정.get("서브당건수", 6)]:
            if e["발행"] and e["발행"] < 하한:
                continue
            결과.append(항목(f"Reddit r/{sub}", e["제목"], e["링크"], e["발행"],
                            e["요약"], weight=설정.get("weight", 1.0)))
            n += 1
        기록(f"  · Reddit r/{sub}: {n}건")
        time.sleep(5.0)
    return 결과


def 수집_x(설정: dict, 하한: datetime) -> list[dict]:
    if cffi_requests is None:
        기록("  ✗ X: curl_cffi 없음 — 건너뜀 (venv 파이썬으로 실행해야 한다)")
        return []
    결과 = []
    for 계정 in 설정.get("계정", []):
        url = f"https://syndication.twitter.com/srv/timeline-profile/screen-name/{계정}"
        entries = None
        # 429 가 잦다. 지문을 바꿔가며 세 번 시도하고, 그래도 안 되면 그 계정만 포기한다.
        for 시도, 지문 in enumerate(("safari", "chrome131", "safari_ios")):
            try:
                r = cffi_requests.get(url, impersonate=지문, timeout=25)
                if r.status_code != 200:
                    raise OSError(f"HTTP {r.status_code}")
                m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', r.text, re.S)
                if not m:
                    raise ValueError("__NEXT_DATA__ 없음")
                entries = json.loads(m.group(1))["props"]["pageProps"]["timeline"]["entries"]
                break
            except Exception as e:
                마지막 = e
                time.sleep(5 * (시도 + 1))
        if entries is None:
            기록(f"  ✗ X @{계정}: {type(마지막).__name__} {마지막}")
            continue

        n = 0
        for ent in entries:
            t = (ent.get("content", {}).get("tweet") or {})
            if not t:
                continue
            tid = t.get("id_str") or ""
            # created_at 은 포맷이 오락가락한다. 트윗 ID(snowflake)에 생성 시각이
            # 박혀 있으니 그쪽이 정확하다. (id >> 22) + 트위터 epoch
            발행 = 시각파싱(t.get("created_at"))
            if 발행 is None and tid.isdigit():
                발행 = datetime.fromtimestamp(
                    ((int(tid) >> 22) + 1288834974657) / 1000, tz=timezone.utc)
            if 발행 and 발행 < 하한:
                continue
            본문 = t.get("full_text") or t.get("text") or ""
            # 리트윗은 syndication 이 본문을 잘라서 준다("RT @gdb: defenders can…").
            # 잘린 조각으로는 정리본을 못 쓴다.
            if not 본문 or 본문.startswith("RT @"):
                continue
            결과.append(항목(f"X @{계정}", 본문[:120], f"https://x.com/{계정}/status/{tid}",
                            발행, 요약=본문, 반응=int(t.get("favorite_count", 0)),
                            weight=설정.get("weight", 1.4), 원저자=f"@{계정}"))
            n += 1
            if n >= 설정.get("계정당건수", 5):
                break
        기록(f"  · X @{계정}: {n}건")
        time.sleep(1.0)
    return 결과


def 수집_bluesky(설정: dict, 하한: datetime) -> list[dict]:
    결과 = []
    for 계정 in 설정.get("계정", []):
        url = ("https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed"
               f"?actor={urllib.parse.quote(계정)}&limit={설정.get('계정당건수', 5)}")
        try:
            data = json.loads(가져오기(url, timeout=20))
        except Exception as e:
            기록(f"  ✗ Bluesky {계정}: {type(e).__name__} {e}")
            continue
        n = 0
        for f in data.get("feed", []):
            p = f.get("post", {})
            rec = p.get("record", {})
            본문 = rec.get("text", "")
            발행 = 시각파싱(rec.get("createdAt"))
            if not 본문 or (발행 and 발행 < 하한):
                continue
            if not AI관련(본문):
                continue
            rkey = (p.get("uri") or "").rsplit("/", 1)[-1]
            결과.append(항목(f"Bluesky {계정}", 본문[:120],
                            f"https://bsky.app/profile/{계정}/post/{rkey}", 발행,
                            요약=본문, 반응=int(p.get("likeCount", 0)),
                            weight=설정.get("weight", 0.9), 원저자=계정))
            n += 1
        기록(f"  · Bluesky {계정}: {n}건")
    return 결과


# ---------------------------------------------------------------- 본문 확보

def 본문받기(it: dict, 글자수상한: int) -> tuple[str, str]:
    """Jina Reader 로 전문을 받는다. (본문, 상태) 를 준다."""
    표적 = it["url"]
    # X·Bluesky 는 이미 전문이 요약칸에 다 들어 있다. 헛되이 긁지 않는다.
    if it["출처"].startswith(("X @", "Bluesky")):
        return it["요약"], "확인 완료"
    # Jina 는 파이썬 클라이언트를 403 으로 막는다. curl 로만 통한다(위 주석 참조).
    try:
        txt = curl가져오기("https://r.jina.ai/" + 표적, timeout=50)
    except Exception as e:
        try:
            txt = 가져오기(표적, timeout=30)
            txt = 태그정리(txt)
        except Exception:
            return "", f"접근 불가 (Jina {e} · 직접 접속도 실패)"
    txt = txt.strip()
    if len(txt) < 400:
        return txt, "일부 확인 (본문이 짧게만 잡힘)"
    return txt[:글자수상한], "확인 완료"


# ---------------------------------------------------------------- 본체

def main() -> int:
    기준 = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime("%Y-%m-%d")
    try:
        기준일 = datetime.strptime(기준, "%Y-%m-%d")
    except ValueError:
        print(f"❌ 날짜 형식이 아니다: {기준}", file=sys.stderr)
        return 2

    # 그날 + 전날치를 본다. 크론을 놓친 날이 있어도 구멍이 안 생긴다.
    하한 = (기준일 - timedelta(days=2)).replace(tzinfo=timezone.utc)

    # 지난 날짜를 따라잡을 때는 위쪽도 막아야 한다. RSS·API 는 언제 물어봐도
    # '지금' 것을 주므로, 상한이 없으면 어제 폴더에 오늘 뉴스가 들어간다.
    오늘 = datetime.now().strftime("%Y-%m-%d")
    상한 = None if 기준 == 오늘 else (기준일 + timedelta(days=1)).replace(tzinfo=timezone.utc)

    설정 = json.load(open(os.path.join(HERE, "sources.json"), encoding="utf-8"))
    날짜폴더 = os.path.join(HERE, 기준)
    원문폴더 = os.path.join(날짜폴더, "원문")
    os.makedirs(원문폴더, exist_ok=True)

    기록(f"===== {기준} AI 뉴스 수집 (하한 {하한:%Y-%m-%d}) =====")

    수집: list[dict] = []
    표 = [
        ("rss", 수집_rss), ("hn", 수집_hn), ("arxiv", 수집_arxiv),
        ("reddit", 수집_reddit), ("x", 수집_x), ("bluesky", 수집_bluesky),
    ]
    for 이름, 함수 in 표:
        s = 설정.get(이름, {})
        if not s.get("enabled"):
            기록(f"[{이름}] 꺼져 있음")
            continue
        기록(f"[{이름}]")
        # 공식 계정은 며칠씩 조용하다가 하나 올린다. 창이 2일이면 통째로 빈다.
        # 출처별로 창을 따로 줄 수 있게 했다(sources.json 의 "일수").
        이하한 = (기준일 - timedelta(days=int(s["일수"]))).replace(tzinfo=timezone.utc) \
            if s.get("일수") else 하한
        try:
            수집 += 함수(s, 이하한)
        except Exception as e:
            기록(f"  ✗ {이름} 전체 실패: {type(e).__name__} {e}")

    if 상한 is not None:
        전 = len(수집)
        수집 = [it for it in 수집
                if not it["발행"] or 시각파싱(it["발행"]) <= 상한]
        기록(f"\n[지난 날짜 보정] {기준} 이후 항목 {전 - len(수집)}건 제외")

    # 중복 제거 — 정규 URL 우선, 같은 제목도 하나로 본다.
    본: dict[str, dict] = {}
    제목본: set[str] = set()
    for it in 수집:
        제목키 = re.sub(r"\W+", "", it["제목"].lower())[:60]
        if it["정규url"] in 본 or (제목키 and 제목키 in 제목본):
            기존 = 본.get(it["정규url"])
            if 기존 and it["반응"] > 기존["반응"]:
                기존["반응"] = it["반응"]
            continue
        본[it["정규url"]] = it
        if 제목키:
            제목본.add(제목키)
    항목들 = list(본.values())

    # 점수 — 무엇을 먼저 볼지의 힌트. 자르는 칼이 아니다.
    지금 = datetime.now(timezone.utc)
    for it in 항목들:
        발행 = 시각파싱(it["발행"]) or 지금
        시간차 = max((지금 - 발행).total_seconds() / 3600, 0)
        신선도 = max(0.0, 1.0 - 시간차 / 72.0)
        it["점수"] = round(it["_weight"] * (1 + 신선도) + min(it["반응"], 500) / 250, 3)
        it.pop("_weight", None)
    항목들.sort(key=lambda x: -x["점수"])

    기록(f"\n[중복 제거] {len(수집)}건 → {len(항목들)}건")

    # 본문 확보 — 상위 N건만
    bs = 설정.get("본문확보", {})
    if bs.get("enabled") and 항목들:
        상한 = int(bs.get("상한", 55))
        글자수 = int(bs.get("글자수상한", 14000))
        # 그냥 점수 상위 N 을 뽑으면 계정 8개짜리 X 가 예산을 통째로 먹는다
        # (2026-08-18 실측: 상위 40건 중 X 가 40건). 출처별 상한을 먼저 건다.
        출처상한 = int(bs.get("출처당상한", 4))
        쓴수: dict[str, int] = {}
        대상 = []
        나머지 = []
        for it in 항목들:
            키 = it["출처"].split(" r/")[0].split(" @")[0]
            if 쓴수.get(키, 0) < 출처상한:
                쓴수[키] = 쓴수.get(키, 0) + 1
                대상.append(it)
            else:
                나머지.append(it)
            if len(대상) >= 상한:
                break
        대상 += 나머지[: max(0, 상한 - len(대상))]  # 남으면 점수순으로 채운다
        기록(f"[본문확보] 상위 {len(대상)}건 Jina Reader")

        def 하나(it: dict) -> None:
            본문, 상태 = 본문받기(it, 글자수)
            it["본문상태"] = 상태
            if 본문:
                경로 = os.path.join(원문폴더, f"{it['id']}.md")
                with open(경로, "w", encoding="utf-8") as f:
                    f.write(f"# {it['제목']}\n\n")
                    f.write(f"- 출처: {it['출처']}\n- 원본 링크: {it['url']}\n")
                    f.write(f"- 발행: {it['발행'] or '미상'}\n- 접근상태: {상태}\n\n---\n\n")
                    f.write(본문)
                it["본문파일"] = os.path.relpath(경로, HERE)

        with ThreadPoolExecutor(max_workers=6) as ex:
            list(as_completed([ex.submit(하나, it) for it in 대상]))
        성공 = sum(1 for it in 대상 if it["본문상태"] == "확인 완료")
        기록(f"  · 전문 확보 {성공}/{len(대상)}건")

    with open(os.path.join(날짜폴더, "_수집.json"), "w", encoding="utf-8") as f:
        json.dump({"기준일": 기준, "수집시각": 지금.isoformat(),
                   "건수": len(항목들), "항목": 항목들}, f, ensure_ascii=False, indent=2)

    with open(os.path.join(날짜폴더, "_수집로그.md"), "w", encoding="utf-8") as f:
        f.write(f"# {기준} 수집 로그\n\n```\n" + "\n".join(로그) + "\n```\n")

    기록(f"\n===== 완료: {len(항목들)}건 → {날짜폴더} =====")
    if not 항목들:
        기록("❌ 한 건도 못 모았다 — 네트워크 또는 전 출처 실패")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
