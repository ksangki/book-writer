# 웹 리서치 — AX 체계 구축 (가제)

<!-- 검색 시점: 2026-09-05 기준 -->
**검색 시점: 2026-09-05 기준**
슬러그: `ax-system` / genre: `tech-book` / 대상 독자: AX 실무 리더·기획자

## 이 문서를 읽는 법 (검증 등급 규약)

리서치 규율상 **"URL로 확인한 것"과 "검색 요약으로만 확인한 것"을 반드시 구분**한다. 각 항목에 아래 등급을 붙였다.

| 등급 | 의미 |
|---|---|
| **최상 (1차·직접 열람)** | 해당 URL을 직접 열어 본문을 확인함. 인용문은 원문 그대로. |
| **중 (2차·검색 요약)** | 검색 엔진 요약으로만 확인. 원문 본문 미열람 → 수치·인용은 Phase 4 fact-checker가 1차 대조 필요. |
| **하 / ⚠️ 미확인** | 출처 추적 실패 또는 집계 사이트발(發). 본문 사용 전 재확인 필수. |

> **저술가에게:** 등급 "중" 이하 항목의 수치를 본문에 쓸 때는 `(사실 확인 필요)` 마커를 남겨라. 등급 "최상" 항목은 그대로 인용 가능하다.

---

# 축 1 — 에이전트의 조직 등록

> 이 책의 최대 차별점. 결론부터: **"AI에게 사번을 준다"는 아이디어는 2026년 9월 현재 (a) 2020년 RPA 시대의 선례, (b) 2024년의 실패한 시도, (c) 2026년 벤더 제품 기능(GA)이라는 세 겹으로 존재한다.** 그런데 셋을 뭉뚱그리면 책이 죽는다. 아래 표가 그 구분이다.

## 1-1. 실제 등록 사례 (표)

| 조직 | 무엇을 등록했나 | 식별자 형태 | 권한 모델 | 감사·폐기 | 출처 URL | 발행일 | 실제 시행 여부 |
|---|---|---|---|---|---|---|---|
| **Deutsche Bank** (독일, 은행) | RPA+AI 봇 **Blue Bot 'Yi'** 를 Corporate Bank의 "digital employee"로 온보딩 | **사번(employee number) + 전용 업무 이메일 주소** | 기사에 명시 없음 ⚠️ | 기사에 명시 없음 ⚠️ | https://www.db.com/news/detail/20200720-deutsche-bank-s-corporate-bank-onboards-its-first-digital-employee-for-client-facing-role?language_id=1 | **2020-07-20** | **운영 중** (2020년 발표 시점 기준 / 2026년 현재 존속 여부 ⚠️ 미확인) |
| **Lattice** (미국, HR SaaS) | "digital workers"에게 **공식 employee record** 부여 — 조직도 편입, 목표·성과지표·시스템 접근권·책임 매니저 배정 | HRIS 상의 정식 employee record | 발표문상 "appropriate systems access" + "accountable manager" | — | https://www.shrm.org/topics-tools/news/technology/lattice-scraps-plans-to-treat-ai-bots-as-employees-after-backlash / https://fortune.com/2024/07/12/lattice-ai-workers-sam-altman-brother-jack-sarah-franklin | 발표 **2024-07-09** → 철회 **2024-07-12** | **발표만(보도자료) → 3일 만에 철회.** 제품에 반영 안 됨 |
| **Goldman Sachs** (미국, IB) | Cognition의 자율 코딩 에이전트 **Devin**을 "hybrid workforce"의 일원으로 배치 | 사번 부여 여부 **⚠️ 미확인** (보도는 "employee #1" 표현을 쓰나 이는 매체 수사) | 인간 개발자 감독 하 실행, "on behalf of our developers" | 명시 없음 ⚠️ | https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html (⚠️ 403으로 본문 미열람) | **2025-07-11** | **파일럿** (CIO Marco Argenti, 12,000명 개발조직 대상, 수백 인스턴스 시작) |
| **Microsoft** (자사 IT) | Agent 365로 사내 에이전트를 사용자·앱·디바이스와 같은 관리 인프라에 편입 | Entra Agent ID | Owner/Sponsor/Manager 3역할 (1-3 참조) | 소프트 삭제 + 캐스케이드 정리 | https://www.microsoft.com/insidetrack/blog/deploying-microsoft-agent-365-how-were-extending-our-infrastructure-to-manage-agents-at-microsoft/ | 2026 (정확일 ⚠️) | **제품 기능(GA)** + 자사 적용 (등급 중) |
| **한국 은행권 RPA** | RPA 로봇에 사번 부여 | — | — | — | — | — | **⚠️ 미확인 — 공개 출처로 확인 실패** |
| **일본 기업 "AI社員"** | 에이전트 비용을 **인건비로 계상**하는 기업 등장, 인사-IT 경계 소멸 | — | — | — | https://www.nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ (⚠️ 유료 구간, 표제+리드만 확인) | **2026-07-09** | **⚠️ 부분 확인** — 표제·리드만 검증됨 |

### 표에 대한 주석 (BLOCKING 규율)

**⚠️ 저술 시 절대 혼동 금지:**
1. **Deutsche Bank Blue Bot 'Yi' 는 확인된 유일한 "사번 부여" 1차 사례다.** 그리고 이것은 **2020년, LLM 이전, RPA 시대의 일이다.** "AI 에이전트에게 사번을 준다"의 선례로 쓰되, 생성형 AI 에이전트 사례로 둔갑시키면 안 된다.
2. **Lattice는 성공 사례가 아니라 실패 사례다.** 이 책에서 가장 유용한 소재이면서 가장 위험한 소재다 — 축 4(변화관리)와 교차한다.
3. **한국 은행권 "RPA 로봇 사번" 은 검증 실패했다.** 국내 은행 RPA 도입 자체는 다수 확인되나(KB국민·우리·NH농협·신한·IBK기업·부산은행), **사번/이름/계정 부여를 명시한 기사를 찾지 못했다.** 기억이나 통념으로 쓰지 마라.

### 사례 1: Deutsche Bank Blue Bot 'Yi'
- 출처: https://www.db.com/news/detail/20200720-deutsche-bank-s-corporate-bank-onboards-its-first-digital-employee-for-client-facing-role?language_id=1
- 저자·날짜: Deutsche Bank 공식 보도자료 · **2020-07-20**
- 신뢰성: **최상 (1차·직접 열람)**
- 핵심 주장: 도이체방크 Corporate Bank가 고객 대면 역할을 맡는 첫 "디지털 직원"을 온보딩했고, 그 디지털 직원에게 **사번과 업무 이메일**을 부여했다.
- 인용 가능한 구절 (원문 그대로):
  > "Blue Bot 'Yi' is the Corporate Bank's first digital employee with a client-facing role. It has been allocated an employee number and has a dedicated working email address."
  > "the onboarding of a new digital employee, named Blue Bot 'Yi' within its Corporate Bank"
- 세부: 상하이 Blue Water Fintech Space에서 RPA + 시맨틱 인식 + AI로 개발. 실시간 맞춤 거래 리포트, 캐시풀링 리포트, 고객 직접 문의 처리. 이름은 제작자 Zhu Yi(Head of China Innovation and Fintech Products – Corporate Bank)에서 따옴.
- 관련 섹션: PART 3 도입부 — "사번은 새로운 아이디어가 아니다. 2020년에 이미 있었다." 계보 서술의 출발점.

### 사례 2: Lattice의 "digital workers" 3일 천하
- 출처: https://www.shrm.org/topics-tools/news/technology/lattice-scraps-plans-to-treat-ai-bots-as-employees-after-backlash · https://www.inc.com/ben-sherry/nevermind-hr-company-lattice-decided-to-bring-ais-into-org-chart-then-changed-its-mind.html · https://fortune.com/2024/07/12/lattice-ai-workers-sam-altman-brother-jack-sarah-franklin
- 저자·날짜: SHRM / Inc. / Fortune · **2024-07 (발표 07-09, 철회 07-12)**
- 신뢰성: **중 (2차·검색 요약)** — 복수 매체 교차 확인됨, 다만 원문 본문 미열람. Sarah Franklin의 LinkedIn 원문 게시글은 **⚠️ 미확인**
- 핵심 주장: HR 플랫폼 Lattice가 "디지털 워커에게 공식 employee record를 주는 첫 회사"를 표방했다가, LinkedIn 여론의 반발로 **3일 만에** 철회했다.
- 인용 가능한 구절:
  > (Lattice CEO Sarah Franklin, 최초 LinkedIn 게시) "'digital workers' will be securely onboarded, trained, and assigned goals, performance metrics, appropriate systems access, and even an accountable manager." ⚠️ 원문 미열람
  > (철회 성명) "This innovation sparked a lot of conversation and questions that have no answers yet... We look forward to continuing to work with our customers on the responsible use of AI but will not further pursue digital workers in the product."
- **이 책에서의 쓰임새 (핵심):** Franklin이 나열한 항목 — *온보딩·교육·목표·성과지표·시스템 접근권·책임 매니저* — 는 **정확히 2년 뒤 Microsoft Entra Agent ID가 Owner/Sponsor/Manager로 제품화한 것과 같은 목록이다.** 즉 **아이디어가 틀린 게 아니라 프레이밍과 순서가 틀렸다.** "HR 시스템에 직원으로 넣겠다"(사람의 자리를 침범)와 "IAM에 신분을 부여하겠다"(계정을 정돈)는 기술적으로 유사하지만 **사회적으로 정반대로 받아들여졌다.**
- 관련 섹션: PART 3 도입 + PART 4(변화관리) 교차. 책 전체에서 가장 강력한 오프닝 후보.

### 사례 3: Goldman Sachs × Devin
- 출처: https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html (⚠️ **HTTP 403 — 본문 직접 열람 실패**)
- 보조 출처: https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin · https://www.forbes.com/sites/bernardmarr/2026/08/06/how-goldman-sachs-is-using-agentic-ai-for-software-engineering-at-scale/ (2026-08-06)
- 신뢰성: **중~하** — CNBC 원문 미열람. **"employee #1", "AI 직원" 표현은 매체의 수사이며 골드만삭스가 사번을 부여했다는 근거는 확인되지 않았다.**
- 확인된 사실: CIO **Marco Argenti**, 약 **12,000명** 개발 조직, 수백 개 Devin 인스턴스로 시작, "hybrid workforce" 프레이밍, 레거시 코드 관리·리팩터링·디버깅 등 반복 작업 배정, 인간 감독 지속.
- 인용 가능한 구절: Devin이 "on behalf of our developers" 로 일한다 (Argenti) ⚠️ 원문 미열람
- 관련 섹션: PART 3 — **"사번 없이도 조직에 편입되는 방식"** 의 대조군. 등록의 스펙트럼을 보여주는 데 쓴다.

---

## 1-2. NHI·에이전트 아이덴티티 — 벤더·표준 (GA / 프리뷰 / 발표만 구분)

> **2026년 9월 현재 상태.** 이 절의 모든 날짜·상태는 "2026-09-05 기준"이며, 이 영역은 분기 단위로 바뀐다. **책 본문에 쓸 때 반드시 "2026년 중반 기준"으로 못 박아라.**

| 벤더·표준 | 제품·기능 | 상태 (2026-09-05 기준) | 발표·GA일 | 신뢰성 | 출처 |
|---|---|---|---|---|---|
| **Microsoft** | **Entra Agent ID** | **GA** | **2026-05-01** | 최상 (1차 열람) | https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id |
| Microsoft | Entra Agent ID — 블루프린트/에이전트 생성 마법사 | **프리뷰** | 2026 | 최상 | 위와 동일 |
| Microsoft | **Agent 365** (에이전트 레지스트리·통합 관제) | **GA**, $15/user/월 (연약정) | 발표 2025-11-18(Ignite) / GA 2026-05-01 | 최상(제품 페이지 열람) / 중(GA일) | https://www.microsoft.com/en-us/microsoft-agent-365 |
| **Okta** | **Agent SSO** | **GA** (코어 SSO에 무상 포함) | **2026-08-24** | 최상 (보도자료 열람) | https://www.okta.com/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/ |
| Okta | **Cross App Access (XAA)** — OAuth 확장 | 발표 2025-06-23 → **MCP의 공식 Enterprise-Managed Authorization 확장으로 채택**(2026-08-24 확인) | 2025-06-23 / 2026-08-24 | 최상 | 위 + https://www.okta.com/newsroom/press-releases/okta-introduces-cross-app-access-to-help-secure-ai-agents-in-the/ |
| **Auth0** (Okta) | **Auth0 for AI Agents** — Auth for MCP, Agent as Principal, On-Behalf-Of Token Exchange, Token Vault, FGA Permissions Index | 2026-05 발표 (GA/프리뷰 구분 ⚠️ 미확인) | 2026-05 | 중 | https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/ |
| **CyberArk** | **Secure AI Agents** (권한 제어·발견·ZSP·감사·수명주기) | **GA** | **2025년 말** (정확일 ⚠️) | 중 | https://www.cyberark.com/press/cyberark-introduces-first-identity-security-solution-purpose-built-to-protect-ai-agents-with-privilege-controls/ |
| **SailPoint** | **Agentic Fabric** (에이전트·NHI 발견·거버넌스, 아이덴티티 그래프) | 발표 **2026-05-11**, **GA는 2026 여름 예정**으로 고지 → 현재 GA 여부 ⚠️ 재확인 필요 | 2026-05-11 | 중 | https://investor.sailpoint.com/news-releases/news-release-details/sailpoint-redefines-identity-security-new-adaptive-identity |
| **1Password** | **Unified Access Pro** (인간·머신·에이전트 통합 발견/보안/감사) | **GA** | **2026-03** | 중 | https://1password.com/press/2026/mar/1password-unified-access |
| **Astrix / Oasis Security / Token Security / Britive / Descope** | NHI·에이전트 아이덴티티 | **⚠️ 미확인** — 개별 GA 상태를 이번 리서치에서 검증하지 못함 | — | 하 | — |
| **Celonis × Microsoft Agent 365** | 프로세스 인텔리전스 연동 + Agent Mining | **프라이빗 프리뷰** | **2026-05-01** | 중 | https://www.celonis.com/blog/scaling-the-agentic-enterprise-with-microsoft-agent-365-and-celonis |

### 표준·프로토콜

| 표준 | 아이덴티티 관련 내용 | 상태·날짜 | 신뢰성 |
|---|---|---|---|
| **MCP Authorization** | MCP 서버 = OAuth **2.1** 리소스 서버. PKCE, Authorization Server Metadata, Protected Resource Metadata, **Resource Indicators(RFC 8707)** 의무화 | 2025-03-26 개정: OAuth 2.1 프레임워크 도입 → 2025-06-18 개정: 리소스 서버로 분류 + RFC 8707 요구 → **2026-07-28 개정: 출시 이래 최대 개정, 코어를 stateless로, 인가 동시 강화** | 중 (spec 페이지 미열람) |
| **A2A (Agent2Agent)** | 각 에이전트가 **agent card**에 OAuth 2.0 / OIDC / mTLS 중 자신이 요구하는 인증 방식을 선언. **v1.0에서 signed agent card 추가** → 카드 발급자 검증 가능 | Google 발표 **2025-04-09** → Linux Foundation 기증 **2025-06-23** → **v1.0**. 지원 조직 150+ , 운영위원회에 AWS·Cisco·Google·IBM·Microsoft | 중 |
| **SPIFFE / SPIRE** | 공유 API 키 대신 워크로드에 **암호학적 신분** 부여. 2025~2026 에이전트에 적용 확산, HashiCorp Vault 1.21(2025)에 네이티브 SPIFFE 인증 추가 | 2025~2026 | 중 |
| **AGNTCY / W3C DID** | — | **⚠️ 미확인** — 이번 리서치 범위에서 검증 실패 | 하 |

### 자료: Microsoft Entra Agent ID — GA 릴리스 노트
- 출처: https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id
- 저자·날짜: Microsoft Learn (author: Dickson-Mwendia) · **ms.date 2026-05-01, 최종 갱신 2026-08-13**
- 신뢰성: **최상 (1차·직접 열람, 공식 문서)**
- 핵심 주장: Entra Agent ID가 GA되면서 AI 에이전트에 **일급 아이덴티티·접근 관리**가 부여됐다.
- 인용 가능한 구절 (원문 그대로):
  > "Microsoft Entra Agent ID is now generally available. This release brings first-class identity and access management to AI agents, enabling organizations to authenticate, authorize, govern, and protect agent identities at enterprise scale."
  > "Microsoft Entra Agent ID extends Zero Trust principles to AI workloads with purpose-built identity constructs, specialized OAuth flows, and comprehensive security controls."
- **책에 직접 쓸 수 있는 기능 목록 (전부 공식 문서 확인):**
  - `agent identity blueprint` / `agent identity` / `agent's user account` — **에이전트가 "사용자 계정"을 별도로 가질 수 있다** (에이전트 전용 Entra user)
  - **Agent identity deletion** — "automated cascade cleanup process and soft-delete functionality" → **폐기(오프보딩)가 제품 기능으로 존재한다**
  - **Sponsor lifecycle workflows** — "Automate sponsor maintenance and reassignment for agent blueprints and agent identities"
  - **Agent identity sponsor templates** — "Two new lifecycle workflow templates for notifying managers and cosponsors, and automatically transfer sponsorship when an agent identity sponsor changes roles or leaves the organization, **to prevent orphaned agents.**"
  - **Access packages for agent identities** — OBO(on-behalf-of)와 autonomous(non-OBO) 시나리오 모두 정책 기반 접근 부여
  - **Conditional Access 템플릿 3종** — 고위험 에이전트 차단 / 자율 에이전트용 / OBO 에이전트용
  - 마이그레이션 경로 — 기존 app registration을 쓰던 에이전트를 Agent ID로 이전, Copilot Studio 에이전트 이전
  - 비(非)MS 플랫폼 연동 — AWS Bedrock, GCP, n8n (sidecar / federation 패턴)
  - **레지스트리 수렴:** "agent registry experiences are converging under Microsoft Agent 365" — Agent 365가 발견·관리의 단일 창구, Entra는 아이덴티티 기반 제공
- 관련 섹션: PART 3 전체의 **기술 레퍼런스**. "사번을 준다"가 은유가 아니라 제품 스펙이 된 증거.

### 자료: Okta Agent SSO GA
- 출처: https://www.okta.com/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/
- 저자·날짜: Okta 공식 보도자료 · **2026-08-24**
- 신뢰성: **최상 (1차·직접 열람)**
- 핵심 주장: XAA를 지원하는 에이전트가 기업 앱에 접속할 때, Okta는 그 에이전트를 **Universal Directory에 인간 직원과 나란히 일급 아이덴티티로 등록**하고, 저장된 자격증명 대신 **수명이 짧은 거버넌스 토큰**을 발급한다.
- 인용 가능한 구절 (원문 그대로):
  > "When such an agent connects to an enterprise application, Okta registers it as a first-class identity in Universal Directory alongside human employees, then issues short-lived, identity-governed tokens in place of stored credentials."
- 핵심 수치:
  > "Only 34% of organizations apply the same security controls to AI agents as they do to human workers." (Okta *AI Agents at Work 2026*)
- 부가: 관리자가 **인간 직원과 동일한 콘솔·워크플로**로 에이전트 접근을 관리. 코어 Okta SSO에 **추가 비용 없이** 포함. 사전 통합 파트너: Anthropic(Claude), Archestra.AI, Asana, Atlassian, Canva, Datadog, Figma, Glean, Granola, Linear, MintMCP, Notion, Slack, Supabase.
- 관련 섹션: PART 3 — "등록"이 이미 벤더 기본 기능이 되었다는 근거. **"같은 콘솔로 관리한다"** 는 문장이 이 책 주장의 산업적 확증.

### 자료: Okta *AI Agents at Work 2026* 조사
- 출처: https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/
- 저자·날짜: Okta 커미션, **Apprize360** 수행 · 2026-03 필드 · 2026 발행 (정확일 ⚠️)
- 신뢰성: **중 (2차·검색 요약)**
- 표본: **경영진 292명 + 지식근로자 492명**, 7개국(미국·영국·호주·캐나다·일본·프랑스·독일)
- 핵심 수치:
  - 34% — AI 에이전트에 인간 직원과 **동일한 보안 통제**를 적용하는 조직 비율
  - 보안 문제를 보고한 응답자 중 **26.7%가 실제 사고**(유출·데이터 노출·시스템 장애), **31.2%는 사전 차단된 아차사고**
  - 지식근로자 응답자의 **100%가 직전 3개월간 AI와 함께 일했다**고 응답
- 관련 섹션: 축 1 문제 제기 + 축 3(shadow AI) 교차.

---

## 1-3. 온보딩·오프보딩·권한 위임·감사·책임 귀속 설계

> **이 책의 가장 희소한 광맥이 여기다.** 특히 **오프보딩(폐기)** 은 2026년 현재 산업 전체가 못 하고 있는 일이고, 그 사실 자체가 수치로 증명되어 있다.

### 자료: Microsoft Entra — Owner / Sponsor / Manager 3역할 모델 【★ 이 책의 핵심 레퍼런스】
- 출처: https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers
- 저자·날짜: Microsoft Learn · **ms.date 2026-04-16, 최종 갱신 2026-09-03**
- 신뢰성: **최상 (1차·직접 열람, 공식 문서)**
- 핵심 주장: Entra Agent ID는 **기술 관리(technical administration)와 사업 책임(business accountability)을 분리**하는 관리 모델을 도입했다. **모든 에이전트 아이덴티티에는 최소 1명의 스폰서(사람 또는 그룹)가 반드시 있어야 한다.**
- 인용 가능한 구절 (원문 그대로):
  > "Microsoft Entra Agent ID introduces an administrative model that separates technical administration from business accountability, ensuring operational control and oversight without excessive permissions."
  > **Owners**: "Technical administrators responsible for operational management of agent identity blueprints and agent identities, including setup, configuration, and credential management."
  > **Sponsors**: "Business representatives accountable for the agent's purpose and lifecycle decisions, including access reviews and agent retention, without technical administrative access. **At least one sponsor is required for each agent identity and agent identity blueprint.**"
  > **Managers**: "User responsible for the agent within the organization's hierarchy, able to request access packages for their reporting agents."
- **설계 디테일 (본문에 그대로 쓸 수 있는 재료):**

| 항목 | Owner | Sponsor | Manager |
|---|---|---|---|
| 성격 | 기술 관리자 | 사업 책임자 | 조직 계층상 상급자 |
| 필수 여부 | **선택** | **필수** (생성 시 반드시 지정) | 선택 |
| 전형적 인물 | 개발자, IT 전문가, 에이전트 제작자, 기술 앱 오너 | 비즈니스 오너, 프로덕트 매니저, 팀 리드 | 인간 관리자 |
| 할당 가능 대상 | 개인 사용자(게스트 포함), **서비스 주체(service principal)** — 그룹 불가 | 사용자(게스트 포함) + 특정 그룹(동적 멤버십, M365). **역할 할당 가능 그룹은 불가** | 개인 사용자만 |
| 최대 수 | — | 에이전트 아이덴티티 기준 **최대 100명(그룹은 5개 이내)**, 에이전트 사용자 계정 기준 최대 5명 | — |
| 할 수 있는 일 | 인증 속성 등 스폰서가 못 바꾸는 속성 변경, 오너·스폰서 추가, 비활성화, 삭제, **재활성화·소프트삭제 복원·하드삭제** | 수명주기 결정(갱신·연장·제거), 에이전트 대신 액세스 패키지 요청, 사업적 정당화 제공, **보안 사고 시 에이전트 행동이 정상인지 판단하고 정지·권한조정 승인** | 자기 밑으로 보고되는 에이전트를 관리센터에서 조회, 액세스 패키지 요청 |
| 할 수 없는 일 | — | 앱 설정 변경 불가. **재활성화·복원 불가** (실수로 지웠으면 오너/관리자에게 요청) | **수정·삭제 불가** |

  > (스폰서 승계) "Sponsorship should be maintained to ensure succession when an employee who's a sponsor moves or leaves."
  > (자동 스폰서 배정 규칙) "For delegated creation requests where both an application and user context exist, **the calling user automatically becomes the sponsor if no sponsors are explicitly specified.** ... **Users with Agent ID admin roles aren't made sponsor automatically during creation. This avoids unintentionally overburdening admins with direct responsibility for individual agents.**"
- **이 책에서의 쓰임새 (핵심 중의 핵심):**
  - 전작이 "사번을 준다면"이라고 전망만 남긴 자리에, **이미 산업 표준 설계가 존재한다**는 답을 줄 수 있다.
  - 특히 **"스폰서 필수 + 관리자는 자동 스폰서가 되지 않음"** 이라는 설계 결정은 이 책의 핵심 주장 — *등록은 통제가 아니라 책임의 소재를 만드는 일* — 을 벤더가 그대로 구현한 증거다.
  - **"기술 관리 ≠ 사업 책임"의 분리**는 한국 조직의 "IT부서가 다 알아서" 관성을 깨는 설계 논거로 쓸 수 있다.
- 관련 섹션: **PART 3의 뼈대 챕터 하나를 통째로 이 문서로 세울 수 있다.**

### 자료: CSA — *The Non-Human Identity Governance Vacuum*
- 출처: https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/ (PDF: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_whitepaper_nonhuman_identity_agentic_ai_governance_v1-csa-styled.pdf)
- 저자·날짜: Cloud Security Alliance · **2026-05-20**
- 신뢰성: **최상~중** (랜딩 페이지 직접 열람 / PDF 본문은 바이너리 파싱 실패 → 수치는 랜딩 페이지 요약 기준)
- 정식 제목: *"The Non-Human Identity Governance Vacuum: AI Agents and the Fastest-Growing Unmanaged Attack Surface"*
- **핵심 수치 (이 책 축 1의 문제 제기에 그대로 쓸 수 있음):**

| 수치 | 내용 |
|---|---|
| **144 : 1** | 클라우드 네이티브 환경의 NHI 대 인간 비율 |
| **45 : 1** | 전체 기업 평균 NHI 대 인간 비율 |
| **8%** | "legacy IAM 시스템이 AI·NHI 위험을 관리할 수 있다"에 **높은 확신**을 표한 응답자 비율 |
| **78%** | **AI 아이덴티티의 생성 또는 제거에 관한 문서화된 정책이 없는** 조직 비율 |
| **51%** | **AI 아이덴티티의 소유권이 불명확**하다고 보고한 조직 비율 |
| **44%** | 2024~2025 사이 측정된 기업 환경의 NHI 증가율 |

- 인용 가능한 구절:
  > "78% of organizations have no documented policy for creating or removing AI identities"
  > "51% of organizations report no clear ownership of AI identities"
  > "Only 8% of respondents expressed high confidence that their legacy IAM systems can manage AI and NHI risks"
- 위험의 성격에 대한 서술 (요약):
  > AI 에이전트는 런타임에 동적으로 권한을 획득하고, 하위 에이전트를 생성하며, 외부 API를 호출하고, 코드를 작성·실행하고, 수십 개 시스템에 걸친 행동을 연쇄시킨다 — 자격증명 하나가 뚫렸을 때의 폭발 반경이 정적 서비스 계정과는 차원이 다르다.
- CSA의 권고: NHI를 소프트웨어 배포의 **비공식 부산물**로 취급하는 것을 멈추고 **정식 아이덴티티 거버넌스**에 편입시켜라.
- 관련 섹션: PART 3 문제 제기 — **"78%가 폐기 정책이 없다"는 이 책 전체에서 가장 강력한 단일 수치다.**

### 자료: 오프보딩·좀비 에이전트 — 개념 정리
- 출처: https://www.darkreading.com/identity-access-management-security/the-lifecycle-crisis-managing-the-birth-life-and-death-of-ai-agents · https://nhimg.org/community/nhi-best-practices/ai-agent-offboarding-what-happens-when-the-worker-never-leaves/ · https://labs.cloudsecurityalliance.org/agentic/agentic-identity-governance-framework-v1/
- 발행일: **⚠️ 개별 기사 발행일 미확인** (Dark Reading 기사 날짜 확인 필요)
- 신뢰성: **중~하 (2차·검색 요약)** — 개념 정리용으로만 쓰고, 수치는 재확인
- 핵심 개념 (본문 용어로 쓸 만함):
  - **revocation ≠ deprovisioning:** 폐기(revocation)는 활성 세션의 즉시 종료, 디프로비저닝은 아이덴티티와 부여된 권한의 **영구적·완전한 제거**. 취소만 된 에이전트는 **등록과 신뢰 관계를 그대로 보유**할 수 있다 → 이 구분이 실무 설계의 핵심.
  - **zombie agent / orphaned agent:** 상시 접근 권한은 있는데 끌 스위치가 없는 고아 NHI. 감시받지 않으므로 공격자가 발견하면 그 권한을 그대로 상속한다.
  - **shadow agent:** 보안 승인 없이 직원이 만든 AI 자동화·서비스 계정·API 토큰·머신 아이덴티티.
  - **정상적 오프보딩 절차 (제안된 형태):** ① 중앙 IdP에서 에이전트 코어 아이덴티티 종료 → ② IdP가 모든 연합 도메인에 디프로비저닝 시그널 브로드캐스트 → ③ 모든 ACL에서 식별자 제거(고아 권한 방지)
  - **20%** — API 키 오프보딩·회수에 대한 공식 프로세스를 갖춘 조직 비율 ⚠️ 출처 재확인 필요
- 관련 섹션: PART 3 — **"폐기 설계" 챕터.** Entra의 soft-delete/cascade cleanup(1-2 참조)과 짝지어 쓰면 강력하다.

### 자료: Deloitte — 가드레일보다 빨리 확산되는 에이전트
- 출처: https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html
- 저자·날짜: Deloitte Insights · **2026-04-24** (*2026 State of AI in the Enterprise* 기반)
- 신뢰성: **최상 (1차·직접 열람)**
- 표본: **IT·비즈니스 리더 3,235명, 24개국** (미주·아태·유럽·중동)
- 핵심 수치:
  - **21%** — 에이전틱 AI에 대해 **성숙한 거버넌스 모델**을 갖췄다는 응답 비율 (→ 약 80%가 없음)
  - **74%** — 2027년까지 AI 에이전트를 최소 "moderately" 쓸 것으로 기대하는 비율 (그중 23% "extensively", 5% 완전 통합)
  - **23%** — 현재 에이전틱 AI를 최소 "moderately" 사용 중인 기업 비율
  - **85%** — 자사 필요에 맞게 에이전트를 커스터마이즈할 계획인 기업 비율
- 인용 가능한 구절:
  > "only 21% of respondents say their organizations have a mature governance model in place for agentic AI"
  > (제목) "Business and IT leaders report AI agents are scaling faster than their guardrails"
- Deloitte가 짚은 **결여된 거버넌스 3요소** (원문 그대로):
  > "clear boundaries for agents that define which decisions they can make independently versus which require human approval, real-time monitoring systems that track agent behavior and flag anomalies, and audit trails that capture the full chain of agent actions"
- 관련 섹션: 축 1 + 축 3 교차. **"23% 쓰는데 21%만 거버넌스"** 라는 대비가 이 책의 존재 이유를 한 줄로 요약한다.

### 자료: NHI 대 인간 비율 — 조사기관별 편차
- 신뢰성: **중~하** — **기관마다 수치가 크게 다르다. 하나만 골라 단정하면 fact-check에서 걸린다.**

| 출처 | 비율 | 기준 시점 | URL |
|---|---|---|---|
| CyberArk | **82 : 1** | 2025-04 | https://www.cyberark.com/press/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security/ |
| Palo Alto Networks *2026 Identity Security Landscape* | **109 : 1** (그중 **79개가 AI 에이전트** ≈ 72.5%) | 2026 | https://www.paloaltonetworks.com/idira/idira-identity-security-landscape |
| CSA | **45 : 1** (평균) / **144 : 1** (클라우드 네이티브) | 2026-05 | 위 CSA 백서 |
| Entro Security | **144 : 1** (2024 상반기 92:1에서 상승) | 2025~2026 | ⚠️ 원문 미확인 |

- **저술 권고:** 단일 수치 대신 **"조사마다 45:1에서 144:1까지 갈린다"** 로 쓰는 편이 정확하고, 오히려 **"아무도 정확히 세지 못한다"** 는 이 책의 논지(= 그래서 등록이 필요하다)를 강화한다.
- 부가 수치: **88%** 의 응답자가 자사에서 "특권 사용자(privileged user)" 정의를 **인간에게만** 적용하는데, **머신 아이덴티티의 42%가 특권·민감 접근권을 갖고 있다** (CyberArk) ⚠️ 원문 재확인 필요

---

## 1-4. 제도·규제 (조문 번호·시행일)

> **⚠️ 최우선 신선도 경보:** EU AI Act의 고위험 의무 시행일이 **2026년에 실제로 연기됐다.** 2025년 이전에 쓰인 모든 자료(그리고 대다수 LLM의 기억)는 **"2026-08-02 고위험 시행"** 을 말하는데 **이는 2026년 9월 현재 틀렸다.** 이 책이 2026년 이후 독자에게 읽힌다면 이 지점이 신뢰의 분수령이다.

### 1-4-1. EU AI Act (Regulation (EU) 2024/1689)

#### (a) 등록 의무 — Article 49
- 출처: https://artificialintelligenceact.eu/article/49/ (Annex VIII: https://artificialintelligenceact.eu/annex/8/)
- 신뢰성: **최상 (1차·직접 열람, 조문 정리 사이트)**
- 조문 요지 (문단별):
  - **Art. 49(1):** 고위험 AI 시스템 **제공자(provider)** 는 시장 출시 전 **EU 데이터베이스에 자신과 시스템을 등록**해야 한다 (Annex III point 2 예외).
  - **Art. 49(2):** Art. 6(3)에 따라 **"고위험이 아니다"라고 스스로 판단한** 시스템도 등록 대상.
  - **Art. 49(3):** **배포자(deployer) 중 공공기관·EU 기관·그를 대신하는 자**는 서비스 개시·사용 전 자신과 그 사용을 EU DB에 등록해야 한다. **→ 민간 배포자는 현재 등록 의무 없음** (대신 Art. 26의 다른 의무를 진다).
  - **Art. 49(4):** 법집행·이주·망명·국경관리 용도는 **비공개 보안 구역**에 등록. "Only the Commission and national authorities referred to in Article 74(8) shall have access".
  - **Art. 49(5):** Annex III point 2 시스템은 **국가 단위 등록**.
  - **Art. 71:** EU 데이터베이스의 근거 조문. **Annex VIII** 이 등록 시 제출 정보(Section A/B/C)를 규정.
- **책에서의 쓰임새:** "국가가 AI 시스템에 **등록번호**를 요구한다"는 제도적 선례. 사내 에이전트 등록이 자의적 관료주의가 아니라 **규제가 요구하는 방향과 같은 방향**임을 보이는 데 쓴다. 단, **민간 배포자는 아직 EU DB 등록 대상이 아니라는 점을 정확히 써야 한다.**

#### (b) 【핵심 최신】 Digital Omnibus — 고위험 의무 연기
- 출처: https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ (**2026-05-27**, 직접 열람) · https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/ · https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/
- 신뢰성: **최상 (Gibson Dunn 직접 열람) + 중 (규정 번호·관보일은 2차)**
- **확정된 사실 (Gibson Dunn 2026-05-27 직접 열람):**
  - Annex III 독립형 고위험 시스템 의무 → **2027-12-02** 로 연기
  - Annex I 규제 제품 내장 AI → **2028-08-02** 로 연기
  - **변경되지 않은 것:** 금지 조항(Art. 5) **2025-02-02 시행 중** (누디파이어/CSAM 금지가 추가됨), GPAI 의무(Art. 51~56) **2025-08-02 시행 중** (집행 범위 명확화)
  - 연기 사유: **정합표준(harmonized standards)의 지연** — 원래 일정대로면 기업이 확정된 기준 없이 준수를 입증해야 했다.
  - 협상 경과: 2026-04-28 1차 삼자협상 결렬 → **2026-05-06 잠정 정치적 합의** → **2026-05-13 이사회 회원국 대표 확인**
- **⚠️ 2차 출처로만 확인 (Phase 4 fact-checker가 EUR-Lex로 대조 필요):**
  - 규정 번호 **Regulation (EU) 2026/1744** ("Digital Omnibus on AI")
  - 관보(OJ) 게재 **2026-07-24**, 발효 **2026-07-27** — 원래 마감(2026-08-02) 6일 전
  - Gibson Dunn(2026-05-27) 시점에는 아직 "Formal adoption and publication in the Official Journal are expected in the coming weeks, in advance of the 2 August 2026 deadline." 라고만 되어 있었음 → 이후 실제로 게재된 것으로 보이나 **EUR-Lex 원문 확인 필요**
  - **Art. 49 등록 의무 자체가 어떻게 조정됐는지는 Gibson Dunn 문서에 언급 없음 → ⚠️ 미확인**
- **저술 규율:** 이 항목은 반드시 **"2026년 9월 기준"** 으로 못 박고, "고위험 의무는 2027년 12월로 미뤄졌다 — 다만 금지 조항과 GPAI 의무는 이미 시행 중"이라는 **두 겹**을 함께 써라. "AI Act가 통째로 미뤄졌다"는 흔한 오해다.

### 1-4-2. NIST AI RMF 1.0
- 출처: https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf (NIST AIRC 공식 크로스워크) · https://techjacksolutions.com/framework-explorer/nist-ai-rmf/
- 발행: **NIST AI RMF 1.0 — 2023-01** / Generative AI Profile (**NIST AI 600-1**) — **2024-07** ⚠️ 600-1 원문 미열람
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 서브카테고리 번호에 출처 간 충돌이 있다**
- **⚠️ 충돌 경보:** 검색 결과 중 하나는 GOVERN 1.6을 "제3자 AI 시스템 리스크 관리"로 서술했으나, 다른 출처와 통상적 이해는 **GOVERN 1.6 = "AI 시스템을 인벤토리하는 메커니즘이 마련되어 있고 조직의 리스크 우선순위에 따라 자원이 배분된다"** 이다. **이 책에 조문 번호를 쓸 거라면 NIST AI RMF 1.0 원문(Playbook 포함)을 반드시 직접 대조하라.**
- 확인된 개념 골자:
  - **GOVERN** = 누가 책임지는가 / **MAP** = 무엇에 대해 책임지는가
  - 역할·책임 정의에 **AI 시스템 오너(AI system owner)** 와 **모델 리스크 오너** 를 포함하고, GOVERN 기능 요구사항에 대한 명확한 책임 귀속과 **그 책임의 문서화된 수용(documented acceptance)** 을 요구
  - MAP은 운영·조달하는 **모든** AI 시스템에 대해 문서화된 컨텍스트, 리스크 분류, 역량 기록, 영향 평가, **명명된 리스크 수용자(named risk acceptance)** 를 요구
- 관련 섹션: PART 3 — "등록은 규제가 이미 요구하는 것"의 미국판 근거. **"named risk acceptance"** 라는 표현이 이 책의 '소유자' 개념과 정확히 맞물린다.

### 1-4-3. ISO/IEC 42001:2023 (AI 경영시스템, AIMS)
- 출처: https://www.schellman.com/blog/ai-governance/iso-42001-roles-and-responsibilities · https://www.hicomply.com/hub/annex-a-controls · https://www.surecloud.com/resource-hub/iso-42001-annex-a-controls
- 발행: **2023-12** (ISO/IEC 42001:2023)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 개별 Annex A 통제 번호(A.x.y)는 확인하지 못했다. 표준 원문은 유료이므로 번호를 본문에 쓰려면 재확인 필수.**
- 확인된 구조:
  - Annex A는 **38개 참조 통제**, **9개 통제 목적(A.2 ~ A.10)** 으로 구성
  - ISO 27001과 달리 **참조 세트(reference set)** — 적용 가능한 통제를 선택하고 제외 사유를 **적용성 선언서(SoA, Statement of Applicability)** 에 정당화해야 한다
  - 9개 목적의 축: AI 정책 / 내부 조직 / 자원 및 영향 평가 / AI 시스템 수명주기 / 데이터 / 투명성 / 책임 있는 사용 / 제3자 관계
  - **AIMS 범위 설정 시 조직은 범위 내 AI 시스템에 대한 자신의 역할(provider/deployer 등)을 공식적으로 규정해야 한다**
  - 심사원은 **완전한 AI 시스템 인벤토리**와 문서화된 프로세스·책임을 요구한다
  - 자원 인벤토리: 코드뿐 아니라 **데이터·컴퓨팅·소프트웨어·사람**까지 문서화. 소유권 정의, 버전 관리, 변경 로그, 데이터 품질 통제, 정기 감사를 갖춘 인벤토리 관리 프로세스가 모범
- **인증 취득 기업 사례: ⚠️ 미확인** — 이번 리서치에서 공개 사례를 검증하지 못했다. 필요하면 별도 조사.
- 관련 섹션: PART 2(SOP)와 PART 3(등록)을 잇는 다리. "인벤토리 + 소유권 + 수명주기"라는 세 단어가 이 책의 뼈대와 같다.

### 1-4-4. 한국 — AI 기본법
- 정식명: **인공지능 발전과 신뢰 기반 조성 등에 관한 기본법**
- 시행일: **2026-01-22**
- 출처: https://www.shinkim.com/kor/media/newsletter/3114 (세종/신&김 등 로펌 뉴스레터) · https://datalaw.kr/posts/ai-basic-law-business-duties/ · https://www.lawtimes.co.kr/news/articleView.html?idxno=216500
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 조문 번호를 확인하지 못했다. 국가법령정보센터 원문 대조 필요.**
- 확인된 골자:
  - **고영향 인공지능** 및 **생성형 인공지능** 사업자에 구체적 책무 부과
  - **투명성 확보 의무:** 고영향 AI 또는 생성형 AI를 활용한 제품·서비스 제공 시 **AI 기반 운영 사실을 이용자에게 사전 고지**
  - **안전성 확보 의무**
  - **의무 주체의 범위:** 모델을 만드는 회사만이 아니라 **남이 만든 AI를 이용해 제품·서비스를 제공하는 회사까지 포함한 "인공지능사업자"** → **이 책 독자(도입 조직)가 정확히 여기 해당한다**
  - **계도 기간:** 과기정통부가 시행 후 **최소 1년 이상**의 유예 기간 운영 → **2027-01 무렵까지** ⚠️ 정확한 종료 시점 재확인
- **책에서의 쓰임새:** 한국 독자에게 가장 직접적인 압력. **"우리는 AI를 만들지 않고 쓰기만 하는데요"가 면책이 아니라는 점**이 이 법의 핵심이고, 이 책이 말하는 등록·기록의 실무적 근거가 된다.

### 1-4-5. 한국 — 개인정보보호위원회
- **생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서** — **2025-08-06** 공개
  - 출처: https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11410
  - 신뢰성: 중
- **생성형 AI 서비스 이용자를 위한 개인정보 보호 가이드** — 2026-05 발간 (바이라인네트워크 2026-05-19 보도)
  - 데이터 수집 → AI 학습 → 서비스 이용 → **외부 서비스 연동** 4단계로 개인정보 처리 지점 구분 (마지막 단계가 에이전트·MCP 시대의 쟁점)
- **2026년 업무 추진계획:** 사전적정성 검토제를 AI 등 신기술 **기획 단계부터** 적극 운영, AI 합성콘텐츠에 대한 정보주체의 삭제 요구권 및 사업자 조치 의무 신설 계획
  - 출처: https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=33715
  - 신뢰성: 중

### 1-4-6. 미국 연방 — OMB M-24-10 / M-25-21
- 출처: https://static.carahsoft.com/concrete/files/9717/4412/5797/Guidance_M-25-21_Accelerating_Federal_Use_of_AI_through_Innovation_Governance_and_Public_Trust.pdf · https://www.wiley.law/alert-Trump-Administration-Revamps-Guidance-on-Federal-Use-and-Procurement-of-AI · 실제 인벤토리 예: https://www.justice.gov/ai/ai-inventory
- 신뢰성: **중 (2차·검색 요약)** — 다만 **각 부처가 실제로 공개 인벤토리 페이지를 운영 중**이라는 사실 자체는 URL로 확인 가능
- 확인된 골자:
  - **M-24-10** (2024-03) → **M-25-21** (**2025-04-03**) 로 **폐지·대체**
  - **Chief AI Officer(CAIO)** 를 60일 내 지정/유지, **AI Governance Board** 를 90일 내 소집
  - 모든 CFO Act 대상 기관은 AI 조달·배포·거버넌스에 대한 명확한 권한을 가진 CAIO를 두고, CAIO는 기관 지도부에 보고
  - **연례 AI use case inventory** 를 작성 → OMB 제출 → **공개 가능한 항목은 기관 웹사이트에 게시**
  - 고영향(high-impact) AI에 최소 리스크 관리 관행 적용
- **책에서의 쓰임새:** **"공공기관이 AI 목록을 만들어 공개한다"** 는, 이 책이 말하는 등록의 가장 가시적인 실물. 실제 인벤토리 페이지(예: 법무부)를 독자에게 보여줄 수 있다.

### 1-4-7. 중국 — 알고리즘 등록제(算法备案) + 생성형 AI 잠행 조치
- 출처: http://english.scio.gov.cn/pressroom/2025-04/09/content_117814020.html (국무원 신문판공실, **2025-04-09**) · https://appinchina.co/what-is-chinas-ai-algorithm-filing/ · https://www.lexology.com/library/detail.aspx?g=3c7273cf-8f85-4702-af70-6edf394ff1c3
- 신뢰성: **중 (2차·검색 요약)** — SCIO 발표(346건)는 정부 출처
- **핵심 수치 (등록제가 실제로 굴러간다는 증거):**

| 시점 | 수치 |
|---|---|
| 2025-03-31 기준 | 생성형 AI 서비스 **346건** CAC 등록 완료 |
| 2025-08-31 기준 | 생성형 AI 서비스 **538건** 신고 + 애플리케이션 등록 **263건** = **801건** 승인 |
| 2025-11 기준 | 국가 등록 플랫폼 누적 알고리즘 **5,822건**, 그중 **67.3%가 생성형 AI** 관련 |

- 제도: **생성형 인공지능 서비스 관리 잠행 조치(2023)** — 신고(filing) 및 안전 평가, 모델 유형·데이터셋 출처·리스크 완화 조치·**지정 책임자(designated responsible personnel)** 공개 의무
- **책에서의 쓰임새:** **"지정 책임자"** 라는 요구는 Entra의 sponsor, NIST의 named risk acceptance와 **같은 것을 다른 언어로 말한다.** 제도와 제품이 독립적으로 같은 결론에 도달했다는 논거 — 이 책 축 1의 가장 세련된 논증이 될 수 있다.

### 1-4-8. 일본
- **AI 사업자 가이드라인: ⚠️ 미확인** — 이번 리서치에서 원문·판본을 검증하지 못했다.
- 확인된 것: 닛케이 **2026-07-09** 기사 표제·리드 — *「社員と化すAIエージェント、費用は人件費？ 人事とITの境界溶かす」* (사원이 되어가는 AI 에이전트, 비용은 인건비? 인사와 IT의 경계를 녹이다). 리드: AI 에이전트 기반의 등장으로 "AI社員"이 탄생, 인건비로 계상하는 기업이 나타나고 있음. 언급된 도구: "OpenClaw", Anthropic "Claude Cowork".
  - 원문 인용 가능 구절 (리드 부분): 「人が細かく指示しなくても、ゴールまでの道筋を自ら考えて実行し、夜間や休日も関係なく業務を進める、まさに社員」
  - **⚠️ 본문은 유료 구간 — 구체 기업명·수치는 확인 불가.**
- 관련 섹션: 축 4(변화관리) — "AI 예산 vs 인건비" 논쟁의 아시아 사례.

---

## 축 1 커버리지

**확보한 것 (강함):**
- ✅ 사번 부여 1차 사례 1건 — **Deutsche Bank Blue Bot 'Yi' (2020-07-20, 공식 보도자료 직접 열람)**
- ✅ 실패 사례 1건 — **Lattice (2024-07, 발표 후 3일 만에 철회)**. 축 1과 축 4를 잇는 최고의 소재
- ✅ **Owner/Sponsor/Manager 3역할 설계 원본** — Microsoft Entra 공식 문서 직접 열람. **이 책 PART 3의 뼈대로 즉시 사용 가능**
- ✅ 오프보딩이 제품 기능으로 존재한다는 증거 — soft-delete, cascade cleanup, **고아 에이전트 방지용 스폰서 승계 워크플로**
- ✅ "78%가 AI 아이덴티티 생성·제거 정책이 없다" (CSA 2026-05-20) — 축 1 문제 제기의 결정타
- ✅ "21%만 성숙한 에이전틱 거버넌스" (Deloitte 2026-04-24, n=3,235, 24개국)
- ✅ 벤더 GA 타임라인 정리 — Entra Agent ID(2026-05-01), Agent 365(2026-05-01), Okta Agent SSO(2026-08-24), 1Password(2026-03), CyberArk(2025 말), SailPoint(2026-05-11 발표)
- ✅ 제도 4개 관할 — EU(Art. 49 + **연기된 시행일**), 미국(M-25-21 + 실제 인벤토리 페이지), 중국(등록 건수 실적), 한국(AI 기본법 2026-01-22)
- ✅ **EU 고위험 의무 2027-12-02 연기** — 이 책의 신선도 우위를 만드는 사실

**비어 있는 것 (⚠️ 후속 필요):**
- ❌ **한국 사례 전무.** 국내 은행권 RPA 사번 부여를 검증하지 못했다 — 국내 사례는 이 책의 한국 독자 설득력에 중요하므로 별도 심층 조사 권고 (금융권 RPA 백서, 금융보안원 자료, 전자신문/디지털데일리 아카이브)
- ❌ **일본 구체 사례.** 닛케이 본문 유료 → 기업명·수치 미확보
- ❌ **ISO/IEC 42001 Annex A 통제 번호** — 유료 표준, 번호 인용 불가
- ❌ **NIST AI RMF 서브카테고리 번호 충돌** — 원문 대조 필요
- ❌ **Astrix / Oasis Security / Token Security / Britive / Descope / WorkOS** 의 개별 GA 상태
- ❌ **AGNTCY, W3C DID** 의 에이전트 아이덴티티 적용
- ❌ **ISO 42001 인증 취득 기업 공개 사례**
- ❌ **통신·제조·공공 산업의 등록 사례** — 확보된 사례가 금융(DB, GS)·IT(MS)에 편중

---

# 축 2 — SOP에서 출발하는 체계 구축

## 2-1. 고전의 재해석 — ISO 9001, Toyota 표준작업

### 자료: ISO 9001:2015 Clause 7.5 — 문서화된 정보
- 출처: https://www.isms.online/iso-9001/clause-7-5-documented-information/ · https://www.thecoresolution.com/clause-7-5-1-9001-2015-explained
- 발행: ISO 9001:2015 (표준 자체) / 해설 글 발행일 ⚠️ 미확인
- 신뢰성: **중 (2차)** — 표준 원문 유료
- 핵심 주장: 7.5는 문서화된 정보의 **통제와 가용성**을 요구하되, **형식이나 문서 구조를 규정하지 않는다.** 7.5.1은 조직 규모·복잡도·리스크에 따라 **필요한 문서화의 정도를 조직이 스스로 정하도록** 유연성을 준다.
- 인용 가능한 구절 (개념):
  > 문서화된 정보는 **지식의 운반체(a carrier of knowledge)**, **의도를 전달하는 수단(a means to communicate intent)**, **품질 프로세스가 준수되고 목표가 달성되었다는 증거의 기록(a record of evidence)** 으로 기능한다.
- **책에서의 쓰임새:** 이 세 기능 — *지식의 운반 / 의도의 전달 / 증거의 기록* — 은 **에이전트에게 절차를 주는 이유와 정확히 같다.** ISO 9001이 "형식을 규정하지 않는다"는 유연성이, 40년 뒤 그 문서가 기계가 읽는 형식(MCP 툴 정의, AGENTS.md)으로 바뀌는 것을 허용한다. **PART 2 오프닝의 좋은 앵글.**

### 자료: Toyota 표준작업(standardized work)과 kaizen
- 출처: https://artoflean.com/articles/standardized-work-and-kaizen/ · https://www.leanblog.org/2026/07/standardized-work-and-kaizen-toyota/ (2026-07) · https://mag.toyota.co.uk/kaizen-toyota-production-system/
- 신뢰성: **중 (2차)**
- 핵심 주장: **표준작업은 kaizen의 토대다.** 비교할 표준이 없으면 개선이 정말 개선인지 알 방법이 없기 때문이다.
- 인용 가능한 구절 (개념):
  > 표준화 → 표준 준수 → 문제 발견 → 개선 → 새 표준 수립 → 반복. **안정된 출발점(표준작업)이 없으면 kaizen은 작동하지 않는다.**
  > 표준작업과 kaizen은 **같은 활동 사이클의 두 부분**이며, 같은 사람들이 같은 표준을 통해 연결되어 수행한다.
- **책에서의 쓰임새 — 이 책 관통선의 고전적 근거:**
  - 바텀업 AI 실험은 **표준 없는 kaizen**이다. 각자 개선하지만 무엇 대비 개선인지 아무도 모른다.
  - 이 책이 SOP에서 출발하는 이유를 **1950년대 도요타의 언어로** 정당화할 수 있다: *"에이전트를 개선하려면 먼저 표준이 있어야 한다."*
  - 도요타에서 표준을 만들고 개선하는 주체가 **동일한 현장 작업자**라는 점 → 탑다운 전향이 현장을 배제하는 게 아니라는 반론 방어.
- 관련 섹션: **PART 2 오프닝 최유력 후보.** AXMM 축 D(평가·측정·개선)와도 연결된다.

## 2-2. 절차를 기계가 읽는 형태로 — SOP as code

### 자료: Amazon Science — *Structuring the Unstructured* 【★ 축 2 최고 자료】
- 출처: https://www.amazon.science/publications/structuring-the-unstructured-a-multi-agent-llm-framework-for-transforming-ambiguous-sops-into-code · PDF: https://assets.amazon.science/50/5d/7d6c576746b5be01c0274b6effdc/386-syntact-structuring-your-n.pdf · https://aclanthology.org/2025.emnlp-industry.163.pdf
- 저자·날짜: Amazon Science · **EMNLP 2025 Industry Track** (2025)
- 신뢰성: **중 (2차·검색 요약)** — **논문 본문은 paper-researcher 담당 영역과 겹침. 웹 리서치에서는 산업 적용 사례로만 기록.**
- 핵심 주장: 비정형·모호한 SOP를 **구조화된 계획 + 실행 가능한 코드 템플릿**으로 변환하는 3단계 멀티에이전트 프레임워크.
- **3모듈 구조 (이 책의 실무 절차로 그대로 번역 가능):**
  1. **Clarifier** — LLM + 사내 지식베이스(RAG) + **human-in-the-loop** 으로 SOP의 모호성을 제거
  2. **Planner** — 정제된 자연어 지시를 **함수(API) 태깅, 조건 분기, human-in-the-loop 체크포인트**를 갖춘 계층적 태스크 플로우로 변환
  3. **Implementor** — 실행 가능한 코드 조각 또는 의사코드 템플릿 생성
- 핵심 수치: **end-to-end 정확도 88.4%**, 주요 LLM 베이스라인 대비 불일치 대폭 감소. Ablation 결과 각 모듈 제거 시 성능 뚜렷하게 하락.
- 관련 자료 (같은 계열):
  - **SOP-Bench** — 실제 산업 SOP로 LLM 에이전트를 평가하는 벤치마크 (Amazon Science) https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures
  - **Agent-Ops** — 이커머스 운영의 end-to-end SOP 자동화 멀티에이전트 오케스트레이션 (Amazon Science)
  - **Agent-S** (arXiv 2503.15520) — SOP를 자동화하는 LLM 에이전틱 워크플로
- **책에서의 쓰임새:** **"사람의 절차 → 에이전트의 절차" 변환에 실제 방법론과 수치가 존재한다**는 증거. 특히 **Clarifier 단계에 사람이 반드시 들어간다**는 설계는 "SOP를 쓰는 일 자체가 조직의 암묵지를 캐내는 일"이라는 이 책의 주장과 일치한다.
- 관련 섹션: PART 2 핵심 챕터.

### 자료: Decagon — *From SOPs to Agent Operating Procedures*
- 출처: https://decagon.ai/blog/from-sops-to-agent-operating-procedures
- 발행일: **⚠️ 미확인**
- 신뢰성: **중~하** (벤더 블로그, 본문 미열람)
- 핵심 개념: **AOP(Agent Operating Procedure)** — "자연어 지시가 구조화된 로직으로 컴파일되어 에이전트가 워크플로를 안정적으로 실행하게 한다." 아키텍처는 task-specific LLM 3개 + **Global Action Repository** + 실행 메모리 + 다중 환경. SOP 워크플로를 **논리 블록 텍스트**로 작성하면 에이전트가 현재 실행 메모리에 따라 행동을 선택.
- **책에서의 쓰임새:** "AOP"라는 용어 자체가 이 책의 조어 후보. 다만 벤더 마케팅 용어이므로 **일반 개념으로 소화해 쓸 것.**

### 자료: AGENTS.md — 에이전트를 위한 README
- 출처: https://agents.md/ · https://www.harness.io/blog/the-agent-native-repo-why-agents-md-is-the-new-standard · https://infoq.com/news/2025/08/agents-md/
- 발행: **2025-08 형식화** (OpenAI · Google · Cursor · Factory · Sourcegraph 협업)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 저장소 수치(20,000 → 60,000)는 출처 간 불일치. 인용 시 재확인.**
- 핵심 주장: AGENTS.md는 **"기계를 위한 README"** 다. README가 개발자에게 최적화된 반면, AGENTS.md는 셋업 명령·테스트 워크플로·코딩 스타일·PR 가이드라인 등 **에이전트 전용 지시의 예측 가능한 위치**를 제공한다.
- 확인된 특징:
  - **스키마 없는 순수 마크다운.** 필수 구조를 강제하지 않음
  - 저장소 루트에 README.md와 나란히 배치
  - **모노레포 지원: 하위 디렉터리에 추가 배치, 트리에서 가장 가까운 파일이 우선** → 계층적 설정. OpenAI 자체 저장소는 하위 컴포넌트에 **88개**의 AGENTS.md 사용
  - Linux Foundation의 **Agentic AI Foundation**이 관리
  - 네이티브 지원: OpenAI Codex, Cursor, GitHub Copilot coding agent, Gemini CLI, Windsurf, Aider, Zed, Factory, Jules, Devin, Amp, JetBrains Junie, UiPath, Semgrep 등
- **책에서의 쓰임새 (매우 중요):** **"절차의 계층"** 이 이미 사실상의 표준으로 존재한다. 전사 규칙(루트) → 부문 규칙(하위 디렉터리) → 가장 가까운 것이 우선. **이것은 조직의 SOP 체계와 구조적으로 동형이다.** 이 책이 제안하는 "SOP 계층"에 기술적 선례를 준다.
- 관련 섹션: PART 2 — "절차를 어디에 두는가" 챕터.

### 자료: MCP Authorization — 절차를 노출하는 규약
- 출처: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization · https://www.descope.com/blog/post/mcp-auth-spec · https://stackoverflow.blog/2026/01/21/is-that-allowed-authentication-and-authorization-in-model-context-protocol/ (2026-01-21)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ spec 원문 미열람. 개정 이력·날짜는 fact-checker가 modelcontextprotocol.io에서 대조 필요.**
- 개정 이력 (2026-09-05 기준):

| 개정 | 날짜 | 내용 |
|---|---|---|
| 초기 인가 도입 | **2025-03-26** | OAuth 2.1 기반 인가 프레임워크 도입 |
| 리소스 서버 분류 | **2025-06-18** | MCP 서버를 OAuth **리소스 서버**로 분류, 클라이언트에 **Resource Indicators (RFC 8707)** 구현 요구 → 토큰이 엉뚱한 서버에 재사용되는 것 방지 |
| 대규모 개정 | **2026-07-28** | MCP 출시 이래 최대 개정. 프로토콜 코어를 **stateless 아키텍처**로 전환, 인가 동시 강화 |

- 필수 보호장치: **PKCE**, Authorization Server Metadata, Protected Resource Metadata, Resource Indicators
- 역할 분리: MCP 서버 = OAuth 2.1 **리소스 서버** / MCP 클라이언트 = OAuth 2.1 **클라이언트** / 별도 **인가 서버**가 로그인·토큰 발급 담당
- **축 1과의 연결:** Okta의 **Cross App Access가 MCP의 공식 Enterprise-Managed Authorization 확장으로 채택**되었다(2026-08-24 확인). 즉 **절차를 노출하는 규약(MCP)과 신분을 부여하는 규약(XAA/OAuth)이 2026년에 합류했다.** 이 책이 말하는 "SOP → 등록"의 기술적 실현이 실제로 일어난 시점.
- 관련 섹션: PART 2 → PART 3 전환부. **책의 관통선이 산업 표준에서 그대로 반복된다는 논증.**

## 2-3. 프로세스 마이닝 — 실제 절차를 캐내는 도구

### 자료: Celonis AgentC / Orchestration Engine / Agent Mining
- 출처: https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence (**2024-10-23**) · https://siliconangle.com/2025/11/04/celonis-feeds-ai-agents-process-intelligence-data-enhance-operational-context/ (**2025-11-04**) · https://www.celonis.com/blog/scaling-the-agentic-enterprise-with-microsoft-agent-365-and-celonis
- 신뢰성: **중 (2차·검색 요약)**
- 타임라인:
  - **2024-10-23** — AgentC 발표: Celonis Process Intelligence로 구동되는 AI 에이전트 도구·통합·파트너십 묶음. **"에이전트가 비즈니스가 어떻게 돌아가는지 이해하게 만든다"**
  - **2025-11-04** (Celosphere 2025) — **Orchestration Engine**, **Agent Mining**, 프로세스 인텔리전스용 **첫 MCP 서버** 출시. Orchestration Engine은 모든 도구·시스템·부서에 걸친 프로세스 태스크를 연결·조율하는 오케스트레이션 레이어
  - **2026-05-01** — **Microsoft Agent 365 × Celonis 프라이빗 프리뷰**. Celonis **Agent Mining**이 모든 에이전트 의사결정의 자율 추론과 로직을 분석
- **책에서의 쓰임새 (강력):** **"프로세스 마이닝이 사람의 프로세스를 캐던 도구에서, 에이전트의 프로세스를 캐는 도구가 되었다."** Agent Mining이라는 이름 자체가 이 책의 관통선(사람의 절차 → 에이전트의 절차)을 벤더가 그대로 따라간 증거다. 그리고 **에이전트의 행동이 감사 가능해진다**는 점에서 축 1(감사)과도 연결된다.
- 부가: 2025~2026년 프로세스 마이닝 도구(Celonis, Apromore, Signavio, IBM Process Mining, KYP.ai, Skan)와 에이전틱 AI가 수렴하기 시작. 프로세스 마이닝 진영은 이미 10년간 "실제 프로세스가 어떻게 돌아가는지 발견·시각화·분석"하는 도구를 만들어 왔다.
- **⚠️ SAP Signavio / UiPath Process Mining의 개별 에이전트 연계 기능 출시 현황은 미확인.**

## 2-4. 암묵지를 절차로 꺼내는 기법
- **⚠️ 이번 리서치에서 가장 얇은 부분.** task mining, work instruction 캡처, SOP 자동 생성 도구(**Scribe · Tango · Guidde**)는 **검증하지 못했다.**
- 확보한 대체 근거: Amazon Science 프레임워크의 **Clarifier 모듈** — "LLM + 사내 지식베이스(RAG) + human-in-the-loop으로 SOP를 명확화"가 사실상 암묵지 발굴 절차의 자동화된 형태다.
- 관련: f7i.ai 아티클이 SOP의 진화를 **"Static Reference" → "Active Execution"** 으로 표현 (https://f7i.ai/blog/standard-operating-procedure-sop-the-definitive-guide-to-dynamic-industrial-workflows-in-2026, 2026) — 프레이밍 용어로 쓸 만함. 신뢰성 하.

## 축 2 커버리지

**확보한 것:**
- ✅ ISO 9001 7.5의 문서화 3기능 (지식 운반 / 의도 전달 / 증거 기록)
- ✅ Toyota 표준작업 = kaizen의 전제 — 이 책 관통선의 고전적 근거
- ✅ **Amazon Science의 SOP→코드 3모듈 프레임워크 + 88.4% 수치** (Clarifier/Planner/Implementor)
- ✅ SOP-Bench, Agent-Ops, Agent-S 등 SOP 자동화 연구 계보
- ✅ AGENTS.md의 **계층적 절차 구조** (모노레포 = 조직 계층의 은유)
- ✅ MCP 인가 개정 이력 3단계 + **XAA가 MCP 공식 확장으로 채택된 사실** (SOP↔등록의 기술적 합류)
- ✅ Celonis **Agent Mining** — 프로세스 마이닝이 에이전트를 향한 사건

**비어 있는 것:**
- ❌ **암묵지 발굴 기법 (task mining, Scribe/Tango/Guidde) 미검증** — 축 2의 가장 큰 구멍
- ❌ **한국 기업 엔지니어링 블로그의 SOP→에이전트 전환 사례 없음** (우아한형제들·카카오·토스·네이버 D2·LINE 검색했으나 해당 주제 글 미발견). **대상 독자가 한국 실무자인 만큼 이 부재가 아프다.**
- ❌ BPMN, LangGraph, Temporal의 워크플로 정의 관점 미조사
- ❌ SAP Signavio · UiPath Process Mining의 에이전트 연계 현황
- ❌ OpenAPI 스펙을 에이전트 절차로 쓰는 실무 사례

---

# 축 3 — 바텀업 → 탑다운 전향

## 3-1. 상향식이 벽에 부딪히는 지점 — 실증 수치

> **저술 규율:** 이 절의 모든 수치는 **표본과 발행 연도를 함께** 써라. 특히 MIT NANDA의 "95%"는 인터넷에서 가장 많이 오용되는 수치이므로, **방법론까지 밝히지 않고 쓰면 이 책이 그 오용에 가담하는 셈이 된다.**

### 자료: MIT NANDA — *The GenAI Divide: State of AI in Business 2025* 【★ 다루되 조심할 것】
- 출처: https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf (v0.1 PDF 미러) · https://www.aigl.blog/state-of-ai-in-business-2025/ · https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html
- 저자·날짜: MIT **Project NANDA** · **2025-07** 발표 (2025-08 광범위 보도)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ MIT 공식 도메인의 원문 URL을 확보하지 못했다. 유통 중인 것은 "v0.1" 표기 PDF 미러다. 이 사실 자체가 서술 가치가 있다.**
- 핵심 주장: 기업이 300~400억 달러를 투입했음에도 **생성형 AI 프로젝트의 95%가 측정 가능한 사업 성과를 내지 못했다.**
- 인용 가능한 구절:
  > "Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with no measurable P&L impact."
- **방법론 (반드시 함께 밝힐 것):**
  - 기간: **2025년 1월~6월**
  - 공개된 AI 이니셔티브 **300건 이상**의 체계적 리뷰
  - 구조화 인터뷰 **52건**
  - **설문 응답 153건** — 4개 컨퍼런스의 시니어 리더 대상
  - → **즉 무작위 표본이 아니라 컨퍼런스 참석자 편의표본이다.** "95%"는 엄밀한 모집단 추정치가 아니다.
- 핵심 진단 (이 책과 직결):
  > 핵심 장벽은 모델 품질도, 인프라도, 규제도 아니다. **학습(learning)** 이다 — 대부분의 GenAI 시스템은 피드백을 보존하지 않고, 맥락에 적응하지 않으며, 시간이 지나도 나아지지 않는다.
  > 이 도구들은 **조직 성과가 아니라 개인 생산성**을 높인다. 기업급 커스텀 구현은 조용히 스케일에서 실패하고 있다.
- **책에서의 쓰임새 (핵심):** *"개인 생산성은 오르는데 조직 성과는 안 오른다"* — **이것이 바텀업의 정의이자 한계다.** 이 책 1장의 문제 제기를 이 한 문장으로 세울 수 있다. **단, "95%"를 단정적으로 인용하지 말고 방법론과 논란을 함께 써라.** 그것이 오히려 저자의 신뢰를 높인다.
- **⚠️ 방법론 논란 자체의 1차 근거는 미확보** — 비판 기사를 별도로 찾을 것.

### 자료: McKinsey — *The State of AI: Global Survey 2026*
- 출처: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai (**⚠️ 직접 열람 실패 — 60초 타임아웃**) · 보조: https://www.fm-magazine.com/news/2026/sep/companies-financial-value-from-ai-holds-firm-in-2026/
- 발행: **2026** (2026-08 보도, 정확일 ⚠️)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 원문 미열람. 표본 크기·필드 기간 미확인. fact-checker 재확인 필수.**
- 핵심 수치:

| 수치 | 내용 |
|---|---|
| **37%** | AI가 자사 **EBIT에 기여**했다는 응답 비율 — **전년 대비 변화 없음** |
| **약 6%** | "AI 고성과자"(EBIT의 5% 이상을 AI에 귀속 + 영향이 "significant") 비율 — **정체** |
| **27% → 40%** | **대기업** 중 하나 이상의 기능에서 **AI 에이전트를 스케일링**하는 비율 (전년 대비 상승) |
| **22%** | 소규모 조직의 동일 지표 — **정체** |
| **8/10** | 자기 개인 생산성이 향상됐다는 응답 |
| **32%** | 에이전틱 코딩 도구로 사내 구축이 가능해져 **소프트웨어 제품·기능 구매를 포기**한 조직 |

- **책에서의 쓰임새 (매우 강력):** **"대기업은 27%→40%로 뛰었는데 소규모는 22%에서 정체"** — 이것이 **탑다운의 효과를 보여주는 가장 직접적인 수치**다. 대기업이 잘해서가 아니라, **체계를 세울 수 있는 규모의 조직만 스케일링에 성공하고 있다**는 해석. 그리고 **"개인 생산성 8/10 vs EBIT 기여 37% 정체"** 는 MIT NANDA의 진단과 정확히 일치한다 — **두 독립 조사가 같은 결론에 도달했다.**
- 관련 섹션: PART 1 — 이 책 전체의 문제 제기.

### 자료: BCG — *Where's the Value in AI?*
- 출처: https://www.bcg.com/publications/2024/wheres-value-in-ai · PDF: https://web-assets.bcg.com/a5/37/be4ddf26420e95aa7107a35aae8d/bcg-wheres-the-value-in-ai.pdf · 보도자료: https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- 발행: **2024-10-24**
- 신뢰성: **중 (2차·검색 요약)** — 다만 BCG 공식 도메인 URL 확보됨
- 표본: **20개 이상 섹터, 59개국, 10개 주요 산업의 CxO·시니어 임원 1,000명**
- 핵심 수치:
  - **74%** — AI로부터 **가시적 가치를 아직 내지 못한** 기업 비율
  - **4%** — 전 기능에 걸쳐 최첨단 AI 역량을 갖추고 **일관되게 상당한 가치**를 창출하는 기업
  - **22%** — AI 전략을 실행하고 고급 역량을 구축해 **상당한 이득을 내기 시작한** 기업
  - → 성공적으로 스케일하는 기업은 **26%**
- **⚠️ 2026년판 "AI Radar" 는 확인하지 못했다.** 2024-10 수치임을 반드시 명기할 것 (2년 전 자료).

### 자료: Gartner — 에이전틱 AI 프로젝트 40% 이상 취소 예측
- 출처: https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 (**⚠️ HTTP 403 — 본문 미열람**) · 보조: https://www.hpcwire.com/bigdatawire/this-just-in/gartner-predicts-over-40-of-agentic-ai-projects-will-be-canceled-by-end-of-2027/ · https://martech.org/gartner-40-of-agentic-ai-projects-will-fail-making-humans-indispensable/
- 발행: **2025-06-25**
- 신뢰성: **중** — Gartner 원문 URL은 확보(403), 내용은 복수 매체 교차 확인
- 핵심 예측:
  > **2027년 말까지 에이전틱 AI 프로젝트의 40% 이상이 취소될 것이다** — 비용 증가, 불명확한 사업 가치, 또는 **부적절한 리스크 통제** 때문에.
- 근거 수치 (**2025년 1월 Gartner 웨비나 참석자 3,412명 폴**):
  - 19% — 에이전틱 AI에 **상당한 투자**를 했다
  - 42% — **보수적 투자**
  - 8% — **투자 없음**
  - 31% — 관망 중이거나 불확실
- 부가 (책에 매우 쓸모 있음):
  > 대부분의 에이전틱 AI 프로젝트는 **하이프에 밀린 초기 실험이나 PoC**이며 오적용되는 경우가 많다.
  > **"agent washing"** — 기존 AI 어시스턴트·RPA·챗봇을 실질적 에이전틱 역량 없이 리브랜딩하는 행태. Gartner는 **수천 개 에이전틱 AI 벤더 중 실제는 약 130개**로 추정.
- **책에서의 쓰임새:** **"부적절한 리스크 통제"가 취소 사유 3개 중 하나로 명시**되었다는 점 — 이 책 축 1(등록·감사)의 실용적 정당화. 거버넌스는 규제 준수가 아니라 **프로젝트 생존 조건**이다.

## 3-2. Shadow AI — 탑다운 필요성의 근거

- 신뢰성: **중~하** — **⚠️ 이 절의 수치 대부분이 집계 사이트를 거쳤다. 원 조사(Microsoft WorkLab, Salesforce, Cyberhaven)의 1차 URL을 확보하지 못했다. 본문 사용 시 반드시 원 조사 확인.**

| 수치 | 내용 | 출처 조사 | 연도 |
|---|---|---|---|
| **78%** | 직원이 **자기 AI를 직장에 가져온다**(BYOAI) | Microsoft WorkLab / Work Trend Index | 2025 ⚠️ |
| **55%** | 승인되지 않은 도구를 사용 | Salesforce | 2024 ⚠️ |
| **49%** | 고용주 승인 없이 AI 도구를 채택했다고 인정 (다수가 무료 버전에 민감한 기업 데이터 입력) | BlackFog 설문 | ⚠️ |
| **11%** | 직원이 AI 도구에 붙여넣는 **전체 데이터 중 민감 정보 비율** (소스코드·고객 PII·재무·법률 문서) | **Cyberhaven** | **2026** |
| **65% vs 31%** | **시니어 의사결정자** 대 그 부하직원의 미승인 AI 도구 사용률. **C레벨은 73%** | ⚠️ 조사 미상 | 2026 |
| **100%** | 직전 3개월간 AI와 함께 일했다고 답한 지식근로자 비율 | **Okta *AI Agents at Work 2026*** (n=492) | 2026 |

- 보조 출처: https://www.cyberhaven.com/infosec-essentials/shadow-ai · https://www.cio.com/article/4124760/roughly-half-of-employees-are-using-unsanctioned-ai-tools-and-enterprise-leaders-are-major-culprits.html · https://www.theregister.com/ai-ml/2026/05/27/bosses-blinded-by-confidence-about-shadow-ai-use-by-workers/5247275 (**2026-05-27**)
- **책에서의 쓰임새 (논리 구조):**
  1. shadow AI는 바텀업의 **성공 지표이자 실패 지표**다 — 사람들이 알아서 쓴다(성공), 조직이 그것을 모른다(실패).
  2. **"경영진이 부하직원보다 2배 이상 많이 미승인 도구를 쓴다"** (65% vs 31%)는 통렬하다. **탑다운을 요구할 사람들이 먼저 규칙 밖에 있다.** 이 책의 변화관리 챕터에서 리더십 정합성을 요구할 근거.
  3. The Register 표제 "Bosses blinded by confidence about shadow AI use by workers" (2026-05-27) — 리더의 인식과 현실의 격차. Okta 조사에서 **지식근로자 100%가 AI를 쓴다**는 사실과 대조.
- 관련 섹션: PART 1 — 바텀업의 초상.

## 3-3. 하향식 전환 성공/실패의 조건
- **⚠️ 이 절이 축 3의 구멍이다.** 구체 기업의 탑다운 전환 성공·실패 사례를 확보하지 못했다.
- 확보한 간접 근거:
  - **McKinsey 2026:** 대기업 27%→40% vs 소규모 22% 정체 → **규모(=체계를 세울 능력)가 갈림**
  - **Deloitte 2026-04-24:** 사용 23% vs 성숙 거버넌스 21% → **거버넌스가 병목**
  - **Gartner 2025-06-25:** 취소 사유에 "부적절한 리스크 통제" 명시
  - **Panasonic Connect (일본):** 2023-02부터 자체 AI 어시스턴트 **ConnectAI**를 **국내 전 직원 약 11,600명**에게 배포, **2024년도 업무시간 44.8만 시간 절감(전년 대비 2.4배), 직원 1인당 월 약 4시간 미만 절감** — 전사 일괄 배포(탑다운)의 사례. ⚠️ **집계 사이트발(https://japan-ai.co.jp/media/4382/), 파나소닉 1차 발표 미확인**
- **후속 필요:** 탑다운 전환의 명시적 성공·실패 케이스 스터디. community-researcher / paper-researcher와 분담 권고.

## 축 3 커버리지

**확보한 것:**
- ✅ MIT NANDA 95% + **방법론 전부** (300건 리뷰 / 52 인터뷰 / 153 설문 / 2025.1~6) → 책임 있게 인용 가능
- ✅ McKinsey 2026 — **대기업 27%→40% vs 소규모 22% 정체** (탑다운 효과의 최강 수치)
- ✅ McKinsey — 개인 생산성 8/10 vs EBIT 37% 정체 (MIT와 교차 확증)
- ✅ BCG 2024-10 — 74% / 4% / 22%, n=1,000, 59개국
- ✅ Deloitte 2026-04-24 — 23% 사용 vs 21% 성숙 거버넌스, n=3,235
- ✅ Gartner 2025-06-25 — 40%+ 취소 예측 + 폴 n=3,412 + **agent washing (수천 중 ~130개만 진짜)**
- ✅ Shadow AI 다수 수치 + **경영진이 더 많이 쓴다(65% vs 31%)**

**비어 있는 것:**
- ❌ **McKinsey 원문 미열람 (타임아웃)** — 표본·필드 기간 미확인
- ❌ **MIT NANDA 공식 원문 URL 미확보** — v0.1 미러만 유통
- ❌ **MIT 95% 방법론 비판 기사 1차 근거 미확보**
- ❌ **BCG 2026년판 "AI Radar" 미확인** — 2024년 수치만 보유 (2년 전)
- ❌ **Stanford AI Index 최신판 미조사**
- ❌ **Wharton / Accenture 조사 미조사**
- ❌ **탑다운 전환 성공/실패의 구체 기업 케이스 부재** ← 축 3의 최대 구멍
- ❌ Shadow AI 수치의 1차 조사 URL (Microsoft WorkLab, Salesforce)

---

# 축 4 — 변화관리

## 4-1. 고전 프레임의 AI 적용

### 자료: Prosci — ADKAR과 AI 도입
- 출처: https://www.prosci.com/ai-change-management · https://www.prosci.com/blog/adkar-for-ai-adoption · https://www.prosci.com/resources/webinars/navigating-ai-adoption-with-adkar
- 발행일: **⚠️ 개별 글 발행일 미확인** (Prosci 공식 도메인이므로 출처 신뢰도는 높음)
- 신뢰성: **중 (2차·검색 요약)** — **⚠️ 아래 수치들은 원문 본문 미열람. 인용 시 재확인 필수.**
- **ADKAR 5요소:** Awareness(인식) → Desire(의지) → Knowledge(지식) → Ability(능력) → Reinforcement(강화). **AI 도입이 멈추면 대개 이 중 하나가 빠져 있다.**
- 핵심 수치 (⚠️ 재확인 필요):
  - Prosci **1,107명 연구**: AI 구현 난이도의 **약 38%가 사용자 숙련도(user proficiency)**, **약 16%가 기술적 문제** → **사람 문제가 기술 문제의 2배 이상**
  - **적극적·가시적 스폰서십**이 AI 도입 성공 확률을 **최대 72%** 높인다
- 저항의 구조 (Prosci *Best Practices in Change Management* 연구):
  - **가장 저항이 큰 집단은 중간관리자**, 그 다음이 현장 직원
  - 직원 저항의 **1위 이유는 결정의 이유를 이해하지 못하는 것**, 다음이 자기 역할에서 변화를 받아들이기 주저함, 그 다음이 일자리 대체 공포
- **책에서의 쓰임새 (중요):** **"중간관리자가 가장 저항한다"** — 이 책이 다루는 탑다운 전향에서 중간관리자는 **집행 주체이자 최대 저항 세력**이다. 그리고 저항 1위 이유가 "이유를 모름"이라는 점은, 이 책이 강조하는 **"왜 등록하는가를 먼저 말하라"** 와 정확히 맞물린다.
- **⚠️ "스폰서십"이라는 단어가 축 1의 Entra sponsor와 우연히 겹친다.** 저술 시 혼동 방지를 위해 용어를 구분하라 (변화관리의 스폰서 = 임원 후원자 / 에이전트의 스폰서 = 사업 책임자). **다만 이 우연은 좋은 수사가 될 수 있다 — 둘 다 "누가 책임지는가"의 문제다.**

### 자료: Kotter 8단계와 AI
- 출처: https://itsm.tools/kotter-change-management/ · https://userguiding.com/blog/kotters-8-step-change-model
- 신뢰성: **하 (2차, 벤더/블로그)** — **⚠️ Kotter Inc. 공식 도메인의 AI 관련 자료를 찾지 못했다.**
- 8단계: 긴박감 조성 → 변화 주도 연합체 구축 → 전략적 비전·이니셔티브 수립 → 자발적 지원군 결집 → 장애물 제거로 행동 가능하게 → (단기 성과 창출 → 성과 통합·추가 변화 → 변화의 제도화)
- **저술 권고:** Kotter를 쓰려면 **Kotter 원저(*Leading Change*, 1996)** 를 직접 근거로 삼고, AI 적용은 저자의 해석으로 서술하라. 현재 확보한 2차 자료는 인용 가치가 낮다.

## 4-2. 감시로 받아들여지는가, 증폭으로 받아들여지는가

### 자료: 알고리즘 감시에 대한 직원 반응 (Cornell 연구)
- 출처: https://www.shrm.org/topics-tools/news/employee-relations/ai-surveillance-in-the-workplace-linked-to-employee-resistance-- · https://www.fm-magazine.com/issues/2025/dec/how-ai-is-changing-the-way-companies-watch-workers/ (2025-12)
- 저자·날짜: Cornell University 연구, SHRM 보도 · **⚠️ 원 논문 미확인, 발행일 미확인**
- 신뢰성: **중~하** — **⚠️ 원 논문을 반드시 추적할 것 (paper-researcher 분담 권고)**
- 핵심 주장: 직원은 어떤 형태의 감시에도 부정적으로 반응하지만, **AI에 의한 감시는 특히 더 큰 불만과 저항**을 낳는다.
- 인용 가능한 구절 (개념):
  > 알고리즘 감시는 참가자들이 **자율성이 줄었다고 인식**하게 만들고, **불평 증가·성과 저하·이직 의사**와 같은 저항 행동을 늘렸다.
- **책에서의 쓰임새 (핵심 반론 방어):** 이 책은 "에이전트를 등록하라"고 말한다. 그런데 **등록은 감시로 오해되기 가장 쉬운 조치다.** 이 연구는 그 오해의 비용이 실측 가능함을 보여준다 — 자율성 인식 저하 → 성과 저하 → 이직. **등록을 감시가 아닌 것으로 설계해야 하는 이유가 정서가 아니라 성과 문제임을 입증한다.**

### 자료: 투명성이 수용을 만든다
- 출처: https://www.pewresearch.org/internet/2023/04/20/americans-views-on-use-of-ai-to-monitor-and-evaluate-workers/ (Pew Research, **2023-04-20**) · https://www.worktime.com/blog/statistics/employee-monitoring-statistics-data · https://high5test.com/employee-monitoring-statistics/
- 신뢰성: **중~하** — **⚠️ Pew 외 수치는 집계 사이트발. 재확인 필요.**
- 핵심 수치 (⚠️ 대부분 재확인 필요):
  - **77%** — 사전에 알려주고 무엇을 수집하는지 투명하게 밝히면 모니터링에 **덜 우려하겠다**는 직원 비율
  - **90%** — 데이터 수집이 **커리어상 이익과 연결된다면** 수용하겠다는 비율
  - **22% vs 74%** — 자신이 온라인으로 모니터링당하는 줄 **아는** 직원 비율(22%) 대 실제 추적 도구를 쓰는 미국 고용주 비율(74%) → **이 격차가 반발의 뿌리**
  - **45% vs 28%** — 고감시 환경의 스트레스 응답률 대 저감시 환경
  - **56%** — 직장 감시로 스트레스·불안을 겪는다는 직원 비율
- **책에서의 쓰임새 (PART 4의 뼈대):** **갈림의 조건이 수치로 나와 있다.**
  1. **사전 고지** — 발견당하지 않게 하라 ("모르고 있다가 알게 된 직원이 훨씬 더 부정적으로 반응한다")
  2. **수집 범위의 명시** — 무엇을 보는지, 무엇을 안 보는지
  3. **당사자 이익과의 연결** — 90%가 커리어 이익과 연결되면 수용
  - 이 셋은 **에이전트 등록 커뮤니케이션 설계의 체크리스트로 그대로 전환된다.**
- **⚠️ "증폭으로 받아들여진 성공 사례"의 구체 기업 케이스는 확보 실패.** 이 책에 필요한 대칭 사례가 비어 있다.

## 4-3. HR적 파장 — 조직도, 헤드카운트, 예산

### 자료: Lattice 역풍 (축 1과 교차) 【★ PART 4 핵심 소재】
- (1-1 사례 2 참조) — **2024-07-09 발표 → 2024-07-12 철회, 3일.**
- **변화관리 관점의 독법:**
  - 기술적으로 Lattice가 하려던 일과 2026년 Microsoft/Okta가 실제로 한 일은 **거의 같다** (신분·소유자·접근권·책임자 부여).
  - 그런데 Lattice는 철회했고 MS/Okta는 GA했다. **차이는 프레이밍과 배치 장소다** — Lattice는 **HR 시스템(사람의 자리)** 에 넣었고, MS/Okta는 **IAM(계정의 자리)** 에 넣었다.
  - Lattice는 **HR 회사**였기 때문에 더 크게 다쳤다. 신뢰 자산이 걸린 영역에서 프레이밍을 잘못하면 3일 만에 접어야 한다.
- **이 책의 가장 중요한 실무 교훈이 여기 있다:** *에이전트를 조직에 등록하되, 사람의 자리에 앉히지 마라.* **PART 3의 설계 원칙이자 PART 4의 커뮤니케이션 원칙.**

### 자료: 비용 회계 — 인건비인가 IT비용인가
- 출처: 닛케이 https://www.nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ · **2026-07-09** (⚠️ 유료, 표제+리드만 확인)
- 표제: **「社員と化すAIエージェント、費用は人件費？ 人事とITの境界溶かす」**
- 신뢰성: **중 (표제·리드만)** — **⚠️ 본문 미확인. 구체 기업명·수치 없음.**
- 확인된 것: AI 에이전트 기반의 등장으로 "AI社員"이 탄생하고 있으며, **관련 비용을 인건비로 계상하는 기업이 나타나고 있다**는 것이 이 기사의 논지. 언급 도구: "OpenClaw", Anthropic "Claude Cowork".
- **책에서의 쓰임새:** "AI 예산 vs 인건비" 논쟁이 **일본에서 이미 회계 실무 이슈로 다뤄지고 있다**는 근거. 다만 본문 미확인이므로 **"닛케이가 2026년 7월 이 주제를 표제로 다뤘다"** 수준으로만 쓰고 구체 주장은 하지 말 것.

### 자료: 리스킬링 — 공개된 대규모 프로그램
- 신뢰성: **중~하 (2차·검색 요약)** — **⚠️ 아래 항목 다수가 원문 미확인. 특히 techtimes.com발 수치는 신뢰도 낮음.**

| 프로그램 | 내용 | 시점 | 신뢰성 |
|---|---|---|---|
| **RAISE US** | 초당파 비영리. **10억 달러 목표 중 5억 달러 이상 확보.** 앵커 기업 후원: **Amazon, Anthropic, Microsoft, OpenAI Foundation.** 설립: Gina Raimondo(전 상무장관), Eric Holcomb(전 인디애나 주지사) | **2026-06-25** | 중 ⚠️ |
| **Meta America's Workforce Academy (AWA)** | **1억 1,500만 달러**, 무료. 전기·광케이블 설치·용접·배관·기계 등 숙련 기능직 대상 | 2026 | 중 ⚠️ |
| EY-Parthenon 설문 | **42%의 CEO가 AI를 위한 대규모 재교육을 계획** | 2026 | 하 ⚠️ |
| 일반 설문 | 74% 조직이 AI 재교육 계획, 62%가 AI 스킬 우선, 61% 근로자가 더 많은 교육을 원함, 54%가 3년 내 직무 변화 예상 | 2026 | 하 ⚠️ |

- 출처: https://www.techtimes.com/articles/319342/20260630/ai-cuts-87714-jobs-while-its-makers-fund-1-billion-worker-retraining-push.htm (2026-06-30) 등
- **저술 권고:** 리스킬링 수치는 **집계 매체 의존도가 높다.** 본문에 쓰려면 RAISE US·Meta의 **공식 발표 페이지를 직접 확인**할 것. 특히 "AI가 87,714개 일자리를 없앴다" 같은 수치는 근거가 취약하므로 **쓰지 말 것.**

### 자료: 리더십 정합성 문제
- **65% vs 31%** — 시니어 의사결정자가 부하직원의 2배 이상으로 미승인 AI 도구를 쓴다 (3-2 참조)
- **The Register (2026-05-27):** "Bosses blinded by confidence about shadow AI use by workers"
- **책에서의 쓰임새:** 변화관리에서 **"먼저 규칙을 지켜야 할 사람이 안 지킨다"** 는 구조적 문제. 탑다운 전향의 첫 단계는 실무자 교육이 아니라 **리더의 자기 규율**이라는 논거.

## 축 4 커버리지

**확보한 것:**
- ✅ **Lattice 사례 — 축 1과 축 4를 잇는 최고의 소재.** "기술은 같고 프레이밍이 달랐다"는 논증 성립
- ✅ ADKAR 5요소 + 저항 구조 (**중간관리자가 최대 저항 집단**, 저항 1위 이유 = "이유를 모름")
- ✅ Cornell — 알고리즘 감시가 자율성 인식 저하 → 성과 저하 → 이직 의사로 이어짐
- ✅ **투명성 수치 3종** (사전 고지 77%, 커리어 연결 90%, 인지 격차 22% vs 74%) → 커뮤니케이션 설계 체크리스트로 전환 가능
- ✅ 리더십 정합성 문제 (65% vs 31%)
- ✅ 닛케이 표제 — "AI 비용은 인건비인가" 가 일본에서 실무 이슈

**비어 있는 것:**
- ❌ **"증폭으로 받아들여진" 성공 사례의 구체 기업 케이스 부재** ← 축 4의 최대 구멍. Lattice(실패)의 대칭이 없다
- ❌ **Cornell 연구 원 논문 미확인** (paper-researcher 분담 권고)
- ❌ **Kotter Inc. 공식 AI 자료 없음** — 현재 2차 자료는 인용 가치 낮음
- ❌ **TAM/UTAUT의 AI 적용 실증 연구 미조사** (paper-researcher 영역)
- ❌ Prosci 수치의 원문 검증 (38%/16%, 72%, n=1,107)
- ❌ 리스킬링 프로그램의 공식 발표 페이지
- ❌ **에이전트를 조직도에 넣는 문제 / 헤드카운트 회계**의 1차 자료 — 닛케이 유료 벽에 막힘

---

# 참고문헌 (전체 URL + 발행일 + 접근일)

> 접근일은 모두 **2026-09-05**. ★ = 직접 열람(1차 확인) / △ = 검색 요약만 / ✗ = 접근 실패

## 축 1 — 조직 등록

| # | 제목 | URL | 발행일 | 열람 |
|---|---|---|---|---|
| 1 | Deutsche Bank's Corporate Bank onboards its first digital employee for client-facing role | https://www.db.com/news/detail/20200720-deutsche-bank-s-corporate-bank-onboards-its-first-digital-employee-for-client-facing-role?language_id=1 | 2020-07-20 | ★ |
| 2 | What's new in Microsoft Entra Agent ID | https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id | 2026-05-01 (갱신 2026-08-13) | ★ |
| 3 | Administrative relationships in Microsoft Entra Agent ID (Owners, sponsors, and managers) | https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers | 2026-04-16 (갱신 2026-09-03) | ★ |
| 4 | Microsoft Agent 365 (제품 페이지) | https://www.microsoft.com/en-us/microsoft-agent-365 | 2026 | ★ |
| 5 | Microsoft Agent 365: The control plane for AI agents (M365 Blog) | https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-agent-365-the-control-plane-for-agents/ | 2025-11-18 | ✗ (404) |
| 6 | Okta brings first-class identity to AI agents with Agent SSO | https://www.okta.com/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/ | 2026-08-24 | ★ |
| 7 | Okta introduces Cross App Access to help secure AI agents in the enterprise | https://www.okta.com/newsroom/press-releases/okta-introduces-cross-app-access-to-help-secure-ai-agents-in-the/ | 2025-06-23 | △ |
| 8 | AI Agents at Work 2026: Securing the agentic enterprise (Okta) | https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/ | 2026 | △ |
| 9 | Auth0 gives developers the identity layer to securely ship agentic apps | https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/ | 2026-05 | △ |
| 10 | 1Password Launches Unified Access for AI Agent Security | https://1password.com/press/2026/mar/1password-unified-access | 2026-03 | △ |
| 11 | SailPoint redefines identity security with new adaptive identity innovations | https://investor.sailpoint.com/news-releases/news-release-details/sailpoint-redefines-identity-security-new-adaptive-identity | 2026-05-11 | △ |
| 12 | CyberArk Introduces First Identity Security Solution Purpose-Built to Protect AI Agents | https://www.cyberark.com/press/cyberark-introduces-first-identity-security-solution-purpose-built-to-protect-ai-agents-with-privilege-controls/ | 2025 (말) | △ |
| 13 | The Non-Human Identity Governance Vacuum (CSA 백서) | https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/ | 2026-05-20 | ★ |
| 14 | CSA 백서 PDF | https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/05/CSA_whitepaper_nonhuman_identity_agentic_ai_governance_v1-csa-styled.pdf | 2026-05 | ✗ (파싱 실패) |
| 15 | Agent Identity Governance Framework v1 (CSA) | https://labs.cloudsecurityalliance.org/agentic/agentic-identity-governance-framework-v1/ | 2026 | △ |
| 16 | The Lifecycle Crisis: Managing the Birth, Life, and Death of AI Agents (Dark Reading) | https://www.darkreading.com/identity-access-management-security/the-lifecycle-crisis-managing-the-birth-life-and-death-of-ai-agents | ⚠️ 미확인 | △ |
| 17 | AI agent offboarding: what happens when the worker never leaves? | https://nhimg.org/community/nhi-best-practices/ai-agent-offboarding-what-happens-when-the-worker-never-leaves/ | ⚠️ 미확인 | △ |
| 18 | Machine Identities Outnumber Humans by More Than 80 to 1 (CyberArk) | https://www.cyberark.com/press/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security/ | 2025-04 | △ |
| 19 | 2026 Identity Security Landscape (Palo Alto Networks) | https://www.paloaltonetworks.com/idira/idira-identity-security-landscape | 2026 | △ |
| 20 | Agentic AI is scaling faster than guardrails (Deloitte Insights) | https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html | 2026-04-24 | ★ |
| 21 | Lattice scraps plans to treat AI bots as employees (SHRM) | https://www.shrm.org/topics-tools/news/technology/lattice-scraps-plans-to-treat-ai-bots-as-employees-after-backlash | 2024-07 | △ |
| 22 | Never Mind! HR Company Lattice... (Inc.) | https://www.inc.com/ben-sherry/nevermind-hr-company-lattice-decided-to-bring-ais-into-org-chart-then-changed-its-mind.html | 2024-07 | △ |
| 23 | Lattice / AI workers (Fortune) | https://fortune.com/2024/07/12/lattice-ai-workers-sam-altman-brother-jack-sarah-franklin | 2024-07-12 | △ |
| 24 | Goldman Sachs is piloting its first autonomous coder (CNBC) | https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html | 2025-07-11 | ✗ (403) |
| 25 | How Goldman Sachs Is Using Agentic AI For Software Engineering At Scale (Forbes) | https://www.forbes.com/sites/bernardmarr/2026/08/06/how-goldman-sachs-is-using-agentic-ai-for-software-engineering-at-scale/ | 2026-08-06 | △ |
| 26 | Deploying Microsoft Agent 365 (Inside Track) | https://www.microsoft.com/insidetrack/blog/deploying-microsoft-agent-365-how-were-extending-our-infrastructure-to-manage-agents-at-microsoft/ | 2026 | △ |
| 27 | 社員と化すAIエージェント、費用は人件費？(日本経済新聞) | https://www.nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ | 2026-07-09 | ✗ (유료) |

## 축 1 — 제도·규제

| # | 제목 | URL | 발행일 | 열람 |
|---|---|---|---|---|
| 28 | EU AI Act Article 49: Registration | https://artificialintelligenceact.eu/article/49/ | Reg. (EU) 2024/1689 | ★ |
| 29 | EU AI Act Annex VIII | https://artificialintelligenceact.eu/annex/8/ | Reg. (EU) 2024/1689 | △ |
| 30 | Article 71: EU database for high-risk AI systems (EC AI Act Service Desk) | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-71 | — | △ |
| 31 | EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines (Gibson Dunn) | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ | 2026-05-27 | ★ |
| 32 | EU agrees to delay key AI Act compliance deadlines (Travers Smith) | https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/ | 2026 | △ |
| 33 | The EU AI Act's August 2, 2026 Deadline Just Moved (ComplianceHub) | https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/ | 2026 | △ |
| 34 | NIST AI RMF to ISO/IEC 42001 Crosswalk (NIST AIRC) | https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf | — | △ |
| 35 | NIST AI RMF Subcategories Explorer | https://techjacksolutions.com/framework-explorer/nist-ai-rmf/ | 2026 | △ |
| 36 | The Roles and Responsibilities in ISO 42001 Explained (Schellman) | https://www.schellman.com/blog/ai-governance/iso-42001-roles-and-responsibilities | ⚠️ 미확인 | △ |
| 37 | ISO 42001 Controls Explained: Annex A (Hicomply) | https://www.hicomply.com/hub/annex-a-controls | ⚠️ 미확인 | △ |
| 38 | AI 기본법 시행과 그 시사점 (신&김) | https://www.shinkim.com/kor/media/newsletter/3114 | 2026 | △ |
| 39 | AI 기본법 시행과 그 시사점 (법률신문/세종) | https://www.lawtimes.co.kr/news/articleView.html?idxno=216500 | 2026 | △ |
| 40 | AI기본법 시행 6개월 — 계도기간이 끝나기 전에 | https://datalaw.kr/posts/ai-basic-law-business-duties/ | 2026 | △ |
| 41 | 생성형 AI 개발·활용을 위한 개인정보 처리 안내서 (개인정보위) | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11410 | 2025-08-06 | △ |
| 42 | 개인정보위, 생성형 AI 이용자 위한 개인정보 보호 가이드 발간 (바이라인) | https://byline.network/2026/05/19-618/ | 2026-05-19 | △ |
| 43 | 2026년 개인정보보호위원회 업무 추진계획 (김·장) | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=33715 | 2026 | △ |
| 44 | OMB M-25-21 (원문 PDF 미러) | https://static.carahsoft.com/concrete/files/9717/4412/5797/Guidance_M-25-21_Accelerating_Federal_Use_of_AI_through_Innovation_Governance_and_Public_Trust.pdf | 2025-04-03 | △ |
| 45 | Trump Administration Revamps Guidance on Federal Use and Procurement of AI (Wiley) | https://www.wiley.law/alert-Trump-Administration-Revamps-Guidance-on-Federal-Use-and-Procurement-of-AI | 2025 | △ |
| 46 | DOJ AI Inventory (실제 인벤토리 예시) | https://www.justice.gov/ai/ai-inventory | — | △ |
| 47 | 346 generative AI services filed with CAC (中国国务院新闻办) | http://english.scio.gov.cn/pressroom/2025-04/09/content_117814020.html | 2025-04-09 | △ |
| 48 | What is China's AI Algorithm Filing? (AppInChina) | https://appinchina.co/what-is-chinas-ai-algorithm-filing/ | 2026 | △ |
| 49 | China's Algorithm Filing Regime (Lexology) | https://www.lexology.com/library/detail.aspx?g=3c7273cf-8f85-4702-af70-6edf394ff1c3 | ⚠️ 미확인 | △ |

## 축 2 — SOP

| # | 제목 | URL | 발행일 | 열람 |
|---|---|---|---|---|
| 50 | ISO 9001, Clause 7.5, Documented Information (ISMS.online) | https://www.isms.online/iso-9001/clause-7-5-documented-information/ | ⚠️ 미확인 | △ |
| 51 | Standardized Work and Kaizen: No Improvement Without a Baseline (Art of Lean) | https://artoflean.com/articles/standardized-work-and-kaizen/ | ⚠️ 미확인 | △ |
| 52 | Toyota's 1992 View: Standardized Work and Kaizen (Lean Blog) | https://www.leanblog.org/2026/07/standardized-work-and-kaizen-toyota/ | 2026-07 | △ |
| 53 | What is kaizen and how does Toyota use it? (Toyota UK) | https://mag.toyota.co.uk/kaizen-toyota-production-system/ | ⚠️ 미확인 | △ |
| 54 | Structuring the unstructured: A multi-agent LLM framework for transforming ambiguous SOPs into code (Amazon Science) | https://www.amazon.science/publications/structuring-the-unstructured-a-multi-agent-llm-framework-for-transforming-ambiguous-sops-into-code | EMNLP 2025 | △ |
| 55 | 위 논문 PDF (ACL Anthology) | https://aclanthology.org/2025.emnlp-industry.163.pdf | 2025 | △ |
| 56 | SOP-Bench: A new benchmark for evaluating AI agents on real business procedures (Amazon Science) | https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures | 2025 | △ |
| 57 | Agent-Ops: multi-agent orchestration for end-to-end SOP automation (Amazon Science) | https://www.amazon.science/publications/agent-ops-a-multi-agent-orchestration-framework-for-end-to-end-sop-automation-in-e-commerce-operations | — | △ |
| 58 | Agent-S: LLM Agentic workflow to automate Standard Operating Procedures (arXiv 2503.15520) | https://arxiv.org/abs/2503.15520 | 2025-03 | △ |
| 59 | From SOPs to Agent Operating Procedures (Decagon) | https://decagon.ai/blog/from-sops-to-agent-operating-procedures | ⚠️ 미확인 | △ |
| 60 | AGENTS.md (공식) | https://agents.md/ | 2025-08~ | △ |
| 61 | The Agent-Native Repo: Why AGENTS.MD is the New Standard (Harness) | https://www.harness.io/blog/the-agent-native-repo-why-agents-md-is-the-new-standard | 2026 | △ |
| 62 | AGENTS.md (InfoQ) | https://infoq.com/news/2025/08/agents-md/ | 2025-08 | △ |
| 63 | MCP Authorization (공식 스펙, 2025-11-25판) | https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization | 2025-11-25 | △ |
| 64 | Diving Into the MCP Authorization Specification (Descope) | https://www.descope.com/blog/post/mcp-auth-spec | ⚠️ 미확인 | △ |
| 65 | Is that allowed? Authentication and authorization in MCP (Stack Overflow Blog) | https://stackoverflow.blog/2026/01/21/is-that-allowed-authentication-and-authorization-in-model-context-protocol/ | 2026-01-21 | △ |
| 66 | MCP Specification Version Timeline | https://hidekazu-konishi.com/entry/mcp_specification_version_timeline.html | 2026 | △ |
| 67 | Linux Foundation Launches the Agent2Agent Protocol Project | https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents | 2025-06-23 | △ |
| 68 | Agent2Agent (Wikipedia) | https://en.wikipedia.org/wiki/Agent2Agent | — | △ |
| 69 | Celonis AgentC: Making AI Agents Work for the Enterprise with Process Intelligence | https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence | 2024-10-23 | △ |
| 70 | Celonis feeds AI agents with process intelligence data (SiliconANGLE) | https://siliconangle.com/2025/11/04/celonis-feeds-ai-agents-process-intelligence-data-enhance-operational-context/ | 2025-11-04 | △ |
| 71 | Scaling the agentic enterprise with Celonis on Microsoft Agent 365 | https://www.celonis.com/blog/scaling-the-agentic-enterprise-with-microsoft-agent-365-and-celonis | 2026-05 | △ |
| 72 | How Kagenti ADK simplifies production AI agent management (Red Hat Developer) | https://developers.redhat.com/articles/2026/05/04/how-kagenti-adk-simplifies-production-ai-agent-management | 2026-05-04 | △ |

## 축 3 — 바텀업→탑다운

| # | 제목 | URL | 발행일 | 열람 |
|---|---|---|---|---|
| 73 | The GenAI Divide: State of AI in Business 2025 (MIT NANDA, v0.1 미러) | https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf | 2025-07 | △ |
| 74 | State of AI in Business 2025 (해설) | https://www.aigl.blog/state-of-ai-in-business-2025/ | 2025 | △ |
| 75 | MIT report: 95% of generative AI pilots at companies are failing (Yahoo/Fortune) | https://finance.yahoo.com/news/mit-report-95-generative-ai-105412686.html | 2025-08 | △ |
| 76 | The State of AI: Global Survey 2026 (McKinsey) | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026 | ✗ (타임아웃) |
| 77 | Companies' financial value from AI holds firm in 2026 (FM Magazine) | https://www.fm-magazine.com/news/2026/sep/companies-financial-value-from-ai-holds-firm-in-2026/ | 2026-09 | △ |
| 78 | Where's the Value in AI? (BCG) | https://www.bcg.com/publications/2024/wheres-value-in-ai | 2024-10 | △ |
| 79 | Where's the Value in AI? (BCG PDF) | https://web-assets.bcg.com/a5/37/be4ddf26420e95aa7107a35aae8d/bcg-wheres-the-value-in-ai.pdf | 2024-10 | △ |
| 80 | AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value (BCG 보도자료) | https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value | 2024-10-24 | △ |
| 81 | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 | ✗ (403) |
| 82 | 위 보도자료 재게재 (BigDATAwire) | https://www.hpcwire.com/bigdatawire/this-just-in/gartner-predicts-over-40-of-agentic-ai-projects-will-be-canceled-by-end-of-2027/ | 2025-06 | △ |
| 83 | Gartner: 40% of agentic AI projects will fail (MarTech) | https://martech.org/gartner-40-of-agentic-ai-projects-will-fail-making-humans-indispensable/ | 2025 | △ |
| 84 | What Is Shadow AI? Risks, Detection, and Prevention (Cyberhaven) | https://www.cyberhaven.com/infosec-essentials/shadow-ai | 2026 | △ |
| 85 | Roughly half of employees are using unsanctioned AI tools (CIO) | https://www.cio.com/article/4124760/roughly-half-of-employees-are-using-unsanctioned-ai-tools-and-enterprise-leaders-are-major-culprits.html | 2026 | △ |
| 86 | Bosses blinded by confidence about shadow AI use by workers (The Register) | https://www.theregister.com/ai-ml/2026/05/27/bosses-blinded-by-confidence-about-shadow-ai-use-by-workers/5247275 | 2026-05-27 | △ |
| 87 | The State of Shadow AI (UpGuard) | https://www.upguard.com/resources/the-state-of-shadow-ai | 2026 | △ |
| 88 | 【2026年最新版】AI導入事例12選 (EQUES, Panasonic Connect 사례 포함) | https://eques.co.jp/column/ai-case-studies/ | 2026 | △ |

## 축 4 — 변화관리

| # | 제목 | URL | 발행일 | 열람 |
|---|---|---|---|---|
| 89 | AI Adoption: Driving Change With a People-First Approach (Prosci) | https://www.prosci.com/ai-change-management | ⚠️ 미확인 | △ |
| 90 | Why Your AI Rollout Stalled And What You Can Do About It (Prosci, ADKAR for AI) | https://www.prosci.com/blog/adkar-for-ai-adoption | ⚠️ 미확인 | △ |
| 91 | Navigating AI Adoption With ADKAR (Prosci 웨비나) | https://www.prosci.com/resources/webinars/navigating-ai-adoption-with-adkar | ⚠️ 미확인 | △ |
| 92 | Use the ADKAR Model for Change Success (Prosci) | https://www.prosci.com/blog/adkar-model | ⚠️ 미확인 | △ |
| 93 | AI Surveillance in the Workplace Linked to Employee Resistance, Turnover (SHRM) | https://www.shrm.org/topics-tools/news/employee-relations/ai-surveillance-in-the-workplace-linked-to-employee-resistance-- | ⚠️ 미확인 | △ |
| 94 | Americans' views on use of AI to monitor and evaluate workers (Pew Research) | https://www.pewresearch.org/internet/2023/04/20/americans-views-on-use-of-ai-to-monitor-and-evaluate-workers/ | 2023-04-20 | △ |
| 95 | How AI is changing the way companies watch workers (FM Magazine) | https://www.fm-magazine.com/issues/2025/dec/how-ai-is-changing-the-way-companies-watch-workers/ | 2025-12 | △ |
| 96 | 50+ employee monitoring stats every manager should know (2026) | https://www.worktime.com/blog/statistics/employee-monitoring-statistics-data | 2026 | △ |
| 97 | Kotter Change Management: How to Apply the 8 Steps Successfully | https://itsm.tools/kotter-change-management/ | ⚠️ 미확인 | △ |
| 98 | AI Cuts 87,714 Jobs While Its Makers Fund $1 Billion Worker Retraining Push (TechTimes) | https://www.techtimes.com/articles/319342/20260630/ai-cuts-87714-jobs-while-its-makers-fund-1-billion-worker-retraining-push.htm | 2026-06-30 | △ |
| 99 | AI Workforce Retraining Fund Hits $500M (TechTimes) | https://www.techtimes.com/articles/319395/20260630/ai-workforce-retraining-fund-hits-500m-companies-cutting-jobs-are-paying-fix.htm | 2026-06-30 | △ |

---

# ⚠️ 미확인·주의 항목 (모아보기)

> **Phase 4 fact-checker 최우선 처리 대상.** 아래 항목은 본문에 등장하면 반드시 검증하고, 검증 불가 시 삭제하거나 표현을 완화해야 한다.

## A. 절대 지어내면 안 되는 것 (BLOCKING)

| # | 항목 | 상태 | 조치 |
|---|---|---|---|
| A-1 | **한국 은행권 RPA 로봇 사번 부여** | **⚠️ 미확인 — 공개 출처로 확인 실패** | **본문에 쓰지 마라.** 국내 은행 RPA 도입 자체는 확인되나(KB국민·우리·NH농협·신한·IBK기업·부산은행) 사번 부여는 근거 없음 |
| A-2 | **Goldman Sachs가 Devin에게 사번을 줬다** | **⚠️ 근거 없음** — "employee #1"은 매체 수사 | "사번"으로 서술 금지. "hybrid workforce에 배치된 파일럿"으로만 |
| A-3 | **Deutsche Bank Blue Bot 'Yi'의 2026년 현재 존속 여부** | ⚠️ 미확인 | "2020년 발표 시점 기준"으로 못 박을 것 |
| A-4 | **ISO/IEC 42001 Annex A 개별 통제 번호(A.x.y)** | ⚠️ 미확인 (표준 유료) | 번호 인용 금지. 구조(38통제/9목적)만 서술 |
| A-5 | **NIST AI RMF GOVERN 1.6의 정확한 문구** | ⚠️ **출처 간 충돌** | NIST 원문·Playbook 직접 대조 필수 |
| A-6 | **한국 AI 기본법 조문 번호** | ⚠️ 미확인 | 국가법령정보센터 원문 대조 필수 |
| A-7 | **Lattice CEO Sarah Franklin의 LinkedIn 원문 인용구** | ⚠️ 2차 매체 경유 | 직접 인용 시 원 게시글 확인, 불가 시 간접화법으로 |

## B. 신선도 경보 (2026-09-05 기준 — 빠르게 바뀜)

| # | 항목 | 주의 |
|---|---|---|
| B-1 | **EU AI Act 고위험 시행일** | **2026-08-02 → 2027-12-02 로 연기됨.** 구버전 정보 다수 유통 중. 반드시 "2026년 9월 기준"으로 못 박을 것 |
| B-2 | **Regulation (EU) 2026/1744 규정 번호·관보일(2026-07-24)·발효일(2026-07-27)** | ⚠️ 2차 출처만. **EUR-Lex 원문 대조 필수** |
| B-3 | **Digital Omnibus가 Art. 49 등록 의무를 어떻게 바꿨는지** | ⚠️ 미확인 |
| B-4 | **SailPoint Agentic Fabric의 현재 GA 여부** | 2026-05-11 발표 시 "2026 여름 GA 예정" → 현재 상태 재확인 |
| B-5 | **MCP 스펙 개정 이력·날짜** | ⚠️ spec 원문 미열람. 2026-07-28 개정 내용 재확인 |
| B-6 | **AGENTS.md 채택 저장소 수** | ⚠️ 20,000 vs 60,000 출처 간 불일치. 수치 인용 지양 |
| B-7 | **Microsoft Agent 365 GA일(2026-05-01)·가격($15/user/월)** | 제품 페이지는 "GA"만 확인. GA 날짜는 2차 |
| B-8 | **한국 AI 기본법 계도기간 종료 시점** | "최소 1년 이상" 만 확인. 정확한 종료일 미확인 |

## C. 수치 재확인 필요 (원 조사 URL 미확보)

| # | 수치 | 출처 | 조치 |
|---|---|---|---|
| C-1 | McKinsey 2026 전 수치 (37% EBIT, 27→40%, 6%, 32%) | 원문 타임아웃 | **표본·필드 기간 포함 재확인** |
| C-2 | MIT NANDA "95%" | 공식 원문 URL 미확보(v0.1 미러만) | 인용 시 **방법론 병기 필수** |
| C-3 | Prosci 38%/16%, n=1,107, 스폰서십 +72% | 원문 미열람 | 재확인 |
| C-4 | Shadow AI 78%(MS WorkLab), 55%(Salesforce), 65% vs 31% | 집계 사이트 경유 | **원 조사 URL 확보 필수** |
| C-5 | 직원 모니터링 77%/90%/22% vs 74%/45% vs 28%/56% | 집계 사이트 경유 | 재확인 (Pew 2023만 1차) |
| C-6 | "API 키 오프보딩 공식 프로세스 20%" | 출처 불명 | 재확인 또는 삭제 |
| C-7 | Cornell 알고리즘 감시 연구 | 원 논문 미확인 | **paper-researcher에 이관 권고** |
| C-8 | NHI 대 인간 비율 (45:1 / 82:1 / 109:1 / 144:1) | 기관마다 상이 | **단일 수치 단정 금지 — "45:1~144:1로 갈린다"로** |
| C-9 | 리스킬링 수치 (RAISE US $500M, Meta $115M, EY 42%) | TechTimes 등 집계 매체 | **공식 발표 페이지 확인 후 사용** |
| C-10 | "AI가 87,714개 일자리 삭감" | 근거 취약 | **쓰지 말 것** |
| C-11 | Panasonic Connect 11,600명 / 44.8만 시간 | 일본 집계 사이트 | 파나소닉 1차 발표 확인 필요 |
| C-12 | CyberArk "머신 아이덴티티 42%가 특권 접근" / "88%가 특권 사용자를 인간에게만 적용" | 검색 요약 | 재확인 |

## D. 접근 실패 로그

| URL | 사유 |
|---|---|
| https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html | HTTP 403 |
| https://www.gartner.com/en/newsroom/press-releases/2025-06-25-... | HTTP 403 |
| https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/18/microsoft-agent-365-the-control-plane-for-agents/ | HTTP 404 (URL 변경 추정) |
| https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 60초 타임아웃 |
| https://www.nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ | 유료 구간 (표제·리드만 확보) |
| CSA 백서 PDF (2.2MB) | PDF 바이너리 파싱 실패 (랜딩 페이지로 대체 확보) |

## E. 의도적으로 제외한 소스 유형

- **논문·학술 자료** — paper-researcher 담당 (arXiv 2510.25819 "Identity Management for Agentic AI", arXiv 2604.23280 "AI Identity: Standards, Gaps, and Research Directions for AI Agents", arXiv 2604.04604 "AI Agents Under EU Law" 등을 검색 중 발견했으나 수집하지 않음 — **research-lead에게: 이 3편은 축 1에 직접 관련되므로 paper-researcher에 전달 권고**)
- **커뮤니티(Reddit·HN·OKKY 등)** — community-researcher 담당
- **날짜 없는 SEO 나열형 아티클** — 다수 검색 결과에서 제외
- **벤더 마케팅 랜딩 페이지** — 제품 상태(GA/프리뷰) 확인 목적 외에는 배제

---

# research-lead에게 남기는 메모

**이 리서치의 결론 세 줄:**

1. **축 1은 성립한다 — 다만 예상과 다른 형태로.** "AI에게 사번을 준 기업 목록"은 짧다(사실상 Deutsche Bank 1건). 그러나 **Microsoft Entra의 Owner/Sponsor/Manager 모델**과 **CSA의 "78%가 폐기 정책 없음"** 이 훨씬 강한 재료다. 책의 앵글을 **"누가 이미 했나"에서 "어떻게 설계하는가 + 왜 아무도 못 하고 있나"** 로 잡으면 압도적으로 강해진다.

2. **Lattice(2024) → Entra Agent ID(2026)의 2년 간극이 이 책의 서사다.** 같은 아이디어가 HR 시스템에서는 3일 만에 죽고 IAM에서는 GA가 됐다. **PART 3(설계)과 PART 4(변화관리)를 하나의 이야기로 묶는 축이 여기 있다.**

3. **한국 사례가 완전히 비어 있다.** 대상 독자가 한국 AX 실무 리더인데 축 1·2·4 모두 한국 사례 0건이다. 제도(AI 기본법, 개인정보위)만 확보됐다. **community-researcher에게 국내 실무자 목소리를, 그리고 별도 심층 조사로 국내 금융·통신권 RPA/에이전트 거버넌스 사례를 요청할 것을 강력 권고한다.**

**보안 규약 준수 확인:** 본 문서의 모든 자료는 공개 웹 출처다. 사내 정보·비공개 기업 정보·실명 인물의 사적 정보는 수집하지 않았다.
