#!/usr/bin/env python3
"""쉬운 문장 계측 — 순수 산문(헤딩·표·그림·인용 블록·목록 제외)의 문장 길이 분포."""
import re, sys
for f in sys.argv[1:]:
    t = open(f, encoding='utf-8').read()
    body = '\n'.join(l for l in t.split('\n') if l.strip() and not l.startswith(('#', '|', '!', '>', '-', '* ', '표 ', '그림 ')))
    body = re.sub(r'"[^"]*"|“[^”]*”', '"…"', body)          # 따옴표 인용은 한 토막으로
    sents = [s for s in re.split(r'(?<=[.?!])\s+', body) if len(s) > 5]
    L = [len(s) for s in sents]
    print(f"{f}: 문장 {len(L)} · 평균 {sum(L)/len(L):.1f}자 · 80자↑ {sum(x > 80 for x in L)} · 110자↑ {sum(x > 110 for x in L)}")
