### arxiv:1002.4311v1 - Lowering the Error Floor of LDPC Codes Using Cyclic Liftings (2010, arXiv/cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 간접 |
| 대상 | both |
| 부호종류 | QC-LDPC |
| 부호rate | 0.4026~0.5 |
| 부호length | 310~3024 |
| 연판정 | 무관 |
| 핵심기여 | 지배적 trapping set의 짧은 사이클을 lifting으로 제거하는 IES 알고리즘으로 error floor 저감 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | O |
| 개선영역 | error-floor |
| iteration감소 | X |
| latency | N/A |
| 추천도 | 중 |
| 한계,주의 | BSC/Gallager A/B 대상, dominant trapping set을 미리 알아야 함, block length 증가로 rate/latency 부담 |
| 추가확인 | min-sum 기반 우리 고rate QC-LDPC의 dominant trapping set 목록 확보 가능 여부 |

> 총평: cyclic lifting으로 특정 trapping set을 의도적으로 제거하는 부호설계 기법 - 원리는 우수하나 우리 고정 H-matrix 재설계·재검증 부담이 커 이식성 하.

### B. 알고리즘 요약

1. 대상: base LDPC 코드(Tanner (155,64), 정규 (504,252), 비정규 (200,100))를 cyclic N-lifting하여 QC-LDPC로 확장, error floor 개선.
2. 문제: 유한길이 LDPC의 error floor는 dominant trapping set이 원인이며, 이를 base code의 성질(차수분포/인코더·디코더 구조/rate)을 보존하며 낮추고자 함.
3. 모델: `(a,b)` trapping set = a개 변수노드가 유도 부그래프에서 b개 홀수차수 검사노드를 갖는 구조; BSC에서 `FER ≈ N_J·ε^J` (J=최소 critical number).
4. 핵심기법: base 그래프의 각 edge에 순환치환 `π_d`(index `d`)를 배정해 N-lifting; trapping set을 구성하는 짧은 사이클을 lifted 그래프에서 더 긴 사이클로 사상.
5. 핵심식: 사이클 c의 permutation index `d = Σ(-1)^i d_{i+1} mod N` (식 3); `O(c)>1`(d≠0)이면 c의 역상이 모두 c보다 긴 사이클(정리1, 따름정리1).
6. 확장: Intentional Edge Swapping(IES) 알고리즘 - trapping set을 critical number 오름차순으로 정렬 후 최소 edge를 골라 `O(c)>1`이 되는 index를 greedy하게 배정(Algorithm 1).
7. 구현 디테일: cyclic 구조라 QC-LDPC로 HW 친화적; block-circulant `H̃'`로 rate/minimum distance 경계 유도.
8. 이론 결과: `N=2^q`일 때 `r(N) ≤ r`(full-rank면 등호, 정리2), `d_min ≤ d_min^(N) ≤ N·d_min`(정리3).
9. 결과: Tanner code에서 N=2로 FER slope 3→4, N=5로 5까지 상승; 무작위 lifting 대비 error floor 크게 우수; BSC용 설계가 BIAWGN+min-sum에서도 error floor 소멸(FER 1e-8까지).
10. 한계: BSC/Gallager A/B로 설계, dominant trapping set 사전 파악 필요, HW 미설계·시뮬만, block length 증가가 비용.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| cyclic lifting으로 QC-LDPC H-matrix 구성 | `ecc_top.cpp` `Load_PCM()` + H-matrix | trapping set 제거형 H-matrix 재설계에 해당 - 고정 부호 재검증 부담 큼 |
| error-floor 개선(정정능력) | `decoder.cpp` `LDPC_Decoder()` (성능 평가 대상) | 디코더 알고리즘 변경 없이 부호구조로 error floor 개선 |
| trapping set/사이클 구조 분석 | `corner.cpp` (수렴실패 추적) | dominant trapping set 식별과 간접 연관 |

적용 가치: 낮음 - 원리(의도적 사이클 제거로 error floor 저감)는 가치 있으나 Prime ECC의 특정 고rate QC-LDPC H-matrix를 재설계·재검증해야 하고 BSC/Gallager 가정이라 직접 이식 부담이 크다.

### D. JSON 블록

```json
{
  "id": "arxiv:1002.4311v1",
  "title": "Lowering the Error Floor of LDPC Codes Using Cyclic Liftings",
  "year": 2010,
  "venue": "arXiv/cs.IT",
  "portability": "하",
  "nand_relevance": "간접",
  "target": "both",
  "code_type": "QC-LDPC",
  "code_rate": null,
  "code_length": "310~3024",
  "soft_quant": "무관",
  "key_contribution": "지배적 trapping set의 짧은 사이클을 cyclic lifting으로 제거하는 IES 알고리즘으로 error floor 저감",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "O",
  "improve_region": "error-floor",
  "iter_reduction": "X",
  "latency": "N/A",
  "recommend": "중",
  "caveat": "BSC/Gallager A/B 대상, dominant trapping set 사전 파악 필요, block length 증가로 rate/latency 부담",
  "todo_check": "min-sum 기반 우리 고rate QC-LDPC의 dominant trapping set 목록 확보 가능 여부"
}
```
