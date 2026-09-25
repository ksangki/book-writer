#!/usr/bin/env python3
"""devrel-next 통합 원고 조립 — 챕터 final + 편집 수정(전환·콜백·표기) + 앞뒤 부속."""
import re, pathlib

BOOK = pathlib.Path(__file__).resolve().parents[2]
SCR = pathlib.Path(__file__).parent
IDENT = 'urn:uuid:2e3ab927-3a44-4ede-b169-e0253729973c'
TITLE, SUB = 'DevRel Next', '코드 너머의 관계'
VER, DATE, AUTHOR = '1.3.0', '2026-09-25', '김상기'
HV = (BOOK.parent / 'VERSION').read_text().strip().lstrip('v')

# 편집 수정: (장, 원문, 교체문, 전부교체 여부)
EDITS = [
    (5, 'Joe Karlsson은 2026년 4월 글에서 이 구도를 셋으로 늘렸다.',
        '4장에서 본 Joe Karlsson은 같은 2026년 4월 글에서 이 구도를 셋으로 늘렸다.', False),
    (7, 'Joe Karlsson은 2026년 4월 20일 글에서 이 역할을',
        '4장에서 본 Joe Karlsson은 같은 2026년 4월 20일 글에서 이 역할을', False),
    (7, 'Rizèl Scarlett가 소개한 운영 방식에도', '5장에서 본 Rizèl Scarlett이 소개한 운영 방식에도', False),
    (7, 'Rizèl Scarlett는', 'Rizèl Scarlett은', True),
    (7, 'Dewan Ahmed는 2026년 8월 11일에 갱신한 글에서 이렇게 답했다.',
        '5장에서 본 Dewan Ahmed는 2026년 8월 11일에 갱신한 같은 글에서 이렇게 답했다.', False),
]
EDITS += [
    (2, '개발자 입장에서는 꽤 찜찜한 관계다.', '개발자 입장에서는 꽤 답답한 관계다.', False),
    (3, '이 문장이 얼마나 찜찜한지 안다.', '이 문장이 얼마나 피곤한지 안다.', False),
]
# "~를 해본 사람으로서" 권위 틀 통권 2회 이하(서문 1회 + 10-6 회고 1회) — team-lead 4.5 권고
EDITS += [
    (1, '이 글을 DevRel을 해본 사람으로서 읽으면, 두 번째 이유가 먼저 걸린다.', '이 글에서 먼저 눈에 걸리는 것은 두 번째 이유다.', False),
    (3, 'DevRel을 해본 사람으로서 이 결론을 읽으면 오래된 직무 기술서를 다시 펼친 기분이 든다.', '이 결론은 오래된 직무 기술서의 한 줄처럼 읽힌다.', False),
    (5, 'DevRel을 했던 사람으로서 이 글에서 가장 오래 남는 것은 진단의 순서다.', '이 글에서 가장 오래 남는 것은 진단의 순서다.', False),
    (6, '이 FDE 공고의 문장은 DevRel을 했던 사람에게 낯설지 않다.', '이 FDE 공고의 문장은 DevRel 공고 옆에 놓아도 낯설지 않다.', False),
    (7, '이야기를 DevRel을 해본 사람으로서 읽으면, 이 네 번째 기능이 나머지 셋을 떠받친다는 생각이 든다.', '이야기를 읽으면, 이 네 번째 기능이 나머지 셋을 떠받친다는 생각이 든다.', False),
    (8, 'DevRel을 해본 사람으로서 "Going first. Figuring stuff out. Guiding others."라는 세 마디를 읽으면, 이 문장은 내게 직무 설명서의 첫 줄처럼 읽힌다.', '"Going first. Figuring stuff out. Guiding others."라는 세 마디는 DevRel 직무 설명서의 첫 줄처럼 읽힌다.', False),
    (8, 'AX를 하는 사람으로서, 나는 이 약어의 우연을 논거로 쓰지 않으려 한다.', '나는 이 약어의 우연을 논거로 쓰지 않으려 한다.', False),
    (9, 'AX를 하는 사람으로서 이 두 댓글은 이 장에서 가장 아프게 읽힌다.', '이 장에서 가장 아프게 읽히는 것은 이 두 댓글이다.', False),
]
# (v1.1.0 5장 deVilla 콜백 편집은 writer-b 5장 정정본에 흡수되어 제거)
# (v1.1.0 6장 '표 1' 편집은 v1.2.0 6장 final에 흡수되어 제거)
# v1.2.0: D/R 표기를 thesis.md에 맞춰 '누구와(D)'로 통일(2장 writer-b 변경에 맞춤)
EDITS += [
    (3, '누구에게(D), 그리고 무엇으로(R).', '누구와(D), 그리고 무엇으로(R).', False),
]
# v1.2.0: 10장 풀어쓰기로 원문 재인용이 다시 들어옴 — 인용 거처(6장 a16z, 3장 roxolotl) 원칙대로 콜백으로
EDITS += [
    (10, '벤처캐피털 a16z의 Joe Schmidt는 2025년 6월 4일 에세이에서 한 흐름을 짚었다. 복잡한 AI 애플리케이션 회사들이 구현 서비스를 앞세우는 \'서비스 주도 성장(services-led growth)\'으로 간다는 것이다. 그 자리는 전문 서비스 인력이 맡는 경우가 많다. 그는 그 인력이 "sometimes rebranded as a forward deployed engineer or an implementation/solutions specialist"라고 썼다. 때로는 FDE나 구현·솔루션 전문가로 이름을 바꿔 단다는 뜻이다. 이 글은 투자사의 에세이이니 그 관점의 이해관계를 함께 읽어두자.',
        '6장에서 본 a16z의 Joe Schmidt는 구현 서비스를 앞세우는 \'서비스 주도 성장(services-led growth)\'을 짚었다. 그 일을 맡는 인력이 때로 FDE 같은 새 이름을 얻는다고도 봤다. 투자사의 에세이라는 점은 여기서도 함께 읽어두자.', False),
    (10, '2026년 2월 26일 Hacker News의 "Will vibe coding end like the maker movement?" 토론이 있다. 바이브 코딩도 메이커 운동처럼 끝날까라는 물음이다. 여기서 roxolotl은 메이커 운동이 느려진 까닭을 사람들의 관심이 그만큼 크지 않았다는 데서 찾았다. 그리고 참여자가 두 배로 늘어도 소수에 머물 것이라고 했다("a small fraction of people").',
        '3장에서 본 메이커 운동 비유가 여기서 다시 돌아온다. 그 토론(Hacker News, 2026-02-26)에서 roxolotl은 참여자가 두 배로 늘어도 소수에 머물 것이라고 봤다.', False),
]
# v1.2.0 데보션: 첫 소개는 2장(저자 공개 기록 문단) — 9장 콜백의 장 번호 정정
EDITS += [
    (9, '3장에서 본 개발자 커뮤니티 데보션', '2장에서 본 개발자 커뮤니티 데보션', False),
]
# v1.2.0 R7(acceptance-v120 권고): 개념어 첫 등장 풀이 — 퍼널은 2-5 소절 상한 여유가 없어 용어집으로만
EDITS += [
    (5, '다음 세대 모델이 배울 코퍼스를 만드는 작업이다.', '다음 세대 모델이 배울 코퍼스(모델이 학습하는 글 묶음)를 만드는 작업이다.', False),
]
HN_CH = {3, 4, 5}  # "HN" → "Hacker News" 표기 통일

chapters = {}
for n in range(1, 11):
    t = (BOOK / 'chapters' / f'{n:02d}_final.md').read_text(encoding='utf-8')
    for ch, a, b, allr in EDITS:
        if ch != n:
            continue
        assert a in t, (n, a[:40])
        t = t.replace(a, b) if allr else t.replace(a, b, 1)
    if n in HN_CH:
        t = re.sub(r'(?<![A-Za-z])HN(?![A-Za-z])', 'Hacker News', t)
    chapters[n] = t.rstrip() + '\n'

front = (SCR / 'front.md').read_text(encoding='utf-8')
back = (SCR / 'back.md').read_text(encoding='utf-8')
biblio = (SCR / 'biblio.md').read_text(encoding='utf-8')

# front.md = 서문 + PART 도입 4개 (--- 구분)
blocks = front.split('\n---\n')
preface = blocks[0].strip().replace('## 서문', '# 서문', 1)
parts = {}
for b in blocks[1:]:
    b = b.strip()
    m = re.match(r'# (PART (\d)\..*)', b)
    parts[int(m.group(2))] = b
PART_BEFORE = {1: 1, 3: 2, 6: 3, 8: 4}

epi_app = back.split('\n---\n')
epilogue = epi_app[0].strip().replace('## 에필로그', '# 에필로그', 1)
appendices = [x.strip() for x in epi_app[1:]]
biblio = biblio.strip().replace('## 참고문헌', '# 참고문헌', 1)

def h1(text):
    return re.match(r'# (.+)', text).group(1).strip()

toc = ['## 목차', '', '- 서문', '']
for n in range(1, 11):
    if n in PART_BEFORE:
        toc += [f'**{h1(parts[PART_BEFORE[n]])}**', '']
    toc.append(f'- {h1(chapters[n])}')
    nxt = n + 1
    if nxt in PART_BEFORE or n == 10:
        toc.append('')
toc += ['- 에필로그']
toc += [f'- {h1(a)}' for a in appendices] + ['- 참고문헌']

title_page = f"""# {TITLE}

## {SUB}

**저자:** {AUTHOR}
**판본:** v{VER} · {DATE}

---

## 판권

**{TITLE} — {SUB}**
**판본:** v{VER}
**발행일:** {DATE}
**저자:** {AUTHOR}
**식별자:** {IDENT}

이 판본은 저자 피드백(결론 세우기·쉽게 풀어쓰기·공개 자료 보강, 10장 '밝은 쪽' 전망 추가)을 반영한 개정판이다. 사례와 수치는 2026년 9월 시점의 공개 자료를 기준으로 했다.

### 라이선스

이 책은 **CC BY-NC-SA 4.0** 라이선스로 배포된다 — [Creative Commons 저작자표시-비영리-동일조건변경허락 4.0 국제](https://creativecommons.org/licenses/by-nc-sa/4.0/).

- **저작자 표시(BY):** 출처를 밝혀야 한다.
- **비상업적 이용(NC):** 상업적 목적으로 이용할 수 없다.
- **동일조건 변경허락(SA):** 변경·재배포 시 동일한 라이선스를 적용해야 한다.

### 출처

이 책은 [book-writer](https://github.com/tobyilee/book-writer) 하네스 v{HV}로 자동 생성되었다.

---

""" + '\n'.join(toc) + '\n'

out = [title_page, preface, '']
for n in range(1, 11):
    if n in PART_BEFORE:
        out += [parts[PART_BEFORE[n]], '']
    out += [chapters[n]]
out += [epilogue, ''] + [a + '\n' for a in appendices] + [biblio, '']
text = '\n'.join(out)
text = re.sub(r'\n{3,}', '\n\n', text)
# 그림·표 전권 연번 (v1.1.0): 장별 '그림 {장}-{k}'·'표 {장}-{k}' → 등장 순서대로 '그림 N'·'표 M'.
# 번호는 캡션 등장 순서로 배정한다(이미지 alt '![그림 3-1. …]' 또는 줄 머리 '그림 3-1.'·'표 3-1.').
# 본문 참조('그림 3-1에서 보듯')도 같은 매핑으로 치환한다. 캡션 없는 참조나 치환 뒤 잔존이 있으면 멈춘다.
FIG_REF = re.compile(r'(?<![가-힣A-Za-z])(그림|표) (\d+)-(\d+)(?!\d)(으로|로|을|를|은|는|과|와|이(?![가-힣])|가(?![가-힣]))?')
# 숫자 끝 발음: 0영·1일·3삼·6육·7칠·8팔은 받침 있음, 1·7·8은 ㄹ받침('로')
def _particle(num, p):
    if not p:
        return ''
    d = str(num)[-1]
    bat, rieul = d in '013678', d in '178'
    pairs = {'을': ('을', '를'), '를': ('을', '를'), '은': ('은', '는'), '는': ('은', '는'),
             '과': ('과', '와'), '와': ('과', '와'), '이': ('이', '가'), '가': ('이', '가')}
    if p in ('으로', '로'):
        return '로' if (rieul or not bat) else '으로'
    a, b = pairs[p]
    return a if bat else b
CAPTION = re.compile(r'(?m)^(?:!\[)?(그림|표) (\d+)-(\d+)\.')
old_style = re.findall(r'(?m)^(?:!\[)?(?:그림|표) \d+\.', text)
assert not old_style, ('장별 구 형식 캡션 잔존(그림 N. / 표 N.) — 새 형식 {장}-{k}로 바꿔야 연번이 겹치지 않는다', old_style[:5])
bare = re.findall(r'(?<![가-힣A-Za-z])(?:그림|표) \d+(?![-\d])', text)
assert not bare, ('연번 전 하이픈 없는 그림·표 참조 잔존 — 장별 옛 번호일 수 있다', bare[:5])
fig_map, counters = {}, {'그림': 0, '표': 0}
for m in CAPTION.finditer(text):
    key = (m.group(1), int(m.group(2)), int(m.group(3)))
    assert key not in fig_map, ('캡션 중복', key)
    counters[key[0]] += 1
    fig_map[key] = counters[key[0]]
refs = {(m.group(1), int(m.group(2)), int(m.group(3))) for m in FIG_REF.finditer(text)}
missing = sorted(refs - set(fig_map))
assert not missing, ('캡션 없는 참조', missing)
def _renum(m):
    n = fig_map[(m.group(1), int(m.group(2)), int(m.group(3)))]
    return f'{m.group(1)} {n}{_particle(n, m.group(4))}'
text = FIG_REF.sub(_renum, text)
assert not FIG_REF.search(text), '연번 치환 뒤 {장}-{k} 잔존'
map_lines = ['| 원래 번호 | 전권 번호 |', '|---|---|'] + [
    f'| {k[0]} {k[1]}-{k[2]} | {k[0]} {v} |' for k, v in sorted(fig_map.items(), key=lambda kv: (kv[0][0] != '그림', kv[1]))]
(SCR / 'figure_map.md').write_text('\n'.join(map_lines) + '\n', encoding='utf-8')
print('figures', counters['그림'], 'tables', counters['표'])
imgs = re.findall(r'!\[[^\]]*\]\(([^)]+)\)', text)
missing_img = [i for i in imgs if not (BOOK / i).exists()]
assert not missing_img, ('그림 파일 없음', missing_img)
(BOOK / '04_manuscript.md').write_text(text, encoding='utf-8')
print('written', len(text))
