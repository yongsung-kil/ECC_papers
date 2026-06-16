# IEEE Xplore — 2016-01


## On Advanced FEC and Coded Modulation for Ultra-High-Speed Optical Transmission

- **ID**: ieee:7422653
- **Type**: journal
- **Published**: thirdquart
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7422653
- **Abstract**: This tutorial paper presents an overview of advanced FEC and coded modulation (CM) for optical communications. It describes the following ultra-high-speed optical transport enabling techniques: codes on graphs (turbo-product and LDPC codes), rate-adaptive CM, and turbo equalization. Given the high potential of LDPC codes, several binary and nonbinary LDPC decoding algorithms are described and FPGA implementation is also discussed. We then demonstrate that some recently proposed attractive LDPC codes could in fact be represented as special instances of irregular quasi cyclic (QC)-LDPC codes from pairwise balanced designs (PBDs). In addition, we describe several LDPC-coded modulation schemes, including hybrid multidimensional CM, block-interleaved CM, multilevel coding, nonbinary (NB) LDPC-CM, and multilevel NB-LDPC-CM. We also demonstrate the application of turbo equalization and rate-adaptive coding in high-speed optical transmission to deal with fiber nonlinearities. Finally, an optimized signal constellation design approach as well as an optimized mapping rule has been discussed.

## A Survey on DCSK-Based Communication Systems and Their Application to UWB Scenarios

- **ID**: ieee:7442517
- **Type**: journal
- **Published**: thirdquart
- **Authors**: Yi Fang, Guojun Han, Pingping Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/7442517
- **Abstract**: In the past two decades, chaotic modulations have drawn a great deal of attention in low-power and low-complexity wireless communication applications due to their excellent anti-fading and anti-intercept capabilities. Of particular interest is the differential chaos shift keying (DCSK), which is considered as a very promising chaotic modulation scheme that achieves not only good error performance, but also low implementation complexity. In this treatise, we provide an insightful survey on the state-of-the-art research in DCSK-based communication systems through an extensive open literature search. In doing so, we firstly review the principles of DCSK modulation and the significant milestones since its inception. Subsequently, we introduce meritorious variants of DCSK, all of which can outperform the original one in certain aspects. We also present the joint design guidelines when combining DCSK with other critical techniques, e.g., error-correction coding and cooperative communication, in wireless communications under both single-user and multiaccess scenarios. Besides, we summarize research progress in the application of DCSK-based communication systems to ultra-wideband scenarios and their corresponding advantages. Specifically, we restrict our attention to the relevant modulation and system designs, as well as their performance-analysis methodologies. This survey aims not only to allow researchers understanding the development and current status of DCSK-based communication systems, but also to inspire further research in this area.

## A Survey of FPGA-Based LDPC Decoders

- **ID**: ieee:7360870
- **Type**: journal
- **Published**: Secondquar
- **Authors**: Peter Hailes, Lei Xu, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7360870
- **Abstract**: Low-density parity check (LDPC) error correction decoders have become popular in communications systems, as a benefit of their strong error correction performance and their suitability to parallel hardware implementation. A great deal of research effort has been invested into LDPC decoder designs that exploit the flexibility, the high processing speed, and the parallelism of field-programmable gate array (FPGA) devices. FPGAs are ideal for design prototyping and for the manufacturing of small-production-run devices, where their in-system programmability makes them far more cost-effective than application-specific integrated circuits (ASICs). However, the FPGA-based LDPC decoder designs published in the open literature vary greatly in terms of design choices and performance criteria, making them a challenge to compare. This paper explores the key factors involved in FPGA-based LDPC decoder design and presents an extensive review of the current literature. In-depth comparisons are drawn amongst 140 published designs (both academic and industrial) and the associated performance tradeoffs are characterized, discussed, and illustrated. Seven key performance characteristics are described, namely, their processing throughput, processing latency, hardware resource requirements, error correction capability, processing energy efficiency, bandwidth efficiency, and flexibility. We offer recommendations that will facilitate fairer comparisons of future designs, as well as opportunities for improving the design of FPGA-based LDPC decoders.

## Joint Design of QC-LDPC Codes for Coded Relay Cooperation

- **ID**: ieee:10855863
- **Type**: journal
- **Published**: January 20
- **Authors**: Lei Tang, Fengfan Yang, Shunwai Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10855863
- **Abstract**: This paper proposes an effective method to jointly design girth-4 cycle-free Quasi-cyclic (QC) Low-density parity-check (LDPC) codes for multi-relay cooperation in a Rayleigh fading channel, where the joint iterative decoding by Min-sum algorithm (MSA) based on the introduced joint Tanner graph is also presented at the destination. Theoretical analysis and simulation show that the proposed QC-LDPC coded cooperation outperforms the randomly coded cooperation under the same conditions.

## Construction of High-Performance Array-Based Non-Binary LDPC Codes With Moderate Rates

- **ID**: ieee:7307109
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Shancheng Zhao, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7307109
- **Abstract**: Based on arrays, excellent low-density parity-check (LDPC) codes with high rates have been constructed. In this letter, we propose to construct high-performance nonbinary LDPC (NBLDPC) codes with moderate rates based on arrays. The proposed construction combines masking and column selection. First, we construct a masking matrix M based on asymptotic thresholds and certain error-prone substructures. Second, we generate a number of column selection sets (CSS) based on Golomb rulers. Based on M, we construct a parity-check matrix for each CSS. Third, we compute the cycle distribution of each parity-check matrix and select the one with the best cycle distribution as output. To assess the effectiveness of the proposed construction, error performances of several NBLDPC codes are presented. Comparisons with other codes are also carried out to show the advantages of our construction.

## Searching for Binary and Nonbinary Block and Convolutional LDPC Codes

- **ID**: ieee:7312464
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Rolf Johannesson
- **PDF**: https://ieeexplore.ieee.org/document/7312464
- **Abstract**: A unified approach to search for and optimize codes determined by their sparse parity-check matrices is presented. Replacing the nonzero elements of a binary parity-check matrix (the base or parent matrix) either by circulants or by companion matrices of elements from a finite field GF $(2^{m})$ , we obtain quasi-cyclic low-density parity-check (LDPC) block codes and binary images of nonbinary LDPC block codes, respectively. By substituting monomials of a formal variable  $D$ , we obtain the polynomial description of an LDPC convolutional code. A set of performance measures applicable to different classes of LDPC codes is considered, and a greedy algorithm for code performance optimization is presented. The heart of the new optimization algorithm is a fast procedure for searching for LDPC codes with large girth of their Tanner graphs. For a few classes of LDPC codes, examples of codes combining good error-correcting performance with compact representation are obtained. In particular, we present optimized convolutional LDPC codes and conclude that the LDPC block codes are still superior to their convolutional counterparts if both decoding complexity and coding delay are considered. Moreover, a specific channel model can easily be embedded into the optimization loop. Thereby, the code can be optimized for a specific channel. The efficiency of such an optimization is demonstrated via an example of faster than Nyquist (FTN) signaling using LDPC codes. The FTN strategy combined with a rate  $R=1/2$  LDPC code of length 64 800 optimized for effective data rate  $R=3/4$  gains more than 0.5 dB compared with the standard LDPC codes of the same rate and length. The obtained gain corresponds to transmission at the capacity of the binary input additive white Gaussian noise channel. In most numerical examples, we consider codes with bidiagonal structure of the parity-check matrix. This restriction preserves low encoding complexity and allows fair comparison with codes selected for communication standards.

## Reliability-Based Joint Detection-Decoding Algorithm for Nonbinary LDPC-Coded Modulation Systems

- **ID**: ieee:7293134
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Min Zhu, Quan Guo, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/7293134
- **Abstract**: This paper studies an extension and improvement of the joint detection-decoding algorithm for nonbinary LDPC-coded modulation systems. The iterative joint detection-decoding (IJDD) algorithm in [1] combines nonbinary LDPC decoding with signal detection based on the hard-message passing strategy, resulting in significantly reduced decoding complexity. However, it applies only to majority-logic decodable nonbinary LDPC codes with high column weight. For nonbinary LDPC codes with low column weight, a noticeable performance loss will be incurred. To handle this problem, we propose a reliability-based iterative joint detection-decoding (also termed improved IJDD) algorithm, which combines the accumulated reliability of symbols based on the one-step majority-logic decoding (MLGD) algorithm and a Chase-like local list decoding algorithm. Simulation results show that the improved IJDD algorithm outperforms the IJDD algorithm by about 0.3 dB using nonbinary LDPC codes with high column weight, and by about 3 dB using nonbinary LDPC codes with low column weight (dv = 4), while maintaining the low complexity of decoding. Compared to the FFT-QSPA, the proposed algorithm has a performance degradation of 0.5 dB in the high column weight regime, and about 1 dB in the low column weight regime.

## Bit Reliability-Based Decoders for Non-Binary LDPC Codes

- **ID**: ieee:7329979
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Qin Huang, Shuai Yuan
- **PDF**: https://ieeexplore.ieee.org/document/7329979
- **Abstract**: Message-passing decoders typically perform well for nonbinary low-density parity-check (NB-LDPC) codes with large computational complexity. As another type of simplified decoders, symbol-reliability-based decoders further reduce the computational complexity. However, the previously proposed algorithms suffer severe error performance degradation for NB-LDPC codes with low column weights. In this paper, a weighted bit-reliability based (wBRB) decoder for NB-LDPC codes is developed and implemented with efficient layered partial-parallel structure. It not only balances the tradeoff between complexity and error performance, but also reduces the memory usage significantly. Furthermore, to enhance the performance of the wBRB decoder, a full bit-reliability-based (FBRB) decoder is proposed. The FBRB decoder is derived based on the binary matrix representation of the nonzero entries in the parity-check matrix. Since more bit-reliability values are passed through the edges of the Tanner graph, the FBRB decoder can achieve better error performance and faster convergence rate than the wBRB decoder. Both of the decoders are implemented on a Xilinx Virtex-5 XC5VLX155T FPGA device for a (403,226) code over GF(25). The results shows that they achieve 118.98 and 95.73 Mbps throughput with 15 iterations, respectively.

## Construction of Quantum LDPC Codes From Classical Row-Circulant QC-LDPCs

- **ID**: ieee:7350103
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Zunaira Babar, Panagiotis Botsinis, Dimitrios Alanis +2
- **PDF**: https://ieeexplore.ieee.org/document/7350103
- **Abstract**: Classical row-circulant quasi-cyclic (QC) low-density parity check (LDPC) matrices are known to generate efficient high-rate short and moderate-length QC-LDPC codes, while the comparable random structures exhibit numerous short cycles of length-4. Therefore, we conceive a general formalism for constructing nondual-containing Calderbank–Shor–Steane (CSS)-type quantum low-density parity check (QLDPC) codes from arbitrary classical row-circulant QC-LDPC matrices. We apply our proposed formalism to the classical balanced incomplete block design (BIBD)-based row-circulant QC-LDPC codes for demonstrating that our designed codes outperform their dual-containing CSS-type counterparts as well as the entanglement-assisted (EA)-QLDPC codes.

## Concatenated Codes for Combating Effects of Intertrack Interference in Shingled Magnetic Recording

- **ID**: ieee:7234917
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Xiangyu Tang, Yu Kou, Lingqi Zeng
- **PDF**: https://ieeexplore.ieee.org/document/7234917
- **Abstract**: We introduce a novel concatenated code that targets errors generated by intertrack interference in shingled magnetic recording. The code has fewer overhead than the conventional product codes. We give a detailed presentation in the code construction and encoding method. We also present a novel decoding scheme for the concatenated code that has very low memory requirements.

## Breaking the Trapping Sets in LDPC Codes: Check Node Removal and Collaborative Decoding

- **ID**: ieee:7320999
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Soonyoung Kang, Jaekyun Moon, Jeongseok Ha +1
- **PDF**: https://ieeexplore.ieee.org/document/7320999
- **Abstract**: Trapping sets strongly degrade performance of low-density parity check (LDPC) codes in the low-error-rate region. This creates significant difficulties for the deployment of LDPC codes to low-error-rate applications such as storage and wireless systems with no or limited retransmission options. We propose a novel technique for breaking trapping sets based on collaborative decoding that utilizes two different decoding modes. While the main decoding mode executes message passing based on the original parity check matrix of the corresponding LDPC code, the sub-decoding mode operates on a modified parity check matrix formed by removing a portion of check nodes in the factor graph representation of the given code. The modified parity check matrix is designed to promote a passing of correct information into erroneous variable nodes in the trapping set. Theoretical properties of the proposed trapping-set-breaking technique have been established based on the notion of the improved separation for the trapped variable nodes. Simulation results show that the proposed collaborative LDPC decoding scheme switching between the two decoding modes back and forth effectively breaks dominant trapping sets of various known types of regular and irregular LDPC codes.

## LDPC Decoding Over Nonbinary Queue-Based Burst Noise Channels

- **ID**: ieee:7017574
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Pedro Melo, Cecilio Pimentel, Fady Alajaji
- **PDF**: https://ieeexplore.ieee.org/document/7017574
- **Abstract**: Iterative decoding based on the sum-product algorithm (SPA) is examined for sending low-density parity check (LDPC) codes over a discrete nonbinary queue-based Markovian burst noise channel. This channel model is adopted due to its analytical tractability and its recently demonstrated capability in accurately representing correlated flat Rayleigh fading channels under antipodal signaling and either hard or soft output quantization. SPA equations are derived in closed form for this model in terms of its parameters. It is then numerically observed that potentially large coding gains can be realized with respect to the Shannon limit by exploiting channel memory as opposed to ignoring it via interleaving. Finally, the LDPC decoding performance under both matched and mismatched decoding regimes is evaluated. It is shown that the Markovian model provides noticeable gains over channel interleaving and that it can effectively capture the underlying fading channel behavior when decoding LDPC codes.

## Spatially Coupled Repeater-Combiner-Convolutional Codes

- **ID**: ieee:7317509
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Wei Hou, Shan Lu, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/7317509
- **Abstract**: A form of spatially coupled codes is obtained by coupling multiple identical concatenated codes consisting of a block outer code (a repetition code followed by a single-parity code) concatenated with a convolutional inner code of infinite impulse response. The coupling operation involves only the outer code of the block-convolutional concatenated code. Because of the simple outer code and diverse inner code, the proposed codes have simple encoding implementation and flexible designation space. Extrinsic information functions are used to analyze the belief propagation (BP) thresholds of the proposed codes over an additive white Gaussian noise channel. The numerical results demonstrate that the proposed codes have better BP threshold and error correction performances than conventional spatially coupled repeat-accumulate codes and spatially coupled low-density parity-check codes. In particular, the proposed codes with a rate of about 0.5 and length of 15628 have a bit-error-rate (BER) of $10^{-5}$ at Eb/N0 of 1.13 dB that is less than 1 dB away from the Shannon limit.

## Construction of Near-Capacity Protograph LDPC Code Sequences With Block-Error Thresholds

- **ID**: ieee:7328274
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Asit Kumar Pradhan, Andrew Thangaraj, Arunkumar Subramanian
- **PDF**: https://ieeexplore.ieee.org/document/7328274
- **Abstract**: Density evolution for protograph low-density parity-check (LDPC) codes is considered, and it is shown that the message-error rate falls double-exponentially with iterations whenever the degree-2 subgraph of the protograph is cycle-free and noise level is below threshold. Conditions for stability of protograph density evolution are established and related to the structure of the protograph. Using large-girth graphs, sequences of protograph LDPC codes with block-error threshold equal to bit-error threshold and block-error rate falling near-exponentially with blocklength are constructed deterministically. Small-sized protographs are optimized to obtain thresholds near capacity for binary erasure and binary-input Gaussian channels.

## Row and Column Extensions of 4-Cycle Free LDPC Codes

- **ID**: ieee:7317762
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Mohammad Gholami, Akram Nassaj
- **PDF**: https://ieeexplore.ieee.org/document/7317762
- **Abstract**: In this letter, an approach is proposed to increase the row (column)-weight of the parity-check matrix of a 4-cycle free LDPC code such that the constructed LDPC code has girth of at least 6. In fact, to each parity-check matrix H, a new graph Gr(H) (Gc(H)) is assigned in which the vertices correspond to the rows (columns) of H and two vertices are adjacent if and only if the associated rows (columns) have in common at least one nonzero element. Now, in a proper vertex coloring of Gr(H) (Gc(H)), each color is considered as a new column (row) whose nonzero elements happen in the rows (columns) in which the corresponding vertices have the same color. Based on this method, some high-rate LDPC codes with girth 6 and column-weight of at least 4 can be constructed from the recently proposed column-weight three LDPC codes with girth 6. Moreover, using the mutually orthogonal Latin squares, this approach is applied on the incidence matrices of some complete bipartite graphs to generate some girth-6 LDPC codes with different column-weights and large minimum-distances.

## A Robust NDA Carrier Tracking Method for LDPC-Coded Systems With Symbol Rate Sampling

- **ID**: ieee:7329919
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Yunhua Li, Bin Tian, Kechu Yi +3
- **PDF**: https://ieeexplore.ieee.org/document/7329919
- **Abstract**: In this letter, a robust nondata-aided (NDA) carrier tracking method is proposed for low-density parity-check (LDPC) coded systems with symbol rate sampling. The proposed method has a novel and hybrid carrier tracking loop combined with the frequency-locked loop (FLL), increasing/decreasing sampling rate blocks, phase-locked loop (PLL), and modified symbol decision method, which is capable of improving estimation accuracy of the frequency offsets and phase offsets at low signal-to-noise ratios (SNRs). When applied to the $(4096,3072)$ LDPC coded system, numerical simulations and comparisons are provided to validate the effectiveness of the proposed carrier tracking method in the case of relatively low SNRs.

## A 3.0 Gb/s Throughput Hardware-Efficient Decoder for Cyclically-Coupled QC-LDPC Codes

- **ID**: ieee:7370816
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Qing Lu, Jianfeng Fan, Chiu-Wing Sham +2
- **PDF**: https://ieeexplore.ieee.org/document/7370816
- **Abstract**: In this paper, we propose a new class of quasi-cyclic low-density parity-check (QC-LDPC) codes, namely cyclically-coupled QC-LDPC (CC-QC-LDPC) codes, and their RAM-based decoder architecture. CC-QC-LDPC codes have a simple structure and are constructed by cyclically-coupling a number of QC-LDPC subcodes. They can achieve throughput and error performance as excellent as LDPC convolutional codes, but with much lower hardware requirements. They are therefore promising candidates for future generations of communication systems such as long-haul optical communication systems. In particular, a rate-5/6 CC-QC-LDPC decoder has been implemented onto a field-programmable gate array (FPGA) and it achieves a throughput of 3.0 Gb/s at 100 MHz clock rate with 10-iteration decoding. No error floor is observed up to an $E_{b}/N_{0}$ of 3.50 dB, where all $1.14\times 10^{16}$ transmitted bits have been decoded correctly.

## RS-LDPC Concatenated Coding for the Modern Tape Storage Channel

- **ID**: ieee:7339707
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Jieun Oh, Jeongseok Ha, Hyegyeong Park +1
- **PDF**: https://ieeexplore.ieee.org/document/7339707
- **Abstract**: In modern tape storage, user data are recorded and retrieved along multiple tracks of rapidly moving, flexible magnetic medium that give rise to a variety of channel impediments including occasional long erasures, more frequent amplitude fades as well as a large amount of random errors. This work considers reliable recovery of data from such tape channels using a novel concatenation of an inner Reed-Solomon (RS) code and an outer nonbinary low-density parity-check (LDPC) code. This particular concatenation scheme and a highly tailored iterative decoding algorithm are chosen to efficiently handle the assortment of the tape channel impediments while meeting the stringent target error rate constraint as well as key practical requirements of the mass tape storage system. Despite the use of a nonbinary LDPC code, the proposed scheme allows excellent performance-complexity tradeoffs. In stark contrast to any existing coding schemes that involve LDPC codes, the proposed concatenation strategy allows semianalytic error rate performance evaluation at rates below what is possible using modern computers, thus providing an ability to ensure satisfactory low-error-rate performance.

## Message Passing Algorithms for Phase Noise Tracking Using Tikhonov Mixtures

- **ID**: ieee:7349155
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Shachar Shayovitz, Dan Raphaeli
- **PDF**: https://ieeexplore.ieee.org/document/7349155
- **Abstract**: Phase noise poses a serious challenge for high-speed digital communications systems mainly when going to higher and higher carrier frequencies, such as in satellite communications. Traditionally, phase noise estimation was performed separately from the decoding task and it was shown, recently, that there is much to be gained from joint estimation and decoding, particularly when using LDPC (low-density parity check)/turbo codes. However, jointly estimating phase noise and decoding is a very complex and computationally demanding task. In this paper, we propose several algorithms based on the sum and product algorithm (SPA) for low complexity joint decoding and estimation of coded information in strong phase noise channels. These algorithms are based on a novel approximation of SPA messages as Tikhonov mixtures of a given order. Since mixture-based Bayesian inference such as SPA, creates an exponential increase in mixture order for consecutive messages, a mixture reduction scheme is a must. Therefore, in this paper, we propose a low complexity mixture reduction algorithm, which provably satisfies an upper bound on the Kullback Leibler (KL) divergence between the mixture and the reduced mixture. We then reduce the complexity even further, including limiting the model order and reducing the clustering effort to simple component selection. As an extreme case, it is even possible to reduce the number of modes to one. We show the relation between the simplified algorithm to the phase locked loop (PLL). Finally, we show simulation results and complexity analysis for the proposed algorithms, which show superior performance over other state of the art low complexity algorithms.

## Analysis and Optimization of Sparse Random Linear Network Coding for Reliable Multicast Services

- **ID**: ieee:7335581
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Andrea Tassi, Ioannis Chatzigeorgiou, Daniel E. Lucani
- **PDF**: https://ieeexplore.ieee.org/document/7335581
- **Abstract**: Point-to-multipoint communications are expected to play a pivotal role in next-generation networks. This paper refers to a cellular system transmitting layered multicast services to a multicast group of users. Reliability of communications is ensured via different random linear network coding (RLNC) techniques. We deal with a fundamental problem: the computational complexity of the RLNC decoder. The higher the number of decoding operations is, the more the user's computational overhead grows and, consequently, the faster the battery of mobile devices drains. By referring to several sparse RLNC techniques, and without any assumption on the implementation of the RLNC decoder in use, we provide an efficient way to characterize the performance of users targeted by ultra-reliable layered multicast services. The proposed modeling allows to efficiently derive the average number of coded packet transmissions needed to recover one or more service layers. We design a convex resource allocation framework that allows to minimize the complexity of the RLNC decoder by jointly optimizing the transmission parameters and the sparsity of the code. The designed optimization framework also ensures service guarantees to predetermined fractions of users. The performance of the proposed optimization framework is then investigated in a LTE-A eMBMS network multicasting H.264/SVC video services.

## A New and Accurate Estimator With Analytical Expression for Frequency Estimation

- **ID**: ieee:7312438
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Xiaohu Liang, Aijun Liu, Xiaofei Pan +2
- **PDF**: https://ieeexplore.ieee.org/document/7312438
- **Abstract**: Frequency estimation of a single complex exponential waveform is an important problem in many fields. In this letter, a new frequency estimator for a complex exponential sine waveform observed under the additive white Gaussian noise (AWGN) is proposed. The proposed estimator is obtained by solving the nonlinear functions. The new estimator has an analytical expression based on interpolation method with three DFT samples. Numerical results demonstrate that the performance of the proposed estimator has lower SNR threshold to closely reach the Cramer-Rao bound (CRB) in the low SNR region and its performance also outperforms previous estimators in the high SNR region.

## Tree Analysis of BATS Codes

- **ID**: ieee:7322211
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Shenghao Yang, Qiaoqiao Zhou
- **PDF**: https://ieeexplore.ieee.org/document/7322211
- **Abstract**: BATS codes are a class of efficient random linear network codes. In this letter, BATS codes are generalized to incorporate batches of different sizes, and the corresponding belief propagation (BP) decoding performance is studied. Using a tree-based analysis, a sufficient condition is obtained such that the BP decoder can recover a given fraction of the input symbols with high probability. Some assumptions in the previous works are relaxed in our analysis so that the analytical results can be applied to more general scenarios.

## Optimizing the Code Rate of Energy-Constrained Wireless Communications With HARQ

- **ID**: ieee:7208849
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Fernando Rosas, Richard Demo Souza, Marcelo E. Pellenz +4
- **PDF**: https://ieeexplore.ieee.org/document/7208849
- **Abstract**: Retransmissions due to decoding errors have a big impact on the energy budget of low-power wireless communication devices, which can be reduced by using hybrid automatic repeat request (HARQ) techniques. Nevertheless, this reduction comes at the cost of extra energy consumption introduced by the added computational load. No complete analysis of the tradeoff between retransmissions reduction and baseband consumption of low-power communications over fading channels has been reported so far. In this paper, we study the energy efficiency achievable by HARQ schemes when the code rate of the error-correcting code is optimized. For this purpose, we develop an energy consumption model that focuses on simple HARQ (S-HARQ) and Chase combining (HARQ-CC) transmissions, which are studied under fast-fading and block-fading scenarios with Nakagami-$m$ fading. The retransmission statistics are analyzed, and expressions for the expected number of transmission trials are derived. Using this framework, it is shown that transmission schemes with high diversity gain are the most efficient choice for long range transmissions, which in our case correspond to HARQ-CC and codes with low code rate. On the other hand, schemes with good multiplexing capabilities are optimal for short link distances, which in our analysis correspond to S-HARQ and high code rates. It is also shown that HARQ-CC can effectively extend the transmission range of a low-power communication device.

## Permutation Trellis Coded Multi-Level FSK Signaling to Mitigate Primary User Interference in Cognitive Radio Networks

- **ID**: ieee:7342915
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Raghed El-Bardan, Engin Masazade, Onur Ozdemir +2
- **PDF**: https://ieeexplore.ieee.org/document/7342915
- **Abstract**: In this paper, we propose a novel spectrum underlay approach for secondary users where a permutation trellis code (PTC) is employed in conjunction with multi-level frequency shift keying signaling in the presence of multiple narrowband primary users (PUs). The PUs are assumed to be dynamic in that they appear intermittently and stay active for an unknown duration. Our proposed approach derives its resilience to the interference caused by PUs and noise disturbances via dispersal of the information in SU's messages over multiple frequencies and time intervals. Our proposed underlay-design improves the SU data rate by accumulating a large amount of spectrum from several PUs, while simultaneously operating at low power to minimize the interference caused at PUs' receivers. We evaluate our system performance in terms of bit error rate (BER) and throughput by approximating the actual BER using properties of the Viterbi decoder. We corroborate our analytical results with simulation results and show that our proposed coded system is robust to heavy interference caused by multiple narrowband PUs.

## EM-Based Phase Noise Estimation in Vector OFDM Systems Using Linear MMSE Receivers

- **ID**: ieee:7008538
- **Type**: journal
- **Published**: Jan. 2016
- **Authors**: Ibo Ngebani, Yabo Li, Xiang-Gen Xia +1
- **PDF**: https://ieeexplore.ieee.org/document/7008538
- **Abstract**: Vector orthogonal frequency-division multiplexing (V-OFDM) for single-transmit-antenna systems is a generalization of OFDM where single-carrier frequency-domain equalization and OFDM are just two special cases. Phase noise in a V-OFDM system leads to a common vector block phase error (CVBPE) and an intervector block carrier interference effect. Severe performance degradation may occur if these two effects are not estimated and compensated well. In this paper, blind and semiblind phase noise estimation and compensation in a V-OFDM system is investigated by using the expectation-maximization (EM) algorithm. This is motivated by the fact that the conventional frequency-domain phase noise suppression schemes based on pilot-aided common phase error (CPE) or CVBPE estimation and compensation are not spectrally efficient as the vector block size is increased. Two novel schemes are proposed: One estimates the CVBPE only, and the other estimates the entire phase noise sequence in the time domain. General closed-form formulas for the maximization step of the EM algorithm for the two schemes are derived, and their computational complexity values are analyzed. The performances of the two schemes are investigated by using linear-minimum-mean-square-error (LMMSE) receivers. Simulations show that the two proposed schemes are very effective in estimating and compensating for phase noise in V-OFDM systems. It turns out that the second proposed scheme not only outperforms the traditional CPE or CVBPE schemes but is computationally efficient as well when applied to V-OFDM systems.

## A Survey on FEC Codes for 100 G and Beyond Optical Networks

- **ID**: ieee:6917198
- **Type**: journal
- **Published**: Firstquart
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Ivan B. Djordjevic +3
- **PDF**: https://ieeexplore.ieee.org/document/6917198
- **Abstract**: Due to the rapid increase in network traffic in the last few years, many telecommunication operators have started transitions to 100-Gb/s optical networks and beyond. However, high-speed optical networks need more efficient forward error correction (FEC) codes to deal with optical impairments, such as uncompensated chromatic dispersion, polarization mode dispersion, and nonlinear effects, and keep the bit error rate (BER) at long distances sufficiently low. To address these issues, new FEC codes, called third-generation codes, have been proposed. A majority of these codes are based on soft-decision decoders and can provide higher coding gain as compared with their predecessors. This paper presents a thorough survey of third-generation FEC codes, suitable for 100 G and beyond optical networks. Furthermore, this paper discusses the main advantages and drawbacks of each scheme and provides a qualitative categorization and comparison of the proposed schemes based on their main features, such as net coding gain and BER. Information about the complexity of each scheme is given as well.

## 20 Years of Turbo Coding and Energy-Aware Design Guidelines for Energy-Constrained Wireless Applications

- **ID**: ieee:7131434
- **Type**: journal
- **Published**: Firstquart
- **Authors**: Matthew F. Brejza, Liang Li, Robert G. Maunder +3
- **PDF**: https://ieeexplore.ieee.org/document/7131434
- **Abstract**: During the last two decades, wireless communication has been revolutionized by near-capacity error-correcting codes (ECCs), such as turbo codes (TCs), which offer a lower bit error ratio (BER) than their predecessors, without requiring an increased transmission energy consumption (EC). Hence, TCs have found widespread employment in spectrum-constrained wireless communication applications, such as cellular telephony, wireless local area network, and broadcast systems. Recently, however, TCs have also been considered for energy-constrained wireless communication applications, such as wireless sensor networks and the `Internet of Things.' In these applications, TCs may also be employed for reducing the required transmission EC, instead of improving the BER. However, TCs have relatively high computational complexities, and hence, the associated signal-processing-related ECs are not insignificant. Therefore, when parameterizing TCs for employment in energy-constrained applications, both the processing EC and the transmission EC must be jointly considered. In this tutorial, we investigate holistic design methodologies conceived for this purpose. We commence by introducing turbo coding in detail, highlighting the various parameters of TCs and characterizing their impact on the encoded bit rate, on the radio frequency bandwidth requirement, on the transmission EC and on the BER. Following this, energy-efficient TC decoder application-specific integrated circuit (ASIC) architecture designs are exemplified, and the processing EC is characterized as a function of the TC parameters. Finally, the TC parameters are selected in order to minimize the sum of the processing EC and the transmission EC.

## Symbol-Decision Successive Cancellation List Decoder for Polar Codes

- **ID**: ieee:7289453
- **Type**: journal
- **Published**: Feb.1, 201
- **Authors**: Chenrong Xiong, Jun Lin, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/7289453
- **Abstract**: Polar codes are of great interests because they provably achieve the symmetric capacity of discrete memoryless channels with arbitrary input alphabet sizes while having an explicit construction. Most existing decoding algorithms of polar codes are based on bit-wise hard or soft decisions. In this paper, we propose symbol-decision successive cancellation (SC) and successive cancellation list (SCL) decoders for polar codes, which use symbol-wise hard or soft decisions for higher throughput or better error performance. First, we propose to use a recursive channel combination to calculate symbol-wise channel transition probabilities, which lead to symbol decisions. Our proposed recursive channel combination has lower complexity than simply combining bit-wise channel transition probabilities. The similarity between our proposed method and Arıkan's channel transformations also helps to share hardware resources between calculating bit- and symbol-wise channel transition probabilities. Second, a two-stage list pruning network is proposed to provide a trade-off between the error performance and the complexity of the symbol-decision SCL decoder. Third, since memory is a significant part of SCL decoders, we propose a pre-computation memory-saving technique to reduce memory requirement of an SCL decoder. Finally, to evaluate the throughput advantage of our symbol-decision decoders, we design an architecture based on a semi-parallel successive cancellation list decoder. In this architecture, different symbol sizes, sorting implementations, and message scheduling schemes are considered. Our synthesis results show that in terms of area efficiency, our symbol-decision SCL decoders outperform existing bit-decision and multi-bit SCL decoders.

## The analysis of hops for multi-hop cooperation in Underwater Acoustic Sensor Networks

- **ID**: ieee:7535777
- **Type**: conference
- **Published**: 9-11 Jan. 
- **Authors**: Xiaoting Jin, Yougan Chen, Xiaomei Xu
- **PDF**: https://ieeexplore.ieee.org/document/7535777
- **Abstract**: Underwater Acoustic Sensor Networks (UASNs) have recently attracted significant attention for exploration and monitoring in underwater environments. The sensor nodes used in UASNs are powered by batteries that are difficult to recharge or replace. It is imperative that the number of hops deployment in multi-hop networks should be very energy efficient whilst at the same time satisfying necessary delay constraints. In this paper, we firstly analyze the relationship of energy consumption, end-to-end delay and number of hops in a multi-hop UASN, and then we investigate how to optimize the number of hops with a fixed distance in term of trade-offs between energy consumption and end-to-end delay. Then we define a cost function to research the minimum number of hops. Simulation results show that, taking into consideration the energy consumption and end-to-end delay, we can obtain an appropriate number of hops for the multi-hop UASN by adopting co-operation over a given distance. The model obtained in this paper is used to determine the number of hops in an energy efficient UASN for an underwater time-critical mission.

## Impact of sea waves on performance of shallow water acoustic communications

- **ID**: ieee:7535761
- **Type**: conference
- **Published**: 9-11 Jan. 
- **Authors**: Shengxing Liu, Chienchung Shen
- **PDF**: https://ieeexplore.ieee.org/document/7535761
- **Abstract**: Shallow water acoustic channels have fast time-variance, long-time multipath spread and large Doppler shift. Their transfer characteristics are influenced by many factors, such as: the operating frequency; the acoustic characteristics of sea surface and bottom; the ocean sound speed profile; the water depth; the depth and distance between the transmitters and the receivers; the variations of channel boundary; and, subsea objects. A time-varying channel impulse response has both deterministic and stochastic characteristics in a shallow water environment. Given the ocean environmental parameters, the deterministic impulse response can be calculated exactly by using underwater sound propagation models. However, it is extremely difficult to predict the stochastic impulse response due to its complexity. The method of ray tracing is quicker and more efficient than other methods such as with normal modes, parabolic equation and wave number integration in order to predict underwater water acoustic channels. At high frequencies, the ray tracing method is as accurate as others. Therefore, the ray tracing method has been widely used to simulate the channel impulse response in underwater acoustic communications. Here we focus on the impact of sea waves on the performance of single-carrier coherent underwater acoustic communications. Assuming that the sea wave is a single sinusoidal wave, we modify the BELLHOP ray module included in the Acoustic Toolbox in order to calculate the time-varying channel impulse response in a shallow water environment. Four time-varying channel impulse responses are presented for sea waves with a wave length of 50.0 m, and wave heights of 0.0, 0.5, 1.0 and 2.0 m. Furthermore, we investigate the impact of the wave height on the performance of the single-carrier coherent underwater acoustic communication system. Simulations demonstrate that bit error rates (BERs) of the system remain unchanged with time when the wave height equals 0.0 m. However, BERs change rapidly with time when the wave height is greater than 0.0 m. The higher the wave height, the faster the channel impulse response changes with time, and as a result, the higher the mean BER.

## Multiple error detection and correction over GF(2m) using novel cross parity code

- **ID**: ieee:7726963
- **Type**: conference
- **Published**: 7-8 Jan. 2
- **Authors**: M. Selva Sundary, V. Logisvary
- **PDF**: https://ieeexplore.ieee.org/document/7726963
- **Abstract**: Communication becomes most important in today's life. The world is dreaded to think beyond any communication gadgets. Data communication basically involves transfers of data from one place to another or from one point of time to another. Error may be introduced by the channel which makes data unreliable for user. Hence we need different error detection and error correction schemes. Our need is to achieve High speed and low complexity. The proposed work is to detect and correct a multiple error using low complexity novel cross parity code at lower overhead over GF(2m). It is able to correct m<;= Dw<;= 3m/2-1 multiple error combination out of all the possible 2m-1 error. Our proposed work is to test on 128 bit parallel and 163 bit (FIPT/NIST) standard word level GF multiplier and improve the efficiency of the circuit when compare to the existing work. Then we implement the design using VHDL, then simulated and synthesized using Modelsim SE 6 simulator and Xilinx ISE 6.3i respectively.

## Design of convolutional encoder and map decoder using dual mode MLMAP decoding algorithm

- **ID**: ieee:7727013
- **Type**: conference
- **Published**: 7-8 Jan. 2
- **Authors**: S. Divya, P. Maniraj Kumar
- **PDF**: https://ieeexplore.ieee.org/document/7727013
- **Abstract**: Nowadays digital communication is very popular due to various advantages like less affected by noise and which can be easily regenerated by various decoding algorithms. In order to correct the error occurring while transmitting the message through communication channel, the forward error correction (FEC) coding is used. In this FEC method, the convolutional encoder provides a suitable mechanism to limit the effects of noise in the digital communication channel. At the receiver side, turbo decoding is used due to better error correcting performance. Turbo decoding provides the iterative process so that, power and the speed is very critical parameter to analyze. The maximum a posteriori (MAP) decoder is recursive and complex, which makes the computation of decoding is difficult to realize. The log-map algorithm is used in the turbo decoding with the exponential correction term by means of jacobian logarithm method which is also complex method. In this paper, we present the Max log MAP (MLMAP) algorithm with the less hardware sharing dual mode single binary (SB) and double binary (DB) method to reduce the power and the area of the decoder. This paper also provides the mathematical equation for calculating the various parameters.

## A base matrix method to construct column weight 3 quasi-cyclic LDPC codes with high girth

- **ID**: ieee:7562999
- **Type**: conference
- **Published**: 27-30 Jan.
- **Authors**: Abhishek Kalsi, Ambar Bajpai, Lunchakorn Wuttisittikulkij +1
- **PDF**: https://ieeexplore.ieee.org/document/7562999
- **Abstract**: This article presents a simple, less computational complexity method for constructing exponent matrix (3, K) of girth 8, 10 and 12 of quasi-cyclic low-density parity-check codes (QC-LDPC) based on generation of base matrix. The construction of code deals with generation of base matrix by a simple algorithm and element wise element method for girth 8, while only element wise element method for girth 10 and 12. These methods are flexible for block-column length K. The simulations are shown in comparison with some existing appreciable work.

## An implementation of low-density MDS array codes for data protection in distributed network data storage system

- **ID**: ieee:7562983
- **Type**: conference
- **Published**: 27-30 Jan.
- **Authors**: Nattakan Puttarak, Phisan Kaewprapha
- **PDF**: https://ieeexplore.ieee.org/document/7562983
- **Abstract**: We present an implementation of disk arrays(RAIDs) in distributed networked data storage environment by applying an error-correcting to accommodate fault tolerance feature. Any of the current state-of-the-art distributed file systems, such as MooseFS [1], can be used as an underlying data space where low density-MDS (Maximum distance separable-Low density parity check) array codes [3] is used as a logical protection layer implemented through FUSE interface (File System In User Space). The redundancy/parity scheme is based on graph structures leading to an MDS code, then can be simply implemented in a parity matrix (H matrix) of an LDPC code. The ability of error correction and data recovery is shown as the bit-error rate (BER) has been investigated. It achieves the same trend compared to the simulation results in [3]. The low-density MDS array code can mitigate hardware failure at higher disk space efficiency comparing to the repetition code.

## Rapid prototyping of multi-mode QC-LDPC decoder for 802.11n/ac standard

- **ID**: ieee:7427981
- **Type**: conference
- **Published**: 25-28 Jan.
- **Authors**: Qing Lu, Chiu-Wing Sham, Francis C. M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/7427981
- **Abstract**: A multi-mode QC-LDPC decoder is proposed to satisfy the 802.11n/ac WiFi standard. With code-specific design, the overall performance of the decoder is enhanced while ensuring an on-the-fly reconfigurable ability. The proposed architecture has been synthesized using an FPGA for measurements. A state-of-art error rate and implementation complexity are reported. Meanwhile, the throughput has been increased to range from 382 MHz to 1852 MHz.

## Assessing CPA resistance of AES with different fault tolerance mechanisms

- **ID**: ieee:7428087
- **Type**: conference
- **Published**: 25-28 Jan.
- **Authors**: Hoda Pahlevanzadeh, Jaya Dofe, Qiaoyan Yu
- **PDF**: https://ieeexplore.ieee.org/document/7428087
- **Abstract**: Countermeasures for Advanced Encryption Standard (AES) to thwart side-channel attack and fault attack are typically investigated in a separate fashion. There is lack of thorough investigation on how one countermeasure specifically for one attack affects the efficiency of another attack. In this work, we consider three different fault detection (FD) methods - double modular redundancy (DMR), inverse function (inverse), and even parity check code (parity). We perform FPGA-based systematic analysis to investigate the impact of FD schemes on the correlation power analysis (CPA) resistance of a complete AES implementation. Moreover, the power model used in the existing work is Hamming weight rather than the powerful Hamming distance one. Our experimental results show that, in some scenarios, the use of fault detection mechanisms in AES improves the resistance against CPA. For instance, applying a parity FD to the AES's S-Box makes it harder to retrieve the key than the case without any FD protection.

## Polysynchronous stochastic circuits

- **ID**: ieee:7428060
- **Type**: conference
- **Published**: 25-28 Jan.
- **Authors**: M. Hassan Najafi, David J. Lilja, Marc Riedel +1
- **PDF**: https://ieeexplore.ieee.org/document/7428060
- **Abstract**: Clock distribution networks (CDNs) are costly in high-performance ASICs. This paper proposes a new approach: splitting clock domains at a very fine level, down to the level of a handful of gates. Each domain is synchronized with an inexpensive clock signal, generated locally. This is possible by adopting the paradigm of stochastic computation, where signal values are encoded as random bit streams. The design method is illustrated with the synthesis of circuits for applications in signal and image processing.

## A Survey on Programmable LDPC Decoders

- **ID**: ieee:7523326
- **Type**: journal
- **Published**: 2016
- **Authors**: Joao Andrade, Gabriel Falcao, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/7523326
- **Abstract**: Low-density parity-check (LDPC) block codes are popular forward error correction schemes due to their capacity-approaching characteristics. However, the realization of LDPC decoders that meet both low latency and high throughput is not a trivial challenge. Usually, this has been solved with the ASIC and FPGA technology that enables meeting the decoder design constraints. But the rise of parallel architectures, such as graphics processing units, and the scaling of CPU streaming extensions has shown that multicore and many-core technology can provide a flexible alternative to the development of dedicated LDPC decoders for the compute-intensive prototyping phase of the design of new codes. Under this light, this paper surveys the most relevant publications made in the past decade to programmable LDPC decoders. It looks at the advantages and disadvantages of parallel architectures and data-parallel programming models, and assesses how the design space exploration is pursued regarding key characteristics of the underlying code and decoding algorithm features. This paper concludes with a set of open problems in the field of communication systems on parallel programmable and reconfigurable architectures.

## Improving the Tolerance of Stochastic LDPC Decoders to Overclocking-Induced Timing Errors: A Tutorial and a Design Example

- **ID**: ieee:7446275
- **Type**: journal
- **Published**: 2016
- **Authors**: Xin Zuo, Isaac Perez-Andrade, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7446275
- **Abstract**: Channel codes, such as low-density parity-check (LDPC) codes, may be employed in wireless communication schemes for correcting transmission errors. This tolerance to channel-induced transmission errors allows the communication schemes to achieve higher transmission throughputs, at the cost of requiring additional processing for performing LDPC decoding. However, this LDPC decoding operation is associated with a potentially inadequate processing throughput, which may constrain the attainable transmission throughput. In order to increase the processing throughput, the clock period may be reduced, albeit this is at the cost of potentially introducing timing errors. Previous research efforts have considered a paucity of solutions for mitigating the occurrence of timing errors in channel decoders, by employing additional circuitry for detecting and correcting these overclocking-induced timing errors. Against this background, in this paper, we demonstrate that stochastic LDPC decoders (LDPC-SDs) are capable of exploiting their inherent error correction capability for correcting not only transmission errors, but also timing errors, even without the requirement for additional circuitry. Motivated by this, we provide the first comprehensive tutorial on LDPC-SDs. We also propose a novel design flow for timing-error-tolerant LDPC decoders. We use this to develop a timing error model for LDPC-SDs and investigate how their overall error correction performance is affected by overclocking. Drawing upon our findings, we propose a modified LDPC-SD, having an improved timing error tolerance. In a particular practical scenario, this modification eliminates approximately 1-dB performance degradation that is suffered by an overclocked LDPC-SD without our modification, enabling the processing throughput to be increased by up to 69.4%, which is achieved without compromising the error correction capability or processing energy consumption of the LDPC-SD.

## Finite Length Analysis of Low-Density Parity-Check Codes on Impulsive Noise Channels

- **ID**: ieee:7809141
- **Type**: journal
- **Published**: 2016
- **Authors**: Zhen Mei, Martin Johnston, Stéphane Le Goff +1
- **PDF**: https://ieeexplore.ieee.org/document/7809141
- **Abstract**: Low-density parity-check (LDPC) codes with very long block lengths are well known for their powerful error correction, but it is not always desirable to employ long codes in communication systems, where latency is a serious issue, such as voice and video communication between multiple users. Finite length analyses of LDPC codes have already been presented in the literature for the additive white Gaussian noise channel, but in this paper, we consider the finite length analysis of LDPC codes for channels that exhibit impulsive noise. First, an exact uncoded bit error probability (BEP) of an impulsive noise channel, modeled as a symmetric α-stable (SαS) distribution, is derived. Then, to obtain the LDPC-coded performance, density evolution is applied to evaluate the asymptotic performance of LDPC codes on SαS channels and determine the threshold signal-to-noise ratio. Finally, we derive closed-form expressions for the BEP and block error probability of short LDPC codes on these channels, which are shown to match closely with simulated results on channels with different levels of impulsiveness, even for block lengths as low as 1000 b.

## Mathematical Models for Simulating Coded Digital Communication: A Comprehensive Tutorial by Big Data Analytics in Cyber-Physical Systems

- **ID**: ieee:7784815
- **Type**: journal
- **Published**: 2016
- **Authors**: Guo Sheng, Xinya Zhao, Hangdong Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7784815
- **Abstract**: In this paper, we first present the significance of information theory and several commonly referred concepts associated with it. Then, the communication channel models constructed by information theory are briefly introduced. Meanwhile, the channel capacity, as a key role in modeling a channel, is expatiated. In addition, source coding and channel coding are compared and explained with a number of simulations. By reading this paper, the readers are expected to understand the significance of information theory as well as the indispensable roles of source coding and channel coding in a communication system. Furthermore, most of the techniques and fundamentals introduced and analyzed in this paper are feasible for the big data analytics in cyber-physical systems, which pave the way for coding over these newborn systems.

## Stochastic Computing Improves the Timing-Error Tolerance and Latency of Turbo Decoders: Design Guidelines and Tradeoffs

- **ID**: ieee:7403849
- **Type**: journal
- **Published**: 2016
- **Authors**: Isaac Perez-Andrade, Shida Zhong, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7403849
- **Abstract**: Stochastic computing has been recently proposed for the hardware implementation of both low-density parity-check (LDPC) decoders and turbo decoders, which facilitate near-optimal error correction capabilities in wireless communication applications. Previous contributions have demonstrated that stochastic LDPC decoders offer an attractive tradeoff between their error correction capabilities, hardware performance, and timing-error tolerance. Motivated by this, we propose a pair of stochastic turbo decoder (STD) designs having significantly enhanced timing-error tolerance and significantly reduced processing latency. Moreover, we characterize the tradeoffs between chip area, energy efficiency, latency, throughput, and error correction capabilities of both the timing-error-tolerant STD and of the reduced-latency STD. We demonstrate that our proposed timing-error-tolerant STD operated at 1.20 V, with a clock period of 2.2 ns and in the presence of a three-standard deviation power supply variation of 7%, exhibits an unimpaired performance, compared with the state-of-the-art STD, operated at 1.20 V and 4 ns and with no power supply variations. This corresponds processing throughput improvement by a factor of 2.42 and energy consumption reduction by a factor of 4. Finally, we demonstrate that our proposed reduced-latency STD has a processing latency that is an order of magnitude lower than that of the state-of-the-art STD. This is despite reducing the chip area by a factor of 4, increasing the processing throughput by a factor of 65, while consuming only 0.005 times the energy of the state-of-the-art STD, when using binary phase-shift keying for communication over an additive white Gaussian noise channel having Eb/N0 = 3 dB.

## Distributed Source Coding and Its Applications in Relaying-Based Transmission

- **ID**: ieee:7423654
- **Type**: journal
- **Published**: 2016
- **Authors**: Abdulah Jeza Aljohani, Soon Xin Ng, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/7423654
- **Abstract**: Distributed source coding (DSC) schemes rely on separate encoding but joint decoding of statistically dependent sources, which exhibit correlation. DSC has numerous promising applications ranging from reduced-complexity handheld video communications to onboard hyperspectral image coding under computational limitations. The concept of separate encoding at the first sight compromises the attainable encoding performance. However, the DSC theory proves that independent encoding can in fact be designed as efficiently as joint encoding, as long as joint decoding is allowed. More specifically, distributed joint source-channel coding (DJSC) is associated with the scenario, where the correlated source signals are transmitted through a noisy channel. In this paper, we present a concise historic background of DSC concerning both its theory and its practical aspects. In addition, a series of turbo trellis-coded modulation (TTCM)-aided DJSC-based cooperative transmission schemes are proposed. DJSC scheme is conceived for the transmission of a pair of correlated sources to a destination node (DN). The first source sequence is TTCM encoded, and then, it is compressed before it is transmitted both over a Rayleigh fading channel, where the second source signal is assumed to be perfectly decoded side-information at the DN for the sake of improving the achievable decoding performance of the first source. The proposed scheme is capable of performing reliable communications for various levels of correlation near to the theoretical Slepian-Wolf/Shannon (SW/S) limit. Pursuing our objective of designing practical DJSC schemes, we further extended the above-mentioned arrangement to a more realistic cooperative communication system, where the pair of correlated sources are transmitted to a DN with the aid of a relay node (RN). Explicitly, the pair of correlated source sequences are TTCM encoded and compressed before transmission over a Rayleigh fading multiple access channel, where our proposed scheme is capable of operating within 0.55 dB from the SW/S limit for a correlation coefficient value of ρ = 0.8, and within 0.07 bits of the minimum SW compression rate. The RN transmits both users' signal with the aid of a powerful superposition modulation technique that judiciously allocates the transmit power between the two signals. The correlation is beneficially exploited at both the RN and the DN using our powerful iterative joint decoder, which is optimized using extrinsic information transfer characteristics charts.

## Subcarrier-Index Modulation Aided OFDM - Will It Work?

- **ID**: ieee:7469311
- **Type**: journal
- **Published**: 2016
- **Authors**: Naoki Ishikawa, Shinya Sugiura, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/7469311
- **Abstract**: The achievable performance of subcarrier-index modulation (SIM) is analyzed in terms of its minimum Euclidean distance, constrained and unconstrained average mutual information, as well as its peak-to-average power ratio (PAPR). Our performance investigations identify the beneficial operating region of the SIM scheme over its conventional orthogonal frequency-division multiplexing (OFDM) counterpart, hence providing general design guidelines for the SIM parameters. More specifically, an SIM scheme is shown to be beneficial for the scenario of a relatively low transmission rate below 2 b/s/Hz. In addition, we demonstrate that the PAPR of the SIM scheme is comparable with that of its OFDM counterpart under the idealized simplifying assumption of having Gaussian input symbols.

## Fountain Coded Cooperative Communications for LTE-A Connected Heterogeneous M2M Network

- **ID**: ieee:7551214
- **Type**: journal
- **Published**: 2016
- **Authors**: Ahasanun Nessa, Michel Kadoch, Bo Rong
- **PDF**: https://ieeexplore.ieee.org/document/7551214
- **Abstract**: Machine-to-machine communication over long-term evolution advanced (LTE-A) network has emerged as a new communication paradigm to support a variety of applications of Internet of Things. One of the most effective techniques to accommodate a large volume of machine type communication (MTC) devices in LTE-A is clustering where devices (nodes) are grouped into number of clusters and forward their traffics to the base station (e.g., LTE eNodeB) through some special nodes called cluster heads (CHs). In many applications, the CHs change location with time that causes variation in distances between neighboring CHs. When these distances increase, the performance of data transmission may degrade. To address this issue, we propose to employ intermediate non-CH nodes as relays between neighboring CHs. Our solution covers many aspects from relay selection to cooperative formation to meet the user's QoS requirements. As the number of total relay plays a significant role in cooperative communications, we first design a rateless-coded-incremental-relay selection algorithm based on greedy techniques to guarantee the required data rate with a minimum cost. After that, we develop both source-feedback and non-source-feedback-based fountain coded cooperative communication protocols to facilitate the data transmission between two neighbor CHs. Numerical results are presented to demonstrate the performance of these protocols with different relay selection methods under Rayleigh fading channel. It shows that the proposed source-feedback-based protocol outperforms its non-source-feedbackprotocol counterpart in terms of a variety of metrics.

## Reduced-Packet-Delay Generalized Buffer-Aided Relaying Protocol: Simultaneous Activation of Multiple Source-to-Relay Links

- **ID**: ieee:7501454
- **Type**: journal
- **Published**: 2016
- **Authors**: Miharu Oiwa, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/7501454
- **Abstract**: Motivated by the recent buffer-aided relaying protocol that selects the best available link at each time slot, we herein introduce an additional degree of freedom to the protocol by simultaneously exploiting multiple links between the source node and the multiple buffer-aided relay nodes, which is enabled owing to the broadcast nature of wireless channels. More specifically, the proposed schemes are designed to allow multiple relay nodes to receive a source packet through source-to-relay broadcast channels, resulting in multiple copies of the source packet, which are stored in relay node buffers. As the explicit benefits of its increased design degree of freedom, the proposed protocols attain a significantly lower end-to-end packet delay than the conventional buffer-aided relaying protocols, which is achieved without imposing any substantial penalty on the achievable outage probability. Furthermore, the proposed protocol is capable of reducing the overhead required for monitoring the available links and buffer statuses of the relay nodes. Based on the Markov chain model, we derive the theoretical bounds of the outage probabilities of the proposed protocols.

## 1.5 Gbit/s FPGA Implementation of a Fully-Parallel Turbo Decoder Designed for Mission-Critical Machine-Type Communication Applications

- **ID**: ieee:7539551
- **Type**: journal
- **Published**: 2016
- **Authors**: An Li, Peter Hailes, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/7539551
- **Abstract**: In wireless communication schemes, turbo codes facilitate near-capacity transmission throughputs by achieving reliable forward error correction. However, owing to the serial data dependencies imposed by the underlying logarithmic Bahl-Cocke-Jelinek-Raviv (Log-BCJR) algorithm, the limited processing throughputs of conventional turbo decoder implementations impose a severe bottleneck upon the overall throughputs of real-time wireless communication schemes. Motivated by this, we recently proposed a fully parallel turbo decoder (FPTD) algorithm, which eliminates these serial data dependencies, allowing parallel processing and hence offering a significantly higher processing throughput. In this paper, we propose a novel resource-efficient version of the FPTD algorithm, which reduces its computational resource requirement by 50%, which enhancing its suitability for field-programmable gate array (FPGA) implementations. We propose a model FPGA implementation. When using a Stratix IV FPGA, the proposed FPTD FPGA implementation achieves an average throughput of 1.53 Gb/s and an average latency of 0.56 μs, when decoding frames comprising N = 720 b. These are, respectively, 13.2 times and 11.1 times superior to those of the state-of-the-art FPGA implementation of the Log-BCJR long-term evolution (LTE) turbo decoder, when decoding frames of the same frame length at the same error correction capability. Furthermore, our proposed FPTD FPGA implementation achieves a normalized resource usage of 0.42 (kALUTs/Mb/s), which is 5.2 times superior to that of the benchmarker decoder. Furthermore, when decoding the shortest N = 40-b LTE frames, the proposed FPTD FPGA implementation achieves an average throughput of 442 Mb/s and an average latency of 0.18 μs, which are, respectively, 21.1 times and 10.6 times superior to those of the benchmarker decoder. In this case, the normalized resource usage of 0.08 (kALUTs/Mb/s) is 146.4 times superior to that of the benchmarker decoder.

## An Intertrack Interference Subtraction Scheme for a Rate-4/5 Modulation Code for Two-Dimensional Magnetic Recording

- **ID**: ieee:7511764
- **Type**: journal
- **Published**: 2016
- **Authors**: Kotchakorn Pituso, Chanon Warisarn, Damrongsak Tongsomporn +1
- **PDF**: https://ieeexplore.ieee.org/document/7511764
- **Abstract**: The performance of a rate-4/5 modulation code is evaluated in two-dimensional magnetic recording (TDMR) channels, where a magnetic medium is described by a discrete Voronoi model, and the two-dimensional sensitivity function of the reader is adopted to generate the TDMR readback signal. Since the read-head sensitivity function covers many tracks, it causes intertrack interference (ITI) that can deteriorate the system performance. Therefore, this letter proposes an ITI subtraction scheme in conjunction with the rate-4/5 modulation code in a coded TDMR channel to mitigate the ITI effect embedded in the readback signals before performing an iterative decoding process. We also investigate the data-dependent readback amplitude distributions and evaluate the TDMR system performance via computer simulation. Results show that the proposed scheme helps improve the TDMR system performance, especially when the areal density is high.

## Protocols and Mechanisms to Recover Failed Packets in Wireless Networks: History and Evolution

- **ID**: ieee:7517301
- **Type**: journal
- **Published**: 2016
- **Authors**: Sheraz Ali Khan, Muhammad Moosa, Farhan Naeem +2
- **PDF**: https://ieeexplore.ieee.org/document/7517301
- **Abstract**: The emergence of multihop wireless networks and the increase in low-latency demands of error tolerant applications, such as voice over internet protocol, have triggered the development of new protocols and mechanisms for recovering failed packets. For example, recovering partially corrupt packets instead of retransmission has emerged as an effective way to improve key network performance metrics, such as goodput, latency, and energy consumption. A number of similar and interesting solutions have been proposed recently to either reconstruct or process corrupt packets on wireless networks. The proliferation of multimedia services on 3G and long term evolution networks, and the stringent quality of service requirements for these applications have given birth to robust codes and new error tolerant mechanisms for packet delivery. Despite years of active research in the field, we lack a comprehensive survey that summarizes recent developments in this area and highlights avenues with potential for future growth. This survey tries to fill in this void by providing a comprehensive review of the evolution of this field and underscoring areas for future research.

## Historical Information Aware Unequal Error Protection of Scalable HEVC/H.265 Streaming Over Free Space Optical Channels

- **ID**: ieee:7556280
- **Type**: journal
- **Published**: 2016
- **Authors**: Yongkai Huo, Cheng Zhou, Junyi Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7556280
- **Abstract**: Free space optical (FSO) systems are capable of supporting high data rates between fixed points in the context of flawless video communications. Layered video coding facilitates the creation of different-resolution subset layers for variable-throughput transmission scenarios. In this paper, we propose historical information aware unequal error protection (HA-UEP) for the scalable high efficiency video codec used for streaming over FSO channels. In particular, the objective function (OF) of the current video frame is designed based on historical information of its dependent frames. By optimizing this OF, specific subset layers may be selected in conjunction with carefully selected forward error correction coding rates, where the expected video distortion is minimized and the required bitrate is reduced under the constraint of a specific throughput. Our simulation results show that the proposed system outperforms the traditional equal error protection (EEP) scheme by about 4.5 dB of Eb/N0 at a peak signal-to-noise ratio of 33 dB. From a throughput-oriented perspective, HA-UEP is capable of reducing the throughput to about 30% compared with that of the EEP benchmarker, while achieving an Eb/N0 gain of 4.5 dB.

## A Fault-Tolerant L1 Cache with Predictable Performance by Virtual Filter Cache

- **ID**: ieee:8074442
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Zhi-Bin, M. Hua-Dong, Z. Feng +1
- **PDF**: https://ieeexplore.ieee.org/document/8074442
- **Abstract**: The Subblock-Disabling schemes have obviousadvantages on delays overhead and capacity loss. However, theexistence of cache line "holes" triggers abundant false hits andthe utilization of available cache capacity is low. A subblockdisablingbased no-collision set-level mending cache architectureVFCcache suited for low set-associative L1 cache is proposed. AnAdditional Tag Array is added and VFCcache is logically dividedinto two parts, MainCache and Virtual Filter Cache (VFC). Theno-collision set-level mending mechanism maybe causes thedivergence of practical associativity and faulty sets. VFC canmask these faulty sets, alleviate such divergence and make theperformance predictable. According to the experiments in Simics, the performance has an increase of 11.73% compared to theBuddy Cache for a 32KB 4-way L1 cache with a failureprobability of 0.004. The average miss rate of the L1-D has adecrease of 5.20% and that of the L1-I has a decrease of 5.02%for 29 benchmarks from SPEC CPU2000/2006 in comparisonwith Buddy Cache.

## Compressive cognitive radio with causal primary message

- **ID**: ieee:7794629
- **Type**: conference
- **Published**: 2016
- **Authors**: W. Xu, Y. Wang, J. Lin
- **PDF**: https://ieeexplore.ieee.org/document/7794629
- **Abstract**: Compressive sensing (CS) is an emerging theory in that it is possible to reconstruct sparse signals from far fewer measurements than traditional methods use. Existing studies utilizing CS in the field of cognitive radio network (CRN) mainly focus on spectrum sensing in interweave mode. However, few works concern about the application of CS in overlay CRNs. In this paper, we study the overlay CRN, which applies CS technology as a joint source-channel code. The secondary user (SU) not only sends its own message, but also employs decode-and-forward relaying strategy to help with primary transmission, where the primary message is obtained in a causal manner. Dirty paper coding is used to pre-cancel the interference of the primary message at the secondary receiver. We discuss the coding schemes when one SU and two SUs are in the CRN. To either case, we formulate the corresponding system optimization problem, which maximizes the secondary rate while satisfying the primary rate requirement. The performance of the proposed scheme is evaluated by numerical simulations and compared with the nonoptimal causal scheme and the non-causal scheme.

## Secure Communication Based on a Modified RB-HARQ Protocol

- **ID**: ieee:7917100
- **Type**: conference
- **Published**: 2016
- **Authors**: Q. Zou, B. Zhang, Z. Ye +1
- **PDF**: https://ieeexplore.ieee.org/document/7917100
- **Abstract**: This paper presents a secure communication scheme based on a modified Reliability-Based Hybrid Automatic Repeat reQuest (RB-HARQ) protocol over the additive white Gaussian noise (AWGN) wiretap channel. RB-HARQ protocol is firstly implemented in the secure communication system and showed a significant enhancement of the physical layer security. The retransmission encoding scheme is the main difference between traditional RB-HARQ and modified RB-HARQ, which can encode the unreliable bits of the authorized user (Bob) and retransmit the encoded unreliable bits through the AWGN wiretap channel. With the retransmission encoding scheme, the maximum retransmission number of RB-HARQ protocol can be largely reduced and secure communication can still be ensured, which is much more practical in long distance communication system. Bit error rate (BER) at both the authorized user (Bob) and eavesdropper (Eve) is used to assess the secrecy performance in this paper. So we calculate the BER of our proposed scheme through theoretical analysis and simulations. The results suggest that the modified RB-HARQ protocol can strongly enhance the reliability and security of our system, with the maximum retransmission number at a low level.

## Video cognitive radio networks for tactical scenarios

- **ID**: ieee:7860536
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Soysa, P. C. Cosman, L. B. Milstein
- **PDF**: https://ieeexplore.ieee.org/document/7860536
- **Abstract**: We examine the performance of uplink video transmission over a mobile cognitive radio (CR) system operating in a hostile environment where an intelligent adversary tries to disrupt communications. We investigate the optimal strategy for spoofing, desynchronizing and jamming a cluster-based CR network with a Gaussian noise signal, over a Rayleigh fading channel. The adversary can limit access for secondary users (SUs) by either transmitting a spoofing signal in the sensing interval, or a desynchronizing signal to disrupt code acquisition by SUs or the cluster head. By jamming the network during the transmission interval, the adversary can reduce the rate of successful transmission. We also propose cross-layer resource allocation algorithms and evaluate their performance under disruptive attacks.

## Optimization of iterative PIC-MMSE based detection with symbol mapping

- **ID**: ieee:7833615
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Zhang, C. Li, S. Ahmed +1
- **PDF**: https://ieeexplore.ieee.org/document/7833615
- **Abstract**: Recently, the iterative detection and decoding technique based on parallel interference cancellation with minimum mean square error (PIC-MMSE) has received considerable attention. To improve the performance, the detector usually adopts a self-iteration which iteratively estimate the soft bit information (SBI). This paper proposes two main idea to improve the performance as well as to reduce the complexity of the PIC-MMSE based MIMO detector. In order to reduce the complexity, we map PIC-MMSE filtered symbol to a specific region so that the detector does not require any search process to find the minima. In addition, we propose an optimization technique to increase the reliability of the soft symbols. Simulation results show that the complexity of the proposed method is reduced to linear-order without performance degradation, and the proposed optimization method can efficiently improve the performance with reasonable complexity.

## Developed RAID DP with combined storage media

- **ID**: ieee:7560930
- **Type**: conference
- **Published**: 2016
- **Authors**: N. Y. Ali, V. M. Thakare
- **PDF**: https://ieeexplore.ieee.org/document/7560930
- **Abstract**: Different storage media have different performance in terms of fetching data. Most powerful one is RAM that has characteristics making it fast to serve I/O processes. Then, we have flash memory that has high performance of read tasks but less in write ones. Third one is HDD which is the slowest but most reliable in terms of preserving data. In this model, we used a combination of the first and third one to form a developed structure of RAID DP that has a much better performance. For parity disk drives, we used DRAM memory for its great performance. Because parity disks are the most overloaded with write processes. RAID 1 is also used as inner RAID system to preserve data stored in DRAM SSD (Solid State Drive) to HDD.

## Space-time coding-assisted transmission for mitigation of MDL impact on mode-division multiplexed signals

- **ID**: ieee:7537474
- **Type**: conference
- **Published**: 2016
- **Authors**: K. Shibahara, T. Mizuno, H. Takara +6
- **PDF**: https://ieeexplore.ieee.org/document/7537474
- **Abstract**: A method is described for applying space-time coding implemented by Hadamard transform to SDM transmission. Experiments demonstrated that the method substantially improves mode dependent loss tolerance and enables transmission reach to be enhanced by 20%.

## A novel scheme for telemetry system data rate optimization

- **ID**: ieee:7500762
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Liaghati, N. Chang, M. Liaghati +1
- **PDF**: https://ieeexplore.ieee.org/document/7500762
- **Abstract**: Limited telemetry bandwidth due to restricted radio frequency spectrum allocation is typically one of the most challenging problems when designing a telemetry system for space applications. To further complicate the problem, a large percentage of the allotted bandwidth is consumed by the over-head required by each packet to follow various standards and layer of protocols used in the telemetry system. This results in inefficiency in the actual telemetry data downlinked to the ground station. In the typical telemetry design, only one virtual channel is used per packet. As a result, in order to achieve the required packet size, filled data is inserted into the remaining bits. This Idle Packet consists of a set pattern of binary digits, and is considered part of the overhead, as its sole purpose is to fill the packet. In this work, a new scheme is proposed which takes advantage of the empty bits by starting the next virtual channel instead of inserting filled bits. This method will reduce the overall amount of overheard, in addition to allowing more data to be transmitted.

## Real-time 70 Gbit/s, 128 QAM Quantum Noise Stream Cipher Transmission over 100 km with Secret Keys Delivered by Continuous Variable Quantum Key

- **ID**: ieee:7767755
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Nakazawa, M. Yoshida, T. Hirooka +2
- **PDF**: https://ieeexplore.ieee.org/document/7767755
- **Abstract**: We demonstrate a real-time quantum noise stream cipher transmission with a continuous variable quantum key distribution system to greatly increase encryption security. 70 Gbit/s, 128 QAM encrypted data have been successfully transmitted over 100 km.

## Probabilistically Shaped QAM for Independent Reach, Spectral Efficiency and Bit-rate Adaptation

- **ID**: ieee:7767614
- **Type**: conference
- **Published**: 2016
- **Authors**: F. Buchali, W. Idler, L. Schmalen +3
- **PDF**: https://ieeexplore.ieee.org/document/7767614
- **Abstract**: In this paper we review probabilistically shaped constellations and experimentally investigate probabilistically shaped QAM systems operated at both high bit-rate and high reach requiring high baudrate transmission. We demonstrate up to 29% reach increase by probabilistic shaping.

## Carrier phase recovery without pilot symbols for non-differential coherent receivers

- **ID**: ieee:7537622
- **Type**: conference
- **Published**: 2016
- **Authors**: M. A. Castrillon, D. A. Morero, M. R. Hueda
- **PDF**: https://ieeexplore.ieee.org/document/7537622
- **Abstract**: We propose a time-domain hybrid modulation technique to eliminate the cycle-slip problem in non-differential coherent receivers. The method avoids the use of pilot symbols for carrier phase recovery, achieving 0.8 dB gain over differential modulation.

## Latency and bandwidth programmable transceivers with power arbitration among multi-tenanted signals

- **ID**: ieee:7537805
- **Type**: conference
- **Published**: 2016
- **Authors**: T. Tanimura, L. Dou, X. Su +6
- **PDF**: https://ieeexplore.ieee.org/document/7537805
- **Abstract**: We propose and experimentally demonstrate novel optical transceiver that enables accommodation of multiple services having diverse requirements within the bandwidth of the single transceiver by a holistic SNR optimization of signal assigned for each service.

## Improved OFDM Decoder for LTE and Beyond

- **ID**: ieee:7881481
- **Type**: conference
- **Published**: 2016
- **Authors**: N. S. Živić, O. Ur-Rehman
- **PDF**: https://ieeexplore.ieee.org/document/7881481
- **Abstract**: Orthogonal Frequency Division Multiplexing, together with Multiple-Input Multiple-Output, is a pillar technique for new generation mobile networks, i.e., for the mobile networks in direction of 5G. Its crucial properties of robustness against fading and Inter-symbol Interference make it a great choice for the demanding data rates of future mobile networks. This paper presents a technique for additional improvement of the Orthogonal Frequency Division Multiplexing error resilience properties, when combined with soft decoding techniques and additional redundancy for error recognition.

## Soft-Decision Decoding in Noncoherent Massive MIMO Systems

- **ID**: ieee:7499102
- **Type**: conference
- **Published**: 2016
- **Authors**: G. Yammine, R. F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/7499102
- **Abstract**: Noncoherent multi-user detection schemes are attractive in massive MIMO uplink systems. In particular, sorted decision-feedback differential detection (DFDD) in combination with noncoherent decision-feedback equalization (nDFE) over the users has been shown to perform well, avoiding the need for channel estimation. So far, integrating channel coding in massive MIMO systems requires knowledge of the channel, where reliability information for the bits is calculated after combining a large number of symbol observations at the receiver. In this paper, we address one method to calculate reliability information by augmenting the sorted decision-feedback differential detection process. To this end, an equivalent trellis-encoder representation of bit-to-symbol mapping and differential encoding is established. Based on this, log-likelihood ratios for the differential symbols can be calculated. The performance of soft-decision decoding in noncoherent massive MIMO systems is assessed by means of numerical simulations and compared to that of a coherent scheme using channel estimation.

## Advanced Receiver Design enables PDM-16QAM DWDM Transmission over 2660 km of SSMF with Only EDFA

- **ID**: ieee:7769421
- **Type**: conference
- **Published**: 2016
- **Authors**: X. Wang, S. Calabro, B. Spinnler +2
- **PDF**: https://ieeexplore.ieee.org/document/7769421
- **Abstract**: We demonstrate experimental DWDM PDM-16QAM transmission at 200 Gb/s over 2660 km of SSMF, using EDFA-only amplification and advanced DSP techniques, including powerful digital predistortion, iterative carrier recovery and decoding using 50% OH soft-decision FEC.

## Non-Uniform Signaling Based LDPC Coded Modulation for High-Speed Optical Transport Networks

- **ID**: ieee:8680233
- **Type**: conference
- **Published**: 2016
- **Authors**: T. Liu, Z. Qu, C. Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8680233
- **Abstract**: Different non-uniform (probability shaping) signaling schemes are introduced in this invited paper. By transmitting symbols with different probabilities, energy efficiency (shaping gain) of traditional schemes can be improved. With constellation points selected according to Maxwell-Boltzmann distribution, ultimate shaping gain of 1.53dB can be achieved.

## Hardware complexity reduction of LDPC-CC decoders based on message-passing approaches

- **ID**: ieee:7952003
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Ben Thameur, C. Bouzouita, N. Khouja +3
- **PDF**: https://ieeexplore.ieee.org/document/7952003
- **Abstract**: LDPC convolutional codes (LDPC-CC) are a family of error-correcting codes (ECC) used in digital communication systems like the IEEE 1901 standard. High throughput and low complexity hardware architectures were designed for real time systems. In this article we demonstrate that an efficient selection of the message passing (MP) algorithm for LDPC-CC decoding improves the architecture features of related works. In fact, considering the LDPC-CC decoders proposed for the IEEE 1901 standard, we show that an appropriate Min-Sum approximation selection can significantly improve the error correction performance by 0.1 to 0.2 dB in terms of Bit Error Ratio. It can also reduce the hardware complexity by 10% to 20% with no impact on the Bit Error Ratio performance.

## The weight consistency matrix framework for general non-binary LDPC code optimization: Applications in flash memories

- **ID**: ieee:7541791
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Hareedy, C. Lanka, C. Schoeny +1
- **PDF**: https://ieeexplore.ieee.org/document/7541791
- **Abstract**: Transmission channels underlying modern memory systems, e.g., Flash memories, possess a significant amount of asymmetry. While existing LDPC codes optimized for symmetric, AWGN-like channels are being actively considered for Flash applications, we demonstrate that, due to channel asymmetry, such approaches are fairly inadequate. We propose a new, general, combinatorial framework for the analysis and design of non-binary LDPC (NB-LDPC) codes for asymmetric channels. We introduce a refined definition of absorbing sets, which we call general absorbing sets (GASs), and an important subclass of GASs, which we refer to as general absorbing sets of type two (GASTs). Additionally, we study the combinatorial properties of GASTs. We then present the weight consistency matrix (WCM), which succinctly captures key properties in a GAST. Based on these new concepts, we then develop a general code optimization framework, and demonstrate its effectiveness on the realistic highly-asymmetric normal-Laplace mixture (NLM) Flash channel. Our optimized codes enjoy over one order (resp., half of an order) of magnitude performance gain in the uncorrectable BER (UBER) relative to the unoptimized codes (resp. the codes optimized for symmetric channels).

## Joint channel coding network coding for multi-way relay systems

- **ID**: ieee:7556045
- **Type**: conference
- **Published**: 2016
- **Authors**: W. Liu
- **PDF**: https://ieeexplore.ieee.org/document/7556045
- **Abstract**: Physical layer network coding (PNC) with channel coding is a strategy that applies error correction at the relay nodes of a relay system to improve data communication reliability of the whole relay system. So far, channel coded PNC schemes have been studied for two-way relay systems, but have not been systematically proposed for general multiple-way relay systems. In this paper, joint channel coding network coding schemes (JCCNC) are proposed for compute-and-forward (CF) relaying scheme that is able to be applied to general types of PAM and QAM modulation systems. LDPC codes are used for channel coding. Numerical results from simulation show that these JCCNC schemes greatly improve the performance of the relay systems.

## Error control coding combined with content recognition

- **ID**: ieee:7752591
- **Type**: conference
- **Published**: 2016
- **Authors**: J. Luo, Q. Huang, S. Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7752591
- **Abstract**: In modern communication systems, there is content redundancy inside the transmitted data no matter what source codes are adopted. This paper introduces machine learning method to utilize content redundancy and perform content recognition, in order to provide side information for error control coding (ECC) and improve performing. It shows that content recognition for English text, based on Trie and machine learning, is able to provide side information for ECC decoders. Moreover, content redundancy is independent of parity bits of error control codes. Iterative Turbo decoding is introduced to further enhance error performance. Simulation results show that the error performance of ECC can be significantly improved with the aid of content recognition.

## ASIC implementation of error detection and correction using high performance majority logic decoder

- **ID**: ieee:7807854
- **Type**: conference
- **Published**: 2016
- **Authors**: R. Pramod, V. Anandi, A. N. Aravind +1
- **PDF**: https://ieeexplore.ieee.org/document/7807854
- **Abstract**: Memory is an integral and important component in most of the digital circuits. It is basically used for storing and retrieving data in many electronic circuits. In recent days, the soft errors affecting digital circuits have become the biggest challenge for memory applications. As technology is scaling down, the effect of single error upsets (SEUs) on memories further increased the concern on their reliability. Therefore this paper attempts to put forth a majority logic decoder based error detection and correction methodology. Cyclic codes are the best candidates for memory applications because of their capacity to handle large number of errors. However, the conventional technique requires large number of decoding cycles which affects the memory performance. Therefore, in this paper an attempt is made to explore an efficient error detection technique that significantly increases the speed of accessing memory whenever data read is error free. Additionally it is ensured to keep area and power consumption of the technique at optimum level. Also, the results are verified in Cadence Encounter RTL compiler 13.10 tool using 180nm technology.

## Serially concatenated multiple parity-check codes for secure communication

- **ID**: ieee:7790441
- **Type**: conference
- **Published**: 2016
- **Authors**: X. -Q. Jiang, E. Bai, J. Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7790441
- **Abstract**: In this paper, two secure codes are studied for a Gaussian wiretap channel. These two secure codes are derived from Multiple Parity-Check (MPC) codes, therefore, have low encoding complexities. These two codes are called M-SC-MPC codes and M-QC-MPC codes, respectively, in this paper. Theoretical security analysis show that these codes guarantees perfect secrecy against an eavesdropper. Simulation results show that the bit error rate of the proposed codes is close to 0.5 at low SNR region and very low at high SNR region over the AWGN channel with iterative decoding.

## Noise-aided gradient descent bit-flipping decoders approaching maximum likelihood decoding

- **ID**: ieee:7593125
- **Type**: conference
- **Published**: 2016
- **Authors**: D. Declercq, C. Winstead, B. Vasic +3
- **PDF**: https://ieeexplore.ieee.org/document/7593125
- **Abstract**: In the recent literature, the study of iterative LDPC decoders implemented on faulty-hardware has led to the counter-intuitive conclusion that noisy decoders could perform better than their noiseless version. This peculiar behavior has been observed in the finite codeword length regime, where the noise perturbating the decoder dynamics help to escape the attraction of fixed points such as trapping sets. In this paper, we will study two recently introduced LDPC decoders derived from noisy versions of the gradient descent bit-flipping decoder (GDBF). Although the GDBF is known to be a simple decoder with limited error correction capability compared to more powerful softdecision decoders, it has been shown that the introduction of a random perturbation in the decoder could greatly improve the performance results, approaching and even surpassing belief propagation or min-sum based decoders. For both decoders, we evaluate the probability of escaping from a Trapping set, and relate this probability to the parameters of the injected noise distribution, using a Markovian model of the decoder transitions in the state space of errors localized on isolated trapping sets. In a second part of the paper, we present a modified scheduling of our algorithms for the binary symmetric channel, which allows to approach maximum likelihood decoding (MLD) at the cost of a very large number of iterations.

## HbbTV based Push-VOD services over DVB networks: Analysis and AL-FEC code application

- **ID**: ieee:7765395
- **Type**: conference
- **Published**: 2016
- **Authors**: F. Mattoussi, M. Crussière, J. -F. Hélard
- **PDF**: https://ieeexplore.ieee.org/document/7765395
- **Abstract**: Hybrid broadcast broadband TV (HbbTV) is an European initiative for providing viewers a richer experience of enhanced and interactive hybrid TV, through the launching of innovative hybrid services on both broadcast and broadband networks, allowing the viewer to interact with the current TV program. The latest release, HbbTV standard v2.0, provides additional features to HbbTV applications. Among the most important advancement of this version was the addition of the Push-VOD service. In this paper we focus on the broadcast method principle of Push-VOD services presented in the HbbTV v2.0. We investigate various technical aspects that have remained open questions in the standard to provide a first reference on the depth analysis of HbbTV based Push-VOD services. In addition, we propose and analyse a first solution for a reliable Push-VOD service delivery within file delivery protocol. This solution is based on the LDPC-Staircase AL-FEC codes using the hybrid (IT/ML) decoding method. Simulation results show that the merging of the repetition and the AL-FEC coding allows to inherit the benefits of both repetition and coding. A reliable file delivery is assured with low recovering complexity and download time.

## A Novel Interleaving Scheme for Polar Codes

- **ID**: ieee:7880865
- **Type**: conference
- **Published**: 2016
- **Authors**: Y. Meng, L. Li, Y. Hu
- **PDF**: https://ieeexplore.ieee.org/document/7880865
- **Abstract**: It's known that the bit errors of polar codes with successive cancellation (SC) decoding are coupled. We call the coupled information bits the correlated bits. In this paper, concatenation schemes are studied for polar codes and LDPC codes. In a conventional concatenation scheme, to achieve a better BER performance, one can divide all Nl bits in a LDPC block into Nl polar blocks to completely de-correlate the possible coupled errors. In this paper, we propose a novel interleaving scheme between a LDPC code and a polar code which breaks the correlation of the errors among the correlated bits. This interleaving scheme still keeps the simple SC decoding of polar codes while achieves a better BER performance than a direct concatenation of polar codes (with BP decoding) with LDPC codes. The proposed scheme also achieves a comparable BER performance (0.5dB difference) at a much smaller delay compared with a Nl block delay scheme.

## Channel Coding for Ultra-Reliable Low-Latency Communication in 5G Systems

- **ID**: ieee:7880930
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Sybis, K. Wesolowski, K. Jayasinghe +2
- **PDF**: https://ieeexplore.ieee.org/document/7880930
- **Abstract**: This paper investigates block error rate (BLER) performance and computational complexity of candidate channel coding schemes for ultra-reliable low latency communication (URLLC) in 5G. The considered candidates are the same as those identified in 3GPP: turbo, LDPC, polar, and convolutional codes. Details of code constructions and decoding algorithms are provided with computational complexity analysis. Code construction parameters, number of iterations, and list sizes are selected to provide a fair comparison among candidate coding schemes. Simulation results on BLER are shown for several code rates and small-to-moderate block sizes. The results reveal that polar and LDPC codes outperform turbo codes for short block sizes of 40 bits, while the opposite is true for medium block sizes of 200 bits. None of the schemes is a clear winner at all considered block sizes and coding rates. Other aspects like implementation complexity, latency, and flexibility will also be important when deciding the URLLC coding scheme.

## Non-surjective finite alphabet iterative decoders

- **ID**: ieee:7511111
- **Type**: conference
- **Published**: 2016
- **Authors**: T. T. Nguyen-Ly, K. Le, V. Savin +3
- **PDF**: https://ieeexplore.ieee.org/document/7511111
- **Abstract**: This paper introduces a new theoretical framework, akin to the use of imprecise message storage in Low Density Parity Check (LDPC) decoders, which is seen as an enabler for cost-effective hardware designs. The proposed framework is the one of Non-Surjective Finite Alphabet Iterative Decoders (NS-FAIDs), and it is shown to provide a unified approach for several designs previously proposed in the literature. NS-FAIDs are optimized by density evolution for WiMAX irregular LDPC codes and we show they provide different trade-offs between hardware complexity and decoding performance. In particular, we derive a set of 27 NS-FAIDs that provide decoding gains up to 0.36 dB, while yielding a memory/interconnect reduction up to 25%/30% compared to the Min-Sum decoder.

## Improved turbo product coding dedicated for 100 Gbps wireless terahertz communication

- **ID**: ieee:7794685
- **Type**: conference
- **Published**: 2016
- **Authors**: L. Lopacinski, J. Nolte, S. Buechner +2
- **PDF**: https://ieeexplore.ieee.org/document/7794685
- **Abstract**: In this article, an improved turbo product decoding scheme is proposed. The new method is almost as effective as hard decodable low-density parity check codes (HD-LDPC). Due to the modified codeword shape, no external interleavers are required to correct burst errors. If the decoder uses Reed-Solomon (RS) codes, then error correction performance against burst errors is significantly higher than the gain provided by HD-LDPC with an external interleaver. An additional advantage is a possibility to design a dedicated decoder for Virtex7 field programmable gate array (FPGA) serial transceivers. In our case, we use the method for 100 Gbps data link layer processor dedicated for wireless communication in the Terahertz band. The targeted platform is Virtex7 FPGA, but the solution can be easily scaled on other technologies.

## Performance comparison of short-length error-correcting codes

- **ID**: ieee:7797660
- **Type**: conference
- **Published**: 2016
- **Authors**: J. Van Wonterghem, A. Alloum, J. J. Boutros +1
- **PDF**: https://ieeexplore.ieee.org/document/7797660
- **Abstract**: We compare the performance of short-length linear binary codes on the binary erasure channel and the binary-input Gaussian channel. We use a universal decoder that can decode any linear binary block code: Gaussian-elimination based Maximum-Likelihood decoder on the erasure channel and probabilistic Ordered Statistics Decoder on the Gaussian channel. As such we compare codes and not decoders. The word error rate versus the channel parameter is found for LDPC, Reed-Muller, Polar, and BCH codes at length 256 bits. BCH codes outperform other codes in absence of cyclic redundancy check. Under joint decoding, the concatenation of a cyclic redundancy check makes all codes perform very close to optimal lower bounds.

## Coded Index Modulation for Non-DC-Biased OFDM in Multiple LED Visible Light Communication

- **ID**: ieee:7504166
- **Type**: conference
- **Published**: 2016
- **Authors**: S. P. Alaka, T. L. Narasimhan, A. Chockalingam
- **PDF**: https://ieeexplore.ieee.org/document/7504166
- **Abstract**: Use of multiple light emitting diodes (LED) is an attractive way to increase spectral efficiency in visible light communications (VLC). A non-DC-biased OFDM (NDC OFDM) scheme that uses two LEDs has been proposed in the literature recently. NDC OFDM has been shown to perform better than other OFDM schemes for VLC like DC-biased OFDM (DCO OFDM) and asymmetrically clipped OFDM (ACO OFDM) in multiple LEDs settings. In this paper, we propose an efficient multiple LED OFDM scheme for VLC which uses coded index modulation. The proposed scheme uses two transmitter blocks, each having a pair of LEDs. Within each block, NDC OFDM signaling is done. The selection of which block is activated in a signaling interval is decided by information bits (i.e., index bits). In order to improve the reliability of the index bits at the receiver (which is critical because of high channel correlation in multiple LEDs settings), we propose to use coding on the index bits alone. We call the proposed scheme as CI-NDC OFDM (coded index NDC OFDM) scheme. We present the performance results of CI-NDC OFDM scheme with the index bits coded by (i) LDPC and (ii) Walsh-Hadamard codes. Simulation results show that, for the same spectral efficiency, CI-NDC OFDM that uses coding on the index bits performs better than NDC OFDM.

## 3DIP: An iterative partitioning tool for monolithic 3D IC

- **ID**: ieee:7970013
- **Type**: conference
- **Published**: 2016
- **Authors**: G. Berhault, M. Brocard, S. Thuries +2
- **PDF**: https://ieeexplore.ieee.org/document/7970013
- **Abstract**: CoolCubeTM is a monolithic 3D (M3D) technology offering a vertical density of integration 20 times higher than face to face copper hybrid bonding (F2F Cu-Cu), thanks to ultra-thin Monolithic Inter-tier Vias (MIVs). In this work, we propose a new partitioning tool exploiting this characteristic for 2-tier Cell-on-Cell ICs before placement. It is based on a fast and iterative algorithm that explores the space of solutions and minimizes the estimated cost of wires with balanced area between tiers without limiting the number of MIVs. A mathematical formulation of the 3D partitioning problem and a comprehensive framework, based on simulated annealing (SA) algorithm coupled with a dedicated cost function, are detailed and compared with Min-Cut (MC) partitions commonly used. It appears that our solution can decrease the estimated total cost of wires by 41% and 45% for the LDPC and FFT/AES units. It also reduces the total cost of wires by 30% to 44% compared to the MC algorithm for the same units and with no significant increase in runtime.

## Weight distribution of the syndrome of linear codes and connections to combinatorial designs

- **ID**: ieee:7541857
- **Type**: conference
- **Published**: 2016
- **Authors**: C. Pacher, P. Grabenweger, D. E. Simos
- **PDF**: https://ieeexplore.ieee.org/document/7541857
- **Abstract**: The expectation and the variance of the syndrome weight distribution of linear codes after transmission of codewords through a binary symmetric channel are derived exactly in closed form as functions of the code's parity-check matrix and of the degree distributions of the associated Tanner graph. The influence of (check) regularity of the Tanner graph is studied. Special attention is payed to Tanner graphs that have no cycles of length four. We further study the equivalence of some classes of combinatorial designs and important classes of LDPC codes and apply our general results to those more specific structures. Simulations validate the analytical results and show that the actual cumulative distribution function of the syndrome weight is close to that of a normal distribution.

## Low-Complexity Detection for FTN Signaling Based on Weighted FG-SS-BP Equalization Method

- **ID**: ieee:7504329
- **Type**: conference
- **Published**: 2016
- **Authors**: T. Yu, M. Zhao, J. Zhong +1
- **PDF**: https://ieeexplore.ieee.org/document/7504329
- **Abstract**: In this paper, a low-complexity turbo detection scheme based on a weighted factor graph (FG) serial-schedule (SS) belief propagation (BP) equalization method is proposed for Faster-than-Nyquist (FTN) signaling. The iterative equalization method is applied to mitigate the severe intersymbol interference (ISI) introduced by FTN signaling. In order to reduce the complexity of the equalization method, Gaussian approximation (GA) is used to calculate the log-likelihood ratio (LLR). Thus, the computational complexity is merely linear with the number of ISI taps. Furthermore, LDPC, as an efficient coding technique, results in performance that approaches the Shannon limit in this turbo detection scheme. The simulation results show that the proposed weighted FG-SS-BP-based turbo detection method performs close to the optimal detector under ISI-free conditions with very low complexity.

## Soft output detection for MIMO systems using binary polar codes

- **ID**: ieee:7905658
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Diouf, I. Diop, I. Dioum +3
- **PDF**: https://ieeexplore.ieee.org/document/7905658
- **Abstract**: Polar codes are proven capacity-achieving and are shown to have equivalent or even better finite length performance than turbo/LDPC codes under some improved decoding algorithm over the Additive White Gaussian Noise (AWGN) channels. Polar coding is based on the so-called channel polarization phenomenon induced by a transform over the underlying binary-input channel. The channel polarization is found to be universal in many signal processing problems and is applied to the coded modulation schemes. In this paper, a small length polar, encoded for a MIMO (Multiple-Input Multiple-Output) systems with soft output MMSE-SIC (Minimum Mean Square Error-Successive Cancellation) detection, is applied to improve the coded performance while reducing the complexity. In order to prove this theory, we compare the proposed MMSE-SIC BER to Zero Forcing (ZF) and Maximum Likelihood (ML) by using 2*2 MIMO systems into Rayleigh channel with BPSK (Binary Phase-Shift Keying) modulation. Simulation results show that MMSE-SIC complexity is lower than the two others detections. We show that the performance of the proposed approach using polar code (128, 64) at 10-2 BER (Bit Error Rate) is around 3dB i.e. 0,66% compared to the optimal ML, while ZF performance is the worst.

## Wiener filter channel estimation for OFDM/OQAM with iterative interference cancellation in LTE channel

- **ID**: ieee:7584319
- **Type**: conference
- **Published**: 2016
- **Authors**: Y. J. Harbi, A. G. Burr
- **PDF**: https://ieeexplore.ieee.org/document/7584319
- **Abstract**: In this paper iterative interference cancellation (IIC) with Wiener filter (WF) channel estimation is proposed to eliminate the inherent intersymbol interference (ISI) and intercarrier interference (ICI) terms in Orthogonal Frequency Division Multiplex/Offset QAM (OFDM/OQAM). An iterative interference cancellation receiver is proposed using a Low-Density Parity-Check (LDPC) decoder with different patterns of scattered pilots under the effect of the timevariant LTE multipath channel. The bit error probability is compared with that of the conventional FFT-OFDM system with insufficient cyclic prefix (CP) under different environments. The results obtained show that the probability of error in the OFDM/OQAM scheme is improved in many scenarios.

## Hybrid Parity-Check and CRC Aided SCL Decoding for Polar Codes

- **ID**: ieee:7917180
- **Type**: conference
- **Published**: 2016
- **Authors**: Q. Yu, Z. Shi, Q. Yan +1
- **PDF**: https://ieeexplore.ieee.org/document/7917180
- **Abstract**: Polar codes under cyclic redundancy check-aided successive cancellation list (CA-SCL) decoding can outperform the turbo codes and the LDPC codes at the cost of high complexity and decoding delay. In order to reduce the decoding complexity, in this paper we propose a hybrid parity-check and CRC aided SCL decoding scheme for polar codes. Simulation results under the binary input additive white Gaussian noise channels (BI-AWGNs) show that, the proposed approach successfully provides over 20% complexity reduction, and 0.2dB performance gain over the traditional CA-SCL scheme with short codeword length at the block error probability (BLER) of 10-2.

## Improved Soft-Decision Forward Error Correction via Post-Processing of Mismatched Log-Likelihood Ratios

- **ID**: ieee:7767651
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Alvarado, L. Szczecinski, T. Fehenberger +2
- **PDF**: https://ieeexplore.ieee.org/document/7767651
- **Abstract**: Correction of soft information based on achievable information rates for SD-FEC is discussed. Linear scaling of LLRs is shown to offer gains of up to 0.75 dB for a rate 0.8 LDPC code in a channel dominated by phase noise.

## 65Tb/s Transoceanic Transmission Using Probabilistically-Shaped PDM-64QAM

- **ID**: ieee:7765589
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Ghazisaeidi, I. F. d. Jauregui Ruiz, R. Rios-Muller +8
- **PDF**: https://ieeexplore.ieee.org/document/7765589
- **Abstract**: We report on a C+L-band transoceanic transmission using capacity-approaching probabilistically-shaped 64QAM. Digital nonlinear compensation and adaptive-rate spatially-coupled LDPC decoding enable transmission of 65 Tb/s over 6600km, with spectral efficiency of 7.3 b/s/Hz.

## On locality of Generalized Reed-Muller codes over the broadcast erasure channel

- **ID**: ieee:7521914
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Alloum, S. -J. Lin, T. Y. Al-Naffouri
- **PDF**: https://ieeexplore.ieee.org/document/7521914
- **Abstract**: One to Many communications are expected to be among the killer applications for the currently discussed 5G standard. The usage of coding mechanisms is impacting broadcasting standard quality, as coding is involved at several levels of the stack, and more specifically at the application layer where Rateless, LDPC, Reed Slomon codes and network coding schemes have been extensively studied, optimized and standardized in the past. Beyond reusing, extending or adapting existing application layer packet coding mechanisms based on previous schemes and designed for the foregoing LTE or other broadcasting standards; our purpose is to investigate the use of Generalized Reed Muller codes and the value of their locality property in their progressive decoding for Broadcast/Multicast communication schemes with real time video delivery. Our results are meant to bring insight into the use of locally decodable codes in Broadcasting.

## Hardware implementation of adaptive modulation for OFDM and SOQPSK with preliminary results

- **ID**: ieee:7465452
- **Type**: conference
- **Published**: 2016
- **Authors**: E. D. Wang, B. Beck, T. Brothers
- **PDF**: https://ieeexplore.ieee.org/document/7465452
- **Abstract**: This paper presents a hardware implementation of a transceiver that employs both OFDM and SOQPSK-TG burst-mode signals, and it also presents an adaptive modulation and coding algorithm that uses both waveforms for the AWGN channel. The implementation complies very closely with the iNET physical layer, in which both modulations, along with an LDPC code, are used in a multi-scheme adaptation algorithm. The adaptive scheme is intended to explore the use of an adaptive algorithm for telemetry systems. The hardware implementations are described and experimental results are presented.

## A high coding-gain reduced-complexity serial concatenated error-control coding solution for wireless sensor networks

- **ID**: ieee:7888352
- **Type**: conference
- **Published**: 2016
- **Authors**: D. P. Nguyen, T. H. Tran, Y. Nakashima
- **PDF**: https://ieeexplore.ieee.org/document/7888352
- **Abstract**: Error-Control Coding (ECC) now plays an important role in wireless transceivers because it helps to increase link reliability and lower required transmit power. One popular problem of ECC implementation is the trade-off between high coding-gain and decoder's complexity. In this paper, we propose a serial concatenated ECC solution which is a combination of truncated-iteration layered-decoding LDPC block code with low-constraint Viterbi decoder at low code rate. Simulation results show that very high coding-gain and reduced-complexity are achieved. This paper also gives a supposition about applying low code rate ECC for less-active wireless nodes in Wireless Sensor Networks (WSN) to reduce transmit power and expand sensor network topology.

## Optimal coefficients for channel-coded linear physical layer network coding

- **ID**: ieee:7565028
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Tahernia, S. C. Liew
- **PDF**: https://ieeexplore.ieee.org/document/7565028
- **Abstract**: This paper investigates the linear network coding map in a Physical-layer Network Coding (PNC) operated two-way relay network. To realize the full potential of Physical-layer Network Coding in high SNR regimes, we need to use high-order signaling beyond BPSK/QPSK. In a PNC system with high-order signaling, we can have many different choices for the network coding (NC) map. For linear network coding, the network-coding map is realized by coefficients corresponding to the weights of the linearly-combined network-coded message. Prior work on channel-coded linear PNC adopted the same network-coding coefficients as in non-channel-coded linear PNC. We find that the optimal coefficients for such uncoded systems are far from optimal for coded systems. We also show that the coefficients that maximize the computation rate in the “compute-and-forward” framework, which adopts nested lattice codes, are near optimal for linear PNC that adopts the LDPC codes.

## Polar coded media-based modulation

- **ID**: ieee:7752485
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Chen, M. Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7752485
- **Abstract**: Media-based Modulation (MBM), introduced by Khandani, is based on bearing part of information in the variations of transmission media. However, MBM combined with forward error correction (FEC) codes is limited to hard decision decoding in the literature, which causes a performance loss. In this paper, a novel scheme is proposed, called polar coded MBM (PCMBM), to provide a higher coding gain and better overall system performance. The proposed PCMBM scheme maps the channel index in the frozen polar set and the other information in the free polar set. The advantage is that the bits that identify the channel do not need to be detected. Based on soft decision metric, this scheme makes full use of the received information by computing the exact likelihood ratio (LR). Furthermore, we analyze the channel capacity of PCMBM which is essential for polar coding and give a low-complexity approach based on sphere decoding to calculate bit LR. Simulation results show that this scheme is approximately 0.7 dB better than MBM with LDPC codes at BER 1e-6 under given conditions.

## Spatially-coupled codes approach symmetric information rate of finite-state Markov fading channels

- **ID**: ieee:7541793
- **Type**: conference
- **Published**: 2016
- **Authors**: H. Abe, K. Kasai
- **PDF**: https://ieeexplore.ieee.org/document/7541793
- **Abstract**: Fukushima et al. proved that spatially-coupled codes, without pilot symbols and any optimization for the channels, universally achieve the symmetric information rate (SIR) of generalized erasure channels with memory. We expect that the universality is also valid for fading channels. The receiver performs joint iterative channel estimation and decoding where factor-graphs-based BCJR channel estimator for finite-state Markov channels and the LDPC decoder are considered. We demonstrate that the reliable transmission is possible at a rate close to the SIR.

## How to select an optimum set of modes for a link adaptive transmission

- **ID**: ieee:7881821
- **Type**: conference
- **Published**: 2016
- **Authors**: M. Taki, R. Mahin Zaeem
- **PDF**: https://ieeexplore.ieee.org/document/7881821
- **Abstract**: Complexity issues and limited feedback rate strictly constraint the number of transmission modes in discrete link adaptation. A new algorithm is designed for selecting an optimum set of modes out of all the possible transmission modes based on the link's characteristics and the constraints. The design goal is to maximize the average spectral efficiency and the selection is done using a combination of nonlinear quantization and integer programming. As numerical evaluations for adaptive LDPC or convolutional coded, QAM modulated transmission show, performance of the proposed scheme is considerably improved in comparison with the benchmark schemes.

## Advanced iterative channel coding schemes: When Shannon meets Moore

- **ID**: ieee:7593146
- **Type**: conference
- **Published**: 2016
- **Authors**: S. Scholl, S. Weithoffer, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/7593146
- **Abstract**: The continuous demands on increased spectral efficiency, higher throughput, lower latency and lower energy in communication systems imposes large challenges on appropriate channel coding schemes and their efficient hardware implementation. Consequently, channel coding is not only a matter of information theory but also more and more knowledge on efficient parallel hardware architectures and underlying semiconductor technology is required. Finally, a deep understanding of the strong interrelation of code structure, decoding algorithms, communications performance and efficient implementation in state-of-the-art semiconductor technology is mandatory. In this paper, we will highlight this strong interrelation on some advanced iterative channel coding techniques, i.e. turbo codes and LDPC codes and demonstrate challenges and limitations with respect to throughput and latency.

## CDMA communication system performance for a constellation of CubeSats around the Moon

- **ID**: ieee:7500710
- **Type**: conference
- **Published**: 2016
- **Authors**: A. Babuscia, D. Divsalar, K. -M. Cheung +1
- **PDF**: https://ieeexplore.ieee.org/document/7500710
- **Abstract**: In this paper a communication system for CubeSats in formation that operate in the vicinity of the Moon is proposed. A CDMA system for the fleet of CubeSats in the vicinity of the moon to communicate with the Earth station is considered. This is an extension of our previous proposed CDMA system for a concept Constellation of CubeSats. In this paper the Doppler effects on CDMA communication system performance for a constellation of CubeSats around the Moon will be investigated. As an example we have estimated the maximum Doppler and Doppler rate profile of a SOLARA/SARA CubeSat scenario. We investigate the Effects of Doppler Shift/Rate on the CDMA system performance as a result of the CubeSat constellation orbiting in a halo orbit around Earth-Moon Lagrange Point L1. A detailed analysis and simulation of system in presence of Doppler frequency and unknown carrier phase will be performed. First we define the CDMA system for uplink and downlink between the vicinity of the Moon and Earth station. Link budgets will be provided both for uplink and downlink. Bandwidth limitations imposed by the spectral standards will be investigated for modulation formats. All system simulations are done using Simulink Matlab platform. For highly efficient nonlinear power amplifiers, we prefer to use a filtered offset QPSK with phase modulation, which is a CCSDS standard for constant envelope signaling. This allows us to use a nonlinear amplifier at CubeSat to operate at saturation point for the highest efficiency. Filtered offset QPSK with phase modulation is much more bandwidth efficient scheme. We demonstrate that this modulation format satisfies the two international spectral standards. For estimated and specified Doppler frequencies and Doppler rates we design frequency-tracking loops to track the Doppler frequency and Doppler rate in the presence of data with filtered offset QPSK with phase modulation. For carrier phase offsets a well-designed tracking loop is derived with specified loop bandwidth for the same modulation format. We use the CCSDS standard LDPC codes for space applications to meet the link budget margins.

## Non-linear distortion noise cancellation for satellite forward links

- **ID**: ieee:7601465
- **Type**: conference
- **Published**: 2016
- **Authors**: S. Dimitrov
- **PDF**: https://ieeexplore.ieee.org/document/7601465
- **Abstract**: In this paper, an iterative receiver that performs non-linear distortion noise cancellation is proposed for application at the user terminal in the DVB-S2X satellite forward link. The performance is assessed for a single-carrier time-division multiplexing (TDM) waveform with low carrier roll-off factors, e.g., down to 5%, and high baud rates, e.g., up to 34 MBaud in a 36-MHz transponder, in accordance with a very-small-aperture terminal (VSAT) scenario. The satellite forward-link channel is comprehensively modelled, including the input multiplexing (IMUX) and output multiplexing (OMUX) filter responses at the satellite transponder, the non-linear travelling wave tube amplifier (TWTA) characteristics, and the phase noise at the user terminal. Modulation orders up to 256-level amplitude and phase-shift keying (APSK) are evaluated with low-density paritycheck (LDPC) forward error correction (FEC). The improved receiver is compared to state-of-the-art compensation techniques, such as pre-distortion at transmitter and linear equalization at receiver. In the higher-baud-rate scenario, the improved receiver demonstrates a 5:2-dB increase of the energy efficiency at 32- APSK or up to 40% increase of the spectral efficiency. In the lower-baud-rate scenario, up to 1:8-dB increase of the energy efficiency at 256-APSK is presented.

## Variable-Rate Anytime Transmission with Feedback

- **ID**: ieee:7881963
- **Type**: conference
- **Published**: 2016
- **Authors**: L. Grosjean, R. Thobaben, L. K. Rasmussen +1
- **PDF**: https://ieeexplore.ieee.org/document/7881963
- **Abstract**: A generalization of the ensemble of non-terminated systematic LDPC convolutional codes developed in our previous work is proposed that allows us to design codes with lower rates than the original structure. We show that over the BEC, the modified codes have improved asymptotic and finite-length behavior and we determine the operational anytime exponent. Having shown the advantages of lowering the rate of the code, we propose a feedback protocol that permits encoder and decoder to operate at a variable rate. The rate is set on-the-fly and depends on the decoding success of the decoder. We describe the construction of the variable rate code structure and demonstrate by simulations the superiority of the variable rate scheme as compared to a scheme using a fixed rate.

## Design challenges of carrier phase tracking for higher modulation orders in high data rate applications

- **ID**: ieee:7795508
- **Type**: conference
- **Published**: 2016
- **Authors**: T. D. Kurp
- **PDF**: https://ieeexplore.ieee.org/document/7795508
- **Abstract**: The use of higher order amplitude and phase shift keying (APSK) modulations allows for increased capacity and spectral efficiency, at the expense of greater transmit power requirements or reduced range. Their adoption in over-the-air communication standards has been paired with highly efficient forward error correction (FEC) techniques such as low density parity check (LDPC) coding which greatly reduces the required operating signal-to-noise ratio (SNR). Maintaining phase coherence for these higher order modulations across a wide range of data rates, at lower SNRs due to the use of FEC coding, presents unique receiver design challenges. Waveform specifications provide little intuition as to how to overcome these. This paper discusses and addresses these design challenges. Specifically, challenges relating to Field Programmable Gate Array (FPGA) implementation of traditional acquisition and tracking schemes across a wide range of symbol rates which approach or exceed the system clock rate.

## Semi-orthogonal MARC with half duplex relaying: A backward compatible cooperative network with interference channels

- **ID**: ieee:7536879
- **Type**: conference
- **Published**: 2016
- **Authors**: M. El Soussi, T. X. Vu, H. N. Nguyen +3
- **PDF**: https://ieeexplore.ieee.org/document/7536879
- **Abstract**: This paper proposes a full-rate cooperative scheme adapted to the slow fading semi-orthogonal multiple access relay channel (MARC). It is assumed that the sources transmit on orthogonal channels and the relay is half duplex transmitting on the same channels as the one of the sources. The sources employ LDPC to encode their messages before transmitting them, while the relay uses a simple demodulate-and-forward strategy to transmit the combination of the received codewords. The presence of the relay does not affect the time-scheduling of the sources. Therefore, this scheme is backward compatible to existing non-cooperative systems. In order to cancel the interference at the destination, we propose a joint network-channel decoder that uses maximum a posteriori (MAP) detection and channel decoding. Through numerical results, we show the benefits of joint network-channel decoder. We also show that the proposed scheme significantly outperforms, in terms of BER, the non-cooperative system as well as the classical relay-assisted orthogonal channel network and that it achieves the maximum code diversity.

## [Front cover]

- **ID**: ieee:7530103
- **Type**: conference
- **Published**: 2016
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7530103
- **Abstract**: The following topics are dealt with: deregulated power system; power distribution system; power factor correction; islanding detection techniques; distributed power generation; microgrid; HVDC transmission lines; photovoltaic power system; buck converter; BLDC motor; MOSFET; adder circuit; logic circuits; carry look-ahead adder; MIMO systems; microstrip patch antenna; LTE; speech enhancement; cognitive radio network; LDPC codes; cloud computing; elliptic curve digital signature; mobile ad hoc networks; and wireless sensor networks.

## Table of contents

- **ID**: ieee:7779344
- **Type**: conference
- **Published**: 2016
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7779344
- **Abstract**: The following topics are dealt with: approximate random number generation; TH-SS signals iterative signals; distributed control method; decoding schemes for punctured Reed-Solomon codes; grayscale images filtering; power grid balancing; iterative LDPC-based joint decoding scheme; time domain equalizer; AWGN channel; FSK decoding; McEliece cryptosystem; nonlinear control systems; lossless image compression; cellular network traffic; spatial processing redundancy; linear codes; renewable power sources; performance evaluation of supercomputers; Shannon ciphers; nonlinear models of digital filters; queuing systems; network coding; rate-distortion adaptive order of bitplanes decoding; distributed video coding; weighted digital watermarking; NAND-flash memory; and next generation wireless networks.

## [Copyright notice]

- **ID**: ieee:7754576
- **Type**: conference
- **Published**: 2016
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7754576
- **Abstract**: The following topics are dealt with: CDMA; delay tolerant networks; dipole antenna; routing protocols; InSAR; WDM-DWDM-PON; 4G heterogeneous cellular networks; wireless mesh network; quad-band bandstop filter; digital image watermarking; Doherty power amplifier; LDPC decoder; wireless multimedia sensor networks; content based video retrieval; color image encryption; UWB radar; cognitive radio; VLSI CMOS circuits design; OFDMA; Rician fading channel; RFID; MIMO channel equalizer; X-ray image classification; and OFDM system.

## [Copyright notice]

- **ID**: ieee:7476295
- **Type**: conference
- **Published**: 2016
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/7476295
- **Abstract**: The following topics are dealt with: Transmission Line; Broadband PLC Systems; Power Line Communication System; MIMO Relay PLC Systems; Channel Estimation; Resource Allocation; Intraflow Network Coding; and LDPC Coded Modulations.

## The Models of Granular System and Algebraic Quotient Space in Granular Computing

- **ID**: ieee:10851925
- **Type**: journal
- **Published**: 2016
- **Authors**: L. Chen, J. Wang, L. Li
- **PDF**: https://ieeexplore.ieee.org/document/10851925
- **Abstract**: Granular computing (GrC) is an emerging computing paradigm, and it is an umbrella term exploring multilevel granularity. we present a generic abstract mathematical model of the granular system. Supposing the inter-granule structure as an algebra, we propose the algebraic quotient space model. In this model, the granulation is based on a congruence relation and all the congruence relations on a granular system form a complete semi-order lattice, which is the theoretical basis for transformation, composition and decomposition among different granularities. The different granulation rules between the topological quotient space model and the algebraic quotient space model lead to the dissimilarity while composing granularities. A real-world case study is presented that demonstrates how the algebraic quotient space model works in the network transmission by error-correcting code. These work shows that the granular system model and the algebraic quotient space model are powerful conceptual modeling and functional specification methodologies for GrC.

## Cross-Layer Chase Combining With Selective Retransmission, Analysis, and Throughput Optimization for OFDM Systems

- **ID**: ieee:7447779
- **Type**: journal
- **Published**: 2016
- **Authors**: T. Shafique, M. Zia, H. -D. Han +1
- **PDF**: https://ieeexplore.ieee.org/document/7447779
- **Abstract**: In this paper, we present a bandwidth efficient retransmission method employing selective retransmission approach at a modulation layer under orthogonal frequency division multiplexing (OFDM) signaling. The proposed cross-layer design embeds a selective retransmission sub-layer in physical layer (PHY) that targets the retransmission of information symbols transmitted over poor quality OFDM sub-carriers. Most of the times, a few errors in decoded bit stream result in packet failure at medium access control (MAC) layer. The unnecessary retransmission of good quality information symbols of a failed packet has detrimental effect on the overall throughput of transceiver. We propose a cross-layer Chase combining with selective retransmission (CCSR) method by blending Chase combining approach at MAC layer and selective retransmission in PHY. The selective retransmission in PHY targets the poor quality information symbols prior to decoding, which results in lower hybrid automatic repeat reQuest retransmissions at MAC layer. We also present bit-error rate upper bound and throughput lower bound for the CCSR method. In order to maximize the throughput, we formulate optimization problem with respect to the amount of information to be retransmitted in selective retransmission. We also present an impact of selective retransmission on latency. The proposed CCSR method achieves a significant throughput gain as compared with the conventional Chase combining method.

## Toward Plug-and-Play Software-Defined Elastic Optical Networks

- **ID**: ieee:7365418
- **Type**: journal
- **Published**: 2016
- **Authors**: F. Cugini, F. Paolucci, F. Fresi +5
- **PDF**: https://ieeexplore.ieee.org/document/7365418
- **Abstract**: Advances in transmission technologies and control plane solutions are driving the introduction of spectrally-efficient ultrahigh rate superchannel transmissions. Modulation format, forward error correction/coding, and carrier spacing represent the key transmission parameters to configure in order to obtain efficient network resource utilization according to the specific optical path requirements. So far, several studies have mainly addressed the efficient configuration of a single selected transmission parameter. Instead, the topic of the combined configuration of the whole set of parameters still requires significant investigations, particularly in the case of automatic configuration procedures. In this study, we first review the aforementioned transmission parameters in terms of their adaptation capabilities. Then, a novel procedure for effective configuration of the whole set of transmission parameters is presented. The procedure, besides modulation format and coding configuration, includes a novel self-adaptation technique for the carrier spacing in a superchannel transmission. Moreover, the technique relies on a novel software-defined networking control to reoptimize the superchannel frequency slot width. The technique has been successfully validated in a field trial where a 1 Tb/s superchannel of eight subcarriers has been automatically adapted from a frequency slot width of 200 GHz to a more efficient slot width of 175 GHz, without traffic disruption.

## Towards Practical Distributed Video Coding for Energy-Constrained Networks

- **ID**: ieee:10855855
- **Type**: journal
- **Published**: 2016
- **Authors**: Y. Cao, S. Gao, C. Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10855855
- **Abstract**: Most of current distributed video codecs are developed based on the structure of Stanford scheme that employs channel coding like LDPC and Turbo codes. However, they need many times of iteration and feedback, which bring high decoding complexity and latency that make them less practical in energy-constrained networks. In this paper, a new distributed video codec based on modulo operation in the pixel domain is proposed, which only needs one feedback request and has a much lower decoding complexity. Mathematical proof of the equivalence between modulo operation and coset partition in the M-ary field is given, which means that the modulo operation in the M-ary field is a good substitute for channel codes in the distributed video coding systems. A system is built based on the proposed scheme. Simulation results show that the proposed scheme outperforms the state-of-the-art distributed video codecs with the decoding complexity as low as 1% to 10% of them.

## Guest Editorial Recent Advances in Capacity Approaching Codes

- **ID**: ieee:7384575
- **Type**: journal
- **Published**: 2016
- **Authors**: E. Arıkan, D. J. Costello, J. Kliewer +4
- **PDF**: https://ieeexplore.ieee.org/document/7384575
- **Abstract**: The papers in this special issue address the topic of capacity approaching codes. This issue reflects a further shift of interest in coding theory research, this time toward polar codes, a new class of capacity achieving codes introduced in 2008. Of the 17 papers appearing in this issue, 9 are devoted to various aspects of polar codes, with 6 papers devoted to LDPC codes, including 3 on spatially coupled (convolutional) LDPC codes, and 2 on other coding topics.

## Density evolution analysis of spatially coupled LDPC codes over BIAWGN channel

- **ID**: ieee:7433602
- **Type**: conference
- **Published**: 20-22 Jan.
- **Authors**: Md. Noor-A-Rahim, Gottfried Lechner, Khoa D. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/7433602
- **Abstract**: In this paper, we study the density evolution analysis of spatially coupled low-density parity-check (SC-LDPC) codes over binary input additive white Gaussian noise (BIAWGN) channels under the belief propagation (BP) decoding algorithm. Using reciprocal channel approximation and Gaussian approximation, we propose averaging techniques for the density evolution of SC-LDPC codes over BIAWGN channels. We show that the proposed techniques can closely predict the decoding threshold while offering reduced complexity compared to the existing multi-edge-type density evolution.

## Coding architecture for optical eU-OFDM transmission over AWGN

- **ID**: ieee:7433670
- **Type**: conference
- **Published**: 20-22 Jan.
- **Authors**: Ronald Mulinde, Khoa D. Nguyen, William G. Cowley +1
- **PDF**: https://ieeexplore.ieee.org/document/7433670
- **Abstract**: To improve the power-spectral efficiency trade-off of intensity-modulated direct-detection (IM/DD) optical transmissions, enhanced unipolar orthogonal frequency-division multiplexing (eU-OFDM) was recently introduced. Uncoded eU-OFDM systems have been presented in literature but coding techniques to further improve the reliability of transmissions over such systems have not yet been explored. Applying off-the-shelf codes to these systems does not lead to the best performance. In this paper, we propose a novel structured encoding-decoding architecture that is suitable for successive interference cancellation (SIC) required in eU-OFDM. Simulation results obtained so far show that the proposed code structure outperforms the off-the-shelf coded systems.

## Using channel state information for low-latency applications in free-space optical communication

- **ID**: ieee:7433601
- **Type**: conference
- **Published**: 20-22 Jan.
- **Authors**: G. S. H. De Silva, William G. Cowley, Gottfried Lechner
- **PDF**: https://ieeexplore.ieee.org/document/7433601
- **Abstract**: Channel coding techniques are widely applied to improve the reliability of high-speed terrestrial free-space optical (FSO) communication links, which are subjected to the atmospheric turbulence-induced signal fading. Since the channel variation is slow, the system performance can be further improved by using the instantaneous channel state information (CSI) at the receiver. The performance of a coding scheme applied in such systems mainly depends on the latency and data rate requirements. In this work, we analyse the code performance bounds of latency-constrained FSO links employing intensity modulation/direct detection (IM/DD) techniques. Assuming perfect receiver-side channel state information (CSI), we propose two approaches to evaluate the lower bound of the word error probability of a coding scheme for a given latency and information rate. While the first method uses Monte Carlo simulations, the second method uses an approximation to derive these bounds. Finally, using LDPC codes, we show that even under these low-latency constrains, a code can approach the performance bound, if CSI can be used at the decoding.

## Repeat-accumulate codes for reconciliation in continuous variable quantum key distribution

- **ID**: ieee:7433603
- **Type**: conference
- **Published**: 20-22 Jan.
- **Authors**: Sarah J. Johnson, Vikram A. Chandrasetty, Andrew M. Lance
- **PDF**: https://ieeexplore.ieee.org/document/7433603
- **Abstract**: This paper investigates the design of low-complexity error correction codes for the verification step in continuous variable quantum key distribution (CVQKD) systems. We design new coding schemes based on quasi-cyclic repeat-accumulate codes which demonstrate good performances for CVQKD reconciliation. Given quasi-cyclic repeat-accumulate codes' commercial maturity, low implementation complexity and existing high-speed ASIC implementations, this makes these codes viable candidates for commercial CVQKD systems.

## Constellation shaping for non-uniform signals in bit-interleaved coded modulation combined with multi-stage decoding

- **ID**: ieee:7433671
- **Type**: conference
- **Published**: 20-22 Jan.
- **Authors**: Gou Hosoya, Hiroyuki Yashima
- **PDF**: https://ieeexplore.ieee.org/document/7433671
- **Abstract**: A signal shaping for the bit-interleaved coded modulation (BICM) is considered. Previous work on signal shaped BICM (SBICM) has two problems: (i) It requires an optimization for the linear factors of superposition modulation. The optimization is valid around target SNR. (ii) The binary labeling of signal constellation is not Gray code. To overcome these problems, non-uniform signal labeling for the input signal with Gaussian distribution is considered. We implement the reduction of peak-to-average power ratio (PAPR) by clipping for the largest signal points. From the numerical results, we show that achievable rate of the proposed modulation is larger than that of the previous modulation of SBICM for wide range of SNR, while keeping the expansion of PAPR small. Moreover it is quite close to the coded modulation capacity for wide range of SNR, especially in some SNR region, it is larger than the coded modulation capacity.

## Low-Power 400-Gbps Soft-Decision LDPC FEC for Optical Transport Networks

- **ID**: ieee:7542134
- **Type**: journal
- **Published**: 15 Sept.15
- **Authors**: Kevin Cushon, Per Larsson-Edefors, Peter Andrekson
- **PDF**: https://ieeexplore.ieee.org/document/7542134
- **Abstract**: We present forward error correction systems based on soft-decision low-density parity check (LDPC) codes for applications in 100-400-Gbps optical transport networks. These systems are based on the low-complexity “adaptive degeneration” decoding algorithm, which we introduce in this paper, along with randomly-structured LDPC codes with block lengths from 30 000 to 60 000 bits and overhead (OH) from 6.7% to 33%. We also construct a 3600-bit prototype LDPC code with 20% overhead, and experimentally show that it has no error floor above a bit error rate (BER) of 10-15 using a field-programmable gate array (FPGA)-based hardware emulator. The projected net coding gain at a BER of 10-15 ranges from 9.6 dB at 6.7% OH to 11.2 dB at 33% OH. We also present application-specific integrated circuit synthesis results for these decoders in 28 nm fully depleted silicon on insulator technology, which show that they are capable of 400-Gbps operation with energy consumption of under 3 pJ per information bit.

## A Low-Complexity Delay-Tunable Coding Scheme for Visible Light Communication Systems

- **ID**: ieee:7491294
- **Type**: journal
- **Published**: 15 Sept.15
- **Authors**: Shancheng Zhao, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7491294
- **Abstract**: Visible light communication (VLC) systems are expected to support a variety of applications, such as common-information broadcasting, real-time multimedia streaming, and large file downloading. Typically, these applications have different delay requirements. Hence, it is desirable to design high-performance coding scheme capable of supporting a wide range of delays but with acceptable hardware complexity. To achieve this, we propose a delay-tunable coding scheme for VLC systems based on block Markov superposition transmission of short non-binary low-density parity-check (NBLDPC) codes. The proposed coding scheme includes the following advantages: 1) it is easily configurable to fulfill different delay requirements while keeping the code rate constant; 2) it requires essentially the same hardware modules to implement the encoder/decoder as the involved short NBLDPC code; and 3) it can have a larger coding gain if a longer delay is tolerated. Numerical results are presented to show the expected tradeoff between delay and energy in a VLC system.

## Probabilistic 16-QAM Shaping in WDM Systems

- **ID**: ieee:7523228
- **Type**: journal
- **Published**: 15 Sept.15
- **Authors**: Chunpo Pan, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/7523228
- **Abstract**: This work proposes a probabilistic shaping scheme for optical WDM systems, where nonlinear interference noise depends on the input optical signal power distribution. With 16-QAM, a white Gaussian channel analysis shows that the shaped constellation is able to achieve a reach improvement of up to 7%, while split-step Fourier method simulations suggest that even higher gains are possible in practice. An example system is developed for a transmission distance around 3280 km. A constellation mapping and a low-density parity-check code are developed for this regime to show a reach improvement of 7.1%. These shaping schemes can also be extended to 64-QAM, where a reach improvement of over 10% is expected.

## Unrepeatered Transmission of  $10\times 400\text{G}$  Over 370 km via Amplification Map Optimization

- **ID**: ieee:7514963
- **Type**: journal
- **Published**: 15 Oct.15,
- **Authors**: João Carlos Soriano Sampaio Januário, Sandro Marcelo Rossi, Stenio Magalhães Ranzini +6
- **PDF**: https://ieeexplore.ieee.org/document/7514963
- **Abstract**: We demonstrate unrepeatered transmission of 10 × 400-Gb/s PM-16QAM Nyquist wavelength-division multiplexing (WDM) dual-carrier superchannels (75-GHz flexigrid) at the SE = 5.33 b/s/Hz, where each superchannel is coherently detected by a single wideband receiver. A 350-km transmission is achieved by using optimized amplification map to efficiently design remote optically pumped amplifier and hybrid amplifiers. Additional digital domain nonlinear compensation allows to increase the transmission distance up to 370 km.

## 3.5-Gbit/s QPSK Signal Radio-Over-Fiber Transmission With 60-GHz Integrated Photonic Array-Antenna Beam Forming

- **ID**: ieee:7448364
- **Type**: journal
- **Published**: 15 Oct.15,
- **Authors**: Masayuki Oishi, Takayoshi Hirasawa, Kotoko Furuya +3
- **PDF**: https://ieeexplore.ieee.org/document/7448364
- **Abstract**: This paper studies the performance of 3.5-Gbit/s quadrature phase shift keying (QPSK) signal radio-over-fiber (RoF) transmission with beam forming of array antennas. An “integrated photonic array-antenna (IPA)” is utilized in this experiment, where uni-travelling carrier photodiodes are fully integrated with 60-GHz-band 4 × 2 array-antenna elements into a single board. The beam forming operation for the IPA is experimentally demonstrated by using a QPSK signal assuming real mobile data traffic, and the QPSK signal quality during the beam forming operation for the IPA is quantitatively evaluated. The expandability for more advanced modulation formats, such as 16-quadratic-amplitude modulation, is also studied. In addition, the required system parameters for practical use are shown by investigating the induced transmission penalty. The obtained results enable us to design next generation radio access networks based on 60-GHz RoF transmission technique.

## Constellation Shaping for WDM Systems Using 256QAM/1024QAM With Probabilistic Optimization

- **ID**: ieee:7563861
- **Type**: journal
- **Published**: 15 Nov.15,
- **Authors**: Metodi P. Yankov, Francesco Da Ros, Edson P. da Silva +5
- **PDF**: https://ieeexplore.ieee.org/document/7563861
- **Abstract**: In this paper, probabilistic shaping is numerically and experimentally investigated for increasing the transmission reach of wavelength division multiplexed (WDM) optical communication systems employing quadrature amplitude modulation (QAM). An optimized probability mass function (PMF) of the QAM symbols is first found from a modified Blahut–Arimoto algorithm for the optical channel. A turbo coded bit interleaved coded modulation system is then applied, which relies on many-to-one labeling to achieve the desired PMF, thereby achieving shaping gains. Pilot symbols at rate at most 2% are used for synchronization and equalization, making it possible to receive input constellations as large as 1024QAM. The system is evaluated experimentally on a 10 GBd, 5 channels WDM setup. The maximum system reach is increased w.r.t. standard 1024QAM by 20% at input data rate of 4.65 bits/symbol and up to 75% at 5.46 bits/symbol. It is shown that rate adaptation does not require changing of the modulation format. The performance of the proposed 1024QAM shaped system is validated on all 5 channels of the WDM signal for selected distances and rates. Finally, it is shown via EXIT charts and BER analysis that iterative demapping, while generally beneficial to the system, is not a requirement for achieving the shaping gain.

## Design of a 1 Tb/s Superchannel Coherent Receiver

- **ID**: ieee:7384692
- **Type**: journal
- **Published**: 15 March15
- **Authors**: David S. Millar, Robert Maher, Domaniç Lavery +9
- **PDF**: https://ieeexplore.ieee.org/document/7384692
- **Abstract**: We describe the design of a trained and pilot-aided digital coherent receiver, capable of detecting a 1 Tb/s superchannel with a single optical front-end. Algorithms for receiver training are described, which calculate the equalizer coefficients, subchannel SNRs, and centroids of the transmitted constellations. Algorithms for pilot-aided operation are then described in detail, providing pilot-aided constant modulus equalization and joint carrier-phase estimation over several coherent subchannels. We demonstrate the detection of a superchannel with net bit rate in excess of 1 Tb/s with a single coherent receiver. An $11\times 10$  GBd DP-64QAM Nyquist superchannel is used, with 1.32 Tb/s gross bit rate.

## Signal Overlap for Elastic Optical Networks

- **ID**: ieee:7469317
- **Type**: journal
- **Published**: 15 July15,
- **Authors**: Tommaso Foggi, Filippo Cugini
- **PDF**: https://ieeexplore.ieee.org/document/7469317
- **Abstract**: In Elastic Optical Networks, advanced transmission techniques based on coherent detection strategies have been proposed and exploited to provide high flexibility in resource allocation. So far, these techniques have assumed the constraint of each optical signal being transmitted along a dedicated frequency slot, by carefully avoiding frequency overlap with other optical signals. In this study, an overlap technique, that enables uncorrelated optical signals to be superimposed along the same spectrum resources, is designed and validated through simulations, both in terms of performance bounds and bit-error rate in coded transmissions. In particular, it is demonstrated how this technique allows each overlapped signal to be correctly received and detected. The proposed technique is less spectrally efficient and more complex to implement than increasing the constellation size and using non overlapping frequency slots, but it warrants consideration for flexible networking. The proposed technique is first theoretically detailed and justified. Then, networking scenarios and implementation schemes suitable for its effective utilization are identified and applied in the case of two overlapped 112 Gb/s polarization-multiplexed quadrature phase shift keying signals. Simulation results show that, applying 3-dB optical signal-to-noise ratio margin on the achieved bounds, optical reaches of around 800 km can be successfully supported by the proposed overlap technique.

## Iteration-Aware LDPC Code Design for Low-Power Optical Communications

- **ID**: ieee:7254117
- **Type**: journal
- **Published**: 15 Jan.15,
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Keisuke Kojima +4
- **PDF**: https://ieeexplore.ieee.org/document/7254117
- **Abstract**: Recent low-density parity-check (LDPC) codes have shown capacity-approaching performance for various communications systems. However, their promising performance cannot always be obtained due to practical constraints, such as finite codeword length, finite iteration, finite memory, and finite precision. In this paper, we focus on a practical design method of high-performance LDPC codes under a constraint of finite-iteration decoding for low-power optical communications. We introduce an iteration-aware LDPC code design approach, which is based on decoding trajectory in extrinsic information transfer chart analysis. It is demonstrated that an LDPC code designed by the conventional curve-fitting method exhibits nearly 2 dB of penalty, when the maximum number of iterations is limited. The results suggest that the LDPC code should be adaptively changed, e.g., when the number of decoding iterations is decreased to save power consumption. We also extend our design method to a multi-objective optimization concept by taking average degrees into account, so that the threshold and the computational complexity are minimized at the same time. The proposed Pareto-optimal codes can achieve additional 2-dB gain or 50% complexity reduction at maximum, in low-power decoding scenarios.

## Replacing the Soft-Decision FEC Limit Paradigm in the Design of Optical Communication Systems

- **ID**: ieee:7406824
- **Type**: journal
- **Published**: 15 Jan.15,
- **Authors**: Alex Alvarado, Erik Agrell, Domaniç Lavery +2
- **PDF**: https://ieeexplore.ieee.org/document/7406824
- **Abstract**: The FEC limit paradigm is the prevalent practice for designing optical communication systems to attain a certain bit error rate (BER) without forward error correction (FEC). This practice assumes that there is an FEC code that will reduce the BER after decoding to the desired level. In this paper, we challenge this practice and show that the concept of a channel-independent FEC limit is invalid for soft-decision bit-wise decoding. It is shown that for low code rates and high-order modulation formats, the use of the soft-decision FEC limit paradigm can underestimate the spectral efficiencies by up to 20%. A better predictor for the BER after decoding is the generalized mutual information, which is shown to give consistent post-FEC BER predictions across different channel conditions and modulation formats. Extensive optical full-field simulations and experiments are carried out in both the linear and nonlinear transmission regimes to confirm the theoretical analysis.

## An Experimental Comparison of Coded Modulation Strategies for 100 Gb/s Transceivers

- **ID**: ieee:7742908
- **Type**: journal
- **Published**: 15 Dec.15,
- **Authors**: Eric Sillekens, Alex Alvarado, Chigo M. Okonkwo +1
- **PDF**: https://ieeexplore.ieee.org/document/7742908
- **Abstract**: Coded modulation is a key technique to increase the spectral efficiency of coherent optical communication systems. Two popular strategies for coded modulation are turbo trellis-coded modulation (TTCM) and bit-interleaved coded modulation (BICM) based on low-density parity-check (LDPC) codes. Although BICM LDPC is suboptimal, its simplicity makes it very popular in practice. In this work, we compare the performance of TTCM and BICM LDPC using information-theoretic measures. Our information-theoretic results show that for the same overhead and modulation format only a very small penalty (less than 0.1 dB) is to be expected when an ideal BICM LDPC scheme is used. However, the results obtained for the coded modulation schemes implemented in this paper show that the TTCM outperforms BICM LDPC by a larger margin. For a 1000 km transmission at 100 Gb/s, the observed gain was 0.4 dB.

## Submarine Transmission Systems Using Digital Nonlinear Compensation and Adaptive Rate Forward Error Correction

- **ID**: ieee:7389319
- **Type**: journal
- **Published**: 15 April15
- **Authors**: Amirhossein Ghazisaeidi, Ivan Fernandez de Jauregui Ruiz, Laurent Schmalen +6
- **PDF**: https://ieeexplore.ieee.org/document/7389319
- **Abstract**: We report on a full C + L-band erbium-doped fiber amplified (EDFA) submarine transmission experiment of 178 wavelength-division multiplexed channels of 49-GBd polarization multiplexed 16QAM signals, achieving 54.2 Tb/s after 6600 km, with a record per-channel average net bit rate of 304.5 Gb/s. Digital backpropagation and time-domain perturbative nonlinearity compensation were alternatively applied to all channels and their respective benefits, in terms of throughput increase, reach increase, and complexity, were addressed. Multiple-rate spatially coupled low density parity check forward error correction codes with a novel rate optimization algorithm were employed. The power consumption of the power feeding equipment of our EDFA-only amplification scheme was analyzed and compared with that of hybrid EDFA Raman amplification. We also provided numerical and theoretical performance analysis of nonlinear uncompensated/compensated systems.

## Comparison of FPGA implementation of LDPC encoder algorithms

- **ID**: ieee:7508190
- **Type**: conference
- **Published**: 14-15 Jan.
- **Authors**: Steffy Johnson, Nidhi Gaur
- **PDF**: https://ieeexplore.ieee.org/document/7508190
- **Abstract**: This paper presents the straightforward method and the lower triangular modification approach, which are the two encoding schemes for LDPC codes and compares the area utilization of both on FPGA platform. Low density parity check (LDPC) codes are linear block codes which are extensively used for error correction and detection in noisy communication channel and they discover significant application in 10GBase-T Ethernet, Wi-Fi, Wi-Max. The FPGA implementation is done on Spartan3E board and we observe that the device utilization by the straightforward method is considerably very small (only one LUT) as compared to that of lower triangular modification approach. This optimizes the size on chip as well as complexity of implementation.

## Achieving FEC and RLL for VLC: A Concatenated Convolutional-Miller Coding Mechanism

- **ID**: ieee:7397916
- **Type**: journal
- **Published**: 1 May1, 20
- **Authors**: Xuanxuan Lu, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/7397916
- **Abstract**: Run-length limited (RLL) codes are widely used in visible light communications to avoid long runs of 1s and 0s that potentially cause the flicker. This letter explores the serial concatenation of convolutional codes and Miller codes to simultaneously achieve forward error correction and RLL control. Miller codes with high bandwidth efficiency are much ignored in practice due to their disappointing power efficiency. The novelty of this letter is that we identity the merit of this previously unfavorable RLL code (i.e., trellis structure and soft decidability), exploit some important coding principles (i.e., interleaved serial concatenation and soft-iterative decoding), and assemble it to a powerful turbo structure that makes it outperform the existing favorable choices. A modified Bahl-Cocke-Jelinek-Raviv decoding algorithm is developed for the proposed concatenation. Analysis and simulations confirm that the new system is capable of solid RLL control and a superb performance better than the existing schemes.

## Impact of 4D Channel Distribution on the Achievable Rates in Coherent Optical Communication Experiments

- **ID**: ieee:7404211
- **Type**: journal
- **Published**: 1 May1, 20
- **Authors**: Tobias A. Eriksson, Tobias Fehenberger, Peter A. Andrekson +3
- **PDF**: https://ieeexplore.ieee.org/document/7404211
- **Abstract**: We experimentally investigate mutual information and generalized mutual information for coherent optical transmission systems. The impact of the assumed channel distribution on the achievable rate is investigated for distributions in up to four dimensions. Single channel and wavelength-division multiplexing (WDM) transmission over transmission links with and without inline dispersion compensation are studied. We show that for conventional WDM systems without inline dispersion compensation, a circularly symmetric complex Gaussian distribution is a good approximation of the channel. For other channels, such as with inline dispersion compensation, this is no longer true and gains in the achievable information rate are obtained by considering more sophisticated four-dimensional (4D) distributions. We also show that for nonlinear channels, gains in the achievable information rate can also be achieved by estimating the mean values of the received constellation in four dimensions. The highest gain for such channels is seen for a 4D correlated Gaussian distribution.

## Amplification Schemes and Multi-Channel DBP for Unrepeatered Transmission

- **ID**: ieee:7389964
- **Type**: journal
- **Published**: 1 May1, 20
- **Authors**: Lidia Galdino, Mingming Tan, Alex Alvarado +8
- **PDF**: https://ieeexplore.ieee.org/document/7389964
- **Abstract**: The performance of unrepeatered transmission of a seven Nyquist-spaced 10 GBd PDM-16QAM superchannel using full signal band coherent detection and multi-channel digital back propagation (MC-DBP) to mitigate nonlinear effects is analysed. For the first time in unrepeatered transmission, the performance of two amplification systems is investigated and directly compared in terms of achievable information rates (AIRs): 1) erbium-doped fibre amplifier (EDFA) and 2) second-order bidirectional Raman pumped amplification. The experiment is performed over different span lengths, demonstrating that, for an AIR of 6.8 bit/s/Hz, the Raman system enables an increase of 93 km (36 %) in span length. Further, at these distances, MC-DBP gives an improvement in AIR of 1 bit/s/Hz (to 7.8 bit/s/Hz) for both amplification schemes. The theoretical AIR gains for Raman and MC-DBP are shown to be preserved when considering low-density parity-check codes. Additionally, MC-DBP algorithms for both amplification schemes are compared in terms of performance and computational complexity. It is shown that to achieve the maximum MC-DBP gain, the Raman system requires approximately four times the computational complexity due to the distributed impact of fibre nonlinearity.

## Decoding Genetic Variations: Communications-Inspired Haplotype Assembly

- **ID**: ieee:7172486
- **Type**: journal
- **Published**: 1 May-June
- **Authors**: Zrinka Puljiz, Haris Vikalo
- **PDF**: https://ieeexplore.ieee.org/document/7172486
- **Abstract**: High-throughput DNA sequencing technologies allow fast and affordable sequencing of individual genomes and thus enable unprecedented studies of genetic variations. Information about variations in the genome of an individual is provided by haplotypes, ordered collections of single nucleotide polymorphisms. Knowledge of haplotypes is instrumental in finding genes associated with diseases, drug development, and evolutionary studies. Haplotype assembly from high-throughput sequencing data is challenging due to errors and limited lengths of sequencing reads. The key observation made in this paper is that the minimum error-correction formulation of the haplotype assembly problem is identical to the task of deciphering a coded message received over a noisy channel-a classical problem in the mature field of communication theory. Exploiting this connection, we develop novel haplotype assembly schemes that rely on the bit-flipping and belief propagation algorithms often used in communication systems. The latter algorithm is then adapted to the haplotype assembly of polyploids. We demonstrate on both simulated and experimental data that the proposed algorithms compare favorably with state-of-the-art haplotype assembly methods in terms of accuracy, while being scalable and computationally efficient.

## Bit-Level Soft Run-Length Limited Decoding Algorithm for Visible Light Communication

- **ID**: ieee:7302045
- **Type**: journal
- **Published**: 1 Feb.1, 2
- **Authors**: He Wang, Sunghwan Kim
- **PDF**: https://ieeexplore.ieee.org/document/7302045
- **Abstract**: In this letter, we proposed a bit-level soft (BLS) run-length limited (RLL) decoding algorithm for visible light communication (VLC). Conventional RLL encoding is only used for dimming control, and the lack of effective RLL decoding is a long-standing issue in VLC systems. Therefore, an RLL decoding method that utilizes soft information from the channel to produce BLS output is proposed for enhancing the performance of the system. The BLS RLL decoder is conjugated with a Reed-Solomon decoder that can efficiently utilize bit-level information from RLL decoding output. The simulation results show that the bit error rate performance of our proposed RLL decoding provides a significant gain over that of the conventional RLL decoding and compares favorably with that of the referenced RLL decoding methods.

## Rate Adaptation and Reach Increase by Probabilistically Shaped 64-QAM: An Experimental Demonstration

- **ID**: ieee:7360102
- **Type**: journal
- **Published**: 1 April1, 
- **Authors**: Fred Buchali, Fabian Steiner, Georg Böcherer +3
- **PDF**: https://ieeexplore.ieee.org/document/7360102
- **Abstract**: A transmission system with adjustable data rate for single-carrier coherent optical transmission is proposed, which enables high-speed transmission close to the Shannon limit. The proposed system is based on probabilistically shaped 64-QAM modulation formats. Adjustable shaping is combined with a fixed-QAM modulation and a fixed forward-error correction code to realize a system with adjustable net data rate that can operate over a large reach range. At the transmitter, an adjustable distribution matcher performs the shaping. At the receiver, an inverse distribution matcher is used. Probabilistic shaping is implemented into a coherent optical transmission system for 64-QAM at 32 Gbaud to realize adjustable operation modes for net data rates ranging from 200 to 300 Gb/s. It is experimentally demonstrated that the optical transmission of probabilistically shaped 64-QAM signals outperforms the transmission reach of regular 16-QAM and regular 64-QAM signals by more than 40% in the transmission reach.
