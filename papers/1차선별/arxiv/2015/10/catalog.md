# arXiv — 2015-10 (1차선별 통과)


## Some problems of Graph Based Codes for Belief Propagation decoding

- **Status**: ✅
- **Reason**: C/E: HW-friendly QC-LDPC의 trapping set/pseudocodeword 측정·BP 디코딩 개선 기법 — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1511.00133v3
- **Type**: preprint
- **Published**: 2015-10-31
- **Authors**: Vasiliy Usatyuk
- **PDF**: https://arxiv.org/pdf/1511.00133v3
- **Abstract**: Short survey about code on the graph by example of hardware friendly quasi-cycle LDPC code. We consider two main properties of code: weight enumerator (well known from classic code theory) and Trapping sets pseudocodewords weight spectrum (a subgraph in code graph's which become reasone of decoding failure under Belief propagation). In paper we show fast methods to measure first components of TS enumerator using EMD=ACE constrains for high girth codes on the graph using graph spectral classification method. This approach simplify solving trouble of agreed between minimal TS pseudocode weight and code distance (which can be measure using knowledge of Authomorphism for algebraic code design methods or measure using lattice reduction(LLL,BKZ) for random graph design methods). In the end of article author raise several challenge problems to improve Sparse and Dense parity-check codes decoding under Belief propagation.

## New Characterization and Efficient Exhaustive Search Algorithm for Elementary Trapping Sets of Variable-Regular LDPC Codes

- **Status**: ✅
- **Reason**: variable-regular 바이너리 LDPC의 elementary trapping set 신규 특성화·탐색 알고리즘 — error floor/코드설계(E)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1510.04954v1
- **Type**: preprint
- **Published**: 2015-10-16
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://arxiv.org/pdf/1510.04954v1
- **Abstract**: In this paper, we propose a new characterization for elementary trapping sets (ETSs) of variable-regular low-density parity-check (LDPC) codes. Recently, Karimi and Banihashemi proposed a characterization of ETSs, which was based on viewing an ETS as a layered superset (LSS) of a short cycle in the code's Tanner graph. A notable advantage of LSS characterization is that it corresponds to a simple LSS-based search algorithm that starts from short cycles of the graph and finds the ETSs with LSS structure efficiently. Compared to the LSS-based characterization of Karimi and Banihashemi, which is based on a single LSS expansion technique, the new characterization involves two additional expansion techniques. The introduction of the new techniques mitigates two problems that LSS-based characterization/search suffers from: (1) exhaustiveness, (2) search efficiency. We prove that using the three expansion techniques, any ETS structure can be obtained starting from a simple cycle, no matter how large the size of the structure $a$ or the number of its unsatisfied check nodes $b$ are. We also demonstrate that for the proposed characterization/search to exhaustively cover all the ETS structures within the $(a,b)$ classes with $a \leq a_{max}, b \leq b_{max}$, for any value of $a_{max}$ and $b_{max}$, the length of the short cycles required to be enumerated is less than that of the LSS-based characterization/search. We also prove that the three expansion techniques, proposed here, are the only expansions needed for characterization of ETS structures starting from simple cycles in the graph, if one requires each and every intermediate sub-structure to be an ETS as well. Extensive simulation results are provided to show that, compared to LSS-based search, significant improvement in search speed and memory requirements can be achieved.

## Density Evolution Analysis of Spatially Coupled LDPC Codes Over BIAWGN Channel

- **Status**: ✅
- **Reason**: SC-LDPC density evolution에 reciprocal channel/Gaussian 근사로 복잡도 저감 신규 기법 — 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1510.04763v1
- **Type**: preprint
- **Published**: 2015-10-16
- **Authors**: Md. Noor-A-Rahim, Gottfried Lechner, Khoa D. Nguyen
- **PDF**: https://arxiv.org/pdf/1510.04763v1
- **Abstract**: In this paper, we study the density evolution analysis of spatially coupled low-density parity-check (SC-LDPC) codes over binary input additive white Gaussian noise (BIAWGN) channels under the belief propagation (BP) decoding algorithm. Using reciprocal channel approximation and Gaussian approximation, we propose averaging techniques for the density evolution of SC-LDPC codes over BIAWGN channels. We show that the proposed techniques can closely predict the decoding threshold while offering reduced complexity compared to the existing multi-edge-type density evolution.

## A Fully-Unrolled LDPC Decoder Based on Quantized Message Passing

- **Status**: ✅
- **Reason**: LUT 기반 finite-alphabet 메시지패싱(min-sum 대체)으로 비트폭 축소 + fully-unrolled HW 아키텍처 — 디코더(C)+HW(D) 핵심 이식 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1510.04589v1
- **Type**: preprint
- **Published**: 2015-10-15
- **Authors**: Alexios Balatsoukas-Stimming, Michael Meidlinger, Reza Ghanaatian +2
- **PDF**: https://arxiv.org/pdf/1510.04589v1
- **Abstract**: In this paper, we propose a finite alphabet message passing algorithm for LDPC codes that replaces the standard min-sum variable node update rule by a mapping based on generic look-up tables. This mapping is designed in a way that maximizes the mutual information between the decoder messages and the codeword bits. We show that our decoder can deliver the same error rate performance as the conventional decoder with a much smaller message bit-width. Finally, we use the proposed algorithm to design a fully unrolled LDPC decoder hardware architecture.
