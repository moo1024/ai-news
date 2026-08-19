#!/usr/bin/env bash
# 매일 1회: AI 뉴스 수집 → 노션 아카이빙(원문 정본 + 정리본) → 브리핑 한 장 → git.
# cron 이 부르지만 손으로 `bash daily.sh` 해도 똑같이 돈다.
#
#   bash daily.sh              오늘 + 최근 3일 중 미처리분 따라잡기
#   bash daily.sh 2026-08-17   그 날짜만 강제로 다시 처리
#
# 뉴스는 시간이 지나면 원문이 사라지므로 대화백업(7일)보다 따라잡기 범위를 짧게 잡았다.
set -uo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$HERE/logs"
DONE_DIR="$HERE/.done"
BACKFILL_DAYS=3
# 변수명에 한글을 쓰지 마라. 배시는 ASCII 이름만 받아서 `$정식건수` 가 확장되지 않고
# 문자 그대로 넘어간다 (2026-08-19 첫 크론이 이걸로 통째로 실패했다).
PICK_N=12

# cron 은 로그인 셸이 아니라 nvm PATH 를 모른다. 전부 절대경로로 박는다.
CLAUDE_BIN="/home/lmh/.nvm/versions/node/v24.18.0/bin/claude"
# 수집기는 X(syndication) 때문에 curl_cffi 가 필요하다. insane-search 의 venv 를 빌린다.
COLLECT_PY="/home/lmh/insane-search-copy/.venv/bin/python"

# 두 세션이 같은 날짜를 동시에 만지면 노션에 중복이 생긴다.
LOCK="/home/lmh/.ai-news.lock"
if [[ -e "$LOCK" ]] && kill -0 "$(cat "$LOCK" 2>/dev/null)" 2>/dev/null; then
  echo "이미 돌고 있다 (PID $(cat "$LOCK")) — 종료"
  exit 0
fi
echo $$ > "$LOCK"
trap 'rm -f "$LOCK"' EXIT

mkdir -p "$LOG_DIR" "$DONE_DIR"
LOG="$LOG_DIR/$(date '+%Y-%m-%d').log"
exec > >(tee -a "$LOG") 2>&1

echo "===== $(date '+%Y-%m-%d %H:%M:%S') 시작 ====="

for 실행파일 in "$CLAUDE_BIN" "$COLLECT_PY"; do
  if [[ ! -x "$실행파일" ]]; then
    echo "❌ 실행파일 없음: $실행파일 — 중단"
    exit 1
  fi
done

process_day() {
  local target="$1"
  echo
  echo "--- [$target] 1) 수집 ---"
  if ! timeout 1800 "$COLLECT_PY" "$HERE/collect.py" "$target"; then
    echo "❌ [$target] 수집 실패 — 미완료로 남김"
    return 1
  fi

  echo "--- [$target] 2) 선별 ---"
  if ! python3 "$HERE/pick.py" "$target" "$PICK_N"; then
    echo "❌ [$target] 선별 실패 — 미완료로 남김"
    return 1
  fi

  echo "--- [$target] 3) 노션 아카이빙 ---"
  # acceptEdits 는 MCP 도구를 자동 승인하지 않는다. 노션 도구를 하나씩 명시해야 한다.
  # 전역 권한을 넓히지 않으려고 여기서만, 필요한 것만 연다. (삭제 계열은 뺐다)
  rm -f "$HERE/$target/_archived.json"
  timeout 3000 "$CLAUDE_BIN" -p "$HERE/ARCHIVE.md 의 절차를 그대로 따라 $target 날짜의 AI 뉴스를 노션에 아카이빙하라. 대상 폴더는 $HERE/$target 이다. 후보 전건을 2단계(원문 정본 + 정리본)로 처리하고, 마지막에 _archived.json 을 반드시 남겨라. 절차서의 '하지 말 것'을 지켜라." \
    --permission-mode acceptEdits \
    --allowedTools \
      "Read" "Glob" "Grep" "Write" \
      "mcp__plugin_Notion_notion__notion-fetch" \
      "mcp__plugin_Notion_notion__notion-search" \
      "mcp__plugin_Notion_notion__notion-create-pages" \
      "mcp__plugin_Notion_notion__notion-update-page" \
      "mcp__plugin_Notion_notion__notion-query-data-sources" \
    2>&1 | tail -60
  echo "--- [$target] 아카이빙 종료 ---"

  # claude -p 는 일을 못 해도 exit 0 이다. 산출물로 판정한다.
  if ! python3 "$HERE/verify_day.py" "$target"; then
    echo "❌ [$target] 검증 실패 — 미완료로 남김, 다음 실행이 재시도한다"
    return 1
  fi

  touch "$DONE_DIR/$target"
  return 0
}

cd "$HERE" || exit 1
FAILED=0

if [[ -n "${1:-}" ]]; then
  rm -f "$DONE_DIR/$1"
  process_day "$1" || FAILED=1
else
  # 오래된 날짜부터 처리해야 노션에 시간 순으로 쌓인다.
  for ((i = BACKFILL_DAYS; i >= 0; i--)); do
    D=$(date -d "$i days ago" '+%Y-%m-%d')
    [[ -f "$DONE_DIR/$D" ]] && continue
    process_day "$D" || FAILED=1
  done
fi

echo
echo "--- 4) git 백업 ---"
if [[ -d "$HERE/.git" ]]; then
  git -C "$HERE" add -A
  if git -C "$HERE" diff --cached --quiet; then
    echo "변경 없음 — 커밋 안 함"
  else
    N=$(git -C "$HERE" diff --cached --name-only | wc -l)
    git -C "$HERE" -c user.email=knugori2025@gmail.com -c user.name=lmh \
      commit -q -m "$(date '+%Y-%m-%d %H:%M') AI 뉴스 (${N}개 파일)"
    echo "커밋 완료 — ${N}개 파일"
  fi
else
  echo "git 저장소 아님 — 백업 건너뜀"
fi

# 로그는 60일, 원문은 120일치만 남긴다. 정본은 노션에 있으므로 로컬은 캐시다.
find "$LOG_DIR" -name '*.log' -mtime +60 -delete 2>/dev/null
find "$HERE" -maxdepth 1 -type d -name '20*-*-*' -mtime +120 -exec rm -rf {} + 2>/dev/null

echo "===== $(date '+%Y-%m-%d %H:%M:%S') 종료 (실패=$FAILED) ====="
exit $FAILED
