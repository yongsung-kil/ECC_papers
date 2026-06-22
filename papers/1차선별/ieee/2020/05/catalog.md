# IEEE Xplore — 2020-05 (1차선별 통과)


## Layered Construction of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 신규 layered 구성으로 6-cycle·trapping set 제거, girth-10 설계 — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8999573
- **Type**: journal
- **Published**: May 2020
- **Authors**: Xiongfei Tao, Yue Xin, Bifang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8999573
- **Abstract**: A layered construction of LDPC codes on 3-dimensional rectangular lattices is explored in this letter. By analyzing the governing conditions of in-layer polygons and inter-layer polygons, and elaborately selecting the slopes of in-layer and inter-layer lines, we remove all the 6-cycles as well as inter-layer 8-cycles which results in a class of LDPC codes without small trapping sets. We further remove the in-layer 8-cycles to design a class of LDPC codes with girth 10.

## Extended Barrel-Shifter for Versatile QC-LDPC Decoders

- **Status**: ✅
- **Reason**: QC-LDPC 디코더용 확장 배럴시프터(permutation network) HW 신규 제안 — D 이식 가능 HW 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8950135
- **Type**: journal
- **Published**: May 2020
- **Authors**: Emmanuel Boutillon, Hassan Harb
- **PDF**: https://ieeexplore.ieee.org/document/8950135
- **Abstract**: In this letter, we present a Barrel-Shifter of size n extended by an additional layer that can handle any circular permutation on a vector of size m, m ≤ n, thanks to a specific initial positioning of the data. The construction of the so-called Extended Barrel-Shifter is motivated by the hardware decoder constraint related to the Low-Density Parity-Check (LDPC) code recently adopted for the 5G mobile standard. The proposed algorithm requires 42% less multiplexers than the best state-of-the-art solution for n = 384 of the 5G LDPC standard. This proposal is also able to process several inputs in parallel without extra hardware cost.

## Efficient Architectures for Multigigabit CCSDS LDPC Encoders

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 신규 HW 아키텍처(FPGA), QC 병렬성 활용 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9019604
- **Type**: journal
- **Published**: May 2020
- **Authors**: Dimitris Theodoropoulos, Nektarios Kranitis, Antonis Tsigkanos +1
- **PDF**: https://ieeexplore.ieee.org/document/9019604
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes have been adopted by the Consultative Committee for Space Data Systems (CCSDS) as the recommended standard for onboard channel coding in Near-Earth and Deep-Space communications. Encoder architectures proposed so far are not efficient for high-throughput hardware implementations targeting the specific CCSDS codes. In this article, we introduce a novel architecture for the multiplication of a dense quasi-cyclic (QC) matrix with a bit vector, which is the fundamental operation of QC-LDPC encoding. The architecture leverages the inherent parallelism of the QC structure by concurrently processing multiple bits, according to an optimized scheduling. Based on this architecture, we propose efficient encoders for CCSDS codes, according to all the applicable low-density parity-check (LDPC) code encoding methods. Moreover, in the special case of the code for Near-Earth communications, we also introduce a preprocessing algorithm to efficiently handle the challenges arising from the generator's matrix circulant size (511 bits). The proposed architectures have been implemented in various field-programmable gate array (FPGA) technologies and validated in Zynq UltraScale+ multiprocessor system-on-chip (MPSoC), achieving a significant speedup compared with previous approaches, while at the same time keeping resource utilization low.

## Error Floor Estimation of LDPC Decoders — A Code Independent Approach to Measuring the Harmfulness of Trapping Sets

- **Status**: ✅
- **Reason**: LDPC trapping set/error floor 추정 신기법, 양자화 min-sum 등 반복 디코더 대상 — error floor 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9005250
- **Type**: journal
- **Published**: May 2020
- **Authors**: Ali Farsiabi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9005250
- **Abstract**: The linear state-space model is a well-known code-independent method to estimate the contribution of a trapping set (TS) structure to the error floor of low-density parity-check (LDPC) codes. In this paper, we provide an in-depth analysis of this method by incorporating a more accurate model for the incoming messages to the TS structure that takes into account the randomness and the correlation among such messages. Based on this analysis, we demonstrate that both randomness and correlation result in the over-estimation of the failure probability of the TS. We then propose an alternate code-independent technique for the error floor estimation of iterative LDPC decoders that can accurately estimate the contribution of different TS structures in the error floor. Compared to the linear state-space model, the proposed method is not only more accurate, but also more general, in that, it is applicable to any saturating iterative message-passing decoder, symmetrically quantized or unquantized, over any memoryless binary-input output-symmetric channel. The proposed technique can be viewed as the local application of importance sampling (IS) to the message-passing algorithm over the subgraph induced by the TS in the code's Tanner graph. In the message-passing process, to account for the effect of the rest of the Tanner graph, density evolution along with a simple correlation model is used to generate the messages coming into the TS from the rest of the Tanner graph. Extensive simulations demonstrate that the proposed technique can accurately estimate the error floor of LDPC codes over both additive white Gaussian noise (AWGN) channel and binary symmetric channel (BSC), for a variety of iterative decoding algorithms and quantization schemes.

## Deep Learning-Aided Dynamic Read Thresholds Design for Multi-Level-Cell Flash Memories

- **Status**: ✅
- **Reason**: NAND MLC 플래시 동적 read threshold, soft LLR 매핑, LDPC-coded 채널 DE 최적화 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9000906
- **Type**: journal
- **Published**: May 2020
- **Authors**: Zhen Mei, Kui Cai, Xuan He
- **PDF**: https://ieeexplore.ieee.org/document/9000906
- **Abstract**: The practical NAND flash memory suffers from various non-stationary noises that are difficult to be predicted. For example, the data retention noise induced channel offset is unknown during the readback process, and hence severely affects the reliability of data recovery from the memory cell. In this paper, we first propose a novel recurrent neural network (RNN)-based detector to effectively detect the data stored in the multi-level-cell (MLC) flash memory without the prior knowledge of the channel. However, compared with the conventional threshold detector, the proposed RNN detector introduces much longer read latency and more power consumption. To tackle this problem, we further propose an RNN-aided (RNNA) dynamic threshold detector, whose detection thresholds can be derived based on the outputs of the RNN detector. We thus only need to activate the RNN detector periodically when the system is idle. Moreover, to enable soft-decision decoding of error-correction codes, we first show how to obtain more read thresholds based on the hard-decision read thresholds derived from the RNN detector. We then propose integer-based reliability mappings based on the designed read thresholds, which can generate the soft information of the channel. Finally, we propose to apply density evolution (DE) combined with the differential evolution algorithm to optimize the read thresholds for low-density parity-check (LDPC) coded flash memory channels. Computer simulation results demonstrate the effectiveness of our proposed RNNA dynamic read thresholds design, for both the uncoded and LDPC-coded flash memory channels, without any prior knowledge of the channel.

## Fine-Grained Bit-Flipping Decoding for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC 신규 hard-decision bit-flipping(FBF) 디코더 + HW 아키텍처 — 이식 가능 디코더·HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9037092
- **Type**: journal
- **Published**: May 2020
- **Authors**: Yuxing Chen, Hangxuan Cui, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9037092
- **Abstract**: This brief presents a novel class of hard-decision algorithms for decoding low density parity check codes. The new algorithms, named fine-grained bit-flipping (FBF) algorithms, employ a detailed classification of each bit, by introducing the XOR value of its estimated and received value as a subdividing criterion. The fine-grained classification allows the algorithms to strengthen the information utilization during each iteration. Simulation results show that the FBF algorithms can achieve up to 5 times better decoding performance than the state-of-the-art bit-flipping algorithms over the binary symmetric channel. Additionally, a well-optimized hardware architecture is developed for implementing FBF algorithms. Compared to other decoders, implementation results demonstrate that the FBF decoders achieve higher throughput and area efficiency.

## Multi-Dimensional Spatially-Coupled Code Design: Enhancing the Cycle Properties

- **Status**: ✅
- **Reason**: 다차원 SC-LDPC 코드설계(cycle property 개선) + 저지연 디코딩, 3D Flash 명시 — E 코드설계, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8984289
- **Type**: journal
- **Published**: May 2020
- **Authors**: Homa Esfahanizadeh, Lev Tauz, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/8984289
- **Abstract**: A circulant-permutation-based spatially-coupled (SC) code is constructed by partitioning the circulant permutation matrices (CPMs) in the parity-check matrix of a block code into several components and piecing copies of these components in a diagonal structure. By connecting several SC codes, multi-dimensional SC (MD-SC) codes are constructed. In this paper, we present a systematic framework for constructing MD-SC codes with notably better cycle properties than their one-dimensional counterparts. In our framework, the multi-dimensional coupling is performed via an informed relocation of problematic CPMs. This work is general in the terms of the number of constituent SC codes that are connected together, the number of neighboring SC codes that each constituent SC code is connected to, and the length of the cycles whose populations we aim to reduce. Finally, we present a decoding algorithm that utilizes the structures of the MD-SC code to achieve lower decoding latency. Compared to the conventional SC codes, our MD-SC codes have a notably lower population of small cycles, and a dramatic BER improvement. The results of this work can be particularly beneficial in data storage systems, e.g., 2D magnetic recording and 3D Flash systems, as high-performance MD-SC codes are robust against various channel impairments and non-uniformity.

## ADMM-Based Decoder for Binary Linear Codes Aided by Deep Learning

- **Status**: ✅
- **Reason**: ADMM-penalized 디코더를 deep unfolding한 신경망 디코더, LDPC에 적용·성능 개선 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9000536
- **Type**: journal
- **Published**: May 2020
- **Authors**: Yi Wei, Ming-Min Zhao, Min-Jian Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/9000536
- **Abstract**: Inspired by the recent advances in deep learning (DL), this work presents a deep neural network aided decoding algorithm for binary linear codes. Based on the concept of deep unfolding, we design a decoding network by unfolding the alternating direction method of multipliers (ADMM)-penalized decoder. In addition, we propose two improved versions of the proposed network. The first one transforms the penalty parameter into a set of iteration-dependent ones, and the second one adopts a specially designed penalty function, which is based on a piecewise linear function with adjustable slopes. Numerical results show that the resulting DL-aided decoders outperform the original ADMM-penalized decoder for various low density parity check (LDPC) codes with similar computational complexity.

## Bipartite Belief Propagation Polar Decoding With Bit-Flipping

- **Status**: ✅
- **Reason**: polar BP를 LDPC형 희소 이분그래프로 변환 후 비트플립 L-BPF 디코더 — BP 디코더 개선 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9053183
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Zihao Gong, Yifei Shen, Houren Ji +4
- **PDF**: https://ieeexplore.ieee.org/document/9053183
- **Abstract**: For the scenarios with high throughput requirements, the belief propagation (BP) decoding is one of the most promising decoding strategies for polar codes. By pruning the redundant variable nodes (VNs) and check nodes (CNs) in the original factor graph, the graph is condensed to a sparse bipartite graph which is similar to the graph for low-density parity-check (LDPC) codes. In this paper, we introduce the bit-flipping scheme into the LDPC-like BP (L-BP) decoding and propose two methods to identify the error-prone VNs. By additional decoding attempts, the L-BP flip (L-BPF) decoding improves the error-rate performance with a similar average complexity for high Eb=N0 values. The simulation results show that the L-BPF decoding achieves 0:25 dB gain compared with the L-BP decoding.

## Decoding 5G-NR Communications VIA Deep Learning

- **Status**: ✅
- **Reason**: 5G-NR LDPC 디맵핑/디코딩에 오토인코더+DNN 적용 — 신경망 LDPC 디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9054192
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Pol Henarejos, Miguel Ángel Vázquez
- **PDF**: https://ieeexplore.ieee.org/document/9054192
- **Abstract**: Upcoming modern communications are based on 5G specifications and aim at providing solutions for novel vertical industries. One of the major changes of the physical layer is the use of Low-Density Parity-Check (LDPC) code for channel coding. Although LDPC codes introduce additional computational complexity compared with the previous generation, where Turbocodes where used, LDPC codes provide a reasonable trade-off in terms of complexity-Bit Error Rate (BER). In parallel to this, Deep Learning algorithms are experiencing a new revolution, specially to image and video processing. In this context, there are some approaches that can be exploited in radio communications. In this paper we propose to use Autoencoding Neural Networks (ANN) jointly with a Deep Neural Network (DNN) to construct Autoencoding Deep Neural Networks (ADNN) for demapping and decoding. The results will unveil that, for a particular BER target, 3 dB less of Signal to Noise Ratio (SNR) is required, in Additive White Gaussian Noise (AWGN) channels.

## Back-to-Back Butterfly Network, an Adaptive Permutation Network for New Communication Standards

- **Status**: ✅
- **Reason**: 적응형 permutation network(B2BN) 충돌없는 경로선택 HW — LDPC 디코더 셔플/permutation 네트워크로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9053364
- **Type**: conference
- **Published**: 4-8 May 20
- **Authors**: Hassan Harb, Cyrille Chavet
- **PDF**: https://ieeexplore.ieee.org/document/9053364
- **Abstract**: In this paper, we introduce an adaptive Back-to-Back Butterfly Network (B2BN) dedicated to next communication standards. It can perform any kind of permutation, and its architecture is based on a concatenation of basic networks. However for a set of permutations, the selection of non-conflicting paths is still a complex task. Hence, in our paper we rely on the properties of the proposed architecture, to introduce a formal model that efficiently solve such conflicts. From the collection of all possible paths in the targeted B2BN, the proposed method select the conflict-free paths to transfer data from the input to their permuted output (w.r.t., a ad hoc constraints model). Once the appropriate paths are selected, the control signals for B2BN are generated. This model has been experimented with 5G communication, showing how to process several frames in parallel with different permutation constraints.

## A LDPC Decoder Based on Efficient Memory Design in DVB-S2 Standard

- **Status**: ✅
- **Reason**: D: DVB-S2 LDPC 디코더 FPGA HW 아키텍처 — VN 메모리 구조/CN 업데이트 순서 조정으로 throughput 향상, NAND 디코더 HW에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9123291
- **Type**: conference
- **Published**: 29-31 May 
- **Authors**: Kaijie Dong, Jinshu Chen
- **PDF**: https://ieeexplore.ieee.org/document/9123291
- **Abstract**: In this paper, a LDPC decoder based on efficient variable node memory structure design is proposed to reduce the time cost of accessing data in the pipeline. Firstly, we prepare the table corresponding to the variable node memory structure. So we can access the data only by reading the table. On this basis, the check node update order is adjusted to avoid performance loss caused by the conflict between adjacent ones. This method is applicable to all code rates, and does not bring loss of decoding performance. It greatly increase the throughput of the decoder, with an affordable resource consumption. Based on the proposed architectures, a high speed LDPC decoder is implemented on Stratix V 5SGXEA7N2F45C2N FPGA, achieves a throughput of 2.05 Gbps for DVB-S2 code rate 2/3 and a throughput of 2.73 Gbps for rate 4/5.

## High Rate Communication over One-Bit Quantized Channels via Deep Learning and LDPC Codes

- **Status**: ✅
- **Reason**: LDPC+오토인코더로 1비트 양자화 비선형채널 ECC 설계, LLR Gaussian화 — 양자화 채널 디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9154208
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Eren Balevi, Jeffrey G. Andrews
- **PDF**: https://ieeexplore.ieee.org/document/9154208
- **Abstract**: This paper proposes a method for designing error correction codes by combining a known coding scheme with an autoencoder. Specifically, we integrate an LDPC code with a trained autoencoder to develop an error correction code for intractable nonlinear channels. The LDPC encoder shrinks the input space of the autoencoder, which enables the autoencoder to learn more easily. The proposed error correction code shows promising results for one-bit quantization, a challenging case of a nonlinear channel. Specifically, our design gives a waterfall slope bit error rate even with high order modulation formats such as 16-QAM and 64-QAM despite one-bit quantization. This gain is theoretically grounded by proving that the trained autoencoder provides approximately Gaussian distributed data to the LDPC decoder even though the received signal has non-Gaussian statistics due to the one-bit quantization.

## Multi Variable-layer Neural Networks for Decoding Linear Codes

- **Status**: ✅
- **Reason**: BP를 신경망으로 본 멀티 변수노드층 신경망 디코더, all-zero 학습 충분 — 이식 가능 신경망 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9163473
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Samira Malek, Saber Salehkaleybar, Arash Amini
- **PDF**: https://ieeexplore.ieee.org/document/9163473
- **Abstract**: The belief propagation algorithm is a state of the art decoding technique for a variety of linear codes such as LDPC codes. The iterative structure of this algorithm is reminiscent of a neural network with multiple layers. Indeed, this similarity has been recently exploited to improve the decoding performance by tuning the weights of the equivalent neural network. In this paper, we introduce a new network architecture by increasing the number of variable-node layers, while keeping the check-node layers unchanged. The changes are applied in a manner that the decoding performance of the network becomes independent of the transmitted codeword; hence, a training stage with only the all-zero codeword shall be sufficient. Simulation results on a number of well-studied linear codes, besides an improvement in the decoding performance, indicate that the new architecture is also simpler than some of the existing decoding networks.

## Algorithm for Removal of Short Cycles in Tanner Graphs with Minimum-Hamming-Distance Check

- **Status**: ✅
- **Reason**: 바이너리 LDPC Tanner 그래프 short cycle 제거 신규 알고리즘(PEG 개선), E 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9130338
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Viktor Ďurček, Michal Kuba, Milan Dado
- **PDF**: https://ieeexplore.ieee.org/document/9130338
- **Abstract**: Two algorithms for removal of short cycles in Tanner graphs of parity-check matrices of binary LDPC codes constructed by Progressive Edge-Growth algorithm are described. These loop-removing algorithms can be used to improve error-correcting performance of existing LDPC codes and achieved results are provided.

## A Modified Rejection-Based Architecture to Find the First Two Minima in Min-Sum-Based LDPC Decoders

- **Status**: ✅
- **Reason**: min-sum LDPC 디코더의 first-two-minima 탐색 HW 아키텍처 개선(rejection-based, FPGA 구현) — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9120630
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Alireza Hasani, Lukasz Lopacinski, Steffen Büchner +2
- **PDF**: https://ieeexplore.ieee.org/document/9120630
- **Abstract**: One of the essential elements of min-sum low-density parity-check (LDPC) decoders is to find the first two minima between the binary messages arriving in the check nodes along with the index of the minimum which are altogether used to compute the messages for sending back to the neighboring variable nodes. The main techniques for this task are tree-based and bit-serial architectures. The latest tree-based architecture, known as rejection-based scheme finds the first two minima and the binary index of the minimum with higher speed than the previous tree-based methods. However, in min-sum LDPC decoders, having one-hot sequence of the minimum of the messages is preferred as it has implementation benefits. In this paper, we modify the existing rejection-based technique to yield the one-hot sequence instead of the binary representation of the minimum index. The proposed modification doesn’t cause any latency in the operation of the module. We also provide the results of the implementation of the modified rejection-based technique and the bit-serial architecture, conducted on a Xilinx Virtex-7 FPGA. The two major architectures are compared in terms of latency, maximum clock frequency, area and power.

## Stopping Criterion for LDPC Decoder based on PEXIT Chart Analysis

- **Status**: ✅
- **Reason**: LDPC 디코더 조기정지(early stopping) 기준 신규 제안(PEXIT 기반 임계값) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9120774
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: Taehyun Kim, JooSung Park, Jun Heo
- **PDF**: https://ieeexplore.ieee.org/document/9120774
- **Abstract**: In this paper, an early stopping scheme is proposed for low-density parity-check (LDPC) decoders. The proposed scheme predicts that the LDPC decoder will not be able to correct errors and then stops the iterative decoding process before reaching the maximum number of iterations. When the number of parity checks unsatisfied at both the $l-$th and the $(l-T)-$th decoding iterations is larger than a threshold, the decoder with the proposed scheme predicts that the decoding of the codeword is failed at the last iteration. Protograph-based extrinsic information transfer (PEXIT) chart analysis is used to determine the threshold. Simulation results show that the LDPC decoder can correct errors with the lower average number of iterations by using both the conventional syndrome test and proposed scheme.

## LDPC-Staircase Codes for Soft Decision Decoding

- **Status**: ✅
- **Reason**: LDPC를 staircase product code 컴포넌트로 사용 + 신규 bit-flipping 디코딩 기법 제안; 바이너리 LDPC BP에 이식 가능 디코더 기여(C)로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9120519
- **Type**: conference
- **Published**: 25-28 May 
- **Authors**: V. B. Wijekoon, Emanuele Viterbo, Yi Hong
- **PDF**: https://ieeexplore.ieee.org/document/9120519
- **Abstract**: Staircase codes, a class of product-like codes, have been demonstrated to perform exceptionally well in optical transmission systems. Although they are predominantly used with BCH component codes and hard decision decoding, soft decision decoding has also been recently attempted, with BCH and polar code based staircase codes. We consider using LDPC codes as the component code of soft decoded staircase codes. Results demonstrate that these codes offer very good performance, with gains in the range of 0.5-1dB over soft decoded BCH-staircase codes, at a BER of 1$0^{-8}$. These can be further improved through the novel bit-flipping scheme we propose.

## Layered LDPC decoder in-order message access scheduling: a case study

- **Status**: ✅
- **Reason**: 레이어드 LDPC 디코더 in-order 메시지 접근 스케줄링/데이터해저드 회피 HW 기법 — NAND LDPC 디코더 아키텍처에 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9118787
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Oana Boncalo, Alexandru Amaricai
- **PDF**: https://ieeexplore.ieee.org/document/9118787
- **Abstract**: This paper discusses the problems of message map-ping and message access scheduling for data hazards avoidance in layered Low-Density Parity-Check Decoder architectures, by using in-order message update strategy. We provide a detailed description of the offline algorithm that provides the fine tuning of message access scheduling that mitigates pipeline related hazards. An increase of 25%, up to 66% in hardware usage efficiency has been obtained when using these algorithms, for WiMAX rate 3/4 code, for the minimum latency case (2 clock cycles), with respect to the case when no off-line optimizations are used. Similar results have been obtained for DVB-S2X code, with 10%, up to 47%, showing that the fine-tune access scheduling improves the throughput of the LDPC decoder architecture at the same cost.

## Codec Implementation of QC-LDPC Code in CCSDS Near-Earth Standard

- **Status**: ✅
- **Reason**: CCSDS type-II QC-LDPC 코덱 FPGA 구현, 인코더/디코더 HW 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9118542
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Juhua Wang, Suchun Yuan, Yuan Zhou +1
- **PDF**: https://ieeexplore.ieee.org/document/9118542
- **Abstract**: Recently, type-II quasi-cyclic (QC) low-density parity-check (LDPC) codes have attracted increasing attention due to their compact structures and promising decoding performance. In this paper, the type-II QC-LDPC code standardized for use in near-earth application is implemented by FPGA. On the basis of analysis for the generator matrix and parity-check matrix of the code, the codec for the type-II LDPC code is designed. By using an XC4VLX200-FPGA, the maximum clock frequency of the encoder is 287MHz at the cost of 810 slices and 15 Blockrams, while the maximum clock frequency of the decoder is 244 MHz at the cost of 10481 slices and 74 Blockrams. The testing result for the codec performance shows that such a code can completely satisfy the requirement for on-board channel coding application. The codec developed in this paper has been successfully employed in many remote-sensing satellite missions in China.

## Real-Time FPGA Verification for 25G-PON and 50G-PON LDPC Codes

- **Status**: ✅
- **Reason**: 25G/50G-PON LDPC 경판정/연판정 FPGA 실시간 구현 및 처리율/error floor 검증, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9192323
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Weiming Wang, Kai Tao, Weifeng Qian +7
- **PDF**: https://ieeexplore.ieee.org/document/9192323
- **Abstract**: Employing 75-piece FPGA implementation, we investigate the performance down to 10-15 BER of hard-decision 25G-PON LDPC and soft-decision 50G-PON LDPC at a record 90-Gbps throughput. FPGA emulations reveal soft-decision LDPC code offers more than 1.5dB coding gain with no error floor.
