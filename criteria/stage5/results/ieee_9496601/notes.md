# ieee:9496601 — 통합 노트 (문서 인덱스)

> stage3: [../../../stage3/results/2022/ieee_9496601.md](../../../stage3/results/2022/ieee_9496601.md)
> 산출물: [pseudocode.md](pseudocode.md)(L0) · [impl.py](impl.py)(L1) · [integration_patch.md](integration_patch.md)(L2) · [verification_plan.md](verification_plan.md)(L3)

## Prime ECC 통합 지점
- 대응 모듈: `decoder.cpp` `CNU_Update_New_Mag()` (min1/min2 magnitude 계산 직후) — stage3 C섹션 재사용.
- 얹는 방식: min1(`M1m`), min2(`M2m`) 확정 직후 **`M1m=min(M1m,P)`, `M2m=min(M2m,Q)` 두 줄 삽입**. 이후 기존 식(3)/scaling 그대로. comparator(clip) 2개 수준.
- 부수: `P`,`Q` 상수는 `ecc_data.h` `PARAM_LLR` 계열 테이블에 bit-width별로 상주시키는 게 자연스러움.

## 이식 난이도
- **낮음**. 기존 min-sum CNU에 상한 clip 2개만 추가, 스케줄(row-layered)·부호구조 변경 없음.
- 유일 부담: `(P,Q)` 재탐색 (부호·bit-width별 정수 스캔).

## 검증 (2단: mechanics는 여기, 성능은 src)
- **mechanics(여기, 완료)**: `python impl.py` — clip이 `max|R|` 4.50→2.25(=α·Q)로 억제됨 확인. **성능 아님**(toy·float·flooding·6var → floor 없음).
- **성능(저쪽 src)**: 설계 → [verification_plan.md](verification_plan.md). 실 QC-LDPC·저bit fixed-point·NAND soft-read에서 baseline/delta/대조군(P=Q) UBER·floor·bit절감 실측.

## 한계 · 리스크
- 여기 프로토타입은 **알고리즘 mechanics 검증용**일 뿐, 논문 이득(저bit UBER↓)은 대형부호·저bit fixed-point에서만 발현.
- 주의(패치·검증에 반영됨): **P/Q 도메인**(입력폭 아님, 내부 magnitude), **baseline 이중정의**(기존 PARAM_LLR 포화), **soft-4bit 미지원**(목표 2/3SD). 상세: [integration_patch.md](integration_patch.md) §3-4, [verification_plan.md](verification_plan.md) §1-2.

## TODO (실이식) → [integration_patch.md](integration_patch.md) §5 참조
- `CNU_Update_New_Mag()` 실 min1/min2 변수명 확인 후 clip 2줄 삽입.
- 내부 magnitude 폭 `Lm`·α 도메인 확정 → (P,Q) 스캔 도메인 고정.
- verification_plan.md대로 저쪽에서 UBER 곡선 실측.
