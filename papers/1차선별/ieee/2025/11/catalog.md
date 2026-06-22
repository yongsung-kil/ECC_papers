# IEEE Xplore — 2025-11 (1차선별 통과)


## Edge-Spreading Raptor-Like LDPC Codes for 6G Wireless Systems

- **Status**: ✅
- **Reason**: SC-LDPC 엣지-스프레딩 구성 및 통합 그래프 기반 최적 커플링 행렬 설계 기법(E)이 NAND 플래시 LDPC 코드 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11025845
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Yuqing Ren, Leyu Zhang, Yifei Shen +4
- **PDF**: https://ieeexplore.ieee.org/document/11025845
- **Abstract**: Next-generation channel coding has stringent demands on throughput, energy consumption, and error rate performance while maintaining key features of 5G New Radio (NR) standard codes such as rate compatibility, which is a significant challenge. Due to excellent capacity-achieving performance, spatially-coupled low-density parity-check (SC-LDPC) codes are considered a promising candidate for next-generation channel coding. In this paper, we propose an SC-LDPC code family called edge-spreading Raptor-like (ESRL) codes. Unlike other SC-LDPC codes that adopt the structure of existing rate-compatible LDPC block codes before coupling, ESRL codes maximize the possible locations of edge placement and focus on constructing an optimal coupled matrix. Moreover, a new graph representation called the unified graph is introduced. This graph offers a global perspective on ESRL codes and identifies the optimal edge reallocation to optimize the spreading strategy. We conduct comprehensive comparisons of ESRL codes and 5G-NR LDPC codes. Simulation results demonstrate that when all decoding parameters and complexity are the same, ESRL codes have obvious advantages in error rate performance and throughput compared to 5G-NR LDPC codes in some specific scenarios (low and high number of iterations), making them a promising solution towards next-generation channel coding.

## SC-GC-LDPC for nand Flash Memory: Construction and Decoding

- **Status**: ✅
- **Reason**: NAND 플래시 직접 대상의 SC-GC-LDPC 코드 구성 및 층화 NMS/SPA 디코딩 알고리즘 제안; A+C+E 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10974699
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Jinhong Mo, Xiongfei Zhai, Min Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/10974699
- **Abstract**: With the continuous improvement of data memory density, as the common solution for error correction of nand flash, the low-density-parity-check (LDPC) code faces more challenges, such as the increasing code length requirements, the worse raw bit error rates (RBERs), and the frequently varied channels. In this article, a new (37536, 33672) spatially coupled and globally coupled LDPC (SC-GC-LDPC) code is constructed to address the above challenge, which outperforms the traditional globally coupled LDPC (GC-LDPC) code with the gaps of 0.065 and 0.08 dB by exploiting the layered sum-product algorithm (SPA) and the layered normalized min-sum (NMS) algorithm, respectively. In the flash channel, the SC-GC-LDPC code also shows superior error correction performance than the conventional GC-LDPC codes with 25% improvement. Due to its special structure of the check matrix, an improved two-level decoding algorithm (ITLA) and an improved two-phase decoding algorithm (ITPA) are proposed in this article. Specifically, the algorithms exploit the adjacent subcodes to correct the faulty ones, which reduces the number of check-node-updating (CNU). For the case of single subcode errors, the simulation results show that the number of CNU is reduced by ranging from 6.64% to 31.14% by applying our proposed algorithms, leading to significant improvement of throughput. Compared with the conventional algorithms, the ITLA and ITPA only show slight performance loss. Moreover, ITPA also provides high flexibility of decoding in the nand flash memory, which can achieve the balance between the error-correction performance and the throughput.

## A Multi-High-Rate Structured Algebraic QC-LDPC Code for 3D TLC NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND 플래시 채널 모델링 및 다중 고율 대수적 QC-LDPC 설계를 직접 다루는 NAND 직접 적용 논문(A+E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11028049
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Linxin Yin, Xiongfei Zhai, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/11028049
- **Abstract**: As the number of stacked layers in 3D NAND flash memory increases, the channels experience more complex noise, leading to significant fluctuations in the error detection rate. Error-correcting codes with varying error correction capabilities (ECC) are required at different flash stages. To address this issue, we investigate multi-high-rate low-density parity-check (LDPC) codes for 3D NAND flash memory in this paper. Firstly, we mathematically model the 3D triple-level cell (TLC) NAND flash channel based on the obtained data from the test platform. Then we propose a multi-high-rate structured algebraic quasi-cyclic LDPC (MHR-SA-QC-LDPC) code. Specifically, the MHR-SA-QC-LDPC code contains the fixed number of information bits and can be adjusted to various rates according to the characteristics of NAND flash channels. Both additive and multiplicative group construction methods are analyzed in the prime field. Simulation results demonstrate that the proposed LDPC codes outperform existing benchmarks in 3D TLC NAND flash channels, improving both ECC performance and device lifetime.

## Efficient Encoding Algorithm and Architecture for 2-D Quasi-Cyclic LDPC Codes With Applications to 2-D Magnetic Recording

- **Status**: ✅
- **Reason**: 2D QC-LDPC 코드의 girth 조건 기반 구성 알고리즘과 3가지 HW 아키텍처(처리량·자원 트레이드오프)가 NAND LDPC HW 구현·코드설계에 직접 이식 가능 (D/E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11142887
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Karthik Bharadwaj, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/11142887
- **Abstract**: We propose an efficient encoding algorithm and architecture for 2-D quasi-cyclic (QC) low-density parity-check (LDPC) codes. The encoding algorithm is derived based on the null space of the parity-check tensor obtained by tiling random permutation tensors satisfying certain girth constraints toward improved error correction performance. Our contributions are threefold. First, the construction of 2-D LDPC codes is generalized to accommodate random tilings of permutation tensors, providing code design flexibility over prior work based on predefined shifts. We provide the conditions for obtaining girth greater than four and six, useful for deriving the parity-check tensor of the code algorithmically. Second, based on the parity-check tensor, the generator tensor of the 2-D code is derived. We prove that the generator tensor of a 2-D code whose parity-check tensor has the same i-shifts within each block row, regardless of the j-shifts, comprises tiles of circulant tensors, useful for hardware realization. Third, three different hardware architectures that trade off hardware resources with speed and throughput are proposed. Finally, we analyze the performance of the code via simulations. The proposed 2-D codes are capable of correcting random errors and cluster errors by design. Specifically, for a 2-D LDPC code of rate 0.5 and size 50  $\times$  100, the proposed approach with random shifts along with layered decoding achieves a 0.7 dB signal-to-noise ratio (SNR) gain for random errors at a code failure rate (CFR) of 10−5 and a 1.8 dB SNR gain for burst errors, compared to non-layered decoding with predefined shifts.

## Rank Analysis and Its Applications for Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: QC-LDPC 패리티 검사 행렬의 랭크 분석 및 코드 설계 적용을 다루며, 마스킹 기법과 부호 설계 절차에 직접 활용 가능 — E(QC-LDPC 코드 설계) 해당.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11168913
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Po-Chun Yang, Chung-Hsuan Wang, Chi-chao Chao
- **PDF**: https://ieeexplore.ieee.org/document/11168913
- **Abstract**: In this paper, we develop a new approach for rank analysis of parity-check matrices for quasi-cyclic low-density parity-check codes based on the associated polynomials of circulant matrices, applicable to general finite fields and arbitrary circulant sizes. Some formulas on the rank for parity-check matrices with one, two, and three row-blocks are first derived. For the general case with arbitrary numbers of row-blocks, lower and upper bounds on the rank are presented, and these bounds can be combined to give the exact rank result under certain conditions. We also investigate the effect on the rank by changing the circulant size. Furthermore, we study the relations between the rank of the masked matrix and that of the masking matrix, which can be used to predict the rank of the parity-check matrix after masking. The obtained rank analysis results are then applied to several classes of existing algebraically constructed parity-check matrices, along with their masked matrices. Finally, we demonstrate how rank analysis can be used in the code design procedure.

## Multiple-Resolution Decoding Architecture for QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 LLR 비트폭 동적 조정 SIMD 다중해상도 디코딩 HW 아키텍처로, 5G NR 대상이나 QC-LDPC VLSI 설계 기법은 NAND 컨트롤러에 이식 가능(D+E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10994196
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: In-Cheol Park, Kangjoon Choi, Hyejung Jang +1
- **PDF**: https://ieeexplore.ieee.org/document/10994196
- **Abstract**: This paper proposes a hardware-efficient multiple-resolution decoding architecture for quasi-cyclic low-density parity-check (QC-LDPC) codes, specifically designed to meet the stringent requirements of the 5G New Radio (NR) standard. The proposed architecture adopts a single-instruction multiple-data (SIMD) approach to dynamically adjust the bitwidth of log-likelihood ratio (LLR) values based on the  $Eb/N_{0}$  condition, significantly reducing hardware complexity and improving throughput area ratio. Unlike conventional single-resolution decoders, the architecture processes 2-bit LLR values in high  $Eb/N_{0}$  regions and scales up to 4-bit or 8-bit LLR values for moderate and low  $Eb/N_{0}$  conditions, maintaining robust error-correcting performance. Key innovations include SIMD-based design for variable-node units (VNUs), check-node units (CNUs), and quasi-cyclic shifting networks (QSNs), as well as optimized memory access scheduling to support all 51 lifting sizes defined in the 5G NR standard. Designed in a 65-nm CMOS process, the decoder achieves a peak throughput of 27.24 Gbps under error-free conditions with a throughput area ratio improvement of  $2.07\times $  compared to the state-of-the-art designs. Furthermore, the proposed architecture demonstrates superior throughput-area ratio and flexibility, supporting all code rates and lifting sizes specified in the 5G NR standard. Simulation results confirm that the proposed decoder meets the peak throughput requirement under error-free conditions, while maintaining robust performance in challenging channel environments.

## Efficient Schemes and Architectures for Check Node Update in Shuffled Min-Sum Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: Shuffled Min-Sum LDPC의 체크노드 업데이트에 λMDQ 기법을 적용해 면적 최대 79%, 지연 70% 감소, 처리량 229% 향상을 달성한 이식 가능 HW 아키텍처(C+D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11003883
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Lisha Luo, Xuan He, Qin Du +3
- **PDF**: https://ieeexplore.ieee.org/document/11003883
- **Abstract**: By dividing Variable Nodes (VNs) into groups and processing groups sequentially, the Shuffled Min-Sum (SMS) decoding of Low-Density Parity-Check (LDPC) codes achieves a good trade-off between hardware resource and throughput. However, under the grouping strategy where at least one Check Node (CN) has multiple VN neighbors in one group, the CN update of State-Of-The-Art (SOTA) SMS decoding has long latency and high complexity. To address the issue, this paper presents two efficient CN update schemes. The first one uses the first two minimum Variable-to-Check (V2C) message magnitudes in each group and a size- $\lambda $  Monotone Double-ended Queue ( $\lambda $ MDQ), leading to an Improved  $\lambda $ MDQ (I- $\lambda $ MDQ) scheme. The second one called the Modified  $\lambda $ MDQ (M- $\lambda $ MDQ) scheme uses only the minimum in each group. As a result, our schemes reduce the number of Selection Modules (SMs) required by the CN update to only one. Simulation results show that both of our schemes have comparable error-correction performance to the SOTA schemes. Furthermore, we simplify the SM via a decomposition design and also present the detailed hardware architectures for our schemes. Analysis using the 90nm CMOS technology library shows that, compared to the SOTA schemes, our I- $\lambda $ MDQ scheme reduces the area and latency by up to 75% and 72%, respectively, while improving the throughput by up to 254%. Similarly, our M- $\lambda $ MDQ scheme reduces the area and latency by up to 79% and 70%, respectively, and improves the throughput by up to 229%.

## Generalized LDPC Codes With Low-Complexity Decoding and Fast Convergence

- **Status**: ✅
- **Reason**: GLDPC 코드의 Min-Sum 디코더 변형 및 protograph 기반 양자화 density evolution 최적화 기법이 이식 가능한 디코더 알고리즘·코드설계(C/E)로, 5G LDPC 대비 수렴 성능 개선 결과 포함.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11131149
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Dawit Simegn, Dmitry Artemasov, Kirill Andreev +2
- **PDF**: https://ieeexplore.ieee.org/document/11131149
- **Abstract**: We consider generalized low-density parity-check (GLDPC) codes with component codes that are duals of Cordaro–Wagner codes. Two efficient decoding algorithms are proposed: one based on Hartmann–Rudolph processing, analogous to Sum-Product decoding, and another based on evaluating two hypotheses per bit, referred to as the Min-Sum decoder. Both algorithms are derived using latent variables and a appropriate message-passing schedule. A quantized, protograph-based density evolution procedure is used to optimize GLDPC codes for Min-Sum decoding. Compared to 5G LDPC codes, the proposed GLDPC codes offer similar performance at 50 iterations and significantly better convergence and performance at 10 iterations.

## Nested Root-Protograph LDPC-Coded Multilevel-Priority IR-HARQ Systems: A New Design for Multi-Stream Transmissions With Non-Ergodic Block Fading

- **Status**: ✅
- **Reason**: NRP-LDPC 코드의 full-diversity 구성 및 rate compatibility 설계 방법론이 이식 가능한 코드설계 기법(E)이며, 유한 블록 길이 성능 분석도 NAND LDPC 설계에 활용 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11079685
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Zhaojie Yang, Xiaoxi Yu, Yaoyue Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/11079685
- **Abstract**: To enhance the adaptability and performance of multi-stream transmissions over non-ergodic block fading (BF) channels, this paper studies a multilevel-priority incremental-redundancy hybrid ARQ (MP-IR-HARQ) system with nested root-protograph-based low-density parity-check (NRP-LDPC) codes. Specifically, we analyze the performance of traditional RP-LDPC codes and reveal that they are unable to achieve full diversity in the IR-HARQ system over non-ergodic BF channels. To address this limitation, we propose a design methodology to construct a family of NRP-LDPC codes having the full-diversity property, throughput-limit-approaching property, outage-limit-approaching performance, and rate compatibility tailored for the IR-HARQ system. Additionally, we incorporate a multilevel-priority design composed of the adaptive modulation, adaptive detection, and successive decoding into the traditional IR-HARQ framework. The designed MP-IR-HARQ system can support the transmission of multiple data streams while providing unequal error protection (UEP) across them. The outage-boundary analyses, throughput analyses, and word-error-rate (WER) simulations demonstrate that the proposed NRP-LDPC-coded MP-IR-HARQ system can not only significantly outperform prior-art counterparts over non-ergodic BF channels, but also enable the multi-data-stream-based UEP transmission.

## An Analysis and Design of Rate-Dependent Nested Scheduling in Layered Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 5G NR LDPC 코드의 레이어드 BP 디코딩을 위한 레이트 의존 중첩 스케줄링 설계로, 레이어드 디코더 스케줄링 개선 기법(C)이 NAND 플래시 LDPC 디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11069260
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Dongxu Chang, Ke Liu, Guanghui Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/11069260
- **Abstract**: In this study, we analyze the characteristics of scheduling sequences for layered belief propagation (LBP) that can result in efficient decoding of low-density parity-check (LDPC) codes. Specifically, we claim that scheduling sequences leading to high decoding efficiency should prioritize updating check nodes with lower error probabilities aggregated from neighboring variable nodes. We prove this conclusion separately on both the BEC and the BI-AWGN channels. Some observable characteristics in “good” scheduling sequences regarding row weights, rows connected to punctured columns, and column weights can serve as corollaries to this conclusion. By comprehensively considering these characteristics of good scheduling, we design a multi-sequence nested scheduling scheme of layered decoding for 5G New Radio (NR) LDPC codes. The proposed schemes can obtain scheduling sequences for various rates of rate-compatible LDPC codes using small hardware storage. What’s more, by respectively storing double-sequence, triple-sequence, or more sequences to obtain scheduling sequences at various code rates, a trade-off can be made between decoder storage and decoding performance. Experimental results demonstrate that the proposed scheme achieves performance improvements compared to existing scheduling schemes at nearly all code rates.

## Protomatrix-Based LDPC Codes for Continuous Phase Modulation

- **Status**: ✅
- **Reason**: protomatrix 기반 LDPC 코드 설계 방법론(PEXIT 탐색, error floor 제거를 위한 2단계 lifting, check node splitting) 및 고처리량 디코더 구조가 NAND LDPC ECC 코드설계·디코더에 이식 가능 (E/C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11071260
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Erik Perrins
- **PDF**: https://ieeexplore.ieee.org/document/11071260
- **Abstract**: This paper develops a design methodology for constructing protomatrix-based low-density parity-check (LDPC) codes that are paired with (matched to) continuous phase modulation (CPM) waveforms. We show how a protomatrix extrinsic information transfer (PEXIT) based search can yield lower decoding thresholds than previously reported, and how a single constraint added to this search is effective at preserving the linear minimum distance growth property while remaining within one dB of capacity. We show that a two-stage lifting procedure plays an essential role in completely eliminating error floors at very low error rates. Our high-throughput joint LDPC–CPM decoder is demonstrated to be practical with execution speeds comparable to a standalone LDPC decoder. The global iterations of the joint decoder are shown to provide natural protection against undetected errors due to small minimum distance, and this protection is further enhanced by a novel check node “splitting” technique. The diverse family of three CPM waveforms that are used in aeronautical telemetry are considered as design examples.

## On Generalized Reed-Solomon Codes

- **Status**: ✅
- **Reason**: 일반화 RS 코드에 LC-OSD(ordered statistics decoding with local constraints) 알고리즘을 제안하며, OSD 계열 알고리즘은 LDPC 디코딩에도 이식 가능(C); JSCC 결합 부분은 Phase 3 재검토 필요
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11007566
- **Type**: journal
- **Published**: Nov. 2025
- **Authors**: Xiangping Zheng, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/11007566
- **Abstract**: In this paper, we prove that the generalized Reed-Solomon (RS) codes are capacity-achieving over binary-input output-symmetric (BIOS) channels, in terms of frame error rate (FER) under maximum likelihood (ML) decoding. In the finite-length region, we present the ordered statistics decoding with local constraints (LC-OSD) algorithm for the generalized RS codes. In particular, the extended most reliable basis (MRB) is derived based on a systematic matrix calculated by the parallel Lagrange interpolation, accelerating the conventional Gaussian elimination (GE). Additionally, we propose a joint source-channel coding (JSCC) scheme that incorporates generalized RS codes and classified enumerative (CE) coding, where the partition of the source is optimized by the k-means++ clustering algorithm. At the transmitter, we implement the CE coding to encode the source information. Then the variable-length codeword of the CE coding is transformed into a fixed-length codeword by the multiple-rate generalized RS encoding and superimposed with a class label for transmission. At the receiver, parallel LC-OSD is performed to recover the source. Simulation results demonstrate that the proposed JSCC scheme outperforms the double polar JSCC scheme (exhibiting a coding gain of up to 1.4 dB) and the JSCC scheme based on polarizing matrix extension (exhibiting a coding gain of up to 0.6 dB), as predicted by Gallager’s JSCC bound.

## Adaptive Layered Enhanced Min-Sum Decoding for Short-Block LDPC Codes in Low-SNR and Burst-Prone Communication Systems

- **Status**: ✅
- **Reason**: 적응형 레이어드 Min-Sum(정규화·오프셋 보정, 조기종료) 디코더 알고리즘이 QC-LDPC 호환으로 NAND LDPC 디코더에 직접 이식 가능(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11455032
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: Guangyi Luo, Dasheng Zhao, Yidu Zhang
- **PDF**: https://ieeexplore.ieee.org/document/11455032
- **Abstract**: Low-bitrate voice and telemetry systems require short LDPC codes with low decoding complexity. This paper presents ALEMS, an Adaptive Layered Enhanced Min-Sum framework for short codes operating under low SNR and bursty conditions. ALEMS combines layered scheduling for fast convergence, an improved Min-Sum core with normalized or offset correction, and adaptive control with an early-stopping policy. These techniques retain the simplicity of Min-Sum decoding while reducing message saturation and trapping effects common in short codes. Simulations using rate-1/2 short LDPC codes over AWGN and Gilbert-Elliott channels show consistent BER and FER gains over normalized Min-Sum and sum-product algorithms, together with fewer iterations and lower stall probability. Under bursty conditions, modest interleaving further enhances robustness without added cost. Fully compatible with QC-LDPC structures and fixed-point realizations, ALEMS offers a balanced solution between theoretical reliability and hardware efficiency for short-block, low-rate applications such as digital voice and narrowband modems.

## FPGA Implementation of 5G NR QC-LDPC Codes

- **Status**: ✅
- **Reason**: 5G NR QC-LDPC FPGA 인코더 — 병렬 순환이동 네트워크·파이프라인 HW 아키텍처가 NAND LDPC 컨트롤러 HW 설계에 이식 가능(D).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11350474
- **Type**: conference
- **Published**: 7-8 Nov. 2
- **Authors**: Susan G Varghese, Rishika Prabeed Kumar, Inshal Hamidi
- **PDF**: https://ieeexplore.ieee.org/document/11350474
- **Abstract**: The rapid development of $\mathbf{5 G}$ communications technology has triggered higher demands for efficient error correction techniques to meet the needs of ultra-reliable, low-latency, and high-throughput data transmission. Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes have been chosen as the 5 G New Radio (NR) standard because they can overcome conventional error correction techniques. These codes are crucial to enable enhanced Mobile Broadband (eMBB) and Ultra-Reliable Low Latency Communication (URLLC) applications by providing strong data integrity with low processing requirements. Nevertheless, hardware implementation of QC-LDPC encoding is extremely challenging because of its high computational complexity and need for adaptability to enable a wide range of code rates and block sizes. This paper is focused on designing and implementing a low-latency, high-throughput QC-LDPC encoder based on FPGA technology that overcomes these issues through optimized algorithms and architectural advancements. The approach encompasses the study of 5 G NR encoding needs, the development of an extremely parallel QC-LDPC encoding algorithm, and implementation on a programmable hardware platform. The encoder features pipeline optimization and parallel cyclic shift networks for enhancing efficiency. The design is synthesized in Verilog HDL and implemented on Nexys 4 DDR FPGA board to support various base graph configurations and lift sizes needed by 5G NR requirements. FPGA testing shows significant improvements in encoding latency, throughput, and resource utilization. With the realization of a fully functional and adaptive encoding chain, this research offers a high-performance and scalable solution for 5G applications and facilitates the development of next-generation wireless communication systems.

## FPGA-based Implementation of Low-Complexity QC-LDPC for Real-Time 50G-PON Systems

- **Status**: ✅
- **Reason**: QC-LDPC의 FPGA 기반 저복잡도 코덱 구현(D/E)으로 NAND LDPC 디코더 HW 설계에 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11350830
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Kim KwangOk, Doo KyeongHwan, Chung HwanSeok
- **PDF**: https://ieeexplore.ieee.org/document/11350830
- **Abstract**: A low-complexity QC-LDPC codec for high-speed 50G-PON is implemented on FPGA-based OLT and ONU prototypes. The proposed QC-LDPC achieves 50 Gbps performance with reduced hardware resource utilization. An optical gain of about 8.7 dB and error-free 40 Gbps transmission are demonstrate through real-time testing.

## Hybrid Check Generalized LDPC Convolutional Codes for Optical Fiber Communications

- **Status**: ✅
- **Reason**: HC-GLDPC-CC의 BCH 컴포넌트 결합 코드 설계(E)와 FPGA 기반 에러 플로어 구현(D)이 NAND LDPC ECC에 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11350500
- **Type**: conference
- **Published**: 5-8 Nov. 2
- **Authors**: Yinlong Shi, Kai Tao, Zitao Wei +5
- **PDF**: https://ieeexplore.ieee.org/document/11350500
- **Abstract**: With the increasing throughput in optical fiber communication networks, Forward Error Correction (FEC) design plays a crucial role in countering channel noise and interference. To improve the BER performance, we construct a class of 28%-overhead HC-GLDPC-CCs with the BCH codes as component code. In this paper, we investigate the effects of code length, the number of iterations, and the proportion of GC nodes on GLDPC codes with software implementation, and emulate the error floor performance with FPGA platform. As shown in the FPGA simulation result, the error floor of the concatenated code with 24 iterations is below 10-15 for an input BER of 4.51e-2, and the net coding gain(NCG) is 12.28dB.

## Decoding of Generalized LDPC Codes Using the BCJR Algorithm

- **Status**: ✅
- **Reason**: GLDPC를 QC-LDPC로 구성+BCJR을 BP에 통합한 디코더 알고리즘, NAND LDPC에 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11301108
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Alexey A. Bandyukov, Andrey A. Metlyakov, Fedor I. Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/11301108
- **Abstract**: Generalized low-density parity-check (GLDPC) codes have emerged as a promising class of error-correcting codes that extend the capabilities of traditional LDPC codes by incorporating more powerful component codes. This paper investigates an approach to construct long GLDPC codes using short component codes. In this scheme, the BCJR algorithm is used as a component decoder and integrated into the belief propagation algorithm. Simulation results demonstrate that constructions incorporating quasi-cyclic LDPC codes yield the best performance. Compared to the conventional decoding approach for LDPC codes, the proposed generalized constructions demonstrated better bit and frame error rate performance. This approach is promising for communication systems that require low latency. A comparison is also provided with LDPC codes constructed using the Progressive Edge-Growth (PEG) algorithm.

## Construction of LDPC Codes for Single Bursts Correction by Masking

- **Status**: ✅
- **Reason**: 블록순환 QC-LDPC 마스킹 구성으로 버스트 정정능력 개선, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11301552
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Alina Veresova, Andrei Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/11301552
- **Abstract**: This paper addresses the problem of constructing codes for correcting single error bursts. The construction is based on a block-circulant design of low-density parity-check codes. For such a design, the maximal correctable burst length is limited by the block size, which forces consideration of codes whose parity-check matrix contains only a small number of large blocks. However, this significantly restricts the attainable sets of code lengths and code rates, and, aside from a few special cases, such codes may be turned out to be rather far from the Reiger bound on the maximum correctable burst length. To overcome these limitations we introduce a masking procedure and propose a method for constructing a masking matrix based on evaluating the burst correcting capability of a code. Experiments estimating the correcting capability of the proposed codes in comparison with both the original block-circulant construction and with random codes defined by dense parity-check matrices were performed. The proposed methodology provides quasicyclic low-density parity-check codes whose correcting capability substantially exceeds that of block-circulant codes without zero subblocks and, for certain parameter choices, approaches the Reiger bound. The resulting codes also provide greater flexibility in varying the number and size of blocks, enabling more versatile adjustment of code lengths and code rates. Finally, the burst correcting capability of the proposed construction is comparable to that of codes defined by dense parity-check matrices, while its quasi-cyclic structure enables more computationally efficient encoding and decoding procedures.

## On the Correcting Capability of Hard-Decision Error-and-Erasure Iterative Decoding of LDPC Codes for Data Storage

- **Status**: ✅
- **Reason**: NAND 플래시 SSD의 error-erasure LDPC 반복디코딩 능력 분석, 코드·디코더 설계 가이드(A/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11301418
- **Type**: conference
- **Published**: 5-7 Nov. 2
- **Authors**: Vladimir Kuzmin, Ilia Chevtaev, Maya Chernaya +2
- **PDF**: https://ieeexplore.ieee.org/document/11301418
- **Abstract**: Modern storage systems such as NAND flash solidstate drives are increasingly exposed to channels where both errors and erasures coexist. Classical Reed-Solomon (RS) codes provide strong error-and-erasure protection but suffer from high decoding complexity and latency, limiting their applicability in high-throughput storage architectures. Low-Density ParityCheck (LDPC) codes, with iterative message-passing decoders, offer near-capacity performance at low complexity and are therefore the preferred solution in practice. While the decoding behavior of LDPC codes has been well studied for pure error or pure erasure channels, the mixed error-and-erasure case has received less attention, despite its direct relevance to storage. In this work, we analyze the potential correction capability of iterative error-and-erasure decoding for LDPC codes under hard-decision channels. Using density evolution, we derive recursion equations for the joint evolution of error and erasure probabilities and establish bounds on the region of correctable error-erasure patterns. The presented results provide theoretical correction bounds that complement existing studies on error-only and erasure-only channels, and offer guidelines for LDPC code and decoder design in storage systems where errors and erasures naturally coexist.

## An Implementation Method of a Ultra-High Speed Variable Block Code Data Encoding and Decoding Structure

- **Status**: ✅
- **Reason**: FPGA 초고속 가변 블록 병렬 인코딩/디코딩 구조(LDPC 포함), 이식 가능 HW 아키텍처(D) 가능성, 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11398590
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Qiang Zhang, Qi Shan, Zhenyu Song
- **PDF**: https://ieeexplore.ieee.org/document/11398590
- **Abstract**: With the increase of satellite communication data, the modem in the ground application system is required to have a higher codec rate and communication capacity. This paper proposes a method for implementing an ultra-high speed variable block code data encoding and decoding structure, which supports serial frame input of correlated ultra-high speed block code data, completes ultra-high speed parallel encoding and decoding, and achieves independent and stable output of ultra-high speed data serial frames. The method proposed in this paper is applicable to FPGA based ultra-high speed variable block code data encoding and decoding, compatible with various block codes such as LDPC, RS, BCH, and multi rate encoding and decoding; Adopting a parallel structure processing approach to rapidly improve the modem throughput of satellite ground application systems; The software calculates the number of parallel loop modules for highspeed data caching, drives the loading of corresponding FPGA bitstreams, quickly reconstructs FPGA encoding and decoding structures, flexibly allocates resources, and improves resource utilization.

## Design and Implementation of an Efficient Parallel Decoding Algorithm for Regular LDPC Codes with Girth Length of Eight

- **Status**: ✅
- **Reason**: BIBD 기하 기반 girth-8 정규 LDPC 구성 + 균일포맷 표준화로 HW 복잡도/지연 감소하는 병렬 디코더 FPGA 구현. 이식 가능한 코드설계+HW 기여(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11512606
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yanjun Ji, Xiao Ji Wei, Qinwei Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/11512606
- **Abstract**: The rapid expansion of the Internet of Things (IoT), robotics, and automated control systems has created a critical demand for high-throughput, low-latency wireless communication. This paper presents the hardware implementation of an efficient parallel decoding algorithm for regular Low-Density Parity-Check (LDPC) codes, constructed with a girth of eight to avoid short cycles. The codes are constructed using a geometric approach based on balanced incomplete block designs (BIBD) to ensure a minimum girth of eight. The design was developed using geometric methods, implemented on the Quartus platform with Verilog Hardware Description Language (HDL), and includes the circuit design and simulation for core modules. Synthesized and deployed on a Stratix II FPGA (EP2S90F1020C3), the decoder achieves a maximum data processing rate of 10 Mbps with robust error correction capabilities. A key innovation is the standardization of all internal information in the decoding process to a uniform format, which eliminates the need for additional data conversion, thereby reducing hardware complexity and computational delay. This makes the design particularly suitable for real-time applications in IoT and robotic systems. In summary, the proposed decoder achieves a 25% reduction in clock cycles for check node updates and a processing throughput of 10 Mbps on FPGA hardware. This work demonstrates a practical and efficient decoding solution that meets the stringent requirements of modern real-time communication systems in IoT and robotics.

## A Performance-Aware Framework For LDPC Code Enhancement Using Shortening Techniques

- **Status**: ✅
- **Reason**: RedCap용 LDPC 단축(shortening)으로 CN 차수 감소해 디코더 복잡도/메모리 절감 — 이식 가능한 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11430116
- **Type**: conference
- **Published**: 12-13 Nov.
- **Authors**: Bhawna Kamra, Ankit Srivastav, Vamshidhar Kamuganti +1
- **PDF**: https://ieeexplore.ieee.org/document/11430116
- **Abstract**: In Release 15, 3GPP introduced the New-Radio $(5 \mathrm{G})$ wireless technology to support a wide range of use-cases across industries into three main service types: enhanced mobile broadband (eMBB), ultra reliable low latency communication (uRLLC) and massive-machine type communication (mMTC). However, numerous emerging use-cases exhibit requirements that lie in between the defined boundaries of the aforementioned service types. These use-cases do not demand the complete capabilities offered by full-fledged 5 G networks. To address such use-cases, in Release 17, 3GPP introduced the reduced capability NR devices (RedCap) as a tailored solution. The standardized low-density parity check (LDPC) scheme lacks the necessary optimizations for low-complexity hardware requirements for the RedCap Devices. In this paper, a customized LDPC code design framework is proposed to meet the low-complexity requirements of NR RedCap devices, while maintaining acceptable BER levels. Specifically, a shortening technique is implemented to reduce the check node (CN) degree, thereby inherently minimizing both decoder complexity and memory requirements. Shortening method must be meticulously selected to avoid significant performance loss, while maintaining the desired properties like girth and sparsity. Simulation results demonstrate that the achieved BER performance remains within the permissible range recommended by the standard for NR RedCap devices with Check node degree reduction.

## On the Design, Performance Assessment, and Implementation of Channel codes for improving information integrity in data storage systems

- **Status**: ✅
- **Reason**: NAND 플래시 채널 모델링 + 고전/현대 ECC 합성·구현 — NAND/스토리지 직접(A/B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11288988
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Achala G, U. Shripathi Acharya, Pathipati Srihari
- **PDF**: https://ieeexplore.ieee.org/document/11288988
- **Abstract**: NAND flash is the primary storage technology in most modern electronic devices. Its evolution has been driven by scaling to increase bit density per cell, which has led to high raw bit error rates (RBER) and reduced data integrity. Multi-level flash devices have greater complexity and even higher RBER. Addressing this requires designing accurate channel models and error correction coding (ECC) algorithms tailored to these models. Our research focuses on modeling the NAND flash channel and synthesizing, implementing both classical and modern ECC techniques optimized for NAND flash architectures, enhancing reliability in contemporary storage systems.
