# IEEE Xplore — 2021-06


## Design and Analysis of Delayed Bit-Interleaved Coded Modulation With LDPC Codes

- **Status**: ❌
- **Reason**: DBICM 변조/BICM 시스템 통신 응용 특이적 LDPC 코드 설계(PEG·EXIT, 비트채널 UEP) — NAND 채널과 무관, 떼어낼 일반 ECC 기법 없음
- **ID**: ieee:9373632
- **Type**: journal
- **Published**: June 2021
- **Authors**: Yihuan Liao, Min Qiu, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/9373632
- **Abstract**: This paper investigates the design and performance of delayed bit-interleaved coded modulation (DBICM) with low-density parity-check (LDPC) codes. For Gray labeled square M-ary quadrature amplitude modulation (QAM) constellations, we investigate the optimal delay scheme with the largest spectrum efficiency of DBICM for a fixed maximum number of delayed time slots and a given signal-to-noise ratio. When analyzing the capacity of DBICM, we find two important properties: the capacity improvement due to delayed coded bits being mapped to the real and imaginary parts of the transmitted symbols are independent of each other; a pair of delay schemes with delayed coded bits having identical bit-channel capacity lead to equivalent DBICM capacity. Using these two properties, we efficiently optimize the delay scheme for any uniform Gray-QAM systems. Furthermore, these two properties enable efficient LDPC code designs regarding unequal error protection via bit-channel type classifications. Moreover, we use protograph-based extrinsic information transfer charts to jointly optimize degree distributions and channel assignments of LDPC codes and propose a constrained progressive edge growth like algorithm to jointly construct LDPC codes and bit-interleavers for DBICM, taking distinctive bit-channel's capacity into account. Simulation results demonstrate that the designed LDPC coded DBICM systems significantly outperform LDPC coded BICM systems.

## Systematic Convolutional Low Density Generator Matrix Code

- **Status**: ❌
- **Reason**: LDGM(저밀도 생성행렬) 부호 — LDPC 패리티검사 부호가 아니라 생성행렬 부호. NAND LDPC ECC에 이식할 패리티검사/디코더 기법 없음.
- **ID**: ieee:9373435
- **Type**: journal
- **Published**: June 2021
- **Authors**: Suihua Cai, Wenchao Lin, Xinyuanmeng Yao +2
- **PDF**: https://ieeexplore.ieee.org/document/9373435
- **Abstract**: In this paper, we propose a systematic low density generator matrix (LDGM) code ensemble, which is defined by the Bernoulli process. We prove that, under maximum likelihood (ML) decoding, the proposed ensemble can achieve the capacity of binary-input output symmetric (BIOS) memoryless channels in terms of bit error rate (BER). The proof technique reveals a new mechanism, different from lowering down frame error rate (FER), that the BER can be lowered down by assigning light codeword vectors to light information vectors. The finite length performance is analyzed by deriving an upper bound and a lower bound, both of which are shown to be tight in the high signal-to-noise ratio (SNR) region. To improve the waterfall performance, we construct the systematic convolutional LDGM (SysConv-LDGM) codes by a random splitting process. The SysConv-LDGM codes are easily configurable in the sense that any rational code rate can be realized without complex optimization. As a universal construction, the main advantage of the SysConv-LDGM codes is their near-capacity performance in the waterfall region and predictable performance in the error-floor region that can be lowered down to any target as required by increasing the density of the uncoupled LDGM codes. Numerical results are also provided to verify our analysis.

## Front cover

- **Status**: ❌
- **Reason**: Front cover, 초록 없음 — 논문 아님
- **ID**: ieee:9489390
- **Type**: journal
- **Published**: June 2021
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/9489390
- **Abstract**: N/A

## Capacity Analysis and Improvement of LDM-Based Multiple-PLP Configurations in ATSC 3.0

- **Status**: ❌
- **Reason**: ATSC 3.0 LDM 다중화/용량 분석. LDPC는 부수 언급(low-rate code 제안)이고 NAND에 이식할 디코더/구성 기법 없음 — 무선 응용 특이.
- **ID**: ieee:9313035
- **Type**: journal
- **Published**: June 2021
- **Authors**: Hyeongseok Kim, Jeongchang Kim, Sung-Ik Park +3
- **PDF**: https://ieeexplore.ieee.org/document/9313035
- **Abstract**: This article analyzes the capacities of various layered-division multiplexing (LDM)-based multiple physical layer pipe (M-PLP) configurations in Advanced Television Systems Committee (ATSC) 3.0. Further, this article proposes an extended multi-layer LDM that consists of a core layer and one or more enhanced layer(s) combined with different injection levels. The proposed multi-layer LDM can be combined with time-division multiplexing (TDM) and/or frequency division multiplexing (FDM) to multiplex more than two PLPs. This article provides the structures of a transmitter and receiver for the multi-layer LDM and various M-PLP configurations based on the proposed multi-layer LDM. In addition, by extending to a multi-layer LDM, the low rate low-density parity-check (LDPC) codes are proposed to improve the transmission efficiency of an extremely robust service with lower data rate, such as robust audio, in the core layer of the multi-layer LDM. Simulation results show that the M-PLP configurations based on more than two layers can obtain the improved reception performance compared to the M-PLP configurations based on only two layers supported by the PHY standard in ATSC 3.0. However, since the performance degradation of layered time-division multiplexing (LTDM) with fewer layers is not significant compared to multi-layer LDM, LTDM can be a good solution to efficiently transmit M-PLPs.

## NoPUF: A Novel PUF Design Framework Toward Modeling Attack Resistant PUFs

- **Status**: ❌
- **Reason**: PUF 하드웨어 보안 설계, LDPC와 무관
- **ID**: ieee:9386262
- **Type**: journal
- **Published**: June 2021
- **Authors**: Antian Wang, Weihang Tan, Yuejiang Wen +1
- **PDF**: https://ieeexplore.ieee.org/document/9386262
- **Abstract**: With the rapid development and globalization of the semiconductor industry, hardware security has emerged as a critical concern. New attacking and tampering methods are continuously challenge current hardware protection methods. Combating these powerful attacks is of great importance in securing hardware devices. This paper proposes a novel framework to protect Physical Unclonable Function (PUF) against modeling attacks, denominated as Noisy PUF (NoPUF). NoPUF exploits structural unpredictability to improve overall security. We present several PUF architectures under the proposed framework that could reconfigure a conventional reliable PUF to a noisy PUF. The reconfigured PUF becomes inherently unreliable and hence achieves a higher resistance against modeling attacks. Moreover, since only a small portion of the Challenge-Response Pairs (CRPs) are required for authentication, the designer can use the information obtained from the initial reliable PUF configuration to find CRPs, which are still reliable in the noisy PUF configuration for authentication. Exploiting such information asymmetry between designer and attacker is the nexus of the proposed NoPUF design methodology. Experimental results show that we can achieve a maximum attacker and designer accuracy difference of 44.79% for a 64-stage NoPUF candidate architecture while ensuring high reliability for selected challenges.

## Low-Complexity Blind PAPR Reduction for OFDM Systems With Rotated Constellations

- **Status**: ❌
- **Reason**: OFDM PAPR 저감용 blind interleaving/회전 성상 디코더. LDPC 무관 — 무선 응용 특이.
- **ID**: ieee:9354499
- **Type**: journal
- **Published**: June 2021
- **Authors**: Tarak Arbi, Zi Ye, Benoît Geller
- **PDF**: https://ieeexplore.ieee.org/document/9354499
- **Abstract**: The high Peak-to-Average Power Ratio (PAPR) of Orthogonal Frequency Division Multiplexing (OFDM) signals leads to a serious system performance degradation. To work around this issue, several algorithms have been proposed in the literature to reduce the PAPR, but, they often suffer from multiple limitations; in particular, the main issue with interleaving techniques is the spectral efficiency loss, as the transmission of a Side Information (SI) is generally required. In contrast to previous works, this article proposes a blind interleaving technique for OFDM systems with signal space diversity. Indeed, with Rotated and Cyclically Q-Delayed (RCQD) constellations, the In-phase (I) and Quadrature (Q) components of constellations symbols are correlated, which allows the receiver to estimate the interleaver index without any SI. Moreover, to lower down the complexity burden at the receiver side, we first design a blind decoder based on the Minimum Mean Square Error (MMSE) criterion and we then propose a low complexity decoder for the Uniformly Projected RCQD (UP-RCQD) QAM, as this constellation has several interesting structural properties and achieves near optimum BER performance. Simulation results show that our proposal leads to a large PAPR reduction and to a near optimum BER performance that outperforms, over various channels, the solution currently used in DVB-T2. They also underline the good performance of the blind decoding performed with up to 98% of complexity reduction compared to the max-log Maximum Likelihood (ML) estimation.

## Polar-Coded Non-Coherent Communication

- **Status**: ❌
- **Reason**: Polar 부호 비동기 통신(SC 디코딩+채널추정). LDPC 아님, 이식할 LDPC 기법 없음.
- **ID**: ieee:9361585
- **Type**: journal
- **Published**: June 2021
- **Authors**: Peihong Yuan, Mustafa Cemil Coşkun, Gerhard Kramer
- **PDF**: https://ieeexplore.ieee.org/document/9361585
- **Abstract**: A polar-coded transmission (PCT) scheme with joint channel estimation and decoding is proposed for channels with unknown channel state information (CSI). The CSI is estimated via successive cancellation (SC) decoding and the constraints imposed by the frozen bits. SC list decoding with an outer code improves performance, including resolving a phase ambiguity when using quadrature phase-shift keying (QPSK) and Gray labeling. Simulations with 5G polar codes and QPSK show gains of up to 2 dB at a frame error rate (FER) of 10-4 over pilot-assisted transmission for various non-coherent models. Moreover, PCT performs within a few tenths of a dB to a coherent receiver with perfect CSI. For Rayleigh block-fading channels, PCT outperforms an FER upper bound based on random coding and operates within one dB of a lower bound.

## Data-Oriented View for Convolutional Coding With Adaptive Irregular Constellations

- **Status**: ❌
- **Reason**: 컨볼루션 부호+적응 불규칙 성상 단패킷 전송. LDPC 무관, 이식할 ECC 기법 없음.
- **ID**: ieee:9352771
- **Type**: journal
- **Published**: June 2021
- **Authors**: Mehmet Cagri Ilter, Risto Wichman, Jyri Hämäläinen +2
- **PDF**: https://ieeexplore.ieee.org/document/9352771
- **Abstract**: Current wireless systems offer various use-cases where conventional channel capacity focused performance criteria might not apply. Following the similar perspective, convolutional encoding can find more room due to its low complexity and low decoding delay. Besides, it has been also shown that error performance of a convolutional encoder can be improved further by using adaptive irregular constellations. A new performance measure, data-oriented approach, was recently proposed for the transmission of small data packets, i.e. mission-critical IoT applications, over fading channels. In this letter, delay performance gain resulting from convolution coding optimized irregular constellations is investigated. Then, we derive a new performance criterion based on delay and finite block length constraints. Based on this criterion, we design irregular constellations together with convolutional coding for short packet transmission.

## Reliability of Small Satellite Networks With Software-Defined Radio and Enhanced Multiple Access Protocol

- **Status**: ❌
- **Reason**: 소형 위성망 신뢰성 모델링(SDR/RA 프로토콜). LDPC ECC 기법 없음 — 네트워크 신뢰성 분석.
- **ID**: ieee:9319263
- **Type**: journal
- **Published**: June 2021
- **Authors**: Seunghwa Jung, Jihwan P. Choi
- **PDF**: https://ieeexplore.ieee.org/document/9319263
- **Abstract**: Space missions exploiting small satellite networks with a use of software-defined radio (SDR) and advanced random access (RA) protocols have attracted an increased amount of attentions given their low costs, low latency levels, low complexity, and yet competitive data rates for global network services. In this article, we derive a mathematical model to demonstrate the reliability of a small satellite network with respect to SDR structures, the transmitted signal power on the uplink/downlink channels, code rates, and packet collisions through an enhanced RA protocol. Our model provides quantitative network reliability with respect to SDR system failure rates, feasible communication parameters, and packet loss ratios. Our analysis suggests a methodology to evaluate network reliability differences according to changes of communication parameters, and a guideline to sustain a reliable network system with appropriate parameter values. We find out that a robust SDR structure with a state-of-the-art analog-to-digital converter can provide reliable network services effectively with reduced power consumption, even with high packet traffic loads, to meet operator-required reliability levels for small satellite networks.

## Secret Key Generation Over Wireless Channels using short Blocklength Multilevel Source Polar Coding

- **Status**: ❌
- **Reason**: polar 기반 비밀키 생성(보안), LDPC는 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:9415041
- **Type**: conference
- **Published**: 6-11 June 
- **Authors**: Henri Hentilä, Yanina Y. Shkel, Visa Koivunen
- **PDF**: https://ieeexplore.ieee.org/document/9415041
- **Abstract**: This paper investigates the problem of secret key generation from correlated Gaussian random variables in the short block-length regime. Inspired by the state-of-the-art performance provided by polar codes in the short blocklength regime for channel coding, we propose an explicit protocol based on polar codes for generating the secret keys. This protocol differs from previously proposed key generation protocols based on polar coding in two main ways: (i) we consider a Gaussian source for the key generation; (ii) we focus on the short block-length regime. Simulation results show that the proposed protocol performs well even for very short blocklengths, especially if one can relax the BER requirements for the generated keys. They also demonstrate that the polar code based protocol outperforms a similar one using LDPC codes in place of polar codes, and that this advantage grows the shorter the blocklength becomes.

## LDPC Coded PAM-4/8 Transmission in Fiber-FSO Link Using Unipolar Probability Distribution and Pre-distortion

- **Status**: ❌
- **Reason**: Fiber-FSO 링크 LDPC 코딩 PAM 전송 실험, 표준 LDPC 응용일 뿐 새 ECC 기법 없음
- **ID**: ieee:9489787
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Rui Zhang, Chin-Wei Hsu, Xizi Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/9489787
- **Abstract**: We experimentally demonstrated LDPC coded PAM transmission with unipolar distribution and pre-distortion in a fiber-FSO hybrid link with the parity bits inserted in the LSB. Different schemes are experimentally compared with up to 2.1-dB sensitivity improvement.

## Impact of DFE on Soft-Input LDPC Decoding for 50G PON

- **Status**: ❌
- **Reason**: DFE가 50G PON LDPC 소프트입력 디코딩에 미치는 영향 분석, 새 디코더/코드설계 기여 없는 응용 분석
- **ID**: ieee:9489713
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Amitkumar Mahadevan, Yannick Lefevre, Wouter Lanneer +4
- **PDF**: https://ieeexplore.ieee.org/document/9489713
- **Abstract**: DFE induced error correlation and mutual information (MI) degradation penalize the 50G PON LDPC code soft-input decoding performance. Bit-interleaving across multiple codewords mitigates the correlated error penalty, but not the MI degradation penalty.

## Adaptive Modulation and Coding Scheme in Coherent PON for Enhanced Capacity and Rural Coverage

- **Status**: ❌
- **Reason**: coherent-PON 적응변조에 표준 shortened LDPC 적용, 새 LDPC 기여 없음 (응용 특이적)
- **ID**: ieee:9489586
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Mu Xu, Haipeng Zhang, Zhensheng Jia +1
- **PDF**: https://ieeexplore.ieee.org/document/9489586
- **Abstract**: An adaptive coded-modulation approach combining QAM and shortened LDPC is proposed in coherent-PON architecture. The BER performance was experimentally verified and network simulations using operator data indicated in-average 40.2% increased capacity and 47.6% improved coverage.

## Performance Improvements in Bandwidth-Limited and Digitally-Equalized 50G-PON Downstream Transmission via Block-Interleaving over Four LDPC Codewords

- **Status**: ❌
- **Reason**: 50G-PON 전송에서 LDPC 코드워드 간 블록 인터리빙, 통신응용 특이적이며 떼어낼 새 ECC 기법 없음
- **ID**: ieee:9489643
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Xiang Liu, Andy Shen, Ning Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/9489643
- **Abstract**: We experimentally quantify the performance improvements in bandwidth-limited 50G-PON downstream transmission with receiver-side equalization based on FFE, DFE and MLSE, by bit-interleaving of every four adjacent LDPC codewords, achieving 32-dB power budget with additional margins.

## Direct-Detection Based Frequency-Resolved I/Q Imbalance Calibration for Coherent Optical Transmitters

- **Status**: ❌
- **Reason**: coherent 광송신기 I/Q 불균형 보정, LDPC와 무관
- **ID**: ieee:9489761
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Xi Chen, Di Che
- **PDF**: https://ieeexplore.ieee.org/document/9489761
- **Abstract**: We propose a method for calibrating the frequency dependent I/Q imbalance in coherent optical transmitters. We demonstrate that with our calibration, the OSNR penalty of a 58-GBaud 256-QAM signal can be reduced by 2.5 dB.

## Achievable Rate Comparison between Probabilistically-Shaped Single-Carrier and Entropy-Loaded Multi-Carrier Signaling in a Bandwidth-Limited 1-Tb/s Coherent System

- **Status**: ❌
- **Reason**: 코히어런트 시스템 SC/MC 신호 비교; LDPC ECC 기법 없음, 변조/엔트로피 로딩 주제
- **ID**: ieee:9489853
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Di Che, Xi Chen
- **PDF**: https://ieeexplore.ieee.org/document/9489853
- **Abstract**: Multicarrier modulation can use entropy loading to adapt a frequency-dependent channel. We compare single- and multi-carrier (SC/MC) signaling in a 100-GBaud coherent system whose performance is mainly degraded by the bandwidth-limited transmitter, and reveal an MC advantage of 0.3 bits/symbol or 20-km reach extension over a single-span transmission.

## 100 Gbit/s PAM-16 Transmission in the 2-µm Band over a 1.15-km Hollow-Core Fiber

- **Status**: ❌
- **Reason**: 홀로코어 광섬유 PAM-16 전송 실험; LDPC/ECC 기법 없음, 떼어낼 디코더·코드설계 없음
- **ID**: ieee:9489794
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Deming Kong, Zhengqi Ren, Yongmin Jung +6
- **PDF**: https://ieeexplore.ieee.org/document/9489794
- **Abstract**: We demonstrate the first low-latency 2-µm-band PAM signal transmission using a hollow-core fiber (HCF). PAM-8 and PAM-16 signals are successfully transmitted over 1.15-km HCF with line rates of 96 Gbit/s and 100 Gbit/s, respectively.

## Optimizations of Probabilistic Constellation Shaping Superposition Schemes for the MISO Visible Light Communication System

- **Status**: ❌
- **Reason**: VLC 확률적 성상 정형(PCS) 기법; ECC/LDPC 디코더·코드설계 기여 없음
- **ID**: ieee:9489807
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Peng Zou, Junwen Zhang, Guoqiang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/9489807
- **Abstract**: Two probabilistic-constellation-shaping (PCS) superposition schemes are proposed in the multi-input-single-output (MISO) visible-light-communication (VLC) system. Performance optimizations of 2.3Gbps MISO-VLC using global and local PCS superposition schemes are experimentally demonstrated in linear and nonlinear operation ranges.

## Demonstration of 28-GHz Band Radio Signal Transmission into Vehicle by Analog Radio over Multi-Mode Fiber

- **Status**: ❌
- **Reason**: 28GHz 무선신호 차량내 전송 데모; ECC/LDPC 관련 기법 전무
- **ID**: ieee:9489971
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Hiroki Yasuda, Toshinori Suzuki, Hsuan-Yun Kao +10
- **PDF**: https://ieeexplore.ieee.org/document/9489971
- **Abstract**: We demonstrate transmitting 28-GHz band radio signals from cascaded IFoF based C-RAN mobile fronthaul system to inside a vehicle by re-radiation of the cost-effective analog radio over multi-mode fiber employing a directly modulated VCSEL.

## 465 Gbps Single Side Band Direct Detection Transmission over 40 km of SSMF using a Single-ended Photodiode

- **Status**: ❌
- **Reason**: SSB 직접검파 전송 적응 알고리즘, ECC/LDPC 무관
- **ID**: ieee:9489783
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Son Thai Le, Karsten Schuh
- **PDF**: https://ieeexplore.ieee.org/document/9489783
- **Abstract**: We propose a novel adaptive algorithm to mitigate simultaneously the O/E front-end response and the SSBI in SSB direct detection transmissions and demonstrate a net data rate of 465 Gb/s over 40 km of SSMF using a single-ended photodiode.

## Long-Haul WDM/SDM Transmission over Coupled 4-Core Fiber with Coupled 4-Core EDFA and Its MDL Characteristics Estimation

- **Status**: ❌
- **Reason**: WDM/SDM 광전송 실험, FEC 언급뿐 새 디코더/코드설계 기법 없음
- **ID**: ieee:9489538
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: Manabu Arikawa, Kohei Hosokawa, Kazunori Hayashi
- **PDF**: https://ieeexplore.ieee.org/document/9489538
- **Abstract**: We demonstrated WDM/SDM transmission of 32-Gbaud PDM-QPSK over coupled 4-core fibers and EDFAs with error-free after FEC for up to 2400 km. We estimated that rms MDL of 1.1 dB per loop was limiting performance.

## About Some Irregular Degree Distributions of LDPC Codes in Two-State Channels

- **Status**: ❌
- **Reason**: Gilbert-Elliott 채널 메모리 전용 degree distribution 최적화 + 표준 BP - NAND에 이식할 새 디코더/구성 없음
- **ID**: ieee:9470627
- **Type**: conference
- **Published**: 31 May-4 J
- **Authors**: A. A. Ovchinnikov, A. A. Fominykh
- **PDF**: https://ieeexplore.ieee.org/document/9470627
- **Abstract**: The paper examines the decoding of low-density parity-check codes in channels with memory. Exact degree distributions optimized for a set of parameters of Gilbert and Gilbert-Elliott channels are given. The decoding performance of low-density parity-check codes constructed using obtained degree distributions are presented under belief propagation decoding over Gilbert-Elliott channel.

## On the Question of the Resistance of Code-Based Cryptosystems to Matrix Density Reduction Attacks

- **Status**: ❌
- **Reason**: 코드기반 암호시스템의 행렬밀도 감소 공격 분석(보안/암호); 떼어낼 ECC 디코더/코드설계 기여 없음
- **ID**: ieee:9470506
- **Type**: conference
- **Published**: 31 May-4 J
- **Authors**: V. A. Veselova, A. A. Ovchinnikov, A. M. Veresova
- **PDF**: https://ieeexplore.ieee.org/document/9470506
- **Abstract**: Methods for reducing the density of matrices are discussed. These methods can be used to analyze the cryptocomplexity of systems based on error-correcting codes. Lowering the density of matrices can affect both the stability of systems that use low-density codes as a private key, and the stability of general systems in which decryption requires solving the problem of decoding errors of a given multiplicity. The article presents the results of experiments for the considered methods of reducing the density.

## Coding for Distributed Multi-Agent Reinforcement Learning

- **Status**: ❌
- **Reason**: 분산 RL straggler 완화용 coding, 표준 regular LDPC를 그대로 사용 - 새 ECC 기여 없음
- **ID**: ieee:9561645
- **Type**: conference
- **Published**: 30 May-5 J
- **Authors**: Baoqian Wang, Junfei Xie, Nikolay Atanasov
- **PDF**: https://ieeexplore.ieee.org/document/9561645
- **Abstract**: This paper aims to mitigate straggler effects in synchronous distributed learning for multi-agent reinforcement learning (MARL) problems. Stragglers arise frequently in a distributed learning system, due to the existence of various system disturbances such as slow-downs or failures of compute nodes and communication bottlenecks. To resolve this issue, we propose a coded distributed learning framework, which speeds up the training of MARL algorithms in the presence of stragglers, while maintaining the same accuracy as the centralized approach. As an illustration, a coded distributed version of the multi-agent deep deterministic policy gradient (MADDPG) algorithm is developed and evaluated. Different coding schemes, including maximum distance separable (MDS) code, random sparse code, replication-based code, and regular low density parity check (LDPC) code are also investigated. Simulations in several multi-robot problems demonstrate the promising performance of the proposed framework.

## Multiuser Detection of an Uplink MU-Large Scale MIMO OFDM using Radial Basis Function

- **Status**: ❌
- **Reason**: MU MIMO OFDM 다중사용자 검출(RBF/MMSE) — LDPC 무관, 무선 검출기
- **ID**: ieee:9484951
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: Shefin Shoukath, Haris. P. A
- **PDF**: https://ieeexplore.ieee.org/document/9484951
- **Abstract**: Multiuser Large Scale MIMO OFDM technique helps to attain the demands of high data rate in wireless communication. Large Scale MIMO elevates the diversity and enables to reduce the fading effects occurring in communication. Multiuser detectors detect the uplink transmitted signals by users in Large scale MIMO OFDM and effectively reduces the interferences among users in wireless environment. The multiuser detection is analysed by cumulative distribution function by varying the number of detector terminals. The detection is done by the Minimum Mean Square Error detector and its performance is evaluated with nonlinear Radial Basis Function detector. The performance of the multiuser detectors are analysed by bit error rate and spectral efficiency.

## CRC Codes as Error Correction Codes

- **Status**: ❌
- **Reason**: CRC를 GRAND로 ECC화 — 비-LDPC 부호이고 GRAND는 단블록 부호용, 바이너리 LDPC BP에 이식되는 기법 아님
- **ID**: ieee:9500279
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Wei An, Muriel Médard, Ken R. Duffy
- **PDF**: https://ieeexplore.ieee.org/document/9500279
- **Abstract**: CRC codes have long since been adopted in a vast range of applications. The established notion that they are suitable primarily for error detection can be set aside through use of the recently proposed Guessing Random Additive Noise Decoding (GRAND). Hard-detection (GRAND-SOS) and soft-detection (ORBGRAND) variants can decode any short, high-rate block code, making them suitable for error correction of CRC-coded data. When decoded with GRAND, short CRC codes have error correction capability that is at least as good as popular codes such as BCH codes, but with no restriction on either code length or rate.The state-of-the-art CA-Polar codes are concatenated CRC and Polar codes. For error correction, we find that the CRC is a better short code than either Polar or CA-Polar codes. Moreover, the standard CA-SCL decoder only uses the CRC for error detection and therefore suffers severe performance degradation in short, high rate settings when compared with the performance GRAND provides, which uses all of the CA-Polar bits for error correction.Using GRAND, existing systems can be upgraded from error detection to low-latency error correction without re-engineering the encoder, and additional applications of CRCs can be found in IoT, Ultra-Reliable Low Latency Communication (URLLC), and beyond. The universality of GRAND, its ready parallelized implementation in hardware, and the good performance of CRC as codes make their combination a viable solution for low-latency applications.

## End-to-end 140 GHz Wireless Link Demonstration with Fully-Digital Beamformed System

- **Status**: ❌
- **Reason**: 140GHz 무선 링크 데모 — LDPC/ECC 기법 없음
- **ID**: ieee:9473600
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Shadi Abu-Surra, Wonsuk Choi, Sungtae Choi +11
- **PDF**: https://ieeexplore.ieee.org/document/9473600
- **Abstract**: It is projected that mobile traffic will increase by 80x by year 2030. To meet this increase in demand, it is inevitable to utilize the terahertz bands (0.1 THz to 10 THz) for future 6G wireless systems. However, operating at such high frequency comes with several fundamental and technical challenges. In this work, we present a proof-of-concept system to demonstrate the feasibility of establishing a communication link at 140 GHz carrier frequency. In addition, this work highlights techniques to tackle the challenges that comes with operating in the terahertz regime. To the authors knowledge, this is the world’s first end-to-end system with up to 16-channel digitally-beamformed 140 GHz system and dynamic beam steering capability. The paper presents lab results which demonstrate link throughput of 6 Gbps at 15-meter distance with adaptive beamforming.

## Field Experiment of 117 Gbit/s Wireless Transmission Using OAM Multiplexing at a Distance of 200 m on 40 GHz Band

- **Status**: ❌
- **Reason**: OAM 다중화 무선 전송 데모 — LDPC/ECC 무관
- **ID**: ieee:9473649
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Yasunori Yagi, Hirofumi Sasaki, Tomoki Semoto +4
- **PDF**: https://ieeexplore.ieee.org/document/9473649
- **Abstract**: In this paper, we demonstrate outdoor wireless transmission using orbital angular momentum (OAM) multiplexing on a 40 GHz band. OAM beams are generated by a Butler matrix analog radio-frequency (RF) circuit and radiated from uniform circular arrays (UCAs). We implemented an OAM multiplexing transmitter (Tx) and receiver (Rx) on a 40-GHz band. This Tx and Rx can generate and separate seven OAM modes (−3, −2, −1, 0, 1, 2, 3) and two polarizations (vertical and horizontal), a total of 15 streams, including the center antenna element which can transmit OAM mode 0. Each channel carries a 1.5 Gbaud signal. We previously reported a 119 Gbit/s transmission at a distance of 100 m using this equipment. This time, we used signal processing with transmit precoding based on singular value decomposition (SVD) to achieve a greater transmission distance. Then, we evaluated the transmission capacity at distances of 100 m and 200 m. The results show that a 137 Gbit/s wireless data transmission is successful at a distance of 100 m and a 117 Gbit/s wireless data transmission is successful at a distance of 200 m.

## Supporting More Active Users for Massive Access via Data-assisted Activity Detection

- **Status**: ❌
- **Reason**: mMTC grant-free 랜덤액세스 활성사용자/데이터 검출. ECC 코드설계·디코더 신규 기여 없음, 무선 응용 특이적
- **ID**: ieee:9500797
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Xinyu Bian, Yuyi Mao, Jun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/9500797
- **Abstract**: Massive machine-type communication (mMTC) has been regarded as one of the most important use scenarios in the fifth generation (5G) and beyond wireless networks, which demands scalable access for a large number of devices. While grant-free random access has emerged as a promising mechanism for massive access, its potential has not been fully unleashed. Particularly, the two key tasks in massive access systems, namely, user activity detection and data detection, were handled separately in most existing studies, which ignored the common sparsity pattern in the received pilot and data signal. Moreover, error detection and correction in the payload data provide additional mechanisms for performance improvement. In this paper, we propose a data-assisted activity detection framework, which aims at supporting more active users by reducing the activity detection error, consisting of false alarm and missed detection errors. Specifically, after an initial activity detection step based on the pilot symbols, the false alarm users are filtered by applying energy detection for the data symbols; once data symbols of some active users have been successfully decoded, their effect in activity detection will be resolved via successive pilot interference cancellation, which reduces the missed detection error. Simulation results show that the proposed algorithm effectively increases the activity detection accuracy, and it is able to support ∼20% more active users compared to a conventional method in some sample scenarios.

## Radio Environment Map Enhanced Intelligent Reflecting Surface Systems Beyond 5G

- **Status**: ❌
- **Reason**: IRS 채널 예측 무선 시스템 — LDPC/ECC 무관
- **ID**: ieee:9473634
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Kai Zhang, Jian Zhao, Pei Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9473634
- **Abstract**: The Sub-6GHz spectrum is crucial for outdoor coverage in the fifth generation (5G) mobile communication systems. Considering the typical urban outdoor environment, one of the fundamental challenges for Sub-6GHz system is its susceptibility to occlusion effects. One way to alleviate this influence is to establish another line of sight link by using an intelligent reflecting surface (IRS). Nevertheless, the performance degradation due to the delay and overhead of the channel feedback can not be neglected. To address this issue, in this paper we propose a radio environment map (REM) based method for occlusion and channel prediction to reduce the delay and overhead. Based on the image information captured by the REM constructor, the user equipments’ (UEs’) location at the next moment are predicted firstly. Then we make prediction for occlusion and channel condition and determine the transmission mode (TM) for each UE. Finally, the optimal phase is obtained by solving a phase optimization problem under a given TM selection matrix constraint. Compared to the state-of-the-art approaches, simulation results show that our proposed method significantly improve the link reliability and energy efficiency.

## Extrinsic Neural Network Equalizer for Channels with High Inter-Symbol-Interference

- **Status**: ❌
- **Reason**: 신경망 ISI 이퀄라이저(ExNE). 채널 이퀄라이제이션 NN이며 LDPC 디코더 자체 기법 아님, NAND 이식성 약함
- **ID**: ieee:9500903
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Xiang Huang, Joohyun Cho, Kazem Hashemizadeh +1
- **PDF**: https://ieeexplore.ieee.org/document/9500903
- **Abstract**: In this paper, we propose a novel extrinsic neural network equalizer (ExNE) for joint iterative equalization and decoding. The proposed ExNE takes the received signal sequence and a priori probabilities from the channel decoder as inputs to directly generate output extrinsic probabilities. This approach improves the performance of iterative equalization and decoding by making explicit use of extrinsic information. A three-step, open-loop neural network (NN) training procedure is developed for the ExNE, independent of the choice of channel code. We propose a new NN architecture termed deep concatenated convolutional blocks with skip connections (DCCB-SC) for ExNE which attains excellent performance with only a moderate number of network parameters. For challenging linear and non-linear inter-symbol-interference (ISI) channels considered in this work, the proposed ExNE approaches the performance of the maximum a posteriori probability (MAP) equalizer without assuming prior knowledge of the channel model.

## Massive Gaussian Multiple-Access by Random Coding With Soft Interference Cancellation

- **Status**: ❌
- **Reason**: 가우시안 랜덤부호 다중접속 유한길이 이론 분석/soft IC. LDPC 디코더·구성 신규 기여 없는 무선 이론
- **ID**: ieee:9500907
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Ralf R. Müller
- **PDF**: https://ieeexplore.ieee.org/document/9500907
- **Abstract**: We utilize recent results on the exact block error probability of Gaussian random codes in additive white Gaussian noise to analyze Gaussian random coding for massive multiple-access at finite message length. Soft iterative interference cancellation is found to closely approach the performance bounds recently found in [1]. The existence of two fundamentally different regimes in the trade-off between power and bandwidth efficiency reported in [2] is related to much older results in [3] on power optimization by linear programming. Furthermore, we tighten the achievability bounds of [1] in the low power regime and show that orthogonal constellations are very close to the theoretical limits for message lengths around 100 and above.

## Receiver Signal Processing for 50Gbit/s Passive Optical Networks

- **Status**: ❌
- **Reason**: 50Gbit/s PON 수신기 디지털 이퀄라이제이션. soft decision 디코딩은 베이스라인일 뿐 LDPC 신규 기법 없음
- **ID**: ieee:9500946
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Rainer Strobel
- **PDF**: https://ieeexplore.ieee.org/document/9500946
- **Abstract**: Increasing bandwidth requirements for home and business Internet connections as well as fiber links for 5G wireless drive the need for higher data rate passive optical networks (PON). PON is a cost-effective way to deploy fiber. A point-to-multipoint topology with passive optical splitters is used to connect many subscribers to one central node. The next development step in PON is 50 Gbit/s per wavelength, which requires improvements in error correction coding and receiver signal processing. This paper investigates digital equalization for PON with respect to performance with soft decision error correction decoding.

## Signals With Sparse Mutual Interference for Sounding Massive MIMO Channels

- **Status**: ❌
- **Reason**: Massive MIMO 사운딩 참조신호 설계 — LDPC/ECC 무관
- **ID**: ieee:9500454
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Branislav M. Popovic, Peng Wang, Fredrik Berggren
- **PDF**: https://ieeexplore.ieee.org/document/9500454
- **Abstract**: In this paper, we propose a set of new sounding reference signals (SRSs) for time-division duplexing (TDD) massive MIMO systems with channel aging. It is analytically shown that the proposed set of SRSs exhibit superior zero correlation zone (ZCZ) property, which guarantees sparse and marginal interference between each other. Therefore, all SRSs in the set can be transmitted concurrently in a cell with a short SRS period per user to alleviate the channel aging effect. We also investigate the detailed SRS construction to achieve low peak-to-average power ratios (PAPRs). Finally, simulation results are provided to show that the proposed SRSs result in significantly larger downlink throughput than the existing 5G New Radio SRSs.

## LDPC Codes with Soft Interference Cancellation for Uncoordinated Unsourced Multiple Access

- **Status**: ❌
- **Reason**: 폴라 외부부호를 LDPC+BP로 교체한 무선 비조정 다중접속(UMA) 응용. density evolution은 표준 수준이고 떼어낼 신규 NAND LDPC 기법 없음
- **ID**: ieee:9500486
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Asit Kumar Pradhan, Vamsi K. Amalladinne, Krishna R. Narayanan +1
- **PDF**: https://ieeexplore.ieee.org/document/9500486
- **Abstract**: This article presents a novel enhancement to the random spreading based coding scheme developed by Pradhan et al. for the unsourced multiple access channel. The original coding scheme features a polar outer code in conjunction with a successive cancellation list decoder (SCLD) and a hard-input soft-output MMSE estimator. In contrast, the proposed scheme employs a soft-input soft-output MMSE estimator for multi-user detection. This is accomplished by replacing the SCLD based polar code with an LDPC code amenable to belief propagation decoding. This novel framework is leveraged to successfully pass pertinent soft information between the MMSE estimator and the outer code. LDPC codes are carefully designed using density evolution techniques to match the iterative process. This enhanced architecture exhibits significant performance improvements and represents the state-of-the-art over a wide range of system parameters.

## Deep Joint Source Channel Coding for Wireless Image Transmission with OFDM

- **Status**: ❌
- **Reason**: 딥러닝 JSCC 무선 이미지 전송. LDPC는 비교 베이스라인, 떼어낼 ECC 기법 없음(JSCC 제외 규칙)
- **ID**: ieee:9500996
- **Type**: conference
- **Published**: 14-23 June
- **Authors**: Mingyu Yang, Chenghong Bian, Hun-Seok Kim
- **PDF**: https://ieeexplore.ieee.org/document/9500996
- **Abstract**: We present a deep learning based joint source channel coding (JSCC) scheme for wireless image transmission over multipath fading channels with non-linear signal clipping. The proposed encoder and decoder use convolutional neural networks (CNN) and directly map the source images to complex-valued baseband samples for orthogonal frequency division multiplexing (OFDM) transmission. The proposed model-driven machine learning approach eliminates the need for separate source and channel coding while integrating an OFDM datapath to cope with multipath fading channels. The end-to-end JSCC communication system combines trainable CNN layers with non-trainable but differentiable layers representing the multipath channel model and OFDM signal processing blocks. Our results show that injecting domain expert knowledge by incorporating OFDM baseband processing blocks into the machine learning framework significantly enhances the overall performance compared to an unstructured CNN. Our method outperforms conventional schemes that employ state-of-the-art but separate source and channel coding such as BPG and LDPC with OFDM. Moreover, our method is shown to be robust against non-linear signal clipping in OFDM for various channel conditions that do not match the model parameter used during the training.

## Evaluation of 5G channel coding technology: for the mMTC scenario

- **Status**: ❌
- **Reason**: 5G mMTC Polar vs LDPC 표준 디코더(MSA/LLR-BP) 비교 평가, 신규 디코더/구성 없음
- **ID**: ieee:9644511
- **Type**: conference
- **Published**: 11-13 June
- **Authors**: Yangyang Zhou, Yaoshan Miao, Meng Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9644511
- **Abstract**: Channel coding technology can provide reliable data transmission for communication systems in complex environments and is a key technology in 5G communication systems. However, channel coding technology in 5G-mMTC scenario is still waiting to be explored. The purpose of this paper is to compare and study which decoding scheme of Polar code and LDPC code is more suitable for the mMTC scenario. The technical evaluation is done by using the BPSK modulation method in the AWGN channel with a code rate of 0.5 to evaluate the error correction performance of the candidate coding technology in the case of short and medium codes. LDPC codes use a minimum sum algorithm (MSA) and LLR belief propagation algorithm (LLR-BP) as decoding schemes, and their iterations are 20. Polar codes adopt Fast-SCL algorithm assisted by CRC as decoding schemes, and Its list sizes are set to 4 and 8. The comparative analysis shows that the Fast-SCL has good error correction performance and the lowest computational complexity among all the candidate schemes. In addition, we also verified that Fast-SCL has a similar error correction performance to CA-SCL.

## Optimization of non-binary LDPC coded massive MIMO systems with partial mapping and EP detection

- **Status**: ❌
- **Reason**: 비이진(GF) LDPC coded MIMO — 비이진 LDPC 제외(규칙 0)
- **ID**: ieee:9511526
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Zhijie Feng, Qingqing Liu, Jin Xu +4
- **PDF**: https://ieeexplore.ieee.org/document/9511526
- **Abstract**: In this work, a non-binary low density parity check (LDPC) coded high dimensional multiple input multiple output (MIMO) scheme with partial mapping for high order modulation is proposed. For the proposed scheme, when $M$ -ary quadrature amplitude modulation (QAM) is employed, then non-binary LDPC code constructed over Galois field with order $\sqrt{M}$ is used for partial mapping, where $\sqrt{M}$ is an integer. At the receiver side, a real-valued expectation propagation (REP) based detection algorithm is used. Furthermore, symbol-wise extrinsic information transfer (SEXIT) chart based iterative optimization algorithm is used to optimize the concatenated non-binary LDPC code. A simplified method is proposed to calculate the component EXIT chart of the massive MIMO detector, which can avoid a large amount of simulations. Numerical simulation results demonstrate the validity of the above idea.

## High-Throughput Visual MIMO Systems for Screen-Camera Communications

- **Status**: ❌
- **Reason**: 스크린-카메라 VLC 시스템, 비이진 채널코딩 언급에 그치고 이식 가능한 LDPC 기법 없음
- **ID**: ieee:9018149
- **Type**: journal
- **Published**: 1 June 202
- **Authors**: Takuya Fujihashi, Toshiaki Koike-Akino, Philip V. Orlik +1
- **PDF**: https://ieeexplore.ieee.org/document/9018149
- **Abstract**: Screen-camera communications, using a liquid crystal display (LCD) screen and camera image sensors, have been attractive variants of visible light communications (VLC) since any external light-emitting modules and photo detectors are required for recent mobile devices, which are usually equipped with display and camera. A major issue in screen-camera communications is a performance loss in transmission rate due to nonlinear channel impairments with ambient noise. To improve transmission rates, we investigate the impact of nonlinear channel equalization, nonbinary channel coding, probabilistic shaping, and nonlinear precoding for high-order modulation schemes. Experimental evaluations using an LCD screen and camera demonstrate that our proposed scheme achieves 3.8-3.3 times higher transmission rates compared to existing schemes for a communication distance of 60-160 cm.
