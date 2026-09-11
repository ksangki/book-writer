# AX 체계 구축 레퍼런스

> Phase 1 산출물. `00_direction.md`의 리서치 우선순위 4축을 따라 웹·논문·커뮤니티 3개 리서치를 통합했다.
> **검색 시점: 2026-09-05 기준.** 원자료는 `research/web.md`·`research/papers.md`·`research/community.md`에 보존한다 (Phase 4 fact-checker의 1차 대조 근거 — 삭제 금지).

## 이 문서를 읽는 법

| 표기 | 의미 |
|---|---|
| `[웹]` `[논문]` `[커뮤]` | 출처 리서처 |
| **★** | 1차 원문 직접 열람 — 그대로 인용 가능 |
| **△** | 검색 요약만 확인 — 본문 사용 시 `(사실 확인 필요)` 마커 부착 |
| **⚠️** | 미확인·수치 귀속 불명 — 확인 전 사용 금지 |
| **🕒** | 신선도 민감 — 인용 시 반드시 시점 명시 |
| `[PR]` `[PP]` | 피어리뷰 게재 / 프리프린트 단독(미검증) |

**저술가에게 세 줄:**
1. **축 1의 앵글을 바꿔라.** "AI에게 사번을 준 기업 목록"은 URL로 검증하면 **사실상 1건**(Deutsche Bank, 2020)이다. 그러나 그 자리를 훨씬 강한 재료가 대체한다 — **Microsoft Entra의 Owner/Sponsor/Manager 3역할 설계(공식 문서 ★)** 와 **"78%가 AI 아이덴티티 폐기 정책이 없다"(CSA)**. 책의 질문을 *"누가 이미 했나"* 에서 **"어떻게 설계하는가 + 왜 아무도 못 하고 있나"** 로 옮기면 압도적으로 강해진다.
2. **Lattice(2024) → Entra Agent ID(2026)의 2년 간극이 이 책의 서사다.** 같은 아이디어가 HR 시스템에서는 3일 만에 죽고 IAM에서는 GA가 됐다. PART 3(설계)과 PART 4(변화관리)를 하나로 묶는 축이 여기 있다.
3. **한국 사례가 0건이다.** 축 1·2·4 모두 국내 기업 사례를 확보하지 못했다. 제도(AI 기본법)와 한국어 커뮤니티 인용 3건만 있다. 이 공백을 Phase 2 planner가 알고 설계해야 한다.

> **⚠️ planner·저술가 필독 — §9를 먼저 보라 (2차 보강, 2026-09-06 완료).**
> 이 문서는 **2라운드로 만들어졌다.** §1~§8은 1차, **§9는 2차 보강**이다. **충돌하는 곳은 §9가 우선한다.**
>
> **§9에서 반드시 먼저 볼 것:**
> - **§9-0 논지 조정 3건** — ① 폐기: "아무도 설계 안 한다" → **"이미 설계돼 있다. 켜져 있지 않을 뿐이다"** ② **BNY는 사번이 아니라 사용자 ID다** ③ 축 3의 실증 뼈대(DORA "AI는 증폭기")
> - **§9-1 축 1 자가 판정표** — 수락 기준 6항목 대조 (4개 충족 / 2개 조건부)
> - **§9-3 자율성 등급** — 1차에서 0건이던 항목. **실무 4종 + 학술 9종 + 1978년 계보** 확보. **PART 3의 중심 장치 후보**
> - **§9-5 축 5(FTE·성과관리)** — 신설 축 전체
> - **§9-7 추가 반론 J~S** — 저술 시 응답 필요
> - **§9-9 사용 금지 목록** / **§9-10 편향 자각**
> - **★ §10 저술 규율 원장** — **Phase 4 fact-checker의 1차 대조 근거.** direction-only 수치, Vaccaro 기준선 비대칭, 판본이 다른 수치, 정정·금지 항목이 전부 여기 있다. **§7-4·§9-9와 충돌하면 §10이 우선한다.**

---

# 1. 개념과 정의

## 1-1. 등록(registration) — 이 책의 중심어

세 리서치가 독립적으로 같은 3종 세트에 도달했다. 이것이 이 책의 "사번·계정·소유자·매니저"가 임의 발명이 아니라는 증거다.

| 층위 | 구성요소 | 근거 |
|---|---|---|
| **학술** | agent identifiers / real-time monitoring / activity logging | Chan et al. (2024) 「Visibility into AI Agents」 `[PR]` FAccT '24 `[논문]` ★ |
| **제품** | Owner(기술 관리) / Sponsor(사업 책임) / Manager(조직 계층) | Microsoft Entra Agent ID 공식 문서 (ms.date 2026-04-16) `[웹]` ★ |
| **제도** | 등록번호 / 지정 책임자 / 감사 기록 | EU AI Act Art. 49, NIST AI RMF의 "named risk acceptance", 중국 알고리즘 등록제의 "designated responsible personnel" `[웹]` |

**가시성(visibility)의 정의** — Chan et al.의 원문 그대로: 어떤 에이전트가 "**where, why, how, and by whom**" 쓰이는가에 대한 정보. 한국어로는 **"어디서·왜·어떻게·누구에 의해"**. `[논문]` ★

**agent ID의 정의** — Chan et al. (2025) 「Infrastructure for AI Agents」 `[PR]` TMLR: 최소한 에이전트 인스턴스에 대한 고유 식별자, 그리고 잠재적으로 시스템 카드나 인증 같은 **부가 정보를 매다는 컨테이너**. 즉 **사번은 숫자 하나가 아니라 소유자·권한·인증 이력을 매다는 고리**다. `[논문]` ★

> **비기술 임원 설득용 비유 (원문 그대로 인용 가능):** ID 유사 체계는 이미 여러 영역에 있다 — "**serial numbers on consumer products, tail numbers on aircraft, and registration numbers for businesses**"(소비재의 일련번호, 항공기의 기체등록번호, 사업자등록번호). 리스크·사고 관리를 가능하게 하기 위해서다. — Chan et al. (2025), arXiv:2501.10114v3 `[논문]` ★

## 1-2. 비인간 아이덴티티(NHI) — 그리고 그 용어에 대한 냉소

**정의 축:** 서비스 계정·API 키·토큰·인증서·머신 아이덴티티를 총칭. 에이전트 아이덴티티는 그 부분집합이자, 성격이 다른 부분집합이다 — **런타임에 동적으로 권한을 획득하고, 하위 에이전트를 생성하며, 외부 API를 호출하고, 코드를 작성·실행하고, 수십 개 시스템에 걸쳐 행동을 연쇄시킨다.** 자격증명 하나가 뚫렸을 때의 폭발 반경이 정적 서비스 계정과 차원이 다르다. (CSA, 2026-05-20) `[웹]`

**⚠️ 그러나 이 정의는 현장에서 즉시 반박당한다 — 이 책의 첫 장이 반드시 받아야 할 반응:**

> **"Wtf? We have been calling these workload identities for years"**
> ("뭐야? 우리 이거 몇 년째 workload identity라고 불러왔는데.")
> — `zingababba`, Hacker News, **2025-02-04**, https://news.ycombinator.com/item?id=42928645 `[커뮤]` ★

같은 스레드에서 `xg15`는 **"service accounts are not bots"**, `xarope`는 OWASP가 결국 나열하는 게 "service accounts and access keys… API keys, tokens, encryption keys, and certificates"뿐이라며 **리브랜딩 아니냐**고 지적했다. `[커뮤]`

## 1-3. 폐기(revocation) ≠ 디프로비저닝(deprovisioning)

실무 설계에서 가장 중요한 구분인데 거의 안 다뤄진다. `[웹]` △

- **revocation(취소):** 활성 세션의 즉시 종료.
- **deprovisioning(디프로비저닝):** 아이덴티티와 부여된 권한의 **영구적·완전한 제거**.
- → **취소만 된 에이전트는 등록과 신뢰 관계를 그대로 보유할 수 있다.**

파생 용어:
- **zombie agent / orphaned agent** — 상시 접근 권한은 있는데 끌 스위치가 없는 고아 NHI. 감시받지 않으므로 공격자가 발견하면 그 권한을 그대로 상속한다.
- **shadow agent** — 보안 승인 없이 직원이 만든 AI 자동화·서비스 계정·API 토큰.

**제안된 정상 오프보딩 절차:** ① 중앙 IdP에서 에이전트 코어 아이덴티티 종료 → ② IdP가 모든 연합 도메인에 디프로비저닝 시그널 브로드캐스트 → ③ 모든 ACL에서 식별자 제거(고아 권한 방지) `[웹]` △

## 1-4. SOP·루틴 — "적힌 절차"와 "실제로 하는 일"

**이 책의 이론적 기둥.** Feldman & Pentland (2003), ASQ 48(1), 94–118 `[PR]` `[논문]` ★

| 측면 | 정의 | 이 책의 번역 |
|---|---|---|
| **ostensive** | "what we typically think of as **the structure**" — 적힌 절차, 머릿속의 루틴 관념 | **적힌 절차** = SOP 문서 |
| **performative** | "**the specific actions, by specific people, at specific times and places**, that bring the routine to life" | **실제로 하는 일** = 로그에 남는 것 |

원문 인용 가능: "The ostensive aspect enables people to **guide, account for, and refer to** specific performances of a routine, and the performative aspect **creates, maintains, and modifies** the ostensive aspect."

**실무 함의 두 갈래:**
- (a) SOP를 그대로 에이전트에 넣으면 **실제로 일이 되는 방식이 아니라 일이 된다고 적힌 방식**을 자동화하게 된다.
- (b) 반대로 이 간극은 **자원**이다 — performative가 ostensive를 갱신하는 경로가 있어야 SOP가 살아 있는 문서가 된다. 에이전트 실행 로그가 그 갱신 경로가 될 수 있다.

**측정 도구:** 프로세스 마이닝의 **conformance checking**이 정확히 ostensive와 performative를 기계적으로 대조하는 절차다. van der Aalst의 3축 — **discovery**(로그에서 실제 프로세스 발견) / **conformance**(적힌 모델과 실제 로그 대조) / **enhancement**(실제 데이터로 모델 개선). `[논문]`

> **저술 제안:** 어려운 용어를 그대로 던지지 말고 — **"적힌 절차"와 "실제로 하는 일"** 로 먼저 말하고, "학계에서는 이걸 ostensive와 performative라고 부른다"로 받는다. 요약하면 **"지도를 그리기 전에 발자국을 봐라."**

## 1-5. 형식화의 두 유형 — enabling vs coercive

**"체계를 세우자"에 반드시 돌아오는 "관료제 만들지 마라"에 대한 정본 답.** Adler & Borys (1996), ASQ 41(1), 61–89 `[PR]` `[논문]`

핵심은 형식화의 **양**이 아니라 **유형**이다. 같은 절차 문서가 어떤 조직에서는 능력을 실어주고(enabling) 어떤 조직에서는 소외시킨다(coercive). 논문의 자기 규정: "proposes a conceptualization of **workflow formalization** that helps reconcile contrasting assessments of bureaucracy as **alienating or enabling** to employees."

> **⚠️ B7 — enabling 형식화의 네 가지 설계 특성**(통상 repair / internal transparency / global transparency / flexibility로 인용됨)은 **원문 확인 실패**. **이 책에 가장 실용적으로 쓸 부분인데 미확보다.** 공개 PDF: `faculty.marshall.usc.edu/Paul-Adler/research/ASQ copy-1.pdf` — **저술 전 반드시 확인.**

## 1-6. 구현(implementation) ≠ 도입(adoption)

"파일럿은 성공했는데 확산이 안 된다"의 정본 이론. Klein & Sorra (1996), AMR 21(4), 1055–1080 `[PR]` `[논문]`

- **implementation climate** = "targeted employees' **shared summary perceptions** of the extent to which their use of a specific innovation is **rewarded, supported, and expected**" — **보상받고, 지원받고, 기대되는가**에 대한 구성원의 공유된 인식.
- **innovation-values fit** = 대상 사용자가 그 혁신이 **자기 가치를 촉진(또는 저해)한다고** 인식하는 정도.
- **구현 결과 스펙트럼: 저항(resistance) — 회피(avoidance) — 순응(compliance) — 헌신(commitment).**

**세 가지 실무 함의:** ① "쓰라고 시켰는데 안 쓴다"의 원인은 둘뿐이다 — 풍토가 약하거나, 가치가 안 맞거나. ② **순응과 헌신은 다르다.** AX 지표가 "사용률"만 보면 순응까지만 측정하는 것이다. ③ "AI가 내 가치를 촉진하는가 저해하는가"가 성패를 가른다.

> **저술 권고:** 변화관리 파트를 Kotter가 아니라 **이 이론으로 세워라.** Kotter의 실증적 지위는 §4-6 참조.

## 1-7. 감독의 두 등급 — 구성적 vs 교정적

Laux (2023), AI & Society `[PR]` `[논문]`

- **구성적(constitutive) 개입:** 사람의 사전 승인 없이는 결정이 성립하지 않음.
- **교정적(corrective) 개입:** 사후 교정으로 충분함.

→ **등록부의 권한 필드를 이 두 등급으로 나누는 설계**를 직접 제안할 수 있다.

## 1-8. 적정 의존(appropriate reliance)

- **적정 의존** = AI 조언이 맞을 때 따르고 틀릴 때 따르지 않는 것. **의존의 양이 아니라 의존의 정확성.**
- **과의존(over-reliance)** = 틀린 조언에 맹목적 동의 / **과소의존(under-reliance)** = 맞는 조언 무시. **둘은 별개 지표로 측정해야 한다.**
- **신뢰(trust)는 믿음으로, 의존(reliance)은 행동으로 나타난다 — 사람은 신뢰하지 않으면서도 의존할 수 있다.** `[논문]`

> **AX 측정 함의:** "직원들이 AI를 신뢰하나요?"라는 설문 문항이 왜 부족한지의 근거. 필요한 것은 태도가 아니라 **행동(의존)의 정확성**이고, 그것을 재려면 등록·로그가 있어야 한다 — 축 1로 되돌아온다.

---

# 2. 핵심 관점들 — 축별 정리

## 축 1 — 에이전트의 조직 등록

### 2-1-1. 관점 A: 등록은 통제가 아니라 "책임의 소재를 만드는 일"

**이 책의 핵심 주장을 벤더가 그대로 구현했다.** Microsoft Entra Agent ID의 관리 모델은 **기술 관리(technical administration)와 사업 책임(business accountability)을 분리**한다. `[웹]` ★ (ms.date 2026-04-16, 갱신 2026-09-03)

> "Microsoft Entra Agent ID introduces an administrative model that **separates technical administration from business accountability**, ensuring operational control and oversight without excessive permissions."

| 역할 | 성격 | 필수 | 할 수 있는 일 | 할 수 없는 일 |
|---|---|---|---|---|
| **Owner** | 기술 관리자 (개발자·IT·에이전트 제작자) | 선택 | 인증 속성 변경, 오너·스폰서 추가, 비활성화, 삭제, **재활성화·소프트삭제 복원·하드삭제** | — |
| **Sponsor** | 사업 책임자 (비즈니스 오너·PM·팀 리드) | **필수** (생성 시 반드시 지정) | 수명주기 결정(갱신·연장·제거), 액세스 패키지 요청, 사업적 정당화, **보안 사고 시 에이전트 행동이 정상인지 판단하고 정지·권한조정 승인** | 앱 설정 변경 불가. **재활성화·복원 불가** |
| **Manager** | 조직 계층상 상급자 | 선택 | 자기 밑으로 보고되는 에이전트 조회, 액세스 패키지 요청 | **수정·삭제 불가** |

**설계 디테일 (원문 그대로 인용 가능):**
- Sponsor: "**At least one sponsor is required for each agent identity and agent identity blueprint.**"
- 승계: "Sponsorship should be maintained to ensure succession when an employee who's a sponsor moves or leaves."
- **책임 희석 방지 규칙:** "For delegated creation requests where both an application and user context exist, **the calling user automatically becomes the sponsor if no sponsors are explicitly specified.** ... **Users with Agent ID admin roles aren't made sponsor automatically during creation. This avoids unintentionally overburdening admins with direct responsibility for individual agents.**"
- 할당 대상: Owner는 개인 사용자(게스트 포함)와 **서비스 주체(service principal)** — 그룹 불가. Sponsor는 사용자 + 특정 그룹(동적 멤버십, M365), **역할 할당 가능 그룹은 불가**. 최대 100명(그룹 5개 이내), 에이전트 사용자 계정 기준 최대 5명. Manager는 개인 사용자만.

> **이 책에서의 쓰임새:** 전작 「AX를 만들다」가 *"사번을 준다면"* 이라고 전망만 남긴 자리에, **이미 산업 표준 설계가 존재한다**는 답을 줄 수 있다. 특히 **"스폰서 필수 + 관리자는 자동 스폰서가 되지 않음"** 이라는 설계 결정은 *등록은 통제가 아니라 책임의 소재를 만드는 일* 이라는 이 책의 명제를 벤더가 구현한 증거다. **"기술 관리 ≠ 사업 책임"의 분리**는 한국 조직의 "IT부서가 다 알아서" 관성을 깨는 논거로 직행한다. → **PART 3의 뼈대 챕터 하나를 이 문서로 통째로 세울 수 있다.**

### 2-1-2. 관점 B: 오프보딩이 진짜 문제다 — 그리고 아무도 못 하고 있다

**축 1 전체에서 가장 강력한 단일 수치.** CSA 『The Non-Human Identity Governance Vacuum: AI Agents and the Fastest-Growing Unmanaged Attack Surface』, **2026-05-20** `[웹]` ★(랜딩 페이지) / △(PDF 파싱 실패)

| 수치 | 내용 |
|---|---|
| **78%** | **AI 아이덴티티의 생성 또는 제거에 관한 문서화된 정책이 없는** 조직 |
| **51%** | **AI 아이덴티티의 소유권이 불명확**하다고 보고한 조직 |
| **8%** | "legacy IAM이 AI·NHI 위험을 관리할 수 있다"에 **높은 확신**을 표한 응답자 |
| **44%** | 2024~2025 사이 측정된 기업 환경의 NHI 증가율 |

원문: "78% of organizations have no documented policy for creating or removing AI identities" / "Only 8% of respondents expressed high confidence that their legacy IAM systems can manage AI and NHI risks"

**그런데 폐기는 이미 제품 기능으로 존재한다** (Entra Agent ID, GA 2026-05-01) `[웹]` ★:
- **Agent identity deletion** — "automated cascade cleanup process and **soft-delete** functionality"
- **Sponsor lifecycle workflows** — 스폰서 유지·재배정 자동화
- **Agent identity sponsor templates** — "automatically transfer sponsorship when an agent identity sponsor changes roles or leaves the organization, **to prevent orphaned agents.**"

**→ 즉 기능은 있는데 정책이 없다.** 이것이 이 책이 서는 자리다.

**현장의 목소리 — 13년 동안 같은 문장:** `[커뮤]`
- **"making offboarding a lot easier... the main pain point, as opposed to onboarding"** — `olegp`, HN, **2013-10-07** 🕒
- **"after firing everyone they of course didn't follow the off boarding process"** (인수 후 해고당하고도 1년 넘게 JIRA 접근 권한이 살아 있었다) — `madaxe_again`, HN, **2026-03-20** ⚠️ 익명 사실 주장

> **저술 제안:** 오프보딩 챕터 오프닝은 **"2013년의 불만과 2026년의 불만이 같은 문장"** 이라는 구도로 열 수 있다. 13년 동안 안 풀린 문제를 에이전트가 수십 배로 증폭시킨다는 게 논거다.

### 2-1-3. 관점 C: "매니저를 붙인다"의 이론적 근거 — 이중으로 지지된다

**(가) 대리인 문제 (경제학·법학):** Kolt (2025) 「Governing AI Agents」, *101 Notre Dame L. Rev.* (forthcoming) `[논문]` — AI 에이전트가 일으키는 문제를 **정보 비대칭(information asymmetry) / 재량권(discretionary authority) / 충성(loyalty)** 세 갈래로 특징짓고, 인간 대리인에게 통하던 해법(인센티브 설계, 모니터링, 신인의무)이 왜 한계에 부딪히는지 논증한다. → **매니저를 붙이는 이유가 관리 취향이 아니라 대리인 문제 해결 장치**임을 말할 수 있다.

**(나) 책임 공백 (철학):** Santoni de Sio & Mecacci (2021), *Philosophy & Technology* 34(4), 1057–1084 `[PR]` `[논문]` ★

> "The responsibility gap is **not one problem but a set of at least four interconnected problems** — gaps in culpability, moral and public accountability, and active responsibility — caused by different sources, **some technical, others organisational, legal, ethical, and societal.**"

| 공백 | 조직 설계로의 번역 |
|---|---|
| 유책성(culpability) | 징계·법적 책임 주체 지정 |
| 도덕적 책임(moral accountability) | **소유자** |
| 공적 책임(public accountability) | 감사 로그·대외 설명 책임 |
| **능동적 책임(active responsibility)** | **사고가 나기 전에 예방할 의무를 진 사람 = 매니저** |

> **핵심:** **네 번째 공백(능동적 책임)이 조직 설계로만 메울 수 있는 유일한 공백**이다. 이것이 "기술로만 풀려는 시도가 왜 실패하는가"의 근거이자 이 책의 존재 이유와 정확히 겹친다.

### 2-1-4. 관점 D: 20년 계보 — "에이전트를 조직에 등록한다"는 새 발상이 아니다

**이 책의 가장 강력한 정당화 카드 중 하나.** LLM이 나오기 20년 전, 다중 에이전트 연구자들은 이미 "역할·그룹·의무"로 에이전트 조직을 명세했다. `[논문]`

**MOISE+** — Hübner, Sichman & Boissier (2002), SBIA 2002, LNAI 2507, DOI: 10.1007/3-540-36127-8_12 `[PR]`
조직을 **세 차원**으로 명세한다:
- **구조적(structural)** — 역할(role), 역할 간 상속 링크, 그룹(group)
- **기능적(functional)** — 목표 달성을 위한 전역 계획(global plans)과 미션(mission)
- **규범적·의무론적(deontic)** — 어느 역할이 어느 미션에 **의무(obligation)** 또는 **허가(permission)** 를 갖는지

원문 인용 가능: 역할은 "**constrain the individual behaviors of the agents**", 조직 링크는 "**regulate the social exchanges between these agents**", 그룹은 "**constrain the layout of agents involved in strong interactions**".

**재조직화(reorganization) 메커니즘:** **OrgManager 역할**의 에이전트가 재구성을 조율하고, **Designer 역할**의 에이전트가 현 구조를 분석해 더 나은 구조를 제안한다. → **"에이전트 조직을 누가 관리하는가"에 20년 전 답이 있다.**

**관련 계보:** OperA (Dignum 2004) — 조직 모델이 에이전트 사회를 "in terms of **roles, constraints and interaction rules**"로 기술. **조직의 목표와 개별 에이전트의 목표가 다를 수 있다**는 긴장을 정면으로 다룬다. / **electronic institutions** (Esteva et al. 2001) + **AMELI** 미들웨어 (2004) — 규범과 프로토콜을 **형식 명세**하고 **런타임에 강제**한다. 즉 "규칙을 문서로 쓰는 것"과 "규칙이 강제되는 것"을 분리하지 않는다.

> **⚠️ 인용 규율:** 이들은 **LLM 이전의 심볼릭 MAS 연구**다. 당시 에이전트는 명세된 대로만 행동하는 결정적 프로그램이었고, LLM 에이전트의 비결정성·프롬프트 취약성은 전제에 없다. **고전 계보로 인용하되 "그대로 적용 가능"이라고 쓰면 안 된다.**

### 2-1-5. 관점 E (반대편): "그거 서비스 계정 리브랜딩 아니냐" + "조직도가 폭발한다"

**이 책의 주장에 정면으로 부딪히는 두 반박이며, 둘 다 실제로 존재한다.** `[커뮤]`

**(가) 용어 반박** — §1-2 인용 4건. **이 책은 "사번을 준다"가 서비스 계정과 어떻게 다른지를 1장 안에서 답하지 못하면 보안·인프라 독자를 첫 챕터에서 잃는다.**

**(나) 직접 해보고 후회한 사람의 증언 — 가장 아픈 반박:**

> **"I went through the entire investor arc in about a day and a half. From the hopeful optimism of hiring a CEO, to watching the org chart explode, to complete disillusionment, to demoting the CEO back to a regular worker..."**
> ("하루 반 만에 투자자 서사를 통째로 겪었다. CEO를 고용하는 희망찬 낙관에서 시작해, 조직도가 폭발하는 걸 지켜보고, 완전한 환멸에 이르렀다가, 결국 CEO를 평사원으로 강등시켰다…")
> — `yego`, HN, **2026-03-04**, https://news.ycombinator.com/item?id=47245374
> 맥락: 멀티 에이전트에 조직적 권한을 넓게 주자 **역할이 20개로 불어나고 실제 산출물 대신 메타 작업을 우선**하기 시작했다. (개인 실험 규모)

> **"Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!"**
> — `polotics`, HN, **2026-09-04** (검색 하루 전), https://news.ycombinator.com/item?id=49561918

> **책이 반드시 갈라야 할 것:** "사번을 준다"가 **권한과 책임의 귀속**을 뜻하지 **조직 놀이(org-chart cosplay)** 를 뜻하지 않는다는 경계. 이 경계를 명시하지 않으면 위 두 인용이 그대로 적중한다.

### 2-1-6. 관점 F (긴장): 새 신원을 만들 것인가, 있는 신원을 쓸 것인가

**이 책의 처방과 정면으로 긴장하는 표준 진영의 설계 철학.** `[커뮤]`

MCP SEP-1933 「Workload Identity Federation」의 설계 의도 (원문):
> "the goal of the spec is to let workloads use existing credentials (think Kubernetes PSAT tokens, SPIFFE JWTs) so that deployments **don't have to further proliferate client secrets** if they have better options available."
> — `PieterKas`, https://github.com/modelcontextprotocol/modelcontextprotocol/pull/1933, 2025-12-17 🕒 (2026-09-05 기준 open·40댓글)

- **이 책:** "에이전트마다 새 신원을 만들어 등록하라"
- **표준 진영:** "새 신원을 만들지 말고 런타임이 이미 주는 신원을 쓰라"

> **저술 제안:** 이 긴장을 회피하지 말고 다루면 책의 깊이가 생긴다. 답의 방향은 아마 **"아이덴티티의 발급 주체는 런타임이되, 등록·소유·수명주기의 원장은 조직이 갖는다"** 일 것이다.

---

## 축 2 — SOP에서 출발하는 체계 구축

### 2-2-1. 관점 A: 표준 없이는 개선도 없다 (고전적 근거)

**이 책 관통선의 가장 오래된 근거.** Toyota 표준작업(standardized work) — **표준작업은 kaizen의 토대다.** 비교할 표준이 없으면 개선이 정말 개선인지 알 방법이 없기 때문이다. 표준화 → 표준 준수 → 문제 발견 → 개선 → 새 표준 수립 → 반복. 표준작업과 kaizen은 **같은 활동 사이클의 두 부분**이며, 같은 사람들이 같은 표준을 통해 연결되어 수행한다. `[웹]` △

> **책에서의 쓰임새:** **바텀업 AI 실험은 "표준 없는 kaizen"이다.** 각자 개선하지만 무엇 대비 개선인지 아무도 모른다. 그리고 도요타에서 표준을 만들고 개선하는 주체가 **동일한 현장 작업자**라는 점은, 탑다운 전향이 현장을 배제하는 게 아니라는 반론 방어가 된다. → **PART 2 오프닝 최유력 후보.** AXMM 축 D(평가·측정·개선)와 연결.

**ISO 9001:2015 Clause 7.5** — 문서화된 정보의 통제와 가용성을 요구하되 **형식이나 구조를 규정하지 않는다.** 문서화된 정보의 세 기능: **지식의 운반체 / 의도를 전달하는 수단 / 증거의 기록.** `[웹]` △
> 이 세 기능은 **에이전트에게 절차를 주는 이유와 정확히 같다.** 그리고 "형식을 규정하지 않는다"는 유연성이, 40년 뒤 그 문서가 기계가 읽는 형식(MCP 툴 정의, AGENTS.md)으로 바뀌는 것을 허용한다.

### 2-2-2. 관점 B: SOP → 코드 변환은 이미 방법론과 수치가 있다

**Amazon Science 『Structuring the Unstructured: A Multi-Agent LLM Framework for Transforming Ambiguous SOPs into Code』** — EMNLP 2025 Industry Track `[웹]` △ / `[논문]` 계열

**3모듈 구조 (이 책의 실무 절차로 그대로 번역 가능):**
1. **Clarifier** — LLM + 사내 지식베이스(RAG) + **human-in-the-loop** 으로 SOP의 모호성 제거
2. **Planner** — 정제된 자연어 지시를 **함수(API) 태깅, 조건 분기, human-in-the-loop 체크포인트**를 갖춘 계층적 태스크 플로우로 변환
3. **Implementor** — 실행 가능한 코드 조각 또는 의사코드 템플릿 생성

**핵심 수치:** end-to-end 정확도 **88.4%** (△ — 원문 확인 권장). Ablation 시 각 모듈 제거로 성능 뚜렷하게 하락.

> **Clarifier 단계에 사람이 반드시 들어간다**는 설계가 "SOP를 쓰는 일 자체가 조직의 암묵지를 캐내는 일"이라는 이 책의 주장과 일치한다.

**MetaGPT** (ICLR 2024 **Oral**, arXiv:2308.00352) `[PR]` `[논문]` — **SOP를 프롬프트 시퀀스로 인코딩**해 LLM 다중 에이전트 협업에 인간 워크플로를 이식. 문제의식: LLM을 순진하게 연결하면 **연쇄적 환각(cascading hallucinations)** 으로 논리적 불일치가 생긴다.
> 원문: SOP는 "**outline the responsibilities of each team member, while establishing standards for intermediate outputs**."
> **→ SOP의 가치가 단계 나열이 아니라 각 단계의 산출물이 무엇이어야 하는지를 못 박는 데 있다**는 통찰. 실무 SOP 작성 지침으로 직접 사용 가능.

**SOP-Bench** (arXiv:2506.08119, v2 2026-02-23) `[PP]` `[논문]` — 인간 전문가가 쓴 실제 SOP에서 도출한 **2,000개 이상 과제**, **12개 비즈니스 도메인**.
- 도메인별 과제 성공률 **57%~100%** — 편차가 매우 크다
- ReAct 최고 성능: **Claude 4 Opus 72.4%**, Claude 4.5 Sonnet **63.3%** 🕒 (2026-02 시점 라인업)
- **어떤 모델-에이전트 조합도 전 도메인을 지배하지 못했다**
- 저자 결론: **"Newer models do not guarantee better performance"**

> **AX 실무 리더에게 가장 실용적인 수치.** "최신 모델로 갈아끼우면 좋아지겠지"를 정면 반박한다. **에이전트를 등록하고 관리한다는 것은 곧 모델 교체를 관리한다는 뜻**이며, 등록부에 **모델 버전과 성능 기준선을 함께 기록**해야 하는 이유가 여기 있다. 도메인별 편차(57~100%)는 **도메인별로 등록·평가해야 한다**는 근거.

### 2-2-3. 관점 C: 절차의 계층은 이미 사실상의 표준이다

**AGENTS.md** — 2025-08 형식화 (OpenAI·Google·Cursor·Factory·Sourcegraph 협업), Linux Foundation의 Agentic AI Foundation이 관리 `[웹]` △
- **"기계를 위한 README"** — 스키마 없는 순수 마크다운, 필수 구조 미강제
- **모노레포 지원: 하위 디렉터리에 추가 배치, 트리에서 가장 가까운 파일이 우선** → 계층적 설정. OpenAI 자체 저장소는 하위 컴포넌트에 **88개** 사용
- ⚠️ **B6 — 채택 저장소 수(20,000 vs 60,000)는 출처 간 불일치. 수치 인용 지양.**

> **책에서의 쓰임새 (매우 중요):** **"절차의 계층"이 이미 사실상의 표준으로 존재한다.** 전사 규칙(루트) → 부문 규칙(하위) → 가장 가까운 것이 우선. **이것은 조직의 SOP 체계와 구조적으로 동형이다.**

### 2-2-4. 관점 D: SOP와 등록이 산업 표준에서 실제로 합류한 시점

**MCP 인가 스펙 개정 이력** 🕒 (2026-09-05 기준, spec 원문 미열람 △) `[웹]`

| 개정 | 날짜 | 내용 |
|---|---|---|
| 초기 인가 도입 | **2025-03-26** | OAuth **2.1** 기반 인가 프레임워크 |
| 리소스 서버 분류 | **2025-06-18** | MCP 서버를 OAuth 리소스 서버로 분류, **Resource Indicators (RFC 8707)** 요구 → 토큰의 엉뚱한 서버 재사용 방지 |
| 대규모 개정 | **2026-07-28** | 출시 이래 최대 개정. 코어를 **stateless 아키텍처**로, 인가 동시 강화 |

**결정적 사건:** Okta의 **Cross App Access(XAA)가 MCP의 공식 Enterprise-Managed Authorization 확장으로 채택**됐다 (2026-08-24 확인) `[웹]` ★
> **즉 절차를 노출하는 규약(MCP)과 신분을 부여하는 규약(XAA/OAuth)이 2026년에 합류했다.** 이 책의 관통선(SOP → 등록)이 산업 표준에서 그대로 반복된 시점. → **PART 2 → PART 3 전환부의 논증.**

**프로세스 마이닝의 전향:** Celonis **Agent Mining** (Microsoft Agent 365 프라이빗 프리뷰, 2026-05-01) — 모든 에이전트 의사결정의 자율 추론과 로직을 분석. `[웹]` △
> **"프로세스 마이닝이 사람의 프로세스를 캐던 도구에서, 에이전트의 프로세스를 캐는 도구가 되었다."** 이름 자체가 이 책의 관통선을 벤더가 따라간 증거이며, 축 1(감사)과도 연결된다.
> 타임라인: AgentC 발표 2024-10-23 → Orchestration Engine·Agent Mining·프로세스 인텔리전스용 첫 MCP 서버 2025-11-04(Celosphere) → MS Agent 365 연동 2026-05-01.

### 2-2-5. 관점 E (반대편): "Confluence는 문서가 죽으러 가는 곳"

**이 책의 1보에 대해 독자가 떠올릴 이미지가 바로 죽은 Confluence 페이지다.** 그리고 이건 한 사람의 짜증이 아니라 **약 5년간 여러 사람이 거의 같은 문장으로 반복한 업계 상식**이다. `[커뮤]` ★

> **"Confluence is where documentation goes to die. And then rot."**
> — `EdwardDiego`, HN, **2020-07-12**, https://news.ycombinator.com/item?id=23808854

같은 문장을 쓴 독립 사례 4건 더: `GordonS`(2019-03-19, 검색 무용·탐색 곤란), `more_corn`(2022-02-06, "absolute garbage"), `stock_toaster`(2023-08-17, 느린 속도·부실한 검색), `morkalork`(2024-02-14). 🕒 시점 명시 필수.

**한국 커뮤니티도 같은 결:** `[커뮤]`
- 검토를 거친 공식 문서 버전이 있는데 다음 버전을 작업하려면 **별도 작업용 페이지를 만들어야 하고, 그 결과 검색 결과가 오염된다** (GeekNews topic 17832)
- Confluence가 너무 느려 **"Confluence 기다리는 중"이 관용구가 될 정도**였다 (GeekNews topic 15610) ⚠️ 익명 주장

> **책이 세워야 할 조건:** "SOP를 만들자"가 아니라 **"살아 있는 SOP만이 재료가 된다"**.

### 2-2-6. 관점 F (2026년 신규 통증): AI가 문서를 쓰기 시작하면서 생긴 부패

> **"When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this."**
> ("LLM이 만든 문서나 런북을 받으면, 첫 생각은 '내가 이걸 읽은 최초의 인간일 가능성이 꽤 높다'는 것이다.")
> — `backlava12`, HN, **2026-08-11**, https://news.ycombinator.com/item?id=49258726 `[커뮤]` ★

> **최고의 챕터 오프닝 후보 중 하나. 쓰기는 공짜가 되고 읽기는 희소해졌다는 역전.** SOP를 AI로 대량 생성하려는 독자에게 정확히 필요한 경고다.

보강: **"1-shotting documentation with AI is a bad idea. You then have to have multiple verification passes to have any chance of it being worth anything."** — `tcoff91`, HN, 2026-07-22.

### 2-2-7. 관점 G (반대편): 긴 규칙 파일은 지켜지지 않는다 — 심지어 해롭다는 주장까지

**이 책이 "에이전트에게 SOP를 준다"고 할 때 가장 실무적으로 아픈 반박.** `[커뮤]`

- 최신 모델(GPT-5.6 계열)에서 상세한 AGENTS.md 지시가 **"redundant at best and frequently actively harmful"** — `nick__m`, HN, 2026-08-29 ⚠️ 익명 주장(특정 모델 동작)
- 모델 5.2 무렵부터 AGENTS.md 사용을 그만뒀다, MCP 툴과 함께 **"useless context bloat"** 를 만든다 — `Topfi`, 2026-08-29 ⚠️ 익명 주장(자체 평가)
- 모델이 외부 컨텍스트 파일을 **진짜로 쓰는지 준수하는 시늉만 하는지 확인할 방법이 없다** — `reacharavindh`, 2026-08-29
- 조용한 실패: **"Claude Code doesn't validate it - it just silently ignores the skill."** — `anotherCodder`, 2026-02-12
- **반대 증언도 있다:** 잘 유지된 AGENTS.md가 메모리 기능보다 **거의 항상 더 나은 결과**를 냈다 — `nzach`, 2026-08-31. **이 논쟁은 아직 안 끝났다 — 양쪽 다 기록한다.**

> **"절차를 주면 따른다"는 가정이 조용히 깨진다.** 감사·검증 루프가 없으면 SOP 배포는 착시다.

### 2-2-8. 관점 H (계보 경고): RPA는 왜 기대만큼 안 됐나

> 기존 RPA는 **"too brittle"** 하고 유지보수 부담이 **대체하려던 노동보다 커지는 경우가 많았다.** — `euphetar`, HN, **2026-07-30** `[커뮤]`

보강: 런타임 에이전트가 **깨지기 쉽고 감사하기 어렵다**는 판단이 직장의 RPA 경험으로 강화됐다(`cowartc`, 2026-04-16) / RPA 스크립트 경험 끝에 **결정론적 코드 기반 + 의도적 AI 통합**으로 갔지 완전 자동화로는 안 갔다(`muchael`, 2026-04-17).

> **RPA 챕터의 핵심 문장: 유지보수 비용 > 절감된 노동이라는 손익 역전이 RPA 실패의 구조다.** 이 책의 "에이전트 등록"이 같은 함정을 피하려면 **등록·소유·감사에 드는 운영 비용을 처음부터 계산에 넣어야 한다.**

---

## 축 3 — 바텀업 → 탑다운 전향

### 2-3-1. 관점 A: 바텀업의 정의이자 한계 — "개인 생산성은 오르는데 조직 성과는 안 오른다"

**두 독립 조사가 같은 결론에 도달했다.** 이것이 이 책 1장의 문제 제기다.

**(가) MIT Project NANDA 『The GenAI Divide: State of AI in Business 2025』** — 2025-07 발표, 2025-08 광범위 보도 `[웹]` △ 🕒

> "Just 5% of integrated AI pilots are extracting millions in value, while the vast majority remain stuck with **no measurable P&L impact**."

핵심 진단 (이 책과 직결):
> 핵심 장벽은 모델 품질도, 인프라도, 규제도 아니다. **학습(learning)** 이다 — 대부분의 GenAI 시스템은 피드백을 보존하지 않고, 맥락에 적응하지 않으며, 시간이 지나도 나아지지 않는다.
> 이 도구들은 **조직 성과가 아니라 개인 생산성**을 높인다.

**⚠️ 방법론 (반드시 함께 밝힐 것) — C2:**
- 기간 2025년 1~6월 / 공개된 AI 이니셔티브 **300건 이상** 리뷰 / 구조화 인터뷰 **52건** / **설문 응답 153건 — 4개 컨퍼런스의 시니어 리더 대상**
- → **무작위 표본이 아니라 컨퍼런스 참석자 편의표본이다.** "95%"는 엄밀한 모집단 추정치가 아니다.
- **MIT 공식 도메인의 원문 URL을 확보하지 못했다.** 유통 중인 것은 "v0.1" 표기 PDF 미러다. **이 사실 자체가 서술 가치가 있다.**

**커뮤니티의 방법론 반박 2건** (HN 스레드 230점·167댓글, 2025-08-18) `[커뮤]`:
- `layer8`: 표본이 **"300 public AI deployments"** 이고 비공개 프로젝트는 빠졌다. 낮은 곳에 달린 열매를 AI 없이도 해결했을 가능성 → **"AI wasn't the key to success?"**
- `RaftPeople`: **"실패"의 정의 문제.** SAP 도입 통계에서도 그랬듯 "실패"란 대개 **예산·일정 초과**를 뜻하지 작동하지 않는다는 뜻이 아니다.

> **저술 규율 (BLOCKING):** 이 숫자를 쓴다면 **방법론과 두 반박을 반드시 함께 실어라.** 그것이 오히려 저자의 신뢰를 높인다. 밝히지 않고 인용하면 **이 책이 그 오용에 가담하는 셈**이 된다.

**(나) McKinsey 『The State of AI: Global Survey 2026』** — 2026 `[웹]` △ (원문 열람 실패 — 타임아웃, C1) 🕒

| 수치 | 내용 |
|---|---|
| **37%** | AI가 자사 **EBIT에 기여**했다 — **전년 대비 변화 없음** |
| 약 **6%** | "AI 고성과자"(EBIT 5% 이상 AI 귀속 + 영향이 significant) — **정체** |
| **27% → 40%** | **대기업** 중 하나 이상의 기능에서 **AI 에이전트를 스케일링**하는 비율 |
| **22%** | **소규모 조직**의 동일 지표 — **정체** |
| **8/10** | 자기 개인 생산성이 향상됐다는 응답 |
| **32%** | 에이전틱 코딩 도구로 사내 구축이 가능해져 소프트웨어 구매를 포기한 조직 |

> **탑다운 효과를 보여주는 가장 직접적인 수치.** 대기업이 잘해서가 아니라 **체계를 세울 수 있는 규모의 조직만 스케일링에 성공하고 있다**는 해석. 그리고 **"개인 생산성 8/10 vs EBIT 기여 37% 정체"** 는 MIT NANDA와 정확히 같은 진단이다.

**(다) 학술 근거 — 채택은 인터넷보다 빨랐지만 절감 시간은 1.4%**
Bick, Blandin & Deming (2024), NBER WP 32966 `[WP]` `[논문]` 🕒 (2024년 말 기준, 이후 갱신 가능성)
- 미국 18~64세 인구의 **거의 40%** 가 생성형 AI 사용
- **취업자 응답자의 23%가 직전 1주일 내 업무 목적 사용, 9%는 매 근무일 사용**
- 전체 근로 시간의 **1~5%** 가 현재 생성형 AI의 보조를 받음
- **응답자가 보고한 절감 시간은 총 근로 시간의 1.4%**
- 생성형 AI의 **업무 채택은 PC만큼 빨랐고, 전체 채택은 PC나 인터넷보다 빨랐다**

> **"채택은 인터넷보다 빨랐지만 절감 시간은 총 근로 시간의 1.4%"** — 이 대비가 이 책의 논지를 한 문장에 담는다. 개인 사용이 아무리 퍼져도 **조직 성과로 응축되지 않는다.**

### 2-3-2. 관점 B: 왜 기술만 사서는 성과가 안 나는가 (정본 근거)

**Brynjolfsson, Hitt & Yang (2002), Brookings Papers on Economic Activity 2002(1)** `[PR]` `[논문]`
> "**each dollar of installed computer capital in a firm is associated with at least five dollars of market value**, after controlling for other assets."

> **예산 협상 자리에서 바로 쓸 수 있는 비율 — 기술 구매 1에 조직 보완재 5.** 이 책의 등록 체계·SOP 정비·변화관리가 바로 그 "5"에 해당한다.
> **⚠️ 인용 규율:** 1990년대 컴퓨터 도입 데이터다. **"기술만으로는 부족하다"는 원리**를 인용하되 **1:5 비율은 IT 사례임을 밝히고** 쓸 것. AI에 직접 대입하면 과대 해석.

**생산성 J-curve** — Brynjolfsson, Rock & Syverson (2017), NBER WP 24001 / (2021) AEJ: Macroeconomics `[논문]`
> 역설의 정식: AI가 "match or surpass human-level performance in increasingly more domains, yet **measured productivity growth has declined by half over the past decade**."
> 네 후보(잘못된 기대 / 잘못된 측정 / 이익의 재분배와 소모 / **구현 지연**) 중 **보완적 혁신과 조직 재설계에 시간이 걸린다**가 가장 설득력 있다고 결론.

> **이 책의 존재 이유를 한 장의 그림으로 만들어주는 이론.** 범용 기술 도입 초기에는 측정 생산성이 오히려 떨어진다 — 조직이 무형자산(프로세스 재설계, 재교육, 새 역할 정의)에 자원을 쏟는데 이 투자는 비용으로 잡히고 산출로는 안 잡히기 때문이다. **바텀업 단계에서 성과가 안 보이는 것이 정상**이며, 골짜기를 건너려면 **체계 구축이라는 무형 투자를 의도적으로** 해야 한다.
> **⚠️ 오용 경계:** 골짜기가 얼마나 깊고 긴지는 사전에 알 수 없다. 이 이론은 **"기다려라"의 알리바이로 오용될 수 있다.**

### 2-3-3. 관점 C: 거버넌스는 규제 준수가 아니라 프로젝트 생존 조건이다

**Deloitte 『2026 State of AI in the Enterprise』** — 2026-04-24, n=**3,235** IT·비즈니스 리더, **24개국** `[웹]` ★
- **21%** — 에이전틱 AI에 **성숙한 거버넌스 모델**을 갖췄다 (→ 약 80%가 없음)
- **23%** — 현재 에이전틱 AI를 최소 "moderately" 사용 중
- **74%** — 2027년까지 최소 "moderately" 쓸 것으로 기대 (그중 23% "extensively", 5% 완전 통합)
- **85%** — 자사 필요에 맞게 에이전트를 커스터마이즈할 계획

> 제목이 그대로 논지다: "Business and IT leaders report **AI agents are scaling faster than their guardrails**"
> Deloitte가 짚은 **결여된 거버넌스 3요소** (원문): "**clear boundaries for agents** that define which decisions they can make independently versus which require human approval, **real-time monitoring systems** that track agent behavior and flag anomalies, and **audit trails** that capture the full chain of agent actions"
> → **"23% 쓰는데 21%만 거버넌스"** 라는 대비가 이 책의 존재 이유를 한 줄로 요약한다. 그리고 이 3요소는 §1-1의 Chan et al. 3축과 정확히 대응한다.

**Gartner** (2025-06-25) `[웹]` △ (원문 403, 복수 매체 교차 확인)
> **2027년 말까지 에이전틱 AI 프로젝트의 40% 이상이 취소될 것이다** — 비용 증가, 불명확한 사업 가치, 또는 **부적절한 리스크 통제** 때문에.
- 근거: 2025년 1월 웨비나 참석자 **3,412명** 폴 — 19% 상당한 투자 / 42% 보수적 투자 / 8% 투자 없음 / 31% 관망
- **"agent washing"** — 기존 AI 어시스턴트·RPA·챗봇을 실질적 에이전틱 역량 없이 리브랜딩. Gartner는 **수천 개 벤더 중 실제는 약 130개**로 추정.

> **"부적절한 리스크 통제"가 취소 사유 3개 중 하나로 명시**됐다는 점 — 이 책 축 1의 실용적 정당화. **거버넌스는 규제 준수가 아니라 프로젝트 생존 조건이다.**

**BCG 『Where's the Value in AI?』** — **2024-10-24** 🕒 (2년 전 자료임을 반드시 명기), n=1,000 CxO·시니어 임원, 59개국 `[웹]` △
- **74%** 가시적 가치를 아직 못 냄 / **4%** 전 기능 최첨단 역량 + 일관된 상당 가치 / **22%** 상당한 이득을 내기 시작 → 성공적 스케일 **26%**

### 2-3-4. 관점 D: shadow AI — 바텀업의 성공 지표이자 실패 지표

**논리 구조 (이 책의 축 3 → 축 1 전환 논증):**
1. shadow AI는 바텀업의 **성공 지표이자 실패 지표**다 — 사람들이 알아서 쓴다(성공), 조직이 그것을 모른다(실패).
2. **경영진이 부하직원보다 2배 이상 많이 미승인 도구를 쓴다** (65% vs 31%, C레벨은 73%) — **탑다운을 요구할 사람들이 먼저 규칙 밖에 있다.** 변화관리 챕터에서 리더십 정합성을 요구할 근거.
3. Okta 조사에서 **지식근로자 100%가 직전 3개월간 AI와 함께 일했다**고 응답 (n=492).

**⚠️ C4 — 이 절의 수치 대부분이 집계 사이트를 거쳤다. 원 조사 URL 미확보. 본문 사용 시 반드시 원 조사 확인.** `[웹]`

| 수치 | 내용 | 출처 조사 | 연도 |
|---|---|---|---|
| **78%** | 직원이 자기 AI를 직장에 가져온다(BYOAI) | Microsoft WorkLab / Work Trend Index | 2025 ⚠️ |
| **55%** | 승인되지 않은 도구 사용 | Salesforce | 2024 ⚠️ |
| **11%** | AI 도구에 붙여넣는 전체 데이터 중 민감 정보 비율(소스코드·PII·재무·법률) | **Cyberhaven** | **2026** |
| **65% vs 31%** | 시니어 의사결정자 대 부하직원의 미승인 사용률 (C레벨 73%) | ⚠️ 조사 미상 | 2026 |
| **100%** | 직전 3개월간 AI와 함께 일한 지식근로자 | Okta *AI Agents at Work 2026* (n=492) | 2026 |

The Register 표제 (2026-05-27): **"Bosses blinded by confidence about shadow AI use by workers"** — 리더의 인식과 현실의 격차.

**⚠️ 학술 근거는 사실상 1건뿐이다:** Silic et al. 「From Shadow IT to Shadow AI」, *Strategic Change* (Wiley), DOI: 10.1002/jsc.2682 — **발행 연도·권·호 미확인(본문 403)**. 전문직 140명 설문 + 임원 10명 인터뷰. `[논문]` ⚠️
> **저술 규율:** shadow AI 통계는 **전부 벤더·업계 조사**다. **분위기 전달용으로만 쓰고 논증의 하중을 실으면 안 된다.** 논증 하중은 학술 근거(Bick et al.의 채택률, 아래 Atkinson & O'Bryan의 행동 기반 측정)에 실어라.

**행동 기반 측정이라는 대안** — Atkinson & O'Bryan (2026), arXiv:2607.04543, ICML 2026 Workshop on Technical AI Governance `[PP→워크숍]` `[논문]`
- 정부 문서에서 언어모델의 흔적을 탐지. 요지: "lightweight, externally reproducible, and based on **revealed behavior rather than stated intent**"
- **2026년 기준, 10개 소스 중 4개에서 AI 보조 작성의 통계적으로 유의한 징후. 2021년 기준선은 일관되게 0에 가까웠다.**
- ⚠️ LLM 텍스트 탐지는 오탐·미탐이 난제 — **절대 수치가 아니라 추세(2021 ≈ 0 → 2026 4/10)로만 인용.**

> **실무 번역:** 사내 AX 성숙도를 **"몇 명이 쓴다고 답했나"가 아니라 "산출물에 흔적이 있나"** 로 재라.

**현장의 온도** `[커뮤]`:
- **"Shadow AI economy: people using personal LLM subscriptions instead of internal offerings"** — `chriskanan`, HN, 2025-08-21
- **"How hard it is to get people to use official corporate tools instead of shadow AI?"** — `pbronez`, HN, 2025-12-03
- 탐지하는 쪽의 언어: **"Big current focus is shadow AI, i.e. catching when employees paste sensitive data into ChatGPT"** — `volker48`, HN, 2026-07-01
  > **"잡아낸다(catching)"** 는 단어가 직원에게 어떻게 들릴지가 변화관리의 핵심이다. 축 4와 직결.
- **한국 맥락 (이 책의 독자에게 가장 실감나는 한 줄):**
  > **"일단 회사에서 AI 서비스를 지원 거의 안해주네요. 개인별로 쓰는건 개인이 하라고 하고(회사에서 쓰려고 개인이 AI 서비스 구독 ㅜ) 팀에는 클로드 프로?월 3만원짜리 지원하고 끝."**
  > — `akapwhd`, GeekNews topic 29217, ≈2026-05 (상대 표기 "4달전", 2026-09-05 조회 기준)

> **설계 조건:** 금지가 아니라 **공식 경로가 개인 경로보다 나아야** 한다.

### 2-3-5. 관점 E: 실증의 이질성 — "누구에게" 효과가 있는가

**세 개의 독립 연구가 같은 이질성에 도달했다: 경험이 적을수록 효과가 크다.** `[논문]`

| 연구 | 게재 | 표본 | 핵심 수치 | 이질성 |
|---|---|---|---|---|
| Brynjolfsson, Li & Raymond (2025) | *QJE* 140(2), 889–942 `[PR]` | 고객지원 상담원 **5,172명** | 시간당 처리 건수 **+15%** | **저숙련: 속도·품질 모두 개선 / 최고 숙련: 속도 소폭 이득, 품질 소폭 하락** |
| Noy & Zhang (2023) | *Science* `[PR]` | 대졸 전문직 **453명** | 소요 시간 **−40%**, 품질 **+18%** | **노동자 간 불평등 감소** |
| Cui et al. (2025) | *Management Science* `[PR]` | 개발자 **4,867명** (MS·Accenture·Fortune 100 3개 현장 RCT) | 완료 과제 **+26.08% (SE 10.3%)** | **경험이 적을수록 채택률·향상 모두 큼** |

인용 가능 원문 (Brynjolfsson et al.): "**less experienced and lower-skilled workers improve both the speed and quality of their output, while the most experienced and highest-skilled workers see small gains in speed and small declines in quality**"

부수 효과 (변화관리 카드): **고객 감정 개선, 직원 유지율(retention) 상승** — "AI가 사람을 밀어낸다"는 프레임에 대한 반증.

> **⚠️ 인용 규율 (BLOCKING):** 위 효과 크기는 **각각 다른 직무·다른 과제·다른 모델 세대**에서 측정됐다. 하나로 뭉뚱그려 "AI는 N% 생산성을 올린다"고 쓰면 안 된다. 각 수치에 **직무·표본·연도·모델 세대**를 반드시 붙일 것. (Brynjolfsson = GPT-3.5 세대, Noy & Zhang = 2023년 초 ChatGPT, Cui = 코드 완성 도구 세대)

**들쭉날쭉한 경계 (jagged frontier)** — Dell'Acqua et al. (2025), *Organization Science* `[PR]` `[논문]`
- 표본: **고숙련 경영 컨설턴트 758명**, **18개 지식노동 과제**, 사전 등록 무작위 실험, **2023년 GPT-4** 🕒
- **경계 안:** 과제 완수 **+12.2%**, 속도 **+25.1%**, 맹검 평가 품질 **+40%**
- **경계 밖:** 정답 확률 **약 19% 낮음** — ⚠️ **B2: "19%"인가 "19%p"인가 출처마다 갈린다. 확정 전엔 "약 19%"로 완충.**

> **이 책이 "실험을 체계로 전향해야 한다"고 말하는 가장 강력한 근거.** jagged frontier는 **개인이 시행착오로 알아낼 수 없는 지형**이다. 어떤 과제가 경계 안이고 밖인지는 **조직이 축적해야 알 수 있는 지식**이며, 그것을 축적하는 장치가 등록부·평가·로그다. **바텀업 실험이 개인 안에서 끝나면 이 지식은 조직에 남지 않는다.**

### 2-3-6. 관점 F (결정적 반증): 인식과 실측의 39%p 괴리

**이 책 전체에서 가장 강력한 한 장면이 될 수 있다.** METR (2025), arXiv:2507.09089 `[PP]` `[논문]` 🕒 (2025년 2~6월, Cursor Pro + Claude 3.5/3.7 Sonnet)

- 표본: AI 사용 경험 중간 수준 개발자 **16명**, **246개 과제**, 대상 프로젝트에 **평균 5년의 사전 경험**
- **과제 시작 전 예측: AI가 완료 시간을 24% 줄일 것**
- **실제 결과: 완료 시간이 19% 증가 — AI가 개발자를 느리게 만들었다**
- **연구 종료 후 사후 추정: AI가 완료 시간을 20% 줄였다**

> 원문: "developers **forecast** that allowing AI would reduce completion time by **24%**. Surprisingly, allowing AI actually **increased** completion time by **19%**."
> **24% → +19% → 20%. 세 숫자를 나란히 놓는 것 자체가 문장이다.**

> **이 책의 논지:** **체감으로 AX 성과를 관리하면 안 된다.** 바텀업 실험이 자기 보고에 의존하는 한 조직은 자기가 어디 있는지 모른다. **측정 체계를 세우는 것이 등록·로깅의 목적 중 하나다.**
> **⚠️ 인용 규율 (BLOCKING):** 표본 16명·246과제로 작다. 대상이 **자기 코드베이스에 평균 5년 숙련된 오픈소스 개발자** — AI의 상대 우위가 가장 작은 조건이다. 프리프린트. **"AI는 생산성을 떨어뜨린다"로 일반화하면 심각한 오독이다.** 반드시 "누구에게, 어떤 조건에서"를 붙일 것.

### 2-3-7. 관점 G (반대편): 탑다운 강제 도입이 실제로 낳은 것 — 증언 11건

**이 책의 가장 위험한 지점.** 탑다운을 옹호하는 책이 이것을 모르면 안 된다. `[커뮤]` (전부 HN, 2025-04 ~ 2026-08)

| 증언 | 작성자·날짜 | 검증 |
|---|---|---|
| **"now he's implementing an AI mandate for every employee, replete with tracking and metrics and the threat of being fired"** | `bitwize`, 2026-03-28 | ⚠️ 익명(자기 회사 CEO) |
| **"mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though."** | `ares623`, 2026-03-06 | 경험담 |
| **"usage of ai is not just allowed or encouraged but mandated. And is part of their performance score"** | `axegon_`, 2026-03-15 | ⚠️ 익명(제3자 회사) |
| **"Microsoft...will simply PIP you for being a luddite if you aren't meeting usage metrics"** | `klardotsh`, 2025-07-01 | ⚠️ 익명 |
| **"everyone was forced to use Microsoft's AI tools whether they worked or not"** | `mips_avatar`, 2025-12-03 | ⚠️ 익명(특정 기업) |
| **"not tying ratings/comp to AI usage (seriously how fucking stupid are they over in Redmond?)"** | `caconym_`, 2025-12-03 | 정서(날것) |
| 필수 쿼리 수까지 지정된 강제 사용 | `stego-tech`, 2025-04-12 | ⚠️ 익명 |
| **"VP right now saying everyone must use AI every day"** | `placardloop`, 2025-05-25 | ⚠️ 익명 |
| AI 의무화가 **지표 게이밍**을 유발 — 준수해 보이려 사용량 비용을 인위적으로 부풀림 | `plaguuuuuu`, 2026-06-28 | 경험담 |
| **"thanks to AI mandate, quality is going downhill a lot faster"** | `rk06`, 2026-08-25 | 정서 |
| AI 의무화가 **"quiet fire people"** 수단으로 쓰이며 교육·실험 시간을 안 줌 | `keeda`, 2025-12-03 | 해석 |

**한국 커뮤니티의 같은 지적 (한국 독자용 인용으로 최적):**
> **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음"**
> — `brainer`, GeekNews topic 33050, ≈2026-08-31

**더 정밀한 진단 (실마리):** 실패 모드는 "강제" 자체가 아니라 **맥락 무시한 획일화**다. `tdeck`(2026-03-29)은 "We believe everyone can be more productive with an SD-based workflow"라는 식으로 **기능적으로 맞지 않는 팀에까지 획일적 워크플로를 강제**해 반감을 산 사례를 들었다.

**⚠️ 균형 장치 (반드시 함께 기록):**
> **"AI adoption is up to 80-90%; ICs absolutely are enamored with AI too. HN...is largely an echo chamber"**
> — `keeda`, HN, 2026-03-28 ⚠️ 익명(80~90% 수치 미검증)
> **이 경고는 이 리서치 문서 자체에 적용된다.** 축 3·4 인용의 약 80%가 HN에서 왔고 Reddit은 접근조차 못 했다. **저술 시 "커뮤니티에서는"과 "업계에서는"을 절대 혼용하지 말 것.**

자발적 도입 성공 목소리도 기록: **"my implementation speed used to be a bottleneck...and now only thoughts and idea are the limit"** — `Aperocky`, 2026-03-27.

---

## 축 4 — 변화관리

### 2-4-1. 관점 A: 저항의 원인은 도구가 아니라 이익 분배다

**이 책 변화관리 파트에 대한 가장 아픈 반론이자, 가장 중요한 진단.** `[커뮤]`

> **"You work the same hours, but you're more tired, and the company pockets the profits"**
> ("일하는 시간은 같은데 더 피곤해지고, 이익은 회사가 챙긴다.")
> — `pron`, HN, **2026-03-28**, https://news.ycombinator.com/item?id=47549649

보강:
- **"as the individual productivity gets increased the amount of FTE per project goes down, and superfluous folks shown the door"** — `pjmlp`, 2026-03-27
- **"Reduction in employees is a primary way to do that. AI is the most promising way to reduce the need for employees."** — `ilaksh`, 2026-03-28

> **실무자가 AI를 거부하는 이유는 도구가 나빠서가 아니라 생산성 향상의 과실이 자기에게 오지 않는다고 믿기 때문이다.** 이 한 문장을 반박하지 못하면 어떤 체계도 안 굴러간다. **"변화관리로 사람을 함께 옮긴다"고 할 때, 옮겨진 그 사람에게 무엇이 남는지를 말하지 못하면 이 책의 변화관리 챕터는 설득 기법 매뉴얼로 읽힌다.**

### 2-4-2. 관점 B: 등록은 감시로 오해되기 가장 쉬운 조치다 — 그리고 그 비용은 실측된다

> **"all your prompts are tracked and easily viewable by whoever oversees it at your company"**
> — `smrtinsert`, HN, **2026-03-29** `[커뮤]`

> **변화관리 챕터의 오프닝 후보 1순위.** 이 책이 "에이전트를 등록하고 감사 로그를 남긴다"고 말할 때, 직원은 **자기 프롬프트가 감사된다**고 듣는다. **등록의 대상이 에이전트인지 사람인지를 명확히 갈라주지 못하면 이 책은 감시 매뉴얼로 읽힌다.**

**가장 입체적인 증언** — `lollobomb`(HN, 2026-05-07): 동료들이 자신 있게 결함 있는 산출물을 쏟아내는 사이 자신은 그걸 검토하느라 압도됐고, 리더십은 **"we should collaborate and embrace AI in all our workflows, or we will be left behind"** 라며 **AI 사용에 대한 의무 생산성 보고**를 요구했다. 시니어인데도 빠질 수 없다고 느꼈다. → **감시·압박·소외·검토 부담이 한 사람 안에서 동시에 일어난다.**

**실증 근거 — 감시로 인식되는 순간의 대가:** `[논문]`
- **Kellogg, Valentine & Christin (2020), *Academy of Management Annals* 14(1), 366–410** `[PR]` — 알고리즘 통제를 Edwards의 **"쟁투의 장(contested terrain)"** 관점으로 종합. 작업장 알고리즘 통제의 여섯 기제 **"6 Rs"**.
  > **✅ B8 해소 (2차, PDF 원문 대조 완료).** **6 Rs = `restricting` · `recommending` · `recording` · `rating` · `replacing` · `rewarding`.**
  > ⚠️ **주의:** 중간에 WebFetch가 네 번째를 **"Ranking"으로 환각**한 적이 있다. **`rating`이 맞다.** 서지: *Academy of Management Annals* **14(1), 366–410**, DOI 10.5465/annals.2018.0174.
  > **이 책의 가장 위험한 지점을 정면으로 비추는 문헌:** "에이전트를 등록하고 로그를 남긴다"는 설계는 **알고리즘 통제 장치와 기술적으로 구별되지 않는다.** 로그는 감사에도 쓰이고 감시에도 쓰인다. 그리고 프레임의 요지는 **"통제는 늘 쟁투의 장"** — 즉 등록 체계 도입은 기술 프로젝트가 아니라 **협상**이다.
- **전자적 성과 모니터링(EPM) 메타분석** — Ravid et al. (2023), *Personnel Psychology*, DOI: 10.1111/peps.12514 `[PR]` ⚠️ (B3: "94개 표본/23,461명" 수치의 귀속 미확정)
  - **EPM이 노동자 성과를 개선한다는 증거는 없다**
  - EPM의 존재는 모니터링 특성과 무관하게 **노동자 스트레스 증가와 연관**
  - **전자 모니터링과 반생산적 업무 행동(CWB) 사이에 정적 관계**
  - 처방: **더 투명하고 덜 침습적으로 모니터링하는 조직은 더 긍정적 태도를 기대할 수 있다**
  > **⚠️ 외삽 경계:** 이건 **사람 모니터링 연구이지 에이전트 로깅 연구가 아니다.** 그러나 **직원이 에이전트 로그를 자기 감시로 인식하는 순간** 이 결과들이 그대로 발동한다는 것이 요점이다.
- **Cornell 연구 (SHRM 보도)** `[웹]` ⚠️ **원 논문 미확인 (C7)** — 알고리즘 감시는 **자율성이 줄었다는 인식**을 만들고, **불평 증가·성과 저하·이직 의사**를 늘렸다. 직원은 어떤 감시에도 부정적이지만 **AI에 의한 감시는 특히 더 큰 저항**을 낳는다.
  > **핵심 반론 방어:** **등록을 감시가 아닌 것으로 설계해야 하는 이유가 정서가 아니라 성과 문제임을 입증한다.**

**갈림의 조건은 수치로 나와 있다** `[웹]` ⚠️ **C5 — Pew(2023-04-20)만 1차, 나머지는 집계 사이트 경유. 재확인 필요:**
- **77%** — 사전에 알려주고 무엇을 수집하는지 투명하게 밝히면 모니터링에 덜 우려하겠다
- **90%** — 데이터 수집이 **커리어상 이익과 연결된다면** 수용하겠다
- **22% vs 74%** — 자신이 모니터링당하는 줄 **아는** 직원(22%) 대 실제 추적 도구를 쓰는 미국 고용주(74%) → **이 격차가 반발의 뿌리**

> **PART 4의 뼈대 — 에이전트 등록 커뮤니케이션 체크리스트로 그대로 전환:**
> ① **사전 고지** (발견당하지 않게 하라) ② **수집 범위 명시** (무엇을 보고 무엇을 안 보는지) ③ **당사자 이익과 연결**

**기술적 해답의 형태** `[커뮤]`: `XuebinMa`의 agent-guard 구현 — **정책 판단 단계와 감사 기록 단계를 파이프라인으로 물리적으로 분리**한다.
> **"'`invocationReason`/`userIntent` are not authorization evidence' isn't a doc promise here — it's enforced by which pipeline stage can see them."**
> — GitHub MCP PR #2817, 2026-05-30

### 2-4-3. 관점 C: 매니저를 세우는 것만으로는 감독이 되지 않는다

**이 책의 등록 설계에 대한 가장 날카로운 비판이자, 그 설계를 정교하게 만드는 재료.** Green (2022), *Computer Law & Security Review* 45 `[PR]` `[논문]` ★ (Future of Privacy Forum 수상)

**41개 정책** 조사 결과 두 가지 결함:
1. **증거에 따르면 사람들은 요구되는 감독 기능을 수행할 능력이 없다.**
2. 그 결과 **인간 감독 정책은 결함 있고 논쟁적인 알고리즘의 사용을 정당화(legitimize)하면서 근본 문제는 다루지 않는다.**

> 원문: 인간 감독 정책은 **"알고리즘 채택에 대한 잘못된 안전감(a false sense of security)을 제공하고, 벤더와 기관이 알고리즘 피해에 대한 책임을 회피(shirk accountability)하게 만든다."**
> 대안: 규제의 중심 기제를 **인간 감독(human oversight)에서 제도적 감독(institutional oversight)으로 전환**하라.

> **이 책이 반드시 다뤄야 할 것:** 사람 한 명을 승인자로 세워놓는 것은 **책임 세탁(accountability laundering)** 이 될 수 있다 — 사고가 나면 "승인자가 있었다"로 방어하고, 실제로 그 승인자는 판단할 능력도 시간도 없었다. **Green의 대안(제도적 감독)은 이 책의 방향과 오히려 일치한다 — 개인 감독자가 아니라 등록·로그·감사라는 제도로 감독을 구성하라.** 이 논문을 정면으로 다루면 이 책의 설계가 순진하지 않다는 것을 증명할 수 있다.

**왜 감독이 실패하는가 — 인지 근거:** Skitka, Mosier & Burdick (1999), *IJHCS* 51(5), 991–1006 `[PR]` `[논문]`
- **자동화 편향(automation bias)** = 자동화를 "**a heuristic replacement for vigilant information seeking and processing**"로 쓰는 경향
- 결과: **비자동화 조건의 참가자가, 매우 신뢰할 만하지만 완벽하지는 않은(very but not perfectly reliable) 자동화 보조를 받은 참가자보다 모니터링 과제에서 더 나은 성과를 냈다.**

> **이 책의 인간 감독 설계에서 가장 중요한 한 문장: "거의 항상 맞는 시스템이 가장 위험하다."**
> 에이전트가 95% 맞으면 사람은 검토를 멈춘다. 오히려 70% 맞는 에이전트가 더 안전하게 감독된다. **에이전트 성능 향상이 감독 품질을 떨어뜨린다**는 역설이며, 등록 체계가 **성능 지표와 감독 강도를 함께** 관리해야 하는 이유다.
> ⚠️ 1999년 항공 시뮬레이션 연구. 현대 LLM의 오류 양상(그럴듯한 환각)은 **더 탐지하기 어렵다**는 방향으로 다르다.

**세 겹의 처방:**
1. **제도적 감독** — 개인이 아니라 등록·로그·감사로 감독을 구성 (Green 2022)
2. **감독자의 오류를 전제한 설계** — **"불신의 제도화(institutionalisation of distrust)"**, 구성적/교정적 권한 등급 분리 (Laux 2023)
3. **인지적 강제 기능(cognitive forcing functions)** — 승인 버튼이 아니라 실제 검토를 유도하는 워크플로 (Buçinca, Malaya & Gajos 2021, *PACM HCI* 5(CSCW1) Art.188 `[PR]`). 예: 에이전트 결론을 보여주기 전에 사람이 먼저 자기 판단을 적게 하기, 일정 시간 지연 후 노출. ⚠️ B9: 효과 크기 미확보.

**⚠️ 함께 기록할 반전:** Bansal et al. (CHI 2021)은 **AI 설명이 팀 성과의 상보성을 높이지 못했고, 오히려 정답 여부와 무관하게 권고 수용률을 높이는 경향**이 있었다고 보고한다. **"설명을 붙이면 감독이 나아진다"는 통념에 대한 정면 반박.** ⚠️ A17: 정확한 서지 미확인.

### 2-4-4. 관점 D: 수용 성향은 조직의 고정 속성이 아니라 설계 변수다

**알고리즘 혐오 vs 알고리즘 선호 — 반드시 병기.** `[논문]`

| 근거 | 결과 | 조건 |
|---|---|---|
| Dietvorst, Simmons & Massey (2015), *JEPG* 144(1) `[PR]` | **알고리즘 혐오** — 오류를 본 뒤 열등한 인간을 선택 | **알고리즘이 틀리는 것을 본 뒤**, 자기 인센티브를 거는 선택 (5개 연구) |
| Logg, Minson & Moore (2019), *OBHDP* 151 `[PR]` | **알고리즘 선호** — 조언이 알고리즘 출처일 때 더 따름 | **일반인(lay people)**, 조언 수용 상황 |
| Dietvorst et al. (2018), *Management Science* 64(3) `[PR]` | **수정 권한을 주면 혐오가 크게 줄고 성과도 개선** | **수정 폭이 심하게 제한돼 있어도 효과 유지** |

**갈리는 이유:** (a) 오류를 목격했는가 (b) 조언인가 대체인가 (c) 판단자가 자기 전문성을 걸고 있는가. Logg의 후속 방향은 **전문가는 알고리즘 조언을 덜 따른다**는 것이므로, 조직 내 전문가 집단에는 Dietvorst 쪽이 더 가깝다. ⚠️ B10: 후속 서지 미확인.

**AX 롤아웃의 가장 잔인한 함정 (Dietvorst 2015):** 원문 — "people **more quickly lose confidence in algorithmic than human forecasters after seeing them make the same mistake**."
> 파일럿에서 에이전트가 **한 번 틀리는 순간** 조직의 신뢰가 비대칭적으로 무너진다. 실무 함의: **에이전트의 오류율을 사람의 오류율과 나란히 공개**하지 않으면 에이전트만 불공정하게 심판받는다.

**가장 실행 가능한 설계 원칙 (Dietvorst 2018):** 원문 — 참가자는 "**considerably more likely to choose to use an imperfect algorithm when they could modify its forecasts**, and they **performed better as a result**" — "**even when participants were severely restricted in the modifications they could make**"에도 유지.
> **에이전트 도입 시 사용자에게 아주 작은 수정 권한이라도 주라.** 수정 폭이 실질적으로 무의미할 정도로 작아도 수용률이 오르고 **실제 성과도 개선된다.** → **"human-in-the-loop"를 형식적 승인 버튼이 아니라 수정 권한으로 설계해야 하는 이유.** 그리고 등록 체계와 연결하면: **에이전트의 권한 스펙에 "사용자 수정 가능 구간"을 명시 필드로 넣어라.**
> **⚠️ 긴장:** "약간의 수정 권한"이 실제 조직에서 **책임 소재를 흐리는 부작용**을 낳을 수 있다 (사용자가 수정했으니 사용자 책임?). 이것은 축 1의 책임 귀속과 충돌한다. **이 긴장을 등록부의 권한 필드에서 명시적으로 해소하는 것이 이 책의 설계 과제다.**

### 2-4-5. 관점 E: 정체성 위협을 다루는 두 지렛대 — 그리고 "문화"는 안 먹혔다

Shonhe & Min (2025), *AI & Society* 40(5), 4079–4092 `[PR]` `[논문]` — 동·남부 아프리카 기록·정보 관리(RIM) 전문가 **413명** 설문
- **RIM 문화는 직업 정체성 위협(PIT)이나 AI 사용 의도에 유의한 영향을 주지 못했다**
- 반면 **XAA(설명 가능한 AI)와 강한 AI 정체성이 PIT를 줄이고 AI 채택을 높이는 데 결정적이었다**

> **실무 함의:** 두 지렛대는 **(1) 설명 가능성**(에이전트가 왜 그렇게 했는지 보여주기), **(2) AI 정체성 형성**(자기 개념 안에 AI 사용을 통합하도록 돕기). 그리고 **문화(조직 차원의 일반적 정보관리 문화)는 효과가 없었다**는 음성 결과가 실무적으로 중요하다 — **"문화를 바꾸자"는 슬로건이 아니라 개인 수준의 정체성 작업이 먹힌다.**
> **⚠️ 외삽 경계:** 단일 직군·단일 지역·자기 보고·횡단 연구. 한국 조직에 옮기려면 조심할 것. **인용 시 반드시 표본 특성을 밝혀라.**

**롤아웃 순서 설계에 직결되는 정합성:** 확인된 패턴 — **경험이 적은 전문가는 증강형(augmentative) AI에서 이득을 보는 반면, 시니어는 대체(substitution)를 기존 자율성과 전문성에 대한 위협으로 인식하는 경우가 더 많다.** 이것은 축 3의 이질성 발견(경험 적을수록 생산성 효과 크다)과 **정확히 겹친다.**
> **즉 효과가 큰 집단과 저항이 작은 집단이 같다.** ⚠️ 개별 논문 미특정 — 패턴 서술로만 쓸 것.

**현장의 정체성 훼손 증언** `[커뮤]`:
- **"most engineers got rebranded as 'not AI talent.' And then came the final insult"** — `beloch`, HN, 2025-12-03 ⚠️ 익명(특정 기업 조직 개편)
  > **조직을 AI 기준으로 재분류하는 순간 무슨 일이 생기는가.** 이 책이 "에이전트에 사번을 준다"고 할 때 **사람들이 자기 사번의 의미가 흔들린다고 느낄 수 있다**는 점.
- 기술 위축: 압박과 도태 공포가 과도한 AI 의존으로 이어지고 **"dependence and progressive atrophy of the skills they once had"** 로 간다 — `joestrouth1`, HN, 2025-11-26

### 2-4-6. 관점 F: 인기 있는 프레임이 검증된 프레임은 아니다

**이 책이 변화관리를 다루는 태도 자체를 규정하는 논문.** Hughes (2011), *Journal of Change Management* 11(4), 451–464 `[PR]` `[논문]` ★

"조직 변화 이니셔티브의 70%가 실패한다"는 수치의 **가장 저명한 출처 다섯**을 추적했다 — **Hammer & Champy, Beer & Nohria, Bain & Company 기사, McKinsey 기사, 그리고 Kotter.** 각각의 경우 **출처가 증거 없이 그 숫자를 진술했거나, 증거 없이 그 숫자를 진술한 다른 출처를 인용**하고 있었다.

> 원문: "whilst the existence of a popular narrative of 70 percent organizational change failure is acknowledged, **there is no valid and reliable empirical evidence to support such a narrative.**"

> **AX 문서와 컨설팅 자료에 "변화의 70%는 실패한다"가 그대로 복사되어 다닌다. 이 책이 그것을 인용하지 않고 왜 인용하지 않는지 밝히는 것만으로도 다른 책들과 구별된다.**

**Kotter/ADKAR의 실증적 지위 — 안전한 논지:**
- **"Kotter를 쓰지 말라는 게 아니라, Kotter가 실증 검증된 예측 모델이라고 믿지 말라는 것."**
- Kotter 비판 세 갈래: (a) **선형적**이며 실제 변화는 선형이 아니다 (Kotter Inc. 자신도 *Accelerate*에서 단계를 동시적인 것으로 재구성하며 사실상 인정) (b) **탑다운**이어서 리더가 할 일은 강하지만 나머지가 변화를 어떻게 경험하는지는 얇다 (c) 개인 수준의 정서적 여정을 다루지 않는다
- **대안: Klein & Sorra (1996)** — 후속 실증 검증이 이루어진 이론 (§1-6)
- ⚠️ **C4:** "Kotter가 분석했다는 100개 이상 기업이 표본으로 문서화된 적 없다", "일화적 증거에 기반" 등의 진술은 **블로그·컨설팅 사이트 주장**이며 학술 확인 실패. **Hughes(2011) 피어리뷰 근거 위에서만 논할 것.**
- ⚠️ **A13 (확인 강력 권장):** 「Why Vilifying the Status Quo Can Derail a Change Effort: Kotter's Contradiction, and Theory Adaptation」, *JCM*, DOI: 10.1080/14697017.2022.2137835 — **Kotter의 1단계("위기감 조성")가 역효과를 낼 수 있다**는 이론적 반박. AX 도입에서 "안 하면 도태된다"는 위기 프레임을 남발하는 실무 관행에 직접 적용된다.

**ADKAR 쪽에서 건질 것** `[웹]` ⚠️ **C3 — Prosci 수치 원문 미열람. 재확인 필요:**
- ADKAR 5요소: Awareness → Desire → Knowledge → Ability → Reinforcement. **AI 도입이 멈추면 대개 이 중 하나가 빠져 있다.**
- Prosci 1,107명 연구: AI 구현 난이도의 **약 38%가 사용자 숙련도**, **약 16%가 기술적 문제** → **사람 문제가 기술 문제의 2배 이상** ⚠️
- **가장 저항이 큰 집단은 중간관리자**, 다음이 현장 직원 ⚠️
- **직원 저항의 1위 이유는 결정의 이유를 이해하지 못하는 것** ⚠️

> **중요:** 이 책이 다루는 탑다운 전향에서 중간관리자는 **집행 주체이자 최대 저항 세력**이다. 그리고 저항 1위 이유가 "이유를 모름"이라는 점은 **"왜 등록하는가를 먼저 말하라"** 와 정확히 맞물린다.
> **⚠️ 용어 충돌 주의:** "스폰서십"이 축 1의 Entra sponsor와 우연히 겹친다. **변화관리의 스폰서 = 임원 후원자 / 에이전트의 스폰서 = 사업 책임자.** 저술 시 구분하되, **이 우연은 좋은 수사가 될 수 있다 — 둘 다 "누가 책임지는가"의 문제다.**

### 2-4-7. 관점 G: 무엇이 수용을 갈랐나 — 확보량은 적지만 방향은 명확하다

> **"providing tools that we aren't forced to use...letting adoption proceed organically"**
> — `caconym_`, HN, **2025-12-03** (같은 사람이 앞에서는 마이크로소프트를 비판했고, 자기 회사에서는 잘 되고 있다며 그 차이를 설명한 대목) `[커뮤]`

**한국 쪽 관찰:** **"구성원의 자율성을 장려하는 문화에서만 상향식 AI 도입이 가능함"**, **"AI는 조직의 기능 장애를 가속함"** — GeekNews topic 33050 GN⁺ 요약 (2차 인용, 원 HN 댓글 미확인 ⚠️)
> **"AI는 조직의 기능 장애를 가속한다"는 이 책 전체의 부제가 될 수 있는 문장.** 다만 2차 인용이므로 원문 확인 필요.

**현장에서 통한 것 (세 곳에서 독립적으로 같은 결론):**
1. **강요하지 않고 도구를 제공하고, 유기적 확산을 기다린다** (`caconym_`, 2025-12-03) — 다만 이 책의 주장과 긴장 관계
2. **AI 사용량을 성과 지표로 삼지 않는다** (`brainer` GeekNews ≈2026-08, `caconym_` 2025-12-03, `plaguuuuuu` 2026-06-28)
3. **활동량·도구 사용률이 아니라 실제 결과를 보상하고, 실패 시 책임자를 찾는 대신 원인을 배우고 시스템을 개선한다** (GeekNews topic 33050)
4. **사용량은 ROI와 상관이 없다** — ⚠️ **인용 금지 (2026-09-06 정정).** 아래는 **GN⁺ 단독 근거**이고, GN⁺는 **사이트 AI가 HN·Lobsters를 요약한 봇 글**이다(§9-10 방법론 함정). **"한국 반응"으로 인용하면 R0-14 위반**이며, 위 1~3번과 묶어 **"여러 곳에서 독립적으로"로 승격시켜도 R0-14 위반**이다. 이 명제에 논증 하중을 싣지 말 것:
   > **"사용량은 가치 있는 산출물이나 투자수익률(ROI)과 상관관계가 없음. 이 글은 실제 근거도 없이 고객이 ROI를 얻고 있다고 홍보하려는 어설픈 시도로 보임"** — GN⁺, GeekNews topic 32661, ≈2026-08-19 ⚠️ **봇 요약**
5. **개인의 향상이 조직 학습으로 자동 전이되지 않는다** — 전이 경로 설계가 별도 과제 (GeekNews topic 29217)

### 2-4-8. 관점 H: HR적 파장 — 조직도, 헤드카운트, 예산

**Lattice 사례 (축 1 × 축 4 교차, PART 3·4를 하나로 묶는 축)** `[웹]` △
- **2024-07-09 발표 → 2024-07-12 철회. 3일.**
- CEO Sarah Franklin이 나열한 항목: "'digital workers' will be securely **onboarded, trained, and assigned goals, performance metrics, appropriate systems access, and even an accountable manager.**" ⚠️ **A7: LinkedIn 원 게시글 미확인 — 직접 인용 시 확인하거나 간접화법으로.**
- 철회 성명: "This innovation sparked a lot of conversation and questions that have no answers yet... will not further pursue digital workers in the product."

> **변화관리 관점의 독법 — 이 책의 가장 중요한 실무 교훈:**
> 기술적으로 Lattice가 하려던 일과 2026년 Microsoft/Okta가 실제로 한 일은 **거의 같다**(신분·소유자·접근권·책임자 부여). 그런데 Lattice는 3일 만에 철회했고 MS/Okta는 GA했다. **차이는 프레이밍과 배치 장소다** — Lattice는 **HR 시스템(사람의 자리)** 에, MS/Okta는 **IAM(계정의 자리)** 에 넣었다. Lattice는 **HR 회사**였기에 더 크게 다쳤다.
> **→ 에이전트를 조직에 등록하되, 사람의 자리에 앉히지 마라.** PART 3의 설계 원칙이자 PART 4의 커뮤니케이션 원칙.

**비용 회계 — 인건비인가 IT비용인가** `[웹]` ✗ (닛케이 유료 구간, 표제·리드만 확인)
- 닛케이 **2026-07-09**: 「社員と化すAIエージェント、費用は人件費？ 人事とITの境界溶かす」(사원이 되어가는 AI 에이전트, 비용은 인건비? 인사와 IT의 경계를 녹이다)
- 리드 인용 가능: 「人が細かく指示しなくても、ゴールまでの道筋を自ら考えて実行し、夜間や休日も関係なく業務を進める、まさに社員」
- **⚠️ 본문 미확인 — 구체 기업명·수치 없음.** "닛케이가 2026년 7월 이 주제를 표제로 다뤘다" 수준으로만 쓰고 구체 주장은 하지 말 것.

**리더십 정합성 문제:** **65% vs 31%** (경영진이 부하직원의 2배 이상 미승인 AI 도구 사용, §2-3-4)
> **변화관리에서 "먼저 규칙을 지켜야 할 사람이 안 지킨다"는 구조적 문제.** 탑다운 전향의 첫 단계는 실무자 교육이 아니라 **리더의 자기 규율**이라는 논거.

**⚠️ 리스킬링 수치 — C9/C10:** RAISE US($500M 이상 확보, 2026-06-25), Meta America's Workforce Academy($1억 1,500만 달러) 등은 **집계 매체(TechTimes 등) 경유**다. **공식 발표 페이지 확인 후 사용.** 특히 **"AI가 87,714개 일자리를 없앴다"는 근거가 취약하므로 쓰지 말 것.**

**추진자(이 책의 1순위 독자)의 좌표** `[커뮤]`: 회사는 개발자의 자율성을 자랑하지만, **AI 도입을 추진할 때마다 규정 준수 요구와 "현대판 러다이트" 분위기에 막힌다.** (GeekNews topic 21037 요약, 2차 ⚠️)
> **위(컴플라이언스)와 아래(반발) 사이에 끼인 추진자.** 이 책 도입부의 인물 설정에 바로 쓸 수 있다.

**커뮤니티가 만든 조어 (인용 가치 높음):** **"aimless tokenmaxing"**(목적 없는 토큰 극대화) — `827a`, HN, 2026-05-22. **이 책이 반대하는 것의 이름.**

**깊은 논점 하나:** **"AI is like an energetic intern who knows his place on the totem pole and wants to please"** — `ryandrake`, HN, 2026-03-28.
> 경영진이 AI를 좋아하는 이유가 성능이 아니라 **순응성**이라는 지적. 이 책이 "에이전트를 조직원으로 등록한다"고 할 때, 그 조직원이 **절대 반대하지 않는 조직원**이라는 사실이 조직에 무엇을 하는가.

---

# 3. 대표 사례

## 3-1. 【핵심】 에이전트를 조직에 등록한 실제 사례

> **BLOCKING 규율:** "실제 시행 여부" 컬럼이 이 표의 존재 이유다. **보도자료 수준의 발표를 운영 사례로 오인하면 책의 신뢰가 무너진다.**

| 조직 | 무엇을 등록했나 | 식별자 형태 | 권한 모델 | 감사·폐기 | 출처 URL | 발행일 | **실제 시행 여부** |
|---|---|---|---|---|---|---|---|
| **Deutsche Bank** (독일·은행) | RPA+AI 봇 **Blue Bot 'Yi'** 를 Corporate Bank의 "digital employee"로 온보딩 | **사번(employee number) + 전용 업무 이메일 주소** | 기사에 명시 없음 ⚠️ | 기사에 명시 없음 ⚠️ | db.com/news/detail/20200720-... | **2020-07-20** | **운영 중** (2020년 발표 시점 기준 / **2026년 현재 존속 여부 ⚠️ 미확인**) |
| **Microsoft** (자사 IT) | Agent 365로 사내 에이전트를 사용자·앱·디바이스와 같은 관리 인프라에 편입 | Entra Agent ID | **Owner / Sponsor / Manager 3역할** | **소프트 삭제 + 캐스케이드 정리 + 스폰서 승계 워크플로** | microsoft.com/insidetrack/blog/deploying-microsoft-agent-365-... | 2026 (정확일 ⚠️) | **제품 기능(GA) + 자사 적용** |
| **Goldman Sachs** (미국·IB) | Cognition의 자율 코딩 에이전트 **Devin**을 "hybrid workforce"의 일원으로 배치 | **사번 부여 여부 ⚠️ 미확인** — 보도의 "employee #1"은 **매체 수사** | 인간 개발자 감독 하, "on behalf of our developers" | 명시 없음 ⚠️ | cnbc.com/2025/07/11/... (✗ HTTP 403) | **2025-07-11** | **파일럿** (CIO Marco Argenti, 12,000명 개발조직, 수백 인스턴스로 시작) |
| **Lattice** (미국·HR SaaS) | "digital workers"에게 **공식 employee record** — 조직도 편입, 목표·성과지표·시스템 접근권·책임 매니저 | HRIS 상의 정식 employee record | "appropriate systems access" + "accountable manager" | — | shrm.org/... / fortune.com/2024/07/12/... | 발표 **2024-07-09** → 철회 **2024-07-12** | **발표만(보도자료) → 3일 만에 철회. 제품 반영 안 됨** |
| **일본 기업** ("AI社員") | 에이전트 비용을 **인건비로 계상**하는 기업 등장, 인사-IT 경계 소멸 | — | — | — | nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ (✗ 유료) | **2026-07-09** | **⚠️ 부분 확인** — 표제·리드만 검증 |
| **한국 은행권 RPA** | RPA 로봇에 사번 부여 | — | — | — | — | — | **⚠️ 미확인 — 공개 출처로 확인 실패. 본문에 쓰지 마라** |

### 표에 대한 저술 규율 (BLOCKING)

1. **Deutsche Bank Blue Bot 'Yi' 는 확인된 유일한 "사번 부여" 1차 사례다.** 그리고 이것은 **2020년, LLM 이전, RPA 시대의 일이다.** "AI 에이전트에게 사번을 준다"의 **선례**로 쓰되, 생성형 AI 에이전트 사례로 둔갑시키면 안 된다.
   > 원문 인용 가능 (공식 보도자료 ★): "**Blue Bot 'Yi' is the Corporate Bank's first digital employee with a client-facing role. It has been allocated an employee number and has a dedicated working email address.**"
   > 세부: 상하이 Blue Water Fintech Space에서 RPA + 시맨틱 인식 + AI로 개발. 실시간 맞춤 거래 리포트, 캐시풀링 리포트, 고객 직접 문의 처리. 이름은 제작자 Zhu Yi(Head of China Innovation and Fintech Products)에서 따옴.
2. **Lattice는 성공 사례가 아니라 실패 사례다.** 이 책에서 가장 유용하면서 가장 위험한 소재다 (§2-4-8).
3. **Goldman Sachs가 Devin에게 사번을 줬다는 근거는 없다 (A-2).** "employee #1"은 매체 수사다. **"hybrid workforce에 배치된 파일럿"으로만 서술하라.**
4. **한국 은행권 "RPA 로봇 사번"은 검증 실패했다 (A-1).** 국내 은행 RPA 도입 자체는 다수 확인되나(KB국민·우리·NH농협·신한·IBK기업·부산은행), **사번/이름/계정 부여를 명시한 기사를 찾지 못했다. 기억이나 통념으로 쓰지 마라.**

## 3-2. 벤더 지형 — GA / 프리뷰 / 발표만 (2026-09-05 기준) 🕒

> **저술 규율:** 이 영역은 분기 단위로 바뀐다. **본문에 쓸 때 반드시 "2026년 중반 기준"으로 못 박아라.**

| 벤더·표준 | 제품·기능 | 상태 | 발표·GA일 | 신뢰성 |
|---|---|---|---|---|
| **Microsoft** | **Entra Agent ID** | **GA** | **2026-05-01** | ★ (공식 문서 열람) |
| Microsoft | Entra Agent ID 블루프린트·에이전트 생성 마법사 | **프리뷰** | 2026 | ★ |
| Microsoft | **Agent 365** (에이전트 레지스트리·통합 관제) | **GA**, $15/user/월(연약정) | 발표 2025-11-18(Ignite) / GA 2026-05-01 | ★(제품 페이지) / △(GA일·가격, B-7) |
| **Okta** | **Agent SSO** | **GA** (코어 SSO에 무상 포함) | **2026-08-24** | ★ (보도자료 열람) |
| Okta | **Cross App Access (XAA)** — OAuth 확장 | 발표 2025-06-23 → **MCP 공식 Enterprise-Managed Authorization 확장으로 채택** | 2025-06-23 / 2026-08-24 | ★ |
| **Auth0** (Okta) | Auth0 for AI Agents (Auth for MCP, Agent as Principal, On-Behalf-Of Token Exchange, Token Vault, FGA Permissions Index) | 2026-05 발표 (**GA/프리뷰 구분 ⚠️ 미확인**) | 2026-05 | △ |
| **CyberArk** | Secure AI Agents (권한 제어·발견·ZSP·감사·수명주기) | **GA** | **2025년 말** (정확일 ⚠️) | △ |
| **SailPoint** | Agentic Fabric (에이전트·NHI 발견·거버넌스, 아이덴티티 그래프) | 발표 2026-05-11, **"2026 여름 GA 예정"** 고지 → **현재 GA 여부 ⚠️ 재확인 필요 (B-4)** | 2026-05-11 | △ |
| **1Password** | Unified Access Pro (인간·머신·에이전트 통합 발견/보안/감사) | **GA** | **2026-03** | △ |
| Astrix / Oasis Security / Token Security / Britive / Descope / WorkOS | NHI·에이전트 아이덴티티 | **⚠️ 미확인** — 개별 GA 상태 검증 실패 | — | 하 |
| **Celonis × MS Agent 365** | 프로세스 인텔리전스 연동 + **Agent Mining** | **프라이빗 프리뷰** | **2026-05-01** | △ |

**Okta Agent SSO의 결정적 문장 (★ 원문 그대로):**
> "When such an agent connects to an enterprise application, Okta **registers it as a first-class identity in Universal Directory alongside human employees**, then issues **short-lived, identity-governed tokens** in place of stored credentials."

부가: 관리자가 **인간 직원과 동일한 콘솔·워크플로**로 에이전트 접근을 관리. 사전 통합 파트너 — Anthropic(Claude), Asana, Atlassian, Canva, Datadog, Figma, Glean, Linear, Notion, Slack, Supabase 등.
> 핵심 수치 (Okta *AI Agents at Work 2026*, n=경영진 292 + 지식근로자 492, 7개국): **"Only 34% of organizations apply the same security controls to AI agents as they do to human workers."**
> 보안 문제 보고자 중 **26.7%가 실제 사고**(유출·데이터 노출·시스템 장애), **31.2%는 사전 차단된 아차사고**.

**표준·프로토콜 지형** 🕒 △

| 표준 | 아이덴티티 관련 내용 | 상태 |
|---|---|---|
| **MCP Authorization** | MCP 서버 = OAuth **2.1** 리소스 서버. PKCE, Authorization Server Metadata, Protected Resource Metadata, **Resource Indicators(RFC 8707)** 의무화 | 2025-03-26 → 2025-06-18 → **2026-07-28 최대 개정** (§2-2-4) |
| **A2A (Agent2Agent)** | 각 에이전트가 **agent card**에 OAuth 2.0 / OIDC / mTLS 중 요구 인증 방식을 선언. **v1.0에서 signed agent card 추가** | Google 발표 2025-04-09 → Linux Foundation 기증 2025-06-23 → v1.0. 지원 조직 150+ |
| **SPIFFE / SPIRE** | 공유 API 키 대신 워크로드에 **암호학적 신분** 부여. HashiCorp Vault 1.21에 네이티브 SPIFFE 인증 추가 | 2025~2026 확산 |
| **AGNTCY / W3C DID** | — | **⚠️ 미확인** — 검증 실패 |

> **⚠️ 반론 10 (커뮤니티):** 관련 GitHub 이슈·PR이 **2026-09-05 기준 전부 open(미확정)** 이다. 특히 **SPIFFE 쪽은 댓글이 한 자릿수**(#382 3댓글, #383 0댓글, #408 2댓글)다. **"업계 표준이 이미 정해졌다"고 쓰면 안 된다.** 책은 특정 표준·제품에 못 박지 말고 **"표준이 정해지기 전에 조직이 무엇을 할 수 있는가"** 로 서술하라. 🕒 출간 시점에 반드시 재확인.

## 3-3. 제도 사례 — 국가가 이미 등록을 요구하고 있다

### (가) EU AI Act (Regulation (EU) 2024/1689)

**등록 의무 — Article 49** ★ (조문 정리 사이트 직접 열람)

| 항 | 내용 |
|---|---|
| **Art. 49(1)** | 고위험 AI **제공자(provider)** 는 시장 출시 전 **EU 데이터베이스에 자신과 시스템을 등록** (Annex III point 2 예외) |
| **Art. 49(2)** | Art. 6(3)에 따라 **"고위험이 아니다"라고 스스로 판단한** 시스템도 등록 대상 |
| **Art. 49(3)** | **배포자(deployer) 중 공공기관·EU 기관**은 서비스 개시 전 등록. → **민간 배포자는 현재 등록 의무 없음** (대신 Art. 26의 다른 의무) |
| **Art. 49(4)** | 법집행·이주·망명·국경관리 용도는 **비공개 보안 구역**에 등록 |
| **Art. 49(5)** | Annex III point 2 시스템은 **국가 단위 등록** |
| **Art. 71 / Annex VIII** | EU 데이터베이스의 근거 조문 / 등록 시 제출 정보(Section A/B/C) |

> **책에서의 쓰임새:** "국가가 AI 시스템에 **등록번호**를 요구한다"는 제도적 선례. 사내 에이전트 등록이 자의적 관료주의가 아니라 **규제가 요구하는 방향과 같은 방향**임을 보이는 데 쓴다. **단, 민간 배포자는 아직 EU DB 등록 대상이 아니라는 점을 정확히 써야 한다.**

**🕒【최우선 신선도 경보 — B-1】 고위험 의무 시행일이 실제로 연기됐다**

> **2025년 이전에 쓰인 대다수 자료(그리고 대다수 LLM의 기억)는 "2026-08-02 고위험 시행"을 말하는데, 이는 2026년 9월 현재 틀렸다.** 이 지점이 이 책 신선도 우위의 분수령이다.

**확정된 사실** (Gibson Dunn, **2026-05-27**, 직접 열람 ★):
- **Annex III 독립형 고위험 시스템 의무 → 2027-12-02 로 연기**
- **Annex I 규제 제품 내장 AI → 2028-08-02 로 연기**
- **변경되지 않은 것:** 금지 조항(Art. 5) **2025-02-02 시행 중** (누디파이어/CSAM 금지 추가), GPAI 의무(Art. 51~56) **2025-08-02 시행 중**
- **연기 사유: 정합표준(harmonized standards)의 지연** — 원래 일정대로면 기업이 확정된 기준 없이 준수를 입증해야 했다
- 경과: 2026-04-28 1차 삼자협상 결렬 → **2026-05-06 잠정 정치적 합의** → **2026-05-13 이사회 회원국 대표 확인**

**⚠️ 2차 출처로만 확인 (B-2 — Phase 4 fact-checker가 EUR-Lex로 대조 필요):**
- 규정 번호 **Regulation (EU) 2026/1744** ("Digital Omnibus on AI"), 관보 게재 **2026-07-24**, 발효 **2026-07-27**
- **B-3: Digital Omnibus가 Art. 49 등록 의무를 어떻게 조정했는지는 미확인**

> **저술 규율:** 반드시 **"2026년 9월 기준"** 으로 못 박고, **"고위험 의무는 2027년 12월로 미뤄졌다 — 다만 금지 조항과 GPAI 의무는 이미 시행 중"** 이라는 **두 겹**을 함께 써라. "AI Act가 통째로 미뤄졌다"는 흔한 오해다.

### (나) 미국 — OMB M-24-10 / M-25-21 + 실제 인벤토리

- **M-24-10**(2024-03) → **M-25-21**(**2025-04-03**)로 **폐지·대체** `[웹]` △
- **Chief AI Officer(CAIO)** 를 60일 내 지정, **AI Governance Board** 를 90일 내 소집
- **연례 AI use case inventory** 작성 → OMB 제출 → **공개 가능한 항목은 기관 웹사이트에 게시**. 실물 예: `justice.gov/ai/ai-inventory`

**【결정적 사례 — 등록부는 어떻게 실패하는가】** `[논문]` ⚠️ **C2: 시민사회 분석(CDT) + 언론 보도. 학술 논문 아님 — 출처 성격 명시 필수. 원자료는 GitHub `ombegov/2025-Federal-Agency-AI-Use-Case-Inventory` 공개.**
- **2025년 연방기관 AI use case inventory: 56개 제출 기관에서 3,611건** — 2024년 1,757건 대비 **105% 증가**
- 그러나 다수 인벤토리가 **일관성 없는 문서화와 필수 리스크 관리 관행 준수에 대한 불충분한 세부 정보**를 담았다
- 리스크 관리 관행의 **면제·연장에 대한 공개 보고는 압도적으로 희소**했고, **국토안보부(DHS)만이 연장 기간에 대한 구체 정보를 포함**했다
- **고영향 use case**는 이론상 배포 전 테스트·영향 평가·모니터링·이의제기 정보를 제공해야 하지만 **실무에서는 불완전**하다

> **이 책의 등록 설계가 "필드를 만드는 것"에서 멈추면 똑같이 된다는 경고. 등록부의 실패 모드는 "등록이 안 되는 것"이 아니라 "등록은 되는데 알맹이가 비는 것"이다.**

### (다) 중국 — 알고리즘 등록제(算法备案) + 생성형 AI 잠행 조치

| 시점 | 수치 | 출처 |
|---|---|---|
| 2025-03-31 | 생성형 AI 서비스 **346건** CAC 등록 완료 | 국무원 신문판공실, 2025-04-09 |
| 2025-08-31 | 생성형 AI 서비스 **538건** 신고 + 애플리케이션 등록 **263건** = **801건** 승인 | △ |
| 2025-11 | 국가 등록 플랫폼 누적 알고리즘 **5,822건**, 그중 **67.3%가 생성형 AI** 관련 | △ |

제도: **생성형 인공지능 서비스 관리 잠행 조치(2023)** — 신고 및 안전 평가, 모델 유형·데이터셋 출처·리스크 완화 조치·**지정 책임자(designated responsible personnel)** 공개 의무.

> **이 책 축 1의 가장 세련된 논증:** **"지정 책임자"** 라는 요구는 Entra의 sponsor, NIST의 named risk acceptance와 **같은 것을 다른 언어로 말한다.** **제도와 제품이 독립적으로 같은 결론에 도달했다.**

### (라) 한국 — AI 기본법 (이 책 독자에게 가장 직접적인 압력)

- 정식명: **인공지능 발전과 신뢰 기반 조성 등에 관한 기본법**, 시행 **2026-01-22** `[웹]` △ ⚠️ **A-6: 조문 번호 미확인 — 국가법령정보센터 원문 대조 필수**
- **고영향 인공지능** 및 **생성형 인공지능** 사업자에 구체적 책무 부과
- **투명성 확보 의무:** 고영향 AI 또는 생성형 AI 활용 제품·서비스 제공 시 **AI 기반 운영 사실을 이용자에게 사전 고지**
- **안전성 확보 의무**
- **의무 주체의 범위:** 모델을 만드는 회사만이 아니라 **남이 만든 AI를 이용해 제품·서비스를 제공하는 회사까지 포함한 "인공지능사업자"**
- **계도 기간:** 시행 후 **최소 1년 이상** → 2027-01 무렵까지 ⚠️ **B-8: 정확한 종료 시점 미확인**

> **핵심:** **"우리는 AI를 만들지 않고 쓰기만 하는데요"가 면책이 아니다.** 이 책이 말하는 등록·기록의 실무적 근거가 된다.

**개인정보보호위원회** `[웹]` △: 「생성형 AI 개발·활용을 위한 개인정보 처리 안내서」(**2025-08-06**) / 「생성형 AI 서비스 이용자를 위한 개인정보 보호 가이드」(2026-05 발간) — 데이터 수집 → AI 학습 → 서비스 이용 → **외부 서비스 연동** 4단계로 처리 지점 구분(마지막 단계가 에이전트·MCP 시대의 쟁점) / 2026년 업무 추진계획: 사전적정성 검토제를 **기획 단계부터** 운영, AI 합성콘텐츠 삭제 요구권 신설 계획.

### (마) NIST AI RMF 1.0 (2023-01) / ISO/IEC 42001:2023

**NIST AI RMF** `[웹]` △ — **GOVERN = 누가 책임지는가 / MAP = 무엇에 대해 책임지는가**
- 역할·책임 정의에 **AI 시스템 오너(AI system owner)** 와 모델 리스크 오너 포함, GOVERN 요구사항에 대한 명확한 책임 귀속과 **그 책임의 문서화된 수용(documented acceptance)** 요구
- MAP은 운영·조달하는 **모든** AI 시스템에 대해 문서화된 컨텍스트, 리스크 분류, 영향 평가, **명명된 리스크 수용자(named risk acceptance)** 요구
- ⚠️ **A-5: 서브카테고리 번호에 출처 간 충돌이 있다** (GOVERN 1.6의 문구). **조문 번호를 쓰려면 NIST 원문·Playbook 직접 대조 필수.**
> **"named risk acceptance"** 라는 표현이 이 책의 '소유자' 개념과 정확히 맞물린다.

**ISO/IEC 42001:2023 (AIMS)** `[웹]` △ — Annex A는 **38개 참조 통제**, **9개 통제 목적(A.2~A.10)**. ISO 27001과 달리 **참조 세트**이므로 제외 사유를 **적용성 선언서(SoA)** 에 정당화해야 한다. AIMS 범위 설정 시 조직은 자신의 역할(provider/deployer)을 공식 규정해야 하고, 심사원은 **완전한 AI 시스템 인벤토리**를 요구한다. 자원 인벤토리는 코드뿐 아니라 **데이터·컴퓨팅·소프트웨어·사람**까지 포함.
- ⚠️ **A-4: 개별 Annex A 통제 번호(A.x.y)는 확인 실패 (표준 유료). 번호 인용 금지 — 구조(38통제/9목적)만 서술.**
- ⚠️ **인증 취득 기업 공개 사례 미확보.**
> **"인벤토리 + 소유권 + 수명주기"라는 세 단어가 이 책의 뼈대와 같다.** PART 2(SOP)와 PART 3(등록)을 잇는 다리.

## 3-4. 등록부는 만들 수 있다 — 실존 증명

**AI Agent Index** (arXiv:2502.01635, 2025-02) `[PP]` `[논문]` — 배포된 에이전틱 AI 시스템의 기술 구성·의도된 용도·안전 기능을 문서화한 **최초의 공개 데이터베이스**. 가장 널리 배포된 **30개 시스템**을 **6개 범주**(법적 사항, 기술적 역량, 자율성·통제, 생태계 상호작용, 평가, 안전)로 심층 기록.
> **외부 연구자도 30개 시스템을 6개 범주로 정리해냈다면, 조직이 자기 에이전트를 등록하는 것은 훨씬 쉬운 일이다. 6개 범주는 사내 등록 스키마의 초안으로 바로 쓸 수 있다.**
> ⚠️ **B1:** "공개 문서 70.1% / 코드 49.3% / 안전 정책 19.4% / 외부 안전 평가 <10%"라는 수치가 확인됐으나 **2025년판(2502.01635)인지 2026년판(2602.17753)인지 판별되지 않았다. 확정 후 인용할 것.** 확정만 되면 **"공시는 절반, 안전 정책은 5분의 1"** 이라는 강력한 수치가 된다.

**계보:** **Model Cards** (Mitchell et al., FAT* '19) — **intended use / out-of-scope use** 구분은 에이전트 권한 명세의 필드로 직수입 가능. ⚠️ 단 모델 카드는 **자발적 공시이며 강제력이 없다** — 발행률이 낮고 품질 편차가 크다는 후속 비판이 있다(위 AI Agent Index 수치가 그 증거). **"문서를 만들자"에서 멈추면 똑같은 운명이라는 경고로 쓸 것.**

**AI Incident Database** (McGregor, AAAI 2021) — 항공 같은 성숙 산업이 **실제 실패를 사고 DB에 축적**해 안전을 개선해온 계보. ⚠️ **B6: "1,000건 이상"은 2021년 기준 수치. 현재 숫자로 쓰면 오류.**
> **등록번호가 있어야 사고 기록이 쌓이고, 사고 기록이 쌓여야 안전이 개선된다.** Chan et al.의 tail number 비유와 이어진다. 사내에서도 **에이전트 사고 원장을 등록부와 같은 키로 묶어야 한다.**

## 3-5. 감사 오버헤드에 대한 정량 반박

**「Auditable Agents」** (arXiv:2604.05485, v1 2026-04-07 / v2 2026-08-13) `[PP]` `[논문]`
- 명제: **"no agent system can be accountable without auditability."**
- 감사 가능성 5차원 (**사내 감사 체크리스트로 그대로 사용 가능**): ① 행위 복구 가능성 ② 생애주기 커버리지 ③ 정책 검사 가능성 ④ 책임 귀속 ⑤ 증거 무결성
- **617 security findings** — 오픈소스 에이전트 프로젝트 **6개** 조사 결과. 감사 가능성의 기본 전제조건조차 생태계 전반에 구현되어 있지 않다.
- **8.3 ms median overhead** — 변조 탐지 가능한 기록 + 사전 실행 중재를 추가했을 때의 중앙값 오버헤드
> **"감사 붙이면 느려진다"는 현장 반론에 대한 직접 반증 수치.**
> ⚠️ **프리프린트다.** 617건은 6개 프로젝트 표본이며 선정 편향 가능. 8.3 ms는 특정 실험 환경 중앙값이므로 **"이 실험 조건에서"를 반드시 붙일 것.**

**정적 권한만으로는 부족하다** — Kaptein et al. (2026), arXiv:2603.16586 `[PP]` `[논문]`
> **"the execution path is the central object for effective runtime governance."**
> 정책 함수의 네 입력: **agent identity / execution history / proposed actions / organizational context**
> **"등록 = 정적 권한 부여"라는 순진한 그림을 깨준다.** 사번과 계정을 발급했다고 끝이 아니다 — "오늘 이미 3건 승인했으면 4번째는 사람 검토" 같은 정책은 런타임에서만 판정 가능하다. **조직 맥락이 정책 함수의 입력에 명시적으로 들어간다**는 점이 이 책의 주제와 정확히 맞는다.

## 3-6. SOP → 절차 전환의 실물 사례

- **Amazon Science 3모듈 프레임워크** (Clarifier / Planner / Implementor, 88.4%) — §2-2-2
- **SOP-Bench** (12도메인 2,000+ 과제) / **Agent-Ops** (이커머스 운영 end-to-end SOP 자동화) / **Agent-S** (arXiv:2503.15520) / **SOP-Maze** (arXiv:2510.08942) — §2-2-2
- ⚠️ **후속 확인 권장:** 「Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents」 arXiv:2607.11346 (2026-07) `[PP]` — **"SOP를 실행 가능한 프로그램으로 컴파일하고 능력 게이트 런타임에서 돌린다"는 접근은 이 책의 주제와 매우 가깝다.**
- **실행 가능한 런북:** Atuin Desktop — "문서처럼 보이지만 터미널처럼 실행되는" 로컬 우선 런북 편집기. 셸 명령·DB 쿼리·HTTP 요청을 한 곳에 두고 반복 운영 절차를 공유 가능한 워크플로로. (GeekNews topic 20489, **2025-04-23**) `[커뮤]`
  > **"SOP → 에이전트 절차"의 중간 단계로 실행 가능한 런북이 이미 존재한다.** 이 책의 진화 서사(문서 → 실행 가능 런북 → 에이전트 SOP)에 실물 근거를 준다.
- **BPM × LLM 학술 지형:** "By **2024–2025, generative AI approaches clearly surpass non-generative AI approaches**" — 실제 적용은 **발견(discovery)과 구현 단계, 특히 추출(extraction) 활동**에 집중. **RAG로 사내 문서·용어집·규정·프로세스 모델링 규칙을 끌어오는 연구**가 늘고 있다. ⚠️ 개별 논문 저자·게재처 미확정 — **추세 서술만 쓰는 편이 안전.**

---

# 축별 커버리지 — Phase 2 planner를 위한 공백 지도

> **planner에게:** 아래 "비어 있는 것"이 **설계 제약**이다. 사례가 없는 자리에 사례 기반 챕터를 배정하면 저술 단계에서 반드시 막힌다.

## 축 1 — 에이전트의 조직 등록

**확보한 것 (강함):**
사번 부여 1차 사례 1건(Deutsche Bank 2020, 공식 보도자료 ★) / 실패 사례 1건(Lattice 2024, 3일) / **Owner-Sponsor-Manager 3역할 설계 원본**(Entra 공식 문서 ★ — PART 3 뼈대로 즉시 사용 가능) / 오프보딩이 제품 기능으로 존재한다는 증거(soft-delete·cascade cleanup·스폰서 승계) / **"78%가 폐기 정책 없음"**(CSA 2026-05-20) / **"21%만 성숙 거버넌스"**(Deloitte, n=3,235, 24개국 ★) / 벤더 GA 타임라인 / 제도 4개 관할(EU Art.49 + **연기된 시행일** / 미국 M-25-21 + 실제 인벤토리 / 중국 등록 실적 / 한국 AI 기본법) / **학술 정본 3종**(Chan 2024 FAccT, Chan 2025 TMLR, Chan 2024 IDs) / 책임 귀속 이중 근거(Kolt 대리인 문제 + Santoni de Sio 네 공백) / **20년 조직 MAS 계보**(MOISE+ 2002, OperA 2004, electronic institutions 2001) / 감사 오버헤드 정량 반박(8.3ms) / **커뮤니티의 정면 반박 3종**(용어 리브랜딩·조직도 폭발·표준 미확정)

**비어 있는 것 (⚠️ 후속 필요):**
- ❌ **한국 사례 전무.** 국내 은행권 RPA 사번 부여 검증 실패. 한국 독자 설득력에 중요하므로 **별도 심층 조사 권고** (금융권 RPA 백서, 금융보안원 자료, 전자신문·디지털데일리 아카이브)
- ❌ **일본 구체 사례** — 닛케이 본문 유료
- ❌ **통신·제조·공공 산업의 등록 사례** — 확보 사례가 금융(DB, GS)·IT(MS)에 편중
- ❌ ISO 42001 Annex A 통제 번호 / NIST AI RMF 서브카테고리 번호 / 한국 AI 기본법 조문 번호
- ❌ Astrix·Oasis·Token Security·Britive·Descope·WorkOS의 개별 GA 상태 / AGNTCY·W3C DID
- ❌ **Entra Agent ID·Okta·Auth0를 실제로 써본 사람의 후기** — 커뮤니티 토론 스레드가 사실상 없다
- ❌ **라이선스 비용 우려의 직접 인용** — "에이전트마다 라이선스를 사야 하냐"는 실무 반응 미확보
- ❌ SPIFFE/SPIRE·VC/DID·confidential computing attestation의 **피어리뷰 평가** (표준 문서로 대체 필요)
- ❌ **Reddit 전체 접근 불가** — NHI 운영 고통의 날것 일화가 최대 광맥인데 통째로 비었다

## 축 2 — SOP에서 출발하는 체계 구축

**확보한 것:**
**적힌 절차 vs 실제 수행의 정본 이론**(Feldman & Pentland 2003 ASQ ★) / **형식화의 두 유형**(Adler & Borys 1996 ASQ) / **암묵지 논쟁 양쪽**(Nonaka 1994 ↔ Gourlay 2006) / 프로세스 마이닝 정본(van der Aalst) + conformance = 공학적 대조 / **MetaGPT**(ICLR 2024 Oral, SOP를 프롬프트 시퀀스로) / **SOP-Bench 정량 수치**(12도메인, 57~100%, "최신 모델이 낫다는 보장 없음") / Amazon Science 3모듈 + 88.4% / **AGENTS.md 계층 구조** / **MCP 인가 개정 3단계 + XAA의 MCP 공식 채택**(SOP↔등록 합류) / **Celonis Agent Mining** / Toyota 표준작업·ISO 9001 7.5 / **Confluence 냉소 5건 + 한국 2건** / **AI 생성 문서의 새 부패 2건(2026)** / 긴 규칙 파일 회의론 4건 + 반대 1건 / 컨텍스트 엔지니어링 휴리스틱 7건 / **RPA 회고 3건**

**비어 있는 것:**
- ❌ **암묵지 발굴 기법 미검증** (task mining, Scribe·Tango·Guidde) — 축 2의 가장 큰 구멍
- ❌ ⚠️ **B7 Adler & Borys의 enabling 형식화 4대 특성** — **이 책에 가장 실용적인데 미확보.** 공개 PDF 있음, 저술 전 확인
- ❌ **한국 기업 엔지니어링 블로그의 SOP→에이전트 전환 사례 없음** (우아한형제들·카카오·토스·네이버 D2·LINE 검색했으나 미발견). **대상 독자가 한국 실무자인 만큼 아프다.**
- ❌ **SOP의 형식화 정도와 에이전트 성능의 관계**("얼마나 자세히 써야 하는가")를 직접 측정한 연구 없음 — **이 책이 현장 관찰로 채워야 할 공백**
- ❌ **프로세스 마이닝을 에이전트 실행 로그에 적용해 conformance 루프를 닫는 연구**를 특정하지 못했다 — **이 책의 독자적 기여 지점이 될 수 있다**
- ❌ BPMN·LangGraph·Temporal 워크플로 정의 관점 / SAP Signavio·UiPath Process Mining의 에이전트 연계 / OpenAPI를 에이전트 절차로 쓰는 실무 사례
- ❌ **SRE 런북 문화 심층 논의 얕음** / MCP 툴 정의 설계 팁 미확보 / 한국 커뮤니티의 SOP·런북 논의 매우 얕음 / 프로세스 마이닝 경험자 목소리 없음

## 축 3 — 바텀업 → 탑다운 전향

**확보한 것:**
MIT NANDA 95% + **방법론 전부**(300건/52인터뷰/153설문) + **커뮤니티 반박 2건** / **McKinsey 대기업 27→40% vs 소규모 22% 정체**(탑다운 효과의 최강 수치) / 개인 생산성 8/10 vs EBIT 37% 정체 / BCG 2024-10(74%/4%/22%, n=1,000) / Deloitte 2026-04-24(23% vs 21%, n=3,235 ★) / Gartner 40%+ 취소 + **agent washing**(수천 중 ~130개) / shadow AI 다수 + **경영진 65% vs 부하 31%** / **생산성 실증 6건 + 이질성 3중 확인** / **METR 39%p 괴리** / Brynjolfsson 1:5 / J-curve / **Klein & Sorra 구현 이론** / Bick et al. **"채택은 인터넷보다 빨랐는데 절감은 1.4%"** / **탑다운 강제 반발 11건** + 균형용 2건 / 한국 맥락 3건

**비어 있는 것:**
- ❌ **탑다운 전환 성공/실패의 구체 기업 케이스 부재** ← **축 3의 최대 구멍.** 간접 근거(McKinsey 규모 격차, Deloitte 거버넌스 병목, Gartner 취소 사유)만 있다
- ❌ McKinsey 원문 미열람(타임아웃) — 표본·필드 기간 미확인 / MIT NANDA 공식 원문 URL 미확보 / MIT 95% 방법론 비판 **기사** 1차 근거 미확보
- ❌ BCG 2026년판 "AI Radar" / Stanford AI Index 최신판 / Wharton·Accenture 조사 미조사
- ❌ Shadow AI 수치의 1차 조사 URL (Microsoft WorkLab, Salesforce)
- ❌ **"보안팀에서 막혔다"·"예산이 안 나왔다" 유형의 구체 증언 확보 실패** — 조달·법무·벤더 심사 단계 좌초는 Reddit·링크드인이 무대인데 둘 다 미접근
- ❌ **에이전트(자동완성 아닌) 세대의 현장 RCT 없음** — 축 3의 실증은 전부 chat/completion 세대다. **"등록된 자율 에이전트"의 생산성 효과에 대한 현장 실증은 사실상 존재하지 않는다** (§4-8 참조)
- ❌ 한국 기업의 AI 도입 생산성 실증 없음 / shadow AI의 피어리뷰 실증 1건뿐(서지 미확정)

## 축 4 — 변화관리

**확보한 것:**
**Lattice 사례**(축1×축4 최고의 소재) / **Green 2022 인간 감독 비판**(41개 정책, "false sense of security", "shirk accountability" ★) / Laux 2023 불신의 제도화 + 구성적/교정적 / **Skitka 1999 자동화 편향**("거의 항상 맞는 시스템이 가장 위험") / Buçinca 2021 인지적 강제 기능 / **알고리즘 혐오 vs 선호 + 처방**(Dietvorst 2015/2018, Logg 2019) / **Kellogg 2020 contested terrain** / **EPM 메타분석**(성과 개선 증거 없음·스트레스·CWB) / Cornell 감시 연구(원 논문 ⚠️) / **투명성 수치 3종**(77%/90%/22% vs 74%) → 커뮤니케이션 체크리스트 / **Hughes 2011 70% 신화 해체** / Klein & Sorra 대안 / Shonhe & Min 2025(XAI·AI 정체성이 지렛대, **문화는 무효**) / **효과 큰 집단 = 저항 작은 집단** 정합성 / ADKAR 저항 구조(중간관리자 최대 저항, 1위 이유 "이유를 모름") / 리더십 정합성(65% vs 31%) / 닛케이 "AI 비용은 인건비인가" / **감시 증언 3건·직무 불안 5건·"뒤처짐" 4건** / **측정에 대한 한국어 인용 3건**

**비어 있는 것:**
- ❌ **"증폭으로 받아들여진" 성공 사례의 구체 기업 케이스 부재** ← **축 4의 최대 구멍.** Lattice(실패)의 대칭이 없다. 커뮤니티 증언 2~3건만 있고 양이 적다
- ❌ **AI 도입 담당자(추진자)의 1인칭 고충 — 거의 비어 있다.** 커뮤니티에서 추진자는 3인칭 비판 대상으로만 등장한다. **이 책 1순위 독자의 언어를 캐오는 데 실패했다.** 대안: 사내 인터뷰·커리어리·링크드인(미접근)
- ❌ **"AI 못 쓰는 사람"의 1인칭 목소리 확보 실패.** 찾은 건 "뒤처질까 두렵다"지 "아무리 해도 안 된다"가 아니다. 능숙한 사람이 모인 커뮤니티에서 구조적으로 안 나온다 — **사내 인터뷰·설문으로 채워야 하는 영역**
- ❌ **주니어 개발자·운영·CS 인력의 목소리 사실상 비어 있음.** 채용 축소와 연결된 당사자 증언 미확보 (Reddit 본진 접근 불가). **이 책의 감정적 무게에 직접 영향**
- ❌ Cornell 연구 원 논문 / Kotter Inc. 공식 AI 자료 / Prosci 수치 원문(38%/16%/72%/n=1,107) / 리스킬링 프로그램 공식 발표 페이지
- ✅ **B8 Kellogg "6 Rs" 개별 항목명 — 2차에서 해소** (restricting/recommending/recording/rating/replacing/rewarding, PDF 원문 대조)
- ❌ **직무 재설계(job crafting)와 AI의 실증** — 정체성 위협 쪽만 확보
- ❌ **에이전트와 사람이 한 팀으로 일할 때의 조직 수준 실증은 사실상 존재하지 않는다.** 기존 human-agent teaming 문헌은 **의사결정 지원 도구(조언자)** 맥락이지 **자율 실행자** 맥락이 아니다
- ❌ 한국 조직의 AI 수용·저항 실증 없음 / 커리어리 전혀 미접근

---

# 4. 논쟁점·상충 관점

> **아래 여덟 쌍은 어느 한쪽만 인용하면 이 책이 틀린 책이 된다.** 저술 시 반드시 양쪽을 제시하고, **왜 갈리는지(조건 차이)** 를 설명하라.

## 4-1. AI는 생산성을 올리는가, 내리는가

| 근거 | 결과 | 대상 | 조건 |
|---|---|---|---|
| Peng et al. (2023) `[PP]` | **−55.8% 소요 시간** (빨라짐) | 개발자 | HTTP 서버 구현, **단일 그린필드 과제** ⚠️ A8: 표본 N 미확인 |
| Cui et al. (2025) `[PR]` *Mgmt Sci* | **+26.08% 완료 과제** (SE 10.3%), n=4,867 | 개발자 | 3개 기업 현장 RCT, **코드 완성 도구** |
| **METR (2025)** `[PP]` | **+19% 소요 시간 (느려짐)**, n=16 / 246과제 | 개발자 | **평균 5년 숙련된 성숙 오픈소스 코드베이스** |

**왜 갈리나:** 세 연구는 **같은 직군을 다르게 잘랐다.** 그린필드 단일 과제 → 크게 빨라짐. 일상적 코드 완성 → 중간. **자기가 5년 다룬 코드베이스에서 복잡한 실제 과제 → 느려짐.** 즉 **AI의 상대 우위는 사용자의 도메인 숙련도에 반비례**한다. Brynjolfsson et al.·Cui et al.의 이질성 발견과 **완벽하게 정합**한다.

> **이 책의 결론:** **"AI가 생산성을 올리는가"는 잘못된 질문이다.** 옳은 질문은 **"누구의, 어떤 과제의 생산성을 올리는가"** 이며, 그 답을 조직이 알려면 **측정 체계 = 등록·로그**가 있어야 한다. **실증들이 이 책의 주장으로 수렴한다.**
> ⚠️ Peng et al.의 55.8%는 **가장 자주 오용되는 수치**다. 이 책이 할 수 있는 좋은 서비스 중 하나가 **"그 55.8%는 HTTP 서버 하나 짜는 단일 과제였다"** 를 알려주는 것이다.

## 4-2. 사람은 알고리즘을 싫어하는가, 좋아하는가

§2-4-4 표 참조. **수용 성향은 조직의 고정 속성이 아니라 설계 변수다.** 검증된 처방은 하나 — **작은 수정 권한.** 다만 이는 축 1의 책임 귀속과 긴장한다(사용자가 수정했으면 책임은 누구에게?). **그 긴장을 등록부의 권한 필드에서 명시적으로 해소하는 것이 이 책의 설계 과제다.**

## 4-3. 암묵지는 형식화될 수 있는가

| 근거 | 입장 |
|---|---|
| **Nonaka (1994)**, *Organization Science* 5(1) `[PR]` | **가능하다.** SECI의 **외재화(Externalization)** 를 통해 암묵지가 형식지로 전환. 조직 지식은 "**a continuous dialogue between tacit and explicit knowledge**"를 통해 창조된다 |
| **Gourlay (2006)**, *JMS* 43(7) `[PR]` | **네 모드 중 어느 것도 더 단순한 설명으로 대체 불가능한 증거를 갖지 못했다**("none are supported by evidence that cannot be explained more simply"). Nonaka의 틀은 **본질적으로 암묵적인 지식을 누락**("omits inherently tacit knowledge")하며, 지식이 사실상 **관리자에 의해 창조**되는 주관적 정의를 쓴다 |

> **이 책의 결론:** SOP 작성은 **전부를 옮기는 작업이 아니라 옮길 수 있는 것을 골라내는 작업**이다. 형식화 불가능한 영역을 인정하고 **그 영역을 사람에게 남기는 경계 설정이 설계의 일부**여야 한다. **"모든 노하우를 문서화하면 에이전트가 다 한다"는 전제로 시작한 AX 프로젝트는 반드시 좌초한다.**
> Gourlay의 대안: 서로 다른 종류의 지식은 서로 다른 종류의 **행동**에서 창조된다 — 암묵지와 연결된 **비반성적 행동**, 형식지와 연결된 **반성적 행동**. (⚠️ Gourlay의 대안 틀도 광범위한 실증 검증을 받은 것은 아니다.)

## 4-4. 인간 감독은 작동하는가

| 근거 | 입장 |
|---|---|
| **EU AI Act Art. 14** 등 규제 프레임 | 인간 감독이 고위험 AI의 핵심 안전장치 |
| **Green (2022)** `[PR]` *CLSR* | **41개 정책 조사 — 사람들은 요구되는 감독 기능을 수행할 능력이 없으며, 감독 정책은 오히려 결함 있는 알고리즘 사용을 정당화하고 책임 회피를 가능하게 한다** |
| **Skitka et al. (1999)** `[PR]` *IJHCS* | **자동화 편향** — 비자동화 조건이 "매우 신뢰할 만하지만 완벽하지 않은" 자동화 보조 조건보다 모니터링 성과가 좋았다 |
| **Laux (2023)** `[PR]` *AI & Society* | 감독을 폐기하지 말고 **불신을 제도화**하라 — 감독자의 오류 가능성을 전제로 제도를 설계 |
| **Buçinca et al. (2021)** `[PR]` *CSCW* | **인지적 강제 기능**으로 과의존을 줄일 수 있다 (설계 수준 처방) |

> **이 책의 결론 — 등록 설계에 반영해야 할 가장 어려운 진실: 매니저를 세우는 것만으로는 감독이 되지 않는다.**
> 세 겹의 처방: ① **제도적 감독**(개인이 아니라 등록·로그·감사로 감독을 구성) ② **감독자의 오류를 전제한 설계**(구성적/교정적 권한 등급 분리) ③ **인지적 강제 기능**(승인 버튼이 아니라 실제 검토를 유도하는 워크플로)
> **가장 반직관적인 함의: 에이전트 성능이 좋아질수록 인간 감독의 품질은 떨어진다.** 성능 지표와 감독 강도를 함께 관리하지 않으면 **개선이 위험을 만든다.**

## 4-5. 탑다운인가, 자율인가 — 【이 책의 존립이 걸린 논쟁】

| 관점 A: 탑다운이 필요하다 | 관점 B: 성공 사례의 공통점은 "강요하지 않음"이다 |
|---|---|
| McKinsey: **대기업 27→40% vs 소규모 22% 정체** — 체계를 세울 수 있는 규모만 스케일링에 성공 | `caconym_`(2025-12-03): **"providing tools that we aren't forced to use...letting adoption proceed organically"** |
| MIT NANDA: 개인 생산성은 오르는데 **조직 성과는 안 오른다** | GeekNews GN⁺: **"구성원의 자율성을 장려하는 문화에서만 상향식 AI 도입이 가능함"** |
| Deloitte: 사용 23% vs 성숙 거버넌스 21% — **거버넌스가 병목** | **탑다운 강제 도입 반발 증언 11건** (§2-3-7) |
| Gartner: 취소 사유에 **"부적절한 리스크 통제"** 명시 | Kellogg et al.: **통제는 늘 쟁투의 장(contested terrain)** |
| Klein & Sorra: **implementation climate**(보상·지원·기대)가 없으면 확산 안 됨 | `tdeck`: 실패 모드는 강제 자체가 아니라 **맥락 무시한 획일화** |

> **이 책이 반드시 세워야 할 구분 (커뮤니티 반론 3):**
> **"탑다운 체계"가 강제(mandate)가 아니라 인프라·보증(guarantee)이라는 구분을 세울 수 있는가.**
> 위에서 정하는 것이 *무엇을 쓰라*가 아니라 *어디까지 안전한가*라면 이야기가 달라진다. **이 구분을 책 초반에 명시적으로 세우기를 강력히 권한다.**
> 그리고 Adler & Borys의 **enabling / coercive** 구분(§1-5)이 이 논쟁의 이론적 해상도를 올려준다 — 문제는 형식화의 **양**이 아니라 **유형**이다.

## 4-6. 등록은 책임인가 감시인가 — 【이 책의 가장 위험한 지점】

| 등록 = 책임 귀속 | 등록 = 알고리즘 통제 |
|---|---|
| Entra의 Sponsor 필수·관리자 자동 배정 배제 = **책임 희석 방지 설계** | Kellogg et al. (2020): **"등록하고 로그를 남긴다"는 설계는 알고리즘 통제 장치와 기술적으로 구별되지 않는다** |
| Santoni de Sio: **능동적 책임 공백은 조직 설계로만 메울 수 있다** | EPM 메타분석: **EPM이 성과를 개선한다는 증거는 없고, 스트레스 증가·CWB와 정적 관계** |
| Chan et al.: 가시성은 거버넌스의 전제 조건 | Cornell: 알고리즘 감시 → **자율성 인식 저하 → 성과 저하 → 이직 의사** |
| Deloitte가 짚은 결여된 3요소에 audit trail 포함 | `smrtinsert`: **"all your prompts are tracked..."** |

> **저자 스스로 인정한 반작용:** Chan et al.(2024)도 가시성 인프라가 **프라이버시 침해와 권력 집중**(인프라를 쥔 쪽이 힘을 갖는 문제)을 낳는다고 명시한다.
> **책이 그어야 할 선:** 에이전트를 감사하는 것과 사람을 감시하는 것의 경계를 **기술적으로** 그을 수 있는가. `XuebinMa`의 **"정책 판단 단계와 감사 기록 단계를 파이프라인으로 물리적으로 분리한다"** 가 답의 형태다. 여기에 투명성 3원칙(사전 고지·수집 범위 명시·당사자 이익 연결)을 얹는다.

## 4-7. 새 신원을 발급할 것인가, 있는 신원을 쓸 것인가

| 이 책 / 벤더 진영 | 표준 진영 (MCP SEP-1933) |
|---|---|
| 에이전트마다 **새 신원을 만들어 등록**하라 (Entra Agent ID, Okta Universal Directory) | **새 신원을 만들지 말고 런타임이 이미 주는 신원**(K8s PSAT, SPIFFE JWT)을 쓰라 — "don't have to further proliferate client secrets" |
| 등록·소유·수명주기의 **원장**이 생긴다 | 시크릿 확산을 막는다 |

> **저술 제안:** 이 긴장을 회피하지 말라. 답의 방향은 **"아이덴티티의 발급 주체는 런타임이되, 등록·소유·수명주기의 원장은 조직이 갖는다"** 일 것이다. 이 구분을 세우면 반론 1("서비스 계정 리브랜딩 아니냐")에도 함께 답할 수 있다.

## 4-8. 지금 터지고 있는 문제인가, 예방적 설계인가 — 【정직성이 걸린 논쟁】

**커뮤니티가 던진 질문 (이 책의 취재 질문으로도 좋다):**
> **"Trying to determine whether autonomous-agent authorization is current operational pain or mostly anticipatory design work."**
> — `Ram9199`, GitHub MCP issue #2902, **2026-06-13**

**학술 쪽의 정직한 진단:** IAPS 『AI Agent Governance: A Field Guide』(2025) — 에이전트 거버넌스 질문과 개입 수단의 탐색은 **"in their infancy"** 이며, **극소수의 연구자들**(주로 시민사회 조직, 공공 연구기관, 프런티어 AI 기업)만이 이 문제를 다루고 있다. `[논문]`

**최신 갭 분석:** Otsuka et al. (2026), arXiv:2604.23280 `[PP]` — AI 아이덴티티의 정의는 "에이전트가 **무엇이라고 선언된 것**과 **무엇을 하는 것으로 관찰되는 것** 사이의 지속적 관계이며, 그 둘이 어느 시점에서든 서로 대응한다는 신뢰의 정도로 한정된다." 다섯 결정적 공백: ① 의미적 의도 검증 ② **재귀적 위임의 책임** ③ 에이전트 아이덴티티 무결성 ④ 거버넌스 불투명성과 집행 ⑤ 운영 지속 가능성. 저자 결론: 공백은 **구조적(structural)** 이며 **"engineering efforts alone are insufficient."**
> **⚠️ 재귀적 위임 — 에이전트가 다른 에이전트를 호출할 때의 책임 — 은 이 책이 반드시 다뤄야 할 공백이다.** 그리고 인사 시스템을 그대로 복사하면 안 되는 지점(특히 **지속성**과 **법적 지위**)을 미리 처리해준다.

> **이 책의 결론:** 2026년 9월 현재 증거로는 **"둘 다이되, 아직은 예방적 설계 쪽이 크다."**
> **"지금 당장 터지고 있다"고 과장하면 나중에 반증당한다. "아직 안 터졌을 때 세워야 한다"는 논리로 가는 게 더 방어 가능하다.**

## 4-9. 【메타】 이 리서치 자체의 편향

> **"AI adoption is up to 80-90%; ICs absolutely are enamored with AI too. HN...is largely an echo chamber"** — `keeda`, HN, 2026-03-28 ⚠️

**정직하게 기록한다:**
- 커뮤니티 인용의 **약 80%가 Hacker News**에서 왔다. **Reddit 전체(r/sysadmin·r/devops·r/ExperiencedDevs·r/AI_Agents·r/cybersecurity·r/ITManagers·r/msp)는 크롤러 차단으로 접근하지 못했다.**
- HN은 **AI 회의론이 과대표되는 곳**이다.
- **A2A #1672**(658댓글)는 자기 프로젝트 홍보 계정의 교차 게시 정황과 균질한 AI 생성 의심 문체가 짙다. **여론 근거가 아니라 설계 쟁점 자료로만 쓸 것.**

> **저술 규율 (BLOCKING): "커뮤니티에서는"과 "업계에서는"을 절대 혼용하지 말 것.** 커뮤니티 정서를 업계 정서로 승격시키면 안 된다.

---

# 5. 실무 적용 팁 — 현장에서 통한 것

> 커뮤니티에서 실제로 검증된 휴리스틱. 이 책의 실무 챕터에 직접 옮길 수 있다.

## 5-1. 에이전트 등록·권한 설계

1. **시크릿을 돌려주지 말고, 토큰을 발행하거나 요청에 서명하라.**
   > "Never return the secret, but mint a new token, or sign a request." — `zimbatm`, HN, 2026-04-14
2. **폭발 반경(blast radius)과 도달 범위(reach)는 다른 문제다 — 따로 풀어라.**
   > "sandbox the agent so it can't touch anything you care about, then route egress through a policy layer" — `coder-pm`, HN, 2026-08-21
3. **승인은 호스트가 아니라 요청 자체에 바인딩하라** — 규칙 매칭이 "method + path + body, not only the host" 기준이어야 한다. (`Jonathanfishner`, 2026-08-19)
4. **런타임에 실제로 건드린 것과 정책이 허용한 것을 diff 할 수 있어야 한다.**
   > "can I diff what an agent was actually allowed to touch at run time against what the policy said" — `ericmaciver`, 2026-08-21
   > **이 책의 "등록"이 실효를 가지려면 필요한 검증 루프.** 그리고 이것이 프로세스 마이닝의 conformance checking과 같은 구조다 (§1-4).
5. **단발 주입 테스트는 부족하다** — 각 단계가 전부 허용된 상태에서 전체가 위험해지는 경우를 놓친다. (`SaurabhKumbhar`, 2026-08-22)
6. **정책 판단 단계와 감사 기록 단계를 물리적으로 분리하라.** 에이전트가 자기 입으로 말한 의도(`userIntent`)가 인가 판단에 절대 닿지 못하게 파이프라인 구조로 막는다. (`XuebinMa`, MCP PR #2817, 2026-05-30)
7. **감사 로그는 두 겹이 필요하다.**
   > "**Client-asserted context with no signed execution record is unverifiable. A signed execution record with no intent context is hard to interpret.**" — `vaaraio`, MCP SEP-2817, 2026-05-29
   > 즉 **"왜 했는가"(의도)와 "무엇을 했는가"(실행)는 다른 증거다.** MCP SEP-2817이 제안하는 필드: `invocationReason` / `model` / `userIntent` / `turnId`. 🕒 2026-09-05 기준 **open(제안 단계)**.
8. **사람 없는 상황(non-interactive)의 인가는 아직 표준이 없다.** 12개 MCP 서버를 프로덕션에서 돌린다는 개발자의 필드 리포트: "There is no user in the loop / There is no central identity provider / **The OAuth 2.1 flow assumes a user-agent redirect, but agents do not have browsers**" → 결국 HMAC-SHA256 파일 기반 토큰 교환으로 자체 해결. ⚠️ 익명 주장 — 미검증.
9. **등록 티어링의 학술 근거:** ID는 "settings where AI systems could have a large impact upon the world, such as in **making financial transactions or contacting real humans**"에서 가장 정당화된다 (Chan 2024, IDs for AI Systems). → **결제·대외 커뮤니케이션에 닿는 에이전트부터 등록하라.**
10. **등록 스키마 초안:** AI Agent Index의 6범주(법적 사항 / 기술적 역량 / 자율성·통제 / 생태계 상호작용 / 평가 / 안전) + Model Card의 **intended use / out-of-scope use** + **모델 버전과 성능 기준선**(SOP-Bench의 "최신 모델이 낫다는 보장 없음").

## 5-2. SOP를 에이전트에게 주는 법

1. **적을수록 낫다** — "We removed over 80% of Claude Code's system prompt for more advanced models" (`hbarka`, 2026-07-26) ⚠️ 미검증 수치
2. **한 덩어리로 주지 말고 "X 할 때는 Y를 참조하라" 패턴으로 쪼개라** — **점진적 공개(progressive disclosure)**. (`boorang`, 2026-08-28 / `mirekrusin`, 2026-09-02)
3. **규칙 파일도 부패한다 — 주기적으로 걷어내라.** 오래된 AGENTS.md에 낡은 규칙이 쌓이면 최신 모델을 혼란시킨다. (`jpalomaki`, 2026-08-20)
   > **SOP 부패는 사람만의 문제가 아니라 에이전트 컨텍스트에서도 동일하게 발생한다.** 이 책의 SOP 라이프사이클 설계에 직접 반영할 것.
4. **추상적 정의 말고 짧은 명령형으로 쓰라** — "always follow TDD" 같은 간결한 지시가 학술적 정의보다 낫다. (`clickety_clack`, 2026-09-02)
5. **프롬프트 길이가 아니라 검증을 늘려라.**
   > "**95% is running the verification deterministically**" — `lazarie`, 2026-08-08
   > **"SOP를 준다"보다 "SOP 준수를 어떻게 확인하는가"가 본체라는 뜻.** 이 책의 등록·감사 논리와 직결.
6. **모델이 바뀌면 기존 하네스가 깨진다.**
   > "New models are like 'thank you for your suggestion...it's irrelevant. Now let me overspend your token budget.'" — `shostack`, 2026-08-05
   > **에이전트 SOP는 버전 고정과 회귀 테스트가 필요한 자산이다.**
7. **각 단계의 산출물 기준을 못 박아라** — MetaGPT: SOP는 "**establishing standards for intermediate outputs**". 단계 나열보다 산출물 정의가 본체다.
8. **SOP를 쓰기 전에 로그부터 봐라.** 사람들이 실제로 하는 절차를 **발견(discovery)** 한 다음, 그것을 SOP로 정련하고, 에이전트에 넣는다. 에이전트가 돌기 시작하면 그 실행 로그로 다시 **conformance**를 검사한다 — **루프가 닫힌다.** (van der Aalst)
   > ⚠️ 전제: 프로세스 마이닝은 **양질의 이벤트 로그**를 요구한다. 로그가 없거나 케이스 ID·타임스탬프·액티비티가 정리되지 않은 조직에서는 시작조차 못 한다. **이것 자체가 "에이전트를 등록하고 로깅부터 세워야 하는" 이유가 된다.**
9. **AI로 문서를 원샷으로 뽑지 마라** — "You then have to have multiple verification passes to have any chance of it being worth anything." (`tcoff91`, 2026-07-22)

## 5-3. 변화관리 설계

1. **사용자에게 아주 작은 수정 권한이라도 주라.** 수정 폭이 무의미할 정도로 작아도 **수용률이 오르고 실제 성과도 개선된다.** (Dietvorst et al. 2018) → 등록부에 **"사용자 수정 가능 구간"** 을 명시 필드로.
2. **커뮤니케이션 3원칙:** ① 사전 고지(발견당하지 않게) ② 수집 범위 명시(무엇을 보고 무엇을 안 보는지) ③ 당사자 이익과 연결.
3. **AI 사용량을 성과 지표로 삼지 마라.** 활동량이 아니라 실제 결과를 보상하라. ⚠️ **근거 구성 주의 (2026-09-06 정정):** "세 곳에서 독립적으로"가 성립하는 것은 **이 명제까지**다(`brainer` ≈2026-08 / `caconym_` 2025-12-03 / `plaguuuuuu` 2026-06-28 — 셋 다 사람 게시물). **"사용량은 ROI와 상관이 없다"는 별개 명제이고 GN⁺ 봇 요약 단독 근거이므로 인용 금지**다(§2-4-7의 4번). 두 명제를 합쳐 "여러 곳에서 독립적으로"로 쓰면 R0-14 위반.
4. **에이전트의 오류율을 사람의 오류율과 나란히 공개하라.** 안 그러면 알고리즘 혐오 때문에 **에이전트만 불공정하게 심판받는다.**
5. **성능 지표와 감독 강도를 함께 관리하라.** 에이전트가 정확해질수록 사람은 검토를 멈춘다(자동화 편향).
6. **"왜 등록하는가"를 먼저 말하라.** 저항 1위 이유는 일자리 공포가 아니라 **결정의 이유를 이해하지 못하는 것**이다. ⚠️(Prosci, 원문 미열람)
7. **중간관리자를 최우선 대상으로 삼아라.** 탑다운 전향에서 이들은 **집행 주체이자 최대 저항 세력**이다. ⚠️(Prosci)
8. **롤아웃 순서: 효과가 큰 집단과 저항이 작은 집단이 같다** — 경험이 적은 인력부터. (Brynjolfsson·Cui·Noy&Zhang 3중 확인 + Shonhe & Min 정합)
9. **문화 슬로건이 아니라 개인 수준의 정체성 작업.** 조직 문화는 유의한 효과가 없었고, **설명 가능성**과 **AI 정체성 형성**이 먹혔다. (Shonhe & Min 2025)
10. **탑다운의 첫 단계는 실무자 교육이 아니라 리더의 자기 규율.** 경영진이 부하직원의 2배 이상 미승인 도구를 쓴다(65% vs 31%).
11. **금지가 아니라 공식 경로가 개인 경로보다 나아야 한다.** shadow AI는 금지로 안 풀린다.
12. **"catching"이라는 단어를 쓰지 마라.** 탐지의 언어가 직원에게 어떻게 들리는지가 변화관리의 핵심이다.
13. **에이전트를 조직에 등록하되, 사람의 자리에 앉히지 마라.** (Lattice → Entra 교훈)
14. **개인의 향상이 조직 학습으로 자동 전이되지 않는다.** 전이 경로 설계가 별도 과제다.

## 5-4. 손익 모델 — RPA의 실패를 반복하지 않으려면

**RPA 실패의 구조: 유지보수 비용 > 절감된 노동.** 이 책의 "에이전트 등록"이 같은 함정을 피하려면 **등록·소유·감사에 드는 운영 비용을 처음부터 계산에 넣어야 한다.**

계산에 반드시 넣을 항목:
- **HR 데이터와 IAM 그룹의 지속적 동기화 비용** (`Quothling`, 2026-09-01 — Entra 그룹 기반 RBAC 유지 부담)
- **소유자 이탈 시 키 로테이션 비용** — "So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?" (`collabs`, 2026-04-25)
- **감사 오버헤드** — 다만 실측은 **8.3ms 중앙값**으로 작다 (Auditable Agents, 이 실험 조건에서)
- **에이전트 SOP의 회귀 테스트·버전 고정 비용** (모델 교체마다)
- **라이선스 비용** — Agent 365 $15/user/월(연약정) 등 △
- **조직 보완재 비율** — Brynjolfsson: 기술 구매 1에 조직 자본 5 (IT 사례, AI 직접 대입은 과대 해석)

---

# 6. 참고문헌

> 접근일은 모두 **2026-09-05**. **★** 직접 열람 / **△** 검색 요약만 / **✗** 접근 실패.
> 상세 목록(웹 99건·논문 68건·커뮤니티 스레드 80여 건)은 `research/web.md`·`research/papers.md`·`research/community.md`에 보존. 아래는 본문 저술에 실제로 쓸 핵심만 추린 것이다.

## 6-1. 축 1 — 에이전트 등록 (1차 자료·제품·제도)

| 제목 | URL | 발행일 | 열람 |
|---|---|---|---|
| Deutsche Bank's Corporate Bank onboards its first digital employee | https://www.db.com/news/detail/20200720-deutsche-bank-s-corporate-bank-onboards-its-first-digital-employee-for-client-facing-role?language_id=1 | **2020-07-20** | ★ |
| What's new in Microsoft Entra Agent ID | https://learn.microsoft.com/en-us/entra/agent-id/whats-new-agent-id | 2026-05-01 (갱신 2026-08-13) | ★ |
| **Administrative relationships in Microsoft Entra Agent ID (Owners, sponsors, managers)** | https://learn.microsoft.com/en-us/entra/agent-id/agent-owners-sponsors-managers | **2026-04-16 (갱신 2026-09-03)** | ★ |
| Microsoft Agent 365 (제품 페이지) | https://www.microsoft.com/en-us/microsoft-agent-365 | 2026 | ★ |
| Okta brings first-class identity to AI agents with Agent SSO | https://www.okta.com/newsroom/press-releases/okta-brings-first-class-identity-to-ai-agents-with-agent-sso/ | **2026-08-24** | ★ |
| Okta introduces Cross App Access | https://www.okta.com/newsroom/press-releases/okta-introduces-cross-app-access-to-help-secure-ai-agents-in-the/ | 2025-06-23 | △ |
| AI Agents at Work 2026 (Okta 조사) | https://www.okta.com/newsroom/articles/ai-agents-at-work-2026-agentic-enterprise-security/ | 2026 | △ |
| Auth0 for AI Agents (2026-05 제품 발표) | https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/ | 2026-05 | △ |
| 1Password Unified Access | https://1password.com/press/2026/mar/1password-unified-access | 2026-03 | △ |
| SailPoint Agentic Fabric | https://investor.sailpoint.com/news-releases/news-release-details/sailpoint-redefines-identity-security-new-adaptive-identity | 2026-05-11 | △ |
| CyberArk Secure AI Agents | https://www.cyberark.com/press/cyberark-introduces-first-identity-security-solution-purpose-built-to-protect-ai-agents-with-privilege-controls/ | 2025(말) | △ |
| **The Non-Human Identity Governance Vacuum (CSA 백서)** | https://labs.cloudsecurityalliance.org/research/csa-whitepaper-nonhuman-identity-agentic-ai-governance-v1-cs/ | **2026-05-20** | ★(랜딩) / ✗(PDF 파싱 실패) |
| Agent Identity Governance Framework v1 (CSA) | https://labs.cloudsecurityalliance.org/agentic/agentic-identity-governance-framework-v1/ | 2026 | △ |
| **Agentic AI is scaling faster than guardrails (Deloitte Insights)** | https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html | **2026-04-24** | ★ |
| The Lifecycle Crisis: Birth, Life, and Death of AI Agents (Dark Reading) | https://www.darkreading.com/identity-access-management-security/the-lifecycle-crisis-managing-the-birth-life-and-death-of-ai-agents | ⚠️ 미확인 | △ |
| AI agent offboarding: what happens when the worker never leaves? | https://nhimg.org/community/nhi-best-practices/ai-agent-offboarding-what-happens-when-the-worker-never-leaves/ | ⚠️ 미확인 | △ |
| Lattice scraps plans to treat AI bots as employees (SHRM) | https://www.shrm.org/topics-tools/news/technology/lattice-scraps-plans-to-treat-ai-bots-as-employees-after-backlash | 2024-07 | △ |
| Lattice / AI workers (Fortune) | https://fortune.com/2024/07/12/lattice-ai-workers-sam-altman-brother-jack-sarah-franklin | **2024-07-12** | △ |
| Goldman Sachs autonomous coder pilot (CNBC) | https://www.cnbc.com/2025/07/11/goldman-sachs-autonomous-coder-pilot-marks-major-ai-milestone.html | 2025-07-11 | ✗ (403) |
| How Goldman Sachs Is Using Agentic AI (Forbes) | https://www.forbes.com/sites/bernardmarr/2026/08/06/how-goldman-sachs-is-using-agentic-ai-for-software-engineering-at-scale/ | 2026-08-06 | △ |
| Machine Identities Outnumber Humans 80:1 (CyberArk) | https://www.cyberark.com/press/machine-identities-outnumber-humans-by-more-than-80-to-1-new-report-exposes-the-exponential-threats-of-fragmented-identity-security/ | 2025-04 | △ |
| 2026 Identity Security Landscape (Palo Alto Networks) | https://www.paloaltonetworks.com/idira/idira-identity-security-landscape | 2026 | △ |
| 社員と化すAIエージェント、費用は人件費？(日本経済新聞) | https://www.nikkei.com/article/DGXZQOUC2411U0U6A620C2000000/ | **2026-07-09** | ✗ (유료) |

## 6-2. 축 1 — 제도·규제

| 제목 | URL | 발행일 | 열람 |
|---|---|---|---|
| **EU AI Act Article 49: Registration** | https://artificialintelligenceact.eu/article/49/ | Reg. (EU) 2024/1689 | ★ |
| EU AI Act Annex VIII | https://artificialintelligenceact.eu/annex/8/ | Reg. (EU) 2024/1689 | △ |
| Article 71: EU database for high-risk AI systems | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-71 | — | △ |
| **EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines (Gibson Dunn)** | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ | **2026-05-27** | ★ |
| EU agrees to delay key AI Act compliance deadlines (Travers Smith) | https://www.traverssmith.com/knowledge/knowledge-container/eu-agrees-to-delay-key-ai-act-compliance-deadlines/ | 2026 | △ |
| The EU AI Act's August 2, 2026 Deadline Just Moved (ComplianceHub) | https://compliancehub.wiki/eu-digital-omnibus-ai-act-deadline-deferral-annex-iii-2027/ | 2026 | △ |
| NIST AI RMF to ISO/IEC 42001 Crosswalk (NIST AIRC) | https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf | — | △ |
| The Roles and Responsibilities in ISO 42001 (Schellman) | https://www.schellman.com/blog/ai-governance/iso-42001-roles-and-responsibilities | ⚠️ 미확인 | △ |
| AI 기본법 시행과 그 시사점 (신&김) | https://www.shinkim.com/kor/media/newsletter/3114 | 2026 | △ |
| AI기본법 시행 6개월 — 계도기간이 끝나기 전에 | https://datalaw.kr/posts/ai-basic-law-business-duties/ | 2026 | △ |
| 생성형 AI 개발·활용을 위한 개인정보 처리 안내서 (개인정보위) | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=11410 | **2025-08-06** | △ |
| 개인정보위, 생성형 AI 이용자 개인정보 보호 가이드 (바이라인) | https://byline.network/2026/05/19-618/ | 2026-05-19 | △ |
| OMB M-25-21 (PDF 미러) | https://static.carahsoft.com/concrete/files/9717/4412/5797/Guidance_M-25-21_Accelerating_Federal_Use_of_AI_through_Innovation_Governance_and_Public_Trust.pdf | **2025-04-03** | △ |
| DOJ AI Inventory (실물 예시) | https://www.justice.gov/ai/ai-inventory | — | △ |
| 2025 Federal Agency AI Use Case Inventory (원자료) | https://github.com/ombegov/2025-Federal-Agency-AI-Use-Case-Inventory | 2025 | △ |
| 346 generative AI services filed with CAC (中国国务院新闻办) | http://english.scio.gov.cn/pressroom/2025-04/09/content_117814020.html | **2025-04-09** | △ |
| What is China's AI Algorithm Filing? (AppInChina) | https://appinchina.co/what-is-chinas-ai-algorithm-filing/ | 2026 | △ |

## 6-3. 학술 문헌 (저자·연도·제목·게재처·DOI/arXiv)

**축 1 — 등록·아이덴티티·거버넌스**
1. Miller, M. S., Yee, K.-P., & Shapiro, J. (2003). *Capability Myths Demolished*. Tech. Report SRL2003-02, Johns Hopkins Univ. `[기술보고서]`
2. Esteva, M., Rodríguez-Aguilar, J. A., Sierra, C., Garcia, P., & Arcos, J. L. (2001). On the Formal Specification of Electronic Institutions. *Agent Mediated Electronic Commerce*, LNAI 1991, 126–147. Springer. `[PR]` ⚠️ A1
3. **Hübner, J. F., Sichman, J. S., & Boissier, O. (2002). A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems (MOISE+). *SBIA 2002*, LNAI 2507. Springer. DOI: 10.1007/3-540-36127-8_12** `[PR]`
4. Dignum, V. (2004). *A Model for Organizational Interaction* (OperA). PhD diss., Utrecht Univ./SIKS. `[학위논문]` ⚠️ A2
5. Esteva, M. et al. (2004). AMELI: An Agent-based Middleware for Electronic Institutions. *AAMAS 2004*, 1, 236–243. ACM. `[PR]` ⚠️ A3
6. Mitchell, M. et al. (2019). Model Cards for Model Reporting. *FAT* '19*. DOI: 10.1145/3287560.3287596. arXiv:1810.03993. `[PR]`
7. McGregor, S. (2021). Preventing Repeated Real World AI Failures by Cataloging Incidents. *AAAI* 35(17), 15458–15463. arXiv:2011.08512. `[PR]`
8. **Santoni de Sio, F., & Mecacci, G. (2021). Four Responsibility Gaps with Artificial Intelligence. *Philosophy & Technology*, 34(4), 1057–1084. DOI: 10.1007/s13347-021-00450-x** `[PR]`
9. **Chan, A., Ezell, C., Kaufmann, M., Wei, K., Hammond, L., Bradley, H., Bluemke, E., Rajkumar, N., Krueger, D., Kolt, N., Heim, L., & Anderljung, M. (2024). Visibility into AI Agents. *ACM FAccT '24*. DOI: 10.1145/3630106.3658948. arXiv:2401.13138v6** `[PR]`
10. Chan, A. (2024). IDs for AI Systems. arXiv:2406.12137 (2024-06-17, 수정 2024-10-28). `[PP]`
11. Casper, S. 외 (2025). The AI Agent Index. arXiv:2502.01635 (2025-02). `[PP]` ⚠️ A4·B1
12. Kolt, N. (2025). Governing AI Agents. *101 Notre Dame L. Rev.* (forthcoming). arXiv:2501.07913. SSRN 4772956. `[PP→PR]`
13. South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. (2025). Authenticated Delegation and Authorized AI Agents. arXiv:2501.09674. **ICML 2025 게재 제목: *Position: AI Agents Need Authenticated Delegation*** (OpenReview 9skHxuHyM4). `[PP→PR]`
14. **Chan, A., Wei, K., Huang, S., Rajkumar, N., Perrier, E., Lazar, S., Hadfield, G. K., & Anderljung, M. (2025). Infrastructure for AI Agents. *TMLR*. arXiv:2501.10114v3 (2025-06-19).** `[PR]`
15. Kraprayoon, J. 외 / IAPS (2025). AI Agent Governance: A Field Guide. arXiv:2505.21808. `[보고서]` ⚠️ A5
16. South, T., Nagabhushanaradhya, S. 외 (19인) (2025). Identity Management for Agentic AI. *OpenID Foundation Whitepaper 2025*. arXiv:2510.25819 (2025-10-29). `[백서]` 🕒
17. Kaptein, M., Khan, V.-J., & Podstavnychy, A. (2026). Runtime Governance for AI Agents: Policies on Paths. arXiv:2603.16586 (2026-03-17). `[PP]`
18. Nian, Y. 외 (2026). Auditable Agents. arXiv:2604.05485 (v1 2026-04-07, v2 2026-08-13). `[PP]`
19. Otsuka, T., Toyoda, K., & Leung, A. (2026). AI Identity: Standards, Gaps, and Research Directions for AI Agents. arXiv:2604.23280 (2026-04-25). `[PP]` 🕒
20. Atkinson, D. I., & O'Bryan, J. E. (2026). Government AI Use as a Monitoring Primitive. arXiv:2607.04543 (2026-07-05). ICML 2026 Workshop on Technical AI Governance. `[PP→워크숍]`

**축 2 — SOP·절차의 형식화**
21. **Adler, P. S., & Borys, B. (1996). Two Types of Bureaucracy: Enabling and Coercive. *ASQ*, 41(1), 61–89. DOI: 10.2307/2393986** `[PR]` ⚠️ B7
22. Nonaka, I. (1994). A Dynamic Theory of Organizational Knowledge Creation. *Organization Science*, 5(1), 14–37. DOI: 10.1287/orsc.5.1.14 `[PR]`
23. **Feldman, M. S., & Pentland, B. T. (2003). Reconceptualizing Organizational Routines as a Source of Flexibility and Change. *ASQ*, 48(1), 94–118. DOI: 10.2307/3556620** `[PR]`
24. Gourlay, S. (2006). Conceptualizing Knowledge Creation: A Critique of Nonaka's Theory. *JMS*, 43(7), 1415–1436. DOI: 10.1111/j.1467-6486.2006.00637.x `[PR]`
25. van der Aalst, W. M. P. (2011 / 2016). *Process Mining*. Springer. DOI: 10.1007/978-3-642-19345-3 / 10.1007/978-3-662-49851-4 `[PR-book]`
26. Hong, S. 외 (2024). MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework. *ICLR 2024 (Oral)*. arXiv:2308.00352. `[PR]` ⚠️ A6
27. Berti, A., Kourani, H., & van der Aalst, W. M. P. (2024). PM-LLM-Benchmark. arXiv:2407.13244. `[PP]` ⚠️ B4
28. **Nandi, S. 외 (24인) (2025/2026). SOP-Bench: Complex Industrial SOPs for Evaluating LLM Agents. arXiv:2506.08119 (v1 2025-06-09, v2 2026-02-23).** `[PP]` 🕒 ⚠️ B5
29. Amazon Science (2025). Structuring the Unstructured: A Multi-Agent LLM Framework for Transforming Ambiguous SOPs into Code. *EMNLP 2025 Industry Track*. https://aclanthology.org/2025.emnlp-industry.163.pdf
30. Agent-S (arXiv:2503.15520) / SOP-Maze (arXiv:2510.08942) / **Compile, Then Page (arXiv:2607.11346, 2026-07)** `[PP]` ⚠️ 저자 미확인

**축 3 — 조직 경제학·실증**
31. **Klein, K. J., & Sorra, J. S. (1996). The Challenge of Innovation Implementation. *AMR*, 21(4), 1055–1080. DOI: 10.5465/amr.1996.9704071863** `[PR]`
32. **Brynjolfsson, E., Hitt, L. M., & Yang, S. (2002). Intangible Assets: Computers and Organizational Capital. *Brookings Papers on Economic Activity*, 2002(1). DOI: 10.1353/eca.2002.0003** `[PR]`
33. Brynjolfsson, E., Rock, D., & Syverson, C. (2017). Artificial Intelligence and the Modern Productivity Paradox. *NBER WP 24001*. `[WP]` / (2021) The Productivity J-Curve. *AEJ: Macroeconomics*. `[PR]` ⚠️ A14
34. Peng, S., Kalliamvakou, E., Cihon, P., & Demirer, M. (2023). The Impact of AI on Developer Productivity: Evidence from GitHub Copilot. arXiv:2302.06590. `[PP]` ⚠️ A8
35. Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*. DOI: 10.1126/science.adh2586 `[PR]`
36. McElheran, K. 외 (2024). AI Adoption in America: Who, What, and Where. *JEMS*, 33(2), 375–415. DOI: 10.1111/jems.12576 `[PR]` 🕒 (2018년 데이터)
37. **Bick, A., Blandin, A., & Deming, D. J. (2024). The Rapid Adoption of Generative AI. *NBER WP 32966*.** `[WP]` 🕒
38. **Brynjolfsson, E., Li, D., & Raymond, L. (2025). Generative AI at Work. *QJE*, 140(2), 889–942.** `[PR]`
39. **Dell'Acqua, F. 외 (2025). Navigating the Jagged Technological Frontier. *Organization Science*. DOI: 10.1287/orsc.2025.21838. HBS WP 24-013.** `[PR]` ⚠️ B2
40. Cui, Z. (K.) 외 (2025). The Effects of Generative AI on High-Skilled Work. *Management Science*. DOI: 10.1287/mnsc.2025.00535 `[PR]`
41. **METR (2025). Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity. arXiv:2507.09089.** `[PP]` ⚠️ A7 🕒
42. Silic, M. 외. From Shadow IT to Shadow AI. *Strategic Change* (Wiley). DOI: 10.1002/jsc.2682 `[PR]` ⚠️ A9

**축 4 — 변화관리·수용·저항**
43. **Skitka, L. J., Mosier, K. L., & Burdick, M. (1999). Does automation bias decision-making? *IJHCS*, 51(5), 991–1006. DOI: 10.1006/ijhc.1999.0252** `[PR]`
44. **Hughes, M. (2011). Do 70 Per Cent of All Organizational Change Initiatives Really Fail? *JCM*, 11(4), 451–464. DOI: 10.1080/14697017.2011.630506** `[PR]`
45. Venkatesh, V., Thong, J. Y. L., & Xu, X. (2012). UTAUT2. *MIS Quarterly*, 36(1), 157–178. `[PR]`
46. **Dietvorst, B. J., Simmons, J. P., & Massey, C. (2015). Algorithm Aversion. *JEPG*, 144(1), 114–126.** `[PR]`
47. **Dietvorst, B. J. 외 (2018). Overcoming Algorithm Aversion. *Management Science*, 64(3), 1155–1170. DOI: 10.1287/mnsc.2016.2643** `[PR]`
48. Logg, J. M., Minson, J. A., & Moore, D. A. (2019). Algorithm appreciation. *OBHDP*, 151, 90–103. DOI: 10.1016/j.obhdp.2018.12.005 `[PR]`
49. **Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at Work: The New Contested Terrain of Control. *Academy of Management Annals*, 14(1), 366–410. DOI: 10.5465/annals.2018.0174** `[PR]` ✅ B8 해소 (6 Rs 원문 대조 완료 — §2-4-2 588행)
50. Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). To Trust or to Think. *PACM HCI*, 5(CSCW1), Art. 188. DOI: 10.1145/3449287 `[PR]` ⚠️ B9
51. **Green, B. (2022). The flaws of policies requiring human oversight of government algorithms. *Computer Law & Security Review*, 45. arXiv:2109.05067.** `[PR]`
52. Ravid, D. M. 외 (2023). A meta-analysis of the effects of electronic performance monitoring on work outcomes. *Personnel Psychology*. DOI: 10.1111/peps.12514 `[PR]` ⚠️ A10·B3
53. Laux, J. (2023). Institutionalised distrust and human oversight of artificial intelligence. *AI & Society*. DOI: 10.1007/s00146-023-01777-z `[PR]` ⚠️ A11
54. Schemmer, M. 외 (2023). Appropriate Reliance on AI Advice. *IUI 2023*. DOI: 10.1145/3581641.3584066 `[PR]` ⚠️ A16
55. Wildman, J. L. 외 (2024). Trust in Human-Agent Teams. DOI: 10.1177/20413866241253278 `[PR]` ⚠️ A12
56. Shonhe, L., & Min, Q. (2025). Mitigating AI-induced professional identity threat and fostering adoption in the workplace. *AI & Society*, 40(5), 4079–4092. DOI: 10.1007/s00146-024-02170-0 `[PR]`
57. Why Vilifying the Status Quo Can Derail a Change Effort: Kotter's Contradiction. *JCM*. DOI: 10.1080/14697017.2022.2137835 `[PR]` ⚠️ A13 — **확인 강력 권장**

## 6-4. 축 2·3 — 조사 보고서·산업 자료

| 제목 | URL | 발행일 | 열람 |
|---|---|---|---|
| The GenAI Divide: State of AI in Business 2025 (MIT NANDA, v0.1 미러) | https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf | **2025-07** | △ ⚠️ 공식 URL 미확보 |
| The State of AI: Global Survey 2026 (McKinsey) | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026 | ✗ (타임아웃) |
| Companies' financial value from AI holds firm in 2026 (FM Magazine) | https://www.fm-magazine.com/news/2026/sep/companies-financial-value-from-ai-holds-firm-in-2026/ | 2026-09 | △ |
| Where's the Value in AI? (BCG) | https://www.bcg.com/publications/2024/wheres-value-in-ai | **2024-10-24** | △ 🕒 |
| Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | **2025-06-25** | ✗ (403) / 교차 확인 △ |
| What Is Shadow AI? (Cyberhaven) | https://www.cyberhaven.com/infosec-essentials/shadow-ai | 2026 | △ |
| Bosses blinded by confidence about shadow AI use (The Register) | https://www.theregister.com/ai-ml/2026/05/27/bosses-blinded-by-confidence-about-shadow-ai-use-by-workers/5247275 | **2026-05-27** | △ |
| Structuring the unstructured (Amazon Science) | https://www.amazon.science/publications/structuring-the-unstructured-a-multi-agent-llm-framework-for-transforming-ambiguous-sops-into-code | EMNLP 2025 | △ |
| SOP-Bench (Amazon Science 블로그) | https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures | 2025 | △ |
| AGENTS.md (공식) | https://agents.md/ | 2025-08~ | △ |
| MCP Authorization (공식 스펙) | https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization | 2025-11-25 | △ 🕒 |
| Linux Foundation Launches the Agent2Agent Protocol Project | https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents | **2025-06-23** | △ |
| Celonis AgentC | https://www.celonis.com/news/press/celonis-agentc-making-ai-agents-work-for-the-enterprise-with-process-intelligence | **2024-10-23** | △ |
| Scaling the agentic enterprise with Celonis on Microsoft Agent 365 | https://www.celonis.com/blog/scaling-the-agentic-enterprise-with-microsoft-agent-365-and-celonis | 2026-05 | △ |
| Americans' views on use of AI to monitor and evaluate workers (Pew) | https://www.pewresearch.org/internet/2023/04/20/americans-views-on-use-of-ai-to-monitor-and-evaluate-workers/ | **2023-04-20** | △ |
| AI Surveillance in the Workplace Linked to Employee Resistance (SHRM/Cornell) | https://www.shrm.org/topics-tools/news/employee-relations/ai-surveillance-in-the-workplace-linked-to-employee-resistance-- | ⚠️ 미확인 | △ |
| AI Adoption: Driving Change With a People-First Approach (Prosci) | https://www.prosci.com/ai-change-management | ⚠️ 미확인 | △ |

## 6-5. 커뮤니티 — 인용 출처 (전체 목록은 `research/community.md`)

**Hacker News 주요 스토리 스레드**

| URL | 제목 | 게시일 | 규모 |
|---|---|---|---|
| https://news.ycombinator.com/item?id=42928645 | OWASP Non-Human Identities Top 10 | 2025-02-04 | 157점·33댓글 |
| https://news.ycombinator.com/item?id=44941118 | 95% of generative AI pilots at companies are failing – MIT report | 2025-08-18 | 230점·167댓글 |
| https://news.ycombinator.com/item?id=46138952 | Everyone in Seattle hates AI | 2025-12-03 | 967점·1065댓글 |
| https://news.ycombinator.com/item?id=47549649 | Why are executives enamored with AI, but ICs aren't? | 2026-03-27 | 109점·168댓글 |
| https://news.ycombinator.com/item?id=47765374 | Show HN: Kontext CLI – Credential broker for AI coding agents | 2026-04-14 | 70점·17댓글 |
| https://news.ycombinator.com/item?id=49363710 | Launch HN: OneCLI – OSS sandboxed agent harness for teams | 2026-08-19 | 88점·36댓글 |

**챕터 오프닝용 핵심 인용 (원문 그대로, 각색 금지)**

| # | 인용 | 출처 | 배정 |
|---|---|---|---|
| 1 | **"mandates happened and now I'm being forced to use them. Absolutely no guidance from leadership though."** | `ares623`, HN, 2026-03-06, item?id=47279806 | **책 전체 오프닝 후보 1순위** — 이 책이 없어서 생긴 일 |
| 2 | **"Wtf? We have been calling these workload identities for years"** | `zingababba`, HN, 2025-02-04, item?id=42928645 | 등록 챕터 |
| 3 | **"Pretty pleaser please people don't get your agents registered as direct-reports in the org-chart with HR!"** | `polotics`, HN, 2026-09-04, item?id=49561918 | 서문 / 사번 챕터 |
| 4 | **"I went through the entire investor arc in about a day and a half. From the hopeful optimism of hiring a CEO, to watching the org chart explode..."** | `yego`, HN, 2026-03-04, item?id=47245374 | 조직 은유의 함정 |
| 5 | **"Confluence is where documentation goes to die. And then rot."** | `EdwardDiego`, HN, 2020-07-12, item?id=23808854 | SOP 챕터 (5인 5년 반복과 함께) |
| 6 | **"When I get an LLM-generated doc or runbook, my first thought is that its very possible that I'm the first person who has ever read this."** | `backlava12`, HN, 2026-08-11, item?id=49258726 | SOP 자동 생성 챕터 |
| 7 | **"A runbook can tell you what usually works, but it cannot tell you when the situation is no longer 'usual.'"** | `flashdesk`, HN, 2026-04-27, item?id=47918548 | 절차의 한계 |
| 8 | **"You work the same hours, but you're more tired, and the company pockets the profits"** | `pron`, HN, 2026-03-28, item?id=47549649 | 변화관리 — 저항의 진짜 이유 |
| 9 | **"all your prompts are tracked and easily viewable by whoever oversees it at your company"** | `smrtinsert`, HN, 2026-03-29, item?id=47549649 | 감사·로깅 챕터 |
| 10 | **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음"** | `brainer`, GeekNews topic 33050, ≈2026-08-31 | 측정 챕터 (한국어 원문) |
| 11 | **"일단 회사에서 AI 서비스를 지원 거의 안해주네요. …(회사에서 쓰려고 개인이 AI 서비스 구독 ㅜ)…"** | `akapwhd`, GeekNews topic 29217, ≈2026-05 | 바텀업의 현실 (한국 독자용) |
| 12 | **"AI를 '잘쓰는법'을 어떻게 다뤄야 하는지는 다들 갈팡질팡하고 있는 것 같네요."** | `kallare`, GeekNews topic 29217, ≈2026-05 | 서문 |
| 13 | **"So every time we fire or lay off the person whose name is on the automation, we need to rotate the keys?"** | `collabs`, HN, 2026-04-25, item?id=47898675 | 소유자 지정 챕터 |
| 14 | **"Client-asserted context with no signed execution record is unverifiable. A signed execution record with no intent context is hard to interpret."** | `vaaraio`, MCP SEP-2817, 2026-05-29 | 감사 로그 설계 |
| 15 | **"aimless tokenmaxing"** | `827a`, HN, 2026-05-22, item?id=48236051 | 이 책이 반대하는 것의 이름 |
| 16 | **"AI is like an energetic intern who knows his place on the totem pole and wants to please"** | `ryandrake`, HN, 2026-03-28, item?id=47549649 | 절대 반대하지 않는 조직원 |

**GitHub 스펙 논쟁 (전부 2026-09-05 조회, 🕒 출간 시 재확인 필수)**

| URL | 제목 | 개설 | 상태 |
|---|---|---|---|
| modelcontextprotocol/modelcontextprotocol#1933 | SEP-1933: Workload Identity Federation | 2025-12-05 | open·40댓글 |
| modelcontextprotocol/modelcontextprotocol#2817 | SEP-2817: AI Invocation Audit Context in Request `_meta` | 2026-05-29 | open·29댓글 |
| modelcontextprotocol/modelcontextprotocol#2787 | SEP-2787: Tool call attestation | 2026-05-25 | open·33댓글 |
| modelcontextprotocol/modelcontextprotocol#2385 | SEP-2385: Tool Auth Manifest | 2026-03-11 | open·23댓글 |
| modelcontextprotocol/modelcontextprotocol#2902 | MCP Authorization in Non-Browser, Non-User-Interactive Scenarios | 2026-06-10 | closed·4댓글 |
| modelcontextprotocol/modelcontextprotocol#3337 | Proposal for the Enterprise IG Audit/Compliance Scope | 2026-09-01 | open·1댓글 |
| a2aproject/A2A#1672 | Proposal: Agent Identity Verification for Agent Cards | 2026-03-22 | open·658댓글 ⚠️ **출처 품질 주의** |
| a2aproject/A2A#1575 | Running implementation of agent identity, delegation, enforcement | 2026-03-02 | open·98댓글 |
| spiffe/spiffe#382 | Proposal: SPIFFE IDs for AI Agent Workloads | 2026-03-26 | open·3댓글 |
| spiffe/spiffe#383 | JWT-SVID claim for model identity in AI workloads | 2026-03-31 | open·**0댓글** |
| spiffe/spiffe#408 | JWT-SVID Support Delegated (Actor) Identity | 2026-06-27 | open·2댓글 |

**GeekNews (게시일 상대 표기 — 2026-09-05 조회 기준 추정치 병기)**

| URL | 제목 | 게시(추정) |
|---|---|---|
| https://news.hada.io/topic?id=29217 | 모두가 AI를 가져도 회사는 여전히 아무것도 배우지 못할 때 | ≈2026-05 |
| https://news.hada.io/topic?id=33050 | 좋은 조직문화가 AI보다 큰 생산성 향상을 만드는 이유 | ≈2026-08-31 |
| https://news.hada.io/topic?id=32661 | 소프트웨어 팀의 AI 사용 패턴 | ≈2026-08-19 |
| https://news.hada.io/topic?id=20489 | Atuin Desktop: 실행 가능한 Runbooks | 2025-04-23 |
| https://news.hada.io/topic?id=21037 | AI가 Microsoft 개발자들을 미치게 만드는 걸 보는 게 새로운 취미가 되었어요 | 상대 표기 |
| https://okky.kr/articles/1532084 | 한국이 AI로 개발자 대체가 빠르게 진행될 수밖에 없는 이유 (OKKY) | "1년 이상 전" ⚠️ 미검증 |

---

# 7. 리서치 한계

## 7-1. 접근하지 못한 소스 (구조적 공백)

| 소스 | 사유 | 잃은 것 |
|---|---|---|
| **Reddit 전체** (r/sysadmin·r/devops·r/ExperiencedDevs·r/AI_Agents·r/cybersecurity·r/ITManagers·r/msp·r/cscareerquestions) | 크롤러 차단 | 축 1의 NHI 운영 고통 날것 일화, 축 3의 조달·보안 심사 좌초 증언, **축 4의 주니어 직무 불안 당사자 목소리** |
| **X / Mastodon / LinkedIn 공개 포스트** | 미접근 | "AI employee" 마케팅에 대한 냉소, 추진자의 1인칭 발언 |
| **커리어리** | 검색 결과 0건 | 한국 실무자 목소리 |
| **Discord / Slack 공개 로그** | 미접근 | 스펙 설계자·얼리어답터 대화 |
| **Lobsters 개별 스레드** | 페이지 404 | "Securing agentic identity"(2026-07-06) 등 존재는 확인, 댓글 미확보 |
| CNBC / Gartner 보도자료 | HTTP 403 | Goldman Sachs 파일럿 원문, Gartner 예측 원문 |
| McKinsey State of AI 2026 | 60초 타임아웃 | **표본 크기·필드 기간 미확인** |
| 닛케이 (2026-07-09) | 유료 구간 | 일본 "AI社員" 구체 기업명·수치 |
| MIT NANDA 공식 원문 | 공식 도메인 URL 미확보 | v0.1 미러만 유통 |
| ISO/IEC 42001 표준 원문 | 유료 | Annex A 개별 통제 번호 |
| CSA 백서 PDF | 바이너리 파싱 실패 | 랜딩 페이지 요약으로 대체 |

## 7-2. 커버하지 못한 영역 (내용 공백)

**전 축 공통 — 가장 아픈 것:**
1. **한국 사례가 사실상 없다.** 대상 독자가 한국 AX 실무 리더인데 축 1·2·4 모두 국내 기업 사례 0건. 확보된 것은 제도(AI 기본법·개인정보위)와 한국어 커뮤니티 인용 5~6건뿐이다. **별도 심층 조사 또는 사내 인터뷰가 필요하다.**
2. **"등록된 자율 에이전트"의 생산성 효과에 대한 현장 실증은 존재하지 않는다.** 축 3의 RCT는 전부 chat/completion 세대(조언자·자동완성)다. 인간-에이전트 팀 문헌도 대부분 **의사결정 지원 도구** 맥락이다. → **이 공백을 책이 정직하게 밝히는 것이 오히려 신뢰도를 높인다.**
3. **한국 조직 맥락의 학술 실증은 네 축 전부에서 0건**이다 (AI 도입 생산성, SOP 형식화 실태, 수용·저항, 에이전트 거버넌스).

**축별 최대 구멍:**
- **축 1:** 한국 사례 / 통신·제조·공공 산업 사례 / **제품을 실제로 써본 사람의 후기**
- **축 2:** 암묵지 발굴 기법(task mining·Scribe·Tango·Guidde) 미검증 / 한국 기업 엔지니어링 블로그의 SOP→에이전트 사례 없음 / **"SOP를 얼마나 자세히 써야 하는가"를 측정한 연구 없음**
- **축 3:** **탑다운 전환 성공/실패의 구체 기업 케이스 부재** / "보안팀에서 막혔다"·"예산이 안 나왔다" 유형 증언 없음
- **축 4:** **"증폭으로 받아들여진" 성공 사례의 구체 기업 케이스 부재**(Lattice 실패의 대칭이 없다) / **추진자의 1인칭 고충 거의 없음** / **"AI 못 쓰는 사람"의 1인칭 목소리 없음** / 주니어·운영·CS 인력 목소리 없음

**이 책의 독자적 기여가 될 수 있는 공백 (planner 참고):**
- **프로세스 마이닝을 에이전트 실행 로그에 적용해 conformance 루프를 닫는 것** — 학술 연구를 특정하지 못했다.
- **재귀적 위임의 책임** — 에이전트가 다른 에이전트를 호출할 때의 귀속. 표준·학술 모두 미해결.
- **등록·소유·감사의 운영 비용을 처음부터 넣은 손익 모델** — RPA 실패를 반복하지 않기 위한 필수 작업인데 공개 자료가 없다.

## 7-3. 편향 경고 (BLOCKING)

1. **커뮤니티 인용의 약 80%가 Hacker News.** HN은 **AI 회의론이 과대표되는 곳**이다. 스레드 안에서 `keeda`가 직접 "HN은 대체로 에코 챔버"라고 지적했고, **이 경고는 이 문서 자체에 적용된다.** → **"커뮤니티에서는"과 "업계에서는"을 절대 혼용하지 말 것.**
2. **A2A #1672**(658댓글)는 자기 프로젝트 홍보 계정 교차 게시 정황 + 균질한 AI 생성 의심 문체. **여론 근거가 아니라 설계 쟁점 자료로만.**
3. **shadow AI·NHI 비율 통계는 전부 벤더·업계 조사**다. **분위기 전달용으로만 쓰고 논증 하중을 실으면 안 된다.**
4. **NHI 대 인간 비율은 기관마다 45:1 ~ 144:1로 갈린다** (CSA 45:1 평균·144:1 클라우드 네이티브 / CyberArk 82:1 / Palo Alto 109:1 / Entro 144:1). **단일 수치 단정 금지.** 오히려 **"아무도 정확히 세지 못한다"** 가 이 책의 논지(그래서 등록이 필요하다)를 강화한다.
5. **"AI가 87,714개 일자리를 없앴다"류 수치는 근거가 취약하다 — 쓰지 마라.**

## 7-4. 자기 검증 1패스 결과

합성 후 ⚠️ 항목·수치·연도·기관명을 재확인했다. **본문 저술 전 반드시 해소해야 할 우선순위:**

**최우선 (BLOCKING — 지어내면 책이 죽는다):**
| # | 항목 | 조치 |
|---|---|---|
| A-1 | 한국 은행권 RPA 로봇 사번 부여 | **본문에 쓰지 마라.** 검증 실패 |
| A-2 | Goldman Sachs가 Devin에게 사번을 줬다 | **근거 없음.** "employee #1"은 매체 수사. "파일럿"으로만 |
| C-10 | "AI가 87,714개 일자리 삭감" | **쓰지 마라** |
| — | 존재하지 않는 논문 인용 | 서지 ⚠️ 표시 항목은 원문 확인 전 인용 금지 |

**높음 (이 책에 가장 유용한데 미확보 — 저술 전 확인):**
| # | 항목 | 확인처 |
|---|---|---|
| B7 | **Adler & Borys의 enabling 형식화 4대 설계 특성** | `faculty.marshall.usc.edu/Paul-Adler/research/ASQ copy-1.pdf` |
| ~~B8~~ | ~~Kellogg et al. "6 Rs" 개별 항목명~~ | **✅ 2차에서 해소 — §2-4-2(588행) 참조** (`restricting`·`recommending`·`recording`·`rating`·`replacing`·`rewarding`, PDF 원문 대조). ⚠️ 종전 "§10-3 참조"는 잘못된 참조였다 — §10-3에 Kellogg 항목이 없다 (2026-09-06 정정) |
| A13 | Kotter's Contradiction (위기감 조성의 역효과) | DOI: 10.1080/14697017.2022.2137835 |
| B2 | Dell'Acqua "19%" vs "19%p" | *Organization Science* 게재본 |
| B1 | AI Agent Index 공시 비율의 판본 | arXiv:2502.01635 vs 2602.17753 초록 대조 |

**신선도 (🕒 2026-09-05 기준 — 빠르게 바뀜):**
| # | 항목 | 주의 |
|---|---|---|
| B-1 | **EU AI Act 고위험 시행일 2026-08-02 → 2027-12-02 연기** | **구버전 정보 다수 유통. 반드시 "2026년 9월 기준"으로 못 박을 것.** 금지조항·GPAI는 시행 중 |
| B-2 | Regulation (EU) 2026/1744 규정 번호·관보일(2026-07-24)·발효일(2026-07-27) | **EUR-Lex 원문 대조 필수** |
| B-3 | Digital Omnibus가 Art. 49를 어떻게 바꿨는지 | ⚠️ 미확인 |
| B-4 | SailPoint Agentic Fabric 현재 GA 여부 | 2026-05-11 "여름 GA 예정" → 재확인 |
| B-5 | MCP 스펙 개정 이력·2026-07-28 개정 내용 | spec 원문 미열람 |
| — | MCP/A2A/SPIFFE 이슈의 open/closed 상태 | **출간 시점에 전량 재확인** |

**수치 재확인 (원 조사 URL 미확보):** McKinsey 2026 전 수치(C1) / MIT NANDA 95%(C2, 방법론 병기 필수) / Prosci 38%·16%·72%·n=1,107(C3) / shadow AI 78%·55%·65% vs 31%(C4) / 직원 모니터링 77%·90%·22% vs 74%(C5, Pew 2023만 1차) / "API 키 오프보딩 공식 프로세스 20%"(C6, 출처 불명 — **재확인 또는 삭제**) / Cornell 감시 연구 원 논문(C7) / NHI 비율(C8) / 리스킬링 수치(C9) / Panasonic Connect 11,600명·44.8만 시간(C11) / CyberArk 특권 접근 42%·88%(C12)

## 7-5. 리서처 실패·재시도 이력

세 리서처(web / paper / community) **모두 정상 완료**했다. 재시도는 없었다. 각 리서처가 자기 커버리지 공백을 문서에 명시했고, 그 내용을 §7-1·7-2에 통합했다.

**리서처 간 이관 권고 (미처리 — planner·fact-checker 참고):**
- web-researcher가 검색 중 발견했으나 수집하지 않은 arXiv 3편 중 2편은 paper-researcher가 **독립적으로 확보했다** (2510.25819 OpenID 백서, 2604.23280 AI Identity). **arXiv:2604.04604 「AI Agents Under EU Law」는 양쪽 모두 미수집** — 축 1 제도 축에 직접 관련되므로 후속 확인 권장.
- Cornell 알고리즘 감시 연구 원 논문 — 양쪽 모두 미확보.
- SPIFFE/SPIRE·W3C VC/DID·EU AI Act 데이터베이스는 **피어리뷰 학술 논문이 없다.** 표준·법령 1차 문서로 직접 참조할 것.

---

# 8. 방향 문서 갱신 반영 (2026-09-05, 리서치 종료 시점)

> 리서치 진행 중 `00_direction.md`가 갱신됐다 — **관통선 교정(저자 승인 완료)** 과 **리서치 축 5 신설**. 세 리서처의 브리프에는 이 두 가지가 없었다. 아래는 **이미 확보한 자료로 무엇을 덮을 수 있고 무엇이 비었는지**를 정직하게 정리한 것이다.

## 8-1. 교정된 관통선 — 레퍼런스가 오히려 강하게 지지한다

**교정 후 정전:**
> ✅ **"바텀업이 씨앗을 만든다. 그러나 씨앗은 저절로 수확되지 않는다. 탑다운이 해야 할 일은 지시가 아니라 거두는 체계다."**
> 탑다운이 공급하는 것은 **과제 목록이 아니라 기준·자원·제도**다.

**리서치는 이 교정을 반박하지 않는다. 오히려 교정 전 논지("바텀업은 틀렸다")보다 훨씬 잘 뒷받침된다.** 근거 매핑:

| 교정된 명제 | 레퍼런스 근거 | 위치 |
|---|---|---|
| **아이디어는 계속 아래에서 온다** | 성공 사례의 공통점이 "강요하지 않음"(`caconym_`) / "자율성을 장려하는 문화에서만 상향식 도입이 가능"(GeekNews) / 탑다운 강제 반발 11건 | §2-3-7, §2-4-7, §4-5 |
| **찍어 누르면 실패한다 (SOP 포함)** | **Adler & Borys enabling vs coercive** — 문제는 형식화의 양이 아니라 유형 / `tdeck`: 실패 모드는 강제가 아니라 **맥락 무시한 획일화** | §1-5, §2-3-7 |
| **씨앗은 저절로 수확되지 않는다** | **MIT NANDA: "개인 생산성은 오르는데 조직 성과는 안 오른다"** / **Bick et al.: 채택은 인터넷보다 빨랐는데 절감은 총 근로 시간의 1.4%** / McKinsey: 개인 생산성 8/10 vs EBIT 37% 정체 | §2-3-1 |
| **탑다운이 공급할 것 = 기준·자원·제도** | **Klein & Sorra: implementation climate = 보상받고·지원받고·기대되는가** — 지시가 아니라 조건이다 / Deloitte의 결여된 3요소(경계·모니터링·감사 추적) | §1-6, §2-3-3 |
| **거두는 체계가 없으면 지식이 조직에 안 남는다** | **Dell'Acqua의 jagged frontier — 경계 안팎은 개인이 시행착오로 알 수 없고 조직이 축적해야 아는 지식** | §2-3-5 |
| **탑다운 = 강제(mandate)가 아니라 인프라·보증(guarantee)** | 커뮤니티 반론 3에 대한 답의 형태로 이미 §4-5에 정리됨 | §4-5 |
| **"무엇을 등록할지의 기준"** | Chan(2024) IDs: **결제·대외 커뮤니케이션에 닿는 에이전트부터** 등록하라 — 티어링의 학술 근거 | §5-1(9) |
| **"폐기의 규칙"** | **CSA: 78%가 생성·제거 정책 없음** / revocation ≠ deprovisioning / Entra의 soft-delete·cascade cleanup·스폰서 승계 | §1-3, §2-1-2 |

> **planner에게:** 이 교정은 §4-5(탑다운 vs 자율 논쟁)를 **책의 1장 반전으로 승격**시킨다. 그 논쟁 표의 좌우 열이 그대로 1장의 긴장이고, Adler & Borys의 enabling/coercive가 그 긴장을 푸는 열쇠다. **⚠️ B7(enabling 형식화 4대 특성)이 미확보라는 점이 여기서 더 아파진다 — 저술 전 확인 우선순위 최상위.**

## 8-2. 축 5 (등록된 에이전트의 성과관리·FTE·생산성) — 부분 확보

> **⚠️ 이 축은 세 리서처의 브리프에 없었다.** 아래는 다른 축을 파다가 함께 걸린 재료를 재배치한 것이며, **전용 리서치를 돌린 결과가 아니다.** 공백이 크다.

### (가) 확보한 것 — 카드 8·9의 설계를 직접 지지하는 근거

**① "자기보고를 그대로 받으면 숫자를 못 믿는다"(신뢰도 등급의 근거) — 실증이 있다.**
- **METR (2025):** 예측 −24% → **실측 +19%** → 사후 추정 −20%. **인식과 실측의 39%p 괴리.** 자기보고 기반 성과 인정이 왜 위험한지의 결정적 수치. (§2-3-6)
- **Bick et al. (2024):** 응답자가 **보고한** 절감 시간이 총 근로 시간의 **1.4%**. 자기보고조차 이 정도다. (§2-3-1)
- **적정 의존 개념:** 신뢰(태도)와 의존(행동)은 다르다 — **설문은 태도를 재고, 필요한 것은 행동의 정확성이다.** (§1-8)
> **→ 카드 8의 "신뢰도 등급(실측 전부 / 표본 할인 / 자기보고 절반)"은 문헌으로 방어된다.** 자기보고 등급에 폐지 시한을 못 박는 설계도 METR로 정당화된다.

**② "분모가 없다" — 분모 선택이 그림을 바꾼다는 방법론적 교훈.**
- **McElheran et al. (2024):** 같은 데이터에서 **기업 수 기준 채택률 6% 미만 vs 고용 가중 평균 18% 초과.** 분모를 무엇으로 잡느냐에 따라 성숙도 그림이 완전히 달라진다. (§참고문헌 36)
> **→ FTE 환산에서 "1 FTE는 연 몇 시간인가"를 인사가 정해줘야 한다는 카드 8의 지적과 같은 구조의 문제다.**

**③ "자율성 계수" — 제도·문헌 근거가 있다.**
- **Deloitte가 짚은 결여된 거버넌스 1요소:** "**clear boundaries for agents that define which decisions they can make independently versus which require human approval**" — 자율성 등급을 제도로 정의하라는 요구. (§2-3-3)
- **Laux의 구성적(constitutive) vs 교정적(corrective) 감독 구분** — 자율성 계수를 등록부 권한 필드로 옮기는 설계 언어. (§1-7)
- **Dietvorst(2018)의 수정 권한** — 사람이 남아 있는 단계를 없애는 것이 능사가 아니다. 작은 수정 권한이 수용과 성과를 함께 올린다. (§2-4-4)
> **→ "사람이 얼마나 남아 있는지에 따라 계수를 곱한다"는 카드 8의 설계는 등록부 권한 등급과 같은 축이다. 하나로 통합하면 책의 뼈대가 단단해진다.**

**④ 측정의 함정 — Goodhart는 이미 현장에서 실증되고 있다.**
- **"AI 사용량 자체를 성과 지표로 삼으면 사람들은 필요하지 않은 작업에도 AI를 사용해 숫자를 맞추게 될 수 있음"** (`brainer`, GeekNews, ≈2026-08-31) — 한국어 원문 인용 가능
- **지표 게이밍 실증 증언:** 준수해 보이려고 **사용량 비용을 인위적으로 부풀린다** (`plaguuuuuu`, 2026-06-28)
- **"사용량은 가치 있는 산출물이나 ROI와 상관관계가 없음"** (GN⁺, GeekNews, ≈2026-08-19)
- **Klein & Sorra:** **순응(compliance)과 헌신(commitment)은 다르다. 사용률만 보는 지표는 순응까지만 측정한다.** (§1-6)
- **J-curve:** 체계 구축기에 **측정 생산성이 오히려 떨어지는 것이 정상**이다 — 무형 투자는 비용으로 잡히고 산출로 안 잡힌다. **측정 체계를 세우는 초기에 숫자가 나쁜 것을 실패로 읽으면 안 된다.** (§2-3-2)
> **→ 카드 8·9의 측정 설계에 그대로 붙는 경고 세트.**

**⑤ "절감이 감원으로 읽히는 순간 현장은 성과를 숨긴다"(카드 9) — 저항의 실증 구조와 정확히 일치한다.**
- **"You work the same hours, but you're more tired, and the company pockets the profits"** (`pron`, 2026-03-28)
- **"as the individual productivity gets increased the amount of FTE per project goes down, and superfluous folks shown the door"** (`pjmlp`, 2026-03-27)
- **반증 카드:** Brynjolfsson et al.(2025)에서 AI 도입 후 **직원 유지율(retention)이 상승**했다. (§2-3-5)
- **처방의 실증:** **90%가 데이터 수집이 커리어상 이익과 연결되면 수용하겠다**고 답했다 (⚠️ C5). → **"재투자를 기본값으로 명시적으로 선언"하라는 카드 9의 처방과 같은 방향.**
- **Kellogg et al.:** 통제는 늘 **쟁투의 장** — 측정 체계 도입은 기술 프로젝트가 아니라 **협상**이다. (§2-4-2)
> **→ 카드 9("이 책 전체에서 가장 중요한 문장")는 커뮤니티 증언 3건 + 실증 반증 1건 + 처방 근거 1건으로 뒷받침된다.**

**⑥ "홍보성 수치 경계"(축 5 규율) — 레퍼런스에 라벨 체계가 이미 있다.**
§7-3 편향 경고와 각 항목의 `[PR]`/`[PP]`/★/△/⚠️ 라벨이 그 요구를 충족한다. 특히 **shadow AI·NHI 비율 통계는 전부 벤더 조사**이고, **MIT 95%는 편의표본**이며, **BCG는 2년 전 자료**다. **논증 하중은 피어리뷰 실증에만 실어라.**

### (나) 비어 있는 것 — 축 5의 진짜 공백

| 항목 | 상태 |
|---|---|
| **"digital FTE" / "digital labor" / agentic workforce planning 프레임·사례** | ❌ **전무.** 벤더(UiPath·Automation Anywhere 등)와 컨설팅사가 이 용어를 쓰는 것으로 알려져 있으나 **이번 리서치에서 검증하지 않았다.** 전용 조사 필요 |
| **RPA 시대 봇 FTE 환산 관행과 그 비판** | ❌ **전무.** 확보한 RPA 자료는 유지보수 손익 역전 회고 3건뿐 (§2-2-8). "봇 1대 = N FTE" 환산 관행의 1차 근거 없음 |
| **에이전트에 KPI를 부여한 사례** | ❌ **전무** |
| **사람+에이전트 팀의 성과 귀속(attribution)** | ⚠️ **개념만 있고 실증 없음.** human-agent teaming 문헌은 대부분 **의사결정 지원 도구** 맥락이며 **자율 실행자와의 성과 배분을 다룬 조직 수준 실증은 존재하지 않는다** (§7-2) |
| **정원 감축을 AI 성과로 보고·공시할 때의 회계 함정** | ❌ **전무.** 닛케이 2026-07-09 표제("비용은 인건비인가")만 있고 **본문 미확인(유료)** |
| **Goodhart's law의 원전·정식 인용** | ❌ 미수집. 현장 실증(위 ④)만 있다 |
| **생산성 역설의 최신 논의** | △ 부분 — J-curve(2017/2021)까지만. 2025~2026년 후속 없음 |
| **"등록된 자율 에이전트"의 생산성 실증** | ❌ **존재하지 않는다.** 축 3의 RCT는 전부 chat/completion 세대 (§7-2) — **책이 정직하게 밝히고 넘어갈 지점** |

> **✅ 【해소됨 — 2026-09-06】** 아래 권고 (A)를 **실제로 실행했다.** 2차 웹 리서치의 B절 + 2차 학술 리서치의 B절이 축 5를 전면 조사했다. **결과는 §9-5에 있고, 이 절의 "비어 있는 것" 목록은 §9-5 커버리지가 대체한다.** 특히 **RPA 봇 FTE 환산 계보**(권고에서 "PART 4의 설득력을 눈에 띄게 올린다"고 지목한 항목)를 확보했다. 아래 원문은 판단 근거로 남긴다.
>
> **planner·오케스트레이터에게 권고 (2026-09-05 시점 원문):** 축 5는 이 책 **PART 4의 중심 장**(카드 8·9)을 떠받쳐야 하는데 **외부 근거가 얇다.** 두 가지 선택지가 있다.
> **(A)** 축 5 전용 보강 리서치 1회 (`digital FTE`·`digital labor`·`agentic workforce planning`·RPA 봇 FTE 환산·Goodhart 원전 — web + paper 2인이면 충분).
> **(B)** 보강 없이 진행하되, **PART 4를 외부 사례가 아니라 저자의 설계론 + 위 (가)의 실증 근거로 세운다.** 카드 8·9는 이미 자체 완결적인 설계이고, (가)의 6개 묶음이 그 설계를 문헌으로 방어한다. **다만 "digital FTE는 업계에서 이미 이렇게 쓴다"는 식의 서술은 근거가 없으므로 금지.**
> **리서치 리드의 판단: (B)로도 책은 성립하되, (A)를 1회 돌리면 PART 4의 설득력이 눈에 띄게 올라간다.** 특히 **RPA 봇 FTE 환산의 실패 계보**는 카드 8의 "이번엔 다르다"를 증명하는 데 직접 쓰인다.

---

# 신선도 원장 (소스별 발행일·버전 시점)

> **Phase 4 fact-checker의 대조 근거.** 개별 `research/*.md`가 정리되더라도 그라운딩이 레퍼런스 안에 남도록 끌어올린 섹션이다.
> **모든 항목의 검색 시점: 2026-09-05 기준.**

## 제품·서비스 (버전·GA 시점)

| 소스 | 상태 시점 | 표기 규칙 |
|---|---|---|
| Microsoft Entra Agent ID | **GA 2026-05-01**, 문서 ms.date 2026-04-16 / 최종 갱신 2026-08-13·2026-09-03 | "2026년 중반 기준" |
| Microsoft Agent 365 | 발표 2025-11-18(Ignite), GA 2026-05-01, $15/user/월(연약정) | "2026년 중반 기준" ⚠️ GA일·가격 2차 |
| Okta Agent SSO | **GA 2026-08-24** | "2026년 8월 기준" |
| Okta Cross App Access (XAA) | 발표 2025-06-23 → **MCP 공식 확장 채택 2026-08-24** | "2026년 8월 기준" |
| Auth0 for AI Agents | 2026-05 발표, GA/프리뷰 구분 ⚠️ | "2026년 5월 발표 기준" |
| CyberArk Secure AI Agents | GA 2025년 말 (정확일 ⚠️) | "2025년 말 기준" |
| SailPoint Agentic Fabric | 발표 2026-05-11, "2026 여름 GA 예정" → 현재 상태 ⚠️ | "2026년 5월 발표 기준" |
| 1Password Unified Access | GA 2026-03 | "2026년 3월 기준" |
| Celonis Agent Mining × MS Agent 365 | 프라이빗 프리뷰 2026-05-01 (AgentC 2024-10-23 → Celosphere 2025-11-04) | "2026년 5월 프리뷰 기준" |

## 표준·프로토콜 (개정 시점)

| 소스 | 시점 | 표기 규칙 |
|---|---|---|
| MCP Authorization | 2025-03-26(OAuth 2.1 도입) → 2025-06-18(리소스 서버·RFC 8707) → **2026-07-28(최대 개정, stateless)** | "MCP 2026-07-28 개정 기준" |
| A2A (Agent2Agent) | Google 발표 2025-04-09 → Linux Foundation 기증 2025-06-23 → **v1.0**(signed agent card) | "A2A v1.0 기준" |
| AGENTS.md | 2025-08 형식화 (Linux Foundation Agentic AI Foundation 관리) | "2025년 8월 형식화 기준" |
| SPIFFE/SPIRE | 2025~2026 에이전트 적용 확산, HashiCorp Vault 1.21 네이티브 SPIFFE 인증 | "2026년 기준" |
| MCP/A2A/SPIFFE 이슈 상태 | **2026-09-05 조회 시점 전부 open (SEP-1933·2817·2787·2385 등, A2A #1672, SPIFFE #382/383/408)**. #2902만 closed | **"2026년 9월 기준 미확정"** — 출간 시 재확인 |

## 제도·규제 (시행일·개정일)

| 소스 | 시점 | 표기 규칙 |
|---|---|---|
| **EU AI Act (Reg. (EU) 2024/1689)** | 금지조항 Art.5 **2025-02-02 시행 중** / GPAI Art.51~56 **2025-08-02 시행 중** / **Annex III 고위험 → 2027-12-02 연기** / **Annex I → 2028-08-02 연기** | **"2026년 9월 기준"** — 구버전(2026-08-02) 정보 다수 유통 |
| Digital Omnibus on AI | 잠정 합의 2026-05-06, 이사회 확인 2026-05-13, Gibson Dunn 분석 2026-05-27 / ⚠️ Reg. (EU) 2026/1744·관보 2026-07-24·발효 2026-07-27은 2차 출처 | "2026년 5월 합의 기준" + EUR-Lex 대조 필요 |
| NIST AI RMF 1.0 | **2023-01** / Generative AI Profile (NIST AI 600-1) **2024-07** | "2023년판 기준" |
| ISO/IEC 42001 | **2023-12** (Annex A 38통제·9목적) | "2023년판 기준" ⚠️ 통제 번호 미확인 |
| 한국 AI 기본법 | **시행 2026-01-22**, 계도기간 최소 1년(≈2027-01까지) ⚠️ | **"2026년 1월 시행 기준"** |
| 개인정보위 안내서 | 생성형 AI 개인정보 처리 안내서 **2025-08-06** / 이용자 가이드 2026-05 | 각 발간 시점 명시 |
| 미국 OMB | M-24-10(2024-03) → **M-25-21(2025-04-03)로 폐지·대체** / 2025년 인벤토리 56기관 3,611건 | "M-25-21, 2025년 4월 기준" |
| 중국 알고리즘 등록제 | 잠행 조치 2023 / 등록 실적: 2025-03-31 346건 → 2025-08-31 801건 → 2025-11 누적 5,822건(67.3% 생성형) | 각 집계 시점 명시 |

## 조사·보고서 (발행일·표본)

| 소스 | 발행일 | 표본 | 표기 규칙 |
|---|---|---|---|
| **CSA 『NHI Governance Vacuum』** | **2026-05-20** | 미확인 | "2026년 5월 기준" |
| **Deloitte 『2026 State of AI in the Enterprise』** | **2026-04-24** | n=3,235, 24개국 | "2026년 4월, n=3,235" |
| Okta 『AI Agents at Work 2026』 | 2026 (필드 2026-03) | 경영진 292 + 지식근로자 492, 7개국 | "2026년, n=784" |
| **McKinsey 『State of AI: Global Survey 2026』** | 2026 (2026-08 보도) | ⚠️ **표본·필드 기간 미확인** | "2026년 기준" + 표본 미상 명시 |
| **MIT NANDA 『The GenAI Divide』** | **2025-07** 발표 (2025-08 보도) | 300+ 이니셔티브 리뷰 / 52 인터뷰 / **153 설문(컨퍼런스 편의표본)** | **"2025년 7월, 편의표본 n=153"** — 방법론 병기 BLOCKING |
| BCG 『Where's the Value in AI?』 | **2024-10-24** | n=1,000 CxO, 59개국 | **"2024년 10월 기준"** — 2년 전 자료 |
| Gartner 에이전틱 취소 예측 | **2025-06-25** | 웨비나 폴 n=3,412 | "2025년 6월 예측" |
| Pew Research 직원 모니터링 | **2023-04-20** | — | "2023년 기준" |
| Cyberhaven shadow AI (민감정보 11%) | 2026 | — | "2026년 기준" |
| Microsoft Work Trend Index (BYOAI 78%) | 2025 ⚠️ | — | "2025년 기준" ⚠️ 원 조사 URL 미확보 |
| Prosci ADKAR 연구 | ⚠️ 발행일 미확인 | n=1,107 ⚠️ | 원문 확인 후 사용 |

## 학술 문헌 (발행 연도·버전·모델 세대)

| 소스 | 발행 | 버전/세대 | 표기 규칙 |
|---|---|---|---|
| Chan et al. 「Visibility into AI Agents」 | FAccT '24 | arXiv:2401.13138 **v6 (2024-05-17)** | "2024년, FAccT 게재" |
| Chan et al. 「Infrastructure for AI Agents」 | TMLR | arXiv:2501.10114 **v3 (2025-06-19)** | "2025년, TMLR 게재" |
| Chan 「IDs for AI Systems」 | 2024-06-17 (수정 2024-10-28) | arXiv:2406.12137 `[PP]` | "2024년 프리프린트" |
| South et al. 「Authenticated Delegation」 | arXiv 2025-01-16 / ICML 2025 | 제목이 다름 — 인용 시 어느 쪽인지 명시 | "2025년, ICML 포지션 페이퍼" |
| OpenID Foundation 백서 | **2025-10-29** | arXiv:2510.25819 v1 | **"2025년 10월 표준 지형 기준"** |
| Otsuka et al. 「AI Identity」 | **2026-04-25** | arXiv:2604.23280 `[PP]` | **"2026년 4월 표준 지형 기준"** |
| 「Auditable Agents」 | v1 **2026-04-07** / v2 **2026-08-13** | arXiv:2604.05485 `[PP]` | "2026년, 이 실험 조건에서" |
| Kaptein et al. 「Runtime Governance」 | **2026-03-17** | arXiv:2603.16586 `[PP]` | "2026년 3월 프리프린트" |
| MOISE+ | 2002 | SBIA 2002, LNAI 2507 | "2002년 — LLM 이전 심볼릭 MAS" |
| Feldman & Pentland | 2003 | ASQ 48(1) | 연도만 |
| Adler & Borys | 1996 | ASQ 41(1) | "1996년, 제조업 맥락" |
| Klein & Sorra | 1996 | AMR 21(4) | 연도만 |
| Skitka et al. | 1999 | IJHCS 51(5) | **"1999년 항공 시뮬레이션"** |
| Brynjolfsson, Hitt & Yang | 2002 | Brookings 2002(1) | **"1990년대 컴퓨터 도입 데이터"** |
| Brynjolfsson, Rock & Syverson | 2017 (WP) / 2021 (AEJ) | NBER 24001 | "2017년 시점 진단" |
| **Brynjolfsson, Li & Raymond** | QJE 2025 (NBER WP 2023-04) | **도입 시점 GPT-3.5 세대** | "GPT-3.5 세대, n=5,172" |
| **Dell'Acqua et al.** | Org Sci 2025 (HBS WP 2023-09) | **2023년 GPT-4** | **"2023년 GPT-4 기준, n=758"** |
| Noy & Zhang | Science 2023-07-13 | **2023년 초 ChatGPT(GPT-3.5)** | "2023년 초, n=453, 글쓰기 단발 과제" |
| Peng et al. (Copilot) | arXiv 2023-02-13 | GitHub Copilot 초기 | **"2023년, 단일 그린필드 과제"** ⚠️ N 미확인 |
| Cui et al. | Mgmt Sci 2025 | **코드 완성 도구 세대** | "n=4,867, 3개 기업 현장 RCT" |
| **METR** | **2025-07-10** | **2025년 2~6월, Cursor Pro + Claude 3.5/3.7 Sonnet** | **"2025년 상반기, n=16/246과제, 성숙 코드베이스"** |
| McElheran et al. | JEMS 2024 | **2018년 Annual Business Survey — 생성형 AI 이전** | **"2018년 기준"** — 현재 수치로 오도 금지 |
| Bick, Blandin & Deming | NBER WP 2024-09 | **2024년 8·11월 설문** | **"2024년 말 기준"** — 갱신 가능성 |
| **SOP-Bench** | v1 2025-06-09 / **v2 2026-02-23** | **Claude 4 Opus·4.5 Sonnet 라인업** | **"2026년 2월 시점 평가"** |
| MetaGPT | ICLR 2024 | 2023~2024년 모델 기준 | "2023~2024년 모델 기준" |
| Green | CLSR 2022 | 41개 정책 (정부 알고리즘 맥락) | "2022년, 정부 알고리즘 41개 정책" |
| Laux | AI & Society 2023-08-25 | EU 맥락 | 연도 명시 |
| Buçinca et al. | PACM HCI 2021-04-22 | CSCW 2021 | 연도 명시 |
| Kellogg et al. | AMA 2020-01-15 | 리뷰 논문 | 연도 명시 |
| Dietvorst et al. | 2015 (JEPG) / 2018 (Mgmt Sci) | 실험실 예측 과제 | 각 연도 명시 |
| Logg et al. | OBHDP 2019 | **일반인(lay people) 대상** | "2019년, 일반인 대상" |
| Hughes | JCM 2011-12 | 5개 출처 문헌 추적 | 연도 명시 |
| Shonhe & Min | AI & Society 2025-01-15 게재 | **동·남부 아프리카 RIM 전문가 n=413** | **"2025년, 단일 직군·단일 지역, n=413"** |
| Ravid et al. EPM 메타분석 | Personnel Psychology 2023 | ⚠️ 표본 귀속 미확정 | 확정 후 사용 |
| AI Incident Database | AAAI 2021 | **"1,000건 이상"은 2021년 수치** | **현재 숫자 별도 확인 필수** |

## 커뮤니티 (게시일 — 시점 명시 없이 인용 금지)

| 구간 | 항목 | 표기 규칙 |
|---|---|---|
| **2013~2015** | 오프보딩 불만(`olegp` 2013-10-07), 오프보딩 실패 침해(`netik` 2015-06-16) | **"13년 전"·"11년 전"임을 반드시 밝힐 것** — 오히려 그것이 논거다 |
| **2019~2024** | Confluence 냉소 5건 (2019-03-19 / 2020-07-12 / 2022-02-06 / 2023-08-17 / 2024-02-14) | "약 5년간 반복된 문장" (첫 건 2019-03-19 ~ 끝 건 2024-02-14 = **4년 11개월**. "7년"은 오기였다 — 2026-09-06 정정) |
| **2024-10** | AI 강제 사용 예고(`Balgair`, "2년 안에") | **"2년 전 발언 — 지금이 그 시점"** 대비로 활용 |
| **2025-02** | OWASP NHI Top 10 스레드 (용어 냉소 4건) | "2025년 2월" |
| **2025-08** | MIT 95% 스레드 + 방법론 반박 2건 | **"2025년 8월"** — "최근 화제"라고 쓰지 말 것 |
| **2025-12** | Everyone in Seattle hates AI (967점·1065댓글) | "2025년 12월" |
| **2026-02 ~ 2026-09** | 탑다운 강제 반발 다수, 감시 증언, AGENTS.md 회의론, RPA 회고, 조직도 폭발(`yego` 2026-03-04), 조직도 등록 반대(`polotics` **2026-09-04**) | 개별 게시일 명시 |
| **GeekNews (상대 표기)** | topic 29217 ≈2026-05 / topic 33050 ≈2026-08-31 / topic 32661 ≈2026-08-19 / topic 20489 2025-04-23 | **"2026-09-05 조회 기준 추정"** 병기 |
| **OKKY** | articles/1532084 "1년 이상 전" | 시점 불확정 명시 ⚠️ |
| **GitHub 이슈 상태** | 전부 2026-09-05 조회 | **"2026년 9월 기준 미확정(open)"** — 출간 시 재확인 |

---
---

# 9. 2차 보강 (리서치 2라운드, 2026-09-06 완료)

> **왜 2차를 돌렸나.** 1차 종료 후 방향 문서에 **관통선 교정**과 **축 5(성과관리·FTE·생산성)** 가 추가됐고, 축 1의 **검증 리드**와 **수락 기준**이 하달됐다. 2차 원자료: `research/web2.md`(1,129행) · `research/papers2_A_autonomy.md`(1,356행) · `research/papers2_B_measurement.md` · `research/papers2_C_orgtheory.md`(1,057행) · `research/community2.md`(1,527행). **전부 보존한다.**
>
> **1차와 충돌하는 곳은 이 섹션이 우선한다.** 충돌 지점은 §9-0에 모아뒀다.

## 9-0. 2차가 바꾼 것 — 【논지 조정 3건, 저술 전 필독】

### 조정 1. 폐기 — "아무도 설계 안 한다" → **"이미 설계돼 있다. 켜져 있지 않을 뿐이다."**

1차의 서술("다들 들이는 건 설계하는데 내보내는 건 아무도 설계 안 한다")은 **2026년 9월 기준 그대로 쓰면 사실과 어긋난다.** 2차에서 반례가 다수 나왔다:
- **Microsoft Entra ID Governance**: access package **만료일 자동 소멸** + 연장 시 **재승인 사이클** + **후원자 퇴사 시 그의 매니저에게 책임 자동 승계** (공식 문서 ★, ms.date 2026-06-05)
- **EU AI Act Annex VIII Section A-7**: 시스템 상태 값에 `no longer available`, **`recalled`** 존재 (규제 원문 ★)
- **미 연방 AI 인벤토리**: `development_stage` 값에 **`Retired`** 존재 (정부 원자료 ★)
- **Saviynt 6단계 라이프사이클**: Retirement 단계의 7항목 체크리스트 (벤더 프레임)

> **그러나 "실제 조직이 공개한 폐기 절차"는 여전히 0건이다.** 7개 검색어 + 6개 기업 엔지니어링 블로그 + 공공기관 정책을 뒤진 기록이 `web2.md` A-6-⑥에 남아 있다.
> **→ 조정안: "도구는 이미 폐기를 설계했다. 조직이 아직 안 켰다."** 1차의 **CSA 78%(생성·제거 정책 없음)** 와 결합하면 원래 주장보다 **더 날카로워진다.**

### 조정 2. BNY — **사번이 아니다. 사용자 ID다.**

업계에 "BNY가 AI에 사번을 줬다"고 회자되나, **CEO 발언 원문에 `employee number`는 없다.**
> **"We also have digital employees — multi-agent solutions wrapped with a `user ID, a login, a persona, a name`"** — Robin Vince, BNY CEO, 2026-03-23

그리고 **BNY 공식 웹사이트는 "digital employees"라는 표현조차 쓰지 않는다** — "AI-enabled solutions"만 쓴다. 디지털 직원 프레이밍은 전부 **경영진 구두 발언과 기자 서술**에서 나온다.
> **→ 저술 규율: "사번"이라 쓰지 마라. "사용자 ID와 로그인, 이름과 페르소나를 부여하고 사람 매니저를 붙였다"까지만.** Deutsche Bank 'Yi'(인사 시스템 사번, 2020)와 **층위가 다르다** — 이 층위 차이 자체가 좋은 서술 소재다.

### 조정 3. 축 3 — 교정된 관통선의 **실증 뼈대를 찾았다**

**DORA 2025** (*State of AI-assisted Software Development*, Google Cloud) 공식 결론 (원문 ★):
> "AI's primary role is as an **amplifier**, magnifying an organization's **existing strengths and weaknesses**. The greatest returns on AI investment come **not from the tools themselves, but from a strategic focus on the underlying organizational system**."
> 고성숙 조직 — **강한 버전 관리, 관측성, 그리고 내부 플랫폼(internal platforms)** 을 갖춘 조직 — 이 **불균형하게 큰 편익**을 본다.

> **→ "AI는 팀을 고치지 않는다. 팀을 증폭한다."** 이 문장 하나가 축 3(중앙이 공급할 것)과 축 5(성과 측정)를 연결한다. **중앙이 무엇을 공급해야 하는가에 대한 실증적 답이다 — 과제 목록이 아니라 버전 관리·관측성·내부 플랫폼.**

### 【교차 발견】 거버넌스와 플랫폼은 같은 함정을 공유한다

- **Gartner (2026-05-26):** 단순 에이전트에 **과잉 제한** → 딜리버리 지연 + **섀도 개발(shadow development)** 유발
- **Golden Cage Syndrome (2026-03-05):** 플랫폼 **강제** → **"Mandatory adoption breeds workarounds"**, 개발자가 raw AWS 자격증명으로 우회

> **같은 실패 모드다.** 축 1(거버넌스)과 축 3(플랫폼)이 구조적으로 연결된다는 논거 — 이 책의 뼈대에 쓸 수 있다.

---

## 9-1. 【수락 기준 대조】 축 1 자가 판정표

> 팀 리드가 하달한 6개 통과선에 대한 정직한 자가 판정. **억지로 채우지 않았다.**

| # | 기준 | 판정 | 확보 건수 | 근거·사유 |
|---|---|---|---|---|
| **1** | **운영 확인 사례 ≥ 3건** (발표가 아닌 실제 시행, 6개 항목 전부 기재) | **⚠️ 조건부 충족 (3건)** | **3** | ① **Deutsche Bank Blue Bot 'Yi'**(2020-07-20, 사번+이메일, 공식 보도자료 ★) ② **BNY**(2025-07~2026-03, 130+ 운영 중, **사번 아닌 user ID** — 조정 2) ③ **Microsoft 자사 IT**(Agent 365로 사내 에이전트 관리, GA+자사 적용). **⚠️ 단 셋 다 감사·폐기 칸이 완전히 채워지지 않았다** — DB는 미공개, BNY는 미공개, MS만 문서화. **엄격히 보면 6항목 전부 채워진 건 1건(Microsoft)뿐이다.** |
| **2** | **벤더 제품 ≥ 4건** (GA/프리뷰/발표만 라벨 + 가능하면 과금) | **✅ 충족 (9건)** | **9** | GA: Entra Agent ID(2026-05-01)·Agent 365·Okta Agent SSO(2026-08-24)·1Password(2026-03)·CyberArk(2025말)·**Workday ASoR(2026-02)**·**ServiceNow AI Control Tower**·**AWS Bedrock AgentCore Identity(2025-10)** / 발표·GA 미확정: SailPoint(2026-05-11)·Auth0. **과금 구조 확보:** Agent ID 자체는 전 Entra 고객 무상, 실사용은 **Agent 365 per-user 라이선스 필요**(§9-2-3) |
| **3** | **자율성 등급 프레임 ≥ 2종** (등급 정의 + **등급별 통제 차등**) | **✅ 초과 충족 (실무 4종 + 학술 9종)** | **13+** | 실무: **Gartner 4단계**·**CSA L0~L5**·**Feng L1~L5 + 자율성 인증서**·Salesforce(통제 차등 △). 학술: **AAL/ACL 이원 체계(ExxonMobil)** 외 8종 + **1978년 Sheridan 원전 계보**. §9-3 전체 |
| **4** | **규제·표준 조문 대조 ≥ 3종** (조문/섹션 번호까지) | **✅ 충족 (6종)** | **6** | EU AI Act **Art.49 + Annex VIII 전 항목**(★) / 미 OMB **M-25-21 + 인벤토리 36필드 전체**(★) / 중국 알고리즘 등록제 / 한국 AI 기본법 / NIST AI RMF / ISO 42001. **⚠️ 단 NIST 서브카테고리 번호·ISO Annex A 통제 번호·한국 조문 번호는 미확인** (§7-4 A-4·A-5·A-6) |
| **5** | **폐기·재심사 절차 사례** | **✅ 충족 — 단 논지 조정 필요** | 벤더/규제 **4건** / **조직 0건** | 반례 4건 확보(조정 1). **실제 조직 공개 사례는 0건이며, 뒤진 곳 13개를 `web2.md` A-6-⑥에 기록**했다. **"없다"가 아니라 "도구엔 있고 조직엔 없다"가 정확한 판정** |
| **6** | **지역 분포** (미국 일변도면 미달, 유럽·아시아 각 1건 이상 시도 흔적) | **⚠️ 조건부 충족** | — | **유럽 ✅** Deutsche Bank(독일, 사번 부여 1차 사례) + EU AI Act. **아시아 ⚠️** 일본 닛케이 2026-07-09(**유료로 본문 미확보**, 표제·리드만) / 중국 알고리즘 등록제(제도만, 기업 사례 없음) / **한국 기업 사례 0건**(1·2차 모두 실패, 뒤진 기록 §7-1). **미국 편중이 사실이다** |

### 종합 판정

**6개 항목 중 4개 충족, 2개 조건부 충족(①⑥).** 기준 ③(자율성 등급)은 **1차에서 0건이었으나 2차에서 초과 달성**했다 — 이것이 2차의 최대 성과다.

**2차 보강으로도 메우지 못한 두 구멍을 명시한다:**
1. **운영 사례의 "감사·폐기" 칸이 비어 있다.** 조직들은 **등록했다는 사실은 말하고 폐기 절차는 말하지 않는다.** 이 비대칭 자체가 이 책의 발견이다(조정 1과 같은 구조).
2. **한국 기업 사례 0건.** 대상 독자가 한국 AX 실무 리더인데 국내 사례가 없다. **3차 리서치로도 공개 웹에서 나올 가능성은 낮다 — 사내 인터뷰·비공개 취재가 필요한 영역으로 판단한다.**

> **오케스트레이터 판단 요청:** 위 두 항목을 근거로 3차 보강을 돌릴지, 아니면 공백을 명시한 채 Phase 2로 넘어갈지. **리서치 리드 의견은 후자다** — 3차를 돌려도 공개 출처에서 나올 것은 소진됐다고 본다.

---

## 9-2. 축 1 보강 — 검증된 사례

### 9-2-1. BNY (미국·은행) — 운영 중, 130+ 규모

| 시점 | 규모 | 표현 | 출처 | 라벨 |
|---|---|---|---|---|
| 2025-07-10 | "dozens"(수십) | 운영 중 | CU Today (WSJ 인용) | `[매체 보도]` |
| 2025-10-17 | "over 100 digital employees" | 운영 중 | Axios (✗ 403, 스니펫만) | `[매체 보도]` |
| 2026-03-23 | **"over 130 specialized Digital Employees", "125+ live use cases", "20,000 Empowered Builders"** | 운영 중 | TBPN Digest (CEO 인터뷰) | `[매체 보도]` |

**확인된 설계 (WSJ 경유, 2025-07):**
- 초기 2개 페르소나: **코드 취약점 식별·수정** / **지급 지시(payment instruction) 검증** — BNY AI Hub 개발
- **회사 로그인** 보유, 이메일 계정 부여 예정, Teams 협업 가능성
- **사람 라인 매니저에게 보고** — "report to direct managers who **review and approve their work**"
- **접근 통제:** 각 인스턴스는 **좁게 정의된 팀에 한정** 배치, 전사 정보 접근 없음

**CIO Leigh-Ann Russell 인용 (The Stack 직접 인터뷰 ★, 2025-08-26):**
> "We have more than 40 AI solutions in full production. They touch almost everything at the bank"
> "**8,000 of those people – bear in mind, we're a 50,000 person bank – are building their own agents**"
> "we have 85% of the bank fully trained"

> **⚠️ 저술 규율 (조정 2 재확인):** **① "사번"이라 쓰지 마라** ② **"경영진이 밝힌 바에 따르면"을 붙여라** — 회사 보도자료 원문이 없고 공식 웹페이지는 이 표현을 안 쓴다 ③ **매니저 지정이 인사 시스템상 실제 보고 라인인지는 불명** ④ WSJ 원 기사는 유료로 미대조.

### 9-2-2. Workday Agent System of Record — **Lattice 실패의 대칭 사례** 【핵심 장면】

1차에서 "**Lattice(실패)의 대칭이 없다**"를 축 4 최대 공백으로 기록했다. **2차에서 찾았다.**

- 발표 **2025-02-11** → **GA 2026-02** (일자 미표기 ⚠️ — "2026년 2월"까지만)
- 해결 대상 문제를 Workday가 명명한 이름: **"agent sprawl"**
- **Agent Registry** 필드: 에이전트 목록, 설명, **어느 보안 그룹이 접근 권한을 갖는지**, 국가별 가용 지역, **현재 상태(status)** + 비용·ROI

**결정적 원문 (Workday 블로그 ★):**
> "agents become part of an organization's workforce strategy — **measured like investments, governed like employees, and improved by training and learning**."

| | **Lattice (2024-07, 3일 만에 철회)** | **Workday ASoR (2025 발표 → 2026 GA)** |
|---|---|---|
| 배치 위치 | **HR 시스템 안, 사람 직원과 같은 레코드** | **별도 Agent Registry** (HCM·재무와 *연동*하되 분리) |
| 용어 | "AI **employees**" — **직원이라고 불렀다** | "**agents**", "digital labor", "digital workforce" |
| 프레이밍 | 사람과 **동렬** | "governed **like** employees" — **"like"가 들어간다** |
| 관리 축 | 인사 평가 축에 편입 시도 | **비용·ROI·접근권한·상태** 축 |
| 결과 | **3일 만에 철회** | **GA, 제품으로 존속** |

> **이 책의 문장:** **Workday가 다르게 한 것은 위치와 조사(助詞)다. 에이전트를 직원*으로* 만들지 않고, 직원*처럼* 통치했다.** 레지스트리를 인사 레코드와 **분리**하되 같은 플랫폼에서 **나란히 보이게** 했다.
> → 1차의 교훈("에이전트를 조직에 등록하되 사람의 자리에 앉히지 마라")이 **실패 사례 1건 + 성공 사례 1건으로 완성된다.**

### 9-2-3. Entra Agent ID 라이선스 — **"에이전트마다 사람 라이선스를 사야 하나"의 답**

> **답: 아이덴티티 생성 자체는 아니다. 하지만 실제로 쓰려면 산다.**

공식 문서 원문 (★): "Microsoft Entra Agent ID ... **Agent ID is available for all Microsoft Entra customers.**"

| 기능 | 필요 라이선스 |
|---|---|
| 에이전트 신원 생성·관리 (Agent ID 자체) | **모든 Entra 고객** (추가 비용 없음) |
| 에이전트가 M365 서비스·워크플로에서 동작 | **Microsoft Agent 365 (per user)** |
| Conditional Access 적용 | Entra ID **P1** |
| ID Protection(위험 탐지) | Entra ID **P2** |
| **ID Governance**(액세스 검토·라이프사이클) | **M365 E7** (Agent 365 + Entra Suite 포함) 또는 **Agent 365 + Entra P1/M365 E3** |

- 가격: Agent 365 **약 $15/user/월**, Entra Suite 약 $12/user/월 ⚠️ **가격 페이지 직접 대조 실패 — "약" 표기 필수**
- **4종 신규 객체** (★): `agent identity blueprint` / `blueprint principal` / `agent identity` / **`agent user`** — "optionally an **agent user** for each agent identity. Each agent identity and agent user can have **distinct access rights**."
- ⚠️ `agent user`가 M365 시트를 소비하는지는 **명시 문장 미확보**

> **책에서의 값어치:** 카드 5('라이선스 벽')의 **공개 대응물**. 그리고 커뮤니티 반론과 정확히 맞물린다 — **"If a company gets more efficient and uses fewer people, Microsoft's immediate reaction is to figure out how to invent some kind of digital seats so they can keep taxing the headcount."** (`latand6`, HN, 2026-04-14)

### 9-2-4. 벤더 지형 보강 (1차 §3-2에 추가)

| 조직/제품 | 식별자 | 권한 모델 | 감사·폐기 | 시행 여부 | 발행일 |
|---|---|---|---|---|---|
| **ServiceNow AI Control Tower** | **AI Asset Inventory** 레코드 — systems/models/prompts/datasets/**MCP servers**, 각각 provider·vendor·**lifecycle phase**·state·**risk classification** | CMDB·CSDM 관계 연결 | **lifecycle phase / state 필드 보유** — 폐기 단계가 데이터 모델에 존재 | **GA**. **2026-06 릴리스부터 관리 에이전트를 Microsoft Agent 365 디렉터리로 직접 게시** | 2026-06 |
| **AWS Bedrock AgentCore Identity** | 에이전트/워크로드별 고유 identity + 메타데이터, 중앙 **agent identity directory** | on-behalf-of 인증·인가, 서드파티 자격증명 관리 | 감사 추적 명시. 폐기 절차 미확인 ⚠️ | **GA (2025-10)** | 2025-10 |
| **Salesforce Agentforce** | 에이전트 정의 + Agentic Maturity / Levels of Determinism | Assistive vs Autonomous 구분, 6단계 agentic control | 미확인 ⚠️ | **GA** | 2026 |
| SAP Joule / Google Gemini Enterprise / Atlassian / Slack | **⚠️ 미확인·미조사** | — | — | — | — |

> **주목할 상호운용 사실:** ServiceNow가 **자기 레지스트리의 에이전트를 Microsoft Agent 365 디렉터리로 게시**하고 "single source of truth for governance is maintained across both registries"를 표방한다. **→ 에이전트 레지스트리 간 연합(federation)이 2026년에 시작됐다.**

---

## 9-3. 【신규】 자율성 등급 — 이 책의 핵심 장치

> 1차에서 **0건**이었다. 2차에서 **실무 4종 + 학술 9종 + 1978년까지 거슬러 가는 계보**를 확보했다. **이 절이 2차의 최대 성과이며, PART 3의 중심 장치가 될 수 있다.**

### 9-3-1. 실무 프레임 4종 — 등급별 통제 차등

| # | 프레임 | 유형 | 등급 수 | **통제 차등** | 발행일 |
|---|---|---|---|---|---|
| 1 | **Gartner 비례적 거버넌스** | `[컨설팅 조사]` | **4** | **✅ 가장 명확** | **2026-05-26** |
| 2 | **CSA Autonomy Levels** (Jim Reavis) | `[표준·기관]` | **6 (L0~L5)** | **✅** | **2026-01-28** |
| 3 | **Feng·McDonald·Zhang** (UW/Knight) | `[학술]` | **5 (L1~L5)** | **✅ + 자율성 인증제** | **2025-07-28** |
| 4 | Salesforce Agentic Maturity Model | `[벤더]` | 5 (L0~L4) | **△ 부분적** (성숙도 축이 주) | 2025-04-10 |

**(가) Gartner 4단계 — 실무 리더에게 가장 직접적** (⚠️ 원문 403, **3개 매체 교차 일치**)

> 분석가 Shiva Varma: **"Enterprises are treating AI agent governance as `binary, either locked down or fully trusted`, and that is the root cause of failure."**

| 레벨 | 이름 | 할 수 있는 일 | **차등 통제** |
|---|---|---|---|
| **L1** | **Observe** | 정의된 소스에 **읽기 전용**. 출력은 요청자에게만 | **경량** — 범위 지정 데이터 접근, 사용자 인증, **사용 로깅**, 기본 보안 테스트 |
| **L2** | **Advise** | 추천·초안 **생성**. 사람이 검토 후 수동 실행. 쓰기 없음 | L1 + **정확도/할루시네이션 테스트**, 도메인 품질 평가, **적정 의존 교육** |
| **L3** | **Act with Approval** | 데이터 쓰기·통신 발송·구성 변경. **매 행동마다 명시적 승인** | **강한 보안 테스트**, **감사 추적 갖춘 승인 워크플로**, **에이전트 전용 인시던트 대응 절차** |
| **L4** | **Act Autonomously** | 가드레일 안에서 **독립 실행**. 사람은 **예외·감사 로그·집계 결과**만 검토 | **지속 모니터링**, 강제 가드레일, **신속 롤백**, **서킷 브레이커**, **명확한 소유권** |

- 두 실패 모드: **과잉 제한** → 딜리버리 지연 + **섀도 개발** / **과소 제한** → 운영·보안·컴플라이언스 리스크
- 예측: "by **2027, 40% of enterprises will demote or decommission autonomous AI agents** due to governance gaps identified only after production incidents occur."
  > **⚠️ 1차의 "Gartner 40% 프로젝트 취소"(2025-06-25)와 다른 예측이다. 혼동 금지.** 이건 **강등 또는 폐기**다.

**(나) CSA 6단계 — L3의 결정적 문장**

| L | 이름 | 원문 정의 | **차등 통제** |
|---|---|---|---|
| **L0** | No Autonomy | "provides information... but **humans perform all actions**" | 출력 품질·정보 유출 방지 |
| **L1** | Assisted | "**each action requires explicit human approval**" | 명확한 **승인 게이트** |
| **L2** | Supervised | "review and approve **a plan or batch of actions**" | 건별 승인 → 상위 인가. **모니터링 + 롤백 필수** |
| **L3** | Conditional | "**within defined boundaries**, escalating only when it exceeds those" | **기계가 읽을 수 있는 경계 정의 + 기술적 강제(정책 문서만으로는 불가)** |
| **L4** | High Autonomy | 인간이 **승인에서 모니터링·예외 처리로 이동** | 지속 모니터링, 이상 탐지, **킬 스위치**, **경영진 수준 리스크 수용** |
| **L5** | Full Autonomy | **목표 설정 + 자기 행동 수정** 가능 | 저자 직접: **"I don't believe Level 5 is appropriate for enterprise deployment today."** |

> **L3의 "기계가 읽을 수 있는 경계 정의 + 기술적 강제 — 정책만으로는 불가"가 이 책의 "체계는 문서가 아니라 시스템"이라는 논지에 직결된다.**

**(다) Feng·McDonald·Zhang — 사용자 역할 축 + 자율성 인증서** (arXiv:2506.12469 / Knight Columbia)

L1 User as **Operator** → L2 **Collaborator** → L3 **Consultant** → L4 **Approver** → L5 **Observer**

> **진짜 기여는 인증서다:** 인증서는 "**prescribes the maximum level of autonomy at which an agent can operate**" — **자율성 상한**을 규정한다. 개발자가 에이전트 + **"autonomy case"**(해당 등급 이하로 동작함을 입증하는 증거 기반 논증)를 제출 → **제3자 거버닝 바디**가 평가·발급. **기술 사양이나 운영 환경이 바뀌면 갱신 필요.**
> **→ "등록 → 등급 부여 → 상한 규정 → 환경 변경 시 재심사"라는 완결 루프.** 저자의 등록 스키마·재심사 논지와 정확히 맞물리며, **조정 1(폐기)의 학술 반례**이기도 하다.

### 9-3-2. ★★ AAL / ACL 이원 체계 — **이 책 등급 장치의 뼈대 후보**

**Zheng, Dong, Depena, Bhatia, Xiao & Xu (ExxonMobil Technology and Engineering), 「Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels」, arXiv:2607.23438v1, 2026-07-26** `[PP]`

핵심: 자율성 논의는 **"기술적으로 할 수 있는 것"과 "실무에서 해도 되는 것"을 습관적으로 뒤섞는다.** 두 축으로 완전히 분리한다.

- **AAL (Allowed Autonomy Level)** — "what an agentic system **is authorized to do** in deployment, rather than what it is technically capable of doing." **조직이 감수할 의사가 있는 책임의 수준.**
- **ACL (Autonomous Capability Level)** — "the **inherent technical capabilities** of an agent, independent of whether those capabilities are exercised."

**AAL 5단계 (원문 Table 1) — 라벨이 한국어로 옮겨도 살아 있다:**

| AAL | Human Role | Human Task | Scope | **Accountability Implication (verbatim)** |
|---|---|---|---|---|
| **A1** | **Hands on** | Execute | Local-task | "Errors are bounded to a single invocation and corrected directly by the human who initiated the action." |
| **A2** | **Instructions on** | Instruct | Decision-support | "The agent provides advice, which can indirectly degrade human decisions." |
| **A3** | **Eyes on** | Supervise | Workflow | "Agents now act; failures become **actions rather than advice**, though supervision and reversibility still limit harm." |
| **A4** | **Mind on** | Set goals and constraints | System | "Humans no longer supervise steps; failures stem from **design errors** rather than execution mistakes." |
| **A5** | **Mind off** | Set policies | Organizational | "Decision-making authority is delegated; failures reflect **accountability and governance gaps**, not task errors." |

**ACL 5단계:** C1 Model/Tool → C2 Helper/Advisor → **C3 Junior Operator** → **C4 Sr. Operator** → **C5 Plant Manager/Decision Maker**

**등급 간에 바뀌는 것 (저자 명시 3축):**
> "As autonomy increases, **human control becomes less direct, reversibility decreases, and the consequences of failures become more difficult to contain**."
> A3→A4→A5는 **"successive transfers of control from runtime supervision to upfront governance and, ultimately, to delegated authority"**
> **→ 통제가 사라지는 게 아니라, 통제가 놓이는 시점이 실행 중 → 설계 시점 → 정책 시점으로 앞당겨진다.**

**★ 실증 사례 2건 — 이 책이 가장 필요로 하는 종류의 증거 (의도적 하향 배치):**
- 데이터 엔지니어링 다중 에이전트: 기술적으로 **C4**이나 **A3로 의도적 하향**. 이유: "ungoverned backfill jobs can corrupt downstream pipelines."
- 에너지 운영 코파일럿: 연 **약 20,000건**의 비정형 현장 보고서 검토. 기술적으로 **C3**이나 **A2(자문 전용)로 배치**. 운영 원칙: **"AI reasons, guardrails verify, human decides."** 이유: 물리 도메인 행위는 대체로 비가역.
- 저자 정식화: **"The gap between C4 and A2 or A3 is not a deficiency; it is a `deliberate governance choice`."**

**인용 가능한 문장:**
- **"An agent should not operate at an AAL higher than the human organization is prepared to accept."**
- **"Importantly, higher capability does not automatically imply higher allowed autonomy."**
- "We expect most real-world Agentic AI applications to operate at **A1 through A3**. Levels A4 and A5 require significantly stronger justification."
- 등급 수 설계 원칙: **"the number of autonomy levels should be limited, their meanings clearly articulated, and their progression clear."** (5단계를 택한 이유: rigor·stability·usability의 균형)
- 안정성 논거: "Autonomy levels that depend on specific model capabilities, benchmarks, or architectural details **risk becoming obsolete or misleading**."

**한계:** **프리프린트(동료심사 없음), 10페이지 산업 실무 보고**, **단일 기업 사례 2건**, 에너지·중공업 편향(비가역성이 지배적인 물리 도메인 직관이 소프트웨어에 그대로 이식되지 않을 수 있음). ACL 판정 기준이 정성적(C3/C4 경계는 판정자 재량).

> **이 책에서의 쓰임새:** 한국 기업의 AX 논의가 거의 항상 **"우리 모델이 뭘 할 수 있나"(=ACL)에서 끝나고 "우리 조직이 뭘 허용할 것인가"(=AAL)로 넘어가지 않는다**는 지적을 이 논문으로 정면 뒷받침할 수 있다. 그리고 **가역성(reversibility)을 등급 판정의 1급 변수**로 삼는 발상 — 코드 커밋 vs 화학 공정 제어 명령의 대조는 그대로 예화가 된다.

### 9-3-3. 학술 계보 — 1978년에 이미 있었다

| 문헌 | 기여 | 서지 |
|---|---|---|
| **Sheridan & Verplank (1978)** | **10단계 자동화 수준의 원전** | MIT Man-Machine Systems Lab 기술보고서. ⚠️ **원 보고서(DTIC ADA057655) 미확보** — 표는 재수록본 경유, "1978 vs 1987" 연도 귀속이 자료마다 갈림 |
| **★ Parasuraman, Sheridan & Wickens (2000)** | **네 단계 정보처리 × 등급** | *IEEE Trans. SMC-A* **30(3), 286–297**. DOI 10.1109/3468.844354. 피인용 **4,253회** `[PR]` |
| **Parasuraman & Riley (1997)** | use / misuse / disuse / abuse | *Human Factors* 39(2), 230–253. ⚠️ 원문 미확보 — 정의는 통상적 정리 |
| **★★ Bainbridge (1983)** | **자동화의 아이러니** | 9개 인용문 확보 |
| **★ Endsley (2017)** | **automation conundrum** | — |
| Endsley & Kaber (1999) | 10단계 × 4기능 배분표 + 실험 | — |
| Beer, Fisk & Rogers (2014) | HRI 자율성 등급 — 계보의 중간 고리 | *J. Human-Robot Interaction* 3(2). DOI 10.5898/JHRI.3.2.Beer. 피인용 613회 `[PR]` |

**★ Parasuraman et al. (2000) — 이 책에 가장 직접 이식되는 문헌** (초록 VERBATIM):
> "**automation does not merely supplant but changes human activity and can impose new coordination demands on the human operator.** We propose that **automation can be applied to four broad classes of functions: 1) information acquisition; 2) information analysis; 3) decision and action selection; and 4) action implementation. Within each of these types, automation can be applied across a continuum of levels... A particular system can involve automation of all four types at different levels.**"

| # | 원문 | AX 대응 |
|---|---|---|
| 1 | **Information acquisition** | 무엇을 수집·감지·조회하는가 |
| 2 | **Information analysis** | 수집된 것을 어떻게 통합·해석·예측하는가 |
| 3 | **Decision and action selection** | 어떤 조치를 택할 것인가 |
| 4 | **Action implementation** | 그 조치를 실제로 집행하는가 |

> **세 가지 실무 처방이 여기서 바로 나온다:**
> 1. **"자율도 3단계"라는 단일 값을 쓰지 마라.** SAE는 기능 하나에 단일 등급을 붙이지만, Parasuraman 모형은 **네 기능에 독립적으로** 배분한다. → AX 등급표를 최소 **(관찰·분석·의사결정·실행) 4칸**으로 쪼개라.
> 2. **이 틀로 "중간 등급"을 해부하면 기이함이 드러난다.** SAE L3는 앞의 세 단계를 모두 높게 자동화해놓고 **"실패했을 때의 결정과 실행"만 인간에게 남긴다** — 인간이 앞의 세 단계에 전혀 참여하지 않은 상태에서 네 번째만 맡는 구조다.
> 3. **"자동화는 대체가 아니라 변형"** — AX 효과를 "사람이 하던 일의 뺄셈"으로 계산하면 **새로 생기는 조율 비용**이 회계에서 통째로 빠진다. (축 5와 직결)

**한계:** 이론·프레임워크 논문이며 **원저 실증 데이터가 없다.** "Parasuraman이 실험으로 증명했다"고 쓰면 오류. 2000년 논문이라 ML 기반 자율성(불투명·확률적)은 다루지 않는다.

**★ 계보 단절 — 이 책이 메울 빈칸 (직접 확인):**
> arXiv API에서 `Sheridan` + `levels of automation` + `large language model`을 **모두 포함하는 논문은 0건**이었다. 고전 계보를 명시적으로 잇는 LLM 에이전트 논문은 **2건뿐**이다 (Zheng et al. 2026 → Sheridan 직접 인용 / Engin & Hand 2026 → Parasuraman 직접 인용). **GAL·Data Agents 등은 SAE만 인용하고 Sheridan은 인용하지 않는다.**
> **→ "1978년에 이미 정리된 자동화 등급 이론이 있는데, 2020년대 AI 에이전트 논의는 그 유산을 거의 참조하지 않고 자율주행 등급만 베끼고 있다. 그런데 자율주행 등급은 1차원이고, 1978~2000년 계보는 2차원이다."** 이 단절을 지적하고 다리를 놓는 것이 **이 책의 실질적 학술 기여**가 될 수 있다.

### 9-3-4. ★ 중간 등급이 가장 위험하다 — 자율주행 실증 사슬

> **A절의 결론:** 서로 다른 연구팀이 서로 다른 방법(테스트트랙 실험·129편 메타분석·시뮬레이터·전문가 인터뷰·결함조사·사고조사)으로 **"중간 등급을 안전하게 만드는 조건"을 각자 도출했더니, 그 조건들이 하나같이 중간 등급의 편익을 상쇄하거나 소멸시킨다**는 데로 수렴했다.
> **→ 중간 등급이 나쁘다는 것이 아니라, 중간 등급을 안전하게 만들면 그것은 더 이상 중간 등급이 아니다.**

확보된 실증: SAE J3016 정본 서지·L0~L5 정의·공식 시각 분할표(L0-2 / L3-5, **홀로 남는 L3**) / **Eriksson & Stanton (2017)** 인계 시간 실측과 **13배의 분산** / **Zhang et al. (2019)** 129편 메타분석 / **Merat et al. (2014)** "제어 회복까지 35–40초" / **Victor et al. (2018)** 테스트트랙 106명 / **Gerber, Schroeter & Ho (2023)** L3의 자기소멸을 학계가 정식 진술 / **NTSB 2건 + NHTSA 2백만 대 조사**

**바로 쓸 수 있는 5문장 (전부 verbatim 확인 완료):**
1. **Bainbridge (1983):** "the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate."
2. **Bainbridge (1983):** "it is humanly impossible to carry out the basic function of monitoring for unlikely abnormalities"
3. **Endsley (2017):** "**as more autonomy is added to a system, and its reliability and robustness increase, the lower the situation awareness of human operators and the less likely that they will be able to take over manual control when needed.**"
4. **Victor et al. (2018):** "neither these reminders nor explicit instructions on system limitations and supervision responsibilities prevented **28% (21/76) of drivers from crashing with their eyes on the conflict object**"
5. **NHTSA EA22-002 (2024):** "This mismatch resulted in a **critical safety gap** between drivers' expectations of the L2 system's operating capabilities and the system's true capabilities. This gap led to **foreseeable misuse and avoidable crashes.**"

> **★ 이것은 1차에서 확보한 Skitka(1999) 자동화 편향("거의 항상 맞는 시스템이 가장 위험")과 완전히 다른 경로로 같은 결론에 도달한다.** 두 계보를 나란히 놓으면 이 책에서 가장 강한 논증 중 하나가 된다.

### 9-3-5. 현장의 반론 — 등급 설계 전에 반드시 받아야 할 것

**(가) 승인 기반 등급은 통제의 외양일 뿐이다** 【이 책 설계에 가장 위험한 발견】
> **"Theoretically that works, but we've found the approach to be fallible. Our telemetry showed users approved roughly `93%` of permission prompts. The more approvals a user sees, the less attention they pay to each, becoming over time much less diligent in their supervision."**
> — Anthropic 엔지니어링 포스트, `ericmcer`가 인용, HN 2026-06-04 ⚠️ **벤더 1차 자료의 2차 인용 — 원문 직접 확인 필요**

짝: **"Anything based on asking users to approve/deny is a catastrophe waiting to happen."** — `emk`, Lobsters, 2026-07-20

> **→ 이 책이 자율성 등급을 승인 축으로 설계하려 한다면, 이 숫자가 그 설계를 시작 전에 재고하게 만든다.** 답의 방향: **등급의 축을 승인이 아니라 능력(capability)과 환경으로 잡아라** — AAL/ACL이 정확히 그 형태다. 승인은 **고위험 행위 소수**에만 남기고 나머지는 **닿을 수 없게 만든다.**

**(나) 현장은 2단계로 쓴다**
실제 채택 등급 수가 **2**인 사례가 복수다(신뢰/테스트 모드 vs 프로덕션, 업무용 제안 전용 vs 실험용 풀권한). **다단계를 제안하려면 왜 2단계로 부족한지를 근거로 세워야 한다.** 등급 수를 늘리는 것 자체가 승인 피로를 재생산할 수 있다.

**(다) 보안은 환경에 속한다**
> **"A simpler approach is just to give the agent it's own user account and let the OS treat it like an `untrusted undergrad` on a shared Unix host, like back in the old days. ... The point is, `security belongs in the environment. Not the harness!`"**
> — `emk`, Lobsters, 2026-07-20
> **→ 이 책의 "사번" 은유가 커뮤니티에 이미 존재한다 — 다만 "직원"이 아니라 "신뢰할 수 없는 학부생"이라는 이름으로.** 이 대비 자체가 챕터를 연다.

---

## 9-4. 축 1 보강 — 폐기·재심사와 등록 스키마

### 9-4-1. 폐기 반례 4종 (§9-0 조정 1의 근거)

**① Microsoft Entra ID Governance** — 가장 완성된 설계 (공식 문서 ★, ms.date 2026-06-05 / 갱신 2026-06-24)
> 목적 진술: "you can govern and manage the identity and access lifecycle of agents, ensuring the agents have a **responsible person providing oversight throughout the agent lifecycle** and **agent's access does not persist longer than it is needed**."

문서화된 메커니즘 4가지:
1. **Sponsor 제도** — "Sponsors of agent identities are **human users accountable for making decisions about its lifecycle and access**."
2. **접근 자동 만료** — access package에 만료일. 임박 시 sponsor에게 알림 → 연장 요청 시 **새 승인 사이클** 트리거, 무대응 시 **"the access package assignment automatically expires... and the agent identity loses access to the target resources."**
3. **★ 후원자 이탈 시 자동 승계** — **"If the sponsor is leaving the organization, sponsorship of the agent identities is automatically transferred to their manager. With sponsorship transferred, `there's always a human user accountable` for managing the access and lifecycle of the agent identities."**
4. **활성화/비활성화** — Sponsor·Owner가 포털에서 enable/disable

> **책에서의 값어치: "사람이 퇴사하면 그가 후원하던 에이전트의 책임이 그의 매니저에게 자동으로 넘어간다."** 고아 계정 문제에 대한 구체적 제도 설계. → 저자의 등록 스키마에 **"책임자 + 책임자 승계 규칙"** 항목이 있어야 한다는 근거.

**② Saviynt 6단계 라이프사이클** (벤더 프레임, 2026-02-26) — Registration → Ownership → Entitlement → Lifecycle Governance → **Retirement** → IGA 통합

**Retirement가 요구하는 7항목 — 이 책의 "폐기 체크리스트"로 그대로 사용 가능:**
① 승인 포함 **공식 폐기 워크플로** ② **즉시 자격증명·토큰 폐기**(API 키·인증서·OAuth) ③ **아웃바운드 접근 제거**(연동·도구 권한) ④ **인바운드 호출 차단**(엔드포인트·웹훅·큐) ⑤ **메모리·데이터 정화**(보관/익명화/안전 삭제) ⑥ **감사 추적 보존**(불변 로깅) ⑦ **폐기 후 잔여 리스크 모니터링**

재심사 규정: **"event-driven, continuous re-certification (not quarterly)"** — 분기 재인증이 아니라 **이벤트 기반 연속 재인증**. 엔타이틀먼트 크립 탐지, 접근 패턴 드리프트 알림, **에이전트가 새 역량을 얻으면 소유자 재확인(re-attestation)**

**③ 규제·정부 스키마에 이미 폐기 상태가 있다** — EU Annex VIII `recalled` / 미 연방 인벤토리 `development_stage = Retired`

**④ 자율성 인증서의 갱신 요건** (Feng et al., §9-3-1 다)

**용어 (좋은 어휘):** "A decommissioned agent has had its **new work frozen and queues drained**, its traffic redirected, its credentials revoked, its identity **`tombstoned in a governance record`**, its records retained per policy, and the whole sequence verified."
> **"tombstoned"** — 삭제가 아니라 **묘비 처리**.

**⚠️ 사용 금지:** "Only 20% of organisations have formal processes for offboarding and revoking API keys" — 조사 주체·표본·연도 전부 미상.

### 9-4-2. 등록 스키마 — 저자의 8항목과 대조할 공개 목록

**① EU AI Act Annex VIII (규제 원문 ★)**

**Section A — 제공자, Art.49(1), 13항목:** ①제공자 이름·주소·연락처 ②대리 제출자 ③공인 대리인 ④**상품명 및 식별 참조번호** ⑤**의도된 목적·맥락·사용 조건** ⑥**입력값 및 작동 로직** ⑦**시스템 상태**(시장 출시/서비스 중/더 이상 제공 안 됨/**리콜됨**) ⑧인증서 유형·번호·만료일 ⑨인증서 스캔본 ⑩출시 회원국 목록 ⑪EU 적합성 선언서 ⑫전자 사용설명서 ⑬추가 정보 URL

**Section B — 고위험 아님으로 자체 판단한 경우:** ①~⑤ 동일 + ⑥ **Art.6(3)에 근거해 고위험이 아니라고 판단한 조건(들)** + ⑧ 시스템 상태

**Section C — 배포자(deployer), Art.49(3), 5항목:** ①배포자 이름·주소·연락처 ②대리 제출자 ③**제공자가 등록한 EU DB 항목의 URL** ④**기본권 영향평가 결과 요약** ⑤DPIA 요약

> **두 가지 관찰:** ⓐ **Section A-7에 `recalled`가 있다** — 규제가 이미 폐기 상태를 스키마에 넣어놨다. ⓑ **Section C(배포자)가 별도로 존재한다** — 만든 자와 쓰는 자의 등록 의무가 분리돼 있다.

**② 미 연방 AI use case inventory — 36개 필드 전체** (정부 원자료 ★, 56기관 3,611건, 고영향 445건, 배포/파일럿 1,818건)

핵심 필드: `id`(= `[기관약칭]–[#]`) / `contact_email`(**책임 개인 또는 팀**) / **`development_stage`**(Pre-deployment / Pilot / Deployed / **Retired**) / `is_high_impact` / `HI_justification`(**고영향 "아님" 판정의 근거**) / **`classification`**(6종 — **`Agentic`** / Classical ML / Computer Vision / Generative AI / NLP / RL) / `system_outputs` / `operational_date` / `contracting_usage` / `vendor_name` / **`have_ato`**(운영 인가 보유 여부) / `has_pii` / `pia_url` / `demographic_features` / `has_custom_code` / `code_url`

**고영향에만 붙는 9개 필드(28~36):** `hi_testing_conducted` / `hi_assessment_completed` / `hi_potential_impacts` / `hi_independent_review` / **`hi_ongoing_monitoring`** / **`hi_training_established`**(운영자 교육) / **`hi_failsafe_presence`**(페일세이프) / **`hi_appeal_process`**(결과에 이의 제기 절차) / `hi_public_consultation`

> **★ 결정적 관찰: 9개 필드가 고영향에만 붙는다 — 위험 등급에 따라 요구 항목이 달라진다. Gartner가 2026년에 "비례적 거버넌스"라 부른 것이 미국 정부 등록 스키마에는 이미 구현돼 있다.** 그리고 **`classification`에 `Agentic`이 별도로 존재한다** — 정부가 에이전트를 따로 세고 있다.

**③ 벤더 레지스트리 필드**

| 제품 | 요구 필드 |
|---|---|
| **ServiceNow AI Control Tower** | provider, vendor, **lifecycle phase**, state, **risk classification** + 자산 유형(systems/models/prompts/datasets/**MCP servers**) |
| **Workday ASoR** | 이름, 설명, **접근 권한 보유 보안 그룹**, 국가별 가용 지역, **상태(status)**, 비용·ROI |
| **Entra Agent ID** | blueprint / blueprint principal / agent identity / agent user + **Owner·Sponsor·Manager** + access package 만료일 |
| **Saviynt(제안)** | 암호학적 고유 ID, **생성 증명(attestation)**, model version, hosting environment, owner, purpose, 베이스라인 최소권한 정책 |

⚠️ **미확보:** Model Card / System Card 표준 섹션 목록, ISO/IEC 42001 인벤토리 요구 항목(유료 표준)

---

## 9-5. 【신규 축 5】 등록된 에이전트의 성과관리·FTE·생산성

> **⚠️ 이 축은 홍보성 수치가 범람한다.** 모든 수치에 출처 성격 라벨을 붙였다: `[보도자료]` `[벤더 백서]` `[동료평가 논문]` `[정부·중앙은행]` `[컨설팅 조사]` `[매체 보도]` `[커뮤니티]`. **라벨 없는 수치는 이 문서에 넣지 않았다.**

### 9-5-1. FTE 환산의 계보 — RPA가 먼저 했고, 먼저 실패했다

**표준 계산식 (업계 관행)** `[벤더 백서]`:
> `FTE = 봇 월 처리 건수 / 사람 월 처리 건수` 또는 `FTE = (건당 사람 소요시간 × 봇 처리 건수) / 사람의 월 정규 근로시간`
> 채택 문턱: "한 프로세스를 자동화해서 **최소 2 FTE는 확보돼야** 할 만하다"

**★ 업계 자기모순 — 이 책 축 5의 경고 문장:**
> **"보수적 계산에서는 `라이선스 1개 = 3 FTE`로 가정하기도 한다. 그러나 실무에서는 `1:1을 넘기는 것조차 어렵다` — 로봇은 대체로 정규 업무시간에만 돌고, 시스템 지연과 애플리케이션 응답시간 때문에 사람보다 빠르지도 않기 때문이다."**
> **"1 라이선스 = 3 FTE"라는 영업 숫자와 "실무에선 1:1도 어렵다"는 현장 숫자가 같은 업계 안에 공존한다.**

**비판받은 지점 5가지 — "이번엔 다르다"를 증명하려면 반드시 넘어야 할 것:**

| # | 비판 | 근거 |
|---|---|---|
| ① | **벤더 비즈니스 케이스의 과장** — "12개월 미만 회수, 3년 ROI 500%"를 제시하나, 조직은 **적합 프로세스 개수를 과대평가**하고 **룰 정교화 작업량을 과소평가**한다. 결과: **"비용 절감이라는 핵심 마일스톤이 결코 실현되지 않고 정치적 지지가 증발한다."** | `[벤더 백서]` |
| ② | **★ 시간 절감 케이스의 근본 결함 【최고 인용문】** | `[커뮤니티]` |
| ③ | **이중 계상** — "사무 인력이 제거되지 않고 **재배치**되었다면, 재배치 가치는 **정원 절감과 별도로** 계상해야 한다." | `[벤더 백서]` |
| ④ | **계산식 자체가 비표준** — "**모두가 자기만의 FTE 편익 계산식을 쓴다** — 생산 가능 시간은 하루 **5.5시간에서 8시간** 사이 어디든이고, 연간 생산일수는 **200일에서 255일** 사이 어디든이다." → **같은 자동화가 계산식에 따라 편익이 40% 이상 차이 난다** | `[벤더 백서]` |
| ⑤ | 실패율 "RPA 도입 30~50% 실패 — EY 2016" | `[컨설팅 조사]` ⚠️ **EY 원 리포트 미대조** |

**★ ② 최고 인용문 (원문 그대로):**
> **"There is unlikely a single automation program in the world that has delivered to an 'Hours saved' business case, and this is simply due to the lack of consideration of Human Capital Change — `10,000 hours sounds great until you realize it is 30 minutes from each of your 20,000 employees.`"**
> — William Harris, LinkedIn `[커뮤니티]` (실무자 서명 글, 데이터 아님)
> **→ "AI로 연 10,000시간 절감"이라는 보고서를 받았을 때 던져야 할 질문이 이 한 문장에 있다.**

**현행 "agentic workforce planning" 제안** `[커뮤니티]` ⚠️ **실증이 아니라 컨설턴트·블로거의 제안 — 개념만 쓰고 수치는 인용 금지:**
- **인력계획이 두 개의 산출물로 쪼개진다:** "사람 정원 계획(human headcount plan)"과 "AI 캐파 계획(AI capacity plan)"
- 재무 권고: "소프트웨어 라이선스와 **분리된 별도의 `agent labor` OpEx 계정**을 만들라"
- 인사 권고: "**workflow deprecation protocol**을 만들라 — 이전에 FTE에게 할당됐던 태스크가 계획 주기 안에서 공식적으로 **ALU(agentic labor unit)로 이관되는 절차**"

### 9-5-2. 회계·공시 — 선언은 공개되고 검증은 공개되지 않는다

**★ Klarna — 이 분야의 정본 계보 (선언 → 검증 → 번복)**

**① 2024-02-27 원 발표** `[보도자료]` ★ (회사 공식, 원문 확보)
- 첫 달 **2.3백만 건** 처리 = 전체 고객서비스 채팅의 **3분의 2**
- > "doing the **`equivalent work of 700 full-time agents`**"
- 고객 만족도 사람 상담원과 **동등(on par)**, 반복 문의 **25% 감소**, 처리 시간 **11분 → 2분 미만**, 23개 시장·35개 이상 언어
- > "**estimated** to drive a **$40 million USD in profit improvement** to Klarna in 2024"

> **⚠️ 정확히 읽을 것: 보도자료는 "700명을 대체했다"가 아니라 "700 full-time agents의 일에 상당하는 양(equivalent work)"이라고 썼다. 환산이지 대체가 아니다.** 이 문장이 언론에서 "700명 해고"로 번역되는 과정 자체가 축 5의 소재다.

**② 2025-05 번복** `[매체 보도]` (Bloomberg 인터뷰, 복수 매체 교차 / ⚠️ 원문 미접근)
- CEO Sebastian Siemiatkowski: AI 챗봇이 사람보다 싸긴 했지만 **"lower quality"** 를 낳았다. 고객이 원하면 **항상 사람과 대화할 수 있도록** 사람을 다시 채용 중.
- 현재 구조: AI가 1선 대부분 처리 + **프리미엄·복잡 케이스에 사람 재투입**한 하이브리드

**③ ⚠️ 검증 불가 지점 — 그리고 그것이 곧 발견:**
> **$40M 이익 개선이 실제로 실현됐는지에 대한 사후 공시·검증 자료를 찾지 못했다.** 원 발표는 "estimated"였고 실현 여부는 공개되지 않았다.
> **→ 이것 자체가 축 5의 논지다: 선언은 공개되고 검증은 공개되지 않는다.**

**★ 커뮤니티의 해부 — FTE 챕터 오프닝 최유력:**
> **"So they simultaneously claim that they've got AI that has replaced 700 people, but that they haven't actually fired 700 people, but if you're listening `Wall Street` we're are firing them, but if you're listening `EU regulators and main street` no no we're definitely not."**
> — `SilverBirch`, HN, **2024-02-29** `[커뮤니티]`
> **→ "AI로 N명분"이라는 문장이 하나의 사실 주장이 아니라 청중별로 다른 세 개의 진술임을 폭로한다.** 이 책이 FTE 환산표를 내밀 때 독자가 던질 첫 질문("이 표는 누구에게 보여주는 표인가")을 미리 세운다.
> 짝(한국, 검증 가능한 반문): **"그러면 ai를 사용하는 사람수만큼 사람수를 줄여야 하는데 그렇게 되고 있나요?"** — `k35241`, OKKY, 2026-08-16

**★ Salesforce — 같은 사실, 두 개의 문장** `[매체 보도]` 2025-09-02
- **CEO Marc Benioff (팟캐스트):** "**I was able to rebalance my headcount on my support**" / "**I've reduced it from 9,000 heads to about 5,000, because `I need less heads`.**" (AI 에이전트가 고객 상호작용 **약 50%** 처리)
- **회사 공식 성명 (프레이밍이 다르다):** "we've seen the number of support cases we handle **decline** and we **`no longer need to actively backfill` support engineer roles**." — 해고가 아니라 **결원 미충원 + 재배치**. 수백 명을 professional services·sales·customer success로 재배치했다고 밝힘.
- 다른 수치: Agentforce로 지원 비용 **$100M 절감**, **300만 건** 대화 처리 `[벤더 백서/경영진 발언]`

> **→ 같은 사실에 대해 CEO는 "heads를 줄였다"고 하고 회사 성명은 "백필을 안 한다"고 한다.** "정원 감축을 AI 성과로 보고할 때의 함정"이 **한 회사 안에서 두 개의 문장으로 존재한다.**

**회계 분류 문제** `[벤더 블로그]`/`[컨설팅 조사]`:
> AI 토큰 지출은 **어느 회계 항목에도 깔끔히 들어맞지 않은 채 여러 버킷을 넘나든다** — 클라우드처럼 소비 기반이지만 사람의 클릭이 아니라 **자율적 의사결정**이 유발하고, SaaS처럼 운영에 통합돼 있지만 다르게 스케일하며, **일부 인건비를 대체하지만 정원 감축에 1:1로 매핑되지 않는다.**
> 권고: 제품 경험의 일부면 **COGS/DevOps 안의 별도 inference 계정**으로 / **명시적 인력 대체·회피** AI면 **수혜 기능 안의 별도 서브계정**에 추적
> **→ "AI가 사람 일을 했는데, 그 비용은 인건비 줄에 안 잡힌다."** 인건비는 줄고 OpEx는 늘지만 **어느 줄에서 늘었는지 아무도 합의하지 못했다.** (1차의 닛케이 2026-07-09 표제와 같은 문제 — 본문은 2차에서도 유료로 미접근)

### 9-5-3. ★ 측정 신뢰도 등급 — 학술 근거 확보

> 이 책은 "실측 / 표본 / 자기보고"로 **신뢰도 등급을 나눠 차등 인정**하는 설계를 제안한다. **그 설계가 문헌으로 방어된다.**

| 등급 | 문헌이 지지하는 설계 규칙 | 근거 |
|---|---|---|
| **실측 (최상)** | 시스템 로그·출입기록 등 객관 기록 | **Chase & Godbey**(클럽 출입기록 대조): **자기보고가 객관 로그 대비 100% 이상 과대** |
| **표본 (중간)** | 시간일지·직접 관찰 등 표본 기반 실측 | Robinson 계열 전체가 "일지 = 기준선"으로 설계 |
| **자기보고 (최하)** | **수준은 못 믿고 순위는 쓸 수 있다** | Buehler: 편향에도 **실제와 r = .77** |
| **자기보고 가산 조건** | ① "지난주" 앵커 + 후속 질문 ② **실측 대조 예고** ③ 실행 당사자가 아닌 **제3자 추정** ④ 원인·결과를 **다른 출처**에서 | Frazis & Stewart / Mabe & West / Jørgensen / Podsakoff |
| **자기보고 감산 조건** | ① "통상적으로 얼마나?" 형태 ② 원인·결과를 **같은 설문지**로 (**Podsakoff: 133~304% 팽창**) ③ **KPI·보상에 연동** | Frazis & Stewart / Podsakoff / Ordóñez |

**핵심 문헌:** Robinson & Bostrom (1994) 자기추정 노동시간 vs 시간일지 / Robinson et al. (2011) 최신 재검증 / **★ Frazis & Stewart (2014) 반박 문헌 — 균형을 위해 필수** / Buehler, Griffin & Ross (1994) 계획 오류의 정본 / **Jørgensen (2004) 소프트웨어 공수 추정 편향** / **★★ Podsakoff et al. (2003 정본 / 2012 수치) 공통방법편향** / Mabe & West (1982) — **"신뢰도는 설계 가능하다"**

> **1차의 METR(예측 −24% / 실측 +19% / 사후 −20%)이 이 등급제의 실증적 정당화이고, 위 문헌들이 그 이론적 뒷받침이다.** 두 겹을 함께 쓰면 카드 8의 설계가 방어된다.

### 9-5-4. ★ 측정 왜곡 — Goodhart 계보 정정과 네 변종

**⚠️ 저술 시 필수 정정 — 흔한 오귀속:**

| | 진술 | 실제 출처 |
|---|---|---|
| **원전** | "**Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.**" | **Goodhart (1975)**, "Problems of Monetary Management: The U.K. Experience", in *Papers in Monetary Economics* Vol. I, Reserve Bank of Australia, pp. 1–20 |
| **대중화 진술** | "**When a measure becomes a target, it ceases to be a good measure.**" | **Strathern (1997)**, "'Improving ratings': audit in the British University system", *European Review* **5(3), 305–321**, p. 308 `[PR]` |

> **널리 인용되는 "When a measure becomes a target…"은 Goodhart가 한 말이 아니다. Goodhart 1975로 귀속시키면 사실 오류다.**
> ⚠️ 판본 차이: Bevan & Hood는 "on it", Manheim & Garrabrant는 "upon it"으로 적었다.
> **★ 메타 발견:** 원문에서 Strathern은 이를 **자기 정식화로 제시하지 않고 Keith Hoskin의 명명을 인용하는 맥락에서** 던진다. **"인용의 인용을 쫓다 보면 원전이 흐려진다"는 이 책의 논지에 딱 맞는 메타 사례이며, 이 책의 규율(원전 확보)이 왜 필요한지의 실례다.**

**★ Strathern 초록 — AX 측정 챕터의 경구로 최적 (VERBATIM):**
> "This paper gives an anthropological comment on what has been called the '**audit explosion**'... **While the metaphor of financial auditing points to the important values of accountability, `audit does more than monitor—it has a life of its own that jeopardizes the life it audits`.**"
> (**감사는 감시 이상의 일을 한다 — 감사는 자기 자신의 생명을 가지며, 그것이 감사하는 대상의 생명을 위태롭게 한다.**)

**★★ Manheim & Garrabrant (2018) 「Categorizing Variants of Goodhart's Law」 arXiv:1803.04585** `[PP]` (전문 확인)
> 정의: "**a Goodhart effect is when optimization causes a collapse of the statistical relationship between a goal which the optimizer intends and the proxy used for that goal.**"
> **네 변종**이 AX 지표 설계에 그대로 이식된다.
> ⚠️ **프리프린트, 동료심사 게재 없음.** 근원은 Garrabrant의 LessWrong 글(2017-12-30).

**계보 전체:** Ridgway (1956) 성과측정 역기능의 최초 지적 / Campbell (1979) 캠벨의 법칙 / **★ Smith (1995) 성과데이터 공개의 8가지 역기능** / **★★ Bevan & Hood (2006) 게이밍의 실증** (전문 확인) / Ordóñez et al. (2009) 「Goals Gone Wild」

**★ 현장 실증 — Goodhart가 픽셀로 내려온다** `[커뮤니티]`:
> **"At Cerebras I know of several people who burn tokens on completely `USELESS tasks (randomly changing pixels in an image)` just to keep them high up on the token leaderboard. ... They made the metric `token usage` (which is just a proxy for LOC) so that's what they're gonna get."**
> — `joshuastuden`, HN, **2026-05-01** ⚠️ 익명 주장 — 미검증
> **같은 달(2026-05) 한국 GeekNews에도 "Amazon 직원들이 AI 토큰 소비량을 부풀린다"는 토픽이 섰다.** 두 대륙, 같은 달, 같은 행동.
> 짝(한국): **"예전에는 개발자들의 개발실력 지표를 코드 몇줄 썼냐 그걸로 지표 설정했었으니까 ㅋㅋㅋ"** — `happing94`, GeekNews, 2026-05-18

### 9-5-5. ★★ 성과 귀속 — 이 책에 쓸 설계 명제 5개

> **1차에서 "사람+에이전트 팀의 성과 귀속은 개념만 있고 실증 없음"으로 기록했다. 2차에서 정면으로 확보했다.**

| # | 명제 | 근거 |
|---|---|---|
| 1 | **팀 성과를 `인간 단독`과 비교하지 말고 `AI 단독`과 비교하라.** 대부분의 AX 보고서는 전자를 재고 후자를 주장한다. | **Vaccaro, Almaatouq & Malone (2024)** — 인간 단독 대비 **g = 0.64**, **AI 단독 대비 g = −0.23** |
| 2 | **AI가 인간보다 나은 과업에 인간 승인 단계를 두지 마라.** 평균 **g = −0.54**의 손실. | Vaccaro et al. |
| 3 | 인간을 넣으려면 **AI가 접근 못 하는 정보를 그 인간이 쥐고 있어야** 한다. 아니면 **d = 0.16, p = 1.0**. | **Hemmer et al.** 실험 1 `[PP]` ⚠️ 게재 여부 미확인 |
| 4 | **설명(XAI)은 적정 신뢰를 만들지 않는다. 오답 수용률을 높인다.** 신뢰도 표시 이상의 효과가 없다. | **Bansal et al. (2021)**(1차의 A17 서지 미확정 → **2차에서 확인 완료**), Vaccaro et al., Schemmer et al. |
| 5 | **과업 수준 이득을 조직 성과로 곱하지 마라.** 관측된 **감쇠율 약 1/6**, 병목은 조율이 필요한 인간 공정에 있다. | Demirer et al., Dillon et al. |

> **★ 세 주제를 꿰는 한 문장:** 팀 성과를 **인간 단독**과 비교하면 **+0.64**, **AI 단독**과 비교하면 **−0.23**이다.
> **→ AX 체계 구축의 첫 번째 설계 결정은 기술 선택이 아니라 `기준선 선택`이다.**

관련: Steyvers et al. (2022) **상보성이 성립하는 구간은 좁다** / Steyvers & Kumar (2024) 세 가지 난제
⚠️ **수치 인용 제한:** Bansal 그림 4B·5, Steyvers PNAS 표 1·2의 정확한 수치는 추출 실패 — **방향성만 인용 가능.**

### 9-5-6. 절감 인력의 처리 — 【이 책의 가장 민감한 대목】

**★ 학술 반증 — "98% 자동화했는데 일자리가 늘었다"** (Bessen, 저자 본인 문장 VERBATIM):
> ATM: "**the number of tellers required to operate a branch office in the average urban market fell from `20 to 13` between 1988 and 2004**" / "**Bank branches in urban areas increased `43 percent`**" / "**the number of bank teller jobs `did not decrease` as the ATMs were rolled out**"
> **19세기 방직 (ATM보다 더 강한 사례):** "**power looms automated `98 percent` of the labor needed to weave a yard of cloth**" / "**the number of factory weaving jobs `increased` over this period**" / "**weavers' wages `rose sharply`**"

> **→ "98% 자동화 → 일자리 증가"는 AX 담론의 "80% 자동화하면 인력이 80% 남는다"는 직관을 깬다.** 저자 본인 문장이라 인용 안전성이 높다.
> ⚠️ **수치 혼용 금지:** Bessen 본인 기사와 Autor(2015)판의 수치가 미묘하게 다르다. 창구직원 총수(50만→55만, 1980–2010)는 **Autor 논문에만** 등장 — "Autor(2015)가 Bessen(2015)을 인용해 제시한 수치"로 표기해야 정확하다.

**⚠️ 서지 정정 2건 (2차에서 발견):**
- Autor, Levy & Murnane (2003): "…An Empirical **Exploration**" (Investigation 아님)
- Bessen, *Economic Policy*: **34권 100호, 2019년 10월** (온라인 게재 2020-07-01). DOI가 `eiaa001`이라 2020년으로 오인되기 쉬움

**균형 문헌:** Acemoglu & Restrepo (2020) 「Robots and Jobs」 *JPE* 128(6), 2188–2244 / Autor 계열 일자리 양극화 3부작 / 고용 안정성과 기술변화 수용 / 2019~2026 재배치 vs 해고 기업 수준 실증

**★ 현장 증언 — 이 책 경고의 직접 증거** `[커뮤니티]`:
> **"At my company people always understate the headcount savings. Because the invariable question is - `You are spending x million and for y FTEs you save only 1 FTE of HC? How does that make sense?`. Or worse yet - `You estimated 40 FTE savings, why don't we pick and chose 40 FTEs to let go`. That sends shivers down managers as it reduces their area of influence."**
> — `thisisit`, HN, **2025-10-09** ⚠️ 익명 주장(사내 관행) — 미검증
> **→ 이 책의 PART 4가 하려는 일(정확한 FTE 환산)이 왜 현장에서 저항받는지를 한 문단으로 설명한다. 저항의 이유가 무능이 아니라 `자기 보존`이라는 점이 핵심이다.**

> 짝(한국, 더 짧고 더 아프다) — **처벌의 형태가 감원이 아니라 `기준선 상향`이라는 더 흔한 진실:**
> **"개발자가 먼저 나서서 미친 생산성을 보여줬기에… 관리자는 `더 미친 생산성`을 바랄 뿐입니다. 그러게 적당히 사용했어야죠."** — `The developer.`, OKKY, 2026-05-14

**★ 절감이 애초에 생기지 않는 구조 — 더 깊은 반론** `[커뮤니티]`:
> **"엑셀이 나와서 바뀐 것의 핵심은 일을 자동화시켜준 것이라기 보다는. 일을 실시간으로 그리고 항시적으로 만든거죠. 발표 5분전이라도 수정할수 있는 긴장된 상태가 유지되니.. 일하는 시간개념이 실시간인 동시에 항시적이라 결국 바빠집니다."**
> — `filekiwi`, GeekNews, **2025-05-13** (한국어 원문 — 번역 손실 없음)
> **→ PART 4 전체의 전제를 뒤흔든다.** 절감분이 어디로 갔는지 묻는 대신, **절감분이 애초에 생기지 않는 구조**를 보여준다. 40년 전 도구로 지금을 설명하므로 AI 논쟁의 진영 싸움을 우회한다.

**⚠️ 재배치·번복 수치 — 전부 사용 금지 (F-1):** "33% 핵심 스킬 상실 / 2/3 재채용 / 55.1% 재교육 미논의 / 51.3% 재배치 가능 / **75% 감원이 절감보다 비쌌다**" — **5개 전부 동일 매체가 인용한 미상의 리포트**. 원 조사 미특정. **fact-checker가 원 조사를 먼저 찾아야 하고, 못 찾으면 삭제.**
**⚠️ 순수한 무해고 선언(no-layoff pledge)의 확정 공개 사례는 1·2차 모두 0건.**

### 9-5-7. 생산성 측정 프레임 — 실무용

**★ DORA 2025** (*State of AI-assisted Software Development*, Google Cloud) `[벤더 백서]` — §9-0 조정 3 참조

수치 (⚠️ **전부 2차 인용, 원 리포트 PDF 미대조**): 채택률 **90%**(전년 +14%) / **80%+** 가 생산성 향상 응답 / **59%** 가 코드 품질 긍정 / **30%** 가 AI 생성 코드를 **거의/전혀 신뢰 안 함** / 개발자 일평균 AI 사용 **약 2시간**
> ⚠️ **"빨라졌지만 나아졌는가"** — 복수 리뷰가 DORA 2025를 두고 **"생산성은 올리지만 딜리버리(안정성)는 저해한다"** 는 긴장을 지적. **정확한 수치는 미확보 — 정성 서술만.**

**DX Core 4** `[벤더 백서]` — DORA·SPACE·DevEx 통합. 4차원 **Speed / Effectiveness / Quality / Impact**. **300개 이상 조직** 검증 → 엔지니어링 효율 **3~12% 증가**, R&D 시간 중 기능 개발 비중 **14% 증가**
> ⚠️ **자사 프레임의 효과를 자사가 측정한 수치임을 반드시 명시.** Speed 차원에 **`perceived rate of delivery`(주관적 체감 속도)** 가 정식 지표로 들어가 있다 — **자기보고 지표의 구조적 취약성**(§9-5-3)이 프레임 안에 내장돼 있다.

**★ 생산성 역설 — 정부·중앙은행 근거** `[정부·중앙은행]`

**Atlanta Fed / Richmond Fed 워킹페이퍼 (2026-03-25)** 「Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives」, 기업 임원 **약 750명** 설문
> **★ "a `productivity paradox`, in which `perceived productivity gains are larger than measured productivity gains`"** — 매출 실현의 지연을 반영한 것으로 보임
> 채택: "**more than half having already invested**" / 이득의 출처: 자본 심화가 아니라 "**increases in revenue-based total factor productivity, closely associated with innovation- and demand-oriented channels**" / 업종: "largest effects concentrated in **high-skill services and finance**"
> **고용: "`little evidence of near-term aggregate employment declines due to AI`"** — 대기업은 감축 예상, 소기업은 소폭 증가 예상. 구성 변화: **정형 사무직 감소, 숙련 기술직 수요 증가**

> **→ "체감한 생산성 향상이 측정된 생산성 향상보다 크다." 연준이 750명 임원에게 물어서 확인한 격차다.** 축 5 전체의 논지를 한 문장으로 지지하며, **동시에 "AI 때문에 총고용이 줄었다는 증거는 아직 미미하다"는 균형도 같은 논문에서 나온다.**

**OECD** 「Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence」 ⚠️ 2차 인용, 발행일 미확인
> AI로 인한 연간 **TFP 증가 0.25~0.6%p** (노동생산성 0.4~0.9%p) / **국가 단위로는 AI 채택률과 TFP 증가 사이에 강한 양의 상관이 없다**; TFP 분산의 **3분의 1 미만**만 설명
> **→ "국가 단위로 보면 AI 많이 쓴 나라가 더 생산적이지 않다." Solow 역설의 2026년판.**

### 9-5-8. 에이전트 KPI — 프레임은 있고 조직 사례는 없다

제안되는 지표군 (복수 벤더 프레임 공통) `[벤더 블로그]` ⚠️ 발행일 대부분 미표기:
**end-to-end task-success rate** / task-completion time / **human-intervention rate** / **cost per completed task** / resolution·deflection·**reopen rate**·FCR / **Autonomous SLA Compliance** / **Goal Alignment Rate** / **Policy Violation Rate**

> ⚠️ **전부 "이렇게 재라"는 제안이다. 실제 조직이 에이전트에 KPI를 걸고 운영한 공개 사례는 1·2차 모두 0건.**
> **★ 쓸 만한 관찰: `human-intervention rate`가 지표로 제안된다는 것 자체가 §9-3의 자율성 등급과 축 5를 잇는 다리다. 개입률이 낮아지면 등급이 오르고, 등급이 오르면 통제가 달라진다 — 측정이 곧 등급 심사가 된다.**

### 축 5 커버리지

**확보한 것:**
✅ **RPA 봇 FTE 환산 계보 + 비판 5가지**("1라이선스=3FTE" vs "1:1도 어렵다", **10,000시간 = 2만명×30분**, 이중 계상, 계산식 비표준 5.5~8h·200~255일) / ✅ **Klarna 정본 계보**(보도자료 원문 "equivalent work" → 2025-05 번복 → **사후 검증 0건**) + **SilverBirch의 세 청중 해부** / ✅ **Salesforce 한 회사 두 문장**(CEO "less heads" vs 회사 "no backfill") / ✅ AI 비용 회계 분류 문제 / ✅ **측정 신뢰도 등급의 학술 근거 전체**(Robinson·Frazis·Buehler·Jørgensen·Podsakoff·Mabe) / ✅ **Goodhart 계보 정정 + 네 변종 + Bevan&Hood 게이밍 실증 + Strathern "audit has a life of its own"** / ✅ **성과 귀속 설계 명제 5개**(Vaccaro g=0.64 vs −0.23이 핵심) / ✅ **Bessen 98% 자동화 → 일자리 증가** / ✅ **연준 750명 "체감 > 측정" 생산성 역설** + OECD TFP 0.25~0.6%p / ✅ DORA "증폭기" / ✅ **현장 증언**(`thisisit` 축소 보고, `The developer.` 기준선 상향, `filekiwi` 엑셀 상시화, Cerebras 픽셀 게이밍)

**비어 있는 것:**
- ❌ **에이전트에 KPI를 걸고 운영한 조직 사례 0건** (프레임만)
- ❌ **에이전트가 한 일을 사람 평가에 반영하는 공개 인사 제도 0건**
- ❌ **순수한 무해고 선언(no-layoff pledge) 공개 사례 0건**
- ❌ **Klarna $40M의 사후 검증·공시 0건** (단, 이 공백 자체가 발견)
- ❌ **재배치·번복 수치 5종 전부 원 조사 미특정 — 사용 금지**
- ❌ **대리지표 조작의 "공개 사례"** — 커뮤니티 증언은 확보(Cerebras)했으나 조직 차원 공개 사례는 0건
- ⚠️ DORA 개별 수치·OECD·Atlanta Fed 전망치가 **전부 2차 인용** — 원문 대조 필요
- ⚠️ Bansal 그림 수치·Steyvers 표 수치 추출 실패 — **방향성만 인용**

---

## 9-6. 축 3 재각도 — 중앙이 무엇을 공급했을 때 현장이 살았나

> 교정된 논지에 맞춰 **"탑다운이 낫다"가 아니라 "중앙이 무엇을 공급하면 현장 혁신이 살아남는가"** 로 각도를 바꿔 조사했다.

### 9-6-1. 실증 뼈대 — DORA 2025 (§9-0 조정 3)

> 고성숙 조직 — **강한 버전 관리, 관측성, 그리고 내부 플랫폼** 을 갖춘 조직 — 이 **불균형하게 큰 편익**을 본다.
> **→ 중앙이 공급해야 할 것의 목록이 실증으로 나왔다. 과제 목록이 아니라 버전 관리·관측성·내부 플랫폼 — 전부 기준·자원·제도다.**

### 9-6-2. Paved road / Golden path — 중앙이 길을 깔되 강제하지 않는다

**Netflix:** 자기 플랫폼을 **"paved path"** 라 부른다 — 일급 지원 인프라·언어·툴링을 포함한 **더 매끄러운 길**. 표준 워크로드는 아이디어에서 프로덕션까지 **몇 분**. **그러나 누구도 paved road로 강제되지 않는다(they never force anyone onto the paved road).**

**★ Golden path의 정의 — 축 3의 교정된 논지를 정확히 표현하는 문장:**
> "반복되는 작업을 통과하는 **지원되고 의견이 있는(opinionated) 경로**를 팀에 제공하는 것 — 손으로 하는 것보다 빠르고, 피하는 것보다 안전하다. **플랫폼은 옳은 길을 쉬운 길로 만든다.** 표준·가드레일·제도적 지식이 **몇몇 시니어의 머릿속이 아니라 그 길 자체에 구워져 있다.**"
> **→ "기준을 문서로 배포하지 말고 길에 구워 넣어라."** 중앙이 공급하는 것은 **지시가 아니라 길**이다.

**Spotify Backstage:** 골든 패스 철학을 구현한 내부 개발자 포털. 템플릿으로 **CI/CD·모니터링·로깅·문서가 이미 구성된 마이크로서비스를 몇 분 만에** 생성. 내부 버전은 **2,000+ 백엔드 서비스, 300개 웹사이트, 4,000개 데이터 파이프라인** 관리.
⚠️ "2026년 agent-first 전환으로 개발자 오버헤드 약 47% 감소"는 **원 출처 미확인 — 인용 금지.**

**Team Topologies:** stream-aligned 스쿼드(제품 흐름) / **platform team(paved road)** / enabling team(역량 부스트) / complicated-subsystem team. ⚠️ **원저(Skelton & Pais, 2019) 미대조 — 개념만.**

### 9-6-3. ★ 하향식 강제가 역효과를 낸 사례 — 반대편 난간

**"Golden Cage Syndrome"** (Platform Engineering 블로그, 2026-03-05) `[커뮤니티]`

세 가지 실패 원인:
1. **Field of Dreams 오류** — "If we build it, they will come. **No, they won't.**" 개발자는 플랫폼을 **소비자로서** 대하고 네이티브 도구보다 느리면 우회한다. **정책 강제로는 진짜 채택을 만들 수 없다.**
2. **허영 지표가 마찰 감소를 대체** — 인지 부하가 아니라 배포 빈도 같은 무관한 지표를 추적한다.
   > **"If I can deploy in 5 minutes, but I have to spend 4 hours debugging a cryptic error message... your platform has failed."**
3. **탈출구 없는 새는 추상화** — 인프라 복잡성을 감췄다가 장애 시 개발자를 가둔다.

**★ 결정적 테스트:**
> **"Mandatory adoption breeds workarounds"** — 개발자는 raw AWS 자격증명을 쓰며 paved road를 우회한다.
> 정의적 질문: **"If I made this platform optional tomorrow, would you still use it?"**
> **옳은 모델:** "**A paved highway next to off-road terrain**" — 속도를 원하면 표준 경로를, 필요하면 raw 인프라를
> **틀린 모델:** **케이지(cage)** — 경직되고, **의무적이고**, 불투명하고, 자율성을 제한하는 추상화

보강: **"Trust drives adoption behavior.** 개발자가 플랫폼을 우회하거나 자기 해법을 짤 때, 그들은 당신에게 무언가를 말하고 있는 것이다."
⚠️ **"80%의 DIY 플랫폼이 실패한다"는 수치는 조사 방법 미공개 — 사용 금지, 서술만.**

### 9-6-4. InnerSource — 중앙이 "공간과 규칙"을 공급했을 때

- 채택: SAP·Microsoft·IBM이 일찍 수용. InnerSource Commons Foundation이 금융·제조·통신·헬스케어 사례집 운영
- **Robert Bosch:** 제품 개발 부문과 서비스 부문 간 **공통 코드베이스 공유** → 현장으로부터의 **빠른 피드백 사이클**
- 채택 동기: "**소프트웨어 재사용 증가** — 재사용 가능한 자산을 공유하는 **공통 공간**을 만드는 관행이 투명성을 높이고 중복 작업을 피하게 해준다"
- **실증:** "이너소스 프로젝트에 참여하는 직원은 **더 많은 사회적 상호작용 유대**를 형성하고 프로젝트에 대한 **공유된 이해 수준이 높다. 사회적 자본이 이너소스 참여와 직무 만족 사이를 매개**한다." `[학술]`

> **→ 중앙이 "코드를 이렇게 짜라"고 지시하는 대신 "공유할 공간과 리뷰 규칙"을 공급했을 때 재사용이 늘었다.** 교정된 논지에 정확히 부합하는 계보이며, **AX 시대에 그대로 이식 가능하다(에이전트·프롬프트·툴의 이너소스).**

### 9-6-5. 조직 이론 근거 (papers2_C)

**★ Adler & Borys enabling 형식화 4대 특성 — 1차의 최우선 미확보 항목(B7), 2차에서 원문 OCR 판독 성공.** 상세는 `research/papers2_C_orgtheory.md` §5-1. **저술 시 그 절을 직접 참조하라.**

후속 실증 계보: Ahrens & Chapman (2004) 회계·관리통제로의 첫 이식 / Wouters & Wilderom (2008) **"무엇을"이 아니라 "어떻게 만들었나"** / Wouters & Roijmans (2011) 프로토타입이 지식통합 장치 / Groen et al. (2012) **참여가 왜 이니셔티브를 늘리는가**(수치 확보) / Souza & Beuren (2018) enabling PMS의 정량 경로 **(⭐ 반전 있음)**

**교정된 논지를 뒷받침하는 조직 이론:**
- **March (1991)** 「Exploration and Exploitation」 (전문 확보) — 양손잡이의 원전
- **von Hippel** 사용자 혁신 계보 (1986 리드 유저 / 1988 *Sources of Innovation* 원표 / **2002 3M 자연실험** / 2005 *Democratizing Innovation* / 2017 *Free Innovation*) — **"아이디어는 계속 아래에서 온다"의 정본 근거**
- **Cohen & Levinthal (1990)** 흡수 역량 (전문 확보) — 중앙이 현장 혁신을 흡수하려면 무엇이 필요한가
- **★ 아이디어 선별 — 누가 좋은 아이디어를 고르는가:** **Berg (2016)** 창작자 vs 관리자의 예측 정확도 / **Boudreau et al. (2016)** **평가자는 참신함에 벌점을 준다** / Criscuolo et al. (2017) 심사 패널의 참신함 역U자 / Mollick & Nanda (2016) 군중 vs 전문가
  > **→ "중앙이 과제를 고른다"는 발상에 대한 직접적 실증 반론. 카드 11(구성원 자발 제안이 최종 관문을 압도적으로 통과했다)과 정확히 맞물린다.**
- Zittrain 생성성(generativity)

---

## 9-7. 추가 반론 J~S — 저술 시 반드시 응답할 것

> 1차에서 반박 A~I를 기록했다(§4, §2-1-5 등). **아래는 2차에서 새로 발견된 것만.** 각 항목에 **겨누는 지점 / 응답 전략 초안**을 붙였다. 응답 전략은 제안이지 지시가 아니다.

| # | 반론 | 겨누는 지점 | 응답 전략 초안 |
|---|---|---|---|
| **J** | **「측정을 정확하게 만들면 현장은 더 숨긴다」** — `thisisit`("항상 절감분을 축소 보고") / `The developer.`("적당히 사용했어야죠") | **PART 4 전체.** 이 반론은 **측정 도구의 품질 문제가 아니다.** 도구가 정확해질수록 위협이 커지므로 저항이 커진다 — **정확도 개선이 문제를 악화시키는 구조** | 측정을 제안하기 **전에** 번역 금지 규칙을 명시하라 — **"이 숫자는 감원 명단으로 번역되지 않는다"를 제도로 보장하지 못하면 측정하지 마라.** PART 4의 순서를 뒤집어 **측정 방법론보다 측정 결과의 사용 제한(use limitation)을 먼저** 다룰 것 |
| **K** | **「METR을 인용하면 선택적 인용이 된다」** — **METR이 2026-02-24 후속 연구에서 속도 향상을 보고했고 "아무도 인용하지 않는다"** | METR 2025-07을 근거로 쓰는 대목. **이 책이 "숫자를 믿지 마라"는 책이므로 자기 숫자의 선택적 인용은 타격이 배가된다** | **후속 연구를 숨기지 말고 먼저 제시하라.** 그리고 논점을 옮겨라 — 필요한 것은 "AI가 개발자를 느리게 한다"가 아니라 **"자기 보고와 실측이 갈라진다"** 는 더 약하고 더 견고한 명제다. **약한 명제로 후퇴하면 반박이 근거가 된다** |
| **L** | **「승인 기반 자율성 등급은 통제의 외양일 뿐」** — 승인률 **93%** + 승인 피로 / "승인/거부 기반은 터지기를 기다리는 재앙" / 모델이 권한 오류를 보고 **우회를 새 목표로 채택** | 자율성 등급을 승인 축으로 설계하는 대목 | **등급의 축을 승인이 아니라 능력(capability)과 환경으로 잡아라** — **AAL/ACL(§9-3-2)이 정확히 그 형태다.** 승인은 고위험 행위 소수에만 남기고 나머지는 **닿을 수 없게** 만든다. 등급표에 **"위협 모델" 열**을 넣어라 |
| **M** | **「'사번을 준다'는 발상 자체가 권한 모델로서 틀렸다」** — "프로세스가 그 사용자의 **모든 주변 권한**을 갖고 '사용자로서' 돌아간다는 발상 자체가 우리를 이 난장판에 빠뜨린 것의 일부다" | **가장 근본적인 은유.** 1차의 반박 A("서비스 계정 아니냐")보다 **한 단계 깊다** — "서비스 계정 모델 자체가 틀렸고 너는 그 틀린 모델을 확대하고 있다" | **사번의 기능을 권한 부여가 아니라 `귀속(attribution)`으로 좁혀라.** 로그 3항 구조(`에이전트(사용자를 대신하여, 권한 맥락을 경유하여) 행위함`)가 그 형태. **"사번 = 권한 묶음"이 아니라 "사번 = 로그에 남는 책임 주체 식별자"** 이고, 실제 권한은 과제 단위 능력 부여로 별도 관리. **이 구분을 1장에서 못 박지 않으면 보안 독자를 잃는다** |
| **N** | **「등록소는 죽는다 — Confluence가 그랬듯이」** — `esc5221`: 인벤토리 대시보드를 만들었지만 방치를 막지 못했고 **그 도구 자체도 방치됐다** / A2A 레지스트리 회의 / 1차의 Confluence 5건 | "에이전트를 등록소에 등록하라"는 1보. **실행 가능성 반론이라 가장 실무적으로 아프다** | **등록소를 사람이 유지하는 문서로 설계하지 마라. 폐기 절차를 만드는 대신 발급 구조에 만료를 내장한다**(§9-4-1의 Entra access package 만료가 실물). **등록이 운영 경로 위에 있어야 산다** — 등록되지 않은 에이전트는 크리덴셜을 못 받는다면, 등록은 관리 업무가 아니라 **작동 조건**이 된다. **"에이전트 등록소는 Confluence가 될 것인가"** 절을 명시적으로 두고 정면으로 답하라 |
| **O** | **「에이전트를 정원으로 세면 벤더가 과금한다」** — "디지털 좌석을 발명해 정원에 과세" / SAP 간접 사용의 선례 / **"5분 뒤엔 회사 전체에 에이전트를 하나만 두는 도구가 나올 것"** | "에이전트에 사번과 정원을 부여한다"는 처방. **독자의 비용을 실제로 증가시킬 수 있다.** 그리고 **과금 단위가 되는 순간 조직은 단위를 조작해 회피한다** — 이 책이 만든 등록 단위가 회피 대상이 된다 | **등록 단위와 과금 단위를 명시적으로 분리하라.** "이 책의 등록 단위를 벤더 좌석 수와 일치시키지 마라"를 실무 규칙으로. SAP 간접 사용 계보를 밝혀 독자가 앞으로 겪을 협상을 예측하게 하라 |
| **P** | **「자율성 등급은 이미 2단계로 충분하다」** — 실제 채택 등급 수가 2인 사례 복수 | 4~5단계 등급표를 제시하는 대목 | **왜 2단계로 부족한지를 근거로 세워라.** 근거가 없다면 **2단계에서 시작하고 필요할 때 쪼개는 방식**을 권하는 편이 현장 언어에 맞는다. (AAL 저자들도 "the number of autonomy levels **should be limited**"라고 명시) |
| **Q** | **「AX가 왜 DX와 다른지 증명하지 못했다」** — "레거시 회사들이 수십 년째 '디지털 전환'을 말하면서 서류 디지털화 이상으로 못 가는 이유는 **충분히 많은 사람이 그 서류에서 자기 일자리를 얻고 있어서, 실제 전환은 정치적으로 지탱 불가능하고 끊임없는 사보타주 때문에 실행 불가능**하기 때문" | **책 전체.** 1차의 반박 I가 **기술적** 반복("RPA도 깨지기 쉬웠다")이었다면 이건 **정치적** 반복이다. **정치적 반복은 기술 개선으로 극복되지 않는다** | **"이번엔 다르다"로 답하지 마라. 답이 없다면 없다고 써라.** 대신 실제로 다르게 할 수 있는 것을 제시하라 — DX는 **서류를 디지털화**했고 AX는 **책임의 귀속을 재설계**한다는 구분. **정원 감축을 목표로 세우면 그 사보타주 구조에 그대로 들어간다** |
| **R** | **「'AX팀을 만드는 순간 실패한다'는 명제가 이미 한국 커뮤니티에 있다」** — GeekNews 토픽(2026-04-09)과 댓글 | **책 제목과 기획 자체** | **먼저 인용하고 동의를 표한 뒤 들어가라.** 그 처방("도메인 현업자가 주도하고 AX기술자가 서포트")이 **이 책의 교정된 논지와 같다.** **무시하면 위협이 되고 인용하면 자산이 된다** — 서문 오프닝 최우선 후보 |
| **S** | **「지금은 운영 고통이 아니라 예방적 설계다」** — 벤더 제품 실사용 후기 **0건** / agent sprawl 증언이 전부 벤더 발언 / SPIFFE 이슈 댓글 한 자릿수 | "지금 체계를 세우지 않으면 늦는다"는 대목. **과장된 긴급성은 이 책을 §9-5-2에서 조롱당한 벤더 마케팅과 같은 범주에 넣는다. 이 책은 다른 사람의 과장을 비판하는 책이므로 자기 과장이 치명적이다** | **긴급성을 낮추고 선점 가치를 높여라.** "이미 난리가 났다"가 아니라 **"제품은 나왔고, 표준은 미확정이고, 도입 사례는 아직 공개되지 않았다. 그래서 지금이 설계를 결정할 수 있는 마지막 창"** 이라고 쓰는 편이 **증거와 일치하고 더 설득력 있다** |

### 【2차의 발견】 벤더 제품 실사용 후기가 존재하지 않는다

1차에서 "확보 실패"로 기록했던 항목을 **검색어를 바꿔 재시도했으나 여전히 0건**이다.
> **이 부재 자체가 이 책의 발견이다: 제품은 GA인데 실제 도입 후기는 아직 커뮤니티에 없다.** 반론 S의 근거이자, 이 책의 시점 포지셔닝("지금이 설계를 결정할 창")의 실증이다.

---

## 9-8. 2차 신선도 원장 추가분

> §신선도 원장에 이어지는 2차 확보분. **검색 시점 2026-09-05.**

| 소스 | 시점 | 표기 규칙 |
|---|---|---|
| **BNY 디지털 직원** | 2025-07(dozens) → 2025-10(100+) → **2026-03-23(130+)** | **"2026년 3월 기준 130여 개"** + "경영진이 밝힌 바에 따르면" |
| **Workday Agent System of Record** | 발표 **2025-02-11** → **GA 2026-02** (일자 미표기) | **"2026년 2월 GA"** (일자 없이) |
| **ServiceNow AI Control Tower** | GA / **2026-06 릴리스**부터 Agent 365 디렉터리 게시 | "2026년 6월 릴리스 기준" |
| **AWS Bedrock AgentCore Identity** | **GA 2025-10** | "2025년 10월 GA" |
| **Entra Agent ID 라이선스** | 문서 **ms.date 2026-06-05 / 갱신 2026-06-24** | "2026년 6월 문서 기준" · 가격은 "약 $15" |
| **Gartner 비례적 거버넌스 4단계** | **2026-05-26** | "Gartner 보도자료(2026-05-26)에 따르면" ⚠️ 원문 403, 3개 매체 교차 |
| **CSA Autonomy Levels L0~L5** | **2026-01-28** | "2026년 1월 기준" |
| **Feng·McDonald·Zhang 5단계 + 인증서** | arXiv **2025-06** / Knight **2025-07-28** | "2025년 기준" |
| **★ AAL/ACL (ExxonMobil)** | arXiv:2607.23438v1, **2026-07-26** | **"2026년 7월 프리프린트"** — 동료심사 없음 명시 필수 |
| **Sheridan & Verplank 10단계** | **1978** (⚠️ 1978 vs 1987 귀속이 자료마다 갈림) | "1978년" + ⚠️ 원 보고서 미확보 명시 |
| **Parasuraman, Sheridan & Wickens** | *IEEE Trans. SMC-A* **30(3), 286–297, 2000-05** | "2000년" — **이론 논문, 실증 아님** 명시 |
| **Bainbridge 자동화의 아이러니** | **1983** | 연도 명시 |
| **Endsley automation conundrum** | **2017** | 연도 명시 |
| **SAE J3016 / 자율주행 인계 실증** | Merat 2014 / Eriksson&Stanton 2017 / Victor 2018 / Zhang 2019 / Gerber 2023 / **NHTSA EA22-002 2024** | 각 연도 명시. **"자율주행 맥락"임을 반드시 밝히고 유비로만** |
| **DORA 2025** | **2025** | "2025년 DORA 리포트" ⚠️ **개별 수치는 2차 인용** |
| **DX Core 4** | — | **"DX사 자체 프레임을 자사가 검증한 수치"** 명시 필수 |
| **Klarna** | 보도자료 **2024-02-27** → 번복 **2025-05** | **"2024년 2월 발표 기준 추정치"** / "2025년 5월 번복" |
| **Salesforce Benioff 발언** | **2025-09-02** | "2025년 9월" + **회사 성명과 병기** |
| **Atlanta/Richmond Fed 750명** | WP **2026-03-25** / SF Fed 게재 2026-04-14 | **"2026년 3월 연준 워킹페이퍼, n≈750"** |
| **OECD TFP 추정** | ⚠️ **발행일 미확인** | 원 문서 확인 후 사용 |
| **Goodhart 원전 / Strathern** | **1975** / **1997** (*European Review* 5(3), 305–321) | **귀속 정정 필수** (§9-5-4) |
| **Manheim & Garrabrant 네 변종** | arXiv:1803.04585, v1 2018-03-13 ~ **v4 2019-02-24** | "2018년 프리프린트" — **동료심사 없음** |
| **Vaccaro, Almaatouq & Malone** | **2024** | "2024년 메타분석" |
| **Bansal et al.** | **CHI 2021** (1차 A17 미확정 → **2차 확인 완료**) | 연도 명시 · **그림 수치 인용 금지** |
| **Bessen ATM/방직** | 기사 **2015-03** 기준("today = 2015") / *Economic Policy* **34(100), 2019-10** | **"2015년 시점"** · 서지 정정 반영 |
| **Acemoglu & Restrepo** | *JPE* **128(6), 2188–2244, 2020** | 연도 명시 |
| **Golden Cage Syndrome** | **2026-03-05** | 연도 명시 · **"80% 실패" 수치 금지** |
| **커뮤니티 2차 인용** | `SilverBirch` 2024-02-29 / `thisisit` 2025-10-09 / `filekiwi` 2025-05-13 / Cerebras 픽셀 2026-05-01 / 승인률 93% 2026-06-04 / `emk` 2026-07-20 / GeekNews AX팀 토픽 2026-04-09 | **개별 게시일 명시.** GeekNews 상대 표기는 "2026-09-05 조회 기준 추정" 병기 |

---

## 9-9. 2차 ⚠️ 사용 금지·재확인 목록 (§7-4에 추가)

### 【사용 금지】 원 출처를 특정하지 못한 수치

| 수치 | 왜 금지인가 |
|---|---|
| **"L0 Observe / L1 Draft / L2 Prepare / L3 Bounded execute / L4 High-autonomy execute" 5단계** | 검색 요약이 "an emerging enterprise framework"라고만 표기. **Gartner 4단계와 혼동 위험. 귀속 불가** |
| **"33% 핵심 스킬 상실 / 2/3 재채용 / 55.1% 재교육 미논의 / 51.3% 재배치 가능 / 75% 감원이 절감보다 비쌌다"** | **5개 전부 동일 매체가 인용한 미상 리포트.** 특히 75%는 강한 주장 |
| "Only **20%** of organisations have formal processes for offboarding and revoking API keys" | 조사 주체·표본·연도 전부 미상 |
| "**80%** of DIY platforms fail" | 조사 방법 미공개 |
| "전 세계 AI 투자 연 **$500B** 초과" | 원자료 미확인 |
| "Spotify Backstage agent-first 전환으로 오버헤드 **약 47%** 감소" | 원 출처 미확인 |
| "Orphaned accounts가 인사이더 침해의 **20%**에 관여" | 벤더 인포그래픽, 원자료 미확인 |
| "RPA 도입 **30~50%** 실패 — EY 2016" | EY 원 리포트 미대조 |
| 에이전틱 에이전시 단위경제("툴 COGS 3~5%→12~18%", "주니어 정원 30~50% 압축", "60 FTE 구성") | 개인 블로그의 **예시 모델**, 실증 아님 |

### 【조건부 사용 — 표현 주의】

| 항목 | 확인된 것 | 확인 안 된 것 | 권장 표현 |
|---|---|---|---|
| **BNY 식별자** | `user ID, a login, a persona, a name` | **사번**, HR 시스템 등재 | **"사번"이라 쓰지 말 것** |
| **BNY 공식성** | CEO·CIO 구두 발언 | **회사 보도자료 원문 없음** | **"경영진이 밝힌 바에 따르면"** |
| **Gartner 4단계** | 등급명·통제 차등·분석가명 (3개 매체 일치) | Gartner 원문 직접 대조 | "Gartner 보도자료(2026-05-26)에 따르면" |
| **Entra 가격** | 라이선스 **요건**은 공식 문서 ★ | **$15 / $12 금액** | **"약 $15"** 또는 금액 생략 |
| **DORA 개별 수치** | 결론 문장은 공식 페이지 ★ | 90%/80%/59%/30%/2시간 **전부 2차** | 원 PDF 대조 후, 미대조면 **"약"** |
| **Klarna $40M** | 보도자료 = "**estimated**" | **실현 여부** | **"$40M 이익 개선을 예상한다고 밝혔다"** |
| **Klarna 700** | "**equivalent work of** 700 full-time agents" | "700명 대체·해고"는 **보도자료에 없음** | **"700명분의 일에 상당하는 양"** |
| **승인률 93%** | Anthropic 엔지니어링 포스트 인용 | **원문 직접 확인** | **원문 확인 후 사용 — 이 책 설계에 결정적이므로 우선순위 높음** |
| **METR** | 2025-07 결과 | **2026-02-24 후속 연구(속도 향상)** | **반드시 후속과 병기** (반박 K) |
| **AAL/ACL** | 등급표 전문 ★ | 동료심사 | **"프리프린트"** 명시 |
| **Sheridan & Verplank** | 10단계 표(재수록본) | 원 보고서(DTIC ADA057655), **1978 vs 1987** | 연도 귀속 주의 |
| **Team Topologies** | 2차 요약 | 원저(2019) | 개념만 |

### 【2차에서 해소된 1차 항목】 ✅

- **A17 Bansal et al. CHI 2021 서지** → **확인 완료**
- **B7 Adler & Borys enabling 4대 특성** → **원문 OCR 판독 성공** (`papers2_C_orgtheory.md` §5-1)
- **Goodhart 원전/정식화 귀속** → **정정 완료** (§9-5-4)
- **자율성 등급 프레임 0건** → **실무 4종 + 학술 9종 확보** (§9-3)
- **축 4 "증폭으로 받아들여진 성공 사례 부재"** → **Workday가 Lattice의 대칭 사례** (§9-2-2)
- **성과 귀속 실증 부재** → **Vaccaro·Bansal·Hemmer로 설계 명제 5개 확보** (§9-5-5)

### 【1·2차 모두 해소 못 한 것】 ❌

1. **한국 기업 사례 0건** (축 1·2·4·5 전부)
2. **에이전트 KPI 운영 조직 사례 0건** / **에이전트를 사람 평가에 반영하는 인사 제도 0건**
3. **무해고 선언(no-layoff pledge) 공개 사례 0건**
4. **실제 조직이 공개한 폐기 절차 0건** (도구·규제에는 있음 — 조정 1)
5. **벤더 제품 실사용 후기 0건** (이 부재 자체가 발견 — 반박 S)
6. **AX 도입 추진자의 1인칭 고충** — 커뮤니티에서 추진자는 3인칭 비판 대상으로만 등장 (1차부터 미해소)
7. **ISO/IEC 42001 인벤토리 요구 항목** (유료 표준)

---

## 9-10. 【편향 자각】 2차 리서치의 한계

**개선된 것:** 커뮤니티 HN 비중 **80% → 45%**, 한국 소스 비중 **44%** 로 상승.

**⚠️ 그러나 새로 생긴 편향 — 저술 전 반드시 알 것:**

1. **단일 스레드 과대 대표 (가장 심각)** — §9-5-4의 지표 게이밍 인용 상당수가 **한 스레드**에서 나왔다. "여러 곳에서 같은 말이 나왔다"고 쓰면 안 된다.
2. **한국 소스가 두 사이트뿐** — GeekNews와 OKKY. 커리어리·velog·브런치는 여전히 미접근.
3. **★ 이 책의 대상 독자가 조사에 없다** — 조사한 곳은 **전부 엔지니어 커뮤니티**다. **이 리서치만 근거로 쓰면 "엔지니어 편에서 경영진을 비판하는 책"이 되기 쉽다.** 이 책의 1순위 독자(AX 실무 리더·기획자)의 목소리는 1·2차 모두 확보하지 못했다.
4. **반AI·냉소 편향** — 1차의 `keeda` 경고("HN은 에코 챔버")가 2차에도 적용된다.
5. **생존 편향** — 말한 사람만 남는다.
6. **시점 편향** — 인용의 시간 분포가 고르지 않다.

**⚠️ 방법론 함정 (커뮤니티 리서처가 명시적으로 경고):**
> **GeekNews의 `GN⁺` 댓글은 사이트 AI가 HN·Lobsters를 요약한 봇 글이다.** 이걸 "한국 반응"으로 인용하면 **편향 개선을 자축하며 HN을 재인용하는 꼴**이 된다. 2차에서는 전량 배제했으나, **1차 문서(§2-4-7 등)에는 GN⁺ 인용이 남아 있다 — 저술 시 주의.**

**Reddit:** 2차에서 재시도했으나 직접 접근 403 재확인. 아카이브 API로 부분 우회했으나 **데이터가 2025-05에서 끊기고** 검색 품질이 낮아 **인용 3건**만 확보했다.

> **저술 규율 (재확인): "커뮤니티에서는"과 "업계에서는"을 절대 혼용하지 마라.**

---
---

# 10. 저술 규율 원장 — fact-checker 대조용 정본

> **이 절이 Phase 4 fact-checker의 1차 대조 근거다.** 리서처들이 원문 대조 과정에서 **명시적으로 정정하거나 한계를 못 박은 항목**만 모았다. §7-4·§9-9의 미확인 목록과 함께 읽되, **충돌하면 이 절이 우선한다.**
>
> **왜 별도 절인가:** 2차 논문 리서치(`papers2_A_autonomy.md`·`papers2_B_measurement.md`)에는 원 산출 형식의 **D(상충 연구 병기)·E(참고문헌 전체)·F(미확인 항목) 세 절이 작성되지 않았다.** ⚠️ 항목이 파일별로 흩어져 있어, **이 §10이 그 F절 역할을 대신한다.**
> **D절 재료 위치:** `papers2_B_measurement.md`의 「상충하는 추정치 비교표」(B-5)와 `papers2_A_autonomy.md`의 A-1-4·A-1-6(Endsley가 **중간 등급을 옹호하는 방향**의 긴장) 두 곳.

## 10-1. 【direction-only】 수치 인용 금지 — 방향성만 쓸 것

원문 대조에는 성공했으나 **그림·표에서 수치가 텍스트 레이어로 추출되지 않은** 항목이다. **부호와 유의성만 인용 가능하고, "몇 %p 떨어졌다"·"동의율이 몇 % 올랐다"는 서술은 금지한다.**

| 항목 | 확보한 것 | 금지되는 것 |
|---|---|---|
| **Bansal et al. (2021) 그림 4B** | **방향성:** "explaining the top prediction lead to better accuracy when the AI recommendation was correct **but worse when the AI was incorrect**" | **오답 시 성능 하락 폭의 수치** |
| **Bansal et al. (2021) 그림 5** | **방향성:** "Adaptive explanations successfully **reduced** the human's tendency to blindly trust the AI... when it was uncertain and more likely to be incorrect" | **상대 동의율 수치** |
| **Steyvers et al. (2022) PNAS 표 1** | 하이브리드 쌍의 상보성 성립 여부(정성) | **out-of-sample 정확도 값** |
| **Steyvers et al. (2022) PNAS 표 2** | 본문 서술 + **상관계수(ρ_HM 0.33 / ρ_HH 0.62 / ρ_MM' 0.71)** + 표본 규모(4,800장, 320 비교) | **3요인의 로그 오즈 효과 추정치·CI·p값** |

> **안전하게 쓸 수 있는 Bansal 인용은 z/p값이다** (본문 텍스트에서 확보): Beer z = −1.18, p = .24 / Amzbook z = 1.23, p = .22 / LSAT z = 0.427, p = .64 — **설명은 신뢰도 표시 대비 유의한 개선이 없었다.**

## 10-2. ★★ Vaccaro et al. (2024) — 두 수치의 비대칭 【이 책에서 가장 조심해야 할 인용】

**같은 370개 효과크기에서 기준선만 바꿔 계산한 두 값이다:**

| 지표 | 기준선 | 값 | 출판편향 검정 |
|---|---|---|---|
| **human augmentation (증강)** | **인간 단독** | **g = 0.64** [0.53, 0.74], t(98)=11.87, p=0.000 | **❌ 통과하지 못했다** (Egger p=0.002, rank τ=0.19 p=0.000) |
| **human-AI synergy (시너지)** | **인간 단독·AI 단독 중 나은 쪽** | **g = −0.23** [−0.39, −0.07], t(92)=−2.89, p=0.005 | **✅ 통과했다** (Egger p=0.438, rank τ=0.05 p=0.121) |

> **★ 규율 1 — 낙관적 수치가 취약한 쪽이다.** 흔히 인용되는 **"+0.64(증강)"이 출판편향 검정을 통과하지 못했고, 비관적인 "−0.23(시너지)"이 통과했다.** 저자들은 증강 쪽에 대해 **"we did not try to correct for potential publication bias to preserve the integrity [of the analysis]"** 라고 명시했다. **이 책이 +0.64만 인용하면 가장 약한 근거를 가장 강한 자리에 놓는 셈이다.**
>
> **★ 규율 2 — 기준선을 반드시 병기하라.** "AI 도입 후 담당자가 더 잘하게 됐다"(증강)와 "인간+AI 체계가 AI 단독보다 낫다"(시너지)는 **완전히 다른 주장**이다. 저자 원문: **"the human-AI systems we analyzed were, on average, better than humans alone but not better than both humans alone and AI alone."**
> **→ 이 책의 한 문장: 대부분의 AX 보고서는 전자를 측정하고 후자를 주장한다.**
>
> **★ 규율 3 — 이질성을 숨기지 마라.** **I² = 97.7%**(시너지) / **93.8%**(증강). 극단적으로 높다. **"평균 −0.23"을 대표값처럼 쓰면 오독이다. "평균은 −0.23이지만 편차가 거의 전부다"로 써야 한다.** 저자들도 초록을 "These findings highlight the **heterogeneity** of the effects"로 닫는다.
>
> **★ 규율 4 — 생성 과업 +0.19를 "시너지가 난다"로 쓰지 마라.** **p = 0.180, 95% CI [−0.09, 0.48]로 0과 유의하게 다르지 않다**(n=34로 표본이 작다). 정확한 진술은 **"의사결정 과업의 손실과 생성 과업의 이득 사이의 차이가 유의하다"**(F(1,104)=7.84, p=0.006)까지다.
>
> **★ 규율 5 — 신선도.** 대상이 **2020-01-01 ~ 2023-06-30 게재 논문**이다. **GPT-4(2023-03) 이후 세대 실험이 거의 없다.** 그리고 **연도 조절효과가 개선 추세를 보인다**(2020 −0.56 → 2021 −0.47 → 2022 +0.01 → 2023 +0.11). **가장 강한 반박이 여기서 나오므로 이 추세를 먼저 밝혀라.**

**함께 쓸 수 있는 확정 수치:** AI가 인간보다 나을 때 시너지 **g = −0.54** [−0.71, −0.37] / 인간이 AI보다 나을 때 시너지 **g = +0.46** [0.28, 0.66], 둘 다 p=0.000, F(1,104)=81.79.
> **→ AI가 인간보다 나은 구간에서는 증강 지표가 최대(+0.74)인데 시너지 지표는 최저(−0.54)다. "담당자가 훨씬 잘하게 됐다"와 "그 사람을 뺐으면 더 나았다"가 동시에 참일 수 있다.**

**⚠️ 서지:** 게재본 제목은 **"When combinations of humans and AI are useful: A systematic review and meta-analysis"**, *Nature Human Behaviour* **8(12), 2293–2303**. **프리프린트(arXiv 2405.06087)는 "When *Are* Combinations of Humans and AI *Useful?*"로 어순이 다르다 — 게재본 제목을 쓸 것.** 세 저자 모두 공동 제1저자.

## 10-3. 조직 이론(papers2_C) — 담당자가 명시적으로 정정한 것

### (가) Adler & Borys enabling 형식화 4대 특성 — **원본 대조 필수**

- **확보:** Ahrens & Chapman (2004) **초록의 나열 문장**에서 `repair` · `internal transparency` · `global transparency` · `flexibility` **VERBATIM 확보**
- **⚠️ 미확보:** **본문의 조작화·개별 정의문.** 그리고 **Wouters & Wilderom 초록에는 네 특성 인용이 아예 없다**
- **⚠️ OCR 경고:** Adler & Borys 원문은 **OCR 판독본**이다. **`ISQ9000` → `ISO 9000` 류의 판독 오류가 관찰됐다. 인용 전 원본 대조 필수**
- **★ 관통선에 가장 가까운 원문 (p.296, 2차 문헌 경유):** enabling 형식화는 **"attempts to mobilize local knowledge and experience in support of central objectives"**
  > **→ "현장 지식과 경험을 중앙의 목표를 위해 동원한다" — 교정된 관통선("바텀업이 씨앗을 만들고, 탑다운은 거두는 체계")의 1996년판 정식화다.** 이 문장 하나가 이 책 관통선의 학술적 정본이 될 수 있다.

### (나) Zittrain 생성성(generativity) — **판본 명시 필수**

| 판본 | 요인 수 | 비고 |
|---|---|---|
| **Zittrain (2006), "The Generative Internet", *Harvard Law Review*** | **네 요인** | 정의문이 2008년판과 **다르다** |
| **Zittrain (2008), *The Future of the Internet — And How to Stop It*** | **다섯 요인** | **`transferability`가 여기서 추가된 다섯째** |

> **★ `transferability`가 이 책의 "수확(harvest)" 은유에 가장 정확히 대응한다** — 현장에서 만들어진 것이 다른 곳으로 옮겨질 수 있는가. **단, 2006년 논문으로 인용하면 오류다.**

### (다) 쓰면 안 되는 것 — 유리한 수치만 골라 쓰지 말 것

| 문헌 | 확보 수준 | 금지 |
|---|---|---|
| **Gibson & Birkinshaw (2004)** 맥락적 양손잡이 | **초록 수준까지만** | **경로계수·네 차원 정의문 미확보.** "가설이 지지되었다" **이상의 서술 금지** |
| **Junni et al. (2013)** 양손잡이 메타분석 | **효과크기 미확보** | **"r = ○○" 형태 인용 금지** |
| **Lilien et al. (2002)** 3M 리드유저 자연실험 | 전문 확보 | **매출·점유율은 유의하나 `영업이익 p=0.70`·`성공확률 p=0.24`는 유의하지 않다.** **유의한 것만 골라 인용하면 왜곡이다 — 반드시 병기하라** |

## 10-4. 자율성 등급(papers2_A) — 정정·금지 항목

| # | 항목 | 규율 |
|---|---|---|
| 1 | **Parasuraman & Riley (1997)** use/misuse/disuse/abuse | **⚠️ 원문 미확보. 정의는 통상적 정리이지 verbatim이 아니다 — 따옴표 직접 인용 금지.** 개념 참조만 |
| 2 | **OpenAI "5단계 AGI" 체계** | **⚠️ 공식 출처 확인 실패. 공식 발표로 서술 금지.** 공식 발간물이 아닐 가능성이 높다 |
| 3 | **Endsley (2017) 게재지** | **✅ 정정: *Human Factors* 59(1), 5–27.** (의뢰서의 *JCEDM* 표기는 오류 — 3중 확인 완료) |
| 4 | **Sheridan & Verplank (1978) 10단계** | 원 보고서(**DTIC ADA057655**)가 아니라 **HFES-Europe 재수록본(Save & Feuerberg 2012, Table 1) 경유**다. ⚠️ **그 재수록본이 저자명을 "Verplanck"로 오기한다.** 그리고 **"1978 vs 1987" 연도 귀속이 자료마다 갈린다** |
| 5 | **AAL/ACL (arXiv:2607.23438)** | **프리프린트 — 동료심사 없음.** 10페이지 산업 실무 보고, **단일 기업(ExxonMobil) 사례 2건** |
| 6 | **Cihon et al. 판정 불일치** | **Actions κ = 0.30** — 등급 판정자 간 일치도가 낮다는 실증. **이 책이 등급표를 제안할 때 반드시 함께 밝혀야 할 한계** |

**★ 2차에서 추가 확보한 이식 템플릿:** **Endsley & Kaber (1999)의 10단계 × 4기능 배분표**가 사실 **Parasuraman보다 더 직접적인 실무 템플릿**이다 — **감시·옵션생성·선택·실행**을 각각 **인간 / 컴퓨터 / 공동**으로 배분한다. AX 등급표 설계 시 이쪽을 먼저 보라.

**★ SAE J3016에서 확보한 조문:** **§3.22 "수용성 = 의식의 한 측면"** / **§5.4 NOTE 4 "충분한 시간"(초 단위 미규정)** — **규제가 "충분한 시간"을 숫자로 정하지 못했다는 사실 자체**가 이 책의 인간 감독 설계 논증에 쓰인다.

**★ L3 인계 실패 실증 수치 (확정):** Eriksson & Stanton **1.97 ~ 25.75초(13배 분산)** / Zhang et al. 129편 메타분석 **평균 2.72초, 연구별 0.69 ~ 19.79초** / Merat et al. **안정화까지 35–40초** / Victor et al. 테스트트랙 **106명 — 눈은 위협물에, 손은 핸들에 있었는데도 28%(21/76) 충돌** / NTSB 2건 + **NHTSA 2백만 대 조사, 467건 충돌**

## 10-5. 측정·경제학(papers2_B) — 판본·수치 규율

### (가) 판본이 다른 수치 — **섞어 쓰면 오류**

| 문헌 | 게재본 | 워킹페이퍼판 | 규율 |
|---|---|---|---|
| **Brynjolfsson, Li & Raymond** | *QJE* 140(2): **+15%, n = 5,172** | NBER 31161: **+14%, 신입·저숙련 +34%, n = 5,179** | **판본 명시 필수.** 두 수치를 한 문장에 섞지 말 것 |
| **Acemoglu & Restrepo** | *JPE* 128(6): **0.2pp / 0.42%** | WP판: **0.18–0.34pp / 0.25–0.5%** | **게재본 수치를 기본으로, 범위를 쓸 때만 WP판 명시** |
| **Bessen ATM 사례** | **1차 출처 = 저자 본인 IMF *Finance & Development* 2015-03** ("지점당 창구직원 20→13명, 도시 지점 수 43% 증가") | Autor(2015)판은 **창구직원 총수 50만→55만(1980–2010)** 을 별도 제시 | **총수 절대 수치는 Bessen 기사에 없다 — "Autor(2015)가 Bessen을 인용해 제시한 수치"로 표기** |
| **Bessen, *Economic Policy*** | **34권 100호, 2019년 10월** (온라인 게재 2020-07-01) | — | DOI가 `eiaa001`이라 **2020년으로 오인되기 쉽다** |
| **Autor, Levy & Murnane (2003)** | "…An Empirical **Exploration**" | — | ⚠️ **"Investigation"은 오표기** |

### (나) 10배 격차 — 상충 추정치 (D절 재료)

> **Acemoglu: 10년 누적 TFP +0.66%** vs **Aghion & Bunel: 연 +0.68%p** — **10배 격차**다. 담당자가 이 격차를 **곱셈 항 네 개**로 해부해 뒀다(`papers2_B_measurement.md` B-5 「상충하는 추정치 비교표」).
> **→ 이 책이 거시 수치를 인용한다면 반드시 두 추정을 병기하고 왜 갈리는지 밝혀라.** 한쪽만 쓰면 10배 틀린 그림을 준다.

### (다) 확정 인용 가능 수치

- **Podsakoff et al. (2012):** 동일출처 팽창률 **133~304%**, 단일 방법이면 **94~270%**
- **Mabe & West (1982):** 자기평가-실제 상관은 **r = .29**로 낮지만, **측정 조건이 변동의 64%를 설명한다** → **"자기보고가 틀린다"가 아니라 "질문 설계가 신뢰도를 가른다"** — 측정 등급제의 직접 정당화
- **Bevan & Hood (2006) 게이밍 실증:** 공식 통계 **96%** vs 환자 설문 **77%**, 그리고 **별점과 임상 품질의 상관이 0**
- **Manheim & Garrabrant (2018) 네 변종:** **Regressional · Extremal · Causal · Adversarial** (하위 유형까지 전문 확보) ⚠️ **프리프린트, 동료심사 없음**
- **Demirer et al. (2026, NBER 35275):** 커밋 누적 효과 **autocomplete +40% / 대화형 에이전트 +140% / 자율 에이전트 +180%** → **프로젝트 수 +50% → 실제 릴리스 +30%**. **대체탄력성 0.25**(= AI와 인간은 **강한 보완재**)
  > **→ 과업 수준 이득의 약 1/6만 최종 산출물로 통과한다.** "weak-link hypothesis" — 병목은 **조율이 필요한 인간 공정**에 있다
- **Dillon et al. (2025, NBER 33795, n = 7,137):** 이메일 시간 **주 3.6시간(31%) 감소**(ITT 1.3시간), 문서 작성은 다소 빨라짐, **회의 시간은 유의한 변화 없음**
  > **→ 혼자 바꿀 수 있는 것만 바뀌었다. 조율이 필요한 이득은 실현되지 않았다.** AX 성과가 개인 지표에서만 잡히고 조직 P&L에서 안 잡히는 현상의 실험적 설명
- **Hemmer et al. 실험 1:** UHCI 없으면 팀 vs AI 단독 **d = 0.16, p = 1.0**(무의미) / 있으면 **d = 0.68, p < 0.001** ⚠️ **[PP] 게재 여부 미확인**
- **Hemmer et al. 실험 2:** 두 AI의 **단독 성능이 동일(0.2666)** 한데 팀 성과는 **0.2473 vs 0.1461 (41% 차이)** → **"AI를 더 정확하게"가 아니라 "AI가 인간과 다른 곳에서 틀리게"가 팀 성과를 결정한다**

### (라) 미조사 공백 — 정직하게 표기할 것

> **⚠️ "도구 vs 운영자 성과 귀속"의 전용 경제학 문헌은 조사하지 못했다** (기술 지대의 귀속, 자본-노동 간 잉여 배분에 관한 노동경제학). WebSearch 예산 소진으로 **독립 탐색 자체가 수행되지 않았다.**
> **§9-5-5와 `papers2_B_measurement.md` §3-6은 B-4·B-5 문헌을 귀속 관점으로 재프레이밍한 것이지 원조사가 아니다.** 책에서 이 영역을 다룰 때는 **"이 질문에 대한 전용 문헌을 우리는 찾지 못했다"** 로 정직하게 쓰거나, 3차 조사를 돌려야 한다.

## 10-6. §4 논쟁점 추가 — 「기준선 선택」

> §4(논쟁점·상충 관점)에 다음을 **4-10**으로 추가한다.

### 4-10. AX 성과를 무엇과 비교할 것인가 — 기준선 논쟁

| 관점 A: 증강 기준선 (인간 단독 대비) | 관점 B: 시너지 기준선 (AI 단독 대비) |
|---|---|
| **g = +0.64** — 담당자가 훨씬 잘하게 됐다 | **g = −0.23** — 그 사람을 뺐으면 더 나았다 |
| 대부분의 기업 AX 보고서가 **이것을 측정한다** | 대부분의 기업 AX 보고서가 **이것을 주장한다** |
| ❌ 출판편향 검정 **미통과** | ✅ 출판편향 검정 **통과** |
| 인간의 기여를 과대평가할 수 있다 | 인간을 빼는 결정으로 오독될 수 있다 |

**갈리는 이유:** 같은 데이터에서 **기준선만 다르다.** 그리고 **AI가 인간보다 나은 구간에서 두 지표는 정반대로 움직인다**(증강 +0.74 / 시너지 −0.54).

> **이 책의 결론으로 삼을 만한 것:** **AX 체계 구축의 첫 번째 설계 결정은 기술 선택이 아니라 `기준선 선택`이다.** 그리고 이 선택은 중립적이지 않다 — **기준선을 고르는 순간 "사람을 어디에 둘 것인가"가 이미 결정된다.** 축 5(측정)와 축 4(변화관리)가 여기서 만난다.
> **⚠️ 단, 이 논쟁을 "그러니 사람을 빼라"로 읽히게 쓰면 안 된다.** Hemmer의 조건(§10-5-다)이 답이다 — **AI가 접근 못 하는 정보를 인간이 쥔 공정에만 인간을 넣어라.** 그것이 없으면 인간은 잡음원이고, 있으면 팀이 AI 단독을 이긴다.

## 10-7. 커버리지 지도 보강 — 이 책의 학술적 기여 지점

> §축별 커버리지에 다음을 명시한다.

**★ 자율성 등급 계보의 단절 (직접 확인, 2026-09-05):**
> arXiv API에서 `Sheridan` + `levels of automation` + `large language model`을 **모두 포함하는 논문은 0건**이다. 고전 계보를 명시적으로 잇는 LLM 에이전트 논문은 **2건뿐**(Zheng et al. 2026 → Sheridan 직접 인용 / Engin & Hand 2026 → Parasuraman 직접 인용). **GAL·Data Agents 등 나머지는 SAE만 인용한다.**
>
> **그리고 SAE는 1차원이고, 1978~2000년 계보는 2차원이다.**
> **→ 이 단절을 지적하고 다리를 놓는 것이 이 책의 실질적 학술 기여가 될 수 있다.** (§9-3-3)

**★ "중간 자율성 등급이 가장 위험하다" — 실증 6갈래 수렴:**
> 테스트트랙 실험 · 129편 메타분석 · 시뮬레이터 · 전문가 인터뷰 · 결함조사 · 사고조사가 각자 **"중간 등급을 안전하게 만드는 조건"** 을 도출했더니, 그 조건들이 하나같이 **중간 등급의 편익을 상쇄하거나 소멸시킨다**는 데로 수렴했다.
> **→ 중간 등급이 나쁜 게 아니라, 중간 등급을 안전하게 만들면 그것은 더 이상 중간 등급이 아니다.** 그리고 이것은 1차의 **Skitka(1999) 자동화 편향**과 **완전히 다른 경로로 같은 결론**에 도달한다. **카드 3(통제 강도 설계)과 직결된다.** (§9-3-4)

---

# 【최종】 Phase 1 산출물 목록

| 파일 | 행 | 내용 |
|---|---|---|
| **`01_reference.md`** | **2,500+** | 합성 결과 (§1~8 1차 / §9 2차 보강 / **§10 저술 규율 원장**) |
| `research/web.md` | 948 | 1차 웹 — 축 1~4 |
| `research/web2.md` | 1,129 | 2차 웹 — BNY·Workday·라이선스·자율성 등급·폐기 반례·등록 스키마·축 5·축 3 |
| `research/papers.md` | 903 | 1차 학술 — 축 1~4 |
| `research/papers2_A_autonomy.md` | 1,356 | 2차 학술 A — **자율성 등급 계보 (완결)** |
| `research/papers2_B_measurement.md` | 2,729 | 2차 학술 B — 측정·FTE·성과 귀속 (**B-1~B-3 정제 / B-4·B-5 원자료**) |
| `research/papers2_C_orgtheory.md` | 1,057 | 2차 학술 C — **조직 이론 (양손잡이·사용자 혁신·흡수역량·아이디어 선별·enabling formalization)** |
| `research/community.md` | 1,118 | 1차 커뮤니티 — 축 1~4 |
| `research/community2.md` | 1,527 | 2차 커뮤니티 — 축 5·자율성 등급·폐기·축 3 |

> **전부 보존 산출물이다. 삭제 금지.** `papers2.md`라는 통합 파일은 만들지 않았다 — B계열 전문이 이미 `papers2_B_measurement.md`(2,729행)에 들어 있어 **중복이기 때문이다.**
