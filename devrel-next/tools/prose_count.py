#!/usr/bin/env python3
"""소절(##)별 순수 산문 자수 — 코드·mermaid 블록, 표(|), 인용 블록(>), 헤딩, 그림 캡션 제외.
사용: python3 devrel-next/tools/prose_count.py devrel-next/chapters/03_final.md [...]
소절당 상한 3,000자를 넘으면 OVER로 표시한다 (02_plan.md 분량 규약)."""
import re
import sys

LIMIT = 3000
for path in sys.argv[1:]:
    in_code, sec, counts, order = False, None, {}, []
    for line in open(path, encoding="utf-8"):
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        if line.startswith("## "):
            sec = line.strip()
            order.append(sec)
            counts[sec] = 0
            continue
        if sec is None or line.startswith(("|", ">", "#")) or re.match(r"^그림 \d+\.", line):
            continue
        counts[sec] += len(line)
    print(path)
    for s in order:
        flag = "OVER" if counts[s] > LIMIT else "ok  "
        print(f"  {counts[s]:>6}  {flag}  {s}")
