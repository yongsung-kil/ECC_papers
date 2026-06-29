# IEEE Xplore — 2026-04


## Throughput-Optimized Multi-Rate LDPC Codes for Satellite Communication Systems With Restricted Decoder Complexity

- **Status**: ✅
- **Reason**: 처리율 최적화 다중률 LDPC 부호설계(프로토매트릭스 탐색) — 코드설계 이식(E)
- **ID**: ieee:11202618
- **Type**: journal
- **Published**: April 2026
- **Authors**: Xing Pan, Zhao Chen, Yukui Pei +1
- **PDF**: https://ieeexplore.ieee.org/document/11202618
- **Abstract**: Multi-rate low-density parity-check (LDPC) codes are widely used in satellite communication (SatCom) systems due to their outstanding performance and adaptable code rates. However, their hardware decoder implementations typically require high hardware resources and many decoding iterations, which pose challenges for high-throughput applications in resource-constrained, high-data-rate SatCom scenarios. To this end, the design of throughput-optimized multi-rate LDPC codes is investigated, aiming to tackle the decoder implementation problem from the perspective of practical code design. Specifically, a multi-rate weighted normalized throughput metric is introduced, which considers two key factors, i.e., the number of non-zero elements in the parity-check matrix and the required decoding iterations. Then, the throughput-optimized multi-rate code design problem is formulated to maximize the proposed metric under given decoding threshold constraints, which is later solved using a protomatrix search method based on the differential evolution (DE) algorithm. Finally, three multi-rate LDPC codes are optimized for scenes with different code rate usage frequencies. Their performance is extensively evaluated both theoretically and numerically. Results demonstrate that the proposed codes outperform other similar LDPC codes in the literature, showing a throughput increase of 20% to 30% under the same hardware resource consumption.

## SiDTBF: Merging Soft Information With Dynamic Threshold Bit Flipping LDPC Decoding for 3-D NAND flash memory

- **Status**: ✅
- **Reason**: 3D NAND 플래시 LDPC 소프트정보+동적임계 BF 디코딩 — NAND 직접+디코더(A/C)
- **ID**: ieee:11154047
- **Type**: journal
- **Published**: April 2026
- **Authors**: Yangyi Li, Meng Zhang, Wei Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11154047
- **Abstract**: Through stacking and multibit technology, 3-D flash memory enhances storage capacity and density; nevertheless, the reduction in noise margin results in an increase in raw bit error rate (RBER) and a decrease in data reliability. Low-density parity-check (LDPC) codes are widely used in flash memory for improving data reliability because of its strong error correction capability. In the early stages of 3-D flash memory use, the RBER is low, and hard decision decoding (e.g., bit flipping (BF) decoding) is generally invoked for error correction. Existing LDPC codes with dynamic threshold BF (DTBF) decoding algorithms cannot correct bit errors when the gradually increasing RBER exceeds its error correction threshold, resulting in an increase in decoding latency. To enhance error correction capability and reduce decoding latency, this article proposes SiDTBF: merging soft information with DTBF LDPC decoding for 3-Dnand flash memory. First, the read reference voltage of various interval lengths is applied in accordance with the threshold voltage distribution drift characteristics of the 3-D flash memory cell to get the decoding soft information of each bit. Second, the strong and weak bits are distinguished using the soft information. In contrast to weak bits, which are more likely to be erroneous, strong bits are more likely to be correct. Finally, all the strong and weak bits are input as initial values for bit-flip iterative decoding. Using the column weight of the parity-check matrix, the threshold for the number of flipped weak bits is determined in the first decoding iteration process. The portion of the weak bits that exceeds the threshold is flipped. In the ensuing iteration phase, the DTBF decoding algorithm is used. SiDTBF improves decoding error correction performance by fusing each bit’s soft information with the DTBF algorithm during the decoding phase. Simulation results show that compared with the current DTBF, SiDTBF significantly improves BF decoding error correction capability and reduces decoding latency.

## Design of Protograph-Based LDPC Codes for Rate-Diverse Multiple Access

- **Status**: ✅
- **Reason**: 프로토그래프 LDPC 부호설계 EXIT 해석 — 코드설계 이식 가능(E)
- **ID**: ieee:11218994
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jingru Xue, Lichao Zhou, Peng Kang +3
- **PDF**: https://ieeexplore.ieee.org/document/11218994
- **Abstract**: In this paper, we investigate the performance of protograph-based low-density parity-check (LDPC) codes for rate-diverse two-user Gaussian multiple access channel (GMAC). Considering the characteristic of rate-diverse GMAC, we first analyze the message passing model of the coding system. Then, we derive a rate-diverse joint protograph-based extrinsic information transfer (RDJP-EXIT) chart to analyze the rate-diverse joint user messages decoding (RDJD) behavior. Guided by the RDJP-EXIT, we design the protograph base matrices of different channel conditions for two users, respectively. Simulation results show that the proposed protograph-based LDPC codes of low decoding threshold significantly outperform the conventional AR4JA codes and irregular LDPC codes in GMAC channels, which are also close to optimal in terms of sum rate.

## A 3.3 Gb/s/mm2 Area-Efficient Non-Binary LDPC Decoder Using Column-Layered Processing

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] NB-LDPC 디코더 HW(trellis min-max, column-layered, 28nm CMOS), 스토리지용으로 명시 — D/E 이식 가능
- **ID**: ieee:11251477
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/11251477
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes are a prominent class of error-correction codes, offering superior error-correcting performance compared to their binary counterparts. However, previous NB-LDPC decoders suffer from high processing complexity and significant memory overhead when supporting high-order Galois fields and long codeword lengths. To address these challenges, the proposed decoder leverages the trellis min-max algorithm and adopts a column-layered decoding schedule with on-the-fly message computation to reduce memory requirements. Additionally, the proposed column-layered algorithm shares up-to-date information among columns, enhancing the convergence speed of the baseline design. Considering the structure of high-rate NB-LDPC codes, we introduce multi-column processing with an optimized banked memory architecture while minimizing parallel processing overhead through submodule optimization. Fabricated using a 28-nm CMOS technology, the prototype 4KB 0.9-rate decoder achieves a 1.42-fold improvement in area efficiency compared to state-of-the-art designs. While the proposed design is motivated by the requirements of storage applications, its modular organization and scalable parallelism also allow adaptation to diverse domains such as wireless and optical communications.

## Design and Analysis of Two-Layer Coding Scheme for DNA-Based Data Storage

- **Status**: ✅
- **Reason**: DNA 스토리지 ECC, BCH+LDPC 연접·유한길이 redundancy 최적화 — B/E 코드 설계 이식 가능
- **ID**: ieee:11316539
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jiayao Zhang, Shancheng Zhao
- **PDF**: https://ieeexplore.ieee.org/document/11316539
- **Abstract**: DNA-based data storage has emerged as a compelling alternative to traditional media due to its ultra-high information density and long-term stability. However, the high read cost caused by the error-prone synthesis, storage, and sequencing processes remains a major bottleneck for practical deployment. To address this challenge, this paper proposes a read-cost-efficient coding framework that enhances reliability without increasing total redundancy. First, a novel two-layer intra-oligo coding scheme based on Bose–Chaudhuri–Hocquenghem (BCH) codes is presented, where index bits and data bits are respectively protected to mitigate base-level errors. Second, a semi-analytical optimization method based on the normal approximation of the finite-length coding rate is developed to allocate redundancy between index and data bits optimally under a fixed total code rate. The inter-oligo protection is further achieved through low-density parity-check (LDPC) codes to combat sequence-level errors. We then present extensive analytical and numerical results to show the effectiveness of the proposed analysis. Finally, we present numerical results to demonstrate that the concatenated code based on the optimized two-layer coding scheme significantly outperforms the concatenated code based on the single-layer coding scheme in terms of frame error rate (FER) under the same sequencing depth and total redundancy. These results underscore the advantages of the two-layer coding scheme and the optimization method for DNA-based data storage systems.

## Learning to Decode Double Polar Codes for Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: polar 부호 JSCC 신경망 BP 디코더 — LDPC 아님, 소스코딩 결합으로 제외
- **ID**: ieee:11197026
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jian Gao, Xin Song, Xiaojun Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/11197026
- **Abstract**: In this paper, a neural belief propagation decoder of double polar codes for joint source-channel coding (JSCC) is proposed. In the decoder, a residual structure is designed to establish information interaction mechanisms at different sizes between the neural sub-decoders and within them. To compensate for the information loss caused by source compression, a charger layer is introduced. In addition, we designed an iterative training scheme and parameter-sharing mechanism to constrain the complexity of the decoder. The multi-loss is extended to JSCC for training the decoder. It constrains the distribution of latent variables, thereby guiding the ResBP to optimize in the expected direction and accelerating training convergence. Experimental results show that the proposed neural decoder outperforms the existing BP-based decoders of double polar codes.

## Random Multiplexing

- **Status**: ❌
- **Reason**: 무선 multiplexing/AMP 검출기 이론, LDPC 미언급·떼어낼 디코더/HW/코드 기법 없음
- **ID**: ieee:11369302
- **Type**: journal
- **Published**: April 2026
- **Authors**: Lei Liu, Yuhao Chi, Shunqi Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/11369302
- **Abstract**: As wireless communication applications evolve from traditional multipath environments to high-mobility scenarios like unmanned aerial vehicles, multiplexing techniques have advanced accordingly. Traditional single-carrier frequency-domain equalization (SC-FDE) and orthogonal frequency-division multiplexing (OFDM) have given way to emerging orthogonal time-frequency space (OTFS) and affine frequency-division multiplexing (AFDM). These approaches exploit specific channel structures—e.g., Toeplitz-structured multipath channel matrix for OFDM and SC-FDE or doubly selective channels for OTFS and AFDM—to diagonalize or sparsify the effective channel, thereby enabling low-complexity detection. However, their reliance on these structures significantly limits their robustness in dynamic, real-world environments. To address these challenges, this paper studies a random multiplexing technique that is decoupled from the physical channels, thereby enabling its application to arbitrary norm-bounded and spectrally convergent channel matrices. Random multiplexing achieves statistical fading-channel ergodicity for transmitted signals by constructing an equivalent input-isotropic channel matrix in the random transform domain. It guarantees the asymptotic replica MAP bit-error rate (BER) optimality of AMP-type detectors for linear systems with arbitrary norm-bounded, spectrally convergent channel matrices and signaling configurations, under the unique fixed point assumption. A low-complexity cross-domain memory AMP (CD-MAMP) detector is considered for random multiplexing systems, leveraging the sparsity of the time-domain channel and the input isotropy of the equivalent channel. Optimal power allocations are derived to minimize the replica MAP BER and maximize the replica constrained capacity of random multiplexing systems, respectively. The optimal coding principle and replica constrained-capacity optimality of CD-MAMP detector are investigated for random multiplexing systems. Additionally, the versatility of random multiplexing in diverse wireless applications is explored. Numerical results are presented to validate the theoretical findings.

## Adaptive Distributed Detection Scheme in Collaborative Multiple-Input Multiple-Output Systems

- **Status**: ❌
- **Reason**: 분산 MIMO 검출 기법, LDPC는 부수 구성요소 — 떼어낼 기법 없음
- **ID**: ieee:11207172
- **Type**: journal
- **Published**: April 2026
- **Authors**: Shunya Morimoto, Hayato Sugai, Hidekazu Murata +6
- **PDF**: https://ieeexplore.ieee.org/document/11207172
- **Abstract**: This paper proposes adaptive distributed detection schemes for terminal-collaborative multiple-input multiple-output (MIMO) systems, in which multiple wireless terminals jointly receive MIMO signals transmitted from a base station. To reduce collaboration traffic while maintaining transmission performance, an on-demand multiple detection terminals scheme is introduced, where detection terminals evaluate the reliability of their decision results and selectively request more reliable decisions from peer terminals within the collaboration group. Building on this, an on-demand adaptive multiple detection terminals (OAMDT) scheme is proposed, wherein detection terminals dynamically assume the role of helper terminals to forward their received signal waveforms when additional diversity is needed due to persistent decision errors. Both schemes employ frequency-domain iterative equalization using MMSE filtering and LDPC decoding, and utilize a residual error coefficient as a reliability metric to guide decision fusion and adaptive role assignment. Simulation results under various fading environments and SNR conditions demonstrate that while the on-demand multiple detection terminals scheme effectively reduces traffic overhead, the OAMDT scheme significantly enhances packet error rate performance with only a modest increase in collaboration traffic. The results further reveal diminishing returns in error performance when increasing the number of detection terminals, suggesting that adaptive role switching is particularly beneficial under constrained conditions such as overloaded MIMO scenarios. These findings indicate that the proposed adaptive collaboration mechanisms can enhance the efficiency and robustness of terminal-collaborated MIMO reception.

## FPGA Implementation of High-Speed LDPC Decoder with Cross-Layer Scheduling for CV-QKD

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더 HW, layered 스케줄링·메모리 충돌 해소 — D 이식 가능 (CV-QKD는 응용일 뿐)
- **ID**: ieee:11500286
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Hao Cheng, Weicheng Yu, Yong Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/11500286
- **Abstract**: This paper addresses the high-throughput requirements of information reconciliation in continuous-variable quantum key distribution (CV-QKD) systems by proposing an FPGA-based quasi-cyclic low-density parity-check (QC-LDPC) decoder implementation utilizing cross-layer scheduling. Through a preprocessing approach involving base matrix row reordering and data merging, the scheme effectively resolves memory access conflicts in layered decoding, enabling conflict-free parallel processing. Operating at 250 MHz, the decoder achieves a throughput of 100.5 Mbps, representing a 20% improvement over conventional approaches while maintaining equivalent frame error rate performance.

## BiBiEQ: Bivariate Bicycle Codes on Erasure Qubits

- **Status**: ❌
- **Reason**: Bivariate Bicycle qLDPC + erasure qubit 양자EC 프레임워크 — 제외 카테고리(양자LDPC), 이식 가능한 고전 디코더/HW 없음
- **ID**: ieee:11500360
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Ameya S. Bhave, Navnil Choudhury, Andrew Nemec +1
- **PDF**: https://ieeexplore.ieee.org/document/11500360
- **Abstract**: Erasure qubits reduce overhead in fault-tolerant quantum error correction (QEC) by converting dominant faults into detectable errors known as erasures. They have demonstrated notable improvements in thresholds and scaling in surface and Floquet code memories. In this work, we use erasure qubits on Bivariate Bicycle (BB) codes from the quantum low-density parity-check (QLDPC) regime. Owing to their sparse structure and favorable rate-distance trade-offs, BB codes are practical candidates for QEC. We introduce BiBiEQ, a novel framework that compiles a given BB code into an erasure-aware memory circuit $C_{E}$. This erasure circuit $C_{E}$ comprises erasure checks (ECs), resets, and erasures spread over a user-specified erasure check schedule (2EC, 4EC). BiBiEQ converts this erasure circuit $C_{E}$ into the stabilizer circuit $C$ for general-purpose decoding. BiBiEQ provides two engines for this conversion, BiBiEQ-Exact and BiBiEQ-Approx. BiBiEQ-Exact preserves the joint-erasure correlations and serves as our accuracy benchmark, while BiBiEQ-Approx uses an independence approximation to accelerate large sweeps and expose accuracy-throughput tradeoffs. Using BiBiEQ, we decode the stabilizer circuits to get a per-round logical error rate (LER) for the BB codes and quantify the effect of the EC schedules on the correctable operating region below the pseudo-threshold. The $4 E C$ schedule keeps the accuracy of both engines close to one another, making BiBiEQ-Approx a reliable proxy for BiBiEQ-Exact for faster sweeps. Below the pseudo-threshold, the code distance ($d$) hop from $d: 6 \rightarrow 10$ yields a drop in LER by $\approx 10-17 \times$ larger than $d: 10 \rightarrow 12$, showing that most gains are realized by $d=10$.

## FPGA and ASIC Implementation of a 12×24 Parity-Check Matrix Based LDPC Decoder

- **Status**: ✅
- **Reason**: Min-sum LDPC 디코더의 FPGA/ASIC RTL 구현(타이밍·전력·면적)으로 이식 가능 HW 아키텍처(D)
- **ID**: ieee:11542085
- **Type**: conference
- **Published**: 21-23 Apri
- **Authors**: Rayala Sai Kumar, Sreehari K N
- **PDF**: https://ieeexplore.ieee.org/document/11542085
- **Abstract**: Low density Parity Check codes are extensively utilized in modern communication systems because they offer error correction performance that approaches the Shannon limit. This work presents the design RTL implementation synthesis & analysis of a 24,12 LDPC Encoder to Decoder Architecture Using Min Sum decoding algorithm. The system includes an LDPC encoder error signal to channel Log Likelihood Ratio LLR generator and iterative LDPC decoder suitable for ASIC and FPGA platforms. The complete design is implemented in synthesizable Verilog and evaluated using Cadence Genus for timing, power and area analysis. Results show that the decoder successfully recovers all transmitted Wi-Fi test patterns using single bit and double bit errors while achieving positive slack in Static Timing Analysis and maintaining low dynamic power consumption. The architecture is efficient for low power wireless applications including Wi-Fi and 5G error correcting systems.

## Exploiting Variable-Dimensional LDPC Coding to Improve NAND Flash Memory System Performance

- **Status**: ✅
- **Reason**: NAND 플래시 메모리용 가변차원 LDPC 코딩(VDLDPC, 2D LDPC) — 행·열 분리 인코딩/디코딩으로 읽기 지연 감소, 직접 A 카테고리
- **ID**: ieee:11539595
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Meng Zhang, Wei Li, Yangyi Li +3
- **PDF**: https://ieeexplore.ieee.org/document/11539595
- **Abstract**: Solid state drives (SSDs) based on NAND flash technology are steadily gaining popularity and mass market adoption due to their increased storage capacity and density. However, because of the more bits in each cell and the reduced cell spacing, they are experiencing a decline in reliability. The most eﬃcient way to ensure reliability of data is to use low-density parity-check (LDPC) codes. Nevertheless, using a hybrid decoding technique for LDPC codes results in a significant decoding latency, which exacerbates performance issues. In this paper, we propose a variable-dimensional LDPC coding scheme, called VDLDPC, to reduce the high decoding latency and thus improve read performance of NAND flash memory on hot read data. One of the crucial designs in the VDLDPC scheme is the two-dimensional LDPC (TD-LDPC) algorithm. TD-LDPC implements row and column encoding separately when writing data to the flash memory by using sub-LDPC codes. Errors in the data arise after a period of retention. When the data is read out, TD-LDPC performs row and column decoding using sub-LDPC codes, and the column decoding result can be re-decoded as a new round of row decoding input. Simulation results show that the proposed VDLDPC scheme has the advantage in decoding latency and reduces the flash memory read response time by up to 12.0% (5.8% on average across all workloads) compared to the current LDPC code scheme. The proposed VDLDPC scheme ensures reliability while improving NAND flash system read performance on hot read data.

## SSALDPC: A Syndrome-Sum Based Adaptive LDPC Decoding Scheme for NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D NAND 플래시 메모리용 syndrome-sum 기반 적응형 LDPC 디코딩(SSALDPC) — read-retry 감소 및 디코딩 지연 최적화, 직접 A/C 카테고리
- **ID**: ieee:11539179
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Lanlan Cui, Fei Wu, Yunlong He +4
- **PDF**: https://ieeexplore.ieee.org/document/11539179
- **Abstract**: The continuous increase in storage density for 3D NAND flash memory, driven by multi-layer stacking and multilevel cell technology, leads to a significant overlap and shift in the threshold voltage distributions. This phenomenon significantly elevates the raw bit error rate (RBER) and poses serious challenges to data reliability. Although solutions based on low-density parity-check (LDPC) codes and read-retry schemes have become the standard approach to mitigate high RBER, the latency introduced by repeated read operations considerably degrades system read performance. This paper proposes a syndrome-sum based adaptive LDPC decoding scheme, named SSALDPC. After an initial hard decision decoding failure, our scheme utilizes the real-time syndrome sum (SS)—generated during the decoding process—to assess the severity of errors. Based on this assessment, it adaptively selects the most appropriate subsequent decoding strategy from three modes: EfficiencyMode (E-Mode), Balance-Mode (B-Mode), or Performance-Mode (P-Mode). Experimental results demonstrate that the proposed SSALDPC scheme reduces the number of read-retry operations and decreases decoding latency under various RBER conditions, while maintaining high error correction capability.

## Optimal Compilation of Syndrome Extraction Circuits for General Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 신드롬 추출 회로 컴파일 프레임워크 — 순수 양자 EC 회로 최적화, 고전 LDPC 설계 기법을 독립적으로 이식 불가
- **ID**: ieee:11539585
- **Type**: conference
- **Published**: 20-22 Apri
- **Authors**: Kai Zhang, Dingchao Gao, Zhaohui Yang +4
- **PDF**: https://ieeexplore.ieee.org/document/11539585
- **Abstract**: Quantum error correcting codes (QECC) are essential for constructing large-scale quantum computers that deliver faithful results. As strong competitors to the conventional surface code, quantum low-density parity-check (qLDPC) codes are emerging rapidly: they offer high encoding rates while maintaining reasonable physical-qubit connectivity requirements. Despite the existence of numerous code constructions, a notable gap persists between these designs—some of which remain purely theoretical—and their circuit-level deployment.In this work, we propose Auto-Stabilizer-Check (ASC), a universal compilation framework that generates depth-optimal syndrome extraction circuits for arbitrary qLDPC codes. ASC leverages the sparsity of parity-check matrices and exploits the commutativity of X and Z stabilizer measurement subroutines to search for optimal compilation schemes. By iteratively invoking an SMT solver, ASC returns a depth-optimal solution if a satisfying assignment is found, and a near-optimal solution in cases of solver timeouts. Notably, ASC provides the first definitive answer to one of IBM’s open problems: for all instances of bivariate bicycle (BB) code reported in their work, our compiler certifies that no depth-6 syndrome extraction circuit exists.Furthermore, by integrating ASC with an end-to-end evaluation framework—one that assesses different compilation settings under a circuit-level noise model—ASC reduces circuit depth by approximately 50% and achieves an average 7x-8x suppression of the logical error rate for general qLDPC codes, compared with as-soon-as-possible (ASAP) and coloration-based scheduling. ASC thus substantially reduces manual design overhead and demonstrates its strong potential to serve as a key component in accelerating hardware deployment of qLDPC codes.

## Attention-Aware Deep Joint Source-Channel Coding for Robust Power Grid Inspection Image Transmission

- **Status**: ❌
- **Reason**: Deep JSCC 이미지 전송 프레임워크로 LDPC는 비교 베이스라인만, 떼어낼 ECC 기법 없음
- **ID**: ieee:11544951
- **Type**: conference
- **Published**: 18-20 Apri
- **Authors**: Haifan Wang, Changzhi Han, Xiaoqiang Shi +4
- **PDF**: https://ieeexplore.ieee.org/document/11544951
- **Abstract**: The modernization of smart grids relies on unmanned aerial vehicles (UAVs) for high-voltage transmission line inspections, yet the transmission of massive high-resolution images over unstable wireless channels poses significant challenges. Traditional digital communication systems based on Shannon’s separation theorem encounter a "cliff effect" under low signal-to-noise ratios, leading to complete decoding failure and rendering them unsuitable for real-time fault detection. This paper proposes an Attention-Aware Deep Joint Source-Channel Coding (Attention-Aware Deep JSCC) framework specifically designed for power grid inspections. This approach integrates a Channel Attention Module (CAM) within the encoder, enabling dynamic identification and amplification of critical semantic features such as insulator defects while suppressing background interference. Additionally, training uses a hybrid loss function that combines MSE and LPIPS to balance pixel-level fidelity and semantic integrity in the reconstructed images. Experimental results on the CPLID dataset demonstrate that this approach effectively mitigates the cliff effect by enabling graceful degradation, achieving significantly superior reconstruction quality under low SNR conditions compared to traditional JPEG+LDPC schemes and standard JSCC baselines, substantially improving accuracy in downstream fault detection tasks.

## On Blind Recognition of BCH Codes Within a Candidate Set

- **Status**: ❌
- **Reason**: BCH 코드 블라인드 파라미터 인식 알고리즘으로 LDPC와 무관, ECC 설계·디코더 기법 아님
- **ID**: ieee:11540728
- **Type**: conference
- **Published**: 17-19 Apri
- **Authors**: Fuhao Ding, Yao Wang, Chuanke Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/11540728
- **Abstract**: In non-cooperative communications, blind recognition of channel codes is a crucial prerequisite for information acquisition and analysis. BCH codes are widely adopted in various communication systems due to their excellent error-correcting performance. However, most existing research has focused on open-set recognition scenarios, with limited attention devoted to closed-set scenarios. To address this research gap, a closed-set parameter recognition algorithm for primitive BCH codes is proposed in this paper. The algorithm sorts candidate parameters based on the space dimension of parity-check matrices. Then the average likelihood difference (LD) is introduced as the test statistic. By leveraging the distinct distribution characteristics of the test statistic under different candidate parameters, a decision threshold is set to sequentially verify each sorted candidate. The last candidate parameter that passes the verification is identified as the final recognition result. Simulation results demonstrate that the proposed algorithm can effectively and reliably achieve the recognition of primitive BCH code parameters under closed-set conditions.

## An Intelligent and Optimized Reconciliation Technique for Enhanced Secret Key Rates in Quantum Key Distribution

- **Status**: ✅
- **Reason**: QKD 조정용이나 경량 신경 BP 디코더 + LLR 캘리브레이션 기법이 고전 LDPC 디코딩에 이식 가능(C) — Phase 3 재검토
- **ID**: ieee:11546488
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Upama Rajan M. N., Reema Mathew A, Shamya A. +3
- **PDF**: https://ieeexplore.ieee.org/document/11546488
- **Abstract**: Quantum key distribution (QKD) is a secure communication technique that uses quantum mechanical principles. This method enables two trusted users to exchange a secret key or message securely by exploiting the fundamental properties of quantum mechanics. Strong long-distance secure communication is provided by QKD but its effectiveness is mainly limited by quantum bit error rate (QBER), finite-key effects, and the effectiveness of classical error-correction during information reconciliation. In this work, we proposes a neural-aided adaptive reconciliation (NAAR) framework based on artificial neural networks for QKD that integrates a lightweight neural belief propagation decoder with QBER-driven adaptive LDPC coderate selection. By lowering frame-error rate and information leakage, neural-assisted log-likelihood ratio calibration enhances belief-propagation convergence for binary symmetric channels. The result shows an improvement in secret key rates (SKR) and lower error rates over traditional LDPC-based reconciliation.
