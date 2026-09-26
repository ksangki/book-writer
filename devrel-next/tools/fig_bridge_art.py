#!/usr/bin/env python3
"""결론 그림 10-2 — GPT 삽화(글자 없음) 위에 라벨을 얹은 SVG.
사용법: python3 fig_bridge_art.py <삽화 jpg> [출력 svg]"""
import base64, pathlib, sys
src = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else pathlib.Path(__file__).resolve().parent.parent / 'figures' / 'fig-10-2.svg'
W, H = 1672, 941
INK, PLUM, CORAL, MUTED = '#231a2e', '#4a3a5e', '#d4553a', '#6b5f76'
F = "font-family=\"Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif\""
o = [f'<image href="data:image/jpeg;base64,{base64.b64encode(src.read_bytes()).decode()}" x="0" y="0" width="{W}" height="{H}"/>']
def t(x, y, s, size, fill=INK, w=700, anchor='middle'):
    o.append(f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
def pill(x, y, w, h, stroke=PLUM, op=.92):
    o.append(f'<rect x="{x-w/2}" y="{y}" width="{w}" height="{h}" rx="{h/2 if h < 40 else 12}" fill="#fffdf9" fill-opacity="{op}" stroke="{stroke}" stroke-width="2"/>')
# 제목
t(W/2, 50, '다리와 건너편 — 건너편에 서는 사람이 늘었다', 36, INK, 800)
t(W/2, 86, "DevRel은 죽지 않았다 — '개발자 관계'에서 '만드는 사람과의 관계'로 넓어진다", 19, MUTED, 600)
# 잇는 일 네 칸 (삽화 속 장면 위)
planks = [(385, '번역', '회사의 말 ↔ 만드는 사람의 말'), (645, '피드백', '막힌 곳을 모아 회사로 되돌린다'),
          (915, '신뢰', '쌓은 결과물이 믿음이 된다'), (1180, '먼저 가보기', '먼저 써 보고 길을 알려 준다')]
for x, h, d in planks:
    pill(x, 118, 250, 74, CORAL)
    t(x, 150, h, 24, INK, 800); t(x, 178, d, 15, MUTED, 600)
t(800, 272, '잇는 일 — 다리 위를 오가는 네 가지', 18, CORAL, 800)
# 무엇으로 — 기둥 셋
pillars = [(510, '에이전트가 읽는', '정확한 문서'), (780, '관계형', '커뮤니티'), (1060, '만든', '증거')]
for x, a, b in pillars:
    pill(x, 778, 190, 62, PLUM)
    t(x, 803, a, 15, MUTED, 700); t(x, 827, b, 20, INK, 800)
pill(780, 858, 330, 38, PLUM, .85); t(780, 884, '무엇으로 — 다리를 받치는 재료', 18, PLUM, 800)
# 왼쪽
pill(110, 455, 150, 40, PLUM); t(110, 482, '회사 · 제품', 18, INK, 800)
# 누구와 — 오른쪽 무리
pill(1500, 200, 300, 40, PLUM); t(1500, 227, '누구와 — 건너편이 넓어졌다', 18, PLUM, 800)
t(1498, 590, '오른쪽 무리', 15, PLUM, 800)
o.append(f'<rect x="1340" y="600" width="316" height="132" rx="12" fill="#fffdf9" fill-opacity=".93" stroke="{PLUM}" stroke-width="2"/>')
rows = [(PLUM, '자주 옷', '전문 개발자 (예전부터)'), (CORAL, '코랄 옷', '빌더 · 회사 안 동료 (새로 선 사람)'), ('#9a8fb0', '로봇', '에이전트 (문서를 읽는 새 독자)')]
for i, (c, k, v) in enumerate(rows):
    y = 632 + i * 36
    o.append(f'<circle cx="1362" cy="{y-6}" r="8" fill="{c}"/>')
    t(1378, y, k, 15, INK, 800, 'start'); t(1440, y, v, 14.5, INK, 600, 'start')
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" '
       f'aria-label="다리와 건너편 — 다리 위 네 칸은 잇는 일(번역·피드백·신뢰·먼저 가보기), 기둥 셋은 무엇으로(에이전트가 읽는 정확한 문서·관계형 커뮤니티·만든 증거), 건너편 무리는 누구와(전문 개발자·빌더·에이전트·회사 안 동료)">'
       + ''.join(o) + '</svg>')
out.write_text(svg, encoding='utf-8'); print('wrote', out, len(svg) // 1024, 'KB')
