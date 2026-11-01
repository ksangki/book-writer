#!/usr/bin/env python3
"""웹 버전 목차를 누르면 해당 장으로 가게 한다 — build_web.py가 만든 index.html 후처리.

사용법: python3 toc_links.py <index.html>   (여러 번 돌려도 결과가 같다)
  - pandoc이 붙인 <section id="…"> 안의 h1/h2 제목을 모은다.
  - "목차"/"차례" 제목 아래 목록 항목(<li>)과 부 제목 문단(<p><strong>…</strong></p>)을
    같은 제목(또는 같은 "N장"·"N부"·"부록 X" 머리)을 가진 장으로 잇는다.
"""
import sys, re, html, pathlib

KEY = re.compile(r'^(\d+\s*장|\d+\s*부|부록\s*[A-Za-z0-9가-힣]+|서문|프롤로그|에필로그|참고문헌|맺는 장|들어가며|나가며)')


def norm(s):
    s = html.unescape(re.sub(r'<[^>]+>', '', s))
    s = s.replace('“', '"').replace('”', '"').replace('‘', "'").replace('’', "'")
    return re.sub(r'\s+', ' ', s).strip().rstrip('.')


def key(s):
    m = KEY.match(s)
    return re.sub(r'\s+', '', m.group(1)) if m else None


def link(h):
    heads = [(sid, lv, norm(t)) for sid, lv, t in re.findall(
        r'<section\s+id="([^"]+)"[^>]*>\s*<h([12])[^>]*>(.*?)</h[12]>', h, flags=re.S)]
    toc = re.search(r'<h([12])[^>]*>\s*(?:목차|차례)\s*</h\1>(.*?)(?=</section>|<h[12][ >])', h, flags=re.S)
    if not toc:
        return h, 0
    # 목차 제목 자신은 대상에서 뺀다. 장·부는 h1에서 찾고, h2는 제목이 똑같을 때만 쓴다(앞부속의 서문 등).
    heads = [(sid, lv, t) for sid, lv, t in heads if t not in ('목차', '차례')]
    h1 = [(sid, t) for sid, lv, t in heads if lv == '1']
    h2_text = {}
    for sid, lv, t in heads:
        if lv == '2':
            h2_text.setdefault(t, sid)
    by_text, by_key = {}, {}
    for sid, t in h1:
        by_text.setdefault(t, sid)
        k = key(t)
        if k:
            by_key.setdefault(k, sid)

    def target(text):
        t = norm(text)
        if not t:
            return None
        if t in by_text:
            return by_text[t]
        for ht, sid in by_text.items():
            if ht.startswith(t) or t.startswith(ht):
                return sid
        k = key(t)
        if k and k in by_key:
            return by_key[k]
        return h2_text.get(t)

    n = 0

    def wrap_li(m):
        nonlocal n
        head, text = m.group(1), m.group(2)
        if '<a ' in text:
            return m.group(0)
        sid = target(text)
        if not sid:
            return m.group(0)
        n += 1
        return f'{head}<a href="#{html.escape(sid, quote=True)}">{text.strip()}</a>'

    def wrap_strong(m):
        nonlocal n
        text = m.group(1)
        sid = target(text)
        if not sid or '<a ' in text:
            return m.group(0)
        n += 1
        return f'<p><strong><a href="#{html.escape(sid, quote=True)}">{text}</a></strong></p>'

    body = toc.group(2)
    # <li>의 첫 텍스트(하위 <ul> 앞까지)만 링크로 감싼다
    body = re.sub(r'(<li>)([^<]+(?:<(?!/?(?:ul|ol|li|a)\b)[^>]*>[^<]*)*?)(?=<ul>|<ol>|</li>)', wrap_li, body)
    # <li><p>제목</p></li> 꼴(한 항목이 문단으로 감싸인 목록)
    body = re.sub(r'(<li>\s*<p>)([^<]+)(?=</p>)', wrap_li, body)
    body = re.sub(r'<p><strong>([^<]+)</strong></p>', wrap_strong, body)
    return h[:toc.start(2)] + body + h[toc.end(2):], n


if __name__ == '__main__':
    p = pathlib.Path(sys.argv[1])
    out, n = link(p.read_text(encoding='utf-8'))
    p.write_text(out, encoding='utf-8')
    print(f'toc_links: {n} links')
