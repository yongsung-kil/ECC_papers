# IEEE Xplore — 2023-04


## GaussianSource Coding Based on P-LDPC Code

- **Status**: ❌
- **Reason**: Gaussian 소스 코딩(압축, lossy source coding) 기반 P-LDPC. 채널코딩 ECC 아님, 소스코딩 제외 대상.
- **ID**: ieee:10045706
- **Type**: journal
- **Published**: April 2023
- **Authors**: Dan Song, Jinkai Ren, Lin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10045706
- **Abstract**: A lossy source coding system based on the protograph low-density parity-check (P-LDPC) code is proposed for Gaussian source compression. In the proposed system, the conventional belief propagation (BP) algorithm is modified to be a concatenated BP-inverse BP (BP- $i$ BP) for encoding and decoding, where the  $i$ BP is constructed by a fully-connected layer of a neural network. Compared to the existing approximate message passing algorithm, the proposed BP- $i$ BP realizes a float-to-bit compression with low complexity for arbitrary Gaussian sources. The BP- $i$ BP is implemented based on the linking relation of the protograph; therefore, it is necessary to optimally design the protograph to obtain better rate-distortion function (RDF) performance. Regarding the coding optimal procedure, a mutual information iteration convergence (MIIC) algorithm is designed as the optimal criterion to determine the source P-LDPC code with minimum distortion. Inspired by the plane construction of quantum stabilizer code, a lattice topological splicing (LTS) algorithm is proposed for regularly building the protograph to reduce the code searching complexity. By using the MIIC and the LTS algorithms, the BP- $i$ BP based on the designed P-LDPC code maintains good distortion performance close to the RDF limit.

## Delayed Bit-Interleaved Coded Transmission for Spatial Modulation

- **Status**: ❌
- **Reason**: 지연 BICM 공간변조용 LDPC 코드 변조; 통신 변조 특이적, LDPC 부호 자체는 표준, 떼어낼 디코더/구성 기여 없음
- **ID**: ieee:10038596
- **Type**: journal
- **Published**: April 2023
- **Authors**: Yang Liu, Huiqin Du, Shancheng Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/10038596
- **Abstract**: It has been shown that delayed bit-interleaved coded modulation (BICM) performs better than the original BICM in some scenarios. This letter is intended to enhance the performance of low-density parity-check (LDPC) coded spatial modulation. To this end, we present the delayed bit-interleaved coded spatial modulation (DBICSM) when LDPC codes are employed. The resulting transmission scheme is termed LDPC-DBICSM. Firstly, we present the encoding structure of the LDPC-DBICSM. Secondly, we present a non-iterative decoder that works only on two blocks of received sequences for the LDPC-BICSM. Thirdly, we present an estimated lower bound on the performance of the LDPC-DBICSM. Finally, we present extensive simulation results to show the performance advantages of the LDPC-DBICSM when compared to the LDPC-BICSM. Particularly, a performance gain of about 1.25 dB is obtained at a bit error rate (BER) of  $10^{-8}$ .

## Trapping and Absorbing Set Enumerators for Nonbinary Protograph-Based Low-Density Parity-Check Code Ensembles

- **Status**: ❌
- **Reason**: 비이진(nonbinary) 프로토그래프 LDPC의 trapping/absorbing set enumerator — 비이진이므로 즉시 제외
- **ID**: ieee:10032599
- **Type**: journal
- **Published**: April 2023
- **Authors**: Emna Ben Yacoub, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/10032599
- **Abstract**: The finite-length trapping and (elementary) absorbing set enumerators for nonbinary protograph-based LDPC code ensembles are derived. Both constrained and unconstrained edge labeling approaches are considered. The normalized logarithmic asymptotic distributions of trapping and (elementary) absorbing sets are obtained through an efficient method that requires solving a system of equations. Using these results, the asymptotic distributions of trapping and (elementary) absorbing sets are evaluated for some example nonbinary protograph-based LDPC code ensembles.

## Efficient BCH Code Encoding and Decoding Algorithm With Divisor-Distance-Based Polynomial Division for STT-MRAM

- **Status**: ❌
- **Reason**: STT-MRAM용 BCH 부호 인코딩/디코딩(다항식 나눗셈). LDPC 아닌 BCH, 떼어낼 LDPC 기법 없음.
- **ID**: ieee:9696257
- **Type**: journal
- **Published**: April 2023
- **Authors**: Li Zhang, Yitao Ma, Tetsuo Endoh
- **PDF**: https://ieeexplore.ieee.org/document/9696257
- **Abstract**: Error-correcting codes (ECCs) are important and widely implemented in memories from high-speed static random-access memory (SRAM) cache to high-volume 3-D NAND. However, from the viewpoint, ECC technology of spin-transfer torque magnetic random access memory (STT-MRAM) is not established yet, as the operation speed of STT-MRAM is higher than dynamic random-access memory (DRAM)/3-D NAND, and its volume is larger than SRAM. Moreover, it is difficult for existing ECCs to guarantee low latency and low hardware complexity while achieving high error correction capabilities. In this work, the time efficiency of both encoding and decoding of Bose–Chaudhuri–Hocquenghem (BCH) codes for STT-MRAM is optimized. A divisor-distance-based (DDB) polynomial division method is proposed to accelerate the polynomial division of BCH encoding and decoding. The DDB division method leverages the characteristics of the divisor polynomial to achieve parallel-processing for multibit on the word-line in the same block in a simple manner. The DDB polynomial division method can execute in multiple approaches with different hardware architectures, where the DDB divider with a parallel multiplier (PM) has the lowest hardware complexity. To demonstrate the superiority of the proposed algorithm: The time efficiency of the proposed BCH codes is successfully verified in software, the proposed algorithm increases the time efficiency of encoding by more than ten times, and the decoding increased by about 10%. The hardware implementation of the proposed DDB divider is presented for improving the hardware complexity, the PM-type DDB divider architecture eliminates the large memory block of the traditional lookup table (LUT) type parallel divider.

## Recursive Decoding of Reed-Muller Codes Starting With the Higher-Rate Constituent Code

- **Status**: ❌
- **Reason**: Reed-Muller 부호 재귀 리스트 디코딩(automorphism/permutation). RM 전용 Plotkin 구조 의존, LDPC 이식성 없음.
- **ID**: ieee:9845388
- **Type**: journal
- **Published**: April 2023
- **Authors**: Mikhail Kamenev
- **PDF**: https://ieeexplore.ieee.org/document/9845388
- **Abstract**: Recursive list decoding of Reed-Muller (RM) codes, with moderate list size, is known to approach maximum-likelihood (ML) performance of short length  $(\leq 256)$  RM codes. Recursive decoding employs the Plotkin construction to split the original code into two shorter RM codes with different rates. In contrast to the standard approach which decodes the lower-rate code first, the method in this paper decodes the higher-rate code first. This modification enables an efficient permutation-based decoding technique, with permutations being selected on the fly from the automorphism group of the code using soft information from a channel. Simulation results show that the error-rate performance of the proposed algorithms, enhanced by a permutation selection technique, is close to that of the automorphism-based recursive decoding algorithm with similar complexity for short RM codes, while our decoders perform better for longer RM codes. In particular, it is demonstrated that the proposed algorithms achieve near-ML performance for short RM codes and for RM codes of length  $2^{m}$  and order  $m-3$  with reasonable complexity.

## Codebook Mismatch can be Fully Compensated by Mismatched Decoding

- **Status**: ❌
- **Reason**: mismatched decoding 순수 정보이론(error exponent, capacity). 디코더/HW/구성으로 안 이어지는 이론 bound.
- **ID**: ieee:9966730
- **Type**: journal
- **Published**: April 2023
- **Authors**: Neri Merhav, Georg Böcherer
- **PDF**: https://ieeexplore.ieee.org/document/9966730
- **Abstract**: We consider an ensemble of constant composition codes that are subsets of linear codes: while the encoder uses only the constant-composition subcode, the decoder operates as if the full linear code was used, with the motivation of simultaneously benefiting both from the probabilistic shaping of the channel input (to achieve higher rates) and from the linear structure of the code (to allow for lower complexity practical decoding). We prove that the codebook mismatch can be fully compensated by using a mismatched additive decoding metric that achieves the random coding error exponent of (non-linear) constant composition codes. As the coding rate tends to the mutual information, the optimal mismatched metric approaches the maximum a posteriori probability (MAP) metric, showing that codebook mismatch with MAP metric is capacity-achieving for the optimal input assignment.

## Multicarrier Acoustic Communications in Multiuser and Interference-Limited Regimes

- **Status**: ❌
- **Reason**: 다중반송파 수중 음향통신; LDPC는 부수 언급 코딩, 통신 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:10035752
- **Type**: journal
- **Published**: April 2023
- **Authors**: Zhengnan Li, Milica Stojanovic
- **PDF**: https://ieeexplore.ieee.org/document/10035752
- **Abstract**: In this article, we address the design of a multicarrier communication system based on orthogonal frequency-division multiplexing and direct sequence spread spectrum. The design targets operation in the low-signal-to-noise-ratio regimes and multiuser settings. Specifically, coding is employed across carriers such that channel estimation and signal detection are coupled. We consider both coherent and differentially coherent detection and extend the principles to multichannel reception. A custom-designed frequency synchronization technique is proposed to counteract the motion-induced Doppler frequency shifting effect. Using the recordings from the 2010 Mobile Acoustic Communication Experiment, where signals were transmitted in the 10.5–15.5-kHz acoustic band in shallow water, with relative motion up to 1.5 m/s, we demonstrate the system performance in terms of the mean squared error and bit error rate in data detection. Further employing Polar and low-density parity-check coding, we show that the proposed methods provide excellent performance while maintaining low computational complexity, making them suitable for a practical implementation.

## Frequency-Domain RF Self-Interference Cancellation for In-Band Full-Duplex Communications

- **Status**: ❌
- **Reason**: 무선 풀듀플렉스 RF 자기간섭 제거 필터 기법, LDPC/ECC와 무관.
- **ID**: ieee:9913884
- **Type**: journal
- **Published**: April 2023
- **Authors**: Zhihong Hunter Hong, Liang Zhang, Wei Li +9
- **PDF**: https://ieeexplore.ieee.org/document/9913884
- **Abstract**: Wireless backhaul has recently gained a significant amount of interest as a cost-effective solution in comparison with conventional backhaul technologies with dedicated microwave links or fiber optics. Self-interference cancellation (SIC) is an enabling technology that allows wireless backhaul to operate in the more spectrum-efficient in-band full-duplex (IBFD) operation mode instead of the out-of-band mode. Compared to Wi-Fi IBFD transceivers, wireless in-band backhaul systems face some unique challenges, such as significantly higher transmission power and much larger propagation delay spread for the self-interference signal, especially in the low-frequency bands under 1 GHz, which often prevent accurate SIC performance. The SIC is often implemented with an interference-cancelling filter, where the filter weights are essentially the channel estimates of the self-interference signals. In this paper, a frequency-domain Radio Frequency (RF) SIC (RF-SIC) framework with a novel filter weight optimization algorithm is proposed to tackle the challenges of wireless in-band backhaul. The proposed RF-SIC does not require a dedicated training phase which needs to stop the transmission of the backhaul signal. Moreover, it has the capability of tracking the self-interference channel variation since the filter weights are updated in a block-by-block fashion.

## Reconfigurable Intelligent Surface-Aided $M$-Ary FM-DCSK System: A New Design for Noncoherent Chaos-Based Communication

- **Status**: ❌
- **Reason**: RIS 기반 카오스 변조(FM-DCSK) 무선통신 시스템 설계, LDPC/ECC와 무관
- **ID**: ieee:9970371
- **Type**: journal
- **Published**: April 2023
- **Authors**: Huan Ma, Yi Fang, Pingping Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9970371
- **Abstract**: In this paper, we propose two reconfigurable intelligent surface-aided $M$-ary frequency-modulated differential chaos shift keying (RIS-$M$-FM-DCSK) schemes. In scheme I, the RIS is regarded as a transmitter at the source to incorporate the $M$-ary phase-shift-keying ($M$-PSK) symbols into the FM chaotic signal and to reflect the resultant $M$-ary FM chaotic signal toward the destination. The information bits of the source are carried by both the positive/negative state of the FM chaotic signal and the $M$-PSK symbols. In scheme II, the RIS is treated as a relay so that both the source and relay can simultaneously transmit their information bits to the destination. The information bits of the source and relay are carried by the positive/negative state of the FM chaotic signal and $M$-PSK symbols generated by the RIS, respectively. The proposed RIS-$M$-FM-DCSK system has an attractive advantage that it does not require channel state information for detection, thus avoiding complex channel estimation. Moreover, we derive the theoretical expressions for bit error rates (BERs) of the proposed RIS-$M$-FM-DCSK system with both scheme I and scheme II over multipath Rayleigh fading channels. Simulations results not only verify the accuracy of the theoretical derivations, but also demonstrate the superiority of the proposed system. The proposed RIS-$M$-FM-DCSK system is a promising low-cost, low-power, and high-reliability alternative for wireless communication networks.

## Quantum Algorithm for Higher-Order Unconstrained Binary Optimization and MIMO Maximum Likelihood Detection

- **Status**: ❌
- **Reason**: 양자 알고리즘(Grover) + MIMO ML 검출, HUBO 최적화. LDPC 무관, 양자 전용 개념 의존.
- **ID**: ieee:10044091
- **Type**: journal
- **Published**: April 2023
- **Authors**: Masaya Norimoto, Ryuhei Mori, Naoki Ishikawa
- **PDF**: https://ieeexplore.ieee.org/document/10044091
- **Abstract**: In this paper, we propose a quantum algorithm that supports a real-valued higher-order unconstrained binary optimization (HUBO) problem. This algorithm is based on the Grover adaptive search that originally supported HUBO with integer coefficients. Next, as an application example, we formulate multiple-input multiple-output maximum likelihood detection as a HUBO problem with real-valued coefficients, where we use the Gray-coded bit-to-symbol mapping specified in the 5G standard. The proposed approach allows us to construct an efficient quantum circuit for the detection problem and to analyze specific numbers of required qubits and quantum gates, whereas other conventional studies have assumed that such a circuit is feasible as a quantum oracle. To further accelerate the quantum algorithm, we also derive a probability distribution of the objective function value and determine a unique threshold to sample better states. Assuming a future fault-tolerant quantum computing, our proposed algorithm has the potential for significantly reducing query complexity in the classical domain and providing a quadratic speedup in the quantum domain.

## Single-Photon-Memory Measurement-Device-Independent Quantum Secure Direct Communication—Part I: Its Fundamentals and Evolution

- **Status**: ❌
- **Reason**: 양자 보안 직접통신(QSDC) 리뷰. 양자 보안, LDPC 무관.
- **ID**: ieee:10049402
- **Type**: journal
- **Published**: April 2023
- **Authors**: Xiang-Jie Li, Dong Pan, Gui-Lu Long +1
- **PDF**: https://ieeexplore.ieee.org/document/10049402
- **Abstract**: Quantum secure direct communication (QSDC) has attracted a lot of attention, which exploits deep-rooted quantum physical principles to guarantee unconditional security of communication in the face of eavesdropping. We first briefly review the fundamentals of QSDC, and then present its evolution, including its security proof, its performance improvement techniques, and practical implementation. Finally, we discuss the future directions of QSDC.

## Attention-Empowered Residual Autoencoder for End-to-End Communication Systems

- **Status**: ❌
- **Reason**: 엔드투엔드 통신용 어텐션 잔차 오토인코더; 채널 오토인코더로 LDPC ECC 디코더/구성과 무관
- **ID**: ieee:10042061
- **Type**: journal
- **Published**: April 2023
- **Authors**: Min Lu, Bin Zhou, Zhiyong Bu
- **PDF**: https://ieeexplore.ieee.org/document/10042061
- **Abstract**: Channel autoencoders adopt neural networks to represent and optimize previous block-driven communication systems from an end-to-end perspective. The existing deep fully connected autoencoder needs retraining when the input length of bit sequences changes since it can only handle fixed-length data. Convolutional neural network (CNN)-based autoencoder can accept arbitrary lengths and is widely adopted. But it has limitations in 1) error floor in high signal-to-noise ratio (SNR) regions, and 2) poor performance against interference. Therefore, we first adopt a residual attention module to enhance the representation ability of the autoencoder, where channel and spatial attention focus on finding fine-grained clues between signals and noise. An adaptive data-flow merging scheme for demapper is further proposed to satisfy dynamic environments. Simulation results show that the proposed method can achieve great gains in coded and uncoded transmission scenarios. Our method is robust and generalizable against error floor and burst interference, as compared to a conventional system.

## Two-Stage Constructions for the Rate-Compatible Shortened Polar Codes

- **Status**: ❌
- **Reason**: Polar 부호 rate-compatible shortening 구성. Polar 전용, LDPC 무관.
- **ID**: ieee:9906049
- **Type**: journal
- **Published**: April 2023
- **Authors**: Chunjie Li, Haiqiang Chen, Zelin Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/9906049
- **Abstract**: In this paper, we propose the two-stage constructions for the rate-compatible shortened polar (RCSP) codes. For the Stage-I construction, the shortening pattern and the frozen bit are jointly designed to make the shortened bits be completely known by the decoder. Besides, a distance-greedy algorithm is presented to improve the minimum Hamming distance of the codes. To design the remaining Stage-II frozen bits, three different construction algorithms are further presented, called the Reed-Muller (RM) construction, the Gaussian Approximation (GA) construction, and the RM-GA construction. Then we give the row weight distribution numerical results of the generator matrix after the Stage-I and Stage-II constructions, which shows that the proposed constructions can efficiently increase the minimum Hamming distance. Simulation results show that the proposed RCSP codes have excellent frame error rate (FER) performances at different code lengths and code rates. More specifically, the RM-GA construction performs best and can achieve at most 0.8 dB gain compared to the Wang14 and the quasi-uniform puncturing (QUP) schemes. The RM construction is designed completely by the distance-constraint without channel evaluation thus has the simplest structure. Interestingly, it still has better FER performance than the existing shortening/puncturing schemes, especially at high signal noise ratio (SNR) region.

## Deep Learning for Waveform Level Receiver Design With Natural Redundancy

- **Status**: ❌
- **Reason**: 딥러닝 파형레벨 수신기(동기화+복조, NR 활용). LDPC 디코더 아님, 통신 수신기 특이적.
- **ID**: ieee:9966932
- **Type**: journal
- **Published**: April 2023
- **Authors**: Zhaorui Zhu, Caiyao Shen, Hongyi Yu +3
- **PDF**: https://ieeexplore.ieee.org/document/9966932
- **Abstract**: High-speed information transmission system demands more powerful communication receivers. In this paper, we integrate deep learning algorithms into constructing waveform level receiver, which is capable of harnessing natural redundancy (NR) in raw message sources. Owing to end-to-end learning paradigm of neural network (NN), the proposed NN receiver can accomplish joint symbol timing synchronization and demodulation based on oversampled waveform sequences directly. The prevalent bidirectional LSTM (BiLSTM) and Transformer structures, suitable for excavating sequential correlation of complex sources and waveform sequences, are considered as the backbone of NN receivers. Under the cases of clean label and noisy label, we conceive two novel training algorithms and interpret their principles in theory. The clean label bits are accessible from original source encoding schemes, while noisy label bits are available from the decision results of canonical receivers with independently noised waveform sequences. When noisy labels possess sufficiently small error rates, optimized NN receiver is competitive with that adopting the accurate labels. As for Markov sources and natural language text sources, simulation results show that the proposed NN receivers’ performances are superior to the classical receivers without a priori knowledge, especially when high spectral efficiency modulation schemes are encountered and random noise is significant.

## Adaptive Parameter Selection in the Simultaneous Transmission of CPM Communication and PN Ranging

- **Status**: ❌
- **Reason**: 위성간 CPM 통신+PN ranging 통합, 적응 파라미터 선택. LDPC/ECC 무관.
- **ID**: ieee:9870540
- **Type**: journal
- **Published**: April 2023
- **Authors**: Rui Xue, Tong Wang
- **PDF**: https://ieeexplore.ieee.org/document/9870540
- **Abstract**: Ranging and communication are the two main functions of intersatellite link (ISL). The integration of these two functions and transmission of them on the same link can simplify the onboard equipment, reduce power consumption, save frequency resources, and integrate the ground station resources to reduce the complexity of the management system. In view of this, the regenerated pseudonoise (PN) ranging signal and continuous phase modulation (CPM) communication signal are combined at the phase level, and an integrated signal model of ranging communication based on CPM+PN is proposed in this article. To improve the accuracy of intersatellite ranging, an adaptive parameter selection algorithm is proposed in this article, which can adaptively select the ranging signal weighting factor according to the current channel state. The simulation results show that the adaptive parameter selection algorithm can greatly improve the ranging accuracy on the premise of ensuring the reliability of communication.

## A Rate Compatible LDPC Scheme in the Quantum Key Distribution System

- **Status**: ❌
- **Reason**: QKD용 Raptor-Like rate-compatible LDPC지만 표준 puncturing/truncation 사용, 양자 채널 응용 특이적이며 새 디코더·구성 기여 없음.
- **ID**: ieee:10211941
- **Type**: conference
- **Published**: 7-9 April 
- **Authors**: Junchao Zhang, Haojie Jin, Hao Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/10211941
- **Abstract**: In the variable quantum transmission channel environment, this paper proposes a rate-compatible LDPC code scheme based on the Raptor-Like structure. With such specific truncation and puncturing operations, we can generate the coding scheme with different code rates under a unified prototype graph, and supports arbitrary information lengths and coding code lengths. On the premise of reducing hardware implementation costs. We can achieve the code rate compatibility and decoding performance requirements of the variable quantum channels. Simulation results show that there is a negative correlation between the coding code rate and the QBER parameter corresponding to the BER threshold. The relevant conclusions can provide reference for the QKD system post-processing LDPC code compatibility scheme.

## VLSI Architecture of a High Speed Polar Code Decoder using Finite Length Scaling LDPC Codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC BP 기반 polar 디코더 VLSI 아키텍처 — 이식 가능 HW/디코더 기여 가능성 (D), 애매하여 보존
- **ID**: ieee:10157091
- **Type**: conference
- **Published**: 5-7 April 
- **Authors**: Kandi Naveen, Vishnubhatla Sai Lakshmi Manonmai, Murala Sri Jaya Nikhitha +2
- **PDF**: https://ieeexplore.ieee.org/document/10157091
- **Abstract**: In this concise a polar decoder form propagation based on belief is formulated which employ finite length LDPC systems. Here the belief sum-product Propagation (BP) is designed for LDPC system beyond affecting the binary communication erasure channels. Belief decoding is parallel and iterative in nature, as it own iteratively nature the required idleness and energy dissemination increments straightly. The prompt report stated that unstable node (VNs) is reduced during individual iteration than as BP. Declination of erased VNs reduces decoding process cause a forceful decrease in complexity, compared among polar decoder that is designed based on CSFG. CSFG is implemented with Quarter-way scheduling algorithm, a sub-factor graph reduces valuations of taken by belief decoder but due to different variable nodes used in the process it has large complication during design. To overcome this BPD with LDPC codes is designed. Simulation and synthesis results in the progressive art reveal that LDPC system drawn better in performance in contrast with belief based propagation.

## Fast Polar Decoder Implementation using Special Nodes

- **Status**: ❌
- **Reason**: special node 기반 고속 polar SC 디코더 — polar 전용, LDPC는 부수 언급, 떼어낼 LDPC 기법 없음
- **ID**: ieee:10136054
- **Type**: conference
- **Published**: 5-6 April 
- **Authors**: Swapnil P. Badar, Kamlesh Khanchandani, Pravin Wankhede
- **PDF**: https://ieeexplore.ieee.org/document/10136054
- **Abstract**: The information sent by the transmitter to the receiver through the channel may be user information or control information. For error-free communication, errorcorrecting codes are needed to detect and correct errors. ECCs like low-density parity check (LDPC) and polar code are selected for channel data and channel control coding, respectively, for 5G wireless communication. Compared to LDPC and turbo codes, Polar code has the ability to use all channel capacity. The Successive Cancellation decoder is a basic polar decoder, which has longer latency due to its sequential nature. A polar decoder with special nodes is proposed in this paper. This fast polar decoder makes the decoding operation faster. The polar decoder is designed using special nodes–Rate-zero, Rate-one, Single Parity Check, and Repetition nodes. These special nodes are generated from the proposed node generator circuit. VLSI architectures of special nodes and fast polar decoder are generated by the Xilinx platform, which is shown in this paper

## Comparison and Analysis of Ricean $K$-Factor Estimators in Industrial Wireless Channels

- **Status**: ❌
- **Reason**: 산업 무선채널 Rician K-factor 추정 분석; ECC/LDPC 무관
- **ID**: ieee:10144125
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Àlvaro A. M. de Medeiros, Victor Cionca
- **PDF**: https://ieeexplore.ieee.org/document/10144125
- **Abstract**: The performance constraints imposed to the use of wireless communications on industrial applications collide with the severe propagation conditions of such adverse environment. The small-scale variations due to multipath and mobility of transceiver and/or scatterers must be characterized properly in order to select the most suitable fading mitigation technique. An important parameter related to the nature of the multipath components is the Rician $K$ -factor, which can be obtained from both channel impulse response and received power level time series, also known as wideband and narrowband methods. At runtime narrowband methods are straightforward due to the reduced capability of operational wireless transceivers. In this paper, we analyze wireless channel measurements of different industrial scenarios in order to compare $K$ -factor estimators. Results indicate similarities between narrowband and a wideband $K$ -factor estimator, which means accurate channel characterization at operational time is possible. Additionally, an application example evaluates the $K$ -factor estimation on the performance of wireless communication systems.

## Research on Physical Layer Key Generation Based on Wireless Channel Characteristics in New Power System

- **Status**: ❌
- **Reason**: 물리계층 키 생성(보안/QKD 유형); ECC 디코더/구성 기법 없음 (보안 제외)
- **ID**: ieee:10154784
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Wang Keming, Gong Haoquan, Ma Jun +3
- **PDF**: https://ieeexplore.ieee.org/document/10154784
- **Abstract**: The new power system is the national development strategy and development direction of smart grid. Communication is the basis of the development of the new power system. in the distribution automation business, communication is the weakest link. In order to make electric power communication develop more smoothly, we should improve our awareness of security issues. Because of the particularity of electric power communication, it often has very high requirements for the security of communication. In order to effectively ensure the security of electric power communication data, data encryption technology can be applied to the data transmission process, and the security of information transmission can be improved through the application of encryption and decryption keys.Physical layer key generation technology is a security technology that uses wireless channel characteristics as a random source to generate keys. This technology uses the anisotropy, time variation and spatial uniqueness of wireless channels to generate random sequences, which is different from traditional encryption methods. Physical layer key generation technology does not require the key management and distribution of a third party trusted organization. In theory, it can achieve one encryption at a time to achieve the absolute security of Shannon confidential communication[1]. This paper first briefly introduces the wireless channel physical layer key generation model and the general process of key generation scheme based on channel feature quantization, and then studies the improved optimization scheme based on traditional channel detection, preprocessing and quantization algorithm, so as to effectively improve the key generation performance.

## Generalized low rank parity check codes

- **Status**: ❌
- **Reason**: Rank-metric LRPC 코드(암호용), F_q-선형 비이진 — LDPC ECC 아님, 비이진
- **ID**: ieee:10160243
- **Type**: conference
- **Published**: 23-28 Apri
- **Authors**: Ermes Franch, Philippe Gaborit, Chunlei Li
- **PDF**: https://ieeexplore.ieee.org/document/10160243
- **Abstract**: In this work we propose a family of ${\mathbb{F}_q}$-linear lowrank parity check (LRPC) codes based on a bilinear product over $\mathbb{F}_q^m$ defined by a generic 3-tensor over ${\mathbb{F}_q}$. A particular choice of this tensor corresponds to the classical ${\mathbb{F}_{{q^m}}}$-linear LRPC codes; and other tensors yield ${\mathbb{F}_q}$-linear codes, which, with some caveats, can be efficiently decoded with the same idea of decoding LRPC codes. The proposed codes contribute to the diversity of rank metric codes for cryptographic applications, particularly for the cases where attacks utilize ${\mathbb{F}_{{q^m}}}$-linearity to reduce decoding complexity.

## Neural Belief Propagation Decoding of Quantum LDPC Codes Using Overcomplete Check Matrices

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) 디코딩으로 degeneracy 등 양자 전용 개념에 의존(overcomplete check matrix, quaternary BP); 원칙 제외
- **ID**: ieee:10161656
- **Type**: conference
- **Published**: 23-28 Apri
- **Authors**: Sisi Miao, Alexander Schnerring, Haizheng Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10161656
- **Abstract**: The recent success in constructing asymptotically good quantum low-density parity-check (QLDPC) codes makes this family of codes a promising candidate for error-correcting schemes in quantum computing. However, conventional belief propagation (BP) decoding of QLDPC codes does not yield satisfying performance due to the presence of unavoidable short cycles in their Tanner graph and the special degeneracy phenomenon. In this work, we propose to decode QLDPC codes based on a check matrix with redundant rows, generated from linear combinations of the rows in the original check matrix. This approach yields a significant improvement in decoding performance with the additional advantage of very low decoding latency. Furthermore, we propose a novel neural belief propagation decoder based on the quaternary BP decoder of QLDPC codes which leads to further decoding performance improvements.

## Rate-Adaptive Protograph MacKay-Neal Codes

- **Status**: ✅
- **Reason**: 프로토그래프 MN/LDPC rate-adaptive 구성, density evolution+error floor, biAWGN 바이너리 — 코드설계(E)
- **ID**: ieee:10161636
- **Type**: conference
- **Published**: 23-28 Apri
- **Authors**: Ayman Zahr, Balazs Matuz, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/10161636
- **Abstract**: A class of rate-adaptive protograph MacKay-Neal (MN) codes is introduced and analyzed. The code construction employs an outer distribution matcher (DM) to adapt the rate of the scheme. The DM is coupled with an inner protograph-based low-density parity-check (LDPC) code, whose base matrix is optimized via density evolution analysis to approach the Shannon limit of the binary-input additive white Gaussian noise (biAWGN) channel over a given range of code rates. The density evolution analysis is complemented by finite-length simulations, and by a study of the error floor performance.

## Achievable Information Rates and Concatenated Codes for the DNA Nanopore Sequencing Channel

- **Status**: ✅
- **Reason**: DNA storage용 concatenated 코드(outer LDPC + inner convolutional)와 channel-tailored ECC 설계; 스토리지 ECC 일반(B)으로 이식 가능성 있어 살림
- **ID**: ieee:10161642
- **Type**: conference
- **Published**: 23-28 Apri
- **Authors**: Issam Maarouf, Eirik Rosnes, Alexandre Graell I Amat
- **PDF**: https://ieeexplore.ieee.org/document/10161642
- **Abstract**: The errors occurring in DNA-based storage are correlated in nature, which is a direct consequence of the synthesis and sequencing processes. In this paper, we consider the memory-k nanopore channel model recently introduced by Hamoum et al., which models the inherent memory of the channel. We derive the maximum a posteriori (MAP) decoder for this channel model. The derived MAP decoder allows us to compute achievable information rates for the true DNA storage channel assuming a mismatched decoder matched to the memory-k nanopore channel model, and quantify the loss in performance assuming a small memory length—and hence limited decoding complexity. Furthermore, the derived MAP decoder can be used to design error-correcting codes tailored to the DNA storage channel. We show that a concatenated coding scheme with an outer low-density parity-check code and an inner convolutional code yields excellent performance.

## A modified probabilistic amplitude shaping scheme to use sign-bit-like shaping with a BICM

- **Status**: ❌
- **Reason**: sign-bit shaping을 5G LDPC BICM에 적용하는 shaping/변조 기법; LDPC는 베이스라인일 뿐 떼어낼 ECC 기여 없음
- **ID**: ieee:10161666
- **Type**: conference
- **Published**: 23-28 Apri
- **Authors**: Vincent Corlay, Hamidou Dembele
- **PDF**: https://ieeexplore.ieee.org/document/10161666
- **Abstract**: On the one hand, sign-bit shaping is a popular shaping scheme where the conditional probability of the sign bit is made non-equiprobable. On the other hand, probabilistic amplitude shaping (PAS) is a popular coding scheme, to combine shaping and a bit-interleaved coded modulation (BICM), where the sign bit should not be involved in the shaping. Indeed, with the PAS scheme the sign bit is the parity bit, i.e., the output of the systematic error-correcting code. As a result, sign-bit shaping has been used with multilevel coded modulations rather than BICM. In this paper, we show that with minor modifications it is possible to use sign-bit-like shaping with a BICM. Simulation results are provided with the 5G NR LDPC BICM scheme.

## Performance Improvement of Multi-level Redundant Discrete Wavelet Transform OFDM System by Using LDPC Encoding and Belief Propagation Algorithm

- **Status**: ❌
- **Reason**: DWT-OFDM에 표준 LDPC+BP 적용한 베이스라인, 새 디코더/구성 기여 없음
- **ID**: ieee:10151120
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Jiacheng Ou, Bin Zhou, Xianhui Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10151120
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) is extensively researched by scholars because of its strong anti-fading ability, anti-interference ability and high frequency band utilization. Based on the discrete wavelet transform orthogonal frequency division multiplexing (DWT-OFDM) all these years, a variety of improved systems have emerged one after another. But the disadvantage is that coding technology has not been effectively applied in these systems. In this paper, We choose multilevel redundant discrete wavelet transform orthogonal frequency division multiplexing (ML-RDWT-OFDM) system as the research object, low-density Parity-check (LDPC) coding and soft decision (SD) decoding of belief propagation algorithm are introduced to increase the ML-RDWT-OFDM performance factor. The uncoded and coded ML-RDWT-OFDM systems are simulated to verify that the coding scheme does improve the performance.

## Direct Transposition Interleaving Technique for DNA Data Storage

- **Status**: ❌
- **Reason**: DNA 저장용 인터리빙 코드(DTIC), LDPC ECC 기법 아님
- **ID**: ieee:10248051
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Zhengyu Li, Kun Bi, Xiangwei Zhao
- **PDF**: https://ieeexplore.ieee.org/document/10248051
- **Abstract**: Compared to traditional storage media, DNA possesses several advantages; however, it is prone to errors in its base sequence during the storage process. When employing traditional error correction coding algorithms for DNA storage, a substantial number of redundant bases are added to ensure lossless data recovery. This approach results in significant base consumption and is ill-suited for scenarios with extreme error cases. To address these issues, this paper proposes the Direct Transpose Interleaving Code (DTIC), which uses data interleaving technology to distribute potential errors in a sequence across multiple sequences. DTIC can be used in conjunction with traditional error correction coding algorithms to enhance data recovery capabilities. Through theoretical analysis and simulation experiments, this paper demonstrates that lossless data recovery necessitates fewer redundant bases with DTIC processing compared to data without DTIC processing.

## An Improved Belief Propagation Bit-Flipping Decoder for Polar Codes

- **Status**: ❌
- **Reason**: Polar 부호용 BP bit-flip 디코더, flip set 구성이 분극채널에 의존해 LDPC 이식성 없음
- **ID**: ieee:10248708
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Mengqing Zhao, Daqin Peng
- **PDF**: https://ieeexplore.ieee.org/document/10248708
- **Abstract**: Bit flipping was first used to improve the decoding performance of successive cancellation (SC) decoder. Since SC decoding process is serial, so the first bit that goes wrong in the decoding process will cause several subsequent bits to go wrong, which will suffer from higher decoding delay than belief propagation (BP) parallel decoding. In order to meet the performance of 5G low latency and high reliability, BP decoding algorithm have received a lot of attention. However, at medium and high signal-to-noise ratios (SNR), BP decoding does not perform as well as the SC list (SCL) decoding algorithm. Hence, BP decoding algorithm borrows bit-flip strategies from SC bit flip (SCF) decoder to improve the performance. The performance of BP bit flip (BPF) decoding depends on whether the construction of the flip set is correct, so this letter proposes a flip set construction approach based on the standard deviation of the log-likelihood ratio (LLR) and the reliability weight of polarized channels, which is comparable to the existing BPF decoding, the improved algorithm can identify the error-prone bits more efficiently and improve the decoding performance.

## An Improved DVB-S2 Phase Coarse Synchronization Algorithm and Its FPGA Implementation

- **Status**: ❌
- **Reason**: DVB-S2 위상 동기 FPGA, LDPC 디코더/코드설계 아님
- **ID**: ieee:10248943
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Xianyu Zhang, Jing Zhang, Zixuan Huang
- **PDF**: https://ieeexplore.ieee.org/document/10248943
- **Abstract**: This paper proposes an improved phase coarse synchronization algorithm, which can be applied to the DVB-S2 system. The improved algorithm can handle the uncorrected residual frequency offset from the frequency synchronization module. Compared with the original algorithm, the residual frequency offset is nearly doubled threshold, and reduces the complexity of FPGA implementation and saves hardware resource overhead. The scheme is implemented on Xilinx Virtex-7 VC709 field programmable gate array, and simulation verifies that the scheme can achieve bit error performance below 10-7 within the supported residual frequency offset range.

## An Efficient FPGA Implementation of LDPC Decoder for 5G New Radio

- **Status**: ✅
- **Reason**: 5G NR LDPC 디코더 FPGA 구현, 정규화 min-sum + circular shift-register 모델 — C/D 이식 가능 디코더·HW
- **ID**: ieee:10134365
- **Type**: conference
- **Published**: 19-21 Apri
- **Authors**: R. Varshini Devi, S. Rajaram
- **PDF**: https://ieeexplore.ieee.org/document/10134365
- **Abstract**: In this work, we present a new design approach for the implementation of an efficient FPGA architecture for the Low-Density Parity Check codes (LDPC) Decoder according to the specifications of 5G New-Radio (NR) cellular communication standard, which has advantages such as high coding gain, good throughput, and low power dissipation. The complexity and time required for implementing 5G NR LDPC decoders using conventional HDL-based methods can pose a significant challenge. To solve this problem, we presented a methodology that utilizes high-level modeling tools to design LDPC decoders for 5G, making the process more efficient. This approach can support the programmable logic design and be used for FPGA implementation. The methodology has been tested by designing, simulating, and implementing representative LDPC decoders. The 5G NR LDPC decoder realization is achieved using a Circular Shift-Register-based model to decrease the difficulty. The data is decoded using the Normalized Min-Sum algorithm. FPGA implementation analyzes the system productivity and efficiency with hardware utilization of the chip and the timing parameters summary. The VLSI circuit design of this Decoder is executed using Xilinx 14.1, programmed with Verilog HDL and hardware operation is evaluated on the Virtex-7 FPGA kit.

## McEliece Cryptosystem: Reducing the Key Size with QC-LDPC codes

- **Status**: ❌
- **Reason**: McEliece 암호시스템 키 크기 축소(보안/암호 응용) — QC-LDPC를 코드기반 암호에 사용, 떼어낼 NAND ECC 디코더/구성 기법 없음, 원칙 제외
- **ID**: ieee:10108339
- **Type**: conference
- **Published**: 17-20 Apri
- **Authors**: Paula Pérez-Pacheco, Pino Caballero-Gil
- **PDF**: https://ieeexplore.ieee.org/document/10108339
- **Abstract**: Post-quantum cryptography is a growing area since Shor showed that a quantum computer with enough qubits could be used to break the most widely used public-key cryptographic protocols today, such as RSA or those based on the discrete logarithm problem. For this reason, it has become urgent to design cryptosystems that are robust against quantum computer attacks. One of them is the code-based McEliece cryptosystem, which was originally proposed using Goppa codes in 1978. The improved version of the original McEliece cryptosystem, called Classic McEliece, made it as far as the fourth round of the NIST Post-Quantum Cryptography standardization process launched by the National Institute of Technology to update the standards and include post-quantum cryptography in digital signatures, encryption and key exchange. In this work we describe and analyze two variants of the original cryptosystem designed to overcome its main drawbacks, such as its large key size and weakness against known attacks. In addition, both the recent attack that allows the recovery of the private key with limited complexity and the ways in which this attack can be prevented by changing the shape of some constituent arrays in these two new variants are discussed.

## R-LDPC: Refining Behavior Descriptions in HLS to Implement High-throughput LDPC Decoder

- **Status**: ✅
- **Reason**: HLS 기반 고처리량 QC-LDPC 디코더 마이크로아키텍처(파이프라인, CNU 공유, shifter 최적화) — HW 아키텍처(D) NAND 이식 가능
- **ID**: ieee:10136941
- **Type**: conference
- **Published**: 17-19 Apri
- **Authors**: Yifan Zhang, Qiang Cao, Jie Yao +1
- **PDF**: https://ieeexplore.ieee.org/document/10136941
- **Abstract**: High-Level Synthesis (HLS) translates high-level behavior-description to Register-Transfer Level (RTL) implemen-tation in modern Field-Programmable Gate Arrays (FPGAs), accelerating domain-specific hardware developments. Low-Density Parity-Check (LDPC), as a powerful error-correction code family, has been widely implemented in hardware for building a reliable data channel over a noisy physical channel in communication and storage applications. Leveraging HLS to fast prototype high-performance LDPC decoder is intriguing with high scalability and low hardware-dependence, but generally is sub-optimal due to the lack of accurate and precise behavior descriptions in HLS to characterize iteration- and circuit-level implementation details. This paper proposes an HLS-based QC-LDPC decoder with scalable throughput by precisely refining the LDPC behavior descriptions, R-LDPC for short. To this end, R-LDPC first adopts an HLS-based LDPC decoder microarchitecture with a module-level pipeline. Second, R-LDPC offers a multi-instance-sharing one (MSO) description to explicitly define shared parts and non-shared parts for an array of check-node updating-units (CNU), eliminating redundant function modules and addressing circuits. Third, R-LDPC designs efficient single-stage and multi-stage shifters to eliminate unnecessary bit-selection circuits. Finally, R-LDPC provides invalid-element aware loop scheduling before the compile phase to avoid some unnecessary stalls at runtime. We implement an R-LDPC decoder, compared to the original HLS-based implementation, R-LDPC reduces the hardware con-sumption up to 56%, the latency up to 67%, and the decoding throughput up to 300%. Furthermore, R-LDPC is adapted to different scales, LDPC standards, and code rates, and can achieve 9.9Gbps decoding throughput in Xilinx U50.

## High Efficient Secret Key Reconciliation Scheme Based on Cascade Algorithm

- **Status**: ❌
- **Reason**: QKD Cascade 정보조정 알고리즘 최적화. 채널 ECC 아닌 reconciliation, LDPC도 아님(BINARY/Cascade), 떼어낼 디코더 기법 없음
- **ID**: ieee:10142787
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Keming Tian, Gang Xin, Jian Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/10142787
- **Abstract**: In the quantum key generation scheme, key reconciliation is used to eliminate inconsistent key bitstream between partners. The speed of reconciliation and the retention length of data are the main indicators for evaluating a reconciliation method. The Cascade algorithm is developed based on the BINARY reconciliation. By forward backtracking, Cascade can correct even-numbered errors hidden in the data. However, its computational complexity seriously affects the reconciliation speed, and the final length of key generated is relatively low. In this paper, an optimization method BFR-Cascade algorithm is proposed to reduce the computational complexity. Meanwhile, the final unified deletion rule (FUDR) is applied to increase retention length of data. Compared with Cascade algorithm, the proposed method can achieve 54% higher reconciliation speed when the signal-to-noise ratio (SNR) is 8dB, and the retention length of data is increased by at least 44% through FUDR.

## Achieving Real-Time Spectrum Sharing in 5G Underlay Coexistence With Channel Uncertainty

- **Status**: ❌
- **Reason**: 5G 스펙트럼 공유 GPU 스케줄러 최적화로 ECC/LDPC 무관
- **ID**: ieee:9580537
- **Type**: journal
- **Published**: 1 April 20
- **Authors**: Shaoran Li, Yan Huang, Chengzhang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/9580537
- **Abstract**: Underlay coexistence is a spectrum efficient mechanism to roll out 5G picocells within a macrocell on the same spectrum. Due to a lack of cooperation between the primary users (PUs) in the macrocell and secondary users (SUs) in the picocells, it is impossible to have complete knowledge of channel conditions between them. Under such a circumstance, chance-constrained programming (CCP) has been shown to be an ideal optimization tool to address such a channel uncertainty. However, solutions to CCP are computationally intensive and cannot meet 5G’s timing requirement (125 $\mu s$μs). To address this problem, we propose a novel scheduler called GPU-based Underlay Coexistence (GUC) with the goal of finding an approximate solution to CCP in real-time. The essence of GUC is to decompose the original optimization problem into a large number of small subproblems that are suitable for parallel computation on GPU platforms. By selecting a subset of promising subproblems and solving them in parallel with fast algorithms, we are able to leverage GPU parallel computing and develop a real-time solution. Through extensive experiments, we show that GUC meets the 125 $\mu s$μs requirement while achieving 90% optimality on average.
