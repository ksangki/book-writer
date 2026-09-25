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
VER = "v1.1.0"
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

cards("OPENING", "ABOUT THIS TALK", "이 발표가 답하려는 질문", [
    ("\"DevRel은 죽었다\"는 부고가 쌓였다", "2023년부터 3년 넘게 작별 편지가 이어졌다. 한 사람의 이직이 한 직업의 부고처럼 읽혔다."),
    ("그 사이 'D'와 'R'이 함께 움직였다", "개발자라 스스로 부르지 않는 빌더가 만들고, 에이전트가 문서를 읽고, 통로가 약해졌다."),
    ("그래서 이 일은 무엇이 되는가", "죽었는지가 아니라, 무엇이 남고 어디로 옮겨 가는지를 공개 자료로 따라간다."),
])

cards("OPENING", "PROMISES", "이 발표가 지키는 세 가지", [
    ("기준 시점을 적는다", "동향·공고·수치는 2026년 9월 시점. 채용 공고는 2026년 9월 25일에 본 공개 목록이다."),
    ("수치에는 라벨을 붙인다", "누가 조사했는지, 표본이 얼마인지, 벤더 데이터인지 논문인지를 숫자 옆에 적는다."),
    ("예측은 예측으로 적는다", "전망에는 [예측] 라벨과 반대 의견, 확인할 관찰 지표를 같은 자리에 둔다."),
])

quote("OPENING", "WHY ME", "DevRel을 했고, 지금은 AX를 한다",
      "DevRel은 회사 바깥의 개발자와 관계를 맺는 일이다.<br>AX는 조직 안에 AI를 퍼뜨리는 일이다.<br>"
      "<span class='coral-t'>하는 일을 동사로 적어보면 두 일의 목록은 꽤 겹친다.</span>",
      "— 서문",
      "먼저 써보고, 가르치고, 보여주고, 막힌 곳을 모아 되돌려준다. 이 발표는 그 겹침이 우연인지, 직업의 다음 모습인지를 묻는다.")

bullets("OPENING", "AGENDA", "오늘 1시간 동안", [
    "<b>PART 1 부고와 계보</b> — DevRel은 정말 죽었나, 그리고 원래 무슨 일을 했나",
    "<b>PART 2 D와 R이 바뀌었다</b> — 빌더와 에이전트라는 새 청중, 약해진 통로",
    "<b>PART 3 직함은 흩어지고 기능은 남는다</b> — 하루치 채용 공고로 읽는 네 가지 기능",
    "<b>PART 4 회사 안으로, 그리고 그다음</b> — 내부 DevRel로서의 AX, 네 갈래 전망",
], foot="각 PART 끝에 다음 주에 쓸 수 있는 질문을 하나씩 남깁니다.")

# ═════════════════════════ PART 1 ═════════════════════════
divider("PART 1", "PART 1", "부고와 계보",
        "죽음을 선고받은 직업의 기록을 먼저 읽고, 이 일이 원래 무엇이었는지로 돌아간다.",
        ["1장. DevRel은 죽었는가", "2장. 경계에 선 사람들"])

quote("PART 1", "THE OBITUARY", "\"Goodbye, forever, probably.\"",
      "\"AI is killing developer education.\"",
      "— Salma Alam-Naylor, 2026-07-02 블로그. DevRel을 떠나며 쓴 글의 소제목. 그의 프로필에는 이제 Staff Engineer가 적혀 있다.",
      "한 사람의 이직 소식이 왜 이렇게 크게 읽혔을까? 글이 개인의 사정에서 멈추지 않았기 때문이다.")

figure("PART 1", "LETTERS", "2023~2026년, 당사자들이 남긴 글", "1-1",
       "그림 1. 2023~2026년 DevRel 당사자들이 남긴 글",
       "작별만 있는 것은 아니다 — 같은 시기에 \"isn't dead, it's just evolving\"(Sam Julien, 2024-03)도, \"overblown\"(Daniel Bryant, 2024-02)도 나왔다.")

stat("PART 1", "NUMBERS", "위기의 숫자는 단위부터 읽는다", [
    ("14.6%", "그해 해고를 겪은 <b>응답자 본인</b> — State of DevRel 2024, 유효 응답 310명, 자기선택"),
    ("18.1%", "해고로 인원이 줄어든 <b>프로그램</b> — 같은 조사"),
    ("26.1%", "해고를 겪은 <b>팀</b> — Common Room 2023, 응답 136명, 벤더 설문"),
    ("약 6%", "Google <b>전체 직원</b> 감원(2023-01) — 보도, DevRel 단독 수치 아님"),
], foot="같은 \"위기\"를 가리키는 숫자들이 서로 다른 것을 셌다. 사람인지, 프로그램인지, 팀인지, 회사 전체인지부터.")

table("PART 1", "FOUR STORIES", "죽음을 설명하는 네 가지 이야기",
      ["이야기", "대표 목소리(시점)", "핵심 문장"],
      [["거품 교정론", "swyx (2024-07)", "\"ZIRP DevRel is dead ... the 'Jobs To Be Done' of DevRel are timeless needs\""],
       ["자기 실패론", "Keith Casey (2024-07-17)", "\"Developer Relations is dying because devrel failed their organizations.\""],
       ["재구조화론", "Lee Briggs (2024-12-10)", "\"Professionals who adapt—aligning their work with sales, customer success, or product teams—will continue to thrive.\""],
       ["부활론", "swyx (2025-10)", "\"reports of DevRel's death have been greatly exaggerated\""]],
      foot="표 3. 네 이야기는 마지막 10장에서 네 갈래 전망으로 다시 돌아옵니다.")

figure("PART 1", "MEASUREMENT", "측정할 수 없는 일의 운명", "1-2",
       "그림 2. 당사자들이 말한 측정 압박의 경로",
       "State of DevRel 2024(n=310, 실무자 설문)가 꼽은 가장 큰 과제: <b>데이터와 지표로 영향을 증명하는 일, 60.7%</b>.")

cards("PART 1", "ORIGIN", "1984년, 매킨토시를 위한 설득", [
    ("에반젤리스트", "서드파티 개발자를 플랫폼으로 데려오는 일. 가치 창출의 중심이 기업 밖으로 옮겨간다는 플랫폼 경제학에 뿌리가 닿는다."),
    ("애드보킷", "설득 위에 피드백이라는 방향이 더해졌다. 교체가 아니라 누적이다."),
    ("경계에 서다", "이때부터 이 일은 회사와 개발자 사이의 경계에 선다 — 양쪽의 말을 번역한다."),
])

figure("PART 1", "BOUNDARY ROLE", "경계 역할 — 번역하고 중개하는 사람", "2-1",
       "그림 3. 경계 역할로서의 DevRel — 모든 선이 양방향이다",
       "Tushman(1977)의 경계 역할: 바깥의 정보를 들여오고, 안에서 통하는 말로 번역하고, 필요한 곳에 퍼뜨린다.")

table("PART 1", "IN THEIR WORDS", "당사자들이 자기 일을 설명한 말",
      ["이름", "날짜·플랫폼", "원문"],
      [["Catalin Pit", "2023-10-31, 블로그", "\"represents the company to the community and the community to the company\""],
       ["Xe Iaso", "2023-10-24, 블로그", "\"you are the bridge between the company and the community of developers …\""],
       ["Ashley Willis", "2025-04-25, 블로그", "\"translate between worlds\""],
       ["Una Kravets", "2024-03-08, X", "\"a liaison for user needs, architect of the solution, test user to provide feedback, and only then a GTM strategist\""]],
      foot="표 5. 직함과 회사는 달라도 같은 자리를 가리킨다 — 양쪽을 잇는 사람.")

figure("PART 1", "LINEAGE", "측정의 계보 — AAARRRP에서 Orbit까지", "2-2",
       "그림 4. DevRel 측정 틀의 계보 — 2012년 DX 정의부터 2024년 Orbit의 인수까지",
       "틀은 계속 나왔지만 난제는 남았다. 경계 역할의 가치는 <b>다른 부서의 숫자</b>로 나타나기 때문이다.")

quote("PART 1", "FRAME", "이 책이 DevRel을 읽는 틀",
      "DevRel = <span class='coral-t'>D</span>(누구에게) × <span class='coral-t'>R</span>(무엇으로)<br>두 변수로 이루어진 경계 역할",
      None,
      "PART 2는 이 두 변수가 동시에 움직였다는 이야기입니다. <b>다음 주 질문:</b> 우리 DevRel의 D와 R을 한 문장씩 적으면 무엇인가?")

# ═════════════════════════ PART 2 ═════════════════════════
divider("PART 2", "PART 2", "D와 R이 바뀌었다",
        "청중(D)은 빌더와 에이전트로 넓어졌고, 관계의 수단(R)은 통로째 다시 배선되고 있다.",
        ["3장. 'D'가 넓어졌다", "4장. 새 독자, 에이전트", "5장. 'R'의 수단이 바뀌었다"])

figure("PART 2", "NOT NEW", "새 이야기가 아니다", "3-1",
       "그림 5. 최종 사용자 프로그래밍에서 바이브 코딩까지 — 다섯 시점",
       "2011년 서베이도 이미 \"대부분의 프로그램은 전문 개발자가 쓰지 않는다\"고 적었다. 바이브 코딩은 그 흐름의 새 물결이고, 달라진 것은 규모와 산출물이다.")

figure("PART 2", "AUDIENCE", "DevRel이 마주한 청중의 띠", "3-2",
       "그림 6. 자연어로 첫 앱을 띄운 사람부터 AI를 의심하며 쓰는 전문 개발자까지",
       "빌더 도구의 공개 수치는 대부분 회사 자체 발표다 — <b>독립 기관이 검증한 수치는 표 6에 없다.</b>")

stat("PART 2", "PROFESSIONALS", "전문 개발자는 AI를 어떻게 느끼나", [
    ("84%", "AI 도구를 쓰고 있거나 쓸 계획"),
    ("46% vs 33%", "정확도를 믿지 못한다 vs 믿는다"),
    ("66%", "가장 큰 불만: <b>\"almost right, but not quite\"</b>"),
], foot="Stack Overflow Developer Survey 2025, 약 49,000명, 개발자 한정 자기선택 표본.")

quote("PART 2", "NEW READER", "Supabase를 고른 것은 누구였나",
      "\"without ever talking to us\"<br>\"Hey, actually now machines are writing the code.\"",
      "— Thor Schaeff, DevRelCon New York 2025-07, \"DX for Humans and Machines\"",
      "AI 빌더 서비스들이 Supabase를 DevRel과 한 번도 대화하지 않고 통합했다. LLM에게 무엇을 쓰면 되느냐고 물으면 Supabase라고 답했기 때문이다.")

figure("PART 2", "15 MONTHS", "에이전트를 위한 표준이 생긴 15개월", "4-1",
       "그림 7. 에이전트를 위한 표준·제품 타임라인(2024-09~2025-12)")

figure("PART 2", "AGENT EXPERIENCE", "에이전트도 사용자다", "4-2",
       "그림 8. 사용자 경험의 계보 — Biilmann의 UX·DX·AX에 Lawson의 정의와 가장 가까운 학술 개념을 더해",
       "에이전트를 위해 걷어낸 마찰은 사람에게도 이롭다.")

cards("PART 2", "READ VENDOR DATA", "\"에이전트가 66%\" — 이 숫자를 어떻게 읽나", [
    ("무엇을 셌나", "\"Agents now account for 66% of measured web-traffic.\" — Mintlify 2026 midyear report, 자사 호스팅 문서 사이트 집계"),
    ("단위가 다르다", "에이전트는 <b>요청</b> 수(2억 1,300만), 사람은 <b>페이지 로드</b> 수(1억 500만). 같은 자로 잰 비율이 아니다."),
    ("방향으로 읽는다", "연초 15.2%에서 반년 사이 네 배 넘게. 벤더 자사 데이터이니 자기 로그로 확인하자."),
])

quote("PART 2", "COUNTERPOINT", "반론 — llms.txt는 아무도 읽지 않는다?",
      "\"FWIW no AI system currently uses llms.txt.\"",
      "— John Mueller(Google), 2025, 언론 인용 · \"/llms.txt is not requested by anything\"(HermanMartinus, Hacker News, 2026-06)",
      "연구가 가리키는 원칙은 형식이 아니라 내용이다 — <b>모델이 모르는 것(비표준 규칙, 최신 API)을 간결하게</b>. 점검 항목은 부록 B.")

figure("PART 2", "TAILWIND", "문서가 입구였던 퍼널", "5-1",
       "그림 9. Tailwind의 퍼널에 코딩 에이전트가 끼어든 자리",
       "반론: \"The real signal is conversions.\"(zdragnar, HN) — 전환율을 보지 않고는 원인을 단정할 수 없다. 에이전트 경로는 이 책의 해석이다.")

table("PART 2", "CHANNELS", "관계의 통로별로 본 변화와 그 근거",
      ["통로", "변화", "근거의 성격"],
      [["문서 사이트", "Tailwind 문서 트래픽 2023년 초 대비 약 40% 감소", "창업자 1차 증언, 방법 미공개"],
       ["공개 Q&A", "출시 6개월 활동 약 25% 상대 감소 / 일일 웹 트래픽 약 12% 감소", "동료 검토 논문 2편"],
       ["Reddit", "감소 증거 없음 / 정보성 요청 3.4% 초과 감소 배제", "동료 검토 논문 / 프리프린트"],
       ["검색", "\"SEO is basically dead\"", "실무자 블로그"],
       ["에이전트", "\"Another channel is agents\"", "r/devrel 댓글"]],
      foot="표 9 발췌. 줄어든 것은 모르는 사람에게 정답을 묻는 정보 교환형 공간, 측정된 범위에서 버틴 것은 관계형 커뮤니티.")

figure("PART 2", "TWO FUNNELS", "두 개의 퍼널, 세 개의 표면", "5-2",
       "그림 10. 개발자·검색 크롤러·LLM — 세 유통 표면과 두 퍼널",
       "human funnel은 <b>신뢰</b>를, machine funnel은 <b>정확성</b>을 요구한다.")

quote("PART 2", "TRUST", "슬롭과 치어리딩 — 신뢰를 잃는 가장 빠른 길",
      "\"every devrel position includes AI cheerleading at this point\"",
      "— Bluesky, 2025-09 · \"push back on demands to use AI for all the things, especially in DevRel\"(Jen Looper, 2025-12)",
      "경계 역할의 신뢰는 \"회사의 말을 그대로 옮기지 않는다\"는 데서 나온다. 응원단이 되는 순간 그 근거가 사라진다. "
      "<b>다음 주 질문:</b> 우리 문서를 가장 많이 읽는 것은 사람인가, 에이전트인가 — 로그로 확인했나?")

# ═════════════════════════ PART 3 ═════════════════════════
divider("PART 3", "PART 3", "직함은 흩어지고 기능은 남는다",
        "2026년 9월 25일, 같은 날 열어본 채용 페이지들에서 이 직업의 다음 모습을 읽는다.",
        ["6장. 공고를 읽다", "7장. 직업에서 역량으로"])

table("PART 3", "ONE DAY SNAPSHOT", "같은 날 열어본 채용 페이지들",
      ["회사(전체 공고, 약)", "DevRel·DX 제목", "FDE·Applied AI·솔루션"],
      [["Anthropic (약 630)", "Developer Relations 1", "Applied AI 제목 38(서울 포함), FDE 계열 7"],
       ["OpenAI (약 830)", "DX Engineer, Cyber 1 (\"Developer Advocate\" 0)", "\"Forward Deployed\" 제목 22"],
       ["Vercel (87)", "DevRel Engineer 1", "FDE 1, Solutions Architect 다수"],
       ["Supabase (55)", "Developer Relations Engineer 3", "—"],
       ["Cursor (125)", "0", "FDE 계열 7~9"],
       ["ElevenLabs (약 220)", "DX Engineer 1", "FDE 계열 16"]],
      foot="표 10 발췌 — Greenhouse·Ashby 공개 API, 제목 키워드 기준. <b>하루치 스냅샷이며 추세 지표가 아니다.</b>")

figure("PART 3", "WHERE THEY WENT", "사람들은 어디로 갔나", "6-1",
       "그림 11. DevRel이라는 이름을 떠난 공개 기록들 — 다섯 방향")

figure("PART 3", "FDE?", "FDE는 DevRel을 대체하는가", "6-2",
       "그림 12. 한 번에 닿는 사람의 수로 놓아본 직함들 — 2026년 9월 25일 공고 문구 기준",
       "반론: 가운데가 눌린다 — \"Developer marketing aimed at engineers who read docs and deliberate\"(Daily Context). 하루치 공고로는 확인할 수 없다.")

cards("PART 3", "FOUR FUNCTIONS", "흩어진 직함 속의 네 가지 기능", [
    ("번역", "회사의 말을 개발자의 말로, 개발자의 말을 회사의 말로."),
    ("피드백 루프", "막힌 곳을 모아 제품으로 되돌려준다. 가장 또렷한 곳은 FDE 공고였다."),
    ("신뢰", "쌓인 결과물이 신뢰가 된다. 가르치기가 여기에 속한다."),
    ("먼저 가보기", "먼저 써보고 알아낸다. 나머지 셋의 재료를 만든다."),
], cols=4, foot="공고들에 되풀이되는 동사 — 번역하기·되돌려주기·가르치기·먼저 써보기(표 12).")

figure("PART 3", "INTERLOCK", "네 기능이 맞물리는 순서", "7-1",
       "그림 13. 네 가지 기능이 맞물리는 순서")

table("PART 3", "CAREER", "커리어 경로가 없다는 것의 양면",
      ["목적지", "가장 많이 쓰는 기능", "함께 알아둘 점"],
      [["FDE·솔루션 엔지니어", "번역, 피드백 루프", "영업 목표와 계약 일정이 일의 리듬을 정함"],
       ["제품 엔지니어·Staff Engineer·MTS", "먼저 가보기", "청중 앞에 서는 일이 크게 줄어듦"],
       ["교육 직무", "신뢰, 번역", "모델이 바뀔 때마다 교재도 바뀜"],
       ["사내 AX", "네 기능 모두", "청중이 회사 안의 동료"]],
      lead="응답자의 61%가 \"no defined career path\" — State of DevRel 2024, 유효 응답 310명. 경로가 없다는 건 불안이지만, 기능 단위로 보면 건너갈 길이 여럿이다.",
      foot="표 13.")

figure("PART 3", "FOR LEADERS", "리더가 볼 것 — 어떤 기능에 사람을 둘 것인가", "7-2",
       "그림 14. 리더가 차례로 답할 세 질문",
       "<b>다음 주 질문:</b> 지난 석 달, 내 시간은 네 기능 중 어디에 가장 많이 들어갔나? (부록 A 워크시트)")

# ═════════════════════════ PART 4 ═════════════════════════
divider("PART 4", "PART 4", "회사 안으로, 그리고 그다음",
        "퍼뜨리는 기술이 회사 안으로 향할 때 — 그리고 이 직업의 네 갈래 전망.",
        ["8장. 퍼뜨리는 기술", "9장. AX를 DevRel처럼 운영하기", "10장. DevRel 다음"])

quote("PART 4", "PLOT TWIST", "DevRel이 전사 AI 확산을 맡다",
      "\"... Well, plot twist: we're not dead.<br>We're standing on the biggest stage of our careers.\"",
      "— Angie Jones(Block), 2025-10-20 블로그 「How DevRel Is Leading AI Adoption」",
      "\"Going first. Figuring stuff out. Guiding others. That's literally what we do in DevRel.\" — 낯선 기술 앞에서도 원래 하던 방식을 그대로 썼다.")

figure("PART 4", "MAPPING", "DevRel의 활동이 사내 확산 장치로 옮겨간 자리", "8-1",
       "그림 15. Block·카카오·Anthropic 공개 기록에 기댄 대응이며, 효과는 아직 검증되지 않았다")

figure("PART 4", "DIFFUSION", "왜 옮겨 쓸 수 있는가 — 확산 이론", "8-2",
       "그림 16. 먼저 가보기·함께 배우기·보여주기·되돌려주기 — 청중이 동료로 옮겨갈 때",
       "Rogers의 관찰 가능성·시험 가능성은 DevRel의 데모·핸즈온과 같은 자리를 가리킨다.")

table("PART 4", "TWO AXs", "같은 약어 AX의 두 뜻",
      ["항목", "Agent Experience", "AI Transformation"],
      [["뜻", "에이전트가 제품·플랫폼의 사용자로서 겪는 경험 전체", "조직에 AI를 들여 일하는 방식을 바꾸는 일"],
       ["사용자로 보는 대상", "에이전트", "조직의 동료"],
       ["둘이 겹치는 일", "사내 문서·도구를 에이전트가 쓸 수 있게 다듬기", "동료가 에이전트를 쓰도록 돕기"]],
      foot="표 14. 같은 두 글자가 따로 생겨난 <b>우연의 일치</b>다 — 운명처럼 읽을 이유는 없다.")

cards("PART 4", "NOT YET PROVEN", "아직 증명되지 않은 것", [
    ("사례가 적다", "공개 사례는 세 건(Block·카카오·Anthropic 공고), 대부분 당사자의 기록이다."),
    ("인과 실증이 없다", "AI 챔피언 프로그램의 효과를 정량화한 동료 검토 연구는 2026년 9월 시점 이 책의 조사 범위에서 찾지 못했다."),
    ("그래서 이 주장은", "이론과 공개 사례의 조합이다. 인과를 입증한 결론이 아니다."),
], foot="8장은 이 한계 고지로 끝납니다. 주장의 강도를 근거의 강도에 맞췄습니다.")

figure("PART 4", "THREE DIALS", "사내 AI 확산 설계의 세 다이얼", "9-1",
       "그림 17. 강도·측정·공유 장치",
       "커뮤니티형 확산이 의무화보다 효과적이라는 비교 연구는 <b>없다</b>. 그래서 눈금에 좋고 나쁨을 표시하지 않았다.")

figure("PART 4", "LEADERBOARD", "리더보드가 만든 냉소", "9-2",
       "그림 18. 강도를 올리고 사용량을 세면 생기는 일 — 감시와 연기로 가는 경로",
       "Shopify 메모(2025-04-07): \"Reflexive AI usage is now a baseline expectation at Shopify\" — 의무화와 공유 장치를 한 문서에 담았다.")

table("PART 4", "WHAT TO COUNT", "무엇을 셀 것인가 — 사례 수집 네 줄 양식",
      ["칸", "묻는 것", "이어지는 곳"],
      [["1", "무엇을 만들었나", "'만든 증거'의 목록"],
       ["2", "누가 쓰고 있나", "확산이 닿은 범위"],
       ["3", "그 덕분에 무엇이 달라졌나", "\"무엇이 달라졌는가\"라는 측정 질문"],
       ["4", "어디서 AI가 틀렸나", "프런티어의 경계 지도"]],
      lead="사용량이 아니라 <b>만든 증거</b> — 배포하고, API 호출에 성공하고, 포크하고, PR을 보낸 흔적.",
      foot="표 17. 한 양식으로 측정과 교육을 함께 한다(부록 C).")

figure("PART 4", "OUTLOOK", "DevRel 다음 — 네 갈래 전망", "10-1",
       "그림 19. 1장의 네 이야기와 새 출발점 하나에서 이어지는 네 전망")

table("PART 4", "WATCH LIST", "무엇을 보면 알 수 있나",
      ["전망 [예측]", "반대 의견", "관찰 지표"],
      [["해체론", "Anthropic·Vercel·Supabase의 DevRel 제목 공고", "인접 직무 공고 속 기능 동사의 빈도"],
       ["확장론", "메이커 운동 상한론, 에이전트 투자 수익 사례 부재", "빌더·에이전트를 청중으로 적은 공고와 프로그램"],
       ["교정론", "Orbit 사례", "'만든 증거'를 성과 기준으로 적는 공고·발표"],
       ["내향론", "의무화 냉소, 인과 증거 부재", "첫 실증 연구, Block·카카오 밖의 공개 사례"]],
      foot="표 18. 예측은 자주 빗나간다 — 그래서 맞았는지 확인할 지표를 함께 적었습니다.")

# ═════════════════════════ CLOSING ═════════════════════════
quote("CLOSING", "REMEMBER", "기억할 세 문장",
      "① DevRel은 <span class='coral-t'>D(누구에게)와 R(무엇으로)</span>로 이루어진 경계 역할이다 — 두 변수가 함께 움직였다.<br><br>"
      "② 직함은 흩어져도 <span class='coral-t'>번역·피드백 루프·신뢰·먼저 가보기</span>는 공고마다 되풀이된다.<br><br>"
      "③ 셀 것은 사용량이 아니라 <span class='coral-t'>만든 증거</span>와 그로 인해 달라진 것이다.")

cards("CLOSING", "ONE THING", "책을 덮으며 해볼 한 가지", [
    ("한 문장으로 적는다", "이번 주에 한 일 하나를 — 누구를 향했고 무엇으로 닿았는지 드러나게."),
    ("다른 부서에 보여준다", "동료 한 사람에게 자기 말로 다시 설명해달라고 부탁한다."),
    ("간격을 좁힌다", "돌아온 설명과 내 문장의 차이 — 그 간격을 좁히는 것이 이 일이다."),
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
.coral-t{color:var(--coral)}
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
