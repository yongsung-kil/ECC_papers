# IEEE Xplore — 2021-06 (1차선별 통과)


## A Reconfigurable and Pipelined Architecture for Standard-Compatible LDPC and Polar Decoding

- **Status**: ✅
- **Reason**: 재구성형 파이프라인 LDPC/polar 디코더 HW 아키텍처(FPGA/ASIC) — LDPC 디코더 HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9415136
- **Type**: journal
- **Published**: June 2021
- **Authors**: Shan Cao, Ting Lin, Shunqing Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9415136
- **Abstract**: With low-density parity-check (LDPC) codes and polar codes selected as the standard codes for the fifth generation (5G) enhanced Mobile Broad Band scenario (eMBB), a decoding architecture that can simultaneously support the decoding of control and data plane becomes necessary at the terminal side to meet the raising requirement for 5 G network deployment. Due to the special structure of LDPC codes according to the Release 15 (R15) 5G standard, a straight-forward extension of the existing reconfigurable scheme is in general difficult. Therefore in this paper, a unified decoding architecture is proposed that can be reconfigured to either LDPC codes or polar codes. Due to various differences between the two codes such as parity-check matrices, codeword lengths and iterative methods, a joint decoding algorithm is introduced by reordering basic decoding operations to the unified add-comparison-add pattern for both codes. Then, a pipelined structure of reconfigurable decoding unit (RDU) is presented correspondingly which is fully compatible with all decoding patterns of the R15 standard. And finally, a reconfigurable decoder is proposed with multiple levels of parallelism, and the reconfiguration scheme is introduced to improve the hardware utilization and decoding efficiency. The proposed decoder is implemented in FPGA and ASIC, respectively, and has achieved state-of-the-art performance in throughput and area efficiency compared to LDPC-only and polar-only decoders.

## Parallel and Flexible 5G LDPC Decoder Architecture Targeting FPGA

- **Status**: ✅
- **Reason**: 병렬·유연 QC-LDPC 디코더 FPGA 아키텍처(프레임 병렬·스케줄링) — NAND LDPC HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9420267
- **Type**: journal
- **Published**: June 2021
- **Authors**: Jérémy Nadal, Amer Baghdadi
- **PDF**: https://ieeexplore.ieee.org/document/9420267
- **Abstract**: The quasi-cyclic (QC) low-density parity-check (LDPC) code is a key error correction code for the fifth generation (5G) of cellular network technology. Designed to support several frame sizes and code rates, the 5G LDPC code structure allows high parallelism to deliver the high demanding data rate of 10 Gb/s. This impressive performance introduces challenging constraints on the hardware design. Particularly, allowing such high flexibility can introduce processing rate penalties on some configurations. In this context, a novel highly parallel and flexible hardware architecture for the 5G LDPC decoder is proposed, targeting field-programmable gate array (FPGA) devices. The architecture supports frame parallelism to maximize the utilization of the processing units, significantly improving the processing rate. The controller unit was carefully designed to support all 5G configurations and to avoid update conflicts. Furthermore, an efficient data scheduling is proposed to increase the processing rate. Compared to the recent related state of the art, the proposed FPGA prototype achieves a higher processing rate per hardware resource for most configurations.

## Layered Decoding for Protograph-Based Low-Density Parity-Check Hadamard Codes

- **Status**: ✅
- **Reason**: LDPC-Hadamard 부호용 layered decoding 알고리즘 제안 — 수렴속도 2배 개선. layered 디코더 기법 이식 가능성(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9349523
- **Type**: journal
- **Published**: June 2021
- **Authors**: Peng W. Zhang, Francis C. M. Lau, Chiu-W. Sham
- **PDF**: https://ieeexplore.ieee.org/document/9349523
- **Abstract**: In this letter, we propose a layered decoding algorithm for protograph-based low-density parity-check Hadamard codes (PLDPC-HCs), which have been shown to be ultimate-Shannon-limit approaching. Compared with the standard decoding algorithm, the layered decoding algorithm improves the convergence rate by about two times. At a bit error rate of 2.0×10-5, the layered decoder using 20 decoding iterations shows a very small degradation of 0.03 dB compared with the standard decoder using 40 decoding iterations. Moreover, the layered decoder using 21 decoding iterations shows the same error performance as the standard decoder using 41 decoding iterations.

## MET-LDPC Code Ensembles of Low Code Rates With Exponentially Few Small Weight Codewords

- **Status**: ✅
- **Reason**: MET-LDPC 저부호율 앙상블 설계, small weight codeword·threshold·유한길이 — 바이너리 코드설계 기여(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9367180
- **Type**: journal
- **Published**: June 2021
- **Authors**: Suhwang Jeong, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/9367180
- **Abstract**: This work studies the design of MET-LDPC code ensembles at low code rates with good threshold performances and exponentially few small weight codewords. There was a notable study on the condition, so called the ` t-value condition', for exponentially few small weight codewords. Meanwhile, it was shown that by introducing degree-one variable nodes, the threshold performances of MET-LDPC code ensembles of low rates can be significantly improved. However, the degree-one variable nodes may result in small weight codewords and thus must be carefully introduced to MET-LDPC code ensembles. Despite the importance, the existing t-value condition was developed only for MET-LDPC code ensembles without degree-one variable nodes. This work extends the t-value condition to MET-LDPC code ensembles with degree-one variable nodes, which includes the existing work as a special case. The extended t-value condition provides useful insights into the contributions of degree-one variable nodes to the distribution of small weight codewords. Thus, the results of this work allow us to design MET-LDPC code ensembles of low rates with both good threshold performances and exponentially few small weight codewords. In addition, it will be demonstrated that MET-LDPC codes at finite lengths based on the designed code ensembles have good error-rate performances both in the waterfall and low-error-rate regions.

## Nested Array-Based Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: array-based SC-LDPC의 dominant absorbing set 최소화 최적화 — 바이너리 코드설계/error floor 기법(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9361568
- **Type**: journal
- **Published**: June 2021
- **Authors**: Salman Habib, David G. M. Mitchell, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/9361568
- **Abstract**: Linear nested codes, where two or more sub-codes are nested in a global code, have been proposed as candidates for reliable multi-terminal communication. In this article, we consider nested array-based spatially coupled low-density parity-check (SC-LDPC) codes and propose a line-counting based optimization scheme for minimizing the number of dominant absorbing sets in order to improve its performance in the high signal-to-noise ratio regime. Since the parity-check matrices of different nested sub-codes partially overlap, the optimization of one nested sub-code imposes constraints on the optimization of the other sub-codes. To tackle these constraints, a multi-step optimization process is applied first to one of the nested codes, then sequential optimization of the remaining nested codes is carried out based on the constraints imposed by the previously optimized sub-codes. Results show that the order of optimization has a significant impact on the number of dominant absorbing sets in the Tanner graph of the code, resulting in a trade-off between the performance of a nested code structure and its optimization sequence: the code which is optimized without constraints has fewer harmful structures than the code which is optimized with constraints. We also show that for certain code parameters, dominant absorbing sets in the Tanner graphs of all nested codes are completely removed using our proposed optimization strategy.

## Spatially Coupled Generalized LDPC Codes: Asymptotic Analysis and Finite Length Scaling

- **Status**: ✅
- **Reason**: SC-GLDPC 코드 설계+유한길이 스케일링+error floor/minimum distance 분석 — 바이너리 코드 설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9398939
- **Type**: journal
- **Published**: June 2021
- **Authors**: David G. M. Mitchell, Pablo M. Olmos, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/9398939
- **Abstract**: Generalized low-density parity-check (GLDPC) codes are a class of LDPC codes in which the standard single parity check (SPC) constraints are replaced by constraints defined by a linear block code. These stronger constraints typically result in improved error floor performance, due to better minimum distance and trapping set properties, at a cost of some increased decoding complexity. In this paper, we study spatially coupled generalized low-density parity-check (SC-GLDPC) codes and present a comprehensive analysis of these codes, including: (1) an iterative decoding threshold analysis of SC-GLDPC code ensembles demonstrating capacity approaching thresholds via the threshold saturation effect; (2) an asymptotic analysis of the minimum distance and free distance properties of SC-GLDPC code ensembles, demonstrating that the ensembles are asymptotically good; and (3) an analysis of the finite-length scaling behavior of both GLDPC block codes and SC-GLDPC codes based on a peeling decoder (PD) operating on a binary erasure channel (BEC). Results are compared to GLDPC block codes, and the advantages and disadvantages of SC-GLDPC codes are discussed.

## ADMM Check Node Penalized Decoders for LDPC Codes

- **Status**: ✅
- **Reason**: 새 ADMM check-node penalized 디코더, error floor 개선 — NAND 바이너리 LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9378578
- **Type**: journal
- **Published**: June 2021
- **Authors**: Haoyuan Wei, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9378578
- **Abstract**: Alternating direction method of multipliers (ADMM) is an efficient implementation of linear programming (LP) decoding for low-density parity-check (LDPC) codes. By adding penalty terms to the objective function of the LP decoding model, ADMM variable node (VN) penalized decoding can suppress the non-integral solutions and improve the frame error rate (FER) performance in the low signal-to-noise ratio (SNR) region. In this paper, we propose a novel ADMM check node (CN) penalized decoding algorithm. Codeword solutions which satisfy all parity-check equations will have smaller penalty values than non-codeword solutions, including the non-integral solutions. We discuss the required properties of CN-penalty functions, propose a few functions that satisfy those properties, and study their performance/complexity trade-offs. We also investigate the convergence properties of the proposed algorithm and prove that its performance is independent of the transmitted codeword. Using Monte Carlo simulations and instanton analysis, we then demonstrate that the proposed CN-penalized decoder outperforms ADMM VN penalized decoders in both waterfall and error floor regions. This comes at the expense of some increase in the decoding complexity.

## NOLD: A neural-network optimized low-resolution decoder for LDPC codes

- **Status**: ✅
- **Reason**: 신경망 최적화 저해상도(2-4bit) min-sum 디코더 — NAND LLR 양자화/저정밀 디코더에 직결(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9445813
- **Type**: journal
- **Published**: June 2021
- **Authors**: Lei Chu, Huanyu He, Ling Pei +1
- **PDF**: https://ieeexplore.ieee.org/document/9445813
- **Abstract**: The min-sum (MS) algorithm can decode Low-density parity-check (LDPC) codes with low computational complexity at the cost of slight performance loss. It is an effective way to realize hardware implementation of the min-sum decoder by quantizing the floating belief messages (i.e., check-to-variable messages and variable-to-check messages) into low-resolution (i.e., 2–4 bits) versions. However, such a way can lead to severe performance degradation due to the finite precision effect. In this paper, we propose a neural-network optimized low-resolution decoding (NOLD) algorithm for LDPC codes to deal with the problem. Specifically, the optimization of decoding parameters (i.e., scaling factors and quantization step) is achieved in a hybrid way, in which we concatenate a NOLD decoder with a customized neural network. All learnable parameters associated with the decoding parameters are assigned to each neuron in the proposed method. What's more, we design a new activation function whose outputs are close to the employed quantizer ones when network parameters are finally optimized off-line. Finally, the performance of the proposed method is verified by numerous experiments. For the case of 2-bit decoding, the proposed approach significantly outperforms several conventional decoders at the expense of slightly increased off-line training time. Besides, the proposed method with 4-bit quantization incurs only 0.1 dB performance loss compared with the floating min-sum decoder at the coded bit-error-rate of 10−5. Moreover, we show that the proposed NOLD decoder works over a wide range of channel conditions for regular and irregular LDPC codes. Simulation code for reproductive results is publicly available1.

## Belief Propagation Decoding of Short Graph-Based Channel Codes via Reinforcement Learning

- **Status**: ✅
- **Reason**: RL 기반 CN 스케줄링 BP 디코더(신경망/순차 스케줄링) — 바이너리 LDPC 디코더 개선 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9406115
- **Type**: journal
- **Published**: June 2021
- **Authors**: Salman Habib, Allison Beemer, Jörg Kliewer
- **PDF**: https://ieeexplore.ieee.org/document/9406115
- **Abstract**: In this work, we consider the decoding of short sparse graph-based channel codes via reinforcement learning (RL). Specifically, we focus on low-density parity-check (LDPC) codes, which for example have been standardized in the context of 5G cellular communication systems due to their excellent error correcting performance. LDPC codes are typically decoded via belief propagation on the corresponding bipartite (Tanner) graph of the code via flooding, i.e., all check and variable nodes in the Tanner graph are updated at once. We model the node-wise sequential LDPC scheduling scheme as a Markov decision process (MDP), and obtain optimized check node (CN) scheduling policies via RL to improve sequential decoding performance as compared to flooding. In each RL step, an agent decides which CN to schedule next by observing a reward associated with each choice. Repeated scheduling enables the agent to discover the optimized CN scheduling policy which is later incorporated in our RL-based sequential LDPC decoder. In order to reduce RL complexity, we propose a novel graph-induced CN clustering approach to partition the state space of the MDP in such a way that dependencies between clusters are minimized. Compared to standard decoding approaches from the literature, some of our proposed RL schemes not only improve the decoding performance, but also reduce the decoding complexity dramatically once the scheduling policy is learned. By concatenating an outer Hamming code with an inner LDPC code which is decoded based on our learned policy, we demonstrate significant improvements in the decoding performance compared to other LDPC decoding policies.

## Construction of Time Invariant Spatially Coupled LDPC Codes Free of Small Trapping Sets

- **Status**: ✅
- **Reason**: SC-LDPC 구성 기법으로 small trapping set 제거·error floor 저감 — 바이너리 코드설계 새 기여(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9359793
- **Type**: journal
- **Published**: June 2021
- **Authors**: Sima Naseri, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9359793
- **Abstract**: In this paper, we propose a design technique for the construction of variable-regular time-invariant spatially-coupled low-density parity-check (SC-LDPC) codes with small constraint length and low error floor. The proposed technique reduces the error floor by imposing simple constraints on the short cycles in the code's Tanner graph, which in turn, result in the elimination of the most dominant trapping sets of the code. In some cases, we also derive lower bounds on the syndrome former memory for satisfying such constraints. The designed codes are superior to the state-of-the-art in terms of error floor performance and/or decoding complexity and latency.

## A 336 Gbit/s Full-Parallel Window Decoder for Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC Full-Parallel Window Decoder HW 아키텍처, critical path/라우팅 개선 신규 기여(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9482457
- **Type**: conference
- **Published**: 8-11 June 
- **Authors**: Matthias Herrmann, Norbert Wehn, Max Thalmaier +3
- **PDF**: https://ieeexplore.ieee.org/document/9482457
- **Abstract**: Low―Density Parity-Check (LDPC) codes are among the most powerful Forward Error Correction (FEC) schemes and part of many communication standards. Emerging use cases are expected to require data rates towards Tbit/s, which is one to two orders of magnitude higher than the throughput specified in 5G-NR. For throughputs towards Tbit/s, state-of-the-art LDPC soft decoders are restricted to short code block sizes of several hundreds to thousands of bits due to routing congestion challenges, forcing a firm limit to the overall communications performance of the transmission system. In this paper, we focus on a relatively new class of LDPC codes, denoted as Spatially Coupled LDPC (SC-LDPC) codes. For the first time, we show that these codes enable efficient, very high throughput (>> 100 Gbit/s) decoding of large code block sizes. To this end, we present an SC-LDPC decoder for a length $N$ = 51328 terminated SC-LDPC code with sub-block size $c$ = 640 and coupling width ms= 1, that achieves a throughput of 336 Gbit/s in a 22nm FD-SOI technology, which is about 50 times higher than the fastest SC-LDPC decoder in literature. In contrast to existing work, the presented decoder is based on the Full-Parallel Window Decoder (FPWD) architecture. We propose algorithmic and architectural modifications to shorten the critical path and to reduce the routing complexity of the FPWD resulting in higher throughput as well as better energy and area efficiency for the modified decoder. The decoder furthermore outperforms a state-of-the-art reference architecture that was implemented for the same code in the same technology in terms of throughput and latency.

## Blind Neural Belief Propagation Decoder for Linear Block Codes

- **Status**: ✅
- **Reason**: blind neural BP 디코더(RNN, gating/weight sharing), 신경망 디코더 신규 기여, NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9482479
- **Type**: conference
- **Published**: 8-11 June 
- **Authors**: Guillaume Larue, Louis-Adrien Dufrene, Quentin Lampin +3
- **PDF**: https://ieeexplore.ieee.org/document/9482479
- **Abstract**: Neural belief propagation decoders were recently introduced by Nachmani et al. as a way to improve the decoding performance of belief propagation iterative algorithm for short to medium length linear block codes. The main idea behind these decoders is to represent belief propagation as a neural network, enabling adaptive weighting of the decoding process. In the present paper an efficient recurrent neural network architecture, based on gating and weights sharing mechanisms, is proposed to perform blind neural belief propagation decoding without prior knowledge of the coding scheme used by the encoder. The proposed architecture is able to learn to decode BCH (15,11) and BCH (15,7) codes at least at the level of performance of a standard belief propagation algorithm and even to outperform it in the case of BCH (15,11) code thanks to NBP approach. A particular emphasis is given to the interpretability and complexity of the proposed model to ensure scalability to larger codes.

## Efficient BP-based Decoding Algorithms for QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 self-correction 기법 + adjusted min-sum으로 error floor·waterfall 개선 — 이식 가능 디코더 알고리즘(C/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9460244
- **Type**: conference
- **Published**: 7-10 June 
- **Authors**: Konstantin Zavertkin, Anastasia Panarina, Aleksei Ovinnikov +1
- **PDF**: https://ieeexplore.ieee.org/document/9460244
- **Abstract**: In this paper we propose to use a self-correction technique with two computationally efficient LDPC decoding algorithms: QRCBP and adjusted min-sum. It is shown that using such a technique allows to improve performance of this algorithms both in error floor and waterfall regions. Also comparison with other BP-based simplified decoding algorithms is presented for three quasi-cyclic LDPC codes.

## Neural Layered Min-Sum Decoding for Protograph LDPC Codes

- **Status**: ✅
- **Reason**: Neural layered min-sum decoder for protograph LDPC with greedy training; portable min-sum decoder enhancement (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9414543
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Dexin Zhang, Jincheng Dai, Kailin Tan +4
- **PDF**: https://ieeexplore.ieee.org/document/9414543
- **Abstract**: In this paper, layered min-sum (MS) iterative decoding is formulated as a customized neural network following the sequential scheduling of check node (CN) updates. By virtue of the lifting structure of protograph low-density parity-check (LDPC) codes, identical network parameters are shared among all derived edges originating from the same edge in the protograph, which makes the number of learn- able parameters manageable. The proposed neural layered MS decoder can support arbitrary codelengths consequently. Moreover, an iteration-wise greedy training method is proposed to tune the parameters such that it avoids the vanishing gradient problem and accelerates the decoding convergence.

## Learned Decimation for Neural Belief Propagation Decoders : Invited Paper

- **Status**: ✅
- **Reason**: Learned decimation for neural belief propagation on short binary LDPC; portable neural decoder improvement (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9414407
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Andreas Buchberger, Christian Häger, Henry D. Pfister +2
- **PDF**: https://ieeexplore.ieee.org/document/9414407
- **Abstract**: We introduce a two-stage decimation process to improve the performance of neural belief propagation (NBP), recently introduced by Nachmani et al., for short low-density parity-check (LDPC) codes. In the first stage, we build a list by iterating between a conventional NBP decoder and guessing the least reliable bit. The second stage iterates between a conventional NBP decoder and learned decimation, where we use a neural network to decide the decimation value for each bit. For a (128,64) LDPC code, the proposed NBP with decimation outperforms NBP decoding by 0.75dB and performs within 1dB from maximum-likelihood decoding at a block error rate of 10−4.

## High-Throughput VLSI Architecture for Soft-Decision Decoding with ORBGRAND

- **Status**: ✅
- **Reason**: ORBGRAND 소프트디시전 디코딩의 고처리량 VLSI 아키텍처 — 임의 선형부호 디코더 HW로 LDPC ECC에 이식 가능 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9414908
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Syed Mohsin Abbas, Thibaud Tonnellier, Furkan Ercan +2
- **PDF**: https://ieeexplore.ieee.org/document/9414908
- **Abstract**: Guessing Random Additive Noise Decoding (GRAND) is a recently proposed approximate Maximum Likelihood (ML) decoding technique that can decode any linear error-correcting block code. Ordered Reliability Bits GRAND (ORBGRAND) is a powerful variant of GRAND, which outperforms the original GRAND technique by generating error patterns in a specific order. Moreover, their simplicity at the algorithm level renders GRAND family a desirable candidate for applications that demand very high throughput. This work reports the first-ever hardware architecture for ORBGRAND, which achieves an average throughput of up to 42.5 Gbps for a code length of 128 at an SNR of 10 dB. Moreover, the proposed hardware can be used to decode any code provided the length and rate constraints. Compared to the state-of-the-art fast dynamic successive cancellation flip decoder (Fast-DSCF) using a 5G polar (128,105) code, the proposed VLSI implementation has 49× more average throughput while maintaining similar decoding performance.

## Towards Practical Near-Maximum-Likelihood Decoding of Error-Correcting Codes: An Overview

- **Status**: ✅
- **Reason**: Overview of near-ML decoders (GRAND, LP, ML-aided, RPA) with HW considerations; portable decoder algorithm survey (C), borderline kept per ambiguous rule.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9414311
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Thibaud Tonnellier, Marzieh Hashemipour, Nghia Doan +2
- **PDF**: https://ieeexplore.ieee.org/document/9414311
- **Abstract**: While in the past several decades the trend to go towards increasing error-correcting code lengths was predominant to get closer to the Shannon limit, applications that require short block length are developing. Therefore, decoding techniques that can achieve near-maximum-likelihood (near-ML) are gaining momentum. This overview paper surveys recent progress in this emerging field by reviewing the GRAND algorithm, linear programming decoding, machine-learning aided decoding and the recursive projection-aggregation decoding algorithm. For each of the decoding algorithms, both algorithmic and hardware implementations are considered, and future research directions are outlined.

## ADMM-Based ML Decoding: from Theory to Practice

- **Status**: ✅
- **Reason**: ADMM 기반 ML 디코딩의 알고리즘/구현 기법 — sparse code LP 디코딩으로 LDPC 디코더에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9414728
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Kira Kraft, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/9414728
- **Abstract**: Integer Linear Programming (ILP) is a general method to solve the Maximum-Likelihood (ML) decoding problem for all kinds of binary linear codes. To this end, state-of-the-art techniques use a Branch-and-Bound (B&B) framework to partition the underlying integer linear problem into several relaxed linear problems. These linear problems then have to be solved in reasonable time by an efficient Linear Programming (LP) solver. Recently, the Alternating Direction Method of Multipliers (ADMM) has been proposed for efficient software and hardware LP decoding of sparse codes, hence, an ADMM-based ML decoder seems to be a promising approach. In this paper, we investigate this approach with respect to its algorithmic and implementation-specific challenges.

## A 5G-Oriented LDPC Encoder Based on Byte-Parallel Configurable Cyclic Shift

- **Status**: ✅
- **Reason**: 5G LDPC 인코더의 byte-parallel cyclic shift 알고리즘+DSP 명령어 확장 — permutation/shift HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9463607
- **Type**: conference
- **Published**: 4-7 June 2
- **Authors**: Yisong Sun, Huan Li, Chen Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/9463607
- **Abstract**: In this paper, we propose a Byte-Parallel Configurable Cyclic Shift (BP-CCS) algorithm, which converts the cyclic shift into a byte-parallel form. This method alleviates the low efficiency of cyclic shift calculation in Low Density Parity Check (LDPC) encoding under the 5G protocol effectively. Besides, we also expand the instruction set of self-developed DSP Universal Communication Processor (UCP) to cope with the hardware implementation bottleneck of BP-CCS algorithm. This allows the implementation of a BP-CCS-based LDPC encoder on UCP, which has been verified on the taped-out chip. Experimental results show that the time consumed by the BP-CCS-based LDPC encoder is about 1/50 of the time specified in 5G communication protocol standard, and the encoder architecture can be easily reconstructed in real time through parameter configuration.

## About Constructing Block Permutation LDPC Codes for Channels with Memory

- **Status**: ✅
- **Reason**: 새 코드 설계 기법(zero-mask superimposed block-permutation LDPC 구성)으로 burst-error 정정 - 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9470529
- **Type**: conference
- **Published**: 31 May-4 J
- **Authors**: A. A. Fominykh, M. N. Isaeva, A. A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/9470529
- **Abstract**: This article examines constructing block-permutation low-density parity-check codes for error burst correction. Block-permutation constructions with superimposed zero masks are considered. We have analyzed the approach of construction such matrices consisting of two stages: finding the location of zero blocks and finding the base matrix. Experimental results containing analysis of correction capability of considered codes over the channel with memory are presented.

## An efficient Channel Coding Architecture for 5G Wireless using High-Level Synthesis

- **Status**: ✅
- **Reason**: HLS 기반 5G LDPC 인코더/디코더 고처리량 아키텍처 제안 — 이식 가능 HW 아키텍처(D).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9453001
- **Type**: conference
- **Published**: 3-5 June 2
- **Authors**: K Jaya Sampath, N Kiran Kumar, K Yeswanth +3
- **PDF**: https://ieeexplore.ieee.org/document/9453001
- **Abstract**: In today's fast paced world, the demand for Mobile Internet is increasing day by day. The fourth generation (4G) systems are now in use world-wide. The present day's 4G LTE has some challenges left such as higher data rates and spectral efficiency due to the tremendous increase in the number of mobile internet users. This led us to a situation of replacing Turbo codes of 4G systems with a channel code that promises higher throughputs. Ever since, the 3GPP had accepted the LDPC codes as a channel coding scheme for 5G wireless communications, a lot of research is going on to optimize the decoder. In 5G, polar codes and LDPC codes are used for error correction for the control channel and data channel respectively. The prime objectives of fifth generation systems are higher data rate, higher spectral efficiency, higher throughput, higher bandwidth, and higher energy efficiency that too at lower latency. There are enormous challenges in the implementation of Channel coding techniques for meeting the requirements of 5G. This highly motivated us to work on the design of efficient LDPC encoder and decoder. Channel coding plays a vital role in any wireless communication system. This work presents a novel efficient high-throughput encoder and decoder for Low Density Parity Check codes for 5th generation wireless Communications. This work proposes strategies to achieve high-throughput Channel coding architecture for LDPC codes using HLS. The proposed design achieves peak throughputs which sufficiently meets the throughput requirement for the 5G NR standard.

## Optimized Implementation of LDPC Codes for MF-TDMA Based Satellite Systems

- **Status**: ✅
- **Reason**: D — GPU 기반 LDPC 디코더 구현 최적화, 병렬 HW 아키텍처 이식 가능성(애매하여 살림)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9510154
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Deepika Revankar Manjunath
- **PDF**: https://ieeexplore.ieee.org/document/9510154
- **Abstract**: The advancements in Satellite Communication with the development of DVB based systems is a bonanza, as it provides a potential solution of supporting large users. To enrich the user experience and to ensure reliable communication across noisy channels, DVB standard incorporates the powerful capabilities of LDPC codes. LDPC codes employ a robust mechanism of Error Detection and Correction, however at the cost of accruing coding complexity. Accordingly, there's a need to optimize the implementation of LDPC codes to cater the rapidly changing communication configurations and the same can be achieved using Graphic Processing Unit (GPU) that can serve as an efficient platform for the implementation of LDPC Decoder.

## Performance Balanced General Decoder Design for QC-LDPC Codes Using Vivado HLS

- **Status**: ✅
- **Reason**: Vivado HLS 기반 QC-LDPC FPGA 디코더 — 광역 파이프라인, 서브매트릭스 대각선 데이터 배치로 접근충돌 회피하는 HW 아키텍처는 NAND LDPC 디코더에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9463813
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Bingbing Wang, Jing Kang, Yan Zhu
- **PDF**: https://ieeexplore.ieee.org/document/9463813
- **Abstract**: Field-programmable gate array are frequently used to implement high-speed Low-density Parity-check (LDPC) decoders. The conventional practice is to develop a register transfer level (RTL) description of a digital circuit, which requires considerable simulation and verification, resulting in a long development cycle. High-level synthesis (HLS) tools significantly accelerate the hardware design process by using software programming languages such as C/C++. Well optimized code can be synthesized by the HLS tools into efficient hardware circuits. In this paper, we designed a Xilinx FPGA-based LDPC decoder using Vivado HLS. The decoder takes advantage of the cyclic shift of the submatrix in the parity check matrix of the quasi-cyclic LDPC (QC-LDPC) codes and uses a wide-pipeline architecture to process one row/column of all non-zero submatrices per clock cycle, with decoding throughput of hundreds of Mbps. By using different arrays to store data on multiple diagonals in a submatrix can easily avoid the performance bottleneck caused by access conflicts. In addition, the decoder has strong generality and flexibility, which has a high practical value.

## Enhanced Partially-Parallel LDPC Decoder for Near Earth Applications

- **Status**: ✅
- **Reason**: CCSDS 부분병렬 LDPC 디코더 HW 최적화 — 고순환가중 서브매트릭스 분할·메모리 정렬로 병렬성/처리율 향상, NAND LDPC 디코더 HW에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9463828
- **Type**: conference
- **Published**: 18-20 June
- **Authors**: Jing Kang, Bingbing Wang, Yufeng Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9463828
- **Abstract**: This paper presents an enhanced partially-parallel low-density parity-check (LDPC) decoder based on Consultative Committee for Space Data Systems (CCSDS) standard for high speed near Earth applications. Architectural level optimization is exploited to reduce hardware complexity and increase decoding throughput. To enchance the parallelism of the partially-parallel decoder, high circulant weight submatrix of the parity check matrix (PCM) are partitioned into several identity matrices with corresponding cyclic-shifted value and processed separately. Furthermore, messages corresponding to adjacent rows of the cyclic-shifted identity matrix are stored in one memory entry, and low-complexity data aligners are designed between memories and processing units to avoid memory access conflicts. Hardware implementation of a (8176,7154) LDPC code on Xilinx Virtex-5 XC5VLX330 FPGA shows that the proposed decoder can achieve a decoding throughput of 1.02 Gb/s at 10 iterations.

## Enumeration of the Degree Distribution Space for Finite Block Length LDPC Codes

- **Status**: ✅
- **Reason**: E: 유한 블록길이 바이너리 LDPC degree distribution 전수 열거 알고리즘. 짧은 코드 최적화 코드설계 기법, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9500939
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Spencer Giddens, Marco A. C. Gomes, João P. Vilela +2
- **PDF**: https://ieeexplore.ieee.org/document/9500939
- **Abstract**: Current methods for optimization of low-density parity-check (LDPC) codes analyze the degree distribution pair asymptotically as block length approaches infinity. This effectively ignores the discrete nature of the space of valid degree distribution pairs for LDPC codes of finite block length. While large codes are likely to conform reasonably well to the infinite block length analysis, shorter codes have no such guarantee. We present and analyze an algorithm for completely enumerating the space of all valid degree distribution pairs for a given block length, code rate, maximum variable node degree, and maximum check node degree. We then demonstrate this algorithm on an example LDPC code of finite block length. Finally, we discuss how the result of this algorithm can be utilized by discrete optimization routines to form novel methods for the optimization of small block length LDPC codes.

## Optimal Placement of Read Thresholds for Coded NAND Flash Memory

- **Status**: ✅
- **Reason**: A: NAND 플래시 read threshold 최적화. MMI+DDE 2단계 read voltage 배치, LDPC 코드 구조 반영 — NAND LDPC 직접 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9500536
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Yishen Yeh, Arman Fazeli, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/9500536
- **Abstract**: Recent advances in the flash memory technology call for more efficient error-correction codes (ECCs) than the conventional, yet very popular, ones such as BCH codes. The ability to make multiple voltage reads allows one to estimate soft values at the time of decoding, which in turn makes soft-decision ECCs such as LDPC codes a suitable candidate for implementation in flash memories. On the other hand, fully utilizing the potential of soft decision based codes demands higher precision memory sensing, which introduces a trade-off between the read latency and the error probability. In this paper, we explore and compares two approaches to optimize the positioning as well as the number of read (word-line) voltages for a specified program/erase (PE) cycle.In the first approach, we aim for selecting those read thresholds that maximize the mutual information (MMI) of the equivalent discrete memoryless channel. By utilizing conventional optimization methods such as the gradient descent (GD), we are able to find the optimal read locations for any number of read probes. Our simulation results show that ~20 reads are effective. Next, we redesign our optimization problem to take the LDPC code structure into account. To do so, we use discretized density evolution (DDE) as a proxy for bit error rate (BER), which serves as our cost function in the GD search. To overcome the problem of local minima, we propose a two-step optimization: MMI for coarse optimization, followed by DDE for fine optimization. Simulation results confirm the effectiveness of this method.1

## Coarsely Quantized Layered Decoding Using the Information Bottleneck Method

- **Status**: ✅
- **Reason**: C/D: Information Bottleneck 기반 거칠게 양자화된 layered LDPC 디코더(LUT·복잡도축소 노드). 저정밀 양자화 디코더 기법 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9500593
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Philipp Mohr, Gerhard Bauch, Fan Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/9500593
- **Abstract**: In recent years coarsely quantized LDPC decoding using a flooding schedule has been extensively studied. However, there exist few works addressing coarse quantization for a layered schedule, which enables improved convergence speed of the message passing algorithm. The layered schedule can especially be beneficial for high throughput applications like fiber optical systems. This paper presents innovative layered decoding approaches, where the information bottleneck method is used for the design of different coarsely quantized decoder architectures. The varieties of investigated node implementations include lookup tables, computational domain techniques as well as reduced complexity approximations. All structures are designed offline using a layered discrete density evolution method. The performance of multiple node architectures is investigated in terms of evolution of mutual information in the design phase and in terms of error rates. We focus in this paper on regular quasi-cyclic codes. Our simulations running on GPUs also allow insights into the error floor behavior.
