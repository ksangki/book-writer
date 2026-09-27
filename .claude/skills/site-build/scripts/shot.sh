#!/usr/bin/env bash
# 화면 확인용 캡처 — 헤드리스 Chrome으로 HTML/SVG를 PNG로 찍는다.
# 사용법: shot.sh <파일.html|파일.svg> <출력.png> [폭x높이=1440x900] [슬라이드 번호]
#   슬라이드 번호를 주면 덱에서 그 장만 보이게 해서 찍는다(#sN). 임시 파일은 끝나면 지운다.
# Chrome이 없으면 종료 코드 2 — 호출한 쪽은 캡처만 건너뛰고 보고한다.
set -uo pipefail
[ $# -ge 2 ] || { echo "usage: shot.sh <file> <out.png> [WxH] [slide]" >&2; exit 2; }
src="$1"; out="$2"; size="${3:-1440x900}"; n="${4:-}"
w="${size%x*}"; h="${size#*x}"
chrome=""
for c in "${CHROME_BIN:-}" "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "$(command -v google-chrome 2>/dev/null)" "$(command -v chromium 2>/dev/null)"; do
  [ -n "$c" ] && [ -x "$c" ] && { chrome="$c"; break; }
done
[ -n "$chrome" ] || { echo "shot.sh: Chrome/Chromium을 찾지 못했다 — 캡처 건너뜀 (CHROME_BIN으로 지정)" >&2; exit 2; }
mkdir -p "$(dirname "$out")"; rm -f "$out"
target="$src"; tmp=""
if [ -n "$n" ]; then
  tmp="$(mktemp "$(dirname "$src")/.shot_XXXXXX")"; mv "$tmp" "$tmp.html"; tmp="$tmp.html"   # 상대 경로(../figures)가 살도록 같은 폴더에
  trap 'rm -f "$tmp"' EXIT
  sed "s|</style>|.slide{display:none!important}#s$n{display:flex!important}body{height:auto;overflow:visible}</style>|" "$src" > "$tmp"
  target="$tmp"
fi
url="file://$(cd "$(dirname "$target")" && pwd)/$(basename "$target")"
perl -e 'alarm 60; exec @ARGV' "$chrome" --headless=new --disable-gpu --hide-scrollbars --window-size="$w,$h" --screenshot="$out" "$url" >/dev/null 2>&1
[ -s "$out" ] && echo "shot: $out" || { echo "shot.sh: 캡처 실패 — $src" >&2; exit 1; }
