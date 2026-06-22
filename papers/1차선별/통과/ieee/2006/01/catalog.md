# IEEE Xplore — 2006-01 (1차선별 통과)


## Low-density parity-check codes for 40-gb/s optical transmission systems

- **Status**: ✅
- **Reason**: LDPC 디코딩에 출력 시퀀스 PDF 기반 향상 디코딩 알고리즘 제시(C), error floor 분석—NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1668096
- **Type**: journal
- **Published**: July-Aug. 
- **Authors**: I.B. Djordjevic, S. Sankaranarayanan, S.K. Chilappagari +1
- **PDF**: https://ieeexplore.ieee.org/document/1668096
- **Abstract**: In this paper, we compare performance of three classes of forward error correction schemes for 40-Gb/s optical transmission systems. The first class is based on the concatenation of Reed-Solomon codes and this is employed in the state-of-the-art fiber-optics communication systems. The second class is the turbo product codes with Bose-Chaudhuri-Hocquenghen component codes. The application of these codes in optical communication systems was extensively studied by Sab and Lemarie, and Mizuochi The third class is the low-density parity-check (LDPC) codes that have attracted much attention over the past decade. We present enhanced decoding algorithms for Turbo product codes and LDPC codes that use probability density function of output sequences instead of calculating initial likelihood ratios assuming (inaccurate) Gaussian or chi-square approximation. The analysis in this paper shows that the LDPC codes perform better than the other codes in the waterfall region at bit error rates as low as 10-9. We also presented error floors results obtained by analyzing decoding failures of hard-decision iterative decoders

## Dynamics and performance analysis of analog iterative decoding for low-density parity-check (LDPC) codes

- **Status**: ✅
- **Reason**: successive relaxation 기반 반복디코딩 개선, BP/min-sum에 적용해 단부호 성능 향상 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1576950
- **Type**: journal
- **Published**: Jan. 2006
- **Authors**: S. Hemati, A.H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1576950
- **Abstract**: Conventional iterative decoding with flooding or parallel schedule can be formulated as a fixed-point problem solved iteratively by a successive substitution (SS) method. In this paper, we investigate the dynamics of a continuous-time (asynchronous) analog implementation of iterative decoding, and show that it can be approximated as the application of the well-known successive relaxation (SR) method for solving the fixed-point problem. We observe that SR with the optimal relaxation factor can considerably improve the error-rate performance of iterative decoding for short low-density parity-check (LDPC) codes, compared with SS. Our simulation results for the application of SR to belief propagation (sum-product) and min-sum algorithms demonstrate improvements of up to about 0.7 dB over the standard SS for randomly constructed LDPC codes. The improvement in performance increases with the maximum number of iterations, and by accordingly reducing the relaxation factor. The asymptotic result, corresponding to an infinite maximum number of iterations and infinitesimal relaxation factor, represents the steady-state performance of analog iterative decoding. This means that under ideal circumstances, continuous-time (asynchronous) analog decoders can outperform their discrete-time (synchronous) digital counterparts by a large margin. Our results also indicate that with the assumption of a truncated Gaussian distribution for the random delays among computational modules, the error-rate performance of the analog decoder, particularly in steady state, is rather independent of the variance of the distribution. The proposed simple model for analog decoding, and the associated performance curves, can be used as an "ideal analog decoder" benchmark for performance evaluation of analog decoding circuits.

## An innovative low-density parity-check code design with near-Shannon-limit performance and simple implementation

- **Status**: ✅
- **Reason**: routing 문제 제거하는 신규 패리티검사 행렬 설계로 작은 구현면적 - 이식 가능 코드설계/HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1576941
- **Type**: journal
- **Published**: Jan. 2006
- **Authors**: M. Eroz, Feng-Wen Sun, Lin-Nan Lee
- **PDF**: https://ieeexplore.ieee.org/document/1576941
- **Abstract**: A novel parity-check matrix design for low-density parity-check (LDPC) codes is described. By eliminating the routing problem associated with LDPC codes, the design results in a small implementation area, and the codes have outstanding error-rate performance close to the Shannon limit for a wide range of code rates, from 1/4 to 9/10, and for various modulation schemes such as binary phase-shift keying (PSK), quaternary PSK, 8-PSK, 16-amplitude PSK (APSK), and 32-APSK. As a result, LDPC codes designed with this method have been standardized for next-generation digital video broadcasting.

## Efficient encoding of quasi-cyclic low-density parity-check codes

- **Status**: ✅
- **Reason**: QC-LDPC 효율적 인코딩(시프트레지스터 회로) - 이식 가능 코드설계/HW(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1576951
- **Type**: journal
- **Published**: Jan. 2006
- **Authors**: Zongwang Li, Lei Chen, Lingqi Zeng +2
- **PDF**: https://ieeexplore.ieee.org/document/1576951
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes form an important subclass of LDPC codes. These codes have encoding advantage over other types of LDPC codes. This paper addresses the issue of efficient encoding of QC-LDPC codes. Two methods are presented to find the generator matrices of QC-LDPC codes in systematic-circulant (SC) form from their parity-check matrices, given in circulant form. Based on the SC form of the generator matrix of a QC-LDPC code, various types of encoding circuits using simple shift registers are devised. It is shown that the encoding complexity of a QC-LDPC code is linearly proportional to the number of parity bits of the code for serial encoding, and to the length of the code for high-speed parallel encoding.

## An algorithm for counting short cycles in bipartite graphs

- **Status**: ✅
- **Reason**: 이분그래프 단주기(girth, g/g+2/g+4) 카운팅 알고리즘—LDPC 사이클 제거·코드설계(E)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1564444
- **Type**: journal
- **Published**: Jan. 2006
- **Authors**: T.R. Halford, K.M. Chugg
- **PDF**: https://ieeexplore.ieee.org/document/1564444
- **Abstract**: Let G=(U/spl cup/W, E) be a bipartite graph with disjoint vertex sets U and W, edge set E, and girth g. This correspondence presents an algorithm for counting the number of cycles of length g, g+2, and g+4 incident upon every vertex in U/spl cup/W. The proposed cycle counting algorithm consists of integer matrix operations and its complexity grows as O(gn/sup 3/) where n=max(|U|,|W|).

## Programmable LDPC decoder based on the bubble-sort algorithm

- **Status**: ✅
- **Reason**: bubble-sort 기반 프로그래머블 병렬 LDPC 디코더 HW 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1581454
- **Type**: conference
- **Published**: 3-7 Jan. 2
- **Authors**: R. Singhal, Gwan Choi, R.N. Mahapatra
- **PDF**: https://ieeexplore.ieee.org/document/1581454
- **Abstract**: Low density parity check (LDPC) codes are one of the most powerful error correcting codes known. Recent research have pointed out their potential for a low cost, low latency hardware implementation. Due to this property, a lot of research has been done to find their suitability in different communication media. These codes have been shown to achieve near Shannon-limit performance in wireless AWGN channels. At the same time these codes can result in significant power reduction in on-chip global and semi-global interconnects. These different applications demand a variety of LDPC coder decoder structures. This paper presents a programmable design for a parallel implementation of an LDPC decoder. The programmability implies that this decoder can adapt itself to any arbitrary LDPC code for a variety of applications. This paper also presents two example configurations, with a throughput of 2.28 Gbps and 4.37 Gbps respectively.

## High-throughput decoder for low-density parity-check code

- **Status**: ✅
- **Reason**: 메모리 절감 modified min-sum LDPC 디코더 칩 구현, 고처리량 HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1594662
- **Type**: conference
- **Published**: 24-27 Jan.
- **Authors**: T. Ishikawa, K. Shimizu, T. Ikenaga +1
- **PDF**: https://ieeexplore.ieee.org/document/1594662
- **Abstract**: We have designed and implemented the LDPC decoder chip with memory-reduction method to achieve high-throughput and practical chip size. The decoder decodes (3,6)-2304 bit regular LDPC codes using modified min-sum algorithm. The decoder achieves a throughput of 530Mb/s at an operating frequency of 147MHz. The chip has been fabricated in a 0.18mum, 6 metal-layer CMOS technology. The chip size is 36m...

## A high-throughput low-power fully parallel 1024-bit 1/2 -rate low density parity check code decoder in 3D integrated circuits

- **Status**: ✅
- **Reason**: 완전병렬 1024비트 LDPC 디코더 3D IC 구현, 병렬 디코더 HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1594652
- **Type**: conference
- **Published**: 24-27 Jan.
- **Authors**: L. Zhou, C. Wakayama, N. Jangkrajarng +2
- **PDF**: https://ieeexplore.ieee.org/document/1594652
- **Abstract**: A 1024-bit, 1/2 -rate fully parallel low density parity check (LDPC) code decoder has been designed and implemented using a 3D 0.18/spl mu/m fully depleted silicon-on-insulator (FDSOI) CMOS technology based on wafer bonding. The taped-out 3D decoder with about 8M transistors was simulated to have a high throughput of 2Gb/s and a low power consumption of only 430mW using 6.4/spl mu/m by 6.3/spl mu/m of die area. The 3D implementation is estimated to offer more than 10/spl times/ power-delay-area product improvement over its corresponding 2D implementation. This first large-scale 3D ASIC with fine-grain (5/spl mu/m) vertical interconnects is made possible by jointly developing a complete automated 3D design flow from a commercial 2D design flow combined with the needed 3D-design point tools.

## Particle Filtering for Iterative Data and Phase Estimation

- **Status**: ✅
- **Reason**: binary LDPC 대상 메시지패싱 기반 phase 추정(particle filtering); 부호 비의존 디코더 기법으로 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1661088
- **Type**: conference
- **Published**: 2006
- **Authors**: D. Le Ruyet, T. Bertozzi, N. Paul
- **PDF**: https://ieeexplore.ieee.org/document/1661088
- **Abstract**: In this paper we consider the iterative decoding of channels with strong phase noise. We propose to estimate the phase using a message passing algorithm based on particle filtering. Instead of estimating the phase directly we use the whole estimated probability density function for the channel decoder. Three versions of phase estimators are derived. The simulation results are given for binary LDPC codes. We compare the proposed iterative data and phase estimators with another solution where the forward backward algorithm is performed over the trellis obtained from the discretization of the phase. The results show that the proposed algorithm achieves a good compromise between performances and complexity

## Connecting Belief Propagation with Maximum Likelihood Detection

- **Status**: ✅
- **Reason**: BP 정류점을 ML 검출과 연결하는 이론. 유한길이·루프 그래프 LDPC BP 디코더 이해 개선 가능성, 애매하여 살림(Phase 3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5755809
- **Type**: conference
- **Published**: 2006
- **Authors**: J. M. Walsh, P. A. Regalia
- **PDF**: https://ieeexplore.ieee.org/document/5755809
- **Abstract**: While its performance in the Gaussian, infinite block length, and loopless factor graph cases are well understood, the breakthrough applications of the belief propagation algorithm to the decoding of turbo and LDPC codes involve finite block lengths, finite alphabets, and factor graphs with loops. It has been shown in these instances that the stationary points of the belief propagation decoder are the critical points of the Bethe approximation to the free energy. However, this connection does not clearly explain why the stationary points of belief propagation yield good performance, since the approximation is not in general exact when there are loops in the graph. We introduce an alternate constrained maximum likelihood optimization problem here which analytically connects the stationary points of belief propagation with the maximum likelihood sequence detector.

## Computational Performance of Various Formulations of the Iterative Soft-Decision Decoder Algorithm

- **Status**: ✅
- **Reason**: LDPC soft-decision BP 디코더의 여러 수식 구현 비교 + 계산상 더 나은 새 formulation 제안 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4036258
- **Type**: conference
- **Published**: 2006
- **Authors**: R. Moberly, M. O'Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/4036258
- **Abstract**: Multiple formulations of the soft-decision decoding algorithm have been published based upon Gallagher's foundational work on LDPC codes (R. Gallager, 1962) and Pearl's iterative belief-propagation (1988). Three published formulations are mathematically identical but differ computationally. A formulation is proposed that is computationally better than the established ones. A visualization strategy is introduced to describe the formulations

## Sub Graph Approach In Iterative Sum-Product Algorithm

- **Status**: ✅
- **Reason**: sum-product 알고리즘 sub-graph 스케줄링으로 수렴 가속. 부호 비의존적 BP 스케줄링 기법, 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5755871
- **Type**: conference
- **Published**: 2006
- **Authors**: M. F. Bayramoglu, A. O. Yilmaz, B. Baykal
- **PDF**: https://ieeexplore.ieee.org/document/5755871
- **Abstract**: A new scheduling algorithm to the iterative sum-product algorithm, which is called sub-graph scheduling, will be presented in this paper. The propesed algorithm provides a schedule which has a higher convergence rate than the iterative sum-product algorithm while keeping the complexity of one iteration withot degrading the performance. Our method also gives an explanation to the fact that turbo decoders have faster convergence rate than LDPC decoders.

## Advanced Channel Decoding Algorithms and Their Implementation for Future Communication Systems

- **Status**: ✅
- **Reason**: Turbo/LDPC 디코더 설계공간·코드설계-아키텍처 통합방법론 논의(DVB-S2 LDPC 디코더 HW), 이식 가능 디코더 HW 관점(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1602408
- **Type**: conference
- **Published**: 2006
- **Authors**: N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/1602408
- **Abstract**: Today’s information society demands access to huge amount of data anywhere and data any time. Hence wireless communications is a key technology. In such systems bandwidth and transmission power are critical resources. Thus advanced communications systems have to rely on sophisticated error correction schemes (FEC). Turbo- and LDPC codes belong to the most efficient error correction schemes known by now. However the iterative decoding nature of these codes imply big implementation challenges w.r.t. throughput, latency and low energy. Moreover future communication systems require flexibility. Thus we have to tradeoff flexibility versus implementation costs. In this talk we discuss the design space for Turboand LDPC decoders and compare different implementation alternatives. Moreover we show the need of a design methodology which have to consider code-design and architecture development in a unified way. We discuss this challenge on the base of 3GPP Turbodecoders and DVB-S2 LDPC decoders.

## Full-Information Rate Distance-4 Block Codes

- **Status**: ✅
- **Reason**: lowest-density quasi-cyclic regular 생성행렬 블록코드 구성; QC 저밀도 코드설계 기법 검토 여지(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4362403
- **Type**: conference
- **Published**: 2006
- **Authors**: G. Altay, O. N. Ucan, N. Altay
- **PDF**: https://ieeexplore.ieee.org/document/4362403
- **Abstract**: A new linear block code construction technique is proposed [1]. It generates all the even codes of length greater than 8 with full information rate for Hamming distance-4. The codes generated by the proposed method include the extended Hamming codes and the Reed Muller codes of distance-4. The generator matrix has useful properties such as lowest density, quasi-cyclic and regular.

## Optimal Soft Symbol Split Methods and Performance Analysis for Applying to Multilevel Modulation of Iterative Codes

- **Status**: ✅
- **Reason**: 다중레벨 변조 소프트심볼 분할 LLR 간소화(Euclidean/MAX/Sector) — LLR 계산 저복잡도 근사로 약하게 이식 여지, 애매하여 Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4023105
- **Type**: conference
- **Published**: 2006
- **Authors**: J. H. Jeong, D. G. Choi, M. H. Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4023105
- **Abstract**: This paper presents bit splitting methods to apply multilevel modulation to iterative codes such as turbo code, low density parity check code and turbo product code. Log-likelihood ratio method splits multilevel symbols to soft decision symbols using the received in-phase and quadrature component based on Gaussian approximation. However it is too complicate to calculate and to implement hardware due to exponential and logarithmic calculation. Therefore this paper presents Euclidean, MAX and Sector method to reduce the high complexity of LLR method. Also, this paper proposes optimal soft symbol split method for three kind of iterative codes

## A Reliability-Based Reed-Solomon Decoding Algorithm for Magnetic Recording Channels

- **Status**: ✅
- **Reason**: adaptive BP를 부분 LDPC 패리티검사에 적용한 Chase형 디코딩; BP 디코더 기법 검토 여지(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4262224
- **Type**: conference
- **Published**: 2006
- **Authors**: H. Xia, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/4262224
- **Abstract**: A simplification of the adaptive belief propagation (BP) algorithm used for decoding Reed-Solomon (RS) codes for magnetic recording channels which leads to a Chase-type algorithm is presented. The BP algorithm has been used to decode a partly low-density parity-check matrix of an RS code.

## Pattern Dependent Noise Predictive Belief Propagation

- **Status**: ✅
- **Reason**: Noise-predictive BP, 4-cycle-free 팩터그래프 병렬구조 BP 기법; 메시지패싱 개선 이식 가능성(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4261731
- **Type**: conference
- **Published**: 2006
- **Authors**: M. N. Kaynak, T. M. Duman, E. M. Kurtas
- **PDF**: https://ieeexplore.ieee.org/document/4261731
- **Abstract**: Inter-symbol interference (ISI) channels are encountered in many applications, including magnetic recording and wireless communication systems. In general maximum a-posteriori (MAP) or maximum likelihood (ML) algorithms are used for channel detection. Recently, iterative belief propagation (BP) algorithm is proposed for channel detection as well. When factor graph of the ISI channel is length 4 cycle free, BP gives a similar performance with the MAP detector, while it has the advantage of parallel structure leading to advantages in read channel architectures. Unlike ISI channels with white noise, for magnetic recording systems, noise is correlated and data (pattern) dependent. Correlation is a result of partial response (PR) equalization and data dependence is a result of the media noise (jitter).

## Iterative Soft-Input Soft-Output Decoding of Reed–Solomon Codes by Adapting the Parity-Check Matrix

- **Status**: ✅
- **Reason**: 패리티검사행렬을 sparse하게 적응시켜 SPA 적용하는 RS SISO 디코딩; 적응형 패리티검사 sparse화 메시지패싱 기법이 부호 비의존적, 예외 포함(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1661852
- **Type**: journal
- **Published**: 2006
- **Authors**: J. Jiang, K. R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1661852
- **Abstract**: An iterative algorithm is presented for soft-input soft-output (SISO) decoding of Reed-Solomon (RS) codes. The proposed iterative algorithm uses the sum-product algorithm (SPA) in conjunction with a binary parity-check matrix of the RS code. The novelty is in reducing a submatrix of the binary parity-check matrix that corresponds to less reliable bits to a sparse nature before the SPA is applied at each iteration. The proposed algorithm can be geometrically interpreted as a two-stage gradient descent with an adaptive potential function. This adaptive procedure is crucial to the convergence behavior of the gradient descent algorithm and, therefore, significantly improves the performance. Simulation results show that the proposed decoding algorithm and its variations provide significant gain over hard-decision decoding (HDD) and compare favorably with other popular soft-decision decoding methods

## Gear-Shift Decoding

- **Status**: ✅
- **Reason**: LDPC용 gear-shift 반복 메시지패싱 디코더로 디코딩 지연 최소화, HW 파이프라인 최적화 적용 가능한 C/D 이식 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1643543
- **Type**: journal
- **Published**: 2006
- **Authors**: M. Ardakani, F. R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1643543
- **Abstract**: This paper considers a class of iterative message-passing decoders for low-density parity-check codes in which the decoder can choose its decoding rule from a set of decoding algorithms at each iteration. Each available decoding algorithm may have different per-iteration computation time and performance. With an appropriate choice of algorithm at each iteration, overall decoding latency can be reduced significantly, compared with standard decoding methods. Such a decoder is called a gear-shift decoder because it changes its decoding rule (shifts gears) in order to guarantee both convergence and maximum decoding speed (minimum decoding latency). Using extrinsic information transfer charts, the problem of finding the optimum (minimum decoding latency) gear-shift decoder is formulated as a computationally tractable dynamic program. The optimum gear-shift decoder is proved to have a decoding threshold equal to or better than the best decoding threshold among those of the available algorithms. In addition to speeding up software decoder implementations, gear-shift decoding can be applied to optimize a pipelined hardware decoder, minimizing hardware cost for a given decoder throughput.
