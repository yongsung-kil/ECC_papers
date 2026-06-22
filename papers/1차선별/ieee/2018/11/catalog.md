# IEEE Xplore — 2018-11 (1차선별 통과)


## Reduced Complexity Window Decoding of Spatially Coupled LDPC Codes for Magnetic Recording Systems

- **Status**: ✅
- **Reason**: SC-LDPC sliding window 디코딩 복잡도 저감(non-uniform schedule, block 재사용) - 바이너리 코드설계/디코더 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8401538
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8401538
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes have emerged to possess capacity-approaching performance. The SC-LDPC codes can be decoded by a sliding window, therefore, the decoding latency and complexity of SC-LDPC codes are lower than those of underlying LDPC codes when the codeword length is very large. In this paper, the SC-LDPC decoder with the sliding window is employed in turbo equalization of magnetic recording systems. We examine the bit error rates (BERs) of the output of the sliding window during the iterative decoding, and then observe that the consecutive code blocks have approximately the same BERs. Herein, to reduce decoding complexity of SC-LDPC codes, the consecutive code blocks can be considered as the output of SC-LDPC codes. In addition, the non-uniform schedule update is adopted in the window decoding to avoid unnecessary updates within a window. The simulation results show that the proposed decoding algorithms applied in bit-patterned media magnetic recording systems can achieve a significant reduction in complexity compared to the traditional decoding without any loss in BER performance.

## Spatially-Coupled Codes for Channels with SNR Variation

- **Status**: ✅
- **Reason**: SC-LDPC 신규 partitioning(column weight 4/6)·인터리빙으로 error floor 개선; 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8424449
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Homa Esfahanizadeh, Ahmed Hareedy, Ruiyi Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/8424449
- **Abstract**: In magnetic recording systems, consecutive sections experience different signal-to-noise ratios (SNRs). To perform error correction over these systems, one approach is to use an individual block code for each section. However, the performance over a section affected by a lower SNR is weaker compared to the performance over a section affected by a higher SNR. Spatially-coupled (SC) codes are a family of graph-based codes with capacity approaching performance and low latency decoding. An SC code is constructed by partitioning an underlying block code to several component matrices, and coupling copies of the component matrices together. The contribution of this paper is threefold. First, we present a new partitioning technique to efficiently construct SC codes with column weights 4 and 6. Second, we present an SC code construction for channels with SNR variation. Our SC code construction provides local error correction for each section by means of the underlying codes that cover one section each, and simultaneously, an added level of error correction by means of coupling among the underlying codes. Third, we introduce a low-complexity interleaving scheme specific to SC codes that further improves their performance over channels with SNR variation. Our simulation results show that our SC codes outperform individual block codes by more than one and two orders of magnitudes in the error floor region compared to the block codes with and without regular interleaving, respectively. This improvement is more pronounced by increasing the memory and column weight.

## A Study on Iterative Decoding With LLR Modulator by Parity Check Information in SMR System

- **Status**: ✅
- **Reason**: 바이너리 LDPC sum-product 반복디코딩에 LLR modulator 추가로 error floor 제거 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8369398
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: M. Nishikawa, Y. Nakamura, H. Osawa +3
- **PDF**: https://ieeexplore.ieee.org/document/8369398
- **Abstract**: In recent years, shingled magnetic recording (SMR) has attracted attention as a new recording system of the hard disk drives. Although SMR can realize narrow track by overwriting data track like tile roofing, it has remarkable performance deterioration due to the influence of inter-track interference. Therefore, the performance improvement of the low-density parity-check (LDPC) coding and iterative decoding system using the sum-product decoding is required. In this paper, we propose the LDPC encoding and iterative decoding system with the log-likelihood ratio modulator and show the error floor is eliminated and improvement of signal-to-noise ratio to achieve the error free is obtained in the SMR under an areal recording density of 4 Tbits/in2 specification for the channel bit sequence coded by run-length limited and LDPC encoders by computer simulation. Therefore, the channel bit is composed bit about five magnetic grains.

## The Velocity of the Propagating Wave for Spatially Coupled Systems With Applications to LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 SC-LDPC density evolution 전파파 속도 해석식·유한길이 스케일링 적용; SC-LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8419715
- **Type**: journal
- **Published**: Nov. 2018
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/8419715
- **Abstract**: We consider the dynamics of message passing for spatially coupled codes and, in particular, the set of density evolution equations that tracks the profile of decoding errors along the spatial direction of coupling. It is known that, for suitable boundary conditions and after a transient phase, the error profile exhibits a “solitonic behavior.” Namely, a uniquely shaped wavelike solution develops, which propagates with a constant velocity. Under this assumption, we derive an analytical formula for the velocity in the framework of a continuum limit of the spatially coupled system. The general formalism is developed for spatially coupled low-density parity-check codes on general binary memoryless symmetric channels, which form the main systems of interest in this paper. We apply the formula for special channels and illustrate that it matches the direct numerical evaluation of the velocity for a wide range of noise values. A possible application of the velocity formula to the evaluation of finite size scaling law parameters is also discussed. We conduct a similar analysis for general scalar systems and illustrate the findings with applications to compressive sensing and generalized low-density parity-check codes on the binary erasure or binary symmetric channels.

## A Further Research on Two-phase Decoding for GC-LDPC Codes

- **Status**: ✅
- **Reason**: GC-LDPC 2단계 디코딩용 개선 log-domain BP 알고리즘+수렴가속 - 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8693129
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Wei Zhou, Lijun Zhang, Qiang Sun
- **PDF**: https://ieeexplore.ieee.org/document/8693129
- **Abstract**: For GC-LDPC code, a targeted decoding scheme is the two-phase decoding scheme, i.e., the local decoding phase and the global decoding phase. For both the phases, we find the direct application of log-domin belief propagation (BP) algorithm will lead to error. Hence, we propose an improved log-domin BP algorithm and it will be used in the two-phase decoding scheme. Since the two-phase decoding scheme has a large gain loss, we present a modified two-phase decoding scheme in order to further accelerate the convergence rate. Simulation results show that the modified two-phase decoder has a gain of about 0.2 dB compared to the two-phase decoder. Moreover, it also can reduce complexity by 33.4% in high SNR compared with the whole decoder.

## Hybrid Decoding of LDPC Codes in Discrete Communication Channels

- **Status**: ✅
- **Reason**: C: bit-flip과 majority-logic을 결합한 하이브리드 LDPC 디코딩(저반복·낮은 error-floor) — 바이너리 LDPC 디코더 기법으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8604309
- **Type**: conference
- **Published**: 26-30 Nov.
- **Authors**: A. A. Ovchinnikov, D. V. Ilina
- **PDF**: https://ieeexplore.ieee.org/document/8604309
- **Abstract**: Decoding of low-density parity-check codes with bit-flip algorithm is considered. The majority-logic decoding is described as bit-flip algorithm with modified decoding threshold. The hybrid decoding combining both algorithms is considered and simulation results in Gaussian channel with hard decision demodulation are given. Described scheme may be effective in high-speed channels with low number of decoding iterations demands together with the requirements of low decoding error probabilities and low error-floors.

## Generalized Globally-Coupled Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: E: globally-coupled LDPC 신규 구성법(RS-like, masking) 제시 — 바이너리 LDPC 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613362
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Yen-Chin Liao, Hsie-Chia Chang, Shu Lin
- **PDF**: https://ieeexplore.ieee.org/document/8613362
- **Abstract**: In this paper, two globally-coupled low-density parity check (GC-LDPC) code constructing methods are presented. The first is a Reed-Solomon-like GC-LDPC code that eases the design parameter searching in algebraic code constructions. The parameters such as the finite field, the associated prime factors, or the number of local codes can be more easily determined. The directly masking approach, the second proposed scheme, facilitates flexible structure designs of the parity check matrices. The two approaches can be regarded as generalizations of the original GC-LDPC codes. The design examples and the simulation results show the feasibility of the proposed techniques. In addition to code constructions, some applications and usage scenarios of GC-LDPC codes are addressed as well.

## On Generalized LDPC Codes for 5G Ultra Reliable Communication

- **Status**: ✅
- **Reason**: GLDPC(일반화 제약노드) QC-LDPC 신규 구성과 constraint-to-variable 업데이트 규칙(C/E), 바이너리 BP 메시지패싱 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613515
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Yanfang Liu, Pablo M. Olmos, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/8613515
- **Abstract**: Generalized low-density parity-check (GLDPC) codes, where single parity-check (SPC) constraint nodes are replaced with generalized constraint (GC) nodes, are a promising class of codes for low latency communication. In this paper, a practical construction of quasi-cyclic (QC) GLDPC codes is proposed, where the proportion of generalized constraints is determined by an asymptotic analysis. We analyze the message passing process and complexity of a GLDPC code over the additive white gaussian noise (AWGN) channel and present a constraint-to-variable update rule based on the specific codewords of the component code. The block error rate (BLER) performance of the GLDPC codes, combined with a complementary outer code, is shown to outperform a variety of state-of-the-art code and decoder designs with suitable lengths and rates for the 5G Ultra Reliable Communication (URC) regime over an additive white gaussian noise (AWGN) channel with quadrature PSK (QPSK) modulation.

## Type-II Quasi-Cyclic LDPC Codes with Girth Eight from Sidon Sequence

- **Status**: ✅
- **Reason**: E: Sidon 수열 기반 girth-8 type-II QC-LDPC 신규 대수적 구성 — 바이너리 LDPC 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613426
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Guohua Zhang, Yulin Hu, Qinwei He +1
- **PDF**: https://ieeexplore.ieee.org/document/8613426
- **Abstract**: In this work, we consider type-II quasi-cyclic LDPC codes with girth eight from a Sidon sequence. We first derive the necessary and sufficient conditions guaranteeing girth-eight type-II QC-LDPC codes. By combining these conditions and the concept of a Sidon sequence, two classes of type-II codes are subsequently proposed with girth up to eight. We discuss the distance upper bounds of the two classes of codes and show that the second class provides a larger distance upper bound. In particular, to the best of our knowledge, the second class we proposed yields the first algebraic construction for girth-eight type-II codes with rates larger than a half and distance upper bounds exceeding twelve. Via simulations, we show that the girth-eight type-II codes from the second class significantly outperform the existing CDF-based girth-eight type-II codes, and that they perform better than or almost identically to the randomly generated girth-eight quadr. congr. codes.

## Read-Voltage Optimization for Finite Code Length in MLC NAND Flash Memory

- **Status**: ✅
- **Reason**: A. MLC NAND 플래시 read-voltage 최적화+유한블록길이 LDPC FER 개선, NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613523
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Kang Wei, Jun Li, Lingjun Kong +2
- **PDF**: https://ieeexplore.ieee.org/document/8613523
- **Abstract**: In this paper, we propose an effective read-voltage optimization method for multi-level-cell (MLC) NAND flash memory to improve the performance of error correcting codes (ECCs) with finite blocklength. Specifically, we first obtain the maximal channel coding rate achievable at a given blocklength and error probability of quantized channel. Based on this finite-blocklength channel-coding rate (FCR), we convert the optimization problem into minimizing the error probability instead of the channel coding rate. Then, we develop a cross iterative search (CIS) method and the genetic algorithm to solve this optimization problem. In our simulations, for a well-designed LDPC code, our read-voltage optimization method improves program-and-erase (PE) endurance up to about 900 and 600 cycles against the maximizing the mutual information (MMI) and entropy-based optimization methods, respectively, at a frame-error-rate (FER) of 2×10-4.

## An Iterative Soft-Decision Decoding Algorithm with Dynamic Saturation for Short Reed-Solomon Codes

- **Status**: ✅
- **Reason**: C: ABP(adaptive belief propagation) 기반 반복 연판정 디코딩, damping 계수·LLR saturation 메시지패싱 기법이 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613470
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Bryan Liu, Yixuan Xie, Lei Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8613470
- **Abstract**: This paper proposes a new iterative soft-decision decoding algorithm which combines list decoding and adaptive belief propagation (ABP) algorithm for short Reed-Solomon (RS) codes. The proposed algorithm generates a list of codewords by restarting the decoder with log-likelihood ratio saturations to the dynamically selected suspicious bits based on an up-to-date best decoded codeword. The suspicious bits are selected according to a joint evaluation of the decoded codeword and the initial channel information. The damping coefficient used in the ABP decoder is set to be proportional to the channel noise variance to achieve a proper convergence speed for the decoder at different SNRs. The performance of the proposed algorithm for short RS codes is investigated. It shows that the proposed algorithm brings a considerable coding gain for short RS codes over additive white Gaussian noise channels.

## Information Theoretic Bounds Based Channel Quantization Design for Emerging Memories

- **Status**: ✅
- **Reason**: A/C: 메모리(STT-MRAM) 채널 1비트 양자화 설계·정보이론 기준 최적화 — LLR 양자화 기법 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8613421
- **Type**: conference
- **Published**: 25-29 Nov.
- **Authors**: Zhen Mei, Kui Cai, Long Shi
- **PDF**: https://ieeexplore.ieee.org/document/8613421
- **Abstract**: Channel output quantization plays a vital role in high-speed emerging memories such as the spin-torque transfer magnetic random access memory (STT-MRAM), where high-precision analog-to-digital converters (ADCs) are not applicable. In this paper, we investigate the design of the 1-bit quantizer which is highly suitable for practical applications. We first propose a quantized channel model for STT-MRAM. We then analyze various information theoretic bounds for the quantized channel, including the channel capacity, cutoff rate, and the Polyanskiy-Poor-Verdu ́(PPV) finite-length performance bound. By using these channel measurements as criteria, we design and optimize the 1-bit quantizer numerically for the STTMRAM channel. Simulation results show that the proposed quantizers significantly outperform the conventional minimum mean-squared error (MMSE) based Lloyd-Max quantizer, and can approach the performance of the 1-bit quantizer optimized by error rate simulations.

## Energy-Efficient and Low Complexity Channel Coding for Wireless Body Area Networks

- **Status**: ✅
- **Reason**: PEXIT 변형으로 protograph LDPC 설계; 바이너리 protograph 코드설계 기법(E) 이식 가능, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8606883
- **Type**: conference
- **Published**: 23-24 Nov.
- **Authors**: Hieu T. Nguyen, Thuy V. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/8606883
- **Abstract**: A new design framework based on the modified protograph extrinsic information transfer (PEXIT) algorithm is proposed for wireless body area networks (WBAN) communication systems. Using the proposed framework, a protograph LDPC code of rate 1/2 is designed for the WBAN channel which is statistically modelled as Rician distribution with K-factor obtained from the path loss model. The proposed protograph LDPC coded system achieves a significant coding gain of 17.5 dB over the uncoded system. This coding gain is much higher than the coding gain (6.1 dB) of irregular LDPC coded system in the additive white Gaussian noise (AWGN) channel reported previously for wireless sensor networks. This significant coding gain together with the low complexity encoder/decoder makes the protograph LDPC code an excellent candidate for WBAN communication systems where energy and complexity are among very demanding technical requirements.

## Layered Offset Min-Sum Decoding for Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: LDPC용 적응형 layered offset min-sum 디코더 신규 제안(C), 바이너리 LDPC 직접 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8618780
- **Type**: conference
- **Published**: 21-23 Nov.
- **Authors**: Nejwa El Maammar, Seddik Bri, Jaouad Foshi
- **PDF**: https://ieeexplore.ieee.org/document/8618780
- **Abstract**: Offset Min-Sum Algorithm (OMSA) and Normalized Min-Sum Algorithm (NMSA) are widely used in commercial LDPC decoders due to low complexity and reasonable performance. In this paper we proposes an Adaptive Layered Offset min- sum algorithm for the decoding of LDPC codes, which utilizes an adaptive offset factor to improve the accuracy of the soft information transferred during the iterative decoding process, and it provides good performance accordingly. The performed simulations showed that the layered offset min-sum decoding for LDPC codes can provide significant improvement compared to existing MS based algorithm, OMSA and NMSA.

## Performance of Self-Corrected APP-Based Decoding Algorithm for Decoders with Quantized Input

- **Status**: ✅
- **Reason**: 양자화 입력(1~3bit) APP/min-sum 디코더의 self-correction 개선 — NAND LLR 양자화 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8612112
- **Type**: conference
- **Published**: 20-21 Nov.
- **Authors**: Aleksei Kharin, Igor Volkov, Aleksei Ovinnikov +2
- **PDF**: https://ieeexplore.ieee.org/document/8612112
- **Abstract**: In this paper we explore the impact of self-correction (SC) modification on performance of a posteriori probability (APP) based decoding algorithm for LDPC codes. Influence of self-correction technique was investigated for decoders with 3, 2 and 1 bit input quantization. It was shown that performance of decoders with quantized input can be significantly improved in comparison with regular APP-based decoding algorithm, and in some cases with Min-Sum algorithm. Convergence of algorithm is almost the same as for Min-Sum decoding. Performance and convergence results are presented for two CCSDS (8176, 7156) and IEEE 802.3an (2048, 1723) LDPC codes for APP-based, SC APP-based and Min-Sum decoding algorithms.

## A High-Throughput QC-LDPC Decoder for Near-Earth Application

- **Status**: ✅
- **Reason**: QC-LDPC 고처리량 디코더 HW(TDMP 스케줄링, NMSA, 메모리 충돌 회피, 65nm) — HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8631641
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Shixian Li, Qichen Zhang, Yun Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8631641
- **Abstract**: Turbo-like decoding message passing (TDMP) scheduling, which is suitable for quasi-cyclic low-density parity-check (QC-LDPC) codes, can obtain better decoding performance and shorter convergence time than two-phase message passing (TPMP). Normalized min-sum algorithm (NMSA) is used to reduce complexity of soft message processing unit. In this paper, we propose a (8176, 7154) QC-LDPC decoder for Consultative Committee for Space Data Systems (CCSDS) standard. In order to avoid memory access conflicts, two cyclic-shifted identity matrices forming a submatrix are processed individually. The decoder is synthesized by TSMC 65nm CMOS process and can achieve a throughput of 4.1Gb/s at clock frequency of 380MHz.

## A Novel Jointed Detection Scheme for MIMO-LDPC Systems

- **Status**: ✅
- **Reason**: MIMO-LDPC 합동검출이나 BP 디코딩 + EP-BP JDD factor graph 기법, BP 개선 디코더(C) 이식 여지(애매시 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8631790
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Guiwu Yang, Jianhao Hu, Guoqiang Yao +2
- **PDF**: https://ieeexplore.ieee.org/document/8631790
- **Abstract**: High performance and high efficiency detection scheme is one of the key issues for MIMO-LDPC system designs. In this paper, we proposed a hybrid jointed detection scheme for MIMO-LDPC detection, in which the expectation propagation (EP) algorithm is used in MIMO detection and the belief propagation (BP) algorithm is adopted for the low density parity check code (LDPC) decoding. In the proposed scheme, we provide a jointed detection algorithm (EP-BP JDD) with the integrated factor graph for MIMO-LDPC systems. Compared with conventional MMSE-PIC IDD and BP-BP JDD, the proposed method can achieve low computational complexity with high performance. The complexity and performance gains become more significant with the number of antennas increasing.

## Girth Analysis of Tanner (5,11) Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC(Tanner)의 girth 분석·사이클 조건 도출 — 카테고리 E 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8564291
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Hengzhou Xu, Hai Zhu, Mengmeng Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/8564291
- **Abstract**: Motivated by the works on the girth of Tanner (3,5), (3,7), (3,11), and (5,7) quasi-cyclic (QC) LDPC codes, we in this paper study the girth of Tanner (5,11) QC-LDPC codes. We first analyze the cycles of Tanner (5,11) QC-LDPC codes, and obtain the conditions for the existence of cycles of length less than 12 in Tanner (5,11) QC-LDPC codes of length 11p where p is a prime number and p =1 (mod 55). Notice that the condition is represented by the polynomial equations in a 55th root of unity of the prime field Fp. By checking the existence of solutions for these equations over Fp, the girths of Tanner (5,11) QC-LDPC codes are obtained.

## Smart Construct High Girth LDPC Codes Based on Permutation Groups

- **Status**: ✅
- **Reason**: permutation group+유전알고리즘 기반 high-girth LDPC 신규 구성법 — 카테고리 E, 무선 응용이나 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8564322
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Qiang Wang, Tingting Lan
- **PDF**: https://ieeexplore.ieee.org/document/8564322
- **Abstract**: In the field of wireless communications, it is of great significance to structure LDPC codes (Low-density Parity-check codes) with large girth. We propose a method to construct high girth LDPC codes based on algebra permutation group of intelligent. Girth larger parity check matrix can be found in Gallager parity check matrix set using genetic algorithm based on permutation group in a relatively short period of time. Simulation results show that the algorithm is efficient, versatile, and consistent with the theoretical analysis.

## Rate-Compatible Protograph LDPC Codes for Spin-Torque Transfer Magnetic Random Access Memory (STT-MRAM)

- **Status**: ✅
- **Reason**: 신규 protograph LDPC 설계(PEXIT/AWE, rate-compatible code extension) - 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8601078
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Xingwei Zhong, Kui Cai, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8601078
- **Abstract**: This paper proposes novel rate-compatible protograph LDPC (RCP-LDPC) codes to correct memory cell errors and mitigate the raw bit error rate (BER) diversity for spin-torque transfer magnetic random access memory (STT-MRAM). Since the STT-MRAM channel is asymmetric, we first apply an independent and identically distributed (i.i.d.) channel adapter to force the channel to be symmetric. We then propose to use the protograph extrinsic information transfer (PEXIT) algorithm, the asymptotic weight distribution (AWE) analysis, as well as the actual error rate performance as the combined guideline for designing protograph LDPC codes with short codeword lengths for STT-MRAM. By further applying a code extension approach, we construct novel RCP-LDPC codes that can work with a single encoder/decoder. Simulation results show that our proposed RCP-LDPC codes outperform the well-known rate-compatible AR4JA protograph codes.

## On the Design of DC-Free K-Constrained LDPC Codes

- **Status**: ✅
- **Reason**: LDPC와 constraint/balance code 결합 코드설계 기법 - 바이너리 LDPC 구성(E) 이식 가능, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8601099
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Chi Dinh Nguyen, Kui Cai, Bingrui Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8601099
- **Abstract**: A novel design of de-free k-constraint low-density parity-check (LDPC) code is proposed in this study. The input user data is first converted into a k-constraint code using a nibble replacement method. After that, a guided scrambling (GS) technique and a (4,6) balance code are deployed together to construct de-free channel coded sequences. The designed de-free k constrained code is further combined with the LDPC code such that the modulation constraints are satisfied in both the systematic and parity parts. Simulation results show that the proposed design not only provides an improved bit-error-rate (BER) performance, but also achieves significant dc suppression.

## Design and Analysis of Spatially Coupled Protograph LDPC Codes for Two-Dimensional Magnetic Recording Systems

- **Status**: ✅
- **Reason**: SC-protograph LDPC 신규 구성+turbo-like EXIT threshold 분석 - SC-LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8601100
- **Type**: conference
- **Published**: 15-17 Nov.
- **Authors**: Zhaojie Yang, Yi Fang, Guojun Han +2
- **PDF**: https://ieeexplore.ieee.org/document/8601100
- **Abstract**: In this paper, a turbo-like extrinsic information transfer (EXIT) algorithm is proposed for two-dimensional magnetic recording (TDMR) systems. Based on the proposed turbo-like EXIT algorithm, we not only analyze the decoding threshold of spatially coupled protograph (SC-P) low-density parity-check (LDPC) codes over TDMR channels under turbo detection, but also conceive a design methodology to construct capacity-approaching terminated SC-P codes. Compared with the original protograph codes, the terminated SC- P codes possess desirable performance gains in both low and high signal-to-noise-ratio (SNR) regions.

## Short Length LDPC Code-Candidate for Satellite Control Channel

- **Status**: ✅
- **Reason**: 신규 short-length LDPC 구성 제안(CCSDS 대비 성능 향상) - 바이너리 LDPC 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8757376
- **Type**: conference
- **Published**: 15-16 Nov.
- **Authors**: Luiza R. Medova, Pavel S. Rybin, Ivan V. Filatov
- **PDF**: https://ieeexplore.ieee.org/document/8757376
- **Abstract**: In this paper we consider the experimental specification for "Short Block Length LDPC codes for TC Synchronization and Channel Coding" by the Consultative Committee for Space Data Systems (CCSDS 231.1-O-1). We consider the methods of constructing LDPC codes and propose the new construction of LDPC code. Numerical results show that proposed construction of LDPC code significantly outperforms one from considered specification under the same decoding algorithm.

## Efficient Four-way Row-splitting Layered QC-LDPC Decoder Architecture

- **Status**: ✅
- **Reason**: four-way row-splitting layered QC-LDPC 디코더 VLSI 아키텍처(7.05Gb/s, 면적효율)로 HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8649976
- **Type**: conference
- **Published**: 12-15 Nov.
- **Authors**: Tram Thi Bao Nguyen, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/8649976
- **Abstract**: This paper presents a four-way row-splitting architecture for layered low-density parity-check (LDPC) decoder. Based on the proposed method, an efficient partially parallel pipelined QC-LDPC decoder is proposed. The synthesis results using TSMC 40-nm standard cell CMOS technology show that the proposed decoder achieves the maximum required throughput of 7.05 Gb/s and outperforms its predecessors in terms of area efficiency.

## Construction of Reed-Solomon Based Quasi-Cyclic LDPC Codes Based on Protograph

- **Status**: ✅
- **Reason**: protograph 기반 RS-QC-LDPC 신규 구성(girth>=8, 최소거리 상한 향상)-E 바이너리 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8633521
- **Type**: conference
- **Published**: 12-14 Nov.
- **Authors**: Inseon Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/8633521
- **Abstract**: In this paper, we propose construction of Reed-Solomon(RS) based Quasi-Cyclic Low-Density Parity-Check(QC-LDPC) codes using protograph combining two existing QC-LDPC codes construction. One is the construction RS based QC-LDPC codes whose girth is at least 8 and another is protograph based QC-LDPC codes to increase the upper bounds of minimum Hamming distance. We construct the protographs to increase the upper bound of minimum Hamming distance for Proto-RS-QC-LDPC codes and simulate some experiment to show coding gain in sense of BER compare to existing QC-LDPC codes.

## LDPC Code Design via Masking Technology and Progressive Optimization

- **Status**: ✅
- **Reason**: masking+progressive 최적화로 girth-4 제거하는 LDPC 코드 설계, 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8599317
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Dongliang Guo
- **PDF**: https://ieeexplore.ieee.org/document/8599317
- **Abstract**: A design of low-density parity-check (LDPC) code via the masking technology and progressive optimization is proposed. The code generated by this method has lower computational complexity, and their parity-check matrices can effectively refrain from the girth -4 phenomenon. The proposed method has the superiorities such as better girth-length characteristic and more flexible trim in the length and rate of the code. Experiment results indicate that the error-correction performance of the new code should be better than or as good as the capability of the code which is constructed without been masking. Futhermore, under the condition of short code length, the performance is better than that of LDPC codes via the randomized construction methods.
