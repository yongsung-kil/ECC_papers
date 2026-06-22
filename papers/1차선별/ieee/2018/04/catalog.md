# IEEE Xplore — 2018-04 (1차선별 통과)


## Improving the Decoding Threshold of Tailbiting Spatially Coupled LDPC Codes by Energy Shaping

- **Status**: ✅
- **Reason**: 바이너리 tailbiting SC-LDPC 디코딩 임계값 개선(energy shaping), SC-LDPC 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8281448
- **Type**: journal
- **Published**: April 2018
- **Authors**: Thomas Jerkovits, Gianluigi Liva, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/8281448
- **Abstract**: We show how the iterative decoding threshold of tailbiting spatially coupled (SC) low-density parity-check (LDPC) code ensembles can be improved over the binary input additive white Gaussian noise channel by allowing the use of different transmission energies for the codeword bits. We refer to the proposed approach as energy shaping. We focus on the special case where the transmission energy of a bit is selected among two values, and where a contiguous portion of the codeword is transmitted with the largest one. Given these constraints, an optimal energy boosting policy is derived by means of a protograph extrinsic information transfer analysis. We show that the threshold of tailbiting SC-LDPC code ensembles can be made close to that of terminated code ensembles while avoiding the rate loss (due to termination). The analysis is complemented by Monte Carlo simulations, which confirm the viability of the approach.

## Design of Binary LDPC Codes With Parallel Vector Message Passing

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC 사이클 최적화(PMPE/QC-PMP) 신규 코드설계 기법, NAND LDPC 구성에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8207605
- **Type**: journal
- **Published**: April 2018
- **Authors**: Xingcheng Liu, Feng Xiong, Zhongfeng Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8207605
- **Abstract**: Many studies were carried out for the construction of low density parity-check (LDPC) codes. They usually focused on introducing the construction methods for good LDPC codes instead of a general method for code optimization. This paper proposes a method with high versatility, called the parallel vector message passing-based edge exchange (PMPE), for optimizing a type of graph-based LDPC codes, without changing the code parameters of mother codes, such as the code length, code rate, and degree distribution. With the approximately nearest codewords searching approach, we find the optimization method can increase the Hamming distance of the LDPC codes. For the quasi-cyclic (QC) LDPC codes, an optimization method, called the parallel vector message passing oriented-to the QC-LDPC codes (QC-PMP), is further suggested, with which the quasi-cyclic characteristics of QC-LDPC codes can remain unchanged in the optimization. To evaluate the performance of the parity-check matrix corresponding to a Tanner graph, a very simple metric, the cycles metric, is introduced to work with the proposed PMPE and QC-PMP algorithms. The experimental results show that the performance of the LDPC codes optimized with the proposed PMPE can be improved significantly at low BER range compared with the mother codes of the random codes, including the regular MacKay code of rate 0.5 and the regular PEG code of rate 0.9. For the case of the regular and irregular QC-LDPC codes with different code lengths and code rates, the optimized LDPC codes with the proposed QC-PMP algorithm significantly outperform the mother codes.

## Flexible WOM codes for NAND flash memory based on raptor-like codes

- **Status**: ✅
- **Reason**: NAND 플래시 직접 대상 WOM 코드(raptor-like rate-compatible LDGM); 카테고리 A, NAND 수명 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8360624
- **Type**: journal
- **Published**: April 2018
- **Authors**: Bohwan Jun, Heeyoul Kwak, Jong-Seon No +1
- **PDF**: https://ieeexplore.ieee.org/document/8360624
- **Abstract**: Write-once memory (WOM) codes aim to extend the lifetime and improve the writing efficiency of storage devices such as NAND flash memory by reducing the number of erase operations. In this paper, a new rewriting scheme for NAND flash memory is proposed, which supports two writes (or only one rewrite) and allows the second write incrementally done multiple times by using raptor-like codes as rate-compatible (RC) low-density generator matrix (LDGM) codes. The proposed scheme improves writing efficiency of the NAND flash memory when combined with a proper page selection method. It is verified via numerical analysis that the proposed WOM codes outperform the conventional WOM codes in terms of writing efficiency.

## 9.1x Error acceptable adaptive artificial neural network coupled LDPC ECC for charge-trap and floating-gate 3D-NAND flash memories

- **Status**: ✅
- **Reason**: A. 3D-NAND(charge-trap/floating-gate) ANN 결합 LDPC ECC, 컨트롤러 구현 직접 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8357064
- **Type**: conference
- **Published**: 8-11 April
- **Authors**: Toshiki Nakamura, Yoshiaki Deguchi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/8357064
- **Abstract**: Adaptive Artificial Neural Network coupled (ANN) LDPC ECC (ANN-LDPC ECC) is proposed to increase acceptable errors by 9.1-times and to extend the data-retention lifetime by 76-times for charge-trap and floating-gate 3D-NAND flash memories. Adaptive ANN automatically compensates for complex memory cell errors such as lateral charge migration, vertical charge de-trap, inter floating-gate capacitive coupling noise and inter word-line variations. In addition, proposed ANN-LDPC can reproduce the dynamic endurance and data-retention time dependence of errors. Proposed ANN-LDPC is implemented in the storage controller and can precisely and adaptively estimate BER. As a result, memory cell errors are corrected without read time penalty or storage controller size increase.

## Reduced-complexity window decoding of spatially coupled LDPC codes for magnetic recording systems

- **Status**: ✅
- **Reason**: SC-LDPC 윈도우 디코딩 복잡도 감소(동적 시프팅 DS-WD/DS-N-WD), 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8508405
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: S. Khittiwitchayakul, W. Phakphisut, P. Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8508405
- **Abstract**: In channel coding theory, the performance of error correcting codes (ECCs) approaching the Shannon limit can be achieved through increasing code lengths. Unfortunately, the complexity of ECCs will be increased as the code length increases. Nowadays, the magnetic recording (MR) system takes advantage of powerful ECCs by using 4 Kbytes sector. Among the advanced ECCs, the spatially coupled LDPC (SC-LDPC) codes (also known as a LDPC convolutional code) [1]are shown to have the decoding latency and complexity lower than those of the underlying LDPC block codes (LDPC-BC). Moreover, the SC-LDPC codes with threshold decoding outperform the LDPC-BC codes [2]. Hence, the SC-LDPC codes are the strong candidate for the future MR systems, when the sector size is increased beyond 4 Kbytes. An SC-LDPC decoder can use sliding window decoding [3]whereby the received signals are decoded by sliding window along the bit sequence. The window decoder is called “uniform window decoding (U-WD),” when all variable nodes (VNs) within a window are updated. In order to reduce the complexity of window decoding, some researchers proposed the non-uniform window decoding (N-WD) [4], which do not update the VNs with no improvement in the bit error rate (BER). This approach provides about 35-50% reduction in complexity compared to U-WD. In this work, we consider the application of SC-LDPC codes in MR systems, whereby SC-LDPC decoder cooperates with BCJR detector to encounter inter-symbol interference (ISI). We propose the dynamic shifting of window decoding (DS-WD) to reduce the complexity of SC-LDPC codes. Herein, the number of shifted bits is defined according to their soft BERs which are estimated at each decoding position. In addition, we modify the N-WD [4]to reinforce our proposed algorithm called “dynamic-shifting non-uniform window decoding (DS-N-WD).” The DS-WD and DS-N-WD achieve the complexity reduction of 7% and 25% without any loss in performance compared to the N-WD algorithms.

## Spatially-Coupled Codes for Channels With SNR Variation

- **Status**: ✅
- **Reason**: SC-LDPC 신규 분할(MO 확장 γ=4)·채널인지 인터리빙으로 error floor 개선, 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8508464
- **Type**: conference
- **Published**: 23-27 Apri
- **Authors**: H. Esfahanizadeh, A. Hareedy, R. Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/8508464
- **Abstract**: Modern magnetic recording (MR) systems require error correcting codes (ECCs) with outstanding error floor performance. Low-density parity-check (LDPC) codes are a primary choice for MR systems because of their error correcting capabilities [1]–[3]. In a magnetic recording device, some sections can be more error-prone than other sections because of the read/write mechanism and physical properties of the device [4]. A realistic channel model for magnetic recording systems must consider the variation of signal to noise ratio (SNR) among consecutive sections of a hard disk drive. For channels with SNR variation, the conventional ECCs are designed to achieve the certain BER for the section with the lowest SNR. For the sections with higher SNRs, this approach results in an additional redundancy which is not necessary to achieve the target BER. Spatially-coupled (SC) codes are a family of graph-based codes that have attracted significant attention because of their capacity approaching performance [5]. SC codes are constructed by partitioning a parity-check matrix H of the underlying block code into component matrices H0,…,Hm, H=H0+…+Hm, and coupling L copies of the component matrices together to obtain the parity-check matrix HSC, Fig. 1. The parameters m and L are known as the memory and coupling length, respectively. An SC code with coupling length L has L replicas, {R1,…,RL}, see Fig. 1. In this paper, we present an SC code design approach for channels with SNR variation. In our code design, the length of the underlying block codes is equal to the length of one section of the channel, and the number of sections spanned by one SC code is determined by L. Because of this structure, each check node (CN) receives messages from more than one section, so more reliable variable nodes (VNs) can help compensate for the sections that are highly affected by noise. In our model for a channel with SNR variation, each section is considered as an AWGN channel with SNRi (i is the section index). For the i’th section, we state the SNR as (SNRi)dB=(SNRabs)dB+(ΔSNRi)dB, where (SNRabs)dB is the absolute SNR and (ΔSNRi)dB is the variation from the absolute SNR for the i’th section. We first describe our code construction approach: The length of the underlying block code is equal to the length of one section of the channel, so each replica of an SC code spans one section of the channel. The coupling length L determines how many sections are spanned by one SC code, so it must be chosen such that a variety of sections with different reliabilities are included. The minimum overlap (MO) approach is recently introduced for partitioning block codes and constructing SC codes [6]. In this approach, the matrix H of a block code is partitioned into several component matrices such that the number of detrimental objects in the graph of the derived SC code for AWGN channels is reduced. In this paper, we use MO approach for constructing SC codes with γ=3. Moreover, we extend this approach to construct SC codes with γ=4. The memory m of an SC code plays the critical role on its performance over channels with SNR variation. By increasing memory, sections are more cooperative, and the SNR variation among them can be alleviated better. The parameter m determines how many different sections are involved in the check equations in an iterative decoding. Because of our SC code construction, most CNs receive messages from VNs within m+1 consecutive sections. As a result, if there is one reliable section with a high SNR, it can in principle help the messages from other m sections be recovered more reliably. For interleaving, we divide the SC codeword into L2/(m+1) chunks. Then, we rearrange them by taking one chunk from each L consecutive chunks and putting them next to each other. This interleaved data is passed through the channel, and the de-interleaving is performed on the received data from the channel and before decoding. Due to interleaving, most CN receives an equal number of messages from all L different levels of reliabilities. Our simulation results show that our channel-based interleaving compensates for the performance gap that exists between the error rates of SC codes over non-uniform and uniform channels with similar average SNR. Our proposed scheme is the first channel-aware interleaving for SC codes, and the complexity of the proposed interleaving is inversely proportional to the number of component matrices. The regular interleaving has a fixed complexity with respect to the memory which is equal to the complexity of our interleaving scheme for the case m=0 (the uncoupled setup). Finally, we show some important simulation results. Block Code 1 is an array-based block code with γ=3, length 289 bits, and rate r=0.82. SC Code 1 and 2 are SC codes with Block Code 1 as the underlying block code. They both have L=30 and length 8670 bits. The memory and rate for SC Code 1 are m=1 and r=0.82, and for SC Code 2 are m=2 and r=0.81, respectively. Fig. 2 shows the BER curves for Block Code 1, SC Code 1, and SC Code 2 over the non-uniform channel. It can be seen that SC Code 1 shows 2 orders of magnitude performance improvement in the error floor area compared to the Block Code 1, with and without (regular) interleaving, respectively. We achieve further improvement when we apply our optimized interleaving to SC Code 1. Moreover, SC Code 2 secures even further improvement by providing more cooperation among different sections of the channel. The longer version includes results for our γ=4 SC codes.

## Construction and decoding of OSMLD codes derived from unital and oval designs

- **Status**: ✅
- **Reason**: BIBD 기반 OSMLD 코드 신규 구성 + iterative threshold decoding — 바이너리 LDPC 계열 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8360280
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Otmane El Mouaatamid, Mohamed Lahmer, Mostafa Belkasmi
- **PDF**: https://ieeexplore.ieee.org/document/8360280
- **Abstract**: A construction of One-Step Majority-Logic Decodable (OSMLD) codes based on the incidence matrices of Balanced Incomplete Block Designs (BIBD) is given. In this paper, we focus on unital and oval designs which are constructed from a Projective Geometry (PG). Thus, we derive from the unital and oval designs new systematic and non-systematic OSMLD codes with rates and lengths not available with existing OSMLD codes. Simulation results show that the derived codes converge well under Iterative Threshold Decoding with an efficient trade-off between complexity and performances.

## A Shuffled-Based Iterative Demodulation and Decoding Scheme for Ldpc Coded Flash Memory

- **Status**: ✅
- **Reason**: TLC NAND 플래시 LDPC 직접(A), shuffled IDD + HW-friendly interleaver 구조로 이식 가능한 HW 기법(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8461609
- **Type**: conference
- **Published**: 15-20 Apri
- **Authors**: Li-Chung Lee, Wei-Min Lai, Mao-Ruei Li +1
- **PDF**: https://ieeexplore.ieee.org/document/8461609
- **Abstract**: In previous studies, a very sparse low-density parity-check (LDPC) code was designed for triple-level cell (TLC) NAND flash using non-Gray mapping, which is able to achieve comparable error-rate performance to the conventional Gray mapping-based scheme. Although a sparse LDPC code can be of benefit to hardware implementations of an iterative demodulation and decoding (IDD) scheme, difficulties emerge, such as latency issue between the decoder and demodulator, when compared to non-IDD schemes. In this paper, a hardware-friendly structure interleaver is used such that a shuffle-based IDD scheme can be realized efficiently. Compared to the conventional Gray-based non-IDD scheme and layered-based IDD scheme, the proposed shuffled-based IDD scheme can provide a better hardware efficiency and better error-rate performance.

## ADMM hardware decoder for regular LDPC codes using a NISC-based architecture

- **Status**: ✅
- **Reason**: regular LDPC용 ADMM-LP NISC 기반 FPGA 디코더 HW 구현+BP 대비 자원비교; 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8377331
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Imen Debbabi, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/8377331
- **Abstract**: The Alternate Direction Method of Multipliers (ADMM) approach is an original method for LDPC decoding based on the linear programming (LP) technique. It introduces a novelty at the error correction performance level. Nevertheless, this method can be toughly implemented due to its high computational complexity. In this paper, an implementation of the ADMM LP decoding algorithm on an FPGA target is presented. Its hardware resource cost is evaluated and compared with the state of the art LDPC decoders using the belief propagation (BP) decoding approach. The preliminary logic synthesis results show that an LP based hardware decoder for LDPC codes should be viable for applications with tough error correction requirements. However, additional research works are required to reach equivalent hardware complexity and throughput performances that are similar to traditional BP based LDPC decoders.

## Implementation aspects of a pipeline ADMM-based LP decoding of LDPC convolutional codes

- **Status**: ✅
- **Reason**: LDPC-CC용 ADMM-LP layered 파이프라인 디코딩+8비트 고정소수점 양자화+Euclidean projection skipping 최적화; 이식 가능한 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8377103
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Hayfa Ben Thameur, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/8377103
- **Abstract**: The enforcement of the linear programming (LP) decoding was recently extended to LDPC convolutional codes (LDPC-CC). It was demonstrated that their convolutional structure suites the message-passing based representation of the LP problem, thanks to the application of the alternating directions method of multipliers (ADMM). In this paper, a modified formulation of the ADMM-LP problem is introduced for pipeline decoding of LDPC-CCs based on the layered schedule. Moreover, an assessment of the fixed-point format required for hardware implementation is provided to evaluate the complexity of the underlying decoding algorithm. Simulations show that an 8-bit quantization scheme yields negligible error correction performances loss of about 0.05 dB regarding the floating-precision ADMM based LDPC-CC decoder. Further, an algorithmic optimization of the Euclidean projection skipping technique, described in [1] [2], is proposed. This improved version enables to reduce the computational complexity of the decoding process without memory penalty contrary to the original formulation.

## Belief propagation decoding of polar codes on permuted factor graphs

- **Status**: ✅
- **Reason**: polar 부호이나 permuted factor graph 기반 BP 디코딩 기법이 부호 비의존적 메시지패싱 개선으로 바이너리 LDPC BP에 이식 가능(예외 C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8377158
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/8377158
- **Abstract**: We show that the performance of iterative belief propagation (BP) decoding of polar codes can be enhanced by decoding over different carefully chosen factor graph realizations. With a genie-aided stopping condition, it can achieve the successive cancellation list (SCL) decoding performance which has already been shown to achieve the maximum likelihood (ML) bound provided that the list size is sufficiently large. The proposed decoder is based on different realizations of the polar code factor graph with randomly permuted stages during decoding. Additionally, a different way of visualizing the polar code factor graph is presented, facilitating the analysis of the underlying factor graph and the comparison of different graph permutations. In our proposed decoder, a high rate Cyclic Redundancy Check (CRC) code is concatenated with a polar code and used as an iteration stopping criterion (i.e., genie) to even outperform the SCL decoder of the plain polar code (without the CRC-aid). Although our permuted factor graph-based decoder does not outperform the SCL-CRC decoder, it achieves, to the best of our knowledge, the best performance of all iterative polar decoders presented thus far.

## On the construction of protograph based SC-LDPC codes for windowed decoding

- **Status**: ✅
- **Reason**: protograph 기반 SC-LDPC 윈도우 디코딩용 코드 설계+DE 최적화로 degree-1 회피·threshold 개선; 바이너리 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8377289
- **Type**: conference
- **Published**: 15-18 Apri
- **Authors**: Martin Schlüter, Najeeb Ul Hassan, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/8377289
- **Abstract**: In this paper we optimize spatially coupled protographs for window decoding (WD) and arbitrary rate. Previous studies found that the belief propagation (BP) threshold of spatially coupled code ensembles achieves the maximum a posteriori (MAP) threshold of their underlying block code ensemble. This property requires a large coupling length L and thus the window decoder is considered to reduce latency and complexity of the decoding. To approach the BP threshold fast in the size of the window W, it is well known that the code requires a special structure to avoid degree-1 variable nodes inside the window. We further require additional structure to construct a systematic code with low encoding complexity, which unfortunately forces degree-1 variable nodes inside the window. Thus, we formulate an optimization problem to maximize the WD threshold and solve it by applying a differential evolution (DE) based algorithm. Compared to the regular protographs obtained by edge spreading, our optimized irregular protographs show a significant improvement in terms of WD threshold and finite length performance for small window sizes, hence leads to small decoding latency and complexity. Furthermore, for high rates our codes can compete with the highly optimized LDPC block codes from the WiMAX standard.
