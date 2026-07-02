### arxiv:2010.07538v3 - Matched Quantized Min-Sum Decoding of Low-Density Parity-Check Codes (2020, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | decoder |
| 부호종류 | irregular |
| 부호rate | 0.67~0.9 |
| 부호length | 20000 |
| 연판정 | soft-2~3bit |
| 핵심기여 | CN은 기존 min 근사를 유지하되, VN 입력 메시지를 extrinsic DMC의 관측치로 모델링해 반복별 LLR로 변환(matched)함으로써 QMS 대비 복호 문턱값을 최대 0.7dB 개선 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | O |
| 개선영역 | waterfall |
| iteration감소 | X |
| latency | N/A |
| 추천도 | 중 |
| 한계,주의 | VN update 규칙이 반복마다 채널을 DE로 추정한 LLR 변환(division/log 포함)을 필요로 해 QMS 대비 연산이 복잡하며, 논문 스스로 "룩업테이블로 근사 구현 가능한가"를 미해결 문제로 남김. 검증은 unstructured irregular 앙상블 DE·FER 시뮬뿐, 정규 매트릭스/HW 미검증 |
| 추가확인 | b=3~4bit(soft-2~3bit) 수준에서 VN LLR 변환을 LUT로 구현했을 때 gatecount/throughput이 기존 min-sum 대비 어느 정도 증가하는지 |

> 총평: CN은 min-sum을 그대로 쓰면서 VN 쪽 메시지 신뢰도를 DE 기반 extrinsic LLR로 재구성해 양자화 손실을 줄이는 기법으로, Prime ECC의 min-sum 코어에 VN 업데이트 개선으로 이식 검토 가치가 있으나 LUT 근사 구현 및 HW 비용 검증이 미확인.

### B. 알고리즘 요약

1. 대상: unstructured irregular LDPC 앙상블(`(d_v,d_c)`-regular 포함), biAWGN 채널(`Y=X+N`, `N~N(0,σ²)`), 메시지는 `b`-bit 균일양자화(양자화 레벨 `M=2^b-1`).
2. 문제: 기존 quantized min-sum(QMS, Smith et al.)은 CN에서 min 근사만 쓰고 VN에서 메시지를 그대로 합산해 sum-product(SPA) 대비 복호 문턱값 손실이 큼.
3. 핵심 모델: CN→VN 메시지를 "binary-input M-ary output discrete memoryless channel(DMC)"의 관측치로 간주, 부호 대칭성 하에서 LLR `L(z)=sign(z)D_{|z|}`, `D_a=ln[P(a|+1)/P(-a|+1)]`로 정의.
4. 핵심 기법(MQMS): CN 업데이트는 기존과 동일한 min 근사(`m_{c→v}=min|m_{v'→c}|·sign(...)`)를 유지하되, VN은 채널 LLR과 각 CN 메시지의 extrinsic 신뢰도 `D` 값을 모두 실수 LLR로 변환해 합산 후 다시 `b`-bit로 양자화: `m_{v→c}=f(L_ch(y)+Σ Lex(m_{c'→v}))`.
5. 핵심 식의 의미: extrinsic DMC의 전이확률(반복별 신뢰도 `D_i^(ℓ)`)을 density evolution(DE)으로 추정해 VN이 각 양자화 레벨의 실제 신뢰도를 반영하게 하는 것이 "matched"의 핵심 — CN의 정보손실(min 근사)을 VN 단에서 보정.
6. 확장: 채널 출력도 양자화된 경우(`b0`-bit) 동일 프레임워크로 확장, `b=2`인 특수case는 기존 ternary message passing(TMP) 디코더와 일치함을 보임.
7. 구현 디테일: 안정성 분석(stability analysis)에서 degree-3 VN 비율이 안정조건 스펙트럴반경 `r<1`에 중요한 역할을 함을 도출(min-sum 계열 공통 특성).
8. 최적화 절차: DE 기반으로 differential evolution을 이용해 `b=4`, `d_v^max=20`(또는 15)에서 rate `2/3~9/10`의 irregular degree distribution(λ(x), ρ(x))을 최적화, PEG로 `n=20000` 부호 구성.
9. 결과: 문턱값 기준 QMS 대비 최대 0.7dB 개선(Table I), `b=b0=5`에서 unquantized BP 대비 0.1dB 이내로 근접. FER 시뮬(Fig.1)에서도 QMS 대비 개선 확인, rate 4/5·7/8 코드 실험.
10. 한계: HW 미설계, LUT 근사 구현 가능성은 미해결 open question으로 남김(논문 저자 스스로 언급), 검증은 unstructured 앙상블 DE·FER 시뮬뿐이며 QC-LDPC 구조나 HW 파이프라인 미검증.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| CN min 근사 업데이트 | `decoder.cpp` `CNU_Update_New_Mag()`, `C2V_Cal_New_Sgn()` | 동일한 min-sum 근사를 사용하므로 CN 로직은 변경 없이 그대로 적용 가능 |
| VN LLR 변환/양자화(extrinsic DMC 매칭) | `decoder.cpp` `VN_Cal_HD()` 등(HD/2SD/3SD), `decoder.h` `Get_VNU_*` | soft-2~3bit 영역의 VN 업데이트 로직을 DE 기반 매칭 LLR 테이블로 교체하는 개선 후보 |
| iteration별 LLR 테이블(DE로 신뢰도 추정) | `ecc_data.h` `PARAM_LLR`, `decoder.cpp` `Get_VNU_Table_Idx()` | 이미 iteration별 LLR threshold 테이블을 보유하고 있어 DE 기반 매칭 테이블로 대체/보강 가능한 구조 |
| 부호 degree distribution 최적화(DE+differential evolution) | `ecc_top.cpp` `Load_PCM()` | 특정 QC-LDPC 고정 구조라 재설계 부담 큼(이식 난이도 높음) |

> 적용 가치: 중간 — CN 로직 변경 없이 VN LLR 계산만 DE 기반 매칭 테이블로 교체하는 방식이 기존 `PARAM_LLR` 구조와 정합 가능해 보이나, 실제 게이트비용(LUT 크기, 곱셈/로그 근사)과 QC-LDPC 구조에서의 재검증이 필요.

### D. JSON 블록

```json
{
  "id": "arxiv:2010.07538v3",
  "title": "Matched Quantized Min-Sum Decoding of Low-Density Parity-Check Codes",
  "year": 2020,
  "venue": "arXiv",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "decoder",
  "code_type": "irregular",
  "code_rate": "0.67~0.9",
  "code_length": "20000",
  "soft_quant": "soft-2~3bit",
  "key_contribution": "CN은 기존 min 근사를 유지하되, VN 입력 메시지를 extrinsic DMC의 관측치로 모델링해 반복별 LLR로 변환(matched)함으로써 QMS 대비 복호 문턱값을 최대 0.7dB 개선",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "O",
  "improve_region": "waterfall",
  "iter_reduction": "X",
  "latency": "N/A",
  "recommend": "중",
  "caveat": "VN update 규칙이 반복마다 채널을 DE로 추정한 LLR 변환(division/log 포함)을 필요로 해 QMS 대비 연산이 복잡하며, 논문 스스로 룩업테이블로 근사 구현 가능한가를 미해결 문제로 남김. 검증은 unstructured irregular 앙상블 DE·FER 시뮬뿐, 정규 매트릭스/HW 미검증",
  "todo_check": "b=3~4bit(soft-2~3bit) 수준에서 VN LLR 변환을 LUT로 구현했을 때 gatecount/throughput이 기존 min-sum 대비 어느 정도 증가하는지"
}
```
