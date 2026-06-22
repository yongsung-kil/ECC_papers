# IEEE Xplore — 2008-07 (1차선별 통과)


## Construction of Regular Quasi-Cyclic Protograph LDPC Codes Based on Vandermonde Matrices

- **Status**: ✅
- **Reason**: Vandermonde 기반 정규 QC protograph 바이너리 LDPC 구성(girth>=6), HW친화 인코딩/디코딩 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4389049
- **Type**: journal
- **Published**: July 2008
- **Authors**: Nicholas Bonello, Sheng Chen, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/4389049
- **Abstract**: In this paper, we investigate the attainable performance of quasi-cyclic (QC) protograph low-density parity-check (LDPC) codes for transmission over both additive white Gaussian noise and uncorrelated Rayleigh channels. The presented codes are constructed using the Vandermonde matrix and thus have a girth of at least six in their corresponding Tanner graph. Furthermore, they also benefit from both low-complexity encoding and decoding, low memory requirements, as well as hardware-friendly implementations. Our simulation results demonstrate that the advantages offered by this family of QC protograph LDPC codes accrue with no compromise in the attainable bit error ratio (BER) and block error ratio (BLER) performances. In fact, it is also shown that despite their implementational benefits, the proposed codes exhibit slight BER/BLER gains when compared to some of their more complex counterparts of the same length.

## Switch-Type Hybrid Hard Decision Decoding Algorithms for Regular Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 정규 LDPC용 switch-type 하이브리드 경판정 디코딩(NSS) 신규 알고리즘 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4544955
- **Type**: journal
- **Published**: July 2008
- **Authors**: Gong Chen, Liu Qi, Cui Huijuan +1
- **PDF**: https://ieeexplore.ieee.org/document/4544955
- **Abstract**: This correspondence presents the switch strategies for switch-type hybrid hard decision decoding algorithms for regular low-density parity-check (LDPC) codes. After the piecewise analysis of extrinsic information transfer functions for Gallager decoding algorithm B (GB), the normalized switch scheme (NSS), for which the majority-based algorithms and GB are two examples, is proposed. Then, several other examples of NSSs are presented and their convergence properties are analyzed based on the extrinsic information transfer (EXIT) functions. In simulations, the proposed NSSs show meaningful performance improvements and less sensitivity to channel parameter underestimations compared with GB for small and moderate block length codes.

## Bypass Decoding: A Reduced-Complexity Decoding Technique for LDPC-Coded MIMO-OFDM Systems

- **Status**: ✅
- **Reason**: LLR 임계 기반 bypass 디코딩으로 LDPC 디코더 복잡도 저감 — 부호 비의존적 디코더 기법으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4382921
- **Type**: journal
- **Published**: July 2008
- **Authors**: Yan Xin, Syed Aon Mujtaba, Tong Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4382921
- **Abstract**: In this paper, we propose a simple reduced-complexity decoding technique called bypass decoding for low-density parity-check (LDPC)-coded multiple-input-multiple-output (MIMO) orthogonal frequency-division multiplexing (OFDM) systems. Employing the bypass decoding technique, the receiver of an LDPC-coded MIMO-OFDM system decodes a codeword in two steps based on the log-likelihood ratios (LLRs) of coded bits. The hard decisions are first made on the coded bits whose LLRs have magnitudes above a certain threshold, and the rest of the coded bits will next be decoded by using an iterative receiver. We show that, as long as the threshold is properly selected, the bypass decoding technique not only delivers considerable complexity reductions but also maintains a comparable performance in LDPC-coded MIMO-OFDM transmissions. We also provide a selection rule for choosing a suitable threshold and show its effectiveness by simulations.

## Implementation aspects of LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC convolutional 코드 저복잡도 디코딩/HW 구현 전략 — 디코더+HW 기법(C/D), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4568447
- **Type**: journal
- **Published**: July 2008
- **Authors**: Ali Emre Pusane, Alberto Jimenez Feltstrom, Arvind Sridharan +3
- **PDF**: https://ieeexplore.ieee.org/document/4568447
- **Abstract**: Potentially large storage requirements and long initial decoding delays are two practical issues related to the decoding of low-density parity-check (LDPC) convolutional codes using a continuous pipeline decoder architecture. In this paper, we propose several reduced complexity decoding strategies to lessen the storage requirements and the initial decoding delay without significant loss in performance. We also provide bit error rate comparisons of LDPC block and LDPC convolutional codes under equal processor (hardware) complexity and equal decoding delay assumptions. A partial syndrome encoder realization for LDPC convolutional codes is also proposed and analyzed. We construct terminated LDPC convolutional codes that are suitable for block transmission over a wide range of frame lengths. Simulation results show that, for terminated LDPC convolutional codes of sufficiently large memory, performance can be improved by increasing the density of the syndrome former matrix.

## Sequential message-passing decoding of LDPC codes by partitioning check nodes

- **Status**: ✅
- **Reason**: 체크노드 분할 순차 메시지패싱 디코딩 — 수렴 빠른 신규 BP 변형(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4568441
- **Type**: journal
- **Published**: July 2008
- **Authors**: Sunghwan Kim, Min-Ho Jang, Jong-Seon No +2
- **PDF**: https://ieeexplore.ieee.org/document/4568441
- **Abstract**: In this paper, we analyze the sequential message- passing decoding algorithm of low-density parity-check (LDPC) codes by partitioning check nodes. This decoding algorithm shows better bit error rate (BER) performance than the conventional message-passing decoding algorithm, especially for the small number of iterations. Analytical results indicate that as the number of partitioned subsets of check nodes increases, the BER performance is improved. We also derive the recursive equations for mean values of messages at check and variable nodes by using density evolution with a Gaussian approximation. From these equations, the mean values are obtained at each iteration of the sequential decoding algorithm and the corresponding BER values are calculated. They show that the sequential decoding algorithm converges faster than the conventional one. Finally, the analytical results are confirmed by the simulation results.

## Asymptotically good LDPC convolutional codes based on protographs

- **Status**: ✅
- **Reason**: protograph 기반 LDPC convolutional 코드 구성과 free distance 분석; 바이너리 LDPC 코드설계(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595143
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: David G. M. Mitchell, Ali E. Pusane, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4595143
- **Abstract**: LDPC convolutional codes have been shown to be capable of achieving the same capacity-approaching performance as LDPC block codes with iterative message-passing decoding. In this paper, asymptotic methods are used to calculate a lower bound on the free distance for several ensembles of asymptotically good protograph-based LDPC convolutional codes. Further, we show that the free distance to constraint length ratio of the LDPC convolutional codes exceeds the minimum distance to block length ratio of corresponding LDPC block codes.

## Improved bilayer LDPC codes using irregular check node degree distribution

- **Status**: ✅
- **Reason**: bilayer LDPC 부호 설계에 비정규 체크노드 차수분포·density evolution 적용한 신규 코드설계 기법(E), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4594964
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Marwan H. Azmi, Jinhong Yuan, Jun Ning +1
- **PDF**: https://ieeexplore.ieee.org/document/4594964
- **Abstract**: This paper presents an improved LDPC code design for decode-and-forward relay system. Our design is based on the recent work of bilayer LDPC code structures.We introduce an irregular check node degree distribution for the lower and hyper (overall) bilayer LDPC code Tanner graphs. We derive the exact relationship between the lower and hyper graphs in terms of degree distributions (node perspective). This relationship acts as constraint to perform the density evolution. We apply the differential evolution algorithm to search for the best degree distribution for both bilayer-lengthened and bilayer-expurgated LDPC codes. We show that the performance gap of the codes is within 0.07595dB and 0.28407dB from the theoretical limits.

## Two-edge type LDPC code ensembles with exponentially few codewords with linear small weight

- **Status**: ✅
- **Reason**: two-edge/multi-edge type LDPC 앙상블의 최소거리 선형증가 조건 도출; 바이너리 코드설계(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595165
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Tsuyoshi Nakasendo, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4595165
- **Abstract**: Multi-Edge type LDPC codes are introduced by Richardson and Urbanke, and they show examples of their ensembles has better performance than other known ensembles. Orlitsky et al. derived the condition for irregular LDPC code ensembles with minimum distance linearly increasing in code length. We derive the condition corresponding to Orlitsky’s condition for two-edge type LDPC code ensembles which is simple example of Multi-Edge type LDPC code ensembles.

## LDPC coding schemes for error control in a multicast network

- **Status**: ✅
- **Reason**: C: joint iterative message-passing decoding scheme improvement for binary LDPC; decoder technique potentially portable
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595101
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Jingyu Kang, Bo Zhou, Zhi Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/4595101
- **Abstract**: This paper investigates error control at the physical layer of a multicast network using low-density parity-check (LDPC) codes. Packets for transmission are encoded into LDPC codewords. A joint iterative message-passing scheme for decoding LDPC codewords at a receive node in the network is proposed to improve error performance. Also proposed is a split-codeword transmission to provide equal error protection for all transmitted packets. Density evolution analysis and some simulation results are also presented.

## On the probabilistic computation algorithm for the minimum-size stopping sets of LDPC codes

- **Status**: ✅
- **Reason**: Probabilistic algorithm for minimum-size stopping sets of LDPC codes; relevant to error-floor/code-design analysis (E) for binary LDPC.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4594995
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Masanori Hirotomo, Yoshiho Konishi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/4594995
- **Abstract**: On the binary erasure channel, the performance of LDPC codes decoded by iterative algorithms is estimated by small-size stopping sets. We have proposed a probabilistic algorithm for computing the minimum size of stopping sets of LDPC codes. In this paper, we analyze the probability and the complexity of finding the minimum-size stopping sets, and give an error probability of determining the minimum size of stopping sets after processing our algorithm. Additionally, we show the numerical results of computing the minimum size of stopping sets of several LDPC codes. In these result, we could compute the minimum size of stopping sets with high reliability.

## Ensemble weight enumerators for protograph-based doubly generalized LDPC codes

- **Status**: ✅
- **Reason**: 프로토그래프 기반 DGLDPC의 최소거리 성장률·error floor 개선 코드설계(E), 바이너리 LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595171
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Yige Wang, Chung-Li Wang, Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4595171
- **Abstract**: Protograph-based doubly generalized LDPC (DGLDPC) codes are explored in this paper. We extend (and in the process simplify) the technique for computing the ensemble weight enumerators of protograph-based LDPC and GLDPC codes to DGLDPC codes. We find that with careful design, protograph-based DGLDPC codes can have a better asymptotic growth rate of minimum distance than that of the protograph-based LDPC and GLDPC codes. Simulation results confirm that protograph-based DGLDPC codes have a low error floor.

## Sparse representations for codes and the hardness of decoding LDPC codes

- **Status**: ✅
- **Reason**: Sparse representation reduction transforming dense codes to sparse codes amenable to BP; potentially transferable code/decoding insight for binary LDPC BP.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4594994
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Nandakishore Santhi
- **PDF**: https://ieeexplore.ieee.org/document/4594994
- **Abstract**: The maximum likelihood decoding problem is known to be NP-hard for binary linear codes, while belief propagation decoding is known to work well in practice for several LDPC codes. In this paper we give a polynomial time reduction from the maximum likelihood decoding (MLD) problem for binary linear codes to the weighted MLD problem for (3,3)- LDPC codes. The reduction proves the NP-hardness of weighted MLD for (3,3)-LDPC codes. It also provides a method which can be used to transform the decoding problem for dense codes to the decoding of sparse codes. The later problem is often more amenable to the use of belief propagation algorithm. For ease of presentation, we have organized the total reduction in several intermediate reductions, most of which are elementary and easy to follow.

## Iterative approximate linear programming decoding of LDPC codes with linear complexity

- **Status**: ✅
- **Reason**: LDPC LP 디코딩의 선형복잡도 근사 반복 알고리즘(C), 디코더 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595237
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/4595237
- **Abstract**: The problem of low complexity linear programming (LP) decoding of low-density parity-check (LDPC) codes is considered. An iterative algorithm for efficient approximate solution of this problem was proposed by Vontobel and Koetter. In this paper the convergence rate and computational complexity of this algorithm are studied. In particular we are interested in obtaining a feasible vector in the LP decoding problem, with objective function value whose distance to the minimum, normalized by the block length, can be made arbitrarily small. It is shown that such a feasible vector can be obtained in linear, in the block length, computational complexity. Combined with previous results, that have shown that the LP decoder can correct some fixed fraction of errors, we conclude that this error correction can be achieved with linear computational complexity.

## LDPC convolutional codes based on braided convolutional codes

- **Status**: ✅
- **Reason**: braided convolutional 기반 새 LDPC-CC 구성과 인코딩/디코딩 아키텍처 제시; 코드설계+디코더 이식 가능(E/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595144
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Marcos B.S. Tavares, Michael Lentmaier, Kamil Sh. Zigangirov +1
- **PDF**: https://ieeexplore.ieee.org/document/4595144
- **Abstract**: We introduce and analyze new constructions of LDPC convolutional codes and their tail-biting versions which are obtained from braided convolutional codes. The basic ideas behind the encoding and decoding architectures for these codes are presented. Additionally, asymptotic results concerning the iterative thresholds are shown for different ensembles. Finally, we evaluate the bit error rate performances of several codes by means of computer simulations.

## New construction of LDPC convolutional codes

- **Status**: ✅
- **Reason**: 새 (3,t)-regular LDPC-CC 구성으로 girth>=8 보장 및 error floor 개선; 바이너리 코드설계(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595145
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Chi-Jen Wu, Yi-Chun Chou, Chung-Hsuan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4595145
- **Abstract**: In this paper, we propose a new construction of (3, t)-regular low-density parity-check convolutional codes by properly including binomial entries in the parity-check matrices. Both of the upper and lower bounds on free distance are derived for the new codes. Compared with previous constructions, our design can not only avoid codes of girth less than 8 but also provide enlarged free distances for some code rates. Simulation results show that the codes based on the new construction can achieve better bit-error-rate performance and lower error floor.

## Efficient layers-based schedules for iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: Tanner graph 서브그래프 분할 기반 layered serial 디코딩 스케줄로 복잡도/성능 개선; 디코더 알고리즘(C) 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595167
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Noam Presman, Eran Sharon, Simon Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/4595167
- **Abstract**: Efficient serial decoding schedules for LDPC codes are described. The schedules are based on dividing the Tanner graph to sub-graphs. This yields an improvement in complexity and performance over the standard schedules. An application of the introduced schedules to decoding codes based on lifted graphs is described. An analysis based on density evolution is presented and is used to predict the behavior of different schedules.

## Asymptotic bit error probability of LDPC codes for the binary erasure channel with finite number of iterations

- **Status**: ✅
- **Reason**: Asymptotic BER of LDPC under BP with finite iterations; finite-length/iteration analysis useful for binary LDPC code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595026
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Ryuhei Mori, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/4595026
- **Abstract**: We consider communication over the binary erasure channel (BEC) using low-density parity-check (LDPC) code and belief propagation (BP) decoding. Furthermore, a gap between the bit error probability after finite number of iterations for finite block length n and that for infinite block length is asymptotically α/n, where α denotes a speci..c constant determined by a degree distribution, a number of iterations and erasure probability. Our main result is to derive an ef..cient algorithm for calculating α for regular ensembles.

## A Feedback Belief Propagation Algorithm for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional 부호용 feedback BP 디코딩 알고리즘, 수렴속도 개선 BP 변형으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4594966
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Yuanhua Liu, Xinmei Wang, Yu-Cheng He
- **PDF**: https://ieeexplore.ieee.org/document/4594966
- **Abstract**: A feedback belief propagation (BP) decoding algorithm for low-density parity-check convolutional codes is proposed. The proposed algorithm can activate the variable nodes more efficiently by applying feedback decoding at each decoding iteration. Compared with the on-demand BP algorithm, the proposed algorithm has a doubled convergence speed and causes only about half of the decoding delay at similar error performances without any increase of storage requirement. Simulation results show that the proposed algorithm can offer a good trade-off between the error-correcting performance and the decoding complexity.

## LDPC codes from voltage graphs

- **Status**: ✅
- **Reason**: E: new structure-based binary QC-LDPC construction via voltage graphs, cycle classification (Abelian-inevitable cycles), portable code design
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595095
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Christine A. Kelley, Judy L. Walker
- **PDF**: https://ieeexplore.ieee.org/document/4595095
- **Abstract**: Several well-known structure-based constructions of LDPC codes, for example codes based on permutation and circulant matrices and in particular, quasi-cyclic LDPC codes, can be interpreted via algebraic voltage assignments. We explain this connection and show how this idea from topological graph theory can be used to give simple proofs of many known properties of these codes. In addition, the notion of Abelian-inevitable cycle is introduced and the subgraphs giving rise to these cycles are classified. We also indicate how, by using more sophisticated voltage assignments, new classes of good LDPC codes may be obtained.

## Error floors in LDPC codes: Fast simulation, bounds and hardware emulation

- **Status**: ✅
- **Reason**: Error floor prediction via absorbing sets with hardware emulation for finite-length LDPC; transferable code-design/HW insight (E/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595025
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Pamela Lee, Lara Dolecek, Zhengya Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/4595025
- **Abstract**: The error-correcting performance of low-density parity check (LDPC) codes, when decoded using practical iterative decoding algorithms, is known to be very close to Shannon limits in the asymptotic limit of large blocklengths. A substantial limitation to the use of finite-length LDPC codes is the presence of an error floor in the low frame error rate (FER) region. This paper develops two methods, a stochastic one based on importance sampling and a deterministic one based on high SNR asymptotics, as applied to suitably defined absorbing structures within the LDPC code, to predict error floors. Our results are in very close agreement with hardware-based experimental results, and moreover extend the prediction of the error probability to as low as 10-30. Our deterministic estimates are guaranteed to be a lower bound to the error probability in the high SNR regime.

## On the guaranteed error correction capability of LDPC codes

- **Status**: ✅
- **Reason**: Girth vs guaranteed error correction of regular LDPC under bit-flipping, trapping set bounds; transferable code-design/decoding insight (E/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595023
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Shashi Kiran Chilappagari, Dung Viet Nguyen, Bane Vasic +1
- **PDF**: https://ieeexplore.ieee.org/document/4595023
- **Abstract**: We investigate the relation between the girth and the guaranteed error correction capability of gamma-left regular LDPC codes when decoded using the bit flipping (serial and parallel) algorithms. A lower bound on the number of variable nodes which expand by a factor of at least 3gamma/4 is found based on the Moore bound. An upper bound on the guaranteed correction capability is established by studying the sizes of smallest possible trapping sets.

## Self-corrected Min-Sum decoding of LDPC codes

- **Status**: ✅
- **Reason**: self-corrected min-sum 디코딩, 부호 비의존적 min-sum 변형으로 NAND LDPC 디코더에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4594965
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/4594965
- **Abstract**: In this paper we propose a very simple but powerful self-correction method for the min-sum decoding of LPDC codes. Unlike other correction methods known in the literature, our method does not try to correct the check node processing approximation, but it modifies the variable node processing by erasing unreliable messages. However, this positively affects check node messages, which become symmetric Gaussian distributed, and we show that this is sufficient to ensure a quasi-optimal decoding performance. Monte-Carlo simulations show that the proposed self-corrected min-sum decoding performs very close to the sum-product decoding, while preserving the main features of the min-sum decoding, that is low complexity and independence with respect to noise variance estimation errors.

## Error rate estimation of finite-length low-density parity-check codes decoded by soft-decision iterative algorithms

- **Status**: ✅
- **Reason**: Error-rate estimation of finite-length LDPC under quantized soft-decision iterative decoding incl error floor; directly relevant (E, quantization).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595024
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4595024
- **Abstract**: This paper describes a combinatorial approach to estimate the error rate performance of low-density parity-check (LDPC) codes decoded by (quantized) soft-decision iterative decoding algorithms. The method is based on efficient enumeration of input vectors with small distances to a reference vector whose elements are selected to be the most reliable values from the input alphabet. Several techniques, including modified cycle enumeration, are employed to reduce the complexity of the enumeration. The error rate estimate is derived by testing the input vectors of small distances and estimating the contribution of larger distance vectors. We demonstrate by a number of examples that the proposed method provides accurate estimates of error rate with computational complexity much lower than that of Monte Carlo simulations, especially at the error floor region.

## Interior point decoding for linear vector channels based on convex optimization

- **Status**: ✅
- **Reason**: 볼록최적화 기반 interior point 디코더(C), 바이너리 LDPC ISI/PR 채널 디코더로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595236
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4595236
- **Abstract**: In this paper, a novel decoding algorithm for low-density parity-check (LDPC) codes based on convex optimization is presented. The decoding algorithm, called interior point decoding, is designed for linear vector channels. The linear vector channels include many practically important channels such as inter symbol interference channels, partial response channels and MIMO channels. It is shown that the maximum likelihood decoding (MLD) rule for a linear vector channel can be relaxed to a convex optimization problem, which is called a relaxed MLD problem. Approximate variations of gradient descent and Newton methods are used to solve the convex optimization problem.

## Coding for the q-ary symmetric channel with moderate q

- **Status**: ✅
- **Reason**: 표준 바이너리 LDPC 디코딩을 단순 수정해 q-ary 대칭채널에 적용하는 실용 디코더 변형, BP 이식 검토 여지(C, 애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595371
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Claudio Weidmann
- **PDF**: https://ieeexplore.ieee.org/document/4595371
- **Abstract**: We study coding schemes for the q-ary symmetric channel with moderate alphabet sizes q that are much smaller than the q = 2256 considered as ldquoentry levelrdquo in some recently proposed packet-based schemes. First, we show theoretical optimality of a simple layered scheme, then we propose a practical coding scheme based on a simple modification of standard binary LDPC decoding.

## Optimizing burst erasure correction of LDPC codes by interleaving

- **Status**: ✅
- **Reason**: QC-LDPC stopping set 기반 burst erasure 개선 인터리버 설계(WiMax protograph QC-LDPC); 바이너리 코드설계(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4595166
- **Type**: conference
- **Published**: 6-11 July 
- **Authors**: Gokul Sridharan, Abishek Kumarasubramanian, Andrew Thangaraj +1
- **PDF**: https://ieeexplore.ieee.org/document/4595166
- **Abstract**: The performance of iterative decoding of low density parity check (LDPC) codes over binary erasure channels can be completely characterized by the study of stopping sets. Therefore, the burst erasure correction capability of a given LDPC code can be readily quantified by searching for stopping sets within consecutive bit nodes. In this work we study the optimal permutation of the bit nodes that will result in the maximum possible burst erasure correction capability for a given LDPC code. Noting that this is essentially a combinatorial optimization problem that is highly likely to be NP-hard, we adopt a simulated annealing based approach for finding the optimal permutation. We present bounds based on stopping sets that limit the burst erasure correction capability. As part of our results, we provide interleavers that greatly improve the burst erasure correction capability of protograph quasi-cyclic LDPC codes used in the WiMax standard.

## On stopping criteria for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 단축 LDPC 조기종료 정지기준(반복수 절감) - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4610813
- **Type**: conference
- **Published**: 25-25 July
- **Authors**: D. Alleyne, J. Sodha
- **PDF**: https://ieeexplore.ieee.org/document/4610813
- **Abstract**: A stopping criterion for short-length low-density parity-check codes (LDPC) is developed based on accumulating evidence which indicates whether the decoder should be allowed to iterate beyond a predefined iteration limit that is lower than the normal maximum number of decoder iterations. Without any additional decoding complexity, we find that the average number of iterations at low SNRs can be reduced without sacrificing performance. Simulation results are presented for the rate frac12 (288, 576) and the rate frac12 (1152, 2304) WiMAX 802.16e LDPC code over an AWGN channel with binary phase shift keying (BPSK) modulation.

## LP decoding of LDPC codes in HARQ systems

- **Status**: ✅
- **Reason**: LP 디코딩+ARQ, integrality 기반 재전송 기준 - 바이너리 LDPC 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4610781
- **Type**: conference
- **Published**: 25-25 July
- **Authors**: Michael Lunglmayr, Jens Berkmann, Mario Huemer
- **PDF**: https://ieeexplore.ieee.org/document/4610781
- **Abstract**: The combination of low density parity check (LDPC) Codes and Automatic Repeat reQuest (ARQ) has shown to be a promising option to increase the throughput of a communication system. A recently proposed method uses the decoding result to request unreliable bits for retransmission (reliability-based Hybrid ARQ). Commonly, Belief Propagation is used to decode LDPC codes. The result of this algorithm naturally provides an estimate for the probability of a bit to be erroneous. Another possibility to decode LDPC codes is via linear programming (LP) decoding. Despite some drawbacks (e.g. in terms of implementation complexity), linear programming decoding provides an interesting alternative to Belief Propagation. This work investigates the feasibility of combining LP decoding with ARQ. In lack of a probability measure for the decoded bits, when using LP decoding, request criteria using the integrality of the values in the LP solution are proposed. We present statistical investigations on the proposed criteria and the results of throughput simulations demonstrating the gains achievable by the proposed methods.

## Design of structured irregular LDPC codes

- **Status**: ✅
- **Reason**: cyclic shift 행렬 기반 불규칙 LDPC 구성+파라미터 최적화 알고리즘 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4602580
- **Type**: conference
- **Published**: 21-25 July
- **Authors**: Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/4602580
- **Abstract**: A novel construction of irregular LDPC codes based on cyclic shift matrices is presented. The construction allows compact specification of LDPC codes of arbitrary length. An optimization algorithm is presented for finding the parameters of the code.

## Code construction algorithm for architecture aware LDPC codes with low-error-floor

- **Status**: ✅
- **Reason**: low-error-floor 위한 trapping/stopping set 감소 코드 구성+TDMP 디코더 FPGA 구현 — 코드설계(E)/HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4602573
- **Type**: conference
- **Published**: 21-25 July
- **Authors**: Dariusz Kania, Wojciech Sulek
- **PDF**: https://ieeexplore.ieee.org/document/4602573
- **Abstract**: The common approach for the design of an error correction system is first to construct a code and then to define the hardware structure of the encoder and decoder. However, in the case of LDPC codes (low-density parity-check) such a constructed code is generally not well suited for a hardware implementation. It has been recognized that the code construction and hardware design must be considered jointly to facilitate LDPC decoder and encoder implementation. In this paper, an efficient decoder structure for regular and irregular LDPC codes, based on TDMP (turbo-decoding message passing) scheme is designed first. The decoder has been implemented and verified in an FPGA device. Constraints for the parity check matrix of a code to be suitable for the decoder architecture are defined. Then an algorithm for LDPC parity check matrix construction subject to these constraints is presented. The algorithm aims at improving performance of the code in the low SNR region by employing irregular codes as well as in high SNR region by reducing the number of small Stopping Sets and Trapping Sets in the Tanner graph of the code making use of a computer search technique.

## LDPC-based advanced FEC for 100 Gbps transmission

- **Status**: ✅
- **Reason**: 100Gbps FEC용 회로복잡도 감소 LDPC 알고리즘 + concatenation으로 error-floor 억제 — 복잡도 저감 디코더/error-floor 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4590567
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Takashi Mizuochi, Yoshikuni Miyata
- **PDF**: https://ieeexplore.ieee.org/document/4590567
- **Abstract**: Practical FEC implementation of 100 Gbps long-haul transmission is discussed. An LDPC code using a novel algorithm is introduced to reduce circuit complexity. Simulation shows that the Q limit is 7.1 dB, and that the concatenation effectively suppresses unwanted error-floor.

## Architecture and VLSI realization of a high-speed programmable decoder for LDPC convolutional codes

- **Status**: ✅
- **Reason**: 수정 Min-Sum 기반 고속 프로그래머블 LDPC 디코더 VLSI/ASIC 아키텍처, 병렬화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4580181
- **Type**: conference
- **Published**: 2-4 July 2
- **Authors**: Marcos B.S. Tavares, Steffen Kunze, Emil Matus +1
- **PDF**: https://ieeexplore.ieee.org/document/4580181
- **Abstract**: In this paper, we present a novel high-speed dual-core programmable decoder architecture for LDPC convolutional codes and their tail-biting versions. This architecture uses a modified Min-Sum algorithm and enables the decoding of a multitude of codes with different node degree distributions, rates and block lengths. We show how the parallelization concepts are derived using the properties of the bipartite graphs underlying the codes. Moreover, the hardware elements composing the architecture will be presented and analyzed in detail. The programmability of the decoder is also considered. Finally, we present the synthesis results for a prototype ASIC which is capable of achieving high decoding throughput still with very high flexibility, relatively low power consumption and small area.
