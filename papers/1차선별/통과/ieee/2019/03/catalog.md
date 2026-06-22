# IEEE Xplore — 2019-03 (1차선별 통과)


## Performance Analysis of Practical QC-LDPC Codes: From DVB-S2 to ATSC 3.0

- **Status**: ✅
- **Reason**: E: QC-LDPC SNR loss 분석법 + raptor-like 구조 신규 코드설계, 바이너리, 베이스행렬·유한길이 분석 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8554116
- **Type**: journal
- **Published**: March 2019
- **Authors**: Shuang Chen, Kewu Peng, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/8554116
- **Abstract**: In this paper, a new analysis method is introduced to predict the gap between Shannon limit and successful decoding signal-to-noise ratio threshold (SNR loss) of practical quasi-cyclic low-density parity check (QC-LDPC) codes. The SNR loss of a QC-LDPC code is summed up from three aspects: 1) the base matrix; 2) the number of iterations for decoding; and 3) the finite codeword length. As an example, the SNR loss of DVB-S2 and ATSC 3.0 LDPC codes is analyzed with the proposed method. Results show that a large portion of the SNR loss of DVB-S2 LDPC codes is due to their base matrices, which is significantly improved in latest ATSC 3.0 standard. Furthermore, with the aid of the proposed analysis method, newly designed QC-LDPC codes with raptor-like structure are proposed. Bit-error rate simulations show that the proposed codes are only 0.4 dB away from Shannon limit under binary-input additive white Gaussian noise channel and only 0.65 dB away from Shannon limit under binary-input Rayleigh fading channel, which are comparable with state-of-art design.

## Analysis of the Joint Viterbi Detector/Decoder (JVDD) Over a Coded AWGN/ISI System ss an LDPC Alternative

- **Status**: ✅
- **Reason**: JVDD를 LDPC 대안으로 DE/EXIT 유사 분석. LDPC SPA 분석 도구 맥락이라 애매하나 살림(Phase3 재검토).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8434235
- **Type**: journal
- **Published**: March 2019
- **Authors**: Kheong Sann Chan, Susanto Rahardja
- **PDF**: https://ieeexplore.ieee.org/document/8434235
- **Abstract**: The joint Viterbi detector/decoder (JVDD) has been proposed as an alternative to the powerful and ubiquitous low-density parity check (LDPC) coding schemes, that are used in the majority of channel coding applications today. At shorter block lengths, the JVDD is able to outperform the state-of-the-art LDPC decoder that can be found in many of today's systems, from deep-space communications to the digital video broadcasting standard, to the advanced television standard committee 3.0. Researchers have developed the tools to analyze the performance of the LDPC decoder, which is known as the sum-product algorithm or message passing algorithm. These tools include density evolution (DE) and extrinsic information transfer (EXIT) charts. To date, no similar such analysis exists for the JVDD. In the current paper we perform a similar preliminary analysis on the JVDD algorithm akin to what DE and EXIT charts are for the LDPC decoder. The current new analysis of the JVDD allows prediction of its probability of error based on the probability distribution functions of the metrics used within the algorithm. Our analysis plays a similar role to the abovementioned tools developed for the LDPC decoder: it allows us to predict the performance of the JVDD under various conditions (such as varying SNR's, thresholds, and block lengths), it improves our understanding of the JVDD algorithm and the match against Monte-Carlo simulations verifies our assumptions on the main error-causing mechanisms within the JVDD.

## An Efficient Post-Processor for Lowering the Error Floor of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC error floor 저감 post-processor(ESPP)와 HW 아키텍처(C/D/E). NAND 저BER 요구에 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8395069
- **Type**: journal
- **Published**: March 2019
- **Authors**: Hangxuan Cui, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8395069
- **Abstract**: Error floor is one major reason for limited use of low-density parity-check (LDPC) codes in applications requiring very low bit error rate. In this brief, an efficient erasure searching post-processor (ESPP) is proposed to lower the error floor of LDPC codes. Here, when a decoding failure is detected, the most unreliable symbols in the decoder output vector are erased, then their values are re-calculated by solving a system of linear equations with a sparse coefficient matrix. Compared to the state-of-the-art post processors, the ESPP has much lower computation complexity. Simulation results show that the proposed method significantly improves the decoding performance of LDPC codes in the error-floor region. Additionally, a well-optimized hardware architecture is developed for the proposed post-processor. Algorithmic transformation and architecture optimization are well explored to reduce the hardware complexity and latency. Synthesis results demonstrate the effectiveness of the proposed architecture.

## LDPC Codes Over the BEC: Bounds and Decoding Algorithms

- **Status**: ✅
- **Reason**: E/C: 유한길이 LDPC ML/near-ML 디코딩 분석 + QC-LDPC용 저복잡도 near-ML 디코더 신규 제안, 바이너리 LDPC, NAND 코드설계/디코더 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8519768
- **Type**: journal
- **Published**: March 2019
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek +2
- **PDF**: https://ieeexplore.ieee.org/document/8519768
- **Abstract**: The performance of maximum-likelihood (ML) decoding on the binary erasure channel for finite-length low-density parity-check (LDPC) codes from two random ensembles is studied. A tightened union-type upper bound on the ML decoding error probability based on the precise coefficients of the average weight spectrum is presented. For LDPC codes from the Gallager ensemble and the Richardson-Urbanke ensemble, new upper bounds on the ML decoding performance based on computing the rank of submatrices of the code parity-check matrix are derived. A new lower bound on the ML decoding threshold followed from the latter error probability bound is obtained. An improved lower bound on the error probability for codes with a known estimate on the minimum distance is presented as well. A new low-complexity near-ML decoding algorithm for quasi-cyclic LDPC codes is proposed and simulated. Its performance is compared to the simulated belief propagation and ML decoding performance and simulated performance of the best known improved iterative decoding techniques, as well as, with the derived upper bounds on the ML decoding performance and with decoding thresholds obtained by the density evolution technique.

## BP-LED Decoding Algorithm for LDPC Codes Over AWGN Channels

- **Status**: ✅
- **Reason**: LDPC용 BP-list erasure 디코딩(BP-LED) 신규 디코더 알고리즘(C). 비이진 부분 있으나 바이너리 QC-LDPC BP 개선 포함.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8445606
- **Type**: journal
- **Published**: March 2019
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek +1
- **PDF**: https://ieeexplore.ieee.org/document/8445606
- **Abstract**: A new method is presented for low-complexity near-maximum-likelihood (ML) decoding of low-density parity-check (LDPC) codes over the additive white Gaussian noise channel. The proposed method termed belief-propagation-list erasure decoding (BP-LED) is based on erasing carefully chosen unreliable bits performed in case of BP decoding failure. A strategy of introducing erasures into the received vector and a new erasure decoding algorithm are proposed. The new erasure decoding algorithm, called list erasure decoding, combines ML decoding over the BEC with list decoding applied if the ML decoder fails to find a unique solution. The asymptotic exponent of the average list size for random regular LDPC codes from the Gallager ensemble is analyzed. Furthermore, a few examples of irregular quasi-cyclic LDPC as well as randomly constructed regular LDPC codes of short and moderate lengths are studied by simulations and their performance is compared to the tightened upper bound on the LDPC ensemble-average performance and the upper bound on the average performance of random linear codes under ML decoding. A comparison of the BP decoding and BP-LED performance of the WiMAX standard codes and performance of the near-ML BEAST decoding are presented. The new algorithm is applied to decoding a short nonbinary (NB) LDPC code over extensions of the binary Galois field. The obtained simulation results are compared to the tightened upper bound on the ensemble-average performance of the binary image of regular NB LDPC codes.

## Adaptive Artificial Neural Network-Coupled LDPC ECC as Universal Solution for 3-D and 2-D, Charge-Trap and Floating-Gate NAND Flash Memories

- **Status**: ✅
- **Reason**: A/C: NAND 플래시(3D/2D, CT/FG) 대상 ANN 결합 LDPC ECC, 적응형 LLR/BER 추정으로 디코더 입력 개선 직접 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8599122
- **Type**: journal
- **Published**: March 2019
- **Authors**: Toshiki Nakamura, Yoshiaki Deguchi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/8599122
- **Abstract**: Adaptive artificial neural network (ANN)coupled low-density parity-check (LDPC) error-correcting code (ECC) (ANN-LDPC ECC) is proposed to increase acceptable errors for various NAND flash memories. The proposed ANN-LDPC ECC can be the universal solutions for 3-D and 2-D, charge-trap and floating-gate NAND flash memories. In 3-D NAND flash, lateral charge migration, vertical charge de-trap, inter floating-gate capacitive coupling noise, and inter word-line variations cause errors. On the other hand, in 2-D NAND flash, the charge de-trap and the harsh inter floating-gate capacitive coupling of adjacent word-lines and bit-lines cause errors. To solve these reliability problems, the proposed ANN automatically and adaptively compensates for complex memory cell errors. Moreover, the proposed ANNLDPC can reproduce the dynamic endurance and data-retention time dependence of errors. In addition, this paper evaluates the impacts of the chip-to-chip variations on the proposed ANN-LDPC. The proposed ANN-LDPC is implemented in the storage controller and can precisely and adaptively estimate bit-error rate (BER) and log-likelihood ratio (LLR). By using the precise LLR, LDPC decoder effectively corrects errors. As a result, ANN-LDPC extends the acceptable data-retention time by over 76× and 45× compared with conventional Bose-Chaudhuri-Hocquenghem (BCH) ECC in 3-D and 2-D triple-level cell (TLC) NAND flash memories, respectively.

## A (21150, 19050) GC-LDPC Decoder for NAND Flash Applications

- **Status**: ✅
- **Reason**: A/D: NAND 플래시 전용 GC-LDPC 디코더, 2단계 local/global 디코딩 + 파이프라인 PE HW 아키텍처 직접 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8528505
- **Type**: journal
- **Published**: March 2019
- **Authors**: Yen-Chin Liao, Chien Lin, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/8528505
- **Abstract**: In this paper, a (21150, 19050) globally-coupled low-density parity check (GC-LDPC) code designed for NAND flash memories is presented. The proposed LDPC code comprises three disjoint subcodes which can be decoded independently. This highly structural parity check matrix contributes to efficient decoder implementation and flexible decoding flow control. Moreover, a two-phase local/global decoding procedure optimized for the proposed GC-LDPC code is introduced. Scenarios of collaborative decoding that leverages the special code structures are discussed. In the proposed decoder architecture, the pipelined processing elements with scheduling are employed to reduce the critical path and decoding latency as well. Implemented in UMC 65 nm process, the post-layout simulation shows a maximum decoding throughput of 4.32 Gb/s with the chip area 3.376 mm2.

## Performance Analysis of Mixed-Scheduling Belief Propagation for LDPC Decoders in OFDM System under Double Fading Channels

- **Status**: ✅
- **Reason**: Mixed-scheduling BP(LBP-LR/RL 결합) 새 BP 스케줄링 기법, 부호 비의존적이라 카테고리 C 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8938879
- **Type**: conference
- **Published**: 6-8 March 
- **Authors**: Mayura Prakodrat, Thanomsak Sopon, Kidsanapong Puntsri +2
- **PDF**: https://ieeexplore.ieee.org/document/8938879
- **Abstract**: This paper presents the performance analysis of orthogonal frequency division multiplexing (OFDM) system using a mixed-scheduling belief propagation (MBP) algorithm for LDPC decoding where a double fading channels is considered. The MBP method is designed based on the LBP algorithm for the left-to-right direction (LBP-LR) and right-to-left direction (LBP-RL). Additionally, the bit error rate (BER) performance comparison of the BP, LBP, and MBP algorithms for LDPC decoding is proposed. The simulation results showed that the bit error rate (BER) performance of the MBP gave better BER than the BP and LBP algorithms, respectively.

## FPGA-Based Real-Time Soft-Decision LDPC Performance Verification for 50G-PON

- **Status**: ✅
- **Reason**: FPGA 실시간 soft-decision LDPC 성능검증(50G-PON); 떼어낼 수 있는 SD LDPC HW/디코더 기법 가능성, 애매하므로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8696463
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Mingwei Yang, Linlin Li, Xiang Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8696463
- **Abstract**: We have studied the combined use of the mother LDPC code from ongoing industrial standards and soft-decision to further improve the performance of the FEC. Through experimental measurements based on a real-time FPGA platform, we found that this approach offers ∼1.3 dB more gross coding gain.

## Improving Short-Length LDPC Codes with a CRC and Iterative Ordered Statistic Decoding : (Invited Paper)

- **Status**: ✅
- **Reason**: 단길이 LDPC + CRC + 반복 OSD 디코딩; 유한길이 코드·OSD 디코더 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8693053
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Wei Zhou, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/8693053
- **Abstract**: The following topics are dealt with: learning (artificial intelligence); optimisation; channel coding; neural nets; probability; statistical analysis; pattern classification; stochastic processes; 5G mobile communication; gradient methods.

## Protograph-Based LDPC Code Design for Probabilistic Shaping with On-Off Keying

- **Status**: ✅
- **Reason**: protograph 기반 LDPC 코드 설계; 바이너리 프로토그래프 구성 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8693049
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Alexandru Dominic Git, Balázs Matuz, Fabian Steiner
- **PDF**: https://ieeexplore.ieee.org/document/8693049
- **Abstract**: This work investigates protograph-based low-density parity-check (LDPC) codes for the additive white Gaussian noise (AWGN) channel with on-off keying (OOK) modulation. A non-uniform distribution of the OOK modulation symbols is considered to improve the power efficiency especially for low signal-to-noise ratios (SNRs). To this end, a specific transmitter architecture based on time sharing is proposed that allows probabilistic shaping of (some) OOK modulation symbols. Tailored protograph-based LDPC code designs outperform standard schemes with uniform signaling and off-the-shelf codes by 1.1 dB for a transmission rate of 0.25 bits/channel use and by 0.9 dB for 0.67 bits/channel use.

## Binary Message Passing Decoding of Product Codes Based on Generalized Minimum Distance Decoding : (Invited Paper)

- **Status**: ✅
- **Reason**: product code GMDD 기반 바이너리 메시지패싱 디코딩 알고리즘; 부호 비의존 BP 기법으로 이식 검토 여지(C, 애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8692862
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Alireza Sheikh, Alexandre Graell i Amat, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/8692862
- **Abstract**: We propose a binary message passing decoding algorithm for product codes based on generalized minimum distance decoding (GMDD) of the component codes, where the last stage of the GMDD makes a decision based on the Hamming distance metric. The proposed algorithm closes half of the gap between conventional iterative bounded distance decoding (iBDD) and turbo product decoding based on the Chase-Pyndiah algorithm, at the expense of some increase in complexity. Furthermore, the proposed algorithm entails only a limited increase in data flow compared to iBDD.

## Spatially Coupled LDPC Codes and the Multiple Access Channel

- **Status**: ✅
- **Reason**: SC-LDPC 코드 설계+윈도우 디코더, DE 분석; 바이너리 SC-LDPC 구성·디코더 기법 이식 가능(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8692899
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Sebastian Cammerer, Xiaojie Wang, Yingyan Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/8692899
- **Abstract**: We consider spatially coupled low-density parity-check (SC-LDPC) codes within a non-orthogonal interleave division multiple access (IDMA) scheme to avoid cumbersome degree profile matching of the LDPC code components to the iterative multi-user detector (MUD). Besides excellent decoding thresholds, the approach benefits from the possibility of using rather simple and regular underlying block LDPC codes owing to the universal behavior of the resulting coupled code with respect to the channel front-end, i.e., the iterative MUD. Furthermore, an additional outer repetition code makes the scheme flexible to cope with a varying number of users and user rates, as the SC-LDPC itself can be kept constant for a wide range of different user loads. The decoding thresholds are obtained via density evolution (DE) and verified by bit error rate (BER) simulations. To keep decoding complexity and latency small, we introduce a joint iterative windowed detector/decoder imposing carefully adjusted sub-block interleavers. Finally, we show that the proposed coding scheme also works for Rayleigh channels using the same code with tolerable performance loss compared to the additive white Gaussian noise (AWGN) channel.

## Performance of Self-Corrected Min-Sum Decoding Algorithm for Decoders with Quantized Input

- **Status**: ✅
- **Reason**: 양자화 입력 self-corrected min-sum 디코딩; NAND LLR 양자화에 직접 이식 가능한 디코더 기법(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8717757
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Aleksei Kharin, Igor Volkov, Aleksei Ovinnikov +2
- **PDF**: https://ieeexplore.ieee.org/document/8717757
- **Abstract**: In this paper we explore the Min-Sum decoding algorithm for LDPC codes with self-correction (SC-MS) modification and how it affects the error correction performance for quantized input data. Three levels of quantization are observed: 3-, 2- and 1-bit.It was shown that the self-corrected modification significantly improves the performance of Min-Sum decoding algorithm with quantized input in comparison with basic Min-Sum decoding algorithm. Convergence of the algorithm is also better than for basic Min-Sum algorithm.Results of error correction performance and convergence are presented for two codes: CCSDS (8176, 7156) and IEEE 802.3an (2048, 1723) LDPC. The results are also presented for the SC APP-based and basic Min-Sum decoding algorithms.

## Scaling the Fast x86 DVB-S2 Decoder to 1 Gbps

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 디코더의 소프트웨어(멀티코어/GPP) 구현·스케일링·캐시 병목 분석 — 이식 가능 HW/구현 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8742225
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Eugene Grayver
- **PDF**: https://ieeexplore.ieee.org/document/8742225
- **Abstract**: Software implementation of LDPC decoders has been an active area of development for the last 10 years. Researchers have focused on implementing the computationally expensive algorithm on both GPPs and GPUs. A major leap in performance was reported in the groundbreaking paper by Bertrand le Gal [2]. This paper builds on the work in [2] by considering the scaling of that implementation on modern many-core processors. We look at the performance of LDPC code specified in the DVB-S2 standard. The large block size of the DVB-S2 code makes the memory architecture of the processor just as important as the clock rate and instruction set. We present results for two generations of Intel Xeons, an Intel Phi (KNL), the recently released AMD EPYC. The key finding is that performance scaling is limited by the amount of available cache memory rather than the number of cores. We also find that heavily multi-threaded, but deterministic software architecture benefits from explicit allocation of threads to cores vs. allowing the operating system to manage threading. The maximum throughput of 1 Gbps was achieved on a mid-range AMD server - issuing a new era of all-software receivers for very high rate waveforms. We also present the performance of the algorithm ported to a low-power ARM processor and compare that to a low-end Intel Core.
