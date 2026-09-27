#!/usr/bin/env python3
"""웹 버전 빌드 — EPUB을 원천으로 pandoc HTML + 그림 추출 + 반응형/다크모드 CSS.

사용법: python3 build_web.py <slug> <epub> <site 폴더>
  - 제목·부제·표지 alt·저장소 링크(repo_url, 있으면)는 <slug>/book_manifest.json에서 읽는다.
  - 색은 매니페스트의 theme.light_accent / theme.dark_accent(없으면 기본값)로 정한다.
  - site 폴더에는 cover.png·BOOK.md·epub/·presentation/이 함께 놓인다고 가정하고 링크한다.
그림 캡션은 "그림 N-k." / "그림 N." 둘 다, 표 캡션은 "표 N-k." 문단과 굵은 글씨 문단 둘 다 인식한다.
"""
import sys, subprocess, pathlib, re, json, html, zipfile
slug, epub, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve(), pathlib.Path(sys.argv[3]).resolve()
m = json.loads((slug / 'book_manifest.json').read_text(encoding='utf-8'))
title = m.get('title', '') + (f" — {m['subtitle']}" if m.get('subtitle') else '')
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
p.tcap{color:var(--muted);font-size:.88rem;text-align:center;margin:.3rem 0 1.8rem} p.tcap b,figcaption b{color:var(--accent)}
img,svg{max-width:100%;height:auto} figure{margin:2rem 0;text-align:center}
figure img{display:block;margin:0 auto;border-radius:10px;border:1px solid var(--line);background:#fbf7f2}
figcaption{color:var(--muted);font-size:.88rem;margin-top:.6rem}
code{background:var(--code);padding:.1em .3em;border-radius:4px} pre{background:var(--code);padding:1rem;overflow-x:auto}
hr{border:0;border-top:1px solid var(--line);margin:2.4rem 0}
.cover-hero{text-align:center;margin:8px 0 32px} .cover-hero img{max-width:320px;width:70%;border-radius:10px;box-shadow:0 12px 32px rgba(0,0,0,.25)}
.dl{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px;font-size:.95rem}
.dl a{border:1px solid var(--accent);padding:.35rem .9rem;border-radius:999px;text-decoration:none}
</style>"""
CSS = CSS.replace('--accent:#9a6b1c', '--accent:' + theme.get('light_accent', '#9a6b1c')).replace('--accent:#e3b35a', '--accent:' + theme.get('dark_accent', '#e3b35a'))
# EPUB 속 표지(인라인 SVG, 웹에선 경로가 깨짐)는 hero와 중복이라 제거
if cover_name:
    cn = re.escape(cover_name)
    h = re.sub(r'<svg[^>]*>(?:(?!</svg>).)*?media/[^"]*' + cn + r'(?:(?!</svg>).)*?</svg>', '', h, count=1, flags=re.S)
    h = re.sub(r'<p><img src="media/[^"]*' + cn + r'"[^>]*/></p>', '', h)
h = re.sub(r'<header id="title-block-header">.*?</header>', '', h, count=1, flags=re.S)
h = re.sub(r'<p><img src="([^"]+)" />\s*(그림 [\d-]+\.[^<]*)</p>',
           lambda x: f'<figure><img src="{x.group(1)}" alt="{x.group(2).strip()}" /><figcaption>{x.group(2).strip()}</figcaption></figure>', h)
h = re.sub(r'<style>.*?</style>', '', h, flags=re.S).replace('</head>', CSS + '\n</head>', 1)
links = [f'<a href="epub/{epub.name}">EPUB 내려받기</a>', '<a href="BOOK.md">책 소개</a>', '<a href="presentation/">발표자료</a>']
if m.get('repo_url'):
    links.append(f'<a href="{html.escape(m["repo_url"], quote=True)}">GitHub</a>')
alt = html.escape(m.get('cover_alt') or f'「{title}」 표지', quote=True)
hero = f'<div class="cover-hero"><img src="cover.png" alt="{alt}" /><div class="dl">{"".join(links)}</div></div>'
h = re.sub(r'(<body[^>]*>)', lambda x: x.group(1) + '\n' + hero, h, count=1)
h = re.sub(r'<table', '<div class="tbl"><table', h)
h = h.replace('</table>', '</table></div>')
h = re.sub(r'<p>(표 [A-Z\d-]+\.)', r'<p class="tcap"><b>\1</b>', h)
h = re.sub(r'<p><strong>(표 [A-Z\d-]+\.)\s*([^<]*)</strong></p>', r'<p class="tcap"><b>\1</b> \2</p>', h)
h = re.sub(r'<figcaption([^>]*)>(?:<p>)?(그림 [\d-]+\.)', r'<figcaption\1><b>\2</b>', h)
(out / 'index.html').write_text(h, encoding='utf-8')
if cover_name:
    for f in (out / 'media').rglob(cover_name):
        f.unlink()  # EPUB 속 표지 사본만 지운다 — 본문 PNG 그림·사진은 그대로 둔다
n_fig = h.count('<figure')
print('web build 완료:', out / 'index.html', '· 그림', n_fig, '· 표 캡션', h.count('class="tcap"'))
