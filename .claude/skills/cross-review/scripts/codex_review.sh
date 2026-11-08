#!/usr/bin/env bash
# 로컬 Codex CLI로 원고·삽화를 읽기 전용 교차 검토한다.
# 사용: codex_review.sh <review_dir> <prompt.md> <out.md> [image ...]
#   <review_dir> Codex에게 보여 줄 것만 모은 검토 전용 폴더 (원고 사본·diff·연구 발췌·전송 가능한 저자 사실 목록)
#                Codex는 이 폴더를 작업 폴더로, 읽기 전용으로 연다. 프로젝트 전체를 넘기지 않는다.
#   <prompt.md>  검토 지시문
#   <out.md>     Codex 마지막 메시지를 저장할 경로 (부모 폴더가 있어야 한다)
#   [image]      첨부할 이미지(jpg·jpeg·png·webp). 없는 파일은 건너뛰고, 하나도 없으면 -i를 붙이지 않는다
# 종료 코드: 0 성공 · 2 인자·입력 오류 · 3 codex 미설치 · 그 밖은 codex 오류
set -euo pipefail
usage() { sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
[ $# -ge 3 ] || usage
review=$1; prompt=$2; out=$3; shift 3
command -v codex >/dev/null 2>&1 || { echo "codex CLI 없음, 교차 검토 건너뜀 (설치: npm i -g @openai/codex)"; exit 3; }
[ -d "$review" ] || { echo "검토 폴더 없음: $review"; exit 2; }
[ -f "$prompt" ] || { echo "지시문 없음: $prompt"; exit 2; }
[ -d "$(dirname "$out")" ] || { echo "출력 폴더 없음: $(dirname "$out")"; exit 2; }
review=$(cd "$review" && pwd -P)
outdir=$(cd "$(dirname "$out")" && pwd -P); out="$outdir/$(basename "$out")"
args=(exec -s read-only --skip-git-repo-check -C "$review" -o "$out")   # 검토 폴더는 git 저장소가 아니다
imgs=()
for img in "$@"; do
  case "$(printf %s "$img" | tr "[:upper:]" "[:lower:]")" in *.jpg|*.jpeg|*.png|*.webp) ;; *) echo "이미지 형식 아님, 건너뜀: $img"; continue;; esac
  [ -f "$img" ] && imgs+=(-i "$img") || echo "이미지 없음, 건너뜀: $img"
done
codex "${args[@]}" ${imgs[@]+"${imgs[@]}"} - < "$prompt" > "${out%.*}.log" 2>&1
echo "codex 검토 완료: $out (로그 ${out%.*}.log, 이미지 $(( ${#imgs[@]} / 2 ))장)"
