# IEEE Xplore — 2025-04


## Finite-Length Puncturing Pattern Design for LDPC Codes With Hadamard Constraints

- **Status**: ✅
- **Reason**: 유한 길이 LDPC 코드용 puncturing 패턴 설계(EXIT 분석 + greedy 알고리즘)로 NAND LDPC 코드 설계에 직접 이식 가능 (E)
- **ID**: ieee:10891393
- **Type**: journal
- **Published**: April 2025
- **Authors**: Junyi Du, Peng Kang, Lei Xiao
- **PDF**: https://ieeexplore.ieee.org/document/10891393
- **Abstract**: In this letter, we propose a two-stage method to design finite-length puncturing patterns for LDPC codes with Hadamard constraints. At the first stage, we propose the distribution of puncturing patterns and develop extrinsic information transfer functions for distribution optimization in terms of the lowest decoding threshold. At the second stage, we analyze the iterative update process of a Hadamard check node (HCN) and find that the Euclidean distance determines the reliability of its output extrinsic information. Based on this, we propose a greedy algorithm to design puncturing patterns to maximize the number of punctured variable nodes with reliable input information. Simulations verify the good performance of the Hadamard-LDPC code with our designed puncturing patterns, compared to the 5G new radio LDPC code and the same Hadamard-LDPC code with other puncturing patterns.

## Soft-Output (SO) GRAND and Iterative Decoding to Outperform LDPC Codes

- **Status**: ❌
- **Reason**: GRAND 기반 product code로 LDPC를 대체하는 방식; LDPC 자체 디코더/코드 설계 기법이 아닌 대체 방식으로 이식 가능한 ECC 기법 없음
- **ID**: ieee:10852599
- **Type**: journal
- **Published**: April 2025
- **Authors**: Peihong Yuan, Muriel Médard, Kevin Galligan +1
- **PDF**: https://ieeexplore.ieee.org/document/10852599
- **Abstract**: We establish that a large, flexible class of long, high redundancy error correcting codes can be efficiently and accurately decoded with guessing random additive noise decoding (GRAND). Performance evaluation demonstrates that it is possible to construct simple product codes with lengths of approximately 200 to 4000 bits and rates between 0.2 and 0.8 that outperform low-density parity-check (LDPC) codes from the 5G New Radio standard in both AWGN and fading channels. The concatenated structure enables many desirable features, including: low-complexity hardware-friendly encoding and decoding; significant flexibility in length and rate through modularity; and high levels of parallelism in encoding and decoding that enable low latency. Central is the development of a method through which any soft-input (SI) GRAND algorithm can provide soft-output (SO) in the form of an accurate a-posteriori estimate of the likelihood that a decoding is correct or, in the case of list decoding, the likelihood that each element of the list is correct. The distinguishing feature of soft-output GRAND (SOGRAND) is the provision of an estimate that the correct decoding has not been found, even when providing a single decoding. Per-block SO can be converted into accurate per-bit SO by a weighted sum that includes a term for the SI. Implementing SOGRAND adds negligible computation and memory to the existing decoding process, and using it results in a practical, low-latency alternative to LDPC codes.

## Channel-Aware Gradient Descent Bit-Flipping Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 channel-aware GDBF 알고리즘으로 error-floor 완화 및 성능 개선, NAND LDPC 디코더에 이식 가능 (C)
- **ID**: ieee:10896727
- **Type**: journal
- **Published**: April 2025
- **Authors**: Woohong Min, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/10896727
- **Abstract**: The gradient descent bit-flipping with momentum (GDBF-w/M) and probabilistic GDBF-w/M (PGDBF-w/M) algorithms significantly improve the decoding performance of the bit-flipping (BF) algorithm. In this letter, we propose a channel-aware GDBF-w/M algorithm which operates deterministically based on the received values from the additive white Gaussian noise (AWGN) channel. Numerical results show that the proposed algorithm does not only mitigate the error-floor phenomenon of the GDBF-w/M algorithm, but it also has better decoding performance than the PGDBF-w/M algorithm without the need for a random number generator. Furthermore, the complexity of the proposed algorithm is slightly higher than that of the GDBF-w/M algorithm.

## Boosted Neural Decoders: Achieving Extreme Reliability of LDPC Codes for 6G Networks

- **Status**: ✅
- **Reason**: 부스티드 뉴럴 min-sum 디코더로 LDPC error floor 해결; boosting·block-wise 훈련·dynamic weight sharing 등 이식 가능한 신경망 디코더 알고리즘(C)
- **ID**: ieee:10845827
- **Type**: journal
- **Published**: April 2025
- **Authors**: Hee-Youl Kwak, Dae-Young Yun, Yongjune Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/10845827
- **Abstract**: Ensuring extremely high reliability in channel coding is essential for 6G networks. The next-generation of ultra-reliable and low-latency communications (xURLLC) scenario within 6G networks requires frame error rate (FER) below 10-9. However, low-density parity-check (LDPC) codes, the standard in 5G new radio (NR), encounter a challenge known as the error floor phenomenon, which hinders to achieve such low frame error rates. To tackle this problem, we introduce an innovative solution: boosted neural min-sum (NMS) decoder. This decoder operates identically to conventional NMS decoders, but is trained by novel training methods including: i) boosting learning with uncorrected vectors, ii) block-wise training schedule to address the vanishing gradient issue, iii) dynamic weight sharing to minimize the number of trainable weights, iv) transfer learning to reduce the required sample count, and v) data augmentation to expedite the sampling process. Leveraging these training strategies, the boosted NMS decoder achieves the state-of-the art performance in reducing the error floor as well as superior waterfall performance. Remarkably, we fulfill the 6G xURLLC requirement for 5G LDPC codes without a severe error floor. Additionally, the boosted NMS decoder, once its weights are trained, can perform decoding without additional modules, making it highly practical for immediate application. The source code is available at https://github.com/ghy1228/LDPC_Error_Floor.

## On Minimal Pseudocodewords of Binary Hamming Codes

- **Status**: ❌
- **Reason**: Hamming code pseudocodewords LP 디코딩 이론 분석; LDPC 직접 미언급이고 순수 이론 bound으로 디코더/HW/코드설계로 이어지지 않음
- **ID**: ieee:10857453
- **Type**: journal
- **Published**: April 2025
- **Authors**: Haiyang Liu, Xiaopeng Jiao, Lianrong Ma
- **PDF**: https://ieeexplore.ieee.org/document/10857453
- **Abstract**: Pseudocodewords, and in particular minimal pseudocodewords, play an important role in understanding the performance of linear programming (LP) decoding. In this paper, we investigate minimal pseudocodewords of binary Hamming codes described by full-rank parity-check matrices. We first provide some general results on minimal pseudocodewords with support size 3 of a binary parity-check matrix. We also prove a lower bound on the minimum binary symmetric channel (BSC) pseudoweight of a binary parity-check matrix. Then we prove that a full-rank parity-check matrix of a binary Hamming code has minimal pseudocodewords of certain types whose support sizes are larger than 3. Interestingly enough, the BSC pseudoweight of all these minimal pseudocodewords is 2. Using this fact as well as the above-mentioned lower bound, we further prove that a full-rank parity-check matrix of a binary Hamming code has minimum BSC pseudoweight 2. Moreover, the additive white Gaussian noise channel (AWGNC) pseudoweight of all these minimal pseudocodewords is 3. Based on numerical observations, we conjecture that a full-rank parity-check matrix of a binary Hamming code has minimum AWGNC pseudoweight 3. Finally, we provide more properties of a subset of minimal pseudocodewords of a full-rank parity-check matrix of a binary Hamming code.

## Novel Double Protograph LDPC Codes for Joint Source-Channel Coding Systems

- **Status**: ❌
- **Reason**: Double protograph LDPC를 이용한 JSCC 논문; protograph 설계가 소스-채널 결합 최적화에 종속되어 독립적으로 이식할 LDPC ECC 설계 기법 없음.
- **ID**: ieee:10770606
- **Type**: journal
- **Published**: April 2025
- **Authors**: Jia Zhan, Wai-Man Tam, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/10770606
- **Abstract**: In this paper, we first propose a novel joint source-channel block code (JSC-BC) in which two protograph-based low-density parity-check (P-LDPC) block codes are connected not only by a source-variable-channel-check (SVCC) linking matrix, but also by a source-check-channel-variable (SCCV) linking matrix that consists of a zero matrix and a lower or upper triangular (base) matrix with “1”s on its diagonal. Also, we simplify the traditional joint protograph extrinsic information transfer (JP-EXIT) algorithm and propose an “untransmitted protograph-based EXIT (UP-EXIT) algorithm” for calculating the source threshold of a JSC-BC. The proposed UP-EXIT algorithm is more efficient because a smaller protograph consisting of only the untransmitted VNs (i.e., the source VNs and the punctured channel VNs) and their connected check nodes need to be considered. By using the UP-EXIT algorithm, we search for candidate codes with high source thresholds. Then, we select those among the candidate codes also with low channel thresholds. Theoretical and simulation results show that the newly constructed codes outperform state-of-the-art double P-LDPC (DP-LDPC) block codes. Furthermore, we spatially couple the joint source-channel block code and obtain a spatially coupled joint source-channel code (SC-JSCC). Theoretical analyses and simulation results show that even with a smaller window size and lower decoding complexity, the SC-JSCC with the spatially coupled structure for each sub-block (source protomatrix, channel protomatrix, SCCV linking matrix, and SVCC linking matrix) can achieve better error performance than existing spatially-coupled DP-LDPC codes.

## A 4.86-pJ/b Energy-Efficient Fully Parallel Stochastic LDPC Decoder With Two-Stage Shared Memory

- **Status**: ✅
- **Reason**: 55nm CMOS 완전 병렬 stochastic LDPC 디코더; shared-memory VN·RNG 공유 설계로 고처리량 달성 — NAND LDPC 디코더 HW(D) 이식 가능.
- **ID**: ieee:10747408
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yakun Zhou, Jienan Chen, Yizhuo Zhou +3
- **PDF**: https://ieeexplore.ieee.org/document/10747408
- **Abstract**: The complex calculations of the low-density parity-check (LDPC) decoder result in significant energy and hardware consumption. To solve the challenge, this brief describes a fully parallel stochastic LDPC decoder with a two-stage shared memory (TSM) variable node (VN). To enhance cost efficiency, our design incorporates a shared low-cost random number generator (RNG) for all 2160 channels. We introduce a TSM VN function, which demonstrates faster convergence and reduced hardware overhead in comparison with the existing methods. We have taped out the (2160, 1760) stochastic LDPC decoder in the 55-nm process. The measure results exhibit that the proposed design achieves a throughput of 57.6 Gb/s, an efficiency of 33.68 Gb/s/mm2, and a power efficiency of 4.86 pJ/bit, underlining superior performance in terms of decoding throughput, hardware efficiency, and energy conservation.

## Source-Constrained Hierarchical Modulation Systems With Protograph LDPC Codes: A Promising Transceiver Design for Future 6G-Enabled IoT

- **Status**: ✅
- **Reason**: Protograph LDPC 코드 설계 및 ILC 디코딩 스킴 포함; 무선 HM 특이적이나 P-LDPC 코드 설계 요소(E) 이식 가능성 있어 애매→보존
- **ID**: ieee:10845840
- **Type**: journal
- **Published**: April 2025
- **Authors**: Zhaojie Yang, Yunye Li, Yong Liang Guan +1
- **PDF**: https://ieeexplore.ieee.org/document/10845840
- **Abstract**: This work studies the transceiver design and convergence performance analysis for the hierarchical modulation (HM) systems with protograph-based low-density parity-check (P-LDPC) codes. Specifically, we first conceive new source-constrained (SC) coding scheme and inter-layer-cascaded (ILC) decoding scheme tailored for the HM-based transmitter and receiver, respectively. Both the proposed SC coding and ILC decoding schemes form an enhanced version of bit-interleaved-coded HM (BIC-HM) systems, namely source-constrained HM (SC-HM) systems, providing a more reliable and flexible multi-data transmission solution. Moreover, according to the SC coding principle, we conceive a novel variable-node-degree-based (VND) multiplexing scheme to further improve the performance of the proposed SC-HM systems. Additionally, based on the ILC decoding framework, we devise a novel mutual information (MI) analysis tool, namely ILC-based extrinsic-information-transfer (ILC-EXIT) algorithm, to predict the decoding thresholds of the proposed P-LDPC-coded SC-HM systems. Theoretical and simulation results demonstrate that the proposed SC-HM systems significantly outperform the existing benchmarks in terms of error performance, decoding latency, and transmission-rate adaptation.

## Design and Performance Evaluation for BILCM-ID System With Improved Stopping Criterion

- **Status**: ✅
- **Reason**: BILCM-ID 시스템의 LDPC 반복 디코딩 개선 stopping criterion(NBEP 기반); stopping criterion 기법이 NAND LDPC 디코더(C)에 이식 가능 — 무선 응용 맥락으로 Phase 3 재검토.
- **ID**: ieee:10812956
- **Type**: journal
- **Published**: April 2025
- **Authors**: Xuhui Ding, Yuchen Xu, Gaoyang Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10812956
- **Abstract**: Low-density parity-check (LDPC) codes characterize both a relatively low decoding complexity and a performance nearing the Shannon limit. The integration of channel coding with modulation, known as bit-interleaved coded modulation (BICM), is widely utilized in communication and broadcasting systems. In particular, iterative message passing processes between soft demapper and decoder have proven effective in improving the bit error rate (BER) performance in the bit-interleaved LDPC coded modulation with iterative decoding (BILCM-ID) systems. This study proposes a novel approach for representing the iterative state in the probability domain for high-order modulation within the BILCM-ID process. Additionally, our methods introduce an improved stopping criterion based on the normalized belief evolution pattern (NBEP). Simulation analyses demonstrate that, compared to conventional hard-decision methods, the proposed algorithm can reduce ineffective iteration delay by approximately 88% with negligible degradation in BER performance.

## Performance Bounds and Degree-Distribution Optimization of Finite-Length BATS Codes

- **Status**: ✅
- **Reason**: LDPC precode의 degree distribution 최적화 및 finite-length BP/ML 성능 분석 포함(E); 네트워크 특이적이나 LDPC 코드 설계 요소 이식 가능성 있어 애매→보존
- **ID**: ieee:10857390
- **Type**: journal
- **Published**: April 2025
- **Authors**: Mingyang Zhu, Shenghao Yang, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10857390
- **Abstract**: Batched sparse (BATS) codes were proposed as a reliable communication solution for networks with packet loss. In the finite-length regime, the error probability of BATS codes under belief propagation (BP) decoding has been studied in the literature and can be analyzed by recursive formulae. However, all existing analyses have not considered precoding or have treated the BATS code and the precode as two separate entities. In this paper, we analyze the word-wise error probability of finite-length BATS codes with a precode under joint decoding, including BP decoding and maximum-likelihood (ML) decoding. The joint BP decoder performs peeling decoding on a joint Tanner graph constructed from both the BATS and the precode Tanner graphs, and the joint ML decoder solves a single linear system with all linear constraints implied by the BATS code and the precode. We derive closed-form upper bounds on the error probability for both decoders. Specifically, low-density parity-check (LDPC) precodes are used for BP decoding, and any generic precode can be used for ML decoding. Even for BATS codes without a precode, the derived upper bound for BP decoding is more accurate than the approximate recursive formula, and easier to compute than the exact recursive formula. The accuracy of the two upper bounds has been verified by many simulation results. Based on the two upper bounds, we formulate an optimization problem to optimize the degree distribution of LDPC-precoded BATS codes, which improves BP performance, ML performance, or both. In our experiments, to transmit 128 packets over a line network with packet loss, the optimized LDPC-precoded BATS codes reduce the transmission overhead to less than 50% of that of standard BATS codes under comparable decoding complexity constraints.

## Higher-Order Staircase Codes

- **Status**: ❌
- **Reason**: Hamming 컴포넌트 코드 기반 higher-order staircase 코드로 LDPC 기반이 아니며 광섬유 전용, 이식 가능 LDPC 기법 없음
- **ID**: ieee:10897312
- **Type**: journal
- **Published**: April 2025
- **Authors**: Mohannad Shehadeh, Frank R. Kschischang, Alvin Y. Sukmadji +1
- **PDF**: https://ieeexplore.ieee.org/document/10897312
- **Abstract**: We generalize staircase codes and tiled diagonal zipper codes, preserving their key properties while allowing each coded symbol to be protected by arbitrarily many component codewords rather than only two. This generalization which we term “higher-order staircase codes” arises from the marriage of two distinct combinatorial objects: difference triangle sets and finite-geometric nets, which have typically been applied separately to code design. We demonstrate one possible realization of these codes, obtaining powerful, high-rate, low-error-floor, and low-complexity coding schemes based on simple iterative syndrome-domain decoding of coupled Hamming component codes. We anticipate that the proposed codes could improve performance–complexity–latency tradeoffs in high-throughput communications applications, most notably fiber-optic, in which classical staircase codes and zipper codes have been applied. We consider the construction of difference triangle sets having minimum scope and sum-of-lengths, which lead to memory-optimal realizations of higher-order staircase codes. These results also enable memory reductions for early families of convolutional codes constructed from difference triangle sets.

## Block Orthogonal Sparse Superposition Codes for L3 Communications: Low Error Rate, Low Latency, and Low Transmission Power

- **Status**: ❌
- **Reason**: BOSS codes(joint coded modulation) 논문으로 LDPC 미언급; 5G polar code 비교 대상이며 이식 가능한 LDPC 기법 없음
- **ID**: ieee:10845812
- **Type**: journal
- **Published**: April 2025
- **Authors**: Donghwa Han, Bowhyung Lee, Min Jang +3
- **PDF**: https://ieeexplore.ieee.org/document/10845812
- **Abstract**: Block Orthogonal Sparse Superposition (BOSS) codes are a promising class of joint coded modulation techniques that can closely approach the finite-blocklength capacity with low-complexity decoding at low code rates under Gaussian channels. However, in fading channels, the performance of BOSS codes degrades considerably due to varying channel fading effects on coded symbols. This paper presents a unified approach to extending BOSS codes to practical fading scenarios and introduces novel joint demodulation and decoding solutions. For fast-fading channels, we propose a minimum mean square error approximation maximum a posteriori (MMSE-A-MAP) algorithm that integrates demodulation and decoding when channel state information is available at the receiver (CSIR). Additionally, for block-fading channels without CSIR, we introduce a joint demodulation and decoding method, referred to as the non-coherent sphere decoding (NSD) algorithm. Simulation results demonstrate that BOSS codes with MMSE-A-MAP decoding outperform 5G polar codes, while the NSD algorithm achieves performance comparable to quasi-maximum likelihood decoding but with significantly reduced complexity. Both decoding methods can be implemented for parallel processing, allowing them to meet low-latency requirements. Furthermore, real-time simulations on a software-defined radio testbed validate the feasibility of using BOSS codes for low-power transmission.

## Semantic Successive Refinement: A Generative AI-Aided Semantic Communication Framework

- **Status**: ❌
- **Reason**: Semantic Communication (JSCC + Diffusion model) 기반으로 LDPC ECC 기법 없음; 소스-채널 결합/시맨틱 통신 제외 범주
- **ID**: ieee:10829825
- **Type**: journal
- **Published**: April 2025
- **Authors**: Kexin Zhang, Lixin Li, Wensheng Lin +4
- **PDF**: https://ieeexplore.ieee.org/document/10829825
- **Abstract**: Semantic Communication (SC) is an emerging technology aiming to surpass the Shannon limit. Traditional SC strategies often minimize signal distortion between the original and reconstructed data, neglecting perceptual quality, especially in low Signal-to-Noise Ratio (SNR) environments. To address this issue, we introduce a novel Generative AI Semantic Communication (GSC) system for single-user scenarios. This system leverages deep generative models to establish a new paradigm in SC. Specifically, At the transmitter end, it employs a joint source-channel coding mechanism based on the Swin Transformer for efficient semantic feature extraction and compression. At the receiver end, an advanced Diffusion Model (DM) reconstructs high-quality images from degraded signals, enhancing perceptual details. Additionally, we present a Multi-User Generative Semantic Communication (MU-GSC) system utilizing an asynchronous processing model. This model effectively manages multiple user requests and optimally utilizes system resources for parallel processing. Simulation results on public datasets demonstrate that our generative AI semantic communication systems achieve superior transmission efficiency and enhanced communication content quality across various channel conditions. Compared to CNN-based DeepJSCC, our methods improve the Peak Signal-to-Noise Ratio (PSNR) by 17.75% in Additive White Gaussian Noise (AWGN) channels and by 20.84% in Rayleigh channels.

## Talkative Power Conversion: A Tutorial

- **Status**: ❌
- **Reason**: 전력 변환 기술(TPC) 튜토리얼로 LDPC ECC와 무관하며 이식 가능한 디코더/HW/코드 설계 기법 없음
- **ID**: ieee:11060655
- **Type**: journal
- **Published**: April 2025
- **Authors**: Peter Adam Hoeher, Yang Leng, Rongwu Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/11060655
- **Abstract**: This article provides a systematic overview of the basics of talkative power conversion (TPC). TPC is an emerging technique for simultaneous information and power transmission, in which data modulation is integrated into a switched-mode power converter. The data sequence is embedded in the ripple voltage, which is superimposing the output voltage of the converter. In contrast to conventional power line communication (PLC), TPC can be used universally, not only in grid applications. Aspects of power electronics (PE) and digital communication are presented in a structured form, including new perspectives such as multiple-input multiple-output (MIMO) techniques applied to TPC, adaptive modulation and channel coding, and advanced receiver design with adaptive channel and load estimation. The new aspects aim to mitigate the inherent shortcomings of TPC.

## Toward Universal Belief Propagation Decoding for Short Binary Block Codes

- **Status**: ✅
- **Reason**: 단거리 블록 코드용 BP 디코딩 개선(sparse PCM 추출, 4-사이클 제거)으로 LDPC 디코더·사이클 제거 기법이 NAND LDPC에 이식 가능 (C/E)
- **ID**: ieee:10887536
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yifei Shen, Zongyao Li, Yuqing Ren +5
- **PDF**: https://ieeexplore.ieee.org/document/10887536
- **Abstract**: Belief propagation (BP) decoding has been recognized for its capacity-approaching performance and high throughput when decoding long low-density parity-check (LDPC) codes. However, the application of BP decoding for short codes is hindered by dense parity-check matrices (PCMs) and prevalent short cycles in the Tanner graph. In this paper, we introduce a general method to extract an optimized sparse PCM for short binary block codes, which removes length-four cycles and enhances the connectivity of short cycles to enable BP decoding with improved performance. Notably, for short binary codes with lengths up to 64, our BP decoding performance approaches the maximum likelihood bound and surpasses the best-reported BP results with reduced computational complexity. Compared with other universal decoding algorithms, BP decoding using our extracted sparse PCMs is competitive in terms of both error-rate performance and computational complexity. These promising results suggest that our method to improve BP decoding for short codes is a step toward a practical universal BP decoder for next-generation communication systems.

## Learning Rate-Compatible Linear Block Codes: An Auto-Encoder Based Approach

- **Status**: ✅
- **Reason**: AE 기반 rate-compatible 선형 블록 코드 설계(다중 puncturing 패턴·AI 디코더); rate-compatible 코드 설계 및 신경망 디코더 기법이 NAND LDPC(C/E)에 이식 가능 — 애매하여 Phase 3 재검토.
- **ID**: ieee:10786312
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yukun Cheng, Wei Chen, Tianwei Hou +2
- **PDF**: https://ieeexplore.ieee.org/document/10786312
- **Abstract**: Artificial intelligence (AI) provides an alternative way to design channel coding with affordable complexity. However, most existing studies can only learn codes for a given size and rate, typically defined by a fixed network architecture and a set of parameters. The support of multiple code rates is essential for conserving bandwidth under varying channel conditions while it is costly to store multiple AI models or parameter sets. In this article, we propose an auto-encoder (AE) based rate-compatible linear block codes (RC-LBCs). The coding process associated with AI or non-AI decoders and multiple puncturing patterns is optimized in a data-driven manner. The superior performance of the proposed AI-based RC-LBC is demonstrated through our numerical experiments.

## Neural Network Aided FTN Transmission Over Doubly Selective Fading Channels: Waveform Learning, Channel Estimation and Data Detection

- **Status**: ❌
- **Reason**: FTN 신호와 이중 선택적 페이딩 채널 대응 NN 기반 파형·검출기 설계 논문; LDPC 언급 없으며 NAND ECC에 이식할 기법 없음.
- **ID**: ieee:10815067
- **Type**: journal
- **Published**: April 2025
- **Authors**: Chengxiang Liu, Guanghui Liu, Fuchen Xu +3
- **PDF**: https://ieeexplore.ieee.org/document/10815067
- **Abstract**: In this paper, we address the key challenges of faster-than-Nyquist signaling (FTNS) in doubly selective fading channels (DSCs) by proposing an end-to-end architecture that jointly optimizes FTN waveform, data detector, and channel estimator. Unlike traditional model-driven approaches, our solution introduces a data-driven optimization strategy, enhancing its ability to optimize parameters on a larger scale. In the proposed architecture, constellation geometry, precoder, and pilot sequences are considered as optimizable variables. Specifically, with the goal of maximizing spectral efficiency (SE), the constellation geometry and precoder are co-trained with a neural network (NN)-based data detector, showing superior performance in mitigating inter-symbol interference (ISI) caused by FTNS and channel spreading. Concurrently, the pilot sequences are optimized alongside the channel estimator to improve the estimation accuracy of CIR at pilot blocks. To track rapidly time-varying CIRs, we apply an attention mechanism to the channel estimator that efficiently leverages the channel's temporal correlation through dynamically assigning weights to the pilot blocks to accurately predict the CIRs for each data block. Simulation results show that our scheme achieves a signal to noise ratio gain of more than 6 dB under a maximum Doppler shift of 10 kHz compared with the state-of-the-art linear pre-equalized FTN system with 64-ary quadrature amplitude modulation.

## Off-Grid Channel Estimation for Orthogonal Delay-Doppler Division Multiplexing Using Grid Refinement and Adjustment

- **Status**: ❌
- **Reason**: ODDM 무선 채널 추정(sparse Bayesian inference) 논문; LDPC 미언급, 무선 채널 추정 특이적으로 이식 가능한 ECC 기법 없음
- **ID**: ieee:10857972
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yaru Shan, Akram Shafie, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/10857972
- **Abstract**: Orthogonal delay-Doppler (DD) division multiplexing (ODDM) has been recently proposed as a promising multicarrier modulation scheme to tackle Doppler spread in high-mobility environments. Accurate channel estimation is of paramount importance to guarantee reliable communication for the ODDM, especially when the delays and Dopplers of the propagation paths are off-grid. In this paper, we propose a novel grid refinement and adjustment-based sparse Bayesian inference (GRASBI) scheme for DD domain channel estimation. The GRASBI involves first formulating the channel estimation problem as a sparse signal recovery through the introduction of a virtual DD grid. Then, an iterative process is proposed that involves (i) sparse Bayesian learning to estimate the channel parameters and (ii) a novel grid refinement and adjustment process to adjust the virtual grid points. The grid adjustment in GRASBI relies on the maximum likelihood principle to attain the adjustment and utilizes refined grids that have much higher resolution than the virtual grid. Moreover, a low-complexity grid refinement and adjustment-based channel estimation scheme is proposed, that can provides a good tradeoff between the estimation accuracy and the complexity. Finally, numerical results are provided to demonstrate the accuracy, the convergence, and the efficiency of the proposed channel estimation schemes.

## Random Spreading With Higher Order Modulation in Unsourced Random Access

- **Status**: ❌
- **Reason**: 무선 대규모 접속(URA) 전용 random spreading 기법으로 LDPC ECC와 무관하며 이식 가능 기법 없음
- **ID**: ieee:10897967
- **Type**: journal
- **Published**: April 2025
- **Authors**: Jian Dang, Zaichen Zhang, Yongpeng Wu
- **PDF**: https://ieeexplore.ieee.org/document/10897967
- **Abstract**: Unsourced random access (URA) is crucial for future massive access scenarios. Existing URA schemes often use low-order modulation and assess performance with a limited number of active users. This work presents a pilot-free URA scheme that employs random spreading and higher-order modulation. We derive a discrete mixture generalized approximate message passing algorithm to enhance active user detection (AUD) and data detection. Simulations show that our proposed method significantly outperforms pilot-based methods in AUD, and higher-order modulation supports a large number of active users while ensuring the target per user probability of error (PUPE) performance.

## Nonlinearity Tolerance of Hierarchical Distribution Matching in Optical Fiber Communication

- **Status**: ❌
- **Reason**: 광섬유 전송용 확률적 진폭 성형(PAS) 분포 매칭 기법으로 LDPC ECC와 무관
- **ID**: ieee:10904087
- **Type**: journal
- **Published**: April 2025
- **Authors**: Mamoru Komatsu, Akira Naka
- **PDF**: https://ieeexplore.ieee.org/document/10904087
- **Abstract**: This letter reports the nonlinearity tolerance properties of hier-archical distribution matching (HiDM), which is a distribution matcher of reasonable complexity for probabilistic amplitude shaping (PAS) in non-linear fiber-optic transmission. Recent studies have demonstrated that PAS exhibits unique nonlinearity tolerance, which varies depending on channel conditions. This tolerance is influenced by the choice of distribution matcher, as analyzed using statistical moments. In this work, we explore the nonlinearity tolerance of HiDM through moment-based analysis and numerical simulations. The results show that the dependence on blocklength in nonlinearity tolerance of HiDM is significantly smaller than in one of enumerative sphere shaping, a common DM. In addition, the property in HiDM is almost independent on the number of layers.

## Joint Inter-Symbol Interference and I/Q Imbalance Cancellation in FTN Systems

- **Status**: ❌
- **Reason**: FTN 시스템 ISI/IQI 제거 알고리즘으로 LDPC 미언급; 무선 수신기 특이적으로 이식 가능한 ECC 기법 없음
- **ID**: ieee:10832532
- **Type**: journal
- **Published**: April 2025
- **Authors**: Mingfei Tong, Xiaojing Huang, J. Andrew Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10832532
- **Abstract**: Current research on faster-than-Nyquist (FTN) systems mainly focuses on baseband digital signal processing without considering the impact of I/Q imbalance (IQI) caused by hardware impairments in the signal chain. To address this problem, this paper considers frequency-dependent IQI and applies the frame-based decision-directed successive interference cancellation (DDSIC) algorithm after minimum mean square error (MMSE) equalization to jointly mitigate inter-symbol interference (ISI) and IQI. We introduce extended-dimension signal models, which use both original and image signals to describe the impact of IQI. Based on the models, a two-stage iterative DDSIC algorithm is then proposed, achieving effective interference cancellation. Furthermore, the theoretical bit error rate (BER) for each iteration of DDSIC and the BER lower bound of the proposed system are derived. Simulation results demonstrate the superiority of DDSIC over some existing algorithms under both additive white Gaussian noise (AWGN) and multipath fading channels. These results also validate the derived theoretical BER expressions and the robustness of our scheme under various ISI and IQI scenarios, respectively.

## Max-Sum-Based Data Associations for Tracking Point and Extended Targets

- **Status**: ❌
- **Reason**: 다중표적 추적을 위한 factor graph max-sum 알고리즘 논문으로, LDPC 디코딩과 무관하며 이식 가능한 ECC 기법 없음.
- **ID**: ieee:10720889
- **Type**: journal
- **Published**: April 2025
- **Authors**: Weizhen Ma, Zhongliang Jing, Peng Dong +1
- **PDF**: https://ieeexplore.ieee.org/document/10720889
- **Abstract**: For multitarget tracking applications, data association is a fundamental problem of assigning measurements to their corresponding targets. In this article, we propose two algorithms for tracking point and extended targets, respectively, based on factor graph representations of the joint probability density functions. Both employ the max-sum (MS) algorithm to find the maximum a posteriori assignment such that the state of each target is updated with the most probable measurement(s). We model the single target densities as Gaussian distribution for point targets and gamma Gaussian inverse Wishart distribution for extended targets. Under linear Gaussian assumptions on the target models, the proposed algorithms provide analytical solutions to multitarget tracking problems. Specifically, the messages flowed in the factor graphs, existence probabilities and states of the targets are analytically calculated. These two algorithms have reduced computational load compared to the particle-based sum-product (SP) algorithms and avoid gating or clustering used by traditional multitarget tracking methods. We compare the proposed MS-based algorithms (MSAs) with the Poisson multi-Bernoulli mixture filters and the SP-based algorithms, and simulation results show that the MSAs have comparable or improved tracking performance.

## Ferroelectric FET-Based Bayesian Inference Engine for Disease Diagnosis

- **Status**: ❌
- **Reason**: FeFET 기반 Bayesian inference 엔진으로 LDPC/ECC와 무관하며 이식 가능한 디코더·HW·코드설계 기법 없음
- **ID**: ieee:10874890
- **Type**: journal
- **Published**: April 2025
- **Authors**: Arka Chakraborty, Musaib Rafiq, Yawar Hayat Zarkob +2
- **PDF**: https://ieeexplore.ieee.org/document/10874890
- **Abstract**: Probabilistic/stochastic computations form the backbone of autonomous systems and classifiers. Recently, biomedical applications of probabilistic computing such as Bayesian networks for disease diagnosis, DNA sequencing, etc. have attracted significant attention owing to their high energy-efficiency. Bayesian inference is widely used for decision making based on independent (often conflicting) sources of information/evidence. A cascaded chain or tree structure of asynchronous circuit elements known as Muller C-elements can effectively implement Bayesian inference. Such circuits utilize stochastic bit streams to encode input probabilities which enhances their robustness and fault-tolerance. However, the CMOS implementations of Muller C-element are bulky and energy hungry which restricts their widespread application in resource constrained IoT and mobile devices such as UAVs, robots, space rovers, etc. In this work, for the first time, we propose a compact and energy-efficient implementation of Muller C-element utilizing a single Ferroelectric FET and use it for cancer diagnosis task by performing Bayesian inference with high accuracy on Wisconsin data set. The proposed implementation exploits the unique drain-erase, program inhibit and drain-erase inhibit characteristics of FeFETs to yield the output as the polarization-state of the ferroelectric layer. Our extensive investigation utilizing an in-house developed experimentally calibrated compact model of FeFET reveals that the proposed C-element consumes (worst-case) energy of 4.1 fJ and an area  $0.07~\mu m^{2}$  and outperforms the prior implementations in terms of energy-efficiency and footprint while exhibiting a comparable delay. We also propose a novel read circuitry for realising a Bayesian inference engine by cascading a network of proposed FeFET-based C-elements for practical applications. Furthermore, for the first time, we analyze the impact of cross-correlation between the stochastic input bit streams on the accuracy of the C-element based Bayesian inference implementation.

## Probabilistic Shaped Multilevel Polar Coding for Wiretap Channel

- **Status**: ❌
- **Reason**: Multilevel polar coding + probabilistic shaping for wiretap channel; LDPC 미언급, 물리계층 보안 특이적으로 이식 가능한 ECC 기법 없음
- **ID**: ieee:10858640
- **Type**: journal
- **Published**: April 2025
- **Authors**: Li Shen, Yongpeng Wu, Peihong Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/10858640
- **Abstract**: A wiretap channel is served as the fundamental model of physical layer security techniques, where the secrecy capacity of the Gaussian wiretap channel is proven to be achieved by Gaussian input. However, there remains a gap between the Gaussian secrecy capacity and the secrecy rate with conventional uniformly distributed discrete constellation input, e.g. amplitude shift keying (ASK) and quadrature amplitude modulation (QAM). In this paper, we propose a probabilistic shaped multilevel polar coding scheme to bridge the gap. Specifically, the input distribution optimization problem for maximizing the secrecy rate with ASK/QAM input is solved. Numerical results show that the resulting sub-optimal solution can still approach the Gaussian secrecy capacity. Then, we investigate the polarization of multilevel polar codes for the asymmetric discrete memoryless wiretap channel, and thus propose a multilevel polar coding scheme integration with probabilistic shaping. It is proved that the scheme can achieve the secrecy capacity of the Gaussian wiretap channel with discrete constellation input, and satisfies the reliability condition and weak security condition. A security-oriented polar code construction method to natively satisfies the leakage-based security condition is also investigated. Simulation results show that the proposed scheme achieves more efficient and secure transmission than the uniform constellation input case over both the Gaussian wiretap channel and the Rayleigh fading wiretap channel.

## Design of a Dual-Level Polar-Coded Scheme for GCI-DCSK Systems

- **Status**: ❌
- **Reason**: 무선 GCI-DCSK 시스템 전용 polar-coded 기법이며 LDPC는 비교 베이스라인으로만 언급, 이식 가능한 ECC 기법 없음
- **ID**: ieee:10896681
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yu Zhou, Liang Lv, Dingfei Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/10896681
- **Abstract**: In this letter, we present a polar-coded scheme tailored to enhance transmission reliability in generalized carrier index differential chaos shift keying (GCI-DCSK) systems. Considering the reliability difference between the index and modulated layers in GCI-DCSK, we develop a dual-level polar-coded modulation (DLC-PCM) scheme that provides unequal error protection (UEP). Furthermore, to better manage the reliability differences among index bits in the GCI-DCSK system, we propose a dual-level bit-interleaved polar-coded modulation (DLC-BIPCM) scheme by incorporating a bit-interleaved coded modulation (BICM) structure within the index layer. Additionally, we derive log-likelihood ratio (LLR) expressions and calculate the capacities of both the index and modulated layers to strategically guide the design of the DLC-PCM scheme. Simulation results demonstrate that our proposed polar-coded approach achieves superior bit error rate (BER) performance and lower complexity compared to existing low-density parity-check (LDPC)-based schemes.

## GT3: An Open-Source 3-nm GAAFET PDK and Platform for End-to-End Evaluation of Emerging Technologies

- **Status**: ❌
- **Reason**: 3nm GAAFET PDK 및 인터커넥트 평가 플랫폼 논문으로 LDPC는 벤치마크 설계로만 사용, 이식 가능한 LDPC 기법 없음
- **ID**: ieee:10906664
- **Type**: journal
- **Published**: April 2025
- **Authors**: Da Eun Shim, Piyush Kumar, Akshata Ashok Kini +3
- **PDF**: https://ieeexplore.ieee.org/document/10906664
- **Abstract**: In this article, we present a comprehensive end-to-end evaluation platform for various front-end-of-line (FEOL) and back-end-of-line (BEOL) technology options at the 3-nm technology node. Based on TCAD modeling of FE and BE, we have developed a 3-nm GAAFET-based process design kit (PDK). We have developed a 6-track standard cell library including 65 cells with a library height of 144 nm. Based on TCAD modeling of interconnects, we have evaluated the resistance of the entire BEOL stack using ruthenium for lower metal levels (M0–M3) and copper for higher metal levels (M4–M13). Based on place and route (PnR) studies using our PDK, we have analyzed the impact of high aspect ratio (AR) Ru interconnects at M2 and M3 in terms of performance using benchmark designs. Our results show that using Ru interconnects improves the circuit performance by up to 10.4% compared with Cu interconnects and that increasing the AR generally results in performance degradation due to the increase in capacitance and via resistances. We have observed a 5.9% and 4% degradation in performance for AES and LDPC, respectively, when moving from AR2 to AR6 local interconnects. However, adding an airgap can improve the higher AR Ru interconnect cases and AR4 with airgap case shows the most performance improvement with an overall 19.7% improvement compared with Cu. This case study also serves as an example that shows the importance of an end-to-end evaluation platform.

## Guest Editorial: Special Issue on Next Generation Advanced Transceiver Technologies—Part II

- **Status**: ❌
- **Reason**: 초록 없는 Guest Editorial로 평가 불가, 선별 대상 외
- **ID**: ieee:10931169
- **Type**: journal
- **Published**: April 2025
- **Authors**: Yunlong Cai, A. Lee Swindlehurst, Aylin Yener +4
- **PDF**: https://ieeexplore.ieee.org/document/10931169
- **Abstract**: N/A

## Study on the Effect of Bit Error Rate on the Performance of Digital Communication System

- **Status**: ❌
- **Reason**: 디지털 통신 BER 일반론 서술로 LDPC 미언급, 이식 가능한 ECC 기법 없음
- **ID**: ieee:10971301
- **Type**: conference
- **Published**: 9-9 April 
- **Authors**: Zhou Wei, Cheng Haodong
- **PDF**: https://ieeexplore.ieee.org/document/10971301
- **Abstract**: Bit error rate is an important index to evaluate the performance of digital communication system. In this paper, the effects of bit error rate on signal transmission and reception performance are studied, and the main factors are understood by analyzing the operating environment and signal processing methods. This paper also provides a solution to effectively reduce the bit error rate, and discusses the change law of the bit error rate in different scenarios.

## Optimum Power-Subcarrier Allocation and Time-Sharing in Multicarrier NOMA Uplink

- **Status**: ❌
- **Reason**: MC-NOMA 업링크 전력·부반송파 할당 최적화 논문으로, LDPC 관련 내용 없음
- **ID**: ieee:10888922
- **Type**: conference
- **Published**: 6-11 April
- **Authors**: Sagnik Bhattacharya, Kamyar Rajabalifardi, Muhammad Ahmed Mohsin +1
- **PDF**: https://ieeexplore.ieee.org/document/10888922
- **Abstract**: Currently used resource allocation methods for uplink multicarrier non-orthogonal multiple access (MC-NOMA) systems have multiple shortcomings. Current approaches either allocate the same power across all subcarriers to a user, or use heuristic-based near-far, strong channel-weak channel user grouping to assign the decoding order for successive interference cancellation (SIC). This paper proposes a novel optimal power-subcarrier allocation for uplink MC-NOMA. This new allocation achieves the optimal power-subcarrier allocation as well as the optimal SIC decoding order. Furthermore, the proposed method includes a time-sharing algorithm that dynamically alters the decoding orders of the participating users to achieve the required data rates, even in cases where any single decoding order fails to do so. Extensive experimental evaluations show that the new method achieves higher sum data rates and lower power consumption compared to current NOMA methods.

## Reinforcing 6G Network Security by Combining Aes and Polar Codes at the Physical Layer

- **Status**: ❌
- **Reason**: AES+polar code 기반 6G 물리계층 보안 — polar code 보안 응용, LDPC 아니며 이식 가능 디코더·코드설계 없음
- **ID**: ieee:11064175
- **Type**: conference
- **Published**: 4-6 April 
- **Authors**: Ravi Shankar, M.P. Mishra
- **PDF**: https://ieeexplore.ieee.org/document/11064175
- **Abstract**: This paper presents the deployment of Advanced Encryption Standard (AES) and polar channel coding in 6 G wireless communication networks for Physical Layer Security (PLS). In reality, we call for attention to this growing demand for enhanced security in 6 G networks as applications such as autonomous cyber-physical systems, ultra-reliable low-latency communications (URLLC), and massive machine-type communications (mMTC) begin to surface. Polar codes are widely used in 5G and are expected to be very important in 6G. This paper evaluates the ability of polar codes to achieve capacity and their flexibility in wiretap channels. Polar codes offer a strong foundation for protecting the physical layer from prying eyes and other security risks when combined with AES. Besides this analysis of potential benefits these security mechanisms offer toward improving data confidentiality and integrity in future networks, the work outlines some technical problems associated with practical implementation in real-world 6 G systems. This paper articulates design considerations through a comprehensive analysis of the integration of AES with polar coding to meet the stringent security and performance criteria of 6 G communications.

## Performance Analysis of LDPC Codes and Polar Codes

- **Status**: ❌
- **Reason**: LDPC vs Polar AWGN 성능 비교 분석뿐 — 새로운 디코더·HW·코드설계 기법 없는 단순 비교
- **ID**: ieee:11012493
- **Type**: conference
- **Published**: 4-5 April 
- **Authors**: Kavitha. K, Archana. N, Hinduja. R +1
- **PDF**: https://ieeexplore.ieee.org/document/11012493
- **Abstract**: Error correction codes such as Polar codes and LDPC codes plays a major part in reliable data transmission over noise channels. Polar codes work on the principle of channel polarization while it is iterative belief propagation for LDPC codes. This study mainly focuses on the performance analysis of polar codes and LDPC codes in Additive White Gaussian Noise channel by comparing different parameters including bit error rate, code rate, and throughput. Polar codes use Successive Cancellation List decoding. It performs well at high SNR and allows multiple decoding paths hence increases complexity. LDPC requires multiple iterations but is highly effective in correcting errors, making it preferable for noisy channels. Polar codes are suitable for high SNR applications and LDPC are suitable for low SNR applications.

## OFDM For Underwater Acoustic Communication Using FPGA

- **Status**: ❌
- **Reason**: 수중 음향 OFDM에 폴라코드 적용; LDPC는 비교 베이스라인 언급뿐, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:11012521
- **Type**: conference
- **Published**: 4-5 April 
- **Authors**: D. Malathi, R. S. Prakalya, T. Rithuvarshini +2
- **PDF**: https://ieeexplore.ieee.org/document/11012521
- **Abstract**: Underwater wireless communication is of prime importance in ocean research, environmental monitoring, and deep-sea exploration. However, it is greatly affected by signal loss, limited bandwidth, and multipath interference, which complicates reliable data transfer. There has been recent interest in a promising solution that is less susceptible to multipath fading and can accommodate higher data rates. To achieve effective performance underwater, one needs robust error correction. In this project, we have fixed our focus on polar coded Orthogonal frequency division multiplexing OFDM - a system tailored toward underwater communication - incorporating Polar Codes with OFDM. Introduced by Erdal Arıkan, Polar Codes are known for their ability to achieve near-capacity performance and efficiency in encoding and decoding processes. A Polar Coded OFDM system to construct and analyze with the objective of improving the communication reliability and efficiency under different conditions of underwater environments. We have designed a simulation environment by emulating all the underwater communication challenges, including signal attenuation, noise, Doppler shifts, and multipath effects, and our system will evaluate all aspects of the designed system along with bit error rate, data rate, and power efficiency. Our results will be compared to those of conventional uncoded OFDM systems as well as other error-correcting techniques such as Turbo and low density parity check LDPC codes. Ultimately, we hope to produce a communication system that operates with greater reliability and efficiency in the challenging oceanic environment.

## Practical MU-MIMO Detection and LDPC Decoding Through Digital Annealing

- **Status**: ✅
- **Reason**: 디지털 어닐링 기반 LDPC 디코딩에 새 비용함수 도입으로 정확도·복잡도 개선 — 이식 가능한 디코더 알고리즘(C)
- **ID**: ieee:10992822
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Po-Shao Chen, Wei Tang, Zhengya Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10992822
- **Abstract**: Digital annealing has been successfully applied to solving combinatorial optimization (CO) problems. It is more flexible, robust, and easier to deploy on edge platforms compared to its counterparts including quantum annealing and analog and in-memory Ising machines. In this work, we apply digital annealing to compute-intensive communication digital signal processing problems, including multi-user detection in multiple-input and multiple-output (MU-MIMO) wireless communication systems and decoding low-density parity-check (LDPC) codes. We show that digital annealing can achieve near maximum likelihood (ML) accuracy for MIMO detection with even lower complexity than the conventional minimum mean square error (MMSE) detection. In LDPC decoding, we enhance digital annealing by introducing a new cost function that improves decoding accuracy and reduces computational complexity compared to the standard formulations.

## DHD: Double Hard Decision Decoding Scheme for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시 직접; 이중 하드결정+LLR 개선+RRV 조정 디코딩 기법(A)
- **ID**: ieee:10993263
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Lanlan Cui, Yichuan Wang, Renzhi Xiao +3
- **PDF**: https://ieeexplore.ieee.org/document/10993263
- **Abstract**: With the advancement of NAND flash technology, the increased storage density leads to intensified interference, which in turn raises the error rate during data retrieval. To ensure data reliability, low-density parity-check (LDPC) codes are extensively employed for error correction in NAND flash memory. Although LDPC soft decision decoding offers high error correction capability, it comes with a significant latency. Conversely, hard-decision decoding, although faster, lacks sufficient error correction strength. Consequently, flash memory typically initiates with hard-decision decoding and resorts to multiple soft decision decoding upon failure. To minimize decoding latency, this paper proposes a decoding mechanism based on the double hard decision, called DHD. This DHD scheme improves the Log-Likelihood Ratio (LLR) in the hard decision process. After the first hard decision fails, the read reference voltage (RRV) is adjusted to perform the second hard decision decoding. If the second hard decision also fails, soft decision decoding is then employed. Experimental results demonstrate that when the Raw Bit Error Rate (RBER) is $8.5 \times 10^{-3}$, DHD reduces the Frame Error Rate (FER) by 86.4% compared to the traditional method.

## PRISM: Malta’s quantum key distribution test-bed network

- **Status**: ❌
- **Reason**: QKD 네트워크 배포 사례; LDPC/디코더 기법 없음
- **ID**: ieee:11000210
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Noel Farrugia, Eleanor Scerri, Nicholas Frendo +5
- **PDF**: https://ieeexplore.ieee.org/document/11000210
- **Abstract**: In this publication we summarise our journey when deploying Malta's first Quantum Key Distribution (QKD) network. The challenges faced in this project and the means used to overcome them are discussed, paving the way for smoother deployments in the future. We also summarise the tools we have built along the way that were essential to manage and monitor such a network, along with the work we have been doing in standardisation bodies and research on the topic.

## A novel slice error correction reconciliation for continuous-variable quantum key distribution

- **Status**: ❌
- **Reason**: CV-QKD 슬라이스 오류정정 reconciliation; 소스 양자화 전처리로 채널 ECC 기법 아님
- **ID**: ieee:11000179
- **Type**: conference
- **Published**: 31 March-2
- **Authors**: Lin Zhu, Xue-Qin Jiang, Han Hai +3
- **PDF**: https://ieeexplore.ieee.org/document/11000179
- **Abstract**: Information reconciliation is a crucial process in continuous-variable quantum key distribution(CV-QKD) systems. The slice error correction (SEC) reconciliation is appropriate for short-distance CV-QKD. However, the efficiency of SEC reconciliation schemes is significantly influenced by noisy channels with low signal-to-noise ratios (SNRs). In this paper, we present an enhanced information reconciliation scheme, termed AC-SEC reconciliation, which adds the new Gaussian sequences c with the original Gaussian sequences y before quantization in the SEC reconciliation to obtain secret key sequences with high variance and reduce noise interferences. Simulation results demonstrate that compared with the traditional SEC reconciliation, the proposed information reconciliation has lower frame error rate (FER) and higher reconciliation efficiency, which can increase the secret key rate (SKR).

## Xgboost Based Regression Forecast for ACM on Q/V-band Satellite Links

- **Status**: ❌
- **Reason**: 위성 링크 ACM SNR 예측(XGBoost); LDPC/ECC 디코더 기법 없음
- **ID**: ieee:11000083
- **Type**: conference
- **Published**: 30 March-4
- **Authors**: Mirela Fetescu, Johannes Ebert, Karin Plimon +4
- **PDF**: https://ieeexplore.ieee.org/document/11000083
- **Abstract**: This paper presents a comparison between classical adaptive coding and modulation (ACM) with fixed modulation and coding (ModCod) margins and two machine learning (ML)-based approaches: univariate and multivariate forecasting models. Both ML approaches are based on variants of Extreme Gradient Boosting (XGBoost) to predict signal-tonoise ratio (SNR) time series, aiding ACM switching decisions. The evaluation of the ACM algorithms is conducted using two years of Q/V-band channel data recorded at the ground station in Graz, Austria, using the Alphasat TDP5 Aldo Paraboni Q/Vband payload. The results demonstrate that the multivariate forecasting model outperforms both the classical ACM algorithm and the univariate forecasting model in terms of spectral efficiency. Additionally, the multivariate model eliminates the need for direct SNR estimation by using easily measurable parameters from the modem.

## An Experimental Analysis of 50G-PON LDPC

- **Status**: ✅
- **Reason**: 50G-PON에서 LDPC 디코딩 파라미터(soft/hard 입력, 반복횟수) 실험 분석 — 이식 가능 디코더 파라미터 통찰(B/C, 애매하여 살림)
- **ID**: ieee:11046425
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: L. Anet Neto, D. Chevalier, G. Simon +5
- **PDF**: https://ieeexplore.ieee.org/document/11046425
- **Abstract**: We experimentally assess the impacts of different LDPC decoding parameters with both soft- and hard-inputs in 50G-PON. We also derive the mean number of decoder iterations per received optical power over 25 km SSMF.

## Integrated high-performance LDPC decoder for Continuous-Variable Quantum Key Distribution System

- **Status**: ✅
- **Reason**: Integrated high-throughput LDPC decoder (Gbps) HW implementation for CV-QKD; decoder HW architecture potentially portable (D), keep for Phase 3 even though QKD app.
- **ID**: ieee:11046950
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Chuang Zhou, Yang Li, Li Ma +4
- **PDF**: https://ieeexplore.ieee.org/document/11046950
- **Abstract**: The throughput of the error correction decoding is one of the major bottlenecks of highspeed continuous-variable quantum key distribution (CV-QKD) systems and an integrated decoder with Gbps decoding throughput is implemented in this work. © 2024 The Authors OCIS codes: (270.5585) Quantum information and processing

## 480 Gbit/s and 240 Gbit/s Single-Carrier Super-Rated Upstream Burst-Mode Coherent PON Utilizing Off-the-Shelf Coherent Receiver

- **Status**: ❌
- **Reason**: Coherent PON upstream burst-mode demonstration; no LDPC/decoder/HW/code-design technique to extract.
- **ID**: ieee:11046587
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Kovendhan Vijayan, Robert Borkowski, Qian Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/11046587
- **Abstract**: We demonstrate 480 Gbits/s (400 G -PON) and 240 Gbits/s (200 G -PON) upstream burstmode coherent PON operation over 29 dB and 41 dB path loss, respectively with SOA boosters acting as shutter and pre-levelers, using off-the-shelf coherent receiver.

## A Novel PS-QAM Signaling with Iterative Decoding for Higher Spectral Efficiencies

- **Status**: ❌
- **Reason**: PS-QAM probabilistic shaping with iterative decoding for spectral efficiency; wireless/optical-specific, no extractable LDPC ECC technique.
- **ID**: ieee:11046653
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Hussam G. Batshon, Gregory Raybon, Di Che +1
- **PDF**: https://ieeexplore.ieee.org/document/11046653
- **Abstract**: We propose a novel multidimensional probabilistically shaped coded modulation scheme with iterative decoding, achieving up to 0.9 dB SNR improvement over PS-QAM across 4 to $10 \mathrm{bits} / \mathrm{s} / \mathrm{Hz}$. Experimental results confirm the performance of the proposed approach. © 2024 The Author(s)

## Nonlinearity Cancellation Based on Optimized First Order Perturbative Kernels

- **Status**: ❌
- **Reason**: Nonlinearity cancellation via perturbative kernels; optical impairment compensation, no ECC technique.
- **ID**: ieee:11046977
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Alex Alvarado, Astrid Barreiro, Gabriele Liga
- **PDF**: https://ieeexplore.ieee.org/document/11046977
- **Abstract**: The potential offered by interference cancellation based on optimized regular perturbation kernels of the Manakov equation is studied. Theoretical gains of up to 2.5 dB in effective SNR are demonstrated.

## 1.5 Terabit/s IM/DD Transmission with Kerr Soliton Frequency Comb for DCI Application

- **Status**: ❌
- **Reason**: IM/DD Kerr soliton comb transmission demo; pure optical transport, no ECC technique.
- **ID**: ieee:11047174
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Lakshmi Narayanan Venkatasubramani, Ahmed Galib Reza, Cagri Ozdilek +4
- **PDF**: https://ieeexplore.ieee.org/document/11047174
- **Abstract**: We experimentally demonstrate 1.575 Terabit/s aggregated transmission rate with $75 \mathrm{~Gb} / \mathrm{s} / \lambda$ on-off keying signal employing a dissipative Kerr soliton optical frequency comb. The system is scalable to provide multi-Terabit/s optical interconnects.

## Core-level Routing in Long-haul MCF Transmission System with FIFO-less Multicore EDFA and Spatial Cross-connect

- **Status**: ❌
- **Reason**: Multicore fiber transmission/core-level routing demo; pure optical transport, no ECC technique.
- **ID**: ieee:11046939
- **Type**: conference
- **Published**: 30 March-3
- **Authors**: Kosuke Komatsu, Shohei Beppu, Daiki Soma +4
- **PDF**: https://ieeexplore.ieee.org/document/11046939
- **Abstract**: Core-level routing in a long-haul multicore fiber transmission system is experimentally demonstrated. Full C-band signals are transmitted over 1685-km 4-core fibers using fan-in/fan-out-less multicore fiber amplifiers and a spatial channel cross-connect for the first time. © 2025 The Author(s)

## A comprehensive Study of Decoding Algorithms for Low Density Parity-Check(LDPC)

- **Status**: ✅
- **Reason**: LDPC 디코딩 알고리즘(BP·Min-Sum 변형) 종합 분석 + HW 친화 알고리즘 다룸, 이식 가능 디코더 기법(C/D)
- **ID**: ieee:11035238
- **Type**: conference
- **Published**: 28-29 Apri
- **Authors**: C S Anil Kumar, M Vedhashri, L Vanditha +2
- **PDF**: https://ieeexplore.ieee.org/document/11035238
- **Abstract**: The near-capacity performance and effective decoding algorithms of Low-Density Parity-Check (LDPC) codes have made them a mainstay of contemporary error correction. With an emphasis on iterative techniques like the Belief Propagation (BP) algorithm, the Min-Sum algorithm, and their variations, this paper offers a thorough analysis of decoding algorithms for LDPC codes. We investigate the trade-offs between various algorithmic techniques’ computational complexity, decoding latency, and error correction performance. Particular focus is placed on new methods and hardware-friendly algorithms that are tailored for next-generation communication systems, such 5 G and beyond.

## Hardware Acceleration of LDPC Encoding Based on CGRA

- **Status**: ✅
- **Reason**: CGRA 기반 LDPC 인코딩 HW 가속(메모리 구조·데이터플로우 최적화) — HW 아키텍처 이식 가능(D)
- **ID**: ieee:11103139
- **Type**: conference
- **Published**: 25-27 Apri
- **Authors**: Zitong Zhou
- **PDF**: https://ieeexplore.ieee.org/document/11103139
- **Abstract**: Low-Density Parity-Check (LDPC) codes, as a class of capacity-approaching forward error correction codes, have been adopted as the encoding strategy for 5 G New Radio data channels. With the exponential increase in data throughput requirements for 5G communications, conventional FPGA-based architectures have demonstrated notable limitations in terms of computational efficiency and scalability. This paper introduces CGRA as a hardware acceleration approach for LDPC encoding. To address the issues of low memory utilization and low computing efficiency in CGRA, we employ data preprocessing, heterogenous memory architecture, and optimized dataflow to enhance hardware acceleration performance. Experimental results based on a $5 \times 5$ Processing Element Array (PEA) demonstrate that our approaches achieve significant performance improvements, including 80 % reduction in data access latency and 43 % decrease in computational processing time compared to baseline implementations.

## Research on the Performance of Cross-Frequency Doppler-aided Beidou MEO B2b Signal Demodulation

- **Status**: ❌
- **Reason**: Beidou B2b 신호 복조 도플러 보조 기법, LDPC·ECC 무관
- **ID**: ieee:11065573
- **Type**: conference
- **Published**: 25-27 Apri
- **Authors**: Tong Liu, Dun Wang, Shuangna Zhang +6
- **PDF**: https://ieeexplore.ieee.org/document/11065573
- **Abstract**: The high message broadcast rate of the BDS-3 MEO satellite B2b signal leads to poor carrier phase tracking performance, limiting its navigation message demodulation capability. In contrast, the Beidou B1C and B2a signals incorporate pilot components free from navigation message modulation, resulting in superior tracking performance. This paper proposes a cross-frequency Doppler-aided method to improve B2b signal demodulation by leveraging pilot signals from other frequencies. After applying cross-frequency Doppler aiding, the carrier phase tracking threshold for the B2b signal is reduced, and tracking accuracy is enhanced, thereby improving demodulation performance. Simulation and field measurements demonstrate a 1 dB improvement in B2b signal demodulation performance when aided by pilot signals.

## Optimized Reliable Content Addressable Memory

- **Status**: ❌
- **Reason**: DRAM CAM 신뢰성 회로 아키텍처(2% 면적·전력) — LDPC/디코더·이식 가능한 ECC 코드설계 기법 없음
- **ID**: ieee:11013533
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Rachamadugu Sri Ranga Likhith, Ravirala Sooraj, Voona Sasikamal +1
- **PDF**: https://ieeexplore.ieee.org/document/11013533
- **Abstract**: Dynamic Random Access Memory (DRAM) scaling is becoming increasingly questionable in terms of reliability and at the same time efficient Error Control Coding (ECC) architectures are needed to solve data correctness problems without impacting system performance too severely. This paper proposes an optimized reliable Content Addressable Memory (CAM) architecture for DRAMs. The proposed architecture employs a slightly larger base circuit, resulting in a 2 % increase in area while reducing power consumption by 3.63%. Although in contrast with current systems, the proposed solution improves the reliability of DRAM and CAM without any loss of existing features.

## Performance Analysis of Channel Coding Techniques for 6G Networks

- **Status**: ❌
- **Reason**: 6G 채널코딩(Conv/LDPC/Polar/Turbo) 성능 비교 벤치마크일 뿐, 떼어낼 디코더·HW·코드설계 기법 없음 — 무선 응용 일반론
- **ID**: ieee:11013676
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Mulagala Dileep, Killi Reshmi, Kodiboina Keerthi +3
- **PDF**: https://ieeexplore.ieee.org/document/11013676
- **Abstract**: Achieving error-free communication is a significant challenge in wireless technology, forming the foundation for reliable communication systems. However, due to impairments on wireless channels, completely error-free communication is impractical. Channel coding techniques, such as Convolutional codes, LDPC codes, Polar codes and Turbo codes have been pivotal in minimizing error rates across various generations of wireless communication. With the advancement of 5G technology, there is a need for advanced channel coding techniques that prioritize low complexity, reduced Bit error rate and high efficiency. The project examines the performance of these four channel coding schemes for 6G networks. Convolutional codes, widely used in earlier generations of communications, are included as a benchmark to evaluate their suitability for 5G applications. Polar codes, designed to achieve near-Shannon limit performance, are analyzed for their structured approach and application in low-latency scenarios. Turbo codes are evaluated for their iterative decoding mechanism, known for providing reliable performance in noisy environments. LDPC codes, currently utilized in 4G systems, are tested for their efficiency in achieving low BER, reduced complexity, spectral efficiency, latency.

## Applicability of 5G-NR LDPC code for Error-reduced Free-Space Optical Communication

- **Status**: ❌
- **Reason**: FSO 무선광통신에 5G-NR QC-LDPC 적용성 분석만; offset Min-Sum은 기성기법 사용일 뿐 떼어낼 새 디코더/HW/코드설계 기여 없음
- **ID**: ieee:11048345
- **Type**: conference
- **Published**: 23-25 Apri
- **Authors**: Chandra Shekhar, Banwari Lal, A Arockia Bazil Raj
- **PDF**: https://ieeexplore.ieee.org/document/11048345
- **Abstract**: Free-space optical (FSO) communication systems are growing in popularity due to the features they offer for Civilian and Defence applications. Features like high data rates, non-licensed spectrum, and secure link makes FSO an optimum choice for many applications. This paper will analyze the applicability of the Fifth-generation new radio (5G-NR) LDPC code for optimum FSO link quality that is severely affected by atmospheric turbulence-induced fading, weather attenuation/disturbances, geometric losses, and misalignment errors. A simulation model for a typical FSO system has been created in MATLAB to model atmospheric turbulence using a Log-normal model for weak turbulence and a Gamma-gamma model for strong turbulence. The 5G-NR standard uses Quasi-cyclic (QC) LDPC code for reduced computational complexity and excellent error performance over noisy channels. In this paper, the offset-based Min-Sum decoding Algorithm has been considered to analyze the BER performance for Uncoded, Analytical, and Coded cases for FSO system implementation. The results indicate a strong case for the applicability of the 5G-NR LDPC code in building FSO systems for reliable communication.

## Analysis of Channel Codes using Machine Learning for FSO Communication System

- **Status**: ❌
- **Reason**: FSO ML 채널추정 연구; 채널 부호는 서베이 수준 언급, 이식 가능 LDPC 기법 없음
- **ID**: ieee:11115334
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Ritu Gupta, Sandeep Kaur, Lalit Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/11115334
- **Abstract**: Perfect channel estimate is not a recommended communication method since it is exceedingly difficult, costly, and time/power intensive. The goal of this work is to find a novel, low-cost, deep learning-based solution. A number of novel deep learning and traditional structure combinations are introduced, examined, and contrasted throughout all atmospheric turbulence regimes, from mild to high., The results show that deep learning is resistant to changes in air turbulence and may perform sufficiently near to the ideal channel estimation approach. The suggested deep learning-based solutions have good performance, minimal complexity, and low cost. As a result, they are advised for mobile communication systems’ channel estimate. Since customers utilize small mobile devices as transceivers, these systems should provide them with advantageous and affordable services. These devices must be inexpensive, simple, and low power users. This work aims to replace deep learning-based channel estimation with a traditional, costly, and difficult technique. A more extensive view on channel codes in various machine learning (ML)-based Free Space Optics (FSO) communication systems studied in this research.

## Novel Capture Algorithm Framework for Spread Spectrum Systems Under Noise and Interference

- **Status**: ❌
- **Reason**: 확산스펙트럼 포착/Doppler 동기 알고리즘 — LDPC 복호는 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:11069821
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Xiaohan Jia, Yebin Bai, Kaichuang Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/11069821
- **Abstract**: In high-speed moving environments, the Doppler effect severely impacts the frequency hopping synchronization of MSK modulated signals. Accurate frequency point estimation and Doppler frequency offset compensation are crucial for ensuring effective frequency hopping synchronization in highdynamic scenarios. To address this challenge, this paper proposes a dual-channel two-stage capture algorithm. The algorithm first establishes an initial capture threshold using the PMF-FFT method, then explores the selection of the sliding window size for two down-converted signals, aiming to find the peak corresponding to the frequency point within one frequency hopping period, while ensuring performance, complexity, and frame header capture time. In the tracking stage, adaptive threshold setting for frequency points within a hopping period is achieved using a correlation synchronization algorithm to correct Doppler frequency offset and bit shifts caused by down-sampling. In the data processing phase, the input signal is demodulated and de-spread in segments at a specified sampling rate and sample size. After LDPC decoding and CRC verification, the received data is obtained. Experimental results show that at an information rate of 300 k and a carrier-to-noise ratio of 40 dB, the system achieves a bit error rate that meets the communication system requirements with an SNR of −8dB.

## Semantic Communication Assisted Cooperative Sensing in UAV Networks

- **Status**: ❌
- **Reason**: UAV 시맨틱 통신 프레임워크 — LDPC는 비교 베이스라인(BMP+LDPC+QPSK)일 뿐
- **ID**: ieee:11069451
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Yundi Deng, Supeng Leng, Ke Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11069451
- **Abstract**: Cooperative sensing and computing are crucial for high-efficiency task completion in numerous Unmanned Aerial Vehicle (UAV) networks-based sensing applications. However, the frequent data exchange among UAVs strains communication bandwidth resources. This challenge can be further exacerbated in low signal-to-interference-plus-noise ratio (SINR) environments. Semantic communication, by extracting and transmitting task-relevant semantic information rather than raw bit streams, offers a novel approach to mitigate these issues by significantly reducing the transmission data volume while enhancing the system's robustness against noise-induced distortions. In this paper, we propose a cooperative sensing semantic communication framework with a variable semantic compression ratio in the scenario of UAVs-based multi-target cooperative sensing. We then design a resource scheduling strategy in order to efficiently integrate the limited resources of the UAVs to simultaneously enhance sensing accuracy and minimize latency of data processing. The simulation results demonstrate that the sensing accuracy of our semantic communication scheme outperforms the traditional BMP+LDPC+QPSK approach by 85.8 % at 0dB SINR, and our solution achieves an improvement up to 64.5 % in average task effectiveness score and up to 68.2 % reduction in latency, when compared to the non-semantic-assisted baseline.

## Comparative Analysis of Improved Decision Directed Carrier Phase Estimation Nonlinearity Mitigation of 16-QAM and 32-QAM

- **Status**: ❌
- **Reason**: 광통신 16/32-QAM 반송파 위상추정·비선형 완화 분석. LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:11019228
- **Type**: conference
- **Published**: 16-17 Apri
- **Authors**: K S Chakradhar, G C Likitha, G Dileep Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/11019228
- **Abstract**: The paper presents a comparative analysis of decision-directed carrier phase estimation and nonlinearity mitigation techniques in optical communication systems using 16-QAM and 32-QAM modulation formats. It investigates the impact of these techniques on system performance, particularly in terms of phase noise and signal distortion caused by fiber nonlinearity. Simulation results demonstrate the effectiveness of carrier phase estimation in reducing phase noise, signal error rate, while nonlinearity mitigation enhances signal integrity and improved band rate and spectrum efficiency. The study highlights the trade-offs between computational complexity and performance improvements in both modulation schemes. The findings offer valuable insights for optimizing future high-capacity optical networks using advanced modulation formats and 5G and LTE mobile networks where efficient use of bandwidth is critical.

## A Layered Improved Multi-Parameter Compensated Min-Sum Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 IMCMS/LIMCMS min-sum 변형 디코더 제안 - 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:11035794
- **Type**: conference
- **Published**: 11-13 Apri
- **Authors**: Xuan Liu, Dongkui Chen
- **PDF**: https://ieeexplore.ieee.org/document/11035794
- **Abstract**: In modern communication technology, low-density parity-check codes (LDPC) are widely used as an extremely important channel coding method, and it has significant performance advantages when dealing with long codes. However, the complexity of LDPC decoding algorithms is high. In response to this phenomenon, based on MCMS decoding algorithm, this paper proposes an Improved Multi-parameter Compensated MinSum (IMCMS) decoding algorithm. This algorithm adds a threshold near zero at the minimum value and chooses a locally optimal algorithm when the minimum value is less than the threshold to avoid the zero return loss of MCMS decoding algorithm. On this basis, a layered scheduling strategy is applied to propose a Layered Improved Multi-parameter Compensated Min-Sum (LIMCMS) decoding algorithm. Simulation results show that the decoding algorithm proposed in this paper not only effectively improves bit error performance but also maintains low computational complexity and significantly accelerates the convergence speed of decoding in academic papers.

## Physical Layer Coding Design for Backscatter Communication Based on Polar-LDPC Cascade Codes

- **Status**: ❌
- **Reason**: 백스캐터 통신용 Polar-LDPC 캐스케이드 - 표준 LDPC를 베이스라인으로 결합, 떼어낼 새 LDPC 기법 없음
- **ID**: ieee:11035964
- **Type**: conference
- **Published**: 11-13 Apri
- **Authors**: Dixi Zhu
- **PDF**: https://ieeexplore.ieee.org/document/11035964
- **Abstract**: Backscatter communication is attracting attention in the emerging field of radio communication as a core technology that supports the connection of a large number of devices and is able to transmit information using RF signals present in the environment. Because reflective tags are passive in design, i.e., they do not require additional energy, reflective communication has obvious advantages in terms of energy consumption and routine maintenance. However, existing reflective communication systems are unreliable due to the low strength of the transmitted signal and susceptibility to noise interference in the environment. For this reason, this paper proposes a code compilation scheme for reflex communication based on the cascading of Polar codes and LDPC codes. The reliability of the scheme is verified in terms of different excitation source time intervals, different signal-to-noise ratios, different signal attenuation degrees, and the presence or absence of an interleaver, using BER as an indicator. Through a large number of simulation experiments on Matlab platform, it is proved that the scheme proposed in this paper can reduce the influence of environmental factors on the communication quality and improve the reliability of the reflection communication system.
