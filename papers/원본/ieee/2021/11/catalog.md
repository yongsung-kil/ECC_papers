# IEEE Xplore — 2021-11


## Neural Layered Decoding of 5G LDPC Codes

- **Status**: ✅
- **Reason**: C: 신경망 layered min-sum(NLMS/NOMS) 디코더, 정규화·오프셋 학습. 바이너리 LDPC 디코더 신기법, 이식 가능.
- **ID**: ieee:9540676
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Nemin Shah, Yash Vasavada
- **PDF**: https://ieeexplore.ieee.org/document/9540676
- **Abstract**: In this letter, we propose various low-complexity neural layered min-sum (NLMS) algorithms to improve the decoding performance of the fifth generation (5G) new radio (NR) low-density parity-check (LDPC) codes. Our proposals are based on the computationally-efficient normalized offset min-sum (NOMS) approach for the layered belief propagation (LBP). The main novelty of our proposals is a deep neural network (DNN) that implements the layered mode decoding and that additionally learns the normalization and the offset parameters of the NOMS scheme. The schemes that we propose use the DNN as well as adaptation and filtering for estimating the optimum values of these parameters. We show by simulation that our proposed decoders achieve a significant computational benefit compared to the standard (non-neural) LBP decoder without an appreciable performance penalty.

## Construction of Multi-Rate Quasi-Cyclic LDPC Codes for Satellite Communications

- **Status**: ✅
- **Reason**: E: 멀티레이트 QC-LDPC 구성 신기법(progressive row elimination/addition, nested 구조, error floor 억제). 이식 가능 바이너리 코드설계.
- **ID**: ieee:9521885
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Chong Zhang, Xijin Mu, Jinhong Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/9521885
- **Abstract**: To provide reliable transmissions with flexible rates for satellite communications, this paper presents a novel method of constructing multi-rate quasi-cyclic low-density parity-check (LDPC) codes. The basic idea is to generate low-rate codes from a high-rate mother code by combining shortening and extending, which ensures that the generated code family owns the same code length, in order to maintain the same frame structure. The code construction involves the design of base matrices and exponent matrices for the designed codes. A progressive row elimination and addition algorithm is proposed for designing the code base matrices from a high rate to low rates. This algorithm leads to the nested and systematic structure of the parity-check matrices, which are desirable for practical implementations of their encoders and decoders, while ensuring the optimal decoding thresholds. In addition, we construct a circulation coefficient matrix based on finite fields and select the optimal rows in this matrix to construct exponent matrices while considering of cycle structures. We demonstrate that the designed codes achieve better performance for all the code rates than the LDPC codes in DVB-S2X standards. In addition, the proposed codes do not exhibit error floors for their block error rates down to 10−5.

## Design of Bilayer and Multi-Layer LDPC Ensembles From Individual Degree Distributions

- **Status**: ✅
- **Reason**: E: 바이너리 bilayer/multi-layer LDPC 앙상블 설계 신기법(개별 차수분포 기반, 저복잡 디코딩 스케줄). 이식 가능 코드설계.
- **ID**: ieee:9517123
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9517123
- **Abstract**: A new approach for designing bilayer and multi-layer LDPC codes is proposed and studied in the asymptotic regime. The ensembles are defined through individual uni-variate degree distributions, one for each layer. We present a construction that: 1) enables low-complexity decoding for high-SNR channel instances, 2) provably approaches capacity for low-SNR instances, 3) scales linearly (in terms of design complexity) in the number of layers. For the setup where decoding the second layer is significantly more costly than the first layer, we propose an optimal-cost decoding schedule and study the trade-off between code rate and decoding cost.

## Windowed Decoding for Delayed Bit-Interleaved Coded Modulation

- **Status**: ❌
- **Reason**: DBICM용 windowed decoding은 변조·sub-block 지연 검출 특이적. LDPC ECC로 이식할 새 기법 아님.
- **ID**: ieee:9521215
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Yihuan Liao, Min Qiu, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/9521215
- **Abstract**: Delayed bit-interleaved coded modulation (DBICM) generalizes bit-interleaved coded modulation (BICM) by modulating differently delayed sub-blocks of codewords onto the same signals. DBICM improves transmission reliability over BICM due to its capability of detecting undelayed sub-blocks with the extrinsic information of the decoded delayed sub-blocks. In this work, we propose a novel windowed decoding algorithm for DBICM, which uses the extrinsic information of both the decoded delayed and undelayed sub-blocks, to improve the detection on all sub-blocks. Numerical results show that the proposed windowed decoding significantly outperforms the original decoding.

## Hybrid-ARQ Protocols Based on Tornado Codes for the Packet Erasure Channel

- **Status**: ❌
- **Reason**: Tornado(fountain/erasure) 기반 hybrid-ARQ. 소거채널·ARQ 특이적, 떼어낼 NAND ECC 기법 없음.
- **ID**: ieee:9520395
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Srinath Puducheri-Sundaravaradhan, Thomas E. Fuja
- **PDF**: https://ieeexplore.ieee.org/document/9520395
- **Abstract**: Lossless data transfer over communication networks has traditionally been achieved by means of ARQ protocols. However, the last ten years have seen an increasing interest in using erasure-correcting codes as an alternative, with the goal of reducing latency, feedback overhead, etc. Since these two approaches possess advantages as well as drawbacks, several hybrid ARQ schemes have also been proposed as good compromise solutions, in order to attain the “best of both worlds”. Extending this principle, this paper develops new classes of hybrid ARQ protocols for erasure channels that allow for flexible trade-offs between two important cost metrics, viz., the computational complexity of coding, and the amount of feedback needed. Our hybrid schemes make use of Tornado codes – a class of low-complexity capacity-achieving erasure codes – whose coding structure is well-suited for feedback-based communications. These schemes demonstrate significant cost reductions versus coding-only and feedback-only approaches over a wide region of interest. Moreover, these schemes are easily tuned to achieve different operating points on a trade-off curve. Finally, the proposed schemes showcase novel means of interweaving coding and feedback.

## Across-Array Coding for Resistive Memories With Sneak-Path Interference and Lognormal Distributed Resistance Variations

- **Status**: ✅
- **Reason**: B: ReRAM 메모리 채널 LLR 생성 및 LDPC 코드워드 across-array 비트할당 신기법. 스토리지 ECC 직접.
- **ID**: ieee:9531624
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Panpan Li, Guanghui Song, Kui Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/9531624
- **Abstract**: Resistive random-access memory (ReRAM) is a promising non-volatile memory technology for achieving high-density and high-speed data storage. However, its crossbar array structure leads to a severe problem known as the sneak path interference (SPI), which is data dependent and correlated within a memory array. Meanwhile, variations of the memory fabrication process also cause deviation of memory cell resistances from their nominal values, which typically follows the lognormal distribution. In this letter, we first propose a cascaded channel model that incorporates these two key factors that affect the reliability of ReRAM. By analyzing the channel correlation of ReRAM caused by the SPI, we develop a novel scheme to estimate the probability of each memory cell to be affected by the SPI, based on which the log-likelihood ratio (LLR) of each channel bit can be generated. Moreover, we propose a novel two-step across-array bit allocation scheme, which distributes the low-density parity-check (LDPC) codewords to multiple memory arrays so as to minimize the correlation of the channel coded bits for decoding. Simulation results show that the proposed across-array bit allocation scheme with LDPC coding can achieve significantly better error rate performance than the prior art coding schemes, with similar implementation complexity and latency.

## A Type-Aware Coding Approach to Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: JSCC를 PAC 코드로 구현. 소스-채널 결합·polar 계열, LDPC ECC 기법 아님.
- **ID**: ieee:9536738
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Xinyuanmeng Yao, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/9536738
- **Abstract**: In this letter, we propose a type-aware coding approach to joint source-channel coding (JSCC) and present a concrete construction with polarization-adjusted convolutional (PAC) codes. A data sequence is first encoded by enumerative coding and then encoded by a data-dependent PAC code, resulting in a transmitted codeword. At the receiver, a type-search decoding algorithm is employed, and the implementation complexity can be reduced by searching only those typical types. Simulation results show that the presented JSCC scheme can outperform the conventional tandem coding scheme with a fixed-to-fixed-length source code and achieve a performance within the gap between the upper and lower bound on the minimum FER of finite-length JSCCs.

## Robust Rateless Spatially Coupled Repeat-Accumulate-Repeat Multi-User Codes on IDMA Systems

- **Status**: ❌
- **Reason**: IDMA용 rateless SC-RA-R 다중사용자 코드. 다중접속·rateless 특이적, NAND ECC로 떼어낼 기법 없음.
- **ID**: ieee:9531433
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Yifei Zhang, Wei Hou, Ying Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9531433
- **Abstract**: In this paper, we design a kind of robust rateless multi-user code, which is called spatially coupled repeat-accumulate-repeat (SC-RA-R) code, for the interleave-division multiple-access (IDMA) system. The code is constructed by serially concatenating a fixed outer spatially coupled repeat-accumulate (SC-RA) code with an adjustable inner irregular repetition code. It achieves rateless property by simply adjusting the parameters of the inner repetition code. The IDMA system with the proposed SC-RA-R multi-user codes can adapt to varying channel qualities and varying number of users via rateless property while keeping encoder and decoder implementation unchanged. Analytical extrinsic information transfer (EXIT) functions are derived to determine belief propagation (BP) decoding thresholds of SC-RA-R codes on the IDMA system. The optimization expression is also given under the constraint that repeat parameters are monotonically non-decreasing with the sum rate decreasing. The numerical results show that the maximum achievable sum rates of the SC-RA-R codes can be close to the Shannon bound for arbitrary channel qualities. Besides, our proposed SC-RA-R codes have better BP thresholds and bit-error-rate (BER) performances than the conventional optimal parallel-concatenate codes (PCC) and the optimal partially repeated spatially coupled low-density parity-check (PR-SC-LDPC) codes on IDMA systems.

## Reliable Minimum Cycle Time of 5G NR Based on Data-Driven Channel Characterization

- **Status**: ❌
- **Reason**: 5G NR 최소 사이클 타임 채널 특성화. LDPC/ECC와 무관한 무선 네트워크 지연 분석
- **ID**: ieee:9328517
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Xiaolin Jiang, Michele Luvisotto, Zhibo Pang +1
- **PDF**: https://ieeexplore.ieee.org/document/9328517
- **Abstract**: Wireless communication is evolving to support critical control in automation systems. The fifth-generation (5G) mobile network air interface New Radio adopts a scalable numerology and mini-slot transmission for short packets that make it potentially suitable for critical control systems. The reliable minimum cycle time is an important indicator for industrial communication techniques but has not yet been investigated within 5G. To address such a question, this article considers 5G-based industrial networks and uses the delay optimization based on data-driven channel characterization (CCDO) approach to propose a method to evaluate the reliable minimum cycle time of 5G. Numerical results in three representative industrial environments indicate that following the CCDO approach, 5G-based industrial networks can achieve, in real-world scenario, millisecond-level minimum cycle time to support several hundred nodes with reliability higher than 99.9999%.

## Practical RIS-Aided Coded Systems: Joint Precoding and Passive Beamforming

- **Status**: ❌
- **Reason**: RIS 보조 시스템 precoding/passive beamforming 최적화. FEC는 일반 언급, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9495932
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Mingyang Yue, Lei Liu, Xiaojun Yuan
- **PDF**: https://ieeexplore.ieee.org/document/9495932
- **Abstract**: Reconfigure intelligent surface (RIS) is considered as a promising technology for next generation wireless networks to improve spectrum efficiency or energy efficiency. This letter, for the first time, investigates a practical RIS-aided coded system. Specially, we consider a forward-error-correction (FEC) code and a linear precoder at the transmitter, while a low-complexity iterative receiver is adopted. In addition, the inter-symbol interference (ISI) channels are considered. We aim to jointly optimize the precoding and the passive beamforming of the RIS to minimize the transmission power given the bit error rate (BER). To solve this non-convex optimization problem, we utilize the alternate optimization to iteratively optimize the precoding and passive beamforming, which are respectively a convex problem and a fractional programming problem. Numerical results show that significant performance improvement can be achieved with the proposed optimization scheme.

## Update Bandwidth for Distributed Storage

- **Status**: ❌
- **Reason**: 분산 스토리지 MDS 어레이 코드의 update bandwidth/redundancy 이론·구성. LDPC ECC 디코더/코드설계 기법 없음.
- **ID**: ieee:9514857
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Zhengrui Li, Sian-Jheng Lin, Po-Ning Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/9514857
- **Abstract**: In this paper, we consider the update bandwidth in distributed storage systems (DSSs). The update bandwidth, which measures the transmission efficiency of the update process in DSSs, is defined as the average amount of data symbols transferred in the network when the data symbols stored in a node are updated. This paper contains the following contributions. First, we establish the closed-form expression of the minimum update bandwidth attainable by irregular array codes. Second, after defining a class of irregular array codes, called Minimum Update Bandwidth (MUB) codes, which achieve the minimum update bandwidth of irregular array codes, we determine the smallest code redundancy attainable by MUB codes. Third, the code parameters, with which the minimum code redundancy of irregular array codes and the smallest code redundancy of MUB codes can be equal, are identified, which allows us to define MR-MUB codes as a class of irregular array codes that simultaneously achieve the minimum code redundancy and the minimum update bandwidth. Fourth, we introduce explicit code constructions of MR-MUB codes and MUB codes with the smallest code redundancy. Fifth, we establish a lower bound of the update complexity of MR-MUB codes, which can be used to prove that the minimum update complexity of irregular array codes may not be achieved by MR-MUB codes. Last, we construct a class of  $(n = k + 2, k)$  vertical maximum-distance separable (MDS) array codes that can achieve all of the minimum code redundancy, the minimum update bandwidth and the optimal repair bandwidth of irregular array codes.

## Optimal Quantizer Structure for Maximizing Mutual Information Under Constraints

- **Status**: ✅
- **Reason**: C/A 관련: 상호정보 최대화 최적 양자화기 설계(임계값 수 상한). NAND LLR 양자화에 직접 이식 가능.
- **ID**: ieee:9530430
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Thuan Nguyen, Thinh Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9530430
- **Abstract**: Consider a channel whose the input alphabet set  $\mathbb {X}=\{x_{1},x_{2}, {\dots },x_{K}\}$  contains  $K$  discrete symbols modeled as a discrete random variable  $X$  having a probability mass function  $\mathbf {p}(\mathbf {x}) = [p(x_{1}), p(x_{2}), {\dots }, p(x_{K})]$  and the received signal  $Y$  being a continuous random variable.  $Y$  is a distorted version of  $X$  caused by a channel distortion, characterized by the conditional densities  $p(y|x_{i})=\phi _{i}(y)$ ,  $i=1,2, {\dots },K$ . To recover  $X$ , a quantizer  $Q$  is used to quantize  $Y$  back to a discrete output  $\mathbb {Z} =\{z_{1}, z_{2}, {\dots }, z_{N}\}$  corresponding to a random variable  $Z$  with a probability mass function  $\mathbf {p}(\mathbf {z}) = [p(z_{1}), p(z_{2}), {\dots }, p(z_{N})]$  such that the mutual information  $I(X;Z)$  is maximized subject to an arbitrary constraint on  $\mathbf {p}(\mathbf {z})$ . Formally, we are interested in designing an optimal quantizer  $Q^{*}$  that maximizes  $\beta I(X;Z) - C(Z)$  where  $\beta $  is a positive number that controls the trade-off between maximizing  $I(X;Z)$  and minimizing an arbitrary cost function  $C(Z)$ . Let  $\mathbf {p}(\mathbf {x}|y)=[p(x_{1}|y),p(x_{2}|y), {\dots },p(x_{K}|y)]$  be the posterior distribution of  $X$  for a given value of  $y$ , we show that for any arbitrary cost function  $C(.)$ , the optimal quantizer  $Q^{*}$  separates the vectors  $\mathbf {p}(\mathbf {x}|y)$  into convex regions. Using this result, a method is proposed to determine an upper bound on the number of thresholds (decision variables on  $y$ ) which is used to speed up the algorithm for finding an optimal quantizer. Numerical results are presented to validate the findings.

## A Study of Post Quantum Cipher Suites for Key Exchange

- **Status**: ❌
- **Reason**: 포스트양자 키교환 cipher suite 벤치마크(보안/암호); 채널코딩 ECC 아님
- **ID**: ieee:9619839
- **Type**: conference
- **Published**: 8-9 Nov. 2
- **Authors**: Daniel Garcia, Hong Liu
- **PDF**: https://ieeexplore.ieee.org/document/9619839
- **Abstract**: Current cryptographic solutions used in information technologies today like Transport Layer Security utilize algorithms with underlying computationally difficult problems to solve. With the ongoing research and development of quantum computers, these same computationally difficult problems become solvable within reasonable (polynomial) time. The emergence of large-scale quantum computers would put the integrity and confidentiality of today’s data in jeopardy. It then becomes urgent to develop, implement, and test a new suite of cybersecurity measures against attacks from a quantum computer. This paper explores, understands, and evaluates this new category of cryptosystems as well as the many tradeoffs among them. All the algorithms submitted to the National Institute of Standards and Technology (NIST) for standardization can be categorized into three major categories, each relating to the new underlying hard problem: namely error code correcting, algebraic lattices (including ring learning with errors), and supersingular isogenies. These new mathematical hard problems have shown to be resistant to the same type of quantum attack. Utilizing hardware clock cycle registers, the work sets up the benchmarks of the four Round 3 NIST algorithms in two environments: cloud computing and embedded system. As expected, there are many tradeoffs and advantages in each algorithm for applications. Saber and Kyber are exceedingly fast but have larger ciphertext size for transmission over a wire. McEliece key size and key generation are the largest drawbacks but having the smallest ciphertext size and only slightly decreased performance allow a use case where key reuse is prioritized. NTRU finds a middle ground in these tradeoffs, being better than McEliece performance wise and better than Kyber and Saber in ciphertext size allows for a use case of highly varied environments, which need to value speed and ciphertext size equally. Going forward, the benchmarking system developed could be applied to digital signature, another vital aspect to a cryptosystem.

## A 7Gbps (160, 80) Non-Binary LDPC Decoder with Dual-Message EMS Algorithm in 22nm FinFET Technology

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC over GF(q)) EMS 디코더 — 비이진 LDPC는 원칙 제외.
- **ID**: ieee:9634818
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/9634818
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes, defined over GF(q), have been extensively studied since analyzed by Davey and Mackay in 1998 [1]. It was demonstrated that the NB-LDPC code has superior error-correcting performance than the binary counterparts in algorithm-level investigation. However, it is hard to directly employ a high-throughput NB-LDPC decoder due to its high processing complexity and excessively long decoding latency. Based on the conventional extended min-sum (EMS) algorithm [2], which reduces the message size without losing the correcting power, we introduce a high-throughput but area-efficient NB-LDPC decoder handling multiple message elements at the same time. The previous variable node processing (VNP) is modified to accept the multiple message elements and to promote parallel processing eventually. For the efficient decoder design, the delay overheads are carefully optimized in the two-stage sorter. The prototype decoder for the (160, 80) NB- LDPC code is implemented in a 22nm FinFET technology, achieving the decoding throughput of 7 Gbps.

## On the Performance of Link Space Communications using NB-LDPC Codes on Embedded Parallel Systems

- **Status**: ❌
- **Reason**: 비이진(GF(q)≤256) NB-LDPC를 GPU에서 디코딩 — 비이진 LDPC는 즉시 제외
- **ID**: ieee:9723365
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Oscar Ferraz, Vitor Silva, Gabriel Falcao
- **PDF**: https://ieeexplore.ieee.org/document/9723365
- **Abstract**: This paper introduces a novel concept for exploiting low-power edge graphics processing units (GPUs) for decoding higher-order non-binary low-density parity-check (LDPC) codes within a good performance level. In the proposed remote system, we exploit the asynchronous and simultaneous use of CPU and GPU resources, time-encoded data streams, and the concept of multi-codeword decoding. We report a coding gain superior to 1dB compared to the binary counterpart for the optimal sum-product algorithm (SPA). We compare our proposed solution against dedicated application-specific integrated-circuit (ASIC) designs, showing that, although behind, the edge GPU is competitive in terms of performance and energy, while supporting a significantly reduced development effort. Moreover, the experiments confirm that the proposed edge architecture provides a promising framework for Galois fields of order up to 256 and also from short to moderate code length equivalent to the binary (128, 64) and (512, 256) codes, supporting efficient and low-latency remote processing, reaching 2 Mbit/s, in conformity with the CCSDS-231 standard, under a global 7W power budget.

## On Coding Techniques for Unsourced Multiple-Access

- **Status**: ❌
- **Reason**: unsourced multiple-access 코드 설계 이론(2-UBAC PUPE bound, pivot 선택); 가산채널 특이 분석으로 NAND 이식 기법 없음
- **ID**: ieee:9723359
- **Type**: conference
- **Published**: 31 Oct.-3 
- **Authors**: Gianluigi Liva, Yury Polyanskiy
- **PDF**: https://ieeexplore.ieee.org/document/9723359
- **Abstract**: In this paper, we attempt to gain insights on designing codes for unsourced multiple access by investigating an important special case of a two-user unsourced binary adder channel (2-UBAC). In 2-UBAC the receiver observes a noiseless real sum of two binary vectors. We show several results. First, for a linear code the per-user probability of error (PUPE) equals the fraction of nonminimal codewords, implying that such codes can at most achieve rate-1/2 while capacity of 2-UBAC is 3/4. Second, for sparse-graph codes to jump start an iterative peeling decoder we need to reveal ("pivot") one of the ambiguous symbols. If the pivot is selected randomly then any irregular LDPC code ensemble has a non-vanishing error probability. If the pivot is selected optimally then we show that three regular LDPC code ensembles attain vanishing PUPE: (3, 4), (4, 5) and (5, 6). Our proof does not apply to any other regular LDPC code ensembles, but we believe that they should all have a non-vanishing error probability. Finally, we discuss ideas about (nonlinear) coding to break through the rate-1/2 bottleneck.

## LLR Metrics for 1024-QAM Soft-Decision: Implementation in IEEE 802.11ax (Wi-Fi 6)

- **Status**: ✅
- **Reason**: 1024-QAM 연판정용 근사 LLR 메트릭 도출(log-domain SPA용) — LLR 근사/양자화 기법은 NAND LDPC 연판정에 이식 가능(A/C 경계, 애매하여 in)
- **ID**: ieee:9615831
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/9615831
- **Abstract**: The IEEE 802.11ax amendment (Wi-Fi 6) has defined modulation code schemes that implement uniform Gray mapping rectangular 1024-QAM constellation. In this paper, we derive approximate log-likelihood ratio (LLR) metrics for softdecoding of binary convolutional codes (BCC) using Viterbi decoding and low-density parity-check codes (LDPC) using the message-passing algorithm, implemented as the log-domain sum-product algorithm. The proposed low-complexity softdecision metrics are validated by simulating the 802.11ax physical layer that implements transmit beamforming transceivers over frequency selective channels.

## An Improved Self-Corrected Min-Sum Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: ISCMS — self-corrected min-sum의 CN 갱신 규칙 개선, 이식 가능 디코더 알고리즘 변형(C)
- **ID**: ieee:9755394
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Xingjin Li, Liguo Zhang, Jingxuan Tan +3
- **PDF**: https://ieeexplore.ieee.org/document/9755394
- **Abstract**: Low-Density Parity-Check (LDPC) code is a linear block code approaching the Shannon limit. The improvement of the decoding performance of LDPC codes is a hot research direction today. To improve the decoding performance of the self-correcting min-sum (SCMS) algorithm, an improved self-correcting min-sum (ISCMS) algorithm is proposed based on this algorithm. In the iterative decoding process of the ISCMS algorithm, the update rule of the check node (CN) is optimized to the update rule of the CN of the IOMS algorithm, which improves the accuracy of decoding from the processing of the CN. Simulation results show that the proposed ISCMS algorithm has better error performance and convergence performance than the SCMS algorithm with a small increase in computational complexity.

## Low Complexity Neural Network-Aided NMS LDPC Decoder

- **Status**: ✅
- **Reason**: NN-aided NMS 디코더 — LLR로 정규화 인자 추론하는 신경망 보조 min-sum 변형, 저복잡도 이식 가능 디코더(C)
- **ID**: ieee:9652964
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Honghao Shi, Mingyang Zhong, Zhiyong Luo +1
- **PDF**: https://ieeexplore.ieee.org/document/9652964
- **Abstract**: For recent years, deep learning has been studied and utilized among decoders in wireless and optical communication. For low density parity check (LDPC) codes, most works use neural network (NN) to implement the belief propagation (BP) decoder and unfold its iterations into layers activated by different functions. However, the whole decoder composed by neural network performs lots of non-linear operations, which are time consuming and unfriendly to hardware implementation. In this work, a neural network-aided normalized min-sum (NN-aided NMS) decoder for LDPC code is proposed, in which the normalization factors are inferred from input log likelihood ratio (LLR) by apre-trained NN, while maintaining check and variable nodes processing the same as in min-sum (MS) decoder. In order to test the proposed decoder with irregular LDPC code, a rate-7/8 one was constructed using progressive edge growth (PEG) algorithm, showing better error correction capability than the standard of consultative committee for space data systems (CCSDS) LDPC (8176,7154) code by 0.08 dB with the same rate. Simulation results show that, NN-aided NMS decoder outperforms MS decoder by 0.3 dB, and its performance approaches BP decoder with a gap of 0.02 dB, which is 50% closer than the best NMS decoder using 0.7 as the normalization factor. The proposed decoder has good performance for both regular and irregular LDPC codes, and needs much less computation complexity than BP decoder. It introduces more linear computation than NMS decoder but achieves better bit error rate (BER) performance, thus becoming a good complement between BP and NMS decoder when trading off among complexity, error correction performance and hardware implementation for wireless and satellite communication.

## Performance Analysis of Mixed MIMO-RF/MIMO-FSO DF Relaying Using Globally Coupled Low Density Parity Check (GC-LDPC) Codes and Diversity Techniques

- **Status**: ❌
- **Reason**: FSO/RF MIMO 릴레이 응용에 GC-LDPC을 베이스라인으로 사용, 표준 two-phase local-global 디코딩만 언급, NAND 이식할 새 ECC 기법 없음
- **ID**: ieee:9673895
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: Ibrahima Gueye, Idy Diop, Ibra Dioum +1
- **PDF**: https://ieeexplore.ieee.org/document/9673895
- **Abstract**: This article focuses on the performance analysis of cooperative systems hybridizing MIMO-RF/MIMO-FSO and error correcting codes including GC-LDPC codes in FSOs. In this double-hop relay system composed of links with several inputs and multiple outputs at radio frequency and with multiple inputs and multiple outputs in FSO. In this system the source transmits the information to the relay by RF links, the relay processes the information received from the source and retransmits it to the destination by FSO links. To decode the data we used two-phase local-global decoding and to eliminate interference between source-relay links and relay-destination links we use interference alignment (IA) technique. It is also assumed that the source-relay link undergoes Rayleigh fading, while the relay-destination links undergo Gamma-Gamma model fading. Using DF relay technology, hybrid MIMO-RF/MIMO-FSO systems combine the advantages of RF and FSO communication technologies. The use of hybrid MIMO- RF/MIMO-FSO cooperative transmission systems improves network reliability and transmission. In this work, we carried out a simulation study on the distribution of the total transmission power at the source and the relay level to understand the best allocations between the source and the relay in order to guarantee a good quality of reception of the data transmitted to the destination. This work also presents studies on the different combimaision techniques. The results of our simulations show that the MIMO-RF/MIMO-FSO system based on GC-LDPC codes gives better performance compared to MIMO-RF/FSO and RF/FSO systems based on the same codes but also with conventional systems without the use of codes.

## A Method of Soft-Sensing Log-Likelihood Ratios Based on Broad Learning System for NAND Flash Memories

- **Status**: ✅
- **Reason**: A — NAND 플래시 직접, BLS 기반 LLR 소프트센싱으로 multi-level read 대체하는 새 기법
- **ID**: ieee:9673965
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: Kainan Ma, Tao Li, Yibo Yin +2
- **PDF**: https://ieeexplore.ieee.org/document/9673965
- **Abstract**: To accelerate the convergence of the soft-decision decoder and improve the reading performance of the NAND flash memory, a multi-level reading method is usually adopted to sense precise log-likelihood ratios (LLR). However, multi-level readings interfere with the threshold voltage in the cells, increasing the probability of bit errors and accelerating cells wear. To solve this problem, this paper proposed an LLR soft-sensing method based on a broad learning system (BLS) to replace multi-level reading, which improves accuracy of sensing from 97.1% to 97.3% by using the raw bit error rate (RBER) as one of the inputs. The output classification probabilities of the network model are used to calculate the LLR. Compared with the multilayer perceptron model, the adoption of BLS hugely decreases the computation amount of network training from 113 epochs to 5, making on-chip retraining feasible. The proposed BLS-based LLR soft-sensing method will be of great application potential in the intelligent error control of non-volatile memories.

## LAEPS: LDPC LLR Adaptive Estimation Based on Pattern Set Distribution Variation in 3D Charge Trap NAND Flash Memories

- **Status**: ✅
- **Reason**: 3D NAND LDPC 소프트디코딩용 LLR 적응 추정(LAEPS) — NAND 직접+LLR 기법(A)
- **ID**: ieee:9661917
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Qianhui Li, Yiyang Jiang, Qi Wang +5
- **PDF**: https://ieeexplore.ieee.org/document/9661917
- **Abstract**: Low-density parity-check (LDPC) code with the soft decoding algorithm has been widely used in 3D NAND flash memories to improve the system reliability, because of its strong error correction ability. However, the accuracy of the soft information represented by the Log-Likelihood Ratios (LLRs) is an important factor which affects the error correction ability of the LDPC decoder. To improve the accuracy of LLRs, a novel LLR Adaptive Estimation scheme based on Pattern Set distribution variation (LAEPS) in 3D charge trap NAND flash memories is presented in this paper. LAEPS estimates the LLR based on not only the information proved by multi-read but also the information proved by adjacent cells in the same channel. Experimental results by silicon test illustrate that LAEPS increases the correction capability of LDPC soft decoding to 1.4x, and decreases the decoding iteration and RBER to about 0.7x and 0.8x.

## A high throughput spatially coupled low density generator matrix coding system

- **Status**: ❌
- **Reason**: SC-LDGM(생성행렬 기반) 코드 HW; LDGM은 바이너리 LDPC가 아닌 별도 부호류로 NAND ECC 표준 아님, 떼어낼 LDPC HW 기여 모호하나 LDGM 특이
- **ID**: ieee:9661891
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Ziyuan Luo, Qingyi Xie, Shanlin Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/9661891
- **Abstract**: Spatially coupled low density generator matrix (SC- LDGM) code is a novel code proposed in recent years but not implemented in hardware platform yet. We designed a hardware architecture for the encoder and decoder of SC-LDGM code, and proposed an efficient storage scheme for the message passing within decoder. We have validated our design using Xilinx evaluation board and conducted a bit error rate simulation. Results shows that our design achieves a throughput of 1.6Gbps and net coding gain of 7.3dB at BER of 10-4.

## LS and MMSE Estimation Channel Techniques for DVB-T2 System Based on MIMO-OFDM

- **Status**: ❌
- **Reason**: DVB-T2 MIMO-OFDM 채널추정(LS/MMSE); LDPC는 베이스라인 부수 언급, 이식 기법 없음
- **ID**: ieee:9655798
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: I Gede Puja Astawa, Bella Pertiwi, Arifin
- **PDF**: https://ieeexplore.ieee.org/document/9655798
- **Abstract**: The research presents the performance of the Least Estimation Channel Square (LS) and Minimum Mean Square Error (MMSE) on Orthogonal System Frequency Division Multiplexing (OFDM) with Multiple Input Multiple Output (MIMO) used in DVB-T2 technology. System performance testing analyses the value of Bit Error Rate (BER) to Signal to Noise Ratio (SNR) received by the system. In the process of data transmission, to transmit will experience noise interference and multipath fading. This can be overcome by Low-density parity-check code (LDPC). To reduce interference fading necessary, proper channel modelling so that the signal detection process at the receiver can be done. Modulation also affects system performance, which is modulation using 16-QAM modulation. This research aims to determine the response characteristic impulse channel propagation by inserting pilot symbols on subcarriers with a specific time. The system can compensate for phase distortion and amplitude of signals affected by multipath channels. The estimator will estimate the channel that contains Rayleigh Fading. MMSE performance with LDPC coding technique produces performance better than LS.

## The Transmission Test and Demonstration for 8K Ultra-high Definition TV Services Using DTMB-A

- **Status**: ❌
- **Reason**: DTMB-A 8K 방송 시연, LDPC 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:9681789
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Changyong Pan, Yunchuan Huang, Chao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9681789
- **Abstract**: Digital terrestrial television multimedia broadcasting-advanced (DTMB-A) system has been officially adopted by the International Telecommunication Union (ITU) as the latest international digital terrestrial television broadcasting (DTTB) standard in 2019. This paper introduces a live demonstration of 8K ultra-high definition (UHD) TV terrestrial broadcasting based on DTMB-A in Feb. 2021, China. The demonstration used the second-generation digital terrestrial television system C of the ITU-R BT. 1877 Recommendation, which supports a maximum payload rate of 200 Mbps by using channel bonding, code stream splitting and combing technologies. The system block diagram and the hardware devices of the trial are analysed technically in detail. The entire demonstration was conducted in Shenzhen Xinghe CoCo Park and displayed on its large outdoor UHD screen, which realized the first 8K live broadcast demonstration based on the DTMB-A in China.

## Code-Domain NOMA Solutions for Wireless Uplink

- **Status**: ❌
- **Reason**: NOMA 업링크 리뷰, LDPC/Polar는 베이스라인 비교일 뿐 새 디코더·구성 기여 없음
- **ID**: ieee:9681773
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Daria Ustinova, Anton Glebov, Serafim Novichkov
- **PDF**: https://ieeexplore.ieee.org/document/9681773
- **Abstract**: In this review paper, we consider the non-orthogonal multiple access (NOMA) schemes for wireless uplink. We assume an additive white Gaussian noise (AWGN) multiple access channel (MAC). We start with the capacity region, followed by the practical proposals for 5G cellular systems. We also consider code-division multiple-access (CDMA) schemes with a random spreading sequence as a predecessor of non-orthogonal multiple access. As a final step, we compare several practical solutions with the use of Polar and LDPC codes. We found the NOMA schemes to achieve better energy efficiency than orthogonal transmission schemes under the same modulation, thanks to a good performance of polar codes under a short block length.

## A new Taxonomy of Physical-Layer Network Coding techniques in Two Way Relay Channel model with single antenna

- **Status**: ❌
- **Reason**: 물리계층 네트워크 코딩(PNC) 분류 체계 — LDPC ECC와 무관, 떼어낼 디코더 기법 없음
- **ID**: ieee:9664726
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Mohammed Aissaoui, Chiraz Houaidia, Adrien Van Den Bossche +2
- **PDF**: https://ieeexplore.ieee.org/document/9664726
- **Abstract**: Physical-layer network coding (PNC) can effectively improve wireless networks by extracting superimposed signals and transforming collision’s dilemma into an advantage. The proposition of higher layer methods (such as Data Link and Network Layer) explicitly designed for PNC can better enhance wireless network performances. Since the field of PNC is very vast and has several applications, the researchers of the higher layers find it very difficult to propose a suitable PNC system for their research, which has led to the scarcity of research works of this type. This article proposes a new classification method designed to help researchers choose the optimal method that suits their system. This paper is a complete guide for researchers of higher layers to discover the PNC field and improve wireless network performances.

## Performance of 5G New Radio Low-Density Parity-Check Codes in Nakagami-m fading Channel

- **Status**: ❌
- **Reason**: 5G NR LDPC를 Nakagami-m 페이딩에서 표준 Offset Min-sum으로 성능 평가만 — 새 기여 없음
- **ID**: ieee:9653235
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Vladimir Vasi&#x0107;
- **PDF**: https://ieeexplore.ieee.org/document/9653235
- **Abstract**: Various scenarios in which the fifth generation of communications systems will be used lead to high demands of the standard that are successfully fulfilled by Low-Density Parity-Check (LDPC) codes, which are used for coding. In this paper, analysis of the performance of Offset Min-sum algorithm as the decoding method is made. Comparison of hard and soft decision decoding is presented, while the influence of different effects on the radio channel is analyzed by Nakagami-m fading.

## Applicability of single- and two-hidden-layer neural networks in decoding linear block codes

- **Status**: ✅
- **Reason**: ANN으로 LDPC error-floor 낮추는 디코딩 스킴 — 이식 가능한 신경망 디코더(C/E)
- **ID**: ieee:9653357
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Srdan Brkic, Predrag Ivanis, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/9653357
- **Abstract**: In this paper, we analyze applicability of single- and two-hidden-layer feed-forward artificial neural networks, SLFNs and TLFNs, respectively, in decoding linear block codes. Based on the provable capability of SLFNs and TLFNs to approximate discrete functions, we discuss sizes of the network capable to perform maximum likelihood decoding. Furthermore, we propose a decoding scheme, which use artificial neural networks (ANNs) to lower the error-floors of low-density parity-check (LDPC) codes. By learning a small number of error patterns, uncorrectable with typical decoders of LDPC codes, ANN can lower the error-floor by an order of magnitude, with only marginal average complexity incense.

## Probability of Error Minimization Techniques in Downlink Massive MIMO Systems

- **Status**: ❌
- **Reason**: massive MIMO 성능 분석, LDPC는 비교 베이스라인만 — 떼어낼 기법 없음
- **ID**: ieee:9671269
- **Type**: conference
- **Published**: 22-24 Nov.
- **Authors**: Shenko Chura Aredo, Yalemzewd Negash, Yihenew Wondie +3
- **PDF**: https://ieeexplore.ieee.org/document/9671269
- **Abstract**: The primarily goal of future wireless communication systems is to device connections with optimal throughput with minimized latency and enhanced reliability at minimum cost. One of the most important technologies for attaining this goal is massive MIMO (mMIMO). Installing a number of antennas on a single Base Station together with channel coding which is achieved by redundant bits provides reliable communication compared to the classical MIMO in which only limited number of antennas are employed. This paper analyzes the performance of coded and uncoded channel with the effect of M. Furthermore, polar and Low-Density Parity Check Code (LDPC) coding schemes are evaluated and compared with the uncoded channel condition at different number of BS antennas. We have also assessed the performance of massive MIMO at perfect and imperfect channel conditions with different constellation orders. The simulation results show that channel coded data in a perfect channel outperforms the uncoded one and as the number of antennas grows, the bit error rate (BER) is reduced.

## LDPC Code with Fractal Decoder Device for 100 Gbps PAM-M Optical Interconnect

- **Status**: ❌
- **Reason**: 광통신 인터커넥트, DVB-S2 표준 LDPC 단순 재사용 — 새 디코더/구성 없음
- **ID**: ieee:9695128
- **Type**: conference
- **Published**: 21-25 Nov.
- **Authors**: Svitlana Matsenko, Sandis Spolitis, Oleksiy Borysenko +3
- **PDF**: https://ieeexplore.ieee.org/document/9695128
- **Abstract**: Modern telecommunication systems must meet the requirements for high-speed performance, low latency, reliable transfer, processing, and information storage. In line with this, the design of the optical communication systems, e.g., data center interconnects (DCI), requires high reliability of data transmission, low latency, and low overhead. It is well known that powerful forward error correction (FEC) codes with artificial redundantly being used in optical networks have several disadvantages, e.g., high-power consumption and high delays in decoder implementation. In this paper, we use an indivisible error detection code to solve these challenges, which we realized in a field-programmable gate array (FPGA) with FEC code based on the low-density parity-check (LDPC) code. Encoding and decoding methods based on the Indivisible codes are relatively less complex and capable of executing end-to-end (E2E) data control. We integrated concatenated codes into the 100 Gbps multilevel pulse amplitude (PAM-M) with Gray code mapping direct detection wavelength division multiplexed (WDM) with standard single-mode fiber (SSMF) and erbium-doped fiber amplifier (EDFA). EDFA uses for signal amplification and to investigate the code performance in the presence of ASE noise. In current conditions, strong candidates for increasing traffic are PAM-M modulation formats (e.g., PAM-4 and PAM-8) since it possesses cost-effectiveness, simplicity, spectral, and energy efficiency. We have investigated the multichannel WDM system anchored to 193.1 THz (optical C-band) central frequency, the per-channel bitrate of 100 Gbps, channel spacing of 100 GHz and EDFA with a noise Figure of 3 dB. The LDPC FEC codes are simulated with code rates $R_{c} \in\{2 / 5,3 / 4,3 / 5,4 / 5\}$ from the digital video broadcasting by satellite – second-generation (DVB-S2) standard.

## A Short Note on the Girth of Tanner (5,13)-Regular QC-LDPC Codes

- **Status**: ❌
- **Reason**: Tanner (5,13)-regular QC-LDPC girth 분포 분석 — 특정 부호족의 사이클 존재 조건 이론 분석에 그침, NAND에 새로 이식할 디코더/HW/구성 기여 없음 (교과서 수준 girth 분석)
- **ID**: ieee:9701750
- **Type**: conference
- **Published**: 19-22 Nov.
- **Authors**: Hengzhou Xu, Hai Zhu, Xiaoxiao Miao +3
- **PDF**: https://ieeexplore.ieee.org/document/9701750
- **Abstract**: This paper studies the girth of Tanner (5,13)-regular QC-LDPC codes. We present the conditions for the existence of cycles of lengths less than 12 in Tanner (5,13)-regular QC-LDPC codes of length ${13p}$ where ${p}$ is a prime of the form ${65i+1}$, and transfer these conditions into the equations in a 65th root of unity of the prime field ${\mathbb{F}_p}$. By checking the existence of solutions for these equations over ${\mathbb{F}_p}$, we derive the girth distribution of Tanner (5,13)-regualr QC-LDPC codes.

## Interference State Estimation-Based LDPC Decoding Scheme Design for Slow FH System

- **Status**: ❌
- **Reason**: 주파수도약(FH) 시스템 간섭상태 추정 기반 LDPC 계층 디코딩 — 무선 FH 응용 특이적 사전확률 갱신, NAND에 떼어낼 일반 디코더 기법 없음
- **ID**: ieee:9639280
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Renzhi Wang, Kegang Pan, Ruixiang Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9639280
- **Abstract**: Aiming at the problem of unsatisfactory performance of the low-density parity-check (LDPC) belief propagation decoding algorithm in the LDPC coded frequency hopping (FH) system when the interference state is unknown, an LDPC layered decoding scheme based on interference state estimation is proposed. The iterative feedback estimation mechanism is used to estimate the interference state of the hop according to the posterior message of the variable node in each hop obtained in each iteration, and then update the decoding prior probability message of the next iteration to realize the LDPC decoding under the interference state estimation Process. The simulation results show that the scheme has better decoding performance and decoding convergence. When the number of hop bits is greater than or equal to 10, the decoding performance is equivalent to the known interference state, and the complexity of the scheme is not enormous.

## On the use of code-based cryptography in automotive applications

- **Status**: ❌
- **Reason**: 코드기반 암호(post-quantum crypto)용 monomial LDPC — 보안/암호 응용, 채널 ECC 디코더 기여 없음, 원칙 제외
- **ID**: ieee:9662841
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Massimo Battaglioni, Giovanni Cancellieri, Paolo Santini
- **PDF**: https://ieeexplore.ieee.org/document/9662841
- **Abstract**: Cybersecurity is a critical aspect for automotive applications. In this paper we approach this issue from a cryptographic point of view. In particular, we propose the use of a post-quantum code based cryptosystem based on a special family of low-density parity-check (LDPC) codes, called fully connected monomial LDPC codes. We also investigate some properties of these codes.

## Mutational LDPC Decoding

- **Status**: ✅
- **Reason**: 패리티검사 행렬 미세변형(mutation)으로 병렬 다중 디코더 운용해 BER 개선 — 새 LDPC 디코딩 알고리즘, NAND에 이식 가능(C)
- **ID**: ieee:9647799
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Jan Broulim, Hovik Grigorian, Alexander Ayriyan
- **PDF**: https://ieeexplore.ieee.org/document/9647799
- **Abstract**: In this paper, we propose an algorithm for improving performance of LDPC decoders, which we called the Mutational LDPC (MLDPC). This algorithm is based on different parity-check matrices produced by slight mutations. An iterative decoding process is performed using mutated matrices in several decoders running in parallel and an overall codeword estimation is then given by information from all decoders. This approach leads to a significant improvement in terms of Bit Error Rate.

## LLR Metrics for 4096-QAM Soft-Decision: Implementation in IEEE 802.11be (Wi-Fi 7)

- **Status**: ✅
- **Reason**: 4096-QAM 저복잡도 LLR metric 도출(LDPC 연성복호용) — LLR 계산/양자화 기법이 NAND 소프트복호 LLR 설계에 이식 가능(C), 애매하므로 살림
- **ID**: ieee:9647849
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/9647849
- **Abstract**: The IEEE 802.11be Task Group (TG) is currently developing the 2024 802.11be amendment (Wi-Fi 7), targeting a maximum throughput of at least 30 Gbps and at least one mode of operation with enhanced worst case latency and jitter. The 802.11be is the first wireless standard to define 4096-QAM modulation scheme. In this paper, we derive and provide a first order validation of low-complexity log-likelihood ratio (LLR) metrics suitable for soft-decoding rectangular Gray-coding 4096-QAM modulation scheme with either binary convolutional codes (BCC) or low-density parity-check (LDPC) codes.

## Single Frequency Network Broadcasting with 5GNR Numerology

- **Status**: ❌
- **Reason**: 5GNR SFN 방송 OFDM numerology/채널단축 수신기 연구; LDPC는 부수 언급 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9647735
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Majid Mosavat, Guido Montorsi
- **PDF**: https://ieeexplore.ieee.org/document/9647735
- **Abstract**: This paper investigates the possibility of using 5G New Radio (5GNR) OFDM numerology in the deployment of efficient Single Frequency Networks (SFNs) for delivering TV services to user devices. The straightforward approach in the design of the physical layer for broadcasting application is based on the adoption of OFDM signalling with very long OFDM symbol and very low sub-carrier spacing (SCS). This design choice allows to dimension the Cyclic Prefix length to eliminate ISI and ICI induced by the large delay spread with a consequent overhead reduction. The 5GNR numerology is designed for unicast transmission and Cyclic Prefix lengths are not compatible with those required for large SFN networks. In this paper we consider a general receiver based on the channel shortening principle, but in the frequency domain. The receiver consists in a bank of per tone time/frequency 2D filters, possibly followed by Maximum-Likelihood (ML) trellis processing on the shortened channel. We provide promising information theoretic bound showing that the extension of 5GNR numerology to SFN is possible with very small performance loss. Even the simplest detector architecture that does not employ trellis processing provides throughput competitive with those that can be obtained with smaller SCS. We provide end to end simulation results with practical modulation and LDPC encoder confirming that the results predicted by the bounds can be closely matched in practice.

## GFDM-based underwater transmission scheme for image signals

- **Status**: ❌
- **Reason**: GFDM 수중 이미지 전송에 표준 LDPC 부수 적용 — 떼어낼 ECC 기법 없음
- **ID**: ieee:9651031
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Chin-Feng Lin, Cheng-Fong Wu, Ching-Lung Hsieh +1
- **PDF**: https://ieeexplore.ieee.org/document/9651031
- **Abstract**: Generalized frequency division multiplexing (GFDM) transmission is an advanced communication scheme, and the main advantages of GFDM are its high spectral efficiency, high throughput, and low latency. In the paper, we design a GFDM based image transmission schemes with perfect and imperfect channel estimations for an underwater multipath fading channel model. Low-density parity-check (LDPC) channel coding is integrated into the proposed GFDM-based underwater image transmission schemes to enhance bit error rate (BER) performance. An adaptive 4 quadrature amplitude modulation (QAM) or 16-QAM, and a power assignment mechanism are integrated into the proposed scheme to achieve high transmission speed or low transmission power. The performance of the peak signal to noise ratios (PSNRs) of the original and received image signals was investigated for the proposed underwater image transmission scheme.

## LDPC-based multi-relay lossy forwarding for correlated source transmission over orthogonal Rayleigh fading channels

- **Status**: ❌
- **Reason**: 다중 릴레이 lossy forwarding에 표준 LDPC+MP 적용 — 네트워크 Tanner-graph 매핑은 통신 응용 특이적, NAND 이식 가능 기법 없음
- **ID**: ieee:9703612
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Amin Zribi, Shulin Song, Tad Matsumoto
- **PDF**: https://ieeexplore.ieee.org/document/9703612
- **Abstract**: In this paper, we design a communication and coding strategy for Lossy Forwarding (LF) systems with multiple relay nodes or helpers based on Low-Density Parity-check Codes (LDPC) with message passing decoding applied on a Tanner-graph that maps all the network. The system performance is investigated under the cases of a fixed number of helpers, and a random multiple shifted-Poisson distributed helpers for orthogonal Rayleigh fading channels. All the practical results will be also compared and validated with respect to theoretical outage probabilities.

## Design and performance analysis of Asynchronous Physical-layer Network Coding system

- **Status**: ❌
- **Reason**: Physical-layer Network Coding 동기화/심볼정렬 기법, LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:9664082
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Qinghao Chen, Taibin Fang, Meng Tang +1
- **PDF**: https://ieeexplore.ieee.org/document/9664082
- **Abstract**: For Physical-layer Network Coding (PNC), the problem of the symbol misalignment is a focus field. In this paper, we present an effective method to detect the number of symbol misalignment by utilizing Zadoff-Chu sequence (ZC sequence). Based on this method, we propose a joint communication system of Asynchronous Physical-layer Network Coding (APNC) and an Improved ZC sequence (IZC) based on BPSK modulation (IZC-APNC). In this system, we design a rule to the relay's symbol misalignment mapping, and correspondingly derive mathematical expressions of data processing. The simulation results show that our proposed system can effectively solve the problem of the symbol misalignment in APNC and improve the reliability of system transmission information.

## Multi-Round Joint Belief Propagation Decoding with Perturbation for JSCC System Based on DP-LDPC Codes

- **Status**: ❌
- **Reason**: DP-LDPC 기반 JSCC 소스-채널 결합 시스템, LDPC가 베이스라인, 떼어낼 순수 ECC 기법 없음
- **ID**: ieee:9618613
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Weiwei Lin, Zhiping Xu, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/9618613
- **Abstract**: In this paper, a multi-round joint belief propagation (BP) decoding with perturbation algorithm is proposed for joint source-channel coding (JSCC) system based on double protograph low-density parity-check (DP-LDPC) codes to improve decoding performance. In the proposed algorithm, the joint BP decoding is concatenated with cyclic redundancy check (CRC). The reliability of each variable node (VN) is evaluated in the joint BP decoding algorithm, and the CRC is used to check the error which is undetected by the joint BP. When error is detected, re-decoding process with perturbation for the unreliable VN is aroused. The simulation results indicate that the proposed method has a better bit error rate (BER) performance in comparison with the traditional joint BP algorithm.

## An Energy Efficient Hybrid FEC-ARQ Communication Scheme for Small Satellite Applications

- **Status**: ✅
- **Reason**: syndrome weight 진동 주기성 기반 신규 조기종료 정지기준(bit-flipping 디코더) — 이식 가능 디코더 기법(C)
- **ID**: ieee:9618067
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Oliver Vassallo, Victor Buttigieg, Marc A. Azzopardi
- **PDF**: https://ieeexplore.ieee.org/document/9618067
- **Abstract**: With the extensive cost reductions associated with small satellites, low Earth orbit missions are increasingly becoming popular, mostly with universities and the New-Space industry. However, a persistent limitation associated with the smallest satellites is the significant reduction in energy resources that each satellite has at its disposal. This limitation poses a challenge when using advanced communication systems, particularly those employing advanced forward error correction such as low-density parity check (LDPC) codes. To conserve the high computational energy required to decode such codes, we propose a novel early termination stopping criterion for LDPC decoders that is based on detecting the periodicity of syndrome weight oscillations. The technique is independent of the operating signal-to-noise ratio and results in reductions better than 80%, in the computational energy expended on a well-known bit-flipping decoding algorithm. Real world results are presented using an ARM-based microcontroller.

## Performance evaluation of offloading LDPC decoding to an FPGA in 5G baseband processing

- **Status**: ✅
- **Reason**: 5G LDPC 디코딩 FPGA 오프로딩 아키텍처 성능평가; 이식 가능 HW 디코더 아키텍처 관점(D)으로 애매하지만 살림
- **ID**: ieee:9739186
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Florian Kaltenberger, Hongzhi Wang, Sakthivel Velumani
- **PDF**: https://ieeexplore.ieee.org/document/9739186
- **Abstract**: Offloading of computationally expensive physical layer processing such as the forward error correction, is one of the key enablers for a fully virtualized open radio access network (RAN). In this paper we show such an offloading architecture and will demonstrate it using the OpenAirInterface 5G New Radio open source software and the Xilinx T1 telco accelerator card. We will show the feasibility and the potential savings of such an architecture.

## Hardware Implementation of Cell-Free MIMO and Dynamic TDD using the OAI 5G NR Codebase

- **Status**: ❌
- **Reason**: 셀프리 MIMO/동적 TDD 5G NR HW 구현, LDPC·이식 가능 ECC 기법 없음
- **ID**: ieee:9739188
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Himani Kamboj, Bhawesh Anand, Sanjhi Gupta +3
- **PDF**: https://ieeexplore.ieee.org/document/9739188
- **Abstract**: The cell-edge user in a traditional cellular network experiences degraded quality of service compared to a user at the centre of the cell due to path loss and interference from neighboring base stations (BSs). Cell-free multiple input and multiple output (MIMO) is a promising technology that can improve the cell-edge performance as it offers macro-diversity and consequently improved coverage and throughput. Moreover, the network capacity in a cellular network is often underutilized due to a static time division duplex (TDD) configuration coupled with asymmetric traffic demands in neighboring cells. To handle heterogeneous traffic demands, dynamic TDD is considered to be a beneficial technology, wherein different cells can independently schedule slots in the uplink (UL)/downlink (DL) directions depending on their local traffic demands. However, dynamic TDD brings new challenges because of the introduction of cross-link interferences (CLI) between users and between BSs. Combining cell-free MIMO with dynamic TDD can effectively overcome the CLI, as there exists inbuilt co-operation between the access points (APs) in the cell-free MIMO architecture. This paper presents a hardware implementation of cell-free MIMO and dynamic TDD using the OPENAIRINTERFACE (OAI) 5G new radio (NR) software stack, with the aim to experimentally understand the role of cell-free MIMO and dynamic TDD in providing better connectivity at the cell-edge and improving network throughput.

## Constant-Weight Convolutional Codes for Index Modulation

- **Status**: ❌
- **Reason**: 인덱스변조용 정중량 컨볼루션 부호 + Viterbi 디코딩; 비-LDPC 부호, 이식 기법 없음
- **ID**: ieee:9739167
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Daniel Nicolas Bailon, Juergen Freudenberger, Volker Kuehn
- **PDF**: https://ieeexplore.ieee.org/document/9739167
- **Abstract**: The encoding of antenna patterns with generalized spatial modulation as well as other index modulation techniques require w-out-of-n encoding where all binary vectors of length n have the same weight w. This constant-weight property cannot be obtained by conventional linear coding schemes. In this work, we propose a new class of constant-weight codes that result from the concatenation of convolutional codes with constant-weight block codes. These constant-weight convolutional codes are nonlinear binary trellis codes that can be decoded with the Viterbi algorithm. Some constructed constant-weight convolutional codes are optimum free distance codes. Simulation results demonstrate that the decoding performance with Viterbi decoding is close to the performance of the best-known linear codes. Similarly, simulation results for spatial modulation with a simple on-off keying show a significant coding gain with the proposed coded index modulation scheme.

## Algorithm and Hardware Co-design for Deep Learning-powered Channel Decoder: A Case Study

- **Status**: ✅
- **Reason**: 신경망 채널 디코더 알고리즘+systolic HW 공동설계, short LDPC FPGA 구현 — 이식 가능(C/D)
- **ID**: ieee:9643510
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Boyang Zhang, Yang Sui, Lingyi Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/9643510
- **Abstract**: Channel decoder is a key component module in many communication systems. Recently, neural networks-based channel decoders have been actively investigated because of the great potential of their data-driven decoding procedure. However, as the intersection among machine learning, information theory and hardware design, the efficient algorithm and hardware codesign of deep learning-powered channel decoder has not been well studied. This paper is a first step towards exploring the efficient DNN-enabled channel decoders, from a joint perspective of algorithm and hardware. We first revisit our recently proposed doubly residual neural decoder. By introducing the advanced architectural topology on the decoder design, the overall error-correcting performance can be significantly improved. Based on this algorithm, we further develop the corresponding systolic array-based hardware architecture for the DRN decoder. The corresponding FPGA implementation for our DRN decoder on short LDPC code is also developed.
