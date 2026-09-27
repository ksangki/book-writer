#!/usr/bin/env python3
"""발표자료 엔진 — 책 한 권을 1시간 발표용 단일 HTML 덱으로.

모든 책의 덱이 같은 규약으로 나오게 하는 공용 모듈이다: 표지(표지 그림 포함) · PART 구분면 ·
진행바 · 페이지 번호 · 슬라이드마다 '쉽게 말하면' 비유 한 줄(ez) · 키보드 이동 · 인쇄(PDF) 스타일.
책마다 달라지는 것은 {slug}/deck/slides.py(내용)와 매니페스트의 theme(색)뿐이다.

slides.py 예 (호출: python3 {slug}/deck/slides.py <이 폴더> {slug}/site/presentation/index.html):
    import sys, pathlib
    sys.path.insert(0, sys.argv[1])
    import deck as D
    HERE = pathlib.Path(__file__).resolve().parent.parent          # {slug}/
    D.setup(slug=str(HERE))                                         # 매니페스트에서 제목·저자·판·색을 읽는다
    D.cover(eyebrow='…', title_html='들이는 <span class="coral-t">사람들</span>',
            subtitle='…', quote='"…"', quote_by='— …')
    D.quote('OPENING', '먼저 질문 하나', '…', '…'); D.ez('…')
    D.divider('PART 1', 'PART 1', '…', '…', ['1장. …', '2장. …'])
    D.figure('PART 1', '…', '…', '3-1', '그림 3-1. …', '…'); D.ez('…')
    D.end_cover(title_html='…', subtitle='…', note='…')
    D.render(sys.argv[2])

그림은 site/figures/fig-{id}.svg를 ../figures/로 참조한다(세로로 긴 그림은 자동 2단).
"""
import html, json, os, pathlib, re, sys

_S = {'slides': [], 'book': '', 'by': '', 'ver': '', 'figdir': None, 'theme': {}, 'cover_img': '../cover.png', 'cover_alt': ''}
slides = _S['slides']

DEFAULT_THEME = {'bg': '#0f1a26', 'panel': '#16222f', 'line': '#2a3a4c', 'text': '#eef1f4', 'muted': '#9fabb8',
                 'dim': '#71808f', 'accent': '#e3b35a', 'accent_d': '#b8862f', 'cream': '#f3eee2',
                 'glow': '#1a2a3c', 'figbg': '#fbf7f2'}


def setup(slug=None, book=None, by=None, ver=None, theme=None, figdir=None, cover_img='../cover.png', cover_alt=None):
    """매니페스트(<slug>/book_manifest.json)가 있으면 제목·저자·판·표지 alt·theme.deck을 거기서 읽는다."""
    m = {}
    if slug:
        p = pathlib.Path(slug) / 'book_manifest.json'
        if p.exists():
            m = json.loads(p.read_text(encoding='utf-8'))
    _S['book'] = book or (m.get('title', '') + (f" — {m['subtitle']}" if m.get('subtitle') else ''))
    _S['by'] = by or m.get('author', '')
    _S['ver'] = ver or ('v' + m['version'] if m.get('version') else '')
    _S['theme'] = {**DEFAULT_THEME, **(m.get('theme', {}).get('deck', {})), **(theme or {})}
    _S['figdir'] = pathlib.Path(figdir) if figdir else (pathlib.Path(slug) / 'figures' if slug else pathlib.Path('figures'))
    _S['cover_img'] = cover_img
    _S['cover_alt'] = html.escape(cover_alt or m.get('cover_alt') or f"「{_S['book']}」 표지", quote=True)


def motif():
    """기본 모티프: 흩어진 점이 틀 안으로 들어가 줄을 맞춘다(색은 theme.accent)."""
    a = _S['theme']['accent']
    dots = ''.join(f'<circle cx="{20 + i * 26}" cy="{30 + ((i * 7) % 9) - 4}" r="{2.5 + i * 0.25:.1f}" fill="{a}" opacity="{0.35 + i * 0.06:.2f}"/>' for i in range(10))
    grid = ''.join(f'<circle cx="{313 + c * 10}" cy="{17 + r * 10}" r="3" fill="{a}"/>' for r in range(4) for c in range(3))
    return (f'<svg class="motif" viewBox="0 0 420 60" aria-hidden="true"><line x1="0" y1="54" x2="420" y2="54" stroke="{_S["theme"]["line"]}" stroke-width="2"/>'
            f'{dots}<rect x="300" y="6" width="46" height="48" fill="none" stroke="{a}" stroke-width="3"/>{grid}</svg>')


def _corners():
    return ('<div class="corner tl"></div><div class="corner tr"></div>'
            '<div class="corner bl"></div><div class="corner br"></div>')


def cover(eyebrow, title_html, subtitle, quote='', quote_by='', meta=None, art=True):
    """첫 표지. art=True면 오른쪽에 표지 그림(세로형)을 둔다."""
    meta = meta or f"{_S['by']} · 1시간 발표"
    inner = (f'<div class="eyebrow coral">{eyebrow}</div><h1 class="cover-title">{title_html}</h1>'
             f'<p class="cover-sub">{subtitle}</p>{motif()}'
             + (f'<p class="cover-quote">{quote}</p>' if quote else '') + (f'<p class="cover-by">{quote_by}</p>' if quote_by else '')
             + f'<div class="cover-meta"><span>{meta}</span><span class="mono dim">{_S["ver"]}</span></div>')
    if art:
        body = (f'<div class="cover-wrap has-art"><div>{inner}</div>'
                f'<figure class="cover-art portrait"><img src="{_S["cover_img"]}" alt="{_S["cover_alt"]}" /></figure></div>')
    else:
        body = f'<div class="cover-wrap"><div>{inner}</div></div>'
    slides.append(('cover', 'OPENING', _corners() + body))


def end_cover(title_html, subtitle, note='', eyebrow='감사합니다'):
    inner = (f'<div class="eyebrow coral">{eyebrow}</div><h1 class="cover-title end">{title_html}</h1>'
             f'<p class="cover-sub">{subtitle}</p>{motif()}' + (f'<p class="cover-quote">{note}</p>' if note else '')
             + f'<div class="cover-meta"><span>{_S["by"]}</span><span class="mono dim">{_S["ver"]}</span></div>')
    slides.append(('cover', 'CLOSING', _corners() + f'<div class="cover-wrap"><div>{inner}</div></div>'))


def divider(sec, eyebrow, title, sub, chapters):
    ch = ''.join(f'<li>{c}</li>' for c in chapters)
    slides.append(('div', sec, f'<div class="div-wrap"><div><div class="eyebrow coral">{eyebrow}</div>'
                               f'<h2 class="div-title">{title}</h2><p class="div-sub">{sub}</p>{motif()}</div>'
                               f'<ul class="div-ch">{ch}</ul></div>'))


def _head(eyebrow, title):
    return (f'<div class="eyebrow cream">{eyebrow}</div><h2 class="content-title">{title}</h2>'
            '<div class="bar small"></div>')


def _opt(cls, s):
    return f'<p class="{cls}">{s}</p>' if s else ''


def cards(sec, eyebrow, title, items, lead=None, foot=None, cols=3):
    cs = ''.join(f'<div class="card"><div class="card-num mono">{i + 1:02d}</div>'
                 f'<div class="card-h">{h}</div><div class="card-sub">{s}</div></div>' for i, (h, s) in enumerate(items))
    slides.append(('content', sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<div class="grid grid-{cols}">{cs}</div>' + _opt('foot-note', foot)))


def quote(sec, eyebrow, title, q, src=None, after=None):
    slides.append(('content', sec, _head(eyebrow, title) + f'<blockquote class="bigq">{q}</blockquote>'
                   + _opt('q-src', src) + _opt('after', after)))


def table(sec, eyebrow, title, head, rows, lead=None, foot=None):
    th = ''.join(f'<th>{c}</th>' for c in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    slides.append(('content', sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<table class="deck-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
                   + _opt('foot-note', foot)))


def stat(sec, eyebrow, title, pairs, foot=None):
    st = ''.join(f'<div class="stat"><div class="stat-n">{n}</div><div class="stat-l">{l}</div></div>' for n, l in pairs)
    slides.append(('content', sec, _head(eyebrow, title) + f'<div class="stat-row">{st}</div>' + _opt('foot-note', foot)))


def bullets(sec, eyebrow, title, items, lead=None, foot=None):
    li = ''.join(f'<li>{i}</li>' for i in items)
    slides.append(('content', sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<ul class="big-list">{li}</ul>' + _opt('foot-note', foot)))


def _ratio(fid):
    p = _S['figdir'] / f'fig-{fid}.svg'
    if not p.exists():
        return 0.5
    vb = re.search(r'viewBox="\s*[-\d.]+[\s,]+[-\d.]+[\s,]+([\d.]+)[\s,]+([\d.]+)"', p.read_text(encoding='utf-8'))
    return float(vb.group(2)) / float(vb.group(1)) if vb else 0.5


def figure(sec, eyebrow, title, fid, cap, foot=None):
    alt = html.escape(re.sub('<[^>]+>', '', cap), quote=True)
    img = f'<img src="../figures/fig-{fid}.svg" alt="{alt}" />'
    if _ratio(fid) > 0.62:   # 세로로 긴 그림 → 2단(설명 | 그림)
        slides.append(('content split', sec, f'<div class="split"><div class="split-text">{_head(eyebrow, title)}'
                                             f'<p class="split-cap">{cap}</p>{_opt("foot-note", foot)}</div>'
                                             f'<figure class="deck-fig tall">{img}</figure></div>'))
    else:
        slides.append(('content', sec, _head(eyebrow, title)
                       + f'<figure class="deck-fig">{img}<figcaption>{cap}</figcaption></figure>' + _opt('foot-note', foot)))


def ez(text):
    """직전 슬라이드에 '쉽게 말하면' 비유 한 줄을 붙인다 — 모든 내용 슬라이드에 하나씩."""
    kind, sec, inner = slides[-1]
    box = f'<div class="easy"><span class="easy-k">쉽게 말하면</span>{text}</div>'
    inner = inner.replace('</div><figure', box + '</div><figure', 1) if 'split' in kind else inner + box
    slides[-1] = (kind, sec, inner)


CSS = """
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
__ROOT__
*{box-sizing:border-box;margin:0}
body{background:var(--bg);color:var(--text);font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;
 scroll-snap-type:y mandatory;overflow-y:scroll;height:100vh;word-break:keep-all}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.progress-bar{position:fixed;top:0;left:0;right:0;height:3px;background:var(--bg);z-index:99}
.progress-fill{height:100%;background:var(--coral);width:0;transition:width .2s}
.slide{min-height:100vh;scroll-snap-align:start;display:flex;flex-direction:column;justify-content:center;
 padding:var(--pad);position:relative;border-bottom:1px solid var(--line)}
.eyebrow{font-size:.78rem;letter-spacing:.18em;font-weight:700;text-transform:uppercase;margin-bottom:.9rem}
.eyebrow.coral{color:var(--coral)} .eyebrow.cream{color:var(--muted)}
.coral-t{color:var(--coral)} .big{font-size:clamp(1.3rem,2.8vw,2rem);font-weight:800;line-height:1.5;color:var(--coral)} .small-q{display:block;font-size:.62em;font-weight:500;color:var(--muted);margin-top:.4rem}
.content-title{font-size:clamp(1.5rem,3.3vw,2.4rem);font-weight:800;line-height:1.3;text-wrap:balance}
.bar{height:3px;width:64px;background:var(--coral);margin:1rem 0 1.3rem;border-radius:2px}
.lead{color:var(--muted);font-size:clamp(.95rem,1.7vw,1.12rem);line-height:1.7;margin-bottom:1.1rem;max-width:62rem}
.foot-note{color:var(--muted);font-size:clamp(.86rem,1.5vw,1rem);line-height:1.7;margin-top:1.2rem;max-width:66rem}
.foot-note b,.lead b,.after b,.stat-l b{color:var(--cream)}
.cover{background:radial-gradient(1200px 600px at 50% 0%,var(--glow) 0%,var(--bg) 70%)}
.cover-wrap{max-width:62rem}.cover-wrap.has-art{max-width:none;width:100%;min-width:0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:3rem;align-items:center}
.cover-wrap.has-art>*{min-width:0}.cover-art{margin:0}.cover-art.portrait{max-width:420px;justify-self:center}.cover-art img{display:block;width:100%;height:auto;border-radius:16px;box-shadow:0 20px 50px rgba(0,0,0,.45)}
.cover-title{font-size:clamp(3rem,8vw,5.6rem);font-weight:800;line-height:1.05;letter-spacing:-.01em}
.cover-title.end{font-size:clamp(2.4rem,6vw,4.2rem)}
.cover-sub{color:var(--cream);font-size:clamp(1.05rem,2.1vw,1.5rem);margin-top:.8rem;line-height:1.45}
.cover-quote{font-size:clamp(1rem,1.9vw,1.3rem);line-height:1.7;margin:.2rem 0 .6rem}
.cover-by{color:var(--muted);font-size:clamp(.85rem,1.5vw,1rem);line-height:1.6}
.cover-meta{display:flex;gap:1.4rem;flex-wrap:wrap;color:var(--dim);font-size:.9rem;margin-top:1.8rem}
.motif{width:min(420px,80%);height:auto;margin:1.4rem 0}
.corner{position:absolute;width:26px;height:26px;border:2px solid var(--coral-d);opacity:.5}
.corner.tl{top:26px;left:26px;border-right:0;border-bottom:0}.corner.tr{top:26px;right:26px;border-left:0;border-bottom:0}
.corner.bl{bottom:26px;left:26px;border-right:0;border-top:0}.corner.br{bottom:26px;right:26px;border-left:0;border-top:0}
.div{background:linear-gradient(120deg,var(--glow) 0%,var(--bg) 65%)}
.div-wrap{display:grid;grid-template-columns:1.3fr .7fr;gap:2.4rem;align-items:center}
.div-title{font-size:clamp(2rem,4.6vw,3.3rem);font-weight:800;line-height:1.2;margin:.2rem 0 .9rem;text-wrap:balance}
.div-sub{color:var(--muted);font-size:clamp(.95rem,1.7vw,1.15rem);line-height:1.7;max-width:40rem}
.div-ch{list-style:none;padding:0;border-left:3px solid var(--coral);padding-left:1.2rem}
.div-ch li{font-size:clamp(1rem,1.7vw,1.2rem);line-height:2;color:var(--cream)}
.grid{display:grid;gap:1rem}.grid-3{grid-template-columns:repeat(3,minmax(0,1fr))}.grid-4{grid-template-columns:repeat(4,minmax(0,1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:1.1rem 1.2rem}
.card-num{color:var(--coral);font-size:.8rem;font-weight:700;margin-bottom:.5rem}
.card-h{font-weight:700;font-size:clamp(1rem,1.7vw,1.18rem);line-height:1.4;margin-bottom:.45rem}
.card-sub{color:var(--muted);font-size:clamp(.85rem,1.4vw,.98rem);line-height:1.6}
.bigq{border-left:4px solid var(--coral);padding:.4rem 0 .4rem 1.4rem;margin:.6rem 0 1rem;
 font-size:clamp(1.15rem,2.5vw,1.8rem);line-height:1.6;font-weight:600;max-width:64rem}
.q-src{color:var(--dim);font-size:.92rem;line-height:1.6;margin-bottom:.9rem;max-width:64rem}
.after{color:var(--muted);font-size:clamp(.9rem,1.6vw,1.06rem);line-height:1.7;max-width:62rem}
.deck-table{border-collapse:collapse;width:100%;max-width:74rem;margin:.4rem 0}
.deck-table th,.deck-table td{border:1px solid var(--line);padding:.6rem .85rem;text-align:left;
 font-size:clamp(.82rem,1.4vw,1.02rem);line-height:1.55;vertical-align:top}
.deck-table th{background:var(--panel);color:var(--coral);font-weight:700}
.big-list{padding-left:1.3rem;max-width:66rem}.big-list li{font-size:clamp(.95rem,1.75vw,1.2rem);line-height:1.75;margin:.5rem 0}
.big-list b{color:var(--cream)}
.stat-row{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));max-width:74rem}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:1.2rem 1.3rem}
.stat-n{color:var(--coral);font-size:clamp(1.6rem,3.4vw,2.5rem);font-weight:800;line-height:1.1;margin-bottom:.5rem}
.stat-l{color:var(--muted);font-size:clamp(.85rem,1.4vw,1rem);line-height:1.6}
.deck-fig{margin:.2rem auto 0;width:100%;text-align:center}
.deck-fig img{display:block;margin:0 auto;max-width:100%;max-height:calc(100vh - 19rem);width:auto;height:auto;background:var(--figbg);border-radius:12px;padding:8px}
div.split{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:3rem;align-items:center;width:100%}
.split-cap{color:var(--cream);font-size:clamp(.95rem,1.6vw,1.1rem);line-height:1.6;margin-top:.4rem}
.deck-fig.tall img{max-height:calc(100vh - 7rem);width:100%;object-fit:contain}
.deck-fig figcaption{color:var(--dim);font-size:.88rem;margin-top:.6rem}
.easy{margin-top:1.3rem;max-width:66rem;background:var(--panel);border:1px solid var(--line);border-left:4px solid var(--coral);
 border-radius:10px;padding:.85rem 1.1rem;font-size:clamp(.95rem,1.7vw,1.14rem);line-height:1.65;color:var(--text)}
.easy-k{display:inline-block;color:var(--coral);font-weight:800;font-size:.8em;letter-spacing:.06em;margin-right:.7rem}
.slide:has(.easy) .deck-fig:not(.tall) img{max-height:calc(100vh - 25rem)}
.page-num{position:absolute;top:1.5rem;right:1.8rem;color:var(--dim);font-size:.8rem}
.page-section{position:absolute;top:1.5rem;left:1.8rem;color:var(--dim);font-size:.8rem;letter-spacing:.08em}
.page-footer{position:absolute;bottom:1.2rem;left:1.8rem;right:1.8rem;display:flex;justify-content:space-between;gap:1rem;color:var(--dim);font-size:.75rem}
.cover .page-num{top:3.5rem;right:3.6rem}.cover .page-section{top:3.5rem;left:3.6rem}.cover .page-footer{bottom:3.2rem;left:3.6rem;right:3.6rem}
@media(max-width:900px){.cover-wrap.has-art{grid-template-columns:minmax(0,1fr);gap:1.6rem}.cover-sub{overflow-wrap:anywhere}.grid-3,.grid-4{grid-template-columns:1fr}.div-wrap,div.split{grid-template-columns:1fr}.deck-fig img,.deck-fig.tall img{max-height:none;width:100%}
 .page-footer{display:none}.slide{min-height:auto;padding:2.4rem 1.1rem 3rem}.deck-table{display:block;overflow-x:auto}}
@media print{body{height:auto;overflow:visible;background:#fff;color:#111}
 .slide{page-break-after:always;min-height:auto;border:none;background:#fff!important;color:#111}
 .card,.stat,.deck-table th{background:#f1f3f5!important;border-color:#ccc!important}
 .content-title,.card-h,.div-title,.cover-title{color:#111}.card-sub,.lead,.foot-note,.div-sub,.after{color:#444}.easy{background:#fbf5e8!important;color:#111;border-color:#e6d3a8!important}.progress-bar{display:none}}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')],fill=document.getElementById('progress');let cur=0;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){cur=slides.indexOf(e.target);
fill.style.width=((cur+1)/slides.length*100)+'%';}}),{threshold:.55});slides.forEach(s=>io.observe(s));
function go(i){i=Math.max(0,Math.min(slides.length-1,i));slides[i].scrollIntoView({behavior:'smooth',block:'start'});}
addEventListener('keydown',e=>{if(['ArrowDown','ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(cur+1);}
if(['ArrowUp','ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(cur-1);}
if(e.key==='Home'){e.preventDefault();go(0);}if(e.key==='End'){e.preventDefault();go(slides.length-1);}});
"""


def render(out):
    t = _S['theme']
    root = (f":root{{--bg:{t['bg']};--panel:{t['panel']};--line:{t['line']};--text:{t['text']};--muted:{t['muted']};--dim:{t['dim']};"
            f"--coral:{t['accent']};--coral-d:{t['accent_d']};--cream:{t['cream']};--glow:{t['glow']};--figbg:{t['figbg']};--pad:clamp(2rem,4.5vw,4.2rem)}}")
    total = len(slides)
    body, cnt = [], {}
    for i, (kind, sec, inner) in enumerate(slides, 1):
        cnt[sec] = cnt.get(sec, 0) + 1
        body.append(f'<section class="slide {kind}" id="s{i}" data-n="{i}">{inner}'
                    f'<div class="page-num mono">{i:03d} / {total}</div>'
                    f'<div class="page-section mono">{sec} / {cnt[sec]:02d}</div>'
                    f'<div class="page-footer"><span>{_S["book"]}</span><span>{_S["by"]}</span></div></section>')
    no_ez = [i for i, (k, s, inner) in enumerate(slides, 1) if k.startswith('content') and 'class="easy"' not in inner]
    doc = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width, initial-scale=1">'
           f'<title>{html.escape(_S["book"])} — 1시간 발표 자료</title><style>{CSS.replace("__ROOT__", root)}</style></head><body>'
           f'<div class="progress-bar"><div class="progress-fill" id="progress"></div></div><main>'
           + '\n'.join(body) + f'</main><script>{JS}</script></body></html>')
    out = pathlib.Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding='utf-8')
    refs = sorted(set(re.findall(r'src="(\.\./[^"]+)"', doc)))
    missing = [r for r in refs if not (out.parent / r).resolve().exists()]
    print(f"deck build 완료 — {total}장, 그림 {doc.count('../figures/')}점")
    problems = []
    if no_ez:
        problems.append(f"'쉽게 말하면'이 없는 내용 슬라이드: {no_ez}")
    if missing:
        problems.append(f"출력 위치 기준으로 없는 참조 파일: {missing} (site/figures·site/cover.png를 먼저 복사했는지 확인)")
    for msg in problems:
        print('WARNING: ' + msg)
    if problems and os.environ.get('DECK_STRICT', '1') != '0':
        sys.exit(1)   # 기본은 엄격 — 자동 흐름에서 놓치지 않게. 의도적이면 DECK_STRICT=0
