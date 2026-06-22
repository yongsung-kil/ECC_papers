# IEEE Xplore — 2019-05


## Performance Analysis of Matched-Filter Detector for MIMO Spatial Multiplexing Over Rayleigh Fading Channels With Imperfect Channel Estimation

- **Status**: ❌
- **Reason**: MIMO MF 검출기 성능분석, LDPC는 부수 베이스라인 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8611121
- **Type**: journal
- **Published**: May 2019
- **Authors**: Yuto Hama, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/8611121
- **Abstract**: The matched-filter (MF) detector is the lowest complexity linear detector in practical MIMO spatial multiplexing systems. Its performance is significantly affected by the number of available antennas and an operating channel SNR. In this paper, we analyze the exact performance of the MF detector without any restrictions on the numbers of the transmit and receive antennas. To this end, we first develop the exact, closed-form expression of the MF detector output over uncorrelated Rayleigh fading channels with an arbitrary number of antennas. Based on this result, we derive the exact closed-form bit error rate expressions for uncoded BPSK, QPSK, and M-ary QAM signaling, which can be seen as the generalized forms of the conventional receiver diversity based on maximum ratio combining. We also elucidate the conditions on the numbers of antennas and channel SNR, where the use of MF detector should become effective. Furthermore, in the case of coded MIMO systems, we develop the optimal metric derived from the exact MF output. The corresponding mutual information justifies the simulated performance of LDPC-encoded MIMO spatial multiplexing with the MF detector over ideally interleaved Rayleigh fading channels. Finally, we extend our analysis to more practical systems with imperfect channel estimation.

## Log-Likelihood Ratio Calculation for Pilot Symbol Assisted Coded Modulation Schemes With Residual Phase Noise

- **Status**: ❌
- **Reason**: 위상잡음 하 coded modulation LLR 계산식 — AWGN 변조 채널 특이적 LLR, NAND LLR 양자화로 이식 무관
- **ID**: ieee:8630510
- **Type**: journal
- **Published**: May 2019
- **Authors**: Peyman Neshaastegaran, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/8630510
- **Abstract**: This paper presents a novel log-likelihood ratio (LLR) calculation for high order coded modulation schemes over an additive white Gaussian noise channel at the presence of residual phase noise (RPN). Residual phase noise is known to significantly degrade the error rate performance of such systems, particularly at lower error rates, resulting in an early error floor. To model RPN, we consider the commonly used pilot symbol assisted modulation schemes for carrier recovery. We derive the exact formula for the calculation of LLR for such systems. To simplify the implementation, we also derive an approximation of LLR which reduces the complexity significantly with almost no loss in performance. The simulation results are presented for coded modulation schemes based on quadrature amplitude modulations and low-density parity-check codes. The simulations demonstrate significant performance improvement in the error rate as a result of using the new LLR calculation instead of the conventional calculation of LLR which ignores the RPN.

## Spatially Coupled Turbo-Like Codes: A New Trade-Off Between Waterfall and Error Floor

- **Status**: ❌
- **Reason**: spatially coupled turbo-like codes의 waterfall/error floor 분석 — 비-LDPC(turbo) 부호, 부호 비의존 BP 이식 기법 제시 없음
- **ID**: ieee:8631116
- **Type**: journal
- **Published**: May 2019
- **Authors**: Saeedeh Moloudi, Michael Lentmaier, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/8631116
- **Abstract**: Spatially coupled turbo-like codes (SC-TCs) have been shown to have excellent decoding thresholds due to the threshold saturation effect. Furthermore, even for moderate block lengths, the simulation results demonstrate a very good bit error rate performance in the waterfall region. In this paper, we discuss the effect of spatial coupling on the performance of TCs in the finite block-length regime. We investigate the effect of coupling on the error floor performance of SC-TCs by establishing conditions under which the spatial coupling either preserves or improves the minimum distance of TCs. This allows us to investigate the error floor performance of SC-TCs by performing a weight enumerator function analysis of the corresponding uncoupled ensembles. Our results demonstrate that the spatial coupling changes the design trade-off between the waterfall and error floor performance. Instead of optimizing the belief propagation (BP) threshold of uncoupled TCs, which in turn leads to a higher error floor, we can take advantage of the threshold saturation property of the SC-TCs. Choosing strong ensembles, characterized by good maximum-a-posteriori (MAP) thresholds and low error floors, the corresponding SC-TCs are then able to simultaneously approach capacity and achieve very low error floor.

## Experimental Demonstration of Spectrally Efficient Frequency Division Multiplexing Transmissions at E-Band

- **Status**: ❌
- **Reason**: SEFDM E-band 무선 전송 실험. LDPC ECC 기법 없음, 변조/하드웨어 무선 응용 특이적.
- **ID**: ieee:8672498
- **Type**: journal
- **Published**: May 2019
- **Authors**: Hedaia Ghannam, Dhecha Nopchinda, Marcus Gavell +2
- **PDF**: https://ieeexplore.ieee.org/document/8672498
- **Abstract**: This paper presents the design and the experimental demonstration of transmission of spectrally efficient frequency division multiplexing (SEFDM) signals, using a single 5-GHz channel, from 81 to 86 GHz in the E-band frequency allocation. A purpose-built E-band SEFDM experimental demonstrator, consisting of transmitter and receiver GaAs microwave integrated circuits, along with a complete chain of digital signal processing is explained. Solutions are proposed to solve the channel and phase offset estimation and equalization issues, which arise from the well-known intercarrier interference between the SEFDM signal subcarriers. This paper shows the highest transmission rate of 12 Gb/s over a bandwidth varying between 2.67 to 4 GHz depending on the compression level of the SEFDM signals, which results in a spectral efficiency improvement by up to 50%, compared to the conventional orthogonal frequency division multiplexing modulation format.

## A Factor-Graph Clustering Approach for Detection of Underwater Acoustic Signals

- **Status**: ❌
- **Reason**: 수중음향 신호검출용 factor graph 클러스터링/loopy BP — 신호검출 응용, ECC 부호용 디코더 기법 아님
- **ID**: ieee:8579234
- **Type**: journal
- **Published**: May 2019
- **Authors**: Dror Kipnis, Roee Diamant
- **PDF**: https://ieeexplore.ieee.org/document/8579234
- **Abstract**: We address the challenge of detecting an arbitrary-shaped underwater acoustic signal. Instead of setting a detection threshold, which due to noise transients may result in a high false alarm rate (FAR), our method classifies each measured sample as either “noise” or “signal.” Utilizing a priori knowledge of only the minimal duration of the signal, the decision is made using loopy belief propagation over a factor graph. Numerical simulations and sea experimental results show that our scheme achieves a favorable tradeoff between the Recall and FAR, and noise robustness, which far exceeds that of benchmark schemes.

## Quasi-Analytical Simulation Method for Estimating the Error Probability of Star Domain Decoders

- **Status**: ❌
- **Reason**: star domain 디코더 블록오류율 추정용 준해석 시뮬레이션 가속법 — 디코더 알고리즘/HW 기여 아닌 평가방법론
- **ID**: ieee:8629020
- **Type**: journal
- **Published**: May 2019
- **Authors**: Aleksandar Minja, Vojin Šenk
- **PDF**: https://ieeexplore.ieee.org/document/8629020
- **Abstract**: Evaluating the block error rate of a digital communication system is usually done using the Monte Carlo (MC) simulation method. The main drawback of the Monte Carlo method is the need of a huge sample size for estimating low error rates. Other methods commonly used are the importance sampling technique and the quasi-analytical method. This paper introduces the metric star domain decoder model and shows that many practical decoders fall into this category. The main result is the introduction of a novel SNR-invariant quasi-analytical technique for estimating the block error rate of a communication link over the geodesic channel model (a generalization of a vast number of commonly used channels, including binary symmetric channel, BEC, and AWGN channel) with a metric star domain decoder used at the receiver. This technique outperforms the Monte Carlo and importance sampling methods in both accuracy and speed. It is shown that our quasi-analytical method is at least 103 times faster than MC and 10 times faster than IS for the same accuracy.

## Connected-coding Retransmission Scheme for Low-density Parity-check Codes in 5G

- **Status**: ❌
- **Reason**: 5G HARQ 재전송용 connected-coding, 통신 응용 특이적이고 채널 ECC 디코더로 떼어낼 기법 없음
- **ID**: ieee:8770690
- **Type**: conference
- **Published**: 9-10 May 2
- **Authors**: Jingwen Zhang, Jingxuan Huang, Ce Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/8770690
- **Abstract**: Aiming at reducing unnecessary packet losses of transport block (TB) level hybrid automatic repeat request (HARQ), we propose a connected-coding retransmission (CCR) scheme for low-density parity-check (LDPC) codes in 5G data channels. Once the transmission of a TB, which is divided into one or several code blocks (CBs), was failed, we introduce failed CBs information into the parity bits of the new CBs by connected encoding. Then error correction for the failed CBs is achieved again by connected decoding to avoid packet losses. The simulation results in fading channel demonstrate that the proposed scheme efficiently improves both CB error rate performances and system throughput performances.

## Modifying Bit-Level Data Compression Scheme based on Adaptive Hamming Code Data Compression Algorithm

- **Status**: ❌
- **Reason**: Hamming code 기반 데이터 압축(소스 코딩), LDPC ECC와 무관 — 채널코딩 아님
- **ID**: ieee:8743541
- **Type**: conference
- **Published**: 9-10 May 2
- **Authors**: Harwin C. Mendoza, Ariel M. Sison, Ruji P. Medina
- **PDF**: https://ieeexplore.ieee.org/document/8743541
- **Abstract**: This paper is directed towards the development of an improved HCDC(k) to minimize the possibility of inflation. An improved adaptive hamming code data compression has been developed by reducing the number of bits used when substituting a non-valid codeword. The proposed algorithm is expected to provide greater compression ratio, space savings, and compression speed. It is also expected to minimize the possibility of inflation when compressing random texts. To evaluate the efficiency of the modified algorithm, simulations were conducted to compress sample texts from COCA corpus and random texts using the original HCDC(k) and modified HCDC(k). Compressing sample texts from COCA corpus lead to a significant difference of 7.5% in space savings and 0.11 in compression ratio. The simulation conducted with random texts lead to a significant difference of 10.45% in space savings and 0.1 in compression ratio. This means that the modified algorithm is more effective when solving inflation.

## Transmitter Design and Synchronization Concepts for DaViD Display Camera Communication

- **Status**: ❌
- **Reason**: 디스플레이-카메라 가시광 통신 변조/동기화, LDPC 부수 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:8770659
- **Type**: conference
- **Published**: 9-10 May 2
- **Authors**: Jianshuang Xu, Johannes Klein, Christian Brauers +1
- **PDF**: https://ieeexplore.ieee.org/document/8770659
- **Abstract**: Visible Light Communication is a promising technology for data transmission, which has become more and more relevant in recent years. Other than the common approach of modulated LED lighting, display-camera communication has become an attractive novel take on the concept. As outlined in earlier papers, the DaViD (Data Transmission Using Video Displays) system provides a modulation concept allowing for a data overlay onto video content which is nearly invisible to the viewer, i.e. causing hardly any perceptible degradation in video quality. This is achieved by differentially modulating the chrominance information of the underlying video frames with low amplitudes. The resulting color differences within the recorded images can be interpreted by the receiver, allowing for reconstruction of the transmitted data. In this paper, we introduce further system details and improvements to the DaViD concept. In addition to traditional transmission systems, on the display-camera link, the receiver has to be not only temporally but also spatially synchronized to the transmitter. We address the spatial synchronization problem by utilizing localization patterns for detecting the modulation area and a separate optimization on columns and rows for data resampling. Using a slight temporal oversampling, clean data frames can be reconstructed on the receiver side. Based on our modulation and coding concept, we achieve a data rate up to 34.56 Mbit/s in our current demonstration setup with hardly any visible degradation in video quality.

## Experimental Investigation of Security Gaps when using Punctured LDPC Coding in Coherent Systems up to 64-GBd DP-64QAM

- **Status**: ❌
- **Reason**: 광통신 물리계층 보안 gap 실험, 표준 punctured LDPC 사용·보안 도메인, 새 디코더/구성 없음
- **ID**: ieee:8727123
- **Type**: conference
- **Published**: 8-8 May 20
- **Authors**: Carsten Schmidt-Langhorst, Johannes Pfeiffer, Robert Elschner +4
- **PDF**: https://ieeexplore.ieee.org/document/8727123
- **Abstract**: In optical transmission systems, security against eavesdroppers is of increasing importance. Following the concept of physical-layer security, we experimentally quantify the security gap that can be achieved when applying punctured low-density parity-check (LDPC) codes for various modulation schemes and bit rates in a state-of-the art laboratory coherent optical communication system. We examine operating points at gross bit-rates up to 768 Gb/s using up to 64.0-GBd dual-polarization (DP) 64-ary quadrature amplitude modulation (QAM) in combination with bit-interleaved coded modulation (BICM). We find that security gaps ranging from 5.6 dB for a net secure data rate of 76.2 Gb/s (32-GBd DP-QAM04) up to 10.7 dB for 457 Gb/s (64-GBd DP-QAM64) are required for the legitimate receiver over the eavesdropper. For the low-cardinality DP-QAM04 format the required security gap is mainly equal to the theoretically achievable minimum security gap. However, with increasing cardinality of the modulation format, the practical implementation penalty accounts for a significant portion of the security gap of up to an additional 3.7 dB at 64-GBd DP-QAM64.

## Record-Sensitivity Gb/S Receiver for Free-Space Applications Based on Phase-Sensitive Amplification

- **Status**: ❌
- **Reason**: 자유공간 광 수신기 PSA, half-rate FEC 부수 언급뿐 LDPC 기법 없음
- **ID**: ieee:8750400
- **Type**: conference
- **Published**: 5-10 May 2
- **Authors**: Ravikiran Kakarla, Jochen Schroder, Peter A. Andrekson
- **PDF**: https://ieeexplore.ieee.org/document/8750400
- **Abstract**: We report error-free, 1 photon-per-bit receiver sensitivity using 10.52 Gb/s QPSK data and a half-rate FEC, enabled by a low-noise phase-sensitive pre-amplifier as well as injection-locking-based pump recovery at sub nano-watt powers. © 2019 The Author(s)

## High Dimensional Quantum Key Distribution with Biphoton Frequency Combs through Energy-Time Entanglement

- **Status**: ❌
- **Reason**: 고차원 QKD(에너지-시간 얽힘), LDPC 무관 양자 키 분배
- **ID**: ieee:8749215
- **Type**: conference
- **Published**: 5-10 May 2
- **Authors**: Murat Can Sarihan, Kai-Chi Chang, Xiang Cheng +7
- **PDF**: https://ieeexplore.ieee.org/document/8749215
- **Abstract**: Biphoton frequency combs offer a photon-efficient way to achieve a very high-rate quantum key distribution by utilizing both time and frequency-bin encoding, while offering theoretically proven unconditional security. © 2019 The Author(s)

## Combined Probabilistic Shaping and Nyquist Pulse Shaping for PAM8 Signal Transmission in WDM Systems

- **Status**: ❌
- **Reason**: WDM PAM8 확률적 셰이핑, LDPC는 베이스라인 코드일뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8750524
- **Type**: conference
- **Published**: 5-10 May 2
- **Authors**: Xiao Han, Mingwei Yang, Ivan B. Djordjevic +4
- **PDF**: https://ieeexplore.ieee.org/document/8750524
- **Abstract**: We use the LDPC-coded probabilistically shaped PAM8 signaling combined with Nyquist pulse shaping to improve the transmission performance in a WDM system. We find that the combination of these shaping schemes offers great performance improvement. © 2019 The Author(s)

## A Modified McEliece Public-Key Cryptosystem Based On Irregular Codes Of QC-LDPC and QC-MDPC

- **Status**: ❌
- **Reason**: QC-LDPC/QC-MDPC 기반 McEliece 공개키 암호, 보안 응용으로 채널 ECC 기법 아님
- **ID**: ieee:8786376
- **Type**: conference
- **Published**: 30 April-2
- **Authors**: Seyed Hesam Odin Hashemi, Ghosheh Abed Hodtani
- **PDF**: https://ieeexplore.ieee.org/document/8786376
- **Abstract**: In this paper, a novel structure was proposed for the McEliece cryptosystem. The McEliece public key cryptosystem utilizes Goppa's codes properties to provide security. Due to its robust security and fast speed of executing the encryption and decryption algorithm, McEliece cryptosystem was suggested as an option for post-quantum systems. However, this cryptosystem is not commonly used nowadays due to several major drawbacks. The most important defect in the McEliece cryptosystem is its lengthy key. In this research, Goppa code was replaced by irregular codes of QC-LDPC and QC-MDPC that are utilized simultaneously in order to resolve the prior bottlenecks of this system. The obtained results further verified that the key length was reduced reasonably. Another advantage of this release compared to the traditional version of McEliece cryptosystem is that it has been more secure against message-resend attacks.

## Distributed Processing for Encoding and Decoding of Binary LDPC codes using MPI

- **Status**: ❌
- **Reason**: 표준 binary LDPC 인코딩/디코딩의 MPI 분산처리 가속만 다룸; NAND ECC에 이식할 새 디코더·HW·코드설계 기법 없음
- **ID**: ieee:8845079
- **Type**: conference
- **Published**: 29 April-2
- **Authors**: Bhargav Gokalgandhi, Ivan Seskar
- **PDF**: https://ieeexplore.ieee.org/document/8845079
- **Abstract**: Low Density Parity Check (LDPC) codes are linear error correcting codes used in communication systems for Forward Error Correction (FEC). But, intensive computation is required for encoding and decoding of LDPC codes, making it difficult for practical usage in general purpose software based signal processing systems. In order to accelerate the encoding and decoding of LDPC codes, distributed processing over multiple multi-core CPUs using Message Passing Interface (MPI) is performed. Implementation is done using Stream Processing and Batch Processing mechanisms and the execution time for both implementations is compared w.r.t variation in number of CPUs and number of cores per CPU. Performance evaluation of distributed processing is shown by variation in execution time w.r.t. increase in number of processors (CPU cores).

## Evaluation of Age of Information for LDPC Coded Transmission over AWGN Channels

- **Status**: ❌
- **Reason**: LDPC 부호화 전송의 Age of Information 이론 분석; 디코더·HW·구성 기여 없는 메트릭 분석
- **ID**: ieee:8746291
- **Type**: conference
- **Published**: 28 April-1
- **Authors**: Mangang Xie, Qianfan Wang, Jie Gong +1
- **PDF**: https://ieeexplore.ieee.org/document/8746291
- **Abstract**: Age of information (AoI) is an important metric in real-time status update communication system to assess the freshness of information. Different from previous works, this paper focuses on the average AoI over additive white Gaussian noise (AWGN) channels. A fixed redundancy (FR) coding scheme is considered, which encodes each k-bits update as an n-bits packet by a low-density parity-check (LDPC) code. By using the renewal-reward theory, a closed-form expression of the average AoI under the FR scheme is derived. Simulation results show that the average AoI relies on Eb/N0, especially in the low Eb/N0 region. For different Eb/N0, an optimal code length always exists to minimize the average AoI. In addition, the same average AoI can be achieved with different code lengths in the high Eb/N0 region. Hence, in the high Eb/N0 region, short codes are preferred especially when the transmission delay is taken into account.

## Design and Experimental Prototyping of Layered Hybrid Decode-Estimate-Forward Relaying

- **Status**: ❌
- **Reason**: 무선 릴레이/UEP 응용, off-the-shelf LDPC를 베이스라인으로만 사용 — NAND로 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:8746434
- **Type**: conference
- **Published**: 28 April-1
- **Authors**: Abeer Ahmad, Imdad Khan, Ahmed Nayyar Hassan +2
- **PDF**: https://ieeexplore.ieee.org/document/8746434
- **Abstract**: We propose, design, and prototype (using software defined radios) a layered hybrid decode-estimate- and-forward relaying strategy. The scheme relies on splitting the source message into two layers with unequal error protection (UEP). Considering half-duplex relay operation, cooperation takes place over two time-slots. The relay attempts to decode both layers during the first time-slot; with the probability of successfully decoding one of the layers being higher than the other due to UEP between the two layers. During the second time-slot, the relay transmits the jointly encoded message containing the successfully decoded layer(s) with the (imperfect) decoding estimates of the unrecoverable layer(s). In order to recover the source information, we design a decoding strategy at the destination that jointly operates on the signals received from the source and the relay. The proposed scheme is implemented using off-the-shelf systematic low-density parity-check codes, with joint decoding achieved through iterative message-passing. Simulations over narrowband Gaussian links indicate a performance gain of up to 3 dB compared to the unlayered operation at the source. We also present prototype results with over-the-air transmissions using National Instruments (NI) USRPs 2921s with all baseband processing implemented in NI LabView. These experimental results indicate significant performance gains over a conventional unlayered relaying approach.

## Performance Analysis and Optimization for the LDPC-Coded Multi-Carrier LDS System

- **Status**: ❌
- **Reason**: 무선 MC-LDS 수신기 특화 joint detection-decoding, LDPC는 베이스라인 — 이식 가능한 ECC 기법 없음
- **ID**: ieee:8746490
- **Type**: conference
- **Published**: 28 April-1
- **Authors**: Han Wang, Kexin Xiao, Bin Xia +1
- **PDF**: https://ieeexplore.ieee.org/document/8746490
- **Abstract**: With the common property of the sparse structure, multi-carrier low density signature (MC-LDS) and low density parity-check (LDPC) codes can be combined into a joint sparse factor graph (JSFG) while the joint detection and decoding (JDD) algorithm could bring significant gains in terms of the bit error rate (BER). In this paper, considering the coupling character of the soft information interaction in the elaborate JSFG, we carve the distribution of the merged decoding soft information from both sides and theoretically analyze the error performance of the uplink LDPC-coded MC-LDS system. Correspondingly, not only the average BER but also the practical decoding threshold could be effectively derived for any given number of iterations. Furthermore, based on the theoretical analysis, we optimize the degree distribution of the JSFG by leveraging the differential evolution method. Finally, simulation results show that the practical threshold of the JDD receiver with the optimized code approaches the signal to noise ratio of the theoretical capacity.

## An Automated FPGA-Based Framework for Rapid Prototyping of Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 전용 FPGA 프로토타이핑 프레임워크 — 바이너리 아니므로 제외
- **ID**: ieee:8702616
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Yaoyu Tao, Qi Wu
- **PDF**: https://ieeexplore.ieee.org/document/8702616
- **Abstract**: Nonbinary LDPC codes have shown superior performance close to the Shannon limit. Compared to binary LDPC codes of similar lengths, they can reach orders of magnitudes lower error rate. However, multitude of design freedoms of non-binary LDPC codes complicates the practical code and decoder design process. Fast simulations are critically important to evaluate the pros and cons. Rapid prototyping on FPGA is attractive but takes significant design efforts due to its high design complexity. We propose a high-throughput reconfigurable hardware emulation architecture with decoder and peripheral co-design. The architecture enables a library and script-based framework that automates the construction of FPGA emulations. Code and decoder design parameters are programmed either during run time or by script in design time. We demonstrate the capability of the framework in evaluating practical code and decoder design by experimenting with two popular nonbinary LDPC codes, regular (2, dc) codes and quasi-cyclic codes: each emulation model can be auto-constructed within hours and the decoder delivers excellent error-correcting performance on a Xilinx Virtex-5 FPGA with throughput of up to hundreds of Mbps.

## A Novel Low-Complexity Joint Coding and Decoding Algorithm for NB-LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(q)) 전용 joint coding/decoding 알고리즘 — 비이진 LDPC 제외 기준
- **ID**: ieee:8702165
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Suwen Song, Jing Tian, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8702165
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes exhibit a much better performance than their binary counterparts, especially for moderate codeword length and high-order modulation. However, their decoding algorithms suffer from very high computational complexity. In this paper, a low-complexity algorithm is proposed, named parity-check erased algorithm (PCEA), where an additional parity check bit is added to each symbol of the codeword when encoding and a series of simple operations are performed based on these bits during decoding. As a universal joint coding and decoding algorithm, the PCEA can be combined with arbitrary NB-LDPC encoding schemes and decoding algorithms based on message passing. The proposed algorithm facilitates significant improvement of decoding performance with a small decrease of the code rate. Additionally, it usually has an even better performance than a nearly same-rate code constructed by the original method, and requires much lower decoding complexity due to smaller size of the parity check matrix.

## Modular PUF Coding Chain with High-Speed Reed-Muller Decoder

- **Status**: ❌
- **Reason**: PUF용 Reed-Muller 디코더 HW + 보안 응용; 비-LDPC 부호이고 RM 전용 구조, LDPC 이식성 없음
- **ID**: ieee:8702484
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Holger Mandry, Andreas Herkle, Ludwig Kürzinger +4
- **PDF**: https://ieeexplore.ieee.org/document/8702484
- **Abstract**: Physical Unclonable Functions (PUFs) offer the possibility to produce unique fingerprints for integrated circuits. As raw PUF responses are affected by noise, some post-processing steps are necessary. We present a coding chain test framework for PUFs on Field Programmable Gate Arrays. The framework allows easy exchange, evaluation and comparison of different PUF implementations, coding algorithms and other chain modules. For a testing framework, the execution time of the evaluated algorithm is a bottleneck, since a huge amount of runs are supposed to be done. Hence, we additionally present a new type of Reed-Muller decoder hardware architecture using parallel modules to speed up the decoding process. The decoding time could be decreased by 95% in comparison to existing implementations at the cost of 41 times higher slice count.

## A Neural Network Aided Approach for LDPC Coded DCO-OFDM with Clipping Distortion

- **Status**: ❌
- **Reason**: VLC DCO-OFDM 클리핑 왜곡 보상용 NN 수신기(LLR 보정), LDPC는 베이스라인 디코더이고 떼어낼 ECC 기법 없음
- **ID**: ieee:8761952
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Yuan He, Ming Jiang, Xintong Ling +1
- **PDF**: https://ieeexplore.ieee.org/document/8761952
- **Abstract**: In visible light communications (VLC), a neural network-aided bit-interleaved coded modulation (NN-BICM) receiver is designed to mitigate the clipping distortion for the LDPC coded DC biased optical orthogonal frequency division multiplexing (DCO-OFDM) systems. Taking the cross-entropy as loss function, the feed forward network is trained by backprop-agation algorithm to output the condition probability through the softmax activation function, thereby assisting in a modified log-likelihood ratio (LLR) improvement. This feed-forward network simplifies the input layer with a single symbol and the corresponding Gaussian variance instead of focusing on the inter-carrier interference over multiple subcarriers. To achieve a further gain, a staked NN-BICM (S-NN-BICM) iterative receiver is proposed by calculating the condition probability with the aid of apriori probability that derived from the extrinsic LLRs in the LDPC decoder at the previous iteration. Both NN-BICM and S-NN-BICM schemes achieve significant performance gains over the existing counterparts, especially more than 0.8 and 1.4 dB in the case of 16-QAM and 511 occupied subcarriers.

## Decoding of Non-Binary LDPC Codes using the Information Bottleneck Method

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC용 information bottleneck 룩업테이블 디코딩 — 비이진 LDPC는 제외
- **ID**: ieee:8761712
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Maximilian Stark, Gerhard Bauch, Jan Lewandowsky +1
- **PDF**: https://ieeexplore.ieee.org/document/8761712
- **Abstract**: Recently, a novel lookup table based decoding method for binary low-density parity-check codes has attracted considerable attention. In this approach, mutual-information-maximizing lookup tables replace the conventional operations of the variable nodes and the check nodes in message passing decoding. Moreover, the exchanged messages are represented by integers with very small bit width. A machine learning framework termed the information bottleneck method is used to design the corresponding lookup tables. In this paper, we extend this decoding principle from binary to non-binary codes. This is not a straightforward extension but requires a more sophisticated lookup table design to cope with the arithmetic in higher order Galois fields. Provided bit error rate simulations show that our proposed scheme outperforms the log-max decoding algorithm and operates close to sum-product decoding.

## Syndrome-Generalized Belief Propagation Decoding for Quantum Memories

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) GBP 디코딩, CSS·short cycle trapping — 양자 전용 개념 의존, 원칙 제외
- **ID**: ieee:8761366
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Nithin Raveendran, Mohsen Bahrami, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/8761366
- **Abstract**: Quantum low-density parity check (QLDPC) codes are promising in realization of scalable, fault tolerant quantum memory for computation. Many of the QLDPC codes constructions suffer from unavoidable short cycles in their Tanner graph which degrade the decoding performance of the belief propagation (BP) algorithm. In this paper, we propose a syndrome based generalized belief propagation (GBP) algorithm for decoding of quantum LDPC codes and analyze how the proposed algorithm escapes from short cycle trapping sets effectively compared to the BP algorithm. Simulation results show improved decoding performance of the GBP algorithm over BP for the dual containing Calderbank, Shor and Steane (CSS) codes when cycles of length 4 are considered in the region based approach.

## LEARN Codes: Inventing Low-Latency Codes via Recurrent Neural Networks

- **Status**: ❌
- **Reason**: RNN 기반 신경망 부호(LEARN), convolutional 대체 — 신경망 디코더가 아닌 부호 설계, LDPC BP 이식 불가
- **ID**: ieee:8761286
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Yihan Jiang, Hyeji Kim, Himanshu Asnani +3
- **PDF**: https://ieeexplore.ieee.org/document/8761286
- **Abstract**: Designing channel codes under low latency constraints is one of the most demanding requirements in 5G standards. However, sharp characterizations of the performances of traditional codes are only available in the large block lengths limit. Code designs are guided by those asymptotic analyses and require large block lengths and long latency to achieve the desired error rate. Furthermore, when the codes designed for one channel (e.g. Additive White Gaussian Noise (AWGN) channel) are used for another (e.g. non-AWGN channels), heuristics are necessary to achieve any non trivial performance - thereby severely lacking in robustness as well as adaptivity. Obtained by jointly designing recurrent neural network (RNN) based encoder and decoder, we propose an end-to-end learned neural code which outperforms canonical convolutional code under block settings. With this gained experience of designing a novel neural block code, we propose a new class of codes under low latency constraint - Low-latency Efficient Adaptive Robust Neural (LEARN) codes, which outperform the state-of-the-art low latency codes as well as exhibit robustness and adaptivity properties. LEARN codes show the potential of designing new versatile and universal codes for future communications via tools of modern deep learning coupled with communication engineering insights.

## Deep Learning-Based Constellation Optimization for Physical Network Coding in Two-Way Relay Networks

- **Status**: ❌
- **Reason**: 양방향 중계 PNC용 DL 컨스텔레이션 최적화, 변복조 학습으로 LDPC ECC 디코더·구성 기여 없음
- **ID**: ieee:8761963
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Toshiki Matsumine, Toshiaki Koike-Akino, Ye Wang
- **PDF**: https://ieeexplore.ieee.org/document/8761963
- **Abstract**: This paper studies a new application of deep learning (DL) for optimizing constellations in two-way relaying with physical-layer network coding (PNC), where deep neural network (DNN)-based modulation and demodulation are employed at each terminal and relay node. We train DNNs such that the cross entropy loss is directly minimized, and thus it maximizes the likelihood, rather than considering the Euclidean distance of the constellations. The proposed scheme can be extended to higher level constellations with slight modification of the DNN structure. Simulation results demonstrate a significant performance gain in terms of the achievable sum rate over conventional relaying schemes. Furthermore, since our DNN demodulator directly outputs bit-wise probabilities, it is straightforward to concatenate with soft-decision channel decoding.

## Throughput Maximization and IR-HARQ Optimization for URLLC Traffic in 5G Systems

- **Status**: ❌
- **Reason**: URLLC IR-HARQ 처리량 최적화, 부호 비의존 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8761154
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Apostolos Avranas, Marios Kountouris, Philippe Ciblat
- **PDF**: https://ieeexplore.ieee.org/document/8761154
- **Abstract**: Emerging 5G networks will need to efficiently support ultra-reliable, low-latency communications (URLLC) services, which require extremely low latency (msec order) with very high reliability (99.999%). We consider a URLLC system with short packets and incremental redundancy hybrid automatic repeat request (IR-HARQ). We aim at maximizing the throughput by optimally tuning the IR-HARQ mechanism subject to URLLC constraints and a fixed energy budget. We propose a dynamic programming algorithm for solving the throughput maximization problem in the finite blocklength regime and assess its performance numerically.

## Asymmetric Construction of Low-Latency and Length-Flexible Polar Codes

- **Status**: ❌
- **Reason**: 비대칭 polar 부호 구성·SC 디코딩, LDPC 무관 — 비-LDPC 원칙 제외
- **ID**: ieee:8761129
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Adam Cavatassi, Thibaud Tonnellier, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/8761129
- **Abstract**: Polar codes are a class of capacity-achieving error correcting codes that have been selected for use in enhanced mobile broadband in the 3GPP 5th generation (5G) wireless standard. Most polar code research examines the original Arkan polar coding scheme, which is limited in block length to powers of two. This constraint presents a considerable obstacle since practical applications call for all code lengths to be readily available. Puncturing and shortening techniques allow for flexible polar codes, while multi-kernel polar codes produce native code lengths that are powers of two and or three. In this work, we propose a new low complexity coding scheme called asymmetric polar coding that allows for any arbitrary block length. We present details on the generator matrix, frozen set design, and decoding schedule. Our scheme offers flexible polar code lengths with decoding complexity lower than equivalent state-of-the-art length-compatible approaches under successive cancellation decoding. Further, asymmetric decoding complexity is directly dependent on the codeword length rather than the nearest valid polar code length. We compare our scheme with other length matching techniques, and simulations are presented. Results show that asymmetric polar codes present similar error correction performance to the competing schemes, while dividing the number of SC decoding operations by up to a factor of 2 using the same codeword length.

## Full-Duplex Jamming for Enhanced Hidden-Key Secrecy

- **Status**: ❌
- **Reason**: 물리계층 보안 self-jamming·concatenated coding, 보안 응용 — 원칙 제외, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8761586
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Zachary Dryer, Adam Nickerl, Marco A. C. Gomes +2
- **PDF**: https://ieeexplore.ieee.org/document/8761586
- **Abstract**: This paper presents a practical physical-layer security scheme based on coding methodologies combined with self-jamming to combat advantaged eavesdroppers, i.e., eavesdroppers that may possess an equal or even better channel than the legitimate receiver. We introduce a strengthened security gap notion, where reliability is assured by typical bit-error rate (BER) measurements, but secrecy is guaranteed by considering the entire distribution of messages upon reception, instead of average measures. Relying on this new security gap notion, we then propose a scheme that combines concatenated coding with self-jamming by the legitimate receiver for effective security and reliability even when eavesdroppers possess a channel with equal or better conditions than the legitimate receiver.

## Adaptive Physical-Layer Security Through Punctured Coding for Secrecy

- **Status**: ❌
- **Reason**: 물리계층 보안용 punctured 코딩(인터리빙/스크램블링), LDPC ECC 디코더·구성 기여 없음, 보안 도메인 제외
- **ID**: ieee:8761595
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Miguel Carreira, Thyago Monteiro, Marco Gomes +2
- **PDF**: https://ieeexplore.ieee.org/document/8761595
- **Abstract**: We propose a coding methodology for physical layer security with adaptive characteristics, whereby adaptive we mean that the system must be tunable to different operational points/signal-to-noise ratio levels of both the legitimate receiver and the eavesdropper. Based on interleaving and scrambling as techniques that shuffle the original message before transmission, we consider puncturing over an interleaving/scrambling key and/or over the message as a mechanism to provide the required adaptability to channel conditions. The proposed techniques have shown suitable adaptability to different channel quality levels of the legitimate receiver and eavesdropper, while still guaranteeing the desired reliability for the legitimate receiver and secrecy against the eavesdropper.

## Research on a TCM-based Transmission Approach for EM-MWD by Combining Phase Modulation and Convolutional Coding

- **Status**: ❌
- **Reason**: TCM(트렐리스부호변조)+컨볼루셔널 코딩 통신 응용; 비-LDPC, 이식 가능 BP 기법 없음
- **ID**: ieee:8826998
- **Type**: conference
- **Published**: 20-23 May 
- **Authors**: Cheng Zhang, Haobin Dong, Jian Ge +6
- **PDF**: https://ieeexplore.ieee.org/document/8826998
- **Abstract**: In practical applications of electromagnetic measurement while drilling (EM-MWD) in the underground coal mine, the signal-to-noise ratio (SNR) of the receiver cannot always meet the requirements of reliable communication conditions due to the earth-attenuation, interfering signal from a well site, etc. Traditional digital communication systems use independent design coding and modulation techniques to improve system performance. The coding is mainly achieved by introducing redundant bits and the improvement of error performance is at the expense of information rate. Aimed to solve this problem, we use a coding technique based on trellis coded modulation (TCM) to maximize the minimum distance between modulated output sequences and achieve significant coding gain. Simulation and experiments show that the system can improve the anti-noise performance of the system by obtaining a coding gain without reducing the transmission rate. Compared to the uncoded quadrature phase shift keying (QPSK), TCM can achieve a coding gain of at least 3 dB under the same transmitting rate. At that time, as the number of TCM system states or trace back depth increases, the coding gain is further enhanced. The TCM code modulation method can be used in an EM-MWD system to improve the system performance.

## Comparative Study of LDPC Algorithms for ATSC 3.0 Physical Layer

- **Status**: ❌
- **Reason**: ATSC 3.0 표준 LDPC에 표준 SPA/MSA/PSPA 비교만; 새 디코더 기여 없는 단순 재사용
- **ID**: ieee:8991894
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Yu-Sun Liu, Hsien-Wei Mi, Tsun-Jen Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/8991894
- **Abstract**: In this paper, we study the performance of the LDPC decoder in the ATSC 3.0 physical layer based on two kinds of likelihood estimation methods, namely, log-likelihood ratio (LLR) and maximum log-likelihood ratio (MLLR), and three decoding algorithms including sum-product algorithm (SPA), min-sum algorithm (MSA), and preferred sum-product algorithm (PSPA). The experimental results show that the performance difference between LLR and MLLR is small, but the difference between SPA and MSA is noticeable. Finally, if no numerical overflow occurs, then SPA has almost identical performance as PSPA, indicating that the overflow prevention capability of the PSPA does not degrade the decoding performance in the experiments.

## VLSI design of Parity check Code with Hamming Code for Error Detection and Correction

- **Status**: ❌
- **Reason**: 패리티체크+Hamming code VLSI, 비-LDPC 기초 블록부호
- **ID**: ieee:9065790
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Subhasri G., Radha N.
- **PDF**: https://ieeexplore.ieee.org/document/9065790
- **Abstract**: In order to get error-free data in any wireless communication systems the data has to be transmitted and received in an efficient manner. But in case of some wireless networks such as cognitive radio(CR) technology ,while performing spectrum sensing and spectrum allocation, they may cause interferences which leads to creating error in transmitted data. To overcome such problem in CR technology, the efficient data transmission needs Error Detection and Correction method. Here various error detection and correction methods are implemented based on parity check code along with hamming code algorithm. Encoder block may calculate the parity bits for data bits in various parity check code methods and also parity bits are coded with hamming codes. Whereas in decoder block, data can be regenerated after calculating syndrome vector and parity checking also takes place. Such encoder and decoder block is developed using verilog coding in Xilinx ISE software. Finally the comparison of various parity check code with hamming code is distinguished.

## A New Technique for Stochastic Division in Unipolar Format

- **Status**: ❌
- **Reason**: stochastic division 산술 아키텍처, LDPC·ECC와 무관 — 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:8741942
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Nikos Temenos, Paul P. Sotiriadis
- **PDF**: https://ieeexplore.ieee.org/document/8741942
- **Abstract**: Stochastic Computing (SC) is an alternative designing technique where signals are processed non-deterministically. Apart from low-area occupation and greatly reduced power dissipation, SC is inherently fault tolerant due to its probabilistic nature. Considering the aforementioned, SC has regained attention in system design where traditional Digital Signal Processing (DSP) cores require demanding number of resources to perform operations or are sensitive to soft-errors. However, specific operations are considered challenging for implementation due to the fact that processing elements are incapable of constructing non-linear functions such as the division. In this work we propose a new architecture that performs stochastic division in unipolar format that produces direct stochastic output and lowers the hardware requirements. Simulation results of Normalised Mean Root Squared Errors (NRMSE) are provided in order to demonstrate the accuracy of the proposed architecture as well as the simplicity for implementation.
