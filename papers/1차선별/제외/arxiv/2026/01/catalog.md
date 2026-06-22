# arXiv — 2026-01


## Fast magic state preparation by gauging higher-form transversal gates in parallel

- **Status**: ❌
- **Reason**: 양자 magic state preparation/qLDPC — 양자EC로 제외
- **ID**: arxiv:2601.22939v1
- **Type**: preprint
- **Published**: 2026-01-30
- **Authors**: Dominic J. Williamson
- **PDF**: https://arxiv.org/pdf/2601.22939v1
- **Abstract**: Magic states are a foundational resource for universal quantum computation. To survive in a realistic noisy environment, magic states must be prepared fault-tolerantly and protected by a quantum error-correcting code. The recent discovery of highly efficient quantum low-density parity-check codes, together with efficient logic gates, lays the groundwork for low-overhead fault-tolerant quantum computation. This motivates the search for fast and parallel protocols for logical magic state preparation to enable universal quantum computation. Here, we introduce a fast code surgery procedure that performs a fault-tolerant measurement of many transversal logic gates in parallel. This is achieved by performing a generalized gauging measurement on a quantum code that supports a higher-form transversal gate. The time overhead of our procedure is constant, and the qubit overhead is linear. The procedure inherits fault-tolerance properties from the base code and the structure of the higher-form transversal gate. When applied to codes that support higher-form Clifford gates our procedure achieves fast and fault-tolerant preparation of many magic states in parallel. This motivates the search for good quantum low-density parity-check codes that support higher-form Clifford gates.

## Structural Conditions for Native CCZ Magic-State Fountains in qLDPC Codes

- **Status**: ❌
- **Reason**: qLDPC magic-state fountain 구조조건 — 양자EC로 제외
- **ID**: arxiv:2601.22489v1
- **Type**: preprint
- **Published**: 2026-01-30
- **Authors**: Mohammad Rowshan
- **PDF**: https://arxiv.org/pdf/2601.22489v1
- **Abstract**: Quantum low-density parity-check (qLDPC) codes promise constant-rate, linear-distance families with bounded-weight checks, and recent work has realized transversal or constant-depth non-Clifford gates on various (often non-LDPC) codes. However, no explicit \emph{qubit} qLDPC family is known that simultaneously has constant rate, linear distance, bounded stabilizer weight, and a native \emph{magic-state fountain} that prepares many non-Clifford resource states in constant depth.   We take a structural approach and identify coding-theoretic conditions under which a CSS qLDPC family necessarily supports a constant-depth $\CCZ$ magic-state fountain. The key ingredients are: (i) an algebraic notion of \emph{magic-friendly triples} of $X$-type logical operators, defined by pairwise orthogonality and a triple-overlap form controlling diagonal $\CCZ$ phases, and (ii) a 3-uniform hypergraph model of physical $\CCZ$ circuits combined with a packing lemma that turns large collections of such triples with bounded overlaps into bounded-degree hypergraphs.   Our main theorem shows that if a CSS code family on $n$ qubits admits $Ω(n^{1+γ})$ magic-friendly triples whose supports have bounded per-qubit participation, then there exists a constant-depth circuit of physical $\CCZ$ gates implementing $Ω(n^γ)$ logical $\CCZ$ gates in parallel while preserving distance up to a constant factor. For asymptotically good qLDPC families such as quantum Tanner codes, this reduces the existence of a native $\CCZ$ magic-state fountain to a concrete combinatorial problem about counting and distributing magic-friendly triples in the logical $X$ space.

## Quantum bootstrap product codes

- **Status**: ❌
- **Reason**: 양자 bootstrap product 코드(CSS qLDPC) — 양자EC로 제외
- **ID**: arxiv:2601.22363v1
- **Type**: preprint
- **Published**: 2026-01-29
- **Authors**: Meng-Yuan Li
- **PDF**: https://arxiv.org/pdf/2601.22363v1
- **Abstract**: Product constructions constitute a powerful method for generating quantum CSS codes, yielding celebrated examples such as toric codes and asymptotically good low-density parity check (LDPC) codes. Since a CSS code is fully described by a chain complex, existing product formalisms are predominantly homological, defined via the tensor product of the underlying chain complexes of input codes, thereby establishing a natural connection between quantum codes and topology. In this Letter, we introduce the \textit{quantum bootstrap product} (QBP), an approach that extends beyond this standard homological paradigm. Specifically, a QBP code is determined by solving a consistency condition termed the ``bootstrap equation''. We find that the QBP paradigm unifies a wide range of important codes, including general hypergraph product (HGP) codes of arbitrary dimensions and fracton codes typically represented by the X-cube code. Crucially, the solutions to the bootstrap equation yield chain complexes where the chain groups and associated boundary maps consist of multiple components. We term such structures \textit{fork complexes}. This structure elucidates the underlying topological structures of fracton codes, akin to foliated fracton order theories. Beyond conceptual insights, we demonstrate that the QBP paradigm can generate self-correcting quantum codes from input codes with constant energy barriers and surpass the code-rate upper bounds inherent to HGP codes. Our work thus substantially extends the scope of quantum product codes and provides a versatile framework for designing fault-tolerant quantum memories.

## Belief Propagation with Quantum Messages for Symmetric Q-ary Pure-State Channels

- **Status**: ❌
- **Reason**: 양자 메시지 BP(BPQM) classical-quantum 채널 디코더 — 양자 제외 카테고리
- **ID**: arxiv:2601.21330v1
- **Type**: preprint
- **Published**: 2026-01-29
- **Authors**: Avijit Mandal, Henry D. Pfister
- **PDF**: https://arxiv.org/pdf/2601.21330v1
- **Abstract**: Belief propagation with quantum messages (BPQM) provides a low-complexity alternative to collective measurements for communication over classical--quantum channels. Prior BPQM constructions and density-evolution (DE) analyses have focused on binary alphabets. Here, we generalize BPQM to symmetric q-ary pure-state channels (PSCs) whose output Gram matrix is circulant. For this class, we show that bit-node and check-node combining can be tracked efficiently via closed-form recursions on the Gram-matrix eigenvalues, independent of the particular physical realization of the output states. These recursions yield explicit BPQM unitaries and analytic bounds on the fidelities of the combined channels in terms of the input-channel fidelities. This provides a DE framework for symmetric q-ary PSCs that allows one to estimate BPQM decoding thresholds for LDPC codes and to construct polar codes on these channels.

## Bayesian Optimization for Quantum Error-Correcting Code Discovery

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 코드 발견(bivariate bicycle codes) 전용 — 독립적으로 떼어낼 고전 QC-LDPC 부호설계 기법 없음
- **ID**: arxiv:2601.18562v1
- **Type**: preprint
- **Published**: 2026-01-26
- **Authors**: Yihua Chengyu, Richard Meister, Conor Carty +2
- **PDF**: https://arxiv.org/pdf/2601.18562v1
- **Abstract**: Quantum error-correcting codes protect fragile quantum information by encoding it redundantly, but identifying codes that perform well in practice with minimal overhead remains difficult due to the combinatorial search space and the high cost of logical error rate evaluation. We propose a Bayesian optimization framework to discover quantum error-correcting codes that improves data efficiency and scalability with respect to previous machine learning approaches to this task. Our main contribution is a multi-view chain-complex neural embedding that allows us to predict the logical error rate of quantum LDPC codes without performing expensive simulations. Using bivariate bicycle codes and code capacity noise as a testbed, our algorithm discovers a high-rate code [[144,36]] that achieves competitive per-qubit error rate compared to the gross code, as well as a low-error code [[144,16]] that outperforms the gross code in terms of error rate per qubit. These results highlight the ability of our pipeline to automatically discover codes balancing rate and noise suppression, while the generality of the framework enables application across diverse code families, decoders, and noise models.

## Analog-to-Stochastic Converter Using Magnetic Tunnel Junction Devices for Vision Chips

- **Status**: ❌
- **Reason**: MTJ 기반 analog-to-stochastic 변환기(비전칩) — LDPC는 동기 언급뿐, NAND에 이식할 디코더/HW 기법 없음
- **ID**: arxiv:2601.14640v1
- **Type**: preprint
- **Published**: 2026-01-21
- **Authors**: Naoya Onizawa, Daisaku Katagiri, Warren J. Gross +1
- **PDF**: https://arxiv.org/pdf/2601.14640v1
- **Abstract**: This paper introduces an analog-to-stochastic converter using a magnetic tunnel junction (MTJ) device for vision chips based on stochastic computation. Stochastic computation has been recently exploited for area-efficient hardware implementation, such as low-density parity-check (LDPC) decoders and image processors. However, power-and-area hungry two-step (analog-to-digital and digital-to-stochastic) converters are required for the analog to stochastic signal conversion. To realize a one-step conversion, an MTJ device is used as it inherently exhibits a probabilistic switching behavior between two resistance states. Exploiting the device-based probabilistic behavior, analog signals can be directly and area-efficiently converted to stochastic signals to mitigate the signal-conversion overhead. The analog-to-stochastic signal conversion is theoretically described and the conversion characteristic is evaluated using device and circuit parameters. In addition, the resistance variability of the MTJ device is considered in order to compensate the variability effect on the signal conversion. Based on the theoretical analysis, the analog-to-stochastic converter is designed in 90nm CMOS and 100nm MTJ technologies and is verified using a SPICE simulator (NS-SPICE) that handles both transistors and MTJ devices.

## Time-Dynamic Circuits for Fault-Tolerant Shift Automorphisms in Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) fault-tolerant 회로·shift automorphism — 양자 EC 전용, 떼어낼 고전 ECC 기법 없음(제외 카테고리)
- **ID**: arxiv:2601.09911v1
- **Type**: preprint
- **Published**: 2026-01-14
- **Authors**: Younghun Kim, Spiro Gicev, Martin Sevior +1
- **PDF**: https://arxiv.org/pdf/2601.09911v1
- **Abstract**: Quantum low-density parity-check (qLDPC) codes have emerged as a promising approach for realizing low-overhead logical quantum memories. Recent theoretical developments have established shift automorphisms as a fundamental building block for completing the universal set of logical gates for qLDPC codes. However, practical challenges remain because the existing SWAP-based shift automorphism yields logical error rates that are orders of magnitude higher than those for fault-tolerant idle operations. In this work, we address this issue by dynamically varying the syndrome measurement circuits to implement the shift automorphisms without reducing the circuit distance. We benchmark our approach on both twisted and untwisted weight-6 generalized toric codes, including the gross code family. Our time-dynamic circuits for shift automorphisms achieve performance comparable to the idle operations under the circuit-level noise model (SI1000). Specifically, the dynamic circuits achieve more than an order of magnitude reduction in logical error rates relative to the SWAP-based scheme for the gross code at a physical error rate of $10^{-3}$, employing the BP-OSD decoder. Our findings improve both the error resilience and the time overhead of the shift automorphisms in qLDPC codes. Furthermore, our work can lead to alternative syndrome extraction circuit designs, such as leakage removal protocols, providing a practical pathway to utilizing dynamic circuits that extend beyond surface codes towards qLDPC codes.

## Breaking the Orthogonality Barrier in Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC 직교성 제약 극복 구성 — qLDPC 전용 설계로 고전 NAND LDPC로 떼어낼 기법 없음(제외)
- **ID**: arxiv:2601.08824v3
- **Type**: preprint
- **Published**: 2026-01-13
- **Authors**: Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2601.08824v3
- **Abstract**: Classical low-density parity-check (LDPC) codes are a widely deployed and well-established technology, forming the backbone of modern communication and storage systems. It is well known that, in this classical setting, increasing the girth of the Tanner graph while maintaining regular degree distributions leads simultaneously to good belief-propagation (BP) decoding performance and large minimum distance. In the quantum setting, however, this principle does not directly apply because quantum LDPC codes must satisfy additional orthogonality constraints between their parity-check matrices. When one enforces both orthogonality and regularity in a straightforward manner, the girth is typically reduced and the minimum distance becomes structurally upper bounded. In this work, we overcome this limitation by using permutation matrices with controlled commutativity and by restricting the orthogonality constraints to only the active part of the construction, while preserving regular check-matrix structures. This design circumvents conventional structural distance limitations induced by parent-matrix orthogonality, and enables the construction of quantum LDPC codes with large girth while avoiding latent low-weight logical operators. As a concrete demonstration, we construct a girth-8, (3,12)-regular $[[9216,4612, \leq 48]]$ quantum LDPC code and show that, under BP decoding combined with a low-complexity post-processing algorithm, it achieves a frame error rate as low as $10^{-8}$ on the depolarizing channel with error probability $4 \%$.

## An Efficient Algorithm to Sample Quantum Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 양자 LDPC용 self-orthogonal sparse 행렬 샘플링 알고리즘 — dual-containing 제약은 qLDPC 전용, NAND ECC로 떼어낼 기법 없음(제외)
- **ID**: arxiv:2601.08387v2
- **Type**: preprint
- **Published**: 2026-01-13
- **Authors**: Paolo Santini
- **PDF**: https://arxiv.org/pdf/2601.08387v2
- **Abstract**: In this paper, we present an efficient algorithm to sample random sparse matrices to be used as check matrices for quantum Low-Density Parity-Check (LDPC) codes. To ease the treatment, we mainly describe our algorithm as a technique to sample a dual-containing binary LDPC code, hence, a sparse matrix $\mathbf H\in\mathbb F_2^{r\times n}$ such that $\mathbf H\mathbf H^\top = \mathbf 0$. However, as we show, the algorithm can be easily generalized to sample dual-containing LDPC codes over non binary finite fields as well as more general quantum stabilizer LDPC codes.   While several constructions already exist, all of them are somewhat algebraic as they impose some specific property (e.g., the matrix being quasi-cyclic). Instead, our algorithm is purely combinatorial as we do not require anything apart from the rows of $\mathbf H$ being sparse enough. In this sense, we can think of our algorithm as a way to sample sparse, self-orthogonal matrices that are as random as possible.   Our algorithm is conceptually very simple and, as a key ingredient, uses Information Set Decoding (ISD) to sample the rows of $\mathbf H$, one at a time. The use of ISD is fundamental as, without it, efficient sampling would not be feasible. We give a theoretical characterization of our algorithm, determining which ranges of parameters can be sampled as well as the expected computational complexity. Numerical simulations and benchmarks confirm the feasibility and efficiency of our approach.

## Land-then-transport: A Flow Matching-Based Generative Decoder for Wireless Image Transmission

- **Status**: ❌
- **Reason**: 무선 이미지 전송 JSCC/생성 디코더 — LDPC는 baseline 비교 대상일 뿐, 떼어낼 ECC 기법 없음(제외)
- **ID**: arxiv:2601.07512v1
- **Type**: preprint
- **Published**: 2026-01-12
- **Authors**: Jingwen Fu, Ming Xiao, Mikael Skoglund +1
- **PDF**: https://arxiv.org/pdf/2601.07512v1
- **Abstract**: Due to strict rate and reliability demands, wireless image transmission remains difficult for both classical layered designs and joint source-channel coding (JSCC), especially under low latency. Diffusion-based generative decoders can deliver strong perceptual quality by leveraging learned image priors, but iterative stochastic denoising leads to high decoding delay. To enable low-latency decoding, we propose a flow-matching (FM) generative decoder under a new land-then-transport (LTT) paradigm that tightly integrates the physical wireless channel into a continuous-time probability flow. For AWGN channels, we build a Gaussian smoothing path whose noise schedule indexes effective noise levels, and derive a closed-form teacher velocity field along this path. A neural-network student vector field is trained by conditional flow matching, yielding a deterministic, channel-aware ODE decoder with complexity linear in the number of ODE steps. At inference, it only needs an estimate of the effective noise variance to set the ODE starting time. We further show that Rayleigh fading and MIMO channels can be mapped, via linear MMSE equalization and singular-value-domain processing, to AWGN-equivalent channels with calibrated starting times. Therefore, the same probability path and trained velocity field can be reused for Rayleigh and MIMO without retraining. Experiments on MNIST, Fashion-MNIST, and DIV2K over AWGN, Rayleigh, and MIMO demonstrate consistent gains over JPEG2000+LDPC, DeepJSCC, and diffusion-based baselines, while achieving good perceptual quality with only a few ODE steps. Overall, LTT provides a deterministic, physically interpretable, and computation-efficient framework for generative wireless image decoding across diverse channels.

## Coset Shaping: Constructions and Bounds

- **Status**: ❌
- **Reason**: coset shaping은 coded QAM/PAM 신호 성형(변조) 기법 — LDPC는 부수 적용, NAND ECC로 떼어낼 디코더·부호설계 기법 없음(제외)
- **ID**: arxiv:2601.05652v3
- **Type**: preprint
- **Published**: 2026-01-09
- **Authors**: Irina Bocharova, Maiara F. Bollauf, Boris Kudryashov
- **PDF**: https://arxiv.org/pdf/2601.05652v3
- **Abstract**: A new geometric shaping technique, referred to as coset shaping, is proposed and analyzed for coded QAM and PAM signaling. This method can be applied to both information and parity bits without introducing additional complexity. It is shown that, as the error-correcting code length and the modulation order grow, the gap to capacity of the proposed shaping scheme can be made arbitrarily small. A Gallager-type bound is provided together with numerical results, including performance comparisons for the shaping scheme combined with short and mid-length binary-coded, as well as nonbinary LDPC-coded QAM signaling

## Achievable Rate and Coding Principle for MIMO Multicarrier Systems With Cross-Domain MAMP Receiver Over Doubly Selective Channels

- **Status**: ❌
- **Reason**: MIMO 멀티캐리어 MAMP 수신기·achievable rate 분석이 본질; LDPC는 finite-length 성능 벤치마크로 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: arxiv:2601.04433v1
- **Type**: preprint
- **Published**: 2026-01-07
- **Authors**: Yuhao Chi, Zhiyuan Peng, Lei Liu +3
- **PDF**: https://arxiv.org/pdf/2601.04433v1
- **Abstract**: The integration of multicarrier modulation and multiple-input-multiple-output (MIMO) is critical for reliable transmission of wireless signals in complex environments, which significantly improve spectrum efficiency. Existing studies have shown that popular orthogonal time frequency space (OTFS) and affine frequency division multiplexing (AFDM) offer significant advantages over orthogonal frequency division multiplexing (OFDM) in uncoded doubly selective channels. However, it remains uncertain whether these benefits extend to coded systems. Meanwhile, the information-theoretic limit analysis of coded MIMO multicarrier systems and the corresponding low-complexity receiver design remain unclear. To overcome these challenges, this paper proposes a multi-slot cross-domain memory approximate message passing (MS-CD-MAMP) receiver as well as develops its information-theoretic (i.e., achievable rate) limit and optimal coding principle for MIMO-multicarrier modulation (e.g., OFDM, OTFS, and AFDM) systems. The proposed MS-CD-MAMP receiver can exploit not only the time domain channel sparsity for low complexity but also the corresponding symbol domain constellation constraints for performance enhancement. Meanwhile, limited by the high-dimensional complex state evolution (SE), a simplified single-input single-output variational SE is proposed to derive the achievable rate of MS-CD-MAMP and the optimal coding principle with the goal of maximizing the achievable rate. Numerical results show that coded MIMO-OFDM/OTFS/AFDM with MS-CD-MAMP achieve the same maximum achievable rate in doubly selective channels, whose finite-length performance with practical optimized low-density parity-check (LDPC) codes is only 0.5 $\sim$ 1.8 dB away from the associated theoretical limit, and has 0.8 $\sim$ 4.4 dB gain over the well-designed point-to-point LDPC codes.

## Single-Shot and Few-Shot Decoding via Stabilizer Redundancy in Bivariate Bicycle Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(BB 코드)·single-shot 디코딩·BP+OSD가 양자 EC 특이적, 제외 카테고리(양자 EC)
- **ID**: arxiv:2601.01137v1
- **Type**: preprint
- **Published**: 2026-01-03
- **Authors**: Mohammad Rowshan
- **PDF**: https://arxiv.org/pdf/2601.01137v1
- **Abstract**: Bivariate bicycle (BB) codes are a prominent class of quantum LDPC codes constructed from group algebras. While the logical dimension and quantum distance of \emph{coprime} BB codes are known to be determined by a greatest common divisor polynomial $g(z)$, the properties governing their fault tolerance under noisy measurement have remained implicit. In this work, we prove that this same polynomial $g(z)$ dictates the code's stabilizer redundancy and the structure of the classical \emph{syndrome codes} required for single-shot decoding. We derive a strict equality between the quantum rate and the stabilizer redundancy density, and we provide BCH-like bounds on the achievable single-shot measurement error tolerance. Guided by this framework, we construct small coprime BB codes with significantly improved syndrome distance ($d_S$) and evaluate them using BP+OSD. Our analysis reveals a structural bottleneck: within the coprime BB ansatz, high quantum rate imposes an upper bound on syndrome distance, limiting single-shot performance. These results provide concrete algebraic design rules for next-generation 2BGA codes in measurement-limited architectures.

## Reinforcement-Learned Unequal Error Protection for Quantized Semantic Embeddings

- **Status**: ❌
- **Reason**: 강화학습 기반 시맨틱 임베딩 UEP·반복부호; LDPC는 비교 대상일 뿐, 시맨틱 통신·소스 코딩 영역으로 제외
- **ID**: arxiv:2601.00186v1
- **Type**: preprint
- **Published**: 2026-01-01
- **Authors**: Moirangthem Tiken Singh, Adnan Arif
- **PDF**: https://arxiv.org/pdf/2601.00186v1
- **Abstract**: This paper tackles the pressing challenge of preserving semantic meaning in communication systems constrained by limited bandwidth. We introduce a novel reinforcement learning framework that achieves per-dimension unequal error protection via adaptive repetition coding. Central to our approach is a composite semantic distortion metric that balances global embedding similarity with entity-level preservation, empowering the reinforcement learning agent to allocate protection in a context-aware manner. Experiments show statistically significant gains over uniform protection, achieving 6.8% higher chrF scores and 9.3% better entity preservation at 1 dB SNR. The key innovation of our framework is the demonstration that simple, intelligently allocated repetition coding enables fine-grained semantic protection -- an advantage unattainable with conventional codes such as LDPC or Reed-Solomon. Our findings challenge traditional channel coding paradigms by establishing that code structure must align with semantic granularity. This approach is particularly suited to edge computing and IoT scenarios, where bandwidth is scarce, but semantic fidelity is critical, providing a practical pathway for next-generation semantic-aware networks.
