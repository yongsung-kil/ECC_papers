# IEEE Xplore — 2020-11


## An Optimized Algorithm to Construct QC-LDPC Matrix in Compressed Sensing

- **Status**: ❌
- **Reason**: 압축센싱용 QC-LDPC 측정행렬 구성, girth-4 제거는 교과서 수준이고 채널코딩 ECC가 아닌 CS 측정행렬 응용이라 떼어낼 새 ECC 기법 없음
- **ID**: ieee:10251837
- **Type**: journal
- **Published**: November 2
- **Authors**: Xiaoqi Yin, Jiansheng Qian, Xingge Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/10251837
- **Abstract**: Aiming at the problems such as the large amount of data in transmission and difficulties in hardware implementation, an optimized algorithm is put forward to generate QC-LDPC measurement matrix based on limited geometry in compressed sensing, which can eliminate the short girth of 4 in Tanner graph through the design of basis matrix. Because of the quasicyclic characteristics, it can be realized by shift register so as to reduce the complexity of coding. The simulation results indicate that QC-LDPC matrix is superior to traditional measurement matrices by using the same OMP algorithm, and there are good improvements in the aspects of PSNR, SSIM, NMSE and runtime, which are conductive to the application of compressed sensing theory in real-time data transmission.

## New GRP LDPC Codes for H-ARQ-IR Over the Block Fading Channel

- **Status**: ❌
- **Reason**: GRP LDPC + H-ARQ-IR로 블록 페이딩 다이버시티 목적, 무선 특이적 구성이고 NAND 이식 가능한 새 디코더/HW 없음
- **ID**: ieee:9149698
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Chanki Kim, Sang-Hyo Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/9149698
- **Abstract**: In this paper, we propose a new construction of generalized root protograph (GRP) low-density parity-check (LDPC) codes which has a guaranteed diversity order. New hybrid-automatic request with incremental redundancy (H-ARQ-IR) is also proposed to ensure high diversity and rate-compatibility in wireless communication systems, where the GRP LDPC codes are employed along with a method called feedback encoding. The proposed H-ARQ-IR has advantages of low-complexity and near-optimal performance. In order to show its performance behavior, theoretical analysis for the proposed scheme is conducted for the block fading channel. Furthermore, numerical analysis shows that it achieves near maximum diversity order under the belief propagation (BP) decoding with binary phase shift keying (BPSK) modulation and high-order quadrature amplitude modulations (QAMs).

## Increasing Throughput in Wireless Communications by Grouping Similar Quality Bits

- **Status**: ❌
- **Reason**: 무선 채널 비트 품질별 그룹핑 스루풋 기법, LDPC 디코더/구성 기여 없음
- **ID**: ieee:9139216
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Mai Zhang, Jiho Song, David J. Love +3
- **PDF**: https://ieeexplore.ieee.org/document/9139216
- **Abstract**: This letter proposes and studies a technique for grouping the bits transmitted through a wireless channel into codewords according to their quality (SNR). It proves that splitting the bits into multiple codewords of different rates provides a higher throughput than mixing heterogeneous quality bits into fixed-rate codewords. The letter first analyzes the pros and cons of different mappings of bits and codewords to the available time, frequency, and modulation resources. Then it describes the proposed scheme for a 16-QAM modulation and illustrates its benefits through simulations. Finally, it provides a mathematical proof of its superiority in a binary-input parallel AWGN channel with finite length error correcting codes. The proposed scheme can be applied to any communications channel using error correcting codes (ECC), but it is of particular interest for millimeter-wave (mmWave) wireless communications, where the channel quality is closely monitored and high order modulations are used over wide bandwidths. The simulations suggest that modest gains in throughput can be obtained with negligible additional complexity.

## Improved Belief Propagation Polar Decoders With Bit-Flipping Algorithms

- **Status**: ❌
- **Reason**: Polar code BP 비트플리핑 디코더 — LDPC가 아닌 폴라 부호 전용 기법, NAND LDPC로 이식할 기법 없음
- **ID**: ieee:9170582
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Yifei Shen, Wenqing Song, Houren Ji +4
- **PDF**: https://ieeexplore.ieee.org/document/9170582
- **Abstract**: Since the inherent serial nature of successive cancellation list (SCL) decoding results in a long latency, belief propagation (BP) decoding for polar codes has drawn attention for high-throughput applications. However, its error correction performance is inferior to that of SCL decoding. Therefore, the bit-flipping strategy has been recently applied to BP decoding, which can approach the SCL decoding performance through multiple additional decoding attempts. The original BP flip (BPF) decoding suffers from an inaccurate identification of erroneous bits by a fixed flip set (FS), which has been improved by the generalized BPF (GBPF) decoding. In this article, the GBPF decoding is extended to support multiple bits being flipped in one decoding attempt. In addition, for two types of decoding errors: detected errors and undetected errors, we propose two novel methods to more effectively identify erroneous bits. For detected errors, the concept of loop sets is defined and a loopbased identification method is introduced based on the study of error patterns of BP decoding. On the other hand, a method to generate a more accurate fixed FS is proposed for undetected errors, which considers the bit error distribution under BP decoding. Combining the two methods, the GBPF with merged sets (GBPF-MS) decoding can achieve the SCL-8 performance and outperforms the state-of-the-art BPF, BP list, and SC flip (SCF) decoding, for polar codes with length 1024 and information rate 1/2. Implemented by 40nm CMOS technology, the proposed GBPF-MS decoder with ten flips exhibits an average throughput of 4.19 Gbps at 2.5 dB, which is 1.6× and 1.72× faster than the state-of-the-art SCL-4 and SCF decoders, respectively.

## Randomized Polar Subcodes With Optimized Error Coefficient

- **Status**: ❌
- **Reason**: Polar subcode 구성(error coefficient 최적화) — 폴라 부호 전용, LDPC 이식성 없음
- **ID**: ieee:9174787
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/9174787
- **Abstract**: A method for construction of polar subcodes with reduced error coefficient is presented. The proposed approach relies on explicit enumeration of low-weight non-zero codewords in a polar code, and construction of dynamic freezing constraints which define a subcode not containing most of these codewords. The obtained codes provide a large performance gain in the high-SNR region compared to non-optimized polar subcodes and polar codes with CRC.

## Learning to Communicate and Energize: Modulation, Coding, and Multiple Access Designs for Wireless Information-Power Transmission

- **Status**: ❌
- **Reason**: SWIPT 무선 정보-전력 전송 변조/코딩 설계, NN 오토인코더 — LDPC ECC로 떼어낼 디코더/HW/코드설계 기법 없음, 무선 응용 특이적
- **ID**: ieee:9169700
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Morteza Varasteh, Jakob Hoydis, Bruno Clerckx
- **PDF**: https://ieeexplore.ieee.org/document/9169700
- **Abstract**: The explosion of the number of low-power devices in the next decades calls for a re-thinking of wireless network design, namely, unifying wireless transmission of information and power so as to make the best use of the RF spectrum, radiation, and infrastructure for the dual purpose of communicating and energizing. This article provides a novel learning-based approach towards such wireless network design. To that end, a parametric model of a practical energy harvester, accounting for various sources of nonlinearities, is proposed using a nonlinear regression algorithm applied over collected real data. Relying on the proposed model, the learning problem of modulation design for Simultaneous Wireless Information-Power Transmission (SWIPT) over a point-to-point link is studied. Joint optimization of the transmitter and the receiver is implemented using Neural Network (NN)-based autoencoders. The results reveal that by increasing the receiver power demand, the baseband transmit modulation constellation converges to an On-Off keying signalling. Utilizing the observations obtained via learning, an algorithmic SWIPT modulation design is proposed. It is observed via numerical results that the performance loss of the proposed modulations are negligible compared to the ones obtained from learning. Extension of the studied problem to learning modulation design for multi-user SWIPT scenarios and coded modulation design for point-to-point SWIPT are considered. The major conclusion of this work is to utilize learning-based results to design non learning-based algorithms, which perform as well. In particular, inspired by the results obtained via learning, an algorithmic approach for coded modulation design is proposed, which performs very close to its learning counterparts, and is significantly superior due to its high real-time adaptability to new system design parameters.

## Efficient Scheduling for the Massive Random Access Gaussian Channel

- **Status**: ❌
- **Reason**: 대규모 랜덤액세스 가우시안 채널 스케줄링, LDPC ECC 기법 없음
- **ID**: ieee:9163281
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Gustavo Kasper Facenda, Danilo Silva
- **PDF**: https://ieeexplore.ieee.org/document/9163281
- **Abstract**: This article investigates the massive random access Gaussian channel with a focus on small payloads. For this problem, grant-based schemes have been regarded as inefficient due to the necessity of large feedbacks and the use of inefficient scheduling request methods. This articles attempts to answer whether grant-based schemes can be competitive against state-ot-art grantless schemes and worthy of further investigation. In order to compare these schemes fairly, a novel model is proposed, and, under this model, a novel grant-based scheme is proposed. The scheme uses Ordentlich and Polyanskiy's grantless method to transmit small coordination indices in order to perform the scheduling request, which allows both the request from the users to be efficient and the feedback to be small. We also present improvements to the Ordentlich and Polyanskiy's scheme, allowing it to transmit information through the choice of sub-block, as well as to handle collisions of the same message, significantly improving the method for very small messages. Simulation results show that, if a small feedback is allowed, the proposed scheme performs closely to the state-of-art while using simpler coding schemes, suggesting that novel grant-based schemes should not be dismissed as a potential solution to the massive random access problem.

## Error Propagation Mitigation in Sliding Window Decoding of Braided Convolutional Codes

- **Status**: ❌
- **Reason**: Braided convolutional codes 슬라이딩윈도우 디코딩 오류전파 완화, LDPC가 아닌 convolutional 코드 특이적 기법
- **ID**: ieee:9165839
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Min Zhu, David G. M. Mitchell, Michael Lentmaier +2
- **PDF**: https://ieeexplore.ieee.org/document/9165839
- **Abstract**: We investigate error propagation in sliding window decoding of braided convolutional codes (BCCs). Previous studies of BCCs have focused on iterative decoding thresholds, minimum distance properties, and their bit error rate (BER) performance at small to moderate frame length. Here, we consider a sliding window decoder in the context of large frame length or one that continuously outputs blocks in a streaming fashion. In this case, decoder error propagation, due to the feedback inherent in BCCs, can be a serious problem. To mitigate the effects of error propagation, we propose several schemes: a window extension algorithm where the decoder window size can be extended adaptively, a resynchronization mechanism where we reset the encoder to the initial state, and a retransmission strategy where erroneously decoded blocks are retransmitted. In addition, we introduce a soft BER stopping rule to reduce computational complexity, and the tradeoff between performance and complexity is examined. Simulation results show that, using the proposed window extension algorithm, resynchronization mechanism, and retransmission strategy, the BER performance of BCCs can be improved by up to four orders of magnitude in the signal-to-noise ratio operating range of interest, and the soft BER stopping rule can be employed to reduce computational complexity.

## Near-Perfect Code Scrambling With Limited Key Information for Wiretap Channels

- **Status**: ❌
- **Reason**: Wiretap 채널 코드 스크램블링 보안 기법 — ECC 디코더/코드설계 기여 아님, 보안 응용
- **ID**: ieee:9204759
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Sangjoon Park, Hyukmin Son
- **PDF**: https://ieeexplore.ieee.org/document/9204759
- **Abstract**: In this paper, we propose a practical code scrambling scheme for secure transmissions with channel coding over wiretap channels. We develop explicit scrambling and descrambling matrix generation algorithms that can be performed with a key of limited length for each message transmission. We demonstrate that the proposed scheme avoids the direct inverse operation for large scrambling and descrambling matrices through binary operations. Therefore, without huge complexity loads and feedback overheads being incurred, the scrambling and descrambling matrices at the transmitter and legitimate receiver, respectively, can be simultaneously updated to the new pair through a few binary operations on each side. We also demonstrate that the proposed scheme approaches the perfect scrambling condition for maximizing the decoding error spreading when a sufficiently long independent key with a uniform Bernoulli distribution is provided, where the key length condition in practical applications can be overcome via key accumulation over transmissions. In addition, the proposed scheme also benefits from the descrambling matrix mismatch when the estimation for the key at the eavesdropper is imperfect. Numerical results confirm our analysis and indicate that the proposed scheme significantly improves the secrecy performance of code scrambling in wiretap channels.

## An OFDM-Based Waveform With High Spectral Efficiency

- **Status**: ❌
- **Reason**: OFDM 파형/송수신기 설계, LDPC ECC와 무관
- **ID**: ieee:9136779
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Filipe Conceição, Marco Gomes, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/9136779
- **Abstract**: A new Time Interleaved Block Windowed Burst OFDM (TIBWB-OFDM) transceiver scheme is studied in this paper, where adjacent OFDM sub-blocks are allowed to overlap in time. This leads to a smaller overall block, increasing the spectral efficiency and decreasing the peak-to-average power ratio (PAPR) of the transmitted signals, when compared with standard TIBWB-OFDM. These efficiency gains are obtained at the expense of interference between sub-blocks, which deteriorates the performance. Thus, we propose several receiver embodiments that include frequency domain equalizers and time domain interference cancellation algorithms to cope with channel effects and interference introduced by the overlapping operation.

## Coding Scheme for High-Order QAM Modulations in the Manhattan Metric

- **Status**: ❌
- **Reason**: Manhattan metric 대수 부호 구성으로 QAM용, LDPC가 아니며 NAND 이식 기법 없음
- **ID**: ieee:9144539
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Viacheslav Davydov, Nikita Zeulin, Igor Pastushok +1
- **PDF**: https://ieeexplore.ieee.org/document/9144539
- **Abstract**: In this letter, a code construction in the Manhattan metric with a polynomial complexity algebraic decoding algorithm is proposed. It is shown that the code construction combined with a high-order QAM modulation enjoys a better code rate compared to a binary BCH code along with a competitive decoding procedure complexity. A performance gain from the use of the proposed code construction increases with the growth of an order of a QAM modulation. The code construction is mostly perspective in scenarios with high signal-to-noise ratios and decoding latency constraints, which are required for current and further generations of communications systems.

## Joint Antenna Detection and Bayesian Channel Estimation for Non-Coherent User Terminals

- **Status**: ❌
- **Reason**: 비코히런트 안테나 검출·채널추정, LDPC 무관
- **ID**: ieee:9141419
- **Type**: journal
- **Published**: Nov. 2020
- **Authors**: Ema Becirovic, Emil Björnson, Erik G. Larsson
- **PDF**: https://ieeexplore.ieee.org/document/9141419
- **Abstract**: In this paper, we propose a method of improving the channel estimates for non-coherent multi-antenna terminals, which are terminals that cannot control the relative phase between its antenna ports, with channels that can be considered constant over multiple time slots. The terminals have multiple antennas and are free to choose whichever antenna they want to use in each time slot. An unknown phase shift is introduced in each time slot as we cannot guarantee that the terminals are phase coherent across time slots. We compare three different clustering techniques that we use to detect the active antenna. We also compare a set of different statistical and heuristic estimators for the channels and the phase shifts. We evaluate the methods by using correlated Rayleigh fading and three different bounds on the uplink capacity. The accuracy of the capacity bounds are verified with bit-error-rate simulations. With our proposed methods we can have an SNR improvement of approximately 2 dB at 1 bit/s/Hz.

## Soft-input decoding of concatenated codes based on the Plotkin construction and BCH component codes

- **Status**: ❌
- **Reason**: Plotkin 구성 GMC 연접부호 + BCH 성분부호의 soft-input 디코딩 — LDPC 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9352179
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Daniel Nicolas Bailon, Johann-Philipp Thiers, Jürgen Freudenberger
- **PDF**: https://ieeexplore.ieee.org/document/9352179
- **Abstract**: Low latency communication requires soft-input decoding of binary block codes with small to medium block lengths. In this work, we consider generalized multiple concatenated (GMC) codes based on the Plotkin construction. These codes are similar to Reed-Muller (RM) codes. In contrast to RM codes, BCH codes are employed as component codes. This leads to improved code parameters. Moreover, a decoding algorithm is proposed that exploits the recursive structure of the concatenation. This algorithm enables efficient soft-input decoding of binary block codes with small to medium lengths. The proposed codes and their decoding achieve significant performance gains compared with RM codes and recursive GMC decoding.

## Implementation of the Nonbinary Encoder and Decoder for Systematic Low Density Parity Check Codes on Raspberry-pi boards

- **Status**: ❌
- **Reason**: 비이진(non-binary, GF) LDPC 인코더/디코더 구현 — 비이진 LDPC 즉시 제외
- **ID**: ieee:9284943
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Abhishek Maheshwari, Usana Tuntoolavest, Kazuhiko Fukawa
- **PDF**: https://ieeexplore.ieee.org/document/9284943
- **Abstract**: Since wireless communication systems supply a large amount of packet-sized (non-binary) data, a channel coding technique that can efficiently correct errors caused by channels is required. This paper focuses on systematic Low-Density Parity-Check (LDPC) code for non-binary codes with symbol size of at least 32 bits/symbol and investigates the transmission of non-binary data under different channel conditions through Message Passing Telemetry Transport (MQTT). Hard decision Message Passing-Vector Symbol Decoding (hMP-VSD) is used as a decoder of systematic LDPC. The encoder and decoder are implemented on the Raspberry Pi (R-pi) boards, and the wireless transmission is done by using the Wi-Fi module.

## Analysis of CNN Based Schemes for LDPC Code Classification Using LUT Based Algorithms

- **Status**: ❌
- **Reason**: CNN 기반 LDPC 코드 분류 시스템 — 디코더/HW/코드설계 아님, 이식 기법 없음
- **ID**: ieee:9284950
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Bradley Comar
- **PDF**: https://ieeexplore.ieee.org/document/9284950
- **Abstract**: This paper analyzes the performance of an LDPC code classification system that determines membership of code-words among 3 randomly generated binary LDPC codes. These codes all have the same codeword size and coderate. High classification accuracies are obtained with relatively small neural networks. The analysis presented here determines the accuracies of various look up tables and compares them to the performance of the neural networks.

## LDPC Codeword Size Determination Using Convolutional Neural Networks

- **Status**: ❌
- **Reason**: CNN으로 LDPC 코드워드 크기 분류 — 디코딩/HW/코드설계가 아닌 분류기, 이식할 ECC 기법 없음
- **ID**: ieee:9284907
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Bradley Comar
- **PDF**: https://ieeexplore.ieee.org/document/9284907
- **Abstract**: This paper discusses the design and performance of a forward error correction (FEC) code classification system that is used to determine the size of an unknown codeword from a stream of bits. The classification system is a deep neural network that is trained and tested on half rate low density parity check (LDPC) codes. Tests were performed on streams of codewords using codes of up to 250 different sizes. The CNN based classifier performs very well.

## Simplified Calculation of Bhattacharyya Parameters in Polar Codes

- **Status**: ❌
- **Reason**: Polar code 구성용 Bhattacharyya 파라미터 계산 단순화 — LDPC와 무관, 비-LDPC 부호 제외
- **ID**: ieee:9271700
- **Type**: conference
- **Published**: 30 Oct.-1 
- **Authors**: Jiahui Xiong, Lijun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9271700
- **Abstract**: The construction of polar code refers to selecting K "most reliable polarizing channels" in N polarizing channels to WN(1)transmit information bits. For non-systematic polar code, Arikan proposed a method to measure the channel reliability for BEC channel, which is called Bhattacharyya Parameter method. The calculated complexity of this method is O(N) . In this paper, we find the complementarity of Bhattacharyya Parameter. According to the complementarity, the code construction under a certain channel condition can be quickly deduced from the complementary channel condition.

## Performance Evaluation of Polar Channel Coding on a Practical VLC Link: A Comparison Study

- **Status**: ❌
- **Reason**: VLC에서 Polar/Turbo/LDPC 성능 비교만, 신규 디코더·구성 기여 없는 응용 비교 연구
- **ID**: ieee:9410037
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Hooman Hematkhah, Yousef Seifi Kavian
- **PDF**: https://ieeexplore.ieee.org/document/9410037
- **Abstract**: In this paper, we investigate the performance of Polar codes, Turbo and Low-Density Parity-Check (LDPC) codes on a practical Visible Light Communication (VLC) link, in terms of the Bit-Error-Ratio (BER) vs. SNR separately. The considered parameters are the number of iterations in Turbo and LDPC and list size in the Polar codes respectively. Then, we compare three methods together with the best value of parameters of each one. To give a fair comparison, we use the same length of code as input and the rate of all codes is 1/2. The results show that the Polar codes perform better than Turbo and LDPC codes on VLC based applications.

## Security Gap Investigation of Multilevel Coding in Coherent Fiber-Optical Systems

- **Status**: ❌
- **Reason**: 물리계층 보안(security gap)·광통신 MLC/BICM 응용, LDPC는 베이스라인이며 떼어낼 ECC 기법 없음
- **ID**: ieee:9273750
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Johannes Pfeiffer, Carsten Schmidt-Langhorst, Robert Elschner +4
- **PDF**: https://ieeexplore.ieee.org/document/9273750
- **Abstract**: In fiber-optical communication systems, security against wiretappers is of increasing importance. To counteract successful eavesdropping, classical encryption schemes may be complemented by approaches following the concept of physical-layer security, e.g., the application of suited coding and modulation schemes. We study the security quantified by the security gap metric (which should be minimized) in a wiretap scenario by using an experimental state-of-the-art coherent laboratory setup with gross bit rates up to 768Gb/s utilizing up to 64.0-GBd dual-polarization (DP) 64-ary quadrature amplitude modulation (QAM). Offline processing of captured waveforms allows the investigation of different signal point labeling and coding strategies. Especially the concept of multilevel coding (MLC), where the secret information is exclusively communicated over the lowest bit level, yields significantly smaller security gaps than bit-interleaved coded modulation (BICM) if the same punctured low-density parity-check (LDPC) code is utilized. An increase of the constellation cardinality, which has been shown to further decrease the security gaps in simulations, results in increased implementation penalties in practical systems. This is especially pronounced at high symbol rates, as MLC requires the legitimate receiver to operate at smaller pre-FEC error rates, i.e., larger signal-to-noise-power ratios. To this end, the security of MLC modulation schemes are experimentally investigated for various signal constellations and symbol rates. A security increase compared to BICM schemes is possible for most examined system configurations.

## 5G and Cloudification to Enhance Real-Time Electricity Consumption Measuring in Smart Grid

- **Status**: ❌
- **Reason**: 5G·클라우드 스마트그리드 통신 아키텍처, LDPC와 무관
- **ID**: ieee:9306518
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: M. Forcan, M. Maksimović, J. Forcan +1
- **PDF**: https://ieeexplore.ieee.org/document/9306518
- **Abstract**: The number of smart devices in Smart Grid (SG) increases continuously and the presence of big data demands more efficient communication architectures. It is anticipated that the full potential of the SG vision in terms of better performances, reliability, and quality of service, can be achieved by incorporating the fifth generation of cellular network technology (5G) and Cloudification into the SG. In order to demonstrate their potential in SG, this paper presents the enhancement of real-time electricity consumption measuring with the help of 5G and Cloud computing. 5G-based communication model supporting Advanced Metering Infrastructure (AMI) in SG is built and validated on the example of real-time communication between the SM model and Cloud platform ThingSpeak.

## Approximate Sorting Check Node Processing in Non-Binary LDPC Decoders

- **Status**: ❌
- **Reason**: Non-Binary LDPC 디코더(EMS) 대상 — 비이진 LDPC는 제외 대상
- **ID**: ieee:9294934
- **Type**: conference
- **Published**: 23-25 Nov.
- **Authors**: Dimitris Chytas, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/9294934
- **Abstract**: This paper proposes the use of parallel approximate sorting networks in Non-Binary LDPC decoders and quantifies their impact in terms of performance and complexity. Motivated by the messages truncation concept of the Extended Min Sum (EMS) algorithm and the reduction it induces on the decoding complexity, we seek for an approximate parallel sorting strategy for the Elementary Check Node (ECN) Unit processing in the EMS algorithm. We quantify the impact of parallel approximate sorting on both error correction decoding performance and hardware complexity. Bubble check sorting methods are compared to proposed parallel approximate sorting techniques in terms of BER vs. noise plots. Furthermore hardware synthesis results are provided to demonstrate the effects of parallel sorting networks on area and throughput. In certain cases of practical interest, a modest degradation of 0.2 dB in coding gain is imposed; however due to proposed parallel approximate sorters, the latency of ECN can be reduced by up to a factor of two or be logarithmic to the input sequence length, in certain architectures. To better illustrate the impact of the proposed techniques, a complete NB-LDPC decoder has been implemented and used for evaluation; it is found that a substantial reduction in the number of clock cycles required per decoding iteration is achieved by the proposed techniques, more than 50% in certain cases.

## CoVer: Collaborative Light-Node-Only Verification and Data Availability for Blockchains

- **Status**: ❌
- **Reason**: 블록체인 라이트노드 검증/데이터 가용성 프로토콜로 LDPC ECC와 무관
- **ID**: ieee:9284704
- **Type**: conference
- **Published**: 2-6 Nov. 2
- **Authors**: Steven Cao, Swanand Kadhe, Kannan Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/9284704
- **Abstract**: Validating a blockchain incurs heavy computation, communication, and storage costs. As a result, clients with limited resources, called light nodes, cannot verify transactions independently and must trust full nodes, making them vulnerable to security attacks. Motivated by this problem, we ask a fundamental question: can light nodes securely validate without any full nodes? We answer affirmatively by proposing CoVer, a decentralized protocol that allows a group of light nodes to collaboratively verify blocks even under a dishonest majority, achieving the same level of security for block validation as full nodes while only requiring a fraction of the work. In particular, work per node scales down proportionally with the number of participants (up to a log factor), resulting in computation, communication, and storage requirements that are sublinear in block size. Our main contributions are light-node-only protocols for fraud proofs and data availability.

## Data transmission in automotive applications and security/safety requirements

- **Status**: ❌
- **Reason**: 차량 통신 보안/안전 채널코딩 일반론; 떼어낼 구체적 LDPC 디코더/HW/코드 기법 없음
- **ID**: ieee:9307393
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: Giovanni Cancellieri, Massimo Battaglioni
- **PDF**: https://ieeexplore.ieee.org/document/9307393
- **Abstract**: Radio communications have a fundamental importance for assuring data exchange between vehicles and from infrastructures to vehicles, or vice-versa. With reference to assisted driving and even completely autonomous driving, such communications must satisfy very high degree of security, with the goal of assuring also the safety of drivers and passengers. Two frameworks are expected to provide a support for secure data transmissions: 5G technology and wireless V2X protocols. Interoperability between them and a proper interface with automotive buses are recommended, in order to reach the best performance and to decrease the costs. In this respect, an efficient use of channel coding can guarantee error correction, i.e., reliable communication, and also strong resilience against cyber attacks.

## LDPC Codes Achieve List Decoding Capacity

- **Status**: ❌
- **Reason**: Pure theory: LDPC list-decoding capacity bounds; no decoder/HW/construction to transplant
- **ID**: ieee:9317881
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Jonathan Mosheiff, Nicolas Resch, Noga Ron-Zewi +2
- **PDF**: https://ieeexplore.ieee.org/document/9317881
- **Abstract**: We show that Gallager's ensemble of Low-Density Parity Check (LDPC) codes achieves list-decoding capacity with high probability. These are the first graph-based codes shown to have this property. This result opens up a potential avenue towards truly linear-time list-decodable codes that achieve list-decoding capacity. Our result on list decoding follows from a much more general result: any local property satisfied with high probability by a random linear code is also satisfied with high probability by a random LDPC code from Gallager's distribution. Local properties are properties characterized by the exclusion of small sets of codewords, and include list-decoding, list-recovery and average-radius list-decoding. In order to prove our results on LDPC codes, we establish sharp thresholds for when local properties are satisfied by a random linear code. More precisely, we show that for any local property $\mathcal{P}$, there is some $R^{\ast}$ so that random linear codes of rate slightly less than $R^{\ast}$ satisfy $\mathcal{P}$ with high probability, while random linear codes of rate slightly more than $R^{\ast}$ with high probability do not. We also give a characterization of the threshold rate $R^{\ast}$. This is an extended abstract. The full version is available at https://arxiv.org/abs/1909.06430

## Performance Evaluation of LDPC Coded Partial-Access IDMA Systems with SNR Evolution

- **Status**: ❌
- **Reason**: Uses standard 3GPP NR QC-LDPC as-is for IDMA SNR-evolution eval; no new decoder/code-design contribution
- **ID**: ieee:9293698
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Masaya Yamagishi, Guanghui Song, Tomotaka Kimura +1
- **PDF**: https://ieeexplore.ieee.org/document/9293698
- **Abstract**: The performance of the quasi-cyclic low-density parity-check (QC-LDPC) coded partial-access interleave division multiple access (IDMA) systems is evaluated with the SNR (signal-to-noise ratio) evolution algorithm. The partial access IDMA system is the IDMA system in which the 0s, i.e., non-energy transmission, are inserted into the chip sequence. The SNR evolution algorithm is developed and employed to evaluate the systems. Numerical and simulation results show that the partial access has better BER (bit error rate) performance than that of the conventional full access in a range of low Eb/N0, and the proposed IDMA system with the 3GPP NR QC-LDPC codes has a good error-floor performance.

## Decodable quantum LDPC codes beyond the square root distance barrier using high dimensional expanders

- **Status**: ❌
- **Reason**: Quantum LDPC via high-dim expanders; relies on quantum-specific X/Z-distance, not classical binary BP transplant
- **ID**: ieee:9317916
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Shai Evra, Tali Kaufman, Gilles Zémor
- **PDF**: https://ieeexplore.ieee.org/document/9317916
- **Abstract**: Constructing quantum LDPC codes with a minimum distance that grows faster than a square root of the length has been a major challenge of the field. With this challenge in mind, we investigate constructions that come from high-dimensional expanders, in particular Ramanujan complexes. These naturally give rise to very unbalanced quantum error correcting codes that have a large X-distance but a much smaller Z-distance. However, together with a classical expander LDPC code and a tensoring method that generalises a construction of Hastings and also the Tillich-Zemor construction of quantum codes, we obtain quantum LDPC codes whose minimum distance exceeds the square root of the code length and whose dimension comes close to a square root of the code length. When the ingredient is a 3-dimensional Ramanujan complex, we show that its 2-systole behaves like a square of the log of the complex size, which results in an overall quantum code of minimum distance n1/2logn, and sets a new record for quantum LDPC codes. When we use a 2-dimensional Ramanujan complex, or the 2-skeleton of a 3-dimensional Ramanujan complex, we obtain a quantum LDPC code of minimum distance n1/2log1/2n. We then exploit the expansion properties of the complex to devise the first polynomial time algorithm that decodes above the square root barrier for quantum LDPC codes.

## High Efficiency Continuous-Variable Quantum Key Distribution Based on Quasi-Cyclic LDPC Codes

- **Status**: ❌
- **Reason**: CVQKD 정보조정용 QC-LDPC, 표준 DVB-T2 기반; reconciliation이라 원칙 제외
- **ID**: ieee:9273490
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Kun Zhang, Xue-Qin Jiang, Yan Feng +2
- **PDF**: https://ieeexplore.ieee.org/document/9273490
- **Abstract**: Information reconciliation in the continuousvariable quantum key distribution (CVQKD) plays a vital role on affecting secret key rate as well as maximum transmission distance. It is necessary to search good error-correcting codes in order to improve the performance of reconciliation efficiency. In this work, we construct Quasi-Cyclic (QC) low-density paritycheck (LDPC) codes based on LDPC codes in the digital video broadcasting second generation terrestrial (DVB-T2) standard, and then combine these codes with information reconciliation in the CVQKD system, which can extremely ameliorate the performance of secret key rate and maximum transmission distance. The simulation results show that our proposed QC-LDPC codes can achieve higher reconciliation efficiency of 93.05% compare to DVB-T2 LDPC codes, which means our proposed QC-LDPC codes can obtain better performance of secret key rate and longer maximum transmission distance.

## A Segment CRC Scheme for Polar Codes

- **Status**: ❌
- **Reason**: polar 코드용 segment CRC; 비-LDPC, 부호 비의존 이식 기법 없음
- **ID**: ieee:9334172
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Daolong Wu, Ying Li, Chilian Chen
- **PDF**: https://ieeexplore.ieee.org/document/9334172
- **Abstract**: In this paper, segment cyclic redundancy check (CRC) scheme for polar codes is discussed. Motivated by the non-monotonic property of the first error probabilities of bit-channels used for transmitting information bits and the sequential decoding property of list successive cancellation (LSC) decoding, we propose a segment CRC scheme for polar codes. Both the principle for dividing information sequence into multiple subsequences and decoding procedure are discussed. The analysis shows that the segment CRC scheme can improve the BLER performance of polar codes, reduce the decoding complexity with the cost of undetected error probability compared with conventional CRC scheme. The simulation results verify our analysis. Besides, we also show how different CRC combinations effect the BLER performance of polar codes by simulation. And the simulation result suggests that the last CRC in the CRC combination must be strong in order to find the correct path in the list.

## Design of McEliece Cryptosystem Based on QC-MDPC Codes

- **Status**: ❌
- **Reason**: QC-MDPC 기반 McEliece 암호; 보안/비-LDPC, 떼어낼 디코더 기법 없음
- **ID**: ieee:9334183
- **Type**: conference
- **Published**: 13-15 Nov.
- **Authors**: Guangfu Wu, Rui Yang, Ziheng Dai
- **PDF**: https://ieeexplore.ieee.org/document/9334183
- **Abstract**: The McEliece public key cryptosystem based on QC-MDPC codes has been shown to be a relatively secure system. McEliece cryptosystem has been shown to quantum resistant, which is faster and simpler compared with RSA. When different types of codes are used, most of the ciphers are easy to be cracked. Initially, the keys were all large matrices. For example, the size of the generating matrix of Goppa codes is 1024×524, and it increases exponentially with the increase of the coding length and the number of generated polynomials. In this paper, we use QC-MDPC codes instead of Goppa codes to reduce the key sizes and improve the decoding algorithm, which can resist all kinds of attacks. In the 5G era of the Internet of things, the application of this cryptosystem can guarantee more access security.

## A comparative study of the most perspective radio access technologies for vehicular V2X networks

- **Status**: ❌
- **Reason**: V2X 무선접속기술 개요/비교 서베이, LDPC 무관 — 떼어낼 ECC 기법 없음
- **ID**: ieee:9379171
- **Type**: conference
- **Published**: 12-13 Nov.
- **Authors**: A. Jantošová, J. Morgoš, I. Dolnák +1
- **PDF**: https://ieeexplore.ieee.org/document/9379171
- **Abstract**: The following article provides an overview of currently the most perspective radio access technologies designed for vehicular V2X (Vehicle-to-Everything) environment, mainly for mutual communication among vehicles, and also for communication between vehicles and infrastructure. Principally, the goal of the article is to summarize general knowledge about radio access technologies designed for vehicular V2X networks, which are mainly WLAN based communication technologies and communication technologies based on cellular V2X technologies. In the context of described vehicular V2X communication technologies, the end of this article compares selected communication technologies that could bring a new perspective not only for scientific research but also for the reader who is interested in the issue of the vehicular V2X networks.
