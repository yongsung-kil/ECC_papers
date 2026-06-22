# IEEE Xplore — 2021-07


## Shortening for LDPC-Coded Multi-User Systems

- **Status**: ❌
- **Reason**: LDPC 멀티유저 GMAC용 shortening 패턴 최적화(EXIT 기반) — 다중접속 응용 특이적, NAND ECC 이식 기법 약함
- **ID**: ieee:9386076
- **Type**: journal
- **Published**: July 2021
- **Authors**: Na Gao, Yin Xu, Yihang Huang +4
- **PDF**: https://ieeexplore.ieee.org/document/9386076
- **Abstract**: This letter explores shortening technology for achieving near Gaussian multiple access channel (GMAC) capacity in low-density parity-check coded multi-user systems. To optimize the shortening patterns, a hybrid extrinsic information transfer (H-EXIT) tool, which integrates EXIT and protograph-based EXIT, is firstly developed. Based on this analysis, H-EXIT priority (HEP) algorithm is proposed to facilitate the optimization of shortening patterns. It can be observed that columns with larger degrees are prior to be selected, which differs from those for point-to-point scenarios. Inspired by this finding, we further propose largest-column-degree priority (LCDP) algorithm, which narrows the selection space to lower the complexity while maintains a comparable performance. Extensive simulation results demonstrate the superiority of proposed shortening schemes from two aspects: 1) Proposed shortening can bring nonnegligible gain over unshortening with consistent sum rate; 2) HEP and LCDP algorithms outperform benchmark algorithms.

## Self-Corrected Belief-Propagation Decoder for Source Coding With Unknown Source Statistics

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스 코딩용 SC-BP 디코더 - 소스 코딩 영역이며 채널 ECC 아님(제외 카테고리: 소스 코딩)
- **ID**: ieee:9411898
- **Type**: journal
- **Published**: July 2021
- **Authors**: Elsa Dupraz, Mohamed Yaoumi
- **PDF**: https://ieeexplore.ieee.org/document/9411898
- **Abstract**: This letter describes a practical Slepian-Wolf source coding scheme based on Low Density Parity Check (LDPC) codes. It considers the realistic setup where the parameters of the statistical model between the source and the side information are unknown. A novel Self-Corrected Belief-Propagation (SC-BP) algorithm is proposed in order to make the coding scheme robust to incorrect model parameters by introducing some memory inside the LDPC decoder. A Two Dimensional Density Evolution (2D-DE) analysis is then developed to predict the theoretical performance of the SC-BP decoder. Both the 2D-DE analysis and Monte-Carlo simulations confirm the robustness of the SC-BP decoder. The proposed solution allows for an important complexity reduction and shows a performance very close to existing methods which jointly estimate the model parameters and the source sequence.

## Probabilistic Shaping for Protograph LDPC-Coded Modulation by Residual Source Redundancy

- **Status**: ❌
- **Reason**: protograph LDPC 확률적 셰이핑(PAS)+소스 잔여중복 — JSCC/변조 셰이핑, ECC 디코더 이식 기법 없음
- **ID**: ieee:9395483
- **Type**: journal
- **Published**: July 2021
- **Authors**: Chen Chen, Qiwang Chen, Lin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/9395483
- **Abstract**: Probabilistic amplitude shaping (PAS) has proved to be a promising way to achieve the shaping gain for an additive white Gaussian noise channel with a distribution matcher (DM). However, the DM schemes may suffer a rate loss and increase both complexity and latency, when they are not suited for the input bit stream with redundancy. In this paper, a novel PAS strategy is proposed for a joint source and channel coded modulation system, where the residual source redundancy after source coding can be exploited to obtain both shaping and coding gains. It is shown that the residual source redundancy can be controlled by choosing the row weight distribution for source code, thus making the probability distribution of the modulated symbols be optimized under an appropriate interleaver design. To guarantee the error-floor performance, the source code is constrained by predicting the probability distribution of source bits within target finite-length frames. By jointly designing source and channel codes, the residual source redundancy can also be exploited to achieve the coding gain. Compared with the state-of-the-art code pairs, the proposed code pairs have better error-floor performance, and achieve higher coding and shaping gains without suffering from the rate-loss and the latency caused by DM.

## Low-Density Parity-Check Coded Direct Sequence Spread Spectrum Receiver Based on Analog Probabilistic Processing

- **Status**: ❌
- **Reason**: 위성통신 DS-SS LDPC 아날로그 수신기 - 응용 특이적이며 이식 가능 ECC 기법은 표준 LDPC 디코딩 수준(아날로그 구현은 NAND와 무관)
- **ID**: ieee:9444629
- **Type**: journal
- **Published**: July 2021
- **Authors**: Xuhui Ding, Jianping An, Zhe Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/9444629
- **Abstract**: Forward error correction (FEC) coding is an indispensable technique in the direct sequence spread spectrum (DS-SS) systems for satellite communication applications. Both the FEC and DS-SS can be regarded as specific cases of probabilistic computing based on analog circuits, which is expected to be a promising solution for power-limited scenarios. The combination of FEC and DS-SS techniques can provide sufficient link margin and robustness for communication systems. In this paper, a probabilistic receiver chain for the Low-Density Parity-Check (LDPC) coded DS-SS system is proposed. Generically, an $m$-sequence can be regarded as a codeword of cyclic linear codes. Similar to the decoding procedure of LDPC codes, the joint detection and decoding process of $m$-sequences can be performed by factor graph-based iterative message-passing algorithms (iMPAs). In terms of the iterative signal processing, we first present an improved approach of iterative stopping criterion which can reduce the average number of iteration by 90% for the LDPC decoding approach. Furthermore, a joint detection and decoding method is developed to provide quick synchronization of the $m$-sequence. Meanwhile, stopping criterion-based iMPAs are especially suitable for analog implementation with low complexity. Finally, cascading to the analog LDPC decoder, the implementation of the $m$-sequence detector is designed. The prototyping chip is fully integrated into a 0.35-$\mu\text{m}$ CMOS technology, which can achieve higher throughput than 3 ${\textbf {Gcps}}$ with a core chip area of 2.79 ${\textbf {mm}}^2$ and power consumption of 6.99 ${\textbf {mW}}$ for its core circuit. Experimental results demonstrate the effectiveness of our proposed receiver mechanism.

## Improving the Tradeoff Between Error Correction and Detection of Concatenated Polar Codes

- **Status**: ❌
- **Reason**: 연접 polar 코드 SCL 디코딩 오류검출/정정 트레이드오프 — polar 전용, LDPC ECC 이식 기법 없음
- **ID**: ieee:9393971
- **Type**: journal
- **Published**: July 2021
- **Authors**: Min Jang, Joohyun Lee, Sang-Hyo Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/9393971
- **Abstract**: Concatenated polar codes under successive cancellation list (SCL) decoding have excellent error-correction performance. However, their expected error-detection capability becomes degraded, when we increase the list size of the SCL decoder in order to improve their error-correction performance. In this paper, we propose a configuration design scheme for the SCL decoder and a post-decoding validation check scheme in order to provide a better tradeoff between error-detection and error-correction performance. Firstly, a configuration of the SCL decoder is designed to improve its own error detection capability. Specifically, a part of dynamic frozen bits (also called parity-check bits) is used for path checking during SCL decoding rather than their original purpose of use, path pruning. Furthermore, the number of paths to be checked by the applied cyclic redundancy check (CRC) code is limited. Secondly, a new metric corresponding to the correlation between the received signal vector and the decoded one is presented to check the validity of the decoding result. These proposed schemes are analyzed to provide a proper configuration of the SCL decoder and determine a threshold for post-decoding validation check. Numerical results show that a better tradeoff between error correction and detection is achieved, compared with conventional schemes.

## Rate-Compatible Codes via Recursive BMST for Content-Sharing in Intelligent Vehicular Network

- **Status**: ❌
- **Reason**: rate-compatible BMST 차량네트워크 콘텐츠공유 — 슈퍼포지션 전송 기법, LDPC ECC 디코더/구성 이식점 없음
- **ID**: ieee:9098040
- **Type**: journal
- **Published**: July 2021
- **Authors**: Shancheng Zhao, Jinming Wen, Xiujie Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/9098040
- **Abstract**: Content-sharing is one of the major applications of vehicular networks. To fully utilize the spectrum and the connection time, rate-compatible codes are required when sharing content. In this paper, we present a simple and flexible method to construct low-complexity rate-compatible codes for content sharing. We first present a novel construction framework for rate-compatible codes via recursive block Markov superposition transmission (rBMST). In the proposed construction, the shared content is partitioned into equal-length data chunks and transmitted directly, while their replicas are taken as the inputs of a given number of parallel systematic encoders to generate parity-check chunks. These parity-check chunks are then transmitted in parallel in a recursive block Markov superposition transmission manner. The proposed construction is flexible in the sense that codes with arbitrary rates can be obtained by adjusting the number of parallel rBMST encoders and the number of randomly punctured bits. We show that the simplest construction, using repetition to generate the parity-check chunks, leads to high-performance and low-complexity rate-compatible rBMST (RC-rBMST) codes. Specifically, the extrinsic information transfer (EXIT) chart analysis shows that asymptotic thresholds of the repetition-based RC-rBMST (RB-RC-rBMST) codes are within 0.25 dB of the channel capacities for a wide range of coding rates. Numerical results are presented to confirm the advantages of the RB-RC-rBMST codes in performance and complexity. Particularly, the RB-RC-rBMST codes perform as well as BMST-R codes but with much lower computational complexities.

## Capacity Optimality of AMP in Coded Systems

- **Status**: ❌
- **Reason**: LRMS+AMP 용량 최적성 - 순수 이론, LDPC 매칭은 표준 irregular LDPC 사용, 새 디코더/구성 없음
- **ID**: ieee:9446137
- **Type**: journal
- **Published**: July 2021
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/9446137
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the approximate message passing (AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of AMP is analyzed. We prove that AMP achieves the constrained capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. As a byproduct, we provide an alternative derivation for the constraint capacity of an LRMS using a proved property of AMP. We discuss realization techniques for the matching principle of binary signaling using irregular low-density parity-check (LDPC) codes and provide related numerical results. We show that the optimized codes demonstrate significantly better performance over un-matched ones under AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Modulated Sparse Superposition Codes for the Complex AWGN Channel

- **Status**: ❌
- **Reason**: Sparse superposition codes(SPARC)+AMP 디코더 - LDPC ECC가 아니며 떼어낼 LDPC 기법 없음
- **ID**: ieee:9433595
- **Type**: journal
- **Published**: July 2021
- **Authors**: Kuan Hsieh, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/9433595
- **Abstract**: This paper studies a generalization of sparse superposition codes (SPARCs) for communication over the complex additive white Gaussian noise (AWGN) channel. In a SPARC, the codebook is defined in terms of a design matrix, and each codeword is a generated by multiplying the design matrix with a sparse message vector. In the standard SPARC construction, information is encoded in the locations of the non-zero entries of the message vector. In this paper we generalize the construction and consider modulated SPARCs, where information is encoded in both the locations and the values of the non-zero entries of the message vector. We focus on the case where the non-zero entries take values from a phase-shift keying (PSK) constellation. We propose a computationally efficient approximate message passing (AMP) decoder, and obtain analytical bounds on the state evolution parameters which predict the error performance of the decoder. Using these bounds we show that PSK-modulated SPARCs are asymptotically capacity achieving for the complex AWGN channel, with either spatial coupling or power allocation. We also provide numerical simulation results to demonstrate the error performance at finite code lengths. These results show that introducing modulation to the SPARC design can significantly reduce decoding complexity without sacrificing error performance.

## Using List Decoding to Improve the Finite-Length Performance of Sparse Regression Codes

- **Status**: ❌
- **Reason**: SPARC+CRC 리스트 디코딩, AMP 디코더 — sparse regression code, 바이너리 LDPC ECC와 무관
- **ID**: ieee:9398698
- **Type**: journal
- **Published**: July 2021
- **Authors**: Haiwen Cao, Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/9398698
- **Abstract**: We consider sparse regression codes (SPARCs) over complex AWGN channels. Such codes can be efficiently decoded by an approximate message passing (AMP) decoder, whose performance can be predicted via so-called state evolution in the large-system limit. In this paper, we mainly focus on how to use concatenation of SPARCs and cyclic redundancy check (CRC) codes on the encoding side and use list decoding on the decoding side to improve the finite-length performance of the AMP decoder for SPARCs over complex AWGN channels. Simulation results show that such a concatenated coding scheme works much better than SPARCs with the original AMP decoder and results in a steep waterfall-like behavior in the bit-error rate performance curves. Furthermore, we apply our proposed concatenated coding scheme to spatially coupled SPARCs. Besides that, we also introduce a novel class of design matrices, i.e., matrices that describe the encoding process, based on circulant matrices derived from Frank or from Milewski sequences. This class of design matrices has comparable encoding and decoding computational complexity as well as very close performance with the commonly-used class of design matrices based on discrete Fourier transform (DFT) matrices, but gives us more degrees of freedom when designing SPARCs for various applications.

## Capacity-Achieving Spatially Coupled Sparse Superposition Codes With AMP Decoding

- **Status**: ❌
- **Reason**: SPARC+AMP 용량달성 증명 - 순수 이론 bound이며 LDPC는 베이스라인 비교용에 불과
- **ID**: ieee:9441022
- **Type**: journal
- **Published**: July 2021
- **Authors**: Cynthia Rush, Kuan Hsieh, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/9441022
- **Abstract**: Sparse superposition codes, also referred to as sparse regression codes (SPARCs), are a class of codes for efficient communication over the AWGN channel at rates approaching the channel capacity. In a standard SPARC, codewords are sparse linear combinations of columns of an i.i.d. Gaussian design matrix, while in a spatially coupled SPARC the design matrix has a block-wise structure, where the variance of the Gaussian entries can be varied across blocks. A well-designed spatial coupling structure can significantly enhance the error performance of iterative decoding algorithms such as Approximate Message Passing (AMP). In this paper, we obtain a non-asymptotic bound on the probability of error of spatially coupled SPARCs with AMP decoding. Applying this bound to a simple band-diagonal design matrix, we prove that spatially coupled SPARCs with AMP decoding achieve the capacity of the AWGN channel. The bound also highlights how the decay of error probability depends on each design parameter of the spatially coupled SPARC. An attractive feature of AMP decoding is that its asymptotic mean squared error (MSE) can be predicted via a deterministic recursion called state evolution. Our result provides the first proof that the MSE concentrates on the state evolution prediction for spatially coupled designs. Combined with the state evolution prediction, this result implies that spatially coupled SPARCs with the proposed band-diagonal design are capacity-achieving. Using the proof technique used to establish the main result, we also obtain a concentration inequality for the MSE of AMP applied to compressed sensing with spatially coupled design matrices. Finally, we provide numerical simulation results that demonstrate the finite length error performance of spatially coupled SPARCs. The performance is compared with coded modulation schemes that use LDPC codes from the DVB-S2 standard.

## Design of Successive cancellation List Decoding of Polar Codes

- **Status**: ❌
- **Reason**: Polar+CRC SCL 디코딩, LDPC는 비교 베이스라인일 뿐 NAND LDPC에 떼어낼 기법 없음
- **ID**: ieee:9489221
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: A.Albert Raj, M. Pooranasankari, S.Sri Abinayaa
- **PDF**: https://ieeexplore.ieee.org/document/9489221
- **Abstract**: Due to the introduction of 5G, the Polar codes have attracted researchers in the communication field. It is one of a linear block error-correcting codes. This is a kind of Information channel coding techniques with low-complexity in nature wherein the encoding and decoding operation will be performed. Moreover, when it is considered in theoretical prospective, this is considered as one of the capacitive achieving algorithm for a wide range of channel. Polar codes are shown to be instances of concatenated codes. It is proved that the effect of a polar code can be increased by showing the multistage decoding algorithm with log likelihood based Successive List decoding (SCL). As for as Frame error rate is concerned the SCL decoding is not an optimal solution. In this paper the performance of polar codes concatenated with CRC codes is presented and it is proved that it outperforms turbo or LDPC codes. The simulation result shows that with the sufficient amount of training this method can provide a lower frame-error rate for different code lengths.

## Performance Analysis of m-PSK/QAM Based on LDPC Code in Maritime Atmospheric Turbulence Channel

- **Status**: ❌
- **Reason**: 해상 난류 채널 LDPC-coded m-PSK/QAM 성능분석. LDPC는 부수 언급, 떼어낼 디코더·HW·코드설계 기여 없음.
- **ID**: ieee:9866499
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Zhongli Yi, Fuzhai Wang, Zheng Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/9866499
- **Abstract**: A LDPC-coded m-PSK/QAM communication system over maritime atmospheric turbulence channel is investigated. The performances of LDPC coded and uncoded with different modulation in turbulence channels are discussed and the design and deployment suggestions are given. © 2021 The Author(s)

## Probabilistic Shaped LDPC-coded 400G PM-64QAM DWDM Transmission in 50-GHz Grid

- **Status**: ❌
- **Reason**: 광통신 PS-64QAM DWDM 전송, LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:9866167
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Xiao Han, Yang Yue, Zhen Qu +2
- **PDF**: https://ieeexplore.ieee.org/document/9866167
- **Abstract**: Crosstalk tolerance of 400G PS-64QAM DWDM transmission in 50-GHz grid is investigated. In single-channel scenario, PS-64QAM outperforms uniform-64QAM by 0.6 dB, while PS-64QAM with optimized roll-off factor features a 0.9-dB gain in DWDM transmission regime. ©2021 The Author(s)

## Improved Time-Frequency Domain Linear Receiver for OFDM-Based OTFS

- **Status**: ❌
- **Reason**: OTFS 수신기 MMSE 등화 — LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:9580245
- **Type**: conference
- **Published**: 28-30 July
- **Authors**: Linfei Xu, Nan Li, Wei Xiang +4
- **PDF**: https://ieeexplore.ieee.org/document/9580245
- **Abstract**: Recently, a novel two-dimensional modulation technique termed orthogonal time frequency space modulation (OTFS) has been proposed for time- and frequency-selective wireless channels, which is designed to transform a time-varying multi-path fading channel into a time-invariant delay-Doppler (DD) channel. In this paper, we propose an improved time-frequency (TF) domain linear receiver for orthogonal frequency division multiplexing (OFDM) based OTFS systems. The proposed receiver uses the minimum mean square error (MMSE) equalizer in the TF domain considering inter-carrier interference, and implements channel normalization in the DD domain. As simulation results show, the proposed receiver can achieve a lower BER for the uncoded system, and also a BLER for the coded OTFS system using low density parity check codes (LDPC) in 5G systems. The complexity of the proposed receiver is almost the same as that of the conventional linear receiver in the TF domain, which is much lower than those of the DD domain receivers.

## Applications of Machine Learning for 5G Advanced Wireless Systems

- **Status**: ❌
- **Reason**: 5G ML 응용 서베이, LDPC ECC 관련 이식 가능 기법 없음
- **ID**: ieee:9498754
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Yingjun Zhou, Jiajun Chen, Man Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9498754
- **Abstract**: Wireless communication is playing an important role in benefiting our daily lives. Fifth generation (5G) advanced wireless communication is anticipated to support various upcoming services. Moreover, machine learning (ML) is expected to optimize wireless systems by tackling complex problems which cannot be solved using traditional mathematical models. In this paper, applications of ML for 5G advanced wireless communication are introduced in conjunction with its research advances. Furthermore, this paper explores the challenges and future research directions of applying ML in 5G advanced wireless communication.

## Iterative Receiver of Uplink Massive MIMO Unsourced Random Access

- **Status**: ❌
- **Reason**: Massive MIMO URA 수신기(CB-MUD+tree decoding), LDPC ECC 무관
- **ID**: ieee:9498916
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Zijie Liang, Jianping Zheng
- **PDF**: https://ieeexplore.ieee.org/document/9498916
- **Abstract**: Massive MIMO un-sourced random access (URA) is a promising massive random access technique for massive machine-type communications. The conventional receiver of uplink URA consists of inner covariance-based multiuser detection (CB-MUD) and outer tree-based decoding, and its performance is highly dependent on the threshold used to determine the activity state of transmit codeword in CB-MUD. In general, this threshold is involved with multiple system parameters, and difficult to optimize. In this paper, an iterative receiver consisting of CB-MUD and outer decoding is proposed. In this iterative receiver, the successive interference cancellation (SIC) strategy is employed, where the covariance information associated with codewords decided in the former iteration is peeled off and the residual covariance is used for CB-MUD in the latter iteration. Noting that the sparsity increases with iterative number, in general, the performance of CB-MUD can be improved which is demonstrated by simulations. On the other hand, multiple iterations can relax the requirement of threshold selection. Concretely, an empirical formula for the threshold setting which decreases with iteration number is presented, and its robustness to system parameters is also verified by simulations.

## Library of Digital Communication Algorithms in the SimInTech Dynamic Modeling Environment. Opportunities and Prospects for Development

- **Status**: ❌
- **Reason**: 통신 알고리즘 라이브러리/모델링 환경 소개일 뿐, 떼어낼 LDPC 디코더·코드·HW 기여 없음
- **ID**: ieee:9494068
- **Type**: conference
- **Published**: 28 June-2 
- **Authors**: Aleksey A. Ovinnikov, Evgeny A. Likhobabin
- **PDF**: https://ieeexplore.ieee.org/document/9494068
- **Abstract**: This paper is devoted to the results of the creation of the Digital Communication Library, as well as to the implementation of the concept of multi-rate signal processing in the SimInTech dynamic modeling environment. When designing the library blocks, the computational complexity of the created algorithms was taken into account, which was reflected in the implementation language of the main functionality. Based on the developed elements, models were created that demonstrate the capabilities of the SimInTech system in the field of signal processing in applied and educational telecommunications tasks.

## Reliable Data Transport Protocol with FEC Mechanism for Erasure Channels

- **Status**: ❌
- **Reason**: erasure 채널 FEC 전송 프로토콜(네트워크 패킷 보호), LDPC ECC 떼어낼 기법 없음 — 무선/응용 특이적 제외
- **ID**: ieee:9522618
- **Type**: conference
- **Published**: 26-28 July
- **Authors**: Zsolt Alfred Polgar
- **PDF**: https://ieeexplore.ieee.org/document/9522618
- **Abstract**: Multimedia services generate an important part of the Internet traffic and the request for such services is increasing continuously. The characteristics of these services and their QoS requirements generate new challenges for the communication protocols. In order to cope with heavy congestions and the feedback implosion phenomenon Forward Error Correction (FEC) mechanisms were integrated into protocols controlling content distribution services and network coding techniques were proposed for peer-to-peer communications. The paper proposes a data transport protocol with integrated FEC mechanism intended to control the transmission between gateway nodes. The gateway level implementation allows protecting aggregated flows against packet drops generated by congestions and channel erasures. The proposed FEC enhanced data transport mechanism is combined with multipath transmissions between gateways, being exploited the diversity offered by such transmissions. A prototype protocol was implemented and experimentally evaluated on simulated transmission channels. The performance improvements of the proposed protocol in terms of packet erasure rate and jitter observed after decoding was demonstrated.

## A Review of Enabling Physical-Layer Technologies for Terahertz Communications

- **Status**: ❌
- **Reason**: 테라헤르츠 물리계층 기술 리뷰, LDPC ECC에 이식할 디코더/HW/코드설계 기여 없음
- **ID**: ieee:9549518
- **Type**: conference
- **Published**: 26-28 July
- **Authors**: Haiyao Xie, Feifei Wang, Yihao Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9549518
- **Abstract**: With the explosive growth of mobile data demand, the contradiction between rate demand and spectrum shortage has become increasingly prominent. High-frequency communication systems such as millimeter wave and terahertz have gradually entered people/s field of vision, and they have been applied to satellite communications because of their vast bandwidth. The bottleneck of wireless bandwidth and spectrum utilization has become a vital issue for future wireless mobile networks, so terahertz communication has been proposed as an essential part of 5G and future 6G mobile networks. This article mainly investigates the enabling physical layer’s critical technologies under the background of terahertz communication, including the recent research and development trend of the high-frequency band and multi-antenna technology and coding technology. Finally, this article points out the challenges and research directions of the terahertz communication network’s physical layer technology in the future.

## Next Generation Mobile Broadcasting BICM Module to Improve T2-Lite System Robustness

- **Status**: ❌
- **Reason**: DVB-NGH BICM 모듈/rotated constellation, LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:9626794
- **Type**: conference
- **Published**: 25-26 July
- **Authors**: Hamzah Sabr Ghayyib, Samir Jasim Mohammed
- **PDF**: https://ieeexplore.ieee.org/document/9626794
- **Abstract**: Digital Video Broadcasting Next Generation Handheld (DVB-NGH) is the next-generation mobile TV broadcasting technology, which the DVB Project has developed. It’s the mobile extension of the high-performance Digital Video Broadcasting Terrestrial Second Generation (DVB-T2), with the most superior transmission technologies. One of the main modifications introduced by DVB-NGH is the advanced module of Bit-interleaved coded and modulation (BICM) based on a subset of DVB-T2 BICM elements. The diversity benefit gained by the modern features included in the DVB-NGH BICM module is examined in this study. This module incorporates two kinds of rotation schemes according to the specified coding rate: two-dimensional and four-dimensional rotated constellations (2D, 4D-RC). A comparison has been made between the acquired gain and the case of using the T2-Lite system’s fundamental BICM module, including the rotated constellations method. To confirm the efficiency of the created module, simulation results were done in MATLAB version R2020b using two fading channels: Rayleigh and 0 dB Echo. Finally, the acquired findings show a significant increase in system robustness when using the DVB-NGH BICM instead of the fundamental T2-Lite BICM module.

## Evaluation of Low-density parity-check code with 16-QAM OFDM in a time-varying channel

- **Status**: ❌
- **Reason**: 표준 LDPC+16QAM OFDM BER 평가 — 새 디코더/구성 없는 표준 적용, 무선 응용 평가
- **ID**: ieee:9530811
- **Type**: conference
- **Published**: 17-18 July
- **Authors**: A. Y. Kuti, A. E. Abdelkareem
- **PDF**: https://ieeexplore.ieee.org/document/9530811
- **Abstract**: In wireless networks, multipath interference in a time-varying channel is a significant and major challenge to effective data transmission. Bit error rate (BER) efficiency is improved using Forward Error Correction (FEC) coding, such as Low-Density Parity-Check (LDPC) coding. LDPC, which can accomplish near Shannon limit efficiency and has recently gained considerable attention because of these properties. The efficiency of an LDPC coded orthogonal frequency division multiplexing (OFDM) communication scheme for time-varying channels is evaluated in this paper. Then we study the bandwidth-efficient coded modulation system based on LDPC codes that have low implementation complexity and high BER efficiency. Simulation is used to investigate the effects of modulation and coding schemes on the performance of the LDPC code.The results show that the device can significantly boost the efficiency of wireless channels while lowering the code rate and improving overall system performance.

## Concatenated Coset Coding in a Multi-tone DHA FH OFDMA System with Order Statistics-based Reception

- **Status**: ❌
- **Reason**: DHA FH OFDMA의 coset code 결합변조 — 비-LDPC, 무선 응용 특이적, 이식 기법 없음
- **ID**: ieee:9530807
- **Type**: conference
- **Published**: 17-18 July
- **Authors**: Dmitry Osipov
- **PDF**: https://ieeexplore.ieee.org/document/9530807
- **Abstract**: A coded modulation scheme for a single-band multi-tone DHA FH OFDMA system that employs order statistics-based reception and a concatenation of coset codes is proposed. It is demonstrated that this coded modulation scheme provides profound performance gain over the conventional coded single-band multi-tone DHA FH OFDMA while preserving the effective transmission rate at the expense of minor complexity increase.

## A Study of Anti-jamming Pseudo Random Partial Band Hopping for OFDM Communication System

- **Status**: ❌
- **Reason**: OFDM 항재밍 주파수홉핑 BER 분석, LDPC 무관 무선통신 응용
- **ID**: ieee:9513938
- **Type**: conference
- **Published**: 13-15 July
- **Authors**: Mohamed A. Soliman, Shady A Deraz, Walid M. Saad +1
- **PDF**: https://ieeexplore.ieee.org/document/9513938
- **Abstract**: Orthogonal frequency-division-multiplexing (OFDM approach) is regarded as one of the most well-known robust methods for mitigating jamming and exploiting hopping schemes across multiple-frequency sub-bands or bands, and is notable for its ability to improve the overall performance of wireless communication schemes, particularly in military communications. Combining the two methods should help to mitigate interference caused by accidental or deliberate jamming, particularly in military applications. The bit-error rate (BER) performance of an enhanced OFDM communication system over a multi-path Rayleigh fading channel is demonstrated in this paper using frequency sub-band hopping techniques in the presence of various types of jammers. The jamming scenarios vary from narrow band-jammer to barrage jammer depending on the jamming ratio are presented. Also, it includes two different hopping strategies, which are 3-band hopping and 6-band hopping. According to the simulation results, by increasing the amount of hopping sub-bands, the BER performance of the entire-regarded hopping schemes is significantly improved.

## Euclidean Distance Spectra of Irregular NB LDPC Coded QAM Signals with Optimized Mappings

- **Status**: ❌
- **Reason**: Non-binary LDPC coded QAM 매핑/거리스펙트럼 — 비이진 LDPC 즉시 제외
- **ID**: ieee:9518126
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek
- **PDF**: https://ieeexplore.ieee.org/document/9518126
- **Abstract**: Properties of non-binary (NB) LDPC codes used in conjunction with coded modulation systems are studied. It is observed that the performance of the NB LDPC coded transmission schemes strongly depends on the mapping between the NB symbols and the signal constellation points. The Euclidean distance spectra for an ensemble of random NB LDPC codes for specific mappings are derived. The simulation results for belief-propagation decoding in the coded modulation schemes with the NB QC-LDPC codes under different mappings are presented.

## Deep Learning-Based Bit Reliability Based Decoding for Non-binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 딥러닝 디코딩, 바이너리 한정 기준 위배로 제외
- **ID**: ieee:9517790
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Taishi Watanabe, Takeo Ohseki, Kosuke Yamazaki
- **PDF**: https://ieeexplore.ieee.org/document/9517790
- **Abstract**: The bit reliability based (BRB) and weighted bit reliability based (wBRB) algorithms are non-binary low-density parity-check (LDPC) code decoding algorithms with an excellent tradeoff between computational complexity and performance. However, the performance of these algorithms needs further improvement. We apply deep learning to these algorithms. Weights are assigned to each edge of the Tanner graphs of the non-binary LDPC codes in the proposed algorithms. We demonstrate the effectiveness of applying deep learning to the BRB and wBRB algorithms in terms of implementation and performance. The proposed algorithms achieve an approximately 0.3 dB higher bit error rate performance than the original algorithms in the high SNR region. The increase in computational complexity and memory consumption does not significantly change the implementation of the algorithms.

## A Class of Non-Binary Doubly-Generalized LDPC codes for Moderate and High Code Rates

- **Status**: ❌
- **Reason**: Non-binary doubly-generalized LDPC (extended alphabets/GF(q)) — 비이진 LDPC 즉시 제외
- **ID**: ieee:9518035
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Gada Rezgui, Iryna Andriyanova, Asma Maalaoui +1
- **PDF**: https://ieeexplore.ieee.org/document/9518035
- **Abstract**: In this paper, a new class of doubly-generalized LDPC codes is proposed. The particular point of the proposed construction is the presence of a small fraction of single parity-check codes at the variable nodes side. Together with the use of extended alphabets, the existence of such a fraction has been shown to improve the asymptotic decoding threshold, without harming the minimum distance behaviour of the code ensemble. Note that the improvement is more significant in cases where the code initially contains check nodes of high degrees, which corresponds to the region of moderate and high code rates.

## Nested LDPC Codes for Random Access Communication

- **Status**: ❌
- **Reason**: Random access 통신용 nested LDPC, ML 디코딩 유한블록 bound 분석 — 통신 응용 특이적 이론, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:9518171
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Yuxin Liu, Michelle Effros
- **PDF**: https://ieeexplore.ieee.org/document/9518171
- **Abstract**: This paper proposes a nested low-density parity-check (LDPC) code design. Combining this nested LDPC code with the random access coding strategy introduced by Yavas, Kostina, and Effros yields a random access LDPC (RA-LDPC) code for reliable communication in random access communication environments where neither the transmitters nor the receiver knows which or even how many transmitters wish to communicate at each moment. Coordination is achieved using sparse scheduled feedback. Bounds on the finite-blocklength performance of the RA-LDPC code under maximum likelihood (ML) decoding are derived using both error exponent and dispersion style analyses. Results include bounds on the penalty of the RA-LDPC code as a function of the LDPC code densities.

## Some Results on Density Evolution of Nonbinary SC-LDPC Ensembles Over the BEC

- **Status**: ❌
- **Reason**: 비이진(nonbinary) SC-LDPC density evolution 이론, 바이너리 한정·순수 이론으로 제외
- **ID**: ieee:9518021
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Mengnan Xu, Dan Zeng, Zhichao Sheng +2
- **PDF**: https://ieeexplore.ieee.org/document/9518021
- **Abstract**: In this paper, we present several theoretic results on density evolution (DE) for nonbinary spatially-coupled low-density parity-check (SC-LDPC) ensembles when the transmission takes place on the binary erasure channel (BEC). In specific, we establish the duality rule for entropy for the nonbinary variable-node (VN) and check-node (CN) operators in such a scenario. We define the partial order between densities and show that the VN and CN operators exhibit the property of partial order preservation. More importantly, we explicitly construct the potential functions for uncoupled and coupled DE recursions, the forms of which almost coincide with those for binary LDPC and SC-LDPC ensembles over general binary memoryless symmetric (BMS) channels. These theoretic findings greatly facilitate the proof of threshold saturation for nonbinary SC-LDPC ensembles on the BEC. Finally, we develop the threshold saturation theorem and its converse, following the lines established by S. Kumar et al.

## Capacity Optimality of AMP in Coded Systems

- **Status**: ❌
- **Reason**: AMP 용량 최적성 순수 이론 분석, LDPC는 수치예시 베이스라인 — 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:9518062
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Lei Liu, Chulong Liang, Junjie Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/9518062
- **Abstract**: This paper studies a large random matrix system (LRMS) model involving an arbitrary signal distribution and forward error control (FEC) coding. We establish an area property based on the approximate message passing (AMP) algorithm. Under the assumption that the state evolution for AMP is correct for the coded system, the achievable rate of AMP is analyzed. We prove that AMP achieves the constrained capacity of the LRMS with an arbitrary signal distribution provided that a matching condition is satisfied. We provide related numerical results of binary signaling using irregular low-density parity-check (LDPC) codes. We show that the optimized codes demonstrate significantly better performance over unmatched ones under AMP. For quadrature phase shift keying (QPSK) modulation, bit error rate (BER) performance within 1 dB from the constrained capacity limit is observed.

## Trapping Set Analysis of Finite-Length Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(QLDPC) trapping set — 양자 EC 원칙 제외, 디코더가 신드롬/축퇴 등 양자 전용 개념 의존
- **ID**: ieee:9518154
- **Type**: conference
- **Published**: 12-20 July
- **Authors**: Nithin Raveendran, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/9518154
- **Abstract**: Iterative decoders for finite length quantum low-density parity-check (QLDPC) codes are impacted by short cycles, detrimental graphical configurations known as trapping sets (TSs) present in a code graph as well as symmetric degeneracy of errors. In this paper, we develop a systematic methodology by which quantum trapping sets (QTSs) can be defined and categorized according to their topological structure. Conventional definition of a TS from classical error correction is generalized to address the syndrome decoding scenario for QLDPC codes. We show that QTS information can be used to design better QLDPC code and decoder. For certain finite-length QLDPC codes, frame error rate improvements of two orders of magnitude in the error floor regime are demonstrated without needing any post-processing steps.

## Iterative Detection and Decoding for Multiuser MIMO Systems with Low Resolution Precoding and PSK Modulation

- **Status**: ❌
- **Reason**: MIMO 저해상도 프리코딩+반복 검출/복호. LDPC는 베이스라인 부호, 떼어낼 LDPC 디코더 기법 없음(무선 응용 특이)
- **ID**: ieee:9513787
- **Type**: conference
- **Published**: 11-14 July
- **Authors**: Erico S. P. Lopes, Lukas T. N. Landau
- **PDF**: https://ieeexplore.ieee.org/document/9513787
- **Abstract**: Low-resolution precoding techniques have gained considerable attention in the wireless communications area recently. Vital but hardly discussed in literature, discrete precoding in conjunction with channel coding is the subject of this study. Unlike prior studies, we propose three different soft detection methods and an iterative detection and decoding scheme that allow the utilization of channel coding in conjunction with low-resolution precoding. Besides an exact approach for computing the extrinsic information, we propose two approximations with reduced computational complexity. Numerical results based on PSK modulation and an LDPC block code indicate a superior performance as compared to the system design based on the common AWGN channel model in terms of bit-error-rate.

## Blind Joint Nonlinear Equalizer for mmWave Communications

- **Status**: ❌
- **Reason**: mmWave 블라인드 비선형 수신기, LDPC는 보조 디코딩일 뿐 새 LDPC 기법 없음
- **ID**: ieee:9509989
- **Type**: conference
- **Published**: 10-11 July
- **Authors**: Bo-Henq Yeh, Fang-Biau Uenq, Cheng-Feng Wu
- **PDF**: https://ieeexplore.ieee.org/document/9509989
- **Abstract**: In this paper, we study the blind joint nonlinear receiver for millimeter wave (mmWave) communication systems. The mmWave system operates in a very high-frequency band and has a lot of bandwidth resources. The RF power amplifier (PA) used by the system poses a huge challenge to signal detection and demodulation. Instead of using high-complexity and difficult-to-implement digital predistortion at the transmitter, the blind joint nonlinear receiver is proposed to make mmWave communication a new possibility in 5G NR. Due to the non-linearity and edge integration, the posteriori probability of the received signal is quite difficult to analyze, which makes existing linear equalization techniques unusable. Therefore, we use the particle filter that is based on Monte Carlo sequence importance sampling. With the aid of LDPC (low-density parity-check) decoding, the proposed blind receiver can operate without training sequence. In this way, the unknown transmitting signal can be successfully recursively estimated. The simulation results validate the proposed method.
