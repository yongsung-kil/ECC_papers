# IEEE Xplore — 2011-03


## Iterative Construction of Regular LDPC Codes from Independent Tree-Based Minimum Distance Bounds

- **Status**: ✅
- **Reason**: tree-based 최소거리 하한 기반 regular LDPC 반복 구성(PEG/ACE 대비 girth 개선) - E 코드설계, 바이너리
- **ID**: ieee:5696808
- **Type**: journal
- **Published**: March 2011
- **Authors**: Eric Psota, Lance C. Pérez
- **PDF**: https://ieeexplore.ieee.org/document/5696808
- **Abstract**: An independent tree-based method for lower bounding the minimum distance of low-density parity-check (LDPC) codes is presented. This lower-bound is then used as the decision criterion during the iterative construction of regular LDPC codes. The new construction algorithm results in LDPC codes with greater girth and improved minimum-distance bounds when compared to regular LDPC codes constructed using the progressive edge-growth (PEG) construction and the approximate cycle extrinsic message degree (ACE)-constrained PEG construction. Simulation results of codes constructed with the new method show improved performance on the additive white Gaussian noise channel at moderate signal-to-noise ratios.

## Efficient Stopping Criterion for Hybrid Weighted Symbol-Flipping Decoding of Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: non-binary LDPC의 symbol-flipping+FFT-QSPA 하이브리드 정지기준 - 비이진 LDPC라 제외
- **ID**: ieee:5701753
- **Type**: journal
- **Published**: March 2011
- **Authors**: Bing Liu, Gaoqi Dou, Wei Tao +1
- **PDF**: https://ieeexplore.ieee.org/document/5701753
- **Abstract**: A two-stage hybrid iterative decoding algorithm with an efficient stopping criterion for nonbinary low-density parity-check (LDPC) codes is proposed, which combines weighted symbol-flipping (WSF) algorithm and fast Fourier transform q-ary sum-product algorithm (FFT-QSPA). The first WSF decoding would be stopped in advance by analyzing the trend of the number of unsatisfied checks. If the first stage decoding is stopped or failed, the second powerful FFT-QSPA is activated. The proposed decoding with the efficient stopping achieves error performance as good as that of FFT-QSPA with a low complexity, and converges faster than hybrid WSF (HWSF) algorithm.

## High Performance Entanglement-Assisted Quantum LDPC Codes Need Little Entanglement

- **Status**: ❌
- **Reason**: 얽힘보조 양자 LDPC(EAQECC) - 양자 전용 개념(얽힘 소비)에 의존, 고전 바이너리 이식 기법 없음
- **ID**: ieee:5714249
- **Type**: journal
- **Published**: March 2011
- **Authors**: Min-Hsiu Hsieh, Wen-Tai Yen, Li-Yi Hsu
- **PDF**: https://ieeexplore.ieee.org/document/5714249
- **Abstract**: Though the entanglement-assisted formalism provides a universal connection between a classical linear code and an entanglement-assisted quantum error-correcting code (EAQECC), the issue of maintaining large amount of pure maximally entangled states in constructing EAQECCs is a practical obstacle to its use. It is also conjectured that the power of entanglement-assisted formalism to convert those good classical codes comes from massive consumption of maximally entangled states. We show that the above conjecture is wrong by providing families of EAQECCs with an entanglement consumption rate that diminishes linearly as a function of the code length. Notably, two families of EAQECCs constructed in the paper require only one copy of maximally entangled state no matter how large the code length is. These families of EAQECCs that are constructed from classical finite geometric LDPC codes perform very well according to our numerical simulations. Our work indicates that EAQECCs are not only theoretically interesting, but also physically implementable. Finally, these high performance entanglement-assisted LDPC codes with low entanglement consumption rates allow one to construct high-performance standard QECCs with very similar parameters.

## Performance Comparisons and Improvements of Channel Coding Techniques for Digital Satellite Broadcasting to Mobile Users

- **Status**: ❌
- **Reason**: 위성방송용 turbo코드 비교 및 IRA-LDPC 적용; 표준 IRA-LDPC 적용 수준으로 떼어낼 신규 기법 없음
- **ID**: ieee:5605633
- **Type**: journal
- **Published**: March 2011
- **Authors**: Stylianos Papaharalabos, David Benmayor, P. Takis Mathiopoulos +1
- **PDF**: https://ieeexplore.ieee.org/document/5605633
- **Abstract**: Digital satellite multimedia broadcasting services in Europe are specified in the Mobile Satellite Services (MSS) frequency band by two recently developed standards, namely the European Telecommunications Standards Institute (ETSI) Satellite Digital Radio (SDR) and the Digital Video Broadcasting-Satellite services to Handhelds (DVB-SH) standards. Commercial deployment of operational systems based on these standards is foreseen in the coming years targeting mainly six large European markets. For these standards, a state-of-the-art channel code is deployed based on the 3rd Generation Partnership Project 2 (3GPP2) specifications having a wide range of coding rates. The purpose of this paper is twofold: (i) It studies and compares, for the first time, the Bit Error Rate (BER) performance of the 3GPP2 turbo code used in the aforementioned systems, in order to serve as a benchmark for system design engineers; and (ii) It investigates novel alternative channel coding schemes, including other state-of-the-art turbo code configurations and also Low-Density Parity-Check (LDPC) codes with linear-time encoding, such as the Irregular Repeat-Accumulate (IRA) codes, in order to improve the performance and/or reduce the complexity in future mobile satellite broadcasting systems. Extensive performance evaluation results in the Additive White Gaussian Noise (AWGN) and uncorrelated Rayleigh/Rician fading channels have shown that the use of turbo codes with higher number of states improves performance against the 3GPP2 turbo codes of up to 0.25 dB but the decoding complexity is almost doubled. Furthermore, the use of duo-binary turbo codes reduces decoding latency and makes them more robust in puncturing with performance improvement against the 3GPP2 turbo codes of up to 0.3 dB but performance degrades at very low coding rates. On the other hand, the use of Rate Compatible (RC)-IRA codes results in smaller performance improvement against the 3GPP2 turbo codes, i.e. up to 0.1 dB, but rate compatibility is used to obtain different coding rates with simple puncturing/extending method.

## Hybrid Linear Programming Based Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 LP 디코딩(interior point) 효율화 + 2단 하이브리드 저복잡도 디코더 - C 이식 가능 디코더 알고리즘
- **ID**: ieee:5699417
- **Type**: journal
- **Published**: March 2011
- **Authors**: Telex Magloire Nkouatchah Ngatched, Attahiru Sule Alfa, Jun Cai
- **PDF**: https://ieeexplore.ieee.org/document/5699417
- **Abstract**: This paper presents a hybrid decoding algorithm for low-density parity-check (LDPC) codes based on the interior point method with barrier function for linear programming (LP) decoding introduced by Wadayama . First, an efficient implementation of Wadayama's algorithm is presented. The main idea behind the modification is to approximate the barrier function for the fundamental polytope defining the code so that it contains only one linear constraint for each of the parity-check constraints. A two-stage hybrid decoding which combines the interior point decoding and a low-complexity decoding algorithm for LDPC codes is then proposed. Simulation results show that the approximations introduced in the proposed algorithms do not result in any performance degradation, while considerably reducing the decoding complexity and latency.

## Security, Reliability in the Networks 4G, Using Elliptic Curve, Irregular LDPC Code and Interleavers of Block

- **Status**: ❌
- **Reason**: 4G 보안+표준 비정규 LDPC를 sum-product로 그대로 사용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:5876421
- **Type**: journal
- **Published**: March 2011
- **Authors**: Washington Fernandez, F. Juan Jara, Oscar Hormazabal
- **PDF**: https://ieeexplore.ieee.org/document/5876421
- **Abstract**: A new system of transmission and reception with security and reliability requests for the networks of fourth generation (4G) is proposed. The security is provided by elliptical curve encryption, system reliability is given by the encoding of irregular low density parity check code (LDPC) and the interleaver. The construction of the irregular LDPC used a technique of low level error, the decoding utilized is the algorithm sum product, and the simulated channel is Additive White Gaussian Noise. According to the results of the proposed system enables transmission and reception achieve a great reliability, because for signal to noise ratio of 4 decibels is 100% of messages received without error

## Using Lossless Data Compression in Data Storage Systems: Not for Saving Space

- **Status**: ✅
- **Reason**: NAND 플래시(및 HDD)에 LDPC ECC 적용, 무손실 압축으로 ECC 잉여도 확보해 쓰기속도 개선 — NAND 직접(A)
- **ID**: ieee:5487513
- **Type**: journal
- **Published**: March 2011
- **Authors**: Ningde Xie, Guiqiang Dong, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5487513
- **Abstract**: Lossless data compression for data storage has become less popular as mass data storage systems are becoming increasingly cheap. This leaves many files stored on mass data storage media uncompressed although they are losslessly compressible. This paper proposes to exploit the lossless compressibility of those files to improve the underlying storage system performance metrics such as energy efficiency and access speed, other than saving storage space as in conventional practice. The key idea is to apply runtime lossless data compression to enable an opportunistic use of a stronger error correction code (ECC) with more coding redundancy in data storage systems, and trade such opportunistic extra error correction capability to improve other system performance metrics in the runtime. Since data storage is typically realized in the unit of equal-sized sectors (e.g., 512 B or 4 KB user data per sector), we only apply this strategy to each individual sector independently in order to be completely transparent to the firmware, operating systems, and users. Using low-density parity check (LDPC) code as ECC in storage systems, this paper quantitatively studies the effectiveness of this design strategy in both hard disk drives and NAND flash memories. For hard disk drives, we use this design strategy to reduce average hard disk drive read channel signal processing energy consumption, and results show that up to 38 percent read channel energy saving can be achieved. For NAND flash memories, we use this design strategy to improve average NAND flash memory write speed, and results show that up to 36 percent write speed improvement can be achieved for 2 bits/cell NAND flash memories.

## Non-Binary Decoder Diversity for Dense or Locally-Dense Parity-Check Codes

- **Status**: ❌
- **Reason**: non-binary Tanner graph로 BP 디코딩하는 non-binary decoder diversity - 비이진 디코더 프레임워크라 제외
- **ID**: ieee:5682554
- **Type**: journal
- **Published**: March 2011
- **Authors**: David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/5682554
- **Abstract**: In this paper, a new and promising framework, called "non-binary decoder diversity", is presented based on the observation that different non-binary Tanner graphs of the same binary code, decoded with a non-binary belief-propagation decoder, can have distinct convergence behaviors and fixed points. The goal of this work is to propose a decoder with linear complexity in the blocklength, and with performance close to maximum-likelihood decoding. This framework is especially interesting for binary codes which are dense or locally-dense, and for which the usual binary iterative decoders perform far from the optimum curves. By using the diversity brought by decoding distinct Tanner graphs of the same code, the proposed technique has very good decoding performance for three very different test cases which are known to be complex decoding problems: (i) near maximum-likelihood decoding (MLD) of BCH codes on the BPSK-AWGN channel, (ii) performance results which outperform bounded distance decoding of BCH codes over a binary symmetric channel (BSC), and finally (iii) decoding performance better than the BCJR-based turbo-decoder for parallel duo-binary turbo-codes.

## More on the Stopping and Minimum Distances of Array Codes

- **Status**: ✅
- **Reason**: 바이너리 array code의 stopping distance/최소거리 분석 - E 코드설계(stopping set 구조), 바이너리 LDPC 패리티검사 구성에 이식 가능
- **ID**: ieee:5682552
- **Type**: journal
- **Published**: March 2011
- **Authors**: M. Esmaeili, M. H. Tadayon, T. A. Gulliver
- **PDF**: https://ieeexplore.ieee.org/document/5682552
- **Abstract**: For q an odd prime and 1≤ m ≤ q, two specific binary qm × q2 parity-check matrices denoted by HP(m, q) and HI(m, q) are considered. The corresponding binary codes, CP(m, q) and CI(m, q), respectively, are called proper and improper array codes with parameters m and q. Given a parity-check matrix H representing a binary code C, let s(H) denote the stopping distance of H and d(C) be the minimum Hamming distance of C. It is known that that s(HI(m, q)) = s(HP(m, q)) = d(CI(m, q)) = d(CP(m, q)) for m ≤ 3. In this paper, we show that these equalities do not hold for all values of m and q. In particular, although s(HP(4, 7)) = d(CP(4, 7)) = 8 we have s(HI(4, 7)) = 9 and d(CI(4, 7)) = 10. It is also shown that s(HP(5,1))dCP(5, 11)) = 10 while s(HI(5,11)) = 11 and d(CI(5, 11)) = 12. This suggests that in many cases the improper array codes would perform better than the proper array codes over the AWGN and binary erasure channels. Performance results are given which confirm this claim. The combinatorial structure of the eight-element stopping sets for H(m ≥ 4,q >; 5) is also determined.

## Reliable Physical Layer Network Coding

- **Status**: ❌
- **Reason**: 물리계층 네트워크코딩(무선 간섭 활용) - 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5699899
- **Type**: journal
- **Published**: March 2011
- **Authors**: Bobak Nazer, Michael Gastpar
- **PDF**: https://ieeexplore.ieee.org/document/5699899
- **Abstract**: When two or more users in a wireless network transmit simultaneously, their electromagnetic signals are linearly superimposed on the channel. As a result, a receiver that is interested in one of these signals sees the others as unwanted interference. This property of the wireless medium is typically viewed as a hindrance to reliable communication over a network. However, using a recently developed coding strategy, interference can in fact be harnessed for network coding. In a wired network, (linear) network coding refers to each intermediate node taking its received packets, computing a linear combination over a finite field, and forwarding the outcome towards the destinations. Then, given an appropriate set of linear combinations, a destination can solve for its desired packets. For certain topologies, this strategy can attain significantly higher throughputs over routing-based strategies. Reliable physical layer network coding takes this idea one step further: using judiciously chosen linear error-correcting codes, intermediate nodes in a wireless network can directly recover linear combinations of the packets from the observed noisy superpositions of transmitted signals. Starting with some simple examples, this paper explores the core ideas behind this new technique and the possibilities it offers for communication over interference-limited wireless networks.

## A Survey on Network Codes for Distributed Storage

- **Status**: ❌
- **Reason**: 분산스토리지 네트워크코딩 서베이 - 리뷰이며 repair bandwidth 중심, 구체적 신규 LDPC 디코더/구성 기여 없음
- **ID**: ieee:5709963
- **Type**: journal
- **Published**: March 2011
- **Authors**: Alexandros G. Dimakis, Kannan Ramchandran, Yunnan Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/5709963
- **Abstract**: Distributed storage systems often introduce redundancy to increase reliability. When coding is used, the repair problem arises: if a node storing encoded information fails, in order to maintain the same level of reliability we need to create encoded information at a new node. This amounts to a partial recovery of the code, whereas conventional erasure coding focuses on the complete recovery of the information from a subset of encoded packets. The consideration of the repair network traffic gives rise to new design challenges. Recently, network coding techniques have been instrumental in addressing these challenges, establishing that maintenance bandwidth can be reduced by orders of magnitude compared to standard erasure codes. This paper provides an overview of the research results on this topic.

## Lossy Compression and Iterative Reconstruction for Encrypted Image

- **Status**: ❌
- **Reason**: 암호화 이미지 손실압축/반복재구성 - 소스코딩(압축), 채널 ECC 아님, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:5665768
- **Type**: journal
- **Published**: March 2011
- **Authors**: Xinpeng Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5665768
- **Abstract**: This work proposes a novel scheme for lossy compression of an encrypted image with flexible compression ratio. A pseudorandom permutation is used to encrypt an original image, and the encrypted data are efficiently compressed by discarding the excessively rough and fine information of coefficients generated from orthogonal transform. After receiving the compressed data, with the aid of spatial correlation in natural image, a receiver can reconstruct the principal content of the original image by iteratively updating the values of coefficients. This way, the higher the compression ratio and the smoother the original image, the better the quality of the reconstructed image.

## Ultra Low Frequency Power-Line Communications Using a Resonator Circuit

- **Status**: ❌
- **Reason**: 전력선통신 공진회로 디지털전송 - LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:5699386
- **Type**: journal
- **Published**: March 2011
- **Authors**: David W. Rieken, Michael R. Walker II
- **PDF**: https://ieeexplore.ieee.org/document/5699386
- **Abstract**: A novel device for the transmission of digital information over power lines is introduced. The transmission circuit is passive, using a resonator circuit to create a narrowband disturbance in the system. This disturbance can be detected over great distances and, in many cases, through distribution transformers. This makes it a promising solution to power-line communication problems in distribution systems that are sparsely populated over large geographical expanses. Modulation algorithms are introduced. We discuss results obtained using a prototype to transmit signals on a real distribution system.

## The Sensing Capacity of Sensor Networks

- **Status**: ❌
- **Reason**: 센서 네트워크 sensing capacity 이론 bound, LDPC ECC와 무관, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:5714263
- **Type**: journal
- **Published**: March 2011
- **Authors**: Yaron Rachlin, Rohit Negi, Pradeep K. Khosla
- **PDF**: https://ieeexplore.ieee.org/document/5714263
- **Abstract**: This paper demonstrates fundamental limits of sensor networks for detection problems where the number of hypotheses is exponentially large. Such problems characterize many important applications including detection and classification of targets in a geographical area using a network of seismic sensors, and detecting complex substances with a chemical sensor array. We refer to such applications as large-scale detection problems. Using the insight that these problems share fundamental similarities with the problem of communicating over a noisy channel, we define the “sensing capacity” and lower bound it for a number of sensor network models. The sensing capacity expression differs significantly from the channel capacity due to the fact that for a fixed sensor configuration, codewords are dependent and nonidentically distributed. The sensing capacity provides a bound on the minimal number of sensors required to detect the state of an environment to within a desired accuracy. The results differ significantly from classical detection theory, and provide an intriguing connection between sensor networks and communications. In addition, we discuss the insight that sensing capacity provides for the problem of sensor selection.

## Information Theoretic Modeling and Analysis for Global Interconnects With Process Variations

- **Status**: ❌
- **Reason**: 공정변이 글로벌 인터커넥트 정보이론 achievable rate 분석; 순수 이론bound로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5352230
- **Type**: journal
- **Published**: March 2011
- **Authors**: Stojan Z. Denic, Bane Vasic, Charalambos D. Charalambous +2
- **PDF**: https://ieeexplore.ieee.org/document/5352230
- **Abstract**: As the CMOS semiconductor technology enters nanometer regime, interconnect processes must be compatible with device roadmaps and meet manufacturing targets at the specified wafer size. The resulting ubiquitous process variations cause errors in data delivering through interconnects. This paper proposes an Information Theory based design method to accommodate process variations. Different from the traditional delay based design metric, the current approach uses achievable rate to relate interconnect designs directly to communication applications. More specifically, the data communication over a typical interconnect, a bus, subject to process variations (“uncertain” bus), is defined as a communication problem under uncertainty. A data rate, called the achievable rate, is computed for such a bus, which represents the lower bound on the maximal data rate attainable over the bus. When a data rate applied over the bus is smaller than the achievable data rate, a reliable communication can be guaranteed regardless of process variations, i.e., a bit error rate arbitrarily close to zero is achievable. A single communication strategy to combat the process variations is proposed whose code rate is equal to the computed achievable rate. The simulations show that the variations in the interconnect resistivity could have the most harmful effect regarding the achievable rate reduction. Also, the simulations illustrate the importance of taking into account bus parasitic parameters correlations when measuring the influence of the process variations on the achievable rates.

## First experimental demonstration of nonbinary LDPC-coded modulation suitable for high-speed optical communications

- **Status**: ❌
- **Reason**: nonbinary LDPC-coded modulation 실험 시연 — 비이진 LDPC 제외
- **ID**: ieee:5875672
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Jiaojiao Fu, Murat Arabaci, Ivan B. Djordjevic +3
- **PDF**: https://ieeexplore.ieee.org/document/5875672
- **Abstract**: The first experimental demonstration of nonbinary-LDPC-coded optical transmission is presented. Using DQPSK, we can achieve >;8dB and ~10dB net coding gains at the BER of 10-6 in the absence and presence of I/Q imbalance, respectively.

## Three-dimensional subcarrier-multiplexed nonbinary-LDPC-coded modulation schemes enabling ultra high speed optical communications

- **Status**: ❌
- **Reason**: 3D nonbinary LDPC-coded modulation — 비이진 LDPC 제외
- **ID**: ieee:5875673
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/5875673
- **Abstract**: We propose nonbinary-LDPC-coded modulation schemes employing subcarrier-multiplexing and three-dimensional constellations. We improve coding gains of conventional PDM-M-QAM by 2.17dB and 2.92dB, for M = 8 and M = 16, respectively, at the BER of 10-7.

## On the reverse concatenated coded-modulation for ultra-high-speed optical transport

- **Status**: ❌
- **Reason**: BCH+LDPC reverse concatenated coded-modulation, 광통신 특이적이며 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:5875671
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/5875671
- **Abstract**: We propose reverse concatenated code with inner BCH code and outer LDPC code. BCH decoder is based on MAP-decoding that provides high-accuracy-reliabilities for suboptimum-LDPC-decoder, leading to performance comparable to long-girth-12-LDPC codes, but with lower decoder-complexity.

## Layered decoding of nonbinary LDPC codes suitable for high-speed optical communications

- **Status**: ❌
- **Reason**: nonbinary LDPC layered decoding — 비이진 LDPC 제외
- **ID**: ieee:5875670
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/5875670
- **Abstract**: We propose using layered update rule in decoding nonbinary LDPC codes. Only 10-15 iterations suffice for good performance. Also, for the same BER performance, it increases throughput by twofold compared to conventional flooding update rule.

## Coded multidimensional pulse amplitude modulation for ultra-high-speed optical transmission

- **Status**: ❌
- **Reason**: 광통신용 다차원 PAM 변조 제안 — LDPC ECC 기법 아님, 떼어낼 것 없음
- **ID**: ieee:5875090
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Ivan B. Djordjevic, Lei Xu, Ting Wang
- **PDF**: https://ieeexplore.ieee.org/document/5875090
- **Abstract**: We propose a coded N-dimensional pulse-amplitude modulation (ND-PAM) suitable for ultra-high-speed serial optical transport. The polarization-multiplexed-ND-PAM significantly outperforms corresponding polarization-multiplexed-QAM counterpart in terms of OSNR sensitivity (>; 4 dB at symbol rate 31.25 GS/s), while enabling beyond 400 Gb/s transmission.

## Low-density parity-check codes and (binary) message passing algorithms

- **Status**: ❌
- **Reason**: LDPC+바이너리 메시지패싱 강연 슬라이드 모음, 교과서 수준 신규 기여 없음
- **ID**: ieee:5875669
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Gerhard Kramer, Alexander von Humboldt
- **PDF**: https://ieeexplore.ieee.org/document/5875669
- **Abstract**: A collection of slides from the author's conference presentation is given. The following topics are discussed: low-density parity-check code; iterative decoding; demodulation; optimization; irregular LDPC code; and binary message passing algorithm.

## FPGA verification of a single QC-LDPC code for 100 Gb/s optical systems without error floor down to BER of 10−15

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC FPGA 검증, error floor-free 1e-15 — 이식 가능 HW 아키텍처/코드설계(D/E)
- **ID**: ieee:5875607
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Deyuan Chang, Fan Yu, Zhiyu Xiao +6
- **PDF**: https://ieeexplore.ieee.org/document/5875607
- **Abstract**: We present FPGA-based emulation results of a single QC-LDPC code with 20% redundancy designed for applications in 100 Gb/s optical transmission systems. Error floor-free transmission can be achieved at BER of 10−15 with a Q factor of 5.9 dB.

## Progress in soft-decision FEC

- **Status**: ❌
- **Reason**: soft-decision FEC LDPC 실무 구현 논의(서베이성), 구체적 신규 디코더/구성/정량비교 없음
- **ID**: ieee:5875249
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Takashi Mizuochi, Yoshikuni Miyata, Kazuo Kubo +3
- **PDF**: https://ieeexplore.ieee.org/document/5875249
- **Abstract**: We discuss the practical implementation of LDPC codes in soft-decision FEC for 100 Gb/s digital coherent systems. The question of the definition of net coding gain for differential QPSK used to avoid cycle slip is raised.

## 1-Tb/s large girth LDPC-coded coherent optical OFDM transmission over 1040-km standard single-mode fiber

- **Status**: ❌
- **Reason**: 광통신 OFDM 실험 시연, girth-12 LDPC를 베이스라인으로 사용 — 새 코드설계/디코더 기여 없음, 응용 특이적
- **ID**: ieee:5875083
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Qi Yang, Zhixue He, Wu Liu +4
- **PDF**: https://ieeexplore.ieee.org/document/5875083
- **Abstract**: We experimentally demonstrate 1-Tb/s CO-OFDM transmission over 1040-km standard single-mode fiber using 50% overhead girth-12 LDPC-coded 16-QAM. More than 4-dB improvement in OSNR sensitivity is achieved over conventional 4-QAM while maintaining the same spectral efficiency.

## Coded modulation in optical communications

- **Status**: ❌
- **Reason**: 광통신 coded modulation 리뷰; iterative demapping뿐 NAND 바이너리 LDPC에 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:5875459
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Henning Bülow, Ekaterina Masalkina
- **PDF**: https://ieeexplore.ieee.org/document/5875459
- **Abstract**: Coded modulation schemes for optical transport are reviewed and coding of 4-D constellations is discussed including iterative demapping for soft-detection of polarization-switched QPSK which achieves 1.5dB sensitivity gain compared to polarization-multiplexed QPSK.

## Study on the performance of decision-aided maximum likelihood phase estimation with a forgetting factor

- **Status**: ❌
- **Reason**: 광통신 위상추정(maximum likelihood) 알고리즘 — LDPC ECC 무관
- **ID**: ieee:5875114
- **Type**: conference
- **Published**: 6-10 March
- **Authors**: Shaoliang Zhang, Lei Xu, Pooi Yuen Kam +2
- **PDF**: https://ieeexplore.ieee.org/document/5875114
- **Abstract**: A structure of non-adaptive decision-aided maximum likelihood is demonstrated by introducing a forgetting factor via both analysis and experiments, which achieves the same performance as the adaptive phase estimation while reducing the algorithm complexity.

## Frame synchronization without attached sync markers

- **Status**: ❌
- **Reason**: 프레임 동기화(ASM 없는 sync) 기법, LDPC는 부수 언급, 떼어낼 ECC/디코더 기법 없음.
- **ID**: ieee:5747327
- **Type**: conference
- **Published**: 5-12 March
- **Authors**: Jon Hamkins
- **PDF**: https://ieeexplore.ieee.org/document/5747327
- **Abstract**: We describe a method to synchronize codeword frames without making use of attached synchronization markers (ASMs). Instead, the synchronizer identifies the code structure present in the received symbols, by operating the decoder for a handful of iterations at each possible symbol offset and forming an appropriate metric. This method is computationally more complex and doesn't perform as well as frame synchronizers that utilize an ASM; nevertheless, the new synchronizer acquires frame synchronization in about two seconds when using a 600 kbps software decoder, and would take about 15 milliseconds on prototype hardware. It also eliminates the need for the ASMs, which is an attractive feature for short uplink codes whose coding gain would be diminished by the overheard of ASM bits. The lack of ASMs also would simplify clock distribution for the AR4JA low-density parity-check (LDPC) codes and adds a small amount to the coding gain as well (up to 0.2 dB).

## A sorting-based architecture of finding the first two minimum values for LDPC decoding

- **Status**: ✅
- **Reason**: row operation용 first-two-minimum 탐색 신규 정렬기반 HW 아키텍처, min-sum 디코더에 직접 이식(C/D)
- **ID**: ieee:5759850
- **Type**: conference
- **Published**: 4-6 March 
- **Authors**: Qian Xie, Zhixiang Chen, Xiao Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/5759850
- **Abstract**: This paper presents an efficient architecture of finding the first two minimum values for row operation in LDPC decoding. Given a set of numbers X, efficient algorithm and its corresponding hardware implementation for finding the first minimum value, min_1st, second minimum value, min_2nd and the position of min_1st are greatly needed in LDPC decoder design. The design is based on sorting-based approach proposed in. Compared to the conventional architecture, our architecture performs better in both speed and area. An extension method is also presented to apply the proposed architecture when the number of inputs is an any positive integer.

## Design of turbo codes without 4-cycles in Tanner graph representation for message passing algorithm

- **Status**: ✅
- **Reason**: turbo를 블록부호로 보고 sparse 패리티검사행렬 구성+4-cycle 제거 기준 제시, 바이너리 LDPC BP에 이식 가능(C/E 예외)
- **ID**: ieee:5759853
- **Type**: conference
- **Published**: 4-6 March 
- **Authors**: Ying Cui, Xiao Peng, Satoshi Goto
- **PDF**: https://ieeexplore.ieee.org/document/5759853
- **Abstract**: Turbo code and Low Density Parity Check (LDPC) code are both recommended as FEC code in many communication standards owing to their impressive error correcting performance. Aiming at the common architecture which can decode both of the two codes, this paper describes the method of decoding turbo codes with message passing algorithm which is conventionally used for LDPC codes. In this method, turbo codes are viewed as block codes and the sparse parity check matrices are constructed through Smith Decomposition or GBT (Generator matrix based transformation). In order to guarantee decoding performance, we propose the criterion of turbo codes with no 4-cycles, which is mathematically proved and demonstrated by the simulation results.

## Sparse Graph Codes for the Two-Way Relay Network with Correlated Sources

- **Status**: ❌
- **Reason**: two-way relay 상관소스용 sparse graph code의 degree distribution 최적화 - 소스-채널 결합/네트워크 코딩, NAND에 떼어낼 ECC 구성 기법 없음
- **ID**: ieee:5749523
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Gottfried Lechner, Roy Timo, Lawrence Ong
- **PDF**: https://ieeexplore.ieee.org/document/5749523
- **Abstract**: We consider the two-way relay network where two nodes communicate via a relay. We assume that the data at the nodes are correlated (e.g., measurements in a sensor network) and that there is no direct communication between the nodes. The nodes communicate via the relay using a two-phase protocol consisting of an uplink part over an orthogonal multiple access channel and a downlink part over a broadcast channel. The individual codes as well as the overall system can be represented by a joint factor graph consisting of a source code at each node, a channel code for the each uplink and a channel code for the downlink. The optimality of separation of source and channel coding implies that it is optimal to individually design these codes. We focus on low-density parity-check codes where code design corresponds to the optimisation of their degree distributions.

## Formulating Binary Compressive Sensing Decoding with Asymmetrical Property

- **Status**: ❌
- **Reason**: 바이너리 압축센싱(소스 압축) verification-based 디코더 분석 - 채널코딩 ECC가 아닌 소스코딩, sensing matrix 설계 (소스 코딩 제외)
- **ID**: ieee:5749479
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Xiao Lin Liu, Chong Luo, Feng Wu
- **PDF**: https://ieeexplore.ieee.org/document/5749479
- **Abstract**: This paper mathematically analyzes the verification based message passing decoder for the binary compressive sensing (CS) compression problem, toward the goal of judging whether the decoding will be successful prior to the decoding process and of providing design guidelines of sensing matrices for better coding performance. For a biased binary source with unequal percentage of bit "0" and "1", we observe that the recovery probabilities for bit "0" and "1" are different during each round of evolution in the decoding process. We refer to this property as asymmetrical recovery. To authors' best knowledge, this paper is the first one to formulate CS decoding by taking the asymmetrical recovery into account. With the new formulation, the recursion of unrecoverable probability of source bits can be characterized more precisely than previous formulations. Furthermore, as an important property of CS decoding, we also characterize the variation on asymmetrical recovery in different rounds of evolution. The simulation results show that the new formulation has a close match with the actual decoding. Finally, we derive design guidelines for random sensing matrices from the source coding perspective.

## Gigabit rate achieving low-power LDPC codes: Design and architecture

- **Status**: ✅
- **Reason**: 저전력 LDPC 코드 패밀리 설계+동일 HW로 다양한 블록길이 디코딩하는 통합 디코더 아키텍처(D/E 이식 가능)
- **ID**: ieee:5779435
- **Type**: conference
- **Published**: 28-31 Marc
- **Authors**: Shadi Abu-Surra, Eran Pisek, Thomas Henige
- **PDF**: https://ieeexplore.ieee.org/document/5779435
- **Abstract**: The quality of any communication system is greatly determined by the performance excellence of the selected channel coding scheme. In this work, we propose algorithms for designing LDPC channel coding schemes. The proposed designs are suitable for achieving Gigabit communications with relatively low-power consumption. We design LDPC code family with fixed block length and no puncturing. Also, starting with an LDPC code base-family, we construct LDPC code families with longer block length but decodable using the same hardware as the base-family. We propose a unified decoder architecture, which can decode all LDPC codes in the designed base-family as well as all LDPC codes in the derived code families with longer block length.

## Serially concatenated LT code with DQPSK modulation

- **Status**: ❌
- **Reason**: LT/fountain+DQPSK rateless 부호, 비-LDPC, EXIT 최적화; 채널 ECC 이식 기법 없음
- **ID**: ieee:5779408
- **Type**: conference
- **Published**: 28-31 Marc
- **Authors**: Iqbal Hussain, Ming Xiao, Lars K. Rasmussen
- **PDF**: https://ieeexplore.ieee.org/document/5779408
- **Abstract**: We consider serial concatenation of a Luby Transform (LT) code with a differential quadrature phase-shift-keying (DQPSK) modulator for transmission over an additive white Gaussian noise (AWGN) Channel. Assuming a target average rate for the operation of the rateless LT DQPSK scheme, the degree distribution of the LT code is optimized in terms of convergence threshold using extrinsic information transfer (EXIT) charts. From the EXIT chart analysis, we show that the proposed LT DQPSK scheme has a similar convergence performance, but lower complexity, as compared to a Raptor code with differential modulation, and a LDPC code optimized for DQPSK. The EXIT chart analysis framework is also applied to evaluate the throughput performance for the three schemes in terms of the average code rate as a function of the signal-to-noise ratio. The comparison demonstrates that the proposed structure is well-suited for adaptive-rate transmission over a wide range of rates.

## A High-efficiency LDPC Encoder for CMMB with Dynamic Programming

- **Status**: ❌
- **Reason**: CMMB 표준 LDPC 인코더(LU분해 동적계획), 디코더/구성 신규 기여 없는 인코딩 효율화
- **ID**: ieee:5750893
- **Type**: conference
- **Published**: 28-29 Marc
- **Authors**: Zhibin Zeng
- **PDF**: https://ieeexplore.ieee.org/document/5750893
- **Abstract**: In this paper, a high-efficiency LDPC encoder for CMMB based on LU decomposition with dynamic programming is proposed. Results from simulation and implementation shows that this method can decrease complexity of encoding and improve encoding rate effectively.

## Studies on Space-Time Block Codes with LDPC

- **Status**: ❌
- **Reason**: LDPC-STBC 결합 무선 응용, 표준 LDPC 부수 언급, 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:5750987
- **Type**: conference
- **Published**: 28-29 Marc
- **Authors**: Li Bai Ping, Wang Ting, Li Juming
- **PDF**: https://ieeexplore.ieee.org/document/5750987
- **Abstract**: Firstly, this paper gives a simple introduction of the encoding/decoding theory of LDPC and Space-time coding. And it carries out a detailed research and analysis on LDPC coding system and the space-time block coding system. Then, LDPC and space-time coding are combined. The performance of LDPC-STBC under AWGN channel is given through computer simulation. The simulation results show that this method can improve the coding performance. In addition, it indicates a detail comparison of the different types of LDPC code weight and STBC receiving ways.

## Design of bilayer lengthened LDPC codes for Rayleigh fading relay channels

- **Status**: ❌
- **Reason**: 릴레이 채널용 bilayer LDPC 코드 설계, Rayleigh fading relay 응용 특이적이며 NAND ECC로 이식할 신규 기법 없음
- **ID**: ieee:5766201
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Osso Vahabzadeh, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/5766201
- **Abstract**: Recently, two classes of high rate bilayer low-density parity-check (LDPC) codes have been proposed for Gaussian relay channels using bilayer density evolution technique. These two classes include bilayer lengthened LDPC codes and bilayer expurgated LDPC codes that have been used in a decode-and-forward relaying strategy. In this paper, we first study the decode-and-forward achievable rates for a Rayleigh fading relay channel. Then, we design bilayer lengthened LDPC codes for this channel model in different SNR regimes, namely, when the link between the source and the relay is much stronger than the link between the source and the destination and when the SNRs of these links are comparable.

## A Markov chain model for Edge Memories in stochastic decoding of LDPC codes

- **Status**: ✅
- **Reason**: stochastic decoding Edge Memory의 Markov chain 수렴 분석, NAND LDPC에 이식 가능한 디코더 알고리즘 기법(C)
- **ID**: ieee:5766114
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Kuo-Lun Huang, Vincent Gaudet, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/5766114
- **Abstract**: Stochastic decoding is a recently proposed method for decoding Low-Density Parity-Check (LDPC) codes. Stochastic decoding is, however, sensitive to the switching activity of stochastic bits, which can result in a latching problem. Using Edge Memories (EMs) has been proposed as a method to counter the latching problem in stochastic decoding. In this paper, we introduce a Markov chain model for EMs and study state transitions over decoding cycles. The proposed method can be used to determine the convergence and the required number of decoding cycles in stochastic decoding. Moreover, it can help to study the behavior of decoding process and to estimate the decoding time.

## Concatenation of LDPC codes with Golden space-time block codes over the block fading MIMO channels: System design and performance analysis

- **Status**: ❌
- **Reason**: LDPC+Golden STBC 연접, 표준 SISO BP를 그대로 사용한 MIMO 응용, 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:5766255
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Jin-Taek Seong, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/5766255
- **Abstract**: The use of low-density parity-check (LDPC) codes over the multi-input multi-output (MIMO) channels has shown the performance to be achieved to the capacity limit. For the 2 × 2 MIMO system, the Golden codes were recently developed as the optimal space-time codes with a full rate and a full diversity gain. In this paper, we give the detailed system design for the concatenated coding scheme, which consists of the LDPC codes as the outer code and the Golden space-time block codes (STBC) as the inner code. The outer binary block codeword transforms itself onto the sequence of the internal space-time (IST) symbols according to a fixed constellation map. The soft-input soft-output (SISO) message passing decoder of the LDPC codes can be combined with a SISO constellation de-mapper as the Golden STBC decoder. They exchange the extrinsic messages in turbo-iterations. We evaluate the error performance for different block lengths of the proposed system. For the Golden codes concatenated with the LDPC codes, the maximum-likelihood union bound analysis is used for performance benchmarking.

## Secret key generation through OFDM multipath channel

- **Status**: ❌
- **Reason**: 보안 키 생성 Slepian-Wolf 소스코딩 + non-binary LDPC 포함, 채널 ECC 아님, 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:5766103
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Yanpei Liu, Stark C. Draper, Akbar M. Sayeed
- **PDF**: https://ieeexplore.ieee.org/document/5766103
- **Abstract**: We analyze the fundamental limits of key generation and describe an implementation based on error correcting codes. We show that key extraction based on channel coefficients significantly outperforms key extraction based on received signal strength indicators (RSSI). The development in this paper is based on an IEEE 802.11a orthogonal frequency-division multiplexing (OFDM) model and We demonstrate that it is feasible to use the sampled channel coefficients in OFDM as the key source. The key extraction problem is cast as a Slepian-Wolf coding and decoding problem. We construct regular and irregular forms of binary and non-binary low-density parity check (LDPC) codes to prototype our key extraction.

## Random complex field code design for security over wiretap channels

- **Status**: ❌
- **Reason**: wiretap 보안용 random complex field code 설계(비-LDPC 부호), 채널 ECC 디코더 기법 아님
- **ID**: ieee:5766212
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Jiaxi Xiao, Xiaoli Ma, Steven W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/5766212
- **Abstract**: Wiretap channel has caught a lot of attention recently in secured communications. A commonly adopted wiretap model is that the main channel is noiseless and the eavesdroppers channel is binary erasure channel (BEC). LDPC codes have been applied to achieve strong secrecy. However, it lacks design flexibility balancing on security and reliability, and cannot illustrate the fundamental tradeoffs among erasure rate, secrecy rate, and the security performance. In this paper, we propose a random complex field code (RCFC) design for such wiretap channels. The design of RCFCs is systematic and flexible for any secrecy rate. By using the proposed code design, the desired receiver can decode the confidential information without any error (in the absence of noise). Simultaneously, when the secrecy rate is below or equal to the secrecy capacity, we prove that the mutual information between the confidential message and the decoded message given by the eavesdropper converges to zero with the codeword length goes to infinity. Additionally, our RCFC design is the first one which provides a platform to tradeoff secrecy rate with the security performance.

## Unequal error protection for noncoherent random linear network coding

- **Status**: ❌
- **Reason**: random linear network coding의 불균등 오류보호, 신호공간 분해 기법으로 LDPC 디코더와 무관
- **ID**: ieee:5766236
- **Type**: conference
- **Published**: 23-25 Marc
- **Authors**: Zhiyuan Yan, Bruce W. Suter
- **PDF**: https://ieeexplore.ieee.org/document/5766236
- **Abstract**: Since random linear network coding (RLNC) is susceptible to various errors, error control for RLNC is important and has attracted a lot of attention recently. Previous error control schemes for RLNC provide uniform error protection to all the packets in a session. However, in practice packets often have different significance and hence require different levels of protection. Furthermore, uniform error protection may be unnecessary or infeasible in some scenarios. In this paper, we investigate unequal error protection for RLNC. In particular, based on a novel signal space decomposition, we propose a new error control scheme that provides different levels of protection to two classes of packets transmitted to the same set of destination nodes.

## Reliable distribution of electronic media in vehicular networks based on fountain codes

- **Status**: ❌
- **Reason**: 차량망 fountain code 응용, LDPC 아닌 fountain/erasure 코딩으로 제외 대상
- **ID**: ieee:5936539
- **Type**: conference
- **Published**: 23-24 Marc
- **Authors**: Robert Budde, Stefan Nowak, Ruediger Kays
- **PDF**: https://ieeexplore.ieee.org/document/5936539
- **Abstract**: Distribution of electronic media to cars plays a key role when it comes to the deployment of car-to-infrastructure communications. Like in other point-to-multipoint systems, the application of fountain codes is highly promising. In this paper, we investigate the applicability of fountain codes in an infrastructure-based automotive communication system and introduce an expedient method to design such a system. By means of system simulations we compare its performance with respect to a data carousel.

## The Design of Network Low Density Parity Check Codes for Wireless Multiple-Access Relay Networks

- **Status**: ❌
- **Reason**: 무선 릴레이 네트워크 NLDPC 설계, fading용 bilayer Gaussian Approx 밀도진화—응용 특이적이고 NAND에 떼어낼 기법 없음
- **ID**: ieee:5763465
- **Type**: conference
- **Published**: 22-25 Marc
- **Authors**: Ying Li, Lili Wang, Yue Sun
- **PDF**: https://ieeexplore.ieee.org/document/5763465
- **Abstract**: Based on the relaying scheme which permits the relay node to jointly encode the data information from two source nodes, a new network low density parity check (NLDPC) code is designed for the Rayleigh fading channel. Since the log-likelihood ratio (LLR) of the signal received from the fading channel is not a Gaussian random variable, the Gaussian Approximation algorithm cannot be employed directly in the density evolution. In this paper, a new hybrid bilayer Gaussian Approximation algorithm is derived to predict the performance of NLDPC codes over Rayleigh fading channels, based on which an optimization algorithm is developed to search for the degree distribution of the NLDPC code. Simulations show that, in a network with two sources, one relay and one destination, the system with the designed NLDPC code holds a performance gap of less than 0.6dB from the threshold.

## On the Rateless Character of Irregular RA Codes

- **Status**: ❌
- **Reason**: IRA 코드 rateless 특성·BEC 용량달성 분석, 무선/erasure 응용 이론으로 NAND 이식 기법 없음
- **ID**: ieee:5763585
- **Type**: conference
- **Published**: 22-25 Marc
- **Authors**: Rong Sun, Jingwei Liu, Pingli Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/5763585
- **Abstract**: This paper introduces the construction of systematic irregular RA codes. The encoding line is used to describe the graph structure of IRA codes. Two interleaving strategies for IRA codes are analyzed and it is shown that the two interleaving strategies are equal. The rateless character of IRA codes is also shown. The performances of IRA codes with different rate in binary erasure channel are simulated. Simulation results show that the IRA codes is capacity achieving. The error floor performance of IRA codes is analyzed and the modified encoding method is presented to lower the error floor.

## Semi-random Kite Codes over Fading Channels

- **Status**: ❌
- **Reason**: Kite 코드(rateless)는 fading 채널용 비-LDPC계열 sparse 코드, ML 디코딩 union bound 분석으로 NAND 바이너리 LDPC BP에 이식할 신규 디코더 없음
- **ID**: ieee:5763463
- **Type**: conference
- **Published**: 22-25 Marc
- **Authors**: Bo Bai, Baoming Bai, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/5763463
- **Abstract**: This paper introduces a new class of rate less forward error correction codes named semi-random Kite (SR-Kite) codes, which can be described by a sparse semi-random parity-check matrix in systematic form. SR-Kite codes have not only rate less property, but also low error floors. We present a simulation-based greedy optimization algorithm to design the degree distribution of SR-Kite codes for independent Rayleigh fading channels. The performances of SR-Kite codes under maximum likelihood decoding are analyzed for both AWGN and independent Rayleigh fading channels via union bound. Both the analysis and simulation results show that the proposed codes perform well over AWGN and fading channels within a wide range of signal-to-noise-ratios.

## New QC-LDPC codes implementation on FPGA platform in Rayleigh fading environment

- **Status**: ✅
- **Reason**: QC-LDPC FPGA(VHDL) 구현 및 large girth 코드 설계, 이식 가능 HW/코드설계 기여(D/E)
- **ID**: ieee:5958912
- **Type**: conference
- **Published**: 20-23 Marc
- **Authors**: Farid Ghani, Abid Yahya, Abdul Kader
- **PDF**: https://ieeexplore.ieee.org/document/5958912
- **Abstract**: This paper presents performance of Quasi-Cyclic low-density parity-check (QC-LDPC) codes on a flat Rayleigh fading channels by employing DPSK modulation scheme. The BER curves show that large girth and diversity level robust the system performance. Moreover, Prototype architecture of the LDPC codes has been implemented by writing Hardware Description Language (VHDL) code and targeted to a Xilinx Spartan-3E XC3S500E FPGA chip. Simulation results show that the proposed QC-LDPC codes achieve a 0.1dB coding gain over randomly constructed codes and perform 1.3 dB from the Shannon-limit at a BER of 10−6 with a code rate of 0.89 for block length of 1332.

## A flexible high throughput multi-ASIP architecture for LDPC and turbo decoding

- **Status**: ✅
- **Reason**: LDPC/turbo 멀티-ASIP 디코더 아키텍처, LDPC 모드 데이터패스 HW 기법(D) 이식 가능
- **ID**: ieee:5763047
- **Type**: conference
- **Published**: 14-18 Marc
- **Authors**: Purushotham Murugappa, Rachid Al-Khayat, Amer Baghdadi +1
- **PDF**: https://ieeexplore.ieee.org/document/5763047
- **Abstract**: In order to address the large variety of channel coding options specified in existing and future digital communication standards, there is an increasing need for flexible solutions. This paper presents a multi-core architecture which supports convolutional codes, binary/duo-binary turbo codes, and LDPC codes. The proposed architecture is based on Application Specific Instruction-set Processors (ASIP) and avoids the use of dedicated interleave/deinterleave address lookup memories. Each ASIP consists of two datapaths one optimized for turbo and the other for LDPC mode, while efficiently sharing memories and communication resources. The logic synthesis results yields an overall area of 2.6mm2 using 90nm technology. Payload throughputs of up to 312Mbps in LDPC mode and of 173Mbps in Turbo mode are possible at 520MHz, fairing better than existing solutions.

## BCH code based multiple bit error correction in finite field multiplier circuits

- **Status**: ❌
- **Reason**: BCH 코드 기반 GF 곱셈기 오류정정, 암호회로 fault tolerance. 비-LDPC, 디코더 기법 이식성 없음
- **ID**: ieee:5770792
- **Type**: conference
- **Published**: 14-16 Marc
- **Authors**: Mahesh Poolakkaparambil, Jimson Mathew, Abusaleh M. Jabir +2
- **PDF**: https://ieeexplore.ieee.org/document/5770792
- **Abstract**: This paper presents a design methodology for multiple bit error detection and correction in Galois field arithmetic circuits such as the bit parallel polynomial basis (PB) multipliers over GF(2m). These multipliers are crucial in most of the cryptographic hardware designs and hence it is essential to ensure that they are not vulnerable to security threats. Security threats arising from injected soft (transient) faults into a cryptographic circuit can expose the secret information, e.g. the secret key, to an attacker. To prevent such soft or transient fault related attacks, we consider fault tolerance as a method of mitigation. Most of the current fault tolerant schemes are only multiple bit error detectable but not multiple bit error correctable. Keeping this in view, we present a multiple bit error correction scheme based on the BCH codes, with an efficient bit-parallel Chien search module. This paper details the design procedure as well as the hardware implementation specs. Comparison with existing methods demonstrate improved area, and reduced delay performances.

## Analysis the performance of a LDPC coded FSO system with Q-ary pulse-position modulation

- **Status**: ❌
- **Reason**: FSO Q-ary PPM에 LDPC 적용한 BER 성능평가 응용, 새 디코더·구성·HW 기여 없음
- **ID**: ieee:5764032
- **Type**: conference
- **Published**: 11-13 Marc
- **Authors**: Bobby Barua, Dalia Barua
- **PDF**: https://ieeexplore.ieee.org/document/5764032
- **Abstract**: Free-space optical communication is an attractive and cost-effective solution for high-rate image, voice, and data transmission. However, optical wave propagation through the air experiences fluctuation in amplitude and phase due to atmospheric turbulence. In this paper, an analytical approach is presented to evaluate the bit error rate performance of a free space optical link using LDPC coded Q-ary optical PPM through atmospheric turbulence channel. Performance results are evaluated for multiple-laser and multiple photo-detector combination without and with LDPC code to combat the effect of atmospheric turbulence. The performance results are evaluated in terms of bit error rate (BER) and coding gain. It is found that LDPC coded system provides significant coding gain of 10 to 20 dB over uncoded system can be evaluated at BER 10-12 for multiple source and photo-detector combinations. It also provides better performance under strong turbulence rather than weak turbulence conditions.

## Performance of LDPCC-MC-CDMA in wideband shortwave channel

- **Status**: ❌
- **Reason**: 표준 LDPC를 MC-CDMA/OFDM 무선 시스템에 적용한 응용 논문, 떼어낼 신규 디코더·구성·HW 기법 없음
- **ID**: ieee:5764130
- **Type**: conference
- **Published**: 11-13 Marc
- **Authors**: Qi Jun-wei, Xue Rui, Zhang Ya-qian
- **PDF**: https://ieeexplore.ieee.org/document/5764130
- **Abstract**: For the poor error-correcting performance of traditional channel codes in shortwave channel, Low Density Parity Check Codes (LDPCC) with a optimal check-up matrix and a suitable decoding algorithm is introduced. Combined with Multi-Carrier-Code Division Multiple Access (MC-CDMA) technology which can inhibit multipath interference remarkably, the LDPC+OFDM+DSSS scheme is proposed. Then the effect of MC modulation and LDPC codes on the performance of the system is studied, which can provide the reference basis for practical application. Simulation results in wideband shortwave channel show that LDPC codes can improve the bit error rate (BER) performance compared with the traditional channel coding. Meanwhile, the system can also inhibit the channel interference and symbol interference effectively and the performance of the system is greatly improved.

## Performance of improved AR3A code over EPR4 channel

- **Status**: ✅
- **Reason**: EPR4(스토리지 partial-response) 채널용 protograph AR3A LDPC 펑처링 개선으로 성능·저복잡도 확보 — B/E 스토리지 코드설계
- **ID**: ieee:5764084
- **Type**: conference
- **Published**: 11-13 Marc
- **Authors**: SiJie Yang, Lin Wang, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/5764084
- **Abstract**: High rate low-density parity-check (LDPC) codes have been under intense research in the serial concatenation of inner Extend partial-response Class 4(EPR4) and outer LDPC codes due to their decoding performance close to the Shannon capacity. The Accumulate Repeat-3 and Accumulate (AR3A) codes, viewed as a subclass of protograph LDPC codes, achieve good decoding performance with simple linear encoder structure and flexible code rates via puncturing variable nodes, which makes us consider the potential of serially concatenating the EPR4 channel with AR3A codes. Simulation results show that AR3A codes can't preserve their performance advantages over regular LDPC codes in the EPR4 channel, although they surpass regular LDPC codes in the AWGN channels. This paper proposes an improved AR3A code where we change the puncturing method, that is, the degree-1 variable nodes are punctured instead of degree-5 ones. The performance curves verify that the improved AR3A code possesses better decoding performance than the regular LDPC code in EPR4 channels and still keeps its original excellent characteristics of low hardware complexity.
