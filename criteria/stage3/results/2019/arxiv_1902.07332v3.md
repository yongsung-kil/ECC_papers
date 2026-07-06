### arxiv:1902.07332v3 - Construction of QC LDPC Codes with Low Error Floor by Efficient Systematic Search and Elimination of Trapping Sets (2019, IEEE Trans. Communications (submitted) / arXiv cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | both |
| 부호종류 | QC-LDPC |
| 부호rate | 0.4~0.5 |
| 부호length | 145~2133 |
| 연판정 | soft-2~3bit |
| 핵심기여 | QC 구조가 배제하는 LETS를 edge-coloring으로 규명하고, parent/child 기반 계층적 backward 탐색으로 목표 trapping set만 제거해 짧은 블록길이로 낮은 error-floor 달성 |
| HW설계 | X |
| 검증수준 | 시뮬 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | O |
| 개선영역 | error-floor |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 중 |
| 한계,주의 | 저rate/짧은 블록 예제(dv=3/4, N=7~79) 위주로 NAND급 고rate·장블록 실증 없음, 5비트 min-sum·AWGN 가정, 부호구성이 특정 QC-LDPC 고정된 Prime ECC에 재검증 부담 큼 |
| 추가확인 | 고rate(~0.9)·장블록에서 layered LETS 탐색의 구성 시간과 도달 가능 lifting degree, NAND RBER/양자화 채널에서 error-floor 이득 유지 여부 |

> 총평: 부호설계(H-matrix 구성)로 error-floor를 낮추는 순수 code-design 논문으로 정정능력에 직접 기여(대상 both)하나, Prime ECC의 QC-LDPC가 고정 rate로 이미 확정되어 있어 이식은 부호 재설계·재검증을 수반한다.

### B. 알고리즘 요약

1. 대상: fully-connected base graph를 cyclic N-lifting한 protograph 기반 binary QC-LDPC (regular, `dv=3~5`, rate 2/5~1/2 예시).
2. 문제: error-floor를 낮추려면 dominant trapping set(특히 LETS) 제거가 핵심인데, 기존 `dpl` 완전탐색은 구성 과정에서 수백~수천 회 반복하기엔 너무 복잡.
3. 핵심 관찰: QC 구조가 일부 ETS를 원천 배제 -- ETS의 normal graph `Ĝ(S)`가 `m`-edge colorable이어야 존재 가능(`χ(Ĝ(S))>m`이면 불가), Proposition 2로 홀수 `a`·`b<min(a,dv)` ETS 배제.
4. 핵심 기법 1단: 제거 목표 collection `L` 중 다른 구조의 child가 아닌 최소 집합 `Lt`만 표적화(부모 제거로 자식 자동 제거) -> 예 r4에서 `|Lt|=74` vs `|L|=392`.
5. 식 의미: 부모 클래스 관계 `(a-1,b+2m-dv)`(dot) / `(a-m,b+2-m(dv-2))`(pa,lo)로 Lemma 1(작은 `a`->작은 `b`)이 성립, 탐색 우선순위 정렬 근거.
6. 핵심 기법 2단: 가장 큰 `a`부터 backward recursion으로 out-of-range 부모 구조 `Π`를 greedy 선택(직접 자식 최다 구조 우선, 낮은 multiplicity 클래스 우선).
7. 구현 트릭: layered 탐색 -- 작은 `a` 클래스(Layer 1)부터 순차 검사하다 한 개라도 발견하면 즉시 종료(positive), 각 층에서 다음 층 필요 구조만 메모리 유지.
8. 구성 절차: exponent matrix `P`를 leftmost column부터 greedy 배정, girth `g0`·LETS-free 제약 검사, 실패 시 backtrack (Problem (a): 최소 lifting / Problem (b): 고정 N에서 amax 최대화).
9. 결과: 3×5 base, r2(a≤8,b≤3)에서 `N=26` vs 기존 [10] `N=41`; (155,64) Tanner 대비 C2가 (8,2)·(10,2) LETS 완전 제거로 SNR 6dB에서 error-floor 우위; QC-PEG/[9] 대비 dominant TS 전무.
10. 한계: HW 미설계, AWGN·5비트 min-sum 시뮬만, 저rate/짧은 블록 예제(N=7~79) 중심으로 NAND급 고rate 대규모 부호 실증 부재.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| QC-LDPC H-matrix / exponent matrix 구성 | [ecc_top.cpp](../Prime_ECC_3.1_Claude/paper_screening_profile.md) `Load_PCM()` | LETS-free exponent matrix를 base+shift 구조로 로드하는 부호구조 로드부에 대응 |
| trapping-set-free 부호설계 (error-floor 개선) | 대응 없음 | Prime ECC는 특정 고rate QC-LDPC로 부호 고정, base graph/lifting 재설계 지점 부재 (프로파일 §4 "높음" 난이도) |
| LETS 계층 탐색 알고리즘 자체 | 대응 없음 | 부호 설계·검증 툴이며 런타임 디코더/인코더 모듈과 직접 대응 없음 |
| 5비트 min-sum + clipping 복호 | [decoder.cpp](../Prime_ECC_3.1_Claude/paper_screening_profile.md) `LDPC_Decoder()`, `CNU_Update_New_Mag()` | 평가에 쓴 min-sum은 이미 보유 기법이라 신규 이식 대상 아님 |

적용 가치: **중간** -- error-floor를 부호구성으로 낮추는 방향은 NAND ECC에 유의미하나, Prime ECC의 QC-LDPC가 고rate로 고정되어 있어 base graph·lifting degree 재설계와 전면 재검증을 요구하고 예시가 저rate/짧은 블록이라 고rate 이식성이 미검증이다.

### D. JSON 블록

```json
{
  "id": "arxiv:1902.07332v3",
  "title": "Construction of QC LDPC Codes with Low Error Floor by Efficient Systematic Search and Elimination of Trapping Sets",
  "year": 2019,
  "venue": "arXiv cs.IT (submitted to IEEE Trans. Communications)",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "both",
  "code_type": "QC-LDPC",
  "code_rate": "0.4~0.5",
  "code_length": "145~2133",
  "soft_quant": "soft-2~3bit",
  "key_contribution": "QC 구조가 배제하는 LETS를 edge-coloring으로 규명하고, parent/child 기반 계층적 backward 탐색으로 목표 trapping set만 제거해 짧은 블록길이로 낮은 error-floor 달성",
  "hw_designed": "X",
  "verification": "시뮬",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "O",
  "improve_region": "error-floor",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "중",
  "caveat": "저rate/짧은 블록 예제(dv=3/4, N=7~79) 위주로 NAND급 고rate·장블록 실증 없음, 5비트 min-sum·AWGN 가정, 부호구성이 특정 QC-LDPC 고정된 Prime ECC에 재검증 부담 큼",
  "todo_check": "고rate(~0.9)·장블록에서 layered LETS 탐색의 구성 시간과 도달 가능 lifting degree, NAND RBER/양자화 채널에서 error-floor 이득 유지 여부"
}
```
