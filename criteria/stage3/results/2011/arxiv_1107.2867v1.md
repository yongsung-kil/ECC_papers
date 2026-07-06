### arxiv_1107.2867v1 - A Two Stage Selective Averaging LDPC Decoding (2011, arXiv [cs.IT])

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | decoder |
| 부호종류 | regular |
| 부호rate | 0.5 |
| 부호length | 504 |
| 연판정 | 무관 |
| 핵심기여 | 2단 디코더: 1단 selective LLR averaging(oscillating TS)+2단 unsatisfied-CN 연결 비트 flip(elementary TS)로 error-floor 저감 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | O |
| 개선영역 | error-floor |
| iteration감소 | X |
| latency | 악화 |
| 추천도 | 중 |
| 한계,주의 | full tanh/atanh Sum-Product 기반 + LLR-BP, 소형 regular PEG(504)만 검증, min-sum 정합·고rate QC-LDPC 미검증 |
| 추가확인 | Prime ECC min-sum(비 tanh)에 selective averaging/bit-flip이 이식될 때 error-floor 개선 유지되는지, β/ν/η/CNthreshold 튜닝 부담 |

> 총평: trapping-set 대응 error-floor 저감 post-processing 디코더로 아이디어(selective averaging+bit-flip)는 min-sum 루프에 접목 여지가 있으나 full SPA·소형 저rate 코드 검증뿐이라 이식성 중.

### B. 알고리즘 요약

1. 시스템: AWGN 채널, factor graph 기반 LLR-BP LDPC 복호, error-floor(trapping set) 저감이 목표.
2. 문제: 고SNR에서 trapping set(특히 elementary/oscillating)이 error-floor를 유발, 기존 averaging 디코더는 waterfall 수렴을 늦춤.
3. 모델: `(x,y)` trapping set = x개 VN 유발 부분그래프에 y개 홀수차 unsatisfied CN, oscillating은 cycle 다중 통과로 LLR 진동.
4. 1단 기법 (selective averaging): 선택된 VN의 출력 메시지를 이전 iter과 평균 `m^(l)=(m^(l)+m^(l-1))/2`, CN 메시지는 미변경.
5. 노드 선택(Algorithm 1): belief `B=|L|` 감소폭 `>β`(진동) 또는 증가율 `>ν`(초기 TS)면 select, 신뢰 노드는 빠르게 수렴시켜 진동 노드 해결 유도.
6. 2단 기법 (elementary TS): max iter 후 미수렴 & unsatisfied CN 수 `<CNthreshold`면, unsatisfied CN 연결 VN 집합 `Vun`에서 공통 CN 없는 부분집합 `Vnc` 선택.
7. 비트 flip: 해당 VN 채널 LLR을 `C(vk)=-C(vk)*η`로 부호반전·스케일, `Selected=2`로 상시 averaging 후 1단 재실행(backtracking은 복잡도 이유로 제거).
8. 최적화: β, ν, η, CNthreshold 상수 튜닝, all-zero codeword 가정 시뮬.
9. 결과: regular PEG(504,252,3,6)에서 제안 2단 디코더가 averaging/standard 디코더 대비 BER·BLER 개선(수치는 그림, 본문 서술 없음→미상).
10. 한계: HW 미설계·시뮬만, full tanh/atanh SPA 사용, 소형 저rate(0.5) 단일 코드만 검증, 2단 재복호로 latency 증가.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| selective averaging VN 메시지 갱신 | `decoder.cpp` `VN_Cal_HD()` 등, `LDPC_Decoder()` 이터레이션 루프 | VN 처리에 belief 기반 averaging 삽입 가능(이식 여지 있음) |
| 노드 선택(belief 증감 임계 β/ν) | `ecc_data.h` `PARAM_LLR`, `decoder.cpp` `Get_VNU_Table_Idx()` | 적응형 LLR 테이블 옆에 선택 로직 추가 여지 |
| 2단 bit-flip post-processing | `corner.cpp`(수렴실패 추적) + `LDPC_Decoder()` 재호출 | 수렴실패 시 unsatisfied CN 기반 flip 후 재복호로 연동 가능 |
| full tanh/atanh Sum-Product CN 연산 | 대응 없음 | Prime ECC는 min-sum(min1/min2)로 SPA 미보유 |

적용 가치: **중간** — error-floor 저감(Prime ECC 관심영역)에 부합하고 selective averaging+bit-flip 아이디어는 min-sum 루프·corner 추적에 접목 여지가 있으나, full SPA·소형 저rate 코드 검증뿐이라 min-sum·고rate QC-LDPC 재검증 필요.

### D. JSON 블록

```json
{
  "id": "arxiv:1107.2867v1",
  "title": "A Two Stage Selective Averaging LDPC Decoding",
  "year": 2011,
  "venue": "arXiv [cs.IT]",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "decoder",
  "code_type": "regular",
  "code_rate": 0.5,
  "code_length": "504",
  "soft_quant": "무관",
  "key_contribution": "2단 디코더: 1단 selective LLR averaging(oscillating TS)+2단 unsatisfied-CN 연결 비트 flip(elementary TS)로 error-floor 저감",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "O",
  "improve_region": "error-floor",
  "iter_reduction": "X",
  "latency": "악화",
  "recommend": "중",
  "caveat": "full tanh/atanh Sum-Product 기반 + LLR-BP, 소형 regular PEG(504)만 검증, min-sum 정합·고rate QC-LDPC 미검증",
  "todo_check": "Prime ECC min-sum(비 tanh)에 selective averaging/bit-flip이 이식될 때 error-floor 개선 유지되는지, β/ν/η/CNthreshold 튜닝 부담"
}
```
