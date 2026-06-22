# IEEE Xplore — 2010-04


## Parity Check Network Coding for “Wireless Cooperative Communications

- **Status**: ❌
- **Reason**: 무선 협력릴레이 네트워크코딩용 다차원 LDPC; 응용특이 구성으로 NAND 이식 기법 없음
- **ID**: ieee:10151984
- **Type**: journal
- **Published**: April 2010
- **Authors**: Bing Du, Jun Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10151984
- **Abstract**: We develop a cooperative decode-and-forward strategy of distributed Source-Relay network coding for a three-node relay model, in which Relay and Source both send their own messages to Destination. First, we present a cooperative communication protocol to achieve decode-and-forward capacity by leveraging transmit rates between Source and Relay and designing distributed Source-Relay network coding accordingly. After-wards, multi-dimension Low-density parity-check (LDPC) code is constructed as a layered structure, where Source LDPC, Relay LDPC, and network LDPC code are organically integrated to realize a distributed design. Our design randomly embeds network-coded message into the layered structure as effective extra checks offering side information for both Source and Relay. Based on derivation of the algebraic relationship between constituent codes, a good multi-dimension LDPC code profile is generated. Meanwhile, network coding complexity maintains linear to the block length. The coding scheme is demonstrated to approach decode-and-forward capacity and still provides effective spatial diversity.

## Minimum distance computation of LDPC codes using a branch and cut algorithm

- **Status**: ❌
- **Reason**: LDPC 최소거리 계산 branch-and-cut, 순수 이론적 도구; 디코더/HW/코드구성으로 이어지지 않음
- **ID**: ieee:5439310
- **Type**: journal
- **Published**: April 2010
- **Authors**: Ahmet B. Keha, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/5439310
- **Abstract**: We give a branch-and-cut algorithm for finding the minimum distance of a binary linear block code. We give two integer programming (IP) models and study the convex hull of the single constraint relaxation of these IP models. We use the new inequalities as cuts in a branch-and-cut scheme. Finally, we report computational results based on turbo and low density parity check (LDPC) codes that demonstrate the effectiveness of our cuts. We demonstrate that our IP formulation and specific cuts are efficient tools for determining the minimum distance of moderate size linear block codes, specifically, they are very efficient for LDPC codes, and provide us with an additional tool for solving this important problem.

## On the Hardness of Approximating Stopping and Trapping Sets

- **Status**: ❌
- **Reason**: stopping/trapping set 근사의 NP-hardness 순수 복잡도 이론; 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:5437429
- **Type**: journal
- **Published**: April 2010
- **Authors**: Andrew McGregor, Olgica Milenkovic
- **PDF**: https://ieeexplore.ieee.org/document/5437429
- **Abstract**: We prove that approximating the size of stopping and trapping sets in Tanner graphs of linear block codes, and more restrictively, the class of low-density parity-check (LDPC) codes, is NP-hard. The ramifications of our findings are that methods used for estimating the height of the error-floor of moderate- and long-length LDPC codes, based on stopping and trapping set enumeration, cannot provide accurate worst-case performance predictions for most codes.

## Performance analysis of LDPC codes with selection diversity combining over identical and non-identical rayleigh fading channels

- **Status**: ❌
- **Reason**: Rayleigh fading에서 LDPC BER 성능분석(EXIT/DE), 무선응용 분석일 뿐 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:5439356
- **Type**: journal
- **Published**: April 2010
- **Authors**: Beng Soon Tan, Kwok Hung Li, Kah Chan Teh
- **PDF**: https://ieeexplore.ieee.org/document/5439356
- **Abstract**: Selection diversity combining employed in conjunction with low-density parity-check codes is able to mitigate the effects of fading. The closed-form bit-error rate expressions of this scheme over independent and non-identically distributed and independent and identically distributed flat Rayleigh fading channels are derived using the extrinsic information transfer chart and Gaussian approximation. The derived expressions are compared with simulation results as well as the Eb/N0 threshold using density evolution (DE). They are in good agreement with simulation results and have the advantage of reduced computational complexity over DE.

## Structure, property, and design of nonbinary regular cycle codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) regular cycle LDPC — 비이진 LDPC는 제외 대상
- **ID**: ieee:5439309
- **Type**: journal
- **Published**: April 2010
- **Authors**: Jie Huang, Shengli Zhou, Peter Willett
- **PDF**: https://ieeexplore.ieee.org/document/5439309
- **Abstract**: In this paper, we study nonbinary regular LDPC cycle codes whose parity check matrix H has fixed column weight j = 2 and fixed row weight d. Through graph analysis, we show that the parity check matrix H of a regular cycle code can be put into an equivalent structure in the form of concatenation of row-permuted block-diagonal matrices if d is even, or, if d is odd and the code's associated graph contains at least one spanning subgraph that consists of disjoint edges. This equivalent structure of H enables: i) parallel processing in lineartime encoding; ii) considerable resource reduction on the code storage for encoding and decoding; and iii) parallel processing in sequential belief-propagation decoding, which increases the throughput without compromising performance or complexity. On the code's structure design, we propose a novel design methodology based on the equivalent structure of H. Finally, we present various numerical results on the code performance and the decoding complexity.

## Coded multipulse pulse-position modulation for free-space optical communications

- **Status**: ❌
- **Reason**: FSO용 MLC/BICM 라벨링 설계, off-the-shelf LDPC를 베이스라인으로 사용; 떼어낼 신규 디코더/코드설계 없음
- **ID**: ieee:5439306
- **Type**: journal
- **Published**: April 2010
- **Authors**: Trung Thanh Nguyen, Lutz Lampe
- **PDF**: https://ieeexplore.ieee.org/document/5439306
- **Abstract**: In this letter, we address two questions concerning the application of multipulse pulse-position modulation (MPPM) for free-space optical (FSO) communications: (1) under what condition would MPPM offer a notable advantage over conventional pulse-position modulation (PPM), and (2) what practical coding scheme should be used to realize that advantage. Focusing on bandwidth-efficient FSO transmission, we find decimated MPPM constellations which are suitable for combining with binary codes and offer significant gains in terms of constellation-constrained capacity over PPM under simultaneous peak-power, average-power, and bandwidth constraints. We then consider labeling design for the popular bit-interleaved coded modulation (BICM) and devise a new multilevel coding (MLC) architecture for MPPM, which we refer to as reduced-layer MLC (RLMLC). Considering the Poisson FSO channel model as a relevant example, we provide simulative evidence that RL-MLC MPPM with off-the-shelf low-density parity-check codes can outperform any PPM scheme under the same transmission constraints.

## Error-Resilient and Low-Complexity Onboard Lossless Compression of Hyperspectral Images by Means of Distributed Source Coding

- **Status**: ❌
- **Reason**: 초분광 이미지 분산소스코딩(압축); 채널 ECC가 아닌 소스코딩
- **ID**: ieee:5338026
- **Type**: journal
- **Published**: April 2010
- **Authors**: Andrea Abrardo, Mauro Barni, Enrico Magli +1
- **PDF**: https://ieeexplore.ieee.org/document/5338026
- **Abstract**: In this paper, we propose a lossless compression algorithm for hyperspectral images inspired by the distributed-source-coding (DSC) principle. DSC refers to separate compression and joint decoding of correlated sources, which are taken as adjacent bands of a hyperspectral image. This concept is used to design a compression scheme that provides error resilience, very low complexity, and good compression performance. These features are obtained employing scalar coset codes to encode the current band at a rate that depends on its correlation with the previous band, without encoding the prediction error. Iterative decoding employs the decoded version of the previous band as side information and uses a cyclic redundancy code to verify correct reconstruction. We develop three algorithms based on this paradigm, which provide different tradeoffs between compression performance, error resilience, and complexity. Their performance is evaluated on raw and calibrated AVIRIS images and compared with several existing algorithms. Preliminary results of a field-programmable gate array implementation are also provided, which show that the proposed algorithms can sustain an extremely high throughput.

## Computationally Efficient Sparse Bayesian Learning via Belief Propagation

- **Status**: ❌
- **Reason**: 압축센싱용 BP기반 sparse Bayesian learning; 채널 LDPC 디코딩 아님, 이식 기법 없음
- **ID**: ieee:5382564
- **Type**: journal
- **Published**: April 2010
- **Authors**: Xing Tan, Jian Li
- **PDF**: https://ieeexplore.ieee.org/document/5382564
- **Abstract**: We present a belief propagation (BP)-based sparse Bayesian learning (SBL) algorithm, referred to as the BP-SBL, to recover sparse transform coefficients in large scale compressed sensing problems. BP-SBL is based on a widely used hierarchical Bayesian model, which is turned into a factor graph so that BP can be applied to achieve computational efficiency. We prove that the messages in BP are Gaussian probability density functions and therefore, we only need to update their means and variances when we update the messages. The computational complexity of BP-SBL is proportional to the number of transform coefficients, allowing the algorithms to deal with large scale compressed sensing problems efficiently. Numerical examples are provided to demonstrate the effectiveness of BP-SBL.

## Capacity-Achieving CPM Schemes

- **Status**: ❌
- **Reason**: Coded CPM/BICM 코딩변조 설계, 외부코드는 컨볼루션 concatenated; LDPC ECC로 떼어낼 기법 없음
- **ID**: ieee:5437449
- **Type**: journal
- **Published**: April 2010
- **Authors**: Alberto Perotti, Alberto Tarable, Sergio Benedetto +1
- **PDF**: https://ieeexplore.ieee.org/document/5437449
- **Abstract**: The pragmatic approach to coded continuous-phase modulation (CPM) is proposed as a capacity-achieving low-complexity alternative to the serially concatenated CPM (SC-CPM) coding scheme. In this paper, we first perform a selection of the best spectrally efficient CPM modulations to be embedded into SC-CPM schemes. Then, we consider the pragmatic capacity (a.k.a. BICM capacity) of CPM modulations and optimize it through a careful design of the mapping between input bits and CPM waveforms. The so obtained schemes are cascaded with an outer serially concatenated convolutional code to form a pragmatic coded-modulation system. The resulting schemes exhibit performance very close to the CPM capacity without requiring iterations between the outer decoder and the CPM demodulator. As a result, the receiver exhibits reduced complexity and increased flexibility due to the separation of the demodulation and decoding functions.

## Convergence of Min-Sum Message-Passing for Convex Optimization

- **Status**: ❌
- **Reason**: convex 최적화용 min-sum 수렴성; 채널 LDPC 디코딩 아닌 일반 최적화, 이식 기법 없음
- **ID**: ieee:5437447
- **Type**: journal
- **Published**: April 2010
- **Authors**: Ciamac C. Moallemi, Benjamin Van Roy
- **PDF**: https://ieeexplore.ieee.org/document/5437447
- **Abstract**: We establish that the min-sum message-passing algorithm and its asynchronous variants converge for a large class of unconstrained convex optimization problems, generalizing existing results for pairwise quadratic optimization problems. The main sufficient condition is that of scaled diagonal dominance. This condition is similar to known sufficient conditions for asynchronous convergence of other decentralized optimization algorithms, such as coordinate descent and gradient descent.

## Turbo joint source-channel coding of non-uniform memoryless sources in the bandwidth-limited regime

- **Status**: ❌
- **Reason**: Turbo 기반 JSCC, 비-LDPC 부호이며 소스-채널 결합; 이식 가능 BP 기법 없음
- **ID**: ieee:5439357
- **Type**: journal
- **Published**: April 2010
- **Authors**: Idoia Ochoa, Pedro Crespo, Javier Del Ser +1
- **PDF**: https://ieeexplore.ieee.org/document/5439357
- **Abstract**: This letter proposes a novel one-layer coding/ shaping scheme with single-level codes and sigma-mapping for the bandwidth-limited regime. Specifically, we consider nonuniform memoryless sources sent over AWGN channels. At the transmitter, binary data are encoded by a Turbo code composed of two identical RSC (Recursive Systematic Convolutional) encoders. The encoded bits are randomly interleaved and modulated before entering the sigma-mapper. The modulation employed in this system follows the unequal energy allocation scheme first introduced in [1]. The receiver consists of an iterative demapping/decoding algorithm, which incorporates the a priori probabilities of the source symbols. To the authors' knowledge, work in this area has only been done for the power-limited regime. In particular, the authors in [2] proposed a scheme based on a Turbo code with RSC encoders and unequal energy allocation. Therefore, it is reasonable to compare the performance - with respect to the Shannon limit - of our proposed bandwidthlimited regime scheme with this former power-limited regime scheme. Simulation results show that our performance is as good or slightly better than that of the system in [2].

## Piecewise linear LLR approximation for non-binary modulations over Gaussian channels with unknown noise variance

- **Status**: ❌
- **Reason**: 비이진 변조 LLR 근사 기법, 부호와 무관한 변조 LLR 계산이며 NAND 바이너리 LDPC에 떼어낼 디코더 기법 없음
- **ID**: ieee:5478739
- **Type**: conference
- **Published**: 4-7 April 
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/5478739
- **Abstract**: Channel log-likelihood ratio (LLR) calculation on many communication channels is a challenging task especially when non-binary modulations are used. This is because LLRs are usually complicated functions of the channel output and their calculation also requires knowledge of the channel parameters. In this paper, we consider the problem of finding good approximate LLRs for the additive white Gaussian noise channel under non-binary modulations when the noise variance is unknown at the receiver. To this end, we propose piecewise linear LLR approximating functions and we use the LLR accuracy measure of to optimize the parameters. First, we assume that the noise variance is known at the receiver and later we generalize the method to the case of unknown noise variance. It is shown in the latter case that the optimum piecewise linear approximate LLRs depend on the code used on the channel. We observe that the optimized piecewise linear LLRs perform extremely close to exact LLRs.

## Channel coding and carrier recovery for adaptive modulation microwave radio links

- **Status**: ❌
- **Reason**: 마이크로파 무선링크 적응변조+반송파복구; 고율 LDPC는 부수 언급, 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:5476350
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Stefano Chinnici, Carmelo Decanis
- **PDF**: https://ieeexplore.ieee.org/document/5476350
- **Abstract**: This paper deals with channel coding and carrier recovery design for high-speed adaptive modulation microwave radio transmission sytems. The challenges posed by the microwave channel are discussed and the design trade-offs are analyzed. The proposed flexible adaptive modulation solution employs M-QAM modulations from 4 QAM up to 512 QAM and a high rate LDPC code. The code-rate flexible LDPC code performs within 1 dB away from the pragmatic capacity in AWGN channel. Particular attention is paid to the design of the carrier synchronization algorithm working at the low SNR conditions imposed by the code and the relatively poor local oscillator behavior.

## Weighted Symbol-Flipping Decoding for Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(GF(q)) LDPC 심볼 플리핑 디코딩으로 비이진 LDPC 제외 대상
- **ID**: ieee:5480573
- **Type**: conference
- **Published**: 24-25 Apri
- **Authors**: Bing Liu, Jun Gao, Gaoqi Dou +1
- **PDF**: https://ieeexplore.ieee.org/document/5480573
- **Abstract**: In this paper, a new low-complexity symbol-flipping algorithm to decode nonbinary low-density parity-check (LDPC) codes is proposed. The decoding procedure updates iteratively the hard-decision received symbol vector in search of a valid codeword in the symbol vector space. Only one symbol is changed in each iteration, and symbol flipping function combines the number of failed checks and reliability of the received bits and calculated symbols. An optional mechanism to avoid infinite loops in high Galois field search is also proposed. Our studies show that the algorithm achieves an appealing tradeoff between performance and complexity over relatively low Galois field for short to medium code length.

## Iterative LDPC-Hadamard Code-Aided Carrier Frequency Synchronization at Extremely Low SNR

- **Status**: ❌
- **Reason**: LDPC-Hadamard 부호+EM 반송파 동기화, 통신 동기화 응용 특이적이고 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:5480704
- **Type**: conference
- **Published**: 24-25 Apri
- **Authors**: Fajian Tang, Zhiping Shi
- **PDF**: https://ieeexplore.ieee.org/document/5480704
- **Abstract**: In this paper, we consider a method of code-aided carrier frequency synchronization at extremely low signal-to noise values based on LDPC-Hadamard code. This system comprises a low-rate LDPC-Hadamard code that is close to Shannon limit at extremely low SNR values and an EM-based carrier frequency synchronizer that makes use of the posterior probabilities of the data symbols, provided by the iterative decoder. Simulations show that the proposed synchronizer can achieve a bit-error-rate (BER) performance of 10-5 at Es/No=-10 dB, and has negligible BER performance degradation as compared to the ideally synchronized system. Through analysis and simulation, we show that our synchronization strategies are very effective at extremely low SNR values.

## Multi-source Distributed Video Coding in Wireless Video Sensor Networks for Water Conservancy Engineering

- **Status**: ❌
- **Reason**: 분산 비디오 코딩/UV 변조 통신, LDPC ECC와 무관
- **ID**: ieee:5480706
- **Type**: conference
- **Published**: 24-25 Apri
- **Authors**: Zhang Mei-Yan, Cai Wen-Yu
- **PDF**: https://ieeexplore.ieee.org/document/5480706
- **Abstract**: Based on analysis of characteristics of UV (Ultraviolet) light power envelope and the output signal of the detector, a modulation scheme for UV communication system employing low pressure mercury lamp as lamp house was proposed. In the scheme, the frequency of UV power envelope is controlled by the current frequency in the electronic ballast and the scheme is similar to the BFSK (Binary Frequency-Shift keying). The modulation experiment was carried out using low pressure mercury lamp as lamp-house. Results show that the modulation scheme is viable.

## A Simplified Soft Decision Demapping Algorithm of 16-APSK Signals in AWGN Channels

- **Status**: ❌
- **Reason**: 16-APSK 소프트 디맵핑 알고리즘, LDPC는 부수 언급일 뿐 변조/디맵핑 기법으로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5480292
- **Type**: conference
- **Published**: 24-25 Apri
- **Authors**: Enxin Yao, Shuai Yang, Wei Jiang
- **PDF**: https://ieeexplore.ieee.org/document/5480292
- **Abstract**: This paper proposes a novel soft decision demapping algorithm of 16-Amplitude Phase Shift Keying (16-APSK) signals in AWGN channels. The proposed algorithm has a lower complexity compared with the well-known Log-Max algorithm. Numerical results show that the proposed algorithm degrades little in BER performance when it is implemented with Low Density Parity Check (LDPC) codes.

## A Novel Channel Coding Scheme Based on BICM for IBOC-AM

- **Status**: ❌
- **Reason**: BICM 임베디드 LDPC 무선/방송(IBOC-AM) 응용 — LDPC 부수 언급, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:5462434
- **Type**: conference
- **Published**: 23-25 Apri
- **Authors**: Shuyang Liu, Jianping Li
- **PDF**: https://ieeexplore.ieee.org/document/5462434
- **Abstract**: A novel channel coding scheme using bit-interleaved coded modulation (BICM) embedded LDPC (BICM-L) is proposed for Hybrid In-Band-On-Channel (IBOC) Amplitude Modulation (AM) system (IBOC-AM). IBOC-AM broadcasts digital audio signals simultaneously with analog AM programs in the AM band. Since both the power and bandwidth allocated for digital audio transmission are limited in this application, BICM-L channel coding scheme is introduced in IBOC-AM， which can achieve better coding gains without bandwidth expansion. Compared with using conventional scheme which has adopted punctured convolutional coding scheme, better coding gains can be obtained by using BICM-L coding scheme in IBOC-AM. Simulation results confirm that, the coding gains of BICM-L outperform the conventional scheme with 2-3 dB over AWGN channels. For Rayleigh fading channels, the coding gains outperform the conventional scheme with 5-6 dB.

## A unified architecture for efficient data and Non-Data Aided frequency estimation for FPGA implementation and application to satellite communications

- **Status**: ❌
- **Reason**: DA/NDA 반송파 주파수 추정 FPGA 구조(위성통신) — LDPC는 부수 언급, 동기화 회로일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:5479672
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Balasubramanian Ramakrishnan, Jeffrey P. Long
- **PDF**: https://ieeexplore.ieee.org/document/5479672
- **Abstract**: Modern codes such as Turbo and LDPC codes operate at low signal-to-noise ratios, which makes carrier synchronization a challenging problem. Hence in many waveforms, some known symbols are inserted periodically into the data stream to achieve Data-Aided (DA) synchronization. However, these known symbols decrease the throughput of the transmissions. The data symbols which are unknown can also be used for synchronization, in which case it is known as Non-Data Aided (NDA) synchronization. In this paper, we present an efficient structure which is almost the same for both the DA and NDA methods,especially suitable for implementation on Field Programmable Gate Arrays (FPGA). We discuss the implementation complexity and trade-offs involved in the FPGA implementation of this structure. We illustrate its utility by applying it a satellite communications waveform, popularly known as DVB-S2.

## Admission Control and System Capacity Assessment of WiMAX with ACM and nb-LDPC Codes Simulation Study with ViMACCS ns2 Patch

- **Status**: ❌
- **Reason**: WiMAX 시스템레벨 시뮬레이션 + nb-LDPC(비이진); 비이진 LDPC이고 신규 ECC 기법 없음
- **ID**: ieee:5474830
- **Type**: conference
- **Published**: 20-23 Apri
- **Authors**: Adam Flizikowski, Witold Holubowicz, Marcin Przybyszewski +1
- **PDF**: https://ieeexplore.ieee.org/document/5474830
- **Abstract**: Authors propose to use cell level simulation as a natural follow up of the link level tests and a preliminary stage of the systematic approach to the system level tests in the context of IMT-Advanced candidates performance evaluation. The system under test (SUT) consists of flexible realizations of the WiMAX physical layer abstraction (providing customized fidelity and thus simulation complexity) with the nb-LDPC codes. The preliminary assessment of system capacity under quasi-mobility conditions (with ACM) is performed using human mobility models and freeware software for radio coverage planning. Moreover two symbol reservation schemes are evaluated in terms of effective bandwidth utilization, blocking and dropping probability. Complete sharing admission control mechanism (CSCAC) is used to show system performance under various load and mobility patterns. It is shown that using nb-LDPC codes improves system throughput in poor radio conditions as compared to RS-CC coding as in the IEEE 802.16e-2005 specification.

## A Practical Approach to Adaptive Coding for the Three-Node Relay Channel

- **Status**: ❌
- **Reason**: relay 채널 분산 적응 코딩(turbo/convolutional, puncturing) - 비-LDPC, 무선 relay 응용 특이적, 제외
- **ID**: ieee:5506300
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Zhongwei Si, Ragnar Thobaben, Mikael Skoglund
- **PDF**: https://ieeexplore.ieee.org/document/5506300
- **Abstract**: In this paper we propose a new adaptive coding scheme for distributed channel coding for the three-node relay channel. In order to make it feasible for application in wireless sensor networks, the distributed code is built from standard components like Turbo and convolutional codes, and adaptation at the relay is obtained by puncturing the input and output of the employed channel code. The proposed code structure includes distributed Turbo codes and distributed serially concatenated codes as special cases. As the results of our optimization show, significant improvements in terms of rate and coverage are obtained. Compared to theoretical limits a decent performance is achieved considering that the focus is on feasibility.

## New Strategies for Coded Modulation Diversity over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: 비이진 LDPC+QAM+신호공간 다이버시티 코딩변조 — 비이진 LDPC 제외
- **ID**: ieee:5506630
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Zhiping Shi, Jing Li, Zhongpei Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5506630
- **Abstract**: We consider the joint exploitation of coding and diversity techniques to achieve efficient, reliable wireless transmission. The system of interest comprises a powerful non-binary low-density parity-check (LDPC) code that will be soft-decoded to supply strong error protection, a quadratic amplitude modulator (QAM) that directly takes in the non-binary LDPC symbols and will be soft-demodulated, and a modulation diversity (or signal space diversity, SSD) operator that will provide power- and bandwidth-efficient diversity gain. By relaxing the rate of the SSD rotation matrices to below 1, we show that a better rate allocation can be arranged between the LDPC codes and the SSD, which brings significant performance gain over previous systems. To facilitate the design and evaluation of the relaxed SSD rotation matrices, three types of efficient constructions are demonstrated and a set of four criteria are developed. Through analysis and simulations, we show that our strategies are very effective in combating random fading and strong noise on Rayleigh fading channels.

## Slepian-Wolf Coding for Reconciliation of Physical Layer Secret Keys

- **Status**: ❌
- **Reason**: 물리계층 비밀키 reconciliation을 위한 Slepian-Wolf/LDPC - QKD형 정보조정이며 떼어낼 디코더 양자화/HW 기법 없음, 제외
- **ID**: ieee:5506131
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Xiaojun Sun, Xiaofu Wu, Chunming Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/5506131
- **Abstract**: In this paper, we show how to compute the Slepian-Wolf lower bound for the reconciliation of physical layer secret keys between two radio terminals. Two coding approaches, including the syndrome method and the parity method, have been proven to require the same number of bits exchanged between two terminals for the reconciliation in the noiseless environment. We also present a practical coding approach based on LDPC codes, and the gap between the practical approach and the Slepian-Wolf bound is given.

## On Diversity Combining with Unknown Channel State Information and Unknown Noise Variance

- **Status**: ❌
- **Reason**: 불완전 CSI 다이버시티 결합 검출 메트릭, LDPC는 베이스라인 성능평가용일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:5506707
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Erik G. Larsson, Ragnar Thobaben, Gang Wang
- **PDF**: https://ieeexplore.ieee.org/document/5506707
- **Abstract**: We derive detection metrics for soft-output diversity combining for the case of imperfect channel state information at the receiver. We treat in particular the case when the noise variance at the receiver is unknown. We contrast conventional training-based methods to a detector based on the generalized likelihood-ratio (GLR) test paradigm. We study the performance of the detectors via EXIT chart analysis and via simulations of LDPC coded transmission over a fast Rayleigh fading channel. The results show that the GLR receivers can significantly outperform the conventional detectors.

## A Reduced Complexity Soft-Input Soft-Output MIMO Detector Combining a Sphere Decoder with a Hopfield Network

- **Status**: ❌
- **Reason**: MIMO sphere decoder+Hopfield 검출기, 부호는 비이진 QC-LDPC — 비이진 LDPC 제외
- **ID**: ieee:5506464
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Daniel J. Louw, Philip R. Botha, Bodhaswar T. J. Maharaj
- **PDF**: https://ieeexplore.ieee.org/document/5506464
- **Abstract**: In this paper, a reduced complexity soft-input soft-output MIMO detector is presented. The detector is intended to be used in conjunction with an error correction code. The detector combines a Sphere Decoder with a Hopfield network to calculate a max-log-map approximation. It is then combined with the error correction code in an iterative structure (turbo). The code used is a quasi-cyclic non-binary LDPC code. The simulation results demonstrate that with less computational complexity, the proposed system's performance equals that of an optimal sphere decoder based detector.

## Cooperative Spectrum Sensing via Belief Propagation in Spectrum-Heterogeneous Cognitive Radio Systems

- **Status**: ❌
- **Reason**: 인지무선 협력 스펙트럼 센싱용 BP — 채널 ECC가 아닌 센싱 추론, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:5506422
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Husheng Li
- **PDF**: https://ieeexplore.ieee.org/document/5506422
- **Abstract**: In a heterogeneous cognitive radio system, different secondary users may suffer from different activities of primary user, thus making a joint cooperative spectrum sensing difficult. However, there typically exists strong correlation among secondary users located close to each other, which can substantially benefit the spectrum sensing. To leverage the correlation, belief propagation (BP) is applied for cooperative spectrum sensing in heterogeneous cognitive radio systems. Simplifications and assumptions are proposed to facilitate the message computing and passing in BP. Numerical results show that the BP based cooperative spectrum sensing can significantly improve the performance over single-user spectrum sensing using only a few iterations. Simulation also shows that the performance is insensitive to the knowledge of mutual distance between secondary users, as well as the number of bits used to quantize beliefs, the communication range and packet loss.

## Network Coding Based on Product Codes in Cooperative Relaying

- **Status**: ❌
- **Reason**: 네트워크 코딩+product code 협력 중계, LDPC 아님(비-LDPC 부호)
- **ID**: ieee:5506486
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Tafzeel ur Rehman Ahsin, Slimane Ben Slimane
- **PDF**: https://ieeexplore.ieee.org/document/5506486
- **Abstract**: Employing network coding at the relay in cooperative relay system can improve the system throughput. However, XOR based network coding does not provide a strong error correction capability that can be used at the base station (receiver) in decoding the information of the cooperating users. Instead a block code can be used to combine the received user packets at the relay station where only the extra redundancy of the block code are forwarded by the relay station. With this structure a better error correction capability is embedded to the network coding scheme providing a better help to the receiver when decoding the user information. Combining this network coding structure with the individual block codes of the users, an overall product code can be obtained which gives the possibility of generating more powerful overall codes and increases the correction capability of the decoding process at the receiver. The obtained results show that the proposed scheme outperforms the conventional XOR based network coding scheme and gives the possibility of combining more users in the cooperation process.

## Coverage Estimation of Uplink 16 QAM Signal up to 20 MHz Bandwidth Based on Field Trial Results of FH-OFDMA System

- **Status**: ❌
- **Reason**: FLASH-OFDM 무선 16QAM 커버리지 측정 필드트라이얼, LDPC ECC 기법 없음
- **ID**: ieee:5506342
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: H. Oguma, S. Kameda, T. Takagi +4
- **PDF**: https://ieeexplore.ieee.org/document/5506342
- **Abstract**: In this paper, we report on a mobile broadband wireless access (MBWA) system field trial with Fast Low-latency Access with Seamless Handoff Orthogonal Frequency Division Multiplexing (FLASH-OFDM), which was carried out at Sendai city in Japan. This paper describes coverage estimates of an uplink 16 quadrature amplitude modulation (QAM) signal under the condition of constant terminal output power when the bandwidths are from 2.56 MHz to 20.48 MHz. The estimates are based on the field trial results of 1.28 MHz bandwidth. The results show that wider bandwidth yields narrower coverage area. 16 QAM can be used within 55 %, 45 %, 35 %, and 25 % of the field trial area when the signal bandwidths are 2.56 MHz, 5.12 MHz, 10.24 MHz, and 20.48 MHz, respectively. We consider that 16 QAM is useful even if the signal bandwidth is wider than that 10 MHz.

## Reliability-Based Sliced Error Correction in Secret Key Agreement from Fading Channel

- **Status**: ❌
- **Reason**: 비밀키 합의 정보조정(Cascade 기반 sliced error correction) — QKD reconciliation 계열, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:5506543
- **Type**: conference
- **Published**: 18-21 Apri
- **Authors**: Takayuki Shimizu, Hisato Iwai, Hideichi Sasaoka
- **PDF**: https://ieeexplore.ieee.org/document/5506543
- **Abstract**: We consider information reconciliation in secret key agreement from a fading channel where two legitimate parties utilize channel estimates of their fading channel as correlated random variables to generate a secret key. The information reconciliation is a process of correcting the discrepancies between the legitimate parties' keys by public discussion in the presence of eavesdropper, where the amount of the information revealed in the public discussion is needed to be as little as possible. In this paper, we propose information reconciliation protocols using the reliability values of channel estimates in order to correct errors effectively. The proposed information reconciliation protocols are modified versions of a protocol used in quantum key distribution called sliced error correction using Cascade. Simulation results show that the proposed protocols can correct errors with less the number of disclosed bits and less the number of communications than the conventional sliced error correction using Cascade.

## Study of LDPC Coded Rotational OFDM System

- **Status**: ❌
- **Reason**: OFDM rotational modulation coded modulation 응용, LDPC는 부수 사용, 떼어낼 ECC 기법 없음
- **ID**: ieee:5480496
- **Type**: conference
- **Published**: 17-18 Apri
- **Authors**: Zengyou Sun, Qianchun Wang, Ju Ren
- **PDF**: https://ieeexplore.ieee.org/document/5480496
- **Abstract**: The method of LDPC coded rotational modulation in OFDM systems is presented in this paper. This method obtains more coding gain modulation compared to traditional coded modulation techniques in fading channels. The results of simulation show that coded modulation gain of rotation modulation is more apparent than that of non-rotation modulation, and it is more apparent with high bit-rate. In addition, the optimal angle of rotation modulation is given.

## Notice of Retraction: Performance of UEP based MIMO scheme for LDPC codes

- **Status**: ❌
- **Reason**: Retracted(철회 논문), 내용 없음
- **ID**: ieee:5486297
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Xuehua Li, Shuhui Yang, Yafei Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/5486297
- **Abstract**: Retracted.

## Reduced-latency stochastic decoding of LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC stochastic 디코딩, 비이진은 제외 대상
- **ID**: ieee:5483537
- **Type**: conference
- **Published**: 12-15 Apri
- **Authors**: Gabi Sarkis, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/5483537
- **Abstract**: Non-binary LDPC codes have excellent error-correcting performance but have not yet been widely adopted due to the high decoder implementation complexity. Stochastic decoding has been proposed as a low-complexity decoding algorithm for non-binary LDPC codes. In this paper we present a new stochastic decoding algorithm for non-binary LDPC codes using tracking forecast memories that has higher throughput and lower latency than previous stochastic decoders.

## Outage thresholds of LDPC codes over nonergodic block-fading channels

- **Status**: ❌
- **Reason**: 블록페이딩 채널 outage 임계값 추정(순수 이론 bound), 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:5483531
- **Type**: conference
- **Published**: 12-15 Apri
- **Authors**: Iryna Andriyanova, Ezio Biglieri, Joseph J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/5483531
- **Abstract**: This paper derives approximations allowing the estimation of outage probability for standard irregular LDPC codes and full-diversity Root-LDPC codes used over nonergodic block-fading channels. Two separate approaches are discussed: a numerical approximation, obtained by curve fitting, for both code ensembles, and an analytical approximation for Root-LDPC codes, obtained under the assumption that the slope of the iterative threshold curve of a given code ensemble matches the slope of the outage capacity curve in the high-SNR regime.

## Some new results on LT and Raptor codes

- **Status**: ❌
- **Reason**: LT/Raptor(fountain) 코드 분석, LDPC 채널 ECC 아니며 떼어낼 기법 없음
- **ID**: ieee:5483534
- **Type**: conference
- **Published**: 12-15 Apri
- **Authors**: Auguste Venkiah, Charly Poulliat
- **PDF**: https://ieeexplore.ieee.org/document/5483534
- **Abstract**: In this paper, some new studies about LT and Raptor codes are presented. Upper and lower bounds on the asymptotic average error probability are derived and they appear quite tight to predict the performance in the error floor region. This study allows to underline the existing trade-off between the asymptotic overhead and the performance in the error floor region. Then, we propose a method to optimize the precode profile for a given LT distribution using a mixture of Gaussian channels.

## Error bounds for decode-and-forward relaying

- **Status**: ❌
- **Reason**: decode-and-forward 릴레이 ML/MAP 디코더 error bound, 비-LDPC 릴레이 응용 특이적
- **ID**: ieee:5483536
- **Type**: conference
- **Published**: 12-15 Apri
- **Authors**: Alexandre Graell i Amat, Ingmar Land, Lars K. Rasmussen
- **PDF**: https://ieeexplore.ieee.org/document/5483536
- **Abstract**: We analyze and compare the maximum-likelihood (ML) decoder and the maximum a-posteriori (MAP) decoder for coding over a decode-and-forward relay network with orthogonal channels. Using a specific model for the errors introduced by the relay, we derive an optimal MAP decoder that operates on a super-trellis and estimates jointly the transmitted codeword and the error pattern introduced by the relay. Furthermore we present analytical expressions for the error rates for both ML and MAP decoding.

## The Design of Efficiently-Encodable LDPC Codes for Coded Cooperation in Relay Channel

- **Status**: ❌
- **Reason**: 릴레이 채널용 효율적 인코딩 LDPC 행렬 구성, 릴레이 협력 응용 특이적이며 NAND 이식 신규 구성 아님
- **ID**: ieee:5471348
- **Type**: conference
- **Published**: 12-14 Apri
- **Authors**: Ziqiang Chen, Shan Ouyang, Hailin Xiao
- **PDF**: https://ieeexplore.ieee.org/document/5471348
- **Abstract**: For the application of LDPC in relay channel, a new matrix construction method for LDPC code is presented. The parity bits generated by the relay node are viewed as part of the whole code in the destination thus can be transmitted directory to the destination without the second coding process. The destination decodes the messages from both the source and the relay with a jointed matrix presented in this paper. Experiment results show that new technique can greatly promote the performance of LDPC in the relay channel.

## Iterative LDPC-Hadamard Code-Aided Carrier Phase Synchronization at Extremely Low SNR

- **Status**: ❌
- **Reason**: LDPC-Hadamard 코드(비표준 연접) 기반 반송파 위상 동기화, 무선 응용 특이적 비-LDPC ECC
- **ID**: ieee:5471314
- **Type**: conference
- **Published**: 12-14 Apri
- **Authors**: Fajian Tang, Zhiping Shi
- **PDF**: https://ieeexplore.ieee.org/document/5471314
- **Abstract**: In this paper, we consider a method of code-aided carrier phase synchronization at extremely low signal-to-noise values based on LDPC-Hadamard code. This system comprises a low-rate LDPC-Hadamard code that is close to Shannon limit at extremely low SNR values and an EM-based carrier phase synchronizer that makes use of the posterior probabilities of the data symbols, provided by the iterative decoder. Simulations show that the proposed synchronizer can achieve a bit-error-rate (BER) performance of at Es/No=-10 dB, and has negligible BER performance degradation as compared to the ideally synchronized system. Through analysis and simulation, we show that our strategies are very effective at extremely low SNR values.
