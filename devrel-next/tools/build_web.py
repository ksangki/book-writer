#!/usr/bin/env python3
"""웹 버전 빌드 — EPUB을 원천으로 pandoc HTML + 그림 추출 + 반응형/다크모드 CSS.
사용법: python3 build_web.py <epub> <출력 폴더>"""
import sys, subprocess, pathlib, re
epub, out = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
out.mkdir(parents=True, exist_ok=True)
subprocess.run(['pandoc', str(epub), '-f', 'epub', '-t', 'html5', '-s',
                '--extract-media=media', '-o', 'index.html',
                '--metadata', 'title=DevRel Next — 코드 너머의 관계', '--metadata', 'lang=ko'],
               cwd=out, check=True)
h = (out / 'index.html').read_text(encoding='utf-8')
CSS = """<style>
:root{--bg:#fbf9f6;--text:#231c2b;--muted:#6b5f76;--line:#e4dce8;--accent:#c4553a;--panel:#f3eef5;--code:#f1ecf3}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17121f;--text:#ece6f0;--muted:#a99cb6;--line:#342a40;--accent:#ff8a6b;--panel:#211a2c;--code:#241c30}}
:root[data-theme="dark"]{--bg:#17121f;--text:#ece6f0;--muted:#a99cb6;--line:#342a40;--accent:#ff8a6b;--panel:#211a2c;--code:#241c30}
html{-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--text);margin:0 auto;max-width:760px;padding:24px 16px 80px;
 font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;font-size:17px;line-height:1.85;word-break:keep-all;overflow-wrap:anywhere}
h1,h2,h3{line-height:1.35;text-wrap:balance}
h1{font-size:1.9rem;margin-top:3.2rem;border-bottom:2px solid var(--accent);padding-bottom:.4rem}
h2{font-size:1.35rem;margin-top:2.4rem} h3{font-size:1.1rem}
a{color:var(--accent)} blockquote{margin:1.2rem 0;padding:.6rem 1rem;border-left:4px solid var(--accent);background:var(--panel);color:var(--text)}
table{border-collapse:collapse;display:block;overflow-x:auto;max-width:100%;font-size:.92rem;margin:1.2rem 0}
th,td{border:1px solid var(--line);padding:.45rem .65rem;vertical-align:top} th{background:var(--panel)}
img,svg{max-width:100%;height:auto} figure{margin:1.6rem 0;text-align:center}
figure img{background:#fff;border-radius:8px;padding:8px} figcaption{color:var(--muted);font-size:.9rem}
code{background:var(--code);padding:.1em .3em;border-radius:4px} pre{background:var(--code);padding:1rem;overflow-x:auto}
hr{border:0;border-top:1px solid var(--line);margin:2.4rem 0}
.cover-hero{text-align:center;margin:8px 0 32px} .cover-hero img{max-width:320px;width:70%;border-radius:10px;box-shadow:0 12px 32px rgba(0,0,0,.25)}
.dl{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px;font-size:.95rem}
.dl a{border:1px solid var(--accent);padding:.35rem .9rem;border-radius:999px;text-decoration:none}
</style>"""
# EPUB 속 표지(인라인 SVG, 웹에선 경로가 깨짐)는 hero와 중복이라 제거
h = re.sub(r'<svg[^>]*>(?:(?!</svg>).)*?media/[^"]+\.png(?:(?!</svg>).)*?</svg>', '', h, count=1, flags=re.S)
h = re.sub(r'<p><img src="media/[^"]+\.png" /></p>', '', h)
h = re.sub(r'<header id="title-block-header">.*?</header>', '', h, count=1, flags=re.S)
# 그림: <p><img src=X /> 그림 N. 캡션</p> → figure + alt
h = re.sub(r'<p><img src="([^"]+)" />\s*(그림 \d+\.[^<]*)</p>',
           lambda m: f'<figure><img src="{m.group(1)}" alt="{m.group(2).strip()}" /><figcaption>{m.group(2).strip()}</figcaption></figure>', h)
h = re.sub(r'<style>.*?</style>', '', h, flags=re.S).replace('</head>', CSS + '\n</head>', 1)
hero = ('<div class="cover-hero"><img src="cover.png" alt="「DevRel Next — 코드 너머의 관계」 표지" />'
        f'<div class="dl"><a href="epub/{epub.name}">EPUB 내려받기</a><a href="BOOK.md">책 소개</a>'
        '<a href="https://github.com/ksangki/devrel-next">GitHub</a></div></div>')
h = re.sub(r'(<body[^>]*>)', r'\1\n' + hero, h, count=1)
(out / 'index.html').write_text(h, encoding='utf-8')
for png in (out / 'media').rglob('*.png'): png.unlink()  # 표지 사본 — 웹은 루트 cover.png 사용
print('web build 완료:', out / 'index.html', '· media', len(list((out / 'media').rglob('*'))) if (out/'media').exists() else 0)
