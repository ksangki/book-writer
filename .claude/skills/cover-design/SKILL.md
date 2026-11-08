---
name: cover-design
description: Generate a book cover image (1600x2400 PNG from GPT via the local Codex CLI, or 1600x2560) based on title, topic mood, and target audience. Craft image generation prompts in English, generate with the local Codex CLI's image_generation (GPT image model, renders Korean text correctly) first, then image-gen MCPs or APIs, fallback to ImageMagick typography. Use when creating, revising, or A/B testing book covers. Author attribution defaults to Toby-AI (override via orchestrator input).
---

# Cover Design

책의 표지 이미지를 설계·생성한다. 결과는 `{slug}/cover.png`(Codex 생성이면 1600×2400, 그 밖에는 1600×2560) + 재생성용 프롬프트 기록.

## 절차

1. **입력 확인** — 책 제목, 부제(있으면), 주제 분위기, 대상 독자
2. **콘셉트 3안 구상**
   - A: 미니멀리즘 — 심볼 하나 + 큰 타이포
   - B: 일러스트형 — 주제 메타포 이미지
   - C: 타이포그래피 중심 — 제목 자체가 그래픽
3. **추천안 선택** — 주제 톤·대상 독자에 가장 맞는 1안
4. **프롬프트 작성** — 영어 프롬프트 권장 (이미지 모델 대부분 영어 최적화)
5. **이미지 생성** — 사용 가능한 도구 순서로 시도
6. **결과 검증** — 해상도, 구도, 제목 가독성 확인
7. **저장** — `cover.png` + `cover_prompt.md`

## 콘셉트 선택 가이드

| 주제 톤 | 추천 콘셉트 |
|---------|------------|
| 차분한 기술서 | A (미니멀리즘, 차분한 색조) |
| 철학·에세이형 | C (타이포그래피, 따뜻한 색) |
| 실전 튜토리얼 | B (일러스트, 선명한 색) |
| 심화·이론서 | A (미니멀, 깊이 있는 색) |

## 프롬프트 작성 원칙

- 스타일 지정: "minimalist book cover", "editorial illustration", "modernist typography"
- 색상 톤: "warm muted palette", "deep blue and gold"
- 분위기: "contemplative", "bold", "serene"
- 구도: "title prominent in upper third, small author attribution at bottom"
- 제외: "no cheesy stock photo aesthetic", "no generic tech gradient"
- 해상도·비율: "portrait orientation, 1.6:1 aspect ratio"

**예시 프롬프트:**
```
A minimalist book cover in portrait format (1600x2560). 
Title "효과적인 SQL 쿼리 튜닝" in bold modern sans-serif 
occupying the top third. Center: a single abstract symbol 
resembling an interconnected graph in deep indigo. 
Background: warm off-white. Bottom-right: "Toby-AI" 
in small elegant serif. Editorial, calm, confident. 
No stock photography. No generic tech gradient.
```

## 이미지 생성 도구 우선순위

1. **로컬 Codex CLI 이미지 생성** — 가장 선호. `codex features list`에 `image_generation … true`이면 GPT 이미지 모델로 바로 그린다. ChatGPT 웹을 거치지 않고, API 키를 따로 넣지 않으며, 한글 제목·부제·저자를 정확히 그린다(2026-11 「코드 너머의 리더」 표지 시안 2개에서 확인).
2. **이미지 생성 MCP** (설치되어 있으면)
3. **외부 API** — OpenAI `gpt-image-1`, Stability SDXL 등 (사용자 API 키 필요)
4. **ImageMagick 폴백** — 단순 타이포그래피 플레이스홀더

## Codex로 그리기

시안은 2개를 그린다. 하나는 영상·발표자료와 색을 맞춘 상징형, 하나는 본문 삽화와 맞춘 회화형처럼 방향을 다르게 잡는다. 지시문 하나에 시안 하나다.

```bash
S=.claude/skills/cover-design/scripts
mkdir -p {slug}/_cover_gpt
bash $S/codex_image.sh {slug}/_cover_gpt/prompt_a.md {slug}/_cover_gpt/candidate_a.png   # run_in_background, 3~4분
bash $S/codex_image.sh {slug}/_cover_gpt/prompt_b.md {slug}/_cover_gpt/candidate_b.png   # 동시에 띄워도 된다
```

- 스크립트는 빈 임시 폴더에서 Codex를 돌리고 결과(1024×1536)를 1600×2400으로 Lanczos 확대한다. 원본은 `_raw.png`로 남는다. 종료 코드 3(codex 없음·기능 꺼짐)이면 다음 도구로 넘어간다.
- 지시문에는 공개될 글자(제목·부제·저자)와 그림 묘사만 넣는다. 원고·사내 정보·실명·미공개 수치는 넣지 않는다.
- 지시문에 꼭 넣을 것: 글자를 정확히 쓰라는 요구와 그 글자 목록, "No other text, no numbers, no logos, no watermark, no book mockup", 피할 클리셰(빛나는 뇌·네온·홀로그램·로봇 군단), AI를 사람 모습으로 그리지 말 것(필요하면 작은 기계 도구로).

```
Create ONE finished Korean nonfiction book cover, portrait 2:3 (1024x1536).
Render this Korean text exactly, correctly spelled, clean and legible: large title "{제목}",
smaller subtitle "{부제}", author "{저자}" near the bottom. No other text, no numbers,
no logos, no watermark, no book mockup, no glowing brains, neon, holograms or robot armies.
Theme: {책이 말하는 것 한 문장}.
Style: {색·질감·화풍}. Image: {장면 하나}. Generous negative space.
```

- 결과를 열어 글자 오탈자를 한 글자씩 대조한다. 틀린 글자가 하나라도 있으면 다시 그린다.
- 고른 시안을 `{slug}/cover.png`로 복사하고, 다른 시안은 `_cover_gpt/`에 남겨 저자에게 알린다. 매니페스트 `cover_alt`를 새 그림에 맞게 쓴다.
- 판권 제작 고지에 "표지는 이미지 생성 모델로 그린 그림이다"를 적는다. 사람이 나오면 "표지 속 인물은 실재하는 사람이 아니다"를 더한다.
- 같은 스크립트로 본문 삽화도 그릴 수 있다(`WxH` 인자로 크기 지정). 삽화를 넣는 절차는 `cross-review` 4절을 따른다.

## ImageMagick 폴백 명령

```bash
convert -size 1600x2560 \
  -gradient '#1a1a2e-#2d1b4e' \
  -gravity center -font 'Apple-SD-Gothic-Neo' -pointsize 120 -fill white \
  -annotate +0-400 "{책 제목}" \
  -pointsize 70 -fill '#c9b8d8' -annotate +0+600 "{부제}" \
  -pointsize 50 -fill white -annotate +0+1000 "Toby-AI" \
  {slug}/cover.png
```

폰트가 없으면 `-font Helvetica` 또는 시스템 기본 폰트 사용.

## 검증 체크

- [ ] 해상도 ≥ 1600×2560 (Codex 생성은 1600×2400)
- [ ] 썸네일(200×320)로 축소해도 제목 읽힘
- [ ] 저자 표기 존재 (기본값 `Toby-AI`, 사용자 지정 시 그 값 — 이미지 안 또는 메타데이터 예정)
- [ ] 클리셰 회피 (기본 그라데이션, 스톡사진 느낌 없음)

## 프롬프트 기록

`cover_prompt.md`:

```markdown
# Cover Design Log

## Version 1 (YYYY-MM-DD)
- Concept: {A/B/C}
- Tool: {codex / mcp / api / imagemagick}
- Prompt:
  ```
  ...
  ```
- Result: cover.png
- Notes: {성공/조정 필요 부분}

## Version 2 ...
```

## 실패 대응

- Codex 실패(종료 코드 3·4) → MCP·API → ImageMagick 폴백 순서로 내려간다
- 이미지 API 실패 → ImageMagick 폴백
- ImageMagick 미설치 → 오케스트레이터에 `brew install imagemagick` 지시 요청, 임시로 단색 PNG 생성
- 생성 결과가 클리셰이거나 제목이 잘 안 보임 → 프롬프트 구체화 (색상·구도 강화) 후 재시도

## 재생성 시

- 이전 `cover.png`를 `cover_v{N}.png`로 백업
- `cover_prompt.md`에 새 버전 append
- 콘셉트 변경 요청 → 3안부터 다시
