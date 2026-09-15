# ai-news

A daily pipeline that collects AI news from ~26 sources, decides what is worth keeping, writes it
up in Korean, and files it into a Notion knowledge base — then checks that it actually landed
before marking the day done.

Runs on cron three times a day. Built with [Claude Code](https://claude.com/claude-code).

```
collect.py  →  pick.py  →  ARCHIVE.md (claude -p)  →  verify_day.py  →  .done
  ~150 items    12 finalists   two-stage Notion write    proof it landed
```

| File | Role |
|---|---|
| `sources.json` | Source list and scoring knobs. **The only file you edit to tune the pipeline** |
| `collect.py` | Scrapes and writes files. Calls no LLM |
| `pick.py` | Splits ~150 collected items into briefing input + 12 archive candidates |
| `ARCHIVE.md` | The procedure `claude -p` reads and executes to write into Notion |
| `verify_day.py` | Confirms the pages exist. `.done` is only stamped if this passes |
| `daily.sh` | Runs the above in order. Cron entry point |

## Two things that turned out to matter

**Scoring alone silences the topics you care about most.** Ranking purely by score meant
Claude Code and Codex news scored zero slots for two days running — outweighed by official-blog
source weights. Nine items were collected and none made the twelve. The fix needed three knobs
together, not one: a score multiplier (1.3), a floor of reserved slots (4), *and* a ceiling (6).
Multiplier alone made it 12 of 12; reserved slots alone let four GitHub repos eat every reserved
seat.

**Verification is a separate stage for a reason.** A write that returns success is not a page that
exists. `verify_day.py` reads back what should be there, and the day is only closed when it is.

---

<details>
<summary><b>운영 문서 (한국어)</b></summary>

    bash ~/ai-news/daily.sh              # 오늘 + 최근 3일 미처리분
    bash ~/ai-news/daily.sh 2026-08-17   # 그 날짜만 다시

## 노션 어디에 쌓이나

- 원문 정본 → 📄 Source Library
- 정리본 → 🤖 클로드·AI 자동화 지식 (`원본자료` 릴레이션으로 원문과 연결)
- 하루치 브리핑 → 📰 AI 뉴스 브리핑 DB (📚 도서관 하위, 날짜·건수로 정렬)

DB 식별자는 `ARCHIVE.md` 에 있다.

## 실측으로 얻은 것 (2026-08-18)

- **Jina Reader 는 파이썬 클라이언트를 403 으로 막는다.** urllib·curl_cffi 둘 다 실패, `curl` 바이너리만 200
- **anthropic.com 은 RSS 를 폐지했다.** 구글뉴스 `site:` 검색으로 대체
- **Reddit `.json` 은 WAF 403, `.rss` 만 통한다.** 그마저 병렬로 때리면 통째로 429 → 순차 5초 간격
- **X 는 `created_at` 포맷이 오락가락한다.** 트윗 ID(snowflake)에서 시각을 뽑는 게 정확
- **본문 확보 예산을 점수순으로만 쓰면 X 가 다 먹는다.** 출처당 4건 상한을 먼저 건다

## 관심주제 — 왜 따로 자리를 떼어주나 (2026-08-19)

점수만으로 뽑으면 **클로드코드·Codex 소식이 매일 0건**이 된다. 공식 블로그 가중치(2.0)에
밀려서다. 이틀 연속 실측으로 확인했다 — 수집은 9건 됐는데 후보 12건에 하나도 못 들어갔다.

| 손잡이 | 값 | 뜻 |
|---|---|---|
| `배수` | 1.3 | 낱말이 걸리면 점수에 곱한다 |
| `예약자리` | 4 | 후보 12칸 중 **최소** 이만큼은 관심주제 |
| `상한` | 6 | **최대** 이만큼. 없으면 12칸이 통째로 덮인다(실측) |

세 개를 다 걸어야 균형이 잡힌다. 배수만 키웠더니 12/12가 관심주제가 됐고,
예약만 걸었더니 깃헙 레포 4개가 그 자리를 다 먹었다(예약 단계는 출처당 2건 상한).

**튜닝은 `sources.json` 에서만 한다.**

## 뜨는 깃헙 레포·스킬은 어떻게 찾나

트렌딩 페이지는 공식 API 가 없다. 대신 **검색 API 의 `created:>날짜` + 별순 정렬**이
사실상 같은 답을 준다 — "최근 만들어졌는데 별이 많이 붙은" = 뜨는 것.

```
GET api.github.com/search/repositories?q=<질의>+created:><날짜>&sort=stars&order=desc
```

질의 4갈래(claude-code · topic:mcp · topic:ai-agents · agent skills). 무인증 60req/hr 이라
요청 사이 2초를 쉰다. **설명이 20자 미만인 레포는 버린다** — 별만 많고 정리본을 쓸 수 없다.
`weight` 를 1.05 로 낮게 둔 이유는 레포가 '기사'가 아니라 '떡밥'이라서다.

</details>
