#!/usr/bin/env python3
"""웹 버전 빌드 — EPUB을 원천으로 pandoc HTML + 그림 추출 + 반응형/다크모드 CSS.

사용법: python3 build_web.py <slug> <epub> <site 폴더>
  - 제목·부제·표지 alt·저장소 링크(repo_url, 있으면)는 <slug>/book_manifest.json에서 읽는다.
  - 색은 매니페스트의 theme.light_accent / theme.dark_accent(없으면 기본값)로 정한다.
  - site 폴더에는 cover.png·BOOK.md·epub/·presentation/이 함께 놓인다고 가정하고 링크한다.
  - site 폴더에 media/opening.mp4(와 media/opening.jpg)가 있으면 표지 아래에 영상을 싣는다(매니페스트 web_videos로 바꿀 수 있다).
목차("목차"/"차례") 항목은 같은 제목의 장으로 링크한다(toc_links.py).
그림 캡션은 "그림 N-k." / "그림 N." 둘 다, 표 캡션은 "표 N-k." 문단, 굵은 글씨 문단, 번호만 굵은 문단("**표 N-k.** 제목")을 모두 인식한다.
"""
import sys, subprocess, pathlib, re, json, html, zipfile
slug, epub, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), pathlib.Path(sys.argv[3]).resolve()
m = json.loads((slug / 'book_manifest.json').read_text(encoding='utf-8'))
title = m.get('title', '') + (f": {m['subtitle']}" if m.get('subtitle') else '')
theme = m.get('theme', {})
out.mkdir(parents=True, exist_ok=True)
subprocess.run(['pandoc', str(epub), '-f', 'epub', '-t', 'html5', '-s',
                '--extract-media=media', '-o', 'index.html',
                '--metadata', f'title={title}', '--metadata', f"lang={m.get('language', 'ko')}"],
               cwd=out, check=True)
h = (out / 'index.html').read_text(encoding='utf-8')
# EPUB 속 표지 이미지 파일명(OPF의 properties="cover-image") — 웹에서는 이 한 파일만 지우고 hero의 site/cover.png를 쓴다.
cover_name = None
with zipfile.ZipFile(epub) as z:
    opf = next((n for n in z.namelist() if n.endswith('.opf')), None)
    if opf:
        mm = re.search(r'<item[^>]*properties="[^"]*cover-image[^"]*"[^>]*>', z.read(opf).decode('utf-8', 'ignore'))
        if mm:
            hh = re.search(r'href="([^"]+)"', mm.group(0))
            cover_name = pathlib.Path(hh.group(1)).name if hh else None
CSS = """<style>
:root{--bg:#fbfaf7;--text:#1b2430;--muted:#5f6b78;--line:#e1e4e8;--accent:#9a6b1c;--panel:#f1f3f5;--code:#eef1f4}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#111a24;--text:#e8ecf0;--muted:#9aa6b2;--line:#2c3a4a;--accent:#e3b35a;--panel:#18232f;--code:#1c2835}}
:root[data-theme="dark"]{--bg:#111a24;--text:#e8ecf0;--muted:#9aa6b2;--line:#2c3a4a;--accent:#e3b35a;--panel:#18232f;--code:#1c2835}
html{-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--text);margin:0 auto;max-width:820px;padding:24px 16px 80px;
 font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;font-size:17px;line-height:1.85;word-break:keep-all;overflow-wrap:anywhere}
h1,h2,h3{line-height:1.35;text-wrap:balance}
h1{font-size:1.9rem;margin-top:3.2rem;border-bottom:2px solid var(--accent);padding-bottom:.4rem}
h2{font-size:1.35rem;margin-top:2.4rem} h3{font-size:1.1rem}
a{color:var(--accent)} blockquote{margin:1.2rem 0;padding:.6rem 1rem;border-left:4px solid var(--accent);background:var(--panel);color:var(--text)}
.tbl{overflow-x:auto;margin:1.6rem 0 .4rem;border:1px solid var(--line);border-radius:10px}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.6}
th,td{border-bottom:1px solid var(--line);padding:.55rem .75rem;vertical-align:top;text-align:left}
th{background:var(--panel);font-weight:700;white-space:nowrap} tbody tr:nth-child(even) td{background:color-mix(in srgb,var(--panel) 45%,transparent)}
tbody tr:last-child td{border-bottom:0}
th,td{overflow-wrap:break-word} td{min-width:6.5em}
p.tcap{color:var(--muted);font-size:.88rem;text-align:center;margin:.3rem 0 1.8rem} p.tcap b,figcaption b{color:var(--accent)}
img,svg{max-width:100%;height:auto} figure{margin:2rem 0;text-align:center}
figure img{display:block;margin:0 auto;border-radius:10px;border:1px solid var(--line);background:#fbf7f2}
figcaption{color:var(--muted);font-size:.88rem;margin-top:.6rem}
code{background:var(--code);padding:.1em .3em;border-radius:4px} pre{background:var(--code);padding:1rem;overflow-x:auto}
hr{border:0;border-top:1px solid var(--line);margin:2.4rem 0}
.cover-hero{text-align:center;margin:8px 0 32px} .cover-hero img{max-width:320px;width:70%;border-radius:10px;box-shadow:0 12px 32px rgba(0,0,0,.25)}
.dl{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px;font-size:.95rem}
.dl a{border:1px solid var(--accent);padding:.35rem .9rem;border-radius:999px;text-decoration:none}
.web-video{margin:0 0 32px} .web-video video{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:10px;background:#000}
</style>"""
CSS = CSS.replace('--accent:#9a6b1c', '--accent:' + theme.get('light_accent', '#9a6b1c')).replace('--accent:#e3b35a', '--accent:' + theme.get('dark_accent', '#e3b35a'))
# EPUB 속 표지(인라인 SVG, 웹에선 경로가 깨짐)는 hero와 중복이라 제거
if cover_name:
    cn = re.escape(cover_name)
    h = re.sub(r'<svg[^>]*>(?:(?!</svg>).)*?media/[^"]*' + cn + r'(?:(?!</svg>).)*?</svg>', '', h, count=1, flags=re.S)
    h = re.sub(r'<p><img src="media/[^"]*' + cn + r'"[^>]*/></p>', '', h)
h = re.sub(r'<header id="title-block-header">.*?</header>', '', h, count=1, flags=re.S)
# EPUB 전용 landmarks 내비(숨김)는 웹에서 대상이 없는 링크가 된다
h = re.sub(r'<nav epub:type="landmarks".*?</nav>', '', h, flags=re.S)
h = re.sub(r'<p><img src="([^"]+)" />\s*(그림 [\d-]+\.[^<]*)</p>',
           lambda x: f'<figure><img src="{x.group(1)}" alt="{x.group(2).strip()}" /><figcaption>{x.group(2).strip()}</figcaption></figure>', h)
h = re.sub(r'<style>.*?</style>', '', h, flags=re.S).replace('</head>', CSS + '\n</head>', 1)
links = [f'<a href="epub/{epub.name}">EPUB 내려받기</a>', '<a href="BOOK.md">책 소개</a>', '<a href="presentation/">발표자료</a>']
for l in m.get('web_links', []):   # 표지 아래 버튼 줄에 더할 링크(매니페스트). download 가 참이면 내려받기 링크
    links.append(f'<a href="{html.escape(l["href"], quote=True)}"' + (' download' if l.get('download') else '') + f'>{html.escape(l["text"])}</a>')
if m.get('repo_url'):
    links.append(f'<a href="{html.escape(m["repo_url"], quote=True)}">GitHub</a>')
alt = html.escape(m.get('cover_alt') or f'「{title}」 표지', quote=True)
hero = f'<div class="cover-hero"><img src="cover.png" alt="{alt}" /><div class="dl">{"".join(links)}</div></div>'
# 영상 블록: site 폴더에 영상 파일이 있으면 표지 바로 아래에 싣는다. 매니페스트 web_videos로 목록·순서·캡션을 정할 수 있다.
videos = m.get('web_videos') or [{'src': 'media/opening.mp4', 'poster': 'media/opening.jpg', 'caption': '발표 오프닝 영상 (60초)'}]
for v in videos:
    if not (out / v['src']).exists():
        continue
    poster = f' poster="{html.escape(v["poster"], quote=True)}"' if v.get('poster') and (out / v['poster']).exists() else ''
    vid_id = f' id="{html.escape(v["id"], quote=True)}"' if v.get('id') else ''
    label = f' aria-label="{html.escape(v["label"], quote=True)}"' if v.get('label') else ''
    hero += (f'\n<figure class="web-video"{vid_id}><video controls playsinline preload="metadata"{poster}{label}>'
             f'<source src="{html.escape(v["src"], quote=True)}" type="video/mp4" /></video>'
             f'<figcaption>{v.get("caption", "")}</figcaption></figure>')
h = re.sub(r'(<body[^>]*>)', lambda x: x.group(1) + '\n' + hero, h, count=1)
h = re.sub(r'<table', '<div class="tbl"><table', h)
h = h.replace('</table>', '</table></div>')
h = re.sub(r'<p>(표 [A-Z\d-]+\.)', r'<p class="tcap"><b>\1</b>', h)
h = re.sub(r'<p><strong>(표 [A-Z\d-]+\.)\s*([^<]*)</strong></p>', r'<p class="tcap"><b>\1</b> \2</p>', h)
h = re.sub(r'<p><strong>(표 [A-Z\d-]+\.)</strong>', r'<p class="tcap"><b>\1</b>', h)   # 번호만 굵은 "**표 N-k.** 제목"
h = re.sub(r'<figcaption([^>]*)>(?:<p>)?(그림 [\d-]+\.)', r'<figcaption\1><b>\2</b>', h)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from toc_links import link as _toc_link   # 목차 항목 → 해당 장 링크
h, n_toc = _toc_link(h)
# 본문에 맨 주소로 적힌 http(s) URL을 링크로 바꾸고, 바깥 링크는 모두 새 창으로 연다.
_URL = re.compile(r"https?://[A-Za-z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")
_SKIP = ('a', 'code', 'pre', 'script', 'style', 'svg', 'title', 'head')
def _linkify(doc):
    parts, depth, n = re.split(r'(<[^>]+>)', doc), {t: 0 for t in _SKIP}, 0
    for i, p in enumerate(parts):
        if p.startswith('<'):
            mt = re.match(r'<(/?)([a-zA-Z0-9]+)', p)
            if mt and mt.group(2).lower() in depth and not p.endswith('/>'):
                depth[mt.group(2).lower()] += -1 if mt.group(1) else 1
            continue
        if any(depth.values()) or 'http' not in p:
            continue
        txt, out_s, last = html.unescape(p), [], 0   # 엔티티를 먼저 풀어야 &quot;·&amp; 끝이 URL에 섞이지 않는다
        for mu in _URL.finditer(txt):
            u, tail = mu.group(0), ''
            while u and (u[-1] in ".,;:!?'\"" or (u[-1] == ')' and u.count('(') < u.count(')'))):
                tail = u[-1] + tail; u = u[:-1]
            if not u.split('://', 1)[1]:
                continue
            out_s.append(html.escape(txt[last:mu.start()], quote=False))
            out_s.append(f'<a href="{html.escape(u, quote=True)}">{html.escape(u, quote=False)}</a>')
            last = mu.start() + len(u); n += 1
        if out_s:
            out_s.append(html.escape(txt[last:], quote=False))
            parts[i] = ''.join(out_s)
    return ''.join(parts), n
h, n_url = _linkify(h)
def _newwin(m):   # 바깥 링크는 기존 target을 덮어 새 창으로, rel에는 noopener noreferrer를 합친다
    tag = m.group(0)
    if not re.search(r'\bhref="https?://', tag):
        return tag
    tag = re.sub(r'\s+target="[^"]*"', '', tag)
    mr = re.search(r'\brel="([^"]*)"', tag)
    if mr:
        toks = mr.group(1).split()
        toks += [x for x in ('noopener', 'noreferrer') if x not in toks]
        tag = tag[:mr.start()] + 'rel="' + ' '.join(toks) + '"' + tag[mr.end():]
    else:
        tag = tag[:-1] + ' rel="noopener noreferrer">'
    return tag[:-1] + ' target="_blank">'
h = re.sub(r'<a\s[^>]*>', _newwin, h)
(out / 'index.html').write_text(h, encoding='utf-8')
if cover_name:
    for f in (out / 'media').rglob(cover_name):
        f.unlink()  # EPUB 속 표지 사본만 지운다 — 본문 PNG 그림·사진은 그대로 둔다
n_fig = h.count('<figure')
print('web build 완료:', out / 'index.html', '· 그림', n_fig, '· 표 캡션', h.count('class="tcap"'), '· 목차 링크', n_toc, '· 맨 주소 링크', n_url, '· 새 창 링크', h.count('target="_blank"'))
