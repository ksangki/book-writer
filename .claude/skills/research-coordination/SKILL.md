---
name: research-coordination
description: Coordinate parallel research agents (web, paper, community) and synthesize findings into a unified reference document. Use when collecting background material for a book, whitepaper, or deep-dive article — triggers on "리서치 조율", "여러 소스에서 자료 모아줘", "reference 문서 만들어줘" style requests. De-duplicates, groups by theme, flags conflicts, preserves citations.
---

# Research Coordination

여러 소스의 리서치를 병렬로 모아 하나의 레퍼런스 문서로 합성한다. 책 저술 중이면 오케스트레이터 Phase 1이 이 흐름을 그대로 따른다.

1. 주제·주요 내용·대상 독자·`genre`·슬러그로 한 문단짜리 브리프를 만든다.
2. 장르에 맞는 리서처를 한 메시지에서 병렬로 띄운다 — `tech-book`은 `web-researcher`·`paper-researcher`·`community-researcher`, 그 밖의 장르는 `web-researcher`·`community-researcher` (학술 근거가 중요한 주제면 `paper-researcher` 추가). 각자 `{slug}/research/{web,papers,community}.md`에 쓴다.
3. 모두 끝나면 `research-lead`를 불러 `{slug}/01_reference.md`로 합성한다. 합성 원칙과 출력 구조는 `research-lead` 에이전트 정의에 있다.

리서처 하나가 실패하면 한 번 다시 띄우고, 또 실패하면 그 소스 없이 합성하며 "리서치 한계"에 적는다.
