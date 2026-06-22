# arXiv — 2018-02 (1차선별 통과)


## Design of Irregular SC-LDPC Codes With Non-Uniform Degree Distributions by Linear Programing

- **Status**: ✅
- **Reason**: 불규칙 SC-LDPC의 비균일 degree distribution을 LP로 설계하는 신규 바이너리 코드설계 기법(E), error floor·유한길이 성능 개선
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1802.07598v2
- **Type**: preprint
- **Published**: 2018-02-21
- **Authors**: Heeyoul Kwak, Jong-Seon No, Hosung Park
- **PDF**: https://arxiv.org/pdf/1802.07598v2
- **Abstract**: In this paper, we propose a new design method of irregular spatially-coupled low-density parity-check (SC-LDPC) codes with non-uniform degree distributions by linear programming (LP). In general, irregular SC-LDPC codes with non-uniform degree distributions is difficult to design with low complexity because their density evolution equations are multi-dimensional. To solve the problem, the proposed method is based on two main ideas: A local design of the degree distributions and pre-computation of the input/output message relationship. These ideas make it possible to design the degree distributions of irregular SC-LDPC codes by solving low complexity LP problems over the binary erasure channel. We also find a proper objective function for the proposed design methodology to improve the performance of SC-LDPC codes. It is shown that the irregular SC-LDPC codes obtained by the proposed method are superior to regular SC-LDPC codes in terms of both asymptotic and finite-length performances.

## Study of Knowledge-Aided Iterative Detection and Decoding for Multiuser MIMO Systems

- **Status**: ✅
- **Reason**: short cycle 지식·하이퍼그래프 reweighting을 활용한 reweighted BP 디코딩 알고리즘으로 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1802.05960v1
- **Type**: preprint
- **Published**: 2018-02-15
- **Authors**: P. Li, R. C. de Lamare, J. Liu
- **PDF**: https://arxiv.org/pdf/1802.05960v1
- **Abstract**: In this work, we consider the problem of reduced latency of low-density parity-check (LDPC) codes with iterative detection and decoding (IDD) receiver in multiuser multiple-antenna systems. The proposed knowledge-aided IDD (KA-IDD) system employs a minimum mean-square error detector with refined iterative processing and a reweighted belief propagation (BP) decoding algorithm. We present reweighted BP decoding algorithms, which exploit the knowledge of short cycles in the graph structure and reweighting factors derived from the expansion of hypergraphs. Simulation results show that the proposed KA-IDD scheme and algorithms outperform prior art and require a reduced number of decoding iterations.

## Polar-Coded Forward Error Correction for MLC NAND Flash Memory Polar FEC for NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND 플래시 직접 ECC 적용, LLR 양자화·sensing·2bit hard-decision 등 NAND 관련 기법 다수(A); polar 위주지만 LDPC 비교·양자화 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1802.04576v1
- **Type**: preprint
- **Published**: 2018-02-13
- **Authors**: Haochuan Song, Frankie Fu, Cloud Zeng +4
- **PDF**: https://arxiv.org/pdf/1802.04576v1
- **Abstract**: With the ever-growing storage density, high-speed, and low-cost data access, flash memory has inevitably become popular. Multi-level cell (MLC) NAND flash memory, which can well balance the data density and memory stability, has occupied the largest market share of flash memory. With the aggressive memory scaling, however, the reliability decays sharply owing to multiple interferences. Therefore, the control system should be embedded with a suitable error correction code (ECC) to guarantee the data integrity and accuracy. We proposed the pre-check scheme which is a multi-strategy polar code scheme to strike a balance between reasonable frame error rate (FER) and decoding latency. Three decoders namely binary-input, quantized-soft, and pure-soft decoders are embedded in this scheme. Since the calculation of soft log-likelihood ratio (LLR) inputs needs multiple sensing operations and optional quantization boundaries, a 2-bit quantized hard-decision decoder is proposed to outperform the hard-decoded LDPC bit-flipping decoder with fewer sensing operations. We notice that polar codes have much lower computational complexity compared to LDPC codes. The stepwise maximum mutual information (SMMI) scheme is also proposed to obtain overlapped boundaries without exhausting search. The mapping scheme using Gray code is employed and proved to achieve better raw error performance compared to other alternatives. Hardware architectures are also given in this paper.
