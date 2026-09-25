#!/usr/bin/env python3
"""04_manuscript.md 조립 — front_matter + 파트 구분 + 10개 장 + back_matter.

챕터가 갱신되면 이 스크립트를 다시 돌려 통합 원고를 재생성한다.
저술 내용은 손대지 않는다 — 파트 구분면만 editor가 공급하는 전환부다.
"""
import pathlib
import re

BASE = pathlib.Path(__file__).resolve().parent
CH = BASE / "chapters"

# 파트 구분면. 각 파트의 첫 장 앞에 삽입된다.
# 한 줄짜리 명제로만 둔다 — 목차 재진술("이번 파트에서는 ~")은 쓰지 않는다.
PARTS = {
    1: (
        "PART 1. 전향 — 위가 할 일은 따로 있다",
        "바텀업이 씨앗을 만든다. 그러나 씨앗은 저절로 수확되지 않는다.",
    ),
    2: (
        "PART 2. 절차 — 체계의 입장권",
        "절차가 글로 적히지 않은 에이전트는 등록 자격이 없다. "
        "그런데 무엇이 있는지부터 모른다면 적을 대상도 정해지지 않는다.",
    ),
    5: (
        "PART 3. 등록 — 조직에 자리를 만든다",
        "등록한다는 것은 책임의 소재를 만드는 일이다. "
        "그런데 자리를 하나 만들려는 순간, 아무도 회의실에서 꺼내지 않았던 질문이 "
        "따라온다 — 그래서 몇 개를 만들 건가.",
    ),
    8: (
        "PART 4. 성과 — 세는 법과 그 대가",
        "세는 일은 여기서부터 어려워진다. 성과를 재려면 그 숫자를 어디에 쓰지 않을 것인지부터 정해야 한다.",
    ),
    10: (
        "PART 5. 끝 — 설계되지 않은 마지막 칸",
        "들이는 법은 다들 설계한다. 거두는 체계의 마지막 동작은 내려놓는 것이다.",
    ),
}

parts_out = [(BASE / "front_matter.md").read_text(encoding="utf-8").rstrip()]

for n in range(1, 11):
    src = CH / f"{n:02d}_final.md"
    body = src.read_text(encoding="utf-8").strip()
    if not body.startswith(f"# {n}장."):
        raise SystemExit(f"{src.name}: 예상한 장 제목 헤딩이 아니다 — {body[:40]!r}")
    if n in PARTS:
        title, line = PARTS[n]
        parts_out.append(f"# {title}\n\n{line}")
    parts_out.append(body)

parts_out.append((BASE / "back_matter.md").read_text(encoding="utf-8").rstrip())

out = "\n\n---\n\n".join(parts_out) + "\n"
target = BASE / "04_manuscript.md"
target.write_text(out, encoding="utf-8")

chars = len(out)
h1 = re.findall(r"^# (.+)$", out, re.M)
print(f"04_manuscript.md 생성 — {chars:,}자 (공백 포함), h1 {len(h1)}개")
for h in h1:
    print("  #", h)
