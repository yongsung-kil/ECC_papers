# IEEE Xplore — 2011-09


## Structured Nonbinary Rate-Compatible Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) RC-QC-LDPC 구성으로 비이진 LDPC는 제외 대상
- **ID**: ieee:5971366
- **Type**: journal
- **Published**: September 
- **Authors**: Jie Huang, Wei Zhou, Shengli Zhou
- **PDF**: https://ieeexplore.ieee.org/document/5971366
- **Abstract**: While existing works on rate-compatible low-density parity-check (RC-LDPC) codes, either binary or nonbinary, all focus on random-like construction, we in this letter present a novel method to construct structured nonbinary RC-LDPC codes. Protograph-based design with structured puncturing is applied while numerical simulation of code performance is adopted for optimization. The resultant codes are qualified as nonbinary quasi-cyclic LDPC (QC-LDPC) codes which are amenable to high-speed implementation of encoder/decoder. Numerical results show that the proposed codes achieve very good performance.

## Adaptive Binary Slepian-Wolf Decoding using Particle Based Belief Propagation

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산 소스코딩(압축)으로 채널 ECC가 아님; particle BP도 소스코딩 전용
- **ID**: ieee:5931041
- **Type**: journal
- **Published**: September 
- **Authors**: Lijuan Cui, Shuang Wang, Samuel Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5931041
- **Abstract**: A major difficulty that plagues the practical use of Slepian-Wolf (SW) coding (and distributed source coding in general) is that the precise correlation among sources needs to be known a priori. To resolve this problem, we propose an adaptive asymmetric SW decoding scheme using particle based belief propagation (PBP). We explain the adaptive scheme for asymmetric setup in detail and then further extend it to the non-asymmetric setup based on the code partitioning approach. Moreover, we introduce a Metropolis-Hastings (MH) algorithm in the resampling step, which efficiently decreases the number of simulation iterations. We show through experiments that the proposed algorithm can simultaneously reconstruct the compressed sources and estimate the joint correlation among sources. Further, comparing to the conventional SW decoder based on standard belief propagation, the proposed approach can achieve higher compression under varying correlation statistics.

## On the Position Selection of Relays in Diamond Relay Networks

- **Status**: ❌
- **Reason**: diamond relay network 위치 선택 문제로 LDPC와 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:5934676
- **Type**: journal
- **Published**: September 
- **Authors**: Qing Wang, Pingyi Fan, Matthew R. Mckay +1
- **PDF**: https://ieeexplore.ieee.org/document/5934676
- **Abstract**: The diamond relay network is an efficient cooperative networking configuration in which the source node cooperates with two selected neighbors. For such networks, we investigate the impact of the relay positioning on the performance. In particular, considering an opportunistic protocol based on the use of relaying buffers, we provide sets of constraints which, when satisfied, give sufficient conditions for simultaneously guaranteeing network stability and throughput improvement. These results are given for both symmetric and asymmetric relay locations. In contrast to prior work dealing with the diamond relay network, we also break the strong hypothesis of no interlink interference between the source and relay transmissions. Our results provide design guidelines for relay selection by establishing areas of feasible relay locations, whilst also identifying optimal positions which lead to maximum throughput gain.

## EXIT Chart Based System Design for Iterative Source-Channel Decoding with Fixed-Length Codes

- **Status**: ❌
- **Reason**: 고정길이 부호 반복 소스-채널 복호(ISCD)·EXIT 차트로 LDPC ECC 아님, 떼어낼 기법 없음
- **ID**: ieee:5936793
- **Type**: journal
- **Published**: September 
- **Authors**: Laurent Schmalen, Marc Adrat, Thorsten Clevorn +1
- **PDF**: https://ieeexplore.ieee.org/document/5936793
- **Abstract**: Audio-visual source encoders for digital wireless communications extract parameter sets on a frame-by-frame basis. Due to delay and complexity constraints these parameters exhibit some residual redundancy which manifests itself in non-uniform parameter distributions and intra- as well as inter-frame correlation. This residual redundancy can be exploited by iterative source-channel decoding (ISCD) to improve the robustness against impairments from the channel. In the design process of ISCD systems the well known EXIT charts play a key role. However, in case of inter-frame parameter correlation, the classic EXIT charts do not provide reliable bounds for predicting the convergence behavior of ISCD. We explain the reasons for the so-called overshooting effect and propose a novel extension to the EXIT chart computation which provide significantly better bounds for the decoding trajectories. Four advanced ISCD system configurations are proposed and investigated using the benefits of the improved EXIT chart based system design. These configurations include regular and irregular redundant index assignments. In addition, we incorporate unequal error protection in the optimization of irregular index assignments. We show how to realize a versatile multi-mode ISCD scheme which operates close to the theoretical limit.

## Second-Order Weight Distributions

- **Status**: ❌
- **Reason**: 2차 weight distribution이라는 부호 이론적 성질 — 순수 이론, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6006632
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Shengtian Yang
- **PDF**: https://ieeexplore.ieee.org/document/6006632
- **Abstract**: A fundamental property of codes, the second-order weight distribution, is proposed to solve the problems such as computing second moments of weight distributions of linear code ensembles. A series of results, parallel to those for weight distributions, is established for second-order weight distributions. In particular, an analogue of MacWilliams identities is proved. The second-order weight distributions of regular LDPC code ensembles are then computed. As easy consequences, the second moments of weight distributions of regular LDPC code ensembles are obtained. Furthermore, the application of second-order weight distributions in random coding approach is discussed. The second-order weight distributions of the ensembles generated by a so-called 2-good random generator or parity-check matrix are computed, where a 2-good random matrix is a kind of generalization of the uniformly distributed random matrix over a finite filed and is very useful for solving problems that involve pairwise or triple-wise properties of sequences. It is shown that the 2-good property is reflected in the second-order weight distribution, which thus plays a fundamental role in some well-known problems in coding theory and combinatorics. An example of linear intersecting codes is finally provided to illustrate this fact.

## On a Family of Circulant Matrices for Quasi-Cyclic Low-Density Generator Matrix Codes

- **Status**: ❌
- **Reason**: QC-LDGM(low-density generator matrix) 부호용 circulant 행렬족; 인코딩 효율 위한 생성행렬 구성으로 NAND LDPC ECC 디코더·패리티검사 설계와 무관
- **ID**: ieee:6006589
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Marco Baldi, Federico Bambozzi, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/6006589
- **Abstract**: We present a new class of sparse and easily invertible circulant matrices that can have a sparse inverse though not being permutation matrices. Their study is useful in the design of quasi-cyclic low-density generator matrix codes that are able to join the inner structure of quasi-cyclic codes with sparse generator matrices, so limiting the number of elementary operations needed for encoding. Circulant matrices of the proposed class permit to hit both targets without resorting to identity or permutation matrices that may penalize the code minimum distance and often cause significant error floors.

## Secret-Sharing LDPC Codes for the BPSK-Constrained Gaussian Wiretap Channel

- **Status**: ❌
- **Reason**: Gaussian wiretap channel 비밀공유 보안 응용; 표준 regular/irregular LDPC 사용, 떼어낼 신규 디코더·구성·HW 없음(보안 원칙 제외)
- **ID**: ieee:5750045
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Chan Wong Wong, Tan F. Wong, John M. Shea
- **PDF**: https://ieeexplore.ieee.org/document/5750045
- **Abstract**: The problem of secret sharing over the Gaussian wiretap channel is considered. A source and a destination intend to share secret information over a Gaussian channel in the presence of a wiretapper who observes the transmission through another Gaussian channel. Two constraints are imposed on the source-to-destination channel; namely, the source can transmit only binary phase-shift-keyed (BPSK) symbols, and symbol-by-symbol hard-decision quantization is applied to the received symbols of the destination. An error-free public channel is also available for the source and destination to exchange messages in order to help the secret-sharing process. The wiretapper can perfectly observe all messages in the public channel. It is shown that a secret-sharing scheme that employs a random ensemble of regular low-density parity-check (LDPC) codes can achieve the key capacity of the BPSK-constrained Gaussian wiretap channel asymptotically with increasing block length. To accommodate practical constraints of finite block length and limited decoding complexity, fixed irregular LDPC codes are also designed to replace the regular LDPC code ensemble in the proposed secret-sharing scheme.

## LDPC Codes for the Gaussian Wiretap Channel

- **Status**: ❌
- **Reason**: Gaussian wiretap 보안용 LDPC(security gap 최적화)로 보안 도메인이며 표준 LDPC+differential evolution, NAND ECC에 새 기법 없음
- **ID**: ieee:5740591
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Demijan Klinc, Jeongseok Ha, Steven W. McLaughlin +2
- **PDF**: https://ieeexplore.ieee.org/document/5740591
- **Abstract**: This paper presents a coding scheme for the Gaussian wiretap channel based on low-density parity-check (LDPC) codes. The messages are transmitted over punctured bits to hide data from eavesdroppers. The proposed coding scheme is asymptotically effective in the sense that it yields a bit-error rate (BER) very close to 0.5 for an eavesdropper whose signal-to-noise ratio (SNR) is lower than the threshold SNRE, even if the eavesdropper has the ability to use a bitwise maximum a posteriori (MAP) decoder. Such codes also achieve high reliability for the friendly parties provided they have an SNR above a second threshold SNRB . It is shown how asymptotically optimized LDPC codes are designed with differential evolution where the goal is to achieve high reliability between friendly parties while keeping the security gap SNRB/SNRE as small as possible to protect against passive eavesdroppers. The proposed coding scheme is encodable in linear time, applicable at finite block lengths, and can be combined with existing cryptographic schemes to deliver improved data security by taking advantage of the stochastic nature of many communication channels.

## Irregular Mapping and its Application in Bit-Interleaved LDPC Coded Modulation With Iterative Demapping and Decoding

- **Status**: ❌
- **Reason**: BILCM-ID용 irregular mapping/labeling 기법(변조-디매핑 반복); 무선 coded modulation 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5960810
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Zaishuang Liu, Kewu Peng, Tao Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5960810
- **Abstract**: This paper proposes an irregular mapping technique, where a new labeling searched via modified adaptive binary switch algorithm (ABSA), mixed with a pre-fixed labeling, can provide near-optimal match to a given outer channel code. By using the proposed technique, the bit-interleaved low-density parity-check (LDPC) coded modulation systems with iterative demapping/decoding (BILCM-ID) could achieve near-capacity performance. With a slight modification on the LDPC coded modulation scheme of DVB-T2 standard, the proposed technique can improve the iterative demapping system by exploiting significant iterative gain. The superior performance is verified via extrinsic information transfer (EXIT) chart analysis and bit error rate (BER) simulation.

## Coding for Cryptographic Security Enhancement Using Stopping Sets

- **Status**: ❌
- **Reason**: 암호 보안 강화용 puncturing LDPC로 stopping set 유발; 보안 응용, NAND ECC로 떼어낼 신규 디코더/구성 기법 없음(보안 원칙 제외)
- **ID**: ieee:5753935
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Willie K. Harrison, João Almeida, Steven W. McLaughlin +1
- **PDF**: https://ieeexplore.ieee.org/document/5753935
- **Abstract**: In this paper, we discuss the ability of channel codes to enhance cryptographic secrecy. Toward that end, we present the secrecy metric of degrees of freedom in an attacker's knowledge of the cryptogram, which is similar to equivocation. Using this notion of secrecy, we show how a specific practical channel coding system can be used to hide information about the ciphertext, thus increasing the difficulty of cryptographic attacks. The system setup is the wiretap channel model where transmitted data traverse through independent packet erasure channels (PECs) with public feedback for authenticated automatic repeat-request (ARQ). The code design relies on puncturing nonsystematic low-density parity-check (LDPC) codes with the intent of inflicting an eavesdropper with stopping sets in the decoder. The design amplifies errors when stopping sets occur such that a receiver must guess all the channel-erased bits correctly to avoid an error rate of one half in the ciphertext. We extend previous results on the coding scheme by giving design criteria that reduce the effectiveness of a maximum-likelihood (ML) attack to that of a message-passing (MP) attack. We further extend security analysis to models with multiple receivers and collaborative attackers. Cryptographic security is even enhanced by the system when eavesdroppers have better channel quality than legitimate receivers.

## Data-Dependent Noise-Predictive Symbol-Based Detector for Perpendicular Magnetic Recording Channels

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC와 결합된 DDNP 검출기; 비이진 LDPC 제외 대상이며 자기기록채널 검출기 기법으로 NAND 이식성 없음
- **ID**: ieee:5752244
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Angelo Poloni, Stefano Vincenti, Stefano Valle
- **PDF**: https://ieeexplore.ieee.org/document/5752244
- **Abstract**: This work introduces a new formulation of the well-known data-dependent noise-predictive (DDNP) approach to whiten noise in partial response channel detection. The new approach is tailored for whitening the branches in the recently introduced symbol-based detectors that are demonstrated to have optimal performance in concatenation with non-binary error correction codes, such as non-binary low density parity check (LDPC) codes. This paper describes a new approach in the context of the perpendicular magnetic channel, where a symbol-based BCJR is concatenated with a non-binary LDPC decoder. Several approximations based on conventional DDNP implementations are suggested to quantify the performance of the new algorithm.

## Stopping Set Distributions of Some Reed–Muller Codes

- **Status**: ❌
- **Reason**: Reed-Muller 부호의 stopping set 분포(비-LDPC 부호, BEC-optimal 패리티검사 이론); 떼어낼 LDPC BP 디코더 기법 없는 순수 이론
- **ID**: ieee:6006580
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Yong Jiang, Shu-Tao Xia, Fang-Wei Fu
- **PDF**: https://ieeexplore.ieee.org/document/6006580
- **Abstract**: Stopping sets and stopping set distribution of a linear code are used to determine the performance of this code under iterative decoding over a binary erasure channel (BEC). Let C be a binary [n,k] linear code with parity-check matrix H, where the rows of H may be dependent. A stopping set S of C with parity-check matrix H is a subset of column indices of H such that the restriction of H to S does not contain a row of weight one. The stopping set distribution {Ti(H)}i=0n enumerates the number of stopping sets with size i of C with parity-check matrix H. Note that stopping sets and stopping set distribution are related to the parity-check matrix H of C. Let H* be the parity-check matrix of C which is formed by all the nonzero codewords of its dual code C⊥. A parity-check matrix H is called BEC-optimal if Ti(H)=Ti(H*), i=0,1,..., n and H has the smallest number of rows. In this paper, we study stopping sets, stopping set distributions and BEC-optimal parity-check matrices of binary linear codes. Using finite geometry in combinatorics, we obtain BEC-optimal parity-check matrices and then determine the stopping set distributions for the Simplex codes, the Hamming codes, the first order Reed-Muller codes, and the extended Hamming codes, which are some Reed-Muller codes or their shortening or puncturing versions.

## An Efficient Encoder Rate Control Solution for Transform Domain Wyner–Ziv Video Coding

- **Status**: ❌
- **Reason**: Wyner-Ziv 비디오 코딩(소스-채널 결합/분산 소스코딩); 채널 ECC 아님, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:5756225
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Catarina Brites, Fernando Pereira
- **PDF**: https://ieeexplore.ieee.org/document/5756225
- **Abstract**: Most Wyner-Ziv (WZ) video coding solutions in the literature use a feedback channel (FC) based decoder rate control (DRC) strategy to adjust the bitrate to correct the side information (SI) errors. More recently, some encoder rate control (ERC) strategies have been proposed to address application scenarios where a FC is not available. The ERC based WZ video coding RD performance depends not only on the (encoder) parity rate estimator (PRE) accuracy but also on the decoder “intelligence” in dealing with the residual errors due to parity rate underestimation. In this context, the main objective of this paper is to propose a more efficient and powerful ERC solution for transform domain WZ (TDWZ) video coding by simultaneously tackling the two issues aforementioned with the following technical novelty: 1) integration in an ERC context of Gray mapping for the quantized DCT coefficients to enhance the correlation between WZ and SI data; 2) more accurate PRE to better estimate the needed parity rate to avoid undesired parity rate underestimations and overestimations; 3) novel soft reconstruction function to reduce the impact of the residual bitplane errors in the decoded WZ frame quality; and 4) weighted overlapped block motion compensation technique to refine the SI used in an iterative WZ decoding framework with the correlation noise model parameters dynamically updated. Experimental results show a considerable RD performance improvement with a reduction of up to about 2 dB of the gap between the ERC and DRC based approaches in TDWZ video coding solutions, thus making this ERC based WZ codec the most efficient available and competitive regarding DRC based WZ video coding solutions.

## Tight Performance Bounds for Permutation Invariant Binary Linear Block Codes Over Symmetric Channels

- **Status**: ❌
- **Reason**: permutation-invariant 바이너리 선형부호 list decoding의 성능 bound — 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6006629
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Kostis Xenoulis, Nicholas Kalouptsidis
- **PDF**: https://ieeexplore.ieee.org/document/6006629
- **Abstract**: Random coding performance bounds for $L$-list permutation invariant binary linear block codes transmitted over output symmetric channels are presented. Under list decoding, double and single exponential bounds are deduced by considering permutation ensembles of the above codes and exploiting the concavity of the double exponential function over the region of erroneous received vectors. The proposed technique specifies fixed list sizes $L$  for specific codes under which the corresponding list decoding error probability approaches zero in a double exponential manner. The single exponential bound constitutes a generalization of Shulman-Feder bound and allows the treatment of codes with rates below the cutoff limit. Numerical examples of the new bounds for the specific category of codes are presented.

## Time Diversity in Mobile DVB-T2 Systems

- **Status**: ❌
- **Reason**: DVB-T2 시간 다이버시티/인터리빙 연구, LDPC는 부수 언급; 떼어낼 LDPC 디코더·구성·HW 기법 없음
- **ID**: ieee:5960811
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: David Gozalvez, David Gomez-Barquero, David Vargas +1
- **PDF**: https://ieeexplore.ieee.org/document/5960811
- **Abstract**: DVB-T2 implements a very flexible time interleaving that allows multiple tradeoffs in terms of time diversity, latency and power saving. In this paper, we study in detail these tradeoffs in the context of mobile reception. Together with time diversity, we also investigate the impact of reduced time de-interleaving memory and Alamouti-based MISO in the mobile reception of DVB-T2 services. In addition, we propose the utilization of upper layer FEC protection in order to overcome the limitations of the DVB-T2 physical layer for the provision of long time interleaving, and enable fast zapping. The performance is evaluated by means of simulations in mobile channels that include the presence of fast fading and shadowing in the received signal.

## Resource Optimized Distributed Source Coding for Complexity Constrained Data Gathering Wireless Sensor Networks

- **Status**: ❌
- **Reason**: 분산 소스 코딩(DSC) 데이터 수집 자원 최적화 - 채널 ECC 아님, LDPC 디코더 기법 없음
- **ID**: ieee:5705538
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Hamidreza Arjmandi, Farshad Lahouti
- **PDF**: https://ieeexplore.ieee.org/document/5705538
- **Abstract**: This paper addresses the problem of efficient data gathering based on distributed source coding (DSC) in wireless sensor networks (WSNs) with a complexity constrained data gathering node (DGN). A particular scenario of interest is a cluster of low complexity sensor nodes among which, one node is selected as the cluster head (CH) or the DGN. Utilizing DSC allows for reducing the required rate of communications by exploiting the dependency between the nodes observations in a distributed manner. We consider a DSC-based rate allocation structure, which takes into account the CH (DGN) memory and computational constraints. Specifically, this is accomplished, respectively, by limiting the number of nodes whose data may be stored at the CH and exploited during decoding, and the number of nodes that can be jointly (de)compressed using DSC. Based on this structure, we investigate two WSN resource optimization problems aiming at: (i) minimizing the total network cost and (ii) maximizing the network lifetime. To these ends, optimal dynamic programming solutions based on a trellis structure are proposed that incur substantially smaller computational complexity in comparison to an exhaustive search. Also, a suboptimal yet high performance solution is presented whose complexity grows in polynomial order with the number of network nodes. Numerical results demonstrate that the proposed rate allocation structure and solutions, even with limited complexity, allow for exploiting most of the available dependency and hence the achievable compression gain.

## A Message-Passing Approach to Combating Desynchronization Attacks

- **Status**: ❌
- **Reason**: 워터마크 desync 공격 대응 factor graph 메시지패싱으로 부호복호가 아닌 추론, NAND LDPC BP에 이식 불가
- **ID**: ieee:5734843
- **Type**: journal
- **Published**: Sept. 2011
- **Authors**: Shankar Sadasivam, Pierre Moulin, Todd P. Coleman
- **PDF**: https://ieeexplore.ieee.org/document/5734843
- **Abstract**: We propose a new paradigm for blind watermark decoding in the presence of desynchronization attacks. Employing Forney-style factor graphs to model the watermarking system, we cast the blind watermark decoding problem as a probabilistic inference problem on a graph, and solve it via message-passing. We study a wide range of moderate to strong attacks including scaling, amplitude modulation, fractional shift, arbitrary linear and shift-invariant filtering, and blockwise filtering, and show that the graph-based iterative decoders perform almost as well as if they had exact knowledge of the desynchronization attack parameters. Other desirable features of the graph-based decoders include the flexibility to adapt to other types of attacks and the ability to cope with the “curse of dimensionality” problem that seemingly results when the desynchronization parameter space has high dimensionality. These properties are unlike most blind watermark decoders proposed to date.

## Design of nonbinary LDPC cycle codes based on cycle entropy

- **Status**: ❌
- **Reason**: nonbinary GF(q) LDPC cycle code 설계 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6067586
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Yongqiang Yin, Xingcheng Liu, Chulong Liang
- **PDF**: https://ieeexplore.ieee.org/document/6067586
- **Abstract**: In this paper, we focus on the design of a type of low- density parity-check (LDPC) codes called cycle codes whose parity-check matrix have exactly weight-2 columns. An approach to design nonbinary LDPC cycle codes with good performance is presented based on cycle entropy defined here. This method can obtain an elegant distribution of the nonbinary elements over the Galois Field GF(q) among the cycles whose length is exactly equal to the girth. Simulation results demonstrate that the LDPC codes designed with the proposed algorithm perform better than the randomly-constructed nonbinary LDPC cycle codes.

## Puncturing schemes for rate-compatible non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC puncturing 기법 — 비이진 LDPC 제외 대상
- **ID**: ieee:6067599
- **Type**: conference
- **Published**: 9-11 Sept.
- **Authors**: Bing Zhang, He-Guang Su, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/6067599
- **Abstract**: Finding good puncturing patterns for rate compatible non-binary LDPC codes are considered over additive white Gaussian noise (AWGN) channels in this paper. We first study several popular puncturing schemes for binary LDPC codes and generalize them to non-binary LDPC codes, where the effects of short cycles in Tanner graph are rarely investigated. By care fully studying the impacts of short cycles when puncturing, we put forward a novel puncturing scheme for rate-compatible non binary LDPC codes. Simulation results show that the proposed puncturing scheme is superior to the above known ones for rate compatible non-binary LDPC codes over AWGN channels at certain cases.

## Statistical-Based Density Evolution Algorithm for Nonbinary Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC density evolution — 비이진은 기준상 제외
- **ID**: ieee:6092934
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: Jie Wu, Minjian Zhao, Jie Zhong +2
- **PDF**: https://ieeexplore.ieee.org/document/6092934
- **Abstract**: A statistical-based density evolution algorithm is proposed for nonbinary low-density parity-check (LDPC) codes. It is applicable to both regular and irregular codes under study. The algorithm proposed serves as a tool to analyze the performance limit for iterative decoding of nonbinary LDPC codes, which in turn guides code design. Specifically, it provides approximated evaluations of convergence thresholds for codes given specific degree distributions. It is shown that, for a class of quasi-cyclic (QC) structured extended irregular repeat-accumulate (SeIRA) nonbinary LDPC codes, degree distributions can be optimized via the algorithm proposed. Simulation results exhibit that the nonbinary LDPC codes designed outperform the optimized binary LDPC codes on the AWGN channel with similar code length and rate in terms of bits. Performance gap between the binary and nonbinary LDPC codes is larger in the scenario of higher order modulation.

## An Improved Distributed Video Coding Scheme for Wireless Video Sensor Network

- **Status**: ❌
- **Reason**: 분산 비디오 코딩(DVC) for WSN — 소스/비디오 코딩, 채널 ECC 아님
- **ID**: ieee:6093102
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: Jinhong Di, Aidong Men, Bo Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6093102
- **Abstract**: Distributed video coding (DVC) is considered as one promising video coding scheme for Wireless Video Sensor Network (WVSN) due to its high compression efficiency and error resilience functionalities, as well as the low encoding complexity. This paper presents an improved DVC scheme based on the source classification in wavelet domain. In this scheme, the new side information (SI) refinement method is adopted. Initial SI is achieved by motion-compensated weighted interpolation. Then we use a motion compensated refinement of the partially decoded Wyner-Ziv (WZ) frame to update SI. A better reconstruction of the WZ frame is eventually obtained with the refined SI. The results indicate that the proposed scheme can improve the whole performance of DVC codec compared to state-of-the-art DVC and be deployed over a real visual sensor platform.

## Evaluating Word Error Rate via Radius of Decision Region

- **Status**: ❌
- **Reason**: WER를 결정영역 반경으로 평가하는 순수 이론 — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6093120
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: Liyun Dai, Hongwen Yang
- **PDF**: https://ieeexplore.ieee.org/document/6093120
- **Abstract**: In [1], it is shown that the word error rate (WER) of binary codes under binary phase-shift keying (BPSK) modulation can be evaluated via the square radius distribution of decision region and a simple approximation formula of WER for turbo-like codes is presented. In this paper, we extend the method in [1] to more general cases including high-order modulations and fading channels. Moreover, an improved closed-form approximate WER formula is also proposed which can reduce the approximation error to 0.05 dB under a BPSK modulation and additive white Gaussian noise (AWGN) channel for the signal-to-noise ratio (SNR) of interesting in wireless systems.

## A Quantize-and-Forward Scheme for Future Wireless Relay Networks

- **Status**: ❌
- **Reason**: Quantize-and-forward 릴레이 통신 — 무선 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6093114
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: Guido Dietl, Matthieu Sciora, Georg Zeitler +2
- **PDF**: https://ieeexplore.ieee.org/document/6093114
- **Abstract**: The orthogonal multiple-access relay channel with two sources is considered. The goal of this paper is to show the applicability and effectiveness of a previously introduced quantize-and-forward scheme to a more realistic channel and system model, including orthogonal frequency division multiple access and multipath fading channels. Simulation results are provided to demonstrate the gain of quantize-and-forward relayed communication as opposed to the point-to-point links without the relay.

## Adaptive Reed-Solomon Coding in Eigen-MIMO with Non-Adaptive Modulation

- **Status**: ❌
- **Reason**: Reed-Solomon 적응 부호화(MIMO) — 비-LDPC, 떼어낼 BP 기법 없음
- **ID**: ieee:6092944
- **Type**: conference
- **Published**: 5-8 Sept. 
- **Authors**: S. Alireza Banani, Rodney G. Vaughan
- **PDF**: https://ieeexplore.ieee.org/document/6092944
- **Abstract**: An adaptive coding scheme for spectral efficiency improvement in eigen-MIMO is presented. It uses Reed-Solomon (RS) codes with non-adaptive QAM. Non-adaptive modulation is of interest since it reduces the high complexity - in both the electronics and the protocol - required for deploying the more commonly treated adaptive modulation. RS codes have practical advantages in terms of their algorithmic simplicity, memory requirements and decoder complexity. Unlike many codes, an analytical solution for the error probability is available for RS coding. This facilitates finding the jointly optimal code rate(s) and power allocation on the eigenchannels, with the criterion of maximum instantaneous practicable capacity (data throughput). The adaptation is applied to two different architectures of the encoders/decoders (CODECs) for eigen-MIMO, and their performances are compared with the uncoded case. The outer coding architecture refers to a single CODEC working on the overall serial data, and inner coding refers to separate CODECs for different eigenchannels. The adaptive RS system with optimum power allocation reveals new capacity behavior which is different to that of water-filling. For the moderate values of SNR (6-20 dB) typical of wireless systems, the improvement in the capacity over the no-coding case is greater for the inner coding architecture.

## Secure multi-spectral hand recognition system

- **Status**: ❌
- **Reason**: 생체인식 보안 시스템; ECC는 부수적 템플릿 보호용, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7073952
- **Type**: conference
- **Published**: 29 Aug.-2 
- **Authors**: Maurício Ramalho, Sanchit Singh, Paulo Lobato Correia +1
- **PDF**: https://ieeexplore.ieee.org/document/7073952
- **Abstract**: This paper proposes a secure multimodal biometric recognition system with a multi-level fusion architecture. A multi-spectral camera is used to capture hand images in the visible and in the near-infrared (NIR) bands of the spectrum. The system uses four biometric traits from the user's hands: palmprint (PP), finger surface (FS), hand geometry (HG) and palm veins (PV), being the latter captured in the near-infrared band. In the feature extraction stage, three different techniques (i.e., Orthogonal Line Ordinal Features, Competitive Code and PalmCode) are implemented to extract features from the palmprint, finger surface and palm veins. The resulting features are then converted to binary in order to apply a secure template storage scheme, consisting of a cryptographic hash function combined with an error-correcting code. In the proposed system architecture, the hand geometry is used as a database indexing trait to reduce the search time needed for identification. Recognition results, obtained using a proprietary database that was built for that purpose, are presented for different combinations of the feature extraction techniques on the various biometric traits, as well as for different fusion methods.

## Iterative ICI cancellation based on factor graphs for large FFT sizes

- **Status**: ❌
- **Reason**: OFDM 고이동성 ICI 제거용 factor-graph BP; LDPC는 BICM 베이스라인, NAND 이식 가능한 디코더 신규 기법 없음(무선 응용 특이적)
- **ID**: ieee:7074132
- **Type**: conference
- **Published**: 29 Aug.-2 
- **Authors**: Pello Ochandiano, Henk Wymeersch, Mikel Mendicute +2
- **PDF**: https://ieeexplore.ieee.org/document/7074132
- **Abstract**: This paper focuses on the challenging problem of signal reception for orthogonal frequency division (OFDM) systems in high mobility environments. A novel framework based on the well-known belief propagation (BP) algorithm is proposed for joint inter-carrier interference (ICI) cancellation, signal detection and channel decoding. The performance of the mentioned near-optimal detection strategy is analyzed over a general bit-interleaved coded modulation (BICM) system applying low-density parity-check (LDPC) codes. The inclusion of pilot symbols is also considered to analyze how they assist the detection process. A full parallel turbo receptor is derived which shows good performance when the ICI power is high due to high mobility or the use of large FFT sizes.

## On capacity and coding for segmented deletion channels

- **Status**: ❌
- **Reason**: deletion channel 용량+LDPC외부+marker 내부코드 MAP, 동기화 특이 응용으로 NAND 이식 기법 없음
- **ID**: ieee:6120332
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Feng Wang, Defne Aktas, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/6120332
- **Abstract**: We consider binary deletion channels with a segmentation assumption which appears to be suited for more practical scenarios. Unlike the binary independent and identically distributed (i.i.d.) deletion channel where each bit is independently deleted with an equal probability, the segmentation assumption prohibits certain transmitted bits to be deleted, i.e., in a block of bits of a certain length, only a limited number of deletions can occur. We first propose several upper and lower capacity bounds for the segmented deletion channel. Then we focus on an interleaved concatenation of an outer low-density parity check (LDPC) code with error-correction capabilities and an inner marker code with synchronization capabilities over these channels. With the help of a specifically designed maximum-a posteriori (MAP) detector, we demonstrate reliable transmission at higher code rates than the existing ones reported in the literature.

## Is rateless paradigm fitted for lossless compression of erasure-impaired sources?

- **Status**: ❌
- **Reason**: BEQ 소스코딩(압축/양자화); 채널 ECC가 아님
- **ID**: ieee:6120144
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Silvija Kokalj-Filipović, Emina Soljanin, Predrag Spasojević
- **PDF**: https://ieeexplore.ieee.org/document/6120144
- **Abstract**: Even though in many network scenarios erasure-impaired sources represent a more appropriate data model than frequently used Gaussian and binary sources, they only recently entered the scene of compression coding through introduction of binary erasure quantization over sparse graphs. Binary erasure quantization (BEQ) considers ternary sources (zeros, ones and erasures), and binary reconstructions where Hamming distortion is defined for non-erasure source symbols, and distortion is zero for any binary reconstruction of erasure symbols. We believe that constructive schemes for binary erasure quantization deserve more attention. We focus on the rate-optimal zero-distortion BEQ schemes, resulting in the complete recovery of both the unerased bits and the (positions of) erasures in the source sequence. We analyze suitability of rateless codes for this form of BEQ, in terms of compression and decompression complexity, and the rate-gap with respect to the theoretically optimal rate. We demonstrate how duals of properly designed fountain codes can be used for the erasure-rate adaptive lossless compression if the compression rate gap is traded off for complexity of encoding and decoding. We also show that there might exist a better trade-off if the dual code is doped with additional fake erasures, but the results are not conclusive. Finally, an important contribution is that we recognized and explained an idiosyncrasy of fountain codes when it comes to the construction of dual codes employed in quantization; namely, the common starting point is the iterative erasure decoding with LDPC codes, which is based on the parity check matrix, meaning that the same graph can be used for the quantization, as it represents the generator matrix of the dual code; this is not the case with LT codes whose decoder is based on the same graph as its encoder. Hence, the dualization needs to take a completely different track, as explained here.

## The performance of low-density random linear fountain codes over higher order galois fields under maximum likelihood decoding

- **Status**: ❌
- **Reason**: 고차 GF(q) fountain/RLF 부호, 비이진+비-LDPC erasure; 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:6120277
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Birgit Schotsch, Radu Lupoaie, Peter Vary
- **PDF**: https://ieeexplore.ieee.org/document/6120277
- **Abstract**: Digital fountain codes over higher order Galois fields exhibit a better performance than their binary counter- parts under maximum likelyhood (ML) decoding when transmitted over a symbol erasure channel (SEC). Especially random linear fountain (RLF) codes exhibit an excellent performance, though at the expense of a high computational complexity for decoding due to their high density generator matrix. For practical applications, we propose RLF codes with a reduced density over higher order Galois fields. Although the reduction of the density results in an error floor at higher reception overheads, the level of this error floor can be well controlled by two parameters. For error floor levels that are tolerable in practical applications, a significant density reduction and thus a reduction of the computational complexity can be achieved. Furthermore, we derive a general upper bound on the symbol erasure rate for Luby Transform (LT) codes over Galois fields Fq of order q. Finally, we propose a method to enhance decoding of Fq-codes in the presence of bit erasures by using the binary images of the Fq-elements, such that not complete Fq-elements have to be discarded if their binary counterparts are impaired by bit erasures.

## Scalable constructions of fractional repetition codes in distributed storage systems

- **Status**: ❌
- **Reason**: 분산스토리지 fractional repetition code 조합설계, LDPC ECC 디코더/구성 기법 아님
- **ID**: ieee:6120326
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Joseph C. Koo, John T. Gill
- **PDF**: https://ieeexplore.ieee.org/document/6120326
- **Abstract**: In distributed storage systems built using commodity hardware, it is necessary to have data redundancy in order to ensure system reliability. In such systems, it is also often desirable to be able to quickly repair storage nodes that fail. We consider a scheme - introduced by El Rouayheb and Ramchandran - which uses combinatorial block design in order to design storage systems that enable efficient (and exact) node repair. In this work, we investigate systems where node sizes may be much larger than replication degrees, and explicitly provide algorithms for constructing these storage designs. Our designs, which are related to projective geometries, are based on the construction of bipartite cage graphs (with girth 6) and the concept of mutually-orthogonal Latin squares. Via these constructions, we can guarantee that the resulting designs require the fewest number of storage nodes for the given parameters, and can further show that these systems can be easily expanded without need for frequent reconfiguration.

## Information theory meets circuit design: Why capacity-approaching codes require more chip area and power

- **Status**: ❌
- **Reason**: 순수 정보이론 VLSI 복잡도 하한(인코더 전력), 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:6120330
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Pulkit Grover, Andrea Goldsmith, Anant Sahai +1
- **PDF**: https://ieeexplore.ieee.org/document/6120330
- **Abstract**: It is generally thought that good codes, i.e. codes that operate at rates close to capacity and attain low error probabilities, are sophisticated constructions that require high encoding and decoding circuit power. In this paper, we rigorously show that this intuition is correct by deriving an information-theoretic lower bound on power consumption for encoding circuits using communication-complexity techniques. We first lower bound the "VLSI complexity" - measured as the product Awiresl2 where Awires is the wire-area and I is the number of clock cycles in implementation - for encoding. Using the lower bound on VLSI complexity, we derive a lower bound on power consumption of any fully-parallel encoding implementation for any code, and show that the consumed power must diverge to infinity as the error probability approaches zero. Further, the speed of this divergence increases as the rate approaches channel capacity. We also provide a refinement of an earlier result on VLSI complexity by El Gamal, Greene and Pang, which derives a lower bound on Achipl2, where Achip is the entire chip area required for encoding.

## Lossy Lempel-Ziv like compression algorithms for memoryless sources

- **Status**: ❌
- **Reason**: lossy LZ78 소스압축, 채널 ECC 아님
- **ID**: ieee:6120380
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Narayana Prasad Santhanam, Dharmendra Modha
- **PDF**: https://ieeexplore.ieee.org/document/6120380
- **Abstract**: We analyze Lempel-Ziv (LZ78) like schemes for lossy compression of memoryless sequences. Given a distortion level and an input sequence x̅, the encoder splits the input sequence into phrases, representing each phrase by a potentially distorted phrase of the same length. Unlike the memoryless case, the distorted representation of a phrase is not uniquely defined by the LZ78 parsing mechanism. The crux of extending the LZ78 parsing scheme for the lossy setting is in the choice of the several possible representations of every phrase of x̅. Indeed, certain natural generalizations of the Lempel Ziv parsing scheme to the lossy case have been shown to be suboptimal. We consider Codelet Parsing, a LZ78 like algorithm which chooses a representation of x̅ based on the notion of lower mutual information. Given a distortion level, string and a type, the lower mutual information is a single-letter characterization of the size of set of sequences of the type matching the string to within the specified distortion level. In this paper, we try to understand the Codelet Parsing algorithm, by considering an indealization of the same, and showing that the coding rate of the idealized algorithm is asymptotically optimal. The emphasis in this paper is not the tightest analysis possible, but relative simplicity in analysis that can still bring out many of the empirically observed phenomena of Codelet Parsing.

## Properties of the MMSE of “bad” codes

- **Status**: ❌
- **Reason**: bad code MMSE 순수 이론 bound, 디코더/HW/구성 기여 없음
- **ID**: ieee:6120384
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Ronit Bustin, Shlomo Shamai
- **PDF**: https://ieeexplore.ieee.org/document/6120384
- **Abstract**: We examine non-optimal codes (alternatively referred to as "bad" codes), over the additive Gaussian noise channel. These codes are required to attain a minimum rate at a specific signal-to-noise ratio (snr). For these codes, we provide a tight lower bound on the minimum mean square error (MMSE), valid for any snr, attainable by superposition codebooks, optimal for a specific degraded Gaussian broadcast channel (BC). Moreover, the MMSE function of codes, attaining a minimum required rate at some snr, and the lower bound on the MMSE at some other snr, is completely defined for all snr, and is the one obtained by the corresponding superposition codebooks.

## Iterative QR decomposition-based detection algorithms with multiple feedback and dynamic tree search for LDPC-coded MIMO systems

- **Status**: ❌
- **Reason**: LDPC-coded MIMO QR분해 검출기(MF/VM-QRD), 검출 기법이며 LDPC는 외부부호 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:6253426
- **Type**: conference
- **Published**: 27-29 Sept
- **Authors**: Jingjing Liu, Peng Li, Li Li +2
- **PDF**: https://ieeexplore.ieee.org/document/6253426
- **Abstract**: In this paper, we present two innovative LDPC- coded QR decomposition-based soft-output detection techniques, both of which are able to achieve a near-ML performance with significant reduced complexity compare to other optimal detection solutions, such as MAP or list SD algorithms. The first detector (MF-QRD) employs a multi-feedback technique to select appropriate candidates when the symbols are unreliable. Another detection strategy called variable-M QRD (VM-QRD) detector is developed which dynamically adapts the number of detection candidates according to the channel variations in each detection layer. The irregular PEG LDPC code is employed as the outer channel code which provides efficient redundancy for mitigating remaining co-channel interference and additive noise. And simulation results show that the proposed algorithms have excellent performances.

## Improved extrinsic information scheduling for non-binary cycle codes

- **Status**: ❌
- **Reason**: 고차 GF(q) 비이진 cycle code 대상 — 비이진 LDPC는 제외
- **ID**: ieee:6157861
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Weigang Chen, Li Yu, Jinsheng Yang
- **PDF**: https://ieeexplore.ieee.org/document/6157861
- **Abstract**: Low-density parity-check codes with variable node degree two over high order Galois fields are called non-binary cycle codes. In this paper, several improved extrinsic information scheduling strategies with reduced iteration times are proposed for non-binary cycle codes. Exploiting the property of underlying sparse graphs for cycle codes, iteration times and hardware complexity including computation units and inner memories can obtain a proper trade-off using the proposed fully serial or turbo scheduling in each iteration. In this way, significant error correction performance can be obtained with less hardware resources and iterations.

## On the coded complex field network coding scheme for multiuser cooperative communications with regenerative relays

- **Status**: ❌
- **Reason**: 복소필드 네트워크코딩+멀티유저 협력통신 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6158021
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Xi Cai, Qingchun Chen, Pingzhi Fan +1
- **PDF**: https://ieeexplore.ieee.org/document/6158021
- **Abstract**: Complex field network coding (CFNC) scheme offers a promising scheme to enable multiuser cooperative communication. In this paper, an error control coding is utilized in the CFNC scheme for multiuser cooperative communications with regenerative relays. At both the regenerative relays and the destination, an iterative multiuser decoder is designed to enable iteration between the MAP-based detection of the multiuser signals and the soft-decision decoding of the error control coding scheme. Analysis and simulation results show that, the coded CFNC scheme is able to significantly improve the reliability of the multiuser message delivery in adverse cooperative communication environment.

## Prototype of channel coding algorithms for digital signal processing board

- **Status**: ❌
- **Reason**: convolutional code + Viterbi DSP 구현, 비-LDPC 부호
- **ID**: ieee:6108791
- **Type**: conference
- **Published**: 25-28 Sept
- **Authors**: Roslina Mohamad, Yuslinda Wati Mohamad Yusof, Ahmad Shafiq Razelan
- **PDF**: https://ieeexplore.ieee.org/document/6108791
- **Abstract**: This paper presents a prototype of the channel coding algorithms with a baseband modem for TMS320C6713 implementation purpose. It is essential to use channel coding in baseband signal in order to reduce the error of the received signal. In this study, convolutional code (CC) is selected to be the type of channel coding and Viterbi decoder for decoding method. The parameters that have been analyzed in the research are constraint length, modulation techniques and decoding decision. The baseband modem with channel coding is simulated in Additive White Gaussian Noise (AWGN) and the performances of each parameter are compared in terms of Bit Error Rate (BER) with theoretical values. Results from the simulation of the proposed baseband modem are in line with the theoretical results. The successful in uploading process for the baseband modem model into TMS320C6713 DSP Starter Kit (DSK) indicates the model is suitable for implementation purpose and further improvements need to be made in the next research in order to validate the implementation results.

## An Improved Decoding Algorithm of Non binary LDPC Code

- **Status**: ❌
- **Reason**: 비이진 LDPC(GF(4)) FFT-BP 디코더 — 기준상 non-binary 제외
- **ID**: ieee:6113595
- **Type**: conference
- **Published**: 24-25 Sept
- **Authors**: Haili Hong, Zhuo Sun
- **PDF**: https://ieeexplore.ieee.org/document/6113595
- **Abstract**: An improved decoding algorithm is presented in order to solve the problem of inconvenient for hardware implementation in decoding algorithm for non-binary LDPC codes based on the FFT-BP algorithm. The innovation of the new algorithm is the importing of the logarithmic operations, which will transform multiplication operations to addition operations in the logarithmic domains. Thus the presented algorithm has the advantages of the reduced complexity and the more convenient hardware implementation. A simulation is made using regular non binary LDPC codes under White Gaussian Noise channel based on GF(4). The result shows that the decoding complexity is much more reduced with the performance decrease by about 0.07 dB when BER( Bit Error Rate )is 10-4.

## Optimization of Bilayer Lengthened QC-LDPC Code for Relay Channel Based on Differential Evolution

- **Status**: ❌
- **Reason**: 릴레이 채널용 bilayer QC-LDPC 구성(차분진화로 girth 최적화) - bilayer/릴레이 구조 의존 응용 특이적, 표준 girth 최적화 수준
- **ID**: ieee:6040191
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Hua Xu
- **PDF**: https://ieeexplore.ieee.org/document/6040191
- **Abstract**: A novel optimization algorithm to design a bilayer lengthened QC-LDPC code for relay channel is proposed in this paper, which combine differential evolution algorithm and bilayer graph for LDPC codes. We aim to construct QC-LDPC codes with best girth(maximum girth and minimum numbers of shortest cycles)both at relay node and destination node. Proposed algorithm is composed of two steps, first the exponent matrix of QC-LDPC code for lower graph is searched by differential evolution algorithm, then the exponent matrix of QC-LDPC code for overall graph is also found by differential evolution algorithm based on the obtained exponent matrix for lower graph. Simulation results verify the validity of proposed algorithm. Constructed QC-LDPC codes may perform well both at relay node and destination node.

## Construction Method of LDPC Codes Used for Satellite Interactive System

- **Status**: ❌
- **Reason**: 위성 통신용 LDPC 부호 구성법 - 응용 특이적 구성이고 표준 수준, NAND에 새로 이식할 일반 코드설계 기여 불명확
- **ID**: ieee:6039975
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Chunjiang Liu, Yuhai Shi, Lifu Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/6039975
- **Abstract**: This paper firstly points out the disadvantage and advantage of Turbo Codes and LDPC codes which are used in satellite interactive communication system, then it introduces the common construction method. Subsequently, this paper putts forward a new construction method of a type of LDPC codes which is fit for satellite interactive communication system. Finally, error correction performance of LDPC Codes which are constructed using this method and Turbo codes is simulated comparison.

## Decoder Design for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(16)) EMS 디코더 HW - 비이진 LDPC는 제외 대상
- **ID**: ieee:6040195
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Fei Liu, Haitao Li
- **PDF**: https://ieeexplore.ieee.org/document/6040195
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes can achieve better error-correcting performance than binary LDPC codes when the code length is moderate. In this paper, we give the different initial step for different modulation and present a hardware implementation of the extended min-sum (EMS) decoding algorithm for non-binary LDPC codes. Moreover, an FPGA simulation over GF(16) is given to demonstrate the efficiency of the presented techniques.

## Multi-Edge Elimination-Based Interleaver for LDPC-CODED BICM Systems

- **Status**: ❌
- **Reason**: BICM 시스템용 멀티에지 제거 인터리버 설계 - 무선 통신 응용 특이적, NAND LDPC ECC로 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:6039974
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Kangming Jiang, Ying Wang, Ying Zeng
- **PDF**: https://ieeexplore.ieee.org/document/6039974
- **Abstract**: In this paper, the impact of multi-edge LDPC symbols on the performance of the bit-interleaved coded modulation (BICM) system is investigated. To avoid the performance degradation caused by multi-edge symbols, we propose a multi-edge elimination-based interleaver design for the LDPC-coded BICM system. It can improve the decoding performance of LDPC-coded BICM system with a little extra computational complexity. Simulation results show that the LDPC-coded BICM system with our proposed interleaver outperforms the traditional system in different code lengths, rates, modulations and channels.

## Code Design and Performance Analysis of a Novel Concatenated LDPC-STBC for Media Communication in Asynchronous Cooperative MIMO Systems

- **Status**: ❌
- **Reason**: 비동기 협력 MIMO용 LDPC-STBC 연접 부호 - 무선 MIMO 응용 특이적, girth-4 제거는 교과서 수준이고 떼어낼 신규 기법 없음
- **ID**: ieee:6040540
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Shan Ding, Lijia Zhang, Hongming Xu
- **PDF**: https://ieeexplore.ieee.org/document/6040540
- **Abstract**: This paper proposes a new cascaded scheme for the asynchronous MIMO systems. In the scheme, the LDPC code without girth-4 and STBC code with guard intervals were employed. The cascaded code is capable to reduce the error rate and improve the performance of transmission, by taking advantage of both LDPC and STBC techniques. What's more, this paper adopted the linear dispersion structure to achieve higher throughout than the classical space time code. At last we apply the concatenated code to the video transmission to demonstrate that the concatenation of LDPC-STBC is more effective than which is without encoding or with a single code on transmission performance.

## A Joint Soft Sparse Encoding Scheme for Relay System

- **Status**: ❌
- **Reason**: 릴레이 시스템용 joint soft sparse 인코딩 - 무선 릴레이 응용 특이적, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:6040182
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Qin Zhang, Dengsheng Lin, Gang Wu
- **PDF**: https://ieeexplore.ieee.org/document/6040182
- **Abstract**: In this paper, we study a joint soft sparse encoding scheme for the three-node relay system. The relayed soft information is expressed basing on the Log- Likelihood-Ratios (LLRs) of the received signals at the relay. We investigate this coding method by using a regular LDPC code at the source and a sparse generator matrix at the relay. We also deliberately design the structure of the joint code by Gaussian approximation. Simulation results demonstrate that the system which uses the proposed coding scheme can obtain a considerable gain over the traditional hard encoding scheme.

## Application of Fountain Code to GPS Navigation Data Structure Design

- **Status**: ❌
- **Reason**: GPS 데이터 프레임용 fountain code 설계 - fountain/erasure 부호이고 응용 특이적, NAND ECC 기법 없음
- **ID**: ieee:6040241
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Meng Wu, Qiyue Yu, Weixiao Meng
- **PDF**: https://ieeexplore.ieee.org/document/6040241
- **Abstract**: Global Positioning System (GPS) has been used widely these days, and it can support a growing number of commercial products, i.e. scientific uses, tracking, and surveillance. There are lots of interesting topics for GPS, and one of the important technologies is how to reasonable design the data frame structure. A good designed structure can improve the efficiency of the frame, and achieve high reliability. While fountain code is a promising and universal technology, with its flexible property of receiving data. This paper proposes a new GPS frame structure based on fountain code as a kind of channel code, which takes full advantages of the flexibility of fountain code. The proposed new scheme expands a new research field for GPS frame structure. And many future works will be done based on this paper.

## Near-Log-MAP Decoding for Turbo Product Codes

- **Status**: ❌
- **Reason**: Turbo Product Codes용 Near-Log-MAP 디코딩 - 비-LDPC 부호이고 product code 구조 의존, 바이너리 LDPC BP로 이식되는 기법 아님
- **ID**: ieee:6040180
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Guo Tai Chen, Lei Cao, Haifeng Zheng
- **PDF**: https://ieeexplore.ieee.org/document/6040180
- **Abstract**: Turbo product codes (TPCs) have been studied since 1994. However, existing decoding algorithms for TPCs are generally based on the algorithm presented by Pyndiah [1], which adopts the idea of MAX-Log-MAP algorithm and neglects the channel side information (CSI). In this paper, we present and investigate the "M-Log-MAP" decoding algorithm that considers multiple codewords in calculating the extrinsic information. It is shown that the algorithm can improve the decoding performance to the near-Log-MAP decoding with a small M (≈ 4). The complexity of the decoding algorithm is also analyzed.

## Performance Analysis of Soft Information Cooperation in Bi-Directional Networks

- **Status**: ❌
- **Reason**: 양방향 릴레이 소프트정보 협력/네트워크코딩, LDPC 무관 — 이식 기법 없음
- **ID**: ieee:6038679
- **Type**: conference
- **Published**: 23-25 Sept
- **Authors**: Sha Wei, Jun Li, Hang Su
- **PDF**: https://ieeexplore.ieee.org/document/6038679
- **Abstract**: In this paper, we propose the soft information cooperation scheme in the bi-directional wireless relay networks.We first compute the Log-Likelihood ratio (LLR), referred to as the soft information of relay received signal in Rayleigh fading channel, and then propose an efficient LLR-based network coding scheme. Moreover, for computational simplicity, we optimize the soft information cooperation by the defined self soft information at terminals. In addition, we analyze the system performance in terms of generalized signal-to-noise ratio (GSNR), which is shown to be an efficient metric to reveal the BER performance, for one-relay and multi-relay cases. The simulation results show that the soft information cooperation scheme outperforms the traditional amplify-and-forward (AF), decode-and-forward (DF) and compress-and- forward (CF) protocols in terms of GSNR and bit- error rate (BER) in the low-SNR regime.

## Low-complexity motion estimation algorithm using edge feature for video compression on wireless video sensor networks

- **Status**: ❌
- **Reason**: 비디오 압축 모션추정 알고리즘, LDPC/ECC 무관
- **ID**: ieee:6077043
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Phat Nguyen Huu, Vinh Tran-Quang, Takumi Miyoshi
- **PDF**: https://ieeexplore.ieee.org/document/6077043
- **Abstract**: This paper proposes a video compression algorithm that uses the edges of frames to estimate and compensate for motions. Based on the algorithm, we propose two schemes that balance energy consumption among nodes in a cluster on a wireless video sensor network. In these schemes, the compression process is divided into several small processing components, which are then distributed to multiple nodes while considering their residual energy. We conducted extensive computational simulations to verify our methods and found that the proposed schemes not only solve the energy balance problem by coordination of the processing tasks but also increase the quality of decoded video.

## Soft feedback turbo equalization for underwater acoustic communications

- **Status**: ❌
- **Reason**: UWA soft feedback turbo equalization, LDPC는 베이스라인 채널코딩일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:6107184
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Amirhossein Rafati, Huang Lou, Yahong Rosa Zheng +1
- **PDF**: https://ieeexplore.ieee.org/document/6107184
- **Abstract**: In this paper, A low-complexity turbo detection scheme is proposed for single-carrier multiple-input multiple output (MIMO) underwater acoustic (UWA) communications that employs low-density parity-check (LDPC) channel coding. The proposed iterative soft feedback equalization (SFE) algorithm offers a novel approach to combating error propagation by utilizing the past soft decisions to mitigate inter-symbol interference. In addition, its computational complexity grows only linearly with the number of equalizer coefficients, compared to the quadratic complexity of minimum mean square error-based linear turbo equalizer. Performance of the proposed detection scheme is verified through experimental data collected in MACE10. Experimental results show that it provides robust detection and improved Bit Error Rate (BER) for MIMO UWA communications with different modulations schemes.

## Blind CFO estimation for zero-padded OFDM over underwater acoustic channels

- **Status**: ❌
- **Reason**: 수중음향 OFDM blind CFO 추정, LDPC 무관 무선 추정 기법
- **ID**: ieee:6107178
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: Wei Zhou, Zhaohui Wang, Jie Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/6107178
- **Abstract**: In this paper, we compare the performance and complexity of three existing blind carrier-frequency-offset (CFO) estimators when they are applied to estimate the residual Doppler shift for zero-padded OFDM transmissions over underwater acoustic channels: the null subcarrier based method [1], the O-M algorithm [2], and the Y-G algorithm [3]. Performances of these three methods are evaluated by extensive numerical simulations and by data sets collected from the Mobile Acoustic Communication Experiment conducted off the coast of Martha's Vineyard, MA, July 23, 2010. Simulation results show that the Y-G algorithm always outperforms the O-M algorithm. As far as the fractional part of CFO is concerned, the Y-G algorithm can perform as good as the null subcarrier based method yet with a much lower computational complexity. When working with real data, the Y-G algorithm needs to be modified and integer CFO estimation based on a few null subcarriers is incorporated. Experimental results show that the modified Y-G algorithm, having lower complexity, performs slightly worse than the null subcarrier based method for small and moderate-size constellations, and becomes ineffective for a large constellation.

## Experimental demonstration of non-binary LDPC coded modulation for ultra-long-haul transmission systems

- **Status**: ❌
- **Reason**: non-binary 4-ary LDPC coded modulation - 비이진 LDPC 명시적 제외 대상
- **ID**: ieee:6065957
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Shaoliang Zhang, Murat Arabaci, Fatih Yaman +6
- **PDF**: https://ieeexplore.ieee.org/document/6065957
- **Abstract**: Performance of rate-0.8 4-ary LDPC coded modulation with MAP detector is demonstrated in 40Gb/s dual-polarization QPSK transmissions. We achieve >;10 dB coding gain at BER of 10-6 and show no countable errors after 10,560 km transmission over legacy DMFs.

## Performance of soft-decision FEC in systems with bivariate Gaussian noise distributions

- **Status**: ❌
- **Reason**: bivariate Gaussian 잡음이 soft-decision LDPC 성능에 미치는 영향 분석, 신규 디코더/구성 기여 없는 무선/통신 응용 분석
- **ID**: ieee:6066027
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Junho Cho, Chongjin Xie, Peter J. Winzer
- **PDF**: https://ieeexplore.ieee.org/document/6066027
- **Abstract**: We demonstrate through analysis and Monte Carlo simulations how general bivariate Gaussian noise impacts the performance of soft-decision low-density parity-check (LDPC) codes designed for additive, circularly symmetric Gaussian noise.

## Soft-decision LDPC turbo decoding for DQPSK modulation in coherent optical receivers

- **Status**: ❌
- **Reason**: DQPSK용 QC-LDPC 반복 복조, 표준 QC-LDPC와 변조 결합 응용으로 NAND 이식할 신규 ECC 기법 없음
- **ID**: ieee:6066139
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: F. Yu, N. Stojanovic, F. N. Hauske +11
- **PDF**: https://ieeexplore.ieee.org/document/6066139
- **Abstract**: We investigate DQPSK modulation combined with QC-LDPC coding. By applying iterative demodulation and soft-decision decoding, the differential decoding penalty is reduced by 2.05dB offering an attractive solution for coherent optical systems with soft-decision FEC.

## Space-time coding schemes for optical MIMO

- **Status**: ❌
- **Reason**: 광 MIMO space-time coding/변조 비교, LDPC 떼어낼 신규 디코더/HW/구성 기법 없음
- **ID**: ieee:6066016
- **Type**: conference
- **Published**: 18-22 Sept
- **Authors**: Yejian Chen, Laurent Schmalen, Henning Bülow +2
- **PDF**: https://ieeexplore.ieee.org/document/6066016
- **Abstract**: We compare different FEC coding/modulation approaches for increasing data rate over an optical MIMO communication link with respect to achievable rates and code performance.

## Hybrid forwarding for serial and parallel wireless relaying in m-nakagami fading channel

- **Status**: ❌
- **Reason**: 무선 relay 적응 forwarding, LDPC 부수 언급으로 떼어낼 기법 없음
- **ID**: ieee:6075102
- **Type**: conference
- **Published**: 15-17 Sept
- **Authors**: Chanchal Kumar De, Sumit Kundu
- **PDF**: https://ieeexplore.ieee.org/document/6075102
- **Abstract**: In this paper, an adaptive forwarding strategy for wireless networks using relays in multi hop and cooperative network is analyzed. Two schemes, amplify-and-forward (AF) and decode-and-forward (DF) are investigated depending on channel condition. Further it allows switching between the two schemes according to channel condition. The bit error probability performance (BEP) for the proposed hybrid strategy has been evaluated in presence of m-nakagami fading. We have evaluated the BER performance for variable number of relays in multi hop and cooperative network. The impact of decoding threshold and `m' parameter on bit error rate (BER) is indicated. Further BEP performance is assessed using LDPC code.

## Application analysis of QC-LDPC codes in shallow water acoustic channels

- **Status**: ❌
- **Reason**: 천해 음향채널 QC-LDPC 적용, girth/순환행렬크기 등 표준 QC-LDPC 파라미터 튜닝 수준, 신규 기여 없음
- **ID**: ieee:6061600
- **Type**: conference
- **Published**: 14-16 Sept
- **Authors**: Chen Yougan, Xu Xiaomei, Zhang Lan +1
- **PDF**: https://ieeexplore.ieee.org/document/6061600
- **Abstract**: The shallow water acoustic (SWA) channel is one of the most challenging channels in wireless digital communications. In this paper, we propose a good performance, low complexity channel coding scheme using quasi-cyclic LDPC (QC-LDPC) codes to improve the communication system reliability for SWA channels. A system simulation model including QC-LDPC codes for the SWA channels is built. With the decoding algorithm of belief propagation (BP), the effects of QC-LDPC codes design parameters, such as girth, circulant permutation matrix size and decoding iterations are discussed. To verify the proposed approach, Quangang Xiaocuo harbor blasting data are used to set up a SWA channel model, and the performances of QC-LDPC codes over the channel model are analyzed. The results show that, with the same parameters, the proposed QC-LDPC channel coding strategy for SWA channels substantially outperforms the conventional (3, 6)-LDPC channel coding strategy, and with less complexity and easy implementation.

## High-order modulation based on repeat-accumulate codes for underwater acoustic communications

- **Status**: ❌
- **Reason**: repeat-accumulate 코드+고차변조 수중음향, 비-LDPC RA 부호이고 떼어낼 LDPC 기법 없음
- **ID**: ieee:6061604
- **Type**: conference
- **Published**: 14-16 Sept
- **Authors**: Zhang Lan, Xu Xiaomei, Feng Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/6061604
- **Abstract**: Several characteristics of underwater acoustic (UWA) communication channels-limited bandwidth, extended multipath and severe fading-impede UWA data transmissions. To solve this problem, we propose to set up a receiver combining repeat-accumulate (RA) coding and high-order modulation, and calculate the channel soft information for RA decoding with high-order modulation. A multipath fading acoustic channel model for the southern Taiwan Strait channel is established based on BELLHOP ray model and its real sound speed profile. The paper also discusses the error correction capability of the different combination of RA coding and high-order modulation. Simulation results show that the system performance may be improved by using error correction coding; however, its data rate will be reduced. While the frequency efficiency grows significantly, the reliability cannot be improved remarkably.

## A wireless deadbeat power control for wind power generation systems in smart grid applications

- **Status**: ❌
- **Reason**: 풍력 발전 무선 deadbeat 전력제어에 LDPC가 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6085173
- **Type**: conference
- **Published**: 11-15 Sept
- **Authors**: Ivan R. S. Casella, A. J. Sguarezi Filho, C. E. Capovilla +1
- **PDF**: https://ieeexplore.ieee.org/document/6085173
- **Abstract**: This paper proposes a wireless deadbeat power control scheme employing low density parity check coding for variable speed wind power generation (the wind industry is the huge driver behind the push for super-grids and cross-border infrastructure) to improve system robustness and reliability. The wind energy systems uses a doubly-fed induction generator and a deadbeat control. The performance improvements of the proposed system are investigated in different propagation conditions by using simulations results.

## Efficient iterative receiver for LDPC coded wireless IPTV system

- **Status**: ❌
- **Reason**: 무선 IPTV SCM 반복수신기 복잡도 절감, LDPC 디코더가 베이스라인이고 떼어낼 신규 디코더 기법 없는 응용 특이적
- **ID**: ieee:6116719
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: YouZhe Fan, James She, Chi-ying Tsui
- **PDF**: https://ieeexplore.ieee.org/document/6116719
- **Abstract**: Multi-level superposition coded modulation (SCM) is a scalable technique for wireless video broadcast/ multicast, in which iterative turbo structures provide receivers with multi-resolution demodulations subject to a high complexity. Forward error correction using low-density parity-check (LDPC) code is helpful for better received video quality but further increasing the receiver complexity. In this paper, a method is proposed to reduce the receiver complexity by using a sequential structure with a faster convergence for demodulation. In addition, the iterative demodulator and the LDPC decoder are jointly designed as a multi-loop iterative structure to reduce the decoding complexity. Experimental results show that up to 67% decoding complexity is reduced and better video quality is achieved at receivers under low signal-to-noise ratios.

## Two-level channel coding for cooperative wireless networks based on WiMAX LDPC codes

- **Status**: ❌
- **Reason**: WiMAX 표준 LDPC를 그대로 사용한 협력 무선 두단계 부호화(Plotkin |u|u+v|), 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:6139940
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Robert Morelos-Zaragoza, Nigel D'souza
- **PDF**: https://ieeexplore.ieee.org/document/6139940
- **Abstract**: In this paper, a channel coding scheme is considered for a pair of cooperative broadcasting nodes in a cognitive wireless network. The scheme offers two levels of error protection using as components two low-density parity-check (LDPC) codes drawn from the IEEE 802.16e (WiMAX) specification. A modified version of the |u|u+v| code construction of Plotkin is employed, to obtain two values of error protection for two types messages, as follows. Each cooperating node transmits two sequences: For the first node, the first sequence is a modulated codeword m(v̅1) from a code C1, while the second node remains quiet. The second sequence sent by the first node is again m(v̅1) while the second code sends a modulated codeword m(v̅2) from a code C2. At the receiving node antenna, the sequences are superposed to construct an “over-the-air” modulated |u|u + v| code. Messages with a higher degree of error protection are intended for receiving nodes physically located far from the pair of cooperating nodes. The performance is examined of two-level codes using both BPSK/QPSK mappings and two 4-PAM mappings with two different levels of average energy, over both AWGN and Rayleigh fading channels.

## Distributed source coding for securing a hand-based biometric recognition system

- **Status**: ❌
- **Reason**: 분산소스코딩 기반 생체인식 보안, 소스코딩+보안 응용으로 채널 ECC 아님
- **ID**: ieee:6115820
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Mauricio Ramalho, Paulo Correia, Luís Ducla Soares
- **PDF**: https://ieeexplore.ieee.org/document/6115820
- **Abstract**: Distributed source coding (DSC) is typically used to compress information from multiple correlated sources that do not communicate with each other. In this paper, DSC principles are used to secure biometric data in a multimodal hand-based recognition system, introducing a novel approach for Log-Likelihood Ratio initialization and a new binarization technique. The proposed biometric recognition system relies on a new architecture using three hand-based biometric traits: palmprint, finger surface and hand geometry, being the latter used as a soft biometric to accelerate the identification process. Promising results are achieved in terms of recognition accuracy, speed and security when performing identification on large databases, like the UST Hand Image Database.

## Design and implementation of a belief propagation detector for sparse channels

- **Status**: ❌
- **Reason**: sparse 채널 심볼검출용 BP 검출기로 채널등화기, 부호 디코딩 LDPC BP 기법이 아니어서 이식 기법 없음
- **ID**: ieee:6043282
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Yanjie Peng, Kai Zhang, Andrew G. Klein +1
- **PDF**: https://ieeexplore.ieee.org/document/6043282
- **Abstract**: In this paper, we address the design and implementation of the symbol detector for sparse channels which are described as having long spanning durations but sparse multipath structure. The traditional maximum-likelihood (ML) algorithm provides an optimal performance to eliminate the multipath effect, however its complexity scales exponentially with the channel length. As a more efficient symbol detection algorithm through sparse channels, the iterative belief propagation (BP) algorithm has a complexity merely dependent on the number of nonzero channel coefficients, while achieving a near-optimal error performance. We present the architecture design for a reconfigurable low-complexity high-throughput BP detector. As an example, we implement a BP detector for quadrature phase-shift keying (QPSK) modulation on Xilinx Virtex 5 FPGA with a maximum frequency of 252 MHz and equivalently a throughput of 100.8 Mb/s at 5 iterations.

## A comparison of the error resiliency of bit-plane based and symbol based pixel-domain distributed video coding

- **Status**: ❌
- **Reason**: 분산비디오코딩 JSCC 비교, turbo 기반에 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6115815
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Hu Chen, Eckehard Steinbach, Chang Wen Chen
- **PDF**: https://ieeexplore.ieee.org/document/6115815
- **Abstract**: This work studies the error resilience of pixel-domain distributed video coding in noisy wireless transmission environment. Turbo codes are used to implement the DVC coder and the AWGN model is assumed for the transmission channel. The goal is to find out whether symbol based coding or bit-plane based coding is more robust against channel noise. We compare the two in the context of joint source-channel coding to ensure a high error resilience. First, we propose a framework to estimate the end-to-end distortion for these two schemes. Next, we allocate the rate between source coding and channel coding, aiming at a minimum end-to-end distortion. Then, we simulate the two schemes, setting the same bit budget for them, and compare their error resilience. Experimental results show that symbol based coding outperforms bit-plane based coding by up to 0.7 dB in PSNR of the decoded video.

## On the performance of hybrid-ARQ with code combining over double rayleigh fading channels

- **Status**: ❌
- **Reason**: HARQ code combining 정보이론 분석(outage/ergodic capacity)으로 V2V 채널 성능 평가, LDPC 디코더·구성·HW 기여 없음
- **ID**: ieee:6139866
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Ali Chelli, Matthias Pätzold
- **PDF**: https://ieeexplore.ieee.org/document/6139866
- **Abstract**: In this paper, we study the performance of hybrid automatic repeat request (HARQ) with code combining (CC) over double Rayleigh channels. This channel can be utilized to model the fading envelope of vehicle-to-vehicle (V2V) channels. We derive analytical solutions for the characteristic quantities of double Rayleigh channels, such as the outage probability, the ergodic capacity, and the bit error probability (BEP). Moreover, we study the performance of HARQ with CC. Our analysis focuses on information theoretic aspects of HARQ with CC. closed-form analytical approximations are derived for the ε-outage capacity, the average number of transmissions, and the average transmission rate of HARQ with CC assuming a maximum number of rounds M for the HARQ protocol. In our study, the communication rate per HARQ round is adjusted to the average signal-to-noise ratio (SNR) such that a target outage probability ε is not exceeded. This setting is conform with modern communication systems, in which a quality of service should be ensured independently of the channel conditions. We demonstrate that HARQ with CC allows to communicate at a rate close to the ergodic capacity, especially at low and medium SNR. This rate is achieved in absence of channel state information (CSI) at the transmitter. This feature makes HARQ very attractive for V2V communications. In fact, in V2V channels, the coherence time is too short to allow for feedback of the instantaneous channel conditions from the receiver to the transmitter.

## Intra-WZ quantization mismatch in distributed video coding

- **Status**: ❌
- **Reason**: 분산비디오코딩 양자화 mismatch, 소스코딩 영역으로 채널 ECC 아님
- **ID**: ieee:6115768
- **Type**: conference
- **Published**: 11-14 Sept
- **Authors**: Jürgen Slowack, Jozef Škorupa, Peter Lambert +3
- **PDF**: https://ieeexplore.ieee.org/document/6115768
- **Abstract**: During the past decade, Distributed Video Coding (DVC) has emerged as a new video coding paradigm, shifting the complexity from the encoder - to the decoder-side. This paper addresses a problem of current DVC architectures that has not been studied in the literature so far, that is, the mismatch between the intra and Wyner-Ziv (WZ) quantization processes. Due to this mismatch, WZ rate is spent even for spatial regions that are accurately approximated by the side-information. As a solution, this paper proposes side-information generation using selective unidirectional motion compensation from temporally adjacent WZ frames. Experimental results show that the proposed approach yields promising WZ rate gains of up to 7% relative to the conventional method.
