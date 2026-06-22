# IEEE Xplore — 2006-12 (1차선별 통과)


## Improvements in belief-propagation decoding based on averaging information from decoder and correction of clusters of nodes

- **Status**: ✅
- **Reason**: BP 디코딩 개선(워터폴: 디코더 평균정보 피드백 / 에러플로어: 클러스터 정정) — 부호 비의존 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4027623
- **Type**: journal
- **Published**: December 2
- **Authors**: Nedeljko Varnica, Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4027623
- **Abstract**: In this letter we provide several methods to improve belief-propagation (BP) decoding of low-density parity-check codes. The methods use additional processing of the decoded information during the decoding process and are grouped into two categories. The first category is useful in the waterfall performance region and is based on processing averaged information obtained from the decoder. Several choices of the feedback information utilized in additional processing are introduced. The second category is useful in the error-floor performance region and is based on fixing clusters of symbols simultaneously, again utilizing the information obtained by monitoring the decoder. We demonstrate on a code example that our methods achieve sizeable gains compared to the original BP decoder

## Graphical Inference Methods for Fault Diagnosis based on Information from Unreliable Sensors

- **Status**: ✅
- **Reason**: LDPC BP 기반 반복 신뢰전파 알고리즘(C), 부호 비의존 메시지패싱 기법 분석
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150125
- **Type**: conference
- **Published**: 5-8 Dec. 2
- **Authors**: Tung Le, Christoforos N. Hadjicostis
- **PDF**: https://ieeexplore.ieee.org/document/4150125
- **Abstract**: In this paper, we study the application of decoding algorithms to the multiple fault diagnosis (MFD) problem. Prompted by the resemblance between graphical representations for MFD problems and parity check codes, we develop a suboptimal iterative belief propagation algorithm (BPA) that is based on the graphical inference method for low density parity check codes. Our simulation results suggest that the algorithm performance strongly depends on the connection density and the reliability of the alarm network. In particular, when the connection density is low and when the alarms and/or connections are unreliable, the algorithm performs almost optimally, i.e., it converges to the solution with the highest posterior probability most of the times. We also provide analytical bounds on the performance of the algorithm for special classes of systems in our framework

## An FPGA Implementation of Array LDPC Decoder

- **Status**: ✅
- **Reason**: D: array LDPC 디코더 FPGA 구현, 메모리/배선 절감 아키텍처 — 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4145732
- **Type**: conference
- **Published**: 4-7 Dec. 2
- **Authors**: Jin Sha, Minglun Gao, Zhongjin Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/4145732
- **Abstract**: Low-Density Parity-Check (LDPC) code is one kind of prominent error correcting codes (ECC) being considered in next generation industry standards. This paper presents an FPGA implementation of array code based Low-Density Parity-Check code decoder. The advantages of the proposed architecture as compared to the fully parallel or partially parallel architecture are: less memory requirement, avoidance of complex global interconnects and its satisfying throughput. These advantages are derived from exploiting the well-defined structure of the parity check matrix of array code based LDPC codes.

## Memory-Efficient Accelerating Schedule for LDPC Decoder

- **Status**: ✅
- **Reason**: 메모리효율 가속 스케줄 LDPC 디코더(단일포트 메모리+FIFO 버퍼링) — 이식 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4145643
- **Type**: conference
- **Published**: 4-7 Dec. 2
- **Authors**: Kazunori Shimizu, Nozomu Togawa, Takeshi Ikenaga +1
- **PDF**: https://ieeexplore.ieee.org/document/4145643
- **Abstract**: This paper proposes a memory-efficient accelerating schedule for LDPC decoder. Important properties of the proposed techniques are as follows: (i) partitioning a pipelined operation not to read and write intermediate messages simultaneously enables the accelerated message-passing schedule to be implemented with single-port memories, (ii) FIFO-based buffering reduces the number of memory banks and words for the decoder based on the accelerated message-passing schedule. The proposed decoder reduces the memories for intermediate messages by half compared to the conventional one based on the accelerated message-passing schedule

## WLC16-2: Reliability-Based Hybrid ARQ (RB-HARQ) Schemes using Low-Density Parity-Check (LDPC) Codes

- **Status**: ✅
- **Reason**: LDPC 코드 구조를 이용해 RB-HARQ 재전송비트 선택(row-base)을 LLR 기반으로 개선, LDPC 패리티검사 구조 활용 기법으로 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4151335
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Yoichi Inaba, Tomonori Saito, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/4151335
- **Abstract**: The reliability-based hybrid ARQ (RB-HARQ) scheme, which can be used with error correcting codes using soft-input soft-output (SISO) decoders such as convolutional codes and turbo codes, has been proposed. In the RB-HARQ scheme, the error rate performance is improved by selecting retransmission bits based on log likelihood ratio (LLR) of each bit in the receiver. However, the receiver has to send the bit positions of retransmission bits to the transmitter. Therefore, the RB-HARQ scheme requires a large number of feedback bits. On the other hand, low density parity check (LDPC) codes are recently attracting a lot of interest, because LDPC codes can achieve near Shannon limit performance. In this paper, we evaluate the RB-HARQ scheme using LDPC codes. Moreover, we propose a RB-HARQ scheme that requires a fewer feedback bits by utilizing a code structure of LDPC code. We refer to the scheme as the RB-HARQ (row base) scheme. We show that the RB-HARQ and RB-HARQ (row base) schemes using LDPC codes have better error rate performance and higher throughput performance than no ARQ scheme. We also show that the RB- HARQ (row base) scheme has a good trade-off between error rate performance and the number of feedback bits compared to the RB-HARQ scheme.

## CTH08-4: Protograph LDPC Codes with Node Degrees at Least 3

- **Status**: ✅
- **Reason**: Protograph LDPC code construction with low decoding thresholds, linear minimum distance, rate-compatibility, FPGA validation — transferable binary code design (E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150708
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Dariush Divsalar, Christopher Jones
- **PDF**: https://ieeexplore.ieee.org/document/4150708
- **Abstract**: In this paper we present protograph codes with degree-3 nodes and one high degree node. The iterative decoding threshold for proposed rate 1/2 codes are lower, by about 0.2 dB, than the best known irregular LDPC codes with degree at least 3. The main motivation is to construct rate-compatible protograph-based LDPC codes for fixed code block length (n) that simultaneously achieve low iterative decoding thresholds and guarantee minimum distance that is linearly increasing with n. We start with a rate 1/2 protograph LDPC code with degree-3 nodes and one high degree node. Higher rate codes are obtained by connecting check nodes with degree-2 non-transmitted nodes. This is equivalent to constraint combining in the protograph. The condition where all constraints are combined corresponds to the highest rate code. Through examples we show that iterative decoding thresholds as low as 0.544 dB can be achieved for small protographs with node degrees at least three. FPGA simulation results show that the proposed family of codes perform as predicted.

## CTH08-5: Efficient Encoding and Termination of Low-Density Parity-Check Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional code (SC-LDPC) efficient encoding/termination with HW architecture — transferable binary code-design/HW (E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150709
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Zhengang Chen, Stephen Bates, Duncan Elliott +1
- **PDF**: https://ieeexplore.ieee.org/document/4150709
- **Abstract**: Low-density parity-check convolutional codes (LDPC-CCs) have been shown to have similar capacity-approaching performance to LDPC block codes. Their encoder structure is simple and efficient. However, the encoder termination, which is required when applied to finite length data frames, increases the encoder complexity and reduces the effective code rate. The LDPC-CC encoding and termination problems are discussed in this paper. A novel all-phase termination scheme is proposed with less implementation complexity and less loss in code rate, compared to existing methods. Finally a system architecture for the LDPC-CC encoder with all-phase termination is given with some analyses.

## CTH08-2: EXIT Chart Analysis for Doubly Generalized LDPC Codes

- **Status**: ✅
- **Reason**: Doubly generalized LDPC code design via EXIT chart optimization — transferable binary code-design/analysis technique (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150706
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Yige Wang, Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4150706
- **Abstract**: The design of generalized low-density parity-check (GLDPC) codes at both check and bit nodes over AWGN channel is considered in this paper. The new codes are referred to as doubly generalized LDPC codes. EXIT charts are used to optimize the parameters of these codes. Closed forms of EXIT functions for some subcodes are presented. Both analysis and simulations show that this method can provide more flexibility in constructing codes with good threshold.

## GEN03-6: Investigation of Error Floors of Structured Low-Density Parity-Check Codes by Hardware Emulation

- **Status**: ✅
- **Reason**: 구조적 LDPC(permutation submatrix) error floor를 HW 에뮬레이션으로 분석, fixed-point 디코딩 효과 규명 및 개선 디코딩 전략 - error floor/HW 기법(D/E 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150790
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Zhengya Zhang, Lara Dolecek, Borivoje Nikolic +2
- **PDF**: https://ieeexplore.ieee.org/document/4150790
- **Abstract**: Several high performance LDPC codes have parity-check matrices composed of permutation submatrices. We design a parallel-serial architecture to map the decoder of any structured LDPC code in this large family to a hardware emulation platform. A peak throughput of 240 Mb/s is achieved in decoding the (2048,1723) Reed-Solomon based LDPC (RS-LDPC) code. Experiments in the low bit error rate (BER) region provide statistics of the error traces, which are used to investigate the causes of the error floor. In a low precision implementation, the error floors are dominated by the fixed-point decoding effects, whereas in a higher precision implementation the errors are attributed to special configurations within the code, whose effect is exacerbated in a fixed-point decoder. This new characterization leads to an improved decoding strategy and higher performance.

## CTH14-6: Error Correction Using a Message-Passing Decoder to Process Cyclic Redundancy Checks

- **Status**: ✅
- **Reason**: CRC 패리티검사행렬 sparsification으로 short cycle 제거 후 LDPC용 MPD 적용 - 부호 비의존적 sparsification/사이클제거 기법(C/E 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150746
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Quentin H. Spencer
- **PDF**: https://ieeexplore.ieee.org/document/4150746
- **Abstract**: This paper proposes a method for correcting errors in messages encoded using cyclic redundancy checks (CRCs), which are typically only used for error detection. This is accomplished for messages of a known length by deriving a parity-check matrix representation of the CRC. The parity-check matrix can then be used to correct errors using the message-passing decoder (MPD) commonly used to decode LDPC codes. The CRC parity-check matrix is not sparse, which inhibits performance of the MPD, but this effect can be reduced by modifying the matrix using recently proposed sparsification techniques to eliminate short cycles. The technique is practical mainly for codes with short block sizes, and can also be applied to coding schemes that concatenate a CRC with an outer error correcting code. Simulation results demonstrate some performance gains, although less than what can be gained using custom-designed LDPC codes for the same rate and message length.

## CTH02-4: When Does One Redundant Parity-Check Equation Matter?

- **Status**: ✅
- **Reason**: Redundant parity-check equations to break trapping sets and improve error-floor of binary LDPC — directly transferable decoder/code technique (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4150674
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Stefan Laendner, Thorsten Hehn, Olgica Milenkovic +1
- **PDF**: https://ieeexplore.ieee.org/document/4150674
- **Abstract**: We analyze the effect of redundant parity-check equations on the error-floor performance of low-density parity- check (LDPC) codes used over the additive white Gaussian noise (AWGN) channel. Our findings show that a large number of iterative decoding errors in the [2640,1320] Margulis code, confined to point trapping sets in the standard Tanner graph, can be corrected if only one redundant parity-check equation is added to the decoder's matrix. We also derive an analytic expression relating the number of rows in the parity-check matrix of a code and the parameters of trapping sets in the code's graph.

## WLC36-2: Convergence Acceleration of Iterative Signal Detection for MIMO System with Belief Propagation

- **Status**: ✅
- **Reason**: BP 반복검출 수렴가속(LLR 갱신 빈도 증가, 비트그룹 분할) 기법으로 BP 스케줄링 개선이 LDPC BP에 이식 가능성 있어 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4151454
- **Type**: conference
- **Published**: 27 Nov.-1 
- **Authors**: Satoshi Gounai, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/4151454
- **Abstract**: In multiple-input multiple-output (MIMO) wireless systems, the receiver must extract each transmitted signal from received signals. An iterative signal detection with belief propagation (BP) is an attractive technique for MIMO systems. This technique can improve the error rate performance with increasing the number of detection and decoding iterations. This number is, however, limited in actual systems because each additional iteration increases the latency, receiver size, and so on. This paper proposes a convergence acceleration technique that can achieve better error rate performance with fewer iterations than the conventional iterative signal detection. Since the log-likelihood ratio (LLR) or a probability of one bit propagates to all other bits with BP, improving some LLRs improves overall decoder performance. In our proposal, all the coded bits are divided into groups and only one group is detected in each iterative signal detection whereas in the conventional approach, each iterative signal detection run processes all coded bits, simultaneously. Our proposal increases the frequency of initial LLR update (for BP) by increasing the number of iterative signal detections and decreasing the number of coded bits that the receiver detects in one iterative signal detection. Computer simulations show that our proposal achieves better error rate performance with fewer detection and decoding iterations than the conventional approach.

## Interconnect-Efficient LDPC Code Design

- **Status**: ✅
- **Reason**: interconnect 효율 LDPC 디코더 HW 지향 코드설계 — 면적/지연/라우팅 최적화, NAND LDPC HW 아키텍처에 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4243665
- **Type**: conference
- **Published**: 16-19 Dec.
- **Authors**: Aiman El-Maleh, Basil Arkasosy, M. Adnan Al-Andalusi
- **PDF**: https://ieeexplore.ieee.org/document/4243665
- **Abstract**: In this paper, we present a new, hardware-oriented technique for designing Low Density Parity Check (LDPC) codes. The technique targets to achieve an interconnect- efficient architecture that reduces the area and delay of the decoder implementation while maintaining good error correction performance. With a fully parallel implementation of the LDPC decoder, the proposed design assumes a constraint on the interconnect wire length which has a direct impact on the maximum signal delay and power dissipation. Furthermore, this design approach is shown to lower interconnect routing congestion, and hence reduce the chip area and maximize chip utilization.

## Root Locus Plots and Iterative Decoding

- **Status**: ✅
- **Reason**: LDPC 반복 디코더의 고정점을 root locus로 분석하는 기법, 디코더 수렴/동역학 통찰로 이식 가능(C, 애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4177969
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Christopher M. Kellett
- **PDF**: https://ieeexplore.ieee.org/document/4177969
- **Abstract**: A well known class of error correction codes called low-density parity-check (LDPC) codes have been the subject of a great deal of recent study in the coding community as a result of their ability to approach Shannon's fundamental capacity limit. Crucial to the performance of these codes is the use of an iterative decoder. We describe LDPC codes and the decoding algorithm and make a connection between the fixed points of the decoding algorithm and the well-known root locus plot. Via two example LDPC codes, we describe the insights afforded by the root locus plot

## A DVB-S2 compliant LDPC decoder integrating the Horizontal Shuffle Scheduling

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더의 Horizontal Shuffle Scheduling 병렬 HW 아키텍처 및 데이터 충돌 회피 기법, NAND LDPC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4212426
- **Type**: conference
- **Published**: 12-15 Dec.
- **Authors**: Arthur Segard, Francois Verdier, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/4212426
- **Abstract**: Low-density parity check codes (LDPC) are a class of channel decoding codes used in digital communications. Very high error correcting performances can be reached with such codes but they require both a great computing effort and randomly constructed decoding matrices. LDPC codes are used to perform the channel coding of the satellite television broadcast standard DVB-S2. This paper proposes a way to design massively parallel hardware architecture of DVB-S2 compliant LDPC decoders. It is based on a particular way to schedule all the algorithm's calculations. The proposed architecture speeds-up the decoding process, allowing the algorithm to converge faster with no significant performance loss. Moreover, a particular data update mechanism has been developed in order to avoid all data conflicts inherent to DVB-S2 matrices even for highly parallel implementations. This paper describes our hardware LDPC decoder architecture and its processing elements. Estimated silicon area of this decoder is 11 mm in ST 90 nm technology and the decoding throughput reaches 591 M bps at 300 MHz for rate 1/2 and code size of 64800
