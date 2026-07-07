### arxiv:0902.1786v2 - On the Dynamics of the Error Floor Behavior in (Regular) LDPC Codes (2009, arXiv / submitted to IEEE Transactions on Information Theory)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 간접 |
| 대상 | other |
| 부호종류 | regular |
| 부호rate | 0.84 |
| 부호length | 2048 |
| 연판정 | 미상 |
| 핵심기여 | 선형 동역학 모델로 지배적 absorption set의 2단계(기하성장→bit-flipping) 거동을 해석해 시뮬 불가 영역(BER 1e-14)까지 error floor를 정확 예측, 802.3an 부호의 지배 (8,8) set을 topological 탐색으로 열거 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | N/A |
| 개선영역 | N/A |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 중 |
| 한계,주의 | 특정 regular (6,32) 802.3an 부호에 특화된 error-floor 예측 이론이라 디코더/부호 개선 산출물이 없음(개선은 별도 [6] post-processing 참조) |
| 추가확인 | Prime ECC의 고VN-degree(17) QC 구조에 absorption-set 해석·importance sampling으로 error floor를 예측 가능한지, [6] post-processing과의 연결 |

> 총평: error floor의 지배 요인인 absorption set 거동을 선형대수로 해석해 저 BER까지 정확히 예측하는 방법론 논문으로, NAND error-floor 이해엔 참고가 되나 떼어 이식할 디코더/부호 산출물은 없다.

### B. 알고리즘 요약

1. 대상은 IEEE 802.3an용 regular `(6,32)` binary LDPC `(2048,1723)`, rate `0.8413`, `H = 384×2048`이고 각 `σ_ij`가 `64×64` 순열행렬인 array 구조.
2. 문제: 통신/스토리지 부호의 error floor(고SNR에서 BER 곡선 완만화)를 시뮬로 재현하려면 BER 1e-12까지 FPGA로도 데이터 1점에 약 1주 소요 — 해석적 예측이 필요.
3. 모델: message-passing 실패는 stopping set을 BSC로 확장한 absorption set(각 VN 이웃의 과반이 짝수 번 연결된 VN 집합)에서 발생, `(a,b)`로 크기 a와 unsatisfied check 수 b(EMD) 표기.
4. 핵심: absorption set 내 outgoing edge 벡터 `x`의 반복을 `x_{I} = Σ(VC)^i λ + extrinsic` 선형계로 놓고, 스펙트럼 정리로 `(VC)^i λ → μ_max^i (λ^T v_max) v_max`.
5. 의미: 최대 고유값 `μ_max = d_v - 2`(=(8,8) set에서 4)가 absorption set의 gain으로, extrinsic 정보가 set에 유입되는 속도(에러 진입 여부)를 결정 (`μ_max ≈ 5 - b/a` 근사).
6. 거동: 초기 lesser-eigenvector 영향이 사라지며 기하성장 → 이후 bit-flipping 고정점(Fig.6), 이 2단계 동역학이 error floor의 원인.
7. 정밀화: check node의 `tanh` 곱을 Taylor 전개해 "check node gain" `g_i = 1 - φ(...)^{d_c-2}` 도입, extrinsic 극성 반전(첫 iteration 원채널 LLR 오류) 확률 `P_p`로 보정.
8. 오류확률: Gaussian density evolution로 extrinsic 평균 `m_λ(ex)`를 구해 `P_AS = Q(f(a,b))` (식 7,11) 산출, 다중도 14,272와 8/1723을 곱해 union-bound BER.
9. 부호 분석: 위상적 논증+탐색으로 802.3an의 지배 (8,8) absorption set 14,272개(모두 Fig.22(b) 위상) 열거, dmin≥10 강화, 다양한 (a,b) class를 Appendix에서 완전 분류.
10. 검증: 해석 계산이 importance sampling과 FPGA hardware 시뮬과 BER 1e-14까지 일치(Fig.8) — (8,8) set의 지배성 확인.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| absorption set 구조(H 종속 error floor) | [ecc_top.cpp](../../Prime_ECC_3.1_Claude/paper_screening_profile.md) `Load_PCM()` | error floor가 PCM 구조에 종속이라는 관점은 Prime ECC PCM 분석에 개념 적용 가능(단 논문은 regular 부호 특화) |
| min-sum 메시지 동역학(체크노드 min 선택) | `decoder.cpp` `CNU_Update_New_Mag()`, `C2V_Cal()` | 논문이 선형화 분석한 대상이 min-sum 거동이라 개념 대응하나 논문은 해석 도구일 뿐 알고리즘 변경 아님 |
| error floor 케이스 발굴(importance sampling/수렴실패) | `corner.cpp` (수렴실패 추적) | error-floor 유발 패턴 발굴 목적이 유사, 방법론 참고 가능 |
| 디코더/부호 개선 산출물 | 대응 없음 | 본 논문은 예측/특성화 이론으로 이식할 기법 없음 |

적용 가치: **낮음** — 이식할 디코더/부호 산출물이 없는 error-floor 예측 이론이며 특정 regular (6,32) 부호에 특화되어, VN degree 17 QC 기반 Prime ECC에는 방법론적 참고(importance sampling·absorption set 개념) 이상은 어렵다.

### D. JSON 블록

```json
{
  "id": "arxiv:0902.1786v2",
  "title": "On the Dynamics of the Error Floor Behavior in (Regular) LDPC Codes",
  "year": 2009,
  "venue": "arXiv (submitted to IEEE Transactions on Information Theory)",
  "portability": "하",
  "nand_relevance": "간접",
  "target": "other",
  "code_type": "regular",
  "code_rate": 0.84,
  "code_length": "2048",
  "soft_quant": "미상",
  "key_contribution": "선형 동역학 모델로 지배적 absorption set의 2단계 거동을 해석해 시뮬 불가 영역(BER 1e-14)까지 error floor를 정확 예측, 802.3an 부호의 지배 (8,8) set을 topological 탐색으로 열거",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "N/A",
  "improve_region": "N/A",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "중",
  "caveat": "특정 regular (6,32) 802.3an 부호에 특화된 error-floor 예측 이론이라 디코더/부호 개선 산출물이 없음(개선은 별도 [6] post-processing 참조)",
  "todo_check": "Prime ECC의 고VN-degree(17) QC 구조에 absorption-set 해석·importance sampling으로 error floor를 예측 가능한지, [6] post-processing과의 연결"
}
```
