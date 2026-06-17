# IEEE Xplore — 2021-05


## A Rate Scalable Construction of Non-Homogeneous Quantum LDPC Codes of CSS Type Based on Balanced Incomplete Block Design

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9328225
- **Type**: journal
- **Published**: May 2021
- **Authors**: Yun-Jiang Wang, Zhuo-Yan Xiao, Xing-Yu Xiong +3
- **PDF**: https://ieeexplore.ieee.org/document/9328225
- **Abstract**: Balanced incomplete block design (BIBD) offers an important way to construct non-homogeneous quantum low-density-parity-check (LDPC) codes of Calderbank-Shor-Steane (CSS) type. However, the rates of the quantum codes based on this method are limited to be 1-2/m approximately, where m, the number of base blocks chosen from the associated BIBD, is even. We overcome this limitation by providing a rate scalable way to construct non-homogeneous quantum LDPC codes of CSS type. With our method, the rates of the resultant quantum codes are 1-2/m', where m'=m/e and e ∈ {1, 2}. Note that here m' can be odd. Thus, we double the rate range of the codes yielded from the existing strategies. Moreover, one can switch codes between the two rates flexibly adapting to various application scenarios.

## On Nested Property of Root-LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9336043
- **Type**: journal
- **Published**: May 2021
- **Authors**: Lorenzo Ortega, Charly Poulliat
- **PDF**: https://ieeexplore.ieee.org/document/9336043
- **Abstract**: We investigate on binary Protograph Root-LDPC codes that can embed an interesting property, called nested property. This property refers to the ability for a coding scheme to achieve full diversity and equal coding gain for any number of received coded blocks and for any configuration of the received code blocks. One can take advantage of this property for “carousel”-type transmissions broadcasting cyclically coded information. For regular Root-LDPC codes, we show that these codes inherently have both properties over the nonergodic block fading channel and when message passing decoding is used. Then, we show that irregular Root-LDPC structures could not provide equal coding gain except if explicit design rules are enforced to ensure that the nested property is fulfilled when designing irregular Root-LDPC codes. Simulation results show that designed nested Root-LDPC codes achieve good performance and full diversity for coding rates R = 1/2, R = 1/3 and R = 1/4.

## High-Speed LDPC Decoders Towards 1 Tb/s

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9378807
- **Type**: journal
- **Published**: May 2021
- **Authors**: Meng Li, Veerle Derudder, Kaoutar Bertrand +2
- **PDF**: https://ieeexplore.ieee.org/document/9378807
- **Abstract**: Beyond 5G systems are expected to approach 1 Tb/s throughput. This poses a significant challenge to the channel decoder. In this paper, we propose a multi-core architecture based on full row parallel layered LDPC decoder with frame interleaving. Compared with conventional partially parallel layered architectures, the proposed architecture increases the throughput by applying frame interleaving into the pipeline architecture and by using multi-core architectures. Two high rate medium size QC LDPC codes are designed with fast decoding convergence speed for this architecture. Both codes are implemented with single core and multi-core architectures to explore different trade-offs between code design, communication performance and implementation. The four decoders are implemented in 16 nm CMOS FinFET technology with a clock rate of 1 GHz. The placement and routing implementation results show that the single core decoder for the LDPC (1027, 856) code is able to provide 114 Gb/s throughput at maximum 3 iterations with an area of 0.173 mm2 and energy efficiency of 1.56 pJ/bit; the multi-core decoder for the (1032, 860) code is able to provide 860 Gb/s throughput at maximum 2 iterations with an area of 1.48 mm2 and energy efficiency of 3.24 pJ/bit. The multi-core decoder achieves the highest throughput in the literature for medium size (1-2k) LDPC codes. When compared with other state-of-the-art fully parallel high speed architectures, the proposed architectures bring a significant gain both in area efficiency and energy efficiency while keeping the ability to offer flexibility in code rate, number of iterations and early stop.

## Quasi-Cyclic LDPC Codes With Parity-Check Matrices of Column Weight Two or More for Correcting Phased Bursts of Erasures

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9353574
- **Type**: journal
- **Published**: May 2021
- **Authors**: Xin Xiao, Bane Vasić, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/9353574
- **Abstract**: In his pioneering work on LDPC codes, Gallager dismissed codes with parity-check matrices of weight two after proving that their minimum Hamming distances grow at most logarithmically with their code lengths. In spite of their poor minimum Hamming distances, it is shown that quasi-cyclic LDPC codes with parity-check matrices of column weight two have good capability to correct phased bursts of erasures which may not be surpassed by using quasi-cyclic LDPC codes with parity-check matrices of column weight three or more. By modifying the parity-check matrices of column weight two and globally coupling them, the erasure correcting capability can be further enhanced. Quasi-cyclic LDPC codes with parity-check matrices of column weight three or more that can correct phased bursts of erasures and perform well over the AWGN channel are also considered. Examples of such codes based on Reed-Solomon and Gabidulin codes are presented.

## Error Floor Estimation of LDPC Coded Modulation Systems Using Importance Sampling

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9349511
- **Type**: journal
- **Published**: May 2021
- **Authors**: Peyman Neshaastegaran, Amir H. Banihashemi, Ramy H. Gohary
- **PDF**: https://ieeexplore.ieee.org/document/9349511
- **Abstract**: One of the key weaknesses of low-density parity-check (LDPC) codes is the error floor that they typically exhibit at high signal-to-noise ratios (SNRs). Such an error floor is usually attributed to problematic structures known as trapping sets (TSs). The overwhelming majority of existing error floor estimation schemes consider the case of binary phase shift keying (BPSK) signalling. Unfortunately, these schemes are not readily extensible to estimate the error floor of high order LDPC coded modulation systems considered herein. To provide such a scheme, in this work, we use mean-shift importance sampling (MS-IS) to develop a novel error floor estimation methodology for high-order pulse amplitude modulation (PAM) and quadrature amplitude modulation (QAM) LDPC coded systems. First, a computationally efficient graphical-based approach is used to identify the TSs of a given LDPC code. Subsequently, a novel analytical approach is devised to identify the TSs that are likely to have a higher contribution in the error floor. These TSs are referred to as potentially dominant TSs (PDTSs). Finally, a new methodology for categorizing the PDTSs into equivalence classes is developed. A representative PDTS of each equivalence class is chosen and an MS-IS framework is devised to obtain the error rate corresponding to each equivalence class. To arrive at the desired MS-IS scheme, we develop an algorithm that invokes the geometry of the constellation to determine the MS value. In contrast with the conventional MS-IS method used in BPSK signalling, in the proposed MS-IS scheme, the MS value is a variable that is determined based on the TS and the transmitted codeword. The computational complexity of the three main steps of our methodology, viz. extracting the PDTSs, determining the MS values, and applying the MS-IS scheme, depends merely on the size of the constellation and the structure of the code, but not on the SNR. Numerical simulations confirm the efficacy and accuracy of the proposed technique at different SNRs.

## Spatially Coupled LDPC Codes With Sub-Block Locality

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9354799
- **Type**: journal
- **Published**: May 2021
- **Authors**: Eshed Ram, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/9354799
- **Abstract**: A new type of spatially coupled low-density parity-check (SC-LDPC) codes motivated by practical storage applications is presented. SC-LDPCL codes (suffix `L' stands for locality) can be decoded locally at the level of sub-blocks that are much smaller than the full code block, thus offering flexible access to the coded information alongside the strong reliability of the global full-block decoding. Toward that, we propose constructions of SC-LDPCL codes that allow controlling the trade-off between local and global correction performance. In addition to local and global decoding, the paper develops a density-evolution analysis for a decoding mode we call semi-global decoding, in which the decoder has access to the requested sub-block plus a prescribed number of sub-blocks around it. SC-LDPCL codes are also studied under a channel model with variability across sub-blocks, for which decoding-performance lower bounds are derived.

## Bit-Plane Coding in Extractable Source Coding: Optimality, Modeling, and Application to 360° Data

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9319718
- **Type**: journal
- **Published**: May 2021
- **Authors**: Fangping Ye, Navid Mahmoudian Bidgoli, Elsa Dupraz +3
- **PDF**: https://ieeexplore.ieee.org/document/9319718
- **Abstract**: In extractable source coding, multiple correlated sources are jointly compressed but can be individually accessed in the compressed domain. Performance is measured in terms of storage and transmission rates. This problem has multiple applications in interactive video compression such as Free Viewpoint Television or navigation in 360° videos. In this letter, we analyze and improve a practical coding scheme. We consider a binarized coding scheme, which insures a low decoding complexity. First, we show that binarization does not impact the transmission rate but only slightly the storage with respect to a symbol based approach. Second, we propose a Q-ary symmetric model to represent the pairwise joint distribution of the sources instead of the widely used Laplacian model. Third, we introduce a novel pre-estimation strategy, which allows to infer the symbols of some bit planes without any additional data and therefore permits to reduce the storage and transmission rates. In the context of 360° images, the proposed scheme allows to save 14% and 34% bitrate in storage and transmission rates respectively.

## Deep-Learning-Based Blind Recognition of Channel Code Parameters Over Candidate Sets Under AWGN and Multi-Path Fading Conditions

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9344644
- **Type**: journal
- **Published**: May 2021
- **Authors**: Sepehr Dehdashtian, Matin Hashemi, Saber Salehkaleybar
- **PDF**: https://ieeexplore.ieee.org/document/9344644
- **Abstract**: We consider the problem of recovering channel code parameters over a candidate set by merely analyzing the received encoded signals. We propose a deep learning-based solution that I) is capable of identifying the channel code parameters for several coding scheme (such as LDPC, Convolutional, Turbo, and Polar codes), II) is robust against channel impairments like multi-path fading, III) does not require any previous knowledge or estimation of channel state or signal-to-noise ratio (SNR), and IV) outperforms related works in terms of probability of detecting the correct code parameters.

## Coding of Multi-Source Information Streams With Age of Information Requirements

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9374436
- **Type**: journal
- **Published**: May 2021
- **Authors**: Haoyuan Pan, Soung Chang Liew, Jiaxin Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/9374436
- **Abstract**: This article puts forth a new channel coding paradigm for multi-source information streams with Age of Information (AoI) requirements. The recently introduced AoI metric characterizes the freshness of information, defined as the time elapsed since the generation of the last successfully received update. We study a setup in which a large number of sensors want to send update information to a common monitor with the help of aggregators. Specifically, an aggregator collects update packets from sensors and forwards them to the monitor. Conventional block codes (such as LDPC codes) that encode and decode each update packet separately do not perform well in such an information aggregation and update scenario. When update packets suffer from packet loss, we show that block codes lead to high instantaneous AoI because a sensor waits for a long time for the next update opportunity. This article investigates stream-based codes to tackle this problem. A distinguishing feature of stream-based codes is the joint encoding of update packets from different sensors, and a series of coded packets are sent continuously like a stream. Different update packets are then jointly decoded using multiple coded packets from the stream. A key challenge with AoI requirements is the joint design of error corrections of old packets and fast decodings of new packets. We design a practical encoding-decoding scheme and a sliding decoding window mechanism to control the decoding complexity. We evaluate two AoI metrics, average AoI and bounded AoI. In particular, bounded AoI corresponds to an AoI threshold that the instantaneous AoI is below a large percentage of the time. Experimental results on software-defined radio show that stream-based codes significantly outperform block codes in both average AoI and bounded AoI under varying channel conditions. Overall, stream-based codes provide a viable channel coding solution to multi-source information streams with timely update requirements.

## Iterative Collision Resolution for Slotted ALOHA With NOMA for Heterogeneous Devices

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9354838
- **Type**: journal
- **Published**: May 2021
- **Authors**: Yu-Chih Huang, Shin-Lin Shieh, Yu-Pin Hsu +1
- **PDF**: https://ieeexplore.ieee.org/document/9354838
- **Abstract**: In this paper, the problem of using uncoordinated multiple access (UMA) to serve a massive amount of heterogeneous users is investigated. Leveraging the heterogeneity, we propose a novel UMA protocol, called iterative collision resolution for slotted ALOHA (IRSA) with non-orthogonal multiple access (NOMA), to improve the conventional IRSA. In addition to the inter-slot successive interference cancellation (SIC) technique used in existing IRSA-based schemes, the proposed protocol further employs the intra-slot SIC technique that enables collision resolution for certain configurations of collided packets. A novel multi-dimensional density evolution is then proposed to analyze and to optimize the proposed protocol. Simulation results show that the proposed IRSA with NOMA protocol can efficiently exploit the heterogeneity among users and the multi-dimensional density evolution can accurately predict the throughput performance. Last, an extension of the proposed IRSA with NOMA protocol to the frame-asynchronous setting is investigated, where a boundary effect similar to that in spatially-coupled low-density parity check codes can be observed to bootstrap the decoding process.

## Shot Interference Detection and Mitigation for Underwater Acoustic Communication Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9343880
- **Type**: journal
- **Published**: May 2021
- **Authors**: Lei Yan, Xiaoli Ma, Xinbin Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9343880
- **Abstract**: Underwater acoustic communications (UACs) are demanded in a wide range of marine applications. However, one of the main challenges for UACs is unexpected interferences from nearby acoustic activities, especially dynamic and short-period interferences (called shot interference), which are hard to detect, estimate, and mitigate over time- and frequency-selective acoustic channels. In this article, we propose a novel filter that mitigates the interference effects for both single-carrier and multi-carrier systems without any prior knowledge of the interference. An Adaptive Sliding Window Interference Detection (ASWID) algorithm is developed to detect the location and the number of interfered symbols. Meanwhile, a least trimmed squares (LTS) equalizer is presented for the shot interference estimation and mitigation based on robust regression. The proposed algorithms are evaluated through numerical simulations and real channel measurements. Our results show that the proposed designs can detect and mitigate shot interferences effectively for single-carrier and multi-carrier UAC systems.

## Code-Aided Modulation Classification Algorithm for Multiuser Uplink SC-FDMA Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9344668
- **Type**: journal
- **Published**: May 2021
- **Authors**: Mohamed Marey, Hala Mostafa
- **PDF**: https://ieeexplore.ieee.org/document/9344668
- **Abstract**: Modulation classification has attracted great interest in rapid deployment in wireless radios for civilian and military applications. While there is a massive amount of works on this topic for single-signal transmissions, a few works are reported in the literature for multi-signal transmissions. Therefore, there is an urgent need to explore different modulation classification algorithms for such scenarios. In this work, we propose a novel modulation classification algorithm for multiuser uplink single-carrier frequency division multiple access systems exploiting the channel decoder's soft information as a beneficial resource to improve the classification performance. Starting from the maximum-likelihood principle, we analytically design the proposed algorithm using a space-alternating generalized expectation-maximization approach. Channel estimation is also developed as an auxiliary task for the proposed algorithm. Simulation results indicate that the proposed algorithm is superior to the traditional algorithms with reduced processing time.

## Unary Coding Design for Simultaneous Wireless Information and Power Transfer With Practical M-QAM

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9303399
- **Type**: journal
- **Published**: May 2021
- **Authors**: Yizhe Zhao, Jie Hu, Kun Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/9303399
- **Abstract**: Relying on the propagation of modulated radio-frequency (RF) signals, we can achieve simultaneous wireless information and power transfer (SWIPT) to support low-power communication devices. In this paper, we proposed a unary coding based SWIPT encoder by considering a practical M-QAM. Markov chains are exploited for characterising coherent binary information source and for modelling the generation process of modulated symbols. Therefore, both mutual information and the average energy harvesting performance at the SWIPT receiver are analysed in semi-closed-form. With the aid of the genetic algorithm, the sub-optimal codeword distribution of the coded information source is obtained by maximising the average energy harvesting performance, while satisfying the requirement of the mutual information. Simulation results demonstrate the advantage of the SWIPT encoder. Moreover, a higher-level unary code and a lower-order M-QAM results in higher WPT performance, when the maximum transmit power of the modulated symbol is fixed.

## A Digital Two-Stage Phase Noise Compensation and rCFO/rSCO Tracking Module for mmW Single Carrier Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9374567
- **Type**: journal
- **Published**: May 2021
- **Authors**: Hsun-Wei Chan, Wei-Che Lee, Kang-Lun Chiu +2
- **PDF**: https://ieeexplore.ieee.org/document/9374567
- **Abstract**: This article proposes a digital two-stage phase noise (PN) compensation and residual carrier frequency offset (rCFO) and residual sampling clock offset (rSCO) tracking module in the baseband receiver side for single carrier (SC) systems in the millimeter-wave (mmW) band. The proposed two-stage PN compensation and rCFO/rSCO tracking module (2STG-PNC&T) includes a correlation-based linear interpolation method for the common phase error (CPE) of the low-frequency PN, a subsymbol CPE compensation with a reformed low-complexity π/4 robust PN slicer for the high-frequency PN, and a tracking mechanism for rCFO and rSCO estimation on 64-QAM under the harsh PN condition of the frequency synthesizers used in the mmW band. The proposed module can restrict the maximum rCFO/rSCO within ±0.4 ppm and track the phase error caused by the PN successfully. Besides, the compensated power spectral density of the residual PN is reduced from -90 to -125 dBc/Hz at 1-MHz offset. A four-time parallelism architecture of the new 2STG-PNC&T is proposed to work at a 625-MHz clock rate under 64-QAM for 15 Gb/s transmission. The gate count/power of the proposed design is only 4.0%/6.9% of the overall digital baseband, respectively.

## An Efficient Frame Optimization Scheme for Low Power Wide Area Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9347473
- **Type**: journal
- **Published**: May 2021
- **Authors**: Zhongyang Yu, Baoming Bai, Min Zhu
- **PDF**: https://ieeexplore.ieee.org/document/9347473
- **Abstract**: In order to support low power wide area networks (LPWANs) with a scarce pilot resource, we discuss the data framing and its corresponding optimization problem. In specific, we design a general pilot-symbol-assisted-modulation (G-PSAM) frame based on the standard PSAM (S-PSAM) frame and derive joint data-aided & non-data-aided Cramér-Rao bounds (DA&NDA CRBs) for carrier frequency offset (CFO), phase offset (PO), and time delay estimation, followed by an approximate DA&NDA CRB for the CFO. With the approximate DA&NDA CRB and the well-known control-variate method (CVM), we then provide an efficient G-PSAM frame optimization scheme, which is asymptotically optimal in terms of the mean-squared-error (MSE) performance. Simulation results show the superiority of the optimized G-PSAM frame over the S-PSAM frame for both the short-packet and long-packet transmissions. Meanwhile, we also present an example verification on the joint DA&NDA aided carrier synchronization (i.e., Turbo synchronization).

## Optimal Detection of Multiple Symbol-Slotted Random Access-Based Packet Transmissions

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9330800
- **Type**: journal
- **Published**: May 2021
- **Authors**: Steven Kisseleff, Wolfgang H. Gerstacker
- **PDF**: https://ieeexplore.ieee.org/document/9330800
- **Abstract**: Random access (RA) protocols are suitable for the support of massive connectivity especially in machine-type communications, such as the Internet of Things (IoT). In this context, ALOHA protocols (both slotted and unslotted) have been re-introduced as promising enablers due to a potentially high throughput when enhanced via successive interference cancellation (SIC). Meanwhile, SIC has become the most popular solution for RA detection problems. In this letter, we first point out the weaknesses of SIC and then propose a novel method based on joint detection of all randomly scheduled data packets. The proposed method is based on the joint computation of a-posteriori probabilities for all data symbols and packet localizations, such that optimal detection for RA is obtained.

## Hybrid Probabilistic-Geometric Shaped LDPC-coded PM- 16QAM in 140 km DWDM Metro Network Communication

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9571396
- **Type**: conference
- **Published**: 9-14 May 2
- **Authors**: Xiao Han, Ivan B Djordjevic, Aleksandra Z. Jovanovic
- **PDF**: https://ieeexplore.ieee.org/document/9571396
- **Abstract**: We implement a hybrid probabilistic-geometric shaping (PGS) LDPC-coded PM-16QAM in a 140 km DWDM metro-network-communication link. We experimentally demonstrate that hybrid PGS LDPC-coded-modulation scheme can provide 0.95 dB improvement over corresponding uniform-distribution-based scheme.

## LDPC-Coded Squeezed-Displaced States-based Quantum Communications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9571143
- **Type**: conference
- **Published**: 9-14 May 2
- **Authors**: Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/9571143
- **Abstract**: We demonstrate that LDPC-coded squeezed-displaced-states-based QPSK has better tolerance to background noise and significantly outperforms corresponding coherent states-based counterpart. For average number of thermal photons 0.3, for LDPC-code of rate 0.8, the improvement is >3 dB.

## 2-µm-band Coherent Transmission of Nyquist-WDM 16-QAM Signal by On-chip Spectral Translation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9571617
- **Type**: conference
- **Published**: 9-14 May 2
- **Authors**: Deming Kong, Yong Liu, Zhengqi Ren +10
- **PDF**: https://ieeexplore.ieee.org/document/9571617
- **Abstract**: We propose and demonstrate the first low-latency 2-µm-band coherent N-WDM transmission by on-chip spectral translation of 4×32-Gbaud 16-QAM signals with 33-GHz spacing. 318.25 Gbit/s net-rate is achieved with error-free performance after 1.15km hollow-core fiber transmission.

## A Code Scheme for G3-PLC Physical Layer Specification Based on Turbo Code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9441595
- **Type**: conference
- **Published**: 7-9 May 20
- **Authors**: Li Jianqi, Zhang Zhe, Zhang Chuanyuan +2
- **PDF**: https://ieeexplore.ieee.org/document/9441595
- **Abstract**: In this paper, A G3-PLC coding scheme based on the Turbo code is proposed. The scheme replaces the convolution encoder in the G3-PLC standard with a Turbo encoder. The Turbo encoder based on random inner interleaver and odd-even punching is constructed to adapt to the G3-PLC standard. A comparison with the coding scheme in the G3 specification and LDPC code is performed, confirming that the proposed scheme has well trade-off in flexibility and reliability. Finally, an implementation on G3-PLC Data Concentrator is carried out to prove the Turbo scheme feasibility in future practical narrowband PLC system.

## A Deep Learning Based Method for Blind Recognition of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9441497
- **Type**: conference
- **Published**: 7-9 May 20
- **Authors**: Longqing Li, Linhai Xie, Zhiping Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/9441497
- **Abstract**: Deep learning is an emerging research direction in machine learning, which has a promising application in the field of communications. In this paper, we focus on adaptive coding systems based on LDPC codes and study the problem of blind recognition with a pre-defined LDPC encoder candidate set. We propose a deep learning (DL)-based method for blind recognition using the log-likelihood ratios (LLR) of the syndrome a posteriori probabilities (SPP). The proposed method requires only a simple Multi-Layer Perceptron (MLP) and can therefore be easily used for systems with high real-time requirements as well as can be easily adapted to different codes and channel parameters. Simulation results show that the proposed approach allows for a comparable recognition performance to existing methods.

## Blind Recognition of LDPC Codes Using Convolutional Neural Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9450940
- **Type**: conference
- **Published**: 7-10 May 2
- **Authors**: Longqing Li, Zhiping Huang, Chunwu Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/9450940
- **Abstract**: The Low Density Parity Check codes have been widely used in modern communication systems, such as 5G new radio and fiber optic communications. In order to balance the quality and rate of communication, both sides of the communication tend to use different codes depending on the channel conditions. Therefore, the blind recognition technology of encoders is receiving increasing attention. At present, the blind recognition methods for Low Density Parity Check codes has been extensively studied. However, most of these methods require accurate estimation of the channel and are therefore limited to specific application scenarios. In this paper, we propose a method for blind recognition of Low Density Parity Check codes using convolutional neural networks. This approach is more flexible than the existing methods and can therefore be quickly deployed to new systems. Simulation results show that a simple network can achieve better identification performance than the existing methods.

## Novel Multi-Parameter based Rate-Matching of Polar Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9486401
- **Type**: conference
- **Published**: 4-5 May 20
- **Authors**: Souradip Saha, Marc Adrat
- **PDF**: https://ieeexplore.ieee.org/document/9486401
- **Abstract**: Polar codes have garnered a lot of attention from the scientific community owing to their low-complexity implementation and provably capacity achieving capability. They have been proposed to be used in 5G networks. However, the conventional approach of channel polarization introduced by Arikan in [1], can be used to design only codewords of length N = 2n, which is a major limitation when codewords of length N ≠ 2n are required. To perform rate-matching for such codeword lengths, using non-2×2 circuit kernels or resizing techniques (upsizing or downsizing) are the solutions. As per the technical specifications of 3GPP 5G NR standardization document [2], a unique threshold coderate value is used to determine whether puncturing or shortening should be used for downsizing polar codes, which although being plausibly optimal for the system configurations in [2], might be sub-optimal over a wider range of design parameter settings. In this paper, we introduce a novel downsizing type-selection (DTS) parameter which takes into account codeword length, coderate, effect of polarization and number of downsized bits, to determine the preferable method for downsizing polar codes.

## Information Bottleneck Message Passing for Military Applications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9486405
- **Type**: conference
- **Published**: 4-5 May 20
- **Authors**: Jan Lewandowsky, Marc Adrat, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/9486405
- **Abstract**: Military communication systems naturally have strong requirements concerning the reliability and the robustness of their physical layer data transmission schemes. Modern channel coding and modulation schemes can meet these requirements in general, but their detection and decoding at the receiving end requires complex and power demanding high-precision implementations of digital algorithms, which are often not suitable for military applications. This motivates to explore novel techniques to build simple detection and decoding algorithms with good performance. In this article, we present novel results on the recent idea of using a machine learning framework termed the Information Bottleneck method to replace demanding implementations of the sum-product algorithm with very simple quantized message passing schemes. We provide a novel explanation, which links the Information Bottleneck decoder processing to the sum-product algorithm. Moreover, we present a novel Information Bottleneck demodulation scheme for quadrature amplitude modulation and discuss special advantages of the Information Bottleneck system design approach for military applications.

## A High Throughput QC-LDPC Decoder Architecture for Near-Earth Satellite Communication

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9464195
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: K. M. Sankar Nampoothiri, Kalyani N Menon, Sayed Muhsin +4
- **PDF**: https://ieeexplore.ieee.org/document/9464195
- **Abstract**: This paper presents a high throughput decoder architecture for the (8176,7154) quasi-cyclic (QC) low density parity check (LDPC) code (C2) recommended by the Consultative Committee for Space Data Systems (CCSDS) for near-earth applications. The architecture avoids memory conflict through the use of multiple shift register based memory circuits and a pipe stage forwarding mechanism, thus allowing for heavy pipelining of the core processing unit. The decoder is implemented on the Xilinx XCVU9P FPGA platform and achieves a throughput of 2.65 Gbps at 10 iterations at a clock frequency of 253 MHz.

## Uniquely Decodable Ternary Codes via Augmented Sylvester-Hadamard Matrices

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9527898
- **Type**: conference
- **Published**: 24-28 May 
- **Authors**: Michel Kulhandjian, Hovannes Kulhandjian, Claude D’Amours
- **PDF**: https://ieeexplore.ieee.org/document/9527898
- **Abstract**: In this paper, we consider the problem of designing uniquely decodable (UD) ternary code sets for low-density spreading code-division multiple-access (LDS-CDMA) systems. The proposed code set provides unique decodability for a number of users K that is greater than the length of the code but lower than the theoretical maximum, i.e., $K\lt K_{\max}^{t}$ *. Simulation results show that with channel encoded scenarios (e.g., turbo, LDPC, polar, etc.) the proposed UD code sets achieve 4 dB or greater performance improvement at a bit error rate (BER) of 10−3 compared to other competing code sets in an additive white Gaussian noise (AWGN) and flat Rayleigh fading channels.

## Channel Reconstruction Based Multiuser Precoding with Limited Feedback

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9527824
- **Type**: conference
- **Published**: 24-28 May 
- **Authors**: Mert Özateş, Mohammad Kazemi, Çağrı Göken +1
- **PDF**: https://ieeexplore.ieee.org/document/9527824
- **Abstract**: We consider the downlink of a multiuser multiple-input multiple-output (MU-MIMO) system, where each user feeds back a partial channel state information (CSI), namely, the quantized version of the dominant eigenvector of its channel covariance matrix, to the base station (BS) for precoding. Specifically, we propose a downlink multiuser precoding scheme by first reconstructing the equivalent channel matrix of each user via a limited feedback, and then by employing a precoder to suppress the multiuser interference at the receivers. For the single stream case, a signal-to-leakage-and-noise ratio (SLNR) based precoding is employed, while for the full stream case with limited feedback, we employ a lattice reduction aided block diagonalization type precoding with suitable modifications at the receiver side. Extensive numerical examples which are provided using the 5G new radio (5G-NR) channel models demonstrate that the proposed schemes outperform the existing eigenvector based algorithms, and they are more robust against the downlink channel estimation errors.

## A Low Complexity Parallel QC-LDPC Encoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9499562
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: Xiaoxia Yao, Lintao Li, Jihong Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9499562
- **Abstract**: In this paper, a low complexity parallel QC (quasi-cyclic)-LDPC (low-density parity-check) Codes encoding algorithm and encoder architecture is introduced. In traditional encoder architectures, the complexity of multiplication operation of information sequence and generator matrix is very high. The proposed encoding algorithm bit selection (BS) directly selects the valid information bits according to position set of non-zero elements in the first column of the sub-matrix, which avoids the operation of invalid information bits. The proposed parallel QC-LDPC encoder architectures is realized for FPGA implementation based on CCSDS (7154, 8176) LDPC codes.

## High Energy-Efficient LDPC Decoder with AVFS System for NAND Flash Memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401163
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Chao Zhang, Jingtong Mo, Zihan Lian +1
- **PDF**: https://ieeexplore.ieee.org/document/9401163
- **Abstract**: In conventional Low-Density Parity-Check (LDPC) decoders, the real-time processing performance should meet its maximum decoding iterations for all packets and the work frequency or supply voltage is always fixed at a high level, which decreases its energy efficiency. In this paper, an energy- efficient LDPC decoding architecture with an adaptive voltage-frequency scaling (AVFS) scheme is presented. According to the usage of input packet FIFO related to variable decoding iterations, the architecture can dynamically adjust decoder's work frequency and supply voltage to reduce the processing energy while meeting its real-time processing requirement. Finally, the decoder is implemented with 28 nm CMOS process. Experimental results show that our decoder has a throughput of 1590 Mb/s when the raw bit error rate (RBER) of Flash memory is up to 10-2. The power consumption of the decoder can be reduced by 25%-62% and energy efficiency can be increased to 1.3-2.5 times under different AWGN noise.

## A 33.2 Gbps/Iter. Reconfigurable LDPC Decoder Fully Compliant with 5G NR Applications

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401329
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Chieh-Yu Lin, Li-Wei Liu, Yen-Chin Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/9401329
- **Abstract**: This paper presents a reconfigurable LDPC decoder implementation fully compliant with all the configurations in the 5G NR standard. Based on the row-based layered normalized Min-Sum (NMS) algorithm, the optimization approaches are proposed to solve the data dependency hazard in the pipeline process. The proposed instruction-level reordering diminishes the redundant latency of our pipelined decoder architecture. Moreover, the proposed data-level rescheduling optimizes the decoding sequence to remove the remaining pipeline stalls in the high- throughput design without decoding performance degradation. Evaluated in Xilinx VCU1525 FPGA, our design achieves a throughput of 6.7 Gbps per iteration. Implemented in TSMC 28nm CMOS process at the post-layout stage, a 33.2 Gbps, in one iteration, throughput can be achieved at a clock rate 556 MHz with the core area 1.97 mm2.

## Segmented Reconfigurable Cyclic Shifter for QC-LDPC Decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401118
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Hing-Mo Lam, Silin Lu, Hezi Qiu +3
- **PDF**: https://ieeexplore.ieee.org/document/9401118
- **Abstract**: In various wireless communication standards, such as Wi-Fi, WiMAX, and 5G standards, QC-LDPC decoders are required to decode a codeword of variable length. Part of the decoder is in idle if the length of codeword is not the maximum. A reconfigurable cyclic shifter is a key element of a QC-LDPC decoder. If the shifter can only shift one input at a time, the QC- LDPC decoder can only decode one codeword at a time as well. A segmented reconfigurable cyclic shifter is proposed in this paper to enable a QC-LDPC decoder to parallelly decode multiple codewords. The proposed shifter can be reconfigured into multiple segments of different sizes. Each segment can perform a cyclic shift of different shift values independently. Therefore, the proposed shifter can enhance the QC-LDPC decoder to decode multiple codewords parallelly by inputting another codeword (or codewords) to re-activate the idle hardware. The test chip of QC- LDPC decoder with the proposed segmented reconfigurable cyclic shifter has been fabricated in 0.18μ CMOS technology which can parallelly decode six codewords.

## High-Efficient Nonbinary LDPC Decoder with Early Layer Decoding Schedule

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401072
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Thang Xuan Pham, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/9401072
- **Abstract**: Increasing nonbinary low density parity check (NB-LDPC) decoder throughput is challenging. This paper considers nonbinary quasi-cyclic LDPC code features to propose an early layered decoding schedule. The proposed method can eliminate idle time introduced by emptying pipeline stages after each layered decoding process, as well as increase decoder throughput. Layout results using TSMC 90-nm CMOS technology confirm that the proposed decoding schedule improved throughput with almost the same hardware complexity compared to the state-of- the-art NB-LDPC decoder. In particular, the proposed approach achieved considerably improved throughput and efficiency compared with predecessors when both early layer decoding schedule and early decoding termination were enabled.

## Content Distribution Network for Streaming Using Multiple Galois Fields

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401700
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Tsung-Kang Hung, Sachin K. Kaushal, Hsu-Feng Hsiao
- **PDF**: https://ieeexplore.ieee.org/document/9401700
- **Abstract**: In this paper, the architecture of random linear network coding based on the hybrid coding in multiple Galois field sizes is proposed. Random linear network coding is an efficient network coding approach that enables network to generate independently and randomly linear mapping between input and output symbols over finite field. With the proposed reduction method, coded symbols and coefficients in higher degree of Galois field can be converted to symbols and coefficients in GF(2) so that hybrid coding in multiple Galois field sizes can be made possible. Therefore, peers in the heterogeneous environments can all benefit from the proposed content distribution network for streaming to better utilize the network resource.

## BER Evaluation System Considering Device Characteristics of TLC and QLC NAND Flash Memories in Hybrid SSDs with Real Storage Workloads

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401203
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Mamoru Fukuchi, Shun Suzuki, Kyosuke Maeda +2
- **PDF**: https://ieeexplore.ieee.org/document/9401203
- **Abstract**: This paper proposes BER evaluation system that evaluates BER of TLC and QLC NAND flash memories with reliability information such as write and erase (W/E) cycle and data-retention time by combining SSD model emulator and device characteristics of NAND flash memories. Proposed system decides which ECC type should be used in TLC and QLC NAND flash in SCM/TLC/QLC NAND flash tri-hybrid SSD, corresponding to various applications and memory capacity ratio. For hm_0 (write- cold application), BCH ECC is enough to correct bit errors in TLC NAND flash. On the other hand, for prxy_0 (write-hot application), LDPC ECC must be applied to TLC NAND flash in case of small SCM capacity, large W/E cycles and high BER in TLC NAND flash. In contrast, this paper concludes that QLC NAND flash needs LDPC ECC regardless of application and memory capacity.

## Efficient Fast-SCAN Flip Decoder for Polar Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9401398
- **Type**: conference
- **Published**: 22-28 May 
- **Authors**: Leyu Zhang, Yutai Sun, Yifei Shen +3
- **PDF**: https://ieeexplore.ieee.org/document/9401398
- **Abstract**: Soft-output decoder is of great importance to be applied in iterative receivers, of which belief propagation (BP) algorithm has been widely studied for 5G low-density parity- check (LDPC) and polar codes. However, for polar codes, BP decoding suffers from high computational complexity and unsatisfactory convergence. To this end, soft cancellation (SCAN) polar decoder has recently drawn attention from academia and can be further improved by using the bit-flipping strategy. Limited by the serial nature of message propagation, the SCAN flip (SCANF) decoder cannot meet a high throughput. In this paper, we accelerate the decoding speed by the fast processing mechanism, conducting Fast-SCANF decoder. The corresponding hardware architecture is designed with memory optimization and implemented by TSMC 40nm technology, delivering a 2.1 Gbps throughput and 65 pJ/b energy. To the knowledge of authors, this is the first SCANF hardware decoder.

## Performance Analysis of LDPC Decoding Algorithms for CCSDS Telecommand Space Data Link Protocol

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9456163
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: P. Rajagopalan, Pradeesh Madavan, H Ramamurthy +1
- **PDF**: https://ieeexplore.ieee.org/document/9456163
- **Abstract**: This paper presents the simulation of the encoding scheme defined by CCSDS for satellite Telecommand operations and analysis of various soft decision and hard decision decoding algorithms for the same. The G(Generator), H (Parity-check) matrices are designed and verified for encoding and decoding of the message respectively. The decoding algorithms are implemented and the performances are analyzed and non-convergence of decoding algorithms, scheduling restrictions of the defined H, G matrix are explored. It is found that soft decision algorithms give 6dB coding gain and hard decision algorithms give 4 dB coding gain for the 4-bit quantized inputs.

## Associated Sectors of Magnetic Recording System via Spatially Coupled LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9454834
- **Type**: conference
- **Published**: 19-22 May 
- **Authors**: Sirawit Khittiwitchayakul, Pornchai Supnithi, Watid Phakphisut
- **PDF**: https://ieeexplore.ieee.org/document/9454834
- **Abstract**: Spatially coupled low-density parity-check (SC- LDPC) codes have emerged as promising advanced error- correcting codes (ECC) for future high-density magnetic recording (MR) systems, which require excellent error-correcting performance and acceptable practical complexity. In the traditional MR systems, the non-associated sectors are generally used, whereby two consecutive sectors are independently decoded by ECC. In this work, we propose the associated sectors of MR systems in which the information stored in the previous sectors can be requested by ECC to reinforce the decoding of the current sector. Moreover, the proposed associated sectors can mitigate the rate-loss problem of SC-LDPC codes in the MR systems. We demonstrate the bit-error-rates (BERs) of SC-LDPC codes in the bit-patterned media magnetic recording (BPMR) systems with non-associated sectors and associated sectors. The simulation results show that the associated sectors help achieve significant performance gains compared to the non-associated sectors.

## Joint Design of Channel Output Quantizer and LUT-Based LDPC Decoder

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9454862
- **Type**: conference
- **Published**: 19-22 May 
- **Authors**: Chatuporn Duangthong, Pornchai Supnithi, Watid Phakphisut
- **PDF**: https://ieeexplore.ieee.org/document/9454862
- **Abstract**: Recently, the LUT-based LDPC decoder has been designed by maximizing mutual information, where the performances of channel output quantizer and LUT-based decoder are considered separately. In this work, we propose the joint design of the channel output quantizer and LUT-based decoder. Our joint design aims to minimize the error probability of LDPC decoding through the density evolution algorithm. We found that the joint design outperforms the previous work at the waterfall region.

## Determining the Effectiveness of LDPC Codes for 5G Information Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9501120
- **Type**: conference
- **Published**: 19-21 May 
- **Authors**: Juliy Boiko, Ilya Pyatin, Oleksander Eromenko
- **PDF**: https://ieeexplore.ieee.org/document/9501120
- **Abstract**: This paper is devoted to research of the urgent problem of developing models of efficient coding in telecommunication networks on the basis of low-density parity-check codes. The solution of the problem is carried out taking into account the code rate and the number of iterations decoding for envisaging the defined noise immunity indices. The noise immunity of signal-code constructions based on low-density codes has been increased by combining them with multi position digital modulation. This solution eventually allowed to develop a strategy for decoder designing of such codes and to optimize the code structure for a specific information network. The paper presents experimental studies of low-density codes for different types of channels. The maximum noise immunity is determined. The possibility of combining low-density codes with differential modulation is estimated. The research results of productivity of information transmission channels with defined codes at different values of redundancy, transport block size, code rate are given.

## Application and Analysis of Expectation Propagation Algorithm in the Binary Erasure Quantization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9519624
- **Type**: conference
- **Published**: 19-20 May 
- **Authors**: Golshan Piroozzadeh, Reza Asvadi
- **PDF**: https://ieeexplore.ieee.org/document/9519624
- **Abstract**: Regarding the widespread utilization of big data, compression and reconstruction of valuable data sets get more essential from the aspect of data storage management. The Binary Erasure Quantization (BEQ) problem considers data-worth for compression and is solved by a dual form of the Belief Propagation (BP) algorithm. Nevertheless, the dual of BP does not converge to the optimum performance because of adverse short cycles in the associated graph of the compression code. We propose a form of Expectation Propagation (EP) algorithm, which gives rise to a precise inference for the BEQ. By the suggested algorithm, the empirical compression rate with zero distortion approximately tends to the theoretical BEQ lossless compression rate.

## Combining Scrambling and Multilevel Coding for Physical-Layer Security

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9472213
- **Type**: conference
- **Published**: 19-20 May 
- **Authors**: Johannes Pfeiffer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/9472213
- **Abstract**: In fiber-optical communication systems, security against wiretappers is of importance. To counteract successful eavesdropping, classical encryption schemes may be complemented by approaches following the concept of physical-layer security (PLS), e.g., the application of suited coding and modulation schemes. In a Gaussian wiretap scenario, the security level may be quantified by the security gap. A recent strategy for PLS is to scramble secret messages prior to transmission, in particular using self-synchronizing scrambling schemes. The combination of channel codes with bit-wise scrambling enables a significant security increase compared to conventional coded transmission, as the error rates at the legitimate receiver are hardly affected. In contrast, an eavesdropper operating at slightly worse channel conditions experiences bit error rates close to 0.5 due to the error multiplication in the descrambling process. An additional security increase can be achieved by a suitable choice of the coded modulation scheme in case of higher-order modulations. Especially the application of multilevel coding (MLC), where scrambled messages are transmitted exclusively over the lowest bit level, yields smaller security gaps than bit-interleaved coded modulation (BICM) if the same channel code and scrambling scheme is utilized. However, this comes at the cost of a decreased secure transmission rate. In this paper, low-density paritycheck (LDPC) codes are applied and combined with various scrambling schemes. The results are compared to theoretically achievable security gaps, which are derived considering perfect scrambling, where any non-zero number of errors prior to descrambling is assumed to result in 50% erroneous bits.

## CICADA: A New Tool to Design Circuits with Correction and Detection Abilities

- **Status**: 미선별
- **Reason**: N/A
- **ID**: ieee:9438900
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Alexander L. Stempkovsky, Tatiana D. ZHukova, Dmitriy Vl. Telpukhov +1
- **PDF**: https://ieeexplore.ieee.org/document/9438900
- **Abstract**: In view of rapid development of microelectronic industry, there is a growing need to ensure reliability and fault tolerance of combinational devices exposed to various destabilizing effects. To solve this problem, methods based on synthesis of concurrent error detection (CED) circuits are now increasingly used, which enable, at the expense of some structural redundancy, correcting and/or detecting errors arising in the circuit. For each specific circuit, depending on the chosen synthesis method, CED circuits have different reliability characteristics, which makes it difficult for designers to choose one or another architecture. Therefore, there is a need to increase automation level of the process of selecting a method for control circuit synthesis, depending on the initial parameters of the protected device. This work is devoted to development of methods and software for detecting the best method for synthesizing a control circuit, taking into account the user-introduced constraint on structural redundancy of the resulting circuit.
