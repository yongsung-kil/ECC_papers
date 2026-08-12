# ieee:9496601 — Prime ECC 통합 패치 플랜

> 저쪽(src 보유·토큰 제한) 환경에서 **값만 채우고 얹으면 되도록** 준비한 전이물.
> 근거: stage3 C섹션 + [profile §6](../../../stage3/Prime_ECC_3.1_Claude/paper_screening_profile.md). 실 변수명은 src에서 확인(아래 `<...>`).

---

## 1. 삽입 지점 (diff 스켈레톤)

`decoder.cpp` `CNU_Update_New_Mag()` — min1/min2 magnitude **확정 직후, 스케일/테이블 매핑 이전**.

```diff
  // decoder.cpp  CNU_Update_New_Mag()  — min1/min2 확정 직후
  <min1_var> = /* 기존 min1 magnitude */;
  <min2_var> = /* 기존 min2 magnitude */;
+ <min1_var> = MIN(<min1_var>, PARAM_LLR.clipP[<bw_idx>]);   // CLIP-1 (신규)
+ <min2_var> = MIN(<min2_var>, PARAM_LLR.clipQ[<bw_idx>]);   // CLIP-2 (신규)
  // 이후 기존 식(3) 선택(자기 최소면 min2) / Get_VNU_Table_Idx() / C2V_Cal_New_Sgn() 그대로
```

- 저쪽이 채울 것: `<min1_var>`, `<min2_var>` 실명 2개 + clip이 **테이블 매핑 이전**인지 위치 확인.
- 상수 상주: `ecc_data.h` `PARAM_LLR` 계열에 bit-width별 `clipP/clipQ` 테이블 추가.
- baseline 토글: `clipP=clipQ=<내부 magnitude 상한 Lm>` (= clip off).

## 2. 인터페이스 매핑표 (toy ↔ Prime ECC)

| toy(impl.py) | Prime ECC(§6) | 비고 |
|---|---|---|
| `two_smallest → M1,M2` | `CNU_Update_New_Mag()` min1/min2 | **★ clip 2줄 삽입점** |
| `pos1` | min1 index(압축 저장) | HW는 index+sign 압축 |
| `sign_prod` | `C2V_Cal_New_Sgn()` 부호 XOR | |
| `alpha*mag` | `PARAM_LLR` / `Get_VNU_Table_Idx()` 스케일 | **명시 곱 아닐 수 있음(§3) — §3 참조** |
| `quantize=int()` | magnitude 양자화 테이블 | 단순 trunc ≠ 실제 테이블 |
| `L[(v,c)]`/`R[(c,v)]` | layered posterior−R / `C2V_Cal()` 출력 | toy full-expand vs 실코드 압축 |

## 3. 파라미터 도메인 명세 (★ 조용한 이득 소실 방지)

- **P·Q는 입력 bit-width `a`가 아니라 "내부 CN magnitude 도메인"의 정수다.** 스캔·상한 `Lm`은 내부 magnitude 표현폭 기준(§profile: magnitude 양자화 테이블/`Get_VNU_Table_Idx`). 입력폭으로 잡으면 도메인 어긋나 최적 (P,Q)가 틀림.
- **α 처리 2케이스** (profile §3: "scaling 코드상 미확인, magnitude 테이블 기반"):
  - (a) α가 명시 곱이면 → toy처럼 clip 후 `alpha*mag`.
  - (b) 스케일이 양자화 테이블 내장이면 → **`alpha*` 없음**, clip은 테이블 인덱스 매핑 **이전**의 정수 magnitude에 건다.
  - 저쪽은 (a)/(b) 중 어느 쪽인지 먼저 확정 후 삽입 순서 결정.

## 4. 시작 파라미터 그리드 (Prime ECC 정합)

| 입력 판정 | 지원? | 시작 (P,Q) seed | 경고 |
|---|---|---|---|
| soft-3bit(3SD) | ✅ primary | Lm 확정 후 `Q≈Lm/2, P≈Lm/4` (정수) | 논문값 차용 금지, seed일 뿐 |
| soft-2bit(2SD) | ✅ 보조 | Lm 작아 자유도 낮음 | a=2급은 P,Q 거의 고정 |
| soft-4bit+ | ❌ 미지원 | — | **논문 헤드라인 4bit는 이식 범위 밖** — 기대치를 2/3SD로 세팅 |

> ⚠ `L=2^(a-1)-1` 휴리스틱을 **입력폭** a에 그대로 쓰면 a=3에서 `P≈0`(min1 전멸=디코더 사망). 반드시 **내부 magnitude 폭 Lm** 기준으로 계산.

## 5. TODO (src 접근 시)
- [ ] `CNU_Update_New_Mag()`의 실제 min1/min2 변수명 확인 → diff `<...>` 치환.
- [ ] 내부 magnitude 표현폭 `Lm` 확정 (P/Q 도메인).
- [ ] α가 명시 곱(a)인지 테이블 내장(b)인지 확인 → 삽입 순서 확정.
- [ ] `PARAM_LLR`가 이미 대칭 포화 clip 중인지 확인 → baseline 정의 고정([verification_plan.md](verification_plan.md) §arms).
