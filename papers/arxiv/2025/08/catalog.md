# arXiv — 2025-08


## A simple universal routing strategy for reducing the connectivity requirements of quantum LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2509.00850v1
- **Type**: preprint
- **Published**: 2025-08-31
- **Authors**: Guangqi Zhao, Fei Yan, Xiaotong Ni
- **PDF**: https://arxiv.org/pdf/2509.00850v1
- **Abstract**: Quantum low-density parity-check codes reduce quantum error correction overhead but require dense, long-range connectivity that challenges hardware implementation, particularly for superconducting processors. We address this problem by demonstrating that long-range connections can be reduced at the cost of increased syndrome extraction circuit depth. Our approach is based on the observation that X and Z ancilla qubits form short loops with data qubits - a property that holds for any quantum code. This enables implementing stabilizer measurement circuits by routing data qubit information through ancilla qubits when direct connections are unavailable. For bivariate bicycle codes, we remove up to 50% of long-range connections while approximately doubling the circuit depth, with the circuit-level distance remaining largely preserved. This method can also be applied to surface codes, achieving the same hexagonal connectivity requirement as McEwen et al. (Quantum 7, 1172 (2023)). Our routing approach for designing syndrome extraction circuits is applicable to diverse quantum codes, offering a practical pathway toward their implementation on hardware with connectivity constraints.

## Louvre: Relaxing Hardware Requirements of Quantum LDPC Codes by Routing with Expanded Quantum Instruction Set

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.20858v1
- **Type**: preprint
- **Published**: 2025-08-28
- **Authors**: Runshi Zhou, Fang Zhang, Hui-Hai Zhao +3
- **PDF**: https://arxiv.org/pdf/2508.20858v1
- **Abstract**: Generalized bicycle codes (GB codes) represent a promising family of quantum low-density parity-check codes, characterized by high code rates and relatively local qubit connectivity. A subclass of the GB code called bivariate bicycle codes (BB codes) has garnered significant interest due to their compatibility with two-layer connectivity architectures on superconducting quantum processors. However, one key limitation of BB codes is their high qubit connectivity degree requirements (degree 6), which exacerbates the noise susceptibility of the system. Building on the recent progress in implementing multiple two-qubit gates on a single chip, this work introduces Louvre -- a routing-based framework designed to reduce qubit connectivity requirements in GB codes. Specifically, Louvre-7 achieves degree reduction while preserving the depth of the syndrome extraction circuit, whereas Louvre-8 further minimizes the connectivity by slightly increasing the circuit depth. When applied to BB codes, these two schemes could reduce the average degree to 4.5 and 4, respectively. Crucially, Louvre eliminates some of the long-range, error-prone connections, which is a distinct advantage over prior approaches. Numerical simulations demonstrate that Louvre-7 has an indistinguishable logical error rate as the standard syndrome extraction circuits of GB codes, while Louvre-8 only incurs a slight error rate penalty. Furthermore, by reordering some of the gates in the circuit, we can reduce the coupler length without degrading the performance. Though most of our analysis focuses on GB codes defined on periodic boundary conditions, we further discuss the adaptability of Louvre to open-boundary lattices and defect-containing grids, underscoring its broader applicability in practical quantum error correction architectures.

## Polar subcodes for MIMO systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.20684v1
- **Type**: preprint
- **Published**: 2025-08-28
- **Authors**: Liudmila Karakchieva, Peter Trifonov
- **PDF**: https://arxiv.org/pdf/2508.20684v1
- **Abstract**: Polar-coded multiple-input multiple-output systems are investigated. An advanced receiver implementing joint list decoding of polar codes and QR- and MMSE-based detectors is proposed. The approximate and exact path metrics are derived for joint list decoder of polar codes. A construction of polar subcodes for MIMO systems with cross-antenna dynamic freezing constraints is proposed. The obtained polar subcodes provide significant performance gain compared to LDPC-coded MIMO systems with the same rate allocation.

## Synthetic Image Detection via Spectral Gaps of QC-RBIM Nishimori Bethe-Hessian Operators

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.19698v1
- **Type**: preprint
- **Published**: 2025-08-27
- **Authors**: V. S. Usatyuk, D. A. Sapozhnikov, S. I. Egorov
- **PDF**: https://arxiv.org/pdf/2508.19698v1
- **Abstract**: The rapid advance of deep generative models such as GANs and diffusion networks now produces images that are virtually indistinguishable from genuine photographs, undermining media forensics and biometric security. Supervised detectors quickly lose effectiveness on unseen generators or after adversarial post-processing, while existing unsupervised methods that rely on low-level statistical cues remain fragile. We introduce a physics-inspired, model-agnostic detector that treats synthetic-image identification as a community-detection problem on a sparse weighted graph. Image features are first extracted with pretrained CNNs and reduced to 32 dimensions, each feature vector becomes a node of a Multi-Edge Type QC-LDPC graph. Pairwise similarities are transformed into edge couplings calibrated at the Nishimori temperature, producing a Random Bond Ising Model (RBIM) whose Bethe-Hessian spectrum exhibits a characteristic gap when genuine community structure (real images) is present. Synthetic images violate the Nishimori symmetry and therefore lack such gaps. We validate the approach on binary tasks cat versus dog and male versus female using real photos from Flickr-Faces-HQ and CelebA and synthetic counterparts generated by GANs and diffusion models. Without any labeled synthetic data or retraining of the feature extractor, the detector achieves over 94% accuracy. Spectral analysis shows multiple well separated gaps for real image sets and a collapsed spectrum for generated ones. Our contributions are threefold: a novel LDPC graph construction that embeds deep image features, an analytical link between Nishimori temperature RBIM and the Bethe-Hessian spectrum providing a Bayes optimal detection criterion; and a practical, unsupervised synthetic image detector robust to new generative architectures. Future work will extend the framework to video streams and multi-class anomaly detection.

## Efficient Probabilistic Parity Shaping for Irregular Repeat-Accumulate LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.19696v1
- **Type**: preprint
- **Published**: 2025-08-27
- **Authors**: Diego Lentner, Thomas Wiegart, Richard D. Wesel
- **PDF**: https://arxiv.org/pdf/2508.19696v1
- **Abstract**: Algorithms are presented that efficiently shape the parity bits of systematic irregular repeat-accumulate (IRA) low-density parity-check (LDPC) codes by following the sequential encoding order of the accumulator. Simulations over additive white Gaussian noise (AWGN) channels with on-off keying show a gain of up to 0.9 dB over uniform signaling.

## Natural Image Classification via Quasi-Cyclic Graph Ensembles and Random-Bond Ising Models at the Nishimori Temperature

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.18717v3
- **Type**: preprint
- **Published**: 2025-08-26
- **Authors**: V. S. Usatyuk, D. A. Sapozhnikov, S. I. Egorov
- **PDF**: https://arxiv.org/pdf/2508.18717v3
- **Abstract**: Modern multi-class image classification uses high-dimensional CNN features that incur large memory and computational costs and obscure the data manifold's geometry. Existing graph-based spectral classifiers work on synthetic or binary tasks but degrade on natural images with many classes because feature manifolds have non-trivial topology. We introduce a physics-inspired pipeline where frozen MobileNetV2 features are interpreted as Ising spins on a sparse multi-edge type quasi-cyclic LDPC graph, defining a Random-Bond Ising Model (RBIM). The model is operated at its Nishimori temperature -- where the smallest eigenvalue of the Bethe-Hessian matrix vanishes. A spectral-topological correspondence links trapping sets in the Tanner graph to topological invariants via poles of the Ihara-Bass zeta function, enabling systematic suppression of harmful substructures that otherwise reduce top-1 accuracy by more than a factor of four. A fast quadratic-Newton estimator finds the Nishimori temperature in $\sim 9$ Arnoldi iterations, a sixfold speed-up over bisection. The resulting ensembles compress the original $1280$-dimensional MobileNetV2 representation to $32$ dimensions (ImageNet-10) or $64$ dimensions (ImageNet-100). We achieve $98.7\%$ top-1 accuracy on ImageNet-10 and $84.92\%$ on ImageNet-100 using a three-graph soft ensemble. Relative to MobileNetV2, our hard ensemble increases accuracy by $0.10\%$ while reducing FLOPs by a factor of $2.67$. Against ResNet-50, the soft ensemble drops only 1.09% accuracy yet cuts FLOPs by $29\times$. The novelty lies in (a) establishing a rigorous link between graph trapping sets and algebraic-topological defects, (b) an efficient Nishimori-temperature estimator, and (c) demonstrating topology-guided LDPC graph embedding for highly compressed classifiers.

## Fermion-to-Fermion Low-Density Parity-Check Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.15323v4
- **Type**: preprint
- **Published**: 2025-08-21
- **Authors**: Chong-Yuan Xu, Ze-Chuan Liu, Yong Xu
- **PDF**: https://arxiv.org/pdf/2508.15323v4
- **Abstract**: Simulating fermionic systems on qubit-based quantum computers often demands significant computational resources due to the requirement to map fermions to qubits. Thus, designing a fault-tolerant quantum computer that operates directly with fermions offers an effective solution to this challenge. Here, we introduce a protocol for fault-tolerant fermionic quantum computation utilizing fermion-to-fermion low-density parity-check (LDPC) codes. Our method employs a fermionic LDPC memory, which transfers its state to fermionic color code processors, where logical operations are subsequently performed. We propose using odd-weight logical Majorana operators to form the code space, serving as memory for the fermionic LDPC code, and provide an algorithm to identify these logical operators. We present examples showing that the encoding rate of fermionic codes often matches that of qubit codes, while the logical failure rate can be significantly lower than the physical error rate. Furthermore, we propose two methods for performing fermionic lattice surgery to facilitate state transfer. Finally, we simulate the dynamics of a fermionic system using our protocol, illustrating effective error suppression.

## Brace for impact: ECDLP challenges for quantum cryptanalysis

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.14011v2
- **Type**: preprint
- **Published**: 2025-08-19
- **Authors**: Pierre-Luc Dallaire-Demers, William Doyle, Timothy Foo
- **PDF**: https://arxiv.org/pdf/2508.14011v2
- **Abstract**: Precise suites of benchmarks are required to assess the progress of early fault-tolerant quantum computers at economically impactful applications such as cryptanalysis. Appropriate challenges exist for factoring but those for elliptic curve cryptography are either too sparse or inadequate for standard applications of Shor's algorithm. We introduce a difficulty-graded suite of elliptic curve discrete logarithm (ECDLP) challenges that use Bitcoin's curve y^2=x^3+7 mod p while incrementally lowering the prime field from 256 down to 6 bits. For each bit-length, we provide the prime, the prime group order, and two deterministic nothing-up-my-sleeve (NUMS) points in compressed SEC1 form. All challenges are generated by a deterministic, reproducible procedure, and no private challenge scalar is chosen in advance. We calibrate classical cost against Pollard's rho records and quantum cost against resource estimation results for Shor's algorithm. We compile Shor's ECDLP circuit to logical counts and map them to physical resources for various parameters of the surface code, the repetition cat code and the LDPC cat codes. Under explicit and testable assumptions on physical error rates, code distances, and non-Clifford supply, our scenarios place the full 256-bit instance within a 2027--2033 window. The challenge ladder thus offers a transparent ruler to track fault-tolerant progress on a cryptanalytic target of immediate relevance, and it motivates proactive migration of digital assets to post-quantum signatures.

## On optimal quantum LRCs from the Hermitian construction and $t$-designs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.13553v1
- **Type**: preprint
- **Published**: 2025-08-19
- **Authors**: Yang Li, Shitao Li, Huimin Lao +2
- **PDF**: https://arxiv.org/pdf/2508.13553v1
- **Abstract**: In a recent work, quantum locally recoverable codes (qLRCs) have been introduced for their potential application in large-scale quantum data storage and implication for quantum LDPC codes. This work focuses on the bounds and constructions of qLRCs derived from the Hermitian construction, which solves an open problem proposed by Luo $et~al.$ (IEEE Trans. Inf. Theory, 71 (3): 1794-1802, 2025). We present four bounds for qLRCs and give comparisons in terms of their asymptotic formulas. We construct several new infinite families of NMDS codes, with general and flexible dimensions, that support t-designs for $t\in \{2,3\}$, and apply them to obtain Hermitian dual-containing classical LRCs (cLRCs). As a result, we derive three explicit families of optimal qLRCs. Compared to the known qLRCs obtained by the CSS construction, our optimal qLRCs offer new and more flexible parameters. It is also worth noting that the constructed cLRCs themselves are interesting as they are optimal with respect to four distinct bounds for cLRCs.

## A Novel CNN Based Standalone Detector for Faster-than-Nyquist Signaling

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.12964v1
- **Type**: preprint
- **Published**: 2025-08-18
- **Authors**: Osman Tokluoglu, Enver Cavus, Ebrahim Bedeer +1
- **PDF**: https://arxiv.org/pdf/2508.12964v1
- **Abstract**: This paper presents a novel convolutional neural network (CNN)-based detector for faster-than-Nyquist (FTN) signaling, introducing structured fixed kernel layers with domain-informed masking to effectively mitigate intersymbol interference (ISI). Unlike standard CNN architectures that rely on moving kernels, the proposed approach employs fixed convolutional kernels at predefined positions to explicitly learn ISI patterns at varying distances from the central symbol. To enhance feature extraction, a hierarchical filter allocation strategy is employed, assigning more filters to earlier layers for stronger ISI components and fewer to later layers for weaker components. This structured design improves feature representation, eliminates redundant computations, and enhances detection accuracy while maintaining computational efficiency. Simulation results demonstrate that the proposed detector achieves near-optimal bit error rate (BER) performance, comparable to the BCJR algorithm for the compression factor $τ\geq 0.7$, while offering up to $46\%$ and $84\%$ computational cost reduction over M-BCJR for BPSK and QPSK, respectively. Additional evaluations confirm the method's adaptability to high-order modulations (up to 64-QAM), resilience in quasi-static multipath Rayleigh fading channels, and effectiveness under LDPC-coded FTN transmission, highlighting its robustness and practicality.

## Magic tricycles: Efficient magic state generation with finite block-length quantum LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.10714v2
- **Type**: preprint
- **Published**: 2025-08-14
- **Authors**: Varun Menon, J. Pablo Bonilla-Ataides, Rohan Mehta +3
- **PDF**: https://arxiv.org/pdf/2508.10714v2
- **Abstract**: The preparation of high-fidelity non-Clifford (magic) states is an essential subroutine for universal quantum computation, but imposes substantial space-time overhead. Magic state factories based on high rate and distance quantum low-density parity check (LDPC) codes equipped with transversal non-Clifford gates can potentially reduce these overheads significantly, by circumventing the need for multiple rounds of distillation and by producing a large number of magic states in a single code-block. As a step towards realizing efficient, fault-tolerant magic state production, we introduce a class of finite block-length quantum LDPC codes which we name tricycle codes, generalizing the well-known bicycle codes to three homological dimensions. These codes can support constant-depth physical circuits that implement logical $CCZ$ gates between three code blocks. To construct these constant-depth $CCZ$ circuits, we develop new analytical and numerical techniques that apply to a broad class of three-dimensional homological and balanced product codes. We further show that tricycle codes enable single-shot state-preparation and error correction, leading to a highly efficient magic-state generation protocol. Numerical simulations of specific codes confirm robust performance under circuit-level noise, demonstrating a high circuit-noise threshold of $>0.5\%$. With modest post-selection, certain tricycle codes of block-lengths of only $50-100$ qubits are shown to achieve logical error-rates of $6\times 10^{-10}$ or lower. Finally, we construct optimal depth syndrome extraction circuits for tricycle codes and present a protocol for implementing them efficiently on a reconfigurable neutral atom platform.

## Fault tolerant Operations in Majorana-based Quantum Codes: Gates, Measurements and High Rate Constructions

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.09928v2
- **Type**: preprint
- **Published**: 2025-08-13
- **Authors**: Maryam Mudassar, Alexander Schuckert, Daniel Gottesman
- **PDF**: https://arxiv.org/pdf/2508.09928v2
- **Abstract**: Majorana-based quantum computation in nanowires and neutral atoms has gained prominence as a promising platform to encode qubits and protect them against noise. In order to run computations reliably on such devices, a fully fault-tolerant scheme is needed for state preparation, gates, and measurements. However, current fault-tolerant schemes have either been limited to specific code families or have not been developed fully. In this work, we develop a general framework for fault-tolerant computation with logical degrees encoded into Majorana hardware. We emphasize the division between even and odd Majorana codes and how it manifests when constructing fault tolerant gadgets for these families. We provide transversal constructions and supplement them with measurements to obtain several examples of fault tolerant Clifford gadgets. For the case of odd codes, we give a novel construction for gadgets using quantum reference frames, that allows to implement operations that are forbidden due to parity superselection. We also provide a fault-tolerant measurement scheme for Majorana codes inspired by Steane error correction, enabling state preparation, measurement of logical operations and error correction. We also point out a construction for odd Majorana codes with transversal T gates. Finally, we construct a high rate quantum LDPC Majorana code with logical qubits. Our work shows that all necessary elements of fault-tolerant quantum computation can be consistently implemented in fermionic hardware such as Majorana nanowires and fermionic neutral atoms.

## Composable Quantum Fault-Tolerance

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.08246v2
- **Type**: preprint
- **Published**: 2025-08-11
- **Authors**: Zhiyang He, Quynh T. Nguyen, Christopher A. Pattison
- **PDF**: https://arxiv.org/pdf/2508.08246v2
- **Abstract**: Proving threshold theorems for fault-tolerant quantum computation is a burdensome endeavor with many moving parts that come together in relatively formulaic but lengthy ways. It is difficult and rare to combine elements from multiple papers into a single formal threshold proof, due to the use of different measures of fault-tolerance. In this work, we introduce composable fault-tolerance, a framework that decouples the probabilistic analysis of the noise distribution from the combinatorial analysis of circuit correctness, and enables threshold proofs to compose independently analyzed gadgets easily and rigorously. Within this framework, we provide a library of standard and commonly used gadgets such as memory and logic implemented by constant-depth circuits for quantum low-density parity check codes and distillation. As sample applications, we explicitly write down a threshold proof for computation with surface code and re-derive the constant space-overhead fault-tolerant scheme of Gottesman using gadgets from this library. We expect that future fault-tolerance proofs may focus on the analysis of novel techniques while leaving the standard components to the composable fault-tolerance framework, with the formal proof following the intuitive ``napkin math'' exactly.

## Long Polar vs. LDPC Codes under Complexity-Constrained Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.05485v1
- **Type**: preprint
- **Published**: 2025-08-07
- **Authors**: Felix Krieg, Marvin Rübenacke, Andreas Zunker +1
- **PDF**: https://arxiv.org/pdf/2508.05485v1
- **Abstract**: The prevailing opinion in industry and academia is that polar codes are competitive for short code lengths, but can no longer keep up with low-density parity-check (LDPC) codes as block length increases. This view is typically based on the assumption that LDPC codes can be decoded with a large number of belief propagation (BP) iterations. However, in practice, the number of iterations may be rather limited due to latency and complexity constraints. In this paper, we show that for a similar number of fixed-point log-likelihood ratio (LLR) operations, long polar codes under successive cancellation (SC) decoding outperform their LDPC counterparts. In particular, simplified successive cancellation (SSC) decoding of polar codes exhibits a better complexity scaling than $N \log{N}$ and requires fewer operations than a single BP iteration of an LDPC code with the same parameters.

## Power and Limitations of Linear Programming Decoder for Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.04769v1
- **Type**: preprint
- **Published**: 2025-08-06
- **Authors**: Shouzhen Gu, Mehdi Soleimanifar
- **PDF**: https://arxiv.org/pdf/2508.04769v1
- **Abstract**: Decoding quantum error-correcting codes is a key challenge in enabling fault-tolerant quantum computation. In the classical setting, linear programming (LP) decoders offer provable performance guarantees and can leverage fast practical optimization algorithms. Although LP decoders have been proposed for quantum codes, their performance and limitations remain relatively underexplored. In this work, we uncover a key limitation of LP decoding for quantum low-density parity-check (LDPC) codes: certain constant-weight error patterns lead to ambiguous fractional solutions that cannot be resolved through independent rounding. To address this issue, we incorporate a post-processing technique known as ordered statistics decoding (OSD), which significantly enhances LP decoding performance in practice. Our results show that LP decoding, when augmented with OSD, can outperform belief propagation with the same post-processing for intermediate code sizes of up to hundreds of qubits. These findings suggest that LP-based decoders, equipped with effective post-processing, offer a promising approach for decoding near-term quantum LDPC codes.

## In-Memory Non-Binary LDPC Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.03567v1
- **Type**: preprint
- **Published**: 2025-08-05
- **Authors**: Oscar Ferraz, Vitor Silva, Gabriel Falcao
- **PDF**: https://arxiv.org/pdf/2508.03567v1
- **Abstract**: Low-density parity-check (LDPC) codes are an important feature of several communication and storage applications, offering a flexible and effective method for error correction. These codes are computationally complex and require the exploitation of parallel processing to meet real-time constraints. As advancements in arithmetic and logic unit technology allowed for higher performance of computing systems, memory technology has not kept the same pace of development, creating a data movement bottleneck and affecting parallel processing systems more dramatically. To alleviate the severity of this bottleneck, several solutions have been proposed, namely the processing in-memory (PiM) paradigm that involves the design of compute units to where (or near) the data is stored, utilizing thousands of low-complexity processing units to perform out bit-wise and simple arithmetic operations. This paper presents a novel efficient solution for near-memory non-binary LDPC decoders in the UPMEM system, for the best of our knowledge the first real hardware PiM-based non-binary LDPC decoder that is benchmarked against low-power GPU parallel solutions highly optimized for throughput performance. PiM-based non-binary LDPC decoders can achieve 76 Mbit/s of decoding throughput, which is even competitive when compared against implementations running in edge GPUs.

## Distributed fault-tolerant quantum memories over a 2xL array of qubit modules

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2508.01879v1
- **Type**: preprint
- **Published**: 2025-08-03
- **Authors**: Edwin Tham, Min Ye, Ilia Khait +2
- **PDF**: https://arxiv.org/pdf/2508.01879v1
- **Abstract**: We propose an architecture for a quantum memory distributed over a $2 \times L$ array of modules equipped with a cyclic shift implemented via flying qubits. The logical information is distributed across the first row of $L$ modules and quantum error correction is executed using ancilla modules on the second row equipped with a cyclic shift. This work proves that quantum LDPC codes such as BB codes can maintain their performance in a distributed setting while using solely one simple connector: a cyclic shift. We propose two strategies to perform quantum error correction on a $2 \times L$ module array: (i) The cyclic layout which applies to any stabilizer codes, whereas previous results for qubit arrays are limited to CSS codes. (ii) The sparse cyclic layout, specific to bivariate bicycle (BB) codes. For the $[[144,12,12]]$ BB code, using the sparse cyclic layout we obtain a quantum memory with $12$ logical qubits distributed over $12$ modules, containing $12$ physical qubits each. We propose physical implementations of this architecture using flying qubits, that can be faithfully transported, and include qubits encoded in ions, neutral atoms, electrons or photons. We performed numerical simulations when modules are long ion chains and when modules are single-qubit arrays of ions showing that the distributed BB code achieves a logical error rate below $2 \cdot 10^{-6}$ when the physical error rate is $10^{-3}$.
