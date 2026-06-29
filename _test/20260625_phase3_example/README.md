# Phase 3 예시 — 논문 본문 정독 분석

> 생성: 2026-06-25 11:34 · 작업폴더(임시). 검증되면 전체로 확장.

## 목적
Phase 2/2.5에서 **초록만** 보고 통과시킨 논문(`algo_mod=1`, 5,307편)을
이번엔 **PDF 본문을 직접 읽고** 두 가지를 정한다.

1. **실제로 이식 가능한 수준인가** (이식성 등급)
2. **카테고리** (decoder/encoder, HW 여부, gatecount, 병렬화, throughput,
   정정능력·iteration·error floor/waterfall 등)

한 번에 **1편씩** 읽고 결과를 출력한다.

## 파일
| 파일 | 역할 |
|------|------|
| `prompt.md` | 1편 분석용 프롬프트 (짧게) |
| `categories.md` | 카테고리/출력 스키마 정의 |
| `results/{id}.md` | 논문별 분석 결과 |
| `resolve_pdf.py` | 논문 id → PDF 경로 매핑 헬퍼 |

## PDF 위치 (참고)
- IEEE: `ieee_downloader_new/downloads/{년}/{월}/ieee_{arnumber}.pdf`
  (매핑: `ieee_downloader_new/download.db` · `download_targets`, id=`ieee:{arnumber}`)
- arXiv: `data/pdfs/arxiv/{년}/{월}/{arxiv_id}.pdf`
- 메타(제목/초록/연도): `data/papers.db` · `papers`

## 진행
- [x] 예시 1편: `ieee:7828079` (Multi-Bit Flipping Decoding) → `results/ieee_7828079.md`
- [ ] 사용자 검토 → 카테고리/프롬프트 확정
- [ ] 전체 5,307편 배치 실행 (Phase 3)
