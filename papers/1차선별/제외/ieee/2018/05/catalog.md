# IEEE Xplore — 2018-05


## Chained LDPC Codes for Future Communication Systems

- **Status**: ❌
- **Reason**: Chained LDPC는 미래 통신 TB 에러율용 코드블록 결합/PEXIT 최적화 - 통신 특이적, NAND 이식 기법 약함이나 애매 - 통신 TB 결합구조 NAND 무관으로 out
- **ID**: ieee:8301547
- **Type**: journal
- **Published**: May 2018
- **Authors**: Lei Yang, Yixuan Xie, Jinhong Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/8301547
- **Abstract**: We propose chained low-density parity-check codes to improve the transport block (TB) error rate performance for high-throughput future communications. The proposed codes connect multiple code blocks (CBs) in a TB into a chain by coupling a few information bits between every two consecutive CBs and insert dummy bits at two ends of the chain. We propose a feed-forward and feed-back TB decoding scheme. We employ the protograph extrinsic information transfer analysis to optimize the coupling pattern to minimize the decoding threshold of the proposed codes. Numerical results demonstrate the excellent TB error rate performance of the proposed codes.

## Finite-Length Analysis of Spatially-Coupled Regular LDPC Ensembles on Burst-Erasure Channels

- **Status**: ❌
- **Reason**: SC-LDPC 버스트 소거 채널 유한길이 성능 분석(이론 bound/DE)으로 표준 앙상블 사용, 새 구성/디코더 없음
- **ID**: ieee:8272426
- **Type**: journal
- **Published**: May 2018
- **Authors**: Vahid Aref, Narayanan Rengaswamy, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/8272426
- **Abstract**: Regular spatially-coupled low-density parity-check ensembles have gained significant interest, since they were shown to universally achieve the capacity of binary memoryless channels under low-complexity belief-propagation decoding. In this paper, we focus primarily on the performance of these ensembles over binary channels affected by bursts of erasures. We first develop an analysis of the finite length performance for a single burst per code word and no errors otherwise. We first assume that the burst erases a complete spatial position, modeling for instance node failures in distributed storage. We provide new tight lower bounds for the block erasure probability (PB) at finite block length and bounds on the coupling parameter for being asymptotically able to recover the burst. We further show that expurgating the ensemble can improve the block erasure probability by several orders of magnitude. Later we extend our methodology to more general channel models. In a first extension, we consider bursts that can start at a random location in the code word and span across multiple spatial positions. Besides the finite length analysis, we determine by means of density evolution the maximum correctable burst length. In a second extension, we consider the case where in addition to a single burst, random bit erasures may occur. Finally, we consider a block erasure channel model which erases each spatial position independently with some probability p, potentially introducing multiple bursts simultaneously. All results are verified using Monte-Carlo simulations.

## Combinatorial Alphabet-Dependent Bounds for Locally Recoverable Codes

- **Status**: ❌
- **Reason**: LRC(locally recoverable) 코드 조합론적 bound/LP bound - 순수 이론, 디코더/HW/LDPC 구성으로 안 이어짐
- **ID**: ieee:8276590
- **Type**: journal
- **Published**: May 2018
- **Authors**: Abhishek Agarwal, Alexander Barg, Sihuang Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/8276590
- **Abstract**: Locally recoverable (LRC) codes have recently been a focus point of research in coding theory due to their theoretical appeal and applications in distributed storage systems. In an LRC code, any erased symbol of a codeword can be recovered by accessing only a small number of other symbols. For LRC codes over a small alphabet (such as binary), the optimal rate-distance trade-off is unknown. We present several new combinatorial bounds on LRC codes including the locality-aware sphere packing and Plotkin bounds. We also develop an approach to linear programming (LP) bounds on LRC codes. The resulting LP bound gives better estimates in examples than the other upper bounds known in the literature. Further, we provide the tightest known upper bound on the rate of linear LRC codes with a given relative distance, an improvement over the previous best known bounds.

## Efficient Compression of Encrypted Binary Images Using the Markov Random Field

- **Status**: ❌
- **Reason**: 암호화 바이너리 이미지 압축(소스코딩)으로 LDPC 기반 decompression - 채널 ECC가 아님
- **ID**: ieee:8219715
- **Type**: journal
- **Published**: May 2018
- **Authors**: Chuntao Wang, Jiangqun Ni, Xinpeng Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/8219715
- **Abstract**: Similar to conventional compression with the original, unencrypted image as the input, the recently emerged compression on encrypted images generally exploits statistical correlation of natural images to improve compression efficiency. Most of these compression schemes in the literature leverage statistical correlation at the content-owner or service-provider side, which would either increase the computational burden on the content-owner or disclose statistical distributions to the service-provider and thus probably hinder their practical applications. Through analysis on properties of the compression system for encrypted data, we believe that it is more preferable to exploit statistical correlation of natural images at the receiver side with both encryption key and sufficient computational capability, which in turn would improve compression efficiency while achieving low computational complexity and sufficient security for the content owner and the service provider. In light of this, we use the Markov random field (MRF) to characterize binary images in the spatial domain and represent it with a factor graph. The constructed MRF representation of the binary image in the factor graph is then integrated seamlessly with the factor graph for low-density parity check (LDPC)-based decompression, yielding a joint factor graph for binary image reconstruction. By deriving message update equations for the joint factor graph, we develop a new lossless compression scheme for encrypted binary images, which involves stream-cipher-based encryption, LDPC-based compression, and factor-graph-based image reconstruction. Preferable parameters for the proposed scheme are first determined numerically on a specific binary image and then applied to other binary images. Extensive simulations show that significant improvements in terms of compression bit rate over the state of the art are achieved, demonstrating the feasibility and effectiveness of the proposed scheme.

## Finite-Length Analysis of Irregular Repetition Slotted ALOHA in the Waterfall Region

- **Status**: ❌
- **Reason**: IRSA(슬롯 ALOHA) 유한길이 분석으로 LDPC erasure 디코딩을 매핑에 활용할 뿐 통신접속 응용, 떼어낼 ECC 디코더/HW 기법 없음
- **ID**: ieee:8307358
- **Type**: journal
- **Published**: May 2018
- **Authors**: Alexandre Graell i Amat, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/8307358
- **Abstract**: A finite-length analysis is introduced for irregular repetition slotted ALOHA (IRSA) that enables to accurately estimate its performance in the moderate-to-high packet loss probability regime, i.e., in the so-called waterfall region. The analysis is tailored to the collision channel model, which enables mapping the description of the successive interference cancellation process onto the iterative erasure decoding of low-density parity-check codes. The analysis provides accurate estimates of the packet loss probability of IRSA in the waterfall region as demonstrated by Monte Carlo simulations.

## Soft-Output Detector for Uplink MU-MIMO Systems With One-Bit ADCs

- **Status**: ❌
- **Reason**: 1-bit ADC MU-MIMO soft-output 검출기(Hamming 거리 기반) - 디코더 입력 LLR 검출 단계, LDPC 디코더 자체 기법 아님
- **ID**: ieee:8301568
- **Type**: journal
- **Published**: May 2018
- **Authors**: Song-Nam Hong, Namyoon Lee
- **PDF**: https://ieeexplore.ieee.org/document/8301568
- **Abstract**: We consider an uplink multiuser multiple-input multiple-output (MU-MIMO) system with one-bit analog-to-digital converters (ADCs). In this system, numerous symbol detectors, such as maximum-likelihood, zero-forcing, and supervised-learning-based detectors, have been proposed by using one-bit quantized channel outputs. The limitation of these hard-decision detectors cannot generate soft outputs from one-bit quantized channel observations, which considerably degrades the performance of a following channel code. To address this problem, in this letter, we present a novel soft-output detector, in which a soft-metric is computed in (binary) Hamming space using weighted Hamming distances. Simulation results demonstrate that the proposed detector can significantly outperform the other detectors for a coded MU-MIMO system with one-bit ADCs.

## Integer-Forcing Message Recovering in Interference Channels

- **Status**: ❌
- **Reason**: 간섭채널 integer-forcing 메시지 복구로 LDPC ECC와 무관, 떼어낼 디코더/구성 없음
- **ID**: ieee:8247247
- **Type**: journal
- **Published**: May 2018
- **Authors**: Seyed Mohammad Azimi-Abarghouyi, Mohsen Hejazi, Behrooz Makki +2
- **PDF**: https://ieeexplore.ieee.org/document/8247247
- **Abstract**: In this paper, we propose a scheme referred to as integer-forcing message recovering (IFMR) to enable receivers to recover their desirable messages in interference channels. Compared to the state-of-the-art integer-forcing linear receiver (IFLR), our proposed IFMR approach needs to decode considerably less number of messages. In our method, each receiver recovers independent linear integer combinations of the desirable messages each from two independent equations. We propose an efficient polynomial-time algorithm to sequentially find the equations and integer combinations with maximum rates and analyze its complexity. We evaluate the performance of our scheme and compare the results with the minimum mean-square error linear receiver (MMSELR) and lattice-reduction-aided successive interference cancellation with signal-to-interference-plus-noise ratio maximizing preprocessing (LaR-aided SIC with SINR-Max), as well as the IFLR schemes. The results indicate that our IFMR scheme outperforms the MMSELR and LaR-aided SIC with SINR-Max schemes, in terms of achievable rate, considerably. Also, compared to the IFLR, the IFMR scheme achieves slightly less rates in moderate signal-to-noise ratios, with significantly less overall implementation complexity.

## Feedback-Assisted Correlated Packet Transmission With a Helper

- **Status**: ❌
- **Reason**: 패킷 재전송/협력다이버시티 분석, XOR 헬퍼 패킷 - LDPC ECC 기법 없음
- **ID**: ieee:8270687
- **Type**: journal
- **Published**: May 2018
- **Authors**: Ade Irawan, Tad Matsumoto
- **PDF**: https://ieeexplore.ieee.org/document/8270687
- **Abstract**: In this paper, we analyze the impact of source correlation on the diversity and coding gains of a retransmission system, where we aim to recover M erroneously received packets only by transmitting one helper packet utilizing the source correlation among the packets. This system is referred to as M-in-1 helper transmission. The helper packet is constructed simply by taking binary exclusive-OR of the M erroneously received information packets, notified via the feedback channel. To identify the tradeoff between source correlation and performance gain due to coding and diversity, we start our investigation with in-depth analyses on rate regions and outage probabilities with M = {2, 3}. We also evaluate the influence of unequal power and/or redundancy allocations between the helper and information packets. Finally, we provide the analytical results on achievable diversity order with arbitrary integer values of M. It is shown that M-in-1 helper transmission can always achieve Mth-order diversity. Furthermore, (M + 1)th-order diversity can be achieved with M being odd when the source correlation is very high; however, it cannot be achieved with M being even.

## Message Passing-Vector Symbol Decoding for LDPC Codes with Nonbinary Symbols

- **Status**: ❌
- **Reason**: nonbinary 심볼 LDPC용 MP-VSD 디코더, 비이진 LDPC 제외 대상
- **ID**: ieee:8442073
- **Type**: conference
- **Published**: 7-9 May 20
- **Authors**: Usana Tuntoolavest, Chayanon Athanan, Koravit Panwong
- **PDF**: https://ieeexplore.ieee.org/document/8442073
- **Abstract**: This paper proposes a new decoding technique called “MP-VSD” for LDPC codes with large nonbinary symbols. It combines Hard Decision Message Passing (HDMP) with Vector Symbol Decoding (VSD). VSD usually uses very short block codes to limit the number of error symbols, which limits the size of matrix inversion required in the VSD decoding step. MP-VSD can correct more than 60% of the correctable error patterns of VSD for an (60, 30) LDPC code with no matrix inversions in a 2-state fading channel model. Thus, longer block codes may be used for nonbinary symbols.

## A Novel NOMA Design Based on Steiner System

- **Status**: ❌
- **Reason**: Steiner system 기반 코드도메인 NOMA 다중접속 기법 - LDPC ECC 아님, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:8500196
- **Type**: conference
- **Published**: 3-5 May 20
- **Authors**: Yuteng Wu, Edidiong Attang, G. E. Atkin
- **PDF**: https://ieeexplore.ieee.org/document/8500196
- **Abstract**: In this paper, a code-domain Non-orthogonal Multiple access (NOMA) technique based on combinatorial structures with balanced incomplete block design is studied. Initially, a Steiner system (STS) is used for its specific highly structured and fair resource allocation properties. A new multiuser detection scheme is provided. Compared with traditional serial and iterative MUD scheme, our scheme is capable of working in parallel with low complexity. Simulation results on Rayleigh and Additive White Gaussian Noise (AWGN) channels shows that our system outperforms than similar code-domain NOMA techniques with higher overload factor and spectrum efficiency.

## An Efficient NB-LDPC Decoding Algorithm for Next-Generation Memories

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC 디코딩 알고리즘(GF(q) trellis min-sum) — non-binary는 제외 대상
- **ID**: ieee:8351585
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Jing Tian, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8351585
- **Abstract**: Due to the aggressive technology scaling, the memory reliability has been seriously degraded, which poses a challenge to the widely used low-density parity-check (LDPC) codes. Non-binary LDPC (NB-LDPC) codes present larger coding gain and lower error floor than their binary counterparts in many cases, which show a great potential to be used in the next-generation memories. However, the excessive computational complexity of current NB-LDPC decoding algorithms form a bottleneck and limit their applications. In this paper, a novel algorithm, called dual-threshold-based shrinking based improved trellis-based min-sum algorithm (simply TIT-MSA), is proposed to deal with this problem. The improvements include two steps. The first step is for the check node processing (CNP). Based on the CNP of the simplified min-sum algorithm (SMSA) and that of the trellis-based extended min-sum algorithm (T-EMSA), an improved trellis-based min-sum algorithm (IT-MSA) is developed, which achieves better error performance and lower computational complexity than its origins. The second step is for the whole decoding process. Based on the IT-MSA, the TIT-MSA is proposed, for which two constant thresholds are introduced to remove redundant messages by constructing two subsets of the Galois field. Simulation results show that the error performance of the TIT-MSA is nearly the same as that of the EMSA. Meanwhile, the proposed algorithm can save almost 90% computations compared to the SMSA and T-EMSA.

## Micro-Architecture Design for Low Overhead Fault Tolerant Network-on-Chip

- **Status**: ❌
- **Reason**: NoC 결함내성용 ECC 재사용(Send-Back) HW — LDPC 아닌 일반 ECC, NAND LDPC에 이식할 기법 없음
- **ID**: ieee:8351501
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Chikun Yuan, Letian Huang, Junshi Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8351501
- **Abstract**: Aggressive technology scaling results in reliability decrease of Network-on-Chips (NoCs). Error Correction Codes (ECC) is commonly used to correct error data. It is necessary to balance the reliability of transmissions and the overhead introduced by encoders and decoders. This work utilizes a mechanism reusing decoders in Network Interfaces (NIs), which is named Send-Back ECC. This paper proposes the detailed hardware implementation of Send-Back NoC after hardware overhead optimizing. The design details of the routers and NIs are described. Simulation results prove that the latency of Send-Back ECC is lower than H2H ECC when bit error rate is lower than 0.0002 and always lower than E2E ECC. The hardware overhead of Send-Back ECC is 10.6% lower than H2H ECC, while the energy consumption is also less than both E2E ECC and H2H ECC.

## Research and Implementation of Channel Coding for Ethernet Wireless Laser Communication System

- **Status**: ❌
- **Reason**: 레이저 통신에 표준 LDPC 채널코딩 적용+FPGA 검증, 떼어낼 신규 LDPC 기법 없음 (응용 특이적)
- **ID**: ieee:8469244
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Zhihe Mi, Zhiquan Zhou, Zhanfeng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/8469244
- **Abstract**: Laser will be affected by all kinds of atmospheric conditions when it propagates in the atmosphere, resulting in high bit error rate during communicates and affecting the normal communications. This paper uses the LDPC channel coding to solve this problem. Throughing the simulation and FPGA implementation, the validity of the design is verified in Ehernet communication.

## The optimizing of LDPC coded frequency-hopping communication over blocking interference

- **Status**: ❌
- **Reason**: 주파수도약 통신용 LDPC degree sequence 최적화, 표준 채널별 차수분포 최적화로 NAND 이식 신규 구성기법 부족; 통신 응용 특이적
- **ID**: ieee:8401402
- **Type**: conference
- **Published**: 23-27 May 
- **Authors**: Shiping Liu, Linhua Ma, Xing Hu +1
- **PDF**: https://ieeexplore.ieee.org/document/8401402
- **Abstract**: In order to further improve the anti-interference ability of frequency-hopping communication system over blocking interference. Under the well channel estimation, the frequency-hopping communication system has been improved by the optimizing degree sequences of LDPC codes over mixed channel. It has been proved by simulation that the performance of the codes in which 2048 code length and 0.5 code rate improves 0.62dB under the optimizing degree sequences of erasure probabilities than that over the Gaussian channel by the error rate of 10-5. It also provides a less complicated compromise proposal aiming at its use in actual fight. It's proposed that the frequency-hopping communication under blocking interference, the LDPC code with 0.5 code rate can be optimized under 40% deletion mixed channel, and simulates that the idea can be applied to the actual combat.

## LDPC Code Design for Fast Fading Interference Channels

- **Status**: ❌
- **Reason**: 간섭채널용 LDPC EXIT chart 임계값 설계, 표준 앙상블 최적화로 NAND에 새로 이식할 신규 디코더/구성 없음
- **ID**: ieee:8422463
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Mahdi Shakiba-Herfeh, A. Korhan Tanc, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8422463
- **Abstract**: We focus on two-user Gaussian interference channels (ICs) with fast fading and study implementation of explicit all public and Han-Kobayashi (HK) coding schemes with low-density parity-check (LDPC) codes. Stability conditions for the coding schemes are derived, and a modified form of the EXIT chart analysis is proposed to estimate the decoding threshold of LDPC code ensembles. The proposed code design is employed in several examples and the obtained rate pairs are compared with the achievable rate region (ARR) boundaries demonstrating that rate pairs very close to the ARR boundaries are attained. Performance of finite block length codes are also studied through simulations of specific codes picked from the optimized LDPC code ensembles in order to verify the analysis.

## Synthesizing LDPC Belief Propagation Decoding with Molecular Reactions

- **Status**: ❌
- **Reason**: 분자 화학반응망(CRN) 기반 BP 디코딩; 실리콘 HW 대체 비목적이라 명시, NAND ECC로 이식 불가한 바이오/저속 응용
- **ID**: ieee:8422570
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Xingchi Zhang, Lulu Ge, Xiaohu You +1
- **PDF**: https://ieeexplore.ieee.org/document/8422570
- **Abstract**: This paper proposes a CRN-based implementation approach for low-density parity-check (LDPC) decoding based on belief propagation (BP). Since the belief (probability) can be naturally mapped to molecule concentration, LDPC decoding can be realized with CRNs instead of silicon based hardware. Theoretical analysis and numerical simulations have demonstrated the feasibility of the proposed approach. Note that, we do not try to substitute the silicon-based LDPC decoder with CRN- based one for high-speed applications. We show that this method can be generalized for other BP-based algorithms and is suitable for large-scale, bio- interface, and latency-insensitive applications.

## Parity-Check Polar Coding for 5G and Beyond

- **Status**: ❌
- **Reason**: polar 부호화/rate matching 설계, LDPC로 이식할 디코더 기법 없음
- **ID**: ieee:8422462
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Huazi Zhang, Rong Li, Jian Wang +5
- **PDF**: https://ieeexplore.ieee.org/document/8422462
- **Abstract**: In this paper, we propose a comprehensive Polar coding solution that integrates reliability calculation, rate matching and parity-check coding. Judging a channel coding design from the industry's viewpoint, there are two primary concerns: (i) low-complexity implementation in application-specific integrated circuit (ASIC), and (ii) superior \& stable performance under a wide range of code lengths and rates. The former provides cost- \& power-efficiency which are vital to any commercial system; the latter ensures flexible and robust services. Our design respects both criteria. It demonstrates better performance than existing schemes in literature, but requires only a fraction of implementation cost. With easily-reproducible code construction for arbitrary code rates and lengths, we are able to report ``1-bit'' fine-granularity simulation results for thousands of cases. The released results can serve as a baseline for future optimization of Polar codes.

## HDM: Hyper-Dimensional Modulation for Robust Low-Power Communications

- **Status**: ❌
- **Reason**: hyper-dimensional 변조 기법, LDPC는 성능 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8422472
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Hun-Seok Kim
- **PDF**: https://ieeexplore.ieee.org/document/8422472
- **Abstract**: This paper introduces hyper-dimensional modulation (HDM), a new class of practical modulation scheme for robust communication among low-power and low- complexity devices. Unlike conventional orthogonal modulations, HDM conveys numerous information bits per symbol by combining hyper-dimensional vectors that are not strictly orthogonal to each other. Information bits are spread across many elements in the hyper-dimensional vector, thus HDM is tolerant of element-wise failures in high noise channels. Bit error rate (BER) evaluation results confirm that uncoded HDM with 256-dimension outperforms low density parity check (LDPC) and Polar codes with the same block length of 256. Analysis reveals HDM demodulation complexity is lower than that of LDPC and Polar decoders when the block length is relatively small. Moreover, HDM provides graceful tradeoffs between data rate and signal-to-noise ratio for robust short message communications among power- and complexity- constrained devices.

## Order Statistics on Minimal Euclidean Distance for Blind Linear Block Code Identification

- **Status**: ❌
- **Reason**: 블라인드 부호 식별(code length 추정), ECC 디코더/구성 기법 아님
- **ID**: ieee:8422347
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Aurelien Bonvard, Sebastien Houcke, Melanie Marazin +1
- **PDF**: https://ieeexplore.ieee.org/document/8422347
- **Abstract**: This article deals with the blind detection and identification of error correcting codes. More precisely, we aim at estimating the code length from a noisy bits stream in a non-cooperative context (e.g. Electronic Warfare). In this context, an eavesdropper may intercept a communication. To retrieve the sent information, one can consider identifying the channel code parameters. The method proposed here relies on a statistical analysis of a Euclidean distance matrix. It allows to estimate the code length. We address a process based on soft bits information with no a priori on the encoder used. Finally, we compare our method with a well known algorithm based on Gauss-Jordan elimination.

## A 5G New Radio LDPC Coded NOMA Scheme Supporting High User Load for Massive MTC

- **Status**: ❌
- **Reason**: 5G NOMA(BICMA) 다중접속 기법; 표준 rate-compatible LDPC 그대로 사용, 무선 응용 특이적이라 떼어낼 ECC 기법 없음
- **ID**: ieee:8422611
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Yushu Zhang, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/8422611
- **Abstract**: To provide massive connectivity of a large number of low-power devices in massive machine-type communications (mMTC), advanced physical layer multiple access technologies are imperative for next generation of cellular networks. In this paper, a physical layer non-orthogonal multiple access (NOMA) scheme, called resource-pattern-aided bit-interleave coded multiple access, BICMA for short, is proposed for mMTC to support high and flexible user load energy-efficiently with low complexity. The rate-compatible length-scalable low-density parity check (LDPC) codes, recommended for 5G new radio in 3GPP work item, are firstly incorporated into NOMA schemes to provide great flexibility and compatibility with other services, like enhanced mobile broadband. In BICMA, instead of spreading, the constellation symbols of users are directly mapped to chips according to resource patterns, of which the density can be adjusted to reduce multi-user interference at each chip. Thanks to the rate-compatible length-scalable LDPC codes and flexible resource pattern, the parameter optimization of BICMA is of low complexity. Simulation results show that the energy-efficiency of BICMA is higher than that of orthogonal multiple access schemes, especially with relatively high sum spectral efficiency. Various user loads, as high as 18 users with spectrum efficiency of 0.25 bits/chip/user, can be supported by BICMA, and the required signal-to-noise ratio of each user only increases slightly while much more users could access the same channel resources simultaneously.

## Analysis and Simulation of the IEEE 802.11ay Single-Carrier PHY

- **Status**: ❌
- **Reason**: 802.11ay SC-PHY 분석; LDPC는 MCS의 일부로 부수 언급, 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: ieee:8422532
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Claudio R. C. M. da Silva, Artyom Lomayev, Cheng Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8422532
- **Abstract**: IEEE 802.11ay is an amendment that enables enhanced throughput for IEEE 802.11 systems operating in the license-exempt 60 GHz band. By specifying advanced physical layer (PHY) features such as channel bonding and aggregation, multiple input multiple output (MIMO) transmission, and non-uniform modulation constellation, IEEE 802.11ay supports a maximum data rate of 100 Gb/s, making it an amendment of great interest for applications as diverse as wireless virtual reality (VR) and backhauling. In this paper, we provide a description and analysis of certain fundamental elements of the single-carrier (SC) PHY defined by IEEE 802.11ay. Among the topics that are discussed are the new frame format, modulation and coding schemes (MCSs), and beamforming training field defined in the amendment. Simulation results of key aspects for the topics covered are presented.

## Turbo Product Codes with Irregular Polar Coding for High-Throughput Parallel Decoding in Wireless OFDM Transmission

- **Status**: ❌
- **Reason**: polar 기반 turbo product code 병렬 디코딩, polar/TPC 구조 의존이라 바이너리 LDPC BP 이식 불가
- **ID**: ieee:8422466
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Toshiaki Koike-Akino, Congzhe Cao, Ye Wang
- **PDF**: https://ieeexplore.ieee.org/document/8422466
- **Abstract**: Ultra-reliable forward error correction (FEC) codes approaching the Shannon limit have played an important role in increasing spectral efficiency of wireless communications. In addition to the error correction performance, both low-power and low-latency decoding are demanded for the fifth generation (5G) wireless applications. In this paper, we introduce turbo product codes (TPC) consisting of multiple polar codes to enable highly parallel decoding for high- throughput and low-latency FEC. With turbo iterative decoding, the proposed polar-TPC can outperform the conventional BCH-based TPC by 0.5 dB, and can approach the performance of the corresponding long polar code within 0.2 dB with a capability of 256- times faster decoding. In addition, we apply irregular polar codes, whose polarization units are pruned, to further reduce the computational complexity by 50% and decoding latency by 80% without sacrificing performance. We analyze the impact of list size, turbo iteration count, and fading channels to demonstrate the potential of the polar-TPC for 5G wireless systems.

## RC-UDP: On Raptor Coding over UDP for Reliable High-Bandwidth Data Transport

- **Status**: ❌
- **Reason**: Raptor(fountain/erasure) 코드 over UDP 네트워크 전송; 비-LDPC 부호이며 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8422948
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Abderrahmen Mtibaa, Charles Good, Satyajayant Misra +2
- **PDF**: https://ieeexplore.ieee.org/document/8422948
- **Abstract**: Data-driven and collaborative research has become the trend for today's scientific communities, resulting in large- scale datasets being shared and transported through networks every day. Most of these large data transfers use TCP sockets which are known to be limited in long-distance and high-bandwidth scenarios. UDP, on the other hand, while fast and efficient does not implement any reliability mechanisms. In this paper, we investigate the use of erasure coding techniques, namely fountain codes, on top of UDP to help high speed and reliable data transfer applications to attain high bandwidth in the face of packet losses. We propose RC-UDP, a Raptor Code over UDP framework that enables reliable data transfers for high bandwidth networks. We implement RC-UDP and evaluate its performance using computer simulation (ns-3) and real world testbed experimentations. We compare RC-UDP to HighSpeed and CUBIC TCP. Our results show that RC-UDP, which achieves up to 75X time reduction while incurring minimum overhead, is beneficial when the network is subject to high congestion or packet drop rates.

## Low Complexity Dynamic Soft-Output Sphere Decoding Based on LLR Clipping and Scaled Euclidean Distances

- **Status**: ❌
- **Reason**: MIMO sphere decoder(ML 검출) LLR clipping; LDPC 부호 디코더 아님, 채널 검출 기법으로 이식 부적합
- **ID**: ieee:8423045
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Mitchell J. Grabner, Xinrong Li, Shengli Fu
- **PDF**: https://ieeexplore.ieee.org/document/8423045
- **Abstract**: Sphere Decoding provides a computationally efficient method of solving the maximum-likelihood detection problem in multiple-input multiple-output communication systems. However, the average computational complexity is normally fixed based on an error criteria before hand, meaning that regardless of if the channel conditions support the information rate or a much higher one, the overall complexity does not change. In this paper, we adapt a maximum a-posteriori probability based sphere decoder to support a converging dynamic complexity using the information rate of the system, the receiver signal-to-noise ratio and maximum theoretical capacity with negligible computational overhead.

## Localization-Based Polar Code Construction with Sublinear Complexity

- **Status**: ❌
- **Reason**: polar code 구성법, 부호 비의존 디코더 기법 아니고 LDPC 이식 불가
- **ID**: ieee:8422461
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Ran Zhang, Yiqun Ge, Hamid Saber +2
- **PDF**: https://ieeexplore.ieee.org/document/8422461
- **Abstract**: In this paper, a localization-based polar construction method is proposed to directly find the set of synthetic channels for information bits given a code configuration. Taking advantage of the partial order of polar codes, only a small number of synthetic channels need to be ordered, which scales as $\mathcal{O} (N/\log_2^{3/2}{N})$, resulting in a sublinear complexity to construct a polar code. Specifically, a practical method is put forward first to fast construct a group-based partial order diagram. A local area in the diagram with adaptive boundaries is then identified. By ordering the synthetic channels within the local area and combining selected ones with all the synthetic channels beyond the local area, the final set of synthetic channels for information bits are determined. Simulation results demonstrate how to adapt the boundary settings to different rate matching schemes and code configurations, and validate the effectiveness of the proposed method compared with the density evolution based methods.

## Sparse Message Passing Based Preamble Estimation for Crowded M2M Communications

- **Status**: ❌
- **Reason**: M2M 프리앰블 추정 sparse message passing, factor graph지만 채널 ECC 디코더 아닌 활성도 추정, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:8422285
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Zhaoji Zhang, Ying Li, Lei Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8422285
- **Abstract**: Due to the massive number of devices in the M2M communication era, new challenges have been brought to the existing random-access (RA) mechanism, such as severe preamble collisions and resource block (RB) wastes. To address these problems, a novel sparse message passing (SMP) algorithm is proposed, based on a factor graph on which Bernoulli messages are updated. The SMP enables an accurate estimation on the activity of the devices and the identity of the preamble chosen by each active device. Aided by the estimation, the RB efficiency for the uplink data transmission can be improved, especially among the collided devices. In addition, an analytical tool is derived to analyze the iterative evolution and convergence of the SMP algorithm. Finally, numerical simulations are provided to verify the validity of our analytical results and the significant improvement of the proposed SMP on estimation error rate even when preamble collision occurs.

## Rateless Coded Adaptive Transmission in Cellular Networks: Role of Power Control

- **Status**: ❌
- **Reason**: rateless 코딩+전력제어 적응전송 분석; LDPC 무관, 순수 무선 셀룰러 응용
- **ID**: ieee:8422964
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Amogh Rajanna, Carl P. Dettmann
- **PDF**: https://ieeexplore.ieee.org/document/8422964
- **Abstract**: Adaptive transmission schemes are a key part of the radio design for 5G wireless channels. The paper studies the performance of two types of adaptive transmission schemes in cellular downlink. One is based on rateless codes with constant power and the other is fixed-rate codes in conjunction with power adaptation. Using a simple stochastic geometry model for cellular downlink, the focus is to understand the key impact of power adaptation in rateless and fixed- rate coded adaptive transmission. The performance of both rateless and fixed-rate coded adaptive transmission schemes are compared by evaluating the typical user rate and success probability achievable with the two schemes. Based on both theoretical analysis and simulation results, the paper clearly shows that rateless coding simplifies the role of power control in an adaptive transmission scheme.

## Characterization on Asynchronous Multiple Access in Non-Line of Sight Scattering Communication

- **Status**: ❌
- **Reason**: 비가시거리 산란통신 비동기 다중접속, HMM/Viterbi/BCJR, LDPC 무관
- **ID**: ieee:8403738
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Guanchu Wang, Chen Gong, Zhimeng Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/8403738
- **Abstract**: We investigate the asynchronous multiple access in non-line of sight scattering communication, where different users transmit signals without perfect alignment in the time domain. Firstly, we characterize the received signal based on hidden markov model (HMM) such that the misalignment among different users can be characterized by the state transition. Then, we investigate the achievable rates based on that of the HMM and obtain the approximate solution using Monte Carlo method. We propose the channel estimation based on EM algorithm. Furthermore, we deploy the Viterbi and BCJR algorithms for the symbol detection and propose the iterative algorithm for multi-user joint decoding. Numerical results show the achievable rates, the performance of proposed channel estimation and joint detection as well as decoding.

## Joint Iterative Detection and Decoding Receiver for Polar Coded SCMA System

- **Status**: ❌
- **Reason**: polar coded SCMA 결합 검출/디코딩, 비-LDPC 부호 응용 특이적, 이식 가능 LDPC 기법 없음
- **ID**: ieee:8403620
- **Type**: conference
- **Published**: 20-24 May 
- **Authors**: Zhipeng Pan, Erbao Li, Lei Wen +2
- **PDF**: https://ieeexplore.ieee.org/document/8403620
- **Abstract**: SCMA and polar coding are possible candidates for 5G systems. In this paper, we develop a joint iterative detection and decoding (JIDD) receiver for the uplink polar coded sparse code multiple access (PC-SCMA) system. In JIDD receiver, messages are exchanged between SCMA detector and polar decoder during each iteration. This is the first joint design for PC-SCMA which has no inner iterations of SCMA detector and polar decoder. But only outer iterations are needed. Simulation results demonstrate that JIDD has lower complexity and better performance than the separate scheme. It obtains 4.8dB performance gain with code length and code rate of polar code are $N=256$ and $R=1/2$ and 3.4dB performance gain with $N=1024$ and $R=1/3$, respectively. Especially, under 150$\text{\%}$ system loading, JIDD only has 0.3dB performance loss compared with the single user uplink PC-SCMA system. The JIDD receiver only needs 5 iterations to converge, which is much less than the other joint receiver for LDPC coded or Turbo coded SCMA systems (need dozens of iterations to converge). Thus, the whole complexity of JIDD for PC-SCMA is much lower than the other two joint receivers.

## Baseband implementation of high speed communication system on FPGA

- **Status**: ❌
- **Reason**: 240GHz OFDM 베이스밴드 FPGA에 LDPC 인코더/디코더 포함되나 표준 구현 일부, 새 디코더/HW 기여 없음
- **ID**: ieee:8404696
- **Type**: conference
- **Published**: 2-5 May 20
- **Authors**: Mustafa Öztürk, Emre Kirkaya, Erşen Balcisoy +3
- **PDF**: https://ieeexplore.ieee.org/document/8404696
- **Abstract**: For high speed data transfer with 240 GHz OFDM based communication system, the baseband calculations should be done at very high processing rate to be able to use communication channel effectively. To reach that much speed, a baseband system is developed on FPGA. Random data generator, LDPC encoder and decoder, QPSK modulator, IFFT and FFT, STBC encoder and decoder with an AWGN generator for channel modeling at 250 MHz clock frequency are tested via simulation and verified by MATLAB model of the system. In addition, the whole system design is implemented at various frequencies on FPGA and simulation results are verified by using embedded integrated logic analyzer.

## On Performance of Multilevel Coding Schemes Based on Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 멀티레벨 코딩 — 비이진 LDPC는 NAND 바이너리 ECC 대상 아님(제외)
- **ID**: ieee:8385517
- **Type**: conference
- **Published**: 2-4 May 20
- **Authors**: Stanislav Kruglik, Valeriya Potapova, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/8385517
- **Abstract**: We address the problem of constructing of coding schemes for the channels with high-order modulations. It is known, that non-binary LDPC codes are especially good for such channels and significantly outperform their binary counterparts. Unfortunately, their decoding complexity is still large. In order to reduce the decoding complexity we consider multilevel coding schemes based on non-binary LDPC codes (NB-LDPC-MLC schemes) over smaller fields. The use of such schemes gives us a reasonable gain in complexity. At the same time the performance of NB-LDPC-MLC schemes is practically the same as the performance of LDPC codes over the field matching the modulation order. In particular by means of simulations we showed that the performance of NB-LDPC-MLC schemes over GF(16) is the same as the performance of non-binary LDPC codes over GF(exp 64) and GF(exp 256) in AWGN channel with QAM (exp 64) and QAM 256 accordingly. We also perform a comparison with bitinterleaved coded modulation based on binary LDPC codes.

## Polar Codes and Polar Lattices for the Heegard-Berger Problem

- **Status**: ❌
- **Reason**: Polar 부호 + 소스 코딩(rate-distortion, lossy source coding) — 비-LDPC이며 소스코딩이라 제외
- **ID**: ieee:8385518
- **Type**: conference
- **Published**: 2-4 May 20
- **Authors**: Jinwen Shi, Ling Liu, Deniz Guenduez +1
- **PDF**: https://ieeexplore.ieee.org/document/8385518
- **Abstract**: Explicit coding schemes are proposed to achieve the rate-distortion bound for the Heegard-Berger problem using polar codes. Specifically, a nested polar code construction is employed to achieve the rate-distortion bound for the binary case. The nested structure contains two optimal polar codes for lossy source coding and channel coding, respectively. Moreover, a similar nested polar lattice construction is employed for the Gaussian case. The proposed polar lattice is constructed by nesting a quantization polar lattice and an AWGN capacityachieving polar lattice.

## Improved CE-OFDM Using LDPC Codes for Frequency Offset Compensation

- **Status**: ❌
- **Reason**: 위성통신 CE-OFDM의 CFO 보정에 LDPC를 부수적으로 삽입, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:8553961
- **Type**: conference
- **Published**: 11-12 May 
- **Authors**: Shagun Sharma, Khushal Thakur
- **PDF**: https://ieeexplore.ieee.org/document/8553961
- **Abstract**: The CE-OFDM is the scheme which can avoid signal distortion which is caused by non linear power amplifier. In this paper, improved CFO scheme is proposed for the CE-ODFM in satellite communication. In the proposed scheme LDPC codes are inserted after Conjugate Symmetry to estimate the CFO at sender and receiver side. The simulation results of the improved CE-OFDM scheme with LDPC code is compared with CE-OFDM scheme without LDPC codes in terms of signal-to-noise ratio over the white Gaussian noise channel. The results shows that proposed model performs well as compared to existing scheme.

## Performance enhancement of wireless sensor networks using an efficient coding approach

- **Status**: ❌
- **Reason**: WSN에서 RLNC+LDPC 결합 응용, BER 개선 무선 응용 특이적이며 떼어낼 ECC 기법 없음
- **ID**: ieee:8525943
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Youssra Chatei, Imane Maslouhi, Kamal Ghoumid +1
- **PDF**: https://ieeexplore.ieee.org/document/8525943
- **Abstract**: The Random Linear Network Coding (RLNC) has been investigated as a promising solution for improve transmission reliability; however, it is highly susceptible to errors. In wireless sensor networks (WSN), The problem resemblance to a column vector on the generator matrix of Low-Density Parity-Check (LDPC) matrix is caused by the important similarity between received symbols from the cluster head (CH). To deal with this problem, we have to reduce BER. The principal objective of this paper is to use an efficient coding approach based on the RNC and LDPC codes using TDMA (Time Division Multiple Access) technology. The coding techniques employed in this paper are focused on enhance planning to report error-bit (BER) vs. signal-to-noise (SNR), between CHs and the base station (BS) node in dense WSN, while describing each point examining effective use of the proposed algorithm.
