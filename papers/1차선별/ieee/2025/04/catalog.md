# IEEE Xplore — 2025-04 (1차선별 통과)


## Finite-Length Puncturing Pattern Design for LDPC Codes With Hadamard Constraints

- **Status**: ✅
- **Reason**: 유한 길이 LDPC 코드용 puncturing 패턴 설계(EXIT 분석 + greedy 알고리즘)로 NAND LDPC 코드 설계에 직접 이식 가능 (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10891393
- **Type**: journal
- **Published**: April 2025
- **Authors**: Junyi Du, Peng Kang, Lei Xiao
- **PDF**: https://ieeexplore.ieee.org/document/10891393
- **Abstract**: In this letter, we propose a two-stage method to design finite-length puncturing patterns for LDPC codes with Hadamard constraints. At the first stage, we propose the distribution of puncturing patterns and develop extrinsic information transfer functions for distribution optimization in terms of the lowest decoding threshold. At the second stage, we analyze the iterative update process of a Hadamard check node (HCN) and find that the Euclidean distance determines the reliability of its output extrinsic information. Based on this, we propose a greedy algorithm to design puncturing patterns to maximize the number of punctured variable nodes with reliable input information. Simulations verify the good performance of the Hadamard-LDPC code with our designed puncturing patterns, compared to the 5G new radio LDPC code and the same Hadamard-LDPC code with other puncturing patterns.

## Channel-Aware Gradient Descent Bit-Flipping Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 channel-aware GDBF 알고리즘으로 error-floor 완화 및 성능 개선, NAND LDPC 디코더에 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10896727
- **Type**: journal
- **Published**: April 2025
- **Authors**: Woohong Min, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/10896727
- **Abstract**: The gradient descent bit-flipping with momentum (GDBF-w/M) and probabilistic GDBF-w/M (PGDBF-w/M) algorithms significantly improve the decoding performance of the bit-flipping (BF) algorithm. In this letter, we propose a channel-aware GDBF-w/M algorithm which operates deterministically based on the received values from the additive white Gaussian noise (AWGN) channel. Numerical results show that the proposed algorithm does not only mitigate the error-floor phenomenon of the GDBF-w/M algorithm, but it also has better decoding performance than the PGDBF-w/M algorithm without the need for a random number generator. Furthermore, the complexity of the proposed algorithm is slightly higher than that of the GDBF-w/M algorithm.

## Boosted Neural Decoders: Achieving Extreme Reliability of LDPC Codes for 6G Networks

- **Status**: ✅
- **Reason**: 부스티드 뉴럴 min-sum 디코더로 LDPC error floor 해결; boosting·block-wise 훈련·dynamic weight sharing 등 이식 가능한 신경망 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10845827
- **Type**: journal
- **Published**: April 2025
- **Authors**: Hee-Youl Kwak, Dae-Young Yun, Yongjune Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/10845827
- **Abstract**: Ensuring extremely high reliability in channel coding is essential for 6G networks. The next-generation of ultra-reliable and low-latency communications (xURLLC) scenario within 6G networks requires frame error rate (FER) below 10-9. However, low-density parity-check (LDPC) codes, the standard in 5G new radio (NR), encounter a challenge known as the error floor phenomenon, which hinders to achieve such low frame error rates. To tackle this problem, we introduce an innovative solution: boosted neural min-sum (NMS) decoder. This decoder operates identically to conventional NMS decoders, but is trained by novel training methods including: i) boosting learning with uncorrected vectors, ii) block-wise training schedule to address the vanishing gradient issue, iii) dynamic weight sharing to minimize the number of trainable weights, iv) transfer learning to reduce the required sample count, and v) data augmentation to expedite the sampling process. Leveraging these training strategies, the boosted NMS decoder achieves the state-of-the art performance in reducing the error floor as well as superior waterfall performance. Remarkably, we fulfill the 6G xURLLC requirement for 5G LDPC codes without a severe error floor. Additionally, the boosted NMS decoder, once its weights are trained, can perform decoding without additional modules, making it highly practical for immediate application. The source code is available at https://github.com/ghy1228/LDPC_Error_Floor.

## A 4.86-pJ/b Energy-Efficient Fully Parallel Stochastic LDPC Decoder With Two-Stage Shared Memory

- **Status**: ✅
- **Reason**: 55nm CMOS 완전 병렬 stochastic LDPC 디코더; shared-memory VN·RNG 공유 설계로 고처리량 달성 — NAND LDPC 디코더 HW(D) 이식 가능.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10747408
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yakun Zhou, Jienan Chen, Yizhuo Zhou +3
- **PDF**: https://ieeexplore.ieee.org/document/10747408
- **Abstract**: The complex calculations of the low-density parity-check (LDPC) decoder result in significant energy and hardware consumption. To solve the challenge, this brief describes a fully parallel stochastic LDPC decoder with a two-stage shared memory (TSM) variable node (VN). To enhance cost efficiency, our design incorporates a shared low-cost random number generator (RNG) for all 2160 channels. We introduce a TSM VN function, which demonstrates faster convergence and reduced hardware overhead in comparison with the existing methods. We have taped out the (2160, 1760) stochastic LDPC decoder in the 55-nm process. The measure results exhibit that the proposed design achieves a throughput of 57.6 Gb/s, an efficiency of 33.68 Gb/s/mm2, and a power efficiency of 4.86 pJ/bit, underlining superior performance in terms of decoding throughput, hardware efficiency, and energy conservation.

## Source-Constrained Hierarchical Modulation Systems With Protograph LDPC Codes: A Promising Transceiver Design for Future 6G-Enabled IoT

- **Status**: ✅
- **Reason**: Protograph LDPC 코드 설계 및 ILC 디코딩 스킴 포함; 무선 HM 특이적이나 P-LDPC 코드 설계 요소(E) 이식 가능성 있어 애매→보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10845840
- **Type**: journal
- **Published**: April 2025
- **Authors**: Zhaojie Yang, Yunye Li, Yong Liang Guan +1
- **PDF**: https://ieeexplore.ieee.org/document/10845840
- **Abstract**: This work studies the transceiver design and convergence performance analysis for the hierarchical modulation (HM) systems with protograph-based low-density parity-check (P-LDPC) codes. Specifically, we first conceive new source-constrained (SC) coding scheme and inter-layer-cascaded (ILC) decoding scheme tailored for the HM-based transmitter and receiver, respectively. Both the proposed SC coding and ILC decoding schemes form an enhanced version of bit-interleaved-coded HM (BIC-HM) systems, namely source-constrained HM (SC-HM) systems, providing a more reliable and flexible multi-data transmission solution. Moreover, according to the SC coding principle, we conceive a novel variable-node-degree-based (VND) multiplexing scheme to further improve the performance of the proposed SC-HM systems. Additionally, based on the ILC decoding framework, we devise a novel mutual information (MI) analysis tool, namely ILC-based extrinsic-information-transfer (ILC-EXIT) algorithm, to predict the decoding thresholds of the proposed P-LDPC-coded SC-HM systems. Theoretical and simulation results demonstrate that the proposed SC-HM systems significantly outperform the existing benchmarks in terms of error performance, decoding latency, and transmission-rate adaptation.

## Design and Performance Evaluation for BILCM-ID System With Improved Stopping Criterion

- **Status**: ✅
- **Reason**: BILCM-ID 시스템의 LDPC 반복 디코딩 개선 stopping criterion(NBEP 기반); stopping criterion 기법이 NAND LDPC 디코더(C)에 이식 가능 — 무선 응용 맥락으로 Phase 3 재검토.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10812956
- **Type**: journal
- **Published**: April 2025
- **Authors**: Xuhui Ding, Yuchen Xu, Gaoyang Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10812956
- **Abstract**: Low-density parity-check (LDPC) codes characterize both a relatively low decoding complexity and a performance nearing the Shannon limit. The integration of channel coding with modulation, known as bit-interleaved coded modulation (BICM), is widely utilized in communication and broadcasting systems. In particular, iterative message passing processes between soft demapper and decoder have proven effective in improving the bit error rate (BER) performance in the bit-interleaved LDPC coded modulation with iterative decoding (BILCM-ID) systems. This study proposes a novel approach for representing the iterative state in the probability domain for high-order modulation within the BILCM-ID process. Additionally, our methods introduce an improved stopping criterion based on the normalized belief evolution pattern (NBEP). Simulation analyses demonstrate that, compared to conventional hard-decision methods, the proposed algorithm can reduce ineffective iteration delay by approximately 88% with negligible degradation in BER performance.

## Performance Bounds and Degree-Distribution Optimization of Finite-Length BATS Codes

- **Status**: ✅
- **Reason**: LDPC precode의 degree distribution 최적화 및 finite-length BP/ML 성능 분석 포함(E); 네트워크 특이적이나 LDPC 코드 설계 요소 이식 가능성 있어 애매→보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10857390
- **Type**: journal
- **Published**: April 2025
- **Authors**: Mingyang Zhu, Shenghao Yang, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10857390
- **Abstract**: Batched sparse (BATS) codes were proposed as a reliable communication solution for networks with packet loss. In the finite-length regime, the error probability of BATS codes under belief propagation (BP) decoding has been studied in the literature and can be analyzed by recursive formulae. However, all existing analyses have not considered precoding or have treated the BATS code and the precode as two separate entities. In this paper, we analyze the word-wise error probability of finite-length BATS codes with a precode under joint decoding, including BP decoding and maximum-likelihood (ML) decoding. The joint BP decoder performs peeling decoding on a joint Tanner graph constructed from both the BATS and the precode Tanner graphs, and the joint ML decoder solves a single linear system with all linear constraints implied by the BATS code and the precode. We derive closed-form upper bounds on the error probability for both decoders. Specifically, low-density parity-check (LDPC) precodes are used for BP decoding, and any generic precode can be used for ML decoding. Even for BATS codes without a precode, the derived upper bound for BP decoding is more accurate than the approximate recursive formula, and easier to compute than the exact recursive formula. The accuracy of the two upper bounds has been verified by many simulation results. Based on the two upper bounds, we formulate an optimization problem to optimize the degree distribution of LDPC-precoded BATS codes, which improves BP performance, ML performance, or both. In our experiments, to transmit 128 packets over a line network with packet loss, the optimized LDPC-precoded BATS codes reduce the transmission overhead to less than 50% of that of standard BATS codes under comparable decoding complexity constraints.

## Toward Universal Belief Propagation Decoding for Short Binary Block Codes

- **Status**: ✅
- **Reason**: 단거리 블록 코드용 BP 디코딩 개선(sparse PCM 추출, 4-사이클 제거)으로 LDPC 디코더·사이클 제거 기법이 NAND LDPC에 이식 가능 (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10887536
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yifei Shen, Zongyao Li, Yuqing Ren +5
- **PDF**: https://ieeexplore.ieee.org/document/10887536
- **Abstract**: Belief propagation (BP) decoding has been recognized for its capacity-approaching performance and high throughput when decoding long low-density parity-check (LDPC) codes. However, the application of BP decoding for short codes is hindered by dense parity-check matrices (PCMs) and prevalent short cycles in the Tanner graph. In this paper, we introduce a general method to extract an optimized sparse PCM for short binary block codes, which removes length-four cycles and enhances the connectivity of short cycles to enable BP decoding with improved performance. Notably, for short binary codes with lengths up to 64, our BP decoding performance approaches the maximum likelihood bound and surpasses the best-reported BP results with reduced computational complexity. Compared with other universal decoding algorithms, BP decoding using our extracted sparse PCMs is competitive in terms of both error-rate performance and computational complexity. These promising results suggest that our method to improve BP decoding for short codes is a step toward a practical universal BP decoder for next-generation communication systems.

## Learning Rate-Compatible Linear Block Codes: An Auto-Encoder Based Approach

- **Status**: ✅
- **Reason**: AE 기반 rate-compatible 선형 블록 코드 설계(다중 puncturing 패턴·AI 디코더); rate-compatible 코드 설계 및 신경망 디코더 기법이 NAND LDPC(C/E)에 이식 가능 — 애매하여 Phase 3 재검토.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10786312
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yukun Cheng, Wei Chen, Tianwei Hou +2
- **PDF**: https://ieeexplore.ieee.org/document/10786312
- **Abstract**: Artificial intelligence (AI) provides an alternative way to design channel coding with affordable complexity. However, most existing studies can only learn codes for a given size and rate, typically defined by a fixed network architecture and a set of parameters. The support of multiple code rates is essential for conserving bandwidth under varying channel conditions while it is costly to store multiple AI models or parameter sets. In this article, we propose an auto-encoder (AE) based rate-compatible linear block codes (RC-LBCs). The coding process associated with AI or non-AI decoders and multiple puncturing patterns is optimized in a data-driven manner. The superior performance of the proposed AI-based RC-LBC is demonstrated through our numerical experiments.

## Practical MU-MIMO Detection and LDPC Decoding Through Digital Annealing

- **Status**: ✅
- **Reason**: 디지털 어닐링 기반 LDPC 디코딩에 새 비용함수 도입으로 정확도·복잡도 개선 — 이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10992822
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Po-Shao Chen, Wei Tang, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10992822
- **Abstract**: Digital annealing has been successfully applied to solving combinatorial optimization (CO) problems. It is more flexible, robust, and easier to deploy on edge platforms compared to its counterparts including quantum annealing and analog and in-memory Ising machines. In this work, we apply digital annealing to compute-intensive communication digital signal processing problems, including multi-user detection in multiple-input and multiple-output (MU-MIMO) wireless communication systems and decoding low-density parity-check (LDPC) codes. We show that digital annealing can achieve near maximum likelihood (ML) accuracy for MIMO detection with even lower complexity than the conventional minimum mean square error (MMSE) detection. In LDPC decoding, we enhance digital annealing by introducing a new cost function that improves decoding accuracy and reduces computational complexity compared to the standard formulations.

## DHD: Double Hard Decision Decoding Scheme for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시 직접; 이중 하드결정+LLR 개선+RRV 조정 디코딩 기법(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10993263
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Lanlan Cui, Yichuan Wang, Renzhi Xiao +3
- **PDF**: https://ieeexplore.ieee.org/document/10993263
- **Abstract**: With the advancement of NAND flash technology, the increased storage density leads to intensified interference, which in turn raises the error rate during data retrieval. To ensure data reliability, low-density parity-check (LDPC) codes are extensively employed for error correction in NAND flash memory. Although LDPC soft decision decoding offers high error correction capability, it comes with a significant latency. Conversely, hard-decision decoding, although faster, lacks sufficient error correction strength. Consequently, flash memory typically initiates with hard-decision decoding and resorts to multiple soft decision decoding upon failure. To minimize decoding latency, this paper proposes a decoding mechanism based on the double hard decision, called DHD. This DHD scheme improves the Log-Likelihood Ratio (LLR) in the hard decision process. After the first hard decision fails, the read reference voltage (RRV) is adjusted to perform the second hard decision decoding. If the second hard decision also fails, soft decision decoding is then employed. Experimental results demonstrate that when the Raw Bit Error Rate (RBER) is $8.5 \times 10^{-3}$, DHD reduces the Frame Error Rate (FER) by 86.4% compared to the traditional method.

## An Experimental Analysis of 50G-PON LDPC

- **Status**: ✅
- **Reason**: 50G-PON에서 LDPC 디코딩 파라미터(soft/hard 입력, 반복횟수) 실험 분석 — 이식 가능 디코더 파라미터 통찰(B/C, 애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11046425
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: L. Anet Neto, D. Chevalier, G. Simon +5
- **PDF**: https://ieeexplore.ieee.org/document/11046425
- **Abstract**: We experimentally assess the impacts of different LDPC decoding parameters with both soft- and hard-inputs in 50G-PON. We also derive the mean number of decoder iterations per received optical power over 25 km SSMF.

## Integrated high-performance LDPC decoder for Continuous-Variable Quantum Key Distribution System

- **Status**: ✅
- **Reason**: Integrated high-throughput LDPC decoder (Gbps) HW implementation for CV-QKD; decoder HW architecture potentially portable (D), keep for Phase 3 even though QKD app.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11046950
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Chuang Zhou, Yang Li, Li Ma +4
- **PDF**: https://ieeexplore.ieee.org/document/11046950
- **Abstract**: The throughput of the error correction decoding is one of the major bottlenecks of highspeed continuous-variable quantum key distribution (CV-QKD) systems and an integrated decoder with Gbps decoding throughput is implemented in this work. © 2024 The Authors OCIS codes: (270.5585) Quantum information and processing

## A comprehensive Study of Decoding Algorithms for Low Density Parity-Check(LDPC)

- **Status**: ✅
- **Reason**: LDPC 디코딩 알고리즘(BP·Min-Sum 변형) 종합 분석 + HW 친화 알고리즘 다룸, 이식 가능 디코더 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11035238
- **Type**: conference
- **Published**: 28-29 Apri
- **Authors**: C S Anil Kumar, M Vedhashri, L Vanditha +2
- **PDF**: https://ieeexplore.ieee.org/document/11035238
- **Abstract**: The near-capacity performance and effective decoding algorithms of Low-Density Parity-Check (LDPC) codes have made them a mainstay of contemporary error correction. With an emphasis on iterative techniques like the Belief Propagation (BP) algorithm, the Min-Sum algorithm, and their variations, this paper offers a thorough analysis of decoding algorithms for LDPC codes. We investigate the trade-offs between various algorithmic techniques’ computational complexity, decoding latency, and error correction performance. Particular focus is placed on new methods and hardware-friendly algorithms that are tailored for next-generation communication systems, such 5 G and beyond.

## Hardware Acceleration of LDPC Encoding Based on CGRA

- **Status**: ✅
- **Reason**: CGRA 기반 LDPC 인코딩 HW 가속(메모리 구조·데이터플로우 최적화) — HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11103139
- **Type**: conference
- **Published**: 25-27 Apri
- **Authors**: Zitong Zhou
- **PDF**: https://ieeexplore.ieee.org/document/11103139
- **Abstract**: Low-Density Parity-Check (LDPC) codes, as a class of capacity-approaching forward error correction codes, have been adopted as the encoding strategy for 5 G New Radio data channels. With the exponential increase in data throughput requirements for 5G communications, conventional FPGA-based architectures have demonstrated notable limitations in terms of computational efficiency and scalability. This paper introduces CGRA as a hardware acceleration approach for LDPC encoding. To address the issues of low memory utilization and low computing efficiency in CGRA, we employ data preprocessing, heterogenous memory architecture, and optimized dataflow to enhance hardware acceleration performance. Experimental results based on a $5 \times 5$ Processing Element Array (PEA) demonstrate that our approaches achieve significant performance improvements, including 80 % reduction in data access latency and 43 % decrease in computational processing time compared to baseline implementations.

## A Layered Improved Multi-Parameter Compensated Min-Sum Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 IMCMS/LIMCMS min-sum 변형 디코더 제안 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11035794
- **Type**: conference
- **Published**: 11-13 Apri
- **Authors**: Xuan Liu, Dongkui Chen
- **PDF**: https://ieeexplore.ieee.org/document/11035794
- **Abstract**: In modern communication technology, low-density parity-check codes (LDPC) are widely used as an extremely important channel coding method, and it has significant performance advantages when dealing with long codes. However, the complexity of LDPC decoding algorithms is high. In response to this phenomenon, based on MCMS decoding algorithm, this paper proposes an Improved Multi-parameter Compensated MinSum (IMCMS) decoding algorithm. This algorithm adds a threshold near zero at the minimum value and chooses a locally optimal algorithm when the minimum value is less than the threshold to avoid the zero return loss of MCMS decoding algorithm. On this basis, a layered scheduling strategy is applied to propose a Layered Improved Multi-parameter Compensated Min-Sum (LIMCMS) decoding algorithm. Simulation results show that the decoding algorithm proposed in this paper not only effectively improves bit error performance but also maintains low computational complexity and significantly accelerates the convergence speed of decoding in academic papers.
