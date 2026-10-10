<!-- 검색 시점: 2026-10-10 기준 -->
# 보강 리서치 — "AI 동료/팀원" 자료 다섯 건 평가 (검색: 2026-10-10 기준)

저자가 받은 목록 다섯 건을 원문 존재·발행일·내용·그림 기준으로 대조하고, v1.7.0 개정에 쓸모가 있는지 판정한 기록이다. 원고는 고치지 않았다.

판정 기호: ✅ 원문 확인 / ⚠️ 검색 요약·2차 출처로만 확인 / ❌ 목록 정보와 다름 / ✗ 찾지 못함·확인 불가

## 0. 수집 한계 (먼저 읽을 것)

- **원문 직접 열람은 다섯 건 모두 실패했다.** 이 환경의 egress 프록시가 `every.to`·`aws.amazon.com`·`blog.replit.com`·`x.com`·미러 사이트 접속을 조직 정책으로 거부했다(`connect_rejected`, WebFetch는 DNS 실패). 따라서 아래 내용은 **전부 검색 엔진 요약·스니펫·2차 미러 경유**다. 부록 B 등급으로는 최대 `△`.
- 그 결과 **그림 1~5 메모는 하나도 검증하지 못했다.** 검색 스니펫에는 이미지·캡션이 나오지 않는다. "그림이 없다"가 아니라 "확인 불가"다. 저자가 원문을 직접 열어 확인해야 한다.
- Every 글 1은 검색 결과상 **구독 장벽(sign-up wall)** 뒤에 본문이 있다. 무료로 보이는 것은 도입부뿐이다.
- 원고에 넣을 수치는 반드시 원문 대조 후 넣는다. 이 문서의 인용은 "검색 요약에 나온 원문 표현"이며 축자 확인이 아니다.

## 1. 출처별 대조표

| # | 목록 정보 | 실제 확인 | URL | 발행 주체·저자 | 실제 발행일 | 성격 라벨 | 판정 |
|---|---|---|---|---|---|---|---|
| 1 | Every, "Why We Handed Our Agent's Infrastructure to Anthropic", 2026-10-08 | 존재 | https://every.to/source-code/why-we-handed-our-agent-s-infrastructure-to-anthropic | Every(Source Code 칼럼), 저자 **Paridhi Agarwal**(엔지니어, Every 첫 기고) | **2026-10-08** (목록과 일치) | `[벤더]` — 자사 제품 개발기. Anthropic 고객 후기 성격도 겸함 | ⚠️ 본문 대부분 유료 장벽 |
| 2 | Every, "Introducing the Every Agent", 2026-10-06 | 존재 | https://every.to/on-every/introducing-the-every-agent (제품 페이지 https://every.to/agent) | Every, 출시글 저자 **Dan Shipper**(CEO) | **2026-10-06** (목록과 일치) | `[벤더]` — 자사 제품 출시 발표 | ⚠️ |
| 3 | Sevendays, "Five AI colleagues working with me day and night", 2026-09-23 | **제목 문자열만 확인.** 벨기에 안트베르펜의 AI·앱 개발 회사 Sevendays 영문 홈페이지(https://www.sevendays.be/en/)의 "Ideas, lessons, and things we've learned" 영역에 같은 제목의 항목 헤딩이 있음 | 개별 글 URL **찾지 못함** | Sevendays(sevendays.be). 저자 미확인 | **확인 불가** (2026-09-23 검증 못 함) | `[벤더]` — AI 솔루션 업체의 자사 블로그(영업 성격) | ✗ 본문·날짜·저자 미확보 |
| 4 | AWS·monday.com, "AI Teammates: how monday.com runs production AI agents on Amazon Bedrock", 2026-07-22 | 존재 | https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/ | AWS Machine Learning Blog(고객 사례). 개별 저자명 **미확인** | **2026-07-22** (aws-news·aggregator 날짜와 일치) | `[벤더]` — 클라우드 벤더가 고객사와 낸 사례 글. 본문 스스로 "every figure in this post comes from monday's own internal production data"라고 밝힘 → 수치는 `[자체 보고]` | ⚠️ |
| 5 | Replit, "The Self-Driving Company", 2026-07-16 | 존재. 단 **replit.com 블로그 글로는 찾지 못했다.** 확인된 원문은 CEO Amjad Masad 개인 X 계정의 Article | https://x.com/amasad/article/2077802290304684404 | **Amjad Masad**(Replit CEO) 개인 명의 | **2026-07-16** (목록과 일치) | `[벤더]` — CEO의 자사 포지셔닝 글. 수치는 `[자체 보고]` | ⚠️ 발행 주체 표기는 "Replit"보다 "Replit CEO Amjad Masad(X)"가 정확 ❌ |

## 2. 출처별 요약과 인용 후보

### 자료 1. Every — Why We Handed Our Agent's Infrastructure to Anthropic
- 출처: 위 표. 저자·날짜: Paridhi Agarwal, 2026-10-08. 신뢰성: **중**(자사 개발기, 유료 장벽으로 본문 미확인).
- 요약
  - Every가 Slack 상주 에이전트(@Every)를 만들면서, 자체 운영하던 OpenClaw 기반 에이전트 함대를 접고 Anthropic의 **Claude Managed Agents**로 인프라를 넘긴 이유와 감수한 트레이드오프를 설명한다.
  - 인프라 운영을 벤더에 맡기고 팀은 "공유 동료(shared coworker)" 자체에 집중하겠다는 결정.
  - 검색 요약에 따르면 장기 실행 DM이 캐시·컨텍스트 한계에 걸리기 전에 새 세션을 여는 방식으로 **총비용을 39% 줄였다**고 보고한다.
  - 가장 큰 제약으로 **Claude 전용(모델 종속)**을 스스로 꼽는다.
- 인용 후보(검색 요약 경유, 원문 대조 필요)
  - "by staying on Claude Managed Agents, we spend our time on @Every instead of the infrastructure underneath it"
  - 비용 39% 절감(새 세션 전략) — `[자체 보고]`
  - Claude-only support가 최대 한계 — 벤더 종속 비용의 자기 고백
- 관련 섹션: 6장 "청구서를 처음부터 계산에 넣는다"(비용 구조·세션 단위 과금), 6장 "층위가 다르다"(플랫폼 계층 위임), 10장(벤더 종속 시 폐기·이전 비용).
- 그림 1 메모(공유 스킬 수정 화면): **확인 불가.** 유료 장벽 + 접속 차단. 참고로 "공유 스킬"이라는 개념은 자료 2·제품 페이지 쪽에서 확인된다(아래).

### 자료 2. Every — Introducing the Every Agent
- 저자·날짜: Dan Shipper, 2026-10-06. 신뢰성: **중**(자사 출시 발표).
- 요약
  - Slack에 사는 "agentic coworker". 복잡한 일을 위임받고, 새 모델·도구에 대한 개인화 알림을 보낸다. 표어는 "AI-pill your whole company".
  - 반복 업무(주간 보고·후속 연락)를 Slack 워크플로로 바꾸는 것을 지향. 현재 **베타**.
  - 반복 가능한 작업을 **팀이 재사용하는 스킬로 저장**한다. 제품 페이지 예시: "GTM skill … used 23 times by our team".
  - 메모리: Slack 스레드마다 세션 하나, 스레드 간에는 에이전트가 세션 시작 때 읽고 배우면서 덧붙이는 **노트 폴더**가 이어진다(엔지니어링 후속글 요약).
  - 가격: "zero percent markup on tokens: What we pay is what you pay". 제품 페이지는 부정확·불완전 응답 가능성을 고지.
- 인용 후보: "GTM skill used 23 times by our team"(스킬 재사용 카운트를 노출하는 설계), 토큰 무마진 과금, 스레드=세션 구조.
- 관련 섹션: 3장 "누가 절차를 적는가", 4장 "도구 쪽은 이미 여기까지 왔다"·"규칙 파일도 부패한다"(팀 공유 스킬, 메모리 노트가 쌓이는 구조의 부패 위험), 8장(사용 횟수는 성과가 아니라 활동 지표).
- 그림: 목록 메모 없음.

### 자료 3. Sevendays — Five AI colleagues working with me day and night
- **찾지 못함(본문).** 확인된 것은 sevendays.be 영문 홈페이지의 블로그 영역 헤딩 문자열뿐이다. 개별 글 URL, 발행일(2026-09-23), 저자, "다섯 동료"의 역할 구성은 하나도 확인하지 못했다.
- 회사 정보(확인됨): 2016년부터 안트베르펜에서 AI 솔루션·맞춤 앱·통합을 하는 벨기에 업체, 채용 페이지에 Claude·Claude Code·맞춤 에이전트를 일상적으로 쓴다고 적음.
- 비슷한 제목의 다른 글(덴마크 Royal Unibrew의 "다섯 AI 동료" 2025년 보도 등)이 검색에 걸렸지만 **대체하지 않았다.**
- 그림 2 메모(첫머리 AI 동료 역할 도식): **확인 불가.**
- 신뢰성: **하**(1인 실무자 경험담 + 업체 영업 글로 추정, 원문 미확보).

### 자료 4. AWS·monday.com — AI Teammates
- 날짜: 2026-07-22. 신뢰성: **중**(벤더 사례 글, 수치 자체 보고). 저자명은 미확인. 관련 monday 엔지니어링 블로그 글(Morphex)의 저자로 Tom Bogin·Oron Morad가 확인되나 이 AWS 글의 저자인지는 **미확인**.
- 요약
  - monday.com 사내 시스템(ZenML 요약상 이름 "Sphera")은 에이전트를 팀원으로 다룬다. 첫 화면은 작업 큐가 아니라 **Teams 페이지**: "a mix of humans and agents, each with a profile, a manager, a scope, and a performance score". 예시 에이전트 Atlas(역할: Software Engineer)는 티켓을 집어 PR을 연다.
  - **신원**: "each agent has a stable identity across Slack, GitHub, and monday, so people can tag, assign, review, or deactivate" it like any teammate.
  - **진입점 셋**: "three first-class inboxes: a Slack @mention, a monday item assignment, a GitHub PR review request".
  - 아키텍처: 모델 호출은 Amazon Bedrock, 이벤트는 SNS → 팀별 SQS → EKS 위 소비자, 상태는 RDS·ElastiCache·EFS·S3. 10년 된 코드베이스(수백 개 마이크로프런트엔드·마이크로서비스)에 맞춘 개조(retrofit) 다섯 가지가 핵심.
  - **자율성**: "confidence-scored merge"로 완전 자율에 다가간다 — 결정적 가드레일·평가 궤적·과거 되돌림(revert) 비율·샌드박스 결과를 결합해 신호가 충분히 강할 때만 사람을 뺀다. Morphex 에이전트 자동 병합률 95%(20개 중 19개) — **2차 요약(aws-news·ZenML)에서만 확인**.
  - 채택 수치: 빌더 10명 중 9명이 월간 AI 코딩 도구 사용, 엔지니어당 PR 처리량 절반 이상 증가 — `[자체 보고]`.
- 인용 후보: 위 "profile, manager, scope, performance score" 문장, "tag, assign, review, or deactivate", "three first-class inboxes", "every figure in this post comes from monday's own internal production data".
- 관련 섹션: 5장(여덟 칸 — 소유자·범위·상태), 6장 "새 신원인가, 있는 신원인가"·BNY/도이체방크 사례 옆, 7장 "중간 등급이 가장 위험하다"·"두 축이 어긋난 자리가 설계다"(신뢰 신호 기반 자동 병합 = 사건별 자율성 상향), 8장 "자기 숫자부터 의심한다"(자체 보고 수치 라벨 사례), 10장(deactivate가 1급 동작).
- 그림 3·4 메모(팀원 화면·협업 보드 화면): 검색 요약은 Teams 페이지의 존재를 서술하므로 **팀원 화면에 해당하는 이미지가 있을 개연성은 있다.** 그러나 이미지 자체는 **확인 불가.** 확인된 시각 자료는 아키텍처 다이어그램(미러 사이트 서술)뿐이다.

### 자료 5. Replit — The Self-Driving Company
- 저자·날짜: Amjad Masad, 2026-07-16, X Article. 신뢰성: **중~하**(CEO 포지셔닝 글, 방법론 미공개 수치).
- 요약
  - "Something strange happened at Replit in the past six months. The same engineers 3x'd output. Support resolved its hardest tickets 60% faster. Anyone could suddenly query the business like an analyst." — 이를 "a new kind of organization: the self-driving company"라 부른다.
  - 에이전트가 사내 전반에 걸친 시스템으로 운영된다: 프로덕션 사고 조사, PR 리뷰, 질의응답, 사업 데이터 분석, 지원 티켓 분류, 영업 계정 조사, Replit Agent 자체 개선.
  - 사람은 목적지를 정하고 결과를 소유하며, 사람의 판단이 필요할 때 에이전트가 에스컬레이션한다(2차 요약).
  - 지원팀이 에이전트에 조사 스킬과 플레이북을 붙였다(2차 요약).
  - 리뷰 시간·되돌림·사고율은 평탄하게 유지됐다고 주장.
- **수치 불일치 주의:** "nearly tripled"(본문) vs 2.9배(신규 입사자 제외)·5.8배(포함, 코드 라인 기준, Platformer 인터뷰·요약). 측정 단위가 다르다. 9월 컨퍼런스에서 CTO가 같은 수치를 말했을 때 3자 기고는 "기준선·단위·방법론 없음"을 지적했다.
- 관련 섹션: 8장 "자기 숫자부터 의심한다"·"개인 지표에서는 잡히는데 조직 손익에서는 안 잡힌다"(코드 라인 산출량 ≠ 성과의 교과서적 사례), 9장 "절감분이 애초에 생기지 않는다면"·"사용처는 셋뿐이다"(같은 인원으로 산출 3배 = 절감분을 인력 감축이 아닌 산출 확대로 쓴 선택), 3·4장(지원 플레이북 → 스킬).
- 그림 5 메모(업무 분석 부분의 제품 사용 흐름 화면): **확인 불가.** 참고로 "query the business like an analyst" 대목이 있으므로 해당 부분에 화면이 있을 수는 있다.

## 3. 원고와의 중복·연결 확인 (grep 결과)

- 원고·레퍼런스·research/*.md 어디에도 **monday·Replit·Every·Sevendays·Managed Agents는 나오지 않는다.** 신규 사례다.
- 가장 가까운 기존 사례는 **도이체방크 "디지털 직원"(2020, 사번+이메일, `[공식]`)과 BNY "디지털 직원"(2026, user ID·로그인·이름·페르소나·사람 매니저, `[매체]`)** — 6장 "새 신원인가, 있는 신원인가"와 부록 B-1. monday 사례는 이 계보의 **세 번째 점**이 되며, 둘과 달리 "manager·scope·performance score·deactivate"라는 **관리 속성이 화면 단위로 공개**됐다는 점이 다르다. 다만 BNY와 같은 함정(벤더/회사 자기 서술, 인사 시스템 등록 여부 미상)이 있다.
- 5장 Entra Agent ID의 오너·스폰서·매니저 구분과 monday의 "manager" 한 칸은 비교 재료가 된다(monday는 한 칸, Entra는 세 역할).

## 4. 장별 반영 제안과 쓸모 판정

| 자료 | 쓸모 | 반영 위치 | 무엇을 하는가 | 이유 |
|---|---|---|---|---|
| 4. monday AI Teammates | **높음** | 6장 "새 신원인가, 있는 신원인가"(BNY 뒤) / 7장 "두 축이 어긋난 자리가 설계다" / 5장 여덟 칸 비교 | **보강.** 신원 하나가 세 진입점(Slack·monday·GitHub)에 걸쳐 일관된다는 설계, 비활성화가 사람 팀원과 같은 1급 동작이라는 점, 신뢰 신호(가드레일·평가·되돌림률·샌드박스)가 충분할 때만 사람을 빼는 자동 병합은 7장 "할 수 있는 것 vs 해도 되는 것"의 실무 구현 예 | 원고에 없는 운영 규모 사례 + 구체 설계 결정. 단 `[벤더]`·`[자체 보고]` 라벨 필수, 95%는 원문 확인 전 사용 금지 |
| 5. Replit Self-Driving Company | **중간** | 8장 "자기 숫자부터 의심한다" / 9장 "사용처는 셋뿐이다" | **반례·경고 사례로 사용.** 3배 vs 2.9배 vs 5.8배 불일치와 방법론 부재는 8장의 "출처 성격 라벨" 규칙을 시연하기 좋다. 9장에서는 "같은 인원, 더 많은 산출"이라는 절감분 사용처 선택의 예 | 홍보성 수치라 근거로는 약하지만, 수치 의심 규율의 시연 재료로는 강하다. 원문이 X Article이라 장기 보존성 낮음 |
| 2. Every Agent 출시 | **중간** | 4장 "도구 쪽은 이미 여기까지 왔다"·"규칙 파일도 부패한다" / 3장 "누가 절차를 적는가" | **갱신.** 팀이 함께 쓰는 스킬 + 사용 횟수 노출 + 세션마다 읽고 덧붙이는 노트 폴더 = 4장이 말한 "기계가 읽는 절차"가 제품 기본값이 된 사례. 동시에 누적 노트의 부패 위험 예 | 2026-10 최신. 다만 소규모 미디어사 베타 제품이라 조직 체계 근거로는 약함 |
| 1. Every 인프라 이전기 | **중간~낮음** | 6장 "청구서를 처음부터 계산에 넣는다" / 10장(종속과 이전 비용) | **보강(선택).** 새 세션 전략 39% 비용 절감, 모델 종속을 최대 한계로 꼽은 자기 고백 | 유료 장벽으로 원문 대조가 어렵다. 저자가 구독으로 직접 확인할 수 있을 때만 |
| 3. Sevendays | **낮음** | — | 사용 보류 | 본문·날짜·저자 미확보. 1인 경험담 성격으로 조직 체계 책의 근거로 부적합 |

### 9장 '디지털 좌석' 냉소·'등록=감시' 오해와의 충돌 — 반대 근거로서의 가치

- **충돌 지점.** monday의 Teams 페이지는 사람과 에이전트를 **같은 화면에 섞고 둘 다에 "performance score"**를 붙인다. 이는 9장이 경계한 바로 그 장면이다. 같은 대시보드에 사람과 에이전트의 점수가 나란히 있으면 "등록 대상이 에이전트인지 사람인지"(9장 핵심 문장)가 흐려지고, 구성원은 자기도 점수 매겨지는 줄로 읽는다. 6장 "디지털 좌석" 냉소에도 연료가 된다 — 에이전트를 "팀원"으로 셈하면 벤더가 팀원 단위로 과금할 명분이 생긴다.
- **반대 근거로서의 가치(높음).** 그래서 오히려 9장에 쓸모가 있다. "AI 팀원" 프레이밍을 그대로 들여오면 어떤 오해가 생기는지 보여 주는 **실재 사례**로 쓰고, 우리 체계는 왜 "등록부의 행은 에이전트이고 사람은 소유자 칸에만 나온다"를 고수하는지 대비시킬 수 있다. 원고가 이미 다룬 Lattice(2024, AI를 직원으로 취급하려다 철회, `[매체]`)와 짝을 지으면 "팀원 프레이밍의 두 결말"이 된다 — 하나는 반발로 철회, 하나는 내부 운영 도구로 정착. 단 monday 쪽 구성원 반응 자료는 없으므로 "오해가 생겼다"고 쓰면 안 되고 "생길 수 있는 구조"로만 쓴다.
- Replit의 "CEO는 영광스러운 라우터"·"자율 주행 회사" 수사, Every의 "AI-pill your whole company"도 같은 축이다. 9장 "같은 사실, 여러 개의 문장" 절에 **피해야 할 문장의 예**로 쓸 수 있다(이 책은 "에이전트가 일을 맡는다"를, 벤더 문장은 "회사가 스스로 굴러간다"를 말한다).

## 5. 그림 인용 권고 (그림 1~5)

**결론: 다섯 그림 모두 스크린샷·도식 원본을 싣지 않는다. 인용문+링크로 바꾸거나, 필요한 것만 자체 재작도한다.**

1. **라이선스 비호환.** 이 책은 CC BY-NC-SA 4.0이다. 책에 실린 그림은 독자가 같은 조건으로 복제·변경·재배포할 수 있다는 약속 안에 들어간다. 타사 글의 스크린샷·도식은 각 회사 저작물(대부분 All rights reserved)이라 그 약속을 책 저자가 대신 해 줄 수 없다. 예외 표기("이 그림은 라이선스에서 제외")는 가능하지만 EPUB 재배포·2차 저작 단계에서 쉽게 떨어져 나간다.
2. **인용 요건이 약하다.** 공정 이용·인용 조항(국내 저작권법 제28조 등)에 기대려면 본문이 주이고 그림이 종이며, 인용 필요성과 출처가 분명해야 한다. 화면 캡처 전체를 그대로 싣는 것은 "종"을 넘기 쉽다. 특히 **유료 장벽 뒤의 화면(그림 1)**은 원 저작자의 시장을 대체한다는 반론에 약하다.
3. **화면 속 제3자 정보.** 제품 화면에는 사람 이름·아바타·Slack 메시지·성과 점수가 찍혀 있을 수 있다(그림 3 팀원 화면이 특히). 원 글에 공개됐다 해도 재배포물에 다시 싣는 것은 별개 문제이고, 이 책 9장의 감시 논의와 정면으로 어긋나는 모양새가 된다.
4. **상표·오인.** 로고·제품 UI가 크게 들어가면 해당 회사의 승인이나 제휴로 오인될 수 있다.
5. **검증 문제.** 메모의 그림 다섯 개는 이번 조사에서 하나도 실재를 확인하지 못했다. 확인 안 된 그림을 싣는 것은 사실 오류 위험이기도 하다.

**대안(우선순위 순)**
- (a) **인용문 + 링크 + 출처 성격 라벨.** 예: monday Teams 페이지는 그림 대신 "a mix of humans and agents, each with a profile, a manager, a scope, and a performance score"를 짧게 인용하고 URL·발행일·`[벤더]`를 붙인다. 부록 B에 행 추가.
- (b) **자체 재작도(mermaid).** 개념만 필요하면 이 책 파이프라인의 mermaid로 다시 그린다. 후보:
  - monday "신원 하나, 진입점 셋" 구조(Slack @멘션·monday 할당·GitHub 리뷰 요청 → 같은 에이전트 신원 → 등록부 한 행). 원 도식을 베끼지 말고 이 책의 등록부 용어(여덟 칸)로 재구성하면 2차 저작물 시비도 줄고 책 논지에 더 맞다.
  - 신뢰 신호 기반 자동 병합(가드레일·평가·되돌림률·샌드박스 → 점수 → 임계값 이상 자동/미만 사람 검토)을 7장 두 축 그림과 연결.
  - 재작도 그림 캡션에는 "monday.com 사례(AWS 블로그, 2026-07-22)를 바탕으로 저자가 다시 그림"이라고 쓴다.
- (c) 원 그림이 꼭 필요하면 **권리자 서면 허락**을 받고, 그 그림만 CC 라이선스 적용 제외임을 캡션과 판권 페이지 양쪽에 적는다. 비용 대비 권하지 않는다.

## 6. 반영 시 규칙 (fact-checker 대조 기준)
- 다섯 건 모두 `[벤더]`. monday·Replit 수치는 `[자체 보고]` 라벨을 본문에 붙인다.
- 원문 미열람이므로 부록 B 확인 등급은 `△`. 저자가 원문을 직접 열어 확인하면 `★`로 올린다.
- **사용 금지(원문 대조 전):** monday Morphex 95%(2차 요약만), Every 39%(유료 장벽), Replit 5.8배(인터뷰 수치, 본문 수치와 단위가 다름), Sevendays 전부.
- Replit의 발행 주체는 "Replit CEO 아므자드 마사드(X 게시물)"로 적는다. "Replit 블로그"로 적지 않는다.
- monday 글 저자명은 확인될 때까지 "AWS 머신러닝 블로그"로만 적는다.
- 제품 상태는 시점을 못 박는다: Every Agent "베타, 2026년 10월 기준".

## 7. 참고한 2차 출처
- aws-news.com 요약(2026-07-22): https://aws-news.com/article/2026-07-22-ai-teammates-how-mondaycom-runs-production-ai-agents-on-amazon-bedrock
- ZenML LLMOps Database, monday 사례: https://www.zenml.io/llmops-database/production-ai-agents-at-scale-engineering-agentic-ai-for-software-development
- monday 엔지니어링 블로그 "I Am Morphex": https://engineering.monday.com/i-am-morphex-im-an-ai-agent-growing-up-inside-a-real-codebase/
- Platformer, Masad 인터뷰: https://www.platformer.news/replit-amjad-massad-interview-coding-design-jobs/
- Masad X 게시물(요약 문장): https://x.com/amasad/status/2077803734990815306
- Every 엔지니어링 후속글 "Building a More Efficient Agent": https://every.to/context-window/building-a-more-efficient-agent
- Sevendays 홈페이지: https://www.sevendays.be/en/ , 채용: https://www.sevendays.be/en/jobs
