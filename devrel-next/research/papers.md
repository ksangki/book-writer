# 논문 리서치: AI 시대 DevRel의 변화

> 검색 시점: 2026-09-25 · 담당: paper-researcher · genre: tech-book
> 규율: 수치는 원문(abstract 또는 본문)에서 확인한 것만. 표본·방법·문헌 유형 라벨 필수. 확인 못 한 것은 [미확인].
> 축: A(DevRel·생태계·DX) / B(비개발자·AI 코딩) / C(Stack Overflow 감소) / D(에이전트가 문서를 읽는다) / E(조직 확산·챔피언) / F(OSS 커뮤니티)

---

## [C] 논문 1: Large language models reduce public knowledge sharing on online Q&A platforms
- 저자·연도: R. Maria del Rio-Chanona, Nadzeya Laurentsyeva, Johannes Wachs (2024)
- 발표처: PNAS Nexus, Vol. 3, Issue 9 (2024-09)
- DOI/arXiv: https://doi.org/10.1093/pnasnexus/pgae400 · 프리프린트 arXiv:2307.07367 (v1 2023-07-14, 제목 "Are Large Language Models a Threat to Digital Public Goods? Evidence from Activity on Stack Overflow")
- 문헌 유형: peer-reviewed 저널 (프리프린트 선행)
- 표본·방법: Stack Overflow 활동 vs 반사실 비교군(러시아어 Stack Overflow, 중국 SegmentFault — ChatGPT 접근 제한; Math Stack Exchange·MathOverflow — ChatGPT 역량 낮음). 차분의 차분(DiD) 회귀.
- 요약: ChatGPT 출시와 맞물려 Stack Overflow 활동이 줄었고, 이 감소가 ChatGPT 특유의 효과인지 비교군으로 검증했다. 저자들은 추정치를 실제 영향의 "하한(lower bound)"으로 해석한다. 프리프린트는 게시물 품질이 유지됐다고 보고 — 저품질 중복만 빠진 게 아니라 유용한 콘텐츠가 대체됐다는 해석. 결론: LLM이 개인 문제 해결은 돕지만 미래 모델 학습용 공공 지식(디지털 공공재)을 줄인다.
- 핵심 수치·결과 (2024 게재본 abstract 기준): "Within 6 months of ChatGPT's release, activity on Stack Overflow decreased by 25% relative to its Russian and Chinese counterparts ... and to similar forums for mathematics." (2022-11 출시 후 6개월)
  - 프리프린트 v1(2023-07) abstract 기준: 주간 게시물 16% 감소, 시간이 갈수록 효과 확대, 많이 쓰이는 언어에서 더 큼.
- 인용할 만한 문장: "We interpret this estimate as a lower bound of the true impact of ChatGPT on Stack Overflow."
- "{연도} 기준": 2024 게재본 / 데이터 2022-11~2023-05(6개월 창)
- 독자 전달 제안: DevRel이 "커뮤니티 Q&A에서 답을 다는" 전통적 활동의 무대가 줄어든 근거. 16%(프리프린트)와 25%(게재본)를 섞지 말 것 — 게재본 25%를 쓰고 "상대적 감소·6개월·DiD 추정·하한" 라벨을 붙인다.

---

## [C] 논문 2: The consequences of generative AI for online knowledge communities
- 저자·연도: Gordon Burtch, Dokyun Lee, Zhichen Chen (2024)
- 발표처: Scientific Reports, Vol. 14, Article 10413 (2024-05-06)
- DOI/arXiv: https://doi.org/10.1038/s41598-024-61221-0 (PMC11074245, 오픈 액세스 CC BY; SSRN 4521754 선행)
- 문헌 유형: peer-reviewed 저널
- 표본·방법: Stack Overflow 및 Reddit 개발자 커뮤니티 데이터, 2021-10 ~ 2023-03. 준실험(ChatGPT 출시 전후 비교, 주제별 효과 추정).
- 요약: Stack Overflow는 웹 방문과 질문량이 모두 유의하게 줄었고, 특히 ChatGPT가 잘하는 주제에서 감소가 컸다. 반면 Reddit 개발자 커뮤니티는 감소 증거가 없었다. 저자들은 이를 "사회적 결속(social fabric)"이 LLM의 커뮤니티 약화 효과에 대한 완충재 역할을 한다는 증거로 해석한다. 감소는 신규·주니어 사용자에 집중됐다.
- 핵심 수치·결과 (본문 확인): "We estimate that Stack Overflow's daily web traffic has declined by approximately 1 million individuals per day, equivalent to approximately 12% of the site's daily web traffic just prior to ChatGPT's release."
- 인용할 만한 문장 (abstract): "By contrast, activity in Reddit communities shows no evidence of decline, suggesting the importance of social fabric as a buffer against the community-degrading effects of LLMs." / "the decline in participation on Stack Overflow is found to be concentrated among newer users, indicating that more junior, less socially embedded users are particularly likely to exit."
- "{연도} 기준": 2024 게재 / 데이터 2021-10~2023-03
- 독자 전달 제안: 이 책의 핵심 논거 후보. "정보 교환형" 커뮤니티는 LLM에 대체되고 "관계형" 커뮤니티는 버틴다 — DevRel의 R(Relations)이 왜 살아남는 축인지 설명하는 실증. 단 Reddit 결과는 "감소 증거 없음"이지 "증가"가 아님.

---

## [C] 논문 3: Is Stack Overflow Obsolete? An Empirical Study of the Characteristics of ChatGPT Answers to Stack Overflow Questions
- 저자·연도: Samia Kabir, David N. Udo-Imeh, Bonan Kou, Tianyi Zhang (2024)
- 발표처: CHI '24 (ACM CHI Conference on Human Factors in Computing Systems, Honolulu, 2024-05)
- DOI/arXiv: https://doi.org/10.1145/3613904.3642596 · arXiv:2308.02312 (v1 2023-08-04, v4 2024-02-07)
- 문헌 유형: peer-reviewed 학회 논문
- 표본·방법: Stack Overflow 프로그래밍 질문 517개에 대한 ChatGPT 답변의 정확성·일관성·포괄성·간결성 수동 분석 + 대규모 언어 분석 + 사용자 연구.
- 핵심 수치·결과 (arXiv abstract): ChatGPT 답변의 52%가 부정확한 정보 포함, 77%가 장황. 사용자 연구 참여자는 그럼에도 35%의 경우 ChatGPT 답변을 선호(포괄성·잘 정리된 문체 때문), 39%의 경우 오정보를 알아채지 못함. [사용자 연구 참여자 수: 미확인 — 원문 확인 필요]
- 인용할 만한 문장: "Our analysis shows that 52% of ChatGPT answers contain incorrect information and 77% are verbose."
- "{연도} 기준": ChatGPT(GPT-3.5 계열, 2023 시점) 기준 — 현 모델 성능으로 일반화 금지.
- 독자 전달 제안: "사람이 쓴 정답·검증된 문서"의 가치가 오히려 커지는 근거. 단 2023년 모델 기준 수치라는 신선도 라벨 필수.

---

## [C] 논문 4: LLMs and Stack Overflow Discussions: Reliability, Impact, and Challenges
- 저자·연도: Leuson Da Silva, Jordan Samhi, Foutse Khomh (2024 프리프린트 / 2025 저널)
- 발표처: Journal of Systems and Software (2025) — arXiv 페이지의 관련 DOI 표기 기준 [권·호 미확인]
- DOI/arXiv: arXiv:2402.08801 (v1 2024-02-13, v2 2025-06-20)
- 문헌 유형: 프리프린트 → peer-reviewed 저널
- 요약: ChatGPT·LLaMA 답변을 Stack Overflow 질문으로 평가. "ChatGPT and LLaMA challenge human expertise, yet do not outperform it for some domains"; 동시에 "a significant decline in user posting activity" 관찰. [구체 감소율: 미확인]
- 본문 수치 (arXiv v2 HTML 확인): 제출 답변 수 543,533 (ChatGPT 이전) → 425,391 (이후, -22%) → 출시 1년 이후 구간 202,326 (-52%). 채택 답변이 있는 질문 212,775 → 157,187 → 78,262. 1년 이후 구간에서 댓글 -46%, 질문 -48%. 일부 주제(특정 프레임워크·라이브러리)는 초기에 통계적 감소 없음 — 감소는 주제별로 균일하지 않음. [비교 구간의 길이·정의: 미확인 — 인용 전 본문 방법 절 확인 필수]
- 독자 전달 제안: 보조 근거로. "-52%"는 구간 정의를 확인하기 전에는 쓰지 말 것. 헤드라인 수치는 논문 1·2 사용.
<!-- 정정: 2026-09-25 본문 수치 추가 -->

---

## [B] 논문 5: The Impact of AI on Developer Productivity: Evidence from GitHub Copilot
- 저자·연도: Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer (2023)
- 발표처: arXiv 프리프린트 (Microsoft Research·GitHub·MIT) [저널 게재 여부 미확인]
- DOI/arXiv: arXiv:2302.06590 (v1 2023-02-13)
- 문헌 유형: preprint (통제 실험). 저자에 GitHub 소속 포함 — 이해관계 라벨 권장.
- 표본·방법: 2022년(Copilot 일반 공개 직전) Upwork로 모집한 전문 프로그래머 95명, 무작위로 처치/통제 분리. 과제: JavaScript로 HTTP 서버 구현, 최대한 빠르게. 참가자 평균 코딩 경력 6년.
- 핵심 수치·결과 (본문 확인): 처치군이 55.8% 더 빨리 완료 (95% CI 21–89%, t-test p=0.0017). 완료 조건부 평균 시간: 처치군 71.17분 vs 통제군 160.89분. 경력이 적은 개발자, 하루 코딩 시간이 긴 개발자, 25~44세가 더 큰 혜택.
- 인용할 만한 문장: "Observed heterogenous effects show promise for AI pair programmers to help people transition into software development careers."
- "{연도} 기준": 2022 Copilot(초기) · 단일 그린필드 과제
- 독자 전달 제안: "비개발자·저경력자가 소프트웨어 영역으로 들어오는 문턱이 낮아진다"는 논지의 초기 실증. 단 단일 과제·실험실 조건 — METR 2025(논문 6)와 함께 제시해 "과제 조건에 따라 결과가 뒤집힌다"로 균형.

---

## [B] 논문 6: Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity
- 저자·연도: Joel Becker, Nate Rush, Elizabeth Barnes, David Rein (METR, 2025)
- 발표처: arXiv 프리프린트 (METR 보고서)
- DOI/arXiv: arXiv:2507.09089 (v1 2025-07-12, v2 2025-07-25)
- 문헌 유형: preprint (RCT)
- 표본·방법: 숙련 오픈소스 개발자 16명(AI 경험 중간 수준), 평균 5년 기여 경력의 성숙한 프로젝트에서 실제 과제 246개. 과제별로 AI 허용/불허 무작위 배정. 허용 시 주로 Cursor Pro + Claude 3.5/3.7 Sonnet. 기간: 2025년 2~6월 프런티어 도구.
- 핵심 수치·결과 (abstract): 사전 예측 — 개발자 "24% 단축", 사후 체감 "20% 단축", 경제학 전문가 "39% 단축", ML 전문가 "38% 단축". 실제 — "allowing AI actually increases completion time by 19%". 느려짐 원인 후보 20가지 속성을 점검, 실험 설계 인공물일 가능성은 낮다고 결론.
- 인용할 만한 문장: "Surprisingly, we find that allowing AI actually increases completion time by 19%--AI tooling slowed developers down."
- "{연도} 기준": 2025년 초(2~6월) 도구 기준. 표본 16명 — 일반화 한계 명시 필수.
- 독자 전달 제안: 체감(20% 빨라짐)과 실측(19% 느려짐)의 괴리가 핵심 — DevRel/AX 담당자가 "AI 쓰면 빨라진다"는 서사를 그대로 전파하면 안 되는 이유. 숙련자·대형 성숙 코드베이스라는 조건 라벨을 반드시 붙인다.

---

## [B] 논문 7: Vibe coding: programming through conversation with artificial intelligence
- 저자·연도: Advait Sarkar, Ian Drosos (Microsoft Research, 2025)
- 발표처: PPIG 2025 (36th Annual Conference of the Psychology of Programming Interest Group)
- DOI/arXiv: arXiv:2506.23253 (v1 2025-06-29, v2 2025-10-03)
- 문헌 유형: 학회 발표 논문 (PPIG — 워크숍 성격의 학회, 동료 검토 수준은 주요 학회보다 가벼움) / preprint
- 표본·방법: 확장 바이브 코딩 세션 영상(생각 말하기 포함) 8시간 이상, framework analysis. 저자들은 "first empirical study of vibe coding"이라 주장.
- 요약: 바이브 코딩은 프롬프트 → 빠른 훑어보기·앱 실행 평가 → 수동 편집을 오가는 반복적 목표 충족 사이클. 프롬프트는 모호한 상위 지시와 세부 기술 명세를 섞는다. 디버깅은 여전히 AI+수동의 혼합.
- 인용할 만한 문장: "Critically, vibe coding does not eliminate the need for programming expertise but rather redistributes it toward context management, rapid code evaluation, and decisions about when to transition between AI-driven and manual manipulation of code."
- "{연도} 기준": 2025 상반기 도구
- 독자 전달 제안: "개발자가 사라진다"가 아니라 "전문성이 재배치된다" — DevRel이 가르칠 내용이 문법·API 사용법에서 맥락 관리·검증 능력으로 옮겨간다는 논지에 직결.

---

## [B] 논문 8: Good Vibrations? A Qualitative Study of Co-Creation, Communication, Flow, and Trust in Vibe Coding
- 저자·연도: Veronica Pimenova, Sarah Fakhoury, Christian Bird, Margaret-Anne Storey, Madeline Endres (2025)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2509.12491 (v1 2025-09-15, v2 2026-06-29)
- 문헌 유형: preprint (질적 연구)
- 표본·방법: 반구조화 인터뷰 + Reddit 스레드 + LinkedIn 게시물, 총 19만 단어 이상. 근거 이론(grounded theory).
- 요약: 바이브 코딩을 AI와의 대화형 상호작용·공동 창작·몰입(flow)과 즐거움 중심의 이론으로 정리. 전문가와 비개발자 모두 바이브 코딩을 하는 이유를 다룬다. 명세·신뢰성·디버깅·지연·코드 리뷰 부담·협업에서 반복되는 고통 지점 도출. 커뮤니티가 스스로 발견·공유한 모범 사례도 정리.
- 인용할 만한 문장: "We find that AI trust regulates movement along a continuum from delegation to co-creation and supports the developer experience by sustaining flow."
- "{연도} 기준": 2025
- 독자 전달 제안: "모범 사례가 커뮤니티에서 발견되고 공유된다"는 대목 — 바이브 코더 커뮤니티가 새 DevRel의 청중이자 지식 생산자라는 근거. Storey(DevEx·SPACE 공저자)가 참여한 점도 연결고리.

---

## [B] 논문 9: Building Software by Rolling the Dice: A Qualitative Study of Vibe Coding
- 저자·연도: Yi-Hung Chou, Boyuan Jiang, Yi Wen Chen, Mingyue Weng, Victoria Jackson, Thomas Zimmermann, James A. Jones (2025)
- 발표처: ESEC/FSE 2026 게재 승인 (arXiv comment 기준)
- DOI/arXiv: arXiv:2512.22418 (v1 2025-12-27)
- 문헌 유형: peer-reviewed 학회 (승인) / preprint
- 표본·방법: 바이브 코딩 영상 20개 근거 이론 분석 — 라이브 코딩 세션 7개(약 16시간, 프롬프트 254개) + 의견 영상 13개(약 5시간).
- 요약: 코드를 거의 보지 않고 AI에 의존하는 부류부터 생성 결과를 검토·수정하는 부류까지 스펙트럼. 모두 생성의 확률적 성질과 씨름하며 디버깅을 "주사위 굴리기"로 묘사. 전문성과 AI 의존도가 만든 서로 다른 멘탈 모델이 프롬프트 전략·평가 방식·신뢰 수준을 좌우.
- 인용할 만한 문장: "some vibe coders rely almost entirely on AI without inspecting code, while others examine and adapt generated outputs."
- "{연도} 기준": 2025
- 독자 전달 제안: 비개발자 청중에게 필요한 것은 "검증 습관"을 심어주는 교육 — DevRel의 교육 콘텐츠 방향.

---

## [B] 논문 10: Computer Science Achievement and Writing Skills Predict Vibe Coding Proficiency
- 저자·연도: Sverrir Thorgeirsson, Theo B. Weidmann, Zhendong Su (ETH Zürich, 2026)
- 발표처: CHI 2026
- DOI/arXiv: https://doi.org/10.1145/3772318.3791666 · arXiv:2603.14133
- 문헌 유형: peer-reviewed 학회 (사전등록 횡단 연구)
- 표본·방법: 대학생 N=100. CS 성취도, 일반 인지 능력, 글쓰기 능력 측정 + 바이브 코딩 평가(전문가 8인 합의로 과제 선정, 전용 환경).
- 핵심 결과: 글쓰기 능력과 CS 성취도 모두 바이브 코딩 성과의 유의한 예측 변수. 일반 인지 능력을 통제해도 CS 성취도는 유의. [효과 크기 수치: 미확인]
- "{연도} 기준": 2026 / 학생 표본 — 현업 일반화 주의
- 독자 전달 제안: "누구나 개발자"라는 서사에 대한 균형 — 비개발자도 만들 수 있지만 CS 기초가 여전히 성과를 가른다. DevRel이 비개발자 청중에게 줄 교육은 "코딩 제로"가 아니라 "개념 기초 + 글쓰기(명세)".

---

## [B] 논문 11: Programming by Chat: A Large-Scale Behavioral Analysis of 11,579 Real-World AI-Assisted IDE Sessions
- 저자·연도: Ningzhi Tang, Chaoran Chen, Zihan Fang, Gelei Xu, Maria Dhakal, Yiyu Shi, Collin McMillan, Yu Huang, Toby Jia-Jun Li (2026)
- 발표처: ACM 게재 (DOI 10.1145/3832783.3834377 — 학회명 미확인)
- DOI/arXiv: arXiv:2604.00436 (v1 2026-04-01, v2 2026-08-23)
- 문헌 유형: peer-reviewed (DOI 부여) / preprint
- 표본·방법: 공개 저장소에 커밋된 Cursor·GitHub Copilot 채팅 — 개발자 메시지 74,998개, 세션 11,579개, 저장소 1,300개, 개발자 899명.
- 요약: 세 가지 변화 — (1) 대화형 프로그래밍은 "점진적 명세"(처음부터 완전히 명세하지 않고 반복 정제), (2) 진단·이해·검증을 AI에 위임하는 인지 노동 재배치, (3) 계획을 지속 산출물로 외부화하고 컨텍스트 주입·행동 제약으로 AI 자율성을 협상.
- 인용할 만한 문장: "developers actively manage the collaboration, externalizing plans into persistent artifacts, and negotiating AI autonomy through context injection and behavioral constraints."
- "{연도} 기준": 2026 (Cursor·Copilot 채팅 모드)
- 독자 전달 제안: 개발자가 AGENTS.md·규칙 파일 같은 "지속 산출물"을 쓴다는 실증 — 플랫폼 기업이 에이전트용 컨텍스트(규칙·문서)를 제공해야 할 이유(축 D)와 연결.

---

## [B] 논문 12: The state of the art in end-user software engineering
- 저자·연도: Andrew J. Ko, Robin Abraham, Laura Beckwith, Alan Blackwell, Margaret Burnett, Martin Erwig, Chris Scaffidi, Joseph Lawrance, Henry Lieberman, Brad Myers, Mary Beth Rosson, Gregg Rothermel, Mary Shaw, Susan Wiedenbeck (2011)
- 발표처: ACM Computing Surveys, Vol. 43, No. 3, Article 21, pp. 1–44 (2011-04)
- DOI/arXiv: https://doi.org/10.1145/1922649.1922658
- 문헌 유형: peer-reviewed 서베이 (seminal)
- 요약: 최종 사용자 소프트웨어 공학(EUSE)이라는 영역을 정의·분류. 최종 사용자 프로그래머는 전문 개발자와 목표는 다르지만 요구사항 이해·설계·재사용·통합·테스트·디버깅에서 같은 공학적 문제를 겪는다. 도구 설계의 횡단 이슈로 위험·보상·도메인 복잡도·자기효능감, 사용자에게 SE 원칙을 교육할 가능성을 다룸.
- 인용할 만한 문장 (abstract): "Most programs today are written not by professional software developers, but by people with expertise in other domains working towards goals for which they need computational support."
- "{연도} 기준": 2011 (스프레드시트·인터페이스 빌더 시대의 개념이지만 바이브 코딩 이해의 이론적 뿌리)
- 독자 전달 제안: "비개발자가 개발한다"는 새 현상이 아니다 — 2011년 서베이가 이미 "대부분의 프로그램은 전문 개발자가 쓰지 않는다"고 했다. AI가 바꾼 것은 그 범위와 산출물의 종류. 책의 도입부에서 "Dev의 경계는 원래 흐렸다"는 논지로 쓰기 좋다.

---

## [B] 논문 13: Estimating the Numbers of End Users and End User Programmers
- 저자·연도: Christopher Scaffidi, Mary Shaw, Brad Myers (2005)
- 발표처: IEEE VL/HCC 2005 (Symposium on Visual Languages and Human-Centric Computing), pp. 207–214
- DOI/arXiv: https://doi.org/10.1109/VLHCC.2005.34
- 문헌 유형: peer-reviewed 학회 (seminal)
- 표본·방법: 미국 인구조사(Census)·노동통계국(BLS) 데이터 기반 추정. Boehm(1995)의 "5,500만 최종 사용자 프로그래머" 예측을 재검토.
- 핵심 수치 (본문 확인, 미국 직장 기준 2012년 추정): 최종 사용자 9,000만 명, 그중 스프레드시트·DB 사용자 5,500만 명 이상(잠재적 프로그래머), 스스로 "프로그래머"라 답할 사람 1,300만 명 이상 vs BLS 전망 전문 프로그래머 300만 명 미만.
- 인용할 만한 문장: "over 13 million will describe themselves as programmers, compared to BLS projections of fewer than 3 million professional programmers."
- "{연도} 기준": 2005년 작성, 2012년 미국 전망치
- 독자 전달 제안: "전문 개발자보다 스스로 프로그래밍하는 비전문가가 몇 배 많았다"는 역사적 기준선. 단 2005년의 **추정·전망**이며 미국 한정 — "실측"으로 쓰면 안 됨. 흔히 "5,500만 명의 최종 사용자 프로그래머"로 인용되지만 그 숫자는 Boehm 예측이며 이 논문은 그것이 사실상 "컴퓨터 사용자 수"였다고 비판한다.

---

## [B] 논문 14: Non-Expert Programmers in the Generative AI Future
- 저자·연도: Molly Q Feldman, Carolyn Jane Anderson (2024)
- 발표처: CHIWORK '24 (3rd Annual Meeting of the Symposium on Human-Computer Interaction for Work), ACM, 2024-06
- DOI/arXiv: https://doi.org/10.1145/3663384.3663393
- 문헌 유형: peer-reviewed 학회 (통제 연구)
- 표본·방법: 비프로그래머 67명 대상 통제 연구, 초보 프로그래머 대상 선행 연구와 비교.
- 요약: 코드 LLM은 자연어→코드로 더 넓은 노동자에게 프로그래밍을 열 잠재력이 있으나, 비전문가는 여러 장벽에 부딪힌다 — 특히 "기술적 의사소통"의 여러 측면. 전통적 입문 프로그래밍 수업이 생성형 AI 활용에 무엇을 준비시키고 무엇을 못 시키는지 드러냄.
- 인용할 만한 문장: "Our study reveals multiple barriers to effective use of large language models of code for non-experts, including several aspects of technical communication."
- "{연도} 기준": 2024 (2023~24 모델)
- 독자 전달 제안: 비개발자 청중의 병목은 "기술적 의사소통" — 이것은 정확히 DevRel이 전문으로 하던 일(기술을 말로 풀어 전달). 새 청중을 위한 DevRel의 역할 정의에 직접 쓰인다.

---

## [B] 논문 15: Non-programmers Assessing AI-Generated Code: A Case Study of Business Users Analyzing Data
- 저자·연도: Yuvraj Virk, Dongyu Liu (2025)
- 발표처: IEEE VL/HCC 2025 (arXiv comment 기준 승인)
- DOI/arXiv: arXiv:2508.06484 (2025-08-08)
- 문헌 유형: peer-reviewed 학회 (승인) / preprint
- 표본·방법: 마케팅·영업 실무자 설문·과제 — LLM이 생성한 마케팅 데이터 분석을 평가하게 함. AI가 자주 틀린다고 반복 고지하고 오류를 찾으라고 명시적으로 요청. [참가자 수: 미확인]
- 요약: 참가자들은 의사결정을 해칠 수 있는 치명적 결함을 자주 놓쳤고, 그중 다수는 기술 지식 없이도 알아챌 수 있는 것이었다. 응답을 단계별로 나누고 결정마다 대안을 보여주면 개선됐지만, 여전히 AI의 단계를 따라 추론하는 데 어려움.
- 인용할 만한 문장: "Our findings suggest that business professionals cannot reliably verify AI-generated data analyses on their own"
- "{연도} 기준": 2025
- 독자 전달 제안: 사내 AX 확산의 위험 — 비개발자가 "만들 수는 있지만 검증은 못 한다". 내부 DevRel(AX 챔피언)의 역할에 검증 가드레일·리뷰 문화 설계가 들어가야 하는 근거.

---

## [B] 논문 16: Adoption of low-code and no-code development: A systematic literature review and future research agenda
- 저자·연도: Matthew Oladeji Ajimati, Noel Carroll, Mary Lou Maher (2024/2025)
- 발표처: Journal of Systems and Software, Vol. 222, Article 112300 (온라인 2024-11-26)
- DOI/arXiv: https://doi.org/10.1016/j.jss.2024.112300
- 문헌 유형: peer-reviewed 체계적 문헌 리뷰
- 표본·방법: 검색 결과 요약 기준 2017~2023 출판물에서 1차 연구 40편 식별 [웹 검색 요약에서 확인 — 원문 대조 미완, 수치 인용 전 재확인 필요]
- 요약: 로우코드·노코드(LCNC)와 시민 개발(citizen development, CD) 실천의 적용, 이론적 렌즈, 편익과 과제를 정리. [abstract 원문 확보 실패 — 요약은 2차 정보]
- 독자 전달 제안: "시민 개발자"는 AI 이전부터 거버넌스 이슈(섀도 IT·품질·보안)를 동반했다는 배경. 바이브 코딩 확산에 그 교훈을 이식하는 논지로.

---

## [D] 논문 17: Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models
- 저자·연도: Cheng-Yu Hsieh, Si-An Chen, Chun-Liang Li, Yasuhisa Fujii, Alexander Ratner, Chen-Yu Lee, Ranjay Krishna, Tomas Pfister (2023, Univ. of Washington·Google)
- 발표처: arXiv 프리프린트 [정식 게재처 미확인]
- DOI/arXiv: arXiv:2308.00675 (2023-08-01)
- 문헌 유형: preprint
- 표본·방법: 비전·언어 6개 과제. 기존 벤치마크 + 수백 개 도구 API가 있는 신규 실사용형 데이터셋. 문서만 준 zero-shot vs 시연(few-shot) 비교.
- 핵심 결과 (abstract): (1) 기존 벤치마크에서 도구 문서만 준 zero-shot이 few-shot과 동등. (2) 수백 개 API가 있는 현실적 데이터셋에서 "zero-shot documentation significantly outperforming few-shot without documentation". (3) GroundingDino·Stable Diffusion·XMem·SAM의 문서만으로 LLM이 Grounded-SAM·Track Anything의 기능을 재발명.
- 인용할 만한 문장: "We advocate the use of tool documentation, descriptions for the individual tool usage, over demonstrations."
- "{연도} 기준": 2023 (GPT-3.5/4 세대)
- 독자 전달 제안: "문서가 에이전트의 사용 설명서"라는 논지의 학술적 뿌리. 예제 코드 대량 생산보다 정확한 레퍼런스 문서가 에이전트 시대에 더 중요할 수 있다 — DevRel 문서 전략의 우선순위 전환 근거.

---

## [D] 논문 18: SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering
- 저자·연도: John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press (2024, Princeton)
- 발표처: NeurIPS 2024 (Advances in Neural Information Processing Systems 37, Main Conference Track)
- DOI/arXiv: arXiv:2405.15793 (v1 2024-05-06, v3 2024-11-11) · proceedings.neurips.cc 2024
- 문헌 유형: peer-reviewed 학회
- 표본·방법: SWE-bench, HumanEvalFix에서 맞춤형 에이전트-컴퓨터 인터페이스(ACI) 평가.
- 핵심 수치 (abstract): pass@1 — SWE-bench 12.5%, HumanEvalFix 87.7% (당시 SOTA, 비대화형 LM 대비 크게 상회).
- 인용할 만한 문장: "we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use."
- "{연도} 기준": 2024 — SWE-bench 12.5%는 2024년 수치이며 이후 모델에서 크게 올랐다. 성능 수치는 역사적 맥락으로만.
- 독자 전달 제안: "에이전트는 새로운 범주의 최종 사용자"라는 문장이 이 책 축 D의 표제 인용 후보. DX(Developer Experience)가 AX(Agent Experience)로 확장된다는 논지에 학술적 근거를 준다. ACI 개념 = 사람용 UI/IDE처럼 에이전트용 인터페이스도 설계 대상.

---

## [D] 논문 19: Model Context Protocol (MCP) Tool Descriptions Are Smelly! Towards Improving AI Agent Efficiency with Augmented MCP Tool Descriptions
- 저자·연도: Mohammed Mehedi Hasan, Hao Li, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan (2026, Queen's University)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2602.14878 (v1 2026-02-16, v3 2026-05-31)
- 문헌 유형: preprint
- 표본·방법: MCP 서버 103개의 도구 856개. 문헌에서 도구 설명 구성요소 6가지 도출 → 채점 루브릭 → "도구 설명 스멜" 형식화 → FM 기반 스캐너로 측정 + 설명 보강 전후 에이전트 성능 비교.
- 핵심 수치 (abstract): 도구 설명의 97.1%가 스멜 1개 이상, 56%가 목적을 명확히 밝히지 않음. 전 구성요소 보강 시 과제 성공률 중앙값 +5.85%p, 부분 목표 달성 +15.12% — 대신 실행 단계 수 +67.46%, 16.67% 사례에서 성능 퇴행. 압축 변형이 신뢰성을 유지하며 토큰 오버헤드를 줄임.
- 인용할 만한 문장: "FMs rely on natural-language tool descriptions, making these descriptions a critical component in guiding FMs to select the optimal tool for a given (sub)task and to pass the right arguments to the tool."
- "{연도} 기준": 2026 상반기 MCP 생태계
- 독자 전달 제안: "에이전트를 위한 테크니컬 라이팅"이 새 DevRel 업무라는 가장 구체적인 실증. 동시에 "많이 쓸수록 좋다"가 아니라는 트레이드오프(단계 +67%, 퇴행 16.67%)도 같이 전달 — 에이전트용 문서는 간결성이 품질이다.

---

## [D] 논문 20: Model Context Protocol (MCP) at First Glance: Studying the Security and Maintainability of MCP Servers
- 저자·연도: Mohammed Mehedi Hasan, Hao Li, Emad Fallahzadeh, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan (2025)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2506.13538 (v1 2025-06-16, v5 2026-04-13)
- 문헌 유형: preprint
- 표본·방법: 오픈소스 MCP 서버 1,899개, 건강 지표 + 범용 정적 분석 + MCP 전용 스캐너.
- 핵심 수치 (abstract, v5): 취약점 8종 식별(전통 취약점과 겹치는 것은 3종). 7.2%가 일반 취약점, 5.5%가 MCP 특유의 tool poisoning. 66%에 코드 스멜, 14.4%에 선행 연구와 겹치는 버그 패턴 10종.
- 인용할 만한 문장: "In late 2024, Anthropic introduced the Model Context Protocol (MCP) to standardize this tool ecosystem. MCP is rapidly emerging as a de facto industry standard."
- "{연도} 기준": 2025 (v5는 2026-04 개정 — 인용 시 버전 명시; 개정 간 수치가 바뀌었을 가능성 있음)
- 독자 전달 제안: 플랫폼 기업이 MCP 서버를 "DevRel 산출물"로 낼 때 보안·유지보수 책임이 따라온다는 경고.

---

## [D] 논문 21: A Measurement Study of Model Context Protocol Ecosystem
- 저자·연도: Hechuan Guo, Yongle Hao, Yue Zhang, Minghui Xu, Peizhuo Lv, Jiezhi Chen, Xiuzhen Cheng (2025, 산둥대 등)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2509.25292 (v1 2025-09-29, v3 2025-11-15)
- 문헌 유형: preprint (측정 연구)
- 표본·방법: MCPCrawler로 6개 주요 마켓 14일 수집 — 원시 항목 17,630개 → 유효 프로젝트 8,401개(서버 8,060 · 클라이언트 341).
- 핵심 결과: 등록 프로젝트의 절반 이상이 무효 또는 저가치. 서버는 의존성 단일 재배(monoculture)·고르지 않은 유지보수의 구조적 위험. 클라이언트는 프로토콜·연결 패턴의 과도기.
- 인용할 만한 문장: "Are MCP marketplaces truly growing, or merely inflated by placeholders and abandoned prototypes?"
- "{연도} 기준": 2025-09 수집 시점
- 독자 전달 제안: "MCP 서버 수 = 생태계 건강"이라는 허영 지표 경계. DevRel 지표론(축 A·F의 건강 지표)과 연결.

---

## [D] 논문 22: Agent READMEs: An Empirical Study of Context Files for Agentic Coding
- 저자·연도: Worawalan Chatlatanagulchai, Hao Li, Yutaro Kashiwa, Brittany Reid, Kundjanasith Thonglek, Pattara Leelaprute, Arnon Rungsawang, Bundit Manaskasemsak, Bram Adams, Ahmed E. Hassan, Hajimu Iida (2025)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2511.12884 (v1 2025-11-17, v2 2026-08-09)
- 문헌 유형: preprint
- 표본·방법: 저장소 1,925개의 에이전트 컨텍스트 파일(AGENTS.md, CLAUDE.md 등) 2,303개, 16개 지시 유형 내용 분석.
- 핵심 수치 (abstract): 테스트 절차 75.9%, 구현 세부 70.8%, 아키텍처 68.1% 포함 vs 보안 14.8%, 성능 14.5%만 명시. 정적 문서가 아니라 잦은 소규모 추가로 진화하는 "설정 코드 같은" 산출물.
- 인용할 만한 문장: "these files are not static documentation but complex, difficult-to-read artifacts that evolve like configuration code through frequent, small additions."
- "{연도} 기준": 2025
- 독자 전달 제안: "에이전트용 README"라는 새 문서 장르의 실태. DevRel이 SDK·샘플 저장소에 AGENTS.md를 제공하는 관행의 근거이자, 보안 가드레일을 넣어야 할 이유.

---

## [D] 논문 23: Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?
- 저자·연도: Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev (2026, ETH Zürich·LogicStar)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2602.11988 (v1 2026-02-12, v2 2026-06-23)
- 문헌 유형: preprint
- 표본·방법: (a) SWE-bench 과제 + LLM 생성 컨텍스트 파일, (b) 개발자가 커밋한 컨텍스트 파일이 있는 저장소의 신규 이슈 모음. 여러 LLM·코딩 에이전트 비교.
- 핵심 결과 (abstract): 컨텍스트 파일 제공이 과제 성공률을 일반적으로 개선하지 않으면서 추론 비용은 평균 20% 이상 증가. 지시 사항은 잘 따르지만, 모델 제공사가 권장하는 "저장소 개요"는 도움이 안 됨. 비표준 코딩 관행 명시에는 유용.
- 인용할 만한 문장: "while context files are useful for specifying non-standard coding practices, any attempts to improve performance should be rigorously evaluated before deployment."
- 반대 결과 참고: Khatri (2026, arXiv:2607.27250) — Claude Code·Codex, 실제 과제 17개·288회 실행에서 컨텍스트 전략이 정확성을 측정 가능하게 움직이지 않음(동등성 검정으로 ≤10~15%p 한정). 해당 논문 서론은 Lulla et al.(2026)이 효율(실행 시간·출력 토큰) 개선을 보고했다고 인용 [Lulla 원문 미확인].
- "{연도} 기준": 2026
- 독자 전달 제안: "에이전트용 문서를 만들면 무조건 좋아진다"는 업계 서사에 대한 학술적 반론. 에이전트용 문서의 가치는 "모델이 모르는 것(비표준 관행·우리만의 규칙)"에 집중될 때 생긴다 — 모델이 이미 아는 개요를 반복하지 말라는 실무 원칙으로 번역.

---

## [A] 논문 24: A Developer Relations (DevRel) model to govern developers in Software Ecosystems
- 저자·연도: Awdren Fontão, Sergio Cleger-Tamayo, Igor Wiese, Rodrigo Pereira dos Santos, Arilo Claudio Dias-Neto (온라인 2021-10 / 권호 2023)
- 발표처: Journal of Software: Evolution and Process, Vol. 35, Issue 5 (2023; 온라인 선공개 2021-10-12)
- DOI/arXiv: https://doi.org/10.1002/smr.2389
- 문헌 유형: peer-reviewed 저널 — **DevRel을 직접 다룬 드문 학술 연구**
- 표본·방법: 회색 문헌 리뷰 + 의견 설문 + 인터뷰로 모델 제안·정제. [설문·인터뷰 표본 수: 미확인]
- 요약: 소프트웨어 생태계(SECO)는 중심 조직(keystone)이 제공하는 플랫폼에 서드파티 개발자가 협력·경쟁하며 기여하는 구조. keystone은 서드파티 개발자의 임계 질량을 끌어들이고 참여시키기 위해 DevRel 내부 팀에 투자한다. DevRel 팀은 SECO 행위자 간 사회적 관계와 keystone 목표-개발자 기대의 시너지를 만들어야 한다. 제안 모델 DevGo(DEVeloper GOVernance): 초점 영역 4개, 개발자 성장 단계 3개, 스테이지 6개, 촉진 요인, 가치 전달 객체 + DevRel 실무자 교훈 62개.
- 인용할 만한 문장: "There are keystones investing in Developer Relations (DevRel) internal team as a global business strategy to attract and engage a critical mass of third-party developers in producing and evolving contributions."
- "{연도} 기준": 2021~2023 (AI 이전 모델)
- 독자 전달 제안: DevRel의 학술적 정의 기준선 — "DevRel = 생태계 거버넌스 기능". AI 이후 "서드파티 개발자"가 "비개발자 빌더 + 에이전트"로 확장될 때 이 모델의 어느 칸이 바뀌는지 대조하는 장치로 쓰기 좋다.

---

## [A] 논문 25: Death of a Software Ecosystem
- 저자·연도: Daniel Massanori, Bruno Cafeo, Igor Wiese, Awdren Fontão (2020)
- 발표처: SBES 2020 (XXXIV Brazilian Symposium on Software Engineering), ACM, pp. 399–404
- DOI/arXiv: https://doi.org/10.1145/3422392.3422445
- 문헌 유형: peer-reviewed 학회 (short paper)
- 표본·방법: Windows Phone 관련 Stack Overflow 질문 46,030개 분석.
- 요약: DevRel 투자에도 생태계가 죽는 사례(Symbian 2012, Firefox OS 2016, Windows Phone 2017). 핵심 플랫폼이 중단될 때 생태계에 무슨 일이 생기는지 — 붕괴의 "활력 징후", 이주·생존 패턴 등 14개 인사이트.
- 인용할 만한 문장: "The Developer Relations (DevRel) is a strategy to attract, engage and mature developers in contributing to a platform."
- "{연도} 기준": 2020
- 독자 전달 제안: "DevRel만으로 생태계를 살릴 수 없다" — 플랫폼 경쟁력과 DevRel의 관계. AI 시대 플랫폼 교체기에 DevRel이 무엇을 할 수 있고 없는지의 역사적 비교.

---

## [A] 논문 26: Developer experience: Concept and definition
- 저자·연도: Fabian Fagerholm, Jürgen Münch (2012)
- 발표처: ICSSP 2012 (International Conference on Software and System Process), IEEE, pp. 73–77
- DOI/arXiv: https://doi.org/10.1109/ICSSP.2012.6225984
- 문헌 유형: peer-reviewed 학회 (short/position paper, seminal)
- 요약: 사용자 경험(UX)에 대응하는 개념으로 개발자 경험(DX)을 제안. 분산 개발, 소프트웨어 생태계에 자발적 외부 개발자 통합 같은 새 작업 방식이 개발자의 감정·인식·동기·과업 동일시에 대한 이해를 요구한다고 주장. 원 논문은 DX를 인지(cognition)·정동(affect)·의욕(conation) 세 측면으로 구조화 [3요소 명칭은 본문 기반으로 널리 인용되나 이번 조사에서 abstract로만 확인 — 본문 재확인 권장].
- 인용할 만한 문장 (abstract): "developer experience could be defined as a means for capturing how developers think and feel about their activities within their working environments"
- "{연도} 기준": 2012
- 독자 전달 제안: DX 개념의 출발점에 이미 "생태계의 외부 개발자"가 있었다 — DX는 처음부터 DevRel의 개념. "Agent Experience(AX)"를 이 정의에 대입하면 "에이전트가 작업 환경에서 어떻게 '처리'하는가"로 바뀐다는 비유 장치.

---

## [A] 논문 27: DevEx: What Actually Drives Productivity
- 저자·연도: Abi Noda, Margaret-Anne Storey, Nicole Forsgren, Michaela Greiler (2023) — **저자 순서 주의: Noda가 제1저자**
- 발표처: ACM Queue, Vol. 21, No. 2, pp. 35–53 (2023-04-30). 재수록: Communications of the ACM, Vol. 66, No. 11, pp. 44–49 (2023-11), 제목 "DevEx: What Actually Drives Productivity?"
- DOI/arXiv: https://doi.org/10.1145/3595878 (Queue) · https://doi.org/10.1145/3610285 (CACM)
- 문헌 유형: 실무자 대상 학술 잡지 기고 (ACM Queue는 일반 학술지 수준의 동료 검토가 아님 — "peer-reviewed 논문"으로 부르지 말 것)
- 요약: DevEx는 개발자의 실제 경험과 일상 업무에서 마주치는 마찰 지점에 초점. 생산성 향상 외에 효율·품질·직원 유지로 비즈니스 성과를 이끈다. 이해 프레임워크(세 차원: 피드백 루프·인지 부하·몰입 상태 — 본문 기준 널리 인용, 이번 조사에서는 abstract만 확인)와 개발자 피드백 + 엔지니어링 시스템 데이터를 결합한 측정 프레임워크 제시.
- 인용할 만한 문장: "Developer experience focuses on the lived experience of developers and the points of friction they encounter in their everyday work."
- "{연도} 기준": 2023
- 독자 전달 제안: 사내 AX/내부 DevRel의 측정 언어. 비개발자 빌더와 에이전트가 들어온 뒤 "피드백 루프·인지 부하·몰입"이 각각 어떻게 바뀌는지 틀로 사용.

---

## [A] 논문 28: The SPACE of Developer Productivity
- 저자·연도: Nicole Forsgren, Margaret-Anne Storey, Chandra Maddila, Thomas Zimmermann, Brian Houck, Jenna Butler (2021)
- 발표처: ACM Queue, Vol. 19, No. 1, pp. 20–48 (2021-02-28) · 재수록 Communications of the ACM, Vol. 64, No. 6, pp. 46–53 (2021-06)
- DOI/arXiv: https://doi.org/10.1145/3454122.3454124 (Queue) · https://doi.org/10.1145/3453928 (CACM)
- 문헌 유형: 실무자 대상 학술 잡지 기고 (Queue/CACM)
- 요약: 개발자 생산성은 개인 활동량이나 시스템 효율 이상이며 단일 지표로 측정할 수 없다. SPACE = Satisfaction and well-being, Performance, Activity, Communication and collaboration, Efficiency and flow.
- 인용할 만한 문장: "Developer productivity is about more than an individual's activity levels or the efficiency of the engineering systems relied on to ship software, and it cannot be measured by a single metric or dimension."
- "{연도} 기준": 2021 (AI 코딩 보조 이전)
- 독자 전달 제안: METR(논문 6)의 체감-실측 괴리와 함께 — AI 도입 효과를 "활동량(A)" 하나로 재면 틀린다. AX 담당자가 경영진에게 보고할 지표 설계 틀.

---

## [A] 논문 29: An Actionable Framework for Understanding and Improving Developer Experience
- 저자·연도: Michaela Greiler, Margaret-Anne Storey, Abi Noda (IEEE TSE 권호 2023; 온라인 2022)
- 발표처: IEEE Transactions on Software Engineering, Vol. 49, No. 4, pp. 1411–1425 (2023-04)
- DOI/arXiv: https://doi.org/10.1109/TSE.2022.3175660
- 문헌 유형: peer-reviewed 저널 — 요청서의 "Greiler/Storey/Noda"는 이 TSE 논문이다. ACM Queue "DevEx"(논문 27, Noda 제1저자)와 별개 문헌이므로 구분할 것.
- 표본·방법: 업계 개발자 21명 반구조화 인터뷰, 전사·반복 코딩(질적 연구).
- 요약: 개발자 경험에 영향을 주는 요인과 요인의 중요도를 좌우하는 특성, 개인·팀의 개선 전략과 장벽, 개선이 안 될 때의 대처 기제를 규명. 결과물이 DX Framework. (2차 자료에 따르면 Queue 논문의 세 차원은 이 연구가 도출한 25개 사회기술적 요인에서 나왔다고 함 — [원문 대조 미확인])
- 인용할 만한 문장: "enhancing developer experience improves productivity, satisfaction, engagement and retention."
- "{연도} 기준": 2022~2023
- 독자 전달 제안: DX 담론의 실증 기반. 표본 21명 질적 연구라는 점을 라벨로.

<!-- 정정 메모(논문 27): DevEx 세 차원 "피드백 루프·인지 부하·몰입 상태"는 검색 요약·CACM 페이지 제목 수준에서 확인됨. 원문 문장 직접 대조는 ACM 403으로 실패. 책에 쓸 때 "Noda 외(2023)는 DevEx를 피드백 루프·인지 부하·몰입 세 차원으로 정리했다" 정도는 안전. -->

---

## [A] 논문 30: What Makes APIs Hard to Learn? Answers from Developers
- 저자·연도: Martin P. Robillard (2009)
- 발표처: IEEE Software, Vol. 26, No. 6, pp. 27–34 (2009-11)
- DOI/arXiv: https://doi.org/10.1109/MS.2009.193 (후속 확장판: Robillard & DeLine, "A field study of API learning obstacles," Empirical Software Engineering, 2011, doi:10.1007/s10664-010-9150-8 — 2차 자료가 말하는 "440명 이상"은 이 확장판의 설문+인터뷰 누계로 보임 [확장판 원문 미확인])
- 문헌 유형: peer-reviewed 잡지 논문 (seminal)
- 표본·방법 (본문 확인): Microsoft 레드먼드 캠퍼스 개발자 대상 설문(13문항), 응답 83명(응답률 8%), 개방형 문항 유효 응답 80명 + 대면 인터뷰. 응답자 평균 경력 12.9년, API 54종 학습 경험.
- 핵심 수치 (본문 확인, 80명 기준): API 학습 방법 — 문서 읽기 78%, 코드 예제 55%, 직접 실험 34%, 아티클 30%, 동료에게 질문 29%. 장애 요인을 1개 이상 언급한 74명 중 50명이 "API 리소스(문서 등)" 관련 장애 언급.
- 요약: 가장 심각한 장애 상당수가 문서·학습 자료에서 나옴. API가 커질수록 개발자는 전체 중 점점 작은 부분만 배우게 되므로 필요한 정보를 찾아가는 수단이 중요.
- "{연도} 기준": 2009, Microsoft 사내 개발자
- 독자 전달 제안: "사람 개발자도 문서를 1순위로 읽었다(78%)" → 지금은 그 자리에 에이전트가 끼어든다. "동료에게 묻기 29%"는 Stack Overflow·커뮤니티의 역할과 비교해 쓸 수 있음. 2009 사내 표본이라는 라벨 필수.

---

## [A] 논문 31: How API Documentation Fails
- 저자·연도: Gias Uddin, Martin P. Robillard (2015)
- 발표처: IEEE Software, Vol. 32, No. 4, pp. 68–75 (2015-07)
- DOI/arXiv: https://doi.org/10.1109/MS.2014.80
- 문헌 유형: peer-reviewed 잡지 논문
- 표본·방법 (abstract): 전문 개발자 대상 설문 2회 총 323명 + API 문서 단위 179개 분석, 흔한 문서 문제 10가지의 실제 발현 조사.
- 핵심 결과: 가장 심각한 세 문제 = 모호성(ambiguity), 불완전성(incompleteness), 부정확성(incorrectness). 10개 문제 중 6개가 다른 API로 갈아타게 만드는 "blocker"로 자주 언급됨.
- 인용할 만한 문장: "The respondents often mentioned six of the 10 problems as 'blockers' that forced them to use another API."
- "{연도} 기준": 2015
- 독자 전달 제안: 문서 결함은 이탈 요인 — 사람 개발자는 불평하고 떠나지만, 에이전트는 모호한 문서에서 조용히 틀린 코드를 만든다. MCP 도구 설명 스멜(논문 19)과 짝지어 "10년 전 문제의 재발"로 서술.

---

## [A] 논문 32: Application Programming Interface Documentation: What Do Software Developers Want?
- 저자·연도: Michael Meng, Stephanie Steinhardt, Andreas Schubert (2017/2018)
- 발표처: Journal of Technical Writing and Communication, Vol. 48, No. 3, pp. 295–330 (온라인 2017-07-26)
- DOI/arXiv: https://doi.org/10.1177/0047281617721853
- 문헌 유형: peer-reviewed 저널
- 표본·방법: 반구조화 인터뷰 + 후속 설문. [표본 수: 미확인]
- 요약: 개발자는 처음에 API의 전체 목적·주요 기능에 대한 전역적 이해를 형성하려 하고, 이후 개념 지향 또는 코드 지향 학습 전략 중 하나를 택한다 — 문서는 둘 다 지원해야 한다. 완전성·명료성 같은 일반 품질 기준이 API 문서에도 적용.
- 인용할 만한 문장: "Developing and maintaining API documentation therefore need to involve the expertise of communication professionals."
- "{연도} 기준": 2017
- 독자 전달 제안: 문서가 "커뮤니케이션 전문가"의 일이라는 학술적 근거 — DevRel/테크 라이터의 정체성. 에이전트 시대에 "개념 지향 vs 코드 지향" 두 독자에 "에이전트"라는 세 번째 독자가 추가된다.

---

## [A] 논문 33: Platform Ecosystems: How Developers Invert the Firm
- 저자·연도: Geoffrey Parker, Marshall Van Alstyne, Xiaoyue Jiang (2017)
- 발표처: MIS Quarterly, Vol. 41, No. 1, pp. 255–266 (2017-03)
- DOI/arXiv: https://doi.org/10.25300/MISQ/2017/41.1.13 (SSRN 2861574)
- 문헌 유형: peer-reviewed 저널 (이론 모형)
- 요약: 코드 스필오버의 형식 모형으로, 개발자 수가 늘면 기업이 폐쇄적 수직 통합보다 개방형 외부 계약으로 혁신하는 쪽을 택한다("기업의 역전") — 가치 창출의 중심이 기업 안에서 밖으로 이동. 개발자가 많을수록 고위험 혁신을 추구하는 플랫폼이 더 수익적일 수 있다.
- 인용할 만한 문장: "The locus of value creation moves from inside the firm to outside." / "More developers give platform firms more chances at success."
- "{연도} 기준": 2017 (Apple·Google·Microsoft 2015년 이후 시가총액 1위권 관찰에서 출발)
- 독자 전달 제안: DevRel이 왜 경영 전략인지 — 외부 개발자 = 플랫폼 가치의 원천. AI 시대에 "개발자 수"가 비개발자 빌더로 폭증하면 이 역전은 더 강해지는가? 이 책의 경영진 독자(2순위)를 위한 이론적 앵커.

---

## [E] 논문 34: Generative AI at Work
- 저자·연도: Erik Brynjolfsson, Danielle Li, Lindsey R. Raymond (NBER WP 2023 / QJE 2025)
- 발표처: The Quarterly Journal of Economics, Vol. 140, No. 2, pp. 889–942 (2025) · 선행 NBER Working Paper w31161 (2023-04, 개정 2023-11)
- DOI/arXiv: https://doi.org/10.1093/qje/qjae044 · https://doi.org/10.3386/w31161
- 문헌 유형: peer-reviewed 저널 (현장 자연실험: 시차 도입)
- 표본·방법: 생성형 AI 대화형 보조 도구를 고객지원 상담원에게 시차 도입. **QJE 게재본: 상담원 5,172명 / NBER WP: 5,179명.**
- 핵심 수치 — **판본별로 다름, 주의:**
  - QJE 2025 게재본 abstract: 시간당 해결 건수 기준 생산성 **평균 15%** 증가. 경험 적고 숙련 낮은 상담원은 속도·품질 모두 개선, 최숙련 상담원은 속도 소폭 상승·품질 소폭 하락.
  - NBER 2023 WP abstract: 생산성 **평균 14%** 증가, **초보·저숙련 34%** 개선.
- 인용할 만한 문장 (QJE): "We also find evidence that AI assistance facilitates worker learning and improves English fluency, particularly among international agents." / "customers are more polite and less likely to ask to speak to a manager."
- "{연도} 기준": 2020~2021 데이터(GPT-3 기반 도구) [데이터 기간은 본문 미확인 — 2차 자료 기준], 2025 게재
- 독자 전달 제안: AI는 "최고수의 암묵지를 신입에게 옮기는 도구" — 사내 AX가 전파하는 것은 도구가 아니라 숙련의 확산이라는 논지. 인용 시 "QJE 2025 게재본 기준 15%"로 명시. 14%/34%는 WP 수치.

---

## [E] 논문 35: Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality
- 저자·연도: Fabrizio Dell'Acqua, Edward McFowland III, Ethan Mollick, Hila Lifshitz(-Assaf), Katherine C. Kellogg, Saran Rajendran, Lisa Krayer, François Candelon, Karim R. Lakhani (WP 2023 / 저널 2026)
- 발표처: Organization Science (INFORMS), Articles in Advance 2026-03-11 (접수 2025-12-18, 승인 2026-01-27) · 선행 HBS Working Paper 24-013 / SSRN 4573321 (2023-09)
- DOI/arXiv: https://doi.org/10.1287/orsc.2025.21838 (오픈 액세스 CC BY 4.0) · SSRN https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321
- 문헌 유형: peer-reviewed 저널 (사전등록 현장 실험)
- 표본·방법: BCG 컨설턴트 758명(WP 기준 회사 개인기여자급 컨설턴트의 약 7%). 기준선 과제 후 무작위 3조건 — AI 없음 / GPT-4 / GPT-4 + 프롬프트 엔지니어링 개요.
- 핵심 수치 (게재본 abstract + 본문 확인):
  - 프런티어 **안** 18개 과제: 과제 12.2% 더 많이 완료, 25.1% 더 빨리 완료, 품질 유의하게 향상. (WP abstract: 품질 "40% 이상" 향상, 평균 이하 성과자 +43%·평균 이상 +17% — 게재본 abstract에는 40%가 빠짐)
  - 프런티어 **밖** 과제: 통제군 정답률 약 84.5% vs AI 조건 60%·70.6% → 평균 **19%p** 하락 (게재본 abstract는 "19% less likely"로 표기하나 본문은 "19 percentage points" — %p가 정확).
  - WP: 성공적 AI 활용의 두 패턴 "켄타우로스(분업)"와 "사이보그(완전 통합)".
- 인용할 만한 문장: "AI assistance improves performance for some tasks but worsens it for others, even within the same knowledge workflow and with a seemingly similar level of difficulty."
- "{연도} 기준": GPT-4 (2023 봄 실험)
- 독자 전달 제안: 사내 AX 챔피언이 해야 할 일 = "프런티어가 어디인지 알려주는 것". 비개발자가 AI로 무엇이든 만들 수 있는 게 아니라, 들쭉날쭉한 경계를 아는 사람이 이긴다. 수치 인용 시 판본(WP 2023 vs Org Sci 2026) 명시.

---

## [E] 논문 36: The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise
- 저자·연도: Fabrizio Dell'Acqua 외 (Ayoubi, Lifshitz, Sadun, Mollick, Mollick, Han, Goldman, Nair, Taub, Lakhani) (2025) [공저자 목록 전체는 원문 대조 미완]
- 발표처: NBER Working Paper w33641 (2025) / HBS Working Paper
- DOI/arXiv: https://doi.org/10.3386/w33641
- 문헌 유형: working paper (사전등록 현장 실험)
- 표본·방법: P&G 전문가 776명, 실제 신제품 혁신 과제. 무작위 2×2 — AI 유무 × 개인/2인 팀.
- 핵심 결과 (abstract): AI를 쓴 개인이 AI 없는 팀과 동등한 성과. AI가 기능 사일로를 깸 — AI 없이는 R&D는 기술적, 커머셜은 사업적 제안에 치우쳤지만 AI 사용자는 배경과 무관하게 균형 잡힌 해법. AI 인터페이스가 더 긍정적 정서 반응을 유발. [효과 크기 수치: 미확인]
- 인용할 만한 문장: "individuals with AI matched the performance of teams without AI, demonstrating that AI can effectively replicate certain benefits of human collaboration."
- "{연도} 기준": 2024 실험 / GPT-4 계열
- 독자 전달 제안: 비개발자가 AI로 "개발자 관점"까지 얻는다 — Dev의 경계가 흐려지는 조직 내 증거. 사내 AX에서 부서 간 경계를 넘는 전파의 근거.

---

## [E] 논문 37: Champions of Technological Innovation
- 저자·연도: Jane M. Howell, Christopher A. Higgins (1990)
- 발표처: Administrative Science Quarterly, Vol. 35, No. 2, pp. 317–341 (1990-06)
- DOI/arXiv: https://doi.org/10.2307/2393393
- 문헌 유형: peer-reviewed 저널 (seminal)
- 표본·방법: 챔피언-비챔피언 25쌍(matched pairs)의 설문 + 인터뷰 전사 분석. (검색 결과 기반 — 원문 abstract 직접 확보 실패, APA PsycNet 요약 수준)
- 핵심 결과: 챔피언은 변혁적 리더 행동을 유의하게 더 많이 사용, 위험 감수·혁신성이 높고, 영향력 시도를 더 많이 하며 더 다양한 영향 전술을 씀. (동년 Leadership Quarterly 1(4):249–264 후속 논문에서 챔피언의 경력 — 더 많은 직무·부서·지역 경험 — 을 보고)
- "{연도} 기준": 1990 (캐나다 기업 대상으로 널리 알려짐 [미확인])
- 독자 전달 제안: 사내 AX 챔피언 = 혁신 챔피언 연구의 현대판. 챔피언은 직함이 아니라 행동(비전 제시·영향력 행사·연합 형성)으로 정의된다 — DevRel이 외부에서 하던 에반젤리즘의 내부 버전.

---

## [E] 논문 38: Diffusion of Innovations (단행본, 5판)
- 저자·연도: Everett M. Rogers (초판 1962, 5판 2003)
- 발표처: Free Press (New York), 5th ed. 2003 [ISBN 확인 미완]
- DOI/arXiv: 없음 (단행본)
- 문헌 유형: 학술 단행본 (seminal)
- 핵심 개념 (원서 직접 대조 미완 — 교과서적으로 널리 인용되는 내용):
  - 혁신 채택률에 영향을 주는 5가지 속성: 상대적 이점, 적합성(compatibility), 복잡성, 시험 가능성(trialability), 관찰 가능성(observability).
  - 채택자 범주: 혁신가 2.5% · 초기 채택자 13.5% · 초기 다수 34% · 후기 다수 34% · 지체자 16% — 채택 시점의 정규분포를 표준편차로 자른 **이론적 구분**이지 실측 비율이 아님.
  - 오피니언 리더(opinion leader)와 변화 촉진자(change agent)의 역할 구분, 동질성(homophily)·이질성(heterophily) 네트워크.
- 인용 주의: "{연도} 기준" = 5판 2003. 초판 연도(1962)와 인용 판본을 섞지 말 것. 페이지 인용 시 판본 명시.
- 독자 전달 제안: DevRel(외부)·AX(내부) 모두 "확산의 기술". 특히 "관찰 가능성"·"시험 가능성"은 DevRel의 데모·샌드박스·핸즈온과, 사내 AX의 쇼케이스·파일럿과 1:1로 대응. 채택자 범주 %를 "조직의 실제 분포"처럼 쓰지 말 것.

---

## [E] 논문 39: Diffusion of Innovations in Service Organizations: Systematic Review and Recommendations
- 저자·연도: Trisha Greenhalgh, Glenn Robert, Fraser Macfarlane, Paul Bate, Olivia Kyriakidou (2004)
- 발표처: The Milbank Quarterly, Vol. 82, No. 4, pp. 581–629 (2004-12)
- DOI/arXiv: https://doi.org/10.1111/j.0887-378X.2004.00325.x
- 문헌 유형: peer-reviewed 체계적 리뷰
- 요약: 보건 서비스 조직에서 혁신을 어떻게 확산·유지하는가에 대한 광범위한 문헌 리뷰. 근거 기반 확산 모형, 지식 공백, 재현 가능한 리뷰 방법론 제시. 본문 모형은 오피니언 리더·챔피언·경계 확장자(boundary spanner)·변화 촉진자를 포함한 조직 내 확산 요소를 다룸 [본문 세부 요소 목록은 원문 대조 미완].
- 인용할 만한 문장 (abstract): "How can we spread and sustain innovations in health service delivery and organization?"
- "{연도} 기준": 2004 / 보건 서비스 맥락
- 독자 전달 제안: Rogers(개인 채택)를 조직 확산으로 옮긴 가교 문헌. 사내 AX는 "개인이 도구를 쓰게 하기"가 아니라 "조직이 혁신을 흡수하게 하기" — 이 구분의 근거.

---

## [E] 논문 40: Special Boundary Roles in the Innovation Process
- 저자·연도: Michael L. Tushman (1977)
- 발표처: Administrative Science Quarterly, Vol. 22, No. 4, pp. 587–605 (1977-12) [끝 페이지 미확인]
- DOI/arXiv: https://doi.org/10.2307/2392402
- 문헌 유형: peer-reviewed 저널 (seminal)
- 요약: 혁신 과정에서 조직 내부와 외부 정보 영역을 잇는 "경계 역할(boundary role)"의 기능 — 외부 정보를 들여와 번역하고 내부에 퍼뜨리는 사람. [abstract·표본 원문 미확보]
- 독자 전달 제안: DevRel의 원형은 "경계 확장자" — 회사(제품팀)와 외부 개발자 사이에서 양방향 번역. 저자의 궤적(DevRel→AX)은 같은 경계 역할을 "외부 생태계↔회사"에서 "AI 기술↔현업 부서"로 옮긴 것. 본문 인용 전 원문 확인 필요.

---

## [E] 논문 41: Communities of Practice (Wenger 계열)
- 저자·연도: (a) Etienne Wenger, *Communities of Practice: Learning, Meaning, and Identity*, Cambridge University Press, 1998 · (b) Etienne C. Wenger, William M. Snyder, "Communities of Practice: The Organizational Frontier," Harvard Business Review, 2000 (Jan–Feb) — Crossref에는 2006 재수록본(Knowledge Management and Organizational Learning, OUP, pp. 259–269, doi:10.1093/oso/9780199291793.003.0017)만 확인 · (c) Wenger, McDermott, Snyder, *Cultivating Communities of Practice*, HBS Press, 2002
- 문헌 유형: 학술 단행본 / 경영 잡지 기고 (seminal)
- 핵심 개념: 실천 공동체(CoP) = 영역(domain)·공동체(community)·실천(practice)의 3요소. 흔히 인용되는 정의 "groups of people who share a concern or a passion for something they do and learn how to do it better as they interact regularly"는 Wenger-Trayner의 후기(2015) 소개문 출처 — 1998 원서 문장이 아님 [주의].
- 독자 전달 제안: 사내 AX 커뮤니티(사내 AI 사용자 모임·챔피언 네트워크)를 설계하는 이론 틀. DevRel의 외부 커뮤니티 운영 경험이 그대로 전이되는 지점. 인용 시 출처 판본 구분.

---

## [E] 논문 42: Beyond Training: How Workers Discover Value in Enterprise AI
- 저자·연도: Riya Sahni, Lydia B. Chilton (Columbia, 2025)
- 발표처: arXiv 프리프린트 (v1 제목 "Beyond Training: Social Dynamics of AI Adoption in Industry") [게재처 미확인]
- DOI/arXiv: arXiv:2502.13281 (v1 2025-02-18, v2 2025-10-06)
- 문헌 유형: preprint (탐색적 인터뷰)
- 표본·방법: M365 Copilot을 쓰는 미국 경력 전문가 10명 인터뷰, Rogers 확산 이론으로 해석.
- 핵심 수치 (abstract, 표본 10명): 공식 교육을 주된 학습 경로로 꼽은 사람 0/10. 시행착오 8/10, 동료와 팁 교환 6/10. 주 용도: 노트·요약, 정보 검색·설명, 글쓰기. 효율 향상 체감, 고급 기능 숙달 자신감은 낮음.
- 인용할 만한 문장: "Findings reveal a strong preference for informal learning methods over structured training."
- "{연도} 기준": 2024~2025 / 표본 10명 — "경향 시사" 수준으로만 인용
- 독자 전달 제안: 사내 AX에서 "교육 과정"보다 "동료 간 팁 교환 채널"이 효과적이라는 시사 — DevRel식 커뮤니티 운영이 사내에서 먹히는 이유. 반드시 n=10 라벨.

---

## [E] 논문 43: AI Adoption Across a Multinational Workforce: Sociotechnical Conditions for GenAI Acceptance in Human Resources
- 저자·연도: Dalia Ali, Maria José Rodríguez Velázquez, Manoel Horta Ribeiro, Vera Liao, Orestis Papakyriakopoulos (2026)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2606.17887 (2026-06-16)
- 문헌 유형: preprint (혼합 방법 사례 연구)
- 표본·방법: 다국적 테크 기업의 레거시 HR 검색 → GenAI 시스템 전환기. 검색 로그 + 설문(n=25) + 반구조화 인터뷰 10건.
- 핵심 결과: 채택은 시스템 설계 가정과 직원의 업무 위치(역할·언어·근속)의 적합도에 좌우. 신뢰는 출처 확인·시스템 비교·의심 시 동료나 HR에 묻기로 형성.
- 인용할 만한 문장: "They also need to treat the organizational knowledge infrastructure as AI infrastructure to improve the accountability and usability of GenAI systems"
- "{연도} 기준": 2026
- 독자 전달 제안: "조직 지식 인프라 = AI 인프라" — 사내 문서화가 사내 AX의 전제. 외부 DevRel의 "문서가 에이전트 인터페이스"(축 D) 논지의 사내 버전으로 연결.

---

## [F] 논문 44: Social Barriers Faced by Newcomers Placing Their First Contribution in Open Source Software Projects
- 저자·연도: Igor Steinmacher, Tayana Conte, Marco Aurélio Gerosa, David Redmiles (2015)
- 발표처: CSCW 2015 (18th ACM Conference on Computer Supported Cooperative Work & Social Computing), pp. 1379–1392
- DOI/arXiv: https://doi.org/10.1145/2675133.2675215
- 문헌 유형: peer-reviewed 학회 (seminal)
- 표본·방법: 체계적 문헌 리뷰 + OSS 기여자 개방형 응답 + OSS에 기여한 학생 + 14개 프로젝트 개발자 36명 반구조화 인터뷰의 질적 분석.
- 핵심 결과 (abstract): 신규 참여자 장벽 개념 모형 — 장벽 58개, 그중 사회적 장벽 13개. 첫 기여 시기가 이탈이 잦은 구간.
- 관련: 같은 연구 계열의 체계적 문헌 리뷰 — Steinmacher, Graciotto Silva, Gerosa, Redmiles, "A systematic literature review on the barriers faced by newcomers to open source software projects," Information and Software Technology, Vol. 59, pp. 67–85, 2015, doi:10.1016/j.infsof.2014.11.001
- 인용할 만한 문장: "Newcomers' seamless onboarding is important for online communities that depend upon leveraging the contribution of outsiders."
- "{연도} 기준": 2015
- 독자 전달 제안: DevRel의 온보딩 설계 근거. AI 시대의 질문 — 신규 참여자의 "첫 질문"을 AI가 흡수하면 장벽은 낮아지는가, 아니면 커뮤니티와의 첫 접점이 사라지는가? Burtch et al.(논문 2)의 "신규 사용자 이탈 집중" 결과와 짝지으면 강력.

---

## [F] 논문 45: Almost There: A Study on Quasi-Contributors in Open-Source Software Projects
- 저자·연도: Igor Steinmacher, Gustavo Pinto, Igor Scaliante Wiese, Marco Aurélio Gerosa (2018)
- 발표처: ICSE 2018 (40th International Conference on Software Engineering), pp. 256–266
- DOI/arXiv: https://doi.org/10.1145/3180155.3180208
- 문헌 유형: peer-reviewed 학회
- 표본·방법: 인기 GitHub 프로젝트 21개의 PR 데이터 + 준기여자·통합자 설문 + PR 263개 수동 분석.
- 핵심 수치 (abstract): 준기여자(PR이 한 번도 수락되지 않은 외부 개발자) 10,099명 — 실제 기여자 총수의 약 70% — 가 미수락 PR 12,367개 제출. 5개 프로젝트에서는 준기여자가 실제 기여자보다 많음. 설문 응답자 약 1/3이 미수락에 동의하지 않았고, 약 30%는 미수락이 동기를 꺾거나 다음 PR을 막았다고 응답. 주된 사유: "대체/중복 PR", "개발자와 팀의 비전 불일치".
- 인용할 만한 문장: "This empirical study is particularly relevant to those interested in fostering developers' participation and retention in OSS communities."
- "{연도} 기준": 2018
- 독자 전달 제안: 커뮤니티 매니지먼트의 핵심은 "거절의 경험 설계". 에이전트 PR 시대(논문 47·48)에 준기여자 문제가 사람→에이전트로 폭증할 가능성과 대비.

---

## [F] 논문 46: Open Source Community Health: Analytical Metrics and Their Corresponding Narratives
- 저자·연도: Sean Goggins, Kevin Lumbard, Matt Germonprez (2021)
- 발표처: SoHeal 2021 (IEEE/ACM 4th International Workshop on Software Health in Projects, Ecosystems and Communities), pp. 25–33
- DOI/arXiv: https://doi.org/10.1109/SoHeal52568.2021.00010
- 문헌 유형: peer-reviewed 워크숍
- 표본·방법: Linux Foundation 작업 그룹 CHAOSS(Community Health Analytics Open Source Software)의 결성 후 첫 4년을 참여형 현장 연구로 분석.
- 요약: 오픈소스 프로젝트는 측정이 쉬운 "활동량" 지표로 평가되지만 평가자의 진짜 질문은 "경쟁·의존 프로젝트 맥락에서 이 프로젝트는 얼마나 건강하고 지속 가능한가". 트레이스 데이터만의 한계를 짚고, 기업-커뮤니티 파트너십으로 지표 표준을 만드는 방법을 제시. 비교·투명성·궤적·시각화를 강조.
- 인용할 만한 문장: "How healthy and sustainable is this project in the context of its competitors or dependent projects?"
- 후속: Lumbard, Germonprez, Goggins, "An empirical investigation of social comparison and open source community health," Information Systems Journal, 34(2):499–532, 2023/2024, doi:10.1111/isj.12485 [내용 미확인]
- "{연도} 기준": 2021
- 독자 전달 제안: DevRel 지표론 — 활동량(스타 수·이벤트 참석자·MCP 서버 수)은 쉽지만 건강을 말해주지 않는다. SPACE(논문 28)와 같은 논리를 커뮤니티에 적용.

---

## [F] 논문 47: On the Use of Agentic Coding: An Empirical Study of Pull Requests on GitHub
- 저자·연도: Miku Watanabe, Hao Li, Yutaro Kashiwa, Brittany Reid, Hajimu Iida, Ahmed E. Hassan (2025)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2509.14745 (v1 2025-09-18, v3 2026-02-09)
- 문헌 유형: preprint
- 표본·방법: Claude Code로 생성된 GitHub PR 567개, 오픈소스 프로젝트 157개.
- 핵심 수치 (abstract): 83.8%가 최종 수락·머지, 머지된 PR의 54.9%는 추가 수정 없이 통합, 나머지 45.1%는 사람의 수정(버그 수정·문서·프로젝트별 표준 준수)을 거침. 에이전트는 주로 리팩터링·문서화·테스트에 사용.
- "{연도} 기준": 2025 (Claude Code 단일 도구 — 에이전트 PR 전체로 일반화 금지. 사람이 에이전트를 써서 올린 PR로 선택 편향 가능)
- 독자 전달 제안: 에이전트가 오픈소스 "기여자"가 되는 현실. 커뮤니티 매니저가 에이전트 기여를 위한 가이드(CONTRIBUTING·AGENTS.md)를 써야 하는 이유.

---

## [F] 논문 48: Why Are Agentic Pull Requests Merged or Rejected? An Empirical Study
- 저자·연도: Sien Reeve O. Peralta, Fumika Hoshi, Hironori Washizaki 외 (2026)
- 발표처: MSR 2026 (23rd International Conference on Mining Software Repositories) 승인, 5쪽 (mining challenge 트랙으로 보임 [트랙 미확인])
- DOI/arXiv: arXiv:2605.22534 (2026-05-21)
- 문헌 유형: peer-reviewed 학회 short paper (승인) / preprint
- 표본·방법: 닫힌 에이전트 PR 11,048개 → 사람이 리뷰한 9,799개 → 대표 사례 717개 수동 검토.
- 핵심 수치 (abstract): 거절된 PR 중 명확한 에이전트 실패는 35.7%, 워크플로 제약 31.2%, 결정 근거 관찰 불가 33.1%. 머지된 PR 중 15.4%는 리뷰어의 명시적 개입(피드백·직접 커밋) 필요. Copilot·Devin은 리뷰어 매개 워크플로에, Codex·Cursor PR은 최소 상호작용으로 머지되는 경향.
- 인용할 만한 문장: "rejection outcomes substantially overstate agent error"
- "{연도} 기준": 2025~2026 에이전트 세대
- 독자 전달 제안: 커뮤니티 매니지먼트가 "사람-에이전트 혼합 기여자"를 다루는 일로 바뀌는 근거. 수락률 하나로 에이전트를 평가하지 말라는 지표론과도 연결.

---

## [F] 논문 49: Generative AI and the Nature of Work
- 저자·연도: Manuel Hoffmann, Sam Boysel, Frank Nagle, Sida Peng, Kevin Xu (2024)
- 발표처: Harvard Business School Working Paper 25-021 / SSRN 5007084 (2024-10) [저널 게재 미확인]
- DOI/arXiv: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084
- 문헌 유형: working paper (준실험, 회귀 불연속 설계)
- 표본·방법: GitHub Copilot 무료 제공 자격 기준(인기 오픈소스 메인테이너)의 임계값을 이용한 회귀 불연속. 2년간 수백만 건의 작업 활동. (검색 요약 기반 — abstract 원문 직접 확보 실패)
- 핵심 결과 (2차 요약): Copilot 접근이 개발자의 작업 배분을 핵심 업무(코딩) 쪽으로, 비핵심 프로젝트 관리 활동에서 멀어지게 이동. 기제: 협업보다 자율 작업 증가, 활용(exploitation)보다 탐색(exploration) 증가. 상대적으로 능력이 낮은 개인에서 효과가 큼. [구체 %: 미확인]
- "{연도} 기준": 2022~2024 Copilot
- 독자 전달 제안: AI가 메인테이너의 "협업·조율" 시간을 줄인다 — 커뮤니티를 돌보는 일(=DevRel/커뮤니티 매니저의 영역)이 개발자 개인에게서 빠져나간다는 해석 가능. 단 원문 확인 전 수치 인용 금지.

---

## [C] 논문 50: Informational Help-Seeking on Reddit Did Not Decline After ChatGPT
- 저자·연도: Hazem Ibrahim, Yasir Zaki (NYU Abu Dhabi, 2026)
- 발표처: arXiv 프리프린트 (2026-09-11 — 검색 시점 기준 2주 전 공개, 동료 검토 전)
- DOI/arXiv: arXiv:2609.12447
- 문헌 유형: preprint (최신, 미검증)
- 표본·방법: Reddit 정보성 커뮤니티 26개 vs 규모 비교 가능한 취미 커뮤니티 90개, ChatGPT 출시 전후 같은 달력 6개월 월별 게시물 수. ChatGPT 이전 66개 시점에서 위약(placebo) 분석 반복. AI 텍스트 탐지기로 게시물 274,411개·댓글 223,775개 채점.
- 핵심 수치 (abstract): 정보성 도움 요청은 감소하지 않음 — 3.4%보다 큰 감소 배제 (선행 연구의 8~25% 감소와 대비). AI 작성 게시물은 정보성 커뮤니티에서 취미 커뮤니티 대비 2~3%p만 더 증가. 저자 추정 최대치(저위험 호기심 커뮤니티 게시물 18% 감소)는 기존 추세와 일치. 선행 연구의 불일치는 동시기 통제 없이 ChatGPT 이전부터 있던 커뮤니티 유형 간 추세 이탈을 효과로 오인했기 때문일 수 있다고 주장.
- 인용할 만한 문장: "Humans still ask humans for help, and, as far as detection can tell, humans still answer them."
- "{연도} 기준": 2026-09 프리프린트 / 데이터 2022-05~2023-05 창 [정확한 창은 본문 미확인]
- 독자 전달 제안: Burtch et al.(논문 2)의 "Reddit은 감소 없음"을 독립적으로 뒷받침하며, "LLM이 커뮤니티를 죽였다"는 서사의 일반화를 경계하는 최신 반론. 단 대상이 Reddit(비 Stack Overflow)이고 프리프린트임을 명시. Stack Overflow 감소를 부정하는 연구가 아님.

---

## [C] 논문 51: An exploratory analysis of Community-based Question-Answering Platforms and GPT-3-driven Generative AI: Is it the end of online community-based learning?
- 저자·연도: Mohammed Mehedi Hasan, Mahady Hasan, Mamun Bin Ibne Reaz, Jannat Un Nayeem Iqra (2024)
- 발표처: arXiv 프리프린트 [게재처 미확인]
- DOI/arXiv: arXiv:2409.17473 (2024-09-26)
- 문헌 유형: preprint
- 표본·방법: 2022년 1~12월 Stack Overflow Python·JavaScript 질문 2,564개에 대해 ChatGPT(API) 답변과 채택 답변 비교(텍스트 지표 4·인지 지표 4) + 2년간 SO 상호작용 지표 3개 + 전문가 14명 보조 설문.
- 핵심 수치 (abstract): ChatGPT 답변이 66% 더 짧고, 질문과 공유 단어 35% 많고, 긍정 감정 25% 높음. 정확도 71~75%. Stack Overflow 댓글 상호작용 최근 38% 감소.
- 인용할 만한 문장: "While Stack Overflow provides benefits from the accumulated crowd-sourced knowledge, it often suffers from unpleasant comments, reactions, and long waiting times."
- "{연도} 기준": GPT-3.5 계열, 2022~2024
- 독자 전달 제안: 사람들이 LLM으로 옮겨간 이유는 정확도만이 아니라 "불친절함·대기 시간" — 커뮤니티 경험(Community Experience)의 실패. DevRel이 운영하는 커뮤니티가 살아남으려면 무엇이 달라야 하는지의 역설적 근거. 38% 감소의 측정 기간 정의는 본문 확인 필요.

---

## [B] 논문 52: Who is using AI to code? Global diffusion and impact of generative AI
- 저자·연도: Simone Daniotti, Johannes Wachs, Xiangnan Feng, Frank Neffke (2026, Complexity Science Hub 등)
- 발표처: Science, Vol. 391, Issue 6787, pp. 831–835 (2026-02-19; 온라인 2026-01-22)
- DOI/arXiv: https://doi.org/10.1126/science.adz9311 · arXiv:2506.08945 (v1 2025-06-10, v2 2025-11-20)
- 문헌 유형: peer-reviewed 저널 (관찰 연구, 신경망 분류기)
- 표본·방법: AI 생성 Python 함수를 판별하는 신경망 분류기로 GitHub 커밋 3,000만 개 이상 분석. **개발자 수: Science 게재본 160,097명 / arXiv 판 "170,000명"**.
- 핵심 수치 (Science abstract): 미국 Python 함수의 추정 29%를 AI가 작성(타국 대비 우위는 줄어드는 중). 이로 인해 분기 산출(온라인 코드 기여)이 3.6% 증가. 경험 많은 시니어 개발자는 생산성 향상과 새 영역 진출, 초기 경력 개발자는 유의한 이득 없음.
- 인용할 만한 문장: "This may widen skill gaps and reshape future career ladders in software development."
- "{연도} 기준": 데이터는 2024년 말까지 (2차 보도: 2022년 약 5% → 2024 4분기 약 30% [본문 미확인])
- 독자 전달 제안: Peng et al.(논문 5, 저경력자가 더 이득)과 **정반대 방향**의 결과 — 실험실 단일 과제 vs 실사용 대규모 관찰의 차이. DevRel이 "AI가 초보자를 개발자로 만든다"고 말할 때 이 논문을 균형추로. "29%"는 "미국, Python 함수, 분류기 추정"이라는 세 겹 라벨 필수 — "코드의 29%"로 확대 금지.

---

## [A] 논문 53: 소프트웨어 생태계 건강 — 기준 문헌 2편 (메타데이터만 확인)
- (a) Konstantinos Manikas, Klaus Marius Hansen, "Software ecosystems – A systematic literature review," Journal of Systems and Software, Vol. 86, No. 5, pp. 1294–1306, 2013-05. doi:10.1016/j.jss.2012.12.026 — peer-reviewed SLR, 피인용 약 470회(OpenAlex 2026-09 기준).
- (b) Slinger Jansen, "Measuring the health of open source software ecosystems: Beyond the scope of project health," Information and Software Technology, Vol. 56, No. 11, pp. 1508–1519, 2014-11. doi:10.1016/j.infsof.2014.04.006 — peer-reviewed.
- 한계: 두 논문 모두 abstract 확보 실패(API 미제공·출판사 403). 요약·수치 [미확인]. 생태계 건강을 생산성·견고성·틈새 창출(Iansiti & Levien 2004 비즈니스 생태계 개념에서 차용)로 보는 틀이 이 계열에서 널리 쓰인다고 알려져 있으나 원문 대조 전 본문 인용 금지.
- 독자 전달 제안: DevRel 성과 지표를 "생태계 건강"으로 격상하는 논의의 학술 계보로만 짧게 언급. 수치 인용 없음.

---

# 책에 쓰기 위험한 오인용 수치

| # | 흔한 오인용 | 원문 확인 결과 | 안전한 표현 |
|---|---|---|---|
| 1 | "ChatGPT 이후 Stack Overflow 질문이 16% 줄었다" 또는 "25%" 혼용 | 16%는 프리프린트 v1(2023-07) 주간 게시물 추정치, 25%는 PNAS Nexus 2024 게재본의 "출시 6개월 내, 러시아·중국·수학 포럼 대비 상대적 활동 감소" | "del Rio-Chanona 외(PNAS Nexus, 2024)는 ChatGPT 출시 후 6개월 동안 Stack Overflow 활동이 비교 플랫폼 대비 약 25% 줄었다고 추정했다(차분의 차분, 저자들은 하한으로 해석)" |
| 2 | "Stack Overflow 방문자가 12% 줄었다" 를 질문 수 감소로 확대 | Burtch 외(2024)의 12%는 **일일 웹 트래픽**(하루 약 100만 명) 추정치. 질문량은 별도 | "일일 웹 트래픽 약 12%" 로만 |
| 3 | "Reddit도 죽었다" / "커뮤니티 전반이 붕괴" | Burtch 외: Reddit 개발자 커뮤니티 감소 증거 없음. Ibrahim & Zaki(2026 프리프린트): Reddit 정보성 요청 3.4% 초과 감소 배제 | 감소는 Stack Overflow형 정보 교환 플랫폼에 집중, 관계형 커뮤니티는 버텼다 |
| 4 | "ChatGPT 답의 52%가 틀린다"를 현재 AI 일반론으로 | Kabir 외(CHI 2024), 2023년 ChatGPT(GPT-3.5 계열), SO 질문 517개 기준 | "2023년 당시 ChatGPT의 Stack Overflow 질문 답변 517개 중 52%가…" |
| 5 | "Copilot 쓰면 55% 빨라진다" | Peng 외(2023 프리프린트): Upwork 모집 95명, JS HTTP 서버 단일 과제, 완료 시간 55.8% 단축(95% CI 21–89%). GitHub 소속 저자 포함 | 실험 조건·표본·신뢰구간 병기 |
| 6 | "AI 쓰면 개발자가 19% 느려진다" 일반화 | METR(2025 프리프린트): 숙련 OSS 개발자 16명, 과제 246개, 2025년 초 도구(Cursor+Claude 3.5/3.7). 체감은 20% 빨라짐 | "숙련 개발자가 자기 대형 저장소에서 일할 때"라는 조건 필수 |
| 7 | "고객지원 생산성 14% 향상" vs "15%" | NBER WP(2023): 14%, 초보 34%, 5,179명 / QJE 게재본(2025): 15%, 5,172명 | 게재본 기준 15%, 판본 명시 |
| 8 | "BCG 컨설턴트 품질 40% 향상" | WP(2023) abstract에만 있음, Organization Science 게재본(2026) abstract에는 "significantly improved quality"로 약화. 12.2%·25.1%는 양쪽 동일 | 12.2%·25.1% 사용, 40%는 "2023 워킹페이퍼 기준" 라벨 |
| 9 | "프런티어 밖에서 19% 덜 정확" | 게재본 abstract는 "19% less likely", 본문은 84.5% → 60%/70.6%, "19 percentage points" | "19%p"(퍼센트포인트) |
| 10 | "미국 코드의 29%를 AI가 쓴다" | Daniotti 외(Science 2026): **미국·Python 함수·분류기 추정** 29%. 개발자 수 게재본 160,097 vs arXiv "170,000" | 세 겹 라벨 유지, 개발자 수는 게재본 |
| 11 | "AI는 초보자를 가장 많이 돕는다"(단정) | Peng(실험)·Brynjolfsson(고객지원)은 저숙련 이득 ↑, Daniotti(Science 2026, 실사용 관찰)는 초기 경력 개발자 **유의한 이득 없음** | 과제·맥락에 따라 방향이 갈린다고 서술 |
| 12 | "AGENTS.md를 쓰면 에이전트 성능이 오른다" | Gloaguen 외(2026 프리프린트): 성공률 개선 없음·비용 20%+ 증가. Khatri(2026): 정확성 영향 측정 불가. 효율 개선 보고(Lulla 외)는 원문 미확인 | "효과는 논쟁 중, 비표준 규칙 명시에만 유용하다는 결과" |
| 13 | "MCP 도구 설명 97%가 불량" 을 "MCP 서버 97%" 로 | Hasan 외(2026): **도구 856개**의 설명 중 97.1%가 스멜 1개 이상 (서버 103개) | 단위는 "도구 설명" |
| 14 | "최종 사용자 프로그래머 5,500만 명" | Boehm(1995) 예측. Scaffidi 외(2005)는 이것이 사실상 컴퓨터 사용자 수였다고 비판, 2012 미국 추정: 스프레드시트·DB 사용자 5,500만+, 자칭 프로그래머 1,300만+, 전문 프로그래머 300만 미만 | 출처를 Scaffidi 외 2005 "추정"으로 |
| 15 | Rogers 채택자 비율(2.5/13.5/34/34/16%)을 조직 실측처럼 | 정규분포를 표준편차로 나눈 이론적 범주 | "이론적 구분" 명시 |
| 16 | "DevEx는 Greiler·Storey·Noda(ACM Queue 2023)" | Queue 논문 저자 순서는 Noda·Storey·Forsgren·Greiler. Greiler·Storey·Noda는 IEEE TSE 논문(인터뷰 21명) | 두 문헌 구분 |
| 17 | "Robillard: 개발자 440명 조사" | IEEE Software 2009 논문은 설문 응답 83명(유효 80). 440명+는 확장판(EMSE 2011)의 누계로 추정 [미확인] | 2009 논문 인용 시 83명 |
| 18 | ACM Queue·CACM 기고(DevEx·SPACE)를 "peer-reviewed 논문" 으로 | 실무자 대상 학술 잡지 기고 | "ACM Queue에 발표한 프레임워크" |
| 19 | "Wenger: CoP는 관심·열정을 공유하고 정기적으로 교류하며 더 잘하게 되는 집단" 을 1998 원서 인용으로 | 해당 문장은 Wenger-Trayner 후기 소개문(2015) 출처 | 출처를 후기 소개문으로 |

---

# 커버리지 메모 (paper-researcher, 2026-09-25)

- 축별 수록: A 11편(24~33, 53) / B 13편(5~16, 52) / C 6편(1~4, 50, 51) / D 7편(17~23) / E 10편(34~43) / F 6편(44~49). 총 53개 항목(단행본·묶음 항목 포함).
- 원문(본문) 대조까지 한 수치: del Rio-Chanona(abstract 두 판본), Burtch(본문 12%), Peng(본문 표본·CI), METR(abstract), Scaffidi(본문), Robillard(본문), Dell'Acqua(WP·게재본 본문), Brynjolfsson(두 판본 abstract), Daniotti(두 판본 abstract), Da Silva(본문).
- abstract만 확인 / [미확인] 다수: Fagerholm·Münch의 인지·정동·의욕 3요소, DevEx 3차원 원문 문장, Howell & Higgins 원문, Tushman 원문, Manikas & Hansen·Jansen, Hoffmann 외 수치, Cybernetic Teammate 효과 크기.
- 학술 공백 (웹 리서처 영역으로 넘김): llms.txt 학술 연구 없음(Ahrefs 블로그 수준 자료만 존재), "Agent Experience(AX)" 개념의 학술 문헌 미발견 — SWE-agent의 "에이전트는 새로운 범주의 최종 사용자"가 가장 가까운 학술 근거. DevRel 직무 변화(감원·FDE 확장)에 대한 학술 연구 미발견. AI 챔피언 프로그램 효과를 정량화한 peer-reviewed 연구 미발견(질적 소표본 연구만).
