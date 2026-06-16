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

## 경계 사례 (판단하며 계속 추가)

- **무선/광통신/PON 응용이라도** 디코더 HW·LLR 양자화·코드설계 기법이 명확히 떼어내 이식 가능하면 → in (응용은 껍데기, 기법이 본질). 예: PON 저비트폭 디코더(11159213), SCMA PLDPC 코드설계(11096949), MIMO LLR Gaussianity 분석(11464434).
- **양자 LDPC(qLDPC)·QKD는 제외 카테고리지만**, 본문이 고전 LDPC로 역이식 가능한 디코더 알고리즘(min-sum/OSD/BP 변형·soft-syndrome)을 제시하면 → in (이식성 > 양자 제외 원칙). 예: BF-OSD(2605.25777), MBBP-LD(2605.14170), QKD용 QC-LDPC FPGA 디코더(11500286). 순수 양자코드 구성/거리 이론은 out 유지.
- **비-NAND 스토리지(HDD/DNA/ReRAM)라도** 스토리지 ECC 일반(B)·코드설계(E)면 → in, 단 Phase3에서 NAND 적합성 재검토 플래그. 예: HDD 변조+LDPC(11301807), DNA BCH+LDPC(11316539).
- **순수이론 bound라도** girth/error-floor 설계공간 특성화(E)에 무게가 있으면 → in 경계 (nonconstructive여도 살림). 예: SC-LDPC 설계공간(2605.18323).
- **소스-채널 결합(JSCC)·시맨틱 통신·fountain/erasure 코드**는 채널 ECC 디코더로 떼어낼 기법이 없으면 → out (LDPC가 베이스라인·부수 언급에 그침).
