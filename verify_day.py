#!/usr/bin/env python3
"""아카이빙이 실제로 됐는지 판정한다.

    python3 verify_day.py <날짜>

왜 필요한가: `claude -p` 는 일을 못 해도 exit 0 으로 끝난다(설명만 하고 종료).
종료코드를 믿지 말고 산출물로 판정해야 한다.

통과 조건
  1. `_archived.json` 이 있고 JSON 으로 읽힌다
  2. 브리핑 페이지 URL 이 있다
  3. `_후보.json` 의 모든 id 가 `정식아카이빙` 배열에 있다
  4. 후보의 절반 이상이 `생성` 또는 `중복` 이다 (전부 실패면 통과시키지 않는다)
"""
from __future__ import annotations

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    if len(sys.argv) < 2:
        print("사용법: verify_day.py <날짜>", file=sys.stderr)
        return 2
    날짜 = sys.argv[1]
    폴더 = os.path.join(HERE, 날짜)

    후보경로 = os.path.join(폴더, "_후보.json")
    결과경로 = os.path.join(폴더, "_archived.json")

    if not os.path.exists(후보경로):
        print(f"❌ 후보 파일 없음: {후보경로}")
        return 1
    if not os.path.exists(결과경로):
        print(f"❌ 결과 파일 없음: {결과경로} — 아카이빙 세션이 아무것도 안 남겼다")
        return 1

    후보 = json.load(open(후보경로, encoding="utf-8"))["항목"]
    try:
        결과 = json.load(open(결과경로, encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"❌ _archived.json 이 JSON 이 아니다: {e}")
        return 1

    브리핑 = (결과.get("브리핑페이지") or "").strip()
    if not 브리핑.startswith("http"):
        print(f"❌ 브리핑 페이지 URL 이 없다: {브리핑!r}")
        return 1

    기록 = {r.get("id"): r for r in 결과.get("정식아카이빙", [])}
    빠짐 = [c["id"] for c in 후보 if c["id"] not in 기록]
    if 빠짐:
        print(f"❌ 후보 {len(빠짐)}건이 결과에 없다: {', '.join(빠짐[:5])}")
        return 1

    생성 = [r for r in 기록.values() if str(r.get("결과", "")).startswith("생성")]
    중복 = [r for r in 기록.values() if "중복" in str(r.get("결과", ""))]
    실패 = [r for r in 기록.values() if str(r.get("결과", "")).startswith("실패")]

    # 새로 만든 건 2단계가 다 있어야 한다. 한쪽만 있으면 껍데기다.
    반쪽 = [r for r in 생성
            if not (str(r.get("source_library", "")).startswith("http")
                    and str(r.get("서고", "")).startswith("http"))]
    if 반쪽:
        print(f"❌ 2단계가 덜 된 행 {len(반쪽)}건 (Source Library 또는 서고 링크 없음): "
              f"{', '.join(r.get('id', '?') for r in 반쪽[:5])}")
        return 1

    성공수 = len(생성) + len(중복)
    if 성공수 * 2 < len(후보):
        print(f"❌ 성공 {성공수}/{len(후보)} — 절반도 못 했다. 실패 {len(실패)}건")
        for r in 실패[:5]:
            print(f"   - {r.get('id')}: {r.get('결과')}")
        return 1

    print(f"✅ 검증 통과 — 생성 {len(생성)} · 중복 {len(중복)} · 실패 {len(실패)} / 후보 {len(후보)}")
    print(f"   브리핑: {브리핑}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
