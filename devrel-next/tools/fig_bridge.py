#!/usr/bin/env python3
"""결론 형상화 그림 — '다리는 그대로, 건너편이 넓어졌다' (fig-10-2.svg).
누구와(건너편 사람들) · 무엇으로(다리를 받치는 기둥) · 잇는 일(다리 상판 네 칸)."""
import pathlib, sys
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / 'figures' / 'fig-10-2.svg'
INK, PLUM, PLUM_S, CORAL, CORAL_S, MUTED, BG = '#231a2e', '#4a3a5e', '#e6dff0', '#e8664a', '#fbe1d8', '#8a7d99', '#fbf7f2'
F = "font-family=\"Pretendard, 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif\""
o = []
def t(x, y, s, size=16, fill=INK, w=500, anchor='middle'):
    o.append(f'<text x="{x}" y="{y}" {F} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
def person(x, y, fill=PLUM, tag=None):
    o.append(f'<circle cx="{x}" cy="{y-58}" r="13" fill="{fill}"/>')
    o.append(f'<path d="M{x-17},{y} v-26 a17,17 0 0 1 34,0 v26 z" fill="{fill}"/>')
    if tag == 'pencil':
        o.append(f'<rect x="{x+16}" y="{y-44}" width="6" height="26" rx="2" fill="{CORAL}" transform="rotate(30 {x+19} {y-31})"/>')
    if tag == 'badge':
        o.append(f'<rect x="{x-7}" y="{y-24}" width="14" height="10" rx="2" fill="#fff"/>')
def robot(x, y):
    o.append(f'<line x1="{x}" y1="{y-78}" x2="{x}" y2="{y-68}" stroke="{CORAL}" stroke-width="3"/><circle cx="{x}" cy="{y-80}" r="4" fill="{PLUM}"/>')
    o.append(f'<rect x="{x-15}" y="{y-68}" width="30" height="24" rx="6" fill="{CORAL}"/>')
    o.append(f'<circle cx="{x-6}" cy="{y-56}" r="3.2" fill="#fff"/><circle cx="{x+6}" cy="{y-56}" r="3.2" fill="#fff"/>')
    o.append(f'<rect x="{x-17}" y="{y-40}" width="34" height="40" rx="7" fill="{CORAL}"/>')

W, H, G = 1280, 660, 380          # 폭·높이·지면 높이
o.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')
t(640, 50, '다리와 건너편 — 건너편에 서는 사람이 늘었다', 28, INK, 800)
t(640, 82, "DevRel은 죽지 않았다 — '개발자 관계'에서 '만드는 사람과의 관계'로 넓어진다", 16, MUTED, 500)
# 물
for i, yy in enumerate((560, 590, 620)):
    o.append(f'<path d="M0,{yy} ' + ' '.join(f'q30,-10 60,0 t60,0' for _ in range(11)) + f'" fill="none" stroke="{PLUM_S}" stroke-width="3"/>')
# 양쪽 언덕
o.append(f'<path d="M0,{G} H250 L220,{H} H0 Z" fill="{PLUM_S}"/>')
o.append(f'<path d="M905,{G} H{W} V{H} H935 Z" fill="{PLUM_S}"/>')
# 왼쪽: 회사·제품
o.append(f'<rect x="50" y="{G-150}" width="150" height="150" rx="8" fill="{PLUM}"/>')
o.append(f'<path d="M40,{G-150} L125,{G-205} L210,{G-150} Z" fill="{PLUM}"/>')
for r in range(3):
    for c in range(3):
        o.append(f'<rect x="{72+c*40}" y="{G-128+r*38}" width="24" height="22" rx="3" fill="#fbe1d8" opacity=".85"/>')
t(125, G+34, '회사 · 제품', 18, INK, 700)
# 다리를 받치는 기둥 = 무엇으로
pillars = [(350, '에이전트가 읽는', '정확한 문서'), (570, '관계형', '커뮤니티'), (790, '만든', '증거')]
for x, a, b in pillars:
    o.append(f'<path d="M{x-62},{G+18} L{x-72},{H-110} H{x+72} L{x+62},{G+18} Z" fill="{PLUM}"/>')
    t(x, G+86, a, 15, '#fff', 600); t(x, G+108, b, 17, '#fff', 800)
t(570, H-72, '무엇으로 — 다리를 받치는 재료', 16, PLUM, 800)
# 상판 = 잇는 일 (네 칸)
o.append(f'<rect x="240" y="{G-4}" width="670" height="26" rx="4" fill="{INK}"/>')
planks = ['번역', '피드백', '신뢰', '먼저 가보기']
pw = 660 / 4
for i, s in enumerate(planks):
    x0 = 245 + i * pw
    o.append(f'<rect x="{x0+6}" y="{G-58}" width="{pw-12}" height="48" rx="10" fill="{CORAL_S}" stroke="{CORAL}" stroke-width="2.5"/>')
    t(x0 + pw/2, G-27, s, 19, INK, 800)
t(575, G-78, '잇는 일 — 다리 위를 오가는 네 가지', 16, CORAL, 800)
# 양방향 화살표
o.append(f'<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{CORAL}"/></marker></defs>')
o.append(f'<line x1="290" y1="{G-108}" x2="860" y2="{G-108}" stroke="{CORAL}" stroke-width="3" marker-start="url(#ah)" marker-end="url(#ah)"/>')
# 오른쪽: 누구와 — 보라=예전부터, 주황=새로 선 사람
person(965, G, PLUM); t(965, G+34, '전문 개발자', 14, INK, 700); t(965, G+52, '(예전부터)', 12, MUTED)
person(1045, G, CORAL, 'pencil'); t(1045, G+34, '빌더', 14, INK, 700)
robot(1130, G); t(1130, G+34, '에이전트', 14, INK, 700)
person(1215, G, CORAL, 'badge'); t(1215, G+34, '회사 안 동료', 14, INK, 700)
t(1090, G-140, '누구와 — 건너편에 서는 사람이 늘었다', 16, PLUM, 800)
o.append(f'<path d="M1005,{G-118} Q1130,{G-96} 1250,{G-118}" fill="none" stroke="{CORAL}" stroke-width="2" stroke-dasharray="4 4"/>')
t(1090, G+84, '보라: 예전부터 · 주황: 새로 선 사람', 13, MUTED, 600)
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="다리와 건너편">' + ''.join(o) + '</svg>'
OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text(svg, encoding='utf-8'); print('wrote', OUT)
