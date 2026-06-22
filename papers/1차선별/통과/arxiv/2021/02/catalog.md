# arXiv — 2021-02 (1차선별 통과)


## A High-Throughput Multi-Mode LDPC Decoder for 5G NR

- **Status**: ✅
- **Reason**: 5G NR LDPC 부분병렬 디코더 HW(FPGA/28nm), 가변 병렬도·새 변수노드 구조 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:2102.13228v2
- **Type**: preprint
- **Published**: 2021-02-25
- **Authors**: Sina Pourjabar, Gwan S. Choi
- **PDF**: https://arxiv.org/pdf/2102.13228v2
- **Abstract**: This paper presents a partially parallel low-density parity-check (LDPC) decoder designed for the 5G New Radio (NR) standard. The design is using a multi-block parallel architecture with a flooding schedule. The decoder can support any code rates and code lengths up to the lifting size Zmax= 96. To compensate for the dropped throughput associated with the smaller Z values, the design can double and quadruple its parallelism when lifting sizes Z<= 48 and Z<= 24 are selected respectively. Therefore, the decoder can process up to eight frames and restore the throughput to the maximum. To simplify the design's architecture, a new variable node for decoding the extended parity bits present in the lower code rates is proposed. The FPGA implementation of the decoder results in a throughput of 2.1 Gbps decoding the 11/12 code rate. Additionally, the synthesized decoder using the 28 nm TSMC technology, achieves a maximum clock frequency of 526 MHz and a throughput of 13.46 Gbps. The core decoder occupies 1.03 mm2, and the power consumption is 229 mW.

## Proximal Decoding for LDPC-coded Massive MIMO Channels

- **Status**: ✅
- **Reason**: 근접(proximal) 경사 기반 새 LDPC 디코딩 알고리즘 — code proximal operator는 채널 무관, BP 대안 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2102.05256v1
- **Type**: preprint
- **Published**: 2021-02-10
- **Authors**: Tadashi Wadayama, Satoshi Takabe
- **PDF**: https://arxiv.org/pdf/2102.05256v1
- **Abstract**: We propose a novel optimization-based decoding algorithm for LDPC-coded massive MIMO channels. The proposed decoding algorithm is based on a proximal gradient method for solving an approximate maximum a posteriori (MAP) decoding problem. The key idea is the use of a code-constraint polynomial penalizing a vector far from a codeword as a regularizer in the approximate MAP objective function. The code proximal operator is naturally derived from code-constraint polynomials. The proposed algorithm, called proximal decoding, can be described by a simple recursion consisting of the gradient descent step for a negative log-likelihood function and the code proximal operation. Several numerical experiments show that the proposed algorithm outperforms known massive MIMO detection algorithms, such as an MMSE detector with belief propagation decoding.
