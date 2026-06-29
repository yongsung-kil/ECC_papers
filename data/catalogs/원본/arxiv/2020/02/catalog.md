# arXiv — 2020-02


## LDPC codes constructed from cubic symmetric graphs

- **Status**: ❌
- **Reason**: 큐빅 대칭 그래프 기반 (3,3)-정규 바이너리 LDPC 구성이나 girth>4 정도의 교과서 수준 구성/이론(파라미터·최소거리 bound)에 그침, NAND에 새로 이식할 디코더·HW·구성 기여 없음
- **ID**: arxiv:2002.06690v1
- **Type**: preprint
- **Published**: 2020-02-16
- **Authors**: Dean Crnkovic, Sanja Rukavina, Marina Simac
- **PDF**: https://arxiv.org/pdf/2002.06690v1
- **Abstract**: Low-density parity-check (LDPC) codes have been the subject of much interest due to the fact that they can perform near the Shannon limit. In this paper we present a construction of LDPC codes from cubic symmetric graphs. The constructed codes are $(3,3)$-regular and the vast majority of the corresponding Tanner graphs have girth greater than four. We analyse properties of the obtained codes and present bounds for the code parameters, the dimension and the minimum distance. Furthermore, we give an expression for the variance of the syndrome weight of the constructed codes. Information on the LDPC codes constructed from bipartite cubic symmetric graphs with less than 200 vertices is presented as well. Some of the constructed codes are optimal, and some have an additional property of being self-orthogonal or linear codes with complementary dual (LCD codes).

## Toward Efficient Quantum Key Distribution Reconciliation

- **Status**: ❌
- **Reason**: QKD 정보조정(reconciliation)에 Turbo 부호 사용, 비-LDPC이고 채널 ECC 아님, 떼어낼 LDPC 디코더 기법 없음
- **ID**: arxiv:2002.04887v1
- **Type**: preprint
- **Published**: 2020-02-12
- **Authors**: Nedra Benletaief, Houria Rezig, Ammar Bouallegue
- **PDF**: https://arxiv.org/pdf/2002.04887v1
- **Abstract**: In this paper, we propose how to construct a reconciliation method for the BB84 Quantum Key Distribution (QKD) protocol. Theoretically, it is unconditionally secure because it is based on the quantum laws of physics, rather than the assumed computational complexity of mathematical problems. BB84 protocol performances can be reduced by various errors and information leakages such as limited intrinsic efficiency of the protocol, imperfect devices and eavesdropping. The proposed reconciliation method allowed to weed out these errors by using Turbo codes. Since their high error correction capability implies getting low errors, this method has high performance especially when compared to the last method presented in the literature based on Low- Density Parity Check codes (LDPC). In particular, we demonstrate that our method leads to a significant improvement of the protocol security and of the Bit Error Rate (BER) even with great eavesdropping capability.

## Protograph-Based Decoding of LDPC Codes with Hamming Weight Amplifiers

- **Status**: ✅
- **Reason**: 프로토그래프 기반 MP 디코딩 + 터보형 메시지교환 디코더, ternary message passing/DE 분석 — 바이너리 LDPC BP에 이식 가능한 디코더 기법(C)
- **ID**: arxiv:2002.02696v1
- **Type**: preprint
- **Published**: 2020-02-07
- **Authors**: Hannes Bartz, Emna Ben Yacoub, Lorenza Bertarelli +1
- **PDF**: https://arxiv.org/pdf/2002.02696v1
- **Abstract**: A new protograph-based framework for message passing (MP) decoding of low density parity-check (LDPC) codes with Hamming weight amplifiers (HWAs), which are used e.g. in the NIST post-quantum crypto candidate LEDAcrypt, is proposed. The scheme exploits the correlations in the error patterns introduced by the HWA using a turbo-like decoding approach where messages between the decoders for the outer code given by the HWA and the inner LDPC code are exchanged. Decoding thresholds for the proposed scheme are computed using density evolution (DE) analysis for belief propagation (BP) and ternary message passing (TMP) decoding and compared to existing decoding approaches. The proposed scheme improves upon the basic approach of decoding LDPC code from the amplified error and has a similar performance as decoding the corresponding moderate-density parity-check (MDPC) code but with a significantly lower computational complexity.
