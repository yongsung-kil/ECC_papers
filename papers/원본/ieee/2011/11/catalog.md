# IEEE Xplore — 2011-11


## Overlapped message passing technique with resource sharing for high speed CMMB LDPC decoder

- **Status**: ✅
- **Reason**: Overlapped Message Passing+resource sharing+메모리 그룹핑 디코더 HW 아키텍처(D); CMMB 도메인이나 이식 가능 병렬화 기법
- **ID**: ieee:6131126
- **Type**: journal
- **Published**: November 2
- **Authors**: Joo-Yul Park, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/6131126
- **Abstract**: Today, demands for high speed digital communication are getting bigger due to wide deployment of 4G mobile communications and mobile TV services. Requirement for high speed data processing makes forward error correction crucial. LDPC is one of the most popular error correcting codes. In this paper, we propose a novel LDPC decoder for the China Multimedia Mobile Broadcasting (CMMB) standard. The LDPC decoding is carried out iteratively, which leads to relatively long decoding latency. Also, due to long code words, the amount of required memory is huge. To resolve these issues, we propose a novel Overlapped Message Passing (OMP) algorithm with an efficient resource sharing technique. Using the proposed method, we find the best permuted parity check matrix of the CMMB to improve the throughput while minimizing the memory requirement. Using the OMP algorithm only, we could improve the performance by 10%. To avoid potential memory access conflicts, a memory grouping technique to improve pipelining performance is also proposed. By applying all the techniques that we propose in this paper, we could improve the performance up to by 451.

## Design of LDPC Codes Based on Progressive Edge Growth Techniques for Block Fading Channels

- **Status**: ❌
- **Reason**: Root-Check LDPC를 block-fading용 PEG로 설계; 무선 fading 특이 코드설계라 바이너리 NAND 이식성 낮으나 PEG 구성 기법이라 애매—그러나 root-check은 fading 전용이라 out
- **ID**: ieee:6034392
- **Type**: journal
- **Published**: November 2
- **Authors**: Andre G. D. Uchoa, Cornelius Healy, Rodrigo C. de Lamare +1
- **PDF**: https://ieeexplore.ieee.org/document/6034392
- **Abstract**: A novel algorithm to design Root-Check LDPC codes based on Progressive Edge Growth (PEG) techniques for block-fading channels is proposed. The performance of the new codes is investigated in terms of the Frame Error Rate (FER) and the Bit Error Rate (BER). Numerical results show that the codes constructed by the proposed algorithm outperform codes constructed by the existing methods by 0.5dB.

## Generalized Adaptive Network Coded Cooperation (GANCC): A Unified Framework for Network Coding and Channel Coding

- **Status**: ❌
- **Reason**: 네트워크 코딩+채널코딩 통합(GANCC) 협력통신 응용; 떼어낼 NAND LDPC ECC 기법 없음
- **ID**: ieee:6024418
- **Type**: journal
- **Published**: November 2
- **Authors**: Xingkai Bao, Jing Tiffany Li
- **PDF**: https://ieeexplore.ieee.org/document/6024418
- **Abstract**: Previous work introduced the idea of matching network codes with network graphs to handle the network dynamics. This paper further integrates channel coding in the adaptive network coding framework through an elegant treatment of circulant shifting. Several code constructions are developed. Theoretical analysis and simulations show that the resultant generalized adaptive network coded cooperation (GANCC) is simple, adaptive, distributive, and capable of remarkable coding gains even with a very small number of cooperating users.

## Design of Multi-Edge-Type Bilayer-Expurgated LDPC Codes for Decode-and-Forward in Relay Channels

- **Status**: ❌
- **Reason**: 릴레이 채널 decode-and-forward용 bilayer/multi-edge-type LDPC 설계; 협력통신 전용 구조로 NAND 이식성 없음
- **ID**: ieee:6042298
- **Type**: journal
- **Published**: November 2
- **Authors**: Marwan H. Azmi, Jinhong Yuan, Gottfried Lechner +1
- **PDF**: https://ieeexplore.ieee.org/document/6042298
- **Abstract**: We consider the design of bilayer-expurgated low density parity-check (BE-LDPC) codes as part of a decode and-forward protocol for use over the full-duplex relay channel. A new ensemble of codes, termed multi-edge-type bilayer expurgated LDPC (MET-BE-LDPC) codes, is introduced where the BE-LDPC code design problem is transformed into the problem of optimizing the multinomials of a multi-edge-type LDPC code. We propose two design strategies for optimizing MET-BE-LDPC codes; the bilayer approach is preferred when the difference in SNR between the source-to-relay and the source to-destination channels is small, while the bilayer approach with intermediate rates is preferred when this difference is large. In both proposed design strategies multi-edge-type density evolution is used for code optimization. The resulting MET-BE-LDPC codes exhibit improved threshold and bit-error-rate performance as compared to previously reported bilayer LDPC codes.

## Design of Irregular Weighted Nonbinary Repeat-Accumulate Codes over GF(q) with q-ary Orthogonal Modulation Using a Gaussian Approximation

- **Status**: ❌
- **Reason**: 비이진 GF(q) repeat-accumulate; 비이진+비-LDPC라 제외
- **ID**: ieee:5957250
- **Type**: journal
- **Published**: November 2
- **Authors**: Yongsang Kim, Kyungwhoon Cheun, Hyuntack Lim
- **PDF**: https://ieeexplore.ieee.org/document/5957250
- **Abstract**: Using a Gaussian approximation to the distribution of the message vectors under density evolution, we design irregular weighted nonbinary repeat-accumulate codes over GF(q) with q-ary orthogonal modulation. The resulting codes achieve a frame error rate of 10-1 within 0.56 to 0.91 dB of channel capacity under the AWGN channel.

## Stability Outage Analysis for LDPC Codes

- **Status**: ❌
- **Reason**: 순수 이론 bound(stability outage probability/density evolution); 디코더·HW·구성 기여 없음, block fading 응용
- **ID**: ieee:6024417
- **Type**: journal
- **Published**: November 2
- **Authors**: Dieter Duyck, Joseph J. Boutros, Marc Moeneclaey
- **PDF**: https://ieeexplore.ieee.org/document/6024417
- **Abstract**: For a given channel instance and a fixed LDPC ensemble, a stability outage event is defined by the density evolution being unstable at the origin. The probability of such an event, referred to as Stability Outage Probability, is a useful lower bound for the word error rate. We formulate the stability outage probability for block fading channels and we introduce the stability diversity order. As a direct application, we show how the class of capacity-achieving ensembles on the erasure channel is bounded away from the outage limit on a block fading channel.

## Degree Distribution Design for LDPC Codes: A Derivative Matching Approach

- **Status**: ✅
- **Reason**: 바이너리 LDPC degree distribution 설계(derivative-matching/EXIT) — 이식 가능 코드설계 E
- **ID**: ieee:5997287
- **Type**: journal
- **Published**: November 2
- **Authors**: Enrico Paolini, Marco Chiani, Marc P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/5997287
- **Abstract**: A deterministic method to design degree distributions for low-density parity-check codes over the binary erasure channel is proposed. This method consists of matching the first and high-order derivatives of the extrinsic information transfer (EXIT) function of the variable node set to the corresponding derivatives of the inverse EXIT function of the check node set, in order to reduce the gap between the two curves in the EXIT chart. A sufficient condition for a check-concentrated distribution to achieve derivative matching up to some order is first obtained, and then a deterministic design algorithm, enabled by the Fourier-Budan theorem, is developed exploiting this sufficient condition. A comparison with other deterministic design techniques is also provided, revealing the potential of the proposed algorithm.

## Flexible LDPC decoder using stream data processing for 802.11n and 802.16e

- **Status**: ✅
- **Reason**: SIMD 기반 IRRWBF bit-flipping 디코더 SW 구현·데이터구조 가속(D/C); 부호 비의존 디코더 HW 기법 이식 가능
- **ID**: ieee:6131118
- **Type**: journal
- **Published**: November 2
- **Authors**: Honey Durga Tiwari, Huynh Ngoc Bao, Yong Beom Cho
- **PDF**: https://ieeexplore.ieee.org/document/6131118
- **Abstract**: Wireless data transmission standards like 802.16e, 802.11n, employ Low Density parity Check (LDPC) codes for error control coding. The bit flipping decoding algorithms presents a tradeoff between the error correcting capability, decoding resources and the decoding time. Software based LDPC decoders provide adaptation capabilities in system parameters such as block size and code rate. In a real-time, low-power mobile environments, the Single-Instruction Multiple-Data (SIMD) processor currently used for video processing, could also be used for the LDPC decoding. In this paper, the implementation efficient, reliability ratio-based, weighted bit flipping (IRRWBF) algorithm is presented using a flexible software based LDPC decoder. Compact data structures are proposed for performing the decoding using SIMD architecture. Based on the implementation on two commonly used SIMD architecture for mobile platform, it was found that the decoding speed can be increased by more than 2000% (using 64 bit SIMD registers with vector integer calculation) and 1800% (using 128 bit SIMD registers with vector floating point calculation). Experimental results for different code lengths of 802.16e and 802.11n show that decoding time in order of 1×10-3 ~10×10-3 seconds is achievable. Due to significantly high throughput and flexibility, the proposed design algorithm and data structure can easily be adapted to any energy-sensitive mobile devices employing SIMD processors1.

## Improved design of bit mapping based on EXIT-chart analysis for DVB-T2 system

- **Status**: ❌
- **Reason**: DVB-T2 bit mapping/DEMUX 설계(EXIT-chart 기반 변조 매핑); 코딩-변조 매핑이라 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6131128
- **Type**: journal
- **Published**: November 2
- **Authors**: Keqian Yan, Tao Cheng, Fang Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6131128
- **Abstract**: In this paper, we focus on the design of bit mapping scheme to improve the error-control performance for the second generation digital video broadcasting-terrestrial (DVB-T2) standard. Generally in the case of low-density parity-check (LDPC)-coded modulation system, the nonuniform bit reliabilities inherent to the high-order modulation and irregular LDPC code imply the mismatch between the decoder and the demodulator. Hence, the bit mapping is plugged between the two modules to match the unequal error protections (UEPs) of different coded bits to different modulation levels. This scheme gives a remarkable performance improvement with no added complexity in the bit-interleaved coded modulation (BICM) system. By performing the curve-fitting on the extrinsic information transfer (EXIT) chart, we propose a DEMUX design methodology to improve the bit mapping scheme. Design examples are given for the DVB-T2 system under the AWGN channel as well as the Rayleigh channel. Simulation results indicate that the proposed DEMUX schemes can even surpass the performance of the DEMUX operation specified in the DVB-T2 standard.

## Analog Joint Source-Channel Coding Using Non-Linear Curves and MMSE Decoding

- **Status**: ❌
- **Reason**: 아날로그 joint source-channel coding; LDPC ECC 기법 없음(소스-채널 결합 제외)
- **ID**: ieee:6007031
- **Type**: journal
- **Published**: November 2
- **Authors**: Yichuan Hu, Javier Garcia-Frias, Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/6007031
- **Abstract**: We investigate the performance of a discrete-time all-analog-processing joint source-channel coding system for the transmission of memoryless sources over average power constrained AWGN channels. First, N:1 bandwidth compression systems are analyzed and optimized. At the encoder, N samples of an i.i.d. source are directly mapped into one channel symbol using a non-linear curve. Different from previous work in the literature, we introduce an additional degree of freedom at the encoder, MMSE decoding instead of ML decoding is considered, and we focus on both high and low channel signal-to-noise ratio (CSNR) regions. By using MMSE decoding, the proposed system presents a performance very close to the theoretical limits, even at low CSNR, as long as the system parameters are properly optimized. Then, N:K bandwidth compression systems are constructed by parallel combination of an M:1 system and a 1:1 uncoded system, and the optimal power allocation between the two constituent systems is derived in order to maximize the overall output signal-to-distortion ratio (SDR). Finally, 1:2 bandwidth expansion systems using mapping functions similar to those used in 2:1 system are investigated. Different from digital systems, the proposed scheme does not require long block lengths to achieve good performance, and shows graceful degradation when the CSNR is lower than the one used for the design.

## Linear Precoding for MIMO Multiple Access Channels with Finite Discrete Inputs

- **Status**: ❌
- **Reason**: MIMO MAC 선형 프리코딩이 본질; LDPC는 BER 평가 베이스라인 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:6030127
- **Type**: journal
- **Published**: November 2
- **Authors**: Mingxi Wang, Weiliang Zeng, Chengshan Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6030127
- **Abstract**: In this paper, we study linear precoding for multiple-input multiple-output (MIMO) multiple access channels (MAC) with finite discrete inputs. We derive the constellation-constrained capacity region for the MIMO MAC with an arbitrary number of users and find that the boundary can be achieved by solving the problem of weighted sum rate maximization with constellation and individual power constraints. Due to the non-concavity of the objective function, we obtain a set of necessary conditions for the optimization problem through Karush-Kuhn-Tucker analysis. To find the optimal precoding matrices for all users, we propose an iterative algorithm utilizing alternating optimization strategy. In particular, each iteration of the algorithm involves the gradient descent update with backtracking line search. Numerical results show that when inputs are digital modulated signals and the signal-to-noise ratio is in the medium range, our proposed algorithm offers considerably higher sum rate than non-precoding and the traditional method which maximizes Gaussian-input sum capacity. Furthermore, a low-density parity-check coded system with iterative detection and decoding for MAC is presented to evaluate the bit error rate (BER) performance of precoders. BER results also indicate that the system with the proposed linear precoder achieves significant gains over the non-precoding system and the precoder designed for Gaussian inputs.

## Home gateway for three-screen TV using H.264 SVC and raptor FEC

- **Status**: ❌
- **Reason**: Raptor FEC 기반 홈게이트웨이 SVC 스트리밍; LDPC 아닌 fountain/erasure 응용
- **ID**: ieee:6131138
- **Type**: journal
- **Published**: November 2
- **Authors**: Eun-Seok Ryu, Nikil Jayant
- **PDF**: https://ieeexplore.ieee.org/document/6131138
- **Abstract**: This paper describes the design and implementation of a multimedia home gateway for threescreen television (3STV) service. The proposed in-home wireless network uses scalable video coding (SVC) and unequal error protection with Raptor forward error correction (FEC) for maximizing the quality of experience (QoE) over the variable-bandwidth, error-prone wireless network. The gateway incorporates (a) dynamic SVC layerswitching, which enables the server to perform selecting appropriate layers from SVC bitstreams, (b) adaptive Raptor FEC, which controls the overhead of Raptor FEC according to packet loss rate (PLR), (c) an efficient combination of (a) and (b), and (d) slice group-based selective streaming in the overall gateway architecture. The paper explains the home gateway architecture as well as experiments for performance evaluation as compared to that of traditional SVC streaming. In the experiments conducted, gains in video quality vary from 2 to 5dB in peak signal-to-noise ratio (PSNR), with corresponding subjective improvements. Overall reductions of bit rate at the input to the home gateway vary from 28% to 36%1.

## Analysis of MIMO Diversity With LDPC Codes Based on a Gaussian Approximation Approach Over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: MIMO 페이딩채널 LDPC BER 가우시안근사 성능분석으로 무선 응용 특이적이며 떼어낼 신규 디코더·구성·HW 없음(순수 분석)
- **ID**: ieee:6034532
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Beng Soon Tan, Kwok Hung Li, Kah Chan Teh
- **PDF**: https://ieeexplore.ieee.org/document/6034532
- **Abstract**: A low-density parity-check (LDPC)-coded multiple-input-multiple-output (MIMO) system is able to achieve excellent bit-error-rate (BER) performance over fading channels. The two types of MIMO systems examined in this paper are the transmit antenna selection/generalized selection combining (TAS/GSC) and orthogonal space-time block code (STBC). The approximate BER expressions of these two systems with LDPC codes using binary phase-shift keying signals over a Rayleigh fading channel are derived based on the Gaussian approximation (GA) approach. These expressions provide a computationally efficient method of analyzing the system performance, as compared with density evolution (DE) and simulation. The stability conditions for both systems using the DE and GA approaches are also presented.

## Weight Distributions of Regular Low-Density Parity-Check Codes Over Finite Fields

- **Status**: ❌
- **Reason**: 유한체(GF) 위 LDPC 무게분포·최소거리 점근 분석으로 비이진 LDPC 이론이며, 이식할 신규 디코더·구성·HW 없음(순수 이론 bound)
- **ID**: ieee:5960793
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Shengtian Yang, Thomas Honold, Yan Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/5960793
- **Abstract**: The average weight distribution of a regular low-density parity-check (LDPC) code ensemble over a finite field is thoroughly analyzed. In particular, a precise asymptotic approximation of the average weight distribution is derived for the small-weight case, and a series of fundamental qualitative properties of the asymptotic growth rate of the average weight distribution are proved. Based on this analysis, a general result, including all previous results as special cases, is established for the minimum distance of individual codes in a regular LDPC code ensemble.

## Improved Linear Programming Decoding of LDPC Codes and Bounds on the Minimum and Fractional Distance

- **Status**: ✅
- **Reason**: LP 디코딩 개선(relaxation tightening)+최소거리/fractional distance 하한 알고리즘(C); 바이너리 LDPC 디코더·구성 기여 이식 가능
- **ID**: ieee:5955120
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: David Burshtein, Idan Goldenberg
- **PDF**: https://ieeexplore.ieee.org/document/5955120
- **Abstract**: We examine LDPC codes decoded using linear programming (LP). Four contributions to the LP framework are presented. First, a new method of tightening the LP relaxation, and thus improving the LP decoder, is proposed. Second, we present an algorithm which calculates a lower bound on the minimum distance of a specific code. This algorithm exhibits complexity which scales quadratically with the block length. Third, we propose a method to obtain a tight lower bound on the fractional distance, also with quadratic complexity, and thus less than previously-existing methods. Finally, we show how the fundamental LP polytope for generalized LDPC codes and nonbinary LDPC codes can be obtained.

## Delayed Stochastic Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 신규 Delayed Stochastic 디코딩 알고리즘+VLSI 구현으로 HW 복잡도·메모리 절감, 바이너리 LDPC 디코더 HW 이식 가능(C/D)
- **ID**: ieee:5975253
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Ali Naderi, Shie Mannor, Mohamad Sawan +1
- **PDF**: https://ieeexplore.ieee.org/document/5975253
- **Abstract**: A new stochastic decoding algorithm, called Delayed Stochastic (DS) decoding, is introduced to implement low-density-parity-check (LDPC) decoders. The delayed stochastic decoding uses an alternative method to track probability values, which results in reduction of hardware complexity and memory requirement of the stochastic decoders. It is therefore suitable for fully-parallel implementation of long LDPC codes with applications in optical communications. Two decoders are implemented using the DS algorithm for medium (2048, 1723) and long (32768, 26624) LDPC codes. The decoders occupy 3.93- mm2 and 56.5- mm2 silicon area using 90-nm CMOS technology and provide maximum core throughputs of 172.4 and 477.7 Gb/s at [(Eb)/(No)]=5.5 and 4.8 dB, respectively.

## Inferring Rankings Using Constrained Sensing

- **Status**: ❌
- **Reason**: 순열 함수 복원/compressed sensing(l0 최적화) 문제로 LDPC ECC 무관, 이식 기법 없음
- **ID**: ieee:6071756
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Srikanth Jagabathula, Devavrat Shah
- **PDF**: https://ieeexplore.ieee.org/document/6071756
- **Abstract**: We consider the problem of recovering a function over the space of permutations (or, the symmetric group) over  $n$ elements from given partial information; the partial information we consider is related to the group theoretic Fourier Transform of the function. This problem naturally arises in several settings such as ranked elections, multi-object tracking, ranking systems, and recommendation systems. Inspired by the work of Donoho and Stark in the context of discrete-time functions, we focus on non-negative functions with a sparse support (support size  $\ll$ domain size). Our recovery method is based on finding the sparsest solution (through $\ell_0$ optimization) that is consistent with the available information. As the main result, we derive sufficient conditions for functions that can be recovered exactly from partial information through  $\ell_0$ optimization. Under a natural random model for the generation of functions, we quantify the recoverability conditions by deriving bounds on the sparsity (support size) for which the function satisfies the sufficient conditions with a high probability as $n \to \infty$. $\ell_0$ optimization is computationally hard. Therefore, the popular compressive sensing literature considers solving the convex relaxation, $\ell_1$ optimization, to find the sparsest solution. However, we show that $\ell_1$ optimization fails to recover a function (even with constant sparsity) generated using the random model with a high probability as $n \to \infty$. In order to overcome this problem, we propose a novel iterative algorithm for the recovery of functions that satisfy the sufficient conditions. Finally, using an Information Theoretic framework, we study necessary conditions for exact recovery to be possible.

## Deep-Space Optical Communications: Future Perspectives and Applications

- **Status**: ❌
- **Reason**: 심우주 광통신 개관 논문으로 LDPC/ECC 디코더·구성·HW 기여 없음
- **ID**: ieee:5985459
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Hamid Hemmati, Abhijit Biswas, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/5985459
- **Abstract**: The concept of deep-space optical communications was formulated shortly after the invention of lasers. The promise of laser communications, high data rate delivery with significantly reduced aperture size for the flight terminal, led to the pursuit of several successful experiments from Earth orbit and provided the incentive for further demonstrations to extend the range to deep space. This paper is aimed at presenting an overview of the current status of optical communications with an emphasis on deep space. Future perspectives and applications of optical communications related to near-Earth and interplanetary communications are also addressed.

## Reliability Options for Data Communications in the Future Deep-Space Missions

- **Status**: ❌
- **Reason**: 심우주 미션 신뢰성 옵션 서베이(CCSDS 채널코딩·ARQ 개괄)로 구체적 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:5982075
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Tomaso de Cola, Enrico Paolini, Gianluigi Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/5982075
- **Abstract**: Availability of higher capacity for both uplinks and downlinks is expected in the future deep-space missions on Mars, thus enabling a large range of services that could eventually support human remote operations. The provisioning for deep-space links offering data rate up to several megabits per second will be a crucial element to allow new services for the space domain along with the common telecommand and telemetry services with enhanced communication capabilities. On the other hand, also the geometry proper of this scenario with orbiting and landed elements sharing only partial visibility among them and towards Earth provides another challenge. This paper surveys the reliability options that are available in the Consultative Committee for Space Data Systems (CCSDS) Protocol Stack for application in the deep-space missions. In particular, the solutions implemented from the physical up to the application layer are illustrated in terms of channel coding and Automatic Retransmission reQuest (ARQ) schemes. Finally, advanced reliability strategies possibly applicable in next-generation deep-space missions are explored as well.

## Asymptotic Capacity of the Separated MIMO Two-Way Relay Channel

- **Status**: ❌
- **Reason**: MIMO 양방향 중계채널 용량 분석(lattice code/GSVD precoding)으로 LDPC 무관, ECC 기법 없음
- **ID**: ieee:6071760
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Hyun Jong Yang, Joohwan Chun, Arogyaswami Paulraj
- **PDF**: https://ieeexplore.ieee.org/document/6071760
- **Abstract**: A multiple-input multiple-output two-way relay channel consisting of two communication nodes and a full-duplex relay node in which no direct link exists between the two communication nodes is considered. We propose an achievable scheme that employs horizontally encoded lattice codes combined with generalized singular value decomposition-based precoding for the first phase. The second phase of the proposed scheme follows the fundamentals of the previous scheme, which uses vertically encoded structural bining, with the only difference that the added codeword of the two codewords from the communication nodes, instead of those two individual codewords, is decoded and retransmitted in the proposed scheme. We show that the proposed scheme achieves the cut-set bound asymptotically as the signal-to-noise ratios of the channels tend to infinity.

## Coded Hierarchical Modulation for Wireless Progressive Image Transmission

- **Status**: ❌
- **Reason**: 무선 점진적 이미지 전송용 계층변조+CRC+convolutional 코딩으로 LDPC 무관, 떼어낼 ECC 기법 없음(JSCC/무선 응용 특이적)
- **ID**: ieee:5963731
- **Type**: journal
- **Published**: Nov. 2011
- **Authors**: Suayb S. Arslan, Pamela C. Cosman, Laurence B. Milstein
- **PDF**: https://ieeexplore.ieee.org/document/5963731
- **Abstract**: A robust coded scheme for progressive multimedia transmission is proposed for additive white Gaussian noise, flat Rayleigh fading channels, and frequency-selective channels using different unequal error protection methods in combination. Hierarchical modulation is coupled with a packetization/combining strategy and an efficient channel encoder consisting of a cyclic redundancy check outer coder concatenated with an inner rate-compatible punctured convolutional coder. Distortion-optimal hierarchical parameters are jointly chosen with the set of channel coding parameters on a packet-switched wireless network with fixed length packets. A lower bound for the performance improvement of the proposed system is derived and shown to give significant gains at lower packet sizes and higher transmission rates. The proposed system is also shown to outperform several existing schemes for realistic wireless channels.

## Joint design of LDPC and Physical-layer Network Coding for bi-directional relay system in the presence of insufficient timing synchronization

- **Status**: ❌
- **Reason**: LDPC와 물리계층 네트워크코딩 결합(릴레이 동기화) — 무선 응용 특이적, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6096812
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Wenwen Liang, Kui Xu, Hua Tian +1
- **PDF**: https://ieeexplore.ieee.org/document/6096812
- **Abstract**: Physical-layer Network Coding (PNC) has shown its power for improving the throughput effectively of the bi-directional relay system. Most of the existing PNC schemes are carried out under the assumption of perfect synchronization. In this paper, we provide some new insights into the joint design of Low-Density Parity-Check (LDPC)-coded and PNC for asynchronous bi-directional relay system with BPSK signaling. In particular, a novel LDPC and PNC joint design method is proposed for mitigating the performance degradation caused by the different timing offsets between relay and two source nodes. Simulation results show that the proposed joint design of LDPC and PNC scheme outperforms traditional method for bi-directional relay system in the presence of insufficient timing synchronization.

## Construction of irregular quasi-cyclic LDPC codes based on Euclidean geometries

- **Status**: ✅
- **Reason**: Euclidean geometry 기반 irregular QC-LDPC 구성(large girth, hyperplane 분해, degree 분포 최적화) — 바이너리 코드 설계(E) 기여
- **ID**: ieee:6096743
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Xueqin Jiang, Moon Ho Lee, Xiaofei Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/6096743
- **Abstract**: This paper presents a method to the construction of irregular low-density parity-check (LDPC) codes based on Euclidean geometries over the Galois field. Codes constructed by this method are quasi-cyclic (QC) and have large girths. The proposed irregular LDPC codes having flexible column/row weights are obtained with a hyperplane decomposing method in Euclidean geometries. Therefore, the degree distributions of proposed irregular LDPC codes can be optimized by technologies like the curve fitting approach in the extrinsic information transfer (EXIT) charts. Simulation results show that these codes perform very well with an iterative decoding over the AWGN channel.

## Polar codes and its application in speech communication

- **Status**: ❌
- **Reason**: Polar code의 음성통신 응용, LDPC는 비교 베이스라인뿐 — 비-LDPC 부호이고 떼어낼 BP 이식 기법 없음
- **ID**: ieee:6096731
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Shengmei Zhao, Peng Shi, Bei Wang
- **PDF**: https://ieeexplore.ieee.org/document/6096731
- **Abstract**: Polar codes are a class of codes proposed currently, which can achieve the capacity of binary symmetric channel with low encoding and decoding algorithm. However, its application is less discussed in the literature. In this paper, we discuss the application of Polar codes in speech communication, and compare the performance of systems with that of low density parity check (LDPC) codes both in Additive white Gaussian channel and Rayleigh channel. The numerical results show that the system coded by Polar codes has a better performance than that coded by LDPC codes, and the system is good with lower code rate and longer code length.

## Joint LDPC and physical network coding with power allocation for two way wireless relaying

- **Status**: ❌
- **Reason**: 무선 양방향 릴레이 채널/네트워크코딩+전력할당 결합; LDPC는 베이스라인이고 NAND로 이식할 디코더·HW·코드설계 기여 없음
- **ID**: ieee:6096840
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Kui Xu, Youyun Xu, Wenwen Liang +2
- **PDF**: https://ieeexplore.ieee.org/document/6096840
- **Abstract**: In this paper, we investigate the joint design of channel and network coding with power allocation in bi-directional relaying systems and propose a combined low complexity LDPC and physical network coding scheme. For the same LDPC codes employed at both source nodes, we show that the relay can decodes the network coded code-words from the superimposed signal received from the BPSK-modulated multiple-access channel. The outage probability analysis shows that the bidirectional relaying system obtains the optimal performance while the total transmit power of the two source nodes equal to the relay node. Simulation results shown that the proposed joint LDPC and physical network coding method outperforms the existing MMSE based LDPC and network coding method over AWGN and complex MAC channel.

## Design of LDPC code strategy for orthogonal modulation

- **Status**: ❌
- **Reason**: MBOK 직교변조용 GF(q) LDPC 결합 전략 — 비이진 LDPC이며 변조-특이 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:6096777
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: HaiYang Hu, Yukui Pei, Ning Ge
- **PDF**: https://ieeexplore.ieee.org/document/6096777
- **Abstract**: M-ary bi-orthogonal keying (MBOK) is a kind of orthogonal modulation that uses the spectrum efficiency to obtain a power gain in the power limited system. In this paper, coding strategy combined with MBOK is investigated to get an optimal combination performance. Specifically, advantages of orthogonal modulation is analyzed and compared with spread spectrum method. Then the error pattern of MBOK modulated signals through AWGN channel is studied to illustrate problems of the combination of LDPC and MBOK. Meanwhile, we investigate the matched combination strategy when modulated by MBOK. And BICM is employed to preserve the soft iterative decoding information when unmatched. At last, we test the performances of these three combination strategies in AWGN channel. According to simulation results, matched GF(q) LDPC strategy for MBOK modulation has at least 0.5db advantage over the unmatched combination when the BER is 1E-5. The gap to Shannon limit could be less than 0.5db. We also discover the unmatched combination could be improved by using BICM, but the performance is still a little worse than the matched combination.

## Improved interleaving scheme for DVB-S2 BICM system

- **Status**: ❌
- **Reason**: DVB-S2 BICM 인터리버 개선 — 위성통신 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6096826
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Kangming Jiang, Ying Wang
- **PDF**: https://ieeexplore.ieee.org/document/6096826
- **Abstract**: DVB-S2 is used as the most popular standard for satellite communications for its efficient BICM structure and outstanding error performance. And the interleaver of DVB-S2 is a simple model with rows-reading columns-writing, wich is convenient for implementation. However, the error performance would be affected by the multi-edge modulated symbols, which can not be eliminated by the original simple interleaver. So in this paper, we focus on the impact of multi-edge LDPC symbols on the performance of the DVB-S2 system, and propose an improved interleaving scheme to prevent the performance degradation caused by the multi-edge modulated symbols. The new interleaving shceme can improve the decoding performance of DVB-S2 BICM system with a little extra computational complexity compared with the original interleaver. Simulation results show that the DVB-S2 BICM system with our proposed interleaver outperforms the traditional system in different code lengths, rates, modulations and channels.

## The investigation of mapping schemes for LDPC-coded modulated systems

- **Status**: ❌
- **Reason**: BICM 변조 매핑 설계(Gray/labeling); LDPC는 부수적, NAND 바이너리 ECC로 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:6096877
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Ying Wang, Kangming Jiang
- **PDF**: https://ieeexplore.ieee.org/document/6096877
- **Abstract**: In conventional bit-interleaved coded modulation (BICM) system with convolutional codes, Gray mapping has been proved to be the best candidate over the additive white Gaussian noise (AWGN) channel. However, when it comes to LDPC-coded BICM and BICM with iterative decoding (BICM ID) systems, Gray mapping doesn't always promise better performance. A simple class of labeling maps that significantly improves the bit error rates (BER) is presented. Meanwhile, we found out that in these systems the overall performance of modulation depends not merely on the constellation schemes, but also the decoding strategy. Compared with the conventional parameters based Euclidean distance, mutual information theory is proved to be a more accurate tool. The simulation results show that only when combined with the suitable mapping and the "state-of-art" decoding algorithms, the BICM system can give full play to their potential.

## Phase noise mitigation in high frequency band SC-MIMO systems

- **Status**: ❌
- **Reason**: SC-MIMO 위상잡음 제거 기법, LDPC 무관 — 무선 응용 특이적
- **ID**: ieee:6096752
- **Type**: conference
- **Published**: 9-11 Nov. 
- **Authors**: Hui Xie, Lin Gui, Jian Xiong
- **PDF**: https://ieeexplore.ieee.org/document/6096752
- **Abstract**: This paper proposes a phase noise cancellation scheme in high frequency band single-carrier (SC) multiple input and multiple output (MIMO) systems by employing a phase tracking loop. Due to the level of noisy oscillators grow quadratically in terms of corresponding carrier frequency, the overall system performance in 6-15GHz band is seriously deteriorated by the phase noise. In the case, a simple phase tracking loop in combination with a modified equalizer is carefully designed for SC-MIMO systems. Simulation results indicate that the proposed mitigation strategy could effectively suppress the performance degradation effects from the phase noise. The analytical results indicate that the symbol-error-rate (SER) performance is improved in contrast to the scheme without phase tracking loop.

## A technique to improve the performance of fixed-point TDMP decoding of QC-LDPC codes in the presence of SNR estimation error

- **Status**: ✅
- **Reason**: QC-LDPC TDMP 디코더의 고정소수점 8비트 양자화/포화 완화 기법 - C/D 이식 가능 (NAND LLR 양자화와 직결)
- **ID**: ieee:6127748
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: JaWone A. Kennedy, Daniel L. Noneaker
- **PDF**: https://ieeexplore.ieee.org/document/6127748
- **Abstract**: Most high-throughput, fixed-point processors offer at least two options for arithmetic operations: 8-bit arithmetic, and 16-bit arithmetic. The lower resolution provides higher computational throughput at the cost of poorer performance in many applications. We investigate the effect of the resolution of saturating, fixed-point arithmetic on the performance of the turbo-decoding message-passing algorithm with quasi-cyclic low-density parity-check codes. We consider limits on the magnitude of extrinsic updates as a means to mitigate the effect of posterior-value saturation on the decoder's performance. We show that a fixed limit on updates only partially overcomes the greater effect of saturation in 8-bit operations, whereas a limit that depends on the degree of the variable node results in performance almost as good as what is possible with 16-bit operations.

## EXIT chart analysis and design of non-binary protograph-based LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) 프로토그래프 LDPC 설계 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6127733
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Ben-Yue Chang, Lara Dolecek, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/6127733
- **Abstract**: Binary LDPC codes built out of protographs constitute a class of high-performance structured codes. In this paper we carefully extend the code construction to the non-binary case. We present a method based on a newly developed EXIT-chart approach to efficiently design non-binary protograph-based LDPC codes with good properties. The results presented here can be particularly useful in the development of coding schemes that can be effectively combined with non-binary modulation in bandwidth-efficient high-speed communication systems.

## An LDPC-based key-agreement scheme over the fast-fading wiretap channel

- **Status**: ❌
- **Reason**: 무선 도청채널 LDPC 키합의(보안) — 기법은 부호탐색으로 secrecy 최적화, 보안 전용이며 이식할 채널ECC 기법 없음
- **ID**: ieee:6127689
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Chan Wong Wong, Tan F. Wong, John M. Shea
- **PDF**: https://ieeexplore.ieee.org/document/6127689
- **Abstract**: This paper considers the design of practical schemes that enable two terminals, namely a source and a destination, to agree on a secret key in the presence of an eavesdropper (wire-tapper). The channel model considered is a fast Rayleigh fading wiretap channel with the constraints of quadrature phase-shift-keyed source symbols and hard-decision destination quantization. It is assumed that there exists a public feedback channel between the source and destination to facilitate the key-agreement process, however, any communication over the public channel is perfectly observed by the wiretapper. A key-agreement scheme employing irregular low-density parity-check (LDPC) codes is proposed, and its secrecy performance is measured in terms of the key rate between the source and destination and the leakage rate about the secret key at the wiretapper. A code search algorithm is also developed to design irregular LDPC codes to achieve good secrecy performance under various channel conditions.

## FPGA implementation of a coherent SOQPSK-TG demodulator

- **Status**: ❌
- **Reason**: SOQPSK 복조기 FPGA 구현 — LDPC는 후단 부수 언급, 떼어낼 디코더 HW 기법 없음
- **ID**: ieee:6127715
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Ehsan Hosseini, Erik Perrins
- **PDF**: https://ieeexplore.ieee.org/document/6127715
- **Abstract**: In this paper, we present a hardware implementation of a demodulator for shaped offset quadrature phase shift keying, telemetry group version (SOQPSK-TG). The demodulator is implemented based on maximum likelihood sequence detection of SOQPSK using the soft-output Viterbi algorithm (SOVA). Symbol timing and carrier phase recovery are fundamental operations required for the best symbol detection. We describe how to generate time and phase error signals from the SOVA which are fed in two separate discrete phase locked loops (PLLs). The PLLs work along with other blocks including a down converter, matched filters and the SOVA in order to provide optimal sequence detection of the received signal from analog to digital converter. Additionally, the SOVA provides output reliabilities for the detected bits which can be used by iterative error correction schemes such as low-density parity-check (LDPC) codes. Moreover, we propose a simplified implementation of the SOVA based on the two-traceback method which reduces the overall size of the demodulator by 25%. The simplification causes a slight degradation in the output reliabilities which is examined by LDPC decoding of its output. The demodulator is targeted for field programmable gate arrays (FPGAs) which provide us with flexibility and rapid prototyping. Finally, the FPGA performance and utilization results along with bit error rate performance of both demodulator and LDPC coded system are presented.

## LDPC coded OFDM system design and performance verification on a realistic underwater acoustic channel model

- **Status**: ❌
- **Reason**: 수중음향 LDPC-OFDM 시스템 설계 — 표준 LDPC 채널 적용, 새 디코더·구성 기여 없음
- **ID**: ieee:6127648
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Hyeong-Won Jeon, Su-Je Lee, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/6127648
- **Abstract**: The underwater acoustic channel (UAC) is highly frequency selective; the degree of selectiveness depends on a detailed geometry of the channel. Further, the response changes over time as conditions affecting the response (such as water temperature, sea surface wind, salinity, etc.) are time-varying. A system design to deal with the frequency and time selective channel in UAC, therefore, becomes very challenging. We consider low density parity check (LDPC) coded orthogonal frequency division multiplexing (OFDM) system to deal with deep sub-band fading problems. In this paper, we aim to, first, provide a detailed realistic UAC model as we have noted that most LDPC coded OFDM systems have not been tested under realistic channels; second, to design a robust LDPC coded OFDM system; and third to test the proposed system under a variety of conditions using the channel model. We show robustness of the proposed system in simulation under a number of realistic channel conditions.

## Improving DVB-S2 performance through constellation shaping and iterative demapping

- **Status**: ❌
- **Reason**: DVB-S2 콘스텔레이션 셰이핑·반복 디매핑 — LDPC는 표준 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:6127729
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Xingyu Xiang, Matthew C. Valenti
- **PDF**: https://ieeexplore.ieee.org/document/6127729
- **Abstract**: Because it is widely supported by commercial-off-the-shelf (COTS) technology, the DVB-S2 waveform standard has become an attractive solution for military communication links. The waveform uses a combination of amplitude-phase-shift keying (APSK) modulation and low-density parity-check (LDPC) codes. Typical DVB-S2 implementations select signals from the APSK signal set with uniform probability. However, information-theoretic results suggest that performance may be improved by selecting lower-energy signals more frequently than higher-energy signals. In this paper, we propose and analyze a DVB-S2-compatible system that shapes the APSK constellation by selecting signals with a nonuniform probability. The receiver iterates between the APSK demapper, the shaping decoder, and the LDPC decoder. Using 32-APSK and a rate of 3 data bits per symbol, the system described in this paper achieves a gain of over 1 dB relative to a standard DVB-S2 system (i.e. one that does not use shaping or iterative demodulation) in additive white Gaussian noise (AWGN) at a bit-error rate of 10-5. About 0.7 dB of the gain can be attributed to shaping, and rest of the gain can be attributed to iterative demodulation and decoding. Lesser gains can be achieved over Rayleigh fading channels.

## On Hybrid ARQ adaptive Forward Error Correction in wireless sensor networks

- **Status**: ❌
- **Reason**: WSN용 HARQ+BCH FEC — 비-LDPC 부호이며 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6119788
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Oskar Eriksson, Erik Björnemo, Anders Ahlén +1
- **PDF**: https://ieeexplore.ieee.org/document/6119788
- **Abstract**: The use of wireless technology in the process industry is becoming increasingly important to obtain fast deployment at low cost. However, poor channel quality often leads to retransmissions, which are governed by Automatic Repeat Request (ARQ) schemes. While ARQ is a simple and useful tool to alleviate packet errors, it has considerable disadvantages: retransmissions lead to an increase in energy expenditure and latency. The use of Forward Error Correction (FEC) however offers several advantages. We consider a Hybrid-ARQ-Adaptive-FEC scheme (HAF) based on BCH codes and Channel State Information. This scheme is evaluated on AWGN and fading channels. It is shown that HAF offers significantly improved performance both in terms of energy efficiency and latency, as compared to ARQ.

## Beam forming using an iterative bootstrapping technique

- **Status**: ❌
- **Reason**: 빔포밍 채널 추정 부트스트래핑 — LDPC 무관, ECC 기법 없음
- **ID**: ieee:6127682
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Y. Vasavada, X. Huang, C. Ravishankar +1
- **PDF**: https://ieeexplore.ieee.org/document/6127682
- **Abstract**: In this paper, we describe a novel bootstrapping technique that iteratively improves an initial estimate of a set of unknown complex-valued channel parameters.

## Power loading for OFDM in tactical packet radio systems

- **Status**: ❌
- **Reason**: OFDM 전력로딩·적응 코딩변조 — 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6127734
- **Type**: conference
- **Published**: 7-10 Nov. 
- **Authors**: Michael A. Juang, Michael B. Pursley
- **PDF**: https://ieeexplore.ieee.org/document/6127734
- **Abstract**: In orthogonal frequency division multiplexing (OFDM) systems, transmitting with different power levels on each subcarrier, known as power loading, can improve performance. Power loading algorithms process channel state information to determine the power distribution that optimizes or improves the performance. Most previous investigations of power loading are for OFDM systems that do not use error-control coding. However, their objective of minimizing the bit error probability at the demodulator output does not minimize the packet error probability when error-control codes are used. Because modern OFDM systems use error-control coding, the utility of those previous results is questionable. Furthermore, the power loading algorithms that minimize the bit error probability use approximations for the error probability that are not accurate for the signal-to-noise ratios of interest in these systems. We consider half-duplex tactical packet communications with OFDM modulation, error-control coding, and iterative decoding. We also investigate the adaptation of the code rate and subcarrier modulation without power loading, as an alternative to power loading. Adaptive coding and modulation is shown to provide higher throughput and more robust performance than power loading. Using a combination of analysis and simulation, we determine the effect of power loading on the binary symbol error probability at the demodulator output, the packet error probability at the decoder output, and the throughput of the packet radio system.

## Trellis based Extended Min-Sum for decoding nonbinary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary GF(q)) LDPC용 T-EMS 디코더 — 비이진 LDPC는 NAND 바이너리 표준에서 제외
- **ID**: ieee:6125307
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Erbao Li, Kiran Gunnam, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6125307
- **Abstract**: In this paper, we propose a new method to implement the Extended Min-Sum (EMS) algorithm based on trellis representation of inputting messages to the check node. The original EMS reduces the decoding complexity by choosing only nm most reliable values and by introducing the idea of configuration sets conf(nm, nc), where nc is the number of deviations from the most reliable output configuration. We propose to work directly on the deviation space by building a configuration trellis based on delta messages, which serves as a new reliability measure. The algorithm is called trellis-EMS (T-EMS). By using the new trellis representation, only nc+1 minimum values from each row of the trellis need to be considered, which reduces the ordering complexity. The trellis representation in the deviation space also reduces the number of output configurations tested, without any performance degradation. Our method is especially suitable for moderate field size q and large check node degree nonbinary LDPC codes.

## Extended non-binary Low-Density Parity-Check codes over erasure channels

- **Status**: ❌
- **Reason**: 비이진 LDPC 기반 확장부호+erasure 채널 — 비이진 LDPC 제외 대상
- **ID**: ieee:6125322
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Lam Pham Sy, Valentin Savin, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6125322
- **Abstract**: Based on the extended binary image of non-binary LDPC codes, we propose a method for generating extra redundant bits, such as to decreases the coding rate of a mother code. The proposed method allows for using the same decoder, regardless of how many extra redundant bits have been produced, which considerably increases the flexibility of the system without significantly increasing its complexity. Extended codes are also optimized for the binary erasure channel, by using density evolution methods. Nevertheless, the results presented in this paper can easily be extrapolated to more general channel models.

## Rate adaptive non-binary LDPC codes with low encoding complexity

- **Status**: ❌
- **Reason**: rate adaptive non-binary LDPC (GF) — 비이진 LDPC 제외
- **ID**: ieee:6190086
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Nicholas B. Chang
- **PDF**: https://ieeexplore.ieee.org/document/6190086
- **Abstract**: For error-correction codes, the optimal coding rate can vary and depend on factors including channel, time-varying fading, environmental interference, power, bandwidth allocation, communication content, and application. Rate adaptive coding schemes are thus important for robust communications. This writeup proposes and studies a rate adaptive low density parity check (LDPC) coding scheme using non-binary Galois fields (GF). The algorithm uses a single low complexity encoding structure, but maintains strong near-capacity performance at arbitrary rational rates. The rate adaptive encoder can be used in a space-time code for multiple-input multiple-output (MIMO) communication systems and is shown to achieve near capacity performance at various rates and different MIMO configurations.

## Improved iterative soft-reliability-based majority-logic decoding algorithm for non-binary low-density parity-check codes

- **Status**: ❌
- **Reason**: non-binary LDPC ISRB 다수결 디코딩 개선 — 비이진 LDPC 제외
- **ID**: ieee:6190138
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6190138
- **Abstract**: Non-binary low-density parity-check (LDPC) codes have some advantages as opposed to their binary counterparts, but unfortunately their decoding complexity is a significant challenge. Hence, the iterative soft-reliability-based (ISRB) majority-logic decoding algorithm is attractive for non-binary LDPC codes, since it involves only finite field additions and multiplications as well as integer additions and comparisons. In this paper, we propose an improved ISRB majority-logic decoding algorithm by using a new reliability update. Our improved algorithm achieves better error performance and faster convergence, while further reducing the computational complexity. For instance, for a (16, 16)-regular (255, 175) cyclic Euclidean geometry LDPC code over GF(28), the proposed algorithm achieves a 0.15 dB coding gain and improves the convergence speed by 10% at a block error rate of 10-4 versus the ISRB majority-logic decoding algorithm. Compared with the ISRB majority-logic decoding algorithm, the proposed algorithm requires the same numbers of finite field additions and multiplications but fewer integer additions and comparisons. Furthermore, the ISRB majority-logic decoding algorithm is based on the accumulation of reliability information, and hence the numerical range of the reliability information increases with iterations. In contrast, the proposed reliability update has a fixed numerical range and thus simplifies hardware implementations.

## Improved cooperative spectrum sensing using belief propagation algorithm and energy detection

- **Status**: ❌
- **Reason**: 인지무선 협력 스펙트럼 센싱에 BP 적용 — 채널 ECC가 아닌 센서 네트워크 검출, 떼어낼 LDPC 디코더 없음
- **ID**: ieee:6125404
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Pranav Sakulkar, Adrish Banerjee
- **PDF**: https://ieeexplore.ieee.org/document/6125404
- **Abstract**: In this paper, we describe a new method for improving cooperative spectrum sensing in cognitive radio. We introduce a new block based on belief propagation algorithm in the conventional structure of cooperative spectrum sensing. The belief propagation block allows propagation of correct beliefs over a network of secondary users and thus in turn improves the primary user detection. We consider the network of secondary users as Tanner graph [1] and propose a scheme based on belief propagation over these graphs to improve the local decisions at the secondary users before sending the decisions to the fusion center. We demonstrate the improvement in probability of detection, Pd using our belief propagation block by simulating the performance of cooperative spectrum sensing using energy detection over Rayleigh fading channels. The proposed scheme provides improvement over conventional cooperative spectrum sensing for both soft combination and hard combination schemes.

## GPU accelerated scalable parallel decoding of LDPC codes

- **Status**: ✅
- **Reason**: GPU 기반 스케일러블 병렬 LDPC 디코더 + 적응 성능튜닝; 이식 가능한 병렬화 HW/SW 아키텍처(D)
- **ID**: ieee:6190388
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Guohui Wang, Michael Wu, Yang Sun +1
- **PDF**: https://ieeexplore.ieee.org/document/6190388
- **Abstract**: This paper proposes a flexible low-density parity-check (LDPC) decoder which leverages graphic processor units (GPU) to provide high decoding throughput. LDPC codes are widely adopted by the new emerging standards for wireless communication systems and storage applications due to their near-capacity error correcting performance. To achieve high decoding throughput on GPU, we leverage the parallelism embedded in the check-node computation and variable-node computation and propose a parallel strategy of partitioning the decoding jobs among multi-processors in GPU. In addition, we propose a scalable multi-codeword decoding scheme to fully utilize the computation resources of GPU. Furthermore, we developed a novel adaptive performance-tuning method to make our decoder implementation more flexible and scalable. The experimental results show that our LDPC decoder is scalable and flexible, and the adaptive performance-tuning method can deliver the peak performance based on the GPU architecture.

## LDPC codes based on Progressive Edge Growth techniques for block fading channels

- **Status**: ✅
- **Reason**: PEG 기반 Root-Check LDPC 구성, girth 최대화 제약 — 바이너리 코드설계(E) 이식 가능
- **ID**: ieee:6125390
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: André G. D. Uchôa, Cornelius Healy, Rodrigo C. de Lamare +1
- **PDF**: https://ieeexplore.ieee.org/document/6125390
- **Abstract**: We propose an algorithm to design Root-Check LDPC codes based on Progressive Edge Growth (PEG) techniques for block-fading channels. The proposed algorithm imposes some restrictions on the traditional PEG algorithm to ensure that the LDPC code generated is Root-Check with the largest possible girth. The performance is investigated by means of the outage probability. By doing so, the codes generated by our proposed algorithm are shown to outperform the existing methods for generating Root-Check LDPC codes.

## Rate-compatible LDPC codes using optimized dummy bit insertion

- **Status**: ✅
- **Reason**: 단일 mother LDPC에서 dummy bit 삽입으로 rate 매칭+error floor 개선 신규 규칙 — 바이너리 LDPC 코드설계(E)
- **ID**: ieee:6125400
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Moritz Beermann, Tobias Breddermann, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/6125400
- **Abstract**: Much attention has been paid to Low-Density Parity-Check (LDPC) codes since their rediscovery by MacKay. They belong to the most powerful channel coding techniques known today and have a broad range of applications. In wireless communication systems it is desirable to be able to adjust the code rate of the employed channel coding scheme (rate-matching) to allow for a flexible strength of error protection for different services and to be able to adapt to the varying quality of the wireless transmission channel. Many of the current systems that employ LDPC codes like, e.g., WiMAX or WLAN specify separate codes for each supported code rate. This paper, in contrast, addresses the problem of using only one mother code and matching (almost) arbitrary code rates that are lower than the mother code rate by inserting known (dummy) bits into the information bit sequence before encoding (also known as pruning or code shortening). We present a novel rule of determining (heuristically) optimized positions of dummy bits within the information bit sequence suitable for LDPC codes. Simulation results show that the frame error rate performance can be improved by the novel approach of dummy bit insertion especially in the error floor region.

## Achieving flexibility in LDPC code design by absorbing set elimination

- **Status**: ✅
- **Reason**: 바이너리 SCB(circulant) LDPC absorbing set 제거·error floor 개선 코드설계 기법(E) — 이식 가능
- **ID**: ieee:6190087
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jiajun Zhang, Jiadong Wang, Shayan Garani Srinivasa +1
- **PDF**: https://ieeexplore.ieee.org/document/6190087
- **Abstract**: Low-density parity-check (LDPC) codes are attractive since their performance is known to approach the Shannon limits for suitably large block lengths. However, for moderate block lengths, error floors still jeopardize the performance even of well-designed LDPC codes. Previous work has shown that the error floor of a broad class of LDPC codes is due to certain graphical structures called absorbing sets. Separable, circulant-based (SCB) codes represent a general family of high-performance, hardware-friendly LDPC codes built out of circulants. A recently proposed technique applies row selection and column elimination methods to SCB codes to dramatically decrease error floors by avoiding certain small dominant absorbing sets in a principled way. This paper focuses on improving the greedy column elimination method to achieve greater flexibility in code rate while provably avoiding small dominant absorbing sets. Flexibility and low implementation complexity are therefore possible without sacrificing SCB code performance.

## Finite-length rate-compatible LDPC codes based on extension techniques

- **Status**: ✅
- **Reason**: 유한길이 rate-compatible LDPC 구성(cycle counting+ACE 기반 확장) - E 코드설계 이식 가능
- **ID**: ieee:6125306
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jingjing Liu, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/6125306
- **Abstract**: We propose two innovative extension schemes for Rate-Compatible (RC) Low-Density Parity-Check (LDPC) codes with short/moderate block lengths. The proposed designs are based on the counting cycles algorithm and the Approximate Cycle Extrinsic Message Degree (EMD). Our layer-structured extension schemes enjoy a linear-time encodable ability and relatively low decoding complexity thanks to low degree profiles with limited decoding iterations, such that they intrinsically fit in a type-II hybrid automatic repeat-request (ARQ) system. Simulation results show that the proposed approaches manage to yield a performance gain of up to 0.3 dB when compared to the existing extension technique.

## Construction of SeIRA QC-LDPC codes with low error floor

- **Status**: ✅
- **Reason**: SeIRA QC-LDPC 구성, circle length+connectivity 결합 신규 metric으로 error floor 개선 — 바이너리 코드설계(E)
- **ID**: ieee:6125358
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Wenyan Zhang, Minjian Zhao, Jie Zhong +2
- **PDF**: https://ieeexplore.ieee.org/document/6125358
- **Abstract**: We investigate the construction method of structured extended irregular repeated-accumulate quasi-cyclic low-density parity-check (SeIRA QC-LDPC) codes with short to moderate length. A new metric is proposed that jointly considers both circle length and circle connectivity, which aims to improve the error correcting performance in the error floor region. Meanwhile, iterative searching method is proposed that increase the possibility of finding out good solution based on the new metric. At last, we apply our construct method to design codes with different length by expanding them from the same mother matrix. Simulation results show that FER of the codes constructed by this method outperform the corresponding codes in the 802.16 standard expanded from the same mother matrix by 0.15~0.4dB at FER around 10-5.

## Distributed joint source-channel coding of correlated binary sources in wireless sensor networks

- **Status**: ❌
- **Reason**: 분산 결합소스채널코딩(JSCC), LDPC는 베이스라인 — 떼어낼 ECC 기법 없음
- **ID**: ieee:6125345
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Iqbal Shahid, Pradeepa Yahampath
- **PDF**: https://ieeexplore.ieee.org/document/6125345
- **Abstract**: In this paper, we present a distributed joint source-channel (DJSC) coding approach for a pair of correlated binary sources transmitted over independent binary symmetric channels. This problem is of interest in wireless sensor network applications, where encoders with low complexity and delay may be required. In the proposed method, a judiciously chosen fraction of information bits and a fraction of parity bits obtained by puncturing the output of a systematic channel code are transmitted for each source. We obtain the achievable rate region for the proposed coding scheme and show that it coincides with the Slepian-Wolf lower bound as the channel error probability approaches zero. Experimental results obtained with a practical implementation based on LDPC codes are also presented which demonstrate that for short coding block lengths (or low delay coding), the proposed DJSC coding method outperforms separate distributed source coding and channel coding.

## On the performance of non-binary LDPC with MIMO in practical systems

- **Status**: ❌
- **Reason**: non-binary LDPC (GF) with MIMO 성능평가 — 비이진 LDPC 제외
- **ID**: ieee:6125401
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Ottavio M. Picchi, Alain Mourad, Ismael Gutierrez +1
- **PDF**: https://ieeexplore.ieee.org/document/6125401
- **Abstract**: This paper aims at assessing the performance of non-binary LDPC codes with MIMO techniques in practical systems (e.g. MIMO 2×2 systems). More specifically, we compare two approaches at the receiver side, a first linear approach (using linear equalizer) and a second less common approach making “soft” use of the maximum likelihood (ML) criterion. Moreover, this paper also tries to assess the suitability of non-binary LDPC for combination with MIMO techniques, as compared to competing binary FEC schemes such as Duo Binary Turbo Codes. This is done by quantifying the gain achieved by non binary LDPC with either Alamouti or Spatial multiplexing techniques, in comparison to DBTC, and with reference to the single antenna context.

## Improved rate-adaptive codes for Distributed Video Coding

- **Status**: ❌
- **Reason**: 분산비디오코딩(DVC) rate-adaptive LDPC - JSCC/소스코딩 응용, 채널 ECC 기법 아님
- **ID**: ieee:6115901
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jeffrey J. Micallef, Reuben A. Farrugia, Carl J. Debono
- **PDF**: https://ieeexplore.ieee.org/document/6115901
- **Abstract**: Distributed Video Coding (DVC) is a coding paradigm which shifts the major computational intensive tasks from the encoder to the decoder. Temporal correlation is exploited at the decoder by predicting the Wyner-Ziv (WZ) frames from the adjacent key frames. Compression is then achieved by transmitting just the parity information required to correct the predicted frame and recover the original frame. This paper proposes an algorithm which identifies most of the unreliable bits in the predicted bit planes, by considering the discrepancies in the previously decoded bit plane. The design of the used Low Density Parity Check (LDPC) codes is then biased to provide better protection to the unreliable bits. Simulation results show that, for the same target quality, the proposed scheme can reduce the WZ bit rates by up to 7% compared to traditional schemes.

## An unequally protected Distributed Compressed Video Sensing algorithm

- **Status**: ❌
- **Reason**: 분산압축비디오센싱 압축센싱+BP - 소스코딩/CS, 채널 ECC 아님
- **ID**: ieee:6115935
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Bin Li, Xuqi Zhu, Yu Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6115935
- **Abstract**: Distributed Compressed Video Sensing (DCVS) has developed as one of the efficient solutions that guarantee low complexity video compression. In this paper, a novel DCVS algorithm with unequal protection of the video signal's elements is proposed. The new algorithm utilizes not only the sparsity and probability distribution of the video signal but also its particular unequal significance feature. Based on this feature, we design the structured irregular low-density sensing matrix to sample the signal. From the analysis and simulation results, it is confirmed that our method has higher recovery quality than the conventional Bayesian Compressed Sensing (CS) using Belief Propagation (BP). Moreover, the excellent noise-resilience of BP is preserved in our algorithm comparing to the DCVS schemes using optimization recovery.

## An efficient architecture for iterative soft reliability-based majority-logic non-binary LDPC decoding

- **Status**: ❌
- **Reason**: NB-LDPC ISRB 다수결 디코더 아키텍처 GF(2^8) — 비이진 LDPC 제외
- **ID**: ieee:6190136
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Xinmiao Zhang, Fang Cai
- **PDF**: https://ieeexplore.ieee.org/document/6190136
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes have better error-correcting performance than their binary counterparts at the cost of higher decoding complexity when the code length is moderate. Compared to other NB-LDPC decoding algorithms, the iterative reliability-based majority-logic decoding can achieve better performance-complexity tradeoff. In this paper, an efficient partial-parallel shift-message decoder architecture is proposed for cyclic NB-LDPC codes based on the iterative soft reliability-based majority-logic decoding (ISRB-MLGD) algorithm. The message shifting is implemented by memories concatenated with variable node units to reduce the area. Although the accumulated soft reliabilities in the ISRB algorithm require longer word length, and accordingly longer critical path and larger memory, the decoder architecture and control logic can be simplified. Particularly, the check node units are modified so that the message switching network can be eliminated. Compared to the iterative hard reliability-based decoder for a (255, 175) NB-LDPC code over GF(28), the proposed ISRB decoder can achieve around 0.8dB coding gain with less than three times hardware complexity.

## A flexible layered LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC flexible layered 디코더 아키텍처(병렬도 가변, 메모리충돌 없음, 확장성 인터커넥트) - D 이식 가능
- **ID**: ieee:6125305
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: I. Tsatsaragkos, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6125305
- **Abstract**: We introduce a flexible layered decoder architecture for Quasi-Cyclic Low Density Parity Check (LDPC) codes. An iterative construction of the parity check matrix is exploited by the proposed decoder to achieve various degrees of parallelism, characterized by a high utilization of variable and check processing nodes, absence of memory conflicts, and a simple and scalable interconnection network. Furthermore, the proposed LDPC decoder supports variable code rate, information-word length and order of modulation. A comparison to prior-art decoders proves the efficiency of the proposed scheme.

## A reduced routing network architecture for partial parallel LDPC decoders

- **Status**: ✅
- **Reason**: 부분병렬 LDPC 디코더의 라우팅 네트워크 축소(permutation network); 면적/속도/전력 개선 HW 아키텍처(D)
- **ID**: ieee:6190420
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Houshmand Shirani-Mehr, Tinoosh Mohsenin, Bevan Baas
- **PDF**: https://ieeexplore.ieee.org/document/6190420
- **Abstract**: A novel partial parallel decoding scheme based on the matrix structure of LDPC codes proposed in IEEE 802.15.3c and IEEE 802.11ad standards is presented that significantly simplifies the routing network of the decoder, and the class of parity-check matrices for which the method can be used is defined. The proposed method results in an almost complete elimination of logic gates on the routing network, which yields improvements in area, speed and power, with an identical error correction performance to conventional partial-parallel decoders. A decoder for the (672,588) LDPC code adopted in the IEEE 802.15.3c is implemented in a 65 nm CMOS technology including place & route with both proposed permutational decoder, and conventional partial-parallel architecture. The proposed permutational LDPC decoder operates at 235 MHz and delivers a throughput of 7.9 Gbps with 5 decoding iterations per block. The proposed permutational decoder has a throughput 30% higher and is approximately 24% smaller than the conventional partial-parallel decoder.

## Finding the most fault-tolerant flat XOR-based erasure codes for storage systems

- **Status**: ❌
- **Reason**: flat XOR 기반 erasure 코드 탐색; 스토리지용이나 LDPC가 아닌 XOR erasure 코드라 LDPC ECC 기법 이식성 없음
- **ID**: ieee:6190329
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Jay J. Wylie
- **PDF**: https://ieeexplore.ieee.org/document/6190329
- **Abstract**: We describe the techniques we developed to efficiently find the most fault-tolerant flat XOR-based erasure codes for storage systems. These techniques substantially reduce the search space for finding fault-tolerant codes (e.g., by a factor of over 52 trillion in one case). This reduction in the search space has allowed us to find the most fault-tolerant codes for larger codes than was previously thought feasible. The result of our effort to find the most fault-tolerant flat XOR-based erasure codes for storage systems has yielded a corpus of 49,215 erasure codes that we are making public.

## On the iterative decoding of binary product codes over the binary erasure channel

- **Status**: ❌
- **Reason**: 바이너리 product code의 BEC 반복디코딩 — LDPC 아닌 product/cyclic 부호, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:6125323
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: P. R. Freitas, V. C. da Rocha, J. S. Lemos-Neto
- **PDF**: https://ieeexplore.ieee.org/document/6125323
- **Abstract**: Iterative decoding in two dimensions over the binary erasure channel is investigated when identical linear binary cyclic codes are employed in each dimension. Decoding of the overall code is simplified by employing iterative decoding with cyclic permutations for the component code in each dimension. Decoding complexity versus performance can be traded as a function mainly of the number of minimum weight codewords selected from the dual of each component code. Using results from computer simulations, a comparative analysis is presented of various iterative decoding algorithms in two dimensions applied to simple codes, specifically the product codes (961,676,9), (225,49,25) and (961,256,49).

## An FPGA implementation architecture for decoding of polar codes

- **Status**: ❌
- **Reason**: polar code 전용 BP FPGA 디코더 — 비-LDPC, polar 구조에 의존하여 바이너리 LDPC BP로 이식 불가
- **ID**: ieee:6125398
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Alptekin Pamuk
- **PDF**: https://ieeexplore.ieee.org/document/6125398
- **Abstract**: Polar codes are a class of codes versatile enough to achieve the Shannon bound in a large array of source and channel coding problems. For that reason it is important to have efficient implementation architectures for polar codes in hardware. Motivated by this fact we propose a belief propagation (BP) decoder architecture for an increasingly popular hardware platform; Field Programmable Gate Array (FPGA). The proposed architecture supports any code rate and is quite flexible in terms of hardware complexity and throughput. The architecture can also be extended to support multiple block lengths without increasing the hardware complexity a lot. Moreover various schedulers can be adapted into the proposed architecture so that list decoding techniques can be used with a single block. Finally the proposed architecture is compared with a convolutional turbo code (CTC) decoder for WiMAX taken from a Xilinx Product Specification and seen that polar codes are superior to CTC codes both in hardware complexity and throughput.

## Outage capacity for MIMO-OFDM systems in block fading channels

- **Status**: ❌
- **Reason**: MIMO-OFDM outage capacity, LDPC은 성능비교 베이스라인일 뿐 떼어낼 기법 없음
- **ID**: ieee:6190112
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Marco Chiani, Andrea Conti, Matteo Mazzotti +2
- **PDF**: https://ieeexplore.ieee.org/document/6190112
- **Abstract**: We introduce the concept of outage capacity for multiple-input multiple-output (MIMO)-orthogonal frequency-division multiplexing (OFDM) systems in time and frequency block fading channels. We derive the outage capacity and its expression is shown to be related to the characteristic function of the capacity for the usual quasi-static MIMO fading channel case. We also compare the outage capacity with the performance of MIMO-OFDM systems employing powerful error correcting codes based on low-density parity-check codes when, due to finite frequency or time interleaving, there is only a small number of fading blocks per codeword.

## Distributed video coding: A promising solution for distributed wireless video sensors or not?

- **Status**: ❌
- **Reason**: DVC 전력소비 분석 서베이성 논문, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:6116018
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Chieh-Chuan Chiu, Shao-Yi Chien, Chia-han Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/6116018
- **Abstract**: Low-power and low-cost distributed wireless video sensors play important roles for applications in machine-to-machine (M2M) and wireless sensor networks. Distributed video coding (DVC), an emerging coding technology based on Wyner-Ziv theory, seems to be a possible solution for implementing low-power video sensors since most of the computational complexity is moved from the encoder to the decoder. In this paper, existing works on DVC are discussed with rate-distortion and power consumption analyses compared with H.264/AVC-based approaches. We show that, since more transmission power is required for compensating the lower rate-distortion performance, the power consumption of sensor nodes using DVC is just similar to that of using H.264/AVC with zero motion vectors. Therefore, there is still a room for improvement to make DVC applicable for distributed wireless video sensors. Based on our analysis results, several possible research directions, such as studies on the trade- off between hardware cost and system power consumption, are also addressed in this paper under a unified DVC framework.

## Decoding by iterative detection (DECIDET): Soft-in/soft-out decoding of arbitrary linear block codes over arbitrary finite fields

- **Status**: ❌
- **Reason**: 임의 유한체 임의 선형블록부호 SISO 디코딩(생성행렬 기반 turbo-like) — LDPC BP 비의존, 비이진 일반화 제외
- **ID**: ieee:6190088
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Todd K. Moon, Jacob H. Gunther
- **PDF**: https://ieeexplore.ieee.org/document/6190088
- **Abstract**: This paper presents a framework for an error correction decoding algorithm which can perform soft-input/soft-output decoding on arbitrary linear block codes over arbitrary finite fields. The algorithm produces estimates of individual symbols by detecting the symbol as a scalar multiple of a column of the generator matrix for the code, with other columns forming an interfering “noise” which is probabilistically modeled. Only the generator matrix is used for the decoder; the parity check matrix is not employed. The posterior probability so obtained is iteratively fed back as a prior input for turbo-like operation. Methods of incorporating statistical dependence among symbols are presented. The decoder can be used for channels with arbitrary noise distributions. Computation over larger fields is achieved through the use of an extended Hadamard transform, which is used to compute the distribution of arbitrary linear combinations of random variables distributed over the field. Results are presented for some codes of various lengths and design distances.

## Sub-optimal importance sampling for fast simulation of linear block codes over BSC channels

- **Status**: ❌
- **Reason**: 선형블록부호 WER의 importance sampling 시뮬레이션 기법 — 디코더/HW/구성 기여 아닌 평가방법론
- **ID**: ieee:6125326
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Gianmarco Romano, Antonio Drago, Domenico Ciuonzo
- **PDF**: https://ieeexplore.ieee.org/document/6125326
- **Abstract**: Estimation of very low word-error probability of hard-decoded linear block codes can be performed through Monte-Carlo simulation. The computational complexity of the standard method however increases as the probability of error to be estimated decreases. In this paper we propose a general algorithm for fast estimation of probability of error of linear block codes on BSC channels based on the importance sampling and the cross-entropy method for rare-events that can be employed for any hard-decision decoder. When optimal decoding is used the algorithm reduces to a single simulation run that can estimate, with a given accuracy, performances for a whole range of sufficiently high signal-to-noise ratios.

## Compressive sensing based imaging via Belief Propagation

- **Status**: ❌
- **Reason**: 압축센싱 이미지 복원에 BP 사용 — 신호복원이지 채널 ECC 아님
- **ID**: ieee:6189996
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Preethi Ramachandra, Mina Sartipi
- **PDF**: https://ieeexplore.ieee.org/document/6189996
- **Abstract**: Multiple description coding (MDC) using Compressive sensing (CS) mainly aims at restoring the image from a small subset of samples with reasonable accuracy using an iterative message passing decoding algorithm commonly known as Belief Propagation (BP). CS technique can accurately recover any compressible or sparse signal from a lesser number of non-adaptive, randomized linear projection samples than that essential by the Nyquist rate. In this paper, we demonstrate how the BP algorithm reconstructs the image from the measurements generated using the sparse image signal and the measurement matrix. Thus we prove that this algorithm is effective even in the absence of side information. The proposed algorithm exhibits remarkable performance in the reconstruction time as well as reconstruction accuracy.

## Maximum likelihood detection upper bound for detect-and-forward relaying over AWGN channels

- **Status**: ❌
- **Reason**: 릴레이 ML 검출 상한, 채널코딩 제거 명시 — LDPC 무관
- **ID**: ieee:6125442
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Khoa Quang Huynh, Tor Aulin
- **PDF**: https://ieeexplore.ieee.org/document/6125442
- **Abstract**: The maximum likelihood (ML) detection rule for the detect-and-forward relaying in Additive White Gaussian Noise (AWGN) channels which takes into account the detecting errors at the relay is formulated. In order to focus the study on relaying, channel coding is eliminated. Based on the derived ML detection rule, the upper bound on the probability of error at the destination's receiver is analyzed. The source-relay-destination channel is assumed to be equivalent to an AWGN channel with an equivalent signal-to-noise ratio (SNR) γeq. For the first time, the γeq is analyzed and its exact analytical expression is derived.

## Outage performance for opportunistic decode-and-forward relaying coded cooperation networks over Nakagami-m fading

- **Status**: ❌
- **Reason**: 협력중계 네트워크 outage 분석, 채널코딩 부수 언급 — 무선응용 특이, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6125395
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Hoc Phan, Trung Q. Duong, Hans-Jürgen Zepernick
- **PDF**: https://ieeexplore.ieee.org/document/6125395
- **Abstract**: In this paper, we analyze the outage performance of an opportunistic decode-and-forward (DF) relaying coded cooperation network over independent, and identically distributed Nakagami-m fading channels. In this scheme, cooperative diversity gain is obtained by integrating opportunistic relaying (OR) selection with channel coding. We have derived an analytical expression for the outage probability (OP) of the considered coded cooperation networks for both error-free relays and errors at the relays. Furthermore, for comparison, we derive an expression for the OP of a conventional OR cooperative network. For both systems, it has been observed that the achievable diversity gain is the same. However, the coded cooperation scheme achieves higher coding gain than the conventional cooperative scheme. Finally, numerical results are provided showing a tight match between the Monte Carlo simulations and the analytical curves.

## Channel tracking for D-BLAST for airborne platforms

- **Status**: ❌
- **Reason**: D-BLAST 채널 트래킹용 LDPC 출력 활용; MIMO 무선 채널 추정 특이적, NAND에 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6190223
- **Type**: conference
- **Published**: 6-9 Nov. 2
- **Authors**: Kapil Borle, Biao Chen, M. J. Gans
- **PDF**: https://ieeexplore.ieee.org/document/6190223
- **Abstract**: Coherent symbol detection requires knowledge of channel state information. The traditional use of embedding pilot symbols with payload data may not be easy to justify if channel variation is fast and/or the data rate requirement is high. We consider the implementation of the D-BLAST algorithm for airborne platforms and develop channel tracking schemes that eliminate or reduce the use of pilot symbols. In a normal operation mode, channel update is achieved dynamically as each layer of the D-Blast, encoded using an LDPC code, is decoded. We find the optimal symbol length to estimate a SISO channel under the Rayleigh channel model and then generalize it to the MIMO case. To ensure that the transceiver can detect outage due to the loss of channel state, an adaptive algorithm is devised utilizing the extremal property of the terminating likelihood ratio of an LDPC decoder.

## Construction of nonbinary LDPC codes: Prime difference approach

- **Status**: ❌
- **Reason**: nonbinary LDPC(GF) 구성 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6197837
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Xin Zhao, Lijun Zhang, Leelung Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6197837
- **Abstract**: This paper presents an algebraic method for constructing structural nonbinary LDPC codes based on the prime difference over finite field. The approach gives a class of quasi-cyclic (QC)-LDPC codes with girth at least 6. Especially, the approach can construct a class of short length code and the decoding complexity is low. Simulation results show that the constructed codes decoded with iterative decoding perform well over the AWGN channel using BPSK transmission in terms of bit-error probability and rate of decoding convergence, collectively.

## Construction of QC-LDPC codes based on PSO algorithm

- **Status**: ✅
- **Reason**: PSO 기반 인코더블 QC-LDPC 구성(girth-4/BER 제약) 신규 코드설계(E), 바이너리 이식 가능
- **ID**: ieee:6197838
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Yang Yang, Yang Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6197838
- **Abstract**: The well known Tanner codes are not encodable, in this paper, we derived an encodable QC LDPC codes and use PSO algorithm to determine the parameters of the parity check matrices of the QC LDPC codes. The proposed PSO code construction considers the girth 4 and BER performance to be the constrained conditions in the fitness function of PSO algorithm. Simulation results show that the QC codes constructed by the proposed method have better performance than that of random LDPC codes.

## A class of (3, k) quasi-cyclic LDPC codes from difference sequences with girth 8

- **Status**: ✅
- **Reason**: difference sequence 기반 (3,k) QC-LDPC girth-8 신규 구성법, 바이너리 코드설계(E) 이식 가능
- **ID**: ieee:6197836
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Bing Li, Lijun Zhang, Lee Lung Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6197836
- **Abstract**: An approach for constructing a class of (3, k)-regular quasi-cyclic low-density parity-check (QC-LDPC) codes is proposed, which is based on combinatorial objects termed difference sequences. By an efficient algorithm for searching good difference sequences, codes in this class have girth at least eight. Simulation results show that the codes slightly outperform the counterpart PEG codes and have better performance than the corresponding MacKay codes and array codes.

## Wide-range, accurate frequency offset compensation algorithm based on LDPC for space coherent optical communication

- **Status**: ❌
- **Reason**: 공간 광통신 주파수오프셋 보상 알고리즘(EM/M&M), LDPC는 부수 언급, NAND 이식 ECC 기법 없음
- **ID**: ieee:6197824
- **Type**: conference
- **Published**: 27-30 Nov.
- **Authors**: Jingsong Xiang, Miaomiao Zhang, Xiaolei Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6197824
- **Abstract**: In this paper, we introduce a wide-range, accurate LDPC coded-aided frequency offset compensation algorithm based on both EM algorithm and M&M algorithm in space coherent optical communication systems. The proposed approach can overcome the shortcoming of the existing frequency offset compensation algorithms which are employed in space coherent optical communication systems directly. It allows performing reliable frequency estimation with respect to the ideal frequency estimation for the signal-to-noise ratios down to a few decibels, and without need phase-locked loops (PLL). The simulations show that the approach can increase the synchronization range about ±50% of the symbol rate. Furthermore, its accurate is close to the Modified Cramer-Rao bound (MCRB) in low signal- to-noise ratio.

## Iterative reconstruction algorithms in compressed sensing

- **Status**: ❌
- **Reason**: 압축센싱 sparse 신호 복원(IP/verification 알고리즘)으로 채널 ECC가 아님, QC-LDPC를 측정행렬로 쓸 뿐
- **ID**: ieee:6143605
- **Type**: conference
- **Published**: 22-24 Nov.
- **Authors**: Ludovic Danjean, Vida Ravanmehr, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/6143605
- **Abstract**: In this paper we give an overview of current results in iterative reconstruction of sparse signals using parity check matrices of low-density parity check (LDPC) codes as measurement matrices in compressed sensing. We provide a detailed explanation of two iterative reconstruction algorithms, Interval Passing (IP) algorithm and verification algorithm. We then compare their performance using parity check matrices of quasi-cyclic low-density parity check (QC-LDPC) codes with different column-weights and rates.

## Full diversity random LDPC codes

- **Status**: ❌
- **Reason**: block fading용 full-diversity 랜덤 LDPC ensemble 설계, 무선 채널 특이적 stopping set 회피로 NAND에 이식할 일반 코드설계 기여 약함
- **ID**: ieee:6101300
- **Type**: conference
- **Published**: 22-23 Nov.
- **Authors**: Dieter Duyck, Joseph J. Boutros, Marc Moeneclaey
- **PDF**: https://ieeexplore.ieee.org/document/6101300
- **Abstract**: The block fading (BF) channel is a useful model for various communication systems in urban environments. Full-diversity error-correcting codes are required to approach the physical limits of the performance on BF channels. Low-density parity-check (LDPC) codes are good error-correcting codes, but full-diversity standard random LDPC codes for the BF channel are not known yet. We design full-diversity random LDPC ensembles at infinite block length by optimizing the threshold in multiple points in the fading space, which takes into account the randomness of the fading. However, this is not sufficient to achieve full-diversity at finite block length, because of stopping sets. We therefore propose a method to generate full-diversity code instances at finite length so that stopping sets over information bits are avoided. The asymptotic and finite length word error rate performance is verified by means of density evolution and Monte Carlo simulations, respectively, confirming that full-diversity standard random LDPC codes exist and perform well.

## A flexible NoC-based LDPC code decoder implementation and bandwidth reduction methods

- **Status**: ✅
- **Reason**: NoC 기반 유연 LDPC 디코더+early/message stopping으로 면적·전력 절감 VLSI 아키텍처(D)
- **ID**: ieee:6136889
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Carlo Condo, Guido Masera
- **PDF**: https://ieeexplore.ieee.org/document/6136889
- **Abstract**: The need for efficient and flexible LDPC (Low Density parity Check) code decoders is rising due to the growing number and variety of standards that adopt this kind of error correcting codes in wireless applications. From the implementation point of view, the decoding of LDPC codes implies intensive computation and communication among hardware components. These processing capabilities are usually obtained by allocating a sufficient number of processing elements (PEs) and proper interconnect structures. In this paper, Network on Chip (NoC) concepts are applied to the design of a fully flexible decoder, capable to support any LDPC code with no constraints on code structure. It is shown that NoC based decoders also achieve relevant throughput values, comparable to those obtained by several specialized decoders. Moreover, the paper explores the area and power overhead introduced by the NoC approach. In particular, two methods are proposed to reduce the traffic injected in the network during the decoding process, namely early stopping of iterations and message stopping. These methods are usually adopted to increase throughput. On the contrary, in this paper, we leverage iteration and message stopping to cut the area and power overhead of NoC based decoders. It is shown that, by reducing the traffic injected in the NoC and the number of iterations performed by the decoding algorithm, the decoder can be scaled to lower degrees of parallelism with small losses in terms of BER (Bit Error Rate) performance. VLSI synthesis results on a 130 nm technology show up to 50% area and energy reduction while maintaining an almost constant throughput.

## Parallel Concatenation of LDPC Codes with Two Sets of Source Bits

- **Status**: ❌
- **Reason**: LDPC 병렬 연접 + 두 소스비트 전송 스킴, 채널코딩보다 연접/전송 구조에 가까워 NAND 단일 LDPC ECC 이식성 약함
- **ID**: ieee:6120565
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: P.C. Catherine, K.M.S. Soyjaudah
- **PDF**: https://ieeexplore.ieee.org/document/6120565
- **Abstract**: Conventional attempts at using parallel concatenation for LDPC codes have not been widely successful. Interestingly, existing schemes do not rely on the concatenating architecture, but rather on the complementary profile of two carefully selected component codes. Each code individually drive the decoding process over the signal-to-noise ratio range over which it excels. In this work however, a concatenating scheme is proposed that is not limited by specific choices of component codes. In addition, the scheme also departs from conventional turbo style settings by transmitting two sets of source bits over the channel, instead of just one. At the receiving side then, two decoders are set up and share extrinsic information. The key difference however with the conventional turbo style, is that the channel information (being independent for both decoders) is not removed when computing the extrinsic information. As signal-to-noise ratio increases, the associated impact of this modification results in a valuable performance gain.

## Erasing Bit Nodes on the Bipartite Graph for Enhanced Performance of LDPC Codes

- **Status**: ✅
- **Reason**: 비트노드 erasing으로 cycle/trapping set 대응하는 신규 BP 디코딩 전략 - 카테고리 C 이식 가능 디코더
- **ID**: ieee:6120564
- **Type**: conference
- **Published**: 18-20 Nov.
- **Authors**: P.C. Catherine, K.M.S. Soyjaudah
- **PDF**: https://ieeexplore.ieee.org/document/6120564
- **Abstract**: The proposed work is based on the fact that the complete set of bit nodes for an LDPC code may not always be required at the receiving side for successful decoding. A corresponding strategy is therefore built up. In contrast to common practice, the total number of iterations available is shared among different sets. The first set runs the decoding algorithm with all its bit nodes. Successive sets (in case of decoding failure) runs each with a different selection of "erased" bit nodes, leading to an overall non-monotonic behavior. The end result is a system capable of effectively dealing with the problem of cycles and trapping sets without even being aware of their existence. Reported results show an important coding gain over conventional systems.

## Efficient Reed-Solomon based LDPC decoders

- **Status**: ✅
- **Reason**: RS-based LDPC 디코더 HW — 메모리 주소생성·셔플네트워크·TM 폴딩 아키텍처가 바이너리 QC-LDPC 디코더에 이식 가능(D)
- **ID**: ieee:6138645
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Chuan Zhang, Sang-Min Kim, Jin Sha
- **PDF**: https://ieeexplore.ieee.org/document/6138645
- **Abstract**: By exploring the specific characteristics of the matrices of Reed-Solomon (RS) based low-density parity-check (LDPC) codes, the authors manage to propose an efficient memory address generation (MAG) method for time-multiplexed (TM) RS-based LDPC code decoder architecture. This unique feature directly results in the MAG scheme which works perfectly with the TM decoders. Furthermore, along with the sum and sign accumulation unit (SSAU), a methodology for designing TM RS-based LDPC code decoder supporting high decoding throughput applications such as a 10GBASE-T system is presented. By developing and evaluating three decoder architectures with different folding factors, this approach proves to be suitable for variable design requirements. In addition, a shuffle network composed of de-multiplexers (deMUX's) and routing blocks is also incorporated to reduce the decoding latency.

## A selective-input non-binary LDPC decoder architecture

- **Status**: ❌
- **Reason**: 32-ary non-binary LDPC 디코더 (Min-Max, 32-ary) — 비이진 LDPC라 제외 대상
- **ID**: ieee:6138641
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Yeong-Luh Ueng, Chung-Jay Yang, Shu-Wei Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6138641
- **Abstract**: This paper presents a layered selective-input Min-Max decoding algorithm and the associated architecture for non-binary LDPC codes. Compared to the selective-input non-binary decoders presented in the literature, our proposed selective-input implementation can be quite easily realized in order to achieve a higher parallelism and a higher throughput. Also, by using a compensation technique, the error performance of the proposed selective-input implementation is quite close to the original Min-Max algorithm even though a small number of selective inputs is used. Using a 90-nm CMOS process, we implemented a 32-ary (837, 726) decoder that can achieve a throughput of 29.0 Mb/s.

## Memory efficient decoder design of nonbinary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC(NB-LDPC) Min-Max 메모리 효율 디코딩 — 비이진 LDPC라 제외
- **ID**: ieee:6138642
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Kai He, Jin Sha, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/6138642
- **Abstract**: This paper presents a memory efficient decoding algorithm for the non-binary low-density parity-check (NB-LDPC) codes. Compared to other recently developed Min-Max decoding algorithm, the message memory as well as the average number of iterations has been reduced using the proposed decoding method. Meanwhile, the corresponding decoder architecture is also proposed.

## A common flexible architecture for Turbo/LDPC codes

- **Status**: ✅
- **Reason**: Turbo/LDPC 공용 ASIC 아키텍처 — 메모리/로직 공유 HW 설계가 바이너리 LDPC 디코더에 이식 가능(D)
- **ID**: ieee:6138644
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Yuebin Huang, Chen Chen, Changsheng Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/6138644
- **Abstract**: Turbo codes and LDPC codes are two of the most powerful error correction codes that can approach Shannon limit in many communication systems. But there are little architecture presented to support both LDPC and Turbo codes, especially by the means of ASIC. This paper have implemented a common architecture that can decode LDPC and Turbo codes, and it is capable of supporting the WiMAX, WiFi, 3GPP-LTE standard on the same hardware. In this paper, we will carefully describe how to share memory and logic devices in different operation mode. The chip is design in a 130nm CMOS technology, and the maximum clock frequency can reach up to 160MHz. The maximum throughput is about 104Mbps@5.5 iteration for Turbo codes and 136Mbps@10iteration for LDPC codes. Comparing to other existing structure, the design speed, area have significant advantage.

## Flexible and efficient FEC decoders supporting multiple transmission standards

- **Status**: ❌
- **Reason**: 다중 표준 FEC(RS/Viterbi/Turbo/LDPC) 디코더 오버뷰 — 서베이성, 떼어낼 신규 바이너리 LDPC 기법 불명확
- **ID**: ieee:6138643
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Yun Chen, Changsheng Zhou, Yuebin Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/6138643
- **Abstract**: An important trend of the modern mobile device is that a single user terminal that will be capable of receiving signals of multiple different transmission standards. Most of these transmission standards employ a forward error correction decoding, including Reed-Solomon, Viterbi, Turbo and low-density parity check and so on. In this overview paper we review several programmable and area-efficient decoder architectures within one hardware platform. We show, in the case of guaranteed throughput performance, compared with multi-core implementation way, better power consumption performance can be gotten.

## A novel low complexity soft-decision demapper for QPSK 8PSK demodulation of DVB-S2 systems

- **Status**: ❌
- **Reason**: DVB-S2 QPSK/8PSK soft-decision demapper LLR 계산 — 변조/복조 demapping이며 LDPC 디코더·코드·HW 기법 아님, 무선 응용 특이적
- **ID**: ieee:6117701
- **Type**: conference
- **Published**: 17-18 Nov.
- **Authors**: Jianing Su, Zhenghao Lu, Xiaopeng Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/6117701
- **Abstract**: This paper provides an efficient low complexity soft-decision demapper algorithm for computing the log-likelihood-ratios (LLRs) of the 8PSK demodulations in the DVB-S2 standard. The proposed method has linear complexity, avoids the multiple square operations in the classical method and reduces the number of compare-select operations by half compared to traditional LLR computation algorithms. The demapper using the proposed method has been verified on Altera FPGA.

## A 115mW 1Gbps QC-LDPC decoder ASIC for WiMAX in 65nm CMOS

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 ASIC, fully parallel layered scheduling 아키텍처+메모리 절감 HW(D) 이식 가능
- **ID**: ieee:6123576
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Xiao Peng, Zhixiang Chen, Xiongxin Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/6123576
- **Abstract**: Structured quasi-cyclic low-density parity-check (QC-LDPC) code is a part of many emerging wireless communication standards, such as WiMAX, WiFi and WPAN. This paper presents a high parallel decoder architecture for the QC-LDPC codes and the corresponding decoder ASIC for WiMAX system. Through utilizing the proposed fully parallel layered scheduling architecture, the decoder chip saves 22.2% memory bits and takes 24~48 clock cycles per iteration for different code rates. It occupies 3.36 mm2 in SMIC 65nm CMOS, and realizes 1Gbps (1056Mbps) throughput at 1.2V, 110MHz and 10 iterations with the power 115mW and power efficiency 10.9pJ/bit/iteration. The energy/bit/iteration reduces 63.6% in normalized comparison with the state-of-art publication.

## A 1pJ/cycle Processing Engine in LDPC application with charge recovery logic

- **Status**: ✅
- **Reason**: LDPC 처리엔진 PE에 charge-recovery logic 저전력 회로기법, 디코더 HW 구현(D) 이식 가능
- **ID**: ieee:6123640
- **Type**: conference
- **Published**: 14-16 Nov.
- **Authors**: Yimeng Zhang, Mengshu Huang, Nan Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/6123640
- **Abstract**: This paper presents a Processing Engine (PE) which is used in Low Density Parity Codec (LDPC) application with a novel charge-recovery logic called pseudo-NMOS boost logic (pNBL), to achieve high-speed and low power dissipation. pNBL is a high-overdriven, low area consuming charge recovery logic, which belongs to boost logic family. Proposed Processing Engine is used in LDPC circuit to reduce power dissipation and increase the processing speed. To demonstrate the performance of proposed PE, a test chip is designed and fabricated with 0.18μm CMOS technology. Simulation results indicate that proposed PE with pNBL dissipates only 1pJ/cycle when working at the frequency of 403MHz, which is only 36% of PE with conventional static CMOS gates. The measurement results shows that the test chip can work as high as 609MHz with the energy dissipation of 2.1pJ/cycle.

## Coded modulation of polarization- and space-multiplexed signals

- **Status**: ❌
- **Reason**: 편광·공간다중 광전송 constellation 최적화, coded modulation. 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:6210752
- **Type**: conference
- **Published**: 13-16 Nov.
- **Authors**: Henning Bülow, Ümit Abay, Andreas Schenk +1
- **PDF**: https://ieeexplore.ieee.org/document/6210752
- **Abstract**: In this Paper we investigate the optimization of constellations for polarization-division multiplexed transmission in standard single-mode fiber systems and for space-division multiplexing in a multi-mode fiber system.
