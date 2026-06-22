# IEEE Xplore — 2018-06


## LP/SDP Hierarchy Lower Bounds for Decoding Random LDPC Codes

- **Status**: ❌
- **Reason**: random LDPC의 LP/SDP 디코딩 한계 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7872442
- **Type**: journal
- **Published**: June 2018
- **Authors**: Badih Ghazi, Euiwoong Lee
- **PDF**: https://ieeexplore.ieee.org/document/7872442
- **Abstract**: Random (dν, dc)-regular low-density paritycheck (LDPC) codes, where each variable is involved in du parity checks and each parity check involves dc variables are well-known to achieve the Shannon capacity of the binary symmetric channel, for sufficiently large dν and dc, under exponential time decoding. However, polynomial time algorithms are only known to correct a much smaller fraction of errors. One of the most powerful polynomial-time algorithms with a formal analysis is the linear programming (LP) decoding algorithm of Feldman et al., which is known to correct an Ω(1/dc) fraction of errors. In this paper, we show that fairly powerful extensions of LP decoding, based on the Sherali-Adams and Lasserre hierarchies, fail to correct much more errors than the basic LP-decoder. In particular, we show that: 1) for any values of dν and dc, a linear number of rounds of the Sherali-Adams LP hierarchy cannot correct more than an O(1/dc) fraction of errors on a random (dν, dc)-regular LDPC code; and 2) for any value of du and infinitely many values of dc, a linear number of rounds of the Lasserre SDP hierarchy cannot correct more than an O(1/dc) fraction of errors on a random (dν, dc)-regular LDPC code. Our proofs use a new stretching and collapsing technique that allows us to leverage recent progress in the study of the limitations of LP/SDP hierarchies for Maximum Constraint Satisfaction Problems (Max-CSPs). The problem then reduces to the construction of special balanced pairwise independent distributions for Sherali-Adams and special cosets of balanced pairwise independent subgroups for Lasserre. Our (algebraic) construction for the Lasserre hierarchy is based on designing sets of points in Fqd (for q any power of 2 and d = 2, 3) with special hyperplane-incidence properties-constructions that may be of independent interest. An intriguing consequence of our work is that expansion seems to be both the strength and the weakness of random regular LDPC codes. Some of our techniques are more generally applicable to a large class of Boolean CSPs called Min-Ones. In particular, for k-Hypergraph Vertex Cover, we obtain an improved integrality gap of k -1- ε that holds after a linear number of rounds of the Lasserre hierarchy, for any k = q + 1 with q an arbitrary prime power. The best previous gap for a linear number of rounds was equal to 2 - ε and due to Schoenebeck.

## Two-Layer LDPC Codes for Low Complexity ML Detection in GSM Systems

- **Status**: ❌
- **Reason**: GSM ML detection 복잡도 절감용 two-layer LDPC, 무선 검출 응용 특이적이며 떼어낼 디코더/구성 기여 없음
- **ID**: ieee:8166736
- **Type**: journal
- **Published**: June 2018
- **Authors**: Xue-Qin Jiang, Yanyan Zheng, Wen Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/8166736
- **Abstract**: Although maximum-likelihood (ML) detection is able to achieve optimal performance in generalized spatial modulation (GSM) systems, its exhaustive search leads to an intractable computational complexity. In this letter, two-layer low-density parity-check (TL-LDPC) codes are proposed to reduce the combinations of transmission vectors in LDPC coded GSM systems. Simulation results show that the complexity of the ML detection in the TL-LDPC-coded GSM systems is much lower than that of the ML detection in conventional LDPC-coded GSM systems with a negligible performance loss.

## Nonbinary LDPC-Coded Spatial Multiplexing for Rate-2 MIMO of DVB-NGH System

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC를 제안하는 논문 - 비이진 LDPC는 명시적 제외 대상
- **ID**: ieee:8237200
- **Type**: journal
- **Published**: June 2018
- **Authors**: Zhanji Wu, Xiang Gao, Chengxin Jiang
- **PDF**: https://ieeexplore.ieee.org/document/8237200
- **Abstract**: To improve the performance on high spatial correlation channels, the enhanced spatial multiplexing (eSM) precoding scheme with the binary low density parity check (LDPC) codes is employed for the rate-2 MIMO transmission in the DVB-NGH standard. However, it just brings very limited performance gain about 0.2-0.4 dB compared with the plain spatial multiplexing scheme in high correlation channels, while it has not any gain in low correlation channels. In this paper, a nonbinary (NB) LDPC coded modulation (CM) eSM scheme is proposed. The binary DVB-NGH LDPC codes are replaced by regular quasi-cyclic NB LDPC codes, and each NB-LDPC coded symbol is directly mapped to two modulation symbols on two transmit antennas. To investigate the performance gain, average mutual information performances of bit-interleaved-coded-modulation (BICM) and CM MIMO systems are analyzed in flat Rayleigh fading channels, which are corresponding to the binary and NB coding scheme, respectively. The information-theoretic analysis turns out that the proposed NB-LDPC CM-MIMO scheme is much superior to the current binary-LDPC BICM-eSM scheme. Simulation results also verify that the proposed scheme has significant up to 3dB performance gain compared with the BICM-eSM scheme under different modulation orders, power imbalances, and channel correlations. Therefore, the proposed scheme is much more reliable and robust, and thus very suitable for the future broadcasting applications.

## An Improved Belief Propagation Decoding of Concatenated Polar Codes With Bit Mapping

- **Status**: ❌
- **Reason**: polar+LDPC concatenation의 bit mapping이 polar 편극에 의존, NAND LDPC BP로 이식 불가
- **ID**: ieee:8344119
- **Type**: journal
- **Published**: June 2018
- **Authors**: Qing-Ping Yu, Zhi-Ping Shi, Li Deng +1
- **PDF**: https://ieeexplore.ieee.org/document/8344119
- **Abstract**: Bit-channels of finite-length polar codes are not fully polarized, and the negative influences from semi-polarized channels are not negligible. In this letter, we consider the concatenated system of an inner polar code and an outer low-density parity-check (LDPC) code to improve the error correction performance of finite-length polar code with belief propagation (BP) decoding. We propose a bit mapping method between LDPC coded bits and polarized channels, aiming to match the coding protection of LDPC codes with polarization of polar codes. Simulation results show that, the concatenated polar codes with bit mapping outperform the pure polar codes with BP decoding and concatenated polar codes with traditional consecutive bit mapping.

## Multilevel Coded Modulation for the Full-Duplex Relay Channel

- **Status**: ❌
- **Reason**: 릴레이 채널용 multilevel coding 프레임워크로 LDPC는 시뮬레이션 베이스라인, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8274994
- **Type**: journal
- **Published**: June 2018
- **Authors**: Ahmed Attia Abotabl, Aria Nosratinia
- **PDF**: https://ieeexplore.ieee.org/document/8274994
- **Abstract**: We investigate coded modulation for full-duplex relay channels, proposing and analyzing a multilevel coding (MLC) framework with capacity approaching performance and practical features. Sufficient conditions are derived under which multilevel coding meets the known achievable rates for decode-and-forward relaying. The effect of a bit additive superposition and the linearity of multilevel code components on the performance of the system are studied. It is shown that linearity of the relay component codes imposes no penalty on rate, however, the linearity of the source-to-relay component codes may impose a performance penalty especially for small modulation constellations. We show that this rate loss occurs because a linearity constraint on codebooks at the source node introduces a new tension between optimality of rate allocation in multilevel coding layers and optimality of source/relay codebook correlations. Motivated by this insight, an alternative modulation labeling is proposed that minimizes the rate loss. The results are extended to multi-antenna relays. Slow fading and fast Rayleigh fading without channel state at the transmitter are also analyzed. The error exponent of the proposed scheme is studied. Finally, the frame- and bit-error rate performance of the proposed scheme is studied via simulations using point-to-point LDPC codes, showing that the proposed MLC relaying has excellent performance.

## On Capacity-Based Codebook Design and Advanced Decoding for Sparse Code Multiple Access Systems

- **Status**: ❌
- **Reason**: SCMA 코드북+LDPC 수신기, 무선 다중접속 응용 특이적이고 LDPC는 베이스라인, 이식 기법 없음
- **ID**: ieee:8328013
- **Type**: journal
- **Published**: June 2018
- **Authors**: Kexin Xiao, Bin Xia, Zhiyong Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/8328013
- **Abstract**: Sparse code multiple access (SCMA) is a promising non-orthogonal air-interface technology for its ability to support massive connections. In this paper, we design the multiuser codebook and the advanced decoding from the perspective of the theoretical capacity and the system feasibility. First, different from the lattice-based constellation in point-to-point channels, we propose a novel codebook for maximizing the constellation constrained capacity. We optimize a series of 1-D superimposed constellations to construct multi-dimensional codewords. An effective dimensional permutation switching algorithm is proposed to further obtain the capacity gain. Consequently, it shows that the performance of the proposed codebook approaches the Shannon limit and achieves significant gains over the other existing ones. Furthermore, we provide a symbol-based extrinsic information transfer tool to analyze the convergence of SCMA iterative detection, where the complex codewords are considered in modeling the a priori probabilities instead of assuming the binary inputs in previous literature. Finally, to approach the capacity, we develop a low-density parity-check code-based SCMA receiver. Most importantly, by utilizing the EXIT charts, we propose an iterative joint detection and decoding scheme with only partial inner iterations, which exhibits significant performance gain over the traditional one with separate detection and decoding.

## Faulty Successive Cancellation Decoding of Polar Codes for the Binary Erasure Channel

- **Status**: ❌
- **Reason**: polar code의 faulty SC 디코딩 분석, BP 비의존이라 LDPC 이식 기법 없음
- **ID**: ieee:8101495
- **Type**: journal
- **Published**: June 2018
- **Authors**: Alexios Balatsoukas-Stimming, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/8101495
- **Abstract**: In this paper, the faulty successive cancellation decoding of polar codes for the binary erasure channel is studied. To this end, a simple erasure-based fault model is introduced to represent errors in the decoder, and it is shown that, under this model, polarization does not happen, meaning that fully reliable communication is not possible at any rate. Furthermore, a lower bound on the frame error rate of polar codes under faulty successive cancellation decoding is provided, which is then used, along with a well-known upper bound, in order to choose a blocklength that minimizes the erasure probability under faulty decoding. Finally, an unequal error protection scheme that can re-enable asymptotically erasure-free transmission at a small rate loss and by protecting only a constant fraction of the decoder is proposed. The same scheme is also shown to significantly improve the finite-length performance of the faulty successive cancellation decoder by protecting as little as 1.5% of the decoder.

## MIMO Scattered Pilot Performance and Optimization for ATSC 3.0

- **Status**: ❌
- **Reason**: ATSC 3.0 MIMO 파일럿 최적화, LDPC 무관 무선 응용 특이적
- **ID**: ieee:8169682
- **Type**: journal
- **Published**: June 2018
- **Authors**: Takuya Shitomi, Eduardo Garro, Kenichi Murayama +1
- **PDF**: https://ieeexplore.ieee.org/document/8169682
- **Abstract**: ATSC 3.0 is the latest digital terrestrial television (DTT) standard, and it allows a higher spectral efficiency and/or a transmission robustness with multiple-input multiple-output (MIMO) technology compared to existing DTT standards. Regarding MIMO channel estimation, two pilot encoding algorithms known as Walsh-Hadamard encoding and Null Pilot encoding are possible in ATSC 3.0. The two MIMO pilot algorithms are standardized so as to have the same pilot positions and the same pilot boosting as single-input single-output, and the optimum pilot configuration has not been fully evaluated for MIMO. This paper focuses on the performance evaluation and optimization of the pilot boosting and the pilot patterns for two MIMO pilot encoding algorithms in ATSC 3.0 using physical layer simulations. This paper provides a great benefit to broadcasters to select the MIMO pilot configuration including pilot boosting, pilot pattern, and pilot encoding algorithm that better suits their service requirements. Several channel interpolation algorithms have been taken into account as a typical receiver implementation in both fixed SFN reception and mobile reception.

## Pliable Fractional Repetition Codes for Distributed Storage Systems: Design and Analysis

- **Status**: ❌
- **Reason**: Fractional repetition 코드(분산스토리지 regeneration)로 LDPC 아님, NAND LDPC ECC 이식 기법 없음
- **ID**: ieee:8272004
- **Type**: journal
- **Published**: June 2018
- **Authors**: Yi-Sheng Su
- **PDF**: https://ieeexplore.ieee.org/document/8272004
- **Abstract**: A distributed storage system (DSS) is one of the most vital components of a cloud computing system used for storing and sharing big data among authorized users. A typical DSS consists of n storage nodes each with a storage capacity of α units of data such that the entire file stored on the DSS can be recovered by accessing any k <; n nodes. The objective of this paper is to construct fractional repetition (FR) codes with applications in DSSs. FR codes are the key to constructing a class of distributed storage codes with exact repair by transfer (i.e., upon failure, a failed storage node is exactly regenerated through simple downloading). A major drawback of existing FR codes is that they are insufficiently flexible to adapt adequately to system changes in DSSs. To address this problem, this paper introduces a new type of FR codes, called pliable FR codes, in which both the per-node storage α and repetition degree ρ can easily and simultaneously be adjusted. In addition, this paper presents several constructions of pliable FR codes and provides a relatively comprehensive analysis of the constructed pliable FR codes, which reveals the following versatile properties of the codes: 1) the transposed codes of the constructed codes are also pliable FR codes; 2) the constructed codes attain a tight upper bound on the file size with equality at least for 1 ≤ k <; min(3, k' + 1), where k' is the smallest value of k such that kα - (k - 1) > n-1/ ρ-1; 3) the constructed codes also meet a Singleton-like bound on the minimum distance at least for 1 ≤ k <; 3, which demonstrates their optimality; 4) the computational complexity necessary for determining the file size or the minimum distance of the constructed codes can be greatly reduced when it is hard to exactly determine them; and 5) the constructed codes can be used as fractional repetition batch codes to provide load balancing in DSSs, for which the batch size (i.e., the number of symbols that can be read in parallel) can be exactly determined.

## Impact of the NAND Flash Power Supply on Solid State Drives Reliability and Performance

- **Status**: ❌
- **Reason**: NAND 전원공급 신뢰성/성능 연구일 뿐 떼어낼 LDPC 디코더/HW/코드설계 기법 없음
- **ID**: ieee:8326554
- **Type**: journal
- **Published**: June 2018
- **Authors**: Cristian Zambelli, Rino Micheloni, Luca Crippa +2
- **PDF**: https://ieeexplore.ieee.org/document/8326554
- **Abstract**: The NAND flash memory technology is the fundamental building block of storage systems like solid state drives. Their reliability drastically impacts the design choices of the error recovery flows exploited to improve drive's performance, which progressively degrades as the number of bit errors to be corrected increases. Among the many causes producing errors, it is found that the NAND flash power supply plays a non-negligible role. In this paper, we will show how the drive's performance degradation rate measured by the sustainable bandwidth, read latency, and quality of service metrics, heavily depends on the power supply. The results will show that by using a lower power supply in endeavor to reduce the energy consumption of the drive will yield a significant bandwidth (up to 44.4 kIOPS), latency (up to 504 μs), and quality-of-service (up to 1.5 ms) detriment. Counterintuitively, we will show that the overall energy consumption per byte will increase (up to 4.5 times) in specific working conditions of the drive.

## Fast Low-Complexity Triple-Error-Correcting BCH Decoding Architecture

- **Status**: ❌
- **Reason**: BCH triple-error 디코딩 아키텍처, 비-LDPC 부호이고 LUT/Chien search 기법 LDPC 비이식
- **ID**: ieee:8125750
- **Type**: journal
- **Published**: June 2018
- **Authors**: Daesung Kim, Injae Yoo, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/8125750
- **Abstract**: An efficient decoding architecture for triple-error-correcting BCH codes is proposed by utilizing a lookup table (LUT) that stores the roots of the error locator polynomial instead of using the Chien search. Two roots of the polynomial equation are precomputed and stored in the LUT in order to relax the hardware complexity. To relax the complexity further, a new method to compress the LUT is additionally proposed. While a large portion of the LUT is filled with unnecessary information in the previous designs, this brief eliminates the redundant information by investigating an algebraic property of the equation. For BCH codes over GF(210), the LUT size is reduced to 18% of the previous work. As a result, the proposed decoding architecture reduces the decoding latency by 38% and the equivalent gate count by up to 40% compared to the previous work, achieving a fast low-complexity triple-error-correcting BCH decoder.

## Decision Region Optimization and Metric-Based Compensation of Memoryless Nonlinearity for APSK Systems

- **Status**: ❌
- **Reason**: APSK 비선형 보상/decision region 최적화로 LDPC는 부수적, 떼어낼 부호 비의존 디코더 기법 없음
- **ID**: ieee:8245813
- **Type**: journal
- **Published**: June 2018
- **Authors**: Daiki Yoda, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/8245813
- **Abstract**: We investigate the effect of memoryless nonlinearity on the error rate performance of both uncoded and coded single-carrier amplitude phase-shift keying systems adopted in the satellite communications standards. For the uncoded system, we develop decision regions that lead to optimal error rate performance as well as suboptimal approaches with less computational complexity. For the coded system, we introduce new metrics that are matched to the statistical characteristics of nonlinear distortion, primarily focusing on the Gaussian approximation of distortion components for reduced computational complexity. The effectiveness of our proposed approaches is demonstrated by numerical results in terms of the generalized mutual information as well as error rate performance.

## A Unitary Precoder for Optimizing Spectrum and PAPR Characteristic of OFDMA Signal

- **Status**: ❌
- **Reason**: OFDMA precoder PAPR/스펙트럼 최적화, LDPC 무관 무선 응용 특이적
- **ID**: ieee:8004470
- **Type**: journal
- **Published**: June 2018
- **Authors**: Renhui Xu, Lei Wang, Zhe Geng +3
- **PDF**: https://ieeexplore.ieee.org/document/8004470
- **Abstract**: In this paper, a unitary precoder is proposed to suppress the out-of-subband (OOSB) spectral leakage and reduce the peak-to-average-power-ratio (PAPR) for DFT-based orthogonal frequency division multiple access uplink signal. The optimum precoder is developed by solving a multi-objective optimization problem and a method which includes two steps is presented. First, employ eigenvalue decomposition to design the precoder with minimizing OOSB power radiation. Then search for the optimum permutation of columns to reduce the PAPR sufficiently. Besides, an iterative decoding algorithm for the proposed precoder is designed to improve the system performance on bit-error-rate (BER). Simulations show that the proposed precoding and decoding method offers significant performance advantages of spectral leakage suppression, PAPR reduction, and BER improvement at the same time.

## Successive Interference Cancellation for LDPC Coded Nonorthogonal Multiple Access Systems

- **Status**: ❌
- **Reason**: LDPC-NOMA SIC 수신기, 무선 다중접속 특이적이고 LDPC는 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:8352727
- **Type**: journal
- **Published**: June 2018
- **Authors**: Lei Yuan, Jie Pan, Nan Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/8352727
- **Abstract**: We design, for the first time, novel successive interference cancellation (SIC) schemes for a two-user nonorthogonal multiple access system using low-density parity-check codes. We first develop a low-complexity SIC scheme treating interference as noise, referred to as the N-SIC scheme, and a SIC with joint detection scheme treating the modulation of interference signal at the near user as side information, referred to as the J-SIC scheme. We then propose a new extrinsic information assisted SIC scheme, referred to as the E-SIC scheme, which exchanges the extrinsic decoding information of the signals for two users and thus incurs an increase complexity. With simulations, we demonstrate that the error performance advantage of the E-SIC scheme over the N-SIC and J-SIC schemes is more significant when the power allocated to the near user is larger, e.g., higher than 45%. When this power becomes smaller, e.g., less than 10%, the low-complexity N-SIC scheme can achieve the best error performance. In addition, we have an important finding that when the two users adopt different order modulation, the decoding convergence speed of the E-SIC scheme improves when the difference between the constellation sizes of two users is larger.

## Noncoherent LDPC-Coded Physical-Layer Network Coding Using Multitone FSK

- **Status**: ❌
- **Reason**: FSK PNC용 LDPC 코드 최적화로 채널 특이적, 표준 LDPC 최적화 수준 - 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:8281062
- **Type**: journal
- **Published**: June 2018
- **Authors**: Terry Ferrett, Matthew C. Valenti
- **PDF**: https://ieeexplore.ieee.org/document/8281062
- **Abstract**: A noncoherent two-way relaying system is developed using physical-layer network coding for improved throughput over conventional relaying in a fading channel. Energy-efficient noncoherent operation is achieved using multitone frequency shift keying (FSK). A novel soft-output demodulator is developed for the relay, and corresponding achievable exchange rates are found for Rayleigh fading and AWGN channels. Bit-error rate performance approaching the achievable rate is realized using a capacity-approaching channel code and a receiver architecture, which iterates between demodulation and channel decoding. Iterative decoding is performed feeding information back from the channel decoder to the demodulator. In addition, the error-rate performance is made to approach the achievable rate more closely by optimizing LDPC codes for this system. The energy efficiency improvement obtained by increasing the modulation order is more dramatic for the proposed physical-layer network coding scheme than it is for a conventional point-to-point system. Using optimized LDPC codes, the bit-error rate performance is improved by as much as 1.1 dB over a widely known standardized LDPC code, and comes to within 0.7 dB of the limit corresponding to the achievable rate. Throughout this paper, the performance for physical-layer network coding is compared with conventional network coding. When noncoherent FSK is used, physical-layer network coding enables higher achievable rates, and conventional network coding exhibits better energy efficiency at low rates.

## Systematic Physical-Layer Raptor Coding to Attain Low Decoding Complexity

- **Status**: ❌
- **Reason**: raptor(fountain) 부호 구성, 비-LDPC이며 이식할 BP 기법 없음
- **ID**: ieee:8344108
- **Type**: journal
- **Published**: June 2018
- **Authors**: Guan-Ting Li, Hsuan-Kuan Wu, Huang-Chang Lee +2
- **PDF**: https://ieeexplore.ieee.org/document/8344108
- **Abstract**: We study physical-layer raptor (PLR) coding for message blocks of moderate lengths to achieve low decoding complexity with only a slight degradation in throughput. Approaches include systematic PLR code construction, convergence analysis, and an early termination strategy that is only appropriate for the systematic PLR code.

## A Study on LDM-BST-OFDM Using Punctured LDPC Code in Partial Reception Band

- **Status**: ❌
- **Reason**: LDM-BST-OFDM 전송심볼 puncturing 응용; LDPC 코드 구성 신규 기법 아님
- **ID**: ieee:8436825
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Hiroto Yamamoto, Akira Nakamura, Makoto Itami
- **PDF**: https://ieeexplore.ieee.org/document/8436825
- **Abstract**: The scheme that combines LDM(Layered Division Multiplexing) to the FDM(Frequency Division Multiplexing) scheme based BST-OFDM(Band Segmented Transmission - Orthogonal Frequency Division Multiplexing) in Japan is proposed for the next DTTB(Digital Terrestrial Television Broadcasting). In this paper, the transmission symbols for the stationary reception are generated by puncturing the symbols after BICM(Bit-Interleaved Coded Modulation) and removed symbols by puncturing are multiplexed to the transmitted symbols for mobile reception by LDM. The performances of the proposed scheme are evaluated by computer simulations under the multipath environment, and the improvement of the required CNR(Carrier to Noise Ratio) in stationary reception was confirmed.

## Novel Interleave-Division Multiple Access Scheme Based on QC-LDPC Codes for Terrestrial Broadcasting Return Channel

- **Status**: ❌
- **Reason**: IDMA에 표준 QC-LDPC 대입; 새 코드·디코더 설계 없음(응용 특이)
- **ID**: ieee:8436671
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Xuan Huang, Kewu Peng, Jian Song
- **PDF**: https://ieeexplore.ieee.org/document/8436671
- **Abstract**: In this paper, to further approach the maximum transmission rate of terrestrial broadcasting return channel, interleave division multiple access (IDMA) is utilized for terrestrial broadcasting return channel rather than conventional orthogonal frequency division multiple access (OFDMA). Extrinsic information transfer (EXIT) chart is employed to analyze the loss of maximum transmission rate for the conventional IDMA scheme. Due to the advantages of quasi-cyclic low density parity check (QC-LDPC) codes, such as the large degree of freedom and the convenience to extent into multiple code rates, the adopted convolutional codes (CCs) in the conventional IDMA scheme are replaced by QC-LDPC codes. The simulation results show when the code rate is 1/2 and QPSK is adopted, the signal to noise ratio (SNR) thresholds of CC and QC-LDPC code are 1.7 dB, and 0.85 dB away from the theoretical Shannon limit, respectively. Thus, the proposed IDMA scheme based on QC-LDPC codes has the maximum transmission rate approaching capability for terrestrial broadcasting return channel.

## Implementation of an ISDB-TBLDM Broadcast System Using the BICM Stage of ATSC 3.0 on Enhanced Layer and Diversity at Reception

- **Status**: ❌
- **Reason**: ISDB-TB 방송; 표준 LDPC+BCH BICM 재사용, 새 기여 없음
- **ID**: ieee:8436637
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Ricardo Seriacopi Rabaca, George Henrique Maranhao garcia de oliveira, Guilherme Rossi Ganzaroli +2
- **PDF**: https://ieeexplore.ieee.org/document/8436637
- **Abstract**: This paper presents performance results of commercial ISDB-TB receivers with the ISDB-TB LDM in Core Layer. The Core Layer is fully compatible with ISDB-TB and is multiplexed with the Enhanced Layer. Simulation results of the Enhanced Layer using a powerful channel coder with modulation up to 256-QNUC and Non-Uniform Constellation are presented. The ISDB-TB LDM can improve the spectral efficiency and useful bit rate so that it becomes possible to use it in the transition for UHDTV applications. The Enhanced Layer uses the same BICM of ATSC 3.0, with LDPC encoder concatenated with the BCH. The implementation was done using the GNU Radio Companion software and Software Defined Radio. The Maximal Ratio Combining technique was proposed to increase the robustness of the system. This solution is an alternative way to introduce a new digital terrestrial broadcasting system using the same channel and infrastructure.

## ATSC 3.0 Physical Layer Modulation and Coding Performance Analysis

- **Status**: ❌
- **Reason**: ATSC 3.0 PHY 성능 분석; 표준 LDPC 사용, 새 기여 없음
- **ID**: ieee:8436876
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Sung-Ik Park, Jae-Young Lee, Sunhyoung Kwon +12
- **PDF**: https://ieeexplore.ieee.org/document/8436876
- **Abstract**: This paper presents ATSC 3.0 physical (PHY) layer modulation and coding performance through computer simulations, laboratory tests, and field trials. Analysis results show that the measured results in laboratory and field are generally well aligned with computer simulation results. The ATSC 3.0 PHY layer performance covers ultra-robust reception (negative SNR operation with QPSK and 2/15 LDPC code) to very high-throughput (over 50 Mbps with 4096-NUC with 13/15 LDPC code) in real field environment.

## Simplified Two-Dimensional Non-Uniform Constellation Demapping Algorithm for ATSC3.0

- **Status**: ❌
- **Reason**: 2D-NUC demapping 알고리즘. 변조/디매핑이라 LDPC ECC 기법 아님.
- **ID**: ieee:8436907
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Hanjiang Hong, Yin Xu, Dazhi He +2
- **PDF**: https://ieeexplore.ieee.org/document/8436907
- **Abstract**: Non-uniform constellations (NUCs) have been adopted in digital broadcasting systems to reduce the shapping gap to the Shannon theoretical limit. Among NUCs, two-dimensional NUCs (2D-NUCs) provide better performance than one-dimensional NUCs (1D-NUCs), but bring higher complexity at the receiver. This paper proposes a simplified demapping algorithm for 2D-NUCs from ATSC3.0 (Advanced Television Systems Committee 3rd Generation), for low to medium code rates. Theoretical analysis and simulation results prove that the complexity of the proposed simplified demapper is reduced while the performance degradation is negligible, compared with the traditional demapper.

## Using Layered-Division-Multiplexing for In-Band Backhaul for ATSC 3.0 SFN and Gapfillers

- **Status**: ❌
- **Reason**: ATSC3.0 SFN 백홀(LDM) 방송 시스템 응용. LDPC 없음, 떼어낼 ECC 기법 없음.
- **ID**: ieee:8436885
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Liang Zhang, Yiyan Wu, Wei Li +9
- **PDF**: https://ieeexplore.ieee.org/document/8436885
- **Abstract**: Due to the rapid increase on the use of mobile devices, delivering mobile broadcasting services (TV/data) is one of the top-priority capabilities for future digital TV (DTV) systems, such as the ATSC 3.0. To improve the mobile service coverage performance for highly populated indoor and closed areas (airports, shopping malls, stadiums, etc.), it becomes necessary to deploy single-frequency-network (SFN) type low-power gapfillters, which could be very costly due to the required backhaul links. This paper proposes a novel technology to use Layered Division Multiplexing (LDM) to implement in-band backhaul to multiple SFN gapfillers. By embedding the backhaul data of the mobile services in the LDM signal structure, a low-cost SFN relay station can be implemented as the gapfiller using conventional ATSC 3.0 receivers. Since the backhaul data is delivered using the same band as the mobile service signal, the proposed technology also achieves high spectrum efficiency. Furthermore, the proposed technology can be used to implement efficient backhaul solutions in the next generation mobile broadband systems (5G and beyond).

## Performance Evaluation of ATSC 3.0 MIMO Precoding

- **Status**: ❌
- **Reason**: ATSC3.0 MIMO precoding 성능평가. ECC/디코더 기법 없음.
- **ID**: ieee:8436897
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Takuya Shitomi, Carlos Barjau, Kenichi Murayama +1
- **PDF**: https://ieeexplore.ieee.org/document/8436897
- **Abstract**: ATSC 3.0, the latest Digital Terrestrial Television (DTT) standard, allows a higher spectral efficiency and/or a transmission robustness with Multiple-Input Multiple-Output (MIMO) technology compared to existing single-antenna DTT networks. Regarding MIMO precoding, three precoding blocks known as Steam Combining (SC), IQ Polarization Interleaving (IQPI) and Phase Hopping (PH) are possible in ATSC 3.0. The three MIMO precoding blocks are standardized as optional, but the performance has not been evaluated. This paper focuses on the performance evaluation of the three MIMO precoding algorithms in ATSC 3.0 using physical layer simulations. Potential gains in required signal to noise ratio (SNR) for several modulation and coding combinations have been evaluated in a fundamental cross-polarized 2x2 MIMO transmission model and MIMO channel snapshots actually captured in an urban area. The fundamental simulation results showed that IQPI and PH provide some gains in a power imbalanced channel and in a small cross polarization discrimination case, respectively. The study based on the practical MIMO channel snapshots concluded that SC potentially provide some gains especially with QPSK and high code rate, but IQPI and PH are less likely to beneficial in an actual static reception scenario.

## Performance Evaluation of ATSC 3.0 Mobile Service with LDM/TDM Under TU-6 Channel

- **Status**: ❌
- **Reason**: LDM/TDM 모바일 서비스 성능비교. 떼어낼 디코더/HW/코드설계 없음.
- **ID**: ieee:8436918
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Sungjun Ahn, Sung-Ik Park, Jae-Young Lee +9
- **PDF**: https://ieeexplore.ieee.org/document/8436918
- **Abstract**: This paper presents performance comparison between layered division multiplexing (LDM) and time division multiplexing (TDM) based mobile services in the Advanced Television System Committee (ATSC) 3.0 standard. The comparison has been performed through extensive computer simulations, leveraging full-chain simulator entirely compliant with A/322. The simulation results demonstrate that LDM can significantly lower the signal-to-noise ratio (SNR) requirement compared to TDM in a given mobile scenario while maintaining the same (or analogous possible) data rate. For instance, LDM based mobile service is 6.1 dB more robust than TDM based service at a velocity of 100 km/h. In addition, even though LD M uses larger FFT size than TDM (16k-FFT for LDM and 8k-FFT for TDM), it is verified that LDM based mobile service is fully feasible under high speed condition.

## Laboratory Test Analysis of TxID Impact into ATSC 3.0 Preamble

- **Status**: ❌
- **Reason**: ATSC 3.0 TxID 프리앰블 영향 분석; LDPC/ECC 기법 없음
- **ID**: ieee:8436818
- **Type**: conference
- **Published**: 6-8 June 2
- **Authors**: Bo-Mi Lim, Sunhyoung Kwon, Sungjun Ahn +5
- **PDF**: https://ieeexplore.ieee.org/document/8436818
- **Abstract**: Advanced Television Systems Committee (ATSC) 3.0 is newly approved standard for a next generation digital television service. In the physical layer standard of ATSC 3.0, the transmitter identification (TxID), which is inserted into a host ATSC 3.0 preamble, is introduced supporting single frequency networks (SFNs). This paper presents impact analysis of TxID signal into the ATSC 3.0 preamble signal according to TxID injection levels. Laboratory tests are intensively performed to analyze possible impact to the host ATSC 3.0 preamble.

## Binary CEO Problem under Log-Loss with BSC Test-Channel Model

- **Status**: ❌
- **Reason**: binary CEO 소스코딩(LDGM-LDPC 양자화+신드롬). 채널 ECC 아닌 소스코딩이라 제외.
- **ID**: ieee:8494699
- **Type**: conference
- **Published**: 6-7 June 2
- **Authors**: Mahdi Nangir, Reza Asvadi, Mahmoud Ahmadian-Attari +1
- **PDF**: https://ieeexplore.ieee.org/document/8494699
- **Abstract**: In this paper, we propose an efficient coding scheme for the two-link binary Chief Executive Officer (CEO) problem under logarithmic loss criterion. The exact rate-distortion bound for a two-link binary CEO problem under the logarithmic loss has been obtained by Courtade and Weissman. We propose an encoding scheme based on compound LDGM-LDPC codes to achieve the theoretical bounds. In the proposed encoding, a binary quantizer using LDGM codes and a syndrome-coding employing LDPC codes are applied. An iterative joint decoding is also designed as a fusion center. The proposed CEO decoder is based on the sum-product algorithm and a soft estimator.

## Successive Wyner-Ziv Coding for the Binary CEO Problem under Log-Loss

- **Status**: ❌
- **Reason**: Wyner-Ziv binary CEO 소스코딩. 채널 ECC 아님, 떼어낼 ECC 기법 없음.
- **ID**: ieee:8494701
- **Type**: conference
- **Published**: 6-7 June 2
- **Authors**: Mahdi Nangir, Reza Asvadi, Mahmoud Ahmadian-Attari +1
- **PDF**: https://ieeexplore.ieee.org/document/8494701
- **Abstract**: An l-link binary CEO problem is considered in this paper. We present a practical encoding and decoding scheme for this problem employing the graph-based codes. A successive coding scheme is proposed for converting an l-link binary CEO problem to the $(2l-1)$ single binary Wyner-Ziv (WZ) problems. By using the compound LDGM-LDPC codes, the theoretical bound of each binary WZ is asymptotically achievable. Our proposed decoder successively decodes the received data by employing the well-known Sum-Product (SP) algorithm and leverages them to reconstruct the source. The sum-rate distortion performance of our proposed coding scheme is compared with the theoretical bounds under the logarithmic loss (log-loss) criterion.

## Entanglement-assisted nonbinary quantum LDPC codes with finite field method

- **Status**: ❌
- **Reason**: 비이진 양자 QC-LDPC + q-ary SPA 디코딩, 비이진+양자 이중 제외 대상
- **ID**: ieee:8397697
- **Type**: conference
- **Published**: 31 May-2 J
- **Authors**: Junhu Shao, Lin Zhou, Ying Sun
- **PDF**: https://ieeexplore.ieee.org/document/8397697
- **Abstract**: Based on quantum stabilizer formalism over multi-level quantum system, non-binary entanglement-assisted quantum coding theory was described in this paper. Then two classes of 2r-ary quantum quasi-cyclic LDPC codes were constructed by using algebraic finite field method over Fq with q = 2r. By iteratively decoded with q-ary sum-product algorithm (QSPA), the constructed 2r-ary quantum LDPC codes have shown significantly better performances than the present binary quantum LDPC codes.

## Analysis of 5G LDPC Codes Rate-Matching Design

- **Status**: ❌
- **Reason**: 5G NR LDPC rate-matching/IR-HARQ 분석. 표준 5G LDPC 구조·circular buffer 운용 분석으로 NAND에 떼어낼 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:8417496
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Fatemeh Hamidi-Sepehr, Ajit Nimbalker, Gregory Ermolaev
- **PDF**: https://ieeexplore.ieee.org/document/8417496
- **Abstract**: This paper analyzes the rate-matching algorithms for LDPC codes in 5G New Radio (NR) framework. Key features of NR LDPC rate-matching design includes flexible bit-selection based on circular buffer operation, enhanced decoding latency via code construction based on a single-parity-check extension from a high rate code, systematic bit puncturing, and support for limited buffer rate-matching (LBRM). IR-HARQ is supported via several redundancy versions (RVs) defined non-uniformly over the transmit circular buffer, enabling possibility of multiple self-decodable RVs. This paper, discusses NR LDPC structure, design, and its key features, followed by an in-depth investigation of IR-HARQ functionality, rate-matching, and (re-)transmissions via different RV ordering selections. Performance of single transmissions, as well as re-transmissions using different schemes are studied and evaluated using throughput and BLER metrics. This study attests the flexibility and robustness of NR LDPC design in addition to efficient support of IR-HARQ operation.

## A Design of Non-Binary Turbo Codes over Finite Fields Based on Gaussian Approximation and Union Bounds

- **Status**: ❌
- **Reason**: 비이진 turbo 부호 설계 - 비-LDPC 비이진 부호, 제외 대상
- **ID**: ieee:8417495
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Toshiki Matsumine, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/8417495
- **Abstract**: In this paper, we develop capacity-approaching non- binary turbo codes defined over high-order finite fields. Since the performance of turbo codes is characterized by the convergence behavior of iterative decoding and error floor in the high SNR region, we attempt to design the non-binary turbo codes based on the following two-stage optimization processes: In the first stage, we employ a Gaussian approximation method for non-binary turbo codes and analyze the convergence property of iterative decoding. After reducing the search space by the first stage, the best component convolutional codes are identified by examining the truncated union bound under the assumption of the uniform interleaver. Simulation results demonstrate that our non-binary turbo codes as designed above can outperform the conventional non-binary LDPC codes.

## NR - The New 5G Radio-Access Technology

- **Status**: ❌
- **Reason**: 5G NR 무선접속 기술 개요(서베이성). 구체적 신규 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:8417851
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Erik Dahlman, Stefan Parkvall
- **PDF**: https://ieeexplore.ieee.org/document/8417851
- **Abstract**: This paper provides a detailed overview of the key technology features of the new 5G/NR radio-access technology, the first release of which has recently been published by 3GPP release 15, of the NR specifications finalized by the end of 2017. This first release is limited to non-standalone NR operation, implying that NR devices rely on LTE for initial access and mobility. The final release-15 specifications, to be available in June 2018, will also support stand-alone NR operation. The difference between stand-alone and non-standalone operation is primarily affecting higher layers and the interface to the core network; the basic radio technology is the same in both cases. This paper will give a detailed overview of the NR radioaccess technology with focus on the key features that distinguish it from 4G LTE.

## Testbed Implementation and Evaluation of Interleaved and Scrambled Coding for Physical-Layer Security

- **Status**: ❌
- **Reason**: 물리계층 보안용 interleaving/scrambling 코딩 SDR 테스트베드. 보안 응용, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:8417699
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Cesar Martins, Telmo Fernandes, Marco Gomes +1
- **PDF**: https://ieeexplore.ieee.org/document/8417699
- **Abstract**: This paper presents a testbed implementation and evaluation of coding for secrecy schemes in a real environment through software defined radio platforms. These coding schemes rely on interleaving and scrambling with randomly generated keys to shuffle information before transmission. These keys are then encoded jointly with data and then hidden (erased) before transmission, thus only being retrievable through parity information resulting from encoded data. An advantage of the legitimate receiver (e.g. a better signal-to-noise ratio) on the reception of those keys provides the means to achieve secrecy against an adversary eavesdropper. Through this testbed implementation, we show the practical feasibility of coding for secrecy schemes in real-world environments, unveiling the usefulness of interleaving and scrambling with a hidden key to reduce the required advantage over an eavesdropper. We further describe and present solutions to a set of issues that appear when doing practical implementations of security schemes in software defined radio platforms.

## Cloud MIMO for Smart Parking System

- **Status**: ❌
- **Reason**: 클라우드 MIMO 스마트주차에 non-binary LDPC 적용 — 비이진 LDPC는 제외 대상이며 신규 디코더/구성 기여 없음
- **ID**: ieee:8417758
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Andrey Ivanov, Stanislav Kruglik, Dmitry Lakontsev
- **PDF**: https://ieeexplore.ieee.org/document/8417758
- **Abstract**: In this paper a cloud version of distributed reception scenario is analyzed in automated parking system. A parking sensor has a single antenna transmitter sending data to a large number of geographically separated single antenna receive routers. This scenario is applicable in smart parking system (SPS) enabled by Internet of Things (IoT). We propose a new functional split, which enables multiple-input multiple-output (MIMO) detection in cloud server and non-binary low density parity check (LDPC) codes application in SPS. The proposed architecture is intended to increase the uplink performance significantly in shadowed scenario and in strong interference scenario, leading to significant battery power saving in IoT sensor. Among other things, such approach requires less expenses due to reduced routers complexity and fits in future 5G concepts of massive IoT.

## Design and Performance of the Polar Coded Modulation for High Mobility Communications

- **Status**: ❌
- **Reason**: non-binary polar coded MLC, 고이동성 통신용. 비이진+비-LDPC 부호, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:8417807
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Peiyao Chen, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/8417807
- **Abstract**: With the development of the high-speed trains (HST), high spectral efficiency and low latency in high mobility scenarios have become an urgent demand. In this paper, we consider bandwidth-efficient multilevel coding (MLC) based on polar codes under high mobility scenarios. Since the use of a lot of binary coding levels and large list sizes will lead to a high latency for polar decoding, we first introduce a new kind of nonbinary polar codes based on multiplicative repetition method. Then, we employ the proposed codes as component codes for MLC scheme, and optimize the design for high mobility scenarios with low latency. Simulation results show that nonbinary polar coded MLC scheme (with less coding levels) outperform LTE turbo codes with high-order modulations, and can exhibit similar performance of binary polar coded bit-interleaved coded modulation scheme but with a smaller list size (reflecting low latency) over HST channels.

## Iterative MRC and EGC Receivers for MIMO-OFDM Systems

- **Status**: ❌
- **Reason**: MIMO-OFDM 반복 FDE 등화(EGC/MRC) 수신기. LDPC 부수 언급조차 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:8417595
- **Type**: conference
- **Published**: 3-6 June 2
- **Authors**: Andreia Pereira, Pedro Bento, Marco Gomes +2
- **PDF**: https://ieeexplore.ieee.org/document/8417595
- **Abstract**: This paper proposes a way of turning the equalisation of multiple- input multiple-output orthogonal frequency division multiplexing (MIMO-OFDM) signals simpler through the employment of low complexity iterative frequency domain equalisation (FDE) receivers based on equal gain combining (EGC) and maximum ratio combining (MRC) concepts, that do not require computing the inverses of high dimensional channel matrices. Performance results show that MIMO- OFDM schemes employing this type of techniques can achieve excellent bit error rate (BER) performances over severe time- dispersive channels and, therefore, approach or even outperform receivers that require inverting channel matrices, such as zero forcing (ZF) and minimum mean squared error (MMSE), after a few iterations.

## Detection of IJTAG attacks using LDPC-based feature reduction and machine learning

- **Status**: ❌
- **Reason**: LDPC 행렬을 IJTAG 공격탐지의 feature reduction(차원축소)에 사용 — 채널 ECC가 아니고 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:8400684
- **Type**: conference
- **Published**: 28 May-1 J
- **Authors**: Xuanle Ren, R. D. Shawn Blanton, Vítor Grade Tavares
- **PDF**: https://ieeexplore.ieee.org/document/8400684
- **Abstract**: IEEE 1687 standard (IJTAG), as an extension to the IEEE 1149.1, facilitates efficient access to embedded instruments by supporting reconfigurable scan networks. Specifically, IJTAG allows each IP to be wrapped by a test data register (TDR) whose access is controlled by a segment insertion bit (SIB) or a scan-mux control bit (SCB). Because the TDRs and the SIB/SCB network are typically not public, but critical for accessing embedded instruments, they might be used for illegitimate purposes, such as dumping credential data and reverse engineering IP design. Machine learning has been proposed to detect such attacks, but the large number of instruments and parallel execution enabled by the IJTAG produce high-dimensional data, which poses a challenge to on-chip detection. In this paper, we propose to reduce the high-dimensional but sparse data using a low-density parity-check (LDPC) matrix. Experiments using a modified version of the OpenSPARC T2 to include IJTAG functionality demonstrate that the use of feature reduction eliminates 91% of the features, leading to 43% reduction in circuit size without affecting detection accuracy. Also, the on-chip detector adds moderate overhead (∼ 8%) to the IJTAG.

## Rate-Compatible LDPC Based IDMA Scheme Supporting Grant-Free Transmission in eMBB

- **Status**: ❌
- **Reason**: IDMA 무선 grant-free 응용 특이적, RL-QC-LDPC는 5G 표준 유사 구성으로 떼어낼 신규 기법 없음
- **ID**: ieee:8450303
- **Type**: conference
- **Published**: 25-29 June
- **Authors**: Zhangmei Chen, Kewu Peng, Yushu Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8450303
- **Abstract**: Enhanced mobile broadband (eMBB) supports not only sustained high-data-rate transmission but also contention based grant-free transmission. For efficient radio resource utilization, interleave-division multiple access (IDMA) which is a promising instantiation of non-orthogonal multiple access is adopted for grant-free transmission in this paper. Conventional IDMA schemes mainly focus on low rate channel code which results in limited total spectral efficiency and limited choices of code rates. Moreover, IDMA schemes suffer from performance degradation under severe multi-user interference, since conventional coding scheme in IDMA is mainly optimized for point-to-point transmission. In this work, we propose a rate-compatible LDPC based IDMA solution to support grant-free transmission in eMBB. The raptor-like quasi-cyclic low-density parity-check (RL-QC-LDPC) codes contained in this solution are similar to the channel codes for 5G eMBB data channel in code rate and length, and optimized towards severe multi-user interference with the aid of multi-edge type density evolution based extrinsic information transfer chart tool. According to block error rate simulation results, the proposed rate-compatible LDPC based IDMA scheme is able to provide high throughput with near capacity performance and be robust to flexible number of access users.

## High Throughput Parallel Concatenated Encoding and Decoding for Polar Codes: Design, Implementation and Performance Analysis

- **Status**: ❌
- **Reason**: polar+LDPC 연접 BP의 GPU 병렬 처리, polar 비의존 신규 LDPC 디코더/HW 기여 없음(비-LDPC 원칙 제외)
- **ID**: ieee:8450398
- **Type**: conference
- **Published**: 25-29 June
- **Authors**: Jiaying Yin, Lixin Li, Huisheng Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/8450398
- **Abstract**: Polar codes can provably achieve the capacity of a symmetric binary discrete memoryless channel and have low encoding and decoding complexity. However, the error rate performance of polar codes decoding in short and moderate length is not very well, moreover, the encoding and decoding of polar codes with the conventional serial mode will lead to poor throughput. In this paper, we propose a hardware architecture of parallel encoding and decoding scheme for polar codes concatenation with LDPC, and take advantage of the parallelism of belief propagation (BP) decoding algorithm of the two codes to reduce the decoding delay. We compare the performance of concatenated scheme with polar codes and investigate the throughput implemented on graphic processing unit (GPU) for Gaussian channel. Experiment results show that the performance of the concatenated scheme outperform only polar codes, and the throughput of the proposed parallel architecture is obviously faster than that of the serial.

## Non-Linear Digital Self-Interference Cancellation for In-Band Full-Duplex Radios Using Neural Networks

- **Status**: ❌
- **Reason**: 풀듀플렉스 자기간섭 제거용 신경망, 채널 디코더 아님·LDPC 무관
- **ID**: ieee:8445987
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Alexios Balatsoukas-Stimming
- **PDF**: https://ieeexplore.ieee.org/document/8445987
- **Abstract**: Full-duplex systems require very strong self-interference cancellation in order to operate correctly and a significant part of the self-interference signal is due to non-linear effects created by various transceiver impairments. As such, linear cancellation alone is usually not sufficient and sophisticated non-linear cancellation algorithms have been proposed in the literature. In this work, we investigate the use of a neural network as an alternative to the traditional non-linear cancellation method that is based on polynomial basis functions. Measurement results from a full-duplex testbed demonstrate that a small and simple feed-forward neural network canceler works exceptionally well, as it can match the performance of the polynomial non-linear canceler with significantly lower computational complexity.

## Reputation and Credit Based Incentive Mechanism for Data-Centric Message Delivery in DTNs

- **Status**: ❌
- **Reason**: DTN 메시지 전달 평판/인센티브 메커니즘, ECC·LDPC 무관
- **ID**: ieee:8411278
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Himanshu Jethawa, Sanjay Madria
- **PDF**: https://ieeexplore.ieee.org/document/8411278
- **Abstract**: In Delay Tolerant Networks (DTNs), to ensure successful message delivery, contribution of mobile nodes in relaying in an opportunistic fashion is essential. In our proposed data-centric dissemination protocol here, messages (images) are annotated with keywords by the source, and then intermediate nodes are presented with an option of adding keyword-based annotations to create higher content strength messages enroute toward the destination. Therefore, the message contents like images get enriched as the ground situation evolves and learned by these intermediate nodes, such as in a disaster situation, or in a battlefield. Due to limited battery and storage capacity in mobile devices, nodes might turn selfish and do not participate in relaying or improving the quality of messages. Thus, additionally, an incentive mechanism is proposed in this paper which considers factors like message quality, level of interests, battery usage, etc for the calculation of incentives. At the same time, in order to prevent the nodes from turning malicious by adding inappropriate message tags in pursuit of acquiring more incentive, a distributed reputation model (DRM) is developed and integrated with the proposed incentive scheme. DRM takes into account inputs from the intermediate users like ratings of the message quality, relevance of annotations in the message, etc. The proposed scheme thus ensures avoidance of congestion due to uncooperative or selfish nodes in the system. The performance evaluations show that our approach delivers more high priority and quality messages with reduced traffic with a slightly lower message delivery ratio compared to a more recent DTN routing like ChitChat, where a source forwards a message to intermediate nodes, which meet or exceed the matching strength of keyword-based interests.

## Neural Network Aided Decoding for Physical-Layer Network Coding Random Access

- **Status**: ❌
- **Reason**: PNC 랜덤액세스 선형결합 선택용 신경망, LDPC BP 디코더 아님·떼어낼 ECC 기법 없음
- **ID**: ieee:8446014
- **Type**: conference
- **Published**: 25-28 June
- **Authors**: Adriano Pastore, Paul De Kerret, Monica Navarro +2
- **PDF**: https://ieeexplore.ieee.org/document/8446014
- **Abstract**: Hinging on ideas from physical-layer network coding, some promising proposals of coded random access systems seek to improve system performance (while preserving low complexity) by means of packet repetitions and decoding of linear combinations of colliding packets, whenever the decoding of individual packets fails. The resulting linear combinations are then temporarily stored in the hope of gathering enough linearly independent combinations so as to eventually recover all individual packets through the resolution of a linear system at the end of the contention frame. However, it is unclear which among the numerous linear combinations-whose number grows exponentially with the degree of collision-will have low probability of decoding error. Since no analytical framework exists to determine which combinations are easiest to decode, this makes the case for a machine learning algorithm to assist the receiver in deciding which linear combinations to target. For this purpose, we train neural networks that approximate the error probability for every possible linear combination based on the estimated channel gains and demonstrate the effectiveness of our approach by numerical simulations.

## Fast multiplication of binary polynomials with the forthcoming vectorized VPCLMULQDQ instruction

- **Status**: ❌
- **Reason**: GF(2^n) 다항식 곱셈 가속(VPCLMULQDQ) 암호용 primitive, LDPC와 무관
- **ID**: ieee:8464777
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Nir Drucker, Shay Gueron, Vlad Krasnov
- **PDF**: https://ieeexplore.ieee.org/document/8464777
- **Abstract**: Polynomial multiplication over binary fields \mathbbF2n is a common primitive, used for example by current cryptosystems such as AES-GCM (with n=128). It also turns out to be a primitive for other cryptosystems, that are being designed for the Post Quantum era, with values n ≫ 128. Examples from the recent submissions to the NIST Post-Quantum Cryptography project, are BIKE, LEDAKem, and GeMSS, where the performance of the polynomial multiplications, is significant. Therefore, efficient polynomial multiplication over F2n, with large n, is a significant emerging optimization target. Anticipating future applications, Intel has recently announced that its future architecture (codename “Ice Lake”) will introduce a new vectorized way to use the current VPCLMULQDQ instruction. In this paper, we demonstrate how to use this instruction for accelerating polynomial multiplication. Our analysis shows a prediction for at least 2× speedup for multiplications with polynomials of degree 512 or more.

## Proactive Channel Adjustment to Improve Polar Code Capability for Flash Storage Devices

- **Status**: ❌
- **Reason**: 플래시용 polar code 채널 튜닝(셀 품질 조정), polar 부호 비-LDPC이고 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:8465820
- **Type**: conference
- **Published**: 24-28 June
- **Authors**: Kun-Cheng Hsu, Che-Wei Tsao, Yuan-Hao Chang +2
- **PDF**: https://ieeexplore.ieee.org/document/8465820
- **Abstract**: With the low encoding/decoding complexity and the high error correction capability, polar code with the support of list-decoding and cyclic redundancy check can outperform LDPC code in the area of data communication. Thus, it also draws a lot of attentions on how to adopt and enable polar codes in storage applications. However, the code construction and encoding length limitation issues obstruct the adoption of polar codes in flash storage devices. To enable polar codes in flash storage devices, we propose a proactive channel adjustment design to extend the effective time of a code construction to improve the error correction capability of polar codes. This design pro-actively tunes the quality of the critical flash cells to maintain the correctness of the code construction and relax the constraint of the encoding length limitation, so that polar codes can be enabled in flash storage devices. A series of experiments demonstrates that the proposed design can effectively improve the error correction capability of polar codes in flash storage devices.

## Performance Comparison of Multi-Level Coding Schemes for Flash Memory

- **Status**: ❌
- **Reason**: NAND 플래시 대상이나 BCH 기반 MLC/MSD 부호화 비교 연구로 LDPC가 아니며, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:8552109
- **Type**: conference
- **Published**: 24-26 June
- **Authors**: Jieun Oh, Seokju Han
- **PDF**: https://ieeexplore.ieee.org/document/8552109
- **Abstract**: This paper compares performances of a number of multi-level coding (MLC)lmulti-stage decoding (MSD) schemes for NAND flash memory applications. A considered scheme is the MLC/MSD method of Imai and Hirakawa applied to l-dimensional (I-D) and 2-D constellations with Bose-Chaudhuri-Hocquemghem (BCH) component codes. By applying MLC/MSD techniques, it is possible to minimize the code rate loss caused by using the code designed for the bit level of page with the highest error rate equally to the remaining bit level of pages. The analytical error rate results indicate performance advantages of MLC/MSD schemes relative to the baseline BCH coding method.

## Achievable Rates for HDF WPNC Strategy with Hierarchical Bit-Wise Network Coding Maps for Higher-Order Constellations in H-MAC Channel with Relative Fading

- **Status**: ❌
- **Reason**: WPNC HDF 네트워크코딩 achievable rate 이론; LDPC는 부수 검증용, 떼어낼 ECC 기법 없음
- **ID**: ieee:8443240
- **Type**: conference
- **Published**: 18-21 June
- **Authors**: Jan Sykora, Petr Hron
- **PDF**: https://ieeexplore.ieee.org/document/8443240
- **Abstract**: The paper addresses Wireless Physical Layer Network Coding (WPNC) with Hierarchical Decode and Forward (HDF) strategy. We analyze achievable hierarchical rates in one stage hierarchical MAC (H-MAC) channel for higher order component constellations with bit-wise Hierarchical Network Code (HNC) maps. This is motivated by a possible application of state-of-the-art binary (e.g, LDPC) codes over higher order constellations. We show that the bit-mapped binary codes do not have the same achievable rates as direct higher-order codes. On top of this, the individual bits in the HNC map might provide very uneven performance and it strongly depends on the combination of component alphabets. The results are supported by a validation with practical LDPC codes.

## A Polar Code Hybrid Rate Matching Scheme

- **Status**: ❌
- **Reason**: polar code rate matching(shortening/puncturing) 기법; 비-LDPC이며 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:8442685
- **Type**: conference
- **Published**: 18-21 June
- **Authors**: Fengjun Xi, Chunxuan Ye, Robert L. Olesen
- **PDF**: https://ieeexplore.ieee.org/document/8442685
- **Abstract**: In recent 3GPP NR standards discussions for 5G, polar codes have been adopted as the control channel coding scheme when the payload size is more than 11 bits. The rate matching schemes for polar codes include shortening, puncturing and repetition. Each of these rate matching schemes has a performance advantage for different conditions. Hence, it is beneficial to include all three types of rate matching schemes. A circular buffer is also designed to support these rate matching schemes. In this paper, we propose a hybrid rate matching scheme which incorporates both shortening and puncturing techniques. This hybrid rate matching scheme provides a performance advantage for some conditions. Also, this hybrid rate matching scheme does not cause a significant impact on the existing polar coding system architecture. Simulation results are provided to show the performance benefit of this hybrid rate matching scheme.

## Low-Density Parity-Check Codes over Finite Gaussian Integer Fields

- **Status**: ❌
- **Reason**: Gaussian integer field 위 LDPC = 비이진(non-binary GF(q) 유사) LDPC, NAND 바이너리 표준 아님 → 제외
- **ID**: ieee:8437456
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Daniel Rohweder, Jürgen Freudenberger, Sergo Shavgulidze
- **PDF**: https://ieeexplore.ieee.org/document/8437456
- **Abstract**: This work proposes a construction for low-density parity-check (LDPC) codes over finite Gaussian integer fields. Furthermore, a new channel model for codes over Gaussian integers is introduced and its channel capacity is derived. This channel can be considered as a first order approximation of the additive white Gaussian noise channel with hard decision detection where only errors to nearest neighbors in the signal constellation are considered. For this channel, the proposed LDPC codes can be decoded with a simple non-probabilistic iterative decoding algorithm similar to Gallager's decoding algorithm A.

## Concatenated Spatially Coupled LDPC Codes for Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: 소스-채널 결합 코딩(JSCC)용 SC-LDPC — JSCC는 제외, 떼어낼 ECC 신규 기법 없음
- **ID**: ieee:8437885
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Ahmad Golmohammadi, David G.M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/8437885
- **Abstract**: In this paper, a method for joint source-channel coding (JSCC) based on concatenated spatially coupled low-density parity-check (SC-LDPC) codes is investigated. A construction consisting of two SC-LDPC codes is proposed: one for source coding and the other for channel coding, with a joint belief propagation-based decoder. Also, a novel windowed decoding (WD) scheme is presented with significantly reduced latency and complexity requirements. Simulation results show a notable performance improvement compared to existing state-of-the-art JSCC schemes based on LDPC codes.

## Hindering Reaction Attacks by Using Monomial Codes in the McEliece Cryptosystem

- **Status**: ❌
- **Reason**: QC-LDPC/MDPC McEliece 암호 reaction attack 방어(monomial code), 보안 도메인이고 NAND ECC 이식 기법 없음 → 제외
- **ID**: ieee:8437553
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Paolo Santini, Marco Baldi, Giovanni Cancellieri +1
- **PDF**: https://ieeexplore.ieee.org/document/8437553
- **Abstract**: In this paper we study recent reaction attacks against QC-LDPC and QC-MDPC code-based cryptosystems, which allow an opponent to recover the private parity-check matrix through its distance spectrum by observing a sufficiently high number of decryption failures. We consider a special class of codes, known as monomial codes, to form private keys with the desirable property of having a unique and complete distance spectrum. We verify that for these codes the problem of recovering the secret key from the distance spectrum is equivalent to that of finding cliques in a graph, and use this equivalence to prove that current reaction attacks are not applicable when codes of this type are used in the McEliece cryptosystem.

## A Message-Passing Algorithm for Counting Short Cycles in Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 짧은 사이클 카운팅 — 비이진 LDPC는 제외 대상
- **ID**: ieee:8437844
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Sunghye Cho, Kyungwhoon Cheun, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/8437844
- **Abstract**: Trapping sets with short cycles are known to give a detrimental effect on the error floor performance of a low-density parity-check (LDPC) code. Unlike in binary LDPC codes., short cycles in a nonbinary low-density parity-check (NB-LDPC) code may be even more harmful to its performance if they do not satisfy the so-called full rank condition (FRC). This is because they may induce low-weight codewords or absorbing sets in that case. Thus, it is crucial to count the number of short cycles not satisfying the FRC as well as the number of short cycles for analyzing the performance of an NB-LDPC code. In this paper, we first develop a novel message-passing algorithm and identify how it is related to the FRC. We then propose a low-complexity algorithm for counting the number of short cycles not satisfying the FRC in an NB-LDPC code, as well as the number of short cycles.

## Low-Complexity Multilevel LDPC Lattices and a Generalization of Construction D'

- **Status**: ❌
- **Reason**: 멀티레벨 LDPC 격자(lattice) 부호 — Construction D' 격자 응용, NAND 바이너리 ECC로 떼어낼 기법 없음
- **ID**: ieee:8437928
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Paulo Ricardo Branco da Silva, Danilo Silva
- **PDF**: https://ieeexplore.ieee.org/document/8437928
- **Abstract**: We propose efficient encoding and decoding algorithms for Construction D` multilevel LDPC lattices whose complexity is linear in the total number of coded bits. Moreover, we propose a generalization of Construction D ` that relaxes some of the nesting constraints on the component codes, leading to a simpler and improved design. Based on this construction, low-complexity multilevel LDPC lattices are designed whose performance under multistage lattice decoding is comparable to that of polar lattices on the power-unconstrained AWGN channel.

## Linear Rate-Compatible Codes with Degree-1 Extending Variable Nodes Under Iterative Decoding

- **Status**: ❌
- **Reason**: rate-compatible IR(PBRL) 수렴판정 이론 분석, NAND ECC와 무관한 RC 구조 특화로 떼어낼 디코더/HW 없음
- **ID**: ieee:8437332
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Sudarsan V.S. Ranganathan, Richard D. Wesel, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/8437332
- **Abstract**: A rate-compatible (RC) code first transmits a set of symbols corresponding to the highest rate. These symbols form the highest-rate code (HRC). If requested by the receiver, the transmitter subsequently sends symbols that lower the rate of the code. Additional symbols are sent until the decoder decodes to a codeword or all symbols of the RC code are exhausted. Consider linear, RC low-density parity-check (LDPC) codes constructed using extending variable nodes of degree 1. That is, every symbol of incremental redundancy (IR) is a linear combination only of symbols of the HRC. We study the convergence of such codes under iterative decoding. We show that the convergence criterion considered after each iteration need only check whether the HRC variable nodes have converged to a codeword. Specifically, there is no need to consider whether the parity checks that generate the IR symbols are satisfied. We substantiate these claims with simulation results of protograph-based raptor-like LDPC (PBRL) codes, which are a family of protograph RC-LDPC codes with the extending structure under consideration. Furthermore, we demonstrate using examples that this extending structure for protograph RC codes is not very far from the optimal extension for a protograph RC code by providing examples of iterative decoding thresholds for PBRL protographs and protographs extended using the optimal degrees for incremental variable nodes.

## Asymptotic Analysis on Spatial Coupling Coding for Two-Way Relay Channels

- **Status**: ❌
- **Reason**: 양방향 릴레이 채널 SC-LDPC 점근 DE 분석 — 무선 응용 특이적 순수 이론, 떼어낼 디코더/HW/구성 신규 기법 없음
- **ID**: ieee:8437898
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Satoshi Takabe, Yuta Ishimatsu, Tadashi Wadayama +1
- **PDF**: https://ieeexplore.ieee.org/document/8437898
- **Abstract**: Compute-and-forward relaying is effective to increase bandwidth efficiency of wireless two-way relay channels. In a compute-and-forward scheme, a relay tries to decode a linear combination composed of transmitted messages from other terminals or relays. Design for error correcting codes and its decoding algorithms suitable for compute-and-forward relaying schemes are still important issue to be studied. In this paper, we will present an asymptotic performance analysis on LDPC codes over two-way relay channels based on density evolution (DE). Because of the asymmetric nature of the channel, we employ the population dynamics DE combined with DE formulas for asymmetric channels to obtain BP thresholds. In addition, we also evaluate the asymptotic performance of spatially coupled LDPC codes for two-way relay channels. The results indicate that the spatial coupling codes yield improvements in the BP threshold compared with corresponding uncoupled codes for two-way relay channels.

## Information Coupled Polar Codes

- **Status**: ❌
- **Reason**: polar code spatial coupling 신규지만 polar 전용 디코딩, LDPC BP에 부호 비의존 이식 아님 → 제외
- **ID**: ieee:8437502
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Xiaowei Wu, Lei Yang, Jinhong Yuan
- **PDF**: https://ieeexplore.ieee.org/document/8437502
- **Abstract**: We propose a new class of spatially coupled polar codes, namely information coupled (IC) polar codes, to improve the error performance of finite length polar codes. In the proposed IC-polar codes, every two consecutive polar code blocks (CBs) in a frame are coupled by sharing a few information bits. We optimize the indices of coupling information so that the less reliable information bits in each CB can obtain more reliable messages from the consecutive CBs during decoding. A decoding scheme is proposed for the IC-polar codes. Simulation results show that the proposed IC-polar codes achieve a considerable gain over the uncoupled counterparts for variable code rates with a slightly increased decoding complexity.

## Non-Uniform Spatially-Coupled LDPC Codes over GF(2m)

- **Status**: ❌
- **Reason**: GF(2^m) 비이진 SC-LDPC — 비이진 LDPC는 제외 대상
- **ID**: ieee:8437900
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Ji Zhang, Baoming Bai, Dixia Deng +3
- **PDF**: https://ieeexplore.ieee.org/document/8437900
- **Abstract**: In this paper we consider the generalization of binary non-uniformly coupled low-density parity-check (LDPC) codes to that over Galois field GF $(2^{m})$. We will perform an iterative decoding threshold analysis for this class of non-uniformly coupled LDPC ensembles formed by randomly coupled and protograph-based coupled ensembles, respectively. By optimizing the coupling among spatial positions, we can construct codes having excellent thresholds and small rate-loss. Moreover, we propose a list-aided windowed decoding (list-aided WD) scheme for nonbinary SC-LDPC codes with low decoding latency. Numerical results show that the list-aided WD which outperforms conventional WD can perform better performance and lower decoding latency than the flooding-schedule decoding at low SNRs on the additive white Gaussian noise channel.

## A new construction of Quantum Error Correcting codes based on Difference Set

- **Status**: ❌
- **Reason**: 양자 오류정정(stabilizer/difference set) 구성, 양자 전용 개념 의존이며 qLDPC — 제외
- **ID**: ieee:8437811
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Tejas Gandhi
- **PDF**: https://ieeexplore.ieee.org/document/8437811
- **Abstract**: In this work we present a new construction of quantum error correcting codes. It is based on the stabilizer formalism but does not use the CSS construction. It takes advantage of the properties of the difference set to construct the code. The technique may also be used to generate the quantum LDPC codes as well as the cyclic codes.

## Attack on the Edon-kKey Encapsulation Mechanism

- **Status**: ❌
- **Reason**: McEliece/EDON-K 암호 공격, LRPC 랭크메트릭 부호 - 보안+비-LDPC 부호로 제외
- **ID**: ieee:8437498
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Matthieu Lequesne, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/8437498
- **Abstract**: The key encapsulation mechanism EDON-K was proposed in response to the call for post-quantum cryptography standardization issued by the National Institute of Standards and Technologies (NIST). This scheme is inspired by the McEliece scheme but uses another family of codes defined over F2128 instead of F2 and is not based on the Hamming metric. It allows significantly shorter public keys than the McEliece scheme. In this paper, we give a polynomial time algorithm that recovers the encapsulated secret. This attack makes the scheme insecure for the intended use. We obtain this result by observing that recovering the error in the McEliece scheme corresponding to EDON-K can be viewed as a decoding problem for the rank-metric. We show that the code used in EDON-K is in fact a super-code of a Low Rank Parity Check (LRPC) code of very small rank (1 or 2). A suitable parity-check matrix for the super-code of such low rank can be easily derived from for the public key. We then use this parity-check matrix in a decoding algorithm that was devised for LRPC codes to recover the error. Finally we explain how we decapsulate the secret once we have found the error.

## Almost Optimal Scaling of Reed-Muller Codes on BEC and BSC Channels

- **Status**: ❌
- **Reason**: Reed-Muller 부호 BEC/BSC scaling 순수 이론 bound, 디코더/HW/구성으로 안 이어짐 + 비-LDPC
- **ID**: ieee:8437453
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Hamed Hassani, Shrinivas Kudekar, Or Ordentlich +2
- **PDF**: https://ieeexplore.ieee.org/document/8437453
- **Abstract**: Consider a binary linear code of length N, minimum distance dmin, transmission over the binary erasure channel with parameter 0 <; ε <; 1 or the binary symmetric channel with parameter 0 <; ε <; 1/2 , and block-MAP decoding. It was shown by Tillich and Zemor that in this case the error probability of the block-MAP decoder transitions “quickly” from δ to 1- δ for any δ > 0 if the minimum distance is large. In particular the width of the transition is of order O(1/√dmin). We strengthen this result by showing that under suitable conditions on the weight distribution of the code, the transition width can be as small as O(1/N1/2-κ), for any κ > 0, even if the minimum distance of the code is not linear. This condition applies e.g., to Reed-Mueller codes. Since O(1/N1/2) is the smallest transition possible for any code, we speak of “almost” optimal scaling. We emphasize that the width of the transition says nothing about the location of the transition. Therefore this result has no bearing on whether a code is capacity-achieving or not. As a second contribution, we present a new estimate on the derivative of the EXIT function, the proof of which is based on the Blowing-Up Lemma.

## The Stability Condition of LDPC Codes Under MAP Decoding

- **Status**: ❌
- **Reason**: LDPC MAP 디코딩 stability condition — 순수 이론 threshold bound, 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:8437939
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Wei Liu, Rüdiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/8437939
- **Abstract**: We determine the stability condition of low-density parity-check codes under both bitwise and blockwise maximum $a$ posteriori decoding. As a consequence, we prove that the stability condition determines an upper bound on both the bitwise and the blockwise maximum $a$ posteriori threshold.

## Bit-Labeling for Delayed BICM with Iterative Decoding

- **Status**: ❌
- **Reason**: BICM-ID 비트라벨링 변조 기법, 채널코딩 ECC 아닌 변조/매핑으로 이식 기법 없음
- **ID**: ieee:8437452
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Leijun Wang, Suihua Cai, Huixiao Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/8437452
- **Abstract**: This paper is concerned with the delayed bit-interleaved coded modulation with iterative decoding (DBICM-ID). We present new criteria for bit-labeling in the DBICM-ID system based on the harmonic mean of the minimum squared Euclidean distance (HMMSED) and the mean average bit-wise mutual information (MABMI) criteria. Different from the conventional HMMSED criterion, taking into account the conditions varying from no feedback to perfect feedback, we also evaluate the variance of the harmonic mean, which is then deployed to reveal the convergence rate. We take 16-QAM as an example to confirm our analysis. Numerical results show that, DBICM-ID with the designed bit-labeling scheme can obtain an extra coding gain of about 0.5 dB.

## Coded Computation Against Straggling Decoders for Network Function Virtualization

- **Status**: ❌
- **Reason**: 클라우드 NFV straggling 완화 coded computation, 채널 ECC 이식 기법 없음 → 제외
- **ID**: ieee:8437525
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Malihe Aliasgari, Jorg Kliewer, Osvaldo Simeone
- **PDF**: https://ieeexplore.ieee.org/document/8437525
- **Abstract**: The uplink of a cloud radio access network architecture is studied in which decoding at the cloud takes place via network function virtualization (NFV) on commercial off-the-shelf (COTS) servers. In order to mitigate the impact of straggling decoders in the cloud computing platform, a novel coding strategy is proposed, whereby the cloud re-encodes the received frames via a linear code before distributing them to the decoding processors. Upper bounds on the resulting frame unavailability probability (FUP) as a function of the decoding latency are derived by assuming a binary symmetric channel for uplink communications. The bounds leverage large deviation results for correlated variables, and depend on the properties of both the uplink linear channel code adopted at the user and the NFV linear code applied at the cloud. Numerical examples demonstrate that the bounds are useful tools for code design, and that coding is instrumental in obtaining a desirable tradeoff between FUP and decoding latency.

## Adaptive Path Interpolation for Sparse Systems: Application to a Simple Censored Block Model

- **Status**: ❌
- **Reason**: sparse factor graph의 mutual information 점근 계산용 순수 이론(adaptive path interpolation), 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:8437628
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Jean Barbier, Chun Lam Chan, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/8437628
- **Abstract**: A new adaptive path interpolation method has been recently developed as a simple and versatile scheme to calculate exactly the asymptotic mutual information of Bayesian inference problems defined on dense factor graphs. These include random linear and generalized estimation, superposition codes, or low rank matrix and tensor estimation. For all these systems the method directly proves in a unified manner that the replica symmetric prediction is exact. When the underlying factor graph of the inference problem is sparse the replica prediction is considerably more complicated and rigorous results are often lacking or obtained by rather complicated methods. In this contribution we extend the adaptive path interpolation method to sparse systems. We concentrate on a Censored Block Model, where hidden variables are measured through a binary erasure channel, for which we fully prove the replica prediction.

## Sublinear- Time Algorithms for Compressive Phase Retrieval

- **Status**: ❌
- **Reason**: compressive phase retrieval sublinear 알고리즘, LDPC ECC 디코더/HW/구성 이식 기법 없음 → 제외
- **ID**: ieee:8437599
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Yi Li, Vasileios Nakos
- **PDF**: https://ieeexplore.ieee.org/document/8437599
- **Abstract**: In the compressive phase retrieval problem, the goal is to reconstruct a sparse or approximately k-sparse vector x ∈ Rn given access to y = |Φx|, where |v| denotes the vector obtained from taking the absolute value of v ∈ Rn coordinatewise. In this paper we present sublinear-time algorithms for different variants of the compressive phase retrieval problem which are akin to the variants of the classical compressive sensing problem considered in theoretical computer science. Our algorithms use pure combinatorial techniques and achieve almost optimal number of measurements.

## A Class of Low-Complexity Codes Based on Doubly Recursive Block Markov Superposition Transmission

- **Status**: ❌
- **Reason**: DrBMST(블록 마르코프 중첩전송) 부호로 SC-LDPC는 비교 베이스라인일 뿐, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8437683
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Shancheng Zhao, Xiao Ma, Qin Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/8437683
- **Abstract**: In this paper, we introduce the doubly recursive block Markov superposition transmission (DrBMST) of short code. An important characteristic of DrBMST codes is that the degrees of the constraint nodes in their normal graphical realizations are at most three. As a result, DrBMST codes can be decoded with low complexity. We propose to use an enlarged code ensemble to analyze the performance of DrBMST under windowed maximum likelihood decoding. Further, the extrinsic information transfer (EXIT) chart analysis is used to study the iterative decoding thresholds of DrBMST code ensembles. The EXIT analysis shows that the iterative decoding thresholds of DrBMST code ensembles are comparable to those of the BMST codes. We have also compared the error performance and the decoding complexity of finite-length DrBMST codes with regular spatial-coupled low-density parity-check (SC-LDPC) codes under equal decoding latency. The comparison results show that the DrBMST code performs about 0.1 dB better than a (4, 8)-regular SC-LDPC code, but with lower computational complexity.

## ARQ for Interference Packet Networks

- **Status**: ❌
- **Reason**: 무선 패킷망 ARQ 프로토콜, LDPC 무관
- **ID**: ieee:8437334
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Alireza Vahid, Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/8437334
- **Abstract**: In multi-user wireless packet networks interference is the throughput bottleneck. Users become aware of the interference pattern via feedback and use this information for contention resolution and for packet retransmission. We consider networks with spatially correlated wireless links, and we develop an opportunistic automatic repeat request function for these networks. We prove the optimality of our protocol using an extremal rank-ratio inequality for spatially correlated channels.

## Hamming-Distance-Based Binary Representation of Numbers

- **Status**: ❌
- **Reason**: Hamming거리 기반 수 표현 인코딩, LDPC ECC 아님(채널코딩 무관)
- **ID**: ieee:8437644
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Minghai Qin
- **PDF**: https://ieeexplore.ieee.org/document/8437644
- **Abstract**: Numbers are represented as binary arrays in computer storage. We propose a length-n binary representation of numbers from 0 to 2n-1 based on Hamming distances such that for any i ∈ {0, ..., 2n-1}, if a constant number of bits (out of n) are flipped, the normalized L1 distance from the distorted number ierror to i is vanishing when n tends to infinity. More precisely, maxi[(|ierror-i|)/(2n)]=o([1/(√n)]). A pair of encoder and decoder with O(n) time complexity is presented to establish the Hamming-distance-based bijection between {0,1}n and {0,1, ..., 2n-1}.

## The Decoding Failure Probability of MDPC Codes

- **Status**: ❌
- **Reason**: MDPC 암호용 부호의 디코딩 실패확률 분석 — bit-flipping 표준, 암호 응용이라 NAND ECC로 떼어낼 신규 기법 없음
- **ID**: ieee:8437843
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/8437843
- **Abstract**: Moderate Density Parity Check (MDPC) codes are defined here as codes which have a parity-check matrix whose row weight is $O(\sqrt{n})$ where $n$ is the length $n$ of the code. They can be decoded like LDPC codes but they decode much less errors than LDPC codes: the number of errors they can decode in this case is of order $\Theta(\sqrt{n})$. Despite this fact they have been proved very useful in cryptography for devising key exchange mechanisms. They have also been proposed in McEliece type cryptosystems. However in this case, the parameters that have been proposed in [11] were broken in [9]. This attack exploits the fact that the decoding failure probability is non-negligible. We show here that this attack can be thwarted by choosing the parameters in a more conservative way. We first show that such codes can decode with a simple bit-flipping decoder any pattern of $O(\frac{\sqrt{n}\log\log n}{\log n})$ errors. This avoids the previous attack at the cost of significantly increasing the key size of the scheme. We then show that under a very reasonable assumption the decoding failure probability decays almost exponentially with the codelength with just two iterations of bit-flipping. With an additional assumption it has even been proved that it decays exponentially with an unbounded number of iterations and we show that in this case the increase of the key size which is required for resisting to the [9] attack is only moderate.

## Ouroboros-E: An Efficient Lattice-based Key-Exchange Protocol

- **Status**: ❌
- **Reason**: 격자 기반 키교환(보안), bit-flipping을 유클리드 메트릭으로 변형 — 양자/보안 도메인, NAND 바이너리 LDPC ECC로 이식 불가
- **ID**: ieee:8437940
- **Type**: conference
- **Published**: 17-22 June
- **Authors**: Jean-Christophe Deneuville, Philippe Gaborit, Qian Guo +1
- **PDF**: https://ieeexplore.ieee.org/document/8437940
- **Abstract**: The Bit Flipping algorithm is a hard decision decoding algorithm originally designed by Gallager in 1962 to decode Low Density Parity Check Codes (LDPC). It has recently proved to be much more versatile, for Moderate Parity Check Codes (MDPC) or Euclidean metric. We further demonstrate its power by proposing a noisy Euclidean version of it. This tweak allows to construct a lattice based key exchange analogous to the Ouroboros protocol for Hamming metric but with a reduction to the Short Integer Solution (SIS) problem. The very efficient decoding algorithm permits to consider smaller alphabets than for NTRU or Ring-LWE decryption algorithms. Overall we obtain a new protocol which competes with the recent NEWHOPE and Kyber proposals, and also with NTRU. The resulting scheme exploits the cyclicity of the error, and benefits from the security of the renowned SIS problem.

## Multilevel Coding for Physical-Layer Security in Optical Networks

- **Status**: ❌
- **Reason**: 광통신 물리계층 보안용 multilevel coding+punctured LDPC, 보안 응용에 LDPC 부수 사용, 신규 디코더/구성 없음
- **ID**: ieee:8436122
- **Type**: conference
- **Published**: 11-12 June
- **Authors**: Johannes Pfeiffer, Robert F. H. Fischer
- **PDF**: https://ieeexplore.ieee.org/document/8436122
- **Abstract**: In this paper, multilevel coding in combination with signal shaping is studied for generating both security against a wiretapper and reliability for the legitimate user. Based on the concept of equivalent bit channels defined by the address bits of M-ary modulation schemes, the effects of using higher-order signaling schemes and signal shaping on the capacity and error rate performance are examined. It is shown that transmission over the LSB channel, encoded via punctured LDPC codes, reduces the resulting security gaps significantly in comparison to binary transmission. Results from numerical simulations cover the theoretical considerations.

## Developing the principle of divergent coding for Gaussian channels

- **Status**: ❌
- **Reason**: convolutional code의 multithreshold/Viterbi 다중알고리즘 디코딩, 비-LDPC 부호이며 BP 이식성 없음
- **ID**: ieee:8405964
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Zolotarev Valery, Grinchenko Natalya, Lotsmanov Alexey +1
- **PDF**: https://ieeexplore.ieee.org/document/8405964
- **Abstract**: Mutithreshold decoding for convolutional codes implementing optimization methods to correct errors based on the search of global extremum of functionals in discrete spaces are considered. The implementation of divergent coding methods with triple concatenation to achieve highly efficient decoding near channel capacity is described. The possibilities of this approach while using concatenation are shown. Multialgorithmic decoding is offered. It implements the principle of divergence with simultaneous usage of two types of decoders: Viterbi algorithm and multithreshold decoding. The implementation of multialgorithmic decoding is shown to substantially decrease decoding complexity at low signal to noise ratio.
