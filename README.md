# Auto Paper Analysis (ECC_papers)

LDPC 논문을 **모아 → 골라내고 → 깊게 읽어 → 써먹을 아이디어로** 정리하는 도구입니다.
최종 목표는 **NAND 플래시 ECC에 적용할 만한 LDPC 기법**을 찾아내는 것입니다.

## 전체 흐름

```
[1] 수집        [2] 1차 선별        [3] 심층 분석       [4] 아이디어
 LDPC 논문   →   NAND에 쓸 만한   →   통과 논문 PDF   →   실현 가능한
 (완료)          것만 골라내기        깊게 읽기            방법·설계 정리
                 (초록만 보고)        (전문 읽기)
```

- **수집(Phase 1)은 완료**됐습니다. 데이터는 `data/papers.db`에 확정 보존(arXiv 1,124 + IEEE 21,101 = **22,225편**). 더 이상 수집하지 않으므로 수집 코드는 제거됐습니다.
- **선별·분석에서 "LLM"은 외부 API가 아니라 이 대화의 Claude**가 직접 합니다 (비용·키 없음).
- 사람이 읽는 카탈로그로 출력되고, GitHub에 백업됩니다.
  - `papers/원본/` — 전체, `papers/1차선별/` — 선별 통과분(+SUMMARY.md)

## 단계별 설명

| 단계 | 하는 일 | 도구 |
|------|---------|------|
| **1. 수집** | arXiv·IEEE에서 LDPC 논문 수집 (완료, IEEE는 전체 초록 CSV 기반) | — (종료) |
| **2. 1차 선별** | 초록만 보고 **NAND 적용 가능성**을 포함/제외(in/out) 이분 판정 | `src/review.py` + `select_workflow.js` + `criteria/selection_criteria.md` |
| **3. 심층 분석** | 통과 논문 PDF 전문을 읽고 핵심 기여·방법·NAND 적용성 분석 | (예정) |
| **4. 아이디어** | 분석을 실제 구현 가능한 방법/설계로 정리 | (예정) |

> **선별 기준**(`criteria/selection_criteria.md`)이 이 시스템의 핵심입니다.
> "NAND에 직접 쓰였나"가 아니라 **"디코더·하드웨어·알고리즘으로 이식 가능한가"**로 판단하며, 선별을 거듭하며 계속 다듬어 갑니다.

## 사용법

선별은 **병렬 워크플로**로 돌립니다. 새 세션에서 **`REVIEW.md 읽고 진행해`** 라고 하면 한 청크가 자동 진행됩니다. 수동으로 단계를 밟으면:

```bash
# [2] 선별 한 청크
python -m src.review batch -n 100 --per 10          # ① 미선별 100편을 _work/{라벨}_{타임스탬프}/로 분할
#                                                     (특정 연도만: --year 2017, 세션 구분: --tag A)
#   ② select_workflow.js 워크플로 실행 → 에이전트 병렬 in/out 판정 → <RUN_DIR>/judgments.json
python -m src.review verify <RUN_DIR>               # ③ 무결성 검증(잘못된 id·중복·decision 오류)
python -m src.review apply <RUN_DIR>/judgments.json # ④ DB(filter_results·status)에 기록
python -m src.review stats                          # 선별 현황
python -m src.progress                              # 진행맵(review_progress.md) 갱신

# 카탈로그 재생성 (선별 결과를 papers/ 에 반영)
python -m src.catalog
```

자세한 절차는 **`REVIEW.md`** 참조.

## 폴더 구조

```
src/             db.py · review.py(선별) · catalog.py · progress.py(진행맵)
REVIEW.md        선별 실행 Runbook  ·  select_workflow.js  병렬 선별 워크플로
criteria/        선별 기준서 (살아있는 문서)
data/            papers.db (SQLite, 모든 메타데이터 단일 저장소)
papers/          사람이 읽는 카탈로그
  원본/          전체 22,225편 (source / 연 / 월 / catalog.md·csv)
  1차선별/       선별 통과분 + 알고리즘 기여 표기 + SUMMARY.md
_pm/             작업 관리 (TODO·DONE·roadmap)
```

## 현재 상태

- **Phase 1 (수집)**: ✅ 완료 — 22,225편 (arXiv 1,124 + IEEE 21,101, 전부 저널·컨퍼런스/프리프린트)
- **Phase 2 (선별)**: 🔄 진행 중 — 진척은 `review_progress.md` 참조 (in/out 누적)
- **Phase 3~4**: 예정
