# IEEE Xplore — 2009-12 (1차선별 통과)


## An efficient dynamic schedule for layered belief-propagation decoding of LDPC codes

- **Status**: ✅
- **Reason**: layered BP의 동적 스케줄(NWRBP+lazy 결합)로 LDPC 수렴/오류성능 개선, 바이너리 LDPC 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5353273
- **Type**: journal
- **Published**: December 2
- **Authors**: Guojun Han, Xingcheng Liu
- **PDF**: https://ieeexplore.ieee.org/document/5353273
- **Abstract**: An efficient dynamic schedule for layered belief-propagation (LBP) decoding of low-density parity-check (LDPC) codes is presented, in which the check nodes connecting to a variable node with maximum relative message residual are chosen in each dynamic decoding iteration, and then LBP is performed for these check nodes. In this schedule we combined the features of lazy schedule and node-wise residual belief propagation (NWRBP) together while keeping the extra computational complexity very low. Simulation results show that the new schedule speeds up the convergence rate and greatly improves error performance at medium to high signal-to-noise ratio (SNR) when compared to the standard LBP decoding algorithm.

## Two reliability-based iterative majority-logic decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: 신규 reliability-based iterative majority-logic 디코더(논리연산+정수가산, 단순 HW) — C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351656
- **Type**: journal
- **Published**: December 2
- **Authors**: Q. Huang, J. Kang, L. Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/5351656
- **Abstract**: This paper presents two novel reliability-based iterative majority-logic decoding algorithms for LDPC codes. Both algorithms are binary message-passing algorithms and require only logical operations and integer additions. Consequently, they can be implemented with simple combinational logic circuits. They either outperform or perform just as well as the existing weighted bit-flipping or other reliability-based iterative decoding algorithms for LDPC codes in error performance with a faster rate of decoding convergence and less decoding complexity. Compared to the sum-product algorithm for LDPC codes, they offer effective trade-offs between performance and decoding complexity.

## Iterative Decoding using Eigenmessages

- **Status**: ✅
- **Reason**: Eigenmessage 기반 BP 변형 디코더(사이클 비국소성 처리)로 바이너리 LDPC 디코딩에 적용, 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5351658
- **Type**: journal
- **Published**: December 2
- **Authors**: Todd K. Moon, John S. Crockett, Jacob H. Gunther +1
- **PDF**: https://ieeexplore.ieee.org/document/5351658
- **Abstract**: The eigenmessage approach to iterative decoding introduces a degree of nonlocality into a belief propagation decoder by representing an entire set of messages around a cycle of the Tanner graph as a linear operator. The eigenvector for the operator represents a fixed point of the belief propagation algorithm around a cycle, with incident messages fixed. A multiple eigenmessage approach is also presented, in which messages around several cycles are simultaneously expressed. The eigenmessage approach may be applied to any graph with cycles, but we demonstrate its use on LDPC decoding. In this setting, computational results compare eigenmessage methods with conventional belief propagation decoding showing, using simulation and EXIT charts, that the eigenmessage approaches slightly reduce the number of decoder iterations compared to belief propagation decoding while preserving the probability of error of conventional decoding.

## Combined normalized and offset min-sum decoding over partial response channels

- **Status**: ✅
- **Reason**: normalized+offset min-sum 결합 디코더 알고리즘 제안(C), 부호 비의존적이며 NAND LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5397609
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: Mahdi Shaghaghi, Yong Liang Guan, Kui Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/5397609
- **Abstract**: In this paper, the combined normalized and offset min-sum algorithm is proposed for efficient decoding of low-density parity-check (LDPC) codes in optical and magnetic storage systems. The proposed algorithm can be considered as a general case of the normalized and offset algorithms, and offers better BER performance compared to them. The performance improvement is presented for a partial response magnetic recording channel. Our simulations are based on an LDPC code from the class of finite-geometry LDPC codes. It will be shown that the proposed method has a performance very close to that of the belief propagation algorithm which has a much higher complexity.

## Differentiating trapping sets with the same label [w; u]

- **Status**: ✅
- **Reason**: 불규칙 LDPC의 trapping set 차별화 기법 제안(error floor 관련, E), NAND error floor 분석에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5397616
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: X. Zheng, Francis C. M. Lau, C. K. Tse
- **PDF**: https://ieeexplore.ieee.org/document/5397616
- **Abstract**: Trapping sets (TSs) have been known to contribute to errors in the decoding of low-density parity-check (LDPC) codes, particularly at the high signal-to-noise ratio (SNR) region. Moreover, TSs with the same label [w; u] are considered equivalent under the automorphism of the graph of a regular code. But according to our our simulations, TSs with the same label [w; u] are producing different error rates in the case of irregular codes. In this paper, we will identify and explain the cause of the differences in error rates for TSs with the same label. Further, we will propose a simple mechanism to differentiate these TSs.

## Optimized decoding schedule for irregular LDPC codes

- **Status**: ✅
- **Reason**: C: irregular LDPC용 최적화 디코딩 스케줄(수렴 가속), 이식 가능 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5522026
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Xuwei Chen, Hui Yu, Youyun Xu
- **PDF**: https://ieeexplore.ieee.org/document/5522026
- **Abstract**: Recently, the concept of layered decoding schedule for Low-Density Parity-Check codes has been introduced. But the advantage of layered decoding schedule for irregular LDPC codes is not as obvious as regular LDPC codes. The major drawback of the layered irregular LDPC codes versus the layered regular LDPC codes is its comparative low convergence decoding speed. Simulation results show that different bit node degrees of irregular LDPC codes significantly contribute to the decoding performance. The decoding performance of bit nodes with different degrees is of great difference. Bit nodes with small degrees always converge slower than larger ones. In this paper, we propose an optimized decoding schedule for irregular LDPC codes to accelerate the decoding convergence rate. Meanwhile, for the irregular LDPC decoder, the faster decoding speed means a higher throughput and almost the same error performance.

## Efficient construction of irregular LDPC codes with midterm block length and nearly optimal performance

- **Status**: ✅
- **Reason**: E: 유한/중간길이 irregular LDPC 구성법(PEG+Downhill Simplex), 바이너리 코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5522079
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Qingwen Jin, Pengjun Wang, Shuzheng Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/5522079
- **Abstract**: In this paper, we propose a general method for constructing irregular LDPC codes with midterm or short block lengths. It is a Monte-Carlo simulation based optimization procedure called Downhill Simplex which uses PEG (Progressive Edge Growth) method for Tanner graph construction in cost function evaluations. It outperforms DE (Density Evolution) method in both efficiency and performance. The efficiency of our proposal mostly depends on the Monte-Carlo simulation time which due to the midterm block lengths is relatively small compared to the time delay of conventional DE method. Simulation results show that for block length of 3200 and a relatively low code rate 3/8, LDPC codes constructed using our proposal noticeably outperform those constructed with DE method by more than 0.2dB in the entire SNR range under AWGN channel.

## Leveraging reliable bits: ECC design considerations for practical secure biometric systems

- **Status**: ✅
- **Reason**: 신뢰도 기반 비트 재배치 후 고차수 변수노드에 매핑+신뢰도 초기화 디코딩 — 부호 비의존 디코더 기법, 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5386479
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Yige Wang, Shantanu Rane, Anthony Vetro
- **PDF**: https://ieeexplore.ieee.org/document/5386479
- **Abstract**: It is well-known that a biometric fuzzy vault can be constructed by applying an error correcting code (ECC) to a biometric signal. This is attractive because authentication only requires the check bits of the ECC to be stored on the access control device, whereas the personal biometric traits need not be stored. For a given coding rate, the ECC attempts to correct the errors between an enrollment biometric and the provided probe, and authenticates if it is successful in doing so. Unfortunately, most implementations of biometric fuzzy vaults have very poor robustness to the inherent noisiness of biometric measurements. In this paper, we provide ECC design considerations for secure biometric systems, which provide both better robustness and greater security. In particular, for any feature extraction algorithm, we propose to reorder the feature bits according to their reliability, and associate the reliable bits with high-degree variable nodes in the graph of the ECC. Further, the reliability of a bit is measured at enrollment and used to initialize the ECC decoding. Experiments on an extensive database show considerable reduction in the false reject rate, while restricting the successful attack rate to a very low value.

## Sparse Decoding of Low Density Parity Check Codes Using Margin Propagation

- **Status**: ✅
- **Reason**: margin propagation으로 SP 디코더 log-sum-exp 근사하는 신규 저전력 디코더, 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5425585
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Ming Gu, Kiran Misra, Hayder Radha +1
- **PDF**: https://ieeexplore.ieee.org/document/5425585
- **Abstract**: One of the key factors underlying the popularity of Low-density parity-check (LDPC) code is its iterative decoding algorithm that is amenable to efficient hardware implementation. Even though different variants of LDPC iterative decoding algorithms have been studied for its error-correcting properties, an analytical basis for evaluating energy efficiency of LDPC decoders has not been reported. In this paper, we present a framework of a parameterized LDPC decoding algorithm that can be optimized to produce sparse representation of communication messages used in iterative decoding. The sparsity of messages is determined by its differential entropy and has been used as a theoretical metric for determining the energy efficiency of an iterative LDPC decoder. At the core of the proposed algorithm is margin propagation (MP) which approximates the log-sum-exp function used in conventional sum-product (SP) decoders by a piecewise linear (PWL) function. Using Monte-Carlo simulations, we demonstrate that the MP decoding leads to a significant reduction in message entropy compared to a conventional SP decoder, while incurring a negligible performance penalty (less than 0.03 dB). The proposed work therefore lays the foundation for design of parameterized LDPC decoders whose bit-error-rate performance can be effectively traded-off with respect to different energy efficiency constraints as required by different set of applications.

## Conflict Resolution by Matrix Reordering for DVB-T2 LDPC Decoders

- **Status**: ✅
- **Reason**: DVB-T2 layered LDPC 디코더 메모리 충돌 해결 행렬재정렬, 바이너리 LDPC HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5425755
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Cedric Marchand, Jean-Baptiste Dore, Laura Conde-Canencia +1
- **PDF**: https://ieeexplore.ieee.org/document/5425755
- **Abstract**: Layered decoding is known to provide efficient and high-throughput implementation of LDPC decoders. However, the implementation of the layered architecture is not always straightforward because of the memory access conflicts in the a-posteriori information memory. In this paper, we focus our attention on a particular type of conflict introduced by the existence of multiple diagonal matrices in the DVB-T2 parity check matrix structure. We illustrate how the reordering of the matrix reduces the number of conflicts, at the cost of limiting the level of parallelism. We then propose a parity extending process to solve the remaining conflicts. Fixed point simulation results show coherent performance without modifying the layered architecture.

## LDPC Decoding Strategies for Two-Dimensional Magnetic Recording

- **Status**: ✅
- **Reason**: 2D 자기기록용 binary error-erasure 채널 LP 디코딩 제안, BP와 비교 — 이식 가능한 LP 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5425930
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Anantha Raman Krishnan, Rathnakumar Radhakrishnan, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/5425930
- **Abstract**: In this paper, we propose a linear programming (LP) decoding scheme for binary error-erasure channel for use in two-dimensional magnetic recording. We compare the performance of this decoding scheme with other decoding schemes like LP decoding for BSC and belief-propagation decoding. Also, we compare the effect of variance of grain-area in the medium on the bit-error rates of various decoding schemes.

## Efficient Ranking of Rate-Compatible Puncturing Patterns for a Given LDPC Code Matrix

- **Status**: ✅
- **Reason**: rate-compatible 펑처링 패턴 랭킹 신규 기준, 바이너리 LDPC 코드 설계 적용(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5425627
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Sissi X. Wu, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/5425627
- **Abstract**: In this paper, we introduce a novel criterion to rank puncturing patterns for rate-compatible LDPC codes. Specifically, based on Gaussian approximation density evolution, a cost function is devised to characterize the degree distribution of the punctured code matrices, which are derived from a mother code matrix by matrix transformation. This cost function allows us to effectively compare the expected performance of candidate puncturing patterns and to sort out good ones. Combined with well-designed search algorithms, the proposed criterion can be applied on both standardized block-LDPC codes and generic binary LDPC codes to get good puncturing patterns with manageable complexity. Numerical simulation results verify the effectiveness of the proposed ranking criterion, and demonstrate that a series of good rate-compatible LDPC codes can be obtained by the proposed ranking criterion.

## Undetected Errors in Quasi-Cyclic LDPC Codes Caused by Receiver Symbol Slips

- **Status**: ✅
- **Reason**: QC-LDPC에서 symbol slip로 인한 undetected error 분석 및 저비용 완화책 제시 — QC-LDPC 코드설계/검출 기법으로 이식 가능(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5425765
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Alexander Kaiser, Sam Dolinar, Michael K. Cheng
- **PDF**: https://ieeexplore.ieee.org/document/5425765
- **Abstract**: Low-density parity-check (LDPC) codes are capacity-approaching forward error correction codes that operate at signal-to-noise ratio (SNR) decoding thresholds very near to the capacity limits. Receivers designed for less optimal codes might not function smoothly at the lower values of SNR where LDPC codes can operate. In particular, an artifact of low-SNR receiver operation is the increased probability of symbol slips. Receiver synchronization errors resulting from symbol insertions or deletions can cause unexpected decoder problems, especially for an LDPC code with a quasi-cyclic construction. In this paper we analyze the theoretical basis for symbol slips to cause undetected errors with quasi-cyclic codes, and we demonstrate these effects via simulations. We also examine several no-cost to low-cost solutions that can mitigate these effects.

## Pivoting Algorithms for Maximum Likelihood Decoding of LDPC Codes over Erasure Channels

- **Status**: ✅
- **Reason**: erasure 채널 LDPC ML 디코딩 pivoting 알고리즘(구조적 Gaussian elimination 개선) — 스토리지 erasure ECC 디코더 기법(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5426289
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Gianluigi Liva, Balazs Matuz, Enrico Paolini +1
- **PDF**: https://ieeexplore.ieee.org/document/5426289
- **Abstract**: This paper investigates efficient maximum-likelihood (ML) decoding algorithms for low-density parity-check (LDPC) codes over erasure channels. In particular, enhancements to a previously proposed structured Gaussian elimination approach are presented. The improvements are achieved by developing a set of algorithms, here referred to as pivoting algorithms, aiming to limit the average number of reference variables (or pivots) from which the erased symbols can be recovered. Four pivoting algorithms are compared, which exhibit different trade-offs between the complexity of the pivoting phase and the average number of pivots. Numerical results on the performance of LDPC codes under ML erasure decoding complete the analysis, confirming that a near-optimum performance can be obtained with an affordable decoding complexity, up to very high data rates. For example, for one of the presented algorithms, a software implementation has been developed, which is capable to provide data rates above 1.5 Gbps on a commercial computing platform.

## A Relaxed Half-Stochastic Iterative Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: Relaxed Half-Stochastic LDPC 디코더 신규 알고리즘+error floor 저감+저복잡도 HW, 바이너리 LDPC 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5425510
- **Type**: conference
- **Published**: 30 Nov.-4 
- **Authors**: Francois Leduc-Primeau, Saied Hemati, Warren J. Gross +1
- **PDF**: https://ieeexplore.ieee.org/document/5425510
- **Abstract**: This paper presents a Relaxed Half-Stochastic (RHS) low-density parity-check (LDPC) decoding algorithm that uses some elements of the sum-product algorithm (SPA) in its variable nodes, but maintains the low-complexity interleaver and check node structures characteristic of stochastic decoders. The algorithm relies on the principle of successive relaxation to convert binary stochastic streams to a log-likelihood ratio (LLR) representation. Simulations of a (2048, 1723) RS-LDPC code show that the RHS algorithm can outperform 100-iterations floating-point SPA decoding. We describe approaches for low-complexity implementation of the RHS algorithm. Furthermore, we show how the stochastic nature of the belief representation can be exploited to lower the error floor.

## Reduced-Comlexity Decoding of LDPC Codes Using TAP Approach

- **Status**: ✅
- **Reason**: LLR-BP, BP-Based, λ-min 알고리즘을 TAP 관점으로 단순화하는 디코더 알고리즘 연구(C, NAND LDPC에 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5632325
- **Type**: conference
- **Published**: 29 Nov.-4 
- **Authors**: Manel Abdelhedi, Omessaad Hamdi, Ammar Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/5632325
- **Abstract**: Low-density parity-check (LDPC) codes are based on random construction. Because of this randomness, it is not easy to analyze them with the traditional methods of information theory. N. Sourlas was the first to point out that LDPC codes have a similarity with Ising spin systems of statistical physics. Besides, it has been shown that the Belief-Propagation algorithm, the LDPC codes decoding algorithm, is equivalent to the Thouless-Anderson-Palmer(TAP) approach. In this paper, we develop the log likelihood ratios-Belief Propagation (LLR-BP) algorithm and its simplifications the BP-Based algorithm and the λ-min algorithm with the TAP approach.

## A Quasi-Parallel Encoder of Quasi-Cyclic LDPC Codes in IEEE 802.16e

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 HW 아키텍처(시프트레지스터, FPGA, 양방향 재귀)—이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5455700
- **Type**: conference
- **Published**: 26-28 Dec.
- **Authors**: Zhuo Ma, Ying Li, Xinmei Wang
- **PDF**: https://ieeexplore.ieee.org/document/5455700
- **Abstract**: We present a quasi-parallel LDPC encoder based on the quasi-cyclic characteristic of the parity check matrix of the LDPC code in IEEE 802.16e. A bidirectional recursion Arithmetic is used to improve its timing requires. The encoder is designed with simple shift registers and mod-2 adders, which is easy to be implemented in FPGA. By taking into account of some intermediate results, a low cost, high performance encoder is realized. The results show that, for the half rate LDPC code with code length 2304, the designed encoder can work at 50 MHz on Xilinx's XC3S1000 FPGA, With total equivalent gates consumes of 65964 and encoding throughput of up to kb*50 Mb/s.

## A Low-Complexity Layered Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: 저복잡도 layered 디코딩 알고리즘, VN 연산 ~60% 감소 — 부호 비의존 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5384575
- **Type**: conference
- **Published**: 25-27 Dec.
- **Authors**: Wang Zhongxun, Mu Qing
- **PDF**: https://ieeexplore.ieee.org/document/5384575
- **Abstract**: A Low-complexity Layered Decoding Algorithm for LDPC Codes is proposed. Our modified algorithm reduces the number of operations in variable nodes to lower LDPC decoder power consumption. The modified parts of LDPC decoder architecture is also described. Simulation results show that comparing with SPA and MSA, our algorithm reducing the number of operations nearly to 60% with little performance los...

## A reduced complexity message passing algorithm with improved performance for LDPC decoding

- **Status**: ✅
- **Reason**: 하드결정 기반에 소프트 채널정보 활용한 저복잡도 LDPC 메시지패싱 알고리즘 개선 - 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5407173
- **Type**: conference
- **Published**: 21-23 Dec.
- **Authors**: Vikram Arkalgud Chandrasetty, Syed Mahfuzul Aziz
- **PDF**: https://ieeexplore.ieee.org/document/5407173
- **Abstract**: In this paper, a simplified message passing algorithm for decoding low-density parity-check (LDPC) codes is proposed with a view to reduce the implementation complexity. The algorithm is based on simple hard-decision decoding techniques while utilizing the advantages of soft channel information for improvement in decoder performance. The algorithm has been validated through simulation using LDPC code compliant with wireless local area network (WLAN -IEEE 802.11n) standard. The results show that the proposed algorithm can achieve significant improvement in bit error rate (BER) performance and average decoding iterations compared to fully hard-decision based decoding algorithms.

## A general decoding framework for high-rate LDPC codes

- **Status**: ✅
- **Reason**: 고율 LDPC용 범용 디코더 HW(message packing 인터커넥션 네트워크) - 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5403795
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: S. M. Ehsan Hosseiniy, Wang Ling Goh, Kheong Sann Chan
- **PDF**: https://ieeexplore.ieee.org/document/5403795
- **Abstract**: This paper presents a hardware solution to the design of general low-density parity-check (LDPC) decoders, which simplifies the delivery network required by the message passing algorithm. While many designs of LDPC decoders for specific classes of codes exist in the literature, the design of a general LDPC decoder capable of supporting random LDPC codes is still challenging. The method proposed in this paper tries to pack different check node (CN) and variable node (VN) messages in the Tanner graph representation of the LDPC code, and is therefore called message packing. This method takes advantage of the fact that for high-rate LDPC's the CN's degree is much larger than the VN's, and two distinct methods for delivering the messages to the CNs and VNs are proposed. Using the proposed interconnection network (IN) results in lower complexity decoding of LDPC codes when compared to other designs.

## A high-performance multibit-flipping algorithm for LDPC decoding

- **Status**: ✅
- **Reason**: 다중비트 플리핑 LDPC 디코딩 알고리즘(low correlation search, culprit vote) - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5403898
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/5403898
- **Abstract**: For LDPC decoding, bit-flipping (BF) algorithms are much simpler than the min-sum algorithms (MSA). However, BF algorithms have the disadvantages of poorer performances and higher iteration counts than MSA. This paper introduces the concepts of low correlation search and culprit vote to further improve the efficiency of the existing BF algorithms. High decoding performances and low iteration number are achieved by flipping those bits with low correlation as much as possible and introducing an additional syndrome vote procedure. As a result, the proposed algorithm can achieve significant decoding performance which is very close to the min-sum algorithm (MSA) but with much lower computation complexity.
