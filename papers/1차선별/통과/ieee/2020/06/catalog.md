# IEEE Xplore — 2020-06 (1차선별 통과)


## LOCO Codes: Lexicographically-Ordered Constrained Codes

- **Status**: ✅
- **Reason**: 바이너리 제약부호(LOCO)로 Flash 셀간간섭 완화, LDPC 패리티만 인코딩해 rate loss 줄이는 신규 코드설계 — NAND LDPC 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8846741
- **Type**: journal
- **Published**: June 2020
- **Authors**: Ahmed Hareedy, Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/8846741
- **Abstract**: Line codes make it possible to mitigate interference, to prevent short pulses, and to generate streams of bipolar signals with no direct-current (DC) power content through balancing. They find application in magnetic recording (MR) devices, in Flash devices, in optical recording devices, and in some computer standards. This paper introduces a new family of fixed-length, binary constrained codes, named lexicographically-ordered constrained codes (LOCO codes), for bipolar non-return-to-zero signaling. LOCO codes are capacity-achieving, the lexicographic indexing enables simple, practical encoding and decoding, and this simplicity is demonstrated through analysis of circuit complexity. LOCO codes are easy to balance, and their inherent symmetry minimizes the rate loss with respect to unbalanced codes having the same constraints. Furthermore, LOCO codes that forbid certain patterns can be used to alleviate inter-symbol interference in MR systems and inter-cell interference in Flash systems. Numerical results demonstrate a gain of up to 10% in rate achieved by LOCO codes with respect to other practical constrained codes, including run-length-limited codes, designed for the same purpose. Simulation results suggest that it is possible to achieve a channel density gain of about 20% in MR systems by using a LOCO code to encode only the parity bits, limiting the rate loss, of a low-density parity-check code before writing.

## Deep Learning-Aided Belief Propagation Decoder for Polar Codes

- **Status**: ✅
- **Reason**: 2-D offset Min-Sum 디코더와 LDPC-polar 결합 OMS 알고리즘 + HW 아키텍처 제안; min-sum 변형(C)으로 LDPC 디코더에 이식 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9097207
- **Type**: journal
- **Published**: June 2020
- **Authors**: Weihong Xu, Xiaosi Tan, Yair Be’ery +4
- **PDF**: https://ieeexplore.ieee.org/document/9097207
- **Abstract**: This paper presents deep learning (DL) methods to optimize polar belief propagation (BP) decoding and concatenated LDPC-polar codes. First, two-dimensional offset Min-Sum (2-D OMS) decoding is proposed to improve the error-correction performance of existing normalized Min-Sum (NMS) decoding. Two optimization methods used in DL, namely back-propagation and stochastic gradient descent, are exploited to derive the parameters of proposed algorithms. Numerical results demonstrate that there is no performance gap between 2-D OMS and exact BP on various code lengths. Then the concatenated OMS algorithms with low complexity are presented for concatenated LDPC-polar codes. As a result, the optimized concatenated OMS decoding yields error-correction performance with CRC-aided successive cancellation list (CA-SCL) decoder of list size 2 on length-1024 polar codes. In addition, the efficient hardware architectures of scalable polar OMS decoder are described and the proposed decoder is reconfigurable to support three code lengths (N = 256, 512, 1024) and two decoding algorithms (2-D OMS and concatenated OMS). The polar OMS decoder implemented on 65 nm CMOS technology achieves a maximum coded throughput of 5.4 Gb/s at Eb/N0 = 4 dB for code length 1024 and 7.5 Gb/s at Eb/N0 = 3.5 dB for code length 256, which are comparable to the state-of-the-art polar BP decoders. Moreover, a 5.1 Gb/s throughput at Eb/N0 = 4 dB is achieved under concatenated OMS decoding mode for code length 1024 with a latency of 200 ns, which is superior to existing CA-SCL decoders that have similar error-correction performance.

## Velocity Analysis of BP Decoding Waves for SC-LDPC Ensembles on BMS Channels: An Interpolation-Based Approach

- **Status**: ✅
- **Reason**: SC-LDPC BP 디코딩 파동 속도 예측(IDE) 신규 분석기법 — 바이너리 SC-LDPC 코드설계/해석에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9018237
- **Type**: journal
- **Published**: June 2020
- **Authors**: Zhonghao Zhang, Kexin Zhang, Zhangyou Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/9018237
- **Abstract**: This paper is concerned with the dynamics of spatially-coupled low-density parity-check (SC-LDPC) ensembles for transmission on general binary memoryless symmetric (BMS) channels under belief-propagation (BP) decoding. The decoding waves of such ensembles are found to exhibit solitonic behavior, propagating along the Tanner graphs at asymptotically constant velocities. A low-complexity approach termed interpolated density evolution (IDE) is proposed to predict the decoding wave velocities. In this approach, the densities of a decoding wave are approximated by interpolating between some fixed points of an uncoupled DE recursion with one-dimensional functions. Two transfer functions for updating these interpolation functions in the IDE recursion are established and a simple strategy is introduced to deal with the coexistence of multiple transition regions. In addition, a threshold analysis is developed based on two ansatzes, explaining why our approach can achieve a good trade-off between computational cost and accuracy, as illustrated with some numerical examples at the end of this paper.

## An Approach to the Generation of Regular QC-LDPC Codes with Girth 8

- **Status**: ✅
- **Reason**: girth-8 정규 QC-LDPC 생성 신규 SES 알고리즘, 더 작은 circulant 크기 달성 — 코드설계 기여(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9134139
- **Type**: conference
- **Published**: 8-11 June 
- **Authors**: Aleksei Kharin, Aleksei Dryakhlov, Evgeny Mirokhin +3
- **PDF**: https://ieeexplore.ieee.org/document/9134139
- **Abstract**: In this paper, we propose a new approach to the generation of regular QC-LDPC codes with girth 8. The aim of the proposed smart exhaustive search (SES) algorithm is to construct codes with the desired lifting factor or to check whether codes with this parameter even exist. Also, this method allows us to reach smaller values of minimal circulant size compared with previously described methods: simulated annealing, hill-climbing, and guess-and-test.

## Irregular QC-LDPC Codes Generation Based on EMD Maximization Criterion for Protograph

- **Status**: ✅
- **Reason**: protograph EMD 최대화 기반 비정규 QC-LDPC 생성 신규 기법(사이클 4~10 제어) — 코드설계 기여(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9134365
- **Type**: conference
- **Published**: 8-11 June 
- **Authors**: Aleksei Kharin, Aleksei Dryakhlov, Evgeny Mirokhin +3
- **PDF**: https://ieeexplore.ieee.org/document/9134365
- **Abstract**: In this paper a new method for irregular QC-LDPC codes generation with desired EMD characteristics is provided. The method allows to control the minimal EMD value for cycles of length of 4, 6, 8 and 10. Better implementations in terms of EMD values and error correction performance of WiFi codes of length 648 were obtained with the proposed method.

## A Model-Driven Deep Learning Method for Normalized Min-Sum LDPC Decoding

- **Status**: ✅
- **Reason**: 모델기반 딥러닝 normalized min-sum LDPC 디코더(NNMS/SNNMS) — 이식 가능한 신경망 디코더 새 기여 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9145237
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Qing Wang, Shunfu Wang, Haoyu Fang +3
- **PDF**: https://ieeexplore.ieee.org/document/9145237
- **Abstract**: With the applications of deep learning networks booming in physical layer communication, deep-learning-based channel decoding methods have become a research hotspot. However, the high complexity hinders the application of deep neural network (DNN) on long code. In this paper, we propose a model-driven deep learning method for normalized min-sum (NMS) low-density parity-check (LDPC) decoding. First, we propose a neural normalized min-sum (NNMS) LDPC decoding network. By unfolding the iterative decoding progress between checking nodes (CNs) and variable nodes (VNs) into a feedforward propagation network, we can make use of the advantages of both model-driven deep learning methods and conventional normalized min-sum (CNMS) LDPC decoding method. Second, considering that the NNMS decoder needs large number of multipliers, we propose a shared neural normalized min-sum (SNNMS) decoding network to reduce the number of correction factors. Experimental results show that the BER performance of the proposed NNMS decoder is 1.5dB better than the conventional LDPC decoder, using fewer iterations. Furthermore, the proposed SNNMS decoder outperforms the proposed NNMS decoder and reduces the computation complexity.

## Information Bottleneck Decoding of Rate-Compatible 5G-LDPC Codes

- **Status**: ✅
- **Reason**: 5G-LDPC용 IB 4-bit LUT 디코더, offset min-sum 능가 — 바이너리 LDPC 양자화 디코더, 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9149304
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Maximilian Stark, Gerhard Bauch, Linfang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/9149304
- **Abstract**: The new 5G communications standard increases data rates and supports low-latency communication that places constraints on the computational complexity of channel decoders. 5G low-density parity-check (LDPC) codes have the so-called protograph-based raptor-like (PBRL) structure which offers inherent rate-compatibility and excellent performance. Practical LDPC decoder implementations use message-passing decoding with finite precision, which becomes coarse as complexity is more severely constrained. Performance degrades as the precision becomes more coarse. Recently, the information bottleneck (IB) method was used to design mutual-information-maximizing lookup tables that replace conventional finite-precision node computations. The IB approach exchanges messages represented by integers with very small bit width. This paper extends the IB principle to the flexible class of PBRL LDPC codes as standardized in 5G. The extensions include puncturing and rate-compatible IB decoder design. As an example of the new approach, a 4-bit information bottleneck decoder is evaluated for PBRL LDPC codes over a typical range of rates. Frame error rate simulations show that the proposed scheme outperforms offset min-sum decoding algorithms and operates very close to double-precision sum-product belief propagation decoding.

## Multi-Label Neural Decoders for Block Codes

- **Status**: ✅
- **Reason**: 블록부호용 멀티라벨 신경망 디코더 — 이식 가능 신경망 디코더(C), LDPC 적용 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9148786
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Cheuk Ting Leung, Rajshekhar V Bhat, Mehul Motani
- **PDF**: https://ieeexplore.ieee.org/document/9148786
- **Abstract**: The problem of decoding an (n, k, d) error-correcting block code, where a k-bit message word is mapped to an n-bit codeword, can be cast as a single-label classification problem. While it has been observed that the performance of such single-label neural decoders closely approaches that of the corresponding maximum likelihood decoder (MLD), the number of output nodes increases exponentially with k, making it prohibitive to implement for large k. To address this issue, we explore classification based multi-label neural decoders, in which the number of output nodes increases linearly with k. We consider well-known linear and non-linear block codes, as well as concatenated block codes, which have applications in emerging wireless networks. Our study finds that (i) although the number of output nodes linearly increases with k in a multi-label decoder, it requires more hidden layers and nodes in each hidden layer than the corresponding single-label decoder to achieve its best performance, and (ii) although one can design a multi-label decoder with bit error rate matching that of the MLD, it leaves more blocks in error leading to a reduced performance in terms of block error rate. We also note that the performance of the proposed decoder for concatenated codes is at least as good as that of a natural decoding algorithm in which the inner code is first decoded using the MLD and then the outer code is decoded with a polynomial-time decoding algorithm.

## Partially Permuted Multi-Trellis Belief Propagation for Polar Codes

- **Status**: ✅
- **Reason**: polar용 부분치환 멀티트렐리스 BP — permutation 기반 BP cycle 완화 아이디어, 이식 가능 디코더(C)로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9149228
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Vismika Ranasinghe, Nandana Rajatheva, Matti Latva-aho
- **PDF**: https://ieeexplore.ieee.org/document/9149228
- **Abstract**: Belief propagation (BP) is an iterative decoding algorithm for polar codes which can be parallelized effectively to achieve higher throughput. However, because of the presence of error floor due to cycles and stopping sets in the factor graph, the performance of the BP decoder is far from the performance of state of the art cyclic redundancy check (CRC) aided successive cancellation list (CA-SCL) decoders. It has been shown that successive BP decoding on multiple permuted factor graphs, which is called the multi-trellis BP decoder, can improve the error performance. However, when permuting the entire factor graph, since the decoder dismisses the information from the previous permutation, the number of iterations required is significantly larger than that of the standard BP decoder. In this work, we propose a new variant of the multi-trellis BP decoder which permutes only a subgraph of the original factor graph. This enables the decoder to retain information of variable nodes in the subgraphs, which are not permuted, reducing the required number of iterations needed in-between the permutations. As a result, the proposed decoder can perform permutations more frequently, hence being more effective in mitigating the effect of cycles which cause oscillation errors. Experimental results show that for a polar code with block length 1024 and rate 0.5 the error performance gain of the proposed decoder at the frame error rate of $10^{-6}$ is 0.25 dB compared to multi-trellis decoder based on full permutations. This performance gain is achieved along with reduced latency in terms of the number of iterations.

## Discrete Polar Decoder using Information Bottleneck Method

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 메시지 양자화 BP 디코더 — LLR 양자화/LUT 기법 NAND LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9149242
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Akira Yamada, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/9149242
- **Abstract**: Polar codes are attracting much attention and being used for control channels of the 5th generation of mobile communication system (5G). As a feature, it is easier to implement encoder and decoder than Turbo codes and LDPC (Low Density Parity Check) codes. One of the decoding methods of polar codes is BP (Belief Propagation) decoding, which can decode in parallel, so that decoding can be performed at high speed. However, due to hardware limitation, calculations on the decoder get very complicated. This issue can be solved by using the information bottleneck method. This method compresses an observation variable to a quantized one while attempting to preserve the mutual information shared with a relevant random variable. In the conventional research, the information bottleneck method is applied to the BP decoding of the LDPC codes. In this paper, the information bottleneck method is used for the BP decoding of polar codes. The BP decoding of polar codes is distinct from that of LDPC codes. It has several types of the messages, and each time a message is updated, the decoding becomes more complex. By using the information bottleneck method, the decoder can compress the channel outputs and the messages of BP into unsigned integers while preventing degradation of the error correcting performance. Thus, we can reduce the complexity of calculation in the decoding process and easily implement the decoder. This paper also investigates the minimum bit width for quantization with negligible degradation and the suboptimal Eb/N0 for designing the lookup tables. These lookup tables are used for updating the messages. The simulation results show that the error correcting capability of the discrete polar decoders of the proposed method is negligibly degraded compared to the BP decoding without compression.

## Quadratic Programming Decoder for Binary LDPC Codes via ADMM Technique with Linear Complexity

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 ADMM 기반 QP 디코더, 선형복잡도, BP 능가 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9149405
- **Type**: conference
- **Published**: 7-11 June 
- **Authors**: Jing Bai, Yongchao Wang
- **PDF**: https://ieeexplore.ieee.org/document/9149405
- **Abstract**: In this paper, we develop an efficient quadratic programming (QP) decoding algorithm via the alternating direction method of multipliers (ADMM) technique for binary low density parity check (LDPC) codes. Its main content is as follows: first, through transforming the three-variables parity check equation to its equivalent expression, we relax the maximum likelihood decoding problem to a quadratic program. Second, the ADMM technique is exploited to design the solving algorithm of the resulting QP decoding model. Compared with the existing ADMM-based mathematical programming (MP) decoding algorithms, our proposed algorithm eliminates complex Euclidean projection onto the check polytope. Third, we prove that the proposed algorithm satisfies the favorable property of all-zeros assumption. Moreover, by exploiting the inside structure of the QP model, we show that the decoding complexity of our proposed algorithm in each iteration is linear in terms of LDPC code length. Simulation results demonstrate that the proposed QP decoder attains better error-correction performance than the sum-product BP decoder and costs the least amount of decoding time amongst the state-of-the-art ADMM-based MP decoding algorithms.

## Generalized LDPC Codes with Convolutional Code Constraints

- **Status**: ✅
- **Reason**: CC-GLDPC 신규 코드 설계(convolutional 제약 GLDPC, DE threshold·weight enumerator 분석), 바이너리 구성(E) 이식 가능성, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174017
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Muhammad Umar Farooq, Saeedeh Moloudi, and Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/9174017
- **Abstract**: Braided convolutional codes (BCCs) are a class of spatially coupled turbo-like codes that can be described by a (2), (3)-regular compact graph. In this paper, we introduce a family of (dv, dc)-regular GLDPC codes with convolutional code constraints (CC-GLDPC codes), which form an extension of classical BCCs to arbitrary regular graphs. In order to characterize the performance in the waterfall and error floor regions, we perform an analysis of the density evolution thresholds as well as the finitelength ensemble weight enumerators and minimum distances of the ensembles. In particular, we consider various ensembles of overall rate R = 1/3 and R = 1/2 and study the trade-off between variable node degree and strength of the component codes. We also compare the results to corresponding classical LDPC codes with equal degrees and rates. It is observed that for the considered LDPC codes with variable node degree dv > 2, we can find a CC-GLDPC code with smaller dv that offers similar or better performance in terms of BP and MAP thresholds at the expense of a negligible loss in the minimum distance.

## A Novel Design of Spatially Coupled LDPC Codes for Sliding Window Decoding

- **Status**: ✅
- **Reason**: SC-LDPC 신규 코드 설계(reduced-degree check 배치로 error burst 회복), 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9173961
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Min Zhu, David G. M. Mitchell, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/9173961
- **Abstract**: We introduce a novel design of spatially coupled low density parity check codes in order to reduce the effects of error propagation in low-latency sliding window decoding for large frame lengths or streaming applications. Specifically, we employ reduced-degree check nodes spaced throughout the coupling chain, which have the effect of allowing the decoder to recover from error bursts. A simplified analysis of the block error rate (BLER) of the proposed codes is presented that allows us to predict the effect of different placements of reduced-degree checks in the coupling chain. Simulation results supporting the beneficial effect of the new code design on the overall BLER performance are included.

## Learned Scheduling of LDPC Decoders Based on Multi-armed Bandits

- **Status**: ✅
- **Reason**: MAB 기반 노드별 LDPC 디코더 스케줄링 — 부호 비의존 디코더 스케줄링 기법(C), NAND LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174337
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Salman Habib, Allison Beemer, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/9174337
- **Abstract**: The multi-armed bandit (MAB) problem refers to the dilemma encountered by a gambler when deciding which arm of a multi-armed slot machine to pull in order to maximize the total reward earned in a sequence of pulls. In this paper, we model the scheduling of a node-wise sequential LDPC decoder as a Markov decision process, where the underlying Tanner graph is viewed as a slot machine with multiple arms corresponding to the check nodes. A fictitious gambler decides which check node to pull (schedule) next by observing a reward associated with each pull. This interaction enables the gambler to discover an optimized scheduling policy that aims to reach a codeword output by propagating the fewest possible messages. Based on this policy, we contrive a novel MAB-based node-wise scheduling (MABNS) algorithm to perform sequential decoding of LDPC codes. Simulation results show that the MAB-NS scheme, aided by an appropriate scheduling policy, outperforms traditional scheduling schemes in terms of complexity and bit error probability.

## Non-Uniform Windowed Decoding For Multi-Dimensional Spatially-Coupled LDPC Codes

- **Status**: ✅
- **Reason**: MD-SC-LDPC 비균일 윈도우 디코더(BEC) — 바이너리 SC-LDPC 디코더 기법(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174511
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Lev Tauz, Homa Esfahanizadeh, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/9174511
- **Abstract**: In this paper, we propose a non-uniform windowed decoder for multi-dimensional spatially-coupled LDPC (MD-SCLDPC) codes over the binary erasure channel. An MD-SC-LDPC code is constructed by connecting together several SC-LDPC codes into one larger code that provides major benefits over a variety of channel models. In general, SC codes allow for lowlatency windowed decoding. While a standard windowed decoder can be naively applied, such an approach does not fully utilize the unique structure of MD-SC-LDPC codes. In this paper, we propose and analyze a novel non-uniform decoder to provide more flexibility between latency and reliability. Our theoretical derivations and empirical results show that our non-uniform decoder greatly improves upon the standard windowed decoder in terms of design flexibility, latency, and complexity.

## Message Flow Analysis in Practical LDPC Decoders for the Interpretation of Absorbing Set Thresholds

- **Status**: ✅
- **Reason**: min-sum 디코더 absorbing set threshold 메시지 흐름 분석 — error floor 관련 디코더 분석(C/E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174483
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Marco Ferrari, Ramon Marenzi, Luca Barletta
- **PDF**: https://ieeexplore.ieee.org/document/9174483
- **Abstract**: Absorbing sets (ASs) cause the error floor phenomenon in many low-density parity-check (LDPC) codes by entrapping iterative decoders. A recent simplified system model for practical min-sum (MS) LDPC decoding predicts that if all variable nodes in an AS have channel messages above a certain threshold, the AS cannot entrap the decoder. The threshold is an AS parameter that depends on its Tanner graph, and is the result of a nonlinear optimization. In this paper, we analyze the messages exchanged in the directed graph (digraph) of the AS during MS decoding while evaluating the AS threshold. By doing this, we unveil the meaning of the threshold value, which is the minimum channel message for which positive feedback loops in the digraph involve all the messages exchanged.

## Analysis of Absorbing Sets using Cosets and Syndromes

- **Status**: ✅
- **Reason**: absorbing set을 coset/syndrome으로 분석 + 새 탐색법 — error floor 코드 설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174513
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: Emily McMillon, Allison Beemer, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/9174513
- **Abstract**: Absorbing sets are combinatorial structures in a Tanner graph that have been shown to characterize iterative decoder failure, and particularly error floor behavior, of LDPC codes. In this paper, we examine the connection between absorbing sets and the syndromes of their support vectors. Using this framework, we provide a new characterization of fully absorbing sets, which have been considered the most harmful for iterative decoders. We also show how the sets of absorbing set support vectors appear as translates of codewords in subspaces of the code. These techniques are used to derive new search methods for absorbing sets.

## Spatially Coupled Codes with Sub-Block Locality: Joint Finite Length-Asymptotic Design Approach

- **Status**: ✅
- **Reason**: SC-LDPC 코드 설계(유한길이+점근적 결합, 사이클 카운트 최적화) — 바이너리 LDPC 코드 설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9174265
- **Type**: conference
- **Published**: 21-26 June
- **Authors**: H. Esfahanizadeh, E. Ram, Y. Cassuto +1
- **PDF**: https://ieeexplore.ieee.org/document/9174265
- **Abstract**: SC-LDPC codes with sub-block locality can be decoded locally at the level of sub-blocks that are much smaller than the full code block, thus providing fast access to the coded information. The same code can also be decoded globally using the entire code block, for increased data reliability. In this paper, we pursue the analysis and design of such codes from both finite-length and asymptotic lenses. This mixed approach has rarely been applied in designing SC codes, but it is beneficial for optimizing code graphs for local and global performance simultaneously. Our proposed framework consists of two steps: 1) designing the local code for both threshold and cycle counts, and 2) designing the coupling of local codes for the best cycle count in the global design.

## A Deeply Pipelined, Highly Parallel and Flexible LDPC Decoder

- **Status**: ✅
- **Reason**: D: deeply pipelined parallel LDPC decoder with delta-update relaxing data dependency, transplantable HW architecture
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9159808
- **Type**: conference
- **Published**: 16-19 June
- **Authors**: Jérémy Nadal, Mickaël Fiorentino, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/9159808
- **Abstract**: A deeply pipelined and parallel LDPC decoder architecture is proposed in this paper. The main feature of this architecture is the Δ-update scheme, which relaxes the data dependency requirement and allows for deeper pipelines than typical decoders. The proposed architecture also has the flexibility to handle a large number of codes. Frame error rate performance is shown for three codes with different quantization parameters. Finally, the impact of pipeline depth on processing time and on the energy-delay product (EDP) is evaluated from post-synthesis results. The results show that the ability to have deeper pipelines can lead to large reductions in EDP.

## LDPC design for 5G NR URLLC & mMTC

- **Status**: ✅
- **Reason**: 소블록용 LDPC 신규 설계 + OSD 횟수 1~2회로 줄인 개선 BP+OSD 디코더 — 이식 가능 디코더(C)/코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9148187
- **Type**: conference
- **Published**: 15-19 June
- **Authors**: Liguang Li, Jun Xu, Jin Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/9148187
- **Abstract**: Low density parity check (LDPC) code in the fifth generation (5G or New Radio, NR) was mainly designed for the enhanced Mobile Broadband (eMBB) scenario, and specific optimization has not been considered for both scenarios of Ultra-Reliable and Low Latency Communications (URLLC) and massive Machine Type Communications (mMTC), especially for small transport block sizes (TBSs). Therefore, we introduce a specific optimized design method of LDPC code for small TBSs of the latter two scenarios. According to the proposed method, a new LDPC code is designed and its performance is better than the LDPC code in 5G. Furthermore, an improved algorithm combining belief propagation (BP) and ordered statistic decoding (OSD) is considered in this paper. Compared with traditional BP+OSD algorithm, although there is slight performance loss, the number of OSD decoding implemented in the improved algorithm can be reduced to 1 or 2. Simulation results indicate that the performance of the improved BP+OSD decoding algorithm is obviously better than that of the popular BP decoding and also better than that of the polar code in 5G.

## Decoding of LDPC Codes for 5G Standard Using Source Distribution

- **Status**: ✅
- **Reason**: BP 디코더 LLR 계산을 소스분포 반영해 변형 — 부호 비의존적 디코더 입력 LLR 보정 기법으로 NAND LDPC에 이식 가능(C), Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9131454
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: A. A. Ovchinnikov, A. A. Fominykh
- **PDF**: https://ieeexplore.ieee.org/document/9131454
- **Abstract**: The paper examines the decoding of low-density parity-check codes taking into account the source distribution. More specifically, we consider the alteration of LLR calculation on the input of belief propagation decoder. The experimental results for binary input additive white Gaussian noise channel are presented using various source distributions.
