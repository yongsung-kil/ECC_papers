# IEEE Xplore — 2025-06 (1차선별 통과)


## A Cross-Layer Scheduling Method for Pipelined Layered Multi-Edge Type QC-LDPC Decoder With Better Conflict Resolution

- **Status**: ✅
- **Reason**: 파이프라인 레이어드 MET-QC-LDPC 디코더의 크로스레이어 스케줄링으로 메모리 충돌 50~75% 감소, NAND LDPC 디코더 HW에 이식 가능한 D 카테고리 기법
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10971375
- **Type**: journal
- **Published**: June 2025
- **Authors**: Dongxu Chang, Qingqing Peng, Guanghui Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10971375
- **Abstract**: For multi-edge type quasi-cyclic low-density parity-check (MET-QC-LDPC) codes, the presence of common variable nodes shared between rows within a single layer poses great challenges for the hardware design of the decoder. In this study, a cross-layer update scheduling method for pipelined layered MET-QC-LDPC codes is proposed to achieve improved conflict resolution. Through a probabilistic analysis, we show that by pairing layers with relatively small common degrees and performing alternating updates between the paired layers, better conflict resolution can be achieved than the layer-by-layer updating approach. Experimental results demonstrate that, at medium to low code rates, 50% to 75% of memory conflicts can be mitigated through the proposed cross-layer scheduling compared to the layer-by-layer scheduling approach, without compromising decoding performance.

## Revisiting Multiple ECC on High-Density NAND Flash memory

- **Status**: ✅
- **Reason**: 3D TLC NAND 플래시 LDPC ECC의 코드율 적응형 설계와 read-retry 감소를 직접 다루는 A 카테고리 핵심 논문
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10947224
- **Type**: journal
- **Published**: June 2025
- **Authors**: Yunpeng Song, Yina Lv, Wentong Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10947224
- **Abstract**: Three-dimensional nand flash memory using the advanced multibit-per-cell technique is widely adopted due to its high density. However, it faces the problem of deteriorating read performance and energy consumption due to decreased reliability. Low-density parity-check code (LDPC) is typically adopted as an error correction code (ECC) to encode data and provide fault tolerance. To reduce the cost, LDPC with a high code rate is always adopted. However, LDPC will lead to read retry operations when the accessed data are not successfully decoded, and such retry-induced performance degradation is serious, especially for modern high-density flash memory. In this work, a reliability-aware differential ECC (READECC) approach is proposed to reduce redundancy protection and storage cost of LDPC with a low code rate and optimize the read performance. The basic idea is to adopt LDPC with a suitable code rate considering both data access characteristics and flash reliability characteristics. First, hot reads are identified based on the frequency of being accessed. Second, based on the reliability variation characteristics, the life of flash memory is divided into three reliability periods. As the reliability period shifts, the code rate of the LDPC adjusts adaptively to minimize redundancy protection. Third, an adaptive-sized logical page approach is further proposed to support LDPC with strong error correction capability (a low code rate) with a low storage cost. Through careful design and evaluation on 3-D triple-level-cell nand flash memory, READECC achieves encouraging optimizations with a negligible cost.

## Dual Diagonal LDPC: A Resource-Efficient Channel Coding Scheme for CubeSat Applications

- **Status**: ✅
- **Reason**: IRA 이중대각 패리티 검사 행렬 구성(코드설계, E) + Min-Sum·Bit-Flipping 결합 LLR 디코더(C) 제안으로 NAND LDPC에 이식 가능한 기법 명확
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10891713
- **Type**: journal
- **Published**: June 2025
- **Authors**: Amr Zeedan, Tamer Khattab, Ridha Hamila +1
- **PDF**: https://ieeexplore.ieee.org/document/10891713
- **Abstract**: The establishment of high-speed connectivity through CubeSats requires innovative solutions to overcome the challenges associated with the development of low-power, high-speed transceivers within the size and mass limitations inherent to CubeSats. Among the most computationally demanding tasks of any transceiver are demodulation and channel decoding, typically requiring a high utilization of hardware resources. This article proposes a channel coding scheme based on low density parity check (LDPC) coding, offering a markedly efficient allocation of resources to address these computational demands. In contrast to traditional LDPC encoding approaches, we develop a simplified algorithm based on an irregular repeat-accumulate (IRA) dual diagonal parity check matrix construction, resulting in an extremely resource-efficient code. The enhanced algorithm efficiently conserves hardware resources through the shared utilization of the parity check bit generator. Moreover, a corresponding low-complexity decoder, based on efficiently combining the Min-Sum (MS) algorithm and the Bit-Flipping (BF) algorithm, which employs the Log-Likelihood Ratio (LLR) is proposed.. We obtain the mathematical closed-form expression for the bit error rate (BER) of the proposed scheme and verify it against simulations, showing a very close match. The proposed scheme achieves high code rate, 3/4, and data rate, 30 Mbps, with a smaller number of decoding iterations, 10, while achieving better BER performance compared to various existing algorithms. Compared to the channel coding schemes currently being employed by CubeSats, our scheme demonstrates the highest information rate, the lowest number of decoding iterations and the highest efficiency.

## U-Shaped Error Correction Code Transformers

- **Status**: ✅
- **Reason**: U-shaped 트랜스포머(U-ECCT) 기반 신경망 디코더 — 일반 선형 코드 디코딩 학습 모델로 NAND LDPC ECC 신경망 디코더에 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10720857
- **Type**: journal
- **Published**: June 2025
- **Authors**: Dang-Trac Nguyen, Sunghwan Kim
- **PDF**: https://ieeexplore.ieee.org/document/10720857
- **Abstract**: In this work, we introduce two variants of the U-shaped error correction code transformer (U-ECCT) in combination with weight-sharing to improve the decoding performance of the error correction code transformer (ECCT) for moderate-length linear codes. The proposed models are inspired by the well-known U-Net architecture to leverage residual information for faster error estimation based on the syndrome-based reliability decoding principle. As an effort to further improve the general decoding performance of the U-ECCT, we propose the variational U-ECCT (VU-ECCT), in which the process of learning the shortcut connections is treated as a generative problem, forming a variational autoencoder (VAE) that exists intertwined with the existing U-ECCT model. This design allows the extraction of mutual information between the different levels of the U-shaped architecture, thus enhancing the performance of large syndrome sequences for low-rate codes. Additionally, to further reduce the model size, a new weight-sharing strategy, called mirror-sharing, is proposed to compress the model size as well as complement the mechanism of the proposed U-shaped architecture. In experiments, it has been demonstrated that our proposed models achieve significantly better performance than baseline conventional algorithms and other learning-based models.

## Low-Complexity Neural Belief Propagation Decoding Algorithm Based on Tensor Ring Decomposition

- **Status**: ✅
- **Reason**: Tensor Ring 분해 기반 저복잡도 Neural BP(NBP/CENBP) 디코더 — BCH·LDPC 적용 실험 포함, NAND LDPC 디코더 복잡도 저감에 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10738425
- **Type**: journal
- **Published**: June 2025
- **Authors**: Yuanhui Liang, Chan-Tong Lam, Qingle Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/10738425
- **Abstract**: Neural belief propagation (NBP) decoding can improve the performance of belief propagation (BP) decoding for high-density parity check (HDPC) codes, at the expense of higher memory storage requirement and computational complexity due to the addition of trainable weight coefficients. To reduce the high storage requirement of NBP, the cyclically equivariant neural BP (CENBP) algorithm makes full use of the cyclically invariant property of the cyclic code, optimizes and reuses the weight coefficients of the NBP algorithm, at the expense of further increasing the computational complexity of NBP. In this paper, we propose low-complexity, in terms of both memory storage requirement and computational complexity, NBP and CENBP decoding algorithms based on Tensor Ring (TR) decomposition. First, in order to reduce the memory storage and computational complexity of the NBP algorithm, we propose a TR-based compression algorithm to compress the messages and mathematical calculations in the NBP decoding algorithm, called TR-NBP algorithm. Second, to address the high computational complexity of the CENBP algorithm, we propose to apply TR decomposition-based compression to the odd layers of the CENBP decoding algorithm, called TR-CENBP, to reduce the computational complexity, and further reduce the required memory storage requirement of the CENBP algorithm. Furthermore, we use TR decomposition-based compression to simplify the mathematical computations associated with the tanh function in the NBP algorithm to further reduce the complexity of the hardware implementation. Experimental results show that direct compression of BP algorithm using TR decomposition results in significant performance degradation and our proposed low complexity TR-NBP algorithm and TR-CENBP algorithm can greatly reduce both the memory storage requirement and computation complexity, without significant performance degradation for typical BCH and LDPC codes.

## Gradient Descent Decoding of MDPC Codes Optimized with Genetic Algorithm

- **Status**: ✅
- **Reason**: 유전 알고리즘으로 최적화된 AD-GDBFwM 비트플리핑 디코더가 BP 수준 성능을 달성하며 LDPC계 코드에 이식 가능한 디코더 알고리즘(C)임
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11114132
- **Type**: conference
- **Published**: 9-12 June 
- **Authors**: Dimitrije Jovanović, Jovan Milojković, Zoran Čiča +1
- **PDF**: https://ieeexplore.ieee.org/document/11114132
- **Abstract**: Bit-flipping (BF) is a very simple algorithm for decoding linear block codes. For the BF to achieve high performances of belief-propagation (BP) algorithms, which are far more complex, we apply several optimizations using the genetic algorithm (GA), to optimize the parameters of our decoder. Adaptive diversity gradient descent bit-flipping with momentum (AD-GDBFwM) algorithm is designed as a cascade of multiple decoders with different parameters, which are optimized with GA. In this paper we consider AD-GDBFwM decoding of mediumdensity parity-check (MDPC) codes. We measure the decoding performance and compare it with the results of various types of decoders, including BP and neural BP.

## Iterative Decoding Algorithms Powered by Deep Learning

- **Status**: ✅
- **Reason**: 신경망 BP 디코딩으로 HDPC/MDPC 코드 단사이클 영향 저감 및 BER 개선—NAND LDPC 디코더에 이식 가능한 신경망 디코더 알고리즘(C)임
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11114279
- **Type**: conference
- **Published**: 9-12 June 
- **Authors**: Dimitrije Jovanović, Predrag Ivaniš
- **PDF**: https://ieeexplore.ieee.org/document/11114279
- **Abstract**: In this paper, we analyze the performance of neural belief propagation (BP) decoding on the additive white Gaussian noise (AWGN) channel, compared to the traditional BP algorithm. Previous investigations have shown that assigning pre-trained weights to BP messages can significantly improve the decoding performance in case of high-density parity-check (HDPC) codes, by reducing the negative impact of short cycles. These weights are trained by a neural network whose structure matches the trellis of the decoder. Specifically, we show that medium-density paritycheck (MDPC) codes decoded with neural BP algorithm can achieve lower bit error rate versus HDPC codes with the same codeword length and the same code rate.

## Multi-Stage Bit-Flipping Decoder Design for Quantum Error-Correcting Codes

- **Status**: ✅
- **Reason**: qLDPC 대상이지만 min-sum 1단계 + WBF/RBF 비트플리핑 다단계 디코더로 error floor 감소 기법(C)이 고전 LDPC에 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11291312
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Patrick J. Moxom, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/11291312
- **Abstract**: This paper proposes the use of simple bit-flipping (BF) methods as a post processor for decoding quantum low-density parity check codes (qLDPC) with message passing (MP). Specifically, min-sum (MS) is used as the MP method for the first stage of the multi-stage decoder. Two methods are proposed that modify the low-complexity Gallager’s algorithm (GA). First, a weighted bit-flipping (WBF) method is developed using soft information from the MP stage. Secondly, GA is modified with a random bit-flipping (RBF) approach. Early stopping and loop detector stage switching methods are used to enhance the performance of the BF stage. These methods are shown to significantly reduce the error floor of the first stage while also being less complex than alternative multi-stage decoders.

## A New Post-Quantum Signature Based on Punctured QC-LDPC Code with Random Insertion

- **Status**: ✅
- **Reason**: QC-LDPC puncturing·최소 해밍 무게 기반 구성·BP 디코딩 개선이 독립적으로 기술되어 있어 고전 QC-LDPC 코드설계(E)로 이식 가능; 보안 응용이나 기반 코드설계 떼어낼 수 있음.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11162115
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Xin Lin, Yusun Fu, Zihao Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/11162115
- **Abstract**: This paper proposes an enhanced version of the CFS signature scheme, leveraging QC-LDPC codes with puncturing and random insertion techniques. The puncturing process is designed based on the selection of minimum Hamming weight codewords, ensuring that the remaining structure of the parity-check matrix retains sufficient error-correcting capabilities. Random insertion of new rows into the punctured parity-check matrix further enhances security by introducing randomness. The cyclic structure of QC-LDPC codes greatly reduces the key size while the BP decoding algorithm improves the decoding success rate, thereby enhancing the signature generation efficiency. The scheme proposed in this paper reduces the key size to 6144 bytes compared to the original CFS scheme's 6283256 bytes under the similar parameters setting. Additionally, the average number of signing attempts is reduced from $t!$ to a constant multiple of $t$. It also greatly enhances security compared to recent improvements, particularly in resisting structural attacks, Stern's attacks, OTD attacks, and forgery attacks. Similar to the original CFS scheme, the proposed scheme can be proven to satisfy Existential Unforgeability under Chosen Message Attacks (EUF-CMA) security.

## A Practical Method for Power Saving in 4G, 5G, and Beyond 5G Channel Decoders Using RBIR

- **Status**: ✅
- **Reason**: RBIR 기반 LDPC 디코더 반복 수 동적 예측(최대 54.7% 감소) 기법(C)이 NAND LDPC 디코더 조기 종료·전력 절감에 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11160748
- **Type**: conference
- **Published**: 8-12 June 
- **Authors**: Anusha Gunturu, Ashok Kumar Reddy Chavva
- **PDF**: https://ieeexplore.ieee.org/document/11160748
- **Abstract**: With sustainability as one of the key requirements and the design principles of the sixth generation (6 G) communications, implementation based power saving solutions that benefit both base station (BS) and user equipment (UE) sides have gained significant interest in the cellular industry research. Channel decoding is one of the receiver modules that can help reduce the power consumption of the receiver significantly, and is applicable to both BS and UE. In this paper, we propose a universal list size and iteration number predictor (ULIP), for reducing the power consumption, applicable for 4G, 5G and beyond-5G channel decoders. We propose to use a link abstraction abstraction metric called received bit information rate (RBIR), that captures the time-varying channel conditions to identify and choose the iteration and list sizes for these decoders, to reduce the power consumption. We evaluate the proposed ULIP for regulating the iteration number in turbo and low-density parity-check (LDPC) decoders, used in 4 G and 5 G data channels, respectively, and the list size in polar decoder, used in 5 G control channel. We also verify the proposed ULIP for regulating the list size in the recently introduced polarization-adjusted convolutional (PAC) decoder, a prospective scheme for 6 G. We show that the proposed solution has upto 54.7 % and 67.4 % reduction of iteration numbers in LDPC and turbo decoders, respectively, for a target block error rate (BLER) of 10 %, and upto $\sim 92 \%$ reduction of list sizes in both polar and PAC decoders, for a target BLER of 0.1 %, compared to conventional decoding methods.

## Implementation of Low-Density Parity-Check (LDPC) Codes in Verilog HDL

- **Status**: ✅
- **Reason**: LDPC 인코더 FPGA/Verilog 구현(다양한 code rate), 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11101329
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: Ritesh Pathak, Sateesh Kumar Awasthi
- **PDF**: https://ieeexplore.ieee.org/document/11101329
- **Abstract**: This work presents FPGA implementation of Low-Density Parity-Check (LDPC) encoder. Low-density coding is an effective method for ensuring reliable communication over noisy channels while minimizing the probability of error. We use Verilog hardware description language (HDL) to simulate this encoder for various code rates. The encoder is implemented on the Xilinx Artix-7 FPGA(XC7A35T-ICPG236C) kit using FPGA 28 nm CMOS technology and DE10-Lite FPGA Kit using FPGA 55 nm CMOS technology.

## Development of a Universal FPGA-Based Coprocessor for 5G NR and WLAN LDPC Coding

- **Status**: ✅
- **Reason**: 5G/WLAN LDPC FPGA 코프로세서 — 디코더 HW 아키텍처·메모리관리·스케줄링 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11037065
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Lukasz Lopacinski, Yiyun Jian, Muhammad Nauman +3
- **PDF**: https://ieeexplore.ieee.org/document/11037065
- **Abstract**: Low-density parity-check (LDPC) codes are widely used in modern communication systems due to their near-capacity error correction performance. This paper presents a practical FPGA implementation of a universal hardware coprocessor for LDPC encoding and decoding, focusing on a system-level architecture, achievable data rate, latency measurements, and hardware resource utilization. The LDPC coding is realized by the Xilinx hardware macros available in the Xilinx RF-SoC FPGAs. We explore various design simplifications, including core combining, memory management, and data scheduling, to achieve high throughput while maintaining the lowest implementation complexity. The proposed architecture is implemented on an FPGA platform and is equipped with 10Gb/s Ethernet interfaces, demonstrating real-time decoding capabilities and improved performance compared to software-based approaches. Experimental results validate the design, showcasing its applicability in high-speed communication systems. This work can serve as a reference for engineers and researchers aiming to deploy LDPC decoding in FPGA-based environments by reusing the existing Intellectual Property (IP), which is freely available in Xilinx SoC.

## High Performance and Resource Efficient Low Density Parity Check Decoder Design

- **Status**: ✅
- **Reason**: Gallager B/Intrinsic GaB 디코더 설계·FPGA 구현 — 이식 가능 디코더 알고리즘+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11112140
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Burak Ünal
- **PDF**: https://ieeexplore.ieee.org/document/11112140
- **Abstract**: Low Density Parity Check (LDPC) codes have gained popularity in communication systems due to their capacity-approaching error correction performance. In this study, a high-performance LDPC decoding algorithm with extremely low resource usage is proposed. Among the hard decision class of LDPC decoders, Gallager B (GaB) provides high-performance hardware due to its computational simplicity. However, GaB suffers from poor error-correction performance. In this study, a new intrinsic computation technique for GaB called Intrinsic Gallager B (IGaB) is introduced to improve error correction performance. Our simulation results show that the IGaB algorithm provides better error correction performance compared with GaB. GaB and IGaB algorithms are implemented on Field Programmable Gate Array (FPGA) to compare hardware performance.

## Protograph-Based LDPC Codes with Local Irregularity

- **Status**: ✅
- **Reason**: Protograph 기반 LDPC 부호 설계(local irregularity, PEXIT 임계값 최적화) — 코드설계 직접 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195381
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Vincent Wüst, Erdem Eray Cil, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/11195381
- **Abstract**: Forward error correcting (FEC) codes are used in many communication standards with a wide range of requirements. FEC codes should work close to capacity, achieve low error floors, and have low decoding complexity. In this paper, we propose a novel category of low-density parity-check (LDPC) codes, based on protograph codes with local irregularity. This new code family generalizes conventional protograph-based LDPC codes and is capable of reducing the iterative decoding threshold of the conventional counterpart. We introduce an adapted version of the protograph extrinsic information transfer (PEXIT) algorithm to estimate decoding thresholds on the binaryinput additive white Gaussian noise channel, perform optimizations on the local irregularity, and simulate the performance of some constructed codes.

## Construction of QC-LDPC Codes with Girth $g$ from the Hermite Normal Form of a Matrix

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC girth-g 구성을 Hermite normal form으로 lifting factor/blocklength 결정하는 새 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195483
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Anthony Gómez-Fonseca
- **PDF**: https://ieeexplore.ieee.org/document/11195483
- **Abstract**: The problem of determining the existence of a protograph-based QC-LDPC code with girth $g$ and shortest blocklength for a prescribed protograph has been investigated in the literature. In some of these works, the goal was to obtain an algebraic expression for the blocklength in terms of the dimensions of the biadjacency matrix of the protograph and a lifting factor $N$. An algebraic expression has been found for $N$ when $g> 4$ is desired in the case of the fully connected (all-one) protograph but only lower bounds for the cases with larger girth. Computer search has been used in most cases to determine the exact value for $N$ that gives the shortest blocklength for a particular protograph. In this paper, we present a promising connection between the lifting factor $N$ (and therefore the blocklength of a QC-LDPC code) and the product of the pivots of the Hermite normal form of a matrix constructed from certain substructures in the protograph called tailless backtrackless closed (TBC) walks.

## Analysis and Design of Improved 5G LDPC Codes for Faster-Than-Nyquist Signaling

- **Status**: ✅
- **Reason**: 바이너리 5G LDPC를 FTN용으로 PEXIT 기반 새 설계기준으로 최적화 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195595
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Jiayi Yang, Qianfan Wang, Shuangyang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/11195595
- **Abstract**: This paper focuses on the analysis and design of improved 5G low-density parity-check (LDPC) codes for faster-than-Nyquist (FTN) signaling. We first propose the protograph-based extrinsic information transfer (PEXIT) chart analysis for the LDPC-coded FTN system using the sum-product algorithm (SPA) based on the Ungerboeck observation model, where the distribution of the output mutual information from the detector is approximately derived using least squares fitting. With the proposed PEXIT chart analysis, we then design the improved LDPC codes for the coded FTN signaling aiming to achieve a lower decoding threshold and thereby better error performance. The proposed codes are optimized based on the raptor-like structure of the 5G LDPC codes and also support rate compatibility. The proposed codes reveals two distinct LDPC code design criteria for FTN signaling, i.e., 1) no information bits should be punctured; 2) columns with high column weights should be removed in the base graph. The advantages of the proposed codes are explicitly verified by our numerical results, where noticeable coding gains compared to existing codes and coded Nyquist systems can be observed.

## Subcode Ensemble Decoding of Linear Block Codes

- **Status**: ✅
- **Reason**: 단블록 LDPC용 subcode ensemble BP 디코딩(SCED)으로 성능 향상 — 디코더 알고리즘 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195423
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Jonathan Mandelbaum, Holger Jäkel, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/11195423
- **Abstract**: Low-density parity-check (LDPC) codes together with belief propagation (BP) decoding yield exceptional error correction capabilities in the large block length regime. Yet, there remains a gap between BP decoding and maximum likelihood decoding for short block length LDPC codes. In this context, ensemble decoding schemes yield both reduced latency and good error rates. In this paper, we propose subcode ensemble decoding (SCED), which employs an ensemble of decodings on different subcodes of the code. To ensure that all codewords are decodable, we use the concept of linear coverings and explore approaches for sampling suitable ensembles for short block length LDPC codes. Monte-Carlo simulations conducted for three LDPC codes demonstrate that SCED improves decoding performance compared to stand-alone decoding and automorphism ensemble decoding. In particular, in contrast to existing schemes, e.g., multiple bases belief propagation and automorphism ensemble decoding, SCED does not require the NP-complete search for low-weight dual codewords or knowledge of the automorphism group of the code, which is often unknown.

## Belief Propagation Decoding for Short Codes on Structured Sparse Parity-Check Matrices

- **Status**: ✅
- **Reason**: 단주기-free 구조적 sparse PCM 설계로 단부호 BP 성능 개선 — 바이너리 디코더/구성 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195685
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Yifei Shen, Zongyao Li, Emmanuel Boutillon +5
- **PDF**: https://ieeexplore.ieee.org/document/11195685
- **Abstract**: As successfully adopted in standard long code scenarios, belief propagation (BP) decoding has been considered a promising universal decoding candidate for next-generation wireless communications. However, when applied to short codes, BP decoding suffers from poor error correction performance due to harmful cycle structures in the Tanner graph. In this paper, we address this issue by designing a structured, sparse parity-check matrix (ssPCM) framework, composed of multiple cycle-free parity-check row blocks (PCRBs). The resulting ssPCMs feature regular row weights and perform better than the state-of-theart 4 -cycle-free row redundant PCMs across Bose-Chaudhuri-Hocquenghem (BCH) codes of length 63.

## In-Memory BER Estimation Using Syndromes of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC 신드롬 기반 BER 추정용 코드설계 기법, in-memory ECC — 바이너리, 새 코드설계 기여(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195686
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Yotam Gershon, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/11195686
- **Abstract**: In-memory computing architectures highly improve computation latency and power compared to von Neumann architectures suffering the memory wall. However, maintaining reliability is challenging due to the difficulty in implementing error-correction coding within memory. We propose a scheme in which strong codes can be used for in-memory computing, while avoiding their costly decoding when error rates are sufficiently small. The key idea and thrust of the paper is to complement the design of LDPC codes to also provide accurate estimation of the input bit-error rate (BER). Toward that, we derive analytical results and give code-design insights for BER estimation in two frameworks: minimizing the mean-squared error (MSE), and estimating threshold crossing as a hypothesis-testing problem.

## BF-Max: an Efficient Bit Flipping Decoder with Predictable Decoding Failure Rate

- **Status**: ✅
- **Reason**: Bit-Flipping 디코더 변형(BF-Max)·저복잡도 HW 구현·DFR 모델링 — 디코더 알고리즘 이식 가능(C). MDPC/암호 맥락이나 BF 기법 자체는 떼어낼 수 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195380
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Alessio Baldelli, Marco Baldi, Franco Chiaraluce +1
- **PDF**: https://ieeexplore.ieee.org/document/11195380
- **Abstract**: The Bit-Flipping (BF) decoder, thanks to its very low computational complexity, is widely employed in post-quantum cryptographic schemes based on Moderate Density Parity Check codes in which, ultimately, decryption boils down to syndrome decoding. In such a setting, for security concerns, one must guarantee that the Decoding Failure Rate (DFR) is negligible. Such a condition, however, is very difficult to guarantee, because simulations are of little help and the decoder performance is difficult to model theoretically. In this paper, we introduce a new version of the BF decoder, that we call BF-Max, characterized by the fact that in each iteration only one bit (the least reliable) is flipped. When the number of iterations is equal to the number of errors to be corrected, we are able to develop a theoretical characterization of the DFR that tightly matches with numerical simulations. We also show how BF-Max can be implemented efficiently, achieving low complexity and making it inherently constant time. With our modeling, we are able to accurately predict values of DFR that are remarkably lower than those estimated by applying other approaches.

## Bounds and New Constructions for Girth-Constrained Regular Bipartite Graphs

- **Status**: ✅
- **Reason**: LDPC용 girth-제약 정규 이분그래프 구성(girth=8, 고부호율 sparse H) — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195214
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Sheida Rabeti, Mohsen Moradi, Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/11195214
- **Abstract**: In this paper, we explore the design and analysis of regular bipartite graphs motivated by their application in lowdensity parity-check (LDPC) codes specifically with constrained girth and in the high-rate regime. We focus on the relation between the girth of the graph, and the size of the sets of variable and check nodes. We derive bounds on the size of the vertices in regular bipartite graphs, showing how the required number of check nodes grows with respect to the number of variable nodes as girth grows large. Furthermore, we present two constructions for bipartite graphs with girth $\mathcal{G}=8$; one based on a greedy construction of ($w_{c}, w_{r}$) -regular graphs, and another based on semi-regular graphs which have uniform column weight distribution with a sublinear number of check nodes. The second construction leverages sequences of integers without any length- 3 arithmetic progression and is asymptotically optimal while maintaining a girth of 8. Also, both constructions can offer sparse parity-check matrices for high-rate codes with medium-to-large block lengths. Our results solely focus on the graph-theoretic problem but can potentially contribute to the ongoing effort to design LDPC codes with high girth and minimum distance, specifically in high code rates.

## Interplay Between Belief Propagation and Transformer: Differential-Attention Message Passing Transformer

- **Status**: ✅
- **Reason**: BP+Transformer 신경망 디코더, 단·중길이 LDPC에서 BP 능가 — 신경망 디코더 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195462
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Chin Wa Ken Lau, Xiang Shi, Ziyan Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/11195462
- **Abstract**: Transformer-based neural decoders have emerged as a promising approach to error correction coding, combining data-driven adaptability with efficient modeling of long-range dependencies. This paper presents a novel decoder architecture that integrates classical belief propagation principles with transformer designs. We introduce a differentiable syndrome loss function leveraging global codebook structure and a differential-attention mechanism optimizing bit and syndrome embedding interactions. Experimental results demonstrate consistent performance improvements over existing transformer-based decoders, with our approach surpassing traditional belief propagation decoders for short-to-medium length LDPC codes.

## A Strategy to Detect Error Propagation in Sliding Window Decoding of SC-LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 슬라이딩윈도우 디코딩의 오류전파 검출 스케줄 — 디코더 알고리즘 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195331
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Mauro M. M. Costantino, Massimo Battaglioni, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/11195331
- **Abstract**: Spatially Coupled Low-Density Parity-Check (SCLDPC) codes are characterized by very long codeword lengths. For this reason, they are usually decoded with sliding window algorithms, which allow piecewise processing and decoding of the codeword symbols. In order to mitigate error propagation, it is possible to adapt strategies, such as non-uniform window sizes and node doping. In this paper, we propose a novel adaptive decoding schedule, which can be integrated with the aforementioned strategies. Numerical results confirm that the proposed approach can successfully detect error propagation events with more accuracy than conventional log-likelihood ratio-based approaches. Simulation results show that the error rate performance of time-invariant SC-LDPC codes significantly improves when the proposed strategies are adopted.

## High-Rate Spatially Coupled LDPC Codes Based on Massey's Convolutional Self-Orthogonal Codes

- **Status**: ✅
- **Reason**: CSOC 기반 고부호율 SC-LDPC 구성+protograph lifting+sliding window BP, girth/free distance 보장 — 코드설계(E)/디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195322
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Daniel J. Costello, Min Zhu, David G. M. Mitchell +1
- **PDF**: https://ieeexplore.ieee.org/document/11195322
- **Abstract**: We propose a new class of high-rate spatially coupled LDPC (SC-LDPC) codes based on the convolutional selforthogonal codes (CSOCs) first introduced by Massey. The SCLDPC codes are constructed by treating the irregular graph corresponding to the parity-check matrix of a systematic rate $R=(n-1) / n$ CSOC as a convolutional protograph. The protograph can then be lifted using permutation matrices to generate a high-rate SC-LDPC code whose strength depends on the lifting factor. The SC-LDPC codes constructed in this fashion can be decoded using iterative belief propagation based sliding window decoding. To improve performance, a non-systematic version of a C SOC parity-check matrix is then proposed by making a slight modification to the systematic construction. Even though the parity-check matrix is in non-systematic form, we show how systematic encoding can still be performed. We also show that the non-systematic convolutional protograph has a guaranteed girth and free distance and that these properties carry over to the lifted versions. Numerical results are included demonstrating that CSOC-based SC-LDPC codes (i) have performance at least as good as that of SC-LDPC codes commonly found in the literature, and (ii) have iterative decoding thresholds comparable to those of existing SC-LDPC code designs.

## Transformer-Based Decoding in Concatenated Coding Schemes Under Synchronization Errors

- **Status**: ✅
- **Reason**: transformer 기반 BP 외부 디코더 제시(신경망 디코더 C) — DNA storage용이나 디코더 기법 이식 가능, 애매해 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195598
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Julian Streit, Franziska Weindel, Reinhard Heckel
- **PDF**: https://ieeexplore.ieee.org/document/11195598
- **Abstract**: We consider the reconstruction of a codeword from multiple noisy copies, each independently corrupted by insertion, deletion, and substitution errors. This problem arises, for example, in DNA data storage. A common code construction uses a concatenated code with an outer linear block code and an inner marker code, decoded via Belief Propagation (BP) and the Bahl-Cocke-Jelinek-Raviv (BCJR) algorithm, respectively. However, the BCJR algorithm scales exponentially with the number of nois copies, making reconstruction from more than about four copies infeasible. In this paper, we introduce BCJRFormer, a transformer-based neural inner decoder for marker codes. BCJRFormer achieves error rates comparable to the BCJR algorithm for single-message transmissions while scaling only quadratically with the number of noisy copies. This makes BCJRFormer well suited for DNA data storage, where multiple reads of the same DNA sequence are common. To further reduce the bit error rate, we replace the BP outer decoder with a transformer-based decoder. Combined, this results in a performant and efficient end-to-end transformer-based pipeline for decoding multiple noisy copies corrupted by insertion, deletion, and substitution errors.

## Improved Decoding of Tanner Codes

- **Status**: ✅
- **Reason**: 바이너리 expander-based Tanner code의 새 선형시간 디코딩 알고리즘/디코딩 반경 개선 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195639
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Zhaienhe Zhou, Zeyu Guo
- **PDF**: https://ieeexplore.ieee.org/document/11195639
- **Abstract**: In this paper, we present improved decoding algorithms for expander-based Tanner codes. We begin by developing a randomized linear-time decoding algorithm that, under the condition that $\delta d_{0}>2$, corrects up to $\alpha n$ errors for a Tanner code $T\left(G, C_{0}\right)$, where $G$ is a ($c, d, \alpha, \delta$) bipartite expander with $n$ left vertices, and $C_{0} \subseteq \mathbb{F}_{2}^{d}$ is a linear inner code with minimum distance $d_{0}$. This result improves upon the previous work of Cheng, Ouyang, Shangguan, and Shen (RANDOM 2024), which required $\delta d_{0}>3$. We further derandomize the algorithm to obtain a deterministic linear-time decoding algorithm with the same decoding radius. Our algorithm improves upon the previous deterministic algorithm of Cheng et al. by achieving a decoding radius of $\alpha n$, compared with the previous radius of $\frac{2 \alpha}{d_{0}(1+0.5 c \delta)} n$. Additionally, we investigate the size-expansion trade-off introduced by the recent work of Chen, Cheng, Li, and Ouyang (IEEE TIT 2023), and use it to provide new bounds on the minimum distance of Tanner codes. Specifically, we prove that the minimum distance of a Tanner code $T\left(G, C_{0}\right)$ is approximately $f_{\delta}^{-1}\left(\frac{1}{d_{0}}\right) \alpha n$, where $f_{\delta}(\cdot)$ is the Size-Expansion Function. As another application, we improve the decoding radius of our decoding algorithms from $\alpha n$ to approximately $f_{\delta}^{-1}\left(\frac{2}{d_{0}}\right) \alpha n$.

## Removal of Small Weight Stopping Sets for Asynchronous Unsourced Multiple Access

- **Status**: ✅
- **Reason**: stopping set 제거+PEG girth 최적화로 error floor 완화 — 바이너리 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195696
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Frederik Ritter, Jonathan Mandelbaum, Alexander Fengler +2
- **PDF**: https://ieeexplore.ieee.org/document/11195696
- **Abstract**: In this paper, we analyze the formation of small stopping sets in joint factor graphs describing a frame-asynchronous two-user transmission. Furthermore, we propose an algorithm to completely avoid small stopping sets in the joint factor graph over the entire range of symbol delays. The error floor caused by these stopping sets is completely mitigated. Our key observation is that, while the order of bits in the codeword is irrelevant in a single-user environment, it turns out to be crucial in an asynchronous, unsourced two-user system. Subsequently, our algorithm finds a reordering of variable nodes which avoids the smallest stopping set in the joint graph. We show that further improvements can be achieved when girth optimization of the single-user graphs by progressive edge growth (PEG) is used in combination with our proposed algorithm. Starting with a randomized code construction with optimized degree distribution, our simulation results show that PEG followed by the proposed algorithm can improve the average per user probability of error in a noiseless channel by almost two orders of magnitude for a broad range of frame delays.

## Threshold Selection for Iterative Decoding of $(v,\ w)$-Regular Binary Codes

- **Status**: ✅
- **Reason**: (v,w)-regular LDPC/MDPC용 bit-flipping 디코더 임계값 선택·DFR 모델 — 디코더 알고리즘 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11195438
- **Type**: conference
- **Published**: 22-27 June
- **Authors**: Alessandro Annechini, Alessandro Barenghi, Gerardo Pelosi
- **PDF**: https://ieeexplore.ieee.org/document/11195438
- **Abstract**: Iterative bit flipping decoders are an efficient and effective choice for decoding codes which admit a sparse parity-check matrix. Among these, sparse $(v,\ w)$-regular codes, which include LDPC and MDPC codes, are of particular interest both for efficient data correction and the design of cryptographic primitives. Throughout the iterative decoding process, the bit flipping thresholds can be determined either statically or during the decoder execution, by using information coming from the initial syndrome value and its updates. In this work, we analyze a two-iterations parallel hard decision bit flipping decoder and propose concrete criteria for threshold determination, backed by a closed form model. In doing so, we introduce a new tightly fitting model for the distribution of the Hamming weight of the syndrome after the first decoder iteration and substantial improvements on the decoding failure rate (DFR) estimation with respect to existing approaches.

## Performance Analysis of an Advanced HARQ Scheme Based on LDPC Coupled Codes

- **Status**: ✅
- **Reason**: 공간결합 LDPC(SC-LDPC) 기반 프레임 중첩 HARQ로 다중블록 동시 디코딩 제안 — 디코더/코드설계 이식 가능성(C/E), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11174663
- **Type**: conference
- **Published**: 17-20 June
- **Authors**: Yiyun Jian, Lukasz Lopacinski, Eckhard Grass
- **PDF**: https://ieeexplore.ieee.org/document/11174663
- **Abstract**: In this paper, we investigate the effectiveness of a newly proposed frame superposition Hybrid Automatic Repeat reQuest (HARQ) scheme, which adopts different variants of spatially coupled low-density parity-check (LDPC) codes. The construction of the method with the use of 5 G new radio (NR) LDPC codes is explained in detail. Bit error rate (BER), frame error rate (FER), and the projected data goodput in additive white Gaussian noise (AWGN) and Rayleigh block fading channels are investigated. The HARQ scheme is based on frame combination by using spatially coupled LDPC codes. It outperforms all classical variants of HARQ and can, hence, be seen as a potential successor of the classical methods. The main cost is the need for more complicated LDPC decoding, whereby the decoder needs to support the decoding of two or even more blocks at the same time.

## Neural Adaptive Offest Min-Sum Algorithm for LDPC Decoding

- **Status**: ✅
- **Reason**: Neural Adaptive Offset Min-Sum(NAOMS) — min-sum 변형 신경망 디코더, NAND LDPC에 이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11165549
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Haojia Zhang, Shuai Han, Hao Chen
- **PDF**: https://ieeexplore.ieee.org/document/11165549
- **Abstract**: With the rapid development of deep learning and its applications in physical layer communication, deep learning-based channel coding has gradually become a research hotspot. In this paper, based on the neural offset min-sum (NOMS) low-density parity-check (LDPC) decoding network, we propose a neural adaptive offset min-sum (NAOMS) LDPC decoding network. By considering the current input values of the check nodes when learning the additive offset parameters and introducing an adaptive offset weight vector, we can better leverage deep learning techniques. Experimental results show that, with a slight increase in complexity, the proposed decoder achieves a 0.8dB improvement in bit error rate (BER) over the NOMS LDPC decoding network. Moreover, the NAOMS decoder requires fewer learning offset parameters compared to the NOMS decoder.

## Adaptive Quantized and Normalized QC-LDPC Universal Block-Parallel Decoder

- **Status**: ✅
- **Reason**: 적응형 양자화·정규화 QC-LDPC 블록병렬 FPGA 디코더 — 이식 가능한 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11165566
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Xia An, Chao Zhang, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/11165566
- **Abstract**: As wireless communication systems evolve, new frameworks place increasing demands on terminal performance, including throughput, latency, power consumption, and size. Software-Defined Radio (SDR) systems have the potential to support multiple communication standards and enabling on-demand upgrades due to their flexibility. However, purely software-based implementations for physical layer protocols reduce efficiency, necessitating the use of external accelerators such as FPGA for specialized computation. Specifically, channel decoding contributes a lot to the physical layer’s complexity, and thus is highly demand for FPGA specialized implementation while retaining the universality of the decoding architecture in some level. This paper presents an adaptive quantized and normalized QC-LDPC universal decoder based on a block-parallel architecture with pipeline and instruction-driven approach. The proposed decoder improves throughput and reduces computational complexity while maintaining flexibility for various QC-LDPC codes. Experimental results demonstrate that the adaptive quantization and normalization scheme significantly outperforms existing methods in terms of decoding performance and maximum frequency, offering a more efficient solution for SDR systems.

## New 5G-NR-Like LDPC Code Design for HRLLC Scenarios

- **Status**: ✅
- **Reason**: 최소거리 최적화로 error floor 저감, PEG/lifting 기반 base matrix 설계 + hybrid list 디코딩 — 이식 가능한 코드설계/디코더 기여(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11165523
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Zhitong He, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/11165523
- **Abstract**: To meet the requirements of hyper-reliable and low-latency communication (HRLLC) scenarios, a new design of 5G-NR-Like LDPC codes is proposed, which majorly optimizes the minimum distance property, to lower the error floor for short to medium code lengths. Meanwhile, progressive row extension techniques are employed for base matrix design, and progressive edge growth and lifting techniques are employed for lifting design, to achieve desirable decoding performance across the nested code rates and code lengths under given design complexity. The hybrid list decoding algorithm is employed to further improve the decoding performance for short block lengths. Simulation results demonstrate the effectiveness of our new 5G-NR-Like LDPC code design and hybrid list decoding algorithm.
