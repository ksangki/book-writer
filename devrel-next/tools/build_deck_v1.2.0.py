#!/usr/bin/env python3
"""발표자료 생성기 — 「DevRel Next — 코드 너머의 관계」 1시간 발표용.
「디지털 워커의 시대」 덱과 같은 구조 규약(표지·PART 구분면·진행바·페이지 번호·인쇄)에
이 책의 표지 팔레트(짙은 자주 + 코랄 + 크림)와 본문 그림 19점을 쓴다. 그림 번호는 책의 전권 연번.
사용법: python3 build_deck.py <출력 index.html 경로>   (그림은 ../figures/fig-{장}-{k}.svg 참조)
"""
import sys, pathlib

OUT = pathlib.Path(sys.argv[1])
BOOK = "DevRel Next — 코드 너머의 관계"
BY = "김상기 · ksangki/devrel-next"
VER = "v1.2.0"
slides = []

MOTIF = ('<svg class="motif" viewBox="0 0 420 60" aria-hidden="true">'
         '<line x1="0" y1="30" x2="420" y2="30" stroke="#4a3a5e" stroke-width="2"/>'
         '<circle cx="4" cy="30" r="4" fill="#4a3a5e"/><circle cx="416" cy="30" r="4" fill="#4a3a5e"/>'
         '<line x1="110" y1="30" x2="310" y2="30" stroke="#ff8a6b" stroke-width="3"/>'
         '<circle cx="110" cy="30" r="16" fill="none" stroke="#ff8a6b" stroke-width="3"/>'
         '<circle cx="210" cy="30" r="8" fill="#ffb199"/>'
         '<rect x="294" y="14" width="32" height="32" fill="none" stroke="#ff8a6b" stroke-width="3"/></svg>')


def cover(first=True):
    if first:
        inner = f"""
    <div class="eyebrow coral">코드 너머의 시리즈</div>
    <h1 class="cover-title">DevRel <span class="coral-t">Next</span></h1>
    <p class="cover-sub">코드 너머의 관계 — AI 시대, DevRel은 누구와 무엇을 잇는가</p>
    {MOTIF}
    <p class="cover-quote">"DevRel을 했고, 지금은 AX를 한다."</p>
    <p class="cover-by">— 하는 일을 동사로 적어보면, 두 일의 목록은 꽤 겹친다</p>
    <div class="cover-meta"><span>김상기 · 1시간 발표</span><span class="mono dim">ksangki/devrel-next · {VER}</span></div>"""
    else:
        inner = f"""
    <div class="eyebrow coral">감사합니다</div>
    <h1 class="cover-title end">DevRel <span class="coral-t">Next</span></h1>
    <p class="cover-sub">코드 너머의 관계</p>
    {MOTIF}
    <p class="cover-quote">워크시트·체크리스트·설계 캔버스는 부록 A~C에 있습니다.</p>
    <div class="cover-meta"><span>웹에서 읽기 · ksangki.github.io/devrel-next</span><span class="mono dim">EPUB · 저장소 epub/ 폴더</span></div>"""
    slides.append(("cover", "OPENING" if first else "CLOSING",
                   '<div class="corner tl"></div><div class="corner tr"></div>'
                   '<div class="corner bl"></div><div class="corner br"></div>'
                   f'<div class="cover-wrap">{inner}</div>'))


def divider(sec, eyebrow, title, sub, chapters):
    ch = ''.join(f'<li>{c}</li>' for c in chapters)
    slides.append(("div", sec, f"""
  <div class="div-wrap">
    <div>
      <div class="eyebrow coral">{eyebrow}</div>
      <h2 class="div-title">{title}</h2>
      <p class="div-sub">{sub}</p>
      {MOTIF}
    </div>
    <ul class="div-ch">{ch}</ul>
  </div>"""))


def _head(eyebrow, title):
    return (f'<div class="eyebrow cream">{eyebrow}</div><h2 class="content-title">{title}</h2>'
            '<div class="bar small"></div>')


def _opt(cls, s):
    return f'<p class="{cls}">{s}</p>' if s else ''


def cards(sec, eyebrow, title, items, lead=None, foot=None, cols=3):
    cs = ''.join(f'<div class="card"><div class="card-num mono">{i + 1:02d}</div>'
                 f'<div class="card-h">{h}</div><div class="card-sub">{s}</div></div>'
                 for i, (h, s) in enumerate(items))
    slides.append(("content", sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<div class="grid grid-{cols}">{cs}</div>' + _opt('foot-note', foot)))


def quote(sec, eyebrow, title, q, src=None, after=None):
    slides.append(("content", sec, _head(eyebrow, title) + f'<blockquote class="bigq">{q}</blockquote>'
                   + _opt('q-src', src) + _opt('after', after)))


def table(sec, eyebrow, title, head, rows, lead=None, foot=None):
    th = ''.join(f'<th>{c}</th>' for c in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    slides.append(("content", sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<table class="deck-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
                   + _opt('foot-note', foot)))


def stat(sec, eyebrow, title, pairs, foot=None):
    st = ''.join(f'<div class="stat"><div class="stat-n">{n}</div><div class="stat-l">{l}</div></div>'
                 for n, l in pairs)
    slides.append(("content", sec, _head(eyebrow, title) + f'<div class="stat-row">{st}</div>'
                   + _opt('foot-note', foot)))


FIGDIR = pathlib.Path(__file__).resolve().parent.parent / 'figures'


def _ratio(fid):
    import re
    vb = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', (FIGDIR / f'fig-{fid}.svg').read_text(encoding='utf-8'))
    return float(vb.group(2)) / float(vb.group(1))


def figure(sec, eyebrow, title, fid, cap, foot=None):
    img = f'<img src="../figures/fig-{fid}.svg" alt="{cap}" />'
    if _ratio(fid) > 0.62:   # 세로로 긴 그림 → 2단(설명 | 그림)
        slides.append(("content split", sec,
                       f'<div class="split"><div class="split-text">{_head(eyebrow, title)}'
                       f'<p class="split-cap">{cap}</p>{_opt("foot-note", foot)}</div>'
                       f'<figure class="deck-fig tall">{img}</figure></div>'))
    else:
        slides.append(("content", sec, _head(eyebrow, title)
                       + f'<figure class="deck-fig">{img}<figcaption>{cap}</figcaption></figure>'
                       + _opt('foot-note', foot)))


def bullets(sec, eyebrow, title, items, lead=None, foot=None):
    li = ''.join(f'<li>{i}</li>' for i in items)
    slides.append(("content", sec, _head(eyebrow, title) + _opt('lead', lead)
                   + f'<ul class="big-list">{li}</ul>' + _opt('foot-note', foot)))


# ═════════════════════════ OPENING ═════════════════════════
cover()

table("결론부터", "결론부터", "이 책이 하려는 말은 한 문장이다",
      ["", "예전", "지금"],
      [["누구와", "전문 개발자", "빌더(스스로 개발자라 부르지 않는 사람) · 에이전트 · 회사 안의 동료"],
       ["무엇으로", "튜토리얼 · 검색 · 포럼", "에이전트가 읽는 정확한 문서 · 관계형 커뮤니티 · 만든 증거"],
       ["잇는 일", "", "번역 · 피드백 · 신뢰 · 먼저 가보기"]],
      lead="<span class='coral-t big'>DevRel은 죽지 않았다.<br>'개발자 관계'에서 '만드는 사람과의 관계'로 넓어진다.</span>",
      foot="오늘 발표는 이 표의 세 줄을 차례로 보여 드리는 순서로 갑니다.")

quote("결론부터", "왜 이 이야기를", "DevRel을 했고, 지금은 AX를 한다",
      "DevRel은 회사 바깥의 개발자와 관계를 맺는 일이다. 그들이 부딪힌 벽은 회사 안의 제품 팀에 전한다.<br>지금 내가 하는 AX는 조직 안에 AI를 퍼뜨리는 일이다.<br>"
      "<span class='coral-t'>두 일을 동사로 적어보면 목록이 꽤 겹친다.</span>",
      "— 서문",
      "먼저 써보고, 가르치고, 보여주고, 막힌 곳을 모아 되돌려준다. 그 동사가 향하는 사람이 회사 안의 동료로 바뀌면, 그 일은 무엇이 될까?")

bullets("결론부터", "순서", "오늘 이야기의 순서", [
    "<b>1. 정말 죽었나?</b> — 부고의 기록과, DevRel이 원래 하던 일",
    "<b>2. 누구와, 무엇으로가 바뀌었다</b> — 빌더와 에이전트, 달라진 통로",
    "<b>3. 직함은 흩어지고 기능은 남는다</b> — 채용 공고 속 네 가지 기능",
    "<b>4. 회사 안으로</b> — 퍼뜨리는 기술이 동료를 향할 때, 그리고 전망",
])

# ═════════════════════════ PART 1 ═════════════════════════
divider("PART 1", "PART 1", "정말 죽었나?",
        "결론에 보태는 것 — 잘려 나간 것은 '잇는 일'이 아니라, 숫자로 설명되지 않던 자리와 옛 방식이었다.",
        ["1장. DevRel은 죽었는가", "2장. 경계에 선 사람들"])

quote("PART 1", "작별 편지", "\"Goodbye, forever, probably.\"",
      "\"AI is killing developer education.\"<br><span class='small-q'>AI가 개발자 교육을 죽이고 있다.</span>",
      "— Salma Alam-Naylor, 2026-07-02 블로그. DevRel을 떠났고, 프로필 직함은 Staff Engineer.",
      "한 사람의 이직이 한 직업의 부고처럼 읽혔다. 비슷한 글이 2023년부터 이어졌다.")

figure("PART 1", "3년의 기록", "2023~2026년, 당사자들이 남긴 글", "1-1",
       "그림 1. 2023~2026년 DevRel 당사자들이 남긴 글",
       "떠난다는 글만 있지 않았다. \"죽지 않았다, 바뀌는 중이다\"라는 반론도 같은 시기에 나왔다.")

stat("PART 1", "숫자 읽기", "위기의 숫자는 무엇을 셌는지부터 본다", [
    ("14.6%", "그해 해고를 겪은 <b>응답자 본인</b><br>State of DevRel 2024, 310명 설문"),
    ("26.1%", "해고를 겪은 <b>팀</b><br>Common Room 2023, 136명 벤더 설문"),
    ("약 6%", "Google <b>회사 전체</b> 감원(2023-01)<br>DevRel만의 숫자가 아니다"),
], foot="같은 '위기'를 말해도 사람·팀·회사 전체를 따로 셌다. 숫자를 옮길 때 무엇을 셌는지를 함께 적어야 한다.")

figure("PART 1", "왜 잘렸나", "성과를 숫자로 보여 주기 어려웠다", "1-2",
       "그림 2. 당사자들이 말한 측정 압박의 경로",
       "DevRel 실무자가 꼽은 가장 큰 어려움: <b>데이터로 영향을 증명하는 일(60.7%)</b> — State of DevRel 2024, 310명 실무자 설문.")

figure("PART 1", "원래 하던 일", "DevRel은 회사와 개발자 사이에서 양쪽 말을 옮기는 자리였다", "2-1",
       "그림 3. 경계 역할로서의 DevRel — 모든 선이 양방향이다",
       "1984년 매킨토시의 '에반젤리스트'로 시작해, 설득 위에 '피드백 전달'이 더해졌다.")

quote("PART 1", "당사자의 말", "DevRel 스스로는 이 일을 이렇게 설명한다",
      "\"represents the company to the community<br>and the community to the company\"<br>"
      "<span class='small-q'>회사를 커뮤니티에, 커뮤니티를 회사에 대변한다.</span>",
      "— Catalin Pit, 2023-10-31 블로그",
      "\"다리(bridge)\"(Xe Iaso), \"서로 다른 세계 사이를 번역한다\"(Ashley Willis) — 직함과 회사는 달라도 같은 자리를 가리킨다.")

quote("PART 1", "PART 1 정리", "그래서 이 책은 DevRel을 두 질문으로 읽는다",
      "<span class='coral-t'>누구와</span> 관계를 맺는가?<br><span class='coral-t'>무엇으로</span> 관계를 맺는가?",
      None,
      "이 두 질문의 답이 동시에 바뀌었다는 것이 PART 2의 이야기다.")

# ═════════════════════════ PART 2 ═════════════════════════
divider("PART 2", "PART 2", "누구와, 무엇으로가 바뀌었다",
        "결론에 보태는 것 — 청중은 빌더와 에이전트로 넓어졌고, 관계를 잇는 통로도 바뀌었다.",
        ["3장. 'D'가 넓어졌다", "4장. 새 독자, 에이전트", "5장. 'R'의 수단이 바뀌었다"])

figure("PART 2", "빌더", "개발자라 부르지 않는 사람도 만든다", "3-2",
       "그림 6. DevRel이 마주한 청중의 띠",
       "비개발자가 만드는 일은 새 이야기가 아니다(2011년 연구도 \"대부분의 프로그램은 전문 개발자가 쓰지 않는다\"고 했다). 달라진 것은 규모와 결과물이다.")

stat("PART 2", "전문 개발자", "전문 개발자도 AI를 쓰지만, 믿지는 않는다", [
    ("84%", "AI 도구를 쓰거나 쓸 계획"),
    ("46%", "정확도를 믿지 못한다(믿는다 33%)"),
    ("66%", "가장 큰 불만: \"거의 맞지만 딱 맞지는 않는 답\""),
], foot="Stack Overflow 개발자 설문 2025, 약 49,000명, 자기선택 표본. DevRel의 청중은 '처음 만드는 사람'부터 'AI를 의심하는 전문가'까지 한 줄로 이어진다.")

quote("PART 2", "에이전트", "Supabase를 고른 것은 누구였나",
      "\"without ever talking to us\"<br><span class='small-q'>우리와 한 번도 이야기하지 않고</span>",
      "— Thor Schaeff, DevRelCon New York 2025-07",
      "AI 빌더 서비스들이 Supabase를 골랐다. LLM에게 \"데이터를 어디에 저장하면 되지?\"라고 물으면 Supabase라고 답했기 때문이라고 그는 전했다. <b>에이전트가 새 독자다.</b>")

figure("PART 2", "15개월", "에이전트를 위한 표준이 빠르게 생겼다", "4-1",
       "그림 7. 에이전트를 위한 표준·제품 타임라인(2024-09~2025-12)",
       "llms.txt, MCP, 'Agent Experience(에이전트도 사용자다)'라는 말까지 15개월 사이에 나왔다.")

cards("PART 2", "숫자 읽기", "\"측정된 웹 트래픽의 66%가 에이전트\" — 이렇게 읽는다", [
    ("누가 셌나", "문서 호스팅 회사 Mintlify가 자기 고객 사이트를 셌다(벤더 자체 집계)."),
    ("단위가 다르다", "에이전트는 '요청' 수, 사람은 '페이지 로드' 수. 같은 자로 잰 비율이 아니다."),
    ("방향으로 본다", "반년 사이 네 배 넘게 늘었다는 방향만 믿고, 자기 로그로 확인하자."),
])

quote("PART 2", "국내에서도", "국내 DevRel 매니저도 같은 변화를 적었다",
      "\"이제는 개발자뿐만 아니라 AI가 나와 회사의 글을<br>검색하고 읽는 시대가 되었고…\"",
      "— josephyang(스스로를 SK플래닛 DevRel Manager라고 소개), 데보션 2025-10-20 기술 블로그 개선 실험",
      "사람의 조회수가 높지 않은 글도 AEO/AIO 전략에 맞춰 발행하면 AI가 잘 찾는 사례가 있다고 적었다(필자 한 사람의 관찰). 개발자와 함께 <b>AI도 회사의 글을 읽는 독자</b>가 됐다는 말이다.")

figure("PART 2", "통로", "문서가 입구였던 회사에 생긴 일", "5-1",
       "그림 9. Tailwind의 퍼널에 코딩 에이전트가 끼어든 자리",
       "Tailwind는 문서 트래픽이 약 40% 줄었다(창업자 증언). 에이전트가 대신 코드를 써 주면 사람은 문서에 오지 않는다 — 이것은 이 책의 해석이다.")

figure("PART 2", "두 퍼널", "사람에게는 신뢰, 에이전트에게는 정확성", "5-2",
       "그림 10. 개발자·검색 크롤러·LLM — 세 유통 표면과 두 퍼널",
       "공개 Q&A는 줄었지만, 관계로 묶인 커뮤니티는 측정된 범위에서 버텼다.")

cards("PART 2", "PART 2 정리", "그래서 무엇으로 이어야 하나", [
    ("에이전트가 읽는 문서", "모델이 모르는 것(최신 API, 비표준 규칙)을 짧고 정확하게."),
    ("관계형 커뮤니티", "정답만 주고받는 곳보다 서로 아는 사람들의 공간이 버틴다."),
    ("만든 증거", "조회수 대신 배포하고, 호출하고, PR을 보낸 흔적을 센다."),
], foot="반대로 신뢰를 잃는 가장 빠른 길은 AI 응원단이 되는 것이다 — \"모든 DevRel 자리에 AI 응원이 딸려 온다\"는 자조가 나온다.")

# ═════════════════════════ PART 3 ═════════════════════════
divider("PART 3", "PART 3", "직함은 흩어지고 기능은 남는다",
        "결론에 보태는 것 — 그날의 공고에서, 잇는 일은 DevRel 공고와 FDE 공고의 문장에 함께 적혀 있었다.",
        ["6장. 공고를 읽다", "7장. 직업에서 역량으로"])

table("PART 3", "채용 공고", "2026년 9월 25일, 같은 날 열어 본 채용 페이지",
      ["회사", "'DevRel' 이름의 공고", "현장 배치형(FDE)·솔루션 공고"],
      [["Anthropic", "1", "Applied AI 38 · FDE 계열 7"],
       ["OpenAI", "0 (DX Engineer 1)", "Forward Deployed 22"],
       ["Supabase", "3", "—"],
       ["ElevenLabs", "0 (DX Engineer 1)", "FDE 계열 16"]],
      foot="표 10 발췌 · 하루치 공개 목록이며 추세가 아니다. 'DevRel'이라는 이름보다 고객 곁으로 가는 직함이 훨씬 많다.")

figure("PART 3", "어디로 갔나", "DevRel을 떠난 사람들이 간 곳", "6-1",
       "그림 11. DevRel이라는 이름을 떠난 공개 기록들 — 다섯 방향")

cards("PART 3", "네 가지 기능", "공고마다 되풀이되는 네 가지 일", [
    ("번역", "회사의 말을 개발자의 말로, 개발자의 말을 회사의 말로 옮긴다."),
    ("피드백", "막힌 곳을 모아 제품 팀에 되돌려 준다."),
    ("신뢰", "가르치고 쌓은 결과물이 믿음이 된다."),
    ("먼저 가보기", "먼저 써 보고 알아낸다. 나머지 셋의 재료가 된다."),
], cols=4, foot="직함은 DevRel, FDE, DX Engineer, 교육 담당, 사내 AX로 흩어져도 이 네 가지는 공고 문구에 계속 나온다.")

table("PART 3", "커리어", "네 가지 기능을 가진 사람이 가는 곳",
      ["가는 곳", "가장 많이 쓰는 기능"],
      [["FDE·솔루션 엔지니어", "번역, 피드백"],
       ["제품 엔지니어", "먼저 가보기"],
       ["교육 담당", "신뢰, 번역"],
       ["사내 AX", "네 가지 모두 — 청중이 회사 안 동료"]],
      lead="DevRel 실무자의 61%가 \"정해진 커리어 경로가 없다\"고 답했다(State of DevRel 2024). 대신 기능으로 보면 갈 길이 여럿이다.")

figure("PART 3", "리더에게", "리더는 세 가지를 차례로 정한다", "7-2",
       "그림 14. 리더가 차례로 답할 세 질문")

# ═════════════════════════ PART 4 ═════════════════════════
divider("PART 4", "PART 4", "회사 안으로, 그리고 다음",
        "결론에 보태는 것 — 만드는 사람은 회사 안에도 있다. 다만 효과는 아직 증명 전이다.",
        ["8장. 퍼뜨리는 기술", "9장. AX를 DevRel처럼 운영하기", "10장. DevRel 다음"])

quote("PART 4", "반전", "DevRel이 회사 전체의 AI 확산을 맡았다",
      "\"plot twist: we're not dead.<br>We're standing on the biggest stage of our careers.\"<br>"
      "<span class='small-q'>반전: 우리는 죽지 않았다. 커리어에서 가장 큰 무대에 서 있다.</span>",
      "— Angie Jones(Block), 2025-10-20 블로그",
      "Block의 DevRel 팀은 낯선 AI 에이전트 앞에서도 늘 하던 대로 했다. \"먼저 가 보고, 알아내고, 다른 사람을 안내한다.\"")

figure("PART 4", "옮겨 간 자리", "바깥에서 하던 일이 회사 안의 장치가 됐다", "8-1",
       "그림 15. DevRel의 활동이 사내 AI 확산의 장치로 옮겨간 자리",
       "밋업은 사내 세션으로, 행사는 팀 방문으로, 커뮤니티 사례 모으기는 사내 사례 공유로.")

quote("PART 4", "저자의 기록", "무엇으로 잴 것인가 — 저자가 공개로 남긴 기록",
      "\"AI 시대에 \"잘했다\"를 토큰 사용량 같은 입력 지표로 재면 방향이 틀어집니다.\"<br>"
      "<span class='coral-t'>\"진짜 신호는 검증된 결과입니다.\"</span>",
      "— 저자가 2026-06-30 데보션에 공개로 남긴, AX를 코드로 구현한 6개월의 기록",
      "사용량이 아니라 결과를 센다 — PART 2에서 본 '만든 증거'와 같은 방향이다. 다만 한 사람의 기록이지 효과의 증거는 아니다.")

cards("PART 4", "솔직하게", "아직 증명되지 않은 것", [
    ("사례가 적다", "공개 사례는 Block·카카오·SK플래닛의 기록과 Anthropic 공고 한 건, 대부분 당사자의 기록이다."),
    ("효과 연구가 없다", "사내 AI 챔피언의 효과를 숫자로 보인 연구는 이 책의 조사 범위에서 찾지 못했다."),
    ("그래서", "이 주장은 가능성이다. 이론과 사례로 뒷받침할 뿐, 입증된 결론은 아니다."),
])

figure("PART 4", "설계", "사내 AI 확산은 세 다이얼로 설계한다", "9-1",
       "그림 17. 강도·측정·공유 장치",
       "커뮤니티형이 의무화보다 낫다는 비교 연구는 없다. 그래서 눈금에 좋고 나쁨을 표시하지 않았다.")

figure("PART 4", "함정", "사용량을 세면 사람들은 사용량을 연기한다", "9-2",
       "그림 18. 강도를 올리고 사용량을 세면 생기는 일",
       "그래서 셀 것은 사용량이 아니라 <b>만든 증거</b>와 그 덕분에 달라진 것이다.")

figure("PART 4", "전망", "네 갈래 전망은 하나의 결론으로 모인다", "10-1",
       "그림 19. 1장의 네 이야기와 새 출발점 하나에서 이어지는 네 전망",
       "흩어지고(해체), 넓어지고(확장), 거품이 빠지고(교정), 안으로 향한다(내향) — 넷은 결론의 세 축에 자리를 잡는다. 확장·내향은 '누구와', 교정은 '무엇으로', 해체는 '잇는 일'의 질문이다.")

# ═════════════════════════ CLOSING ═════════════════════════
quote("CLOSING", "결론", "다시, 한 문장",
      "DevRel은 죽지 않았다.<br><span class='coral-t'>'개발자 관계'에서 '만드는 사람과의 관계'로 넓어진다.</span>",
      None,
      "누구와: 빌더·에이전트·회사 안 동료 · 무엇으로: 에이전트가 읽는 문서·관계형 커뮤니티·만든 증거 · 잇는 일: 번역·피드백·신뢰·먼저 가보기")

cards("CLOSING", "내일 해 볼 것", "책을 덮으며 해 볼 한 가지", [
    ("한 문장으로 쓴다", "이번 주에 한 일 하나를 — 누구를 향했고, 무엇으로 닿았는지 보이게."),
    ("다른 부서에 보여 준다", "동료 한 사람에게 자기 말로 다시 설명해 달라고 부탁한다."),
    ("차이를 좁힌다", "돌아온 설명과 내 문장의 차이 — 그 간격을 좁히는 것이 이 일이다."),
])

cover(first=False)

# ═════════════════════════ 렌더 ═════════════════════════
TOTAL = len(slides)
body, cnt = [], {}
for i, (kind, sec, inner) in enumerate(slides, 1):
    cnt[sec] = cnt.get(sec, 0) + 1
    body.append(f'<section class="slide {kind}" id="s{i}" data-n="{i}">{inner}'
                f'<div class="page-num mono">{i:03d} / {TOTAL}</div>'
                f'<div class="page-section mono">{sec} / {cnt[sec]:02d}</div>'
                f'<div class="page-footer"><span>{BOOK}</span><span>{BY}</span></div></section>')

CSS = """
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
:root{--bg:#17121f;--panel:#211a2c;--line:#342a40;--text:#f2ecf5;--muted:#a99cb6;--dim:#7d6c90;
 --coral:#ff8a6b;--coral-d:#d4604a;--cream:#efe8f2;--pad:clamp(2rem,4.5vw,4.2rem)}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);color:var(--text);font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;
 scroll-snap-type:y mandatory;overflow-y:scroll;height:100vh;word-break:keep-all}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.progress-bar{position:fixed;top:0;left:0;right:0;height:3px;background:#0f0b15;z-index:99}
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
.cover{background:radial-gradient(1200px 600px at 50% 0%,#2a1d38 0%,#17121f 70%)}
.cover-wrap{max-width:62rem}
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
.div{background:linear-gradient(120deg,#2a1d38 0%,#17121f 65%)}
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
.deck-fig img{display:block;margin:0 auto;max-width:100%;max-height:calc(100vh - 19rem);width:auto;height:auto;background:#fbf7f2;border-radius:12px;padding:8px}
.split{display:grid;grid-template-columns:.9fr 1.1fr;gap:2.4rem;align-items:center}
.split-cap{color:var(--cream);font-size:clamp(.95rem,1.6vw,1.1rem);line-height:1.6;margin-top:.4rem}
.deck-fig.tall img{max-height:calc(100vh - 6rem)}
.deck-fig figcaption{color:var(--dim);font-size:.88rem;margin-top:.6rem}
.page-num{position:absolute;top:1.5rem;right:1.8rem;color:var(--dim);font-size:.8rem}
.page-section{position:absolute;top:1.5rem;left:1.8rem;color:var(--dim);font-size:.8rem;letter-spacing:.08em}
.page-footer{position:absolute;bottom:1.2rem;left:1.8rem;right:1.8rem;display:flex;justify-content:space-between;gap:1rem;color:#5a4d68;font-size:.75rem}
.cover .page-num{top:3.5rem;right:3.6rem}.cover .page-section{top:3.5rem;left:3.6rem}.cover .page-footer{bottom:3.2rem;left:3.6rem;right:3.6rem}
@media(max-width:900px){.grid-3,.grid-4{grid-template-columns:1fr}.div-wrap,.split{grid-template-columns:1fr}.deck-fig img,.deck-fig.tall img{max-height:none;width:100%}
 .page-footer{display:none}.slide{min-height:auto;padding:2.4rem 1.1rem 3rem}.deck-table{display:block;overflow-x:auto}}
@media print{body{height:auto;overflow:visible;background:#fff;color:#111}
 .slide{page-break-after:always;min-height:auto;border:none;background:#fff!important;color:#111}
 .card,.stat,.deck-table th{background:#f6f1f7!important;border-color:#ccc!important}
 .content-title,.card-h,.div-title,.cover-title{color:#111}.card-sub,.lead,.foot-note,.div-sub,.after{color:#444}.progress-bar{display:none}}
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
doc = (f'<!doctype html><html lang="ko"><head><meta charset="utf-8">'
       f'<meta name="viewport" content="width=device-width, initial-scale=1">'
       f'<title>{BOOK} — 1시간 발표 자료</title><style>{CSS}</style></head><body>'
       f'<div class="progress-bar"><div class="progress-fill" id="progress"></div></div><main>'
       + '\n'.join(body) + f'</main><script>{JS}</script></body></html>')
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(doc, encoding='utf-8')
print(f"deck build 완료 — {TOTAL}장, 그림 {doc.count('../figures/')}점")
