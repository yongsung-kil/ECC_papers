# IEEE Xplore — 2026-04


## A 3.3 Gb/s/mm2 Area-Efficient Non-Binary LDPC Decoder Using Column-Layered Processing

- **Status**: ❌
- **Reason**: [기준개정:비이진제외] NB-LDPC 디코더 HW(trellis min-max, column-layered, 28nm CMOS), 스토리지용으로 명시 — D/E 이식 가능
- **ID**: ieee:11251477
- **Type**: journal
- **Published**: April 2026
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/11251477
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes are a prominent class of error-correction codes, offering superior error-correcting performance compared to their binary counterparts. However, previous NB-LDPC decoders suffer from high processing complexity and significant memory overhead when supporting high-order Galois fields and long codeword lengths. To address these challenges, the proposed decoder leverages the trellis min-max algorithm and adopts a column-layered decoding schedule with on-the-fly message computation to reduce memory requirements. Additionally, the proposed column-layered algorithm shares up-to-date information among columns, enhancing the convergence speed of the baseline design. Considering the structure of high-rate NB-LDPC codes, we introduce multi-column processing with an optimized banked memory architecture while minimizing parallel processing overhead through submodule optimization. Fabricated using a 28-nm CMOS technology, the prototype 4KB 0.9-rate decoder achieves a 1.42-fold improvement in area efficiency compared to state-of-the-art designs. While the proposed design is motivated by the requirements of storage applications, its modular organization and scalable parallelism also allow adaptation to diverse domains such as wireless and optical communications.

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

## BiBiEQ: Bivariate Bicycle Codes on Erasure Qubits

- **Status**: ❌
- **Reason**: Bivariate Bicycle qLDPC + erasure qubit 양자EC 프레임워크 — 제외 카테고리(양자LDPC), 이식 가능한 고전 디코더/HW 없음
- **ID**: ieee:11500360
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Ameya S. Bhave, Navnil Choudhury, Andrew Nemec +1
- **PDF**: https://ieeexplore.ieee.org/document/11500360
- **Abstract**: Erasure qubits reduce overhead in fault-tolerant quantum error correction (QEC) by converting dominant faults into detectable errors known as erasures. They have demonstrated notable improvements in thresholds and scaling in surface and Floquet code memories. In this work, we use erasure qubits on Bivariate Bicycle (BB) codes from the quantum low-density parity-check (QLDPC) regime. Owing to their sparse structure and favorable rate-distance trade-offs, BB codes are practical candidates for QEC. We introduce BiBiEQ, a novel framework that compiles a given BB code into an erasure-aware memory circuit $C_{E}$. This erasure circuit $C_{E}$ comprises erasure checks (ECs), resets, and erasures spread over a user-specified erasure check schedule (2EC, 4EC). BiBiEQ converts this erasure circuit $C_{E}$ into the stabilizer circuit $C$ for general-purpose decoding. BiBiEQ provides two engines for this conversion, BiBiEQ-Exact and BiBiEQ-Approx. BiBiEQ-Exact preserves the joint-erasure correlations and serves as our accuracy benchmark, while BiBiEQ-Approx uses an independence approximation to accelerate large sweeps and expose accuracy-throughput tradeoffs. Using BiBiEQ, we decode the stabilizer circuits to get a per-round logical error rate (LER) for the BB codes and quantify the effect of the EC schedules on the correctable operating region below the pseudo-threshold. The $4 E C$ schedule keeps the accuracy of both engines close to one another, making BiBiEQ-Approx a reliable proxy for BiBiEQ-Exact for faster sweeps. Below the pseudo-threshold, the code distance ($d$) hop from $d: 6 \rightarrow 10$ yields a drop in LER by $\approx 10-17 \times$ larger than $d: 10 \rightarrow 12$, showing that most gains are realized by $d=10$.

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
