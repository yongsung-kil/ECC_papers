# IEEE Xplore — 2018-10


## Design of LDPC Codes for the Unequal Power Two-User Gaussian Multiple Access Channel

- **Status**: ❌
- **Reason**: 2-user Gaussian MAC용 LDPC 설계(EXIT chart); 다중접속 채널 특이적, NAND 단일채널 ECC에 떼어낼 신규 기법 없음
- **ID**: ieee:8356057
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Alexios Balatsoukas-Stimming, Athanasios P. Liavas
- **PDF**: https://ieeexplore.ieee.org/document/8356057
- **Abstract**: In this letter, we describe an LDPC code design framework for the unequal power two-user Gaussian multiple access channel using EXIT charts. We show that the sum-rate of the LDPC codes designed using our approach can get close to the maximal sum-rate of the two-user Gaussian multiple access channel. Moreover, we provide numerical simulation results that demonstrate the excellent finite-length performance of the designed LDPC codes.

## A Low-Complexity Hardware for Deterministic Compressive Sensing Reconstruction

- **Status**: ❌
- **Reason**: 압축센싱 OMP 복원 HW; LDPC 패리티검사를 측정행렬 생성에만 활용, 채널 ECC 디코더 아님
- **ID**: ieee:8301022
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Mohammad Fardad, Sayed Masoud Sayedi, Ehsan Yazdian
- **PDF**: https://ieeexplore.ieee.org/document/8301022
- **Abstract**: Reconstruction algorithms of compressively sampled data include solving a sparse approximation problem. This problem requires iterative search or optimization techniques. Software implementations are not fast enough for real-time applications of recovery algorithms and these algorithms should be implemented in hardware. This paper presents a low-complexity hardware for real-time reconstruction of compressively sensed signal using orthogonal matching pursuit algorithm. The main goal of this research is to provide a deterministic alternative to the random measurement matrix. The construction of this matrix is based on the connection between the parity check matrix of low-density parity-check (LDPC) codes and the measurement matrix of compressive sensing. For efficient hardware realization, a geometric approach to the construction of LDPC codes is used for matrix generation on the fly without requiring a lot of storage. Cyclic and binary structure of this matrix leads to the lower computational complexity and hardware cost in the reconstruction side. The described hardware has been implemented and evaluated on a virtex6 field-programmable gate array from Xilinx. Implementation results show that the proposed architecture has better performance in terms of hardware utilization. Moreover, the accuracy of the recovered signal is comparable with the previous works in which the random measurement matrix is used.

## Symmetric Block-Wise Concatenated BCH Codes for NAND Flash Memories

- **Status**: ❌
- **Reason**: NAND용이나 BCH 기반 concatenated 부호; 비-LDPC, 디코더 기법이 BCH stopping set 전용으로 LDPC BP 이식성 없음
- **ID**: ieee:8362743
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Daesung Kim, Krishna R. Narayanan, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8362743
- **Abstract**: This paper introduces a high rate error-correcting coding scheme called symmetric block-wise concatenated Bose-Chaudhuri-Hocquenghem (symmetric BC-BCH) codes tailored for storage devices with hard-decision outputs, e.g., storage devices based on NAND flash memory. It will be shown that a careful integration of the symmetry and 2-D block-wise concatenation is especially beneficial to achieve improvements of error-rate performance when an iterative hard-decision-based decoding (IHDD) is assumed. The claim is substantiated by proving that the proposed symmetric concatenation is optimal in terms of error-rate performance in the low error-rate regime over other 2-D block-wise concatenations. Besides, this paper proposes a novel way to design constituent codes, which enables us to enjoy advantages of primitive BCH codes and to efficiently break stopping sets associated with the IHDD in the low error-rate regime. We consider error-control systems made up of a symmetric BC-BCH code, the IHDD, and simple auxiliary decoders specifically targeting to break stopping sets caused in the IHDD. It will be shown that the auxiliary decoders significantly improve error-rate performance at a negligible amount of extra complexity. Performance comparisons are also carried out between error-control systems with the proposed and other coding schemes such as BCH codes, quasi-primitive BC-BCH codes, and low-density parity-check codes.

## Secure device pairing via handshake detection

- **Status**: ❌
- **Reason**: 스마트워치 악수 감지 보안 디바이스 페어링, LDPC/ECC 무관 - 제외
- **ID**: ieee:8450874
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Zhenge Guo, Xueguang Gao, Qiang Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/8450874
- **Abstract**: Multi-party applications are becoming popular due to the development of mobile smart devices. In this work, we explore Secure Device Pairing (SDP), a novel pairing mechanism, which allows users to use smart watches to detect the handshake between users, and use the shaking information to create security keys that are highly random. Thus, we perform device pairing without complicated operations. SDP dynamically adjusts the sensor’s sampling frequency and uses different classifiers at varying stages to save the energy. A multi-level quantization algorithm is used to maximize the mutual information between two communicating entities without information leakage. We evaluate the main modules of SDP with 1800 sets of handshake data. Results show that the recognition accuracy of the handshake detection algorithm is 98.2%, and the power consumption is only 1/3 of that of the single sampling frequency classifier.

## Polar Codes for Informed Receivers

- **Status**: ❌
- **Reason**: polar 코드 기반 informed receiver 구성, 부호 비의존 BP 이식 기법 없음 - 비-LDPC 제외
- **ID**: ieee:8440099
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Yu-Chih Huang, Shin-Lin Shieh
- **PDF**: https://ieeexplore.ieee.org/document/8440099
- **Abstract**: The problem of sending independent messages to a receiver which already has been informed a subset of messages as side information is studied. Which messages are available at the receiver is assumed to be oblivious to the transmitter. A simple yet powerful construction of codes for informed receivers based on polar codes is proposed to efficiently and fairly convert side information into reduction in probability of errors for any message side information. Compared with existing designs based on codes on graph or algebraic codes, the proposed construction is both conceptually and practically simple. Moreover, the codes inherit many good properties of polar codes, including explicit construction and low-complexity encoding and decoding scaling such as O(N log N) where N is the blocklength. Extensions to high-order modulation and block fading channels are also proposed. Simulation results indicate that for every side information configuration, the proposed codes can convert side information into reduction in signal-to-noise ratio of roughly 6 dB/bit at bit error rate of 10-5 under additive white Gaussian noise channel or block fading channel.

## Constant-Envelope Multicarrier Waveforms for Millimeter Wave 5G Applications

- **Status**: ❌
- **Reason**: mmWave 5G용 CE-OFDM 파형 설계; LDPC·ECC 기여 전무한 무선 PHY 변조 논문
- **ID**: ieee:8409331
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Talha Faizur Rahman, Claudio Sacchi, Simone Morosi +2
- **PDF**: https://ieeexplore.ieee.org/document/8409331
- **Abstract**: A key point of Fifth Generation (5G) wireless networking will be the exploitation of higher frequency bands in the millimeter wave (mm-Wave) spectrum to provide unprecedented data rates to mobile users. In such a perspective, the PHYsical (PHY) layer design priorities should be reconsidered. In this paper, we investigate Constant-Envelope Multicarrier (CE-MC) waveforms for future adoption in mm-Wave 5G transmissions, namely: Constant-Envelope Orthogonal Frequency Division Multiplexing (CE-OFDM) and Constant-Envelope Single-Carrier OFDM (CE-SC-OFDM). These waveforms are obtained by imposing a nonlinear phase modulation to a real-valued OFDM and SC-OFDM signal, respectively. Thanks to their 0dB Peak-to-Average-Power Ratio, such unconventional signaling formats are insensitive to nonlinear distortions and allow to exploit the flexibility of conventional multicarrier systems together with augmented resilience against multipath fading and phase noise. CE-OFDM and CE-SC-OFDM have been assessed by means of computer simulations in a short-range mm-Wave 5G scenario, i.e., downlink transmission in outdoor picocells. Simulation results demonstrate that CE multicarrier waveforms enhance robustness and increase coverage and capacity in the proposed scenario, as compared to conventional OFDM and SC-OFDM counterparts.

## Fully-Parallel Stochastic Decoder for Rate Compatible Modulation

- **Status**: ❌
- **Reason**: RCM(rate compatible modulation)용 stochastic 디코더; LDPC가 아닌 mapping matrix 복호, 부호 비의존 이식성 불명확한 변조 전용
- **ID**: ieee:8320793
- **Type**: journal
- **Published**: Oct. 2018
- **Authors**: Fang Lu, Yan Dong, Chang Wen Chen
- **PDF**: https://ieeexplore.ieee.org/document/8320793
- **Abstract**: Rate compatible modulations (RCMs) are attractive for achieving seamless and blind rate adaptation under time varying channel. Although the decoding of RCM is inherently parallel, the highly complex processing nodes, and routing congestion have prohibited the implementation of fully-parallel decoders for high throughput. In this paper, we propose a new stochastic decoding algorithm for RCM to achieve desired parallel decoding. This algorithm provides even much better decoding performance than the floating-point belief propagation decoding algorithm with 20 iterations. To evaluate the effectiveness of the proposed algorithm, we apply it for the implementation of a field-programmable gate-array fully-parallel stochastic decoder that decodes a 400 × 400 mapping matrix. Several novel structure techniques, including the RAM-based channel stream generator and the configurable variable node, are exploited to reduce the logical resources consumption. The implemented decoder achieves a clock frequency of 220 MHz and provides a maximum throughput about 136Mb/s at SNR = 10 dB and the number of symbols is 400. To the best of our knowledge, this decoder is the first reported fully-parallel RCM decoder which achieves the highest decoding throughput. This research validates the potential of stochastic RCM decoding as a practical approach for area-efficient and high throughput decoders.

## Comparative Study of Channel Coding Schemes for 5G

- **Status**: ❌
- **Reason**: 5G 채널코딩(conv/turbo/LDPC/polar) 비교 서베이; 신규 기여 없고 비이진 LDPC 언급
- **ID**: ieee:8548806
- **Type**: conference
- **Published**: 9-11 Oct. 
- **Authors**: Walled Khalid Abdulwahab, Abdulkareem Abdulrahman Kadhim
- **PDF**: https://ieeexplore.ieee.org/document/8548806
- **Abstract**: In this paper we look into 5G requirements for channel coding and review candidate channel coding schemes for 5G. A comparative study is presented for possible channel coding candidates of 5G covering Convolutional, Turbo, Low Density Parity Check (LDPC), and Polar codes. It seems that polar code with Successive Cancellation List (SCL) decoding using small list length (such as 8) is a promising choice for short message lengths (≤128 bits) due to its error performance and relatively low complexity. Also adopting non-binary LDPC can provide good performance on the expense of increased complexity but with better spectral efficiency. Considering the implementation, polar code with decoding algorithms based on SCL required small area and low power consumption when compared to LDPC codes. For larger message lengths (≥256 bits) turbo code can provide better performance at low coding rates (<;1/2).

## Wireless In-Band Distribution Link using LDM for SFN Transmitters and Gapfillers in ATSC 3.0

- **Status**: ❌
- **Reason**: ATSC 3.0 SFN gapfiller 무선 분배링크 응용; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8551152
- **Type**: conference
- **Published**: 9-11 Oct. 
- **Authors**: Liang Zhang, Yiyan Wu, Wei Li +8
- **PDF**: https://ieeexplore.ieee.org/document/8551152
- **Abstract**: Delivering services to mobile devices in densely populated indoor and enclosed areas, such as stadiums, airports, train stations, and shopping malls, has the potential to bring more viewership to terrestrial broadcast services. The next-generation ATSC 3.0 system is designed with extremely robust transmission capability to deliver high-quality mobile services to portable and handheld receivers. Even with the most robust transmission mode, delivering services to these indoor environments still proves challenging due to high penetration losses. One solution is to deploy low-power, single frequency network (SFN) transmitters, called SFN Gapfillers, which can provide reliable mobile services specifically to indoor/enclosed areas. In deploying SFN Gapfillers, a significant cost derives from the service data distribution link. In this paper, we propose a wireless, in-band distribution link using Layered Division Multiplexing (LDM) technology. Instead of dedicated fiber or microwave links, in the proposed solution, the service distribution-link data is delivered to the SFN Gapfillers with a high-power transmitter, using the Enhanced Layer of a two-layer ATSC 3.0 signal, which results in low infrastructure and operational costs. By using LDM, the wireless distribution links are implemented with high spectrum efficiency since they share the same TV band with the broadcast services. To guarantee successful SFN operation of the Gapfillers, sufficient delay of the broadcast service signal from the SFN distribution signal is required. The proposed technology also can be applied to deploy conventional SFN transmitters to extend coverage areas or to provide services to remote areas.

## Analysis of Jamming Attacks on a Hopped OFDM Communication System

- **Status**: ❌
- **Reason**: OFDM 재밍 공격 분석, LDPC ECC 기법 없음
- **ID**: ieee:8599930
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Mohamed A. Soliman, Karim H. Moussa, Walid M. Saad +2
- **PDF**: https://ieeexplore.ieee.org/document/8599930
- **Abstract**: Orthogonal frequency division multiplexing (OFDM) was considered to be a well-known robust method and a utilizing hopping method across various frequency bands or sub-bands that is known for its capability to enhance the performance of these communication systems. The combination between both of these techniques should be useful in mitigating interference especially the jamming that is caused accidentally or on purpose mainly in the military applications. This paper illustrates that the bit error rate (BER) performances of an improved OFDM communication system utilizing several frequency sub-bands hopping techniques against different categories of jammers are presented. In case of low jamming power at the front end of the receiver, the system performance is enhanced gradually by raising the number of frequency hopping sub-bands against narrowband, wideband and barrage jammers. At a high jamming power, no improvement is achieved using the sub-bands hopping methods.

## Linear Erasure Block Codes over Either a Field of Rational Numbers Q or an Algebraic Structure Ψq

- **Status**: ❌
- **Reason**: 비-LDPC erasure 블록부호 수학모델(LT/Raptor/Zigzag 일반화), 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:8600217
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Yehor Savchenko
- **PDF**: https://ieeexplore.ieee.org/document/8600217
- **Abstract**: In this paper, we define a mathematical model of linear erasure block codes (k, C) for symbol erasure channels (SEC) that are built over either a field of rational numbers Q or an algebraic structure Ψq. We show the necessary condition for the codes (k, C) to be optimal, and we demonstrate that some of the already existing erasure codes may be considered as the specific cases of the codes (k, C) over a Ψq, such as Luby Transform, Raptor or Zigzag Decodable.

## DCI-Free Based Downlink Prescheduling Scheme for Ultra-Reliable and Low Latency Communications

- **Status**: ❌
- **Reason**: 5G URLLC 다운링크 프리스케줄링, LDPC 무관
- **ID**: ieee:8600167
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Man Dai, Ce Sun, Xinyi Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8600167
- **Abstract**: The fifth generation (5G) cellular network are divided into three key usage scenarios as enhanced mobile broadband, massive machine-type communications and ultra-reliable and low-latency communications (URLLC). To insure the low end-to-end delay and high reliability for users in URLLC, the overhead of physical downlink control channel (PDCCH) resource needs to be greatly increased during the scheduling process. In this paper, a downlink prescheduling scheme is proposed, where we don't need to transmit downlink control information (DCI). With this DCI-Free scheme, we can not only save PDCCH resource to support more users, but also simplify the signaling interaction to reduce the time delay. Simulation results show that the proposed scheme is able to support more users and decrease transmission delay without downlink control information in URLLC.

## VLSI-Architecture of Radix-2/4/8 SISO Decoder for Turbo Decoding at Multiple Data-rates

- **Status**: ❌
- **Reason**: 비-LDPC turbo SISO 디코더 VLSI, QPP 인터리버 기반으로 LDPC BP에 이식 불가
- **ID**: ieee:8644753
- **Type**: conference
- **Published**: 8-10 Oct. 
- **Authors**: Rahul Shrestha, Ashutosh Sharma
- **PDF**: https://ieeexplore.ieee.org/document/8644753
- **Abstract**: We propose flexible-architecture for soft-input soft-output (SISO) decoder with radix-2/4/8 modes to support multiple data-rates. This work presents designs of major internal blocks of SISO decoder using extensive steering logic to support multiple radix operating-modes. These architectures enable efficient clock-gating of our decoder for low-power consumption in different operating modes. Subsequently, we have aggregated eight SISO decoders with quadratic-permutation-polynomial (QPP) interleavers/de-interleavers to design parallel-turbo decoder architecture which can operate in multi-radix mode. Suggested SISO decoder is ASIC synthesized and post-layout simulated in UMC 65 nm-CMOS process. Performance analyses in AWGN channel environment showed that the bit-error-rate (BER) of 10-4 could be achieved at 5 dB and 0.8 dB for SISO and turbo decoders respectively. Implementation result shows that the suggested SISO decoder could achieve throughput in the range 270-810 Mbps with the corresponding power consumption range of 12.24-37.67 mW. In comparison to the state-of-the-art, our design achieved 38% higher throughput and 61% lower power consumption. Similarly, our multi-radix parallel-turbo decoder is hardware prototyped in 28 nm-CMOS Zynq-FPGA board. It delivers a range of data-rates from 80-320 Mbps operating at 160 MHz of clock frequency for 8 iterations.

## Constant Overhead Quantum Fault-Tolerance with Quantum Expander Codes

- **Status**: ❌
- **Reason**: 양자 expander 코드 fault-tolerance, 신드롬측정/스태빌라이저 의존 양자전용 디코더로 고전 이식 불가
- **ID**: ieee:8555154
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Omar Fawzi, Antoine Grospellier, Anthony Leverrier
- **PDF**: https://ieeexplore.ieee.org/document/8555154
- **Abstract**: We prove that quantum expander codes can be combined with quantum fault-tolerance techniques to achieve constant overhead: the ratio between the total number of physical qubits required for a quantum computation with faulty hardware and the number of logical qubits involved in the ideal computation is asymptotically constant, and can even be taken arbitrarily close to 1 in the limit o small physical error rate. This improves on the polylogarithmic overhead promised by the standard threshold theorem. To achieve this, we exploit a framework introduced by Gottesman together with a family of constant rate quantum codes, quantum expander codes. Our main technical contribution is to analyze an efficient decoding algorithm for these codes and prove that it remains robust in the presence of noisy syndrome measurements, a property which is crucial for fault-tolerant circuits. We also establish two additional features of the decoding algorithm that make it attractive for quantum computation: it can be parallelized to run in logarithmic depth, and is single-shot, meaning that it only requires a single round of noisy syndrome measurement.

## Hybrid Probabilistic-Geometric Shaping in Optical Communication Systems

- **Status**: ❌
- **Reason**: 광통신 확률-기하 성형(constellation shaping), LDPC ECC 기법 없음
- **ID**: ieee:8527283
- **Type**: conference
- **Published**: 30 Sept.-4
- **Authors**: Zhen Qu, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8527283
- **Abstract**: We propose a universal distribution matcher applicable to any two-dimensional signal constellation. We experimentally demonstrate that the performance of the proposed 32-ary quadrature amplitude modulation (QAM), based on hybrid probabilistic-geometric shaping, is superior to probabilistically shaped (PS)-32QAM and regular 32QAM, and comparable to PS-64QAM.

## 10-Gb/s Transmission Over 10-m SI-POF with M-PAM and Multilayer Perceptron Equalizer

- **Status**: ❌
- **Reason**: SI-POF PAM 전송 MLP 등화기, 채널 등화이고 LDPC ECC 기법 없음
- **ID**: ieee:8527269
- **Type**: conference
- **Published**: 30 Sept.-4
- **Authors**: Isaac N. Osahon, Majid Safari, Wasiu O. Popoola
- **PDF**: https://ieeexplore.ieee.org/document/8527269
- **Abstract**: We demonstrate the gigabit-per-second transmission over a step-index plastic optical fiber (SI-POF) of 10-m length with a pulse-amplitude modulation (PAM). A multilayer perceptron-based equalizer is used to mitigate an intersymbol interference and non-linearity in the system. Using this equalizer with 32-PAM, a data rate of 10 Gb/s is achieved over the 10-m SI-POF at a bit error rate of 10-2, which is below the 20% forward error correction limit.

## On the Decoding Radius Realized by Low-Complexity Decoded Non-Binary Irregular LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) irregular LDPC majority-logic 디코딩 — 비이진 LDPC는 제외 대상
- **ID**: ieee:8664375
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Pavel Rybin, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/8664375
- **Abstract**: In this paper we consider the low complexity majority-logic decoding algorithm for irregular non-binary low-density parity-check (LDPC) codes. The decoding algorithm is a generalization of the bit-flipping algorithm for binary LDPC codes. The lower estimate on the decoding radius realized by this algorithm is derived for the first time for irregular non-binary LDPC codes. We present the numerical results for the derived lower bound.

## Complete Multipartite Graph Codes

- **Status**: ❌
- **Reason**: 그래프 코드/블록단위 product code 일반화 — LDPC 인코딩 알고리즘 차용 언급뿐, NAND 바이너리 LDPC에 새로 이식할 디코더/구성 기여 없음
- **ID**: ieee:8664263
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Yuta Kumano, Yoshiyuki Sakamaki, Hironori Uchikawa
- **PDF**: https://ieeexplore.ieee.org/document/8664263
- **Abstract**: Graph codes are constructed from undirected graphs where the code symbols correspond to the edges and component codes are associated with the vertices. We investigate graph codes on multigraphs whereas previous work has mainly studied them on simple graphs. This paper proposes graph codes constructed from complete multipartite graphs as generalizations of block-wise product codes. The graph codes show better error-correcting performance in error-floor region compared with block-wise product codes. This paper also shows an efficient encoding method for the graph codes by employing Richardson and Urbanke's encoding algorithm for LDPC codes.

## Recovery Guarantee of Sparse Binary Sensing Matrices under Greedy Algorithm

- **Status**: ❌
- **Reason**: 압축센싱 OMP 복원 보장 — LDPC 패리티검사를 sensing matrix로 차용, 채널 ECC/디코더 기여 아님
- **ID**: ieee:8664323
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Wen-Yao Chen, Chung-Chin Lu
- **PDF**: https://ieeexplore.ieee.org/document/8664323
- **Abstract**: The theory of compressed sensing was established independently by Donoho and by Candès et al.. The main result of compressed sensing is that one can recover a high-dimensional sparse signal through a small number (far less than the signal dimension) of linear random measurements by convex optimization. It means that a sparse high dimensional signal can be compressed as a low dimensional signal. Orthogonal matching pursuit (OMP) and l1-minimization are two main reconstruction algorithms. The OMP algorithm is an iterative greedy algorithm and has the advantage of easy implementation. In this paper, we use a class of structured sparse binary matrices to be measurement matrices and study their recovery guarantee under the greedy OMP algorithm. These matrices are parity-check matrices of LDPC codes. It was reported that according to simulation results, parity-check matrices constructed by progressive edge-growth (PEG) algorithm can have better recovery rate than random Gaussian matrices under the OMP algorithm. But there is still no literature about theoretical analysis on this topic. In this paper, we show that the OMP algorithm does not provide the same recovery guarantee as l1-minimization for general parity-check matrices of LDPC codes. A modified OMP algorithm that reaches the same recovery guarantee as l1-minimization is proposed.

## Sparse Multiple Access and Code Design with Near Channel Capacity Performance

- **Status**: ❌
- **Reason**: 다중접속 sparse access 응용 — LDPC degree 분포+puncture 공동 최적화이나 multi-user 통신 특이적, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:8664311
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Akira Osamura, Guanghui Song, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/8664311
- **Abstract**: For the problem of multiple users simultaneously communicating with a single receiver, a sparse multiple access scheme is proposed. Each user employs a low-density parity-check (LDPC) code. To mitigate multi-user interference, the codeword of each user is randomly punctured and the punctured bits are replaced by idle slots. That is, only a small random set of users are active at each time. The restriction of number of concurrent users significantly reduces the multi-user decoding complexity. Moreover, this puncture facilitates an efficient message-passing decoding over a sparse graph. With a joint optimization of the degree distribution of the LDPC code and the column weight distribution of the puncture matrix, capacity-approaching performance is achieved.

## Slepian-Wolf Coding with Side-Information Having Insertion/Deletion Errors

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산소스코딩에 비이진(non-binary) LDPC 사용—비이진 LDPC 제외 + 소스코딩
- **ID**: ieee:8664215
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/8664215
- **Abstract**: This paper considers Slepian-Wolf (SW) coding in which side-information (SI) has insertion and deletion errors, presuming that the SI is given as a binary vector generated by temporal and/or spatial interpolation or extrapolation of related binary vectors. The coding could be regarded as a simplified model of SW coding in distributed video coding. From the generation process of SI vector, we define a hypothetical error model in the SI vector as an insertion/deletion/substitution error channel, and then show a coding scheme using nonbinary LDPC code. Decoding is based on an iterative multi-path decoding of forward-backward algorithm and FFT sum-product algorithm. Simulation results show the relations between insertion/deletion probability and decoded bit error rates.

## Optimal Training Channel Statistics for Neural-based Decoders

- **Status**: ❌
- **Reason**: Polar 신경망 디코더의 최적 훈련통계 이론; 부호 비의존 적이긴 하나 polar 특화 분석이고 BP 이식 기여 불명확—원칙 제외(비-LDPC)
- **ID**: ieee:8645128
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Meryem Benammar, Pablo Piantanida
- **PDF**: https://ieeexplore.ieee.org/document/8645128
- **Abstract**: This work investigates the design of End-to-End channel coding based on deep learning. The focus is on the design of neural networks based channel decoders. We demonstrate the existence of an optimal training statistic for the cross-entropy loss which allows the network to generalize to channel statistics unseen during training while performing close to their optimal decision rule. Numerical results illustrate an application to Polar coding on binary input memoryless channels.

## Efficient Scheduling of Serial Iterative Decoding for Zigzag Decodable Fountain Codes

- **Status**: ❌
- **Reason**: Fountain/zigzag erasure 코드 peeling 디코딩 — fountain/erasure는 제외 대상, 채널 ECC 기법 아님
- **ID**: ieee:8664321
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Yoshihiro Murayama, Takayuki Nozaki
- **PDF**: https://ieeexplore.ieee.org/document/8664321
- **Abstract**: Fountain codes are erasure correcting codes realizing reliable communication systems for the multicast on the Internet. The zigzag decodable fountain (ZDF) code is one of generalization of the Raptor code, i.e, applying shift operation to generate the output packets. The ZDF code is decoded by a two-stage iterative decoding algorithm, which combines the packet-wise peeling algorithm and the bit-wise peeling algorithm. By the bit-wise peeling algorithm and shift operation, ZDF codes outperform Raptor codes under iterative decoding in terms of decoding erasure rates and overheads. However, the bit-wise peeling algorithm spends long decoding time. This paper proposes a fast bit-wise decoding algorithm for the ZDF codes. Simulation results show that the proposed algorithm drastically reduces the decoding time compared with the existing algorithm.

## Shifted Coded Slotted ALOHA

- **Status**: ❌
- **Reason**: Coded slotted ALOHA 랜덤액세스 스킴(SIC+shift)으로 패킷 erasure 영역. 채널 ECC 디코더 기법 아님, 무선 랜덤액세스 응용 특이적
- **ID**: ieee:8664385
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Tomokazu Emoto, Takayuki Nozaki
- **PDF**: https://ieeexplore.ieee.org/document/8664385
- **Abstract**: A random access scheme is a fundamental scenario in which users transmit through a shared channel and cannot coordinate with each other. In recent years, successive interference cancellation (SIC) is introduced into the random access scheme. It is possible to decode transmitted packets using collided packets by the SIC. The coded slotted ALOHA (CSA) is a random access scheme using the SIC. The CSA encodes each packet using a local code prior to transmission. It is known that the CSA achieves excellent throughput. On the other hand, it is reported that shift operation improves the decoding performance for packet-oriented erasure correcting coding system. In this paper, we propose a random access scheme which applies the shift operation to the CSA. Numerical examples show that our proposed random access scheme achieves better throughput and packet loss rate than the CSA.

## Blind Reconstruction of Binary Cyclic Codes over Binary Erasure Channel

- **Status**: ❌
- **Reason**: 바이너리 cyclic code blind reconstruction (BEC) — 비-LDPC, 코드 식별 문제로 NAND ECC 기법 아님
- **ID**: ieee:8664357
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Arti D. Yardi
- **PDF**: https://ieeexplore.ieee.org/document/8664357
- **Abstract**: Given a sequence of noise-affected codewords of an unknown channel code, the problem of blind reconstruction of channel codes consists of identifying this unknown channel code. This problem has many applications in military surveillance and cognitive radios. In this paper, we study this problem for the case when the noise is introduced by the binary erasure channel (BEC) and the unknown channel code is a binary cyclic code of known length. We provide an algorithm to find the generator polynomial of the unknown cyclic code. We also provide an analysis of our algorithm where we provide a lower bound on the probability of correctly identifying the factors of the generator polynomial.

## Reliability-Based Parametric LDLC Decoding

- **Status**: ❌
- **Reason**: Low-density lattice code(LDLC)의 Gaussian mixture BP 디코딩—격자부호 실수값 메시지로 바이너리 LDPC BP에 직접 이식 불가
- **ID**: ieee:8664251
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Warangrat Wiriya, Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/8664251
- **Abstract**: This paper proposes reliability-based parametric decoding of low-density lattice codes (LDLC). We define the reliability of the check-to-variable messages for two purposes. The first one is to choose to approximate the infinite Gaussian mixtures by one or two Gaussians. The reliability of each check-to-variable message is calculated. If there is higher reliability than a fixed threshold value, one Gaussian will be selected; otherwise two Gaussians will be used. The other purpose is for the updating sequence of variable nodes of the parametric shuffled BP (SBP) decoding algorithm. The parametric SBP increases the convergence speed. The updating sequence of SBP follows the order of reliability of the check-to-variable messages from high to low. The numerical results show that the proposed algorithm gives superior performance and lower complexity compared to two or three Gaussian decoding algorithm. At a probability of symbol error equal 10-4 and n = 100 and 1000, the proposed algorithm gains 0.25 and 0.2 dB, respectively. Moreover, the proposed algorithm provides lower decoding time, fewer number of iterations for convergence and lower memory requirement.

## Energy Efficient Communication with Interdependent Source-Channel Coding: An Enhanced Methodology

- **Status**: ❌
- **Reason**: WSN 소스-채널 결합 코딩(JSCC)으로 LDPC 비의존, 떼어낼 ECC 기법 없음
- **ID**: ieee:8589643
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: N.C. Resmi, Sonali Chouhan
- **PDF**: https://ieeexplore.ieee.org/document/8589643
- **Abstract**: The primary design goals of an energy constrained Wireless Sensor Network are bit error rate (BER) performance and energy efficiency. An enhanced methodology is proposed in this paper for the energy efficient Interdependent Source-Channel Coding scheme. The scheme minimizes the energy overhead for encoding/decoding and redundant bits' transmission typical of a forward error correction scheme. An intensified BER performance and a significant amount of compression in place of redundancy compared to standard codes are achieved. The proposed methodology, validated in the context of Mica2 mote and MicaZ mote, yields a notable raise in compression and coding gain compared to the earlier proposed methodology.

## Low-complexity distributed set-theoretic decoders for analog fountain codes

- **Status**: ❌
- **Reason**: 아날로그 fountain code의 실수값 set-theoretic 디코더, 바이너리 LDPC BP와 무관 (fountain/erasure 제외)
- **ID**: ieee:8645310
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Renato L. G. Cavalcante, S. Stanczak, D. Schupke +1
- **PDF**: https://ieeexplore.ieee.org/document/8645310
- **Abstract**: Analog fountain codes (AFCs) have been recently proposed as a capacity-approaching coding scheme for Gaussian channels. In AFCs, coded symbols are real valued, and the number of generated codes can grow unboundedly. In this work, we exploit these characteristics of AFCs to pose the decoding process as an adaptive filtering problem. This formulation opens up the possibility of deriving a large family of online decoding algorithms that process coded symbols as they arrive, in a truly online fashion. In particular, we present two algorithms based on the adaptive projected subgradient method, and we further improve the performance of these algorithms by using heuristics inspired by recent results on superiorization. We also show that the proposed techniques can be trivially extended to distributed settings where receivers can exchange information locally. Simulations show that the proposed techniques can outperform state-of-the-art batch methods in some scenarios.

## Recursive Construction of k-Ary Uniquely Decodable Codes for Multiple-Access Adder Channel

- **Status**: ❌
- **Reason**: k-ary uniquely decodable 다중접속 adder channel 코드 — 비-LDPC, NAND ECC 무관
- **ID**: ieee:8664318
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Shan Lu, Wei Hou, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/8664318
- **Abstract**: A recursive construction of k-ary uniquely decodable multiuser codes is proposed for use in a noiseless multiple-access adder channel. The code rates of the proposed codes are higher than those of previous uniquely decodable multiuser codes. A recursive decoding algorithm is also proposed.

## Shaping Gain of Lattices Based on Convolutional Codes and Construction A

- **Status**: ❌
- **Reason**: convolutional code 기반 lattice shaping gain — 비-LDPC, NAND ECC 무관
- **ID**: ieee:8664359
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Fan Zhou, Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/8664359
- **Abstract**: This paper studies the shaping gain and the performance-complexity trade-off of convolutional code lattices, lattices that are based on convolutional codes and Construction A. Generator polynomials for convolutional codes which provide the best-found shaping gain are presented, for various code rates, memory orders and lattice dimensions. Results are based on exhaustive searches. The obtained shaping gains usually exceed that of convolutional codes good for coding. Convolutional code lattices with memory order 7 can provide a shaping gain of 1.20 dB (up to a possible 1.53 dB theoretical maximum) at dimension 256, which is higher than the 1.03 dB shaping gain of the Leech lattice. While convolutional code lattices based on rate 1/2 convolutional codes have the best shaping gain for a fixed memory order, we show that using rate 1/3 convolutional codes produces a more favorable performance-complexity trade-off.

## Decision Feedback Scheme with Criterion LR+Th for the Ensemble of Linear Block Codes

- **Status**: ❌
- **Reason**: 선형블록부호 앙상블 결정피드백 error exponent 이론 bound — 디코더/HW/구성으로 안 이어지는 순수 이론
- **ID**: ieee:8664336
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Toshihiro Niinomi, Hideki Yagi, Shigeichi Hirasawa
- **PDF**: https://ieeexplore.ieee.org/document/8664336
- **Abstract**: A decision criterion called LR+Th for decision feedback scheme was proposed by Hashimoto. Though Forney’s decision criterion (FR) is optimal and meets the Neyman-Pearson’s lemma, LR+Th is suboptimal. However, the error exponent of LR+Th is shown to be asymptotically equivalent to that of FR by random coding arguments for block codes. In this paper, applying the technique of DS2 bound, we derive an upper bound for the error probability of LR+Th with the ensemble of linear block codes. It elucidates the relation between the random coding exponents of block codes and those of linear block codes.

## Analysis on Probabilistic Construction of Connected Dominating Sets over Regular Graph Ensembles

- **Status**: ❌
- **Reason**: 무선 ad-hoc 가상백본용 connected dominating set 확률 구성 분석. LDPC 부호·디코더와 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8664384
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Takafumi Nakano, Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/8664384
- **Abstract**: In this paper, we propose a simple probabilistic construction of connected dominating sets (CDS) that is useful for virtual backbones of wireless ad-hoc networks. In the construction, each node in a network has a random bit and the node joins the virtual backbone if and only if the random bit is one. Our main contribution is to derive the exact formula of the expected success probability of the probabilistic CDS construction over regular graph ensembles. The derivation of the formula is based on a counting argument for a special class of labeled simple graphs with socket nodes. The ensemble average indicates the typical performance of the proposed probabilistic CDS construction and the expected values can be efficiently evaluated in polynomial time.

## Analysis of the Dual-Threshold-Based Shrinking Scheme for Efficient NB-LDPC Decoding

- **Status**: ❌
- **Reason**: NB-LDPC(GF(q)) 디코딩 복잡도 절감 기법 — 비이진 LDPC라 제외
- **ID**: ieee:8605702
- **Type**: conference
- **Published**: 26-30 Oct.
- **Authors**: Jing Tian, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8605702
- **Abstract**: In this paper, the dual-threshold-based shrinking (DTBS) scheme for efficient non-binary low-density parity-check (NB-LDPC) decoding, which has been initially presented in our previous work [1], is further studied. Particularly, the TIT-MSA is an example to employ this scheme presented in [1]. Its computational complexity is theoretically analyzed in this paper. Numerical results show that more than 70% computational complexity is reduced compared with the SMSA, while the error performance loss is negligible. Besides, when considering memory consumption, we extend this scheme by setting a maximum number of kept values with an efficient searching method, and apply it to the TIT-MSA. Simulation results indicate that the new decoding algorithm achieves both comparable error performance and significant memory reduction. For example, the memory consumption is reduced by about 61% for a (256, 203) code over GF(28) and about 31% for an (837, 726) code over GF(25).

## A New Error Correction Scheme for Physical Unclonable Function

- **Status**: ❌
- **Reason**: PUF 암호용 오류정정(ECMC, code-offset 대안) — 보안/PUF reconciliation, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8605707
- **Type**: conference
- **Published**: 26-30 Oct.
- **Authors**: Kai Sun, Yifei Shen, Yingjie Lao +3
- **PDF**: https://ieeexplore.ieee.org/document/8605707
- **Abstract**: Error correction is an indispensable component when physical unclonable functions (PUFs) are used in cryptographic applications, because environmental factors influence PUFs' performance. Nowadays, syndrome-based scheme and code-offset scheme are used in PUF error correction. In this paper, a new scheme named error correction with multiple challenge-response pairs (ECMC) is proposed to perform better than code-offset scheme under certain circumstances.

## FPGA Implementation of A Hybrid Decoder for STT-MRAM

- **Status**: ❌
- **Reason**: 확장 Hamming 부호용 하이브리드 디코더(STT-MRAM) — 비-LDPC 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:8605688
- **Type**: conference
- **Published**: 26-30 Oct.
- **Authors**: Xue Liu, Kui Cai, Zhen Mei
- **PDF**: https://ieeexplore.ieee.org/document/8605688
- **Abstract**: Process variation and random thermal fluctuation severely affect the reliability of spin-torque transfer magnetic random access memory (STT-MRAM). This paper presents an FPGA-based two-stage hybrid decoder of extended Hamming codes for STT-MRAM with less decoding latency and lower implementation complexity. Experiments indicate that the presented implementation can improve the STT-MRAM's tolerance to process variation and random thermal fluctuation.

## Security Performance of Polar Codes in UV Wireless Communications

- **Status**: ❌
- **Reason**: polar vs LDPC 보안성능 비교(security gap), 새 디코더/구성/HW 없음
- **ID**: ieee:8595916
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Xuetong Liang, Min Zhang, Dahai Han
- **PDF**: https://ieeexplore.ieee.org/document/8595916
- **Abstract**: In this paper we investigate the performance of low-density parity-check (LDPC) and polar codes in ultraviolet (UV) communications system in terms of the bit-error-ratio (BER) for different link spans and security gap. We show that polar coded system enhanced the security performance compared to the system coded by LDPC in the UV communication systems.

## Rate-Adaptive Coded Modulation with Geometrically-shaped Constellations

- **Status**: ❌
- **Reason**: 기하 성형 성상 rate-adaptive coded modulation, LDPC ECC 신규 기법 없음
- **ID**: ieee:8595918
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Bin Chen, Yi Lei, Domanic Lavery +2
- **PDF**: https://ieeexplore.ieee.org/document/8595918
- **Abstract**: Information-theoretic metrics are used to design rate-adaptive coded modulation based on geometrically-shaped constellations with soft- and hard-decision FEC. Numerical results show that an 8% reach extension can be achieved with flexible data rates and transmission distances.

## Performance Analysis of LDPC Codes for Wireless Optical Communication Systems in Different Seawater Environments

- **Status**: ❌
- **Reason**: 해수 UWOC에 LDPC 단순 적용 성능분석, 떼어낼 기법 없음
- **ID**: ieee:8596282
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Jingni Zhang, Yi Yang, Zhuo Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/8596282
- **Abstract**: Optical signal is severely attenuated in seawater, which affects the performace of underwater wireless optical communication(UWOC) system and limits the wireless optical transmission distance. In this paper, wireless optical seawater channel transmission model is analyzed and established. And based on the transmission model, the OOK optical modulation and LDPC codes is combined to analyze the performance of the UWOC system and the transmission distance of wireless optical(TDWO) in different seawater environments. The results show that the clearer the water quality, the better performance of LDCP coding system. And when the optical source is 30mW, the TDWO is less than 6.2m,the coding system can improve the system performance in offshore environment.

## Secure Bidirectional Adaptive Resource Allocation in SDN-Enabled 5G Fronthaul Networks

- **Status**: ❌
- **Reason**: SDN 5G fronthaul 자원할당+BER 서비스, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8595910
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Mingwei Yang, Houman Rastegarfar, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8595910
- **Abstract**: We propose a software-defined resource allocation scheme in a mobile fronthaul (MFH) network that supports dynamic processing resource sharing. Our studies point to the feasibility of guaranteed bit error rate (BER) service using adaptation.

## Random-Interleave-Based Anti-Occlusion Scheme for MIMO-VLC System

- **Status**: ❌
- **Reason**: MIMO-VLC 안티-오클루전 랜덤 인터리브 기법 — 무선/통신 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8595802
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Shuang Zhan, Zhitong Huang, Yu Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/8595802
- **Abstract**: Visible light communication (VLC) has attracted more and more attention due to the extensively deployment of light emitting diodes (LED). Considering the occlusion problem is a difficulty in actual indoor environment, an anti-occlusion VLC system deserves to be completed. In this paper, we propose random-interleaved-based anti-occlusion scheme for multiple-input multiple-output (MIMO) VLC system. The simulation and experiment results show that the proposed scheme offers superior bit error rate (BER) performance in environment of obstructions.

## Hybrid Probabilistic-Geometric-Shaped 8-PAM Suitable for Data Centers’ Communication

- **Status**: ❌
- **Reason**: 데이터센터용 HPGS 8-PAM 시그널링 — LDPC는 베이스라인 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:8595831
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Xiao Han, Mingwei Yang, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8595831
- **Abstract**: We propose a hybrid probabilistic-geometric-shaped (HPGS) 8-PAM signaling scheme, as a candidate suitable for data centers' communications. The properly chosen HPGS 8-PAM parameters for different SNR-regions allows us to closely approach the Shannon limit. We demonstrate that LPDC-coded HPGS 8-PAM outperforms both probabilistic-shaped and uniform LDPC-coded 8-PAM schemes.

## Polar Codes Analysis of 5G Systems

- **Status**: ❌
- **Reason**: polar vs turbo vs LDPC 비교 서베이성 5G 논문, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:8751838
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Marwan DHUHEIR, Sıtkı ÖZTÜRK
- **PDF**: https://ieeexplore.ieee.org/document/8751838
- **Abstract**: In this paper, we investigate the achievements and challenges of using polar codes in 5th generation New Radio (5G-NR) communications systems. Polar codes are considered the promising technique to solve the problems that emerged in previous generation wireless communications systems such as latency, complexity, error correction capability, network infrastructure and Quality of Service (QoS). Polar codes have been chosen as the standard control channels in 5G-NR by the 3rd Generation Partnership Project (3GPP). In this work, we compare polar codes with the two competitor codes that might be used in 5G-NR, which are turbo codes and Low Density Parity Check (LDPC) Codes. The comparison between them focused on advantages and disadvantages of each code scheme to make it easy understanding the performance, achievements, and challenges of each code.

## Coded Frameless ALOHA

- **Status**: ❌
- **Reason**: frameless ALOHA 랜덤액세스+erasure 코드 SIC, 채널 ECC 아닌 충돌해소, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8555829
- **Type**: conference
- **Published**: 25-26 Oct.
- **Authors**: Shun Ogata, Koji Ishibashi
- **PDF**: https://ieeexplore.ieee.org/document/8555829
- **Abstract**: We propose a random access scheme named coded frameless ALOHA to completely eliminate the inherent error floor of the original frameless ALOHA, and show the optimized performance of the system. Coded frameless ALOHA uses erasure correcting codes, and transmitted packets are retrieved by an iterative process between successive interference cancellation and a message-passing decoder for erasure correcting codes. The packet loss rate of coded frameless ALOHA is theoretically analyzed and used to optimize parameters so that the achievable throughput is maximized. Numerical examples show that the proposed scheme exhibits better performance than conventional frameless ALOHA schemes.

## Security-oriented DSA for Network Access Control in Cognitive Radio Networks

- **Status**: ❌
- **Reason**: 인지무선 보안 DSA/NAC; LDPC ECC 무관
- **ID**: ieee:8574191
- **Type**: conference
- **Published**: 23-24 Oct.
- **Authors**: Lei Li, Chunxiao Chigan, Shuai Yuan
- **PDF**: https://ieeexplore.ieee.org/document/8574191
- **Abstract**: Observing both Dynamic Spectrum Allocation/Access (DSA) and Network Access Control (NAC) are indispensable for granting network access privilege to eligible Cognitive Radio Network (CRN) users, we propose a novel security-oriented DSA algorithm to provide communication confidentiality for NAC in CRNs with negligible network performance degradation. Moreover, with the integration of this security-oriented DSA into NAC framework, the implementation complexity of NAC system is reduced. This is because not only is the complex encryption/decryption in traditional NAC replaced with our DSA, but also can the usage of a management mechanism to coordinate operations between DSA and NAC in real-world CRN systems be avoided. As the result, a complete secure solution for NAC design is achieved as the security-oriented DSA is capable of providing confidential communication for both authentication messages and subsequent user data. The analysis shows our proposed cryptography based NAC framework is robust to varying communication environment. Simulations verify that the confidentiality achieved by security-oriented DSA induces negligible degradation on average throughput per user compared with existing DSA schemes.

## Coding for Short Messages in Multipath Underwater Acoustic Communication Channels

- **Status**: ❌
- **Reason**: 수중음향 short-packet 컨볼루션(FTB) 부호 평가; 비-LDPC, 이식 디코더 기법 없음
- **ID**: ieee:8604711
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Mohammadhossein Behgam, Y. Rosa Zheng, Zhiqiang Liu
- **PDF**: https://ieeexplore.ieee.org/document/8604711
- **Abstract**: This paper applies the full tail-biting (FTB) convolutional codes to short data packets and evaluates their performance in underwater acoustic communication by computer simulation and an ocean experiment. The simulation results for AWGN channels show that the FTB codes achieve the similar bit error rate (BER) performance as the zero-tailing convolutional (ZTC) codes regardless of block lengths, while the direct-truncate convolutional (DTC) codes suffer from BER degradation, specially with short block lengths. Both simulation and ocean experimental results demonstrate that the FTB codes are excellent candidates for underwater acoustic communication systems where short data blocks and strong error correction codes are needed.

## A Novel D-Metric for Blind Detection of Polar Codes

- **Status**: ❌
- **Reason**: polar 코드 블라인드 검출용 D-메트릭; 부호 비의존적 디코더 기법 아니고 polar SC/SSC 특화
- **ID**: ieee:8598385
- **Type**: conference
- **Published**: 21-24 Oct.
- **Authors**: Yuqing Ren, Feng Shu, Liping Li +3
- **PDF**: https://ieeexplore.ieee.org/document/8598385
- **Abstract**: As a known error-correcting code that has been proved to fully achieve the binary discrete memoryless channel (B-DMC) capacity, polar codes have been considered as a breakthrough in coding theory since its invention. In 2016, polar codes were selected by the 3GPP as the control channel codes for the enhance mobile broadband (eMBB) scenario. The related research of polar codes has been further pushed to the forefront of applications. In spite of the urgent practical needs, research on the algorithm design and efficient implementation of polar codes for control channels and Internet of Things (IoT) is still in infancy. This paper is to combine successful cancellation (SC) and simplified successful cancellation (SSC) decoders to propose a low-complexity algorithm that can realize blind detection of polar codes. Log-likelihood ratios (LLRs) of frozen bits are used to introduce a new metric D, which is to distinguish polar codes of different formats. The realization of blind detection of polar codes can avoid the receiver's executing complicated decoding algorithm for all polar code candidates, reducing the power, complexity, and delay.

## Nanopore DNA Sequencing Channel Modeling

- **Status**: ❌
- **Reason**: 나노포어 DNA 시퀀싱 채널모델링; ECC 설계 방향 제시뿐 신규 LDPC 기법 없음
- **ID**: ieee:8598361
- **Type**: conference
- **Published**: 21-24 Oct.
- **Authors**: Laura Conde-Canencia, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/8598361
- **Abstract**: In this paper we first present a simplified DNA storage chain (partially inspired by the classical digital communication principles) and review the last advances on error-correcting codes for DNA storage. We then introduce a novel DNA channel model for a new generation of nanopore sequencers. For this, we analyze the reported experimental results to define and characterize an original DNA sequencing channel model. This contribution opens new directions in the design of efficient error-correcting codes to improve the performance of DNA-based data storage.

## Memory-efficient Error Correction Scheme for Flash Memories using GPU

- **Status**: ❌
- **Reason**: 플래시 메모리 BCH ECC의 패리티 배치/GPU 구현; 비-LDPC 부호이고 이식할 LDPC 디코더 기법 없음
- **ID**: ieee:8598394
- **Type**: conference
- **Published**: 21-24 Oct.
- **Authors**: Arul K. Subbiah, Tokunbo Ogunfunmi
- **PDF**: https://ieeexplore.ieee.org/document/8598394
- **Abstract**: In this paper, we present an alternate method to organize the parity bits of Bose-Chaudhuri-Hocquenghen (BCH) encoder on a Flash memory array. Previous methods for BCH error correction scheme requires parity bytes to be stored within a given block thus reducing the ability to scale up for higher bit error correction capabilities. A new memory organization of the parity bits in the user area is proposed, so the limitation of the number of bit errors to be corrected is removed. Without sacrificing the throughput, this method provides a LUT approach where the parity bits, for a given user data block, are stored in local GPU memory. The experimental results show that, in the case of BCH (8191, 7983, 16), there are no limitations imposed by the spare area for the number of bit errors to be corrected. Also, there is no speed degradation in bit error correction by utilizing the user data area for parity bits with the proposed GPU implementation.

## Array LDPC Code-based Compressive Sensing

- **Status**: ❌
- **Reason**: array LDPC 패리티검사 행렬을 압축센싱 측정행렬로 사용, ECC 디코딩 아님(소스/센싱 응용)
- **ID**: ieee:8635990
- **Type**: conference
- **Published**: 2-5 Oct. 2
- **Authors**: Mahsa Lotfi, Mathukumalli Vidyasagar
- **PDF**: https://ieeexplore.ieee.org/document/8635990
- **Abstract**: In this paper, we focus on the problem of compressive sensing using binary measurement matrices, and basis pursuit as the recovery algorithm. We obtain new lower bounds on the number of samples to achieve robust sparse recovery using binary matrices and derive sufficient conditions for a binary matrix with fixed column-weight to satisfy the robust null space property. Next we prove that any column-regular binary matrix with girth 6 has nearly optimal number of measurements. Then we show that the parity check matrices of array LDPC codes are nearly optimal in the sense of having girth six and almost satisfying the lower bound on the number of samples. Array code parity check matrices demonstrate an example of binary matrices that achieve guaranteed recovery via robust null-space property and in practice for n ≤ 106 provide faster recovery compared to the Gaussian counterpart.

## Teaching Reform Design Based on MATLAB

- **Status**: ❌
- **Reason**: LDPC 교육(teaching reform) 논문 — 신규 기여 없음, 제외
- **ID**: ieee:8589376
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Xiumin Wang, Hong Chang, Binggang Xiao +3
- **PDF**: https://ieeexplore.ieee.org/document/8589376
- **Abstract**: This paper analyzes some problems in the teaching process of "Information Theory and Coding". According to the characteristics of the course and the teaching process, a new teaching method is proposed, which focuses on cultivating students' multi-faceted ability. This article explores new teaching methods on the basis of theoretical teaching, focusing on cultivating students' multi-faceted abilities. This teaching method, through the practice and self-learning process, takes the design of the coding and decoding structure of LDPC code as an example, combines theory with practice, stimulates students' self-learning consciousness, deepens theoretical understanding, and cultivates compound talents.

## Low-complexity Check Node Processing for Trellis Min-max Nonbinary LDPC Decoding

- **Status**: ❌
- **Reason**: 비이진(GF(32)) NB-LDPC 디코더/CNU 아키텍처 - non-binary는 기준상 명시적 제외
- **ID**: ieee:8587443
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Huyen Pham Thi, Hung Dao Tuan, Le Dinh Trang Dang +2
- **PDF**: https://ieeexplore.ieee.org/document/8587443
- **Abstract**: Nonbinary low-density-parity-check (NB-LDPC) code outperforms their binary counterpart in terms of error-correcting performance when the code length is moderate. Check node processing is a bottleneck of the NB-LDPC decoding. In this paper, a novel half-row modified two-extra-column trellis min-max (HR-mTEC-TMM) algorithm is proposed for the check node processing to reduce not only the complexity but also the storage memory. The check node unit (CNU) architecture corresponding to the proposed algorithm is designed for the (837, 726) NB-LDPC code over GF(32). The implementation results using 90-nm CMOS technology show that the proposed CNU architecture obtains a reduction of 28.3% for the area and 43.87% for the storage memory with an acceptable error-correcting performance loss, compared to existing work.

## A PDQ-Based Iterative Receiver in Massive MIMO Systems With Low Resolution ADCs

- **Status**: ❌
- **Reason**: Massive MIMO 저해상도 ADC 수신기/양자화 최적화 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8555531
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Junhao Lin, Ming Jiang
- **PDF**: https://ieeexplore.ieee.org/document/8555531
- **Abstract**: In this paper, we propose a low-complexity pseudo-de-quantization based (PDQ-based) iterative receiver in massive multi-user multi-input multi-output (MU-MIMO) systems with low resolution analog-to-digital converters (ADCs). First, a unified framework of massive MU-MIMO system with low resolution ADCs is presented. Then, a low-complexity iterative algorithm applying iterative soft decision interference cancellation (ISDIC) is introduced, where a soft information updating scheme is proposed for the PQD-based optimal detection and an iterative architecture of PDQ-based receiver is given. After that, the effect of quantization step size on the performance of PDQ-based iterative receiver is discussed and a new method is proposed to optimize the quantization step with given resolution ADCs. Finally, simulation results show that the PDQ-based iterative receiver can achieve significant improvement with iterative processing and provide a noticeable performance gain over the MMSE-ISDIC receiver with low resolution ADCs.

## Enhanced Bit-Flipping Successive Cancellation Decoding for Convolutional Polar Codes

- **Status**: ❌
- **Reason**: convolutional polar용 BF-SC 디코딩; polar 전용 SC 디코더, LDPC BP 이식 불가
- **ID**: ieee:8555718
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Ran Zhang, Yiqun Ge, Wuxian Shi +1
- **PDF**: https://ieeexplore.ieee.org/document/8555718
- **Abstract**: The paper presents an enhanced bit-flipping (BF) successive cancellation (SC) decoding method under limited cyclic redundancy checks (CRC). Although BF-SC decoding achieves comparable performance to SC list decoding via a series of SC decodings, the existing methods are inevitably impaired under limited CRC checks, which is the case during blind detection in physical downlink control channel. To this end, we propose a path-metric-assisted BF-SC method, which before CRC checks filters the clearly erroneous decodings and further prioritizes the ones more likely to be correct. Combined with convolutional polar codes - a recently-proposed encoding method with substantial coding gain but same $2x2$ kernel as the original polar, the proposed method is demonstrated to outperform the reference polar code settings in the current 5G standard even with limited CRC checks.

## Rate Matching and Piecewise Sequence Adaptation for Polar Codes with Reed-Solomon Kernels

- **Status**: ❌
- **Reason**: Polar codes with RS kernels rate matching; 비-LDPC 부호, LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:8555566
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Ran Zhang, Hamid Saber, Yiqun Ge +1
- **PDF**: https://ieeexplore.ieee.org/document/8555566
- **Abstract**: The paper studies rate matching for polar codes with Reed-Solomon (RS) kernels. A low-complexity rate matching scheme, referred to as smallest index puncturing, is put forward with validity proof. To resolve the dramatically increased complexity of reliability sequence generation due to rate matching, a piecewise sequence adaptation method is designed. The method significantly cuts down the computation complexity while keeping a negligible performance loss. Simulation results demonstrate the performance gain of the 4-dimension RS kernel over the original binary 2-by-2 kernel under rate matching, and verify the efficacy of the proposed piecewise method.

## Performance Analysis of Land-to-Ship Marine Communication Based on Block Markov Superposition Transmission and Spatial Modulation

- **Status**: ❌
- **Reason**: 해상통신 BMST+공간변조; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8555637
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Yao Shi, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/8555637
- **Abstract**: Marine communications are distinct from terrestrial mobile communications, whose performance is affected by many factors, such as ship movement, waves, rain and fog. The system described in this paper is a coastal communication network based on distributed antennas. In order to improve the reliability of information transmission in the oceanic environment, a transmission mechanism is proposed in this paper, which is based on block Markov superposition transmission and spatial modulation. We investigate the performance of the proposed transmission mechanism under the Rician fading channel and discuss the impact of different parameters on the bit error rate. Simulation results verify the analyses and indicate that the proposed scheme gives a better bit error rate in marine environment.

## Polar Coding for Noncoherent Block Fading Channels

- **Status**: ❌
- **Reason**: 블록페이딩 채널 polar 코딩; 비-LDPC, 이식 가능 LDPC 기법 없음
- **ID**: ieee:8555698
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Mengfan Zheng, Wen Chen, Cong Ling
- **PDF**: https://ieeexplore.ieee.org/document/8555698
- **Abstract**: In this paper, we consider the problem of polar coding for block fading channels without any instantaneous channel state information (CSI). We first decompose a block fading channel of Tc symbols per coherent interval into Tc binary-input sub-channels in a mutual-information-preserving way, and then design a multilevel (MLC) polar coding scheme for them. The proposed scheme achieves the ergodic mutual information of binary-input block fading channels with only channel distribution information (CDI). Simulations results are presented to compare the performance of the proposed MLC scheme and polar codes designed for i.i. d. fading channels with interleaving, which can provide some guidance for practical designs.

## Redundant Residue Number System Coded Diffusive Molecular Communications

- **Status**: ❌
- **Reason**: RRNS(잉여수계) 부호의 분자통신 응용; 비-LDPC, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8555582
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Liwei Mu, Xingcheng Liu, Lie-Liang Yang
- **PDF**: https://ieeexplore.ieee.org/document/8555582
- **Abstract**: To enhance the reliability of diffusive molecular communications (DMC), redundant residue number system (RRNS) code is introduced to DMC in this paper. We justify the rationality behind the application of RRNS code in DMC, and explain the principles of the RRNS-coded DMC. Assuming binary molecular shift keying (BMoSK) modulation, we investigate the performance of DMC systems, when the DMC systems experience both inter-symbol interference (ISI) and molecular noise. Our studies and performance results show that RRNS code constitutes a class of promising error-control codes, which facilitates DMC systems to achieve a good trade-off among coding rate, implementation complexity and reliability.

## Increasing Minimum Distance of Polar Codes with Outer Parity-Check Codes

- **Status**: ❌
- **Reason**: polar+outer parity-check 연접부호, list SC 디코더 — 비-LDPC 부호, 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:8539599
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Kyungmok Oh, Daejin Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8539599
- **Abstract**: This work proposes a concatenated coding scheme which consists of inner polar codes and outer parity-check nodes aiming at increasing minimum distance. There have been a few studies on the concatenation of polar and parity-check codes, which are however heuristic approaches. This work instead proposes a systematic and deterministic algorithm based on a necessary condition to achieve an increased minimum distance. We demonstrate that the proposed coding scheme has a better error-rate performance as compared to those of competing codes such as polar-CRC codes, turbo codes and low-density parity-check (LDPC) codes at short lengths. In addition, it will be shown that codes with the proposed scheme can be efficiently decoded with a list successive cancellation (SC) decoder. The performance superiority of the proposed coding scheme will be confirmed via Monte-Carlo simulations.

## Design and Performance Analysis of Vehicle MIMO System for NR-based enhanced V2X

- **Status**: ❌
- **Reason**: eV2X 차량 MIMO 시스템 설계, LDPC는 표준 NR 부호 부수 적용 — 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:8539612
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Sangmi Moon, Intae Hwang
- **PDF**: https://ieeexplore.ieee.org/document/8539612
- **Abstract**: The 3rd Generation Partnership Project (3GPP) has recently developed enhanced vehicle-to-everything (eV2X) communication. The requirements of the eV2X service are significantly higher than those of existing V2X, with the required data transmission rates ranging from tens of Mbps to up to 1000 Mbps. In addition, communication should be performed with an extremely low error probability within a time delay of several to several tens of ms. In this study, a low-density parity-check code and 256 quadrature amplitude modulation (QAM), which are new radio technologies, are applied to meet the low-latency, high-reliability, and high-data-rate requirements of eV2X. In addition, we propose a vehicle multiple-input multiple-output system. The proposed system increases reliability through transmit diversity and lowers latency through a short transmission time interval. Simulation results show that the proposed system exhibits high reliability, high data rate, and low latency.

## Efficiently Encodable Multi-Edge Type LDPC Codes for Long-Distance Quantum Cryptography

- **Status**: ❌
- **Reason**: QKD reconciliation용 MET-LDPC, 게다가 비이진 다중에지 — 정보조정+선형시간 인코딩만, 떼어낼 디코더/HW 기여 없음
- **ID**: ieee:8539496
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Suhwang Jeong, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/8539496
- **Abstract**: Reconciliation is a key procedure in quantum cryptography to share the same secret key between two remote parties. For long-distance quantum cryptography, the reconciliation is often realized with multi-edge type low-density parity-check (MET-LDPC) codes due to unique advantages of MET-LDPC codes, e.g. a suitable structure for decoder implementation and capacity-approaching performances especially at very low rates. However, to make the realization practically viable, the encoding complexity of MET-LDPC codes must also be properly addressed, which unfortunately has been well touched. This work proposes a simple but efficient MET-LDPC code structure which allows a linear-time encoding complexity of MET-LDPC codes without compromising their error-correcting performances.

## LDPC-based Joint Source-Channel-Network Coding for the Multiple Access Relay Channel

- **Status**: ❌
- **Reason**: MARC용 JSCN LDPC 결합 소스-채널-네트워크 코딩 — LDPC 베이스라인, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:8629710
- **Type**: conference
- **Published**: 16-19 Oct.
- **Authors**: Marwa Ben Abdessalem, Amin Zribi, Tadashi Matsumoto +1
- **PDF**: https://ieeexplore.ieee.org/document/8629710
- **Abstract**: In this work, we investigate the MARC (Multiple Access Relay Channel) setup, in which two Markov sources communicate to a single destination, aided by one relay, based on Joint Source Channel Network (JSCN) LDPC codes. In addition, the two source nodes compress the information sequences with an LDPC source code. The compressed symbols are directly transmitted to both a relay and a destination nodes in two transportation phases. Indeed, the relay performs the concatenation of the received compressed sequences to obtain a recovered sequence, which is encoded with an LDPC channel code, before being forwarded to the destination. At the receiver, we propose an iterative joint decoding algorithm that exploits the correlation between the two sources-relay data and takes into account the errors occurring in the sources-relay links to estimate the source data. We show based on simulation results that the JSCN coding and decoding scheme into a MARC setup achieves a good performance with a gain of about 5 dB compared to a conventional LDPC code.

## Bit-Interleaved Coded Modulation using Set Partitioned 4-D Multidimensional for Optical Commmunications

- **Status**: ❌
- **Reason**: 광통신 BICM 4D 변조 설계, LDPC는 베이스라인이고 떼어낼 디코더·코드설계 없음
- **ID**: ieee:8580328
- **Type**: conference
- **Published**: 15-19 Oct.
- **Authors**: Brayan Peñafiel, Andres Ortega
- **PDF**: https://ieeexplore.ieee.org/document/8580328
- **Abstract**: In this paper, we proposed a novel Bit-Interleaved LDPC Coded Modulation scheme for long-haul coherent optical link at 50/80/100 km using the method called Set Partitioned (SP) to generate 4-D Multidimensional Modulations with 3 subcarriers in order to transmit at 4096 SP-QAM and 8192 SP-QAM rectangular and cross constellations-points respectively. The results show that the Spectral Efficiency (SE) is reduced at 2 bit/sym/Hz and improve the BER performance system around 10dB in terms of OSNR with respect to traditional techniques of modulations.

## Rateless codes for satellite systems over rain fading channels

- **Status**: ❌
- **Reason**: 위성 rateless 코드로 기존 LDPC 활용, 이식할 LDPC ECC 기법 없음
- **ID**: ieee:8742499
- **Type**: conference
- **Published**: 15-18 Oct.
- **Authors**: Satya Chan, Meixiang Zhang, Daesub Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/8742499
- **Abstract**: Modern satellite systems utilize high frequency bands usually above 15 GHz to provide high speed transmission services, and adopt adaptive modulation and coding (AMC) schemes in order to countermeasure serious rain fading occurred in the utilized frequency bands. This paper introduces an efficient scheme to countermeasure rain fading by using rateless codes. The proposed scheme utilizes existing AMC scheme with the LDPC codes, and thus it can be easily combined with existing standards. The error rate and spectral efficiency performance simulation results demonstrate performance enhancement over a satellite rain fading channel, with almost the same code rate as the existing LDPC codes.

## Maximizing data throughput in earth observation satellite to ground transmission by employing a flexible high data rate transmitter operating in X-band and Ka-band

- **Status**: ❌
- **Reason**: 위성 송신기 시스템, 표준 LDPC(DVB-S2)/ACM 단순 사용, 신규 ECC 기여 없음
- **ID**: ieee:8742521
- **Type**: conference
- **Published**: 15-18 Oct.
- **Authors**: Philipp Wertz, Marcus Kiessling, Franz-Josef Hagmanns
- **PDF**: https://ieeexplore.ieee.org/document/8742521
- **Abstract**: Earth Observation (EO) and Intelligence, Surveillance and Reconnaissance (ISR) Systems equipped with High Resolution instruments are designed for high-performance operations in terms of fast revisit time, for very short system response time and for providing actionable intelligence with low data latency. The increased reliance on this data has created demand for decreasing latency. However, higher speeds and increasing bandwidth for data download are needed with the increasing numbers of satellites. At the same time, the scarce frequency resources especially in X-band (8.025 GHz to 8.4 GHz) but also in Ka-band (25.5 GHz to 27 GHz) call for more bandwidth efficient modulation schemes. This paper shares details regarding a new data transmission solution to efficiently use the available radio frequency (RF) bandwidth both in X-Band and Ka-Band by using Adaptive Coding & Modulation (ACM) as a key technology, allowing the volume of data to adapt to link budget characteristics. At the same time, high performance forward error correction coding such as SCCC and LDPC (DVB-S2) and high order modulation schemes (up to 64-APSK) are used, yielding both high power and spectrum efficiency. in terms of end-to-end performance, such sophisticated systems need to account for the ground station receiver characteristics. The proposed solution has therefore been verified using prototypes of both transmitter and receiver. Finally, a specific highly integrated transmitter design suited for smaller Earth Observation satellites down to SmallSats is presented.

## Enhancing LoRa Capacity using Non-Binary Single Parity Check Codes

- **Status**: ❌
- **Reason**: LoRa 용량 향상용 non-binary SPC 부호; 비이진+비-LDPC 단일패리티검사, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8589188
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Tallal Elshabrawy, Joerg Robert
- **PDF**: https://ieeexplore.ieee.org/document/8589188
- **Abstract**: LoRa has established itself as one of the main solutions within evolving Low Power Wide Area Networks, LP-WAN. LoRa is primarily pillared on its patented chirp spread spectrum modulation. In LoRa modulation, linearly increasing cyclic chirp signals span the LoRa bandwidth. The rate of increase of these chirp signals is dependent on the applied spreading factor (SF). Increasing the spreading factor extends the coverage range for LoRa communication at the expense of a reduced data rate. Typically, LoRa signals with different spreading factors are quasi-orthogonal such that LoRa essentially supports multiple simultaneous logical networks with different coverage ranges. Given that LoRa utilizes an ALOHA-based protocol for medium access, the total capacity of LoRa networks is governed by the system loads and time-on-air for packet transmissions of each SF-network. In this paper, non-binary single parity check (SPC) codes with soft-decision decoding are introduced as a tool to enhance the capacity of LoRa networks. The LLRs for the soft decision decoding of LoRa symbols are first derived. It is then shown that SPC codes succeed in achieving measurable coding gains for typical LP-WAN applications at the scale of 1.2 dB. Coinciding with enabling/disabling SPC in each logical SF-network, the system loads as well as the packet transmission times could be optimized with the objective of maximizing the packet delivery ratio. The presented capacity results indicate that in fact SPC optimization can achieve capacity gains at the scale of up to 65% compared to the nominal LoRa networks.

## Multi-Bit Low Redundancy Error control with Parity Sharing for NoC Interconnects

- **Status**: ❌
- **Reason**: 단순 parity check 기반 NoC EDC, LDPC 아님, 떼어낼 디코더/구성 기법 없음 - 제외
- **ID**: ieee:8724118
- **Type**: conference
- **Published**: 15-16 Oct.
- **Authors**: U. Sai Himaja, M. Vinodhini, N.S. Murty
- **PDF**: https://ieeexplore.ieee.org/document/8724118
- **Abstract**: Network-on-Chips (NoCs) have become an efficient solution to overcome the issues of the bus-based architectures in System-on-Chips (SoCs). In the era of deep sub-micron technology, many systems are getting affected by number of errors which cause NoC failure. In order to overcome this issue, an Error Detection and Correction (EDC) coding technique is needed. So, this paper presents a Multi-bit Low Redundancy Error control with Parity Sharing (MLREPS) coding technique for NoC Interconnects. In this coding technique, a simple parity check code is used to achieve error correction with small area, power and delay overhead. In addition, it achieves higher reliability. Simulated results of the MLREPS coding technique are compared with the 2D fault coding technique. Analysis shows that the proposed coding technique is better than the existing technique in terms of residual error probability, link power consumption and swing voltage of the link by 42.2%, 77% and 55.5%.

## Polar Code Encoder and Decoder Implementation

- **Status**: ❌
- **Reason**: Polar code 인코더/디코더 구현(비-LDPC), 부호비의존 이식 기법 없음 - 제외
- **ID**: ieee:8723895
- **Type**: conference
- **Published**: 15-16 Oct.
- **Authors**: Ajith Cyriac, Gayathri Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/8723895
- **Abstract**: Polar codes are error correction codes developed by Erdal Arikan which achieves channel capacity and its reduced complexity makes it more attractive and successful. In the past several decades we are searching for some techniques which will reduce the effect of noise to a very low value so that we can reproduce the transmitted signal more accurately. Erdal Arkan come up with a new concept which known as polar codes, here we use a channel polarization concept and hence named as polar codes. The discovery of polar code is standing as a milestone in coding theory and lot of researches are carrying out on this topic. Variety of schemes have been proposed over these years for the generation, encoding and decoding of polar codes. The important area of research is the decoder section and most widely used one is successive cancellation decoder[3]. Reduced complexity is the most attractive feature with an overall encoding and decoding complexity of O(NlogN) for a block size of N, which leads to its great success. Polar code concept is used in the most promising 5G technology[10]. In this work a complete implementation of the polar Encoder and decoder is discussed with its MATLAB and Verilog implementations

## A QC-LDPC Code Based Digital Signature Algorithm

- **Status**: ❌
- **Reason**: QC-LDPC+BP를 디지털 서명(보안)에 사용, 표준 부호/디코더 재사용으로 새 ECC 기여 없음
- **ID**: ieee:8648750
- **Type**: conference
- **Published**: 12-15 Oct.
- **Authors**: Fang Ren, Xuefei Yang, Dong Zheng
- **PDF**: https://ieeexplore.ieee.org/document/8648750
- **Abstract**: CFS digital signature algorithm, which proposed in 2001, is the most important code based digital signature algorithm and can resist the known attack of quantum algorithms. But the efficiency of CFS is very low because of the extremely low signing speed and the large public key size. In this paper, a variation of CFS algorithm is presented. Instead of the Goppa code and the Patterson decoding algorithm, the new algorithm selects the Quasi-Cyclic Low Density Parity Check (QC-LDPC) code and the Belief Propagation (BP) decoding algorithm in the signing process. Compared with CFS algorithm, the new algorithm greatly reduces the storage space of public key and improves the efficiency of signature without compromising the security.
