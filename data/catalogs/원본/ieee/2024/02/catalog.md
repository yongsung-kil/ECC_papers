# IEEE Xplore — 2024-02


## Antenna Position Estimation Based on Weighted Centroid Localization for Short-Range MIMO Transmission

- **Status**: ❌
- **Reason**: MIMO 안테나 위치추정(WCL); ECC/LDPC와 전혀 무관
- **ID**: ieee:10355756
- **Type**: journal
- **Published**: February 2
- **Authors**: Kazumitsu Sakamoto, Osamu Muta
- **PDF**: https://ieeexplore.ieee.org/document/10355756
- **Abstract**: To achieve ultrahigh-speed transmission using short-range multiple-input multiple-output (SR-MIMO) transmission, estimating the displacement of the facing transmitting (Tx) and receiving (Rx) antennas must be done with high precision, with installation in the opposite position with millimeter-order accuracy. When using the weighted centroid localization (WCL) method, which is a conventional position estimation method, the position estimation accuracy degrades as the Tx displacement and Rx antennas increase. In this letter, we propose a method to calculate the center of gravity position using the WCL method, considering the symmetry based on the Rx antenna with the largest received signal strength indicator. Additionally, computer simulation results demonstrate that the proposed method can achieve antenna position estimation with millimeter-order accuracy.

## Code-Aided Channel Estimation in LDPC-Coded MIMO Systems

- **Status**: ❌
- **Reason**: LDPC 코딩 MIMO 채널 추정 — LDPC는 채널 추정 보조, 떼어낼 디코더/HW/코드 기법 없는 무선 응용
- **ID**: ieee:10319806
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Binghui Shi, Yongpeng Wu, Peihong Yuan +3
- **PDF**: https://ieeexplore.ieee.org/document/10319806
- **Abstract**: For a multiple-input multiple-output (MIMO) system with unknown channel state information (CSI), a novel low-density parity check (LDPC)-coded transmission (LCT) scheme with joint pilot and data channel estimation is proposed. To fine-tune the CSI, a method based on the constraints introduced by the coded data from an LDPC code is designed such that the MIMO detector exploits the fine-tuned CSI. For reducing the computational burden, a coordinate ascent algorithm is employed along with several approximation methods, effectively reducing the required times of MIMO detection and computational complexity to achieve a satisfying performance. Simulation results utilizing WiMAX standard LDPC codes and quadrature phase-shift keying (QPSK) modulation demonstrate gains of up to 1.3 dB at a frame error rate (FER) of 10−4 compared to pilot-assisted transmission (PAT) over Rayleigh block-fading channels.

## Customized Joint Blind Frame Synchronization and Decoding Methods for Analog LDPC Decoder

- **Status**: ❌
- **Reason**: 블라인드 프레임 동기화+디코딩 — 동기화 기법이 본질, 아날로그 LDPC 칩은 동기화 응용 특이적이라 NAND 디코더로 이식 기법 없음
- **ID**: ieee:10296886
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Xuhui Ding, Kexin Zhou, Gaoyang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/10296886
- **Abstract**: In this study, a joint blind frame synchronization and decoding method is proposed based on the normalized syndrome satisfaction probability (NSSP) provided by the soft Low-Density Parity-Check (LDPC) codes decoder. To reduce complexity, a stopping criterion is introduced into the iterative process through the convergence of NSSP evolution patterns. In addition to achieving an excellent synchronization performance, this method also eliminates the redundancy caused by the pilot sequence. Furthermore, it is compared with the optimal pilot-based and other code-aided frame synchronization algorithms. According to analytical and simulation results, the proposed technique outperforms other advanced code-aided frame synchronization solutions in synchronization, which makes it applicable to achieve comparable performance to the pilot-based methods in specific coding gains. Due to the introduction of a novel stopping criterion, the average number of joint detection & decoding is reduced by up to 90%. Analog probability processing technology integrates sub-threshold region circuits with probability domain-based iterative message-passing algorithms inspired by high energy efficiency and low complexity. Hence, hardware implementation is presented based on the analog LDPC decoder chip as fabricated in a 0.35- $\boldsymbol \mu {m}$  CMOS technology for our proposed algorithms. The experimental results demonstrate the effectiveness of the proposed method and the realization loss is within 0.2 dB compared with the theoretical circuit simulation results.

## Optimized Non-Surjective FAIDs for 5G LDPC Codes With Learnable Quantization

- **Status**: ✅
- **Reason**: QC-LDPC용 NS-FAID 디코더를 양자화 신경망으로 LUT 최적화 + 2비트 양자화 — 이식 가능 디코더(C), 저비트 양자화는 NAND LDPC에 직접 관련
- **ID**: ieee:10352132
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Yanchen Lyu, Ming Jiang, Yifan Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10352132
- **Abstract**: This letter proposes a novel approach for designing non-surjective (NS) finite alphabet iterative decoders (FAIDs) for quasi-cyclic low-density parity-check (LDPC) codes, especially 5G LDPC codes. We employ recurrent quantized neural networks to optimize the look-up tables used in NS-FAIDs, the design of which is the kernel of FAIDs. During the optimization of LUTs, the quantized message alphabets and quantization thresholds are jointly designed. To cope with the untrainable problem of quantization thresholds in the existing neural-network-based linear FAIDs, we use softmax distribution to soften the implied one-hot distribution of quantization thresholds, making it trainable in the neural network. The proposed decoders offer enhanced universality compared to existing neural network-based linear FAIDs, making them directly applicable to 5G LDPC codes with support for 2-bit quantization over the additive white Gaussian noise channel. Additionally, they significantly outperform the original NS-FAID in terms of performance.

## Deep Learning Aided LLR Correction Improves the Performance of Iterative MIMO Receivers

- **Status**: ✅
- **Reason**: DNN 기반 LLR 보정 기법 — 신경망 디코더 보조(C)로 분류 가능, LLR 신뢰도 보정은 NAND LDPC 연판정에 이식 여지. 애매하나 in으로 살림
- **ID**: ieee:10246845
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Jue Chen, Tsang-Yi Wang, Jwo-Yuh Wu +4
- **PDF**: https://ieeexplore.ieee.org/document/10246845
- **Abstract**: A Deep Learning (DL) aided Logarithmic Likelihood Ratio (LLR) correction method is proposed for improving the performance of Multiple-Input Multiple-Output (MIMO) receivers, where it is typical to adopt reduced-complexity algorithms for avoiding the excessive complexity of optimal full-search algorithms. These sub-optimal techniques typically express the probabilities of the detected bits using LLRs that often have values that are not consistent with their true reliability, either expressing too much confidence or not enough confidence in the value of the corresponding bits, leading to performance degradation. To circumvent this problem, a Deep Neural Network (DNN) is trained for detecting and correcting both over-confident and under-confident LLRs. We demonstrate that the complexity of employing the DL-aided technique is relatively low compared to the popular reduced-complexity receiver detector techniques since it only depends on a small number of real-valued inputs. Furthermore, the proposed approach is applicable to a wild variety of iterative receivers as demonstrated in the context of an iterative detection and decoding aided MIMO system, which uses a low-complexity Smart Ordering and Candidate Adding (SOCA) scheme for MIMO detection and Low-Density Parity Check (LDPC) codes for channel coding. We adopt Extrinsic Information Transfer (EXIT) charts for quantifying the Mutual Information (MI) and show that our DL method significantly improves the BLock Error Rate (BLER). Explicitly, we demonstrate that about 0.9 dB gain can be achieved at a BLER of $10^{-3}$ by employing the proposed DL-aided LLR correction method, at the modest cost of increasing the complexity by 16% compared to a benchmarker dispensing with LLR correction.

## Shift-Sum Decoding of Non-Binary Cyclic Codes

- **Status**: ❌
- **Reason**: 비이진 cyclic codes(RS, NB-BCH) 대상 shift-sum 디코딩 — 비이진 코드라 제외 (LDPC도 아님)
- **ID**: ieee:10269061
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Jiongyue Xing, Martin Bossert, Li Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10269061
- **Abstract**: This paper proposes a novel shift-sum decoding method for non-binary cyclic codes, which only requires finite field operations but yields advanced decoding performance. Using the cyclically different minimum-weight dual codewords (MWDCs) and their proper shifts, a frequency matrix can be obtained as a reliability metric for identifying the error positions and magnitudes. By analyzing the statistical distributions of the matrix entries, the rationale for the shift-sum decoding’s advanced error-correction capability is revealed. Based on this decoding method, a hard-decision iterative shift-sum (HISS) decoding algorithm is first proposed. It can correct errors beyond half of the code’s minimum Hamming distance. By further utilizing the reliability information obtained from the channel, a soft-decision iterative shift-sum (SISS) decoding algorithm is then proposed to improve the decoding performance. Both the HISS and the SISS algorithms are realized only with polynomial multiplications and numerical comparisons, which are hardware-friendly. To further improve the error-correction performance, the HISS and SISS algorithms can be integrated in a Chase decoding mechanism for handling the test-vectors. Simulation results on Reed-Solomon (RS) and non-binary BCH (NB-BCH) codes show that the proposed algorithms yield a competent decoding and complexity performances in comparison with the existing decoding algorithms.

## Variational Inference-Based Iterative Receiver for Unified Non-Orthogonal Waveform (uNOW)

- **Status**: ❌
- **Reason**: 비직교 파형(uNOW) 변분추론 이터레이티브 수신기/등화; 통신 응용 특이적, LDPC ECC 기법 없음
- **ID**: ieee:10246433
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Nan Wu, Yikun Zhang, Haoyang Li +4
- **PDF**: https://ieeexplore.ieee.org/document/10246433
- **Abstract**: Non-orthogonal waveform has been identified as a promising spectrally efficient technology in the next generation wireless communications. In this correspondence, we develop computationally efficient iterative receivers from a unified variational inference perspective for unified non-orthogonal waveform (uNOW) signaling over multipath channels. Building on the constructed multi-layer factor graph, the parametric message passing algorithms for equalization are derived by invoking the mean field (MF) and Bethe approximation. To improve the convergence rate of the MF method, we propose its refined version with sequential message passing schedule to enhance the message updating. For Bethe approximation considering the dependence among symbols, we further propose its reduced-complexity version by exploiting Gaussian approximation. Simulation results demonstrate the benefits of the proposed variational inference-based message passing receivers conceived for uNOW signaling.

## Low-Complexity SVD Precoding for Faster-Than-Nyquist Signaling Using High-Order Modulations

- **Status**: ❌
- **Reason**: FTN 신호용 SVD 프리코딩 — LDPC는 부수 언급, 떼어낼 ECC 기법 없는 무선 응용 특이적
- **ID**: ieee:10292444
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Qiang Li, Liping Li, Yingsong Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10292444
- **Abstract**: To address the low spectrum efficiency of satellite communications, faster-than-Nyquist (FTN) signaling has proven a promising technology to improve the spectrum efficiency without requiring additional bandwidth or antennas. However, FTN signaling violates the Nyquist criterion, thereby resulting in intersymbol interference (ISI). While existing singular value decomposition (SVD) precoding can eliminate FTN-induced ISI, it ignores interblock interference, leading to low estimation accuracy. Besides, existing SVD precoding requires high complexity due to the lack of efficient and convenient implementation method. Replacing the linear convolution in FTN shaping by the circular convolution, we construct the circular FTN (CFTN) signaling and propose a CFTN-SVD precoding, which offers several advantages over the existing SVD precoding. First, the proposed CFTN-SVD precoding does not require the transmitter to acquire any accurate information about the receiver, streamlining the transmission process. Second, the proposed CFTN-SVD precoding is designed with low implementation complexity, leveraging fast Fourier transform (FFT) and inverse FFT (IFFT) to facilitate the practical implementation. Last but not least, the proposed CFTN-SVD precoding takes all FTN-induced ISI into consideration, resulting in improved estimation accuracy and making it suitable for high-order modulations. Simulation results show that compared with the bit error rate (BER) of Nyquist signaling, the BER loss of the proposed CFTN-SVD precoding is about 0.8 and 0.25 dB for uncoded and coded FTN signaling, respectively, when adopting 256-amplitude phase shift keying.

## Reed-Solomon Coded Probabilistic Constellation Shaping for Molecular Communications

- **Status**: ❌
- **Reason**: 분자 통신용 RS 코딩+성상 셰이핑 — 비이진 RS 코드, LDPC 무관, 응용 특이적
- **ID**: ieee:10356127
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Yuankun Tang, Fei Ji, Qianqian Wang +3
- **PDF**: https://ieeexplore.ieee.org/document/10356127
- **Abstract**: Probabilistic constellation shaping (PCS) is a promising technique employed in molecular communications, utilizing molecular shell mapping (MSM). However, the performance of MSM, particularly its bit error rate (BER), falls short when the exact channel state information is unavailable. To address this challenge and enhance robustness, we propose a scheme known as Reed-Solomon coded PCS (RS-PCS) scheme. This approach combines shaping and coding through a parallel transmitter structure, preserving the shaped distribution at the output of the RS encoder. In addition, we develop a low-complexity receiver that leverages the intra-sequence interference. Our numerical results on BER clearly demonstrate that the proposed RS-PCS scheme outperforms existing schemes that only consider the PCS or RS coding techniques alone.

## Generalized Channel Coding and Decoding With Natural Redundancy in Protocols

- **Status**: ❌
- **Reason**: 프로토콜 자연 잉여 활용 결합 디코딩(JPCD) — LDPC가 베이스라인, 프로토콜 계층 잉여 활용으로 NAND ECC에 떼어낼 기법 없음
- **ID**: ieee:10303283
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Yongbin Li, Hongyi Yu, Xia Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10303283
- **Abstract**: Mainstream wireless communication networks mostly adopt the layered protocol encapsulation mechanism, which inevitably introduces natural redundancy into protocols. To fully exploit the abundant natural redundancy in protocols (NRP), this paper provides a novel cross-frame and cross-layer perspective for channel coding and decoding (CCD). First, a generalized CCD architecture is developed for the first time to describe the NRP and artificial redundancy in channel codes (ARC) uniformly. The concept of equivalent code rate is proposed correspondingly to evaluate the potential gain of NRP. Second, we summarize the types of NRP, and for each of them, factor graphs and sum-product algorithms (SPAs) are adopted to model and solve the correlation between it and ARC. On this basis, the joint decoding of multi-class NRP and ARC is further considered, and a general SPA-based joint protocol-channel decoding (JPCD) scheme is presented. Finally, tests on the 802.11n TCP/IP/MAC protocol stack demonstrate that the JPCD scheme can significantly improve the decoding performance of both the packet header and payload with a relatively small computational cost. Our work shows great promise in reducing error retransmission, bandwidth overhead, and the difficulty of source recovery.

## An Efficient Approximate EP-Based Iterative Detection and Decoding for Massive MIMO

- **Status**: ❌
- **Reason**: Massive MIMO용 EP 기반 IDD 검파-복호; LDPC는 coded 시스템 베이스라인, 검파기 기법이라 NAND LDPC 디코더로 이식할 부호/디코더 기여 없음
- **ID**: ieee:10234642
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Xiaosi Tan, Weiping Li, Zaichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10234642
- **Abstract**: In this letter, an efficient approximate expectation propagation (EPA) based iterative detection and decoding (IDD) scheme named EPA-IDD is first proposed for LDPC-coded massive MIMO systems. EPA is applied in IDD to bypass the variance updates in the inner loops, which reduces matrix inversions, simplifies extrinsic messages, and effectively enhance the convergence performance of IDD. In addition, a partial resetting scheme is proposed to efficiently adopt the decoder output into the EPA detector. A Neumann series based approximation called wNSA-EPA-IDD is further developed to reduce complexity. Numerical results show that the proposed EPA-IDD schemes outperform the state-of-the-art (SOA) double EP (DEP) in various LDPC-coded MIMO scenarios. Complexity analysis is presented to validate the improved efficiency of the proposed algorithms.

## An Improved Adaptive Coding and Modulation Scheme With Hybrid Switching Standard for UAV-to-Ground Free Space Optical Communication

- **Status**: ❌
- **Reason**: UAV FSO용 적응 코딩변조 — LDPC FER 기반 스위칭만 부수 언급, 무선 응용 특이적
- **ID**: ieee:10308596
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Qianwu Zhang, Boyang Liu, Guanwen Chen +6
- **PDF**: https://ieeexplore.ieee.org/document/10308596
- **Abstract**: In this paper, an improved adaptive coding and modulation scheme with hybrid switching standard is proposed for UAV-to-Ground free space optical (FSO) communication to mitigate the degradation of turbulence intensity variation. In order to improve bits efficiency in different turbulence, a channel estimator based on Gated Recurrent Unit (GRU) and a hybrid switching standard based on frame error rate (FER) of LDPC decoding are applied. Simulation results show that the GRU estimator achieves approximately 34.9% improvement in training time compared to the LSTM estimator, without degradation in system performance. Moreover, the hybrid switching standard significantly improves the signal-to-noise ratio (SNR) switching threshold deviation of the ACM scheme from 1.8 dB and 4 dB, which were observed in moderate turbulence conditions, to an average of 0.35 dB. This improvement allows for the effective implementation of the ACM scheme in different turbulence intensities at a relatively small cost, thereby enhancing the communication quality of FSO systems in atmospheric channels characterized by turbulent variations.

## Research and Analysis of CRC Checksum Algorithm Based on FPGA

- **Status**: ❌
- **Reason**: CRC 체크섬 FPGA 구현 — LDPC 아니고 오류검출 알고리즘, NAND LDPC ECC와 무관
- **ID**: ieee:10612854
- **Type**: conference
- **Published**: 24-26 Feb.
- **Authors**: Haobo Yin
- **PDF**: https://ieeexplore.ieee.org/document/10612854
- **Abstract**: The term Cyclic Redundancy Check (CRC) refers to a type of checksum algorithm used in data communication protocols to detect errors in data transmission. CRC check code can be generated and added to the transmitted message, allowing the receiver to verify the integrity of the data. This technique has become widely used in digital communication systems and networks to ensure the accuracy and reliability of data transmission. The CRC8 encoder is a digital circuit that performs error detection during data transmission. A simulation was conducted to verify its functionality, comparing output data with expected values. The results confirmed the circuit's effectiveness in accurately detecting errors and generating CRC8 values. It plays a vital role in ensuring data integrity. In conclusion, CRC is a widely used error detection algorithm with strengths and limitations in data transmission and storage systems. Ongoing research aims to enhance its efficiency and accuracy for more reliable data integrity.

## Communication Synchronization and Anti-Interference Technology based on Artificial Intelligence

- **Status**: ❌
- **Reason**: CNN 기반 통신 동기/항간섭, LDPC ECC와 무관 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:10499063
- **Type**: conference
- **Published**: 23-24 Feb.
- **Authors**: Yongdong Li
- **PDF**: https://ieeexplore.ieee.org/document/10499063
- **Abstract**: With the development of the Internet of Things and the Industrial Internet, more and more devices require stable and reliable wireless connections. When traditional communication synchronization methods encounter complex electromagnetic environments with various interferences and noises, their performance will be limited and they will be difficult to adapt to and accurately process signal characteristics. Therefore, this article introduces the convolutional neural network algorithm based on artificial intelligence for optimization and improvement. This article focuses on exploring the methods of using CNN for signal feature extraction, and proposes the design and optimization of adaptive filters and anti-interference encoding and decoding techniques. Finally, through two sets of simulation experiments, the following conclusions were drawn: compared with traditional methods, the overall average improvement in synchronization accuracy index of CNN is 8.3%, while the signal error rate index is comprehensively reduced by 17.35%. This end-to-end learning and optimization strategy makes CNN signal recovery more effective in complex environments and improves the overall performance and reliability of communication systems.

## Performance Analysis of LDPC Coded Outdoor Long-Distance Imaging MIMO System

- **Status**: ✅
- **Reason**: 빔별 BER 고려 LDPC 디코딩 방법 제안 — LLR/신뢰도 채널통계 반영 디코더 기법 이식 가능(C)
- **ID**: ieee:10556090
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Daiki Ishikawa, Chedlia Ben Naila, Hiraku Okada +1
- **PDF**: https://ieeexplore.ieee.org/document/10556090
- **Abstract**: In this work, the performance of light-emitting diode-based (LED-based) imaging Multiple Input Multiple Output (MIMO) system for long-distance outdoor transmission is evaluated, and based on the results, a proposal for improving the performances is presented. We first conducted outdoor communication experiments, and error-free transmission of 200 Mbps over 100 m was achieved without using Forward Error Correction or other error control schemes. Nonetheless, communication errors occurred at distances shorter than 100 m. Furthermore, the bit error rate (BER) differed for each beam from each transmitting LED. Therefore, we introduced Low-density Parity-check (LDPC) codes along with a decoding method that takes into account the BER of each signal beam. The effectiveness of this decoding method is predicated on the time-invariance of the BER, which we have separately confirmed through experimental data. We assume that encoded bit errors for each signal beam would follow the BER observed in our non-encoded communication experiments. Under this assumption, we assessed various LDPC codes with different code lengths and coding rates. Our results demonstrated an improvement in BER performance.

## Comparisons of TDM and FDM Pilot Signals for Phase Noise Estimation with High-Order QAM for DFT-Spread OFDM

- **Status**: ❌
- **Reason**: OFDM 위상잡음 추정용 파일럿 멀티플렉싱 비교; LDPC는 코드율 베이스라인 언급에 불과
- **ID**: ieee:10556069
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Ryota Kuribayashi, Mamoru Sawahashi
- **PDF**: https://ieeexplore.ieee.org/document/10556069
- **Abstract**: This paper presents comparisons of time division multiplexing (TDM) and frequency division multiplexing (FDM) based pilot signal multiplexing methods for estimating the time-varying phase noise (PN) in a high-order QAM scheme for discrete Fourier transform (DFT)-spread orthogonal frequency division multiplexing (DFT-S-OFDM). Computer simulation results show that the peak-to-average power ratio at the complementary cumulative distribution function of 10−4 of DFT-S-OFDM with FDM pilot multiplexing is increased by approximately 1.8 dB and 1.2 dB compared to that for DFT-S-OFDM with a TDM based pilot signal and that for DFT-S-OFDM without a pilot signal, respectively, for 256QAM. We also show that the required received signal-to-noise ratio (SNR) satisfying the bit error rate (BER) of 10−8 for the TDM based pilot signal is decreased by approximately 1.1 dB, 1.2 dB, and 1.3 dB compared to that with the FDM based pilot signal for the low-density parity-check (LDPC) coding rate of 1/2, 3/4, and 8/9, respectively, for 256QAM assuming the same frequency bandwidth. Hence, we show that the TDM based pilot signal for PN estimation achieves superior performance to that for the FDM based pilot signal although FDM based pilot multiplexing has the potential for improvement by using elaborate cancellation of single-carrier distortion.

## An Efficient PLS Scheme for Coded MIMO Systems Under Imperfect Channel Estimation

- **Status**: ❌
- **Reason**: PLS 채널의존 인터리빙·MIMO 보안 스킴; LDPC 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:10556020
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Thara Son, Sooyoung Kim
- **PDF**: https://ieeexplore.ieee.org/document/10556020
- **Abstract**: In recent years, the concept of physical layer security (PLS) has emerged as a promising approach to supplement tra-ditional cryptographic solutions. However, many PLS techniques rely on accurate knowledge of the channel state information (CSI) at the transmitter, which can be difficult to obtain in real-world scenarios. This paper presents a physical layer security scheme designed to enhance the security of a coded multi-input multi-output (MIMO) system operating under imperfect channel estimation conditions. To achieve a high level of security, we adopt a strategy that involves a channel-dependent interleaving scheme for the coded MIMO system, and combined additional simple coding schemes to prevent serious performance degradation caused by CSI error. Simulation results presented in this paper demonstrate that the proposed scheme effectively protects the transmitted data without any information leakage to the eavesdronner.

## Quad Ways for Polar Coded HARQ

- **Status**: ❌
- **Reason**: Polar 코드 HARQ-CC LLR 기법 — LDPC 아니고 polar 전용, 이식할 LDPC 디코더 기여 없음
- **ID**: ieee:10473255
- **Type**: conference
- **Published**: 19-20 Feb.
- **Authors**: Syeda Aamna Rubab, Nargis Bibi
- **PDF**: https://ieeexplore.ieee.org/document/10473255
- **Abstract**: Hybrid automatic repeat request provide wireless reliability while preserving significant efficiency in transmission, which is important for battery-operated low complexity applications such as IoT. The hybrid automatic repeat request system using polar codes as FEC, in combination with chase combining is simple to create. However, the HARQ-CC mechanisms often encounter challenges related to error rates and throughput performance. To improve error performance and reduce retransmissions, we developed four alternative HARQ-CC techniques. We utilize valuable information contained in received signals by introducing four LLR sequences to aid the decoder. The simulation results illustrate that the proposed techniques for creating new LLR’s provide superior error performance and increased throughput efficiency while necessitating fewer retransmissions than simple HARQ-CC schemes.
