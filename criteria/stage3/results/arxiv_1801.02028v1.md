### arxiv:1801.02028v1 - Characterization and Efficient Search of Non-Elementary Trapping Sets of LDPC Codes with Applications to Stopping Sets (2018, arXiv cs.IT)

| 카테고리 | 값 |
|---|---|
| 이식성 | 중 |
| NAND관련성 | 간접 |
| 대상 | code-design |
| 부호종류 | 기타 |
| 부호rate | 0.23~0.88 |
| 부호length | 128~16383 |
| 연판정 | 무관 |
| 핵심기여 | ETS에서 dot 확장으로 NETS를 계층적 특성화·완전탐색하고, 이를 stopping distance smin 상·하한 도출에 적용 |
| HW설계 | X |
| 검증수준 | 이론 |
| 복잡도 | 미상 |
| 병렬화 | 미상 |
| Throughput | 미상 |
| 메모리라우팅 | 없음 |
| 정정능력향상 | N/A |
| 개선영역 | N/A |
| iteration감소 | N/A |
| latency | N/A |
| 추천도 | 중 |
| 한계,주의 | 순수 구조 탐색·이론 도구(MATLAB), 디코더/HW 없음·error-floor를 직접 개선하지 않고 진단·분석만 |
| 추가확인 | dv≥3 변수정규 위주로 유도됨(불규칙은 비완전탐색), 우리 고rate QC-LDPC의 dv·girth에서 탐색 복잡도·완전성 범위(amax) 확인 |

> 총평: NETS/stopping-set을 빠르게 완전열거하고 smin 상·하한을 주는 구조 분석 도구. 부호를 고치진 않으나 우리 H-matrix의 error-floor 취약구조 진단·검증에 쓸 수 있는 오프라인 툴 가치.

### B. 알고리즘 요약

1. 대상: 임의 binary LDPC(변수정규·불규칙), Tanner graph 구조 분석. AWGN/BSC의 error-floor는 trapping set(TS), BEC은 stopping set(SS)이 주범.
2. 문제: 기존 branch-&-bound류 완전탐색은 짧은 block length(<1008), 작은 TS에만 가능. NETS(비초등 TS) 완전탐색 도구가 사실상 없음.
3. 핵심 정의: `(a,b) TS`는 크기 `a`, unsatisfied check `b`. ETS=degree 1/2 check만, NETS=degree≥3 check 포함. LETS=leaf 없는 ETS. SS=degree-1 check 없는 TS.
4. 핵심 기법 1: NETS를 "ETS에서 시작해 `dotm`(depth-one tree) 확장을 한 변수노드씩 반복 적용해 도달하는 임베디드 그래프 계열"로 특성화(Lemma 3, Prop.1~5).
5. 의미: 이미 존재하는 효율적 ETS/LETS 탐색기([7],[8])의 출력을 입력으로 재사용 → dot 확장만으로 NETS까지 저복잡도로 확장 탐색.
6. 핵심 기법 2: degree-3 check 개수 f에 따라 `N3,N3,3,...`, `N4,N4,3` 부류로 제한하고, `amax`(Table II)까지 완전탐색 보장 범위를 이론적으로 확정(Theorem 2).
7. 구현 디테일: Algorithm 1(NETS 탐색), Algorithm 2(smin 하한 LSS3), Algorithm 3(비완전 dot/path/lollipop 확장으로 smin 상한), MATLAB 구현.
8. SS 응용: ESS=b=0 LETS, NESS=NETS의 부분집합. Prop.6/7로 하한 LSS1<LSS2, 완전탐색으로 정확 smin 또는 LSS3 하한, 비완전 탐색으로 상한.
9. 결과: rate 0.23~0.88, length 128~16383의 20 정규·8 불규칙 부호에 적용. 정확 smin/상하한을 수초~수십분에 도출(예: [10]의 600~3085시간을 5~34분으로 단축), 고rate 대형부호(C9: rate 0.87, n=16383)도 처리.
10. 한계: 순수 분석/탐색 도구(디코더·HW 없음), 완전탐색 보장은 변수정규 dv=3~6·g=6~10 범위, 불규칙 부호는 비완전 탐색만.

### C. Prime ECC 관련 모듈 핀포인트

| 논문 요소 | Prime ECC 모듈 | 관련성 |
|---|---|---|
| TS/SS 구조 탐색 대상 H-matrix | [ecc_top.cpp](criteria/stage3/Prime_ECC_3.1_Claude/) `Load_PCM()` | 우리 QC-LDPC H(`PCM_b`)를 입력으로 오프라인 error-floor 취약구조 진단 가능 |
| error-floor 원인 구조(NETS/NESS) 분석 | [decoder.cpp](criteria/stage3/Prime_ECC_3.1_Claude/) `LDPC_Decoder()` (간접) | 탐색 결과로 수렴실패 원인 해석, 단 알고리즘 자체는 디코더에 삽입 안 됨 |
| 수렴실패 추적 대조 | [corner.cpp](criteria/stage3/Prime_ECC_3.1_Claude/) | 우리 corner/수렴실패 케이스와 TS 목록 상호 대조 가능 |
| dot/path/lollipop 탐색 알고리즘 자체 | 대응 없음 | 부호설계·검증용 외부 MATLAB 툴, 런타임 디코더 경로엔 대응 모듈 없음 |

적용 가치: **중간** — 부호를 직접 개선하지 않는 오프라인 구조분석 도구지만, 우리 고rate QC-LDPC H-matrix의 stopping/trapping set·smin을 빠르게 검증해 error-floor 리스크를 사전 진단하는 데 활용 가치가 있음.

### D. JSON 블록

```json
{
  "id": "arxiv:1801.02028v1",
  "title": "Characterization and Efficient Search of Non-Elementary Trapping Sets of LDPC Codes with Applications to Stopping Sets",
  "year": 2018,
  "venue": "arXiv cs.IT",
  "portability": "중",
  "nand_relevance": "간접",
  "target": "code-design",
  "code_type": "기타",
  "code_rate": null,
  "code_length": "128~16383",
  "soft_quant": "무관",
  "key_contribution": "ETS에서 dot 확장으로 NETS를 계층적 특성화·완전탐색하고 stopping distance smin 상·하한 도출에 적용",
  "hw_designed": "X",
  "verification": "이론",
  "complexity": "미상",
  "parallelism": "미상",
  "throughput_gbps": null,
  "mem_routing": "없음",
  "correction_gain": "N/A",
  "improve_region": "N/A",
  "iter_reduction": "N/A",
  "latency": "N/A",
  "recommend": "중",
  "caveat": "순수 구조 탐색·이론 도구(MATLAB), 디코더/HW 없음·error-floor를 직접 개선하지 않고 진단만",
  "todo_check": "변수정규 dv≥3 위주 유도(불규칙은 비완전), 우리 고rate QC-LDPC dv·girth에서 완전탐색 범위(amax) 확인"
}
```
