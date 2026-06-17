# arXiv — 2021-02


## A High-Throughput Multi-Mode LDPC Decoder for 5G NR

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2102.13228v2
- **Type**: preprint
- **Published**: 2021-02-25
- **Authors**: Sina Pourjabar, Gwan S. Choi
- **PDF**: https://arxiv.org/pdf/2102.13228v2
- **Abstract**: This paper presents a partially parallel low-density parity-check (LDPC) decoder designed for the 5G New Radio (NR) standard. The design is using a multi-block parallel architecture with a flooding schedule. The decoder can support any code rates and code lengths up to the lifting size Zmax= 96. To compensate for the dropped throughput associated with the smaller Z values, the design can double and quadruple its parallelism when lifting sizes Z<= 48 and Z<= 24 are selected respectively. Therefore, the decoder can process up to eight frames and restore the throughput to the maximum. To simplify the design's architecture, a new variable node for decoding the extended parity bits present in the lower code rates is proposed. The FPGA implementation of the decoder results in a throughput of 2.1 Gbps decoding the 11/12 code rate. Additionally, the synthesized decoder using the 28 nm TSMC technology, achieves a maximum clock frequency of 526 MHz and a throughput of 13.46 Gbps. The core decoder occupies 1.03 mm2, and the power consumption is 229 mW.

## On Quantum Weight Reduction

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2102.10030v3
- **Type**: preprint
- **Published**: 2021-02-19
- **Authors**: M. B. Hastings
- **PDF**: https://arxiv.org/pdf/2102.10030v3
- **Abstract**: We give a general procedure for weight reducing quantum codes. This corrects a previous work\cite{owr}, and introduces a new technique that we call "coning" to effectively induce high weight stabilizers in an LDPC code. As one application, any LDPC code (with arbitrary $O(1)$ stabilizer weights) may be turned into a code where all stabilizers have weight at most $5$ at the cost of at most a constant factor increase in number of physical qubits and constant factor reduction in distance. Also, by applying this technique to a quantum code whose $X$-stabilizers are derived from a classical log-weight random code and whose $Z$-stabilizers have linear weight, we construct an LDPC quantum code with distance $\tilde Ω(N^{2/3})$ and $\tildeΩ(N^{2/3})$ logical qubits.

## Capacity Optimality of AMP in Coded Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2102.05441v2
- **Type**: preprint
- **Published**: 2021-02-10
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://arxiv.org/pdf/2102.05441v2
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the approximate message passing (AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of AMP is analyzed. We prove that AMP achieves the constrained capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. We provide related numerical results of binary signaling using irregular low-density parity-check (LDPC) codes. We show that the optimized codes demonstrate significantly better performance over un-matched ones under AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Proximal Decoding for LDPC-coded Massive MIMO Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2102.05256v1
- **Type**: preprint
- **Published**: 2021-02-10
- **Authors**: Tadashi Wadayama, Satoshi Takabe
- **PDF**: https://arxiv.org/pdf/2102.05256v1
- **Abstract**: We propose a novel optimization-based decoding algorithm for LDPC-coded massive MIMO channels. The proposed decoding algorithm is based on a proximal gradient method for solving an approximate maximum a posteriori (MAP) decoding problem. The key idea is the use of a code-constraint polynomial penalizing a vector far from a codeword as a regularizer in the approximate MAP objective function. The code proximal operator is naturally derived from code-constraint polynomials. The proposed algorithm, called proximal decoding, can be described by a simple recursion consisting of the gradient descent step for a negative log-likelihood function and the code proximal operation. Several numerical experiments show that the proposed algorithm outperforms known massive MIMO detection algorithms, such as an MMSE detector with belief propagation decoding.

## Encoding and Decoding Construction D' Lattices for Power-Constrained Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2102.04741v1
- **Type**: preprint
- **Published**: 2021-02-09
- **Authors**: Fan Zhou, Arini Fitri, Khoirul Anwar +1
- **PDF**: https://arxiv.org/pdf/2102.04741v1
- **Abstract**: This paper focuses on the encoding and decoding of Construction D' coding lattices that can be used with shaping lattices for power-constrained channels. Two encoding methods and a decoding algorithm for Construction D' lattices are given. A design of quasi-cyclic low-density parity-check (QC-LDPC) codes to form Construction D' lattices is presented. This allows construction of nested lattice codes which are good for coding, good for shaping, and have low complexity encoding and decoding. Numerical results of using $E_8$, $BW_{16}$ and Leech lattices for shaping a Construction D' lattice indicate that the shaping gains 0.65 dB, 0.86 dB and 1.03 dB are preserved, respectively.
