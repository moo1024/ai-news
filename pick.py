#!/usr/bin/env python3
"""수집 결과를 아카이빙 단계가 읽을 수 있는 크기로 줄인다.

    python3 pick.py <날짜> [정식건수]

_수집.json 은 150건 × 요약 1,200자라 그대로 넘기면 컨텍스트를 다 먹는다.
그래서 두 개로 갈라 준다.

    _브리핑입력.md   전 항목 한 줄 요약 (뉴스레터가 이걸로 만들어진다)
    _후보.json       정식 2단계 아카이빙 대상 (기본 12건) — 전문이 확보된 것만 고른다

고르는 기준은 점수 순이되, 출처가 한쪽으로 쏠리지 않게 같은 출처는 최대 3건까지만 담는다.
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
출처당상한 = 3
지난날확인 = 14  # 며칠 전까지 거슬러 '이미 정리한 것'을 볼까


def 이미정리한것(날짜: str) -> set[str]:
    """지난 날들에 이미 2단계 아카이빙한 id 를 모은다.

    한 기사가 며칠씩 피드에 남아 있어서, 안 걸러내면 어제 정리한 걸 오늘 또 고른다
    (2026-08-19 실측: 후보 12건 중 5건이 전날과 동일). 노션 단계에서도 중복 조회로
    막지만, 그러면 그날 새로 정리되는 게 7건으로 줄어든다. 여기서 빼고 다음 순위를 채운다.
    """
    from datetime import datetime, timedelta
    기준 = datetime.strptime(날짜, "%Y-%m-%d")
    본: set[str] = set()
    for i in range(1, 지난날확인 + 1):
        d = (기준 - timedelta(days=i)).strftime("%Y-%m-%d")
        경로 = os.path.join(HERE, d, "_archived.json")
        if not os.path.exists(경로):
            continue
        try:
            자료 = json.load(open(경로, encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for r in 자료.get("정식아카이빙", []):
            # 실패한 건은 빼지 않는다. 다시 시도할 기회를 준다.
            if r.get("id") and not str(r.get("결과", "")).startswith("실패"):
                본.add(r["id"])
    return 본


def main() -> int:
    if len(sys.argv) < 2:
        print("사용법: pick.py <날짜> [정식건수]", file=sys.stderr)
        return 2
    날짜 = sys.argv[1]
    정식건수 = int(sys.argv[2]) if len(sys.argv) > 2 else 12

    폴더 = os.path.join(HERE, 날짜)
    수집경로 = os.path.join(폴더, "_수집.json")
    if not os.path.exists(수집경로):
        print(f"❌ 수집 파일 없음: {수집경로}", file=sys.stderr)
        return 1

    자료 = json.load(open(수집경로, encoding="utf-8"))
    항목 = 자료["항목"]
    if not 항목:
        print("❌ 항목이 0건", file=sys.stderr)
        return 1

    # --- 후보 선정: 전문이 있는 것 중 점수순, 출처 쏠림 방지, 지난날 정리분 제외
    기정리 = 이미정리한것(날짜)
    쓴출처: dict[str, int] = {}
    후보 = []
    걸러낸수 = 0
    for it in 항목:
        if it.get("본문상태") != "확인 완료" or not it.get("본문파일"):
            continue
        if it["id"] in 기정리:
            걸러낸수 += 1
            continue
        키 = it["출처"].split(" r/")[0].split(" @")[0]
        if 쓴출처.get(키, 0) >= 출처당상한:
            continue
        쓴출처[키] = 쓴출처.get(키, 0) + 1
        후보.append(it)
        if len(후보) >= 정식건수:
            break

    with open(os.path.join(폴더, "_후보.json"), "w", encoding="utf-8") as f:
        json.dump({"날짜": 날짜, "건수": len(후보), "항목": 후보}, f,
                  ensure_ascii=False, indent=2)

    # --- 브리핑 입력: 전 항목을 출처 묶음으로
    묶음: dict[str, list[dict]] = {}
    for it in 항목:
        묶음.setdefault(it["출처"], []).append(it)

    후보ID = {c["id"] for c in 후보}
    줄 = [f"# {날짜} AI 뉴스 수집 결과 — 총 {len(항목)}건", "",
          f"정식 아카이빙 후보 {len(후보)}건은 아래 목록에서 `★` 로 표시했다.",
          "전문은 `{날짜}/원문/<id>.md` 에 있다.", ""]
    for 출처 in sorted(묶음, key=lambda k: -max(i["점수"] for i in 묶음[k])):
        묶 = sorted(묶음[출처], key=lambda x: -x["점수"])
        줄.append(f"## {출처} ({len(묶)}건)")
        for it in 묶:
            표 = "★ " if it["id"] in 후보ID else ""
            요약 = (it.get("요약") or "").replace("\n", " ")[:200]
            줄.append(f"- {표}**{it['제목']}**")
            줄.append(f"  - id: `{it['id']}` · 점수 {it['점수']} · 반응 {it['반응']} · 발행 {it['발행'] or '미상'}")
            줄.append(f"  - {it['url']}")
            if 요약:
                줄.append(f"  - 요약: {요약}")
            if it.get("본문파일"):
                줄.append(f"  - 전문: `{it['본문파일']}`")
        줄.append("")

    with open(os.path.join(폴더, "_브리핑입력.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(줄))

    print(f"후보 {len(후보)}건 / 전체 {len(항목)}건 "
          f"(지난 {지난날확인}일간 이미 정리한 것 {걸러낸수}건 제외) → _후보.json, _브리핑입력.md")
    if not 후보:
        print("❌ 전문이 확보된 항목이 하나도 없다", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
