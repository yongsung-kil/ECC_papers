# arXiv — 2013-01 (1차선별 통과)


## Linear Programming Decoding of Spatially Coupled Codes

- **Status**: ✅
- **Reason**: spatially coupled 코드의 LP 디코딩 — dual witness·hyperflow 분석은 바이너리 LDPC LP 디코더 분석/설계(C/E)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1301.6410v2
- **Type**: preprint
- **Published**: 2013-01-27
- **Authors**: Louay Bazzi, Badih Ghazi, Rudiger Urbanke
- **PDF**: https://arxiv.org/pdf/1301.6410v2
- **Abstract**: For a given family of spatially coupled codes, we prove that the LP threshold on the BSC of the graph cover ensemble is the same as the LP threshold on the BSC of the derived spatially coupled ensemble. This result is in contrast with the fact that the BP threshold of the derived spatially coupled ensemble is believed to be larger than the BP threshold of the graph cover ensemble as noted by the work of Kudekar et al. (2011, 2012). To prove this, we establish some properties related to the dual witness for LP decoding which was introduced by Feldman et al. (2007) and simplified by Daskalakis et al. (2008). More precisely, we prove that the existence of a dual witness which was previously known to be sufficient for LP decoding success is also necessary and is equivalent to the existence of certain acyclic hyperflows. We also derive a sublinear (in the block length) upper bound on the weight of any edge in such hyperflows, both for regular LPDC codes and for spatially coupled codes and we prove that the bound is asymptotically tight for regular LDPC codes. Moreover, we show how to trade crossover probability for "LP excess" on all the variable nodes, for any binary linear code.

## A Low-Complexity Encoding of Quasi-Cyclic Codes Based on Galois Fourier Transform

- **Status**: ✅
- **Reason**: QC-LDPC 저복잡도 인코딩(Galois Fourier 변환), rank-deficient 패리티검사 적용 — 바이너리 QC-LDPC 인코딩 설계(E)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1301.3220v1
- **Type**: preprint
- **Published**: 2013-01-15
- **Authors**: Qin Huang, Li Tang, Zulin Wang +2
- **PDF**: https://arxiv.org/pdf/1301.3220v1
- **Abstract**: The encoding complexity of a general (en,ek) quasi-cyclic code is O[(e^2)(n-k)k]. This paper presents a novel low-complexity encoding algorithm for quasi-cyclic (QC) codes based on matrix transformation. First, a message vector is encoded into a transformed codeword in the transform domain. Then, the transmitted codeword is obtained from the transformed codeword by the inverse Galois Fourier transform. For binary QC codes, a simple and fast mapping is required to post-process the transformed codeword such that the transmitted codeword is binary as well. The complexity of our proposed encoding algorithm is O[e(n-k)k] symbol operations for non-binary codes and O[ek(n-k)(log_2 e)] bit operations for binary codes. These complexities are much lower than their traditional counterpart O[(e^2)(n-k)k]. For example, our complexity of encoding a 64-ary (4095,2160) QC code is only 1.59% of that of traditional encoding, and our complexities of encoding the binary (4095, 2160) and (8176, 7154) QC codes are respectively 9.52% and 1.77% of those of traditional encoding. We also study the application of our low-complexity encoding algorithm to one of the most important subclasses of QC codes, namely QC-LDPC codes, especially when their parity-check matrices are rank deficient.
