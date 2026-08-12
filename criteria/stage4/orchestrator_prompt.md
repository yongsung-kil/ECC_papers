# Stage 4 오케스트레이터 프롬프트 (SKELETON)

> 위치: `criteria/stage4/orchestrator_prompt.md`
> stage3 [orchestrator_prompt.md](../stage3/orchestrator_prompt.md) 대응.
> **상태: 뼈대.** 외부 검증 리스트([reviewed_papers.md](reviewed_papers.md))가 채워지면 확정한다.

---

## 작업

[filter_criteria.md](filter_criteria.md) 기준으로 stage3 결과를 필터링해 구현 후보 shortlist를 만든다.

- 입력 1: `criteria/stage3/results/{연도}/*.md` (하단 JSON 블록 = 기계 필터 소스)
- 입력 2: [reviewed_papers.md](reviewed_papers.md) (외부 검증 리스트)
- 출력: `criteria/stage4/results/` (형식 미정 — README "미결정" 참조)

## 절차 (초안)

1. **매핑**: `reviewed_papers.md` 각 행의 URL/제목 → stage3 `id` 로 잇는다.
   - IEEE URL 끝 숫자 → `ieee_{숫자}` 자동 매칭.
   - 제목만 있는 항목 → stage3 결과 제목과 유사도 매칭(불확실하면 사용자에게 확인 목록 제시).
2. **자동 필터**: stage3 JSON 필드로 축2 컷 적용 (`portability`/`recommend`/`nand_relevance` 등, 임계값은 filter_criteria).
3. **판정 병합**: 축1(외부 검증) + 축2(자동) → `decision` / `priority` 산출 (filter_criteria 로직).
4. **저장**: shortlist 출력.
5. **리포트**: keep N편 / drop M편 / 매핑 실패 K편 한 줄 보고.

## 실행 방식 (미정)

- 규모가 작으면(수십 편) **단일 패스 스크립트**로 충분 — stage3 같은 멀티 agent 병렬 불필요.
- 논문별 정성 판정이 필요하면 stage3 orchestrator 패턴(10 agent × 3편/라운드) 재사용.
- **→ 입력 규모 확정 후 결정.**

## 미결정

- [ ] 매핑 자동화 범위 (URL 자동 / 제목 수동)
- [ ] 필터 방향·임계값 (filter_criteria 확정 대기)
- [ ] 출력 형식 (단일 파일 vs 논문별)
- [ ] 실행 방식 (스크립트 vs 멀티 agent)
