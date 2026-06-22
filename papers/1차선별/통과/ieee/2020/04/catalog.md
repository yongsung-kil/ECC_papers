# IEEE Xplore — 2020-04 (1차선별 통과)


## A Threshold-Based Min-Sum Algorithm to Lower the Error Floors of Quantized LDPC Decoders

- **Status**: ✅
- **Reason**: 양자화 디코더 error floor를 낮추는 새 threshold-based min-sum 변형 제안 — 이식 가능 디코더(C), NAND LDPC 직접 적용 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8970554
- **Type**: journal
- **Published**: April 2020
- **Authors**: Homayoon Hatami, David G. M. Mitchell, Daniel J. Costello +1
- **PDF**: https://ieeexplore.ieee.org/document/8970554
- **Abstract**: For decoding low-density parity-check (LDPC) codes, the attenuated min-sum algorithm (AMSA) and the offset min-sum algorithm (OMSA) can outperform the conventional min-sum algorithm (MSA) at low signal-to-noise-ratios (SNRs), i.e., in the “waterfall region” of the bit error rate curve. This paper demonstrates that, for quantized decoders, MSA actually outperforms AMSA and OMSA in the “error floor” region, and that all three algorithms suffer from a relatively high error floor. This motivates the introduction of a modified MSA that is designed to outperform MSA, AMSA, and OMSA across all SNRs. The new algorithm is based on the assumption that trapping sets are the major cause of the error floor for quantized LDPC decoders. A performance estimation tool based on trapping sets is used to verify the effectiveness of the new algorithm and also to guide parameter selection. We also show that the implementation complexity of the new algorithm is only slightly higher than that of AMSA or OMSA. Finally, the simulated performance of the new algorithm, using several classes of LDPC codes (including spatially coupled LDPC codes), is shown to outperform MSA, AMSA, and OMSA across all SNRs.

## Using Error Modes Aware LDPC to Improve Decoding Performance of 3-D TLC NAND Flash

- **Status**: ✅
- **Reason**: 3D TLC NAND에 직접 적용한 error-mode 인식 LDPC LLR 최적화로 디코딩 지연/BER 개선 (카테고리 A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8634908
- **Type**: journal
- **Published**: April 2020
- **Authors**: Fei Wu, Meng Zhang, Yajuan Du +5
- **PDF**: https://ieeexplore.ieee.org/document/8634908
- **Abstract**: 3-D triple-level cell (3-D TLC) NAND flash has high storage density and capacity, but degrading data reliability due to high raw bit error rates induced by a certain number of program/erase cycles. To guarantee data reliability, low-density parity-check (LDPC) codes are selected as the error correction codes in modern flash memories because of strong error correction capability. However, directly adopting LDPC codes induces high decoding latency due to iterative updating of log-likelihood ratio (LLR) information in the decoding process. Increasing LLR information accuracy can greatly improve decoding performance. In this paper, we propose EMAL: using error modes aware LDPC codes for further enhancing the decoding performance of 3-D TLC NAND flash. We first obtain 3-D TLC error modes based on an FPGA testing platform, and then exploit the error modes to optimize LLR information and enable the decoding to converge at a high speed. The simulation results show that the decoding performance is significantly improved, resulting in reduced bit error rates and decoding latency.

## A 75-Gb/s/mm2 and Energy-Efficient LDPC Decoder Based on a Reduced Complexity Second Minimum Approximation Min-Sum Algorithm

- **Status**: ✅
- **Reason**: 신규 SAMS(second minimum approximation min-sum) 알고리즘 + 라우팅 절감 VLSI 디코더 → 이식 가능 디코더/HW (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8935206
- **Type**: journal
- **Published**: April 2020
- **Authors**: Henry Lopez, Hsun-Wei Chan, Kang-Lun Chiu +2
- **PDF**: https://ieeexplore.ieee.org/document/8935206
- **Abstract**: This article presents a high-throughput and low-routing complexity low-density parity check (LDPC) decoder design based on a novel second minimum approximation min-sum (SAMS) algorithm. The routing congestion is mitigated by reducing the required interconnections in the critical path of the routing network. The implementation and postlayout results with 28-nm 1P9M CMOS process show that the proposed design can achieve a throughput of 10.5 Gb/s for a millimeter-wave 60-GHz baseband system while satisfying the low bit error rate (BER) requirements (10-7). The proposed design reduces the wiring in the routing network by 21% and improves the area by 12% compared to the conventional min-sum (MS) and normalized MS (NMS) algorithm. Additional hardware optimizations are obtained by considering the internal message passing resolution based on the BER and signal-to-noise ratio (SNR) requirements for a practical baseband system. The power consumption is efficiently reduced by the employment of a shared address generator that exploits the degree of parallelism to reduce the switching activity on a group of memory elements. The LDPC decoder is implemented with a core area of 0.14 mm2, power consumption of 81 mW at 312.5 MHz, and the area and power efficiency of 75 Gb/s/mm2 and 10.2 pJ/bit, respectively.

## Failure Analysis of the Interval-Passing Algorithm for Compressed Sensing

- **Status**: ✅
- **Reason**: compressed sensing IPA 실패셋 분석이나 array LDPC 패리티검사행렬 기반 trapping/termatiko set·4-cycle 회피·minimum distance bound는 바이너리 LDPC 코드설계로 이식 가능 (E, 애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8968331
- **Type**: journal
- **Published**: April 2020
- **Authors**: Yauhen Yakimenka, Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/8968331
- **Abstract**: In this work, we perform a complete failure analysis of the interval-passing algorithm (IPA) for compressed sensing. The IPA is an efficient iterative algorithm for reconstructing a k-sparse nonnegative n-dimensional real signal x from a small number of linear measurements y . In particular, we show that the IPA fails to recover x from y if and only if it fails to recover a corresponding binary vector of the same support, and also that only positions of nonzero values in the measurement matrix are of importance to the success of recovery. Based on this observation, we introduce termatiko sets and show that the IPA fails to fully recover x if and only if the support of x contains a nonempty termatiko set, thus giving a complete (graph-theoretic) description of the failing sets of the IPA. Two heuristics to locate small-size termatiko sets are presented. For binary column-regular measurement matrices with no 4-cycles, we provide a lower bound on the termatiko distance, defined as the smallest size of a nonempty termatiko set. For measurement matrices constructed from the parity-check matrices of array low-density parity-check codes, upper bounds on the termatiko distance equal to half the best known upper bound on the minimum distance are provided for column-weight at most 7, while for column-weight 3, the exact termatiko distance and its corresponding multiplicity are provided. Next, we show that adding redundant rows to the measurement matrix does not create new termatiko sets, but rather potentially removes termatiko sets and thus improves performance. An algorithm is provided to efficiently search for such redundant rows. Finally, we present numerical results for different specific measurement matrices and also for protograph-based ensembles of measurement matrices, as well as simulation results of IPA performance, showing the influence of small-size termatiko sets.

## Edge-Coloring Technique to Analyze Elementary Trapping Sets of Spatially-Coupled LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: SC-LDPC의 elementary trapping set을 edge-coloring으로 분석·회피하는 신규 코드설계 기법, 바이너리 protograph (카테고리 E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8943947
- **Type**: journal
- **Published**: April 2020
- **Authors**: Mohammad-Reza Sadeghi, Farzane Amirzade
- **PDF**: https://ieeexplore.ieee.org/document/8943947
- **Abstract**: In this letter, for the first time, an edge-coloring technique is proposed to characterize a certain elementary trapping set (ETS) and to obtain sufficient conditions to avoid small ETSs from occurrence in the Tanner graph of SC-LDPC convolutional codes. This technique is applicable to all protograph-based LDPC codes with different girths whose protographs are single-edge, that is, the entries of their base matrices are 0, 1. To further demonstrate the effectiveness of our proposed technique, we apply it to Time-Invariant SC-LDPC-CCs with girths 6 and 8 and column weights up to 5.

## Syndrome-Coupled Rate-Compatible Error-Correcting Codes: Theory and Application

- **Status**: ✅
- **Reason**: 코셋·신드롬 기반 rate-compatible LDPC/BCH 신규 구성을 MLC 플래시에 적용 평가, 바이너리 (B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8957447
- **Type**: journal
- **Published**: April 2020
- **Authors**: Pengfei Huang, Yi Liu, Xiaojie Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/8957447
- **Abstract**: Rate-compatible error-correcting codes (ECCs), which consist of a set of extended codes, are of practical interest in both wireless communications and data storage. In this work, we first study the lower bounds for rate-compatible ECCs, thus proving the existence of good rate-compatible codes. Then, we propose a general framework for constructing rate-compatible ECCs based on cosets and syndromes of a set of nested linear codes. We evaluate our construction from two points of view. From a combinatorial perspective, we show that we can construct rate-compatible codes with increasing minimum distances, and we discuss decoding algorithms and correctable patterns of errors and erasures. From a probabilistic point of view, we prove that we are able to construct capacity-achieving rate-compatible codes, generalizing a recent construction of capacity-achieving rate-compatible polar codes. Applications of rate-compatible codes to data storage are considered. We design two-level rate-compatible codes based on Bose-Chaudhuri-Hocquenghem (BCH) and low-density parity-check (LDPC) codes which are two popular codes widely used in the data storage industry, and then we evaluate the performance of these codes in multi-level cell (MLC) flash memories. We also examine code performance on binary and $q$ -ary symmetric channels. Finally, we briefly discuss two variations of our main construction and their relative performance.

## Design of Protograph-Based Quasi-Cyclic Spatially Coupled Ldpc Codes

- **Status**: ✅
- **Reason**: QC-SC-LDPC binary code construction: girth-6 protographs, larger-girth QC lifting, syndrome former bound — portable code-design technique (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9124803
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Shuoshuo Wang, Zhanji Wu, Qihao Wu
- **PDF**: https://ieeexplore.ieee.org/document/9124803
- **Abstract**: In this paper, we deal with time-varing quasi-cyclic (QC) spatially-coupled (SC) low-density parity-check (LDPC) codes by lifting the coupled protographs. The construction method of girth-6 protographs for any code rate is proposed. We provide a theoretical lower bound on the syndrome former constraint length under condition of the protographs without 4-cycles in their Tanner graphs. Then we use periodic QC lifting method to search the QC-SC-LDPC matrices with larger girth based on the protographs. The minimum dimension size of QC-SC-LDPC codes is given to count the girth of QC-SC-LDPC codes with a semi- infinite binary-check matrix structure. The performance of such constructed codes with lower complexity and delay is superior to the LDPC block codes.

## Exploiting Asymmetric Errors for LDPC Decoding Optimization on 3D NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D NAND LDPC 디코딩 최적화, 비대칭 에러 활용 센싱 레벨 배치로 read latency 감소. NAND 직접(A) 핵심.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8936476
- **Type**: journal
- **Published**: 1 April 20
- **Authors**: Qiao Li, Liang Shi, Yufei Cui +1
- **PDF**: https://ieeexplore.ieee.org/document/8936476
- **Abstract**: By stacking layers vertically, the adoption of 3D NAND has significantly increased the capacity for storage systems. The complex structure of 3D NAND introduces more errors than planer flash. To address the reliability issue, low-density parity-check (LDPC) code with a strong error correction capability is now widely applied on 3D NAND flash memory. However, LDPC has long decoding latency when the raw bit error rates (RBER) are high. This is because it needs fine-grained soft sensing between voltage states to iteratively decode the raw data. Multiple sensing voltages are applied on flash cell array to gain necessary information for decoding. In this article, a new sensing level placement scheme with reduced number of sensing levels is proposed. The basic idea for the placement scheme is motivated by three asymmetric error characteristics of flash memory: the asymmetric errors between different states, the asymmetric errors caused by voltage left-shifts and right-shifts and asymmetric errors among layers in a 3D NAND flash block. With awareness of these three types of error characteristics, reduced number of sensing levels are placed to achieve reduced read latency for LDPC decoding while maintaining the error correction capability of LDPC. Experiment analysis shows that the proposed scheme achieves significant performance improvement.
