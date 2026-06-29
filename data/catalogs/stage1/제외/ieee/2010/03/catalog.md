# IEEE Xplore — 2010-03


## Nonbinary LDPC codes constructed based on a cyclic MDS code and a low-complexity nonbinary message-passing decoding algorithm

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC 구성+nonbinary message-passing 디코더. 비이진 LDPC는 제외 대상
- **ID**: ieee:5426595
- **Type**: journal
- **Published**: March 2010
- **Authors**: Chao Chen, Baoming Bai, Xinmei Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5426595
- **Abstract**: In this letter, we propose a construction of nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes based on a cyclic maximum distance separable (MDS) code. The parity-check matrices are significantly rank deficient square matrices and their Tanner graphs have a girth of at least 6. The minimum distances of the codes are very respectable as far as LDPC codes are concerned. Based on plurality voting and iterative mechanism, a low-complexity nonbinary massage-passing decoding algorithm is proposed. It only requires finite field operations, integer additions and integer comparisons. Simulation results show that the decoding algorithm is fit for the proposed codes, providing efficient trade-offs between performance and decoding complexity, which suggests that the coding scheme may find some applications in communication or storage systems with high-speed and low-power consumption requirements.

## Burst Decoding of Cyclic Codes Based on Circulant Parity-Check Matrices

- **Status**: ❌
- **Reason**: 순환부호 버스트 정정 알고리즘(circulant PCM). 비-LDPC cyclic 코드 중심, LDPC는 부수 언급뿐
- **ID**: ieee:5429123
- **Type**: journal
- **Published**: March 2010
- **Authors**: Shumei Song, Shu Lin, Khaled Abdel-Ghaffar +3
- **PDF**: https://ieeexplore.ieee.org/document/5429123
- **Abstract**: An error-burst correcting algorithm is developed based on a circulant parity-check matrix of a cyclic code. The proposed algorithm is more efficient than error trapping if the code rate is less than about 2/3. It is shown that for any (n, k) cyclic code, there is an n × n circulant parity-check matrix such that the algorithm, applied to this matrix, corrects error bursts of lengths up to the error-burst correction limit of the cyclic code. This same matrix can be used to efficiently correct erasure bursts of lengths up to n - k. The error-burst correction capabilities of a class of cyclic low-density parity-check (LDPC) codes constructed from finite geometries are also considered.

## Design of bandwidth-efficient unequal error protection LDPC codes

- **Status**: ❌
- **Reason**: 고차 변조용 UEP LDPC 코드설계(density evolution degree distribution). 변조 의존 무선 응용 특이, NAND 이식 기법 약함
- **ID**: ieee:5426513
- **Type**: journal
- **Published**: March 2010
- **Authors**: Sara Sandberg, Neele Von Deetzen
- **PDF**: https://ieeexplore.ieee.org/document/5426513
- **Abstract**: This paper presents a strategy for the design of bandwidth-efficient LDPC codes with unequal error protection. Bandwidth efficiency is obtained by appropriately designing the codes for higher order constellations, assuming an AWGN channel. The irregularities of the LDPC code are designed, using the Gaussian approximation of the density evolution, to enhance the unequal error protection property of the code as well as account for the different bit error probabilities given by the higher order constellation. The proposed code design algorithm is flexible in terms of the number and proportions of protection classes. It also allows arbitrary modulation schemes. Our method combines the design of unequal error protection LDPC codes for the binary input AWGN channel with the code design for higher order constellations by dividing the variable node degree distribution into sub-degree distributions for each protection class and each level of protection from the modulation. The results show that appropriate code design for higher order constellations reduces the overall bit-error rate significantly. Furthermore, the unequal error protection capability of the code is increased, especially for high SNR.

## Lossy Source Compression Using Low-Density Generator Matrix Codes: Analysis and Algorithms

- **Status**: ❌
- **Reason**: LDGM 손실 소스 압축(rate-distortion). 소스코딩이며 채널 ECC 아님
- **ID**: ieee:5429117
- **Type**: journal
- **Published**: March 2010
- **Authors**: Martin J. Wainwright, Elitza Maneva, Emin Martinian
- **PDF**: https://ieeexplore.ieee.org/document/5429117
- **Abstract**: We study the use of low-density generator matrix (LDGM) codes for lossy compression of the Bernoulli symmetric source. First, we establish rigorous upper bounds on the average distortion achieved by check-regular ensemble of LDGM codes under optimal minimum distance source encoding. These bounds establish that the average distortion using such bounded degree families rapidly approaches the Shannon limit as the degrees are increased. Second, we propose a family of message-passing algorithms, ranging from the standard belief propagation algorithm at one extreme to a variant of survey propagation algorithm at the other. When combined with a decimation subroutine and applied to LDGM codes with suitably irregular degree distributions, we show that such a message-passing/decimation algorithm yields distortion very close to the Shannon rate-distortion bound for the binary symmetric source.

## Joint Nonlinear Channel Equalization and Soft LDPC Decoding With Gaussian Processes

- **Status**: ❌
- **Reason**: Gaussian process 비선형 채널 등화 중심. LDPC 디코더는 성능 측정용일 뿐 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5290078
- **Type**: journal
- **Published**: March 2010
- **Authors**: Pablo M. Olmos, Juan José Murillo-Fuentes, Fernando Perez-Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5290078
- **Abstract**: In this paper, we introduce a new approach for nonlinear equalization based on Gaussian processes for classification (GPC). We propose to measure the performance of this equalizer after a low-density parity-check channel decoder has detected the received sequence. Typically, most channel equalizers concentrate on reducing the bit error rate, instead of providing accurate posterior probability estimates. We show that the accuracy of these estimates is essential for optimal performance of the channel decoder and that the error rate output by the equalizer might be irrelevant to understand the performance of the overall communication receiver. In this sense, GPC is a Bayesian nonlinear classification tool that provides accurate posterior probability estimates with short training sequences. In the experimental section, we compare the proposed GPC-based equalizer with state-of-the-art solutions to illustrate its improved performance.

## Analysis and optimization of a rateless coded joint relay system

- **Status**: ❌
- **Reason**: 릴레이 시스템 Raptor(rateless) 코드 EXIT 최적화. 비-LDPC rateless, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:5427449
- **Type**: journal
- **Published**: March 2010
- **Authors**: Chen Gong, Guosen Yue, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/5427449
- **Abstract**: We consider the code design for a half-duplex 4-node joint relay system with two sources, one relay, and one destination. The relay combines the information from both sources and transmits it to the destination together with both sources. We consider two coding schemes for information combining at the relay, namely, the superposition coding (SC) and the Raptor coding (RC). The Raptor codes are employed at the sources as well as the relay. The relay and the destination perform iterative a posteriori probability (APP) detection and soft Raptor decoding. For both SC and RC, the profiles for Raptor codes are optimized based on the extrinsic information transfer (EXIT) function analysis. For both the additive white Gaussian noise (AWGN) and block fading channels, the joint relay system with optimized profiles exhibits significant performance gains over that employing the code profile optimized for either the singleuser AWGN channel or the 2-user multiple-access channel.

## Sparse Channel Estimation for Multicarrier Underwater Acoustic Communication: From Subspace Methods to Compressed Sensing

- **Status**: ❌
- **Reason**: 수중음향 멀티캐리어 sparse 채널 추정(compressed sensing). LDPC와 무관, ECC 기법 없음
- **ID**: ieee:5352256
- **Type**: journal
- **Published**: March 2010
- **Authors**: Christian R. Berger, Shengli Zhou, James C. Preisig +1
- **PDF**: https://ieeexplore.ieee.org/document/5352256
- **Abstract**: In this paper, we investigate various channel estimators that exploit channel sparsity in the time and/or Doppler domain for a multicarrier underwater acoustic system. We use a path-based channel model, where the channel is described by a limited number of paths, each characterized by a delay, Doppler scale, and attenuation factor, and derive the exact inter-carrier-interference (ICI) pattern. For channels that have limited Doppler spread we show that subspace algorithms from the array processing literature, namely Root-MUSIC and ESPRIT, can be applied for channel estimation. For channels with Doppler spread, we adopt a compressed sensing approach, in form of Orthogonal Matching Pursuit (OMP) and Basis Pursuit (BP) algorithms, and utilize overcomplete dictionaries with an increased path delay resolution. Numerical simulation and experimental data of an OFDM block-by-block receiver are used to evaluate the proposed algorithms in comparison to the conventional least-squares (LS) channel estimator. We observe that subspace methods can tolerate small to moderate Doppler effects, and outperform the LS approach when the channel is indeed sparse. On the other hand, compressed sensing algorithms uniformly outperform the LS and subspace methods. Coupled with a channel equalizer mitigating ICI, the compressed sensing algorithms can effectively handle channels with significant Doppler spread.

## Rateless coding for hybrid free-space optical and radio-frequency communication

- **Status**: ❌
- **Reason**: FSO/RF 하이브리드 rateless(Raptor) 코딩 ARQ. fountain/rateless, LDPC ECC 기법 아님
- **ID**: ieee:5427418
- **Type**: journal
- **Published**: March 2010
- **Authors**: Ali Abdulhussein, Anand Oka, Trung Thanh Nguyen +1
- **PDF**: https://ieeexplore.ieee.org/document/5427418
- **Abstract**: Free-space optical (FSO) transmission systems enable high-speed communication with relatively small deployment costs. However, FSO suffers a critical disadvantage, namely susceptibility to fog, smoke, and conditions alike. A possible solution to this dilemma is the use of hybrid systems employing FSO and radio frequency (RF) transmission. In this paper we propose the application of a rateless coded automatic repeatrequest scheme for such hybrid FSO/RF systems. The advantages of our approach are (a) the full utilization of available FSO and RF channel resources at any time, regardless of FSO or RF channel conditions and temporal variations, and (b) no need for a-priori rate selection at the transmitter. In order to substantiate these claims, we establish the pertinent capacity limits for hybrid FSO/RF transmission and present simulation results for transmission with off-the-shelf Raptor codes, which achieve realized rates close to these limits under a wide range of channel conditions. We also show that in conditions of strong atmospheric turbulence, rateless coding is advantageous over fixed-rate coding with rate adaptation at the transmitter.

## Drizzle: Cooperative Symbol-Level Network Coding in Multichannel Wireless Networks

- **Status**: ❌
- **Reason**: 무선 심볼레벨 네트워크코딩/HARQ 처리량 향상. LDPC 부재, 떼어낼 ECC 디코더 기법 없음
- **ID**: ieee:5378535
- **Type**: journal
- **Published**: March 2010
- **Authors**: Ronny Yongho Kim, Jin Jin, Baochun Li
- **PDF**: https://ieeexplore.ieee.org/document/5378535
- **Abstract**: Errors are inherently present in unreliable wireless channels. The primary challenge in designing error-control protocols in the medium-access control (MAC) or physical layer is to effectively maximize achievable throughput in wireless networks, even when unpredictable and time-varying errors exist. Network coding has successfully been applied to improve throughput in IEEE 802.11-based wireless networks with a shared broadcast channel. In state-of-the-art physical-layer designs in multichannel wireless networks [such as IEEE 802.16 Worldwide Interoperability for Microwave Access (WiMAX)], however, the convenience of a shared wireless broadcast channel to perform opportunistic listening no longer exists, and hybrid automatic repeat request (HARQ) is the predominant error-control protocol in the physical layer, rather than plain automatic repeat request in IEEE 802.11 MAC. Would network coding be well employed in multichannel wireless networks and able to bring further improvements over HARQ? This paper proposes Drizzle, which is a new solution to maximizing throughput with the presence of errors, which takes advantage of network coding at the symbol level in multichannel wireless networks. By operating at the symbol level and using soft-decision values, we show that Drizzle is able to exploit both time and cooperative diversity in realistic multichannel wireless networks, to adapt to time-varying and bursty channel errors, and to efficiently collect as many correct symbols as possible at the receiver.

## Linear Precoder Design Through Cut-Off Rate Maximization in MIMO-OFDM Coded Systems With Imperfect CSIT

- **Status**: ❌
- **Reason**: MIMO-OFDM linear precoder 설계, cut-off rate 최대화. 코드 비의존적 송신기 설계로 LDPC ECC 기법 없음
- **ID**: ieee:5325696
- **Type**: journal
- **Published**: March 2010
- **Authors**: Francesc Rey, Meritxell Lamarca, Gregori Vazquez
- **PDF**: https://ieeexplore.ieee.org/document/5325696
- **Abstract**: This paper proposes a linear transmitter design that aims at minimizing the packet error rate (PER) using partial channel state information at the transmitter (CSIT). The design is based on the maximization of the channel cut-off rate, which provides an upper bound on the codeword error probability over the ensemble of random codes. The advantage of this optimization criterion is that it allows to get a low PER while keeping the design independent of the specific channel code used in the system. The algorithm is derived for a multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) system, and adopts a Bayesian approach to design an algorithm robust to CSI errors. The proposed algorithm converges to the open-loop transmission scheme for the case of no channel knowledge and it converges to the closed-loop design with perfect CSI for the case of no uncertainty. Simulation results evidence the performance gain in terms of PER and throughput of the proposed algorithm when compared to more commonly used optimization criteria.

## A Linear Encoding Approach to Index Assignment in Lossy Source-Channel Coding

- **Status**: ❌
- **Reason**: lossy source-channel coding (JSCC)+소스 양자화; LDPC가 베이스라인, 떼어낼 NAND ECC 디코더/코드설계 기법 없음
- **ID**: ieee:5429132
- **Type**: journal
- **Published**: March 2010
- **Authors**: Maria Fresia, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/5429132
- **Abstract**: We present a general scheme for the lossy transmission of a source with arbitrary statistics through a noisy channel under the mean-square error fidelity criterion. Our approach is based on transform coding, scalar quantization of the transform coefficients and linear encoding of the quantization indices. Entropy coding and channel coding are merged into a single linear encoding function, such that the ¿catastrophic¿ behavior of conventional entropy coding is avoided and the full power of modern coding techniques and iterative ¿Belief-Propagation¿ decoding can be exploited. We show that this approach is asymptotically optimal in the limit of large block length, for arbitrary source statistics and binary-input output-symmetric channel. In the practical regime of finite block length and low decoding complexity, we show, through the explicit construction of codes for the lossy transmission of digital images over a binary symmetric channel, that our approach yields significant improvements with respect to previously proposed channel-optimized quantization schemes and also with respect to the conventional concatenation of state-of-the art image coding with state-of-the art channel coding. Although our constructive example focuses on a special case, the approach is general and can be applied to other classes of sources of practical interest.

## Randomized parity forwarding in large-scale cooperative broadcast network

- **Status**: ❌
- **Reason**: 협동 브로드캐스트 분산 패리티 생성 프로토콜. 네트워크 코딩 응용, 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:5426519
- **Type**: journal
- **Published**: March 2010
- **Authors**: Sang Wu Kim
- **PDF**: https://ieeexplore.ieee.org/document/5426519
- **Abstract**: We present a randomized cooperative broadcasting technique that is flexible to topology changes and robust to transmission errors in large-scale wireless networks. A single source sends a common message (codeword) to all nodes, and those nodes that decode the message correctly then generate a parity bit (a partial information on the message) and broadcast it to the remaining nodes. The remaining nodes integrate the original codeword from the source with the network-generated parity bits to construct a lower rate, and thus more powerful, error correcting code. The protocol overhead is significantly reduced by allowing each node to randomly generate a parity bit independent of other nodes. We show that the probability of decoding error decreases exponentially with the number of nodes in the network, and that the performance degradation relative to the deterministic parity generation (that requires a centralized coordination of nodes) becomes smaller as the number of nodes increases. We also show that the proposed approach enables all nodes to correctly receive the message within the first cooperation stage if the number of nodes is sufficiently large. Hence, the proposed approach is promising for applications in large-scale wireless broadcast networks.

## SimTag: Exploiting tag bits similarity to improve the reliability of the data caches

- **Status**: ❌
- **Reason**: 캐시 tag bit 유사도 기반 오류복구, LDPC와 무관
- **ID**: ieee:5456917
- **Type**: conference
- **Published**: 8-12 March
- **Authors**: Jesung Kim, Soontae Kim, Yebin Lee
- **PDF**: https://ieeexplore.ieee.org/document/5456917
- **Abstract**: Though tag bits in the data caches are vulnerable to transient errors, few effort has been made to reduce their vulnerability. In this paper, we propose to exploit prevalent same tag bits to improve error protection capability of the tag bits in the data caches. When data are fetched from the main memory, it is checked if adjacent cache lines have the same tag bits as those of the data fetched. This similarity information is stored in the data caches as extra bits to be used later. When an error is detected in the tag bits, the similarity information is used to recover from the error in the tag bits. The proposed scheme has small area, energy, and performance overheads with error protection coverage of 97.9% on average. In contrast, the previously proposed In-Cache Replication scheme is shown to incur large performance and energy overheads.

## Optical communications performance of hybrid 34-meter microwave antennas

- **Status**: ❌
- **Reason**: 광통신 안테나 설계, LDPC 기법 전혀 없음
- **ID**: ieee:5446955
- **Type**: conference
- **Published**: 6-13 March
- **Authors**: V. Vilnrotter, D. Hoppe, B. Moision +1
- **PDF**: https://ieeexplore.ieee.org/document/5446955
- **Abstract**: There is considerable interest in determining whether suitably modified versions of existing 34-meter antennas at NASA's Goldstone Communications Complex, originally designed for X-band (nominally 8 GHz) and Ka-band (32 GHz) operation, could also be used to receive near-infrared optical signals. The robust backup structure of these antennas, together with extremely large collecting apertures and milli-degree pointing capabilities suggest that dual RF/Optical communications may indeed be possible, at optical data-rates approaching 1 gigabit per second (GBPS) from typical Mars distances. Several design concepts have emerged as possible candidates, requiring modifications ranging from polishing and coating of the existing aluminum panels of the main reflector, to significant redesign involving replacement of the panels with optical reflectors. Optical receiver parameters such as collecting area, field-of-view (FOV), and immunity to reflected sunlight differ markedly for each design concept, hence will likely lead to different levels of performance in terms of data-throughput at a given BER, and in terms of the ability to point close to the sun. The communications performance of two candidate design concepts operating under realistic daytime conditions is evaluated, with particular emphasis on spatial and temporal acquisition algorithms and receiver optimization to achieve the best possible communication performance at high data rates.

## A DVB-T2 receiver realization based on a software-defined radio concept

- **Status**: ❌
- **Reason**: DVB-T2 SDR 수신기 데모 구현, 표준 LDPC 디코딩 적용일 뿐 신규 디코더/HW 기여 없음
- **ID**: ieee:5463488
- **Type**: conference
- **Published**: 3-5 March 
- **Authors**: Christian Kocks, Alexander Viessmann, Andreas Waadt +7
- **PDF**: https://ieeexplore.ieee.org/document/5463488
- **Abstract**: When DVB-T (Digital Video Broadcasting - Terrestrial) was introduced in the 1990s, it was impossible to foresee the upcoming demand for HDTV devices. Thus, a revision of this broadcasting standard, namely DVB-T2, was necessary. Recently finalized, this standard is targeting to high-definition television (HDTV). To pave the way to commercialization, an appropriate implementation concept and its corresponding validation are of utmost importance. Without a doubt, the most challenging requirements introduced by the DVB-T2 specification are an FFT (Fast Fourier Transform) size of up to 32k samples, 256-QAM (Quadrature Amplitude Modulation) and LDPC (Low-Density Parity-Check) coding with a block size of 64800 bits. Within this manuscript, the authors present a software-defined radio based realization of a demonstrator platform. This platform employs a combined DSP (Digital Signal Processor) and FPGA (Field-Programmable Gate Array) solution being capable of meeting these requirements.

## Adaptive channel coding for the three-node relay channel with limited channel-state information

- **Status**: ❌
- **Reason**: 3노드 릴레이 채널용 적응 채널코딩, 무선 WSN 응용 특이적, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:5463299
- **Type**: conference
- **Published**: 3-5 March 
- **Authors**: Zhongwei Si, Ragnar Thobaben, Mikael Skoglund
- **PDF**: https://ieeexplore.ieee.org/document/5463299
- **Abstract**: We address the design of adaptive channel codes for the three-node relay channel. In order to make the code design feasible for wireless sensor-network (WSN) applications, we focus on the special case where only limited channel-state information is available for code adaptation. For this purpose we design distributed codes which feature a limited set of modes which are optimized to serve a certain range of channel conditions. As the results show, a good performance in terms of coverage and achievable rate is maintained compared to the case with perfect channel-state information. If the target application is spectrum sensing, the proposed scheme provides a feasible solution to improve the sensing performance and to reduce the latency due to its increased data rate compared to standard solutions.

## Coded CP-SC communication scheme for outdoor power line communications

- **Status**: ❌
- **Reason**: PLC 채널 LDPC+CP-SC 임펄스노이즈 평가—표준 LDPC 응용 평가, 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:5479907
- **Type**: conference
- **Published**: 28-31 Marc
- **Authors**: Filipe A. La-Gatta, Moisés V. Ribeiro, Andrei P. Legg +1
- **PDF**: https://ieeexplore.ieee.org/document/5479907
- **Abstract**: In this paper, we consider a cyclic prefixed single-carrier communication scheme with frequency domain equalization (CP-SC) and low-density parity check code (LDPC) over power line communication (PLC) channel. The aim is to evaluate the error performance when the PLC channel is corrupted by impulsive noise. The simulation results show that the best performance is obtained when the LDPC code is considered in association with the frequency domain equalizer based on the MMSE criterion. Additionaly, comparative results between the CP-SC and SC-DFE are presented. The results indicate that CP-SC with FDE-MMSE offer better performance than SC-DFE. Moreover, we present a simulation result that indicates that if the channel decoder has correct information about the impulsive noise variance, then error performance improvements can be obtained.

## An improved implementation scheme based on BICM for IBOC-AM

- **Status**: ❌
- **Reason**: IBOC-AM BICM 채널코딩 개선—LDPC/convolutional 선택 응용 특이적, 떼어낼 디코더/구성 없음
- **ID**: ieee:5486894
- **Type**: conference
- **Published**: 27-29 Marc
- **Authors**: Liu Shuyang, Yang Gang, Li Jianping
- **PDF**: https://ieeexplore.ieee.org/document/5486894
- **Abstract**: This paper proposes an improved channel coding scheme based on bit-interleaved coded modulation (BICM) for in-band on-channel amplitude modulation (IBOC-AM). It can yield better coding gains than traditional scheme over Rayleigh fading channels. Generally, BICM embedded LDPC code for IBOC (BICM-L) has better coding performances than BICM embedded convolutional codes for IBOC (BICM-C), which has been proved to be an advanced scheme. However, there is a zone named blind-zone existing in the region of SNRs, where the performance gains of BICM-L with high-order modulation are worse than BICM-C. To achieve an improved performance, for the blind-zone?? BICM-L is replaced by BICM-C in this improved scheme. Simulation results confirm that, by using the proposed improved scheme, a better performance gains up to 0.3 dB can be achieved for the blind-zone between 4 dB SNR and 5.1 dB SNR, while an additional gains about 4 dB can be achieved in regions of high SNRs.

## Rate-Compatible Slepian-Wolf Coding with Short Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 LDPC + Slepian-Wolf 소스코딩, 이중 제외
- **ID**: ieee:5453449
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Kenta Kasai, Takayuki Tsujimoto, Ryutaroh Matsumoto +1
- **PDF**: https://ieeexplore.ieee.org/document/5453449
- **Abstract**: Rate-compatible asymmetric Slepian-Wolf coding with non-binary LDPC codes of moderate code length is presented.The proposed encoder and decoder use only one single mother code.With the proposed scheme, better compressed rate and lower error rate than those ofconventional scheme are achieved with even smaller source length.

## Theoretically Optimal Low-Density Parity-Check Code Ensemble for Gallager's Decoding Algorithm A

- **Status**: ❌
- **Reason**: Gallager 알고리즘A 최적 앙상블 순수 이론 bound, 디코더/HW/구성 이식 없음
- **ID**: ieee:5453535
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Feng Wu, Peiwen Yu
- **PDF**: https://ieeexplore.ieee.org/document/5453535
- **Abstract**: For a class of low-density parity-check (LDPC) code ensembles with right node degrees as binomial distribution, this paper proves that the theoretically optimal LDPC code ensemble should be regular for a binary-symmetric channel (BSC) and Gallager’s decoding algorithm A. Our proof consists of two steps. First, with the assumption of right edge degrees as binomial, we prove that the LDPC threshold of single left edge degree is larger than that of multiple left edge degrees. Second, we verify that the LDPC threshold is the largest when binomial distribution of right node degrees degrades to single value. Very interestingly, although both right and left edge degrees are unique in the theoretically optimal LDPC code ensemble, they are floating values. When the floating degrees are approximated by a two-term binomial distribution, the threshold at half rate is exactly the same as Bazzi’s result via linear programming. It verifies our proof from another angle

## Fast implementation of Wyner-Ziv Video codec using GPGPU

- **Status**: ❌
- **Reason**: GPGPU Wyner-Ziv 비디오 Slepian-Wolf 소스코딩 구현, 채널 ECC 아님
- **ID**: ieee:5463150
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Ryanggeun Oh, Jongbin Park, Byeungwoo Jeon
- **PDF**: https://ieeexplore.ieee.org/document/5463150
- **Abstract**: In this paper, we report a fast implementation of Wyner-Ziv video decoder using general-purpose computing on graphics processing units (GPGPU). Despite of its many advantages, Wyner-Ziv video coding has a problem of huge decoding complexity. Since Slepian-Wolf decoding with rate adaptive LDPC accumulate code takes up more than 90% of entire Wyner-Ziv video decoding complexity, in this paper, we focus on fast implementation of the Slepian-Wolf decoder using the CUDA (Compute Unified Device Architecture) which is a GPGPU architecture developed by NVIDIA. Our implementation is shown to be 4~5 times (QCIF size) or 15~20 times (CIF size) faster compared to conventional Slepian-Wolf decoding.

## Analysis of LDPC Codes for Compression of Nonuniform Sources with Side Information Using Density Evolution

- **Status**: ❌
- **Reason**: 분산 소스코딩(압축) LDPC, 채널 ECC 아님
- **ID**: ieee:5453501
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Raghunadh K. Bhattar, K. R. Ramakrishnan, K. S. Dasgupta
- **PDF**: https://ieeexplore.ieee.org/document/5453501
- **Abstract**: In this paper, we explore the use of LDPC codes for nonuniform sources under distributed source coding paradigm. Our analysis reveals that several capacity approaching LDPC codes indeed do approach the Slepian-Wolf bound for nonuniform sources as well. The Monte Carlo simulation results show that highly biased sources can be compressed to 0.049 bits/sample away from Slepian-Wolf bound for moderate block lengths.

## LDPC Codes for Information Embedding and Lossy Distributed Source Coding

- **Status**: ❌
- **Reason**: 정보임베딩/lossy 분산소스코딩, 채널 ECC 아님
- **ID**: ieee:5453526
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Mina Sartipi
- **PDF**: https://ieeexplore.ieee.org/document/5453526
- **Abstract**: Inspired by our recent work on lossy distributed source coding with side information available at the decoder, we propose a practical scheme for information embedding system with side information available at the encoder. Our proposed scheme is based on sending parity bits using LDPC codes. We provide a design procedure for the LDPC code that guarantees performance close to the Gelfand-Pinsker and Wyner-Ziv limits. Using simulation results, we show that the proposed method performs close to both Wyner-Ziv and Gelfand-Pinsker theoretical limits for even short length codes.

## Tanner Graph Based Image Interpolation

- **Status**: ❌
- **Reason**: 이미지 보간에 BP 적용, 채널 ECC 기법 없음
- **ID**: ieee:5453483
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Ruiqin Xiong, Wen Gao
- **PDF**: https://ieeexplore.ieee.org/document/5453483
- **Abstract**: This paper interprets image interpolation as a channel decoding problem and proposes a tanner graph based interpolation framework, which regards each pixel in an image as a variable node and the local image structure around each pixel as a check node. The pixels available from low-resolution image are "received" whereas other missing pixels of highresolution image are "erased", through an imaginary channel. Local image structures exhibited by the low-resolution image provide information on the joint distribution of pixels in a small neighborhood, and thus play the same role as parity symbols in the classic channel coding scenarios. We develop an efficient solution for the sum-product algorithm of belief propagation in this framework, based on a gaussian auto-regressive image model. Initial experiments show up to 3dB gain over other methods with the same image model. The proposed framework is flexible in message processing at each node and provides much room for incorporating more sophisticated image modelling techniques.

## Rate Distortion Bounds for Binary Erasure Source Using Sparse Graph Codes

- **Status**: ❌
- **Reason**: BES 소스코딩 rate-distortion 순수 bound, 채널 ECC 아님
- **ID**: ieee:5453435
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Grégory Demay, Vishwambhar Rathi, Lars K. Rasmussen
- **PDF**: https://ieeexplore.ieee.org/document/5453435
- **Abstract**: We consider lower bounds on the rate-distortion performance for the binary erasure source(BES) introduced by Martinian and Yedidia, using sparse graph codes for compression. Our approach follows that of Kudekar and Urbanke, where lower bounds on the rate distortion performance of low-density generator matrix (LDGM) codes for the binary symmetric source(BSS) are derived. They introduced two methods for deriving lower bounds, namely the counting method and the test channel method. Based on numerical results they observed that the two methods lead to the same bound. We generalize these two methods for the BES and prove that indeed both methods lead to identical rate-distortion bounds for the BES and hence, also forthe BSS.

## On the design of different concurrent EDC schemes for S-Box and GF(p)

- **Status**: ❌
- **Reason**: 암호 HW(AES S-Box) 오류검출/정정용 패리티예측 — LDPC가 여러 코드 중 하나로 부수 언급, 보안 도메인, 떼어낼 LDPC 기법 없음
- **ID**: ieee:5450467
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: J. Mathew, H. Rahaman, A. M. Jabir +2
- **PDF**: https://ieeexplore.ieee.org/document/5450467
- **Abstract**: Recent studies have shown that an attacker can retrieve confidential information from cryptographic hardware (e.g. the secret key) by introducing internal faults. A secure and reliable implementation of cryptographic algorithms in hardware must be able to detect or correct such malicious attacks. Error detection/correction (EDC), through fault tolerance, could be an effective way to mitigate such fault attacks in cryptographic hardware. To this end, we analyze the area, delay, and power overhead for designing the S-Box, which is one of the main complex blocks in the Advanced Encryption Standard (AES), with error detection and correction capability. We use multiple Parity Predictions (PPs), based on various error correcting codes, to detect and correct errors. Various coding techniques are presented, which include simple parity prediction, split parity codes, Hamming, Hsiao, and LDPC codes. The S-Box, GF(p), and PP circuits are synthesized from the specifications, while the decoding and correction circuits are combined to form the complete designs. The analysis shows a comparison of the different approaches characterized by their error detection capability.

## Concatenated QC-LDPC and SPC codes for 100 Gbps ultra long-haul optical transmission systems

- **Status**: ❌
- **Reason**: 표준 QC-LDPC+SPC concatenation 광전송 응용 — 새 코드설계 기여 없는 표준 부호 재사용
- **ID**: ieee:5465467
- **Type**: conference
- **Published**: 21-25 Marc
- **Authors**: Norifumi Kamiya, Satomi Shioiri
- **PDF**: https://ieeexplore.ieee.org/document/5465467
- **Abstract**: We propose and investigate a novel FEC coding scheme based on a concatenation of QC-LDPC with single-parity-check codes. High performance of a Q-limit of 5.8 dB with 20.5% overhead has been achieved with FPGA-based simulations.

## A triple-concatenated FEC using soft-decision decoding for 100 Gb/s optical transmission

- **Status**: ❌
- **Reason**: triple-concatenated FEC 광전송 응용 — LDPC가 베이스라인, 떼어낼 신규 기법 없음
- **ID**: ieee:5465469
- **Type**: conference
- **Published**: 21-25 Marc
- **Authors**: Yoshikuni Miyata, Kenya Sugihara, Wataru Matsumoto +5
- **PDF**: https://ieeexplore.ieee.org/document/5465469
- **Abstract**: We propose a novel triple-concatenated forward error correction for 100 Gb/s transmission. Simulation shows that a net coding gain of 10.8 dB is obtained by a soft-decision LPDC code concatenated with the enhanced FEC listed in G.975.1.

## Coded polarization-multiplexed iterative polar modulation (PM-IPM) for beyond 400 Gb/s serial optical transmission

- **Status**: ❌
- **Reason**: polar modulation 광전송 coded-modulation — 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:5465277
- **Type**: conference
- **Published**: 21-25 Marc
- **Authors**: Ivan B. Djordjevic, Hussam G. Batshon, Lei Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/5465277
- **Abstract**: We propose a coded polarization-multiplexed iterative polar modulation (PM-IPM) as an enabling coded-modulation scheme for beyond 400 Gb/s serial optical transmission. We demonstrate that the proposed scheme can achieve 400 Gb/s optical transmission over 2250 km (for M = 3D16).

## Soft decision FEC for 100G transport systems

- **Status**: ❌
- **Reason**: 100G 광전송 soft-decision concatenated FEC, 응용 특이적 구현 — 떼어낼 신규 LDPC 디코더/구성 없음
- **ID**: ieee:5465466
- **Type**: conference
- **Published**: 21-25 Marc
- **Authors**: Kiyoshi Onohara, Yoshikuni Miyata, Takashi Sugihara +3
- **PDF**: https://ieeexplore.ieee.org/document/5465466
- **Abstract**: A practical implementation of soft decision based FEC for 100 G transport systems is discussed. The keys are a stronger coding gain using triple-concatenated FEC and a multi-lane distribution architecture to improve the error correction capability.

## Decoding complexity of irregular LDGM-LDPC codes over the BISOM channels

- **Status**: ❌
- **Reason**: LDGM-LDPC 디코딩 복잡도 이론 bound, BISOM/BEC 대상 순수 이론 분석으로 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:5464840
- **Type**: conference
- **Published**: 17-19 Marc
- **Authors**: Manik Raina, Predrag Spasojević
- **PDF**: https://ieeexplore.ieee.org/document/5464840
- **Abstract**: An irregular LDGM-LDPC code is studied as a sub-code of an LDPC code with some randomly punctured output-bits. It is shown that the LDGM-LDPC codes achieve rates arbitrarily close to the channel-capacity of the binary-input symmetric-output memoryless (BISOM) channel with bounded complexity. The measure of complexity is the average-degree (per information-bit) of the check-nodes for the factor-graph of the code. A lower-bound on the average degree of the check-nodes of the irregular LDGM-LDPC codes is obtained. The bound does not depend on the decoder used at the receiver. The stability condition for decoding the irregular LDGM-LDPC codes over the binary-erasure channel (BEC) under iterative-decoding with message-passing is described.

## Estimation with random linear mixing, belief propagation and compressed sensing

- **Status**: ❌
- **Reason**: relaxed BP 압축센싱·랜덤벡터 추정 일반화, 채널 ECC 디코더 아님(추정/CS), 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5464768
- **Type**: conference
- **Published**: 17-19 Marc
- **Authors**: Sundeep Rangan
- **PDF**: https://ieeexplore.ieee.org/document/5464768
- **Abstract**: We apply Guo and Wang's relaxed belief propagation (BP) method to the estimation of a random vector from linear measurements followed by a componentwise probabilistic measurement channel. The relaxed BP method is a Gaussian approximation of standard BP that offers significant computational savings for dense measurement matrices. The main contribution of this paper is to extend Guo and Wang's relaxed BP method and analysis to general (non-AWGN) output channels. Specifically, we present detailed equations for implementing relaxed BP for general channels and show that the relaxed BP has an identical asymptotic large sparse limit behavior as standard BP as predicted by the Guo and Wang's state evolution (SE) equations. Applications are presented to compressed sensing and estimation with bounded noise.

## Partial-parallel decoder architecture for quasi-cyclic non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC over GF(2^5)) 디코더 아키텍처 — 비이진 LDPC 제외 규칙
- **ID**: ieee:5495502
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: Xinmiao Zhang, Fang Cai
- **PDF**: https://ieeexplore.ieee.org/document/5495502
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes can achieve better error-correcting performance than binary LDPC codes when the code length is moderate. For the first time, this paper proposes a partial-parallel decoder architecture based on the Min-max algorithm for quasi-cyclic NB-LDPC codes. A novel boundary tracking based scheme and corresponding architecture are developed to implement the elementary step of the check node processing. In addition, layered decoding is applied, and the hardware units are optimized to reduce the latency and area. This paper also introduces an overlapped method for the check node processing among different layers to further speed up the decoding. From complexity analysis, the proposed decoder with 5 iterations for a (837,726) code over GF(25) can easily achieve 60 Mbps throughput on ASIC devices. It is 40% more efficient than prior designs.

## Structured dirty-paper coding using low-density lattices

- **Status**: ❌
- **Reason**: 비이진 LDPC 기반 lattice dirty-paper coding; 비이진+소스/방송채널 응용 제외
- **ID**: ieee:5496012
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: Sang Hyun Lee, Ankit Ghiya, Sriram Vishwanath +2
- **PDF**: https://ieeexplore.ieee.org/document/5496012
- **Abstract**: This paper studies dirty-paper coding in a Gaussian broadcast channel with two receivers. It finds that an approximate version of dirty-paper coding using low-density lattices can be implemented with a complexity that is polynomial-time on average in the block length. The main difference between this paper and prior work is that a non-binary LDPC-based lattice codebook is used for each user, and one codebook is aligned with the other. The low-density nature enables tractable encoding and decoding algorithms, and the alignment gives structure to the overall signal transmitted and it enables us to perform the encoding and decoding efficiently.1

## Adaptive nonasymmetric Slepian-Wolf decoding using particle filtering based belief propagation

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산 소스코딩(압축) particle filtering BP; 소스코딩이라 채널 ECC 아님
- **ID**: ieee:5495996
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: Samuel Cheng, Shuang Wang, Lijuan Cui
- **PDF**: https://ieeexplore.ieee.org/document/5495996
- **Abstract**: A major difficulty that plagues the practical use of Slepian-Wolf coding (and distributed source coding in general) is that the precise correlation among sources need to be known a priori. To resolve this problem, we have proposed an adaptive asymmetric Slepian-Wolf decoding scheme using particle filtering based belief propagation in our recent work. In this paper, we extend the adaptive scheme to the non-asymmetric setup based on the code partitioning approach. We show through experiments that the proposed algorithm can simultaneously reconstruct the compressed sources and estimate the joint correlation among sources. Further, comparing to the conventional Slepian-Wolf decoder based on standard belief propagation, the proposed approach can achieve higher compression under varying correlation statistics.

## Low density frames for compressive sensing

- **Status**: ❌
- **Reason**: compressive sensing 희소 신호 복원(소스 코딩/신호처리); 채널 ECC LDPC 아님
- **ID**: ieee:5495898
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: Mehmet Akçakaya, Jinsoo Park, Vahid Tarokh
- **PDF**: https://ieeexplore.ieee.org/document/5495898
- **Abstract**: We consider the compressive sensing of a sparse or compressible signal x ∈ ℝM. We explicitly construct a class of measurement matrices, referred to as the low density frames, and develop decoding algorithms that produce an accurate estimate x even in the presence of additive noise. Low density frames are sparse matrices and have small storage requirements. Our decoding algorithms for these frames can be implemented in O(Mdvdc) complexity, where dc and dv are the row and column weight of the frame respectively. Simulation results are provided, demonstrating that our approach significantly outperforms state-of-the-art recovery algorithms for numerous cases of interest.

## Privacy and security of features extracted from minutiae aggregates

- **Status**: ❌
- **Reason**: 지문 생체인증 보안(syndrome 저장); 보안/template 응용으로 채널 ECC 아님, 신규 LDPC 기법 없음
- **ID**: ieee:5495392
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: Abhishek Nagar, Shantanu Rane, Anthony Vetro
- **PDF**: https://ieeexplore.ieee.org/document/5495392
- **Abstract**: This paper describes our recent analysis on the security and privacy of biometric feature vectors obtained from fingerprint minutiae. A large number of contiguous regions (cuboids) are selected at random in the minutiae space, and several new features are extracted from the minutiae inside each such cuboid. Specifically, the features are extracted from the average minutia coordinate within a cuboid, the standard deviation of the minutiae coordinates, and the aggregate wall distance, i.e., the sum of distance of each minutia from the boundary of the cuboids. In terms of matching performance on a public database, the feature vectors provide an equal error rate of 3 % even if the imposter is allowed to use the same local patches as the genuine user. Performance within a secure biometrics framework is evaluated by applying an LDPC code to the feature vectors and storing only the syndrome at the access control device, for use in authentication. The paper concludes with a discussion on methods to analyze security and privacy of biometric systems that use such local-aggregate-based feature vectors in a secure biometric recognition framework. This discussion highlights security attacks via template injection, spoofing, and cancelability compromises and also considers the difficulty of privacy attacks via template inversion.
