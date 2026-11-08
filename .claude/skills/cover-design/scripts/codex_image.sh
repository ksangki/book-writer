#!/usr/bin/env bash
# 로컬 Codex CLI의 이미지 생성 기능(GPT 이미지 모델)으로 표지·삽화 한 장을 그린다. ChatGPT 웹을 거치지 않는다.
# 사용: codex_image.sh <prompt.md> <out.png> [WxH]
#   <prompt.md> 그림 지시문. 제목·부제·저자처럼 공개될 글자와 그림 묘사만 넣는다 (사내 정보·실명·미공개 수치 금지)
#   <out.png>   결과를 둘 경로 (부모 폴더가 있어야 한다). 이미 있으면 덮어쓰지 않고 멈춘다
#   [WxH]       Lanczos 확대 크기 (기본 1600x2400). 원본은 <out>의 이름에 _raw를 붙여 함께 남긴다
# 빈 임시 폴더에서 Codex를 workspace-write로 돌려, Codex가 프로젝트 파일을 보거나 고치지 못하게 한다.
# 한 장에 3~4분 걸린다. run_in_background로 띄우고 여러 시안은 동시에 돌려도 된다.
# 종료 코드: 0 성공 · 2 인자·입력 오류 · 3 codex 미설치 · 4 이미지가 만들어지지 않음 · 그 밖은 codex 오류
set -euo pipefail
usage() { sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
[ $# -ge 2 ] || usage
prompt=$1; out=$2; size=${3:-1600x2400}
command -v codex >/dev/null 2>&1 || { echo "codex CLI 없음 (설치: npm i -g @openai/codex), 다른 도구로 넘어감"; exit 3; }
[ -f "$prompt" ] || { echo "지시문 없음: $prompt"; exit 2; }
[ -d "$(dirname "$out")" ] || { echo "출력 폴더 없음: $(dirname "$out")"; exit 2; }
[ -e "$out" ] && { echo "이미 있음, 덮어쓰지 않음: $out (먼저 백업하거나 다른 이름을 쓴다)"; exit 2; }
features=$(codex features list 2>/dev/null || true)   # grep -q로 파이프를 일찍 닫으면 pipefail이 실패로 본다
grep -Eq '^image_generation[[:space:]].*true' <<<"$features" \
  || { echo "codex에 image_generation 기능이 꺼져 있음, 다른 도구로 넘어감"; exit 3; }

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
{ cat "$prompt"; printf '\n\nUse your image generation tool. Save the final image into the current working directory as image.png (copy it from wherever the tool saved it) and print its path. Do not create or modify any other file.\n'; } > "$work/prompt.txt"
log="${out%.*}.log"
codex exec -s workspace-write --skip-git-repo-check -C "$work" -o "$work/last.md" - < "$work/prompt.txt" > "$log" 2>&1
[ -f "$work/image.png" ] || { echo "이미지가 만들어지지 않음. 로그: $log"; exit 4; }

raw="${out%.*}_raw.png"
cp "$work/image.png" "$raw"
if command -v magick >/dev/null 2>&1; then
  magick "$raw" -filter Lanczos -resize "$size" -strip "$out"
else
  cp "$raw" "$out"; echo "ImageMagick 없음, 확대하지 않고 원본 크기로 저장"
fi
echo "생성 완료: $out (원본 $raw, 로그 $log)"
