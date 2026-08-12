# Stage 5 — Pseudo-code + 이식/검증 패키지

> 위치: `criteria/stage5/`
> 상태: 예시 1편 완료([results/ieee_9496601/](results/ieee_9496601/)). 깊이·언어 확정(아래 결정사항).

---

## 파이프라인 위치

```
stage3 (심층 분석) → stage4 (외부 검증 필터 → shortlist) → stage5 ★ (구현)
```

## 운영 전제 (중요)

- **이 PC엔 Prime ECC src가 없다.** src(C++ 원본, /또는 Python 버전)는 **다른 환경**에 있고 그 환경은 **토큰이 제한적**.
- 전략: 토큰 넉넉한 **여기서 이식·검증 패키지를 최대한 준비** → 저쪽은 **빈칸 채우고 통합+실행만** 싸게.
- 따라서 stage5 산출물은 "동작하는 독립 디코더"가 아니라 **저쪽으로 보낼 전이물 패키지**다.

## 목적

stage4 shortlist(현재는 stage3 샘플) 논문의 핵심 기법을 **저쪽 src에 바로 얹고 검증할 수 있는** 패키지로 떨군다.

## 구현 깊이 사다리 (여기서 어디까지 / 무엇을 저쪽에)

| Lv | 산출물 | 여기서? |
|---|---|---|
| L0 | pseudocode.md — 언어 중립 의사코드 + delta 위치 | ✅ 여기 |
| L1 | impl.py — **delta-only 정확성 레퍼런스**(mechanics smoke test, 성능 아님) | ✅ 여기 |
| L2 | integration_patch.md — 삽입 diff·매핑표·파라미터 도메인 명세 | ✅ 여기 |
| L3 | verification_plan.md — 저쪽이 돌릴 실험 설계(부호·채널·arm·지표·P/Q스캔·pass/fail) + (선택) 스캔 하네스 골격 | ✅ 여기 |
| L4 | **실제 성능 실측(UBER/FER/floor, bit 절감)** | ❌ **src(저쪽)에서만** |

- **완전한 독립 디코더 재구현 금지** — Prime ECC가 이미 min-sum을 보유. 전이되는 건 delta(수 줄)뿐.
- **성능 검증을 여기서 하지 말 것** — 이득은 저bit fixed-point·실 QC-LDPC floor·NAND soft-read에서만 발현. float toy는 오도.

## 대상 (입력)

- **원래 목표**: stage4 shortlist 논문 → **Prime ECC 3.1 src 코드**에 이식.
  - 현재 이 repo에는 src 코드 자체는 없고 프로파일만 있음:
    [Prime_ECC_3.1_Claude/paper_screening_profile.md](../stage3/Prime_ECC_3.1_Claude/paper_screening_profile.md)
    (모듈 지도 §6 = 이식 지점 참조)
- **지금(stage4 미완)**: stage3 결과 중 **일부 샘플 논문**으로 예시 진행.
  - 후보 선정 → [targets.md](targets.md)

## 산출물 구조

논문 1편 = 폴더 하나: `criteria/stage5/results/{id_underscore}/`

```
results/{id_underscore}/
├── pseudocode.md          # L0 의사코드 + 알고리즘 명세
├── impl.py                # L1 delta-only 정확성 레퍼런스 (mechanics smoke test)
├── integration_patch.md   # L2 삽입 diff·매핑표·파라미터 도메인 명세
├── verification_plan.md   # L3 저쪽이 돌릴 검증 설계
└── notes.md               # 통합 요약·이식 난이도·한계 (위 문서 인덱스)
```

템플릿: [results/_TEMPLATE/](results/_TEMPLATE/) · 완성 예시: [results/ieee_9496601/](results/ieee_9496601/)

## 구성 파일

| 파일 | 역할 | 상태 |
|---|---|---|
| [implementation_prompt.md](implementation_prompt.md) | 논문 1편 구현 절차·출력 형식 (stage3 `analysis_prompt` 대응) | 뼈대 |
| [orchestrator_prompt.md](orchestrator_prompt.md) | 멀티 agent 실행 (stage3 orchestrator 대응) | 뼈대 |
| [targets.md](targets.md) | 예시로 쓸 stage3 샘플 논문 목록 | 빈 템플릿 |
| `results/_TEMPLATE/` | 산출물 폴더 템플릿 | 템플릿 |

## 결정사항 (2026-07-09 라이트리뷰 후 확정)

- [x] **구현 언어 = Python.** 여기 Python은 delta 정확성 레퍼런스 + (저쪽용) 실코드급 검증 하네스 골격. **C++가 원본**이며 성능 실측은 src에서. cpp는 길어서 여기서 직접 안 함.
- [x] **구현 깊이 = L0~L3 준비, L4(성능 실측)는 src.** 완전 독립 디코더 금지, 여기서 성능검증 금지(위 사다리).
- [x] **Prime ECC src 접근 = 여기 불가.** 여기선 패키지만 준비, 실행은 저쪽. profile로만 판정.
- [x] **예시 대상 = stage3 기준** (stage4 미완). 첫 예시 `ieee_9496601` 완료.
- [x] **스캔 하네스는 여기서 안 만듦(계획만).** [verification_plan.md](results/ieee_9496601/verification_plan.md) 설계(스캔 그리드·CSV·pass/fail)로 충분 — 하네스 코드는 실 H·채널·내부 magnitude 폭이 있는 **src 환경에서 작성**. (2026-07-09 결정)

> 근거: `_pm/tasks/20260709_stage5_depth_review/` (라이트리뷰 4관점).
