#!/usr/bin/env python3
"""발표자료 생성기 — 「디지털 워커의 시대」 1시간 발표용.
전작 「AX를 만들다」 덱의 구조 규약(슬라이드 섹션·PART 구분면·진행바·페이지 번호·인쇄)을
따르되, 이 책의 표지 팔레트(남색 #16222e + 금색 #c9963f + 크림)와 에디토리얼 삽화 6점을 쓴다.
사용법: python3 build_deck.py <출력 index.html 경로>
"""
import sys, pathlib, html as _h

OUT = pathlib.Path(sys.argv[1])
BOOK = "디지털 워커의 시대, AI 에이전트를 조직의 성과로 만드는 체계"
BY = "김상기 · ksangki/ax-system"
VER = "v1.3.0"

slides = []   # (kind, section_label, html_body)

def cover():
    slides.append(("cover", "OPENING", f"""
  <div class="corner tl"></div><div class="corner tr"></div>
  <div class="corner bl"></div><div class="corner br"></div>
  <div class="cover-wrap">
    <div class="eyebrow gold">AX 3부작 · 처방편</div>
    <h1 class="cover-title">디지털 워커의 시대</h1>
    <p class="cover-sub">AI 에이전트를 조직의 성과로 만드는 체계</p>
    <div class="neon-bar gold"></div>
    <p class="cover-quote">"바텀업이 씨앗을 만든다. 그러나 씨앗은 저절로 수확되지 않는다."</p>
    <p class="cover-by">— 탑다운이 할 일은 지시가 아니라 거두는 체계다</p>
    <div class="cover-meta">
      <span>김상기 · 1시간 발표</span>
      <span class="mono dim">ksangki/ax-system · {VER}</span>
    </div>
  </div>"""))

def divider(sec, eyebrow, title, sub, img=None, alt=""):
    art = f'<img class="div-art" src="../assets/illustrations/{img}" alt="{alt}" />' if img else ""
    slides.append(("div", sec, f"""
  <div class="div-wrap">
    <div class="div-text">
      <div class="eyebrow gold">{eyebrow}</div>
      <h2 class="div-title">{title}</h2>
      <p class="div-sub">{sub}</p>
    </div>
    {art}
  </div>"""))

def cards(sec, eyebrow, title, items, lead=None, foot=None, cols=3):
    lead_h = f'<p class="lead">{lead}</p>' if lead else ""
    foot_h = f'<p class="foot-note">{foot}</p>' if foot else ""
    cs = "".join(f"""
      <div class="card">
        <div class="card-num mono">{i+1:02d}</div>
        <div class="card-h">{h}</div>
        <div class="card-sub">{s}</div>
      </div>""" for i, (h, s) in enumerate(items))
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  {lead_h}
  <div class="grid grid-{cols}">{cs}</div>
  {foot_h}"""))

def quote(sec, eyebrow, title, q, src=None, after=None):
    src_h = f'<p class="q-src">{src}</p>' if src else ""
    aft = f'<p class="after">{after}</p>' if after else ""
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  <blockquote class="bigq">{q}</blockquote>
  {src_h}{aft}"""))

def table(sec, eyebrow, title, head, rows, lead=None, foot=None):
    lead_h = f'<p class="lead">{lead}</p>' if lead else ""
    foot_h = f'<p class="foot-note">{foot}</p>' if foot else ""
    th = "".join(f"<th>{c}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  {lead_h}
  <table class="deck-table"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>
  {foot_h}"""))

def bullets(sec, eyebrow, title, items, lead=None, foot=None):
    lead_h = f'<p class="lead">{lead}</p>' if lead else ""
    foot_h = f'<p class="foot-note">{foot}</p>' if foot else ""
    li = "".join(f"<li>{i}</li>" for i in items)
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  {lead_h}
  <ul class="big-list">{li}</ul>
  {foot_h}"""))

def stat(sec, eyebrow, title, pairs, foot=None):
    foot_h = f'<p class="foot-note">{foot}</p>' if foot else ""
    st = "".join(f"""
      <div class="stat">
        <div class="stat-n">{n}</div>
        <div class="stat-l">{l}</div>
      </div>""" for n, l in pairs)
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  <div class="stat-row">{st}</div>
  {foot_h}"""))

def figure(sec, eyebrow, title, svg, cap, foot=None):
    foot_h = f'<p class="foot-note">{foot}</p>' if foot else ""
    slides.append(("content", sec, f"""
  <div class="eyebrow cream">{eyebrow}</div>
  <h2 class="content-title">{title}</h2>
  <div class="neon-bar gold small"></div>
  <figure class="deck-fig"><img src="../figures/{svg}" alt="{cap}" /><figcaption>{cap}</figcaption></figure>
  {foot_h}"""))

# ───────────────────────── OPENING ─────────────────────────
cover()

cards("OPENING", "ABOUT THIS TALK", "이 발표가 답하려는 하나의 질문", [
 ("AI 과제 목록은 이미 수백 건이다", "공모를 한 번 띄우면 목록은 빠르게 분다. 보고 자리에서도 훌륭하게 작동한다."),
 ("그런데 조직 성과로는 옮겨가지 않는다", "개인 생산성은 올랐다는데 조직 지표는 그대로다. 파일럿은 파일럿에서 멈춘다."),
 ("그래서, 위에서 무엇을 내려보내야 하는가", "이 발표는 그 질문에 대한 답이다. 정답은 과제 목록이 아니다."),
])

cards("OPENING", "THREE PROMISES", "이 발표가 지키는 세 가지", [
 ("구호가 아니라 순서로", "\"역량의 시대\" 같은 선언은 한 문단이면 충분하다. 그다음의 지루한 이야기를 한다."),
 ("숫자에는 라벨을 붙인다", "벤더 자체 계측인지 동료평가 논문인지 익명 게시물인지 밝힌다. 라벨 없는 수치는 쓰지 않는다."),
 ("현장의 냉소를 예고로 쓴다", "\"AX팀을 만드는 순간 실패한다\"는 말부터 먼저 인용하고 시작한다."),
])

quote("OPENING", "THE CYNICISM", "먼저 인용하고 시작하는 문장",
 "“AX팀을 만들어놓고 ‘너희가 AX팀이니까 빨리 AI로 자동화해봐’가 문제라는 말 같아요.<br>도메인 현업자가 주도하고 AX기술자가 서포트하면서 AI를 도입하는 게 가장 좋을 것 같은데.”",
 "— GeekNews 사용자 <span class='mono'>snisty</span>, 2026-04-09 토픽의 댓글. 개인의 공개 발언이며 조사 데이터가 아니다.",
 "반박할 말을 찾지 못했다. 동의하기 때문이다. 그리고 그 처방이 이 발표가 도달하는 결론과 같다.")

bullets("OPENING", "AGENDA", "오늘 1시간 동안", [
 "<b>PART 1 전향</b> — 바텀업이 벽에 부딪혔다면, 위가 할 일은 정말 '정해서 밀어붙이는 것'인가",
 "<b>PART 2 절차</b> — 체계의 입장권은 SOP다. 사람의 절차를 기계가 읽는 절차로",
 "<b>PART 3 등록</b> — 여덟 칸, 청구서의 벽, 그리고 '할 수 있는 것'과 '해도 되는 것'",
 "<b>PART 4 성과</b> — 무엇과 비교할 것인가, 그리고 절감분은 누구의 것인가",
 "<b>PART 5 폐기</b> — 아무도 설계하지 않는 마지막 칸",
 "<b>실행</b> — 90일 로드맵과 세 개의 Gate",
], foot="각 PART는 다음 주에 바로 쓸 수 있는 도구를 하나씩 남깁니다.")

# ───────────────────────── 진단 ─────────────────────────
divider("DIAGNOSIS", "PART 1", "전향 — 위가 할 일은 따로 있다",
 "개인은 배웠는데 조직은 남기지 못했다. 그 격차는 도구가 아니라 체계에 있다.",
 "part-1-harvest.webp", "현장의 씨앗을 위의 체계가 물길과 수확 장치로 받치는 삽화")

cards("DIAGNOSIS", "THE GAP", "채택은 인터넷보다 빨랐다. 그런데", [
 ("도입 속도", "생성형 AI의 업무 채택 속도는 과거 어떤 기술보다 빨랐다."),
 ("절감 실측", "그런데 자기보고된 업무시간 절감은 평균 1.4% 수준에 머물렀다. <span class='src'>Bick et al., 근로자 조사</span>"),
 ("파일럿 정체", "기업 GenAI 파일럿 다수가 손익 효과 없이 멈춘다. <span class='src'>MIT NANDA — 편의표본, 방법론 논쟁 있음</span>"),
], foot="세 숫자의 출처 성격이 각각 다릅니다. 그 차이를 밝히는 것이 이 발표의 규율입니다.")

cards("DIAGNOSIS", "THE WRONG TURN", "그래서 위에서 정하면 되는가 — 아니다", [
 ("씨앗은 아래에서 온다", "최종 관문을 통과한 후보의 압도적 다수가 현장의 자발적 제안에서 나왔다."),
 ("강제는 우회를 부른다", "하향식 강제 도입은 섀도 사용을 낳는다. 과잉 제한도 같은 실패를 만든다."),
 ("표준화조차 그렇다", "절차 표준화를 위에서 찍어 누르면 실패한다는 것이 현장의 결론이다."),
])

quote("DIAGNOSIS", "THE PIVOT", "이 발표의 관통선",
 "바텀업이 씨앗을 만든다.<br>그러나 씨앗은 저절로 수확되지 않는다.<br><span class='gold-t'>탑다운이 할 일은 지시가 아니라 거두는 체계다.</span>",
 None,
 "초기 구상은 \"바텀업은 한계에 부딪혔으니 탑다운으로 전향한다\"였습니다. 현장 데이터가 그 문장을 지지하지 않아 고쳤습니다.")

figure("DIAGNOSIS", "WHAT COMES DOWN", "위가 공급하는 것은 과제 목록이 아니다",
 "fig-01.svg", "그림 1. 씨앗은 아래에서 오고, 체계는 위에서 온다",
 "기준 · 자원 · 제도 · 폐기 규칙 — 넷이다. 아이디어는 계속 아래에서 온다는 것이 전제다.")

bullets("DIAGNOSIS", "EVIDENCE", "중앙이 무엇을 공급하면 현장이 사는가", [
 "DORA 2025: <b>AI는 증폭기다</b> — 최대 수익은 도구가 아니라 근본 조직 시스템에 대한 전략적 집중에서 온다",
 "고성숙 조직만 불균형한 편익을 얻는다 — <b>버전 관리 · 관측성 · 내부 플랫폼</b>",
 "되돌릴 수 있게, 볼 수 있게, 다시 만들지 않게 — 전부 기준·자원·제도다",
 "이 발표가 설계할 등록부·감사 로그·폐기 규칙이 하는 일과 같다. 대상만 코드에서 에이전트로 바뀐다",
], foot="출처: DORA State of AI-assisted Software Development 2025")

# ───────────────────────── 운영체계 지도 ─────────────────────────
divider("THE SYSTEM", "OVERVIEW", "한눈에 보는 운영체계",
 "발견에서 폐기까지, 아홉 단계. 각 단계는 앞 단계의 산출물을 입력으로 받는다.")

cards("THE SYSTEM", "LIFECYCLE 01–04", "발견 → 표준화 → 등록 → 인증", [
 ("DISCOVER 발견", "후보 목록을 다섯 관문으로 가린다."),
 ("STANDARDIZE 표준화", "실제 업무를 SOP로 적고 기계가 읽게 한다."),
 ("REGISTER 등록", "목적·Owner·업무·시스템을 기록한다."),
 ("CERTIFY 역량 인증", "무엇을 안정적으로 할 수 있는지 검증한다."),
], cols=4)

cards("THE SYSTEM", "LIFECYCLE 05–09", "권한 → 운영 → 측정 → 보상 → 폐기", [
 ("AUTHORIZE 권한", "데이터·도구·행동의 허용 범위를 정한다."),
 ("OPERATE 운영", "실행·로그·비용·감사·중지 절차를 돌린다."),
 ("MEASURE 측정", "시간·FTE·품질·ROI를 함께 본다."),
 ("REWARD 보상·재배치", "절감분을 성과로 인정하고 새 역량에 쓴다."),
 ("RETIRE 폐기", "권한을 회수하고 계정을 닫고 기록을 남긴다."),
], cols=5,
 foot="가운데를 관통하는 것이 <b>Agent Registry · Agent ID</b> — 단계가 아니라 전 생애주기를 꿰는 기반입니다.")

bullets("THE SYSTEM", "NINE WALLS", "체계를 세우다 부딪히는 아홉 개의 벽", [
 "목록은 있는데 <b>실체를 모른다</b> → 재고 조사",
 "가리려니 <b>정의가 없다</b> → 관문·판별",
 "절차가 <b>적혀 있지 않다</b> → SOP",
 "적어도 <b>기계가 못 읽는다</b> → 변환",
 "등록하려니 <b>적을 칸이 없다</b> → 스키마",
 "<b>청구서가 막는다</b> → 계층과 위임",
 "<b>통제 기준이 없다</b> → 자율성 등급",
 "<b>성과를 못 잰다</b> → FTE 환산",
 "재면 <b>현장이 숨긴다</b> → 그리고 폐기",
])

# ───────────────────────── PART 2 절차 ─────────────────────────
divider("PROCEDURE", "PART 2", "절차 — 체계의 입장권",
 "적힌 절차와 실제로 하는 일은 원래 다르다. 그 간극이 광맥이다.",
 "part-2-procedure.webp", "문서에 적힌 절차와 실제 업무의 흔적이 하나의 경로로 합쳐지는 삽화")

cards("PROCEDURE", "INVENTORY", "세어보면 다 있는데, 대보면 없다", [
 ("이름표는 실체를 보장하지 않는다", "목록을 한 건씩 열면 기존 자동화, 데이터 분석, 아이디어 문장 하나가 섞여 있다."),
 ("빅테크의 정의는 한 곳을 가리킨다", "목표가 있고, 도구로 외부에 작용하며, 그 과정을 스스로 결정한다."),
 ("그래서 흔한 목록의 정체가 보인다", "대시보드는 관찰만 한다. 룰 기반 알람은 스스로 결정하지 않는다."),
])

table("PROCEDURE", "DEFINITIONS", "무엇을 에이전트라 부를 것인가 — 세 정의",
 ["출처", "정의의 핵심"],
 [["OpenAI (2025)", "사용자를 대신해 과업을 <b>독립적으로</b> 완수하는 시스템. LLM을 쓰더라도 실행 흐름을 제어하지 않으면 에이전트가 아니다"],
  ["Anthropic (2024-12)", "LLM이 자기 프로세스와 도구 사용을 <b>동적으로 지휘</b>하며 수행 방식의 통제권을 쥔 시스템. 미리 짜인 워크플로와 구분"],
  ["Google 백서 (2024)", "가진 도구로 세계를 <b>관찰하고 그에 작용</b>하여 목표를 달성하려는 애플리케이션"]],
 foot="정의는 방향을 준다. 그러나 판정은 해주지 않는다 — 그래서 관문이 필요하다.")

figure("PROCEDURE", "TOOL 01", "재고 조사의 다섯 관문", "fig-02.svg",
 "그림 2. 재고 조사의 다섯 관문",
 "관문의 순서가 곧 정의다. 값싼 판정을 앞에, 비싼 판정을 뒤에 둔다.")

table("PROCEDURE", "TOOL 02", "실무자에게는 질문 셋이면 된다",
 ["", "묻는 것", "아니라면"],
 [["전제", "우리 조직의 업무인가", "대상 아님"],
  ["①", "실제로 <b>행동</b>하는가 (쓰기·발송·처리)", "가볍게 등록만"],
  ["②", "<b>스스로</b> 도는가 (사람은 예외에만)", "보통 등록"],
  ["③", "<b>되돌릴 수 없는</b> 일인가 (돈·대외·민감)", "등록 + 모니터링"]],
 foot="통제의 강도는 <b>똑똑한 정도가 아니라 되돌릴 수 없음의 정도</b>로 정합니다.")

quote("PROCEDURE", "THE API WALL", "붙일 곳이 없는 시스템은, 에이전트에게는 존재하지 않는다",
 "“All teams will henceforth expose their data and functionality through service interfaces. (…) Anyone who doesn't do this will be fired.”",
 "— 아마존 창업자 제프 베이조스의 2002년 전후 지시. 스티브 예기의 2011년 회고 문면이 정본처럼 유통된다.",
 "과제 목록을 내리지 않았습니다. <b>모든 시스템에 붙일 곳이 있어야 한다는 기준 하나</b>를 내리고 예외를 봉쇄했습니다 — 씨앗을 고르는 대신 밭을 갈았습니다.")

cards("PROCEDURE", "WRITTEN VS DONE", "적힌 절차와 실제로 하는 일", [
 ("두 얼굴은 원래 다르다", "적힌 것은 일반화된 것이고, 실제 수행은 특정한 것이다. <span class='src'>Feldman &amp; Pentland 2003</span>"),
 ("문서가 죽는 이유", "\"Confluence는 문서가 죽으러 가는 곳\" — 5년에 걸쳐 여러 사람이 같은 말을 남겼다."),
 ("간극은 광맥이다", "문서에 없는 지식이 실행 안에 남아 있다는 뜻이다. 아직 아무도 꺼내지 않았을 뿐이다."),
])

figure("PROCEDURE", "TOOL 03", "발견 → 대조 → 개선의 닫힌 루프", "fig-03.svg",
 "그림 3. 프로세스 마이닝의 세 축이 그대로 작업 순서가 된다",
 "실행이 문서를 갱신하는 경로를 만들면 문서가 산다. 없으면 발행되는 순간부터 늙는다.")

cards("PROCEDURE", "THE GATEWAY", "에이전트에게는 길목이 하나다", [
 ("모델 호출이 단일 관문", "사람의 절차는 시스템마다 로그를 심어야 했다. 에이전트는 어떤 시스템을 상대하든 모델을 반드시 부른다."),
 ("관측이 공짜에 가까워진다", "누가·언제·무엇을 하려고 불렀는지가 그 길목에서 저절로 남는다. A2A 호출 관계도 동적으로 그려진다."),
 ("막을 곳도 하나다", "권한 규칙을 걸면 환경 통제가 되고, 차단 스위치를 달면 킬 스위치의 집행 지점이 된다."),
], foot="심사의 재료도 바뀝니다 — <b>진술 대신 로그, 표본 대신 전수, 연 단위 주기 대신 상시 대조.</b>")

# ───────────────────────── PART 3 등록 ─────────────────────────
divider("REGISTRY", "PART 3", "등록 — 조직에 자리를 만든다",
 "등록은 이름표가 아니라 책임과 권한의 연결이다.",
 "part-3-registry.webp", "디지털 워커가 신원과 권한과 비용이 연결된 조직 등록부에 들어오는 삽화")

table("REGISTRY", "CASE STUDY", "사흘과 2년을 가른 것",
 ["", "래티스 (2024-07, 사흘 만에 철회)", "워크데이 (2025 발표 → 2026 출시)"],
 [["배치 위치", "인사 시스템 안, 사람 직원과 같은 레코드", "별도 에이전트 레지스트리 (연동하되 분리)"],
  ["부르는 말", "\"AI 직원(employees)\"", "\"에이전트\", \"디지털 노동\""],
  ["프레이밍", "사람과 동렬", "\"직원<b>처럼</b>(like employees) 통치한다\""],
  ["관리 축", "인사 평가 축에 편입", "비용·ROI·접근권한·상태"]],
 foot="결정적인 것은 조사 하나였습니다 — 직원<b>으로</b> 만들지 않고 직원<b>처럼</b> 통치했습니다.")

figure("REGISTRY", "TOOL 04", "등록한다는 건 여덟 칸을 채운다는 뜻이다", "fig-04.svg",
 "그림 4. 여덟 칸의 등록부",
 "앞의 일곱은 순순히 채워집니다. <b>마지막 한 칸이 늘 비어 있습니다.</b>")

cards("REGISTRY", "GRANULARITY", "행위마다 허용 수준을 따로 적는다", [
 ("제안만", "실행은 못 한다. 결과를 사람이 옮겨야 다음이 진행된다."),
 ("조회", "읽기만 한다. 상태를 바꾸지 않는다."),
 ("승인 후 실행", "사람이 건건이 승인해야 실행된다."),
 ("한도 내 자동", "미리 정한 범위 안에서는 스스로 실행한다."),
], cols=4,
 foot="한 칸에 \"실행 가능\"이라고만 적으면, <b>가장 위험한 행위가 가장 안전한 행위와 같은 권한</b>을 얻습니다.")

quote("REGISTRY", "THE INVOICE", "제도는 청구서에 부딪혀 모양이 잡힌다",
 "사번을 주면 계정이 생기고, 계정이 생기면 <span class='gold-t'>상용 SaaS 라이선스가 계정 수만큼 과금된다.</span>",
 None,
 "해법: 에이전트에게 전용 식별 체계를 주고 <b>책임지는 사람의 사번에 매핑</b>한다. 타협처럼 보이지만 책임의 종착점이 사람으로 남아 오히려 더 옳은 설계가 됩니다.")

figure("REGISTRY", "TWO LAYERS", "두 계층과 책임자 매핑", "fig-06.svg",
 "그림 6. 전부에게 식별자, 자격 갖춘 것에만 사번",
 "1계층은 관측을 위한 식별자, 2계층은 생산성 관리를 위한 사번입니다.")

stat("REGISTRY", "THE LANDSCAPE", "에이전트 신원은 이미 제품이 됐다", [
 ("GA", "Microsoft Entra Agent ID — 디렉터리 신원 + Owner·Sponsor·Manager 3역할"),
 ("GA", "Okta Agent SSO — \"사람 직원과 나란히 퍼스트클래스 신원으로 등록\""),
 ("34%", "사람 직원과 같은 통제를 AI 에이전트에 적용하는 조직 <span class='src'>Okta, 7개국 조사 2026</span>"),
], foot="규제도 등록을 요구합니다 — EU AI Act, 미 연방 AI 인벤토리, 중국 알고리즘 등록제, 한국 AI 기본법.")

# ───────────────────────── 자율성 ─────────────────────────
cards("AUTONOMY", "THE MIDDLE", "중간 등급이 가장 위험하다", [
 ("28%가 충돌했다", "테스트트랙 106명 실험. 눈은 장애물을 보고 손은 핸들에 있었는데도. <span class='src'>Victor et al. 2018</span>"),
 ("잘 만들수록 감독이 어려워진다", "자율성이 높아질수록 사람의 상황 인식은 낮아진다. <span class='src'>Endsley 2017, Human Factors</span>"),
 ("여섯 갈래가 같은 결론에 닿는다", "중간 등급을 안전하게 만드는 조건들이 하나같이 중간 등급의 편익을 없앤다."),
])

stat("AUTONOMY", "THE APPROVAL TRAP", "승인 게이트는 왜 외양만 남는가", [
 ("93%", "사용자가 권한 프롬프트를 승인하는 비율 — \"승인이 많아질수록 주의는 줄어든다\" <span class='src'>Anthropic 자체 계측 2026-05</span>"),
 ("84%", "샌드박싱이 권한 프롬프트 자체를 줄인 비율 <span class='src'>같은 회사 자체 보고 2025-10</span>"),
], foot="승인 축이 무너진 자리에서 <b>환경 축이 질문 자체를 없앴습니다.</b> 통제는 클릭이 아니라 구조에 심습니다.")

figure("AUTONOMY", "TOOL 05", "할 수 있는 것과 해도 되는 것", "fig-07.svg",
 "그림 7. 두 축의 분리 — 배치는 역량이 아니라 허가가 정한다",
 "\"더 높은 역량이 자동으로 더 높은 허용 자율성을 뜻하지 않는다.\" 배치는 둘 중 낮은 쪽을 따릅니다.")

cards("AUTONOMY", "DELIBERATE CHOICE", "낮춘 것이 결론일 수 있다", [
 ("C4를 A3로 낮췄다", "기술적으로 가능했지만 통제되지 않은 작업이 하류를 오염시킬 수 있어서."),
 ("\"결함이 아니라 의도된 거버넌스 선택\"", "낮은 등급을 '아직 덜 된 상태'로 취급하는 순간 로드맵이 위험을 밀어붙인다."),
 ("그리고 높은 등급이 더 필요한 것도 아니다", "역량은 평범해도 <b>여러 부서가 실제로 쓰는 범용 에이전트</b>가 조직엔 먼저 값을 낸다."),
])

cards("AUTONOMY", "WHO VERIFIES", "전수 로그는 누가 읽는가", [
 ("사람은 못 읽는다", "심사의 재료가 전수 로그가 됐는데, 그 양은 사람이 감당할 수 없다."),
 ("검증 에이전트를 세운다", "단, <b>작업자와 다른 곳에서 틀려야</b> 한다. 같은 모델·같은 맥락의 '검증했음'은 복창이다."),
 ("검증자도 등록부에 오른다", "그래야 \"검증자는 누가 검증하나\"가 감사 가능성에서 끊긴다."),
], foot="사람의 자리는 사라지지 않고 이동합니다 — <b>체계 설계 · 표본 감사 · 예외 판정.</b>")

# ───────────────────────── PART 4 성과 ─────────────────────────
divider("MEASURE", "PART 4", "성과 — 세는 법과 그 대가",
 "무엇을 재느냐보다, 잰 숫자를 어디에 쓰느냐가 먼저다.",
 "part-4-measure.webp", "절감 시간과 품질을 저울에 올리고 새로운 업무 역량으로 돌려보내는 삽화")

quote("MEASURE", "THE OPENING QUESTION", "1만 시간은 누구에게서 모인 것인가",
 "“1만 시간은 근사하게 들린다. <span class='gold-t'>그런데 그건 직원 2만 명에게서 각각 30분씩이다.</span>”",
 "— 자동화 업계 실무자의 서명 글. 조사 데이터가 아니라 경험담이다.",
 "한 사람의 5년치라면 정원 하나가 남습니다. 2만 명의 30분씩이라면 아무것도 남지 않습니다.")

table("MEASURE", "THE BASELINE", "첫 설계 결정은 기술이 아니라 기준선이다",
 ["", "증강 기준선 (인간 단독 대비)", "시너지 기준선 (둘 중 나은 쪽 대비)"],
 [["효과크기", "<b>g = +0.64</b>", "<b>g = −0.23</b>"],
  ["읽는 방식", "담당자가 훨씬 잘하게 됐다", "그 사람을 뺐으면 더 나았다"],
  ["출판편향 검정", "❌ 통과하지 못했다", "✅ 통과했다"]],
 foot="같은 370개 효과크기입니다. 기준선만 바꿨습니다. <b>대부분의 보고서는 전자를 재고 후자를 주장합니다.</b> <span class='src'>Vaccaro et al., Nature Human Behaviour 2024</span>")

cards("MEASURE", "NOT A HEADCOUNT CUT", "그렇다고 사람을 빼라는 뜻은 아니다", [
 ("조건은 정보 비대칭이다", "인간이 AI가 못 보는 정보를 쥐고 있으면 팀이 AI 단독을 뚜렷하게 이긴다."),
 ("틀리는 지점이 성과를 가른다", "단독 성능이 같은 두 AI를 사람과 짝지었더니 팀 성과가 41% 갈렸다."),
 ("그래서 질문이 바뀐다", "\"사람을 뺄까\"가 아니라 \"이 공정에서 사람이 쥔 정보가 무엇인가\"."),
], foot="출처: Hemmer et al., <i>European Journal of Information Systems</i> 2025")

figure("MEASURE", "TOOL 06", "두 단 환산과 두 계수", "fig-08.svg",
 "그림 8. 처리량 → 시간 → FTE, 그리고 두 계수",
 "<b>신뢰도</b>는 '이 숫자를 믿을 수 있나', <b>자율성</b>은 '이 중 에이전트 몫이 얼마인가'. 곱해 쓰지만 이중 할인이 아닙니다.")

bullets("MEASURE", "MEASUREMENT DISCIPLINE", "재는 자리에서 지킬 것", [
 "<b>평균 성공률 하나로 판정하지 않는다</b> — \"몇 번을 연달아 시켜 한 번도 안 틀렸는가\"가 더 쓸모 있다",
 "<b>과업 수준 이득을 조직 성과로 곱하지 않는다</b> — 과업 이득의 일부만 최종 산출물로 통과한다",
 "<b>자기보고 등급에는 폐지 시한을 못 박는다</b> — 실측으로 옮겨갈 유인을 만드는 것이 목적이다",
 "<b>자기 숫자부터 의심한다</b> — 우리가 인용하는 연구의 후속도 함께 본다",
])

# ───────────────────────── 절감분 ─────────────────────────
quote("PEOPLE", "THE CLIMAX", "이 발표에서 가장 중요한 문장",
 "<span class='gold-t'>절감이 곧 감원으로 읽히는 순간, 현장은 성과를 숨긴다.</span><br>그러면 측정 체계 자체가 붕괴한다.",
 None,
 "측정이 정확해질수록 그 숫자의 위협도 정확해집니다. 도구를 개선할수록 숨길 유인이 커집니다.")

figure("PEOPLE", "TWO FATES", "같은 숫자, 두 개의 운명", "fig-09.svg",
 "그림 9. 어떻게 읽히느냐가 측정의 운명을 정한다",
 "감축으로 읽히면 과소 보고 → 측정 붕괴. 재투자 선언이 믿기면 신뢰 축적 → 더 정확한 숫자.")

table("PEOPLE", "THREE USES", "절감분의 사용처는 셋뿐이다",
 ["사용처", "내용", "현장의 반응"],
 [["<b>재투자</b>", "확보한 시간을 새 일, 더 가치 있는 일로", "협조적"],
  ["<b>품질·처리량</b>", "같은 인원으로 더 많이, 더 정확하게", "중립"],
  ["<b>감축</b>", "정원 조정", "강한 저항"]],
 foot="세 줄은 서로를 오염시킵니다. 첫 번째를 하겠다고 말해도 <b>세 번째가 가능하다는 것을 모두가 알면</b> 선언은 믿기지 않습니다.")

bullets("PEOPLE", "TOOL 07", "측정보다 먼저 선언할 것", [
 "이 체계의 절감 수치는 <b>인력 조정의 근거로 쓰지 않는다</b> — 기한 명시, 재논의 없으면 자동 연장",
 "확보된 시간의 기본 용도는 <b>재투자</b>다 — 바꾸려면 공개 논의",
 "수치는 조직 단위로만 집계하며 <b>개인별로 분해하지 않는다</b>",
 "이 체계는 에이전트의 활동을 기록한다 — <b>구성원 개인의 도구 사용 내역은 대상이 아니다</b>",
], foot="<b>말하지 않은 기본값은 기본값이 아닙니다.</b> 사람들은 말해지지 않은 것을 최악으로 해석합니다.")

# ───────────────────────── PART 5 폐기 ─────────────────────────
divider("RETIRE", "PART 5", "끝 — 설계되지 않은 마지막 칸",
 "폐기는 삭제가 아니라, 권한을 거두고 기록을 남기는 운영 절차다.",
 "part-5-retire.webp", "에이전트의 열쇠와 기록이 회수되고 다음 학습의 씨앗이 남는 삽화")

stat("RETIRE", "THE EMPTY CELL", "마지막 칸은 왜 비는가", [
 ("78%", "AI 아이덴티티를 만들거나 제거하는 <b>문서화된 정책이 없는</b> 조직 <span class='src'>CSA 2026-05</span>"),
 ("51%", "AI 아이덴티티의 <b>소유권이 불명확</b>하다고 답한 비율"),
 ("0건", "이 책이 찾은 <b>실제 조직의 공개 폐기 절차</b> — 검색어 7개, 확인 13곳"),
], foot="0건은 지어내지 않고 <b>부재 자체를 발견으로</b> 다뤘습니다.")

quote("RETIRE", "THE CORRECTION", "초기 구상을 철회하며",
 "도구는 이미 폐기를 설계했다.<br><span class='gold-t'>조직이 아직 안 켰다.</span>",
 "— Entra의 후원자 자동 승계, EU AI Act의 <span class='mono'>recalled</span>, 미 연방 인벤토리의 <span class='mono'>Retired</span>, 자율성 인증서의 갱신 요건",
 "\"아무도 설계 안 했다\"가 맞다면 처방은 간단합니다. 이미 설계돼 있는데 안 쓰인다면, 문제는 설계 능력이 아니라 <b>켜는 결정</b>입니다.")

bullets("RETIRE", "TOOL 08", "폐기 체크리스트 — 일곱 항목", [
 "① 공식 폐기 워크플로 (누가 요청하고 누가 승인하는가)",
 "② 자격 증명·토큰 즉시 폐기 (전부 목록에 있는가)",
 "③ 아웃바운드 접근 제거 · ④ 인바운드 호출 차단",
 "⑤ 메모리·데이터 정화 (보관·익명화·삭제를 구분했는가)",
 "⑥ <b>감사 추적 보존 — 지우지 않고 남기는 유일한 항목</b>",
 "⑦ 폐기 후 잔여 리스크 모니터링",
], foot="이 표의 칸들은 벤더의 발명이 아니라 <b>규제 스키마가 이미 요구하는 자리</b>입니다.")

figure("RETIRE", "THE CIRCUIT", "등록에서 폐기까지의 회로", "fig-10.svg",
 "그림 10. 재심사는 사건에 걸고, 위험 등급에 따라 바닥 주기를 둔다",
 "삭제가 아니라 <b>묘비 처리</b> — 운영에서는 사라지고, 기록에서는 남습니다.")

# ───────────────────────── 실행 ─────────────────────────
divider("EXECUTE", "ROADMAP", "90일 도입 로드맵",
 "전사 제도를 한 번에 완성하는 것이 목표가 아니다. 대표 업무 3~5개로 전 구간을 한 번 통과시킨다.")

cards("EXECUTE", "90 DAYS", "세 구간, 세 개의 Gate", [
 ("0–30일 · 발견과 기준", "후보 판정 · 대표 업무와 Owner 선정 · 기준선 확보 · 등록 스키마 초안<br><b class='gate'>GATE 1 — 실체와 책임자가 확인됐는가</b>"),
 ("31–60일 · 등록과 통제", "SOP 작성 · Agent ID 발급 · 역량/권한 등급 분리 판정 · 최소 권한과 중지 수단<br><b class='gate'>GATE 2 — 제한된 운영을 허가할 수 있는가</b>"),
 ("61–90일 · 운영과 증명", "제한 범위 운영 · 로그 점검 · 측정 · 재투자 원칙 선언 · 폐기 리허설<br><b class='gate'>GATE 3 — 확대·보완·중단 중 하나를 결정했는가</b>"),
], foot="30일마다 산출물보다 <b>결정 근거</b>를 남깁니다. 보완이나 중단도 정상적인 결과로 기록합니다.")

cards("EXECUTE", "NEXT WEEK", "다음 주에 할 수 있는 것", [
 ("10건 × 5분", "기존 목록 열 건을 다섯 관문에 통과시켜 본다. 떨어진 이유를 옆 칸에 적는다."),
 ("세 칸부터", "등록부는 신원·스폰서·행위 범위 세 칸으로 연다. 여덟 칸은 열만 만들어 둔다."),
 ("선언이 먼저", "측정을 시작하기 전에 '이 숫자를 어디에 쓰지 않을지'부터 문서로 남긴다."),
])

quote("CLOSING", "REMEMBER", "기억할 세 문장",
 "① 씨앗은 아래에서 온다. 위가 공급할 것은 목록이 아니라 <span class='gold-t'>기준·자원·제도·폐기 규칙</span>이다.<br><br>"
 "② 통제의 강도는 똑똑한 정도가 아니라 <span class='gold-t'>되돌릴 수 없음의 정도</span>로 정한다.<br><br>"
 "③ 절감이 감원으로 읽히는 순간 숫자는 숨는다 — <span class='gold-t'>측정보다 선언이 먼저</span>다.")

slides.append(("cover", "CLOSING", f"""
  <div class="corner tl"></div><div class="corner tr"></div>
  <div class="corner bl"></div><div class="corner br"></div>
  <div class="cover-wrap">
    <div class="eyebrow gold">감사합니다</div>
    <h1 class="cover-title end">디지털 워커의 시대</h1>
    <p class="cover-sub">AI 에이전트를 조직의 성과로 만드는 체계</p>
    <div class="neon-bar gold"></div>
    <p class="cover-quote">각 장이 남긴 아홉 개의 워크시트는 부록 A에 있습니다.</p>
    <div class="cover-meta">
      <span>웹에서 읽기 · ksangki.github.io/ax-system</span>
      <span class="mono dim">EPUB · 저장소 epub/ 폴더</span>
    </div>
    <p class="cover-by">AX 3부작 — 『AX를 만들다』(실전기) · 『나는 이 게임을 안다』(진단) · 이 책(처방)</p>
  </div>"""))

# ───────────────────────── 렌더 ─────────────────────────
TOTAL = len(slides)
body = []
sec_counts = {}
for i, (kind, sec, inner) in enumerate(slides, start=1):
    sec_counts[sec] = sec_counts.get(sec, 0) + 1
    body.append(f"""<section class="slide {kind}" id="s{i}" data-n="{i}">{inner}
  <div class="page-num mono">{i:03d} / {TOTAL}</div>
  <div class="page-section mono">{sec} / {sec_counts[sec]:02d}</div>
  <div class="page-footer"><span>{BOOK}</span><span>{BY}</span></div>
</section>""")

CSS = """
html{-webkit-text-size-adjust:100%;text-size-adjust:100%}
:root{
 --bg:#0d1620; --panel:#16222e; --panel2:#1c2b3a; --line:#2a3b4d;
 --text:#f2efe6; --muted:#a9a291; --dim:#6f7b88;
 --gold:#d9a441; --gold-d:#a87f3a; --cream:#e8e2d2; --red:#e06c5a; --green:#7fb069;
 --pad:clamp(2rem,4.5vw,4.2rem);
}
*{box-sizing:border-box;margin:0}
body{background:var(--bg);color:var(--text);
 font-family:'Pretendard','Apple SD Gothic Neo','Noto Sans KR',sans-serif;
 scroll-snap-type:y mandatory;overflow-y:scroll;height:100vh}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace}
.progress-bar{position:fixed;top:0;left:0;right:0;height:3px;background:#0a1017;z-index:99}
.progress-fill{height:100%;background:var(--gold);width:0;transition:width .2s}
.slide{min-height:100vh;scroll-snap-align:start;display:flex;flex-direction:column;
 justify-content:center;padding:var(--pad);position:relative;border-bottom:1px solid var(--line)}
.eyebrow{font-size:.78rem;letter-spacing:.18em;font-weight:700;text-transform:uppercase;margin-bottom:.9rem}
.eyebrow.gold{color:var(--gold)} .eyebrow.cream{color:var(--muted)}
.content-title{font-size:clamp(1.5rem,3.4vw,2.5rem);font-weight:800;line-height:1.3}
.neon-bar{height:3px;width:110px;background:var(--gold);margin:1.1rem 0 1.4rem;border-radius:2px}
.neon-bar.small{width:64px;height:2px}
.lead{color:var(--muted);font-size:clamp(.95rem,1.7vw,1.15rem);line-height:1.7;margin-bottom:1.2rem;max-width:60rem}
.foot-note{color:var(--muted);font-size:clamp(.88rem,1.5vw,1.02rem);line-height:1.7;margin-top:1.3rem;max-width:64rem}
.foot-note b,.lead b{color:var(--cream)}
.src{color:var(--dim);font-size:.85em}
.gold-t{color:var(--gold)}
/* cover */
.cover{justify-content:center;background:radial-gradient(1200px 600px at 50% 0%,#16222e 0%,#0d1620 70%)}
.cover-wrap{max-width:62rem}
.cover-title{font-size:clamp(2.6rem,7vw,5rem);font-weight:800;line-height:1.1;letter-spacing:-.01em}
.cover-title.end{font-size:clamp(2.2rem,5.5vw,3.8rem)}
.cover-sub{color:var(--cream);font-size:clamp(1.05rem,2.2vw,1.6rem);margin-top:.8rem;line-height:1.45}
.cover-quote{font-size:clamp(1rem,1.9vw,1.3rem);line-height:1.7;color:var(--text);margin:.4rem 0 1rem}
.cover-by{color:var(--muted);font-size:clamp(.85rem,1.5vw,1rem);line-height:1.6;margin-top:.8rem}
.cover-meta{display:flex;gap:1.4rem;flex-wrap:wrap;color:var(--dim);font-size:.9rem;margin-top:1.8rem}
.corner{position:absolute;width:26px;height:26px;border:2px solid var(--gold-d);opacity:.5}
.corner.tl{top:26px;left:26px;border-right:0;border-bottom:0}
.corner.tr{top:26px;right:26px;border-left:0;border-bottom:0}
.corner.bl{bottom:26px;left:26px;border-right:0;border-top:0}
.corner.br{bottom:26px;right:26px;border-left:0;border-top:0}
/* divider */
.div{background:linear-gradient(120deg,#16222e 0%,#0d1620 65%)}
.div-wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:2.4rem;align-items:center}
.div-title{font-size:clamp(1.9rem,4.4vw,3.1rem);font-weight:800;line-height:1.2;margin:.2rem 0 .9rem}
.div-sub{color:var(--muted);font-size:clamp(.95rem,1.7vw,1.15rem);line-height:1.7}
.div-art{width:100%;border-radius:14px;box-shadow:0 18px 44px rgba(0,0,0,.45)}
/* cards */
.grid{display:grid;gap:1rem}
.grid-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.grid-4{grid-template-columns:repeat(4,minmax(0,1fr))}
.grid-5{grid-template-columns:repeat(5,minmax(0,1fr))}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:1.1rem 1.2rem}
.card-num{color:var(--gold);font-size:.8rem;font-weight:700;margin-bottom:.5rem}
.card-h{font-weight:700;font-size:clamp(1rem,1.7vw,1.18rem);line-height:1.4;margin-bottom:.45rem}
.card-sub{color:var(--muted);font-size:clamp(.85rem,1.4vw,.98rem);line-height:1.6}
.card-sub .gate,.gate{display:inline-block;margin-top:.6rem;color:var(--gold);font-size:.92em}
/* quote */
.bigq{border-left:4px solid var(--gold);padding:.4rem 0 .4rem 1.4rem;margin:.6rem 0 1rem;
 font-size:clamp(1.15rem,2.5vw,1.85rem);line-height:1.6;font-weight:600;max-width:64rem}
.q-src{color:var(--dim);font-size:.92rem;line-height:1.6;margin-bottom:.9rem}
.after{color:var(--muted);font-size:clamp(.9rem,1.6vw,1.08rem);line-height:1.7;max-width:62rem}
.after b{color:var(--cream)}
/* table */
.deck-table{border-collapse:collapse;width:100%;max-width:72rem;margin:.4rem 0}
.deck-table th,.deck-table td{border:1px solid var(--line);padding:.62rem .9rem;text-align:left;
 font-size:clamp(.85rem,1.45vw,1.05rem);line-height:1.55;vertical-align:top}
.deck-table th{background:var(--panel);color:var(--gold);font-weight:700}
.deck-table td b{color:var(--cream)}
/* list */
.big-list{padding-left:1.3rem;max-width:66rem}
.big-list li{font-size:clamp(.95rem,1.75vw,1.2rem);line-height:1.75;margin:.5rem 0}
.big-list b{color:var(--cream)}
/* stats */
.stat-row{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));max-width:72rem}
.stat{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:1.2rem 1.3rem}
.stat-n{color:var(--gold);font-size:clamp(1.7rem,3.6vw,2.6rem);font-weight:800;line-height:1.1;margin-bottom:.5rem}
.stat-l{color:var(--muted);font-size:clamp(.85rem,1.4vw,1rem);line-height:1.6}
.stat-l b{color:var(--cream)}
/* figure */
.deck-fig{margin:.3rem 0;max-width:62rem}
.deck-fig img{width:100%;background:#f7f3ea;border-radius:12px;padding:10px}
.deck-fig figcaption{color:var(--dim);font-size:.88rem;margin-top:.6rem;text-align:center}
/* chrome */
.page-num{position:absolute;top:1.5rem;right:1.8rem;color:var(--dim);font-size:.8rem}
.page-section{position:absolute;top:1.5rem;left:1.8rem;color:var(--dim);font-size:.8rem;letter-spacing:.08em}
.page-footer{position:absolute;bottom:1.2rem;left:1.8rem;right:1.8rem;display:flex;justify-content:space-between;
 gap:1rem;color:#4e5a66;font-size:.75rem}
.cover .page-num{top:3.5rem;right:3.6rem} .cover .page-section{top:3.5rem;left:3.6rem}
.cover .page-footer{bottom:3.2rem;left:3.6rem;right:3.6rem}
@media(max-width:900px){
 .grid-3,.grid-4,.grid-5{grid-template-columns:1fr}
 .div-wrap{grid-template-columns:1fr}
 .div-art{max-height:34vh;object-fit:cover}
 .page-footer{display:none}
 .slide{min-height:auto;padding:2.2rem 1.2rem 3rem}
}
@media print{
 body{height:auto;overflow:visible;background:#fff;color:#111}
 .slide{page-break-after:always;min-height:auto;border:none;background:#fff;color:#111}
 .card,.stat,.deck-table th{background:#f4f1e8!important;border-color:#ccc!important}
 .cover,.div{background:#fff!important}
 .cover-title,.div-title,.content-title,.card-h{color:#111}
 .card-sub,.lead,.foot-note,.div-sub,.after{color:#444}
 .progress-bar{display:none}
}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];
const fill=document.getElementById('progress');
let cur=0;
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){
  cur=slides.indexOf(e.target);
  fill.style.width=((cur+1)/slides.length*100)+'%';
}}),{threshold:.55});
slides.forEach(s=>io.observe(s));
function go(i){i=Math.max(0,Math.min(slides.length-1,i));slides[i].scrollIntoView({behavior:'smooth',block:'start'});}
addEventListener('keydown',e=>{
 if(['ArrowDown','ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(cur+1);}
 if(['ArrowUp','ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(cur-1);}
 if(e.key==='Home'){e.preventDefault();go(0);}
 if(e.key==='End'){e.preventDefault();go(slides.length-1);}
});
"""

doc = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{BOOK} — 1시간 발표 자료</title>
<style>{CSS}</style>
</head>
<body>
<div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
<main>
{chr(10).join(body)}
</main>
<script>{JS}</script>
</body>
</html>
"""

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(doc, encoding="utf-8")
print(f"deck build 완료 — {TOTAL}장, 삽화 {doc.count('assets/illustrations/')}점, 도판 {doc.count('../figures/')}점")
