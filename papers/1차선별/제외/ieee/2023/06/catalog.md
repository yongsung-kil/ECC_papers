# IEEE Xplore — 2023-06


## Classification of Δ-Divisible Linear Codes Spanned by Codewords of Weight Δ

- **Status**: ❌
- **Reason**: q-ary Δ-divisible 선형부호 분류(부호이론 일반) — LDPC ECC 디코더/HW/구성 기여 없음
- **ID**: ieee:10026815
- **Type**: journal
- **Published**: June 2023
- **Authors**: Michael Kiermaier, Sascha Kurz
- **PDF**: https://ieeexplore.ieee.org/document/10026815
- **Abstract**: We classify all  $q$ -ary  $\Delta $ -divisible linear codes which are spanned by codewords of weight  $\Delta $ . The basic building blocks are the simplex codes, and for  $q=2$  additionally the first order Reed-Muller codes and the parity check codes. This generalizes a result of Pless and Sloane, where the binary self-orthogonal codes spanned by codewords of weight 4 have been classified, which is the case  $q=2$  and  $\Delta =4$  of our classification. As an application, we give an alternative proof of a theorem of Liu on binary  $\Delta $ -divisible codes of length  $4\Delta $  in the projective case.

## Improved Decoding of Expander Codes

- **Status**: ❌
- **Reason**: expander code 거리/리스트디코딩 한계의 조합론적 이론 분석 — LDPC 디코더/HW/구성으로 안 이어지는 순수 이론 bound
- **ID**: ieee:10024861
- **Type**: journal
- **Published**: June 2023
- **Authors**: Xue Chen, Kuan Cheng, Xin Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10024861
- **Abstract**: We study the classical expander codes, introduced by Sipser and Spielman, (1996). Given any constants  $0 < \alpha, \varepsilon < 1/2$ , and an arbitrary bipartite graph with  $N$  vertices on the left,  $M < N$  vertices on the right, and left degree  $D$  such that any left subset  $S$  of size at most  $\alpha N$  has at least  $(1- \varepsilon)|S|D$  neighbors, we show that the corresponding linear code given by parity checks on the right has distance at least roughly  $\frac {\alpha N}{2 \varepsilon }$ . This is strictly better than the best known previous result of  $2(1- \varepsilon) \alpha N$  Sudan, (2000), Viderman, (2013) whenever  $\varepsilon < 1/2$ , and improves the previous result significantly when  $\varepsilon $  is small. Furthermore, we show that this distance is tight in general, thus providing a complete characterization of the distance of general expander codes. Next, we provide several efficient decoding algorithms, which vastly improve previous results in terms of the fraction of errors corrected, whenever  $\varepsilon < \frac {1}{4}$ . Finally, we also give a bound on the list-decoding radius of general expander codes, which beats the classical Johnson bound in certain situations (e.g., when the graph is almost regular and the code has a high rate). Our techniques exploit novel combinatorial properties of bipartite expander graphs. In particular, we establish a new size-expansion tradeoff, which may be of independent interests.

## Joint Optimization of OFDM and Channel Coding for URLLC in Industrial Channels

- **Status**: ❌
- **Reason**: URLLC 무선 OFDM+코딩 결합 최적화, LDPC는 선택지 베이스라인일 뿐 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:9919381
- **Type**: journal
- **Published**: June 2023
- **Authors**: Yasantha Samarawickrama, Álvaro A. M. de Medeiros, Victor Cionca
- **PDF**: https://ieeexplore.ieee.org/document/9919381
- **Abstract**: Industrial communications have very tight requirements of reliability and latency, which are challenging to achieve at highly dynamic industrial radio channels. Redundancy in the modulation and coding can improve reliability but incurs excess latency. Minimizing latency subject to reliability constraint for a given channel state opens up the scope for static and runtime optimization. In this article, we explore joint optimal configuration of orthogonal frequency division multiplexing (OFDM) and channel coding, using polar, low density parity check (LDPC) and convolutional codes to minimize the transmission time subject to a maximum acceptable packet error rate, for three realistic channels reported by National Institute of Standards and Technology, using channel impulse response measurements, as well as perfect and imperfect channel estimation. The results show that the use of strong channel codes can significantly reduce transmission time, by up to 24% compared to convolutional codes, with LDPC achieving fastest transmission. For transmission times of 10–20 ${\rm\mu}$s, the contribution of the cyclic prefix (CP) is significant, up to 30% for convolutional codes. Stronger channel codes allow reduced CP, even considering the added redundancy such as cyclic redundancy check, resulting in overall lower transmission time. The decoding time also introduces significant overheads, up to 50% of transmission time for polar codes. The article also investigates the impact of channel estimation errors, which adversely impact ultrareliable low-latency performance: Lower bound errors violate the reliability constraint and higher bound errors introduce excess transmission times.

## In-Band Full-Duplex Communications in ATSC 3.0 Single Frequency Network

- **Status**: ❌
- **Reason**: ATSC 3.0 SFN 간섭 제거 기법 — LDPC 부수 언급, 떼어낼 ECC 기법 없는 무선 응용 특이적
- **ID**: ieee:10057133
- **Type**: journal
- **Published**: June 2023
- **Authors**: Zhihong Hunter Hong, Liang Zhang, Wei Li +7
- **PDF**: https://ieeexplore.ieee.org/document/10057133
- **Abstract**: Wireless in-band backhaul, a.k.a. in-band distribution links (IDL), is a spectrum-efficient and cost-effective enabling technology to the realization of Advanced Television Systems Committee (ATSC) 3.0 in the single frequency network (SFN) mode, where all the transmitter towers are synchronized to transmit the same broadcast signal in the same frequency band. Inter-tower communications network (ITCN) transforms the broadcast towers into a mesh network, thereby introducing datacasting capability to the traditional broadcast network. Both the ITCN and IDL can be operated in the most spectrum-efficient in-band full-duplex (IBFD) mode. In these situations, the ITCN/IDL receivers at the SFN towers receive the signal of interest (SOI) not only severely corrupted by the self-interference signal from its co-located transmitter, but also the co-channel interference signals from neighbouring transmitters. Moreover, the ITCN/IDL signals may be combined with the broadcast signal in the Layer Division Multiplexing (LDM) format to achieve better overall spectral efficiency. Therefore, the LDM inter-layer interference must also be mitigated. In this paper, the interferences for the ITCN/IDL signal in the SFN environment are analyzed, and a novel iterative successive signal cancellation scheme is proposed to effectively mitigate the interferences in the ITCN/IDL signal detection process in ATSC 3.0 SFNs.

## Basis-Finding Algorithm for Decoding Fountain Codes for DNA-Based Data Storage

- **Status**: ❌
- **Reason**: DNA 저장용 fountain(LT) 코드 디코딩 BFA — LDPC가 아닌 fountain/erasure 외부코드, 떼어낼 ECC 기법 없음
- **ID**: ieee:10035460
- **Type**: journal
- **Published**: June 2023
- **Authors**: Xuan He, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/10035460
- **Abstract**: In this paper, we consider the decoding of fountain codes where the received symbols may have errors. It is motivated by the application of fountain codes in DNA-based data storage systems where the inner code decoding, which generally has undetectable errors, is performed before the outer fountain code decoding. We propose a novel and efficient decoding algorithm, namely basis-finding algorithm (BFA), followed by three implementations. The key idea of the BFA is to find a basis of the received symbols, and then use the most reliable basis elements to recover the source symbols with the inactivation decoding. Gaussian elimination is used to find the basis and to identify the most reliable basis elements. As a result, the BFA has polynomial time complexity. For random fountain codes, we are able to derive some theoretical bounds for the frame error rate (FER) of the BFA. Extensive simulations with Luby transform (LT) codes show that, the BFA has significantly lower FER than the belief propagation (BP) algorithm except for an extremely large amount of received symbols, and the FER of the BFA generally decreases as the average weight of basis elements increases.

## Graph-based conflict-free MAC protocol and conflict analysis for a two-layer ultraviolet communication network

- **Status**: ❌
- **Reason**: UV 통신망 MAC 프로토콜/충돌 분석 — LDPC ECC와 무관
- **ID**: ieee:10131967
- **Type**: journal
- **Published**: June 2023
- **Authors**: Yuchen Pan, Guanchu Wang, Yubo Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10131967
- **Abstract**: To efficiently exploit the space division multiplexing of ultraviolet (UV) communication, we apply link coverage characteristics to construct a conflict graph and design conflict-free protocols for a two-layer UV communication network. The network is divided into two layers: the first-layer network forms a backbone and the second-layer network serves as local access. We construct a routing model and medium-access control (MAC) model. Then we propose Routing-MAC joint scheduling for the first-layer network based on the conflict graph. We investigate the system throughput and delay of joint scheduling under different node intensities. For second-layer networks, we propose a multi-link conflict-free protocol adopting protocol frames of carrier sense multiple access with collision avoidance (CSMA/CA). Numerical results show that the multi-link conflict-free protocol can improve the system throughput by more than 100% compared with CSMA/CA. Moreover, we perform a conflict analysis on the proposed protocols to investigate the influence of conflict intensity. According to the conflict analysis, we optimize the path planning of Routing-MAC joint scheduling to reduce the average delay of the network. Numerical results show that the optimized Routing-MAC joint scheduling leads to larger system throughput and lower delay.

## Bit-Metric Decoding Rate in Multi-User MIMO Systems: Applications

- **Status**: ❌
- **Reason**: MU-MIMO 링크적응·PHY abstraction(ML 기반 SINR 추정), LDPC ECC 기법 없음
- **ID**: ieee:9961232
- **Type**: journal
- **Published**: June 2023
- **Authors**: K. Pavan Srinath, Jakob Hoydis
- **PDF**: https://ieeexplore.ieee.org/document/9961232
- **Abstract**: This is the second part of a two-part paper that focuses on link-adaptation (LA) and physical layer (PHY) abstraction for multi-user MIMO (MU-MIMO) systems with non-linear receivers. The first part proposes a new metric, called bit-metric decoding rate (BMDR) for a detector, as being the equivalent of post-equalization signal-to-interference-noise ratio (SINR) for non-linear receivers. Since this BMDR does not have a closed form expression, a machine-learning based approach to estimate it effectively is presented. In this part, the concepts developed in the first part are utilized to develop novel algorithms for LA, dynamic detector selection from a list of available detectors, and PHY abstraction in MU-MIMO systems with arbitrary receivers. Extensive simulation results that substantiate the efficacy of the proposed algorithms are presented.

## Implementation of SC-FDE waveform on SDRP Using Vitis HLS

- **Status**: ❌
- **Reason**: SC-FDE 파형 HLS 구현, Xilinx LDPC IP 부수 언급뿐 새 ECC 기법 없음
- **ID**: ieee:10262723
- **Type**: conference
- **Published**: 8-9 June 2
- **Authors**: Pankaj Bhatoe, Rajendra Kumar Gupta, Abhishek Jain +1
- **PDF**: https://ieeexplore.ieee.org/document/10262723
- **Abstract**: High Level Synthesis (HLS) tools give designers a time-efficient platform to develop the best design solution by exploring multiple design alternatives without a detailed understanding of hardware. In this work, hardware implementation of Single Carrier Frequency Domain Equalization (SC-FDE) waveform on software-defined radio (SDR) using Vitis HLS is presented. The SC-FDE waveform is implemented on an FPGA-based software-defined radio platform (SDRP). In this platform, Xilinx Virtex-7 FPGA is used as the main processing device to implement modulation, demodulation, synchronization, and Maximal Ration Combining (MRC) functionalities, and AD9364 transceiver is used for baseband to RF conversion. The waveform has been tested for AWGN and fading channels using the Channel Emulator. Resource utilization of HLS-generated IPs and performance of waveform is presented in terms of throughput and SNR with different channel conditions. Furthermore, the performance of this waveform with Xilinx LDPC IP is also presented. We have also validated waveform in the real scenarios by over-the-air transmission. The maximum throughput of 29 Mbps is achieved with this waveform.

## Can graph neural network-based detection mitigate the impact of hardware imperfections?

- **Status**: ❌
- **Reason**: IQI 완화용 GNN 검출기(BP와 비교), LDPC 부호 디코더 기여 아님
- **ID**: ieee:10167895
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Lamprini Mitsiou, Stylianos Trevlakis, Argiris Tsiolas +3
- **PDF**: https://ieeexplore.ieee.org/document/10167895
- **Abstract**: Until recently, researchers used machine learning methods to compensate for hardware imperfections at the symbol level, indicating that optimum radio-frequency transceiver performance is possible. Nevertheless, such approaches neglect the error correcting codes used in wireless networks, which inspires machine learning (ML)-approaches that learn and minimise hardware imperfections at the bit level. In the present work, we evaluate a graph neural network (GNN)-based intelligent detector’s in-phase and quadrature imbalance (IQI) mitigation capabilities. We focus on a high-frequency, high-directional wireless system where IQI affects both the transmitter (TX) and the receiver (RX). The TX uses a GNN-based decoder, whilst the RX uses a linear error correcting algorithm. The bit error rate (BER) is computed using appropriate Monte Carlo simulations to quantity performance. Finally, the outcomes are compared to both traditional systems using conventional detectors and wireless systems using belief propagation based detectors. Due to the utilization of graph neural networks, the proposed algorithm is highly scalable with few training parameters and is able to adapt to various code parameters.

## Very high data rate acoustic communication - continuous image transmission using hierarchical modulation in shallow water near vertical channels

- **Status**: ❌
- **Reason**: 수중음향 계층변조+표준 LDPC, 떼어낼 새 LDPC 기법 없음
- **ID**: ieee:10244612
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: George Masters, Jeff Neasham, Charalampos Tsimenidis +3
- **PDF**: https://ieeexplore.ieee.org/document/10244612
- **Abstract**: Real-time communication in underwater environments is essential for a variety of applications, including exploration, conservation, and construction. However, transmitting compressed video streams across various conditions is challenging due to high-frequency attenuation, time-varying Doppler, multipath propagation, and inconsistent throughput. To address these issues and allow for continuous image transmission in rapidly changing channel conditions we propose a communication system that utilizes advanced signal processing techniques, including an adaptive decision feedback equalizer with a circular array, and low-density parity-check channel coding. The use of hierarchical modulation theoretically has been shown to be beneficial for continuous image transmission due to its flexibility in deciding the image quality at the receiver based on the channel conditions. Hierarchical modulation was investigated to see if it can demonstrate the benefits when compared to standard 16-QAM, in an underwater acoustic channel. The proposed system is tested in the dynamic environment of the North Sea, with Doppler velocities of up to 3 knots at a vertical depth of 100 m. The system is used to transmit still images, where the receiver can decide whether the greyscale or colour image is recoverable. Our approach demonstrates a reliable and efficient communication link, achieving transmission of continuous images with rates up to 100 kb/s while compensating for Doppler shifts in a noisy, multi-reverberating environment utilising a hierarchical modulation scheme.

## Frequency Offset Estimation for High Data Rate Acoustic MIMO-OFDM Systems

- **Status**: ❌
- **Reason**: 수중음향 MIMO-OFDM 주파수오프셋 추정, LDPC 기법 없음
- **ID**: ieee:10244655
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Zhengnan Li, Diego A. Cuji, Yukihiro Kida +3
- **PDF**: https://ieeexplore.ieee.org/document/10244655
- **Abstract**: Multiple-input multiple-output (MIMO) communication techniques are considered with the goal of increasing the information throughput via spatial multiplexing over an underwater acoustic link. Our focus is on designing a frequency offset compensation algorithm for the MIMO system based on multicarrier modulation in the form of orthogonal frequency offset compensation (OFDM). The system relies on the simultaneous estimation of parallel transmit channels and multichannel receive-side data detection. The frequency offset compensation method utilizes a set of hypothesized frequency offsets and proceeds to detect the data symbols in the MIMO-OFDM system. We assess the system performance in terms of per user bit error rate (BER) and demonstrate the proposed methods using MIMO-OFDM recordings collected over a 14 km link off the coast of Kochi Prefecture, Japan, in July 2022. The low complexity and excellent performance of the proposed frequency offset compensation algorithm for MIMO-OFDM systems make it practical for future hardware implementations.

## Training Terahertz Wireless Systems to Battle I/Q Imbalance

- **Status**: ❌
- **Reason**: IQI 완화용 ML 송수신기 공동학습, LDPC 기법 없음
- **ID**: ieee:10167934
- **Type**: conference
- **Published**: 5-8 June 2
- **Authors**: Alexandros-Apostolos A. Boulogeorgos, Angeliki Alexiou
- **PDF**: https://ieeexplore.ieee.org/document/10167934
- **Abstract**: Due to the non-ideality of analog components, transceivers experience high levels of hardware imperfections, like in-phase and quadrature imbalance (IQI), which manifests itself as the mismatches of amplitude and phase between the I and Q branches. Unless proper mitigated, IQI has an important and negative impact on the reliability and efficiency of high-frequency and high-data-rate systems, such as terahertz wireless networks. Recognizing this, the current paper presents an intelligent transmitter (TX) and an intelligent receiver (RX) architecture that by employing machine learning (ML) methodologies is capable to fully-mitigate the impact of IQI without performing IQI coefficients estimation. They key idea lies on co-training the TX mapper’s and RX demapper in order to respectively design a constellation and detection scheme that takes accounts for IQI. Two training approaches are implemented, namely: i) conventional that requires a considerable amount of data for training, and ii) a reinforcement learning based one, which demands a shorter dataset in comparison to the former. The feasibility and efficiency of the proposed architecture and training approaches are validated through respective Monte Carlo simulations.

## WITT: A Wireless Image Transmission Transformer for Semantic Communications

- **Status**: ❌
- **Reason**: 시맨틱 이미지 전송 Transformer; LDPC/채널코딩 ECC 기법 없음
- **ID**: ieee:10094735
- **Type**: conference
- **Published**: 4-10 June 
- **Authors**: Ke Yang, Sixian Wang, Jincheng Dai +3
- **PDF**: https://ieeexplore.ieee.org/document/10094735
- **Abstract**: In this paper, we aim to redesign the vision Transformer (ViT) as a new backbone to realize semantic image transmission, termed wireless image transmission transformer (WITT). Previous works build upon convolutional neural networks (CNNs), which are inefficient in capturing global dependencies, resulting in degraded end-to-end transmission performance especially for high-resolution images. To tackle this, the proposed WITT employs Swin Transformers as a more capable backbone to extract long-range information. Different from ViTs in image classification tasks, WITT is highly optimized for image transmission while considering the effect of the wireless channel. Specifically, we propose a spatial modulation module to scale the latent representations according to channel state information, which enhances the ability of a single model to deal with various channel conditions. As a result, extensive experiments verify that our WITT attains better performance for different image resolutions, distortion metrics, and channel conditions. The code is available at https://github.com/KeYang8/WITT.

## Bit Error and Block Error Rate Training for ML-Assisted Communication

- **Status**: ❌
- **Reason**: ML 통신 학습용 손실함수(BCE/BLER) 제안 — LDPC 디코더/코드설계 기법 아님, 떼어낼 ECC 기여 없음
- **ID**: ieee:10095841
- **Type**: conference
- **Published**: 4-10 June 
- **Authors**: Reinhard Wiesmayr, Gian Marti, Chris Dick +2
- **PDF**: https://ieeexplore.ieee.org/document/10095841
- **Abstract**: Even though machine learning (ML) techniques are being widely used in communications, the question of how to train communication systems has received surprisingly little attention. In this paper, we show that the commonly used binary cross-entropy (BCE) loss is a sensible choice in uncoded systems, e.g., for training ML-assisted data detectors, but may not be optimal in coded systems. We propose new loss functions targeted at minimizing the block error rate and SNR deweighting, a novel method that trains communication systems for optimal performance over a range of signal-to-noise ratios. The utility of the proposed loss functions as well as of SNR deweighting is shown through simulations in NVIDIA Sionna.

## BER-Aware Dynamic Resource Management for Edge-Assisted Goal-Oriented Communications

- **Status**: ❌
- **Reason**: BER-aware goal-oriented 무선 자원관리·Lyapunov 최적화 — LDPC ECC 기법 없음, 응용 특이적
- **ID**: ieee:10096653
- **Type**: conference
- **Published**: 4-10 June 
- **Authors**: Francesco Binucci, Paolo Banelli
- **PDF**: https://ieeexplore.ieee.org/document/10096653
- **Abstract**: This paper investigates a BER-aware goal-oriented system design, for digital wireless communications, enabling edge-assisted learning applications. Targeting image classification tasks, we exploit banks of encoders at the transmitter, and classifiers at the edge-server that, trained under different BER conditions and exploiting knowledge of the channel state and computation load, let us to dynamically adapt, in a goal-oriented fashion, the size of the data to be transmitted, the M-QAM scheme, and the system BER, to fulfill task-specific performance. Exploiting Lyapunov optimization, we propose a minimum-energy strategy, which trades information rates for BER, under delay and classification accuracy constraints.

## Comparative Analysis of Polar and LDPC Codes in Space and Satellite Communication Systems

- **Status**: ❌
- **Reason**: 메모리 채널에서 표준 5G LDPC vs Polar 성능 비교, 새 디코더/구성 없음(폴라 구성만 최적화)
- **ID**: ieee:10148035
- **Type**: conference
- **Published**: 29 May-2 J
- **Authors**: A. A. Fominykh, A. A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/10148035
- **Abstract**: Satellite and space communication systems have received a lot of attention as crucial transmission frameworks in recent years. In these systems, the signal is mostly degraded by fast amplitude and phase changes (fading), which cause error bursts. Hence, robust error-correcting codes that can handle error bursts are necessary for space and satellite transmissions of good quality. Low-density parity-check (LDPC) codes and polar codes were adopted as coding schemes in the modern 5G communication standard. A lot of research was conducted on their performance over memoryless channels, but their error correction capability over channels with memory is a less researched area. In this study, we examine and compare the error-correcting performance of LDPC codes and polar codes in channels with memory specified by a correlated Rayleigh channel model. We evaluate the error-correcting capabilities of LDPC and polar decoding algorithms in a correlated Rayleigh fading channel with different correlation coefficients. Also, we optimize the construction of the polar code for fading channels and present the simulation results comparing it to the 5G polar code construction.

## Evaluation of Error Probability of Iterative Schemes for Channels with Memory

- **Status**: ❌
- **Reason**: 메모리 채널용 product code 반복복호 성능 비교 — 표준 기법 비교, 떼어낼 새 LDPC 기여 없음
- **ID**: ieee:10148000
- **Type**: conference
- **Published**: 29 May-2 J
- **Authors**: A. A. Ovchinnikov, A. A. Fominykh
- **PDF**: https://ieeexplore.ieee.org/document/10148000
- **Abstract**: The common technique to perform decoding in channels with memory is to use interleaving, which increases both complexity and delay at the receiver. To overcome these limitations, coding scheme adaptation approaches might be used. One of the approaches is the optimization of long error-correcting codes and the modification of the decoder, taking into account the existence of error bursts. Another traditional approach to coding scheme adaptation that combats error bursts is using product codes under an iterative decoding scheme. The component codes themselves are not able to correct error bursts, but the two-dimensional structure and iterative decoding allow for correcting grouping errors. In this paper, we investigate and compare the performance of the described approaches.

## Continuous-Variable Quantum Key Distribution: Background and Perspectives

- **Status**: ❌
- **Reason**: 연속변수 QKD 리뷰 — 양자 보안, LDPC ECC 기법 없음
- **ID**: ieee:10148041
- **Type**: conference
- **Published**: 29 May-2 J
- **Authors**: E. V. Burlakov, A. V. Korobov
- **PDF**: https://ieeexplore.ieee.org/document/10148041
- **Abstract**: The review examines the essential characteristics of continuous-variable quantum key distribution protocols. In these protocols, information is encoded into the complex amplitude of the optical field, which can have a continuous range of values, unlike a qubit. An advantage over many other quantum key distribution protocols is provided by the fact that the practical implementation of these protocols does not require sources and single-photon detectors. Additionally, they offer a relatively high rate of secret key generation. However, continuous-variable protocols require a specific analysis of secrecy and special consideration for the influence of noise that may arise during practical implementation. This presents a broad area for further research.

## Investigation of LoRa Based Signal Code Constructions Noise Immunity

- **Status**: ❌
- **Reason**: LoRa용 비이진(non-binary) LDPC — 비이진 LDPC는 즉시 제외
- **ID**: ieee:10178471
- **Type**: conference
- **Published**: 28-30 June
- **Authors**: V. O. Varlamov, N. A. Kandaurov, N. Y. Liberovskiy +1
- **PDF**: https://ieeexplore.ieee.org/document/10178471
- **Abstract**: Long-range (LoRa) communication systems are actively used to implement the control and telemetry channels of unmanned aerial vehicles, due to its high noise immunity. However, existing solutions provide the main part of noise immunity due to the spreading of data symbols using a chirp modulation with frequency offset corresponding to symbols number, and a Hamming like code is used for encoding. The purpose of this work is to study the potential noise immunity of systems with LoRa modulation when using a non-binary LDPC code with error correction. Due to the implementation of decoding by a posteriori probabilities of receiving symbols, this algorithm allows for an increase potential noise immunity at a constant data transfer rate, which will increase the range of operation of unmanned aerial vehicle control systems.

## LDPC Encoder Identification via Belief Propagation for Integrated Sensing and Communication Systems

- **Status**: ❌
- **Reason**: LDPC 인코더 식별(blind identification), 디코딩/부호설계가 아닌 송신부호 추정 — NAND ECC에 이식할 기법 없음
- **ID**: ieee:10283632
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Hongyu Wang, Fanggang Wang, Yu Liu
- **PDF**: https://ieeexplore.ieee.org/document/10283632
- **Abstract**: Channel coding identification has attracted significant attention since it finds crucial applications in some key techniques for integrated sensing and communication (ISAC), e.g., interference cancellation and adaptive modulation and coding. In this paper, we propose a channel coding identification algorithm for low-density parity-check (LDPC) codes that exploits the belief propagation (BP) algorithm to improve the identification performance in the ISAC system. A maximum likelihood (ML) identifier is developed to determine the unknown LDPC encoder. In contrast to the existing algorithms, a novel log-likelihood function is proposed as the decision metric of the ML identifier, which is characterized by the conditional probabilities of the transmitted symbol. Particularly, these conditional probabilities are calculated accurately via the BP algorithm, enhancing the identification performance. Furthermore, we extend the proposed algorithm to the asynchronous scenario based on the designed decision metric. Numerical results show that the proposed algorithm achieves significant identification performance improvements compared with the existing algorithms.

## The Difficult Road of Expectation Propagation Towards Phase Noise Detection

- **Status**: ❌
- **Reason**: 위상잡음 채널에서 EP 적용 분석, LDPC는 베이스라인이고 떼어낼 ECC 디코더 기여 없음
- **ID**: ieee:10278761
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Giulio Colavolpe, Elisa Conti, Amina Piemontese +1
- **PDF**: https://ieeexplore.ieee.org/document/10278761
- **Abstract**: Expectation Propagation (EP) is a promising framework in message-passing algorithms based on factor-graphs. The inherent ability to combine prior (partial) knowledge of system variables with channel observations suggests that an effective estimation of random channel parameters can be achieved even with a very limited number of pilot symbols, thus increasing the payload efficiency. Yet, the way in which the probability distributions of latent variables (both data and parameters) are combined and projected often requires ad-hoc adjustments to reach satisfactory performance. Here, we apply EP to a classical problem of LDPC-coded transmission on a strong Wiener phase noise channel and discuss how and why, even in the simple case of binary modulation, EP can fail or succeed.

## When Wireless Hierarchical Federated Learning Meets Physical Layer Security: A Finite Blocklength Approach for MIMO Channel

- **Status**: ❌
- **Reason**: 물리계층 보안 + 유한블록길이 federated learning, LDPC는 latency 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:10283538
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Haonan Zhang, Zhiming Yu, Chuanchuan Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/10283538
- **Abstract**: In the authors' previous work, a framework for the wireless hierarchical federated learning (HFL) in the presence of physical layer security (PLS) is established, and a finite blocklength (FBL) approach for the wireless SISO channel is proposed. In this paper, we further propose an FBL approach for the MIMO channel, and show that the proposed scheme almost achieves perfect secrecy without affecting the learning performance of wireless HFL, and the transmission latency of our proposed scheme is significantly shorter than that of classical LDPC code.

## Quantum Annealing-Aided Multi-User Detection: An Application to Uplink Non-Orthogonal Multiple Access

- **Status**: ❌
- **Reason**: 양자어닐링 기반 다중사용자 검출 LLR 계산, NOMA 응용이며 LDPC ECC 이식 기법 없음
- **ID**: ieee:10279631
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Kouki Yonaga, Kenichi Takizawa
- **PDF**: https://ieeexplore.ieee.org/document/10279631
- **Abstract**: A new method to realize computation of the log-likelihood ratio (LLR) in multi-user detection (MUD) by quantum annealing (QA) is proposed herein. One metaheuristic algorithm for solving combinatorial optimization problems is QA. Recently, QA has been applied in various fields to hasten computations. This study specifically examines the application of QA in up-link non-orthogonal multiple access (UL-NOMA) that employs iterative MUD. Our proposed method, QA-aided MUD, uses QA to calculate LLR in iterative MUD. We tested QA-aided MUD with a D-Wave quantum annealer. The error rate analysis demonstrates that QA-aided MUD has comparable performance to that of conventional MUD method. Furthermore, when the annealing time was set to 20 µs, we demonstrated than that the total computation time is 1/10 of the computation time necessary when using a digital computer. We also evaluated the convergence behavior of QA-aided MUD through evolution of mutual information. The results indicate that QA-assisted MUD has almost identical convergence performance to that of the conventional MUD method for LLR calculations.

## Rate-Matched Turbo Autoencoder: A Deep Learning Based Multi-Rate Channel Autoencoder

- **Status**: ❌
- **Reason**: Turbo Autoencoder 신경망 채널코드 rate-matching, LDPC ECC 이식 기법 아님
- **ID**: ieee:10278629
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Linfang Wang, Hamid Saber, Homayoon Hatami +2
- **PDF**: https://ieeexplore.ieee.org/document/10278629
- **Abstract**: Turbo Autoencoder (TAE) is a deep-learning based channel code that demonstrates promising error correction performance. This paper studies the rate-matching problem for TAE and proposes a rate-matched TAE framework. The rate-matched TAE is a single auto-encoder model that can be used for multiple code rates. It matches the code rate of a mother $(3k, k)$ TAE to a desired code of parameters ($n^{\ast}, k^{\ast}$) by using a combination of freezing message bits, repeating code symbols, and puncturing code symbols. We refer to the conventional TAE with message word length $k$ and code length $3k$ as mismatched TAE. The rate-matched TAE shares the same encoder and decoder structure with mismatched TAE but is trained to jointly optimize the performance across multiple rates. We study two important hyper-parameters for the rate-matched TAE: puncturing pattern and training signal-to-noise ratio (SNR) for constituent rates. Three puncturing patterns, namely, head, tail, and uniform puncturing are proposed and evaluated. Training SNRs are determined according to a heuristic method that uses test loss as a performance metric. Our simulation results show that the rate-matched TAE for $k= 100$ and rates $r\in \{0.1, 0.2, \ldots, 0.9\}$ significantly outperforms the mismatched TAE when $r\geq 0.4$.

## Joint Source-Channel Coding for Wireless Image Transmission: A Neural Architecture Search Approach

- **Status**: ❌
- **Reason**: 신경망 기반 JSCC 무선 이미지 전송 (NAS), LDPC ECC 무관 — 떼어낼 채널코딩 기법 없음
- **ID**: ieee:10279680
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Yuchen Yang, Shaowei Wang
- **PDF**: https://ieeexplore.ieee.org/document/10279680
- **Abstract**: In this paper, we propose a joint source-channel coding (JSCC) scheme for wireless image transmission, where the encoder and decoder of the transmission system are implemented by convolutional neural networks. A neural architecture search (NAS) method is introduced to find promising network structures aiming at minimizing the distortion of the target image. Experimental results demonstrate that our proposed scheme, referred to as NAS-JSCC, significantly outperforms the conventional manually designed ones in terms of peak-signal-to-noise ratio in nearly all tested signal-to-noise ratio regions.

## Deep Learning-Based Joint Channel Coding and Frequency Modulation for Low Power Connectivity

- **Status**: ❌
- **Reason**: 딥러닝 기반 채널코딩+주파수변조 결합(JCM) 무선 응용, NAND LDPC 이식 기법 없음
- **ID**: ieee:10278753
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Boxuan Chang, Chenyu Wang, Hun-Seok Kim
- **PDF**: https://ieeexplore.ieee.org/document/10278753
- **Abstract**: Low-power, low-cost wireless communication is a fundamental requirement of Internet-of-Things (IoT) and massive machine-type communication (mMTC). Various low power connectivity standards such as Bluetooth and LoRa adopt non-coherent frequency modulation schemes as they exhibit significantly lower complexity and power consumption compared to coherent in-phase and quadrature (IQ) modulation schemes. In our paper, we propose a deep learning-based joint channel coding and modulation (JCM) scheme for digitally controlled oscillator (DCO)-based frequency modulation. The learned encoder takes an information bit sequence and produces DCO control samples that represent instantaneous frequency to modulate the radio frequency (RF) signal. The learned decoder recovers/decodes information bits from the received noisy samples without any preamble to assist time and frequency synchronization. We train and test the proposed scheme under significant phase noise and carrier frequency offset (CFO) of the DCO to successfully mitigate these practical impairments at the receiver.

## Joint Frequency Offset Compensation and Detection for Multi-User MIMO-OFDM Systems with Frequency Asynchronous User Access

- **Status**: ❌
- **Reason**: MU-MIMO-OFDM CFO 보상/검출 기법, LDPC ECC 자체 기여 없음
- **ID**: ieee:10278608
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Chathura Jayawardena, Konstantinos Nikitopoulos
- **PDF**: https://ieeexplore.ieee.org/document/10278608
- **Abstract**: Multi-user (MU) MIMO-OFDM systems with aggressive spatial multiplexing are promising to enhance throughput and enable massive connectivity. In such systems, residual carrier frequency offsets (CFOs), due to the instability of oscillators and doppler shifts, can substantially degrade the achievable uplink throughput, especially when the number of connected devices becomes large. Existing approaches to mitigate CFOs in MU scenarios, typically involve closed-loop feedback that can result in high signaling overhead and/or significant residual CFO. Being able to compensate for the CFO of the multiple users at the receiver side, can enable the joint transmission of frequency asynchronous users, can obviate the need for high overhead synchronization procedures, can enable the use of cheaper oscillators, and can potentially unlock new user access schemes. However, as we discuss here in detail, compensating for the multiple user CFOs at the receiver is currently impractical due to the corresponding exponential complexity requirements. At the same time, methods that are typically used in single-user MIMO-OFDM systems are inappropriate for MU-MIMO scenarios and, as we show, can result in substantial (e.g., 80%) throughput degradation. To fill this gap, for the first time, we propose a joint CFO compensation and MU detection scheme that can support a large number of spatially transmitted information streams with practical processing complexity and latency requirements. We show that the proposed scheme enables frequency asynchronous user transmission and approaches the performance of perfectly synchronized systems with complexity requirements that are comparable to current MU-MIMO detection schemes that assume perfect synchronization.

## AI/ML Optimized High-Order Modulations

- **Status**: ❌
- **Reason**: ML 기반 고차 변조 constellation 최적화, LDPC는 부수 코딩일 뿐 ECC 기여 없음
- **ID**: ieee:10279091
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Pranav Madadi, Joonyoung Cho, Charlie Jianzhong Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10279091
- **Abstract**: We propose machine learning (ML) based optimization methods and new high order modulations for reliable and high-capacity communications. The widely adopted square quadrature amplitude modulations (QAM) fundamentally exhibit a shaping loss of up to 1.53 dB to the Shannon capacity bound. The proposed modulations obtained through the ML based optimization outperform the square QAMs and other state of-the-art ones by about 1.2 dB and 0.3 dB, respectively, for 1024-ary modulation with LDPC coding. We construct the neural network architecture and training methods to reflect the desired properties of well-performing modulations. This significantly helps in the training convergence of the ML models to a desired optimal state and leads to the modulation constellation and bit to-symbol mapping that reduces the shaping loss to the Shannon capacity bound to a large extent. Moreover, the ML methods enable the development of new optimal modulations for a wide range of target SNR and modulation orders.

## Weight and Trapping Set Distributions for Non-Binary Regular Low-Density Parity-Check Code Ensembles

- **Status**: ❌
- **Reason**: 비이진(non-binary) regular LDPC의 weight/trapping set 분포 — 비이진 LDPC 즉시 제외 규칙
- **ID**: ieee:10206469
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Emna Ben Yacoub
- **PDF**: https://ieeexplore.ieee.org/document/10206469
- **Abstract**: The variances of weight and trapping set distributions of non-binary regular low-density parity-check ensembles are derived. Using the second moment method, bounds on the probabilities that a randomly chosen code from the ensemble has its weight and trapping set distributions close to the ensemble averages are obtained.

## Non Binary LDPC Coded Orthogonal Modulation Schemes based on Non Binary Multilevel Coding

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 코드 설계 — 기준 0번에 의해 즉시 제외 (바이너리 LDPC만 포함)
- **ID**: ieee:10206851
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Jocelyn Bourduge, Charly Poulliat, Benjamin Gadat
- **PDF**: https://ieeexplore.ieee.org/document/10206851
- **Abstract**: Existing error correcting schemes approaching the capacity of orthogonal modulations are mainly resorting to optimized bit-interleaved coded modulation (BICM) schemes with mandatory iterative decoding or to non binary coded coding schemes for which the field order is matched to the modulation order. The latter approach is efficient especially for short codeword lengths but suffers from a high complexity for high modulation orders. In this paper, we study properties of multi-level coding (MLC) schemes for high order orthogonal modulations and propose to consider non binary MLC to naturally address layer reduction. Design of non binary LDPC codes for non binary MLC is then investigated for both the Gaussian and Rayleigh fading channels showing good performance in both asymptotic and finite length regimes.

## Fast Blind Recovery of Linear Block Codes over Noisy Channels

- **Status**: ❌
- **Reason**: 선형블록코드 패리티체크 행렬 blind recovery(GE+검증) — 코드 식별 문제이며 NAND LDPC 디코더/구성/HW 기여 아님
- **ID**: ieee:10206775
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Peng Wang, Yong Liang Guan, Lipo Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10206775
- **Abstract**: This paper addresses the blind recovery of the parity check matrix of an (n, k) linear block code over noisy channels by proposing a fast recovery scheme consisting of 3 parts. Firstly, this scheme performs initial error position detection among the received codewords and selects the desirable codewords. Then, this scheme conducts Gaussian elimination (GE) on a k-by-k full-rank matrix and uses a threshold and the reliability associated to verify the recovered dual words, aiming to improve the reliability of recovery. Finally, it performs decoding on the received codewords with partially recovered dual words. These three parts can be combined into different schemes for different noise level scenarios. The GEV that combines Gaussian elimination and verification has a significantly lower recovery failure probability and a much lower computational complexity than an existing Canteaut-Chabaud-based algorithm, which relies on GE on n-by-n full-rank matrices. The decoding-aided recovery (DAR) and error-detection-&-codeword-selection-&-decoding-aided recovery (EDCSDAR) schemes can improve the code recovery performance over GEV for high noise level scenarios, and their computational complexities remain much lower than the Canteaut-Chabaud-based algorithm.

## Bound on the ML Decoding Error Probability for Coded QAM Signals with Shaping

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC 중심이며 ML 디코딩 오류확률 bound(순수 이론) — 비이진 제외 + 떼어낼 새 디코더/HW 기법 없음
- **ID**: ieee:10206612
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Sander Mikelsaar +1
- **PDF**: https://ieeexplore.ieee.org/document/10206612
- **Abstract**: An approach for estimation of the maximum-likelihood (ML) decoding error probability for coded shaped QAM signals is proposed. It is based on approximation of the squared Euclidean distance spectra of the coded shaped signal constellations. Two variants of shaping used in the communication system with coded QAM signaling are studied: shaping before coding (SBC) and shaping after coding (SAC). First, the new approach is verified by applying it to short codes. Then, it is used to derive a random coding bound on the ML decoding error probability for the ensemble of binary linear codes. Simulation results for the frame error rate (FER) performance of belief-propagation decoding for the optimized nonbinary (NB) quasicyclic (QC)-LDPC codes used with SBC and SAC, as well as the same performance of the binary QC-LDPC block codes in the 5G standard are compared to the new bound.

## Capacity Achieving Codes for an Erasure Queue-channel

- **Status**: ❌
- **Reason**: erasure queue-channel용 인터리빙 wrapper + Polar 편극화; 큐채널 특화 이론으로 NAND 바이너리 LDPC 디코더/구성 새 기여 없음
- **ID**: ieee:10206525
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Jaswanthi Mandalapu, Avhishek Chatterjee, Krishna Jagannathan +1
- **PDF**: https://ieeexplore.ieee.org/document/10206525
- **Abstract**: We consider a queue-channel model that captures the waiting time-dependent degradation of information bits as they wait to be transmitted. Such a scenario arises naturally in quantum communications, where quantum bits tend to decohere rapidly. Trailing the capacity results obtained recently for certain queue-channels, this paper aims to construct practical channel codes for the erasure queue-channel (EQC)—a channel characterized by highly correlated erasures, governed by the underlying queuing dynamics. Our main contributions in this paper are twofold: (i) We propose a generic ‘wrapper’ based on interleaving across renewal blocks of the queue to convert any capacity-achieving block code for a memoryless erasure channel to a capacity-achieving code for the EQC. Next, due to the complexity involved in implementing interleaved systems, (ii) we study the performance of LDPC and Polar codes without any interleaving. We show that standard Arıkan’s Polar transform polarizes the EQC for certain restricted class of erasure probability functions. We also highlight some possible approaches and the corresponding challenges involved in proving the polarization of a general EQC.

## On the Limits of HARQ Prediction for Short Deterministic Codes with Error Detection in Memoryless Channels

- **Status**: ❌
- **Reason**: HARQ decodability prediction 이론 분석 — 떼어낼 LDPC 디코더/HW/코드설계 기여 없음, ML/SPD 예측 한계의 순수 이론 bound
- **ID**: ieee:10206831
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Barış Göktepe, Cornelius Hellge, Tatiana Rykova +2
- **PDF**: https://ieeexplore.ieee.org/document/10206831
- **Abstract**: We provide a mathematical framework to analyze the limits of Hybrid Automatic Repeat reQuest (HARQ) and derive analytical expressions for the most powerful test for estimating the decodability under maximum-likelihood decoding and t-error decoding. Furthermore, we numerically approximate the most powerful test for sum-product decoding. We compare the performance of previously studied HARQ prediction schemes and show that none of the state-of-the-art HARQ prediction is most powerful to estimate the decodability of a partially received signal vector under maximum-likelihood decoding and sum-product decoding. Furthermore, we demonstrate that decoding in general is suboptimal for predicting the decodability.

## Probabilistic Group Testing in Distributed Computing with Attacked Workers

- **Status**: ❌
- **Reason**: 분산컴퓨팅 불량 워커 식별용 group testing + sparse parity-check 코드 — 채널코딩 ECC 디코더 아님, 이식할 LDPC 기법 없음
- **ID**: ieee:10206705
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Sarthak Jain, Martina Cardone, Soheil Mohajer
- **PDF**: https://ieeexplore.ieee.org/document/10206705
- **Abstract**: The problem of distributed matrix-vector product is considered, where the server distributes the task of the computation among n worker nodes, out of which L are compromised (but non-colluding) and may return incorrect results. Specifically, it is assumed that the compromised workers are unreliable, that is, at any given time, each compromised worker may return an incorrect and correct result with probabilities α and 1−α, respectively. Thus, the tests are noisy. This work proposes a new probabilistic group testing approach t o identify the unreliable/compromised workers with $O\left( {\frac{{L\log (n)}}{\alpha }} \right)$ tests. Moreover, using the proposed group testing method, sparse parity-check codes are constructed and used in the considered distributed computing framework for encoding, decoding and identifying the unreliable workers. This methodology has two distinct features: (i) the cost of identifying the set of L unreliable workers at the server can be shown to be considerably lower than existing distributed computing methods, and (ii) the encoding and decoding functions are easily implementable and computationally efficient.

## Capacity-Achieving Sparse Regression Codes via Vector Approximate Message Passing

- **Status**: ❌
- **Reason**: Sparse regression codes + VAMP 디코더의 capacity-achieving 이론 분석 — LDPC ECC 아니고 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:10206691
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Yizhou Xu, YuHao Liu, ShanSuo Liang +4
- **PDF**: https://ieeexplore.ieee.org/document/10206691
- **Abstract**: Sparse regression codes (SPARCs) are a promising coding scheme that can approach the Shannon limit over Additive White Gaussian Noise (AWGN) channels. Previous works have proven the capacity-achieving property of SPARCs with Gaussian design matrices. We generalize these results to right orthogonally invariant ensembles that allow for more structured design matrices. With the Vector Approximate Message Passing (VAMP) decoder, we rigorously demonstrate the exponentially decaying error probability for design matrices that satisfy a certain criterion with the exponentially decaying power allocation. For other spectra, we design a new power allocation scheme to show that the information theoretical threshold is achievable.

## Variable-Length Codes with Bursty Feedback

- **Status**: ❌
- **Reason**: variable-length feedback 코드의 비점근 achievability bound — 순수 이론 bound, 디코더/HW/구성 없음
- **ID**: ieee:10206991
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: James Y. Chen, Recep Can Yavas, Victoria Kostina
- **PDF**: https://ieeexplore.ieee.org/document/10206991
- **Abstract**: We study variable-length codes for point-to-point discrete memoryless channels with noiseless unlimited-rate feed-back that occurs in L bursts. We term such codes variable-length bursty-feedback (VLBF) codes. Unlike classical codes with feedback after each transmitted code symbol, bursty feedback fits better with protocols that employ sparse feedback after a packet is sent and also with half-duplex end devices that cannot transmit and listen to the channel at the same time. We present a novel non-asymptotic achievability bound for VLBF codes with L bursts of feedback over any discrete memoryless channel. We numerically evaluate the bound over the binary symmetric channel (BSC). We perform optimization over the time instances at which feedback occurs for both our own bound and Yavas et al.’s non-asymptotic achievability bound for variable-length stop-feedback (VLSF) codes, where only a single bit is sent at each feedback instance. Our results demonstrate the advantages of richer feedback: VLBF codes significantly outperform VLSF codes at short blocklengths, especially as the error probability ϵ decreases. Remarkably, for BSC(0.11) and error probability 10−10, our VLBF code with L = 5 and expected decoding time N ≤ 400 outperforms the achievability bound given by Polyanskiy et al. for VLSF codes with L = ∞, and our VLBF code with L = 3.

## Belief-Propagation with Quantum Messages for Polar Codes on Classical-Quantum Channels

- **Status**: ❌
- **Reason**: polar code의 양자 메시지 BP(BPQM), 양자 컴퓨터 전용 디코더 — 양자 EC 원칙 제외, 고전 바이너리 LDPC 디코더 아님
- **ID**: ieee:10206723
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Avijit Mandal, S. Brandsen, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/10206723
- **Abstract**: This paper considers the design and decoding of polar codes for general classical-quantum (CQ) channels. It focuses on decoding via belief-propagation with quantum messages (BPQM) and, in particular, the idea of paired-measurement BPQM (PM-BPQM) decoding. Since the PM-BPQM decoder admits a classical density evolution (DE) analysis, one can use DE to design a polar code for any CQ channel and then efficiently compute the trade-off between code rate and error probability. We have also implemented and tested a classical simulation of our PM-BPQM decoder for polar codes. While the decoder can be implemented efficiently on a quantum computer, simulating the decoder on a classical computer actually has exponential complexity. Thus, simulation results for the decoder are somewhat limited and are included primarily to validate our theoretical results.

## Bayes-Optimal Estimation in Generalized Linear Models via Spatial Coupling

- **Status**: ❌
- **Reason**: GLM 신호추정에서 spatially coupled sensing matrix + AMP 추정기, LDPC ECC 코드설계/디코더 기여 아님 — 추정 문제로 이식 가능 ECC 기법 없음
- **ID**: ieee:10206625
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Pablo Pascual Cobo, Kuan Hsieh, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/10206625
- **Abstract**: We consider the problem of signal estimation in a generalized linear model (GLM). GLMs cover many canonical problems in statistical estimation including linear regression and phase retrieval. Recent work has precisely characterized the asymptotic minimum mean-squared error (MMSE) for GLMs with i.i.d. Gaussian sensing matrices. However, in many models there is a significant gap between the MMSE and the performance of the best known feasible estimators. In this work we address this gap by considering GLMs defined via spatially coupled sensing matrices. We propose an efficient approximate message passing (AMP) algorithm for estimation and prove that with a simple choice of spatially coupled design, the MSE of a carefully tuned AMP estimator approaches the asymptotic MMSE. Numerical results show that for finite signal dimensions, spatially coupled designs can yield substantially lower MSE than i.i.d. Gaussian designs when used with AMP algorithms.

## Theoretical analysis of achievable rates for channel-polarized multilevel coding under binary-input AWGN channels

- **Status**: ❌
- **Reason**: 채널분극 다단부호(CP-MLC)의 달성가능 레이트 이론분석(bound)뿐, 디코더/HW/코드구성으로 이어지지 않음
- **ID**: ieee:10206822
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Takeshi Kakizaki, Masanori Nakamura, Fukutaro Hamaoka +1
- **PDF**: https://ieeexplore.ieee.org/document/10206822
- **Abstract**: High-performance and low-complexity forward error correction (FEC) has attracted attention in high-speed optical-fiber communications to reduce the power consumption of digital signal processors (DSPs) for digital coherent systems. Multilevel coding (MLC) provides a solution to reduce the decoding complexity by utilizing soft-decision decoding (SDD) only in low-capacity bit-levels on symbols. However, the amount of reduction for MLC with low-modulation order is lower than the high modulation order because of the large ratio of the least significant bit to the entire code frame. Channel-polarized MLC (CP-MLC) has been reported, which is binary MLC that applies SDD to only a low-capacity channel converted by channel-polarization. Reported simulation results show that CP-MLC can reduce the decoding complexity while mitigating performance degradation. To efficiently implement CP-MLC into the DSPs, theoretical analysis is necessary for the optimal design of CP-MLC. This paper derives and analyzes the CP-MLC capacity, which is the maximum achievable rate, under a binary-input additive white Gaussian noise (BAWGN) channel to determine the decoding performance limit for each ratio of SDD to hard-decision decoding (HDD). Our results show that CP-MLC can provide better upper bounds of performance than HDD and reduce the decoding complexity by decreasing the SDD ratio while mitigating the performance gap with the capacity of the BAWGN channel. We also demonstrate that the theoretical analysis can estimate the performance of CP-MLC applied to practical codes.

## Capacity of Noncoherent FSK with Doppler Frequency Uncertainty

- **Status**: ❌
- **Reason**: non-coherent FSK 용량/소프트 디코더 메트릭 — LDPC는 성능 평가 도구로 부수 언급, NAND에 이식할 새 ECC 기법 없음
- **ID**: ieee:10206962
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Jesús Gómez-Vilardebó, Xavier Mestre, Mònica Navarro +1
- **PDF**: https://ieeexplore.ieee.org/document/10206962
- **Abstract**: This paper studies the capacity of orthogonal M-ary frequency-shift keying modulations with non-coherent detection and Doppler frequency uncertainty at the receiver. The optimal code rates that minimize the energy-per-bit to noise power spectral density ratio required for reliable communications are studied. In addition, optimal and suboptimal metrics for soft-decoders are proposed for non-fading channels with or without average signal and noise power estimation and used to evaluate the performance of LDPC codes.

## How Many Matrices Should I Prepare To Polarize Channels Optimally Fast?

- **Status**: ❌
- **Reason**: polar code 커널/scaling exponent 이론 — LDPC 아님, NAND ECC에 이식할 기법 없음
- **ID**: ieee:10206989
- **Type**: conference
- **Published**: 25-30 June
- **Authors**: Hsin-Po Wang, Venkatesan Guruswami
- **PDF**: https://ieeexplore.ieee.org/document/10206989
- **Abstract**: Polar codes that approach capacity at a near-optimal speed, namely with scaling exponents close to 2, have been shown possible for q-ary erasure channels (Pfister and Urbanke), the BEC (Fazeli, Hassani, Mondelli, and Vardy), all BMS channels (Guruswami, Riazanov, and Ye), and all DMCs (Wang and Duursma). There is, nevertheless, a subtlety separating the last two papers from the first two, namely the usage of multiple dynamic kernels in the polarization process, which leads to increased complexity and fewer opportunities to hardware-accelerate. This paper clarifies this subtlety, providing a tradeoff between the number of kernels in the construction and the scaling exponent. We show that the number of kernels can be bounded by O(ℓ3/µ−1) where µ is the targeted scaling exponent and ℓ is the kernel size. In particular, if one settles for scaling exponent approaching 3, a single kernel suffices, and to approach the optimal scaling exponent of 2, about $O(\sqrt \ell )$ kernels suffice.

## Radio Planning of Using Both 5G and 6G Radio Plannings for Mobile Broadband Services

- **Status**: ❌
- **Reason**: 5G/6G 기지국 무선 망 설계 — LDPC/ECC 무관
- **ID**: ieee:10212866
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Supachart Chinkhong, Pasu Kaewplung
- **PDF**: https://ieeexplore.ieee.org/document/10212866
- **Abstract**: In the near future, 6G technology will play a significant role in broadband mobile communication. 6G aims to provide services with data rates up to Tbps and low latency. The introduction of 6G technology will help alleviating traffic congestion during periods of high usage by many devices. In the future, services that require even higher data rates, such as Virtual Reality (VR), Extended Reality (XR), and holograms, 6G technology will be possible to support these services effectively. The objective of this paper aims to propose an approach for the radio planning using base stations of both 5G and 6G radio access networks that should be installed in a service area. In this paper, a 5G and 6G radio planning achieved by considering based on the total data rate of use cases for mobile broadband service, data rate, and coverage area of the base station for both 5G and 6G. Each position of the base station and the coverage area are shown in a sample area, which is a dense urban in Siam Square shopping center Bangkok, Thailand, by using 5G base stations to cover sample area, and use 6G base stations in locations for ultra-high speed use cases. The result can be used to analyze the preliminary network installation to establish the base station for extending the service area in the future.

## Adaptive Group Based Symbol Flipping Decoding Algorithm

- **Status**: ❌
- **Reason**: non-binary LDPC symbol-flipping 디코더 — 비이진 LDPC 제외
- **ID**: ieee:10200963
- **Type**: conference
- **Published**: 20-23 June
- **Authors**: Waheed Ullah, Dushantha Nalin K. Jayakody, Fengfan Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/10200963
- **Abstract**: This paper introduces an adaptive technique for grouping variable nodes in decoding non-binary LDPC codes that involve symbol flipping. The technique considers both the individual symbol reliability and majority-based voting when grouping variable nodes in each iteration. Groups are formed based on the cumulative density of the variable nodes, with the least reliable variable nodes given the highest priority. The decoding algorithm then proceeds to decode subsequent groups in order of decreasing priority. The results of numerical analysis demonstrate that this approach strikes a balance between computational complexity and bit error rate performance, making it suitable for various applications, such as data storage and mobile networks.

## Efficient Power Allocation in Coded MIMO Systems

- **Status**: ❌
- **Reason**: LDPC-MIMO 전력할당 딥러닝, LDPC는 베이스라인이고 떼어낼 디코더/코드 기법 없음 — 무선 응용 특이
- **ID**: ieee:10199200
- **Type**: conference
- **Published**: 20-23 June
- **Authors**: Haochen Wu, Ke Ma, Yang Ming +2
- **PDF**: https://ieeexplore.ieee.org/document/10199200
- **Abstract**: Multiple-input multiple-output (MIMO) and low-density parity check (LDPC) codes are two of the fundamental technologies in the fifth-generation (5G) networks, where an efficient power allocation scheme is desired to minimize the bit error rate (BER) of the LDPC-coded MIMO system. However, the conventional power allocation methods do not take into account the constraint of modulation and coding scheme (MCS), which may degrade the BER performance. To solve this issue, we propose a deep learning based method to predict the efficient power allocation scheme in coded MIMO systems. Specifically, a neural network is built to learn the complex BER-SNR function to derive the power allocation ratio between the parallel MIMO streams, where the training label is acquired based on the exhaustive searching algorithm. Simulation results show that our proposed method could achieve better BER performance than its conventional counterparts.

## Packet Encoding Based on Encrypted Raptor Code for Secure Internet of Vehicles Communication

- **Status**: ❌
- **Reason**: 암호화 Raptor(fountain+LDPC) 보안 인코딩, 비-LDPC fountain·보안 — 제외
- **ID**: ieee:10199567
- **Type**: conference
- **Published**: 20-23 June
- **Authors**: Junzhe Cheng, Dongyang Xu, Gautam Srivastava +1
- **PDF**: https://ieeexplore.ieee.org/document/10199567
- **Abstract**: The Internet of Vehicles (IoV) industry has developed rapidly in recent years. However, the information security of IoV needs more attention. The use of cross-layer secure transmission technology can improve the security of IoV communication, but the existing cross-layer schemes have some shortcomings. To this end, we propose a packet encoding scheme based on encrypted Raptor codes to improve the secure capacity of IoV communication by utilizing fountain codes and physical layer Low-density parity-check (LDPC) codes. Specifically, we choose Raptor codes which combine LDPC codes and fountain codes for secure encoding. With a sparser degree distribution, Raptor codes make decoding faster and more accurate at the legitimate receiver. In the transmission, the transmitter encrypts and sends the coding control information corresponding to the packets received by the legitimate receiver, rather than sending the generating matrix directly. We found that confidentiality can be improved by this encrypting. The simulation results show that the proposed scheme has higher security than the comparison schemes.

## Physical Layer Authentication in Private Campus Networks based on Machine Learning

- **Status**: ❌
- **Reason**: 물리계층 인증 ML, LDPC ECC 무관 — 보안/무선
- **ID**: ieee:10201068
- **Type**: conference
- **Published**: 20-23 June
- **Authors**: Nandish P. Kuruvatti, Sachinkumar B. Mallikarjun, Sai Charan Kusumapani +2
- **PDF**: https://ieeexplore.ieee.org/document/10201068
- **Abstract**: Mobile communication is in the deployment phase of its fifth generation (5G) technology standards and the research activities have begun toward the sixth generation (6G) of mobile communication systems. Private campus networks (PCNs) serving a specific use case of the vertical industries (e.g., smart factory) are commonplace in the 5G and will continue to be the same in the future. Facilitating secure operations in such a PCN is of the utmost priority. Physical layer security (PLS) is one of the most promising security paradigms for the present and future generations of mobile communication systems, which works on the principle of channel reciprocity. In this paper, PLS concepts are applied to design authentication schemes for the PCN. Measurements of the physical layer are carried out in a live PCN and a grid-wise radio environment map is constructed. A lookup table-based as well as Machine learning (Decision trees, Random Forest) based PHY packet authentication schemes are designed and evaluated to showcase their applicability in providing efficient authentication in the PCN environment.

## LDPC and ultra-massive multi-input multi-output for secrecy in 6G

- **Status**: ❌
- **Reason**: 6G PLS 보안 + erasure LDPC를 표준대로 사용, 새 디코더/구성/HW 기여 없음, 보안 도메인
- **ID**: ieee:10182942
- **Type**: conference
- **Published**: 19-23 June
- **Authors**: Djedjiga Benzid, Michel Kadoch
- **PDF**: https://ieeexplore.ieee.org/document/10182942
- **Abstract**: Sixth generation (6G) wireless networks are a promising technology for meeting the extreme demands of 2030 of high data rates, ultra-low latency, and ultra-reliability. However, supporting the services of 6G networks requires advanced security mechanisms. In addition, 6G has a rapid and simple means of accessing the channel because of its broadcast transmission method, which makes it prone to eavesdropping attacks. Physical-layer security (PLS) is predicted to be a suitable method of achieving network security, in which the characteristics and advantages of wireless networks are exploited. PLS technologies include wiretap code designs, artificial noise injection (jamming), multi-input multi-output (MIMO)(beamforming), and physical-layer authentication. This paper proposes an erasure corrector code, namely a low-density parity check (LDPC), and ultra-massive MIMO (UMMIMO) to fix this issue. The simulation results show that our solution guarantees data secrecy, even against eavesdroppers with many antennas and considerable decoding resources, while reducing power consumption, consequently supporting secure, green transmission.

## Code-Aided Carrier Synchronization with Adjustable Operating Ranges for Satellite Communications

- **Status**: ❌
- **Reason**: 위성 code-aided 캐리어 동기화 알고리즘 — LDPC 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:10182805
- **Type**: conference
- **Published**: 19-23 June
- **Authors**: Taiyi Chen, Yafeng Zhan, Haoran Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/10182805
- **Abstract**: Due to limited link resources and increasing demand for data transmission, receivers in satellite communications are required to achieve carrier synchronization, demodulation, and decoding operations at low signal-to-noise ratio (SNR) conditions, thus making full use of the link budget. In this context, code-aided (CA) carrier synchronization is a promising solution, synchronizing low-SNR signals without additional pilot overhead. However, traditional CA carrier synchronization suffers from a narrow operating range and, in practice, performs poorly in tracking dynamic signals with large Doppler frequency offsets. To solve such a problem, we presents a low-complexity algorithm to improve the operating range of CA carrier synchronization. This algorithm tolerates large carrier offsets through coarse correction based on a confidence metric function (CMF). Additionally, a candidate list mechanism is introduced to reduce the computational overhead. The operating range of the algorithm can be adjusted by varying its parameters to sustain carrier recovery under different dynamic scenarios. Simulations verify the effectiveness of the proposed algorithm.

## Evaluation of LTE-based 5G Terrestrial Broadcasting Systems for Mobile Reception Based on Average Mutual Information Analysis

- **Status**: ❌
- **Reason**: LTE 5G 지상파 방송 인터리브 깊이/모바일 수신 평가, LDPC 부수 언급뿐
- **ID**: ieee:10211111
- **Type**: conference
- **Published**: 14-16 June
- **Authors**: Zhitong He, Kewu Peng, Boran Sun +4
- **PDF**: https://ieeexplore.ieee.org/document/10211111
- **Abstract**: LTE-based 5G terrestrial broadcast, which is standardized in 3GPP Rel-14 and Rel-16, is one of the two technical evolutional-routes of 5G broadcast. In physical layer, the mobile reception performance loss of LTE-based 5G terrestrial broadcast majorly stems from numerology, coded modulation, interleave depth and channel estimation. Among these factors, interleave depth directly affects the mobile reception performance at different speeds, and low-speed mobile reception puts forward higher requirements of interleave depth. In this paper, the typical configuration of LTE-based 5G terrestrial broadcast is selected, and how interleave depth influences the mobile reception performance is revealed based on the analysis of average mutual information (AMI) probability density distribution and outage probability over small-scale Rayleigh fading channels. The analysis results show that the mobile reception performance could be significantly improved by appropriately increasing the interleave depth. Hence increasing interleave depth could be considered for the evolution of LTE-based 5G terrestrial broadcast towards the next generation mobile broadcast systems.

## Performance Evaluation of 5G MBS for Terrestrial Broadcasting Scenarios

- **Status**: ❌
- **Reason**: 5G NR-MBS 지상파 방송 성능 평가(CP 길이 등), 떼어낼 LDPC 기법 없음
- **ID**: ieee:10211121
- **Type**: conference
- **Published**: 14-16 June
- **Authors**: Seok-Ki Ahn, Sungjun Ahn, Sesh Simha +5
- **PDF**: https://ieeexplore.ieee.org/document/10211121
- **Abstract**: This paper provides performance evaluations of 5G NR-MBS for terrestrial broadcasting environments. The physical layer performance of NR-MBS is analyzed through theoretical point of view and block error rate (BLER) performance over high-power high-tower (HPHT) infrastructure. Considering the future development of NR-MBS for terrestrial broadcasting services, this paper focuses on the performance evaluation of NR unicast numerology including length of cyclic prefix (CP) over HPHT single frequency network (SFN) environments. Specifically, it is demonstrated that the effect of CP length on the decoding performance depends on the transmission rate and the quality of channel estimation over HPHT SFN environments.

## A Proposal for Quality Evaluation Method of Ultra-high Order QAM Signal

- **Status**: ❌
- **Reason**: 초고차 QAM 신호 품질 평가(MER) 방법, LDPC/ECC 무관
- **ID**: ieee:10211314
- **Type**: conference
- **Published**: 14-16 June
- **Authors**: Yuki Hirabayashi, Shingo Asakura, Kohei Kambara
- **PDF**: https://ieeexplore.ieee.org/document/10211314
- **Abstract**: Modulation error ratio (MER) is one of the indexes to evaluate received signal quality, and MER measuring functions have been widely installed in digital signal analyzers. However, it is inconvenient to use the MER value for evaluating the quality of an ultra-high order quadrature amplitude modulation (QAM) signal since the MER value is different from the actual signal quality depending on a relatively higher noise level. In this paper, we propose a novel method to solve this problem and evaluate its efficiency for Advanced Integrated Services Digital Broadcasting-Terrestrial (Advanced ISDB-T), a new digital terrestrial television broadcasting system. The proposed method was verified by a computer simulation and laboratory test using a prototype analyzer. The results show the effectiveness of the proposed method.

## A 2.35 Gb/s/mm2 (7440, 6696) NB-LDPC Decoder over GF(32) using Memory-Reduced Column-Wise Trellis Min-Max Algorithm in 28nm CMOS Technology

- **Status**: ❌
- **Reason**: GF(32) 비이진(NB-)LDPC 디코더 — 비이진 LDPC는 명시적 제외 대상
- **ID**: ieee:10185244
- **Type**: conference
- **Published**: 11-16 June
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/10185244
- **Abstract**: For the cost-efficient non-binary low-density parity-check (NB-LDPC) decoder realization, this paper presents a column-wise trellis min-max (CW-TMM) algorithm, greatly relaxing the sorter costs of the previous TMM method without lowering the error-correcting capability. The message compression is used to the trellis-based decoder for the first time, minimizing the memory requirements even for long NB-LDPC codes. In addition, novel circuit-level optimizations are developed to further remove the redundant computing units in the previous works. As a result, the prototype (7440, 6696) decoder over GF(32) in 28 nm CMOS process achieves the normalized area-efficiency of 2.35 Gb/s/mm2, saving the decoding complexity and the on-chip memory size by 63% and 54%, respectively.

## Synchronization Algorithms from High-Rate LDPC Codes for DNA Data Storage

- **Status**: ❌
- **Reason**: DNA 저장용 동기화 알고리즘(삽입/삭제 정정·consensus), high-rate LDPC는 부수적 — 떼어낼 LDPC 디코더/HW/구성 기법 없음
- **ID**: ieee:10167916
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Belaïd Hamoum, Aref Ezzeddine, Elsa Dupraz
- **PDF**: https://ieeexplore.ieee.org/document/10167916
- **Abstract**: Data storage on synthetic DNA is a novel technique that offers improved durability and density compared to conventional storage supports. Current challenges in the practical implementation of DNA data storage include the high cost of DNA synthesis and the significant amount of errors introduced during DNA sequencing. These errors are not only substitutions but also insertions and deletions, which compromise the sequence synchronization and cannot be corrected using conventional error correction methods. To overcome these issues, this paper proposes an error correction scheme that prioritizes the reduction of DNA synthesis costs through the use of high rate codes. The proposed solution utilizes a consensus algorithm that leverages the inherent redundancy in the output data, followed by a proposed synchronization method for correcting residual insertions and deletions after the consensus. Numerical results show the effectiveness of the proposed method at correcting a large amount of errors, while maintaining a high coding rate.
