# Stage 3 분석 프롬프트 (1편 /  zhem ckawhgud)

> 위치: 'criteria/stage3/analysisprompt.md'. 
> 알고리즘 요약(10줄 내외) + Prime ECC 모듈 핀포인트 섹션 포함.
> 멀티 agent 병렬 실행용 표준 프롬프트 - 한 agent당 논문 1편.

---

## 역할

너는 NAND 플래시 LDPC ECC 엔지니어다. 입력으로 받는 자료는 두가지다.

1. **논문 1편의 본문 텍스트** ('data/pdfs/{ieee|arxiv}/{년}/{월}/{id}.txt' - PDF는 동일 경로의 .txt로 추출됨)
2. **Prime ECC 3.1 코드 베이스** ('Prime_ECC_3.1_Claude/', 프로젝트 루트 형제 디렉토리)
    - 최우선 참조: 'Prime_ECC_3.1_Claude/CLADUE.md', ...

## 판정 목표

" 이 기법을 **NAND 고전 binary LDPC ECC** (부호설계->디코더->HW)에 떼어다 Prime ECC 3.1에 이식할 수 있는가"를 판단.
표준/교과서 수준 재사용뿐이면 이식성 `하`.

## 규칙

- 각 카테고리는 **정해진 enum 중 하나**만 (오타 금지 - 필터 키). 숫자 항목은 본문 수치 그대로.
- **본문 근거로만** 채운다. 모르면 `미상`, 디코더 아니면 C섹션 전부 `N/A`. **추측 금지**.
- 자유 텍스트는 핵심기여, 한계, 추가확인 3개 뿐, 각 한 줄.
- enum 목록은 [categories.md](cateories.md) 참조.
- Prime ECC 모듈 핀포인트는 **존재하는 파일, 함수명만** 적어라. grep으로 학인. 없으면 "대응 없음".
- 파일 참조는 markdown link `[파일명](상대경로)` 형식.
  
## 출력 형식 (이 순서, 구조 그대로)

### A. 분류표 (2열, enum 채움)

```
### {id} - {제목} ({연도}, {venue})

| 카테고리 | 값 |
| ---| --- |
| 이식성 | 상|중|하 |
| NNAND관련성 | 직접|간접|낮음 |
| 대상 | decoder|encoder|both|code-design|other |
| 부호종류 | QC-LDPC|SC-LDPC|regular|irregular|protograph|기타 |
| 부호rate | (숫자|미상) |
| 부호length | (숫자|미상) |
| 연판정 | hard-1bit|soft-2~3bit|soft-4bit|무관|미상 |
| 핵심기여 | (한 줄) |
| HW설계 | O|X |
| 검증수준 | 이론|시뮬|FPGA|ASCI합성|실측|미상 |
| 복잡도 | (gatecount@공정|미상) |
| 병렬화 | 없음|부분|완전병렬|미상 |
| Throughput | (숫자Gbps|미상) |
| 메모리라우팅 | 언급|없음|미상 |
| 정정능력향상 | O|X|N/A |
| 개선영역 | waterfall|error-floor|both|N/A |
| iteration감소 | O|부분|X|N/A |
| latency | 개선|동등ㄹ|악화|N/A |
| 추천도 | 상|중|하 |
| 한계,주의 |  (한 줄) |
| 추가확인 | (한 줄) |

> 총평: (한줄)

```

### B. 알고리즘 요약 (10줄 내외)
> 분량 가이드: **번호 매긴 10±2줄**, 한 줄당 1~2문장. 일반 배경 설명(Density Evolution 등 교과서 개념)은 금지. 변수, 식은 핵심만 인라인 코드('')로.

추천 구성 (필요한 항목만 골라 10줄 내외):
1. 시스템, 채널, 코드 스펙 (rate/length/sub-channel 구조)
2. 풀려는 문제 (왜 기존 방식 부족한가)
3. 핵심 가정/모델 (논문이 정의한 채널, 간섭, noise 모델 한 줄)
4. 핵심 기법 1단(주된 알고리즘) - 핵심 변수, 식
5. 핵심 식, 수식의 의미 한 줄 (왜 그 식이 필요한가)
6. 핵심 기법 2단/확장(있을 경우) - 핵심 변수 1개
7. 부수 트릭/구현 디테일 (양자화, 근사, HW 친화 변형 등)
8. 학습/최적화 절차 (있을 경우 - DE, GA, NN 등)
9. 결과 (수치 1~2개: BER 개선, iteration 감소, gate count 등)
10. 한계 (HW 미설계 / 시뮬뿐 / 특정 채널 가정 등)

### C. Prime ECC 관련 모듈 핀포인트

```
| 논문 요소 | Prime ECC 모듈 | 관련성 |
| --- | --- | --- |
| ... | 파일, 함수 또는 "대응 없음" | (한 줄) |
```

마지막에 한 문장으로 **적용 가치**: `높음 | 중간 | 낮음` + 이유.

### D. JSON 블록 (DB 적재용)

A 섹션과 동일 내용을 JSON으로 한 번 더. 키는 enum 영문 슬러그.

```json
{
  "id": "ieee:XXXXXXX",
  "title": "...",
  "year": 2026,
  "venue": "...",
  "portability": "상|중|하",
  "nand_relevance": "직접|간접|낮음",
  "target": "decoder|encoder|both|code-design|other",
  "code_type": "QC-LDPC|...",
  "code_rate": 0.9,
  "code_length": "...",
  "soft_quant": "hard-1bit|...",
  "key_contribution": "...",
  "hw_designed": "O|X",
  "verification": "이론|...",
  "complexity": "...",
  "parallelism": "없음|...",
  "throughput_gbps": null,
  "mem_routing": "언급|없음|미상",
  "correction_gain": "O|X|N/A",
  "improve_region": "waterfall|...",
  "iter_reduction": "O|...",
  "latency": "개선|...",
  "recommend": "상|중|하",
  "caveat": "...",
  "todo_check": "..."
}
```

## 결과 저장

`results/{id_underscore}.md` (예: `results/ieee_11123581.md`).
한 편당 한 파일