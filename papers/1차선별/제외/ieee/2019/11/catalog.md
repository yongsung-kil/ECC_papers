# IEEE Xplore — 2019-11


## Near-Capacity Detection and Decoding: Code Design for Dynamic User Loads in Gaussian Multiple Access Channels

- **Status**: ❌
- **Reason**: GMAC NOMA용 LDPC+반복부호 직렬연접 EXIT 최적화 — 무선 다중접속 응용 특이적, 표준 LDPC를 베이스라인으로 사용, 떼어낼 NAND 이식 기법 없음
- **ID**: ieee:8804231
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Xiaojie Wang, Sebastian Cammerer, Stephan Ten Brink
- **PDF**: https://ieeexplore.ieee.org/document/8804231
- **Abstract**: This paper considers the forward error correction (FEC) code design for approaching the capacity of a dynamic multiple access channel (MAC) where both the number of users and their respective signal powers keep constantly changing, resembling the scenario of an actual wireless cellular system. To obtain a low-complexity non-orthogonal multiple access (NOMA) scheme, we propose a serial concatenation of a low-density parity-check (LDPC) code and a repetition code (REP), this way achieving near Gaussian MAC (GMAC) capacity performance while coping with the dynamics of the MAC system. The joint optimization of the LDPC and REP codes is addressed by matching the analytical extrinsic information transfer (EXIT) functions of the sub-optimal multi-user detector (MUD) and the channel code for a specific and static MAC system, achieving near-GMAC capacity. We show that the near-capacity performance can be flexibly maintained with the same LDPC code regardless of the variations in the number of users and power levels. This flexibility (or elasticity) is provided by the REP code, acting as “user-load and power equalizer”, dramatically simplifying the practical implementation of NOMA schemes, as only a single LDPC code is needed to cope with the dynamics of the MAC system.

## Cross-Packet Coding for Delay-Constrained Streaming Applications

- **Status**: ❌
- **Reason**: 지연제약 스트리밍용 cross-packet 코딩 — 채널 ECC 디코더 기법 아님, LDPC 이식 기여 없음
- **ID**: ieee:8794566
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Giuseppe Cocco, Dario Floreano
- **PDF**: https://ieeexplore.ieee.org/document/8794566
- **Abstract**: Delay-constrained streaming from a moving platform is of paramount importance for applications such as the remote control of drones, where a low-delay video stream is required in order to provide visual feedback to the pilot while providing high quality video at playback. In this letter we propose a scheme based on cross-packet coding for delay-constrained streaming over block fading channels with channel state information at the receiver only. The proposed scheme largely enhances upon a memoryless transmission approach in terms of average decoded rate and provides increased protection to packets transmitted earlier within a block, which is useful for successively compressed sources such as IPPPP video streams. The proposed scheme approaches the asymptotic upper bound over a wide range of SNR already for blocks with size of practical relevance and has a comparatively low complexity.

## Successive Wyner-Ziv Coding for the Binary CEO Problem Under Logarithmic Loss

- **Status**: ❌
- **Reason**: binary CEO/Wyner-Ziv 소스코딩(LDGM 양자화+LDPC 신드롬) — 채널 ECC가 아닌 소스/분산코딩
- **ID**: ieee:8815929
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Mahdi Nangir, Reza Asvadi, Jun Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/8815929
- **Abstract**: The  $L$ -link binary Chief Executive Officer (CEO) problem under logarithmic loss is investigated in this paper. A quantization splitting technique is applied to convert the problem under consideration to a  $(2L-1)$ -step successive Wyner-Ziv (WZ) problem, for which a practical coding scheme is proposed. In the proposed scheme, Low-Density Generator-Matrix (LDGM) codes are used for binary quantization while Low-Density Parity-Check (LDPC) codes are used for syndrome generation; the decoder performs successive decoding based on the received syndromes and produces a soft reconstruction of the remote source. The simulation results indicate that the rate-distortion performance of the proposed scheme can approach the theoretical inner bound based on binary-symmetric test-channel models.

## Enhanced Machine Learning Techniques for Early HARQ Feedback Prediction in 5G

- **Status**: ❌
- **Reason**: 5G E-HARQ 디코딩 결과를 ML로 조기 예측하는 통신 응용 — 떼어낼 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:8792202
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Nils Strodthoff, Barış Göktepe, Thomas Schierl +2
- **PDF**: https://ieeexplore.ieee.org/document/8792202
- **Abstract**: We investigate Early Hybrid Automatic Repeat reQuest (E-HARQ) feedback schemes enhanced by machine learning techniques as a path towards ultra-reliable and low-latency communication (URLLC). To this end, we propose machine learning methods to predict the outcome of the decoding process ahead of the end of the transmission. We discuss different input features and classification algorithms ranging from traditional methods to newly developed supervised autoencoders. These methods are evaluated based on their prospects of complying with the URLLC requirements of effective block error rates below 10-5 at small latency overheads. We provide realistic performance estimates in a system model incorporating scheduling effects to demonstrate the feasibility of E-HARQ across different signal-to-noise ratios, subcode lengths, channel conditions and system loads, and show the benefit over regular HARQ and existing E-HARQ schemes without machine learning.

## Spiral Constellations for Phase Noise Channels

- **Status**: ❌
- **Reason**: 위상잡음 채널용 나선형 성상도/검출기 설계 — LDPC ECC 무관, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:8811626
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Alessandro Ugolini, Amina Piemontese, Thomas Eriksson
- **PDF**: https://ieeexplore.ieee.org/document/8811626
- **Abstract**: In this paper, we consider the design of spiral constellations for channels affected by phase noise. The strength of the proposed constellations resides both on the performance and on the extreme simplicity of the design. The symbols can in fact be expressed in analytical form, and are uniquely defined through a single parameter that accounts for the phase and thermal noise variances. The structure of the proposed constellations allows to easily determine the points that are closest to any point in the complex plane, therefore we also propose a low complexity detector that is suitable for phase noise channels in medium-high signal-to-noise ratio conditions. The performance of the proposed constellations are assessed in terms of information rate and error rate. Despite their simplicity, the new spiral constellations have excellent performance, especially when the constellation size grows large.

## Shaped On–Off Keying Using Polar Codes

- **Status**: ❌
- **Reason**: polar 부호 확률 셰이핑(OOK 신호)으로 비-LDPC, LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:8770064
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Thomas Wiegart, Fabian Steiner, Patrick Schulte +1
- **PDF**: https://ieeexplore.ieee.org/document/8770064
- **Abstract**: The probabilistic shaping scheme by Honda and Yamamoto (2013) for polar codes is used to enable power-efficient signaling for on-off keying (OOK). As OOK has a non-symmetric optimal input distribution, shaping approaches that are based on the concatenation of a distribution matcher followed by systematic encoding do not result in optimal signaling. Instead, these approaches represent a time-sharing scheme, where only a fraction of the codeword symbols is shaped. The proposed scheme uses a polar code for joint distribution matching and forward error correction which enables asymptotically optimal signaling. Numerical simulations show a gain of 1.8 dB compared to uniform transmission at a spectral efficiency of 0.25 bits/channel use for a blocklength of 65 536 bits.

## On Channel Quantization for Spin-Torque Transfer Magnetic Random Access Memory

- **Status**: ❌
- **Reason**: STT-MRAM 채널 양자화이나 polar code 전용 SC 디코더 대상 — 비-LDPC, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8821377
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Zhen Mei, Kui Cai, Long Shi +1
- **PDF**: https://ieeexplore.ieee.org/document/8821377
- **Abstract**: As emerging memories such as spin-torque transfer magnetic random access memory (STT-MRAM) suffer from reliability issues caused by process variations and thermal fluctuations, the design of channel quantizer with the minimum number of quantization bits is critical to support effective error correction coding for ensuring high-density and high-speed memory data storage. In this paper, we first propose a quantized channel model for STT-MRAM. Based on the quantized channel model, we derive various information theoretic bounds, including the mutual information, cutoff rate, and the Polyanskiy-Poor-Verdú (PPV) finite-length performance bound. By using these bounds as design criteria, we optimize the quantizer design for the polar-coded STT-MRAM channel. Moreover, we also propose a polar-code-specific quantization design with the successive cancellation decoding algorithm, by using the block error probability bound obtained from density evolution (DE). Simulation results show that all our proposed quantizers generally outperform the prior art greedy merging quantizer. In addition, both the cutoff rate and PPV bound based quantizers outperform the most widely applied mutual information based quantizer for short-length polar codes with 2-bit quantization. Furthermore, the DE quantizer designed specifically for polar codes achieves the best performance among all the proposed quantizers.

## Polylog-LDPC Capacity Achieving Codes for the Noisy Quantum Erasure Channel

- **Status**: ❌
- **Reason**: 양자 스태빌라이저 부호의 erasure 채널 용량 도달 이론 — 양자 전용 개념 의존, 고전 바이너리 LDPC로 이식할 디코더/구성 기여 없음
- **ID**: ieee:8746813
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Seth Lloyd, Peter Shor, Kevin Thompson
- **PDF**: https://ieeexplore.ieee.org/document/8746813
- **Abstract**: We provide polylog sparse quantum codes for correcting the Erasure channel arbitrarily close to the capacity. Specifically, we provide the [[n, k, d]] quantum stabilizer codes that correct for the erasure channel arbitrarily close to the capacity if the erasure probability is at least 0.33 and with a generating set (S1, S2, ... Sn-k) such that |Si| ≤ log2+ζ(n) for all i and for any ζ > 0 with high probability. In this paper, we show that the result of Delfosse et al. is tight: one can construct capacity approaching codes with weight almost O(1).

## High-Efficient Adaptive Modulation for PWM-Based Multi-Level Perpendicular Magnetic Recording on Insufficient Resolution Channel

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC over GF(32) 기반 자기기록 변조 기법 — 비이진 LDPC 제외 대상
- **ID**: ieee:8784414
- **Type**: journal
- **Published**: Nov. 2019
- **Authors**: Kohsuke Harada
- **PDF**: https://ieeexplore.ieee.org/document/8784414
- **Abstract**: In this paper, we propose a high-efficient constrained adaptive 5-binary to 4-ternary (5B4T)-modulation in pulsewidth modulation (PWM)-based ternary perpendicular magnetic recording (PMR). The high-efficient modulation is required to obtain higher user-bit density (UBD) gain in low-resolution channel, in which transition interval and magnetic-grain size are equivalent on media. In our proposed constrained adaptive 5B4T-modulation, one mapping-set is adaptively selected from the prepared two different mapping-sets to satisfy a specific constraint of ternary signal in modulation block-by-block. For the signal detection in the proposed modulation, we provide a practical solution which is a blind-detection method on likelihood vector. The likelihood vector is re-calculated as joint-metric using the likelihood values of adjacent modulation blocks. By using the vector of joint-metric, a likelihood vector is further generated to decode non-binary low-density parity-check (NB-LDPC) codes. Our simulation results demonstrate that the proposed adaptive 5B4T-modulated PWM-based ternary-PMR, combined with NB-LDPC codes over GF(32), shows a significant robustness in ultra-low-resolution channel, which occurs magnetization-missing frequently.

## Performance Analysis of QC-LDPC and Polar Codes for eMBB in 5G Systems

- **Status**: ❌
- **Reason**: 5G eMBB용 표준 QC-LDPC와 polar 코드의 BLER 성능 비교만, 새 디코더/구성/HW 기여 없음 (표준 부호 단순 비교)
- **ID**: ieee:8980142
- **Type**: conference
- **Published**: 8-10 Nov. 
- **Authors**: K. Deergha Rao, T.Aravinda Babu
- **PDF**: https://ieeexplore.ieee.org/document/8980142
- **Abstract**: For 5G enhanced mobile broad band (eMBB) services, 3GPP has selected Quasi Cyclic LDPC (QC-LDPC) and Polar codes for data and control channel coding respectively. The data channel requirements in respect to message block lengths and channel code rates are different from the control channel requirements. The error correction performance degrades with decreased message lengths. Further, So far designed polar codes are SNR dependent. Hence, this paper considers polar codes designed based on method independent of SNR and performance evaluation of the QPSK modulated QC-LDPC codes and polar codes for 5G eMBB service over AWGN is carried out using block error rate (BLER) as the performance measures.

## Protograph LPDC Coded Large-Scale MIMO Communications with Low-Resolution ADCs

- **Status**: ❌
- **Reason**: LS-MIMO 저해상도 ADC 결합 검출/디코딩 수신기로 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9026536
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Hieu D. Vu, Thuy V. Nguyen, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9026536
- **Abstract**: In this paper, we develop a new algorithm of joint detection and decoding receiver for the large-scale multiple-input multiple-out (LS-MIMO) coded communication systems with low-resolution ADCs. The new algorithm enables us to perform extensive experiments to address the performance and complexity tradeoff issue for LS-MIMO communication systems. Our study results indicate that 4-bit ADC is the best choice to achieve an excellent balance between the transmit power and complexity. Furthermore, the experiments reveal that the LS-MIMO system with 4-bit ADC can approach the performance of the high-resolution LS-MIMO system in the entire range of signal to noise ratio. In the other extreme, the LS-MIMO system with 2-bit ADC suffers 2.2 dB performance loss in terms of transmit power at bit error rate (BER) 10-6. In all test cases, an extra bit to increase the resolution from 4-bit ADC to 5-bit ADC achieves a tiny fraction of power gain in return.

## Efficient Information Reconciliation for Energy-Time Entanglement Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD 정보조정용 그래프코딩 — 채널 ECC 아닌 reconciliation, 비이진 변조 결합, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:9048898
- **Type**: conference
- **Published**: 3-6 Nov. 2
- **Authors**: Siyi Yang, Murat Can Sarihan, Kai-Chi Chang +2
- **PDF**: https://ieeexplore.ieee.org/document/9048898
- **Abstract**: Graph based codes such as low density parity check (LDPC) codes have been shown promising for the information reconciliation phase in quantum key distribution (QKD). However, existing graph coding schemes have not fully utilized the properties of the QKD channel. In this work, we first investigate the channel statistics for discrete variable (DV) QKD based on energy-time entangled photons. We then establish a so-called balanced modulation scheme that is promising for this channel. Based on the modulation, we propose a joint local-global graph coding scheme that is expected to achieve good error-correction performance.

## Variational Bayesian Inference based Soft-Symbol Decoding for Uplink Massive MIMO Systems with Low Resolution ADCs

- **Status**: ❌
- **Reason**: 무선 MIMO 소프트심볼 검출(변분베이즈) 논문 — 채널검출이지 LDPC 디코더/구성/HW 기여 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:9048750
- **Type**: conference
- **Published**: 3-6 Nov. 2
- **Authors**: Sai Subramanyam Thoota, Chandra R. Murthy
- **PDF**: https://ieeexplore.ieee.org/document/9048750
- **Abstract**: In this paper, we present an algorithm to obtain the posterior beliefs of the transmitted bits in an uplink coded massive multiple-input-multiple-output (MIMO) wireless communication system with low resolution analog-to-digital-converters (ADC) at the base station (BS). The nonlinearities introduced by low resolution ADCs necessitates a new multiuser detection approach, for which propose a variational Bayes' inference framework. Further, in coded communications, it is more important to obtain soft symbol estimates for the data bits, rather than hard decisions on the data symbols. We approximate the exact posterior distribution with a fully factorized distribution used in mean field theory in statistical physics, and find its parameters such that the evidence lower bound (ELBO) is maximized. These parameters are used to obtain the posterior beliefs of the transmitted bits in an iterative manner. The resulting algorithm, named the quantized variational Bayesian soft symbol decoding (QVBSSD) is computationally inexpensive and easy to implement. The output posterior beliefs are input to a soft-input-hard-output channel decoder, which gives the decoded bits. We empirically illustrate the bit error rate (BER) of the QVBSSD algorithm, and show its superiority compared to the unquantized MMSE based detection..

## Redundancy-Aided Iterative Reliability-Based Majority-Logic Decoding for NB-LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 디코더 — 바이너리 한정 기준에 따라 제외
- **ID**: ieee:8983490
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Suwen Song, Jing Tian, Jun Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8983490
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes tend to exhibit much better performance than their binary counterparts while suffering from very high computational complexity. As a type of hard-decision NB-LDPC decoding algorithm, the iterative reliability-based majority-logic decoding (IRB-MLGD) algorithms are attractive for their low computation complexity, coming with obvious performance degradation. Aiming at improving the error-correction performance, in this paper, we introduce few redundant bits to the original NB-LDPC encoding and the corresponding checksum operations to the improved iterative soft reliability-based (IISRB)-MLGD. Based on the joint coding and decoding method, the obtained redundancy-aided (RA)-IISRB decoding algorithm shows significant performance improvement while maintaining the low-complexity property. Simulation results demonstrate that the proposed algorithm can achieve a more than 1.0dB extra coding gain over the original IISRB with a slight decrease of code rate.

## Carrier phase recovery for DVB-S2x standard in VL SNR channel

- **Status**: ❌
- **Reason**: DVB-S2x 반송파 위상 동기, ECC 무관 동기화 기법
- **ID**: ieee:9384472
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Pansoo Kim, Joon-Gyu Ryu
- **PDF**: https://ieeexplore.ieee.org/document/9384472
- **Abstract**: In this paper, we come up with a robust carrier phase synchronization scheme in DVB-S2x Annex E SF mode format 2 for VL SNR channel. Unlike DVB-S2 standard, DVB-S2x standard can support VL SNR condition by around — 10 dB which is useful for low profile antenna and heavy rain channel condition. The proposed scheme is applicable to reduce the FER performance degradation which is caused by inaccurate estimation. By means of computer simulations, we can show that there were practically much closer approaches over the ideal AWGN channel for the proposed scheme in terms of FER performance.

## DFT-Spread Spectrally Efficient Non-Orthogonal FDMA: Invited Paper

- **Status**: ❌
- **Reason**: SC-SEFDMA 비직교 파형 통신 기법, LDPC 무관
- **ID**: ieee:8942535
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Tongyang Xu, Izzat Darwazeh
- **PDF**: https://ieeexplore.ieee.org/document/8942535
- **Abstract**: Single carrier frequency division multiple access (SC-FDMA) has been comprehensively investigated and standardized in 4th generation (4G) and 5th generation (5G) mobile systems. Its significant advantage is low peak-to-average power ratio (PAPR), which makes it suitable for uplink channel communications. However, over a long time period, SC-FDMA has not made breakthrough especially in data rate enhancement, which may not catch up with the next generation evolution in communications. This work proposes to use a non-orthogonal waveform in SC-FDMA to promote a new concept, termed single carrier spectrally efficient frequency division multiple access (SC-SEFDMA). This non-orthogonal single carrier access technique maintains essentially similar complexity as SC-FDMA but advantageously can either achieve higher data rate for the same amount of power consumption or the same data rate with less power consumption.

## On decoding strategies for satellite uplink asynchronous random access channels

- **Status**: ❌
- **Reason**: 위성 비동기 랜덤액세스 디코딩 전략, 떼어낼 LDPC 기법 없음
- **ID**: ieee:9384417
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Farbod Kayhan, Nader Alagha
- **PDF**: https://ieeexplore.ieee.org/document/9384417
- **Abstract**: In this chapter, we first review the state-of-the-art schemes for nonorthogonal multiple access where multiple users share the satellite channel radio resources. Among different grant-based and grant-free access schemes, we focus on nonslotted techniques, we study some decoding strategies to improve the performance of asynchronous contention resolution diversity ALOHA. Our preliminary results show that the performance of the decoder can be improved significantly if the information on overlapping bursts' powers and the exact differential delay among the incoming bursts are known at the receiver. We present the simulation results for a simple model and discuss the possible generalizations to a more realistic system scenario. Finally, we shortly discuss the efficiency of the physical layer abstraction methods under our model assumptions.

## Hardware precoding demonstration in multibeam UHTS communications under realistic payload characteristics

- **Status**: ❌
- **Reason**: 멀티빔 위성 프리코딩 HW 테스트베드, LDPC는 단순 측정용
- **ID**: ieee:9384476
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Juan Duncan, Jorge Querol, Nicola Maturo +6
- **PDF**: https://ieeexplore.ieee.org/document/9384476
- **Abstract**: In this chapter, we present a new hardware test-bed to demonstrate closed-loop precoded communications for interference mitigation in multibeam ultrahigh throughput satellite systems under realistic payload and channel impairments. We build the test-bed to demonstrate a real-time channel aided precoded transmission under realistic conditions such as the power constraints and satellite- payload nonlinearities. We develop a scalable architecture of an SDR platform with the DVB-S2X piloting. The SDR platform consists of two parts: analog-to-digital (ADC) and digital-to-analog (DAC) converters preceded by radio frequency (RF) front end and field-programmable gate array (FPGA) backend. The former introduces realistic impairments in the transmission chain such as carrier frequency and phase misalignments, quantization noise of multichannel ADC and DAC, and nonlinearities of RF components. It allows evaluating the performance of the precoded transmission in a more realistic environment rather than using only numerical simulations. We benchmark the performance of the communication standard in realistic channel scenarios, evaluate received signal SNR, and measure the actual channel throughput using LDPC codes.

## The LDPC Code and Rateless Code for Wireless Sensor Network

- **Status**: ❌
- **Reason**: WSN에서 표준 LDPC/Rateless 부호 성능 비교만; 새 디코더·구성·HW 기여 없음
- **ID**: ieee:9095935
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Haiyan Wang
- **PDF**: https://ieeexplore.ieee.org/document/9095935
- **Abstract**: This paper gives a concept of wireless sensor network and describe the encoding algorithm and decoding algorithm along with the implementation of LDPC code and Rateless code. Compare the performances of those two code in WSN environment by making simulation in a Rayleigh channel in matlab and derive results and conclusions from the simulation.

## A Simplified Code-aided Carrier Synchronization Algorithm

- **Status**: ❌
- **Reason**: 코드보조 반송파 동기화 알고리즘(통신 응용 특이적); 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:9095976
- **Type**: conference
- **Published**: 28-30 Nov.
- **Authors**: Meng Zhengke, Zhang Haoliang, Wang Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/9095976
- **Abstract**: The code-aided synchronization technology can realize the estimation of carrier synchronization parameters with low signal to noise ratio when using the soft information output during decoding. However, the computational complexity based on the Expectation Maximization (EM) algorithm is very high. It proposes a new algorithm that divides the frequency offset search interval, adopts the coarse search and the fine search together, and uses different step sizes to reduce the complexity of the algorithm in the two searches. The simulation results show that compared with the original EM algorithm, the algorithm can reduce the computational complexity of the original EM algorithm without losing performance.

## Analysis and Design of LDPC Codes for FTN Signaling with Finite Number of Turbo Iterations

- **Status**: ❌
- **Reason**: FTN signaling용 LDPC 코드 설계 분석(EXIT/AIR bound), 무선 turbo equalization 응용 특이적이며 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:8971243
- **Type**: conference
- **Published**: 26-27 Nov.
- **Authors**: Srdan Brkic, Predrag Ivaniš
- **PDF**: https://ieeexplore.ieee.org/document/8971243
- **Abstract**: This paper contains a performance analysis of Faster than Nyquist (FTN) signaling schemes that employ low-density parity-check (LDPC) codes, trellis-based detector and turbo equalization decoding principle. Based on EXIT charts analysis, we provide a numerical upper bound on achievable information rate (AIR) of FTN communication systems with identically and uniformly distributed (i.u.d.) inputs and finite number of turbo decoding iterations. Additionally, we derive a tighter conjectured upper bound on AIR and demonstrate its usefulness by showing that it is possible to design randomly constructed LDPC codes that operate within 0.7 dB of the proposed bound.

## The Effect of Error Correcting Codes in the Chain of Transmission and Comparison between the Performances of these Codes

- **Status**: ❌
- **Reason**: 여러 ECC(turbo/conv/block/LDPC) 성능 비교 연구, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:8966917
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Fayssal Menezla, Mohammed Sofiane Bendelhoum, Zoubir Mahdjoub +2
- **PDF**: https://ieeexplore.ieee.org/document/8966917
- **Abstract**: The aim of the present paper is to study and compare, in an optimal way, the functions of coding and decoding of a transmission channel through deferent coders (Turbo-Code, Convolution Code, Code en Bloc, Code LDPC). Whatever the quality of the communication media and the used transmission techniques, disturbances will occur, and cause errors. In these conditions, the received binary sequence will not be identical to the transmitted one. To eliminate these problems, techniques of protection against transmission errors can be used. On the other hand, to eliminate the noise introduced by the channel and to improve the reception of the communication system, it is necessary to add an Error Correcting Encoder (ECC) in this chain. As a choice of Code, it is possible to use turbo codes because these codes make it possible to approach the theoretical limit of correction presented by Shannon. For this reason, turbo codes are used in most modern communications systems. The obtained simulations results under conditions compatible with a hardware realization of the encoder and the decoder show very close performances to the theoretical limits of the channel coding.

## Firmware Updates Over the Air Mechanisms for Low Power Wide Area Networks: A Review

- **Status**: ❌
- **Reason**: FUOTA 펌웨어 업데이트/WSN 리뷰, LDPC ECC와 무관
- **ID**: ieee:9015851
- **Type**: conference
- **Published**: 21-22 Nov.
- **Authors**: Mompoloki Pule, Adnan M. Abu-Mahfouz
- **PDF**: https://ieeexplore.ieee.org/document/9015851
- **Abstract**: Wireless Sensor Networks (WSN) provide an affordable infrastructure that allows numerous control and data collection processes to be conducted with high spatial and temporal resolution. The recent arrival of Low Power Wide Area Networks (LPWAN) has given rise to WSN solutions with long range capabilities and a high level of autonomy. However, this has come at a cost of having low data rates and poses quite a huge challenge on implementation of high bandwidth applications such as Firmware Updates Over the Air (FUOTA). Firmware updates are essential throughout the lifetime of a product for several reasons including post deployment bug fixes, introduction of new security features and implementation of performance optimizations. This paper proposes a generic and hypothetical approach to designing an efficient FUOTA mechanism for WSN/LPWAN. The paper also presents a review of past literature on similar works and how best existing approaches have addressed the challenges of remote sensor node reprogramming.

## Results of the DTMB-A Field Trials in Hong Kong

- **Status**: ❌
- **Reason**: DTMB-A 지상파 방송 현장 시험 결과, LDPC 무관한 SFN 커버리지 측정 — 떼어낼 ECC 기법 없음
- **ID**: ieee:9030555
- **Type**: conference
- **Published**: 20-21 Nov.
- **Authors**: Changyong Pan, Chao Zhang, Hui Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/9030555
- **Abstract**: Digital terrestrial/television multimedia broadcasting - advanced (DTMB-A), the new generation of digital terrestrial television broadcasting (DTTB) system proposed by China, has been officially accepted by the International Telecommunication Union (ITU) as the international DTTB standard in 2015. Compared with DTMB standard, DTMB-A has higher spectrum efficiency, stronger robustness and more flexible system parameter combinations. In August 2019, at the invitation of Television Broadcasts Limited (TVB), Tsinghua University organized the field trials to evaluate the coverage effect of DTMB-A in Hong Kong. By setting up the single frequency network (SFN) with 3 transmitting stations, 4K UHDTV program can be transmitted by DTMB-A effectively. In this paper, the DTMB-A SFN structure and measurement results in Hong Kong are analyzed in detail.

## Probabilistically-Shaped Four-Dimensional LDPC-Coded Modulation in 100 km DWDM Optical Transmission for Metro Network Applications

- **Status**: ❌
- **Reason**: 확률성형 4D LDPC 변조, 변조/성형 중심에 LDPC는 베이스라인, 신규 디코더/구성 없음
- **ID**: ieee:8989110
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Xiao Han, Mingwei Yang, Ivan B. Djordjevic +1
- **PDF**: https://ieeexplore.ieee.org/document/8989110
- **Abstract**: We propose a probabilistically-shaped four-dimensional LDPC-coded modulation (PS-4D-LDPC-CM) scheme as a candidate suitable for metro DWDM communications. We experimentally demonstrate that PS modulation can also be used in high-dimensional-modulation scheme for DWDM systems, and that PS-4D-LDPC-CM scheme provides 1.3dB improvement over corresponding uniform distribution-based scheme.

## A Nonuniform Signal Shaping Scheme Based on BCH and LDPC Concatenated Code

- **Status**: ❌
- **Reason**: BCH+LDPC 연접 신호성형 기법, 변조 성형 중심으로 떼어낼 디코더/HW 기여 없음
- **ID**: ieee:8989148
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Xia Sheng, Qi Zhang, Xiangjun Xin +6
- **PDF**: https://ieeexplore.ieee.org/document/8989148
- **Abstract**: A nonuniform 12QAM signal shaping scheme based on BCH and LDPC concatenated code is proposed. The simulation results show that the proposed scheme requires lower SNR than uncoded-PS-12QAM and LDPC-PS12QAM schemes.

## Beyond 100G Optical Interconnect with Short-Block Polar Coding

- **Status**: ❌
- **Reason**: Polar+CRC+SCL 광통신, 비-LDPC이고 SCL은 polar 전용 디코더라 LDPC BP 이식 불가
- **ID**: ieee:8989041
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Wenkai Yang, Zibin Li, Dongdong Zou +3
- **PDF**: https://ieeexplore.ieee.org/document/8989041
- **Abstract**: We investigate polar code with cyclic redundancy check (CRC) and successive cancellation list (SCL) decoding in beyond 100G optical interconnection. Error free can be achieved with 80% code rate polar coding when the hard decision BER is 2.5×10−2

## High-Performance 50G-PON Burst-Mode Upstream Transmission at 25 Gb/s with DSP-Assisted Fast Burst Synchronization and Recovery

- **Status**: ❌
- **Reason**: 50G-PON 버스트모드 DSP 동기화, LDPC는 BER 임계치 언급뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8989106
- **Type**: conference
- **Published**: 2-5 Nov. 2
- **Authors**: Huaiyu Zheng, Andy Shen, Ning Cheng +3
- **PDF**: https://ieeexplore.ieee.org/document/8989106
- **Abstract**: We experimentally demonstrate high-performance burst-mode upstream transmission at 25 Gb/s for 50G-PON. With a novel DSP-assisted burst-mode receiver, we achieve fast burst synchronization and recovery within ∼200 ns, and a record receiver sensitivity of −29.8 dBm at the SD-LDPC BER threshold of 2×10−2 after 20-km SSMF transmission.

## A Comparative Performance Analysis of Regular LDPC Codes Over AWGN and Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: 정규 LDPC AWGN vs Rayleigh 단순 성능비교, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:8988542
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Reza Biazaran, Hermann J. Helgert
- **PDF**: https://ieeexplore.ieee.org/document/8988542
- **Abstract**: In this paper, we provide a comparative performance analysis of regular Low Density Parity Check (LDPC) codes with rate ½ over uncorrelated Rayleigh fading channel and Additive White Gaussian Noise (AWGN) channel to find out to what extent a Rayleigh channel, in which the transmissions are interleaved, approximates the effect of an Additive White Gaussian Noise (AWGN) channel . We provide two performance metrics to quantify this comparative study, probability of bit error, and cross correlation of the bits as they travel across the two channels. We calculate cross correlation of the transmitted codewords while the bits are fully or partially interleaved and demonstrate that fully interleaving bits of LDPC encoded codewords (transmitted across Rayleigh fading channel) creates the most correlation with encoded codewords (transmitted across Additive White Gaussian Noise channel) by a factor of 7/5. Additionally, we show that the regular LDPC code used in this study generally performs better (or similar) over Gaussian channel. For two specific signal to noise ratios of 2 dB and 4 dB, probability of bit error associated with Rayleigh channel is approximately twice as much as probability of bit error associated with AWGN channel.

## Downscaled LDPC Codes for Indonesia Digital Video Broadcasting Terrestrial 2nd Generation (DVB-T2)

- **Status**: ❌
- **Reason**: DVB-T2 표준 LDPC를 downscaling해 성능평가, 신규 디코더/구성 기여 없는 표준 부호 재사용
- **ID**: ieee:9068651
- **Type**: conference
- **Published**: 18-19 Nov.
- **Authors**: Citra Yasin Akbar Fadhlika, Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/9068651
- **Abstract**: This paper evaluates the performances of Low Density Parity Check (LDPC) codes standardized for the Digital Video Broadcasting Terrestrial 2nd Generation (DVB-T2) for further practical development and applications in Indonesia. We consider a multi carrier transmission scheme under Bandung channel model derived from Indonesia natural environments. To reduce the computational complexity of encoder and decoder, we use a downscaling technique for LDPC codes of DVB-T2 with a block length of 16200 bits to 270 bits. We perform a computer-based simulation to demonstrate the effectiveness of the downscaled LDPC codes. The simulation results show acceptable Bit Error Rate (BER) performances of downscaled LDPC codes DVB-T2 under Bandung channel model suitable for application in device consuming low power.

## Extrinsic Information Transfer (EXIT) Analysis for Short Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 EXIT 분석(이론), LDPC는 개념 차용만 — 비-LDPC 이론, 떼어낼 LDPC 디코더/HW 기여 없음
- **ID**: ieee:9068617
- **Type**: conference
- **Published**: 18-19 Nov.
- **Authors**: Fauzil Halim Mufassa, Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/9068617
- **Abstract**: Ze the quality of channels into either completely noisy or noieseless channels. This paper presents extrinsic information transfer (EXIT) analysis for iterative decoding of Polar codes to reveal the mechanism of channel transformation. The purpose of understanding the transformation process are to comprehend the placement process of information bit and frozen bit and to comprehend the security standard of Polar codes. Mutual information derived based on the concept of EXIT chart for check nodes and variable nodes of low density parity check (LDPC) codes and applied to Polar codes. This paper explores the quality of the polarized channels in finite blocklength. The finite block-length is of our interest since in the fifth telecommunications generation (5G) the block length is limited. This paper reveals the EXIT curve changes of Polar codes and explores the polarization characteristics, thus, high value of mutual informations for frozen bit are needed to be detectable. If it is the other way, the error correction capability of Polar codes would be drastically decreases. These results are expected to be a reference for developments of Polar codes for 5G technologies and beyond.

## Simplified Variable Node Unit Architecture for Nonbinary LDPC Decoder

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC over GF(32) 디코더 — 비이진 LDPC는 명시적 제외
- **ID**: ieee:8953111
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Huyen Pham Thi, Cuong Dinh The, Nghia Pham Xuan +2
- **PDF**: https://ieeexplore.ieee.org/document/8953111
- **Abstract**: Nonbinary low-density-parity-check (NB-LDPC) code outperforms their binary counterpart in terms of error-correcting performance and error-floor property when the code length is moderate. However, the drawback of NB-LDPC decoders is high complexity and the complexity increases considerably when increasing the Galois-field order. In this paper, a simplified basic-set trellis min-max (sBS-TMM) algorithm that is especially efficient for high-order Galois Fields, is proposed for the variable node processing to reduce the complexity of the variable node unit (VNU) as well as the whole decoder. The decoder architecture corresponding to the proposed algorithm is designed for the (837, 726) NB-LDPC code over GF(32). The implementation results using 90-nm CMOS technology show that the proposed decoder architecture reduces the gate count by 21.35% and 9.4% with almost similar error-correcting performance, compared to the up-to-date works.

## Deep Learning based Channel Code Recognition using TextCNN

- **Status**: ❌
- **Reason**: 채널코드 인식(TextCNN) — 디코딩/ECC가 아닌 코드 분류, 떼어낼 디코더 기법 없음
- **ID**: ieee:8935805
- **Type**: conference
- **Published**: 11-14 Nov.
- **Authors**: Xiongfei Qin, Shengliang Peng, Xi Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/8935805
- **Abstract**: The following topics are dealt with: radio spectrum management; cognitive radio; cellular radio; learning (artificial intelligence); wireless channels; telecommunication computing; radiofrequency interference; 5G mobile communication; signal detection; mobile computing.

## Analysis and Comparison of Several Mitigation Techniques for Middleton Class-A Noise

- **Status**: ❌
- **Reason**: Middleton class-A 임펄스 잡음 완화(클리핑/블랭킹/LLR) — 무선/PLC 채널 잡음 완화 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8938020
- **Type**: conference
- **Published**: 11-13 Nov.
- **Authors**: Md Sahabul Alam, Bassant Selim, Georges Kaddoum
- **PDF**: https://ieeexplore.ieee.org/document/8938020
- **Abstract**: Impulsive noise is a common impediment in many wireless, power line communication (PLC), and smart grid communication systems that prevents the system from achieving error-free transmission. In this paper, we compare and analyze several impulsive noise mitigation techniques for Middleton class-A noise considering single carrier modulation with low-density parity-check (LDPC) coded transmission. For this, we investigate the widely used non-linear methods such as clipping, blanking, and combined clipping/blanking to mitigate the noxious effects of impulsive noise. Although, the performance of these techniques are widely acknowledged for simple Bernoulli-Gaussian impulsive noise mitigation in case of orthogonal frequency division multiplexing (OFDM)-based multi-carrier communication systems, their mitigation capabilities in regards to Middleton class-A noise remains unknown. We further investigate the log-likelihood ratio (LLR)-based impulsive noise mitigation. Simulation results are provided to highlight the robustness of the LLR-based mitigation scheme over simple clipping/blanking schemes for the considered scenario. Moreover, our results show that while clipping performs better than blanking for Bernoulli-Gaussian noise, the later shows better performance in case of Middleton class-A noise.
