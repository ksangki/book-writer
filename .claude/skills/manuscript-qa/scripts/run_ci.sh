#!/usr/bin/env bash
# 원고 CI(manuscript-ci) 실행기 — 설치 위치를 찾아 check / check-build를 돌린다.
# 사용법: run_ci.sh check <04_manuscript.md>      정적 점검(LLM 없음) → <slug>/ci_report.md
#         run_ci.sh check-build <책.epub>          빌드 산출물 점검 → 결과를 stdout
# 찾는 순서: $MANUSCRIPT_CI_HOME(소스 체크아웃) → PATH의 manuscript-ci → ~/source/github/manuscript-ci
# 어디에도 없으면 종료 코드 3으로 "건너뜀"을 알린다(오케스트레이터가 완료 보고에 적는다).
set -uo pipefail
usage() { echo "usage: run_ci.sh check|check-build <file>" >&2; exit 2; }
[ $# -eq 2 ] || usage
mode="$1"; target="$2"
[ -f "$target" ] || { echo "run_ci.sh: 파일이 없다 — $target" >&2; exit 2; }
run() {
  if [ -n "${MANUSCRIPT_CI_HOME:-}" ] && [ -d "$MANUSCRIPT_CI_HOME/src/manuscript_ci" ]; then
    (cd "$MANUSCRIPT_CI_HOME" && PYTHONPATH=src python3 -m manuscript_ci.cli "$@")
  elif command -v manuscript-ci >/dev/null 2>&1; then
    manuscript-ci "$@"
  elif [ -d "$HOME/source/github/manuscript-ci/src/manuscript_ci" ]; then
    (cd "$HOME/source/github/manuscript-ci" && PYTHONPATH=src python3 -m manuscript_ci.cli "$@")
  else
    echo "manuscript-ci를 찾지 못했다 — 건너뜀 (pip install git+https://github.com/ksangki/manuscript-ci.git 또는 MANUSCRIPT_CI_HOME 지정)" >&2
    return 3
  fi
}
dir="$(cd "$(dirname "$target")" && pwd)"; abs="$dir/$(basename "$target")"
case "$mode" in
  check)
    out="$(run check "$abs" 2>&1)"; code=$?
    [ $code -eq 3 ] && { echo "$out" >&2; exit 3; }
    out="$(echo "$out" | sed "s|$dir/||g")"          # 로컬 절대 경로를 보고서에 남기지 않는다
    report="$dir/ci_report.md"
    { echo "# 원고 CI 정적 점검 — $(date +%F)"; echo; echo '```'; echo "$out"; echo '```'; echo;
      echo "## 규칙별 건수"; echo "$out" | grep -oE '^\[[a-z-]+\]' | sort | uniq -c | sed 's/^/- /'; } > "$report"
    echo "ci check: exit $code · $(echo "$out" | grep -cE '^\[') findings → $report"
    exit $code ;;
  check-build)
    run check-build "$abs"; exit $? ;;
  *) usage ;;
esac
