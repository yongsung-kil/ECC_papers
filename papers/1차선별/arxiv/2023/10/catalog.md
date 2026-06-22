# arXiv — 2023-10 (1차선별 통과)


## 4-Cycle Free Spatially Coupled LDPC Codes with an Explicit Construction

- **Status**: ✅
- **Reason**: 4-cycle free SC-LDPC 명시적 구성법 (good sequences) — 바이너리 SC-LDPC 코드 설계·girth 제거 신기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2310.12657v1
- **Type**: preprint
- **Published**: 2023-10-19
- **Authors**: Zeinab Roostaie, Mohammad Gholami, Farzad Parvaresh
- **PDF**: https://arxiv.org/pdf/2310.12657v1
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are a class of capacity approaching LDPC codes with low message recovery latency when a sliding window decoding is used. In this paper, we first present a new method for the construction of a class of SC-LDPC codes by the incidence matrices of a given non-negative integer matrix $E$, and then the relationship of 4-cycles between matrix $E$ and the corresponding SC-LDPC code are investigated. Finally, by defining a new class of integer finite sequences, called {\it good sequences}, for the first time, we give an explicit method for the construction of a class of 4-cycle free SC-LDPC codes that can achieve (in most cases) the minimum coupling width.

## An Efficient Algorithm for Counting Cycles in QC and APM LDPC Codes

- **Status**: ✅
- **Reason**: QC/APM-LDPC Tanner 그래프의 임의 길이 사이클 카운팅 신규 알고리즘 — 바이너리 코드 설계·girth/사이클 분석 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2310.12556v1
- **Type**: preprint
- **Published**: 2023-10-19
- **Authors**: Mohammad Gholami, Zahra Gholami
- **PDF**: https://arxiv.org/pdf/2310.12556v1
- **Abstract**: In this paper, a new method is given for counting cycles in the Tanner graph of a (Type-I) quasi-cyclic (QC) low-density parity-check (LDPC) code which the complexity mainly is dependent on the base matrix, independent from the CPM-size of the constructed code. Interestingly, for large CPM-sizes, in comparison of the existing methods, this algorithm is the first approach which efficiently counts the cycles in the Tanner graphs of QC-LDPC codes. In fact, the algorithm recursively counts the cycles in the parity-check matrix column-by-column by finding all non-isomorph tailless backtrackless closed (TBC) walks in the base graph and enumerating theoretically their corresponding cycles in the same equivalent class. Moreover, this approach can be modified in few steps to find the cycle distributions of a class of LDPC codes based on Affine permutation matrices (APM-LDPC codes). Interestingly, unlike the existing methods which count the cycles up to $2g-2$, where $g$ is the girth, the proposed algorithm can be used to enumerate the cycles of arbitrary length in the Tanner graph. Moreover, the proposed cycle searching algorithm improves upon various previously known methods, in terms of computational complexity and memory requirements.

## Boosting Learning for LDPC Codes to Improve the Error-Floor Performance

- **Status**: ✅
- **Reason**: C/E: neural min-sum 디코더 학습기법으로 표준 LDPC error-floor 제거, 추가 HW 없이 기존 디코더에 통합 가능 — NAND ECC 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2310.07194v2
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Hee-Youl Kwak, Dae-Young Yun, Yongjune Kim +2
- **PDF**: https://arxiv.org/pdf/2310.07194v2
- **Abstract**: Low-density parity-check (LDPC) codes have been successfully commercialized in communication systems due to their strong error correction capabilities and simple decoding process. However, the error-floor phenomenon of LDPC codes, in which the error rate stops decreasing rapidly at a certain level, presents challenges for achieving extremely low error rates and deploying LDPC codes in scenarios demanding ultra-high reliability. In this work, we propose training methods for neural min-sum (NMS) decoders to eliminate the error-floor effect. First, by leveraging the boosting learning technique of ensemble networks, we divide the decoding network into two neural decoders and train the post decoder to be specialized for uncorrected words that the first decoder fails to correct. Secondly, to address the vanishing gradient issue in training, we introduce a block-wise training schedule that locally trains a block of weights while retraining the preceding block. Lastly, we show that assigning different weights to unsatisfied check nodes effectively lowers the error-floor with a minimal number of weights. By applying these training methods to standard LDPC codes, we achieve the best error-floor performance compared to other decoding methods. The proposed NMS decoder, optimized solely through novel training methods without additional modules, can be integrated into existing LDPC decoders without incurring extra hardware costs. The source code is available at https://github.com/ghy1228/LDPC_Error_Floor .

## The impact when neural min-sum variant meets ordered statistics decoding of LDPC codes

- **Status**: ✅
- **Reason**: C: neural min-sum 변형 + OSD 하이브리드 디코더, 저복잡도/고처리율 설계 — 바이너리 LDPC 디코더 기법으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2310.07129v2
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://arxiv.org/pdf/2310.07129v2
- **Abstract**: This paper introduces three key initiatives in the pursuit of a hybrid decoding framework characterized by superior decoding performance, high throughput, low complexity, and independence from channel noise variance.   Firstly, adopting a graphical neural network perspective, we propose a design methodology for a family of neural min-sum variants. Our exploration delves into the frame error rates associated with different decoding variants and the consequential impact of decoding failures on subsequent ordered statistics decoding. Notably, these neural min-sum variants exhibit generally indistinguishable performance, hence the simplest member is chosen as the constituent of the hybrid decoding.   Secondly, to address computational complexities arising from exhaustive searches for authentic error patterns in cases of decoding failure, two alternatives for ordered statistics decoding implementation are proposed. The first approach involves uniformly grouping test error patterns, while the second scheme dynamically generates qualified searching test error patterns with varied sizes for each group. In both methods, group priorities are determined empirically.   Thirdly, iteration diversity is highlighted in the case of LDPC codes requiring high maximum iterations of decoding. This is achieved by segmenting the long iterative decoding trajectory of a decoding failure into shorter segments, which are then independently fed to small models to enhance the chances of acquiring the authentic error pattern.   These ideas are substantiated through extensive simulation results covering the codes with block lengths ranging from one hundred to several hundreds.

## An Optimal Unequal Error Protection LDPC Coded Recording System

- **Status**: ✅
- **Reason**: B/E: 기록(recording) 시스템용 비정칙 LDPC UEP 코드 설계, density evolution/EXIT 최적화 — 스토리지 ECC 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2310.04923v2
- **Type**: preprint
- **Published**: 2023-10-07
- **Authors**: Hong-fu Chou
- **PDF**: https://arxiv.org/pdf/2310.04923v2
- **Abstract**: For efficient modulation and error control coding, the deliberate flipping approach imposes the run-length-limited(RLL) constraint by bit error before recording. From the read side, a high coding rate limits the correcting capability of RLL bit error. In this paper, we study the low-density parity-check (LDPC) coding for RLL constrained recording system based on the Unequal Error Protection (UEP) coding scheme design. The UEP capability of irregular LDPC codes is used for recovering flipped bits. We provide an allocation technique to limit the occurrence of flipped bits on the bit with robust correction capability. In addition, we consider the signal labeling design to decrease the number of nearest neighbors to enhance the robust bit. We also apply the density evolution technique to the proposed system for evaluating the code performances. In addition, we utilize the EXIT characteristic to reveal the decoding behavior of the recommended code distribution. Finally, the optimization approach for the best distribution is proven by differential evolution for the proposed system.
