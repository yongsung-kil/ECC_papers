# IEEE Xplore — 2014-07 (1차선별 통과)


## Reduced-Complexity Min-Sum Algorithm for Decoding LDPC Codes With Low Error-Floor

- **Status**: ✅
- **Reason**: 새 reduced-complexity min-sum 변형(second-min emulation, iteration-dependent correction), error-floor 분석, FPGA/CMOS layered decoder — C/D 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6742731
- **Type**: journal
- **Published**: July 2014
- **Authors**: Fabián Angarita, Javier Valls, Vicenç Almenar +1
- **PDF**: https://ieeexplore.ieee.org/document/6742731
- **Abstract**: This paper proposes a low-complexity min-sum algorithm for decoding low-density parity-check codes. It is an improved version of the single-minimum algorithm where the two-minimum calculation is replaced by one minimum calculation and a second minimum emulation. In the proposed one, variable correction factors that depend on the iteration number are introduced and the second minimum emulation is simplified, reducing by this way the decoder complexity. This proposal improves the performance of the single-minimum algorithm, approaching to the normalized min-sum performance in the water-fall region. Also, the error-floor region is analyzed for the code of the IEEE 802.3an standard showing that the trapping sets are decoded due to a slow down of the convergence of the algorithm. An error-floor free operation below BER=10-15 is shown for this code by means of a field-programmable gate array (FPGA)-based hardware emulator. A layered decoder is implemented in a 90-nm CMOS technology achieving 12.8 Gbps with an area of 3.84 mm2.

## Modified tree structure approach for finding the first two minimum values

- **Status**: ✅
- **Reason**: min-sum 디코더 체크노드에서 1·2위 최소값 탐색용 MTS 기법으로 비교횟수·HW 비용 감소 — 부호 비의존적 디코더/HW 기법, 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6889306
- **Type**: conference
- **Published**: 9-13 July 
- **Authors**: Weiwei Cui, Yi Yang, Xueqin Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/6889306
- **Abstract**: In the min-sum decoding algorithm of low-density parity-check (LDPC) codes, for a given set of input values to one check node, efficient approaches for finding the first and the second minimum values are greatly needed for the low complexity decoder. In this paper, based on the tree structure (TS) approach, we propose the modified TS (MTS) approach, which requires less number of comparisons to find the first and the second minimum values. Therefore, the hardware cost of the proposed MTS approach is lower than that of the TS approach.

## High speed LDPC decoder design based on general overlapped message-passing architecture

- **Status**: ✅
- **Reason**: non-QC LDPC용 GOMP 오버랩 메시지패싱 디코더+cycle bus로 처리량 2배, HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6876832
- **Type**: conference
- **Published**: 8-11 July 
- **Authors**: Baihong Lin, Qi Li, Yukui Pei +2
- **PDF**: https://ieeexplore.ieee.org/document/6876832
- **Abstract**: The design of high speed decoders with traditional partly parallel architecture for non-quasi-cycle (NQC) LDPC codes is a challenging problem due to its high memory-block consumption and the low hardware utilization efficiency. In this paper, a general overlapped message passing (GOMP) decoding algorithm is proposed to improve the hardware utilization efficiency (HUE), which overcomes the limitation of overlapped message passing (OMP) decoders proposed before. On the basis of the given codes, this algorithm nearly doubles the throughput without sacrificing double memory or causing loss in performance compared to BP algorithm. Furthermore, we present a technique called cycle bus to reduce the number of block RAMs in the multi-core decoder. Moreover, an example of a rate-2/3, length-15360 irregular LDPC code with 8.43 dB coding gain for BPSK in AWGN channel is given, whose decoders features nearly double throughput, 22.22% increase in memory 8.35% reduction in logic registers cost and more reasonable distribution in block RAMs cost.

## An application of generalized belief propagation: splitting trapping sets in LDPC codes

- **Status**: ✅
- **Reason**: GBP로 LDPC trapping set 분할해 error-floor 영역 디코딩 개선 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874924
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Jean-Christophe Sibel, Sylvain Reynal, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6874924
- **Abstract**: Generalized belief propagation (GBP) is known to be a well-suited technique for approximate inference problems in loopy factor graphs. It can absorb problematic subgraphs inside regions to reduce their influence on the inference. However, the choice of regions to be used in GBP remains a delicate issue. This paper proposes an approach to create specific regions when dealing with Low-Density Parity-Check (LDPC) codes. We split trapping sets, known to degrade the decoding performance, to make GBP locally optimal. Experiments show that GBP can then perform better than BP, especially in the error-floor region.

## Quasi-cyclic LDPC codes on two arbitrary sets of a finite field

- **Status**: ✅
- **Reason**: 유한체 기반 QC-LDPC 구성(girth8+)과 저복잡도 반복 디코더 제시 — 바이너리 코드설계(E)/디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875275
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6875275
- **Abstract**: This paper presents a simple and flexible method for constructing QC-LDPC codes based on two arbitrary sets of a finite field. Based on this method, a high-rate, high-performance and very low error-floor QC-LDPC code is first constructed and then a class of rate-1/2 QC-LDPC codes whose Tanner graphs have girth 8 or larger is presented. Also presented is a reduced-complexity iterative decoding algorithm for QC-LDPC codes.

## An upper bound on the minimum distance of array low-density parity-check codes

- **Status**: ✅
- **Reason**: Minimum-distance upper bound for binary array (QC-)LDPC codes via template support matrix; code-design analysis relevant to QC-LDPC construction (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875416
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Eirik Rosnes, Marcel Adrian Ambroze, Martin Tomlinson
- **PDF**: https://ieeexplore.ieee.org/document/6875416
- **Abstract**: In this work, we present an upper bound on the minimum distance of array low-density parity-check (LDPC) codes. An array LDPC code is a quasi-cyclic LDPC code specified by two integers q and m, where q is an odd prime and m ≤ q. In the literature, the minimum distance of these codes (denoted by d(q,m)) has been thoroughly studied for m ≤ 5. Both exact results, for small values of q and m, and general (i.e., independent of q) bounds have been established. For m ≤ 6, the best known minimum distance upper bound, derived by Mittelholzer (IEEE Int. Symp. Inf. Theory, Jun./Jul. 2002), is d(q, 6) ≤ 32. In this work, we derive an improved upper bound of d(q, 6) ≤ 20 by using the concept of a template support matrix of a codeword. The bound is tight with high probability in the sense that we have not been able to find codewords of strictly lower weight for several values of q using a minimum distance probabilistic algorithm. Finally, we provide new specific minimum distance results for m ≤ 6 and low-to-moderate values of q ≤ 79.

## On the error-correcting capabilities of low-complexity decoded irregular LDPC codes

- **Status**: ✅
- **Reason**: Error-correcting capability lower bound for irregular binary LDPC with low-complexity iterative decoder via Tanner graph; decoder/code analysis portable (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875418
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Pavel Rybin
- **PDF**: https://ieeexplore.ieee.org/document/6875418
- **Abstract**: This paper deals with the irregular binary low-density parity-check (LDPC) codes with the constituent single parity check (SPC) codes and the error-correcting iterative low-complex decoding algorithm. The lower bound on the error fraction, guaranteed corrected by the considered iterative algorithm, was obtained for the irregular LDPC code for the first time in this paper. This lower bound was obtained as a result of analysis of Tanner graph representation of irregular LDPC code. The number of decoding iterations, required to correct the errors, is a logarithmic function of the code length. The numerical results, obtained at the end of the paper for proposed lower bound achieved similar results for the previously known best lower-bounds for regular LDPC codes and were represented for the first time for the irregular LDPC codes.

## On the upper bound on undetected error probability for LDPC code

- **Status**: ✅
- **Reason**: Undetected error probability estimation for binary LDPC under BP/iterative decoding; decoder-side analysis technique portable to binary LDPC (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875417
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Pavel Rybin, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/6875417
- **Abstract**: This paper deals with the method of undetected error probability estimation for a low-density parity-check (LDPC) code under any given iterative decoding algorithm. We propose such modification of a given iterative decoding algorithm, that almost preserves a decoding failure exponent and decoding complexity of this algorithm. We obtain the upper bound on the undetected error probability for the modified algorithm. We show how to use the proposed method to estimate the undetected error probability of LDPC code under the belief propagation (BP) algorithm at the end of this paper.

## An improved ensemble of variable-rate LDPC codes with precoding

- **Status**: ✅
- **Reason**: precoding 적용 rate-compatible LDPC(Kite) 구성 — 바이너리 가변율 코드 설계(E) 이식 가능, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875219
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Min Zhu, Yucheng Qu, Kai Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/6875219
- **Abstract**: In this paper, we apply the precoding technique developed by Abbasfar et al. for ARA codes to the original rate-compatible LDPC codes introduced in [1] to obtain an improved ensemble of variable-rate LDPC codes, which perform universally well over the AWGN channel in the low to high code-rate region. The proposed codes will be named precoded Kite codes. The Extrinsic Information Transfer (EXIT) chart is used to optimize the code performance. Numerical results show that the precoded Kite codes can achieve a coding gain of up to 0.3 dB over the codes in [1]. A performance comparison is also made between the proposed codes and the Raptor codes over the AWGN channel. It is shown that the proposed codes outperform the Raptor codes universally in a wide code rate range over AWGN channels. Extensive simulation results confirm that precoded Kite codes perform close to capacity within a range of code rates from 0.1 to 0.9.

## Absorbing set characterization of array-based spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC 흡수집합(absorbing set) 특성 분석 — error floor/사이클 제거 코드설계(E)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874960
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: David G.M. Mitchell, Lara Dolecek, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/6874960
- **Abstract**: Absorbing sets are combinatorially defined objects existing in the Tanner graph of a low-density parity-check (LDPC) code that have been shown to cause failures in the iterative message-passing decoder when transmission occurs over the additive white Gaussian noise channel. In this paper, we study the absorbing set properties of a class of high-rate array-based spatially coupled LDPC (SC-LDPC) codes that are constructed by coupling together L array-based LDPC block codes. We prove that the smallest absorbing sets existing in the Tanner graph of the SC-LDPC code have the same size as those in the corresponding uncoupled LDPC codes, and the number of such sets grow linearly with L. We show that spatial coupling greatly reduces the average number (per symbol) of minimal sets compared to the uncoupled codes, and we explain that this reduction is due to many absorbing sets and small cycles being `broken' by the coupling process. The large reduction in the number of minimal absorbing sets suggests that array-based SC-LDPC codes will have significantly improved decoding performance in the high signal-to-noise ratio regime compared to the corresponding uncoupled LDPC codes.

## Design of non-precoded protograph-based LDPC codes

- **Status**: ✅
- **Reason**: protograph 기반 LDPC 신규 설계(차분진화, 낮은 반복 디코딩 임계값) — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875340
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Hironori Uchikawa
- **PDF**: https://ieeexplore.ieee.org/document/6875340
- **Abstract**: A new family of protograph-based codes with no punctured variable nodes is presented. The codes are constructed by using differential evolution, partial brute force search, and the lengthening method introduced by Nguyen et al.. The protograph ensembles satisfy the linear minimum distance growth property and have the lowest iterative decoding thresholds yet reported in the literature among protograph codes without punctured variable nodes. Simulation results show that the new codes perform better than state-of-the-art protograph codes when the number of decoding iterations is small.

## Adaptive linear programming decoding of polar codes

- **Status**: ✅
- **Reason**: Adaptive cut-generation LP decoding on sparse factor graph + reduced factor graph; LP/projection technique is code-agnostic and portable to binary LDPC BP/LP decoding (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875381
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Veeresh Taranalli, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6875381
- **Abstract**: Polar codes are high density parity check codes and hence the sparse factor graph, instead of the parity check matrix, has been used to practically represent an LP polytope for LP decoding. Although LP decoding on this polytope has the ML-certificate property, it performs poorly over a BAWGN channel. In this paper, we propose modifications to adaptive cut generation based LP decoding techniques and apply the modified-adaptive LP decoder to short block-length polar codes over a BAWGN channel. The proposed decoder provides significant FER performance gain compared to the previously proposed LP decoder and its performance approaches that of ML decoding at high SNRs. We also present an algorithm to obtain a smaller factor graph from the original sparse factor graph of a polar code. This reduced factor graph preserves the small check node degrees needed to represent the LP polytope in practice. We show that the fundamental polytope of the reduced factor graph can be obtained from the projection of the polytope represented by the original sparse factor graph and the frozen bit information. Thus, the LP decoding time complexity is decreased without changing the FER performance by using the reduced factor graph representation.

## Design of unstructured and protograph-based LDPC coded continuous phase modulation

- **Status**: ✅
- **Reason**: 프로토그래프/비정형 LDPC 코드설계(degree-1/2 노드 패턴, threshold 최적화) — CPM 응용이나 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875180
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Tarik Benaddi, Charly Poulliat, Marie-Laure Boucheret +2
- **PDF**: https://ieeexplore.ieee.org/document/6875180
- **Abstract**: In this paper, we derive an asymptotic analysis and optimization of coded CPM systems using both unstructured and protograph-based LDPC codes ensembles. First, we present a simple yet effective approach to design unstructured LDPC codes : by inserting partial interleavers between LDPC and CPM, and allowing degree-1 and degree-2 variable nodes in a controlled pattern, we show that designed codes perform that can operate very close to the maximum achievable rates. Finally, the extension to protograph based codes is discussed. We provide some simple rules to design good protograph codes with good threshold properties.

## LDPC convolutional codes versus QC LDPC block codes in communication standard scenarios

- **Status**: ✅
- **Reason**: QC-LDPC BC와 LDPC-CC 비교, degree distribution/girth 최적화 및 저복잡도 인코딩 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875339
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Rolf Johannesson
- **PDF**: https://ieeexplore.ieee.org/document/6875339
- **Abstract**: Outstanding asymptotical performance demonstrated by low-density parity-check (LDPC) convolutional codes (CC) makes them strong competitors with respect to quasi-cyclic (QC) LDPC block codes (BC) currently used in a variety of communication standards. However, typically communication standards, for example, DVB-S2 or WIMax standards impose rather serious restrictions on the structure of the employed codes. These restrictions are related to different implementation issues such as existence of low-complexity encoding and decoding, short decoding delay etc. Two scenarios are considered. In one scenario, short-delay and low-complexity constraints are taken into account. In the other scenario, the complexity requirement is relaxed. Both LDPC CCs and QC LDPC BCs with optimized degree distribution and girth profile, which enable low-complexity encoding, are constructed for these scenarios. Having both delay and complexity constraints yields QC LDPC BCs that outperform the LDPC CCs. In this scenario LDPC CCs play an important role mostly for constructing tailbiting QC LDPC BCs. On the other hand, assuming only a decoding delay constraint the LDPC CCs can be superior compared to the QC LDPC BCs at the relatively low signal-to-noise ratio region. Moreover, under practically acceptable decoding delays also the LDPC CCs with low-complexity encoding structure beat records in approaching the Shannon limit. A new LDPC CC is presented achieving the BER 10-7 with decoding delay 96000 bits at 0.62 dB, that is, performing only about 0.43 dB from the Shannon limit.

## Spatially-coupled MacKay-Neal codes with no bit nodes of degree two achieve the capacity of BEC

- **Status**: ✅
- **Reason**: degree-2 변수노드 제거로 error floor 개선하는 바이너리 SC-LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874884
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Takuya Okazaki, Kenta Kasai
- **PDF**: https://ieeexplore.ieee.org/document/6874884
- **Abstract**: Obata et al. proved that spatially-coupled (SC) MacKay-Neal (MN) codes achieve the capacity of BEC. However, the SC-MN codes have many variable nodes of degree two and have higher error floors. In this paper, we prove that SC-MN codes with no variable nodes of degree two achieve the capacity of BEC.

## Check-hybrid GLDPC codes: Systematic elimination of trapping sets by super checks

- **Status**: ✅
- **Reason**: super check로 trapping set 체계적 제거하는 GLDPC 구성 — 바이너리 LDPC error floor 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874923
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Vida Ravanmehr, David Declercq, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/6874923
- **Abstract**: In this paper, we propose a new approach to constructing a class of check-hybrid generalized low-density parity-check (GLDPC) codes which are free of small trapping sets. This approach is based on converting selected checks of an LDPC code involving a trapping set to super checks corresponding to a shorter error correcting component code. In particular, we follow two goals in constructing the check-hybrid GLDPC codes: First, the super checks are replaced based on the knowledge of trapping sets of the global LDPC code. We show that by converting only some single checks to super checks the decoder corrects the errors on a trapping set and hence eliminates the trapping set. Second, the number of super checks required for eliminating certain trapping sets is minimized to reduce the rate-loss. We first give an algorithm to find a set of critical checks in a trapping set of an LDPC code and then we provide some upper bounds on the minimum number of critical checks needed to eliminate certain trapping sets in the parity-check matrix of an LDPC code. A possible fixed set for a class of check-hybrid codes is also given.

## Analyzing finite-length protograph-based spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: 프로토그래프 SC-LDPC 유한길이 스케일링 법칙·peeling 디코딩 분석 — 바이너리 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874961
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Markus Stinner, Pablo M. Olmos
- **PDF**: https://ieeexplore.ieee.org/document/6874961
- **Abstract**: The peeling decoding for spatially coupled low-density parity-check (SC-LDPC) codes is analyzed for a binary erasure channel. An analytical calculation of the mean evolution of degree-one check nodes of protograph-based SC-LDPC codes is given and an estimate for the covariance evolution of degree-one check nodes is proposed in the stable decoding phase where the decoding wave propagates along the chain of coupled codes. Both results are verified numerically. Protograph-based SC-LDPC codes turn out to have a more robust behavior than unstructured random SC-LDPC codes. Using the analytically calculated parameters, the finite-length scaling laws for these constructions are given and verified by numerical simulations.

## Noise modeling and capacity analysis for NAND flash memories

- **Status**: ✅
- **Reason**: NAND 플래시 노이즈 모델링·용량 분석, soft cell-level/동적 임계값 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875236
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Qing Li, Anxiao Jiang, Erich F. Haratsch
- **PDF**: https://ieeexplore.ieee.org/document/6875236
- **Abstract**: Flash memories have become a significant storage technology. However, they have various types of error mechanisms, which are drastically different from traditional communication channels. Understanding the error models is necessary for developing better coding schemes in the complex practical settings. This paper endeavors to survey the noise and disturbs in NAND flash memories, and construct channel models for them. The capacity of flash memory under these models is analyzed, particularly regarding capacity degradation with flash operations, the trade-off of sub-thresholds for soft cell-level information, and the importance of dynamic thresholds.

## Efficient maximum-likelihood decoding of linear block codes on binary memoryless channels

- **Status**: ✅
- **Reason**: 선형블록코드 ML 디코딩 분기한정 알고리즘, (155,64) Tanner LDPC 벤치마크 사용 — LDPC에 이식 가능한 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875302
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Michael Helmling, Eirik Rosnes, Stefan Ruzika +1
- **PDF**: https://ieeexplore.ieee.org/document/6875302
- **Abstract**: In this work, we consider efficient maximum-likelihood decoding of linear block codes for small-to-moderate block lengths. The presented approach is a branch-and-bound algorithm using the cutting-plane approach of Zhang and Siegel (IEEE Trans. Inf. Theory, 2012) for obtaining lower bounds. We have compared our proposed algorithm to the state-of-the-art commercial integer program solver CPLEX, and for all considered codes our approach is faster for both low and high signal-to-noise ratios. For instance, for the benchmark (155, 64) Tanner code our algorithm is more than 11 times as fast as CPLEX for an SNR of 1.0 dB on the additive white Gaussian noise channel. By a small modification, our algorithm can be used to calculate the minimum distance, which we have again verified to be much faster than using the CPLEX solver.

## Improving code diversity on block-fading channels by spatial coupling

- **Status**: ✅
- **Reason**: SC-LDPC 다이버시티 향상(coupling memory)+슬라이딩윈도우 디코더 — 바이너리 SC 구성/디코더(E/C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875246
- **Type**: conference
- **Published**: 29 June-4 
- **Authors**: Najeeb ul Hassan, Michael Lentmaier, Iryna Andriyanova +1
- **PDF**: https://ieeexplore.ieee.org/document/6875246
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are considered for transmission over the block-fading channel. The diversity order of the SC-LDPC codes is studied using density evolution and simulation results. We demonstrate that the diversity order of the code can be increased, without lowering the code rate, by simply increasing the coupling parameter (memory) of a SC-LDPC code. For a (3,6)-regular SC-LDPC code with rate R = 1=2 and memory mcc = 4 a remarkable diversity of d = 10 is achieved without the need for any specific code structure. The memory of the SC-LDPC codes makes them robust against a non-stationary mobile-radio environment. The decoding of SC-LDPC codes using a latency constrained sliding window decoder is also considered.

## A Cost-Effective and Reliable Cloud Storage

- **Status**: ✅
- **Reason**: 분산 스토리지용 LDPC, localized property 가진 신규 ECC 설계 — 스토리지 ECC(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6973838
- **Type**: conference
- **Published**: 27 June-2 
- **Authors**: Yongmei Wei, Yong Wee Foo
- **PDF**: https://ieeexplore.ieee.org/document/6973838
- **Abstract**: The project aims to provide a scalable, reliable and cost effective cloud storage solution based on a Low Density Parity Check (LDPC) code-based framework. The novelties of the project lie in the following aspects. Firstly, the proposed framework utilizes a new technique called dynamic parameterization so that the existing resources can be used more efficiently. Secondly, a tailored error correction code with localized property is specifically designed to minimize the cost occurred during encoding and decoding for the distributed storage system. Thirdly, a neuroevolution approach is proposed, combining artificial neural network learning algorithm with evolutionary method, to develop predictive models for dynamic resource allocation and performance optimization.

## Dynamic write-level and read-level signal design for MLC NAND flash memory

- **Status**: ✅
- **Reason**: A. MLC NAND 플래시 직접—동적 write/read-level 전압 설계, 양자화 레벨(LLR 양자화 관련) 신규 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6923850
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Chaudhry Adnan Aslam, Yong Liang Guan, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/6923850
- **Abstract**: In this paper, we propose dynamic write-level and read-level voltage scheme for MLC NAND flash memory. We study the characteristics of flash channel which can be modeled as mixture of Uniform and Exponential distribution. Since this channel shows non-stationary behavior, we present probability of error analysis and introduce the concept of dynamically adjusting the verify-level (write-level) and quantization-level (read-level) voltage values over varying flash channel. The proposed dynamic voltage based method outperforms fixed verify-level voltage scheme. We demonstrate improvements in bit-error-rate (BER) performance and cell storage capacity for the proposed signal design scheme.

## Failure analysis of two-bit flipping decoding algorithms

- **Status**: ✅
- **Reason**: BSC상 바이너리 LDPC용 two-bit flipping 디코더의 trapping set 분석/error floor 개선 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6983914
- **Type**: conference
- **Published**: 22-25 July
- **Authors**: Bane Vasić, Dung Viet Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/6983914
- **Abstract**: We consider a class of bit flipping algorithms for low-density parity-check codes over the binary symmetric channel in which one additional bit at a variable and check nodes is employed. For these two-bit flipping algorithms, we give and illustrate through examples a recursive procedure for finding all uncorrectable error patters and corresponding induced subgraphs, referred as a trapping set profile. This procedure is used to select a small collection of good algorithms that in a decoding diversity approach, run in parallel or serial, outperform Gallager A/B, min-sum and sum product algorithm in the error floor region.

## Modified greedy permutation algorithm for low complexity encoding in LDPC codes

- **Status**: ✅
- **Reason**: SALT/ALT 기반 sparse 행렬 저복잡도 인코딩 기법 — 코드/인코더 설계 이식 가능성, 애매하여 살림(Phase 3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6992981
- **Type**: conference
- **Published**: 10-11 July
- **Authors**: B Rajasekar, E Logashanmugam
- **PDF**: https://ieeexplore.ieee.org/document/6992981
- **Abstract**: The low-density parity-check (LDPC) codes are used to achieve excellent performance with low encoding and decoding complexity. One major criticism concerning LDPC codes has been their apparent high encoding complexity and memory inefficient nature due to large parity check matrix. More generally, we consider the encoding problem for codes specified by sparse parity-check matrices. We show how to exploit the sparseness of the parity-check matrix to obtain efficient encoders. A new technique for efficient encoding of LDP Codes based on the known concept of approximate lower triangulation (ALT) is introduced. The algorithm computes parity check symbols by solving a set of sparse equations, and the triangular factorization is employed to solve the equations efficiently. The key of the encoding method is to get the systematic approximate lower triangular (SALT) form of the Parity Check Matrix with minimum gap g, because the smaller the gap is, the more efficient encoding will be obtained. The functions are to be coded in MATLAB.
