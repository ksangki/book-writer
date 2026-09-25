"""그림 공용 도구 — 「DevRel Next」 v1.1.0.
표지 팔레트(자주 잉크 + 코랄 강조 + 크림 종이)로 EPUB·웹 공용 SVG를 그린다.
XHTML 호환: <foreignObject> 없이 <text>/<tspan>만 쓴다 (epubcheck RSC-005 회피).
"""
from xml.sax.saxutils import escape

PAPER = '#fbf7f2'
CARD = '#fffdfa'
LINE = '#ddd2dc'
INK = '#2a2033'
MUTED = '#6f6479'
CORAL = '#d4604a'       # 밝은 바탕에서의 코랄(대비 확보용으로 표지보다 한 톤 짙게)
CORAL_SOFT = '#f7ddd5'
PLUM = '#5b4470'
PLUM_SOFT = '#ebe3f0'
FONT = "Pretendard,'Apple SD Gothic Neo','Noto Sans KR',sans-serif"


def _w(ch):
    """글자 폭 근사 (한글·전각 1.0, 라틴·숫자 0.56)."""
    return 1.0 if ord(ch) > 0x2E80 else (0.3 if ch == ' ' else 0.56)


def text_width(s, size):
    return sum(_w(c) for c in s) * size


def wrap(s, size, max_w):
    """어절 단위 줄바꿈 (keep-all)."""
    words, lines, cur = s.split(' '), [], ''
    for wd in words:
        cand = (cur + ' ' + wd).strip()
        if cur and text_width(cand, size) > max_w:
            lines.append(cur)
            cur = wd
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return lines


class Fig:
    def __init__(self, w, h):
        self.w, self.h, self.parts = w, h, []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=16, fill=INK, weight=400, anchor='middle', max_w=None, lh=1.35):
        lines = wrap(s, size, max_w) if max_w else [s]
        y0 = y - (len(lines) - 1) * size * lh / 2
        spans = ''.join(
            f'<tspan x="{x:.1f}" y="{y0 + i * size * lh:.1f}">{escape(l)}</tspan>'
            for i, l in enumerate(lines))
        self.add(f'<text fill="{fill}" font-size="{size}" font-weight="{weight}" '
                 f'text-anchor="{anchor}" dominant-baseline="middle">{spans}</text>')
        return len(lines)

    def block(self, x, top, items, lh=1.35, gap=4, anchor='middle', measure=False):
        """items=[(text,size,fill,weight,max_w)]를 위에서 아래로 쌓는다. 끝 y를 돌려준다."""
        y = top
        for (s, size, fill, weight, max_w) in items:
            lines = wrap(s, size, max_w) if max_w else [s]
            for l in lines:
                y += size * lh
                if not measure:
                    self.add(f'<text x="{x:.1f}" y="{y - size * 0.3:.1f}" fill="{fill}" font-size="{size}" '
                             f'font-weight="{weight}" text-anchor="{anchor}">{escape(l)}</text>')
            y += gap
        return y

    def box(self, x, y, w, h, label, sub=None, accent=False, soft=None, size=17, rx=12):
        fill = soft or (CORAL_SOFT if accent else CARD)
        stroke = CORAL if accent else LINE
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="{2.5 if accent else 1.8}"/>')
        cy = y + h / 2
        if sub:
            self.text(x + w / 2, cy - size * 0.55, label, size, INK, 700, max_w=w - 20)
            self.text(x + w / 2, cy + size * 0.75, sub, min(size - 3.5, 14.5), MUTED, 400, max_w=w - 20)
        else:
            self.text(x + w / 2, cy, label, size, INK, 700, max_w=w - 20)

    def arrow(self, d, accent=False, label=None, lx=None, ly=None, dash=False, both=False, width=None):
        col = CORAL if accent else INK
        mk = 'mc' if accent else 'mi'
        extra = ' stroke-dasharray="6 5"' if dash else ''
        start = f' marker-start="url(#{mk})"' if both else ''
        self.add(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width or (3 if accent else 2)}"'
                 f'{extra} marker-end="url(#{mk})"{start}/>')
        if label:
            self.text(lx, ly, label, 14, MUTED)

    def line(self, x1, y1, x2, y2, col=LINE, width=1.8, dash=False):
        extra = ' stroke-dasharray="5 5"' if dash else ''
        self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{width}"{extra}/>')

    def dot(self, x, y, r=7, accent=False):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CORAL if accent else PLUM}"/>')

    def svg(self, title):
        defs = (
            '<defs>'
            f'<marker id="mi" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="{INK}"/></marker>'
            f'<marker id="mc" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" fill="{CORAL}"/></marker>'
            '</defs>')
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" '
                f'role="img" aria-label="{escape(title)}" font-family="{FONT}">'
                f'<title>{escape(title)}</title>{defs}'
                f'<rect width="{self.w}" height="{self.h}" fill="{PAPER}"/>'
                + ''.join(self.parts) + '</svg>')
