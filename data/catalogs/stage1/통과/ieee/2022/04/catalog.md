# IEEE Xplore — 2022-04 (1차선별 통과)


## Reconstruction-Computation-Quantization (RCQ): A Paradigm for Low Bit Width LDPC Decoding

- **Status**: ✅
- **Reason**: RCQ low-bit-width LDPC decoding with dynamic non-uniform quantization, Min-Sum variant, layered DDE, FPGA impl on QC-LDPC — directly portable decoder/HW (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9706474
- **Type**: journal
- **Published**: April 2022
- **Authors**: Linfang Wang, Caleb Terrill, Maximilian Stark +7
- **PDF**: https://ieeexplore.ieee.org/document/9706474
- **Abstract**: This paper uses the reconstruction-computation-quantization (RCQ)paradigm to decode low-density parity-check (LDPC) codes. RCQ facilitates dynamic non-uniform quantization to achieve good frame error rate (FER) performance with very low message precision. For message-passing according to a flooding schedule, the RCQ parameters are designed by discrete density evolution. Simulation results on an IEEE 802.11 LDPC code show that for 4-bit messages, a flooding Min Sum RCQ decoder outperforms table-lookup approaches such as information bottleneck (IB) or Min-IB decoding, with significantly fewer parameters to be stored. Additionally, this paper introduces layer-specific RCQ, an extension of RCQ decoding for layered architectures. Layer-specific RCQ uses layer-specific message representations to achieve the best possible FER performance. For layer-specific RCQ, this paper proposes using layered discrete density evolution featuring hierarchical dynamic quantization (HDQ) to design parameters efficiently. Finally, this paper studies field-programmable gate array (FPGA) implementations of RCQ decoders. Simulation results for a (9472, 8192) quasi-cyclic (QC) LDPC code show that a layered Min Sum RCQ decoder with 3-bit messages achieves more than a 10% reduction in LUTs and routed nets and more than a 6% decrease in register usage while maintaining comparable decoding performance, compared to a 5-bit offset Min Sum decoder.

## Memory Efficient Mutual Information-Maximizing Quantized Min-Sum Decoding for Rate-Compatible LDPC Codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC용 메모리효율 MIM 양자화 min-sum 디코더+LUT — NAND LLR 양자화에 직결되는 새 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9684364
- **Type**: journal
- **Published**: April 2022
- **Authors**: Peng Kang, Kui Cai, Xuan He +1
- **PDF**: https://ieeexplore.ieee.org/document/9684364
- **Abstract**: In this letter, we propose a two-stage design method to construct memory efficient mutual information-maximizing quantized min-sum (MIM-QMS) decoder for rate-compatible low-density parity-check (LDPC) codes. We first develop a modified density evolution to design a unique set of lookup tables (LUTs) that can be used for rate-compatible LDPC codes. The constructed LUTs are optimized based on their discrepancy values and a merge function to reduce the memory requirement. Numerical results show that the proposed rate-compatible MIM-QMS decoder can reduce the memory requirement for decoding by up to 94.92 % compared to the benchmark rate-compatible LUT-based decoder with generally faster convergence speed. In addition, the proposed decoder can approach the performance of the floating-pointing belief propagation decoder within 0.15 dB.

## Node-Wise Scheduling Algorithm of ADMM Decoding Based on Line Segment Projection

- **Status**: ✅
- **Reason**: ADMM 기반 LDPC 디코딩의 노드별 스케줄링+선분투영 LSA 개선 — 새 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9681710
- **Type**: journal
- **Published**: April 2022
- **Authors**: Qiaoqiao Xia, Pinquan He, Xin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/9681710
- **Abstract**: In order to simplify the node-wise scheduling algorithm of the alternating direction method of multipliers (NS-ADMM) decoding, approximate line segment projection algorithm (LSA) is adopted to perform the projection in the node-wise scheduling algorithm. Experimental results show that using approximate line segment projection instead of precise projection in node-wise scheduling algorithm will yield a poor frame error rate (FER) performance. To solve this problem, dynamic scheduling strategy that selects the message-passing schedule according to the convergence status of the check node is proposed. Simulation results demonstrate that the modified node-wise scheduling algorithm based on line segment projection outperforms existing decoding algorithms in terms of FER performance and convergence speed, while it has good error correction performance with a lower computational complexity.

## A Study on Performance Evaluation With Neural Network Detector in SMR System

- **Status**: ✅
- **Reason**: SMR(자기기록) 스토리지에서 LDPC 반복디코딩에 신경망 검출기(NND)를 결합한 새 LLR 산출 기법 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9546790
- **Type**: journal
- **Published**: April 2022
- **Authors**: M. Nishikawa, Y. Nakamura, Y. Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/9546790
- **Abstract**: We previously applied a neural network detector (NND) to the low-density parity-check (LDPC) coding and iterative decoding system in a shingled magnetic recording (SMR) system. In this study, we evaluate the performance of iterative decoding using a new NND by computer simulation. The conventional NND gets the log-likelihood ratio (LLR) as the reliability of the sequence recorded from the two-dimensional finite impulse response (TD-FIR) filter output and the sum-product (SP) decoder output, but the new NND finds the LLR by adding the SP decoder input in order to consider the difference between the SP decoder input and the decoding result. Furthermore, we clarify that the new NND brings the almost same effect as the a posteriori probability (APP) decoder in the iterative decoding system.

## High throughput FPGA implementation of Min-Sum LDPC Decoder Architecture for Wireless Communication Standards

- **Status**: ✅
- **Reason**: QC-LDPC min-sum 디코더 FPGA 구현(파이프라이닝·병렬 멀티코어) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9790744
- **Type**: conference
- **Published**: 30 March-1
- **Authors**: Pavel Nikishkin, Ruslan Goriushkin, Nikita Vinogradov +2
- **PDF**: https://ieeexplore.ieee.org/document/9790744
- **Abstract**: This paper presents a min-sum decoder design for Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes. The design is supported various LDPC Parity-Check matrices including the WiMAX (IEEE 802.16e) and the WiFi (IEEE 802.11n) standards matrices. New techniques such as pipelining of the decoding architecture core are proposed. These core calculate variable-to-check (VTC) and new check-to-variable (CTV) messages and also update estimate of posterior probabilities (APPs). The parallel multicore decoding architecture implies a prior shift of values based on the LDPC matrix and simultaneous calculation of values for the core. Proposed decoder is implemented on the Zynq-7000 Mini-ITX Evaluation Board (XC7Z100-2FFG900).

## An Architecture for Efficient encoding of Quasi cyclic LDPC codes and its implementation in FPGA

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 FPGA HW 아키텍처, throughput·자원 최적화 — D 이식 가능 HW
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9787597
- **Type**: conference
- **Published**: 23-24 Apri
- **Authors**: G Sowmya, K Keerthi, J T Lalitkrushna +3
- **PDF**: https://ieeexplore.ieee.org/document/9787597
- **Abstract**: The Quasi Cyclic LDPC codes are one of the most widely used channel coding technique as they offer low complexity encoding along with parallelism in decoding. The existing architectures used for the encoding of such codes focus either on higher throughput or lower hardware resources. The proposed architecture optimizes both, especially for the implementation in space-qualified FPGAs where the resources are limited, yet higher throughput and encoding speed are expected. The proposed architecture can be used for any QC-LDPC code where the length of the information sequence is even multiple of the code’s Circulant size. As an illustration to the proposed architecture, an encoder for the CCSDS specified (8176, 7154) QC-LDPC codes is implemented in FPGA.

## Layered Bit-Flipping Algorithms for Decoding LDPC Codes

- **Status**: ✅
- **Reason**: Layered bit-flipping(LISBF) 새 디코더 + flipping threshold 최적화 기법, 스토리지 명시 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9778904
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Fangxia Luo, Xuan He, Jiongyue Xing +1
- **PDF**: https://ieeexplore.ieee.org/document/9778904
- **Abstract**: At present, various communication and storage systems have put forward high requirements on both the complexity and performance of low-density parity-check (LDPC) decoders. Bit flipping decoders are a good candidate for these applications. This letter proposes to utilize the column layered scheduling to speed up the convergence and improve the error correcting performance of existing bit flipping algorithms. As the information storage bit flipping (ISBF) algorithm generally performs the best, we investigate the layered ISBF (LISBF) algorithm in detail, including developing two efficient techniques for optimizing the computation of flipping thresholds: forward-backward computation and two-max computation. Simulation results on a (3, 6) LDPC code show that, compared to the ISBF algorithm, the LISBF algorithm can reduce the frame error rate by up to an order and reduce the average number of iterations by around 40%.

## Parallel LDPC Decoder Based on Low-Complexity Corrected Min Sum Algorithm

- **Status**: ✅
- **Reason**: Low-Complexity Corrected Min Sum(LCC-MS) 새 디코더 알고리즘 + HW 구현 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9849693
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Yisong Sun, Huan Li, Xinyu Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/9849693
- **Abstract**: To correct the errors introduced by the approximation in the Min Sum (MS) algorithm with low complexity, we proposed Low-Complexity Corrected Min Sum (LCC-MS) algorithm. Aiming at the implementation bottleneck of the algorithm on the self-developed DSP (Universal Communication Processor, UCP), we optimized the algorithm process and expanded the instruction set of UCP. Therefore, the LDPC decoder based on LCC-MS algorithm is implemented on UCP, and verified on the chip that has been taped out. The verification results of the longest code length and the highest code rate show that the LCC-MS algorithm has a gain of 0.16dB when the bit error rate is 10-5 compared with the MS algorithm, and the decoder based on LCC-MS algorithm can process up to 149 code blocks in one time slot.

## Implicit Globally-Coupled LDPC Codes Using Free-Ride Coding

- **Status**: ✅
- **Reason**: implicit GC-LDPC 신규 코드 구성(레이트 손실 없이 글로벌 패리티, 컴포넌트 인코더 재사용). 바이너리 LDPC 코드 설계 기여(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9771931
- **Type**: conference
- **Published**: 10-13 Apri
- **Authors**: Xiao Ma, Qianfan Wang, Mangang Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/9771931
- **Abstract**: In this paper, we present a new construction of the globally-coupled LDPC (GC-LDPC) codes, referred to as implicit GC-LDPC codes, where the additional global parity-check bits are transmitted using the free-ride coding. The presented GC-LDPC codes have the same rates as the component LDPC codes, avoiding the rate reduction caused by the global parity checks for the conventional GC-LDPC codes. Moreover, the encoders of the component LDPC codes are reusable in the presented GC-LDPC codes, a distinguished feature as compared with the conventional GC-LDPC codes. The simulation results show that the proposed implicit GC-LDPC codes can improve the performance of the component LDPC codes, yielding extra coding gain of up to 0.7 dB (with (3,6)-regular LDPC codes as the component codes) and 0.5 dB (with IEEE 802.16e LDPC codes as the component codes).

## Joint estimation and decoding algorithm for LDPC code in different impulsive noise channel

- **Status**: ✅
- **Reason**: C: 임펄스 잡음 채널 LDPC 디코더에 사후확률 활용 joint estimation-decoding 반복기법 — 잡음 적응형 디코딩 개선으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9771567
- **Type**: conference
- **Published**: 10-13 Apri
- **Authors**: Chong Xu, Hongbo Zhao, Ling Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9771567
- **Abstract**: This paper presents a joint estimation and decoding algorithm for decoding over different impulsive noise in practical use, as the state of most impulsive noise changes rapidly in the wireless networks and cause performance degradation of low-density parity-check (LDPC) code decoding. The proposed algorithm fully utilizes the posteriori probability information of the decoding algorithm to strengthen estimation instead of regarding as the probability of input as equal probability. First, we derive the simplified objective of estimation expression. Then we designed the whole process of algorithm, which combines the estimator and decoder in an iterative manner. The simulation results show that the decoding performance of the proposed decoder can reach nearly known real noise parameters decoder within 0.1dB. Comparing with previous decoders, the proposed decoder has lower bit error rate (BER).

## Joint MIMO Detection and LDPC Decoding Via Enhanced Belief Propagation for 5G-NR

- **Status**: ✅
- **Reason**: BP 기반 결합 검출-복호에 pre-filtering/partial marginalization/스케줄링/damping 등 BP 개선 기법 제시. 디코더 알고리즘 일부 이식 가능(C, 애매하나 살림).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9771941
- **Type**: conference
- **Published**: 10-13 Apri
- **Authors**: Jing Qian, Sha Hu, Hao Wang
- **PDF**: https://ieeexplore.ieee.org/document/9771941
- **Abstract**: In this paper, we consider joint MIMO detection and LDPC decoding on a tripartite factor graph. Conventional method in this regard design a belief propagation (BP) detector that applies an matched filtering detection per layer by subtracting interferences from other layers, which is suboptimal. Further, the BP scheduling between detection and decoding is unoptimized, which makes the interaction less effective. To overcome these issues, we propose to enhance the BP based joint detection and decoding (BP-JDD) receiver with 4 different techniques: pre-filtering (PF), partial marginalization (PM), hybrid updating schedule (HUS) and damping. Among them, PF and PM can improve the BP detection under challenging conditions, such as correlated MIMO channels, high-order modulations, or high code-rates, while HUS and damping are effective to accelerate convergence and reduce the number of overall iterations for BP-JDD to succeed. Combining these 4 techniques yields an enhanced BP-JDD design that can provide significant performance gains over traditional turbo receivers, and is also robust against channel variations.
