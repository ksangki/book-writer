#!/usr/bin/env python3
"""Count prose characters per chapter and flag outliers.

Usage: python3 length_report.py {slug}

Prose = chapter text minus fenced blocks (code, mermaid, ::: divs), tables,
block quotes, and HTML comments. Characters are counted with spaces, without
newlines. Flags chapters under 70% or over 150% of the median.
"""
import glob
import os
import re
import statistics
import sys


def prose_chars(text: str) -> int:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"^```.*?^```[^\n]*$", "", text, flags=re.S | re.M)
    text = re.sub(r"^:::.*?^:::\s*$", "", text, flags=re.S | re.M)
    lines = [
        ln for ln in text.splitlines()
        if not ln.lstrip().startswith(("|", ">", "#"))
    ]
    return len("".join(lines))


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("usage: length_report.py {slug}")
    slug = sys.argv[1]
    paths = sorted(glob.glob(os.path.join(slug, "chapters", "*_final.md")))
    paths = [p for p in paths if re.match(r"\d+_final\.md$", os.path.basename(p))]
    if not paths:
        sys.exit(f"no chapters/*_final.md under {slug}")

    rows = []
    for p in paths:
        with open(p, encoding="utf-8") as f:
            rows.append((os.path.basename(p).split("_")[0], prose_chars(f.read())))
    median = statistics.median(n for _, n in rows)

    print("| 장 | 산문 글자 수 | 중앙값 대비 | 판정 |")
    print("|----|-------------|------------|------|")
    for ch, n in rows:
        ratio = n / median if median else 0
        if ratio < 0.7:
            verdict = "⚠️ 짧음"
        elif ratio > 1.5:
            verdict = "⚠️ 김"
        else:
            verdict = "OK"
        print(f"| {int(ch)}장 | {n:,} | {ratio:.0%} | {verdict} |")
    print()
    print(f"중앙값: {median:,.0f}자 · 합계: {sum(n for _, n in rows):,}자 "
          "(표·코드·mermaid·::: 블록·인용·헤딩 제외, 공백 포함)")


if __name__ == "__main__":
    main()
