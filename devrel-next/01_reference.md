# AI 시대 DevRel의 변화 레퍼런스

> 슬러그 `devrel-next` · genre `tech-book` · 검색 시점 **2026-09-25** · 합성: research-lead
> 1차 근거 파일(보존, 삭제 금지): `research/web.md`(웹 W-x-y), `research/papers.md`(논문 P-n), `research/community.md`(커뮤니티 C-x-y). 본 문서의 괄호 번호가 그 파일의 항목 번호다. fact-checker는 본문 주장을 여기 → 원 파일 순으로 대조한다.
> 라벨 규약: [1차]=당사자 공식 발표·문서·공고, [언론]=언론 보도, [설문]=설문(주체·표본 병기), [논문-PR]=동료 검토, [프리프린트], [WP]=워킹페이퍼, [벤더]=이해관계 있는 벤더 자사 데이터, [블로그/의견], [커뮤니티]=익명·개인 발언, [예측], [미확인], (확인 필요).
> 익명화: 저자 소속 회사·그룹 계열 정보는 수집·수록하지 않았다(커뮤니티 리서처가 계열 블로그 1건 제외). 아래 한국 사례의 카카오·토스·우아한형제들은 모두 공개 자료다.
> 익명화 예외(저자 승인, 2026-09-25, `00_direction.md` 저자 결정 기록 (3)(4)): 데보션(DEVOCEAN) **공개 게시물**은 공개 글에 적힌 내용만 쓴다(사내 정보 추가·원장 금지 수치 인용 금지, 원 파일 `research/devocean.md`). 저자 본인 공개 글은 「말하지 않고 만들었다」(2026-06-30)·「DevRel 커뮤니티 6번째 모임을 참여하며」(2023-04-03) 두 편만 1인칭 근거로 쓰고, 회사명은 참고문헌에만 둔다. 그 밖의 저자 글·저자 관련 제3자 글(서평·발표 후기·NotebookLM 생성 글)은 쓰지 않는다.

---

## 0. 한눈에 보기 — 이 레퍼런스가 말하는 것

1. **DevRel은 원래 "경계 역할"이었다.** 에반젤리즘(Apple 1984) → Advocate(양방향) → 측정 압박(DRL·AAARRRP·Orbit) → ZIRP 종료기 감원(2022~24) → "죽었다/돌아왔다" 논쟁(2024~26) → 직무 정의의 제도화(LF DRF, 2025-08).
2. **'Dev'가 넓어졌다.** 바이브 코딩(Karpathy 2025-02, Collins 올해의 단어 2025) + 빌더 도구의 폭증(Lovable·Replit·Bolt·v0·Claude Code·Cursor). 동시에 전문 개발자 도구도 폭증 — 'Dev 확장'은 '전문 개발자 축소'와 동의어가 아니다. 학술적으로는 "비전문가가 대부분의 프로그램을 쓴다"는 말이 2011년에 이미 있었다(Ko et al.).
3. **새 청중이 생겼다 — 에이전트.** llms.txt(2024-09), MCP(2024-11 → LF AAIF 2025-12), Agent Experience(Biilmann 2025-01), Stripe·Vercel·Cloudflare·Supabase·GitHub의 MCP/에이전트용 문서. 벤더 데이터로는 문서 요청의 과반이 에이전트(단위 주의). 반론도 강하다(llms.txt 미소비, AGENTS.md 효과 논쟁, MCP=마케팅 신호).
4. **직무가 해체·재조립된다.** 2026-09-25 공개 채용 목록 스냅샷에서 AI 랩·도구사의 'DevRel' 제목 공고는 소수, Applied AI·FDE·Solutions는 다수. 동시에 Anthropic·Vercel·Supabase는 DevRel 공고를 새 정의(에이전트 인프라, 제품 조직 내 배치, 'builders' 청중)로 내고 있다. 직함은 흩어지고(Head of AI education, MTS, FDE, DX Engineer, Developer Education Lead), 일의 핵심(외부와 제품 사이 번역·피드백 루프)은 공고 문구에 그대로 남아 있다.
5. **DevRel 기술이 사내로 향한다.** Block(Angie Jones: CEO가 전사 AI 확산을 DevRel에 맡김), 카카오(DevRel 담당자가 AI 마일리지 프로그램 운영·인사관리학회 발표), Anthropic "Developer Education Lead"(사내 GTM 대상). 학술 뿌리: Rogers 확산 이론, 혁신 챔피언(Howell & Higgins 1990), 경계 역할(Tushman 1977), 실천 공동체(Wenger).
6. **'R(관계)'이 살아남는 축이라는 실증 후보.** Stack Overflow(정보 교환형)는 LLM 이후 활동이 줄었지만 Reddit 개발자 커뮤니티(관계형)는 감소 증거가 없었다(Burtch et al. 2024; Ibrahim & Zaki 2026 프리프린트).

---

## 1. 개념과 정의

### 1-1. DevRel의 정의 (출처별)
| 정의 | 출처 | 라벨 |
|---|---|---|
| "create a vibrant ecosystem of 3rd party developers, by being the interface between those developers and your platform's product, engineering, and design teams" | Google DevRel 미션, Phil Leggetter 인용 (2016-02-03) W-1-3 | [블로그, 1차 인용] |
| "Our job is to inspire and equip developers to build the next generation of amazing applications..." | Twilio 미션, Leggetter 인용 W-1-3 | [블로그] |
| DevRel = keystone(플랫폼 중심 조직)이 서드파티 개발자의 임계 질량을 끌어들이고 참여시키기 위한 생태계 거버넌스 기능. 모델 DevGo(초점 영역 4·성장 단계 3·스테이지 6·교훈 62) | Fontão et al., J. Softw. Evol. Process 35(5), 2023 (온라인 2021-10), doi:10.1002/smr.2389 P-24 | [논문-PR] DevRel 직접 연구로 드묾 |
| "The Developer Relations (DevRel) is a strategy to attract, engage and mature developers in contributing to a platform." | Massanori et al., SBES 2020, doi:10.1145/3422392.3422445 P-25 | [논문-PR short] |
| "DevRel has always been a role that defies simple definition. It's not marketing, but it overlaps with marketing. It's not sales, but it supports sales." | Lee Briggs, 2024-12-10 W-2-3 | [블로그/의견] |
| PR이 일반인에게 기업을 알린다면 DR은 개발자에게 기업을 알리는 활동 | kt cloud 기술블로그, 2024-11-04 C-8-3 | [블로그] 국내 통념 예시 |
| LF DRF 결성문은 명시적 정의 없이 "product, marketing, support, engineering and sales"를 잇는 일로 기술, 결성 배경 "a lack of role clarity and difficulty in measuring impact" | Linux Foundation, 2025-08-25 W-2-8 | [1차] |

### 1-2. 에반젤리스트 → 애드보킷
- Guy Kawasaki의 1984년 직함 "software evangelist" — 서드파티 개발자에게 매킨토시용 소프트웨어를 만들도록 설득(위키 요약 2차 + 본인 블로그 회고 "Mike Boich started evangelism and hired me"). W-1-1 [중]
- Microsoft DPE(2012 보도) → Cloud Developer Advocate. "Advocate는 양방향(회사를 대변하는 동시에 개발자를 대변해 제품팀에 전달), Evangelism은 일방향"이라는 논리. **Sam Ramji 발언 귀속은 [미확인] → "업계에서 흔히 설명되는 논리"로만.** W-1-2

### 1-3. 측정·운영 프레임워크 (계보)
| 프레임 | 핵심 | 출처·날짜 |
|---|---|---|
| AAARRRP (Phil Leggetter) | Awareness·Acquisition·Activation·Retention·Referral·Revenue·Product. AARRR에 Awareness·Product 추가. 회사 유형별 목표 상이 | leggetter.co.uk, DevRelCon London 2016 W-1-3 |
| DevRel Qualified Leads (Mary Thengvall) | 커뮤니티에서 발견해 사내 적절한 팀으로 연결한 사람 = 가치. 단 영업 지표 씌우기엔 반대 | marythengvall.com 2019-12-14 W-1-5 |
| Orbit Model (Josh Dzielak 외) | Gravity = Love × Reach, "커뮤니티는 퍼널이 아니다". 2019-11 공개 | GitHub orbit-love W-1-6. **후일담:** Orbit사는 2024-04-11 Postman 인수 발표, 제품 종료(데이터 수집 2024-05-31 중단·기능 2024-07-11 비활성 — 2차 정리) |
| Developer Journey Map (Lewko & Parton) | Discover → Evaluate → Learn → Build → Scale | 『Developer Relations: How to Build and Grow a Successful Developer Program』 Apress 2021 W-1-7 |
| 『The Business Value of Developer Relations』 | DevRel 가치 증명의 고전. 한국어판 『기업의 성공을 이끄는 Developer Relations』(조은옥 옮김, 한빛미디어 2022-06-03) | Apress 2018 W-1-4, W-8-4. **책 속 정의 문장 원문 [미확인]** |
| DX(Developer Experience) | "a means for capturing how developers think and feel about their activities within their working environments" — 출발점부터 생태계 외부 개발자를 포함 | Fagerholm & Münch, ICSSP 2012 P-26 [논문-PR]. 인지·정동·의욕 3요소는 본문 재확인 권장 |
| DevEx 3차원 | 피드백 루프·인지 부하·몰입 | Noda·Storey·Forsgren·Greiler, ACM Queue 2023 P-27 **(peer-reviewed 논문 아님 — 실무자 대상 잡지 기고)**. 실증 기반은 Greiler·Storey·Noda IEEE TSE 2023(인터뷰 21명) P-29 |
| SPACE | Satisfaction·Performance·Activity·Communication·Efficiency — 단일 지표 불가 | Forsgren et al., ACM Queue 2021 P-28 |
| CHAOSS | 활동량 지표 vs 건강·지속가능성 질문 | Goggins et al., SoHeal 2021 P-46 |

### 1-4. 새 용어
| 용어 | 정의·명명 | 출처 |
|---|---|---|
| Vibe coding | "There's a new kind of coding I call "vibe coding", where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." | Karpathy X, 2025-02-02 W-3-1 [1차] |
| Vibe coding (사전) | "the use of artificial intelligence prompted by natural language to write computer code" — Collins Word of the Year 2025 | Collins, 2025-11-06 W-3-2 [1차] |
| AI Engineer | 파운데이션 모델 위에서 제품을 만드는 엔지니어 | swyx, Latent Space 2023-06-30 W-5-1 |
| Agent Experience (AX) | "the holistic experience AI agents will have as the user of a product or platform." 계보: UX(Don Norman 1993) → DX(Jeremiah Lee 2011, Biilmann 서술) → AX | Mathias Biilmann(Netlify CEO), 2025-01-28 W-4-6 [1차] |
| AX = DX + UX | "agent experience is a combination of developer experience and user experience"(기사 서술) | Dana Lawson(Netlify CTO), The New Stack 2026-06-06 C-9-1 |
| ACI (Agent-Computer Interface) | "LM agents represent a new category of end users with their own needs and abilities" | Yang et al., SWE-agent, NeurIPS 2024 P-18 [논문-PR] — **AX의 가장 가까운 학술 근거** |
| End-user programming | "Most programs today are written not by professional software developers, but by people with expertise in other domains" | Ko et al., ACM Computing Surveys 2011 P-12 [논문-PR] |
| FDE (Forward Deployed Engineer) | 전략 고객에 임베드되는 엔지니어. Palantir 기원은 보도의 일반 서술(Palantir 1차 [미확인]) | FT(2025-11 추정), a16z 2025-06-04 W-5-2 |
| Machine funnel / Human funnel | 문서·구조화 콘텐츠·MCP(정확성) vs 영상·워크숍·서사(신뢰). "Stop trying to make one piece of content serve both." | Dewan Ahmed, 2026-08-11 갱신 W-5-6 [블로그] |
| 세 개의 유통 표면 | human developers, search crawlers, LLMs | Joe Karlsson, 2026-04-20 C-6-4 [블로그] |
| Dev Zero | 출시 전 신기능을 "complete stranger"로 먼저 써보는 역할 | Joe Karlsson C-6-4 |
| DevRel Engineering | 작동하는 프로토타입·도구가 콘텐츠를 대체하는 주 가치 흐름 [예측] | Liran Tal 2026 W-9-4; Karl Weinmeister(Google) "FDE at scale = DevRel Engineering"(Medium 원문 미대조) C-5 |

> **책 장치 메모 (00_direction 교차점, 출처 확인 완료):** 해외 DevRel 담론의 "AX"는 Agent Experience — 명명자 Mathias Biilmann, 2025-01-28 개인 블로그(1차). 저자의 AX(AI Transformation)와 약어가 겹친다. "AX 용어가 12개월 내 VC 메모에 등장, AX Specialist 채용 등장"은 2차 용어집 주장 → **사용 금지**.

---

## 2. 축별 발견

### 축 1. 정의와 계보 — 요지
- 에반젤리즘의 기원은 "플랫폼에 서드파티 개발자를 끌어오는 일"(Apple 1984). DevRel은 태생부터 **플랫폼 경제학**의 기능이다 — Parker, Van Alstyne & Jiang(MIS Quarterly 2017, P-33): "The locus of value creation moves from inside the firm to outside." / "More developers give platform firms more chances at success."
- 이론적 원형은 **경계 역할(boundary role)** — 조직 안팎 정보를 번역·중개(Tushman, ASQ 1977, P-40; 원문 abstract 미확보, 인용 전 확인).
- DevRel이 생태계를 살리지 못한 사례: Symbian(2012)·Firefox OS(2016)·Windows Phone(2017) — "DevRel만으로 생태계를 살릴 수 없다"(Massanori et al. 2020, P-25, Windows Phone SO 질문 46,030개).
- 가치 측정 논쟁은 오래 "증거보다 의견·일화"(Chris Reddington, 2026-03-11, Warwick MBA 논문 기반, 질적 인터뷰 n=13: 전술 활동과 조직 전략 성과의 연결을 명확히 보인 사람 2명, 약 15%) W-1-8.

### 축 2. DevRel 위기 — 요지
**설문 (라벨 필수)**
- State of Developer Relations 2024 (11th, DevRel.Agency 운영, 스폰서 Common Room 등, 2024-09-10 발표) — 유효 응답 310명(완료 242), 33개국, 자기선택 표본. 개인 해고 경험 **14.6%**, 프로그램 단위 인원 채용 27% / 해고로 감소 18.1% / 재편 22.1%, 중위 기본급 $150,000(2023 $175,000), 정의된 커리어 경로 없음 61%, AI 사용 약 78%(미사용 21.8%). W-2-5. **2025판은 2026-09-25 기준 확인 못함.** "영향력 증명 어려움 61%" 수치는 검색 요약 수준 — Joe Karlsson 재인용 "60.7%"(C-6-4)와 함께 원문 확인 필요.
- Common Room 2023 DevRel Compensation & Culture Report (2023-08-31, n=136, 벤더 설문) — "73.9% ... did not experience layoffs" → 역산 26.1%는 **팀 단위** 해고 경험. 번아웃 경험 67.1%. W-2-6

**감원 (DevRel 단독 수치 아님)**
- Google 2023-01 약 12,000명(6%) — 해고된 직무에 developer relations 포함(9to5Google, SNS 증언 기반) W-2-7
- Twilio 2022-09 11%, 2023-02 약 17%, 2023-12 약 5% [언론] W-2-7
- 특정 기업 "DevRel 팀 전원 해고" 단정은 1차 미확인 → **금지**.
- 1인칭 기록: David Neal "My role has been eliminated"(Bluesky 2023-07-25), Salma Alam-Naylor 2023년 "made redundant ... moving away from a community-centred approach to an enterprise-based strategy"(블로그 2026-07-02), Raymond Camden Webflow 구조조정으로 해고(Bluesky 2026-05-27). C-2-1, C-5-2, C-9-2

**"죽었다" 담론의 세 갈래**
| 입장 | 대표 | 인용 |
|---|---|---|
| 거품 교정론 | swyx, "DevRel's Death as Zero Interest Rate Phenomenon" (dx.tips/zirp, HN 제출 2024-07-08 → 발행 2024-07 이전) | "ZIRP DevRel is dead ... the 'Jobs To Be Done' of DevRel are timeless needs" |
| 자기 실패론 | Keith Casey, "A Painful Reckoning" 2024-07-17 | "Developer Relations is dying because devrel failed their organizations." / "If Marketing can't measure your contribution, you don't fit into their budget." |
| 재구조화론 | Lee Briggs, 2024-12-10 (작성 당시 Tailscale Sales Engineer — 본인이 DevRel→SE 이동 사례) | "Professionals who adapt—aligning their work with sales, customer success, or product teams—will continue to thrive." |
| 부활론 | swyx, "DevRel Is -Unbelievably- Back" (HN 2025-10-13) | "reports of DevRel's death have been greatly exaggerated" — 검색량 5배는 본인도 과장 가능성 인정. Cursor가 LeeRob, Cognition이 swyx 채용 |
| 이탈 선언 | Salma Alam-Naylor, "Goodbye, forever, probably." 2026-07-02 (DevRel → Staff Engineer) | "If DevRel is to survive, I think it will need to look entirely different from how it functioned during the last ten years." / 섹션 제목 "AI is killing developer education" |
| 절충 | r/devrel Daria-Dovzhikova 2026-09-14 [커뮤니티] | "the role isn't dying. the headcount version is. ... "advocate" was a salary with no number on it. that's what got cut." |

**제도화**
- Linux Foundation Developer Relations Foundation: 결성 의향 2024-09-16 → 공식 결성 2025-08-25(OSS Europe, Amsterdam). 미션 "Elevate the professional practice of developer relations and increase awareness of it as a driver of business value." 산출물 Persona Library(24), Tools Catalog(36), Events Directory. 인물 Stacey Kruczek 등. W-2-8 [1차]
- 병치(해석은 저자 몫): 같은 LF가 2025년에 DRF(8월)와 Agentic AI Foundation(12월, MCP 기증처)을 모두 품었다.

### 축 3. 'Dev'의 확장 — 요지
**상징적 순간:** Karpathy 트윗(2025-02-02) — 1주년 회고에서 "a shower of thoughts throwaway tweet". Collins 올해의 단어(2025-11-06).

**빌더 도구 수치 (모두 출처 라벨 병기)**
| 제품 | 수치 | 시점 | 라벨 |
|---|---|---|---|
| Lovable | ARR $200M(7월 $100M에서 2배), 일 방문 500만, 하루 신규 프로젝트 10만, Discord 10만+ | 2025-11-18 | [회사 발표] W-3-3 |
| Replit | 연환산 매출 $150M, 기업가치 $3B | 2025-09-10 | [언론 TechCrunch] |
| Replit | $400M 조달·기업가치 $9B, 연말 run-rate $1B **목표** | 2026-03 | [회사 게시] (리드 투자자 표기 상이 — 확인 필요) W-3-4 |
| Claude Code | "just six months after becoming available to the public, it reached $1 billion in run-rate revenue" | 2025-12-03 | [1차 Anthropic] W-3-5 |
| Claude Code | run-rate $2.5B+, 주간 활성 사용자 연초 대비 2배 | 2026-02 | [언론 Reuters 보도 — research-lead 자기 검증 시 확인; Anthropic 1차 원문 문장은 미대조] |
| Cursor | run-rate $2B(2026-02)→$3B(04말)→$4B(06초), 약 75% 기업 고객 | 2026-06 | [언론, 익명 소식통] W-3-6 |
| Bolt.new | 출시(2024-10) 당시 StackBlitz ARR 약 $80K → 5개월 후 ~$40M, 20명 미만 | 2025 상반기 | [CEO 인터뷰 발언] W-3-7 |
| v0 | 사용자 350만 (Series F $9.3B 시점) | 2025-09 | [언론 요약, 보도자료 원문 403] W-3-8 |

- 포지셔닝 문구: Lovable "everyone should be able to build software. Not just the 1% who can code" / "Welcome to the age of the builder"(2025-11). Replit Amjad Masad "We don't care about professional coders anymore"(Semafor 2025-01-15), "Replit is about making everyone a software engineer"(2026-03). v0.app "anyone"(2025-08).
- **전문 개발자 도구도 동시 폭증**(Cursor·Claude Code의 기업 매출 비중) → "Dev 확장 ≠ 전문 개발자 축소"(W-3-6 해석).

**개발자 인구**
- GitHub Octoverse 2025(2025-10-28, 데이터 2024-09~2025-08): "180 million-plus developers"(= **GitHub 계정 수**, 직업 개발자 아님), 신규 3,600만+(+23%), "nearly 80% of new developers on GitHub use Copilot in their first week", 2025-08 TypeScript 최다 언어, 인도 2030 미국 추월 [예측]. W-3-9
- Octoverse 2024: Python이 JavaScript 추월, 생성형 AI 프로젝트 98%↑. 총 개발자 수는 원문 재확인 필요. W-3-10
- Stack Overflow Developer Survey 2025(약 49,000명, 개발자 한정 자기선택): AI 사용·계획 84%, 정확도 불신 46% vs 신뢰 33%, 긍정 정서 60%(2023~24 70%+에서 하락), 최대 불만 "almost right, but not quite" 66%, 에이전트 월 1회 이상 31%. W-3-11 → **전문 개발자의 회의 vs 비개발 빌더의 열광 — DevRel이 두 청중을 동시에 상대**.

**학술 기준선·균형추**
- Scaffidi, Shaw & Myers(VL/HCC 2005, P-13): 2012년 미국 직장 **추정** — 최종 사용자 9,000만, 스프레드시트·DB 사용자 5,500만+, 자칭 프로그래머 1,300만+ vs BLS 전문 프로그래머 300만 미만. "5,500만 최종 사용자 프로그래머"는 Boehm(1995) 예측이며 이 논문은 그것이 사실상 컴퓨터 사용자 수였다고 비판.
- Sarkar & Drosos(PPIG 2025, P-7): "vibe coding does not eliminate the need for programming expertise but rather redistributes it toward context management, rapid code evaluation, and decisions about when to transition..."
- Feldman & Anderson(CHIWORK '24, 비프로그래머 67명, P-14): 비전문가의 장벽은 "several aspects of technical communication" → **정확히 DevRel의 전문 영역**.
- Thorgeirsson et al.(CHI 2026, 학생 N=100, P-10): 글쓰기 능력·CS 성취도가 바이브 코딩 성과를 예측.
- Virk & Liu(VL/HCC 2025, P-15): "business professionals cannot reliably verify AI-generated data analyses on their own".
- Chou et al.(FSE 2026 승인, 영상 20개, P-9): 디버깅을 "주사위 굴리기"로 묘사, 코드를 안 보는 부류~검토하는 부류 스펙트럼.
- Pimenova et al.(프리프린트 2025, 19만 단어, P-8): 커뮤니티가 모범 사례를 스스로 발견·공유.
- Tang et al.(ACM 2026, 세션 11,579개·개발자 899명, P-11): "externalizing plans into persistent artifacts".
- 생산성 실증은 방향이 갈린다: Peng et al.(프리프린트 2023, n=95, 단일 과제) 55.8% 빠름·저경력 더 이득 / METR(프리프린트 2025, 숙련 OSS 16명·과제 246개) 19% 느려짐, 체감은 20% 빨라짐 / Daniotti et al.(Science 2026, 개발자 160,097명) 미국 Python 함수 추정 29% AI 작성, **초기 경력 개발자는 유의한 이득 없음**. P-5, P-6, P-52

**현장 목소리(커뮤니티)**
- "I don't have to be a "real developer" anymore — I just need to describe what I want clearly." / "it gave me permission to build again." (HN Show HN ivcatcher, 2026-01-19, OP 진위 의심 댓글 있음 — 확인 필요) C-3-1
- "In this sense LLMs are another wave of "end-user programming" like excel formula." (HN mjburgess 2026-01-19)
- 보안·유지보수: Replit 에이전트 DB 삭제(Jason Lemkin X 2025-07-18), Lovable 호스팅 앱 1.8만 명 노출(The Register 2026-02-27 보도, HN), "death spiral of errors"(Lee Robinson 2025-07-21). C-3-2, C-3-3, C-5
- 상한론: "Will vibe coding end like the maker movement?" — "a small fraction of people"(roxolotl, HN 2026-02-26); "vibe coding may just be happening without an audience"(a1o). C-3-2

### 축 4. 새 청중: 에이전트 — 요지
**표준·프로토콜 타임라인**
| 날짜 | 사건 | 출처 |
|---|---|---|
| 2024-09-03 | llms.txt 제안(Jeremy Howard, Answer.AI) "to provide information to help agents use a website" | llmstxt.org [1차] W-4-1 |
| 2024-11-25 | MCP 발표 — "a new standard for connecting AI assistants to the systems where data lives". 초기 도입 Block·Apollo·Zed·Replit·Codeium·Sourcegraph | Anthropic [1차] W-4-3 |
| 2025-01-28 | Agent Experience 명명 | Biilmann [1차] W-4-6 |
| 2025-04-04 | GitHub 공식 MCP 서버 퍼블릭 프리뷰 | GitHub changelog [1차] |
| 2025-04-07 | Cloudflare 원격 MCP 서버("industry's first" — 자기 주장) | Cloudflare [1차] |
| 2025-04 / 2025-10 | Supabase MCP 서버 / 원격 MCP (날짜 원문 확인 권장) | Supabase blog [1차] |
| 2025-08 | 카카오 PlayMCP 베타("국내 최초" — 자기 주장) | kakaocorp [1차] W-8-2 |
| 2025-08-06 | Vercel MCP 퍼블릭 베타(read-only, OAuth) | Vercel blog [1차] |
| 2025-12-09 | LF Agentic AI Foundation 결성 — MCP(Anthropic)·goose(Block)·AGENTS.md(OpenAI). 1년 성과: 월 SDK 다운로드 9,700만+, 활성 서버 1만+ [주체 발표] | LF·MCP blog [1차] |
| 검색 시점 판 | Stripe "building-with-ai": 원격 MCP, Agent Toolkit, Agent skills 카탈로그(`/.well-known/skills/index.json`), 모든 docs URL에 `.md` 붙이면 마크다운. 첫 줄 "Give an AI agent access to Stripe, and build products that agents can use." | docs.stripe.com [1차] W-4-4 |
| 2026-08-04 | Google Cloud: Developer Advocate·Technical Writer가 이끈 태스크포스가 Agent Skills 제작 — "a skill is a living product, not a one-off document", GitHub 스타 15,000+ [회사 발표] | Google Cloud blog [1차] W-5-6 |

- Stripe llms.txt의 에이전트 지시문 예: "Always use the Checkout Sessions API over the legacy Charges API"(Apideck 블로그 2026-02-23 2차 인용 — 원문 docs.stripe.com/llms.txt 직접 확인 권장). 해석: 학습 데이터 속 구식 API 추천을 문서 쪽에서 교정.

**에이전트 트래픽 데이터 (벤더)**
- Mintlify, "The state of docs traffic: a 2026 midyear report"(2026-07-29): "Agents now account for 66% of measured web-traffic"(2026-07), 7월 에이전트 웹 요청 2억 1,300만 vs 사람 페이지 로드 1억 500만, 연초 15.2%. **단위가 다르다(요청 vs 페이지 로드)**, 식별 한계 자인, 벤더 이해관계. research-lead가 원문 재확인(2026-09-25). "Claude Code 단독 1억 9,940만 요청"은 이 보고서에 없음 → 다른 글(state-of-ai) 수치로 [미확인]. W-4-5, C-6-5

**DevRel 채택 경로가 바뀐 일화**
- Thor Schaeff(DevRelCon NY 2025-07, 발표 자동 전사본): Bolt·Lovable 등이 Supabase를 "without ever talking to us" 통합 — LLM이 "use Supabase"라고 추천. "just in the last quarter ... basically the same amount of signups as in the last four years"는 **발표자 구두 주장, Supabase 1차 미확인**. 이유 가설: 전 스택이 오픈소스·Postgres 30년 → LLM 학습 지식. C-5-1
- Joe Karlsson(2026-04-20): "In an AI coding assistant, the AI is solving a problem directly. It's not shopping. You have to already be there." / "your README, your examples directory, your API reference, and your SDK docs are your LLM marketing." C-6-4
- Sourcegraph 발표(Stephanie Jarmak) 전언: '쇼핑' 프롬프트에서 약 65% 추천, '근본 문제' 프롬프트에서 0회 — r/devrel jcasman 전언, 발표자 자체 테스트 → (확인 필요). C-2-5
- 비개발 빌더도 "AI가 스택을 골랐다"(HN ivcatcher, GeekNews 비개발 게임 개발자의 Supabase 채택 2025-06-17). C-3-1, C-8-1

**학술 근거**
- Hsieh et al.(프리프린트 2023, P-17): "We advocate the use of tool documentation ... over demonstrations." — 문서만 준 zero-shot이 few-shot과 동등 이상.
- Hasan et al.(프리프린트 2026, MCP 서버 103개·도구 856개, P-19): **도구 설명**의 97.1%가 스멜 1개 이상, 56% 목적 불명. 보강 시 성공률 중앙값 +5.85%p, 대신 실행 단계 +67.46%, 16.67% 퇴행.
- Hasan et al.(프리프린트 2025/v5 2026-04, 서버 1,899개, P-20): 7.2% 일반 취약점, 5.5% tool poisoning.
- Guo et al.(프리프린트 2025-09, 유효 프로젝트 8,401, P-21): "Are MCP marketplaces truly growing, or merely inflated by placeholders and abandoned prototypes?" — 허영 지표 경계.
- Chatlatanagulchai et al.(프리프린트 2025, 컨텍스트 파일 2,303개, P-22): 보안 14.8%·성능 14.5%만 명시, "evolve like configuration code".
- Gloaguen et al.(프리프린트 2026, P-23): 컨텍스트 파일이 성공률을 일반적으로 개선하지 않고 추론 비용 평균 20%+ 증가, "저장소 개요"는 무익, **비표준 관행 명시에는 유용**. Khatri(2026)도 정확성 영향 측정 불가.
- 사람 문서 연구의 연속성: Robillard(IEEE Software 2009, 응답 83명) API 학습 방법 문서 78%·예제 55%·동료 질문 29% / Uddin & Robillard(2015, 323명) 모호성·불완전성·부정확성, 10개 중 6개 문제가 다른 API로 갈아타게 하는 blocker / Meng et al.(2017) "need to involve the expertise of communication professionals". P-30~32

**반론 (별도 박스로 서술할 것)**
- John Mueller(Google): "FWIW no AI system currently uses llms.txt." / "comparable to the keywords meta tag"(2025, 언론 인용) W-4-2
- HermanMartinus(블로그 플랫폼 운영자 자칭, 약 8만 블로그): "/llms.txt is not requested by anything" (HN 2026-06-05) — 반박: 주요 벤더는 게시, GitBook 요청 관측, "게시와 소비는 다르다". 대안 "Accept: text/markdown". C-6-2
- MCP "marketing signal not a technical one"(HN 2026-03-01) vs 엔터프라이즈·비개발 사용자에겐 필수. C-6-6
- xena(HN 2026-09-18): "a 100% score on ax-check ... has not 10xed the growth numbers like I was told it would." (2024-07엔 같은 계정이 "recently broken into DevRel") C-9-1
- Tailwind 딜레마: Adam Wathan "making it easier for LLMs to read our docs just means less traffic to our docs"(GitHub PR #2388, 2026-01-06) — 축 6 참조.
- **서술 원칙:** SEO 신호로서의 llms.txt(회의론 강함)와 코딩 에이전트·MCP가 문서를 직접 가져가는 개발자 문서 맥락(벤더 데이터가 효과 주장)을 분리한다. "llms.txt가 표준이 됐다" 단정 금지.

### 축 5. 직무 재편·새 직함 — 요지
**공개 채용 목록 스냅샷 (2026-09-25 확인, Greenhouse/Ashby 공개 API, [1차 스냅샷 — 추세 지표 아님])**
| 회사(전체 공고 수) | DevRel 인접 공고 관찰 |
|---|---|
| Anthropic (627) | Applied AI Architect 계열 20건+(서울 포함), FDE 4 + 매니저 2 + Pre-Sales(FDE) 1, **Developer Relations 1**, Developer Education Lead 1, Copywriter, Developer 1 |
| OpenAI (827) | "Forward Deployed" 제목 22건, Developer Experience Engineer, Cyber 1, "Developer Advocate" 제목 0 |
| Vercel (87) | DevRel Engineer, Agentic Infrastructure 1, FDE 1, SA 다수 |
| Supabase (55) | Developer Relations Engineer 3(SF·NY·런던) |
| Cloudflare (382) | FDE 계열 10건 안팎, VoidZero Developer Relations Engineer 1(근무지 후보 서울 포함) |
| Cursor (125) | FDE 계열 7~9, SA 다수, DevRel 제목 0 |
| Replit (75) / Lovable (79) / ElevenLabs (221) / Stripe (694) | FDE 1 / Community Manager·SA / DX Engineer 1 / DevRel 제목 0 |
| Hugging Face·Google DeepMind·Mintlify | 조회 실패 [미확인] |

**공고 원문 인용 (URL은 W-5-3~5-5)**
- Anthropic Developer Relations(updated 2026-08-21): "help developers discover, onboard, and get the most out of Claude Code, Claude Tag, and future developer products" / "Help define what world-class AI developer relations looks like in this emerging field" / "from individual hobbyists to enterprise engineering teams" / "Build frameworks and mechanisms for measuring developer success" / "Act as an advocate for developer needs at Anthropic, translating developer feedback into concrete product and content initiatives". **연봉 "$290,000 — $435,000 USD"(OTE, 영업 보너스 포함 범위로 명시)** — research-lead가 Greenhouse API로 재확인(2026-09-25).
- Anthropic Developer Education Lead, Claude Platform(updated 2026-09-21): 청중이 **사내 GTM 조직** — "let Anthropic's go-to-market teams showcase the Claude Developer Platform with confidence" / "You're an engineer who teaches." / "You know the difference between a demo that raises awareness and one that creates champions." → 내부 DevRel의 공식 직무.
- Anthropic FDE(updated 2026-08-21): "embeds directly with our most strategic customers" / "Deliver technical artifacts for customers like MCP servers, sub-agents, and agent skills" / "contribute insights back to our Product and Engineering teams"(DevRel 피드백 루프와 동형).
- Anthropic Copywriter, Developer: "an audience that is notoriously allergic to being marketed to" / "sits between Dev Rel's technical content and pure marketing" → 콘텐츠 업무 분화.
- OpenAI Developer Experience Engineer, Cyber(2026-09-11): "The Developer Experience team at OpenAI has a singular focus: empowering developers globally." / "the developer journey, from onboarding with Codex to first API call to production deployment" → 도메인(보안) 특화. (공고 속 모델명은 미검증 — 본문 인용 시 제외 권장)
- Vercel DevRel Engineer, Agentic Infrastructure(2026-09-17): "Vercel is the agentic infrastructure company, freeing people and agents to ship what's next." / "work inside the product teams" / "Applications without one will not be considered."(가르친 결과물 링크 필수) / "your job is to hit the rough edges first" / 보고 라인 Head of AI Infrastructure(제품 조직 배치).
- Supabase DevRel Engineer(2026-08-21): "Our users are builders, startup founders, weekend hackers, and engineers scaling to millions of users." / "350,000+ developers"(공고 내 자기 서술).
- Cloudflare VoidZero DevRel: "someone who identifies as a builder, teacher, mentor, and communicator". 배경 Cloudflare의 VoidZero 인수(2026-06-04, "to Build the Future of the AI-Native Web").
- 과거 공고(마감 추정, 스니펫만): Anthropic "Developer Relations, MCP" — "growing the MCP developer ecosystem".

**FDE 급증 보도**
- FT "The new hot job in AI: forward-deployed engineers"(X 게시 2025-11 초 추정, 페이월 미정독). 2차 인용상 FDE 월간 공고 2025-01~09 800%+ 증가 — **원 데이터 제공자 [미확인] → "FT 보도에 따르면" 라벨만**.
- a16z Joe Schmidt, "Trading Margin for Moat"(2025-06-04, VC 에세이): "services-led growth", "sometimes rebranded as a forward deployed engineer or an implementation/solutions specialist", 당시 OpenAI 공개 채용 311건 중 FDE·솔루션 22건(a16z 집계). Palantir 언급 없음.

**직함 이동 1인칭 기록 [커뮤니티/블로그]**
| 인물 | 이동 | 출처 |
|---|---|---|
| Lee Robinson | Vercel(5년) → Cursor, "teach the future of coding" / "More people are becoming developers because of AI, but they're not learning the right skills" | X 2025-07-18, Substack 2025-07-21 C-5 |
| cameron.stream | Letta "founding devrel engineer"(2025-07) → "Member of Technical Staff"(2026-06-16) | Bluesky C-5-2 |
| Raphael De Lio | Redis Developer Advocate → FDE (Medium 403, 요약만) | 2026-08 C-5-1 (확인 필요) |
| Salma Alam-Naylor | DevRel → Staff Engineer | 2026-07-02 C-2-1 |
| Lee Briggs | DevRel → Sales Engineer(Tailscale) | 2024-12 W-2-3 |
| Dona Sarkar (Microsoft) | "AI Power Users DevRel team" 맡음 — 청중이 AI 파워유저로 확장 | Bluesky 2025-01-17 C-5-2 |
| Fly.io | "Is it DevRel? Not exactly. It's closer to a journalist ... not asking for evangelists – we're looking for storytellers." | Bluesky 2025-06-11 |
| Kelsey Hightower | 클라우드 네이티브 DevRel의 AI 인프라 전환 기회 공지 | Bluesky 2025-07-22 |
| swyx | DevRel(Netlify·AWS·Temporal·Airbyte 이력으로 알려짐 — 확인 필요) 출신이 "AI Engineer" 명명, 2025 Cognition 합류(본인 서술) | W-5-1, C-2-4 |

**DevRel 인물의 발전 방향 제안 [블로그/의견]**
- Patrick Chanezon(2025-11-07, DevRel 20년): 3방향 — (1) 개발자가 AI 코딩 에이전트를 잘 다루게 가르치기, (2) 개발자 서비스의 AX 최적화, (3) DevRel 업무 자체의 AI 전환. "Will the model remember you?" W-5-6
- Rizèl Scarlett, "How to Lead DevRel in the AI Era: Stop Playing It Safe" — **발행 2025-09-16**(research-lead 재확인; community.md의 "2026-09-16" 표기는 오기). 작성 당시 Block goose DevRel 리드, 검색 시점 프로필 "Principal Developer Advocate at Entire". "Even though I was a leader, I continued to build." / "Developers aren't the only ones reading your documentation anymore; AI agents read them too." / 릴리스마다 문서 갱신 GitHub Action / "forty-thousand-dollar networking breakfasts that yield zero long-term developer adoption". W-5-6, C-5-3
- Dewan Ahmed(2026-08-11 갱신): "Technical credibility is still earned by building, not by talking about building" / "A great DevRel team still cannot save a bad product" / "You are hired to remove a cost or a risk". W-5-6
- Liran Tal(2026): "DevRel Engineering", "code is cheap", 범용 콘텐츠 ROI 하락 [예측]. W-9-4

**DevRelCon 현장 (1차 발표 기록·참관기)**
- DevRelCon NYC 2026 참관기(Ayodeji Ogundare, LinkedIn Pulse 2026-07-25): "Developer Relations is not disappearing, but its audience, interfaces, and measures of success are changing." 컨퍼런스 질문 — "What does developer experience mean when many builders do not identify as developers?" / Jess Lee·Mike Swift 세션 "DevRel Is Dead. Long Live DevRel." — 청중이 수천만 전문 개발자에서 "around a billion people who can build with software"로 [주장·예측] / Nikita Jotwani "DevRel for a Developer You'll Never Hear From" / Joey de Villa·Sean Keegan "What changed because this DevRel work existed?" / Hahnbee Lee "Treat agent instructions and skills as maintained product surfaces, much like SDKs." C-5-1 (참관기 요약이므로 발표 원문 대조 권장)
- AI Engineer World's Fair 2026 취재(Dev.to Daily Context, 2026-07-02): "AI products fail at integration, not awareness." / "DevRel owns the top of the funnel ... FDE owns the bottom ... What gets squeezed is the middle." / "A conference talk earns applause, but a merged PR in the customer's repo earns a renewal." C-2-4

### 축 6. 콘텐츠·커뮤니티의 변화 — 요지
**Stack Overflow 감소 (학술 — 헤드라인은 1·2만 사용)**
- del Rio-Chanona, Laurentsyeva & Wachs, PNAS Nexus 3(9), 2024, doi:10.1093/pnasnexus/pgae400: "Within 6 months of ChatGPT's release, activity on Stack Overflow decreased by 25% relative to its Russian and Chinese counterparts ... and to similar forums for mathematics." 저자들은 하한으로 해석. (프리프린트 v1의 16%와 혼용 금지) P-1
- Burtch, Lee & Chen, Scientific Reports 14:10413, 2024: 일일 웹 트래픽 약 100만 명/일(직전 트래픽의 약 12%) 감소, **감소는 신규·주니어 사용자에 집중**, "activity in Reddit communities shows no evidence of decline, suggesting the importance of social fabric as a buffer". P-2
- Ibrahim & Zaki, arXiv:2609.12447(2026-09-11, **동료 검토 전**): Reddit 정보성 도움 요청 3.4% 초과 감소 배제 — "Humans still ask humans for help". P-50
- Kabir et al., CHI 2024(질문 517개, 2023 ChatGPT): 답변 52% 부정확·77% 장황, 사용자는 35% 선호·39% 오류 미인지. **2023 모델 기준.** P-3
- Da Silva et al.(JSS 2025): 답변 수 -22% → 1년 이후 구간 -52% — **구간 정의 확인 전 사용 금지**. P-4
- Hasan et al.(프리프린트 2024): 사람들이 LLM으로 옮긴 이유에 "unpleasant comments, reactions, and long waiting times" — 커뮤니티 경험의 실패. P-51
- 현장 체감: "SO was clearly on the decline ... It peaked around 2017 ... ChatGPT just pushed it off the cliff"(HN 2026-05-26), 2014년 이후 모더레이션 강화로 "the site felt unwelcome". 지식이 비색인 Discord·Slack으로 파편화(bloppe, HN 2025-05-15), "there won't be a new Stack Overflow to train LLMs on"(jmyeet). C-6-1

**문서 트래픽·퍼널의 탈동조화 — Tailwind (1차 당사자 증언, GitHub PR #2388)**
- Adam Wathan 2026-01-07: "Traffic to our docs is down about 40% from early 2023 despite Tailwind being more popular than ever. The docs are the only way people find out about our commercial products" / "our revenue is down close to 80%" / "75% of the people on our engineering team lost their jobs here yesterday". **조사 주체: 회사 자체, 방법 미공개. 75%는 엔지니어 4명 중 3명**(HN stephenson, Business Insider 제목과 일치). 후속: Google AI Studio 후원(HN 2026-01-08). 반론: 트래픽이 아니라 전환율을 봐야 한다(zdragnar). C-6-3

**콘텐츠·교육 수요의 변화 [커뮤니티]**
- Salma: "People aren't seeking information in the ways we once knew; The Internet and its communities have fragmented." / 익명 동료 재인용 "The forums are dead, the new Discord is quiet."(확인 필요)
- Josh W. Comeau 재인용(원 게시물 [미확인]): 세 번째 강의가 통상의 약 1/3 판매 궤도, LLM 개인 튜터링과 직업 불안의 이중 타격.
- Angie Jones: "SEO is basically dead (sorry). ... Check your referrers and you'll see ChatGPT is bringing you your future community members." C-7-1
- r/devrel: "channel problem, not a content problem" — 앉아서 읽는 개발자의 시간 슬롯이 사라짐, "Another channel is agents"(2026-06). C-2-5
- AI 슬롭 역류: Rachel Andrew "proposals for content for Google DevRel sites ... obvious AI slop"(Bluesky 2026-09-22), Jake Archibald "These accounts used to be run by DevRel. Now they're run by marketing."(2026-04-07, 운영 주체는 작성자 주장). C-5-2
- 'AI 치어리딩' 우려: "every devrel position includes AI cheerleading at this point"(2025-09-11), "chatgpt ads but with an api"(2025-05-21), Jen Looper "push back on demands to use AI for all the things, especially in DevRel"(2025-12-21).
- Rizèl Scarlett: AI 데모 콘텐츠의 유통기한 — "once models improved, it felt like an outdated trick".

**커뮤니티 매니지먼트의 새 대상: 에이전트 기여자 (학술)**
- Watanabe et al.(프리프린트 2025, Claude Code PR 567개): 83.8% 머지, 머지된 것 중 54.9% 무수정. P-47
- Peralta et al.(MSR 2026, 닫힌 에이전트 PR 11,048개): "rejection outcomes substantially overstate agent error", 머지된 15.4%는 리뷰어 개입 필요. P-48
- 온보딩 기준선: Steinmacher et al.(CSCW 2015) 장벽 58개(사회적 13), Steinmacher et al.(ICSE 2018) 준기여자 10,099명(기여자 총수의 약 70%). P-44, P-45
- Hoffmann et al.(HBS WP 2024): Copilot 접근이 비핵심 프로젝트 관리 활동에서 코딩으로 작업 배분 이동 — **2차 요약, 수치 인용 금지**. P-49

### 축 7. 내부 DevRel / AI 확산 — 요지
**공개 사례**
- **Block — Angie Jones, "How DevRel Is Leading AI Adoption"(angiejones.tech 2025-10-20, DevRelCon 발표 기반)** — 책 논지와 가장 직접 연결되는 공개 사례.
  - "A couple years ago, everyone was asking if DevRel was dead. ... Well, plot twist: we're not dead. We're standing on the biggest stage of our careers."
  - 3년 키운 제품이 종료 → "instead of letting us go, leadership asked us to pivot to ... goose, an AI agent. ... We didn't know anything about AI agents."
  - "Going first. Figuring stuff out. Guiding others. That's literally what we do in DevRel."
  - "All 12,000 employees at my company now have access to goose. ... Guess who our CEO asked to lead this? DevRel." (**12,000명은 작성자 기술 — Block 공개 자료로 확인 필요**)
  - "we started teaching everyone – legal, marketing, design, research, executive assistants. ... We treated them like any other community of builders."
  - "We didn't position ourselves as AI experts. We positioned ourselves as people learning alongside the community" / "they don't trust your shiny demos ... They want to see the full, messy, real process." / "We help them move from fear to curiosity."
- **카카오 — DevRel 담당자 Sue(sue.cream)의 공개 기록 (tech.kakao.com)**
  - "Vibe Coding하는 비개발자는 개발자인가(1)"(2025-04-22): "저의 개발 모국어는 AI ... AI Monolingual ... 다르게 표현하자면, 저는 비개발자입니다." / 최소 필수 지식(MVK) — 지시의 의미·에이전트 처리 범위·클라이언트-서버·개발-배포 흐름 / "기다리는 것이 배우는 것보다 빠르다". (2)(2025-04-24): "필요한 도구를 찾는 것보다 내가 직접 만들어서 쓰는 것이 더 빠르다".
  - "생산성 혁신의 실험: AI 마일리지 프로그램"(2025-09-19): 상용 AI 도구 크레딧 지원, 약 3개월 시범 운영 100여 명·30여 조직·40여 과제. 3개월 차 설문 "이제는 도구 없이 개발하기 어렵다 68.4% / 불편하지만 감수 가능 31.6% / 전혀 문제 없다 0%" (**카카오 기술전략 자체 운영·사내 참여자 약 100명 설문 라벨 필수**). "원숭이 꽃신" 자문(의존인가 역량인가). "숫자로 보여드리는 것 이상의 실체 ... 개발자들의 실제 사례가 모이는 것". 역할이 '코더'에서 '코치'로 확장.
  - "한국인사관리학회에서 공유한 'AI 네이티브 전환'"(2025-10-30): 2024년부터 실험 — 1차(1인 개발자 1주 앱 프로토타입), 2차(1개 팀 50% 이상 생산성 향상 — 자사 수치), 2025-05~07 마일리지 시범. "AI 네이티브 전환은 단순한 기술 도입이 아니라, 일하는 방식과 조직문화를 함께 바꾸는 여정".
  - 카카오 "1K: 바이브코딩전"(joseph.choi, 2025-11-03): 비개발자 참가 허용, 1시간(실개발 35분) 99개 MVP, 목적을 "코딩 스킬이 아닌 아이디어 구현의 자신감과 재미"로, 예제 프롬프트로 "성공 경험을 복제 가능하게".
  - ※ 카카오는 저자 소속사가 아님 — 공개 자료 비교 인용 가능.
- **Anthropic Developer Education Lead** — 사내 GTM 대상 인에이블먼트 공식 직무(축 5).
- **Shopify — Tobi Lütke 메모 "Reflexive AI usage is now a baseline expectation"(X 공개 2025-04-07):** "The call to tinker with it was the right one, but it was too much of a suggestion." / "Learning is self directed, but share what you learned." / 성과평가 반영, 인력 요청 전 AI로 불가능함을 입증, #ai-centaurs 등 공유 채널. 현장 반응: 사용량 감시 공포(HN). C-7-2
- **Coinbase** — AI를 즉시 시도하지 않은 엔지니어 해고 발언(TechCrunch 2025-08-22) 및 HN 반발. **Zapier** — AI Fluency Rubric(Wade Foster X 2026-03-31: Capable/Adoptive/Transformative). 해커톤 후 사용률 10%→50%→97%는 CEO 구두 수치 [미확인]. C-7-2
- **냉소:** "AI-champion guy ... put a leaderboard ... praising guys with the cheapest LOC"(HN 2026-05-25), "Lie ... and become the biggest AI champion at your company"(HN 2026-05-13). → DevRel 허영 지표 문제의 재현. C-7-3

**이론·연구**
- Rogers, *Diffusion of Innovations* 5판(Free Press 2003; 초판 1962): 채택 속성 5가지(상대적 이점·적합성·복잡성·시험 가능성·관찰 가능성), 오피니언 리더·변화 촉진자, 동질성/이질성. 채택자 범주 %는 **이론적 구분**. 관찰 가능성·시험 가능성 ↔ DevRel의 데모·샌드박스, AX의 쇼케이스·파일럿. P-38 (원서 페이지 대조 미완)
- Howell & Higgins, ASQ 35(2), 1990: 챔피언은 변혁적 리더 행동·위험 감수·다양한 영향 전술(25쌍 비교, 원문 abstract 미확보). → 챔피언은 직함이 아니라 행동. P-37
- Greenhalgh et al., Milbank Quarterly 2004: 조직 확산의 체계적 리뷰(오피니언 리더·챔피언·경계 확장자 포함). P-39
- Tushman 1977 경계 역할 P-40; Wenger 실천 공동체(1998/2002; 흔한 정의 문장은 2015 후기 소개문 출처) P-41.
- Sahni & Chilton(프리프린트 2025, M365 Copilot 사용자 **n=10**): 공식 교육을 주 학습 경로로 꼽은 사람 0/10, 시행착오 8/10, 동료와 팁 교환 6/10. "strong preference for informal learning methods over structured training". P-42
- Ali et al.(프리프린트 2026): "treat the organizational knowledge infrastructure as AI infrastructure". P-43
- Brynjolfsson, Li & Raymond, QJE 140(2), 2025(상담원 5,172명): 생산성 평균 15%(WP 2023: 14%, 초보·저숙련 34%) — AI가 숙련자의 암묵지를 신입에게 옮김. P-34
- Dell'Acqua et al., Organization Science 2026(BCG 758명, WP 2023): 프런티어 안 과제 12.2% 더 많이·25.1% 더 빨리, 밖에서는 정답률 약 84.5% → 60%/70.6%(약 19%p 하락). "Jagged frontier" — AX 챔피언의 일은 프런티어가 어디인지 알려주는 것. P-35
- Dell'Acqua et al., "The Cybernetic Teammate"(NBER WP 2025, P&G 776명): AI를 쓴 개인 = AI 없는 팀, 기능 사일로 완화. P-36
- **학술 공백:** AI 챔피언 프로그램 효과를 정량화한 peer-reviewed 연구 미발견. "DevRel 역량이 AX 확산에 전이된다"의 근거는 (a) 이론(확산·챔피언·경계 역할·CoP)과 (b) 공개 사례(Block·카카오·Anthropic 공고)의 조합이지, 인과 실증이 아니다.

### 축 8. 한국 동향 — 요지 (확인된 것만)
- **토스:** SLASH(2021~, SLASH24 2024-09-12 첫 오프라인) → **토스 메이커스 컨퍼런스 25**(2025-07-23~25) — 개발자용 SLASH·디자이너용 Simplicity를 '메이커' 전체로 통합(세션 102·연사 126, 회사 발표). "메이커 = 개발자, 디자이너, PO, PM, DA 등". 'builder' 용어 확산과 병치 가능(인과 단정 금지). 2026년 개최 여부 [미확인]. W-8-1
- **카카오:** if(kakaoAI)2024 → if(kakao)25(2025-09-23~25) 기조세션에서 PlayMCP 등 에이전트 생태계. PlayMCP 베타 2025-08("국내 최초" 자기 주장), MCP 개발 공모전 'MCP Player 10'(10명, 총 2,100만 원 — 회사 발표). 내부 확산은 축 7. W-8-2
- **네이버 DEVIEW:** 2023-02-27~28 오프라인. 2024년 이후 개최 여부 [미확인] → "중단" 단정 금지. W-8-3
- **우아한형제들:** DevRel 담당자 채용(2022 추정, 채용 플랫폼 2차) — DevRel 팀이 "기술 조직 산하 Tech HR 실" 소속, "대내외 개발자들과의 관계를 바탕으로 ... 기술 조직을 알리는" 활동 → **한국 대기업형 DevRel = 채용 브랜딩 성격** vs 해외 플랫폼 기업형 = 제품 채택(대조점, 현재 조직 상태 [미확인]). W-8-4
- **CJ올리브영 DevRel 공고(현재 404, 검색 요약만):** 개발자 역량 내재화 교육·내부 지식 자산화·기술 가드레일 정의 — 내부 확산형 DevRel의 국내 변종 후보. **원문 재확인 필수.** C-8-3
- **GeekNews Weekly #350(2026-03):** "과거에는 Developer Evangelist가 컨퍼런스와 블로그, 샘플 코드를 통해 생태계를 키웠다면, 지금은 그 역할이 제품 안으로 더 깊이 들어와 핵심 레이어로 이동했습니다." / "개발자 생태계를 가진 쪽이 이깁니다. 다만 그 방식은 많이 달라졌습니다." (편집자 실명 미표기) C-8-1
- **국내 비개발 빌더:** GeekNews Show GN "비개발자가 바이브코딩으로 소울라이크 게임을 개발해보았습니다"(sltyphoon, 2025-06-17) — Supabase 채택, AI 간 교차검증, 구글플레이 출시, 확산 경로가 "지인의 10분 테트리스 시연"(1:1 전파). C-8-1
- **국내 커뮤니티 DevRel 활동 주제 이동:** "비개발자를 위한 바이브코딩 온라인 세미나"(velog jwclare95, 2025-08-01, 커뮤니티명 미기재), OKKY "AI시대 IT업계 일자리 위기 끝장토론회"(참관기 2025-06-01 — "AI 때문에 사람을 안 뽑는다(O) / AI로 대체되었기 때문에 안 뽑는다(X)"). C-8-2
- **GeekNews 논쟁:** "Vibe 코딩과 개발자 종말론"(2025-03-25), "바이브 코드는 레거시 코드임"(2025-08-02) — "와" vs "왜? 이렇게", "탈 수 있죠. 근데 만들진 못하겠죠". C-8-4
- **커뮤니티·출판:** DevRel KR(X 계정), 데브챗(검색 요약상 국내 DevRel 스터디·네트워킹 모임, 40여 명 — 원출처 URL [미확인]), 저자 공개 이력 『코드 너머, 회사보다 오래 남을 개발자』(데브챗 출신 7인 공저, 한빛미디어 2025) 독자 리뷰 존재 확인. Mary Thengvall 한국어판(2022).
- **글로벌 공고의 한국 근무지(2026-09-25):** Anthropic Applied AI Architect·Manager 서울, Cloudflare VoidZero DevRel 근무지 후보에 서울 — 'DevRel'보다 'Applied AI(고객 배치형)'가 많다는 스냅샷 관찰(일반화 금지). W-8-5
- **공백:** 국내 DevRel 인력 규모·채용 추이 수치 없음(지어내지 않음). 당근·토스 DevRel 전담 조직 공개 정보 미확인. OKKY·커리어리·링크드인 한국어 원문 미수집.

### 축 9. 발전 방향·전망 — 요지 (모두 [예측/의견])
| 인물·출처 | 날짜·장소 | 요지 |
|---|---|---|
| Jensen Huang | World Government Summit 2024-02-12 | "everybody in the world is now a programmer — that is the miracle."(보도 인용, 영상 원문 미대조) — 'Dev 소멸' 극단 |
| Dario Amodei | CFR 2025-03-10 | "in three to six months, where AI is writing 90% of the code ... in 12 months ... essentially all of the code." 단서 "The programmer still needs to specify..." → Gruber(Daring Fireball 2026-03-13) 회고: 사람 코드 대체가 아니라 코드 총량 폭증 |
| Andrew Ng (반대) | 2025 LinkedIn(원문 URL [미확인]) | "This advice will be seen as some of the worst career advice ever given." / "As coding becomes easier, more people should code, not fewer." |
| Mathias Biilmann | 2025-01-28 | AX를 설계하지 않으면 "risk being replaced"; "Agents will far more frequently be collaborators and extensions of humans, rather than replacements." |
| Dana Lawson (Netlify CTO) | The New Stack 2026-06-06 | "Every human assumption we removed made the platform better for everyone." / "billion new applications written by 2029"(기사 서술, 출처 불명 — 확인 필요) |
| swyx | 2024-07 / 2025-10 | 거품 교정 → "DevRel is back" |
| Lee Briggs | 2024-12-10 | 측정 가능한 대안 직무(Community Solutions Engineer 등) |
| Chanezon / Dewan Ahmed / Liran Tal | 2025-11 / 2026-08 / 2026 | AX 최적화·DevRel Engineering·machine/human funnel |
| DevRelCon NYC 2026 | 2026-07 | 청중 수천만 → 약 10억 빌더 [주장] |
| 반대·회의 | HN 2026-02~09 | 메이커 운동 상한론(roxolotl), AX ROI 미증명(cyanydeez), AX 100점에도 성장 없음(xena) |

**전망의 세 구도 (웹·커뮤니티 리서처 제안 통합)**
- (a) **해체론** — DevRel 기능이 FDE·SE·제품·마케팅·AI 교육으로 흩어진다(Briggs, a16z, HN hilariously, cameron.stream).
- (b) **확장론** — 청중이 빌더+에이전트로 넓어져 일이 늘어난다(Biilmann, Chanezon, DevRelCon NYC 2026, Anthropic·Vercel·Supabase 공고, Angie Jones).
- (c) **교정론** — 거품이 꺼졌을 뿐 본질은 같다(swyx ZIRP, Dewan Ahmed, Daria-Dovzhikova "headcount version").
- (d) **내향론** — DevRel 기술이 사내 AI 확산으로 향한다(Block, 카카오, Anthropic Developer Education Lead) — 위험: 의무화·사용량 지표가 감시·냉소를 낳는다.

---

## 3. 대표 사례 (본문 오프닝·사례 박스 후보)

| # | 사례 | 쓰임 | 강도 |
|---|---|---|---|
| S1 | Supabase가 "한 번도 말을 걸지 않고" AI 빌더에게 채택됨 (Thor Schaeff, DevRelCon NY 2025) | 새 청중=에이전트 장 오프닝 | 일화 강함 / 수치(4년치 가입=1분기)는 미확인 |
| S2 | Tailwind: 인기 최고, 문서 트래픽 -40%, 매출 약 -80%, 엔지니어 4명 중 3명 해고 (Adam Wathan, GitHub PR 2026-01) | 퍼널 탈동조화 | 1차 당사자 증언(방법 미공개) |
| S3 | Block: 제품 종료 → DevRel이 AI 에이전트로 피벗 → CEO가 전사 확산을 DevRel에 (Angie Jones 2025-10) | 내부 DevRel로서의 AX | 1인칭 공개 기록(12,000명 확인 필요) |
| S4 | 카카오 DevRel 담당자: "저는 비개발자입니다" → AI 마일리지 → 인사관리학회 발표 (2025-04~10) | 'D' 경계·DevRel→AX 궤적의 국내 병행 | 1차 공개 블로그(자사 수치 라벨) |
| S5 | Stripe 문서: `.md` 접미사·MCP·Agent skills·llms.txt 지시문 | docs as product, 이중 청중 문서 | 1차 공식 문서 |
| S6 | Anthropic 공고 3종 병치: Developer Relations(외부) / Developer Education Lead(사내) / FDE(고객 임베드) | 직무 분화 한 장면 | 1차 공고(2026-09-25 스냅샷) |
| S7 | Vercel DevRel Engineer: 제품 조직 안, "가르친 결과물 링크 없으면 불합격" | DevRel = 만드는 사람 | 1차 공고 |
| S8 | Salma Alam-Naylor 이탈 선언과 HN 토론 (2026-07) | 위기의 체감 | 1차 블로그 |
| S9 | Google Cloud Agent Skills — DevRel·테크 라이터가 만든 "living product" (2026-08) | 새 산출물 | 1차 회사 블로그 |
| S10 | Orbit: "커뮤니티는 퍼널이 아니다" 프레임을 만든 회사의 인수·종료 (2024) | 측정 도구 시장의 한 장면 | 1차 보도자료 + 2차 정리 |
| S11 | Stack Overflow vs Reddit — 정보 교환형은 줄고 관계형은 버텼다 (Burtch 2024, Ibrahim & Zaki 2026) | R(관계)의 생존 논거 | 논문-PR + 프리프린트 |
| S12 | 토스 SLASH → 메이커스 컨퍼런스 (2025) | '개발자'에서 '메이커'로 이름이 바뀐 국내 사례 | 1차 |
| S13 | Lee Robinson: DevRel → "teach the future of coding" (Cursor 2025-07) | 직함 이동 + 새 청중(AI로 개발자가 된 사람) | 1차 X·Substack |
| S14 | xena: 2024 "DevRel 입문 불안" → 2026 "AX 100점에도 10배 성장 없음" | 발전 방향 장의 균형추 | 커뮤니티 1인칭 |

---

## 4. 논쟁점·상충 관점 (통합하지 말고 병기)

| 쟁점 | 관점 A | 관점 B | 서술 가이드 |
|---|---|---|---|
| DevRel은 죽었나 | 사망·해체: ZIRP 종료, 측정 불능, SE·FDE 흡수, AI가 교육 청중을 없앰(Casey, Briggs, Salma, HN) | 부활·확장: AI 도구사 채용, bottom-up 채택 수요 최고(swyx 2025-10), "biggest stage"(Angie Jones), 공고의 새 정의 | 절충 "역할은 살고 숫자 없는 인력이 잘렸다"(Daria-Dovzhikova) 병기 |
| 비개발 빌더는 '개발자'인가 | "permission to build", 게이트키핑 비판, 도메인 전문가 우위, EUP의 연장(Ko 2011) | "toys", 보안·유지보수 붕괴, 검증 불능(Virk & Liu), CS 기초가 성과 예측(Thorgeirsson) | Sarkar & Drosos "전문성의 재배치"를 교량으로 |
| 에이전트용 문서(llms.txt·AGENTS.md·MCP)는 효과가 있나 | 벤더 게시·에이전트 트래픽 급증(Mintlify 벤더), 문서 zero-shot 효과(Hsieh), 도구 설명 보강 효과(Hasan 2026) | 크롤러 미소비(Mueller, HermanMartinus), AGENTS.md 성공률 개선 없음·비용 +20%(Gloaguen), MCP=마케팅 신호, AX ROI 미증명 | "모델이 모르는 것(비표준 규칙·최신 API)"에 집중할 때 가치 — 두 맥락(SEO vs 코딩 에이전트) 분리 |
| LLM 친화 문서의 사업 효과 | 채택 경로 확보(Supabase) | 트래픽·매출 잠식(Tailwind) | 같은 현상의 양면 — "채택과 수익의 탈동조화" |
| AI는 초보자를 가장 돕나 | Peng 2023(저경력 이득↑), Brynjolfsson(저숙련 34%, WP) | Daniotti Science 2026(초기 경력 유의한 이득 없음), METR(숙련자 19% 느려짐) | 과제·맥락에 따라 방향이 갈린다 |
| AI 확산은 의무화인가 커뮤니티인가 | 의무화: "too much of a suggestion"(Lütke), 평가·채용 반영 | 커뮤니티: 주간 enablement·사례 수집(Block·카카오), 비공식 학습 선호(Sahni & Chilton n=10) | 현장 반발(감시 공포·냉소) 함께 |
| 커뮤니티는 죽었나 | SO 25% 감소(PNAS Nexus), "forums are dead" | Reddit 감소 증거 없음(Burtch), 3.4% 초과 감소 배제(Ibrahim & Zaki 프리프린트) | 감소는 정보 교환형에 집중 |
| 문서는 늘었나 줄었나 | "MORE documentation"(HN Fabricio20) | "less docs ... hallucinated AI slop"(HN izacus) | 커뮤니티 체감 대립 — 수치 없음 |
| FDE와 DevRel의 관계 | FDE가 DevRel을 대체(Daily Context "middle is squeezed") | 1:1 vs 1:many 보완(Weinmeister 요약) | FDE 공고 문구가 DevRel 피드백 루프와 동형이라는 관찰 병기 |

---

## 5. 실무 적용 팁 (저자 논지로 쓸 때의 재료 — 출처는 대부분 [커뮤니티/블로그], 미검증 휴리스틱)

1. **측정을 "만든 증거"로:** 배포·성공한 API 호출·포크·PR·재방문. "What changed because this DevRel work existed?"(DevRelCon NYC 2026). 커뮤니티 건강은 활동량이 아니다(CHAOSS P-46, SPACE P-28).
2. **분기별 LLM 가시성 수동 벤치마크:** ICP의 실제 질문으로 여러 모델에 프롬프트, '쇼핑' 프롬프트와 '근본 문제' 프롬프트를 분리(Joe Karlsson; Sourcegraph 발표 전언). Karlsson 본인도 "largely unsolved"라 인정.
3. **README·examples·API 레퍼런스가 LLM 마케팅이다.** 공개 Q&A 답변은 커뮤니티 작업이자 코퍼스 작업(Karlsson).
4. **에이전트용 문서는 간결·비표준 규칙 중심:** 모델이 이미 아는 개요 반복 금지(Gloaguen P-23), 보강은 단계 수 증가 트레이드오프(Hasan P-19), 보안 가드레일 명시(P-22 14.8%).
5. **문서 조각의 독립성:** 조각이 단독으로 의미를 갖게, 에이전트 지시문·스킬을 SDK처럼 유지보수(DevRelCon NYC 2026; Google "living product").
6. **릴리스마다 문서 갱신 자동 티켓**(Rizèl Scarlett GitHub Action).
7. **Machine funnel과 Human funnel 분리**(Dewan Ahmed).
8. **"Show the mess" + 함께 배우는 사람으로 포지셔닝**(Angie Jones) — 매끈한 데모 불신.
9. **리더도 계속 만든다**(Rizèl Scarlett); **Dev Zero** — 출시 전 낯선 사람으로 먼저 써보기(Karlsson); Vercel 공고 "hit the rough edges first".
10. **진단 먼저:** 콘텐츠 문제인가, 제품 문제인가, 유통 문제인가(Karlsson). "A great DevRel team still cannot save a bad product"(Dewan Ahmed; 학술 대응 P-25).
11. **Discord 명단을 영업에 넘기지 말 것**(Karlsson).
12. **사내 확산(AX) 설계:** 진입 장벽 낮은 도구·예제 프롬프트로 "성공 경험의 복제"(카카오 1K), 비개발자용 최소 필수 지식(MVK), 공유 채널(Shopify #ai-centaurs), 공식 교육보다 동료 팁 교환(Sahni & Chilton n=10), 검증 가드레일(Virk & Liu), 프런티어 경계 안내(Dell'Acqua), 확산 담당자의 자문 "원숭이 꽃신을 주고 있지 않은가"(카카오 Sue).
13. **챔피언 허영 지표 경계:** 토큰·LOC 리더보드 냉소(HN) — 외부 DevRel의 허영 지표와 같은 함정.
14. **로저스 속성 대응표:** 시험 가능성 = 샌드박스·핸즈온·파일럿, 관찰 가능성 = 쇼케이스·라이브 빌드, 복잡성 감소 = MVK·템플릿, 적합성 = 기존 도구 연결(MCP).

---

## 6. 수치 원장 (본문 사용 가능 수치 — 수치·출처·라벨·날짜)

| # | 수치 | 출처 | 라벨 | 기준 시점 |
|---|---|---|---|---|
| N1 | DevRel 실무자 개인 해고 경험 14.6% | State of DevRel 2024, DevRel.Agency | [설문, n=310 유효·자기선택·33개국] | 2024-09 발표 |
| N2 | 프로그램 인원 채용 27% / 해고로 감소 18.1% / 재편 22.1% | 同上 | [설문] | 2024 |
| N3 | 중위 기본급 $150,000(2023 $175,000) | 同上 | [설문] | 2024 |
| N4 | 정의된 커리어 경로 없음 61% | 同上 | [설문] | 2024 |
| N5 | 팀 단위 해고 경험 26.1%(= 100 - 73.9) | Common Room 2023 | [벤더 설문, n=136] | 2023-08-31 |
| N6 | 번아웃 경험 67.1% | Common Room 2023 | [벤더 설문, n=136] | 2023 |
| N7 | DevRel 리더 13명 중 2명(약 15%)만 전술-전략 연결 입증 | Chris Reddington | [질적 인터뷰 n=13, MBA 논문 기반 블로그] | 2026-03-11 |
| N8 | Lovable ARR $200M, 하루 신규 프로젝트 10만 | Lovable | [회사 발표] | 2025-11-18 |
| N9 | Replit 연환산 매출 $150M, 기업가치 $3B | TechCrunch | [언론] | 2025-09-10 |
| N10 | Replit $400M 조달·$9B, run-rate $1B 목표 | Replit | [회사 게시] | 2026-03 |
| N11 | Claude Code GA 6개월 만에 run-rate $1B | Anthropic | [1차] | 2025-12-03 |
| N12 | Claude Code run-rate $2.5B+ | Reuters 보도 | [언론] | 2026-02 |
| N13 | Cursor run-rate $4B, 약 75% 기업 | Dealroom·TechCrunch | [언론, 익명 소식통] | 2026-06 |
| N14 | Bolt ARR ~$80K → ~$40M(5개월) | Eric Simons 인터뷰 | [CEO 발언] | 2025 상반기 |
| N15 | v0 사용자 350만 | Series F 보도 | [언론 요약] | 2025-09 |
| N16 | GitHub 계정 1억 8천만+, 신규 3,600만+(+23%) | Octoverse 2025 | [플랫폼 데이터 — 계정 수] | 데이터 2024-09~2025-08 |
| N17 | 신규 GitHub 사용자 약 80%가 첫 주 Copilot 사용 | Octoverse 2025 | [플랫폼 데이터] | 同上 |
| N18 | 개발자 AI 사용·계획 84%, 불신 46% vs 신뢰 33%, "almost right" 불만 66% | SO Developer Survey 2025 | [설문, 약 49,000명·개발자 한정] | 2025 |
| N19 | 문서 웹 트래픽 중 에이전트 66%(7월), 연초 15.2%; 에이전트 요청 2억 1,300만 vs 사람 페이지 로드 1억 500만 | Mintlify midyear report | [벤더 자사 플랫폼, 단위 상이] | 2026-01~07 |
| N20 | MCP 월 SDK 다운로드 9,700만+, 활성 서버 1만+ | AAIF 결성 발표 | [주체 발표] | 2025-12-09 |
| N21 | Stack Overflow 활동 25% 상대 감소(출시 6개월, DiD, 하한) | del Rio-Chanona et al., PNAS Nexus | [논문-PR] | 2024 / 데이터 2022-11~2023-05 |
| N22 | SO 일일 웹 트래픽 약 100만 명/일(약 12%) 감소, 신규 사용자 집중; Reddit 감소 증거 없음 | Burtch et al., Sci. Rep. | [논문-PR] | 2024 / 데이터 2021-10~2023-03 |
| N23 | Reddit 정보성 요청 3.4% 초과 감소 배제 | Ibrahim & Zaki | [프리프린트, 검토 전] | 2026-09-11 |
| N24 | ChatGPT SO 답변 52% 부정확·77% 장황 | Kabir et al., CHI 2024 | [논문-PR, 질문 517개, 2023 모델] | 2024 |
| N25 | Copilot 처치군 55.8% 빠름(95% CI 21–89%) | Peng et al. | [프리프린트, n=95, 단일 과제, GitHub 저자] | 2023 |
| N26 | 숙련 OSS 개발자 AI 허용 시 19% 느려짐(체감 20% 빨라짐) | METR | [프리프린트 RCT, 16명·246과제] | 2025 초 도구 |
| N27 | 미국 Python 함수 추정 29% AI 작성, 초기 경력 유의한 이득 없음 | Daniotti et al., Science | [논문-PR, 160,097명] | 데이터 ~2024 말 |
| N28 | 고객지원 생산성 평균 15% | Brynjolfsson et al., QJE 2025 | [논문-PR, 5,172명] | 게재 2025 |
| N29 | 프런티어 안 12.2% 더 많이·25.1% 더 빨리 / 밖 약 19%p 하락 | Dell'Acqua et al., Org. Sci. 2026 | [논문-PR, BCG 758명, GPT-4] | 2023 실험 |
| N30 | MCP 도구 설명 97.1% 스멜(도구 856개·서버 103개) | Hasan et al. | [프리프린트] | 2026 |
| N31 | MCP 서버 7.2% 일반 취약점, 5.5% tool poisoning(1,899개) | Hasan et al. v5 | [프리프린트] | 2026-04 판 |
| N32 | 컨텍스트 파일 보안 명시 14.8%, 성능 14.5% | Chatlatanagulchai et al. | [프리프린트, 파일 2,303개] | 2025 |
| N33 | 컨텍스트 파일 제공 시 추론 비용 평균 20%+ 증가, 성공률 개선 없음 | Gloaguen et al. | [프리프린트] | 2026 |
| N34 | Claude Code PR 83.8% 머지, 54.9% 무수정 | Watanabe et al. | [프리프린트, PR 567개] | 2025 |
| N35 | API 학습: 문서 78%, 예제 55%, 동료 질문 29% | Robillard, IEEE Software | [논문-PR, 응답 80명, MS 사내] | 2009 |
| N36 | 2012 미국 추정: 자칭 프로그래머 1,300만+ vs 전문 300만 미만 | Scaffidi et al., VL/HCC | [논문-PR, 추정·전망] | 2005 작성 |
| N37 | 비개발자 67명 통제 연구 — 기술적 의사소통 장벽 | Feldman & Anderson, CHIWORK | [논문-PR] | 2024 |
| N38 | 공식 교육 주 학습 경로 0/10, 동료 팁 교환 6/10 | Sahni & Chilton | [프리프린트, n=10] | 2025 |
| N39 | Tailwind 문서 트래픽 약 -40%(2023 초 대비), 매출 약 -80%, 엔지니어 4명 중 3명 해고 | Adam Wathan, GitHub PR #2388 | [1차 당사자 증언, 방법 미공개] | 2026-01-07 |
| N40 | 카카오 AI 마일리지: 약 100명·30여 조직·40여 과제·3개월; "도구 없이 개발 어렵다" 68.4% | tech.kakao.com | [기업 자체 운영·사내 설문 ≈100명] | 2025-05~07 운영, 2025-09-19 게시 |
| N41 | Anthropic Developer Relations 연봉 범위 $290,000–$435,000(OTE) | Greenhouse 공고 | [1차 공고, 2026-09-25 재확인] | updated 2026-08-21 |
| N42 | 공고 스냅샷 건수(표, 축 5) | Greenhouse/Ashby API | [1차 스냅샷, 추세 아님] | 2026-09-25 |
| N43 | a16z 집계: 당시 OpenAI 공개 채용 311건 중 FDE·솔루션 22건 | a16z | [VC 에세이 집계] | 2025-06-04 |
| N44 | Orbit Postman 인수 | Postman·BusinessWire | [1차] | 2024-04-11 |
| N45 | LF DRF 결성 의향 / 공식 결성 | LF 보도자료 | [1차] | 2024-09-16 / 2025-08-25 |

---

## 7. 금지·주의 수치 목록

| 수치/주장 | 문제 | 대체 |
|---|---|---|
| "DevRel 종사자 26%가 해고됐다" | Common Room 26.1%는 **팀 단위** | 개인은 N1 14.6%, 팀은 N5로 구분 |
| "State of DevRel 2025에 따르면" | 2025판 확인 못함 | 2024판 + "2024년 기준" |
| "문서 독자의 2/3가 에이전트" | 벤더 데이터, 요청 vs 페이지 로드 단위 불일치 | "Mintlify가 자사 호스팅 문서에서 집계한 바로는(2026-07)" + 단위 |
| Mintlify "Almost half your docs traffic is AI"(2026-02), "Claude Code 단독 1억 9,940만 요청" | 방법론 부재 / 중간 보고서에 없음 | 인용 안 함 |
| "State of DevRel: 영향력 증명이 최대 과제 60.7%/61%" | 요약·재인용 수준 | 원문 확인 전 사용 금지 |
| Karpathy 트윗 "450만 뷰" | 2차 | 생략 |
| "AX 용어 12개월 내 VC 메모 등장, AX Specialist 채용" | 2차 용어집 | 생략 |
| FDE 공고 "800% 증가" | 원 데이터 제공자 미확인 | "FT 보도에 따르면(2025-11)" 라벨 필수 |
| FDE "700%(Indeed)" / "1,000% YoY" / "10x in 18 months" | 2차·기준 상이 | 사용 금지 |
| "OpenAI FDE 팀 50명 확장", "Anthropic 파트너 팀 $100M" | 2차 블로그 | 생략 |
| MIT NANDA "생성형 AI 파일럿 95% 실패" | 범위 밖·방법론 논란 | 원 보고서·비판 확인 전 금지 |
| Replit "ARR $525M"(2026-04) | Sacra 추정 | "Sacra 추정" 라벨 또는 N9·N10 |
| Lovable "$500M ARR" / 사용자 "약 800만" | 1차 미확인 | N8까지 |
| v0 "400만/600만" | 2차 통계 블로그 | N15 |
| Apple EvangeList "44,000명" | 위키 스니펫 | 생략 |
| "Evangelist→Advocate는 Sam Ramji의 말" | 1차 미확인 | "업계에서 흔히 설명되는 논리" |
| Chanezon 글 속 "SO 64.8% weekly", Databricks "5개 중 4개 DB는 코드가 생성" | 2차 인용 | SO 원문 수치(N18) |
| 공고 건수 비교로 "DevRel 직무 감소" 단정 | 단일 스냅샷·제목 키워드 | "2026-09-25 공개 목록 기준 예시" |
| "특정 기업 DevRel 팀 전원 해고" | 1차 미확인 | 기업 전체 감원(N 없음, W-2-7)만 |
| SO 16%(프리프린트)와 25%(게재본) 혼용 | 판본 상이 | N21(25%, 라벨) |
| "SO 방문자 12% 감소"를 질문 수로 확대 | 트래픽 지표 | N22 "일일 웹 트래픽" |
| "Reddit도 죽었다" | 반대 증거 | N22·N23 |
| "ChatGPT 답 52%가 틀린다"를 현재 일반론으로 | 2023 모델 | N24 라벨 |
| "Copilot 쓰면 55% 빨라진다" / "AI 쓰면 19% 느려진다" 일반화 | 조건 의존 | N25·N26 조건 병기 |
| "고객지원 14%"와 "15%" 혼용, "초보 34%" 무라벨 | 판본 상이 | 게재본 15%, 34%는 "2023 WP" |
| "BCG 품질 40% 향상" | WP에만 | 12.2%·25.1%, 40%는 "2023 WP" |
| "프런티어 밖 19% 덜 정확" | %p가 정확 | "약 19%p" |
| "미국 코드의 29%" | 미국·Python 함수·분류기 추정 | 세 겹 라벨 |
| "AI는 초보자를 가장 많이 돕는다" 단정 | 상반 결과 | 맥락 의존 서술 |
| "AGENTS.md 쓰면 에이전트 성능이 오른다" | 반대 결과 | 논쟁 중, 비표준 규칙에만 유용 |
| "MCP 서버 97%가 불량" | 단위는 도구 설명 | N30 |
| "최종 사용자 프로그래머 5,500만" | Boehm 예측 | N36 |
| Rogers 채택자 %를 조직 실측처럼 | 이론적 구분 | "이론적 구분" 명시 |
| DevEx 저자 "Greiler·Storey·Noda(Queue)" | Queue는 Noda 제1저자, TSE와 별개 | 두 문헌 구분 |
| "Robillard 440명 조사" | 2009 논문은 83명 | N35 |
| DevEx·SPACE를 "peer-reviewed 논문"으로 | 잡지 기고 | "ACM Queue에 발표한 프레임워크" |
| Wenger CoP 정의 문장을 1998 원서로 | 2015 소개문 | 출처 구분 |
| Stack Overflow "월 질문 약 300건"(Slashdot 요약), "월 2.5만 건"(HN 댓글) | 요약·댓글 수치, 시점·정의 불명 | SEDE 원 쿼리로 재계산 전 사용 금지 (lessons: 원 데이터에서 계산) |
| Supabase "1분기 가입 = 4년치" | 발표 구두 주장 | "발표자에 따르면" 라벨 또는 생략 |
| Sourcegraph 발표 "65% vs 0회" | 전언·자체 테스트 | "발표자 자체 테스트(전언)" 라벨 또는 생략 |
| Block "12,000명 전원 goose 접근" | 작성자 기술 | "Angie Jones에 따르면" 라벨 |
| Zapier "10%→50%→97%" | CEO 구두·원문 미대조 | 생략 |
| Dana Lawson "2029년까지 10억 앱" | 기사 서술·출처 불명 | "[예측] ~라고 말했다" 수준 또는 생략 |
| Jensen Huang "$500k 엔지니어가 $250k 토큰" | GeekNews 재인용, 원출처 확인 필요 | 원출처(All-In 팟캐스트) 확인 전 금지 |
| swyx "developer relations 검색량 5배" | 본인도 과장 인정 | 생략 |
| Hoffmann et al. Copilot 작업 배분 % | 2차 요약 | 방향성만, 수치 금지 |
| Da Silva et al. "-52%" | 구간 정의 미확인 | 사용 금지 |
| Rizèl Scarlett 글 "2026-09-16" | 오기 — 실제 2025-09-16 | 2025-09-16 |

---

## 8. 참고문헌 (URL·DOI)

### 1차·공식
- Leggetter, "Defining Developer Relations" (2016-02-03) https://www.leggetter.co.uk/2016/02/03/defining-developer-relations.html · AAARRRP https://www.leggetter.co.uk/aaarrrp/
- Thengvall, *The Business Value of Developer Relations* (Apress 2018) https://link.springer.com/book/10.1007/978-1-4842-3748-9 · 한국어판 https://www.hanbit.co.kr/store/books/look.php?p_code=B9102351881
- Thengvall, "DevRel Qualified Leads" (2019-12-14) https://www.marythengvall.com/blog/2019/12/14/devrel-qualified-leads-repurposing-a-common-business-metrics-to-prove-value
- Orbit Model https://github.com/orbit-love/orbit-model · Postman 인수 https://blog.postman.com/announcing-postman-has-acquired-orbit/
- Lewko & Parton, *Developer Relations* (Apress 2021) https://www.devrel.agency/book
- State of Developer Relations 2024 https://www.stateofdeveloperrelations.com/2024devrelreport
- Common Room 2023 Report https://www.commonroom.io/blog/2023-developer-relations-compensation-and-culture-report-overview/
- LF DRF 의향 https://www.linuxfoundation.org/press/linux-foundation-announces-intent-to-form-developer-relations-foundation · 결성 https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-developer-relations-foundation
- Karpathy https://x.com/karpathy/status/1886192184808149383
- Collins WOTY 2025 https://blog.collinsdictionary.com/language-lovers/collins-word-of-the-year-2025-ai-meets-authenticity-as-society-shifts/
- Lovable https://lovable.dev/blog/one-year-of-lovable
- Replit https://replit.com/news/funding-announcement · Semafor https://www.semafor.com/article/01/15/2025/replit-ceo-on-ai-breakthroughs-we-dont-care-about-professional-coders-anymore
- Anthropic Claude Code $1B https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone · Series G https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation
- GitHub Octoverse 2025 https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ · 2024 https://github.blog/news-insights/octoverse/octoverse-2024/
- SO Developer Survey 2025 https://survey.stackoverflow.co/2025/ai
- llms.txt https://llmstxt.org/
- MCP https://www.anthropic.com/news/model-context-protocol · AAIF https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation · https://blog.modelcontextprotocol.io/posts/2025-12-09-mcp-joins-agentic-ai-foundation/
- Cloudflare remote MCP https://www.cloudflare.com/press/press-releases/2025/cloudflare-accelerates-ai-agent-development-remote-mcp/ · GitHub MCP https://github.blog/changelog/2025-04-04-github-mcp-server-public-preview/ · Vercel MCP https://vercel.com/blog/introducing-vercel-mcp-connect-vercel-to-your-ai-tools · Supabase https://supabase.com/blog/mcp-server · Stripe https://docs.stripe.com/building-with-ai
- Mintlify midyear report https://www.mintlify.com/blog/state-of-docs-traffic
- Biilmann, "Introducing AX" https://biilmann.blog/articles/introducing-ax/ · https://www.netlify.com/agent-experience/
- swyx, "The Rise of the AI Engineer" https://www.latent.space/p/ai-engineer · "ZIRP" https://dx.tips/zirp · "DevRel is back" https://dx.tips/devrel-is-back
- a16z, "Trading Margin for Moat" https://a16z.com/services-led-growth/
- 공고: Anthropic DevRel https://job-boards.greenhouse.io/anthropic/jobs/5383596008 · Developer Education Lead https://job-boards.greenhouse.io/anthropic/jobs/5311465008 · FDE https://job-boards.greenhouse.io/anthropic/jobs/5302966008 · Copywriter https://job-boards.greenhouse.io/anthropic/jobs/5423931008 · OpenAI DX Engineer Cyber https://jobs.ashbyhq.com/openai/708121e8-51ac-4a24-a2ff-bd9889ba5486 · Vercel https://job-boards.greenhouse.io/vercel/jobs/6122437004 · Supabase https://jobs.ashbyhq.com/supabase/a1320bbf-bfae-49a8-a1b7-12eeccaf39ca · Cloudflare VoidZero https://boards.greenhouse.io/cloudflare/jobs/8190563
- Google Cloud Agent Skills https://cloud.google.com/blog/topics/developers-practitioners/behind-the-scenes-how-we-build-test-and-scale-google-agent-skills
- 토스 https://toss.im/tossfeed/article/tmc25 · 카카오 https://if.kakao.com/2025 · https://www.kakaocorp.com/page/detail/11674
- 카카오 기술블로그 https://tech.kakao.com/posts/697 · /700 · /762 · /783 · /784

### 블로그·의견·언론
- Keith Casey https://caseysoftware.com/blog/developer-relations-a-painful-reckoning
- Lee Briggs https://leebriggs.co.uk/blog/2024/12/10/the-death-of-devrel
- Chris Reddington https://chrisreddington.com/blog/devrel-value-creation/
- Salma Alam-Naylor https://whitep4nth3r.com/blog/goodbye-forever-probably/
- Patrick Chanezon https://blog.chanezon.com/2025/11/07/devrel-evolution-with-ai-agents.html
- Rizèl Scarlett (2025-09-16) https://dev.to/blackgirlbytes/how-to-lead-devrel-in-the-ai-boom-stop-playing-it-safe-19jo
- Dewan Ahmed https://www.dewanahmed.com/devrel-ai-era/
- Liran Tal https://lirantal.com/blog/devrel-2026-thematic-shifts-product-centric-advocacy-coding-agents
- Joe Karlsson https://www.joekarlsson.com/blog/running-devrel-2026/
- Angie Jones https://angiejones.tech/how-devrel-is-leading-ai-adoption/
- Lee Robinson https://leerob.substack.com/p/a-new-chapter
- Thor Schaeff (DevRelCon NY 2025) https://developerrelations.com/talks/redefining-developer-experience-in-the-age-of-vibe-coding/
- DevRelCon NYC 2026 참관기 https://www.linkedin.com/pulse/devrelcon-new-york-2026-building-humans-agents-next-billion-ogundare-avq8e
- Daily Context, "Is FDE killing DevRel?" https://dev.to/dailycontext/is-forward-deployed-engineering-killing-devrel-1833
- The New Stack, Dana Lawson https://thenewstack.io/netlify-agent-experience-engineers/
- Tailwind PR #2388 https://github.com/tailwindlabs/tailwindcss.com/pull/2388
- Tobi Lütke 메모 https://x.com/tobi/status/1909251946235437514
- Mueller/llms.txt https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/
- Gruber https://daringfireball.net/linked/2026/03/13/amodei-ai-code-claim-chowder
- NVIDIA WGS https://blogs.nvidia.com/blog/world-governments-summit/
- GeekNews Weekly #350 https://news.hada.io/weekly/202612 · https://news.hada.io/topic?id=21499 · https://news.hada.io/topic?id=19936 · https://news.hada.io/topic?id=22265
- HN 스레드: 48774195, 40904951, 45571058, 43999125, 48282709, 48410589, 41439983, 46527950, 47208398, 46673809, 47182659, 48095550, 43613079, 44991082, 49744416 (https://news.ycombinator.com/item?id=…)
- r/devrel https://www.reddit.com/r/devrel/comments/1vzh2zb/death_of_the_developer_advocate/ 외 (C-2-5)

### 논문
- del Rio-Chanona et al. 2024 doi:10.1093/pnasnexus/pgae400 · Burtch et al. 2024 doi:10.1038/s41598-024-61221-0 · Kabir et al. 2024 doi:10.1145/3613904.3642596 · Da Silva et al. arXiv:2402.08801 · Ibrahim & Zaki arXiv:2609.12447 · Hasan et al. arXiv:2409.17473
- Peng et al. arXiv:2302.06590 · METR arXiv:2507.09089 · Sarkar & Drosos arXiv:2506.23253 · Pimenova et al. arXiv:2509.12491 · Chou et al. arXiv:2512.22418 · Thorgeirsson et al. doi:10.1145/3772318.3791666 · Tang et al. arXiv:2604.00436 · Ko et al. doi:10.1145/1922649.1922658 · Scaffidi et al. doi:10.1109/VLHCC.2005.34 · Feldman & Anderson doi:10.1145/3663384.3663393 · Virk & Liu arXiv:2508.06484 · Ajimati et al. doi:10.1016/j.jss.2024.112300 · Daniotti et al. doi:10.1126/science.adz9311
- Hsieh et al. arXiv:2308.00675 · Yang et al. arXiv:2405.15793 · Hasan et al. arXiv:2602.14878 · Hasan et al. arXiv:2506.13538 · Guo et al. arXiv:2509.25292 · Chatlatanagulchai et al. arXiv:2511.12884 · Gloaguen et al. arXiv:2602.11988 · Khatri arXiv:2607.27250
- Fontão et al. doi:10.1002/smr.2389 · Massanori et al. doi:10.1145/3422392.3422445 · Fagerholm & Münch doi:10.1109/ICSSP.2012.6225984 · Noda et al. doi:10.1145/3595878 · Forsgren et al. doi:10.1145/3454122.3454124 · Greiler et al. doi:10.1109/TSE.2022.3175660 · Robillard doi:10.1109/MS.2009.193 · Uddin & Robillard doi:10.1109/MS.2014.80 · Meng et al. doi:10.1177/0047281617721853 · Parker et al. doi:10.25300/MISQ/2017/41.1.13 · Manikas & Hansen doi:10.1016/j.jss.2012.12.026 · Jansen doi:10.1016/j.infsof.2014.04.006
- Brynjolfsson et al. doi:10.1093/qje/qjae044 · Dell'Acqua et al. doi:10.1287/orsc.2025.21838 · Dell'Acqua et al. doi:10.3386/w33641 · Howell & Higgins doi:10.2307/2393393 · Rogers 2003 (Free Press, 5th ed.) · Greenhalgh et al. doi:10.1111/j.0887-378X.2004.00325.x · Tushman doi:10.2307/2392402 · Wenger 1998/2002 · Sahni & Chilton arXiv:2502.13281 · Ali et al. arXiv:2606.17887
- Steinmacher et al. doi:10.1145/2675133.2675215 · Steinmacher et al. doi:10.1145/3180155.3180208 · Goggins et al. doi:10.1109/SoHeal52568.2021.00010 · Watanabe et al. arXiv:2509.14745 · Peralta et al. arXiv:2605.22534 · Hoffmann et al. SSRN 5007084

---

## 9. 리서치 한계 (커버하지 못한 영역)

- **State of DevRel 2025판** 미발견. DevRelCon·DevRel Collective 공식 1차 발표 원문은 전사본 1건(Thor Schaeff)과 참관기 1건 위주.
- **채용 보드:** Hugging Face·Google DeepMind·Mintlify 조회 실패. openai.com/careers 개별 공고 403. 공고는 2026-09-25 스냅샷이며 이후 마감 가능.
- **페이월·차단:** FT 원문, Medium(Weinmeister·De Lio), LinkedIn(개인 글), BusinessWire(Vercel Series F), Fast Company.
- **1차 미확보:** Palantir FDE 기원, Sam Ramji 발언, Andrew Ng LinkedIn 원문, Jensen Huang 영상 원문, Josh W. Comeau 원 게시물, Block 12,000명, Supabase 가입 수치.
- **Reddit:** 공식 API 403 — r/devrel 일부만. r/ExperiencedDevs·r/cscareerquestions·r/lovable 미수집.
- **한국:** OKKY·커리어리·브런치·데브챗 원문 미수집, 국내 DevRel 인력·채용 수치 없음, DEVIEW 2024 이후·당근·토스 DevRel 조직 미확인. CJ올리브영 공고는 검색 요약만.
- **학술 공백:** DevRel 직무 변화(감원·FDE 확장)에 대한 학술 연구 없음. llms.txt 학술 연구 없음. "Agent Experience" 학술 문헌 없음(SWE-agent ACI가 최근접). AI 챔피언 프로그램 효과 정량 peer-reviewed 연구 없음.
- **대표성:** 커뮤니티 증거는 HN·r/devrel·Bluesky의 개발자·DevRel 당사자 편향. 비개발 빌더 목소리는 Show HN·Show GN·기업 블로그에 치우침.
- **저자 경험:** 00_direction 규칙대로 수집하지 않음(지어내지 않음). 저자 소속 그룹 계열 공개 블로그 1건은 규칙에 따라 제외.

---

## 10. 책의 논지 후보 3개와 근거 강도

### 논지 A — "DevRel은 죽지 않았다. 'D'와 'R'이 바뀌었다." (청중 확장·재정의론)
DevRel의 대상 'D'는 전문 개발자에서 **빌더(비개발자 포함) + 에이전트**로 넓어졌고, 'R'의 수단은 튜토리얼·컨퍼런스에서 **문서·MCP 서버·스킬·제품 내 경험(AX)**으로 옮겨갔다. DevRel은 "사람과 에이전트가 함께 쓰는 제품 경험의 설계자"가 된다.
- **근거 강도: 중상.**
  - 강: 표준·제품의 1차 타임라인(llms.txt·MCP·AAIF·Stripe/Vercel/Cloudflare/GitHub/Supabase), Biilmann AX 명명, 공고 문구(Anthropic "from individual hobbyists", Supabase "Our users are builders", Vercel "agents and people"), 학술 ACI 개념, 빌더 도구 성장 수치(회사 발표·보도 라벨), Supabase·Tailwind 일화.
  - 약: 에이전트 트래픽 수치는 벤더 단일 출처, llms.txt·AGENTS.md 효과는 학술·현장 모두 논쟁 중, AX ROI 회의(xena), "10억 빌더"는 예측, 메이커 운동 상한론.

### 논지 B — "직함은 흩어지고 기능은 남는다." (해체·재조립론)
DevRel이라는 **직함**은 FDE·Applied AI·Solutions·DX Engineer·AI 교육·MTS로 흩어지지만, 그 **기능**(외부와 제품 사이의 양방향 번역·피드백 루프·신뢰 구축)은 새 직무 공고 문구 안에 그대로 남는다. DevRel은 직업에서 **역량(capability)**으로 바뀐다.
- **근거 강도: 중.**
  - 강: 공고 원문(FDE "contribute insights back to our Product and Engineering teams", Developer Education Lead), 1인칭 직함 이동 다수(Lee Robinson·cameron.stream·Salma·Briggs), HN·Daily Context의 SE/FDE 흡수 관찰, 설문(재편 22.1%, 커리어 경로 부재 61%), LF DRF 결성 배경("lack of role clarity").
  - 약: 공고 건수는 단일 스냅샷(추세 불가), FDE 급증 수치는 원 데이터 미확인, DevRel 직무 변화 학술 연구 부재, 반대 증거(Anthropic·Vercel·Supabase가 DevRel 제목 공고를 여전히 냄, swyx "DevRel is back").

### 논지 C — "DevRel의 다음 무대는 회사 안이다 — 내부 DevRel로서의 AX." (내향·전이론, 저자 궤적 논지)
외부 개발자 생태계에 기술을 퍼뜨리던 기술(먼저 가보기·함께 배우기·데모·커뮤니티 운영·피드백 번역)은 조직 안에 AI를 퍼뜨리는 일(AX)에 그대로 전이된다. 비개발자가 AI로 만드는 시대에 사내의 모든 직원이 'D'가 된다. 그리고 해외 DevRel의 새 과제 AX(Agent Experience)와 저자의 AX(AI Transformation)는 같은 약어로 만난다.
- **근거 강도: 중(사례·이론 강함, 인과 실증 약함).**
  - 강: Block(Angie Jones — CEO가 전사 확산을 DevRel에), 카카오(DevRel 담당자의 AI 마일리지·인사관리학회 발표), Anthropic Developer Education Lead(사내 GTM 대상 공식 직무), Shopify·Zapier의 확산 장치, 이론 계보(Rogers·Howell & Higgins·Tushman·Wenger·Greenhalgh), GenAI 현장 실험(Brynjolfsson·Dell'Acqua — 숙련 확산·들쭉날쭉한 경계), 비공식 학습 선호(Sahni & Chilton n=10), 비개발자 검증 불능(Virk & Liu).
  - 약: AI 챔피언 프로그램 효과의 정량 peer-reviewed 연구 없음, 공개 사례 수가 적고 자사 수치 라벨 필요, 현장 냉소(챔피언 연기·허영 지표), 저자 1인칭 에피소드 미확보(`author_input_needed.md` 대상), AX 약어 교차는 수사 장치 — 과장 금지.

**합성 권고:** 세 논지는 배타적이지 않다. 책의 척추로는 **A(무엇이 바뀌었나) → B(직업은 어떻게 되나) → C(그 기술은 어디로 가나)** 순서가 대상 독자 1·2·3순위와 정렬된다. 반론(교정론·해체론·AX ROI 회의)은 각 PART에 병기한다. 대비 쌍("Dev vs 비Dev", "사람 vs 에이전트")이 주제의 뼈대이므로 수사 대구 과다 위험이 높다(00_direction lessons).

---

## 신선도 원장 (소스별 발행일·버전 시점)

> 검색 시점: 모든 항목 2026-09-25. "{연도} 기준"은 수치가 가리키는 시점.

| 소스 | 발행일 | 기준 시점 |
|---|---|---|
| Kawasaki "software evangelist" | 1984(사건) / 위키 검색 시점 판 | 1984 기준 |
| Leggetter 정의·AAARRRP | 2016-02-03 / DevRelCon London 2016 | 2016 기준 |
| Thengvall 책 / DRL 글 / 한국어판 | 2018 / 2019-12-14 / 2022-06-03 | 2018~2019 기준 |
| Orbit Model / Postman 인수 | 2019-11 / 2024-04-11 | 2024 기준 |
| Lewko & Parton | 2021 | 2021 기준 |
| Chris Reddington | 2026-03-11 | 2026 기준 |
| swyx ZIRP / DevRel is back | 2024-07(HN 2024-07-08) / 2025-10(HN 2025-10-13) | 2024 / 2025 기준 |
| Keith Casey / Lee Briggs | 2024-07-17 / 2024-12-10 | 2024 기준 |
| State of DevRel 2024 | 2024-09-10 | 2024 기준(2025판 부재) |
| Common Room Report | 2023-08-31 | 2023 기준 |
| LF DRF | 2024-09-16 / 2025-08-25 | 2025 기준 |
| Karpathy / Collins | 2025-02-02 / 2025-11-06 | 2025 기준 |
| Lovable | 2025-11-18 | 2025-11 기준 |
| Replit | 2025-01-15 / 2025-09-10 / 2026-03 | 2026-03 기준 |
| Claude Code | 2025-12-03 / 2026-02(Reuters) | 2026-02 기준 |
| Cursor | 2026-04-17 / 2026-06-09 | 2026-06 기준 |
| Bolt / v0 | 2025 상반기 / 2025-08·09 | 2025 기준 |
| Octoverse 2025 / 2024 | 2025-10-28(2026-02-28 갱신) / 2024-10 | 데이터 2024-09~2025-08 / 2024 |
| SO Developer Survey 2025 | 2025(블로그 2025-12-29) | 2025 기준 |
| llms.txt | 2024-09-03(페이지 수정 2026-08-10) | 2024 제안 |
| Mueller llms.txt 발언 | 2025-04~06(보도) | 2025 기준 |
| MCP / AAIF | 2024-11-25 / 2025-12-09 | 2025-12 기준 |
| Cloudflare·GitHub·Supabase·Vercel MCP | 2025-04-07 / 2025-04-04 / 2025-04·10 / 2025-08-06 | 2025 기준 |
| Stripe building-with-ai | 검색 시점 판 | 2026-09 기준 |
| Mintlify midyear report | 2026-07-29 | 2026-01~07 데이터 |
| Biilmann AX / X 후속 | 2025-01-28 / 2025-07(추정) | 2025 기준 |
| swyx AI Engineer | 2023-06-30 | 2023 기준 |
| FT FDE / a16z | 2025-11(추정) / 2025-06-04 | 2025 기준 |
| 채용 공고 스냅샷(Anthropic·OpenAI·Vercel·Supabase·Cloudflare·Cursor 등) | 개별 updated 2026-08~09 | **2026-09-25 확인 기준** |
| Chanezon / Rizèl Scarlett / Dewan Ahmed / Google Agent Skills / Liran Tal | 2025-11-07 / **2025-09-16** / 2026-08-11 갱신 / 2026-08-04 / 2026(월 미확인) | 각 발행 시점 |
| Huang / Amodei / Gruber / Ng | 2024-02-12 / 2025-03-10 / 2026-03-13 / 2025(날짜 미확인) | 각 발언 시점 [예측] |
| 토스 TMC 25 / 카카오 if(kakao)25·PlayMCP / DEVIEW 2023 / 우아한 공고 | 2025-07 / 2025-09·2025-08 / 2023-02 / 2022 추정 | 각 시점 |
| Salma Alam-Naylor / HN 토론 | 2026-07-02 / 2026-07-03 | 2026-07 기준 |
| Thor Schaeff DevRelCon NY | 2025-07 | 2025 기준 |
| DevRelCon NYC 2026 참관기 | 2026-07-25 | 2026-07 기준 |
| Joe Karlsson | 2026-04-20 | 2026 기준 |
| Angie Jones | 2025-10-20 | 2025 기준 |
| Tailwind PR #2388 | 2026-01-06~07 | 2026-01 기준(트래픽은 2023 초 대비) |
| Lee Robinson | 2025-07-18 / 2025-07-21 | 2025 기준 |
| Tobi Lütke 메모 / Coinbase / Zapier 루브릭 | 2025-04-07 / 2025-08-22 / 2026-03-31 | 각 시점 |
| Dana Lawson (The New Stack) | 2026-06-06 | 2026 기준 |
| xena ax-check 댓글 | 2026-09-18 | 2026-09 기준 |
| 카카오 기술블로그 697·700·762·783·784 | 2025-04-22 / 04-24 / 09-19 / 10-30 / 11-03 | 운영 2025-05~07 |
| GeekNews Weekly #350 / Show GN 21499 / 19936 / 22265 | 2026-03 / 2025-06-17 / 2025-03-25 / 2025-08-02 | 각 시점 |
| velog jwclare95 / OKKY 토론회 | 2025-08-01 / 2025-06-01 | 2025 기준 |
| del Rio-Chanona (PNAS Nexus) | 2024-09 (프리프린트 2023-07-14) | 데이터 2022-11~2023-05 |
| Burtch et al. | 2024-05-06 | 데이터 2021-10~2023-03 |
| Kabir et al. | CHI 2024 (arXiv 2023-08) | 2023 모델 |
| Ibrahim & Zaki | 2026-09-11 (검토 전) | 2022~2023 창 |
| Peng / METR / Daniotti | 2023-02 / 2025-07 / 2026-02-19 | 2022 / 2025 초 / ~2024 말 |
| Sarkar & Drosos / Pimenova / Chou / Thorgeirsson / Tang | 2025-06 / 2025-09 / 2025-12 / CHI 2026 / 2026-04 | 2025~2026 도구 |
| Hsieh / SWE-agent | 2023-08 / NeurIPS 2024 | 2023 / 2024 모델 |
| Hasan(MCP 설명) / Hasan(MCP 보안 v5) / Guo / Chatlatanagulchai / Gloaguen | 2026-02(v3 05-31) / 2026-04-13 / 2025-09~11 / 2025-11(v2 2026-08) / 2026-02(v2 06-23) | 2025~2026 MCP 생태계 |
| Fontão / Massanori / Fagerholm & Münch / DevEx / SPACE / Greiler TSE | 2021-10(권호 2023) / 2020 / 2012 / 2023-04 / 2021-02 / 2023-04 | AI 이전 기준 |
| Robillard / Uddin & Robillard / Meng / Parker | 2009 / 2015 / 2017 / 2017 | 각 시점 |
| Brynjolfsson QJE / Dell'Acqua Org Sci / Cybernetic Teammate | 2025 (WP 2023) / 2026-03-11 (WP 2023-09) / 2025 | GPT-3~4 세대 |
| Rogers / Howell & Higgins / Tushman / Greenhalgh / Wenger | 2003(5판) / 1990 / 1977 / 2004 / 1998·2002 | 고전 |
| Sahni & Chilton / Ali et al. | 2025-02(v2 10-06) / 2026-06-16 | 2024~2026 |
| Steinmacher 2015·2018 / Goggins / Watanabe / Peralta / Hoffmann | 2015 / 2018 / 2021 / 2025-09 / 2026-05 / 2024-10 | 각 시점 |

---

## 부록: research-lead 자기 검증 1패스 (경고 항목 우선, 2026-09-25)

| 항목 | 방법 | 결과 |
|---|---|---|
| Anthropic DevRel 공고 연봉 $290,000–$435,000 (커뮤니티 C-5 WebFetch 추출) | Greenhouse 공개 API 직접 조회 | **확인** — "Annual Salary: $290,000 — $435,000 USD", OTE(영업 보너스 포함 범위) 명시. updated 2026-08-21 |
| Rizèl Scarlett 글 날짜 불일치(web 2025-09-16 vs community 2026-09-16) | dev.to 원문 조회 | **2025-09-16 확정**, community.md 표기 오기. 검색 시점 프로필은 "Principal Developer Advocate at Entire" |
| Mintlify 66%·2억 1,300만 vs 1억 500만·15.2% | 원문 재조회 | **확인**. 단 "Claude Code 1억 9,940만 요청"은 이 보고서에 없음 → 금지 목록 |
| Claude Code $2.5B run-rate (web [확인 필요]) | 웹 검색 | Reuters 보도(2026-02) 기반으로 다수 보도 일치 → [언론] 라벨로 승격. Anthropic 1차 원문 문장은 미대조 |
| swyx ZIRP 발행일 | HN 제출일(2024-07-08) 대조 | 2024-07-08 이전 발행으로 한정 |
| 저자 소속사 정보 혼입 | 3개 파일 검토 | 혼입 없음(커뮤니티 리서처가 계열 블로그 1건 사전 제외) |
| 미해결 경고(본문 사용 전 fact-checker 재확인 대상) | — | Block 12,000명, Supabase 가입 수치, Sourcegraph 65%, State of DevRel "61%/60.7% 영향력 증명", SO 월 질문 수(SEDE 재계산 필요), CJ올리브영 공고 원문, Jensen Huang 토큰 발언 원출처, Dana Lawson "10억 앱" |
