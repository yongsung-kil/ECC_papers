# arXiv — 2026-03


## SAFT: Sensitivity-Aware Filtering and Transmission for Adaptive 3D Point Cloud Communication over Wireless Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.26197v1
- **Type**: preprint
- **Published**: 2026-03-27
- **Authors**: Huda Adam Sirag Mekki, Hui Yuan, Mohanad M. G. Hassan +2
- **PDF**: https://arxiv.org/pdf/2603.26197v1
- **Abstract**: Reliable transmission of 3D point clouds over wireless channels is challenging due to time-varying signal-to-noise ratio (SNR) and limited bandwidth. This paper introduces sensitivity-aware filtering and transmission (SAFT), a learned transmission framework that integrates a Point-BERT-inspired encoder, a sensitivity-guided token filtering (STF) unit, a quantization block, and an SNR-aware decoder for adaptive reconstruction. Specifically, the STF module assigns token-wise importance scores based on the reconstruction sensitivity of each token under channel perturbation. We further employ a training-only symbol-usage penalty to stabilize the discrete representation, without affecting the transmitted payload. Experiments on ShapeNet, ModelNet40, and 8iVFB show that SAFT improves geometric fidelity (D1/D2 PSNR) compared with a separate source--channel coding pipeline (G-PCC combined with LDPC and QAM) and existing learned baselines, with the largest gains observed in low-SNR regimes, highlighting improved robustness under limited bandwidth.

## Theory of (Co)homological Invariants on Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.25831v1
- **Type**: preprint
- **Published**: 2026-03-26
- **Authors**: Zimu Li, Yuguo Shao, Fuchuan Wei +2
- **PDF**: https://arxiv.org/pdf/2603.25831v1
- **Abstract**: With recent breakthroughs in the construction of good qLDPC codes and nearly good qLTCs, the study of (co)homological invariants of quantum code complexes, which fundamentally underlie their logical operations, has become evidently important. In this work, we establish a systematic framework for mathematically analyzing these invariants across a broad spectrum of constructions, from HGP codes to sheaf codes, by synthesizing advanced math tools. We generalize the notion of canonical logical representatives from HGP codes to the sheaf code setting, resolving a long-standing challenge in explicitly characterizing sheaf codewords. Building on this foundation, we present the first comprehensive computation of cup products within the intricate framework of sheaf codes. Given Artin's primitive root conjecture which holds under the generalized Riemann hypothesis, we prove that $\tildeΘ(N)$ independent cup products can be supported on almost good qLDPC codes and qLTCs of length N, opening the possibility of achieving linearly many parallel, nontrivial, constant-depth multi-controlled-Z gates. Moreover, by interpreting sheaf codes as covering spaces of HGP codes via graph lifts, we propose a scheme that inductively generates families of both HGP and sheaf codes in an interlaced fashion from a constant-size HGP code. Notably, the induction preserves all (co)homological invariants of the initial code. This provides a general framework for lifting invariants or logical gates from small codes to infinite code families, and enables efficient verification of such features by checking on small instances. Our theory provides a substantive methodology for studying invariants in HGP codes and extends it to sheaf codes. In doing so, we reveal deep and unexpected connections between qLDPC codes and math, thereby laying the groundwork for future advances in quantum coding, fault tolerance, and physics.

## Exploiting the Degrees of Freedom: Multi-Dimensional Spatially-Coupled Codes Based on Gradient Descent

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.25824v1
- **Type**: preprint
- **Published**: 2026-03-26
- **Authors**: Ata Tanrıkulu, Mete Yıldırım, Ahmed Hareedy
- **PDF**: https://arxiv.org/pdf/2603.25824v1
- **Abstract**: Spatially-coupled (SC) codes are a class of low-density parity-check (LDPC) codes that is gaining increasing attention. Multi-dimensional (MD) SC codes are constructed by connecting copies of an SC code via relocations in order to mitigate various sources of non-uniformity and improve performance in many storage and transmission systems. As the number of degrees of freedom in the MD-SC code design increases, appropriately exploiting them becomes more difficult because of the complexity growth of the design process. In this paper, we propose a probabilistic framework for the MD-SC code design, based on the gradient-descent (GD) algorithm, to design high performance MD codes where this challenge is addressed. In particular, we express the expected number of detrimental objects, which we seek to minimize, in the graph representation of the code in terms of entries of a probability-distribution matrix that characterizes the MD-SC code design. We then find a locally-optimal probability distribution, which serves as the starting point of the finite-length (FL) algorithmic optimizer that produces the final MD-SC code. We adopt a recently-introduced Markov chain Monte Carlo (MCMC) FL algorithmic optimizer that is guided by the proposed GD algorithm. We apply our framework to various objects of interest. We start from simple short cycles, and then we develop the framework to address more sophisticated cycle concatenations, aiming at finer-grained optimization. We offer the theoretical analysis as well as the design algorithms. Next, we present experimental results demonstrating that our MD codes, conveniently called GD-MD codes, have notably lower numbers of targeted detrimental objects compared with the available state-of-the-art. Moreover, we show that our GD-MD codes exhibit significant improvements in error-rate performance compared with MD-SC codes obtained by a uniform distribution.

## Clifford synthesis via generalized S and CZ gates

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.24731v1
- **Type**: preprint
- **Published**: 2026-03-25
- **Authors**: Vadym Kliuchnikov, Marcus P. da Silva
- **PDF**: https://arxiv.org/pdf/2603.24731v1
- **Abstract**: We show that any $n$-qubit Clifford unitary can be implemented using at most $2n$ multi-qubit joint measurements. All the multi-qubit joint measurements used for implementing the Clifford unitary can be chosen to form at most two sets of independent mutually-commuting measurements. Each of these sets is of size at most $n$. This enables very flexible space-time trade-offs when implementing Clifford unitaries. We also discuss a version of the result that relies on multi-target CNOTs and is more relevant for targeting fault-tolerant hardware based on Quantum LDPC codes.

## Finite-Degree Quantum LDPC Codes Reaching the Gilbert-Varshamov Bound

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.24588v2
- **Type**: preprint
- **Published**: 2026-03-25
- **Authors**: Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2603.24588v2
- **Abstract**: We construct asymptotically good nested Calderbank-Shor-Steane (CSS) code pairs from Hsu-Anastasopoulos codes and MacKay-Neal codes. In the fixed-degree regime, we prove that the coding rate stays bounded away from zero and that the relative distances on both sides stay bounded away from zero with probability tending to one as the blocklength grows. Moreover, within an explicit low-degree search window, we determine exactly which even regular degree choices in our construction attain the classical Gilbert-Varshamov (GV) bound on both constituent sides, and consequently the CSS GV bound at fixed finite degree.

## Benchmarking Techniques for Decoded Quantum Interferometry

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.24441v1
- **Type**: preprint
- **Published**: 2026-03-25
- **Authors**: Leon Bollmann, Maximilian Hess
- **PDF**: https://arxiv.org/pdf/2603.24441v1
- **Abstract**: We develop a new benchmarking scheme for the Decoded Quantum Interferometry (DQI) algorithm quantifying the number of quantum gates required to obtain an optimal solution to a problem amenable to DQI. We apply the benchmarking scheme to the Binary Paint Shop Problem (BPSP) in order to benchmark the performance of DQI against a state of the art classical solver. To do so, we provide an explicit construction of a quantum circuit implementation of a greedy decoder for low-density parity check codes arising from max-2-XORSAT problems.

## Unanticipated Adversarial Robustness of Semantic Communication

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.24082v1
- **Type**: preprint
- **Published**: 2026-03-25
- **Authors**: Runxin Zhang, Yulin Shao, Hongyu An +2
- **PDF**: https://arxiv.org/pdf/2603.24082v1
- **Abstract**: Semantic communication, enabled by deep joint source-channel coding (DeepJSCC), is widely expected to inherit the vulnerability of deep learning to adversarial perturbations. This paper challenges this prevailing belief and reveals a counterintuitive finding: semantic communication systems exhibit unanticipated adversarial robustness that can exceed that of classical separate source-channel coding systems. On the theoretical front, we establish fundamental bounds on the minimum attack power required to induce a target distortion, overcoming the analytical intractability of highly nonlinear DeepJSCC models by leveraging Lipschitz smoothness. We prove that the implicit regularization from noisy training forces decoder smoothness, a property that inherently provides built-in protection against adversarial attacks. To enable rigorous and fair comparison, we develop two novel attack methodologies that address previously unexplored vulnerabilities: a structure-aware vulnerable set attack that, for the first time, exploits graph-theoretic vulnerabilities in LDPC codes to induce decoding failure with minimal energy, and a progressive gradient ascent attack that leverages the differentiability of DeepJSCC to efficiently find minimum-power perturbations. Designing such attacks is challenging, as classical systems lack gradient information while semantic systems require navigating high-dimensional, non-convex spaces; our methods fill these critical gaps in the literature. Extensive experiments demonstrate that semantic communication requires up to $14$-$16\times$ more attack power to achieve the same distortion as classical systems, empirically substantiating its superior robustness.

## Towards a Unified Coding Scheme for 6G

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.23123v1
- **Type**: preprint
- **Published**: 2026-03-24
- **Authors**: Paul Bezner, Erdem Eray Cil, Jannis Clausius +14
- **PDF**: https://arxiv.org/pdf/2603.23123v1
- **Abstract**: The growing demand for higher data rates necessitates continuous innovations in wireless communication systems, particularly with the emergence of 6G. Channel coding plays a crucial role in this evolution. In 5G systems, rate-adaptive raptor-like quasi-cyclic irregular low-density parity-check codes are used for the data link, while polar codes with successive cancellation list decoding handle short messages on the synchronization channel. However, to meet the stringent requirements of future 6G systems, a versatile and unified coding scheme should be developed - one that offers competitive error-correcting performance alongside low complexity encoding and decoding schemes that enable energy-efficient hardware implementations. This white paper outlines the vision for such a unified coding scheme. We explore various 6G communication scenarios that pose new challenges to channel coding and provide a first analysis of potential solutions.

## Distance-Finding Algorithms for Quantum Codes and Circuits

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.22532v1
- **Type**: preprint
- **Published**: 2026-03-23
- **Authors**: Mark Webster, Abraham Jacob, Oscar Higgott
- **PDF**: https://arxiv.org/pdf/2603.22532v1
- **Abstract**: The distance of a classical or quantum code is a key figure of merit which reflects its capacity to detect errors. Quantum LDPC code families have considerable promise in reducing the overhead required for fault-tolerant quantum computation, but calculating their distance is challenging with existing methods. We generally assess the performance of a quantum code under circuit level error models, and for such scenarios the circuit distance is an important consideration. Calculating circuit distance is in general more difficult than finding the distance of the corresponding code as the detector error matrix of the circuit is usually much larger than the code's check matrix. In this work, we benchmark a wide range of distance-finding methods for various classical and quantum code families, as well as syndrome-extraction circuits. We consider both exact methods (such as Brouwer-Zimmermann, connected cluster, SAT and mixed integer programming) and heuristic methods which have lower run-time but can only give a bound on distance (examples include random information set, syndrome decoder algorithms, and Stim undetectable error methods). We further develop the QDistEvol algorithm and show that it performs well for the quantum LDPC codes in our benchmark. The algorithms and test data have been made available to the community in the codeDistance Python package.

## Optimal Compilation of Syndrome Extraction Circuits for General Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.21499v1
- **Type**: preprint
- **Published**: 2026-03-23
- **Authors**: Kai Zhang, Dingchao Gao, Zhaohui Yang +4
- **PDF**: https://arxiv.org/pdf/2603.21499v1
- **Abstract**: Quantum error correcting codes (QECC) are essential for constructing large-scale quantum computers that deliver faithful results. As strong competitors to the conventional surface code, quantum low-density parity-check (qLDPC) codes are emerging rapidly: they offer high encoding rates while maintaining reasonable physical-qubit connectivity requirements. Despite the existence of numerous code constructions, a notable gap persists between these designs -- some of which remain purely theoretical -- and their circuit-level deployment.   In this work, we propose Auto-Stabilizer-Check (ASC), a universal compilation framework that generates depth-optimal syndrome extraction circuits for arbitrary qLDPC codes. ASC leverages the sparsity of parity-check matrices and exploits the commutativity of X and Z stabilizer measurement subroutines to search for optimal compilation schemes. By iteratively invoking an SMT solver, ASC returns a depth-optimal solution if a satisfying assignment is found, and a near-optimal solution in cases of solver timeouts. Notably, ASC provides the first definitive answer to one of IBM's open problems: for all instances of bivariate bicycle (BB) code reported in their work, our compiler certifies that no depth-6 syndrome extraction circuit exists.   Furthermore, by integrating ASC with an end-to-end evaluation framework -- one that assesses different compilation settings under a circuit-level noise model -- ASC reduces circuit depth by approximately 50% and achieves an average 7x-8x suppression of the logical error rate for general qLDPC codes, compared with as-soon-as-possible (ASAP) and coloration-based scheduling. ASC thus substantially reduces manual design overhead and demonstrates its strong potential to serve as a key component in accelerating hardware deployment of qLDPC codes.

## Independent Trivariate Bicycle Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.17703v1
- **Type**: preprint
- **Published**: 2026-03-18
- **Authors**: Aygul Azatovna Galimova
- **PDF**: https://arxiv.org/pdf/2603.17703v1
- **Abstract**: We introduce six independent trivariate bicycle (ITB) codes, which extend the bivariate bicycle framework of Bravyi et al.\ to three cyclic dimensions. Using asymmetric polynomial pairs on three-dimensional tori, we construct four codes including a $[[140,6,14]]$ code with $kd^2/n = 8.40$. In the code-capacity setting, the $[[140,6,14]]$ code achieves a pseudothreshold of $8.0\%$ and $kd^2/n = 8.40$, exceeding the best multivariate bicycle code of Voss et al.\ ($7.9\%$, $kd^2/n = 2.67$). With circuit-level depolarizing noise, pseudothresholds reach $0.59\%$ for $[[140,6,14]]$ and $0.53\%$ for $[[84,6,10]]$. On the SI1000 superconducting noise model, the $[[140,6,14]]$ code achieves a per-round per-observable rate of $5.6 \times 10^{-5}$ at $p = 0.20\%$. We additionally present two self-dual codes with weight-8 stabilizers: $[[54,14,5]]$ ($kd^2/n = 6.48$) and $[[128,20,8]]$ ($kd^2/n = 10.0$). These results expand the design space of algebraic quantum LDPC codes and demonstrate that the third cyclic dimension yields competitive candidates for practical fault-tolerant implementations.

## Optimizing Logical Mappings for Quantum Low-Density Parity Check Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.17167v1
- **Type**: preprint
- **Published**: 2026-03-17
- **Authors**: Sayam Sethi, Sahil Khan, Maxwell Poster +2
- **PDF**: https://arxiv.org/pdf/2603.17167v1
- **Abstract**: Early demonstrations of fault tolerant quantum systems have paved the way for logical-level compilation. For fault-tolerant applications to succeed, execution must finish with a low total program error rate (i.e., a low program failure rate). In this work, we study a promising candidate for future fault-tolerant architectures with low spatial overhead: the Gross code. Compilation for the Gross code entails compiling to Pauli Based Computation and then reducing the rotations and measurements to the Bicycle ISA. Depending on the configuration of modules and the placement of code modules on hardware, one can reduce the amount of resulting Bicycle instructions to produce a lower overall error rate.   We find that NISQ-based, and existing FTQC mappers are insufficient for mapping logical qubits on Gross code architectures because 1. they do not account for the two-level nature of the logical qubit mapping problem, which separates into code modules with distinct measurements, and 2. they naively account only for length two interactions, whereas Pauli-Products are up to length $n$, where $n$ is the number of logical qubits in the circuit. For these reasons, we introduce a two-stage pipeline that first uses hypergraph partitioning to create in-module clusters, and then executes a priority-based algorithm to efficiently assign clusters onto hardware. We find that our mapping policy reduces the error contribution from inter-module measurements, the largest source of error in the Gross Code, by up to $\sim36\%$ in the best case, with an average reduction of $\sim13\%$. On average, we reduce the failure rates from inter-module measurements by $\sim22\%$ with localized factory availability, and by $\sim17\%$ on grid architectures, allowing hardware developers to be less constrained in developing scalable fault tolerant systems due to software driven reductions in program failure rates.

## AtlasRAN: Timing-Aware Evaluation of Open-source 5G Platforms for Integrated Wireless Testbeds

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.14661v3
- **Type**: preprint
- **Published**: 2026-03-15
- **Authors**: Ryan Barker, Tolunay Seyfi, Alireza Ebrahimi Dorcheh +3
- **PDF**: https://arxiv.org/pdf/2603.14661v3
- **Abstract**: Open-source 5G and O-RAN experimentation now spans discrete-event simulators, host-OS emulators, SDR hardware-in-the-loop testbeds, O-RU/Open Fronthaul deployments, wireless digital twins, and accelerator-backed RAN runtimes. These environments may expose similar protocol interfaces while preserving very different timing, I/O, synchronization, buffering, transport, and observability behavior. Thus, studies that appear to measure the same network property may instead measure different execution harnesses: functional compatibility is not timing fidelity.   This paper presents AtlasRAN, a timing-aware evaluation framework for deciding what an open-source 5G platform can credibly measure. AtlasRAN provides two reference architectures: a CPU-centric path spanning software emulation, SDR/HIL, and O-RU/OFH execution, and an accelerator/twin path spanning offline modeling, code-realistic twins, and real-time AI-RAN runtimes, plus a compact claim-to-capability matrix. We ground the framework in a CU--DU uplink load study comparing OpenAirInterface RFSim with the Sionna Research Kit, which offloads LDPC decoding to CUDA while retaining much of the surrounding OAI host-OS emulation path. As UE concurrency increases, OAI goodput falls from 114.59 Mb/s at one UE to 16.35 Mb/s in the degraded twelve-UE region, while Sionna-RK falls from 103.34 Mb/s to 16.15 Mb/s. Fairness remains near ideal, CPU/GPU utilization falls with load, and the RFSim real-time factor drops below unity, indicating that the accelerated decoder is under-fed by host-OS inter-process communication and timing effects rather than saturated. AtlasRAN therefore argues that integrated wireless testbeds and digital twins should report timing discipline, transport path, memory movement, and observability as first-class experimental variables.

## Quantum Process Realization of LDPC Code Dualities and Product Constructions

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.13538v1
- **Type**: preprint
- **Published**: 2026-03-13
- **Authors**: Shuhan Zhang, Deepak Aryal, Yi-Zhuang You
- **PDF**: https://arxiv.org/pdf/2603.13538v1
- **Abstract**: We realize a broad class of code constructions, including Kramers-Wannier duality, tensor product, and check product, as quantum processes consisting of ancilla initialization, local unitaries, and projective measurements. Using ZX-calculus, we represent these transformations diagrammatically and provide a systematic algorithm for extracting quantum circuits. Central to our framework is the observation that the physical content of a classical LDPC code is captured by the operator algebra associated with its Tanner graph, and that code transformations correspond to maps between such algebras. Kramers-Wannier duality then admits a natural interpretation as gauging, while tensor and check products correspond to coupled-layer constructions in which interlayer coupling and projection implement a quotient on stacked operator algebras. Together, these results establish a unified framework connecting code transformations, quantum circuits, and mappings between distinct quantum phases of matter.

## Learning to Decode Quantum LDPC Codes Via Belief Propagation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.10192v1
- **Type**: preprint
- **Published**: 2026-03-10
- **Authors**: Mohsen Moradi, Vahid Nourozi, Salman Habib +1
- **PDF**: https://arxiv.org/pdf/2603.10192v1
- **Abstract**: Belief-propagation (BP) decoding for quantum low-density parity-check (QLDPC) codes is appealing due to its low complexity, yet it often exhibits convergence issues due to quantum degeneracy and short cycles that exist in the Tanner graph. To overcome this challenge, this paper proposes a reinforcement-learning (RL) approach that learns (offline) how to decode QLDPC codes based on sequential decoding trajectories. The decoding is formulated as a Markov decision process with a local, syndrome-driven state representation of the underlying RL agent. To enable fast inference, critical for practical implementation, we incrementally update our RL-based QLDPC decoder using second-order neighborhoods that avoid global rescans. Simulation results on representative QLDPC codes demonstrate the superiority of the proposed RL-based QLDPC decoders in terms of performance and convergence speed when compared to flooding and random sequential schedules, while achieving performance competitive with state-of-the-art BP-based decoders at comparable complexity.

## Construction of a Family of Quantum Codes Using Sub-exceding Functions via the Hypergraph Product and the Generalized Shor Construction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.08213v1
- **Type**: preprint
- **Published**: 2026-03-09
- **Authors**: Luc Rabefihavanana, Harinaivo Andriatahiny, Randriamiarampanahy Ferdinand
- **PDF**: https://arxiv.org/pdf/2603.08213v1
- **Abstract**: In this paper, we introduce a new family of stabilizer quantum LDPC codes derived from the classical linear codes $L_k$ and $L_k^{+}$, defined via sub-exceding functions. In previous work, these codes demonstrated strong performance in minimum distance, decoding efficiency, and structural simplicity. By combining the hypergraph product framework with a generalized Shor construction, we obtain a scalable class of quantum codes with parameters $[[6k^2,\, k^2,\, d]]$. The resulting quantum codes exhibit a rich combinatorial structure and promising properties, particularly in terms of locality, low-density parity-check (LDPC) structure, and asymptotic behavior. The minimum distance satisfies $d=3$ for $k=3$ and $d=4$ for $k\ge4$, establishing a new framework for structured quantum LDPC code design and optimization.

## Mirror codes: High-threshold quantum LDPC codes beyond the CSS regime

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.05496v1
- **Type**: preprint
- **Published**: 2026-03-05
- **Authors**: Andrey Boris Khesin, Jonathan Z. Lu
- **PDF**: https://arxiv.org/pdf/2603.05496v1
- **Abstract**: The realization of quantum error correction protocols whose logical error rates are suppressed far below physical error rates relies on an intricate combination: the error-correcting code's efficiency, the syndrome extraction circuit's fault tolerance and overhead, the decoder's quality, and the device's constraints, such as physical qubit count and connectivity. This work makes two contributions towards error-corrected quantum devices. First, we introduce mirror codes, a simple yet flexible construction of LDPC stabilizer codes parameterized by a group $G$ and two subsets of $G$ whose total size bounds the check weight. These codes contain all abelian two-block group algebra codes, such as bivariate bicycle (BB) codes. At the same time, they are manifestly not CSS in general, thus deviating substantially from most prior constructions. Fixing a check weight of 6, we find $[[ 60, 4, 10 ]], [[ 36, 6, 6 ]], [[ 48, 8, 6 ]]$, and $[[ 85, 8, 9 ]]$ codes, all of which are not CSS; we also find several weight-7 codes with $kd > n$.   Next, we construct syndrome extraction circuits that trade overhead for provable fault tolerance. These circuits use 1-2, 3, and 6 ancillae per check, and respectively are partially fault-tolerant (FT), provably FT on weight-6 CSS codes, and provably FT on \emph{all} weight-6 stabilizer codes. Using our constructions, we perform end-to-end quantum memory experiments on several representative mirror codes under circuit-level noise. We achieve an error pseudothreshold on the order of $0.2\%$, approximately matching that of the $[[ 144, 12, 12 ]]$ BB code under the same model. These findings position mirror codes as a versatile candidate for fault-tolerant quantum memory, especially on smaller-scale devices in the near term.

## QGPU: Parallel logic in quantum LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.05398v1
- **Type**: preprint
- **Published**: 2026-03-05
- **Authors**: Boren Gu, Andy Zeyi Liu, Armanda O. Quintavalle +3
- **PDF**: https://arxiv.org/pdf/2603.05398v1
- **Abstract**: Quantum error correction is critical to the design and manufacture of scalable quantum computing systems. Recently, there has been growing interest in quantum low-density parity-check codes as a resource-efficient alternative to surface codes. Their adoption is hindered by the difficulty of compiling fault-tolerant logical operations. A key challenge is that logical qubits do not necessarily map to disjoint sets of physical qubits, which limits parallelism. We introduce clustered-cyclic codes, a quantum low-density parity-check code family with finite-size instances such as [[136,8,14]] and [[198,18,10]] that are competitive with state-of-the-art constructions. These codes admit a directly addressable logical basis, enabling highly parallel logical measurement layers. To leverage this structure, we propose parallel product surgery for quantum product codes. Using an auxiliary copy of the data patch and an engineered product-connection structure, the protocol performs many logical Pauli-product measurements in a single surgery round with small, fixed overhead. For clustered-cyclic codes, this yields surface-code-style maximal parallelism: up to k/2 disjoint Pauli-product measurements per round under explicit algebraic conditions. We prove that parallel product surgery preserves the code distance for hypergraph product codes and numerically verify distance preservation for the listed clustered-cyclic instances with k = 8. Finally, for the [[24,8,3]] clustered-cyclic code, treating half of the logical qubits as auxiliaries enables arbitrary parallel CNOTs on disjoint pairs; combined with symmetry-derived operations, these gates generate the full Clifford group fault-tolerantly.

## Simplified circuit-level decoding using Knill error correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.05320v2
- **Type**: preprint
- **Published**: 2026-03-05
- **Authors**: Ewan Murphy, Subhayan Sahu, Michael Vasmer
- **PDF**: https://arxiv.org/pdf/2603.05320v2
- **Abstract**: Quantum error correction will likely be essential for building a large-scale quantum computer, but it comes with significant requirements at the level of classical control software. In particular, a quantum error-correcting code must be supplemented with a fast and accurate classical decoding algorithm. Standard techniques for measuring the parity-check operators of a quantum error-correcting code involve repeated measurements, which both increases the amount of data that needs to be processed by the decoder, and changes the nature of the decoding problem. Knill error correction is a technique that replaces repeated syndrome measurements with a single round of measurements, but requires an auxiliary logical Bell state. Here, we provide a theoretical and numerical investigation into Knill error correction from the perspective of decoding. We give a self-contained description of the protocol, prove its fault tolerance under locally decaying (circuit-level) noise, and numerically benchmark its performance for quantum low-density parity-check codes. We show analytically and numerically that the time-constrained decoding problem for Knill error correction can be solved using the same decoder used for the simpler code-capacity noise model, illustrating that Knill error correction may alleviate the stringent requirements on classical control required for building a large-scale quantum computer.

## Parsimonious Quantum Low-Density Parity-Check Code Surgery

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.05082v1
- **Type**: preprint
- **Published**: 2026-03-05
- **Authors**: Andrew C. Yuan, Alexander Cowtan, Zhiyang He +2
- **PDF**: https://arxiv.org/pdf/2603.05082v1
- **Abstract**: Quantum code surgery offers a flexible, low-overhead framework for executing logical measurements within quantum error-correcting codes. It encompasses several fault-tolerant logical computation schemes, including parallel surgery, universal adapters and fast surgery, and serves as the key primitive in extractor architectures. The efficiency of these schemes crucially depends on constructing low-overhead ancilla systems for measuring arbitrary logical operators in general quantum Low-Density Parity-Check (qLDPC) codes. In this work, we introduce a method to construct an ancilla system of qubit size $O(W \log W)$ to measure an arbitrary logical Pauli operator of weight $W$ in any qLDPC stabilizer code. This new construction immediately reduces the asymptotic overhead across various quantum code surgery schemes.

## Linear-Time Encodable and Decodable Quantum Error-Correcting Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.04543v1
- **Type**: preprint
- **Published**: 2026-03-04
- **Authors**: Adam Wills, Ting-Chun Lin, Rachel Yun Zhang +1
- **PDF**: https://arxiv.org/pdf/2603.04543v1
- **Abstract**: Recent years have seen rapid development in the subject of quantum coding theory, with breakthroughs on many exciting classes of codes, including quantum LDPC codes, quantum locally testable codes, and quantum codes with interesting transversal gates. However, a natural class of quantum codes, which has been well-studied classically, has not yet been treated: those which can be quickly encoded and decoded. This problem concerns the channel capacity setting, where a noise channel sits between perfect encoding and unencoding/decoding operations; this is the setting that is relevant for communication between fault-tolerant quantum computers.   In this work, we construct asymptotically good quantum codes that can be encoded and unencoded by quantum circuits of logarithmic depth and consisting of a linear total number of gates. The classical decoding algorithms also run in logarithmic depth and use $\mathcal{O}(n \log n)$ gates, or alternatively a linear number of gates but with higher depth. We further construct explicit and asymptotically good quantum codes whose encoding, unencoding and decoding all use a linear number of gates, and additionally whose encoding and unencoding may be run in logarithmic depth.

## Point Cloud Feature Coding for Object Detection over an Error-Prone Cloud-Edge Collaborative System

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.03890v1
- **Type**: preprint
- **Published**: 2026-03-04
- **Authors**: Chongzhen Tian, Hui Yuan, Pan Zhao +3
- **PDF**: https://arxiv.org/pdf/2603.03890v1
- **Abstract**: Cloud-edge collaboration enhances machine perception by combining the strengths of edge and cloud computing. Edge devices capture raw data (e.g., 3D point clouds) and extract salient features, which are sent to the cloud for deeper analysis and data fusion. However, efficiently and reliably transmitting features between cloud and edge devices remains a challenging problem. We focus on point cloud-based object detection and propose a task-driven point cloud compression and reliable transmission framework based on source and channel coding. To meet the low-latency and low-power requirements of edge devices, we design a lightweight yet effective feature compaction module that compresses the deepest feature among multi-scale representations by removing task-irrelevant regions and applying channel-wise dimensionality reduction to task-relevant areas. Then, a signal-to-noise ratio (SNR)-adaptive channel encoder dynamically encodes the attribute information of the compacted features, while a Low-Density Parity-Check (LDPC) encoder ensures reliable transmission of geometric information. At the cloud side, an SNR-adaptive channel decoder guides the decoding of attribute information, and the LDPC decoder corrects geometry errors. Finally, a feature decompaction module restores the channel-wise dimensionality, and a diffusion-based feature upsampling module reconstructs shallow-layer features, enabling multi-scale feature reconstruction. On the KITTI dataset, our method achieved a 172-fold reduction in feature size with 3D average precision scores of 93.17%, 86.96%, and 77.25% for easy, moderate, and hard objects, respectively, over a 0 dB SNR wireless channel. Our source code will be released on GitHub at: https://github.com/yuanhui0325/T-PCFC.

## Characterization of Blind Code Rate Recovery in Linear Block Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2603.02031v1
- **Type**: preprint
- **Published**: 2026-03-02
- **Authors**: Atreya Vedantam, Radha Krishna Ganti
- **PDF**: https://arxiv.org/pdf/2603.02031v1
- **Abstract**: Forward Error Correction (FEC) is used ubiquitously in the communication pipeline. We explore noncooperative decoding where we aim to recover the code rate of a linear block code. We present a metric to characterize the quality of the code rate recovery which uses any rank based estimation technique. We derive a closed form expression for this metric in terms of the algorithmic and the environmental parameters and assert that it should be low for good recovery. We use this metric to derive an expression for a better code rate estimate in high noise conditions and compare it with existing estimates. Finally we validate the derived expression for the metric and the improved performance in the code rate estimate by simulating the recovery of a Low Density Parity Check (LDPC) code. This also enables us to derive the optimal algorithmic parameters for recovery.
