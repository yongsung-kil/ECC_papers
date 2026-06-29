# 저장소 구조 재배치 — criteria / src 차수화

> 작성: 2026-06-25 · 상태: **src 재배치 완료**(커밋 대기) · 결정 A 채택
> 갱신(2026-06-25): 사용자 결정으로 **단계 라벨을 stageN으로 전면 통일**(criteria/1차→criteria/stage1,
> criteria/2차→criteria/stage2 …). "1차/2차"는 개념 명칭으로만 본문에 남김. 데이터는 papers/→`data/catalogs/`,
> PDF→`data/pdfs/{ieee,arxiv}/`로 통합. 저장처(미결정 #4)는 **md/json 소스 + papers.db enum+round 테이블, 마일스톤 커밋**으로 확정.

## 완료 (이 대화)
- [x] `src/stage1/` 생성 → `review.py`·`algo_classify.py`·`select_workflow.js`·`algo_workflow.js` 이동
- [x] `src/report/` 생성 → `catalog.py`·`progress.py` 이동
- [x] `src/stage2/` 골격 생성(README+__init__, 2차 정착지)
- [x] `db.py`는 `src/` 루트 공유 유지 (`from src.db` 임포트 무변경)
- [x] 옮긴 .py의 `PROJECT_ROOT` 깊이 +1 보정 (parent×3)
- [x] 명령어·기준서 경로 참조 52건 일괄 갱신 (README/CLASSIFICATION/REVIEW + docstring + .js)
  - `python -m src.review` → `python -m src.stage1.review` 등
  - `criteria/selection_criteria.md` → `criteria/stage1/selection_criteria.md`
- [x] 스모크: import·PROJECT_ROOT·`stats` CLI 정상
- [ ] 커밋 — **다른 대화의 tools/downloader 이동과 트리가 섞여 보류**

## 보류/다른 대화 소관
- `common/` 추출(batch/verify/pdf)은 2차 착수 시 (소비자 생기면). 지금은 미생성.
- `criteria/stage2/`·`src/stage2/analyze.py`는 `_test` 프로토타입 확정 후 정착.
- PDF→`data/pdfs/`, 다운로더→`tools/ieee_downloader/`는 다른 대화 진행 중(트리에 일부 반영됨).



## 목적
판정이 **1차(선별 in/out) → 2차(정독 분류) → 3차…** 로 이어진다.
현재 `src`·workflow는 **1차 전용**으로 평면화돼 있어 2차 모듈을 더하면 뒤섞인다.
criteria(`criteria/stage1/`)와 **1:1로 대응되는 차수 구조**로 재배치한다.

## 용어 정리 (3중 번호체계 충돌 해소)
| 사용자 | 코드(현재) | 내용 | criteria | src |
|--------|-----------|------|----------|-----|
| **1차** | Phase 2 + 2.5 | NAND 적용성 in/out + algo_mod | `criteria/stage1/` | `src/stage1/` |
| **2차** | Phase 3 | PDF 정독 → enum 분류 + 이식성 | `criteria/stage2/` | `src/stage2/` |
| 3차+ | Phase 4~ | 아이디어 카드·실현성 | `criteria/stage3/` | `src/stage3/` |

- "차" = **살아남은 논문에 대한 연속 판정 라운드** (= 사용자 모델). 이걸 정본으로.
- `Phase 2/2.5/3` 라벨은 CLASSIFICATION.md·docstring에서 `1차/2차`로 치환.
- TODO의 `Phase 1~5`(로드맵)는 별개 축이므로 유지하되, 판정 라운드는 "차"로 명시.

## 제안 구조 (target)

```
criteria/
├── stage1/  selection_criteria.md          # 선별 in/out 기준 (이동 완료)
└── stage2/  categories.md, prompt.md        # 정독 enum 스키마 (← _test 산출물 정착)

src/
├── __init__.py
├── db.py                  # 공유: 스키마·연결 (전 단계 import)
├── common/                # 단계 무관 유틸
│   ├── batch.py           #   미선별/미분석 → agent_NN.json 분할 (review.make_batches 일반화)
│   ├── verify.py          #   판정 JSON 무결성 검증 (review.verify_run 일반화)
│   └── pdf.py             #   id → PDF 경로 (_test/resolve_pdf.py 정착)
├── stage1/                # 1차: 선별 + algo_mod
│   ├── review.py          #   ← src/review.py
│   ├── algo_classify.py   #   ← src/algo_classify.py
│   ├── select_workflow.js #   ← 루트
│   └── algo_workflow.js   #   ← 루트
├── stage2/                # 2차: 정독 enum 분류 + 이식성
│   ├── analyze.py         #   batch(미분석 분할)/apply(결과 DB 기록)/stats — 신규
│   └── analyze_workflow.js#   정독 분석 워크플로 — 신규
└── report/                # 보기/리포트 (공유)
    ├── catalog.py         #   ← src/catalog.py
    └── progress.py        #   ← src/progress.py
```

호출 변화: `python -m src.review batch` → `python -m src.stage1.review batch` 등.
(README·CLASSIFICATION·docstring의 명령 예시 일괄 치환 필요)

## 미결정 (사용자 확인)
1. **src 레이아웃 깊이**: stage 서브패키지(위 안) vs flat 접두사(`s1_review.py`) vs 최소변경(지금 평면 + stage2만 추가)
2. **algo_mod(현 2.5)**: stage1 안에 포함 vs 독립 stage
3. **workflow .js 위치**: stage 폴더 동거 vs 별도 `workflows/`
4. **2차 분석 저장처**(다른 대화 소관이나 src가 의존): papers.db 같은 테이블 vs 별도 db vs md 전용
   → 권고: **enum .md(사람용) + papers.db 테이블(쿼리 정본)**. analyses 테이블을 enum 스키마로 재설계.

## 다른 대화와의 경계 (여기선 손대지 않음)
- PDF `ieee_downloader_new/downloads` → `data/pdfs/ieee/` 이동, arXiv도 `data/pdfs/arxiv/`
- 다운로더 코드 → `tools/ieee_downloader/`, 구버전 예시(`tools/ieee_download*.py`) 삭제
- → src의 `common/pdf.py`는 이 최종 PDF 경로를 가리키도록만 맞추면 됨

## 안전성
- src 이동은 import 경로·`python -m` 명령만 바뀜(로직 무변경). 🔶 Review 등급.
- 이동 후 `python -m src.stage1.review stats` 등으로 스모크 테스트.
- papers.db는 무변경(테이블 재설계는 2차 착수 시 별도).
