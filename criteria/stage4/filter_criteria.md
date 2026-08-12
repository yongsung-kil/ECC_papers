# Stage 4 필터 기준 / 출력 스키마 (SKELETON)

> 위치: `criteria/stage4/filter_criteria.md`
> stage3 [categories.md](../stage3/categories.md)의 stage4 대응 문서.
> **상태: 뼈대.** 아래 enum·임계값은 예시(placeholder)이며 사용자 확정 후 고정한다.

---

## 판정 대상

stage3 통과 논문 전체(`criteria/stage3/results/{연도}/*.md`) 중
**stage5(구현)로 넘길 후보** 를 keep/drop 한다.

## 필터 신호 (2축)

### 축 1 — 외부 검증 매칭 (핵심, human-in-the-loop)

[reviewed_papers.md](reviewed_papers.md) 의 검증 논문과 stage3 논문을 매칭.

| 값(enum) | 의미 |
|---|---|
| `verified-keep` | 외부 검증 결과 "쓸만함" → 구현 후보 |
| `verified-drop` | 외부 검증 결과 "불필요/부적합" → 제외 |
| `not-reviewed` | 외부 검토 안 함 (stage3 필드로만 판단) |

> ⚠ **미결정**: 검증 논문을 "통과(우선순위↑)"로 볼지 "이미 봤으니 제외"로 볼지 방향 확정 필요 (README 참조).

### 축 2 — stage3 필드 기반 자동 필터 (병용, 임계값 예시)

stage3 JSON 필드로 자동 컷. (아래는 **예시 임계값** — 확정 전)

| 필드(stage3) | 통과 조건(예시) |
|---|---|
| `portability` (이식성) | `상` 또는 `중` |
| `recommend` (추천도) | `상` |
| `nand_relevance` | `직접` 또는 `간접` |
| (필요 시 추가) | … |

## 출력 스키마 (예시)

논문 1편당 아래 판정. (형식 확정 전 — 단일 shortlist.json 가정)

```json
{
  "id": "ieee:XXXXXXX",
  "title": "...",
  "stage3_path": "criteria/stage3/results/2024/ieee_XXXXXXX.md",
  "external_review": "verified-keep | verified-drop | not-reviewed",
  "auto_filter": "pass | fail",
  "decision": "keep | drop",
  "priority": "상 | 중 | 하",
  "reason": "(한 줄) keep/drop 근거"
}
```

## 필터 로직 (의사결정, 확정 전)

```
decision =
    drop   if external_review == "verified-drop"
    keep   if external_review == "verified-keep"
    keep   if auto_filter == "pass"        # not-reviewed 이면 stage3 필드로
    drop   otherwise
```

> 위 로직·enum·임계값은 전부 **placeholder**. 사용자가 검증 리스트와 방향을 확정하면 이 문서를 고정 기준으로 승격한다.
