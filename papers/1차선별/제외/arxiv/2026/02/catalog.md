# arXiv — 2026-02


## The Distance Spectrum of IEEE 802.11 Binary Convolutional Codes

- **Status**: ❌
- **Reason**: IEEE 802.11 BCC(컨볼루션 부호) 거리스펙트럼 분석, LDPC 부수 언급일 뿐 LDPC 기법 없음
- **ID**: arxiv:2602.23651v1
- **Type**: preprint
- **Published**: 2026-02-27
- **Authors**: Rethna Pulikkoonattu
- **PDF**: https://arxiv.org/pdf/2602.23651v1
- **Abstract**: Binary convolutional coding (BCC) has been a cornerstone of the IEEE 802.11 wireless LAN standard since its inception, and it remains relevant today across the full generational arc from the legacy 802.11a/g through Wi-Fi 6 (802.11ax) and into the forthcoming Wi-Fi 8 (802.11bn). Although low-density parity-check (LDPC) codes now dominate high-throughput applications, BCC is mandatory for backward compatibility and continues to serve as the default forward-error-correction scheme in bandwidth-constrained and cost-sensitive deployments: 20 MHz-only devices, Internet-of-Things nodes, and other implementations where LDPC's decoder complexity is prohibitive. Critically, BCC at rate 1/2 is the coding scheme used throughout the packet preamble in every IEEE 802.11-compliant frame, making it indispensable regardless of which data-field code is selected. Furthermore, the new Enhanced Long Range (ELR) packet format introduced in the 802.11bn/UHR amendment mandates rate-1/2 BCC for the data portion of the frame, reinforcing the continued importance of this code in next-generation deployments. The performance of BCC under Viterbi decoding is governed by the distance spectrum of the convolutional code. This note explains how to compute that spectrum exactly for the IEEE 802.11 mother code (rate 1/2, K=7, generators octal 133 / octal 171) and its three standard punctured derivatives (rates 2/3, 3/4, 5/6) obtained via rate-compatible puncturing. Union-bound BEP and FER curves are derived for AWGN with BPSK/QPSK and Gray-coded M-QAM modulation and validated against Monte Carlo simulation. Python, Julia, and C++ implementations are openly available at https://github.com/geekymode/bcc_spectrum.

## Generalized $\mathbb{Z}_p$ toric codes as qudit low-density parity-check codes

- **Status**: ❌
- **Reason**: Z_p 토릭코드 기반 qudit 양자 LDPC, 양자 EC 영역으로 제외
- **ID**: arxiv:2602.20158v1
- **Type**: preprint
- **Published**: 2026-02-23
- **Authors**: Zijian Liang, Yu-An Chen
- **PDF**: https://arxiv.org/pdf/2602.20158v1
- **Abstract**: We study two-dimensional translation-invariant CSS stabilizer codes over prime-dimensional qudits on the square lattice under twisted boundary conditions, generalizing the Kitaev $\mathbb{Z}_p$ toric code by augmenting each stabilizer with two additional qudits. Using the Laurent-polynomial formalism, we adapt the Gröbner basis to compute the logical dimension $k$ efficiently, without explicitly constructing large parity-check matrices. We then perform a systematic search over various stabilizer realizations and lattice geometries for $p\in\{3,5,7,11\}$, identifying qudit low-density parity-check codes with the optimal finite-size performance. Representative examples include $[[242,10,22]]_3$ and $[[120,6,20]]_{11}$, both achieving $k d^{2}/n=20$. Across the searched regime, the best observed $k d^{2}$ at fixed $n$ increases with $p$, with an empirical relation $k d^{2} = 0.0541 \, n^{2}\ln p + 3.84 \, n$, compatible with a Bravyi--Poulin--Terhal-type tradeoff when the interaction range grows with system size.

## Fault-tolerant interfaces for quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC fault-tolerant 인터페이스, 양자 EC 영역으로 제외
- **ID**: arxiv:2602.16948v1
- **Type**: preprint
- **Published**: 2026-02-18
- **Authors**: Matthias Christandl, Omar Fawzi, Ashutosh Goswami
- **PDF**: https://arxiv.org/pdf/2602.16948v1
- **Abstract**: The preparation of a quantum state using a noisy quantum computer (gate noise strength $δ$), will necessarily affect an O($δ$)-fraction of the qubits, no matter which protocol is used. Here, we show that fault-tolerant quantum state preparation can be achieved with constant space overhead improving on previous constructions requiring polylogarithmic overhead.   To achieve this, we add to the toolbox of fault-tolerant schemes for circuits with quantum input and output. More specifically, we construct fault-tolerant interfaces that decrease the level of protection for quantum low-density parity-check (LDPC) codes. When information is encoded in multiple code blocks, our interfaces have constant space overhead.   In our decoder construction that change the level of protection by an arbitrary amount, we circumvent bottlenecks to error pileup and overhead by gradual lowering of the level of encoding at the same time as we increase the number of blocks on which decoding is carried out simultaneously.

## Self-dual Stacked Quantum Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: self-dual 양자 LDPC 코드 구성, 양자 EC 영역으로 제외
- **ID**: arxiv:2602.15372v1
- **Type**: preprint
- **Published**: 2026-02-17
- **Authors**: Ze-Chuan Liu, Chong-Yuan Xu, Yong Xu
- **PDF**: https://arxiv.org/pdf/2602.15372v1
- **Abstract**: Quantum low-density parity-check (qLDPC) codes are promising candidates for fault-tolerant quantum computation due to their high encoding rates and distances. However, implementing logical operations using qLDPC codes presents significant challenges. Previous research has demonstrated that self-dual qLDPC codes facilitate the implementation of transversal Clifford gates. Here we introduce a method for constructing self-dual qLDPC codes by stacking non-self-dual qLDPC codes. Leveraging this methodology, we develop double-chain bicycle codes, double-layer bivariate bicycle (BB) codes, double-layer twisted BB codes, and double-layer reflection codes, many of which exhibit favorable code parameters. Additionally, we conduct numerical calculations to assess the performance of these codes as quantum memory under the circuit-level noise model, revealing that the logical failure rate can be significantly reduced with high pseudo-thresholds.

## Non-Abelian Quantum Low-Density Parity Check Codes and Non-Clifford Operations from Gauging Logical Gates via Measurements

- **Status**: ❌
- **Reason**: non-Abelian 양자 LDPC 게이징 구성, 양자 EC 영역으로 제외
- **ID**: arxiv:2602.12228v1
- **Type**: preprint
- **Published**: 2026-02-12
- **Authors**: Maine Christos, Chiu Fan Bowen Lo, Vedika Khemani +1
- **PDF**: https://arxiv.org/pdf/2602.12228v1
- **Abstract**: In this work, we introduce constructions for non-Abelian qLDPC codes obtained by gauging transversal Clifford gates using measurement and feedback. In particular, we identify two qualitatively different approaches to gauging qLDPC codes to obtain their non-Abelian counterparts. The first approach applies to codes that exhibit a generalized form of Poincaré duality and leads to a qLDPC non-Abelian Clifford stabilizer code, whose stabilizers are reminiscent of the action of a Type-III twisted quantum double. Our second approach applies to general qLDPC codes, and uses a graph of ancilla qubits which may be tailored to properties of the input codes to gauge a single transversal gate. For both constructions, the resulting gauged codes are shown to have properties analogous to 2D non-Abelian topological order -- e.g. the analog of a single anyon on a torus. We conclude by demonstrating that our gauging procedures enable magic state preparation via the measurement of logical Clifford gates. Consequently, our gauging constructions offer a protocol for performing non-Clifford operations on any qLDPC code.

## The Pinnacle Architecture: Reducing the cost of breaking RSA-2048 to 100 000 physical qubits using quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC로 RSA 깨는 fault-tolerant 양자 아키텍처, 양자 EC 영역으로 제외
- **ID**: arxiv:2602.11457v2
- **Type**: preprint
- **Published**: 2026-02-12
- **Authors**: Paul Webster, Lucas Berent, Omprakash Chandra +5
- **PDF**: https://arxiv.org/pdf/2602.11457v2
- **Abstract**: The realisation of utility-scale quantum computing inextricably depends on the design of practical, low-overhead fault-tolerant architectures. We introduce the Pinnacle Architecture, which uses quantum low-density parity check (QLDPC) codes to allow for universal, fault-tolerant quantum computation with a spacetime overhead significantly smaller than that of any competing architecture. With this architecture, we show that 2048-bit RSA integers can be factored with fewer than one hundred thousand physical qubits, given a physical error rate of $10^{-3}$, code cycle time of $1$ microsecond and a reaction time of $10$ microseconds. We thereby demonstrate the feasibility of utility-scale quantum computing with an order of magnitude fewer physical qubits than has previously been believed necessary.

## Six Times to Spare: Characterizing GPU-Accelerated 5G LDPC Decoding for Edge-RSU Communications

- **Status**: ❌
- **Reason**: 5G LDPC GPU offload 처리량 벤치마크 — NAND에 이식할 디코더/HW/코드설계 기법 없음, 무선 엣지 컴퓨팅 특이적
- **ID**: arxiv:2602.04652v2
- **Type**: preprint
- **Published**: 2026-02-04
- **Authors**: Ryan Barker, Julia Boone, Tolunay Seyfi +3
- **PDF**: https://arxiv.org/pdf/2602.04652v2
- **Abstract**: Ultra-reliable low-latency vehicular communications (URLLC) require sufficient physical-layer (PHY) compute headroom at the network edge, where roadside units (RSUs) and compact next-generation base stations (gNBs) must meet strict timing constraints while co-hosting higher-layer services. In 5G New Radio (5G NR), low-density parity-check code (LDPC) decoding is a latency-sensitive iterative PHY workload whose cost scales with both workload parallelism and decoder iteration budget, making it a potential bottleneck on general-purpose central processing units (CPUs). This paper presents a reproducible, telemetry-backed microbenchmark derived from the Sionna LDPC5G baseline to characterize the compute headroom obtained through graphics processing unit (GPU) offload on compact heterogeneous edge platforms. We evaluate decoder behavior across multiple processor architectures and a wide range of batch sizes and iteration counts, with emphasis on dense operating regimes relevant to edge provisioning. Results show that GPU acceleration substantially increases LDPC throughput, reduces amortized decode service time, and shifts compute pressure away from the CPU, thereby improving the feasibility of meeting edge-RSU timing budgets under heavy parallel workloads. These findings indicate that GPU offload can provide substantial spare PHY compute margin for compact vehicular edge platforms, making dense decode workloads more practical within realistic edge power and timing constraints.

## Qudit Twisted-Torus Codes in the Bivariate Bicycle Framework

- **Status**: ❌
- **Reason**: Qudit 양자 LDPC(twisted-torus) 코드 — qLDPC/양자EC로 제외 카테고리
- **ID**: arxiv:2602.04443v1
- **Type**: preprint
- **Published**: 2026-02-04
- **Authors**: Mourad Halla
- **PDF**: https://arxiv.org/pdf/2602.04443v1
- **Abstract**: We study finite-length qudit quantum low-density parity-check (LDPC) codes from translation-invariant CSS constructions on two-dimensional tori with twisted boundary conditions. Recent qubit work [PRX Quantum 6, 020357 (2025)] showed that, within the bivariate-bicycle viewpoint, twisting generalized toric patterns can significantly improve finite-size performance as measured by $k d^{2}/n$. Here $n$ denotes the number of physical qudits, $k$ the number of logical qudits, and $d$ the code distance. Building on this insight, we extend the search to qudit codes over finite fields. Using algebraic methods, we compute the number of logical qudits and identify compact codes with favorable rate--distance tradeoffs. Overall, for the finite sizes explored, twisted-torus qudit constructions typically achieve larger distances than their untwisted counterparts and outperform previously reported twisted qubit instances. The best new codes are tabulated.
