# arXiv — 2011-05 (1차선별 통과)


## A Flexible LDPC code decoder with a Network on Chip as underlying interconnect architecture

- **Status**: ✅
- **Reason**: NoC 기반 유연 LDPC 디코더 VLSI 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1105.2624v1
- **Type**: preprint
- **Published**: 2011-05-13
- **Authors**: Carlo Condo, Guido Masera
- **PDF**: https://arxiv.org/pdf/1105.2624v1
- **Abstract**: LDPC (Low Density Parity Check) codes are among the most powerful and widely adopted modern error correcting codes. The iterative decoding algorithms required for these codes involve high computational complexity and high processing throughput is achieved by allocating a sufficient number of processing elements (PEs). Supporting multiple heterogeneous LDPC codes on a parallel decoder poses serious problems in the design of the interconnect structure for such PEs. The aim of this work is to explore the feasibility of NoC (Network on Chip) based decoders, where full flexibility in terms of supported LDPC codes is obtained resorting to an NoC to connect PEs. NoC based LDPC decoders have been previously considered unfeasible because of the cost overhead associated to packet management and routing. On the contrary, the designed NoC adopts a low complexity routing, which introduces a very limited cost overhead with respect to architectures dedicated to specific classes of codes. Moreover the paper proposes an efficient configuration technique, which allows for fast on--the--fly switching among different codes. The decoder architecture is scalable and VLSI synthesis results are presented for several cases of study, including the whole set of WiMAX LDPC codes, WiFi codes and DVB-S2 standard.
