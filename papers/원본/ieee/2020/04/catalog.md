# IEEE Xplore — 2020-04


## A Threshold-Based Min-Sum Algorithm to Lower the Error Floors of Quantized LDPC Decoders

- **Status**: ✅
- **Reason**: 양자화 디코더 error floor를 낮추는 새 threshold-based min-sum 변형 제안 — 이식 가능 디코더(C), NAND LDPC 직접 적용 가능
- **ID**: ieee:8970554
- **Type**: journal
- **Published**: April 2020
- **Authors**: Homayoon Hatami, David G. M. Mitchell, Daniel J. Costello +1
- **PDF**: https://ieeexplore.ieee.org/document/8970554
- **Abstract**: For decoding low-density parity-check (LDPC) codes, the attenuated min-sum algorithm (AMSA) and the offset min-sum algorithm (OMSA) can outperform the conventional min-sum algorithm (MSA) at low signal-to-noise-ratios (SNRs), i.e., in the “waterfall region” of the bit error rate curve. This paper demonstrates that, for quantized decoders, MSA actually outperforms AMSA and OMSA in the “error floor” region, and that all three algorithms suffer from a relatively high error floor. This motivates the introduction of a modified MSA that is designed to outperform MSA, AMSA, and OMSA across all SNRs. The new algorithm is based on the assumption that trapping sets are the major cause of the error floor for quantized LDPC decoders. A performance estimation tool based on trapping sets is used to verify the effectiveness of the new algorithm and also to guide parameter selection. We also show that the implementation complexity of the new algorithm is only slightly higher than that of AMSA or OMSA. Finally, the simulated performance of the new algorithm, using several classes of LDPC codes (including spatially coupled LDPC codes), is shown to outperform MSA, AMSA, and OMSA across all SNRs.

## Using Error Modes Aware LDPC to Improve Decoding Performance of 3-D TLC NAND Flash

- **Status**: ✅
- **Reason**: 3D TLC NAND에 직접 적용한 error-mode 인식 LDPC LLR 최적화로 디코딩 지연/BER 개선 (카테고리 A)
- **ID**: ieee:8634908
- **Type**: journal
- **Published**: April 2020
- **Authors**: Fei Wu, Meng Zhang, Yajuan Du +5
- **PDF**: https://ieeexplore.ieee.org/document/8634908
- **Abstract**: 3-D triple-level cell (3-D TLC) NAND flash has high storage density and capacity, but degrading data reliability due to high raw bit error rates induced by a certain number of program/erase cycles. To guarantee data reliability, low-density parity-check (LDPC) codes are selected as the error correction codes in modern flash memories because of strong error correction capability. However, directly adopting LDPC codes induces high decoding latency due to iterative updating of log-likelihood ratio (LLR) information in the decoding process. Increasing LLR information accuracy can greatly improve decoding performance. In this paper, we propose EMAL: using error modes aware LDPC codes for further enhancing the decoding performance of 3-D TLC NAND flash. We first obtain 3-D TLC error modes based on an FPGA testing platform, and then exploit the error modes to optimize LLR information and enable the decoding to converge at a high speed. The simulation results show that the decoding performance is significantly improved, resulting in reduced bit error rates and decoding latency.

## A 75-Gb/s/mm2 and Energy-Efficient LDPC Decoder Based on a Reduced Complexity Second Minimum Approximation Min-Sum Algorithm

- **Status**: ✅
- **Reason**: 신규 SAMS(second minimum approximation min-sum) 알고리즘 + 라우팅 절감 VLSI 디코더 → 이식 가능 디코더/HW (C/D)
- **ID**: ieee:8935206
- **Type**: journal
- **Published**: April 2020
- **Authors**: Henry Lopez, Hsun-Wei Chan, Kang-Lun Chiu +2
- **PDF**: https://ieeexplore.ieee.org/document/8935206
- **Abstract**: This article presents a high-throughput and low-routing complexity low-density parity check (LDPC) decoder design based on a novel second minimum approximation min-sum (SAMS) algorithm. The routing congestion is mitigated by reducing the required interconnections in the critical path of the routing network. The implementation and postlayout results with 28-nm 1P9M CMOS process show that the proposed design can achieve a throughput of 10.5 Gb/s for a millimeter-wave 60-GHz baseband system while satisfying the low bit error rate (BER) requirements (10-7). The proposed design reduces the wiring in the routing network by 21% and improves the area by 12% compared to the conventional min-sum (MS) and normalized MS (NMS) algorithm. Additional hardware optimizations are obtained by considering the internal message passing resolution based on the BER and signal-to-noise ratio (SNR) requirements for a practical baseband system. The power consumption is efficiently reduced by the employment of a shared address generator that exploits the degree of parallelism to reduce the switching activity on a group of memory elements. The LDPC decoder is implemented with a core area of 0.14 mm2, power consumption of 81 mW at 312.5 MHz, and the area and power efficiency of 75 Gb/s/mm2 and 10.2 pJ/bit, respectively.

## Failure Analysis of the Interval-Passing Algorithm for Compressed Sensing

- **Status**: ✅
- **Reason**: compressed sensing IPA 실패셋 분석이나 array LDPC 패리티검사행렬 기반 trapping/termatiko set·4-cycle 회피·minimum distance bound는 바이너리 LDPC 코드설계로 이식 가능 (E, 애매하여 살림)
- **ID**: ieee:8968331
- **Type**: journal
- **Published**: April 2020
- **Authors**: Yauhen Yakimenka, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/8968331
- **Abstract**: In this work, we perform a complete failure analysis of the interval-passing algorithm (IPA) for compressed sensing. The IPA is an efficient iterative algorithm for reconstructing a k-sparse nonnegative n-dimensional real signal x from a small number of linear measurements y . In particular, we show that the IPA fails to recover x from y if and only if it fails to recover a corresponding binary vector of the same support, and also that only positions of nonzero values in the measurement matrix are of importance to the success of recovery. Based on this observation, we introduce termatiko sets and show that the IPA fails to fully recover x if and only if the support of x contains a nonempty termatiko set, thus giving a complete (graph-theoretic) description of the failing sets of the IPA. Two heuristics to locate small-size termatiko sets are presented. For binary column-regular measurement matrices with no 4-cycles, we provide a lower bound on the termatiko distance, defined as the smallest size of a nonempty termatiko set. For measurement matrices constructed from the parity-check matrices of array low-density parity-check codes, upper bounds on the termatiko distance equal to half the best known upper bound on the minimum distance are provided for column-weight at most 7, while for column-weight 3, the exact termatiko distance and its corresponding multiplicity are provided. Next, we show that adding redundant rows to the measurement matrix does not create new termatiko sets, but rather potentially removes termatiko sets and thus improves performance. An algorithm is provided to efficiently search for such redundant rows. Finally, we present numerical results for different specific measurement matrices and also for protograph-based ensembles of measurement matrices, as well as simulation results of IPA performance, showing the influence of small-size termatiko sets.

## Edge-Coloring Technique to Analyze Elementary Trapping Sets of Spatially-Coupled LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: SC-LDPC의 elementary trapping set을 edge-coloring으로 분석·회피하는 신규 코드설계 기법, 바이너리 protograph (카테고리 E)
- **ID**: ieee:8943947
- **Type**: journal
- **Published**: April 2020
- **Authors**: Mohammad-Reza Sadeghi, Farzane Amirzade
- **PDF**: https://ieeexplore.ieee.org/document/8943947
- **Abstract**: In this letter, for the first time, an edge-coloring technique is proposed to characterize a certain elementary trapping set (ETS) and to obtain sufficient conditions to avoid small ETSs from occurrence in the Tanner graph of SC-LDPC convolutional codes. This technique is applicable to all protograph-based LDPC codes with different girths whose protographs are single-edge, that is, the entries of their base matrices are 0, 1. To further demonstrate the effectiveness of our proposed technique, we apply it to Time-Invariant SC-LDPC-CCs with girths 6 and 8 and column weights up to 5.

## Syndrome-Coupled Rate-Compatible Error-Correcting Codes: Theory and Application

- **Status**: ✅
- **Reason**: 코셋·신드롬 기반 rate-compatible LDPC/BCH 신규 구성을 MLC 플래시에 적용 평가, 바이너리 (B/E)
- **ID**: ieee:8957447
- **Type**: journal
- **Published**: April 2020
- **Authors**: Pengfei Huang, Yi Liu, Xiaojie Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8957447
- **Abstract**: Rate-compatible error-correcting codes (ECCs), which consist of a set of extended codes, are of practical interest in both wireless communications and data storage. In this work, we first study the lower bounds for rate-compatible ECCs, thus proving the existence of good rate-compatible codes. Then, we propose a general framework for constructing rate-compatible ECCs based on cosets and syndromes of a set of nested linear codes. We evaluate our construction from two points of view. From a combinatorial perspective, we show that we can construct rate-compatible codes with increasing minimum distances, and we discuss decoding algorithms and correctable patterns of errors and erasures. From a probabilistic point of view, we prove that we are able to construct capacity-achieving rate-compatible codes, generalizing a recent construction of capacity-achieving rate-compatible polar codes. Applications of rate-compatible codes to data storage are considered. We design two-level rate-compatible codes based on Bose-Chaudhuri-Hocquenghem (BCH) and low-density parity-check (LDPC) codes which are two popular codes widely used in the data storage industry, and then we evaluate the performance of these codes in multi-level cell (MLC) flash memories. We also examine code performance on binary and $q$ -ary symmetric channels. Finally, we briefly discuss two variations of our main construction and their relative performance.

## Interleaved Polar (I-Polar) Codes

- **Status**: ❌
- **Reason**: Interleaved polar code 구성·WEF 분석으로 polar 코드 전용, LDPC 이식 기법 없음
- **ID**: ieee:8968424
- **Type**: journal
- **Published**: April 2020
- **Authors**: Mao-Ching Chiu
- **PDF**: https://ieeexplore.ieee.org/document/8968424
- **Abstract**: By inserting interleavers between intermediate stages of the polar encoder, a new class of polar codes, termed interleaved polar (i-polar) codes, is proposed. By the uniform interleaver assumption, we derive the weight enumerating function (WEF) and the input-output weight enumerating function (IOWEF) averaged over the ensemble of i-polar codes. The average WEF can be used to calculate the upper bound on the average block error rate (BLER) of a code selected at random from the ensemble of i-polar codes. Also, we propose a concatenated coding scheme that employs P high rate codes as the outer code and Q i-polar codes as the inner code with an interleaver in between. The average WEF of the concatenated code is derived based on the uniform interleaver assumption. Simulation results show that BLER upper bounds can well predict BLER performance levels of the concatenated codes. The results show that the performance of the proposed concatenated code with P=Q=2 is better than that of the CRC-aided i-polar code with P=Q=1 of the same length and code rate at high signal-to-noise ratios (SNRs). Moreover, the proposed concatenated code allows multiple decoders to operate in parallel, which can reduce the decoding latency and hence is suitable for ultra-reliable low-latency communications (URLLC).

## A Grant-Free Random Access Scheme for M2M Communication in Massive MIMO Systems

- **Status**: ❌
- **Reason**: massive MIMO grant-free random access의 EICA 검출 알고리즘 — LDPC ECC 기법 없음, 무선 응용 특이적
- **ID**: ieee:8993804
- **Type**: journal
- **Published**: April 2020
- **Authors**: Huimei Han, Ying Li, Wenchao Zhai +1
- **PDF**: https://ieeexplore.ieee.org/document/8993804
- **Abstract**: A novel grant-free random access scheme is proposed to support massive connectivity with low access delay and overhead for machine-to-machine communication in massive multiple-input-multiple-output systems. This scheme allows all active user equipments (UEs) to transmit their pilots and uplink messages via the same time-frequency resource and performs the joint active UEs detection and uplink message decoding without channel estimation in one shot by utilizing the proposed ensemble independent component analysis (EICA) decoding algorithm. We call the proposed scheme the EICA-based pilot random access (EICA-PA). We analyze the successful access probability, probability of missed detection, and uplink throughput of the EICA-PA scheme. Numerical results show that the EICA-PA scheme significantly improves the successful access probability and uplink throughput, decreases missed detection probability and provides low-frame error rate at the same time.

## Efficient Sparse Code Multiple Access Decoder Based on Deterministic Message Passing Algorithm

- **Status**: ❌
- **Reason**: SCMA(비직교 다중접속) 디코더로 LDPC ECC가 아닌 NOMA 검출, 이식 ECC 기법 없음
- **ID**: ieee:8967122
- **Type**: journal
- **Published**: April 2020
- **Authors**: Chuan Zhang, Chao Yang, Xu Pang +5
- **PDF**: https://ieeexplore.ieee.org/document/8967122
- **Abstract**: Being an effective non-orthogonal multiple access (NOMA) technique, sparse code multiple access (SCMA) is promising for future wireless communication. Compared with orthogonal techniques, SCMA enjoys higher overloading tolerance and lower complexity because of its sparsity. In this paper, based on deterministic message passing algorithm (DMPA), algorithmic simplifications such as domain changing and probability approximation are applied for SCMA decoding. Early termination, adaptive decoding, and initial noise reduction are also employed for faster convergence and better performance. Numerical results show that the proposed optimizations benefit both decoding complexity and speed. Furthermore, efficient hardware architectures based on folding and retiming are proposed. VLSI implementation is also given in this paper. Comparison with the state-of-the-art have shown the proposed decoder's advantages in both latency and throughput (multi-Gbps).

## Blind Estimation of Code Parameters for Product Codes Over Noisy Channel Conditions

- **Status**: ❌
- **Reason**: Product code(RS/BCH) 파라미터 블라인드 추정으로 LDPC ECC 기법 없음
- **ID**: ieee:8804240
- **Type**: journal
- **Published**: April 2020
- **Authors**: R. Swaminathan, A.S. Madhukumar, Guohua Wang
- **PDF**: https://ieeexplore.ieee.org/document/8804240
- **Abstract**: Product codes are multidimensional codes constructed using multiple component codes. In this paper, novel algorithms are proposed for the blind estimation of two-dimensional product code parameters over the noisy channel conditions considering Reed-Solomon and Bose-Chaudhuri-Hocquenghem as component codes. The performance of the algorithms in terms of probability of the correct estimation is investigated for different code parameters. It is observed that the accuracy improves with the decrease in modulation order and code dimension values.

## Low-Complexity Detection for Faster-than-Nyquist Signaling Based on Probabilistic Data Association

- **Status**: ❌
- **Reason**: FTN 신호 BPSK 시퀀스 검출(PDA)로 LDPC ECC 기법 아님
- **ID**: ieee:8941122
- **Type**: journal
- **Published**: April 2020
- **Authors**: Michel Kulhandjian, Ebrahim Bedeer, Hovannes Kulhandjian +2
- **PDF**: https://ieeexplore.ieee.org/document/8941122
- **Abstract**: In this letter, we investigate the sequence estimation problem of faster-than-Nyquist (FTN) signaling as a promising approach for increasing spectral efficiency (SE) in future communication systems. In doing so, we exploit the concept of Gaussian separability and propose two probabilistic data association (PDA) algorithms with polynomial time complexity to detect binary phase-shift keying (BPSK) FTN signaling. Simulation results show that the proposed PDA algorithm outperforms the recently proposed SSSSE and SSSgbKSE algorithms for all SE values with a modest increase in complexity. The PDA algorithm approaches the performance of the semidefinite relaxation (SDRSE) algorithm for SE values of 0.96 bits/sec/Hz, and it is within the 0.5 dB signal-to-noise ratio (SNR) penalty at SE values of 1.10 bits/sec/Hz for the fixed values of β = 0.3.

## Comprehensive Study on CC-LDPC, BC-LDPC and Polar Code

- **Status**: ❌
- **Reason**: Survey comparing CC-LDPC/BC-LDPC/polar for 6G; comparative study only, no new binary LDPC decoder/HW/construction to extract
- **ID**: ieee:9124897
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Kun Zhu, Zhanji Wu
- **PDF**: https://ieeexplore.ieee.org/document/9124897
- **Abstract**: Channel coding scheme is very crucial for the next sixth generation (6G) mobile communication. In this paper, we investigate the encoding and decoding methods of the state-of-the-art channel codes, which include the convolutional code LDPC (CC-LDPC), block code LDPC (BC-LDPC) and polar code to access the benefits from CC-LDPC. And then, we present comprehensive evaluation to compare their error performance, decoding complexity and latency. Our research shows that CC-LDPC has the advantages in terms of high reliability, low complexity and low latency. Finally, we propose some open research problems and solving ideas for CC-LDPC application in 6G communication.

## Design of Protograph-Based Quasi-Cyclic Spatially Coupled Ldpc Codes

- **Status**: ✅
- **Reason**: QC-SC-LDPC binary code construction: girth-6 protographs, larger-girth QC lifting, syndrome former bound — portable code-design technique (E)
- **ID**: ieee:9124803
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Shuoshuo Wang, Zhanji Wu, Qihao Wu
- **PDF**: https://ieeexplore.ieee.org/document/9124803
- **Abstract**: In this paper, we deal with time-varing quasi-cyclic (QC) spatially-coupled (SC) low-density parity-check (LDPC) codes by lifting the coupled protographs. The construction method of girth-6 protographs for any code rate is proposed. We provide a theoretical lower bound on the syndrome former constraint length under condition of the protographs without 4-cycles in their Tanner graphs. Then we use periodic QC lifting method to search the QC-SC-LDPC matrices with larger girth based on the protographs. The minimum dimension size of QC-SC-LDPC codes is given to count the girth of QC-SC-LDPC codes with a semi- infinite binary-check matrix structure. The performance of such constructed codes with lower complexity and delay is superior to the LDPC block codes.

## Coding Techniques for 5G Networks: A Review

- **Status**: ❌
- **Reason**: 5G 코딩 기법 리뷰(LDPC/Polar) — 서베이, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:9137797
- **Type**: conference
- **Published**: 3-4 April 
- **Authors**: Mrinmayi V Patil, Sanjay Pawar, Zia Saquib
- **PDF**: https://ieeexplore.ieee.org/document/9137797
- **Abstract**: In todays world, the demand for Mobile Internet is increasing and the Internet of Things poses a challenging requirement for 5G wireless communications. Turbo Codes and Tail Bitting Convolution Codes (TBCC) have proven to be efficient for LTE communication. But these codes have failed to satisfy the conditions defined for 5G Communications. In 5G, we require advanced error correction techniques for channel coding. To fulfill 5G communications requirements, we use LDPC and Polar codes for error correction. In 5G NR (New Radio) LDPC codes used for the data channel and control channel Polar Codes are used. We get high Coding gain for this code. It has several features such as high throughput, low power dissipation, and low latency. We describe encoding and decoding methods of LDPC and Polar Codes. They use two types of Base matrices of 5G NR for this code. Polar codes depend on channel polarization and are the first code that has achieved Shannon channel capacity. Polar codes have wide applications in Information theory. Quasi Cyclic LDPC code, Irregular Repeat-Accumulate (IRA) code, Spatially Coupled LDPC (SP-LDPC), NBLDPC-Polar Codes described. For 5G Standard this code plays an important role in Channel Coding.

## Codeword Generation for a Combined Cryptography and LDPC Coding System

- **Status**: ❌
- **Reason**: 암호+LDPC 결합 시스템의 cyphertext 생성(보안 응용), 떼어낼 채널 ECC 디코더·구성 기법 없음
- **ID**: ieee:9198715
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Bradley Comar
- **PDF**: https://ieeexplore.ieee.org/document/9198715
- **Abstract**: This paper describes a method of generating the cyphertext for a combined cryptographic and LDPC encoding system. This combined system is used for the purpose of enhancing privacy. However, to create the cyphertext, 2 matrix inversions must occur and one of these matrices may sometimes be singular. In addition to this inversion issue, this combined system may use many more PRNG bits per message bit than the standard XORing system. Both issues are addressed here.

## On Efficient and Low-Complexity Decoding of Binary LDPC-Coded CSK Signals for GNSS Links with Increased Data Rates

- **Status**: ❌
- **Reason**: GNSS CSK 신호 복조/iterative demapping 복잡도 저감; LDPC는 베이스라인, CSK demapping에 특화돼 NAND LDPC로 이식할 새 기법 없음
- **ID**: ieee:9110196
- **Type**: conference
- **Published**: 20-23 Apri
- **Authors**: Rémi Chauvat, Axel Garcia-Pena, Matteo Paonni
- **PDF**: https://ieeexplore.ieee.org/document/9110196
- **Abstract**: GNSS with high data rate links are of interest to accommodate new needs and applications (e.g. precise positioning, authentication, reduction of TTFFD). In this context, a binary LDPC-coded CSK signal is an attractive candidate to increase data rates with a high data recovery robustness. However, such a proposal requires an increase of receiver's computational complexity with respect to receivers for current coded DSSS/BPSK GNSS links. The computational complexity required for data recovery is analysed in this article and insights on crucial technical choices are given for the reception of binary LDPC-coded CSK signals. CSK demodulation is shown to dominate the overall computational cost and the use of digital chip-matched filtering prior to demodulation is proposed to reduce this cost. In addition, iterative demapping, which is crucial to optimize the power efficiency of binary LDPC-coded CSK links is also shown to have high computational complexity. Therefore, low-complexity iterative demapping strategies are studied and simple yet efficient solutions are proposed.

## LDPC Decoding Based On Statistical Mechanics Of Spin-Glasses: A Study

- **Status**: ❌
- **Reason**: Spin-glass/statistical-mechanics review of LDPC decoding; no concrete new decoder/HW/construction
- **ID**: ieee:9092331
- **Type**: conference
- **Published**: 16-19 Apri
- **Authors**: Z. JADDI, A. AIT MADI, M. BENBRAHIM
- **PDF**: https://ieeexplore.ieee.org/document/9092331
- **Abstract**: In this paper, the LDPC (Low Density Parity Check Codes) decoding algorithm has been investigated using statistical mechanics properties. The main advantage of LDPC codes is their performance that works in near Shannon limit, and the ability to use iterative decoding algorithms. In 1989 N. Sourlas showed that error-correcting codes can be considered as Spin-Glass systems thus making it possible to model LDPC codes as an Ising model, opening the way for information theorists to solve coding problems with the power of statistical mechanics. According to N. Sourlas, the decoding problem can be solved by finding the ground state of the corresponding spin-system Hamiltonian. The main goal of this paper is to review as simple as possible the statistical properties of LDPC codes, and how it is used especially facing the decoding problem.

## Investigation of Harmonic Frequency Multiplication on Transmitted Data through Pulse Shaping for 6G Communication

- **Status**: ❌
- **Reason**: 6G 펄스셰이핑/주파수 체배 RF 연구, LDPC/디코더/ECC 기법 없음
- **ID**: ieee:9102565
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: Özgün Ersoy, Asaf Behzat Şahin
- **PDF**: https://ieeexplore.ieee.org/document/9102565
- **Abstract**: Communication shifts to high carrier frequencies with increasing data rates and the need for quality transmission. In this context, studies are carried out at 28 GHz in 5G technology, and communication systems in the frequency band of 60–70 GHz are studied. In addition, communication systems in the frequency band of 140–180 GHz are planned for 6G technology. However, amplifier active balanced mixers cannot be found at high frequencies in existing technology, frequency multiplication via Schottky diode only viable solution for these ahead of the technology curve frequency bands. We investigated the effects of frequency upconversion through harmonic frequency multiplication on the transmitted digital data pulse shape and data rate. These studies were simulated in the MATLAB simulation environment and corroborated in our experimental 50–75 GHz carrier wireless communication system. We showed that through pulse shaping the transmitted data eye diagram SNR can be improved by 3 dB or data rate can be increased by 20% alternatively.

## Exploiting Asymmetric Errors for LDPC Decoding Optimization on 3D NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D NAND LDPC 디코딩 최적화, 비대칭 에러 활용 센싱 레벨 배치로 read latency 감소. NAND 직접(A) 핵심.
- **ID**: ieee:8936476
- **Type**: journal
- **Published**: 1 April 20
- **Authors**: Qiao Li, Liang Shi, Yufei Cui +1
- **PDF**: https://ieeexplore.ieee.org/document/8936476
- **Abstract**: By stacking layers vertically, the adoption of 3D NAND has significantly increased the capacity for storage systems. The complex structure of 3D NAND introduces more errors than planer flash. To address the reliability issue, low-density parity-check (LDPC) code with a strong error correction capability is now widely applied on 3D NAND flash memory. However, LDPC has long decoding latency when the raw bit error rates (RBER) are high. This is because it needs fine-grained soft sensing between voltage states to iteratively decode the raw data. Multiple sensing voltages are applied on flash cell array to gain necessary information for decoding. In this article, a new sensing level placement scheme with reduced number of sensing levels is proposed. The basic idea for the placement scheme is motivated by three asymmetric error characteristics of flash memory: the asymmetric errors between different states, the asymmetric errors caused by voltage left-shifts and right-shifts and asymmetric errors among layers in a 3D NAND flash block. With awareness of these three types of error characteristics, reduced number of sensing levels are placed to achieve reduced read latency for LDPC decoding while maintaining the error correction capability of LDPC. Experiment analysis shows that the proposed scheme achieves significant performance improvement.
