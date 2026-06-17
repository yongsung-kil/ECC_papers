# IEEE Xplore — 2024-06


## Low-Rate LDPC Code Design for DTMB-A

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10410655
- **Type**: journal
- **Published**: June 2024
- **Authors**: Zhitong He, Kewu Peng, Chao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10410655
- **Abstract**: Digital terrestrial television multimedia broadcasting-advanced (DTMB-A) proposed by China is served as a 2nd generation digital terrestrial television broadcasting (DTTB) standard with advanced forward error correction coding schemes. Nevertheless, to adapt low signal-to-noise ratio (SNR) scenarios such as in cloud transmission systems, LDPC codes with low rates are required for DTMB-A. In this paper, the new design of low-rate DTMB-A LDPC codes is presented systematically. Specifically, a rate-compatible Raptor-Like structure of low-rate DTMB-A LDPC codes is presented, which supports multiple low code rates with constant code length. Then a new construction method is proposed for low-rate DTMB-A LDPC codes, where progressive block extension is employed and the minimum distance is majorly optimized such that the minimum distance increases after each block extension. Finally, the performance of the constructed DTMB-A LDPC codes with two low code rates of 1/3 and 1/4 are simulated and compared with ATSC 3.0 LDPC codes, which demonstrates the effectiveness of our design.

## A Generalized Adjusted Min-Sum Decoder for 5G LDPC Codes: Algorithm and Implementation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10461640
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yuqing Ren, Hassan Harb, Yifei Shen +2
- **PDF**: https://ieeexplore.ieee.org/document/10461640
- **Abstract**: 5G New Radio (NR) has stringent demands on both performance and complexity for the design of low-density parity-check (LDPC) decoding algorithms and corresponding VLSI implementations. Furthermore, decoders must fully support the wide range of all 5G NR blocklengths and code rates, which is a significant challenge. In this paper, we present a high-performance and low-complexity LDPC decoder, tailor-made to fulfill the 5G requirements. First, to close the gap between belief propagation (BP) decoding and its approximations in hardware, we propose an extension of adjusted min-sum decoding, called generalized adjusted min-sum (GA-MS) decoding. This decoding algorithm flexibly truncates the incoming messages at the check node level and carefully approximates the non-linear functions of BP decoding to balance the error-rate and hardware complexity. Numerical results demonstrate that the proposed fixed-point GA-MS has only a minor gap of 0.1 dB compared to floating-point BP under various scenarios of 5G standard specifications. Secondly, we present a fully reconfigurable 5G NR LDPC decoder implementation based on GA-MS decoding. Given that memory occupies a substantial portion of the decoder area, we adopt multiple data compression and approximation techniques to reduce 42.2% of the memory overhead. The corresponding 28nm FD-SOI ASIC decoder has a core area of 1.823 mm2 and operates at 895 MHz. It is compatible with all 5G NR LDPC codes and achieves a peak throughput of 24.42 Gbps and a maximum area efficiency of 13.40 Gbps/mm2 at 4 decoding iterations.

## Area-Efficient QC-LDPC Decoding Architecture With Thermometer Code-Based Sorting and Relative Quasi-Cyclic Shifting

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10507156
- **Type**: journal
- **Published**: June 2024
- **Authors**: Boseon Jang, Hyejung Jang, Sungho Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/10507156
- **Abstract**: The 5G New-Radio (NR) communication standard requires high throughput and low latency, so low-density parity-check (LDPC) codes, which have higher inherent parallelism and lower decoding complexity than turbo codes, were adopted as the main coding method for data channels. In traditional LDPC min-sum decoders, the check node unit was realized using a sorting unit based on the min-tree structure. However, this structure resulted in high hardware complexity and long latency. To address this issue, we propose a new sorting method based on the thermometer code-based number system. Additionally, we introduce a new LDPC decoding architecture that reduces the number of QSN stages from two to one, significantly lowering the shifting logic complexity needed to support different lifting sizes. This is achieved by using relative shift amounts instead of absolute shift amounts specified in the parity check matrix. The proposed decoder implemented using a partially parallel structure in a 65nm CMOS technology satisfies the various operation modes and the throughput requirements of the 5G NR standard, and boasts a higher normalized throughput than state-of-the-art LDPC decoders.

## An Efficient Information Reconciliation Scheme via Partial Encoding for Physical Layer Secret Key Generation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10488080
- **Type**: journal
- **Published**: June 2024
- **Authors**: Toshiki Matsumine, Hideki Ochiai, Junji Shikata
- **PDF**: https://ieeexplore.ieee.org/document/10488080
- **Abstract**: This letter proposes an efficient information reconciliation coding scheme for physical layer secret key generation. We consider a high-rate key generation system, where multiple key bits are extracted from one Gaussian random variable source, each of which has different reliability depending on its bit level. Although the conventional bit-interleaved coded modulation (BICM)-type reconciliation protects all the key bits by forward error correction (FEC), the computational complexity associated with its encoding and decoding can be a bottleneck in achieving a high secret key rate especially for low-cost devices with limited computational capabilities. To alleviate this complexity issue, we propose a new reconciliation scheme that efficiently reduces the complexity by applying FEC only to the least reliable bits (LRBs). We demonstrate by simulations that the proposed information reconciliation based on partial encoding achieves a lower key bit mismatch rate (BMR) than the conventional BICM-type reconciliation even with lower decoding complexity. Furthermore, we provide a lower bound on the asymptotic BMR of the proposed scheme that is useful for estimating the performance in high signal-to-noise ratio (SNR) regimes.

## Adaptive Modulation and Coding With LDPC Codes and Retransmission for Ultraviolet Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10506962
- **Type**: journal
- **Published**: June 2024
- **Authors**: Fei Long, Jingyin Tang, Lingfeng Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10506962
- **Abstract**: To adapt to different transmission power and distances, we design a rate-compatible transmission protocol to realize different transmission rates for ultraviolet (UV) communication. We have designed ensembles based on low-density parity-check (LDPC) codes, incorporating various code lengths and rates working under different channel conditions. Furthermore, the direct sequence spreading technique is adopted to obtain different channel codes working in weaker channel conditions. Through simulating the frame error rate (FER) performance across various signal and background radiation intensities, we obtain a table of switching thresholds for channel coding under distinct channel conditions. Different from that for radio-frequency (RF) communication with only one parameter of signal-to-noise ratio (SNR), the switching threshold table is constructed based on the combination of two parameters for UV Communication, the signal intensity and background radiation intensity. We also propose adaptive coding with hybrid automatic retransmission requests based on the combination of signal intensity and background intensity. It is verified through simulation that our designed system shows larger throughput under varying channel conditions compared with channel coding with a fixed rate in UV Communication.

## EBDN: Entropy-Based Double Nonuniform Sensing Algorithm for LDPC Decoding in TLC nand Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10382664
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yongchao Wang, Debao Wei, Ming Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/10382664
- **Abstract**: Low-density parity-check (LDPC) codes are widely employed in NAND flash memory to improve the reliability of data. However, LDPC has serious latency problems when the raw bit error rate (RBER) is high. The reason is that not only a sufficient sensing level is required to obtain accurate soft information but also a high number of iterations are needed. To reduce the latency of LDPC, an entropy-based double nonuniform (EBDN) sensing algorithm is proposed in this article. The basic idea of this algorithm is to exploit the entropy to quantify the nonuniformity of intrastate and interstate. And the sensing levels are placed in a targeted manner based on the entropy, thereby significantly reducing the number of sensing levels without reducing the LDPC error correction performance. The experimental results show that the proposed algorithm can decrease the number of iterations of LDPC by approximately 70% and reduce the read latency by 34.52% compared with the traditional nonuniform sensing algorithm.

## Sparse Code Multiple Access With Enhanced K-Repetition Scheme: Analysis and Design

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10295166
- **Type**: journal
- **Published**: June 2024
- **Authors**: Ke Lai, Zilong Liu, Jing Lei +3
- **PDF**: https://ieeexplore.ieee.org/document/10295166
- **Abstract**: This work presents a novel K-Repetition based Hybrid Automatic Repeat reQuest (HARQ) scheme for uplink sparse code multiple access (SCMA) systems. Our core idea is to apply network coding (NC) principle to re-encode different packets (after channel coding and interleaving) or their fragments, where K-Repetition is an emerging HARQ technique (recommended in 3GPP Release 15) for enhanced reception in future massive machine-type communications. Such a proposed scheme is referred to as the NC aided K-repetition SCMA (NCK-SCMA) in this paper. We aim to understand the optimal NCK-SCMA design criteria for maximizing the channel diversity as well as the efficient receiver processing for superior error rate performances. It is found that NC can enable a larger diversity order for NCK-SCMA with fewer resources (i.e., higher spectrum efficiency). Toward this objective, some novel design criteria are developed for the efficient configuration of NCK-SCMA. Moreover, we propose an iterative network decoding and SCMA detection (INDSD) algorithm for robust and low-complexity recovery of the transmit data from a low-density parity-check (LDPC) coded uplink NCK-SCMA system. Simulation results demonstrate that the proposed NCK-SCMA lead to higher throughput and improved reliability over the conventional K-SCMA.

## Enhanced Joint Source-Channel Polarization Effect Based on Polarizing Matrix Extension

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10491360
- **Type**: journal
- **Published**: June 2024
- **Authors**: Wei Wang, Kai Niu, Jincheng Dai
- **PDF**: https://ieeexplore.ieee.org/document/10491360
- **Abstract**: In this letter, we propose a joint source-channel coding scheme based on polarizing matrix extension (PME-JSCC). The PME-JSCC can combine channel received signal and source side information to form a longer polar code. We extend the source encoding matrix and place channel bits on the extended bits. Due to the lower triangular structure of the polarizing matrix, source bits will not be changed by channel bits. The PME-JSCC can obtain enhanced joint source-channel polarization (JSCP) effect. This effect enhances the reliabilities of both channel bits and source encoded bits simultaneously. The bound on the block error probability for PME-JSCC is improved. And the PME-JSCC can be proved to reach the fundamental limit on JSCC. Simulation results show that the PME-JSCC scheme outperforms the DP-LDPC and the D-Polar codes under the joint successive cancellation list (J-SCL) decoder and can approximate the JSCC finite length bound in the short blocklength regime.

## Spatially Coupled Codes via Bidirectional Block Markov Superposition Transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10339816
- **Type**: journal
- **Published**: June 2024
- **Authors**: Gaoyan Li, Shancheng Zhao, Haiqiang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10339816
- **Abstract**: In this paper, we present a new class of spatially coupled codes obtained by using both non-recursive and recursive block-oriented superposition. The resulting codes are termed as bidirectional block Markov superposition transmission (BiBMST) codes. Firstly, we perform an iterative decoding threshold analysis according to protograph-based extrinsic information transfer (PEXIT) charts for the BiBMST codes over the binary erasure channels (BECs). Secondly, we derive the generator and parity-check matrices of the BiBMST codes. Thirdly, extensive numerical results are presented to show the advantages of the proposed BiBMST codes. Particularly, our numerical results show that, under the constraint of an equal decoding latency, the BiBMST codes perform better than the recursive BMST (rBMST) codes. However, the simulation results show that, in finite-length regime, negligible performance gain is obtained by increasing the encoding memory. We solve this limitation by introducing partial superposition, and the resulting codes are termed as partially-connected BiBMST (PC-BiBMST) code. Analytical results have confirmed the advantages of the PC-BiBMST codes over the original BiBMST codes. We also present extensive simulation results to show the performance advantages of the PC-BiBMST codes over the spatially coupled low-density parity-check (SC-LDPC) codes, spatially coupled generalized LDPC (SC-GLDPC) codes, and the original BiBMST codes in the finite-length regime.

## Satellite-to-Ground Continuous Variable Quantum Key Distribution: The Gaussian and Discrete Modulated Protocols in Low Earth Orbit

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10415457
- **Type**: journal
- **Published**: June 2024
- **Authors**: Mikhael T. Sayat, Biveen Shajilal, Sebastian P. Kish +5
- **PDF**: https://ieeexplore.ieee.org/document/10415457
- **Abstract**: The Gaussian modulated continuous variable quantum key distribution (GM-CVQKD) protocol is known to maximise the mutual information between two parties during quantum key distribution (QKD). An alternative modulation scheme is the discrete modulated CVQKD (DM-CVQKD) protocol. In this paper, we perform a feasibility study for practical satellite-to-ground CVQKD with a focus on comparing existing GM-CVQKD and DM-CVQKD protocols with the application of the performance of recent reconciliation methods. We use a satellite-to-ground link model which takes into account geometric, scintillation, and scattering losses from the link distance, atmospheric turbulence, and atmospheric aerosols, respectively. In addition, recent multidimensional (MD) and multilevel coding and multistage decoding (MLC-MSD) reconciliation method models in combination with multiedge-type low-density parity-check (MET-LDPC) code models have been used to determine the reconciliation efficiency. Realistic parameters have been used for the calculation of the secret key rate (SKR) along with a comparison between MD and MLC-MSD reconciliation during satellite-to-ground GM-CVQKD, for the first time. The results show that GM-CVQKD outperforms DM-CVQKD. In addition, GM-CVQKD with MD reconciliation outperforms GM-CVQKD with MLC-MSD reconciliation in the finite size limit by producing positive SKRs at larger link distances and lower elevation angles.

## Memory AMP for Generalized MIMO: Coding Principle and Information-Theoretic Optimality

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10332136
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yufei Chen, Lei Liu, Yuhao Chi +2
- **PDF**: https://ieeexplore.ieee.org/document/10332136
- **Abstract**: To support complex communication scenarios in next-generation wireless communications, this paper focuses on a generalized MIMO (GMIMO) with practical assumptions, such as massive antennas, practical channel coding, arbitrary input distributions, and general right-unitarily-invariant channel matrices (covering Rayleigh fading, certain ill-conditioned and correlated channel matrices). The orthogonal/vector approximate message passing (OAMP/VAMP) receiver has been proved to be information-theoretically optimal in GMIMO, but it is limited to high-complexity linear minimum mean-square error (LMMSE). To solve this problem, a low-complexity memory approximate message passing (MAMP) receiver has recently been shown to be Bayes optimal but limited to uncoded systems. Therefore, how to design a low-complexity and information-theoretically optimal receiver for GMIMO is still an open issue. To address this issue, this paper proposes an information-theoretically optimal MAMP receiver and investigates its achievable rate analysis and optimal coding principle. Specifically, due to the long-memory linear detection, state evolution (SE) for MAMP is intricately multi-dimensional and cannot be used directly to analyze its achievable rate. To avoid this difficulty, a simplified single-input single-output (SISO) variational SE (VSE) for MAMP is developed by leveraging the SE fixed-point consistent property of MAMP and OAMP/VAMP. The achievable rate of MAMP is calculated using the VSE, and the optimal coding principle is established to maximize the achievable rate. On this basis, the information-theoretic optimality of MAMP is proved rigorously. Furthermore, the simplified SE analysis by fixed-point consistency is generalized to any two iterative detection algorithms with the identical SE fixed point. Numerical results show that the finite-length performances of MAMP with practical optimized low-density parity-check (LDPC) codes are  $0.5 \sim 2.7$  dB away from the associated constrained capacities. It is worth noting that MAMP can achieve the same performances as OAMP/VAMP with  $4\%$  of the time consumption for large-scale systems.

## Optimal Single-Shot Decoding of Quantum Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10477410
- **Type**: journal
- **Published**: June 2024
- **Authors**: Aldo Cumitini, Stefano Tinelli, Balázs Matuz +2
- **PDF**: https://ieeexplore.ieee.org/document/10477410
- **Abstract**: We discuss single-shot decoding of quantum Calderbank-Shor-Steane codes with faulty syndrome measurements. We state the problem as a joint source-channel coding problem. By adding redundant rows to the code’s parity-check matrix, we obtain an additional syndrome error correcting code which addresses faulty syndrome measurements. Thereby, the redundant rows are chosen to obtain good syndrome error correction capabilities while keeping the stabilizer weights low. Optimal joint decoding rules are derived which, though too complex for general codes, can be evaluated for short quantum codes.

## Deep Learning-Empowered Semantic Communication Systems With a Shared Knowledge Base

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10318078
- **Type**: journal
- **Published**: June 2024
- **Authors**: Peng Yi, Yang Cao, Xin Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/10318078
- **Abstract**: Deep learning-empowered semantic communication is regarded as a promising candidate for future 6G networks. Although existing semantic communication systems have achieved superior performance compared to traditional methods, the end-to-end architecture adopted by most semantic communication systems is regarded as a black box, leading to the lack of explainability. To tackle this issue, in this paper, a novel semantic communication system with a shared knowledge base is proposed for text transmissions. Specifically, a textual knowledge base constructed by inherently readable sentences is introduced into our system. With the aid of the shared knowledge base, the proposed system integrates the message and corresponding knowledge from the shared knowledge base to obtain the residual information, which enables the system to transmit fewer symbols without semantic performance degradation. In order to make the proposed system more reliable, the semantic self-information and the source entropy are mathematically defined based on the knowledge base. Furthermore, the knowledge base construction algorithm is developed based on a similarity-comparison method, in which a pre-configured threshold can be leveraged to control the size of the knowledge base. Moreover, the simulation results have demonstrated that the proposed approach outperforms existing baseline methods in terms of transmitted data size and sentence similarity.

## Low Complexity Turbo SIC-MMSE Detection for Orthogonal Time Frequency Space Modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10411929
- **Type**: journal
- **Published**: June 2024
- **Authors**: Qi Li, Jinhong Yuan, Min Qiu +2
- **PDF**: https://ieeexplore.ieee.org/document/10411929
- **Abstract**: Recently, orthogonal time frequency space (OTFS) modulation has garnered considerable attention due to its robustness against doubly-selective wireless channels. In this paper, we propose a low-complexity iterative successive interference cancellation based minimum mean squared error (SIC-MMSE) detection algorithm for zero-padded OTFS (ZP-OTFS) modulation. In the proposed algorithm, signals are detected based on layers processed by multiple SIC-MMSE linear filters for each sub-channel, with interference on the targeted signal layer being successively canceled either by hard or soft information. To reduce the complexity of computing individual layer filter coefficients, we also propose a novel filter coefficients recycling approach in place of generating the exact form of MMSE filter weights. Moreover, we design a joint detection and decoding algorithm for ZP-OTFS to enhance error performance. Compared to the conventional SIC-MMSE detection, our proposed algorithms outperform other linear detectors, e.g., maximal ratio combining (MRC), for ZP-OTFS with up to 3 dB gain while maintaining comparable computation complexity.

## Survey for a Decade of Coding for DNA Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10535435
- **Type**: journal
- **Published**: June 2024
- **Authors**: Omer Sabary, Han Mao Kiah, Paul H. Siegel +1
- **PDF**: https://ieeexplore.ieee.org/document/10535435
- **Abstract**: Advancements in DNA synthesis and sequencing technologies have enabled the storage of data on synthetic DNA strands. However, realizing its potential relies on the design of tailored coding techniques and algorithms. This survey paper offers an overview of past contributions, accompanied by a special issue that showcases recent developments in this field.

## Post-Quantum Authentication Against Cyber-Physical Attacks in V2X-Based Autonomous Vehicle Platoon

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10368128
- **Type**: journal
- **Published**: June 2024
- **Authors**: Dongyang Xu, Keping Yu, Lei Liu +4
- **PDF**: https://ieeexplore.ieee.org/document/10368128
- **Abstract**: In this paper, we propose a platoon access authentication system for initial access process in autonomous vehicle platoons (AVPs) in which post-quantum encryption and signal processing techniques are employed to protect against both active and passive cyber-physical attacks. To avoid passive quantum cyber attacks, a quasi-cyclic moderate-density parity-check code is used to encode and decode AVP messages. Moreover, an independent component analysis-based signal separation technique is employed to eliminate the effect of high-power active cyber attacks on AVP messages. To measure the reliability of the system, we derive an analytical expression for the system failure probability, taking into account the influence of both the cyber and physical planes. The simulations show that the proposed system is effective against attacks and can help reduce system failures caused by intentional and unintentional adverse cyber-physical effects. The proposed system offers a potential solution to the challenge of protecting initial access while maintaining ultra-reliable low-latency communications between AVPs and the infrastructure.

## Exploiting FDD Channel Reciprocity for Physical Layer Secret Key Generation in IoT Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10497579
- **Type**: journal
- **Published**: June 2024
- **Authors**: Ehsan Olyaei Torshizi, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/10497579
- **Abstract**: The utilization of physical layer Secret Key Generation (SKG) is increasingly prevalent in securing wireless communication within Internet of Things systems, particularly in Narrow-band IoT. While most key-generation schemes are tailored for Time Division Duplex (TDD) systems, generating secret keys in Frequency Division Duplex (FDD) systems presents challenges due to the distinct frequency bands for uplink and downlink. In response to this, we propose an efficient FDD-based key generation technique that capitalizes on the reciprocity of scattering matrix parameters  $S_{12}$  and  $S_{21}$  within the same frequency range. Specifically, we harness the capabilities of MUSIC algorithm during the direction of arrival estimation phase. Numerical results demonstrate promising outcomes in addressing key challenges, including randomness, and Key Disagreement Ratio (KDR).

## Polar-Coded Gaussian Multiple-Access Channels With Physical-Layer Network Coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10388470
- **Type**: journal
- **Published**: June 2024
- **Authors**: Yuping Qiu, Zhaopeng Xie, Peng Kang +2
- **PDF**: https://ieeexplore.ieee.org/document/10388470
- **Abstract**: In this paper, we propose a two-user polar-coded physical-layer network coding (TU-PC-PNC) scheme for the Gaussian multiple access channel (GMAC) to enhance the transmission reliability. We first investigate the characteristics of polar encoding and derive the concatenated codeword structure, by which we can implement the message exclusive OR (XOR)-based PNC via code construction and improve the channel polarization effect. The PNC-aided decoding rule based on the concatenated codeword is then invented to compute the initial messages for recovery. In addition, we introduce the joint optimization framework by Monte Carlo-based method, which can be used to optimize the polar code and power allocation with maximized sum user rate. The capacity analysis of the bit-channels and simulation results show that the proposed TU-PC-PNC can significantly outperform the benchmark scheme by more than 1 dB under the GMAC.

## IRSA-Based Random Access Over the Gaussian Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10411106
- **Type**: journal
- **Published**: June 2024
- **Authors**: Velio Tralli, Enrico Paolini
- **PDF**: https://ieeexplore.ieee.org/document/10411106
- **Abstract**: A framework for the analysis of synchronous grant-free massive multiple access schemes based on the irregular repetition slotted ALOHA (IRSA) protocol and operating over the Gaussian multiple access channel is presented. IRSA-based schemes are considered here as an instance of the class of unsourced slotted random access codes, operating over a frame partitioned in time slots, and are obtained by concatenation of a medium access control layer code over the entire frame and a physical layer code over each slot. In this framework, an asymptotic analysis is carried out in presence of both collisions and slot decoding errors due to channel noise, which allows the derivation of density-evolution equations, asymptotic limits for minimum packet loss probability and average load threshold, and a converse bound for threshold values. This analysis is exploited as a tool for the evaluation of performance limits in terms of minimum signal-to-noise ratio required to achieve a given packet loss probability, and also provides convergence boundary limits that hold for any IRSA scheme with given physical layer coding scheme. The tradeoff between energy efficiency and spectrum efficiency is numerically evaluated comparing some known coding options, including those achieving random coding bounds at slot level. It is shown that IRSA-based schemes have a convergence boundary limit within few dB from the random coding bound when the number of active transmitters is sufficiently large.

## Entropy-Based Energy Dissipation Analysis of Mobile Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10301609
- **Type**: journal
- **Published**: June 2024
- **Authors**: Litao Yan, Xiaohu Ge
- **PDF**: https://ieeexplore.ieee.org/document/10301609
- **Abstract**: One of the most prominent physical aspects of mobile communication systems is that they are inherently non-equilibrium systems. Traditional researches on the energetic costs of communication systems pay little attention to the relationship between the energy and the information transmitted and processed by the system. On the other hand, recent breakthroughs in nonequilibrium thermodynamics have led to a deeper understanding of the thermodynamics of information. To investigate the energetic costs of a mobile communication system at a fundamental level, in this paper, an entropy-based energy dissipation model based on nonequilibrium thermodynamics is first proposed for mobile communication systems. The energy dissipation model relates the energy and information through the common concept “entropy” from thermodynamics and information theory. Moreover, the theoretical minimal energy dissipation limits are derived for typical modulations in mobile communication systems. Simulation results show that the practical energy dissipation of information processing and information transmission is three and seven orders of magnitude away from the theoretical minimal energy dissipation limits in mobile communication systems, respectively. The energy dissipation model and results derived in the paper provide guidelines on how to design future mobile communication systems to minimize the thermodynamic costs.

## SIC-Based UAMP Detection for MIMO-OTFS Under Fractional Delay-Doppler Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10500696
- **Type**: journal
- **Published**: June 2024
- **Authors**: Jin Xu, Xuanyun Ma, Kai Niu +1
- **PDF**: https://ieeexplore.ieee.org/document/10500696
- **Abstract**: Orthogonal Time Frequency Space (OTFS) has proven to be an effective solution for transmission in high-speed mobile scenarios. The combination of multiple input multiple output and OTFS (MIMO-OTFS) can obtain advantages in transmission rate and spectral efficiency. However, the spatial coupling interference present in MIMO-OTFS poses a challenge to signal detection. This letter focuses on the symbol detection of MIMO-OTFS systems under fractional delay-Doppler channels. Aiming at the spatial coupling interference and inter-symbol interference (ISI) existing in the system, we propose a unitary transform approximate message passing detection algorithm based on serial interference cancellation (SIC-UAMP). It conducts cyclic redundancy check (CRC) on the decoded data streams and feeds back the correctly decoded part to the detector to eliminate the interference. Additionally, we introduce an empirical extrinsic information transfer (E-EXIT) chart to offer a more precise depiction of the iterative detection compared to the traditional EXIT chart. Simulation results under fast fading Rayleigh channels show that SIC-UAMP performs better than UAMP, especially in the medium to high signal-to-noise ratio (SNR) range.

## Joint Design of Denoising Diffusion Probabilistic Models and LDPC decoding for Wireless Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10615729
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Xudong Guan, Hao Ju, Yin Xu +4
- **PDF**: https://ieeexplore.ieee.org/document/10615729
- **Abstract**: Due to its powerful generative capabilities, denoising diffusion probabilistic models (DDPM) have found applications in various domains. In this paper, DDPM is employed in a wireless channel receiver, where we design a decoder structure incor-porating DDPM and low-density parity-check (LDPC) decoding to enhance the error correction capabilities of the receiver. The LDPC decoding method based on DDPM proposed in this paper is iterative. The received signal must pass through the DDPM and demodulation modules first. The output is multiplied with the LDPC parity check matrix to get the parity information and then feedback to the DDPM module to assist and carry out the following iterative denoising output. Compared with the typical communication system, the LDPC decoding method proposed in this paper utilizes the diffusion model to assist the channel equal-ization with the parity check information generated during the decoding process and realizes the inter-module joint optimization at the receiver. Also, in order to have a better performance on processing and predicting sequence data, recurrent neural net-work (RNN) is a reasonable choice for its unique circular concept and the long-short-term memory network structure. This paper proved that the proposed decoding method has BER performance gains of 0.5dB to 0.2dB over the typical LDPC decoding methods using normalized min-sum(NMS) algorithm under additive white Gaussian noise (AWGN) channel and Rayleigh channel.

## Zak-OTFS and LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622586
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Beyza Dabak, Venkatesh Khammammetti, Saif Khan Mohammed +1
- **PDF**: https://ieeexplore.ieee.org/document/10622586
- **Abstract**: Orthogonal Time Frequency Space (OTFS) is a framework for communications and active sensing that processes signals in the delay-Doppler (DD) domain. It is informed by 6G propagation environments, where Doppler spreads measured in $\text{kHz}$ make it more and more difficult to estimate channels, and the standard model-dependent approach to wireless communication is starting to break down. We consider Zak-OTFS where inverse Zak transform converts information symbols mounted on DD domain pulses to the time domain for transmission. Zak-OTFS modulation is parameterized by a delay period $\tau_{p}$ and a Doppler period $\nu_{p}$, where the product $\nu_{p}\nu_{p}=1$. When the channel spread is less than the delay period, and the Doppler spread is less than the Doppler period, the Zak-OTFS input-output relation can be predicted from the response to a single pilot symbol. The highly reliable channel estimates concentrate around the pilot location, and we configure low-density parity-check (LDPC) codes that take advantage of this prior information about reliability. It is advantageous to allocate information symbols to more reliable bins in the DD domain. We report simulation results for a Veh-A channel model where it is not possible to resolve all the paths, showing that LDPC coding extends the range of Doppler spreads for which reliable model-free communication is possible. We show that LDPC coding reduces sensitivity to the choice of transmit filter, making bandwidth expansion less necessary. Finally, we compare BER performance of Zak-OTFS to that of a multicarrier approximation (MC-OTFS), showing LDPC coding amplifies the gains previously reported for uncoded transmission.

## High-Rate Fair-Density Parity-Check Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622808
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Hessam Mahdavifar
- **PDF**: https://ieeexplore.ieee.org/document/10622808
- **Abstract**: We introduce fair-density parity-check (FDPC) codes targeting high-rate applications. In particular, we start with a base parity-check matrix $H_{b}$ of dimension $2\sqrt{n}\times n$, where $n$ is the code block length, and the number of ones in each row and column of $H_{b}$ is equal to $\sqrt{n}$ and 2, respectively. We propose a deterministic combinatorial method for picking the base matrix $H_{b}$, assuming $n=4t^{2}$ for some integer $t\geqslant 2$. We then extend this by obtaining permuted versions of $H_{b}$ (e.g., via random permutations of its columns) and stacking them on top of each other leading to codes of dimension $k\geqslant n-2s\sqrt{n}+s$, for some $s\geqslant 2$, referred to as order-s FDPC codes. We propose methods to explicitly characterize and bound the weight distribution of the new codes and utilize them to derive union-type approximate upper bounds on their error probability under Maximum Likelihood (ML) decoding. For the binary erasure channel (BEC), we demonstrate that the approximate ML bound of FDPC codes closely follows the random coding upper bound (RCU) for a wide range of channel parameters. Also, remarkably, FDPC codes, under the low-complexity min-sum decoder, improve upon 5G-LDPC codes for transmission over the binary-input additive white Gaussian noise (B-AWGN) channel by almost 0.5dB (for $n=1024$, and rate = 0.878). Furthermore, we propose a new decoder as a combination of weighted min-sum message-passing (MP) decoding algorithm together with a new progressive list (PL) decoding component, referred to as the MP-PL decoder, to further boost the performance of FDPC codes. This paper opens new avenues for a fresh investigation of new code constructions and decoding algorithms in high-rate regimes suitable for ultra-high throughput (high-frequency/optical) applications.

## Neural Belief Propagation Decoders for Concatenated Calderbank-Shor-Steane Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622478
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Jihao Fan, Jinbing Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10622478
- **Abstract**: Quantum low-density parity check (QLDPC) codes have rapidly developed in the field of quantum error correction in recent years. A variety of quantum code families have emerged from numerous research activities. In this paper, we employ concatenated Calderbank-Shor-Steane (CSS) codes, hypergraph product codes, and Bacon-Shor codes to train belief-propagation (BP) and neural BP (NBP) decoders. At the same time, we employ a concatenation scheme in BP and NBP, the amplified construction of CSS codes is realized, and the training of longer length parameter quantum codes is realized. The numerical results show that the concatenated CSS codes demonstrate better error correction performance compared to both hypergraph product codes and Bacon-Shor codes. In addition, the concatenated CSS codes are trained using the concatenation scheme to improve the error correction performance of the decoder.

## Effect of Feedback Delay on Adaptive LDPC Coding in a Fading Free-Space Optical Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622619
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Semira Galijasevic, Jingchao Luo, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/10622619
- **Abstract**: Free-space optical (FSO) links are sensitive to channel fading caused by atmospheric turbulence, varying weather conditions, and changes in the distance between the transmitter and receiver. To mitigate FSO fading, this paper applies linear and quadratic prediction to estimate fading channel conditions and dynamically select the appropriate low-density parity check (LDPC) code rate. This adaptivity achieves reliable communication while efficiently utilizing the available channel mutual information. Protograph-based Raptor-like (PBRL) LDPC codes supporting a wide range of rates are designed, facilitating convenient rate switching. When channel state information (CSI) is known without delay, dynamically selecting LDPC code rate appropriately maximizes throughput. This work explores how such prediction behaves as the feedback delay is increased from no delay to a delay of 4 ms for a channel with a coherence time of 10 ms.

## Low-Complexity Linear Programming Based Decoding of Quantum LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622622
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Sana Javed, Francisco Garcia-Herrero, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/10622622
- **Abstract**: This paper proposes two approaches for reducing the impact of the error floor phenomenon when decoding quantum low-density parity-check codes with belief propagation based algorithms. First, a low-complexity syndrome-based linear programming (SB- LP) decoding algorithm is proposed, and second, the proposed SB-LP is applied as a post-processing step after syndrome-based min-sum (SB-MS) decoding. For the latter case, a new early stopping criterion is introduced to decide when to activate the SB- LP algorithm, avoiding executing a predefined maximum number of iterations for the SB-MS decoder. Simulation results show, for a sample hypergraph code, that the proposed decoder can lower the error floor by two to three orders of magnitude compared to SB-MS for the same total number of decoding iterations.

## Efficient Near Maximum-Likelihood Reliability-Based Decoding for Short LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622261
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Weiyang Zhang, Chentao Yue, Yonghui Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10622261
- **Abstract**: In this paper, we propose an efficient decoding algorithm for short low-density parity check (LDPC) codes by carefully combining the belief propagation (BP) decoding and ordered statistics decoding (OSD) algorithms. Specifically, a modified BP (mBP) algorithm is applied for a certain number of iterations prior to OSD to enhance the reliability of the received message, where an offset parameter is utilized in mBP to control the weight of the extrinsic information in message passing. By carefully selecting the offset parameter and the number of mBP iterations, the number of errors in the most reliable positions (MRPs) in OSD can be reduced by mBP, thereby significantly improving the overall decoding performance of error rate and complexity. Simulation results show that the proposed algorithm can approach the maximum-likelihood decoding (MLD) for short LDPC codes with only a slight increase in complexity compared to BP and a significant decrease compared to OSD. Specifically, the order- (m -1) decoding of the proposed algorithm can achieve the performance of the order-m OSD.

## A Deep Learning Based Decoder for Concatenated Coding Over Deletion Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622561
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: E. Uras Kargı, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/10622561
- **Abstract**: In this paper, we introduce a deep learning-based decoder designed for concatenated coding schemes over a deletion/substitution channel. Specifically, we focus on serially concatenated codes, where the outer code is either a convolutional or a low-density parity-check (LDPC) code, and the inner code is a marker code. We utilize Bidirectional Gated Recurrent Units (BI-GRUs) as log-likelihood ratio (LLR) estimators and outer code decoders for estimating the message bits. Our results indicate that decoders powered by BI-GRUs perform comparably in terms of error rates with the MAP detection of the marker code. We also find that a single network can work well for a wide range of channel parameters. In addition, it is possible to use a single BI-GRU based network to estimate the message bits via one-shot decoding when the outer code is a convolutional code. 11Code is available at https://github.com/Bilkent-CTAR-Lab/DNN-for-Deletion-Channel

## A Unified Hierarchical Semantic Knowledge Base for Multi-Task Semantic Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622764
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Lingyi Wang, Wei Wu, Fuhui Zhou +3
- **PDF**: https://ieeexplore.ieee.org/document/10622764
- **Abstract**: Semantic communication is a promising approach to address the challenge of limited spectrum resources in the sixth-generation (6G) communication networks. However, prior works on semantic communication focus primarily on semantic coding, and they do not investigate how to efficiently construct a semantic knowledge base. In this paper, a codebook-based unified hierarchical semantic knowledge base (UH-SKB) framework is studied for multi-task semantic communications. To maximize semantic representation spaces and effectively explore the semantic relevance among multiple tasks, the semantic knowledge base is constructed jointly in both the horizontal and vertical directions. A deep K-subspace cluster method is proposed to facilitate semantic relevance extraction and semantic subspace construction for high-dimensional semantic information. Simulation results demonstrate that the proposed UH-SKB can support multi-task semantic communications efficiently, achieving up to 13.4%, 14% and 6.3% performance improvement respectively for reconstruction, segmentation and classification tasks compared to standalone semantic knowledge bases at the novel dataset when SNR is 0 dB. Moreover, the proposed UH-SKB exhibits 95.3% knowledge search efficiency improvement on the reconstruction task compared to standalone semantic knowledge bases.

## Multimodal Large Language Models Driven Privacy-Preserving Wireless Semantic Communication in 6G

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10615340
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Daipeng Cao, Jun Wu, Ali Kashif Bashir
- **PDF**: https://ieeexplore.ieee.org/document/10615340
- **Abstract**: In the context of 6G and artificial intelligence, the amount of data on the internet is rapidly increasing. However, traditional syntactic communication encoding techniques are approaching the Shannon limit and have reached a bottleneck. Semantic communication can significantly reduce data traffic and enhance communication efficiency by converting multimodal data, such as images, audio, and video, into semantic information for transmission. However, current semantic communication technology is still in its early stages and faces many challenges. The main challenges in semantic communication currently include data heterogeneity, semantic consistency, and privacy issues. Multimodal large language models (MLLM) could perform semantic understanding of multimodal data and semantic-based multimodal data generation, which offer a unified and consistent multimodal semantic conversion. Therefore, we propose a Privacy-Preserving Semantic Communication scheme based on MLLM (MLLM-PSC). The semantic interpretation ability of MLLM-PSC is cultivated based on the pre-training and fine-tuning of MLLM, without the need for additional knowledge base (KB) alignment. We take textual semantics as a medium for consistently conversion of multimodal data, while safeguarding sensitive semantic information based on few-shot learning. Our simulation results demonstrate the superior performance of MLLM-PSC.

## Knowledge Graph Driven UAV Cognitive Semantic Communication Systems for Efficient Object Detection

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622874
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Xi Song, Lu Yuan, Zhibo Qu +4
- **PDF**: https://ieeexplore.ieee.org/document/10622874
- **Abstract**: Unmanned aerial vehicles (UAVs) are widely used for object detection. However, the existing UAV-based object detection systems are subject to the serious challenge, namely, the finite computation, energy and communication resources, which limits the achievable detection performance. In order to overcome this challenge, a UAV cognitive semantic communication system is proposed by exploiting knowledge graph. Moreover, a multi-scale compression network is designed for semantic compression to reduce data transmission volume while guaranteeing the detection performance. Furthermore, an object detection scheme is proposed by using the knowledge graph to overcome channel noise interference and compression distortion. Simulation results conducted on the practical aerial image dataset demonstrate that compared to the benchmark systems, our proposed system has superior detection accuracy, communication robustness and computation efficiency even under high compression rates and low signal-to-noise ratio (SNR) conditions.

## A Methodology and Testbed to Develop an Energy Model for 5G Virtualized RANs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10615464
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Sofia Martins, Ana Aguiar, Peter Steenkiste
- **PDF**: https://ieeexplore.ieee.org/document/10615464
- **Abstract**: Virtualized Radio Access Networks are a promising solution to reduce the energy consumption of 5G networks. However, the shift from traditional to virtualized RANs has rendered existing energy models for RANs obsolete. In this paper, we present a methodology and testbed to develop an energy model for vRANs. Our methodology estimates the energy consumption of Baseband Unit functions based on performance monitoring counters and utilization metrics collected on a testbed. Our experimental results offer insights into the distribution of energy consumption across RAN functions. These results suggest that, under our experimental conditions, the physical layer is considerably more energy-intensive than other layers. We believe that this methodology can serve as a foundation for constructing an energy consumption model that will facilitate the development of energy-aware load balancers and the selection of energyefficient RAN deployments, leading to significant energy savings.

## Short Blocklength Secret Coding via Helper-Assisted Learning over the Wiretap Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10623082
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Vidhi Rana, Rémi A. Chou, Taejoon Kim
- **PDF**: https://ieeexplore.ieee.org/document/10623082
- **Abstract**: Consider the Gaussian wiretap channel, where a legitimate transmitter wishes to send a confidential message to a legitimate receiver in the presence of an eavesdropper. Unfortunately, in this setting, it is well known that if the eavesdropper experiences less channel noise than the legitimate receiver, then it is impossible for the transmitter to achieve positive secrecy rates. A known solution to this issue consists in involving a second transmitter, referred to as a helper, to help the first transmitter to achieve security. While such a solution has been studied for the asymptotic blocklength regime and via non-constructive coding schemes, in this paper, for the first time, we design explicit and short blocklength codes using deep learning and cryptographic tools to demonstrate the benefit and practicality of cooperation between two transmitters over the wiretap channel. Specifically, our proposed codes show strict improvement in terms of information leakage compared to existing point-to-point codes that do not consider a helper, even when the transmitter has adverse channel conditions, in the sense that the eavesdropper experiences less channel noise than the legitimate receiver. Our code design approach relies on a reliability layer, implemented with an autoencoder architecture inspired by the successive interference cancellation method developed for broadcast channels, and a security layer implemented with universal hash functions.

## Linear Jamming Bandits: Learning to Jam OFDM-Modulated Signals

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622747
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Zachary Schutz, Daniel J. Jakubisin, Charles E. Thornton +1
- **PDF**: https://ieeexplore.ieee.org/document/10622747
- **Abstract**: This work investigates the use of linear reinforce-ment learning to effectively jam an OFDM-modulated victim signal. Prior work has shown improved convergence with the use of linear bandits, a variant of reinforcement learning, to jam single-carrier digital phase-amplitude modulation schemes using time-domain (TD) jamming schemes. However, communication systems today typically employ orthogonal frequency division multiplexing (OFDM) to transmit data, particularly in 4G/5G networks. This work explores the use of linear Thompson Sampling (TS) to efficiently jam OFDM-modulated signals where the jammer may select from single-carrier and OFDM jamming schemes. We show that linear TS performs better than traditional reinforcement learning (UCB-1 algorithm) in terms of maximizing the victim symbol error rate (SER). We also draw novel insights by observing the action states to which the reinforcement learning algorithm converges to.

## Cycle-Detection Based Decimation Policies for Lossy Source Encoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10622968
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Masoumeh Alinia, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/10622968
- **Abstract**: We propose a variant of the belief propagation guided decimation (BPGD) algorithm for the lossy binary sym-metric source coding problem, called DeciPolicy, which enables different decimation policies to decide when to trigger decimation, which variables to decimate, and which value to assign to decimated bits. In particular, we introduce a method that uses information about the cycles existing in the graph of a low-density generator matrix (LDGM) code to select candidate nodes for decimation. The proposed family of policies can be combined to include cycle detection-based decimation, parallel decimation of several bits, and random or hard value assignment. We demonstrate the algorithms on different constructions of LDGM codes, including an optimized irregular degree distribution and semi-regular Ising models, and show that our decimation policies lower the distortion when compared to various classical soft and hard BPGD algorithms, closing the gap to the rate-distortion limit.

## Deep Learning based Joint Source-Channel Coding for Computer-generated Holograms

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10615727
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Jing-Kai Huang, Chia-Han Lee
- **PDF**: https://ieeexplore.ieee.org/document/10615727
- **Abstract**: Computer-generated holography (CGH) is a technique used to create and reconstruct 3D scenes through numerical calculations on computers to provide immersive visual experiences. CGH is expected to have diverse applications, but how to efficiently encode, transmit, and decode holograms is less discussed. In this paper, we propose a deep learning (DL)-based end-to-end design of joint encoding, transmission, and decoding of holograms in the hologram domain, called deep hologram joint source-channel coding network (DHJSCCN). At the transmitter, the joint design of the source encoder and the channel encoder allows for the efficient compression and transmission of the phase component of CGHs, while at the receiver, the corrupted signal can be decoded and reconstructed by the joint design of the source decoder and the channel decoder. Simulation results demonstrate that the proposed DHJSCCN achieves a significant improvement in peak signal-to-noise ratio (PSNR) compared to JPEG2000+LDPC under both the additive white Gaussian noise (AWGN) channel and the slow fading channel. Compared to the state-of-the-art DL-based designs, DHJSCCN also shows 1 dB improvement in PSNR with about 35% lower complexity.

## Combating Multi-Path Interference to Improve Chirp-Based Underwater Acoustic Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10623112
- **Type**: conference
- **Published**: 9-13 June 
- **Authors**: Wenjun Xie, Enqi Zhang, Lizhao You +3
- **PDF**: https://ieeexplore.ieee.org/document/10623112
- **Abstract**: Linear chirp-based underwater acoustic communication has been widely used due to its reliability and long-range transmission capability. However, unlike the counterpart chirp technology in wireless - LoRa, its throughput is severely limited by the number of modulated chirps in a symbol. The fundamental challenge lies in the underwater multi-path channel, where the delayed signal may cause inter-symbol and intra-symbol interfere. In this paper, we present UWLoRa+, a system that realizes the same chirp modulation as LoRa with higher data rate, and address the multi-path challenge via the following new designs: a) we replace the linear chirp used by LoRa with the non-linear chirp to reduce the signal interference range and the collision probability; b) we design an algorithm that first demodulates each path and then combines the demodulation results of detected paths; and c) we replace the Hamming codes used by LoRa with the non-binary LDPC codes to mitigate the impact of the inevitable collision. Experiment results show that the new designs improve the bit error rate (BER) by 3 times, and the packet error rate (PER) significantly, compared with the LoRa's naive design. Compared with an state-of-the-art system for decoding underwater LoRa chirp signal, UWLoRa+ improves the throughput by up to 50 times.

## Implementation of LDPC Decoder using Barrel Shifter

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10575499
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: Bhavya Lakshmi Tulasi Edara, T Guhambika Naga Aishwarya, Saahith Reddy Patlolla +1
- **PDF**: https://ieeexplore.ieee.org/document/10575499
- **Abstract**: The research work explores the implementation of an LDPC decoder utilizing a barrel shifter architecture tailored for processing 128-bit data. LDPC codes are recognized for their efficacy in error correction across various communication systems, necessitating efficient decoding mechanisms. Integration of a barrel shifter into the decoder architecture facilitates essential shifting operations required for LDPC decoding, thereby enhancing throughput and minimizing latency. The study delves into the design considerations for the barrel shifter-based implementation and elucidates the LDPC decoding algorithm. Through simulation, the performance of the proposed decoder is evaluated in terms of throughput, latency, and resource utilization. The experimental results validate the feasibility and effectiveness of the LDPC decoder with a barrel shifter architecture for processing 128-bit data, underscoring its potential for integration into high-speed communication systems.

## Improving the Power Efficiency in OFDM System using LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10575635
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: M Selvi, S Jeeva, J Jaswanth
- **PDF**: https://ieeexplore.ieee.org/document/10575635
- **Abstract**: Orthogonal Frequency Division Multiplexing (OFDM) systems have power usage issues due to the high Peak-to-Average Power Ratio (PAPR). Signal distortion and inefficiency result from clipping and filtering’s limited PAPR reduction. An innovative approach using Low-Density Parity-Check (LDPC) codes in OFDM is proposed to address the. LDPC codes strive to minimize PAPR values while maintaining signal integrity with greater error correction and flexibility. A meticulous LDPC matrix design using Progressive Edge Growth (PEG), efficient Sum-Product Algorithm (SPA) encoding/decoding, and OFDM transmitter integration methodologies are used in the system. Extensive models and testing show significant PAPR reduction and BER improvements over conventional systems. Results show consistent PAPR reductions from 5.8 to 7.2 dB and lower BER values across channel circumstances. LDPC matrix size research shows that a $2 \times 4$ matrix has a lower BER of 0.0934 than a $4 \times 5$ matrix. The LDPC-based technique improves power economy and reliability in OFDM systems, promising broad applications in wireless communication networks and multimedia transmission.

## Integrating Emerging Technologies with Infrastructure as Code in Distributed Environments

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10575600
- **Type**: conference
- **Published**: 5-7 June 2
- **Authors**: Syed Imran Abbas, Ankit Garg
- **PDF**: https://ieeexplore.ieee.org/document/10575600
- **Abstract**: Manual provisioning of infrastructure limited flexibility, scalability, and stability in distributed environments. The adoption of Infrastructure as Code (IaC) principles has dramatically enhanced deployment agility, reducing infrastructure change implementation to mere minutes. Automation facilitated dynamic scaling, optimizing resource utilization and cost efficiency. By standardizing configurations as code, IaC improved consistency and reliability, mitigating the risks associated with configuration drift and security vulnerabilities. This shift significantly reduced operational overhead, allowing IT teams to concentrate on strategic initiatives. Uniform and auditable configurations strengthened security and compliance, ensuring adherence to regulatory standards. The integration of IaC with emerging technologies has revolutionized organizational operations, enabling enterprises to navigate complex digital landscapes with increased agility and resilience. Through automation and standardization, organizations are now better positioned for sustained success and competitiveness in the evolving digital era.

## The Comparative Analysis of Single Error Bursts Decoders for Linear Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10564623
- **Type**: conference
- **Published**: 3-7 June 2
- **Authors**: A. M. Veresova, M. N. Isaeva, A. A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/10564623
- **Abstract**: The article considers the problem of correcting single error bursts, taking into account the influence of the structure of the linear block code parity-check matrix on the performance of decoding algorithms. A heuristic algorithm based on the determination of certain events and an algorithm based on dense information sets for correcting single error bursts are considered. Codes based on a block-permutation construction, as well as random linear codes, are selected. Experiments have been conducted to evaluate the computational efficiency and error probability for the codes and decoders under consideration, taking into account the density of the parity-check matrices and the construction of the codes. It is obtained that when using a block-permutation construction, the heuristic algorithm shows a much lower probability of error with an operating time slightly inferior to the decoder based on dense information sets. However, when the structure of the sparse parity-check matrix changes, the decoding complexity increases, and with increasing matrix density, the complexity of the heuristic algorithm tends to exponential even with small burst lengths. For matrices that do not have a block-permutation structure, the algorithm based on dense information sets shows the best error probability and operating time. Thus, based on the comparative analysis carried out, it can be concluded that the task of correcting single error bursts can be solved with polynomial complexity regardless of the structure of the linear code and optimized taking into account this structure.

## Receiver Metric Design for Short-Block Channels : A Perspective for Reliable 6G Signaling Scenarios

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10597121
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Mody Sy, Raymond Knopp
- **PDF**: https://ieeexplore.ieee.org/document/10597121
- **Abstract**: This paper introduces receiver metrics for joint estimation and detection in short block length channels, emphasizing enhanced performance for advanced receivers, especially in scenarios with unknown channel state information and low training dimension density. Utilizing a complete 5G transceiver chain for Polar and LDPC coded transmissions paired with QPSK modulation, we analyze interleaved reference signals and data over a small number of OFDM symbols, preventing near-perfect channel estimation. Suited for mini-slot transmissions in ultra-reliable, low-latency communications, our evaluation covers up to SIMO and SU-MIMO transmission configurations over Rayleigh block fading and Line-Of-Sight channels. Results show that, with detection windows of about four modulated symbols, the proposed BICM metrics achieve detection performance that is close to that of a coherent receiver with perfect channel state information for both polar and LDPC coded configurations.

## An Advanced MIMO Multicarrier Framework for NTN-Based 5G Broadcast/Multicast Transmissions

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10591513
- **Type**: conference
- **Published**: 3-5 June 2
- **Authors**: Talha Faizur Rahman, Vuk Marojevic, Claudio Sacchi
- **PDF**: https://ieeexplore.ieee.org/document/10591513
- **Abstract**: Satellites are teaming up with 5G, forming a non-terrestrial network (NTN), to support broadband applications over wide coverage areas. However, low latency and high reliability are the challenges in NTN which is addressed through the use of low-earth orbit (LEO) satellites. High transmission efficiency can be accomplished by employing multiple-input multiple-output (MIMO) antenna systems and multicarrier wave-forms. Conventional multicarrier techniques, such as Orthogonal Frequency Division Multiplexing (OFDM) and its variants, are sensitive to the nonlinear distortion of high power amplifiers (HPAs) and high Doppler environments. Therefore, we consider Constant Envelope OFDM (CE-OFDM) assisted with Space-Time Shift Keying (STSK) and Low-Density Parity Check (LDPC) encoding for 5G broadcast/multicast systems based on LEO satellites working in the L-band. We propose a low complexity receiver based on A Posteriori Probability (APP) STSK decoding integrated with LDPC decoding, in which we derive the APP of LDPC coded bits for the STSK-CE-OFDM transmission. We analyze the computational complexity of the proposed receiver scheme and conclude that it is effective in counteracting HPA nonlinearity and high Doppler effects inherent to LEO satellites. Numerical results show that the proposed framework outper-forms conventional multicarrier techniques with a gain as high as 16 dB in the presence of amplifier nonlinearity.

## Research and Application Analysis of Turbo Code Decoding Algorithms

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10709190
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: Yue Zhao
- **PDF**: https://ieeexplore.ieee.org/document/10709190
- **Abstract**: This article embarks on an exhaustive exploration and in-depth analysis of Turbo code decoding algorithms, a crucial constituent in communication technology. The primary objective is to delve into the technical nitty-gritty, theoretical framework, and significant implications of Turbo codes, thereby emphasizing its centrality in modern communication systems. As a part of this analysis, the standard Turbo code decoding algorithm is meticulously scrutinized, followed by an examination of diverse optimization techniques. The study also comprises exhaustive performance assessments, encompassing aspects such as error rate performance and computational complexity. A careful evaluation of the strengths and limitations of these algorithms provides a balanced perspective on their practical efficacy. These decoding algorithms are then compared under various parameters to arrive at insightful conclusions about their relative performances. In addition, this work probes into the myriad applications of Turbo codes. Primarily, it examines their use in wireless communication systems, optical fiber communication systems, and more, shedding light on their versatility and indispensable role across numerous domains. The investigation touches upon how the strengths of Turbo codes are harnessed in these systems, while also discussing potential challenges in implementation.

## Online Evaluation of Communication Interference Effectiveness Based on CRITIC-AHP

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10696271
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: Wenjun Hou, Hu Jin, Chuang Peng
- **PDF**: https://ieeexplore.ieee.org/document/10696271
- **Abstract**: Aiming at the problem of online evaluation of the communication interference effect, an online evaluation method of the multi-attribute communication interference effect based on subjective and objective weights is proposed. In this paper, various communication behavior parameters are selected as interference effect evaluation indicators from the perspective of transmitter anti-jamming. The Criteria Importance Through Inter-criteria Correlation, CRITIC) and Analytic Hierarchy Process (AHP) determine the objective and subjective weights and combine the two to determine the final weights. The interference effect is judged according to the degree of change of each indicator parameter before and after the interference. At the same time, to objectively reflect the degree of parameter variation, the anti-jamming ability of the modulation style is numerically calculated. The experimental results show that the proposed method can effectively reflect the interference effect and still has stable performance in the case of small samples.

## Implementation of OFDM Using GNU Radio with HackRF One and RTL-SDR

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10625021
- **Type**: conference
- **Published**: 28-29 June
- **Authors**: Y Manasa, D Dharun, U Vamshi +1
- **PDF**: https://ieeexplore.ieee.org/document/10625021
- **Abstract**: Modern communication systems frequently employ orthogonal frequency division multiplexing (OFDM) as a modulation technology because of its capacity to reduce the impacts of inter-symbol interference and multipath fading. In this work, the implementation of OFDM using GNU Radio with the HackRF One software-defined radio (SDR) platform has been proposed. The work aims to demonstrate the practical implementation of OFDM, a complex digital communication technique, using readily available hardware and open-source software tools. GNU Radio provides a flexible and powerful framework for signal processing and modulation, while the HackRF One SDR offers the capability to transmit and receive RF signals over a wide frequency range. The implementation involves designing and configuring OFDM transmitter and receiver blocks within the GNU Radio environment, utilizing the HackRF One for RF signal transmission and RTL-SDR for reception. Various aspects such as synchronization, channel estimation, and error correction will be addressed to ensure reliable communication performance. The work not only serves as an educational resource for understanding OFDM principles and GNU Radio usage but also provides a practical platform for experimenting with SDR technology in real-world communication scenarios. OFDM (Orthogonal Frequency Division Multiplexing) signal transmission has been successfully implemented to accommodate three distinct types of input data: textual, audio, and image inputs and their corresponding waveforms and outputs have been obtained.

## Coding Solutions for Robust Performance in Wireless Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10724493
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: K. Sumathi, N. Selvanathan, G. Rajasekar
- **PDF**: https://ieeexplore.ieee.org/document/10724493
- **Abstract**: Wi-Fi structures require reliable coding solutions to ensure robust overall performance. Latest advances in wireless technologies have accelerated the want for reliable coding strategies to catch up on signal losses because of shadowing, fading, and imperfect channel situations. Traditional coding techniques, together with forward mistakes correction (FEC) and variety coding, conflict to hold strong performance underneath challenging conditions. New coding strategies are needed to ensure a reliable Wi-Fi communiqué in difficult propagation environments. Recent research in coding answers for robust wireless systems has explored a selection of methods, such as faster codes, Low-Density Parity-test (LDPC) codes, and area-time coding. LDPC codes offer extended code lengths, which boosts coding benefits and features quite low computational complexity. Area-time codes are a block coding method that improves blunder resilience by utilizing a couple of antennas and transmitting the identical sign in more than one direction simultaneously. These coding answers were implemented to provide improved overall performance in diverse Wi-Fi systems, which include cell, WLAN, and satellite TV for PC communiqué networks. Particularly, turbo codes, LDPC codes, and area-time codes have been used effectively in WLAN networks to reduce channel mistakes and growth records prices, in addition to in mobile networks to enhance spectral efficiency and offer better throughput.

## Comparative Analysis of Processing Latency and CPU Efficiency in FPGA-Based FEC Acceleration

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10588877
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Aerman Tuerxun, Akihiro Nakao
- **PDF**: https://ieeexplore.ieee.org/document/10588877
- **Abstract**: As Radio Access Networks (RANs) evolve towards more intelligent and software-defined paradigms, an increasing number of workloads are being offloaded to hardware accelerators. A significant challenge in this context is to minimize CPU consumption while ensuring low and stable latency in processing acceleration. Tailoring load allocation to meet varying latency requirements in different application scenarios is essential. In this paper, we present an application of RF Network on Chip (RFNoC) technology for FPGA-based acceleration of Low-Density Parity-Check (LDPC) code and Polar code. We conduct a comparative analysis of CPU and FPGA processing performance in OpenAinInterface (OAI) platform, with and without the Data Plane Development Kit (DPDK), to determine optimal load allocation for diverse data requirements. The findings indicate that RFNoC serves as an effective FPGA accelerator for the LDPC process, offering up to a fivefold increase in acceleration and significantly reducing processing delay jitter. Furthermore, the experimental outcomes provide a foundation for future research endeavors, specifically in the realm of efficient load optimization strategies.

## Secure Logistics Using Blockchain and Quantum Techniques

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10724489
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Ritesh Mohanty, K Anusha, N Manikandan +2
- **PDF**: https://ieeexplore.ieee.org/document/10724489
- **Abstract**: The COVID-19 pandemic has underscored the critical need for securing the vaccine supply chain to ensure its trustworthiness and reliability. This paper proposes a novel framework integrating blockchain technology (BCT) and quantum encryption to address the challenges of vaccine passport falsification, concerns over facility quality standards, and international recognition of vaccination documentation. Blockchain technology offers transparency and immutability, while quantum encryption provides enhanced security for storing sensitive user data such as passwords.Through qualitative content analysis of 126 cases across various industries, this study identifies the capabilities that blockchain-based supply chain systems empower and their performance outcomes. The analysis reveals a focus on capabilities related to operations, specific to information sharing and co-ordination, leading to outcomes such as quality compliance, process improvement, flexibility, cost reduction, and reduced process time.The integration of blockchain and quantum encryption in the proposed framework offers a multifaceted approach to addressing the challenges of vaccine supply chain security. Blockchain technology ensures transparency and immutability by creating an indelible record of transactions and events throughout the supply chain. This transparent ledger enhances trust among stakeholders, mitigating the risk of falsification and ensuring the integrity of vaccine passports and documentation.Furthermore, quantum encryption adds an additional layer of security by leveraging the principles of quantum mechanics to encrypt sensitive user data. Unlike traditional encryption methods, quantum encryption offers unconditional security, protecting user passwords and other confidential information from potential breaches and unauthorized access.The proposed framework combines blockchain technology and quantum encryption to enhance transparency, reliability, and trust in vaccine distribution. It addresses immediate challenges like those posed by COVID-19 while laying the groundwork for a resilient supply chain. The study contributes insights to supply chain management literature and offers a valuable tool for stakeholders. Yet, further empirical research is necessary to validate its effectiveness across industries and contexts, ensuring refinement and adaptability.

## Systematic Turbo-Polar, Turbo-LDPC-Polar and Turbo-LDPC Codes Based on Belief Propagation Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683047
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Rahim Umar, Atta ul Quddus, Yi Ma
- **PDF**: https://ieeexplore.ieee.org/document/10683047
- **Abstract**: In this paper, we propose the Turbo principle (of using parallel concatenated channel encoders separated by an interleaver and iterative soft-input and soft-output decoding between the constituent decoders) onto Polar and LDPC codes resulting in Turbo-Polar, Turbo-LDPC-Polar and Turbo-LDPC schemes with the aim of enhancing the BLER performance while also reducing the decoding complexity. All the proposed turbo-coded schemes are decoded using the traditional Belief Propagation (BP) algorithm based on low-density parity-check iterative decoding through a factor graph. Monte Carlo simulation results confirm the superiority of Turbo-LDPC and Turbo-LDPC-Polar schemes in BLER performance over state-of-the-art cyclic redundancy check-aided successive cancellation List decoding (CA-SCL) of Polar Codes with a large list size of 32 for large block lengths (larger than 3072 bits) while having reduced computational decoding complexity in comparison to CA-SCL decoding in an additive white Gaussian noise (A WGN) channel. Furthermore, Turbo-LDPC (based on 5G New Radio specifications for LDPC code) outperforms the standalone 5G-NR LDPC code and achieves about 1 dB gain at a BLER of 10–4 over correlated slow fading Rayleigh channel; however, being turbo-iterative in nature, it has higher complexity (about six-fold) than the standalone 5GNR LDPC code.

## Coding-Shaping Concatenation Scheme for Ultrashort Probabilistic Shaping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683085
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Yanan Luo, Qin Huang
- **PDF**: https://ieeexplore.ieee.org/document/10683085
- **Abstract**: It's challenging to design probabilistic shaping for ultra-reliable low-latency communications (URLLC), due to significant rate loss in ultrashort block-length regime. Unlike shaping-coding concatenation schemes as employed by probabilistic amplitude shaping (PAS), this paper proposes a coding-shaping concatenation (CSC) such that the rate loss is reduced by the coding rate, promising good performance. Moreover, because de-shaping is performed before decoding, to mitigate error propagation stemming from de-shaping, this paper proposes to use CCDM as shaping codes, and derives an efficient list de-mapping based on their weight constraint. It provides soft information for decoding with limited error propagation. Simulation and analysis results show that, with shaping block-length of 8, the proposed CSC achieves up to 1.1 dB shaping gain compared to uniform signaling with less average iterations.

## Joint Detection and Decoding for Helicopter Satellite Communication System with LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683487
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Wei Bao, Jiangtao Wang, Yongchao Wang
- **PDF**: https://ieeexplore.ieee.org/document/10683487
- **Abstract**: In this paper, we propose a joint detection and decoding method for a helicopter satellite communication system with low-density parity-check codes, in response to the problem that the signals are periodically occluded by the helicopter rotor blades. First, we introduce a finite-state Markov model to describe the occlusion channel. Second, we design a joint detection and decoding method based on this model. Specifically, a posteriori probability of each symbol based on the occlusion detection is calculated, which is exploited to complete the decoding procedure. In the end, we test the performance of the proposed method under the simulated rotor occlusion channel, and the simulation results show that the proposed method can achieve excellent bit error rate performance in the rotor occlusion channel.

## Low-Complexity Decoder of Analog Fountain Codes for Industrial Internet of Things

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683654
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Ke Zhang, Ye Wang, Jian Jiao +2
- **PDF**: https://ieeexplore.ieee.org/document/10683654
- **Abstract**: In this paper, towards the ultra-reliable low-latency requirements of industrial Internet of Things (IIoT), we design a low decoding complexity ordered statistic decoder (OSD) for short analog fountain codes (S-AFCs). We first propose a concatenated decoder named soft-OSD (S-OSD) for S-AFCs, where the S-AFCs are concatenated with LDPC codes. Then, we analyze the log-likelihood ratio (LLR) output of inner decoder via the density evolution (DE), the DE results provide the theoretical guidelines to design the discarding criterion (DC) of test error patterns (TEPs) and stopping criterion (SC) to lower the complexity of S-OSD. Simulation results show that the S-OSD can achieve the same error performance with existing decoding algorithms for S-AFCs, and the complexity of S-OSD is greatly decreased, in terms of the average re-encoding number of OSD and operations number per information bit.

## Hybrid Shaping for Bit-Interleaved Coded Modulation with Iterative Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683676
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Jiayi Yang, Qianfan Wang, Congduan Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10683676
- **Abstract**: In this paper, we integrate the 5G low-density parity-check (LDPC) coded modulation systems with hybrid shaping, where the centroid-based geometric shaping is implemented to remedy the performance loss of the many-to-one probabilistic shaping. Taking into account the fact that the 5G parity-check matrices have an uneven density in different parts, we elaborately design a simple row-column interleaver for the bit-interleaved coded modulation with iterative decoding (BICM-ID) system to allocate the ambiguous bits caused by the many-to-one mapping to the sparser parity part, resulting in the hybrid shaping for BICM-ID (HS-BICM-ID) system. Numerical results have shown that the HS-BICM-ID can obtain shaping gains of about 0.5 dB and 1.4 dB compared to the constant composition distribution matching (CCDM) shaping and the geometric shaping, respectively, while it can obtain a shaping gain of about 1.7 dB compared to the scheme with uniform input. Our work has also shown that, at low and moderate spectral efficiency, the presented hybrid shaping can achieve a significant shaping gain and effectively remedy the performance loss of dyadic many-to-one probabilistic shaping.

## An Adaptive Coded Caching Scheme for Time-Varying Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683348
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Mirna HAIDAR, Yasser FADLALLAH, Zeinab KASSIR +2
- **PDF**: https://ieeexplore.ieee.org/document/10683348
- **Abstract**: New technologies that incorporate affordable storage at the edge, such as caching, are anticipated to facilitate the growth of wireless communication and accommodate increased traffic. In this paper, we address the challenge of adapting the original coded caching scheme to time-varying channels through a low-complexity approach. The approach categorizes graph nodes into two groups: those requiring modifications and those that remain unchanged. When a user's code rate increases, a merge process is applied to the associated graph vertices, while a split process is implemented for users with a decreased code rate. Subsequently, the graph is adaptively colored to facilitate continuous transmission. The efficacy and performance of the proposed scheme are demonstrated through simulation results.

## Link-Level Performance Analysis of DVB Standards in Ultra-Dense LEO Satellite-Terrestrial Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683179
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Xin Zhang, Yilei Wang, Xiaohan Qin +3
- **PDF**: https://ieeexplore.ieee.org/document/10683179
- **Abstract**: Ultra-dense low earth orbit (LEO) satellite terrestrial networks (ULSNs) are considered as a crucial component of future six generation (6G) networks, offering ubiquitous and massive services for various applications. However, for the development of advanced physical layer technologies for ULSNs, a comprehensive link-level simulation tool that integrates up-to-date satellite communication protocols becomes paramount and is urgently needed. In this paper, we develop a versatile simulator for the link-level performance analysis of ULSNs under the prevalent digital video broadcasting (DVB) standards. We first establish a complete satellite-terrestrial microwave channel model, taking practical factors such as rain attenuation, cloud attenuation, and Doppler frequency shift into consideration. Subsequently, the whole physical layer modules tailored for satellite-terrestrial microwave communication are implemented, including diverse physical layer modulation and coding schemes (MCSs). Furthermore, we realize adaptive coding and modulation (ACM) for adaptive channel performance simulation. Finally, comparative performance analysis using the established channel model is conducted to demonstrate the effectiveness of different MCSs of DVB standards. The complete link-level performance analysis based on our self-developed simulator can advance the field of satellite-terrestrial microwave communication and provide valuable insights for further exploration of ULSNs.

## Age of Collection with Network-Coded Multiple Access: An Experimental Study

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683581
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Yurong Lai, Hai Liu, Tse-Tin Chan +2
- **PDF**: https://ieeexplore.ieee.org/document/10683581
- **Abstract**: This paper studies information freshness in collaborative surveillance scenarios operated with non-orthogonal multiple access (NOMA), where each monitoring device observes a portion of a common target and reports its latest status on the target to a common access point (AP) to recover the complete observation. We use age of collection (AoC) as a metric of information freshness. Unlike the conventional age of information (AoI) metric, the instantaneous AoC decreases only when the AP receives all partial updates from different devices (i.e., successfully receives a “joint” update). Conventional NOMA schemes typically use multiuser decoding (MUD) techniques to decode update messages from different devices. However, MUD does not work well when the signal-to-noise ratios (SNRs) of different NOMA users are (nearly) balanced. Therefore, we consider network-coded multiple access (NCMA), an advanced NOMA scheme that integrates MUD with physical-layer network coding (PNC). PNC is a technique that turns wireless interferences into useful network-coded information, which works well even when the SNRs of different users do not differ much. Experimental results on software-defined radios indicate that NCMA is a practical solution for achieving low average AoC under different channel conditions. This is the first study to show that NCMA, thanks to the combination of MUD and PNC, can receive joint update messages in a shorter period of time, thus significantly reducing the average AoC of the system.

## On the Implementation of Neural Network-based OFDM Receivers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683574
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Moritz Benedikt Fischer, Sebastian Dörner, Takayuki Shimizu +3
- **PDF**: https://ieeexplore.ieee.org/document/10683574
- **Abstract**: Neural network (NN)-based receivers for orthogonal frequency division multiplex (OFDM) excel through promising performance and benefits in their applicability. In this paper we analyze their capabilities when they are imposed with practical constraints that have to be considered when implementing such a receiver on hardware. Specifically, we focus on the effects of uniform linear affine quantization and it is shown which performance can be achieved by utilizing quantization-aware training (QAT) with trainable quantizers. In order to reduce the computational complexity of the NN-based receiver different pruning methods are investigated. We showcase that a reduction of the number of floating-point operations (FLOPs) by more than 50% is possible at the cost of less than 0.25 dB difference. Finally, an intuition on joint pruning and quantization is given.

## An Efficient Resource Block Scheduling Based Anti-Jamming Method for Securing Next-Generation Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10646325
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Cem Örnek, Mesut Kartal
- **PDF**: https://ieeexplore.ieee.org/document/10646325
- **Abstract**: This study introduces a robust anti-jamming method in response to the escalating threat of jamming attacks on next- generation communication systems. As contemporary communication systems undertake increasingly critical tasks, safeguarding them against jamming attacks becomes paramount. The proposed methodology initially involves identifying the Radio Blocks (RBs) affected by jamming attacks through Error Vector Magnitude (EVM) vs. RB measurement. Because the RBs represent the frequency domain, this measurement reveals the specific frequencies targeted by the jammer. Subsequently, an RB sharing strategy is proposed that effectively distributes clean and jammed RBs to user equipment (UEs). The strategy prioritizes protecting UEs closest to the jammer by allocating clean RBs and isolating their signals from jammer interference in the frequency domain. Acknowledging the value of RB resources, this research also endeavors to assess jammed RBs, allocating them to UEs farthest from the jammer or, if unfeasible, reducing the data rate to enhance resilience against jamming attacks. The contributions of this study include achieving low-complexity decision making without the need for training, which is particularly advantageous given the low-latency requirements of next-generation communication systems. Furthermore, the proposed approach seamlessly integrates with the existing system architecture by leveraging IQ data obtained from the natural system flow for the necessary EVM measurement. Emphasizing the precious nature of RB resources, this study aims to optimize their utilization, avoid discarding jammed RBs, and explore ways to leverage them efficiently. The simulation results demonstrate that our methodology maintains maximum UE efficiency, even during jamming attacks.

## MMSE-Aided Unitary Approximate Message Passing Detection for MIMO-OTFS System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683591
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Xuanyun Ma, Jin Xu, Chao Dong +2
- **PDF**: https://ieeexplore.ieee.org/document/10683591
- **Abstract**: The multiple-input multiple-output orthogonal time frequency space (MIMO-OTFS) has emerged as a promising scheme for high-mobility wireless communications. The unitary approximate message passing (UAMP) detection has demonstrated outstanding performance in the single-input single-output (SISO)-OTFS system. However, We found that directly employing the UAMP detection for the MIMO-OTFS system results in performance degradation and the emergence of an error floor. Therefore, we propose a minimum mean square error (MMSE)-aided UAMP scheme, incorporating MMSE to assist UAMP by providing the prior information. Notably, we reduce the complexity by setting a signal-to-noise ratio (SNR) threshold, only when SNR exceeds the threshold shall we start the MMSE-aided mechanism. Simultaneously, we analyze the impact of fractional delay and consider it into system model, aiming to optimize the practicality of the system. Simulation results under fast-fading Rayleigh channels demonstrate that the proposed MMSE-aided UAMP significantly outperforms the original UAMP in the medium to high SNR range.

## Implementation of NavIC Ll Transmitter and Receiver

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683652
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Satheesh Kumar Simhachalam, Ahmed Hamdan, Madhu Addanki +2
- **PDF**: https://ieeexplore.ieee.org/document/10683652
- **Abstract**: This paper introduces a softwIare based transmitter and receiver architecture for Navigation through Indian Constellation (NavIC) L1 Standard Positioning Service (SPS) signal used for civilian purposes. Details of the signal characteristics, various signal processing blocks of both transmitter and receiver as well as channel modeling are available in this work. The receiver performance is verified through simulations by gener-ating random navigation data at transmitter and recovering it using the architecture proposed in the paper. This work will enable the community to take up further research in building new algorithms for NavIC Ll signals.

## Receiver Designs for SC-SCMA Systems Over Frequency Selective Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10683053
- **Type**: conference
- **Published**: 24-27 June
- **Authors**: Tianzhu Qin, Ziyi Yang, Jia'ao Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/10683053
- **Abstract**: Sparse code multiple access (SCMA) is a candidate technology for further wireless communication system to enhance the multiple access capacity. The existing multi carriers technique based SCMA schemes, such as orthogonal frequency division multiplexing (OFDM), have been well studied and considered as a promising candidate for future 6G protocols. However, the high peak-to-average power ratio (PAPR) issue resulted by the multi carriers techniques limits the applications of SCMA in long distance transmission scenarios and low cost sensor networks. To address this issue, single carrier based SCMA transmission scheme (SC-SCMA) has been proposed and demonstrates low PAPR. But the multi user signal detection is still a major chal-lenge for SC-SCMA, especially for frequency selective channels (FSC). In this paper, we establish the interference model of SC-SCMA system in FSC, and construct an extended factor graph (EFG) for multi user detection. Afterward, the Gaussian approx-imate interference based belief propagation algorithm processing on EFG (E-GAIBP) is proposed, realizing efficient detection and complexity reduction. Furthermore, to earn higher performance gain, joint E-GAIBP detection and LDPC decoding scheme (E-GAIBP-JDD) is introduced. Numerical results demonstrate that compared with classical MPA using EFG, E-GAIBP shows great complexity reduction and E-GAIBP-JDD performs great performance gain.

## SymPhase: Phase Symbolization for Fast Simulation of Stabilizer Circuits

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11294801
- **Type**: conference
- **Published**: 23-27 June
- **Authors**: Wang Fang, Mingsheng Ying
- **PDF**: https://ieeexplore.ieee.org/document/11294801
- **Abstract**: This paper proposes an efficient stabilizer circuit simulation algorithm that only traverses the circuit forward once. We introduce phase symbolization into stabilizer generators, which allows possible Pauli faults in the circuit to be accumulated explicitly as symbolic expressions in the phases of stabilizer generators. This way, the measurement outcomes are also symbolic expressions, and we can sample them by substituting the symbolic variables with concrete values, without traversing the circuit repeatedly. We show how to integrate symbolic phases into the stabilizer tableau and maintain them efficiently using bit-vector encoding. A new data layout of the stabilizer tableau in memory is proposed, which improves the performance of our algorithm (and other stabilizer simulation algorithms based on the stabilizer tableau). We implement our algorithm and data layout in a Julia package named SymPhase.jl, and compare it with Stim, the state-of-the-art simulator, on several benchmarks. We show that SymPhase.jl has superior performance in terms of sampling time, which is crucial for generating a large number of samples for further analysis.

## Enhanced Layered Quasi-Cyclic Low-Density Parity-Check Codes for the McEliece Cryptosystem in Satellite Communications System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10803377
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Junda Zhang, Ge Zhang, Zhigang Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10803377
- **Abstract**: Given the rapid advancement of quantum computing technology, the McEliece cryptosystem, rooted in coding theory, stands out as one of the few cryptographic systems resilient against quantum attacks. Nevertheless, the system's extensive public key length and low transmission rate have hindered its practical utility. To overcome these challenges, we propose a methodology to implement the McEliece cryptosystem employing quasi-cyclic low-density parity-check (QC-LDPC) codes, thereby diminishing the public key size albeit at the expense of height-ened decryption complexity. Furthermore, we introduce a row-layered normalized min-sum low-density parity-check decoding algorithm aimed at minimizing system complexity and optimizing hardware resource utilization.

## Novel LDPC Code-Aided Modified CME-Based Anti-Jamming Strategy

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10803411
- **Type**: conference
- **Published**: 21-23 June
- **Authors**: Yuan Chai, Jiawen Chen, Xuhui Ding +1
- **PDF**: https://ieeexplore.ieee.org/document/10803411
- **Abstract**: Direct sequence spread spectrum (DSSS) system is extensively utilized in modern satellite communication systems owing to its inherent anti-interception and anti-jamming capabilities. However, the anti-jamming performance of the system is constrained by its spreading ration. While a larger spreading ration increases the jamming margin, it also leads to an expansion in signal bandwidth, thereby resulting in reduced communication efficiency and wastage of spectrum resources. The consecutive mean excision (CME) algorithm shows the potential to enhance the system's resistance to jamming for a fixed spreading ratio. Nonetheless, it is limited in effectively addressing residual burst errors in the channel. In this paper, an LDPC code-aided anti-jamming strategy based on modified CME is proposed. By introducing overlap windowing and overlap addition operations, the CME algorithm is optimized to achieve jamming detection and suppression in the frequency domain. Moreover, the logarithmic likelihood ratio (LLR) of the despread signal is modified, along with decoding based on the belief propagation (BP) algorithm to further improve the error-correcting capability of the DSSS system. Simulation results compared with the traditional algorithm demonstrate that the proposed method has significantly improved communication performance against narrowband jamming.

## Network Vulnerability Analysis via Quantum Computing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11062742
- **Type**: conference
- **Published**: 20-23 June
- **Authors**: Andrew P. Kennedy, Thang N. Dinh, My T. Thai
- **PDF**: https://ieeexplore.ieee.org/document/11062742
- **Abstract**: In many complex networking systems, identifying critical nodes whose removal maximally disrupts network connectivity remains an important yet computationally challenging problem for network vulnerability analysis. Finding near-optimal solutions is known to be NP-hard. In this paper, we explore the potential of near-term quantum computing devices to efficiently solve the k-Critical Node Detection (k-CND) problem. We formulate the problem as a quadratic unconstrained binary optimization (QUBO), a mathematical optimization over binary variables amenable to solution on quantum annealers. We present a novel integer linear programming (ILP) formulation and its conversion into QUBOs and provide benchmarking results on D-Wave's quantum annealers. Our theoretical analysis proves that our proposed formulation, ILP2, generates substantially smaller QUBO than the state-of-the-art ILP1 formulation. Experimentally, our efficient QUBO yields a 59.7% decrease in QUBO variables on a graph with 10 vertices and 40 edges, and an 11.7% reduction in qubits on a 15-vertex, 22-edge graph compared to that of QUBO1. We analyze the solution quality and running time across quantum, classical, and hybrid solvers to assess the potential for quantum advantage. Our work showcases the promise and challenges of tackling this important graph problem on near-term quantum hardware.

## SEECAD: Semantic End-to-End Communication for Autonomous Driving

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10588546
- **Type**: conference
- **Published**: 2-5 June 2
- **Authors**: Soheyb Ribouh, Abdenour Hadid
- **PDF**: https://ieeexplore.ieee.org/document/10588546
- **Abstract**: Semantic communication is a key paradigm in future 6G systems, designed to revolutionize the physical layer of traditional communication, in order to enhance efficiency of data transmission. Fueled by advancements in deep learning architectures, image processing has made significant strides in segmentation and scenes analysis for autonomous vehicles (AVs). Motivated by these advancements, we present an innovative outlook on communication systems, by leveraging semantic data. Thus, we introduce a novel semantic end-to-end communication system, named SEECAD, specifically designed for image transmission in autonomous driving environments. SEECAD is based on a theoretical model, aligning with the semantic level concepts and leveraging a shared knowledge base to efficiently transmit meaningful image data. The semantic encoder and decoder of SEECAD are built upon deep learning architecture, empowered by Low-Density Parity-Check (LDPC) codes. This integration serves to minimize semantic error transmission and enhance the segmentation accuracy at the receiver. Our proposed semantic communication approach was extensively evaluated in various wireless image transmission scenarios over an AWGN channel, using different QAM modulations (4QAM and 16QAM). Our experimental results demonstrated that the proposed SEECAD achieves accurate and effective image transmission in noisy environments.

## Adaptive LDPC Decoder with Performance Prediction Based on Average Mutual Information

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10608331
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Xia An, Chao Zhang, Kewu Peng +2
- **PDF**: https://ieeexplore.ieee.org/document/10608331
- **Abstract**: In mobile reception scenario, the channel quality usually shows some fluctuation, while traditional low-density parity-check (LDPC) decoders which utilize fixed decoding algorithms have difficulties to balance the decoding complexity and threshold performance under different channel quality. Adaptive LDPC decoder needs performance prediction in order to guide the selection of decoding options. Traditional performance prediction based on signal-to-noise ratio and channel state information is not precise enough to help the selection of decoding options due to the rapidly varying instant channel state information or incorrect channel-parameter estimation. In this paper, we propose a novel adaptive LDPC decoder with bit-wise average mutual information (AMI) based performance prediction, which could switch between multiple decoding options according to the performance prediction results obtained from the computed AMI and the pre-determined AMI-performance relationship. The proposed decoder adopts multiple candidate decoding algorithms with distinct decoding complexity and threshold performance, and includes the option of direct retransmission. Thus, it could enhance the adaptability of the decoder to the varying channel quality, the robustness to the channel-parameter estimation error, and meanwhile cut down the computing resource waste caused by the avoidable decoding failure. We further propose a novel loop correction method which could effectively correct the channelparameter estimation error by using the decoder output to adjust the decoder input.

## Performance Evaluation of 5G Broadcast and ATSC 3.0 for Cellular Broadcasting Scenarios

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10608271
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Sung-Ik Park, Seok-Ki Ahn, Soyoung Han +3
- **PDF**: https://ieeexplore.ieee.org/document/10608271
- **Abstract**: This paper provides performance evaluation results of two broadcasting technologies from different origin, that is, 5G Broadcast and ATSC 3.0 as cellular broadcasting solutions. Their physical-layer capabilities are evaluated through theoretical point of view and block error rate (BLER) performance. The evaluation results demonstrate that the performance of 5G Broadcast has improved with efficient NR RAN compared to LTE-RAN based solutions. Meanwhile, ATSC 3.0 outperforms 5G Broadcast in cellular broadcasting scenarios, attributed to the utilization of a time interleaver and well-designed bit interleaved coded modulation (BICM).

## Improving Cooperative Wi-Fi Broadcast with Fine-Grained Channel Estimation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10682925
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Lizhao You, Shuoling Liu, Wenjun Xie +3
- **PDF**: https://ieeexplore.ieee.org/document/10682925
- **Abstract**: Cooperative broadcast is an efficient approach to improve Wi-Fi broadcast performance in a crowded scenario with densely deployed access points (APs). However, the current concurrent transmission MAC protocols cannot synchronize multi-APs’ signals perfectly for all users. As a result, the superimposed signal from APs is time-varying at the users due to the multiple time-domain channels and carrier frequency offsets (CFOs) from multiple APs. The traditional channel estimation approach that estimates the superimposed channel as a whole is ill-suited for the superimposed signal. In this paper, we propose a fine-grained channel estimation approach to first estimate these channel parameters for each AP, and then reconstruct the superimposed channel. Specifically, we present a two-stage channel estimation algorithm that first estimates the CFOs by discretizing the CFO range and matching the most possible CFOs, and then computes the time-domain channels. Experiment and simulation results show the new channel estimation approach achieves much lower bit error rate (BER) and packet error rate (PER) than the traditional IEEE 802.11 approach. In addition, we propose a distributed mechanism to choose the master AP that initializes multi-APs’ simultaneous transmission, which the current concurrent transmission MAC protocols lack. Network-layer simulation results show that the proposed cooperative broadcast scheme improves the throughput by 64% to 82% compared with the traditional uncooperative broadcast scheme.

## Test Automation of the Physical Layer of TV 3.0

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10608290
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Daniel Pedroso Neri, Fadi Jerji, Cristiano Akamine
- **PDF**: https://ieeexplore.ieee.org/document/10608290
- **Abstract**: This paper presents the automation of testing Brazil’s Digital Terrestrial Television Broadcasting (DTTB) standards physical layers as part of the TV 3.0 project, the discussion centers on leveraging automation tools to enhance efficiency. Specifically, it explores the implementation of automated testing protocols in Advanced Television Systems Committee 3.0 (ATSC 3.0) and Advanced Integrated Services Digital Broadcasting-Terrestrial (Advanced ISDB-T), during Phase 3 tests of the next generation of Brazil’s DTTB system and how this automation helped to improve the tests efficiency and accuracy.

## In-Band Full-Duplex Communications with MIMO in ATSC 3.0

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10608255
- **Type**: conference
- **Published**: 19-21 June
- **Authors**: Zhihong Hunter Hong, Wei Li, Liang Zhang +7
- **PDF**: https://ieeexplore.ieee.org/document/10608255
- **Abstract**: Wireless in-band backhaul, i.e. in-band distribution links (IDL) and inter-tower communications networks (ITCN) were previously proposed as key enabling technologies for the next-generation digital broadcasting systems, a.k.a. the Advanced Television Systems Committee (ATSC) 3.0 system. Both ITCN/IDL can be operated in the spectrum-efficient in-band full-duplex (IBFD) mode and the same frequency band is shared between the broadcast service signal and the ITCN/IDL signals. Integrating multi-input multi-output (MIMO) into ITCN/IDL transmission is desirable to increase the throughput and reduce the portion of the spectrum occupied by ITCN/IDL. Self-interference cancellation (SIC) in IBFD communications with the dual-polarization MIMO in ATSC 3.0 is investigated in this paper. A MIMO SIC was previously proposed by the authors which is capable to cancel both the co-polarization and cross-polarization self-interferences without requiring a dedicated training phase for the SIC filter weight estimation. Foregoing a dedicated training phase is more spectrum efficient and flexible in system design, however, it results in the presence of the remote signal of interest as an “intrinsic noise” in the SIC filter weight estimation. An iterative “intrinsic noise” cancellation scheme is proposed in this paper to further improve the MIMO SIC performance.

## Trainable Pre-Processing Approach for Efficient Neural Network-based 4K-QAM Soft Demodulator

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10674131
- **Type**: conference
- **Published**: 14-16 June
- **Authors**: Donlaporn Triamwichanon, Patinya Muangkammuen, Puripong Suthisopapan
- **PDF**: https://ieeexplore.ieee.org/document/10674131
- **Abstract**: The practicality of the densely packed and through-put boosting modulation scheme, 4K-QAM, is obstructed by its ultra-high complexity soft demodulator that is essential for generating log-likelihood ratios (LLR) as an input for modern error correction decoders. A preprocessing technique that facilitates efficient training for neural network-based 4K-QAM soft demodulator, which inherently possesses very low computational complexity, is proposed in this paper. The results clearly demonstrate that such an alternative 4K-QAM demodulation can achieve an identical bit error rate (BER) performance with substantial computation complexity reduction compared with the conventional optimal soft demodulator.
