# IEEE Xplore — 2018-09


## Design of Quantum LDPC Codes From Quadratic Residue Sets

- **Status**: ❌
- **Reason**: 양자 QC-stabilizer LDPC(self-orthogonal, symplectic) — 양자 전용 직교성에 의존, qLDPC 제외
- **ID**: ieee:8340056
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Yixuan Xie, Jinhong Yuan, Qifu Tyler Sun
- **PDF**: https://ieeexplore.ieee.org/document/8340056
- **Abstract**: We design classes of quantum low-density paritycheck (LDPC) codes, called quasi-cyclic stabilizer (QCS) codes, from conventional QC-LDPC codes. The proposed QCS codes belong to the family of non-Calderbank-Shor-Steane stabilizer codes. The QC-LDPC codes are self-orthogonal with respect to the symplectic inner product (SIP) and are constructed from submatrices of nonorthogonal Latin squares via array dispersion. The Latin squares are constructed using quadratic (non)-residue sets of prime modulus p, where p = 4n ± 1. For p = 4n - 1, two constructions, namely, Type-I-A and Type-I-B QCS codes, are proposed based on matrix superposition and matrix concatenation, respectively. For p = 4n +1, Type-II QCS codes are proposed based on permutations of a base matrix. We show that the parity-check matrix for Type-I-B and Type-II QCS codes is self-orthogonal with respect to the SIP for all orders of circulant permutation matrix. This resulting in ensembles of QCS codes characterized by a single base matrix. We show that the minimum distance of Type-II QCS codes can be lower bounded by the minimum distance of the QC-LDPC codes. Simulation results show that the proposed QCS codes outperform some codes in the literature with a noteworthy low-error floor, below 10-7, over quantum depolarizing channels.

## A Coded DCSK Modulation System Over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: 비이진(nonbinary) protograph LDPC 기반 DCSK 무선 변조 — 비이진 LDPC 제외
- **ID**: ieee:8338131
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Pingping Chen, Long Shi, Yi Fang +3
- **PDF**: https://ieeexplore.ieee.org/document/8338131
- **Abstract**: Coded modulation (CM) is a bandwidth efficient framework to approach the capacity limit of the differential chaos shift keying (DCSK) systems. In this paper, we propose an M-ary DCSK system operated with CM based on nonbinary protograph low-density parity-check (LDPC) codes over Rayleigh fading channels. First, we investigate the performance of the proposed nonbinary channel coded DCSK (CM-DCSK) and bit-interleaved coded DCSK (BICM-DCSK). In particular, we show that CM-DCSK outperforms BICM-DCSK over Rayleigh fading channels in terms of capacity limit. Compared with BICM-DCSK, CM-DCSK can simplify the receiver structure, since it does not require turbo iteration between the noncoherent detector and channel decoder. Second, guided by the modified extrinsic information transfer (EXIT) analysis, we put forth two new types of nonbinary protograph LDPC codes to approach the capacity limit of CM-DCSK. Both EXIT analysis and simulation results demonstrate that the proposed protograph-coded CM-DCSK achieves a better error performance than BICM-DCSK even with iterative decoding. Furthermore, we show the performance superiority of nonbinary protograph-coded CM-DCSK over a practical ultra-wideband channel. Hence, we conclude that this proposed scheme offers a good alternative for wireless local area network applications.

## On Bit-Level Decoding of Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC의 비트레벨 디코딩 — 비이진 LDPC 대상, 바이너리 LDPC 신규 기법 아님
- **ID**: ieee:8340066
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Mu Zhang, Kui Cai, Qin Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/8340066
- **Abstract**: This paper addresses binary message-passing (MP) decoding for nonbinary low-density parity-check (NB-LDPC) codes based on the binary image of Galois field symbols. The parity-check matrix of NB-LDPC codes in binary form is used to perform MP. The corresponding nonbinary check node (CN) update and variable node (VN) update can thus be decomposed to a set of binary sub-CN updates and sub-VN updates with much lower computational complexity. In particular, we start from adapting the binary parity-check matrix with Gaussian elimination. Then, we add redundant rows to the parity-check matrix instead of adaptation to further improve the performance. A min-max operation based on the expanded matrix is proposed for the CN update. It not only decreases the computational complexity incurred by Gaussian elimination but also improves the error performance. Simulation results show that the bit-level decoding with min-max operation can achieve similar error performance as the extended min-sum algorithm, but the computational complexity can be lower than the min-sum algorithm for binary LDPC codes.

## Optimal Design of Cascade LDPC-CPM System Based on Bionic Swarm Optimization Algorithm

- **Status**: ❌
- **Reason**: 위성 LDPC-CPM degree distribution 최적화+표준 PEG — 무선 응용 특이적, 교과서 수준 PEG 재사용, 신규 디코더/구성 없음
- **ID**: ieee:8369365
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Yu Zhang, Qingyu Li, Ling Huang +2
- **PDF**: https://ieeexplore.ieee.org/document/8369365
- **Abstract**: The direct-to-home satellite digital video broadcasting has been fast developed in the past decades, and the continuous phase modulation (CPM) is an alternative modulation scheme with the advantages of constant envelope and high spectral efficiency for the band-limited channel and non-linear amplifiers of the satellite transponder. In this paper, CPM cascaded with irregular low density parity check (LDPC) code is studied. A practical system model with global interleaving is proposed for the optimization of degree distribution of the LDPC codes, and code word design is obtained with a modified progressive edge-growth algorithm. Simulation results combined with theoretical analysis clarify the effect of signal-to-noise ratios and two important CPM parameters (modulation index h and correlation length L ), providing guidance for system design. Simulation on bit error rate performance show the validity of the proposed algorithm. This paper systematically solves the optimal system design of cascade irregular LDPC-CPM and is of great significance for future satellite broadcasting.

## A Novel Shaping Scheme for PAPR Reduction in Single-Carrier Modulation

- **Status**: ❌
- **Reason**: turbo 부호 기반 PAPR shaping(펑처링) 무선 변조 기법 — 비-LDPC, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8331859
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Or Levi, Dan Raphaeli, Yonathan Tate
- **PDF**: https://ieeexplore.ieee.org/document/8331859
- **Abstract**: A novel PAPR shaping technique intended for systems with high spectral efficiency and single carrier transmission is presented. This technique applies puncturing of error correction redundancy bits to achieve a desired Markovian symbol transmission probability distribution, which avoids symbol sequences with high peak values. For a 16-QAM system with transmission rate of 3 bit/symbol and a root raised cosine (RRC) pulse shape filter with roll-off factor 0.1 and duration of six symbols, an overall gain of about 2.2 dB is demonstrated by simulations using pragmatic binary turbo code for error correction. The technique can be used to improve any single carrier communication link limited by the high power amplifier (HPA) peak power.

## Encoding and Indexing of Lattice Codes

- **Status**: ❌
- **Reason**: lattice code의 인코딩/인덱싱(군론적) — LDPC ECC 디코더/구성 기법 아님
- **ID**: ieee:8361838
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Brian M. Kurkoski
- **PDF**: https://ieeexplore.ieee.org/document/8361838
- **Abstract**: Encoding and indexing of lattice codes is generalized from self-similar lattice codes to a broader class of lattices. If coding lattice Ac and shaping lattice As satisfy As ⊆ Ac, then Ac/As is a quotient group that can be used to form a (nested) lattice code C. Conway and Sloane's method of encoding and indexing does not apply when the lattices are not self-similar. Results are provided for two classes of lattices. 1) If Ac and As both have generator matrices in a triangular form that satisfies As ⊆ Ac, then encoding is always possible. 2) When Ac and As are described by full generator matrices, if a solution to a linear diophantine equation exists, then encoding is possible. In addition, special cases where C is a cyclic code are considered. A condition for the existence of a group isomorphism between the information and C is given. The results are applicable to a variety of coding lattices, including Construction A, Construction D, and low-density lattice codes. A variety of shaping lattices may be used as well, including convolutional code lattices and the direct sum of important lattices such as D4, E8, etc. Thus, a lattice code C can be designed by selecting Ac and As separately, avoiding the competing design requirements of self-similar lattice codes.

## Polar Codes and Polar Lattices for the Heegard–Berger Problem

- **Status**: ❌
- **Reason**: polar 부호/polar lattice의 Heegard-Berger 소스코딩 — 비-LDPC, 소스코딩, 떼어낼 BP 기법 없음
- **ID**: ieee:8353931
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Jinwen Shi, Ling Liu, Deniz Gündüz +1
- **PDF**: https://ieeexplore.ieee.org/document/8353931
- **Abstract**: Explicit coding schemes are proposed to achieve the rate-distortion function of the Heegard-Berger problem using polar codes. Specifically, a nested polar code construction is employed to achieve the rate-distortion function for doubly symmetric binary sources when the side information may be absent. The nested structure contains two optimal polar codes for lossy source coding and channel coding, respectively. Moreover, a similar nested polar lattice construction is employed when the source and the side information are jointly Gaussian. The proposed polar lattice is constructed by nesting a quantization polar lattice and a capacity-achieving polar lattice for the additive white Gaussian noise channel.

## Soft-Output-Sparse-Aware (SOSA) Detector for Coded MU-MIMO Systems

- **Status**: ❌
- **Reason**: MU-MIMO sparse-aware 소프트출력 검출기 — 채널 디텍터, LDPC 디코더 기법 아님
- **ID**: ieee:8379451
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: Gyu-Jeong Park, Rong Ran, Seong Keun Oh +1
- **PDF**: https://ieeexplore.ieee.org/document/8379451
- **Abstract**: In this correspondence, we present a novel soft-output-sparse-aware (SOSA) detector for an uplink multiuser multiple-input-multiple-output system. The proposed detector consists of two steps: First, a transmit vector is detected using a low-complexity detector; second, an improved soft-output is generated by exploiting the sparsity of a residual error vector (i.e., the difference between the transmit vector and the detected one). In contrast, the previous sparse-aware (SA) detectors used the sparsity to refine the hard-decision output of the underlying detector. Therefore, the SOSA detector can significantly outperforms the (hard-output) SA detectors for the coded systems since the former only can be well-incorporated into state-of-the-art soft channel decoders. Via simulation results, we demonstrate that the SOSA detector attains a nontrivial coded gain over the (soft-output) underlying detector with a similar complexity. Furthermore, the performance gap grows as signal-to-noise ratio and a system size grow.

## Soft-Output Decision-Based Detection of SSK, BI-SSK and QSM

- **Status**: ❌
- **Reason**: SSK/QSM 변조용 soft-output ML 검출기; LDPC 부호·디코더 기여 없음, 떼어낼 ECC 기법 없는 무선 변조 논문
- **ID**: ieee:8532194
- **Type**: journal
- **Published**: Sept. 2018
- **Authors**: A. A. Tijani, N. Pillay, H. Xu
- **PDF**: https://ieeexplore.ieee.org/document/8532194
- **Abstract**: Space shift keying (SSK) modulation is a special case of conventional spatial modulation (SM), where the amplitude and/or phase modulation symbols are eliminated from the transmission process so as to reduce complexity. However, high spectral efficiencies are difficult to achieve with SSK. At the same time, the spectral efficiency of SM can be further improved. On this note, to further enhance the spectral efficiencies of both SM and SSK, quadrature SM (QSM) and Bi-SSK modulations, respectively, were proposed. In coded channels, typically soft-output detection coupled with soft-input channel decoding yields significant signal-to-noise ratio (SNR) gain. Hence, in this paper, we propose soft-output maximum-likelihood detectors (SOMLD) for SSK, Bi-SSK and QSM modulated systems. Monte Carlo simulation results demonstrate that the error performances of the proposed SOMLD schemes closely match with that of their hard-decision maximum-likelihood detector counterparts in uncoded channels; while, significant SNR gains are yielded in coded channels.

## Blind Estimation of an Approximated Likelihood Ratio in Impulsive Environment

- **Status**: ❌
- **Reason**: 임펄스 잡음 환경 근사 LLR 블라인드 추정이 본질 — 블라인드 추정 문제로 제외(블라인드 LLR 추정)
- **ID**: ieee:8580788
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Yasser Mestrah, Anne Savard, Alban Goupil +2
- **PDF**: https://ieeexplore.ieee.org/document/8580788
- **Abstract**: Robust communication is necessary for many wireless applications. Making a decision at the receiver requires an evaluation of the likelihood. However, in impulsive noise, the traditional Gaussian-based receiver exhibits a very significant performance loss. This paper proposes to approximate the likelihood ratio in a binary transmission with a function adapted to impulsive noise conditions but also efficient when noise is purely Gaussian. We introduce a blind estimation of the two parameters defining the approximation and evaluate its performance when used as the inputs of the belief propagation decoder. Our proposal allows us not only to achieve performance close to the optimal decoding but also to have a simple implementation and to adapt to different environment, impulsive or not, independently of the underlying statistical noise model, without the need of a training sequence.

## MDPC Decoding Algorithms and Their Impact on the McEliece Cryptosystem

- **Status**: ❌
- **Reason**: QC-MDPC 기반 McEliece 암호시스템의 BitFlip 디코딩 변형; 보안 암호 도메인이며 NAND 바이너리 LDPC ECC로 이식할 새 기법 아님
- **ID**: ieee:8511202
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Artur Janoska
- **PDF**: https://ieeexplore.ieee.org/document/8511202
- **Abstract**: In recent years, research has been conducted aimed at finding alternative asymmetric systems other than traditional systems such as RSA (Rivest-Shamir-Adleman algorithm) and ECC (Elliptic-curve cryptography). One of the most promising is code-based cryptosystems since their security is based on well-known NP-hard problems. Especially, the most interesting cryptosystem is system proposed by Misoczki et al. based on QC-MDPC codes which use the modified BitFlip algorithm as the decoding algorithm. This work presents a comparison of different variants of MDPC decoding algorithms and their impact on the cryptosystem. We present a complete analysis of modification of this algorithm and new results of the likelihood of correct word decoding for security systems which ensure security level 2128and 2256.

## Delay-limited Protograph Low Density Parity Codes for Space-Time Block Codes

- **Status**: ❌
- **Reason**: STBC용 지연제한 protograph LDPC 설계; Alamouti STBC 페이딩 채널 특이적, NAND 이식할 일반 코드설계 기법 아님
- **ID**: ieee:8580756
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Thuy V. Nguyen, Cuong Pham, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/8580756
- **Abstract**: This paper presents a framework to design protograph low density parity check (LDPC) codes for wireless communications where Alamouti space time block code (STBC) scheme is exploited to combat with the fading effect and the number of decoding iterations is limited. The decoding threshold of the resulting protograph code is about 0.7 dB better than that of the state-of-the-art code in the literature. The simulation of the proposed code is reported, and simulation results confirm the analytical advantages of the design. No error floor is found down to frame error rate (FER) of 10-6.

## Constellation design with deep learning for downlink non-orthogonal multiple access

- **Status**: ❌
- **Reason**: 딥러닝 NOMA 성상도 설계; LDPC는 부수 언급(터보/LDPC와 결합 가능 정도), 떼어낼 ECC 디코더/구성 기법 없음
- **ID**: ieee:8580937
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: F. Alberge
- **PDF**: https://ieeexplore.ieee.org/document/8580937
- **Abstract**: The non-orthogonal multiple access (NOMA) technique is considered as a key component for the next generation cellular system. In downlink NOMA, the constellation of several users are superposed for transmission. The resulting super-constellation needs to be carefully designed for allowing recovering of the data at the receiver side. A deep learning method for constellation optimization is proposed here in the context of downlink NOMA communications. The method is based on an analogy between auto-encoders, a powerful tool in neural networks, and communication systems. Simulation results have verified the effectiveness of this method for both constellation design and optimization of the individual receivers of the users. The optimized encoder/decoder can be successfully combined with iterative error-correction devices such as turbo-codes or LDPC and can be integrated in current communication systems. This technique is quite general and can be used for point-to-point communication as well as for multi-user access under various channel conditions.

## A Tighter Upper Bound for the BER of Convolutional Codes Over Exponentially Correlated Nakagami-$m$ Fading

- **Status**: ❌
- **Reason**: convolutional code BER 상한 순수 이론 bound; 디코더/HW/구성으로 안 이어짐, 비-LDPC
- **ID**: ieee:8580973
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Yassine Mouchtak, Faissal El Bouanani, Daniel Benevides da Costa
- **PDF**: https://ieeexplore.ieee.org/document/8580973
- **Abstract**: In this paper, a tighter upper bound for the bit error rate (BER) of convolutional codes operating under exponentially correlated Nakagami- m fading is proposed. Our analysis relies on the derivation of new lower bounds per each eigenvalue since the BER expression is written in terms of the pairwise error probability, which by its turn depends on the eigenvalues of the channel covariance matrix. In comparison to previous results published elsewhere in the literature, the proposed bounds are shown to be tighter, specially for high signal-to-noise ratio regions, being therefore of great importance and usefulness for the forthcoming researches in the field. Moreover, this result can be generalized to all linear block codes as well as other fading models as the proposed eigenvalues' upperbounds are the main key of this work.

## Applying Coded Modulation with Probabilistic and Geometric Shaping for Wireless Backhaul Channel

- **Status**: ❌
- **Reason**: 무선 백홀용 확률/기하 shaping과 표준 WiMAX/DVB-S2 LDPC 조합; 표준부호 재사용, 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:8580849
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Najeeb Ul Hassan, Wen Xu, Anastasios Kakkavas
- **PDF**: https://ieeexplore.ieee.org/document/8580849
- **Abstract**: Recently, several shaping schemes have been proposed for optical and wireless communications. A shaping technique modifies the distribution of transmit symbols to approximate the capacity achieving input distribution, hence resulting in a shaping gain. In this work, probabilistic and geometric shaping techniques for wireless backhaul channel are evaluated based on their frame error rate performance using soft and hard decision decoding with LDPC codes from the WiMAX and DVB-S2 standards. For soft decision decoding, both probabilistic and geometric shaping methods show significant gain compared to transmission with uniformly distributed symbols. However, when low complexity hard decision decoding is employed, only probabilistic shaping schemes exhibit large gains.

## Secret Key Sharing Protocol Between Units Connected by Wireless MIMO Fading Channels

- **Status**: ❌
- **Reason**: MIMO 페이딩 채널 비밀키 공유 프로토콜; ECC는 부수 언급, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:8511206
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Valery Korzhik, Aleksandr Gerasimovich, Cuong Nguyen +4
- **PDF**: https://ieeexplore.ieee.org/document/8511206
- **Abstract**: The method of secret key sharing between units that did not possess any secret keys in advance is considered. It is assumed that between these units there are duplex wireless MIMO fading channels. In a recent paper published by D. Qin and Z. Dingh a new key sharing protocol has been proposed between legitimate users based on eigenvalues which are invariant under permutation of two matrices in their product. We extend this statement to a characteristic polynomial and by the way to matrix trace. Methods of key bits extraction are optimized both theoretically and experimentally. On the contrary to a statement of D. Qin and Z. Ding we prove that their key sharing protocol occurs insecure if eavesdroppers have the same channels as legitimate users. In order to provide reliability and security of the shared keys both error correction codes and privacy amplification methods can be used.

## Optimization of Constellation-based DC-BICM Systems over Power Line Channels

- **Status**: ❌
- **Reason**: 전력선 채널용 차분 카오스 BICM 시스템의 protograph LDPC 설계; 통신 응용 특이적 P-LDPC, NAND 이식 가능 신규 코드설계로 보기 어려움
- **ID**: ieee:8580673
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Yuyang Zhang, Lin Wang, Qiwang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8580673
- **Abstract**: In this paper, we propose a constellation-based differential chaotic bit-interleaved coded modulation system with iterative receiver (DC-BICM-IR) over power line channels (PLCs) and then design a new protograph-based low density parity check (P-LDPC) code for the system.

## Capacity of AWGN and Rayleigh Fading Channels with $M$-ary Inputs

- **Status**: ❌
- **Reason**: AWGN/레일리 페이딩 채널 용량 해석; 순수 이론 capacity bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:8580707
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Pei Yang, Zeliang Ou, Hongwen Yang
- **PDF**: https://ieeexplore.ieee.org/document/8580707
- **Abstract**: Since the performance of Turbo and Low Density Parity Check Code (LDPC) codes are very close to Shannon limit, a great deal of attention has been placed on the capacity of additive white Gaussian noise (AWGN) and fading channels with arbitrary channel inputs. However, no closed-form solution has been developed due to the complicated Gaussian integrations. In this paper, we investigate the capacities of AWGN and Rayleigh fading channels with M-ary inputs, e.g. phase shift keying (PSK) and quadrature amplitude modulation (QAM). By firstly adopting successive interference cancellation (SIC) and the entropy power Gaussian approximation, the capacity of an AWGN channel with M-QAM and M-PSK modulations can be approximated as the superposition of the capacity of an AWGN channel with BPSK modulation. Furthermore, the ergodic capacity of a Rayleigh fading channel can be derived directly by averaging the instantaneous capacity of an AWGN channel with respect to the probability density function (PDF) of the fading channel gain. Simulation results verify the effectiveness of the proposed method for estimating the capacity of AWGN and Rayleigh fading channels of all SNR ranges.

## QoS Estimation for Wireless Video Streaming Based on WiGIG Technology

- **Status**: ❌
- **Reason**: WiGIG 무선 비디오 스트리밍 QoS 추정, LDPC 무관
- **ID**: ieee:8520205
- **Type**: conference
- **Published**: 4-7 Sept. 
- **Authors**: Baliar Volodymir, Olena Mazurkiewicz
- **PDF**: https://ieeexplore.ieee.org/document/8520205
- **Abstract**: As a result of the development of the Internet and overall portability of the user's devices, there is a growing need for streaming such wideband signals as digital video signals in HDTV format and/or HDR UHDTV. At the same time, users tend to use wireless access for such technologies. One of such technologies is Wi-GIG technology used for wireless displays, short range communications and other applications mainly in frequency band 60 GHz. The transmission of MPEG video signals requires the provision of a certain level of QoS. Requirement for QoS in basic standard for Wi-GIG are absent. This article presents the results of the author's research of QoS determination using a technology based on the WiGIG standard. Scientific novelty consists of definition of requirement definition for successful MPEG delivery in 60 GHz. Result of study can be used during radio planning and system resource allocation during implementation WI-GIG technologies for MPEG video application delivery.

## Joint Source-Channel Decoding for MDC-encoded Sources Transmitted Over Relay Systems

- **Status**: ❌
- **Reason**: MDC 소스-채널 결합 디코딩(JSCC) - LDPC는 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:8530486
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Amin Zribi, Tad Matsumoto
- **PDF**: https://ieeexplore.ieee.org/document/8530486
- **Abstract**: This paper presents a new transmission strategy combined with a source and channel coding and decoding method to deliver a source of information to two users requesting different quality-of-service and having different channel states. Source coding operation relies on Multiple Description Coding (MDC) and channel coding uses LDPC codes. To achieve a better quality for the high-quality-requiring user, we consider cooperative communication where another user acts as a relay. We propose a three-dimensions iterative decoding algorithm that exploits the source-relay correlation and the descriptions correlation. We demonstrate how the lossy forwarding process can help the user with bad channel conditions to recover a first quality even at very low source-destination SNRs. If the channel conditions for the second user are fair enough, it is possible to decode the second description, and achieve a very low distortion based on combining the two descriptions. It is also shown that exploiting the residual correlation between the two descriptions can lead to better results especially for medium-to-high SNRs.

## Notice of Removal: Blind Identification of LDPC Codes Based on Decoding

- **Status**: ❌
- **Reason**: Notice of Removal — 초록 'Removed.', 내용 없음
- **ID**: ieee:8941823
- **Type**: conference
- **Published**: 28-30 Sept
- **Authors**: Weinian Wang, Hua Peng, Lei Ji
- **PDF**: https://ieeexplore.ieee.org/document/8941823
- **Abstract**: Removed.

## Rate-Adaptive Polar-Coded Constellation Shaping for Flexible Optical Networks

- **Status**: ❌
- **Reason**: polar 부호 기반 컨스털레이션 셰이핑으로 비-LDPC이며 부호 비의존 이식 디코더 기법 없음
- **ID**: ieee:8535280
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Shajeel Iqbal, Metodi P. Yankov, Søren Forchhammer
- **PDF**: https://ieeexplore.ieee.org/document/8535280
- **Abstract**: We propose a many-to-one constellation shaping method for flexible-rate implicitly punctured polar-coded QAM. The simulation results show 1.5 dB of performance improvement and 80 km to 320 km increase in transmission distance, over the conventionally punctured polar codes.

## Performance Metrics for Communication Systems with Forward Error Correction

- **Status**: ❌
- **Reason**: FEC 성능 메트릭/임계값 논의, 신규 디코더·구성·HW 없음(개념적 메트릭)
- **ID**: ieee:8535432
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/8535432
- **Abstract**: We revisit performance metrics for optical communication systems with FEC. We illustrate the concept of universality and discuss the most widespread performance thresholds. Finally, we show by example how to include FEC into transmission experiments.

## Optimization of Probabilistic Shaping Enabled Transceivers with Large Constellation Sizes for High Capacity Transmission

- **Status**: ❌
- **Reason**: 광통신 트랜시버 DSP/콘스텔레이션 성형 최적화, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:8535393
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Ezra Ip, Yue-Kai Huang, Shaoliang Zhang +7
- **PDF**: https://ieeexplore.ieee.org/document/8535393
- **Abstract**: We study digital signal processing techniques to optimize the back-to-back performance of large probabilistic shaped constellations. We cover joint optimization of LDPC and constellation shaping, CD pre-compensation, clipping and I/Q imbalance compensation.

## Joint Propagation of Continuous Variable Quantum Key Distribution and $18 \times 24.5$ Gbaud PM-16QAM Channels

- **Status**: ❌
- **Reason**: CV-QKD 광채널 공전파 실험, ECC 코드설계/디코더 기여 없음
- **ID**: ieee:8535421
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Tobias A. Eriksson, Takuya Hirano, Georg Rademacher +8
- **PDF**: https://ieeexplore.ieee.org/document/8535421
- **Abstract**: We study the impact of in-band ASE noise on the performance of CV-QKD over 10 km of fiber. We demonstrate co-propagation of CV-QKD and 3.5 Tbit/s classical coherent channels and show stable key generation over 48 hours.

## EXIT Convergence Analysis of BICM-ID Based on High-Dimensional Modulation and Polar-TPC

- **Status**: ❌
- **Reason**: polar turbo product code + HDM EXIT 분석, 비-LDPC 부호이며 부호 비의존 이식 디코더 기법 없음
- **ID**: ieee:8535499
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Toshiaki Koike-Akino, Ye Wang, Keisuke Kojima +2
- **PDF**: https://ieeexplore.ieee.org/document/8535499
- **Abstract**: We analyze polar turbo product codes (TPC) used with high-dimensional modulations (HDM). Our analysis reveals that the polar-TPC can significantly improve performance via iterative HDM demodulation employed across parallel and pipeline TPC decoding, achieving 2 dB gain for 16 dimensions.

## Long-Distance PDM-32QAM 3-Mode Fibre Transmission Over 1000 km Using Hybrid Multicore EDFA/Raman Repeated Amplification with Cyclic Mode Permutation

- **Status**: ❌
- **Reason**: few-mode fibre 장거리 광전송 증폭 실험으로 LDPC ECC 무관
- **ID**: ieee:8535260
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Takayuki Mizuno, Kohki Shibahara, Hirotaka Ono +1
- **PDF**: https://ieeexplore.ieee.org/document/8535260
- **Abstract**: We demonstrate 1000-km long-distance transmission of PDM-32QAM signals over a few-mode fibre transmission line. We employed multicore EDFA and distributed Raman amplification at the repeater in combination with cyclic mode permutation, which improved OSNR and suppressed MDL and DMD impact.

## SDN-Enabled Cross-Layer Flexibility in 5G Fronthaul Networks

- **Status**: ❌
- **Reason**: 5G 프론트홀 SDN 자원할당 프레임워크로 LDPC ECC 기법과 무관
- **ID**: ieee:8535353
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Mingwei Yang, Houman Rastegarfar, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8535353
- **Abstract**: We propose a software-defined resource allocation framework for mobile fronthaul (MFH) applications, combining secure and scalable modulation order and code rate adaptation and dynamic processing resource sharing. Successful transmission within a 34 km cover range is experimentally demonstrated.

## Blind Decoding-Metric Estimation for Probabilistic Shaping via Expectation Maximization

- **Status**: ❌
- **Reason**: 확률 성형용 디코딩 메트릭 EM 추정, 부호 비의존 통신 응용; LDPC BP에 떼어낼 디코더 기법 없음
- **ID**: ieee:8535375
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Fabian Steiner, Patrick Schulte, Georg Böcherer
- **PDF**: https://ieeexplore.ieee.org/document/8535375
- **Abstract**: An unsupervised learning approach based on expectation maximization is proposed to obtain the parameters of a soft decision forward error correction decoding metric for probabilistic shaping. The algorithm depends only on the channel observations and does not require transmitted data.

## Experimental Characterization of $10 \times 8$ GBd DP-1024QAM Transmission with 8-bit DACs and Intradyne Detection

- **Status**: ❌
- **Reason**: DP-1024QAM 광전송 실험 특성화로 LDPC ECC 기여 없음
- **ID**: ieee:8535205
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Edson P. da Silva, Frederik Klejs, Mads Lillieholm +6
- **PDF**: https://ieeexplore.ieee.org/document/8535205
- **Abstract**: We experimentally investigate the transmission of 10×8 GBd DP-1024QAM over full Raman amplified low-loss fiber spans. For multicarrier systems using 8-bit DACs, a record achievable information rate of 15.7 bit/symbol is observed after 200 km using standard intradyne detection.

## Nanosecond-Latency IM/DD/DSB to Coherent/SSB Converter

- **Status**: ❌
- **Reason**: IM/DD-coherent 아날로그 변환기, ECC와 무관
- **ID**: ieee:8535521
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Arthur Lowery, Bill Corcoran
- **PDF**: https://ieeexplore.ieee.org/document/8535521
- **Abstract**: We demonstrate an all-analogue converter from intensity modulated direct-detection double-side-band to field-modulation coherent single-sideband, which is based on the Weaver SSB method. This is designed to interface short-haul datacentre links to coherent metro/long-haul links.

## Achievable Information Rate Losses for High Order Modulation and Hard-Decision Forward Error Correction

- **Status**: ❌
- **Reason**: 고차 변조+경판정 FEC 정보율 손실 이론 분석, 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:8535531
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Alex Alvarado, Yi Lei, David S. Millar
- **PDF**: https://ieeexplore.ieee.org/document/8535531
- **Abstract**: We study the combination of high-order modulation formats and hard-decision FEC from an information rate point of view. It is shown that the relative rate losses are approximately constant for the same FEC overhead when the constellation size increases.

## Schalkwijk-Kailath Feedback Error Correction for Optical Data Center Interconnects

- **Status**: ❌
- **Reason**: Schalkwijk-Kailath 피드백 부호로 LDPC가 아니며 FEC 회피 방식, NAND LDPC에 이식할 기법 없음
- **ID**: ieee:8535184
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Kieran Parsons +1
- **PDF**: https://ieeexplore.ieee.org/document/8535184
- **Abstract**: We investigate capacity-approaching feedback coding without relying on power-hungry forward error correction. For short-reach interconnects, linear feedback codes show a great advantage in computational complexity and latency, achieving net coding gain of 11.4 dB with three-times feedback.

## Merits of Coded Modulation with Probabilistic and Geometrical Shaping

- **Status**: ❌
- **Reason**: 코디드 변조+확률·기하 셰이핑 광전송 응용으로 NAND LDPC에 이식할 ECC 기법 없음
- **ID**: ieee:8535107
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Hussam G. Batshon
- **PDF**: https://ieeexplore.ieee.org/document/8535107
- **Abstract**: The design and merits of multi-dimensional coded modulation with iterative decoding and hybrid constellation shaping are discussed. The paper focuses on how the use of coded modulation enables adaptive non-linear compensation techniques to further improve performance in nonlinear transmission systems.

## 3-Bit Digitized-RoF Retransmission of 12ch 16APSK Broadcast Signals with Improved Nonlinear Compression

- **Status**: ❌
- **Reason**: 위성방송 DRoF 재전송 압축 기법, ECC 무관
- **ID**: ieee:8535578
- **Type**: conference
- **Published**: 23-27 Sept
- **Authors**: Ryota Shiina, Toshihito Fujiwara, Satoshi Ikeda
- **PDF**: https://ieeexplore.ieee.org/document/8535578
- **Abstract**: We achieve 3-bit retransmission of 12ch multiplexed 16APSK broadcast satellite signals having extremely wideband, 38.36 MHz/ch, for 4K/8K-UHD using a DRoF-based video distribution system with new compression technique that offers a 40% cut in the transmission rate.

## Selection Combining in Hybrid RF/FSO Systems for IM/DD and Heterodyne Detection in Varying Weather Conditions

- **Status**: ❌
- **Reason**: 하이브리드 RF/FSO 다이버시티 분석, LDPC 무관한 무선 응용
- **ID**: ieee:8742823
- **Type**: conference
- **Published**: 20-21 Sept
- **Authors**: Vaibhav Sundharam, Shagun Johari
- **PDF**: https://ieeexplore.ieee.org/document/8742823
- **Abstract**: A hybrid RF/FSO scheme that can be deployed to effectively combat the issue of signal fading in pure FSO systems is proposed in this paper. The scheme transmits the same information through the channel at the same data rate, across both RF and FSO links. At the receiver, selection combining scheme is deployed to couple the incoming signals from multiple RF receivers and a single FSO receiver. Taking into consideration the atmospheric path loss and turbulence, the closed loop expression for the Cumulative Distribution Function (CDF) is proposed. Additionally, the closed-form expressions for important performance parameters, such as Outage Probability (OP) and Bit Error Rate (BER) are also formulated, all in terms of Meijer's G function for both the Intensity Modulation/Direct Detection (IM/DD) and Heterodyne Detection techniques.

## PHYSIM - A Physical Layer Simulation Software

- **Status**: ❌
- **Reason**: 물리계층 시뮬레이션 SW 프레임워크, LDPC는 비교 대상일 뿐 신규 기법 없음
- **ID**: ieee:8576187
- **Type**: conference
- **Published**: 2-5 Sept. 
- **Authors**: Florian Jackisch
- **PDF**: https://ieeexplore.ieee.org/document/8576187
- **Abstract**: Modern communication systems use different physical layer (PHY) techniques with diverse performance characteristics. Each PHY configuration option introduces trade-offs for spectral efficiency, robustness, out-of-band emissions, peak-to-average power ratio, and implementation complexity. This paper introduces the cross-platform PHYSIM software framework. PHYSIM can compare established modulations like orthogonal frequency-division multiplexing (OFDM) with modern alternatives, e.g., filter bank multi-carrier, universal filtered multi-carrier, and filtered-OFDM. Additionally, PHYSIM can draw performance comparisons between new coding schemes like polar codes and more established methods like low-density parity-check codes and turbo codes. The PHYSIM graphical user interface (GUI) assists in the design of physical layer parameters. The GUI offers plots to compare the performance of PHY configurations in transmission channels. The plots display the transmitted spectra, the received constellation diagrams, as well as the modulation, bit, and frame error ratios. Hence, the PHYSIM simulation framework assists the designer of a physical layer system and helps to find PHY settings for a target application.

## Joint Crosstalk Avoidance with Multiple Bit Error Correction Coding Technique for NoC Interconnect

- **Status**: ❌
- **Reason**: NoC crosstalk 회피 + Hamming/parity 부호 — 비-LDPC, 이식 가능 LDPC 기법 없음
- **ID**: ieee:8554417
- **Type**: conference
- **Published**: 19-22 Sept
- **Authors**: T Siva Teja, T Sai Kiran, T.V.V Satya Narayana +2
- **PDF**: https://ieeexplore.ieee.org/document/8554417
- **Abstract**: In an On-chip communication where the devices have scaled down to nanometer scale, a single chip contains numerous processing elements and inter-communication between these elements is Network on chip. Glitches in NoC or the disturbances in the physical environment of NoC leads to multiple-bit errors. These leads to the loss of data communicated and may cause need for retransmission. Retransmitted packets create network congestion and heavy traffic. Errors, which are mainly caused by coupling effects, introduce crosstalk. This establishes a need for a coding technique for multiple bit error correction and avoiding crosstalk to form a reliable on-chip communication. In this paper, we propose Joint Crosstalk Avoidance with Multiple bit Error Correction (JCAMEC) coding technique which uses extended Hamming code and simple parity check code along with duplication. Duplicating the encoded bits provides the benefit of avoiding crosstalk. The coding technique in this work is placed in Network Interface (NI) to reduce the hardware overhead involved at every router in case of Hop to Hop error correction. However, to avoid the error propagation an error detector is placed at the router across each port, which consumes less area and power overhead compared to generic coding techniques. Evaluation and analysis is carried out based on the NI critical path delay along with the total power and area. Also, probability of residual error, power consumption and voltage swing of the link are estimated. The results demonstrate that JCAMEC coding technique outperforms the coding techniques considered for comparison and builds NoC with better reliability.

## Analytical Performance Evaluation of a LDPC and STBC Coded FDM FSO Communication System under Turbulent Atmospheric Channel

- **Status**: ❌
- **Reason**: FSO 통신에서 LDPC vs STBC 성능 해석 평가일 뿐 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8628052
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Bobby Barua, S. P. Majumder
- **PDF**: https://ieeexplore.ieee.org/document/8628052
- **Abstract**: Free space Optical (FSO) communication systems are severely laid down with the weather situations. Atmospheric turbulence is one of the essential facts that degrade the overall performance of a FSO system even under smooth sky circumstance. Coding is one of the techniques that may be applied to improve the overall performance of a communication system. Moreover, it's miles very crucial to apply proper coding approach to enhance the performance. This paper affords an analytical method to evaluate the overall performance of LDPC and STBC coded FSO communication system under the impact of strong atmospheric turbulence. Evaluation is done to find the expressions for the output photodetector current and signal to noise power ratio. The average bit error rate is evaluated numerically thinking about gamma-gamma distributions for the atmospheric turbulence. Analytical results show that for similar type of system configuration in FSO, STBC provides better performances than LDPC code.

## Two Countermeasures against Reaction Attacks on LEDApkc and other QC-MDPC and QC-LDPC based McEliece Cryptosystems in ARQ Setting Heuristic Discussion

- **Status**: ❌
- **Reason**: McEliece 암호 reaction attack 대응책으로 보안 응용, 떼어낼 디코더/코드설계 기여 없음
- **ID**: ieee:8555831
- **Type**: conference
- **Published**: 13-15 Sept
- **Authors**: Peter Farkaš
- **PDF**: https://ieeexplore.ieee.org/document/8555831
- **Abstract**: two new countermeasures against reaction attacks on LEDApkc and other similar McEliece cryptosystems using quasi-cyclic low-density parity-check codes and quasi-cyclic moderate density parity-check codes in automatic repeat request setting are presented in this manuscript. In this scenario it is supposed that the attacks are enabled for Eve by gaining information from Bob's decryption failures via negative acknowledgements on the feedback channel used in the automatic repeat request transmission technique. The two countermeasures proposed in this manuscript are trying to make this information needed for the attacks useless or completely unavailable. In the first one this information is camouflaged by stochastically generated negative acknowledgements, which are sent in the feedback channel. In the second, an outer fountain code makes the feedback channel redundant.

## Game-Based Thermal-Delay-Aware Adaptive Routing (GTDAR) for Temperature-Aware 3D Network-on-Chip Systems

- **Status**: ❌
- **Reason**: 3D NoC 열관리 라우팅, LDPC/ECC와 무관
- **ID**: ieee:8306659
- **Type**: journal
- **Published**: 1 Sept. 20
- **Authors**: Kun-Chih Chen
- **PDF**: https://ieeexplore.ieee.org/document/8306659
- **Abstract**: The thermal problem of three-dimensional Network-on-Chip (3D NoC) is proven to be severer than 2D NoC due to the stacking dies and heterogeneous thermal conduction between each silicon layers. To control the system temperature under a certain thermal limit, the current Dynamic Thermal Managements (DTMs) can be classified into temporal approaches and spatial approaches. The temporal DTM approaches reduce the processing speed of those overheated NoC components. However, for emerging cooling consideration, the full throttling scheme is usually applied as the system temperature reaches the alarming level, which results in significant system performance overhead. On the other hand, the spatial DTM approaches migrate the traffic load away from the overheated components. Although the spatial DTM approaches can mitigate the performance impact during the temperature control, the cooling period is longer than the temporal approaches because of the asynchronous phenomenon of traffic and temperature behavior among the NoC components. To consider the advantages of the temporal and spatial DTM approaches, it is necessary to synchronize the information of traffic and temperature behavior in the NoC systems. In this paper, we apply the Game Theory to propose a Game-based Thermal-Delay-aware Adaptive Routing (GTDAR) scheme. The GTDAR first adopts the Thermal-Delay principle to transfer the long-term temperature information to short-term traffic information by allocating the input buffer length of each NoC routers, which can reduce the thermal problem into the traffic problem. Afterward, the GTDAR involves the Nash Equilibrium property to distribute the packet routing to mitigate the thermal problem by considering the traffic and temperature simultaneously. In our experiments, the proposed Game-based Thermal-Delay-aware Adaptive Routing (GTDAR) scheme can help to improve 8.7 percent to 130 percent system performance with only 2.4 percent area overhead compared with the previous works.
