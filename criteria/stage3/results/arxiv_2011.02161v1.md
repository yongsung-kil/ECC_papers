### arxiv:2011.02161v1 - Learned Decimation for Neural Belief Propagation Decoders (2020, arXiv (Invited Paper))

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 간접 |
| 대상 | decoder |
| 부호종류 | 기타 |
| 부호rate | 0.5 |
| 부호length | 128 |
| 연판정 | soft-4bit+ |
| 핵심기여 | Neural BP(NBP) 디코더에 list-based decimation과 NN 기반 learned decimation 2단계를 결합해 short LDPC code에서 ML 근접(<1dB) 성능을 달성하는 NBP-D 디코더 제안 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 언급 |
| 정정능력향상 | O |
| 개선영역 | waterfall |
| iteration감소 | 부분 |
| latency | 악화 |
| 추천도 | 하 |
| 한계,주의 | decimation 횟수 nD에 따라 복잡도가 지수적으로 증가(2^nD)하며 CCSDS (128,64) 등 short code 대상, NAND용 대용량·고rate QC-LDPC에서는 트리 분기 복잡도 폭증으로 비현실적 |
| 추가확인 | 대용량(수천~수만 bit) 고rate QC-LDPC에서 decimation tree 복잡도 스케일링 검증 필요 |

> 총평: short LDPC code(n=128, rate 0.5)에서 NBP + list/learned decimation으로 ML 근접 성능을 달성하나 복잡도가 지수적으로 증가해 NAND용 대용량·고rate QC-LDPC HW 디코더에는 이식하기 어려움.

### B. 알고리즘 요약

1. 시스템: CCSDS 표준 short LDPC code(`n=128`, `k=64`, `rate=0.5`, 평균 CN degree `d̄c=8`), AWGN 채널, BPSK.
2. 문제: NBP(weighted BP, 각 엣지에 학습 가중치 부여)는 적은 iteration에서는 BP보다 우수하지만 iteration을 늘리면 BP와 성능이 수렴하고 ML과의 gap이 남음 — 이는 absorbing set 때문.
3. 핵심 가정: LLR 절댓값이 가장 작은(least reliable) VN을 결정하면 correct sign 여부가 수렴을 좌우한다는 가정 하에 decimation(해당 VN을 ±∞로 고정) 적용.
4. 핵심 기법 1단(list-based decimation): NBP를 `ℓmax` iteration 수행 후 가장 신뢰도 낮은 VN을 찾아 `+∞`/`−∞` 두 갈래로 분기하는 binary decoding tree를 `nD`번 반복 구성, 최종 `2^nD`개 codeword candidate 생성.
5. 핵심 식: `μch,v = μch,v + sign(μv^(ℓmax)) · fNN(μch,v, {μ(c→v)^(ℓmax)|c∈N(v)}, θ)` — 2단(learned decimation)에서 NN이 decimation 크기(부호는 유지)를 예측해 channel LLR에 더함으로써 tree 분기 없이 유사 효과를 냄.
6. 확장: 최종 후보 codeword 중 `argmax_i Σ_j y_j(-1)^{c_i,v_j}` (수신값과의 상관 최대)로 최종 codeword 선택.
7. 부수 트릭: NN은 3-layer(16, 16, 1 뉴런, ReLU→ReLU→linear)로 모든 VN·모든 decimation step에 가중치 공유(weight tying), 학습 시 decoding tree의 정답 경로만 사용하는 genie 가정으로 학습 비용 절감.
8. 학습/최적화: 1단계로 iteration-tied NBP를 multiloss bitwise cross-entropy + Adam으로 학습, 이후 가중치 고정하고 NBP-D 전체를 동일 손실로 추가 학습.
9. 결과: NBP(50 iter)는 ML 대비 약 1.75dB 열위, NBP-D(10,4,0)는 NBP(50) 대비 0.4dB 개선(복잡도 5.4배, weight 수 1152), learned decimation 추가(NBP-D(10,4,4))로 ML과 1dB 미만 차이까지 근접(복잡도 18.2배).
10. 한계: 복잡도가 `dc·m·ℓmax·(2^(nD+1)−1) + nLD·2^nD`로 decimation 수에 지수적으로 증가, short code(n=128)에서만 검증, HW 구현·gate/throughput 분석 전무.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| Neural BP(가중치 학습 BP) | 대응 없음 | Prime ECC는 min-sum 기반 고정 알고리즘이며 학습형 엣지 가중치 구조 없음 |
| list-based decimation(binary tree 분기) | 대응 없음 | 코드워드 후보를 지수적으로 늘리는 구조라 Prime ECC의 단일 경로 파이프라인 디코더와 근본적으로 불일치 |
| learned decimation(NN 기반 LLR 보정) | `channel.cpp` `Set_LLR_Th()` | 개념적으로 LLR 임계값 조정과 유사하나 NN 추론 결합은 HW 시뮬레이터에 대응 없음 |
| 최종 codeword 선택(correlation argmax) | `partial_CRC.cpp` / `full_CRC.cpp` | Prime ECC는 CRC 기반 조기종료·검증이며 다중 후보 correlation 비교 방식과는 다름, 대응 없음 |

적용 가치: `낮음` — short code(n=128) 전용이며 decimation tree로 인한 지수적 복잡도 증가가 NAND용 대용량·고rate QC-LDPC HW 디코더의 고정 파이프라인 구조와 근본적으로 맞지 않음.

### D. JSON 블록

```json
{
  "id": "arxiv:2011.02161v1",
  "title": "Learned Decimation for Neural Belief Propagation Decoders",
  "year": 2020,
  "venue": "arXiv (Invited Paper)",
  "portability": "하",
  "nand_relevance": "간접",
  "target": "decoder",
  "code_type": "기타",
  "code_rate": 0.5,
  "code_length": 128,
  "soft_quant": "soft-4bit+",
  "key_contribution": "Neural BP 디코더에 list-based decimation과 NN 기반 learned decimation 2단계를 결합해 short LDPC code에서 ML 근접(<1dB) 성능을 달성하는 NBP-D 디코더 제안",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "언급",
  "correction_gain": "O",
  "improve_region": "waterfall",
  "iter_reduction": "부분",
  "latency": "악화",
  "recommend": "하",
  "caveat": "decimation 횟수 nD에 따라 복잡도가 지수적으로 증가(2^nD)하며 CCSDS (128,64) 등 short code 대상, NAND용 대용량·고rate QC-LDPC에서는 트리 분기 복잡도 폭증으로 비현실적",
  "todo_check": "대용량(수천~수만 bit) 고rate QC-LDPC에서 decimation tree 복잡도 스케일링 검증 필요"
}
```
