# IEEE Xplore — 2007-12


## Distance Bounds for an Ensemble of LDPC Convolutional Codes

- **Status**: ❌
- **Reason**: LDPC convolutional 앙상블의 최소거리 하한 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4385784
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Arvind Sridharan, Dmitri Truhachev, Michael Lentmaier +2
- **PDF**: https://ieeexplore.ieee.org/document/4385784
- **Abstract**: An ensemble of $(J,K)$ -regular low-density parity- check (LDPC) convolutional codes is introduced and existence-type lower bounds on the minimum distance $d _ {\rm L}$ of code segments of finite length $L$  and on the free distance  $d _{\rm free}$ are derived. For sufficiently large constraint lengths $\nu$ , the distances are shown to grow linearly with $\nu$ and the ratio $d_ {\rm L}/\nu$ approaches the ratio $d _{ {\rm free}}/\nu$  for large $L$ . Moreover, the ratio of free distance to constraint length is several times larger than the ratio of minimum distance to block length for Gallager's ensemble of (J,K)-regular LDPC block codes.

## Analog Iterative LDPC Decoder Based on Margin Propagation

- **Status**: ✅
- **Reason**: Margin propagation 기반 LDPC 디코더 신규 알고리즘으로 min-sum/sum-product 대비 잡음환경 우수, 디코더(C) 이식 가능
- **ID**: ieee:4358645
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Chhay Kong, Shantanu Chakrabartty
- **PDF**: https://ieeexplore.ieee.org/document/4358645
- **Abstract**: A margin propagation (MP) algorithm that can be used for implementing analog decoders for low-density parity check (LDPC) codes is presented. Unlike conventional sum-product analog decoders that rely on translinear operation of transistors, MP decoders use addition, subtraction and threshold operations, and therefore can be mapped onto different analog circuit topologies (current-mode, charge-mode, or nonelectronic circuits). This brief describes salient properties of the MP decoding algorithm and compares its performance to the sum-product and the min-sum (MS) decoding algorithms. Simulation results demonstrate that MP based LDPC decoders achieve nearly an identical bit error rate performance as their sum-product counterparts and achieve superior performance as compared to the MS decoding algorithm. Results presented in this brief also demonstrate that, when messages in LDPC decoding are corrupted by additive noise, the MP decoding algorithm delivers superior performance compared to its sum-product and MS counterparts.

## Quasi-Cyclic Generalized LDPC Codes With Low Error Floors

- **Status**: ✅
- **Reason**: 구조화 QC G-LDPC 신규 코드 설계(LDPC doping, Hamming 컴포넌트로 error floor 저감) - 바이너리 LDPC 코드설계 기법(E)
- **ID**: ieee:4403033
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Gianluigi Liva, William E. Ryan, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/4403033
- **Abstract**: In this paper, a novel methodology for designing structured generalized low-density parity-check (G-LDPC) codes is presented. The proposed design results in quasi-cyclic G-LDPC codes for which efficient encoding is feasible through shift-register-based circuits. The structure imposed on the bipartite graphs, together with the choice of simple component codes, leads to a class of codes suitable for fast iterative decoding. A pragmatic approach to the construction of G-LDPC codes is proposed. The approach is based on the substitution of check nodes in the protograph of a low-density parity-check code with stronger nodes based, for instance, on Hamming codes. Such a design approach, which we call low-density parity-check (LDPC) code doping, leads to low-rate quasi-cyclic G-LDPC codes with excellent performance in both the error floor and waterfall regions on the additive white Gaussian noise channel.

## New Constructions of Quasi-Cyclic LDPC Codes Based on Special Classes of BIBDs for the AWGN and Binary Erasure Channels

- **Status**: ✅
- **Reason**: BIBD 기반 QC-LDPC 신규 구성법, 바이너리 LDPC 코드 설계 기법(E) 이식 가능
- **ID**: ieee:4407817
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Lan Lan, Ying Yu Tai, Shu Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/4407817
- **Abstract**: This paper presents new methods for efficiently constructing encodable quasi-cyclic low-density parity-check (LDPC) codes based on special balanced incomplete block designs (BIBDs). Codes constructed perform well over both the additive white Gaussian noise (AWGN) and binary erasure channels with iterative decoding.

## Use of Low-Density Parity-Check Codes for Dominant Error Events Detection and $k$-Constraint Enforcement

- **Status**: ✅
- **Reason**: QC-LDPC 패리티검사로 dominant error event 검출 신규 기법, NAND ECC 코드설계/디코더 보조에 이식 가능
- **ID**: ieee:4380282
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Fei Sun, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4380282
- **Abstract**: In this paper, we propose to leverage the simple and explicit parity checks inherent in low-density parity-check (LDPC) codes to detect dominant error events without code rate penalty. This is enabled by enforcing a very weak constraint on the LDPC code parity check matrix structure. Such a constraint can be readily satisfied by most structured LDPC codes reported in the open literature, such as quasi-cyclic (QC) LDPC codes. Moreover, this zero-redundancy dominant error events detection can be extended to handle the bit errors that occur when deliberate bit-flipping is used to enforce -constraints. We have demonstrated the effectiveness of the proposed method in computer simulations.

## Area-Efficient Min-Sum Decoder Design for High-Rate Quasi-Cyclic Low-Density Parity-Check Codes in Magnetic Recording

- **Status**: ✅
- **Reason**: 고율 QC-LDPC min-sum 디코더의 면적효율 VLSI 아키텍처 신규 설계(D), NAND ECC HW에 직접 이식 가능
- **ID**: ieee:4380288
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Hao Zhong, Wei Xu, Ningde Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/4380288
- **Abstract**: We report a silicon area efficient method for designing a quasi-cyclic (QC) low-density parity-check (LDPC) code decoder. Our design method is geared to magnetic recording that demands high code rate and very high decoding throughput under stringent silicon cost constraints. The key to designing the decoder is to transform the conventional formulation of the min-sum decoding algorithm in such a way that we can readily develop a hardware architecture with several desirable features: 1) silicon area saving potential inherent in the min-sum algorithm for high-rate codes can be fully exploited; 2) the decoder circuit critical path may be greatly reduced; and 3) check node processing and variable node processing can operate concurrently. For the purpose of demonstration, we designed application-specific integrated circuit decoders for four rate-8/9 regular-(4, 36) QC-LDPC codes that contain 512-byte, 1024-byte, 2048-byte, and 4096-byte user data per codeword, respectively. Synthesis results show that our design method can meet the beyond-2 Gb/s throughput requirement in future magnetic recording at minimal silicon area cost.

## Estimation of Bit and Frame Error Rates of Finite-Length Low-Density Parity-Check Codes on Binary Symmetric Channels

- **Status**: ✅
- **Reason**: 유한길이 LDPC의 BSC 하드결정 디코딩 BER/FER 추정법(최소가중 오류패턴 열거), error floor 분석에 직접 이식 가능(E)
- **ID**: ieee:4395276
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Hua Xiao, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/4395276
- **Abstract**: A method for estimating the performance of low-density parity-check (LDPC) codes decoded by hard-decision iterative decoding algorithms on binary symmetric channels (BSCs) is proposed. Based on the enumeration of the smallest weight error patterns that cannot be all corrected by the decoder, this method estimates both the frame error rate (FER) and the bit error rate (BER) of a given LDPC code with very good precision for all crossover probabilities of practical interest. Through a number of examples, we show that the proposed method can be effectively applied to both regular and irregular LDPC codes and to a variety of hard-decision iterative decoding algorithms. Compared with the conventional Monte Carlo simulation, the proposed method has a much smaller computational complexity, particularly for lower error rates.

## Bounds on the Expansion Properties of Tanner Graphs

- **Status**: ✅
- **Reason**: Tanner 그래프 확장성 하한+stopping distance/redundancy 경계, 바이너리 LDPC 코드설계 기법으로 이식 가능(E)
- **ID**: ieee:4385795
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Mingrui Zhu, Keith M. Chugg
- **PDF**: https://ieeexplore.ieee.org/document/4385795
- **Abstract**: This work focuses on the expansion properties of a Tanner Graph because they are known to be related to the performance of associated iterative message-passing algorithms over various channels. By analyzing the eigenvalues and corresponding eigenvectors of the normalized incidence matrix representing a Tanner Graph, lower bounds on these expansion properties are derived. Specifically, for the binary erasure channel, these results lead to two lower bounds on stopping distance for any given binary linear code and an upper bound on stopping redundancy for the family of difference-set codes (type-I 2-D projective geometry low-density parity-check (LDPC) codes).

## Approaching V-BLAST Capacity With Adaptive Modulation and LDPC Encoding

- **Status**: ✅
- **Reason**: V-BLAST에 LDPC+density evolution 코드설계 및 rate-compatible punctured LDPC 설계 포함, 코드설계 기법 이식 가능(E)
- **ID**: ieee:4395280
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Yan Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4395280
- **Abstract**: This paper presents a practical implementation of the vertical Bell Laboratories layered space-time (V-BLAST) type system, in which the multiple-input multiple-output (MIMO) open-loop capacity can be approached with conventional scalar coding, using adaptive modulation with appropriate channel codes, e.g., low-density parity-check (LDPC) codes and optimum successive detection (OSD). The density evolution technique is employed to determine the maximal achievable rate of an LDPC code for each transmit antenna for a given channel realization at a given signal-to-noise ratio. Numerical results will show that the average sum rate of the adaptively modulated LDPC encoded system is quite close to the V-BLAST capacity with both rate and power adaptations. Considering the performance degradation caused by error propagation due to the imperfect feedback and relatively long decoding delay in the OSD, we use parallel interference cancellation followed by minimum mean square error filtering in the bit error rate (BER) performance simulation. Simulation results will show that a target BER of 10-5 can be achieved by the optimally designed LDPC codes. To simplify the code design, we replace the LDPC codes, optimally designed for each channel realization, with rate-compatible punctured LDPC codes, at the cost of a slight sum rate loss. If the fading process is nonergodic, the outage capacity corresponding to a given outage probability is used to measure the channel performance. As an example, we design the LDPC codes for an adaptively modulated 2times2 V-BLAST system to approach its outage capacity for a given outage probability.

## Sufficient Conditions for Convergence of the Sum–Product Algorithm

- **Status**: ✅
- **Reason**: Sum-Product(BP) 수렴 보장 조건 도출, 부호 비의존적 BP 이론으로 바이너리 LDPC BP 디코더에 이식 가능(C)
- **ID**: ieee:4385778
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Joris M. Mooij, Hilbert J. Kappen
- **PDF**: https://ieeexplore.ieee.org/document/4385778
- **Abstract**: Novel conditions are derived that guarantee convergence of the Sum-Product Algorithm (also known as Loopy Belief Propagation or simply Belief Propagation (BP)) to a unique fixed point, irrespective of the initial messages, for parallel (synchronous) updates. The computational complexity of the conditions is polynomial in the number of variables. In contrast with previously existing conditions, our results are directly applicable to arbitrary factor graphs (with discrete variables) and are shown to be valid also in the case of factors containing zeros, under some additional conditions. The conditions are compared with existing ones, numerically and, if possible, analytically. For binary variables with pairwise interactions, sufficient conditions are derived that take into account local evidence (i.e., single-variable factors) and the type of pair interactions (attractive or repulsive). It is shown empirically that this bound outperforms existing bounds.

## Information Theoretic Foundations of Adaptive Coded Modulation

- **Status**: ❌
- **Reason**: 적응변조 정보이론 튜토리얼, LDPC는 부수 언급일 뿐 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4383372
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Giuseppe Caire, K. Raj Kumar
- **PDF**: https://ieeexplore.ieee.org/document/4383372
- **Abstract**: In wireless/mobile communications, terminals adapt their rate and transmit power or, more in general, their coding and modulation scheme, depending on the time-varying channel conditions. This paper presents, in a tutorial form, the information theoretic framework underlying such “adaptive modulation” techniques. First, we review fading channel models, channel state information assumptions, and related capacity results. Then, we treat the case of input power constraint, where the optimal input distribution is Gaussian. Finally, we address the case of discrete modulations. In order to treat the latter, we make use of the recently developed method of “mercury-waterfilling,” based on the relationship between mutual information and minimum mean-square error (MMSE) estimation of the channel input from the channel output. While the traditional design of adaptive modulation schemes based on uncoded bit-error rate (BER) involves the optimization over a discrete set of signal constellations, when powerful (i.e., capacity approaching) coding schemes are used the corresponding adaptive coded modulation design becomes surprisingly simple. The regime of very powerful coding is justified by the use of modern coding schemes, such as turbo codes and low-density parity-check codes, able to perform close to channel capacity at very small BER.

## A Computationally Efficient Multilevel Coding Scheme for ISI Channels

- **Status**: ❌
- **Reason**: ISI 채널용 다중레벨 코딩+MMSE 등화기 수신구조, LDPC 비의존이며 NAND LDPC ECC에 이식할 기법 없음
- **ID**: ieee:4385777
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Mei Chen, Teng Li, Oliver M. Collins
- **PDF**: https://ieeexplore.ieee.org/document/4385777
- **Abstract**: This paper proposes a multilevel coding scheme with linear mapping for intersymbol interference (ISI) channels and derives a low-complexity receiver structure that can achieve the ISI channel capacity. The transmitter superimposes many layers of independent binary antipodal streams to generate a quadrature amplitude modulation (QAM) or Gaussian-like channel input. The receiver performs multistage decoding with decision feedback and interference cancellation. Within each stage is a linear minimum mean-square-error (MMSE) equalizer followed by an error-correcting decoder. The complexity scales linearly with the channel length and the number of layers, and the process is shown to be asymptotically information lossless if a fixed input power is properly distributed over a sufficiently large number of layers. This framework is then extended to achieve the capacity of the ISI channel using a transmitter-side spectral shaping filter that converts a Gaussian input sequence with a white spectrum to one with a water-filling spectrum.

## A Unified Approach to the Performance Analysis of Speed-Estimation Techniques in Mobile Communication

- **Status**: ❌
- **Reason**: 모바일 속도/도플러 추정 기법 성능분석, LDPC 무관
- **ID**: ieee:4403030
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Ali Abdi, Hong Zhang, Cihan Tepedelenlioglu
- **PDF**: https://ieeexplore.ieee.org/document/4403030
- **Abstract**: The estimation of the mobile speed, or equivalently, the maximum Doppler frequency, is of importance in a variety of applications in wireless mobile communications. In this paper, a unified framework for the performance analysis of several major speed-estimation techniques is presented, which allows a fair comparison between all the methods, analytically. Interestingly, it is proved that all these methods are equivalent, asymptotically, i.e., for large observation intervals. In addition, we have derived closed-form expressions for the bias and variance of a recently proposed covariance-based method. We have also introduced a new estimator that relies on the average number of maxima of the inphase component, and have calculated its variance, analytically. Our extensive performance analysis, supported by Monte Carlo simulations, have revealed that depending on the channel condition and the observation interval, one needs to use a crossing- or a covariance-based technique, to achieve the desired estimation accuracy over a large range of mobile speeds.

## Toward a unified framework for modeling and analysis of diversity in joint source - channel coding

- **Status**: ❌
- **Reason**: JSCC diversity 모델링 프레임워크, LDPC가 베이스라인이며 떼어낼 ECC 기법 없음
- **ID**: ieee:4403031
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Andres Kwasinski, K.J. Ray Liu
- **PDF**: https://ieeexplore.ieee.org/document/4403031
- **Abstract**: The study of joint source-channel Coding (JSCC) systems faces one major challenge in obtaining an analytical expression for the function that links end-to-end distortion with channel signal-to-noise ratio, the D-SNR curve. In this paper, for certain multimedia systems using practical source and channel codes in a JSCC bit rate allocation design, the D-SNR curve is shown to be well approximated by a set of carefully selected points where the relative contribution of channel errors to end-to-end distortion is small. This approach has the potential advantage that it could be applied to represent the performance of many practical systems using JSCC bit rate allocation for which it is shown that the D-SNR function is approximately linear in log-log scales. A unified framework for the modeling, analysis, and performance measurement of these systems is proposed by considering a view of diversity more general than its usual interpretation. This view extends that of diversity to include redundant information so that coding and diversity gain are still used to characterize performance. Furthermore, the proposed approach is applied to study issues arising from using practical source and channel codes, including the effects on the performance of channel codes of different strength or source codes with different compression efficiency.

## Two Algorithms for Constructing Efficient Huffman-Code-Based Reversible Variable Length Codes

- **Status**: ❌
- **Reason**: RVLC(reversible variable length code) 구성 알고리즘으로 비-LDPC 소스/엔트로피 코딩, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4403032
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Chia-Wei Lin, Ja-Ling Wu, Yuh-Jue Chuang
- **PDF**: https://ieeexplore.ieee.org/document/4403032
- **Abstract**: In this paper, Huffman-code-based reversible variable length code (RVLC) construction algorithms are studied. We use graph models to represent the prefix, suffix, and Hamming distance relationships among RVLC candidate code words. The properties of the so-obtained graphs are investigated in detail, based on which we present two efficient RVLC construction algorithms: Algorithm 1 aims at minimizing the average code word length while Algorithm 2 jointly minimizes the average code word length and maximizes the error-detection probability at the same time.

## A Fully Integrated MIMO Multiband Direct Conversion CMOS Transceiver for WLAN Applications (802.11n)

- **Status**: ❌
- **Reason**: WLAN 802.11n MIMO CMOS 트랜시버 회로, LDPC 무관 RF 응용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:4381436
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Arya Behzad, Keith A. Carter, Hung-Ming Chien +24
- **PDF**: https://ieeexplore.ieee.org/document/4381436
- **Abstract**: 802.11n is the latest offering from the IEEE standard committee tasked with enabling and enhancing WLAN systems. This standard utilizes several techniques to offer a much larger rate versus range than the legacy WLAN systems. A single-chip multiband direct-conversion CMOS MIMO transceiver (2times2) targeted for WLAN applications is presented. This transceiver is capable of satisfying the requirements of the draft 802.1 In standard and achieves PHY rates of > 270 Mb/s. The receivers and transmitters achieve an EVM of better than -41 dB (0.9%) and -40 dB (1.0%) operating in legacy g and a modes, respectively. From a 1.8 V supply and with both cores operating, the chip draws 275 mA in RX mode and 280 mA in TX mode.

## Reduced-Complexity BCJR Algorithm for Turbo Equalization

- **Status**: ❌
- **Reason**: turbo equalization용 BCJR(트렐리스) 감소복잡도 알고리즘, LDPC BP에 이식되지 않는 비-LDPC 디코더
- **ID**: ieee:4395266
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Dario Fertonani, Alan Barbieri, Giulio Colavolpe
- **PDF**: https://ieeexplore.ieee.org/document/4395266
- **Abstract**: We propose novel techniques to reduce the complexity of the well-known Bahl, Cocke, Jelinek, and Raviv (BCJR) algorithm when it is employed as a detection algorithm in turbo equalization schemes. In particular, by also considering an alternative formulation of the BCJR algorithm, which is more suitable than the original one for deriving reduced-complexity techniques, we describe three reduced-complexity algorithms, each of them particularly effective over one of the three different classes of channels affected by intersymbol interference (minimum-phase, maximum-phase, and mixed-phase channels). The proposed algorithms do not explore all paths on the trellis describing the channel memory, but they work only on the most promising ones, chosen according to the maximum a posteriori criterion. Moreover, some optimization techniques improving the effectiveness of the proposed solutions are described. Finally, we report the results of computer simulations showing the impressive performance of the proposed algorithms, and we compare them with other solutions in the literature.

## Max-Product Algorithms for the Generalized Multiple-Fault Diagnosis Problem

- **Status**: ❌
- **Reason**: 다중고장진단 max-product 알고리즘, 채널 LDPC ECC가 아닌 진단그래프 추론으로 떼어낼 ECC 기법 없음
- **ID**: ieee:4362694
- **Type**: journal
- **Published**: Dec. 2007
- **Authors**: Tung Le, Christoforos N. Hadjicostis
- **PDF**: https://ieeexplore.ieee.org/document/4362694
- **Abstract**: In this paper, we study the application of the max-product algorithm (MPA) to the generalized multiple-fault diagnosis (GMFD) problem, which consists of components (to be diagnosed) and alarms/connections that can be unreliable. The MPA and the improved sequential MPA (SMPA) that we develop in this paper are local-message-passing algorithms that operate on the bipartite diagnosis graph (BDG) associated with the GMFD problem and converge to the maximum a posteriori probability (MAP) solution if this graph is acyclic (in addition, the MPA requires the MAP solution to be unique). Our simulations suggest that both the MPA and the SMPA perform well in more general systems that may exhibit cycles in the associated BDGs (the SMPA also appears to outperform the MPA in these more general systems). In this paper, we provide analytical results for acyclic BDGs and also assess the performance of both algorithms under particular patterns of alarm observations in general graphs; this allows us to obtain analytical bounds on the probability of making erroneous diagnosis with respect to the MAP solution. We also evaluate the performance of the MPA and the SMPA algorithms via simulations, and provide comparisons with previously developed heuristics for this type of diagnosis problems. We conclude that the MPA and the SMPA perform well under reasonable computational complexity when the underlying diagnosis graph is sparse.

## An Adaptive Packet Repeat Proposal RB_IR_HARQ Scheme based on LDPC code

- **Status**: ❌
- **Reason**: LDPC 기반 적응형 HARQ 재전송 throughput 개선, 무선 응용, NAND 이식 기법 없음
- **ID**: ieee:4426236
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Ning He, Hong Wen, ShuYa Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/4426236
- **Abstract**: In this paper, we propose a new adaptive HARQ scheme based on LDPC codes by observing the reliability and the relations between reliability and BLER with different code rate. The results of the simulations show that this scheme can achieve higher throughput and lower time delay, and that it doesn't increase the complexity of the system.

## A Combining Decoding Method of LDPC Codes for HARQ

- **Status**: ❌
- **Reason**: HARQ 다중패킷 결합 디코딩(최소거리 기준), 페이딩채널 throughput, 무선 응용 특이적
- **ID**: ieee:4426243
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Zhiping Shi, Liang Zhou
- **PDF**: https://ieeexplore.ieee.org/document/4426243
- **Abstract**: This paper proposes a new combining decoding method for low density parity check codes in the multiple received packets combining used in HARQ, which is based on the minimum distance criterion. Simulation results show that the new combining methods outperform the conventional chase combining over fading channel in terms of throughput.

## Link Adaptation of LDPC Codes Based on Exponential Effective-SNR Mapping Link Quality Model

- **Status**: ❌
- **Reason**: LDPC-OFDM 링크적응 EESM 모델, 무선 통신 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:4426238
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Wei Sun, Xiang Chen, Zesong Fei +1
- **PDF**: https://ieeexplore.ieee.org/document/4426238
- **Abstract**: To improve the flexibility and accuracy of link adaptation (LA) of LDPC coded OFDM system, the classical exponential effective-SNR mapping (EESM) link quality model is extended to LDPC codes. Theoretical analysis and simulation results indicate that by selecting proper modulation and coding adjusting factors, the EESM model is precise for LDPC codes, both in terms of complexity and accuracy for various modulation and coding schemes (MCS), sub- channel states and coding block lengths. Therefore it can be treated as an accurate link to system (L2S) interface for LDPC coded multi-carrier system. To verify it, a new LA scheme based on LDPC codes specified in IEEE802.16e standard is presented. Based on the EESM model, the link-level performance of BPSK over additional white Gaussian noise (AWGN) channel is used to predict the throughput performances of the LA scheme, which match the simulation results very well.

## An Ordered HARQ Scheme for LDPC-Coded OFDM System

- **Status**: ❌
- **Reason**: LDPC-OFDM HARQ 재전송 스케줄링, 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:4426232
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Xuehua Li, Zhensong Li, Yiqing Cao +1
- **PDF**: https://ieeexplore.ieee.org/document/4426232
- **Abstract**: In this paper, an ordered Hybrid ARQ(HARQ) scheme for LDPC-coded OFDM system is presented , in which the important bits with large degrees have high retransmission priorities and are mapped to the sub-carriers with better CQI levers in OFDM system. The new scheme considers the degree distribution property of LDPC codes and improved the system performance by providing the important bits with more protection. The performance of the new scheme has been investigated by the Gaussian Approximation (GA). The analysis and simulation results prove that the new scheme is practical because it has better performance with low system complexity.

## The New Decoding Method of Rate Compatible LDPC Codes Based on the IR-HARQ Schemes

- **Status**: ❌
- **Reason**: IR-HARQ rate-compatible LDPC 재전송 디코딩, 무선 HARQ 응용, NAND 채널 ECC 기법 아님
- **ID**: ieee:4426241
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Shuya Yang, Hong Wen, Ning He +1
- **PDF**: https://ieeexplore.ieee.org/document/4426241
- **Abstract**: This paper proposes a new decoding method based on IR_HARQ scheme that uses rate-compatible LDPC codes as the FEC codes. And it can use the former decoding result, which can improve the performance of decoding scheme. This paper also evaluates the new decoding method by simulation. The results show that better performance both on system throughput and iterative times can be obtained.

## Constructing double- and triple-erasure-correcting codes with high availability using mirroring and parity approaches

- **Status**: ❌
- **Reason**: B후보지만 double/triple erasure 미러링+패리티 디스크 어레이 코드, LDPC 아닌 erasure 코드라 떼어낼 BP 기법 없음
- **ID**: ieee:4447715
- **Type**: conference
- **Published**: 5-7 Dec. 2
- **Authors**: Gang Wang, Xiaoguang Liu, Sheng Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/4447715
- **Abstract**: With the rapid progress of the capacity and slow pace of the speed/MTTF of hard disks, and increasing size of storage systems, the reliability and availability of storage systems become more and more serious. This paper discusses the method of constructing double- and triple-erasure-correcting codes via combining mirroring and parity approaches in details, and presents a double-erasure code MPDC and a triple-erasure code MPPDC based on one-factorizations of complete graphs. The two codes are simple, easy to implement, and have no disk number limitation. They achieve perfect fault-free load balance and approximately optimal reconstruction load balance. The simulation results show that, compared with other double- and triple-erasure codes, MPDC and MPPDC have comparative light-load and moderate-load performance and better heavy-load performance in fault-free mode. Because parity declustering is used, the two codes are far superior to the other double- and triple-erasure codes in degraded- and reconstruction-mode performance.

## High throughput encoder architecture for DVB-S2 LDPC-IRA codes

- **Status**: ✅
- **Reason**: DVB-S2 LDPC-IRA 인코더 FPGA HW 아키텍처(병렬 패리티 계산) — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:4497709
- **Type**: conference
- **Published**: 29-31 Dec.
- **Authors**: Marco Gomes, Gabriel Falcao, Alexandre Sengo +3
- **PDF**: https://ieeexplore.ieee.org/document/4497709
- **Abstract**: Due to their excellent bit-error-rate performance, low density parity check codes (LDPC) have been adopted by the recent digital video satellite broadcast standard (DVB-S2). In order to simplify the encoding procedure, irregular repeat and accumulate (IRA) LDPC codes have been chosen. This paper proposes an efficient, low delay and high throughput encoder architecture shared by all DVB-S2 LDPC-IRA codes. The architecture explores the periodic structure of the adopted codes by performing on the fly partial-parallel computation of the parity check bits. The architecture implementation on a XC2VP30 Virtex2P Xilinx FPGA (@131.7 MHz) shows a minimum throughput of 5.93 Gb/s in worst case conditions. Synthesis results are also presented.

## Quasi-cyclic LDPC codes based on D and Q matrices through progressive edge growth

- **Status**: ✅
- **Reason**: 수정 PEG 기반 QC-LDPC 구성(D/Q matrix, permutation vector)으로 바이너리 QC-LDPC 코드 설계 기법(E)
- **ID**: ieee:4445811
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: Wei Zhan, Guangxi Zhu, Li Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/4445811
- **Abstract**: We propose a general method for constructing regular and irregular quasi-cyclic LDPC codes based on the modified PEG (progressive edge growth) graph. The idea of permutation vector is introduced. Through permutation vectors, the QC-LDPC codes based on arbitrary circulant permutation matrices, which are not limited to identity matrix, Q-matrix or D-matrix, can be generated with flexible parameters such as block length, code rate, degree distribution. Simulation results demonstrate that QC-LDPC codes using the new PEG algorithm show an error correction performance comparable to the random LDPC codes based on the traditional PEG algorithm. In addition, the PEG QC-LDPC codes have more hardware-friendly parity check matrices than the random PEG LDPC codes and can fulfill linear-time encoding. The QC-LDPC codes based on D-matrix and Q-matrix are more suitable to be used in QC-LDPC codes than identity matrix because they outperform that of identity matrix by 0.1-0.2 dB in the new PEG algorithm.

## Asymptotic performance analysis of LDPC coded iterative multi-user detection schemes with EXIT charts

- **Status**: ❌
- **Reason**: LDPC 코드 멀티유저 검출 EXIT chart 점근 성능분석, 무선 응용 특이적이고 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:4446006
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: Dongchang Hu, Lin Wang, Qinfang Wei
- **PDF**: https://ieeexplore.ieee.org/document/4446006
- **Abstract**: The threshold determinations of system parameters in LDPC coded multi-user detection algorithm are investigated with EXIT Charts in this paper. It is showed that the tolerable maximal cross correlation coefficient of the iterative detection algorithm is about 0.7, and under the proper cross correlation coefficient it is found that the minimum signal to noise ratios (SNR) converges with the user number in the cell, which indicates the successful cancellation of the MAI among users. Simulation results also show the minimum signal to noise ratios’ linear increases with the code rate, which illuminates that the code rate will have more influence on the system performance once the cross correlation matrix is fixed

## Graph representations of BCH codes in frequency domain

- **Status**: ❌
- **Reason**: BCH 코드 주파수영역 그래프/트렐리스 표현, 비-LDPC이고 BP에 이식 가능한 부호 비의존 기법 없음
- **ID**: ieee:4445809
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: H.S. Wang, G.H. Zeng
- **PDF**: https://ieeexplore.ieee.org/document/4445809
- **Abstract**: A trellis and a Wiberg-like graph for a Bose-Chaudhuri-Hochquenghem (BCH) code in frequency domain are proposed and thus the concept of codes defined on graphs is extended from time domain to frequency domain. And a decoding algorithm on trellis in frequency domain is presented by introducing a concept of syndrome trellis. Finally, Comparisons of graph representations of BCH codes in time domain and frequency domain are also discussed.

## Performance of Q-ary PCGC based on PEG algorithm

- **Status**: ❌
- **Reason**: PCGC을 GF(4)/GF(q) 비이진으로 설계, 비이진 LDPC는 제외 대상
- **ID**: ieee:4445808
- **Type**: conference
- **Published**: 28 Nov.-1 
- **Authors**: Xiang Yang, Lin Wang, Yong Li
- **PDF**: https://ieeexplore.ieee.org/document/4445808
- **Abstract**: PCGC (Parallel Concatenated Gallager Codes) are a new class of concatenated codes based on component LDPC codes. They show the low complexity of encoding while maintaining a good performance compare to LDPC codes. In this paper we investigate the performance of q-ary PCGC scenario, and the PEG (Progressive Edge-Growth) algorithm is introduced into the design of component parity check matrix. Simulation results show that q-ary PCGC with proper component design on GF(4) are better than the comparable LDPC codes at the short lengths. Meanwhile it is found that PCGC on GF(4) also outperform PCGC on GF(2) with analogous complexity. Finally it is seen that q-ary PCGC can be optimized further through proper component design on GF(q).

## Joint network and channel coding for cooperative networks

- **Status**: ❌
- **Reason**: 협력 네트워크 joint network-channel coding(Tanner+sum-product) — 네트워크코딩 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4665225
- **Type**: conference
- **Published**: 2-5 Dec. 2
- **Authors**: Sarah J. Johnson, Christopher M. Kellett
- **PDF**: https://ieeexplore.ieee.org/document/4665225
- **Abstract**: In this paper we propose joint network and channel coding schemes for cooperative networks. The joint decoding schemes require no adjustment to either the sending or intermediary network nodes, but are achieved by describing joint network code / channel code Tanner graphs at the receiving node and applying iterative sum-product decoding. The performance of the proposed schemes are simulated on a simple ldquobutterflyrdquo network and very promising results are obtained.

## Dual Mode PCGCs For Advanced Wireless Communications Networks

- **Status**: ❌
- **Reason**: PCGC(parallel concatenated Gallager codes) 무선용 turbo/단일행렬 디코딩. 부호 비의존적 이식 기법 불명확한 응용 특이적 연접부호
- **ID**: ieee:4437415
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Hatim M. Behairy
- **PDF**: https://ieeexplore.ieee.org/document/4437415
- **Abstract**: Parallel concatenated Gallager codes (PCGCs) are presented in two different modes of decoding. The turbo decoding mode is proposed for long, delay sensitive applications to reduce the decoding complexity, while the single matrix decoding may be used for short data oriented applications in advanced wireless communications networks. Techniques for the design, analysis, and convergence predictions of PCGCs are discussed.

## Performance analysis of 802.11n wireless LAN physical layer

- **Status**: ❌
- **Reason**: 802.11n WLAN PHY MIMO/OFDM 성능분석, 컨볼루션 인코더 대체 검토 - 떼어낼 LDPC 기법 없음
- **ID**: ieee:4475664
- **Type**: conference
- **Published**: 16-18 Dec.
- **Authors**: Amr M. Otefa, Namat M. ElBoghdadly, Essam A. Sourour
- **PDF**: https://ieeexplore.ieee.org/document/4475664
- **Abstract**: In the last few years, we have seen an explosive growth of wireless LAN deployments in both the business and consumer environments. The latest WLAN standard, currently in draft version, is labeled 802.11n. It is based on multiple-input multiple-output (MIMO) antenna technology combined with Orthogonal Frequency Division Multiplexing (OFDM). MIMO is concerned with spatial diversity and Space-Time Block Coding techniques, which distribute the data signal over several transmit and receive antennas to increase the raw PHY layer data rates to near 600 Mbps, and/or significantly enhance performance in terms of bit error rate (BER). Hence we have set our goals in this research to simulate an 802.1 In system in a fading channel, compare the performance of different MIMO modes and channel bandwidths, and study replacing the standard convolutional encoder.

## A 1.45Gb/s (576,288) LDPC Decoder for 802.16e standard

- **Status**: ✅
- **Reason**: 802.16e LDPC 디코더지만 reordered decoding scheme+이중 코드워드 동시처리로 CNU/BNU 100% 활용 HW 아키텍처 신규 기여(D)
- **ID**: ieee:4458033
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/4458033
- **Abstract**: In this work, a (576,288) LDPC decoder for 802.16e standard is presented. This design is a partially parallel architecture based on a new optimally reordered decoding scheme. Besides, the proposed architecture handles two different code words at a time to achieve 100% utilization rate of both CNU and BNU. As a result, high throughput and low hardware complexity are achieved. In chip implementation, the proposed design achieves a data rate of 1.45 Gb/s with 10 iterations and 7 quantization bits, at the cost of 881K gates, based on UMC 0.18μm process technology.

## A Systematic Optimized Comparison Algorithm for Fast LDPC Decoding

- **Status**: ✅
- **Reason**: CNU 비교연산 최적 합성 알고리즘으로 임계경로 단축+비교기 최소화하는 HW 설계 기법(D), NAND LDPC 디코더 이식 가능
- **ID**: ieee:4458034
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Jui-Hui Hung, Sau-Gee Chen
- **PDF**: https://ieeexplore.ieee.org/document/4458034
- **Abstract**: This paper proposes a novel systematic optimization algorithm for comparison operations required by a check node unit (CNU) in LDPC decoding, given any input number Nin. The algorithm can automatically synthesize an optimized fast comparison operations that guarantees a shortest comparison delay time of [log2 (Nm-1)]Tcmp and a minimized total number of two-input comparators, where Tcmp is the delay time of a comparator. High speed is achieved by adopting parallel divide-and-conquer comparison operations, while the required comparators are minimized by developing a novel set construction algorithm that maximizes shareable comparison operations. The designed CNU is favourable to the existing CNU designs which are non-systematically designed with either longer critical path delays or higher comparator counts than the proposed designs. The proposed design is particularly good for long code length cases, when it is impractical to do customized optimized designs by hand, due to high design complexity.

## Constructing Quasi-Cyclic LDPC codes Using a Search Algorithm

- **Status**: ✅
- **Reason**: QC-LDPC 탐색 기반 구성 알고리즘, 4-cycle 회피+girth/rate/length 유연성 제시하는 바이너리 코드설계 기법(E)
- **ID**: ieee:4458089
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Gabofetswe Malema
- **PDF**: https://ieeexplore.ieee.org/document/4458089
- **Abstract**: This article presents a search algorithm for constructing regular and irregular quasi-cyclic LDPC codes. Code rows and columns are divided into j (column weight) and k (row-weight) or more groups respectively. Rows or columns in a group are connected to the same group and in order of appearance. Grouping of rows and columns forms sub-matrices. The sequential row-column connections order creates a cyclic structure in sub-matrices. The row-column constraint is observed to avoid four-cycles. The proposed algorithm is flexible compared to other methods. It obtains codes over a wide range of girths, rates and lengths. Bit-error rate simulations show that obtained codes have good performance with randomly searched codes performing better that sequentially searched codes.

## An Energy Saving Scheme for Long Range and High Data Rate Wireless Sensor Networks

- **Status**: ❌
- **Reason**: WiMAX PHY+센서노드 에너지 절감 통합 설계, LDPC는 부수 언급이고 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4458162
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: Li-Hsieh Lin, Wen-An Tsou, Long-Sheng Fan +2
- **PDF**: https://ieeexplore.ieee.org/document/4458162
- **Abstract**: For increasing demands on transceiving coverage, reliability and high resolution of sensing data in modern wireless sensor network applications, a novel digital transceiver scheme for wireless sensor node with integration of WiMAX PHY, QoS, and low-density parity check (LDPC) code had been proposed. It will be 67% energy saving to support high gain sensing amplifier thus to provide high resolution digitization of sensing data. With WiMAX based regulation, 30 mile transmission range and 74 Mbps data rate for long range and high data rate wireless sensor networks can be achieved.

## Iterative Threshold Decoding of One Step Majority Logic Decodable block Codes

- **Status**: ❌
- **Reason**: OSMLD 블록코드의 APP threshold 반복디코딩, LDPC가 아닌 majority-logic 부호 대상이라 비-LDPC 원칙 제외
- **ID**: ieee:4458188
- **Type**: conference
- **Published**: 15-18 Dec.
- **Authors**: M. Lahmer, M. Belkasmi, F. Ayoub
- **PDF**: https://ieeexplore.ieee.org/document/4458188
- **Abstract**: In this paper an iterative decoding of one step majority logic decodable (OSMLD) block codes is studied. We use a soft-in soft-out of APP threshold algorithm which is able to decode theses codes nearly as well as belief propagation (BP) algorithm. The Computation time of the proposed algorithm is very low and good performance results are obtained on both AWGN and Rayleigh fading channels. A comparison of the proposed algorithm and BP algorithm is also presented. We succeed to apply EXIT chart technique to our iterative process.

## A new class of non-binary LDPC codes design based on inverse block jacket matrices

- **Status**: ❌
- **Reason**: non-binary LDPC(Jacket 행렬 기반) - 비이진 LDPC 제외 대상
- **ID**: ieee:4786362
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Xueqin Jiang, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/4786362
- **Abstract**: In this paper, we will introduce a new kind of non-binary LDPC Codes in communication systems. We evaluate the performance of the new LDPC codes over an AWGN channel. This new LDPC Codes are constructed based on the Jacket matrics. Codes of this class have girth at least 6. They perform very well with iterative decoding.

## Comparison of Gaussian channel with Rayleigh fading channel over LDPC-DPC transmission scheme

- **Status**: ❌
- **Reason**: LDPC-DPC dirty paper coding 무선 응용, 표준 LDPC 사용, 채널 비교만 - 떼어낼 신규 기법 없음
- **ID**: ieee:4786363
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Subash Shree Pokhrel, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/4786363
- **Abstract**: The dirty paper channel model indicates that lossless precoding is theoretically possible at any signal-to-noise ratio (SNR). In this paper, we propose a transmission scheme for dirty-paper coding using Low Density Parity Check (LDPC) codes and compare the performance between Gaussian and Rayleigh fading channels. The simulation results show that LDPC codes are good coding schemes over Gaussian channel using LDPC-DPC transmission scheme in multiuser communication systems.

## Coded SC-FDE system over impulsive noise channels

- **Status**: ✅
- **Reason**: 임펄스 잡음 채널에 대한 LDPC simplified decoding 제안 - 디코더 변형(C) 가능성으로 살림
- **ID**: ieee:4786391
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Ying-hao Qi, bo Wang, Pei-wei Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/4786391
- **Abstract**: Single carrier transmission with cyclic prefix (SC-CP or SC-FDE), has lower PAPR (peak to average power ratio) problem and requires smaller backoff of amplifier than orthogonal frequency division multiplexing (OFDM) technique. In order to combat impulsive noise under power limited channels, we apply regular LDPC (Low Density Parity Check) codes and propose a simplified decoding method. Also We compare the system with and without CP combining under uncoded and coded case. Simulation results show that the proposed method is effective under impulsive noise channels.

## Distributed minimum cost multicasting with lossless source coding and network coding

- **Status**: ❌
- **Reason**: 네트워크 코딩+무손실 소스코딩 멀티캐스트 - 채널 ECC 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4434962
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Tao Cui, Tracey Ho, Lijun Chen
- **PDF**: https://ieeexplore.ieee.org/document/4434962
- **Abstract**: In this paper, we consider minimum cost lossless source coding for multiple multicast sessions. Each session comprises a set of correlated sources whose information is demanded by a set of sink nodes. We propose a distributed end-to-end algorithm which operates over given multicast trees, and a back-pressure algorithm which optimizes routing and coding over the whole network. Unlike other existing algorithms, the source rates need not be centrally coordinated; the sinks control transmission rates across the sources. With random network coding, the proposed approach yields completely distributed and optimal algorithms for intra-session network coding. We prove the convergence of our proposed algorithms. Some practical considerations are also discussed. Experimental results are provided to complement our theoretical analysis.

## Coded π/2 phase shift NS-QAM modulation and its iterative decoding

- **Status**: ❌
- **Reason**: NS-QAM 변조+RSC 외부부호 반복복호 - 비-LDPC, 변조/turbo 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:4786317
- **Type**: conference
- **Published**: 12-14 Dec.
- **Authors**: Changqing Liu, Yu Zhang, Jian Song +2
- **PDF**: https://ieeexplore.ieee.org/document/4786317
- **Abstract**: In this paper, a novel π/2 phase shift non-square (NS) 22n+1-ary (n≥1) quadrature amplitude modulation (QAM) scheme is presented. The modulated signal of this scheme has lower peak-average power ratio (PAPR) than conventional QAM signal by removing all 180° phase shift between adjacent constellation points, so it can mitigate the impact of channelnonlinearity on the signal spectrum. In addition, such modulation scheme contains inherent memory, which can be treated as a type of inner coding. When concatenated with simple outer codes, iterative decoding schemes can be adopted for the system. Simulation results show that this modulation scheme has much lower spectrum regrowth when passing through nonlinear channel, while the coded systems which adopt Recursive System Code (RSC) as outer code can achieve better coding gains than some other coded QAM systems in both additive white Gaussian noise (AWGN) and nonlinear channels.

## Design and performance of LDPC codes extended with parity-check symbols from a larger alphabet

- **Status**: ❌
- **Reason**: mixed integer residue ring(Z_m) 위 비이진 LDPC 확장(zero divisor 엣지가중)으로 바이너리 LDPC 아님, 제외
- **ID**: ieee:4449724
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Elisa Mo, Marc A. Armand
- **PDF**: https://ieeexplore.ieee.org/document/4449724
- **Abstract**: This paper describes a method for constructing a certain class of LDPC codes over mixed integer residue rings. These codes are essentially extended LDPC codes where the additional redundant symbols come from a larger alphabet. In particular, we address the effects that zero divisors as edge weights in the Tanner graph of LDPC codes over Z, have, from the pseudocodeword perspective. First, we show that weighting certain edges of a Tanner graph with zero divisors of Z, can reduce the number of pseudocodewords arising from its finite degree covers. Second, we prove that in adding a redundant row to a given parity-check matrix, the smaller the number of zero divisors it contains, the more effective it is in constricting the corresponding fundamental polytope. Moreover, we argue that cycles of length four are not bad provided at least one of the four corresponding edge weights is a zero divisor. The culmination of these findings is a procedure for judiciously adding redundant check nodes to the Tanner graph representation of a mixed- alphabet code such that significant performance improvements under iterative decoding may be obtained.

## Architecture of the modified Block-Type Low-Density parity-check code decoding design

- **Status**: ✅
- **Reason**: modified B-LDPC(QC-LDPC) 비대칭 패리티행렬 분포+non-overlapping BNU/CNU min-sum 디코더 아키텍처로 코드설계/HW 기여(D/E)
- **ID**: ieee:4449728
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Kuang-Hao Lin, Robert C. Chang, Sheng-Dong Wu
- **PDF**: https://ieeexplore.ieee.org/document/4449728
- **Abstract**: In this paper, a combined Low-Density Parity-Check (LDPC) code decoding design method, called modified Block-Type LDPC (B-LDPC), for realistic LDPC coding system architectures is presented. The B-LDPC code, which is a special class of quasi-cyclic LDPC (QC-LDPC), has an efficient encoding algorithm owing to the simple structure of their parity-check matrices. A proposed distribution of irregular parity-check matrix for the modified B-LDPC is developed so that we can obtain an area-efficient decoder design, good error correction performance, and achievable architecture implementation. The modified B-LDPC code decoding utilizes the iterative min-sum algorithm (MSA) and its decoding architecture design employs the non-overlapping operations of bit node unit (BNU) and check node unit (CNU). Different block matrix sizes for parity-check matrix can be adopted so that the modified B-LDPC code decoding improves the throughput without obvious performance degradation.

## Pragmatic two-level coded modulation using Reed-Solomon product codes

- **Status**: ❌
- **Reason**: Reed-Solomon product code 기반 coded modulation으로 비-LDPC 부호, 떼어낼 BP 기법 없음
- **ID**: ieee:4449773
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Samar Changuel, Raphael Le Bidan, Ramesh Pyndiah
- **PDF**: https://ieeexplore.ieee.org/document/4449773
- **Abstract**: A pragmatic two-level coded modulation scheme based on the direct product of two high-rate single-error-correcting Reed-Solomon (RS) codes is introduced for bandwidthefficient transmission in power-limited systems. The proposed scheme uses a single code/decoder. Data rate flexibility is achieved by simply varying the number of uncoded bits. A simple twostage decoding procedure is described that can operate either on hard- or soft-decisions from the demodulator. A study is carried out in order to optimize the bit-labeling strategy and the minimum Euclidean distance of the code. Simulation results show that the proposed coded modulation scheme exhibits a constant gap to capacity regardless of the cardinality of the signal set. Furthermore this gap can be reduced by considering RS component codes defined over large Galois fields.

## A low-complexity iterative symbol timing estimator for turbo receivers

- **Status**: ❌
- **Reason**: turbo 수신기용 심볼타이밍/캐리어 동기 추정으로 채널 디코더 ECC 기법 아님
- **ID**: ieee:4449851
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Hongyi Fu, Kai Yen, Yuen Sam Kwok +1
- **PDF**: https://ieeexplore.ieee.org/document/4449851
- **Abstract**: We consider the problem of symbol timing synchronization at low SNR without a training sequence in this paper. A low-complexity iterative joint symbol timing and carrier synchronization algorithm making use of the extrinsic information from the soft-input soft-output (SISO) decoder is proposed. The non- data-aided (NDA) algorithms are used for initial synchronization. The simulation results show that the proposed low-complexity solution works effectively and can converge after a few iterations. The receiver with the proposed iterative synchronizers can reach the ideal performance with perfect synchronization at very low SNR.

## Performance analysis of cyclic delay diversity on UWB OFDM systems

- **Status**: ❌
- **Reason**: UWB OFDM cyclic delay diversity SER/outage 분석으로 LDPC 무관
- **ID**: ieee:4449680
- **Type**: conference
- **Published**: 10-13 Dec.
- **Authors**: Poramate Tarasak, Khiam-Boon Png, Xiaoming Peng
- **PDF**: https://ieeexplore.ieee.org/document/4449680
- **Abstract**: This paper addresses cyclic delay diversity (CDD) on an ultrawideband communication system based on orthogonal frequency division multiplexing (OFDM) technique. Symbol error rate (SER) and outage probability have been derived. Results are obtained using a simplified version of IEEE802.15.3 standard channel model which takes into account multipath clustering and Poisson arrival properties. It is shown that with only two transmit antennas, CDD effectively improves SER performance and reduces outage probability significantly especially on the channel with short delay spread. Both simulation and analytical results agree well in all considered cases.
