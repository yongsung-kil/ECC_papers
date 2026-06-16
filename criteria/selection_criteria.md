# 1차 선별 기준 (Selection Criteria)

논문이 **NAND 플래시 LDPC ECC에 활용 가능한가**를 초록만 보고 **포함(in) / 제외(out)** 이분법으로 판정한다.

## 대원칙

"NAND에 직접 쓰인 논문"이 아니어도 **기법을 떼어내 NAND LDPC ECC
(부호 설계 → 디코더 알고리즘 → HW 구현)에 이식할 수 있으면 포함**한다.
응용 도메인(무선·통신·우주·양자 등)이 NAND가 아니어도, 이식 가능한
디코더·HW·코드설계 기법이 있으면 포함.

## 포함 (in)

- **A. NAND/SSD/플래시 직접** — read-retry, LLR 양자화, retention, 3D TLC/QLC, 컨트롤러
- **B. 스토리지 ECC 일반** — 디스크/erasure, storage용 비이진 LDPC
- **C. 이식 가능 디코더 알고리즘** — min-sum 변형, BP 개선, OSD, 신경망 디코더
- **D. 이식 가능 HW 아키텍처** — FPGA/VLSI 디코더, 병렬화, permutation network
- **E. 이식 가능 코드 설계** — QC/SC-LDPC 구성, girth·사이클 제거, error floor, 유한길이, 비이진

## 제외 (out)

- 양자 LDPC(qLDPC)·양자 EC, QKD·보안
- 소스 코딩 (압축·양자화, 예: BEQ) — 채널코딩 ECC가 아님
- 무선/통신 응용 특이적 — LDPC가 부수 언급, 떼어낼 기법 없음
- 순수 이론 bound — 디코더/HW/구성으로 안 이어짐
- 소스-채널 결합(JSCC)·fountain/erasure·시맨틱 통신 — LDPC가 베이스라인, 떼어낼 ECC 기법 없음

> 양자·무선 논문이라도 **디코더 알고리즘·HW가 명확히 이식 가능**하면 포함(C/D).

## 판단 절차

1. 초록에서 **떼어낼 수 있는 기법**(디코더/HW/코드설계)을 먼저 찾는다 → 있으면 **포함**(C/D/E).
2. 없고 NAND/스토리지 직접이면 **포함**(A/B).
3. 둘 다 아니면 **제외**.
4. **애매하면 포함**으로 살리고 `reason`에 근거를 남긴다 (Phase 3에서 재검토).

## 출력 형식

```json
[{"id": "...", "decision": "in|out", "reason": "한 줄 근거"}]
```
