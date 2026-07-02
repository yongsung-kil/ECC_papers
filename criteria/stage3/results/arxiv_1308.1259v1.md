### arxiv:1308.1259v1 - On Characterization of Elementary Trapping Sets of Variable-Regular LDPC Codes (2013, arXiv)

| 카테고리 | 값 |
|---|---|
| 이식성 | 하 |
| NAND관련성 | 간접 |
| 대상 | code-design |
| 부호종류 | regular |
| 부호rate | 미상 |
| 부호length | 미상 |
| 연판정 | 무관 |
| 핵심기여 | left-regular LDPC의 (a,b) elementary trapping set 비동형 구조를 나열하고, 다수가 짧은 사이클의 layered superset(LSS)임을 증명, LSS 기반 탐색 알고리즘 제시 |
| HW설계 | X |
| 검증수준 | 이론 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | X |
| 개선영역 | N/A |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 하 |
| 한계,주의 | 순수 그래프이론/조합론 분석이며 실제 부호 구성·시뮬레이션·error-floor 수치 결과 없음 |
| 추가확인 | 특정 (a,b) 클래스가 Prime ECC 3.1의 실제 H-matrix(비-regular, QC-LDPC)에도 적용되는지는 별도 검증 필요 |

> 총평: dl=3~6, g=6/8 left-regular LDPC의 trapping set 위상을 exhaustive하게 카탈로그화한 이론 논문으로, 실제 부호/디코더/HW 적용 사례나 수치 결과가 전혀 없어 이식 가치는 낮음.

### B. 알고리즘 요약

1. 대상은 좌측 정규(variable-regular, degree `dl`) LDPC 코드의 Tanner graph이며, error floor의 주원인인 elementary trapping set(ETS)의 그래프 구조를 특성화한다.
2. 기존 연구는 특정 구조코드(STS, EG, array-based)나 작은 크기의 trapping set에 한정되어 있어, 임의의 `dl`, girth `g`, 클래스 `(a,b)`(a=집합 크기, b=unsatisfied check node 수)에 대한 일반적 특성화가 부족했다.
3. ETS는 유도 부분그래프의 check node degree가 1 또는 2뿐인 trapping set으로 정의하며, `normal graph`(degree-1 제거, degree-2를 edge로 치환) 표현으로 단순화한다.
4. 핵심 개념은 layered superset(LSS): ETS `S`가 부분집합 `C`의 LSS이면 `C=S(0) ⊂ S(1) ⊂ ... ⊂ S(a-α)=S` 형태로 한 노드씩 늘려가는 nested ETS 열이 존재.
5. LSS 성질은 짧은 사이클에서 출발해 노드를 하나씩 추가하며 더 큰 ETS를 찾는 탐색(Routine 1, Algorithm 1)을 가능케 하며, 복잡도는 `O(b·dr)`(dr=check node degree) 수준.
6. 비동형 구조 열거에는 nauty 그래프 동형성 프로그램을 사용하되, normal graph 표현으로 탐색 공간을 극적으로 축소(예: 5300만개 → 11개 구조).
7. `dl=3,4,5,6`, `g=6,8`, `a,b≤10` 범위에서 각 (a,b) 클래스의 비동형 구조 수와 이들이 어떤 길이의 사이클의 LSS인지 표(Table I~VIII)로 전수 제시.
8. 결과적으로 대부분의 dominant ETS(작은 a,b)는 짧은 사이클의 LSS이며, 일부(특히 두 ETS가 check node로 연결된 구조)는 "NA"(어떤 사이클의 LSS도 아님)로 분류됨.
9. 수치 결과는 그래프 구조 개수(예: dl=6,g=6에서 (9,10) 클래스 5411개 구조 중 1개만 non-LSS)이며 BER/error-floor 곡선이나 실제 부호 성능 실험은 없음.
10. 한계: 순수 조합론적 그래프 특성화 연구로, 특정 QC-LDPC H-matrix 설계나 HW/디코더 구현으로 이어지지 않으며 시뮬레이션·실측 결과가 전무함.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| ETS/absorbing set 구조 특성화 | 대응 없음 | Prime ECC 3.1은 특정 QC-LDPC H-matrix 고정 사용, trapping-set 카탈로그 기반 재설계 모듈 없음 |
| LSS 기반 짧은 사이클 탐색 알고리즘 | `ecc_top.cpp` `Load_PCM()` | H-matrix 품질 사전검증(오프라인) 용도로만 참고 가능, 실코드 없음 |
| Error floor 원인 분석 | 대응 없음 | 디코더 알고리즘 변경이 아닌 부호 구성 단계 이론이라 decoder.cpp와 직접 연결 안 됨 |

> 적용 가치: 낮음 — variable-regular(비-QC) LDPC의 순수 그래프이론적 trapping set 카탈로그로, Prime ECC의 고정된 QC-LDPC 구조 재설계에는 이론적 참고 이상의 직접 이식 요소가 없음.

### D. JSON 블록

```json
{
  "id": "arxiv:1308.1259v1",
  "title": "On Characterization of Elementary Trapping Sets of Variable-Regular LDPC Codes",
  "year": 2013,
  "venue": "arXiv",
  "portability": "하",
  "nand_relevance": "간접",
  "target": "code-design",
  "code_type": "regular",
  "code_rate": null,
  "code_length": "미상",
  "soft_quant": "무관",
  "key_contribution": "left-regular LDPC의 (a,b) elementary trapping set 비동형 구조를 나열하고, 다수가 짧은 사이클의 layered superset(LSS)임을 증명, LSS 기반 탐색 알고리즘 제시",
  "hw_designed": "X",
  "verification": "이론",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "X",
  "improve_region": "N/A",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "하",
  "caveat": "순수 그래프이론/조합론 분석이며 실제 부호 구성·시뮬레이션·error-floor 수치 결과 없음",
  "todo_check": "특정 (a,b) 클래스가 Prime ECC 3.1의 실제 H-matrix(비-regular, QC-LDPC)에도 적용되는지는 별도 검증 필요"
}
```
