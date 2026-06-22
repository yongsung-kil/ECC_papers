# IEEE Xplore — 2026-04 (1차선별 통과)


## Throughput-Optimized Multi-Rate LDPC Codes for Satellite Communication Systems With Restricted Decoder Complexity

- **Status**: ✅
- **Reason**: 처리율 최적화 다중률 LDPC 부호설계(프로토매트릭스 탐색) — 코드설계 이식(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11202618
- **Type**: journal
- **Published**: April 2026
- **Authors**: Xing Pan, Zhao Chen, Yukui Pei +1
- **PDF**: https://ieeexplore.ieee.org/document/11202618
- **Abstract**: Multi-rate low-density parity-check (LDPC) codes are widely used in satellite communication (SatCom) systems due to their outstanding performance and adaptable code rates. However, their hardware decoder implementations typically require high hardware resources and many decoding iterations, which pose challenges for high-throughput applications in resource-constrained, high-data-rate SatCom scenarios. To this end, the design of throughput-optimized multi-rate LDPC codes is investigated, aiming to tackle the decoder implementation problem from the perspective of practical code design. Specifically, a multi-rate weighted normalized throughput metric is introduced, which considers two key factors, i.e., the number of non-zero elements in the parity-check matrix and the required decoding iterations. Then, the throughput-optimized multi-rate code design problem is formulated to maximize the proposed metric under given decoding threshold constraints, which is later solved using a protomatrix search method based on the differential evolution (DE) algorithm. Finally, three multi-rate LDPC codes are optimized for scenes with different code rate usage frequencies. Their performance is extensively evaluated both theoretically and numerically. Results demonstrate that the proposed codes outperform other similar LDPC codes in the literature, showing a throughput increase of 20% to 30% under the same hardware resource consumption.

## SiDTBF: Merging Soft Information With Dynamic Threshold Bit Flipping LDPC Decoding for 3-D NAND flash memory

- **Status**: ✅
- **Reason**: 3D NAND 플래시 LDPC 소프트정보+동적임계 BF 디코딩 — NAND 직접+디코더(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11154047
- **Type**: journal
- **Published**: April 2026
- **Authors**: Yangyi Li, Meng Zhang, Wei Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11154047
- **Abstract**: Through stacking and multibit technology, 3-D flash memory enhances storage capacity and density; nevertheless, the reduction in noise margin results in an increase in raw bit error rate (RBER) and a decrease in data reliability. Low-density parity-check (LDPC) codes are widely used in flash memory for improving data reliability because of its strong error correction capability. In the early stages of 3-D flash memory use, the RBER is low, and hard decision decoding (e.g., bit flipping (BF) decoding) is generally invoked for error correction. Existing LDPC codes with dynamic threshold BF (DTBF) decoding algorithms cannot correct bit errors when the gradually increasing RBER exceeds its error correction threshold, resulting in an increase in decoding latency. To enhance error correction capability and reduce decoding latency, this article proposes SiDTBF: merging soft information with DTBF LDPC decoding for 3-Dnand flash memory. First, the read reference voltage of various interval lengths is applied in accordance with the threshold voltage distribution drift characteristics of the 3-D flash memory cell to get the decoding soft information of each bit. Second, the strong and weak bits are distinguished using the soft information. In contrast to weak bits, which are more likely to be erroneous, strong bits are more likely to be correct. Finally, all the strong and weak bits are input as initial values for bit-flip iterative decoding. Using the column weight of the parity-check matrix, the threshold for the number of flipped weak bits is determined in the first decoding iteration process. The portion of the weak bits that exceeds the threshold is flipped. In the ensuing iteration phase, the DTBF decoding algorithm is used. SiDTBF improves decoding error correction performance by fusing each bit’s soft information with the DTBF algorithm during the decoding phase. Simulation results show that compared with the current DTBF, SiDTBF significantly improves BF decoding error correction capability and reduces decoding latency.

## Design of Protograph-Based LDPC Codes for Rate-Diverse Multiple Access

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC 부호설계 EXIT 해석 — 코드설계 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11218994
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jingru Xue, Lichao Zhou, Peng Kang +3
- **PDF**: https://ieeexplore.ieee.org/document/11218994
- **Abstract**: In this paper, we investigate the performance of protograph-based low-density parity-check (LDPC) codes for rate-diverse two-user Gaussian multiple access channel (GMAC). Considering the characteristic of rate-diverse GMAC, we first analyze the message passing model of the coding system. Then, we derive a rate-diverse joint protograph-based extrinsic information transfer (RDJP-EXIT) chart to analyze the rate-diverse joint user messages decoding (RDJD) behavior. Guided by the RDJP-EXIT, we design the protograph base matrices of different channel conditions for two users, respectively. Simulation results show that the proposed protograph-based LDPC codes of low decoding threshold significantly outperform the conventional AR4JA codes and irregular LDPC codes in GMAC channels, which are also close to optimal in terms of sum rate.

## Design and Analysis of Two-Layer Coding Scheme for DNA-Based Data Storage

- **Status**: ✅
- **Reason**: DNA 스토리지 ECC, BCH+LDPC 연접·유한길이 redundancy 최적화 — B/E 코드 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11316539
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jiayao Zhang, Shancheng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/11316539
- **Abstract**: DNA-based data storage has emerged as a compelling alternative to traditional media due to its ultra-high information density and long-term stability. However, the high read cost caused by the error-prone synthesis, storage, and sequencing processes remains a major bottleneck for practical deployment. To address this challenge, this paper proposes a read-cost-efficient coding framework that enhances reliability without increasing total redundancy. First, a novel two-layer intra-oligo coding scheme based on Bose–Chaudhuri–Hocquenghem (BCH) codes is presented, where index bits and data bits are respectively protected to mitigate base-level errors. Second, a semi-analytical optimization method based on the normal approximation of the finite-length coding rate is developed to allocate redundancy between index and data bits optimally under a fixed total code rate. The inter-oligo protection is further achieved through low-density parity-check (LDPC) codes to combat sequence-level errors. We then present extensive analytical and numerical results to show the effectiveness of the proposed analysis. Finally, we present numerical results to demonstrate that the concatenated code based on the optimized two-layer coding scheme significantly outperforms the concatenated code based on the single-layer coding scheme in terms of frame error rate (FER) under the same sequencing depth and total redundancy. These results underscore the advantages of the two-layer coding scheme and the optimization method for DNA-based data storage systems.

## FPGA Implementation of High-Speed LDPC Decoder with Cross-Layer Scheduling for CV-QKD

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더 HW, layered 스케줄링·메모리 충돌 해소 — D 이식 가능 (CV-QKD는 응용일 뿐)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11500286
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Hao Cheng, Weicheng Yu, Yong Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/11500286
- **Abstract**: This paper addresses the high-throughput requirements of information reconciliation in continuous-variable quantum key distribution (CV-QKD) systems by proposing an FPGA-based quasi-cyclic low-density parity-check (QC-LDPC) decoder implementation utilizing cross-layer scheduling. Through a preprocessing approach involving base matrix row reordering and data merging, the scheme effectively resolves memory access conflicts in layered decoding, enabling conflict-free parallel processing. Operating at 250 MHz, the decoder achieves a throughput of 100.5 Mbps, representing a 20% improvement over conventional approaches while maintaining equivalent frame error rate performance.

## FPGA and ASIC Implementation of a 12×24 Parity-Check Matrix Based LDPC Decoder

- **Status**: ✅
- **Reason**: Min-sum LDPC 디코더의 FPGA/ASIC RTL 구현(타이밍·전력·면적)으로 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11542085
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Rayala Sai Kumar, Sreehari K N
- **PDF**: https://ieeexplore.ieee.org/document/11542085
- **Abstract**: Low density Parity Check codes are extensively utilized in modern communication systems because they offer error correction performance that approaches the Shannon limit. This work presents the design RTL implementation synthesis & analysis of a 24,12 LDPC Encoder to Decoder Architecture Using Min Sum decoding algorithm. The system includes an LDPC encoder error signal to channel Log Likelihood Ratio LLR generator and iterative LDPC decoder suitable for ASIC and FPGA platforms. The complete design is implemented in synthesizable Verilog and evaluated using Cadence Genus for timing, power and area analysis. Results show that the decoder successfully recovers all transmitted Wi-Fi test patterns using single bit and double bit errors while achieving positive slack in Static Timing Analysis and maintaining low dynamic power consumption. The architecture is efficient for low power wireless applications including Wi-Fi and 5G error correcting systems.

## Exploiting Variable-Dimensional LDPC Coding to Improve NAND Flash Memory System Performance

- **Status**: ✅
- **Reason**: NAND 플래시 메모리용 가변차원 LDPC 코딩(VDLDPC, 2D LDPC) — 행·열 분리 인코딩/디코딩으로 읽기 지연 감소, 직접 A 카테고리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11539595
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Meng Zhang, Wei Li, Yangyi Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11539595
- **Abstract**: Solid state drives (SSDs) based on NAND flash technology are steadily gaining popularity and mass market adoption due to their increased storage capacity and density. However, because of the more bits in each cell and the reduced cell spacing, they are experiencing a decline in reliability. The most eﬃcient way to ensure reliability of data is to use low-density parity-check (LDPC) codes. Nevertheless, using a hybrid decoding technique for LDPC codes results in a significant decoding latency, which exacerbates performance issues. In this paper, we propose a variable-dimensional LDPC coding scheme, called VDLDPC, to reduce the high decoding latency and thus improve read performance of NAND flash memory on hot read data. One of the crucial designs in the VDLDPC scheme is the two-dimensional LDPC (TD-LDPC) algorithm. TD-LDPC implements row and column encoding separately when writing data to the flash memory by using sub-LDPC codes. Errors in the data arise after a period of retention. When the data is read out, TD-LDPC performs row and column decoding using sub-LDPC codes, and the column decoding result can be re-decoded as a new round of row decoding input. Simulation results show that the proposed VDLDPC scheme has the advantage in decoding latency and reduces the flash memory read response time by up to 12.0% (5.8% on average across all workloads) compared to the current LDPC code scheme. The proposed VDLDPC scheme ensures reliability while improving NAND flash system read performance on hot read data.

## SSALDPC: A Syndrome-Sum Based Adaptive LDPC Decoding Scheme for NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D NAND 플래시 메모리용 syndrome-sum 기반 적응형 LDPC 디코딩(SSALDPC) — read-retry 감소 및 디코딩 지연 최적화, 직접 A/C 카테고리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11539179
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Lanlan Cui, Fei Wu, Yunlong He +4
- **PDF**: https://ieeexplore.ieee.org/document/11539179
- **Abstract**: The continuous increase in storage density for 3D NAND flash memory, driven by multi-layer stacking and multilevel cell technology, leads to a significant overlap and shift in the threshold voltage distributions. This phenomenon significantly elevates the raw bit error rate (RBER) and poses serious challenges to data reliability. Although solutions based on low-density parity-check (LDPC) codes and read-retry schemes have become the standard approach to mitigate high RBER, the latency introduced by repeated read operations considerably degrades system read performance. This paper proposes a syndrome-sum based adaptive LDPC decoding scheme, named SSALDPC. After an initial hard decision decoding failure, our scheme utilizes the real-time syndrome sum (SS)—generated during the decoding process—to assess the severity of errors. Based on this assessment, it adaptively selects the most appropriate subsequent decoding strategy from three modes: EfficiencyMode (E-Mode), Balance-Mode (B-Mode), or Performance-Mode (P-Mode). Experimental results demonstrate that the proposed SSALDPC scheme reduces the number of read-retry operations and decreases decoding latency under various RBER conditions, while maintaining high error correction capability.

## An Intelligent and Optimized Reconciliation Technique for Enhanced Secret Key Rates in Quantum Key Distribution

- **Status**: ✅
- **Reason**: QKD 조정용이나 경량 신경 BP 디코더 + LLR 캘리브레이션 기법이 고전 LDPC 디코딩에 이식 가능(C) — Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11546488
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Upama Rajan M. N., Reema Mathew A, Shamya A. +3
- **PDF**: https://ieeexplore.ieee.org/document/11546488
- **Abstract**: Quantum key distribution (QKD) is a secure communication technique that uses quantum mechanical principles. This method enables two trusted users to exchange a secret key or message securely by exploiting the fundamental properties of quantum mechanics. Strong long-distance secure communication is provided by QKD but its effectiveness is mainly limited by quantum bit error rate (QBER), finite-key effects, and the effectiveness of classical error-correction during information reconciliation. In this work, we proposes a neural-aided adaptive reconciliation (NAAR) framework based on artificial neural networks for QKD that integrates a lightweight neural belief propagation decoder with QBER-driven adaptive LDPC coderate selection. By lowering frame-error rate and information leakage, neural-assisted log-likelihood ratio calibration enhances belief-propagation convergence for binary symmetric channels. The result shows an improvement in secret key rates (SKR) and lower error rates over traditional LDPC-based reconciliation.
