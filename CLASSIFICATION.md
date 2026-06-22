# 논문 분류 작업 정리 (Phase 2 · Phase 2.5)

> 기준 시점: 2026-06-22 · 데이터: `data/papers.db` (SQLite)

전체 수집 논문 **22,225편**(arXiv 1,124 + IEEE 21,101)을 두 단계로 분류했다.
초록만 보고 판정했으며, 판정은 병렬 에이전트(LLM)가 수행하고 결과를 DB에 기록했다.

```
[전체 22,225]
   └─ Phase 2 (1차 선별: NAND LDPC ECC 적용성)
        ├─ filtered_out 15,999  (제외)
        └─ filtered_in   6,226  (통과)
              └─ Phase 2.5 (알고리즘 수정 여부)
                   ├─ algo_mod=1  5,311  (유지: 알고리즘/코드 기여 있음)
                   └─ algo_mod=0    915  (제외: 하드웨어 수정만)
```

---

## Phase 2 — 1차 선별 (in / out)

**판정 질문**: "이 논문을 NAND 플래시 LDPC ECC에 활용할 수 있는가?"
NAND에 직접 쓰인 논문이 아니어도, 기법(부호 설계 → 디코더 알고리즘 → HW 구현)을 떼어내
NAND LDPC ECC에 이식할 수 있으면 통과(in). 판단 축은 도메인이 아니라
"NAND 고전 바이너리 LDPC에 *새로* 이식할 기법이 있나"다.

**판정 기준 전문**: [criteria/selection_criteria.md](criteria/selection_criteria.md)

포함(in) 카테고리:

| 코드 | 내용 |
|------|------|
| A | NAND/SSD/플래시 직접 (read-retry, LLR 양자화, retention, 3D TLC/QLC, 컨트롤러) |
| B | 스토리지 ECC 일반 (디스크/erasure, storage용 바이너리 LDPC) |
| C | 이식 가능 디코더 알고리즘 (min-sum 변형, BP 개선, OSD, 신경망 디코더) |
| D | 이식 가능 HW 아키텍처 (FPGA/VLSI 디코더, 병렬화, permutation network) |
| E | 이식 가능 코드 설계 (QC/SC-LDPC 구성, girth·사이클 제거, error floor, 유한길이) |

주요 제외(out) 항목: 비이진 LDPC(GF(q)), 비-LDPC 부호(polar·turbo·RS·BCH), 표준 부호의
단순 재사용, 양자 LDPC·보안, QKD 정보조정, 소스 코딩, 무선/통신 응용 특이, 순수 이론 bound,
JSCC·fountain/erasure 등. (각 항목의 예외 조건은 기준서 참조)

**방법**:
- 미선별 논문을 100편 단위 청크로 분할, 청크당 에이전트 10개(에이전트당 10편)가 병렬 판정.
- 각 에이전트는 기준서와 담당 논문 초록을 읽고 `in`/`out` + 한 줄 근거(`reason`)를 반환.
- DB 기록 전 무결성 검증(존재하지 않는 id·중복·decision 오류), 통과 시에만 적용.
- 도구: `src/review.py`(분할/기록/검증), `select_workflow.js`(병렬 판정 워크플로),
  절차서 `REVIEW.md`.

**결과**: filtered_in **6,226** / filtered_out **15,999** (전체 22,225편 = 100% 완료).

> 보정 이력(2026-06-22): 블라인드 부호 인식·블라인드 LLR 추정 2편(`ieee:11406886`,
> `ieee:8580788`)을 제외로 재분류(기준서 제외 항목 신설). filtered_in 6,228→6,226.

**DB 기록 위치**:
- `papers.status` = `filtered_in` | `filtered_out`
- `filter_results.reason` = 판정 근거 한 줄 (근거 안에 적용 카테고리 표기, 예: `(C/E)`, `(D)`, `A 직접`)

---

## Phase 2.5 — 알고리즘 수정 여부 (algorithm vs hardware-only)

**판정 질문**: Phase 2 통과 논문 중 "**알고리즘 측면의 수정(기여)**가 있는가?"
디코더 알고리즘 또는 부호(코드) 설계/구성에 새 기여가 있으면 유지,
기여가 **하드웨어 구현/아키텍처뿐**(표준 알고리즘을 FPGA/VLSI/ASIC로 구현·가속)이면 제외.

**판정 규칙**: 적용 카테고리가 **D(하드웨어)만**이면 제외, A·B·C·E 중 하나라도 있으면 유지.

**방법** (2단계):
1. **태그 파싱** — Phase 2 `reason`에 표기된 카테고리(`(C/E)`, `(D)`, `A/E`, `카테고리 A` 등)를
   정규식으로 추출해 자동 분류. 카테고리가 D뿐 → 제외(0), 그 외 → 유지(1).
2. **애매분 재판정** — 태그를 찾지 못한 논문(579편)만 에이전트가 초록을 다시 읽고
   `keep`(알고리즘/코드 기여) / `drop`(HW만)으로 판정 → 491 유지 / 88 제외.

- 도구: `src/algo_classify.py`(파싱·분류·배치·기록), `algo_workflow.js`(애매분 재판정 워크플로).

**결과** (filtered_in 6,226편 대상): 유지 **5,311** / 제외(HW만) **915**.
제외된 915편은 "min-sum 디코더 FPGA 구현", "QC-LDPC VLSI 아키텍처" 등 표준 알고리즘의
하드웨어 구현·가속에 그치는 논문들이다.

**DB 기록 위치**: `filter_results.algo_mod`
- `1` = 알고리즘/코드 기여 있음 (유지)
- `0` = 하드웨어 수정만 (제외)

status는 `filtered_in` 그대로 두고 컬럼만 플래그로 둔다.
이후 단계는 `algo_mod = 1`(5,311편)만 대상으로 삼으면 HW-only 915편이 제외된다.

---

## 현황 확인 / 재현

```bash
# Phase 2 현황 (status별 집계)
python -m src.review stats

# Phase 2.5 현황 (algo_mod별 집계)
python -m src.algo_classify stats

# 진행맵(연도별 선별 완료 현황) 갱신
python -m src.progress        # → review_progress.md
```

직접 조회 예:

```sql
-- Phase 2 통과 + 알고리즘 기여 있는 논문 (다음 단계 대상)
SELECT p.id, p.title, f.reason
FROM filter_results f JOIN papers p ON p.id = f.paper_id
WHERE p.status = 'filtered_in' AND f.algo_mod = 1;

-- Phase 2.5에서 제외된(HW만) 논문
SELECT p.id, p.title, f.reason
FROM filter_results f JOIN papers p ON p.id = f.paper_id
WHERE p.status = 'filtered_in' AND f.algo_mod = 0;
```

## 관련 파일

| 파일 | 역할 |
|------|------|
| `criteria/selection_criteria.md` | Phase 2 판정 기준서 |
| `REVIEW.md` | Phase 2 실행 절차서 |
| `src/review.py` · `select_workflow.js` | Phase 2 분할/기록/검증 · 병렬 판정 |
| `src/algo_classify.py` · `algo_workflow.js` | Phase 2.5 분류 · 애매분 재판정 |
| `data/papers.db` | 모든 메타데이터·판정 결과 (papers / filter_results) |
| `review_progress.md` | 연도별 선별 완료 현황 |
