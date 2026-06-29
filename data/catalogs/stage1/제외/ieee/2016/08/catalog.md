# IEEE Xplore — 2016-08


## Non-Binary LDPC Codes for Magnetic Recording Channels: Error Floor Analysis and Optimized Code Design

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC 자기기록채널 error floor/코드최적화(balanced absorbing set) — 비이진 LDPC 제외
- **ID**: ieee:7482740
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Ahmed Hareedy, Behzad Amiri, Rick Galbraith +1
- **PDF**: https://ieeexplore.ieee.org/document/7482740
- **Abstract**: In this paper, we provide a comprehensive analysis of the error floor along with code optimization guidelines for structured and regular non-binary low-density parity-check (NB-LDPC) codes in magnetic recording (MR) applications. While the topic of the error floor performance of binary LDPC codes over additive white Gaussian noise (AWGN) channels has recently received considerable attention, very little is known about the error floor performance of NB-LDPC codes over other types of channels, despite the early results demonstrating superior characteristics of NB-LDPC codes relative to their binary counterparts. We first show that, due to the outer looping between the detector and the decoder in the receiver, the error profile of NB-LDPC codes over partial-response (PR) channels is qualitatively different from the error profile over AWGN channels—this observation motivates us to introduce new combinatorial objects aimed at capturing decoding errors that dominate the PR channel error floor region. We call these objects balanced absorbing sets (BASs), which are viewed as a special subclass of previously introduced absorbing sets (ASs). Aided by these new objects (BASs), we develop a method that combines analytical equations and biased simulations to predict the error floor performance of NB-LDPC codes over PR channels without the need to execute extensive Monte Carlo (MC) simulations. We show that explicitly incorporating the inter-symbol interference of MR channels into our prediction method makes the accuracy of the error floor estimate within 0.2 of an order of magnitude from the traditional MC simulation. In addition, we prove that, due to the more restrictive definition of BASs (relative to the more general class of ASs), an additional degree of freedom can be exploited in the code design for PR channels. We then demonstrate that the proposed code optimization aimed at removing dominant BASs offers performance improvements in the frame error rate in the error floor region by up to 2.5 orders of magnitude over the unoptimized designs. Our code optimization technique carefully, yet provably, removes BASs from the code while preserving its overall structure (node degree, quasi-cyclic property, regularity, and so forth). The resulting codes outperform the existing binary and NB-LDPC solutions for PR channels by about 2.5 and 1.25 orders of magnitude, respectively.

## Reduced-Complexity Nonbinary LDPC Decoder for High-Order Galois Fields Based on Trellis Min–Max Algorithm

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(32)/GF(64)) trellis min-max 디코더 — 비이진 LDPC 제외
- **ID**: ieee:7399426
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Jesús O. Lacruz, Francisco García-Herrero, María José Canet +1
- **PDF**: https://ieeexplore.ieee.org/document/7399426
- **Abstract**: Nonbinary LDPC codes outperform their binary counterparts in different scenarios. However, they require a considerable increase in complexity, especially in the check-node (CN) processor, for high-order Galois fields (GFs) higher than GF(16). To overcome this drawback, we propose an approximation for the trellis min-max algorithm that allows us to reduce the number of exchanged messages between the CN and the variable node compared with previous proposals from the literature. On the other hand, we reduce the complexity in the CN processor, keeping the parallel computation of messages. We implemented a layered scheduled decoder, based on this algorithm, in a 90-nm CMOS technology for the (837, 723) NB-LDPC code over GF(32) and the (1536, 1344) over GF(64), achieving an area saving of 16% and 36% for the CN and 10% and 12% for the whole decoder, respectively. The throughput is 1.07 and 1.26 Gb/s, which outperforms the state of the art of high-rate decoders with the high GF order from the literature.

## An Efficient Algorithm to Improve the Success Threshold of Node-Based Verification-Based Algorithms in Compressed Sensing

- **Status**: ❌
- **Reason**: 압축센싱 verification-based 신호복원 — 채널 ECC 아님, BEC stopping set 영감만, 떼어낼 디코더 기법 없음
- **ID**: ieee:7470554
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Sara Khosravi, Reza Asvadi, Mahmoud Ahmadian-Attari
- **PDF**: https://ieeexplore.ieee.org/document/7470554
- **Abstract**: In this letter, we introduce an algorithm to enhance the success threshold of node-based verification-based (NB-VB) algorithms in compressed sensing. The NB-VB algorithms have low computational complexity, and are generally classified as iterative message passing algorithms employed for signal recovery. However, similar to the standard iterative decoding of low-density parity-check codes over the binary erasure channel (BEC) in the context of channel coding, these algorithms become inefficient in the stopping sets. The proposed method, with the inspiration of improved decoding algorithms over the BEC, enhances the performance of NB-VB algorithms by guessing values of some unverified signal elements. Our simulation results indicate that although the proposed method improves the success threshold significantly, it does not cause any considerable increase in the complexity of standard NB-VB algorithms.

## Optimization Design and Asymptotic Analysis of Systematic Luby Transform Codes Over BIAWGN Channels

- **Status**: ❌
- **Reason**: Systematic LT(fountain) 부호의 degree distribution 최적화로 비-LDPC fountain 영역, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7493629
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Shengkai Xu, Dazhuan Xu
- **PDF**: https://ieeexplore.ieee.org/document/7493629
- **Abstract**: In this paper, we study systematic Luby transform (SLT) codes over binary input additive white Gaussian noise (BIAWGN) channels. To improve the bit-error-rate (BER) performance of SLT codes on the BIAWGN channel, this paper presents a novel optimization design of degree distributions. First, we apply the Gaussian approximation (GA) to analyze the asymptotic BER performance of SLT codes and calculate overhead thresholds for successful decoding. Second, we derive an approximate closed-form expression for lower bound on BER by applying the GA and further simplify the expression in low and high signal-to-noise ratio regimes, respectively. Third, we adopt the conventional linear programming (CLP) constrained by the GA to optimize the degree distribution of SLT codes. The objective of CLP is to minimize the average degree of the degree distribution that may result in bad error floor. To improve the error floor caused by CLP, we put forth a novel optimization model constrained by the lower bound on BER, and using the model we can design the degree distribution more flexibly with any desired BER. Simulation results show that the proposed degree distribution can provide better BER performance of SLT codes over the BIAWGN channel.

## A Factor Graph Approach to Iterative Channel Estimation, Detection, and Decoding for Two-Path Successive Relay Networks

- **Status**: ❌
- **Reason**: two-path relay 채널추정/검출/복호 factor graph 수신기 — off-the-shelf SISO 디코더, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7458882
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Frederic Lehmann
- **PDF**: https://ieeexplore.ieee.org/document/7458882
- **Abstract**: We consider cooperative communications between a source node and a destination node with the help of two relays. In order to overcome the half-duplex constraint, the amplify-and-forward two-path relaying protocol is used. We adopt orthogonal frequency-division multiplexing modulation to combat frequency-selective channels and asynchronous reception at the destination node. In this paper, we develop a coherent receiver architecture suitable for unknown block fading channels. A factor graph representing the joint a posteriori probability of the coded symbols and the channels in the frequency domain is introduced. Then, we derive a Bayesian inference algorithm based on message passing over the factor graph. The resulting iterative receiver maintains low-complexity, based on the interaction between an off-the-shelf soft-input soft-output decoder and a newly introduced per-subcarrier processor for two-path relaying channel estimation and symbol detection. Simulation results show that the proposed solution maintains the full diversity order, even with a limited number of training blocks.

## Perfect Secrecy in Physical-Layer Network Coding Systems From Structured Interference

- **Status**: ❌
- **Reason**: 물리계층 네트워크코딩 완전비밀성 — 보안/통신 응용, LDPC ECC 기법 없음
- **ID**: ieee:7464919
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: David A. Karpuk, Arsenia Chorti
- **PDF**: https://ieeexplore.ieee.org/document/7464919
- **Abstract**: Physical-layer network coding (PNC) has been proposed for next generation networks. In this paper, we investigate PNC schemes with embedded perfect secrecy by exploiting structured interference in relay networks with two users and a single relay. In a practical scenario where both users employ finite and uniform signal input distributions, we establish upper bounds (UBs) on the achievable perfect secrecy rates and make these explicit when pulse amplitude modulation modems are used. We then describe two simple, explicit encoders that can achieve perfect secrecy rates close to these UBs with respect to an untrustworthy relay in the single antenna and single relay setting. Last, we generalize our system to a multiple-input multiple-output relay channel, where the relay has more antennas than the users and study optimal precoding matrices, which maintain a required secrecy constraint. Our results establish that the design of PNC transmission schemes with enhanced throughput and guaranteed data confidentiality is feasible in next generation systems.

## Polar Code Design for Noisy Blackwell Channels

- **Status**: ❌
- **Reason**: polar code 설계(noisy Blackwell, Marton) — MLC 플래시 언급하나 polar 전용 설계, LDPC 이식 불가
- **ID**: ieee:7487044
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Lanying Zhao, Sung-Ik Choi, Sae-Young Chung
- **PDF**: https://ieeexplore.ieee.org/document/7487044
- **Abstract**: In this letter, we introduce a class of discrete memoryless broadcast channels, called noisy Blackwell channels, which generalize the Blackwell channel to include noise and to more than two users. We design the polar code for the noisy Blackwell channel based on Marton's coding scheme. We choose auxiliary random variables and the mapping from auxiliary random variables to the channel input, such that the sum-rate capacity can be achieved very closely. Furthermore, we show that the designed polar code can be applied to multi-level cell flash memories for improving random I/O performance. The simulation results demonstrate that our designed polar codes achieve good performance even for a large number of users.

## The design and implementation of the unidirectional data transmission equipment based on 802.11 physical frame

- **Status**: ❌
- **Reason**: Raptor/fountain FEC 기반 단방향 무선전송 장비, 비-LDPC이고 무선응용 특이적
- **ID**: ieee:7883165
- **Type**: conference
- **Published**: 26-28 Aug.
- **Authors**: Baihui Lu, Zhengxiang Li, Qibin Lu
- **PDF**: https://ieeexplore.ieee.org/document/7883165
- **Abstract**: With the rapid development of wireless network, people begin to require more on the reliability of data transmission, especially on the communication methods that can be applied under special condition. This paper usages the transceiver chip which is in line with the existing IEEE802.11 protocol, while changes the singe frame or frames ACK retransmission from IEEE802.11 protocol by recover lost data through Raptor codes which is based on FEC. All these changes aim to build a new unidirectional transmission mode, which contributes to data stream transport normally in the case of the sender exist interference source.

## Performance scrutiny and optimization of LDPC coded MIMO OFDM systems

- **Status**: ❌
- **Reason**: MIMO-OFDM 무선응용에 표준 LDPC 구성/density evolution 그대로 사용, 새 디코더·구성 기여 없음
- **ID**: ieee:7824815
- **Type**: conference
- **Published**: 26-27 Aug.
- **Authors**: V. S. Jadhav, Prithviraj Sawant
- **PDF**: https://ieeexplore.ieee.org/document/7824815
- **Abstract**: The implementable decoders and large collection of data transmission and storage channels can be admitted at the same time using low density parity check (LDPC) group of Linear block codes. We will review some of the LDPC construction techniques and encoding problem for LDPC codes. Also certain special classes of LDPC codes which will resolve encoding problems will be introduced. Performance analysis and design optimization of LDPC coded multiple input multiple output(MIMO) orthogonal frequency division multiplexing(OFDM) has been considered. The tools of density evolution with mixture Gaussian approximations are used to optimize LDPC codes which are not regular and to compute minimum operational signal-to-noise ratios (SNRs) for ergodic MIMO-OFDM channels. In particular, the optimization is done for various MIMO-OFDM system configurations, which include a different channel models and different demodulation schemes; the performance which is optimized is checked with the corresponding channel capacity. The iterative message passing decoding algorithm which gives optimal performance will be presented. The performance of turbo-iterative receiver that consists of a soft maximum a posteriori (MAP) demodulator will be presented. From the LDPC profiles that already are optimized for ergodic channels, we construct small block-size irregular codes for outage MIMO-OFDM channels.

## An improved successive cancellation decoder for polar codes

- **Status**: ❌
- **Reason**: polar code SCL/CRC-aided 디코더 중심, LDPC는 비교 베이스라인일 뿐 이식할 LDPC BP 기법 없음
- **ID**: ieee:7879671
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Lin Qi, Yu Xu, Tong Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7879671
- **Abstract**: The successive cancellation decoder is the first decoding algorithm for polar codes which can achieve binary memoryless symmetric channels' capacity. However, SC does not perform well. A method called SC List algorithm is proposed and is one of the best algorithms in terms of balance between bits error rate and computation complexity. In this paper, we find that CRC-aided SCL algorithm improves the effect of polar codes. This scheme is that CRC and polar codes play an inner and outer codes role in a concatenation codes. Simulation shows that Frame error rate of length N=1024 under SCL decoding with L=2 and an 8 bit CRC polar codes perform better than length N=1944 under offset min-sum decoding LDPC codes with a flooding schedule and a maximum of 10 iterations. All simulation is in the binary input addition white Gaussian noise channel and use BPSK modulation. Furthermore, the complexity of CRC-aided SCL algorithm is acceptable. The only weak point is that we need to sacrifice a little information rate.

## Message Passing for Analysis and Resilient Design of Self-Healing Interdependent Cyber-Physical Networks

- **Status**: ❌
- **Reason**: 사이버물리 네트워크 장애전파 factor graph 메시지패싱으로 채널 ECC 디코더 아님
- **ID**: ieee:7568543
- **Type**: conference
- **Published**: 1-4 Aug. 2
- **Authors**: Ali Behfarnia, Ali Eslami
- **PDF**: https://ieeexplore.ieee.org/document/7568543
- **Abstract**: Coupling cyber and physical systems gives rise to numerous engineering challenges and opportunities. An important challenge is the contagion of failure from one system to another, that can lead to large scale cascading failures. On the other hand, self-healing ability emerges as a valuable opportunity where the overlay cyber network can cure failures in the underlying physical network. To capture both self-healing and contagion, we introduce a factor graph representation of inter-dependent cyber-physical systems in which factor nodes represent various node functionalities and the edges capture the interactions between the nodes. We develop a message passing algorithm to study the dynamics of failure propagation and healing in this representation. Through applying a fixed point analysis to this algorithm, we investigate the network reaction to initial disruptions. Our analysis provides simple yet critical guidelines for choosing network parameters to achieve resiliency against cascading failures.

## Probabilistic-relationships in the DVB-T2 mobile-reception signal received from a fix-reception mode broadcasting service

- **Status**: ❌
- **Reason**: DVB-T2 모바일 수신 통계 분석; LDPC는 BER 지표로 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:7821920
- **Type**: conference
- **Published**: 1-3 Aug. 2
- **Authors**: Budi Setiyanto, Risanuri Hidayat, I Wayan Mustika +1
- **PDF**: https://ieeexplore.ieee.org/document/7821920
- **Abstract**: DVB-T2 (Digital Video Broadcasting Terrestrial Second Generation) standard is mainly intended to fix-reception service. Nevertheless, it is possible that some of enthusiastic users attempt to receive it in mobile environment. Therefore, formulating a technique for improving the reception quality is necessary, and exploring the received signal properties will be useful to do it. This paper presents quantitative-relationships in the received signal explored from field-observation result. The result informs that pairwise relationships between recovered picture and signal describing quantities, as well as among these quantities themselves, are more appropriate expressed probabilistically than mathematically. These quantities include CNR (carrier-to-noise ratio), pre-LDPC (low density parity check) decoding BER (bit-error-rate), and post-LDPC decoding BER. As numerical examples: (1) CNR border between successful and failed receptions is as high as about 14 dB, and (2) for probability of reception-success is as high as about 0.5, the border of these three quantities are about 18 dB, 4.5 × 10−2, and 10−5, respectively.
