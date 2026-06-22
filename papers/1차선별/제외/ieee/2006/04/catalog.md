# IEEE Xplore — 2006-04


## LDPC-coded MIMO systems with unknown block fading channels: soft MIMO detector design, channel estimation, and code optimization

- **Status**: ❌
- **Reason**: MIMO 무선 응용 특이적 soft detector/채널추정 설계, 떼어낼 바이너리 LDPC ECC 기법 없음(코드 degree profile 최적화는 표준 EXIT 수준)
- **ID**: ieee:1608563
- **Type**: journal
- **Published**: April 2006
- **Authors**: Jun Zheng, B.D. Rao
- **PDF**: https://ieeexplore.ieee.org/document/1608563
- **Abstract**: This paper considers the design of a practical low-density parity check (LDPC)-coded multiple-input multiple-output (MIMO) system composed of M transmit and N receive antennas operating in a flat-fading environment where channel state information (CSI) is assumed to be unavailable both to the transmitter and the receiver. A soft iterative receiver structure is developed, which consists of three main blocks: a soft MIMO detector and two LDPC component soft decoders. We first propose at the component level several soft-input soft-output MIMO detectors whose performances are much better than the conventional minimal mean square error (MMSE)-based detectors. In particular, one optimal soft MIMO detector and two simplified suboptimal detectors are developed that do not require an explicit channel estimate and offer an effective tradeoff between complexity and performance. In addition, a modified expectation maximization (EM)-based MIMO detector is developed that completely removes positive feedback between input and output extrinsic information and provides much better performance compared with the direct EM-based detector that has strong correlations especially in fast-fading channels. At the structural level, the LDPC-coded MIMO receiver is constructed in an unconventional manner where the soft MIMO detector and LDPC variable node decoder form one super soft-decoding unit, and the LDPC check node decoder forms the other component of the iterative decoding scheme. By exploiting the proposed receiver structure, tractable extrinsic information transfer functions of the component soft decoders are obtained, which further lead to a simple and efficient LDPC code degree profile optimization algorithm with proven global optimality and guaranteed convergence from any initialization. Finally, numerical and simulation results are provided to confirm the advantages of the proposed design approach for the coded MIMO system.

## LDPC-based channel coding of correlated sources with iterative joint decoding

- **Status**: ❌
- **Reason**: 상관 소스의 LDPC 결합 채널디코딩(분산 소스코딩/JSCC 성격), 표준 sum-product 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:1621157
- **Type**: journal
- **Published**: April 2006
- **Authors**: F. Daneshgaran, M. Laddomada, M. Mondin
- **PDF**: https://ieeexplore.ieee.org/document/1621157
- **Abstract**: This letter considers low-density parity-check (LDPC) coding of correlated binary sources and a novel iterative joint channel decoding without communication of any side information. We demonstrate that depending on the extent of the source correlation, additional coding gains can be obtained. Two stages of iterative decoding are employed. During global iterations, updated estimates of the source correlation are obtained and passed on to the sum-product decoder that performs local iterations with a predefined stopping criterion and/or a maximum number of local decoding iterations. Simulation results indicate that very few global iterations (2-5) are sufficient to reap significant benefits from implicit knowledge of source correlation. Finally, we provide analytical performance bounds for our iterative joint decoder and comparisons with sample simulation results.

## Concatenated zigzag hadamard codes

- **Status**: ❌
- **Reason**: zigzag Hadamard 연접부호(비-LDPC), FHT/EXIT 분석 — 바이너리 LDPC BP로 이식할 기법 없음
- **ID**: ieee:1614097
- **Type**: journal
- **Published**: April 2006
- **Authors**: W.K.R. Leung, Guosen Yue, Li Ping +1
- **PDF**: https://ieeexplore.ieee.org/document/1614097
- **Abstract**: In this correspondence, we introduce a new class of low-rate error correction codes called zigzag Hadamard (ZH) codes and their concatenation schemes. Each member of this class of codes is specified by a highly structured zigzag graph with each segment being a Hadamard codeword. The ZH codes enjoy extremely simple encoding and very low-complexity soft-input-soft-output (SISO) decoding based on a posteriori probability (APP) fast Hadamard transform (FHT) technique. We present an asymptotic performance analysis of the proposed concatenated ZH codes using the extrinsic mutual information transfer (EXIT) chart for infinite-length codes. We also provide a union bound analysis of the error performance for finite-length codes. Furthermore, the concatenated ZH codes are shown to be a good class of codes in the low-rate region. Specifically, a rate-0.0107 concatenated code with three ZH components and an interleaver size of 65536 can achieve the bit error rate (BER) performance of 10/sup -5/ at -1.15dB, which is only 0.44 dB away from the ultimate Shannon limit. The proposed concatenated ZH codes offer similar performance as another class of low-rate codes-the turbo-Hadamard codes, and better performance than superorthogonal turbo codes, with much lower encoding and decoding complexities.

## Concatenated LDGM codes with single decoder

- **Status**: ❌
- **Reason**: LDGM(생성행렬) 직렬연접 코드 설계 — NAND 바이너리 LDPC ECC로 이식할 신규 디코더/구성 없음
- **ID**: ieee:1613749
- **Type**: journal
- **Published**: April 2006
- **Authors**: Joon-Sung Kim, Hong-Yeop Song
- **PDF**: https://ieeexplore.ieee.org/document/1613749
- **Abstract**: We propose a design criterion for serially concatenated LDGM codes which require a single decoder and a bit-interleaver. The inner LDGM code can be obtained by expanding the rows of the parity check matrix of the outer LDGM code. The resulting codes can be decoded using only the inner LDGM decoder with slight modification. Simulation results show that the performance of the proposed codes is almost the same as that of serially concatenated LDGM code's using both the inner and the outer decoders.

## On code design for the Slepian-Wolf problem and lossless multiterminal networks

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스코딩(분산 압축), IRA/turbo 사용 — 채널 ECC 아님
- **ID**: ieee:1614079
- **Type**: journal
- **Published**: April 2006
- **Authors**: V. Stankovic, A.D. Liveris, Zixiang Xiong +1
- **PDF**: https://ieeexplore.ieee.org/document/1614079
- **Abstract**: A Slepian-Wolf coding scheme for compressing two uniform memoryless binary sources using a single channel code that can achieve arbitrary rate allocation among encoders was outlined in the work of Pradhan and Ramchandran. Inspired by this work, we address the problem of practical code design for general multiterminal lossless networks where multiple memoryless correlated binary sources are separately compressed and sent; each decoder receives a set of compressed sources and attempts to jointly reconstruct them. First, we propose a near-lossless practical code design for the Slepian-Wolf system with multiple sources. For two uniform sources, if the code approaches the capacity of the channel that models the correlation between the sources, then the system will approach the theoretical limit. Thus, the great advantage of this design method is its possibility to approach the theoretical limits with a single channel code for any rate allocation among the encoders. Based on Slepian-Wolf code constructions, we continue with providing practical designs for the general lossless multiterminal network which consists of an arbitrary number of encoders and decoders. Using irregular repeat-accumulate and turbo codes in our designs, we obtain the best results reported so far and almost reach the theoretical bounds.

## Nonlinear dynamics of iterative decoding systems: analysis and applications

- **Status**: ❌
- **Reason**: 반복디코딩의 비선형 동역학 분석+turbo 정지조건 — 주로 turbo 대상, 떼어낼 LDPC BP 기법 없는 이론/응용
- **ID**: ieee:1614071
- **Type**: journal
- **Published**: April 2006
- **Authors**: L. Kocarev, F. Lehmann, G.M. Maggio +3
- **PDF**: https://ieeexplore.ieee.org/document/1614071
- **Abstract**: Iterative decoding algorithms may be viewed as high-dimensional nonlinear dynamical systems, depending on a large number of parameters. In this work, we introduce a simplified description of several iterative decoding algorithms in terms of the a posteriori average entropy, and study them as a function of a single parameter that closely approximates the signal-to-noise ratio (SNR). Using this approach, we show that virtually all the iterative decoding schemes in use today exhibit similar qualitative dynamics. In particular, a whole range of phenomena known to occur in nonlinear systems, such as existence of multiple fixed points, oscillatory behavior, bifurcations, chaos, and transient chaos are found in iterative decoding algorithms. As an application, we develop an adaptive technique to control transient chaos in the turbo-decoding algorithm, leading to a substantial improvement in performance. We also propose a new stopping criterion for turbo codes that achieves the same performance with considerably fewer iterations.

## A cross-layer TCP modelling framework for MIMO wireless systems

- **Status**: ❌
- **Reason**: MIMO 무선 TCP 크로스레이어 모델링, LDPC 무관 (채널코딩은 부수 언급)
- **ID**: ieee:1618941
- **Type**: journal
- **Published**: April 2006
- **Authors**: A.L. Toledo, Xiaodong Wang, B. Lu
- **PDF**: https://ieeexplore.ieee.org/document/1618941
- **Abstract**: We propose a general framework based in the Gilbert model for cross-layer analysis of TCP and UDP over MIMO wireless systems. Our framework takes into consideration diverse system characteristics often difficult to express as a Gilbert model such as fading, space-time transmission schemes, modulation, channel coding and ARQ. We apply our framework to analyze the TCP performance of two representative MIMO systems, namely, the BLAST system and the orthogonal space-time block coded (STBC) system. In particular, we investigate the optimal information rate that maximizes the TCP throughput, the effect of Doppler on the optimal TCP throughput and the optimal channel coding rate for various modulations. We provide simulations results from the ns-2 network simulator to demonstrate the accuracy of the proposed analytical framework in characterizing the TCP performance. We further apply the framework to two additional cross-layer applications: the analysis of the buffer occupancy on the base station, and the analysis of CBR video transmission over MIMO systems. We show that while the optimal rate for maximum TCP throughput is far from the channel capacity, the optimal rate for error and delay-tolerant video transmission requires much higher rates, and so the physical layer should be aware and adapt to the type of application in order to increase the system performance. We also show that mobility benefits systems with larger buffers, especially for TCP, as the ARQ scheme is able to recover the shorter burst errors. In general, our investigation shows that the type of application plays a crucial role in the optimization of a wireless system, and that our modelling framework is useful for the cross-layer analysis and design of those systems.

## Simplified eIRA code design and performance analysis for correlated Rayleigh fading channels

- **Status**: ❌
- **Reason**: eIRA(반복누적) 코드 설계로 비-LDPC 부호이며 Rayleigh fading 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1618918
- **Type**: journal
- **Published**: April 2006
- **Authors**: Fei Peng, M. Yang, W.E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1618918
- **Abstract**: We present a simple design technique for extended irregular repeat-accumulate (eIRA) codes for flat Rayleigh fading channels, using simple channels as surrogates in the design. We show that eIRA codes designed for the burst-erasure channel (BuEC) or the burst-erasure channel with AWGN (BuEC-G) achieve essentially the same performance over Rayleigh fading channels as codes designed for the fading channel. Thus, to design good codes for Rayleigh fading channels, instead of implementing the complex design procedures targeted, specifically for this channel, we propose the simple approach of designing codes over surrogate channels, the BuEC or the BuEC-G. We also show that eIRA codes designed for the BuEC enjoy the advantage of efficient encodability and a lower error-rate floor. Finally, we demonstrate that it is the distribution of the number of faded bits per codeword which determines the difference between correlated and uncorrelated fading channel performance. Perfect channel state information is assumed in this paper.

## Reliable channel regions for good binary codes transmitted over parallel channels

- **Status**: ❌
- **Reason**: 병렬채널 ML 디코딩 Gallager bound 순수 이론 — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1614074
- **Type**: journal
- **Published**: April 2006
- **Authors**: Ruoheng Liu, P. Spasojevic, E. Soljanin
- **PDF**: https://ieeexplore.ieee.org/document/1614074
- **Abstract**: We study the average error probability performance of binary linear code ensembles when each codeword is divided into J subcodewords with each being transmitted over one of J parallel channels. This model is widely accepted for a number of important practical channels and signaling schemes including block-fading channels, incremental redundancy retransmission schemes, and multicarrier communication techniques for frequency-selective channels. Our focus is on ensembles of good codes whose performance in a single channel model is characterized by a threshold behavior, e.g., turbo and low-density parity-check (LDPC) codes. For a given good code ensemble, we investigate reliable channel regions which ensure reliable communications over parallel channels under maximum-likelihood (ML) decoding. To construct reliable regions, we study a modifed 1961 Gallager bound for parallel channels. By allowing codeword bits to be randomly assigned to each component channel, the average parallel-channel Gallager bound is simplified to be a function of code weight enumerators and channel assignment rates. Special cases of this bound, average union-Bhattacharyya (UB), Shulman-Feder (SF), simplified-sphere (SS), and modified Shulman-Feder (MSF) parallel-channel bounds, allow for describing reliable channel regions using simple functions of channel and code spectrum parameters. Parameters describing the channel are the average parallel-channel Bhattacharyya noise parameter, the average channel mutual information, and parallel Gaussian channel signal-to-noise ratios (SNRs). Code parameters include the union-Bhattacharyya noise threshold and the weight spectrum distance to the random binary code ensemble. Reliable channel regions of repeat-accumulate (RA) codes for parallel binary erasure channels (BECs) and of turbo codes for parallel additive white Gaussian noise (AWGN) channels are numerically computed and compared with simulation results based on iterative decoding. In addition, an examp

## Use of 2.4 GHz frequency band for Communications Based Train Control data communications systems

- **Status**: ❌
- **Reason**: CBTC 2.4GHz 무선 통신 대역 사용 논의, LDPC 무관
- **ID**: ieee:1634082
- **Type**: conference
- **Published**: 4-6 April 
- **Authors**: M. Fitzmaurice
- **PDF**: https://ieeexplore.ieee.org/document/1634082
- **Abstract**: The increasing deployment of CBTC by public transit agencies that use a data communications systems based in the 2.4 GHz ISM band has raised the concern of RF interference between CBTC equipped trains and the variety of new and existing users of this band. The vast number of RF devices that currently operate in this band (like microwave ovens, cordless telephones, medical devices etc.) have recently been augmented by the proliferation of "Wi-Fi" hotspots and wireless computers permitting untethered Internet access by the public and RF identification (RFID) technology. While the popularity of the band is a source of concern, paradoxically, this same popularity yields many advantages and benefits to CBTC systems that use it. Often the fact that a frequency band is "crowded" or heavily used (however that is defined) immediately precludes its use for those systems or services that consider themselves to be mission critical. While avoiding a heavily used frequency band for an important application is a prudent course of action, it might not be possible or, upon closer examination, even necessary. There might not be any other spectrum available or, if there is, the cost and technical risk of obtaining regulatory approval or developing the unique radio equipment could prove prohibitive. Additionally, technical advances in radio equipment and signal processing might completely obviate any perceived interference

## Average Coset Weight Distribution of Multi-Edge type LDPC Code Ensembles

- **Status**: ❌
- **Reason**: MET-LDPC 앙상블 평균 coset 무게분포 순수 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5755947
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Kenta Kasai, Yuji Shimoyama, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/5755947
- **Abstract**: Multi-Edge type Low-Density Parity-Check codes (MET-LDPC codes) introduced by Richardson and Urbanke are generalized LDPC codes which can be seen as LDPC codes obtained by concatenating some standard (ir)regular LDPC codes. We prove in this paper that MET-LDPC code ensembles possess a certain symmetry with respect to their Average Coset Weight Distributions (ACWD). Using the symmetry, we drive ACWD of MET-LDPC code ensembles from ACWD of their constituent ensembles.

## On Belief Propagation Decoding of LDPC Codes over Groups

- **Status**: ❌
- **Reason**: 유한체/링/군 위의 LDPC(비이진 일반화) BP 디코딩, 바이너리 LDPC 범위 밖
- **ID**: ieee:5755848
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Alban Goupil, Maxime Colas, Guillaume Gelle +1
- **PDF**: https://ieeexplore.ieee.org/document/5755848
- **Abstract**: We introduce a wide class of LDPC codes, large enough to include LDPC codes over finite fields, rings or groups as well as some non-linear codes. This class is defined by an extension of the parity-check equations involved in the code's definition. A belief propagation decoding procedure with the same complexity as for the decoding of LDPC codes over finite fields is presented for theses new parities. Examples are given that illustrate the interest of this new code family.

## Construction of Parity-Check Matrices for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 패리티검사 행렬 구성 — 비이진 LDPC 제외
- **ID**: ieee:5755835
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Dai Kimura, Frederic Guilloud, Ramesh Pyndiah
- **PDF**: https://ieeexplore.ieee.org/document/5755835
- **Abstract**: This paper presents a novel construction method for parity-check matrices of non-binary LDPC codes which selects nearly optimum non-zero elements in the parity-check matrices. The proposed method can improve the codeweight distribution of non-binary LDPC codes of column weight 2. The decoding performance of the non-binary LDPC codes using the parity-check matrices constructed by the proposed method can outperform that of the random method significantly.

## GF(2m) Low-Density Parity-Check Codes Derived from Cyclotomic Cosets

- **Status**: ❌
- **Reason**: GF(2^m) 비이진 LDPC 구성 - 비이진 제외 대상
- **ID**: ieee:5755905
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: C. Tjhai, M. Tomlinson, R. Horan +2
- **PDF**: https://ieeexplore.ieee.org/document/5755905
- **Abstract**: Based on the ideas of cyclotomic cosets, idempotents and Mattson-Solomon polynomials, we present a new method to construct GF(2m), where m > 0, cyclic low-density parity-check codes. The construction method produces the dual code idempotent which is used to define the parity-check matrix of the low-density parity-check code. An interesting feature of this construction method is the ability to increment the code dimension by adding more idempotents and so steadily decrease the sparseness of the parity-check matrix. We show that the constructed codes can achieve performance close to the sphere-packing-bound constrained for binary transmission.

## High Rate Non-Systematic LDPC Codes for Nonuniform Sources

- **Status**: ❌
- **Reason**: 비균일 소스 대상 비조직 LDPC, 소스 리던던시 활용이라 채널 ECC 기법 아님
- **ID**: ieee:5755948
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Gil I. Shamir, Li Wang, Joseph J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/5755948
- **Abstract**: Non-systematic channel encoding is superior to systematic encoding in the presence of source redundancy.We show analytically that for high rate codes the advantage of non-systematic encoding over systematic encoding becomes even more significant. We then consider classes of non-systematic low-density parity-check (LDPC) codes based on scrambling or splitting redundant data bits into coded bits. Scrambling and splitting are achieved by cascading a sparse matrix or an inverse of a sparse matrix, respectively, with an LDPC code. Such codes exhibit excellent performance in the presence of source redundancy, which is far superior to that of systematic LDPC codes. The advantage of such codes is even more significant for high rate coding. Simulation results demonstrate this advantage.

## Performance Analysis of BP Decoding for LDPC Codes Using the EXIT Equations

- **Status**: ❌
- **Reason**: EXIT 방정식 기반 BP 수렴 임계값 분석 방법 — 성능분석 도구일 뿐 떼어낼 디코더/구성/HW 기여 없음
- **ID**: ieee:5755870
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: He Zheng, Hanying Hu
- **PDF**: https://ieeexplore.ieee.org/document/5755870
- **Abstract**: By using the equations derived from extrinsic information transfer (EXIT) functions, we propose a new performanceanalysis method for belief propagation (BP) decoding of regular and irregular low-density parity-check (LDPC) codes. By means of the derived so-called EXIT equations, the problem of finding the convergence threshold for a given regular or irregular LDPC code can be described as a minimizing optimization. On the additive white Gaussian noise (AWGN) channel, the achieved convergence threshold values by our proposed optimization for the enumerated regular and irregular codes have error to those from density evolution about 0.01dB and 0.05dB, respectively. Furthermore, the proposed method in contrast with density evolution is more convenient since no iterations and no computations for Fourier and inverse Fourier transforms are required during the performance analysis.

## Upper Bounds of Block Error Probability of Standard Irregular LDPC Code Ensemble under Maximum Likelihood Decoding

- **Status**: ❌
- **Reason**: irregular LDPC ensemble의 ML 디코딩하 블록오류 상한 유도 — 순수 이론 bound, 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:5755869
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Ryoji Ikegaya, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://ieeexplore.ieee.org/document/5755869
- **Abstract**: In this paper, we derive the upper bound of the average block error probability of a given standard irregular LDPC code ensemble under the maximum likelihood decoding. Our results are the forms including the case of regular LDPC code ensembles.

## An intuitive way to calculate a lower bound on a convergence threshold for LDPC codes

- **Status**: ❌
- **Reason**: EXIT 차트 기반 수렴 임계값 하한 계산 방법론, 순수 이론 분석으로 디코더/HW/구성 비연결
- **ID**: ieee:5755904
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Thorsten Hehn, Andac Doenmez, Johannes B. Huber
- **PDF**: https://ieeexplore.ieee.org/document/5755904
- **Abstract**: Belief-propagation decoding for low-density parity-check (LDPC) codes only performs well if the decoder does not get stuck during information exchange between variable and check nodes, i.e. performs above a certain threshold. As the binary erasure channel and the binary symmetric channel are both the least and most informative channels from information combining point of view (depending on the type of nodes being considered (variable- or check-)), one can calculate upper and lower bounds on the required mutual information that has to be sent over the channel for successful iterative decoding. In this paper we present an additional easily understandable methodology for calculation of the lower bound for the required mutual information. Our method is intuitive as its approach is based on EXIT charts.

## On the Application of Error-Correcting Codes with Low-Density Generator Matrix over Different Quantum Channels

- **Status**: ❌
- **Reason**: LDGM 기반 CSS 양자코드, 양자채널 EC라 원칙 제외(스태빌라이저/양자율 의존)
- **ID**: ieee:5755950
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Hanqing Lou, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/5755950
- **Abstract**: We propose the use of linear codes with low-density generator matrix in the context of error correction over different quantum channels. The basic idea is to construct a Calderbank-Shor-Steane (CSS) code based on the generator matrix and the parity-check matrix of an LDGM code, applying row operations in both matrices to achieve the desired quantum rate. Decoding is performed in an iterative manner, using message passing over the corresponding graphs. The proposed codes allow greater flexibility and are easier to design than existing sparse-graph quantum codes, while leading to better performance.

## Performance versus Complexity Per Iteration for Low-Density Parity-Check Codes: An Information-Theoretic Approach

- **Status**: ❌
- **Reason**: 성능-복잡도 트레이드오프의 정보이론적 bound 분석, 떼어낼 디코더/HW/구성 기법 없는 순수 이론
- **ID**: ieee:5755847
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Igal Sason, Gil Wiechman
- **PDF**: https://ieeexplore.ieee.org/document/5755847
- **Abstract**: The paper is focused on the tradeoff between performance and decoding complexity per iteration for LDPC codes in terms of their gap (in rate) to capacity. The study of this tradeoff is done via information-theoretic bounds which also enable to get an indication on the sub-optimality of message-passing iterative decoding algorithms (as compared to optimal ML decoding). The bounds are generalized for parallel channels, and are applied to ensembles of punctured LDPC codes where both intentional and random puncturing are addressed. This work suggests an improvement in the tightness of some information-theoretic bounds which were previously derived by Burshtein et al. and by Sason and Urbanke.

## Iterative Multiuser Detection of Random CDMA Using Partitioned Spreading

- **Status**: ❌
- **Reason**: random CDMA partitioned spreading 다중사용자 검출에 LDPC 활용 — 무선/다중접속 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:5755891
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Christian Schlegel, Dmitri Truhachev, Lukasz Krzymien
- **PDF**: https://ieeexplore.ieee.org/document/5755891
- **Abstract**: Iterative joint detection of random CDMA is considered in conjunction with error control coding, in particular using low-density parity-check (LDPC) codes. The spreading sequences are partitioned into sections, called "partitioned spreading (PS)", creating an artificial repetition code which interfaces the LDPC code with the multiple access channel. A suboptimal, but efficient cancelation processor is used at the multiple access processing node in the factor graph describing the overall system. This system is then analyzed using Gaussian density evolution and it is shown that partitioned spreading conditions the channels such that the efficiency of the code is increased substantially. A comparison between direct application of LDPC coding (without partition spreading) to a two-stage decoding procedure and a full iterative decoding schedule of PS-CDMA reveals that gains of over 100% in spectral efficiencies can be achieved with regular LDPC codes.

## Comparison of High-Performance Codes on AWGN Channel with Erasures

- **Status**: ❌
- **Reason**: 표준 DVB-S2 LDPC/turbo 성능 비교 위주, PEG 개선은 위성 erasure 채널 특화 코드 설계로 NAND 이식성 약함
- **ID**: ieee:5755813
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Andac Doenmez, Thorsten Hehn, Stefan Laendner +1
- **PDF**: https://ieeexplore.ieee.org/document/5755813
- **Abstract**: This paper provides an overview of near Shannon-limit operating codes when transmitted over the additive white Gaussian noise (AWGN) channel with erasures. We compare the performance of standardized low-density parity-check (LDPC) codes and parallel-concatenated (turbo) codes to two progressive edge growth (PEG) optimized codes and a new design. The assumed channel, an AWGN channel with erasures, plays an important role in the field of satellite communications. The standardized codes we chose for our comparison purposes are the DVB-S2 LDPC code and a previously designed turbo code of 3GPP2. Furthermore, we use the PEG algorithm, which is improved by a novel method, to design better LDPC codes for this channel.

## On Parity-Check Matrices with Optimal Stopping and/or Dead- End Set Enumerators

- **Status**: ❌
- **Reason**: erasure 반복디코딩의 stopping/dead-end set 열거자 bound 순수 이론, 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:5755902
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Khaled A. S. Abdel-Ghaffar, Jos H. Weber
- **PDF**: https://ieeexplore.ieee.org/document/5755902
- **Abstract**: The performance of iterative decoding techniques for linear block codes correcting erasures depends very much on the sizes of the stopping sets associated with the underlying Tanner graph, or, equivalently, the parity-check matrix representing the code. In this paper, we introduce the notion of dead-end sets to explicitly demonstrate this dependency. The choice of the parity-check matrix entails a trade-off between performance and complexity. We give bounds on the complexity of iterative decoders achieving optimal performance in terms of the sizes of the underlying parity-check matrices. Further, we fully characterize codes for which the optimal stopping set enumerator equals the weight enumerator.

## Joint design of code, constellation and power allocation in BICM LDPC coded systems

- **Status**: ❌
- **Reason**: BICM LDPC 변조/전력할당 결합설계, 무선 응용 특이적이고 떼어낼 디코더/구성 ECC 기법 없음
- **ID**: ieee:5755922
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Oscar Lahuerta, Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/5755922
- **Abstract**: The performance of a system using low density parity check (LDPC) codes depends on the proper matching of several parameters: degree profile of the code, constellation size and constellation labelling and the power allocated to each transmitted symbol. In this paper we propose a unified formulation for the optimisation of all these parameters, so that some or all of them can be jointly designed to maximise the spectral efficiency for a certain transmitted power or to minimise the transmitted power that guarantees a certain spectral efficiency. The proposed algorithm is based on the EXIT chart analysis of the LDPC code and it can be applied to two different set ups: (I) scenarios where the transmitter has perfect channel knowledge, so the proposed algorithm can be regarded as an extension of waterfilling and bit-loading policies that takes into account the specific channel code stage, and to (II) scenarios where the transmitter only knows the average channel quality, so the proposed algorithm can be regarded as a generalisation of the previously proposed irregular codes and irregular modulation schemes. Besides, it can be applied to the optimisation of BICM and BICM-ID.

## On the Connection Between Finite Graph Covers, Pseudo-Codewords, and Linear Programming Decoding of Turbo Codes

- **Status**: ❌
- **Reason**: turbo 부호의 LP 디코딩·pseudo-codeword 순수 이론, 떼어낼 LDPC 디코더/HW 기법 없음
- **ID**: ieee:5755823
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/5755823
- **Abstract**: The performance of turbo decoding on the binary erasure channel (BEC) can be characterized in terms of turbo stopping sets. Apply turbo decoding until the transmitted codeword has been recovered, or the decoder fails to progress further. Then the set of erased positions that will remain when the decoder stops is equal to the unique maximum-size turbo stopping set which is also a subset of the set of erased positions. The concept of turbo stopping sets is an adaptation of stopping sets from the theory of iterative belief-propagation (BP) decoding of low-density parity-check (LDPC) codes. In this work we consider relaxed linear programming (LP) decoding of turbo codes as described by Feldman in his thesis. We show that the set of points from the relaxed polytope where all entries are rational numbers is equal to the set of all pseudo-codewords of all unite graph covers of the turbo code factor graph. We also show that there is a many-to-one correspondence between pseudo-codewords and turbo stopping sets in the following sense. The support set of any pseudo-codeword, i.e., the set of non-zero coordinates, is a turbo stopping set, and for any turbo stopping set there is a pseudo-codeword with support set equal to the turbo stopping set. Furthermore, the minimum additive white Gaussian noise (AWGN) pseudo-weight of pseudo-codewords with support set equal to a minimal type-1 turbo stopping set is equal to its support set size. Finally, we present some simulation results showing the infuence of small-size turbo stopping sets on turbo decoding on the AWGN channel.

## A Geometric Description of the Iterative Least-Squares Decoding of Analog Block Codes

- **Status**: ❌
- **Reason**: 복소/실수상 아날로그 블록코드의 반복 least-squares 복호 — 바이너리 LDPC 아님, 떼어낼 BP 이식 기법 불명확
- **ID**: ieee:5755874
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Fangning Hu, Werner Henkel
- **PDF**: https://ieeexplore.ieee.org/document/5755874
- **Abstract**: This paper outlines that when decoding an arbitrary analog block codes, i.e., a block codes over the complex or real numbers, in an iterative fashion by splitting the H-Matrix in two, leads to a least-squares estimate. Such a Turbo-like algorithm represents iterative projections in Euclidean space. A step size controls the convergence speed. The paper generalized an earlier result based on array codes (product codes) with analog parity-check component codes. The results in here are considered to be an important step towards an intuitive understanding of iterative decoding schemes of conventional Turbo and LDPC codes.

## Maximum a Posteriori Decoding System Using an ARMA Process for a Partial Response Channel with Burst Errors

- **Status**: ❌
- **Reason**: 수직자기기록 채널의 ARMA 기반 MAP 채널복호(버스트오류) — 채널추정/검출 기법, LDPC는 베이스라인, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:5755896
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Hidetoshi Saito, Ryuji Kohno
- **PDF**: https://ieeexplore.ieee.org/document/5755896
- **Abstract**: One of new idea of maximum a posteriori (MAP) decoding with an autoregressive and moving-average (ARMA) process is introduced into the iterative (recursive) decoding processes between MAP decoding and turbo or sum-product decoding in a perpendicular magnetic recording channel. In this paper, MAP decoding with linear prediction is called MAP-ARMA decoding. The estimation techniques based on multivariate time series analysis, stochastic models and processes are effective for burst errors or continuous erasures. It is shown that this estimation problem for missing data values (observations) is solved by maximum likelihood estimation for an ARMA process with missing values by using multivariate statistical techniques. For the given (4608,4097) low-density parity check (LDPC) coding system, the error rate performance using proposed channel predicting and MAP decoding systems in the channel with both a burst of length 70 or less and random errors attains the almost same performance of conventional MAP decoding in the channel with only random errors.

## Using binary images of non binary LDPC codes to improve overall performance

- **Status**: ❌
- **Reason**: 비이진 LDPC 최적화(바이너리 이미지 활용해도 대상이 non-binary LDPC), 비이진 제외 규칙
- **ID**: ieee:5755957
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Charly Poulliat, Marc Fossorier, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/5755957
- **Abstract**: In this paper, we address the problem of the optimization of non binary LDPC codes for finite lengths. Using the binary image of the code, we provide a method for both waterfall and error floor improvements based on the algebraic properties of rows, cycles and stopping sets.

## Analytical Bounds on Maximum-Likelihood Decoded Linear Codes with Applications to Turbo-Like Codes: An Overview

- **Status**: ❌
- **Reason**: ML 디코딩 에러확률 bound 서베이, 순수 이론으로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5755824
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Igal Sason, Shlomo Shamai
- **PDF**: https://ieeexplore.ieee.org/document/5755824
- **Abstract**: Upper and lower bounds on the error probability of linear codes under maximum-likelihood (ML) decoding are shortly surveyed and applied to ensembles of codes on graphs. For upper bounds, focus is put on Gallager bounding techniques and their relation to a variety of other reported bounds. Within the class of lower bounds, we address de Caen's based bounds and their improvements, sphere-packing bounds, and information-theoretic bounds on the bit error probability of codes defined on graphs. A comprehensive overview is provided in the monograph.

## Iterative Channel Estimation and Decoding of LDPC Coded BICM on block fading channels

- **Status**: ❌
- **Reason**: block fading 채널에서 LDPC-BICM 반복 채널추정+복호 — 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:5755873
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Chuan-gang Zhao, Jia-ru Lin, Wei-ling Wu
- **PDF**: https://ieeexplore.ieee.org/document/5755873
- **Abstract**: This paper focuses on the performance analysis of regular LDPC coded BICM for block fading channels. We propose an iterative receiver which carries out channel estimation and decoding iteratively via belief propagation algorithm over coherent and non-coherent block fading channels and derive the ML and MAP channel estimator for higher order modulations. Analysis shows that as Signal-to-Noise Ratio (SNR)or channel memory increases, MAP channel estimator becomes ML channel estimator. Simulation result verifies our analysis.

## Probabilistic Message Passing in Peer Data Management Systems

- **Status**: ❌
- **Reason**: Peer 데이터관리 매핑오류 탐지용 확률적 메시지패싱 — LDPC ECC와 무관
- **ID**: ieee:1617409
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: P. Cudre-Mauroux, K. Aberer, A. Feher
- **PDF**: https://ieeexplore.ieee.org/document/1617409
- **Abstract**: Until recently, most data integration techniques involved central components, e.g., global schemas, to enable transparent access to heterogeneous databases. Today, however, with the democratization of tools facilitating knowledge elicitation in machine-processable formats, one cannot rely on global, centralized schemas anymore as knowledge creation and consumption are getting more and more dynamic and decentralized. Peer Data Management Systems (PDMS) provide an answer to this problem by eliminating the central semantic component and considering instead compositions of local, pair-wise mappings to propagate queries from one database to the others. PDMS approaches proposed so far make the implicit assumption that all mappings used in this way are correct. This obviously cannot be taken as granted in typical PDMS settings where mappings can be created (semi) automatically by independent parties. In this work, we propose a totally decentralized, efficient message passing scheme to automatically detect erroneous mappings in PDMS. Our scheme is based on a probabilistic model where we take advantage of transitive closures of mapping operations to confront local belief on the correctness of a mapping against evidences gathered around the network. We show that our scheme can be efficiently embedded in any PDMS and provide a preliminary evaluation of our techniques on sets of both automatically-generated and real-world schemas.

## Advances in Iterative Decoding and Maximum Likelihood Decoding for the Packet Network with Comparisons to Fountain Codes over the Erasure Channel

- **Status**: ❌
- **Reason**: BEC상 BCH/순환부호 ML 디코딩+fountain 비교, erasure/패킷네트워크 응용으로 LDPC ECC 이식 기법 없음
- **ID**: ieee:5755865
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: J. Cai, M. Tomlinson, C. Tjhai +2
- **PDF**: https://ieeexplore.ieee.org/document/5755865
- **Abstract**: In this paper, we propose a novel ML decoding algorithm - the In-place Algorithm in conjunction with a Product Packetisation method for the congested Internet Network modeled as a Binary Erasure Channel (BEC). Any code can be used with this algorithm and we give results for cyclic codes constructed from BCH codes. Existing codes and decoding algorithms are compared in terms of performance and decoding complexity. It is shown that a significant performance improvement can be achieved. In general, ML decoding on the Erasure channel has a complexity of O(N3) or O(N2) depending on the algorithm. It is shown that this complexity can be reduced to O(N1:5) for the network channel by using the product packetisation method. With an analysis in performance, ratelessness can be achieved by acks.

## Design of Rate-Compatible Serially Concatenated Convolutional Codes

- **Status**: ❌
- **Reason**: 직렬연접 컨볼루션 부호(SCCC) 설계, 비-LDPC 부호이며 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:5755814
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: - Graell, - Graell, Fredrik Braennstroem +1
- **PDF**: https://ieeexplore.ieee.org/document/5755814
- **Abstract**: Recently a powerful class of rate-compatible serially concatenated convolutional codes (SCCCs) have been proposed based on minimizing analytical upper bounds on the error probability in the error floor region. Here this class of codes is further investigated by combining analytical upper bounds with extrinsic information transfer charts analysis. Following this approach, we construct a family of rate-compatible SCCCs with good performance in both the error floor and the waterfall regions over a broad range of code rates.

## Estimating the Minimum Distance of Large-Block Turbo Codes using Iterative Multiple-Impulse Methods

- **Status**: ❌
- **Reason**: 터보코드 최소거리 추정 기법, 비-LDPC이며 LDPC BP로 이식되는 디코더 기법 아님
- **ID**: ieee:5755853
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Stewart Crozier, Paul Guinand, Andrew Hunt
- **PDF**: https://ieeexplore.ieee.org/document/5755853
- **Abstract**: A difficult problem for turbo codes is the efficient and accurate determination of the distance spectrum, or even just the minimum distance, for specific interleavers. This is especially true for large blocks, with many thousands of data bits, if the distance is high. This paper compares a number of recent distance estimation techniques and introduces a new approach, based on using specific event impulse patterns and iterative processing, that is specifically tailored to handle long interleavers with high spread. The new method is as reliable as two previous iterative multiple-impulse methods, but with much lower complexity. A minimum distance of 60 has been estimated for a rate 1/3, 8-state, turbo code with a dithered relative prime (DRP) interleaver of length K=65,536.

## Unequal Energy Allocation with Turbo Codes for Nonuniform Sources

- **Status**: ❌
- **Reason**: turbo 부호의 비균등 에너지 할당, 비-LDPC이며 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:5755830
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Gil I. Shamir, Richard Demo Souza, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/5755830
- **Abstract**: Non-systematic channel codes can have a significant advantage over systematic codes when utilizing redundancy left in the data for channel decoding. However, results previously attained show that even with such codes there is a performance gap to the theoretical limits. We study techniques that allow reducing this gap by using unequal energy allocation for both systematic and non-systematic turbo codes. For both types of codes, there are regions of source non-uniformity, for which they outperform codes with equal energy allocation. Systematic codes with unequal allocation perform well at extreme non-uniformities. The non-systematic codes perform well at moderate non-uniformities and still outperform their equal energy allocation counterparts at extreme non-uniformities. A theoretical study of the mutual information attainable by the different classes of codes for different source non-uniformities is presented, and supports the advantage of non-systematic codes with unequal allocation over the other classes of codes. While it also points out that the non-systematic codes should be better for extreme source non-uniformities, simulation results show that the current designs of the systematic codes with unequal energy allocation are still better than those of the non-systematic codes in this region.

## Code-aided channel tracking for OFDM

- **Status**: ❌
- **Reason**: OFDM 채널추정 EM 수신기, LDPC 부수 언급 통신 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:5755913
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Henk Wymeersch, Frederik Simoens, Heidi Steendam +1
- **PDF**: https://ieeexplore.ieee.org/document/5755913
- **Abstract**: This contribution deals with the problem of tracking a frequency-selective channel for OFDM systems, where the data is protected by a powerful error-correcting code. We present an EM-based receiver, operating on a single OFDM symbol at a time, that iterates between channel estimation and data detection. The channel estimator accepts information from the detector in the form of a posteriori probabilities. The estimator is robust in a sense that it makes very few assumptions regarding the underlying channel model. Complexity-reducing approximations are discussed. Performance results are provided in the form of Monte Carlo simulations.

## Design and Analysis of Linear Precoders for Bit-Interleaved Coded Modulation with Iterative Decoding

- **Status**: ❌
- **Reason**: BICM-ID 선형 프리코더 설계, 변조/매핑 영역 통신 응용으로 LDPC ECC 이식 기법 없음
- **ID**: ieee:5755923
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Frederik Simoens, Henk Wymeersch, Marc Moeneclaey
- **PDF**: https://ieeexplore.ieee.org/document/5755923
- **Abstract**: In this paper, we consider linear precoders for Bit-Interleaved Coded Modulation with iterative decoding (BICM-ID) on AWGN channels. In a BICM-ID set-up, the encoder and symbol mapper are separated by an interleaver in order to achieve better performance and to allow a simplified (yet sub-optimal) decoding strategy. However, careful design of the symbol mapper is imperative in order to achieve a satisfactory performance. An alternative solution to the design of the (multi-dimensional) mapper is rendered by inserting a precoder before the symbol mapper. A precoder allows for more flexibility and its design is often less involved than the design of a symbol mapper. Based upon a pairwise error probability (PEP) argument, we derive fairly simple design criteria from which we can easily obtain optimal precoders. Simulation results back our analytical findings.

## Turbo TCM Coded OFDM System for Powerline Channel

- **Status**: ❌
- **Reason**: Turbo TCM + 단순 패리티검사 OFDM 전력선 통신, LDPC 아님, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:5755924
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Yanxia Wang, Libo Yang, Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/5755924
- **Abstract**: In this paper we examine the possibility of improving the OFDM modulated HomePlug networks using Turbo TCM with 64QAM constellation for higher data rate transmission. We simplify the standard Turbo TCM into a punctured parity-concatenated trellis code in which a TCM code is used as the inner code and a simple parity-check code is used as the outer code. The study shows that the system can offer much higher spectral efficiency, for example, 39 Mbps, which is 3 times higher than the current HomePlug1.0 system. We show several essential requirements to achieve high rate such as frequency and time diversifications, multi-level error protection.

## Source model aided lossless turbo source coding

- **Status**: ❌
- **Reason**: turbo 기반 무손실 소스 코딩(압축), 채널 ECC가 아닌 소스 코딩
- **ID**: ieee:5755819
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Nicolas Duetsch, Sebastian Graf, Javier Garcia-Frias +1
- **PDF**: https://ieeexplore.ieee.org/document/5755819
- **Abstract**: The integration of a source model into lossless source coding based on punctured turbo codes is considered. We use the turbo principle to iteratively estimate the source statistics and to compensate the errors due to compression. In order to cope with the critical part of joint estimation and decoding, the start-up, we propose the use of an asymmetric turbo code with one recursive Quick-Look-In component code. Moreover, we present an alternative puncturing method, which ensures the compression of the data in a predetermined number of reconstruction attempts. Simulation results show that the proposed scheme outperforms traditional source codes when compressing data with memory.

## Products of Random Matrices in Iterative (Turbo) Decoding

- **Status**: ❌
- **Reason**: turbo MAP 디코딩의 random matrix 곱 수렴성 이론, 부호설계/디코더 이식 기여 없는 순수 이론
- **ID**: ieee:5755906
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Lars Schmitt, Heinrich Meyr
- **PDF**: https://ieeexplore.ieee.org/document/5755906
- **Abstract**: From an implementation as well as theoretical point of view it is a fundamental property of the symbol-by-symbol MAP decoding algorithm, that the dependence of the decoder output on the decoder inputs decays with distance in the code trellis. By using results from the theory of products of random matrices we present a general prove of this property and show that the rate of decay is exponentially with distance along the trellis. Furthermore, we examine how the rate of decay depends on the channel parameter and the a priori information, and how it evolves during the iterative decoding process. Finally, we comment on possible practical implications.

## The Singleton Bound for Network Error-Correcting Codes

- **Status**: ❌
- **Reason**: 네트워크 에러정정 부호의 Singleton bound 순수 이론, LDPC 디코더/HW/구성 기여 없음
- **ID**: ieee:5755844
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Ning Cai, Raymond W. Yeung
- **PDF**: https://ieeexplore.ieee.org/document/5755844
- **Abstract**: Inspired by network coding, network error-correcting codes was introduced in "N. Cai, R. W. Yeung, Network coding and error correction" for multicasting a source message to a set of nodes on a network. The usual approach in existing networks, namely link-by-link error correction, is a special case of network error correction. In "N. Cai, R. W. Yeung, Network coding and error correction", network generalizations of the Hamming bound and the Gilbert-Varshamov bound were obtained. In this paper, we prove the network generalizations of the Singleton Bound and its tightness.

## Factor Graph Based Derivation of a Receiver for PCC Coded Transmissions over a Frequency Selective Fading Channel

- **Status**: ❌
- **Reason**: PCC(병렬연접 컨볼루션) 수신기 factor graph 유도, 채널추정 결합이라 NAND LDPC 이식 기법 없음
- **ID**: ieee:5755938
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: M. F. Flanagan, A. D. Fagan
- **PDF**: https://ieeexplore.ieee.org/document/5755938
- **Abstract**: In previous work, we presented a receiver to detect and decode parallel concatenated convolutional (PCC) coded transmissions over a frequency selective Rayleigh fading channel. This scheme generalized work by Valenti and Woerner to frequency selective channels. It was shown that re-estimation of the channel after each PCC decoding iteration yields significant gain. In this paper we present a detailed derivation of our receiver from factor graph theory. This illustrates the interaction between the channel estimation procedure and the message passing algorithm. In particular it is shown that, in contrast to Valenti and Woerner's scheme, the pilot symbols appear as variables in the factor graph.

## A New Method for Performance Evaluation of Bit Decoding Algorithms Using Statistics of the Log Likelihood Ratio

- **Status**: ❌
- **Reason**: LLR pdf를 지수모델로 추정하는 성능평가(시뮬레이션 샘플수 절감) 방법 — 디코더/구성/HW 기여 아닌 평가기법
- **ID**: ieee:5755877
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Ali Abedi, Amir K. Khandani
- **PDF**: https://ieeexplore.ieee.org/document/5755877
- **Abstract**: This paper presents a new method for the performance evaluation of bit decoding algorithms. The method is based on estimating the Probability Density Function (pdf) of the bit Log Likelihood Ratio (LLR) by using an exponential model. It is widely known that the pdf of the bit LLR is close to the normal density. The proposed approach takes advantage of this property to present an efficient algorithm for the pdf estimation. The moment matching method is combined with the maximum entropy principle to estimate the underlying parameters. We present a simple method for computing the probabilities of the point estimates for the estimated parameters, as well as for the bit error rate. The corresponding results are used to compute the number of samples that are required for a given precision of the estimated values. It is demonstrated that this method requires significantly fewer samples as compared to the conventional Monte-Carlo simulation.

## A Quasi-Random Approach to Space-Time Codes

- **Status**: ❌
- **Reason**: 공간시간 부호 + turbo형 반복디코딩, LDPC 아님, 무선 응용 특이적이라 이식 기법 없음
- **ID**: ieee:5755927
- **Type**: conference
- **Published**: 3-7 April 
- **Authors**: Keying Wu, Li Ping, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5755927
- **Abstract**: This paper presents a quasi-random approach to space-time (ST) codes. The basic principle is conceptually simple, yet still very effective and flexible regarding the transmission rate and antenna numbers. We outline a turbo-type iterative decoding algorithm with complexity growing linearly with the transmit antenna number, and independently of the layer number. We develop simple techniques for fast performance assessment. Based on these techniques, efficient power allocation strategies are examined, which greatly enhance the system performance. Simulation results show that the proposed code can achieve near-capacity performance at low decoding complexity.

## Symbol-flipping based decoding of generalized low-density parity-check codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 GLDPC 심볼플립 디코딩, 비이진이라 제외
- **ID**: ieee:1696457
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Fang-Chun Kuo, L. Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/1696457
- **Abstract**: An efficient symbol-flipping based decoding algorithm designed for nonbinary generalized low-density parity-check (GLDPC) codes is proposed. By extending the concept of the weighted bit flip voting (WBFV) algorithm designed for binary Hamming-code based GLDPC codes, the symbol-flipping decoding algorithm can be beneficially employed for decoding the family of GLDPC codes constructed from nonbinary constituent codes, such as nonbinary Bose Chaudhuri Hocquenghem (BCH) codes or Reed Solomon (R-S) codes. The simulation results demonstrate that improvements of 1 dB and 2.7 dB are achieved by the proposed coding scheme in comparison to the more conventional binary GLDPC codes using the WBFV decoding algorithm, when using the Galois Field GF(32) for communicating over AWGN and uncorrelated Rayleigh fading channels, respectively

## Effects of impulse noise on the performance of multidimensional parity check codes

- **Status**: ❌
- **Reason**: 다차원 패리티체크(MDPC) 임펄스잡음 성능, LDPC 아닌 단순 패리티코드+이론 bound
- **ID**: ieee:1696597
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: S. Nammi, D.K. Borah, C. Schneider +1
- **PDF**: https://ieeexplore.ieee.org/document/1696597
- **Abstract**: This paper investigates the effects of impulse noise on the performance of multidimensional parity check codes (MDPC) in additive white Gaussian noise and Rayleigh fading channels. The Bhattacharya upper bound is derived for impulsive noise and is found to closely match with the simulation results. It is observed that impulse noise can degrade the bit error rate performance by several dBs. Further, the use of incorrect impulse noise model in the receiver decoding algorithm is found to cause severe penalty in fading channels. Our results also show that MDPC codes outperform traditional convolutional codes in impulsive noise channels. The performance of MDPC codes is found to be slightly inferior to turbo codes, when the latter uses slightly lower code rate and higher complexity. The capacity limits for impulsive noise channels are also calculated

## Union bounds to error probabilities of LDPC-coded Q-ary modulation systems over fast fading MIMO channels

- **Status**: ❌
- **Reason**: LDPC+Q-ary 변조 MIMO 오류확률 union bound, 순수 이론 bound로 디코더/HW 미연결
- **ID**: ieee:1696458
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Jingqiao Zhang, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/1696458
- **Abstract**: Closed-form union bounds are derived for the error performance of low-density parity-check (LDPC) coded Q-ary modulation systems over fast fading multi-input multi-output (MIMO) channels. The LDPC codewords are mapped onto space-time modulation blocks, referred to as associated space-time (AST) codewords, in one-to-one correspondence. Based on this relationship, the distance spectrum of the AST code is identified in a combinatorial manner, and each AST codeword possessing the same distance metric renders the identical pairwise error probability. The union bound is obtained in a closed form and can be efficiently evaluated by the method of polynomial expansion. In addition, the analysis is extended to the system with random coding which contributes to a concise expression of the error exponent. Numerical results are presented for different channel scenarios and modulation schemes, which indicate that the bounds are useful to benchmark the practical performance of iterative detection and decoding algorithms

## A new layered space-time-frequency architecture with LDPC coding for OFDM MIMO multiplexing

- **Status**: ❌
- **Reason**: OFDM MIMO LSTF 아키텍처에 표준 비정형 LDPC 사용, 떼어낼 신규 LDPC 디코더/구성 없음
- **ID**: ieee:1683578
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Yuanliang Huang, Jiangzhou Wang, K. Higuchi +1
- **PDF**: https://ieeexplore.ieee.org/document/1683578
- **Abstract**: This paper is focused on the study of layered space-time-frequency (LSTF) architectures with channel coding for orthogonal frequency division multiplexing (OFDM) multiple-input multiple-output (MIMO) multiplexing system in high speed wireless transmission under frequency-selective fading channel. In order to achieve the available spatial, temporal and frequency diversity, and at the same time make the system implementation feasible for ultra high data rate OFDM MIMO multiplexing, we propose a new LSTF architecture with each independently coded layer being threaded in the three-dimensional space-time-frequency transmission array. List sphere decoding is used for MIMO multiplexing detection, and the irregular low-density parity-check code (LDPC) is chosen as the channel code. Three construction rules are adopted to generate high coding rate irregular LDPC codes with low encoding complexity and little performance loss. Simulation results show that the proposed LSTF architecture can significantly outperform the LSTF assuming each independently coded layer being transmitted through a permanently assigned antenna, and get almost the same performance as the LSTF applying coding across the whole information stream. On the other hand, due to its structure of multiple parallel lower-speed codecs with shorter codeword length, the proposed LSTF architecture is more realizable for ultra high data rate transmission than the LSTF applying coding across the whole information stream

## Design of structured eIRA codes with applications to wireless channels

- **Status**: ❌
- **Reason**: eIRA 코드는 RA계열 구조, 무선채널용 error floor 설계지만 NAND 이식 신규 LDPC 구성 아닌 무선응용 특이적
- **ID**: ieee:1696490
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Yifei Zhang, W.E. Ryan, Fei Peng
- **PDF**: https://ieeexplore.ieee.org/document/1696490
- **Abstract**: In this paper, we present design techniques for structured extended irregular repeat-accumulate (SeIRA) codes with low error-rate floors. These SeIRA codes permit flexibility in code dimension, length, and rate, while facilitating encoder/decoder implementation due to their structure. We present a design algorithm for SeIRA codes and software-based performance results which demonstrate their low floors. Then we present two design algorithms for multi-rate SeIRA code families implementable by a single encoder/decoder. Lastly, we present the performances of SeIRA codes on the single-carrier independent Rayleigh fading channel and SeIRA-coded OFDM over a frequency-selective correlated fading channel

## Low-complexity soft demapper for OFDM fading channels with ICI

- **Status**: ❌
- **Reason**: OFDM ICI 억제 soft demapper, LDPC는 성능평가 부수언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:1696518
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: Fei Peng, W.E. Ryan
- **PDF**: https://ieeexplore.ieee.org/document/1696518
- **Abstract**: We present a low-complexity soft demapper that computes bit log-likelihood ratios (LLRs) while suppressing orthogonal frequency division multiplexing (OFDM) inter-carrier interference (ICI). The proposed demapper consists of two stages and can be realized in a fully-parallel architecture. We examine uncoded and low-density parity-check (LDPC) coded performance over frequency-selective Doppler fading channels. We compare the coded and uncoded performances of our demapper with those of an MMSE detector with successive detection (MMSE-SD) and also the match-filter (MF) bound. We show that the proposed demapper achieves optimal performance in the system operating-SNR region. Given the proposed near-optimal demapper, complex receiver designs that iterate between the detector and the decoder may not be worthwhile

## A purely symbol-based precoded and LDPC-coded iterative-detection assisted sphere-packing modulated space-time coding scheme

- **Status**: ❌
- **Reason**: 비이진 LDPC + STBC-SP 심볼기반 turbo 검출, non-binary라 제외
- **ID**: ieee:1696456
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: O. Alamri, S.X. Ng, F. Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/1696456
- **Abstract**: In this contribution, we propose a purely symbol-based LDPC-coded scheme based on a space-time block coding (STBC) signal construction method that combines orthogonal design with sphere packing, referred to here as (STBC-SP). We demonstrate that useful performance improvements may be attained when sphere packing aided modulation is concatenated with non-binary LDPC especially, when performing purely symbol-based turbo detection by exchanging extrinsic information between the non-binary LDPC decoder and a rate-1 non-binary inner precoder. We also investigate the convergence behaviour of this symbol-based concatenated scheme with the aid of novel non-binary extrinsic information transfer (EXIT) charts. The proposed symbol-based turbo-detected STBC-SP scheme exhibits a 'turbo-cliff' at Eb/N0 = 5.0 dB and achieves an Eb/N0 gain of 19.2 dB at a BER of 10 -5 over Alamouti's scheme

## Precoder-aided iterative detection assisted multilevel coding and three-dimensional EXIT-chart analysis

- **Status**: ❌
- **Reason**: 멀티레벨 코딩 3D EXIT 차트 분석, LDPC 비의존 변조/프리코더 기법으로 떼어낼 LDPC 기법 없음
- **ID**: ieee:1696478
- **Type**: conference
- **Published**: 3-6 April 
- **Authors**: R.Y.S. Tee, S.X. Ng, L. Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/1696478
- **Abstract**: A novel three-dimensional (3D) EXIT chart is developed for investigating the iterative behaviour of multilevel coding (MLC) invoking multistage decoding (MSD). The extrinsic information transfer characteristics of both the symbol-to-bit demapper used and those of the different protection constituent decoders suggest that potential improvements can be achieved by appropriately designing the demapper. The proposed 3D EXIT chart is then invoked for studying the precoder-aided multilevel coding scheme employing both MSD and parallel independent decoding (PID) for communicating over AWGN and uncorrelated Rayleigh fading channels with the aid of 8PSK modulation. At BER=10-5, the precoder was capable of enhancing the achievable Eb/N0 performance by 0.5 dB to 2.5 dB over AWGN and Rayleigh channels, respectively

## SoC for COFDM Wireless Communications: Challenges and Opportunities

- **Status**: ❌
- **Reason**: COFDM 무선 SoC 설계 개관, LDPC 떼어낼 ECC 기법 없는 무선 응용 특이적
- **ID**: ieee:4027497
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Chen-yi Lee, Hsuan-yu Liu, Chien-ching Lin
- **PDF**: https://ieeexplore.ieee.org/document/4027497
- **Abstract**: Coded orthogonal frequency division multiplexing (COFDM) technology has been widely accepted in many communication systems due to both bandwidth efficiency and robustness to channel distortion. This opens a great of opportunities for SoC society to deal with design complexity by exploiting benefits of giga-scale integration. In this paper, we'll first review the general design concept of COFDM systems and then highlight several key issues in SoC realization. Then a system-level design flow by taking into account both performance indices and hardware complexity was introduced. Several core modules related to COFDM system were also addressed to see how better solutions can be achieved, especially for wireless applications. Finally two case studies on WLAN and OFDM-UWB were discussed to demonstrate our proposals as well as to provide some directions for further research

## A Comparative Performance and Complexity Study of Short-Length LDPC and Turbo Product Codes

- **Status**: ❌
- **Reason**: 단length SR-LDPC vs TPC 성능/복잡도 비교; girth-6 제거는 교과서 수준, 새 구성/디코더 기여 없음
- **ID**: ieee:1684775
- **Type**: conference
- **Published**: 24-28 Apri
- **Authors**: M.A. Landolsi
- **PDF**: https://ieeexplore.ieee.org/document/1684775
- **Abstract**: This paper presents a comparative performance and complexity study between low-density parity-check (LDPC) codes and turbo product codes (TPC) of short block length (within 2048 bits). The LDPC codes are of the semi-random (SR) type, characterized by low encoder complexity, and are further optimized by eliminating short cycles of length 4 (minimum girth 6). The TPC codes are obtained from 2D and 3D constructions chosen to match the LDPC codes' parameters. The numerical results show that the SR-LDPC codes have slightly better error performance (to within 0.5dB at a BER of 10-5 while demonstrating lower computational complexity per decoder iteration but the required number of decoding iterations is larger. However, this disadvantage is significantly reduced for moderately high signal-to-noise ratios (starting from 2.5dB). It is therefore concluded that SR-LDPC codes have a more competitive performance-complexity advantage overall

## Applying LDPC Codes to the GPRS

- **Status**: ❌
- **Reason**: GPRS에 표준 LDPC 적용·프로토콜 수정, 새 디코더/구성/HW 없음
- **ID**: ieee:5758153
- **Type**: conference
- **Published**: 2-5 April 
- **Authors**: Fakheredine Keyrouz, Wen Xu, Tiago Gasiba
- **PDF**: https://ieeexplore.ieee.org/document/5758153
- **Abstract**: For GPRS the well-known convolutional code is currently used as a Forward Error Correction (FEC) mechanism, and the Viterbi algorithm for decoding. With the recent introduction of Multimedia Broadcast Multicast Services (MBMS), new applications that require more bandwidth and reliability are foreseen. It is known that the current GPRS system does not perform well enough without further modifications, therefore, more efficient information distribution schemes need to be considered. To meet these increased requirements, especially for MBMS, we study the introduction of carefully designed LDPC codes at the physical layer. To exploit the full benefit of the superior performance of LDPC codes for longer streams in MBMS, a modification in the GPRS protocol stack is proposed where larger RLC/MAC blocks are allowed, and its impact on the existing GPRS protocol stack is minimized.

## Random distributed multiresolution representations with significance querying

- **Status**: ❌
- **Reason**: Distributed multiresolution sensor-network source/data representation; not channel-coding LDPC, no portable ECC technique
- **ID**: ieee:1662446
- **Type**: conference
- **Published**: 19-21 Apri
- **Authors**: W. Wang, K. Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/1662446
- **Abstract**: We propose random distributed multiresolution representations of sensor network data, so that the most significant encoding coefficients are easily accessible by querying a few sensors, anywhere in the network. Less significant encoding coefficients are available by querying a larger number of sensors, local to the region of interest. Significance can be defined in a multiresolution way, without any prior knowledge of the source data, as global summaries versus local details. Alternatively, significance can be defined in a data-adaptive way, as large differences between neighboring data values. We propose a distributed encoding algorithm that is robust to arbitrary wireless communication connectivity graphs, where links can fail or change with time. This randomized algorithm allows distributed computation that does not require strict global coordination or awareness of network connectivity at individual sensors. Because computations involve sensors in local neighborhoods of the communication graph, they are communication-efficient. Our framework uses local interaction among sensors to enable flexible information retrieval at the global level.

## Serially Concatenated LDPC and Space-Time Trellis Codes with Transmit Antenna Selection

- **Status**: ❌
- **Reason**: LDPC+STTC 직렬연접+안테나선택 무선 다이버시티 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:1659751
- **Type**: conference
- **Published**: 17-19 Apri
- **Authors**: Aydin, Altunbas
- **PDF**: https://ieeexplore.ieee.org/document/1659751
- **Abstract**: In this paper, the transmit antenna selection technique is proposed to be applied to a serial concatenation scheme of low-density parity-check (LDPC) and space-time trellis codes (STTC) and the frame error rate performance of this scheme is analyzed over quasi-static, block, and fast Rayleigh fading channels by computer simulations. It is shown that transmit antenna selection further improves the performance of the serial concatenation of LDPC and STTC. In particular, transmit antenna selection provides diversity gain over quasistatic and block fading channels and only coding gain over fast fading channels. It is also shown that diversity gain over fast and block fading channels is improved by increasing the number of LDPC decoding iterations.
