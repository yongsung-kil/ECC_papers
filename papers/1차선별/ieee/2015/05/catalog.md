# IEEE Xplore — 2015-05 (1차선별 통과)


## High-Throughput LDPC-Decoder Architecture Using Efficient Comparison Techniques & Dynamic Multi-Frame Processing Schedule

- **Status**: ✅
- **Reason**: 고처리율 layered min-sum LDPC 디코더 HW 아키텍처, 효율적 비교회로 — 이식 가능 HW(D), 바이너리
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7079518
- **Type**: journal
- **Published**: May 2015
- **Authors**: Sachin Kumawat, Rahul Shrestha, Nikunj Daga +1
- **PDF**: https://ieeexplore.ieee.org/document/7079518
- **Abstract**: This paper presents architecture of block-level-parallel layered decoder for irregular LDPC code. It can be reconfigured to support various block lengths and code rates of IEEE 802.11n (WiFi) wireless-communication standard. We have proposed efficient comparison techniques for both column and row layered schedule and rejection-based high-speed circuits to compute the two minimum values from multiple inputs required for row layered processing of hardware-friendly min-sum decoding algorithm. The results show good speed with lower area as compared to state-of-the-art circuits. Additionally, this work proposes dynamic multi-frame processing schedule which efficiently utilizes the layered-LDPC decoding with minimum pipeline stages. The suggested LDPC-decoder architecture has been synthesized and post-layout simulated in 90 nm-CMOS process. This decoder occupies 5.19 mm2 area and supports multiple code rates like 1/2, 2/3, 3/4 & 5/6 as well as block-lengths of 648, 1296 & 1944. At a clock frequency of 336 MHz, the proposed LDPC-decoder has achieved better throughput of 5.13 Gbps and energy efficiency of 0.01 nJ/bits/iterations, as compared to the similar state-of-the-art works.

## Protograph-Based Raptor-Like LDPC Codes

- **Status**: ✅
- **Reason**: Protograph-based Raptor-like 바이너리 LDPC 신규 구성 — protograph 설계, ACE/CPEG lifting, error floor 개선 등 코드설계(E) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7045568
- **Type**: journal
- **Published**: May 2015
- **Authors**: Tsung-Yi Chen, Kasra Vakilinia, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/7045568
- **Abstract**: This paper proposes protograph-based Raptor-like (PBRL) codes as a class of rate-compatible low-density parity-check codes for binary-input AWGN channels. As with the Raptor codes, exclusive-OR operations on precoded bits produce additional parity bits providing extensive rate compatibility. Unlike Raptor codes, each additional parity bit in the protograph is explicitly designed to optimize the density evolution threshold. During the lifting process, approximate cycle extrinsic message degree (ACE) and circulant progressive edge growth (CPEG) constraints are used to avoid undesirable graphical structures. Some density-evolution performance is sacrificed to obtain lower error floors, particularly at short block-lengths. Simulation results are shown for information block sizes of k = 1032 and 16 384. For a target frame error rate of 10-5, at each rate, the k = 1032 and 16 384 code families perform within 1 dB and 0.4 dB of both the Gallager bound and the normal approximation, respectively. The 16 384 code family outperforms the best known standardized code family, namely, the AR4JA codes. The PBRL codes also outperform DVB-S2 codes that have the advantages of longer blocklengths and outer BCH codes. Performance is similar to RC code families designed by Nguyen et al. that do not constrain codes to have the PBRL structure and involve simulation in the optimization process at each rate.

## Impact of Redundant Checks on the LP Decoding Thresholds of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC LP 디코딩 임계값에 redundant parity check 영향 분석 — 디코더/코드설계 이론이나 LP 디코더 개선·redundant check 추가는 BP/사이클 제거에 이식 가능(C/E), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7072507
- **Type**: journal
- **Published**: May 2015
- **Authors**: Louay Bazzi, Hani Audah
- **PDF**: https://ieeexplore.ieee.org/document/7072507
- **Abstract**: Feldman et al. [11] asked whether the performance of the linear programming (LP) decoder can be improved by adding redundant parity checks to tighten the LP relaxation. We prove in this paper that for low-density parity-check codes, even if we include all redundant parity checks, asymptotically there is no gain in the LP decoder threshold on the binary symmetric channel under certain conditions on the base Tanner graph. First, we show that if the Tanner graph has bounded check-degree and satisfies a condition which we call asymptotic strength, then including high degree redundant parity checks in the LP does not significantly improve the threshold of the LP decoder in the following sense. For each constant δ > 0, there is a constant k > 0 such that the threshold of the LP decoder containing all redundant checks of degree at most k improves by at most δ upon adding to the LP all redundant checks of degree larger thank. We conclude that if the graph satisfies an additional condition which we call rigidity, then including all redundant checks does not improve the threshold of the base LP. We call the graph asymptotically strong if the LP decoder corrects a constant fraction of errors even if the log-likelihood-ratios of the correct variables are arbitrarily small. By building on a construction due Feldman et al. [9] and its recent improvement by Viderman [24], we show that asymptotic strength follows from sufficiently large variable-to-check expansion. We also give a geometric interpretation of asymptotic strength in terms pseudocodewords. We call the graph rigid if the minimum weight of a sum of check nodes involving a cycle tends to infinity as the block length tends to infinity. Under the assumptions that the graph girth is logarithmic and the minimum check degree is at least 3, rigidity is equivalent to the nondegeneracy property that adding at least logarithmically many checks does not give a constant weight check. We argue that nondegeneracy is a typical property of random check-regular Tanner graphs.

## Stopping Set Elimination by Parity-Check Matrix Extension via Integer Linear Programming

- **Status**: ✅
- **Reason**: 정지집합 제거를 위한 패리티검사 행렬 확장(ILP) + 4-cycle 회피 — error floor 개선·코드설계 기법(E), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7073646
- **Type**: journal
- **Published**: May 2015
- **Authors**: Hossein Falsafain, Sayyed Rasoul Mousavi
- **PDF**: https://ieeexplore.ieee.org/document/7073646
- **Abstract**: Error-rate floor phenomenon is known to be a serious impediment to the use of low-density parity-check (LDPC) codes for some practical applications that demand high data reliability. In the case of binary erasure channels (BECs), certain error-prone patterns, known as stopping sets, are proven to cause this performance degradation. A possible approach to diminish this drawback over BECs is to eliminate stopping sets by parity-check matrix extension. Given a parity-check matrix H, and a list L of its stopping sets, we present an integer linear programming (ILP) formulation to find a parity-check equation which eliminates the maximum number of stopping sets in L. One of the distinguishing advantages of the proposed scheme is its flexibility for modifications such as: limiting the weight of the new parity-check row, making the new row redundant or linearly independent, 4-cycle avoidance, and taking into account the sizes of stopping sets. Armed with these adjustments, the method can provide good performance improvements, as evidenced by simulation results. Furthermore, for a given Q ∈ N, by extending the basic formulation, we provide an ILP formulation for finding a set of size Q of parity-check equations which can best eliminate the stopping sets in L, among all such sets.

## Density Evolution and Functional Threshold for the Noisy Min-Sum Decoder

- **Status**: ✅
- **Reason**: Noisy Min-Sum 디코더 density evolution/functional threshold — 유한정밀 min-sum 변형 분석으로 NAND LDPC 디코더(C)에 직접 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7001663
- **Type**: journal
- **Published**: May 2015
- **Authors**: Christiane Kameni Ngassa, Valentin Savin, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/7001663
- **Abstract**: This paper investigates the behavior of the Min-Sum decoder running on noisy devices. Our aim is to evaluate the robustness of the decoder to computation noise caused by the faulty logic in the processing units. This type of noise represents a new source of errors that may occur during the decoding process. To this end, we first introduce probabilistic models for the arithmetic and logic units of the finite-precision min-sum decoder and then carry out the density evolution analysis of the noisy min-sum decoder. We show that, in some particular cases, the noise introduced by the device can help the min-sum decoder to escape from fixed points attractors and may actually result in an increased correction capacity with respect to the noiseless decoder. We also point out a specific threshold phenomenon, referred to as functional threshold, which accurately describes the convergence behavior of noisy decoders. The behavior of the noisy MS is demonstrated in the asymptotic limit of the code length through a noisy version of density evolution and is also verified in the finite-length case by Monte Carlo simulations.

## On Some Properties of the Mutual Information Between Extrinsics With Application to Iterative Decoding

- **Status**: ✅
- **Reason**: iterative 디코딩 extrinsic LLR 상호정보 분석으로 stopping criterion·scaling factor 추정 — min-sum 스케일링·정지조건은 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7084594
- **Type**: journal
- **Published**: May 2015
- **Authors**: Florence Alberge
- **PDF**: https://ieeexplore.ieee.org/document/7084594
- **Abstract**: Iterative decoding is an efficient error-correction tool based on the exchange of extrinsic probabilities between the constituent decoders. In this paper, the properties of the mutual information between the extrinsic LLR at the output of two constituent decoders are analyzed with application to turbo and LDPC codes. This is a bridge between information-theoretic analysis and practical implementations. It is proved here that the mutual information between extrinsics is a lower bound of the mutual information between each extrinsic and the transmitted message. In addition, an efficient online evaluation is provided in the paper with accuracy validated through numerical experiments. As an application, the mutual information between extrinsics is used for designing efficient stopping criterion and error detection rules at the decoder side. Two online methods for the estimation of optimal scaling factor to be applied to the extrinsic LLR are also derived. In contrast with most references, an analytical expression is obtained that does not require estimation of the actual transmitted bits. All results in the paper are derived for Gaussian distributed LLR with independent mean and variance.

## An iterative bit flipping based decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: New bit-flipping decoding algorithm for LDPC using inter-stage data correlation — transferable BP/BF decoder improvement (category C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7140214
- **Type**: conference
- **Published**: 6-7 May 20
- **Authors**: Sajjad Imani, Reza Shahbazian, Seyed Ali Ghorashi
- **PDF**: https://ieeexplore.ieee.org/document/7140214
- **Abstract**: In this paper a new decoding algorithm for low density parity check (LDPC) codes based on bit flipping (BF) is proposed. In the proposed algorithm, the BF criterion benefits the data correlation between the decoded and received signal in current and previous stages. The proposed algorithm also degrades the decoding probability of one code word to another one in the same codebook. Simulation results confirm our theoretical formulation and show a good enhancement in code error rate and bit error rate of the proposed decoding algorithm compared to the conventional ones.

## Comparative analysis of single mode and multimode QC-LDPC decoder using modified belief propagation algorithm

- **Status**: ✅
- **Reason**: C/D: modified BP 기반 QC-LDPC 디코더 + partially parallel Verilog/FPGA HW, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7150811
- **Type**: conference
- **Published**: 28-30 May 
- **Authors**: M.V. Mankar, G.M. Asutkar, P.K. Dakhole
- **PDF**: https://ieeexplore.ieee.org/document/7150811
- **Abstract**: Low density parity check codes (LDPC) are appearing in an increasing number of applications which shows a performance close to the Shannon limit. The near Shannon limit error correction capability has lead LDPC codes to become the coding technique of choice in many communications and storage systems since their introduction. LDPC have good error correcting performance which enables efficient and reliable communication. Quasi-cyclic LDPC codes known as a subclass of LDPC codes are used whose parity check matrices consists of circulant permutation matrices. This character of QC-LDPC codes opens the door for the multi-mode. In the present work partially parallel architecture for single mode and multi-mode quasi-cyclic low density parity check (QC-LDPC) decoders have been designed using modified belief propagation algorithm. QC-LDPC codes require less memory as compared to LDPC codes and resource occupied by the single mode decoder is only a little more than the multi-mode decoder. This decoder is modeled using Verilog software, synthesized and performed place and route for the design using Xilinx ISE 13.2.

## ADMM decoding of error correction codes: From geometries to algorithms

- **Status**: ✅
- **Reason**: ADMM 디코딩 서브루틴(ℓ1 ball projection)은 부호 비의존적 BP-LP 디코더 기법으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7133156
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7133156
- **Abstract**: Many code constraints can be represented using factor graphs. By relaxing these factorable coding constraints to linear constraints, it is straightforward to form a decoding optimization problem. Furthermore, by pairing these factor graphs with the alternating directions method of multipliers (ADMM) technique of large-scale optimization, one can develop distributed algorithms to solve the decoding optimization problems. However, the non-trivial part has always been developing an efficient algorithm for the subroutines of ADMM, which directly relates to the geometries of the relaxed coding constraints. In this paper, we focus on summarizing existing results and distilling insights to these problems. First, we review the ADMM formulation and geometries involved in the subroutines. Next, we present a linear time algorithm for projecting onto an ℓ1 ball with box constraints.

## A 3.46 Gb/s (9141,8224) LDPC-based ECC scheme and on-line channel estimation for solid-state drive applications

- **Status**: ✅
- **Reason**: NAND SSD용 LDPC ECC, MGDBF+min-sum 다중전략 디코더 및 온라인 채널추정 — 직접 해당(A/C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7168917
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Kin-Chu Ho, Chih-Lung Chen, Yen-Chin Liao +2
- **PDF**: https://ieeexplore.ieee.org/document/7168917
- **Abstract**: As the reliability of NAND Flash memory keeps degrading, Low-Density Parity-Check (LDPC) codes are widely proposed to extend the endurance of Solid State Drive (SSD). However, implementing powerful decoding algorithm such as soft min-sum algorithm with high decoding speed comes along with higher hardware cost. To achieve efficient hardware cost, we propose a multi-strategy ECC scheme which consists of modified gradient descent bit-flipping (MGDBF), hard min-sum, and soft min-sum decoders. The MGDBF decoder aims to correct most of the erroneous codewords with advantages of high decoding throughput and low hardware cost, while the soft min-sum decoder is targeted to correct codewords with large number of errors under moderate decoding throughput and reasonable hardware cost. In addition, we propose a bi-sectional channel estimation technique which enables on-line estimation of distribution to generate accurate soft information for LDPC decoding with low complexity. The ECC codec and the complete Toggle DDR 1.0 NAND interface control circuits are integrated and fabricated in 90nm CMOS process. The throughput of proposed MGDBF decoder achieves 3.46 Gb/s which satisfies the throughput requirement of both toggle DDR 1.0 and 2.0 NAND interfaces.

## Latency-optimized stochastic LDPC decoder for high-throughput applications

- **Status**: ✅
- **Reason**: 확률적(stochastic) LDPC 디코더 지연 단축 신규 전략(LUT 초기화, BF 후처리) — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7169329
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Di Wu, Yun Chen, Qichen Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/7169329
- **Abstract**: Stochastic decoding can be applied to Low-Density Parity-Check codes in order to achieve high throughput with less area. However, most architectures suffer from large decoding latencies, due to the mechanism of stochastic computation. In this paper, three novel strategies, including the LUT-based initialization, the posterior-information-based hard decision and the Bit-Flipping-based post processing, are proposed in order to reduce decoding latency and hence improve throughput. For the standard IEEE 802.3an (2048, 1723) code, simulation indicates 75.7% reduction in average decoding cycles at 4.5 dB with satisfied bit error rate. Moreover, hardware implementation shows that the area of variable node units is reduced significantly in SMIC 65 nm technology.

## Refresh-free dynamic standard-cell based memories: Application to a QC-LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC 디코더의 동적 SCM 메모리로 면적 44% 절감 HW 기법 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7168911
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Pascal Meinerzhagen, Andrea Bonetti, Georgios Karakonstantis +3
- **PDF**: https://ieeexplore.ieee.org/document/7168911
- **Abstract**: The area and power consumption of low-density parity check (LDPC) decoders are typically dominated by embedded memories. To alleviate such high memory costs, this paper exploits the fact that all internal memories of a LDPC decoder are frequently updated with new data. These unique memory access statistics are taken advantage of by replacing all static standard-cell based memories (SCMs) of a prior-art LDPC decoder implementation by dynamic SCMs (D-SCMs), which are designed to retain data just long enough to guarantee reliable operation. The use of D-SCMs leads to a 44% reduction in silicon area of the LDPC decoder compared to the use of static SCMs. The low-power LDPC decoder architecture with refresh-free D-SCMs was implemented in a 90nm CMOS process, and silicon measurements show full functionality and an information bit throughput of up to 600 Mbps (as required by the IEEE 802.11n standard).

## Efficient realization of probabilistic gradient descent bit flipping decoders

- **Status**: ✅
- **Reason**: PGDBF 비트플립 디코더 HW 구현(LFSR/IVRG 랜덤생성) — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7168928
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Khoa Le, David Declercq, Fakhreddine Ghaffari +4
- **PDF**: https://ieeexplore.ieee.org/document/7168928
- **Abstract**: In this paper, several implementations of the recently introduced PGDBF decoder for LDPC codes are proposed. In [2], the authors show that using randomness in bit-flipping decoders can greatly improve the error correction performance. In this paper, two models of random generators are proposed and compared through hardware implementation and performance simulation. A conventional implementation of the random generator through LFSR as a first design, and a new approach using binary sequences that are produced by the LDPC decoder, named IVRG, as second design. We show that both implementation of the PGDBF improve greatly the error correction performance, while maintaining the same large throughtput. However, the performance gain requires a large hardware overhead in the case of LFSR-PGDBF, while the overhead is limited to only 10% in the case of the IVRG-PGDBF.

## TTCN: A new approach for low-power split-row LDPC decoders

- **Status**: ✅
- **Reason**: Split-Row LDPC 디코더 저전력 TTCN 기법, 체크노드 게이팅 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7169068
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Mohammad Shahrad, Mahdi Shabany
- **PDF**: https://ieeexplore.ieee.org/document/7169068
- **Abstract**: Split-Row technique is proved to be one of the most effective methods to reduce the routing complexity of fully-parallel LDPC decoders. This technique is based on the idea of splitting each check node processor to multiple smaller processors. This paper introduces a new method, to increase the power-efficiency of Split-Row LDPC decoders. The proposed method is called trust to the truthful check node (TTCN), enabling the decoder to only depend on a portion of check node processors at specific decoding iterations. This leads to an average reduction of 30%-40% in the check node dynamic power consumption. This is achieved by means of trust to a minority of check node processors and gating the others. In fact, a great side effect of the proposed method is also a slight improvement in the error performance.

## Fast estimation of error floor effect for irregular low-density parity-check codes

- **Status**: ✅
- **Reason**: E: irregular 바이너리 LDPC error floor 저감(girth/EMD/short cycle 지표) — 이식 가능 코드 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7147163
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Alexei A. Ovinnikov, Vladimir V. Vityazev
- **PDF**: https://ieeexplore.ieee.org/document/7147163
- **Abstract**: The article summarizes a comparison of numerous irregular low-density parity-check codes using a set of metrics such as girth, number of short cycles in Tanner graph and extrinsic message degree (EMD). Based on this these metrics, we analyze how to decrease error floor for such codes with no negative effect to threshold.

## Design of LDPC code ensembles with fast convergence properties

- **Status**: ✅
- **Reason**: 유한 반복수 최적화 LDPC 앙상블 설계(EXIT+differential evolution), GLDPC 포함 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7185085
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Ian P. Mulholland, Enrico Paolini, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7185085
- **Abstract**: The design of low-density parity-check (LDPC) code ensembles optimized for a finite number of decoder iterations is investigated. Our approach employs EXIT chart analysis and differential evolution to design such ensembles for the binary erasure channel and additive white Gaussian noise channel. The error rates of codes optimized for various numbers of decoder iterations are compared and it is seen that in the cases considered, the best performance for a given number of decoder iterations is achieved by codes which are optimized for this particular number. The design of generalized LDPC (GLDPC) codes is also considered, showing that these structures can offer better performance than LDPC codes for low-iteration-number designs. Finally, it is illustrated that LDPC codes which are optimized for a small number of iterations exhibit significant deviations in terms of degree distribution and weight enumerators with respect to LDPC codes returned by more conventional design tools.

## Evaluation of the robustness of LDPC encoders to hardware noise

- **Status**: ✅
- **Reason**: faulty HW에서 LDPC 인코더 견고성 분석·인코딩 에러확률·저복잡도 인코딩 비교 — HW/구성 관점 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7185092
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Elsa Dupraz, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/7185092
- **Abstract**: This paper analyzes the robustness of Low Density Parity Check (LDPC) encoders on faulty hardware. The faulty hardware effect on the encoder is represented by an error model at the XOR gate level. We review the existing LDPC encoding solutions in the works of Richardson and Urbante (2001) and Chen et al. (2005) and the code constructions in the works of Ping et al. (2001), Jin et al. (2000), and Garcia-Frias and Zhong (2003) that guarantee low encoding complexity. For each of the existing solutions, we provide the analytic expression of the encoding error probability, and we use it to evaluate the robustness of the encoders to hardware noise. We then identify the two best encoding solutions in terms of robustness and we compare their performance with Monte-Carlo simulations.

## SC-LDPC codes over the block-fading channel: Robustness to a synchronisation offset

- **Status**: ✅
- **Reason**: SC-LDPC 데이터 할당 기반 동기 오프셋 견고성 — 블록페이딩 응용이나 SC-LDPC 구성 기법 이식 가능(E), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7185094
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Iryna Andriyanova, Najeeb Ul Hassan, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/7185094
- **Abstract**: Spatially-Coupled LDPC (SC-LDPC) codes have been recently shown to be very efficient for transmissions over nonergodic channels, in particular over block-fading channels [1]. In fact, it is possible to design a SC-LDPC code with any given code diversity [2]. In this work, we investigate the performance of SC-LDPC codes over block-fading channels, assuming a mismatch (or offset) between the first bit of a transmission packet and a first bit of a codeword. Such a mismatch is called the synchronisation offset, and it has a negative impact on the code diversity. We propose a data-allocation scheme for SC-LDPC codes that allows to obtain a robustness to the synchronisation offset. Combined together with the code design from [2], it allows to design efficient SC-LDPC codes, whose performance degrades only slowly under imperfect transmission conditions.

## Performance Characterization of LDPC Codes for Large-Volume NAND Flash Data

- **Status**: ✅
- **Reason**: A. NAND 플래시 LDPC 성능 특성화 + soft info 품질 채널 metric 제안 — NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7150301
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Patrick Khayat, Mustafa Kaynak, Sivagnanam Parthasarathy +1
- **PDF**: https://ieeexplore.ieee.org/document/7150301
- **Abstract**: High bit error rates of next-generation flash devices necessitate the use of more powerful error correction codes (ECCs), such as low-density parity-check (LDPC) codes, instead of the legacy Bose-Chaudhuri-Hocquenghem (BCH) codes. Unlike algebraic codes, the random nature of LDPC codes as well as their ability to use soft information requires the use of Monte Carlo (MC) simulations to evaluate code performance. Given a large volume of NAND data, this can pose resource challenges both in terms of simulation platforms and time needed for the Monte Carlo simulations. In order to overcome these challenges, we introduce a new channel metric in this paper to quantify the quality of soft information and propose a practical LDPC code performance characterization methodology.

## LDPC Soft Decoding with Reduced Power and Latency in 1X-2X NAND Flash-Based Solid State Drives

- **Status**: ✅
- **Reason**: A. NAND 플래시 SSD에서 LDPC soft decoding 전력/지연 최적화 (NAND-Assisted Soft Decision) — 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7150293
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Lorenzo Zuolo, Cristian Zambelli, Piero Olivo +2
- **PDF**: https://ieeexplore.ieee.org/document/7150293
- **Abstract**: The reliability of the non-volatile NAND flash memories, measured in terms of Raw Bit Error Rate (RBER), is reaching critical levels for traditional error detection and correction. Therefore, to ensure data trustworthiness in nowadays NAND flash-based Solid State Drives, it becomes essential exploiting powerful correction algorithms such as the Low Density Parity Check (LDPC). However, the burdens of this approach materialize in an increased NAND flash power consumption due to the increased memory read latencies that translates in limited disk performance. In this work it is performed a comparison between a standard LDPC decoding approach based on hard and soft decisions and an optimized solution called LDPC NAND- Assisted Soft Decision. The simulation results on 2X, 1X and mid-1X MLC NAND flash-based Solid State Drives in terms of NAND flash I/O power consumption, disk read latencies and performance, favor the adoption of the presented solution.

## Enhancing the error-correcting performance of LDPC codes for LTE and WiFi

- **Status**: ✅
- **Reason**: LTE/WiFi LDPC용 수정 SPA 디코더 제안(디코딩셋 활용, 동일 반복수에서 성능 개선); 부호 비의존 BP 개선 기법이라 NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7148600
- **Type**: conference
- **Published**: 15-16 May 
- **Authors**: Insah Bhurtah, Pierre Clarel Catherine, K.M. Sunjiv Soyjaudah
- **PDF**: https://ieeexplore.ieee.org/document/7148600
- **Abstract**: Low-density parity-check (LDPC) codes are one of the most powerful error-correcting codes for wireless communication of high-speed data. This power comes from an efficient decoding scheme, the sum-product algorithm (SPA), which runs over the bipartite graph defining the code. In this work, we propose to use a modified version of the decoding algorithm over the LDPC codes used in Long Term Evolution (LTE) and WiFi and demonstrate that with the same number of iterations, without any increase in time complexity, we can achieve an enhanced error-correcting performance. The only trade off of the system is the necessary storage of the decoding sets, for a total size of ns × n, where ns is the number of decoding sets used and n is the codeword length. In this work, the maximum value of ns used is 5, which makes the trade-off fairly acceptable, considering that the coding gain is obtained virtually free-of-charge.

## The design of protograph LDPC codes for two-dimensional magnetic recording channels

- **Status**: ✅
- **Reason**: EXIT chart + ensemble weight enumerator로 protograph LDPC 신규 설계(E), 바이너리 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7157698
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: P. Chen, L. Kong, Y. Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/7157698
- **Abstract**: This paper investigates the performance of the protograph based low-density parity-check (LDPC) codes for two dimensional (2D) inter symbol interference (ISI) channels with magnetic recording density . The protograph LDPC codes have been shown to possess excellent error performance over AWGN channel and over partial response channel. Moreover, the protograph structure that realizes linear encoding and decoding allows high-speed encoding and decoding implementations. We further proposes a protograph LDPC code for 2D ISI channel with the help of extrinsic information transfer (EXIT) chart fitting and asymptotic ensemble weight enumerators. Analysis and simulation results show that the proposed code has performance gain both in low- and high-SNR regions over previously optimized irregular LDPC codes for 2D ISI channels.

## Protograph based quasi-cyclic LDPC coding for ultra-high density magnetic recording channels

- **Status**: ✅
- **Reason**: protograph 기반 QC-LDPC 신규 코드 설계(E). 자기기록용이나 바이너리 QC-LDPC 구성 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7157697
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: L. Kong, L. He, P. Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7157697
- **Abstract**: Bit-patterned media recording (BPMR), heat (or microwave) assisted magnetic recording (HAMR) and shingled writing (SW)/two-dimensional magnetic recording (TDMR) have been primed to further increase the areal density of magnetic recording beyond 1Tb/in2. However, with the reduction of the track pitch, inter-track interference (ITI) becomes a major impairment for these magnetic recording systems. ITI combined with the conventional (down-track) inter-symbol interference (ISI) forms a two-dimensional (2D) interference that severely degrades the performance of data detection in these systems.

## A soft decodable concatenated LDPC code

- **Status**: ✅
- **Reason**: SSD/HDD용 LDPC, error floor<1e-12, 큰 블록 코드워드, soft decodable concatenated LDPC 신규 설계(A/B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7157702
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: S. Yang, Y. Han, X. Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/7157702
- **Abstract**: Low density parity check (LDPC) codes with iterative soft decoding have been adopted as the primary error correction coding technology in data storage devices, e.g., hard disk drives (HDDs) and solid state drives (SSDs). Data storage normally has stringent requirements for low probability of decoding failure since there is no re-transmission mechanism as available for most other data communication applications. Typically the error floor of a LDPC decoder in a storage application should be below 10-12. Recently, the adoption of 4 kB sector formats has allowed LDPC code word size to increase from 4096 user bits to 32768 user bits. This increase in code word size has enabled significantly more error correction power and better noise tolerance margin. Further increases in LDPC code block size beyond 4KB are expected to deliver further SNR gain but would be very expensive in terms of silicon area and power consumption.

## Algebraic Constructions of Quasi-Cyclic LDPC Codes Based on Prime Fields

- **Status**: ✅
- **Reason**: 소수체 기반 QC-LDPC 신규 대수적 구성(E), 빠른 수렴. 바이너리 QC-LDPC 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7145673
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Rui Zhang, Guixia Kang, Ningbo Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7145673
- **Abstract**: On dispersing different base matrices combined with masking, different kinds of quasi-cyclic low-density parity check (QC-LDPC) codes are constructed, which may achieve good error performances. Two new algebraic constructions of regular QC-LDPC codes are presented in this paper. The two constructions are based on two base matrices by dispersing and masking. The two base matrices are based on the generators of the cyclic group of a prime field. Results show that the two classes of codes presented in this paper perform well with iterative decoding over AWGN channel and have advantages over MacKay codes in some aspects of code performances. We find that one of the constructed codes converges very fast with iterative decoding, which is a critical property in ultra-high throughput communication systems.

## Novel Extending Scheme for the Construction of Rate-Compatible IRA-Like Codes

- **Status**: ✅
- **Reason**: 새 확장 알고리즘으로 rate-compatible IRA-like LDPC 구성(균일 체크노드 분포, 선형 인코딩) — 바이너리 LDPC 코드 설계 신규 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7145956
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Wenwen Li, Jing Lei, Er-bao Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7145956
- **Abstract**: In this paper, a novel extending algorithm is proposed for the construction of rate compatible (RC) irregular repeat accumulate like (IRA-like) codes. Based on the structure characters of IRA-like codes, we propose an extending algorithm with uniform check node degree distribution and strong dependency in parity check matrix. Lower rate codes constructed through this method are efficiently encodable and well performed. Starting from initial code rate 8/16, the designed extending algorithm combining with existing puncturing algorithm realizes a series of RC IRA-like codes with rate R = 8/24, 8/23... 8/9. Simulation results show that the constructed RC IRA-like codes outperform those of similar algorithms from 0.04dB to 0.4 dB.

## Phase noise-robust LLR calculation with linear/bilinear transform for LDPC-coded coherent communications

- **Status**: ✅
- **Reason**: 위상잡음에 강건한 LDPC 디코더 LLR 계산(선형/이중선형 변환) — LLR 계산 기법은 NAND 채널 LLR 산출에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7184331
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Keisuke Kojima +1
- **PDF**: https://ieeexplore.ieee.org/document/7184331
- **Abstract**: We propose a modified log-likelihood ratio (LLR) calculation for an LDPC decoder to be robust against residual phase noise at the demodulator. The proposed scheme is based on a linear/bilinear transform offers 1 ~ 2dB gain in the presence of large phase noise.
