#!/usr/bin/env python3
"""「DevRel Next」 v1.1.0 그림 렌더러 — figure_specs.md의 사양을 SVG로.
출력: devrel-next/figures/fig-{장}-{k}.svg  (editor가 조립 시 전권 연번으로 캡션을 바꾼다)
사용법: python3 figures.py [id ...]   (인자 없으면 전부)
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from figlib import Fig, INK, MUTED, CORAL, CORAL_SOFT, PLUM, PLUM_SOFT, LINE, CARD

OUT = pathlib.Path(__file__).resolve().parent.parent / 'figures'
OUT.mkdir(exist_ok=True)
FIGS = {}


def fig(fid, title):
    def deco(fn):
        FIGS[fid] = (title, fn)
        return fn
    return deco


def timeline_h(f, y, events, x0=90, x1=910, hi=None, label_w=150):
    """가로 연표: events=[(date,label,sub)]. 위/아래 교대, 블록은 위에서 아래로 정확히 쌓는다."""
    f.line(x0 - 30, y, x1 + 30, y, INK, 2.2)
    n = len(events)
    for i, (d, lab, sub) in enumerate(events):
        x = x0 + (x1 - x0) * (i / (n - 1) if n > 1 else 0.5)
        acc = hi is not None and i == hi
        f.dot(x, y, 9 if acc else 7, acc)
        items = [(d, 15, CORAL if acc else PLUM, 700, None), (lab, 15, INK, 700 if acc else 600, label_w)]
        if sub:
            items.append((sub, 12.5, MUTED, 400, label_w))
        up = i % 2 == 0
        if up:
            hgt = f.block(x, 0, items, measure=True)
            top = y - 22 - hgt
            f.line(x, y - 10, x, y - 20, LINE, 1.6)
        else:
            top = y + 22
            f.line(x, y + 10, x, y + 20, LINE, 1.6)
        f.block(x, top, items)


# ───────────────────────── 1장 ─────────────────────────
@fig('1-1', '2023~2026년 DevRel 당사자들이 남긴 글')
def f11():
    ev = [  # (날짜, 인물, 요지, 유형)  유형: 작별 / 진단 / 반론
        ('2023-07-25', 'David Neal', '"My role has been eliminated"', '작별'),
        ('2023-11-28', 'Alexander Reelsen', 'DevRel을 떠나며, "cost center"', '작별'),
        ('2024-02-05', 'Joey deVilla', 'Okta 해고 기록', '작별'),
        ('2024-02-09', 'Daniel Bryant', '"overblown"', '반론'),
        ('2024-03-07', 'Sam Julien', '"isn\'t dead, it\'s just evolving"', '반론'),
        ('2024-07', 'swyx', '거품 교정론', '진단'),
        ('2024-07-17', 'Keith Casey', '자기 실패론', '진단'),
        ('2024-10-30', 'Liz Acosta', '번아웃으로 떠남', '작별'),
        ('2024-12-10', 'Lee Briggs', '재구조화론', '진단'),
        ('2025-10', 'swyx', '부활론', '반론'),
        ('2026-01 초', 'Marcos Placona', '2026 예측', '진단'),
        ('2026-05-27', 'Raymond Camden', '해고', '작별'),
        ('2026-06-23', 'Justin Poehnelt', '해고 기록', '작별'),
        ('2026-07-02', 'Salma Alam-Naylor', '"Goodbye, forever, probably."', '작별'),
        ('2026-07-06', 'Joey deVilla', 'DevRelCon 발표 초록', '진단'),
        ('2026-09-14', 'r/devrel', '"headcount version"', '진단'),
    ]
    row = 44
    f = Fig(1000, 150 + row * len(ev))
    f.text(500, 40, '2023~2026년, DevRel 당사자들이 남긴 글', 21, INK, 700)
    cols = {'작별': CORAL, '진단': PLUM, '반론': '#3f7f6e'}
    lx = 300
    for k, (name, c) in enumerate(cols.items()):
        x = lx + k * 150
        f.add(f'<circle cx="{x}" cy="78" r="7" fill="{c}"/>')
        f.text(x + 14, 78, {'작별': '작별·이탈', '진단': '진단·예측', '반론': '반론'}[name], 14, MUTED, anchor='start')
    y0, ax = 118, 300
    f.line(ax, y0 - 10, ax, y0 + row * (len(ev) - 1) + 10, LINE, 2.4)
    for i, (d, who, what, kind) in enumerate(ev):
        y = y0 + i * row
        acc = who.startswith('Salma')
        f.add(f'<circle cx="{ax}" cy="{y}" r="{9 if acc else 6.5}" fill="{cols[kind]}"/>')
        f.text(ax - 22, y, d, 14.5, CORAL if acc else MUTED, 700 if acc else 400, anchor='end')
        f.text(ax + 22, y, who, 15.5, INK, 700, anchor='start')
        f.text(ax + 22 + 170, y, what, 14.5, INK if acc else MUTED, 400, anchor='start')
    return f


@fig('1-2', '당사자들이 말한 측정 압박의 경로')
def f12():
    f = Fig(1000, 350)
    f.text(500, 38, '당사자들이 말한 측정 압박의 경로', 21, INK, 700)
    boxes = [('역할 정의가 흐릿함', None), ('기여를 측정하기 어려움', None),
             ('비용 센터로 보임', None), ('감원 때 먼저 축소', None)]
    notes = ['Julien 2024 · DRF 2024-09', 'Casey 2024 · Reddington 13명 중 2명', 'Reelsen 2023']
    w, h, gap, y = 196, 86, 46, 130
    x = 38
    xs = []
    for i, (lab, _) in enumerate(boxes):
        f.box(x, y, w, h, lab, accent=(i == 3), size=17)
        xs.append(x)
        x += w + gap
    for i in range(3):
        xa, xb = xs[i] + w, xs[i + 1]
        f.arrow(f'M{xa + 4},{y + h / 2} L{xb - 6},{y + h / 2}')
        f.block((xa + xb) / 2, y + h + 18, [(notes[i], 13, MUTED, 400, 150)])
    f.text(500, 318, '여러 당사자의 글이 공통으로 가리키는 진단이며, 인과를 입증한 자료는 아니다', 13.5, MUTED)
    return f


# ───────────────────────── 3장 ─────────────────────────
@fig('3-1', '최종 사용자 프로그래밍에서 바이브 코딩까지')
def f31():
    f = Fig(1000, 440)
    f.text(500, 38, '최종 사용자 프로그래밍에서 바이브 코딩까지', 21, INK, 700)
    timeline_h(f, 235, [
        ('2005', 'Scaffidi 등의 추정', '2012년 미국: 자칭 프로그래머 1,300만+ · 전문 300만 미만'),
        ('2011', 'Ko 등 서베이', '"대부분의 프로그램은 전문 개발자가 쓰지 않는다"'),
        ('2025-02-02', 'Karpathy "vibe coding"', '트윗 한 줄'),
        ('2025-11-06', 'Collins 올해의 단어', None),
        ('2026-01', 'Hacker News', '"another wave of end-user programming"'),
    ], hi=2, label_w=175)
    return f


@fig('3-2', 'DevRel이 마주한 청중의 띠')
def f32():
    f = Fig(1000, 400)
    f.text(500, 38, 'DevRel이 마주한 청중의 띠', 21, INK, 700)
    x0, x1, y = 110, 890, 150
    f.add(f'<rect x="{x0 - 30}" y="{y - 14}" width="{x1 - x0 + 60}" height="28" rx="14" fill="{PLUM_SOFT}"/>')
    pts = ['자연어로 첫 앱을 띄운 빌더', '코드를 거의 안 보는 바이브 코더',
           '생성 결과를 검토·수정하는 사람', 'AI를 매일 쓰며 결과를 의심하는 전문 개발자']
    for i, p in enumerate(pts):
        x = x0 + (x1 - x0) * i / 3
        f.dot(x, y, 9)
        f.text(x, y + 58, p, 15, INK, 600, max_w=170)
    f.text(x0 - 10, y - 42, '빌더 도구의 고객', 15, PLUM, 700, anchor='start')
    f.text(x0 - 10, y - 20 - 44, 'Lovable · Replit · Bolt · v0', 12.5, MUTED, anchor='start')
    f.text(x1 + 10, y - 42, '전문 개발자 도구의 고객', 15, PLUM, 700, anchor='end')
    f.text(x1 + 10, y - 64, 'Claude Code · Cursor · Copilot', 12.5, MUTED, anchor='end')
    f.add(f'<rect x="{x0 - 30}" y="300" width="{x1 - x0 + 60}" height="52" rx="12" fill="{CORAL_SOFT}" stroke="{CORAL}" stroke-width="2.5"/>')
    f.text(500, 326, '같은 문서·튜토리얼·행사가 띠 전체에 닿는다', 17, INK, 700)
    return f


# ───────────────────────── 4장 ─────────────────────────
@fig('4-1', '에이전트를 위한 표준·제품 타임라인(2024-09~2025-12)')
def f41():
    ev = [('2024-09-03', 'llms.txt 제안', 'Jeremy Howard'),
          ('2024-11-25', 'MCP 발표', 'Anthropic'),
          ('2025-01-28', 'Agent Experience 명명', 'Mathias Biilmann'),
          ('2025-04-04', 'GitHub 공식 MCP 서버', '퍼블릭 프리뷰'),
          ('2025-04-07', 'Cloudflare 원격 MCP 서버', None),
          ('2025-08-06', 'Vercel MCP', '퍼블릭 베타'),
          ('2025-08', '카카오 PlayMCP', '베타'),
          ('2025-12-09', 'Agentic AI Foundation 결성', 'Linux Foundation')]
    row = 54
    f = Fig(1000, 110 + row * len(ev))
    f.text(500, 40, '에이전트를 위한 표준·제품 타임라인', 21, INK, 700)
    ax, y0 = 330, 96
    f.line(ax, y0 - 10, ax, y0 + row * (len(ev) - 1) + 10, LINE, 2.4)
    for i, (d, what, who) in enumerate(ev):
        y = y0 + i * row
        acc = i == len(ev) - 1
        f.dot(ax, y, 9 if acc else 7, acc)
        f.text(ax - 24, y, d, 15, CORAL if acc else MUTED, 700 if acc else 400, anchor='end')
        f.text(ax + 24, y, what, 16, INK, 700, anchor='start')
        if who:
            f.text(ax + 24 + 300, y, who, 14, MUTED, anchor='start')
    return f


@fig('4-2', '사용자 경험의 계보 — Biilmann의 UX·DX·AX에 Lawson의 정의와 가장 가까운 학술 개념을 더해')
def f42():
    f = Fig(1000, 360)
    f.text(500, 34, '사용자 경험의 계보', 21, INK, 700)
    f.text(500, 62, 'Biilmann의 UX·DX·AX에 Lawson의 정의와 가장 가까운 학술 개념을 더해', 13.5, MUTED)
    y, w, h = 110, 210, 96
    xs = [70, 395, 720]
    labs = [('UX', '1993 · Don Norman'), ('DX', '2011 · Jeremiah Lee'), ('AX', '2025 · Mathias Biilmann')]
    for i, (a, b) in enumerate(labs):
        f.box(xs[i], y, w, h, a, b, accent=(i == 2), size=24)
    f.arrow(f'M{xs[0] + w + 4},{y + h / 2} L{xs[1] - 6},{y + h / 2}')
    f.arrow(f'M{xs[1] + w + 4},{y + h / 2} L{xs[2] - 6},{y + h / 2}')
    f.text((xs[1] + w + xs[2]) / 2, y - 18, 'DX와 UX의 결합(Lawson)', 13.5, MUTED)
    f.box(720, 262, 210, 70, 'ACI', '2024 · SWE-agent 논문', soft=PLUM_SOFT, size=20)
    f.arrow(f'M825,262 L825,{y + h + 8}', dash=True)
    f.text(640, 290, '가장 가까운 학술 개념', 13.5, MUTED, anchor='end')
    return f


# ───────────────────────── 6장 ─────────────────────────
@fig('6-1', 'DevRel이라는 이름을 떠난 공개 기록들')
def f61():
    f = Fig(1000, 520)
    f.text(500, 38, 'DevRel이라는 이름을 떠난 공개 기록들', 21, INK, 700)
    f.box(60, 228, 190, 80, 'DevRel', accent=True, size=22)
    items = [('기술 직무로', 'Member of Technical Staff — cameron.stream · Staff Engineer — Salma'),
             ('고객·매출 쪽으로', 'Sales Engineer — Lee Briggs'),
             ('가르치는 일로', 'Cursor AI 교육 — Lee Robinson'),
             ('이야기 쓰는 일로', 'Fly.io 공고 "closer to a journalist"'),
             ('청중을 다시 정의', 'AI Power Users DevRel — Dona Sarkar')]
    y = 78
    for lab, sub in items:
        f.box(430, y, 510, 70, lab, sub, size=16)
        f.arrow(f'M250,268 C340,268 340,{y + 35} 424,{y + 35}')
        y += 84
    f.text(500, 502, '스스로 공개한 기록만 모았다 — 대표성 없음', 13.5, MUTED)
    return f


@fig('6-2', '한 번에 닿는 사람의 수로 놓아본 직함들')
def f62():
    f = Fig(1000, 380)
    f.text(500, 38, '한 번에 닿는 사람의 수로 놓아본 직함들', 21, INK, 700)
    x0, x1, y = 130, 870, 180
    f.arrow(f'M{x0 - 40},{y} L{x1 + 50},{y}', width=2.2)
    f.text(x0 - 40, y + 30, '적음', 14, MUTED, anchor='start')
    f.text(x1 + 50, y + 30, '많음', 14, MUTED, anchor='end')
    pts = [('FDE · Applied AI', '고객 한 곳 안으로'),
           ('제품 팀 안의 DevRel Engineer', 'Vercel — 출시 전에 먼저 부딪힘'),
           ('DevRel · DX Engineer', '공개 문서·데모로 다수의 개발자와 에이전트에게')]
    for i, (a, b) in enumerate(pts):
        x = x0 + (x1 - x0) * i / 2
        f.dot(x, y, 10)
        f.text(x, y - 56, a, 16, INK, 700, max_w=230)
        f.text(x, y - 30, b, 13, MUTED, max_w=240)
    f.add(f'<rect x="{x0 - 40}" y="258" width="{x1 - x0 + 90}" height="52" rx="12" fill="{CORAL_SOFT}" stroke="{CORAL}" stroke-width="2.5"/>')
    f.text(500, 284, '되돌려주기 — 제품·엔지니어링 팀으로 피드백', 16.5, INK, 700)
    f.text(500, 346, '2026년 9월 25일 공고 문구 기준', 13, MUTED)
    return f


# ───────────────────────── 7장 ─────────────────────────
@fig('7-1', '네 가지 기능이 맞물리는 순서')
def f71():
    f = Fig(1000, 300)
    f.text(500, 38, '네 가지 기능이 맞물리는 순서', 21, INK, 700)
    labs = ['먼저 가보기', '번역', '피드백 루프', '신뢰']
    notes = ['먼저 가본 사람이 번역한다', '번역한 것을 되돌린다', '쌓인 결과물이 신뢰가 된다']
    w, h, gap, y = 190, 84, 60, 110
    x = 45
    xs = []
    for i, lab in enumerate(labs):
        f.box(x, y, w, h, lab, accent=(i == 0), size=19)
        xs.append(x)
        x += w + gap
    for i in range(3):
        xa, xb = xs[i] + w, xs[i + 1]
        f.arrow(f'M{xa + 4},{y + h / 2} L{xb - 6},{y + h / 2}')
        f.text((xa + xb) / 2, y + h + 40, notes[i], 13.5, MUTED, max_w=200)
    f.text(500, 278, '먼저 가보기가 나머지 셋을 떠받친다', 14, CORAL, 700)
    return f


@fig('7-2', '리더가 차례로 답할 세 질문')
def f72():
    f = Fig(1000, 470)
    f.text(500, 38, '리더가 차례로 답할 세 질문', 21, INK, 700)
    qs = ['① 어느 기능이 병목인가', '② 어느 조직에 붙일까', '③ 무엇을 만든 증거로 볼까']
    ys = [80, 205, 330]
    for i, q in enumerate(qs):
        f.box(50, ys[i], 330, 80, q, accent=(i == 0), size=18)
    for i in range(2):
        f.arrow(f'M215,{ys[i] + 80 + 4} L215,{ys[i + 1] - 6}')
    ex = [('먼저 가보기 → 제품 조직', 150), ('번역 → 문서·교육', 245), ('피드백 루프 → 제품 관리', 340)]
    f.text(700, 120, '예시 배치', 14, MUTED, 700)
    for lab, yy in ex[:2]:
        pass
    for j, lab in enumerate(['먼저 가보기 → 제품 조직', '번역 → 문서·교육', '피드백 루프 → 제품 관리']):
        yy = 150 + j * 52
        f.box(560, yy - 22, 340, 44, lab, soft=PLUM_SOFT, size=15, rx=10)
        f.line(380, 245, 560, yy, LINE, 1.6, dash=True)
    f.box(560, 330 + 40, 340, 70, '배포된 앱 · 성공한 API 호출', '고쳐진 버그 · 줄어든 지원 문의', soft=PLUM_SOFT, size=15, rx=10)
    f.text(730, 358, '예시 증거', 14, MUTED, 700)
    f.line(380, 370, 560, 405, LINE, 1.6, dash=True)
    return f


# ───────────────────────── 9장 ─────────────────────────
@fig('9-1', '사내 AI 확산 설계의 세 다이얼')
def f91():
    f = Fig(1000, 420)
    f.text(500, 38, '사내 AI 확산 설계의 세 다이얼 — 강도·측정·공유 장치', 21, INK, 700)
    rows = [('강도', ['권유', '성과평가 반영', '채용·해고']),
            ('측정', ['사용량', '사용해서 만든 결과', '그로 인해 달라진 것']),
            ('공유 장치', ['없음', '공유 채널', '사례 양식'])]
    y = 110
    for r, (name, ticks) in enumerate(rows):
        acc = r == 1
        f.add(f'<rect x="40" y="{y - 40}" width="760" height="80" rx="14" fill="{CORAL_SOFT if acc else CARD}" stroke="{CORAL if acc else LINE}" stroke-width="{2.5 if acc else 1.8}"/>')
        f.text(110, y, name, 19, INK, 700)
        x0, x1 = 250, 700
        f.line(x0, y, x1, y, PLUM, 2.2)
        for k, t in enumerate(ticks):
            x = x0 + (x1 - x0) * k / 2
            f.dot(x, y, 7, acc)
            f.text(x, y + 24, t, 14.5, INK, 600, max_w=180)
        y += 110
    f.add(f'<path d="M820,70 Q850,70 850,110 L850,300 Q850,330 820,330" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    f.text(915, 200, '세 줄의 조합 = 한 조직의 확산 설계', 15, INK, 700, max_w=110)
    f.text(420, 398, '눈금의 좋고 나쁨은 표시하지 않았다 — 효과를 비교한 연구가 없다', 13.5, MUTED)
    return f


@fig('9-2', '강도를 올리고 사용량을 세면 생기는 일')
def f92():
    f = Fig(1000, 560)
    f.text(500, 38, '강도를 올리고 사용량을 세면 생기는 일', 21, INK, 700)
    chain = [('강도 다이얼을 올림', None), ('측정이 사용량에 머묾', None), ('사용량이 평가와 이어짐', None),
             ('사용량을 연기함', '토큰·LOC 리더보드, "biggest AI champion"'), ('감시로 읽힘 · 냉소', None)]
    y = 70
    for i, (a, b) in enumerate(chain):
        f.box(90, y, 400, 66, a, b, size=17)
        if i < len(chain) - 1:
            f.arrow(f'M290,{y + 66 + 4} L290,{y + 92 - 6}')
        y += 92
    f.box(600, 150, 330, 100, '사용량은 진단에만', '\'만든 증거\'를 나란히 둔다', accent=True, size=18)
    f.arrow('M490,191 C540,191 550,200 594,200', dash=True, accent=True)
    f.text(760, 280, '첫 줄에 무엇을 올리나', 14, MUTED)
    return f


# ───────────────────────── 10장 ─────────────────────────
@fig('10-1', '1장의 네 이야기와 새 출발점 하나에서 이어지는 네 전망')
def f101():
    f = Fig(1000, 520)
    f.text(500, 38, '출발점 다섯, 전망 넷', 21, INK, 700)
    srcs = ['거품 교정론', '자기 실패론', '재구조화론', '부활론', '8·9장의 사내 확산 사례']
    outs = ['교정론', '해체론', '확장론', '내향론']
    sy = [90, 170, 250, 330, 410]
    oy = [110, 250, 330, 410]
    for i, s in enumerate(srcs):
        f.box(40, sy[i], 250, 60, s, soft=PLUM_SOFT if i < 4 else CARD, size=16)
    for i, o in enumerate(outs):
        f.box(420, oy[i], 200, 60, o, accent=(i == 3), size=18)
    links = [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3)]
    for s, o in links:
        lab = '측정 문제로 흡수' if s == 1 else None
        f.arrow(f'M290,{sy[s] + 30} C355,{sy[s] + 30} 355,{oy[o] + 30} 414,{oy[o] + 30}')
        if lab:
            f.text(352, sy[s] + 52, lab, 13, MUTED)
    f.box(740, 230, 220, 90, '관찰 지표와 반대 의견', soft=CARD, size=16)
    for i in range(4):
        f.arrow(f'M620,{oy[i] + 30} C680,{oy[i] + 30} 680,275 734,275')
    f.text(165, 488, '1장의 네 이야기 + 새 출발점', 13.5, MUTED)
    f.text(520, 488, '10장의 네 전망', 13.5, MUTED)
    return f


# ───────────────────────── 2장 ─────────────────────────
@fig('2-1', '경계 역할로서의 DevRel')
def f21():
    f = Fig(1000, 560)
    f.text(500, 38, '경계 역할로서의 DevRel', 21, INK, 700)
    cx, cy = 500, 300
    f.box(cx - 120, cy - 45, 240, 90, 'DevRel', '경계 역할', accent=True, size=22)
    nodes = [(20, cy - 45, '외부 개발자', '서드파티·커뮤니티', '질문·불만·사용 사례', 'L'),
             (cx - 130, 70, '제품·엔지니어링', None, '피드백 번역·요구사항', 'T'),
             (780, cy - 45, '마케팅', None, '메시지·캠페인', 'R'),
             (cx - 130, 450, '영업', None, '기술 검증·도입 지원', 'B')]
    for x, y, a, b, lab, side in nodes:
        w = 200 if side in 'LR' else 260
        f.box(x, y, w, 90 if side in 'LR' else 70, a, b, size=18)
        if side == 'L':
            f.arrow(f'M{x + w + 6},{cy} L{cx - 126},{cy}', both=True); f.text((x + w + cx - 120) / 2, cy - 22, lab, 13, MUTED, max_w=140)
        elif side == 'R':
            f.arrow(f'M{cx + 126},{cy} L{x - 6},{cy}', both=True); f.text((cx + 120 + x) / 2, cy - 22, lab, 13, MUTED, max_w=140)
        elif side == 'T':
            f.arrow(f'M{cx},{y + 76} L{cx},{cy - 51}', both=True); f.text(cx + 14, (y + 70 + cy - 45) / 2, lab, 13.5, MUTED, anchor='start')
        else:
            f.arrow(f'M{cx},{cy + 51} L{cx},{y - 6}', both=True); f.text(cx + 14, (cy + 45 + y) / 2, lab, 13.5, MUTED, anchor='start')
    return f


@fig('2-2', 'DevRel 측정 틀의 계보')
def f22():
    ev = [('2012', 'DX 정의', 'Fagerholm & Münch'),
          ('2016', 'AAARRRP', 'Leggetter, DevRelCon London — 회사 유형별 목표'),
          ('2019-11', 'Orbit Model', '"Communities aren\'t funnels" — Love × Reach'),
          ('2019-12', 'DevRel Qualified Leads', 'Thengvall — 사내 팀에 연결한 사람'),
          ('2021', 'Developer Journey Map', 'Lewko & Parton — 개발자의 여정'),
          ('2021', 'SPACE', 'Forsgren 외, ACM Queue 잡지 기고 — 단일 지표 불가'),
          ('2021', 'CHAOSS 연구', 'Goggins 외 — 건강과 지속 가능성'),
          ('2023', 'DevEx', 'Noda 외, ACM Queue 잡지 기고 — 피드백 루프·인지 부하·몰입'),
          ('2024-04-11', 'Orbit, Postman 인수 발표', '틀을 만든 회사가 독립 제품으로 남지 못한 장면')]
    row = 54
    f = Fig(1000, 110 + row * len(ev))
    f.text(500, 40, 'DevRel 측정 틀의 계보', 21, INK, 700)
    ax, y0 = 230, 96
    f.line(ax, y0 - 10, ax, y0 + row * (len(ev) - 1) + 10, LINE, 2.4)
    for i, (d, what, sub) in enumerate(ev):
        y = y0 + i * row
        acc = i == len(ev) - 1
        f.dot(ax, y, 9 if acc else 7, acc)
        f.text(ax - 24, y, d, 15, CORAL if acc else MUTED, 700 if acc else 400, anchor='end')
        f.text(ax + 24, y - 9, what, 16, INK, 700, anchor='start')
        f.text(ax + 24, y + 12, sub, 13, MUTED, anchor='start')
    return f


# ───────────────────────── 5장 ─────────────────────────
@fig('5-1', '문서가 유료 제품의 입구였던 Tailwind의 퍼널에 코딩 에이전트가 끼어든 자리')
def f51():
    f = Fig(1000, 420)
    f.text(500, 38, 'Tailwind의 퍼널에 끼어든 코딩 에이전트', 21, INK, 700)
    xs, y, w, h = [40, 290, 540, 790], 90, 180, 70
    labs = ['개발자', '문서 사이트 방문', '유료 제품을 알게 됨', '고객']
    for i, l in enumerate(labs):
        f.box(xs[i], y, w, h, l, size=17)
        if i:
            f.arrow(f'M{xs[i - 1] + w + 4},{y + h / 2} L{xs[i] - 6},{y + h / 2}')
    f.text(500, y + h + 26, 'Wathan: "The docs are the only way people find out about our commercial products …"', 13, MUTED)
    f.box(290, 270, 430, 76, '코딩 에이전트가 Tailwind 클래스를 대신 씀', accent=True, size=17)
    f.arrow(f'M130,{y + h + 4} C130,300 200,308 284,308', accent=True)
    f.text(146, 236, '문서 방문 없이 채택', 13.5, CORAL, 700, anchor='start')
    f.arrow(f'M505,270 L{380},{y + h + 42}', dash=True)
    f.text(560, 236, '방문 기록이 남지 않음', 13.5, MUTED, anchor='start')
    f.text(500, 392, '에이전트 경로는 이 책의 해석 — Wathan은 원인을 AI의 영향으로만 말했다', 13, MUTED)
    return f


@fig('5-2', '개발자·검색 크롤러·LLM — 세 유통 표면과 두 퍼널')
def f52():
    f = Fig(1000, 460)
    f.text(500, 38, '세 유통 표면과 두 퍼널', 21, INK, 700)
    f.box(40, 190, 200, 86, 'DevRel 콘텐츠·자산', size=17)
    mids = [('사람 개발자', 90), ('검색 크롤러', 190), ('LLM·코딩 에이전트', 290)]
    for i, (l, y) in enumerate(mids):
        f.box(360, y, 230, 76, l, '양쪽 퍼널로 보낸다' if i == 1 else None, accent=(i == 1), size=17)
        f.arrow(f'M240,233 C300,233 300,{y + 38} 354,{y + 38}')
    f.box(700, 110, 260, 96, 'human funnel', '영상·워크숍·서사 → 신뢰', soft=PLUM_SOFT, size=18)
    f.box(700, 260, 260, 96, 'machine funnel', '문서·레퍼런스·MCP → 정확성', soft=PLUM_SOFT, size=18)
    for (sy, ty) in [(128, 158), (228, 158), (228, 308), (328, 308)]:
        f.arrow(f'M590,{sy} C645,{sy} 645,{ty} 694,{ty}')
    return f


# ───────────────────────── 8장 ─────────────────────────
@fig('8-1', 'DevRel의 활동이 사내 AI 확산의 장치로 옮겨간 자리')
def f81():
    rows = [('정기 밋업', '매주 세션 · 격주 사내 밋업', 'Block · 토스 · Duolingo'),
            ('해커톤', '전사 AI 해커톤 · 빌더 위크', 'Zapier · Atlassian · Canva'),
            ('핸즈온 워크숍 · 오피스아워', '사내 워크숍 · 15분 오피스아워', 'Intuit 공고 · Duolingo'),
            ('앰배서더 프로그램', '사내 챔피언 · 애드버킷 네트워크', 'GitHub · Microsoft · Block'),
            ('에반젤리스트', '조직별 AI 에반젤리스트', 'LINE Plus'),
            ('커뮤니티 사례 모으기', '사례 공유 채널 · Show & Tell', '카카오 · Zapier · 당근'),
            ('청중 맞춤 번역', '메시지 초점을 코드에서 결과로', 'Block'),
            ('데모', '챔피언을 만드는 데모', 'Anthropic 공고 문구')]
    f = Fig(1000, 170 + 72 * len(rows) + 80)
    f.text(500, 38, 'DevRel의 활동이 사내 확산 장치로 옮겨간 자리', 21, INK, 700)
    f.text(230, 92, 'DevRel이 바깥에서 하던 일', 16, PLUM, 700)
    f.text(770, 92, '사내 AI 확산의 장치', 16, PLUM, 700)
    y = 120
    for a, b, src in rows:
        f.box(60, y, 340, 54, a, size=16)
        f.box(600, y, 340, 54, b, src, size=16)
        f.line(400, y + 27, 600, y + 27, MUTED, 1.4)
        y += 72
    f.add(f'<rect x="60" y="{y + 10}" width="880" height="54" rx="12" fill="{CORAL_SOFT}" stroke="{CORAL}" stroke-width="2.5"/>')
    f.text(500, y + 37, '여러 회사의 공개 기록에 기댄 대응 — 수치는 모두 자체 보고, 효과를 비교한 연구는 없다', 15.5, INK, 700)
    return f


@fig('8-2', '먼저 가보기·함께 배우기·보여주기·되돌려주기 — 청중이 동료로 옮겨갈 때')
def f82():
    f = Fig(1000, 560)
    f.text(500, 38, '네 동사 — 청중이 동료로 옮겨갈 때', 21, INK, 700)
    cx, cy, r = 500, 300, 150
    pos = {'g': (cx, cy - r), 'l': (cx + r, cy), 's': (cx, cy + r), 'f': (cx - r, cy)}
    labs = {'g': '먼저 가보기', 'l': '함께 배우기', 's': '보여주기', 'f': '되돌려주기'}
    import math
    ang = {'g': -90, 'l': 0, 's': 90, 'f': 180}
    for a, b in [('g', 'l'), ('l', 's'), ('s', 'f'), ('f', 'g')]:
        a0 = math.radians(ang[a] + 30); a1 = math.radians((ang[b] if ang[b] > ang[a] else ang[b] + 360) - 30)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        f.arrow(f'M{x0:.1f},{y0:.1f} A{r},{r} 0 0 1 {x1:.1f},{y1:.1f}', width=2.4)
    for k2, (x, y) in pos.items():
        f.box(x - 80, y - 28, 160, 56, labs[k2], accent=(k2 == 'g'), size=17)
    notes = [(cx, cy - r - 60, '청중: 외부 개발자 → 동료', True),
             (cx, cy + r + 58, '관찰 가능성·시험 가능성 (Rogers)', False),
             (cx - r - 90, cy + 62, '피드백 번역: 제품팀 → 도입 담당·경영진', False)]
    for x, y, t, acc in notes:
        f.text(x, y, t, 14.5, CORAL if acc else MUTED, 700 if acc else 400, max_w=230)
    return f


if __name__ == '__main__':
    ids = sys.argv[1:] or list(FIGS)
    for fid in ids:
        title, fn = FIGS[fid]
        (OUT / f'fig-{fid}.svg').write_text(fn().svg(title), encoding='utf-8')
        print('wrote', f'fig-{fid}.svg')
