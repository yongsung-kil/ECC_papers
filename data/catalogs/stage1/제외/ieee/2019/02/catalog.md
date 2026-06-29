# IEEE Xplore — 2019-02


## New Design of High-Rate Generalized Root Protograph LDPC Codes for Nonergodic Block Interference

- **Status**: ❌
- **Reason**: 표준 protograph LDPC 구성을 비에르고딕 블록간섭 채널에 적용한 무선응용 특이적 코드, NAND 이식할 새 디코더/HW 기법 없음
- **ID**: ieee:8571264
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Chanki Kim, Jong-Seon No, Gangsan Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/8571264
- **Abstract**: In this letter, we propose high-rate generalized root protograph (GRP) low-density parity-check (LDPC) codes for a nonergodic two-state binary symmetric channel with block interference with and without block fading. In these channels, the proposed GRP LDPC codes have asymptotic and finite-length performance improvement approaching to channel outage probability.

## Integrated Design of JSCC Scheme Based on Double Protograph LDPC Codes System

- **Status**: ❌
- **Reason**: 소스-채널 결합(JSCC) DP-LDPC 설계로 LDPC가 베이스라인, NAND 채널 ECC에 떼어낼 기법 없음(JSCC 제외 항목)
- **ID**: ieee:8594605
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Qiwang Chen, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/8594605
- **Abstract**: In this letter, an integrated design of joint source-channel coding scheme based on the double protograph low-density parity-check (DP-LDPC) codes is proposed. As degree-2 variable nodes (VNs) structure plays an important role in the performance of both water-fall and error-floor regions, the maximum number of degree-2 VNs for DP-LDPC codes is determined from a global perspective. By comparing different allocation schemes for degree-2 VNs, new design principles are proposed. Several DP-LDPC codes with different numbers of degree-2 VNs are proposed. The simulated results reveal the superiority of the optimized DP-LDPC codes, which are in line with the decoding threshold analysis by a joint protograph extrinsic information transfer algorithm.

## Hybrid Check Node Architectures for NB-LDPC Decoders

- **Status**: ❌
- **Reason**: NB-LDPC(GF(64)/GF(256)) check node 아키텍처 — 비이진 LDPC라 제외
- **ID**: ieee:8464053
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Cédric Marchand, Emmanuel Boutillon, Hassan Harb +2
- **PDF**: https://ieeexplore.ieee.org/document/8464053
- **Abstract**: This paper proposes a unified framework to describe the check node architectures of non-binary low-density parity-check (NB-LDPC) decoders. Forward-backward, syndrome-based, and pre-sorting approaches are first described. Then, they are hybridized in an effective way to reduce the amount of computation required to perform a check node. This paper is specially impacting check nodes of high degrees (or high coding rates). Results of 28-nm ASIC post-synthesis for a check node of degree 12 (i.e., a code rate of 5/6 with a degree of variable equal to 2) are provided for NB-LDPC over GF(64) and GF(256). While simulations show almost no performance loss, the new proposed hybrid implementation check node increases the hardware and the power efficiency by a factor of six compared with the classical forward-backward architecture. This leads to the first ever reported implementation of a degree 12 check node over GF(256), and these preliminary results open the road to high decoding throughput, high rate, and high-order Galois field NB-LDPC decoder with a reasonable hardware complexity.

## CRC-Aided Sphere Decoding for Short Polar Codes

- **Status**: ❌
- **Reason**: Polar code용 CRC-aided sphere decoding; 부호 의존적(SCL 대안)이라 바이너리 LDPC BP에 이식 불가, 비-LDPC 원칙 제외
- **ID**: ieee:8570830
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Jinnan Piao, Jincheng Dai, Kai Niu
- **PDF**: https://ieeexplore.ieee.org/document/8570830
- **Abstract**: Polar codes have recently been adopted as a coding scheme for fifth-generation wireless systems, owing to their excellent performance at short code lengths. In this letter, we propose a cyclic redundancy check (CRC)-aided sphere decoding (CA-SD) algorithm to further improve the performance of short polar codes. It provides better performance than the widely used CRC-aided successive cancellation list (CA-SCL) decoding, and it is robust to the CRC length that leads to the stable performance under a wide range of code rates. By employing the Gaussian elimination method, we transform the underlying parity check relationships in CRC as the equivalent new forms. This ensures the parity check bits can be uniquely judged by previous decoded bits rather than the redundant search during the CA-SD. By this means, the complexity of CA-SD is reduced and comparable with the CA-SCL decoding under short code lengths.

## Compute–Forward Multiple Access (CFMA): Practical Implementations

- **Status**: ❌
- **Reason**: CFMA 다중접속용 off-the-shelf LDPC + 수정 SPA — 다중접속 합부호 복구 특이적, 단일채널 NAND ECC로 이식할 일반 디코더 기법 아님
- **ID**: ieee:8485351
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Erixhen Sula, Jingge Zhu, Adriano Pastore +2
- **PDF**: https://ieeexplore.ieee.org/document/8485351
- **Abstract**: We present a practical strategy that aims to attain rate points on the dominant face of the multiple access channel capacity using a standard low complexity decoder. This technique is built upon recent theoretical developments of Zhu and Gastpar on compute-forward multiple access which achieves the capacity of the multiple access channel using a sequential decoder. We illustrate this strategy with off-the-shelf LDPC codes. In the first stage of decoding, the receiver first recovers a linear combination of the transmitted codewords using the sum-product algorithm (SPA). In the second stage, by using the recovered sum-of-codewords as side information, the receiver recovers one of the two codewords using a modified SPA, ultimately recovering both codewords. The main benefit of recovering the sum-of-codewords instead of the codeword itself is that it allows to attain points on the dominant face of the multiple access channel capacity without the need of rate-splitting or time sharing while maintaining a low complexity in the order of a standard point-to-point decoder. This property is also shown to be crucial for some applications, e.g., interference channels. For all the simulations with single-layer binary codes, our proposed practical strategy is shown to be within 1.7 dB of the theoretical limits, without explicit optimization on the off-the-self LDPC codes.

## A Novel Weight Coefficient PEG Algorithm for Ultra-Reliable Short Length Analog Fountain Codes

- **Status**: ❌
- **Reason**: Analog Fountain Codes (AFC)용 PEG 변형 — fountain code 무선 URLLC 특이적, 바이너리 LDPC ECC로 떼어낼 girth 기법 없음
- **ID**: ieee:8425638
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Zixuan Huang, Jian Jiao, Ke Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8425638
- **Abstract**: The stringent requirements of ultra-reliable and low latency communication (URLLC) services is the most challenging feature of fifth generation systems. The design and optimization of efficient short length codes is essential for URLLC. This letter investigates a novel weight coefficient progressive edge-growth (WCPEG) algorithm to construct ultra-reliable analog fountain codes (AFCs) in the short length regime. Our WCPEG AFC can approach the normal approximation benchmark by eliminating the small girth cycles in the encoding Tanner graph. We first analyze the properties of short length AFC, and then present the comprehensive description and theoretical identification of the WCPEG AFC algorithm. Simulation results demonstrate the superior performance of WCPEG AFC in the short length regime.

## Ultrareliable and Low-Latency Communication Techniques for Tactile Internet Services

- **Status**: ❌
- **Reason**: URLLC 무선 물리계층 서베이성 논문, channel code는 부수 언급, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8474959
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Kwang Soon Kim, Dong Ku Kim, Chan-Byoung Chae +9
- **PDF**: https://ieeexplore.ieee.org/document/8474959
- **Abstract**: This paper presents novel ultrareliable and low-latency communication (URLLC) techniques for URLLC services, such as Tactile Internet services. Among typical use cases of URLLC services are teleoperation, immersive virtual reality, cooperative automated driving, and so on. In such URLLC services, new kinds of traffic such as haptic information including kinesthetic information and tactile information need to be delivered in addition to high-quality video and audio traffic in traditional multimedia services. Furthermore, such a variety of traffic has various characteristics in terms of packet sizes and data rates with a variety of requirements of latency and reliability. Furthermore, some traffic may occur in a sporadic manner but requires reliable delivery of packets of medium to large sizes within a low latency, which is not supported by current state-of-the-art wireless communication systems and is very challenging for future wireless communication systems. Thus, to meet such a variety of tight traffic requirements in a wireless communication system, novel technologies from the physical layer to the network layer need to be devised. In this paper, some novel physical layer technologies such as waveform multiplexing, multiple-access scheme, channel code design, synchronization, and full-duplex transmission for spectrally efficient URLLC are introduced. In addition, a novel performance evaluation approach, which combines a ray-tracing tool and system-level simulation, is suggested for evaluating the performance of the proposed schemes. Simulation results show the feasibility of the proposed schemes providing realistic URLLC services in realistic geographical environments, which encourages further efforts to substantiate the proposed work.

## Design of SCMA Codebooks Based on Golden Angle Modulation

- **Status**: ❌
- **Reason**: SCMA codebook(GAM 기반) 설계로 LDPC ECC와 무관, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:8576566
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Zeina Mheich, Lei Wen, Pei Xiao +1
- **PDF**: https://ieeexplore.ieee.org/document/8576566
- **Abstract**: In this paper, we propose to use golden angle modulation (GAM) points to construct codebooks for uplink and downlink sparse code multiple access (SCMA) systems. We provide two categories of codebooks with one and two optimization parameters, respectively. The advantages of the proposed design method are twofold: 1) the number of optimization variables is independent of codebook and system parameters; and 2) it is simple to implement. In the downlink, we use GAM points to build a multidimensional mother constellation for SCMA codebooks, while in the uplink GAM points are directly mapped to user codebooks. The proposed codebooks exhibit good performance with low peak to average power ratio compared to the codebooks proposed in the literature based on constellation rotation and interleaving.

## Deep Learning Constellation Design for the AWGN Channel With Additive Radar Interference

- **Status**: ❌
- **Reason**: radar 간섭 AWGN용 auto-encoder constellation 설계 — 변조/디매핑, LDPC ECC 디코더 기법 아님
- **ID**: ieee:8490882
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Florence Alberge
- **PDF**: https://ieeexplore.ieee.org/document/8490882
- **Abstract**: Radar and wireless communication coexistence is considered in this paper as a possible solution to face the exploding demand and rising congestion in wireless networks. The transmission medium is modeled as an AWGN channel with additive radar interference. Standard constellations are not optimal in this context, and an auto-encoder (AE) is used to design proper constellations and corresponding receiver devices. AE is a powerful tool in neural networks that shares strong similarities with communication systems. This technique is particularly relevant in the lack of an analytical expression of the loss function. In the asymptotic region (high interference regime), the optimal constellation shape is known and the AE always converges toward this optimal solution. In the other regions, the AE is able to yield solutions that outperform the standard configurations. Several demapping alternatives are also considered leading to the conclusion that it is possible to maintain the communication link in the presence of radar interference independently of the interference power. This is a step further compared with previous works in which solutions were limited to low or high interference regimes.

## Lattice-Partition-Based Downlink Non-Orthogonal Multiple Access Without SIC for Slow Fading Channels

- **Status**: ❌
- **Reason**: lattice-partition NOMA(SIC 없는) 수신 — 무선 다중접속 특이적, LDPC ECC 기법 없음
- **ID**: ieee:8517129
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Min Qiu, Yu-Chih Huang, Jinhong Yuan +1
- **PDF**: https://ieeexplore.ieee.org/document/8517129
- **Abstract**: In this paper, the problem of downlink non-orthogonal multiple access (NOMA) over slow fading channels is studied. Full-channel state information (CSI) is assumed at the receivers, while only the statistical CSI is assumed to be available at the transmitter. A novel lattice-partition-based scheme is proposed which, according to statistical CSI, employs discrete inputs from appropriately designed constellations carved from a lattice, rather than continuous Gaussian inputs as used in most existing works. Theoretical analysis shows that for any outage probability smaller than 63.21%, which covers almost all the cases of practical interest, the proposed scheme with single-user decoding, i.e., without successive interference cancellation (SIC) is able to approach the NOMA outage capacity region within a constant gap, independent of the signal-to-noise ratio, and the number of users. Simulation results fortify the effectiveness of the proposed scheme by showing that the approach without SIC can achieve outage rates that are very close to the outage capacity region and the gap becomes even smaller when SIC is employed.

## Systematic Fountain Codes for Massive Storage Using the Truncated Poisson Distribution

- **Status**: ❌
- **Reason**: 분산스토리지용 fountain/erasure code + Poisson degree distribution BP — fountain degree 분포 설계 특이적, NAND 채널 ECC로 떼어낼 기법 없음(JSCC/fountain 제외 카테고리)
- **ID**: ieee:8519783
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Toritseju Okpotse, Shahram Yousefi
- **PDF**: https://ieeexplore.ieee.org/document/8519783
- **Abstract**: Erasure codes for distributed storage systems (DSS) are required to offer systematic encoding, low repair locality, low encoding/decoding complexity, and low decoding/storage overhead. However, the information theoretical bounds have shown that all these metrics might need to be carefully traded-off with one another. In this paper, we consider systematic Fountain codes with belief propagation (BP) decoding for massive scale DSSs. Analyzing the role of some degrees in the BP decoding process, we propose using the truncated Poisson distribution (TPD) for encoded symbol degrees. Identifying encoded symbol redundancy as a factor that degrades decoding overhead, we derive the probability of redundancy during the BP decoding process and use this as a tool for determining the Poisson parameter. Our proposed solution nicely addresses the first three DSS metrics with a slight toll on storage/decoding overhead. Through simulations, we show that the decoding overhead performance of the proposed scheme exhibits significant improvement over some existing Fountain code degree distributions in the literature. For instance, at a decoding overhead of 60%, we achieve a data loss probability closely approaching 10-4, while other Fountain codes compared are about a factor of 102 higher.

## Throughput Region of Spatially Correlated Interference Packet Networks

- **Status**: ❌
- **Reason**: 무선 패킷망 간섭/random access throughput region 이론, LDPC ECC와 무관
- **ID**: ieee:8421262
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Alireza Vahid, Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/8421262
- **Abstract**: In multi-user wireless packet networks, interference, typically modeled as packet collision, is the throughput bottleneck. Users become aware of the interference pattern via feedback and use this information for contention resolution and packet retransmission. Conventional random access protocols interrupt communication to resolve contention, which reduces network throughput and increases latency and power consumption. In this paper, we take a different approach, and we develop opportunistic random access protocols rather than pursuing conventional methods. We allow wireless nodes to communicate without interruption and to observe the interference pattern. We then use this interference pattern knowledge and channel statistics to counter the negative impact of interference. We prove the optimality of our protocols using an extremal rank-ratio inequality. An important part of our contributions is the integration of spatial correlation in our assumptions and results. We identify spatial correlation regimes in which inherently outdated feedback becomes as good as idealized instantaneous feedback and correlation regimes in which feedback does not provide any throughput gain. To better illustrate the results, and as an intermediate step, we characterize the capacity region of finite-field spatially correlated interference channels with delayed channel state information at the transmitters.

## An Efficient Optimal Algorithm for the Successive Minima Problem

- **Status**: ❌
- **Reason**: MIMO integer-forcing용 lattice SMP 알고리즘 — LDPC 무관, 격자 탐색 이론
- **ID**: ieee:8502084
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Jinming Wen, Lanping Li, Xiaohu Tang +1
- **PDF**: https://ieeexplore.ieee.org/document/8502084
- **Abstract**: In many applications, including integer-forcing linear multiple-input and multiple-output (MIMO) receiver design, one needs to solve a successive minima problem (SMP) on an n-dimensional lattice to get an optimal integer coefficient matrix A* ∈ Zn×n. In this paper, we first propose an efficient optimal SMP algorithm with an O(n2) memory complexity. The main idea behind the new algorithm is it first initializes with a suitable suboptimal solution, which is then updated via a novel algorithm with only O(n2) flops in each updating, until A* is obtained. Different from existing algorithms which find A* column by column through using a sphere decoding search strategy n times, the new algorithm uses a search strategy once only. We then rigorously prove the optimality of the proposed algorithm. Furthermore, we theoretically analyze its complexity. In particular, we not only show that the new algorithm is Ω(n) times faster than the most efficient existing algorithm with polynomial memory complexity, but also assert that it is even more efficient than the most efficient existing algorithm with exponential memory complexity. Finally, numerical simulations are presented to illustrate the optimality and efficiency of our novel SMP algorithm.

## Performance of Viterbi Decoding With and Without ARQ on Rician Fading Channels

- **Status**: ❌
- **Reason**: Viterbi/convolutional code + ARQ on fading — 비-LDPC, 떼어낼 BP 기법 없음
- **ID**: ieee:8487021
- **Type**: journal
- **Published**: Feb. 2019
- **Authors**: Lan V. Truong
- **PDF**: https://ieeexplore.ieee.org/document/8487021
- **Abstract**: In this paper, we investigate the performance of the Viterbi decoding algorithm with/without Automatic Repeat reQuest (ARQ) over a Rician flat fading channel with unlimited interleaving. We show that the decay rate of the average bit error probability with respect to the bit energy to noise ratio is at least equal to df at high-bit energy to noise ratio for both cases (with ARQ and without ARQ), where df is the free distance of the convolutional code. The Yamamoto-Itoh flag helps to reduce the average bit error probability by a factor of 4(d)f with a negligible retransmission rate. We also prove an interesting result that the average bit error probability decays exponentially fast with respect to the Rician factor for any fixed bit energy per noise ratio. In addition, the average bit error exponent with respect to the Rician factor is shown to be df.

## Performance Analysis of Circle-Constellation-Based M-DCSK Modulation for Broadcasting Application with Enhanced Reliability by LDPC

- **Status**: ❌
- **Reason**: 방송용 M-DCSK 변조에 LDPC를 부수적으로 적용, 표준 LDPC 사용 — 떼어낼 신규 LDPC 기법 없음(무선 응용 특이적)
- **ID**: ieee:8821728
- **Type**: conference
- **Published**: 23-25 Feb.
- **Authors**: Wei Wei, Junghwan Kim
- **PDF**: https://ieeexplore.ieee.org/document/8821728
- **Abstract**: In this paper, a circle-constellation-based M-ary differential chaos shift keying (M=8;8-DCSK) is proposed for broadcasting application, such as digital video broadcasting (DVB), rather than coherent amplitude phase shift keying (APSK) which implementation is much complex because of the necessity of synchronous demodulation at the receiver. In addition, low density parity check (LDPC) which can denote the effective reduction of bit error rate (BER) by an iteration decoding algorithm is also deployed in the proposed system to overcome the degradation of BER performance which results from the channels nonlinearity and the effect of natural or man-made noises, such as additive white Gaussian noise (AWGN) or partial band noise jamming (PBNJ). From the computer simulation results, the proposed regular and irregular LDPC-coded 8-DCSK requires merely -27 dB power to retain the BER in the range of 10-1~10-3 under AWGN and PBNJ with ρ=0.5.

## Serial Concatenated Convolution Codes for Coded OFDM in Digital Audio Broadcasting Environment

- **Status**: ❌
- **Reason**: DAB용 직렬연접 컨볼루션 부호, LDPC 아님·이식 기법 없음
- **ID**: ieee:8908080
- **Type**: conference
- **Published**: 21-22 Feb.
- **Authors**: P. Santhosh Kumar, M. Raju, Md. Asim Iqbul
- **PDF**: https://ieeexplore.ieee.org/document/8908080
- **Abstract**: In this paper, we are simulating the Bit Error Rate (BER) for computerized Digital Audio Broadcasting (DAB) framework that utilizes Co-OFDM system by parallel and serial coding schemes. Serial convolution coded data appears to be an Additive White Gaussian Noise (AWGN) Channel that is dependent on various imperative constant dimensions and code originator polynomial values obtained by convolution coding. Bit error rate simulations are done by applying sound signal and then estimating their performance with BER execution for the convolution coded. Serial convolution with various processor speeds 1/2 and 1/3 in AWGN is increasingly dependent on the perceptual coding. It is estimated, measured and plotted for developing a convolution coded DAB system environment.

## Two-Dimensional Magnetic Recording Systems with CRC-concatenated Polar Channel Coding Schemes

- **Status**: ❌
- **Reason**: polar+CRC SCL 자기기록(TDMR) 코딩으로 비-LDPC, LDPC 이식 기법 없음
- **ID**: ieee:8661322
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Hidetoshi Saito
- **PDF**: https://ieeexplore.ieee.org/document/8661322
- **Abstract**: It is known that a CRC (cyclic redundancy check)-concatenated polar coding scheme with successive cancellation list (SCL) decoding can signicantly enhance the error rate performance of the polar code with successive cancellation decoding. This advanced decoding method for the CRC-concatenated polar coding scheme is also called the CRC-aided SCL decoding method. In this research, the CRC-concatenated polar coding schemes are designed for multi-track recording with two-dimensional (2D) run-length limited constraints. We evaluate the error rate performances of the two-dimensional magnetic recording (TDMR) systems with the proposed coding and 2D partial response equalization schemes using bit-patterned media. As a result, it shows that the block error rate (BER) performances of the multi-track recording systems with CRC-aided SCL decoding are superior to that of the single recording systems with the conventional high rate binary coding schemes.

## On the Relation between PAPR and System Performance in Multicarrier Modulation

- **Status**: ❌
- **Reason**: 멀티캐리어 PAPR vs 성능 분석으로 LDPC가 부수 언급, 떼어낼 ECC/디코더 기법 없음
- **ID**: ieee:8661312
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Stephan Pfletschinger, Ludwig Erhardt
- **PDF**: https://ieeexplore.ieee.org/document/8661312
- **Abstract**: The high peak power in comparison to the average transmit power is one of the major long-standing problems in multicarrier modulation and is known as the PAPR (peak to average power ratio) problem. Many PAPR reduction methods have been devised and their comparison is usually based on the complementary cumulative distribution function (CCDF) of the PAPR. While this comparison is straightforward and easy to compute, its relationship with system performance metrics like the (uncoded) BER or the word error rate (WER) for coded systems is considerably more involved. We evaluate the impact of the PAPR on performance metrics like uncoded BER, EVM (error vector magnitude), mutual information and the WER for soft decoding. In this context, we find that system performance is not necessarily degraded by an increasing PAPR. We show that a high number of subcarriers, despite the corresponding high PAPR, is actually not a problem for the system performance and provide a simple explanation for this seemingly counter-intuitive fact.

## Multilevel Coding over Eisenstein Integers with Ternary Codes

- **Status**: ❌
- **Reason**: ternary GF(3) LDPC 기반 multilevel coding으로 비이진+신호성좌 응용 특이적, 떼어낼 바이너리 ECC 기법 없음
- **ID**: ieee:8661302
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Sebastian Stern, Daniel Rohweder, Juergen Freudenberger +1
- **PDF**: https://ieeexplore.ieee.org/document/8661302
- **Abstract**: This work introduces new signal constellations based on Eisenstein integers, i.e., the hexagonal lattice. These sets of Eisenstein integers have a cardinality which is an integer power of three. They are proposed as signal constellations for representation in the equivalent complex baseband model, especially for applications like physical-layer network coding or MIMO transmission where the constellation is required to be a subset of a lattice. It is shown that these constellations form additive groups where the addition over the complex plane corresponds to the addition with carry over ternary Galois fields. A ternary set partitioning is derived that enables multilevel coding based on ternary error-correcting codes. In the subsets, this partitioning achieves a gain of 4.77 dB, which results from an increased minimum squared Euclidean distance of the signal points. Furthermore, the constellation-constrained capacities over the AWGN channel and the related level capacities in case of ternary multilevel coding are investigated. Simulation results for multilevel coding based on ternary LDPC codes are presented which show that a performance close to the constellation-constrained capacities can be achieved.

## Two-Stage Dimension-Wise Coded Modulation for Four-Dimensional Hurwitz-Integer Constellations

- **Status**: ❌
- **Reason**: 4D Hurwitz 성좌 coded modulation으로 신호성좌 응용 특이적, LDPC는 시뮬 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8661331
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Sebastian Stern, Felix Frey, Johannes K. Fischer +1
- **PDF**: https://ieeexplore.ieee.org/document/8661331
- **Abstract**: In state-of-the-art fiber-optical systems and upcoming wireless standards, transmission over both planes of polarization of electromagnetic waves is an important approach to increase the spectral efficiency. To this end, four-dimensional modulation schemes are suited. In this paper, coded modulation for signal constellations over the Hurwitz integers, an isomorphic representation of the four-dimensional checkerboard lattice, is studied. In particular, a two-stage coding strategy is proposed where the components of the four-dimensional signal are preprocessed jointly before conventional coded-modulation techniques like bit-interleaved coded modulation or multistage decoding are applied individually per dimension. The theoretical capacities as well as numerical results from simulations with LDPC codes show that the proposed approach enables a performance gain over the straightforward application of ASK constellations per dimension or QAM constellations per polarization.

## Polar Code Construction for List Decoding

- **Status**: ❌
- **Reason**: polar SCL 디코딩용 코드 구성으로 비-LDPC, LDPC BP 이식 기법 없음
- **ID**: ieee:8661319
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Peihong Yuan, Tobias Prinz, Georg Boecherer +3
- **PDF**: https://ieeexplore.ieee.org/document/8661319
- **Abstract**: A heuristic construction of polar codes for successive cancellation list (SCL) decoding with a given list size is proposed to balance the trade-off between performance measured in frame error rate (FER) and decoding complexity. Furthermore, a construction based on dynamically frozen bits with constraints among the "low weight bits" (LWB) is presented. Simulation results show that the LWB-polar codes outperform the CRCpolar codes and the eBCH-polar codes under SCL decoding.

## On Decoding Schemes for the MDPC-McEliece Cryptosystem

- **Status**: ❌
- **Reason**: MDPC-McEliece 암호 디코딩 — 보안/암호 도메인, 새 BP 알고리즘이지만 GJS 공격 방어 목적이며 채널 ECC 비의존, 원칙 제외(보안)
- **ID**: ieee:8661339
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Hannes Bartz, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/8661339
- **Abstract**: In this paper, classical (iterative) decoding schemes for moderate-density parity-check (MDPC) codes are considered. The algorithms are analyzed with respect to their error-correction capability as well as their resilience against a recently proposed reaction-based key-recovery attack on a variant of the MDPC-McEliece cryptosystem by Guo, Johansson and Stankovski (GJS). New message-passing decoding algorithms are presented and analyzed. The proposed decoding algorithms have an improved error-correction performance compared to existing hard-decision decoding schemes and can reduce the effectiveness of the GJS reaction-based attack for an appropriate choice of the algorithm's parameters.

## Genetic Algorithm-based Polar Code Construction for the AWGN Channel

- **Status**: ❌
- **Reason**: polar code 구성(frozen bit 선택)으로 비-LDPC, 부호 비의존적 이식 디코더 기법 없음
- **ID**: ieee:8661304
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Ahmed Elkelesh, Moustafa Ebada, Sebastian Cammerer +1
- **PDF**: https://ieeexplore.ieee.org/document/8661304
- **Abstract**: We propose a new polar code construction framework (i.e., selecting the frozen bit positions) for the additive white Gaussian noise (AWGN) channel, tailored to a given decoding algorithm, rather than based on the (not necessarily optimal) assumption of successive cancellation (SC) decoding. The proposed framework is based on the Genetic Algorithm (GenAlg), where populations (i.e., collections) of information sets evolve successively via evolutionary transformations based on their individual error-rate performance. These populations converge towards an information set that fits the decoding behavior. Using our proposed algorithm, we construct a polar code of length 2048 with code rate 0.5, without the CRC-aid, tailored to plain successive cancellation list (SCL) decoding, achieving the same error-rate performance as the CRC-aided SCL decoding, and leading to a coding gain of 1dB at BER of 10(exp6). Further, a belief propagation (BP)-tailored polar code approaches the SCL error-rate performance without any modifications in the decoding algorithm itself.

## Signal Constellations for Physical-Layer Security

- **Status**: ❌
- **Reason**: 물리계층 보안 신호성좌/shaping으로 punctured LDPC는 베이스라인, 떼어낼 디코더/구성 기법 없음(보안 도메인)
- **ID**: ieee:8661330
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Johannes Pfeiffer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/8661330
- **Abstract**: In any transmission scheme, security against an eavesdropper is of importance. Contrary to classical encryption, security directly at the physical layer can be achieved by applying suited coding and modulation schemes. Meanwhile it has been shown that using higher-order constellations in combination with multilevel coding is able to improve the level of security. In this paper, the influence of the constellation, in particular its cardinality and its dimensionality, on the gained security is assessed. Moreover, the effect of signal shaping, i.e., choosing a non-uniform distribution of the signal points, is investigated. Based the channel capacity we present a criterion to optimize the distribution. The theoretical findings are supported by numerical simulations employing punctured LDPC codes.

## The Turbo Principle in Molecular Communications

- **Status**: ❌
- **Reason**: 분자통신 turbo principle/BICM 응용으로 LDPC가 베이스라인일 뿐 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:8661323
- **Type**: conference
- **Published**: 11-14 Feb.
- **Authors**: Martin Damrath, Max Schurwanz, Peter A. Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/8661323
- **Abstract**: This work introduces the turbo principle into the area of diffusion-based molecular communication (DBMC). By means of bit-interleaved coded modulation (BICM) at the transmitter side, channel encoder and modulator are serially concatenated with a random interleaver in-between. At the receiver side, iterative processing between detector and channel decoder is performed. The convergence of the iterative processing is investigated by an extrinsic information transfer (EXIT) chart analysis. In addition, the EXIT chart is used to predict the system performance and to determine the communication channel capacity including the DBMC channel. Bit-error-rate (BER) simulations are performed for advanced low-density parity-check (LDPC) codes. These numerical results confirm the benefit of turbo processing over non-iterative processing for DBMC applications.

## Soft Decision-based Data Detection Scheme for NR Communications System

- **Status**: ❌
- **Reason**: NR 256QAM soft-decision 데이터 검출 — 무선 통신 응용 특이적, LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:8669050
- **Type**: conference
- **Published**: 11-13 Feb.
- **Authors**: Sangmi Moon, Soonho Kwon, Hyeonsung Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/8669050
- **Abstract**: In this paper, the low-density parity-check code and 256 QAM of new radio (NR) technology were applied to meet the high reliability and high data-rate requirements of 5G communications systems. In addition, we propose a data detection scheme based on a soft decision to improve the reliability. The simulation results show that the proposed data detection scheme can improve the error rate and throughput of a conventional system.

## Deep Learning for Polar Codes over Flat Fading Channels

- **Status**: ❌
- **Reason**: Polar 부호 딥러닝 디코딩 — 비-LDPC, 부호 의존적 신경망 디코딩, 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:8669025
- **Type**: conference
- **Published**: 11-13 Feb.
- **Authors**: Ade Irawan, Gunawan Witjaksono, Wahyu Kunto Wibowo
- **PDF**: https://ieeexplore.ieee.org/document/8669025
- **Abstract**: This paper proposes a deep-neural-networks scheme for decoding polar coded short packets. We consider packet transmission over frequency-flat quasi-static Rayleigh fading channels, where the channel coefficient is constant over a packet but changes packet-by-packet. Potential applications of the proposed technique are machine-type communications, messaging services, smart metering networks, and other wireless sensor networks requiring high reliability and low-latency. Computer simulations results confirm that even with simple codebook construction for an additive white Gaussian noise (AWGN) channel without fading, the proposed technique closes to the theoretical outage and achieves the coding gain in fading channel. Analyses of the learning epochs and training signal-to-noise power ratio (SNR) selections are also presented to demonstrate the effectiveness of the technique.
