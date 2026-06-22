# IEEE Xplore — 2018-01 (1차선별 통과)


## Design Guidelines of Low-Density Parity-Check Codes for Magnetic Recording Systems

- **Status**: ✅
- **Reason**: 자기기록(MR) 스토리지용 LDPC 코드 설계 서베이지만 코드구성·디코더·error floor 정량 가이드라인 포함 → 서베이 예외 포함(B/C/E), Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8269289
- **Type**: journal
- **Published**: Secondquar
- **Authors**: Yi Fang, Guojun Han, Guofa Cai +3
- **PDF**: https://ieeexplore.ieee.org/document/8269289
- **Abstract**: As one of the most classical data-storage systems, magnetic recording (MR) systems have attracted a significant amount of research attention in the past several decades due to the advantages of low cost and high storage density. Along with the continual increase of areal density of modern MR devices, more severe inter-symbol interference (ISI) and noise appear and thus reliable storage becomes more difficult. To address this challenging problem, turbo detections and error-correction codes (ECCs) have been applied to MR systems so as to significantly improve the overall data-storage reliability. Among all the existing ECCs, low-density parity-check (LDPC) codes are of particular interest because they can offer excellent error performance with relatively low encoding and decoding complexity. This paper presents a comprehensive survey of the latest research advancements in LDPC-code design for MR systems from the perspectives of code construction, decoder design, as well as asymptotic performance-evaluation methodology. More specifically, we summarize the design guidelines of LDPC encoder and decoder over both one-dimensional (OD) ISI and two-dimensional (TD) ISI channels, which are commonly used to characterize MR systems with different areal densities. We also concisely portray the research progress in the design of some LDPC-code variants, such as protograph codes, repeat-accumulate codes, spatially coupled codes, and their non-binary counterparts over the aforementioned ISI channels. In particular, we restrict our attention to the reading process and ignore the written-in errors in MR systems unless otherwise stated. Hopefully, this survey will inspire more research activities in the area of LDPC-coded MR systems.

## An Iterative Check Polytope Projection Algorithm for ADMM-Based LP Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: ADMM 기반 LP 디코딩의 parity-check polytope 투영을 sorting 없이 선형복잡도로 수행하는 새 디코더 알고리즘 — 바이너리 LDPC BP/LP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8082498
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Haoyuan Wei, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8082498
- **Abstract**: Alternating direction method of multipliers (ADMM) is a popular technique for linear-programming decoding of low-density parity-check codes. The computational complexity of ADMM is dominated by the Euclidean projection of a real-valued vector onto a parity-check polytope. Existing algorithms for such a projection all require sorting operations, which happen to be the most complex part of the projection. In this letter, we propose an iterative algorithm, without sorting operation, for projection onto the parity-check polytope. The proposed algorithm has a worst case complexity linear in the input dimension compared with the super-linear complexity of existing algorithms.

## On the Construction of LDPC Codes Free of Small Trapping Sets by Controlling Cycles

- **Status**: ✅
- **Reason**: QC-LDPC 구성으로 small trapping set 제거(8-cycle 제어)·error floor 개선 → 카테고리 E 이식 가능 코드설계, 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7874123
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Xiongfei Tao, Yufei Li, Yonghe Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7874123
- **Abstract**: Low-density parity-check (LDPC) codes exhibit excellent error correcting capability. However, small trapping sets in the Tanner graph are harmful to the iterative decoding algorithm. In this letter, we present a method of constructing (3, n) girth-eight quasi-cyclic LDPC codes with low error floor by removing the small trapping sets from the Tanner graph. To address this issue, we analyze the relationship between eight-cycles and small trapping sets of Tanner graphs based on fully connected base graphs without parallel edges. We find that if some eight-cycles are not found in the Tanner graphs, any elementary trapping set in the range of a ≤ 8 and b ≤ 3 is removed naturally. We also derive a lower bound on the permutation size for the construction of such codes. The experimental simulation shows a favorable error rate performance with lower error floor over additive white Gaussian noise channels.

## Memory-Reduced Look-Up Tables for Efficient ADMM Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC ADMM 디코딩 LUT 비균일 양자화 메모리 절감 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8055603
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Xiaopeng Jiao, Yu-Cheng He, Jianjun Mu
- **PDF**: https://ieeexplore.ieee.org/document/8055603
- **Abstract**: The Euclidean projection involved in the decoding of low-density parity-check (LDPC) codes with the alternating direction method of multipliers (ADMM) can be simplified by jointly using uniform quantization and look-up tables (LUTs). However, the memory requirement for the original LUT-based ADMM decoding is comparatively large. In this letter, a nonuniform quantization method is proposed to save the memory cost by minimizing the mean square error of the outputs of Euclidean projections during quantization. Simulation results over two exemplified LDPC codes show that the proposed method can achieve similar error-rate performances when compared with the original LUT-based ADMM decoding by using significantly less memory units.

## A Reconfigurable LDPC Decoder Optimized for 802.11n/ac Applications

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 min-sum 근사 개선+barrel rotator permutation network HW — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8052499
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Ioannis Tsatsaragkos, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/8052499
- **Abstract**: This paper presents a high data-rate low-density parity-check (LDPC) decoder, suitable for the 802.11n/ac (WiFi) standard. The innovative features of the proposed decoder relate to the decoding algorithms and the interconnection between the processing elements. The reduction of the hardware complexity of decoders based on the min-sum (MS) algorithms comes at the cost of performance degradation, especially at high-noise regions. We introduce more accurate approximations of the log-sum-product algorithm that also operate well for low signal-to-noise ratio values. Telecommunication standards, including WiFi, support more than one quasi-cyclic LDPC codes of different characteristics, such as codeword length and code rate. A proposed design technique derives networks, capable of supporting a variety of codes and efficiently realizing connectivity between a variable number of processing units, with a relatively small hardware overhead over the single-code case. As a demonstration of the proposed technique, we implemented a reconfigurable network based on barrel rotators, suitable for LDPC decoders compatible with WiFi standard. Our approach achieves low complexity and high clock frequency, compared with related prior works. A 90-nm application-specified integrated circuit implementation of the proposed high-parallel WiFi decoder occupies 4.88 mm2 and achieves an information throughput rate of 4.5 Gbit/s at a clock frequency of 555 MHz.

## A New Multi-Edge Metric-Constrained PEG Algorithm for Designing Binary LDPC Code With Improved Cycle-Structure

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 신규 multi-edge PEG 알고리즘으로 cycle-structure 개선 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8039508
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Xuan He, Liang Zhou, Junyi Du
- **PDF**: https://ieeexplore.ieee.org/document/8039508
- **Abstract**: The progressive edge-growth (PEG) algorithm constructs an edge in each stage to maximize the variable node (VN) of interest's local girth in real time. Thus, this VN's local girths, after more than one edge is added to the current tanner graph (TG) setting, may not be maximized relative to that TG setting. To address this problem, we define the multi-edge local girth and edge-trial, and based on these definitions, propose a new multi-edge metric-constrained PEG algorithm (MM-PEGA) to improve the design at each VN. The MM-PEGA constructs an edge in each stage that, relative to the current TG setting, can potentially maximize the VN of interest's local girth after a certain number (up to the edge-trial) of edges are added to the TG setting. We first analyze the properties of the multi-edge local girth, and then propose an algorithm for calculating the multi-edge local girth. We also propose a method for accelerating the MM-PEGA. Moreover, we generalize the MM-PEGA for improving different PEG-like designs. According to the theoretical analysis, increasing the edge-trial of the MM-PEGA is expected to positively affect the cycle-structure and the error performance of resulting low-density parity-check (LDPC) code. This expectation is verified by simulations.

## LLR-Distribution-Based Non-Uniform Quantization for RBI-MSD Algorithm in MLC Flash Memory

- **Status**: ✅
- **Reason**: MLC 플래시 RBI-MSD용 LLR분포기반 비균일 양자화 — NAND 직접+디코더 양자화(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8047952
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Shijie Ouyang, Guojun Han, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/8047952
- **Abstract**: Multi-level cell (MLC) technique has been widely used to improve the storage capacity of NAND flash memory at the price of sacrificing some storage reliability. As a type of excellent error-correction codes, low-density parity-check (LDPC) codes can significantly enhance the performance of flash memory. However, the conventional decoding algorithms for LDPC codes suffer from the drawback of high complexity. To address this problem, we propose a serial reliability-based iterative min-sum decoding (RBI-MSD) algorithm for LDPC-coded MLC flash memory systems to strike a desirable trade-off between the performance and complexity. Furthermore, we conceive a novel log-likelihood-ratio (LLR)-distribution-based non-uniform quantization method for the RBI-MSD algorithm. Unlike conventional quantization methods, the proposed non-uniform quantization method substantially exploits the distribution characteristics of channel initial LLRs in MLC flash memory. Simulation results indicate that the proposed non-uniform quantization method not only exhibits more excellent error performance than the conventional non-uniform and uniform counterparts, but also is applicable to other RBI decoding algorithms.

## An Imprecise Stopping Criterion Based on In-Between Layers Partial Syndromes

- **Status**: ✅
- **Reason**: 레이어드 LDPC 디코더 조기정지 기준(in-between layers partial syndrome)으로 저HW비용 신규 기법 → C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7954939
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: D. Declercq, V. Savin, O. Boncalo +1
- **PDF**: https://ieeexplore.ieee.org/document/7954939
- **Abstract**: In this letter, we address the issue of early stopping criterion for layered LDPC decoders, aiming at more safeness with low hardware cost and minimum latency. We introduce a new on-the-fly measure in the decoder, called in-between layers partial syndrome, and define a family of stopping criteria, with different tradeoffs among complexity, latency, and performance. Numerical results show that our stopping criteria surpass existing solutions, and can be as safe as the full-syndrome detection, down to frame error rates (FERs) as low as FER = 10-8.

## Decision-Directed Retention-Failure Recovery With Channel Update for MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND retention-aware BP 디코딩(RABP) 및 채널갱신 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7959126
- **Type**: journal
- **Published**: Jan. 2018
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/7959126
- **Abstract**: To recover from the retention noise induced errors in nand flash memory, a retention-aware belief-propagation (RABP) decoding scheme for low-density parity-check codes is introduced. The RABP is a two-stage decoding scheme in which the memory cell's charge-loss effect is systematically compensated. In RABP decoding, instead of read retries for data recovery, the probable victim cells are first determined with the help of read-back voltage signal and the decoded bit decisions. Then, for such suspected victim cells, their log-likelihood-ratio regions are modified in such a way as to absorb the effect of cell voltage downshift caused by retention noise, and then a second round of belief-propagation (BP) decoding is performed afresh, often with decoding failure recovery. Furthermore, leveraging on the RABP decoded bit-error pattern, an RABP assisted channel update (RABP-CU) algorithm is proposed which re-estimates the latest cell voltage distribution parameters without incurring new memory sensing operations. This is achieved by minimizing the mean squared error between the measured and predicted bit error/erasure values. Through simulations, it is shown that the RABP decoder increases the retention time limit by up to 70% compared with single round of BP decoding. The proposed RABP-CU algorithm further extends the data retention time.

## Design of nested protograph-based LDPC codes with low error-floors

- **Status**: ✅
- **Reason**: E. 프로토그래프 LDPC 유해 그래프구조 제거로 error-floor 저감(데이터스토리지 명시), 바이너리 코드설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8301736
- **Type**: conference
- **Published**: 8-10 Jan. 
- **Authors**: Matthew L. Grimes, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/8301736
- **Abstract**: In this paper, we propose a method to design nested protograph-based low-density parity-check (LDPC) codes for network communications with low error-floors via a graph modification procedure. Lowering the error-floor of nested LDPC codes is essential for certain applications that require very low decoded error rates in moderate to high signal-to-noise-ratios (SNRs) like optical communication and data storage. The multilevel method we propose improves upon existing state-of-the-art algebraic designs by the identification and removal of harmful graph structures from nested LDPC codes, effectively improving the performance of each of the nested codes in their error-floor region. Simulation results are provided that confirm the expected performance improvement.

## Algebra-Assisted Construction of Quasi-Cyclic LDPC Codes for 5G New Radio

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 신규 구성(WANC 사이클 메트릭 기반 알고리즘)으로 코드 설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8456498
- **Type**: journal
- **Published**: 2018
- **Authors**: Huaan Li, Baoming Bai, Xijin Mu +2
- **PDF**: https://ieeexplore.ieee.org/document/8456498
- **Abstract**: Quasi-cyclic LDPC (QC-LDPC) codes have been accepted as the standard codes of 5G enhanced mobile broadband data channel. These standard codes are designed to support multiple lifting sizes and possess rate-compatible property, which can help adapt various information lengths and code rates well. In this paper, we propose an algebra-assisted method for constructing QC-LDPC codes with such properties. We will first review the encoding mechanism and requirements of 5G LDPC codes, and present cycle analysis for such emerging codes. We then propose a metric, referred to as weighted average number of cycles (WANC), from the perspective of cycle structure for constructing the QC-LDPC codes that can support multiple lifting sizes. Based on the WANC metric and algebraic methods, we develop a simple and practical algorithm to construct this kind of QC-LDPC codes. We finally apply the proposed algorithm to construct the exponent matrices for cases of 5G LDPC codes and the standard LDPC codes of consultative committee for space data systems, respectively. Simulation results show that the proposed WANC metric and designed algorithm are feasible and effective, and thus can be utilized to design other similar QC-LDPC codes.

## On the Stopping Distance of SA-LDPC Codes by Transversal Designs

- **Status**: ✅
- **Reason**: E: transversal design 기반 SA-LDPC stopping distance/error floor 분석, 바이너리 LDPC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8415746
- **Type**: journal
- **Published**: 2018
- **Authors**: Zahra Ferdosi, Farhad Rahmati, Mohammad Hesam Tadayon
- **PDF**: https://ieeexplore.ieee.org/document/8415746
- **Abstract**: In this paper, we analyze the size of the smallest stopping set (called the stopping distance) for the parity-check matrix of a superposed array low-density parity-check (SA-LDPC) code for column weights 3 and 4 by using the transversal design (TD) concept. An SA-LDPC code is obtained as the result of an n-fold recursive product operation (a superposition method) on the parity-check matrix of an array low-density parity-check (array LDPC) code, Hn(m, q), where n ≥ 2 and m and q are column and row weights, respectively. We provide the lower and upper bounds for the stopping distance of these codes. Our simulation result shows that the SA-LDPC codes can compete with the TD-LDPC codes, random LDPC codes, and lattice LDPC codes of comparable rates and lengths and can improve the error floor region of the bit error rate curve.

## QFEC ASIP: A Flexible Quad-Mode FEC ASIP for Polar, LDPC, Turbo, and Convolutional Code Decoding

- **Status**: ✅
- **Reason**: Quad-mode FEC ASIP에 LDPC(WiMAX) 디코딩 지원, 메모리공유·throughput HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8543800
- **Type**: journal
- **Published**: 2018
- **Authors**: Wan Qiao, Dake Liu, Shaohan Liu
- **PDF**: https://ieeexplore.ieee.org/document/8543800
- **Abstract**: In this paper, we extend polar decoding function to our previous design, and propose a flexible quad-mode forward error correction application specific instruction-set processor (QFEC ASIP) that supports polar, low-density parity-check (LDPC), turbo, and convolutional code (CC) decoding with multiple code lengths and code rates. A unified polar/LDPC/turbo/CC quad-mode algorithm framework is presented. The top level architecture of QFEC ASIP and the polar data path are designed on the basis of the algorithm framework. A quad-mode confliction-free global memory system is proposed. 65.2% of global memory banks, 48.9% of global memory bits, and 29.7% of global memory area are saved via hardware sharing. Specially accelerated FEC decoding instructions make the decoding procedure fully programmable and ensure the high throughput. Synthesis using 65-nm technology shows that the total area of QFEC ASIP is 4.26 mm2. QFEC ASIP provides the maximum throughput of 1345 Mb/s for polar, 917 Mb/s for LDPC (WiMAX), 320 Mb/s for turbo, and 387 Mb/s for CC (64 states) at the clock frequency of 344 MHz. QFEC ASIP occupies much smaller silicon area than the sum of the silicon area of 4 single-mode FEC decoders that together provide a similar function range as QFEC ASIP.

## Lower Bounds on the Lifting Degree of QC-LDPC Codes by Difference Matrices

- **Status**: ✅
- **Reason**: QC-LDPC lifting degree·girth(6/10/12) 하한·사이클 제거 구성, 바이너리 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8350277
- **Type**: journal
- **Published**: 2018
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/8350277
- **Abstract**: In this paper, we define two “difference matrices” which correspond to an exponent matrix. We present necessary and sufficient conditions for these difference matrices to have quasi-cyclic low-density parity-check codes (QC-LDPC) codes with a certain girth. We achieve all non-isomorphic QC-LDPC codes with the shortest length, girth 6, the column weight, m = 4, and the row weight, 5 ≤ n ≤ 11. Moreover, a method to obtain an exponent matrix with girth 10 is presented which reduces the complexity of the search algorithm. If the first row and the first column of the exponent matrix are all-zero, then by applying our method we do not need to test Fossorier's lemma to avoid 6-cycles and 8-cycles. For girth 10, we also provide a lower bound on the lifting degree which is tighter than the existing bound. For girth 12, a new lower bound on the lifting degree is achieved.

## An Approach to Evaluating the Number of Closed Paths in an All-One Base Matrix

- **Status**: ✅
- **Reason**: all-one 기저행렬 폐경로(cycle) 개수 평가법 제안 — QC-LDPC 사이클 제거·코드 최적화(E)에 직접 이식
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8326474
- **Type**: journal
- **Published**: 2018
- **Authors**: Sheng Jiang, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/8326474
- **Abstract**: Given an all-one base matrix of size M×N, a closed path of different lengths can be formed by starting at an arbitrary element and moving horizontally and vertically alternatively before terminating at the same “starting” element. When the closed-path length is small, say 4 or 6, the total number of combinations can be evaluated easily. When the length increases, the computation becomes non-trivial. In this paper, a novel method is proposed to evaluate the number of closed paths of different lengths in an all-one base matrix. Theoretical results up to closed paths of length 10 have been derived and are verified by the exhaustive search method. Based on the theoretical work, results for closed paths of length larger than 10 can be further derived. Note that each of such closed paths may give rise to one or more cycles in a low-density parity-check (LDPC) code when the LDPC code is constructed by replacing each “1” in the base matrix with a circulant permutation matrix or a random permutation matrix. Since LPDC codes with short cycles are known to give unsatisfactory error correction capability, the results in this paper can be used to estimate the amount of effort required to evaluate the number of potential cycles of an LDPC code or to optimize the code.

## LDPC Decoding Algorithms for Implant to Implant Wireless Body Area Network

- **Status**: ✅
- **Reason**: WBAN용이지만 신규 저복잡도 하이브리드 결정 LDPC 디코딩 알고리즘 제안(C) — 부호 비의존 디코더로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8306087
- **Type**: journal
- **Published**: 2018
- **Authors**: Albashir Adel Youssef, Bassant Abdelhamid, Salwa Hussein El-ramly +2
- **PDF**: https://ieeexplore.ieee.org/document/8306087
- **Abstract**: Wireless body area network (WBAN) is a promising network aiming at enhancing the communication in medical applications. It is adopted by medical organizations due to its flexibility in remotely monitoring patient health status. WBANs suffer from many limitations due to excessive channel impairments. Low density parity check (LDPC) codes are proposed to mitigate WBAN's impairments concerning the bit error rate, complexity, and dissipated energy. In this paper, a comprehensive performance analysis of various LDPC decoding algorithms is used to improve communication and reduce complexity in implant to implant WBAN channel. Moreover, a novel low complex LDPC decoding algorithm, which has a performance close to soft decision and a decoding time close to hard decision algorithms is proposed to minimize the dissipated energy. The proposed algorithm can be classified as a hybrid decision algorithm. The results demonstrate extensive analysis and comparisons between hard, soft, and hybrid decision algorithms.

## Decoding Optimization for 5G LDPC Codes by Machine Learning

- **Status**: ✅
- **Reason**: QC-LDPC용 머신러닝 최적화 선형근사 min-sum(LAMS) 디코더로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8458121
- **Type**: journal
- **Published**: 2018
- **Authors**: Xiaoning Wu, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/8458121
- **Abstract**: In this paper, we propose a generalized minimum-sum decoding algorithm using a linear approximation (LAMS) for protograph-based low-density parity-check (PB-LDPC) codes with quasi-cyclic (QC) structures. The linear approximation introduces some factors in each decoding iteration, which linearly adjust the check node updating and channel output. These factors are optimized iteratively using machine learning, where the optimization can be efficiently solved by a small and shallow neural network with training data produced by the LAMS decoder. The neural network is built according to the parity check matrix of a PB-LDPC code with a QC structure which can greatly reduce the size of the neural network. Since, we optimize the factors once per decoding iteration, the optimization is not limited by the number of the iterations. Then, we give the optimized results of the factors in the LAMS decoder and perform decoding simulations for PB-LDPC codes in fifth generation mobile networks (5G). In the simulations, the LAMS algorithm shows noticeable improvement over the normalized and the offset minimum-sum algorithms and even better performance than the belief propagation algorithm in some high signal-to-noise ratio regions.

## Design and Analysis of Punctured Terminated Spatially Coupled Protograph LDPC Codes With Small Coupling Lengths

- **Status**: ✅
- **Reason**: E: punctured terminated SC-protograph LDPC 신규 puncturing 설계(P-TE-SC-P), 바이너리 LDPC 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8398231
- **Type**: journal
- **Published**: 2018
- **Authors**: Zhaojie Yang, Yi Fang, Guojun Han +2
- **PDF**: https://ieeexplore.ieee.org/document/8398231
- **Abstract**: Spatially coupled protograph (SC-P) low-density parity-check codes can achieve excellent performance and simple implementation when the coupling length is sufficiently large. However, in the case of small coupling lengths, terminated SC-P (TE-SC-P) codes suffer from relatively weaker decoding thresholds and lower code rates compared with the original protograph codes. To address the above issues, we propose a novel design method to enhance the performance of such TE-SC-P codes. Specifically, we develop a bus-topology-like puncturing rule so as to formulate a new family of SC-P codes, referred to as punctured TE-SC-P (P-TE-SC-P) codes. Theoretical analyses and simulation results show that the proposed P-TE-SC-P codes possess significant performance gains over conventional SC-P codes and randomly punctured TE-SC-P (called RP-TE-SC-P) codes with relatively higher computational complexity.

## Generalized LDPC Codes for Ultra Reliable Low Latency Communication in 5G and Beyond

- **Status**: ✅
- **Reason**: QC-GLDPC 신규 구성+min-sum/양자화 분석+constraint-to-variable 갱신규칙, 바이너리 LDPC 디코더/구성 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8532357
- **Type**: journal
- **Published**: 2018
- **Authors**: Yanfang Liu, Pablo M. Olmos, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/8532357
- **Abstract**: Generalized low-density parity-check (GLDPC) codes, where single parity-check constraints on the code bits are replaced with generalized constraints (an arbitrary linear code), are a promising class of codes for low-latency communication. In this paper, a practical construction of quasi-cyclic GLDPC codes is proposed, where the proportion of generalized constraints is determined by an asymptotic analysis. We analyze the complexity and performance of the message passing decoder with various update rules (including standard full-precision sum-product and min-sum algorithms) and quantization schemes for a GLDPC code over the additive white Gaussian noise (AWGN) channel and present a constraint-to-variable update rule based on the specific codewords of the component codes. The block error rate performance of the GLDPC codes, combined with a complementary outer code, is shown to outperform a variety of state-of-the-art code and decoder designs with suitable lengths and rates for the 5G ultra-reliable low-latency communication regime over an AWGN channel with quadrature PSK modulation.

## RBER Aware Multi-Sensing for Improving Read Performance of 3D MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D MLC NAND, RBER-aware multi-sensing로 LLR soft-decision 센싱 지연 개선, NAND LDPC 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8478389
- **Type**: journal
- **Published**: 2018
- **Authors**: Meng Zhang, Fei Wu, Xubin Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/8478389
- **Abstract**: 3D-multi-level cell (MLC) NAND flash memory adopts 3D stack technology and stores two bits per cell, leading to improved storage capacities, but sacrificing data reliability. Low-density parity-check (LDPC) codes showing strong error correction capability benefit from their soft decision decoding, which is widely exploited to guarantee data reliability. Nevertheless, adopting LDPC codes can introduce a concern about read performance, because their iterative soft-decision decoding requires LogLikelihood Ratio (LLR) information, called soft decision information, by applying multi-sensing voltages. This process of obtaining LLR information leads to high sensing and transferring latencies, lowering down 3D-MLC read performance. In particular, when raw bit error rates (RBER) are much higher due to the long retention periods and program/erase (P/E) cycles, this problem becomes more serious. In this paper, we propose a RBER-aware multi-sensing scheme for reducing sensing and transferring latencies, and thus improving read performance. This proposed scheme exploits the variations of RBER in flash pages with the increase of retention time and P/E cycles to dynamically apply sensing voltages. Simulation results show that this scheme significantly decreases the number of required sensing voltages while maintaining LDPC error correction capability, enhancing 3D-MLC read performance.

## Information-Optimum LDPC Decoders Based on the Information Bottleneck Method

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 정수연산 LUT LDPC 디코더, min-sum 능가; 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8268118
- **Type**: journal
- **Published**: 2018
- **Authors**: Jan Lewandowsky, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/8268118
- **Abstract**: The Information Bottleneck method is a powerful and generic tool from the field of machine learning. It compresses an observation to a quantized variable while attempting to preserve the mutual information shared with a relevant random variable. This paper describes a new application of the Information Bottleneck method in communications. It explains in detail, how the Information Bottleneck method can be applied to construct discrete message passing decoders for regular low-density parity-check codes. The obtained decoders process only unsigned integers and use only simple lookup tables as node operations. As a consequence, the decoders can be implemented using only unsigned integer arithmetic which makes them significantly simpler and faster than the state-of-the-art decoders which process real valued log-likelihood ratios. Anyway, included results show that the considered discrete message passing decoders perform surprisingly close to optimum message passing decoders and even outperform state-of-the-art decoders, such as the min-sum decoder. We aim to take the reader on a journey from the theoretical idea of the Information Bottleneck method to a complete design framework for the considered discrete decoders. Several included figures and examples illustrate the decoder construction process and its analysis.

## Improving Windowed Decoding of SC LDPC Codes by Effective Decoding Termination, Message Reuse, and Amplification

- **Status**: ✅
- **Reason**: SC-LDPC 윈도우 디코딩 개선(종료/메시지 재사용/증폭) 신규 디코더 기법 및 error floor 저감 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8101470
- **Type**: journal
- **Published**: 2018
- **Authors**: Inayat Ali, Jong-Hwan Kim, Sang-Hyo Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/8101470
- **Abstract**: In this paper, we address a number of weaknesses of the windowed decoding of spatially coupled low-density parity-check (SC LDPC) codes and propose three modifications that simultaneously improve its performance, complexity, and latency. An effective termination method of the windowed decoding and the reuse of edge messages of previous target symbols provide a good performance-latency tradeoff when compared with the conventional windowed decoder. Also, we propose a scheme that lowers the error floor, in which the amplified edge messages of the previous window are used in the present window. The proposed windowed decoding, consisting of the three schemes, provides a significant performance gain with smaller latency. The validity of the new windowed decoding is verified by the evaluation with codes from different SC LDPC ensembles.

## Delay-Universal Channel Coding With Feedback

- **Status**: ✅
- **Reason**: E/C: SC-RA 기반 anytime 부호+error floor 완화 피드백, 바이너리 SC-LDPC 계열 구성·EC 기법 일부 이식 여지(애매→살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8404040
- **Type**: journal
- **Published**: 2018
- **Authors**: Md. Noor-A-Rahim, M. O. Khyam, Yong Liang Guan +3
- **PDF**: https://ieeexplore.ieee.org/document/8404040
- **Abstract**: In this paper, the design of error-correcting or channel codes for delay-universal/anytime communication is shown while considering systems with and without a feedback link. We construct practical and low complexity anytime channel codes based on spatially-coupled repeat-accumulate (SC-RA) codes. Performance and density evolution analysis are shown for the binary erasure channel (BEC) and the binary input additive white Gaussian noise (BIAWGN) channel. We observe that the erasure/error floors exist even at low decoding delay in the following cases: 1) when the code rate is close to the Shannon capacity; and/or 2) when the code parameters are chosen to target a high decaying rate of erasure/error probability. To mitigate erasure/error floors, we present feedback algorithms for BEC and BIAWGN channels. We show that the proposed feedback strategies can greatly enhance the performance of anytime SC-RA codes. Numerical results also show that the feedback strategies significantly reduce the decoder complexity. The proposed feedback approach is applied to an aircraft tracking application to track/calculate/estimate the state information of the aircraft. Based on comparisons of the results obtained from the traditional block and anytime coding scenarios, it is observed that the latter significantly outperforms the former in terms of tracking performance.

## Early termination belief propagation decoder with parity check matrix for polar codes

- **Status**: ✅
- **Reason**: polar용 BP 디코더의 syndrome 기반 early termination 기법 — 부호 비의존적 BP 조기종료 아이디어로 바이너리 LDPC BP에 이식 가능(예외 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8372719
- **Type**: conference
- **Published**: 2018
- **Authors**: H. -F. Yu, H. -C. Lee, S. -K. Lee
- **PDF**: https://ieeexplore.ieee.org/document/8372719
- **Abstract**: In this paper, a belief propagation (BP) decoding algorithm with early termination is proposed for polar code. The early termination is accomplished using the syndrome generated by the parity-check matrix, which can be transferred from the generator matrix. With the assistance of the early termination, the BP decoder can provide not only a better bit error rate performance but also significantly reduce the decoding complexity. For (1024, 512) polar codes, the average numbers of iterations can be reduced from 80 to 23 when Eb/N0=3 dB. The reduction in the computation complexity is about 70%.

## Decoding Reed-Muller Codes Using Minimum- Weight Parity Checks

- **Status**: ✅
- **Reason**: Iterative BP/bit-flipping on redundant min-weight parity checks with per-observation PC selection; decoder technique arguably code-agnostic, transferable to binary LDPC BP (C), keep for Phase 3
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8437637
- **Type**: conference
- **Published**: 2018
- **Authors**: E. Santi, C. Hager, H. D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/8437637
- **Abstract**: Reed-Muller (RM) codes exhibit good performance under maximum-likelihood (ML) decoding due to their highly-symmetric structure. In this paper, we explore the question of whether the code symmetry of RM codes can also be exploited to achieve near-ML performance in practice. The main idea is to apply iterative decoding to a highly-redundant parity-check (PC) matrix that contains only the minimum-weight dual codewords as rows. As examples, we consider the peeling decoder for the binary erasure channel, linear-programming and belief propagation (BP) decoding for the binary-input additive white Gaussian noise channel, and bit-flipping and BP decoding for the binary symmetric channel. For short block lengths, it is shown that near-ML performance can indeed be achieved in many cases. We also propose a method to tailor the PC matrix to the received observation by selecting only a small fraction of useful minimum-weight PCs before decoding begins. This allows one to both improve performance and significantly reduce complexity compared to using the full set of minimum-weight PCs.

## Spatially-Coupled Code Design for Partial-Response Channels: Optimal Object-Minimization Approach

- **Status**: ✅
- **Reason**: SC-LDPC 코드 설계 OO-CPO로 detrimental object 최소화(Flash/PR 채널) — 바이너리 SC-LDPC 신규 구성·error floor 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8647335
- **Type**: conference
- **Published**: 2018
- **Authors**: A. Hareedy, H. Esfahanizadeh, A. Tan +1
- **PDF**: https://ieeexplore.ieee.org/document/8647335
- **Abstract**: Spatially-coupled (SC) codes are among the most attractive error-correcting codes for use in modern storage devices. SC codes are constructed by partitioning an underlying block code and coupling the partitioned components. Here, we focus on circulant-based SC codes. Recently, the optimal overlap (OO), circulant power optimizer (CPO) approach was introduced to construct high performance SC codes for AWGN and Flash channels. The OO partitioning stage operates on the protograph of the SC code, while the CPO optimizes the circulant powers, in order to minimize the number of detrimental objects. Since the nature of detrimental objects in the graph of a code critically depends on the characteristics of the channel of interest, extending the OO-CPO approach to construct SC codes for channels with intrinsic memory is not a straightforward task. In this paper, we tackle one relevant extension; we construct high performance SC codes for practical 1-D magnetic recording channels, i.e., partial-response (PR) channels. Via combinatorial techniques, we carefully build and solve the optimization problem of the OO partitioning, focusing on the objects of interest in the case of PR channels. Then, we customize the CPO to further reduce the number of these objects in the graph of the code. SC codes designed using the OO-CPO approach for PR channels outperform prior state-of-the-art SC codes by around 3 orders of magnitude in FER and 1.1 dB in SNR, and more intriguingly, outperform structured block codes of the same length by around 1.6 orders of magnitude in FER and 0.4 dB in SNR.

## Thresholds of Braided Convolutional Codes on the AWGN Channel

- **Status**: ✅
- **Reason**: braided convolutional의 spatial coupling threshold/density evolution 분석 — SC-LDPC 코드설계(E)로 이식 가능, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8437937
- **Type**: conference
- **Published**: 2018
- **Authors**: M. U. Farooq, S. Moloudi, M. Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/8437937
- **Abstract**: In this paper, we perform a threshold analysis of braided convolutional codes on the additive white Gaussian noise (AWGN) channel. The decoding thresholds are estimated by Monte-Carlo density evolution techniques and compared with approximate thresholds from an erasure channel prediction. The results show that, with spatial coupling, the predicted thresholds are very accurate and quickly approach capacity if the coupling memory is increased. For uncoupled ensembles with random puncturing, the prediction can be improved with help of the AWGN threshold of the unpunctured ensemble.

## High-rate Spatially Coupled Codes for Channels with Synchronous Errors

- **Status**: ✅
- **Reason**: Spatially-coupled (binary) LDPC code design with density evolution/protograph analysis for synchronous-error channels (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8437608
- **Type**: conference
- **Published**: 2018
- **Authors**: R. Goto, K. Kasai
- **PDF**: https://ieeexplore.ieee.org/document/8437608
- **Abstract**: In this paper, we deal with coding for synchronous errors. In [1], we introduced a synchronously erroneous finite state Markov channel model whose SIR is computable. Numerical experiments demonstrated spatially-coupled codes approach the SIR of the channel. However, at high-rate region, there is a gap to the SIR even if very long code length was used. In this paper, for the channel, we apply density evolution analysis [2] and the extended version for FSMC [3]. The results show that the threshold of protograph coupled codes is degraded at high-rate region, while random coupled codes approach the SIR even in the high-rate region.

## Deep Learning Based Joint Detection and Decoding of Non-Orthogonal Multiple Access Systems

- **Status**: ✅
- **Reason**: MPA/BP factor graph에 weight 부여 후 딥러닝 학습하는 neural decoder — 부호 비의존적 BP 개선(C), 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8644090
- **Type**: conference
- **Published**: 2018
- **Authors**: F. Sun, K. Niu, C. Dong
- **PDF**: https://ieeexplore.ieee.org/document/8644090
- **Abstract**: In recent years, many studies have applied deep learning techniques to the field of communication. Many of them have achieved reduced complexity or improved performance. In this paper, we apply deep learning techniques to joint multiuser detection and decoding of non-orthogonal multiple access system. We construct the neural network detector and decoder based on message passing algorithm (MPA) and belief propagation (BP) algorithm, respectively. And the decoder is cascaded with the detector to form a larger neural network. To achieve this, we assign weights to the edges of the respective factor graphs and then use deep learning approaches to train these weights to get better performance. Compared with the conventional method (i.e. MPA for multiuser detection and BP for decoding), the proposed method improves the joint detection and decoding performance, while the computational complexity is not greatly increased.

## Error Characterization and ECC Usage Relaxation beyond 20nm Floating Gate NAND Flash Memory

- **Status**: ✅
- **Reason**: A: 20nm 이하 floating gate NAND read-retry/ECC bit 완화·TLC BER 직접 - NAND ECC 직접 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8388829
- **Type**: conference
- **Published**: 2018
- **Authors**: S. H. Ku, T. W. Lin, C. H. Cheng +8
- **PDF**: https://ieeexplore.ieee.org/document/8388829
- **Abstract**: Endurance of floating gate flash memories at 19nm node and beyond is studied comprehensively. Experiments reveal that the random telegraph noise (RTN) would degrade the read margin with a tail, which quickly reshapes into a symmetric Gaussian form in a lightly-stressed state. After heavy stress, the lower part of tail would spread further while the upper part keeps roughly overlapped with that during fresh. This unique behavior, which was firstly measured by the self-established Budget Product Tester (BPT), can be explained by stress-induced hole trap creation. To investigate the impact of RTN on operation window, a novel algorithm of Multi-Times-Verify accompanied with the optimal Read-Retry (MTVR2) is proposed and validated by BPT. The advantage of MTVR2 to reduce the requirement of Error-Correcting Code (ECC) bit is demonstrated. Finally, the improvement of bit error rate (BER) in TLC operation with MTVR2 is also evaluated.

## A Neural Network Lattice Decoding Algorithm

- **Status**: ✅
- **Reason**: 신경망 디코더 4-cycle 제거→girth-6, updated LLR 사용; HDPC지만 NN 디코더+사이클제거 기법 바이너리 BP에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613440
- **Type**: conference
- **Published**: 2018
- **Authors**: M. -R. Sadeghi, F. Amirzade, D. Panario +1
- **PDF**: https://ieeexplore.ieee.org/document/8613440
- **Abstract**: Neural network decoding algorithms are recently introduced by Nachmani et al. to decode high-density parity-check (HDPC) codes. In contrast with iterative decoding algorithms such as sum-product or min-sum algorithms in which the weight of each edge is set to 1, in the neural network decoding algorithms, the weight of every edge depends on its impact in the transmitted codeword. In this paper, we provide a novel feed-forward neural network lattice decoding algorithm suitable to decode lattices constructed based on Construction A, whose underlying codes have HDPC matrices. We first establish the concept of feed-forward neural network for HDPC codes and improve their decoding algorithms compared to Nachmani et al. We then apply our proposed decoder for a Construction A lattice with HDPC underlying code, for which the well-known iterative decoding algorithms show poor performances. The main advantage of our proposed algorithm is that instead of assigning and training weights for all edges, which turns out to be time-consuming especially for high-density parity-check matrices, we concentrate on edges which are present in most of 4-cycles and removing them gives a girth -6 Tanner graph. This approach, by slight modifications using updated LLRs instead of initial ones, simultaneously accelerates the training process and improves the error performance of our proposed decoding algorithm.

## BP Polar Decoders with Early Termination and Belief Enhancing

- **Status**: ✅
- **Reason**: BP polar 조기종료(LLR/CRC)+belief enhancing+HW, 부호비의존 BP 조기종료 기법 LDPC BP 이식 여지(C) 애매—살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8631617
- **Type**: conference
- **Published**: 2018
- **Authors**: C. Yang, J. Yang, X. Liang +3
- **PDF**: https://ieeexplore.ieee.org/document/8631617
- **Abstract**: In this paper an early termination scheme, partial LLR-aided (PLA) scheme, is proposed for belief propagation (BP) polar decoding with lower complexity and higher throughput. Numerical results of (1024, 512) code show at least 82% iteration reduction than conventional design at SNR =3.5 dB with proposed early termination scheme. In this paper, belief enhancing schemes based on threshold and cyclic redundancy check (CRC) are proposed, namely, threshold-based LLR (TB-LLR) scheme and segment-divided CRC (SD-CRC) scheme. For (1024, 512) polar code, the performance gains for TB-LLR and SD-CRC are 0.35 dB and 0.2 dB respectively, when BER = 10-3. A general hardware architecture for proposed BP polar decoders is also proposed.

## A Low-Complexity Projection Algorithm for ADMM-Based LP Decoding

- **Status**: ✅
- **Reason**: ADMM-LP LDPC 디코딩의 패리티폴리톱 projection 저복잡도화—이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8625295
- **Type**: conference
- **Published**: 2018
- **Authors**: F. Gensheimer, T. Dietz, S. Ruzika +2
- **PDF**: https://ieeexplore.ieee.org/document/8625295
- **Abstract**: In this paper, we present a new low-complexity algorithm for computing the projection onto the parity polytope in the context of ADMM-based LP decoding. This projection is the heart of the ADMM algorithm, that usually involves a sorting operation, which is the main effort of the projection. Our proposed algorithm relies on new findings in the recursive structure of the parity polytope and works by fixing selected components in an iterative manner. The absence of the sorting operation makes it preferable for efficient hard- and software implementations. In addition, we can show that this new projection algorithm requires up to 37% less arithmetic operations compared to state-of-the-art projections.

## Recent Advances on Stochastic and Noise Enhanced Methods in Error Correction Decoders

- **Status**: ✅
- **Reason**: 확률적/노이즈증강 디코더 리뷰지만 stochastic decoding·HW회로 구현 등 LDPC BP 디코더에 이식 가능한 구체 기법 다룸(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8625277
- **Type**: conference
- **Published**: 2018
- **Authors**: C. Winstead, T. Tithi, E. Boutillon +1
- **PDF**: https://ieeexplore.ieee.org/document/8625277
- **Abstract**: This paper offers a review of recent developments in non-deterministic error correction decoding methods, which can be described in two broad classes. The first class uses stochastic computation to emulate the arithmetic operations of conventional decoding algorithms. The second class achieves noise enhancement by randomly perturbing the calculations of a standard decoder. Stochastic decoders inherit analysis techniques from the conventional algorithms they emulate, but the noise-enhanced algorithms are newer, more difficult to explain, and not yet fully understood. We describe a Markov chain analysis technique to both explain and optimize noise enhancement in these algorithms. Circuit implementation is also discussed, including both conventional hardware architectures and circuits based on memristor threshold logic, where memristor non-determinism can be exploited for noise enhancement.

## Flash read disturb management using adaptive cell bit-density with in-place reprogramming

- **Status**: ✅
- **Reason**: NAND 플래시 read disturb 관리·cell bit-density·threshold voltage 직접 (카테고리A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8342030
- **Type**: conference
- **Published**: 2018
- **Authors**: T. Wu, Y. Ma, L. Chang
- **PDF**: https://ieeexplore.ieee.org/document/8342030
- **Abstract**: Read disturbance is a circuit-level noise induced by flash read operations. Read refreshing employs data migration to prevent read disturbance from corrupting useful data. However, it costs frequent block erasure under read-intensive workloads. Inspired by software-controlled cell bit-density, we propose to reserve selected threshold voltage levels as guard levels to extend the tolerance of read disturbance. Blocks with guard levels have a low cell bit-density, but they can store frequently read data without frequent read refreshing. We further propose to convert a high-density block into a low-density one using in-place reprogramming to reduce the need for data migration. Our approach reduced the number of blocks erased due to read refreshing by up to 85% and the average read response time by up to 22%.

## Conceiving Extrinsic Information Transfer Charts for Stochastic Low-Density Parity-Check Decoders

- **Status**: ✅
- **Reason**: 확률적(stochastic) LDPC 디코더의 EXIT 차트 수렴분석 신규 모델, 이식 가능 디코더 분석 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8472803
- **Type**: journal
- **Published**: 2018
- **Authors**: A. Pérez-Pascual, A. Hamilton, R. G. Maunder +1
- **PDF**: https://ieeexplore.ieee.org/document/8472803
- **Abstract**: Stochastic low-density parity-check decoders (SLDPCs) have found favor recently both for correcting transmission errors as well as for improving the hardware efficiency. The main drawback of these decoders is that they require hundreds of time periods to decode each frame, but their chip area is smaller than that of their fixed-point counterparts, so they can achieve higher hardware efficiency and may consume less energy. In this paper, we propose a novel extrinsic information transfer chart technique for characterizing the iterative decoding convergence of all the sequences involved in the SLDPC. We have conceived a new model, which takes into consideration not only the sequences exchanged between the decoders but also the sequences generated inside the variable-node decoder (those which are stored in the edge memories). In this way, the model is able to predict the number of decoding iterations required for achieving iterative decoding convergence, as confirmed by own decoder simulations. The proposed technique offers new insights into the operation of SLDPCs, which will facilitate improved designs for the research community.

## Exploiting Locality for Improved Decoding of Binary Cyclic Codes

- **Status**: ✅
- **Reason**: binary cyclic 부호 OSD에 BP 1라운드 삽입 등 디코딩 개선; OSD 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8269402
- **Type**: journal
- **Published**: 2018
- **Authors**: M. N. Krishnan, B. Puranik, P. V. Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/8269402
- **Abstract**: In this paper, we show how the presence of locality within a binary cyclic code can be exploited to improve decoding performance and to reduce decoding complexity. We pursue two approaches. Under the first approach, we show how the ordered statistics decoding (OSD) method can be modified by inserting a simple single round belief-propagation step at the start that involves only the local codes. The resultant locality-aware OSD algorithm yields an appreciable signal-to-noise ratio (SNR) gain for a given level of reliability and essentially the same level of decoder complexity. Under the second, trellis decoding approach, we show that the careful introduction of locality results in the creation of a cyclic subcode that possesses lower maximum state complexity. In addition, we present a simple means of deriving an upper bound to the state complexity profile of any cyclic code that is based only on the zeros of the code. Furthermore, we show how the decoding speed of either locality-aware OSD or trellis decoding can be significantly increased in the presence of locality, in the moderate-to-high SNR regime, by making the use of a quick-look decoder that often returns the maximum likelihood code word.

## Practical MIMO-NOMA: Low Complexity and Capacity-Approaching Solution

- **Status**: ✅
- **Reason**: MIMO-NOMA용 multi-user IRA 채널코드 신규 설계+message-passing 디코더+EXIT 분석, 바이너리 LDPC계열 코드설계/디코더 이식 여지로 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8423459
- **Type**: journal
- **Published**: 2018
- **Authors**: Y. Chi, L. Liu, G. Song +3
- **PDF**: https://ieeexplore.ieee.org/document/8423459
- **Abstract**: MIMO-NOMA combines multiple-input multiple-output (MIMO) and non-orthogonal multiple access (NOMA) techniques to address heterogeneous challenges, such as massive connectivity, low latency, and high reliability in the 5G cellular communication system and beyond. In this paper, a coded MIMO-NOMA system with capacity-approaching performance and low implementation complexity is proposed. Specifically, the proposed MIMO receiver consists of a linear minimum mean-square error (LMMSE) multi-user detector and a bank of single-user message-passing decoders, which decompose the overall NOMA signal recovery into distributed low-complexity computations with iterative processing. An asymptotic extrinsic information transfer analysis is employed to model the overall performance, and a novel class of multi-user irregular repeat-accumulate channel codes that match with the LMMSE multi-user detector in the iterative decoding process are constructed for the system. As a result, the proposed coded MIMO-NOMA system achieves asymptotic performance within 0.2 dB from the theoretical capacity. Simulation results validate the reliability and robustness of the proposed system in practical settings that include different system loads, iteration numbers, code lengths, fast/block fading, and imperfect channel estimation.

## FPGA implementation of Parity Check Matrix based Low Density Parity Check Decoder

- **Status**: ✅
- **Reason**: PCM 기반 LDPC 디코더 FPGA(Verilog) 구현, 병렬 HW 아키텍처로 카테고리 D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8398997
- **Type**: conference
- **Published**: 19-20 Jan.
- **Authors**: H. Praveena, K. Kalyani
- **PDF**: https://ieeexplore.ieee.org/document/8398997
- **Abstract**: Low Density Parity Check (LDPC) error correction decoders have become popular in diverse communication systems, owing to their strong error correction performance and their suitability to parallel hardware implementation. Low Density Parity Check Decoder is a class of Forward Error Correction Codes. The parameterization of a particular LDPC code is defined by its Parity Check Matrix. Parity Check matrix which describes the specific logical combination of the transmitted message bits into parity checks. PCMs are sparse matrices having far more zero entries than nonzero. It allows LDPC codes to be iteratively decoded using a low complexity message passing algorithm. Thus the objective of this project is to implement a PCM based LDPC decoder architecture on FPGA. Initially the components of LDPC decoder are identified then Verilog HDL coding for these components have been written, simulated using Altera Quartus II software. The implementation of these components are done on Altera Cyclone II FPGA kit to improve the error correction performance of communication system.

## Low-Complexity Concatenated LDPC-Staircase Codes

- **Status**: ✅
- **Reason**: 내부 LDPC degree distribution 최적화 + QC 구성 + layered message-passing 디코더 스케줄 + HW친화 — 이식 가능 코드설계(E)/디코더(C)/HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8307171
- **Type**: journal
- **Published**: 15 June15,
- **Authors**: Masoud Barakatain, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/8307171
- **Abstract**: A low-complexity soft-decision concatenated FEC scheme, consisting of an inner LDPC code and an outer staircase code, is proposed. The inner code is tasked with reducing the bit error probability below the outer-code threshold. The concatenated code is obtained by optimizing the degree distribution of the inner-code ensemble to minimize estimated data-flow, for various choices of outer staircase codes. A key feature that emerges from this optimization is that it pays to leave some inner codeword bits completely uncoded, thereby greatly reducing a significant portion of the decoding complexity. The tradeoff between required signal-to-noise ratio and decoding complexity of the designed codes is characterized by a Pareto frontier. Computer simulations of the resulting codes reveals that the net coding-gains of existing designs can be achieved with up to 71% reduction in complexity. A hardware-friendly quasi-cyclic construction is given for the inner codes, which can realize an energy-efficient decoder implementation, and even further complexity reductions via a layered message-passing decoder schedule.
