# arXiv — 2025-06


## Improved energy barrier in higher-dimensional hypergraph product codes

- **Status**: ❌
- **Reason**: 양자 hypergraph product 코드의 energy barrier 이론 분석 — 양자 EC, 스태빌라이저 의존, 디코더/HW/코드설계 이식 기법 없음
- **ID**: arxiv:2506.19219v3
- **Type**: preprint
- **Published**: 2025-06-24
- **Authors**: Guangqi Zhao
- **PDF**: https://arxiv.org/pdf/2506.19219v3
- **Abstract**: Single-shot error correction outperforms conventional approaches by requiring only one round of stabilizer measurements for decoding, even in the presence of measurement errors. This capability relates to the confinement property of codes, which provides an energy barrier lower bound. Earlier research established a confinement property for higher-dimensional hypergraph product (HHGP) codes (Quintavalle et al. 2021 PRX Quantum), yielding an energy barrier lower bound for these codes. In this work, by analyzing the structure of logical operators, we show an improved energy barrier lower bound for HHGP codes with low-density parity-check (LDPC) property. Our bound exceeds results derived from confinement alone, and unlike standard hypergraph product codes, these higher dimensional variants can possess macroscopic energy barriers even when the underlying classical codes lack this property. Specifically, our analysis shows that the energy barrier of LDPC HHGP codes is lower bounded by the distance of the underlying classical codes. This bound is tight if the underlying classical codes exhibit system size-dependent distances but constant energy barriers, like 3D and 4D toric codes.

## Abelian multi-cycle codes for single-shot error correction

- **Status**: ❌
- **Reason**: 양자 LDPC(QHP/스태빌라이저/토릭) 양자 전용 구성, 고전 바이너리 이식 기법 없음
- **ID**: arxiv:2506.16910v3
- **Type**: preprint
- **Published**: 2025-06-20
- **Authors**: Hsiang-Ku Lin, Pak Kau Lim, Alexey A. Kovalev +1
- **PDF**: https://arxiv.org/pdf/2506.16910v3
- **Abstract**: We construct a family of quantum low-density parity-check codes locally equivalent to higher-dimensional quantum hypergraph-product (QHP) codes. Similarly to QHP codes, the proposed codes have highly redundant sets of low-weight stabilizer generators, which improves decoding accuracy in a fault-tolerant regime and gives them single-shot properties. The advantage of the new construction is that it gives shorter codes. We derive simple expressions for the dimension of the proposed codes in two important special cases, give bounds on the distances, and explicitly construct some relatively short codes. Circuit simulations for codes locally equivalent to 4-dimensional toric codes show a (pseudo)threshold close to 1.1%, better than for toric or surface codes with a similar noise model.

## Quantum Error Correction Exploiting Degeneracy to Approach the Hashing Bound

- **Status**: ❌
- **Reason**: 양자 EC + 고차 Galois field(비이진) LDPC + 축퇴 활용 — 비이진·양자 모두 제외 대상
- **ID**: arxiv:2506.15636v1
- **Type**: preprint
- **Published**: 2025-06-18
- **Authors**: Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2506.15636v1
- **Abstract**: Quantum error correction is essential for realizing scalable quantum computation. Among various approaches, low-density parity-check codes over higher-order Galois fields have shown promising performance due to their structured sparsity and compatibility with iterative decoding algorithms whose computational complexity scales linearly with the number of physical qubits. In this work, we demonstrate that explicitly exploiting the degeneracy of quantum errors can significantly enhance the decoding performance. Simulation results over the depolarizing channel indicate that the proposed method, at a coding rate of 1/3, achieves a frame error rate as low as $10^{-4}$ at a physical error rate of 9.45% for a code with 104,000 logical qubits and 312,000 physical qubits, approaching the quantum hashing bound. These findings highlight the critical role of degeneracy in closing the gap to the fundamental limits of quantum error correction.

## Tour de gross: A modular quantum computer based on bivariate bicycle codes

- **Status**: ❌
- **Reason**: 양자 LDPC(bivariate bicycle) 모듈러 양자컴퓨터, 양자 전용
- **ID**: arxiv:2506.03094v1
- **Type**: preprint
- **Published**: 2025-06-03
- **Authors**: Theodore J. Yoder, Eddie Schoute, Patrick Rall +5
- **PDF**: https://arxiv.org/pdf/2506.03094v1
- **Abstract**: We present the bicycle architecture, a modular quantum computing framework based on high-rate, low-overhead quantum LDPC codes identified in prior work. For two specific bivariate bicycle codes with distances 12 and 18, we construct explicit fault-tolerant logical instruction sets and estimate the logical error rate of the instructions under circuit noise. We develop a compilation strategy adapted to the constraints of the bicycle architecture, enabling large-scale universal quantum circuit execution. Integrating these components, we perform end-to-end resource estimates demonstrating that an order of magnitude larger logical circuits can be implemented with a given number of physical qubits on the bicycle architecture than on surface code architectures. We anticipate further improvements through advances in code constructions, circuit designs, and compilation techniques.

## Stratified Cohomological Quantum Codes via Colimits in Ch(R)

- **Status**: ❌
- **Reason**: 양자 스태빌라이저/CSS·qudit 코드 구성, 양자 전용 개념 의존
- **ID**: arxiv:2509.06958v1
- **Type**: preprint
- **Published**: 2025-06-03
- **Authors**: William Boone Samuels
- **PDF**: https://arxiv.org/pdf/2509.06958v1
- **Abstract**: We introduce \emph{stratified colimit codes}: stabiliser codes obtained by taking the degree-wise colimit $\mathcal C_\bullet(X):=\operatorname*{colim}_{σ\in X}F(σ)$ of a functor $F\colon X\to\mathbf{Ch}(R)$ from a finite poset into the category of chain complexes over a commutative ring~$R$. Axioms requiring only transitivity and boundary-compatibility of the morphisms in $F$ ensure that $\partial^2=0$, so the homology $H_\bullet$ and cohomology $H^\bullet$ furnish the usual CSS $Z$- and $X$-type logical sectors; torsion in $H_\bullet$ classifies qudit charges via the universal coefficient sequence. Varying $F$ recovers classical surface and color codes, $\mathbb{RP}^2$ torsion codes, twisted toric families with rate $k\sim d$, and X-cube style fracton models, all without referencing an ambient cell complex. Matrix Smith normal form (PID case) and sparse Gaussian elimination (field case) compute $H_\bullet$ directly, giving LDPC parameters that inherit the sparsity of $F$. Because the construction is ring agnostic and functorial, it extends naturally to code surgery (push-outs) and, at the next categorical level, to bicomplex domain walls. Stratified colimit codes therefore supply a concise algebraic chassis for designing, classifying, and decoding topological and fractal quantum codes without ever drawing a lattice.
