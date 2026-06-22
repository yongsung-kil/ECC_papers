# IEEE Xplore — 2021-11 (1차선별 통과)


## Neural Layered Decoding of 5G LDPC Codes

- **Status**: ✅
- **Reason**: C: 신경망 layered min-sum(NLMS/NOMS) 디코더, 정규화·오프셋 학습. 바이너리 LDPC 디코더 신기법, 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9540676
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Nemin Shah, Yash Vasavada
- **PDF**: https://ieeexplore.ieee.org/document/9540676
- **Abstract**: In this letter, we propose various low-complexity neural layered min-sum (NLMS) algorithms to improve the decoding performance of the fifth generation (5G) new radio (NR) low-density parity-check (LDPC) codes. Our proposals are based on the computationally-efficient normalized offset min-sum (NOMS) approach for the layered belief propagation (LBP). The main novelty of our proposals is a deep neural network (DNN) that implements the layered mode decoding and that additionally learns the normalization and the offset parameters of the NOMS scheme. The schemes that we propose use the DNN as well as adaptation and filtering for estimating the optimum values of these parameters. We show by simulation that our proposed decoders achieve a significant computational benefit compared to the standard (non-neural) LBP decoder without an appreciable performance penalty.

## Construction of Multi-Rate Quasi-Cyclic LDPC Codes for Satellite Communications

- **Status**: ✅
- **Reason**: E: 멀티레이트 QC-LDPC 구성 신기법(progressive row elimination/addition, nested 구조, error floor 억제). 이식 가능 바이너리 코드설계.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9521885
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Chong Zhang, Xijin Mu, Jinhong Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/9521885
- **Abstract**: To provide reliable transmissions with flexible rates for satellite communications, this paper presents a novel method of constructing multi-rate quasi-cyclic low-density parity-check (LDPC) codes. The basic idea is to generate low-rate codes from a high-rate mother code by combining shortening and extending, which ensures that the generated code family owns the same code length, in order to maintain the same frame structure. The code construction involves the design of base matrices and exponent matrices for the designed codes. A progressive row elimination and addition algorithm is proposed for designing the code base matrices from a high rate to low rates. This algorithm leads to the nested and systematic structure of the parity-check matrices, which are desirable for practical implementations of their encoders and decoders, while ensuring the optimal decoding thresholds. In addition, we construct a circulation coefficient matrix based on finite fields and select the optimal rows in this matrix to construct exponent matrices while considering of cycle structures. We demonstrate that the designed codes achieve better performance for all the code rates than the LDPC codes in DVB-S2X standards. In addition, the proposed codes do not exhibit error floors for their block error rates down to 10−5.

## Design of Bilayer and Multi-Layer LDPC Ensembles From Individual Degree Distributions

- **Status**: ✅
- **Reason**: E: 바이너리 bilayer/multi-layer LDPC 앙상블 설계 신기법(개별 차수분포 기반, 저복잡 디코딩 스케줄). 이식 가능 코드설계.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9517123
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9517123
- **Abstract**: A new approach for designing bilayer and multi-layer LDPC codes is proposed and studied in the asymptotic regime. The ensembles are defined through individual uni-variate degree distributions, one for each layer. We present a construction that: 1) enables low-complexity decoding for high-SNR channel instances, 2) provably approaches capacity for low-SNR instances, 3) scales linearly (in terms of design complexity) in the number of layers. For the setup where decoding the second layer is significantly more costly than the first layer, we propose an optimal-cost decoding schedule and study the trade-off between code rate and decoding cost.

## Across-Array Coding for Resistive Memories With Sneak-Path Interference and Lognormal Distributed Resistance Variations

- **Status**: ✅
- **Reason**: B: ReRAM 메모리 채널 LLR 생성 및 LDPC 코드워드 across-array 비트할당 신기법. 스토리지 ECC 직접.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9531624
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Panpan Li, Guanghui Song, Kui Cai +1
- **PDF**: https://ieeexplore.ieee.org/document/9531624
- **Abstract**: Resistive random-access memory (ReRAM) is a promising non-volatile memory technology for achieving high-density and high-speed data storage. However, its crossbar array structure leads to a severe problem known as the sneak path interference (SPI), which is data dependent and correlated within a memory array. Meanwhile, variations of the memory fabrication process also cause deviation of memory cell resistances from their nominal values, which typically follows the lognormal distribution. In this letter, we first propose a cascaded channel model that incorporates these two key factors that affect the reliability of ReRAM. By analyzing the channel correlation of ReRAM caused by the SPI, we develop a novel scheme to estimate the probability of each memory cell to be affected by the SPI, based on which the log-likelihood ratio (LLR) of each channel bit can be generated. Moreover, we propose a novel two-step across-array bit allocation scheme, which distributes the low-density parity-check (LDPC) codewords to multiple memory arrays so as to minimize the correlation of the channel coded bits for decoding. Simulation results show that the proposed across-array bit allocation scheme with LDPC coding can achieve significantly better error rate performance than the prior art coding schemes, with similar implementation complexity and latency.

## Optimal Quantizer Structure for Maximizing Mutual Information Under Constraints

- **Status**: ✅
- **Reason**: C/A 관련: 상호정보 최대화 최적 양자화기 설계(임계값 수 상한). NAND LLR 양자화에 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9530430
- **Type**: journal
- **Published**: Nov. 2021
- **Authors**: Thuan Nguyen, Thinh Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9530430
- **Abstract**: Consider a channel whose the input alphabet set  $\mathbb {X}=\{x_{1},x_{2}, {\dots },x_{K}\}$  contains  $K$  discrete symbols modeled as a discrete random variable  $X$  having a probability mass function  $\mathbf {p}(\mathbf {x}) = [p(x_{1}), p(x_{2}), {\dots }, p(x_{K})]$  and the received signal  $Y$  being a continuous random variable.  $Y$  is a distorted version of  $X$  caused by a channel distortion, characterized by the conditional densities  $p(y|x_{i})=\phi _{i}(y)$ ,  $i=1,2, {\dots },K$ . To recover  $X$ , a quantizer  $Q$  is used to quantize  $Y$  back to a discrete output  $\mathbb {Z} =\{z_{1}, z_{2}, {\dots }, z_{N}\}$  corresponding to a random variable  $Z$  with a probability mass function  $\mathbf {p}(\mathbf {z}) = [p(z_{1}), p(z_{2}), {\dots }, p(z_{N})]$  such that the mutual information  $I(X;Z)$  is maximized subject to an arbitrary constraint on  $\mathbf {p}(\mathbf {z})$ . Formally, we are interested in designing an optimal quantizer  $Q^{*}$  that maximizes  $\beta I(X;Z) - C(Z)$  where  $\beta $  is a positive number that controls the trade-off between maximizing  $I(X;Z)$  and minimizing an arbitrary cost function  $C(Z)$ . Let  $\mathbf {p}(\mathbf {x}|y)=[p(x_{1}|y),p(x_{2}|y), {\dots },p(x_{K}|y)]$  be the posterior distribution of  $X$  for a given value of  $y$ , we show that for any arbitrary cost function  $C(.)$ , the optimal quantizer  $Q^{*}$  separates the vectors  $\mathbf {p}(\mathbf {x}|y)$  into convex regions. Using this result, a method is proposed to determine an upper bound on the number of thresholds (decision variables on  $y$ ) which is used to speed up the algorithm for finding an optimal quantizer. Numerical results are presented to validate the findings.

## LLR Metrics for 1024-QAM Soft-Decision: Implementation in IEEE 802.11ax (Wi-Fi 6)

- **Status**: ✅
- **Reason**: 1024-QAM 연판정용 근사 LLR 메트릭 도출(log-domain SPA용) — LLR 근사/양자화 기법은 NAND LDPC 연판정에 이식 가능(A/C 경계, 애매하여 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9615831
- **Type**: conference
- **Published**: 31 Oct.-2 
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/9615831
- **Abstract**: The IEEE 802.11ax amendment (Wi-Fi 6) has defined modulation code schemes that implement uniform Gray mapping rectangular 1024-QAM constellation. In this paper, we derive approximate log-likelihood ratio (LLR) metrics for softdecoding of binary convolutional codes (BCC) using Viterbi decoding and low-density parity-check codes (LDPC) using the message-passing algorithm, implemented as the log-domain sum-product algorithm. The proposed low-complexity softdecision metrics are validated by simulating the 802.11ax physical layer that implements transmit beamforming transceivers over frequency selective channels.

## An Improved Self-Corrected Min-Sum Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: ISCMS — self-corrected min-sum의 CN 갱신 규칙 개선, 이식 가능 디코더 알고리즘 변형(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9755394
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Xingjin Li, Liguo Zhang, Jingxuan Tan +3
- **PDF**: https://ieeexplore.ieee.org/document/9755394
- **Abstract**: Low-Density Parity-Check (LDPC) code is a linear block code approaching the Shannon limit. The improvement of the decoding performance of LDPC codes is a hot research direction today. To improve the decoding performance of the self-correcting min-sum (SCMS) algorithm, an improved self-correcting min-sum (ISCMS) algorithm is proposed based on this algorithm. In the iterative decoding process of the ISCMS algorithm, the update rule of the check node (CN) is optimized to the update rule of the CN of the IOMS algorithm, which improves the accuracy of decoding from the processing of the CN. Simulation results show that the proposed ISCMS algorithm has better error performance and convergence performance than the SCMS algorithm with a small increase in computational complexity.

## Low Complexity Neural Network-Aided NMS LDPC Decoder

- **Status**: ✅
- **Reason**: NN-aided NMS 디코더 — LLR로 정규화 인자 추론하는 신경망 보조 min-sum 변형, 저복잡도 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9652964
- **Type**: conference
- **Published**: 26-28 Nov.
- **Authors**: Honghao Shi, Mingyang Zhong, Zhiyong Luo +1
- **PDF**: https://ieeexplore.ieee.org/document/9652964
- **Abstract**: For recent years, deep learning has been studied and utilized among decoders in wireless and optical communication. For low density parity check (LDPC) codes, most works use neural network (NN) to implement the belief propagation (BP) decoder and unfold its iterations into layers activated by different functions. However, the whole decoder composed by neural network performs lots of non-linear operations, which are time consuming and unfriendly to hardware implementation. In this work, a neural network-aided normalized min-sum (NN-aided NMS) decoder for LDPC code is proposed, in which the normalization factors are inferred from input log likelihood ratio (LLR) by apre-trained NN, while maintaining check and variable nodes processing the same as in min-sum (MS) decoder. In order to test the proposed decoder with irregular LDPC code, a rate-7/8 one was constructed using progressive edge growth (PEG) algorithm, showing better error correction capability than the standard of consultative committee for space data systems (CCSDS) LDPC (8176,7154) code by 0.08 dB with the same rate. Simulation results show that, NN-aided NMS decoder outperforms MS decoder by 0.3 dB, and its performance approaches BP decoder with a gap of 0.02 dB, which is 50% closer than the best NMS decoder using 0.7 as the normalization factor. The proposed decoder has good performance for both regular and irregular LDPC codes, and needs much less computation complexity than BP decoder. It introduces more linear computation than NMS decoder but achieves better bit error rate (BER) performance, thus becoming a good complement between BP and NMS decoder when trading off among complexity, error correction performance and hardware implementation for wireless and satellite communication.

## A Method of Soft-Sensing Log-Likelihood Ratios Based on Broad Learning System for NAND Flash Memories

- **Status**: ✅
- **Reason**: A — NAND 플래시 직접, BLS 기반 LLR 소프트센싱으로 multi-level read 대체하는 새 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9673965
- **Type**: conference
- **Published**: 25-28 Nov.
- **Authors**: Kainan Ma, Tao Li, Yibo Yin +2
- **PDF**: https://ieeexplore.ieee.org/document/9673965
- **Abstract**: To accelerate the convergence of the soft-decision decoder and improve the reading performance of the NAND flash memory, a multi-level reading method is usually adopted to sense precise log-likelihood ratios (LLR). However, multi-level readings interfere with the threshold voltage in the cells, increasing the probability of bit errors and accelerating cells wear. To solve this problem, this paper proposed an LLR soft-sensing method based on a broad learning system (BLS) to replace multi-level reading, which improves accuracy of sensing from 97.1% to 97.3% by using the raw bit error rate (RBER) as one of the inputs. The output classification probabilities of the network model are used to calculate the LLR. Compared with the multilayer perceptron model, the adoption of BLS hugely decreases the computation amount of network training from 113 epochs to 5, making on-chip retraining feasible. The proposed BLS-based LLR soft-sensing method will be of great application potential in the intelligent error control of non-volatile memories.

## LAEPS: LDPC LLR Adaptive Estimation Based on Pattern Set Distribution Variation in 3D Charge Trap NAND Flash Memories

- **Status**: ✅
- **Reason**: 3D NAND LDPC 소프트디코딩용 LLR 적응 추정(LAEPS) — NAND 직접+LLR 기법(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9661917
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Qianhui Li, Yiyang Jiang, Qi Wang +5
- **PDF**: https://ieeexplore.ieee.org/document/9661917
- **Abstract**: Low-density parity-check (LDPC) code with the soft decoding algorithm has been widely used in 3D NAND flash memories to improve the system reliability, because of its strong error correction ability. However, the accuracy of the soft information represented by the Log-Likelihood Ratios (LLRs) is an important factor which affects the error correction ability of the LDPC decoder. To improve the accuracy of LLRs, a novel LLR Adaptive Estimation scheme based on Pattern Set distribution variation (LAEPS) in 3D charge trap NAND flash memories is presented in this paper. LAEPS estimates the LLR based on not only the information proved by multi-read but also the information proved by adjacent cells in the same channel. Experimental results by silicon test illustrate that LAEPS increases the correction capability of LDPC soft decoding to 1.4x, and decreases the decoding iteration and RBER to about 0.7x and 0.8x.

## Applicability of single- and two-hidden-layer neural networks in decoding linear block codes

- **Status**: ✅
- **Reason**: ANN으로 LDPC error-floor 낮추는 디코딩 스킴 — 이식 가능한 신경망 디코더(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9653357
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Srdan Brkic, Predrag Ivanis, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/9653357
- **Abstract**: In this paper, we analyze applicability of single- and two-hidden-layer feed-forward artificial neural networks, SLFNs and TLFNs, respectively, in decoding linear block codes. Based on the provable capability of SLFNs and TLFNs to approximate discrete functions, we discuss sizes of the network capable to perform maximum likelihood decoding. Furthermore, we propose a decoding scheme, which use artificial neural networks (ANNs) to lower the error-floors of low-density parity-check (LDPC) codes. By learning a small number of error patterns, uncorrectable with typical decoders of LDPC codes, ANN can lower the error-floor by an order of magnitude, with only marginal average complexity incense.

## Mutational LDPC Decoding

- **Status**: ✅
- **Reason**: 패리티검사 행렬 미세변형(mutation)으로 병렬 다중 디코더 운용해 BER 개선 — 새 LDPC 디코딩 알고리즘, NAND에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9647799
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Jan Broulim, Hovik Grigorian, Alexander Ayriyan
- **PDF**: https://ieeexplore.ieee.org/document/9647799
- **Abstract**: In this paper, we propose an algorithm for improving performance of LDPC decoders, which we called the Mutational LDPC (MLDPC). This algorithm is based on different parity-check matrices produced by slight mutations. An iterative decoding process is performed using mutated matrices in several decoders running in parallel and an overall codeword estimation is then given by information from all decoders. This approach leads to a significant improvement in terms of Bit Error Rate.

## LLR Metrics for 4096-QAM Soft-Decision: Implementation in IEEE 802.11be (Wi-Fi 7)

- **Status**: ✅
- **Reason**: 4096-QAM 저복잡도 LLR metric 도출(LDPC 연성복호용) — LLR 계산/양자화 기법이 NAND 소프트복호 LLR 설계에 이식 가능(C), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9647849
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Roger Pierre Fabris Hoefel
- **PDF**: https://ieeexplore.ieee.org/document/9647849
- **Abstract**: The IEEE 802.11be Task Group (TG) is currently developing the 2024 802.11be amendment (Wi-Fi 7), targeting a maximum throughput of at least 30 Gbps and at least one mode of operation with enhanced worst case latency and jitter. The 802.11be is the first wireless standard to define 4096-QAM modulation scheme. In this paper, we derive and provide a first order validation of low-complexity log-likelihood ratio (LLR) metrics suitable for soft-decoding rectangular Gray-coding 4096-QAM modulation scheme with either binary convolutional codes (BCC) or low-density parity-check (LDPC) codes.

## An Energy Efficient Hybrid FEC-ARQ Communication Scheme for Small Satellite Applications

- **Status**: ✅
- **Reason**: syndrome weight 진동 주기성 기반 신규 조기종료 정지기준(bit-flipping 디코더) — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9618067
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Oliver Vassallo, Victor Buttigieg, Marc A. Azzopardi
- **PDF**: https://ieeexplore.ieee.org/document/9618067
- **Abstract**: With the extensive cost reductions associated with small satellites, low Earth orbit missions are increasingly becoming popular, mostly with universities and the New-Space industry. However, a persistent limitation associated with the smallest satellites is the significant reduction in energy resources that each satellite has at its disposal. This limitation poses a challenge when using advanced communication systems, particularly those employing advanced forward error correction such as low-density parity check (LDPC) codes. To conserve the high computational energy required to decode such codes, we propose a novel early termination stopping criterion for LDPC decoders that is based on detecting the periodicity of syndrome weight oscillations. The technique is independent of the operating signal-to-noise ratio and results in reductions better than 80%, in the computational energy expended on a well-known bit-flipping decoding algorithm. Real world results are presented using an ARM-based microcontroller.

## Performance evaluation of offloading LDPC decoding to an FPGA in 5G baseband processing

- **Status**: ✅
- **Reason**: 5G LDPC 디코딩 FPGA 오프로딩 아키텍처 성능평가; 이식 가능 HW 디코더 아키텍처 관점(D)으로 애매하지만 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9739186
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Florian Kaltenberger, Hongzhi Wang, Sakthivel Velumani
- **PDF**: https://ieeexplore.ieee.org/document/9739186
- **Abstract**: Offloading of computationally expensive physical layer processing such as the forward error correction, is one of the key enablers for a fully virtualized open radio access network (RAN). In this paper we show such an offloading architecture and will demonstrate it using the OpenAirInterface 5G New Radio open source software and the Xilinx T1 telco accelerator card. We will show the feasibility and the potential savings of such an architecture.

## Algorithm and Hardware Co-design for Deep Learning-powered Channel Decoder: A Case Study

- **Status**: ✅
- **Reason**: 신경망 채널 디코더 알고리즘+systolic HW 공동설계, short LDPC FPGA 구현 — 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9643510
- **Type**: conference
- **Published**: 1-4 Nov. 2
- **Authors**: Boyang Zhang, Yang Sui, Lingyi Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/9643510
- **Abstract**: Channel decoder is a key component module in many communication systems. Recently, neural networks-based channel decoders have been actively investigated because of the great potential of their data-driven decoding procedure. However, as the intersection among machine learning, information theory and hardware design, the efficient algorithm and hardware codesign of deep learning-powered channel decoder has not been well studied. This paper is a first step towards exploring the efficient DNN-enabled channel decoders, from a joint perspective of algorithm and hardware. We first revisit our recently proposed doubly residual neural decoder. By introducing the advanced architectural topology on the decoder design, the overall error-correcting performance can be significantly improved. Based on this algorithm, we further develop the corresponding systolic array-based hardware architecture for the DRN decoder. The corresponding FPGA implementation for our DRN decoder on short LDPC code is also developed.
