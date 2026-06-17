# arXiv — 2026-05


## SAT, MaxSAT, and SMT for QLDPC Distance Computation: A Large-Scale Empirical Study

- **Status**: ❌
- **Reason**: QLDPC distance 계산(SAT/MaxSAT); 양자 코드 검증 도구라 제외
- **ID**: arxiv:2606.12445v1
- **Type**: preprint
- **Published**: 2026-05-29
- **Authors**: Yu-Fang Chen, Seyed Mohammad Reza Jafari, Ching-Yi Lai
- **PDF**: https://arxiv.org/pdf/2606.12445v1
- **Abstract**: Exact distance computation for quantum LDPC (QLDPC) codes plays a central role in validating candidate fault-tolerant quantum-code constructions, yet the computational structure of this problem remains poorly understood. Despite substantial recent progress in QLDPC design, it remains unclear which algorithmic principles govern the practical scalability of exact distance computation and which classes of exact solvers are best suited to this task. To address these questions, we conduct a systematic study of SAT- and MaxSAT-based formulations for exact QLDPC distance computation across representative codes. We further compare these formulations against several established exact-distance approaches in order to better understand the algorithmic landscape of exact QLDPC distance computation. Our study challenges and refines several prevailing intuitions about exact QLDPC distance computation. First, despite the XOR-rich structure of QLDPC parity checks, practical scalability appears to be governed more by the handling of cardinality constraints and optimization bounds than by parity reasoning alone. Accordingly, XOR-aware reasoning does not provide a systematic advantage across our benchmark suite. Second, Brouwer-Zimmermann-style search, long regarded as the benchmark paradigm for exact distance computation in sparse classical codes, no longer maintains its traditional scalability advantage in the QLDPC setting. This finding challenges the expectation that techniques successful for sparse classical codes remain dominant for QLDPC codes. Third, substantial qualitative differences arise even among MaxSAT solvers themselves. Branch-and-bound MaxSAT significantly outperforms unsat-core-based MaxSAT on challenging benchmarks, demonstrating that solver architecture and optimization strategy play a decisive role in practical scalability.

## OTA Characterization of Dual-User IEEE 802.11be EHT-MU Under Transmit-Chain Imbalance

- **Status**: ❌
- **Reason**: IEEE 802.11be 무선 OTA 측정; LDPC vs BCC 부수 언급, 떼어낼 기법 없음
- **ID**: arxiv:2605.26995v1
- **Type**: preprint
- **Published**: 2026-05-26
- **Authors**: Mir Lodro, Francesco Raimondo, Geoffrey S. Hilton +2
- **PDF**: https://arxiv.org/pdf/2605.26995v1
- **Abstract**: This paper presents a controlled over-the-air (OTA) characterization of dual-user IEEE 802.11be Extremely High Throughput Multi-User (EHT-MU) transmission under transmit-chain imbalance. The objective is to determine whether attenuation applied to one access-point transmit chain produces packet-global degradation or appears primarily as stream-dependent payload degradation after receiver processing. Measurements are performed in a shielded RF enclosure using two NI USRP-2953R and NI USRP-2942R software-defined radios, with one USRP generating a dual-user non-OFDMA EHT-MU waveform and the other implementing synchronized dual-branch packet recovery. A calibrated attenuation sweep is applied to the second AP transmit chain (TX2), and performance is evaluated using bit error rate (BER), EHT-Data error vector magnitude (EVM), control-field success probability, payload-success probability, and subcarrier-level EVM distributions. The results show that the stream decoded as User~1 remains at the BER floor over the tested range, while the stream decoded as User~2 exhibits progressive EVM degradation followed by threshold-like BER and payload-success collapse. Common signaling fields remain recoverable, indicating that the dominant observed failure mode is stream-local at the receiver output than the packet-global. Replacing User~2 binary convolutional coding (BCC) with low density parity check (LDPC) coding delays the BER and payload-success collapse by approximately \(5\)~dB of TX2 attenuation, demonstrating a measurable coding-dependent robustness margin for the more sensitive stream.

## Best-First Ordered Statistics Decoding of Quantum LDPC Codes

- **Status**: ✅
- **Reason**: Best-First OSD 디코더 알고리즘 개선(가능도순 탐색으로 query 1/100); OSD 변형은 NAND LDPC에 이식 가능(C)
- **ID**: arxiv:2605.25777v1
- **Type**: preprint
- **Published**: 2026-05-25
- **Authors**: Michele Banfi, Marco Ferrari, Antonino Favano +2
- **PDF**: https://arxiv.org/pdf/2605.25777v1
- **Abstract**: Belief Propagation (BP) followed by Ordered Statistics Decoding (OSD) has emerged as the gold standard for decoding quantum low-density parity-check (QLDPC) codes. Recent advancements in this field have proposed new methods and algorithms to lower the complexity of this standard pipeline. Because of code degeneracy, and more in general because multiple distinct error patterns can produce the same syndrome, OSD is inherently a list-decoding technique; that is, it enumerates a set of syndrome-consistent candidates and returns the most probable one. In this work, we propose a variant of OSD, which we call Best-First OSD (BF-OSD), that explores the error-candidate space more efficiently by traversing it in order of decreasing likelihood, rather than by brute-force enumeration of a pre-selected subset. In addition, we depart from the conventional BP+OSD cascade: instead of conditioning the OSD invocation on BP convergence, we invoke OSD after a fixed, small number of BP iterations. This design choice is motivated by the full circuit-level noise regime, in which BP is particularly unreliable. Monte Carlo simulations of a family of Bivariate Bicycle (BB) codes under full circuit-level noise show that BF-OSD matches the performance of the BP+OSD baseline while exploring the solution space with 1/100th of the query budget.

## Quantum non-demolition measurements as a practical primitive for fault-tolerant computation against biased noise

- **Status**: ❌
- **Reason**: 바이어스 노이즈 양자 fault-tolerant용 QND Z측정 프리미티브 — 양자EC, NAND LDPC로 이식할 기법 없음
- **ID**: arxiv:2605.24262v1
- **Type**: preprint
- **Published**: 2026-05-22
- **Authors**: Christophe Vuillot, Diego Ruiz, Jérémie Guillaud +1
- **PDF**: https://arxiv.org/pdf/2605.24262v1
- **Abstract**: Leveraging noise bias, where phase-flip errors dominate over bit-flips, can drastically reduce the hardware overhead of fault-tolerant quantum computation, but existing approaches require bias-preserving CNOT gates whose implementation remains experimentally challenging and is provably impossible for strictly two-dimensional systems. We show that high-fidelity quantum non-demolition (QND) multi-qubit Pauli $Z$ measurements provide an equally powerful yet more accessible primitive. We demonstrate that such measurements can fully replace bias-preserving CNOT gates for compiling all operations required by bias-tailored error correction, including stabilizer measurements for repetition codes, XZZX surface codes, and LDPC codes. We propose concrete physical implementations of this primitive for two platforms: solid-state nuclear spins coupled to electron spin ancillas, and dissipatively stabilized superconducting cat qubits. Through circuit-level numerical simulations, we show that an asymmetric XZZX surface code implemented with weight-four QND $Z$ measurements achieves a phase-flip threshold of $\sim\!1.25\%$ and provides a qubit overhead reduction of up to $6\times$ compared to a bias-unaware surface code at noise bias $η= 10^4$. In the regime of very large bias, a repetition code with QND $Z$ measurements attains a threshold of $\sim\!2.3\%$ and achieves overhead comparable to that of a bias-preserving CNOT scheme, without requiring such a gate. Our results establish QND multi-$Z$ measurements as a practical and hardware-efficient route to fault-tolerant quantum computation for a broad class of biased-noise platforms.

## A Two-Branch Finite-Field Construction for Regular CSS LDPC Bases

- **Status**: ✅
- **Reason**: 유한체 QC형 base 구성+girth≥8/4-cycle 제거+cyclic lift+log-domain BP; 코드설계(E)·디코더(C) 이식 가능
- **ID**: arxiv:2605.23894v1
- **Type**: preprint
- **Published**: 2026-05-22
- **Authors**: Koki Okada, Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2605.23894v1
- **Abstract**: This paper develops a two-branch multiplicative-coset construction for regular Calderbank-Shor-Steane (CSS) quantum low-density parity-check base matrices. For a target column weight \(J\) and an even row weight \(L\), the method reduces regularity, CSS orthogonality, and same-type 4-cycle exclusion to explicit quotient-coset conditions over a finite field. A normalized exhaustive search for these conditions produces base matrices for several \((J,L)\) pairs, so the construction is not tied to a single degree distribution. The construction separates the finite-length design into two stages: the base matrix fixes the degree distribution and the first girth constraints, and a cyclic lift randomizes edge connections subject to exact algebraic checks. As a detailed example, we carry one \((3,10)\)-regular base through the lift and decoding stages. For this example, the selected 64-fold lift gives a code whose same-type Tanner graphs have girth at least eight, and it also excludes a specified weight-16 nondegenerate logical-support orbit. The resulting instance is a \([[10240,4108,\,10\le d\le32]]\) CSS code. For decoding, we use joint log-domain belief propagation together with low-complexity deterministic post-processing rules for small residual syndromes, including repairs for residual patterns with two unsatisfied checks. The frame error rate (FER) measurements provide finite-length decoding data for this detailed example; at depolarizing probability \(p=0.058\), the post-processing FER is \(1.0\times10^{-7}\).

## Concatenating Algebraic Codes over High-Rate Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 EC 부호 연접·qudit 리스트 디코딩 — NAND로 이식할 고전 디코더/HW 없음
- **ID**: arxiv:2605.21898v1
- **Type**: preprint
- **Published**: 2026-05-21
- **Authors**: Adam Wills, Michael E. Beverland, Lev S. Bishop +4
- **PDF**: https://arxiv.org/pdf/2605.21898v1
- **Abstract**: Different quantum error correction schemes trade off overhead, error suppression, and hardware connectivity. Code concatenation can relax these tradeoffs by using an outer code whose non-local connectivity is supplied by logical operations of an inner code rather than directly by hardware. Prior works showed that this can reduce memory overhead for local low-rate inner codes such as the surface code. Here, we study concatenation over non-local, high-rate inner codes. Such inner codes experience correlated errors among the many logical qubits in a single codeblock. We handle this by treating each block as a single logical Galois qudit, enabling concatenation with algebraic outer codes with excellent parameters and, crucially, list decoders. In particular, we consider a memory system formed by concatenating quantum Reed-Solomon outer codes over the gross code. For fault-tolerant syndrome extraction, we develop a Galois qudit Shor scheme using "time-like" Reed-Solomon protection against measurement errors. Interestingly, a lightweight fault tolerance scheme, that would fail for qubits, works well for large-alphabet qudits, suggesting a very different theory of fault tolerance for such qudits. The whole protocol is optimised via improved bicycle instruction logical error rates, novel compilation strategies, and recent decoder post-selection rules.   At uniform $10^{-3}$ physical noise, the concatenated gross code reaches the teraquop regime, which it previously could not access, with a lower space overhead than the $288$-qubit two-gross code, while offering several advantages from the engineering standpoint. Beyond our main case study, we believe the core ideas of Galois qudits, quantum Reed-Solomon outer codes, and list decoding, will prove generically powerful and highly transferable ideas across high-rate quantum architectures.

## Forced Gap Post-Selection for Quantum LDPC Codes and their Operations

- **Status**: ❌
- **Reason**: 양자 LDPC 후처리 post-selection 전략 — 양자 EC 전용, 이식 기법 없음
- **ID**: arxiv:2605.20346v1
- **Type**: preprint
- **Published**: 2026-05-19
- **Authors**: Adam Wills, Theodore J. Yoder, Isaac Chuang
- **PDF**: https://arxiv.org/pdf/2605.20346v1
- **Abstract**: We develop a simple and general post-selection strategy for high-rate quantum codes that is transferrable across decoders. After an initial baseline run, the decoder is re-run once per logical observable, and forced in these latter runs to provide a solution where the given observable has the complementary outcome. Shots are rejected that find logically complementary solutions with similar likelihoods compared to the baseline. Using the Relay-BP decoder, we benchmark the strategy on the $72$-qubit and $144$-qubit bivariate bicycle codes, as well as surgery gadgets for the latter. In comparison to previous post-selection strategies, our results offer an improved logical error rate by over a factor of $4$ on the same circuit and physical error rate, and at the same rate of post-selection. Our strategies are also lightweight, relying only on FPGA-friendly belief propagation, whereas the previous best used repeated rounds of a high-latency BP-OSD decoder.

## Perception-Aware Video Semantic Communication

- **Status**: ❌
- **Reason**: 비디오 시맨틱 통신(소스코딩/코덱), LDPC는 베이스라인 언급뿐
- **ID**: arxiv:2605.19397v1
- **Type**: preprint
- **Published**: 2026-05-19
- **Authors**: Yinhuan Huang, Zhijin Qin
- **PDF**: https://arxiv.org/pdf/2605.19397v1
- **Abstract**: Ultra-high-resolution streaming and emerging immersive services are driving rapidly increasing wireless video traffic. However, perceptually pleasing video transmission over bandwidth-limited and latency-constrained wireless links remains challenging for conventional separated source-channel systems, which primarily target bit-level reliability and often suffer performance degradation under short-blocklength transmission. In addition, pixel-level distortion optimization does not necessarily align with human perception, while existing learned video codecs may incur high complexity and raise deployment issues. This paper proposes PVSC, a perception-aware video semantic communication framework for real-time wireless video transmission. PVSC eliminates explicit motion-vector transmission and exploits spatio-temporal feature coding to generate compact and channel-robust symbol streams. It also specifies side-information formatting, reference-buffer management, and lightweight rate control, enabling stable receiver-side reconstruction and bandwidth-adaptive inference with a single model. Extensive experiments demonstrate that PVSC achieves superior performance across diverse datasets, resolutions, GOP configurations, and channel conditions. Compared with the engineered ``VTM + 5G LDPC'' baseline, PVSC saves up to about 75% and 87% bandwidth at comparable LPIPS and DISTS, respectively, while enabling real-time inference on a single NVIDIA RTX 4090 GPU.

## Translation-invariant quantum low-density parity-check codes from compactified fracton models

- **Status**: ❌
- **Reason**: fracton 기반 병진불변 양자 LDPC 순수 이론 — 채널 ECC 아님
- **ID**: arxiv:2605.19298v1
- **Type**: preprint
- **Published**: 2026-05-19
- **Authors**: Cassandra M. Hopkin, Victor V. Albert, Dominic J. Williamson
- **PDF**: https://arxiv.org/pdf/2605.19298v1
- **Abstract**: Quantum error-correcting codes with translation symmetry and local checks have been studied extensively, leading to a wide variety of fracton codes in three or more dimensions which lack a complete unifying picture. Recently, the study of translation-invariant codes with long-range checks has revealed impressive performance for small fixed-size instances in two dimensions. Here, we provide a unifying picture for a large family of translation-invariant codes, both local and long-range, that captures many fracton codes and all Abelian Two-Block Group Algebra (A2BGA) codes, including the Bivariate Bicycle (BB) codes. The balanced product structure of A2BGA codes leads to a local parent code that is a hypergraph product fracton model in a higher dimension. Different compactifications of a parent code produce a wide variety of descendant codes which provides a unifying picture for their properties. In particular, all BB codes with the same check weight are derived from a single parent hypergraph product fracton model. This construction allows us to extend Wang and Pryadko's code-parameter bounds for Generalized Bicycle codes to A2BGA codes. We conjecture that the transversal gates and energy barriers of the translation-invariant descendant codes are limited by those of their parent fracton models.

## Existence and Counting Bounds for High-Memory Spatially-Coupled Codes via the Combinatorial Nullstellensatz

- **Status**: ✅
- **Reason**: 고전 SC-LDPC 단주기·girth 제거 설계공간 특성화 (E) — 비록 nonconstructive bound
- **ID**: arxiv:2605.18323v1
- **Type**: preprint
- **Published**: 2026-05-18
- **Authors**: Lei Huang
- **PDF**: https://arxiv.org/pdf/2605.18323v1
- **Abstract**: The finite-length performance of spatially-coupled low-density parity-check (SC-LDPC) codes is strongly affected by short cycle configurations and the harmful structures induced by them. This paper studies SC-LDPC code design directly at the protograph level, where the design variables are the edge-spreading assignments specified by the partition matrix. In contrast to CLLL/Moser--Tardos based constructive frameworks for QC-SC-LDPC codes, we focus on sharper nonconstructive existence and counting bounds. By encoding cycle-activation conditions as polynomial vanishing constraints over finite grids, we apply the Combinatorial Nullstellensatz to derive sufficient memory conditions for eliminating prescribed cycle-induced harmful structures. For fully connected $(γ,κ)$ base graphs, the resulting bounds explicitly characterize the memory required to destroy all $4$-cycles as well as all $4$- and $6$-cycles, and for fixed $γ$, they are asymptotically tight up to a constant factor compared with known lower bounds. We further apply the Alon--Füredi theorem to obtain lower bounds on the number of feasible edge-spreading assignments, including an explicit counting bound for assignments that eliminate all $4$-cycles and hence yield girth at least six. These results provide a refined algebraic-combinatorial characterization of the feasible design space for high-memory SC-LDPC codes, although no corresponding construction algorithm is provided.

## Maximum Likelihood Decoding of Quantum Error Correction Codes

- **Status**: ❌
- **Reason**: 양자 EC 최대우도복호 리뷰 — 양자 신드롬 디코딩 전용
- **ID**: arxiv:2605.17230v1
- **Type**: preprint
- **Published**: 2026-05-17
- **Authors**: Hanyan Cao, Ge Yan, Yuxuan Du +1
- **PDF**: https://arxiv.org/pdf/2605.17230v1
- **Abstract**: Quantum error correction (QEC) is indispensable for realizing fault-tolerant quantum computation, yet its effectiveness hinges critically on the classical decoding algorithm that interprets noisy syndrome measurements. Among all possible decoding strategies, maximum likelihood decoding (MLD) is provably optimal, since it identifies the logical group with largest likelihood by summing over all possible errors within logical class consistent with the observed syndrome. Despite its optimality, MLD is computationally intractable in general (#P-hard), motivating a rich landscape of exact and approximate algorithms. In this topical review, we provide a unified perspective on MLD by surveying recent advances through three complementary lenses: statistical mechanics, tensor networks, and artificial intelligence. From the statistical mechanics viewpoint, the MLD problem maps onto evaluating partition functions of disordered spin models, enabling exact solutions for certain codes and noise models as well as threshold estimation via phase-transition analysis. From the tensor network perspective, approximate contraction of tensor networks on the code's factor graph yields decoders that closely approach MLD accuracy with polynomial computational cost. From the artificial intelligence perspective, neural-network-based decoders, including autoregressive generative models and recurrent transformers, learn to approximate the MLD distribution from data, achieving high accuracy with the parallelism afforded by modern hardware accelerators. We discuss the connections among these three approaches, review their application to both simulated and experimental quantum hardware, and outline open challenges including real-time decoding, scalability to large code distances, and generalization to high-rate quantum low-density parity-check codes.

## Clifford-deformed zero-rate LDPC codes with 50% biased noise thresholds

- **Status**: ❌
- **Reason**: Clifford-deformed 양자 LDPC 바이어스 노이즈 임계값 — 양자 EC
- **ID**: arxiv:2605.15348v1
- **Type**: preprint
- **Published**: 2026-05-14
- **Authors**: Jagannath Das, Sayandip Dhara, Pedro Medina +2
- **PDF**: https://arxiv.org/pdf/2605.15348v1
- **Abstract**: Applying single-qubit Clifford unitaries to a Pauli stabilizer code produces a Clifford-deformed variant whose stabilizers remain Pauli operators, but with locally rotated Pauli axes. Such deformations provide a simple way to tailor a fixed code to anisotropic noise, and have enabled unusually high thresholds under strongly biased dephasing. In this work, we discuss zero-rate quantum low-density parity-check (LDPC) codes, for which there exist Clifford-deformed variants where the number of biased logical operators scales slower than the distance, or there exists a basis of logical operators whose overlap satisfies certain scaling conditions; in this case, the code-capacity threshold for the Clifford-deformed variant under i.i.d. pure dephasing noise approaches 50%. This property provably explains previously known code examples with 50% biased noise thresholds, such as XY surface code, XZZX surface code, color code, as well as some 3D Clifford-deformed codes. As a concrete new example, we study Clifford deformations of the tile codes of Ref. [1]. Similar to the phase diagram of 50% thresholds for random Clifford deformations of the surface code in Ref. [2], we find a similar phase diagram for the tile codes. We also construct several translationally invariant deformations of the tile code with 50% thresholds, and present numerical evidence for improved performance at finite bias and under circuit-level noise. In the circuit-level setting, performance is governed by the residual bias after a full syndrome-extraction cycle, linking our simulations to phenomenological models commonly used to study Clifford-deformed codes. We estimate this residual bias for different qubit platforms by modeling microscopic implementations of tile-code syndrome extraction.

## Univariate Bicycle Quantum LDPC Codes: Explicit Logical Structure and Distance Bounds

- **Status**: ❌
- **Reason**: Univariate Bicycle 양자 LDPC 부호 구성·거리 한계 — 양자 EC
- **ID**: arxiv:2605.14173v1
- **Type**: preprint
- **Published**: 2026-05-13
- **Authors**: Sheida Rabeti, Hessam Mahdavifar
- **PDF**: https://arxiv.org/pdf/2605.14173v1
- **Abstract**: We introduce univariate bicycle (UB) codes, a structured subclass of generalized bicycle (GB) quantum low-density parity-check (LDPC) codes obtained via a Frobenius relation. This construction reduces the code design space from a two-polynomial search in GB codes to a single-polynomial search, while preserving sparsity. We provide an explicit algebraic characterization of the logical coset spaces by constructing a basis for the logical quotient space, yielding a complete parametrization of logical operators. Leveraging this structure, we derive upper bounds on the minimum distance by relating structured logical representatives to cycle-density properties of associated circulant matrices. Finally, simulation results for short- to medium-length UB codes (block lengths ranging from a few hundred to approximately $10^3$) demonstrate competitive performance relative to existing GB and bivariate bicycle (BB) codes despite the additional algebraic restriction.

## Multiple-Bases Belief Propagation List Decoding for Quantum LDPC Codes

- **Status**: ✅
- **Reason**: MBBP 리스트 BP 디코더(사이클프리 서브트리 다양성)는 고전 LDPC로 이식 가능 (C)
- **ID**: arxiv:2605.14170v1
- **Type**: preprint
- **Published**: 2026-05-13
- **Authors**: Sheida Rabeti, Hessam Mahdavifar
- **PDF**: https://arxiv.org/pdf/2605.14170v1
- **Abstract**: In this paper, we propose a belief-propagation (BP)-based decoder, termed the Multiple-Bases Belief-Propagation List Decoder (MBBP-LD), for quantum low-density parity-check (QLDPC) codes. The key idea is to generate \emph{structured decoding diversity} by constructing multiple redundant parity-check representations via cycle-free subtree decompositions of the Tanner graph, and running BP decoding in parallel across these representations. This extends the classical Multiple-Bases Belief-Propagation (MBBP) framework to the quantum setting while preserving the linear-time complexity and efficiency of standard BP decoding, and avoids the need for super-linear post-processing.   Simulation results demonstrate that MBBP-LD improves upon existing BP-based decoders, including BP with ordered statistics decoding (BP-OSD) and belief propagation with guided decimation (BPGD) across several QLDPC codes, while requiring substantially fewer total BP iterations. For bivariate bicycle codes $[[144,12,12]]$ and $[[288,12,18]]$, MBBP-LD achieves up to $20\%$ reduction in error rate compared to BPGD and up to $30\%$ compared to BP-OSD in the low- and moderate-error regimes. For the larger B1 code $[[882, 24, 18 \leq d \leq 24]]$, MBBP-LD attains comparable or improved performance relative to BPGD while maintaining BP-like decoding latency under parallel implementation.

## A Deep Learning-based Receiver for Asynchronous Grant-Free Random Access in Control-to-Control Networks

- **Status**: ❌
- **Reason**: 무선 그랜트프리 랜덤액세스 DL 수신기, LDPC는 부수적·이식 기법 없음
- **ID**: arxiv:2605.12180v1
- **Type**: preprint
- **Published**: 2026-05-12
- **Authors**: Massimo Battaglioni, Edoardo Carnevali, Dania De Crescenzo +3
- **PDF**: https://arxiv.org/pdf/2605.12180v1
- **Abstract**: In this paper, we study grant-free, asynchronous control-to-control (C2C) communications in an indoor scenario with a shared wireless channel. Each communication node transmits command units, each consisting of a variable-length low-density parity-check (LDPC)--coded payload preceded by a start sequence and followed by a tail sequence. Due to the asynchronous nature of the access, transmissions from different nodes are not aligned over time. As a result, each receiving controller observes the superposition of multiple command units transmitted by different nodes over a receiver-defined superframe interval. Each node transmits one or more replicas of the same command unit. We propose a receiver architecture in which the detection of command unit boundaries (start/tail sequences) is carried out by a single convolutional neural network (CNN) operating directly on the received signal. We show that, while start-sequence detection must rely only on the received waveform, tail-sequence detection can additionally exploit the soft information produced by the LDPC decoder, together with channel estimates. Finally, once commands units are successfully decoded, successive interference cancellation (SIC) can be applied. Simulation results demonstrate that the receiver we propose achieves reliable packet-boundary identification and a low end-to-end packet loss rate, even under uncoordinated and high-traffic operating conditions.

## Scalable Mamba-Based Message-Passing Neural Decoder for Error-Correcting Codes

- **Status**: ✅
- **Reason**: Mamba 기반 메시지패싱 신경망 디코더(MMPD), (1056,880) LDPC에서 검증 — 이식 가능 디코더 알고리즘(C)
- **ID**: arxiv:2605.10681v1
- **Type**: preprint
- **Published**: 2026-05-11
- **Authors**: Rostislav Gusev, Nikita Aleksandrov, Artem Solomkin +1
- **PDF**: https://arxiv.org/pdf/2605.10681v1
- **Abstract**: Forward error correction is essential for reliable communication over noisy channels. Attention-based model-free neural decoders have shown strong performance for short codes, but their scalability to longer codes is limited by the quadratic memory and computational cost of attention. In this paper, we introduce the Mamba message-passing decoder (MMPD), an attention-free syndrome-based neural decoder for binary linear codes. MMPD retains the Tanner-graph structure of a message-passing decoder by performing local pairwise aggregation along variable-check edges. To enable efficient long-range information propagation, these local updates are combined with bidirectional Mamba state-space blocks. By avoiding dense attention matrices, MMPD scales more favorably for long codes in both memory and computation. Experiments on the (1056, 880) LDPC code show that MMPD achieves a 0.45 dB gain over the state-of-the-art CrossMPT decoder at a specified target bit error rate, while reducing memory consumption by a factor of 1.5. This reduction factor increases substantially for longer codes, demonstrating the applicability of MMPD to scalable neural decoding of practical long codes.

## Syndrome Adaptive Gain Control for Min-Sum Decoding of Quantum LDPC Codes

- **Status**: ✅
- **Reason**: Syndrome adaptive gain Min-Sum 디코더(SAGMS) — 양자LDPC 대상이나 온라인 게인 적응 MS 변형은 NAND LDPC로 이식 가능(C)
- **ID**: arxiv:2605.10433v1
- **Type**: preprint
- **Published**: 2026-05-11
- **Authors**: Hernan Cordova, Alexios Balatsoukas-Stimming, Yunus Can Gültekin +2
- **PDF**: https://arxiv.org/pdf/2605.10433v1
- **Abstract**: Min-Sum (MS) decoding is a popular low-complexity alternative to belief propagation (BP), retaining only the minimum incoming message magnitude during check-node (CN) processing, at the cost of systematic message magnitude overestimation. The scaled MS (SMS) decoder compensates for this effect using a fixed scaling factor. We propose the syndrome adaptive gain Min-Sum (SAGMS) decoder for quantum low-density parity-check (QLDPC) codes, which adapts the message gain online based on the fraction of unsatisfied stabilizers, requiring no per-code or per-noise level optimization. We show that the scaling factor required for SMS to match belief propagation decreases with the CN degree, so any fixed scaling optimized for one degree incurs into a growing penalty as the CN degree varies. SAGMS avoids this limitation by adapting the gain during decoding. Simulations on generalized bicycle QLDPC codes demonstrate that SAGMS matches or outperforms the frame error rate (FER) of an offline optimized SMS decoder. Moreover, SAGMS approaches BP performance and, under certain conditions outperforms it while retaining MS-level complexity.

## A Global Coding Scheme for OFDM over Finite Fields

- **Status**: ✅
- **Reason**: GF(2^s) QC-LDPC 구성 + 병렬 이진 소프트결정 반복 디코딩, error floor 없음 — 이식 가능 코드설계/디코더(E/C)
- **ID**: arxiv:2605.09865v1
- **Type**: preprint
- **Published**: 2026-05-11
- **Authors**: Juane Li, Qi-yue Yu, Khaled Abdel-Ghaffar +1
- **PDF**: https://arxiv.org/pdf/2605.09865v1
- **Abstract**: This paper proposes a highly efficient global coded-multiplexing scheme, conceptualized as Orthogonal Frequency Division Multiplexing over a finite field (FF-OFDM), for reliable multiuser communications. By utilizing a prime length cyclic code and its Hadamard equivalents as algebraic subcarriers, independent data streams are globally multiplexed via a Galois Fourier Transform (GFT) without rate loss. We show that this finite-field synthesis intrinsically generates a global Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) code over $\mathrm{GF}(2^s)$, whose parity-check matrix is governed by the structural rigor of partial geometries. At the receiver, supported by a binary decomposition theorem, the received nonbinary global codeword is jointly decoded using parallel binary iterative soft-decision algorithms prior to demultiplexing. This joint decoding enables seamless reliability information sharing across all user streams, achieving near-bound error performance, rapid convergence without error floors, and strictly linear amortized decoding complexity.

## On Codes with Support-Constrained Parity Checks

- **Status**: ✅
- **Reason**: 패리티체크 support 제약 하 최소거리 최대화 코드설계 — LDPC 설계에 직접 적용되는 구성 기법(E)
- **ID**: arxiv:2605.08644v1
- **Type**: preprint
- **Published**: 2026-05-09
- **Authors**: Barron Han, Hikmet Yildiz, Babak Hassibi
- **PDF**: https://arxiv.org/pdf/2605.08644v1
- **Abstract**: We study linear codes that maximize minimum distance subject to arbitrary support constraints on the parity-check matrix. Such constraints arise naturally in the design of LDPC codes, locally repairable codes, and hardware-constrained systems where each parity check must involve only a limited number of code symbols. They are also essential in quantum error correction, where sparse stabilizers reduce measurement noise and respect the connectivity constraints of physical qubit architectures. We derive the optimal minimum distance possible given support constraints on the parity-check matrix and show it is achievable over sufficiently large fields. When this maximum distance coincides with the Singleton bound for unconstrained parity check matrices, the dual GM-MDS construction yields generalized Reed--Solomon codes obeying the mask. In the generator-matrix setting, the GM-MDS theorem guarantees that the optimal distance can always be achieved by a subcode of a generalized Reed--Solomon code while satisfying arbitrary support constraints. We show that this is not true for the parity-check setting. We exhibit a set of support constraints, derived from the vertex-edge incidence of $K_{6,6}$, for which the optimal minimum distance cannot be realized by any subcode of a generalized Reed--Solomon code over any field. We also analyze structured constraint families -- regular, balanced, and cyclic masks -- through numerical optimization, providing design guidance for practical code constructions.

## Non-binary LDPC codes for Data Storage

- **Status**: ✅
- **Reason**: 데이터 스토리지용 비이진 LDPC 코드, 최소거리/이레이저 분석 — 스토리지 ECC + 비이진 코드설계(B/E)
- **ID**: arxiv:2605.08500v2
- **Type**: preprint
- **Published**: 2026-05-08
- **Authors**: Irina Bocharova, Boris Kudryashov, Henk D. L. Hollmann +1
- **PDF**: https://arxiv.org/pdf/2605.08500v2
- **Abstract**: In modern data storage systems, non-binary LDPC codes for recovering from disk failures are increasingly considered strong competitors to MDS codes such as Reed-Solomon codes. Since disk failures can be modeled as erasures, we analyze non-binary LDPC codes over a $q$-ary field in the $q$-ary erasure channel, relative to MDS codes. Our focus is on non-binary LDPC codes whose parity-check matrix is obtained by replacing the non-zero entries of a binary base matrix by elements of a $q$-ary finite field. For such LDPC codes, we introduce the notion of ultimate distance, which upper-bounds their minimum distance. We derive a random-coding bound on the number of non-correctable erasure patterns for the Gallager ensemble of regular non-binary LDPC codes under maximum-likelihood decoding. An algorithm for finding the ultimate distance is presented. A low-complexity algorithm for searching for the minimum distance of the non-binary LDPC code is proposed. Finally, we construct examples of non-binary LDPC codes achieving the ultimate distance.

## RFNoC-Based FPGA Offloading for Fully Programmable PHY Acceleration

- **Status**: ✅
- **Reason**: FPGA 기반 LDPC 인코딩/디코딩·LLR 추정 HW 가속 — 이식 가능 HW 아키텍처(D)
- **ID**: arxiv:2605.07704v1
- **Type**: preprint
- **Published**: 2026-05-08
- **Authors**: A. Oguz Kislal, Osman Mert Yilmaz, Bengu Bilgic Keskin +2
- **PDF**: https://arxiv.org/pdf/2605.07704v1
- **Abstract**: Hardware acceleration has emerged as a key research topic for supporting computationally intensive signal processing and artificial intelligence applications in 6G research and development studies. This paper presents an RF Network on Chip (RFNoC) based hardware acceleration framework that offloads key physical layer procedures to a field programmable gate array (FPGA). The proposed design accelerates procedures, including low density parity check codes (LDPC) encoding and decoding, rate matching and unmatching, interleaving and deinterleaving, scrambling and descrambling, and log likelihood ratio estimation. The accelerator is integrated directly into the OpenAirInterface radio access network software, enabling simultaneous use of the FPGA as driver of the radio front end and a high throughput accelerator. The proposed system is validated through real time experiments with a commercial smartphone successfully connecting to the network. The implementation results demonstrate that a throughput of about 900 Mbps is achiievable using a moderate FPGA resource utlization.

## Affine Subcode Ensemble Decoding for Degeneracy-Aware Quantum Error Correction

- **Status**: ✅
- **Reason**: Affine subcode ensemble BP 디코딩 + overcomplete 행렬 — 양자 대상이나 고전 BP 개선 기법으로 이식 가능(C)
- **ID**: arxiv:2605.06547v2
- **Type**: preprint
- **Published**: 2026-05-07
- **Authors**: Leo Wursthorn, Jonathan Mandelbaum, Sisi Miao +4
- **PDF**: https://arxiv.org/pdf/2605.06547v2
- **Abstract**: Quantum low-density parity-check codes are promising candidates for low-overhead fault-tolerant quantum computing, but degeneracy is known to impair the convergence of belief-propagation (BP) decoding of these codes. In this work, we show that appending linearly independent rows to a check matrix of a stabilizer code can reduce the search space for a valid degenerate solution. Motivated by this, we extend the recently proposed affine subcode ensemble decoding technique from the classical to the quantum setting. Moreover, we employ overcomplete matrices for each decoding path. Monte-Carlo simulations on toric and generalized bicycle codes demonstrate improved convergence and reduced logical error rate.

## Design and Analysis of Quantum Dual-Containing CSS LDPC Codes based on Quasi-Dyadic Matrices

- **Status**: ❌
- **Reason**: 양자 CSS LDPC(qLDPC) 부호 구성 — 양자 EC는 제외 카테고리. 떼어낼 이식형 디코더/HW 없음(표준 binary BP만 언급).
- **ID**: arxiv:2605.03631v2
- **Type**: preprint
- **Published**: 2026-05-05
- **Authors**: Alessio Baldelli, Marco Baldi, Massimo Battaglioni +2
- **PDF**: https://arxiv.org/pdf/2605.03631v2
- **Abstract**: Building scalable quantum computers requires quantum error-correcting codes that enable reliable operations in the presence of noise. Motivated by such need, this paper introduces two constructions of high-rate, quantum dual-containing (DC) Calderbank-Shor-Steane (CSS) low-density parity-check (LDPC) codes based on quasi-dyadic matrices. Their DC structure enables the transversal implementation of the Hadamard gate, and, jointly with the sparsity of their parity-check matrices enable low-complexity decoding via a standard binary belief-propagation algorithm. We provide several theoretical results concerning the cycle properties of these CSS codes. We also investigate their automorphism groups as well as their minimum distance. Furthermore, through numerical simulations, we show that the quantum CSS LDPC codes obtained through these constructions achieve better finite-length error rate performance than existing DC codes across different block lengths and code rates.

## Combinatorial Analysis of Dyadic and Quasi-Dyadic Codes

- **Status**: ✅
- **Reason**: QLDPC 동기이나 dyadic/quasi-dyadic 기반 짧은사이클 열거·제어, PEG식 girth 최대화, absorbing set/error-floor 분석 — 고전 LDPC 코드설계(E)에 직접 이식 가능.
- **ID**: arxiv:2605.01942v1
- **Type**: preprint
- **Published**: 2026-05-03
- **Authors**: Anthony Gómez-Fonseca, Gretchen L. Matthews, Kirsten D. Morris +1
- **PDF**: https://arxiv.org/pdf/2605.01942v1
- **Abstract**: Quantum low-density parity-check (QLDPC) codes offer a promising route to scalable fault-tolerant quantum computation, but their performance under iterative decoding is strongly influenced by short-cycle structure and other harmful subgraphs in the associated Tanner graphs. This paper develops an algebraic framework for constructing and analyzing (Q)LDPC codes from dyadic and quasi-dyadic matrices-translation-invariant $2^\ell \times 2^\ell$ binary matrices specified compactly by a signature row and forming a commutative ring with recursive block structure. Leveraging this structure, we relate cycles in lifted Tanner graphs to tailless backtrackless closed walks in the protograph and derive efficient, implementable methods to enumerate and control short cycles (notably $4$-, $6$-, and $8$-cycles). We introduce dyadic-aware PEG-style construction algorithms that use forbidden sets of shifts to maximize attainable girth when possible and otherwise minimize the multiplicity of the shortest cycles at the target girth. Motivated by error-floor phenomena, we further characterize and explicitly enumerate absorbing sets in key dyadic layout boundary cases, identifying configurations that induce abundant $(a,0)$-absorbing sets. Finally, we propose CSS-oriented dyadic constructions that satisfy commutation constraints by design and demonstrate via belief-propagation simulations that reducing short-cycle multiplicity can yield substantial decoding gains even when girth cannot be increased.

## Improved Rate-versus-Distance Upper Bounds for LDPC Codes

- **Status**: ❌
- **Reason**: LDPC rate-distance 상한 순수 이론 bound — 디코더/HW/구성으로 안 이어짐, 제외.
- **ID**: arxiv:2605.01213v1
- **Type**: preprint
- **Published**: 2026-05-02
- **Authors**: Chong Shangguan, Yulin Yang
- **PDF**: https://arxiv.org/pdf/2605.01213v1
- **Abstract**: LDPC codes play a vital role in coding theory and practical error correction. A central problem in this direction is to understand their rate--distance tradeoff. In this paper, we introduce a new framework for estimating ball sizes in the coset graphs of LDPC codes. The key new object is the coset-weight generating function, which encodes the minimum Hamming weights of all cosets of a linear code. Rather than estimating coset balls directly, we upper-bound this generating function through a local growth analysis for codes spanned by low-weight vectors. This framework sharpens the previous ball-size estimate of Iceland and Samorodnitsky. Combined with a general method of Friedman and Tillich that relates balls in coset graphs to sizes of error-correcting codes, it further improves the upper bounds on the rate of LDPC codes for a significant range of relative distances.

## A Scalable FPGA Architecture for Real-Time Decoding of Quantum LDPC Codes Using GARI

- **Status**: ✅
- **Reason**: 양자 LDPC용이나 message-passing 디코더 FPGA 아키텍처(자원재사용·병렬도·저지연) — HW 아키텍처(D) 이식 가능성 있어 애매하므로 살림.
- **ID**: arxiv:2605.01035v1
- **Type**: preprint
- **Published**: 2026-05-01
- **Authors**: Daniel Báscones, Arshpreet Singh Maan, Valentin Savin +1
- **PDF**: https://arxiv.org/pdf/2605.01035v1
- **Abstract**: In this work, we introduce a new hardware architecture for decoding correlated errors in quantum LDPC codes. The decoder is based on message passing and exploits the structure of the detector error model obtained through the recently introduced Graph Augmentation and Rewiring for Inference (GARI) method. The proposed architecture enables flexible scaling and can, in principle, adapt to any quantum LDPC codes using the GARI framework. It leverages resource reuse while maintaining a modest degree of parallelism, thereby reducing power consumption and area requirements, while preserving low decoding latency.   As a case study, the architecture was implemented on a VCU19P FPGA as an ensemble of three decoder cores targeting the [[144,12,12]] bivariate bicycle code, achieving an average latency of 596 ns per decoding round. This implementation consumes six times fewer resources than the previous GARI-based proposal, being the first reported implementation of multiple decoder cores for correlated errors on a single FPGA device. This enables better energy-conscious scaling of the quantum error correction layer on the classical side, reducing overall power consumption while meeting real-time constraints without compromising decoding accuracy under correlated errors.
