# 학술 리서치 2차 보강 — 섹션 A: 자율성 등급 프레임의 학술 계보

> **상태: 완결.** A-1(LOA 고전) · A-2(LLM 에이전트 최신 등급) · A-3(자율주행 등급 유비와 그 한계) 전부 조사·정리 완료. 섹션별 커버리지와 미확인 항목은 문서 말미 「A 커버리지」에 정리돼 있다.
> **짝 문서:** 섹션 B는 `papers2_B_measurement.md`, 섹션 C는 `papers2_C_orgtheory.md`.


검색 시점: **2026-09-05**

> **이 문서의 위치.** 1차 리서치(`research/papers.md`)를 대체하지 않는다. 1차에서 비어 있던 세 영역 — (A) 자율성 등급 프레임의 학술 계보, (B) 축 5 측정·FTE·성과 귀속, (C) 축 3 "중앙이 무엇을 공급하는가" — 만 판다. 1차에서 확보한 문헌은 재조사하지 않았다.
>
> **표기 규약.** `[PR]` 동료심사 / `[PP]` 프리프린트 단독 / `[WP]` 워킹페이퍼·기관 보고서·표준 문서 / `[BK]` 단행본.
>
> **인용 규율.** 아래 모든 항목은 2026-09-05 기준으로 검색·원문 대조를 실제로 수행한 것이다. 수치는 원문 그대로이며 반올림하지 않았다. 확인하지 못한 것은 삭제하지 않고 `⚠️ 미확인`으로 남겼고, **F절에 전부 모아 두었다. 저술 전 F절을 반드시 읽어라.**
>
> **원문 텍스트 보관 위치.** 이번 조사에서 확보한 원문 추출 텍스트(J3016 전문, Bainbridge, Victor, NTSB 2건, NHTSA, Adler & Borys OCR, Kellogg, Acemoglu & Restrepo 등)는 세션 스크래치패드에 남아 있다. 인용 최종 대조가 필요하면 F절 말미의 파일 목록을 참조하라.

---

# A. 자율성 등급 프레임의 학술 계보

> **결론부터.** 이 책의 핵심 장치인 "에이전트 자율성 등급"은 **1978년부터 이어지는 두터운 학술 계보** 위에 있다. 계보는 세 갈래다.
> 1. **고전 자동화 등급** — Sheridan & Verplank (1978) → Parasuraman, Sheridan & Wickens (2000) → Endsley & Kaber (1999)
> 2. **자율주행 등급** — SAE J3016 (2021)
> 3. **군사·인권법 계보** — human in/on/out-of-the-loop 삼분법 (HRW 2012)
>
> 그리고 **2024~2026년 LLM 에이전트 문헌은 대부분 (2)만 베끼고 (1)을 참조하지 않는다.** 이 단절 자체가 이 책이 메울 수 있는 실질적 빈칸이다(A-2 §계보 단절 참조).

---

## A-1. LOA 고전 — 이 계보의 뿌리

### A-1-1. Sheridan & Verplank (1978) — 10단계 자동화 수준의 원전

**서지**
> Thomas B. Sheridan & William L. Verplank. *Human and Computer Control of Undersea Teleoperators.* Technical Report, Massachusetts Institute of Technology, **Man-Machine Systems Laboratory**, **1978-07-15**.
> DTIC DOI: **10.21236/ada057655** (DTIC 문서번호 ADA057655) · ONR Technical Report NR 196-152
> 피인용 **1,191회** (OpenAlex, 2026-09-05 확인) · **[WP]**

> ⚠️ **태그에 주의.** 이것은 **MIT 기술보고서이며 동료심사 학술지 논문이 아니다.** "1978년 논문"으로 쓰면 부정확하다. "MIT 기술보고서"로 표기하라.

**핵심 주장.** 인간 감독 제어(human supervisory control)의 정도를 **완전 수동에서 완전 자율까지 10단계 연속체**로 배열했다. 현대 "levels of automation" 논의 전체의 원점이다.

**★ 10단계 표 (VERBATIM)**

| | # | 원문 (verbatim) | 한국어 역 |
|---|---|---|---|
| **Low** | 1 | "The computer offers no assistance, human must take all decisions and actions" | 컴퓨터는 아무 도움도 주지 않는다. 인간이 모든 결정과 행동을 해야 한다 |
| | 2 | "The computer offers a complete set of decision/action alternatives, or" | 컴퓨터가 결정·행동 대안의 **완전한 집합**을 제시하거나 |
| | 3 | "Narrows the selection down to a few, or" | 선택지를 **소수로 좁히거나** |
| | 4 | "Suggests one alternative, and" | **하나의 대안을 제안하고** |
| | 5 | "Executes that suggestion if the human approves, or" | 인간이 승인하면 그 제안을 **실행하거나** |
| | 6 | "Allows the human a restricted veto time before automatic execution" | 자동 실행 전 인간에게 **제한된 거부 시간**을 허용하거나 |
| | 7 | "Executes automatically, then necessarily informs the human, and" | **자동 실행한 뒤 반드시 인간에게 통보**하고 |
| | 8 | "Informs the human only if asked, or" | **요청받을 때만** 인간에게 알리거나 |
| | 9 | "Informs the human only if it, the computer, decides to" | **컴퓨터가 알리기로 결정할 때만** 알리거나 |
| **High** | 10 | "The computer decides everything, acts autonomously, ignores the human" | 컴퓨터가 **모든 것을 결정하고 자율적으로 행동하며 인간을 무시한다** |

> ⚠️ **출처 경로를 정확히 밝혀라.** 위 표는 **1978년 원 보고서에서 직접 확인한 것이 아니다.** 동료심사 학회 논문에 재수록된 판본에서 verbatim 확보했다:
> Save, L., & Feuerberg, B., "**Designing Human-Automation Interaction: a new level of Automation Taxonomy**," *Proceedings of Human Factors of Systems and Technology 2012* (HFES Europe Chapter), **Table 1 (p. 44)**, 표제 "Levels of automation of Decision and Action Selection (Sheridan & Verplanck, 1978)". `[PR]`
> 원 보고서(DTIC ADA057655) 자체는 이번 조사에서 확보하지 못했다.
> ※ 이 재수록본은 저자명을 **"Verplanck"**로 잘못 표기한다. **정확한 철자는 Verplank**다(DTIC·OpenAlex 확인).
>
> 교차 확인: NASA/TM-2006-214504 (Kaber & Prinzel 2006) **Table 1**에도 동일 계열의 10단계가 "Sheridan(1987)의 10단계"로 실려 있다 — "1. The computer offers no assistance; the human must do it all … 10. The computer decides everything and acts autonomously, ignoring the human." **연도 귀속이 1978 / 1987로 갈리므로 인용 시 어느 판본인지 밝혀라.**

**이 책에 쓸 수 있는 부분 — 매우 크다.**
1. **등급 2~4가 "선택지의 폭"으로만 갈린다는 점이 결정적이다.** 완전한 집합 제시(2) → 소수로 좁힘(3) → 하나만 제안(4). 이 세 단계는 **행동 권한이 아니라 "인간에게 남겨진 선택지의 수"로 등급을 가른다.** 오늘날 대부분의 AX 등급표가 놓치는 축이다. LLM 에이전트로 옮기면 "후보 3개를 주는 에이전트"와 "정답 하나를 주는 에이전트"는 **다른 자율성 등급**이다 — 실행 권한이 똑같더라도.
2. **등급 6 "제한된 거부 시간(restricted veto time)"이 1978년에 이미 있었다.** 이것이 오늘날 "N초 안에 취소하지 않으면 실행" 패턴의 원형이다. 그리고 A-3의 인계 시간 실증 전체가 바로 이 등급을 겨눈다.
3. **등급 7~9가 "통보 정책"만으로 갈린다.** 반드시 알림(7) / 물으면 알림(8) / 알릴지를 기계가 결정(9). **관측가능성(observability)이 자율성의 독립 축**이라는 발상이 원전에 이미 있었다. Cihon et al.(2025)이 40여 년 뒤 재발견한 것과 같다(A-2 §6).

**인용 가능한 문장.** 위 10단계 각 문구가 그대로 인용 재료다. 특히 등급 1과 10의 대구가 강하다.

**한계·반박**
- 해저 원격조작기(undersea teleoperator)라는 매우 특수한 도메인의 기술보고서다.
- **단일 축 척도**다. Parasuraman et al.(2000)이 이 한계를 정면으로 지적하고 4단계로 쪼갠다.
- 등급 2~4와 7~9가 사실상 서로 다른 두 종류의 축(선택지 폭 / 통보 정책)을 하나의 사다리에 억지로 얹었다는 비판이 가능하다. **이 책이 그 지적을 하면 기여가 된다.**

---

### A-1-2. ★ Parasuraman, Sheridan & Wickens (2000) — 네 단계 정보처리 × 등급

**이 책의 자율성 등급 장치에 가장 직접적으로 이식되는 문헌이다.**

**서지**
> R. Parasuraman, T. B. Sheridan, & C. D. Wickens. "**A model for types and levels of human interaction with automation**." *IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans*, **30(3), 286–297**, **2000년 5월**.
> DOI: **10.1109/3468.844354** · PMID **11760769** · DBLP `journals/tsmc/ParasuramanSW00`
> 제1저자 소속: Cognitive Science Laboratory, The Catholic University of America, Washington, DC
> 피인용 **4,253회** (Semantic Scholar, 2026-09-05 확인) · **[PR]**

**★ 초록 전문 (VERBATIM, PubMed 수록 공식 초록)**
> "Technical developments in computer hardware and software now make it possible to introduce automation into virtually all aspects of human-machine systems. Given these technical capabilities, **which system functions should be automated and to what extent?** We outline a model for types and levels of automation that provides a framework and an objective basis for making such choices. **Appropriate selection is important because automation does not merely supplant but changes human activity and can impose new coordination demands on the human operator.** We propose that **automation can be applied to four broad classes of functions: 1) information acquisition; 2) information analysis; 3) decision and action selection; and 4) action implementation. Within each of these types, automation can be applied across a continuum of levels from low to high, i.e., from fully manual to fully automatic. A particular system can involve automation of all four types at different levels.** The human performance consequences of particular types and levels of automation constitute primary evaluative criteria for automation design using our model. **Secondary evaluative criteria include automation reliability and the costs of decision/action consequences**, among others."

**★ 네 단계 명칭 (VERBATIM) 및 등급 적용 방식**

| # | 원문 명칭 | 한국어 역 | AX 대응 |
|---|---|---|---|
| 1 | **Information acquisition** | 정보 획득 | 무엇을 수집·감지·조회하는가 |
| 2 | **Information analysis** | 정보 분석 | 수집된 것을 어떻게 통합·해석·예측하는가 |
| 3 | **Decision and action selection** | 의사결정 및 행동 선택 | 어떤 조치를 택할 것인가 |
| 4 | **Action implementation** | 행동 실행 | 그 조치를 실제로 집행하는가 |

**등급 적용 방식 — 이 논문의 결정적 통찰.**
Save & Feuerberg(2012)가 이 관계를 정확히 요약한다 (VERBATIM):
> "A second decisive step was made by Parasuraman, Sheridan, and Wickens (2000) who acknowledged the Sheridan-Verplanck 10-point scale and **introduced the idea of associating levels of automation to functions.** These functions are based on a four-stage model of human information processing and can be translated into equivalent system functions: (1) information acquisition, (2) information analysis, (3) decision and action selection and (4) action implementation."

즉 **Sheridan의 10단계 척도를 버리지 않고, 그것을 네 기능 각각에 독립적으로 적용한다.** 원 논문 초록의 표현이 정본이다 — **"A particular system can involve automation of all four types at different levels."** (한 시스템이 네 유형 전부를 서로 다른 수준으로 자동화할 수 있다.)

**이 책에 쓸 수 있는 부분 — A절에서 가장 중요한 항목이다.**

1. **"자율도 3단계"라는 단일 값을 쓰지 말라는 처방의 정본 근거다.** SAE J3016은 기능 하나에 **단일 등급**을 붙이지만, Parasuraman 모형은 네 기능을 **각각 독립적으로** 배분한다. AX 등급표를 최소 **(관찰 · 분석 · 의사결정 · 실행)** 4칸으로 쪼개라는 실무 처방이 여기서 바로 도출된다.

2. **★ 이 틀로 "중간 등급"을 해부하면 그 기이함이 드러난다.** SAE L3는 정보획득·분석·결정·실행을 **모두 높은 수준으로 자동화해 놓고, "실패했을 때의 결정과 실행"만 인간에게 남긴다.** 즉 **인간이 앞의 세 단계에 전혀 참여하지 않은 상태에서 네 번째 단계만 맡는 구조**다. Parasuraman·Endsley·Bainbridge가 각자의 언어로 불가능하다고 말한 바로 그 배분이다. → **A-3의 논증과 여기서 만난다.**

3. **"자동화는 대체가 아니라 변형"이라는 명제.** 초록의 이 문장이 AX ROI 계산의 구조적 결함을 정확히 지적한다:
   > "**automation does not merely supplant but changes human activity and can impose new coordination demands on the human operator.**"
   > (자동화는 단순히 대체하는 것이 아니라 인간 활동을 **변화시키며**, 인간 운영자에게 **새로운 조율 부담을 부과**할 수 있다.)
   → AX 도입 효과를 "사람이 하던 일의 뺄셈"으로 계산하면 **새로 생겨나는 조율 비용**이 회계에서 통째로 빠진다. 이 문장은 이 책의 측정 챕터(B절)와도 직결된다.

4. **"부차적 평가 기준"에 자동화 신뢰도와 결과의 비용이 들어간다는 점.** 초록 마지막 문장이 **가역성·결과 심각도**를 등급 선택의 기준으로 이미 지목하고 있다 — 2026년 ExxonMobil 팀이 재발견한 것과 같다(A-2 §1-3).

**인용 가능한 문장·수치.** 위 초록 전문 전체, 특히 굵게 표시한 세 구절.

**한계·반박**
- **이론·프레임워크 논문이다.** 원저 실증 데이터가 없다. 저자들 스스로 "framework and an objective basis"를 제공한다고만 쓴다. "Parasuraman이 실험으로 증명했다"고 쓰면 오류다.
- "objective basis"라는 표현에도 불구하고, 실제 등급 선택은 **인간 성능 결과에 대한 평가 판단**에 의존하며 자동으로 산출되지 않는다.
- **2000년 논문이다.** ML 기반 자율성(불투명·확률적·분포 이동)은 다루지 않는다. 다만 4단계 분해라는 구조적 통찰은 오히려 LLM 에이전트에서 더 유효해진다.
- ⚠️ 권·호·페이지는 확인했으나(30(3), 286–297), 논문 내부 Table의 10단계 문구 자체는 원문에서 직접 확인하지 못했다 — Save & Feuerberg 재수록본 경유다.

---

### A-1-3. Parasuraman & Riley (1997) — 오용·미사용·남용

**서지**
> Raja Parasuraman & Victor Riley. "**Humans and Automation: Use, Misuse, Disuse, Abuse**." *Human Factors: The Journal of the Human Factors and Ergonomics Society*, **39(2), 230–253**, **1997년 6월**.
> DOI: **10.1518/001872097778543886** · **[PR]**

**핵심 주장.** 인간-자동화 관계의 실패를 세 유형으로 구분한다 — **misuse**(자동화에 대한 과의존), **disuse**(정당한 자동화를 쓰지 않음), **abuse**(인간의 능력·결과를 고려하지 않은 설계자·관리자의 자동화 적용).

**이 책에 쓸 수 있는 부분.**
- 이 삼분법은 AX 실패 분류에 그대로 이식된다. 특히 **abuse의 정의가 "사용자가 아니라 설계자·관리자의 잘못"을 지목한다**는 점이 중요하다. AX 도입 실패를 "직원이 안 쓴다"(disuse)로만 진단하는 조직에, "그건 abuse일 수 있다"는 세 번째 선택지를 준다.
- 1차에서 확보한 Skitka(1999) 자동화 편향, 그리고 A-3의 Victor et al.(2018)과 **misuse 축에서 정확히 만난다.**

**한계·반박**
- ⚠️ **이번 조사에서 서지(권·호·페이지·DOI)는 확인했으나 원문 초록·본문은 확보하지 못했다.** 위 삼분법 요약은 통상적 정리이며 **verbatim 인용이 아니다.** 따옴표 인용을 하려면 원문 대조가 필요하다. → F절.

---

### A-1-4. Endsley & Kiris (1995) — 루프 밖 성능 문제

**서지**
> Mica R. Endsley & Esin O. Kiris. "**The Out-of-the-Loop Performance Problem and Level of Control in Automation**." *Human Factors*, **37(2), 381–394**, **1995년 6월**.
> DOI: **10.1518/001872095779064555** · **[PR]**

**★ 초록 전문 (VERBATIM — SAGE 공식 페이지에서 확보)**
> "**The out-of-the-loop performance problem, a major potential consequence of automation, leaves operators of automated systems handicapped in their ability to take over manual operations in the event of automation failure.** This is attributed to a possible **loss of skills** and of **situation awareness (SA)** arising from **vigilance and complacency problems, a shift from active to passive information processing, and change in feedback provided to the operator.** We studied the automation of a navigation task using an expert system and demonstrated that **low SA corresponded with out-of-the-loop performance decrements in decision time following a failure of the expert system.** **Level of operator control in interacting with automation is a major factor in moderating this loss of SA.** Results indicated that **the shift from active to passive processing was most likely responsible for decreased SA under automated conditions.**"

**이 책에 쓸 수 있는 부분 — 그리고 반드시 정직하게 다뤄야 할 긴장.**

이 논문의 결론은 **"제어 수준이 SA 상실을 조절한다"**이며, Endsley 계열 연구는 여기서 **"중간 수준의 자동화가 완전 자동화보다 SA를 잘 보존한다"**는 처방을 이끌어낸다. **이는 이 책의 "중간 등급이 가장 위험하다"와 정면으로 부딪힐 수 있다. 반드시 정직하게 다뤄라.**

**정직한 해소는 이렇다 — "관여의 중간"과 "책임 배분의 중간"은 다르다.**
Endsley가 옹호하는 것은 **인간이 능동적으로 정보를 처리하도록 남겨두는 것**(= 결과적으로 인간이 옵션 생성·선택에 계속 참여하는 설계)이지, **"평소엔 손 떼고 있다가 호출되면 들어오는" 시간축상의 중간(L3) 구조가 아니다.** 오히려 L3는 Endsley가 지목한 **"능동적 처리에서 수동적 처리로의 전환"을 극대화한 뒤 인계 책임만 남긴** 형태다. 따라서 이 논문은 L3에 대한 근거가 아니라 **L3에 대한 반증**으로 읽는 것이 옳다.

> **AX 번역:** "사람을 루프에 넣는다"는 말은 **역할표(RACI)에 이름을 넣는 것이 아니라, 그 사람이 능동적으로 정보를 처리하게 만드는 것**을 뜻해야 한다. **승인 버튼만 누르는 자리는 수동적 처리이고, 수동적 처리는 SA를 보존하지 못한다.**

**한계·반박**
- 항법 과제 기반 **실험실 연구**이며 운전·조직 맥락이 아니다.
- ⚠️ **표본 크기·효과크기 등 본문 수치는 확인하지 못했다**(유료 장벽, 초록만 확보). 수치 인용 계획이 있으면 원문 대조 필요. → F절.
- 1995년 "전문가 시스템" 대상이며 현대 ML 자동화와 실패 양상이 다르다.

---

### A-1-5. ★ Endsley (2017) — "자동화 난제(automation conundrum)"

**이 한 문장이 이 책의 A절 주장을 그대로 압축한다.**

**서지**
> Mica R. Endsley. "**From Here to Autonomy: Lessons Learned From Human–Automation Research**." *Human Factors*, **59(1), 5–27**, **2017년 2월**.
> DOI: **10.1177/0018720816681350** · PMID **28146676** · **[PR]**

> ⚠️ **의뢰서 정정.** 의뢰서에는 게재지가 *Journal of Cognitive Engineering and Decision Making*으로 적혀 있었으나, **실제 게재지는 *Human Factors* 59권 1호, 5–27쪽**이다. Crossref·Europe PMC·PubMed **3중 확인**. 인용 시 반드시 수정하라.

**★ automation conundrum 진술 (VERBATIM, Europe PMC 수록 공식 초록)**
> "As autonomous and semiautonomous systems are developed for automotive, aviation, cyber, robotics and other applications, the ability of human operators to effectively oversee and interact with them when needed poses a significant challenge. **An automation conundrum exists in which as more autonomy is added to a system, and its reliability and robustness increase, the lower the situation awareness of human operators and the less likely that they will be able to take over manual control when needed.** The **human-autonomy systems oversight model** integrates several decades of relevant autonomy research on operator situation awareness, out-of-the-loop performance problems, monitoring, and trust, which are all major challenges underlying the automation conundrum. Key design interventions for improving human performance in interacting with autonomous systems are integrated in the model, including human-automation interface features and central automation interaction paradigms comprising **levels of automation, adaptive automation, and granularity of control** approaches."

> **한국어 역 (자동화 난제):** "시스템에 자율성이 더해지고 그 **신뢰성과 견고성이 높아질수록**, 인간 운영자의 상황인식은 **더 낮아지고**, 필요할 때 수동 제어를 인계받을 가능성은 **더 작아진다.**"

**이 책에 쓸 수 있는 부분 — A절 전체의 이론적 중심축.**

자동화 품질(신뢰성·견고성)과 인간 인계 능력이 **역상관**한다면, "자동화 품질은 높으면서 인간 인계에 의존하는" 지점 — 즉 **중간 등급 — 이 최대 위험 지점**이라는 결론이 논리적으로 따라온다. 낮은 등급은 자동화 품질이 낮아 인간이 계속 붙어 있고, 높은 등급은 인간 인계에 의존하지 않으므로, **양 끝은 난제를 회피하지만 중간만이 난제의 정확한 정점에 앉는다.**

> **책에서 쓸 수 있는 도식:** 세로축 "인계 실패 위험", 가로축 "자동화 등급" → **역U자(∩) 곡선의 꼭대기가 중간 등급.** 이 곡선의 **이론적 근거가 Endsley의 자동화 난제**이고, **실측 근거가 Merat(35–40초)·Zhang(꼬리 분산)·Victor(28%)·NHTSA(467건)**다(A-3).

> **★ AX 번역 (직관에 반하지만 중요).** 사내 AI 도구가 **잘 작동할수록** 검토자의 실질적 검토 강도는 떨어진다. 따라서 **"정확도 95%짜리 AI + 사람 검토"는 "정확도 70%짜리 AI + 사람 검토"보다 오히려 위험할 수 있다.** 남은 5%가 검토를 통과할 확률이 훨씬 높기 때문이다. 이것은 1차에서 확보한 Skitka(1999)의 자동화 편향("거의 항상 맞는 시스템이 가장 위험")과 **같은 결론에 다른 경로로 도달한다.**

**한계·반박**
- **리뷰/이론 논문이다** (원저 실험이 아님). "Endsley가 실험으로 보였다"고 쓰면 오류다.
- 자동차·항공·사이버·로보틱스를 함께 다루는 범도메인 종합이며, 인용된 개별 연구의 강도는 도메인마다 다르다.
- ⚠️ **결정적 유보:** Endsley 자신은 이 난제에 대해 **"자동화를 줄이자"가 아니라 "인터페이스·적응형 자동화·제어 입자도(granularity of control)로 완화하자"**는 처방을 제시한다. 즉 **"중간 등급을 건너뛰자"는 결론을 저자가 직접 내리지는 않는다.** 이 논문을 그 근거로 쓸 때는 **"저자의 결론이 아니라 저자의 전제로부터 도출한 것"**임을 밝히는 편이 정직하다.

---

### A-1-6. ★ Endsley & Kaber (1999) — 10단계 × 4기능 배분표

**SAE보다 훨씬 나은 등급 모델이 이미 1999년에 있었다.**

**서지**
> Mica R. Endsley & David B. Kaber. "**Level of automation effects on performance, situation awareness and workload in a dynamic control task**." *Ergonomics*, **42(3), 462–492**, **1999-03-01**.
> DOI: **10.1080/001401399185595** · **[PR]**

**★ 초록 (VERBATIM, Taylor & Francis 공식 페이지)**
> "Various levels of automation (LOA) designating the degree of human operator and computer control were explored within the context of a dynamic control task as a means of improving overall human/machine performance. **Automated systems have traditionally been explored as binary function allocations; either the human or the machine is assigned to a given task. More recently, intermediary levels of automation have been discussed as a means of maintaining operator involvement in system performance, leading to improvements in situation awareness and reductions in out-of-the-loop performance problems.** A LOA taxonomy applicable to a wide range of psychomotor and cognitive tasks is presented here... The functions allocated to a human operator and/or computer included *monitoring* displays, *generating* processing options, *selecting* an 'optimal' option and *implementing* that option... **Thirty subjects** performed simulation trials involving various levels of automation. Several automation failures occurred and out-of-the-loop performance decrements were assessed. **Results suggest that, in terms of performance, human operators benefit most from automation of the implementation portion of the task, but only under normal operating conditions; in contrast, removal of the operator from task implementation is detrimental to performance recovery if the automated system fails. Joint human/system option generation significantly degraded performance in comparison to human or automated option generation alone.** Lower operator workload and higher situation awareness were observed under automation of the decision making portion of the task (i.e. selection of options), although human/system performance was only slightly improved."

**★ 10단계 × 4기능 배분표 (VERBATIM)**

출처: Kaber, D. B., & Prinzel, L. J. III (2006), *Adaptive and Adaptable Automation Design*, **NASA/TM-2006-214504**, September 2006, **Table 2** ("Endsley and Kaber's (1999) Levels of Automation Taxonomy"). `[WP]`

| # | 자동화 수준 | MONITORING | GENERATING | SELECTING | IMPLEMENTING |
|---|---|---|---|---|---|
| 1 | Manual Control | Human | Human | Human | Human |
| 2 | Action Support | Human/Computer | Human | Human | Human/Computer |
| 3 | Batch Processing | Human/Computer | Human | Human | Computer |
| 4 | Shared Control | Human/Computer | Human/Computer | Human | Human/Computer |
| 5 | Decision Support | Human/Computer | Human/Computer | Human | Computer |
| 6 | Blended Decision Making | Human/Computer | Human/Computer | Human/Computer | Computer |
| 7 | Rigid System | Human/Computer | Computer | Human | Computer |
| 8 | Automated Decision Making | Human/Computer | Human/Computer | Computer | Computer |
| 9 | Supervisory Control | Human/Computer | Computer | Computer | Computer |
| 10 | Full Automation | Computer | Computer | Computer | Computer |

**이 책에 쓸 수 있는 부분 — AX 등급 설계의 직접적 템플릿.**

1. **이 표가 그대로 템플릿이다.** SAE J3016은 등급을 **하나의 축**(누가 DDT를 하는가)으로 눌러 담았지만, Endsley & Kaber는 **4개 기능(감시·옵션생성·선택·실행)을 독립적으로 배분**한다. 그래서 "실행은 컴퓨터, 선택은 인간"(#5 Decision Support) 같은 조합이 표현된다. **Parasuraman et al.(2000)의 4단계와 짝을 이루며, 이쪽은 실제 배분표까지 제공한다.**

2. **★ "정상 시 최적 = 실패 시 최악"의 실험적 증거.**
   > "human operators benefit most from automation of the **implementation** portion of the task, **but only under normal operating conditions**; in contrast, **removal of the operator from task implementation is detrimental to performance recovery if the automated system fails.**"
   → 실행을 자동화하면 평상시 성능은 가장 좋아지지만, **실패했을 때 회복 성능은 오히려 나빠진다.** 이 트레이드오프가 등급 설계의 핵심 딜레마다.

3. **★ "어설픈 협업이 명확한 단독 배분보다 나쁘다"는 직접 증거.**
   > "**Joint human/system option generation significantly degraded performance in comparison to human or automated option generation alone.**"
   → **인간과 시스템이 옵션을 공동 생성하는 것이, 인간 단독이나 자동 단독보다 성능을 유의하게 악화시켰다.** "중간 등급이 가장 위험하다"의 또 다른 실증 축이며, **"AI와 사람이 함께 후보를 낸다"는 배분이 실증적으로 가장 나쁜 조합이었다**는 경고로 그대로 쓸 수 있다.

> **AX 번역:** AX 등급표를 만들 때 "AI 자율도 1~5단계" 같은 단일 축을 쓰지 말고, **최소한 (관찰·후보생성·선택·실행) 4축으로 쪼개서 각각 배분하라.** 그리고 **"AI와 사람이 함께 후보를 낸다"는 배분은 실증적으로 가장 나쁜 조합**이었음을 기억하라.

**한계·반박**
- 참가자 **30명**의 실험실 시뮬레이션(동적 제어 과제). 운전·조직 의사결정으로의 외적 타당성은 별도 논증이 필요하다.
- ⚠️ **이 논문은 오히려 "중간 수준 자동화가 SA를 보존한다"는 방향을 지지한다**(초록: "intermediary levels of automation... leading to improvements in situation awareness"). **책의 주장과 긴장 관계에 있다.** 정직한 해소는 A-1-4와 같다 — Endsley·Kaber의 "중간 수준"은 **인간이 선택·생성에 계속 참여하는 관여의 중간**이지, **"평소 이탈 + 유사시 복귀"라는 시간축상의 중간이 아니다.** 오히려 이 논문의 "실행 자동화 → 실패 시 회복 저하" 결과는 중간 등급에 대한 반증이다. **이 구분을 책에서 명시적으로 다루면 논증이 훨씬 단단해진다.**
- ⚠️ 10단계 분류표는 **NASA 기술보고서에 재수록된 판본**으로 확인했다. 원 논문(Ergonomics 42(3)) 원표와의 자구 대조는 하지 않았다. 원표에는 각 수준의 서술적 정의가 함께 실려 있을 가능성이 높다. → F절.

---

### A-1-7. ★★ Bainbridge (1983) — 자동화의 아이러니

**43년 전에 이미 다 쓰여 있었다. 이 책의 A절에서 가장 인용가치가 높은 단일 문헌이다.**

**서지**
> Lisanne Bainbridge. "**Ironies of Automation**." *Automatica*, **19(6), 775–779**, **1983**.
> DOI: **10.1016/0005-1098(83)90046-8** · Pergamon Press Ltd. / © 1983 IFAC · Brief Paper
> 접수 1982-12-16, 개정 1983-05-23. 최초 발표: IFAC/IFIP/IFORS/IEA Conference on Analysis, Design, and Evaluation of Man-Machine Systems, Baden-Baden, F.R.G., **1982년 9월**
> 저자 소속: Department of Psychology, University College London · **[PR]**

**초록 (VERBATIM)**
> "This paper discusses the ways in which **automation of industrial processes may expand rather than eliminate problems with the human operator**. Some comments will be made on methods of alleviating these problems within the 'classic' approach of leaving the operator with responsibility for abnormal conditions, and on the potential for continued use of the human operator for on-line decision-making within human-computer collaboration."

**★ 인용 가능한 문장 — 전부 VERBATIM (원문 5쪽 PDF에서 추출)**

**(1) 설계자가 자동화하지 못한 것만 사람에게 남는다**
> "**The second irony is that the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate.** It is this approach which causes the problems to be discussed here, as it means that **the operator can be left with an arbitrary collection of tasks, and little thought may have been given to providing support for them.**"
> (두 번째 아이러니는, 운영자를 제거하려 한 설계자가 결국 **자신이 자동화할 방법을 떠올리지 못한 과업들을** 그 사람에게 남긴다는 것이다. 그 결과 운영자에게는 **임의로 그러모은 과업 뭉치**가 남겨지고, 그것을 지원할 방법은 거의 고려되지 않는다.)

**(2) 인간은 감시에 부적합하다**
> "**We know from many 'vigilance' studies (Mackworth, 1950) that it is impossible for even a highly motivated human being to maintain effective visual attention towards a source of information on which very little happens, for more than about half an hour. This means that it is humanly impossible to carry out the basic function of monitoring for unlikely abnormalities**, which therefore has to be done by an automatic alarm system connected to sound signals."
> (수많은 '경계(vigilance)' 연구로부터 우리는, **아무리 동기가 높은 인간이라도 거의 아무 일도 일어나지 않는 정보원에 대해 30분 남짓을 넘겨 효과적인 시각적 주의를 유지하는 것은 불가능하다**는 것을 안다. 이는 **일어날 법하지 않은 이상을 감시한다는 기본 기능을 수행하는 것이 인간에게는 불가능하다**는 뜻이다.)

**(3) 감시 아이러니의 정면 진술**
> "**A more serious irony is that the automatic control system has been put in because it can do the job better than the operator, but yet the operator is being asked to monitor that it is working effectively.**"
> (더 심각한 아이러니는, 자동 제어 시스템이 **운영자보다 그 일을 더 잘하기 때문에** 도입되었는데도, 정작 그 운영자에게 **그것이 제대로 작동하는지 감시하라고 요구한다**는 것이다.)

**(4) ★ 실시간 검증 불가능성 → "불가능한 과업"**
> "The second problem is that **if the decisions can be fully specified then a computer can make them more quickly, taking into account more dimensions and using more accurately specified criteria than a human operator can. There is therefore no way in which the human operator can check in real-time that the computer is following its rules correctly.** One can therefore only expect the operator to monitor the computer's decisions at some meta-level, to decide whether the computer's decisions are 'acceptable'. **If the computer is being used to make the decisions because human judgement and intuitive reasoning are not adequate in this context, then which of the decisions is to be accepted? The human monitor has been given an impossible task.**"
> (…**인간 감시자에게는 불가능한 과업이 주어진 것이다.**)
> → **LLM 시대에 오히려 더 강해지는 논증이다.**

**(5) 기술 퇴화 — 감시하는 동안 숙련이 사라진다**
> "Unfortunately, **physical skills deteriorate when they are not used, particularly the refinements of gain and timing. This means that a formerly experienced operator who has been monitoring an automated process may now be an inexperienced one.** If he takes over he may set the process into oscillation."

**(6) ★★ 인계 순간의 역설 — "중간 등급이 가장 위험하다"의 원형 논증**
> "**When manual take-over is needed there is likely to be something wrong with the process, so that unusual actions will be needed to control it, and one can argue that the operator needs to be more rather than less skilled, and less rather than more loaded, than average.**"
> (수동 인계가 필요한 시점에는 프로세스에 무언가 잘못이 생겼을 가능성이 크고, 따라서 그것을 제어하려면 **평소와 다른 조치**가 필요하다. 그러므로 그 운영자는 평균보다 **덜 숙련된 것이 아니라 더 숙련되어야 하고, 더 부하가 걸린 것이 아니라 덜 걸려 있어야 한다**고 말할 수 있다.)

**(7) 맥락 구축에는 시간이 걸린다 — Merat의 35–40초와 직결**
> "Manual operators may come into the control room **quarter to half an hour before they are due to take over control**, so they can get this feel for what the process is doing. The implication of this for manual take-over from automatically controlled plant is that **the operator who has to do something quickly can only do so on the basis of minimum information**, he will not be able to make decisions based on wide knowledge of the plant state until he has had time to check and think about it."

**(8) 전체를 관통하는 명제**
> "This paper suggests that the increased interest in human factors among engineers reflects the irony that **the more advanced a control system is, so the more crucial may be the contribution of the human operator.**"

**(9) 표제 개념 정의 (논문 서두에 그대로 인쇄되어 있음)**
> "**Irony:** combination of circumstances, the result of which is the direct opposite of what might be expected."
> "**Paradox:** seemingly absurd though perhaps really well-founded statement."

**이 책에 쓸 수 있는 부분 — 결정적.**

**(6)번 인용이 "중간 등급이 가장 위험하다"의 원형 논증이다.** 인계가 필요한 순간은 정의상 **이상 상황**이고, 이상 상황은 평소보다 **더 높은 숙련과 더 낮은 부하**를 요구한다. 그런데 자동화는 정확히 그 두 가지를 **반대 방향으로** 만들어놓는다 — 감시만 하던 사람은 숙련이 퇴화했고((5)), 방금까지 다른 일을 하고 있었으므로 맥락이 없다((7)). **자동화 수준이 높을수록 이 격차가 커지고, 인간이 여전히 폴백을 맡고 있는 한 격차는 그대로 위험이 된다.**

> **★ AX 번역 (이 책 전체에서 가장 강한 논증 중 하나).** "AI가 초안을 쓰고 사람이 검토한다"는 체계를 오래 돌리면, **검토자의 판단력 자체가 퇴화한다.** 그리고 검토가 정말로 필요한 순간은 AI가 평소와 다르게 작동한 순간이며, 그때 요구되는 판단력은 평소보다 **높다.** 즉 **검토 역량이 가장 필요한 순간에 가장 낮아지도록 설계된 체계**다. 이것이 Bainbridge가 1983년에 프로세스 플랜트에 대해 쓴 것이고, 2026년의 AX 체계에 그대로 적용된다.

**한계·반박**
- **개념 논문(Brief Paper)이며 원저 실증 데이터가 없다.** 프로세스 산업·조종실 자동화 사례와 선행 연구의 종합이다. **"Bainbridge가 실험으로 증명했다"고 쓰면 오류다.**
- **"약 30분" 경계 수치는 Mackworth(1950)의 2차 인용이다.** 원 실험은 레이더 감시 과제(Clock Test)로 현대 맥락과 과제 구조가 다르다. **정밀한 수치보다 정성적 명제로 쓰는 편이 안전하다.**
- 1983년 시점의 규칙 기반 프로세스 제어를 대상으로 하며, 확률적·불투명한 현대 ML 시스템에 대한 논의는 없다. 다만 (4)번 인용은 오히려 LLM 시대에 강해진다.
- ⚠️ 확보한 PDF가 OCR 산출물이라 명백한 판독 오류("h u m a n", "corrcct" 등)가 섞여 있었다. **의미와 문장 구조는 신뢰할 만하지만, 최종 게재 전 정본(Automatica 원본 또는 Elsevier 판) 대조를 권한다.** 특히 구두점·이탤릭. → F절.

---

### A-1 정리 — 등급 프레임 비교표

| 프레임 | 연도 | 등급 수 | 축의 구조 | 등급별로 달라지는 것 | 태그 |
|---|---|---|---|---|---|
| **Sheridan & Verplank** | 1978 | **10** | 단일 축 (의사결정·행동 선택) | 선택지의 폭(2–4) → 거부권(5–6) → 통보 정책(7–9) | [WP] |
| **Parasuraman, Sheridan & Wickens** | 2000 | 10 × **4기능** | **2차원** (기능 × 수준) | 네 정보처리 단계마다 독립적으로 수준 지정 | [PR] |
| **Endsley & Kaber** | 1999 | **10** × 4기능 배분 | 2차원 (배분표) | 감시·생성·선택·실행 각각을 인간/컴퓨터/공동으로 배분 | [PR] |
| **SAE J3016** | 2021 | **6** (L0–L5) | 단일 축 (DDT·폴백·ODD) | 누가 운동제어·OEDR·폴백을 하는가, ODD 제한 유무 | [WP] |

> **이 표에서 읽어야 할 것.** 가장 정교한 프레임(Parasuraman, Endsley & Kaber)은 **2차원**이고, 가장 널리 베껴지는 프레임(SAE)은 **1차원**이다. 그리고 2024~2026년 LLM 에이전트 문헌은 거의 전부 SAE를 베낀다(A-2). **이 책이 2차원 프레임으로 돌아가면 그것만으로 차별화된다.**

---
## A-2. LLM 에이전트에 적용된 최신 자율성 등급 (2024~2026)

> **조사 결과 요약.** 실제 검색으로 확인된 등급 프레임이 **9건** 있다. 이 중 **동료심사를 통과한 것은 2건**(Morris et al. ICML 2024, Luo et al. SIGMOD 2026)뿐이고 나머지는 프리프린트·워크숍·연구소 에세이다. 그리고 **2026년 현재 가장 실무적으로 유용한 발견은 "능력과 허용 권한을 분리하라"(A-2-3)와 "자율성은 단일 척도가 아니라 다차원"(A-2-8~10)이다.**

---

### A-2-1. Morris et al. — "Levels of AGI"의 **자율성 6단계** `[PR]`

**서지**
> Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, Shane Legg. "**Levels of AGI for Operationalizing Progress on the Path to AGI**."
> arXiv:**2311.02462** — v1: **2023-11-04** / v2: 2024-01-05 / v3: 2024-05-22 / v4: 2024-06-05 / v5: **2025-09-24**
> 게재: **ICML 2024 (Proceedings)** · https://arxiv.org/abs/2311.02462 · CC BY-NC-ND 4.0 · **[PR]**

**핵심 주장.** AGI를 이분법이 아니라 **깊이(성능) × 넓이(일반성)의 행렬**로 등급화하자는 제안. 그런데 이 책에 결정적인 부분은 AGI 성능 표가 아니라 **§6.2 "Capabilities vs. Autonomy"에 따로 실린 자율성 표**다. 저자들의 논지: **능력 등급이 자율성 등급을 "해금(unlock)"할 뿐, 자율성 등급을 결정하지는 않는다.**

**★ 등급표 — Levels of Autonomy (6단계, §6.2)**

| # | 등급 명칭 (verbatim) | 한국어 역 | 예시 시스템 (verbatim) | **새로 도입되는 위험 (verbatim)** |
|---|---|---|---|---|
| 0 | **Autonomy Level 0: No AI** | 자율성 0단계: AI 없음 | "Analogue approaches (e.g., sketching with pencil on paper)" | n/a (status quo risks) |
| 1 | **Autonomy Level 1: AI as a Tool** | 1단계: **도구**로서의 AI | "Information-seeking with the aid of a search engine" | **de-skilling** (e.g., over-reliance) |
| 2 | **Autonomy Level 2: AI as a Consultant** | 2단계: **자문가**로서의 AI | "Relying on a language model to summarize a set of documents" | **over-trust** |
| 3 | **Autonomy Level 3: AI as a Collaborator** | 3단계: **협업자**로서의 AI | "Training as a chess player through interactions with and analysis of a chess-playing AI" | **anthropomorphization** (e.g., parasocial relationships) |
| 4 | **Autonomy Level 4: AI as an Expert** | 4단계: **전문가**로서의 AI | "Using an AI system to advance scientific discovery (e.g., protein-folding)" | **societal-scale ennui** |
| 5 | **Autonomy Level 5: AI as an Agent** | 5단계: **행위자**로서의 AI | "Autonomous AI-powered personal assistants (not yet unlocked)" | **misalignment** |

**참고 — Levels of AGI (성능 축, 6단계):** Level 0 No AI / 1 Emerging / 2 Competent / 3 Expert / 4 Virtuoso / 5 Superhuman. 각 등급은 **Narrow**와 **General** 두 축으로 이원 배치된다.

**★ 등급 간에 바뀌는 것.** 변하는 축은 딱 하나 — **인간이 AI에게 내주는 상호작용 역할**이다. 도구(내가 쓴다) → 자문가(의견을 듣는다) → 협업자(같이 한다) → 전문가(맡긴다) → 행위자(위임한다). 그리고 **각 단계마다 위험의 종류 자체가 바뀐다.** 1단계는 탈숙련, 2단계는 과신, 5단계는 정렬 실패. **위험이 "커지는" 게 아니라 종류가 갈아엎어지는 구조다.**

**★ 인용 가능한 문장 — 이 책 등급 장치의 철학적 정당화**
> "Higher levels of autonomy are '**unlocked**' by AGI capability progression, though **lower levels may be desirable for particular tasks and contexts.**"
> (더 높은 자율성 단계는 AGI 능력 진전에 의해 '해금'되지만, **특정 과업과 맥락에서는 오히려 낮은 단계가 바람직할 수 있다.**)

**이 책에 쓸 수 있는 부분.**
1. 위 한 문장이 **"우리 회사 모델이 5단계를 할 수 있다"와 "우리 회사가 이 업무를 5단계로 돌려야 한다"는 완전히 다른 명제**라는 것 — 실무 리더에게 가장 먼저 각인시켜야 할 구분이다.
2. **위험 열(column)이 등급마다 다르다**는 설계가 한국 기업이 흔히 만드는 "1~5단계로 갈수록 위험이 커진다" 식 단조 증가 표보다 훨씬 정교하다. 그대로 벤치마킹할 만하다.

**한계·반박**
- 자율성 표는 논문의 **부수적 기여**다(§6.2, 표 하나 분량). AGI 등급표만큼 정교하게 방어되어 있지 않다.
- "societal-scale ennui" 같은 위험 항목은 **경험적 근거가 없는 사변**이다. 인용 시 근거 수준을 함께 표기하라.
- 등급이 **조직 운영 단위가 아니라 개인의 상호작용 단위**로 정의돼 있어 기업 거버넌스에 바로 쓰기엔 결이 안 맞는다. 이 간극을 메우는 것이 A-2-3이다.

---

### A-2-2. Feng, McDonald & Zhang — 5단계, **사용자 역할** 기준 `[WP]`

**서지**
> K. J. Kevin Feng, David W. McDonald, Amy X. Zhang. "**Levels of Autonomy for AI Agents**."
> arXiv:**2506.12469** — v1: **2025-06-14** / v2: 2025-07-28 · cs.HC; cs.AI
> 게재: **Knight First Amendment Institute, "AI and Democratic Freedoms" 에세이 시리즈**
> https://arxiv.org/abs/2506.12469 · **[WP]** (동료심사 학회 논문이 아니라 연구소 에세이)

**핵심 주장.** **"자율성은 의도적인 설계 결정이며, 능력 및 운영 환경과 별개다."** 이 셋을 분리하지 않으면 "모델이 똑똑해졌으니 자율성도 올려야 한다"는 잘못된 추론에 빠진다.

**★ 등급표 (5단계 — 사용자가 취하는 역할로 정의)**

| # | 역할 (verbatim) | 한국어 역 | 정의 (verbatim) | 사용자가 행사하는 통제 |
|---|---|---|---|---|
| L1 | **Operator** | 조작자 | "User is in charge at all times while the agent is available to provide support on-demand." | 에이전트는 호출이 있어야 동작. 계획 수립은 사용자 몫 |
| L2 | **Collaborator** | 협업자 | "Both the agent and the user can plan, delegate, and execute tasks to leverage each other's capabilities." | 사용자가 작업물 수정 가능, 언제든 통제권 회수 |
| L3 | **Consultant** | 자문 의뢰자 | "Agent takes initiative in task planning and execution over extended time horizons." | 직접 조작이 아니라 **메시지를 통한 피드백**으로 간접 통제 |
| L4 | **Approver** | 승인자 | "User is only required to interact with the agent when the agent encounters a blocker." | 에이전트가 자율 결정, **중대한 행위에 대해서만** 승인 요청 |
| L5 | **Observer** | 관찰자 | "Fully autonomous agent that does not require, and comes with no means for, user involvement." | 로그 모니터링 + **비상 정지 스위치**만 |

**★ 등급 간에 바뀌는 것.** 이 프레임의 영리한 점은 등급을 **에이전트의 능력이 아니라 "인간이 무엇이 되는가"로 이름 붙였다**는 것이다. 조작자 → 협업자 → 자문 의뢰자 → 승인자 → 관찰자. **인간의 역할 이름만 읽어도 자기 조직이 지금 어디 있는지 즉시 판단된다.**

**인용 가능한 문장·개념**
> "We argue that an agent's level of autonomy can be treated as a **deliberate design decision, separate from its capability and operational environment.**"
- **AI autonomy certificates(AI 자율성 인증서):** 제3자 거버넌스 기구가 발급하는 디지털 문서로, 특정 기술 사양과 환경이 주어졌을 때 **"에이전트가 운용될 수 있는 최대 자율성 등급을 규정한다(prescribe the maximum level of autonomy at which an agent can operate)."**

**이 책에 쓸 수 있는 부분.** **L4 Approver와 L5 Observer 사이의 경계선이 가장 실전적인 재료다.** L4는 "막혔을 때만 부른다", L5는 **"부를 수단 자체가 없다."** 대부분의 한국 기업이 "자동화했다"고 말할 때 실제로는 L3~L4 사이에 있고, L5는 **비상 정지 외에 개입 경로가 설계상 존재하지 않는 상태**라는 점을 명확히 하면 리더들의 자기 진단이 훨씬 정확해진다.

> ⚠️ **번역 주의.** 여기서 `Consultant`는 "자문 의뢰자"다 — **자문하는 쪽이 AI가 아니라, 사람이 AI에게 맡겨놓고 훈수만 두는 구조**다. **Morris et al.의 "AI as a Consultant"와 방향이 정반대**이므로 두 프레임을 나란히 쓸 때 반드시 구별하라.

**한계·반박**
- **동료심사를 거치지 않았다.** `[WP]`로 표기해야 한다.
- ⚠️ 확인 결과 이 논문은 **Sheridan & Verplank(1978)도, Parasuraman et al.(2000)도, SAE J3016도 인용하지 않는다.** Morris et al.은 참고문헌에 있으나 AGI 등급 맥락으로만 언급된다. 즉 고전 계보와 단절돼 있다 — **이 책이 그 연결을 직접 이어주면 오히려 기여가 된다.**
- 등급 판정 기준이 **정성적**이라 두 평가자가 같은 시스템을 다르게 매길 여지가 크다(A-2-9의 κ 참조).

---

### A-2-3. ★★ Zheng et al. — **AAL / ACL 이원 체계** (이번 조사의 최대 수확) `[PP]`

**서지**
> Haining Zheng, Qian Dong, Rodolfo K. Depena, Jonathan D. Bhatia, Feng Xiao, Peng Xu (**ExxonMobil Technology and Engineering Company** / ExxonMobil Global Operations Company).
> "**Separating Capability from Permission: A Governance Framework for Agentic AI Autonomy Levels**."
> arXiv:**2607.23438v1** — 제출 **2026-07-26** · cs.AI; cs.CY; cs.MA · 10 pages, 2 tables, 3 figures
> https://arxiv.org/abs/2607.23438 · **[PP]** (프리프린트, 게재지 명시 없음)

**핵심 주장.** 자율성 논의는 **"기술적으로 할 수 있는 것"과 "실무에서 해도 되는 것"을 습관적으로 뒤섞는다.** 저자들은 이를 두 축으로 완전히 분리한다.

- **AAL (Allowed Autonomy Level, 허용 자율성 등급)** — "what an agentic system **is authorized to do** in deployment, rather than what it is technically capable of doing." 조직이 **감수할 의사가 있는 책임(accountability)의 수준.**
- **ACL (Autonomous Capability Level, 자율 능력 등급)** — "the **inherent technical capabilities** of an agent, independent of whether those capabilities are exercised in deployment."

**★ 등급표 A — Allowed Autonomy Level (AAL), 5단계 (원문 Table 1 전재)**

| AAL | Human Role | Human Tasks | Task Scope | **Accountability Implication (verbatim)** |
|---|---|---|---|---|
| **A1** | **Hands on** | Execute | Local-task | "Errors are bounded to a single invocation and corrected directly by the human who initiated the action." |
| **A2** | **Instructions on** | Instruct | Decision-support | "The agent provides advice, which can indirectly degrade human decisions." |
| **A3** | **Eyes on** | Supervise | Workflow | "Agents now act; failures become actions rather than advice, though supervision and reversibility still limit harm." |
| **A4** | **Mind on** | Set goals and constraints | System | "Humans no longer supervise steps; failures stem from design errors rather than execution mistakes." |
| **A5** | **Mind off** | Set policies | Organizational | "Decision-making authority is delegated; failures reflect accountability and governance gaps, not task errors." |

**각 AAL 본문 정의 (요지 + 핵심 verbatim)**
- **A1**: 에이전트는 **명시적 인간 호출에 대응해서만** 제한된 과업을 실행. 스스로 행동을 개시하지 않음.
- **A2**: 에이전트는 제안·분석을 **생성만** 하고 "all execution remains human-performed."
- **A3**: "agents execute multi-step tasks under human supervision." 에이전트 행위에는 인간 승인이 필요하거나, 이전 단계로 되돌릴 수 있어야 하거나, 완화 장치가 동반되어야 함. **가역성(reversibility)은 애플리케이션 의존적**이며 신중히 평가해야 함. (원문 예시: 소스 저장소에 커밋하는 코딩 에이전트는 가역, 산업용 화학 공정 제어 명령을 실행하는 에이전트는 비가역.)
- **A4**: "agents autonomously execute open-ended, multi-step workflows to achieve human-defined goals within fixed constraints." 인간은 목표·성공 기준·제약을 **사전에** 지정하되 실행 중 개별 행위를 승인하지 않음. **"moving correctness concerns from runtime supervision to upfront design."**
- **A5**: 인간은 운용 개시 **이전에** 정책 의도와 운영 경계를 정의·부호화·승인. 이후 에이전트는 "making and executing decisions without human intervention, step-level supervision, or routine reversibility." 책임은 권한을 위임한 **조직**에 귀속.

**★ 등급표 B — Autonomous Capability Level (ACL), 5단계 (원문 Table 2 전재)**

| ACL | Capability (verbatim) | Agent As | Highest AAL | Example |
|---|---|---|---|---|
| **C1** | "High-level perception/low-level reasoning. Able to provide results when called." | Model, Tool | A1 | Pattern recognition model, isolated manufacturing systems |
| **C2** | "High-level reasoning. Able to help humans make decisions." | Helper, Advisor, Assistant | A2 | Forecasting, predictive maintenance |
| **C3** | "Reasoning, planning, and tool calling. Able to complete tasks defined by humans." | **Junior Operator** | A3 | AI data analysis, some AI coding tools |
| **C4** | "Reasoning, multi-step planning, tool orchestration. Able to plan and complete tasks from an open-ended workflows." | **Sr. Operator** | A4 | Advanced AI coding agents |
| **C5** | "Reasoning, planning, tool orchestration, monitoring, and adaption. Able to run entire operations independently." | **Plant Manager, Decision Maker** | A5 | Self-running supply chain, unmanned manufacturing |

**★ 등급 간에 바뀌는 것 (저자들이 명시한 3축)**
> "As autonomy increases, **human control becomes less direct, reversibility decreases, and the consequences of failures become more difficult to contain**, requiring correspondingly stronger governance justification and safeguards."

그리고 A3→A4→A5의 이동을 **"successive transfers of control from runtime supervision to upfront governance and, ultimately, to delegated authority"**로 정식화한다. 즉 **통제가 사라지는 게 아니라, 통제가 놓이는 시점이 실행 중 → 설계 시점 → 정책 시점으로 앞당겨지는 것이다.**

**결정 절차 (Figure 1).** ① 시스템의 최고 ACL 판정 → ② 대응 AAL 잠정 설정 → ③ 해당 AAL에서의 최고 위험/결과 판정 → ④ **"Is the risk acceptable?"** → 아니면 **AAL을 1단계 낮추고** ③으로 복귀 → 수용 가능하면 확정. 절차는 A1에서 종료되며, **"In rare cases where risk remains unacceptable even at A1, the application should not be deployed in its current form and requires redesign."**

**★ 실증 사례 2건 — 의도적 하향 배치 (이 책이 가장 필요로 하는 종류의 증거)**
- **데이터 엔지니어링 다중 에이전트 시스템** — 기술적으로 **C4**이나 **A3로 의도적 하향 배치.** 이유: "ungoverned backfill jobs can corrupt downstream pipelines."
- **에너지 운영 다중 에이전트 코파일럿** — 연간 **약 20,000건**("approximately 20,000 unstructured field reports annually")의 비정형 현장 보고서를 검토하는 엔지니어 지원. 기술적으로 **C3**이나 **A2(자문 전용)로 배치.** 운영 원칙: **"AI reasons, guardrails verify, human decides."** 이유: 물리 도메인의 행위는 대체로 비가역(잘못된 장비 사이징은 시추 후 되돌릴 수 없음).
- 저자들의 정식화: **"The gap between C4 and A2 or A3 is not a deficiency; it is a deliberate governance choice."**

**★ Sheridan 계보 연결 — A절 계보 논증의 핵심 근거**
이 논문은 결론부에서 **명시적으로** 고전 계보를 호출한다:
> "Readers may refer to seminal work by **Sheridan and Verplank (1978)** to gain insight into such refinement."

참고문헌에 `Sheridan T.B.; Verplank W.L. 1978. Human and Computer Control of Undersea Teleoperators, Technical Report. MIT Cambridge Man-Machine Systems Lab.`이 실려 있다. 또한 **SAE J3016(2021), NIST AI RMF(2023), EU AI Act(2024), Feng·McDonald·Zhang(2025)**를 모두 인용한다. **이 논문 한 편이 1978년 Sheridan → 2026년 엔터프라이즈 에이전트 거버넌스로 이어지는 계보의 살아 있는 증거다.**

**인용 가능한 문장·수치**
- "An agent should not operate at an AAL **higher than the human organization is prepared to accept.**"
- "**Importantly, higher capability does not automatically imply higher allowed autonomy.**"
- "We expect most real-world Agentic AI applications to operate at **A1 through A3**. Levels **A4 and A5** require significantly stronger justification and safeguards due to their scope and potential impact and are therefore expected to be assigned **more selectively**."
- 등급 수 선택 근거: "we found that **five AAL levels** strike an appropriate balance between distinguishing meaningful differences in autonomous behavior and maintaining usability for governance reviews."
- 설계 3원칙: **rigor · stability · usability**. 특히 "**the number of autonomy levels should be limited, their meanings clearly articulated, and their progression clear.**"
- 안정성 논거: "Autonomy levels that depend on specific model capabilities, benchmarks, or architectural details **risk becoming obsolete or misleading** as new techniques emerge."

**이 책에 쓸 수 있는 부분 — A절에서 가장 큰 덩어리.**
1. **AAL/ACL 이원 분리를 이 책 등급 장치의 뼈대로 삼을 수 있다.** 한국 기업의 AX 논의가 거의 항상 "우리 모델이 뭘 할 수 있나"(=ACL)에서 끝나고 "우리 조직이 뭘 허용할 것인가"(=AAL)로 넘어가지 않는다는 지적을 이 논문으로 정면 뒷받침할 수 있다.
2. **"Hands on → Instructions on → Eyes on → Mind on → Mind off"** — 다섯 라벨은 한국어로 옮겨도 감이 살아 있고 임원 보고에 그대로 쓸 수 있다. 저자들도 "has proven effective for communication"이라고 자평한다.
3. **의도적 하향 배치 사례 2건** — "능력이 있어도 안 쓴다"가 실패가 아니라 **거버넌스 선택**이라는 것.
4. **가역성(reversibility)을 등급 판정의 1급 변수**로 삼는 발상. 코드 커밋 vs 화학 공정 제어 명령의 대조는 그대로 예화가 된다.

**한계·반박**
- **프리프린트이며 동료심사를 거치지 않았다.** 10페이지 분량의 산업 실무 보고에 가깝다.
- **단일 기업(ExxonMobil) 사례 2건**에 기반한다. 에너지·중공업 편향이 뚜렷하고, 비가역성이 지배적인 물리 도메인의 직관이 소프트웨어 도메인에 그대로 이식되지 않을 수 있다.
- 저자들 스스로 인정: "The terminology used to describe different levels ... **may benefit from further fine-tuning**."
- ACL 판정 기준이 여전히 정성적이다. C3과 C4의 경계("open-ended workflow"인가)는 판정자 재량이 크다.
- ACL을 **개별 컴포넌트가 아니라 조합된 시스템 수준에서** 평가해야 한다고 명시하는데(부록 A.2), 실무 판정 난도를 크게 높인다.

---

### A-2-4. Luo, Li, Fan & Tang — Data Agents 6단계, **SAE 명시 차용** `[PR]`

**서지**
> Yuyu Luo, Guoliang Li, Ju Fan, Nan Tang. "**Data Agents: Levels, State of the Art, and Open Problems**."
> arXiv:**2602.04261v1** — 제출 **2026-02-04** · 게재: **2026 ACM SIGMOD/PODS Conference**, Bengaluru, India
> https://arxiv.org/abs/2602.04261 · **[PR]** (SIGMOD 2026 게재 확인)

**★ 등급표 (6단계, 원문 정의 verbatim)**

| # | 명칭 | 한국어 역 | 정의 (verbatim) |
|---|---|---|---|
| L0 | **No Autonomy** | 자율성 없음 | "All tasks in data management, preparation, and analysis are performed manually by humans." |
| L1 | **Assistance** | 보조 | "L1 data agents operate within a stateless, prompt-response framework. They can answer questions, generate code snippets, or suggest queries, but they **do not perceive or interact with the environment**." |
| L2 | **Partial Autonomy** | 부분 자율 | "L2 data agents gain the ability to **perceive and interact with their environment**, including data lakes, DBMSs, code interpreters, and external APIs." |
| L3 | **Conditional Autonomy** | 조건부 자율 | "L3 data agents are expected to autonomously orchestrate and execute tailored data pipelines for a wide range of tasks **under human supervision**." |
| L4 | **High Autonomy** | 고자율 | "L4 data agents achieve high autonomy and reliability, **eliminating the need for human supervision and explicit instructions**." |
| L5 | **Full Autonomy** | 완전 자율 | "At L5, data agents are envisioned to **innovate new solutions and paradigms beyond existing methods**, acting as fully autonomous and generative data scientists." |

**★ 계보 (중요).** 저자들이 SAE 차용을 **명시적으로 선언**한다:
> "Similar challenges were previously faced by the driving-automation community, which motivated the **SAE J3016 standard** that introduced a six-level taxonomy of autonomy."

**이 책에 쓸 수 있는 부분.**
1. **동료심사(SIGMOD 2026)를 통과한 6단계 표**라 인용 안정성이 가장 높다.
2. **L1→L2의 분기점이 "환경을 지각·상호작용하는가"**라는 점이 매우 실용적인 눈금이다 — **사내 챗봇(L1)과 사내 시스템에 붙은 에이전트(L2) 사이의 선을 정확히 그어준다.**
3. "왜 하필 6단계인가"에 대한 정직한 답("자율주행 커뮤니티가 먼저 같은 문제를 겪었고 SAE J3016이 나왔다")을 그대로 인용할 수 있다.

**한계·반박**
- 데이터 관리 도메인 한정.
- **L5 정의("기존 방법을 넘어선 새 패러다임을 혁신")는 자율성 등급이 아니라 능력 등급에 가깝다.** A-2-3의 AAL/ACL 구분으로 보면 L4~L5는 ACL 축으로 미끄러진 셈이다. **이 미끄러짐 자체가 "왜 능력과 권한을 분리해야 하는가"의 좋은 반례가 된다.**

---

### A-2-5. Feng & Chen — GUI Agent Autonomy Levels (GAL), 6단계 `[PP]`

**서지**
> Sidong Feng (CUHK Shenzhen), Chunyang Chen (TU Munich). "**How Smart Is Your GUI Agent? A Framework for the Future of Software Interaction**."
> arXiv:**2602.11514v1** — 제출 **2026-02-12** · CC BY 4.0 · DOI 10.48550/arXiv.2602.11514 · **[PP]**

**등급표 (6단계)**

| # | 명칭 (verbatim) | 한국어 역 | 정의 |
|---|---|---|---|
| L0 | **No Automation** | 자동화 없음 | "The user performs all actions manually" |
| L1 | **Minimal Assistance** | 최소 보조 | "observes user interactions and offers lightweight guidance" — **행위는 하지 않음** |
| L2 | **Basic Automation** | 기본 자동화 | 명시적 지시가 있을 때 "executes each command immediately, without clarification" |
| L3 | **Conditional Automation** | 조건부 자동화 | 사전 정의된 규칙 내에서 "executes multi-step workflows" — **인간 감독 필수** |
| L4 | **High Automation** | 고자동화 | 애플리케이션을 가로질러 "autonomously handling complex, interconnected tasks" |
| L5 | **Full Automation** | 완전 자동화 | "across any software, operating system, or interface" |

**등급 간에 바뀌는 것 (저자 정리).**
- **결정 권한:** 사용자 → 에이전트 → 인간 게이트가 붙은 에이전트 → 드물게만 개입 → 완전 자율
- **행위 실행:** 없음 → 조언만 → 단일 스텝 → 다단계 시퀀스 → 앱 간 복합 워크플로 → 범용
- **인간 감독:** 매 스텝 → 모니터링 → 검증 게이트 → 예외 처리 → 드문 개입 → **소멸(eliminated)**

**계보.** **SAE International (2016)을 1차 영감으로 명시 인용** — "Inspired by the autonomy levels like SAE levels." Sheridan·Parasuraman은 인용하지 않는다.

**이 책에 쓸 수 있는 부분.** **L2와 L3의 차이**("지시받은 명령을 즉시 실행" vs "사전 정의된 규칙 안에서 다단계 워크플로")는 실무자가 자기 회사의 RPA/자동화 도구를 자리매김하기 좋은 눈금이다. 또한 **L5를 "감독 소멸"로 정의한 것은 EU AI Act Article 14(고위험 시스템의 인간 감독 의무)와 정면 충돌한다** — 이 충돌 자체가 좋은 서술 소재다(A-2-11).

**한계·반박** 프리프린트이며 **SAE 등급의 거의 직역 이식**이다(L0 No Automation ~ L5 Full Automation). 독창성보다는 **도메인 적용 사례**로 인용하는 게 정직하다. ⚠️ 게재지 확인 실패 → F절.

---

### A-2-6. Ye et al. — 의료 LLM 자율성 **4단계(L0–L3)** `[PP]`

**서지**
> Xiao Ye, Jacob Dineen, Zhaonan Li, Zhikun Xu, Weiyu Chen, Shijie Lu, Yuxi Huang, Ming Shen, Phu Tran, Ji-Eun Irene Yum, Muhammad Ali Khan, Muhammad Umar Afzal, Irbaz Bin Riaz, Ben Zhou (Arizona State University / Mayo Clinic).
> "**Evaluating Medical LLMs by Levels of Autonomy: A Survey Moving from Benchmarks to Applications**."
> arXiv:**2510.17764v1** — 제출 **2025-10-20** · **[PP]**

**등급표 (4단계)**

| # | 명칭 | 정의 (verbatim) | 인간의 역할 |
|---|---|---|---|
| L0 | **Inform** | "the system functions purely as an informational tool: it explains medical concepts and provides a general background in plain language." | 비개인화 교육 콘텐츠 + 명시적 면책. 임상 결정 없음 |
| L1 | **Information Transformation & Aggregation** | "turns raw, heterogeneous clinical data into standardized, computable representations and then combines them with external evidence to produce grounded outputs." | 데이터 구조화·검색 인프라 지원. 자율 결정 없음 |
| L2 | **Decision Support** | "the system provides patient-specific recommendations that can assist clinical decision making." | 임상의가 검토하고 **독립적으로** 조치 결정 |
| L3 | **Agents Under Human Supervision** | "systems that plan and invoke tools/APIs to initiate actions in clinical workflows **while keeping a clinician explicitly 'in the loop'** for review, modification, and sign-off." | 체크포인트별 명시적 감독 |

**★ 이 책에 쓸 수 있는 부분 — 규제 산업에서는 등급 상단이 아예 잘려 있다.**
이 서베이는 **L4·L5를 아예 정의하지 않는다.** 의료에서는 "인간 감독 하 에이전트"가 **현실적 최상단**이다. 금융·통신 등 규제 산업 리더 독자에게 "우리는 왜 5단계까지 못 가나"에 대한 답이 된다 — **못 가는 게 아니라 가면 안 되는 것.** 또한 **L0→L1의 분기점("원시 임상 데이터를 표준화·계산 가능한 표현으로 변환")은 AX 체계 구축의 데이터 레이어 작업과 정확히 대응한다.**

**한계·반박** 프리프린트. `L3` 정의에서 `in the loop`를 인용부호로 쓰면서도 출처를 밝히지 않는다. Morris et al.·SAE·Parasuraman·Sheridan 모두 인용하지 않는다.

---

### A-2-7. Chiodo et al. — **"HITL"이라는 한 단어가 실은 세 가지** `[PP]`

**서지**
> Maurice Chiodo, Dennis Müller, Paul Siewert, Jean-Luc Wetherall, Zoya Yasmine, John Burden. "**Formalising Human-in-the-Loop: Computational Reductions, Failure Modes, and Legal-Moral Responsibility**."
> arXiv:**2505.10426** — v1: **2025-05-15** / v2: 2025-09-25 · 31 pages · **[PP]**

**★ 초록 (VERBATIM)**
> "We use the notion of oracle machines and reductions from computability theory to formalise different Human-in-the-loop (HITL) setups for AI systems, **distinguishing between trivial human monitoring (i.e., total functions), single endpoint human action (i.e., many-one reductions), and highly involved human-AI interaction (i.e., Turing reductions)**. We then proceed to show that **the legal status and safety of different setups vary greatly.** We present a taxonomy to categorise HITL failure modes, highlighting the practical limitations of HITL setups."

**등급표 (3단계 — 형식적 환원 수준)**

| # | 구성 | 한국어 역 | 형식적 대응 |
|---|---|---|---|
| 1 | **trivial human monitoring** | 형식적 인간 모니터링 | total functions |
| 2 | **single endpoint human action** | 단일 종단점 인간 행위 | many-one reductions |
| 3 | **highly involved human-AI interaction** | 고관여 인간-AI 상호작용 | Turing reductions |

**★ 이 책에 쓸 수 있는 부분.** **"HITL"이라는 한 단어가 실은 전혀 다른 세 가지를 뭉뚱그린다**는 통찰이 핵심이다. 한국 기업 문서에서 **"사람이 검토합니다(HITL)"라는 문장이 실제로는 1번(형식적 모니터링, 사실상 고무도장)인 경우가 압도적으로 많다**는 지적을 이 논문이 형식적으로 뒷받침한다. 저자들은 또 영국·EU 규제가 책임 귀속에서 **"인간에게 부당하게 책임을 전가(unfairly placing blame on humans)"**하지 않아야 함을 강조한다 — EU AI Act Article 14와 함께 읽으면 강력한 대비가 된다.

**한계·반박** 프리프린트이며 수학적 형식화가 실무 판정 도구로 바로 쓰이긴 어렵다. 등급이 "감독 강도"가 아니라 "계산 구조"로 정의돼 있어 조직 운영 언어로 번역하는 작업이 필요하다.

---

### A-2-8. Grunde-McLaughlin et al. — **감독 등급을 올려도 감독의 질은 안 따라온다** `[PP]`

**서지**
> Madeleine Grunde-McLaughlin, Hussein Mozannar, Maya Murad, Jingya Chen, Saleema Amershi, Adam Fourney (Microsoft Research 계열).
> "**Overseeing Agents Without Constant Oversight**." arXiv:**2602.16844v1** — 제출 **2026-02-18** · cs.HC; cs.AI · **[PP]**

**핵심 주장.** 인간 감독을 가능케 하려고 에이전트는 추론·행위 스텝의 **트레이스(trace)**를 제공하지만, **"Designing traces to have an informative, but not overwhelming, level of detail remains a critical challenge."** Computer User Agent 대상 **사용자 연구 3건**.

**★ 핵심 발견 (인용 가능)**
- 새 인터페이스는 **오류 발견 시간을 단축**시켰으나, 참가자들은 **정확도의 유의미한 개선 없이 확신(confidence)만 더 커졌다**고 보고.
- 인간 검증의 난제: **"managing built-in assumptions, users' subjective and changing correctness criteria, and the shortcomings, yet importance, of communicating the agent's process."**

**★ 이 책에 쓸 수 있는 부분.** **"확신은 늘었는데 정확도는 그대로"**는 Morris et al.의 Level 2 위험 **over-trust**를 실험적으로 확인한 것이다. 등급표를 만든 뒤 반드시 따라와야 할 반론 — **"3단계(감독)로 설정했다고 감독이 실제로 일어나는 것은 아니다"** — 의 근거로 최적이다. **A-3의 Victor et al.(2018) "눈은 도로에, 손은 핸들에, 그래도 28% 충돌"과 정확히 같은 구조다.**

**한계·반박** 프리프린트, 단일 에이전트 대상. ⚠️ 게재 학회 미확인 → F절.

---

### A-2-9. ★ Cihon et al. — 5차원 × 3수준, 그리고 **판정 불일치의 수치** `[WP]`

**서지**
> Peter Cihon, Merlin Stein, Gagan Bansal, Sam Manning, Kevin Xu. "**Measuring AI agent autonomy: Towards a scalable approach with code inspection**."
> arXiv:**2502.15212v1** — 제출 **2025-02-21** · **NeurIPS SoLaR Workshop 2024** · **[WP]** (워크숍 논문)

**등급표 — 5차원 × 3수준**

| 차원 | Lower | Middle | Higher |
|---|---|---|---|
| **Actions** | conversation only | pre-configured tools | arbitrary code execution |
| **Environment** | constrained | protected Docker | unconstrained internet/local access |
| **Orchestration** | predetermined | bounded flexible | unbounded |
| **Human-in-the-loop** | always consult | terminate condition | never consult |
| **Observability** | dashboards/explanations | logs | no logs |

**★ 실증 결과 (수치 — 반올림 금지)**
- 대상: **AutoGen 애플리케이션 10건**
- 평가자 간 일치도 **Fleiss' κ = 0.64** (전체)
- 차원별: **Orchestration κ=0.67**, **human-in-the-loop κ=0.65**, **Environment κ=0.60**, **Observability κ=0.47**, **Actions κ=0.30**
- 핵심 발견: **"No application scored 'lower' on actions"**

**★ 이 책에 쓸 수 있는 부분.**
1. **관측가능성(observability)을 자율성의 한 차원으로 넣은 드문 사례.** "로그가 없으면 자율성이 더 높다"는 발상 — AX 체계의 로깅·감사 요건을 자율성 등급과 묶어 설명할 때 결정적이다. **그리고 이것은 Sheridan(1978) 등급 7~9(통보 정책)의 재발견이다**(A-1-1).
2. **★ κ 수치가 가장 유용하다.** Actions 차원의 **κ=0.30**은 "무엇을 할 수 있는가"가 **가장 합의가 안 되는 축**이라는 뜻이다. **"자율성 등급 판정은 생각보다 훨씬 안 맞는다"는 것을 숫자로 말할 수 있는 유일한 자료**이며, 이 책이 "판정 기준을 문서화하고 2인 이상이 독립 판정하라"고 권고할 때의 근거다.
3. **"모든 앱이 actions에서 lower를 받지 못했다"** — 실무에서 도입되는 에이전트는 **이미 대부분 상단 자율성에서 출발한다**는 실증. "우리는 아직 낮은 단계"라고 믿는 조직에 대한 반증.

**한계·반박** **워크숍 논문**이며 정식 학회 논문이 아니다. 표본이 **AutoGen 앱 10건**으로 매우 작다. 코드 정적 검사라 **런타임 실제 행위와 괴리**가 있을 수 있다.

---

### A-2-10. ★ Engin & Hand — "범주가 아니라 차원", **3As** `[PP]`

**이 항목은 이 책이 등급표를 내놓는 순간 반드시 따라올 반론에 대한 정면 답변이다.**

**서지**
> Zeynep Engin (The Digital Statecraft Academy; UCL 컴퓨터과학과), David Hand (Imperial College London 수학과).
> "**Towards Adaptive Categories: Dimensional Governance for Agentic AI**."
> arXiv:**2505.11579** — v1: **2025-05-16** / v2: 2025-11-22 / v3: **2026-06-19** · 본문 12쪽 · CC BY 4.0 · **[PP]**

**★ 핵심 주장 (초록 verbatim)**
> "As AI systems evolve from static tools to dynamic agents, traditional categorical governance frameworks—based on **fixed risk tiers, levels of autonomy, or human oversight models**—are increasingly insufficient on their own."

**★ 등급이 아니라 "차원" — 3As (본문 verbatim)**
> "We propose **dimensional governance**: a framework built on three core characteristics of AI systems—**decision authority** (when and how should AI have the right to decide?), **process autonomy** (how independently does the system operate?), and **accountability configuration** (who is responsible when something goes wrong?). We call these **'the 3As of dimensional governance.'**"

| 차원 | 원문 | 한국어 역 | 정의 질문 (verbatim) |
|---|---|---|---|
| A1 | **decision authority** | 결정 권한 | "when and how should AI have the right to decide?" |
| A2 | **process autonomy** | 과정 자율성 | "how independently does the system operate?" |
| A3 | **accountability configuration** | 책임 구성 | "who is responsible when something goes wrong?" |

핵심 전환:
> "Rather than **only** asking *'Which box does this system fit into?'*, dimensional governance first asks *'**Where along multiple critical dimensions does this system currently stand—and how is it moving?**'*"

**범주적 프레임워크의 실패 5가지 (§2 원문 소제목)**
1. **Risk depends on context and application** — "Risk emerges from deployment context rather than being intrinsic to the system."
2. **Technological evolution challenges fixed categorisation**
3. **AI systems operate on dynamic, evolving data foundations** — "A recommendation algorithm initially classified as 'low-risk' may gradually shift toward higher-risk behaviour as its training data evolves, **without crossing any clear categorical boundary** that would trigger enhanced oversight."
4. **Multi-agent architectures disrupt linear autonomy progression** — "Authority becomes a **dynamic, relational property** rather than a fixed feature of individual systems."
5. **Meaningful human oversight is increasingly challenged** — "humans nominally retain oversight responsibilities **without real operational influence**."

**★ 핵심 진단문 (인용 최적)**
> "The core problem remains consistent: **not that categories themselves are unnecessary**, but that static categorisation assumes human-AI relationships can be neatly boxed into fixed states, when reality reveals continuous, evolving patterns of *agency*, *autonomy*, and *accountability*."

**★ 계보 인용 확인.** 본문 §2에서 **`Parasuraman et al., 2000`**을 "levels of autonomy"를 정의한 범주적 프레임워크의 대표로 **명시 인용**하며, `EU AI Act, 2024`·`Docherty, 2012`·`NIST AI RMF (2023)`를 모두 인용한다. **즉 2026년 에이전틱 AI 거버넌스 논쟁이 2000년 논문을 직접 상대하고 있다.**

**★ 현실 실패 사례 3건 (§2 말미 — 그대로 예화로 사용 가능)**
- **금융:** "decision-support tools"로 분류된 신용평가 알고리즘이 **"quietly assumed *de facto* decision authority** as human reviewers increasingly defer to algorithmic outputs" (Gsenger & Strle, 2021 인용)
- **헬스케어:** "advisory"로 배포된 진단 시스템이 의도보다 훨씬 강하게 임상 결정을 좌우하며, **인간 판단이 기계 권고를 언제 뒤집어야 하는지에 대한 명확한 임계가 없다** (Shortliffe & Sepúlveda, 2018 인용)
- **자율주행:** 인간 운전자와 AI 코파일럿 사이 책임 경계가 흐려져 **"neither party maintained full situational awareness or control"**인 사고 (Ansari et al., 2022 인용)

**운용 3단계 (§3).** ① 차원을 따라 **측정** → ② 규제 요건을 결정하는 **증거 기반 임계** 설정 → ③ 증거가 쌓이면 **임계를 조정**한다. 이때 **기저 차원 프레임워크 자체는 안정적으로 유지.** 유비: 신용평가(연속 점수 + 조정 가능한 대출 임계), **BMI**(연속 측정 + 25·30 임계).

**★ 이 책에 쓸 수 있는 부분 — 등급 장치의 "안전장치".**
1. 이 책이 등급표를 제시하는 순간 반드시 따라올 반론("현실은 칸으로 안 나뉜다")에 대한 **정면 답변**을 제공한다. 저자들 자신이 **"categories themselves are not unnecessary"**라고 명시하므로, 이 논문은 등급표의 적이 아니라 **등급표를 제대로 쓰는 법**이다.
2. **"범주를 차원 위에 세워라"** — 등급은 목적이 아니라 **연속 차원 위에 놓은 조정 가능한 임계**라는 설계 원리. 이 책의 등급표를 "고정된 5칸"이 아니라 **"3개 축 위의 임계선"**으로 제시하면 훨씬 강해진다.
3. **실패 사례 3건**은 "자문(advisory)으로 도입했는데 실질 결정권이 슬그머니 넘어갔다"는 이 책의 핵심 경고에 딱 맞는 증거다. 특히 **"quietly assumed de facto decision authority"**는 그대로 인용할 문장이다.
4. **BMI 유비**는 한국 독자에게 즉시 이해된다.

**한계·반박** 프리프린트이며 **Commentary 성격**이다(저자들 스스로 "This Commentary builds upon and extends earlier work on the Human-AI Governance (HAIG) framework (Engin, 2025)"라고 밝힘). **3As를 실제로 어떻게 측정할 것인지에 대한 조작적 정의가 없다.** 문제 제기에 강하고 해법에 약하다 — **이 책이 3As를 A-2-3의 AAL/ACL과 결합해 조작화하면 오히려 이 책의 기여가 된다.**

---

### A-2-11. 그 밖의 다차원 프레임 2건

**(a) Trumpler et al. — AAAA, 이산 등급 폐기 `[PP]`**
> Lennart Trumpler, Rodrigo Furlan de Assis, Elias Ribeiro da Silva, Luis Antonio de Santa-Eulalia, Christian Hendriksen. "**Agentic AI Autonomy Assessment: A Decision-Support Framework Towards Governed Supply Chain Systems**." arXiv:**2607.25405v1** — 제출 **2026-07-28** · 28 pages · **[PP]**

초록 (VERBATIM): "existing taxonomies of autonomy **only offer discrete classifications, rely on subjective judgement, and cannot track autonomy across a system's life cycle**…" 제안 3차원: **user delegation, consultation, collaboration.**

실증 (VERBATIM): "The framework's construct validity was tested in a simulated **beer distribution game**… Results reveal a **weak link between autonomy and tier costs with a positional effect: upstream tiers benefit from higher autonomy while downstream tiers are harmed**, positioning autonomy as **an inherent dimension of agentic systems, orthogonal to capability.**"

> **★ 이 책에 쓸 수 있는 부분.** ① **"자율성은 능력과 직교(orthogonal)한다"**는 실험적 주장 — A-2-3의 AAL/ACL 분리를 **정량 실험으로 뒷받침하는 유일한 자료.** ② **위치 효과(positional effect)**가 가장 값지다: **공급망 상류는 높은 자율성으로 이익, 하류는 손해.** 즉 **"조직 내 어느 위치에 있느냐에 따라 최적 자율성 등급이 다르다."** 전사 일괄 등급 정책이 왜 실패하는지에 대한 실증 근거이며, **부서·기능별로 등급을 달리 잡아야 한다**는 주장의 뼈대가 된다. ③ 생애주기 추적 — "한 번 3단계로 승인하면 끝"이 아니라는 것.
>
> **한계:** 프리프린트이며 실증이 **시뮬레이션(맥주 유통 게임)**이다. 저자들 스스로 자율성-성과 연결이 **"weak link"**라고 보고한다 — **자율성을 높인다고 성과가 좋아진다는 증거는 약하다.** 이 책이 자율성 상향을 무조건 권하지 않아야 할 근거이기도 하다.

**(b) Händler (2023) — 다차원의 초기 사례 `[PP]`**
> Thorsten Händler. "**Balancing Autonomy and Alignment: A Multi-Dimensional Taxonomy for Autonomous LLM-powered Multi-Agent Architectures**." arXiv:**2310.03659v1** — 제출 **2023-10-05** · **[PP]**
>
> **2023년 10월**이라는 시점이 값지다 — Morris et al.(2023-11-04)보다 **한 달 앞서** "자율성은 다차원"을 제목에 내걸었다. "다차원 접근이 최근 유행이 아니라 LLM 에이전트 담론 초기부터 있었다"는 계보 서술에 쓸 수 있다. ⚠️ 세부 차원 목록 미확인 → F절.

**(c) Li et al. — ASTELD 6축 `[PP]`**
> Siyuan Li 외 22인. "**ASTELD: A Six-Axis Classification Framework for Autonomous AI Agents**." arXiv:**2608.05201v1** — 제출 **2026-08-05** · 40 pages · **[PP]**
> 6축: Architecture pattern / Security posture / Tool integration model / Execution paradigm / **Level of autonomy and human control** / Deployment topology. **8개 자율 AI 에이전트 플랫폼에 실증 적용.**
>
> **이 책에 쓸 수 있는 부분:** **자율성이 6개 축 중 하나일 뿐**이라는 배치 자체가 논거다 — AX 체계를 "자율성 등급표 하나"로 환원하려는 유혹에 대한 견제. ⚠️ 해당 축의 구체적 등급값 미확인 → F절.

---

### A-2-12. AI 랩·규제기관의 공식 프레임

**(a) Anthropic — Responsible Scaling Policy / AI Safety Levels `[WP]`**
> Anthropic, "Anthropic's Responsible Scaling Policy," **2023-09-19** · https://www.anthropic.com/news/anthropics-responsible-scaling-policy
> 현행: **Version 3.4, 2026-07-08 발효** (anthropic.com/rsp)

- **ASL = "AI Safety Levels"**, 모델: **"modeled loosely after the US government's biosafety level (BSL) standards for handling of dangerous biological materials."**

| 등급 | 정의 (verbatim, 2023 초판) |
|---|---|
| **ASL-1** | "Systems which pose no meaningful catastrophic risk, for example a 2018 LLM or an AI system that only plays chess." |
| **ASL-2** | "Systems that show early signs of dangerous capabilities – for example ability to give instructions on how to build bioweapons – but where the information is not yet useful due to insufficient reliability or not providing information that e.g. a search engine couldn't." |
| **ASL-3** | "Systems that **substantially increase the risk of catastrophic misuse** compared to non-AI baselines (e.g. search engines or textbooks) **OR** that show **low-level autonomous capabilities**." |
| **ASL-4+** | "Not yet defined as it is too far from present systems, but will likely involve **qualitative escalations in catastrophic misuse potential and autonomy**." |

**★ ASL-3 실제 발동 (2025):** Anthropic, "Activating ASL3 protections," **2025-05-22**. 발동 모델 **Claude Opus 4**. ASL-3 Security Standard("increased internal security measures that make it harder to steal model weights") + ASL-3 Deployment Standard(CBRN 오용 위험 제한). ASL-2 대비 "a higher level of defense … **suitable against sophisticated non-state attackers**."

> **이 책에 쓸 수 있는 부분.** ① **"등급이 실제로 발동된 사례"** — 프레임워크가 문서로만 존재하지 않고 2025년 5월 실제로 트리거되어 배포 조건이 바뀌었다. **등급 체계가 종이가 아니라 작동하는 장치임을 보여주는 최상의 예화.** ② **BSL(생물안전등급) 차용** — 자율성 등급의 유비를 자율주행에서만 찾을 필요가 없다는 좋은 반례. ③ ASL-3 정의에 **"low-level autonomous capabilities"**가 명시적으로 들어간다.
>
> **한계:** 기업 자율 규제 문서이며, **자율성 등급이 아니라 위험 능력 등급**이다. 조직의 업무 위임 수준을 재는 눈금이 아니라 **모델 출시 게이트**다. **목적이 다르다는 점을 반드시 구분해 서술하라.** 등급 판정 주체가 개발사 자신이라는 자기심사 구조의 한계도 있다. ⚠️ 현행 v3.4의 ASL 정식 정의문 미확인 → F절.

**(b) OpenAI — Preparedness Framework v2 `[WP]`**
> OpenAI, "Preparedness Framework," **Version 2, Last updated: 2025-04-15** (PDF 원문 직접 판독)

Tracked Categories 3개: **Biological and Chemical** / **Cybersecurity** / **AI Self-improvement**(후자는 "could also create new challenges for **human control of AI systems**").

능력 임계 2단계 (VERBATIM):
- **High**: "capabilities that **significantly increase existing risk vectors** for severe harm… required to have robust and effective safeguards… **before they are deployed**"
- **Critical**: "capabilities that present a meaningful risk of a **qualitatively new threat vector**… require safeguards **even during the development** of the covered system, **irrespective of deployment plans**."

Research Categories 중 자율성 관련: **Long-range Autonomy** ("execute a long-horizon sequence of actions… **without being directed by a human**"), **Autonomous Replication and Adaptation**, **Sandbagging**, **Undermining Safeguards**, **Nuclear and Radiological**.

**★ v2 변경 사항 (VERBATIM) — 이 책에 매우 유용**
> "**AI Self-improvement** (now a Tracked Category), **Long-range Autonomy** and **Autonomous Replication and Adaptation** (now Research Categories) **are distinct aspects of what we formerly termed Model Autonomy.**"

기타 수치: "severe harm" 정의 = **"the death or grave injury of thousands of people or hundreds of billions of dollars of economic damage."** / AI Self-improvement [Critical] = "…in **1/5th the wall-clock time** of equivalent progress in 2024 (e.g., sped up to just **4 weeks**)…"

> **★ 이 책에 쓸 수 있는 부분.** **"Model Autonomy를 세 조각으로 쪼갰다"**는 v2 변경이 다차원 논지를 **기업 실무 레벨에서 뒷받침**한다. **OpenAI조차 "자율성"이라는 단일 범주로는 측정이 안 돼서 자기 개선 / 장기 자율 / 자율 복제·적응으로 분해했다**는 사실은, "자율성 등급을 하나의 숫자로 매기려 하지 말라"는 이 책의 주장에 실무 권위를 실어준다. 또한 **High=배포 전 / Critical=개발 중에도**라는 게이트 구분은 A-2-3 AAL의 "실행 중 감독 → 설계 시점 거버넌스" 전이와 개념적으로 짝을 이룬다.
>
> **한계:** 자율성이 Tracked가 아니라 **Research Category(위협 모델이 아직 성숙하지 않은 영역)로 강등**돼 있다 — **가장 중요한 축이 가장 덜 측정 가능한 축**이라는 자백이기도 하다. 반박 소재로 쓰면 좋다.
>
> ⚠️ **중요:** 널리 회자되는 **OpenAI의 "5단계 AGI 진척 체계"(Level 1 Chatbots ~ Level 5 Organizations)는 이번 조사에서 공식 출처를 확인하지 못했다.** Preparedness Framework v2 PDF 전문 어디에도 등장하지 않는다. **"OpenAI가 공식 발표한 5단계"로 쓰면 안 된다.** → F절.

**(c) Google DeepMind — Frontier Safety Framework `[WP]` (부분 확인)**
> FSF **3.0: 2025-09-22** 발행 / **3.1: 2026-04-17** 갱신 (deepmind.google 블로그 기준)

확인된 CCL(Critical Capability Level) 계열: **Harmful Manipulation CCL** / **Instrumental Reasoning CCLs**("an AI model starts to think deceptively") / **Machine Learning R&D CCLs** / **Tracked Capability Levels (TCLs)** — FSF 3.1에서 신설, "spot and evaluate potential less extreme risks sooner."

> **이 책에 쓸 수 있는 부분.** ① **Instrumental Reasoning CCL** — 자율성 등급을 **행위 범위가 아니라 인지 성향**으로 재는 드문 사례. ② **FSF 3.1의 TCL 신설** — 등급 체계가 "너무 성글다"는 운용 피드백에 따라 **중간 계층을 추가한 실제 사례.** 독자에게 **"등급표는 한 번 만들고 끝이 아니라 운용하며 눈금을 조정하는 것"**을 말할 때 쓸 수 있는 증거다. **세 프런티어 랩(Anthropic v3.4, OpenAI v2, DeepMind v3.1)이 모두 자기 등급 체계를 여러 차례 개정했다**는 사실 자체가 강력한 서술 재료다.
>
> **한계:** 블로그 페이지 기준 확인이며 CCL 전체 목록·정식 정의문 미확인. **이 프레임워크에도 "자율성 등급" 표는 없다** — 능력 임계만 있다. → F절.

**(d) ★ EU AI Act Article 14 — 인간 감독 (법령)**
> **Regulation (EU) 2024/1689** (Artificial Intelligence Act), **Article 14 — Human oversight.** Official Journal of the EU, L 2024/1689, **2024년 7월**.

**제1항 (VERBATIM):**
> "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they **can be effectively overseen by natural persons** during the period in which they are in use."

**제4항 (a)~(e) — 감독자에게 보장되어야 할 능력 (VERBATIM)**

| 항 | 원문 | 한국어 역 |
|---|---|---|
| (a) | "properly understand the relevant capacities and limitations of the high-risk AI system and be able to duly monitor its operation" | 시스템의 능력과 **한계**를 적절히 이해하고 작동을 정당하게 모니터링 |
| (b) | "remain aware of the possible tendency of automatically relying or over-relying on the output produced by a high-risk AI system (**automation bias**)" | 산출물에 자동 의존·과의존하는 경향(**자동화 편향**)을 계속 인식 |
| (c) | "correctly interpret the high-risk AI system's output, taking into account…the interpretation tools and methods available" | 가용 도구·방법을 고려해 산출물을 올바르게 해석 |
| (d) | "decide…**not to use** the high-risk AI system or to otherwise **disregard, override or reverse** the output" | 사용하지 않기로 결정하거나 산출물을 무시·무효화·번복 |
| (e) | "**intervene** in the operation of the high-risk AI system or **interrupt** the system through a **'stop' button** or a similar procedure" | 작동에 개입하거나 **'정지' 버튼**으로 중단 |

**제5항 (요지):** Annex III 1(a)의 특정 생체인식 시스템은 조치가 **최소 2인의 유자격 자연인**에 의한 검증을 거쳐야 한다(법 집행 맥락의 비례성 예외 있음).

> **★ 이 책에 쓸 수 있는 부분 — 매우 크다.**
> 1. **(b)의 automation bias 명문화는 놀라운 입법이다.** **"과의존 경향을 계속 인식할 것"을 법적 의무로 부과**했다. Morris et al.의 Level 2 위험 "over-trust", A-2-8의 "확신은 늘고 정확도는 그대로", 그리고 1차에서 확보한 Skitka(1999)와 **정확히 사각 대응**한다.
> 2. **(d)의 "disregard, override or reverse"와 (e)의 "stop button"은 A-2-2 Feng et al.의 L5 Observer가 가진 유일한 권한("emergency off-switch")과 정확히 같다.** 즉 **EU 규제는 고위험 영역에서 최소 L4~L5 사이 어딘가의 감독을 법으로 강제**하는 셈이다.
> 3. 이 조항 덕분에 이 책은 **"등급을 자유롭게 고를 수 있는 게 아니다"**라고 단언할 수 있다 — **고위험 분류에 들어가는 순간 상단 등급은 법적으로 봉인된다.** A-2-6(의료 L0~L3)의 실증과 겹친다.
> 4. **제5항의 "최소 2인"** — 등급 체계에 **감독자 수**라는 축을 넣을 수 있다는 힌트. 대부분의 등급표가 놓치는 차원이다.
>
> **한계·반박.** 실효성 논쟁이 크다. A-2-10 Engin & Hand의 지적: 콘텐츠 모더레이션에서 인간 검토자가 명목상 승인권을 갖지만 "the volume and opacity of AI-generated recommendations often render this oversight **superficial**." 즉 **Article 14는 감독의 형식을 규정할 뿐 감독의 실질을 보장하지 못한다.** A-2-7의 "trivial human monitoring"이 바로 이 함정이다.

**(e) ★ NIST AI RMF — 자율성을 등급화하지 **않는다** `[WP]`**
> **NIST AI 100-1, "Artificial Intelligence Risk Management Framework (AI RMF 1.0)."** **2023년 1월** · DOI **10.6028/NIST.AI.100-1** (PDF 원문 직접 판독)

**확인 결과 — 결론부터.** **AI RMF 1.0은 자율성에 대해 이산적 등급이나 계층을 정의하지 않는다.** 자율성은 정의적 속성으로 한 번 언급될 뿐이다:
> "**AI systems are designed to operate with varying levels of autonomy** (Adapted from: **OECD Recommendation on AI:2019; ISO/IEC 22989:2022**)."

프레임워크 본체는 **GOVERN / MAP / MEASURE / MANAGE** 4기능이며, 인간-AI 상호작용은 Appendix C에서 다뤄지지만 **등급 체계는 아니다.** 신뢰성 특성 7가지에도 자율성은 없다. 갱신 계획: "**a review with formal input from the AI community is expected to take place no later than 2028.**"

> **★ 이 책에 쓸 수 있는 부분 — 이 책의 존재 이유 그 자체.**
> **"세계에서 가장 널리 참조되는 AI 위험 관리 표준에는 자율성 등급표가 없다."** NIST는 자율성을 "varying levels"라고 **인정만 하고 눈금을 제공하지 않는다.** 그 빈칸을 각 조직이 스스로 채워야 하며 — 실제로 A-2-3의 ExxonMobil 팀이 한 일이 정확히 그것이다(자사 프레임워크를 "developed on the foundation of the **NIST AI Risk Management Framework (NIST 2023)**"라고 명시하면서 **자율성 등급을 추가로 신설**). **이 서사는 그대로 이 책의 한 장이 된다.**
>
> **한계:** 자발적 프레임워크이며 집행력이 없다. **2023년 1월 문서로 에이전틱 AI 이전 시대의 산물이다**(A-2-3 저자들도 "it needs to be updated to accommodate recent advances in Agentic AI"라고 지적).

---

### A-2-13. ★ in / on / out-of-the-loop의 **기원 확인**

의뢰서가 지정한 "DoD Directive 3000.09인가 ICRC/HRW인가"를 직접 확인했다.

**★ 확인된 사실 — HRW 보고서가 이 삼분법을 정의한다.** `[WP]`
> **Human Rights Watch, "Losing Humanity: The Case against Killer Robots."** **2012년 11월 19일 발행.**
> https://www.hrw.org/report/2012/11/19/losing-humanity/case-against-killer-robots

| 용어 | 원문 정의 (VERBATIM) | 한국어 역 |
|---|---|---|
| **Human-in-the-Loop Weapons** | "Robots that can select targets and deliver force **only with a human command**" | 인간의 명령이 있을 때에만 표적을 선정하고 무력을 행사할 수 있는 로봇 |
| **Human-on-the-Loop Weapons** | "Robots that can select targets and deliver force **under the oversight of a human operator who can override the robots' actions**" | 로봇의 행위를 무효화할 수 있는 인간 운용자의 감독 하에 표적을 선정·행사할 수 있는 로봇 |
| **Human-out-of-the-Loop Weapons** | "Robots that are capable of selecting targets and delivering force **without any human input or interaction**" | 어떠한 인간의 입력이나 상호작용 없이 표적을 선정·행사할 수 있는 로봇 |

**귀속 확인.** 이 보고서는 **해당 용어들을 미 국방부 Directive 3000.09에 귀속시키지 않는다.** 보고서 자체가 이 분류 체계를 제시·정립하는 형태다.

**학술 인용 관행 확인.** Engin & Hand(2026, A-2-10)는 본문에서 "technical models distinguish between 'human-in-the-loop' and 'human-out-of-the-loop' architectures (**Docherty, 2012**)"라고 쓴다. **Bonnie Docherty는 "Losing Humanity" 보고서의 저자다.** 즉 **2026년 AI 거버넌스 학술 문헌이 이 삼분법의 출처로 HRW 2012 보고서를 인용하고 있다는 것이 직접 확인된다.**

> **★ 이 책에 쓸 수 있는 부분 — 그리고 반드시 붙여야 할 경고.**
> 1. 확인된 사실만으로도 서술은 충분히 강하다: **"우리가 회의실에서 아무렇지 않게 쓰는 '휴먼 인 더 루프'라는 말은, 2012년 자율살상무기 금지를 주장한 인권 보고서에서 정의된 용어다."** 이 계보의 낙차 자체가 좋은 챕터 오프닝이다.
> 2. **주의:** 원 정의는 **"표적을 선정하고 무력을 행사한다(select targets and deliver force)"**를 전제한다. 즉 이 삼분법은 애초에 **비가역적·치명적 행위**를 다루려고 만든 눈금이다. 사무 자동화에 그대로 쓰면 **눈금이 지나치게 거칠어진다.** 이 점을 지적하면서 A-2-3의 5단계로 넘어가는 구성이 자연스럽다.
> 3. ⚠️ **DoDD 3000.09 기원설은 이번 조사에서 확인하지 못했으므로 책에 단정 서술하면 안 된다.** 확인된 HRW 계보로 쓰거나 원문 확인 후 쓰라. → F절.

---

### ★ A-2 계보 단절 — 이 책이 메울 수 있는 빈칸

**직접 확인한 사실 (2026-09-05 기준).** arXiv API에서 `Sheridan` + `levels of automation` + `large language model`을 모두 포함하는 논문 검색 결과는 **0건**이었다. 고전 계보를 명시적으로 잇는 LLM 에이전트 논문은 **매우 드물다.** 확인된 직접 연결은 **2건뿐**이다:

1. **Zheng et al. 2026 (arXiv:2607.23438)** → **Sheridan & Verplank 1978 직접 인용**
2. **Engin & Hand 2026 (arXiv:2505.11579v3)** → **Parasuraman et al. 2000 직접 인용**

반면 **A-2-5(GAL)와 A-2-4(Data Agents)는 SAE만 인용하고 Sheridan은 인용하지 않는다.**

> **★ 이 희소성 자체가 서술 소재다.** "1978년에 이미 정리된 자동화 등급 이론이 있는데, 2020년대 AI 에이전트 논의는 그 유산을 거의 참조하지 않고 **자율주행 등급만 베끼고 있다.**" 그리고 자율주행 등급은 **1차원**이고 1978~2000년 계보는 **2차원**이다(A-1 정리표). **이 책이 그 단절을 지적하고 다리를 놓으면 실질적 기여가 된다.**

**보너스 — 로봇공학 쪽 중간 다리** `[PR]`
> Jenay M. Beer, Arthur D. Fisk, Wendy A. Rogers. "**Toward a Framework for Levels of Robot Autonomy in Human-Robot Interaction**." *Journal of Human-Robot Interaction*, **3(2)**, **2014년 6월**. DOI **10.5898/JHRI.3.2.Beer**. 피인용 **613회**. Open Access.
> — Sheridan 위에 자율성 등급 분류를 세운 HRI 분야 대표작. 계보 서술의 중간 고리로 유용하다.

---
## A-3. 자율주행 등급의 유비 — 유효한 계보인가, 그리고 그 한계

> **★ 이 절의 결론을 먼저 말한다.** 서로 다른 연구팀이, 서로 다른 방법(테스트트랙 실험 · 129편 메타분석 · 시뮬레이터 · 전문가 인터뷰 · 결함조사 · 사고조사)으로 **"중간 등급을 안전하게 만드는 조건"을 각자 도출했더니, 그 조건들이 하나같이 중간 등급의 편익을 상쇄하거나 소멸시킨다**는 데로 수렴했다. 이것이 "중간 등급이 가장 위험하다"의 가장 강한 형태다 — **중간 등급이 나쁘다는 것이 아니라, 중간 등급을 안전하게 만들면 그것은 더 이상 중간 등급이 아니다.**
>
> 그리고 이것은 1차에서 확보한 **Skitka(1999) 자동화 편향("거의 항상 맞는 시스템이 가장 위험")과 같은 결론에 완전히 다른 경로로 도달한다.**

---

### A-3-1. SAE J3016 — 정본 서지와 L0–L5 정의

**정본 서지 (확인 완료)**

| 항목 | 내용 |
|---|---|
| 문서번호 | **J3016™ APR2021** (온라인 식별자 `J3016_202104`, 개정 코드 **J3016C**) |
| 정식 명칭 | *(R) Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles* |
| 문서 종류 | **SURFACE VEHICLE RECOMMENDED PRACTICE** — **표준이 아니라 "권고 실무"다. 중요한 구분.** |
| 최초 발행 | Issued **2014-01** (2014-01-16) |
| 현행 개정 | Revised **2021-04** (2021-04-30), Superseding J3016 JUN2018 |
| 개정 이력 | 202104(Latest) ← 201806 ← 201609 ← 201401(Issued) |
| 발행 위원회 | **On-Road Automated Driving (ORAD) Committee**, SAE International |
| 분량 | 41쪽 |
| 국제 정합 | SAE ORAD ↔ **ISO TC204/WG14** 합동 작업반(2018년 결성) 공동 개정 |
| 태그 | **[WP]** |

**2026년 현재도 202104가 현행인가?** 두 갈래로 확인했다.
1. SAE 자신의 개정 이력 표에 `J3016_202104 / 2021-04-30 / **Latest**` 표기.
2. **미 연방관보 전문 검색 결과, 2026-07-31자 NHTSA 고시(91 FR 48494, Zoox 임시 면제 승인)**가 각주에서 April 2021판을 원용한다 — 즉 **2026년 7월 시점 미 규제당국이 참조하는 판본이 여전히 April 2021이다.**
> "For purposes of this Grant Notice, the term Automated Driving System and the abbreviation ``ADS'' are used as defined in SAE International J3016… (**April 2021**)…" — NHTSA, 91 FR 48494 (2026-07-31)

**★ L0–L5 정의표 (J3016 APR2021 §5 및 Table 1 — VERBATIM)**

| Lv | 명칭 | 서술적 정의 (verbatim, §5) | 지속적 횡·종방향 운동제어 | OEDR | **DDT 폴백** | ODD |
|---|---|---|---|---|---|---|
| **0** | No Driving Automation | "The performance by the driver of the entire DDT, even when enhanced by active safety systems." | Driver | Driver | **Driver** | n/a |
| **1** | Driver Assistance | "The sustained and ODD-specific execution by a driving automation system of **either the lateral or the longitudinal** vehicle motion control subtask of the DDT (but not both simultaneously) with the expectation that the driver performs the remainder of the DDT." | Driver **and** System | Driver | **Driver** | Limited |
| **2** | Partial Driving Automation | "The sustained and ODD-specific execution by a driving automation system of **both the lateral and longitudinal** vehicle motion control subtasks of the DDT with the expectation that **the driver completes the OEDR subtask and supervises** the driving automation system." | System | **Driver** | **Driver** | Limited |
| **3** | Conditional Driving Automation | "The sustained and ODD-specific performance by an ADS of **the entire DDT under routine/normal operation** with the expectation that **the DDT fallback-ready user is receptive to ADS-issued requests to intervene**, as well as to DDT performance-relevant system failures in other vehicle systems, **and will respond appropriately**." | System | System | **Fallback-ready user** | Limited |
| **4** | High Driving Automation | "The sustained and ODD-specific performance by an ADS of **the entire DDT and DDT fallback**." (Table 1 판: "…**without any expectation that a user will need to intervene**.") | System | System | **System** | Limited |
| **5** | Full Driving Automation | "The sustained and **unconditional (i.e., not ODD-specific)** performance by an ADS of the entire DDT and DDT fallback." | System | System | **System** | **Unlimited** |

*(주: §5.4의 L3 정의에는 "under routine/normal operation (see 3.27)"이 들어 있으나 Table 1의 L3 서술 정의에는 이 구절이 없다. §5.5·5.6과 Table 1의 L4·L5 문구도 미묘하게 다르다 — **인용 시 어느 쪽을 쓰는지 밝히는 편이 안전하다.**)*

**경계에서 실제로 갈리는 것 (각 경계의 판별식)**

| 경계 | 갈리는 것 | 원문 근거 |
|---|---|---|
| **L0→L1** | 시스템이 DDT의 일부를 **지속적으로** 수행 시작 (순간적 개입인 AEB·ESC는 등급 밖) | §1 Scope: active safety systems는 "momentary intervention"이므로 제외 |
| **L1→L2** | 횡·종방향 제어를 **동시에** 수행 | §5.2 vs §5.3 |
| **★ L2→L3** | **OEDR과 감시(supervise)의 주체가 운전자→시스템으로 이동.** 운전자는 "감시자"에서 "폴백 대기자"로 신분이 바뀜 | §5.3 vs §5.4 NOTE 2 |
| **★ L3→L4** | **DDT 폴백의 주체.** L4는 사용자가 응답하지 않아도 시스템이 스스로 최소위험상태(MRC) 달성 | §5.5 NOTE 1 |
| **L4→L5** | ODD 제한의 유무 | §5.6 NOTE 1 |

**★ L3→L4 경계 — SAE 자신의 정의 (VERBATIM, §5.5 NOTE 1)**
> "The user does not need to supervise a Level 4 ADS feature or be receptive to a request to intervene while the ADS is engaged. A Level 4 ADS is capable of automatically performing DDT fallback, as well as achieving a minimal risk condition if a user does not resume performance of the DDT. **This automated DDT fallback and minimal risk condition achievement capability is the primary difference between Level 4 and Level 3 ADS features.** This means that an in-vehicle user of an engaged Level 4 ADS feature is a passenger who need not respond to DDT performance-relevant system failures."

**L3 운전자의 신분 — "DDT fallback-ready user" 공식 정의 (VERBATIM, §3.31.3)**
> "The user of a vehicle equipped with an engaged Level 3 ADS feature who is **properly qualified and able to operate the vehicle** and **is receptive to ADS-issued requests to intervene** and to evident DDT performance-relevant system failures in the vehicle compelling him or her to perform the DDT fallback."
> NOTE 1: "**DDT performance by a Level 3 ADS assumes that a fallback-ready user is available to perform the DDT as required. There is no such assumption at Levels 4 and 5.**"
> NOTE 2: "A DDT fallback-ready user who transitions to performing part or all of the DDT **becomes a driver**."

**★★ "수용성(receptivity)" 공식 정의 (VERBATIM, §3.22) — 이 절에서 가장 중요할 수 있는 문장**
> "**An aspect of consciousness characterized by a person's ability to reliably and appropriately focus his/her attention in response to a stimulus.**"
> ("**의식의 한 측면**으로, 자극에 반응하여 자신의 주의를 신뢰할 수 있고 적절하게 집중시킬 수 있는 능력.")

> **★ 이 책에 쓸 수 있는 부분 — 논증의 급소.**
> **L3 전체가 "수용성"이라는, 표준이 스스로 '의식의 한 측면'이라고 부른 심리 상태 위에 얹혀 있다.** 공학 표준이 시스템 요구사항을 **인간의 의식 상태에 의존시킨 것**이다. 그런데 표준은 그 상태를 어떻게 달성·측정·보증하는지는 규정하지 않는다(§8.1이 명시하듯 이 문서는 "does not provide specifications, or otherwise impose requirements").
> **AX 번역:** "휴먼 인 더 루프"를 통제 수단으로 적어놓고 **그 사람이 실제로 주의를 유지하는 조건은 설계하지 않는 것**과 똑같은 결함이다.

**★ "충분한 시간" 조항 (VERBATIM, §5.4 NOTE 4) — 뒤의 실증과 정면충돌하는 지점**
> "In the event of a DDT performance-relevant system failure in a Level 3 ADS, or in the event that the ADS exits its ODD, the ADS will issue a request to intervene **within sufficient time** for the fallback-ready user (whether in-vehicle or remote) to respond appropriately."

> **표준은 "충분한 시간(sufficient time)"이라고만 쓰고 초 단위를 규정하지 않는다.** A-3-2 이하의 실증 자료 전체가 바로 이 빈칸을 향한 공격이다.

**★ "역할"의 정의 (VERBATIM) — 표준이 스스로 그은 한계선**
> "'Role' in this context refers to **the expected role of a given primary actor, based on the design** of the driving automation system in question **and not necessarily to the actual performance** of a given primary actor. For example, **a driver who fails to monitor the roadway during engagement of a Level 1 adaptive cruise control (ACC) system still has the role of driver, even while s/he is neglecting it.**"

> **★ 이 책에 쓸 수 있는 부분.** J3016은 **역할을 "설계상 기대치"로 정의하고, 실제 인간이 그 역할을 수행하는지 여부를 정의 밖으로 밀어냈다**고 스스로 명시한다. 즉 표준 자체가 **"사람이 이 역할을 실제로 해낼 수 있는가"라는 질문에 답하지 않겠다고 선언**한 것이다. 중간 등급의 위험은 바로 이 **설계상 기대치와 실제 인간 수행 사이의 간극**에 고여 있고, 표준은 구조적으로 그 간극을 보지 않는다.
> **AX 번역:** "사람이 최종 검토한다"고 적어둔 RACI 문서가 **실제 검토 행위를 보장하지 않는 것**과 정확히 같은 구조다.

**등급이 붙는 대상 (VERBATIM) — AX 등급 설계에 그대로 빌려올 원칙**
> "**The levels apply to the driving automation feature(s) that are engaged in any given instance of on-road operation of an equipped vehicle.** As such, although a given vehicle may be equipped with a driving automation system that is capable of delivering multiple driving automation features that perform at different levels, **the level of driving automation exhibited in any given instance is determined by the feature(s) that are engaged.**"
> → **등급은 시스템이 아니라 "지금 켜져 있는 기능"에 붙는다.** AX 등급표를 "이 에이전트는 3단계"가 아니라 **"이 워크플로에서 지금 켜진 기능이 3단계"**로 쓰라는 근거.

---

### A-3-2. ★ SAE 자신의 공식 분할 — L0-2 / L3-5, 그리고 홀로 남는 L3

**출처:** *SAE J3016™ LEVELS OF DRIVING AUTOMATION™* 요약표, Copyright © 2021 SAE International, `sae-j3016-visual-chart_5.3.21.pdf` (2021-05-03 갱신본). **[WP]**
> ※ **SAE가 "출처를 밝히면 AS-IS로 자유롭게 복사·배포 가능"하다고 명시한 자료다:** "The summary table may be freely copied and distributed AS-IS provided that SAE International is acknowledged as the source of the content." → **책에 그대로 실을 수 있다.**

| | **SAE LEVEL 0 / 1 / 2** | **SAE LEVEL 3 / 4 / 5** |
|---|---|---|
| 분류명 | "These are **driver support features**" | "These are **automated driving features**" |
| 운전석의 인간이 해야 할 일 | "**You are driving** whenever these driver support features are engaged – **even if your feet are off the pedals and you are not steering**" / "**You must constantly supervise these support features; you must steer, brake or accelerate as needed to maintain safety**" | "**You are not driving** when these automated driving features are engaged – **even if you are seated in 'the driver's seat'**" |
| L3만의 단서 | — | (L3) "**When the feature requests, you must drive**" · (L4·L5) "These automated driving features **will not require you to take over driving**" |

**표준 본문의 같은 분할 (VERBATIM, §5 서두)**
> "The lower two levels of driving automation (1 and 2) refer to cases in which **the (human) driver continues to perform part of the DDT** while the driving automation system is engaged. These are therefore referred to as '**driver support**' features."
> "The upper three levels of driving automation (3 to 5) refer to cases in which **the automated driving system (ADS) performs the entire DDT** on a sustained basis while it is engaged. These are therefore referred to as '**automated driving**' features."

> **★ 이 책에 쓸 수 있는 부분 — 논증의 시각적 중심축.**
> SAE의 공식 요약표는 6개 등급을 **2 대 3으로 쪼개고, L3에만 예외 딱지를 붙인다.** L0–L2는 "당신이 운전 중", L4–L5는 "당신은 운전 중이 아니며 인계 요구도 없음"으로 깔끔하게 갈리는데, **L3만 홀로 "당신은 운전 중이 아니지만, 요청이 오면 운전해야 한다"는 조건부 상태**에 놓인다.
> 즉 **SAE 자신의 커뮤니케이션 자료에서조차 L3는 두 세계 어디에도 온전히 속하지 않는 유일한 칸이다.** "중간 등급이 가장 위험하다"는 주장은 표준 반대편에서 던지는 비판이 아니라, **표준 자신의 구조가 이미 드러내고 있는 봉합선**을 지적하는 것이다.
>
> **★ AX 번역:** 자동화 등급을 설계할 때 **"사람이 상시 감독한다"(L0–2형)와 "사람이 개입할 필요가 없다"(L4–5형)는 각각 일관된 설계**다. 그러나 **"평소엔 손 떼도 되지만 부르면 즉시 들어와야 한다"(L3형)는 두 설계의 최악의 조합**이다 — **감독의 부담은 없애고 개입의 책임만 남기기 때문이다.**

---

### A-3-3. ★ Eriksson & Stanton (2017) — 인계 시간의 실측과 **13배의 분산**

**서지**
> Alexander Eriksson & Neville A. Stanton. "**Takeover Time in Highly Automated Vehicles: Noncritical Transitions to and From Manual Control**." *Human Factors*, **59(4), 689–705**. 온라인 선공개 **2017-01-26**, 인쇄 2017년 6월호.
> DOI: **10.1177/0018720816685832** · PMID 28124573 · **[PR]**
> *원문 확보: University of Southampton 기관 리포지토리 승인원고(eprint 403717)*

**핵심 주장.** 기존 인계 연구는 거의 전부 **긴급 상황**만 다뤘고, 정작 훨씬 자주 일어날 **비긴급 인계**는 연구 공백이었다. 비긴급 상황에서 재보니 **인계 시간이 문헌 보고치보다 실질적으로 더 길었고, 무엇보다 분산이 압도적으로 컸다.**

**★ 인용 가능한 수치 — 전부 VERBATIM, 반올림 없음**

*(A) 25편 문헌 리뷰*
> "...with times varying from **0-30 seconds for TORlt** and **1.14-15 seconds for TOrt** as shown in Table 1. A total of **25 papers** reported either TORlt, or TOrt and were included in the review."
> "The review showed that the mean TORlt was **6.37±5.36 seconds** with a mean reaction time of **2.96±1.96 seconds**."

*(TORlt = Take-Over-Request lead time / TOrt = Take Over reaction time)*

*(B) 자체 실험* — 참가자 **26명**(여 10, 남 16), 연령 20–52세, **M = 30.27, SD = 8.52**, 평균 운전경력 10.57년(SD = 8.61), 시뮬레이터, 요청 간격 30–45초, 약 24회 전환
> "The results showed a significant increase in control transition time of **~1.5 seconds** when drivers were prompted to resume control whilst engaged in a secondary task (**Z = -4.43, p < 0.01, r = 0.86**). It took drivers approximately **4.46±1.63 seconds** to resume control when not occupied by a secondary task, and **6.06±2.39 seconds** to resume control when engaged in a secondary task"

*(C) Table 2 원표 — 밀리초 단위*

| | 문헌 메타리뷰 | 자동→수동, **부차과제 없음** | 자동→수동, **부차과제 있음** |
|---|---|---|---|
| Median | 2470 ms | **4567 ms** | **6061 ms** |
| IQR | 1415 ms | 1632 ms | 2393 ms |
| **Min** | 1140 ms | **1975 ms** | **3179 ms** |
| **Max** | 15000 ms | **25750 ms** | **20994 ms** |

*(D) ★ 결론부 — 이 책의 핵심 인용문*
> "When subjecting drivers to TOR's without time restrictions we found that drivers take between **1.97-25.75 seconds (Median = 4.56)** to resume control from automated driving in normal conditions, and between **3.17-20.99 seconds (Median = 6.06)** to do so whilst engaged in a secondary task preceding the control transition."
> "It is clear from Figure 7 that **designing for the median, or average driver effectively exclude a large part of the user group**, which could have severe implications for drivers who fall outside of the mean or median."
> "**there is a large spread in the TOrt, which when designing driving automation should be considered, as the range of performance is more important than the median or mean, as these exclude a large portion of drivers.**"
> "designers of automated vehicles **should not focus on the mean, or median, driver** when it comes to control transition times."

*(E) 저자들의 처방 — A-3-8과 연결*
> "In light of these results, **there is a case for 'adaptive automation' that modulates TORlt** by, for example, detecting whether the driver gaze is off road for a certain time-period, providing the driver with a few additional seconds before resuming control."

> **★ 이 책에 쓸 수 있는 부분.**
> 이 논문의 진짜 발견은 "평균이 4.5초다"가 아니라 **"최소 1.97초와 최대 25.75초가 같은 실험, 같은 26명 안에 공존한다"**는 것이다. **13배 차이다.**
> L3 설계자는 "충분한 시간"을 정해야 하는데, **25.75초를 보장하면 L3의 실용적 가치가 사라지고, 평균 4.5초로 잡으면 사용자군의 상당 부분이 구조적으로 배제된다.** **어느 쪽을 택해도 L3는 자기모순에 빠진다.** 반면 L2(상시 감독)와 L4(개입 불필요)는 이 딜레마 자체가 없다 — **인계 시간이라는 변수가 안전 경로에 아예 등장하지 않기 때문이다.**
>
> **★ AX 번역:** "사람이 개입할 시간을 X분 준다"는 SLA를 설계할 때, **평균 응답 시간이 아니라 분포의 꼬리로 설계해야 한다.** 그리고 꼬리로 설계했더니 자동화의 이득이 사라진다면, 그 구간은 **애초에 사람 개입을 전제하지 않는 설계로 가거나, 사람이 계속 붙어 있는 설계로 되돌리는 것**이 옳다. **중간은 없다.**

**한계·반박**
- 고정형 시뮬레이터 연구이며 실도로 위험 인식이 낮아 반응이 느려졌을 가능성.
- 참가자 26명, 평균 연령 30.27세로 **젊은 편향.** 고령 운전자 대표성 부족.
- **비긴급 조건이 설계상 의도된 것**이므로 "긴급 상황에서도 25초 걸린다"로 확대 인용하면 오독이다. 저자들도 "suboptimal responses are acceptable in emergencies"라고 명시적으로 구분한다.
- ⚠️ **원문 내부 불일치:** 본문은 "4.46±1.63 seconds"라고 쓰지만 Table 2 중앙값은 4567 ms, 결론부는 "Median = 4.56"이다. 또 ±값은 SD가 아니라 **IQR**로 표기되어 있다. **인용 시 "중앙값 4.56초, IQR 1.63초"로 쓰는 편이 정확하다.**
- ⚠️ **이 논문 자체의 사실 오류 하나:** 서론에서 Tesla Autopilot을 "**conditional driving automation (SAE Level 3**)"로 서술하는데, **Autopilot은 SAE Level 2다**(NHTSA·NTSB 공식 분류 및 Tesla 자신의 분류). **이 문장은 인용하지 말 것.**

---

### A-3-4. ★ Zhang et al. (2019) — 129편 메타분석

**서지**
> Bo Zhang, Joost de Winter, Silvia Varotto, Riender Happee, & **Marieke Martens**. "**Determinants of take-over time from automated driving: A meta-analysis of 129 studies**." *Transportation Research Part F*, **64, 285–307**. 온라인 2019-05-31, 발행 2019년 7월.
> DOI: **10.1016/j.trf.2019.04.020** · **[PR]**
> ⚠️ Semantic Scholar의 저자 목록에 **오류**가 있다(제5저자를 "Brady Michael Kuhl"로 표기). **Crossref·TU Delft·U Twente 및 원문 PDF 모두 Marieke Martens로 확인.**

**표본.** **129개 연구** / 119개 레코드가 포함 기준 충족 / **520개** 평균·중앙값 TOT 관측치. 발행연도 2000–2018, 그중 **116/129가 2015년 이후.**

**★ 인용 가능한 수치 — 전부 VERBATIM**

*(A) 통합 추정치*
> "**The mean TOT across studies and conditions ranged from 0.69 s to 19.79 s, and the average mean TOT was 2.72 s (SD = 1.45, n = 520).**"

*(B) 조절변수별 평균 차이 D (초)*
- 시간 예산(큰 예산 vs 작은 예산): "**average D = 1.35 s**" — **예산이 클수록 느려짐**
- 2회차 인계 vs 1회차: "**average D = 1.00 s**"
- **핸드헬드 기기 사용**: "The use of a handheld device **strongly increased** the mean TOT (**average D = 1.33 s**)"
- 핸즈프리 시각적 비운전과제 vs 과제 없음: "**average D = 0.29 s**"
- TOR 제공 vs 미제공: "**average D = 0.58 s**"
- 눈을 감고 있다가 인계: "**average D = 1.19 s**"
- 청각 TOR vs 시각전용: "**average D = 1.41**", 진동촉각 TOR vs 시각전용: "**1.41 s**"

*(C) ★ 평균과 분산의 강한 상관*
> "a strong association (**r = 0.82; ρ = 0.73, n = 397**)" → "the mean and standard deviation of the take-over time were highly correlated, **indicating that the mean is predictive of variability**"

*(D) 선형혼합효과모형*
> 기저 평균 TOT: "**average baseline TOT = 2.15 s**". 조건별: **Hand=1 → 2.71 s** / **URG_Low=1 → 3.43 s** / URG_Med=1 → **2.75 s** / IRU=1 → **2.58 s**
> 오차항: 연구 간 분산 σ = **0.1357** (Wald-Z = 6.89, p = 5.40 × 10⁻¹²), 관측 간 분산 = **0.0375** (Wald-Z = 13.73, p = 6.73 × 10⁻⁴³)

*(E) ★ 결론부 — 설계 함의*
> "**our meta-analysis suggests that achieving a low mean TOT should not necessarily be a design target.** We showed that **drivers take more time (i.e., the mean TOT is higher) when they have more time (i.e., when the urgency is lower).** Future engineering efforts should be directed towards **ensuring that drivers actually have sufficient time**…"
> "…**drivers should not be permitted to engage in handheld non-driving tasks if take-over situations can be urgent.**"

> **★ 이 책에 쓸 수 있는 부분 — 세 가지가 결정적이다.**
> **① 평균이 아니라 꼬리가 문제다.** 129개 연구를 다 모아도 평균은 2.72초로 안심스러워 보이지만, **개별 연구의 평균만 놓고도 0.69초에서 19.79초까지** 벌어진다. 그리고 저자들은 **평균과 표준편차가 r = 0.82로 강하게 상관**한다는 것을 보였다 — **느린 인계는 곧 예측 불가능한 인계**라는 뜻이다.
> **② 시간을 더 주면 사람은 더 늦게 온다.** "drivers take more time when they have more time" — **여유를 늘려도 안전 마진이 그만큼 늘지 않는다.** 인간의 인계 시간은 **시스템이 주는 예산에 맞춰 팽창한다.** 이것은 L3의 근본 설계 가정("리드타임을 충분히 주면 안전하다")을 **직접 반박한다.**
> **③ 손에 뭔가 들고 있으면 1.33초가 추가된다. 그런데 L3의 상업적 매력은 정확히 "손에 뭔가 들 수 있다"는 것이다.** **L3가 파는 편익이 곧 L3를 위험하게 만드는 변수다.** 저자들의 처방을 문자 그대로 적용하면 **L3의 상품성 자체가 소멸한다.**
>
> **★ AX 번역:** "AI가 처리하고, 이상하면 사람이 개입한다"는 체계를 만들 때, 사람에게 **다른 일을 할 자유를 주는 것**과 **빠른 개입을 요구하는 것**은 **양립 불가능한 요구**다. 둘 중 하나를 포기해야 하고, 포기하지 않으면 그 자유가 **개입 지연으로 정확히 환산되어** 돌아온다.

**한계·반박 (저자 자신이 명시한 것들)**
> "**nearly all included studies were conducted in a driving simulator.** … the driver's level of perceived risk perception may be low in simulators… which could **discourage a fast take-over response**. While the TOTs measured in simulator studies may not accurately reflect the numeric values… **the results may still be valid concerning the direction of the effects.**"
> ★ **가장 무서운 한계:** "if a participant would **not react at all** (which sometimes happened...), **their results were not taken into account** in the reported mean TOT, which would **underestimate** the mean TOT." — **"아예 반응하지 않은 사람"이 평균에서 빠져 있다.**
- 숨은 조절변수 존재 가능(주행 속도, TOR 강도, 피로·음주 등). 연구 내 분석의 D는 **4~17개 연구**에 기반해 표본이 얇다. TOT 조작적 정의가 연구마다 다르다.

---

### A-3-5. ★★ Merat et al. (2014) — "제어 회복까지 35–40초"

**이 절에서 가장 강력한 단일 대비를 만들어낸다.**

**서지**
> Natasha Merat, A. Hamish Jamson, Frank C. H. Lai, Michael Daly, & Oliver M. J. Carsten. "**Transition to manual: Driver behaviour when resuming control from a highly automated vehicle**." *Transportation Research Part F*, **27(Part B), 274–282**. 온라인 **2014-10-16**.
> DOI: **10.1016/j.trf.2014.09.005** · **[PR]** · **오픈액세스 (CC BY-NC-ND 3.0)**

**설계.** 리즈대 모션 기반 시뮬레이터. 46명 참가, 결측으로 **37명 분석.** 연령 28–67세, **Mean = 47.35, SD = 10.33.** 전원 10년 이상 운전경력, 연평균 주행 **27,207 마일 (SD = 20,790 마일).** 25분 연습.

**★ 인용 가능한 수치 — VERBATIM**
> **"Whether automation transition to manual was based on a fixed or variable interval, it took drivers around 35–40 s to stabilise their lateral control of the vehicle."** (초록)
> "Both lateral driving measures and eye fixations showed a **10–15 s lag time** between disengagement of the automation and resumption of control by the driver. For these measures, initial large values at around 15 s after transfer of control lead to a more stabilised value **after around 35–40 s**."
> "it took drivers around **15–20 s** to refocus their attention back towards the road centre" (변동 조건)
> "this visual attention continued to be erratic for **up to 40 s** after the transfer of control"
> "Following a dramatic rise in the number of corrections after 10 s, they are seen to **stabilize after around 35–40 s**. Therefore, whether control was passed to drivers after a Fixed or Variable time, **it took around 10 s for drivers to resume control** and this was seen by an exaggeration in steering corrections in the next 10–15 s, which then steadied after around 35–40 s."
> 통계: 조향 수정 횟수 Drive 주효과 **F(1, 23) = 45.45, p < .0001, η² = .66**; Time 주효과 **F(11, 253) = 25.45, p < .0001, η² = .52**; 상호작용 **F(11, 253) = 3.68, p < .0001, η² = .14**. SDLP Time 효과 **F(11, 209) = 17.88, p < .0001**, "SDLP was much lower for the first 10 s, before equalizing to between **0.1 and 0.2 m**".

**★ 결론부 — L3를 명시적으로 지목한다**
> "The results of this study indicate that **if drivers are out of the loop due to control of the vehicle in a limited self-driving situation (Level 3 automation), their ability to regain control of the vehicle is better if they are expecting automation to be switched off.** As **regular disengagement of automation is not a particularly practical method for keeping drivers in the loop**, future research should consider how to best inform drivers of their obligation to resume control…"
> "Further research… is also needed to consider how **the 30–40 s needed to resume adequate control of driving** affects drivers' situation awareness…"
> "This study also suggests that **drivers require around 40 s to resume adequate and stable control of driving from automation**, which might be considered a 'comfortable transition time' as stipulated by the NHTSA guidelines on Level 3 automation (NHTSA, 2013)."

> **★★ 이 책에 쓸 수 있는 부분 — 가장 강력한 단일 대비.**
> 이 논문이 다른 인계 연구와 결정적으로 다른 점은 **"제어를 되찾은 시점"과 "제어가 안정된 시점"을 분리했다**는 것이다. 손이 핸들로 돌아오는 데는 **10초**, 그러나 조향이 안정되고 차선 유지가 정상 수준으로 돌아오는 데는 **35–40초**가 걸린다. **그 사이 25–30초 동안 운전자는 "운전 중"이지만 "제대로 운전 중"은 아니다.**
>
> **세 문헌을 나란히 놓으면 논증이 완성된다:**
> - **SAE J3016 §5.4 NOTE 4:** ADS는 "**within sufficient time**"에 개입 요청을 발령한다 (초 단위 미규정)
> - **Zhang et al. 2019:** 실측 인계 시간 평균 **2.72초**, 개별 연구 평균 범위 **0.69–19.79초**
> - **Merat et al. 2014:** 안정적 제어 회복에 **35–40초**
>
> 즉 업계가 "인계 시간"이라 부르며 최적화해온 2~7초는 **핸들을 잡는 시간**일 뿐, **판단할 수 있는 상태가 되는 시간이 아니다.** L3의 안전 논증은 이 두 가지를 혼동한 위에 서 있다.
>
> **★ AX 번역:** AI 파이프라인에서 **"사람이 이어받았다"는 이벤트가 로그에 찍히는 순간과, 그 사람이 실제로 맥락을 파악하고 판단할 수 있게 되는 순간은 다르다. 후자는 전자보다 3~4배 길다.** 인수인계 SLA를 로그 타임스탬프로 측정하면, **측정되지 않는 곳에 위험이 전부 쌓인다.**

**한계·반박**
- 고사양이지만 **시뮬레이터** 연구. **46명 모집, 12명 결측으로 37명만 분석** — 결측률 26%로 높다.
- 참가자 평균 연령 47.35세, 연평균 27,207마일의 **고주행 숙련 운전자** 편향.
- 자동화 해제가 **경고(TOR) 없이** 이루어진 조건이 포함되어 실제 L3 시스템보다 회복이 느렸을 수 있다(Eriksson & Stanton 2017이 이 점을 지적).
- 분석 구간이 인계 후 1분으로 한정(다만 저자들은 "the same pattern was seen for consequent 60 s periods"라고 보고).
- SDLP 자체는 두 조건 간 유의차가 없었다(**F = 1.39**). 유의한 것은 **시간 효과와 조향 수정 횟수**다 — **인용 시 "고정 vs 변동 조건 차이"와 "인계 후 시간 경과 효과"를 혼동하지 말 것.**
- ⚠️ 권 표기: 확보 PDF 헤더는 "Part F **27** (2014) 274–282"이나 일부 DB는 **27(Part B)**로 표기. 표기 통일 필요.

---

### A-3-6. ★★ Victor et al. (2018) — 눈은 위협물에, 손은 핸들에, 그래도 **28% 충돌**

**"감시 지표는 안전을 보장하지 않는다"의 결정적 증거. 시뮬레이터가 아니라 실제 테스트 트랙이다.**

**서지**
> Trent W. Victor, Emma Tivesten, Pär Gustavsson, Joel Johansson, Fredrik Sangberg, & Mikael Ljung Aust. "**Automation Expectation Mismatch: Incorrect Prediction Despite Eyes on Threat and Hands on Wheel**." *Human Factors*, **60(8), 1095–1116**. 온라인 2018-08-10, 2018년 12월호.
> DOI: **10.1177/0018720818788164** · **[PR]** · 저자 소속: **Volvo Cars / Chalmers**

**★ 초록 (VERBATIM) — 이 책에 그대로 쓸 수 있는 4문장**
> "**Background:** Securing driver engagement—by mitigating **irony of automation (i.e., the better the automation, the less attention drivers will pay to traffic and the system, and the less capable they will be to resume control)**—and by communicating system limitations to avoid mental model misconceptions—is a major challenge in the human factors literature."
> "**Method:** **One hundred six drivers** participated in **three test-track experiments**... After 30 min, a conflict occurred wherein the lead vehicle cut out of lane to reveal a conflict object in the form of either a stationary car or a garbage bag."
> "**Results:** Supervision reminders effectively maintained drivers' eyes on path and hands on wheel. However, **neither these reminders nor explicit instructions on system limitations and supervision responsibilities prevented 28% (21/76) of drivers from crashing with their eyes on the conflict object (car or bag).**"
> "**Conclusion:** The results uncover the important role of expectation mismatches, showing that **a key component of driver engagement is cognitive (understanding the need for action), rather than purely visual (looking at the threat), or having hands on wheel.**"
> "**Application: Automation needs to be designed either so that it does not rely on the driver or so that the driver unmistakably understands that it is an assistance system that needs an active driver to lead and share control.**"

**★ 추가 수치 (VERBATIM)**
> "despite explicit and detailed instructions on specific system limitations in risk scenarios, **28% of the drivers still crashed.** As for supervision reminders, **even when drivers both had their eyes on the road and their hands on the wheel, 30% of the drivers still crashed.**"
> (실험 2) "the garbage bag conflict, **where 31% crashed**, was preceded by an unexpected lane drift event 15 min earlier, **where 38% did not intervene.**"
> (실험 3) "**Fifty-two out of the 60 participants (87%) realized the need to intervene** at some moment during the conflict; 8 did not. Of the 16 participants who crashed, the most common response theme (**by 11 participants**) was that **they realized too late** that they needed to intervene"
> (실험 3) "**All of these seven who crashed had their eyes on path toward the target when it actually was visible** prior to the LV cut-out maneuver (**14 s before the conflict point**)."
> **신뢰(trust) 평정:** "The participants in Experiments 2 and 3 rated trust at **4.50 on average (SD = 2.10)**, and **the participants who crashed rated a higher trust (M = 6.24, SD = 0.62) compared with the ones who did not crash (M = 3.84, SD = 2.09).**"
> (실험 1) "Drivers displayed both **extreme visual distraction and sleepiness, with one participant sleeping when the conflict occurred, all within 30 min of driving. This level of inattention during driving has, to our knowledge, never been reported in driving research.** … **In this experiment, we see more than a third of participants with glances over 8 s.**" (통상 최대 시각 산만 기준은 2초)

**★ 핵심 해석 문장 (VERBATIM)**
> "**The novel finding in this study, however, is that looking at the road does not equate to acting upon a threat.** The decision to act in a conflict situation hinges on the belief of whether the driver needs to act or if the car will act to resolve a conflict... **Clearly, looking at the road and the conflict object is not the same as being in the loop, at least not for some drivers.**"
> "**expectations seem to matter so much that some drivers can have their hands on wheel and eyes on threat and still crash because they expect and trust the system to act.**"
> 참가자 발언: "**No I did not do it [intervene] because I trusted the car**," / "**At first I trusted the car. I thought that the car would brake or stop, thus I did not act. Actually I should have braked but when I was going to brake it was too late.**"
> "Until unsupervised autonomous driving exists, **automation is assistance and the driver is not free to disengage from the driving task.**"

> **★★ 이 책에 쓸 수 있는 부분 — 결정적.**
> 이 연구가 특별한 이유는 **"운전자 모니터링"이라는 업계의 표준 처방을 실험적으로 무력화**했다는 점이다. 시선 추적 리마인더는 **작동했다** — 시선은 도로에 있었고 손은 핸들에 있었다. **그런데도 28~30%가 충돌했다.** 즉 **업계가 중간 등급의 안전 담보로 내세우는 모든 관측 가능한 지표(시선·손·경고 응답)를 100% 충족한 상태에서도 3명 중 1명은 실패한다.** 실패한 것은 지표가 아니라 **기대와 신뢰라는, 계측 불가능한 인지 상태**다.
>
> 그리고 **저자들이 내리는 처방이 곧 이 책의 테제다:** *"Automation needs to be designed **either** so that it does not rely on the driver **or** so that the driver unmistakably understands that it is an assistance system that needs an active driver."* — **either/or, 즉 중간은 없다는 선언이다.** **Volvo Cars 소속 연구자들이 최상위 인간공학 저널에 쓴 문장**이라는 점에서 무게가 크다.
>
> **★ AX 번역:** **"사람이 검토했다"는 감사 로그(시선·클릭·타임스탬프)는 실제 검토를 증명하지 못한다.** Victor의 참가자들은 감사 로그 관점에서 완벽했다 — 눈은 화면에, 손은 키보드에. 그럼에도 30%가 실패했다. **AX 거버넌스가 관측 가능한 대리지표(proxy)에 의존하는 한, 그 지표를 만족시키면서 실패하는 경로가 항상 열려 있다.** → **이것은 B-2의 Goodhart·Campbell 논의와 정확히 같은 구조다.**

**한계·반박 (저자가 직접 기술)**
> "These results should be tempered by the experimental limitations. In particular, **the realism, or real-world representativeness, of the experiments is lacking. The drivers knew they were participating in a study, there were test leaders present in the vehicle, they were on a test track without traffic in adjacent lanes, and the stationary balloon car did not look like a real car.** For these reasons, **it is currently not possible to precisely assess whether similar results would appear in naturalistic driving.**"
- 3개 실험의 조건이 서로 달라(교육 수준 저/중/고, 리마인더 유형 3종) **단일 표본 106명의 28%가 아니라 조건별 부분표본(21/76, 16/60 등)**이다. **인용 시 분모를 반드시 밝혀라.**
- 이 연구의 대상은 **L2(감독형 자동화)**이며 L3가 아니다. **L3에 적용할 때는 "L2에서도 이 정도인데 감독 의무마저 없앤 L3에서는"이라는 a fortiori 논법으로만 써야 정확하다.**

---

### A-3-7. ★ Gerber, Schroeter & Ho (2023) — **L3의 자기소멸**을 학계가 정식 진술

**요청받은 "L2–L3 경계에 대한 동료심사 논증"의 가장 직접적인 근거다.**

**서지**
> Markus A. Gerber, Ronald Schroeter, & Beryl Ho. "**A human factors perspective on how to keep SAE Level 3 conditional automated driving safe**." *Transportation Research Interdisciplinary Perspectives*, **22, 100959**, **2023년 11월**.
> DOI: **10.1016/j.trip.2023.100959** · **[PR]** · **골드 오픈액세스** (DOAJ 수록)

**★ 초록 (VERBATIM, DOAJ에서 확보)**
> "The Society of Automotive Engineers (SAE) defines Conditional Automated Driving (CAD) or SAE level 3 as the next step in the transition to higher automated driving. A human factors challenge at this level is to **keep the fallback-ready user aware of the driving situation. The problem with the widely accepted terminology of SAE is that it does not consider the human factors of achieving this safety-critical transition and lacks in defining a required or appropriate state of fallback readiness and how a human reaches this state.** This paper aims to understand how research and industry currently perceive the problem and how they counteract it. We conducted **exploratory expert interviews with N = 15 subject matter experts from universities, research centres and vehicle manufacturers.** ... The results show that **the user should remain physically and sensory in the state of regular drivers to allow a safe transition, which narrows down the problem to maintaining an appropriate cognitive state, level of arousal, and motivational conditions.** Lastly, the experts identify that the **NDRA should be (a) limited to the onboard-entertainment system and (b) context-aware and (temporarily) restricted or interrupted.**"

> **★★ 이 책에 쓸 수 있는 부분 — "중간 등급의 자기소멸"의 학술적 정식화.**
> 전문가 15인이 도달한 결론을 그대로 읽으면 이렇다:
> - **L3가 안전하려면** 사용자가 **"일반 운전자와 같은 물리적·감각적 상태"**에 머물러야 하고, 비운전 활동은 **인포테인먼트로 제한**되며 **맥락에 따라 중단**되어야 한다.
> - **그런데 "일반 운전자와 같은 상태에 머물러 있고, 다른 일은 제한된다"면 그것은 사실상 L2다.**
> - **즉, L3를 안전하게 만드는 조건들의 목록은 L3를 L2로 되돌리는 조건들의 목록이다.**
>
> 또한 이 논문은 **SAE 용어체계 자체의 결함**을 지목한다 — "**요구되는 폴백 준비 상태를 정의하지 못하고, 인간이 그 상태에 어떻게 도달하는지도 정의하지 못한다.**" A-3-1에서 본 §3.22("수용성 = 의식의 한 측면")와 §5.4 NOTE 4("충분한 시간")의 공백을 **학계가 정확히 같은 자리에서 지적하고 있다.**
>
> **★ AX 번역:** **"AI가 자율적으로 처리하되 사람이 준비 상태로 대기한다"는 설계를 안전하게 만들려면, 그 사람이 다른 일을 하지 못하게 해야 한다. 그러면 자동화로 얻으려던 생산성이 사라진다. 중간 등급의 편익은 정의상 그 안전 조건과 상충한다.**

**한계·반박**
- **전문가 인터뷰 기반 탐색적 질적 연구(N = 15)**이며 실증 실험이나 통계적 검정이 아니다. **"연구가 증명했다"가 아니라 "전문가들이 이렇게 판단했다"로 인용해야 정확하다.**
- 표본 15인의 소속 분포와 산업계 이해관계의 영향은 초록만으로 판단할 수 없다.
- ⚠️ 본문 전문 미확보(ScienceDirect 차단). **초록만 verbatim 확인.** → F절.

---

### A-3-8. 실세계 증거 — NTSB 2건 + NHTSA 대규모 조사

**(a) NTSB HAR-17/02 — Williston 테슬라 사망사고 (SAE L2) `[WP]`**
> National Transportation Safety Board. *Collision Between a Car Operating With Automated Vehicle Control Systems and a Tractor-Semitrailer Truck Near Williston, Florida, May 7, 2016.* **NTSB/HAR-17/02**.

**추정 원인 (VERBATIM)**
> "…**the probable cause of the Williston, Florida, crash was the truck driver's failure to yield the right of way to the car, combined with the car driver's inattention due to overreliance on vehicle automation, which resulted in the car driver's lack of reaction to the presence of the truck. Contributing to the car driver's overreliance on the vehicle automation was its operational design, which permitted his prolonged disengagement from the driving task and his use of the automation in ways inconsistent with guidance and warnings from the manufacturer.**"

**★★ "37분 중 25초" (VERBATIM) — 이 책에서 가장 강력한 실사례 숫자**
> "Vehicle performance data showed that **for the 41-minute trip from Cedar Key, Autopilot was active for 37 minutes.** During the trip, while Autopilot was in use, **the system detected driver-applied torque on the steering wheel on seven different occasions for a total of 25 seconds. The longest period between alerts during which Autopilot did not detect the driver's hands on the steering wheel was nearly 6 minutes.** For the entire trip, Autopilot was in some form of warning mode for a total of approximately **2 minutes**."
> "the system displayed the initial visual warning to the driver **seven times** ('**Hold Steering Wheel**')… progressed to the initial auditory warning (alert chime 1) **six times**… **Progression to the second auditory warning (alert chime 2) did not occur during the trip, nor did the system initiate the Autosteer deactivation protocol.**"
> "The last driver input before the crash was to increase the TACC speed to 74 mph… **1 minute 51 seconds before the crash.** After that input, there was **no driver interaction with Autopilot, no change in steering angle, and no brake lamp switch activation until the collision.**" / "**No brakes were applied before or during the collision.**"

**★ 주요 조사 결과 (VERBATIM, 번호 그대로)**
> **5.** "**If automated vehicle control systems do not automatically restrict their own operation to those conditions for which they were designed and are appropriate, the risk of driver misuse remains.**"
> **6.** "**Because driving is an inherently visual task and a driver may touch the steering wheel without visually assessing the roadway, traffic conditions, or vehicle control system performance, monitoring steering wheel torque provides a poor surrogate means of determining the automated vehicle driver's degree of engagement with the driving task.**"
> **9.** "**The way that the Tesla Autopilot system monitored and responded to the driver's interaction with the steering wheel was not an effective method of ensuring driver engagement.**"

> **★★ 이 책에 쓸 수 있는 부분 — "37분 중 25초".**
> **41분 주행 중 37분간 자동화가 켜져 있었고, 그 37분 동안 운전자의 손이 핸들에서 감지된 시간은 총 25초다.** 비율로는 약 **1.1%.** 그리고 시스템은 이 상황을 7번 감지해 경고했지만, **두 번째 청각 경고나 자동조향 해제 프로토콜까지는 한 번도 진행되지 않았다** — 매번 25초 중 일부의 토크 입력으로 **경고가 리셋되었기 때문이다.**
> 이것이 **"감시 지표를 만족시키면서 감시하지 않는 것"의 완벽한 실사례**이며, Finding 6이 그 구조를 정확히 진술한다.
> **★ AX 번역: 대리지표 기반 통제는 대리지표를 만족시키는 회피 행동을 낳는다.** "월 1회 로그인 확인", "승인 클릭", "체크박스 서명" 같은 AX 거버넌스 지표는 전부 Williston의 **"25초 토크"와 같은 구조**다.
>
> **한계:** 단일 사고 조사이며 **통계적 대표성이 없다.** 추정 원인 **1순위는 트럭 운전자의 통행우선권 미양보**이며 자동화 문제는 "결합된(combined with)" 요인이다 — **"자동화가 사고를 냈다"로 단순화하면 부정확하다.** 당시 Autopilot은 Version 7 기준이며 이후 소프트웨어가 여러 차례 변경되었다.

**(b) NTSB HAR-20/01 — Mountain View 테슬라 사망사고 (SAE L2) `[WP]`**
> NTSB. *Collision Between a Sport Utility Vehicle Operating With Partial Driving Automation and a Crash Attenuator, Mountain View, California, March 23, 2018.* **NTSB/HAR-20/01**.

**추정 원인 (VERBATIM)**
> "…**the Tesla Autopilot system steering the sport utility vehicle into a highway gore area due to system limitations, and the driver's lack of response due to distraction likely from a cell phone game application and overreliance on the Autopilot partial driving automation system. Contributing to the crash was the Tesla vehicle's ineffective monitoring of driver engagement, which facilitated the driver's complacency and inattentiveness.**"

**수치 (VERBATIM)**
> "**the crash trip lasted 28 minutes 33 seconds. Autopilot was active more than 75 percent of the time and during the final 18 minutes 55 seconds.** … **driver-applied torque to the steering wheel was not detected 34.4 percent of the time** [Autopilot was active]."
> "**About 6 seconds before the crash, no driver-applied steering wheel torque was detected**" / "drivers [can] have their hands off the steering wheel for **up to 3 minutes** under certain highway driving [conditions]" / "**About 0.49 seconds before the crash, the FCW system detected a stationary object in the Tesla's path.**"

**★ 주요 조사 결과 (VERBATIM) — 규제적 판단**
> **15.** "**Because monitoring of driver-applied steering wheel torque is an ineffective surrogate measure of driver engagement, performance standards should be developed pertaining to an effective method of ensuring driver engagement in SAE Level 2 partial driving automation systems.**"
> **16.** "**If Tesla Inc. does not incorporate system safeguards that limit the use of the Autopilot system to those conditions for which it was designed, continued use of the system beyond its operational design domain is foreseeable and the risk for future crashes will remain.**"
> **19.** "**The National Highway Traffic Safety Administration's approach to the oversight of automated vehicles is misguided, because it essentially relies on waiting for problems to occur rather than addressing safety issues proactively.**"
> **20.** "**It is essential that the [NHTSA's] surveillance and defect investigation program closely examine issues related to foreseeable misuse of automation and perform a forward-looking risk analysis…**"

> **★ 이 책에 쓸 수 있는 부분 — "예견 가능한 오용(foreseeable misuse)"이라는 규제 언어.**
> NTSB가 두 차례 사고(2016, 2018)를 거치며 도달한 핵심 개념은 **"foreseeable misuse"**다. 즉 **"사용자가 매뉴얼을 어긴 것"이 아니라 "설계가 그 위반을 예견 가능하게 만들어 놓은 것"이 결함**이라는 판단이다. 그리고 결정적으로, **NTSB는 이 문제를 개별 제조사가 아니라 "SAE Level 2 부분운전자동화 시스템" 범주 전체의 문제로 프레이밍한다**(Finding 15, 17). **즉 등급 자체가 위험 단위다.**
> **★ AX 번역:** AX 거버넌스에서 **"직원이 정책을 위반했다"는 사고 분석은 대부분 틀렸다.** **정책이 위반을 예견 가능하게 만들어 놓았는지**를 물어야 하고, 그 답이 "그렇다"면 결함은 정책 쪽에 있다.
>
> **한계:** 단일 사고. **사고 심각도의 상당 부분은 충돌 완충장치가 이전 사고로 파손된 채 수리되지 않은 데 기인한다**(Finding 13, 14: "**If the crash attenuator… had been repaired in a timely manner… the Tesla driver most likely would have survived the collision.**"). **자동화 요인만 떼어 인용하면 사실 왜곡이다.** NTSB는 규제 권한이 없는 권고 기관이므로 Finding 17·19의 NHTSA 비판은 기관 간 견해 차이라는 맥락을 함께 밝히는 편이 공정하다.

**(c) ★★ NHTSA ODI EA22-002 — 2백만 대 규모의 실세계 증거 `[WP]`**
> U.S. DOT, NHTSA, Office of Defects Investigation. *ODI Resume — Investigation: EA22002, Subject: Autopilot System Driver Controls.* Date Opened **2022-06-08**, Date Closed **2024-04-25**.

**대상 규모 (VERBATIM)**
> Products: "2012 – 2023 Model Y, X, S, 3 equipped w/ Autopilot manufactured up to 7-Dec-2023" · **Population: 2,031,220**
> Problem Description: "**The prominence and scope of Autopilot's control may be insufficient to prevent crashes due to lack of driver engagement.**"

**사고 집계 (VERBATIM, 표)**

| 구분 | ODI | Manufacturer | EWR D&I | Other | **Total** |
|---|---|---|---|---|---|
| All Incidents / Crashes | 12 | 259 | 10 | 421 | **467\*** |
| Injury Incidents | 1 | 31 | 7 | 27 | **32\*** |
| Number of Injuries | 1 | 53 | 12 | 41 | **54\*** |
| **Fatality Incidents** | 2 | 11 | 3 | 9 | **13\*** |
| **Number of Fatalities** | 2 | 12 | 3 | 9 | **14\*** |

*"\*Total eliminates duplicates received by the manufacturer"*

**★ 분석 및 결론 (VERBATIM)**
> "**ODI completed an analysis of 956 crashes reported up to August 30, 2023.** In approximately half (**489**) of those crashes, ODI found: 1.) that there was insufficient data to make an assessment; 2.) the other vehicle was at fault; 3.) Autopilot was found to not be in use; or 4.) the crash was otherwise unrelated to EA22002. **Of the remaining 467 crashes, ODI identified trends resulting in three categories: collisions in which the frontal plane of the Tesla struck another vehicle or obstacle with adequate time for an attentive driver to respond to avoid or mitigate the crash (211), roadway departures where Autosteer was inadvertently disengaged by the driver's inputs (111), and roadway departures in low traction conditions such as wet roadways (145).**"
> "**Crash and human factors assessment showed that Autopilot controls did not sufficiently ensure driver attention and appropriate use. At the same time, peer analysis and vehicle evaluations established that Autopilot invited greater driver confidence via its higher control authority and ease of engagement. This mismatch of weak usage controls and high control authority was evident in these crash categories**, which included indications of driver disengagement from the driving task."
> "**ODI completed an extensive body of work via PE21020 and EA22002, which showed evidence that Tesla's weak driver engagement system was not appropriate for Autopilot's permissive operating capabilities. This mismatch resulted in a critical safety gap between drivers' expectations of the L2 system's operating capabilities and the system's true capabilities. This gap led to foreseeable misuse and avoidable crashes.**"
> "**During EA220002, ODI identified at least 13 crashes involving one or more fatalities and many more involving serious injuries, in which foreseeable driver misuse of the system played an apparent role.**"
> (리콜) "On December 12, 2023, **Tesla filed a Defect Information Report (Recall 23V838)**… **stated that the prominence and scope of the system's controls may be insufficient to prevent driver misuse, and described a remedy to improve the effectiveness of driver warnings and to reduce mode confusion.**"
> (후속) "…**ODI has opened a Recall Query (RQ24009) to assess the effectiveness of the 23V838 remedy.**"

**L2에 대한 NHTSA의 규범적 정의 (VERBATIM)**
> "L2 systems should be designed to support the driver's need to monitor the system in response to the constantly changing driving environment and, if necessary, take over the dynamic driving task. **To ensure sufficient driver engagement, vehicles with L2 systems should employ driver engagement systems and usage controls that are appropriate and sufficient for the L2 system design and driver expectations.**"

> **★★ 이 책에 쓸 수 있는 부분 — "제어 권한과 관여 통제의 불일치(mismatch)". 이 절에서 가장 이식성 높은 개념이다.**
> NHTSA가 **2백만 대·467건 충돌·13건 치명사고**를 분석해 도출한 결함의 정체는 **"Autopilot이 자율주행을 잘 못한다"가 아니었다.** 결함은 **"높은 제어 권한(high control authority)"과 "약한 사용 통제(weak usage controls)"의 불일치**였다.
> - **높은 제어 권한** = 시스템이 실제로 많은 것을 대신 해준다 → 사용자의 신뢰와 이탈을 **초대(invited)**한다
> - **약한 사용 통제** = 그럼에도 사용자가 계속 감독하도록 강제하는 장치는 빈약하다
> - 그 사이의 간극 = **"critical safety gap between drivers' expectations… and the system's true capabilities"**
>
> **★ "중간 등급이 가장 위험하다"를 규제 언어로 옮기면 정확히 이것이다: 제어 권한이 올라가는 속도를, 관여 통제가 따라가지 못하는 구간이 중간 등급이다.** 낮은 등급에서는 권한이 낮아 간극이 없고, 높은 등급에서는 통제 요구가 없어 간극이 없다. **간극은 그 사이에서만 벌어지고, 권한이 최대이면서 통제가 여전히 인간에게 남아 있는 지점에서 최대가 된다.**
> 그리고 **Tesla의 결함신고서가 스스로 밝힌 시정 목표에 "mode confusion을 줄이는 것"이 포함되어 있다는 점** — 요청받은 "L2–L3 경계의 모드 혼동" 논점에 대한 **제조사 자신의 인정**이다.
>
> **★ AX 번역:** AX 도구를 배포할 때 물어야 할 단 하나의 질문은 **"이 도구의 제어 권한이 커진 만큼, 사람의 관여를 담보하는 장치도 같이 커졌는가?"**다. 대개는 권한만 커지고 통제는 그대로다. **그 격차가 곧 critical safety gap이다.**

**한계·반박 (반드시 병기)**
- **이 자료는 분모가 없다.** 467건·13건은 절대 수치이며, **동일 조건에서 Autopilot 미사용 시의 사고율과 비교되지 않았다.** **"Autopilot이 사고를 늘렸다"는 결론을 이 문서로부터 도출할 수 없다.** Tesla 측은 일관되게 Autopilot 사용 시 주행거리당 사고율이 낮다고 주장해 왔다(이 문서에서 검증되지 않음).
- 956건 중 **489건은 판정 불가·타차 과실·Autopilot 미사용 등으로 제외**되었고, 남은 467건도 "Autopilot이 원인"이라는 판정이 아니라 **"EA22002 관련 경향이 관찰된 사고"**다.
- 데이터 출처가 이질적이다(ODI 12건, 제조사 259건, EWR 10건, SGO·언론 421건). **보고 편향이 크다.**
- 조사는 **결함 확정이 아니라 Tesla의 자발적 리콜을 이유로 종결**되었고, NHTSA는 곧바로 **그 리콜의 효과성을 재조사하는 RQ24009를 개설**했다 — **문제가 해결되었다는 판정이 아니다.**
- 이 조사는 **L2**에 관한 것이다. L3 논증에는 **a fortiori 논법으로만** 쓰라.

---

### A-3-9. 처방 — 고정 등급의 대안은 "더 높은 등급"이 아니라 "고정하지 않는 것"

**서지**
> David B. Kaber & Lawrence J. Prinzel III. *Adaptive and Adaptable Automation Design: A Critical Review of the Literature and Recommendations for Future Research.* **NASA/TM-2006-214504**, **September 2006**. NASA Langley Research Center. **[WP]** (전문 32쪽 확보)

**★ 핵심 결론 (VERBATIM)**
> "In contrast to adaptable systems, **adaptively automated systems provide for dynamic task/function allocations mandated by a computer based on real-time monitoring of operator workload states. Decision making regarding the allocation of system control is not an additional responsibility of operators and, consequently, overall workload may be lower. Based on the review of literature, numerous approaches to adaptive automation (model-based, performance-based, workload-based, etc.) have been shown to improve operator performance in both psychomotor and cognitive tasks and to facilitate workload reductions in comparison to completely manual control and static automation. These findings are far more promising than the current results on adaptable systems performance.**"
> "Studies of automation invocation authority in adaptive systems have also revealed **an advantage of computer mandates of function allocation over human delegation of tasks to a computer** because of potential workload issues."
> (적응**가능**형에 대한 신중론) "**when system operators are required to switch between control strategies or tasks on a regular basis, adaptable automation appears to provide some advantage over static automation but it is not superior to manual control.**"

**★ 자동화가 만들어내는 "새로운" 문제 5가지 (VERBATIM, Woods 1996 인용 포함)**
> "As a consequence, automation increases the burdens and complexities for those responsible for operating, troubleshooting, and managing systems resulting in '**new**' problems, including:
> 1. adding to or changing the nature of the task, such as device setup and initialization, configuration control, and operating sequences;
> 2. changing and/or adding cognitive demands;
> 3. **changing the roles of people in the system, often relegating people to supervisory controllers who watch over the automation potentially leading to 'out-of-the-loop' performance issues;**
> 4. increasing coupling and integration among parts of a system often resulting in data overload and lack of 'transparency' leaving operators to wonder '**what is it [the automation] doing now?**'; and
> 5. **lack of appreciation of the impact of automation on humans by those who advocate for the use of the technology.**"

> **★ 이 책에 쓸 수 있는 부분.**
> 이 리뷰는 두 가지를 구분한다 — **적응형(adaptive, 컴퓨터가 실시간 상태 감지로 배분을 바꿈)**과 **적응가능형(adaptable, 인간이 배분을 선택함)**. 결론은 **적응형이 정적(고정) 자동화보다 우월하고, 적응가능형은 그렇지 않다**는 것이다. **배분 결정 자체가 인간에게 추가 부하가 되기 때문이다.**
> **이것이 이 책의 논증에 중요한 뉘앙스를 더한다.** "중간 등급이 위험하다"의 처방은 **"등급을 올려라"가 아니라 "등급을 고정하지 말라"**일 수 있다. Eriksson & Stanton(2017)이 제안한 것도 정확히 이것이다 — 시선이 도로를 벗어난 시간을 감지해 **리드타임을 동적으로 늘리는 적응형 TOR.**
> 그리고 **위 5번 항목 — "기술 도입을 옹호하는 사람들이 자동화가 인간에게 미치는 영향을 이해하지 못한다" — 은 AX 추진 조직에 대한 20년 전의 정확한 진단이다.**
>
> **★ AX 번역:** AX 체계의 자동화 수준을 **정책 문서에 고정된 값으로 박아넣지 말고, 상황 신호(작업 위험도·모델 신뢰도·담당자 상태·최근 오류율)에 따라 동적으로 조정되게** 설계하라. 다만 **"조정 여부를 사용자가 매번 판단하게" 하는 방식(adaptable)은 실증적으로 이득이 크지 않다** — 그 판단 자체가 새로운 부하이기 때문이다.

**한계·반박** **2006년 리뷰**이며 이후 20년의 연구가 반영되어 있지 않다. 검토 대상이 주로 항공·프로세스 제어·실험실 과제다. 적응형 자동화의 핵심 난점 — **운영자 상태를 실시간으로 신뢰성 있게 추정하는 것** — 은 2006년에도 미해결이었고 상당 부분 여전히 미해결이다. NASA 기술보고서로 **동료심사 논문이 아니다.**

**최신 후속 (서지만 확인)**
> Marco Bernabei & Francesco Costantino. "**Adaptive automation: Status of research and future challenges**." *Robotics and Computer-Integrated Manufacturing*, **88, 102724**, **2024년 8월**. DOI **10.1016/j.rcim.2024.102724** · **[PR]**
> ⚠️ **초록·본문 미확보**(ScienceDirect 차단). **"적응형 자동화가 2024년까지 이어지는 살아 있는 연구 프로그램"이라는 신선도 근거로만 안전하게 쓸 수 있다. 구체적 주장·수치 인용은 원문 확인 전까지 하지 말 것.** → F절.

---

### ★ A-3 종합 — 서로 다른 방법이 같은 곳에 도착한다

| 출처 | 처방 (VERBATIM) | 태그 |
|---|---|---|
| **Victor et al. (2018)** | "Automation needs to be designed **either so that it does not rely on the driver or so that the driver unmistakably understands that it is an assistance system** that needs an active driver to lead and share control." | [PR] |
| **Zhang et al. (2019)** | "achieving a low mean TOT should not necessarily be a design target... efforts should be directed towards **ensuring that drivers actually have sufficient time**" | [PR] |
| **Eriksson & Stanton (2017)** | "designers of automated vehicles **should not focus on the mean, or median, driver**... there is a case for '**adaptive automation' that modulates TORlt**" | [PR] |
| **Merat et al. (2014)** | "**regular disengagement of automation is not a particularly practical method for keeping drivers in the loop**" | [PR] |
| **Gerber et al. (2023)** | 사용자는 "**remain physically and sensory in the state of regular drivers**"; NDRA는 "**limited to the onboard-entertainment system**"이며 "**context-aware and (temporarily) restricted or interrupted**" | [PR] |
| **NHTSA EA22-002 (2024)** | "**driver engagement systems and usage controls that are appropriate and sufficient for the L2 system design and driver expectations**" | [WP] |
| **Kaber & Prinzel (2006)** | 적응형(computer-mandated) 배분이 정적 자동화보다 우월; 적응가능형(human-delegated)은 그렇지 않음 | [WP] |

> **★ 책에 쓸 수 있는 종합 명제.** 서로 다른 연구팀이, 서로 다른 방법으로, **"중간 등급을 안전하게 만드는 조건"을 각자 도출했더니 그 조건들이 하나같이 중간 등급의 편익을 상쇄하거나 소멸시킨다**는 데로 수렴했다. **중간 등급이 나쁘다는 것이 아니라, 중간 등급을 안전하게 만들면 그것은 더 이상 중간 등급이 아니다.**

### ★ A절 논증 뼈대로 바로 쓸 수 있는 5문장 (모두 verbatim 확인 완료)

1. **Bainbridge (1983):** "the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate."
2. **Bainbridge (1983):** "it is humanly impossible to carry out the basic function of monitoring for unlikely abnormalities"
3. **Endsley (2017):** "as more autonomy is added to a system, and its reliability and robustness increase, the lower the situation awareness of human operators and the less likely that they will be able to take over manual control when needed."
4. **Victor et al. (2018):** "neither these reminders nor explicit instructions on system limitations and supervision responsibilities prevented 28% (21/76) of drivers from crashing with their eyes on the conflict object"
5. **NHTSA EA22-002 (2024):** "This mismatch resulted in a **critical safety gap** between drivers' expectations of the L2 system's operating capabilities and the system's true capabilities. This gap led to foreseeable misuse and avoidable crashes."

---

## ★ A 커버리지

**확보 (충분)**
- **A-1 LOA 고전:** Sheridan & Verplank 10단계 **표 전문 확보**(재수록본 경유) / Parasuraman·Sheridan·Wickens 4단계 + 초록 전문 / Endsley & Kaber 10×4 배분표 + 실험 결과 / Bainbridge 9개 인용문 / Endsley 2017 automation conundrum / Endsley & Kiris 초록 전문 — **등급 비교표 작성 완료**
- **A-2 최신 등급:** 실재 확인된 프레임 **9건** + AI 랩 공식 문서 **3건** + 규제 **2건**. 등급표는 대부분 **원문 판독으로 verbatim 확보.** AAL/ACL 이원 체계, 3As 다차원, κ 판정 불일치 수치까지 확보
- **A-3 자율주행 유비:** J3016 정본 서지·L0–L5 정의·수용성 정의·"충분한 시간" 조항·공식 시각 분할표 / 인계 실증 3건(26명 실험·129편 메타분석·37명 시뮬레이터) / 테스트트랙 106명 / L3 비판 동료심사 논문 / NTSB 2건 + NHTSA 2백만 대 조사 — **"중간 등급이 가장 위험하다"의 실증 사슬 완성**
- **계보 단절 확인:** arXiv 검색 0건, 직접 연결 2건만 존재 — **이 책의 기여 지점 특정**

**비어 있음 / 미완**
- ⚠️ **Sheridan & Verplank 1978 원 보고서(DTIC ADA057655) 미확보.** 10단계 표는 재수록본 경유이며, "1978 vs 1987" 연도 귀속이 자료마다 갈린다.
- ⚠️ **Parasuraman & Riley (1997) 원문 미확보.** use/misuse/disuse/abuse 정의는 통상적 정리이며 verbatim이 아니다.
- ⚠️ **Endsley & Kiris(1995)·Endsley(1995) 본문 수치 미확보** (초록만).
- ⚠️ **OpenAI "5단계 AGI" 공식 출처 확인 실패** — 공식 발간물이 아닐 가능성이 높다.
- ⚠️ **DoDD 3000.09 원문 미확인** — in/on/out-of-the-loop 기원은 **HRW 2012로만** 서술하라.
- ⚠️ **제조사의 "L3를 건너뛰겠다"는 공식 1차 발언 확인 실패.** 다만 Victor et al.의 "either/or" 처방(Volvo Cars 소속)·Gerber et al.의 L3 용어 비판·NHTSA의 critical safety gap으로 **논증은 근거 없이도 성립한다.**
- **ACM DL·IEEE Xplore·OpenReview·USENIX·CHI/CSCW/FAccT proceedings 직접 검색 미수행**(WebSearch 예산 소진). arXiv/OpenAlex/Semantic Scholar API로 대체했으므로 **arXiv에 프리프린트를 올리지 않은 HCI 학회 논문이 누락되었을 가능성**이 있다. 특히 FAccT 계열 인간 감독 등급 연구는 추가 조사를 권한다.

---
