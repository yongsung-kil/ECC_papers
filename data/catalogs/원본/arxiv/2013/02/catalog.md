# arXiv — 2013-02


## Joint Physical Network Coding and LDPC decoding for Two Way Wireless Relaying

- **Status**: ❌
- **Reason**: 양방향 릴레이용 physical network coding+LDPC 결합 디코딩, 무선응용 특이적이며 떼어낼 순수 ECC 기법 없음
- **ID**: arxiv:1302.4840v1
- **Type**: preprint
- **Published**: 2013-02-20
- **Authors**: Kui Xu, Zhenxing Lv, Youyun Xu +3
- **PDF**: https://arxiv.org/pdf/1302.4840v1
- **Abstract**: In this paper, we investigate the joint design of channel and network coding in bi-directional relaying systems and propose a combined low complexity physical network coding and LDPC decoding scheme. For the same LDPC codes employed at both source nodes, we show that the relay can decodes the network coded codewords from the superimposed signal received from the BPSK-modulated multiple-access channel. Simulation results shown that this novel joint physical network coding and LDPC decoding method outperforms the existing MMSE network coding and LDPC decoding method over AWGN and complex MAC channel.

## Low-power Secret-key Agreement over OFDM

- **Status**: ❌
- **Reason**: OFDM secret-key agreement에서 LDPC를 정보조정(reconciliation)에 사용 — QKD/보안 reconciliation 범주, 떼어낼 신규 디코더·HW 기법 없음
- **ID**: arxiv:1302.4767v1
- **Type**: preprint
- **Published**: 2013-02-19
- **Authors**: Francesco Renna, Nicola Laurenti, Stefano Tomasin +5
- **PDF**: https://arxiv.org/pdf/1302.4767v1
- **Abstract**: Information-theoretic secret-key agreement is perhaps the most practically feasible mechanism that provides unconditional security at the physical layer to date. In this paper, we consider the problem of secret-key agreement by sharing randomness at low power over an orthogonal frequency division multiplexing (OFDM) link, in the presence of an eavesdropper. The low power assumption greatly simplifies the design of the randomness sharing scheme, even in a fading channel scenario. We assess the performance of the proposed system in terms of secrecy key rate and show that a practical approach to key sharing is obtained by using low-density parity check (LDPC) codes for information reconciliation. Numerical results confirm the merits of the proposed approach as a feasible and practical solution. Moreover, the outage formulation allows to implement secret-key agreement even when only statistical knowledge of the eavesdropper channel is available.

## Bilayer Protograph Codes for Half-Duplex Relay Channels

- **Status**: ✅
- **Reason**: half-duplex relay용 protograph 기반 LDPC 코드 설계 — 구조적 설계·낮은 인코딩 복잡도 기법은 바이너리 LDPC 코드설계(E)로 이식 가능
- **ID**: arxiv:1302.4516v1
- **Type**: preprint
- **Published**: 2013-02-19
- **Authors**: Thuy Van Nguyen, Aria Nosratinia, Dariush Divsalar
- **PDF**: https://arxiv.org/pdf/1302.4516v1
- **Abstract**: Despite encouraging advances in the design of relay codes, several important challenges remain. Many of the existing LDPC relay codes are tightly optimized for fixed channel conditions and not easily adapted without extensive re-optimization of the code. Some have high encoding complexity and some need long block lengths to approach capacity. This paper presents a high-performance protograph-based LDPC coding scheme for the half-duplex relay channel that addresses simultaneously several important issues: structured coding that permits easy design, low encoding complexity, embedded structure for convenient adaptation to various channel conditions, and performance close to capacity with a reasonable block length. The application of the coding structure to multi-relay networks is demonstrated. Finally, a simple new methodology for evaluating the end-to-end error performance of relay coding systems is developed and used to highlight the performance of the proposed codes.

## Linked-Cluster Technique for Finding the Distance of a Quantum LDPC Code

- **Status**: ❌
- **Reason**: 양자 LDPC 코드의 거리 계산 기법 — 양자 전용 개념 의존, 고전 바이너리 LDPC 디코더·설계로 이식 불가
- **ID**: arxiv:1302.1845v1
- **Type**: preprint
- **Published**: 2013-02-07
- **Authors**: Alexey A. Kovalev, Ilya Dumer, Leonid P. Pryadko
- **PDF**: https://arxiv.org/pdf/1302.1845v1
- **Abstract**: We present a linked-cluster technique for calculating the distance of a quantum LDPC code. It offers an advantage over existing deterministic techniques for codes with small relative distances (which includes all known families of quantum LDPC codes), and over the probabilistic technique for codes with sufficiently high rates.
