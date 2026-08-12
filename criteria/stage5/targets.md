# Stage 5 대상 논문 (예시용, 나중에 채움)

> 위치: `criteria/stage5/targets.md`
> **상태: 빈 템플릿.** stage4 완성 전까지 stage3 결과 중 **샘플**을 골라 예시 stage5를 돌린다.

---

## 선정 기준 (제안)

stage3 JSON 필드로 "구현 가치 높은" 논문을 고른다. 예:

- `portability` = `상`  (이식 쉬움)
- `recommend` = `상`  (정독가치 높음)
- `target` = `decoder` 또는 `both`  (Prime ECC 디코더에 바로 얹힘)
- `hw_designed` 무관 (알고리즘 delta만 있어도 구현 대상)

> stage3 결과에서 위 조건으로 후보를 뽑는 스크립트/쿼리는 추후 추가 (`src/report/` 패턴 재사용 가능).

## 대상 목록

| # | stage3_id | 제목 | 선정 이유 | 언어 | 상태 |
|---|---|---|---|---|---|
| 1 | ieee_9496601 | A Low Bit-Width LDPC Min-Sum Decoding Scheme for NAND Flash (TCAD'22) | 이식성 상·적용가치 높음·delta가 CNU min1/min2 클리핑 1지점 | py | ✅ 예시 완료 (`results/ieee_9496601/`) |
| 2 | | | | | |
| 3 | | | | | |

> 확정되면 [orchestrator_prompt.md](orchestrator_prompt.md) `TARGETS` 로 넘긴다.
