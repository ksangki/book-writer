# 학술 리서치 2차 보강 — 섹션 B: 축 5 (측정 · FTE · 성과 귀속)

> **상태: B-1 ~ B-3 정제 완료 / B-4 · B-5 원자료 수록.**
> - **B-1**(자기보고 측정 신뢰도) · **B-2**(측정 왜곡·대리지표) · **B-3**(인간+기계 성과 귀속) — 정제 완료. 각 항목이 서지 · 핵심 주장 · 이 책에 쓸 부분 · VERBATIM 인용 · 한계 4단으로 정리돼 있다.
> - **B-4**(자동화·고용·재배치) · **B-5**(AI와 총요소생산성) — **서지·수치 확인은 완료했으나 최종 편집 전 원자료 형태로 수록한다.** 내용은 신뢰할 수 있고 인용 규율(원문 대조·VERBATIM·미확인 표시)을 동일하게 지켰으나, 절 번호 체계와 서술 톤이 B-1~B-3과 아직 통일돼 있지 않다.
> - 각 절 끝의 `⚠️ 미확인 항목`을 **저술 전 반드시 확인하라.**
>
> **짝 문서:** 섹션 A는 `papers2_A_autonomy.md`, 섹션 C는 `papers2_C_orgtheory.md`.

# B. 축 5 — 측정 · FTE · 성과 귀속

---

## B-1. 자기보고 생산성 측정의 신뢰도

> **이 절이 방어하는 설계.** 이 책은 측정 신뢰도를 **"실측 / 표본 / 자기보고"**로 나눠 차등 인정하자고 제안한다. 아래 문헌은 그 설계를 두 방향에서 지지한다 — **(1) 자기보고는 방향성 있는 편향을 갖는다. (2) 그러나 그 편향의 크기는 설계 가능한 변수다.** 두 번째가 더 중요하다. **"자기보고를 버려라"가 아니라 "낮은 등급으로 인정하고 편향을 보정하라"**가 문헌이 지지하는 결론이다.

---

### B-1-1. Robinson & Bostrom (1994) — 자기추정 노동시간 vs 시간일지

**서지**
> John P. Robinson & Ann Bostrom. "**The overestimated workweek? What time diary measures suggest.**" *Monthly Labor Review*, **August 1994**, pp. **11–23**. U.S. Bureau of Labor Statistics.
> https://www.bls.gov/opub/mlr/1994/article/overestimated-workweek-what-time-diary-measures-suggest.htm · **[PR]** (미 노동통계국 공식 학술지)
> ※ 원문 PDF는 스캔 이미지라 OCR로 추출했다. 산문의 수치는 여러 위치에서 교차 확인했으나 **표 셀 값은 OCR 판독이므로 최종 인용 전 시각 대조를 권한다.**

**핵심 주장.** 같은 응답자에게 (a) "일주일에 몇 시간 일하나" 추정 질문과 (b) 24시간 시간일지를 **동시에** 받으면, 추정치가 일지 기록보다 체계적으로 높다. 그리고 **추정치가 클수록 과대추정 폭이 커진다.** 1965·1975·1985년 미국 전국 시간일지 조사 3개 파동(합산 **n = 4,723**; 1965년 816, 1975년 1,305, 1985년 2,602).

**★ 인용 가능한 문장·수치 (VERBATIM)**
> "Nonetheless, it is clear that values of the estimate-diary difference do rise as values of estimate responses increase, being **−3 hours for the zero-hour category, 2 hours for the 40—44-hour category and 25 hours for the 75 hours or more category.**"
> (추정치–일지 차이는 추정 응답이 커질수록 상승한다. 0시간 구간 −3시간, 40–44시간 구간 2시간, **75시간 이상 구간 25시간**.)

> "Among workers claiming to work **more than 55 hours per week, the gap was often more than 10 hours per week**, indicating reports considerably above the actual hours worked."

> "In these high-hour workweek categories, **the ratio of estimate-diary difference to actual hours worked is as high as 50 percent.** Among those in normal 35—44-hour categories, overestimation is not nearly as high—**closer to 10 percent.**"
> ※ OCR이 "SO percent"로 판독한 자리 = "50 percent". 시각 확인 권장.

> "Another pattern in table 2 is that values of the difference are **lowest in 1965 (1 hour), higher in 1975 (4 hours), and highest in 1985 (7 hours).** This suggests that, over the 20-year-period, **respondents were becoming progressively more inaccurate in more recent surveys.**"

> "It would appear that **simply taking these estimates at face value and averaging them would lead to serious overestimates.**"

**표 2 (일지 노동시간, 1965–85 평균) — 추정 구간별 "추정−일지" 차이 (시간/주):**
0시간 **−3** / 20–29 2 / 30–34 2 / 35–39 7 / 40–44 2 / 45–49 3 / 50–54 9 / 55–59 10 / 60–64 14 / 65–74 15 / **75+ 25**

**★ 이 책에 쓸 수 있는 부분.** "자기보고"를 측정 신뢰 등급 최하위에 두는 설계의 1차 근거다. 특히 **"많이 일한다고 말하는 사람일수록 더 많이 부풀린다"는 비선형 패턴**은, **AX 도입 효과를 자기보고로 걷을 때 열성 사용자(=효과를 크게 보고할 사람)에게서 오차가 가장 커진다**는 예측으로 그대로 옮겨진다.

**한계·반박 (중요)**
1. **Jerry Jacobs의 평균회귀 반론.** 격차가 "추정치가 클수록 크다"는 패턴은 측정오차가 있는 두 변수 간의 **평균회귀**로도 나온다. Robinson & Bostrom은 선형성을 근거로 반박했으나("The generally linear relation … generally rules out an explanation … in terms of simple regression toward the mean") 결정적이지 않다.
2. **Frazis & Stewart(2014)의 정면 반박** — B-1-3 참조. **이 문헌은 반드시 반박과 함께 인용해야 한다.**
3. 시간일지도 완벽하지 않다(왜곡·미화·망각).
4. 1965–1985 데이터라 낡았다.
5. **이 논문은 노동시간에 관한 것이지 생산성이 아니다.** 확장 인용할 때는 **"시간 자기보고조차 이 정도 편향인데, 생산성 자기보고는 어떻겠나"라는 a fortiori 논증**으로 쓰는 것이 안전하다.

---

### B-1-2. Robinson, Martin, Glorieux & Minnen (2011) — 최신 데이터 재검증

**서지**
> John P. Robinson, Steven Martin, Ignace Glorieux, & Joeri Minnen. "**The overestimated workweek revisited.**" *Monthly Labor Review*, **June 2011**, pp. **43–53**. BLS. **[PR]**

**핵심 주장.** 미국 ATUS 2003–07(15세 이상 7만 명 이상 면접, 응답률 약 56%)와 벨기에 플랑드르 주간 일지 조사(1999년 n=1,533, 2004년 n=1,780; 분석 표본 18–64세 취업자 **n=1,796** — 남 977, 여 819)로 1994년 발견을 재현. **격차는 5~10% 범위로 지속·일관되게 존재하나 아주 크지는 않다.**

**★ 인용 가능한 문장·수치 (VERBATIM)**
> "Data from the American Time Use Survey (ATUS) and a Belgian national survey using weekly diaries indicate that, when asked to estimate their number of work hours, employed respondents tend to **overestimate their work hours by 5–10 percent** in relation to the work hours they report in their time diaries; **most of the overestimation is accounted for by respondents who estimate longer work hours**"

> "The 'estimate–diary' gaps range from **2.1 hours to 6.3 hours**; in other words… people **overestimated by between 5 percent and 12 percent.**"

**표 1 (2003–07) — 추정 / 일지 / 차이:**
- ATUS "usual": 39.5 / 36.3 / **3.2** · 41.3 / 37.4 / **3.9** · 44.0 / 40.4 / **3.6**
- CPS "usual": 39.5 / 35.9 / **3.6** · 41.3 / 37.3 / **4.0** · 43.5 / 38.1 / **5.4**
- CPS "last week": 38.7 / 35.9 / **2.8** · 41.3 / 37.6 / **3.7** · 43.5 / 40.4 / **3.1**
- 여성 CPS "last week", 35시간 이상: 43.9 / 37.6 / **6.3** ← **최대 격차**
- 남성 ATUS "usual", 1시간 이상: 42.7 / 40.6 / **2.1** ← **최소 격차**

**★ 가사노동에서는 격차가 두 배 (매우 인용하기 좋음)**
> "when the time spent doing these nine tasks was added up, it was found that, per week, **men estimated a total of 23 hours of housework versus 10 hours in the diary, and women estimated 32 hours versus 17 hours in the diary.**"
> "Unlike the case for paid work hours… **the gap for housework is almost double.**"

**★ 활동 빈도 자기보고 — AX 사용 빈도에 직접 적용 가능**
> "**Estimates across all, or almost all, activities ultimately sum to more than 168 hours per week.**" … "For both types of clubs, **almost half of all respondents overestimated the actual number of times they participated by more than 100 percent.**"
> ※ 후자는 Chase & Godbey의 수영·테니스 클럽 **출입기록 대조** 연구. **행위 빈도 자기보고가 객관 로그 대비 2배 이상 부풀려진 사례**로, **AX 도구 사용 빈도 자기보고에 그대로 적용된다.**

**★★ 이 책의 명제에 그대로 쓸 수 있는 문장**
> "**An answer to a time-estimate question is a perception rather than a number arrived at through pure addition**, and the perception probably is influenced by implicit or explicit work-hour arrangements between the employer and the employee; in addition, **the perception is not formally verified.**"
> (시간 추정 질문에 대한 답은 **순수한 덧셈으로 도달한 숫자가 아니라 지각**이며, 그 지각은 고용주와 피고용인 사이의 암묵적·명시적 합의에 영향받을 가능성이 크다. 게다가 **그 지각은 공식적으로 검증되지 않는다.**)
> → **"자기보고는 측정이 아니라 지각"**이라는 이 책의 명제에 그대로 쓸 수 있다.

**한계·반박.** 벨기에 조사 응답률이 낮다(1999년 약 27%, 2004년 약 37%). 그리고 **Frazis & Stewart(2014)가 이 논문의 표 1 자체를 반박했다.**

---

### B-1-3. ★ Frazis & Stewart (2014) — 반박 문헌 (균형을 위해 필수)

**서지**
> Harley Frazis & Jay C. Stewart. "**Is the workweek really overestimated?**" *Monthly Labor Review*, **June 2014**. BLS. **[PR]**
> 선행: Frazis & Stewart (2004), "What can time-use data tell us about hours of work?" *MLR*, December 2004, pp. 3–9.

**핵심 주장.** Robinson et al.(2011)의 핵심 표에는 내부 불일치가 있으며, 제대로 표본을 맞춰 재현하면 **CPS "지난주 실제 노동시간" 질문의 편향은 사실상 0이다.** 질문 설계(앵커 + 후속 질문)가 편향을 크게 줄인다.

**★ 인용 가능한 문장 (VERBATIM)**
> "This article documents **substantial inconsistencies** in research claiming that the Current Population Survey overestimates hours worked and **confirms that any such bias is small.**"
> "We examined Robinson et al.'s results closely and found that their main table of results contains **extensive internal inconsistencies—evidence of programming or transcription errors.**"
> "For the sample as a whole, **the average difference between CPS actual hours and diary hours is only 0.2 hour per week.**"
> "**The usual-hours question anchors the response, and the follow-up questions direct the respondent to focus on the previous week. This sequence of questions appears to substantially reduce bias relative to asking a single question.** So one answer to the question 'Is the workweek overestimated?' is '**Not by average CPS respondents answering questions about the previous week.**'"
> "Our replication… produced results similar to those in our earlier work—**a substantial bias for the ATUS usual-hours question, less bias for CPS usual hours, and a small negative bias for CPS actual hours.**"

**★★ 가장 강력한 인용거리 — 반박자조차 패턴은 재현했다**
> "Our results are **qualitatively similar to Robinson et al.'s: the gap between estimate-question hours and diary hours grows almost monotonically for each comparison, going from negative to positive as reported hours increase.**"

**★ 이 책에 쓸 수 있는 부분 — 이게 오히려 책의 설계 논지를 강화한다.**
"자기보고가 항상 틀린다"가 아니라 **"질문 설계에 따라 자기보고의 신뢰도가 달라진다 — 그래서 등급을 매기고 설계를 규율해야 한다"**는 주장으로. AX 측정에서 **"이번 분기에 AI로 얼마나 생산성이 올랐나요?"(나쁜 설계)와 "어제 이 작업에 몇 분 썼나요?"(좋은 설계)**의 차이를 정당화한다.

**한계·반박.** **양측이 합의하는 지점이 있다:** 이들도 **ATUS "usual hours" 질문에는 상당한 편향이 있음을 인정한다.** 즉 **"통상적으로 얼마나?" 형태의 질문(= 대부분의 사내 생산성 설문이 쓰는 형태)은 여전히 편향된다.**

---

### B-1-4. Buehler, Griffin & Ross (1994) — 계획 오류의 정본

**서지**
> Roger Buehler, Dale Griffin, & Michael Ross. "**Exploring the 'planning fallacy': Why people underestimate their task completion times.**" *Journal of Personality and Social Psychology*, **67(3), 366–381**, **1994년 9월**.
> DOI: **10.1037/0022-3514.67.3.366** · **[PR]**

**핵심 주장.** 사람은 자기 과업의 완료 시점을 체계적으로 낙관 편향되게 예측한다. **결정적으로, "최악의 경우"를 상정하라고 지시해도 여전히 과소추정하며 정확도는 개선되지 않는다.**

**★ 인용 가능한 수치 (VERBATIM, Study 1: 워털루대 심리학 우등논문 수강생 37명 — 여 27, 남 10; 분석 n=33)**
> "When asked for their best estimate, respondents predicted, on average, that they would finish in **33.9 days**, but they actually took **55.5 days**, **t(32) = 3.43, p < .002.**"
> "**Fewer than one third of the respondents (29.7%)** finished in the time they reported as their most accurate prediction."
> "When they assumed that 'everything went as well as it possibly could,' students offered predictions that were almost 30 days earlier than the actual completion times (**M = 27.4 days vs. 55.5 days**), **t(32) = 4.11, p < .001**; only **10.8%** of the respondents finished their theses by the optimistic date."
> "Interestingly, **fewer than half of the respondents (48.7%) finished by the time they had predicted assuming that 'everything went as poorly as it possibly could.'** Although the difference was not significant, respondents tended to underestimate their actual completion times **even when they made pessimistic predictions** (**M = 48.6 days vs. 55.5 days**), **t(32) = 1.03, ns.**"
> "**Although the instructions to make a pessimistic prediction decreased the optimistic bias in prediction, it did not increase the accuracy of respondents' forecasts.**"

**★★ 결정적 뉘앙스 — 이 책의 설계를 정확히 정당화한다**
> "Despite the optimistic bias, respondents' best estimates were by no means devoid of information: **The predicted completion times were highly correlated with actual completion times (r = .77, p < .001).**"
> → **자기보고는 *수준(level)*에서는 편향되지만 *순위(rank)*에서는 유용하다.** 이것이 **"자기보고를 버리지 말고 낮은 등급으로 인정하라"**는 이 책의 설계를 정확히 정당화한다.

**Study 1 표 1 전체값:** 예측일 **33.9**(최선)/**27.4**(낙관)/**48.6**(비관), 실제 **55.5**, 차이 −21.6/−28.1/−6.9, 절대차이 22.6/28.2/23.2, 예측시간 내 완료 비율 **29.7%/10.8%/48.7%**, 상관 **.77/.73/.72**.
**Study 2:** 학업 과제 예측 5.8일 vs 실제 10.7일, **F(1,87)=20.00, p<.001**; 비학업 과제 예측 5.0일 vs 실제 9.2일. 상관 .36/.48.

**★ 이 책에 쓸 수 있는 부분.** **"비관 시나리오를 물어봐도 안 고쳐진다"**는 결과는, AX 효과 추정에서 **"보수적으로 잡아보세요"라는 흔한 완화책이 작동하지 않는다**는 실증 근거다.

**한계·반박.** 대학생 표본, 개인 과업 단위. 조직 단위 생산성 측정으로의 외적 타당도는 직접 검증되지 않았다. 다만 Jørgensen(2004)이 소프트웨어 실무자 대상으로 같은 방향을 확인한다.

---

### B-1-5. ★ Jørgensen (2004) — 소프트웨어 공수 추정 편향

**서지**
> Magne Jørgensen. "**A review of studies on expert estimation of software development effort.**" *Journal of Systems and Software*, **70(1–2), 37–60**, **2004년 2월**.
> DOI: **10.1016/S0164-1212(02)00156-5** · **[PR]**

**핵심 주장.** 전문가 판단 기반 공수 추정은 소프트웨어 업계의 지배적 방식이며 체계적으로 과소추정된다. **결정적으로, 과잉낙관은 통제 수준에 비례해 커지고, 유일하게 효과적인 완화책은 "본인이 아닌 사람이 추정하게 하는 것"이다.**

**★ 인용 가능한 문장 (VERBATIM)**
> "The results from many human judgment studies indicate that **people get over-optimistic when predicting own performance**, i.e., they have problems separating '**wish**' and '**realism**'."

> "A general phenomenon seems to be that **the level of over-optimism increases with the level of control** (Koehler and Harvey 1997), e.g., **a software developer responsible for the whole task to be estimated is supposed to be more over-optimistic than a project leader** that plans and supervises the work of other project members."

> "This over-optimism may be difficult to reduce, and in (Newby-Clark, Ross et al. 2000) it was found that **the only effective method was to let someone other than the executing person predict the work.**"

> "**someone other than the person(s) responsible for developing and implementing a plan of action should estimate its probability of success.**" (Harvey 2001 인용)

**★★ B-1과 B-2를 잇는 다리 문장**
> "In our opinion, this means that **the estimation accuracy should be part of the projects' evaluation criteria, but that a strong pressure from accuracy accountability or reward/punishment should be avoided.**"
> → **측정 정확도 자체를 목표로 걸면 정확도가 망가진다.** B-2의 Goodhart로 바로 넘어간다.

> "This type of situation both puts an unfortunate pressure on the estimator and leads to conflicting goals, i.e., **a conflict between 'be realistic' and 'please the manager'.**"

**★★ "경험 많은 사람의 자기보고는 더 믿을 만하다"는 통념의 반박**
> "Jørgensen and Sjøberg (2002b) report that **software maintainers with application specific experience had fewer maintenance problems, but did not predict their own work more accurately.** Similarly, Lichtenstein and Fischhoff (1977) report that **the level of over-optimism … was independent of the actual correctness of the answers, i.e., the level of expertise.**"
> → **측정 등급제에서 시니어 자기보고에 가산점을 주지 말아야 할 근거.**

**★ 이 책에 쓸 수 있는 부분.** AX 효과 자기평가를 **"실행 당사자"에게 맡기면 안 되는 이유**의 소프트웨어 도메인 근거. 그리고 **"추정 정확도를 평가·보상에 강하게 연동하면 오히려 정확도가 떨어진다"**는 반직관적 결론은 AX KPI 설계에 직결된다.

**한계·반박.** 리뷰 논문이므로 1차 데이터가 아니다. 2004년 자료라 애자일·AI 코딩 도구 이후 환경 변화를 반영하지 못한다.
⚠️ **"소프트웨어 프로젝트가 평균 30–40% 공수 초과" 류의 수치는 원문 대조로 확인하지 못했다.** → F절.

---

### B-1-6·7. ★★ Podsakoff et al. — 공통방법편향 (2003 정본 / 2012 수치)

**서지 (정본)**
> Philip M. Podsakoff, Scott B. MacKenzie, Jeong-Yeon Lee, & Nathan P. Podsakoff. "**Common method biases in behavioral research: A critical review of the literature and recommended remedies.**" *Journal of Applied Psychology*, **88(5), 879–903**, **2003년 10월**. DOI **10.1037/0021-9010.88.5.879** · **[PR]**

**서지 (수치가 강한 후속)**
> Philip M. Podsakoff, Scott B. MacKenzie, & Nathan P. Podsakoff. "**Sources of method bias in social science research and recommendations on how to control it.**" *Annual Review of Psychology*, **63, 539–569**. 온라인 선공개 2011-08-11, 권 발행 **2012년 1월**. DOI **10.1146/annurev-psych-120710-100452** · **[PR]** (원문 PDF 전문 확인 완료)

> ⚠️ **인용 전략 권고:** 2003년판은 **정본(canonical) 각주**로 병기하고, **수치 인용은 2012년판을 쓰라.** 2003년판 본문 전문은 이번 조사에서 확보하지 못했다.

**★★ 핵심 수치 — 동일 출처 vs 상이 출처 상관 팽창률 (2012, 표 2 VERBATIM)**

| 관계 | 동일 출처 k / N / r / ρ | 상이 출처 k / N / r / ρ | **% 팽창** |
|---|---|---|---|
| Leader behaviors → outcome variables | 255 / 2,874 / 0.414 / **0.456** | 255 / 2,354 / 0.156 / **0.191** | **239%** |
| Personality variables → job performance | 123 / 1,504 / 0.259 / 0.312 | 139 / 898 / 0.113 / 0.147 | **212%** |
| Job attitudes → OCB | 98 / 6,729 / 0.270 / 0.340 | 155 / 13,551 / 0.190 / 0.230 | **148%** |
| Participative decision making → work outcomes | 91 / 391 / 0.343 / 0.343 | 140 / 1,453 / 0.165 / 0.165 | **208%** |
| Organizational commitment → job performance | 148 / 3,745 / 0.180 / 0.183 | 159 / 1,924 / 0.138 / 0.138 | **133%** |
| Person-organization fit → job performance | 12 / 639 / 0.230 / 0.283 | 21 / 813 / 0.073 / 0.093 | **304%** |
| OCB → performance evaluations | 95 / 2,808 / 0.490 / 0.595 | 56 / 2,889 / 0.260 / 0.323 | **184%** |

> "The results indicate that the average corrected correlation between leader behaviors and outcome variables … when taken from the same source is **0.456**, but only **0.191** when obtained from different sources. This means that the average corrected correlation … is **239% (0.456/0.191) larger** when these measures are obtained from the same source…"
> ※ 본문 서술의 213%·147%는 표 2의 **212%·148%**와 반올림 표기가 다르다. **표 값을 우선 인용하라.**

**★★ 가장 강력한 단일 문장 — 자기보고 단일 출처**
> "First, these estimates are **conservative** because they are based on MTMM studies that used two or more less-than-perfectly correlated methods, and in many cases the biggest concern regarding method bias is in studies that use **only a single method** (which implies a true Rmk,ml of 1.00). Indeed, **if a single method had been used to calculate these estimates, they would have ranged from 94% to 270%.**"

**MTMM 기반 분산 분해 (표 1, VERBATIM)**

| 연구 | 표본 | 특질 요인 분산 | **방법 요인 분산** | 오차 분산 |
|---|---|---|---|---|
| Cote & Buckley (1987) | 70 matrices | 42% | **26%** | 32% |
| Williams et al. (1989) | 11 matrices | 48% | **25%** | 21% |
| Buckley et al. (1990) | 61 matrices | 42% | **22%** | 36% |
| Doty & Glick (1998) | 28 matrices | 46% | **32%** | 22% |
| Lance et al. (2010) | 18 matrices | 40% | **18%** | 42% |

> "This suggests that **the correlation between the traits was inflated approximately 45% (0.127/0.281) by method bias.** Similar estimates … are **38% in Buckley et al. (1990), 92% in Doty & Glick (1998), and 60% in Lance et al. (2009).**"

**추가 확인 수치**
- **Sharma et al.(2009)**, 기술수용모형 48개 연구 75표본: "the mean correlation between the focal constructs was about **0.16** when the susceptibility… was **low** and about **0.59** when… **high**, and (b) about **56% of the between-studies variance** in this literature was attributable to method biases." 결론: method bias **"presents a major potential validity threat to the findings of IS research"**
- 역문항 효과: "the average correlation among these five constructs was **0.21** when item word bias was controlled but increased to **0.50** when it was not controlled (**an increase of 238%**)."
- 리더십 메타분석(Lowe et al. 1996): 출처 분리가 "decreased the correlation between leadership style and effectiveness by **67% (from 0.57 to 0.19)**"
- 팀 프로세스–혁신(Hülsheger et al. 2009): "decreased the relationship by about **49% (from 0.45 to 0.23)**"
- 종합 재현: "the average corrected correlation … was **0.359** when they were obtained from the same source, it decreased to **0.184** when they were obtained from different sources (**a 49% decrease**)."
- 문헌 현황: "studies (**76%**) involved only a single measurement procedure"

**★★ 이 책에 쓸 수 있는 부분 — 측정 설계의 하드 룰.**
**AX 설문에서 "AI를 얼마나 쓰나요?"와 "생산성이 얼마나 올랐나요?"를 같은 사람에게 같은 설문지로 묻는 순간 상관이 인위적으로 부푼다.** 그 팽창 폭이 **동일 출처 대비 133~304%**, 단일 방법만 쓰면 **94~270%**다. **"AI 활용도와 생산성이 상관관계가 있다"는 사내 분석의 대부분이 이 함정에 있다.**

**한계·반박.** 팽창률 추정에 상당한 변동이 있다("ranging from 38% to 92%"). 추정치들이 서로 독립이 아니다(MTMM 연구가 겹친다). 저자들 스스로 "**regardless of which estimate is used, the bottom line is that the amount of method bias is substantial**"로 마무리한다. 다만 **일부 방법론자는 CMB의 심각성이 과장되었다고 주장**한다는 점도 함께 적어야 균형이 맞는다.

---

### B-1-8. ★ Mabe & West (1982) — 자기평가 타당도, 그리고 **신뢰도는 설계 가능하다**

**서지**
> Paul A. Mabe III & Stephen G. West. "**Validity of self-evaluation of ability: A review and meta-analysis.**" *Journal of Applied Psychology*, **67(3), 280–296**, **1982년 6월**.
> DOI: **10.1037/0021-9010.67.3.280** · **[PR]**

**핵심 주장.** 자기평가 능력과 실제 성과 측정치를 비교한 **55개 연구** 종합 결과, **평균 타당도 계수는 r = .29 (SD = .25)**로 낮고 변동이 크다. **그러나 측정 조건이 타당도 변동의 64%를 설명한다** — 즉 **자기평가의 신뢰도는 고정된 것이 아니라 설계 가능한 변수다.**

**★ 인용 가능한 수치 (VERBATIM — 출판사 초록 기반)**
> "a low mean validity coefficient (**mean r = .29**) with high variability (**SD = .25**)" — 55개 연구.
> 타당도를 높이는 **조건 9가지가 변동의 64%를 설명**하며, 명시적으로 확인된 것: **"the rater's expectation that the self-evaluation would be compared with criterion measures"** (자기평가가 준거 측정치와 **대조될 것이라는 평가자의 기대**), 자기평가 경험, 익명성 보장, 동료 비교를 강조하는 지시.
> 사람 변수: "**high intelligence, high achievement status, and internal locus of control** were associated with more accurate evaluations."

**★★ 이 책에 쓸 수 있는 부분 — 측정 등급제의 가장 직접적인 이론적 정당화.**
**"자기보고는 낮은 신뢰도를 갖지만, 그 신뢰도를 높이는 조건이 실증적으로 알려져 있다."**
가장 실무적인 함의: **자기보고 항목이라도, 응답자가 "이 답은 나중에 실측 로그와 대조된다"는 것을 알고 있으면 신뢰도가 올라간다.** → **측정 등급제에서 "자기보고 + 대조 예고" 항목을 순수 자기보고보다 한 등급 위로 두는 근거.**

**한계·반박.** 1982년 메타분석이고 r = .29는 이질적 능력 영역을 뭉뚱그린 값이다. ⚠️ **원문 PDF 전문 미확인** — 초록 수준의 확인이며, **9개 조건의 완전한 목록과 각 조절효과 크기는 원문 대조가 필요하다.** → F절.

---

### ★ B-1 정리 — 이 책의 측정 등급제 설계로

| 등급 | 문헌이 지지하는 설계 규칙 | 근거 |
|---|---|---|
| **실측 (최상)** | 시스템 로그·출입기록 등 객관 기록 | Chase & Godbey(클럽 출입기록 대조): **자기보고가 객관 로그 대비 100% 이상 과대** |
| **표본 (중간)** | 시간일지·직접 관찰 등 표본 기반 실측 | Robinson 계열 전체가 "일지 = 기준선"으로 설계 |
| **자기보고 (최하)** | **수준은 못 믿고 순위는 쓸 수 있다** | Buehler: 편향에도 **r = .77**로 실제와 높은 상관 |
| **자기보고 가산 조건** | ① "지난주" 앵커 + 후속 질문 ② **실측 대조 예고** ③ 실행 당사자가 아닌 제3자 추정 ④ 원인·결과를 다른 출처에서 | Frazis & Stewart / Mabe & West / Jørgensen / Podsakoff |
| **자기보고 감산 조건** | ① "통상적으로 얼마나?" 형태 ② 원인·결과를 **같은 설문지**로 ③ **KPI·보상에 연동** | Frazis & Stewart / Podsakoff(133~304% 팽창) / Ordóñez(B-2-8) |

---

## B-2. 측정 왜곡 · 대리지표

---

### B-2-1. Goodhart (1975) — 원전

**서지**
> Charles A. E. Goodhart. "**Problems of Monetary Management: The U.K. Experience.**" In *Papers in Monetary Economics*, Vol. I. Sydney: **Reserve Bank of Australia**, 1975, pp. 1–20.
> 재수록: Courakis, Anthony S. (ed.), *Inflation, Depression, and Economic Policy in the West*. Totowa, NJ: Barnes and Noble Books, 1981, p. 116.
> 관련 재진술: Goodhart, C. A. E. (1984). *Monetary Theory and Practice: The UK Experience*. London: Macmillan, **p. 94**. · **[WP]** (중앙은행 학술회의 논문)

**★ 원문 문구 (VERBATIM, 3곳 교차 확인)**
> "**Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes.**"
> (관찰된 통계적 규칙성은 **통제 목적으로 압력이 가해지는 순간 붕괴하는 경향**이 있다.)

교차 확인한 인용처 3곳(모두 원문 fetch로 확인): ① Manheim & Garrabrant (2018) 각주 1 및 참고문헌 [1] ② Bevan & Hood (2006) **p. 521** ③ Crone & Pidd (2005) **p. 486**.
> ※ Bevan & Hood는 **"on it"**, Manheim & Garrabrant는 **"upon it"**으로 적었다. **판본 차이 가능성 — 인용 시 표기 주의.**

**★ 이 책에 쓸 수 있는 부분.** **원전은 통화 총량에 관한 것이지 "지표를 목표로 삼으면 안 된다"는 일반 경영 격언이 아니었다**는 사실 자체가 중요한 서술 소재다. Manheim & Garrabrant가 명시하듯 "This has been interpreted and explained more widely, perhaps to the point where **it is ambiguous what the term means.**"

**한계.** ⚠️ 1975년 원문 PDF 자체에는 접근하지 못했다. → F절.

---

### B-2-2. ★ Strathern (1997) — "측정이 목표가 되면" 정본 (원문 직접 확인)

**서지**
> Marilyn Strathern. "**'Improving ratings': audit in the British University system.**" *European Review*, **5(3), 305–321**, **1997년 7월**.
> DOI: **10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4** · **[PR]**
> 각주: "This is adapted from the **Founders' Memorial Lecture given at Girton College, Cambridge, on 11 March 1997.**"

**★★ 원문 문단 전체 (VERBATIM, p. 308)**
> "**When a measure becomes a target, it ceases to be a good measure.** The more a 2.1 examination performance becomes an expectation, the poorer it becomes as a discriminator of individual performances. **Hoskin describes this as 'Goodhart's law'**, after the latter's observation on instruments for monetary control which lead to other devices for monetary flexibility having to be invented. However, targets that seem measurable become enticing tools for improvement. The linking of improvement to commensurable increase produced practices of wide application."

**★★ 서술상 매우 중요한 발견 — 인용의 인용 문제.**
이 격언은 흔히 "Strathern의 굿하트 법칙 재진술"로 인용되지만, **원문에서 Strathern은 이를 자기 정식화로 제시하지 않고 Keith Hoskin의 명명을 인용하는 맥락에서 던진다.** 위키피디아 등 2차 출처는 "Strathern이 이 표현을 Goodhart의 작업에 명시적으로 귀속시켰다"고 서술하는데, **원문의 실제 문장 구조는 그보다 간접적이다.**
> **이 디테일 자체가 "인용의 인용을 쫓다 보면 원전이 흐려진다"는 이 책의 논지에 딱 맞는 메타 사례다.** 그리고 이 책의 규율(원전 서지 확보)이 왜 필요한지를 보여주는 실례이기도 하다.

**★ 논문 초록 (VERBATIM) — AX 측정 챕터의 경구로 최적**
> "This paper gives an anthropological comment on what has been called the '**audit explosion**', the proliferation of procedures for evaluating performance… **While the metaphor of financial auditing points to the important values of accountability, audit does more than monitor—it has a life of its own that jeopardizes the life it audits.** The runaway character of assessment practices is analysed in terms of cultural practice."
> (**감사는 감시 이상의 일을 한다 — 감사는 자기 자신의 생명을 가지며, 그것이 감사하는 대상의 생명을 위태롭게 한다.**)

**한계·반박.** 인류학 에세이이고 실증 데이터가 없다. 영국 대학 평가 맥락에 특수하다.
⚠️ **Hoskin의 1차 출처는 확인하지 못했다** — 원전 추적을 완결하려면 필요하다. → F절.

---

### B-2-3. ★★ Manheim & Garrabrant (2018) — 굿하트 법칙 **네 변종** (최우선 항목, 전문 확인 완료)

**서지**
> David Manheim & Scott Garrabrant. "**Categorizing Variants of Goodhart's Law.**" **arXiv:1803.04585** [cs.AI].
> DOI: **10.48550/arXiv.1803.04585** · **버전: v1 2018-03-13 / v2 2018-03-27 / v3 2018-04-09 / v4 2019-02-24.** 문서 내 날짜 표기 "February 26, 2019."
> 저자 소속: David Manheim / Scott Garrabrant (**MIRI**) · 근원: Garrabrant, "Goodhart Taxonomy", 2017-12-30, LessWrong
> **[PP]** — **프리프린트. 동료심사 저널 게재 없음.**

**★ 저자들의 굿하트 효과 정의 (VERBATIM)**
> "As used in this paper, **a Goodhart effect is when optimization causes a collapse of the statistical relationship between a goal which the optimizer intends and the proxy used for that goal.**"

**형식화 (VERBATIM 요지).** 시스템 S와 상태 s ∈ S. 규제자는 허용 영역 A ⊆ S를 선택해 시스템에 영향을 준다. **Goal** = 규제자의 참 목표 G(s) → ℝ. 규제자는 불완전한 지식 때문에 G(s)로 행동할 수 없고 **대리지표 M(s) → ℝ**로만 행동한다. 규제자는 임계 c를 골라 `s ∈ A iff M(s) ≥ c`로 허용 상태를 정의한다.

**★★ 네 변종 — 한 문장 요약 (VERBATIM)**
> "The four categories of Goodhart effects introduced by Garrabrant are 1) **Regressional**, where selection for an imperfect proxy necessarily also selects for noise, 2) **Extremal**, where selection for the metric pushes the state distribution into a region where old relationships no longer hold, 3) **Causal**, where an action on the part of the regulator causes the collapse, and 4) **Adversarial**, where an agent with different goals than the regulator causes the collapse. **These varied forms often occur together, but defining them individually is useful.**"

#### ① Regressional Goodhart — 회귀적

> "**Regressional Goodhart** - When selecting for a proxy measure, you select not only for the true goal, but also for **the difference between the proxy and the goal.** This is also known as '**Tails come apart.**'"

형식 모델: `M = G + normal(μ, σ²)`

> "Due to the noise, a point with a large M value will likely have a large G value, but also a large noise value. Thus, when M is large, you can expect G to be predictably smaller than M. … **While this is the simplest Goodhart effect, it is also the most fundamental: it cannot be avoided. No matter what measure is chosen for optimization, an inexact metric necessarily leads to a divergence between the goal and the metric in the tail.**"

> **★ AX 적용.** **"완벽한 지표를 찾으면 된다"는 환상을 깨는 데 결정적이다.** 상위 성과자만 골라내는 순간(=임계값 c를 높게 잡는 순간) **노이즈도 함께 뽑힌다.** "AI 활용 우수 부서 top 10"을 뽑으면, 그 명단에는 실제로 잘한 부서와 **측정 오차가 컸던 부서가 섞여 있다. 이것은 지표를 개선해도 사라지지 않는다.**

#### ② Extremal Goodhart — 극단적

> "**Extremal Goodhart** - Worlds in which the proxy takes an extreme value may be very different from the ordinary worlds in which the relationship between the proxy and the goal was observed. A form of this occurs in statistics and machine learning as '**out of sample prediction.**'"

**두 하위 유형 (VERBATIM)**
> "**Extremal Goodhart - Model Insufficiency** - The metric of interest is based on a learned relationship between the goal and the metric which is approximately accurate in the initial region. **Selection pressure moves the metric away from the region in which the relationship is most accurate so that the relationship collapses.**"
> 예시: "In machine learning this often happens due to **underfitting**, such as when a relationship is assumed to be a low degree polynomial because higher order polynomial terms are small in the observed region."

> "**Extremal Goodhart - Change in Regime** - The proxy M may be related to G differently in different regions. **Even if the correct relationship is learned for the observed region, in the region where the proxy takes an extreme value the relationship to the goal may be fundamentally different.**"
> 예시(VERBATIM): "**wind-speed measurements may be systematically biased downwards when the wind-speed exceeds the design tolerances of the instruments.**"

> **★ AX 적용.** **"파일럿에서 검증된 지표를 전사로 확대"할 때 정확히 이 일이 일어난다.** 파일럿 구간에서 관측된 "AI 사용량 ↔ 생산성" 관계가, 사용량이 극단으로 밀린 영역에서는 **근본적으로 다른 관계**일 수 있다.

#### ③ Causal Goodhart — 인과적

> "**Causal Goodhart** - When the causal path between the proxy and the goal is indirect, intervening can change the relationship between the measure and proxy. If a regulator intervenes to maximize a metric, the causal pathway can change such that the proxy no longer tracks the goal. In such cases, **extreme interventions can be less effective than more moderate ones, and further selection or intervention can be counterproductive.**"

> "Interestingly, **this does not require any uncertainty, nor does it require an incorrect understanding of the relationships**, unlike earlier cases. Instead, **the effect is induced by the regulator's action.**"

**세 하위 유형 (VERBATIM 정의)**
> "**Shared Cause Intervention** - The regulator intervenes on a shared cause of the metric and the goal."
> 예시(VERBATIM): "Suppose… there are two tests administered to students which are correlated. **If a teacher trains skills related to test taking generally**, one of the traits which make the students likely to do well on both tests changes. Because of this, the remaining relationship between scores on the two tests is due to other factors, and **the new correlation between scores is likely to be lower than the earlier correlation.**"

> "**Intermediary Intervention** - The regulator intervenes on a variable in the causal chain connecting Goal to Metric." — "This does not necessarily affect the Goal at all, but **can serve to increase the value of the metric.**"

> "**Metric Manipulation** - The regulator intervenes to set the Metric, without affecting other nodes."
> 예시(VERBATIM): "Imagine… that **a teacher changes test scores or grades.** This doesn't contribute to the goal of learning, it simply changes M so that it is **useless** … in measuring G."

**보너스 — 지표 설계 오류 3유형 (VERBATIM)**
> "**Ignored Shared Cause** - The regulator assumes the relationship between the Goal and Metric is a causal chain, or is direct, but **there is instead a shared cause.**"
> "**Ignored Intermediary** - The regulator assumes the relationship … is direct, but **an intermediary exists which creates an additional source of noise.**"
> "**Ignored Additional Cause** - The metric is caused by multiple factors, of which the goal relates to only some. Alternatively, the goal is caused by multiple factors, of which the metric relates to only some."

#### ④ Adversarial Goodhart — 적대적

> "First, the actor may have goals which the regulator is unaware of … and the agent can act independently of the regulator in a way that adversely affects the regulator's goal. We refer to such cases as **adversarial misalignment.** Second, the regulator can use incentives to align the agent's goals and use their actions as a way to optimize, while not acting themself. We refer to these as '**Cobra effects.**'"

> "**Adversarial Misalignment Goodhart** - The agent applies selection pressure **knowing the regulator will apply different selection pressure on the basis of the metric.**"

> "**Campbell's Law** - Agents select a metric knowing the choice of regulator metric. **Agents can correlate their metric with the regulator's metric, and select on their metric.** This further reduces the usefulness of selection using the metric for acheiving the original goal."
> 모델: `M_R = G_R + X`, `M_A = G_A · X` — "if X ∼ normal(μ, σ²), **the correlation between G_A and M_A is zero over the full set of states, but becomes positive on the subspace selected by the regulator.**"

> "**Normal Cobra Effect** - The regulator modifies the agent goal, usually via an incentive, to correlate it with the regulator metric. The agent then acts by **changing the observed causal structure due to incompletely aligned goals** in a way that creates a Goodhart effect."
> 코브라 효과 유래(VERBATIM): "This is named after **a supposed situation** in colonial India where British authorities offered a reward for dead cobras. Instead of hunting cobras, however, some people **bred and killed their own cobras**… This not only failed to achieve the goal, but **led to more cobras than before the reward was offered.**"
> ⚠️ **저자들 스스로 "supposed"·"(supposedly) historical"이라고 단서를 단다.** 이 일화의 사실성은 논란거리이므로 **책에서 인용할 때 이 단서를 함께 옮겨라.**

> "**Non-Causal Cobra Effect** - The regulator modifies the agent goal to make agent actions aligned with the regulator's metric. Under selection pressure from the agent, **extremal Goodhart effects occur or regressional Goodhart effects are worsened.**"

**★★ 결론부 (VERBATIM) — 이 책에 그대로 쓸 수 있는 최고의 문장**
> "**The importance of Goodhart effects depends on the amount of power directed towards optimizing the proxy, and so the increased optimization power offered by artificial intelligence makes it especially critical for that field.**"
> (굿하트 효과의 중요성은 **대리지표 최적화에 투입되는 힘의 양**에 달려 있으며, 따라서 **인공지능이 제공하는 증대된 최적화 능력은 이를 특히 결정적으로 만든다.**)
> → **"AI가 최적화 능력을 키우면, 지표 왜곡의 파괴력도 함께 커진다."** AX 지표 설계 챕터의 결론 문장으로 최적이다.

**★★ 이 네 유형을 AX 지표 설계에 그대로 이식하는 방법**

| 변종 | AX에서의 전형적 발현 | 대응 |
|---|---|---|
| **Regressional** | "AI 활용 우수 부서 top 10"에 측정 오차 큰 부서가 섞임 | **회피 불가.** 임계값 기반 선발 자체를 줄이고 구간 추정으로 |
| **Extremal** | 파일럿 구간의 "사용량↔성과" 관계가 전사 확대 후 붕괴 | 극단 영역에서 **관계를 재추정.** 파일럿 계수를 외삽 금지 |
| **Causal** | "AI 활용률을 올려라"는 지시가 활용률과 성과의 연결을 끊음 | **개입 자체가 지표를 망가뜨린다**는 것을 인정. 온건한 개입 |
| **Adversarial** | 팀이 활용률 지표를 만족시키는 최소 행동을 학습 | **관측되지 않는 결과 지표**와 병행 측정 |

**한계·반박 (반드시 표기)**
- **동료심사를 거치지 않은 프리프린트다.** 저자들 스스로 인정: "Because none of the terms were laid out formally, **the categories proposed do not match what was originally discussed.**" → **이 분류는 Goodhart 원전의 분류가 아니라 저자들의 재구성**임을 명시해야 한다.
- 캠벨 법칙의 학문적 선행성 언급(VERBATIM): "Other closely related formulations, such as Campbell's law (**which arguably has scholarly precedence**) and the Lucas critique, were also initially specific…"
- 형식 모델은 단순화되어 있고 **실증 검증이 없다.**

---

### B-2-4. Campbell (1979) — 캠벨의 법칙

**서지**
> Donald T. Campbell. "**Assessing the impact of planned social change.**" *Evaluation and Program Planning*, **2(1), 67–90**, **1979**.
> DOI: **10.1016/0149-7189(79)90048-X** · 선행판: Campbell (1976), Occasional Paper Series #8, The Public Affairs Center, Dartmouth College (ERIC ED303512) · **[PR]**

**★ 법칙 원문 (VERBATIM)**
> "**The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor.**"
> (어떤 정량적 사회지표든 사회적 의사결정에 **더 많이 사용될수록**, 그것은 **부패 압력에 더 노출되고**, 그것이 **감시하려던 사회적 과정을 왜곡하고 부패시킬 가능성이 더 커진다.**)

**확인 상태.** 이 문구는 **Manheim & Garrabrant(2018) 각주 5에서 원문 fetch로 verbatim 확인**했으며, 그들의 참고문헌 [6]이 위 서지다. 여러 2차 출처는 **p. 85**로 지목한다.
⚠️ **Campbell 1979 원문 PDF 자체에는 접근하지 못했다. 페이지 번호(p. 85)는 미확인.** → F절.

**★ 이 책에 쓸 수 있는 부분.** **Goodhart보다 조직·사회 지표에 훨씬 직접적이다.** AX 성숙도 지표·AI 활용률 KPI 등 **"조직을 감시하려는 지표"**에 대한 경고로는 Goodhart보다 **정확한 인용**이다. 그리고 **Campbell이 Goodhart보다 학문적 선행성을 갖는다는 논쟁**(Rodamar, "There ought to be a law! Campbell v. Goodhart", *Significance* 15, 2018, DOI 10.1111/j.1740-9713.2018.01205.x) 자체가 좋은 서술 소재다.

**한계.** 1979년 사회정책 평가 맥락. 실증 데이터가 아니라 방법론적 논평이다.

---

### B-2-5. Ridgway (1956) — 성과측정 역기능의 최초 지적

**서지**
> V. F. Ridgway. "**Dysfunctional consequences of performance measurements.**" *Administrative Science Quarterly*, **1(2), 240–247**, **1956년 9월**.
> DOI: **10.2307/2390989** · **[PR]**

**핵심 주장 (2차 출처 확인).** 성과 측정치는 **단일(single)·복수(multiple)·복합(composite)** 어느 형태든 역기능을 낳는다. *Policy and Society*(2015, Oxford) 리뷰의 요약:
> "**single measures** motivate individuals to behave in ways that are wasteful and detrimental to the goals espoused, while **multiple measures** lead to trade-offs between criteria and objectives that may be contradictory, and **composite measures** can cause tension, role and value conflicts."
> ⚠️ **이는 Ridgway 원문의 직접 인용이 아니라 리뷰 논문의 요약이다.** 원문 verbatim이 필요하면 ASQ/JSTOR 접근이 필요하다. → F절.

**★ 이 책에 쓸 수 있는 부분.** **1956년에 이미 알려져 있었다**는 사실의 서사적 힘. "AI 시대의 새로운 문제"가 아니라 **"70년 된 문제가 AI의 최적화 압력으로 증폭된 것"**이라는 프레이밍(→ B-2-3 결론부와 직결). 특히 **"복합 지표(composite)도 답이 아니다"**는 주장은 **AX 성숙도 종합점수 설계에 대한 직접 경고**다(→ B-2-7 (e)의 "별점과 임상 품질 상관 0"과 짝을 이룬다).

---

### B-2-6. ★ Smith (1995) — 성과데이터 공개의 **8가지 역기능**

**서지**
> Peter Smith. "**On the unintended consequences of publishing performance data in the public sector.**" *International Journal of Public Administration*, **18(2–3), 277–310**, **1995**.
> DOI: **10.1080/01900699508525011** · **[PR]**

**★ 여덟 가지 목록 (VERBATIM)**
출처: Crone, Deborah & Pidd, Michael (2005), *International Journal of Productivity and Performance Management*, **54(5/6)**, DOI 10.1108/17410400510604601, **p. 486**의 원문 fetch로 확인.
도입 문장(VERBATIM): "**It is important to realise that this is not an argument against performance measurement per se, more an indictment of the clumsy way that such schemes are sometimes implemented.**"

1. **Tunnel vision (터널 시야)**: "which occurs when service managers, faced with many different targets, **choose the ones that are easiest to measure and ignore the rest.**"
2. **Sub-optimisation (부분 최적화)**: "when service managers choose to operate in ways that **serve their own operation well but damage the performance of the overall system.**"
3. **Myopia (근시안)**: "when, for whatever reason, managers focus their efforts on **short-term targets at the expense of longer-term objectives.**"
4. **Measure fixation (지표 고착)**: "when outcomes are difficult to measure there is a natural tendency to use PIs based on measurable outputs. **Measure fixation occurs when the PI itself becomes the focus rather than the desired outcome.**"
5. **Misrepresentation (허위표시)**: "this is a form of fraud and occurs when performance data is either **misreported or distorted to create a good impression.**"
6. **Misinterpretation (오해석)**: "this is most evident in **performance league tables.** The statistical measures are imprecise …, which means that **there may be no real difference between many of the units sequenced in the table** – though this may not be obvious from the single-point estimates used."
7. **Gaming (게이밍)**: "this occurs when a canny manager **deliberately under-achieves in order to secure a lower target in the next round** of activity."
8. **Ossification (경직화)**: "which happens when a PI is **past its sell-by date and has lost its purpose, but no one can be bothered to revise or remove it.**"

**★★ 이 책에 쓸 수 있는 부분 — AX 측정 체계 리뷰의 체크리스트로 그대로 이식 가능한 8항목.**
특히 사내 AX 지표 운영에서 가장 자주 관찰되면서 문헌 인용이 드문 두 항목:
- **⑥ Misinterpretation** — **부서별 AI 활용률 순위표의 통계적 무의미성.** 순위는 매겨지지만 그 차이가 유의하지 않다.
- **⑧ Ossification** — **한번 만든 KPI를 아무도 안 지우는 문제.** AX 대시보드가 계속 늘어나기만 하는 이유.

**한계·반박.** ⚠️ **여덟 항목의 정의 문구는 Smith 원문이 아니라 Crone & Pidd(2005)의 요약이다.** Smith 원문 verbatim이 필요하면 Taylor & Francis 접근이 필요하다(403). → F절. 또한 **이는 "측정 자체에 대한 반론이 아니라 서투른 실행에 대한 고발"이다 — 책에서 "측정하지 말라"는 논지로 오용하면 안 된다.**

---

### B-2-7. ★★ Bevan & Hood (2006) — 게이밍의 실증 (전문 확인 완료)

**이 절에서 가장 값나가는 실증 자료다.**

**서지**
> Gwyn Bevan & Christopher Hood. "**What's measured is what matters: targets and gaming in the English public health care system.**" *Public Administration*, **84(3), 517–538**, **2006년 9월**.
> DOI: **10.1111/j.1467-9299.2006.00600.x** · LSE Research Online: https://eprints.lse.ac.uk/16211/
> 저자 소속: Bevan(LSE), Hood(All Souls College, Oxford) · **[PR]**

**초록 (VERBATIM)**
> "In the 2000s, governments in the UK, particularly in England, developed **a system of governance of public services that combined targets with an element of terror.** This has obvious parallels with the Soviet regime, which was initially successful but then collapsed. Assumptions underlying governance by targets represent **synecdoche** (taking a part to stand for a whole); and that problems of measurement and gaming do not matter. We examine the robustness of the regime of targets and terror to these assumptions…"

#### (a) 먼저, 목표제는 정말 효과가 있었다 (균형 잡힌 인용을 위해 필수)

> "In 2002, **23 per cent of patients spent over four hours in A&E departments**, but in the three months from April to June 2004 **only 5.3 per cent** stayed that long" (National Audit Office 2004, p. 2 인용)
> "For 1999–2000, prior to star rating, **some trusts only managed 40 per cent.** After achieving 75 per cent became a key target… performance jumped dramatically, and, at the end of that year, **the worst achieved nearly 70 per cent.**"
> "in 2003, in England, **less than 1 per cent** of patients waited more than 12 months for an elective admission, the equivalent figures for **Scotland, Wales and Northern Ireland were 10, 16 and 22 per cent** of patients respectively." (목표제가 없던 다른 UK 국가들과의 자연실험 대조)

#### (b) ★★ 그러나 측정 자체가 무너졌다 — 공식 수치 vs 환자 설문

> "in 2002/03, **officially, in 139 out of 158 acute trusts 90 per cent of patients were seen in less than four hours, but only 69 per cent of patients reported that experience in the survey; in 2004/05, the official level had increased to 96 per cent, but the survey-reported level was only 77 per cent.**"
> → **공식 지표와 실제 경험의 괴리가 21%p → 19%p로 유지되며 함께 상승했다.** **AX 측정에서 "대시보드 수치"와 "현장 체감"의 괴리를 논할 때 가장 강력한 실증 수치다.**

> "the proportion of emergency calls logged as Category A ranged from **fewer than 10 per cent to over 50 per cent** across ambulance trusts" — **분류 기준 자체가 5배 이상 편차 = 지표 정의의 자의성.**

> "the Audit Commission (2003), on the basis of 'spot checks' at **41 trusts** between June and November 2002, **found reporting errors in at least one indicator in 19 of those trusts.**" (**41곳 중 19곳 = 46%**)

> "**there was no systematic audit of measures on which performance data are based**, so such inquiries were both partial and episodic."
> → **"측정을 측정하는 장치"의 부재.** **AX 측정 체계에 메타 감사를 넣어야 하는 근거.**

#### (c) ★ 게이밍의 3유형 (원문 정의 VERBATIM)

> "**Ratchet effects** refer to the tendency for central controllers to base next year's targets on last year's performance, meaning that managers who expect still to be in place in the next target period have **a perverse incentive not to exceed targets even if they could easily do so** (Litwack 1993): '**a wise director fulfils the plan 105 per cent, but never 125 per cent**' (Nove 1958, p. 4)."
> → **소비에트 격언 인용문 자체가 최고의 서술 소재다.**

> "**Threshold effects** refer to the effects of targets on the distribution of performance… putting pressure on those performing below the target level to do better, but also **providing a perverse incentive for those doing better than the target to allow their performance to deteriorate to the standard**…, and more generally **to crowd performance towards the target.**"

> "**Attempts to limit the threshold effect by basing future targets on past performance will tend to accentuate ratchet effects and attempts to limit ratchet effects by system-wide targets will tend to accentuate threshold effects.**"
> → **★ 두 효과가 서로 트레이드오프라서 순수한 해법이 없다** — 지표 설계자에게 가장 중요한 통찰.

> "Attempts to achieve targets at the cost of significant but unmeasured aspects of performance … result in **output distortions**."

**게이밍의 정의 (VERBATIM)**
> "'Gaming' is here defined as **reactive subversion such as 'hitting the target and missing the point'** or reducing performance where targets do not apply."

#### (d) ★★ 구체적 게이밍 사례와 수치 (VERBATIM)

> "A study by the Commission for Health Improvement (2003c) found evidence that in **a third of ambulance trusts**, response times had been '**corrected**' to be reported to be less than eight minutes. … an expected pattern of 'noisy decline' (where there has been no 'correction'), and of a 'corrected' pattern with **a curious 'spike' at 8 minutes** – with the strong implication that **times between 8 and 9 minutes have been reclassified to be less than 8 minutes.**"
> → **★ 분포의 스파이크 = 조작의 통계적 지문.** **AX 지표 감사에서 "분포를 보라"는 실무 지침의 근거.**

> "a study of the distribution of waiting times in A&E found **frequency peaked at the four-hour target** (Locker and Mason 2005)"

> "Surveys by the British Medical Association reported widespread practice of a second and third type of gaming responses: **the drafting in of extra staff and the cancelling of operations** scheduled for the period over which performance was measured"

> "A fourth practice was to require **patients to wait in queues of ambulances outside A&E Departments** until the hospital … was confident that that patient could be seen within four hours … Such tactics may have **unintendedly caused delays in responding to seriously ill individuals**"

> "A fifth gaming response was observed in response to the so-called 'trolley-wait' target … The response took the form of **turning 'trolleys' into 'beds' by putting them into hallways.**"
> → **정의 조작(definition gaming)의 완벽한 예.**

> "the National Audit Office (2001) reported evidence that **nine NHS trusts had 'inappropriately' adjusted their waiting lists, three of them for some three years or more, affecting nearly 6000 patient records.**"

> **★★ "the waiting time target for new ophthalmology outpatient appointments at a major acute hospital had been achieved by cancellation and delay of follow-up appointments, which did not figure in the target regime. Recording of clinical incident forms for all patients showed that, as a consequence, 25 patients lost their vision over two years, and this figure is likely to be an underestimate.**"
> → **★★ "측정되지 않는 것으로 대가를 치른다"는 명제의 가장 강력한 실증 사례.**

> "There is anecdotal evidence that such publication results in **a reluctance by surgeons to operate on high risk cases, those who stand to gain most from surgery** (Marshall et al. 2000). Because **mortality rates are extremely low (about 2 per cent), one extra death has a dramatic impact on a surgeon's performance in a year**, and **risk-adjustment methods cannot resolve such problems.**"

#### (e) ★★ 종합 지표가 실제 품질과 상관 0이었다

> "reactive gaming seems to have been practised by **a significant minority of service-provider units (ranging from 7 to 33 per cent in the studies quoted)**…"

> "the star rating system meant that it was possible for **three-star trusts to have within them a scandalously poor clinical service, and zero-star trusts an excellent service.** Rowan et al. (2004) found **no relationship between performance in star ratings and the clinical quality of adult critical care provided by hospitals.**"
> → **★★ AX 성숙도 종합점수 설계에 대한 결정적 경고.** Ridgway(1956)의 "복합 지표도 답이 아니다"가 50년 뒤 수치로 확인된 셈이다.

**synecdoche(제유) 개념 (VERBATIM)**
> "What underlies these assumptions is the idea of **synecdoche (taking a part to stand for a whole).** Such assumptions would not be trivial even in a world where no gaming took place, but they become more problematic when gaming enters the picture."
> → **"부분으로 전체를 대신하기"** — 대리지표 문제를 부르는 **이 책만의 우아한 용어로 채택 가능하다.**

**한계·반박.** 영국 NHS 단일 사례. 저자들 스스로 증거 한계를 인정한다("even if we have to return a Scottish 'not-proven' verdict on assumption (i) … these data, limited as they are…"). **그리고 성과 개선이 실재했다는 점을 이 논문 스스로 강조한다 — 책에서 "목표제는 나쁘다"로 단순화하면 오독이다.**

---

### B-2-8. Ordóñez et al. (2009) — Goals Gone Wild

**서지**
> Lisa D. Ordóñez, Maurice E. Schweitzer, Adam D. Galinsky, & Max H. Bazerman. "**Goals Gone Wild: The Systematic Side Effects of Overprescribing Goal Setting.**" *Academy of Management Perspectives*, **23(1), 6–16**, **2009년 2월**.
> DOI: **10.5465/AMP.2009.37007999** · **[PR]** · 워킹페이퍼판: **Harvard Business School Working Paper 09-083** `[WP]`
> **반박 논문(반드시 병기):** Locke, E. A., & Latham, G. P. (2009). "**Has Goal Setting Gone Wild, or Have Its Attackers Abandoned Good Scholarship?**" *AMP*. DOI 10.5465/AMP.2009.37008000

**★ 초록 (VERBATIM)**
> "…we argue that **the beneficial effects of goal setting have been overstated and that systematic harm caused by goal setting has been largely ignored.** We identify specific side effects associated with goal setting, including **a narrow focus that neglects non-goal areas, a rise in unethical behavior, distorted risk preferences, corrosion of organizational culture, and reduced intrinsic motivation.** Rather than dispensing goal setting as a benign, over-the-counter treatment for motivation, managers and scholars need to conceptualize goal setting as a **prescription-strength medication that requires careful dosing, consideration of harmful side effects, and close supervision.** We offer a warning label to accompany the practice of setting goals."

**★ 사례 (VERBATIM) — 책의 오프닝 소재로 최적**
> "Sears set sales goals for its auto repair staff of **$147/hour**. This specific, challenging goal prompted staff to **overcharge for work and to complete unnecessary repairs on a companywide basis** (Dishneau, 1992). … Sears' '**goal setting process for service advisers created an environment where mistakes did occur**,' Brennan admitted."

> "Ackman (2002) compares Enron's incentive system to '**paying a salesman a commission based on the volume of sales and letting him set the price of goods sold.**' … '**Enron executives were meeting their goals, but they were the wrong goals**'…"

> (Ford Pinto) "CEO Lee Iacocca announced the specific, challenging goal of producing a new car that would be '**under 2000 pounds and under $2,000**'… the fuel tank … was located behind the real axle in **less than 10 inches of crush space** … executives … calculated that the costs of lawsuits associated with Pinto fires (**which involved 53 deaths and many injuries**) would be less than the cost of fixing the design. In this case, **the specific, challenging goals were met (speed to market, fuel efficiency, and cost) at the expense of other important features that were not specified (safety, ethical behavior, and company reputation).**"
> → **★ "명시된 목표는 달성되었고, 명시되지 않은 것들이 대가를 치렀다"** — 이 문장 구조 자체가 **AX KPI 설계 장의 뼈대**가 될 수 있다. Bevan & Hood의 "25명이 시력을 잃었다"와 같은 구조다.

> "In the late 1980s, **Miniscribe employees shipped bricks to customers instead of disk drives to meet shipping targets.** And in 1993, **Bausch and Lomb employees falsified financial statements to meet earnings goals.**"

> "Kayes (2006) cites the **1996 Mt. Everest disaster in which eight climbers died** … as an example of '**destructive goal pursuit**.'"

**★★ 실증 연구 인용 (VERBATIM) — B-1과 B-2를 직접 잇는 문장**
> "One of the few studies that looked for a direct link between goal setting and cheating found that participants were **more likely to misrepresent their performance level when they had a specific, challenging goal than when they did not, especially when their actual performance level fell just short of reaching the goal** (Schweitzer, Ordóñez, & Douma, 2004)."
> → **★★ 목표가 걸린 순간 자기보고 자체가 왜곡된다.** **"자기보고 등급을 낮게 치되, 그 등급이 KPI에 연동되면 더 낮게 쳐야 한다"는 이중 규칙의 근거.**

> "Goal setting can promote two different types of cheating behavior. **First, when motivated by a goal, people may choose to use unethical methods to reach it.** … **Second, goal setting can motivate people to misrepresent their performance level—in other words, to report that they met a goal when in fact they fell short.**"

> "…the point cannot be overstated: **goal setting motivates unethical behavior.**"
> "A number of factors serve as catalysts…: **lax oversight, financial incentives for meeting performance targets** …, **and organizational cultures with a weak commitment to ethics.**"

**★ Table 1: A Warning Label for Setting Goals (VERBATIM, 8항목) — AX KPI 설계 체크리스트로 그대로 이식 가능**
1. **Are the goals too specific?** "Narrow goals can blind people to important aspects of a problem. Be sure that goals are comprehensive and include all of the critical components for firm success (e.g., quantity and quality)."
2. **Are the goals too challenging?** "…Provide skills and training to enable employees to reach goals. **Avoid harsh punishment for failure to reach a goal.**"
3. **Who sets the goals?** "People will become more committed to goals they help to set. At the same time, people may be tempted to set easy to reach goals."
4. **Is the time horizon appropriate?** "Be sure that short-term efforts to reach a goal do not harm investment in long-term outcomes."
5. **How might goals influence risk taking?** "**Be sure to articulate acceptable levels of risk.**"
6. **How might goals motivate unethical behavior?** "Goals narrow focus, such that employees may be less likely to recognize ethical issues… **Multiple safeguards may be necessary**…"
7. **Can goals be idiosyncratically tailored for individual abilities and circumstances while preserving fairness?**
8. **How will goals influence organizational culture?** "**If cooperation is essential, consider setting team-based rather than individual goals.**"

**한계·반박 (반드시 병기)**
- 이 논문은 **동일 저널 동일 호에서 Locke & Latham(2009)에게 정면 반박**당했다 — 목표설정 이론의 창시자들이 **"공격자들이 좋은 학문을 포기했다"**고 제목에서부터 응수했다.
- 사례 중심 논증이 많고 실증 인과 증거는 Schweitzer et al.(2004) 등 소수에 의존한다.
- **저자들 스스로 "goal setting should be prescribed selectively"라고 하지 목표설정을 폐기하라고 하지 않는다.**

---

### ★ B-2 정리 — 계보와 이식표

| 문헌 | 연도 | 기여 | AX 이식 |
|---|---|---|---|
| **Ridgway** | 1956 | 성과측정 역기능 최초 지적. **단일·복수·복합 모두 역기능** | AX 성숙도 **종합점수**도 안전하지 않다 |
| **Goodhart** | 1975 | "통제 압력이 가해지면 통계적 규칙성이 붕괴" | 원전은 통화 정책 — **일반 격언이 아니었다** |
| **Campbell** | 1979 | "사회 지표는 많이 쓸수록 부패한다" | **조직 지표에 가장 직접적인 인용** |
| **Smith** | 1995 | **8가지 역기능 목록** | AX 지표 리뷰 **체크리스트** |
| **Strathern** | 1997 | "측정이 목표가 되면 좋은 측정이기를 그친다" | "감사는 자기 생명을 갖고 대상의 생명을 위협한다" |
| **Bevan & Hood** | 2006 | **게이밍 3유형 + 실측 수치** | 공식 96% vs 체감 77%; **종합점수 ↔ 실제 품질 상관 0** |
| **Ordóñez et al.** | 2009 | 목표설정의 부작용 + **경고 라벨 8항목** | AX KPI 설계 체크리스트 |
| **Manheim & Garrabrant** | 2018 | **굿하트 4변종 형식화** | **AI가 최적화 능력을 키우면 왜곡의 파괴력도 커진다** |

---

## ★ B-1 · B-2 커버리지

**확보 (충분)**
- **B-1:** 시간일지 vs 자기추정 3부작(1994 원전 / 2011 재검증 / **2014 반박**) — **반박까지 확보한 것이 오히려 설계 논지를 강화한다.** 계획 오류 정본 + 소프트웨어 공수 추정 + 공통방법편향(**팽창률 133~304%, 단일 방법 94~270%**) + 자기평가 타당도 메타분석(**r = .29, 조건이 변동의 64% 설명**)
- **B-2:** Goodhart 원문 문구 3곳 교차 확인 / Strathern **원문 p.308 직접 확인 + 귀속의 메타 사례 발견** / **Manheim & Garrabrant 4변종 전문 확보(하위 유형 포함)** / Campbell 법칙 verbatim / Smith 8항목 / **Bevan & Hood 게이밍 실증 전문** / Ordóñez 경고 라벨 8항목

**비어 있음 / 미완**
- ⚠️ **Goodhart 1975 · Campbell 1979 · Ridgway 1956 · Smith 1995 원문 PDF 모두 미접근.** 문구는 교차 확인했으나 **페이지 번호와 원문 자구는 2차 출처 경유다.**
- ⚠️ **Podsakoff et al. 2003 본문 미확보** (수치는 2012년판 사용).
- ⚠️ **Mabe & West 1982의 9개 조건 완전 목록 미확인.**
- ⚠️ **소프트웨어 공수 초과 수치(30–40%, 41%, CHAOS 89%) 원문 대조 실패** — 쓰려면 Moløkken-Østvold & Jørgensen 원문 확인 필요.
- ⚠️ **Podsakoff의 더 최신 후속**(*Annual Review of Organizational Psychology and OB*, "Common Method Bias: It's Bad, It's Complex, It's Widespread, and It's Not Easy to Fix", DOI 10.1146/annurev-orgpsych-110721-040030) — **저자·연도·권·페이지 미확인.** 최신성을 강조하려면 확인 후 사용하라.

---
## B-3. 인간+기계 팀의 성과 귀속 (Performance Attribution)

검색·확인 시점: **2026-09-05**. 모든 인용문은 로컬 원문(`bansal.txt`/`bansal_raw.txt`, `vaccaro.txt`, `hemmer.txt`, `pnas.txt`)의 텍스트 레이어에서 그대로 추출했고, 서지는 Crossref·Semantic Scholar·Europe PMC·arXiv API로 교차 확인했다.

---

### 3-1. 【최우선·확인 완료】 Bansal et al. (2021) — 설명은 팀 성과를 올리지 않는다

#### 서지
> Gagan Bansal, Tongshuang Wu, Joyce Zhou, Raymond Fok, Besmira Nushi, Ece Kamar, Marco Tulio Ribeiro, and Daniel S. Weld, "Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance," in ***Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems*** (CHI '21), May 8–13, 2021, Yokohama, Japan. New York: ACM, pp. **1–16**.
> DOI: [10.1145/3411764.3445717](https://doi.org/10.1145/3411764.3445717) · arXiv: **2006.14779** (최초 게시 2020-06-26, v3) · **[PR]** · 발행: **2021-05**
> OA 전문: https://idl.cs.washington.edu/files/2021-AIExplanationsTeamPerformance-CHI.pdf

✅ **의뢰하신 저자 8인 명단은 Crossref·Semantic Scholar 양쪽에서 순서까지 정확히 일치한다.** (Semantic Scholar만 2저자를 "Tongshuang Sherry Wu"로 표기하고, Crossref·게재본은 "Tongshuang Wu" — **게재본 표기를 쓸 것.**)

#### 핵심 주장
기존 XAI 연구는 "AI가 설명하면 인간-AI 팀 성과가 오른다"고 주장해 왔다. 그러나 그 개선은 **AI가 인간보다 훨씬 정확했던 실험**에서만 관측되었다 — 즉 팀이 AI 단독보다 나빴고, 설명은 그 격차를 줄인 것뿐이다. 이 논문은 AI 정확도를 **인간 평균과 같게 맞춰** 진짜 상보성이 나올 여지("complementary zone")를 만든 뒤 다시 물었다. 답: **상보적 성과는 나왔지만, 그것은 설명이 아니라 신뢰도(confidence) 표시만으로 이미 달성되었고, 설명은 아무것도 추가하지 못했다.** 대신 설명은 **AI 권고가 틀렸을 때조차 인간이 그것을 받아들일 확률을 높였다.**

#### 연구 설계 (과업 · N · 조건)
- **데이터셋 3종:** Beer(맥주 리뷰 감성 분류), Amzbook(아마존 도서 리뷰 감성 분류), LSAT(로스쿨 입학시험 논리 문항)
- **모집:** Amazon Mechanical Turk, 미국 거주, 사전 승인율 ≥97%, 승인 과업 ≥1,000건
- **조건(conditions):** Human alone / Team (Conf) / Team (Explain-Top-1, AI) / Team (Explain-Top-2, AI) / Team (Adaptive, AI) / Team (Adaptive, Expert)
- **품질 필터:** 중앙값 라벨링 시간 <2초이거나 전 문항 동일 라벨 부여한 응답자 제거
- **과업량:** 감성 분류는 50문항(불명확 예시 제외), LSAT는 피로 때문에 문항 수 축소
- **보상:** 기본 $0.50 + 정답당 $0.05 + 총 정확도 90% 초과 시 $0.50, 95% 초과 시 $1.00 + 설문 $0.25

#### 이 책에 쓸 수 있는 부분
- **AX 거버넌스의 핵심 설계 근거.** "AI에 설명 기능(XAI)을 붙이면 사람이 제대로 판단할 것"이라는 가정이 실증적으로 기각된다. 설명은 **적정 신뢰(appropriate reliance)가 아니라 맹목적 신뢰(blind trust)를 키운다.**
- **표 1(선행 연구 대조표)이 그 자체로 강력한 자료다.** 8개 선행 연구 전부에서 팀이 AI 단독보다 못했다 — "사람을 한 명 끼워 넣으면 안전해진다"는 통념의 정면 반박.
- **성과 귀속 관점:** 팀이 AI 단독보다 잘한 것이 아니라면 그 성과는 도구의 것이지 팀의 것이 아니다. AX 성과 배분 논의의 출발점.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 초록 전문 — 이 책에서 가장 많이 쓸 대목**
> "Many researchers motivate explainable AI with studies showing that human-AI team performance on decision-making tasks improves when the AI explains its recommendations. However, prior studies observed improvements from explanations only when the AI, alone, outperformed both the human and the best team. Can explanations help lead to complementary performance, where team accuracy is higher than either the human or the AI working solo? We conduct mixed-method user studies on three datasets, where an AI with accuracy comparable to humans helps participants solve a task (explaining itself in some conditions). **While we observed complementary improvements from AI augmentation, they were not increased by explanations. Rather, explanations increased the chance that humans will accept the AI's recommendation, regardless of its correctness.** Our result poses new challenges for human-centered AI: Can we develop explanatory approaches that encourage appropriate trust in AI, and therefore help generate (or improve) complementary performance?"

> 국역: "많은 연구자가 설명가능 AI를 정당화할 때, AI가 자기 권고를 설명하면 의사결정 과업에서 인간-AI 팀 성과가 향상된다는 연구들을 근거로 든다. 그러나 선행 연구들은 **AI 단독이 인간과 최선의 팀 둘 다를 능가했을 때에만** 설명의 개선 효과를 관측했다. 설명이 상보적 성과 — 팀 정확도가 인간 단독이나 AI 단독보다 높은 상태 — 로 이어지도록 도울 수 있는가? …**AI 증강으로부터 상보적 개선을 관측했지만, 그것은 설명에 의해 증가하지 않았다. 오히려 설명은 인간이 AI의 권고를, 그것이 옳든 그르든 상관없이 받아들일 확률을 높였다.**"

**(b) 표 1 — 선행 연구 8건 전부에서 상보성 실패 (인용가치 최상)**

| 도메인 | 과업 | 지표 | 인간 단독 | AI 단독 | 팀 | 상보적? |
|---|---|---|---|---|---|---|
| 분류 | Deceptive review [43] | Accuracy ↑ | 51.1% | 87.0% | 74.6% | ✗ |
| 분류 | Deceptive review [42] | Accuracy ↑ | 54.6% | 86.3% | 74.0% | ✗ |
| 분류 | Income category [83] | Accuracy ↑ | 65% | 75% | 73% | ✗ |
| 분류 | Loan defaults [27] | Norm. Brier ↑ | 0 | 1 | 0.682 | ✗ |
| 분류 | Hypoxemia risk [53] | AUC ↑ | 0.66 | 0.81 | 0.78 | ✗ |
| 분류 | Nutrition prediction [12] | Accuracy ↑ | 0.46 | 0.75 | 0.74 | ✗ |
| QA | Quiz bowl [21] | — | "AI outperforms top trivia players." | | | ✗ |
| 회귀 | House price [65] | Avg. Abs. Error ↓ | $331k | $200k | $232k | ✗ |

원문 표 캡션:
> "Recent studies that evaluate the effect of automatically generated explanations on human-AI team performance. **While explanations did improve team accuracy, the performance was not complementary — acting autonomously, the AI would have performed even better.** For papers with multiple domains or experiments, we took one sample with the most comparable human and AI performance."

> 국역: "…**설명이 팀 정확도를 개선하기는 했지만 그 성과는 상보적이지 않았다 — 자율적으로 행동했다면 AI가 오히려 더 잘했을 것이다.**"

**(c) 실험 설계 수치 — 전부 VERBATIM**
> "In total, we recruited **566 (Beer) and 552 (Amzbook) crowd workers**, and in both datasets, **84% of participants passed the screening and post-filtering**. Eventually, we collected data from **around 100 participants (ranging from 93 to 101 due to filtering) per condition.**"

> AI 정확도 고정: "We then selected 50 unambiguous examples so that the **AI's accuracy was 84%** (i.e., comparable to human accuracy), with equal false positive and false [negative rates]"
> 파일럿의 비보조 인간 정확도: "**87% for Beer and 85% for Amzbook**"
> LSAT: "achieved **65% accuracy** on these examples, comparable to the **67% human accuracy** that we observed in our pilot study."

> 보너스 설계의 의도(중요): "**Since we fixed the AI performance at 84%, humans could not obtain the bonus by blindly following the AI's recommendations.**" / "Participants spent **13 minutes** on average on the experiment and received an average payment of **$3.35** (equivalent to an hourly wage of **$15.77**)." / LSAT: "The average completion time for the LSAT task was **16 minutes**, with an average payment of **$6.30** (equals an hourly wage of **$23.34**)."

**(d) 상보성은 달성되었으나 — 설명이 아니라 신뢰도로**
> "The baseline team condition, Team (Conf), achieved complementary performance across tasks. For Beer, providing AI recommendations and confidence to users increased their performance to (**µ = 0.89 ± σ = 0.05**), surpassing both AI (**0.84**) and unassisted human accuracy (**0.82 ± 0.09**). Similarly, Team (Conf) achieved complementary performance for Amzbook and LSAT, with **relative gains of 2.2% and 20.1%** over unassisted workers."

> 국역: "기준 팀 조건인 Team (Conf)는 전 과업에서 상보적 성과를 달성했다. Beer의 경우 AI 권고와 신뢰도를 제공하자 성과가 **0.89 ± 0.05**로 올라 AI(**0.84**)와 비보조 인간 정확도(**0.82 ± 0.09**) 둘 다를 넘어섰다. Amzbook과 LSAT에서도 비보조 노동자 대비 각각 **2.2%, 20.1%의 상대적 향상**으로 상보적 성과를 달성했다."

**(e) 설명은 아무것도 추가하지 못했다 — p값 전부**
> "**We did not observe significant improvements over the confidence baseline by displaying explanations.** For example, for Beer, Team (Conf) and Team (Explain-Top-1, AI) achieved similar performance, with the accuracy being **0.89 ± 0.05 vs. 0.88 ± 0.06** respectively; the difference was insignificant (**z = −1.18, p = .24**). We observed the same pattern for Amzbook (**z = 1.23, p = .22**) and LSAT (**z = 0.427, p = .64**). As a result, we could not reject our hypothesis…that Explain-Top-1 performs similar to simply showing confidence. **This result motivates the need to develop new AI systems and explanation methods that provide true value to team performance by supplementing the model's confidence**, perhaps working in tandem with confidence scores."

> Top-1 vs Top-2 설명 간 차이도 무의미: Beer (**z = 0.85, p = .40**), Amzbook (**z = 0.81, p = .42**), LSAT (**z = 0.42, p = .68**).

> Adaptive 설명도 실패: "we did not observe any significant differences between Team (Adaptive, AI) and Team (Conf) for Beer (**z = −1.02, p = .31**) or Amzbook (**z = 1.08, p = .28**). We did not observe significant differences between Team (Adaptive, Expert) and Team (Conf) for LSAT (**z = 0.16, p = .87**)."

> **전문가가 직접 쓴 설명조차 효과 없음:** "More surprisingly, **switching the source of Adaptive explanation to expert-generated did not significantly improve sentiment analysis results.** For example…the differences in performance between Team (Adaptive, Expert) and Team (Adaptive, AI) were insignificant: Beer (**z = 1.31, p = .19**) and Amzbook (**z = −0.78, p = .43**)."

**(f) 설명이 오류를 증폭하는 메커니즘 — 이 책의 경고 문단**
> "Split the team performance by whether the AI made a mistake (Figure 4B), we observe that **explaining the top prediction lead to better accuracy when the AI recommendation was correct but worse when the AI was incorrect**, as in our pilot study. This is consistent with Psychology literature [39], which has shown that **human explanations cause listeners to agree even when the explanation is wrong**, and recent studies that showed explanations can mislead data scientists into overtrusting ML models for deployment [38]. While these results were obtained by measuring user's subjective ratings of trust, **to the best of our knowledge, our studies are the first to show this phenomenon for explanation and end-to-end decision making with large-scale studies.**"

> 국역: "AI가 오답을 냈는지 여부로 팀 성과를 나눠 보면, **상위 예측을 설명하는 것이 AI 권고가 맞았을 때는 정확도를 높였지만 AI가 틀렸을 때는 오히려 낮췄다.** …이는 **인간의 설명이 그 설명이 틀렸을 때조차 청자를 동의하게 만든다**는 심리학 문헌과 일치한다. …**우리가 아는 한, 이 현상을 설명과 종단 간(end-to-end) 의사결정에 대해 대규모 연구로 보인 것은 우리 연구가 처음이다.**"

> 그림 4B 캡션: "Splitting the analysis based on the correctness of AI accuracy, we saw that **for Beer and LSAT, Explain-Top-1 explanations worsened performance when the AI was incorrect**, the impact of Explain-Top-1 and Explain-Top-2 explanations were correlated with the correctness of the AI's recommendation, and Adaptive explanations seemed to have the potential to improve Explain-Top-1 when the AI was incorrect, and to retain the higher performance of Explain-Top-1 when the AI was correct."

**(g) 논의부 — 윤리적 함의 (챕터 마무리용)**
> "**One concerning observation was that explanations increased blind trust rather than appropriate reliance on AI.** This is problematic especially in domains where humans are required in the loop for moral or legal reasons (e.g., medical diagnosis) and suppose **the presence of explanations simply soothes the experts (e.g., doctors), making them more compliant so they blindly (or become more likely to) agree with the computer. Encouraging human-AI interactions like these seems deeply unsatisfactory and ethically fraught.** Importantly, while prior works also observed instances of inappropriate reliance on AI, **our studies quantified its effect on team performance.**"

> 국역: "**우려스러운 관찰 하나는, 설명이 AI에 대한 적정 신뢰가 아니라 맹목적 신뢰를 키웠다는 점이다.** 이는 도덕적·법적 이유로 인간이 루프 안에 있어야 하는 영역(예: 의료 진단)에서 특히 문제가 된다. **설명의 존재가 전문가(예: 의사)를 그저 안심시켜, 그들이 더 순응적으로 변해 컴퓨터에 맹목적으로 동의하게 만든다고 해보자. 이런 인간-AI 상호작용을 장려하는 것은 대단히 불만족스럽고 윤리적으로 위태로워 보인다.**"

**(h) 정성 분석의 신뢰도 — 재현성 근거**
> 인터애노테이터 일치도: "We scored the inter-annotator agreement with both the Cohen's κ [and]…high agreements, with an average **µ(κ) = 0.71, σ(κ) = 0.18** (the average agreement was **93% ± 6.5%**)." 최종 분석은 **409개 고유 응답**.
> "…**the same proportion of participants self-reported using AI's confidence scores regardless of whether they saw explanations** (Figure 9)."

#### ⚠️ 추출하지 못한 수치 (반드시 유의)
- **그림 4B(오답 시 조건별 성능 하락 폭)와 그림 5(상대 동의율, relative agreement rates)의 정확한 수치는 그래프로만 제시되어 텍스트 레이어에서 추출되지 않았다.** 본문에서 확보한 것은 **방향성 서술 + 표 1 + 본문 z/p값**까지다.
- 따라서 **"설명이 오답 시 성능을 몇 %p 떨어뜨렸다"거나 "동의율이 몇 % 올랐다"는 식의 수치 인용은 하지 말 것.** 이 논문에서 안전하게 쓸 수 있는 것은 **부호와 유의성**뿐이다.
- 그림 5에 대해 본문이 서술하는 방향성은 확보했다: "**Across the three datasets, Adaptive explanations successfully reduced the human's tendency to blindly trust the AI (i.e., decreased agreement) when it was uncertain and more likely to be incorrect.** For example, comparing Team (Explain-Top-1, AI) [with Explain-Top-2]…(pink rectangles) **were less likely to agree with the AI compared to those who saw Explain-Top-1** (blue rectangles)."

#### 한계·반박
1. **MTurk 크라우드워커 + 프록시 과업.** 저자 본인이 인정한다 — "**Since the nature of the proxy tasks can significantly change the human behavior, they can lead to potential misleading conclusions.**" 실제 전문가·실제 업무에 그대로 외삽할 수 없다.
2. **설명 방식이 highlight 기반(Top-1/Top-2/Adaptive)에 한정.** 2021년 기준 XAI이며, LLM의 자연어 추론 설명(chain-of-thought)에 그대로 적용되는지는 이 논문이 다루지 않는다.
3. **AI 정확도를 인위적으로 84%에 고정.** 실무의 AI는 과업별로 정확도가 크게 흔들린다.
4. **다만 이 결론은 이후 메타분석으로 재확인되었다** — 아래 3-2의 Vaccaro et al.에서 "AI Explanation Included" 조절변수가 **통계적으로 유의하지 않다.** 두 문헌을 나란히 인용하면 반박이 매우 어려워진다.

---

### 3-2. 【최우선·확인 완료】 Vaccaro, Almaatouq & Malone (2024) — 인간+AI는 평균적으로 최선의 단독보다 못하다

#### 서지
> Michelle Vaccaro, Abdullah Almaatouq, and Thomas Malone, "When combinations of humans and AI are useful: A systematic review and meta-analysis," ***Nature Human Behaviour***, vol. **8**, no. **12** (December 2024), pp. **2293–2303**. 온라인 선공개 **2024-10-28**.
> DOI: [10.1038/s41562-024-02024-1](https://doi.org/10.1038/s41562-024-02024-1) · **[PR]**
> 프리프린트: arXiv:**2405.06087** (v1 2024-05-09, v2 2024-10-29) · **[PP]**
> ⚠️ **프리프린트 제목은 "When *Are* Combinations of Humans and AI *Useful?*"로 어순이 다르다. 게재본 제목을 쓸 것.** 세 저자 모두 **공동 제1저자 표기(∗)**.

✅ **의뢰하신 기억("인간-AI 조합이 평균적으로 인간 단독/AI 단독 중 나은 쪽보다 못했다")은 정확하다.** 정밀 수치까지 확인 완료.

#### 메타분석 범위
- **74편 논문 → 106개 실험 → 370개 효과크기**
- **2020년 1월 1일 ~ 2023년 6월 30일 게재**, **피어리뷰 게재물만** 포함
- **사전등록(pre-registered)** 체계적 문헌고찰 + 3수준(three-level) 메타회귀

원문:
> "To evaluate this synergy in human-AI systems, we analyzed **370 unique effect sizes from 106 different experiments published between January 2020 and June 2023** that included the performance of the [human alone, AI alone, and human-AI system]."
> "…we identified **74 that met our inclusion criteria**. These papers reported the results of **106 unique experiments**, and many of the experiments had multiple conditions, so we collected a total of **370 unique effect sizes**."
> "studies published between **January 1, 2020 and June 30, 2023**" / "we sought to control for this issue by **only including studies published in peer-reviewed publications**"

#### 핵심 주장 — 두 기준선의 구분이 이 논문의 설계 핵심
- **human-AI synergy(시너지)** = 팀 vs **인간 단독과 AI 단독 중 더 나은 쪽** → **g = −0.23** (유의한 손실)
- **human augmentation(증강)** = 팀 vs **인간 단독** → **g = 0.64** (중대형 이득)

> 효과크기 정의(부록): "For strong synergy, Hedges' g represents the standardized mean difference between [the human-AI system and] the human alone or AI alone, **whichever one performs better, on average.** For human augmentation, Hedges' g [is relative to the human alone]."
> 해석 규약: "values of Hedges' g around **0.2** correspond to a **small** effect, values around **0.5** a **medium** effect, and [around 0.8 a large effect]."

#### 이 책에 쓸 수 있는 부분
- **AX 성과 귀속의 결정적 프레임.** "AI를 도입했더니 담당자가 더 잘하게 됐다"(증강)와 "인간+AI 체계가 AI 단독보다 낫다"(시너지)는 **완전히 다른 주장**이며, 데이터는 전자만 지지한다. **대부분의 기업 AX 보고서는 전자를 측정하고 후자를 주장한다.**
- **"누가 더 나은가"가 결과를 결정한다는 조절효과**가 실무 설계 규칙으로 바로 번역된다 — **인간이 AI보다 나은 과업에만 인간을 루프에 넣어라.**
- **의사결정 과업 vs 생성 과업의 부호 반전**은 AX 과제 포트폴리오 분류 기준이 된다.
- **설명 조절변수가 유의하지 않다**는 결과는 3-1의 Bansal을 메타 수준에서 재확인한다.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 초록 전문**
> "Inspired by the increasing use of AI to augment humans, researchers have studied human-AI systems involving different tasks, systems, and populations. Despite such a large body of work, we lack a broad conceptual understanding of when combinations of humans and AI are better than either alone. Here, we addressed this question by conducting a pre-registered systematic review and meta-analysis of over 100 recent experimental studies reporting over 300 effect sizes. **First, we found that, on average, human-AI combinations performed significantly worse than the best of humans or AI alone (Hedges' g = −0.23, 95% confidence interval −0.39 to −0.07). Second, we found performance losses in tasks that involved making decisions and significantly greater gains in tasks that involved creating content. Finally, when humans outperformed AI alone, we found performance gains in the combination, but when the AI outperformed humans alone we found losses.** These findings highlight the heterogeneity of the effects of human-AI collaboration and point to promising avenues for improving human-AI systems."

> 국역: "**첫째, 평균적으로 인간-AI 조합은 인간 단독 또는 AI 단독 중 나은 쪽보다 유의하게 못한 성과를 냈다(Hedges' g = −0.23, 95% 신뢰구간 −0.39 ~ −0.07). 둘째, 의사결정을 수반하는 과업에서는 성과 손실을, 콘텐츠 생성을 수반하는 과업에서는 유의하게 더 큰 이득을 발견했다. 셋째, 인간이 AI 단독을 능가했을 때는 조합에서 성과 이득이 있었지만, AI가 인간 단독을 능가했을 때는 손실이 있었다.**"

**(b) 두 기준선의 정반대 결과 — 이 책의 핵심 인용**
> "We found that the human-AI systems performed significantly worse overall than this baseline. The overall pooled effect was negative (**g = −0.23, t(92) = −2.89, two-tailed p = 0.005, 95% confidence interval (CI) −0.39 to −0.07**) and considered small according to conventional interpretations."

> "On the other hand, when we compared the performance of the human-AI systems to a different baseline – the humans alone – we found substantial evidence of human augmentation. The human-AI systems performed significantly better than humans alone, and this pooled effect size was positive (**g = 0.64, t(98) = 11.87, two-tailed p = 0.000, 95% CI 0.53 to 0.74**) and medium to large in size. … **In other words, the human-AI systems we analyzed were, on average, better than humans alone but not better than both humans alone and AI alone.**"

> 국역: "**다시 말해, 우리가 분석한 인간-AI 시스템은 평균적으로 인간 단독보다는 나았지만, 인간 단독과 AI 단독 둘 다보다 낫지는 않았다.**"

> ⭐ **정확한 대응 관계:** g = **0.64**는 **인간 단독 대비**(human augmentation), g = **−0.23**은 **인간 단독·AI 단독 중 나은 쪽 대비**(human-AI synergy)다. **두 수치는 같은 370개 효과크기에서 기준선만 바꿔 계산한 것이다.**

**(c) 과업 유형 조절효과 — 의사결정은 손실, 생성은 이득**
> "First, we found that the type of task significantly moderated human-AI synergy (**F(1, 104) = 7.84, two-tailed p = 0.006**). Among decision tasks—those in which participants decided between a finite set of options—the pooled effect size for human-AI synergy was significantly negative (**g = −0.27, t(104) = −3.20, two-tailed p = 0.002, 95% CI −0.44 to −0.10**), which indicates performance losses from combining humans and AI. In contrast, among creation tasks—those in which participants created some sort of open response content—the pooled effect size for human-AI synergy was positive (**g = 0.19, t(104) = 1.35, two-tailed p = 0.180, 95% CI −0.09 to 0.48**), pointing to synergy between humans and AI. **Even though the average performance gains for creation tasks were not significantly different from 0 (presumably because of the relatively small sample size of n = 34), the difference between losses for decision tasks and gains for creation tasks was statistically significant.**"

> ⚠️ **인용 주의:** 생성 과업의 +0.19는 **p = 0.180으로 0과 유의하게 다르지 않다.** "생성 과업에서는 시너지가 난다"고 단정하면 과잉 해석이다. 정확한 진술은 "**의사결정 과업의 손실과 생성 과업의 이득 사이의 차이가 유의하다**"이다.

**(d) 가장 중요한 조절효과 — 누가 더 나은가 (의뢰하신 baseline relative skill)**
> "Second, we found that the performance of the human and AI relative to each other impacted both human-AI synergy (**F(1, 104) = 81.79, two-tailed p = 0.000**) and human augmentation (**F(1, 104) = 24.35, two-tailed p = 0.000**). As shown in Figure 2, **when the human alone outperformed the AI alone, the combined human-AI system outperformed both alone with an average pooled effect size for human-AI synergy of g = 0.46 (t(104) = 5.06, two-tailed p = 0.000, 95% CI 0.28 to 0.66)**, a medium-sized effect. **But when the AI alone outperformed the human alone, performance losses occurred in the combined system relative to the AI alone, with a negative effect size for human-AI synergy of g = −0.54 (t(104) = −6.20, two-tailed p = 0.000, 95% CI −0.71 to −0.37)**, a medium-sized effect."

> 국역: "**인간 단독이 AI 단독보다 나았을 때, 결합된 인간-AI 시스템은 둘 다를 능가했다(g = 0.46, 95% CI 0.28~0.66). 그러나 AI 단독이 인간 단독보다 나았을 때는, AI 단독 대비 성능 손실이 발생했다(g = −0.54, 95% CI −0.71~−0.37).**"

> 증강 쪽 대응 결과: "When the AI outperformed the human alone, greater performance gains tended to occur in the human-AI systems relative to the human alone, and the pooled effect size for human augmentation was positive and medium to large in magnitude (**g = 0.74, t(104) = 13.50, two-tailed p = 0.000, 95% CI 0.63 to 0.85**)."

> ⭐ **이 대비가 핵심이다.** AI가 인간보다 나은 구간에서는 **증강 지표는 최대(+0.74)인데 시너지 지표는 최저(−0.54)**다. 즉 **"담당자가 훨씬 잘하게 됐다"와 "그 사람을 뺐으면 더 나았다"가 동시에 참일 수 있다.** AX 성과 귀속 논의에 그대로 쓸 수 있는 가장 강력한 한 쌍.

**(e) 표 S7 — 조절변수별 효과크기 전체 (책의 부록 표로 그대로 옮길 만함)**

| 조절변수 하위집단 | n | 시너지 g [95% CI] | p |
|---|---|---|---|
| **전체 효과크기** | **370** | **−0.23 [−0.39, −0.07]** | **0.005** |
| 누가 더 나은가: **AI** | 249 | **−0.54 [−0.71, −0.37]** | 0.000 |
| 누가 더 나은가: **인간** | 121 | **0.46 [0.28, 0.65]** | 0.000 |
| 과업: 생성(Create) | 34 | 0.19 [−0.09, 0.48] | 0.180 |
| 과업: 결정(Decide) | 336 | −0.27 [−0.44, −0.10] | 0.002 |
| 출력: 이진(Binary) | 132 | −0.53 [−0.76, −0.31] | 0.000 |
| 출력: 범주(Categoric) | 180 | 0.11 [−0.17, 0.39] | 0.441 |
| 출력: 수치(Numeric) | 24 | −0.81 [−1.20, −0.43] | 0.000 |
| 출력: 개방형(Open Response) | 34 | 0.19 [−0.09, 0.48] | 0.186 |
| 데이터: 이미지 | 164 | 0.07 [−0.22, 0.36] | 0.647 |
| 데이터: 복합(Multiple) | 78 | −0.55 [−0.85, −0.25] | 0.000 |
| 데이터: 수치 | 24 | −1.08 [−1.28, −0.89] | 0.000 |
| 데이터: 텍스트 | 96 | −0.17 [−0.47, 0.13] | 0.255 |
| 데이터: 비디오 | 8 | −0.03 [−0.39, 0.32] | 0.847 |
| AI 유형: Deep | 198 | −0.02 [−0.27, 0.24] | 0.897 |
| AI 유형: Shallow | 107 | −0.59 [−0.85, −0.33] | 0.000 |
| AI 유형: Wizard of Oz | 65 | −0.15 [−0.64, 0.35] | 0.559 |
| 연도 2020 | 68 | −0.56 [−0.90, −0.21] | 0.002 |
| 연도 2021 | 107 | −0.47 [−0.76, −0.18] | 0.002 |
| 연도 2022 | 130 | 0.01 [−0.39, 0.42] | 0.954 |
| 연도 2023 | 65 | 0.11 [−0.21, 0.44] | 0.488 |
| **AI 설명 포함: 아니오** | **228** | **−0.21 [−0.41, −0.01]** | **0.008** |
| **AI 설명 포함: 예** | **142** | **−0.25 [−0.43, −0.06]** | **0.212** |
| AI 신뢰도 포함: 아니오 | 269 | −0.29 [−0.50, −0.08] | 0.019 |
| AI 신뢰도 포함: 예 | 101 | −0.12 [−0.31, 0.07] | 0.098 |
| 전문가 참여자: 예 | 235 | −0.23 [−0.51, 0.04] | 0.006 |
| 전문가 참여자: 아니오 | 135 | −0.23 [−0.42, −0.04] | 0.257 |
| 크라우드워커: 예 | 164 | −0.29 [−0.50, −0.08] | 0.006 |
| 분업(Division of Labor): 예 | **4** | 0.22 [−0.42, 0.87] | 0.494 |
| 분업(Division of Labor): 아니오 | 366 | −0.24 [−0.40, −0.08] | 0.004 |

> ⭐ **두 줄이 특히 값나간다.** ① **설명 유무는 유의한 조절변수가 아니다** — Bansal(2021)의 메타 수준 재확인. ② **연도별로 손실이 사라지는 추세**(2020 −0.56 → 2023 +0.11).

**(f) 유의하지 않았던 조절변수 — 원문이 명시적으로 열거**
> "The remaining moderators we investigated were **not statistically significant** for human-AI synergy or human augmentation (**explanation, confidence, participant type, division of labor**)."
> 유의했던 것: "the type of AI involved in the experiment (**F(2, 103) = 3.77, two-tailed p = 0.026**) and the year of publication (**F(3, 102) = 3.65, two-tailed p = 0.015**) moderated human-AI synergy, and the experimental design moderated human augmentation (**F(1, 104) = 4.90, two-tailed p = 0.029**)."
> 데이터 유형: "the type of data involved in the task significantly moderated both human-AI synergy (**F(4, 101) = 15.24, two-tailed p = 0.000**) and human augmentation (**F(4, 101) = 6.52, two-tailed p = 0.000**)."

**(g) 이질성 — 반드시 함께 인용할 것**
> "We also found evidence for substantial heterogeneity of effect sizes in our estimations of human-AI synergy (**I² = 97.7%**) and human augmentation (**I² = 93.8%**)."

> ⚠️ **I² = 97.7%는 극단적으로 높다.** "평균 −0.23"이라는 단일 수치를 대표값처럼 쓰면 오독이다. 저자들 스스로 초록에서 "These findings highlight the **heterogeneity** of the effects"라고 결론짓는다. **책에서는 반드시 "평균은 −0.23이지만 편차가 거의 전부다"로 써야 한다.**

**(h) 강건성 검정 — 결론이 흔들리지 않음**
> 논문 수준 집계: "we found a comparable overall effect size for human-AI synergy (**g = −0.22, t(67) = −2.46, two-tailed p = 0.017, 95% CI −0.41 to −0.04**) and for human augmentation (**g = 0.65, t(69) = 9.96, two-tailed p = 0.000, 95% CI 0.52 to 0.78**)."
> 대안 가중: "(**g = −0.25, t(104) = −3.45, two-tailed p = 0.001, 95% CI [−0.39, −0.11]**) and human augmentation (**g = 0.60, t(104) = 12.60, two-tailed p = 0.000, 95% CI [0.50, 0.69]**)."
> Leave-one-out: "ranged from **−0.28 to −0.19** with two-tailed **p < 0.05 (0.000 to 0.019) in all cases**" / 증강은 "**0.61 to 0.66**"
> 이상치 제거: "(**g = −0.21, t(98) = −2.59, two-tailed p = 0.011, 95% CI [−0.36, −0.05]**) and human augmentation (**g = 0.64, t(98) = 11.73, two-tailed p = 0.000, 95% CI [0.53, 0.75]**)."

**(i) 출판편향 — 저자들의 자기 검증 (⭐ 낙관 수치가 더 취약하다)**
> 시너지: "two-tailed **p = 0.438, 95% CI −2.39 to 1.04**), nor did the rank correlation test (**τ = 0.05, two-tailed p = 0.121**). Taken as a whole, these tests suggest that **our results for human-AI synergy are robust** [to publication bias]."
> 증강: "two-tailed **p = 0.002, 95% CI 0.76 to 3.16**), as does the rank correlation test (**τ = 0.19, two-tailed p = 0.000**)." / "we did not try to correct for potential publication bias to preserve the integrity [of the analysis]"

> ⚠️ **인용 시 중요:** 부정적 결과(시너지 −0.23)는 출판편향 검정을 **통과했고**, 긍정적 결과(증강 +0.64)는 **통과하지 못했다.** 즉 **낙관적 수치 쪽이 더 취약하다.**

**(j) 3개 실험 하위표본 (참고)**
> "from these 3 experiments, we found that, on average, human-AI synergy (**g = 0.22, t(104) = 0.69, two-tailed p = 0.494, 95% CI −0.42 to 0.87**) occurred, but the result was not statistically significant"

#### 한계·반박
1. **2020-01~2023-06 게재 논문에 한정.** GPT-4(2023-03) 이후 세대의 실험이 거의 없다. **연도 조절효과가 개선 추세를 보이므로 최신 모델에서는 결론이 달라질 수 있다**는 것이 가장 강한 반박이다.
2. **I² 97.7%의 극단적 이질성** — 위 (g).
3. **실험실 과업 중심.** 생성 과업 표본이 **n = 34**로 매우 작다.
4. **"분업(division of labor)" 설계가 n = 4밖에 없다.** 즉 이 문헌 대부분은 "인간과 AI가 같은 과업을 중복 수행하고 인간이 최종 결정"이라는 **단일 구조**를 잰 것이다. **역할을 나누는 설계(AX 실무에서 실제로 중요한 것)는 사실상 미검증 영역이다 — 책에서 이 공백 자체를 지적하면 독창적이다.**

---

### 3-3. 【확인 완료·⚠️ 프리프린트】 Hemmer, Schemmer, Kühl, Vössing & Satzger (2024) — 상보성은 어디에서 오는가

#### 서지
> Patrick Hemmer, Max Schemmer, Niklas Kühl, Michael Vössing, and Gerhard Satzger, "Complementarity in Human-AI Collaboration: Concept, Sources, and Evidence," arXiv:**2404.00029** (v1 2024-03-28, v2). · **[PP]**
> URL: https://arxiv.org/abs/2404.00029 · 원문 표지에 "**P REPRINT**" 표기

> ⚠️ **[PP] 주의:** **정식 학술지·학회 게재 여부를 확인하지 못했다.** 인용 시 반드시 **프리프린트로 표기**하거나 게재 여부를 재확인할 것. 다만 실험 설계·통계 보고 수준은 게재 논문급이고, **동일 저자군의 인접 논문 3편은 피어리뷰 게재를 확인했다**(아래 3-3-보론).

#### 핵심 주장
상보적 팀 성과(CTP)가 좀처럼 관측되지 않는 이유는 **상보성의 원천을 개념적으로 분리하지 못했기 때문**이다. 상보성을 **잠재력(potential)**과 **실현된 효과(effect)**로 나누고, 잠재력을 두 원천으로 쪼갠다:
- **고유 상보성(inherent, CP_inh)** ← **정보 비대칭**: 인간이 AI가 접근할 수 없는 맥락 정보를 가짐
- **협업 상보성(collaborative, CP_coll)** ← **역량 비대칭**: 둘의 강점 영역이 다름

#### 이 책에 쓸 수 있는 부분
**B-3 전체에서 가장 실무적으로 유용한 논문이다.** Bansal과 Vaccaro가 "인간을 넣으면 대체로 손해"라는 나쁜 소식을 준다면, 이 논문은 **"그러면 언제 인간을 넣어야 하는가"에 대한 설계 답**을 준다:

> **AI가 접근할 수 없는 정보를 인간이 가지고 있을 때만 인간을 루프에 넣어라. 그 정보가 없으면 인간은 AI 출력의 잡음원일 뿐이다.**

AX 실무 번역: 현장 맥락·고객 이력·비공식 지식·규제 판단처럼 **시스템에 안 들어간 정보**를 담당자가 쥐고 있는 공정에만 휴먼 인 더 루프를 설계한다. **시스템이 모든 것을 아는 공정에서 승인 단계를 두는 것은 성과를 떨어뜨린다.**

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 초록**
> "Artificial intelligence (AI) has the potential to significantly enhance human performance across various domains. Ideally, collaboration between humans and AI should result in complementary team performance (CTP) -- a level of performance that neither of them can attain individually. **So far, however, CTP has rarely been observed, suggesting an insufficient understanding of the principle and the application of complementarity.** Therefore, we develop a general concept of complementarity and formalize its theoretical potential as well as the actual realized effect in decision-making situations. Moreover, **we identify information and capability asymmetry as the two key sources of complementarity.** Finally, we illustrate the impact of each source on complementarity potential and effect in two empirical studies."

**(b) 실험 1 — 정보 비대칭 (주택 가격 예측, MAE 기준)**

표본: "we continued with the data of **101 participants** across both conditions—**53 in the treatment without UHCI and 48 in that with UHCI**." (UHCI = unique human contextual information = 주택 사진; AI는 표 형태 데이터만 접근)
사전 검정력 분석 결과 필요 표본 86, 실제 모집 120(조건당 60).

> "Participants in the treatment without UHCI achieve an **MAE of $251,282**, while those in the treatment with UHCI yield an **MAE of $200,510—an improvement of $50,772 (20.21%)**, which is significant (**d = 0.92, p < 0.001**, two-sample, two-tailed T-test)."

> "The team performance in the treatment without UHCI results in an **MAE of $160,095** versus an **MAE of $148,009** in the treatment with UHCI—an improvement of **$12,086 (7.55%)**, which is significant (**d = 0.59, p < 0.05**). In both treatments, the human-AI team outperforms the AI (**MAE: $163,080**). Whereas the difference between the performance of the human-AI team and the performance of the AI alone is significant in the treatment with UHCI (**d = 0.68, p < 0.001**), **the difference in the treatment without UHCI does not constitute a significant improvement (d = 0.16, p = 1.0).**"

> 국역: "…양 처치 모두에서 인간-AI 팀이 AI(MAE $163,080)를 능가한다. **그러나 팀 성과와 AI 단독 성과의 차이가 유의한 것은 UHCI가 있는 처치뿐이고(d = 0.68, p < 0.001), UHCI가 없는 처치에서의 차이는 유의한 개선이 아니다(d = 0.16, p = 1.0).**"

> ⭐ **이 문장 하나가 챕터의 설계 원칙이 된다.** 인간이 AI가 못 보는 정보(사진)를 가졌을 때만 팀이 AI 단독을 유의하게 이겼다. 그 정보가 없으면 **d = 0.16, p = 1.0** — 아무것도 아니다.

> 상보성 잠재력: "In the condition without UHCI, the **CP_inh is $42,995**, and increases to **$61,970** in the condition with UHCI (**d = 1.05, p < 0.001**, two-tailed Mann-Whitney U test)."
> 협업 잠재력(반대 방향): "Whereas in the condition without UHCI, the **CP_coll results in $120,085**, in the condition with UHCI it amounts to **$101,110** (**d = 1.05, p < 0.001**). Since the participants in both conditions work with the same AI model…**the CP…is $163,080 in both conditions.**"
> 실현된 효과: "(without UHCI: **$14,468**; with UHCI: **$27,860**; **d = 0.87, p < 0.001**)"
> 실현률: "unique human contextual information not only enhances the theoretically available inherent complementarity potential, but that **the participants could also use significantly more of it (without UHCI: 34%; with UHCI: 45%; d = 0.82, p < 0.001**)."

> "**Overall, the most important finding is that humans can realize a disproportionally large amount of the inherent complementarity potential through unique contextual information, which finally results in CTP.**"
> 국역: "**가장 중요한 발견은, 인간이 고유한 맥락 정보를 통해 고유 상보성 잠재력을 불균형하게 큰 폭으로 실현할 수 있으며, 그것이 최종적으로 CTP로 귀결된다는 점이다.**"

**(c) 실험 2 — 역량 비대칭 (이미지 분류, 분류오류 기준)**

> "Humans conducting the task alone exhibit a classification error of approximately 0.30, which is nearly identical across the conditions (**Baseline AI: 0.2999; Complementary AI: 0.2951; d = 0.05, p = 1.0**)."

> "Whereas the human-AI team yields a **classification error of 0.2473** in the condition with the baseline AI, this error decreases even further to **0.1461** in the team with the complementary AI. This corresponds to **an improvement of 41%**, which is significant (**d = 1.29, p < 0.001**). Both classification errors are significantly lower than that of the AI conducting the task alone in both conditions (**Baseline AI: 0.2666, d = 0.33, p < 0.05; Complementary AI: 0.2666, d = 1.25, p < 0.001**)."

> ⭐ **핵심:** 두 AI는 **단독 성능이 완전히 동일(0.2666)**하다. 다른 것은 **어디서 틀리는가**뿐이다. 그런데 팀 성과는 0.2473 vs 0.1461 — **41% 차이.** **"AI를 더 정확하게 만들기"가 아니라 "AI가 인간과 다른 곳에서 틀리게 만들기"가 팀 성과를 결정한다.**

> 잠재력: "(**Baseline AI: 0.0640, Complementary AI: 0.2480; d = 3.81, p < 0.001**)" / CP_coll "(**Baseline AI: 0.2026, Complementary AI: 0.0186, d = 3.81, p < 0.001**)"
> "Whereas the inherent complementarity potential constitutes **24% of the overall complementarity potential in the baseline condition, this share rises to 93% in the complementary AI condition.**"
> 실현: "In the baseline condition, **58%** of the inherent complementarity potential could be realized…resulting in a **CE_inh of 0.0368.** In the condition with the complementary AI, it is possible to realize **89%**…resulting in a **CE_inh of 0.2196.** This shows a significant performance improvement (**d = 3.43, p < 0.001**)."
> "It indicates that **humans tended to rely on the AI decisions when they were correct, but on their decision when it was incorrect.**"

**(d) 협업 상보성은 두 실험 모두 음(−)이었다 — 균형 인용용**
> 실험 1: "We do not find a significant difference between the two treatments (**CE_coll: without UHCI: $−11,483; with UHCI: $−12,789; d = 0.08, p = 1.0**)."
> 실험 2: "in both conditions the collaborative complementarity effect (CE_coll) is negative. Whereas the value is only slightly negative in the baseline condition (**Baseline AI: −0.0175**), it decreases to **−0.0990** in the condition with the complementary AI (**d = 1.32, p < 0.001**)."

> "…**there might be a trade-off between turning a higher level of capability asymmetry into performance synergies and not relying on the AI's suggestions due to witnessing erroneous decisions in "easier" instances.**"
> 국역: "**역량 비대칭을 성과 시너지로 전환하는 것과, "더 쉬운" 사례에서 AI의 오답을 목격한 탓에 AI 제안을 신뢰하지 않게 되는 것 사이에 상충관계가 있을 수 있다.**" → **AX 실무의 "한 번 틀린 걸 본 뒤로 아무도 안 씀" 현상의 정확한 학술 서술.**

**(e) 경영 함의 — 저자들이 직접 쓴 문장**
> "Our work also has important implications for managerial decision-makers. In application areas with suitable decision-making tasks, **responsible managers should focus on deploying AI systems that enable the realization of CTP through** [the sources of complementarity]."
> "**Our research's most important implication is the need to design for CTP**, which is influenced by the source of [complementarity]."

#### 한계·반박
- **⚠️ 프리프린트다(게재 확인 필요).**
- 실험이 **주택가격 예측·이미지 분류**라는 인공적 과업. 조직 업무로의 외삽에 유보.
- **협업 상보성(CE_coll)은 두 실험 모두 음(−)이었다.** 즉 "역할을 나누면 좋아진다"는 부분은 이 논문도 입증하지 못했다. 입증된 것은 **정보·역량 비대칭이 잠재력을 키우고 인간이 그 잠재력의 상당 부분을 실현한다**는 것까지다.
- 상보성 지표(CP/CE) 정의가 이 논문 고유의 것이라 **다른 문헌과 직접 비교가 어렵다.**

#### 3-3-보론. 같은 연구그룹의 확인된 인접 문헌 (전부 서지 확인 완료)

**① 정보 비대칭이 상보성의 원천임을 처음 보인 논문** — arXiv:**2205.01467**, 2022-05 · **[PP]**
> Patrick Hemmer, Max Schemmer, Niklas Kühl, Michael Vössing, and Gerhard Satzger, "On the Effect of Information Asymmetry in Human-AI Teams."
> "…**we identify information asymmetry as an essential source of complementarity potential**, as in many real-world situations, humans have access to different contextual information. By conducting an online experiment, we demonstrate that **humans can use such contextual information to adjust the AI's decision, finally resulting in CTP.**"

**② XAI 메타분석 — Bansal의 결론을 2022년에 이미 메타 수준에서 확인** · **[PR]**
> Max Schemmer, Patrick Hemmer, Maximilian Nitsche, Niklas Kühl, and Michael Vössing, "A Meta-Analysis of the Utility of Explainable Artificial Intelligence in Human-AI Decision-Making," in ***Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society*** (AIES '22). DOI: [10.1145/3514094.3534128](https://doi.org/10.1145/3514094.3534128) · arXiv:2205.05126
> "We observe a **statistically positive impact of XAI on users' performance.** Additionally, the first results indicate that human-AI decision-making tends to yield **better task performance on text data.** However, **we find no effect of explanations on users' performance compared to sole AI predictions.**"
> ⭐ **마지막 문장이 핵심이다.** 설명은 **인간 단독 대비로는 도움이 되지만, AI 단독 대비로는 아무 효과가 없다.** **Vaccaro의 "증강 vs 시너지" 구분과 정확히 같은 구조** — 세 문헌이 같은 결론으로 수렴한다.

**③ AI가 인간에게 위임하는 설계 — 성과 귀속 논의에 직결** · **[PR]**
> Patrick Hemmer, Monika Westphal, Max Schemmer, Sebastian Vetter, Michael Vössing, and Gerhard Satzger, "Human-AI Collaboration: The Effect of AI Delegation on Human Task Performance and Task Satisfaction," in ***Proceedings of the 28th International Conference on Intelligent User Interfaces*** (IUI '23). DOI: [10.1145/3581641.3584052](https://doi.org/10.1145/3581641.3584052) · arXiv:2303.09224
> "In an experimental study with **196 participants**, we show that **task performance and task satisfaction improve through AI delegation, regardless of whether humans are aware of the delegation.** Additionally, we identify **humans' increased levels of self-efficacy as the underlying mechanism** for these improvements in performance and satisfaction. Our findings provide initial evidence that **allowing AI models to take over more management responsibilities can be an effective form of human-AI collaboration in workplaces.**"
> ⭐ **AX 조직 설계에 매우 쓸모 있다.** "사람이 AI에 위임"이 아니라 **"AI가 사람에게 위임"**하는 구조가 성과와 만족도를 **둘 다** 올렸고, 그 메커니즘은 **자기효능감**이었다. "AI에게 지시받으면 사기가 떨어진다"는 통념의 반증.

---

### 3-4. 【확인 완료】 Steyvers, Tejeda, Kerrigan & Smyth (2022) — 상보성이 성립하는 구간은 좁다

#### 서지
> Mark Steyvers, Heliodoro Tejeda, Gavin Kerrigan, and Padhraic Smyth, "Bayesian modeling of human–AI complementarity," ***Proceedings of the National Academy of Sciences***, vol. **119**, no. **11**, e2111547119. 온라인 **2022-03-11**, 지면 **2022-03-15**.
> DOI: [10.1073/pnas.2111547119](https://doi.org/10.1073/pnas.2111547119) · PMID 35275788 · PMCID **PMC8931210** · **[PR]**

#### 핵심 주장
인간과 기계의 예측을 **베이지안 결합 모형**으로 합칠 때 상보성(하이브리드 쌍 HM이 인간 쌍 HH·기계 쌍 MM' 둘 다를 이김)이 성립하는 조건을 **이론적으로 유도하고 실증적으로 검증**했다. 결론: 상보성은 **오류의 상관이 낮을 때, 그리고 두 주체의 성능 차이가 크지 않을 때만** 성립하며, **그 구간은 좁다.**

#### 이 책에 쓸 수 있는 부분
- Vaccaro의 메타분석 결과("인간이 나을 때만 시너지, AI가 나을 때는 손실")에 **수학적 설명**을 제공한다. 그 결과는 우연이 아니라 **결합 모형의 구조적 귀결**이다.
- **"오류의 상관"이 핵심 설계 변수**라는 명제. AX에서 검토자를 붙일 때 물어야 할 질문은 "이 사람이 유능한가"가 아니라 **"이 사람이 AI와 다른 곳에서 틀리는가"**다.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) Significance 문단 (초록 대용)**
> "With the increase in artificial intelligence in real-world applications, there is interest in building hybrid systems that take both human and machine predictions into account. Previous work has shown the benefits of separately combining the predictions of diverse machine classifiers or groups of people. Using a Bayesian modeling framework, we extend these results by **systematically investigating the factors that influence the performance of hybrid combinations of human and machine classifiers** while taking into account the unique ways human and algorithmic confidence is expressed."

**(b) 표본 — 의뢰하신 4,800장 / 320개 비교 확인**
> "we collected a large dataset of human and machine classification decisions for a set of **4,800 images.**"
> "To understand how complementarity varies as a function of the difference between human and machine classifier performance, Fig. 4 shows the out-of-sample results for **320 comparisons by crossing four levels of fine tuning, four levels of image noise, and 20 CNN pairs.**"
> 결합 모형 결과 조건: "The results are based on low levels of image noise (**Ω = 80**) and with CNNs that are fine-tuned for one epoch" / 추론은 MCMC, **4겹 교차검증(fourfold cross-validation)**.

**(c) 인간과 기계는 서로 다른 곳에서 틀린다 — 이 책의 인용 문장**
> "**Even at comparable levels of performance, human participants and machine classifiers make different types of errors.** Fig. 2 shows examples of HM algorithm complementarity. The images in Fig. 2A are challenging for humans but relatively easy for machine classifiers. For all of these images, human accuracy and confidence were low (**all six human participants made a low-confidence classification, and at most, one out of six human participants made a correct judgment**), but machine accuracy was high (**at least four out of five machine classifiers made a correct classification for any of these images**). The images in Fig. 2B are challenging for machine classifiers but relatively easy for humans. **All six human judges made a correct and high-confidence classification, whereas at most, one out of five machine classifiers made a correct classification for each of these images.**"

> 국역: "**성능 수준이 비슷할 때조차 인간 참여자와 기계 분류기는 서로 다른 종류의 오류를 낸다.** …[2A는] 인간 6명 전원이 저신뢰 분류를 했고 많아야 6명 중 1명만 정답을 냈지만, 기계는 5개 중 최소 4개가 정답을 냈다. …[2B는] **인간 판정자 6명 전원이 고신뢰 정답을 냈지만, 기계 분류기는 많아야 5개 중 1개만 정답을 냈다.**"

**(d) 오류 상관 — 의뢰하신 0.33/0.62/0.71 확인**
> 사후평균(추론값): "The hybrid HM pairs are correlated less (**posterior mean around 0.4**) than human-only (**posterior mean around 0.7**) or machine-only pairs (**posterior means between 0.65 and 0.75**)."
> 이론 예측에 쓰인 값(그림 4 캡션): "The colored area shows the area of complementarity as predicted by theory based on **ρ_HM = 0.33, ρ_HH = 0.62, and ρ_MM' = 0.71**, approximately matching the correlations inferred by the Bayesian combination model. The dashed line shows the predicted area of complementarity for a best-case situation where the latent human and model predictions are uncorrelated, **ρ_HM = 0**, and the nonhybrid correlations remain the same (**ρ_HH = 0.62, ρ_MM' = 0.71**)."
> 강건성: "Having only a single continuous confidence score…and discretizing the machine confidence scores into a small set of ordinal categories, analogous to the human confidence scores, **do not change the qualitative pattern of results.**"

**(e) 상보성의 좁은 띠 — 가장 중요한 인용**
> "The shaded area in Fig. 4 shows that **there is a relatively narrow band of performance difference that produces complementarity.** **The human and machine classifiers need to perform at similar levels in order to produce a hybrid HM pair that is more accurate than either two humans or two machine classifiers.** These results strongly depend on the correlations between human and machine classifier. For example, in a hypothetical scenario where the HM classifier correlation is zero, the zone of complementarity will grow (dashed line). **However, note that even in this best-case scenario, there are still limits on the accuracy differences that produce complementarity.**"

> 국역: "**상보성을 만들어내는 성능 차이의 띠는 비교적 좁다. 인간과 기계 분류기가 비슷한 수준으로 수행해야만, 인간 둘이나 기계 둘보다 더 정확한 하이브리드 쌍이 나온다.** …하이브리드 상관이 0인 가상 시나리오에서는 상보성 구간이 넓어진다. **그러나 그 최선의 경우조차 상보성을 만들어내는 정확도 차이에는 여전히 한계가 있다.**"

**(f) 상보성의 형식적 정의 (책의 각주용)**
> "Complementarity is observed if the hybrid combination HM outperforms the combinations consisting of human or machine classifiers alone: **A_H,M > A_H,H and A_H,M > A_M,M'**."
> "We have complementarity if for some H ∈ {H₁, H₂} and some M ∈ {M₁, M₂}, we have **A_H,M > max{A_H₁,H₂, A_M₁,M₂}**." / "Hence, **complementarity is equivalent to the condition r_H,M > max{r_H₁,H₂, r_M₁,M₂}**."
> "increasing the nonhybrid correlations (ρ_MM and ρ_HH) **will always cause the nonhybrid pair accuracies to decrease, thus making complementarity easier to achieve.**"

**(g) 선행 문헌 대비 기여**
> "Prior work has shown empirically that **hybrid HM algorithm systems do not always lead to superior performance.** Our results in this paper go beyond these earlier studies, both theoretically and empirically, and **show specifically what factors contribute to complementarity.**"

#### ⚠️ 추출하지 못한 수치
- **표 1(하이브리드 쌍의 out-of-sample 정확도)과 표 2(클래스별 오류 모형·인간 신뢰도·기계 신뢰도 3요인의 로그 오즈 효과 추정치, CI, p)**는 표에만 있고 Europe PMC 전문 XML에서 값이 분리 추출되지 않았다. 확보한 것은 **본문 서술 + 상관계수 + 표본 규모**까지다. **3요인의 구체적 효과 추정치는 인용하지 말 것.**

#### 한계·반박
- **이미지 분류 단일 도메인**, 인공 노이즈로 성능을 변조한 설계. 조직 의사결정으로의 외삽은 **유비 수준**이다.
- **"결합(combination)" 모형이지 "인간이 AI 조언을 보고 최종 결정"하는 실제 워크플로가 아니다.** 후자는 인지 편향(앵커링, 자동화 편향)이 개입하므로 **이 논문의 상한보다 나쁠 가능성이 높다.** — 실제로 Bansal·Vaccaro가 그 나쁜 쪽을 측정한 것이다. **세 문헌을 이 순서로 배치하면 "이론적 상한 → 실험적 현실 → 메타분석 평균"이라는 논증이 선다.**
- 인간 신뢰도가 **단일 이산 평정**뿐이어서 기계 대비 정보량이 적다(저자들도 명시).

---

### 3-5. 【확인 완료】 Steyvers & Kumar (2024) — 세 가지 난제 (프레임 인용원)

#### 서지
> Mark Steyvers and Aakriti Kumar, "Three Challenges for AI-Assisted Decision-Making," ***Perspectives on Psychological Science***, vol. **19**, no. **5**, pp. **722–734**. 온라인 선공개 **2023-07-13**, 지면 **2024-09**.
> DOI: [10.1177/17456916231181102](https://doi.org/10.1177/17456916231181102) · **[PR]**
> 프리프린트: PsyArXiv, DOI 10.31234/osf.io/gctv6, **2022-10-16** · **[PP]**

#### 핵심 주장 & 인용 (VERBATIM, 게재본 초록)
> "Artificial intelligence (AI) has the potential to improve human decision-making by providing decision recommendations and problem-relevant information to assist human decision-makers. However, the full realization of the potential of human–AI collaboration continues to face several challenges. **First, the conditions that support complementarity (i.e., situations in which the performance of a human with AI assistance exceeds the performance of an unassisted human or the AI in isolation) must be understood.** This task requires humans to be able to recognize situations in which the AI should be leveraged and to develop new AI systems that can learn to complement the human decision-maker. **Second, human mental models of the AI, which contain both expectations of the AI and reliance strategies, must be accurately assessed.** **Third, the effects of different design choices for human-AI interaction must be understood, including both the timing of AI assistance and the amount of model information that should be presented to the human decision-maker to avoid cognitive overload and ineffective reliance strategies.** In response to each of these three challenges, we present an interdisciplinary perspective based on recent empirical and theoretical findings and discuss new research directions."

> 국역: "**첫째, 상보성을 뒷받침하는 조건**(즉 AI 지원을 받은 인간의 성과가 비보조 인간이나 AI 단독의 성과를 능가하는 상황)**이 이해되어야 한다.** …**둘째, AI에 대한 인간의 멘탈 모델** — AI에 대한 기대와 의존 전략을 모두 담고 있는 — **이 정확히 평가되어야 한다. 셋째, 인간-AI 상호작용의 서로 다른 설계 선택의 효과가 이해되어야 하며, 여기에는 AI 지원의 타이밍과 인지 과부하·비효과적 의존 전략을 피하기 위해 의사결정자에게 제시해야 할 모델 정보의 양이 모두 포함된다.**"

#### 이 책에 쓸 수 있는 부분
AX 체계의 **인간 측 설계 요건 3종 세트**로 그대로 옮길 수 있다: ① 상보성 조건 식별 ② **운영자의 AI 멘탈 모델 관리**(교육·기대 설정) ③ **개입 시점과 정보량 설계**(인지 과부하 방지). 특히 ②는 "AX는 도구 도입이 아니라 운영자 역량 설계"라는 이 책 논지와 직결된다.

#### 한계
- **논평(perspective) 논문이며 새 실증을 제시하지 않는다. 수치 인용원으로 쓰지 말고 프레임 인용원으로만 쓸 것.**

#### 3-5-보론. 신뢰도 표시의 부호 반전 (확인 완료) · **[PR]**
> Heliodoro Tejeda Lemus, Aakriti Kumar, and Mark Steyvers, "How Displaying AI Confidence Affects Reliance and Hybrid Human-AI Performance," ***Frontiers in Artificial Intelligence and Applications*** (IOS Press), **2023-06-22**. DOI: [10.3233/faia230087](https://doi.org/10.3233/faia230087)
> "Our results demonstrate that **displaying AI confidence increases joint accuracy when people are assisted by a classifier that is better than humans on average. Conversely, when assisted by a classifier with performance worse than an average human, joint accuracy was better when no AI confidence was displayed.** However, for the adoption of AI advice we observed the opposite pattern: **people rely more on a higher accuracy classifier that does not display confidence compared to one that does.**"
> ⭐ **AX UI 설계 규칙:** 신뢰도 표시가 **항상** 좋은 것이 아니다. **AI가 사람보다 못한 구간에서는 신뢰도를 감추는 편이 팀 성과가 낫다.** (Bansal에서 신뢰도가 설명보다 유효했던 것과 함께 읽으면, "신뢰도 표시"조차 조건부임을 알 수 있다.)

#### 3-5-보론2. 의존 전략의 잠재 추정 (서지 확인 완료) · **[PR]**
> Heliodoro Tejeda, Aakriti Kumar, Padhraic Smyth, and Mark Steyvers, "AI-Assisted Decision-making: a Cognitive Modeling Approach to Infer Latent Reliance Strategies," ***Computational Brain & Behavior***, vol. **5**, no. **4**, pp. **491–508**, 온라인 2022-10-19, 지면 2022-12. DOI: [10.1007/s42113-022-00157-y](https://doi.org/10.1007/s42113-022-00157-y)
> "We develop a cognitive model that allows us to infer the **latent** reliance strategy of humans on AI assistance **without asking the human to make an independent decision.** … The model's predicted reliance strategies closely track the strategies employed by humans in the two experimental paradigms."
> → AX 운영에서 **"담당자가 실제로 AI에 얼마나 의존하는가"를 별도 실험 없이 로그에서 추정**하는 방법론적 근거로 쓸 수 있다.

---

### 3-6. 기술의 경제학에서 "도구 몫 vs 운영자 몫" 귀속

> 이 항목은 B-4·B-5에서 확보한 문헌을 **B-3 관점으로 재배열**한 것이다(서지 원본은 b4.md/b5.md에 있다). 성과 귀속 논의에 직접 쓰이는 부분만 추렸다.

#### (a) 이론적 원류 — 자동화된 단계가 남은 인간 단계의 가치를 올린다
> Autor (2015, *JEP* 29(3): 3–30, DOI [10.1257/jep.29.3.3](https://doi.org/10.1257/jep.29.3.3)) **[PR]**:
> "Typically, these inputs each play essential roles; that is, improvements in one do not obviate the need for the other. If so, **productivity improvements in one set of tasks almost necessarily increase the economic value of the remaining tasks.**"
> "Analogously, **when automation or computerization makes some steps in a work process more reliable, cheaper, or faster, this increases the value of the remaining human links in the production chain.**"

이것이 **성과 귀속의 근본 비대칭**이다. 도구가 좋아지면 그 몫은 도구에 귀속되는 것처럼 보이지만, **동시에 남은 인간 과업의 한계 가치가 올라간다.** AX 성과를 "AI가 낸 것"으로만 계상하면 **이 두 번째 항을 회계에서 빠뜨린다.**

단, 저자 본인의 봉인 문장을 반드시 함께:
> "**A construction worker who is expert with a shovel but cannot drive an excavator will generally experience falling wages as automation advances. Similarly, a bank teller who can tally currency but cannot provide "relationship banking" is unlikely to fare well at a modern bank.**"
→ **가치 상승은 보완 과업을 공급할 수 있는 사람에게만 귀속된다.**

#### (b) 실증 — 이득은 균등하게 귀속되지 않는다 (숙련도 역전)
> Brynjolfsson, Li & Raymond (2025, *QJE* 140(2): 889–942, DOI [10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044)) **[PR]**:
> "Access to AI assistance **increases worker productivity, as measured by issues resolved per hour, by 15% on average, with substantial heterogeneity across workers.** … **Less experienced and lower-skilled workers improve both the speed and quality of their output, while the most experienced and highest-skilled workers see small gains in speed and small declines in quality.**"
> WP판(NBER 31161, n = **5,179**): "**by 14% on average, including a 34% improvement for novice and low-skilled workers but with minimal impact on experienced and highly skilled workers.**"
> ⚠️ 게재본은 **15%, n = 5,172**. **판본을 반드시 명시할 것.**

> ⭐ **성과 귀속의 실무적 뒤집기.** 같은 도구가 같은 조직 안에서 사람에 따라 **+34%에서 −(품질)**까지 갈린다. "AX 성과 = 도입률 × 평균 효과"라는 계산이 왜 틀리는지의 근거.

#### (c) 실증 — 프론티어 안과 밖에서 부호가 뒤집힌다
> Dell'Acqua, McFowland III, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon & Lakhani (2026, *Organization Science* 37(2): 403–423, DOI [10.1287/orsc.2025.21838](https://doi.org/10.1287/orsc.2025.21838)) **[PR]**, n = **758**:
> "For each one of a set of **18 realistic knowledge tasks within the frontier** of AI capabilities…subjects using AI outperformed those not using AI, **completing 12.2% more tasks and completing them 25.1% more quickly** on average while also delivering solutions of significantly improved quality. **However, for a complex managerial task selected to be outside the frontier, subjects using AI were 19% less likely to produce correct solutions compared with those without AI.**"

#### (d) 실증 — 과업 이득의 대부분은 최종 산출물에 도달하지 못한다 (⭐ 귀속 논의의 결정타)
> Demirer, Musolff & Yang (2026, NBER WP **35275**, May 2026) **[WP]**, GitHub 개발자 10만+:
> "autocomplete, interactive coding agents, and autonomous coding agents each significantly increase coding activity ('commits'), with respective **cumulative effects of 40%, 140%, and 180%**. **These gains, however, attenuate sharply across the production hierarchy: the 180% cumulative effect falls to 50% for the number of projects, and to 30% for actual releases.** This pattern is consistent with the **weak-link hypothesis**: the strong productivity gains from AI are attenuated by human bottlenecks in the production chain, with an **estimated elasticity of substitution of 0.25 between AI and human effort, which indicates strong complementarities.** … **Large task-level AI productivity gains have therefore translated only partially into shipped and used software thus far.**"

> ⭐ **성과 귀속의 핵심 수치: 과업 수준 이득의 약 1/6만 최종 산출물로 통과한다.** 그리고 **대체탄력성 0.25**는 AI와 인간이 **강한 보완재**임을 뜻한다 — 남은 인간 병목을 풀지 않으면 AI를 아무리 넣어도 산출이 안 는다.

#### (e) 실증 — 혼자 바꿀 수 있는 것만 바뀌었다
> Dillon, Jaffe, Immorlica & Stanton (2025, NBER WP **33795**, DOI 10.3386/w33795) **[WP]**, n = **7,137**:
> "access to the AI tool during the first year of its release **primarily impacted behaviors that workers could change independently and not behaviors that require coordination to change**: workers who used the tool in more than half of the sample weeks spent **3.6 fewer hours, or 31% less time on email each week (intent to treat estimate is 1.3 hours)** and completed documents moderately faster, but **did not significantly change time spent in meetings.**"

> ⭐ **성과 귀속을 조직 설계 문제로 전환하는 문장.** 개인에게 귀속되는 이득은 실현되고, **조율이 필요한 이득은 실현되지 않는다.** AX 성과가 개인 생산성 지표에서만 잡히고 조직 P&L에서 안 잡히는 현상의 실험적 설명.

#### ⚠️ 이 항목의 공백 (재확인 요청 대상)
- 의뢰서가 언급한 **"경제학에서 도구와 운영자 사이의 이득 귀속"**을 정면으로 다룬 **전용 문헌**(기술 지대의 귀속, 자본-노동 간 잉여 배분에 관한 노동경제학 문헌)은 **WebSearch 예산 200회 소진으로 독립 탐색하지 못했다.** 위 (a)~(e)는 B-4·B-5 문헌의 재배열이며, **이 주제의 전용 탐색은 남아 있다.**

---

### B-3 종합 — 이 책에 쓸 설계 명제 5개

| # | 명제 | 근거 |
|---|---|---|
| 1 | 팀 성과를 **인간 단독**과 비교하지 말고 **AI 단독**과 비교하라. 대부분의 AX 보고서는 전자를 재고 후자를 주장한다. | Vaccaro et al. (g = 0.64 vs −0.23), Schemmer et al. |
| 2 | **AI가 인간보다 나은 과업에 인간 승인 단계를 두지 마라.** 평균 g = −0.54의 손실이 난다. | Vaccaro et al. |
| 3 | 인간을 넣으려면 **AI가 접근 못 하는 정보를 그 인간이 쥐고 있어야** 한다. 아니면 d = 0.16, p = 1.0. | Hemmer et al. 실험 1 |
| 4 | **설명(XAI)은 적정 신뢰를 만들지 않는다.** 오답 수용률을 높인다. 신뢰도 표시 이상의 효과가 없다. | Bansal et al., Vaccaro et al.(설명 조절 무의미), Schemmer et al. |
| 5 | **과업 수준 이득을 조직 성과로 곱하지 마라.** 관측된 감쇠율은 약 1/6이고, 병목은 조율이 필요한 인간 공정에 있다. | Demirer et al., Dillon et al. |

**세 주제를 꿰는 한 문장(B-3 판본):** 팀 성과를 **인간 단독**과 비교하면 +0.64, **AI 단독**과 비교하면 −0.23이다. **AX 체계 구축의 첫 번째 설계 결정은 기술 선택이 아니라 기준선 선택이다.**

---

### B-3 관련 ⚠️ 미확인 항목 (요청하신 전체 목록이 아니라, B-3에 한정된 것만)

1. **⚠️ 게재 여부 확인 필요** · Hemmer et al., arXiv 2404.00029 — **정식 게재 여부 미확인, [PP]로 표기할 것.** 인접 논문 3편(2205.01467 / 2205.05126 AIES'22 / 2303.09224 IUI'23)은 게재 확인 완료.
2. **⚠️ 그림 수치 추출 실패** · Bansal et al. **그림 4B·그림 5**의 정확한 수치(오답 시 성능 하락 폭, 상대 동의율). **방향성만 인용 가능, 수치 인용 금지.**
3. **⚠️ 표 수치 추출 실패** · Steyvers et al. PNAS **표 1·표 2**(3요인의 로그 오즈 효과 추정치·CI·p). **본문 서술 + 상관계수 + 표본 규모까지만 확보.**
4. **⚠️ 미탐색** · 3-6의 "도구 vs 운영자 이득 귀속" 전용 경제학 문헌 — WebSearch 예산 소진.

### 로컬 원문 파일 (재확인용)
`/private/tmp/claude-1219186993/-Users-1112022-source-github-book-writer/dc570957-917d-436c-849d-9b90c31835d4/scratchpad/`
`bansal.txt`(layout) · `bansal_raw.txt`(raw, 두 컬럼 정렬 해제본 — 논의부 인용은 이쪽이 정확) · `vaccaro.txt`(본문+부록 표 S1~S7) · `hemmer.txt` · `pnas.txt`(Europe PMC XML → 평문)
---

> **아래 B-4 · B-5는 원자료(raw) 수록분이다.** 서지·수치는 원문 대조로 확인했고 미확인 항목도 그대로 남아 있으나, 절 번호·서술 톤이 위 B-1~B-3과 통일되지 않았다. 인용 시 각 항목의 `한계·반박`과 문서 말미 `⚠️ 미확인 항목`을 함께 읽어라.

## B-4. 자동화·고용·재배치(redeployment) — 학술 문헌 검증 결과

검색 시점: **2026-09-05**
검증 방식: 원문 PDF 직접 추출(pdftotext), Crossref/OpenAlex/OpenLibrary API, 발행처 페이지 대조. 인용문은 모두 원문 텍스트 레이어에서 그대로 추출한 것이며, 기억에 의존해 재구성한 문장은 없습니다.

---

### 0. 먼저 정정해야 할 것 (의뢰 내용 중 서지 오류)

| 의뢰서 표기 | 실제 확인된 정본 |
|---|---|
| Autor, Levy & Murnane (2003) "…An Empirical **Investigation**" | "…An Empirical **Exploration**" — MIT 게재본 표제지·QJE·NBER WP 8337 모두 "Exploration" |
| Bessen, *Economic Policy* 2020 | 권호는 **34권 100호, 2019년 10월**(온라인 게재 2020-07-01). DOI가 `eiaa001`이라 2020년으로 오인되기 쉬움 |

책에 쓸 때 이 두 가지는 반드시 정정된 형태로 표기해야 합니다.

---

### 1. 【최우선】 Acemoglu & Restrepo (2020) — 로봇과 일자리

#### 서지
> Daron Acemoglu and Pascual Restrepo, "Robots and Jobs: Evidence from US Labor Markets," ***Journal of Political Economy***, vol. 128, no. 6, pp. 2188–2244 (2020).
> DOI: [10.1086/705716](https://doi.org/10.1086/705716) · **[PR]** 피어리뷰
> 원문 판권면 표기: **"Electronically published April 22, 2020"** / "[ Journal of Political Economy, 2020, vol. 128, no. 6]"
> 워킹페이퍼 판본: **NBER Working Paper No. 23285, March 2017** · https://www.nber.org/papers/w23285 · **[WP]**
> OA 전문(게재본 조판 PDF): https://par.nsf.gov/servlets/purl/10398689

#### 핵심 주장
로봇은 "자본 심화(capital deepening)" 일반과 다르다. 로봇은 **노동이 수행하던 과업(task) 자체를 대체**하므로, IT 자본이나 총자본 증가와는 질적으로 다른 노동시장 효과를 낳는다. 미국 통근권(commuting zone) 722개를 단위로 1990~2007년 로봇 노출도를 (미국이 아닌) 유럽·한국 등 로봇 선진국의 산업별 도입 추세로 도구변수화해 추정했다.

#### 이 책에 쓸 수 있는 부분
- "AX로 인력이 남는다"를 다룰 때, **지역 효과(local effect)와 총량 효과(aggregate effect)가 2배 차이 난다**는 점이 결정적이다. 한 조직·한 지역에서 체감되는 충격은 경제 전체 충격의 약 두 배로 과장되어 보인다. 조직 안에서 "우리 팀 20명이 8명으로 줄었다"는 체감과, 회사·산업 전체 순효과는 다르다는 논리를 여기서 끌어올 수 있다.
- **비교역 부문(nontradables) 파급이 전체 감소의 약 2/3**라는 결과는, "자동화된 부서만 아프고 끝나지 않는다"는 조직 내부 논리로 확장 가능하다.
- 저자들 스스로 **총량 추정치는 지역 추정치보다 훨씬 조심해서 읽어야 한다**고 명시한다 — 책에서 수치를 인용할 때 이 유보를 함께 옮기면 신뢰도가 크게 올라간다.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 게재본 초록 — 헤드라인 추정치**
> "We study the effects of industrial robots on US labor markets. We show theoretically that robots may reduce employment and wages and that their local impacts can be estimated using variation in exposure to robots—defined from industry-level advances in robotics and local industry employment. We estimate robust negative effects of robots on employment and wages across commuting zones. We also show that areas most exposed to robots after 1990 do not exhibit any differential trends before then, and robots' impact is distinct from other capital and technologies. **One more robot per thousand workers reduces the employment-to-population ratio by 0.2 percentage points and wages by 0.42%.**"

> 국역: "노동자 1,000명당 로봇 1대가 추가되면 고용인구비율은 0.2%포인트, 임금은 0.42% 하락한다."

**(b) NBER 워킹페이퍼(2017) 초록 — 수치가 다름. 반드시 구분할 것**
> "According to our estimates, **one more robot per thousand workers reduces the employment to population ratio by about 0.18-0.34 percentage points and wages by 0.25-0.5 percent.**"

> ※ 게재본(0.2pp / 0.42%)과 WP판(0.18–0.34pp / 0.25–0.5%)의 수치가 **다르다**. 한국어 자료 상당수가 WP판 수치를 JPE 2020 인용으로 붙여 쓰고 있으므로, 책에서는 게재본 수치를 쓰고 각주로 WP판을 병기하는 것이 안전하다.

**(c) 지역(commuting zone) 효과 — 표준오차 포함**
> "Our base estimates in columns 3 and 6 in panel A, which we use in our quantitative evaluation in the next subsection, are −0.39 (standard errors = 0.09) for employment and −0.77 (standard errors = 0.15) for log hourly wages."

> 국역: 고용 계수 **−0.39 (표준오차 0.09)**, 로그 시간당임금 계수 **−0.77 (표준오차 0.15)**.
> ※ 부호·등호 기호는 PDF 텍스트 레이어에서 `20.39`, `5 0:09` 형태로 깨져 나오므로 위와 같이 복원했습니다. 조판 원문 확인 시 재검 권장(⚠️ 기호 복원).

**(d) 지역 효과의 크기 — 로봇 1대 = 6명**
> "Our estimates imply that between 1990 and 2007 the increase in the stock of robots (approximately one additional robot per thousand workers from 1993 to 2007) reduced the average employment-to-population ratio in a commuting zone by 0.39 percentage points and average wages by 0.77% (relative to a commuting zone with no exposure to robots). These estimates are sizable but not implausible. For example, they imply that **one more robot in a commuting zone reduces employment by about six workers**; this estimate includes both direct and indirect effects, the latter caused by the decline in the demand for nontradables as a result of reduced employment and wages in the local economy."

**(e) 각주 26 — 총 로봇 대수와 총 일자리 (매우 인용가치 높음)**
> "The increase of one more robot per thousand workers between 1993 and 2007 is equivalent to an increase of 0.6 robots per thousand people or **a total increase of 120,000 robots**. Our estimates imply that these additional robots led to a 0.39 percentage points lower (private) employment-to-population ratio, which is equivalent to one robot reducing employment by six (≈0.0039/(0.6/1,000)) workers. Equivalently, **the increase of 120,000 in the stock of robots during this period is predicted to have reduced employment by 756,000 jobs.** We obtain a reduction in employment of **720,000 jobs (or about four jobs per robot)** if we use the estimate for 1990–2014 from panel C together with the larger increase of 180,000 in the stock of robots over this longer time period."

**(f) 총량 효과 — 로봇 1대 = 3.3명, 40만 개**
> "With our preferred specification, our estimates imply that one more robot per thousand workers reduces the aggregate employment-to-population ratio by about 0.2 percentage points and wages by about 0.42% (compared with its larger local effects, 0.39 percentage points and 0.77%, respectively), or equivalently, **one new robot reduces employment by about 3.3 workers.**"

> "Using these parameter estimates, we compute the aggregate effects of improvements in robotics technology. One more robot per thousand workers is predicted to reduce aggregate wages by 0.42% and the aggregate employment-to-population ratio by 0.2 percentage points (**or 400,000 jobs**); equivalently, one more robot reduces employment by 3.3 workers."

**(g) 비교역 부문 파급 2/3 — "자동화된 부서만 아픈 게 아니다"**
> "With these parameter values, **about two-thirds of the decline in the demand for labor in an exposed commuting zone is driven by the contraction of the nontradable sector.** … (where manufacturing accounts for 0.16 of the 0.45 decline in the employment-to-population ratio in response to one more robot per thousand workers, with the rest of the decline accounted for by nontradables)."

**(h) 저자 자신의 유보 — 반드시 함께 인용할 것**
> "To explore these aggregate implications, we need to make further assumptions on cross-commuting zone spillovers (**and this suggests greater caution in interpreting these aggregate estimates than the local effects discussed in the previous paragraph**)."

**(i) 결론부 — "아직 로봇은 적다"**
> "**There are relatively few robots in the US economy, so the number of jobs lost due to robots has been limited thus far (a 0.2 percentage point decline in the aggregate employment-to-population ratio, or about 400,000 jobs).** However, if robotics technology proceeds as expected by experts over the next two decades (e.g., Brynjolfsson and McAfee 2014, 27–32; Ford 2015), the future aggregate implications of robots could be larger."

**(j) 중국 수입 충격과의 비교 (각주 27) — 스케일 감각용**
> "the implied magnitude from the rise in Chinese imports is a decline of about 1 percentage point in the employment-to-population ratio—**2.5 times the 0.39 percentage points decline due to the rising use of industrial robots.**"

**(k) BCG 시나리오 — 미래 외삽**
> "In their aggressive scenario, the world stock of robots will quadruple by 2025. This corresponds to 5.25 more robots per thousand workers in the United States and with our estimates would lead to **a 1 percentage point lower employment-to-population ratio and 2 percentage points lower wage growth between 2015 and 2025.**"

**(l) 각주 30 — 1990–2014 대안 추정**
> "…one additional robot per thousand workers reduces employment by 0.15 percentage points and hourly wages by 0.67%. Then the increase of 180,000 robots during this period is estimated to **reduce aggregate employment by 420,000 jobs and hourly wages by 1%.**"

**(m) 로봇의 정의 (IFR)**
> "an automatically controlled, reprogrammable, and multipurpose [machine]" (IFR 2014). "That is, industrial robots are fully autonomous machines…"

#### 한계·반박
1. **AI ≠ 산업용 로봇.** 이 논문의 대상은 IFR 정의의 "완전 자율·재프로그래밍 가능한 다목적 기계"다. 사무직 AI에 그대로 외삽할 근거는 논문 자체에 없다. 같은 저자들의 Acemoglu·Autor·Hazell·Restrepo(2022)는 오히려 AI의 총량 효과가 **아직 탐지 불가(too small to be detectable)**라고 결론짓는다(아래 §5-5 참조).
2. **미국 단일국 결과다.** 같은 방법론을 독일에 적용한 Dauth et al.(2021)은 대체 효과가 **약 50% 작고**, 서비스업의 신규 일자리로 **완전히 상쇄**된다고 보고한다(§5-2). 국가별 노동시장 제도가 결과를 뒤집는다.
3. **총량 추정의 모델 의존성.** 통근권 간 무역·자본소득 스필오버에 관한 구조 가정(명제 3)에 크게 의존한다. 저자들 본인이 (h)에서 유보를 명시.
4. **표준오차 논쟁.** Borusyak, Hull & Jaravel(2018) 방식의 shift-share 보정 표준오차 문제를 저자들이 표 A20/A31/A32에서 다루었다고 밝혔으나("We do not find systematic differences…"), shift-share 설계의 추론 타당성은 이 문헌의 상시 쟁점이다.
5. 메타분석 반론이 존재한다: Guarascio et al., "Robots vs. Workers: Evidence From a Meta-Analysis," *Journal of Economic Surveys*(2025), DOI [10.1111/joes.12699] — 검색 결과로 존재는 확인했으나 **본문·수치는 미확인**(⚠️ 아래 목록 참조).

---

### 2. Autor 계열 일자리 양극화 3부작

#### 2-1. Autor, Levy & Murnane (2003)

**서지**
> David H. Autor, Frank Levy, and Richard J. Murnane, "The Skill Content of Recent Technological Change: **An Empirical Exploration**," ***The Quarterly Journal of Economics***, vol. 118, no. 4, November 2003, pp. 1279–1333.
> DOI: [10.1162/003355303322552801](https://doi.org/10.1162/003355303322552801) · **[PR]**
> WP 판본: NBER Working Paper No. **8337, June 2001** · **[WP]**
> OA 전문: https://economics.mit.edu/sites/default/files/publications/the%20skill%20content%202003.pdf

**핵심 주장**
"컴퓨터가 고학력자를 대체하지 않고 보완한다"는 기존의 숙련편향기술변화(SBTC) 상관관계에 **인과 메커니즘**을 부여한 논문. 컴퓨터는 *학력*이 아니라 *과업(task)*에 작용한다 — 명시적 규칙으로 기술 가능한 과업(routine)은 대체하고, 문제해결·복잡한 소통(nonroutine)은 보완한다.

**이 책에 쓸 수 있는 부분**
AX 논의에서 "직무 단위가 아니라 과업 단위로 쪼개라"는 실무 조언의 학술적 원류가 정확히 이 논문이다. 특히 **"명목상 같은 직무 안에서 과업 구성이 바뀐다"**는 결과가, "직무는 그대로 두고 내용을 갈아끼우는 재배치"라는 이 책의 논지와 정확히 맞물린다.

**인용 가능한 문장·수치 (VERBATIM)**

초록 전문:
> "We apply an understanding of what computers do to study how computerization alters job skill demands. We argue that computer capital (1) substitutes for workers in performing cognitive and manual tasks that can be accomplished by following explicit rules; and (2) complements workers in performing nonroutine problem-solving and complex communications tasks. Provided that these tasks are imperfect substitutes, our model implies measurable changes in the composition of job tasks, which we explore using representative data on task input for 1960 to 1998. We find that within industries, occupations, and education groups, computerization is associated with reduced labor input of routine manual and routine cognitive tasks and increased labor input of nonroutine cognitive tasks. Translating task shifts into education demand, **the model can explain 60 percent of the estimated relative demand shift favoring college labor during 1970 to 1998. Task changes within nominally identical occupations account for almost half of this impact.**"

routine/nonroutine 정의 (본문):
> "(1) that computer capital substitutes for workers in carrying out a limited and well-defined set of cognitive and manual activities, those that can be accomplished by following explicit rules (**what we term "routine tasks"**); and (2) that computer capital complements workers in carrying out problem-solving and complex communication activities (**"nonroutine" tasks**)."

Table II 패널 A — 1960년 분포의 백분위 기준 경제 전체 과업투입 평균 (All):
| 과업 유형 | 1960 | 1980(CPS) | 1990 | 1998 |
|---|---|---|---|---|
| Nonroutine analytic | 50.0 | 53.2 | 56.2 | **58.7** |
| Nonroutine interactive | 50.0 | 53.3 | 58.6 | **62.2** |
| Routine cognitive | 50.0 | 51.8 | 48.3 | **44.4** |
| Routine manual | 50.0 | 53.8 | 52.3 | **49.2** |
| Nonroutine manual | 50.0 | 44.4 | 41.8 | **41.3** |

Table II 패널 B — 10년 환산 변화량 (Total / Between-industry / Within-industry, 합산 성별):
| 기간 | Routine cognitive | Routine manual | Nonroutine analytic | Nonroutine interactive |
|---|---|---|---|---|
| 1980–1990 | **−3.48** (−1.42 / −2.07) | −1.47 (−0.16 / −1.31) | 2.97 (0.92 / 2.05) | 5.31 (0.52 / 4.79) |
| 1990–1998 | **−4.88** (−1.31 / **−3.57**) | **−3.88** (−0.38 / **−3.50**) | 3.12 (0.67 / 2.45) | 4.48 (0.54 / 3.94) |

> 읽는 법: 1990년대 루틴 인지 과업 감소분 −4.88 중 **−3.57(73%)이 산업 내부(within)** 변화다. 즉 "산업이 통째로 사라져서"가 아니라 **같은 산업·같은 직무 안에서 일의 내용이 바뀌어서** 일어난 변화다. 이 책의 재배치 논지에 그대로 쓸 수 있다.

결과 요약(본문):
> "the task model explains a sizable share—**25 to 65 percent**—of the estimated growth in college-equivalent/noncollege-equivalent demand in each decade."

> "we find that these extensive margin task changes explain **20 to 25 percent** of the estimated demand shift for college versus noncollege labor during 1970 to 1998. If we focus on only the two most recent decades and include both intensive and extensive margin changes, the task model can explain a large fraction—**60 to 90 percent**—of the estimated increase in relative demand for college employment. Notably, **almost 40 percent of the computer contribution to rising educational demand in the last two decades is due to shifts in task composition within nominally unchanging occupations.**"

데이터 범위:
> "representative data on task input for 1960 to 1998" — 자료원은 Dictionary of Occupational Titles(1977, 1991) × Census IPUMS 1960/1970/1980 + CPS MORG 1980/1990/1998, 1,120개 산업–성별–학력 셀.

**한계·반박**
- 과업 측정이 DOT(직업사전) 기반이라 **측정오차가 크다**. 1977·1991 두 시점 DOT만 존재해 intensive margin 변화를 거칠게 잡는다. 저자들도 "extensive/intensive margin" 구분으로 이를 다룬다.
- 컴퓨터 이용도(산업별 컴퓨터 사용 근로자 비율, 1984–1997)를 처치변수로 쓰므로 **엄밀한 인과 식별이 아니다**. 저자들의 서술도 "associated with"에 머문다.
- 이후 문헌은 "routine/nonroutine" 이분법이 생성형 AI에는 잘 안 맞는다고 본다 — AI는 비루틴 인지 과업을 직접 친다.

---

#### 2-2. Autor & Dorn (2013)

**서지**
> David H. Autor and David Dorn, "The Growth of Low-Skill Service Jobs and the Polarization of the US Labor Market," ***American Economic Review***, vol. 103, no. 5, pp. 1553–1597 (August 2013).
> DOI: [10.1257/aer.103.5.1553](https://doi.org/10.1257/aer.103.5.1553) · **[PR]**
> OA 전문: https://www.ddorn.net/papers/Autor-Dorn-LowSkillServices-Polarization.pdf
> WP 판본: IZA Discussion Paper No. 7068 · **[WP]**

**핵심 주장**
숙련 상·하위는 늘고 중위가 줄어드는 **U자형 양극화**는, "루틴 과업 자동화 비용 하락"과 "다양성을 선호하는 소비자 선호"의 상호작용에서 나온다. 루틴 직무에 특화돼 있던 지역일수록 IT를 더 많이 도입했고, 저숙련 노동이 서비스 직종으로 재배치되었다.

**이 책에 쓸 수 있는 부분**
"남는 인력을 어디로 보낼 것인가"의 역사적 답이 **중간이 아니라 양끝**이었다는 사실. 자동화가 만든 여유 인력은 자연 상태로 두면 상향(고숙련 분석직)이 아니라 **하향(대면 서비스직)**으로 흘렀다는 점이 이 책 논지의 반대 극(counter-case)이 된다. 즉 "재배치는 저절로 좋게 끝나지 않는다"는 경고에 쓸 수 있다.

**인용 가능한 문장·수치 (VERBATIM)**

초록 전문:
> "We offer a unified analysis of the growth of low-skill service occupations between 1980 and 2005 and the concurrent polarization of US employment and wages. We hypothesize that polarization stems from the interaction between consumer preferences, which favor variety over specialization, and the falling cost of automating routine, codifiable job tasks. Applying a spatial equilibrium model, we corroborate four implications of this hypothesis. Local labor markets that specialized in routine tasks differentially adopted information technology, reallocated low-skill labor into service occupations (employment polarization), experienced earnings growth at the tails of the distribution (wage polarization), and received inflows of skilled labor. (JEL J24, J31, R23)"

U자형:
> "In net, **employment changes in the United States during this period were strongly U-shaped in skill level, with relative employment declines in the middle of the distribution and relative gains at the tails.**"

> "As with employment growth, **wage growth is strikingly U-shaped in skill percentiles, with the greatest gains in the upper tail, modest gains in the lower tail, and substantially smaller gains toward the median.**"

서비스 직종 정의 — 책에 그대로 옮기기 좋음:
> "Service occupations are jobs that involve assisting or caring for others, for example, **food service workers, security guards, janitors and gardeners, cleaners, home health aides, child care workers, hairdressers and beauticians, and recreation occupations.**"

핵심 수치:
> "Though among the least educated and lowest paid categories of employment, **the share of US labor hours in service occupations grew by 30 percent between 1980 and 2005** after having been flat or declining in the three prior decades (Table 1)."

> "The increase was even steeper among noncollege workers, by which we mean those with no more than a high school education, among whom **service occupation employment rose from 12.9 to 19.8 percent of total work hours between 1980 and 2005, a 53 percent increase** (Appendix Table 1)."

> "Accompanying their rising employment, **real wage growth in service occupations substantially outpaced that in other low-skill occupations, averaging 6.4 percent per decade between 1980 and 2005.**"

표본 범위:
> "…calculate the change between 1980 and 2005 in the share of employment accounted for by **318 detailed occupations encompassing all of US nonfarm employment**. Occupations are ranked by skill level, which is approximated by the mean log wage of workers in each occupation in 1980."

국제 일반성:
> "Notably, this pattern of employment polarization is not unique to the United States. Although not recognized until recently, a similar "polarization" of employment by skill level has been underway in **numerous industrialized economies in the last 20 to 30 years.**" (각주에서 Goos, Manning & Salomons: **16개 유럽 국가 중 15개국**에서 확인)

**한계·반박**
- 분석 창이 **1980–2005**로 끝난다. 2000년대 후반 이후 미국의 양극화는 약화·정체되었다는 후속 문헌이 있다(Autor 본인 후속 연구 포함).
- 인과 식별은 공간균형모형 + 1980년 루틴직 비중을 이용한 노출도 설계로, Bartik 계열의 통상적 반론(사전 추세, 지역 특성 상관)을 받는다.
- "서비스 직종으로의 재배치"는 **하향 이동**이다. 자동화의 좋은 결말로 읽으면 안 된다.

---

#### 2-3. Autor (2015)

**서지**
> David H. Autor, "Why Are There Still So Many Jobs? The History and Future of Workplace Automation," ***Journal of Economic Perspectives***, vol. 29, no. 3, Summer 2015, pp. 3–30.
> DOI: [10.1257/jep.29.3.3](https://doi.org/10.1257/jep.29.3.3) · **[PR]**
> OA 전문: https://economics.mit.edu/sites/default/files/inline-files/Why%20Are%20there%20Still%20So%20Many%20Jobs_0.pdf

**핵심 주장**
자동화는 대체(substitution)만 하는 게 아니라 **보완(complementarity)**한다. O-ring 생산함수 논리에 따라, 어떤 공정 단계가 값싸고 확실해지면 **남은 인간 단계의 경제적 가치가 오히려 올라간다.** 그리고 자동화의 한계는 폴라니의 역설 — 우리가 암묵적으로만 아는 일은 규칙으로 적을 수 없다.

**이 책에 쓸 수 있는 부분**
이 책의 핵심 프레임인 "AX로 확보한 FTE를 어디에 쓸 것인가"의 **경제학적 근거**가 여기 있다. 자동화된 단계 옆에 남은 인간 단계의 가치가 상승한다면, 남는 인력을 자르는 것은 그 가치 상승분을 스스로 버리는 것이다. 아래 인용 (a)·(b)를 나란히 배치하면 챕터 논지가 한 문단으로 선다.

**인용 가능한 문장·수치 (VERBATIM)**

**(a) O-ring 논리 — 이 책의 논지 문장**
> "Typically, these inputs each play essential roles; that is, improvements in one do not obviate the need for the other. If so, **productivity improvements in one set of tasks almost necessarily increase the economic value of the remaining tasks.**"

> "Analogously, **when automation or computerization makes some steps in a work process more reliable, cheaper, or faster, this increases the value of the remaining human links in the production chain.**"

**(b) ATM–은행 창구직원 사례 전문 — 이 책에서 가장 많이 쓸 대목**
> "As a contemporary example, consider the surprising complementarities between information technology and employment in banking, specifically the experience with automated teller machines (ATMs) and bank tellers documented by Bessen (2015). **ATMs were introduced in the 1970s, and their numbers in the US economy quadrupled from approximately 100,000 to 400,000 between 1995 and 2010.** One might naturally assume that these machines had all but eliminated bank tellers in that interval. But **US bank teller employment actually rose modestly from 500,000 to approximately 550,000 over the 30-year period from 1980 to 2010** (although given the growth in the labor force in this time interval, these numbers do imply that bank tellers declined as a share of overall US employment). With the growth of ATMs, what are all of these tellers doing? Bessen observes that two forces worked in opposite directions. First, by reducing the cost of operating a bank branch, ATMs indirectly increased the demand for tellers: **the number of tellers per branch fell by more than a third between 1988 and 2004, but the number of urban bank branches (also encouraged by a wave of bank deregulation allowing more branches) rose by more than 40 percent.** Second, as the routine cash-handling tasks of bank tellers receded, information technology also enabled a broader range of bank personnel to become involved in "relationship banking." Increasingly, **banks recognized the value of tellers enabled by information technology, not primarily as checkout clerks, but as salespersons, forging relationships with customers and introducing them to additional bank services like credit cards, loans, and investment products.**"

**(c) 즉시 따라붙는 경고 — 이 문장을 빼고 인용하면 오독이다**
> "**This example should not be taken as paradigmatic; technological change is not necessarily employment-increasing or Pareto-improving.** Three main factors can mitigate or augment its impacts. First, workers are more likely to benefit directly from automation if they supply tasks that are complemented by automation, but not if they primarily (or exclusively) supply tasks that are substituted. **A construction worker who is expert with a shovel but cannot drive an excavator will generally experience falling wages as automation advances. Similarly, a bank teller who can tally currency but cannot provide "relationship banking" is unlikely to fare well at a modern bank.**"

> ※ **이 책의 재배치 논지에 가장 정직한 문장**입니다. "재배치하면 된다"가 아니라 "보완 과업을 공급할 수 있는 사람만 이득을 본다" — 즉 재배치는 재교육을 전제로만 성립한다.

**(d) 폴라니의 역설**
> "But the scope for this kind of substitution is bounded because there are many tasks that people understand tacitly and accomplish effortlessly but for which neither computer programmers nor anyone else can enunciate the explicit "rules" or procedures. **I have referred to this constraint as Polanyi's paradox, named after the economist, philosopher, and chemist who observed in 1966, "We know more than we can tell"** (Polanyi 1966; Autor 2015). When we break an egg over the edge of a mixing bowl, identify a distinct species of birds based on a fleeting glimpse, write a persuasive paragraph, or develop a hypothesis to explain a poorly understood phenomenon, we are engaging in tasks that we only tacitly understand how to perform. **Following Polanyi's observation, the tasks that have proved most vexing to automate are those demanding flexibility, judgment, and common sense—skills that we understand only tacitly.**"

각주 4 — 모라벡의 역설 원문 인용:
> "Computer scientists often refer to this phenomenon as Moravec's paradox, after Moravec (1988) who wrote, **"[I]t is comparatively easy to make computers exhibit adult level performance on intelligence tests or playing checkers, and difficult or impossible to give them the skills of a one-year-old when it comes to perception and mobility.""**

**(e) 1961년 TIME 기사 — 챕터 오프닝용 역사적 반복**
> "The number of jobs lost to more efficient machines is only part of the problem. What worries many job experts more is that automation may prevent the economy from creating enough new jobs. . . . Throughout industry, the trend has been to bigger production with a smaller work force. . . . Many of the losses in factory jobs have been countered by an increase in the service industries or in office jobs. But automation is beginning to move in and eliminate office jobs too. . . . In the past, new industries hired far more people than those they put out of business. But this is not true of many of today's new industries."
> — *TIME* magazine, "The Automation Jobless," February 24, 1961 (Autor 2015, p.3에서 재인용)

**(f) 존슨 대통령 자문위원회(1966) 결론 — 명문**
> "Thus technological change (along with other forms of economic change) is an important determinant of the precise places, industries, and people affected by unemployment. But the general level of demand for goods and services is by far the most important factor determining how many are affected, how long they stay unemployed, and how hard it is for new entrants to the labor market to find jobs. **The basic fact is that technology eliminates jobs, not work**" (Bowen 1966, p. 9).

> 국역: "기본적인 사실은, 기술은 **일자리**를 없애지 **일**을 없애지 않는다는 것이다."

**한계·반박**
- 2015년 논문이다. 생성형 AI 이전이며, Autor는 "폴라니의 역설이 곧 극복될 것 같지 않다"고 판단했다 — 2022년 이후 LLM은 이 판단의 일부를 무효화했다. 책에서 인용할 때 반드시 시점을 명시할 것.
- ATM 사례는 저자 본인이 (c)에서 "전형(paradigmatic)으로 받아들이지 말라"고 명시적으로 봉인했다. **한국 경영 담론에서 가장 자주 오용되는 사례**이므로, 이 봉인 문장을 함께 옮기는 것이 이 책의 차별점이 될 수 있다.
- 은행 창구직 고용은 그 후 실제로 감소했다(BLS 기준). "ATM 사례"의 시간 창이 2010년에서 끝난다는 점을 짚어야 한다. (⚠️ 2010년 이후 BLS teller 통계는 이번 리서치에서 미확인)

---

### 3. 【최우선】 Bessen — ATM과 은행 창구직원의 **1차 출처**

#### 3-1. 단행본 (사례의 정본)

> James Bessen, ***Learning by Doing: The Real Connection between Innovation, Wages, and Wealth***. New Haven: Yale University Press, 2015.
> ISBN **978-0-300-19566-8** (hardcover, 0300195664) / e-book ISBN 9780300213645, DOI [10.12987/9780300213645](https://doi.org/10.12987/9780300213645) · 약 310쪽 · **[단행본]**
> 확인 경로: OpenLibrary(초판 1995→오기 아님, first_publish_year 2015, Yale University Press), Crossref(Yale UP, 전자책 DOI 및 챕터 DOI 존재: BIBLIOGRAPHY pp.263–286, INDEX pp.287–296)
> ⚠️ **본문 지면(페이지) 수준의 인용은 미확인** — 책 전문 접근 불가. 아래 3-2가 저자 본인이 쓴 요약본이므로 실무상 이것을 1차 인용원으로 쓸 것을 권장.

#### 3-2. 저자 본인 요약 기사 (실제로 검증 가능한 1차 출처)

> James Bessen, "**Toil and Technology**," ***Finance & Development*** (IMF quarterly magazine), Vol. **52**, No. **1**, **March 2015**.
> URL: https://www.imf.org/external/pubs/ft/fandd/2015/03/bessen.htm · **[WP]** (기관 발간물, 비피어리뷰)
> 원문 각주: 이 기사는 저자의 *Learning by Doing* 에 기반한다고 명시.
> 동일 본문 재게재본(저자 바이라인 확인): https://www.atmmarketplace.com/articles/tellers-technology-and-atms/ — 동일 수치 교차 확인 완료.

**인용 가능한 문장·수치 (VERBATIM, 저자 본인 문장)**

ATM/창구:
> "Automated teller machines (ATMs) were first installed in the United States and other developed economies in the **1970s**."
> "**Starting in the mid-1990s, banks rapidly increased their use of ATMs.**"
> "**over 400,000 are installed in the United States alone today**" *(today = 2015년 3월 기준)*
> "**the number of tellers required to operate a branch office in the average urban market fell from 20 to 13 between 1988 and 2004**"
> "**Bank branches in urban areas increased 43 percent**"
> "**the number of bank teller jobs did not decrease as the ATMs were rolled out**"

> 국역: "도시 지역 평균 시장에서 지점 하나를 운영하는 데 필요한 창구직원 수는 **1988년 20명에서 2004년 13명으로** 줄었다. (그러나) 도시 지역 은행 지점 수는 **43% 증가**했다. …ATM이 보급되는 동안 은행 창구직 일자리 수는 줄지 않았다."

19세기 방직 사례 — ATM보다 오히려 더 강한 사례:
> "**power looms automated 98 percent of the labor needed to weave a yard of cloth**"
> "**the number of factory weaving jobs increased over this period**"
> "**weavers' wages rose sharply compared with those of other workers during the late 19th century**"

> 국역: "역직기는 옷감 1야드를 짜는 데 필요한 노동의 **98%를 자동화**했다. (그럼에도) 이 기간 공장 방직 일자리 수는 **증가**했고, 방직공의 임금은 다른 노동자에 비해 **급격히 상승**했다."

> ※ **책에 쓰기 좋은 조합:** "98% 자동화 → 일자리 증가"는 ATM 사례보다 수치가 극적이고, 저자 본인의 문장이라 인용 안전성이 높습니다. AX 담론에서 "80% 자동화하면 인력이 80% 남는다"는 직관을 깨는 데 유용합니다.

**Autor(2015)판 수치와의 대조표** — 두 출처의 수치가 미묘하게 다르니 책에서 섞어 쓰지 말 것:

| 항목 | Bessen 본인 (F&D 2015) | Autor (JEP 2015, Bessen 2015 인용) |
|---|---|---|
| ATM 대수 | "over 400,000 … today" | "quadrupled from approximately **100,000 to 400,000 between 1995 and 2010**" |
| 지점당 창구직원 | "**from 20 to 13** between 1988 and 2004" | "fell by **more than a third** between 1988 and 2004" |
| 도시 지점 수 | "increased **43 percent**" | "rose by **more than 40 percent**" |
| 창구직원 총수 | "did not decrease" (수치 없음) | "**from 500,000 to approximately 550,000** over the 30-year period from 1980 to 2010" |

> ※ 창구직원 총수의 절대 수치(50만→55만, 1980–2010)는 **Autor 논문에만** 등장하며, Bessen 본인 기사에는 없습니다. 책에서 이 숫자를 쓸 때는 "Autor(2015)가 Bessen(2015)을 인용해 제시한 수치"로 표기하는 것이 정확합니다.

#### 3-3. Bessen의 *Economic Policy* 논문

> James Bessen, "Automation and jobs: when technology boosts employment," ***Economic Policy***, vol. **34**, issue **100**, **October 2019**, pp. **589–626**. (온라인 게재: 2019-10-01 / OUP 표기 "Published: 01 July 2020")
> DOI: [10.1093/epolic/eiaa001](https://doi.org/10.1093/epolic/eiaa001) · ISSN 0266-4658 · **[PR]**
> WP 판본: SSRN **10.2139/ssrn.2935003** (2017), Boston University School of Law, Technology & Policy Research Initiative · **[WP]**
> OA(제출본, CC BY-NC-SA): https://scholarship.law.bu.edu/faculty_scholarship/815
> ⚠️ BU 리포지토리의 "Recommended Citation"은 시작 페이지를 **585**로, Crossref/OUP는 **589**로 표기 — 불일치. 책에서는 **589–626**(발행처 기준) 사용 권장.

**초록 전문 (VERBATIM, Crossref/OUP)**
> "Will new technologies cause industries to shed jobs, requiring novel policies to address mass unemployment? **Sometimes productivity-enhancing technology increases industry employment instead. In manufacturing, jobs grew along with productivity for a century or more; only later did productivity gains bring declining employment. What changed? The elasticity of demand.** Using data over two centuries for US textile, steel and auto industries, this paper shows that **automation initially spurred job growth because demand was highly elastic. But demand later became satiated, leading to job losses.** A simple model explains why this pattern might be common, suggesting that today's technologies may cause some industries to decline and others to grow. **Automation might not cause mass unemployment, but it may well require workers to make disruptive transitions to new industries, requiring new skills and occupations.**"

**핵심 주장 / 이 책에 쓸 수 있는 부분**
Bessen의 진짜 기여는 "자동화하면 일자리가 는다"가 아니라 **조건부 명제**다: 수요의 가격탄력성이 높은 구간에서는 자동화가 고용을 늘리고, 수요가 포화되면 같은 자동화가 고용을 줄인다. **똑같은 기술이 산업의 생애주기 어디에 있느냐에 따라 부호가 뒤집힌다.**

AX 챕터에 이 논리를 옮기면: "AI로 처리 단가가 떨어졌을 때, 우리 서비스의 수요는 탄력적인가 포화되었는가?"가 **남는 인력을 어디로 보낼지의 1차 분기점**이 된다. 탄력적이면 같은 사업 안에서 볼륨 확대로 흡수되고, 포화되었으면 새 사업/새 직무로 옮겨야 한다. — 이 책의 "확보한 FTE를 어디에 쓰나"에 가장 잘 맞는 이론적 틀입니다.

**한계·반박**
- 대상 산업이 **미국 섬유·철강·자동차 3개 제조업, 2세기 시계열**이다. 서비스/지식노동으로의 외삽은 저자가 하지 않는다.
- 수요탄력성 추정 자체가 장기 시계열 식별 문제를 안는다.
- ⚠️ 논문 본문의 구체 수치(산업별 탄력성 추정치, 고용 전환점 연도)는 이번 리서치에서 **미확인** — BU 리포지토리와 OUP 모두 403 차단.

---

### 4. 고용 안정성과 노동자의 기술변화 수용

#### 4-1. Ichniowski, Shaw & Prennushi (1997) — 【이 주제의 최강 증거】

**서지**
> Casey Ichniowski, Kathryn Shaw, and Giovanni Prennushi, "The Effects of Human Resource Management Practices on Productivity: A Study of Steel Finishing Lines," ***American Economic Review***, vol. **87**, no. **3** (June 1997), pp. **291–313**.
> JSTOR: https://www.jstor.org/stable/2951347 · DOI 없음(AER 1999년 이전) · **[PR]**
> WP 판본: NBER Working Paper No. **5333, November 1995** · https://www.nber.org/papers/w5333 · **[WP]**
> ⚠️ NBER 페이지의 published-version 표기가 "**Vol. 86** (June 1997)"로 되어 있으나 이는 NBER 측 오기. OpenAlex/JSTOR 기준 **Vol. 87, No. 3**이 정확.

**게재본 초록 전문 (VERBATIM)**
> "The authors investigate the productivity effects of innovative employment practices using data from a sample of **thirty-six homogeneous steel production lines owned by seventeen companies**. The productivity regressions demonstrate that lines using a set of innovative work practices, which include **incentive pay, teams, flexible job assignments, employment security, and training**, achieve substantially higher levels of productivity than do lines with the more traditional approach, which includes narrow job definitions, strict work rules, and hourly pay with close supervision. Their results are consistent with recent theoretical models which stress **the importance of complementarities among work practices.**"

> ※ "employment security(고용 안정성)"가 **혁신적 관행 묶음의 5대 구성요소 중 하나로 초록에 명시**되어 있습니다. 이 책의 논지를 지지하는 가장 직접적인 학술 문장입니다.

#### 4-2. Ichniowski & Shaw (2003) — 위 논문의 **수치를 저자 본인이 verbatim으로 재보고**

**서지**
> Casey Ichniowski and Kathryn Shaw, "Beyond Incentive Pay: Insiders' Estimates of the Value of Complementary Human Resource Management Practices," ***Journal of Economic Perspectives***, vol. **17**, no. **1**, Winter 2003, pp. **155–180**.
> DOI: [10.1257/089533003321164994](https://doi.org/10.1257/089533003321164994) · **[PR]**

**인용 가능한 문장·수치 (VERBATIM) — 이 절의 핵심**

**(a) "고용 안정 보장"이 고성과 HRM 시스템의 7대 구성요소 중 하나**
> "At one extreme is the "high-involvement" human resource management system that incorporates innovative practices across all seven areas of human resource management that we consider—**extensive employee screening, elaborate pay-for-performance plans, work teams, employment security guarantees, extensive labor-management communications, broad job definitions and ongoing training in skills and problem solving.** At the other extreme is the "traditional" system with no innovative human resource management practices in any of these seven areas."

> 국역: "…광범위한 직원 선발, 정교한 성과급 제도, 작업팀, **고용 안정 보장**, 광범위한 노사 커뮤니케이션, 넓은 직무 정의, 그리고 기술·문제해결 역량에 대한 지속적 훈련."

**(b) 효과 크기 — 6.7% / 3.2% / 1.4%**
> "Given these measures of the lines' human resource management environments, regression results for finishing lines show that, relative to the traditional human resource management system, **productivity is 6.7 percent higher under the innovative human resource management system, 3.2 percent higher under the "high-teamwork" system and 1.4 percent higher under the "communications" system.** Lines that adopt a full bundle of innovative work practices therefore achieve the highest levels of productivity, and the traditional system produces the lowest performance. **The same hierarchy of performance is also observed when examining quality of output.**"

**(c) 부분 도입은 효과 없음 — 이 책의 "찔끔 도입 금지" 논지에 직결**
> "We also estimate the productivity effects of changes in individual human resource management practices, and **in no case did an individual human resource management innovation, such as problem-solving teams, have a measurable effect on productivity by itself.** These patterns suggest that important complementarities exist among innovative human resource management practices. **As a bundle, the innovative human resource management practices work, but are ineffective when individual practices are instituted.**"

> 국역: "개별 HRM 혁신(예: 문제해결팀)이 **단독으로** 생산성에 측정 가능한 효과를 낸 사례는 **단 한 건도 없었다.** …묶음으로는 작동하지만, 개별 관행으로 도입하면 효과가 없다."

**(d) 금액 환산**
> "The estimated 6.7 percent productivity difference between a line with the most innovative human resource management system and a line with the most traditional human resource management system is economically important. **It translates into a difference in profitability of about $2.24 million annually per finishing line.**"

**(e) 표본·설계 — insider econometrics**
> "**The first study uses panel data from 36 finishing lines that coat and treat very large coils of flat-rolled steel.** The second study uses panel data from 34 minimill production lines… Both studies **include almost all of the production lines of these types in the United States and develop large panels with well over 2,000 monthly observations in each study's sample.**"

> "we conduct field research at every production line and interview experienced workers and production experts…we interview multiple respondents at each line, including production supervisors, human resource management managers, line workers and union officials…"

**(f) 미국 확산 통계 (원출처: Osterman 2000)**
> "Osterman (2000) reports that by **1997, 85 percent of establishments had adopted at least one innovative human resource management practice, up from 65 percent in 1992. The percentage of establishments with more than one innovative human resource management practice increased from 38 to 71 percent over this same five-year period.**"
> ⚠️ 이 수치의 원출처는 Osterman(2000)이며, Ichniowski & Shaw의 인용을 통한 재인용입니다. 직접 인용하려면 Osterman 원문 확인 필요.

**한계·반박**
- 산업 하나(미국 철강 마감라인)의 36개 라인. **외적 타당성이 좁다.**
- 고용 안정 보장을 개별적으로 분리한 효과 추정은 없다(묶음 효과만). "고용을 보장하면 생산성이 X% 오른다"라고 쓰면 **과잉 해석**이다. 정확한 진술은 "고용 안정 보장을 **포함한** 묶음이 6.7% 높은 생산성과 연관된다"이다.
- 고정효과 모형에서는 전통형→혁신형으로 완전 전환한 라인이 없어 최대 효과를 식별하지 못한다(저자들 각주 5에서 명시).

#### 4-3. MacDuffie (1995)

> John Paul MacDuffie, "Human Resource Bundles and Manufacturing Performance: Organizational Logic and Flexible Production Systems in the World Auto Industry," ***ILR Review*** (당시 *Industrial and Labor Relations Review*), vol. **48**, no. **2** (January 1995), pp. **197–221**.
> DOI: [10.1177/001979399504800201](https://doi.org/10.1177/001979399504800201) (JSTOR: 10.2307/2524483) · **[PR]** · 폐쇄 접근, OA PDF 없음

**초록 전문 (VERBATIM, 발행처 메타데이터 기준)**
> "Using a unique international data set from a **1989–90 survey of 62 automotive assembly plants**, the author tests two hypotheses: that **innovative HR practices affect performance not individually but as interrelated elements in an internally consistent 'bundle' or system**; and that these HR bundles contribute most to assembly plant productivity and quality when they are integrated with manufacturing policies under 'organizational logic' of a flexible production system. Analysis of the data, which tests three indices representing distinct human resource practices and manufacturing policies, supports both hypotheses. **Flexible production plants with team-based work systems, 'high-commitment' HR practices (such as contingent compensation and extensive training), and low inventory and repair buffers consistently outperformed mass production plants.**"

**이 책에 쓸 수 있는 부분**
"묶음(bundle)" 개념의 원전. AX 도입을 기술 프로젝트로만 하면 안 되고 **조직 논리와 함께 묶어야 한다**는 논지의 학술 근거. Ichniowski et al.(1997)과 한 쌍으로 인용하면 "단일 산업 결과"라는 반박을 상당히 방어할 수 있다(자동차 62개 공장 국제 표본 + 철강 36개 라인 미국 전수).

**한계·반박**
- 62개 공장의 **횡단면(cross-section)** 데이터. 인과 추론이 약하다. 역인과(성과 좋은 공장이 혁신 관행을 도입) 가능성을 배제하지 못한다.
- 1989–90년 자료. IMVP(MIT International Motor Vehicle Program) 서베이 기반.
- ⚠️ 본문의 구체 생산성 수치(공장당 조립시간 등)는 **미확인** — 전문 접근 불가.

#### 4-4. Womack, Jones & Roos (1990)

> James P. Womack, Daniel T. Jones, and Daniel Roos, ***The Machine That Changed the World***. New York: Rawson Associates / Macmillan, **1990**. 약 323쪽.
> ISBN 0029463165 / 9780029463161 (초판), 이후 판: 0060974176(Harper Perennial), 1416554521 / 9781416554523(Free Press, 2007 개정판)
> 확인 경로: OpenLibrary (first_publish_year **1990**, 저자 3인 확인) · **[단행본]**

**핵심 주장**
MIT IMVP 5년 연구를 대중서로 옮긴 책. "린 생산(lean production)"이라는 용어를 대중화했고, 대량생산 대비 린 생산이 인력·재고·불량·개발기간 전 영역에서 우위임을 국제 비교로 제시했다.

**이 책에 쓸 수 있는 부분**
"고용 보장이 개선 참여를 이끈다"는 도요타 생산방식의 서사적 원전. 다만 —

**한계·반박 (중요)**
- ⚠️ **책 본문의 구체 수치(공장별 조립시간, 불량률, 개발 리드타임 등)는 이번 리서치에서 검증하지 못했습니다.** 원서 접근 불가. 이 책에서 수치를 인용하려면 **원서 해당 지면을 직접 확인**하거나, 동일 IMVP 데이터를 쓴 **MacDuffie(1995)의 피어리뷰 결과로 대체**하는 편이 안전합니다.
- *The Machine*은 대중서이며 피어리뷰 논문이 아니다. 방법론(공장 선정, 조립시간 정의)에 대한 학계 비판이 존재한다.

#### 4-5. Levine & Tyson (1990)

> **[확인됨]** David I. Levine and Laura D'Andrea Tyson, "Participation, Productivity, and the Firm's Environment," ***California Management Review***, vol. **32**, no. **4** (July 1990), pp. **86–100**. DOI: [10.2307/41166630](https://doi.org/10.2307/41166630) · **[PR]**
>
> **[⚠️ 미확인]** 동명의 장(chapter)이 Alan S. Blinder (ed.), *Paying for Productivity: A Look at the Evidence* (Washington, DC: Brookings Institution, **1990**)에 수록되어 있다는 것이 통설이나, **정확한 수록 지면(통상 pp. 183–243으로 인용됨)을 이번 리서치에서 확인하지 못했습니다.** Crossref·OpenAlex 모두 이 챕터를 색인하지 않고, Google Books API는 쿼터 초과.
> 다만 모(母) 편저서의 존재는 확인: Alan S. Blinder (ed.), *Paying for Productivity*, Brookings Institution, **1990**, ISBN 0815709994 / 9780815709992, 약 308–322쪽 (OpenLibrary).

**핵심 주장 (통설)**
참여적 작업조직이 생산성으로 이어지려면 **고용 안정성·이익 공유·수평적 임금구조·노동자 대표권**이라는 보완 조건이 필요하다. 고용 불안 상태에서는 노동자가 생산성 향상에 협조하지 않는다.

> ⚠️ **경고:** "employment guarantees elicit cooperation with productivity improvement"류의 유명한 문장은 이 챕터에서 온 것으로 널리 인용되지만, **원문을 확인하지 못했으므로 이 책에서 직접 인용(따옴표 인용)해서는 안 됩니다.** 대신 위 4-2(a)(b)의 Ichniowski & Shaw 문장을 쓰면 동일한 논지를 검증된 인용으로 낼 수 있습니다.

#### 4-6. Appelbaum, Bailey, Berg & Kalleberg (2000)

> Eileen Appelbaum, Thomas Bailey, Peter Berg, and Arne L. Kalleberg, ***Manufacturing Advantage: Why High-Performance Work Systems Pay Off***. Ithaca, NY: Cornell University Press (ILR Press).
> ISBN **9780801437656** (hardcover). Cornell UP 도서 페이지에서 서명·저자 4인·발행처 확인. **[단행본]**
> 학술 서평 3편으로 교차 확인: *Industrial and Labor Relations Review* 55(1), Oct 2001, p.175 (DOI 10.2307/2696195) · *Academy of Management Review* 26(3), Jul 2001, p.459 (DOI 10.2307/259189) · *Contemporary Sociology* 30(3), May 2001, p.250 (DOI 10.2307/3089250)
> ⚠️ 발행 연도 **2000**은 서평 시점(2001년 5·7·10월)과 정합적이나, 발행처 페이지에서 직접 확인하지 못했습니다.

**핵심 주장 (통설)**
고성과 작업시스템(HPWS)이 성과로 이어지는 경로는 **AMO 모형** — Ability(역량), Motivation(동기), Opportunity to participate(참여 기회) 세 요소가 동시에 갖춰져야 한다. 철강·의류·의료기기 3개 산업의 현장 조사.

> ⚠️ 본문 수치·인용문 **미확인**.

---

### 5. 최근(2019–2026) 증거 — 재배치 vs 해고, 재교육, 기업 수준 실증

> **이 절이 이 책의 "남는 FTE를 어떻게 할 것인가" 챕터에서 가장 값이 나갑니다.** Acemoglu-Restrepo가 "총량은 마이너스"를 말한다면, 아래 논문들은 **"같은 자동화라도 기업이 어떻게 대응하느냐에 따라 노동자의 결말이 갈린다"**를 실증합니다.

#### 5-1. 【최우선】 Bessen, Goos, Salomons & van den Berge — 자동화하는 기업의 노동자에게 무슨 일이 일어나는가

**서지**
> James Bessen, Maarten Goos, Anna Salomons, and Wiljan van den Berge, "What Happens to Workers at Firms that Automate?" ***The Review of Economics and Statistics***, vol. **107**, no. **1**, pp. **125–141**. (온라인 선공개 **2023-02-07**; 인쇄 호는 2025)
> DOI: [10.1162/rest_a_01284](https://doi.org/10.1162/rest_a_01284) · **[PR]**
> WP 판본 (전문 OA, 인용 가능): "**Automatic Reaction – What Happens to Workers at Firms that Automate?**", **CPB Discussion Paper, February 2019** (본문 일자 January 2019), CPB Netherlands Bureau for Economic Policy Analysis. SSRN DOI 10.2139/ssrn.3328877 · **[WP]**
> PDF: https://www.cpb.nl/sites/default/files/omnidownload/CPB-Discussion-Paper-390-Automatic-Reaction-What-Happens-to-Workers-at-Firms-that-Automate.pdf

**게재본 초록 전문 (VERBATIM)**
> "We estimate the impact of firm-level automation on individual worker outcomes by combining Dutch microdata with a direct measure of automation expenditures covering all private nonfinancial sector firms. Using a novel difference-in-differences event-study design leveraging lumpy investment, we find that **automation increases the probability of incumbent workers separating from their employers. Workers experience a five-year cumulative wage income loss of 9% of one year's earnings, driven by decreases in days worked.** These adverse impacts of automation are **larger in smaller firms, and for older and middle-educated workers.** By contrast, **no such losses are found for firms' investments in computers.**"

> ※ 게재본은 **9%**, WP판은 **8%**로 수치가 다릅니다. 반드시 판본을 명시하세요.

**WP판(2019)의 상세 수치 — 전부 VERBATIM**

WP 초록:
> "We provide the first estimate of the impacts of automation on individual workers by combining Dutch micro-data with a direct measure of automation expenditures covering firms in all private non-financial industries over **2000-2016**. Using an event study differences-in-differences design, we find that automation at the firm increases the probability of workers separating from their employers and decreases days worked, leading to a **5-year cumulative wage income loss of about 8% of one year's earnings for incumbent workers**. **We find little change in wage rates.** Further, lost wage earnings are only partially offset by various benefits systems and are **disproportionately borne by older workers and workers with longer firm tenure**. **Compared to findings from a literature on mass layoffs, the effects of automation are more gradual and automation displaces far fewer workers**, both at the individual firms and in the workforce overall."

이직 확률:
> "Indeed, in the automation year, the separation probability for incumbent workers is **2.1 percentage points higher**, where the (matched) control group incumbent separation probability is **13 percent**, such that the automation-year effect corresponds to a **16 percent rise** in firm separation for these workers. **Cumulatively after five years, incumbents have a 8.6 percentage point higher chance of firm separation: this is a 24 percent rise** compared to the average five-year (cumulative) chance of firm separation among control group workers of **36 percent**."

> "Recent hires experience a **4.1 percentage point increase** in the chance of firm separation in the year of the automation event."

**대량해고와의 정면 비교 — 이 책에서 가장 중요한 문단**
> "The mass layoff studies typically include workplaces where **30 percent or more** of the employees are separated, and even larger portions of the workforce are laid off in studies of plant closings. **In contrast, only 2 percent of incumbent workers leave their employer in the year of an automation event relative to the control group. Even after 5 years, automation only accounts for the separation of 8.6 percent of incumbent workers (7.2 percent for recent hires).** Putting event exposure and impact together, **the annual separation hazard from automation is around 0.77 percent (0.086 × 0.09), compared to 4 percent for mass lay-offs. As such, the overall risk that a worker will separate from their firm in a mass layoff or plant closing in any year is almost an order of magnitude greater than the risk of firm separation due to automation.**"

**속도의 차이 — "자동화는 천천히 온다"**
> "This discussion highlights another difference from findings on mass lay-offs and plant closings: **the impact of automation occurs relatively slowly while the mass layoff literature reports an immediate impact followed by a period of adjustment. The slow response may reveal something about the nature of automation. If automation were a simple story of machines replacing humans, then most of the job losses would occur the year of the automation event or, perhaps, the year after. The slow response suggests that automation appears to involve substantial adjustment costs, perhaps reflecting significant complementarities with workers.**"

**퇴출된 사람의 손실 — 대량해고 대비**
> "Incumbent workers who leave their employer after an automation event experience an average loss of earnings of about **17 percent in the fifth year after the event**. By comparison, **Jacobson et al. (1993) find that long-tenured workers in Pennsylvania experienced a loss of earnings of 25 percent six years after a mass layoff. Couch and Placzek (2010) find losses of 13 to 15 percent six years after a mass layoff** in another sample. However, **Jacobson et al. (1993) report an average earnings loss of over 40 percent immediately following the layoff and Couch and Placzek (2010) report an immediate loss of 33 percent. The earnings loss during the first year of automation is less than 4 percent by comparison.**"

**결론부**
> "Incumbent workers are around **25 percent more likely to separate** from their firm, followed by a decrease in days worked. This leads to a five-year cumulative wage income loss of about **8% of one year's earnings** for incumbent workers. We find little change in wage rates. Further, lost wage earnings are only partially offset by various benefits systems, and disproportionately borne by older workers – **the rate of early retirement increases by 24% as a result of automation.**"

**사회안전망의 상쇄율 — 매우 인용가치 높음**
> "We find that incumbent workers do receive additional benefit income following an automation event…**only 15 percent of the negative wage income impact is offset.**"

> 국역: "임금소득 손실의 **15%만** (실업급여·복지·장애급여를 합쳐도) 보전된다."

**컴퓨터 투자와의 대비 — 이 책의 논지에 결정적**
게재본 초록: "**By contrast, no such losses are found for firms' investments in computers.**"
> 국역: "이에 비해 기업의 **컴퓨터 투자에서는 그런 손실이 발견되지 않는다.**"
> ※ "IT 투자 ≠ 자동화 투자"라는 구분이 실증적으로 확인된 것. AX 예산을 무엇으로 잡느냐가 노동자 결말을 가른다는 논지에 쓸 수 있습니다.

**이 책에 쓸 수 있는 부분**
- "AI 도입 = 대량해고"라는 대중 서사를 **데이터로 정확히 반박**하되, "그래서 괜찮다"로 가지 않게 하는 균형 자료. 연간 이직 위험이 대량해고 대비 **약 1/5(0.77% vs 4%)**.
- **고령·장기근속자에게 손실이 집중**되고 **조기퇴직이 24% 증가**한다는 결과는, "재배치 대상 선정에서 누가 밀려나는지"를 다루는 실무 논의에 직결.
- 사회안전망이 **15%만** 보전한다 → 회사 내부 재배치가 사회적 이전보다 훨씬 효율적인 완충장치라는 논지.

**한계·반박**
- 네덜란드 2000–2016. 강한 고용보호·조밀한 사회안전망을 가진 국가. 한국·미국 외삽 시 주의.
- 자동화 측정이 **회계상 "자동화 지출" 항목의 급증(lumpy spike)**이다. 무엇을 자동화로 계상하는지가 기업마다 다를 수 있다.
- 생성형 AI 이전 시기다.

#### 5-2. 【최우선】 Dauth, Findeisen, Suedekum & Woessner — 독일: 로봇이 오면 사람은 **회사 안에서 옮겨간다**

**서지**
> Wolfgang Dauth, Sebastian Findeisen, Jens Suedekum, and Nicole Woessner, "The Adjustment of Labor Markets to Robots," ***Journal of the European Economic Association***, vol. **19**, no. **6** (2021), pp. **3104–3153**. (온라인 2021-03-22)
> DOI: [10.1093/jeea/jvab012](https://doi.org/10.1093/jeea/jvab012) · **[PR]**
> OA 전문: https://kops.uni-konstanz.de/server/api/core/bitstreams/1db5d40b-7c39-496f-b543-a8c3afe19f69/content

**초록 전문 (VERBATIM)**
> "We use detailed administrative data to study the adjustment of local labor markets to industrial robots in Germany. **Robot exposure, as predicted by a shift-share variable, is associated with displacement effects in manufacturing, but those are fully offset by new jobs in services. The incidence mostly falls on young workers just entering the labor force. Automation is related to more stable employment within firms for incumbents, and this is driven by workers taking over new tasks in their original plants. Several measures indicate that those new jobs are of higher quality than the previous ones.** Young workers also adapt their educational choices, and substitute away from vocational training towards colleges and universities. Finally, industrial robots have benefited workers in occupations with complementary tasks, such as managers or technical scientists. (JEL: J24, O33, F16, R11)"

**인용 가능한 문장·수치 (VERBATIM)**

**(a) 재배치의 실증 — 이 책 챕터 전체의 근거 문장**
> "**Incumbent workers, maybe paradoxically at first glance, actually see an increase in their plant tenure in response to more automation.**"

> "Our third main contribution shows that this latter effect—that is, **automation causing more stable employment within firms—is driven by workers taking over new roles within their original plants. Displacement of old tasks, hence, takes place. However, it is swiftly offset by transitions of incumbent workers into new tasks for the same employer. Several measures indicate that those new jobs are of higher quality than the previous ones: The new occupations pay higher wages, are characterized by a larger share of abstract instead of routine tasks, and a higher college share.**"

> 국역: "기존 과업의 대체는 실제로 일어난다. **그러나 그것은 같은 고용주 밑에서 기존 노동자가 새로운 과업으로 이동함으로써 신속히 상쇄된다.** …새 직무는 이전보다 임금이 높고, 루틴 대신 추상 과업 비중이 크며, 대졸자 비중이 높다."

**(b) 회사에 남은 사람과 밀려난 사람 — 이 책의 가장 날카로운 대조**
> "One key result of the analysis is that **average earnings are hardly affected by robots. But effects differ strongly across workers with different adjustment patterns: Those who are retained by their plants experience positive earnings effects as they transition into new tasks. Workers who are forced to switch plants, industries, or leave manufacturing see significant earnings losses, however.**"

> "Automation mostly increases inequality **within** groups of ex-ante similar manufacturing workers. **It creates large gaps between those who manage to stay at their original plant (thereby reaping the benefits of automation through longer tenure and higher wages) and those who are forced to leave their original employer, as they typically face an earnings drop and do not easily recover.**"

> 국역: "자동화는 주로 **사전적으로 유사한** 제조업 노동자 집단 **내부의** 불평등을 키운다. 원래 공장에 **남는 데 성공한 사람**(장기근속과 높은 임금으로 자동화의 이득을 거둔다)과 **떠밀려 나간 사람**(임금이 떨어지고 쉽게 회복하지 못한다) 사이에 큰 격차를 만든다."

> ※ **이 책의 챕터 주제문으로 쓸 수 있는 문장입니다.** "자동화가 노동자에게 좋냐 나쁘냐"가 아니라 "**같은 자동화가 남긴 사람과 내보낸 사람을 정반대로 갈라놓는다**"는 것.

**(c) 정량 — 원 공장 근속일 증가**
> "Quantitatively, it translates into an increase of **171 (= 8.3594 × [26.052 − 5.547]) days of employment (over 20 years) in one's original plant** for a worker starting out in the manufacturing industry at the **75th percentile of robot exposure relative to a worker from the 25th percentile. This number grows to 894 days when comparing the 90th and 10th percentiles.**"

**(d) 로봇 1대당 대체 인원 — 미국과의 비교**
> "**The preferred estimate from column (4) implies a displacement effect of 1.7 workers per newly installed robot.**"
> "Replicating this empirical strategy for Germany, we also find significant displacement effects, **although around 50% smaller on average.** The key difference, however, is that **we additionally identify significant and offsetting re-allocation effects.**"
> Table 4 "Effect of one robot" 행 (총 E/POP 및 부문별): 0.3 / −1.8 / −2.0 / −1.7 / 1.6 / 1.6 / 2.0 (⚠️ pdftotext에서 부호가 소실되어 아래 부호는 본문 서술로부터 복원. 표 인용 시 원본 재확인 필요)

**(e) 대량해고와의 대비 (각주 27)**
> "**industrial robots did not trigger mass layoff episodes in Germany**, which limits the scope for negative spillovers."

**(f) 숙련편향이 아니다**
> "**Stated differently, we cannot detect evidence of skill-biased technological change.**"

**한계·반박**
- 독일 제조업. **강한 노조·직장평의회(Betriebsrat)·직업훈련 체계**가 배경이다. 그 제도 없이 "재배치는 저절로 일어난다"고 읽으면 오독.
- 부담이 **신규 진입 청년층**에 전가되었다(초록 명시). 내부자의 안정은 외부자의 기회 상실로 지불되었을 수 있다.
- shift-share 설계의 통상적 식별 논쟁 적용.

#### 5-3. 【최우선】 Battisti, Dustmann & Schönberg — 기술·조직 변화와 **재교육**

**서지**
> Michèle Battisti, Christian Dustmann, and Uta Schönberg, "Technological and Organizational Change and the Careers of Workers," ***Journal of the European Economic Association***, vol. **21**, no. **4** (2023), pp. **1551–1594**. (온라인 2023-02-28)
> DOI: [10.1093/jeea/jvad014](https://doi.org/10.1093/jeea/jvad014) · **[PR]**
> OA 전문: https://eprints.gla.ac.uk/293212/2/293212.pdf

**초록 전문 (VERBATIM)**
> "This paper investigates the effects of technological and organizational change (T&O) on jobs and workers. We show that **although T&O reduces firm demand for routine relative to abstract task-based jobs, affected workers do not face higher probability of non-employment or lower earnings growth than unaffected workers. Rather, firms that adopt T&O offer routine workers retraining opportunities to upgrade to more abstract jobs.** **Older workers form an important exception: T&O increases the risk that they permanently withdraw from the labor market and reduces their earnings, regardless of the tasks they performed in the firm prior to T&O.**"

> 국역: "기술·조직 변화는 추상 과업 직무 대비 루틴 직무에 대한 기업 수요를 줄이지만, **영향을 받은 노동자들이 비고용 확률이 더 높거나 소득 증가율이 더 낮아지지는 않는다. 오히려 기술·조직 변화를 도입한 기업들은 루틴 노동자에게 더 추상적인 직무로 상향 이동할 수 있는 재교육 기회를 제공한다.** 고령 노동자는 중요한 예외다 — 기술·조직 변화는 그들이 노동시장에서 영구히 이탈할 위험을 높이고 소득을 줄이며, 이는 그들이 이전에 어떤 과업을 수행했는지와 무관하다."

**이 책에 쓸 수 있는 부분**
"재교육을 통한 내부 상향 재배치"가 **관찰된 기업 행동**임을 보이는 가장 직접적인 증거. 동시에 **고령 노동자 예외**를 명시하므로, 이 책이 "재배치 만능론"으로 미끄러지지 않게 하는 균형추가 된다. 5-1(고령·장기근속자에게 손실 집중)과 결론이 일치하므로 두 논문을 나란히 인용하면 매우 강한 문단이 됩니다.

**한계·반박**
- 독일 데이터. 5-2와 같은 제도 배경 유보 적용.
- ⚠️ 본문의 구체 수치(재교육 참여율, 상향 이동률 등)는 이번 리서치에서 **미확인**. OA PDF는 확보 가능(위 링크).

#### 5-4. Koch, Manuylov & Smolka — 스페인: 로봇 도입 기업은 **순 일자리 창출**

**서지**
> Michael Koch, Ilya Manuylov, and Marcel Smolka, "Robots and Firms," ***The Economic Journal***, vol. **131**, no. **638** (2021), pp. **2553–2584**. (온라인 2021-01-30)
> DOI: [10.1093/ej/ueab009](https://doi.org/10.1093/ej/ueab009) · **[PR]**
> OA PDF: https://academic.oup.com/ej/article-pdf/131/638/2553/39509703/ueab009.pdf

**초록 발췌 (VERBATIM)**
> "We study the microeconomic implications of robot adoption using a rich panel data set of **Spanish manufacturing firms over a 27-year period (1990–2016)**. … we establish robust evidence for **positive selection, i.e., ex ante better performing firms (measured through output and labour productivity) are more likely to adopt robots.** … we find that **robot adoption generates substantial output gains in the vicinity of 20–25% within four years, reduces the labour cost share by 5–7% points, and leads to net job creation at a rate of 10%.** These results are robust to controlling for non-random selection into robot adoption through a difference-in-differences approach combined with a propensity score reweighting estimator."

**이 책에 쓸 수 있는 부분**
**기업 수준에서는 자동화가 순 고용을 늘린다**(+10%)는 결과. Acemoglu-Restrepo의 지역·총량 마이너스와 정면으로 병치하면 "**어느 단위에서 보느냐에 따라 부호가 뒤집힌다**"는 이 책의 핵심 논지를 뒷받침한다. 즉 자동화한 기업은 커지고, 자동화하지 않은 경쟁사가 줄어든다 — 조직 내부 의사결정자의 관점에서는 이쪽이 더 현실적인 프레임.

**한계·반박**
- **선택 편의**가 크다(저자들도 "positive selection"을 명시). 원래 잘하던 기업이 로봇을 도입한다.
- 기업 수준 +10%가 산업·경제 전체의 +를 뜻하지 않는다(사업 이전 효과, business stealing).
- 스페인 제조업.

#### 5-5. Acemoglu, Autor, Hazell & Restrepo — AI의 총량 효과는 **아직 탐지되지 않는다**

**서지**
> Daron Acemoglu, David Autor, Jonathon Hazell, and Pascual Restrepo, "Artificial Intelligence and Jobs: Evidence from Online Vacancies," ***Journal of Labor Economics***, vol. **40**, no. **S1** (April 2022), pp. **S293–S340**.
> DOI: [10.1086/718327](https://doi.org/10.1086/718327) · **[PR]**
> OA 전문(LSE): https://researchonline.lse.ac.uk/id/eprint/113325/1/AI_And_Jobs.pdf

**초록 전문 (VERBATIM)**
> "We study the impact of artificial intelligence (AI) on labor markets using establishment-level data on the near universe of online vacancies in the United States from 2010 onward. There is rapid growth in AI-related vacancies over 2010–18 that is driven by establishments whose workers engage in tasks compatible with AI's current capabilities. **As these AI-exposed establishments adopt AI, they simultaneously reduce hiring in non-AI positions and change the skill requirements of remaining postings. While visible at the establishment level, the aggregate impacts of AI-labor substitution on employment and wage growth in more exposed occupations and industries is currently too small to be detectable.**"

**이 책에 쓸 수 있는 부분**
"AI가 일자리를 없앤다"는 주장에 대한 **동일 저자군의 자기 절제**. 사업장 수준에서는 보이지만(**비AI 직무 채용 축소**라는 구체적 경로!) 총량으로는 아직 안 보인다. 특히 **"해고가 아니라 채용 축소"**라는 관찰은 이 책의 실무 논의(자연 감소 vs 재배치 vs 해고)에 직결됩니다.

**한계·반박**
- 데이터가 **2010–2018년 온라인 채용공고**. 생성형 AI(2022~) 이전이다. 2026년 시점에서 인용할 때 반드시 명시.
- 채용공고는 실제 고용이 아니다.

#### 5-6. Acemoglu & Restrepo (2022) — 과업 대체가 임금 불평등의 50~70%

**서지**
> Daron Acemoglu and Pascual Restrepo, "Tasks, Automation, and the Rise in U.S. Wage Inequality," ***Econometrica***, vol. **90**, no. **5** (2022), pp. **1973–2016**.
> DOI: [10.3982/ECTA19815](https://doi.org/10.3982/ecta19815) · **[PR]**

**초록 발췌 (VERBATIM)**
> "We document that **between 50% and 70% of changes in the U.S. wage structure over the last four decades are accounted for by relative wage declines of worker groups specialized in routine tasks in industries experiencing rapid automation.** … **The negative relationship between wage changes and task displacement is unaffected when we control for changes in market power, deunionization, and other forms of capital deepening and technology unrelated to automation.** … **Our quantitative evaluation explains how major changes in wage inequality can go hand-in-hand with modest productivity gains.**"

**이 책에 쓸 수 있는 부분**
마지막 문장이 특히 값집니다 — **"큰 불평등 변화와 미미한 생산성 향상이 함께 갈 수 있다."** AX 투자 대비 효과를 논할 때, "생산성은 별로 안 올랐는데 사람은 갈렸다"는 최악의 시나리오가 이론적으로도 실증적으로도 가능하다는 경고.

#### 5-7. Acemoglu & Restrepo (2019) — 대체 효과 vs 재도입 효과 (개념 틀)

**서지**
> Daron Acemoglu and Pascual Restrepo, "Automation and New Tasks: How Technology Displaces and Reinstates Labor," ***Journal of Economic Perspectives***, vol. **33**, no. **2** (Spring 2019), pp. **3–30**.
> DOI: [10.1257/jep.33.2.3](https://doi.org/10.1257/jep.33.2.3) · **[PR]** · OA PDF: https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.33.2.3

**초록 발췌 (VERBATIM)**
> "**Automation, which enables capital to replace labor in tasks it was previously engaged in, shifts the task content of production against labor because of a displacement effect.** As a result, automation always reduces the labor share in value added and may reduce labor demand even as it raises productivity. **The effects of automation are counterbalanced by the creation of new tasks in which labor has a comparative advantage. The introduction of new tasks changes the task content of production in favor of labor because of a reinstatement effect, and always raises the labor share and labor demand.** … **Our empirical decomposition suggests that the slower growth of employment over the last three decades is accounted for by an acceleration in the displacement effect, especially in manufacturing, a weaker reinstatement effect, and slower growth of productivity than in previous decades.**"

**이 책에 쓸 수 있는 부분**
"남는 FTE를 어디에 쓸 것인가"에 대한 **가장 정확한 이론적 답**: **새로운 과업(new tasks)을 만드는 것**. 대체 효과만 있고 재도입 효과가 없으면 노동몫이 계속 줄어든다. 조직 단위로 번역하면 — 자동화로 확보한 인력을 **기존 과업에 재배치**만 하면 재도입이 아니고, **새 과업을 설계해 붙여야** 비로소 재도입 효과다.

#### 5-8. Brynjolfsson, Li & Raymond — 생성형 AI 현장 실증

**서지**
> Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond, "Generative AI at Work," ***The Quarterly Journal of Economics***, vol. **140**, no. **2** (2025), pp. **889–942**. (온라인 2024-12-29)
> DOI: [10.1093/qje/qjae044](https://doi.org/10.1093/qje/qjae044) · **[PR]**

**초록 전문 (VERBATIM)**
> "We study the staggered introduction of a generative AI–based conversational assistant using data from **5,172 customer-support agents**. Access to AI assistance **increases worker productivity, as measured by issues resolved per hour, by 15% on average, with substantial heterogeneity across workers.** The effects vary significantly across different agents. **Less experienced and lower-skilled workers improve both the speed and quality of their output, while the most experienced and highest-skilled workers see small gains in speed and small declines in quality.** We also find evidence that **AI assistance facilitates worker learning and improves English fluency**, particularly among international agents. While AI systems improve with more training data, we find that the gains from AI adoption are largest for moderately rare problems, where human agents have less baseline experience but the system still has adequate training data. Finally, we provide evidence that **AI assistance improves the experience of work along several dimensions: customers are more polite and less likely to ask to speak to a manager.**"

**이 책에 쓸 수 있는 부분**
- **+15% 생산성**은 곧 "동일 업무량에 필요한 FTE가 약 13% 줄어든다"는 뜻이다 — 이 책의 출발점 수치로 쓰기 좋다.
- **저경력자가 가장 많이 개선되고 최고 숙련자는 오히려 품질이 소폭 하락**한다는 이질성은, 재배치 대상 선정 로직을 뒤집는다. 통념("저성과자를 내보낸다")과 반대 방향의 시사점.
- "AI가 학습을 촉진한다"는 결과는 **재배치 = 재교육**이라는 논지를 지지한다.

**한계·반박**
- 단일 기업, 고객지원이라는 단일 직무. 외적 타당성 제한.
- 2020–2021년 도입 시기. 모델 세대가 다르다.
- 생산성 향상이 고용으로 어떻게 번역되는지는 이 논문이 다루지 않는다.

#### 5-9. 참고: 대량해고의 장기 상흔(scarring) — 비교 기준선

> Louis S. Jacobson, Robert J. LaLonde, and Daniel G. Sullivan, "Earnings Losses of Displaced Workers," ***American Economic Review***, 1993.
> ⚠️ **권·호·지면(통상 83(4): 685–709)을 이번 리서치에서 직접 확인하지 못했습니다.** OpenAlex·Crossref 모두 미색인. 다만 동일 저자·동일 제목의 W.E. Upjohn Institute Working Paper (1992, DOI [10.17848/wp92-11](https://doi.org/10.17848/wp92-11), OA PDF 존재)는 확인됨.
> 인용 수치는 Bessen et al.(2019)이 verbatim으로 옮긴 것으로 대체 가능:
> "**Jacobson et al. (1993) find that long-tenured workers in Pennsylvania experienced a loss of earnings of 25 percent six years after a mass layoff.**" / "**Jacobson et al. (1993) report an average earnings loss of over 40 percent immediately following the layoff.**"
> 그리고 "**Couch and Placzek (2010) find losses of 13 to 15 percent six years after a mass layoff in another sample**" / "**Couch and Placzek (2010) report an immediate loss of 33 percent.**"
> — Couch & Placzek (2010), "Earnings Losses of Displaced Workers Revisited," *American Economic Review* 100(1): 572–589, DOI [10.1257/aer.100.1.572](https://doi.org/10.1257/aer.100.1.572) **[PR]** (서지 확인 완료)

---

### 6. 챕터 구성 제안 (증거 배치안)

이 자료로 "남는 FTE를 어떻게 할 것인가" 챕터를 다음 순서로 세울 수 있습니다.

1. **공포의 역사적 반복** — Autor(2015)의 1961년 TIME 인용 + 존슨 위원회 "technology eliminates jobs, not work"
2. **그런데 데이터는 마냥 낙관적이지 않다** — Acemoglu & Restrepo(2020) 0.2pp / 40만 개, 로봇 1대 = 3.3명
3. **단, 그건 총량이다. 기업 단위에서는 부호가 뒤집힌다** — Koch et al.(2021) 순 고용 +10%
4. **ATM 신화의 정확한 판본** — Bessen(2015) verbatim 수치 + Autor의 봉인 문장("should not be taken as paradigmatic")
5. **진짜 갈림길: 남긴 사람 vs 내보낸 사람** — Dauth et al.(2021)의 "large gaps between those who manage to stay… and those who are forced to leave"
6. **재배치는 실제로 일어난다 — 조건이 갖춰지면** — Battisti et al.(2023) 재교육을 통한 상향 이동 / Dauth et al. 원 공장 근속 +171일
7. **재배치 vs 해고의 비용 차이** — Bessen et al.: 자동화 이직위험 0.77% vs 대량해고 4%, 1년차 손실 4% vs 33~40%, 사회안전망 상쇄 15%
8. **누가 밀려나는가** — 고령·장기근속자, 조기퇴직 +24% (Bessen et al.) + Battisti et al.의 고령자 예외
9. **왜 고용 안정을 보장해야 하는가** — Ichniowski & Shaw(2003): "employment security guarantees"를 포함한 묶음 6.7%, **개별 도입은 효과 0**
10. **결론: 재배치는 이전이 아니라 창조다** — Acemoglu & Restrepo(2019)의 reinstatement effect: 새 과업을 만들지 않으면 재배치가 아니다

---

### ⚠️ 미확인 항목

아래는 **삭제하지 않고 남겨둔** 항목들입니다. 책 원고에 반영하려면 서지 확인이 필요합니다.

1. **⚠️ 미확인 — 서지 확인 필요** · Levine & Tyson, "Participation, Productivity, and the Firm's Environment," in Alan S. Blinder (ed.), *Paying for Productivity: A Look at the Evidence*, Brookings Institution, 1990 — **수록 지면(통상 pp. 183–243)** 확인 실패. Crossref·OpenAlex 미색인, Google Books API 쿼터 초과. 모 편저서(Blinder 1990, Brookings, ISBN 0815709994)의 존재는 확인. 동명의 *California Management Review* 32(4): 86–100 (DOI 10.2307/41166630)은 확인 완료 — 두 판본을 혼동하지 말 것.

2. **⚠️ 미확인 — 인용문 확인 필요** · "고용 보장이 생산성 개선에 대한 협력을 이끌어낸다"류의 **Levine & Tyson 원문 문장** — 널리 인용되나 원문 대조 실패. **따옴표 인용 금지.** 대체 인용원: Ichniowski & Shaw(2003)의 "employment security guarantees" 문장(본문 4-2(a)).

3. **⚠️ 미확인 — 수치 확인 필요** · Womack, Jones & Roos, *The Machine That Changed the World*(1990)의 **본문 내 구체 수치**(공장별 조립시간, 불량률, 개발 리드타임, NUMMI 사례 수치). 원서 접근 불가. 서지 자체(저자 3인, 1990, Rawson Associates/Macmillan, ISBN 0029463165, 약 323쪽)는 OpenLibrary로 확인.

4. **⚠️ 미확인 — 수치 확인 필요** · MacDuffie(1995) **본문의 생산성·품질 수치**. 초록은 발행처 메타데이터로 verbatim 확보했으나 본문은 폐쇄 접근(SAGE/JSTOR).

5. **⚠️ 미확인 — 수치 확인 필요** · Bessen, *Economic Policy* 34(100), 2019 **본문의 산업별 수요탄력성 추정치 및 고용 전환점 연도**. 초록만 verbatim 확보. BU 리포지토리(scholarship.law.bu.edu) 및 OUP 전문 모두 403 차단.
   - 부수 이슈: BU 리포지토리 "Recommended Citation"의 시작 페이지 **585** vs Crossref/OUP **589** 불일치.
   - 부수 이슈: SSRN 판본(10.2139/ssrn.2935003)의 **BU Law & Economics Research Paper 번호**(통상 17-09로 인용됨) 미확인.

6. **⚠️ 미확인 — 지면 확인 필요** · James Bessen, *Learning by Doing*(Yale UP, 2015)의 **ATM/창구직원 서술이 실린 정확한 장·지면**. 서지(ISBN 9780300195668, 약 310쪽, DOI 10.12987/9780300213645)와 참고문헌/색인 지면(263–286 / 287–296)은 Crossref로 확인. 저자 본인의 동일 내용 요약(IMF *F&D*, 2015-03)으로 대체 인용 권장.

7. **⚠️ 미확인 — 서지 확인 필요** · Jacobson, LaLonde & Sullivan (1993), *American Economic Review* — **권·호·지면(통상 83(4): 685–709)** 미확인. OpenAlex·Crossref 미색인. Upjohn WP 92-11(1992, DOI 10.17848/wp92-11)은 확인.

8. **⚠️ 미확인 — 발행 정보 확인 필요** · Appelbaum, Bailey, Berg & Kalleberg, *Manufacturing Advantage*의 **발행 연도(2000)와 임프린트(ILR Press)**. Cornell UP 페이지에서 서명·저자·발행처·ISBN(9780801437656)은 확인, 연도·쪽수는 미확인. 서평 3편(2001년)으로 간접 정합.

9. **⚠️ 미확인 — 본문 확인 필요** · Battisti, Dustmann & Schönberg(2023) **본문의 구체 수치**(재교육 참여율, 직무 상향 이동률, 고령자 이탈 위험 크기). 초록만 verbatim. OA PDF 확보 경로 존재: https://eprints.gla.ac.uk/293212/2/293212.pdf

10. **⚠️ 미확인 — 본문 확인 필요** · Guarascio, Piccirillo et al., "Robots vs. Workers: Evidence From a Meta-Analysis," *Journal of Economic Surveys*(2025), DOI 10.1111/joes.12699 — **존재는 검색 결과로 확인, 저자 전원·권호·지면·메타분석 결론 수치는 미확인.** Acemoglu-Restrepo에 대한 가장 중요한 최신 반론 후보이므로 추가 확인 권장.

11. **⚠️ 기호 복원 주의** · Acemoglu & Restrepo(2020)의 표준오차 인용문 — PDF 텍스트 레이어에서 마이너스(−)와 등호(=)가 각각 `2`, `5`로 깨져 추출됨(`20.39`, `5 0:09`). 본문 4-1(c)에서 복원했으나, 조판 원문(par.nsf.gov PDF 또는 JPE) 재대조 권장.

12. **⚠️ 미확인** · Autor(2015)가 인용한 **2010년 이후 미국 은행 창구직원 고용 추이(BLS OES/CES)**. ATM 사례를 2026년 시점에 쓰려면 "그 후 어떻게 되었는가"가 필요한데, 이번 리서치 범위 밖.

13. **⚠️ NBER 메타데이터 오류(확인됨)** · NBER WP 5333 페이지의 published-version 표기가 "American Economic Review, Vol. **86** (June 1997): 291-313" — **Vol. 87이 정확**(OpenAlex/JSTOR 2951347 기준). NBER 페이지를 그대로 인용하지 말 것.

14. **⚠️ 접근 실패 기록** · Ichniowski, Shaw & Prennushi(1997) AER **게재본 전문**은 확보 실패(JSTOR 폐쇄, NBER WP 5333 PDF는 텍스트 레이어가 미러링 OCR로 판독 불가). 6.7% 등 핵심 수치는 **저자 본인들이 JEP 2003에서 verbatim 재보고한 것**으로 대체 인용했으며, 이 방식이 서지적으로 안전합니다.

---

#### 리서치 로그 (재현용)
확보한 원문 텍스트 파일은 `/private/tmp/claude-1219186993/-Users-1112022-source-github-book-writer/dc570957-917d-436c-849d-9b90c31835d4/scratchpad/` 에 있습니다:
`ar_robots.txt`(A&R JPE 게재본), `alm2003.txt`(ALM QJE), `autor2015.txt`(Autor JEP), `autordorn2013.txt`(A&D AER), `dauth.txt`(JEEA), `bgsv.txt`(CPB DP 390), `jep2003.txt`(Ichniowski & Shaw JEP).

**주의:** PDF WebFetch가 "organization policy"/"copyright" 사유로 거부를 반환한 경우가 5건 있었으나, 모두 공개 학술 문헌에 대한 오탐이었습니다. 해당 PDF는 로컬에 저장되므로 `pdftotext -layout`로 정상 추출했습니다.

---

## B-5. AI와 총요소생산성(TFP) — 최신 거시 추정치 (2024–2026)

> 검색·확인 시점: **2026-09-05**. 아래 모든 서지·수치는 원문 PDF 또는 출판사·기관 페이지를 실제로 열어 확인한 것이다. 확인하지 못한 항목은 맨 끝 `⚠️ 미확인 항목`에 별도로 남겼다.

---

### 0. 이 토픽의 지형 한눈에

같은 기술, 같은 10년, 같은 데이터 소스(Eloundou et al., Svanberg et al., Noy–Zhang, Brynjolfsson et al., Peng et al.)를 쓰는데 **연간 TFP 기여 추정치가 0.064pp에서 1.5pp까지 약 20배 벌어진다.** 이 격차는 데이터가 아니라 **가정**에서 나온다. 그리고 놀랍게도 그 가정들은 대부분 **명시적으로 문서화되어 있어서 하나씩 추적이 가능하다.** 특히 Aghion & Bunel(2024)은 Acemoglu의 **수식을 그대로 쓰면서 파라미터만 바꿔** 10배 큰 값을 얻는다 — 이 책의 5장·6장 어디에 쓰든, "숫자 싸움이 아니라 가정 싸움"이라는 논지의 결정적 증거다.

---

## 1. 축이 되는 논문: Acemoglu

### 1-1. Daron Acemoglu, "The Simple Macroeconomics of AI" — NBER Working Paper 32487

**서지 (WP 버전)**
- Acemoglu, Daron. "The Simple Macroeconomics of AI." *NBER Working Paper* No. 32487, National Bureau of Economic Research, Cambridge, MA, **May 2024**.
- DOI: `10.3386/w32487` / URL: https://www.nber.org/papers/w32487
- PDF: https://www.nber.org/system/files/working_papers/w32487/w32487.pdf
- JEL: E24, J24, O30, O33
- 태그: **[WP]** (NBER 표지에 명시: "They have not been peer-reviewed…")

**서지 (게재 버전)**
- Acemoglu, Daron. "The simple macroeconomics of AI." *Economic Policy*, Vol. **40**, Issue **121**, January 2025, pp. **13–58**.
- DOI: `10.1093/epolic/eiae042` / URL: https://academic.oup.com/economicpolicy/article-abstract/40/121/13/7728473
- 온라인 선공개: **2024-08-06**, 지면: **2025-01** (2025-01)
- 태그: **[PR]**

**서지 (선행 초고 — 수치가 다름, 반드시 구별할 것)**
- Acemoglu, Daron. "The Simple Macroeconomics of AI." MIT Economics, **April 5, 2024** draft.
- URL: https://economics.mit.edu/sites/default/files/2024-04/The%20Simple%20Macroeconomics%20of%20AI.pdf
- 태그: **[WP]**

#### 핵심 주장

AI의 미시적 효과가 **과업 수준의 비용 절감**으로 나타나는 한, 거시 효과는 **Hulten 정리의 한 변형**으로 결정된다. 즉 `총요소생산성 증가 = (AI가 영향을 미치는 과업의 GDP 비중) × (그 과업들의 평균 비용 절감률)`. 이 항등식이 모든 낙관적 예측에 규율(discipline)을 부과한다. 기존 실증치를 대입하면 10년간 TFP 증가는 **최대 0.66%**, 학습난도를 반영하면 **0.53% 미만**이다.

#### 이 책에 쓸 수 있는 부분

- **"AX는 결국 과업 단위의 산술"**이라는 프레임. 경영진이 "AI로 생산성 10배"를 말할 때, Hulten 항등식은 "그 10배가 전체 원가의 몇 %를 차지하는 과업에 적용되는가"를 되묻게 한다. 한국 기업의 AX 과제 우선순위 선정 논리로 직결된다.
- **"쉬운 과업 / 어려운 과업" 구분**. AX 파일럿이 늘 성공하고 전사 확산에서 실패하는 이유를 설명하는 가장 깔끔한 경제학적 언어다.
- **도입률이 병목이라는 지적** — 2019년 미국 기업 중 AI 투자 기업이 1.5% 미만이었다는 수치는 "기술 성숙 ≠ 조직 도입"의 근거.
- **GDP와 후생의 괴리** — "AI가 GDP를 2% 올리면서 후생을 −0.72% 낮출 수 있다"는 계산은 AX의 목적함수 설정 챕터에서 쓸 만하다.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 초록 — NBER/게재 버전 (0.66% / 0.53%)**

> "Using existing estimates on exposure to AI and productivity improvements at the task level, these macroeconomic effects appear nontrivial but modest—no more than a 0.66% increase in total factor productivity (TFP) over 10 years."
>
> 기존의 AI 노출도 추정치와 과업 수준 생산성 향상치를 사용하면, 이 거시적 효과는 사소하지는 않지만 완만하다 — 10년간 총요소생산성(TFP) 증가분이 **0.66%를 넘지 않는다.**

> "The paper then argues that even these estimates could be exaggerated, because early evidence is from easy-to-learn tasks, whereas some of the future effects will come from hard-to-learn tasks, where there are many context-dependent factors affecting decision-making and no objective outcome measures from which to learn successful performance. Consequently, predicted TFP gains over the next 10 years are even more modest and are predicted to be less than 0.53%."
>
> 이 논문은 나아가 이 추정치조차 과장일 수 있다고 주장한다. 초기 증거가 **배우기 쉬운 과업(easy-to-learn tasks)**에서 나온 반면, 미래 효과의 일부는 **배우기 어려운 과업(hard-to-learn tasks)** — 의사결정에 영향을 주는 맥락 의존적 요인이 많고 성공적 수행을 학습할 객관적 성과 지표가 없는 과업 — 에서 나올 것이기 때문이다. 따라서 향후 10년간 예측되는 TFP 증가분은 더욱 완만하여 **0.53% 미만**으로 예측된다.

**(b) 계산의 4단계 — 각 파라미터 (NBER/게재 버전)**

> "This calculation implies that 20% of US labor tasks are exposed to AI. I then use Svanberg et al.'s estimate for computer vision tasks that, among all exposed tasks, 23% can be profitably performed by AI (for the rest, the authors estimate that the costs would exceed the benefits). I take the average labor cost savings to be 27%—the average of the estimates in Noy and Zhang (2023) and Brynjolfsson et al. (2023)—and turn this into overall cost savings using industry labor shares, which imply average overall cost savings of 14.4%."
>
> 이 계산은 **미국 노동 과업의 20%가 AI에 노출**되어 있음을 의미한다. 다음으로 Svanberg et al.의 컴퓨터 비전 과업 추정치를 사용한다 — 노출된 전체 과업 중 **23%가 AI로 수익성 있게 수행될 수 있다**(나머지는 비용이 편익을 초과한다고 저자들은 추정한다). **평균 노동비용 절감률은 27%**로 잡는데, 이는 Noy & Zhang(2023)과 Brynjolfsson et al.(2023) 추정치의 평균이며, 이를 산업별 노동소득분배율로 전환하면 **평균 총비용 절감률 14.4%**가 된다.

> "This calculation implies that total factor productivity (TFP) effects within the next 10 years should be no more than 0.66% in total—or approximately a 0.064% increase in TFP growth annually."
>
> 이 계산은 향후 10년간 총요소생산성(TFP) 효과가 총 **0.66%를 넘지 않으며 — 연간 TFP 성장률로는 약 0.064%p 증가**임을 의미한다.

**(c) 노출 과업의 GDP 비중 산출 — 4.6%**

> "Svanberg et al.'s base estimates imply that among computer vision-exposed tasks, 23% can be feasibly (and profitably) automated within 10 years. Applying this number to Eloundou et al.'s estimates, I arrive at the GDP share of tasks impacted by AI over the next 10 years as 0.23 × 0.200 = 4.6% of all tasks (or occupations)."
>
> Svanberg et al.의 기본 추정치는 컴퓨터 비전 노출 과업 중 **23%가 10년 내에 실현 가능하고 (수익성 있게) 자동화될 수 있음**을 의미한다. 이 수치를 Eloundou et al.의 추정치에 적용하면, 향후 10년간 AI의 영향을 받는 과업의 GDP 비중은 **0.23 × 0.200 = 전체 과업(또는 직업)의 4.6%**가 된다.

**(d) 최종 산식**

> "TFP gains over the next 10 years = 0.046 × 0.144 = 0.0066."
>
> 향후 10년간 TFP 증가 = 0.046 × 0.144 = **0.0066** (=0.66%).

> "In other words, according to this basic estimation strategy, TFP gains over the next 10 years from AI are about 0.66%—meaning that relative to the baseline without the current suite of AI and computer vision advances, TFP will be higher by 0.66 percentage points in 10 years."
>
> 다시 말해, 이 기본 추정 전략에 따르면 AI로 인한 향후 10년간 TFP 증가는 약 **0.66%** — 현재의 AI·컴퓨터 비전 진보가 없는 기준선 대비 10년 후 TFP가 **0.66%p 높아진다**는 뜻이다.

**(e) 상한 시나리오 (Peng et al. 포함 / GPU 비용 급락)**

> "If we were to consider the higher productivity numbers from Peng et al., 0.144 would be replaced by 0.193, and the 10-year TFP gains would be 0.89%, instead of 0.66%."
>
> Peng et al.의 더 높은 생산성 수치를 고려하면 0.144가 **0.193**으로 대체되고, 10년 TFP 증가는 0.66%가 아니라 **0.89%**가 된다.

> "For example, in Svanberg et al.'s scenarios where costs for computer vision decline very rapidly, such as 10% a year, the fraction of tasks that are feasibly automated may be as high as 30%. This would raise the GDP share impacted by AI to approximately 6%, and correspondingly increase the TFP gains over the next 10 years to about 0.9%."
>
> 예컨대 Svanberg et al.의 시나리오 중 컴퓨터 비전 비용이 **연 10%**처럼 매우 빠르게 하락하는 경우, 실현 가능하게 자동화되는 과업 비중은 **30%까지** 올라갈 수 있다. 이는 AI 영향 GDP 비중을 약 **6%**로 높이고, 그에 따라 10년 TFP 증가를 약 **0.9%**로 끌어올린다.

**(f) hard/easy 조정 — 73% 쉬운 과업**

> "Using a range of (speculative) assumptions, I estimate an upper bound of 73% easy tasks among Eloundou et al.'s exposed tasks. I suppose that productivity gains in hard tasks will be approximately one quarter of the easy ones. This leads to an updated, more modest increase in TFP and GDP in the next 10 years that can be upper bounded by 0.53% and 0.90%, respectively."
>
> 일련의 (사변적인) 가정을 사용하여, Eloundou et al.의 노출 과업 중 **쉬운 과업의 상한을 73%**로 추정한다. 어려운 과업에서의 생산성 향상은 쉬운 과업의 **약 4분의 1**이라고 가정한다. 이는 향후 10년간 TFP와 GDP의 증가분을 각각 **0.53%와 0.90%**로 상한지을 수 있는, 갱신된 더 완만한 값으로 이어진다.

> "TFP gains over the next 10 years = 0.033 × 0.144 + (0.046 − 0.033) × 0.037"
>
> (쉬운 노출 과업 GDP 비중 3.3% × 총비용 절감 14.4%) + (어려운 노출 과업 1.3% × 총비용 절감 3.7%)

**(g) 어려운 과업의 7% 절감률이 나온 근거 — 이 대목이 논쟁의 진앙이다**

> "Here I take those productivity gains to be 7%. My reasoning is as follows. I consider the tasks involved in the Peng et al. (2023) study to be very easy for generative AI for reasons explained above. Those studied in Noy and Zhang (2023) are also on the easy side, and led to cost savings of about 40%, which is about two thirds of the cost savings in Peng et al., while the customer service tasks in Brynjolfsson et al. (2023) are already moving towards somewhat more complex tasks, and these had cost savings of only 14%. […] This motivates my choice of half of the cost savings of their study, 7% (which is also about a quarter of the baseline 27% cost reduction estimate I used in the previous subsection)."
>
> 여기서 나는 그 생산성 향상을 **7%**로 잡는다. 근거는 다음과 같다. Peng et al.(2023) 연구의 과업들은 생성형 AI에게 매우 쉽다고 본다. Noy & Zhang(2023)의 과업도 쉬운 축이며 **약 40%의 비용 절감**을 낳았는데, 이는 Peng et al. 비용 절감의 약 3분의 2다. 반면 Brynjolfsson et al.(2023)의 고객 서비스 과업은 이미 다소 복잡한 쪽으로 이동해 있으며, **비용 절감이 14%에 불과**했다. […] 이것이 그 연구 비용 절감의 **절반인 7%**를 내가 택한 이유다 (이는 앞 절에서 쓴 기준선 27% 절감 추정치의 약 4분의 1이기도 하다).

**(h) TFP → GDP 전환**

> "Using the capital share for the entire private business sector, 0.43, this implies that GDP gains will be equal to the TFP gains multiplied by 1.75 (≃ 1/(1 − 0.43)). Hence taking the baseline estimate of an increase in TFP of 0.66%, I obtain a first estimate for GDP growth due to AI of 1.16% over 10 years, or taking the presence of hard tasks into account, a lower estimate of 0.93%."
>
> 민간기업 부문 전체의 **자본소득분배율 0.43**을 사용하면, GDP 증가는 TFP 증가의 **1.75배**가 된다. 따라서 TFP 0.66% 증가라는 기준 추정치를 취하면 AI로 인한 10년 GDP 성장 추정치는 **1.16%**, 어려운 과업의 존재를 감안하면 더 낮은 **0.93%**를 얻는다.

**(i) 결론부 종합 — 이 문단 하나면 인용으로 충분하다**

> "Taking these considerations into account, I estimate that TFP effects from AI advances within the next 10 years will be modest—an upper bound that does not take into account the distinction between hard and easy tasks would be about a 0.66% increase in total within 10 years, or about a 0.064% increase in annual TFP growth. When the presence of hard tasks among those that will be exposed to AI is recognized, this upper bound drops to about 0.53%. GDP effects will be somewhat larger than this because automation and task complementarities will also lead to greater investment. But my calculations suggest that the GDP boost within the next 10 years should also be modest, in the range of 0.93% − 1.16% over 10 years in total, provided that the investment increase resulting from AI is modest, and in the range of 1.4% − 1.56% in total, if there is a large investment boom."
>
> 이러한 고려를 감안하여, 나는 향후 10년간 AI 진보의 TFP 효과가 완만할 것으로 추정한다 — 어려운 과업과 쉬운 과업의 구분을 감안하지 않은 상한은 10년간 총 **약 0.66% 증가**, 즉 **연간 TFP 성장률 약 0.064%p 증가**다. AI에 노출될 과업 중 어려운 과업의 존재를 인정하면 이 상한은 **약 0.53%**로 떨어진다. GDP 효과는 자동화와 과업 보완성이 더 큰 투자를 유발하므로 이보다 다소 클 것이다. 그러나 내 계산은 향후 10년간 GDP 증가 역시 완만할 것임을 시사한다 — AI로 인한 투자 증가가 완만하다면 10년간 총 **0.93%~1.16%** 범위, 대규모 투자 붐이 있다면 총 **1.4%~1.56%** 범위다.

**(j) "사소하지 않다"는 자기 방어 — 균형 잡힌 인용을 위해 반드시 함께**

> "These results should not be interpreted as arguing that there are no major benefits from AI. First, an increase of about 0.53 − 0.66% in TFP within 10 years is modest but still far from trivial."
>
> 이 결과가 AI에 큰 편익이 없다는 주장으로 해석되어서는 안 된다. 첫째, 10년 내 TFP **0.53~0.66% 증가**는 완만하지만 결코 사소하지 않다.

**(k) 도입률 병목 — AX 실무에 가장 직접적인 문장**

> "These adoption numbers ignore the fact that there is still very little investment in AI in the US corporate sector. Acemoglu et al. (2022) estimate that less than 1.5% of US businesses had any investment in AI in 2019 […] These considerations suggest that even the 0.046% number for the share of GDP impacted by AI may be a big overestimate, and the true numbers could be much smaller."
>
> 이 도입률 수치는 미국 기업 부문에 여전히 AI 투자가 매우 적다는 사실을 무시하고 있다. Acemoglu et al.(2022)은 **2019년 미국 기업 중 AI에 조금이라도 투자한 곳이 1.5% 미만**이었다고 추정한다. […] 이런 고려는 AI 영향 GDP 비중 0.046이라는 수치조차 큰 과대추정일 수 있으며, 실제 수치는 훨씬 작을 수 있음을 시사한다.
>
> *(주: 원문 표기 "0.046%"는 0.046(=4.6%)의 오식으로 보이나 **원문 그대로** 옮겼다.)*

**(l) J-커브 — 10년이라는 시계(視界) 자체를 의심하는 대목**

> "In the context of digital technologies, Greenwood and Yorukoglu (1997) and Brynjolfsson et al. (2021), among others, have argued that productivity gains will take a J-shaped pattern, and the former paper predicts that the flat part of the J-curve lasts no less than 20 years for digital technologies. If so, the 14.4% overall cost reductions may be a significant overestimate for the next 10 years."
>
> 디지털 기술의 맥락에서 Greenwood & Yorukoglu(1997)와 Brynjolfsson et al.(2021) 등은 생산성 이득이 **J자 패턴**을 띨 것이라 주장해 왔으며, 전자는 디지털 기술의 경우 **J커브의 평탄 구간이 최소 20년** 지속된다고 예측한다. 그렇다면 14.4%라는 총비용 절감은 향후 10년에 대해 상당한 과대추정일 수 있다.

**(m) "나쁜 새 과업" — GDP와 후생의 분리**

> "For example, AI may appear to increase GDP by 2%, while in reality reducing welfare by −0.72%."
>
> 예컨대 AI는 **GDP를 2% 올리는 것처럼 보이면서 실제로는 후생을 −0.72% 낮출** 수 있다.

> "Roughly speaking, their estimates imply that revenue can increase by about $53 per user-month, but this has a negative impact on total GDP/welfare equivalent to $19 per user-month."
>
> 대략 말해, 이들의 추정치는 **사용자·월당 약 53달러의 수입 증가**가 가능하지만, 이것이 **사용자·월당 19달러에 해당하는** 총 GDP/후생의 **음의 효과**를 갖는다는 뜻이다.

#### ⭐ NBER WP와 게재본 사이의 개정 (질문 사항 — 정밀 확인 완료)

**게재 버전(Economic Policy 2025)의 초록 수치는 NBER WP(2024-05)와 동일한 0.66% / 0.53%다.** 개정은 그 이전, **MIT 2024-04-05 초고 → NBER 2024-05 WP** 사이에 있었다. 파라미터 변화는 다음과 같다:

| 파라미터 | MIT 2024-04-05 초고 | NBER 2024-05 = Economic Policy 2025 |
|---|---|---|
| 노출 과업의 GDP 비중 | **19.9%** | **20%** (0.200) |
| 수익성 있게 자동화 가능한 비중 (Svanberg) | 23% | 23% (동일) |
| 영향받는 과업의 GDP 비중 | 0.23 × 0.199 = **4.6%** | 0.23 × 0.200 = **4.6%** |
| 평균 노동비용 절감률 | 27% | 27% (동일) |
| **AI 노출 조정 노동소득분배율** | **0.57** | **0.535** |
| 평균 총비용 절감률 | 0.27 × 0.57 = **15.4%** | 0.27 × 0.535 = **14.4%** |
| **10년 TFP (기준)** | **0.71%** (연 0.07%p) | **0.66%** (연 0.064%p) |
| Peng 포함 시 총비용 절감 / 10년 TFP | 0.205 / **0.94%** | 0.193 / **0.89%** |
| GPU 급락 시나리오 10년 TFP | 약 **1%** | 약 **0.9%** |
| 쉬운 과업 비중 | **74%** | **73%** |
| 어려운 과업 총비용 절감률 | 0.040 | 0.037 |
| **hard 조정 10년 TFP** | **0.55%** | **0.53%** |
| **자본소득분배율** | **0.40** (×1.66) | **0.43** (×1.75) |
| 10년 GDP (기준 / hard 조정) | **1.1% / 0.92%** | **1.16% / 0.93%** |
| 대규모 투자 붐 시 10년 GDP | **1.6–1.8%** | **1.4–1.56%** |

> **핵심:** 하향 개정(0.71→0.66, 0.55→0.53)의 **거의 전부**가 **노동소득분배율 0.57 → 0.535** 한 줄에서 나온다. 자본소득분배율은 0.40→0.43으로 올라가 GDP 승수가 1.66→1.75로 커졌기 때문에 GDP 수치는 오히려 소폭 상승(1.1→1.16)했다. 노출 과업 비중(19.9→20.0)과 쉬운 과업 비중(74→73)은 사실상 반올림 수준의 재계산이다.
>
> **이 사실 자체가 인용거리다.** 세계 최고 수준의 거시경제학자가 낸 "AI 생산성 효과" 대표 추정치의 개정폭 대부분이, AI와 아무 상관없는 **국민계정의 노동소득분배율 소수점 셋째 자리**에서 나왔다. 추정치의 견고함이 어디에 달려 있는지를 보여준다.

**질문에서 언급된 "~0.9% GDP" 수치의 정체:** 이는 GDP 기준선(1.16%)이 아니라 **hard-task 조정 GDP 상한 0.90%**(초록 표현) 또는 본문의 **0.93%**다. 초록은 "upper bounded by 0.53% and 0.90%, respectively"라 쓰고, 본문 §3.4는 "a lower estimate of 0.93%"라 쓴다. **두 수치가 원문 안에서 공존하므로 인용 시 어느 쪽인지 밝힐 것.**

#### 한계·반박

1. **Hulten 정리의 적용 조건.** Hulten 정리는 1차 근사(first-order approximation)로서, 효율적 배분·미세한 충격·**신규 과업/신제품 없음**을 전제한다. Acemoglu 본인도 신규 과업 효과를 "계산에서 빼두었다"고 명시한다. AI가 대규모 신규 과업·신제품을 만들면 이 항등식은 하한이 된다.
2. **10년이라는 자의적 시계.** GPT 확산 지체를 강조하면서 정작 추정 지평은 10년으로 고정한다. J커브 평탄 구간이 20년이라면 10년 추정은 "아직 아무 일도 안 일어난 구간"을 재는 셈이다 — 반대로 20년 이후를 재면 값이 커진다.
3. **Svanberg et al.의 23%를 생성형 AI 전반에 외삽.** 저자 스스로 "This is not a trivial step"이라며 인정한다. Aghion & Bunel이 정확히 이 지점을 공격한다.
4. **비용 하락을 0으로 가정.** 23%를 고정한다는 것은 향후 10년간 AI 비용 절감 진보가 없다고 가정하는 것과 같다 (Aghion & Bunel의 지적).
5. **자본심화(capital deepening) 경로 축소.** TFP만이 후생 관련 지표라고 주장하지만, 실제 AI 투자 붐은 자본심화를 통해 노동생산성을 올린다.

---

### 1-2. 게재본에 함께 실린 공식 논평 (직접 반박 2건)

**Benoît Cœuré discussion of: The simple macroeconomics of AI**
- *Economic Policy*, Vol. 40, Issue 121, pp. **59–64**, 2025-01. DOI: `10.1093/epolic/eiae055`. **[PR]**
- 골자: Acemoglu의 프레임워크가 "AI가 경제에 영향을 미치는 경로를 서술하는 일관된 거시 프레임워크"로서 훌륭하다고 평가하되, AI를 **점진적 변화로 취급하는 보수적 접근**이라는 점을 지적. 노동시장 분석 중 **AI가 저학력 여성 노동자에게 상대적으로 큰 영향**을 준다는 결과가 과거 자동화(제조업·저학력 남성 중심)와 대비되어 주목할 만하다고 평가.

**David Hémous discussion of: The simple macroeconomics of AI**
- *Economic Policy*, Vol. 40, Issue 121, pp. **65–69**, 2025-01-27. DOI: `10.1093/epolic/eiae061`. **[PR]**
- 확인된 인용:
> "Acemoglu (2025) provides a methodology to compute back-of-the-envelope estimates of AI's impact on TFP, output and welfare over a medium-term horizon (10 years)."
>
> Acemoglu(2025)는 중기(10년) 시계에서 AI가 TFP·산출·후생에 미치는 영향을 **개략적으로(back-of-the-envelope) 추정하는 방법론**을 제공한다.

---

## 2. 반박 / 더 높은 추정치들

### 2-1. Goldman Sachs — Briggs & Kodnani (2023-03)

**서지**
- Briggs, Joseph, and Devesh Kodnani. "The Potentially Large Effects of Artificial Intelligence on Economic Growth." *Global Economics Analyst*, Goldman Sachs Global Investment Research, **26 March 2023, 9:05PM EDT**. (표지에 Jan Hatzius, Giovanni Pierdomenico도 연락처로 병기)
- 공개 사본: https://archive.org/details/the-potentially-large-effects-of-ai-goldman-sachs
- 태그: **[WP]** (투자은행 리서치 노트, 비심사)

#### 핵심 주장
직업별 O*NET 과업 데이터로 노출도를 계산한 뒤, ① 대체된 노동의 비용 절감 ② 비대체 노동자의 생산성 향상 ③ 실직자 재고용의 구성효과를 합산해 **미국 노동생산성 증가율이 연 약 1.5%p 상승**, 이를 전 세계로 외삽해 **연간 세계 GDP 7%(≈7조 달러) 증가**를 얻는다.

#### 인용 가능한 문장·수치 (VERBATIM — 사용자 추정 "7%/1.5%" 정밀 확인 결과)

> "We estimate that generative AI could raise annual US labor productivity growth by just under 1½pp over a 10-year period following widespread adoption, although the boost to labor productivity growth could be much smaller or larger depending on the difficulty level of tasks AI will be able to perform and how many jobs are ultimately automated."
>
> 우리는 생성형 AI가 **광범위한 도입 이후 10년에 걸쳐 미국의 연간 노동생산성 증가율을 1.5%p 바로 아래만큼** 끌어올릴 수 있다고 추정한다. 다만 노동생산성 증가 폭은 AI가 수행할 수 있는 과업의 난도와 궁극적으로 몇 개의 일자리가 자동화되는지에 따라 훨씬 작거나 클 수 있다.

> "The boost to global labor productivity could also be economically significant, and we estimate that AI could eventually increase annual global GDP by 7%."
>
> 세계 노동생산성 상승 역시 경제적으로 유의미할 수 있으며, 우리는 AI가 **궁극적으로 연간 세계 GDP를 7% 증가**시킬 수 있다고 추정한다.

> "Applying our estimated global labor productivity boost to countries in our coverage implies that widespread AI adoption could eventually drive a 7% or almost $7tn increase in annual global GDP over a 10-year period."
>
> 추정된 세계 노동생산성 상승분을 커버리지 국가들에 적용하면, 광범위한 AI 도입이 궁극적으로 **10년에 걸쳐 연간 세계 GDP를 7%, 거의 7조 달러 증가**시킬 수 있음을 의미한다.

> "Under these assumptions we estimate that widespread adoption of generative AI could raise overall labor productivity growth by around 1.5pp/year (vs. a recent 1.5% average growth pace), roughly the same-sized boost that followed the emergence of prior transformative technologies like the electric motor and personal computer."
>
> 이 가정 하에서 우리는 생성형 AI의 광범위한 도입이 **전체 노동생산성 증가율을 연 약 1.5%p** 높일 수 있다고 추정한다(최근 평균 증가 속도 1.5%와 대비). 이는 **전기 모터와 개인용 컴퓨터** 같은 이전의 변혁적 기술 등장 이후 뒤따랐던 상승과 대략 같은 크기다.

**노출도 (Acemoglu의 19.9~20%와 정면 대비)**

> "Using data on occupational tasks in both the US and Europe, we find that roughly two-thirds of current jobs are exposed to some degree of AI automation, and that generative AI could substitute up to one-fourth of current work. Extrapolating our estimates globally suggests that generative AI could expose the equivalent of 300mn full-time jobs to automation."
>
> 미국과 유럽의 직업별 과업 데이터를 사용하여, 우리는 **현재 일자리의 약 3분의 2가 어느 정도 AI 자동화에 노출**되어 있으며, **생성형 AI가 현재 업무의 최대 4분의 1을 대체**할 수 있음을 발견한다. 이 추정치를 전 세계로 외삽하면 생성형 AI가 **정규직 3억 명에 해당하는 일자리**를 자동화에 노출시킬 수 있음을 시사한다.

> "we estimate that one-fourth of current work tasks could be automated by AI in the US (Exhibit 5, top panel), with particularly high exposures in administrative (46%) and legal (44%) professions and low exposures in physically-intensive professions such as construction (6%) and maintenance (4%)."
>
> 우리는 미국에서 **현재 업무 과업의 4분의 1이 AI로 자동화될 수 있다**고 추정하며, 특히 **행정직(46%)과 법률직(44%)**에서 노출도가 높고 **건설(6%)·유지보수(4%)** 같은 물리적 집약 직종에서는 낮다.

> "Our estimates intuitively suggest that fewer jobs in EMs are exposed to automation than in DMs, but that 18% of work globally could be automated by AI on an employment-weighted basis (Exhibit 6)."
>
> 우리 추정치는 신흥시장(EM)이 선진시장(DM)보다 자동화에 노출된 일자리가 적음을 직관적으로 시사하지만, **고용가중 기준으로 전 세계 업무의 18%가 AI로 자동화**될 수 있음을 보여준다.

**시나리오 폭 — 시계(視界) 가정의 민감도**

> "Exhibit 13 therefore also considers other plausible scenarios and shows that the boost to US productivity growth could easily range from 0.3-3.0pp depending on the difficulty level of tasks generative AI can perform, how many jobs are ultimately automated, and the speed of adoption"
>
> 따라서 Exhibit 13은 다른 그럴듯한 시나리오도 고려하며, 미국 생산성 증가 상승분이 생성형 AI가 수행 가능한 과업의 난도, 궁극적으로 자동화되는 일자리 수, **도입 속도**에 따라 **0.3~3.0%p 범위**에 쉽게 걸칠 수 있음을 보여준다.

> "In a much less powerful AI scenario where, for example, generative AI is only ultimately able to 'skim a short article to gather the main point' (difficulty score 2) rather than 'determine the interest cost to finance a new building' (difficulty score 4), the implied labor productivity growth boost would fall to 0.3pp/year. If AI is instead more powerful and is able to, again for example, 'analyze the cost of medical care services for all US hospitals' (difficulty score 6), the implied labor productivity growth boost would rise to 2.9pp/year."
>
> 훨씬 덜 강력한 AI 시나리오, 예컨대 생성형 AI가 "새 건물 금융의 이자 비용을 산정"(난도 4) 대신 "짧은 기사를 훑어 요점 파악"(난도 2)만 궁극적으로 가능한 경우, 함의되는 노동생산성 증가 상승분은 **연 0.3%p**로 떨어진다. 반대로 AI가 더 강력해 "미국 전체 병원의 의료 서비스 비용 분석"(난도 6)이 가능하다면 **연 2.9%p**로 올라간다.

> "Third, we vary the timeline of adoption. The productivity growth boost would only be roughly half as large if the gains are realized over a 20-year period and one-third as large if realized over a 30-year period."
>
> 셋째, 도입 시점을 달리한다. 이득이 **20년에 걸쳐 실현되면 생산성 증가 상승분은 대략 절반**, **30년이면 3분의 1**에 그친다.

> "Our estimates imply that AI adoption could boost global annual productivity growth for countries in our coverage by 1.4pp (FX-weighted average) over a 10-year period, although we would likely expect a more delayed impact in EM economies."
>
> 우리 추정치는 AI 도입이 커버리지 국가의 **연간 세계 생산성 증가율을 10년에 걸쳐 1.4%p(환율가중 평균)** 높일 수 있음을 의미한다. 다만 신흥국에서는 더 지연된 영향을 예상한다.

#### 한계·반박
- **비심사 투자은행 리서치.** GS 스스로 "we are not incorporating our findings into our baseline economic forecasts at this time"(현재 이 결과를 기준 경제 전망에 반영하고 있지 않다)라고 명시한다 — **낙관 추정치를 인용할 때 반드시 병기해야 할 문장이다.**
- 노출도 산정에서 "AI가 O*NET 난도 4까지 수행 가능"이라는 **가정**을 base case로 놓았을 뿐, 검증된 값이 아니다.
- 자동화 가능성(technical exposure)을 **수익성 필터 없이** 그대로 생산성 이득으로 환산한다. Acemoglu의 23% 필터(=수익성 검증)에 해당하는 단계가 없다.
- 광범위한 도입 **이후** 10년이라는 조건부 서술 — "언제 그 시점이 오는가"는 추정하지 않는다.

---

### 2-2. Baily, Brynjolfsson & Korinek — Brookings (2023-05)

**서지**
- Baily, Martin Neil, Erik Brynjolfsson, and Anton Korinek. "Machines of mind: The case for an AI-powered productivity boom." *Brookings Institution* commentary, **May 10, 2023**.
- URL: https://www.brookings.edu/articles/machines-of-mind-the-case-for-an-ai-powered-productivity-boom/
- 태그: **[WP]** (싱크탱크 논평, 비심사)

#### 핵심 주장
생성형 AI는 **인지노동(cognitive work)** 자체를 값싸게 만드는 기술이며, 두 경로로 작동한다. ① **현재 산출**의 생산성 향상 ② **아이디어 생산**의 가속 — 후자는 성장률 자체를 항구적으로 끌어올린다. 다만 **생산성 J커브** 때문에 효과는 지연된다.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 총량 산술 — Hulten식 계산의 낙관 버전**

> "If generative AI makes cognitive workers on average 30% more productive over a decade or two and cognitive work makes up about 60% of all value added in the economy (as measured by the wage bill attributable to cognitive tasks), this amounts to a 18% increase in aggregate productivity and output, spread out over those years."
>
> 생성형 AI가 10~20년에 걸쳐 인지노동자를 평균 **30% 더 생산적**으로 만들고, 인지노동이 경제 전체 부가가치의 **약 60%**를 차지한다면(인지 과업에 귀속되는 임금총액 기준), 이는 그 기간에 분산된 **총생산성 및 산출의 18% 증가**에 해당한다.

**(b) 두 번째 경로 — 아이디어 생산의 자동화 (Acemoglu가 명시적으로 계산에서 뺀 부분)**

> "Cognitive workers not only produce current output but also invent new things, engage in discoveries, and generate the technological progress that boosts future productivity."
>
> 인지노동자는 현재 산출을 생산할 뿐 아니라 **새로운 것을 발명하고, 발견에 참여하며, 미래 생산성을 높이는 기술 진보를 만들어낸다.**

> "If productivity growth was 2% and the cognitive labor that underpins productivity growth is 20% more productive, this would raise the growth rate of productivity by 20% to 2.4%."
>
> 생산성 증가율이 2%였고 그 증가를 뒷받침하는 인지노동이 **20% 더 생산적**이 되면, 이는 생산성 증가율을 20% 높여 **2.4%**로 만든다.

**(c) 확산 지연 — J커브 (낙관론자가 스스로 인정하는 단서)**

> "The 'productivity J-curve' describes how new technologies, especially general purpose technologies, deliver productivity gains only after a period of investment in complementary intangible goods, such as business processes and new skills."
>
> **"생산성 J커브"**는 신기술, 특히 범용기술이 **업무 프로세스와 새로운 역량 같은 보완적 무형자산에 대한 투자 기간을 거친 후에야** 생산성 이득을 가져오는 방식을 서술한다.

**(d) 미시 증거 인용**

> "call center operators became 14% more productive when they used the technology, with the gains of over 30% for the least experienced workers"
>
> 콜센터 상담원은 이 기술을 사용할 때 **14% 더 생산적**이 되었고, **가장 경험이 적은 노동자에게는 30% 이상**의 이득이 있었다.

> "software engineers can code up to twice as fast using a tool called Codex" / "many writing tasks can also be completed twice as fast" / "economists can be 10-20% more productive using large language models"
>
> 소프트웨어 엔지니어는 Codex를 사용해 **최대 2배 빠르게** 코딩할 수 있다 / 많은 글쓰기 과업도 **2배 빠르게** 완료할 수 있다 / 경제학자는 대규모 언어모델을 사용해 **10~20% 더 생산적**일 수 있다.

#### 이 책에 쓸 수 있는 부분
- **"AX의 두 번째 곡선"** — 업무 자동화(일시적 레벨 효과)와 아이디어 생산 가속(항구적 성장률 효과)을 분리하는 프레임. 기업의 AX 투자 포트폴리오를 "운영 효율" vs "R&D·제품 혁신"으로 나누는 논리적 근거가 된다.
- **J커브** — "왜 우리 회사 AX는 아직 실적에 안 잡히는가"에 대한 가장 인용하기 좋은 답.

#### 한계·반박
- 30%·60%·18%는 **예시적 가정**이며 저자들도 illustrative임을 밝힌다. 노출도 필터·수익성 필터·도입률이 전혀 없다 — Acemoglu 산식의 4항 중 2항(수익성, 노출 GDP비중)을 사실상 1로 놓은 것과 같다.
- "인지노동이 부가가치의 60%"라는 값이 Acemoglu의 "노출 과업 GDP 비중 20%"와 3배 차이 나는데, 두 정의(인지노동 전체 vs LLM 노출 과업)가 다르므로 **직접 비교 불가**. 이 점을 명확히 하지 않으면 잘못된 비교가 된다.

---

### 2-3. ⭐ Aghion & Bunel — "AI and Growth: Where Do We Stand?" (2024-06)

**이 논문이 토픽 B-5의 핵심이다.** Acemoglu의 **수식을 그대로 쓰면서 파라미터만 바꿔** 10배 큰 값을 얻는다. 발산의 원인을 파라미터 단위로 분해해 보여주는 유일한 문헌이다.

**서지**
- Aghion, Philippe, and Simon Bunel. "AI and Growth: Where Do We Stand?" **June 2024**.
- 저자 소속(원문 표기): Aghion — Collège de France, INSEAD et London School of Economics; Bunel — Banque de France et École Normale Supérieure.
- PDF: https://www.frbsf.org/wp-content/uploads/AI-and-Growth-Aghion-Bunel.pdf (Federal Reserve Bank of San Francisco 호스팅, 서버 Last-Modified 2024-08-03; FRBSF 관련 행사: "Philippe Aghion: The Growth and Employment Effects of AI", 2024-04)
- 태그: **[WP]**

#### 핵심 주장
두 가지 접근으로 향후 10년 AI의 거시 생산성 효과를 추정한다. ① **과거 기술혁명과의 유비** → **연 0.8~1.3%p** ② **Acemoglu의 과업기반 산식에 본인들의 문헌 독해를 대입** → **연 0.07~1.24%p, 중앙값 0.68%p**.

#### 인용 가능한 문장·수치 (VERBATIM)

**(a) 초록 — 두 접근의 결론**

> "Based on the first approach, we estimate that the AI revolution should increase aggregate productivity growth by between 0.8 and 1.3pp per year over the next decade. Using the second approach but with our own reading of the recent empirical literature on the various components of the task-based formula, we obtain a median estimate of 0.68pp additional annual total factor productivity (TFP) growth. Our estimates do not take into account the fact that AI automates tasks not only in the production of goods and services, our focus in this note, but also in the production of ideas."
>
> 첫 번째 접근에 따르면, 우리는 AI 혁명이 향후 10년간 **총생산성 증가율을 연 0.8~1.3%p** 높일 것으로 추정한다. 두 번째 접근을 쓰되 과업기반 산식의 각 구성요소에 대한 **우리 자신의 최근 실증문헌 독해**를 적용하면, **연간 총요소생산성(TFP) 증가율 추가분의 중앙값 0.68%p**를 얻는다. 우리 추정치는 AI가 재화·서비스 생산의 과업뿐 아니라 **아이디어 생산의 과업도 자동화**한다는 사실을 반영하지 않은 것이다.

**(b) Acemoglu와의 직접 대조 — 이 문장이 결정적이다**

> "As for the second approach, it leads Acemoglu (2024) to a much smaller extra growth estimate of 0.07 pp per year over the next decade. Using the same task-based formula, but with our own reading of the recent empirical literature regarding each component of that formula, we estimate that the AI revolution should increase aggregate productivity growth by between 0.07pp and 1.24pp, with a median estimate of 0.68pp additional annual TFP growth."
>
> 두 번째 접근의 경우, 그것은 Acemoglu(2024)를 향후 10년간 **연 0.07%p**라는 훨씬 작은 추가 성장 추정치로 이끈다. **동일한 과업기반 산식**을 사용하되 그 산식의 각 구성요소에 관한 **우리 자신의 최근 실증문헌 독해**를 적용하면, 우리는 AI 혁명이 총생산성 증가율을 **연 0.07%p에서 1.24%p 사이**로 높일 것이며 **중앙값은 연 0.68%p 추가 TFP 성장**이라고 추정한다.

**(c) 4개 파라미터 — 각각의 구간과 근거**

> "TFP gains over 10 years = GDP share of tasks that are exposed to AI × Share of exposed tasks for which it will be economically profitable to use AI × Average costs savings from AI × AI exposure-adjusted labor share"

**① 노출도:**
> "They estimate that the GDP share of tasks that are exposed to AI is 19.9%. Following a related approach based on an estimation of the exposure to AI of every task defined by O*NET, Gmyrek et al. (2023) finds 18.5% exposed in advanced countries. Conversely, relying on abilities rather than tasks, Pizzinelli et al. (2023) estimates that this share is much higher, around 60% in the United States, and even reaching 68% in the United Kingdom (Figure 4). […] This leads us to consider that the relevant interval for estimating the share of GDP of tasks exposed to AI is [0.185; 0.68]."
>
> 그들[Eloundou et al.]은 AI에 노출된 과업의 GDP 비중을 **19.9%**로 추정한다. O*NET이 정의한 모든 과업의 AI 노출도를 추정하는 관련 접근을 따르면, Gmyrek et al.(2023)은 선진국에서 **18.5%** 노출을 발견한다. 반대로 과업이 아니라 **능력(abilities)**에 기반하면, Pizzinelli et al.(2023)은 이 비중이 훨씬 높아 **미국 약 60%, 영국은 68%**에 이른다고 추정한다. […] 이는 AI 노출 과업의 GDP 비중 추정에 적절한 구간이 **[0.185; 0.68]**임을 시사한다.

**② 수익성 필터 — Acemoglu의 23% 고정에 대한 정면 반박:**
> "However, this figure of 23% suffers from two major shortcomings: 1. It assumes that the proportion of tasks for which it will be profitable to use AI will remain constant over time. This is equivalent to assuming that the cost-saving advances from AI implementation will be zero over the next decade. 2. Svanberg et al. (2024) focuses on computer vision, rather than generative AI in general, which could have a different share of profitable tasks, as it encompasses a much wider technological field."
>
> 그러나 이 **23%라는 수치는 두 가지 중대한 결함**이 있다. **1.** AI 사용이 수익성 있는 과업의 비율이 **시간이 흘러도 일정하게 유지된다**고 가정한다. 이는 **향후 10년간 AI 도입의 비용 절감 진보가 0**이라고 가정하는 것과 같다. **2.** Svanberg et al.(2024)은 생성형 AI 일반이 아니라 **컴퓨터 비전**에 초점을 두는데, 생성형 AI는 훨씬 넓은 기술 영역을 포괄하므로 수익성 있는 과업 비중이 다를 수 있다.

> "Using a methodology based on the cost of computing time rather than performance, Besiroglu and Hobbhahn (2022) estimates a 22% annual decline in computing costs over recent years (Figure 7). At this rate, the proportion of tasks that can incorporate IA will rise to around 50% within 10 years (Figure 5). […] this leads us to consider that, given the literature available, a relevant interval for estimating the proportion of exposed tasks for which it will be profitable to use AI is [0.23; 0.8]."
>
> 성능이 아니라 컴퓨팅 시간 비용에 기반한 방법론을 사용하여, Besiroglu & Hobbhahn(2022)은 최근 수년간 **연 22%의 컴퓨팅 비용 하락**을 추정한다. 이 속도라면 AI를 도입할 수 있는 과업 비중은 **10년 내 약 50%**로 상승한다. […] 이는 이용 가능한 문헌을 감안할 때, AI 사용이 수익성 있는 노출 과업 비중 추정의 적절한 구간이 **[0.23; 0.8]**임을 시사한다.

**③ 비용 절감률 — Peng을 뺄 것인가 넣을 것인가:**
> "Peng et al. (2023) estimates these gains at +55.8% for programmers, and Noy and Zhang (2023) estimates a +40% gain for analysts. For customer service employees, Brynjolfsson et al. (2023) finds a gain of +14% for the first month following the introduction of the AI assistant, reaching +25% for the second month and stabilizing between +25% and +30% in the following three months (Figure 1). Over 10 years, the gains considered for this study thus appear to be in the order of +25%. On the grounds that the analysis framework of Peng et al. (2023) is less relevant because the task evaluated is too finely defined, Acemoglu (2024) looks to the average of the results of the other two studies to derive an effect on worker productivity of +27%. When we take the three studies into account, the long-term productivity effect reaches an average of +40%. This leads us to consider that the relevant interval for estimating the average labor cost savings made possible by AI is [0.27; 0.4]."
>
> Peng et al.(2023)은 프로그래머의 이득을 **+55.8%**, Noy & Zhang(2023)은 분석가의 이득을 **+40%**로 추정한다. 고객 서비스 직원에 대해 Brynjolfsson et al.(2023)은 AI 어시스턴트 도입 후 첫 달 **+14%**, 둘째 달 **+25%**에 도달하고 이후 3개월간 **+25%~+30% 사이에서 안정화**되는 이득을 발견한다. 따라서 **10년에 걸쳐 이 연구에서 고려되는 이득은 +25% 수준**으로 보인다. Peng et al.(2023)의 분석틀이 평가 과업이 지나치게 세밀하게 정의되어 관련성이 낮다는 이유로, Acemoglu(2024)는 나머지 두 연구 결과의 평균을 취해 노동자 생산성 효과 **+27%**를 도출한다. **세 연구를 모두 고려하면 장기 생산성 효과는 평균 +40%에 이른다.** 이는 AI가 가능케 하는 평균 노동비용 절감 추정의 적절한 구간이 **[0.27; 0.4]**임을 시사한다.

> ⭐ **주목:** Aghion & Bunel은 Brynjolfsson et al.의 **14%가 아니라 안정화된 25%**를 읽는다. Acemoglu는 **14%**를 사용한다. 같은 논문, 다른 숫자. 이것 하나만으로도 이 책에 쓸 수 있는 강력한 사례다.

**④ 노동소득분배율:**
> "In the absence of studies providing more precise information on the labor share in value added adjusted for exposure to AI or examining countries other than the United States, we cannot refine the labor share following AI exposure. We therefore retain Acemoglu (2024)'s value of 0.57."
>
> AI 노출로 조정된 부가가치 대비 노동소득분배율에 관한 더 정밀한 정보를 제공하거나 미국 외 국가를 검토한 연구가 없으므로, 우리는 AI 노출에 따른 노동소득분배율을 정교화할 수 없다. 따라서 **Acemoglu(2024)의 값 0.57을 그대로 사용**한다.

**(d) 최종 기준선 계산 — 인용 시 이 산식 자체를 옮기는 것이 가장 효과적이다**

> "However, a baseline scenario taking into account (i) the share of tasks exposed to AI in developed countries estimated at 60% (Pizzinelli et al., 2023), (ii) the share of exposed tasks for which it will be profitable to use AI estimated at 50% due to a 22% annual decline in computing costs (Besiroglu and Hobbhahn, 2022) and (iii) productivity gains enabled by AI estimated at 40% based on three benchmark studies (Peng et al., 2023; Noy and Zhang, 2023; Brynjolfsson et al., 2023) leads to an estimated increase in annual productivity growth of 0.68pp over 10 years"
>
> 그러나 (i) 선진국에서 AI에 노출된 과업 비중 **60%**(Pizzinelli et al., 2023), (ii) 컴퓨팅 비용의 연 22% 하락으로 인해 AI 사용이 수익성 있는 노출 과업 비중 **50%**(Besiroglu & Hobbhahn, 2022), (iii) 세 벤치마크 연구에 기반한 AI 생산성 이득 **40%**를 고려한 기준 시나리오는 **10년에 걸쳐 연간 생산성 증가율 0.68%p 상승**이라는 추정으로 이어진다.

> **Annual TFP gains = ExpAI × ProfitableAI × LaborCostSavingsAI × LaborShareAI × 10 = 0.68**
> **0.60 × 0.50 × 0.40 × 0.57 → 0.68**
>
> (Acemoglu: **0.200 × 0.23 × 0.27 × 0.535 → 0.066**)

**(e) 역사 유비 접근**

> "If we assume that the productivity gains enabled by the AI wave of the next decade will be comparable to those of the electricity wave of the 1920s in Europe, then productivity growth would increase by 1.3 percentage points per year starting in 2024 (Figure 2a). If we prefer to use the digital technology wave of the late 1990s and early 2000s in the United States as a point of comparison, the increase in productivity growth would be around 0.8 percentage points per year (Figure 2b). By comparison, France's potential productivity growth is now estimated at 0.5% per year over the medium term."
>
> 향후 10년 AI 물결이 가능케 하는 생산성 이득이 **1920년대 유럽의 전기 물결**과 비교 가능하다고 가정하면, 생산성 증가율은 2024년부터 **연 1.3%p** 상승할 것이다. **1990년대 후반~2000년대 초 미국의 디지털 기술 물결**을 비교 기준으로 삼는 편을 택하면, 생산성 증가는 **연 약 0.8%p** 상승할 것이다. 비교하자면 프랑스의 잠재 생산성 증가율은 현재 중기적으로 **연 0.5%**로 추정된다.

**(f) 전기의 30년 지연 — 확산 지체를 정면으로 다룬다**

> "In the United States, as in Europe, the productivity gains from electricity did not materialize until about thirty years after the invention of the technology. […] Building on the parallel with the introduction of electricity, a thirty-year lag would suggest that the impact of AI on productivity is likely to be felt in the next few years."
>
> 미국에서도 유럽에서도 전기로부터의 생산성 이득은 **기술 발명 후 약 30년이 지나서야** 실현되었다. […] 전기 도입과의 유비에 기초하면, **30년의 시차**는 AI가 생산성에 미치는 영향이 **향후 수년 내에 체감될 가능성**이 있음을 시사한다.
>
> *(주: 머신러닝의 통계적 접근이 1990년대부터 부상했다는 앞 문단을 받아, "1990년대 + 30년 = 2020년대"라는 논리다.)*

**(g) 이 추정이 상한이 아니라 하한일 수 있는 이유 (신규 아이디어 생산)**

> "This estimate in turn may be seen as a lower bound to the extent that it does not account for the fact that AI also automates the production of ideas. On the other hand, it does not take into account potential barriers to growth, in particular those associated with the lack of competition in the upstream segments of the AI value chain."
>
> 이 추정치는 **AI가 아이디어 생산도 자동화한다는 사실을 반영하지 않는다는 점에서 하한으로 볼 수 있다.** 반면, 성장의 잠재적 장벽, 특히 **AI 가치사슬의 상류 부문에서의 경쟁 부재**와 관련된 장벽을 고려하지 않은 것이기도 하다.

**(h) 경쟁 정책 — 한국 AX 정책 논의에 직결**

> "The difference between the ICT and AI revolutions is that this time the GAFAMs are dominant from the outset and can therefore immediately prevent the entry of new, innovative firms. The lack of competition is particularly pronounced in the upstream segments of the AI production chain, namely access to data and computing power, which are dominated by a small number of large firms"
>
> ICT 혁명과 AI 혁명의 차이는, 이번에는 **GAFAM이 처음부터 지배적**이어서 새롭고 혁신적인 기업의 진입을 **즉시 차단**할 수 있다는 점이다. 경쟁 부재는 AI 생산 사슬의 **상류 부문 — 즉 데이터와 컴퓨팅 파워에 대한 접근 —** 에서 특히 두드러지며, 이는 소수의 대기업에 의해 지배되고 있다.

#### 이 책에 쓸 수 있는 부분
- **"같은 공식, 다른 답"** — 이 책 전체의 논지를 지탱할 수 있는 사례. 표 하나로 두 계산을 나란히 놓으면 독자가 즉시 이해한다.
- **Brynjolfsson 14% vs 25%** — "어느 시점의 숫자를 읽을 것인가"가 거시 추정을 10배 바꾼다는 사실. AX ROI 측정 챕터에 그대로 이식 가능.
- **컴퓨팅 비용 연 22% 하락** — Acemoglu가 0으로 놓은 항목. AX 투자 의사결정에서 "지금 안 되는 것"과 "3년 뒤에도 안 되는 것"을 구별하라는 실무 지침의 근거.

#### 한계·반박
- 노출도 60%는 **과업(task) 기반이 아니라 능력(abilities) 기반** 측정(Pizzinelli et al.)을 가져온 것이며, 저자들도 "이 연구는 노출 과업의 GDP 비중이 아니라 노출 과업 비중만 제공한다"고 인정하면서 "노출 과업이 소수 부문에 집중되지 않았다면 크기가 비슷할 것"이라고 **가정**한다. 측정 대상이 다른 두 수치를 같은 산식 자리에 넣는 데 대한 정당화가 약하다.
- 수익성 필터 50%는 "22% 비용 하락이 10년 지속"이라는 외삽에 의존한다.
- 노동소득분배율만은 Acemoglu의 **구버전 값 0.57**을 그대로 썼다(게재본은 0.535). 즉 두 논문의 비교는 완전히 동일 기준이 아니다 — **이 책에 표를 만들 때 각주로 밝힐 것.**
- 미게재 노트(2024-06)이며 정식 학술지 게재 여부는 확인되지 않았다(⚠️ 참조).

---

## 3. 기관 추정치

### 3-1. IMF — Cazzaniga et al. (2024-01)

**서지**
- Cazzaniga, Mauro, Florence Jaumotte, Longji Li, Giovanni Melina, Augustus J. Panton, Carlo Pizzinelli, Emma Rockall, and Marina M. Tavares. "Gen-AI: Artificial Intelligence and the Future of Work." *IMF Staff Discussion Note* **SDN/2024/001**, International Monetary Fund, **January 2024**.
- ISBN: **979-8-40026-254-8** / JEL: E24, J24, J31, O33, O38
- PDF: https://www.imf.org/-/media/Files/Publications/SDN/2024/English/SDNEA2024001.ashx
- 태그: **[WP]** (IMF 직원 토론노트 — 표지에 "published to elicit comments and to encourage debate", "views… do not necessarily represent the views of the IMF")

#### 인용 가능한 문장·수치 (VERBATIM — 사용자 추정 60/40/26 정밀 확인 결과: **전부 정확**)

> "Almost 40 percent of global employment is exposed to AI, with advanced economies at greater risk but also better poised to exploit AI benefits than emerging market and developing economies. In advanced economies, about 60 percent of jobs are exposed to AI, due to prevalence of cognitive-task-oriented jobs. A new measure of potential AI complementarity suggests that, of these, about half may be negatively affected by AI, while the rest could benefit from enhanced productivity through AI integration. Overall exposure is 40 percent in emerging market economies and 26 percent in low-income countries."
>
> **전 세계 고용의 거의 40%가 AI에 노출**되어 있으며, 선진국은 더 큰 위험에 처해 있지만 신흥시장·개발도상국보다 AI의 편익을 활용할 준비도 더 잘 되어 있다. **선진국에서는 인지 과업 중심 일자리가 우세하여 약 60%의 일자리가 AI에 노출**되어 있다. AI 보완성 잠재력의 새로운 측정치는 이 중 **약 절반이 AI에 부정적 영향**을 받을 수 있고 나머지는 AI 통합을 통한 생산성 향상의 혜택을 볼 수 있음을 시사한다. **전체 노출도는 신흥시장 경제 40%, 저소득국 26%**다.

> "About 40 percent of workers worldwide are in high-exposure occupations; the share is 60 percent in advanced economies, which indicates potentially large macroeconomic implications. […] In the average advanced economy, 27 percent of employment is in high-exposure, high-complementarity occupations, 33 percent in high-exposure, low-complementarity jobs. In comparison, emerging market economies have corresponding shares of 16 and 24 percent, respectively, and low-income countries have shares of 8 and 18 percent, respectively."
>
> 전 세계 노동자의 약 **40%가 고노출 직업**에 있으며, 선진국에서는 그 비중이 **60%**로 잠재적으로 큰 거시경제적 함의를 시사한다. […] 평균적 선진국에서는 고용의 **27%가 고노출·고보완성 직업**, **33%가 고노출·저보완성 직업**에 있다. 비교하면 신흥시장 경제는 각각 **16%와 24%**, 저소득국은 각각 **8%와 18%**다.

> "Almost 70 and 60 percent of UK and US employment, respectively, is in high-exposure occupations, approximately equally distributed between those that are high- and low-complementarity positions. High-exposure employment in emerging market economies ranges from 41 percent in Brazil to 26 percent in India."
>
> **영국과 미국 고용의 각각 거의 70%와 60%**가 고노출 직업에 있으며, 고보완성 직위와 저보완성 직위 사이에 대략 균등하게 분포한다. 신흥시장 경제의 고노출 고용은 **브라질 41%에서 인도 26%**까지 분포한다.

**생산성/산출 시뮬레이션 (질문의 "productivity/growth numbers")**

> "The productivity increase is calibrated to generate close to a 1.5 percentage point increase in the workers' average annual productivity growth rate in the first 10 years after AI adoption. This value is at the lower end of firm-level studies estimating the potential impact of AI adoption on workers' productivity (as discussed in Briggs and Kodnani 2023)."
>
> 생산성 증가는 **AI 도입 후 첫 10년간 노동자 평균 연간 생산성 증가율이 1.5%p 가까이 상승**하도록 캘리브레이션되었다. 이 값은 AI 도입이 노동자 생산성에 미치는 잠재적 영향을 추정하는 **기업 수준 연구들의 하단**에 해당한다(Briggs & Kodnani 2023에서 논의된 대로).

> "we assume that the labor share declines by 5.5 percentage points following the introduction of AI."
>
> 우리는 AI 도입 이후 **노동소득분배율이 5.5%p 하락**한다고 가정한다.

> "In the first scenario, in which AI has low complementarity, the use of AI leads to an increase in output of almost 10 percent thanks to a combination of capital deepening and a small increase in total factor productivity"
>
> AI의 보완성이 낮은 첫 번째 시나리오에서, AI 사용은 **자본심화와 소폭의 총요소생산성 증가의 결합** 덕분에 **산출을 거의 10% 증가**시킨다.

> "Last, when the productivity impact is also considered, output increases by 16 percent between steady states, and total factor productivity increases by almost 4 percent. These gains happen primarily in the first 10 years of the transition. Under this third scenario, despite the increase in labor income inequality, the total income level increases for all workers in the economy, ranging from 2 percent for low-income workers to almost 14 percent for high-income workers."
>
> 마지막으로 생산성 영향까지 고려하면, 정상상태 간 **산출은 16% 증가**하고 **총요소생산성은 거의 4% 증가**한다. 이 이득은 주로 **전환기의 첫 10년**에 발생한다. 이 세 번째 시나리오에서는 노동소득 불평등 증가에도 불구하고 경제 내 모든 노동자의 총소득 수준이 증가하는데, 그 범위는 **저소득 노동자 2%에서 고소득 노동자 거의 14%**까지다.

> "Total income levels of low-income workers decline by 2 percent, while the gains at the top are almost 8 percent"
>
> (고보완성 시나리오에서) 저소득 노동자의 총소득 수준은 **2% 하락**하는 반면 상위층의 이득은 **거의 8%**다.

#### 이 책에 쓸 수 있는 부분
- **"노출도 ≠ 대체"** — IMF의 노출×보완성 2×2 분류는 AX 인력 전략의 프레임으로 그대로 쓸 수 있다. 한국은 선진국 프로필(고노출)에 가깝고, 고보완성 직군 비중을 높이는 것이 정책 목표가 된다.
- **60%/40%/26%** — 국가별 AI 노출 격차를 보여주는 가장 널리 인용되는 수치.
- **TFP 4% vs 산출 16%** — 산출 증가의 대부분이 TFP가 아니라 **자본심화**에서 온다는 사실. Acemoglu가 "TFP만이 후생 관련"이라 말한 이유를 정확히 보여준다.

#### 한계·반박
- **노출도는 잠재적 기술 노출이며 실제 도입·수익성 필터가 없다.** IMF의 60%와 Acemoglu의 4.6%(수익성 필터 통과분)는 **전혀 다른 개념**이므로 나란히 놓으면 안 된다.
- 모델 시뮬레이션은 **정상상태 간 비교**이며, 생산성 캘리브레이션 값 1.5%p는 Goldman Sachs를 근거로 **외생적으로 부여**된 것이다. 즉 IMF의 TFP 4%는 독립적 추정이 아니라 **GS 가정의 파생물**이다 — 인용 시 반드시 밝힐 것.
- 노동소득분배율 5.5%p 하락은 1980–2014년 영국 경험을 차용한 가정이다.

---

### 3-2. OECD — 3편 (2024-11 / 2025-06 / 2025-12)

이 세 편은 **Acemoglu와 Goldman Sachs 사이를 명시적으로 메우는 "중간 추정치"**이며, 두 진영을 같은 그림에 놓고 비교한다.

#### (a) Filippucci, Gál & Schief (2024-11) — "Miracle or Myth?"

**서지**
- Filippucci, Francesco, Peter Gal, and Matthias Schief. "Miracle or Myth? Assessing the macroeconomic productivity gains from Artificial Intelligence." *OECD Artificial Intelligence Papers*, OECD Publishing, Paris, **22 November 2024**. DOI: `10.1787/b524a072-en`. 태그: **[WP]**

**초록 VERBATIM**
> "The paper studies the expected macroeconomic productivity gains from Artificial Intelligence (AI) over a 10-year horizon. It builds a novel micro-to-macro framework by combining existing estimates of micro-level performance gains with evidence on the exposure of activities to AI and likely future adoption rates, relying on a multi-sector general equilibrium model with input-output linkages to aggregate the effects. Its main estimates for annual aggregate total-factor productivity growth due to AI range between 0.25-0.6 percentage points (0.4-0.9 pp. for labour productivity). The paper discusses the role of various channels in shaping these macro-level gains and highlights several policy levers to support AI's growth-enhancing effects."
>
> 이 논문은 **10년 시계**에서 AI로부터 기대되는 거시 생산성 이득을 연구한다. 미시 수준 성과 이득의 기존 추정치를 **활동의 AI 노출도** 및 **향후 예상 도입률**에 관한 증거와 결합하고, **투입산출 연관을 갖춘 다부문 일반균형 모형**에 의존해 효과를 총계화하는 새로운 **미시-거시 프레임워크**를 구축한다. AI로 인한 **연간 총계 총요소생산성 증가율의 주요 추정치는 0.25~0.6%p 범위**(노동생산성은 **0.4~0.9%p**)다. 이 논문은 이 거시적 이득을 형성하는 다양한 경로의 역할을 논의하고 AI의 성장 촉진 효과를 뒷받침할 여러 정책 수단을 제시한다.

> ⭐ **이 하나의 값이 이 토픽의 중간값 앵커다.** Acemoglu(연 0.064%p)의 **4~9배**, Aghion & Bunel(연 0.68%p)의 **0.4~0.9배**, Goldman Sachs(연 1.5%p 노동생산성)의 **1/4~2/3**.

#### (b) Filippucci, Gál, Laengle & Schief (2025-06) — G7 확장

**서지**
- Filippucci, Francesco, Péter Gál, Katharina Laengle, and Matthias Schief. "Macroeconomic productivity gains from Artificial Intelligence in G7 economies." *OECD Artificial Intelligence Papers*, OECD Publishing, Paris, **26 June 2025**. DOI: `10.1787/a5319ab5-en`. 태그: **[WP]**

**초록 VERBATIM**
> "Across the three scenarios considered, the estimated range for annual aggregate labour productivity growth due to AI range between 0.4-1.3 percentage points in countries with high AI exposure – due to stronger specialisation in highly AI-exposed knowledge intensive services such as finance and ICT services – and more widespread adoption (e.g. United States and United Kingdom). In contrast, projected gains in several other G7 economies are up to 50% smaller, reflecting differences in sectoral composition and assumptions about the relative pace of AI adoption."
>
> 고려된 세 시나리오에 걸쳐, AI로 인한 **연간 총계 노동생산성 증가율의 추정 범위는 AI 노출도가 높고**(금융·ICT 서비스 같은 고노출 지식집약 서비스에 대한 강한 특화 때문) **도입이 더 광범위한 국가(예: 미국, 영국)에서 0.4~1.3%p**다. 반면 다른 여러 G7 경제의 예상 이득은 **최대 50%까지 작은데**, 이는 부문 구성의 차이와 AI 도입의 상대적 속도에 대한 가정을 반영한다.

#### (c) Chaar, Filippucci, Jona-Lasinio & Nicoletti (2025-12) — "AI and the Global Productivity Divide"

**서지**
- Chaar, Tania, Francesco Filippucci, Cecilia Jona-Lasinio, and Giuseppe Nicoletti. "AI and the Global Productivity Divide: Fuel for the Fast or a Lift for the Laggards?" *OECD Artificial Intelligence Papers*, **December 2025, No. 51**. DOI: `10.1787/c315ea90-en`. CC BY 4.0.
- PDF: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/ai-and-the-global-productivity-divide_f47026c5/c315ea90-en.pdf
- 태그: **[WP]**

**⭐ 이 논문의 Figure 1은 Goldman Sachs / Aghion-Bunel / Acemoglu를 하나의 축에 놓고 비교한다 — 이 책의 비교 그래프 원본으로 최적이다.**

> "Figure 1: AI will be a key driver of productivity growth in advanced economies, with large cross-country heterogeneity — Predicted labour productivity growth due to AI over the next 10 years, percentage points (annualised)"
>
> 그림 1: AI는 선진국 생산성 성장의 핵심 동인이 될 것이며, 국가 간 이질성이 크다 — **향후 10년간 AI로 인한 예측 노동생산성 증가율, %p(연율화)**
> (가로축 항목: Goldman Sachs (2023, USA) / Aghion and Bunel (2024, USA) / Acemoglu (2024, USA) / USA / GBR / DEU / CAN / FRA / ITA / JPN)

> "Notes: In the low adoption scenario AI adoption is assumed to be up by 23% in the US (in line with historical electricity phones adoption path), in the medium adoption up by 40% (in line with historical ICT technologies adoption path), in the high adoption up by 60% (in line with historical mobile phones adoption path). Exposure is taken from Eloundou et al. (2025), with the expanded capabilities assuming full synergies from additional software."
>
> 주: **저도입 시나리오**에서는 미국의 AI 도입이 **23%** 상승(역사적 전기·전화 도입 경로에 부합), **중도입**은 **40%** 상승(역사적 ICT 기술 도입 경로에 부합), **고도입**은 **60%** 상승(휴대전화의 빠른 확산에 부합)한다고 가정한다. 노출도는 Eloundou et al.(2025)에서 취했으며, 확장된 역량은 추가 소프트웨어로부터의 완전한 시너지를 가정한다.

> "Overall, the authors evaluate the potential AI productivity gains to be lower in other G7 countries than in the US, as a consequence of slower rates of expected adoption and different industrial structures. In a scenario where AI adoption follows the same path of past ICT technologies and covers a broad range of tasks, AI benefits in terms of labour productivity are expected to be around half of those of the US in Italy and Japan"
>
> 전반적으로 저자들은 다른 G7 국가의 잠재적 AI 생산성 이득이 **예상 도입 속도가 느리고 산업구조가 다르다는 결과로** 미국보다 낮다고 평가한다. AI 도입이 과거 ICT 기술과 동일한 경로를 따르고 광범위한 과업을 포괄하는 시나리오에서, 노동생산성 측면의 AI 편익은 **이탈리아와 일본에서 미국의 약 절반** 수준으로 예상된다.

> "Forthcoming OECD work confirms this trend for OECD and G20 economies (Filippucci et al., 2025), projecting contributions of AI to growth as low as .05-.3 pp annually for countries with a lower incidence of complementary factors to AI adoption, over the next 10 years."
>
> 향후 발표될 OECD 연구는 OECD 및 G20 경제에 대해 이 추세를 확인하며, **AI 도입의 보완적 요소가 적은 국가에서는 향후 10년간 AI의 성장 기여가 연 0.05~0.3%p까지 낮을 것**으로 전망한다.

#### 이 책에 쓸 수 있는 부분
- **한국에 대한 함의가 가장 직접적인 자료.** "부문 구성 + 도입 속도"가 국가별 AI 생산성 이득을 결정한다는 명제. 한국의 금융·ICT 비중과 제조업 비중을 대입해 논의를 전개할 수 있다.
- **도입률 시나리오 23%/40%/60%를 각각 전기·ICT·휴대전화 확산 경로에 대응시킨 설계** — "AX 확산 속도를 무엇에 비유할 것인가"라는 질문을 정량적 선택지로 바꿔준다.
- OECD의 미시-거시 프레임워크는 **투입산출 연관을 통한 총계화**로 Hulten의 1차 근사를 넘어선다. Acemoglu의 방법론적 한계에 대한 기관 차원의 대응.

#### 한계·반박
- OECD 역시 노출도·미시 성과 이득 추정치를 외부 문헌(Eloundou et al. 등)에서 가져온다. 입력값이 바뀌면 결과도 바뀐다는 근본 취약성은 동일.
- "Miracle or Myth?" 본문 전체는 열지 못했다(⚠️ 참조) — 초록의 수치만 확인.

---

### 3-3. BIS — Annual Economic Report 2024, Chapter III

**서지**
- Bank for International Settlements. "III. Artificial intelligence and the economy: implications for central banks." *BIS Annual Economic Report 2024*, **30 June 2024**. URL: https://www.bis.org/publ/arpdf/ar2024e3.htm. 태그: **[WP]** (국제기구 연차보고서 장)

#### 인용 가능한 문장·수치 (VERBATIM)

> "ChatGPT alone reached one million users in less than a week and nearly half of US households have used gen AI tools in the past 12 months."
>
> ChatGPT만 해도 **일주일 안에 100만 사용자**에 도달했고, **미국 가구의 거의 절반**이 지난 12개월간 생성형 AI 도구를 사용했다.

> "In 2023 alone, spending on AI exceeded $150 billion worldwide, and a survey of US companies' technology officers across all sectors suggests almost 50% rank AI as their top budget item over the next years."
>
> **2023년 한 해에만 전 세계 AI 지출이 1,500억 달러를 넘었고**, 전 부문 미국 기업 기술책임자 대상 설문은 **거의 50%가 향후 수년간 AI를 최우선 예산 항목으로 꼽는다**는 것을 시사한다.

> "The estimates provided by the literature for AI's impact on annual labour productivity growth (ie output per employee) are thus substantive, although their range varies."
>
> 따라서 AI가 **연간 노동생산성 증가율**(즉 종업원당 산출)에 미치는 영향에 대해 문헌이 제시하는 추정치는 상당하지만, **그 범위는 편차가 크다.**

> "Comparing programmer groups with similar productivity levels and work experience but with or without access to the LLM shows a 55% increase in productivity (measured by the number of lines of code produced) on average for the group with access to the LLM." / "Productivity increased only among junior programmers"
>
> 생산성 수준과 경력이 유사하되 LLM 접근 여부가 다른 프로그래머 집단을 비교하면, LLM 접근 집단에서 평균 **55%의 생산성 증가**(생산된 코드 줄 수로 측정)가 나타난다. / **생산성은 주니어 프로그래머에게서만 증가**했다.

#### 한계·반박
- 이 장은 **AI가 중앙은행에 갖는 함의**가 초점이며, 독자적 거시 TFP 추정치를 제시하지 않는다. "문헌의 범위 편차가 크다"는 서술에 그친다. 거시 수치 인용원으로는 부적절하고, **"주니어에게만 효과"**와 **투자 규모 통계**의 인용원으로 쓰는 것이 적절하다.

---

## 4. 2025–2026 최신 거시 추정치 & 기업 수준 TFP 증거

### 4-1. 미시 실험 4대 벤치마크 (Acemoglu·Aghion 산식의 입력값)

#### Peng, Kalliamvakou, Cihon & Demirer (2023) — GitHub Copilot RCT
- Peng, Sida, Eirini Kalliamvakou, Peter Cihon, and Mert Demirer. "The Impact of AI on Developer Productivity: Evidence from GitHub Copilot." arXiv:2302.06590, **13 February 2023**. DOI: `10.48550/arXiv.2302.06590`. 태그: **[PP]**

> "Recruited software developers were asked to implement an HTTP server in JavaScript as quickly as possible. The treatment group, with access to the AI pair programmer, completed the task 55.8% faster than the control group."
>
> 모집된 소프트웨어 개발자들에게 JavaScript로 HTTP 서버를 최대한 빨리 구현하도록 요청했다. AI 페어 프로그래머에 접근한 **처치집단은 통제집단보다 과업을 55.8% 빠르게** 완료했다.

#### Noy & Zhang (2023) — Science
- Noy, Shakked, and Whitney Zhang. "Experimental evidence on the productivity effects of generative artificial intelligence." *Science*, Vol. **381**, Issue **6654**, pp. **187–192**, **13 July 2023**. DOI: `10.1126/science.adh2586`. 태그: **[PR]**

> "In a preregistered online experiment, we assigned occupation-specific, incentivized writing tasks to 453 college-educated professionals and randomly exposed half of them to ChatGPT. Our results show that ChatGPT substantially raised productivity: The average time taken decreased by 40% and output quality rose by 18%. Inequality between workers decreased, and concern and excitement about AI temporarily rose. Workers exposed to ChatGPT during the experiment were 2 times as likely to report using it in their real job 2 weeks after the experiment and 1.6 times as likely 2 months after the experiment."
>
> 사전등록된 온라인 실험에서, **453명의 대졸 전문직**에게 직업별 인센티브가 부여된 글쓰기 과업을 할당하고 그중 절반을 무작위로 ChatGPT에 노출시켰다. 결과는 ChatGPT가 생산성을 상당히 높였음을 보여준다: **평균 소요시간이 40% 감소하고 산출물 품질은 18% 상승**했다. 노동자 간 불평등은 감소했고 AI에 대한 우려와 흥분은 일시적으로 상승했다. 실험 중 ChatGPT에 노출된 노동자는 실험 2주 후 실제 직무에서 그것을 사용한다고 보고할 가능성이 **2배**, 2개월 후에는 **1.6배**였다.

#### Brynjolfsson, Li & Raymond (2025) — QJE ⭐ 게재본과 WP의 수치가 다르다
- Brynjolfsson, Erik, Danielle Li, and Lindsey R. Raymond. "Generative AI at Work." *The Quarterly Journal of Economics*, Vol. **140**, Issue **2**, pp. **889–942**, 2025 (온라인 2024-12-29, 지면 2025-02-04). DOI: `10.1093/qje/qjae044`. 태그: **[PR]**
- 워킹페이퍼: NBER WP **31161**, April 2023, revised **November 2023**. DOI: `10.3386/w31161`. 태그: **[WP]**

**게재본(QJE) 초록 VERBATIM:**
> "We study the staggered introduction of a generative AI–based conversational assistant using data from 5,172 customer-support agents. Access to AI assistance increases worker productivity, as measured by issues resolved per hour, by 15% on average, with substantial heterogeneity across workers. […] Less experienced and lower-skilled workers improve both the speed and quality of their output, while the most experienced and highest-skilled workers see small gains in speed and small declines in quality."
>
> 우리는 **5,172명의 고객지원 상담원** 데이터를 사용해 생성형 AI 기반 대화형 어시스턴트의 시차 도입을 연구한다. AI 지원에 대한 접근은 시간당 해결 건수로 측정한 노동자 생산성을 **평균 15%** 높이며, 노동자 간 이질성이 상당하다. […] **경험이 적고 숙련도가 낮은 노동자는 산출의 속도와 품질을 모두 개선**하는 반면, **가장 경험 많고 숙련도 높은 노동자는 속도에서 작은 이득, 품질에서 작은 하락**을 본다.

**워킹페이퍼(NBER 31161) 초록 VERBATIM:**
> "we study the staggered introduction of a generative AI-based conversational assistant using data from 5,179 customer support agents. Access to the tool increases productivity, as measured by issues resolved per hour, by 14% on average, including a 34% improvement for novice and low-skilled workers but with minimal impact on experienced and highly skilled workers."
>
> 우리는 **5,179명의 고객지원 상담원** 데이터를 사용해 […] 도구 접근은 시간당 해결 건수로 측정한 생산성을 **평균 14%** 높이며, 여기에는 **초보·저숙련 노동자의 34% 개선**이 포함되지만 경험 많고 고숙련인 노동자에 대한 영향은 미미하다.

> ⚠️ **인용 시 주의:** Acemoglu는 **WP 버전의 14%**를 쓴다. QJE 게재본은 **15%(n=5,172)**다. Aghion & Bunel은 **안정화된 25%**를 쓴다. 세 수치가 모두 "같은 연구"에서 나온다. 이 책에서 이 사실 자체를 하나의 절로 다룰 만하다.

#### Dell'Acqua et al. (2026) — BCG 현장실험, Organization Science
- Dell'Acqua, Fabrizio, Edward McFowland III, Ethan Mollick, Hila Lifshitz-Assaf, Katherine Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, and Karim R. Lakhani. "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality." *Organization Science*, Vol. **37**, Issue **2**, pp. **403–423**, **March 2026**. DOI: `10.1287/orsc.2025.21838`. 태그: **[PR]**
- 선행 워킹페이퍼: SSRN, 2023. DOI: `10.2139/ssrn.4573321`. 태그: **[WP]**

**게재본 초록 VERBATIM:**
> "The preregistered experiment involved 758 knowledge workers. After establishing a performance baseline on similar tasks, subjects were randomly assigned to one of three conditions: no AI access, GPT-4 AI access, or GPT-4 AI access with a prompt engineering overview. For each one of a set of 18 realistic knowledge tasks within the frontier of AI capabilities ranging from creative to analytical tasks, subjects using AI outperformed those not using AI, completing 12.2% more tasks and completing them 25.1% more quickly on average while also delivering solutions of significantly improved quality. However, for a complex managerial task selected to be outside the frontier, subjects using AI were 19% less likely to produce correct solutions compared with those without AI, pointing to potential limitations of AI supporting knowledge workers."
>
> 사전등록 실험에는 **758명의 지식노동자**가 참여했다. 유사 과업에서 성과 기준선을 설정한 뒤, 피험자를 세 조건 중 하나에 무작위 배정했다: AI 미접근, GPT-4 접근, GPT-4 접근+프롬프트 엔지니어링 개요. AI 역량의 **프론티어 안**에 있는 창의적~분석적 18개 현실적 지식과업 각각에 대해, AI를 사용한 피험자는 사용하지 않은 이들을 능가하여 **평균 12.2% 더 많은 과업을 완료하고 25.1% 더 빠르게** 완료했으며 **유의하게 개선된 품질의 해법**을 내놓았다. 그러나 **프론티어 밖**으로 선정된 복잡한 관리 과업에서는, AI를 사용한 피험자가 사용하지 않은 이들보다 **정답을 낼 가능성이 19% 낮았다** — AI가 지식노동자를 지원하는 데 있어 잠재적 한계를 시사한다.

> ⭐ **"들쭉날쭉한 프론티어(jagged frontier)"** 개념은 Acemoglu의 "easy-to-learn / hard-to-learn" 구분에 대한 **실험적 확증**이다. 이 책에서 두 문헌을 연결하면 강력하다.

---

### 4-2. 도입률 — 거시 계산의 진짜 병목

#### Bick, Blandin & Deming — "The Rapid Adoption of Generative AI"
- Bick, Alexander, Adam Blandin, and David J. Deming. "The Rapid Adoption of Generative AI." *NBER Working Paper* No. **32966**, **September 2024**, revised **February 2025**. DOI: `10.3386/w32966`. (FRB St. Louis Working Paper 2024-027 병행) 태그: **[WP]**

> "As of late 2024, nearly 40 percent of the U.S. population age 18-64 uses generative AI. 23 percent of employed respondents had used generative AI for work at least once in the previous week, and 9 percent used it every work day. Relative to each technology's first mass-market product launch, work adoption of generative AI has been as fast as the personal computer (PC), and overall adoption has been faster than either PCs or the internet. […] Between 1 and 5 percent of all work hours are currently assisted by generative AI, and respondents report time savings equivalent to 1.4 percent of total work hours. This suggests that substantial productivity gains from generative AI are possible."
>
> **2024년 말 기준, 18~64세 미국 인구의 거의 40%가 생성형 AI를 사용**한다. 취업 응답자의 **23%가 지난 한 주에 최소 한 번 업무에 생성형 AI를 사용**했고, **9%는 매 근무일 사용**했다. 각 기술의 첫 대중시장 제품 출시 시점 대비, 생성형 AI의 **업무 도입은 개인용 컴퓨터(PC)만큼 빨랐고, 전체 도입은 PC나 인터넷보다 빨랐다.** […] **현재 전체 근로시간의 1~5%가 생성형 AI의 지원을 받으며, 응답자들이 보고한 시간 절감은 전체 근로시간의 1.4%에 해당한다.** 이는 생성형 AI로부터 상당한 생산성 이득이 가능함을 시사한다.

> ⭐ **"전체 근로시간의 1.4% 절감"** — 이것이 2024년 말 현재 관측된 **실제 거시 규모**다. Acemoglu의 10년 누적 TFP 0.66%와 비교하면, 확산 초기임을 감안해도 Goldman Sachs의 연 1.5%p와는 자릿수가 다르다. **이 책에서 "지금 실제로 일어나고 있는 일"의 앵커로 쓸 수 있는 가장 좋은 단일 숫자다.**

#### Bonney et al. — 미국 인구조사국 BTOS (2024 → 2026)
- Bonney, Kathryn, Cory Breaux, Cathy Buffington, Emin Dinlersoz, Lucia S. Foster, Nathan Goldschlag, John C. Haltiwanger, Zachary Kroff, and Keith Savage. "Tracking Firm Use of AI in Real Time: A Snapshot from the Business Trends and Outlook Survey." *NBER Working Paper* No. **32319**, **April 2024**. DOI: `10.3386/w32319`. JEL: L23, O31, O33. 태그: **[WP]**
  (관련 게재본: Bonney et al., "The impact of AI on the workforce: Tasks versus jobs?" *Economics Letters*, 2024-09-13, DOI `10.1016/j.econlet.2024.111971` **[PR]**)

> "We provide new, real-time estimates of current and expected future use of AI for business purposes based on the Business Trends and Outlook Survey for September 2023 to February 2024. During this period, bi-weekly estimates of AI use rate rose from 3.7% to 5.4%, with an expected rate of about 6.6% by early Fall 2024. […] AI users often utilize AI to substitute for worker tasks and equipment/software, but few report reductions in employment due to AI use. Many firms undergo organizational changes to accommodate AI, particularly by training staff, developing new workflows, and purchasing cloud services/storage. AI users also exhibit better overall performance and higher incidence of employment expansion compared to other businesses. The most common reason for non-adoption is the inapplicability of AI to the business."
>
> 우리는 2023년 9월~2024년 2월 Business Trends and Outlook Survey에 기반해 사업 목적 AI 사용의 현재 및 예상 미래에 대한 새로운 실시간 추정치를 제공한다. 이 기간 **격주 AI 사용률 추정치는 3.7%에서 5.4%로 상승**했으며, **2024년 초가을까지 약 6.6%**로 예상된다. […] AI 사용 기업은 종종 노동자 과업과 장비/소프트웨어를 대체하는 데 AI를 활용하지만, **AI 사용으로 인한 고용 감소를 보고하는 곳은 거의 없다.** 많은 기업이 AI를 수용하기 위해 조직 변화를 겪는데, 특히 **직원 교육, 신규 워크플로 개발, 클라우드 서비스/스토리지 구매**를 통해서다. AI 사용 기업은 다른 기업 대비 **전반적으로 더 나은 성과와 더 높은 고용 확대 발생률**을 보인다. 미도입의 가장 흔한 이유는 **AI가 해당 사업에 적용 불가능**하다는 것이다.

- Bonney, Kathryn, Cory L. Breaux, Emin Dinlersoz, Lucia S. Foster, John C. Haltiwanger, and Aditya A. Pande. "The Microstructure of AI Diffusion: Evidence from Firms, Business Functions, and Worker Tasks." *NBER Working Paper* No. **35141**, **April 2026**. DOI: `10.3386/w35141`. 태그: **[WP]**

> "Using novel, nationally representative data from the 2026 AI supplement to the U.S. Census Bureau's Business Trends and Outlook Survey (BTOS), we characterize AI diffusion across three layers: firm-wide adoption, business-function deployment, and worker-task use. During Nov 2025–Jan 2026, 18% of firms used AI in at least one function (32%, employment-weighted), with adoption expected to reach 22% within six months. Use is concentrated in large firms and knowledge-intensive sectors, reaching 50%–60% (60%–70%, employment-weighted) among very large firms in Information, Professional Services, and Finance. Among adopters, scope remains limited: 57% use AI in three or fewer functions, most often Sales and Marketing (52%), Strategy (45%), and IT (41%). Worker-level use appears in 23% (41%, employment-weighted) of firms, primarily for writing, document analysis, and information search; 65% restrict use to three or fewer tasks. […] Most firms (66%) use AI for task augmentation, while employment reductions are rare (2%). Regression results show a positive relationship between firm performance and AI integration breadth. However, functional deployment and operational investment are associated with employment declines, while worker-task use is not once these factors are controlled for."
>
> 미국 인구조사국 BTOS의 2026년 AI 부록에서 나온 새로운 전국 대표 데이터를 사용해, 우리는 **기업 전체 도입, 업무기능 배치, 노동자 과업 사용**의 세 층위로 AI 확산을 특징짓는다. **2025년 11월~2026년 1월, 기업의 18%가 최소 하나의 기능에서 AI를 사용**했고(**고용가중 32%**), 6개월 내 도입률이 **22%**에 이를 것으로 예상된다. 사용은 대기업과 지식집약 부문에 집중되어, 정보·전문서비스·금융의 초대형 기업에서는 **50~60%(고용가중 60~70%)**에 이른다. 도입 기업 중에서도 범위는 제한적이다: **57%가 세 개 이하 기능에서만** AI를 사용하며, 가장 흔한 것은 **영업·마케팅(52%), 전략(45%), IT(41%)**다. 노동자 수준 사용은 기업의 **23%(고용가중 41%)**에 나타나며 주로 글쓰기·문서 분석·정보 검색이고, **65%는 세 개 이하 과업**으로 제한한다. […] **대부분의 기업(66%)은 과업 증강(augmentation)에 AI를 사용**하고, **고용 감축은 드물다(2%)**.

> ⭐ **이 논문 하나로 "AX 도입의 폭 vs 깊이"를 정량화할 수 있다.** 도입했다고 해도 3개 기능 이하가 57%. Acemoglu가 말한 "AI 영향 GDP 비중 4.6%"의 현실 세계 대응물이 바로 이것이다.

---

### 4-3. 기업 수준 TFP 증거 (2023–2026)

#### Czarnitzki, Fernández & Rammer (2023) — 독일 기업 패널
- Czarnitzki, Dirk, Gastón P. Fernández, and Christian Rammer. "Artificial intelligence and firm-level productivity." *Journal of Economic Behavior & Organization*, Vol. **211**, pp. **188–205**, **2023-05-12**. DOI: `10.1016/j.jebo.2023.05.008`. 태그: **[PR]**

> "We exploit unique survey data on firms' adoption of AI technology and estimate its productivity effects with a sample of German firms. We employ both a cross-sectional dataset and a panel database. To address the potential endogeneity of AI adoption, we also implement IV estimators. We find positive and significant associations between the use of AI and firm productivity. This finding holds for different measures of AI usage, i.e., an indicator variable of AI adoption, and the intensity with which firms use AI methods in their business processes."
>
> 우리는 기업의 AI 기술 도입에 관한 고유 설문 데이터를 활용해 **독일 기업 표본**으로 그 생산성 효과를 추정한다. 횡단면 데이터셋과 패널 데이터베이스를 모두 사용한다. AI 도입의 잠재적 내생성을 다루기 위해 **IV 추정량**도 적용한다. 우리는 **AI 사용과 기업 생산성 사이에 양(+)이고 유의한 연관**을 발견한다. 이 결과는 AI 사용의 여러 측정치 — AI 도입 지시변수, 기업이 업무 프로세스에서 AI 방법을 사용하는 강도 — 에 대해 유지된다.

#### Baslandze et al. (2026) — 미국 기업 임원 서베이 ⭐ 자본심화가 아니라 TFP
- Baslandze, Salomé, Zachary Edwards, John Graham, Ty McClure, Brent H. Meyer, Michael Sparks, Sonya R. Waddell, and Daniel Weitz. "Artificial Intelligence, Productivity, and the Workforce: Evidence from Corporate Executives." *NBER Working Paper* No. **34984**, **March 2026**. 태그: **[WP]**

> "We use novel data from a survey of nearly 750 corporate executives to study the effects of artificial intelligence (AI) on productivity and the workforce. We document substantial heterogeneity in AI adoption across firms, with more than half having already invested, though many smaller firms are only beginning to do so. Labor productivity gains are positive, vary across sectors, and are expected to strengthen in 2026, with the largest effects concentrated in high-skill services and finance. These gains are not primarily driven by firms' capital deepening but instead reflect increases in revenue-based total factor productivity, closely associated with innovation-and demand-oriented channels. We document a productivity paradox, in which perceived productivity gains are larger than measured productivity gains, likely reflecting a delay in revenue realizations."
>
> 우리는 **약 750명의 기업 임원** 설문의 새로운 데이터를 사용해 AI가 생산성과 노동력에 미치는 효과를 연구한다. 기업 간 AI 도입에 상당한 이질성이 있음을 기록하며, **절반 이상이 이미 투자**했지만 많은 소기업은 이제 막 시작하고 있다. 노동생산성 이득은 양(+)이고 부문별로 다르며 2026년에 강화될 것으로 예상되고, **가장 큰 효과는 고숙련 서비스와 금융에 집중**되어 있다. **이 이득은 주로 기업의 자본심화에 의해 추동되는 것이 아니라 매출 기반 총요소생산성(revenue-based TFP)의 증가를 반영**하며, 혁신 및 수요 지향 경로와 밀접히 연관된다. 우리는 **인지된 생산성 이득이 측정된 생산성 이득보다 큰 생산성 역설**을 기록하는데, 이는 매출 실현의 지연을 반영하는 것으로 보인다.

#### Babina, He & Jiang (2026) — 조직자본 경로
- Babina, Tania, Alex X. He, and Renhao Jiang. "Canaries in the Gold Mine: Early Productivity Gains from Artificial Intelligence Creating Organization Capital." *NBER Working Paper* No. **35684**, **August 2026**. 태그: **[WP]**

> "Using a new firm-level measure of AI investment based on AI-skilled employment—spanning machine learning through generative and agentic AI—we show that AI investments are associated with productivity growth in recent years, but not over the previous decade. We trace the productivity gains to the accumulation of organization capital that AI helps create: durable firm-specific knowledge acquired through learning-by-doing that enables more efficient production. […] Overall, our findings suggest that AI investment generates productivity growth by creating organization capital."
>
> AI 숙련 고용에 기반한 새로운 기업 수준 AI 투자 측정치 — 머신러닝부터 생성형·에이전틱 AI까지 포괄 — 를 사용해, 우리는 **AI 투자가 최근 수년간의 생산성 증가와 연관되지만 지난 10년간은 그렇지 않았음**을 보인다. 우리는 그 생산성 이득의 원천을 **AI가 만들어내는 조직자본(organization capital)의 축적** — 즉 **행함으로써 배우기(learning-by-doing)**를 통해 획득되고 더 효율적인 생산을 가능케 하는 지속적 기업 특수 지식 — 으로 추적한다. […] 전반적으로 우리 발견은 **AI 투자가 조직자본을 창출함으로써 생산성 증가를 낳는다**는 것을 시사한다.

> ⭐ **AX 실무에 가장 직접적인 2026년 결과.** "AI를 사는 것"이 아니라 "AI가 조직자본을 만들게 하는 것"이 생산성을 낳는다. Brynjolfsson의 무형자산·J커브 논지의 실증 확인.

#### Yotzov et al. (2026) — 4개국 임원 6,000명
- Yotzov, Ivan, Jose Maria Barrero, Nicholas Bloom, Philip Bunn, Steven J. Davis, Kevin M. Foster, Aaron Jalca, Brent H. Meyer, Paul Mizen, Michael A. Navarrete, Pawel Smietanka, Gregory Thwaites, and Ben Zhe Wang. "Firm Data on AI." *NBER Working Paper* No. **34836**, **February 2026, Revised March 2026**. JEL: E0. 태그: **[WP]**

> "We survey nearly 6,000 senior business executives at US, UK, German, and Australian firms to develop new evidence on AI adoption and its effects on jobs, productivity, and output. […] We find four main results. First, 69% of firms actively use AI, with higher usage rates at younger and more productive firms. Second, more than two thirds of executives regularly use AI, but their usage rate averages only 1.5 hours a week. Third, executives report little own-firm impact of AI over the last 3 years, with nine-in-ten reporting no impact on employment or productivity. Fourth, these same executives predict sizable effects over the next 3 years, predicting that AI will boost productivity at their firms by an average of 1.4%, raise output 0.8%, and cut employment 0.7%. In contrast, employees anticipate that AI will raise employment 0.5% at their firms in the next 3 years, highlighting an expectations gap between employers and employees."
>
> 우리는 미국·영국·독일·호주 기업의 **고위 임원 약 6,000명**을 설문해 AI 도입과 그것이 일자리·생산성·산출에 미치는 효과에 대한 새로운 증거를 개발한다. […] 네 가지 주요 결과를 발견한다. **첫째, 기업의 69%가 적극적으로 AI를 사용**하며, 더 젊고 더 생산적인 기업에서 사용률이 높다. **둘째, 임원의 3분의 2 이상이 정기적으로 AI를 사용하지만 사용률은 주당 평균 1.5시간에 불과**하다. **셋째, 임원들은 지난 3년간 자사에 대한 AI의 영향이 거의 없다고 보고하며, 열 중 아홉이 고용이나 생산성에 영향이 없었다고 답한다.** **넷째, 바로 그 임원들이 향후 3년간 상당한 효과를 예측하는데, AI가 자사 생산성을 평균 1.4% 높이고, 산출을 0.8% 올리며, 고용을 0.7% 줄일 것으로 전망**한다. 반면 직원들은 AI가 향후 3년간 자사 고용을 0.5% 높일 것으로 예상해, **고용주와 피고용인 사이의 기대 격차**를 부각한다.

> ⭐ **"69%가 사용, 주당 1.5시간, 열 중 아홉은 영향 없음"** — 이 세 숫자의 병치가 AX 현실을 가장 잔인하게 요약한다. 도입률 통계와 효과 통계를 혼동하면 안 된다는 결정적 증거.

---

### 4-4. 미시→거시 감쇠(attenuation)의 직접 증거 ⭐ 5번 항목의 핵심 실증

#### Demirer, Musolff & Yang (2026) — "Writing Code vs. Shipping Code"
- Demirer, Mert, Leon Musolff, and Liyuan Yang. "Writing Code vs. Shipping Code: Productivity Effects Across Generations of AI Coding Tools." *NBER Working Paper* No. **35275**, **May 2026** (NBER 목록 표기 June 2026). 태그: **[WP]**

> "We study these questions in the context of software development, using data on more than 100,000 GitHub developers combined with their AI usage telemetry. In a matched event study design, we find that autocomplete, interactive coding agents, and autonomous coding agents each significantly increase coding activity ('commits'), with respective cumulative effects of 40%, 140%, and 180%. These gains, however, attenuate sharply across the production hierarchy: the 180% cumulative effect falls to 50% for the number of projects, and to 30% for actual releases. This pattern is consistent with the weak-link hypothesis: the strong productivity gains from AI are attenuated by human bottlenecks in the production chain, with an estimated elasticity of substitution of 0.25 between AI and human effort, which indicates strong complementarities. We further confirm these results across four major app marketplaces, finding a moderate increase in the number of new apps but no increase in total usage. Large task-level AI productivity gains have therefore translated only partially into shipped and used software thus far."
>
> 우리는 **10만 명 이상의 GitHub 개발자** 데이터를 그들의 AI 사용 텔레메트리와 결합해 소프트웨어 개발 맥락에서 이 질문들을 연구한다. 매칭 이벤트 스터디 설계에서, 자동완성·대화형 코딩 에이전트·자율 코딩 에이전트가 각각 코딩 활동("커밋")을 유의하게 증가시키며 **누적 효과는 각각 40%, 140%, 180%**임을 발견한다. **그러나 이 이득은 생산 위계를 거치며 급격히 감쇠한다: 180%의 누적 효과가 프로젝트 수에서는 50%로, 실제 릴리스에서는 30%로 떨어진다.** 이 패턴은 **약한 고리 가설(weak-link hypothesis)**과 부합한다: AI로부터의 강한 생산성 이득이 생산 사슬의 **인간 병목**에 의해 감쇠되며, **AI와 인간 노력 사이의 대체탄력성 추정치는 0.25**로 강한 **보완성**을 나타낸다. 우리는 나아가 4개 주요 앱 마켓플레이스에서 이 결과를 확인하여, 신규 앱 수는 완만히 증가하지만 **총 사용량은 증가하지 않음**을 발견한다. 따라서 **과업 수준의 큰 AI 생산성 이득은 지금까지 출시되고 사용되는 소프트웨어로는 부분적으로만 전환되었다.**

> ⭐⭐ **이 논문이 5번 항목("왜 추정치가 갈리는가")의 실증적 결정타다.** Peng et al.의 55.8%는 "코드 작성" 수준이고, 최종 산출물(릴리스)에서는 그 효과가 1/6로 감쇠한다. **Hulten 정리와 Baumol 병목이 실제 데이터로 관측된 사례**이며, "AX 파일럿 KPI가 좋았는데 왜 P&L에 안 잡히나"에 대한 가장 정확한 답이다.

#### Humlum & Vestergaard (2026) — 덴마크 행정자료, 정밀 영(null)
- Humlum, Anders, and Emilie Vestergaard. "Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI." *NBER Working Paper* No. **33777**, **May 2025**, revised **March 2026**. DOI: `10.3386/w33777`. 태그: **[WP]**

> "We document rapid currents: most employers in exposed occupations have adopted chatbot initiatives, workers report productivity benefits, and new AI-related tasks are widespread. Yet these currents have not broken the surface: using difference-in-differences, we estimate precise null effects on earnings and recorded hours at both the worker and workplace levels, ruling out effects larger than 2% two years after the launch of ChatGPT. What moves is the structure of work: employers absorb AI through task reorganization—including new tasks in content generation, AI oversight, and AI integration—and adopters transition into higher-paying occupations where AI chatbots are more relevant, though still too few to move average earnings. Technological change reshapes work well before it surfaces in earnings or hours."
>
> 우리는 **빠른 해류**를 기록한다: 노출 직업의 고용주 대부분이 챗봇 이니셔티브를 도입했고, 노동자들은 생산성 편익을 보고하며, 새로운 AI 관련 과업이 널리 퍼져 있다. **그러나 이 해류는 아직 수면을 뚫지 못했다:** 이중차분법을 사용해 우리는 **노동자 수준과 사업장 수준 모두에서 소득과 기록된 노동시간에 대해 정밀한 영(null) 효과를 추정하며, ChatGPT 출시 2년 후 시점에서 2%보다 큰 효과를 배제**한다. 움직이는 것은 **일의 구조**다: 고용주는 콘텐츠 생성·AI 감독·AI 통합의 새로운 과업을 포함한 **과업 재조직**을 통해 AI를 흡수하고, 도입자들은 AI 챗봇이 더 유의미한 고임금 직업으로 이동하지만 평균 소득을 움직이기에는 아직 수가 너무 적다. **기술 변화는 소득이나 노동시간에 드러나기 훨씬 전부터 일을 재편한다.**

#### Dillon, Jaffe, Immorlica & Stanton (2025) — 7,137명 RCT
- Dillon, Eleanor Wiske, Sonia Jaffe, Nicole Immorlica, and Christopher T. Stanton. "Shifting Work Patterns with Generative AI." *NBER Working Paper* No. **33795**, **May 2025**. DOI: `10.3386/w33795`. 태그: **[WP]**

> "Half of the 7,137 workers in the study received access to a generative AI tool integrated into the applications they already used for emails, document creation, and meetings. We find that access to the AI tool during the first year of its release primarily impacted behaviors that workers could change independently and not behaviors that require coordination to change: workers who used the tool in more than half of the sample weeks spent 3.6 fewer hours, or 31% less time on email each week (intent to treat estimate is 1.3 hours) and completed documents moderately faster, but did not significantly change time spent in meetings."
>
> 연구에 참여한 **7,137명 노동자의 절반**이 이메일·문서 작성·회의에 이미 사용 중이던 애플리케이션에 통합된 생성형 AI 도구에 접근했다. 우리는 출시 첫해 AI 도구 접근이 주로 **노동자가 독립적으로 바꿀 수 있는 행동**에 영향을 미쳤고 **변화에 조율이 필요한 행동**에는 그렇지 않았음을 발견한다: 표본 주간의 절반 이상에서 도구를 사용한 노동자는 매주 이메일에 **3.6시간 적게, 즉 31% 적은 시간**을 썼고(**ITT 추정치는 1.3시간**) 문서를 완만히 빠르게 완료했지만, **회의 시간은 유의하게 바꾸지 못했다.**

> ⭐ **"혼자 바꿀 수 있는 것은 바뀌었고, 조율이 필요한 것은 안 바뀌었다."** AX가 조직 재설계 문제라는 명제의 실험적 증거.

---

## 5. ⭐ 상충하는 추정치 비교표

**주의:** 아래는 서로 다른 정의(TFP vs 노동생산성, 10년 누적 vs 연간, 조건부 vs 무조건부)를 담고 있으므로 열 이름을 반드시 함께 읽어야 한다.

| 출처 | 추정치 | 기간 | 핵심 가정 (노출 × 수익성 × 절감률 × 노동분배율) | 발산 원인 |
|---|---|---|---|---|
| **Acemoglu (2025, EP; NBER WP 32487)** [PR/WP] | **10년 누적 TFP +0.66%** (연 +0.064%p) / hard 조정 시 **+0.53%** / GDP +0.93~1.16% (투자붐 시 1.4~1.56%) | 10년 | **0.200 × 0.23 × 0.27 × 0.535 = 0.0066** | 수익성 필터 23%를 **10년 내내 고정**(비용 하락 0). Brynjolfsson **14%** 채택, Peng 55.8% **제외**. 신규 과업 **불산입**. |
| **Acemoglu (MIT 2024-04 초고)** [WP] | 10년 TFP **+0.71%** / hard 조정 **+0.55%** / GDP 1.1%·0.92% | 10년 | 0.199 × 0.23 × 0.27 × **0.57** | 게재본과의 유일한 실질 차이 = **노동분배율 0.57 vs 0.535** |
| **Aghion & Bunel (2024-06)** [WP] | **연 TFP +0.68%p** (구간 0.07~1.24%p); 역사유비 접근 **연 +0.8~1.3%p** | 10년 | **0.60 × 0.50 × 0.40 × 0.57 = 0.0684** | ① 노출도를 과업(20%)이 아닌 **능력 기반 60%**로 교체 ② 비용 **연 22% 하락** 반영해 수익성 필터 23→**50%** ③ Peng 포함해 절감률 27→**40%** |
| **Goldman Sachs, Briggs & Kodnani (2023-03)** [WP] | 미국 **노동생산성 연 +1.5%p**(범위 0.3~3.0), 세계 **연 +1.4%p**, **세계 GDP +7%(≈$7조)** | "광범위 도입 **이후**" 10년 | 노출 **직업 2/3**, 업무 **1/4** 대체 가능, 세계 고용가중 **18%**, 완전대체 노동자 7% | 수익성 필터 **없음**. 도입 시점 **미추정**(조건부). 20년이면 절반·30년이면 1/3로 축소됨을 스스로 명시. |
| **Baily, Brynjolfsson & Korinek (2023-05, Brookings)** [WP] | **총생산성·산출 +18%** (10~20년 분산) + 아이디어 생산 경로로 성장률 2%→**2.4%** | 10~20년 | 인지노동 생산성 **+30%** × 인지노동 부가가치 비중 **60%** | 노출 필터·수익성 필터·도입률이 **모두 없음**. 대신 Acemoglu가 뺀 **신규 아이디어 생산 경로를 포함**. |
| **OECD, Filippucci·Gál·Schief (2024-11)** [WP] | **연 TFP +0.25~0.6%p** (노동생산성 **+0.4~0.9%p**) | 10년 | 미시 성과이득 × 노출도 × **향후 도입률 경로**, **다부문 일반균형 + 투입산출 총계화** | Hulten 1차 근사 대신 **부문 간 연관·재배분**을 모형화. 도입률을 **명시적 시나리오**로 내생화. |
| **OECD, Filippucci et al. (2025-06, G7)** [WP] | 고노출·고도입국(미·영) **연 노동생산성 +0.4~1.3%p**; 여타 G7 최대 **50% 작음** | 10년 | 도입률 상승 **23% / 40% / 60%** (전기·ICT·휴대전화 확산 경로 대응) | 국가별 **부문 구성**과 **도입 속도**가 차이를 만듦 |
| **OECD (2025-12, 예고 연구)** [WP] | 보완 요소가 적은 국가 **연 +0.05~0.3%p** | 10년 | 보완적 요소(기술·데이터·자본) 부족 | **보완 자산 부재**가 이득을 소멸시킴 |
| **IMF, Cazzaniga et al. (2024-01, SDN/2024/001)** [WP] | 정상상태 간 **산출 +16%, TFP +4%** (고보완·고생산성 시나리오); 저보완 시 산출 +10% | 정상상태 간(이득의 대부분은 첫 10년) | 노출 **세계 40%·선진국 60%·신흥 40%·저소득 26%**; 노동분배율 **−5.5%p**; 생산성은 **연 1.5%p 상승하도록 캘리브레이션** | 생산성 값이 **독립 추정이 아니라 GS 값의 이식**. 산출 증가의 상당 부분이 **자본심화**(TFP 4% vs 산출 16%). |
| **McKinsey Global Institute (2023)** — Acemoglu 인용 경유 [WP] | 세계경제에 **$17.1조~$25.6조** 부양; AI+자동화 전체로 선진국 연평균 GDP 성장 **+1.5~3.4%p** | "향후 10년" | (Acemoglu 논문 §1에서 재인용) | 대체 가능 업무 시간 비중을 그대로 성장으로 환산 |
| **Bick, Blandin & Deming (2024-09/2025-02)** [WP] — *예측이 아닌 관측치* | **실제 시간 절감 = 전체 근로시간의 1.4%**; 근로시간의 1~5%만 AI 지원 | 2024년 말 현시점 | 전국 대표 설문 | **추정이 아니라 측정.** 낙관 추정의 현실 대조군. |
| **Yotzov et al. (2026-02/03)** [WP] — *관측+임원 전망* | 지난 3년: **열 중 아홉이 영향 없음**; 향후 3년 전망: 생산성 **+1.4%**, 산출 **+0.8%**, 고용 **−0.7%** | 과거 3년 / 향후 3년 | 4개국 임원 6,000명, **주당 1.5시간 사용** | 도입률(69%)과 효과(≈0)의 괴리 |
| **Demirer, Musolff & Yang (2026-05)** [WP] — *감쇠 계수* | 커밋 **+180%** → 프로젝트 **+50%** → **릴리스 +30%**; AI-인간 대체탄력성 **0.25** | 관측 기간 | GitHub 개발자 10만+ | **미시→거시 감쇠율 ≈ 1/6.** 과업 이득을 그대로 총계화하면 안 되는 이유. |
| **Humlum & Vestergaard (2025-05/2026-03)** [WP] — *정밀 영* | 소득·노동시간에 **정밀한 null**, **2% 초과 효과 배제** | ChatGPT 출시 후 2년 | 덴마크 행정자료 + 도입 설문 | 도입은 빠른데 **거시 지표엔 아직 미도달** |

---

## 6. 왜 이렇게 갈리는가 — 발산의 해부

### 6-1. 발산의 90%는 곱셈 항 네 개에서 나온다

Acemoglu와 Aghion & Bunel은 **완전히 동일한 산식**을 쓴다.

```
연간 TFP 기여 = (AI 노출 과업의 GDP 비중)
              × (노출 과업 중 AI 사용이 수익성 있는 비중)
              × (평균 노동비용 절감률)
              × (AI 노출 조정 노동소득분배율)
```

| 항 | Acemoglu | Aghion & Bunel | 배율 |
|---|---|---|---|
| 노출도 | 0.200 | **0.60** | **3.0×** |
| 수익성 | 0.23 | **0.50** | **2.2×** |
| 절감률 | 0.27 | **0.40** | **1.5×** |
| 노동분배율 | 0.535 | 0.57 | 1.07× |
| **곱** | **0.0066** | **0.0684** | **≈10.4×** |

**곱셈 구조이기 때문에, 각 항의 "합리적 범위 내" 선택 3개가 겹치면 10배가 된다.** 아무도 비합리적인 값을 쓰지 않았는데 결론이 10배 갈린다 — 이것이 이 논쟁의 본질이다.

### 6-2. 항별 발산 원인의 정체

#### (1) 노출도 — 측정 단위의 문제 (3배)
Acemoglu는 Eloundou et al.의 **과업(task) 기반** 측정을 임금총액 가중으로 GDP 비중으로 환산해 **19.9~20%**를 얻는다. Aghion & Bunel은 Pizzinelli et al.의 **능력(abilities) 기반** 측정 **60%**를 쓴다. IMF도 능력 기반이며 선진국 **60%**다.

이 둘은 **다른 것을 재고 있다.** 과업 기반은 "LLM이 이 과업의 소요시간을 유의하게 줄이는가"를 묻고, 능력 기반은 "이 직업에 필요한 능력들이 AI가 잘하는 능력과 겹치는가"를 묻는다. 후자가 훨씬 관대하다. Aghion & Bunel 스스로 "이 연구는 노출 과업의 GDP 비중이 아니라 노출 과업 비중만 제공한다"고 인정하면서, 그 둘이 비슷할 것이라고 **가정**한다.

> **책에 쓸 표현:** IMF의 "선진국 일자리 60%가 AI에 노출"과 Acemoglu의 "미국 노동 과업 20%가 AI에 노출"은 **모순이 아니다. 다른 질문의 답이다.** 한국 언론에서 두 수치가 자주 충돌하는 것처럼 인용되는데, 그것은 오독이다.

#### (2) 수익성 필터 — 비용 하락을 0으로 볼 것인가 (2.2배)
Acemoglu는 Svanberg et al.의 컴퓨터 비전 연구에서 **"현재 비용 기준 수익성 있는 과업 23%"**를 가져와 **10년간 고정**한다. Aghion & Bunel은 이를 정면으로 지적한다 — "이는 향후 10년간 AI 도입의 비용 절감 진보가 0이라고 가정하는 것과 같다."

Aghion & Bunel은 Besiroglu & Hobbhahn의 **연 22% 컴퓨팅 비용 하락**을 넣어 10년 후 **50%**를 쓴다. Acemoglu 본인도 연 10% 하락 시나리오에서 23%→30%, TFP 0.66%→0.9%가 됨을 계산해 두었다(하지만 채택하지 않는다).

**여기가 가장 중요한 분기점이다.** AI 추론 비용이 실제로 얼마나 빨리 떨어졌는가는 2024~2026년에 상당히 관측 가능해졌고, 이 항의 값이 이 논쟁의 향후 승패를 결정한다.

#### (3) 절감률 — 어느 연구의 어느 시점을 읽을 것인가 (1.5배)
같은 세 연구(Peng 55.8%, Noy–Zhang 40%, Brynjolfsson 14%/15%/25%)를 놓고:
- Acemoglu: Peng **제외**(과업이 너무 협소), Brynjolfsson은 **첫 달 14%** → 평균 **27%**
- Aghion & Bunel: Peng **포함**, Brynjolfsson은 **안정화된 25%** → 평균 **40%**

이 하나만으로 **1.5배**다. 그리고 Acemoglu는 여기에 더해 **"어려운 과업 = 쉬운 과업의 1/4(7%)"**이라는 조정을 추가로 곱한다(0.66%→0.53%).

#### (4) 노동소득분배율 — 아무도 논쟁하지 않는데 개정폭의 전부를 설명한 항 (1.07배)
Acemoglu 자신의 0.71%→0.66% 개정은 거의 전적으로 **0.57 → 0.535**에서 나왔다. Aghion & Bunel은 구버전 값 0.57을 그대로 썼다. 즉 두 논문의 비교조차 완전히 동일 기준이 아니다.

### 6-3. 산식 밖의 발산 요인 — 더 근본적인 다섯 가지

#### (a) 시계(視界)와 GPT 확산 지체 — 조건부인가 무조건부인가
Goldman Sachs의 "연 1.5%p"는 **"광범위한 도입 이후(following widespread adoption)"의 10년**이다. 즉 **조건부 서술**이며, 그 조건이 언제 성립하는지는 추정하지 않는다. GS 스스로 **20년이면 절반, 30년이면 1/3**이 된다고 명시한다.

Acemoglu의 0.66%는 **지금부터의 10년**이라는 **무조건부 서술**이다. 그리고 그는 J커브의 평탄 구간이 디지털 기술의 경우 최소 20년이라는 선행 연구를 근거로 "14.4% 비용 절감조차 향후 10년에 대해서는 상당한 과대추정일 수 있다"고 덧붙인다.

Aghion & Bunel은 반대 방향으로 유비를 쓴다 — 전기의 30년 지연을 인정하되, **통계적 머신러닝의 시작을 1990년대로 잡으면 "30년 후"가 곧 2020년대**라고 계산한다. **같은 역사적 사실(30년 지연)로 정반대 결론에 도달한다.**

> **책에 쓸 표현:** "10년"이라는 같은 단어가 세 문헌에서 각각 **지금부터 10년 / 도입 완료 후 10년 / 전환기 첫 10년**을 뜻한다. 숫자를 나란히 놓기 전에 시계를 맞춰야 한다.

#### (b) 신규 과업·신제품을 셀 것인가 — Hulten 정리의 성립 조건
Hulten 정리는 **기존 과업의 한계적 비용 절감**에 대한 1차 근사다. 신규 과업·신제품은 근사에서 빠져 있다.

- **Acemoglu:** 명시적으로 제외하고, 오히려 **"나쁜 새 과업"**(딥페이크·조작적 광고·중독성 SNS)이 GDP를 올리면서 후생을 낮출 수 있다고 계산한다(GDP +2%, 후생 −0.72%).
- **Aghion & Bunel:** 자기 추정치가 "AI가 **아이디어 생산**도 자동화한다는 사실을 반영하지 않으므로 **하한**"이라고 명시한다. 이 경로는 레벨이 아니라 **성장률 자체**를 항구적으로 올린다.
- **Baily·Brynjolfsson·Korinek:** 이 경로를 **적극적으로 포함**하며, 인지노동 20% 향상 → 생산성 증가율 2%→2.4%라는 예시를 든다.

**이것이 가장 근본적인 분기다.** 레벨 효과(일시적)와 성장률 효과(항구적)는 수학적으로 다른 대상이다. Acemoglu는 전자만 재고, Aghion과 Brookings 팀은 후자를 이야기한다. **두 진영은 사실상 다른 변수를 추정하고 있다.**

#### (c) 자본심화 vs TFP — 무엇을 "생산성"이라 부를 것인가
- **Acemoglu:** TFP를 재고, GDP는 자본소득분배율로 나눠 파생시킨다(×1.75). 그리고 **"후생에 관련된 것은 GDP가 아니라 TFP"**라고 못 박는다 — 추가 투자는 소비에서 나오고, 에너지 사용 증가는 GDP에 잡히되 후생 개선이 아니기 때문.
- **Goldman Sachs:** **노동생산성**을 잰다. 노동생산성은 TFP + 자본심화이므로 정의상 더 크다.
- **IMF:** 정상상태 산출 +16%인데 **TFP는 +4%뿐**이다. 나머지는 자본심화다.
- **OECD:** TFP 0.25~0.6%p ↔ 노동생산성 0.4~0.9%p로 **두 값을 나란히 제시**한다. 비율 약 1.5~1.6배.
- **Baslandze et al. (2026):** 관측된 기업 수준 이득이 **자본심화가 아니라 매출 기반 TFP**에서 온다고 보고 — Acemoglu 쪽 개념에 가까운 실증.

> **책에 쓸 표현:** "생산성이 1.5% 오른다"는 문장을 볼 때마다 물어야 한다 — **TFP인가, 노동생산성인가.** 한국 언론과 컨설팅 보고서는 이 둘을 거의 구별하지 않는다. 1.5~1.6배 차이가 여기서 발생한다.

#### (d) 미시→거시 외삽: Baumol 병목과 약한 고리 — 2026년의 새 증거
Hulten 정리는 **"과업 z의 비용이 π만큼 싸지면 총 효과는 π × (z의 GDP 비중)"**이라고 말한다. 이는 **자동화되지 않은 과업이 병목이 된다**는 뜻이다. Baumol의 비용병(cost disease)과 같은 논리 — 싸진 것의 비중은 줄고, 안 싸진 것의 비중이 커진다.

Acemoglu가 과업 간 대체탄력성 σ<1(총보완재, gross complements)을 가정한 것도 같은 취지다.

**2026년 Demirer, Musolff & Yang이 이를 직접 측정했다:** 코딩 활동 +180% → 프로젝트 +50% → **실제 릴리스 +30%**. AI-인간 노력 간 **대체탄력성 0.25**. 즉 **과업 수준 이득의 약 1/6만 최종 산출물로 통과한다.**

Dillon et al.(2025)의 결과도 같은 방향이다 — 이메일(혼자 바꿀 수 있음)은 31% 줄었지만 **회의(조율 필요)는 안 줄었다.**

> **책에 쓸 표현:** AX 파일럿에서 "80% 시간 단축"이 나왔다면, 그것을 회사 전체 원가에 곱하는 것은 **Hulten 정리를 정확히 반대로 쓰는 것**이다. 물어야 할 질문은 "그 과업이 우리 원가의 몇 %인가"와 "그 다음 공정은 얼마나 빨라졌는가"다.

#### (e) 노출도(exposure) ≠ 도입(adoption) ≠ 효과(effect)
이 셋의 혼동이 대중적 논의에서 가장 큰 오차를 만든다. 2024–2026년 관측 데이터가 이 세 층위를 분리해준다:

| 층위 | 수치 | 출처 |
|---|---|---|
| **잠재 노출** | 선진국 일자리 60% / 미국 과업 20% | IMF 2024 / Eloundou via Acemoglu |
| **수익성 필터 통과** | 노출 과업의 23% (→ 전체의 4.6%) | Svanberg et al. via Acemoglu |
| **기업 도입 (2024초)** | 3.7% → 5.4% | Bonney et al. 2024 |
| **기업 도입 (2026초)** | 18% (고용가중 32%), 57%는 3개 기능 이하 | Bonney et al. 2026 |
| **기업 도입 (임원 자기보고)** | 69% "적극 사용", **주당 1.5시간** | Yotzov et al. 2026 |
| **개인 사용 (2024말)** | 인구 40%, 취업자 주간 23%, 매일 9% | Bick et al. 2024/2025 |
| **실제 시간 절감** | **전체 근로시간의 1.4%** | Bick et al. |
| **소득·노동시간 효과** | **정밀한 null, 2% 초과 배제** | Humlum & Vestergaard |
| **기업 자기보고 효과 (과거 3년)** | **열 중 아홉이 "영향 없음"** | Yotzov et al. 2026 |

> **이 표 하나가 이 책에서 가장 유용한 자산일 수 있다.** "AI가 일자리의 60%에 영향을 준다"에서 "실제로 근로시간의 1.4%가 절감됐다"까지, 각 층위의 필터가 무엇인지 보여준다.

### 6-4. 종합: 2026년 9월 현재 어느 쪽이 이기고 있는가

**단기(관측된 것)에서는 Acemoglu 쪽이 옳았다.**
- Bick et al.: 근로시간 절감 1.4%
- Humlum & Vestergaard: 소득·노동시간 **정밀한 null**, 2% 초과 배제
- Yotzov et al.: 임원 열 중 아홉이 "지난 3년 영향 없음"
- Demirer et al.: 과업 이득의 1/6만 최종 산출물로 통과
- Bonney et al. 2026: 도입 기업의 57%가 3개 기능 이하

**그러나 그 이유는 Acemoglu의 산식이 맞아서가 아니라, 아직 J커브의 평탄 구간이기 때문일 수 있다.** 그리고 2026년의 새 증거들은 낙관론 쪽 메커니즘도 지지한다:
- Babina, He & Jiang: AI 투자 → **조직자본** → 생산성 증가 (최근 수년에만 관측)
- Baslandze et al.: 관측된 이득이 자본심화가 아니라 **매출 기반 TFP**, "인지된 이득 > 측정된 이득"의 **생산성 역설**
- Yotzov et al.: 같은 임원들이 **향후 3년 +1.4% 생산성**을 전망

**즉 데이터는 "효과가 없다"가 아니라 "효과가 아직 지표에 도달하지 않았다"를 말한다.** Humlum & Vestergaard의 마지막 문장이 이 국면을 가장 정확히 요약한다:

> "Technological change reshapes work well before it surfaces in earnings or hours."
> 기술 변화는 소득이나 노동시간에 드러나기 **훨씬 전부터** 일을 재편한다.

**책의 논지로 정리하면:** AX의 거시 효과에 대한 논쟁은 "AI가 대단한가"의 논쟁이 아니라 **"보완 자산(조직자본·워크플로·역량·경쟁 환경)이 얼마나 빨리 축적되는가"의 논쟁**이다. Acemoglu의 낮은 값은 보완 자산 축적을 사실상 0으로 놓은 결과이고, Goldman Sachs의 높은 값은 그것을 이미 끝났다고 가정한 결과다. OECD의 중간값(연 0.25~0.6%p TFP)이 도입률을 명시적 시나리오로 내생화했다는 점에서 **가장 방어 가능한 앵커**다. 그리고 OECD 2025-12의 경고 — 보완 요소가 적은 국가는 **연 0.05~0.3%p**에 그친다 — 가 한국에 가장 직접적인 함의다.

---

## ⚠️ 미확인 항목

1. **Aghion & Bunel (2024), "AI and Growth: Where Do We Stand?" — 정식 게재 여부·학술지·시리즈 번호 미확인.** 확인된 것: 2024년 6월자 PDF가 `https://www.frbsf.org/wp-content/uploads/AI-and-Growth-Aghion-Bunel.pdf`에 호스팅되어 있고(HTTP 200, Content-Type: application/pdf, Last-Modified 2024-08-03), FRBSF에 관련 행사 페이지("Philippe Aghion: The Growth and Employment Effects of AI", 2024-04)가 존재한다. **논문 표지·본문 어디에도 시리즈명이나 게재 정보가 없다.** OpenAlex·Crossref 어디에서도 이 제목이 검색되지 않았다. → **인용 시 "unpublished note, June 2024, hosted by FRBSF"로 표기하고 URL을 병기할 것.** 서지 확인 필요.

2. **Dell'Acqua et al. 워킹페이퍼 버전의 "품질 40% 향상" 수치 — 미확인.** 게재본(Organization Science 2026)은 "delivering solutions of significantly improved quality"라고만 쓰고 구체적 %를 초록에 넣지 않았다. SSRN(4573321)과 HBS Working Paper 24-013 원문은 모두 403으로 접근 실패. **"40% 이상 높은 품질"은 널리 인용되지만 이번 조사에서 1차 출처로 확인하지 못했다.** 서지·수치 확인 필요.

3. **Hémous 논평의 "연 0.066%p" 수치 — 원문 대조 미완.** Oxford Academic 초록 페이지 기반 요약에서 "adding merely 0.066 percentage points to annual TFP growth"로 나왔으나, Acemoglu 원문(NBER/게재본)은 **0.064%**로 명시한다. Hémous 논평 전문(pp. 65–69)은 유료장벽으로 열지 못했다. **인용 시 Acemoglu 원문의 0.064%를 쓰고, Hémous 값은 대조 후 사용할 것.**

4. **Coeuré 논평 전문 미확인.** pp. 59–64, DOI `10.1093/epolic/eiae055`는 확인. 본문 내용은 초록 페이지 기반 요약만 확보했으며, 직접 인용 가능한 verbatim 문장은 "a consistent macro framework to describe the channels through which AI impacts the economy" 한 구절뿐이다.

5. **OECD "Miracle or Myth?" (2024-11) 본문 미열람.** 초록의 수치(연 TFP 0.25~0.6%p, 노동생산성 0.4~0.9%p)는 OpenAlex를 통해 verbatim 확인. **다만 이들이 Acemoglu와의 차이를 어떤 가정 차이로 설명하는지는 본문을 못 봐서 확인하지 못했다.** OECD 서버·iLibrary 모두 403. 서지 확인 필요.

6. **OECD "Macroeconomic productivity gains from AI in G7 economies" (2025-06) 본문 미열람.** 초록만 verbatim 확보. **국가별(특히 한국은 G7이 아니므로 미포함) 수치는 확인 못했다.**

7. **OECD 2025-12 논문이 인용한 "Forthcoming OECD work (Filippucci et al., 2025)"의 연 0.05~0.3%p 수치 — 원 출처 미발표.** 인용 시 "OECD(2025-12)가 인용한 미발표 연구"임을 밝힐 것.

8. **BIS Annual Economic Report 2024 Chapter III에는 거시 TFP/GDP 추정 범위의 구체적 수치가 없다.** 그림·표에 수치가 있을 가능성이 있으나 HTML 페이지에서는 추출되지 않았다. PDF 직접 링크(`ar2024e3.pdf`) 시도 실패. **BIS 워킹페이퍼 중 AI-생산성 수치를 담은 것이 별도로 있을 수 있으나, 이번 세션에서 웹 검색 예산 소진으로 탐색하지 못했다.**

9. **McKinsey Global Institute (2023) 수치($17.1조~$25.6조, 연 GDP 성장 +1.5~3.4%p)는 Acemoglu 논문을 경유한 2차 인용이다.** McKinsey 원문("The economic potential of generative AI: The next productivity frontier", 2023)을 직접 확인하지 않았다. 원문 대조 필요.

10. **Goldman Sachs 보고서는 Internet Archive 사본(20페이지 PDF)으로 확인했다.** 원본 GS 배포본(gspublishing.com)은 403. Archive 사본 표지에 "For the exclusive use of GIULIA.LORIA@COMMUNITY.IT" 워터마크가 있어 **개인 배포본의 아카이브**로 보인다. 서지 자체(제목·저자·2023-03-26 9:05PM EDT·Global Economics Analyst)와 인용한 모든 수치는 그 PDF 본문에서 verbatim 확인했으나, **공식 배포본과의 판본 차이 가능성은 배제하지 못했다.**

11. **Bonney et al. NBER 32319의 게재본** — *Economics Letters*(2024-09-13, DOI `10.1016/j.econlet.2024.111971`)로 제목이 바뀌어 게재("The impact of AI on the workforce: Tasks versus jobs?")된 것을 서지 수준에서 확인했으나, **게재본의 수치가 WP와 동일한지는 대조하지 않았다.**

12. **Demirer, Musolff & Yang (NBER 35275)의 발행월 표기 불일치** — NBER 논문 페이지는 "May 2026", NBER 검색 API 목록은 "June 2026"으로 표시된다. 인용 시 논문 페이지 기준 **May 2026**을 권장하되 확인 필요.

13. **Acemoglu 원문의 "0.046% number for the share of GDP impacted by AI" 표기** — 문맥상 0.046(=4.6%)이어야 하나 원문에 "0.046%"로 표기되어 있다. **오식으로 보이나 원문 그대로 인용했다.** 게재본(Economic Policy)에서 정정되었는지 확인 필요.

14. **Acemoglu 초록의 hard-task 조정 GDP 값 "0.90%"와 본문 §3.4의 "0.93%" 불일치** — 두 값이 같은 NBER PDF 안에 공존한다(초록은 §3.6의 부문 간 대체 반영 후 값, 본문 §3.4는 단순 자본계수 환산 값으로 추정되나, §3.6 본문을 완독하지 못해 확정하지 못했다). **인용 시 어느 값인지 반드시 밝힐 것.**