# Stage 5 오케스트레이터 프롬프트 (SKELETON)

> 위치: `criteria/stage5/orchestrator_prompt.md`
> stage3 [orchestrator_prompt.md](../stage3/orchestrator_prompt.md) 대응.
> **상태: 뼈대.** 대상 논문·언어 확정 후 고정.

---

## 작업

[implementation_prompt.md](implementation_prompt.md) 절차로 대상 논문을 구현한다.
- 대상: stage4 shortlist (지금은 [targets.md](targets.md) 의 stage3 샘플).
- 저장: `criteria/stage5/results/{id_underscore}/` (폴더당 pseudocode.md / impl.* / notes.md).

## 입력 파라미터

| 파라미터 | 의미 | 예시 |
|---|---|---|
| `TARGETS` | 구현할 논문 id 목록 (targets.md 기반) | `ieee_9810937,arxiv_0801.1208v4` |
| `LANG` | 구현 언어 | `py` \| `cpp` (**미정**) |

## 병렬 처리 규칙 (stage3 패턴 축약)

- stage3와 달리 편수가 적고 편당 작업량이 크므로:
  - **한 agent당 논문 1편** (stage3는 3편). 구현은 편차가 커서 묶지 않는다.
  - 한 라운드 동시 호출 수는 대상 규모에 맞춤 (예: 5편이면 5 agent 1라운드).
  - agent 재사용 금지(`SendMessage` 금지) — stage3와 동일 이유.
- subagent_type: `general-purpose` 또는 `claude` (파일 Write 필요, `Explore` 금지).

## 각 agent 프롬프트 템플릿 (자기완결)

```
너는 LDPC ECC 논문 구현 작업자다. 논문 1편을 구현한다.

[필수 사전 읽기]
1. criteria/stage5/implementation_prompt.md — 구현 절차·출력 형식
2. criteria/stage3/results/{연도}/{id_underscore}.md — 이 논문의 stage3 분석 (B/C 섹션이 출발점)
3. criteria/stage3/Prime_ECC_3.1_Claude/paper_screening_profile.md — 통합 지점(§6)
4. (필요 시) data/pdfs/.../{id}.txt — 수식/파라미터 보강

[대상 논문]
- id: {paper_id}   언어: {LANG}

[수행]
1. stage3 결과의 알고리즘 요약(B) 파악 → 필요 시 .txt로 수식 보강
2. criteria/stage5/results/{id_underscore}/pseudocode.md 작성
3. impl.{LANG} 최소 동작 구현 + 실행/검증
4. notes.md (Prime ECC 통합 노트 · 검증 · 한계)
끝나면 [반환값]으로 보고 후 종료.

[반환값]
DONE: {id} -> results/{id_underscore}/ (pseudocode/impl/notes)
FAILED: {id} (사유 한 줄)
```

## 미결정

- [ ] 언어(`LANG`) 확정
- [ ] 대상 논문 목록(targets.md) 확정
- [ ] 검증 깊이 (동작 확인 / 시뮬)
