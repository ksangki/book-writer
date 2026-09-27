#!/usr/bin/env python3
"""{slug}/figures/figures.py 의 출발점 — 복사해서 쓴다.

사용법: BOOK_MANIFEST={slug}/book_manifest.json python3 {slug}/figures/figures.py [id ...]
출력:   {slug}/figures/fig-{장}-{k}.svg   (인자가 없으면 전부)
그림마다 @fig('N-k', '제목') 함수를 하나 두고, 자주 쓰는 세 모양(흐름·격자·순환)은 아래 헬퍼를 쓴다.
"""
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(sys.argv[0]).resolve().parent))          # 책 폴더에 figlib 사본이 있으면 우선
sys.path.insert(1, '.claude/skills/book-figures/scripts')                     # 책 폴더에 figlib 사본이 없고, 하네스 루트에서 실행할 때만 쓰인다
from figlib import Fig, INK, MUTED, ACCENT, ACCENT_SOFT, SECOND, SECOND_SOFT, LINE, CARD

OUT = pathlib.Path(sys.argv[0]).resolve().parent
FIGS = {}


def fig(fid, title):
    def deco(fn):
        FIGS[fid] = (title, fn)
        return fn
    return deco


def chain(f, y, items, x0=60, w=260, h=100, gap=40, accent_idx=None, size=18):
    """가로 흐름: items=[(제목, 설명)] 상자를 화살표로 잇는다."""
    for i, (a, b) in enumerate(items):
        x = x0 + i * (w + gap)
        f.box(x, y, w, h, a, b, accent=(i == accent_idx), size=size)
        if i < len(items) - 1:
            f.arrow(f'M{x + w + 4},{y + h / 2} L{x + w + gap - 4},{y + h / 2}')


def grid(f, x0, y0, cells, cols=2, w=420, h=90, gx=40, gy=24, size=17):
    """격자: cells=[(제목, 설명, 강조여부)]."""
    for i, (a, b, acc) in enumerate(cells):
        r, c = divmod(i, cols)
        f.box(x0 + c * (w + gx), y0 + r * (h + gy), w, h, a, b, accent=acc, size=size)


def cycle(f, cx, cy, r, labels, w=190, h=64, close=True, size=16):
    """순환: labels를 원 위에 두고 시계 방향 화살표로 잇는다(close=False면 마지막→처음 생략)."""
    n = len(labels)
    pts = [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * i / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * i / n)) for i in range(n)]
    for i in range(n if close else n - 1):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1; d = math.hypot(dx, dy)
        f.arrow(f'M{x1 + dx / d * 70:.1f},{y1 + dy / d * 40:.1f} L{x2 - dx / d * 70:.1f},{y2 - dy / d * 40:.1f}')
    for (x, y), lab in zip(pts, labels):
        f.box(x - w / 2, y - h / 2, w, h, lab, size=size)


@fig('1-1', '예시 — 세 단계 흐름')
def f11():
    f = Fig(1000, 260)
    f.text(500, 40, '예시 — 세 단계 흐름', 21, INK, 700)
    chain(f, 100, [('보이게', '목록을 한 화면에'), ('고르게', '무엇을 남길지'), ('합치게', '겹치는 것부터')], accent_idx=0)
    return f


if __name__ == '__main__':
    ids = sys.argv[1:] or list(FIGS)
    for fid in ids:
        title, fn = FIGS[fid]
        (OUT / f'fig-{fid}.svg').write_text(fn().svg(title), encoding='utf-8')
        print('wrote', f'fig-{fid}.svg')
