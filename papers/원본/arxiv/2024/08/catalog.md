# arXiv — 2024-08


## Long-Range $ZZ$ Interaction via Resonator-Induced Phase in Superconducting Qubits

- **Status**: ❌
- **Reason**: 초전도 큐빗 ZZ 상호작용 게이트 — qLDPC 연결성 하드웨어, 고전 LDPC 이식 기법 없음
- **ID**: arxiv:2408.16617v2
- **Type**: preprint
- **Published**: 2024-08-29
- **Authors**: Xiang Deng, Wen Zheng, Xudong Liao +8
- **PDF**: https://arxiv.org/pdf/2408.16617v2
- **Abstract**: Superconducting quantum computing emerges as one of leading candidates for achieving quantum advantage. However, a prevailing challenge is the coding overhead due to limited quantum connectivity, constrained by nearest-neighbor coupling among superconducting qubits. Here, we propose a novel multimode coupling scheme using three resonators driven by two microwaves, based on the resonator-induced phase gate, to extend the $ZZ$ interaction distance between qubits. We demonstrate a CZ gate fidelity exceeding 99.9\% within 160 ns at free spectral range (FSR) of 1.4 GHz, and by optimizing driving pulses, we further reduce the residual photon to nearly $10^{-3}$ within 100 ns at FSR of 0.2 GHz. These facilitate the long-range CZ gate over separations reaching sub-meters, thus significantly enhancing qubit connectivity and making a practical step towards the scalable integration and modularization of quantum processors. Specifically, our approach supports the implementation of quantum error correction codes requiring high connectivity, such as low-density parity check codes that paves the way to achieving fault-tolerant quantum computing.

## Performance of Cascade and LDPC-codes for Information Reconciliation on Industrial Quantum Key Distribution Systems

- **Status**: ❌
- **Reason**: QKD 정보 조정 Cascade vs LDPC 비교 — 보안 응용, 표준 LDPC 성능 평가일 뿐 새 기법 없음
- **ID**: arxiv:2408.15758v1
- **Type**: preprint
- **Published**: 2024-08-28
- **Authors**: Ronny Müller, Claudia De Lazzari, Fernando Chirici +5
- **PDF**: https://arxiv.org/pdf/2408.15758v1
- **Abstract**: Information Reconciliation is a critical component of Quantum Key Distribution, ensuring that mismatches between Alice's and Bob's keys are corrected. In this study, we analyze, simulate, optimize, and compare the performance of two prevalent algorithms used for Information Reconciliation: Cascade and LDPC codes in combination with the Blind protocol. We focus on their applicability in practical and industrial settings, operating in realistic and application-close conditions. The results are further validated through evaluation on a live industrial QKD system.

## Continuous Optimization for Decoding Errors

- **Status**: ❌
- **Reason**: 리스트 디코딩 이론(Tanner/AEL/Folded RS) — 순수 이론 bound/조합론, 연판정 BP 디코더/HW로 이어지지 않음
- **ID**: arxiv:2408.14652v1
- **Type**: preprint
- **Published**: 2024-08-26
- **Authors**: Shashank Srivastava
- **PDF**: https://arxiv.org/pdf/2408.14652v1
- **Abstract**: Error-correcting codes are one of the most fundamental objects in pseudorandomness, with applications in communication, complexity theory, and beyond. Codes are useful because of their ability to support decoding, which is the task of recovering a codeword from its noisy copy. List decoding is a relaxation where the decoder is allowed to output a list of codewords, and has seen tremendous progress over the last 25 years. In this thesis, we prove new algorithmic and combinatorial results about list decoding.   We describe a list decoding framework that reduces the task of efficient decoding to proving distance in certain restricted proof systems. We then instantiate this framework for Tanner codes of Sipser and Spielman [IEEE Trans. Inf. Theory 1996] and Alon-Edmonds-Luby (AEL) distance amplification [FOCS 1995] of unique decodable base codes to get the first polynomial time list decoding algorithms for these codes. We also show extensions to the quantum version of AEL distance amplification to get polynomial-time list decodable quantum LDPC codes.   We next give an alternate viewpoint of the above framework based on abstract regularity lemmas. We show how to efficiently implement the regularity lemma for the case of Ta-Shma's explicit codes near the Gilbert-Varshamov bound [STOC 2017]. This leads to a near-linear time algorithm for unique decoding of Ta-Shma's code.   We also give new combinatorial results that improve known list sizes beyond the Johnson bound. Firstly, we adapt the AEL amplification to construct a new family of explicit codes that can be combinatorially list decoded to the optimal error correction radius. This is the first example of such a code that does not use significant algebraic ingredients. Secondly, we present list size improvements for Folded Reed-Solomon codes, improving the state of the art list size for explicit list decoding capacity achieving codes.

## Quantum Rainbow Codes: Achieving Linear Rate, Growing Distance and Transversal Non-Clifford Gates with Generalised Colour Codes

- **Status**: ❌
- **Reason**: 양자 레인보우 코드(컬러/핀 코드 일반화) — 양자 transversal 게이트 구성, 고전 바이너리 이식 불가
- **ID**: arxiv:2408.13130v3
- **Type**: preprint
- **Published**: 2024-08-23
- **Authors**: Thomas R. Scruby, Arthur Pesah, Mark Webster
- **PDF**: https://arxiv.org/pdf/2408.13130v3
- **Abstract**: We introduce rainbow codes, a novel class of quantum error correcting codes generalising colour codes and pin codes. Rainbow codes can be defined on any $D$-dimensional simplicial complex that admits a valid $(D + 1)$-colouring of its $0$-simplices. We study in detail the case where these simplicial complexes are derived from chain complexes obtained via the hypergraph product and, by reinterpreting these codes as collections of colour codes joined at domain walls, show that we can obtain code families with growing distance and number of encoded qubits as well as logical non-Clifford gates implemented by transversal application of $T$ and $T^†$. By combining these techniques with the quasi-hyperbolic colour codes of Zhu et al. (arXiv:2310.16982) we obtain a family of codes with transversal non-Clifford gates and parameters $[\![n, Θ(n), Θ(log(n))]\!]$. This is the first example of a family of LDPC codes with linear rate, growing distance and transversal non-Clifford gates, which are necessary conditions for the magic-state distillation parameter $γ=\textrm{log}_d (n/k)$ to be made arbitrarily small. In contrast to several other constructions that satisfy these requirements, our codes are natively defined on qubits, are LDPC, and have non-Clifford gates implementable by single-qubit (rather than entangling) physical operations, but are not asymptotically good.

## Binary codes from subset inclusion matrices

- **Status**: ✅
- **Reason**: 부분집합 포함행렬 기반 바이너리 LDPC 패리티검사 구성·최소거리 분석 — 신규 바이너리 코드 설계 기법(E), 애매하나 살림
- **ID**: arxiv:2408.12154v1
- **Type**: preprint
- **Published**: 2024-08-22
- **Authors**: Alexey D. Marin, Ivan Yu. Mogilnykh
- **PDF**: https://arxiv.org/pdf/2408.12154v1
- **Abstract**: In this paper, we study the minimum distances of binary linear codes with parity check matrices formed from subset inclusion matrices $W_{t,n,k}$, representing $t$-element subsets versus $k$-element subsets of an $n$-element set. We provide both lower and upper bounds on the minimum distances of these codes and determine the exact values for any $t\leq 3$ and sufficiently large $n$. Our study combines design and integer linear programming techniques. The codes we consider are connected to locally recoverable codes, LDPC codes and combinatorial designs.

## A Quantum Approximate Optimization Algorithm-based Decoder Architecture for NextG Wireless Channel Codes

- **Status**: ❌
- **Reason**: QAOA 기반 양자 디코더 — 양자 하드웨어(qubit/gate)에 의존, 고전 NAND LDPC 디코더로 이식 불가
- **ID**: arxiv:2408.11726v1
- **Type**: preprint
- **Published**: 2024-08-21
- **Authors**: Srikar Kasi, James Sud, Kyle Jamieson +1
- **PDF**: https://arxiv.org/pdf/2408.11726v1
- **Abstract**: Forward Error Correction (FEC) provides reliable data flow in wireless networks despite the presence of noise and interference. However, its processing demands significant fraction of a wireless network's resources, due to its computationally-expensive decoding process. This forces network designers to compromise between performance and implementation complexity. In this paper, we investigate a novel processing architecture for FEC decoding, one based on the quantum approximate optimization algorithm (QAOA), to evaluate the potential of this emerging quantum compute approach in resolving the decoding performance-complexity tradeoff.   We present FDeQ, a QAOA-based FEC Decoder design targeting the popular NextG wireless Low Density Parity Check (LDPC) and Polar codes. To accelerate QAOA-based decoding towards practical utility, FDeQ exploits temporal similarity among the FEC decoding tasks. This similarity is enabled by the fixed structure of a particular FEC code, which is independent of any time-varying wireless channel noise, ambient interference, and even the payload data. We evaluate FDeQ at a variety of system parameter settings in both ideal (noiseless) and noisy QAOA simulations, and show that FDeQ achieves successful decoding with error performance at par with state-of-the-art classical decoders at low FEC code block lengths. Furthermore, we present a holistic resource estimation analysis, projecting quantitative targets for future quantum devices in terms of the required qubit count and gate duration, for the application of FDeQ in practical wireless networks, highlighting scenarios where FDeQ may outperform state-of-the-art classical FEC decoders.

## Multi-User SR-LDPC Codes

- **Status**: ❌
- **Reason**: NOMA 무선용 SR-LDPC 다중사용자 AMP-BP 스킴 — 무선 특이적, 떼어낼 고전 ECC 기법 없음
- **ID**: arxiv:2408.11165v1
- **Type**: preprint
- **Published**: 2024-08-20
- **Authors**: Jamison R. Ebert, Jean-Francois Chamberland, Krishna R. Narayanan
- **PDF**: https://arxiv.org/pdf/2408.11165v1
- **Abstract**: This article introduces a novel non-orthogonal multiple access (NOMA) scheme for coordinated uplink channels. The scheme builds on the recently proposed sparse-regression low-density parity-check (SR-LDPC) code, and extends the underlying notions to scenarios with many concurrent users. The resulting scheme, called Multi-User SR-LDPC (MU-SR-LDPC) coding, consists of each user transmitting its own SR-LDPC codeword using a unique sensing matrix in conjunction with a characteristic outer LDPC code. To recover the sent information, the decoder jointly processes the received signals using a low-complexity and highly-parallelizable AMP-BP algorithm. At finite blocklengths (FBL), MU-SR-LDPC codes are shown to achieve a target BER at a higher spectral efficiency than baseline orthogonal multiple access (OMA) and non-orthogonal multiple access (NOMA) schemes with similar computational complexity. Furthermore, MU-SR-LDPC codes are shown to match the performance of maximum a posteriori (MAP) decoding in certain regimes. For certain blocklengths and a sufficiently high number of users, MU-SR-LDPC codes may achieve a higher spectral efficiency than the approximate FBL capacity of the effective single-user Gaussian channel seen by each user in a comparable OMA scheme. Results are supported by numerical simulations.

## Effect of Correlated Errors on Quantum Memory

- **Status**: ❌
- **Reason**: 양자 메모리 상관오류·Quantum Tanner 코드 — 양자 전용(스태빌라이저) 개념 의존, 원칙 제외
- **ID**: arxiv:2408.08786v2
- **Type**: preprint
- **Published**: 2024-08-16
- **Authors**: Smita Bagewadi, Avhishek Chatterjee
- **PDF**: https://arxiv.org/pdf/2408.08786v2
- **Abstract**: Recent results on constant overhead LDPC code-based fault-tolerance against i.i.d. errors naturally lead to the question of fault-tolerance against errors with long-range correlations. Ideally, any correlation can be captured by a joint (system and bath) Hamiltonian. However, an arbitrary joint Hamiltonian is often intractable, and hence, the joint Hamiltonian model with pairwise terms was introduced and developed in a series of foundational works. However, the analysis of the new constant overhead codes in that error model appears to be quite challenging. In this paper, to model correlated errors in quantum memory, we introduce a correlation model which is a generalization of the well-known hidden random fields. This proposed model, which includes stationary and ergodic (non-Markov) error distributions, is shown to capture correlations not captured by the joint Hamiltonian model with pairwise terms. On the other hand, building on non-i.i.d. measure concentration, we show that for a broad class of non-Markov and (possibly) non-stationary error distributions, quantum Tanner codes ensure an exponential retention time (in the number of physical qubits), when the error rate is below a threshold. An implication of these results is that the rate of decay of the correlation with distance does not necessarily differentiate between good and bad correlation.

## Enhanced BICM Receivers for Ultra-Reliable Low-Latency Short Packet Communications

- **Status**: ❌
- **Reason**: 5G BICM 수신기 결합 추정-검출 LLR 메트릭 — 무선 수신기 특이적, LDPC는 베이스라인
- **ID**: arxiv:2408.08660v4
- **Type**: preprint
- **Published**: 2024-08-16
- **Authors**: Mody Sy, Raymond Knopp
- **PDF**: https://arxiv.org/pdf/2408.08660v4
- **Abstract**: This paper presents enhanced receiver metrics for joint estimation-detection in short blocklength transmissions, addressing scenarios with unknown channel state information and low or sparse training resource density. We show that it is possible to enhance the performance and sensitivity through block-wise joint estimation-detection compared to standard receivers. The performance analysis makes use of a full 5G transmitter and receiver chains for both Polar and LDPC coded transmissions paired with QPSK modulation scheme. We consider transmissions where reference signals are interleaved with coded data and both are transmitted over a small number of OFDM symbols so that near-perfect channel estimation cannot be achieved. Unlike conventional symbol-by-symbol detection in BICM systems, where the observation for a given coded bit is confined to the symbol in which it is conveyed,the proposed method performs block-wise joint detection over a sliding window of adjacent symbols to fundamentally leverages their statistical dependencies. Accordingly, the LLR for a particular coded bit incorporates information from all symbols within the detection window, rather than being constrained to its host symbol alone. Performance evaluation spans SIMO and SU-MIMO configurations, emphasizing the efficacy of the estimation-detection strategy in realistic base station receiver scenarios. Our findings demonstrate that when the detection windows used in the metric units are on the order of four modulated symbols, the proposed receivers remarkably outperform the conventional ones and can be used to achieve detection performance that is close to that of coherent receivers with perfect CSI.

## Optimization by Decoded Quantum Interferometry

- **Status**: ❌
- **Reason**: Decoded Quantum Interferometry — 양자 최적화 알고리즘이 LDPC 디코딩을 도구로 사용, 고전 디코더 기여 아님
- **ID**: arxiv:2408.08292v5
- **Type**: preprint
- **Published**: 2024-08-15
- **Authors**: Stephen P. Jordan, Noah Shutty, Mary Wootters +6
- **PDF**: https://arxiv.org/pdf/2408.08292v5
- **Abstract**: Achieving superpolynomial speedups for optimization has long been a central goal for quantum algorithms. Here we introduce Decoded Quantum Interferometry (DQI), a quantum algorithm that uses the quantum Fourier transform to reduce optimization problems to decoding problems. For approximating optimal polynomial fits over finite fields, DQI achieves a superpolynomial speedup over known classical algorithms. The speedup arises because the problem's algebraic structure is reflected in the decoding problem, which can be solved efficiently. We then investigate whether this approach can achieve speedup for optimization problems that lack algebraic structure but have sparse clauses. These problems reduce to decoding LDPC codes, for which powerful decoders are known. To test this, we construct a max-XORSAT instance where DQI finds an approximate optimum significantly faster than general-purpose classical heuristics, such as simulated annealing. While a tailored classical solver can outperform DQI on this instance, our results establish that combining quantum Fourier transforms with powerful decoding primitives provides a promising new path toward quantum speedups for hard optimization problems.

## Stabilizer Entanglement Distillation and Efficient Fault-Tolerant Encoders

- **Status**: ❌
- **Reason**: 양자 얽힘 증류·스태빌라이저/qLDPC 디코더 — 양자 전용 개념 의존, 제외
- **ID**: arxiv:2408.06299v2
- **Type**: preprint
- **Published**: 2024-08-12
- **Authors**: Yu Shi, Ashlesha Patil, Saikat Guha
- **PDF**: https://arxiv.org/pdf/2408.06299v2
- **Abstract**: Entanglement is essential for quantum information processing, but is limited by noise. We address this by developing high-yield entanglement distillation protocols with several advancements. (1) We extend the 2-to-1 recurrence entanglement distillation protocol to higher-rate n-to-(n-1) protocols that can correct any single-qubit errors. These protocols are evaluated through numerical simulations focusing on fidelity and yield. We also outline a method to adapt any classical error-correcting code for entanglement distillation, where the code can correct both bit-flip and phase-flip errors by incorporating Hadamard gates. (2) We propose a constant-depth decoder for stabilizer codes that transforms logical states into physical ones using single-qubit measurements. This decoder is applied to entanglement distillation protocols, reducing circuit depth and enabling protocols derived from high-performance quantum error-correcting codes. We demonstrate this by evaluating the circuit complexity for entanglement distillation protocols based on surface codes and quantum convolutional codes. (3) Our stabilizer entanglement distillation techniques advance quantum computing. We propose a fault-tolerant protocol for constant-depth encoding and decoding of arbitrary states in surface codes, with potential extensions to more general quantum low-density parity-check codes. This protocol is feasible with state-of-the-art reconfigurable atom arrays and surpasses the limits of conventional logarithmic depth encoders. Overall, our study integrates stabilizer formalism, measurement-based quantum computing, and entanglement distillation, advancing both quantum communication and computing.

## Linear-optical quantum computation with arbitrary error-correcting codes

- **Status**: ❌
- **Reason**: 선형광학 양자계산·qLDPC/GKP — 순수 양자, 고전 LDPC 이식 기법 없음
- **ID**: arxiv:2408.04126v3
- **Type**: preprint
- **Published**: 2024-08-07
- **Authors**: Blayney W. Walshe, Ben Q. Baragiola, Hugo Ferretti +11
- **PDF**: https://arxiv.org/pdf/2408.04126v3
- **Abstract**: High-rate quantum error correcting codes mitigate the imposing scale of fault-tolerant quantum computers but require efficient generation of non-local, many-body entanglement. We provide a linear-optical architecture with these properties, compatible with arbitrary codes and Gottesman-Kitaev-Preskill qubits on generic lattices, and featuring a natural way to leverage physical noise bias. Simulations of hyperbolic surface codes and bivariate bicycle codes, promising families of quantum low-density parity-check codes, reveal a threshold comparable to the 2D surface code with substantially better encoding rates.

## Transform Arbitrary Good Quantum LDPC Codes into Good Geometrically Local Codes in Any Dimension

- **Status**: ❌
- **Reason**: qLDPC를 기하 국소 코드로 변환 — 순수 양자 코드 구성(체인 복합체), 비대상
- **ID**: arxiv:2408.01769v1
- **Type**: preprint
- **Published**: 2024-08-03
- **Authors**: Xingjian Li, Ting-Chun Lin, Min-Hsiu Hsieh
- **PDF**: https://arxiv.org/pdf/2408.01769v1
- **Abstract**: Geometrically local quantum codes, comprised of qubits and checks embedded in $\mathbb{R}^D$ with local check operators, have been a subject of significant interest. A key challenge is identifying the optimal code construction that maximizes both dimension and distance. Recent advancements have produced several constructions, but these either depend on specific good quantum low-density parity-check (qLDPC) codes or are limited to three dimensions. In this work, we introduce a construction that can transform any good qLDPC code into an optimal geometrically local quantum code. Our approach hinges on a novel procedure that extracts a two-dimensional structure from an arbitrary three-term chain complex. We expect that this procedure will find broader applications in areas such as weight reduction and the geometric realization of chain complexes.

## Time-Efficient Logical Operations on Quantum Low-Density Parity Check Codes

- **Status**: ❌
- **Reason**: qLDPC 논리 Pauli 동시 측정 — 양자 전용 연산, 제외
- **ID**: arxiv:2408.01339v3
- **Type**: preprint
- **Published**: 2024-08-02
- **Authors**: Guo Zhang, Ying Li
- **PDF**: https://arxiv.org/pdf/2408.01339v3
- **Abstract**: We propose schemes capable of measuring an arbitrary set of commutative logical Pauli operators in time independent of the number of operators. The only condition is commutativity, a fundamental requirement for simultaneous measurements in quantum mechanics. Quantum low-density parity check (qLDPC) codes show great promise for realizing fault-tolerant quantum computing. They are particularly significant for early fault-tolerant technologies as they can encode many logical qubits using relatively few physical qubits. By achieving simultaneous measurements of logical operators, our approaches enable fully parallelized quantum computing, thus minimizing computation time. Our schemes are applicable to any qLDPC codes and maintain the low density of parity checks while measuring multiple logical operators simultaneously. These results enhance the feasibility of applying early fault-tolerant technologies to practical problems.
