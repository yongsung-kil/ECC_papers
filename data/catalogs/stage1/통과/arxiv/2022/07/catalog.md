# arXiv — 2022-07 (1차선별 통과)


## High-throughput decoder of quasi-cyclic LDPC codes with limited precision for continuous-variable quantum key distribution systems

- **Status**: ✅
- **Reason**: FPGA QC-LDPC 디코더 + 제한 정밀도 residual bit error correction — 이식 가능 HW/디코더(D), 바이너리 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:2207.01860v1
- **Type**: preprint
- **Published**: 2022-07-05
- **Authors**: Chuang Zhou, Yang Li, Li Ma +7
- **PDF**: https://arxiv.org/pdf/2207.01860v1
- **Abstract**: More than Mbps secret key rate was demonstrated for continuous-variable quantum key distribution (CV-QKD) systems, but real-time postprocessing is not allowed, which is restricted by the throughput of the error correction decoding in postprocessing. In this paper, a high-throughput FPGA-based quasi-cyclic LDPC decoder is proposed and implemented to support Mbps real-time secret key rate generation for CV-QKD for the first time. A residual bit error correction algorithm is used to solve the problem of high frame errors rate (FER) caused by the limited precision of the decoder. Specifically, real-time high-speed decoding for CV-QKD systems with typical code rates 0.2 and 0.1 is implemented on a commercial FPGA, and two throughputs of 360.92Mbps and 194.65Mbps are achieved, respectively, which can support 17.97 Mbps and 2.48 Mbps real-time generation of secret key rates under typical transmission distances of 25km and 50km, correspondingly. The proposed method paves the way for high-rate real-time CV-QKD deployment in secure metropolitan area network.
