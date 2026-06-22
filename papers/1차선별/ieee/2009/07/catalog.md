# IEEE Xplore — 2009-07 (1차선별 통과)


## On the Pairwise Error Probability of Linear Programming Decoding on Independent Rayleigh Flat-Fading Channels

- **Status**: ✅
- **Reason**: LP 디코딩 PEP·stopping set 분석, 바이너리 선형부호 디코딩 이론으로 LDPC error floor/디코더 분석에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5075878
- **Type**: journal
- **Published**: July 2009
- **Authors**: Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/5075878
- **Abstract**: In this paper, we consider the pairwise error probability (PEP) of a linear programming (LP) decoder for a general binary linear code as formulated by Feldman  (IEEE Trans. Inf. Theory, Mar. 2005) on an independent (or memoryless) Rayleigh flat-fading channel with coherent detection and perfect channel state information (CSI) at the receiver. Let  ${\bf H}$ be a parity-check matrix of a binary linear code and consider LP decoding based on ${\bf H}$. The output of the LP decoder is always a pseudocodeword. We will show that the PEP of decoding to a pseudocodeword  ${\mmb \omega}$ when the all-zero codeword is transmitted on the above-mentioned channel, behaves asymptotically as $K({\mmb \omega}) \cdot (E_s/N_0)^{-\vert\chi({\mmb \omega})\vert}$, where $\chi({\mmb \omega})$ is the support set of ${\mmb \omega}$, i.e., the set of nonzero coordinates, $E_s/N_0$ is the average signal-to-noise ratio (SNR), and $K({\mmb \omega})$ is a constant independent of the SNR. Note that the support set $\chi({\mmb \omega})$ of ${\mmb \omega}$ is a stopping set. Thus, the asymptotic decay rate of the error probability with the average SNR is determined by the size of the smallest nonempty stopping set in the Tanner graph of  ${\bf H}$. As an example, we analyze the well-known  $(155,64)$ Tanner code and present performance curves on the independent Rayleigh flat-fading channel.

## Identical-capacity channel decomposition for design of universal LDPC codes

- **Status**: ✅
- **Reason**: 채널 분해 기반 universal LDPC 코드 설계(바이너리, E)—NAND의 다양한 채널상태 대응에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165390
- **Type**: journal
- **Published**: July 2009
- **Authors**: Ali Sanaei, Mahdi Ramezani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5165390
- **Abstract**: Design of low-density parity-check (LDPC) codes suitable for all channels which exhibit a given capacity C is investigated. Such codes are referred to as universal LDPC codes. First, based on numerous observations, a conjecture is put forth that a code working on N equal-capacity channels, also works on any convex combination of these N channels. As a supporting evidence, we prove that a code satisfying the stability condition on N channels, also satisfies the stability condition on the convex hull of these N channels. Then, a channel decomposition method is suggested which spans any given channel with capacity C in terms of a number of identical-capacity basis channels. We expect codes that work on the basis channels to be suitable for any convex combination of the bases, i.e., all channels with capacity C. Such codes are found over a wide range of rates. An upper bound on the achievable rate of universal LDPC codes is suggested. Through examples, it is shown that our codes achieve rates extremely close to this upper bound. In comparison with existing LDPC codes designed for a given channel, significant performance gain is reported when codes are used over various channels of equal capacity.

## Design of low-rate irregular LDPC codes using trellis search

- **Status**: ✅
- **Reason**: trellis search로 패리티검사행렬 사이클 분포 개선, structured LDPC 확장(E)—바이너리 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165394
- **Type**: journal
- **Published**: July 2009
- **Authors**: Sang Hyun Lee, Kwang Soon Kim
- **PDF**: https://ieeexplore.ieee.org/document/5165394
- **Abstract**: A simple design method using trellis search is proposed for good low-density parity-check (LDPC) codes with relatively low code rates. By applying a trellis search technique to the design of a pre-assigned part of the parity-check matrix that allows a simple encoding, we improve the distribution of cycles formed by the entries contained in the parity-check part of the parity-check matrix. In addition, we extend the proposed algorithm to a class of structured LDPC codes, which have been recently preferred in many practical applications. Simulation results show that the codes designed by the proposed method outperform those constructed by conventionally used greedy design algorithms.

## Low BER performance estimation of LDPC codes via application of importance sampling to trapping sets

- **Status**: ✅
- **Reason**: trapping set 기반 importance sampling으로 LDPC 저BER/error floor 추정, 코드설계·디코더 평가에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165375
- **Type**: journal
- **Published**: July 2009
- **Authors**: Enver Cavus, Charles L. Haymes, Babak Daneshrad
- **PDF**: https://ieeexplore.ieee.org/document/5165375
- **Abstract**: We introduce an importance sampling (IS) method that successfully simulates the performance of Low density Parity Check (LDPC) Codes in an AWGN channel at very low bit error rates (BERs). By effectively finding and biasing bit node combinations that are the dominant sources of error events, called trapping sets, the developed technique provokes more frequent decoder failures. Consequently, fewer simulation runs and higher simulation gains are achieved.

## Improved random redundant iterative HDPC decoding

- **Status**: ✅
- **Reason**: random redundant 다중 BP 디코더+permutation 기반 SISO 디코딩—부호 비의존 BP 개선 기법(C)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5165392
- **Type**: journal
- **Published**: July 2009
- **Authors**: Ilan Dimnik, Yair Be'ery
- **PDF**: https://ieeexplore.ieee.org/document/5165392
- **Abstract**: An iterative algorithm for soft-input soft-output (SISO) decoding of classical algebraic cyclic block codes is presented below. Inspired by other approaches for high performance belief propagation (BP) decoding, this algorithm requires up to 10 times less computational complexity than other methods that achieve similar performance. By utilizing multiple BP decoders, and using random permutation taken from the permutation group of the code, this algorithm reaches near maximum likelihood performance. A computational complexity comparison of the proposed algorithm versus other methods is presented as well. This includes complexity versus performance analysis, allowing one to trade between the former and the latter, according to ones needs.

## An Area-Efficient LDPC Decoder Architecture and Implementation for CMMB Systems

- **Status**: ✅
- **Reason**: min-sum 비트폭 양자화·인터커넥트 감축 area-efficient LDPC 디코더 HW(C/D)—이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5200039
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Kai Zhang, Xinming Huang, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/5200039
- **Abstract**: This paper presents an area-efficient LDPC decoder architecture for the China multimedia mobile broadcasting (CMMB) standard. Several techniques are adopted to reduce memory size, including the min-sum algorithm (MSA), optimal bit-width quantization of the iterative messages and reduced complexity for the interconnect network. The decoder for the rate-1/2 9216-bit code is implemented using the 90 nm 1.0 V CMOS technology. It achieves the decoding throughput of 48 Mbps at 5 iterations when operating at 60 MHz and the power dissipation is only 34 mW.

## Candidate bit based bit-flipping decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: candidate bit 기반 비트플리핑 하드디시전 디코더, 저복잡도 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205798
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Guiqiang Dong, Yanan Li, Ningde Xie +2
- **PDF**: https://ieeexplore.ieee.org/document/5205798
- **Abstract**: A novel hard-decision decoding algorithm for low-density parity-check (LDPC) codes is proposed in this paper. This algorithm employs the correlation information among the column vectors of the parity-check matrix and syndrome vector for decoding. It does not require soft information, and has low decoding complexity. Simulation results show that the proposed decoding algorithm could provide an effective tradeoff between error performance and decoding complexity.

## Short quasi-cyclic LDPC codes from convolutional codes

- **Status**: ✅
- **Reason**: short QC-LDPC 신규 구성(large girth/min distance, convolutional 표현 탐색) — 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205685
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Roman V. Satyukov +1
- **PDF**: https://ieeexplore.ieee.org/document/5205685
- **Abstract**: We search for good regular quasi-cyclic (QC) LDPC codes with J = 2 ones in each column. In order to simplify the search, QC LDPC codes are represented in the form of tail-biting (TB) convolutional codes. A modified BEAST algorithm is used for finding the free distance (minimum distance) and the girth of both parent convolutional and block LDPC codes. Representations of known bipartite graphs and LDPC based on finite geometries in the form of TB convolutional codes are found. This approach is further generalized for J = 3 QC LDPC codes. Examples of good short LDPC codes with large girth and minimum distance are given. For example, we present a rate 2=5 J = 3 QC LDPC (225, 92)- code with girth 8 and minimum distance 24.

## On the probabilistic computation of the stopping redundancy of LDPC codes

- **Status**: ✅
- **Reason**: LDPC stopping redundancy 계산 알고리즘으로 패리티검사행렬 stopping set 구조 개선. error floor 관련 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205954
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Masanori Hirotomo, Yoshiho Konishi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/5205954
- **Abstract**: On the binary erasure channel (BEC), the performance of low-density parity-check (LDPC) codes decoded by iterative algorithms is estimated by the small stopping sets in the codes. The size of smallest stopping set is called the stopping distance. Since it depends on the structure of parity-check matrix for the code, we can construct the parity-check matrix by adding dependent rows so that the stopping distance is equal to the minimum distance. The stopping redundancy is defined as the smallest number of rows in such a parity-check matrix. In this paper, we propose a probabilistic algorithm for computing the stopping redundancy of LDPC codes. Additionally, we show numerical results of computing the stopping redundancy of (155,64), (504,252) and (1008,504) LDPC codes.

## On the number of minimum weight codewords of SFA-LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 array(SFA) LDPC의 최소가중치 코드워드 수 분석 — 유한길이/구성(E) 관련, 애매하여 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205673
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Yuichi Kaji
- **PDF**: https://ieeexplore.ieee.org/document/5205673
- **Abstract**: The number of minimum weight codewords is an important parameter to measure the potential performance of a linear block code. This paper studies the number of minimum weight codewords of simple and full-length array (SFA) LDPC codes. The notion of a cyclic shift closure is introduced, and it is shown that the set of minimum weight codewords of the code is partitioned by cyclic shift closures of minimum weight codewords. Each cyclic shift closure is generated from a special codeword. With the help of computer experiment, general algebraic forms of the special codewords are determined. As the result, the numbers of minimum weight codewords of several classes of SFA-LDPC codes are clearly expressed by formulas.

## Adaptive turbo equalizer with stopping rule based on LDPC codes

- **Status**: ✅
- **Reason**: LDPC 기반 turbo equalizer의 EXIT chart 조기정지 규칙. 반복디코딩 수렴 모니터링/조기종료는 BP 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205586
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Myung-Kyu Lee, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/5205586
- **Abstract**: In this paper we propose a stopping rule for adaptive turbo equalizers based on low-density parity-check (LDPC) codes. Using an extrinsic information transfer (EXIT) chart, we analyze the convergence behavior of a turbo equalizer and devise an adaptive turbo equalizer with stopping rule. It monitors the status of iterative decoding and stops performing equalization when the decoding messages are reliable enough to converge successfully only by LDPC decoding. Simulation results show that the proposed scheme has lower complexity than the conventional schemes, while it has a similar performance.

## Two-bit message passing decoders for LDPC codes over the binary symmetric channel

- **Status**: ✅
- **Reason**: 2-bit 메시지패싱 디코더(BSC, column-weight-4) 임계값/오류정정 조건 — 저복잡도 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205790
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Lucile Sassatelli, Shashi Kiran Chilappagari, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/5205790
- **Abstract**: A class of two-bit message passing decoders for decoding column-weight-four LDPC codes over the binary symmetric channel is proposed. The thresholds for various decoders in this class are derived using density evolution. For a specific decoder, the sufficient conditions for correcting all error patterns with up to three errors are derived.

## New group shuffled BP decoding algorithms for LDPC codes

- **Status**: ✅
- **Reason**: group shuffled BP 그룹화/스케줄/자가조정 정규화 min-sum 개선 — 이식 가능한 BP 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205781
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Chi-Yuan Chang, Yu-Liang Chen, Chang-Ming Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/5205781
- **Abstract**: Implementing a belief propagation (BP) based LDPC decoder requires high degrees of parallelism using many component soft-in soft-output (SISO) decoding units to perform message passing from variable nodes to check nodes or vice versa. An obvious complexity-reduction solution is to serialize the decoding process, i.e., dividing a decoding iteration into several serial sub-iterations in which a sub-iteration performs only part of the complete parallel message-passing operation. The group horizontal shuffled BP (GHSBP) and vertical shuffled BP (GVSBP) algorithms respectively partition the check and variable nodes of the code graph into groups to perform group-by-group message-passing decoding. This paper proposes new techniques to improve three key elements of a GHSBP decoding algorithm, namely, the grouping method, the decoding schedule and the log-likelihood updating formulae. The (check nodes) grouping method and decoding schedule optimize certain design criterion. The new normalized min-sum updating formula with a self-adjustable correction (scaling) factor offers better nonlinear approximation. Numerical performance of new GHSBP algorithms that include part or all three new techniques indicate that the combination of the proposed grouping and decoding schedule yields a faster convergence rate and our modified min-sum algorithm gives performance superior to that of the conventional min-sum and normalized min-sum algorithm and is very close to that of the sum-product algorithm.

## Analytical solution of covariance evolution for regular LDPC codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC block error 추정용 covariance evolution 해석해. 코드설계(유한길이 성능예측) 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205923
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Takayuki Nozaki, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/5205923
- **Abstract**: The covariance evolution is a system of differential equations with respect to the covariance of the number of edges connecting to the nodes of each residual degree. Solving the covariance evolution, we can derive distributions of the number of check nodes of residual degree 1, which helps us to estimate the block error probability for finite-length LDPC code. Amraoui et al. resorted to numerical computations to solve the covariance evolution. In this paper, we give the analytical solution of the covariance evolution.

## On unequal error protection of finite-length LDPC codes over BECs: A scaling approach

- **Status**: ✅
- **Reason**: 유한길이 LDPC UEP 스케일링 분석(E, 유한길이 코드설계)—애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205356
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Amir H. Djahanshahi, P. H. Siegel, L. B. Milstein
- **PDF**: https://ieeexplore.ieee.org/document/5205356
- **Abstract**: In this paper, we explore a novel approach to evaluate the inherent UEP (unequal error protection) properties of irregular LDPC (low-density parity-check) codes over BECs (binary erasure channels). Exploiting the finite-length scaling methodology, suggested by Amraoui et. al., we introduce a scaling approach to approximate the bit erasure rates of variable nodes with different degrees in the waterfall region of the peeling decoder. Comparing the bit erasure rates obtained from Monte Carlo simulation with the proposed scaling approximations, we demonstrate that the scaling approach provides a close approximation for a wide range of code lengths (between 1000 and 8000). In view of the complexity associated with the numerical evaluation of the scaling approximation, we also derive simpler upper and lower bounds.

## Adaptive decoding of LDPC codes with binary messages

- **Status**: ✅
- **Reason**: 바이너리 메시지 적응형 디코딩+LUT+서브이터레이션 복잡도 절감 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205782
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Ingmar Land, Gottfried Lechner, Lars Rasmussen
- **PDF**: https://ieeexplore.ieee.org/document/5205782
- **Abstract**: A novel adaptive binary decoding algorithm for LDPC codes is proposed, which reduces the decoding complexity while having a comparable or even better performance than corresponding non-adaptive alternatives. In each iteration the variable node decoders use the binary check node decoders multiple times; each single use is referred to as a sub-iteration. To process the sequences of binary messages in each iteration, the variable node decoders employ pre-computed look-up tables. These look-up tables as well as the number of sub-iterations per iteration are dynamically adapted during the decoding process based on the decoder state, represented by the mutual information between the current messages and the syndrome bits. The look-up tables and the number of sub-iterations per iteration are determined and optimized using density evolution. The performance and the complexity of the proposed adaptive decoding algorithm is exemplified by simulations.

## Trapping set analysis of protograph-based LDPC convolutional codes

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC convolutional의 trapping set/error floor 분석 — error floor 예측 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205687
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: David G. M. Mitchell, Ali E. Pusane, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/5205687
- **Abstract**: It has been suggested that ¿near-codewords¿ may be a significant factor affecting decoding failures of LDPC codes over the AWGN channel. A near-codeword is a sequence that satisfies almost all of the check equations. These near-codewords can be associated with so-called `trapping sets' that exist in the Tanner graph of a code. In this paper, we analyse the trapping sets of protograph-based LDPC convolutional codes. LDPC convolutional codes have been shown to be capable of achieving the same capacity-approaching performance as LDPC block codes with iterative message-passing decoding. Further, it has been shown that some ensembles of LDPC convolutional codes are asymptotically good, in the sense that the average free distance grows linearly with constraint length. Here, asymptotic methods are used to calculate a lower bound on the trapping set growth rates for two ensembles of asymptotically good protograph-based LDPC convolutional codes. This can be used to predict where the error floor will occur for these codes under iterative message-passing decoding.

## LDPC decoding and code design on extrinsic trees

- **Status**: ✅
- **Reason**: extrinsic tree 디코딩 + 그에 맞는 패리티검사행렬 설계 — 이식 가능 디코더/코드설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205794
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Eric Psota, Lance C. Perez
- **PDF**: https://ieeexplore.ieee.org/document/5205794
- **Abstract**: Extrinsic tree decoding of low-density parity-check codes operates on modified, finite computation trees created from the Tanner graph of the code. The goal of the extrinsic tree algorithm is to maintain or improve the performance of existing iterative decoders, while providing a decoding algorithm for which upper bounds can be computed. The extrinsic tree algorithm is examined, along with the design of parity-check matrices on which the extrinsic tree decoder performs well.

## On a class of doubly-generalized LDPC codes with single parity-check variable nodes

- **Status**: ✅
- **Reason**: Doubly-generalized LDPC code design (SPC variable nodes, weight-distribution growth-rate analysis) - binary code construction technique transferable (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205731
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Enrico Paolini, Mark F. Flanagan, Marco Chiani +1
- **PDF**: https://ieeexplore.ieee.org/document/5205731
- **Abstract**: A class of doubly-generalized low-density parity-check (D-GLDPC) codes, where single parity-check (SPC) codes are used as variable nodes (VNs), is investigated. An expression for the growth rate of the weight distribution of any D-GLDPC ensemble with a uniform check node (CN) set is presented at first, together with an analytical technique for its efficient evaluation. These tools are then used for detailed analysis of a case study, namely, a rate-1/2 D-GLDPC ensemble where all the CNs are (7, 4) Hamming codes and all the VNs are length-7 SPC codes. It is illustrated how the VN representations can heavily affect the code properties and how different VN representations can be combined within the same graph to enhance some of the code parameters. The analysis is conducted over the binary erasure channel. Interesting features of the new codes include the capability of achieving a good compromise between waterfall and error floor performance while preserving graphical regularity, and values of threshold outperforming LDPC counterparts.

## Analysis of LDPC decoding schedules

- **Status**: ✅
- **Reason**: Analysis of LDPC decoding schedules (serial/message-passing order) for faster convergence - decoder scheduling technique directly transferable (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205776
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Eran Sharon, Noam Presman, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/5205776
- **Abstract**: Schedule is the order of passing messages between vertices of the bipartite graph defining an LDPC code during decoding. Schedules may significantly differ in the rate of decoding convergence. New efficient generalized serial schedules are described and analyzed. They provide significant convergence rate speedup factors compared to previously known schedules. For the proposed schedules, combinatorial and probabilistic analysis is presented, explaining the fast convergence observed in simulations. Using it, LDPC ensembles for which significantly better convergence rates can be obtained are identified.

## Analysis of error floors of LDPC codes under LP decoding over the BSC

- **Status**: ✅
- **Reason**: Error floor analysis under LP decoding over BSC, instanton search algorithm - binary LDPC decoder/error-floor analysis transferable (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205739
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Shashi Kiran Chilappagari, Bane Vasic, Mikhail Stepanov +1
- **PDF**: https://ieeexplore.ieee.org/document/5205739
- **Abstract**: We consider linear programming (LP) decoding of a fixed low-density parity-check (LDPC) code over the binary symmetric channel (BSC). The LP decoder fails when it outputs a pseudo-codeword which is not a codeword. We propose an efficient algorithm termed the instanton search algorithm (ISA) which, given a random input, generates a set of flips called the BSC-instanton and prove that: (a) the LP decoder fails for any set of flips with support vector including an instanton; (b) for any input, the algorithm outputs an instanton in the number of steps upper-bounded by twice the number of flips in the input. We obtain the number of unique instantons of different sizes by running the ISA sufficient number of times. We then use the instanton statistics to predict the performance of the LP decoding over the BSC in the error floor region. We also propose an efficient semi-analytical method to predict the performance of LP decoding over a large range of transition probabilities of the BSC.

## Multi-stage decoding of LDPC codes

- **Status**: ✅
- **Reason**: 양자화/비양자화 BP + MILP 다단 디코딩으로 error floor 개선 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205786
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Yige Wang, Jonathan S. Yedidia, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/5205786
- **Abstract**: In this paper we present a three-stage decoding strategy that combines quantized and un-quantized belief propagation (BP) decoders with a mixed-integer linear programming (MILP) decoder. Each decoding stage is activated only when the preceding stage fails to converge to a valid codeword. The faster BP decoding stages are able to correct most errors, yielding a short average decoding time. Only in the rare cases when the iterative stages fail is the slower but more powerfulMILP decoder used. The MILP decoder iteratively adds binary constraints until either the maximum likelihood codeword is found or some maximum number of binary constraints has been added. Simulation results demonstrate a large improvement in the word error rate (WER) of the proposed multi-stage decoder in comparison to belief propagation. The improvement is particularly noticeable in the low crossover probability (error floor) regime. Through introduction of an accelerated ¿active-set¿ version of the quantized BP decoder we significantly speed up the pace of simulation to simulate low density parity check (LDPC) codes of length up to around 2000 down to a WER of around 10-10 on the binary symmetric channel. We demonstrate that for certain codes our approach can efficiently approach the optimal ML decoding performance for low crossover probabilities.

## Robust initial LLRs for iterative decoders in presence of non-Gaussian noise

- **Status**: ✅
- **Reason**: 비가우시안 노이즈 하 LDPC 디코더용 robust 초기 LLR 설계. NAND의 비가우시안 채널 LLR 양자화/초기화에 직접 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205626
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Arun Ayyar, Michael Lentmaier, K. Giridhar +1
- **PDF**: https://ieeexplore.ieee.org/document/5205626
- **Abstract**: We consider the decoding of LDPC codes in presence of non-Gaussian noise, especially a set of ¿-mixture models. For each of these models, the optimal LLRs are presented. We study the performance degradation due to the use of incorrect LLR in presence of a given noise model. Without modifying the existing LDPC decoder, we propose robust initial LLR which require minimum knowledge about the underlying noise model and are computationally less complex. Since BER simulations are computationally heavy, we use density evolution to compare the thresholds of different LLRs.

## Decreasing error floor in LDPC codes by parity-check matrix extensions

- **Status**: ✅
- **Reason**: Lowering LDPC error floor via parity-check matrix extensions - directly transferable binary code-design technique for error floor (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205738
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Omer Fainzilber, Eran Sharon, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/5205738
- **Abstract**: High error floors in optimized irregular LDPC codes limit their usage in applications that require low error rates. We introduce new methods for lowering the error floor of LDPC codes, based on enhancing the code's parity-check matrix with additional linearly dependent and independent parity-checks. We prove NP hardness of certain optimization problems related to proposed methods and provide upper bound on the number of parity-checks that need to be added. We show that the proposed methods can lower the error floor of the code significantly, by several orders of magnitude, at negligible or no rate penalty.

## On the convergence of iterative belief propagation

- **Status**: ✅
- **Reason**: BP 수렴/L-value 증가가 변수노드 차수로 제한됨을 분석 — LDPC BP 디코더 동작 분석으로 디코더 설계에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5205780
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Axel Heim, Ulrich Sorger
- **PDF**: https://ieeexplore.ieee.org/document/5205780
- **Abstract**: The convergence of iterative decoding schemes utilizing belief propagation is considered. A quantitative bound for the output L-values of a Turbo decoder is given that only depends on the received word and thus is independent from the decoder iterations. Further, it is shown that the exponential increase of the L-values in each iteration within an LDPC decoder is limited by the degree of the variable nodes.

## Quantization for soft-output demodulators in bit-interleaved coded modulation systems

- **Status**: ✅
- **Reason**: LLR 양자화 설계(equiprobable quantizer)로 LDPC 디코더 입력 양자화 기법 NAND read LLR 양자화에 이식 가능(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5206049
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Clemens Novak, Peter Fertl, Gerald Matz
- **PDF**: https://ieeexplore.ieee.org/document/5206049
- **Abstract**: We study quantization of log-likelihood ratios (LLR) in bit-interleaved coded modulation (BICM) systems in terms of an equivalent discrete channel. We propose to design the quantizer such that the quantizer outputs become equiprobable. We investigate semi-analytically and numerically the ergodic and outage capacity over single- and multiple-antenna channels for different quantizers. Finally, we show bit error rate simulations for BICM systems with LLR quantization using a rate 1/2 low-density parity-check code.

## Multi-core platforms for signal processing: source and channel coding

- **Status**: ✅
- **Reason**: 멀티코어/GPU상의 LDPC 디코딩 병렬화 기법—이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5202874
- **Type**: conference
- **Published**: 28 June-3 
- **Authors**: Leonel Sousa, Svetislav Momcilovic, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/5202874
- **Abstract**: In this paper we propose to show how signal processing algorithm designers can understand the nuances of multicore computing engines in order to conveniently exploit these powerful devices. This is illustrated by presenting source and channel coding, two fundamental operations in multimedia signal processing. We describe methods and principles to develop parallel signal processing algorithms to compute motion estimation for advanced video coding, and low-density parity-check code decoding for forward error correction in the channel coding context. The paper will consider general purpose multi-core architectures and accelerators such as the Cell/B.E. and graphics processing units. Experimental evaluation of the multi-core systems allows their performance for signal processing applications to be compared side by side with previous hardware dedicated solutions.

## Optimum LDPC decoder: A memory architecture problem

- **Status**: ✅
- **Reason**: LDPC 디코더 메모리 아키텍처 설계 방법론, 65nm 면적/에너지/지연 탐색; 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5227131
- **Type**: conference
- **Published**: 26-31 July
- **Authors**: Erick Amador, Renaud Pacalet, Vincent Rezard
- **PDF**: https://ieeexplore.ieee.org/document/5227131
- **Abstract**: This paper addresses a frequently overlooked problem: designing a memory architecture for an LDPC decoder. We analyze the requirements to support the codes defined in the IEEE 802.11n and 802.16 e standards. We show a design methodology for a flexible memory subsystem that reconciles design cost, energy consumption and required latency on a multistandard platform. We show results after exploring the design space on a CMOS technology of 65 nm and analyze various use cases from the standardized codes. Comparisons among representative work reveal the benefits of our exploration.

## Simplified receiver for LDPC-Coded interleave-division multiple-access (IDMA) system

- **Status**: ✅
- **Reason**: LDPC-coded IDMA 수신기 디코딩 복잡도 저감(LDPC/반복부호 스위칭); 바이너리 LDPC 디코더 복잡도 트레이드오프 기법 이식 가능성, 애매하므로 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5250566
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Tao Peng, Xiao Yue, Xu He +1
- **PDF**: https://ieeexplore.ieee.org/document/5250566
- **Abstract**: Low density parity check (LDPC) codes can be applied to IDMA system, called LDPC-Coded IDMA System, which is presented recently for combing the advantages of LDPC and IDMA. However, the high complexity for decoding and detection remains a problem. In this paper, a simplified receiver structure is proposed for LDPC-coded IDMA system. The main idea is based on a switch between LDPC and repetition code decoding processing, so as to make a better tradeoff between computational complexity and system performance. Simulation results show that the proposed receiver structure can achieve similar system performance but with reduced complexity by simplifying the processing of LDPC decoding.
