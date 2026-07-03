### arxiv:1809.10910v2 - Protograph-Based LDPC Code Design for Ternary Message Passing Decoding (2018, arXiv cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | both |
| 부호종류 | protograph |
| 부호rate | 0.67~0.9 |
| 부호length | 22176 |
| 연판정 | soft-2~3bit |
| 핵심기여 | erasure를 3번째 메시지로 쓰는 ternary message passing(TMP) 복호+DE로 최적화한 protograph 부호로 BMP 대비 최대 0.6dB 이득 |
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
| 한계,주의 | biAWGN 채널·통신표준(광통신/5G) 지향, HW 미설계·error-floor는 부호설계로만 제어, 복호부는 TMP에 맞춘 부호와 결합돼야 이득 발현 |
| 추가확인 | 3진 메시지(erasure 포함) 양자화가 NAND soft-read(2~3bit LLR)와 gate 절감 측면에서 min-sum 대비 실이득 있는지, NAND RBER 채널에서 재검증 필요 |

> 총평: erasure 포함 3진 메시지로 복호 데이터 흐름을 줄이는 저복잡도 MP 복호 + 전용 protograph 부호설계로 waterfall 이득을 보이나, biAWGN·통신 지향이고 HW 미설계라 NAND binary LDPC 이식은 중간.

### B. 알고리즘 요약

1. 채널: biAWGN, 입력 `{-1,+1}`, VN이 채널 LLR `Lch=2y/σ²` 계산; 부호는 protograph 기반 QC-LDPC(rate 2/3~9/10, 유한길이 예제 n=22176 QC).
2. 풀려는 문제: 고throughput FEC에서 BP 메시지의 양자화 비트 수가 복잡도(데이터 흐름)를 좌우 - 메시지 알파벳을 최소화하면서 채널 soft 정보를 활용.
3. 핵심 모델: 반복 복호 메시지를 extrinsic 채널(binary error-and-erasure channel, BEEC) 출력으로 모델링, 메시지 신뢰도 `D=ln((1-θ-ε)/θ)`.
4. 핵심 기법(TMP): 모든 VN↔CN 메시지를 3진 알파벳 `M={-1,0,+1}`(0=erasure)로 제한, 양자화 함수 `f(x)`는 임계값 `a`로 3분할 (`|x|<a`면 0).
5. CN 갱신은 이웃 메시지 곱(부호), VN 갱신은 `f(Lch + Σ D_{CV}·m_{C→V})` - 가중치 `D_{CV}`는 반복별·edge type별로 설계단계에서 결정(복호 복잡도에 미포함).
6. erasure 도입 근거: state VN(accumulator/5G 부호)이나 punctured 부호처럼 초기 LLR=0인 경우 불확실성을 명시적으로 표현 → threshold 개선.
7. 부수 디테일: `a=1.3`(예제), 반복별 `D_{CV}` 테이블(Table IV~VII)을 설계단계에서 사전계산, 2비트로 3진 표현(양자화 레벨 1개 손해).
8. 최적화: 비정형·protograph 앙상블에 대해 정확한 density evolution(DE)로 threshold 계산, stability 조건 유도, differential evolution으로 protograph 탐색(가중스펙트럼 `G(ω)`로 최소거리 양수 제약→error floor 제어).
9. 결과: TMP-최적화 앙상블이 BMP 대비 asymptotic 0.37~0.6dB threshold 이득, 유한길이(n=22176)에서 unquantized BP 대비 0.2~0.5dB 손실 이내, TMP로 AR4JA 복호 시 0.2~0.5dB 우위.
10. 한계: HW 미설계, biAWGN·통신표준(광/5G) 지향, error-floor는 부호설계(최소거리)로만 제어, 이득은 TMP 전용 부호와 결합해야 발현.

### C. Prime ECC 관련 모듈 핀포인트

```
| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| TMP 3진 메시지 복호 루프 (CN 곱, VN f(·)) | decoder.cpp LDPC_Decoder(), C2V_Cal() | 반복 message passing 복호 루프에 대응, min-sum 대신 3진 MP로 교체 시 여기 수정 |
| 채널 LLR→3진 양자화 f(x), 임계값 a | channel.cpp Set_LLR_Th(), Set_R_Offset() | soft-read LLR threshold/양자화부에 대응, 2~3bit soft와 정합 가능 |
| 반복별 가중치 D_CV 테이블 | ecc_data.h PARAM_LLR, decoder.cpp Get_VNU_Table_Idx() | iteration별 LLR/가중 테이블 참조 구조와 유사(적응형 LLR 이미 보유) |
| protograph/부호 앙상블 설계 (DE+DifferentialEvolution) | ecc_top.cpp Load_PCM() | 부호구조 로드부에만 접점, DE 기반 부호최적화 툴은 미보유 |
| erasure(0) 메시지 도입 | 대응 없음 | Prime ECC는 HD/2SD/3SD 기반 min-sum, erasure 상태 메시지 미보유 |
```

적용 가치: **중간** - 저복잡도 3진 MP 복호와 반복별 가중치 설계는 Prime ECC 복호루프·적응형 LLR 구조와 접점이 있으나, biAWGN·통신 부호 최적화가 전제이고 HW·NAND RBER 검증이 없어 이득 이식 전 재검증이 필요하다.

### D. JSON 블록

```json
{
  "id": "arxiv:1809.10910v2",
  "title": "Protograph-Based LDPC Code Design for Ternary Message Passing Decoding",
  "year": 2018,
  "venue": "arXiv cs.IT",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "both",
  "code_type": "protograph",
  "code_rate": "0.67~0.9",
  "code_length": "22176",
  "soft_quant": "soft-2~3bit",
  "key_contribution": "erasure를 3번째 메시지로 쓰는 ternary message passing(TMP) 복호+DE로 최적화한 protograph 부호로 BMP 대비 최대 0.6dB 이득",
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
  "caveat": "biAWGN 채널·통신표준(광통신/5G) 지향, HW 미설계·error-floor는 부호설계로만 제어, 복호부는 TMP에 맞춘 부호와 결합돼야 이득 발현",
  "todo_check": "3진 메시지(erasure 포함) 양자화가 NAND soft-read(2~3bit LLR)와 gate 절감 측면에서 min-sum 대비 실이득 있는지, NAND RBER 채널에서 재검증 필요"
}
```
