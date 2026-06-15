# Auto Paper Analysis (ECC_papers)

LDPC 논문을 **자동으로 모으고 → 골라내고 → 깊게 읽어 → 써먹을 아이디어로** 정리하는 도구입니다.
최종 목표는 **NAND 플래시 ECC에 적용할 만한 LDPC 기법**을 찾아내는 것입니다.

## 전체 흐름

```
[1] 수집        [2] 1차 선별        [3] 심층 분석       [4] 아이디어
 LDPC 논문   →   NAND에 쓸 만한   →   통과 논문 PDF   →   실현 가능한
 전부 긁기       것만 골라내기        깊게 읽기            방법·설계 정리
 (arXiv+IEEE)    (초록만 보고)        (전문 읽기)
```

- **수집**은 한 번에 전부(`drain`) 받습니다. 주기 실행이 아니라 "날 잡아서" 1회.
- **선별·분석에서 "LLM"은 외부 API가 아니라 이 대화의 Claude**가 직접 합니다 (비용·키 없음).
- 모든 데이터는 `data/papers.db`(SQLite)에 쌓이고, 사람이 읽기 쉬운 `papers/.../catalog.md`로 자동 출력되며, GitHub에 자동 백업됩니다.

## 단계별 설명

| 단계 | 하는 일 | 핵심 도구 |
|------|---------|-----------|
| **1. 수집** | `LDPC` / `low-density parity-check`로 arXiv·IEEE에서 논문을 광범위하게 수집. 중복은 자동 제외, 끊긴 지점부터 이어받기 | `src/runner.py` |
| **2. 1차 선별** | 초록만 보고 **NAND 적용 가능성**을 점수화(통과/제외). 판단 기준은 문서로 관리 | `src/review.py` + `criteria/selection_criteria.md` |
| **3. 심층 분석** | 통과한 논문의 PDF 전문을 읽고 핵심 기여·방법·NAND 적용 가능성 분석 | (예정) |
| **4. 아이디어** | 분석을 실제 구현 가능한 방법/설계로 정리 | (예정) |

> **선별 기준**(`criteria/selection_criteria.md`)이 이 시스템의 핵심입니다.
> "NAND에 직접 쓰였나"가 아니라 **"디코더·하드웨어·알고리즘으로 이식 가능한가"**로 판단하며, 선별을 거듭하며 계속 다듬어 갑니다.

## 사용법

```bash
# [1] 수집 — 전부 받기(전량 drain) / 또는 1배치만
python -m src.runner --drain
python -m src.runner -n 100 --sources arxiv

# [2] 선별 — 미선별 논문(초록)을 기준서와 함께 출력 → Claude가 판단 → 결과 적용
python -m src.review pending > pending.md     # ① 목록 뽑기 (기준서 포함)
#   ② Claude가 읽고 판단 → judgments.json 작성 ([{id, score, decision, reason}, ...])
python -m src.review apply judgments.json     # ③ DB에 기록(통과/제외)
python -m src.review stats                    # 선별 현황
```

## 폴더 구조

```
src/        수집·선별 코드 (db, arxiv_collector, ieee_collector, runner, review)
criteria/   선별 기준서 (살아있는 문서)
data/       papers.db (SQLite, 모든 메타데이터 단일 저장소)
papers/     사람이 읽는 카탈로그 (arxiv|ieee / 연 / 월 / catalog.md·csv)
logs/       수집 실행 로그
_pm/        작업 관리 (TODO·DONE·roadmap)
```

## 현재 상태

- **Phase 1 (수집)**: 완료 — arXiv 광범위 + IEEE 연도 버킷, 커서 이어받기, GitHub 자동 백업
- **Phase 2 (선별)**: 도구·기준서 완성, 실증 완료
- **Phase 3~4**: 예정

수집 대상 규모: arXiv ≈ 1,600편 / IEEE ≈ 18,000편 (LDPC 전체).
