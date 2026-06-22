# arXiv — 2012-02 (1차선별 통과)


## Selecting Two-Bit Bit Flipping Algorithms for Collective Error Correction

- **Status**: ✅
- **Reason**: two-bit bit flipping 알고리즘 집합 선택으로 low error floor, BSC 바이너리 LDPC 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1202.1348v2
- **Type**: preprint
- **Published**: 2012-02-07
- **Authors**: Dung Viet Nguyen, Bane Vasic, Michael W. Marcellin
- **PDF**: https://arxiv.org/pdf/1202.1348v2
- **Abstract**: A class of two-bit bit flipping algorithms for decoding low-density parity-check codes over the binary symmetric channel was proposed in [1]. Initial results showed that decoders which employ a group of these algorithms operating in parallel can offer low error floor decoding for high-speed applications. As the number of two-bit bit flipping algorithms is large, designing such a decoder is not a trivial task. In this paper, we describe a procedure to select collections of algorithms that work well together. This procedure relies on a recursive process which enumerates error configurations that are uncorrectable by a given algorithm. The error configurations uncorrectable by a given algorithm form its trapping set profile. Based on their trapping set profiles, algorithms are selected so that in parallel, they can correct a fixed number of errors with high probability.

## Enhancing the Error Correction of Finite Alphabet Iterative Decoders via Adaptive Decimation

- **Status**: ✅
- **Reason**: FAID(finite alphabet iterative decoder)에 적응적 decimation으로 error floor 개선 — 이식 가능한 바이너리 LDPC 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1202.1337v2
- **Type**: preprint
- **Published**: 2012-02-07
- **Authors**: Shiva Kumar Planjery, Bane Vasic, David Declercq
- **PDF**: https://arxiv.org/pdf/1202.1337v2
- **Abstract**: Finite alphabet iterative decoders (FAIDs) for LDPC codes were recently shown to be capable of surpassing the Belief Propagation (BP) decoder in the error floor region on the Binary Symmetric channel (BSC). More recently, the technique of decimation which involves fixing the values of certain bits during decoding, was proposed for FAIDs in order to make them more amenable to analysis while maintaining their good performance. In this paper, we show how decimation can be used adaptively to further enhance the guaranteed error correction capability of FAIDs that are already good on a given code. The new adaptive decimation scheme proposed has marginally added complexity but can significantly improve the slope of the error floor performance of a particular FAID. We describe the adaptive decimation scheme particularly for 7-level FAIDs which propagate only 3-bit messages and provide numerical results for column-weight three codes. Analysis suggests that the failures of the new decoders are linked to stopping sets of the code.

## Mutual-Information Optimized Quantization for LDPC Decoding of Accurately Modeled Flash Data

- **Status**: ✅
- **Reason**: NAND MLC 플래시 LDPC 디코딩용 MMI 양자화·다중리드 word-line 전압 최적화 — A/C 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1202.1325v1
- **Type**: preprint
- **Published**: 2012-02-07
- **Authors**: Jiadong Wang, Guiqiang Dong, Tong Zhang +1
- **PDF**: https://arxiv.org/pdf/1202.1325v1
- **Abstract**: High-capacity NAND flash memories use multi-level cells (MLCs) to store multiple bits per cell and achieve high storage densities. Higher densities cause increased raw bit error rates (BERs), which demand powerful error correcting codes. Low-density parity-check (LDPC) codes are a well-known class of capacity-approaching codes in AWGN channels. However, LDPC codes traditionally use soft information while the flash read channel provides only hard information. Low resolution soft information may be obtained by performing multiple reads per cell with distinct word-line voltages.   We select the values of these word-line voltages to maximize the mutual information between the input and output of the equivalent multiple-read channel under any specified noise model. Our results show that maximum mutual-information (MMI) quantization provides better soft information for LDPC decoding given the quantization level than the constant-pdf-ratio quantization approach. We also show that adjusting the LDPC code degree distribution for the quantized setting provides a significant performance improvement.

## A Non-Disjoint Group Shuffled Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: 비분리 그룹 셔플드 BP 스케줄링으로 수렴 가속 — 이식 가능한 바이너리 LDPC 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1202.1060v1
- **Type**: preprint
- **Published**: 2012-02-06
- **Authors**: Yen-Cheng Hsu, Tofar C. -Y. Chang, Yu T. Su +1
- **PDF**: https://arxiv.org/pdf/1202.1060v1
- **Abstract**: To reduce the implementation complexity of a belief propagation (BP) based low-density parity-check (LDPC) decoder, shuffled BP decoding schedules, which serialize the decoding process by dividing a complete parallel message-passing iteration into a sequence of sub-iterations, have been proposed. The so-called group horizontal shuffled BP algorithm partitions the check nodes of the code graph into groups to perform group-by-group message-passing decoding. This paper proposes a new grouping technique to accelerate the message-passing rate. Performance of the proposed algorithm is analyzed by a Gaussian approximation approach. Both analysis and numerical experiments verify that the new algorithm does yield a convergence rate faster than that of existing conventional or group shuffled BP decoder with the same computing complexity constraint.

## Low-Density Arrays of Circulant Matrices: Rank and Row-Redundancy Analysis, and Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: 순환행렬 배열 rank/row-redundancy 분석 기반 신규 QC-LDPC 구성 — 이식 가능한 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1202.0702v1
- **Type**: preprint
- **Published**: 2012-02-03
- **Authors**: Qin Huang, Keke Liu, Zulin Wang
- **PDF**: https://arxiv.org/pdf/1202.0702v1
- **Abstract**: This paper is concerned with general analysis on the rank and row-redundancy of an array of circulants whose null space defines a QC-LDPC code. Based on the Fourier transform and the properties of conjugacy classes and Hadamard products of matrices, we derive tight upper bounds on rank and row-redundancy for general array of circulants, which make it possible to consider row-redundancy in constructions of QC-LDPC codes to achieve better performance. We further investigate the rank of two types of construction of QC-LDPC codes: constructions based on Vandermonde Matrices and Latin Squares and give combinatorial expression of the exact rank in some specific cases, which demonstrates the tightness of the bound we derive. Moreover, several types of new construction of QC-LDPC codes with large row-redundancy are presented and analyzed.
