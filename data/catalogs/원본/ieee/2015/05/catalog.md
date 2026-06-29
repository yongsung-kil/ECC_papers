# IEEE Xplore — 2015-05


## High-Throughput LDPC-Decoder Architecture Using Efficient Comparison Techniques & Dynamic Multi-Frame Processing Schedule

- **Status**: ✅
- **Reason**: 고처리율 layered min-sum LDPC 디코더 HW 아키텍처, 효율적 비교회로 — 이식 가능 HW(D), 바이너리
- **ID**: ieee:7079518
- **Type**: journal
- **Published**: May 2015
- **Authors**: Sachin Kumawat, Rahul Shrestha, Nikunj Daga +1
- **PDF**: https://ieeexplore.ieee.org/document/7079518
- **Abstract**: This paper presents architecture of block-level-parallel layered decoder for irregular LDPC code. It can be reconfigured to support various block lengths and code rates of IEEE 802.11n (WiFi) wireless-communication standard. We have proposed efficient comparison techniques for both column and row layered schedule and rejection-based high-speed circuits to compute the two minimum values from multiple inputs required for row layered processing of hardware-friendly min-sum decoding algorithm. The results show good speed with lower area as compared to state-of-the-art circuits. Additionally, this work proposes dynamic multi-frame processing schedule which efficiently utilizes the layered-LDPC decoding with minimum pipeline stages. The suggested LDPC-decoder architecture has been synthesized and post-layout simulated in 90 nm-CMOS process. This decoder occupies 5.19 mm2 area and supports multiple code rates like 1/2, 2/3, 3/4 & 5/6 as well as block-lengths of 648, 1296 & 1944. At a clock frequency of 336 MHz, the proposed LDPC-decoder has achieved better throughput of 5.13 Gbps and energy efficiency of 0.01 nJ/bits/iterations, as compared to the similar state-of-the-art works.

## Protograph-Based Raptor-Like LDPC Codes

- **Status**: ✅
- **Reason**: Protograph-based Raptor-like 바이너리 LDPC 신규 구성 — protograph 설계, ACE/CPEG lifting, error floor 개선 등 코드설계(E) 이식 가능.
- **ID**: ieee:7045568
- **Type**: journal
- **Published**: May 2015
- **Authors**: Tsung-Yi Chen, Kasra Vakilinia, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/7045568
- **Abstract**: This paper proposes protograph-based Raptor-like (PBRL) codes as a class of rate-compatible low-density parity-check codes for binary-input AWGN channels. As with the Raptor codes, exclusive-OR operations on precoded bits produce additional parity bits providing extensive rate compatibility. Unlike Raptor codes, each additional parity bit in the protograph is explicitly designed to optimize the density evolution threshold. During the lifting process, approximate cycle extrinsic message degree (ACE) and circulant progressive edge growth (CPEG) constraints are used to avoid undesirable graphical structures. Some density-evolution performance is sacrificed to obtain lower error floors, particularly at short block-lengths. Simulation results are shown for information block sizes of k = 1032 and 16 384. For a target frame error rate of 10-5, at each rate, the k = 1032 and 16 384 code families perform within 1 dB and 0.4 dB of both the Gallager bound and the normal approximation, respectively. The 16 384 code family outperforms the best known standardized code family, namely, the AR4JA codes. The PBRL codes also outperform DVB-S2 codes that have the advantages of longer blocklengths and outer BCH codes. Performance is similar to RC code families designed by Nguyen et al. that do not constrain codes to have the PBRL structure and involve simulation in the optimization process at each rate.

## Impact of Redundant Checks on the LP Decoding Thresholds of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC LP 디코딩 임계값에 redundant parity check 영향 분석 — 디코더/코드설계 이론이나 LP 디코더 개선·redundant check 추가는 BP/사이클 제거에 이식 가능(C/E), 바이너리 LDPC
- **ID**: ieee:7072507
- **Type**: journal
- **Published**: May 2015
- **Authors**: Louay Bazzi, Hani Audah
- **PDF**: https://ieeexplore.ieee.org/document/7072507
- **Abstract**: Feldman et al. [11] asked whether the performance of the linear programming (LP) decoder can be improved by adding redundant parity checks to tighten the LP relaxation. We prove in this paper that for low-density parity-check codes, even if we include all redundant parity checks, asymptotically there is no gain in the LP decoder threshold on the binary symmetric channel under certain conditions on the base Tanner graph. First, we show that if the Tanner graph has bounded check-degree and satisfies a condition which we call asymptotic strength, then including high degree redundant parity checks in the LP does not significantly improve the threshold of the LP decoder in the following sense. For each constant δ > 0, there is a constant k > 0 such that the threshold of the LP decoder containing all redundant checks of degree at most k improves by at most δ upon adding to the LP all redundant checks of degree larger thank. We conclude that if the graph satisfies an additional condition which we call rigidity, then including all redundant checks does not improve the threshold of the base LP. We call the graph asymptotically strong if the LP decoder corrects a constant fraction of errors even if the log-likelihood-ratios of the correct variables are arbitrarily small. By building on a construction due Feldman et al. [9] and its recent improvement by Viderman [24], we show that asymptotic strength follows from sufficiently large variable-to-check expansion. We also give a geometric interpretation of asymptotic strength in terms pseudocodewords. We call the graph rigid if the minimum weight of a sum of check nodes involving a cycle tends to infinity as the block length tends to infinity. Under the assumptions that the graph girth is logarithmic and the minimum check degree is at least 3, rigidity is equivalent to the nondegeneracy property that adding at least logarithmically many checks does not give a constant weight check. We argue that nondegeneracy is a typical property of random check-regular Tanner graphs.

## Stopping Set Elimination by Parity-Check Matrix Extension via Integer Linear Programming

- **Status**: ✅
- **Reason**: 정지집합 제거를 위한 패리티검사 행렬 확장(ILP) + 4-cycle 회피 — error floor 개선·코드설계 기법(E), 바이너리 LDPC
- **ID**: ieee:7073646
- **Type**: journal
- **Published**: May 2015
- **Authors**: Hossein Falsafain, Sayyed Rasoul Mousavi
- **PDF**: https://ieeexplore.ieee.org/document/7073646
- **Abstract**: Error-rate floor phenomenon is known to be a serious impediment to the use of low-density parity-check (LDPC) codes for some practical applications that demand high data reliability. In the case of binary erasure channels (BECs), certain error-prone patterns, known as stopping sets, are proven to cause this performance degradation. A possible approach to diminish this drawback over BECs is to eliminate stopping sets by parity-check matrix extension. Given a parity-check matrix H, and a list L of its stopping sets, we present an integer linear programming (ILP) formulation to find a parity-check equation which eliminates the maximum number of stopping sets in L. One of the distinguishing advantages of the proposed scheme is its flexibility for modifications such as: limiting the weight of the new parity-check row, making the new row redundant or linearly independent, 4-cycle avoidance, and taking into account the sizes of stopping sets. Armed with these adjustments, the method can provide good performance improvements, as evidenced by simulation results. Furthermore, for a given Q ∈ N, by extending the basic formulation, we provide an ILP formulation for finding a set of size Q of parity-check equations which can best eliminate the stopping sets in L, among all such sets.

## Density Evolution and Functional Threshold for the Noisy Min-Sum Decoder

- **Status**: ✅
- **Reason**: Noisy Min-Sum 디코더 density evolution/functional threshold — 유한정밀 min-sum 변형 분석으로 NAND LDPC 디코더(C)에 직접 이식 가능.
- **ID**: ieee:7001663
- **Type**: journal
- **Published**: May 2015
- **Authors**: Christiane Kameni Ngassa, Valentin Savin, Elsa Dupraz +1
- **PDF**: https://ieeexplore.ieee.org/document/7001663
- **Abstract**: This paper investigates the behavior of the Min-Sum decoder running on noisy devices. Our aim is to evaluate the robustness of the decoder to computation noise caused by the faulty logic in the processing units. This type of noise represents a new source of errors that may occur during the decoding process. To this end, we first introduce probabilistic models for the arithmetic and logic units of the finite-precision min-sum decoder and then carry out the density evolution analysis of the noisy min-sum decoder. We show that, in some particular cases, the noise introduced by the device can help the min-sum decoder to escape from fixed points attractors and may actually result in an increased correction capacity with respect to the noiseless decoder. We also point out a specific threshold phenomenon, referred to as functional threshold, which accurately describes the convergence behavior of noisy decoders. The behavior of the noisy MS is demonstrated in the asymptotic limit of the code length through a noisy version of density evolution and is also verified in the finite-length case by Monte Carlo simulations.

## BICMC and TD Comparative Performance Study of 16-APSK Signal Variants for DVB-S2 Systems

- **Status**: ❌
- **Reason**: DVB-S2 16-APSK 변조/매핑 성능연구, LDPC는 베이스라인 부수 언급, 떼어낼 LDPC 기법 없음.
- **ID**: ieee:7057637
- **Type**: journal
- **Published**: May 2015
- **Authors**: Vassilis Dalakas, Stylianos Papaharalabos, P. Takis Mathiopoulos +3
- **PDF**: https://ieeexplore.ieee.org/document/7057637
- **Abstract**: A comparative performance study, in terms of Bit Interleaved Coded Modulation Capacity (BICMC) and Total Degradation (TD), between Amplitude Phase Shift Keying (APSK) signal variants for the 2nd generation Digital Video Broadcasting via Satellite (DVB-S2) system is presented. Motivated by the observation that the presence of more signal points in the outer ring of 16-APSK signals appears to improve the performance in a non-linear (NL) channel, we investigate the performance of 2-14 and 3-13 APSK signals with two novel bit-to-symbol mappings as alternatives to the 4-12 APSK, which is currently proposed as the modulation scheme for the DVB-S2 standard. Performance evaluation results are obtained for an air-interface based on this standard, which includes a Non-Linear (NL) High Power Amplifier (HPA), predistortion, raised cosine Nyquist filters and Low-Density Parity-Check (LDPC) codes. Performance results have shown that the proposed 3-13 APSK signal not only achieves the best BICMC performance with higher gains occurring at high signal-to-noise ratios, but also outperforms, in terms of TD performance, all the other considered 16-ary APSK signal variants.

## List Decoding of Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 SC list 디코더 — polar 구조 의존적, 바이너리 LDPC BP에 그대로 이식되는 부호 비의존 기법 아님.
- **ID**: ieee:7055304
- **Type**: journal
- **Published**: May 2015
- **Authors**: Ido Tal, Alexander Vardy
- **PDF**: https://ieeexplore.ieee.org/document/7055304
- **Abstract**: We describe a successive-cancellation list decoder for polar codes, which is a generalization of the classic successive-cancellation decoder of Arıkan. In the proposed list decoder, L decoding paths are considered concurrently at each decoding stage, where L is an integer parameter. At the end of the decoding process, the most likely among the L paths is selected as the single codeword at the decoder output. Simulations show that the resulting performance is very close to that of maximum-likelihood decoding, even for moderate values of L. Alternatively, if a genie is allowed to pick the transmitted codeword from the list, the results are comparable with the performance of current state-of-the-art LDPC codes. We show that such a genie can be easily implemented using simple CRC precoding. The specific list-decoding algorithm that achieves this performance doubles the number of decoding paths for each information bit, and then uses a pruning procedure to discard all but the L most likely paths. However, straightforward implementation of this algorithm requires Ω(Ln2) time, which is in stark contrast with the O(n log n) complexity of the original successive-cancellation decoder. In this paper, we utilize the structure of polar codes along with certain algorithmic transformations in order to overcome this problem: we devise an efficient, numerically stable, implementation of the proposed list decoder that takes only O(Ln logn) time and O(Ln) space.

## On Some Properties of the Mutual Information Between Extrinsics With Application to Iterative Decoding

- **Status**: ✅
- **Reason**: iterative 디코딩 extrinsic LLR 상호정보 분석으로 stopping criterion·scaling factor 추정 — min-sum 스케일링·정지조건은 LDPC BP에 이식 가능(C)
- **ID**: ieee:7084594
- **Type**: journal
- **Published**: May 2015
- **Authors**: Florence Alberge
- **PDF**: https://ieeexplore.ieee.org/document/7084594
- **Abstract**: Iterative decoding is an efficient error-correction tool based on the exchange of extrinsic probabilities between the constituent decoders. In this paper, the properties of the mutual information between the extrinsic LLR at the output of two constituent decoders are analyzed with application to turbo and LDPC codes. This is a bridge between information-theoretic analysis and practical implementations. It is proved here that the mutual information between extrinsics is a lower bound of the mutual information between each extrinsic and the transmitted message. In addition, an efficient online evaluation is provided in the paper with accuracy validated through numerical experiments. As an application, the mutual information between extrinsics is used for designing efficient stopping criterion and error detection rules at the decoder side. Two online methods for the estimation of optimal scaling factor to be applied to the extrinsic LLR are also derived. In contrast with most references, an analytical expression is obtained that does not require estimation of the actual transmitted bits. All results in the paper are derived for Gaussian distributed LLR with independent mean and variance.

## Closed-Form CRLBs for CFO and Phase Estimation From Turbo-Coded Square-QAM-Modulated Transmissions

- **Status**: ❌
- **Reason**: Turbo/LDPC coded 시스템의 CFO·위상 추정 CRLB 이론, 디코더/HW/구성으로 안 이어지는 추정 bound.
- **ID**: ieee:7001708
- **Type**: journal
- **Published**: May 2015
- **Authors**: Faouzi Bellili, Achref Methenni, Sofiène Affes
- **PDF**: https://ieeexplore.ieee.org/document/7001708
- **Abstract**: In this paper, we consider the problem of joint phase and carrier frequency offset (CFO) estimation for turbo-coded systems. We derive for the first time the closed-form expressions for the exact Cramér-Rao lower bounds (CRLBs) of these estimators over turbo-coded square-QAM-modulated single- or multi-carrier transmissions. In the latter case, the derived bounds remain valid in the general case of adaptive modulation and coding (AMC) where the coding rate and modulation order vary from one subcarrier to another depending on the corresponding channel quality information (CQI). In particular, we introduce a new recursive process that enables the construction of arbitrary Gray-coded square-QAM constellations. Some hidden properties of such constellations will be revealed, owing to this recursive process, and carefully handled to decompose the system's likelihood function (LF) into the sum of two analogous terms. This decomposition makes it possible to carry out analytically all the statistical expectations involved in the Fisher information matrix (FIM). The new analytical CRLB expressions corroborate the previous attempts to evaluate the underlying bounds empirically. In the low-to-medium signal-to-noise ratio (SNR) region, the CRLB for code-aided (CA) estimation lies between the bounds for completely blind [non-data-aided (NDA)] and completely data-aided (DA) estimation schemes, thereby highlighting the effect of the coding gain. Most interestingly, in contrast to the NDA case, the CA CRLBs start to decay rapidly and reach the DA bounds at relatively small SNR thresholds. It will also be shown that contrary to the CRLB of the phase shift, the CRLB of the CFO improves in a multi-carrier system as compared to its counterpart in a single-carrier system. The derived bounds are also valid for LDPC-coded systems and they can be evaluated in the same way when the latter are decoded using the turbo principal.

## Frequency-Domain-Equalization-Aided Iterative Detection of Faster-than-Nyquist Signaling

- **Status**: ❌
- **Reason**: Faster-than-Nyquist 통신 송수신기/iterative detection + turbo, LDPC 무관. 떼어낼 바이너리 LDPC 디코더/HW/구성 기법 없음.
- **ID**: ieee:6850067
- **Type**: journal
- **Published**: May 2015
- **Authors**: Shinya Sugiura, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/6850067
- **Abstract**: A reduced-complexity three-stage-concatenated faster-than-Nyquist signaling (FTNS)-based transceiver architecture is proposed, which operates with the aid of soft decision (SoD) frequency-domain equalization (FDE) at the receiver. More specifically, the decoding algorithm conceived allows us to attain near-capacity performance as an explicit benefit of iterative detection, which is capable of eliminating the intersymbol interference imposed by FTNS. The proposed SoD FDE-aided FTNS detector has low decoding complexity that linearly increases upon increasing the FTNS block length and, hence, is particularly beneficial for practical long-dispersion scenarios. Furthermore, extrinsic information transfer charts are utilized for designing a near-capacity three-stage-concatenated turbo FTNS system, which exhibits an explicit turbo cliff in the low-signal-to-noise-ratio region, hence outperforming its conventional two-stage-concatenated FTNS counterpart.

## Tentpoles Scheme: A Data-Aided Channel Estimation Mechanism for Achieving Reliable Vehicle-to-Vehicle Communications

- **Status**: ❌
- **Reason**: V2V 채널추정(Tentpoles) 무선통신 응용, ECC는 부수 언급뿐 떼어낼 LDPC 기법 없음.
- **ID**: ieee:7001094
- **Type**: journal
- **Published**: May 2015
- **Authors**: Zheng Li, Fan Bai, Joseph A. Fernandez +1
- **PDF**: https://ieeexplore.ieee.org/document/7001094
- **Abstract**: IEEE 802.11p-based Dedicated Short Range Communications (DSRC) is considered a promising wireless technology for enhancing transportation safety and improving highway efficiency. One major challenge of IEEE 802.11p technology development ensuring its communication reliability in highly dynamic Vehicle-to-Vehicle (V2V) environments. In this paper, by investigating the characteristics of V2V channels through empirical measurements, we show that the decreased reliability of V2V communication is because the IEEE 802.11p design does not have sufficient number of training symbols in time domain and pilot subcarriers in frequency domain to enable estimation of the fast-changing V2V channels accurately. To tackle this challenge, we propose a new approach called Tentpoles scheme, which utilizes a small subset of data symbols and subcarriers protected by a strong Error Correction Code (ECC) to track and estimate V2V channel variations. Since this subset of data symbols and subcarriers provide dual-use, our Tentpoles scheme not only improves the accuracy of channel estimation and communication reliability, but has only a small impact on effective throughput. Through extensive simulations in synthetic V2V channels and emulation experiments using empirical measurements, our proposed Tentpoles scheme is shown to significantly outperform other V2V channel estimation and equalization methods in terms of communication reliability, at the cost of only moderate loss of throughput.

## Multicarrier airborne ultrasound transmission with piezoelectric transducers

- **Status**: ❌
- **Reason**: 초음파 OFDM 통신 시스템, LDPC 무관 채널코딩 부수 언급뿐 — 떼어낼 LDPC 기법 없음
- **ID**: ieee:7103530
- **Type**: journal
- **Published**: May 2015
- **Authors**: Alexander Ens, Leonhard M. Reindl
- **PDF**: https://ieeexplore.ieee.org/document/7103530
- **Abstract**: In decentralized localization systems, the received signal has to be assigned to the sender. Therefore, longrange airborne ultrasound communication enables the transmission of an identifier of the sender within the ultrasound signal to the receiver. Further, in areas with high electromagnetic noise or electromagnetic free areas, ultrasound communication is an alternative. Using code division multiple access (CDMA) to transmit data is ineffective in rooms due to high echo amplitudes. Further, piezoelectric transducers generate a narrow-band ultrasound signal, which limits the data rate. This work shows the use of multiple carrier frequencies in orthogonal frequency division multiplex (OFDM) and differential quadrature phase shift keying modulation with narrowband piezoelectric devices to achieve a packet length of 2.1 ms. Moreover, the adapted channel coding increases data rate by correcting transmission errors. As a result, a 2-carrier ultrasound transmission system on an embedded system achieves a data rate of approximately 5.7 kBaud. Within the presented work, a transmission range up to 18 m with a packet error rate (PER) of 13% at 10-V supply voltage is reported. In addition, the transmission works up to 22 m with a PER of 85%. Moreover, this paper shows the accuracy of the frame synchronization over the distance. Consequently, the system achieves a standard deviation of 14 μs for ranges up to 10 m.

## Fountain Code Design for the Y-Network

- **Status**: ❌
- **Reason**: Fountain/LT/Raptor 코드 분산설계(다항식 인수분해), erasure fountain은 떼어낼 채널 LDPC ECC 기법 없음.
- **ID**: ieee:7051206
- **Type**: journal
- **Published**: May 2015
- **Authors**: Reza Rafie Borujeny, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/7051206
- **Abstract**: This paper describes a novel approach for designing distributed fountain codes based on polynomial factorization. The proposed approach is used for the well known Y-network configuration. The suggested factorization approach is applicable to LT codes and Raptor codes or any other fountain code describable with a degree distribution. Simulation results verify the success of this technique.

## Massive Parallelization of the WRF GCE Model Toward a GPU-Based End-to-End Satellite Data Simulator Unit

- **Status**: ❌
- **Reason**: 기상모델 GPU 병렬화, ECC/LDPC와 무관
- **ID**: ieee:7110544
- **Type**: journal
- **Published**: May 2015
- **Authors**: Melin Huang, Bormin Huang, Xiaojie Li +3
- **PDF**: https://ieeexplore.ieee.org/document/7110544
- **Abstract**: Modern weather satellites provide more detailed observations of cloud and precipitation processes. To harness these observations for better satellite data assimilations, a cloud-resolving model, known as the Goddard Cumulus Ensemble (GCE) model, was developed and used by the Goddard Satellite Data Simulator Unit (G-SDSU). The GCE model has also been incorporated as part of the widely used weather research and forecasting (WRF) model. The computation of the cloud-resolving GCE model is time-consuming. This paper details our massively parallel design of GPU-based WRF GCE scheme. With one NVIDIA Tesla K40 GPU, the GPU-based GCE scheme achieves a speedup of ${\bf 361} \times $ as compared to its original Fortran counterpart running on one CPU core, whereas the speedup for one CPU socket (four cores) with respect to one CPU core is only ${\bf 3}.{\bf 9} \times $.

## Slepian-Wolf Coding for Broadcasting With Cooperative Base-Stations

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스코딩/BS 협력 방송 정보이론, 채널 ECC 아님.
- **ID**: ieee:7050289
- **Type**: journal
- **Published**: May 2015
- **Authors**: Roy Timo, Michele Wigger
- **PDF**: https://ieeexplore.ieee.org/document/7050289
- **Abstract**: We propose a base-station (BS) cooperation model for broadcasting a discrete memoryless source in a cellular or heterogeneous network. The model allows the receivers to use helper BSs to improve network performance, and it permits the receivers to have prior side information about the source. We establish the model's information-theoretic limits in two operational modes: In Mode 1, the helper BSs are given information about the channel codeword transmitted by the main BS, and in Mode 2 they are provided correlated side information about the source. Optimal codes for Mode 1 use hash-and-forward coding at the helper BSs; while, in Mode 2, optimal codes use source codes from Wyner's helper source-coding problem at the helper BSs. We prove the optimality of both approaches by way of a new list-decoding generalisation used in Theorem 6 of Tuncel (2006), and in doing so, show an operational duality between Modes 1 and 2.

## An Efficient Data Layout Scheme for Better I/O Balancing in RAID-6 Storage Systems

- **Status**: ❌
- **Reason**: RAID-6 MDS 기반 데이터 레이아웃(UPC) — LDPC ECC 아닌 패리티 배치, 떼어낼 LDPC 기법 없음.
- **ID**: ieee:11288452
- **Type**: journal
- **Published**: May 2015
- **Authors**: Ping Xie, Jian-Zhong Huang, Er-Wei Dai +2
- **PDF**: https://ieeexplore.ieee.org/document/11288452
- **Abstract**: Among redundant arrays of independent disks (RAID)-6 codes, maximum distance separable (MDS) based RAID-6 codes are popular because they have the optimal storage efficiency. Although vertical MDS codes exhibit better load balancing compared to horizontal MDS codes in partial stripes, an I/O unbalancing problem still exists in some vertical codes. To address this issue, we propose a novel efficient data layout, uniform P-code (UPC), to support highly balanced I/Os among P-coded disk arrays (i.e., PC). In UPC, the nonuniformly distributed information symbols in each parity chain of P-code are moved along their columns to other rows, thus enabling the parity chain to keep original parity relationships and tolerate double disk failures. The UPC scheme not only achieves optimal storage efficiency, computational complexity, and update complexity, but also supports better I/O balancing in the context of large-scale storage systems. We also conduct a performance study on reconstruction algorithms using an analytical model. Besides extensive theoretical analysis, comparative performance experiments are conducted by replaying real-world workloads under various configurations. Experimental results illustrate that our UPC scheme significantly outperforms the PC scheme in terms of average user response time. In particular, in the case of a 12-disk array, the UPC scheme can improve the access performance of the RAID-6 storage system by 29.9% compared to the PC scheme.

## Estimation and Detection on Uniform Hexagonal Array Models

- **Status**: ❌
- **Reason**: 자기기록 매체의 헥사고날 격자 데이터 검출/추정 문제, ECC·LDPC 기법 없음.
- **ID**: ieee:6953254
- **Type**: journal
- **Published**: May 2015
- **Authors**: Michael Carosino, Roger Wood, Jihoon Park +1
- **PDF**: https://ieeexplore.ieee.org/document/6953254
- **Abstract**: Magnetic recording at the highest areal density on conventional granular recording media uses $\sim 10$ grains to carry each bit of customer data. Efforts to reduce this number have focused on improving the resolution of the writing and reading processes and, in particular, on improving uniformity of the recording medium and on incorporating knowledge of the recording medium statistics into the detection process. This paper considers the extreme case of data detection on a perfect hexagonal array of grains. This paper looks at two aspects: 1) the estimation of the angle and positioning of the array with respect to the bit-steam and 2) the use of that information to assist data detection. At aggressive densities with very few grains per bit (GPB), the estimation proceeds well and the extra information is helpful in detection. With more GPB, the gains become small.

## Comparative analysis of low power novel encoders for Flash ADC in 45nm technology

- **Status**: ❌
- **Reason**: Flash ADC용 저전력 인코더 회로(45nm) — NAND 플래시 아닌 ADC 회로, ECC 무관
- **ID**: ieee:7225442
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Aditi Kar, Moushumi Das, Bipasha Nath +2
- **PDF**: https://ieeexplore.ieee.org/document/7225442
- **Abstract**: The electronics world is faced with various challenges when attempting to integrate analog signals with discrete or digital systems. The ADC is not a new concept b y any means, but is still a topic of interest when it comes to technology due to its inevitable necessity in many systems being used today. Power consumption in ICs was always a challenging issue. Most of the technology emphasizes on speed, accuracy, less power consumption. In almost all digital functioning, encoders are mandatory. Decreasing power consumption in an encoder is an area of strong desire. In this paper, we have designed two novel ultra low power encoders for Flash ADC application and also show its comparison with previous encoder available in literature. The work has been done on Tanner tool v15 in 45 nm technology with various DC voltage supplies.

## Sliceable bandwidth variable transponders for elastic optical networks: The idealist vision

- **Status**: ❌
- **Reason**: 탄력광망 transponder 아키텍처 — LDPC 무관
- **ID**: ieee:7322019
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: E. Riccardi, A. Pagano, E. Hugues-Salas +16
- **PDF**: https://ieeexplore.ieee.org/document/7322019
- **Abstract**: This paper describes the general architecture for a sliceable bandwidth variable transponder as identified within the IDEALIST European project. The capability of generate super-channels (optical connections with several adjacent optical sub-carriers) and the slice-ability (super-channels generated together but independently routed in the network towards different destinations) are the key elements of the considered architecture.

## An iterative bit flipping based decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: New bit-flipping decoding algorithm for LDPC using inter-stage data correlation — transferable BP/BF decoder improvement (category C).
- **ID**: ieee:7140214
- **Type**: conference
- **Published**: 6-7 May 20
- **Authors**: Sajjad Imani, Reza Shahbazian, Seyed Ali Ghorashi
- **PDF**: https://ieeexplore.ieee.org/document/7140214
- **Abstract**: In this paper a new decoding algorithm for low density parity check (LDPC) codes based on bit flipping (BF) is proposed. In the proposed algorithm, the BF criterion benefits the data correlation between the decoded and received signal in current and previous stages. The proposed algorithm also degrades the decoding probability of one code word to another one in the same codebook. Simulation results confirm our theoretical formulation and show a good enhancement in code error rate and bit error rate of the proposed decoding algorithm compared to the conventional ones.

## One-level LDPC lattice codes for the relay channels

- **Status**: ❌
- **Reason**: LDPC lattice codes for relay channels; lattice/Construction D' coding for relay networks, no transferable NAND binary LDPC decoder/HW/code-design technique.
- **ID**: ieee:7140213
- **Type**: conference
- **Published**: 6-7 May 20
- **Authors**: Hassan Khodaiemehr, Dariush Kiani, Mohammad-Reza Sadeghi
- **PDF**: https://ieeexplore.ieee.org/document/7140213
- **Abstract**: LDPC lattices were first family of lattices which have efficient decoding algorithm in high dimensions. An LDPC lattice can be constructed from Construction D' and a number of nested LDPC codes. When we consider one code as underlying code of these lattices, one-level LDPC lattices will be obtained. In this paper we propose a new encoding and decoding method for one-level LDPC lattices. We also establish an efficient shaping method for these lattices based on hypercube shaping. Then, based on this encoding and decoding, we propose the implementation of block Markov encoding for one-way relay networks, using obtained one-level LDPC lattice codes. Our proposed decoding algorithm has lower complexity than those given for LDLC lattices.

## Comparative analysis of single mode and multimode QC-LDPC decoder using modified belief propagation algorithm

- **Status**: ✅
- **Reason**: C/D: modified BP 기반 QC-LDPC 디코더 + partially parallel Verilog/FPGA HW, 이식 가능
- **ID**: ieee:7150811
- **Type**: conference
- **Published**: 28-30 May 
- **Authors**: M.V. Mankar, G.M. Asutkar, P.K. Dakhole
- **PDF**: https://ieeexplore.ieee.org/document/7150811
- **Abstract**: Low density parity check codes (LDPC) are appearing in an increasing number of applications which shows a performance close to the Shannon limit. The near Shannon limit error correction capability has lead LDPC codes to become the coding technique of choice in many communications and storage systems since their introduction. LDPC have good error correcting performance which enables efficient and reliable communication. Quasi-cyclic LDPC codes known as a subclass of LDPC codes are used whose parity check matrices consists of circulant permutation matrices. This character of QC-LDPC codes opens the door for the multi-mode. In the present work partially parallel architecture for single mode and multi-mode quasi-cyclic low density parity check (QC-LDPC) decoders have been designed using modified belief propagation algorithm. QC-LDPC codes require less memory as compared to LDPC codes and resource occupied by the single mode decoder is only a little more than the multi-mode decoder. This decoder is modeled using Verilog software, synthesized and performed place and route for the design using Xilinx ISE 13.2.

## The IEEE 802.11n wireless LAN for real-time industrial communication

- **Status**: ❌
- **Reason**: IEEE 802.11n WLAN 산업통신 성능 연구 — LDPC ECC 무관, 떼어낼 기법 없음
- **ID**: ieee:7160568
- **Type**: conference
- **Published**: 27-29 May 
- **Authors**: Federico Tramarin, Stefano Vitturi, Michele Luvisotto +1
- **PDF**: https://ieeexplore.ieee.org/document/7160568
- **Abstract**: In the last years, IEEE 802.11 Wireless LANs (WLANs) have proved their effectiveness for a wide range of real-time industrial communication applications. Nonetheless, the enhancements at the PHY and MAC layers introduced by the IEEE 802.11n amendment have not yet been adequately addressed in the context of industrial communication. In this paper we investigate the impact of some IEEE 802.11n new features on some important performance figures for industrial applications, such as timeliness and reliability.

## Asymptotic distance properties of protograph-based spatially coupled LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 SC-LDPC의 자유거리 점근 분석 — 비이진 LDPC이며 순수 이론 bound, 제외
- **ID**: ieee:7133099
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Kechao Huang, David G. M. Mitchell, Xiao Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/7133099
- **Abstract**: In this paper, asymptotic methods are used to form lower and upper bounds on the typical free distance growth rate of ensembles of periodically time-varying protograph-based spatially coupled low-density parity-check (SC-LDPC) codes over GF(q). By evaluating and comparing these bounds, we find that the typical free distance of q-ary SC-LDPC codes increases linearly with constraint length and that the bounds coincide for a sufficiently large period. In particular, we show that the free distance to constraint length ratio of (3, 6)-regular q-ary SC-LDPC code ensembles exceeds the minimum distance to block length ratio of an underlying q-ary LDPC block code (LDPC-BC) ensemble. We also show that, similar to the minimum distance growth rate of the (3, 6)-regular q-ary LDPC-BC ensemble, the free distance growth rate of (3, 6)-regular q-ary SC-LDPC code ensembles increases with the field size q up to a certain point, and then it decreases as q increases further.

## Design of LDPC codes for the q-ary partial erasure channel

- **Status**: ❌
- **Reason**: q-ary partial erasure channel용 LDPC 차수분포 설계 — 비이진+erasure 채널, NAND 채널 ECC 아님
- **ID**: ieee:7133125
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/7133125
- **Abstract**: In this paper, we discuss practical design of low-density parity-check (LDPC) codes for the q-ary partial erasure channel (QPEC). This channel is an extension of the binary erasure channel (BEC), where partial information on the output is available. We provide a linear programming (LP) optimization for the design of good degree distributions, and compare our code design results to codes obtained using an LP optimization formulated for the BEC. We show superior performance in terms of code rate and complexity, when designing an LDPC code for a desired decoding threshold.

## Polar codes for magnetic recording channels

- **Status**: ❌
- **Reason**: polar 코드를 자기기록 ISI 채널 컴포넌트로 사용 — 비-LDPC 부호 중심, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:7133166
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Aman Bhatia, Veeresh Taranalli, Paul H. Siegel +6
- **PDF**: https://ieeexplore.ieee.org/document/7133166
- **Abstract**: Polar codes provably achieve the capacity of binary memoryless symmetric (BMS) channels with low complexity encoding and decoding algorithms, and their finite-length performance on these channels, when combined with suitable decoding algorithms (such as list decoding) and code modifications (such as a concatenated CRC code), has been shown in simulation to be competitive with that of LDPC codes. However, magnetic recording channels are generally modeled as binary-input intersymbol interference (ISI) channels, and the design of polar coding schemes for these channels remains an important open problem. Current magnetic hard disk drives use LDPC codes incorporated into a turbo-equalization (TE) architecture that combines a soft-output channel detector with a soft-input, soft-output sum-product algorithm (SPA) decoder. An interleaved coding scheme with a multistage decoding (MSD) architecture with LDPC codes as component codes has been proposed as an alternative to TE for ISI channels. In this work, we investigate the use of polar codes as component codes in the TE and MSD architectures. It is shown that the achievable rate of the MSD scheme converges to the symmetric information rate of the ISI channel when the number of interleaves is large. Simulations results comparing the performance of LDPC codes and polar codes in TE and MSD architectures are presented.

## A new coding method for a multiple-access system with a large number of active users

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 멀티액세스 코딩 — 바이너리 LDPC 한정 기준에 따라 제외
- **ID**: ieee:7133114
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Alexey Frolov, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/7133114
- **Abstract**: The paper addresses the problem of constructing an asynchronous multiple access system for a multi-user Q-frequency channel with additive white Gaussian noise (AWGN). We propose a coding scheme for the channel which allows a large number of users to work simultaneously in the system. The scheme combines the ideas of Frequency Shift Keying (FSK) and Frequency Hopping Spread Spectrum (FHSS). The major component of the scheme is a non-binary low-density parity-check (LDPC) code. The efficiency of the resulting multiple-access system is shown by simulations.

## On adaptive linear programming decoding of ternary linear codes

- **Status**: ❌
- **Reason**: ternary(GF(3)) 선형부호의 LP 디코딩 — 비이진 부호 대상이라 제외
- **ID**: ieee:7133150
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Eirik Rosnes, Michael Helmling
- **PDF**: https://ieeexplore.ieee.org/document/7133150
- **Abstract**: In this work, we consider adaptive linear programming (LP) decoding of ternary linear codes, i. e., linear codes over the finite field Fq with q = 3 elements. In particular, we characterize completely the codeword polytope (or the convex hull) of the binary image, under Flanagan's embedding, of a ternary single parity-check code. Then, this characterization is used to develop an efficient adaptive LP decoder for ternary codes. Numerical experiments confirm that this decoder is very efficient compared to a static LP decoder and scales well with both block length and check node degree. Finally, we briefly consider the case of nonbinary codes over the finite field Fq with q = 3m elements, where m > 1 is a positive integer.

## Polar coding for the broadcast channel with confidential messages

- **Status**: ❌
- **Reason**: polar 코딩 기반 wiretap 보안 — 비-LDPC+보안, 이식 가능한 BP 기법 없음
- **ID**: ieee:7133142
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Rémi A. Chou, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/7133142
- **Abstract**: We develop a low-complexity and secrecy capacity achieving polar coding scheme for the discrete memoryless wiretap channel. Our scheme extends previous work by using a nearly optimal amount of uniform randomness in the stochastic encoder, and avoiding assumptions regarding the symmetry or degraded nature of the channels. The price paid for these extensions is that the encoder and decoder are required to share a secret seed of negligible size. We also highlight a close conceptual connection between the proposed polar coding scheme and a random binning proof of the secrecy capacity.

## A comparison of skewed and orthogonal lattices in Gaussian wiretap channels

- **Status**: ❌
- **Reason**: 가우시안 도청채널 격자 coset 코딩 비교 — 보안/격자 이론, LDPC ECC와 무관
- **ID**: ieee:7133106
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Alex Karrila, Camilla Hollanti
- **PDF**: https://ieeexplore.ieee.org/document/7133106
- **Abstract**: We consider lattice coset-coded transmissions over a wiretap channel with additive white Gaussian noise (AWGN). Examining a function that can be interpreted as either the legitimate receiver's error probability or the eavesdropper's correct decision probability, we rigorously show that, albeit offering simple bit labeling, orthogonal nested lattices are suboptimal for coset coding in terms of both the legitimate receiver's and the eavesdropper's probabilities.

## Some “goodness” properties of LDA lattices

- **Status**: ❌
- **Reason**: LDPC 기반 LDA 격자의 패킹/MSE 양자화 goodness 증명 — 순수 격자 이론, 디코더/HW/구성 기여 없음
- **ID**: ieee:7133102
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Shashank Vatedka, Navin Kashyap
- **PDF**: https://ieeexplore.ieee.org/document/7133102
- **Abstract**: We study some structural properties of Construction-A lattices obtained from low-density parity-check (LDPC) codes over prime fields. Such lattices are called low-density Construction-A (LDA) lattices, and have been shown to achieve the capacity of the AWGN channel under closest lattice-point decoding. Also, simulations suggest that they perform well under belief propagation decoding. In this work, we prove that LDA lattices are good for packing and mean squared error (MSE) quantization, and that their duals are good for packing. With this, we can conclude that codes constructed using nested LDA lattices can achieve the capacities of the AWGN channel and the dirty paper channel, the rates guaranteed by the compute-and-forward protocol, and the best known rates for bidirectional relaying with perfect secrecy.

## ADMM decoding of error correction codes: From geometries to algorithms

- **Status**: ✅
- **Reason**: ADMM 디코딩 서브루틴(ℓ1 ball projection)은 부호 비의존적 BP-LP 디코더 기법으로 바이너리 LDPC에 이식 가능(C)
- **ID**: ieee:7133156
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7133156
- **Abstract**: Many code constraints can be represented using factor graphs. By relaxing these factorable coding constraints to linear constraints, it is straightforward to form a decoding optimization problem. Furthermore, by pairing these factor graphs with the alternating directions method of multipliers (ADMM) technique of large-scale optimization, one can develop distributed algorithms to solve the decoding optimization problems. However, the non-trivial part has always been developing an efficient algorithm for the subroutines of ADMM, which directly relates to the geometries of the relaxed coding constraints. In this paper, we focus on summarizing existing results and distilling insights to these problems. First, we review the ADMM formulation and geometries involved in the subroutines. Next, we present a linear time algorithm for projecting onto an ℓ1 ball with box constraints.

## Encoding and decoding algorithms for LP-decodable multipermutation codes

- **Status**: ❌
- **Reason**: 멀티퍼뮤테이션 부호의 LP/ADMM 디코딩, 순열부호 전용이고 바이너리 LDPC BP로 이식되는 기법 아님
- **ID**: ieee:7133088
- **Type**: conference
- **Published**: 26 April-1
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7133088
- **Abstract**: LP-decodable multipermutation codes are a class of multipermutation codes that can be decoded using linear programming (LP). These codes are defined using linearly constrained multipermutation matrices, which are binary matrices that satisfy particular row sum and column sum constraints. Although generic LP solvers are capable of solving the LP decoding problem, they are not efficient in general because they do not leverage structures of the problem. This motivates us to study efficient decoding algorithms. In this paper, we focus on encoding and decoding algorithms for LP-decodable multipermutation codes. We first describe an algorithm that “ranks” multipermutations. In other words, it maps consecutive integers, one by one, to an ordered list of multipermutations. By leveraging this algorithm, we develop an encoding algorithm for a code proposed by Shieh and Tsai. Regarding decoding algorithms we propose an iterative decoding algorithm based on the alternating direction method of multipliers (ADMM), each iteration of which can be solved efficiently using off-the-shelf techniques. Finally, we study decoding performances of different decoders via simulation.

## Deterministic construction of Quasi-Cyclic sparse sensing matrices from one-coincidence sequence

- **Status**: ❌
- **Reason**: QC-LDPC 기반 압축센싱 sensing matrix 구성 — 채널 ECC 아닌 CS 응용, 떼어낼 디코더/구성 기여 없음
- **ID**: ieee:7148870
- **Type**: conference
- **Published**: 25-29 May 
- **Authors**: Weijun Zeng, Huali Wang, Guangjie Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/7148870
- **Abstract**: In this paper, a new class of deterministic sparse matrices derived from Quasi-Cyclic (QC) low-density parity-check (LDPC) codes is presented for compressed sensing (CS). In contrast to random and other deterministic matrices, the proposed matrices are generated based on circulant permutation matrices, which require less memory for storage and low computational cost for sensing. Its size is also quite flexible compared with other existing fixed-sizes deterministic matrices. Furthermore, both the coherence and null space property of proposed matrices are investigated, specially, the upper bounds of signal sparsity k is given for exactly recovering. Finally, we carry out many numerical simulations and show that our sparse matrices outperform Gaussian random matrices under some scenes.

## WiCOD: Wireless control plane serving an all-optical data center

- **Status**: ❌
- **Reason**: 데이터센터 무선 제어 평면 아키텍처 — LDPC/ECC 무관
- **ID**: ieee:7151086
- **Type**: conference
- **Published**: 25-29 May 
- **Authors**: Tugcan Aktaş, Chang-Heng Wang, Tara Javidi
- **PDF**: https://ieeexplore.ieee.org/document/7151086
- **Abstract**: A novel architecture for the future data center networks with possibly up to a thousand of Top of the Rack (ToR) switches is proposed. The proposed architecture, WiCOD, relies on a wireless control plane serving an all-optical data plane. The first contribution of the work is the separation of the data and the control planes: while the data is switched between the ToR switches in an all-optical high rate network, the network state and control information is continuously conveyed to and from a central unit over an ultra low-latency wireless network. A proof of concept for this architecture is also presented by considering the initial design possibilities for each one of the planes. In order to obtain low packet delays, the data plane scheduling policies take non-zero reconfiguration and monitoring delays into consideration. The results prove that very low queueing delays are guaranteed for strictly frequent updates on the network state. Based on this observation, a technique for monitoring of ToR switch queue occupancy information is purposed. This monitoring technique uses mmWave wireless communications via a spatially adapted MIMO Orthogonal Frequency Division Multiple Access (MIMO-OFDMA) over a static frequency selective channel with large number of densely packed ToRs. The reduced monitoring delays, offered by this low-latency radio access technology, makes the fine-grained and adaptive circuit switching feasible and, in turn, enables a high utilization of optical switches.

## From paley graphs to deterministic sensing matrices with real-valued Gramians

- **Status**: ❌
- **Reason**: Paley graph 기반 압축센싱 결정론 행렬 — LDPC/ECC와 무관
- **ID**: ieee:7148915
- **Type**: conference
- **Published**: 25-29 May 
- **Authors**: Arash Amini, Hamed Bagh-Sheikhi, Farokh Marvasti
- **PDF**: https://ieeexplore.ieee.org/document/7148915
- **Abstract**: The performance guarantees in recovery of a sparse vector in a compressed sensing scenario, besides the reconstruction technique, depends on the choice of the sensing matrix. The so-called restricted isometry property (RIP) is one of the well-used tools to determine and compare the performance of various sensing matrices. It is a standard result that random (Gaussian) matrices satisfy RIP with high probability. However, the design of deterministic matrices that satisfy RIP has been a great challenge for many years now. The common design technique is through the coherence value (maximum modulus correlation between the columns). In this paper, based on the Paley graphs, we introduce deterministic matrices of size q+1/2 × q with q a prime power, such that the corresponding Gram matrix is real-valued. We show that the coherence of these matrices are less than twice the Welch bound, which is a lower bound valid for general matrices. It should be mentioned that the introduced matrix differs from the equiangular tight frame (ETF) of size q-1/2 × q arising from the Paley difference set.

## A 3.46 Gb/s (9141,8224) LDPC-based ECC scheme and on-line channel estimation for solid-state drive applications

- **Status**: ✅
- **Reason**: NAND SSD용 LDPC ECC, MGDBF+min-sum 다중전략 디코더 및 온라인 채널추정 — 직접 해당(A/C/D)
- **ID**: ieee:7168917
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Kin-Chu Ho, Chih-Lung Chen, Yen-Chin Liao +2
- **PDF**: https://ieeexplore.ieee.org/document/7168917
- **Abstract**: As the reliability of NAND Flash memory keeps degrading, Low-Density Parity-Check (LDPC) codes are widely proposed to extend the endurance of Solid State Drive (SSD). However, implementing powerful decoding algorithm such as soft min-sum algorithm with high decoding speed comes along with higher hardware cost. To achieve efficient hardware cost, we propose a multi-strategy ECC scheme which consists of modified gradient descent bit-flipping (MGDBF), hard min-sum, and soft min-sum decoders. The MGDBF decoder aims to correct most of the erroneous codewords with advantages of high decoding throughput and low hardware cost, while the soft min-sum decoder is targeted to correct codewords with large number of errors under moderate decoding throughput and reasonable hardware cost. In addition, we propose a bi-sectional channel estimation technique which enables on-line estimation of distribution to generate accurate soft information for LDPC decoding with low complexity. The ECC codec and the complete Toggle DDR 1.0 NAND interface control circuits are integrated and fabricated in 90nm CMOS process. The throughput of proposed MGDBF decoder achieves 3.46 Gb/s which satisfies the throughput requirement of both toggle DDR 1.0 and 2.0 NAND interfaces.

## Latency-optimized stochastic LDPC decoder for high-throughput applications

- **Status**: ✅
- **Reason**: 확률적(stochastic) LDPC 디코더 지연 단축 신규 전략(LUT 초기화, BF 후처리) — 이식 가능 디코더/HW(C/D)
- **ID**: ieee:7169329
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Di Wu, Yun Chen, Qichen Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/7169329
- **Abstract**: Stochastic decoding can be applied to Low-Density Parity-Check codes in order to achieve high throughput with less area. However, most architectures suffer from large decoding latencies, due to the mechanism of stochastic computation. In this paper, three novel strategies, including the LUT-based initialization, the posterior-information-based hard decision and the Bit-Flipping-based post processing, are proposed in order to reduce decoding latency and hence improve throughput. For the standard IEEE 802.3an (2048, 1723) code, simulation indicates 75.7% reduction in average decoding cycles at 4.5 dB with satisfied bit error rate. Moreover, hardware implementation shows that the area of variable node units is reduced significantly in SMIC 65 nm technology.

## Refresh-free dynamic standard-cell based memories: Application to a QC-LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC 디코더의 동적 SCM 메모리로 면적 44% 절감 HW 기법 — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:7168911
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Pascal Meinerzhagen, Andrea Bonetti, Georgios Karakonstantis +3
- **PDF**: https://ieeexplore.ieee.org/document/7168911
- **Abstract**: The area and power consumption of low-density parity check (LDPC) decoders are typically dominated by embedded memories. To alleviate such high memory costs, this paper exploits the fact that all internal memories of a LDPC decoder are frequently updated with new data. These unique memory access statistics are taken advantage of by replacing all static standard-cell based memories (SCMs) of a prior-art LDPC decoder implementation by dynamic SCMs (D-SCMs), which are designed to retain data just long enough to guarantee reliable operation. The use of D-SCMs leads to a 44% reduction in silicon area of the LDPC decoder compared to the use of static SCMs. The low-power LDPC decoder architecture with refresh-free D-SCMs was implemented in a 90nm CMOS process, and silicon measurements show full functionality and an information bit throughput of up to 600 Mbps (as required by the IEEE 802.11n standard).

## Efficient realization of probabilistic gradient descent bit flipping decoders

- **Status**: ✅
- **Reason**: PGDBF 비트플립 디코더 HW 구현(LFSR/IVRG 랜덤생성) — 이식 가능 디코더/HW(C/D)
- **ID**: ieee:7168928
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Khoa Le, David Declercq, Fakhreddine Ghaffari +4
- **PDF**: https://ieeexplore.ieee.org/document/7168928
- **Abstract**: In this paper, several implementations of the recently introduced PGDBF decoder for LDPC codes are proposed. In [2], the authors show that using randomness in bit-flipping decoders can greatly improve the error correction performance. In this paper, two models of random generators are proposed and compared through hardware implementation and performance simulation. A conventional implementation of the random generator through LFSR as a first design, and a new approach using binary sequences that are produced by the LDPC decoder, named IVRG, as second design. We show that both implementation of the PGDBF improve greatly the error correction performance, while maintaining the same large throughtput. However, the performance gain requires a large hardware overhead in the case of LFSR-PGDBF, while the overhead is limited to only 10% in the case of the IVRG-PGDBF.

## A 630 Mbps non-binary LDPC decoder for FPGA

- **Status**: ❌
- **Reason**: GF(16) 비이진 NB-LDPC 디코더 — 비이진 LDPC 제외
- **ID**: ieee:7169065
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: J. O. Lacruz, F. García-Herrero, M. J. Canet +2
- **PDF**: https://ieeexplore.ieee.org/document/7169065
- **Abstract**: A high-speed non-binary LDPC decoder based on Trellis Min-Max algorithm with layered schedule is presented. The proposed approach compresses the check-node output messages into a reduced set, decreasing the number of messages sent to the variable node. Additionally, the memory resources from the layered architecture are reduced. The proposed decoder was implemented for the (2304,2048) NB-LDPC code over GF(16) on a Virtex-7 FPGA and in a 90 nm CMOS process. Our implementation outperforms state-of-the-art NB-LDPC decoder implementations for both technologies, achieving a throughput of 630 and 965 Mbps, respectively.

## TTCN: A new approach for low-power split-row LDPC decoders

- **Status**: ✅
- **Reason**: Split-Row LDPC 디코더 저전력 TTCN 기법, 체크노드 게이팅 — 이식 가능 HW 아키텍처(D)
- **ID**: ieee:7169068
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Mohammad Shahrad, Mahdi Shabany
- **PDF**: https://ieeexplore.ieee.org/document/7169068
- **Abstract**: Split-Row technique is proved to be one of the most effective methods to reduce the routing complexity of fully-parallel LDPC decoders. This technique is based on the idea of splitting each check node processor to multiple smaller processors. This paper introduces a new method, to increase the power-efficiency of Split-Row LDPC decoders. The proposed method is called trust to the truthful check node (TTCN), enabling the decoder to only depend on a portion of check node processors at specific decoding iterations. This leads to an average reduction of 30%-40% in the check node dynamic power consumption. This is achieved by means of trust to a minority of check node processors and gating the others. In fact, a great side effect of the proposed method is also a slight improvement in the error performance.

## Fast estimation of error floor effect for irregular low-density parity-check codes

- **Status**: ✅
- **Reason**: E: irregular 바이너리 LDPC error floor 저감(girth/EMD/short cycle 지표) — 이식 가능 코드 설계 기법
- **ID**: ieee:7147163
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Alexei A. Ovinnikov, Vladimir V. Vityazev
- **PDF**: https://ieeexplore.ieee.org/document/7147163
- **Abstract**: The article summarizes a comparison of numerous irregular low-density parity-check codes using a set of metrics such as girth, number of short cycles in Tanner graph and extrinsic message degree (EMD). Based on this these metrics, we analyze how to decrease error floor for such codes with no negative effect to threshold.

## The performance of multithreshold decoder over fading channels

- **Status**: ❌
- **Reason**: self-orthogonal code용 multithreshold decoder, LDPC는 비교 대상일 뿐 — 비-LDPC 부호, 이식 기법 없음
- **ID**: ieee:7147162
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: V.V. Zolotarev, G.V. Ovechkin, D.A. Shevlyakov
- **PDF**: https://ieeexplore.ieee.org/document/7147162
- **Abstract**: Multithreshold decoders (MTD) for self-orthogonal codes (SOC) are discussed. It's known MTD can provide near optimum decoding with linear complexity only. Bit-error rate performance of MTD in multipath Rayleigh and Rician fading channels is analyzed. Several questions of application of MTD with orthogonal frequency division multiplexing and multiple-input and multiple output technology for improving reliability of communication with unmanned vehicles are discussed. The performance of multithreshold decoders in such conditions is presented. Comparison with decoders for DVB-S2 low-density parity-check codes is presented. It's shown MTD provides comparable with LDPC decoders performance at much lower complexity.

## Generalized Error Locating Codes with Soft Decoding of Inner Codes

- **Status**: ❌
- **Reason**: GEL 코드(error-locating code)의 inner code soft decoding으로 비-LDPC 부호이며 LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:7147689
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Igor Zhilin, Fedor Ivanov, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/7147689
- **Abstract**: In this paper we propose to consider a generalized error-locating code (GEL-code) as a possible candidate for data transmission systems that require high code rates along with strict requirements on wrong decoding probability. The paper describes the construction of the GEL-code and the algorithms for encoding and decoding. The main idea is to implement a soft decoding of the inner codes. It will be shown that such approach results in better performance than hard decision decoding of inner codes. We present a method for constructing GEL code (with the minimal redundancy) that guarantees that the probability of wrong decoding will be less than required one (for a given channel error probability). Numerical results for a maximal achievable code rate depending on input signal-noise ratio on code symbol are presented.

## Fast Design Space Exploration Using Vivado HLS: Non-binary LDPC Decoders

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC 디코더 HLS 설계 — non-binary LDPC는 제외 대상
- **ID**: ieee:7160047
- **Type**: conference
- **Published**: 2-6 May 20
- **Authors**: Joao Andrade, Nithin George, Kimon Karras +4
- **PDF**: https://ieeexplore.ieee.org/document/7160047
- **Abstract**: Computing on field-programmable gate arrays (FPGAs) has been receiving continued interest as it provides high performance at relatively low power budgets, while avoiding the high non-recurring engineering (NRE) costs associated with ASIC designs. However, FPGA development is typically performed using register transfer level (RTL) languages which make the design process protracted and error-prone when compared to software design flows. To ease these problems, high-level synthesis (HLS) tools have been introduced which abstract away the RTL architecture description from the designer. In this work we explore the design space of a nonbinary GF (q) low-density parity-check (LDPC) decoder using Vivado HLS and compare it with state-of-the-art RTL designs.

## Design of LDPC code ensembles with fast convergence properties

- **Status**: ✅
- **Reason**: 유한 반복수 최적화 LDPC 앙상블 설계(EXIT+differential evolution), GLDPC 포함 — 이식 가능 코드설계(E)
- **ID**: ieee:7185085
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Ian P. Mulholland, Enrico Paolini, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7185085
- **Abstract**: The design of low-density parity-check (LDPC) code ensembles optimized for a finite number of decoder iterations is investigated. Our approach employs EXIT chart analysis and differential evolution to design such ensembles for the binary erasure channel and additive white Gaussian noise channel. The error rates of codes optimized for various numbers of decoder iterations are compared and it is seen that in the cases considered, the best performance for a given number of decoder iterations is achieved by codes which are optimized for this particular number. The design of generalized LDPC (GLDPC) codes is also considered, showing that these structures can offer better performance than LDPC codes for low-iteration-number designs. Finally, it is illustrated that LDPC codes which are optimized for a small number of iterations exhibit significant deviations in terms of degree distribution and weight enumerators with respect to LDPC codes returned by more conventional design tools.

## LDPC coded modulation schemes with largely unequal error protection

- **Status**: ❌
- **Reason**: 무선 UEP 코드변조 + 물리계층 보안 응용, 떼어낼 NAND용 디코더/HW/코드설계 신규 기법 없음
- **ID**: ieee:7185084
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Giacomo Ricciutelli, Marco Baldi, Nicola Maturo +1
- **PDF**: https://ieeexplore.ieee.org/document/7185084
- **Abstract**: Coding and modulation schemes able to achieve unequal error protection are of interest for many applications in which parts of the payload must be differently protected against the noise. They are also useful for physical layer security of transmissions over the broadcast channel with confidential messages. Classical design approaches aim at optimizing the performance over all the protection classes, independently of the separation between them. We instead propose a solution to improve the performance over the most protected bits, at the expense of performance over the least protected ones. This allows to design coded modulation schemes with largely unequal error protection. We also consider the use of high order modulations, and propose a technique to study the performance over each protection class in the asymptotic regime of infinite code length.

## Evaluation of the robustness of LDPC encoders to hardware noise

- **Status**: ✅
- **Reason**: faulty HW에서 LDPC 인코더 견고성 분석·인코딩 에러확률·저복잡도 인코딩 비교 — HW/구성 관점 이식 가능(D)
- **ID**: ieee:7185092
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Elsa Dupraz, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/7185092
- **Abstract**: This paper analyzes the robustness of Low Density Parity Check (LDPC) encoders on faulty hardware. The faulty hardware effect on the encoder is represented by an error model at the XOR gate level. We review the existing LDPC encoding solutions in the works of Richardson and Urbante (2001) and Chen et al. (2005) and the code constructions in the works of Ping et al. (2001), Jin et al. (2000), and Garcia-Frias and Zhong (2003) that guarantee low encoding complexity. For each of the existing solutions, we provide the analytic expression of the encoding error probability, and we use it to evaluate the robustness of the encoders to hardware noise. We then identify the two best encoding solutions in terms of robustness and we compare their performance with Monte-Carlo simulations.

## On coding for Faster-Than-Nyquist signaling

- **Status**: ❌
- **Reason**: FTN 시그널링용 sparse 그래프 코드 설계, FTN 검출·디코딩 결합 응용 특이적이라 NAND 이식 기법 약함
- **ID**: ieee:7185093
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Romain Tajan, Bouchra Benammar, Charly Poulliat +1
- **PDF**: https://ieeexplore.ieee.org/document/7185093
- **Abstract**: In this paper, we study the design of sparse graph based codes for Faster-Than-Nyquist (FTN) signaling. Using an asymptotic approach based on EXIT charts, we show that good low-density parity check codes can be designed that perform well under iterative detection and decoding and that have better performance than a FTN scheme using a code optimized for the additive white Gaussian noise channel.

## SC-LDPC codes over the block-fading channel: Robustness to a synchronisation offset

- **Status**: ✅
- **Reason**: SC-LDPC 데이터 할당 기반 동기 오프셋 견고성 — 블록페이딩 응용이나 SC-LDPC 구성 기법 이식 가능(E), 애매하여 살림
- **ID**: ieee:7185094
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Iryna Andriyanova, Najeeb Ul Hassan, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/7185094
- **Abstract**: Spatially-Coupled LDPC (SC-LDPC) codes have been recently shown to be very efficient for transmissions over nonergodic channels, in particular over block-fading channels [1]. In fact, it is possible to design a SC-LDPC code with any given code diversity [2]. In this work, we investigate the performance of SC-LDPC codes over block-fading channels, assuming a mismatch (or offset) between the first bit of a transmission packet and a first bit of a codeword. Such a mismatch is called the synchronisation offset, and it has a negative impact on the code diversity. We propose a data-allocation scheme for SC-LDPC codes that allows to obtain a robustness to the synchronisation offset. Combined together with the code design from [2], it allows to design efficient SC-LDPC codes, whose performance degrades only slowly under imperfect transmission conditions.

## Hermite polynomials based characterization of the received LLR's distribution in OFDM transmissions

- **Status**: ❌
- **Reason**: OFDM 수신 LLR 분포의 Hermite 다항식 특성화(성능예측). 디코더/HW/구성으로 이어지지 않는 분석 기법, 무선 응용.
- **ID**: ieee:7185076
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Mihály Varga, Vasile Bota, Horia Hedeşiu
- **PDF**: https://ieeexplore.ieee.org/document/7185076
- **Abstract**: The increased demand of low-latency and spectrally efficient wireless transmissions requires accurate performance prediction mechanisms. A widely used performance prediction method for coded multicarrier transmissions applying iteratively decoded error correction codes is based on the employment of the mean mutual information of the coded bit. A precise knowledge at the transmitter site of the log likelihood ratios distribution at the receiver facilitates the accurate performance prediction and unambiguous modeling of the decoder's behavior in a multiphase transmission. This paper proposes an analytical method to characterize the distribution of the received bits log likelihood ratios using a limited number of parameters. The paper also evaluates the accuracy provided by the proposed theoretical method by comparing its results to the ones obtained from measurements. The performance evaluation shows that the proposed method provides good accuracies both for transmissions over Gaussian and frequency-selective channels.

## Performance Characterization of LDPC Codes for Large-Volume NAND Flash Data

- **Status**: ✅
- **Reason**: A. NAND 플래시 LDPC 성능 특성화 + soft info 품질 채널 metric 제안 — NAND 직접
- **ID**: ieee:7150301
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Patrick Khayat, Mustafa Kaynak, Sivagnanam Parthasarathy +1
- **PDF**: https://ieeexplore.ieee.org/document/7150301
- **Abstract**: High bit error rates of next-generation flash devices necessitate the use of more powerful error correction codes (ECCs), such as low-density parity-check (LDPC) codes, instead of the legacy Bose-Chaudhuri-Hocquenghem (BCH) codes. Unlike algebraic codes, the random nature of LDPC codes as well as their ability to use soft information requires the use of Monte Carlo (MC) simulations to evaluate code performance. Given a large volume of NAND data, this can pose resource challenges both in terms of simulation platforms and time needed for the Monte Carlo simulations. In order to overcome these challenges, we introduce a new channel metric in this paper to quantify the quality of soft information and propose a practical LDPC code performance characterization methodology.

## LDPC Soft Decoding with Reduced Power and Latency in 1X-2X NAND Flash-Based Solid State Drives

- **Status**: ✅
- **Reason**: A. NAND 플래시 SSD에서 LDPC soft decoding 전력/지연 최적화 (NAND-Assisted Soft Decision) — 직접 해당
- **ID**: ieee:7150293
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Lorenzo Zuolo, Cristian Zambelli, Piero Olivo +2
- **PDF**: https://ieeexplore.ieee.org/document/7150293
- **Abstract**: The reliability of the non-volatile NAND flash memories, measured in terms of Raw Bit Error Rate (RBER), is reaching critical levels for traditional error detection and correction. Therefore, to ensure data trustworthiness in nowadays NAND flash-based Solid State Drives, it becomes essential exploiting powerful correction algorithms such as the Low Density Parity Check (LDPC). However, the burdens of this approach materialize in an increased NAND flash power consumption due to the increased memory read latencies that translates in limited disk performance. In this work it is performed a comparison between a standard LDPC decoding approach based on hard and soft decisions and an optimized solution called LDPC NAND- Assisted Soft Decision. The simulation results on 2X, 1X and mid-1X MLC NAND flash-based Solid State Drives in terms of NAND flash I/O power consumption, disk read latencies and performance, favor the adoption of the presented solution.

## Enhancing the error-correcting performance of LDPC codes for LTE and WiFi

- **Status**: ✅
- **Reason**: LTE/WiFi LDPC용 수정 SPA 디코더 제안(디코딩셋 활용, 동일 반복수에서 성능 개선); 부호 비의존 BP 개선 기법이라 NAND 이식 가능(C)
- **ID**: ieee:7148600
- **Type**: conference
- **Published**: 15-16 May 
- **Authors**: Insah Bhurtah, Pierre Clarel Catherine, K.M. Sunjiv Soyjaudah
- **PDF**: https://ieeexplore.ieee.org/document/7148600
- **Abstract**: Low-density parity-check (LDPC) codes are one of the most powerful error-correcting codes for wireless communication of high-speed data. This power comes from an efficient decoding scheme, the sum-product algorithm (SPA), which runs over the bipartite graph defining the code. In this work, we propose to use a modified version of the decoding algorithm over the LDPC codes used in Long Term Evolution (LTE) and WiFi and demonstrate that with the same number of iterations, without any increase in time complexity, we can achieve an enhanced error-correcting performance. The only trade off of the system is the necessary storage of the decoding sets, for a total size of ns × n, where ns is the number of decoding sets used and n is the codeword length. In this work, the maximum value of ns used is 5, which makes the trade-off fairly acceptable, considering that the coding gain is obtained virtually free-of-charge.

## Invertible subset LDPC codes for PAPR reduction in OFDM-WLAN systems

- **Status**: ❌
- **Reason**: OFDM-WLAN PAPR 저감용 IS-LDPC — 무선 응용 특이적이며 NAND ECC로 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:7284485
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Si Shu, Daiming Qu, Xuebing Pei
- **PDF**: https://ieeexplore.ieee.org/document/7284485
- **Abstract**: A new type of low density parity-check (LDPC) codes, called as invertible subset LDPC (IS-LDPC) codes, was proposed to reduce the peak-to-average power ratio (PAPR) for orthogonal frequency-division multiplexing (OFDM) systems with low complexity recently. In this paper, we apply IS-LDPC codes to OFDM-wireless local area networks (OFDM-WLAN) systems and design parameters of IS-LDPC codes to satisfy requirements of the IEEE 802.11 OFDM-WLAN system. Moreover, we propose interleaved subset mapping scheme to guarantee the frequency diversity gain. The simulation results show that the IS-LDPC codes for the IEEE 802.11 OFDM-WLAN system exhibit good error-correcting performance and significantly reduce the PAPR. With all mentioned advantages, the PAPR reduction scheme based on IS-LDPC codes could serve as an attractive PAPR reduction solution for the IEEE 802.11 OFDM-WLAN systems.

## Performance analysis of efficient coding schemes for wireless sensor networks

- **Status**: ❌
- **Reason**: WSN ECC 성능비교에서 RS 부호가 최적이라는 결론, LDPC는 부수 언급 — 비-LDPC, 떼어낼 기법 없음
- **ID**: ieee:7173277
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Imad Ez-zazi, Mounir Arioua, Ahmed el Oualkadi +1
- **PDF**: https://ieeexplore.ieee.org/document/7173277
- **Abstract**: Energy consumption in sensor nodes and Link reliability are two of the major challenges in Wireless Sensor Networks (WSNs). The data exchanged between nodes and base station are vulnerable to corruption by errors induced by random noise, signal fading and other factors. In this regard, error control coding (ECC) is an efficient technique used to increase link reliability and to reduce the required transmitted power. In this context, the choice of energy efficient ECC with a suitable modulation scheme is a crucial task at the link and physical layer of wireless sensor networks to improve their lifetime. Since the WSNs are energy constraint in nature, both the probability of bit error rate (BER) and power consumption have to be taken into account. A performance analysis of error control coding schemes referring to BPSK modulation through a Gaussian channel (AWGN) is presented in this paper. Our results show that the RS(31,21) outperforms other ECC schemes and can be the optimal choice for wireless sensor network environment.

## Construction of quasi-cyclic LDPC cycle codes over Galois Field GF(q) based on cycle entropy and application on patterned media storage

- **Status**: ❌
- **Reason**: GF(q) 비이진 QC-LDPC cycle code(패턴드미디어) — 비이진 LDPC는 명시적 제외
- **ID**: ieee:7157325
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: X. Liu, F. Xiong, Y. Yin
- **PDF**: https://ieeexplore.ieee.org/document/7157325
- **Abstract**: Low-density parity-check (LDPC) codes which were proposed in 1962 had been proved to approach the Shannon limit performance. Due to the superior performance, LDPC codes have got wide applications in information transmission and magnetic recording. Meanwhile, good codes usually bear good performance, such as irregular quasi-cyclic LDPC, so it is valuable to study deeply the construction of LDPC codes. In this digest, we focus on the construction of a type of quasi-cyclic LDPC codes, called cycle codes whose parity-check matrix has exactly weight-2 columns. Based on our previous work, the Maximum Cycle Entropy(MCE) Algorithm for constructing nonbinary LDPC codes is then improved and extended to its quasi-cyclic form (QC-MCE), which maintains the quasi-cyclic structure of the parity-check matrix. With this method employed, an elegant distribution of nonzero entries over the Galois Field GF(q) can be obtained among the cycles whose length is related to the girth. Thus, the independence of probabilistic information transferred during decoding is increased, leading to a better performance. Through comparisons and convergence analyses we find that the proposed QC-MCE algorithm behaves much better than the conventional random one and performs as well as the existing method over the AWGN channel. The decoding complexity of our proposed codes is reasonably low due to the QC structure of the codes. The codes constructed with the proposed method can be well applied over the patterned media storage.

## The design of protograph LDPC codes for two-dimensional magnetic recording channels

- **Status**: ✅
- **Reason**: EXIT chart + ensemble weight enumerator로 protograph LDPC 신규 설계(E), 바이너리 코드 설계 이식 가능
- **ID**: ieee:7157698
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: P. Chen, L. Kong, Y. Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/7157698
- **Abstract**: This paper investigates the performance of the protograph based low-density parity-check (LDPC) codes for two dimensional (2D) inter symbol interference (ISI) channels with magnetic recording density . The protograph LDPC codes have been shown to possess excellent error performance over AWGN channel and over partial response channel. Moreover, the protograph structure that realizes linear encoding and decoding allows high-speed encoding and decoding implementations. We further proposes a protograph LDPC code for 2D ISI channel with the help of extrinsic information transfer (EXIT) chart fitting and asymptotic ensemble weight enumerators. Analysis and simulation results show that the proposed code has performance gain both in low- and high-SNR regions over previously optimized irregular LDPC codes for 2D ISI channels.

## Protograph based quasi-cyclic LDPC coding for ultra-high density magnetic recording channels

- **Status**: ✅
- **Reason**: protograph 기반 QC-LDPC 신규 코드 설계(E). 자기기록용이나 바이너리 QC-LDPC 구성 기법 이식 가능
- **ID**: ieee:7157697
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: L. Kong, L. He, P. Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/7157697
- **Abstract**: Bit-patterned media recording (BPMR), heat (or microwave) assisted magnetic recording (HAMR) and shingled writing (SW)/two-dimensional magnetic recording (TDMR) have been primed to further increase the areal density of magnetic recording beyond 1Tb/in2. However, with the reduction of the track pitch, inter-track interference (ITI) becomes a major impairment for these magnetic recording systems. ITI combined with the conventional (down-track) inter-symbol interference (ISI) forms a two-dimensional (2D) interference that severely degrades the performance of data detection in these systems.

## Performance evaluation of LDPC coding and iterative decoding system in TDMR R/W channel with head skew

- **Status**: ❌
- **Reason**: TDMR HDD 채널 BER 평가, 2D-FIR 등화기 + LDPC 부수 적용. 떼어낼 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:7157692
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: R. Suzutou, Y. Nakamura, H. Osawa +3
- **PDF**: https://ieeexplore.ieee.org/document/7157692
- **Abstract**: Two-dimensional magnetic recording (TDMR) by shingled magnetic recording (SMR) draws attention as a next generation technology to increase recording densities in hard disk drive (HDD) [1]. TDMR exploits two-dimensional signal processing using the waveforms reproduced by array head from the intended and adjacent tracks to mitigate the impact of intertrack interference (ITI) [2]. However array head has the issue on the degradation of bit error rate (BER) performance due to head skew [3], [4]. In this study, we evaluate the BER performance of TDMR R/W channel with head skew under the specification of 4 Tbit/inch2 employing low-density parity check (LDPC) coding and iterative decoding system using a two-dimensional finite impulse response (TD-FIR) filter by computer simulation.

## Soft-output decoding of 2D modulation codes for bit-patterned media recording

- **Status**: ❌
- **Reason**: BPMR용 2D 변조코드 LLR 구현이 핵심, LDPC는 베이스라인. 떼어낼 LDPC ECC 신규 기법 없음
- **ID**: ieee:7157703
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: C. Warisarn, P. Kovintavewat
- **PDF**: https://ieeexplore.ieee.org/document/7157703
- **Abstract**: The two-dimensional (2D) interference is a major impairment in bit-patterned media recording (BPMR) systems because of small bit and track pitches, especially at high recording densities. To mitigate this problem, we introduced 2D modulation codes, which output only the hard decision, for an uncoded BPMR system (i .e ., without error-correction codes). To utilize a rate-4/5 constructive inter-track interference (CITI) code in the coded BPMR system, which employs a low-density parity-check (LDPC) code, we propose the log-likelihood ratio (LLR) algebra implementation in Boolean logic mappings for the CITI coding scheme. Then, this soft CITI coding scheme together with a modified 2D soft-output Viterbi algorithm (2D-SOVA) detector [4] and a LDPC decoder will jointly perform iterative decoding.

## A soft decodable concatenated LDPC code

- **Status**: ✅
- **Reason**: SSD/HDD용 LDPC, error floor<1e-12, 큰 블록 코드워드, soft decodable concatenated LDPC 신규 설계(A/B/E)
- **ID**: ieee:7157702
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: S. Yang, Y. Han, X. Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/7157702
- **Abstract**: Low density parity check (LDPC) codes with iterative soft decoding have been adopted as the primary error correction coding technology in data storage devices, e.g., hard disk drives (HDDs) and solid state drives (SSDs). Data storage normally has stringent requirements for low probability of decoding failure since there is no re-transmission mechanism as available for most other data communication applications. Typically the error floor of a LDPC decoder in a storage application should be below 10-12. Recently, the adoption of 4 kB sector formats has allowed LDPC code word size to increase from 4096 user bits to 32768 user bits. This increase in code word size has enabled significantly more error correction power and better noise tolerance margin. Further increases in LDPC code block size beyond 4KB are expected to deliver further SNR gain but would be very expensive in terms of silicon area and power consumption.

## Joint low-complexity detection and reliability-based BP decoding for non-binary LDPC coded TDMR channels

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) LDPC 디코딩 대상이라 바이너리 한정 기준에 따라 제외
- **ID**: ieee:7157693
- **Type**: conference
- **Published**: 11-15 May 
- **Authors**: G. Han, M. Wang, Y. Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/7157693
- **Abstract**: Bit Patterned media recording (BPMR), heat assisted magnetic recording (HAMR), and shingled writing (SMR) with 2-dimensional (2-D) readback have been explored to further scale magnetic recording areal density over the next decade. However, from a signal processing perspective, all these magnetic recording technologies face a common challenge that is how to efficiently recover recorded data from the readback signals corrupted by inter-symbol interference and inter-track interference. The extension of Viterbi algorithm and BCJR algorithm to the 2D ISI channel has prohibitive complexity for the typical 2-D data size. In [1], the authors proposed an IRCSDFA-GA-BCJR detection algorithm which has an enormous complexity reduction compared with the conventional IRCSDFA and the optimal BCJR. In this paper, an efficient iterative detection and decoding scheme is proposed for Non-binary LDPC (NB-LDPC) codes coded two dimensional magnetic recording (TDMR) channels, in which both the low-complexity IRCSDFA-GA-BCJR detection and the fast convergence BP decoding are employed to improve the performance of 2-D channel detection.

## Algebraic Constructions of Quasi-Cyclic LDPC Codes Based on Prime Fields

- **Status**: ✅
- **Reason**: 소수체 기반 QC-LDPC 신규 대수적 구성(E), 빠른 수렴. 바이너리 QC-LDPC 설계 이식 가능
- **ID**: ieee:7145673
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Rui Zhang, Guixia Kang, Ningbo Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7145673
- **Abstract**: On dispersing different base matrices combined with masking, different kinds of quasi-cyclic low-density parity check (QC-LDPC) codes are constructed, which may achieve good error performances. Two new algebraic constructions of regular QC-LDPC codes are presented in this paper. The two constructions are based on two base matrices by dispersing and masking. The two base matrices are based on the generators of the cyclic group of a prime field. Results show that the two classes of codes presented in this paper perform well with iterative decoding over AWGN channel and have advantages over MacKay codes in some aspects of code performances. We find that one of the constructed codes converges very fast with iterative decoding, which is a critical property in ultra-high throughput communication systems.

## Novel Extending Scheme for the Construction of Rate-Compatible IRA-Like Codes

- **Status**: ✅
- **Reason**: 새 확장 알고리즘으로 rate-compatible IRA-like LDPC 구성(균일 체크노드 분포, 선형 인코딩) — 바이너리 LDPC 코드 설계 신규 기여(E)
- **ID**: ieee:7145956
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Wenwen Li, Jing Lei, Er-bao Li +1
- **PDF**: https://ieeexplore.ieee.org/document/7145956
- **Abstract**: In this paper, a novel extending algorithm is proposed for the construction of rate compatible (RC) irregular repeat accumulate like (IRA-like) codes. Based on the structure characters of IRA-like codes, we propose an extending algorithm with uniform check node degree distribution and strong dependency in parity check matrix. Lower rate codes constructed through this method are efficiently encodable and well performed. Starting from initial code rate 8/16, the designed extending algorithm combining with existing puncturing algorithm realizes a series of RC IRA-like codes with rate R = 8/24, 8/23... 8/9. Simulation results show that the constructed RC IRA-like codes outperform those of similar algorithms from 0.04dB to 0.4 dB.

## Clustered Multiuser Detection Using SC-FDE Transmission with Iterative Receivers

- **Status**: ❌
- **Reason**: SC-FDE 다중사용자 검출(IB-DFE)이 핵심, LDPC는 부수 언급. 떼어낼 LDPC 기법 없음
- **ID**: ieee:7145747
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Joao Gante, Marco Gomes, Rui Dinis +1
- **PDF**: https://ieeexplore.ieee.org/document/7145747
- **Abstract**: Iterative block decision feedback equalization (IB-DFE) algorithms are proven to be powerful tools when detecting several uplink signals sharing the same physical channel. However, those algorithms may face some constraints -- the IB-DFE has some difficulty picking certain signals up if they are considerably weaker than the rest and the computational effort grows exponentially with the number of signals to be detected. In this paper we present a clustered multiuser detection scheme, based on an IB-DFE algorithm. It is demonstrated that if the mobile terminals (MTs) have enough power and are distributed in clusters, with considerable power difference between them, it is possible to successfully detect them all while containing the computational complexity. Our scheme also requires fewer receiving antennas than the original IB-DFE implementations and, with the aid of low-density parity- check (LDPC) and turbo- equalization, it is able to reach high performance levels with low power requirements.

## Iterative Frequency-Domain Equalization for General QAM Constellations with Reduced Envelope Fluctuations through Magnitude Modulation Techniques

- **Status**: ❌
- **Reason**: QAM + magnitude modulation + IB-DFE 무선통신 특이적, LDPC는 BICM 베이스라인. 이식 기법 없음
- **ID**: ieee:7145894
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Marco Gomes, Rui Dinis, Vitor Silva +2
- **PDF**: https://ieeexplore.ieee.org/document/7145894
- **Abstract**: The development of new mobile communications systems faces several important challenges, namely demanding for high bit rates, high spectral efficiency, low energy consumption and the usage of hostile channels. In order to fulfill these requirements for block-based single carrier transmissions, we propose to use high order QAM constellations combined with envelope control Magnitude Modulation (MM) techniques and bit-interleaved coded modulation with LDPC codes. Also, the receiver uses powerful MM specialized IB-DFE solutions to combat the channel distortion and noise. The obtained results have shown significant improvements in terms of energy efficiency and bit error rate.

## Is MAC Joint Decoding Optimal for Interference Channels?

- **Status**: ❌
- **Reason**: 간섭채널 MAC 결합디코딩 정보이론 분석, LDPC 부수. 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:7145891
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Guangxia Zhou, Wen Xu, Gerhard Bauch
- **PDF**: https://ieeexplore.ieee.org/document/7145891
- **Abstract**: Harsh interference is a major obstacle to achieve high capacity, especially when the state-of-the-art wireless networks intend to reuse the same resource. Information theoretic study shows that joint decoding with interference can achieve the sum capacity of a strong interference channel. However, the optimal joint decoding technique is too complex for practical applications, because it requires detecting and decoding all messages simultaneously. A two-user strong interference channel can be formed by two two- user multiple access channels (MACs), so a natural question arises as whether the decoding schemes optimal for the MAC remains optimal when applied to the interference channel. This paper investigates the relevant decoding techniques, namely the MAC rate splitting (RS) and iterative detection-decoding. Although these techniques have been shown to be optimal for MACs, we show that they cannot achieve the optimal performance anymore under interference channels.

## Pseudo Block Coded Single-Carrier Transmission Using Frequency-Domain Block Signal Detection

- **Status**: ❌
- **Reason**: single-carrier 주파수영역 등화/블록신호검출 통신 응용, BP는 검출기로 부수 언급 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7146035
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Hiroyuki Miyazaki, Fumiyuki Adachi
- **PDF**: https://ieeexplore.ieee.org/document/7146035
- **Abstract**: Recently, we proposed a pseudo block coded single-carrier (PBC-SC) transmission using minimum mean square error (MMSE) based frequency-domain equalization and decoding (FDED) and show that MMSE based FDED achieves BER performance superior to 2-step decoding (which performs frequency-domain equalization and hard decision decoding separately). However, there still exists a large BER performance gap between MMSE based FDED and MF bound due to the presence of residual inter-symbol interference (ISI) after MMSE based FDED. In this paper, in order to narrow the performance gap, we propose frequency-domain block signal detection (FDBD) aided FDEDs for PBC-SC transmission: frequency-domain iterative interference cancellation (FDIC), maximum likelihood block sig-nal detection employing QR decomposition and M algorithm (QRM-MLBD) and belief propagation (BP). We compare, by computer simulation, the BER performances and the computa-tional complexities of three FDBD aided FDED schemes. It is shown that QRM-MLBD and BP can achieve almost the same BER performance as MF bound with much lower computational complexity than MMSE based FDED.

## Phase noise-robust LLR calculation with linear/bilinear transform for LDPC-coded coherent communications

- **Status**: ✅
- **Reason**: 위상잡음에 강건한 LDPC 디코더 LLR 계산(선형/이중선형 변환) — LLR 계산 기법은 NAND 채널 LLR 산출에 이식 가능(C)
- **ID**: ieee:7184331
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Keisuke Kojima +1
- **PDF**: https://ieeexplore.ieee.org/document/7184331
- **Abstract**: We propose a modified log-likelihood ratio (LLR) calculation for an LDPC decoder to be robust against residual phase noise at the demodulator. The proposed scheme is based on a linear/bilinear transform offers 1 ~ 2dB gain in the presence of large phase noise.

## LDPC-coded 16-dimensional modulation based on the Nordstrom-Robinson nonlinear block code

- **Status**: ❌
- **Reason**: Nordstrom-Robinson 비선형 블록코드 기반 16차원 변조에 LDPC를 EXIT chart로 최적화 — 변조 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7183463
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Toshiaki Koike-Akino, David S. Millar, Keisuke Kojima +4
- **PDF**: https://ieeexplore.ieee.org/document/7183463
- **Abstract**: We propose a new high-dimensional modulation (HDM) format, based on the Nordstrom-Robinson code, which is the best-known nonlinear block code in 16 dimensions. With EXIT chart, we optimize LDPC codes for various HDM formats, and show their benefits.

## FPGA-based non-binary QC-LDPC coding for high-speed coherent optical transmission

- **Status**: ❌
- **Reason**: non-binary QC-LDPC 코드 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7184332
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: Ding Zou, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7184332
- **Abstract**: We present a large-girth-non-binary QC-LDPC code suitable for beyond 100 Gb/s optical transmission and describe its implementation in FPGA. Great performance with Q-limit of 5.0 dB at BER of 10-10 has been found, which corresponds to NCG of 11.95 dB at 10-15.

## Multi-gigabit coherent communications using low-rate FEC to approach the Shannon capacity limit

- **Status**: ❌
- **Reason**: rate-1/4 FEC+coherent 수신기 광통신, 부호 구체 기여 없음 — 통신 응용, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7184330
- **Type**: conference
- **Published**: 10-15 May 
- **Authors**: David J. Geisler, Venkat Chandar, Timothy M. Yarnall +2
- **PDF**: https://ieeexplore.ieee.org/document/7184330
- **Abstract**: Combining a rate-¼ forward error-correcting code, a coherent receiver, and an optical phase-locked loop yields near error-free performance with 2-dB photon-per-bit sensitivity, which is <;3-dB from the Shannon limit for a rate-¼, pre-amplified, coherent receiver.
