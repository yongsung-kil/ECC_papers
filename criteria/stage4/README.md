# Stage 4 — 외부 검증 기반 추가 필터 (틀만 잡힌 상태)

> 위치: `criteria/stage4/`
> 상태: **SKELETON (틀만)** — 입력(검토 논문 리스트)·확정 필터 기준은 나중에 채운다.

---

## 파이프라인 위치

```
stage1 (초록 1차 선별, 6,222편 통과)
   ↓
stage3 (Prime ECC 프로파일 참조 심층 분석 → results/{연도}/{id}.md + JSON)
   ↓
stage4 ★ 여기 — "다른 곳에서 이미 검증한 논문" 리스트로 추가 필터 → 구현 후보 shortlist
   ↓
stage5 (shortlist 논문 pseudo-code + 간단 구현)
```

## 목적

stage3에서 자동 분석된 논문들 중, **사용자가 이 파이프라인 바깥(다른 곳)에서 이미 한 번 검토·검증한 논문**을
교차 대조하여 **구현으로 넘길 후보(shortlist)** 를 추린다.

- stage3 = 기계(agent) 판정. stage4 = 사람(사용자) 검증을 얹는 human-in-the-loop 게이트.
- 두 신호(stage3 필드 + 외부 검증)를 합쳐 **keep / drop / 우선순위** 를 정한다.

## 입력 (2종)

1. **stage3 결과**: `criteria/stage3/results/{연도}/{id_underscore}.md` (하단 JSON 블록이 기계 필터용 소스)
2. **외부 검증 논문 리스트**: [reviewed_papers.md](reviewed_papers.md) ← **나중에 사용자가 채움**
   - 원천 후보: 프로젝트 루트 [reviewed_papers.txt](../../reviewed_papers.txt) (제목·IEEE URL 혼재 raw 목록)
   - 과제: 제목/URL → stage3 `id` 매핑 (아래 "미결정" 참조)

## 출력

- `criteria/stage4/results/` — 필터 통과분 shortlist (형식 미정, [filter_criteria.md](filter_criteria.md) 참조)
- 후보: 단일 `shortlist.md` + `shortlist.json`, 또는 stage3처럼 논문별 파일. **미결정.**

## 구성 파일

| 파일 | 역할 | 상태 |
|---|---|---|
| [filter_criteria.md](filter_criteria.md) | 필터 기준·출력 스키마 (stage3 `categories.md` 대응) | 뼈대 |
| [reviewed_papers.md](reviewed_papers.md) | 외부 검증 논문 입력 리스트 (템플릿) | 빈 템플릿 |
| [orchestrator_prompt.md](orchestrator_prompt.md) | 필터 실행 절차 (stage3 orchestrator 대응) | 뼈대 |
| `results/` | shortlist 출력 | 비어 있음 |

## 미결정 (사용자 확인 필요)

- [ ] **매핑 방법**: 외부 리스트(제목/URL) ↔ stage3 `id`(`ieee_XXXXXXX` / `arxiv_YYYY.NNNNNvK`)를 어떻게 잇나?
      (IEEE URL 끝 숫자 = `ieee_{그 숫자}` 로 자동 매칭 가능 / 제목만 있는 항목은 수동 or 유사도 매칭)
- [ ] **필터 방향**: 외부 검증 논문을 **통과(우선순위↑)** 로 볼지, 이미 봤으니 **제외** 로 볼지
- [ ] **stage3 필드 추가 필터** 병용 여부 (예: 이식성 상/중 + 추천도 상만)
- [ ] **출력 형식**: 단일 shortlist 파일 vs 논문별 파일
