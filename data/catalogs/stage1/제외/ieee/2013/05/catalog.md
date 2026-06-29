# IEEE Xplore — 2013-05


## Improved Code-Aided Symbol Timing Recovery with Large Estimation Range for LDPC-Coded Systems

- **Status**: ❌
- **Reason**: Code-aided symbol timing recovery/synchronization for LDPC-coded wireless; no portable decoder/HW/code-design ECC technique
- **ID**: ieee:6497001
- **Type**: journal
- **Published**: May 2013
- **Authors**: Xin Man, Haitao Zhai, Jun Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/6497001
- **Abstract**: We present an improved code-aided symbol timing recovery method for low-density parity-check (LDPC) coded systems, which comprises two supporting algorithms: 1) a coarse estimation by utilizing a cost function, the mean absolute value of soft output of the LDPC decoder and 2) a fine estimation based on the Expectation-Maximization (EM) algorithm with a simple maximization step. With low computational complexity, this proposed algorithm can achieve symbol timing recovery at low signal-to-noise ratio (SNR) with large estimation range, eliminating the biased results of many algorithms for large timing offset values. Simulation results for the case of 8-PSK system with (1944,972) LDPC code show that the root-mean-square-error (RMSE) performance of the proposed algorithm approaches the modified Cramer-Rao lower bound (MCRB) at Eb/No=4dB, and the bit-error-rate (BER) curve is very close to that of ideal synchronization.

## Scaling, Offset, and Balancing Techniques in FFT-Based BP Nonbinary LDPC Decoders

- **Status**: ❌
- **Reason**: Nonbinary (GF(q)) FFT-based BP LDPC decoder; non-binary LDPC excluded
- **ID**: ieee:6488777
- **Type**: journal
- **Published**: May 2013
- **Authors**: Sangmin Kim, Gerald E. Sobelman
- **PDF**: https://ieeexplore.ieee.org/document/6488777
- **Abstract**: An analysis of finite precision effects in nonbinary mixed-domain low-density parity-check decoders is presented. It is shown how improved decoding performance can be achieved by using an offset-based method and proper scaling techniques. In addition, a novel fast Fourier transform (FFT)-based belief propagation (BP) decoder architecture is proposed which balances the computational load between processing units. The results show a 47% reduction in the number of required field-programmable gate array slices compared to a standard FFT-based BP architecture.

## Interactive Encoding and Decoding Based on Binary LDPC Codes With Syndrome Accumulation

- **Status**: ❌
- **Reason**: Syndrome accumulation 기반 무손실 소스코딩(Slepian-Wolf) — 소스 코딩이라 채널 ECC 아님, 원칙 제외 (애매하나 BP bound 언급은 부수적)
- **ID**: ieee:6395828
- **Type**: journal
- **Published**: May 2013
- **Authors**: Jin Meng, En-Hui Yang
- **PDF**: https://ieeexplore.ieee.org/document/6395828
- **Abstract**: Interactive encoding and decoding based on binary low-density parity-check codes with syndrome accumulation (SA-LDPC-IED) is proposed and investigated. Assume that the source alphabet is GF(2), and the side information alphabet is finite. It is first demonstrated how to convert any classical universal lossless code Cn (with block length n and side information available to both the encoder and decoder) into a universal SA-LDPC-IED scheme. It is then shown that with the word error probability approaching 0 subexponentially with n , the compression rate (including both the forward and backward rates) of the resulting SA-LDPC-IED scheme is upper bounded by a functional of that of Cn, which in turn approaches the compression rate of Cn for each and every individual sequence pair (xn, yn) and the conditional entropy rate H (X |Y) for any stationary, ergodic source and side information (X, Y) as the average variable node degree l̅ of the underlying LDPC code increases without bound. When applied to the class of binary source and side information (X, Y) correlated through a binary symmetrical channel with crossover probability unknown to both the encoder and decoder, the resulting SA-LDPC-IED scheme can be further simplified, yielding even improved rate performance versus the bit error probability when l̅ is not large. Simulation results (coupled with linear time belief propagation decoding) on binary source-side information pairs confirm the theoretic analysis and further show that the SA-LDPC-IED scheme consistently outperforms the Slepian-Wolf coding scheme based on the same underlying LDPC code. As a by-product, probability bounds involving LDPC established in the course are also interesting on their own and expected to have implications on the performance of LDPC for channel coding as well.

## A Low-Complexity LDPC Decoding Algorithm for Hierarchical Broadcasting: Design and Implementation

- **Status**: ❌
- **Reason**: 계층 방송 시스템 ILI 완화용 구조기반 디코딩, 무선 응용 특이적이고 NAND LDPC BP로 떼어낼 ECC 기법 없음
- **ID**: ieee:6395844
- **Type**: journal
- **Published**: May 2013
- **Authors**: Zixia Hu, Hui Liu
- **PDF**: https://ieeexplore.ieee.org/document/6395844
- **Abstract**: In this paper, we present a structure-based decoding algorithm for the hierarchical broadcasting systems. Unlike the traditional hierarchical demodulation approaches that suffer from serious interlayer interference (ILI), the proposed method exploits the structure information on the secondary layer to mitigate the ILI impairment, thereby offering significant gains in reception performance. The algorithm can be applied to different channel coding and mapping schemes under various channel profiles. In addition, the new algorithm has been implemented on a broad-band in-band-on-channel digital radio broadcasting system. Numerical results from both simulations and laboratory experiments are provided to quantify the performance advantages of the new algorithm.

## On Pseudocodewords and Improved Union Bound of Linear Programming Decoding of HDPC Codes

- **Status**: ❌
- **Reason**: HDPC(BCH) 대상 LP 디코딩 union bound 개선, 순수 이론 bound이며 비-LDPC HDPC 대상이라 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6480916
- **Type**: journal
- **Published**: May 2013
- **Authors**: Ohad Gidon, Yair Be'ery
- **PDF**: https://ieeexplore.ieee.org/document/6480916
- **Abstract**: In this paper, we present an improved union bound on the Linear Programming (LP) decoding performance of binary linear codes transmitted over an additive white Gaussian noise channel. The bounding technique is based on the Hunter bound, which is a second-order upper bound in probability theory, and it is minimized by Prim's minimum spanning tree algorithm. The bound calculation needs the fundamental cone generators of a given parity-check matrix rather than only their weight distribution, but involves relatively low computational complexity. It is targeted to high-density parity-check codes, where the number of their generators is extremely large and these generators are densely distributed in the Euclidean space. We explore the generator density and make a comparison between different parity-check matrix representations. That density affects the improvement of the proposed bound over the conventional LP union bound. This paper also presents a complete pseudo-weight distribution of the fundamental cone generators for the BCH[31,21,5] code.

## A Novel Decoding Scheme for LT-Codes in Wireless Broadcasting Systems

- **Status**: ❌
- **Reason**: 무선 방송용 LT-codes(fountain) hybrid soft/hard 디코딩, fountain 부호이며 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:6484243
- **Type**: journal
- **Published**: May 2013
- **Authors**: Kongtao Wang, Zhiyong Chen, Hui Liu
- **PDF**: https://ieeexplore.ieee.org/document/6484243
- **Abstract**: In this letter, a novel decoding strategy for Luby transform (LT) codes in wireless broadcasting systems is presented and analyzed. The proposed hybrid-soft-and-hard-decoding (HSHD) scheme leverages cooperation between the MAC and the PHY layer, and achieves significant gains in spectrum efficiency and broadcasting coverage with marginal increase in complexity. Simulation results are provided to illustrate the excellent performance of HSHD in both AWGN and Rayleigh fading channels. The decoding complexity of HSHD is also quantified.

## RS-Enhanced TCM for Multilevel Flash Memories

- **Status**: ❌
- **Reason**: 멀티레벨 플래시 대상이나 부호가 TCM+RS 연접이며 LDPC 아님, 비-LDPC 부호로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6476608
- **Type**: journal
- **Published**: May 2013
- **Authors**: Jieun Oh, Jeongseok Ha, Jaekyun Moon +1
- **PDF**: https://ieeexplore.ieee.org/document/6476608
- **Abstract**: Multilevel flash memories store more than one bit per storage cell and are further characterized by large word (page) sizes and very low target error rates. In this paper, a high-rate error control scheme is presented that uses inner trellis-coded modulation (TCM) for storing two bits per cell with five possible charge levels. The coded subset-label bits and the uncoded signal-label bits of TCM are independently protected by separate outer Reed-Solomon (RS) codes. The resulting scheme permits multistage decoding. Errors made by the TCM decoder in the subset-label bits occur in bursts and are corrected by the associated first RS decoder prior to determining signal-label bits and correcting errors in those bits by the associated second RS decoder. The multi-stage decoding avoids the significant spread of errors from subset-label bits into the generally larger number of signal-label bits which is typical for conventional serial RS-TCM concatenation when the inner TCM system operates at relatively low SNR. The error performance of the proposed scheme is evaluated at low error rates by a mixed simulation-analytic method. It is shown that the proposed scheme exhibits highly favorable performance vs. complexity tradeoffs compared to the other schemes.

## Generalized Adaptive Network Coding Aided Successive Relaying for Noncoherent Cooperation

- **Status**: ❌
- **Reason**: 적응형 네트워크 코딩+협력 릴레이, 무선 응용 특이적이고 LDPC ECC 기법 없음
- **ID**: ieee:6476609
- **Type**: journal
- **Published**: May 2013
- **Authors**: Li Li, Li Wang, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/6476609
- **Abstract**: A generalized adaptive network coding (GANC) scheme is conceived for a multi-user, multi-relay scenario, where the multiple users transmit independent information streams to a common destination with the aid of multiple relays. The proposed GANC scheme is developed from adaptive network coded cooperation (ANCC), which aims for a high flexibility in order to: 1) allow arbitrary channel coding schemes to serve as the cross-layer network coding regime; 2) provide any arbitrary trade-off between the throughput and reliability by adjusting the ratio of the source nodes and the cooperating relay nodes. Furthermore, we incorporate the proposed GANC scheme in a novel successive relaying aided network (SRAN) in order to recover the typical 50% half-duplex relaying-induced throughput loss. However, in support of the coherent detection, in addition to carrying out all the relaying functions, the relays have to estimate the Source-to-Relay channels, which imposes a substantial extra energy consumption and bit rate reduction owing to the inclusion of pilots. Hence noncoherent detection is employed for eliminating the power-hungry channel estimation. Finally, we intrinsically amalgamate our GANC scheme with the joint network-channel coding (JNCC) concept into a powerful three-stage concatenated architecture relying on iterative detection, which is specifically designed for the destination node (DN). The proposed scheme is also capable of adapting to rapidly time-varying network topologies, while relying on energy-efficient detection.

## On the performance of 1-level LDPC lattices

- **Status**: ❌
- **Reason**: LDPC lattice(격자부호) min-sum 디코딩 — 부호가 격자 기반이라 바이너리 LDPC 채널 ECC와 다름, 떼어낼 기법 없음
- **ID**: ieee:6555759
- **Type**: conference
- **Published**: 8-9 May 20
- **Authors**: Mohammad-Reza Sadeghi, Amin Sakzad
- **PDF**: https://ieeexplore.ieee.org/document/6555759
- **Abstract**: The low-density parity-check (LDPC) lattices perform very well in high dimensions under generalized min-sum iterative decoding algorithm. In this work, we focus on 1-level LDPC lattices. We show that these lattices are the same as lattices constructed based on Construction A and low-density lattice-code (LDLC) lattices. In spite of having slightly lower coding gain, 1level regular LDPC lattices have remarkable performances. The lower complexity nature of the decoding algorithm for these type of lattices allows us to run it for higher dimensions easily. Our simulation results show that a 1-level LDPC lattice of size 10000 can work as close as 1.1 dB at normalized error probability (NEP) of 10-5.This can also be reported as 0.6 dB at symbol error rate (SER) of 10-5 with sum-product algorithm.

## Channel coding adoption versus increasing sensing time in secondary service to manage the effect of imperfect spectrum sensing in cognitive radio networks

- **Status**: ❌
- **Reason**: 인지무선 스펙트럼 센싱 vs 채널코딩 트레이드오프, rate-compatible LDPC 단순 사용 — 무선 응용 특이적, 새 기법 없음
- **ID**: ieee:6555757
- **Type**: conference
- **Published**: 8-9 May 20
- **Authors**: Sadjad Haddadi, Hamid Saeedi, Keivan Navaie
- **PDF**: https://ieeexplore.ieee.org/document/6555757
- **Abstract**: In this paper we consider an overlay cognitive network in which to guarantee a Quality of Service (QoS) for the primary users, a maximum probability of collision is enforced to secondary service. When collision, caused by imperfect spectrum sensing, happens, it results in increasing error rate in both primary and secondary systems. While such degradation in primary service conforms with QoS requirements of that service, this may not be acceptable from secondary user perspective. Such degradation can be dealt with in secondary service either by employing channel coding techniques at the expense of effective rate reduction or increasing the sensing time to reduce the collision probability. This results in the reduction of the data transmission time which also results in the reduction of effective data rate for secondary users. In this paper, we compare these two cases and show that using rate-compatible Low-Density Parity-Check codes, the effective data rate for the coded case can be significantly more than that of the case without channel coding while exhibiting a considerably better performance.

## Performance and Complexity of Turbo Equalizers for optical coherent Gbit/s Transmission with optimal and suboptimal Detection Strategies

- **Status**: ❌
- **Reason**: Turbo equalizer(BCJR/MMSE) for optical coherent; LDPC는 부수 baseline, 떼어낼 LDPC ECC 기법 없음(C/D/E 해당 없음)
- **ID**: ieee:6507683
- **Type**: conference
- **Published**: 6-7 May 20
- **Authors**: Klaus Oestreich, Joachim Speidel
- **PDF**: https://ieeexplore.ieee.org/document/6507683
- **Abstract**: In this paper, we investigate two different turbo equalizers with distinct detection strategies for coherent optical communication with QPSK modulated signals. The first receiver comprises a BCJR detector and a soft-in soft-out LDPC decoder. In the second receiver, the BCJR unit is replaced by a linear MMSE filter. Offering enough turbo iterations for the receiver with MMSE detection, the performance is almost the same as for the receiver with the optimal BCJR detection. As the computational complexity of the MMSE detection is considerable lower as for the BCJR detection, the turbo equalizer with MMSE detection offers a good compromise between complexity and performance.

## Improving performance of H.264/AVC transmissions over vehicular networks

- **Status**: ❌
- **Reason**: 차량 네트워크 H.264 전송에 LDPC를 conv코드 대체로 부수 사용. 무선 응용 특이적, 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:6573185
- **Type**: conference
- **Published**: 27-31 May 
- **Authors**: Ismael Rozas-Ramallal, Tiago M. Fernández-Caramés, Adriana Dapena +1
- **PDF**: https://ieeexplore.ieee.org/document/6573185
- **Abstract**: This paper evaluates the performance of H.264/AVC transmissions over IEEE 802.11p -a standard explicitly designed to perform vehicular communications- and proposes two different strategies for improving performance. The first one consists in substituting the convolutional codes used in IEEE 802.11p with Low-Density Parity-Check (LDPC) codes. The second strategy consists in adapting the transmission power by taking into account the picture type (I/P/B picture). Experimental simulation results show that the utilization of these two methods allows us to reduce GOP (Group Of Pictures) losses and improves video quality without increasing computational requirements. The evaluation has been carried out using a testbed that integrates the H.264/AVC JM encoder, an IEEE 802.11p transceiver and an FPGA-based channel emulator that implements vehicular channel models based on a measurement campaign performed in 2006 in Atlanta, Georgia.

## Error-correction schemes with erasure information for fast memories

- **Status**: ❌
- **Reason**: 메모리 erasure ECC지만 SEC-DED/단축 SEC 코드 기반(비-LDPC), LDPC 무관. 떼어낼 LDPC 기법 없음
- **ID**: ieee:6569371
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Samuel Evain, Valentin Gherman
- **PDF**: https://ieeexplore.ieee.org/document/6569371
- **Abstract**: Two error correction schemes are proposed for binary memories that can be affected by erasures, i.e. errors with known location but unknown value. The erasures considered here are due to the drifting of the electrical parameter used to encode information outside the normal ranges associated to a logic 0 or a logic 1 value. For example, a dielectric breakdown in a magnetic memory cell may reduce its electrical resistance sensibly below the levels which correspond to logic 0 and logic 1 values stored in healthy memory cells. Such deviations can be sensed during memory read operations and the acquired information can be used to boost the fault masking capacity of an error-correcting code. Here, we investigate the use of erasure information to enable double-bit error correction with the help of single-bit error correction and double-bit error detection codes or shortened single-bit error correction codes.

## FFT-SPA non-binary LDPC decoding on GPU

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC FFT-SPA GPU 디코딩; 비이진 LDPC 제외
- **ID**: ieee:6638633
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: J. Andrade, G. Falcao, V. Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/6638633
- **Abstract**: It is well known that non-binary LDPC codes outperform the BER performance of binary LDPC codes for the same code length. The superior BER performance of non-binary codes comes at the expense of more complex decoding algorithms that demand higher computational power. In this paper, we propose parallel signal processing algorithms for performing the FFT-SPA and the corresponding decoding of non-binary LDPC codes over GF(q). The constraints imposed by the complex nature of associated subsystems and kernels, in particular the Check Nodes, present computational challenges regarding multicore systems. Experimental results obtained on GPU for a variety of GF(q) show throughputs in the order of 2 Mbps, which is far above from the minimum throughput required, for example, for real-time video applications that can benefit from such error correcting capabilities.

## Universal Wyner-Ziv coding for Gaussian sources

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩+비이진 LDPC; 소스코딩이며 비이진 LDPC라 이중 제외
- **ID**: ieee:6638640
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Elsa Dupraz, Aline Roumy, Michel Kieffer
- **PDF**: https://ieeexplore.ieee.org/document/6638640
- **Abstract**: This paper considers the problem of lossy source coding with side information at the decoder only, for Gaussian sources, when the joint statistics of the sources are partly unknown. We propose a practical universal coding scheme based on scalar quantization and nonbinary LDPC codes, which avoids the binarization of the quantized coefficients. We first explain how to choose the rate and to construct the LDPC coding matrix. Then, a decoding algorithm that jointly estimates the source sequence and the joint statistics of the sources is proposed. The proposed coding scheme suffers no loss compared to the practical coding scheme with same rate but known variance.

## A modified watermark synchronisation code for robust embedding of data in DNA

- **Status**: ❌
- **Reason**: DNA 데이터 임베딩 watermark 동기화 코드 + 표준 LDPC — LDPC 부수 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:6637830
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: David Haughton, Félix Balado
- **PDF**: https://ieeexplore.ieee.org/document/6637830
- **Abstract**: DNA data embedding is a newly emerging field aspiring to encode data in deoxyribonucleic acid (DNA). DNA is an inherently digital and noisy medium, undergoing substitution, insertion and deletion mutations. Hence, encoding information in DNA can be seen as a particular case of digital communications in which biological constraints must be observed. In this paper we propose a modification of Davey and MacKay's watermark synchronisation code (unrelated to digital watermarking) to create an encoding procedure more biocompatible with the host organism than previous methods. In addition, when combined with a low density parity check (LDPC) code, the method provides near-optimum error correction. We also obtain the theoretical embedding capacity of DNA under substitution mutations for the increased biocompatibility constraint. This result, along with an existing bound on capacity for insertion and deletion mutations, is compared to the proposed algorithm's performance by means of Monte Carlo simulations.

## Optimal deterministic compressed sensing matrices

- **Status**: ❌
- **Reason**: 결정론적 압축센싱 측정행렬(girth 활용); 압축센싱 신호복원이며 LDPC ECC 코드설계 아님
- **ID**: ieee:6638795
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Arash Saber Tehrani, Alexandros G. Dimakis, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/6638795
- **Abstract**: We present the first deterministic measurement matrix construction with an order-optimal number of rows for sparse signal reconstruction. This improves the measurements required in prior constructions and addresses a known open problem in the theory of sparse signal recovery. Our construction uses adjacency matrices of bipartite graphs that have large girth. The main result is that girth (the length of the shortest cycle in the graph) can be used as a certificate that a measurement matrix can recover almost all sparse signals. Specifically, our matrices guarantee recovery “for-each” sparse signal under basis pursuit. Our techniques are coding theoretic and rely on a recent connection of compressed sensing to LP relaxations for channel decoding.

## Hardware-driven compressive sampling for fast target localization using single-chip UWB radar sensor

- **Status**: ❌
- **Reason**: UWB 레이더 압축센싱에 LDPC 행렬을 센싱매트릭스로 사용 — 채널 ECC가 아닌 CS 응용, 떼어낼 디코더 기법 없음
- **ID**: ieee:6638126
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Sungwon Lee, Chenliang Du, Hossein Hashemi +1
- **PDF**: https://ieeexplore.ieee.org/document/6638126
- **Abstract**: To design an energy-efficient UWB ranging system, we propose a compressive sampling (CS) technique tightly coupled to a recently proposed hardware. Our goal is to design a system that is robust to high noise and consumes less energy while providing reliable localization. In this work, we first introduce a representation of UWB signals as group sparse signals with the number of groups corresponding to the number of objects in the environment. Also, we design an efficient measurement system that is constructed using low-density parity-check (LDPC) matrix, in order to satisfy several constraints imposed by the hardware: non-negative integer entries in measurement (sensing) matrix, constant row-wise sum of non-zero entries in the matrix, and a unique structure characterized by Kronecker product. To enhance performance, we propose a window-based reweighted L1 minimization that outperforms other existing algorithms in our simulation. The result shows that our proposed method can achieve reliable target-localization, while using only 40% of the scanning (sampling) time required by the sequential scanning scheme, even in highly-noisy environments.

## On finite alphabet compressive sensing

- **Status**: ❌
- **Reason**: 유한알파벳 압축센싱; ECC 채널코딩 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6638794
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Abhik Kumar Das, Sriram Vishwanath
- **PDF**: https://ieeexplore.ieee.org/document/6638794
- **Abstract**: This paper considers the problem of compressive sensing over a finite alphabet, where the finite alphabet may be inherent to the nature of the data or a result of quantization. We show that there are significant benefits to analyzing the problem while incorporating its finite alphabet nature, versus ignoring it and employing a conventional real alphabet based toolbox. Specifically, when the alphabet is finite, our techniques have a lower sample complexity compared to real-valued compressive sensing for low levels of sparsity, facilitate constructive designs of sensing matrices based on coding-theoretic techniques, and allow for lesser amount of data storage.

## On the use of explicit redundancy for delayless soft-decision audio decoding

- **Status**: ❌
- **Reason**: 오디오 soft-decision 디코딩(베이지안 암묵중복); 블록부호 일반, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6638637
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Florian Pflug, Tim Fingscheidt
- **PDF**: https://ieeexplore.ieee.org/document/6638637
- **Abstract**: Wireless transmission systems for high-quality digital audio signals require a low end-to-end delay and strong robustness against channel distortions. In this work we investigate a Bayesian approach to delayless soft-decision decoding of high-quality audio signals jointly exploiting both implicit redundancy within the audio signal and explicit sample-wise redundancy appended by a channel (block) encoder. Because our approach introduces no algorithmic delay, it can be employed in audio transmission systems that are extremely sensitive to latency like, e. g., wireless digital microphones. Experiments carried out with representative audio signals transmitted over AWGN channels show a significant increase in signal quality.

## Securewaveforms for SISO channels

- **Status**: ❌
- **Reason**: 무선 보안 파형 설계(SINR/AN); ECC·LDPC 무관
- **ID**: ieee:6638554
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Ming Li, Sandipan Kundu, Dimitris A. Pados +1
- **PDF**: https://ieeexplore.ieee.org/document/6638554
- **Abstract**: We develop a novel waveform design approach to minimize the likelihood that a message transmitted wirelessly between trusted single-antenna nodes is intercepted by an eavesdropper. In particular, first, with knowledge of the eavesdropper's channel state information (CSI) we find the optimal waveform and transmit energy that minimize the signal-to-interference-plus-noise ratio (SINR) at the output of the eavesdropper's maximum-SINR linear filter, while at the same time provide the intended receiver with a required pre-specified SINR at the output of its own max-SINR filter. Next, if prior knowledge of the eavesdropper's CSI is unavailable, we design a waveform that maximizes the amount of energy available for generating disturbance to eavesdroppers, termed artificial noise (AN), while the SINR of the intended receiver is maintained at the pre-specified level. Simulation studies demonstrate our analytical developments and illustrate the benefits of the designed waveforms on securing single-input single-output (SISO) transmissions.

## Hybrid variational Bayesian channel estimation, demodulation and decoding for OFDM under sparse multipath channels

- **Status**: ❌
- **Reason**: OFDM 변분베이즈 채널추정+Turbo 코딩 수신기; LDPC 무관, 떼어낼 바이너리 LDPC 디코더 기법 없음
- **ID**: ieee:6638520
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Chulong Chen, Michael D. Zoltowski
- **PDF**: https://ieeexplore.ieee.org/document/6638520
- **Abstract**: In this paper, a novel hybrid OFDM receiver based on sparse variational Bayesian (VB) learning and soft-input soft-output decoding is proposed. By noticing that a key part of the inference problem approximated by VB (message-passing) methods may be inferred exactly, an genetic interfacing structure is proposed allowing the use of virtually all existing soft-input soft-output decoding schemes. Therefore the tasks of joint channel state estimation, demodulation and decoding are iteratively solved under the proposed hybrid variational Bayesian framework. The bit-interleaved coded modulation with Turbo coding is used to demonstrate the potential performance of the proposed structure. Very promising results in performance are observed in computer simulated experiments.

## Memory scaling: A systems architecture perspective

- **Status**: ❌
- **Reason**: 메모리/DRAM 스케일링 시스템 아키텍처 서베이, NAND 언급은 부수적이며 떼어낼 LDPC 디코더/코드 기법 없음
- **ID**: ieee:6582088
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Onur Mutlu
- **PDF**: https://ieeexplore.ieee.org/document/6582088
- **Abstract**: The memory system is a fundamental performance and energy bottleneck in almost all computing systems. Recent system design, application, and technology trends that require more capacity, bandwidth, efficiency, and predictability out of the memory system make it an even more important system bottleneck. At the same time, DRAM technology is experiencing difficult technology scaling challenges that make the maintenance and enhancement of its capacity, energy-efficiency, and reliability significantly more costly with conventional techniques. In this paper, after describing the demands and challenges faced by the memory system, we examine some promising research and design directions to overcome challenges posed by memory scaling. Specifically, we survey three key solution directions: 1) enabling new DRAM architectures, functions, interfaces, and better integration of the DRAM and the rest of the system, 2) designing a memory system that employs emerging memory technologies and takes advantage of multiple different technologies, 3) providing predictable performance and QoS to applications sharing the memory system. We also briefly describe our ongoing related work in combating scaling challenges of NAND flash memory.

## Computational complexities and relative performance of LDPC codes and turbo codes

- **Status**: ❌
- **Reason**: LDPC vs Turbo 복잡도/성능 비교 — 표준 부호 비교 분석, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:6615299
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: Jiancun Zuo, Qiudong Sun, Fangming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6615299
- **Abstract**: This paper addresses the computational requirements and relative performance of low-density parity-check (LDPC) codes and Turbo codes. Detailed complexity analysis and exact formulas giving the required number of calculations are first presented for LDPC codes and Turbo codes, and then Monte Carlo simulations are performed to compare their relative performance at comparable computation cost. The numeral results show that even at moderate block length the optimized irregular LDPC codes can also beat Turbo codes with only 19% computational cost.

## The information reconciliation protocol basing on error codes

- **Status**: ❌
- **Reason**: QKD 정보조정(reconciliation)용 LDPC 개선—채널 ECC 아님, 떼어낼 디코더 양자화/HW 기법 명시 없음
- **ID**: ieee:6615401
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: Sun Niuniu, Zhang Shuilian, Xin Gang +1
- **PDF**: https://ieeexplore.ieee.org/document/6615401
- **Abstract**: Information reconciliation (IR) is an important step in quantum key distribution (QKD). The error correcting codes are widely used in IR, which can also be seen as error correction. But it proved that this approach contains deleting the leaked information in practical applications. Error coding is not always a guarantee of the reconciliation. It only require of the data's consistency and security. In this paper, Author proposed an improvement scheme of LDPC code on the property of reconciliation and performed some number simulations to evaluate that method. It's shown that this method would achieve a higher efficiency than the original algorithm. Therefore, this algorithm has special important meaning to the key generation.

## Data transfer paradigms for future networks: Fountain coding or congestion control?

- **Status**: ❌
- **Reason**: fountain/erasure 코딩 vs 혼잡제어, 떼어낼 채널 LDPC ECC 기법 없음
- **ID**: ieee:6663513
- **Type**: conference
- **Published**: 22-24 May 
- **Authors**: Sándor Molnár, Zoltán Móczár, András Temesváry +3
- **PDF**: https://ieeexplore.ieee.org/document/6663513
- **Abstract**: The research history of congestion control protocols has unveiled that it is difficult to find an optimal solution, which meets all the challenges of the evolving Internet. As an alternative paradigm recent studies suggest replacing congestion control with erasure coding techniques. In this paper we present a performance study of this approach comparing it with TCP based solutions. In order to investigate the new paradigm in details and also in practice, we have developed and implemented a novel transport protocol (Digital Fountain based Communication Protocol, DFCP) where an efficient digital fountain based erasure coding scheme plays the role of correcting packet loss. We present some analytical and simulation results together with our first performance comparisons in a testbed environment.

## Prototype of 3-Gb/s 60-GHz millimeter-wave-based wireless file-transfer system

- **Status**: ❌
- **Reason**: 60GHz 무선 파일전송 시스템 프로토타입, ECC/LDPC 디코더 기여 없음
- **ID**: ieee:6565715
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Yasuo Asakura, Keitarou Kondou, Masashi Shinagawa +2
- **PDF**: https://ieeexplore.ieee.org/document/6565715
- **Abstract**: We report the development of the prototype of a high-speed wireless file-transfer system using a 60-GHz band. The prototype achieved an effective user-data rate over 3 Gb/s using a quadrature-phase-shift keying modulation, including overheads of a physical layer and a retransmission control between two memory devices, by using a new 40-nm CMOS baseband LSI and automatic direct memory-access contro...

## A decoding algorithm with reduced complexity for non-binary LDPC codes over large fields

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC 대형 필드 디코딩 복잡도 저감. 비이진 LDPC 제외.
- **ID**: ieee:6572189
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Jun Lin, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6572189
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes outperform their binary counterparts in some cases, but their high decoding complexity is a significant hurdle to their applications. In this paper, we propose a decoding algorithm with reduced computational complexities and smaller memory requirements for NB-LDPC codes over large fields. First, a simplified algorithm is proposed to reduce the computational complexity of variable node processing. To reduce memory requirements, existing NB-LDPC decoders often truncate the message vectors to a limited number nm of values. However, the memory requirements of these decoders remain high when the field size is large, since nm needs to be large enough to alleviate error performance degradation. In this paper, an improved trellised based check node processing algorithm is proposed to significantly reduce the memory requirement. The number of elements in a variable-to-check message is reduced to nv (nv <; nm). The sorted log likelihood ratio (LLR) vector of a check-to-variable message is approximated using a piece-wise linear function. Thus, only few LLRs are stored and other LLRs are computed on-the-fly when needed. For each a priori message, most LLRs are approximated with a linear function. Our numerical results demonstrate that the proposed decoding algorithm outperforms existing algorithms. Two LLR generation units (LGUs) are proposed to compute LLR vectors for check-to-variable messages, and the two LGUs require only a fraction of the area needed to store nm LLRs.

## Memory efficient EMS decoding for non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC EMS 디코딩 메모리 효율화. 비이진 LDPC 제외.
- **ID**: ieee:6572101
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Leixin Zhou, Jin Sha, Yun Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6572101
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes are an extension of binary LDPC codes with significantly better performance when the code length is moderate. Previously, forward-backward schemes are used to implement check node processing, which need large amount of memory. In this paper, a novel approach-TCL-EMS is proposed for NB-LDPC decoding. Compared to original EMS decoding algorithm, the memory efficiency is improved and the average number of iterations is reduced significantly. Also, the overall decoder architecture is proposed.

## Low-complexity layered iterative hard-reliability-based majority-logic decoder for non-binary quasi-cyclic LDPC codes

- **Status**: ❌
- **Reason**: 비이진 QC-LDPC IHRB-MLGD 디코더. 비이진 LDPC 제외.
- **ID**: ieee:6572104
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6572104
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes have some advantages as opposed to their binary counterparts, but unfortunately their decoding complexity is a significant challenge. Hence, iterative hard-reliability-based majority-logic decoding (IHRB-MLGD) algorithms are attractive for NB-LDPC codes due to their low complexities. In this paper, we propose a layered improved iterative hard-reliability-based majority-logic decoding algorithm and design a partly parallel architecture for the proposed algorithm. Our improved algorithm achieves better error performance and faster convergence than existing IHRB-MLGD algorithms, while maintaining low complexities. The proposed partly parallel architecture achieves a throughput of 779 Mbps with SMIC 0.13um CMOS technology.

## Improving the performance of new service overlaid ASK-DPSK WDM-PON with nonbinary LDPC coding

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 코딩 스킴 — 바이너리 한정 기준 위배
- **ID**: ieee:6676436
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Haiping Wang, Yang Lu, Biao Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6676436
- **Abstract**: We propose a novel nonbinary low-density parity-check (NB-LDPC) coding scheme for new service overlaid wavelength-division-multiplexed passive optical network (WDM-PON). In conventional binary coding scheme, each channel is encoded/decoded independently; while in our nonbinary coding scheme, old service channel and new service channel are encoded/decoded together. Compared with independent binary coding scheme, NB-LDPC coding scheme provides better bit-error-rate performance as shown by our simulation.

## Low-density parity-check code-based WDM-OFDM-PON

- **Status**: ❌
- **Reason**: WDM-OFDM-PON 광통신 응용, LDPC 부수 사용·떼어낼 신규 ECC 기법 없음
- **ID**: ieee:6676435
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Qinglong Luo, Min Feng, Chenglin Bai +2
- **PDF**: https://ieeexplore.ieee.org/document/6676435
- **Abstract**: In this letter, a WDM-OFDM-PON architecture using LDPC code is brought up to increase transmission range and system performance. In optical line terminal (OLT), LDPC-coded OFDM signal at 10-Gb/s is transmitted as downstream. At each optical network unit (ONU), the optical OFDM signal is demodulated with direct detection, and on-off keying date at 2.5-Gb/s is returned as upstream. Simulation results show that the transmission distance could exceed 20-km with negligible penalty.

## Recognition of channel encoder parameters from intercepted bitstream

- **Status**: ❌
- **Reason**: 가로채기 비트스트림에서 채널부호 파라미터 인식(블라인드 식별) - ECC 디코더/구성/HW 기법 아님
- **ID**: ieee:6599815
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Yasser Karimian, Mahmoud Ahmadian Attari
- **PDF**: https://ieeexplore.ieee.org/document/6599815
- **Abstract**: We study recovering the channel encoder parameters for an unknown code from intercepted bitstream received from Binary Symmetric Channel in this paper. An iterative column elimination algorithm is introduced which attempts to eliminate parity bits in codewords of noisy data. This algorithm is very practical due to low complexity and use of XOR operator. Since, the computational complexity is low, searching for the length of code and synchronization is possible. Furthermore, the Hamming weight of the parity check words are only used in threshold computation and unlike other algorithms, they have negligible effect in the proposed algorithm. Eventually, experimental results are presented and estimations for the maximum noise level allowed for recovering the words of the parity check matrix are investigated.

## LDPC coded OFDM systems over broadband indoor power line channels: A performance analysis

- **Status**: ❌
- **Reason**: PLC OFDM에 표준 LDPC 적용 성능분석 - 신규 디코더/구성/HW 기여 없음, 표준 부호 단순 사용
- **ID**: ieee:6635852
- **Type**: conference
- **Published**: 13-17 May 
- **Authors**: Yasin Kabalci, Ibrahim Develi, Ersan Kabalci
- **PDF**: https://ieeexplore.ieee.org/document/6635852
- **Abstract**: Power line communication (PLC) is an emerging technology that aims to provide communication over power lines. In this paper, bit error rate (BER) performances of low-density parity-check (LDPC) coded orthogonal frequency-division multiplexing (OFDM) systems have been investigated in broadband (BB) PLC channels. The performance analyses have been performed for three different indoor channel conditions that were generated by using new and more practical PLC channel model proposal. From the simulation results, it was demonstrated that the LDPC coding scheme offers considerable coding gain with reasonable encoding complexity in the whole channel conditions, when compared to uncoded OFDM systems.
