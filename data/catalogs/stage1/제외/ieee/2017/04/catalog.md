# IEEE Xplore — 2017-04


## Low-Complexity Transformed Encoder Architectures for Quasi-Cyclic Nonbinary LDPC Codes Over Subfields

- **Status**: ❌
- **Reason**: 비이진(GF(2^p)) QC-LDPC 인코더로 non-binary 대상 제외
- **ID**: ieee:7779152
- **Type**: journal
- **Published**: April 2017
- **Authors**: Xinmiao Zhang, Ying Tai
- **PDF**: https://ieeexplore.ieee.org/document/7779152
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are adopted in many digital communication and storage systems. The encoding of these codes is traditionally done by multiplying the message vector with a generator matrix consisting of dense circulant submatrices. To reduce the encoder complexity, this paper introduces two schemes making use of finite Fourier transform. We focus on QC-LDPC codes whose circulant submatrices are of dimension  $(2^{r}-1)\times (2^{r}-1)$  and the entries are elements of GF $(2^{p})$ , where  $p$  divides  $r$ , and hence, GF $(2^{p})$  is a subfield of GF $(2^{r})$ . These cover a broad range of codes, and binary LDPC codes are a special case. Making use of conjugacy constraints, low-complexity architectures are developed for finite Fourier and inverse transforms over subfields in this paper. In addition, composite field arithmetic is exploited to eliminate the computations associated with message mapping and reduce the complexity of Fourier transform. For a (2016, 1074) nonbinary QC-LDPC code whose generator matrix consists of circulants of dimension  $63 \times 63$  with GF $(2^{2})$  entries, the proposed encoders achieve 22% area reduction compared with the conventional encoders without sacrificing the throughput.

## A New Variant of the McEliece Cryptosystem Based on QC-LDPC and QC-MDPC Codes

- **Status**: ❌
- **Reason**: QC-LDPC/QC-MDPC 기반 McEliece 암호시스템, 보안 응용이며 새 디코더·구성 기여 없음
- **ID**: ieee:7784752
- **Type**: journal
- **Published**: April 2017
- **Authors**: Hamza Moufek, Kenza Guenda, T. Aaron Gulliver
- **PDF**: https://ieeexplore.ieee.org/document/7784752
- **Abstract**: This letter presents a new version of the McEliece cryptosystem based on quasi-cyclic (QC) low density parity check codes and QC moderate density parity check codes. A modified self-shrinking generator is used to obtain random bits, which are utilized in the cryptosystem. It is shown that this system is secure against known structural and decoding attacks.

## Toward the Prediction of Irreducible Error Floor in Space Time Trellis Code

- **Status**: ❌
- **Reason**: space time trellis code의 error floor 예측 — LDPC의 error-prone substructure 개념을 차용만, LDPC 부호/디코더 기여 아님
- **ID**: ieee:7811264
- **Type**: journal
- **Published**: April 2017
- **Authors**: Ungku Azmi Iskandar Ungku Chulan, Mardina Abdullah, Nor Fadzilah Abdullah
- **PDF**: https://ieeexplore.ieee.org/document/7811264
- **Abstract**: This letter presents a prediction algorithm that foresees the possibility of irreducible error floor for a particular design of a generator matrix G in space time trellis code. This is done without the need of complex and time-consuming simulation, which removes the demand of considerable computational resource. To note, the prediction achieves approximately 93% accuracy and reduces roughly 99% of the temporal cost of simulation. It capitalizes on error prone substructure, a well-known concept from low density parity check code to enable the predictive mechanism. This can be useful in code design where problematic generator matrices can be omitted from consideration.

## Linear network coding and parallel transmission increase fault tolerance and optical reach

- **Status**: ❌
- **Reason**: 랜덤 선형 네트워크 코딩(광 네트워크), LDPC ECC 아님
- **ID**: ieee:7901451
- **Type**: journal
- **Published**: April 2017
- **Authors**: Xiaomin Chen, Anna Engelmann, Admela Jukan +1
- **PDF**: https://ieeexplore.ieee.org/document/7901451
- **Abstract**: Modern optical network systems are evolving toward more spectral flexibility and efficiency driven by the ever-increasing need for high-speed transmission. In spectrally efficient elastic optical networks, a more integrated, fault tolerant transmission system is becoming critical, due to the accompanying optical impairments and the resulting limitations in optical reach. Previous work has addressed the issue of optical reach and transmission tolerance to faults (errors) in the physical layer by deploying various forward error correction schemes. This paper proposes a different approach, complementary to the error correction mechanisms in the physical layer. In our approach, we apply randomized linear network coding (RLNC) at the source node to encode all data in the electronic layer before all-optical transmission. To achieve fault tolerance, a coded auxiliary optical channel is used in parallel with the main path. With the auxiliary path and RLNC, as shown analytically, the system is able to use more advanced modulation formats in the main path, while being highly tolerant to bit errors and packet loss caused by optical impairments. The results show that the system can alleviate the constraints on optical transmission quality and achieve better optical reach and spectral efficiency.

## Lattice Index Codes From Algebraic Number Fields

- **Status**: ❌
- **Reason**: lattice index coding(브로드캐스트/사이드정보), LDPC ECC 기법 아님
- **ID**: ieee:7822990
- **Type**: journal
- **Published**: April 2017
- **Authors**: Yu-Chih Huang
- **PDF**: https://ieeexplore.ieee.org/document/7822990
- **Abstract**: Broadcasting K independent messages to multiple users where each user demands all the messages and already has a subset of the messages as side information is studied. Recently, Natarajan et al. proposed a novel broadcasting strategy called lattice index coding, which adopts lattices constructed over some principal ideal domains (PID) for transmission. Using the structure of lattices over PID, they showed that this scheme provides uniform side information gain for any side information configuration, a desired property which essentially guarantees a fair signal-to-noise ratio gain when normalized by the amount of information contained in side information. In this paper, we generalize this strategy to a general ring of algebraic integers, which may not be a PID. Upper and lower bounds on the side information gains for the proposed scheme constructed over some interesting classes of number fields are provided and are shown to coincide asymptotically in message rate. This generalization substantially enlarges the design space and partially includes the scheme by Natarajan et al. as a special case. Perhaps more importantly, in addition to side information gains, the proposed lattice index codes benefit from diversity gains inherent in constellations carved from number fields when used over Rayleigh fading channel. Some interesting examples are provided for which the proposed scheme allows the messages to be from the same field.

## Design of Generalized Concatenated Codes Based on Polar Codes With Very Short Outer Codes

- **Status**: ❌
- **Reason**: polar 기반 GCC 설계, 부호 비의존적이지 않고 LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:7513399
- **Type**: journal
- **Published**: April 2017
- **Authors**: Hamid Saber, Ian Marsland
- **PDF**: https://ieeexplore.ieee.org/document/7513399
- **Abstract**: We present a new design approach to construct generalized concatenated codes (GCCs) based on polar codes (PCs). It is already known that PCs can be considered as a special class of the GCCs with polar outer and inner codes. We show how density evolution (DE) can be used to develop a channel-specific method to design outer codes of length L under maximum-likelihood (ML) decoding. Once a bank of outer codes of length L and different rates have been designed, we develop a rate-allocation algorithm to allocate rates to the outer codes of the GCC with the goal of minimizing the overall block error rate for a given overall rate of K/N. To maintain the low complexity of the SC decoder, we only design very short outer codes (L ≤ 8). We show that, at this outer code length, it is possible to design GCC-PCs that can result in up to 0.5-dB coding gain while reducing decoding complexity.

## EXIT Chart-Based IRA Code Design for TDMR Turbo-Equalization System

- **Status**: ❌
- **Reason**: TDMR turbo-equalization용 IRA 코드 EXIT 설계 — 비-LDPC(IRA)+채널특이적 등화기 의존, 떼어낼 LDPC ECC 기법 약함
- **ID**: ieee:7837588
- **Type**: journal
- **Published**: April 2017
- **Authors**: Morteza Mehrnoush, xBenjamin J. Belzer, Krishnamoorthy Sivakumar +1
- **PDF**: https://ieeexplore.ieee.org/document/7837588
- **Abstract**: We present an extrinsic information transfer (EXIT) chart-based design technique for irregular repeat-accumulate (IRA) codes used in 2-D magnetic recording (TDMR) turbo-equalization systems. The channel model includes Voronoi magnetic grains, 2-D intersymbol interference (2D-ISI) and additive white Gaussian noise (AWGN). The receiver uses a 2D-ISI BCJR equalizer and an IRA decoder. For one outer equalizer-decoder iteration, we propose theory and simulation-based methods for computing EXIT curves. The simulation method calculates experimental EXIT curves for the check node decoder (CND) and the combination of the variable node decoder (VND) and an equalizer. The theoretical approach recursively calculates CND and VND Gaussian mixture model parameters in order to calculate EXIT curves. We then fit the VND and CND EXIT curves to find optimized variable node degree distributions. Simulation results show that the TDMR-optimized IRA codes achieve up to a 6.2% density increase in user bits/grain (U/G) compared with IRA codes designed for AWGN channels. The theory-based code designs achieve the same or better U/G as the simulation-based designs, but require 98% less design computation time. We also derive optimized IRA codes for iterative turbo-equalization; these codes can achieve simultaneous U/G gains and SNR savings compared with AWGN-optimized codes.

## Quasi-Universal BATS Code

- **Status**: ❌
- **Reason**: BATS/fountain erasure 네트워크 코드, degree distribution 설계로 LDPC ECC에 떼어낼 기법 없음
- **ID**: ieee:7522090
- **Type**: journal
- **Published**: April 2017
- **Authors**: Xiaoli Xu, Yong Liang Guan, Yong Zeng +1
- **PDF**: https://ieeexplore.ieee.org/document/7522090
- **Abstract**: Batched sparse (BATS) code is a class of temporal network code that achieves near-optimal tradeoff between network throughput and coding length for multi-hop erasure networks. However, the performance of the traditional BATS code degrades dramatically when the designed degree distribution does not match the actual channel condition. In this paper, we first prove that a universal degree distribution that asymptotically achieves the optimal rate for all channel rank distributions does not exist for BATS code with batch size greater than one. We then propose a quasi-universal BATS (QU-BATS) code that achieves near-optimalperformance for a range of channel conditions. This makes it suitable for use in scenarios where the end-to-end channel rank distribution is not fixed or not exactly known, e.g., in multicast or wireless transmission. In the proposed QU-BATS coding scheme, multiple degree distributions are designed, and the coded packets are generated according to different degree distributions at different transmission stages. Simulation results show that the proposed QU-BATS code strictly outperforms the fountain code and the traditional BATS codes for multihop data streaming over uncertain or time-varying network links, with lower decoding complexity.

## Error detection and correction in semiconductor memories using 3D parity check code with hamming code

- **Status**: ❌
- **Reason**: 반도체 메모리용 3D 패리티+해밍코드 EDAC — 비-LDPC 부호, 이식할 LDPC 기법 없음
- **ID**: ieee:8286516
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Shivani Tambatkar, Siddharth Narayana Menon, V. Sudarshan +2
- **PDF**: https://ieeexplore.ieee.org/document/8286516
- **Abstract**: Data stored in memory or buffer needs Error Detection And Correction (EDAC). Errors occur due to supply voltage fluctuations and/or noise due to electromagnetic interference or external radiation. These errors could be either temporary or permanent. In this paper, a EDAC method is proposed to detect and correct errors based on 3D parity check. In the encoder, the data bits are arranged in a matrix format and then parity bits are calculated for each row, column and diagonal. Errors present in parity bits are detected and corrected using Hamming code. Regeneration of data bits and Syndrome calculation at the decoder helps in detecting and correcting the error bits in the data. The 3D Parity check code can correct up to 3 bits of any combination of errors in the data and the Hamming code can correct up to 3 bits in the parity, if they occur in specific combinations. Thus, this method can detect and correct errors in both data and parity bits. This method achieves higher reliability by having a slight tradeoff in area and power consumption compared to other similar methods.

## Maximizing System Capacity Using Adaptive Coding and Modulation Techniques for Slowly Fading Channels

- **Status**: ❌
- **Reason**: 적응적 코딩/변조(ACM), convolutional+Viterbi 무선 throughput 최적화 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8359070
- **Type**: conference
- **Published**: 5-7 April 
- **Authors**: Faisal M. Alawwad, Yousef A. Al-Zahrani, Hatim M. Behairy
- **PDF**: https://ieeexplore.ieee.org/document/8359070
- **Abstract**: In this paper, an adaptive coding and modulation (ACM) technique is introduced in an attempt to maximize the channel throughout. This technique suggests five different pairs of coding and modulation techniques, starting from low modulation orders and code rates going through higher values. Simulation over additive white Gaussian noise (AWGN) of the physical layer of the system is performed using M-phase shift keying (M-PSK) modulation and convolutional codes with soft Viterbi decoding algorithm. In addition, the channel throughput for each Modulation and coding pair is obtained using specific packet retransmission mechanism. An algorithm for adaptive coding and modulation is developed and the overall throughout of the adaptive system is determined with respect to the received Eb/No values.

## Compressed Sensing Performance of Binary Matrices with Binary Column Correlations

- **Status**: ❌
- **Reason**: 압축센싱(compressed sensing)용 바이너리 측정행렬 분석 — LDPC ECC 디코더/구성 아님, 소스/측정 영역
- **ID**: ieee:7921910
- **Type**: conference
- **Published**: 4-7 April 
- **Authors**: Weizhi Lu, Tao Dai, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/7921910
- **Abstract**: This paper studies a class of binary matrices with correlations between distinct columnsequal to zero or one, which has reported comparable performance with random matrices inrecent studies of compressed sensing. For such matrix, we analyze its structure propertyand provide an improved performance estimation.

## Iterative channel detection with LDPC product code for bit patterned media recording

- **Status**: ❌
- **Reason**: BPMR용 SOVA+LDPC product code 반복검출(표준 turbo-equalization), 이식할 신규 LDPC 디코더/구성 없음
- **ID**: ieee:8007596
- **Type**: conference
- **Published**: 24-28 Apri
- **Authors**: S. Jeong, J. Lee
- **PDF**: https://ieeexplore.ieee.org/document/8007596
- **Abstract**: Because of the explosion in data growth, the requirement for storage system with high density has been increased. Bit patterned media recording (BPMR) is a candidate for the next generation magnetic systems which has many advantages to achieve recording density of 1 Tb/in2 and beyond. This paper proposes an iterative channel detection scheme with low density parity check (LDPC) product code using extrinsic information between soft output Viterbi algorithm (SOVA) and LDPC for BPMR.

## Design of LDPC codes for unequal ISI channels

- **Status**: ❌
- **Reason**: 불균등 ISI 채널에 코드워드 분할 전송(다이버시티성) 기법, 이식 가능한 디코더/구성 없음
- **ID**: ieee:8007592
- **Type**: conference
- **Published**: 24-28 Apri
- **Authors**: W. Phakphisut, P. Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/8007592
- **Abstract**: In magnetic recording system, each track or sector may suffer different distortion and noise levels, for example, media noise, intersymbol interference (ISI)/inter-track interference (ITI), reader sensitivity (in case of multi-reader), resulting in unequal error rates or unequal ISI channels. A generic scenario is considered for the multi-read system whereby tracks with different areal densities experience unequal ISI and ITI levels, hence, different targets are used. In this work, the codeword of LDPC code is divided and transmitted in the unequal ISI channels. The aim of this scheme is to avoid transmitting the whole codeword in a high error rate channel. It resembles the diversity technique in wireless communication, which transmit the information over multiple-channel by multiple-antenna. In this work, we use the unequal ISI channels.

## Non-binary protograph-based LDPC codes for 2-D ISI magnetic recording channels

- **Status**: ❌
- **Reason**: 비이진(NP-LDPC) protograph 코드, 비이진 제외
- **ID**: ieee:8007591
- **Type**: conference
- **Published**: 24-28 Apri
- **Authors**: P. Chen, K. Cai, L. Kong +2
- **PDF**: https://ieeexplore.ieee.org/document/8007591
- **Abstract**: Two dimensional (2-D) inter-symbol-interference (ISI), consisting of ISI in the down track direction and inter-track interference (ITI) along the cross-track direction, is a major factor that severely degrades the performance of ultra-high density magnetic recording systems. In this work, we propose a modified protograph extrinsic information transfer (EXIT) analysis, based on which we design novel NP-LDPC codes for 2-D ISI channels. II.

## Secure key management for 5G physical layer security

- **Status**: ❌
- **Reason**: 5G 물리계층 보안 키관리에 LDPC를 신뢰성 보장용으로 사용, 보안 응용이며 떼어낼 새 LDPC 기법 없음
- **ID**: ieee:7930246
- **Type**: conference
- **Published**: 24-25 Apri
- **Authors**: Asim Mazin, Kemal Davaslioglu, Richard D. Gitlin
- **PDF**: https://ieeexplore.ieee.org/document/7930246
- **Abstract**: Next generation 5G wireless networks pose several important security challenges. One fundamental challenge is key management between the two communicating parties. The goal is to establish a common secret key through an unsecured wireless medium. In this paper, we introduce a new physical layer paradigm for secure key exchange between the legitimate communication parties in the presence of a passive eavesdropper. The proposed method ensures secrecy via pre-equalization and guarantees reliable communications by the use of Low Density Parity Check (LDPC) codes. One of the main findings of this paper is to demonstrate through simulations that the diversity order of the eavesdropper will be zero unless the main and eavesdropping channels are almost correlated, while the probability of key mismatch between the legitimate transmitter and receiver will be low. Simulation results demonstrate that the proposed approach achieves very low secret key mismatch between the legitimate users, while ensuring very high error probability at the eavesdropper.

## Performance analysis of IEEE 802.11ac/ax WLAN technologies under the presence of CFO

- **Status**: ❌
- **Reason**: 802.11ac/ax WLAN PHY의 CFO 영향 분석, LDPC 무관 통신 응용
- **ID**: ieee:7937579
- **Type**: conference
- **Published**: 19-20 Apri
- **Authors**: Jiri Milos, Ladislav Polak, Martin Slanina
- **PDF**: https://ieeexplore.ieee.org/document/7937579
- **Abstract**: In the recent twenty years, numerous IEEE 802.11 technologies have been developed for Wireless Local Area Network (WLAN) connectivity. The common point of these technologies is that the latest IEEE 802.11 version has always several advanced features compared to its predecessor. IEEE 802.11ax is one of the upcoming technologies, primarily developed for the Industrial, Security and Medical (ISM) band. IEEE 802.11ax is planned to be released in 2019 and extend the features of IEEE 802.11ac. This paper presents a simulation-based performance analysis of the IEEE 802.11ac/ax technologies on the physical layer (PHY) level. The transmitter and receiver models of both technologies have been implemented and tested in MATLAB. Furthermore, this work explores IEEE 802.11ac/ax performance degradation that may be caused by carrier frequency offset (CFO). Results show lower resistance of IEEE 802.11ax against CFO.

## Determination of partial weight enumerators of BCH codes by Hash methods

- **Status**: ❌
- **Reason**: BCH 부호 부분 무게분포 산출(해시 가속), 비-LDPC 이론 분석으로 떼어낼 디코더·HW 없음
- **ID**: ieee:7934666
- **Type**: conference
- **Published**: 19-20 Apri
- **Authors**: My Seddiq El Kasmi Alaoui, Saïd Nouh, Abdelaziz Marzak
- **PDF**: https://ieeexplore.ieee.org/document/7934666
- **Abstract**: The PWE (Partial Weight Enumerator) algorithm permits to obtain a partial weights enumerator for linear codes. This algorithm is based on the Multiple Impulse Method combined with a Monte Carlo Method. The main disadvantage of this algorithm is the height run time complexity when the set of selected codewords as sample is large. However, when this set is reduced it becomes not representative and the quality of approximation decrease. In this paper, we will present an improved version PWEH of the PWE algorithm based on Hash techniques in order to remedy this disadvantage. The comparison between PWE and PWEH shows that the run time of this latest is reduced at more than 5100%. PWEH is validated and it is used to find an approximation of the partial weight enumerators of BCH (255,199) code where the weight distributions is still unknown.

## DaRe: Data Recovery through Application Layer Coding for LoRaWAN

- **Status**: ❌
- **Reason**: LoRaWAN 애플리케이션 계층 fountain/convolutional 데이터복구, LDPC 아님 떼어낼 ECC 기법 없음
- **ID**: ieee:7946866
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Paul J. Marcelis, Vijay S. Rao, R. Venkatesha Prasad
- **PDF**: https://ieeexplore.ieee.org/document/7946866
- **Abstract**: Internet of Things (IoT) solutions are increasingly being deployed for smart applications. To provide good communication for the increasing number of smart applications, there is a need for low cost and long range Low Power Wide Area Network (LPWAN) technologies. LoRaWAN is an energy efficient and inexpensive LPWAN solution that is rapidly being adopted all around the world. However, LoRaWAN does not guarantee reliable communication in its basic configuration. Transmitted frames can be lost due to the channel effects and mobility of the end-devices. In this study, we perform extensive measurements on a new LoRaWAN network to characterise spatial and temporal properties of the LoRaWAN channel. The empirical outage probability for the farthest measured distance from the closest gateway of 7.5km in our deployment is as low as 0.004, but the frame loss measured at this distance was up to 70%. Furthermore, we show that burstiness in frame loss can be expected for both mobile and stationary scenarios. Frame loss results in data loss, since in the basic configuration frames are only transmitted once. To reduce data loss in LoRaWAN, we design a novel coding scheme for data recovery called DaRe, which extends frames with redundant information that is calculated from the data from previous frames. DaRe combines techniques from convolutional codes and fountain codes. We develop an implementation for DaRe and show that 99% of the data can be recovered with a code rate of 1/2 for up to 40% frame loss. Compared to repetition coding DaRe provides 21% more data recovery, and can save up to 42% energy consumption on transmission for 10 byte data units. DaRe also provides better resilience to bursty frame loss. This study provides useful results to both LoRaWAN network operators as well as developers of LoRaWAN applications. Network operators can use the characterisation results to identify possible weaknesses in the network, and application developers are offered a tool to prevent possible data loss.
