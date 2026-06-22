# arXiv — 2024-10


## Testing Tensor Products of Algebraic Codes

- **Status**: ❌
- **Reason**: 텐서곱 대수기하 부호의 local testability 순수 이론 — 양자 LDPC 동기, 디코더/HW로 안 이어지는 이론 bound
- **ID**: arxiv:2410.22606v2
- **Type**: preprint
- **Published**: 2024-10-30
- **Authors**: Sumegha Garg, Madhu Sudan, Gabriel Wu
- **PDF**: https://arxiv.org/pdf/2410.22606v2
- **Abstract**: Motivated by recent advances in locally testable codes and quantum LDPCs based on robust testability of tensor product codes, we explore the local testability of tensor products of (an abstraction of) algebraic geometry codes. Such codes are parameterized by, in addition to standard parameters such as block length $n$ and dimension $k$, their genus $g$. We show that the tensor product of two algebraic geometry codes is robustly locally testable provided $n = Ω((k+g)^2)$. Apart from Reed-Solomon codes, this seems to be the first explicit family of two-wise tensor codes of high dual distance that is robustly locally testable by the natural test that measures the expected distance of a random row/column from the underlying code.

## Quantum LDPC Codes with Transversal Non-Clifford Gates via Products of Algebraic Codes

- **Status**: ❌
- **Reason**: transversal non-Clifford 게이트 지원 양자 LDPC 구성 — 양자 전용(스태빌라이저/magic state) 의존, 원칙 제외
- **ID**: arxiv:2410.14662v1
- **Type**: preprint
- **Published**: 2024-10-18
- **Authors**: Louis Golowich, Ting-Chun Lin
- **PDF**: https://arxiv.org/pdf/2410.14662v1
- **Abstract**: For every integer $r\geq 2$ and every $ε>0$, we construct an explicit infinite family of quantum LDPC codes supporting a transversal $C^{r-1}Z$ gate with length $N$, dimension $K\geq N^{1-ε}$, distance $D\geq N^{1/r}/\operatorname{poly}(\log N)$, and stabilizer weight $w\leq\operatorname{poly}(\log N)$. The previous state of the art construction (in most parameter regimes) was the $r$-dimensional color code, which has only constant dimension $K=O(1)$, and otherwise has the same parameters up to polylogarithmic factors. Our construction provides the first known codes with low-weight stabilizers that are capable of magic state distillation with arbitrarily small yield parameter $γ=\log(N/K)/\log(D)>0$.   A classical analogue of transversal $C^{r-1}Z$ gates is given by the multiplication property, which requires component-wise products of classical codewords to belong to another similar code. As a byproduct of our techniques, we also obtain a new construction of classical locally testable codes with such a multiplication property.   We construct our codes as products of chain complexes associated to classical LDPC codes, which in turn we obtain by imposing local Reed-Solomon codes on a specific spectral expander that we construct. We prove that our codes support the desired transversal $C^{r-1}Z$ gates by using the multiplication property to combine local circuits based on the topological structure.

## Transversal non-Clifford gates for quantum LDPC codes on sheaves

- **Status**: ❌
- **Reason**: sheaf 기반 양자 LDPC의 transversal non-Clifford 게이트 — 양자 전용 개념 의존, 원칙 제외
- **ID**: arxiv:2410.14631v1
- **Type**: preprint
- **Published**: 2024-10-18
- **Authors**: Ting-Chun Lin
- **PDF**: https://arxiv.org/pdf/2410.14631v1
- **Abstract**: A major goal in quantum computing is to build a fault-tolerant quantum computer. One approach involves quantum low-density parity-check (qLDPC) codes that support transversal non-Clifford gates. In this work, we provide a large family of such codes. The key insight is to interpret the logical operators of qLDPC codes as geometric surfaces and use the intersection number of these surfaces to define the non-Clifford operation. At a more abstract level, this construction is based on defining the cup product on the chain complex induced from a sheaf.

## Operator algebra and algorithmic construction of boundaries and defects in (2+1)D topological Pauli stabilizer codes

- **Status**: ❌
- **Reason**: (2+1)D 양자 Pauli 스태빌라이저 부호의 경계/결함 구성 — qudit 양자 EC, 양자 전용 개념 의존, 원칙 제외
- **ID**: arxiv:2410.11942v5
- **Type**: preprint
- **Published**: 2024-10-15
- **Authors**: Zijian Liang, Bowen Yang, Joseph T. Iosue +1
- **PDF**: https://arxiv.org/pdf/2410.11942v5
- **Abstract**: Quantum low-density parity-check codes, such as the Kitaev toric code and bivariate bicycle codes, are often defined with periodic boundary conditions, which are difficult to realize in physical systems. In this paper, we present an algorithm for constructing all gapped boundaries and defects of two-dimensional Pauli stabilizer codes. Using the operator algebra formalism, we establish a one-to-one correspondence between the topological data, such as anyon fusion rules and topological spins, of two-dimensional bulk stabilizer codes and one-dimensional boundary anomalous subsystem codes. To make the operator algebra computationally accessible, we adapt Laurent polynomials and convert the tasks into matrix operations, e.g., the Hermite normal form for obtaining boundary anyons and the Smith normal form for determining fusion rules. This approach enables computers to automatically generate all possible gapped boundaries and defects for topological Pauli stabilizer codes through boundary anyon condensation and topological order completion. This streamlines the analysis of surface codes and associated logical operations for fault-tolerant quantum computation. Our algorithm applies to $\mathbb{Z}_d$ qudits for both prime and nonprime $d$, enabling exploration of topological phases beyond the Kitaev toric code. We have applied the algorithm and explicitly demonstrated the lattice constructions of 2 boundaries and 6 defects in the $\mathbb{Z}_2$ toric code, 3 boundaries and 22 defects in the $\mathbb{Z}_4$ toric code, 1 boundary and 2 defects in the double semion code, 1 boundary and 22 defects in the six-semion code, 6 boundaries and 270 defects in the color code, and 6 defects in the anomalous three-fermion code. Finally, we study the boundaries of bivariate bicycle codes, showing that they exhibit large logical dimensions and anyons with long translation periods.

## Collision Diversity SCRAM: Beyond the Sphere-Packing Bound

- **Status**: ❌
- **Reason**: 6G NOMA용 SCRAM 다중접속 정보이론 기법, LDPC는 베이스라인 — 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: arxiv:2410.07887v1
- **Type**: preprint
- **Published**: 2024-10-10
- **Authors**: Sally Nafie, Joerg Robert, Albert Heuberger
- **PDF**: https://arxiv.org/pdf/2410.07887v1
- **Abstract**: This paper presents a novel scheme dubbed Collision Diversity (CoD) SCRAM, which is provisioned to meet the challenging requirements of the future 6G, portrayed in massive connectivity, reliability, and ultra-low latency. The conventional SCRAM mechanism, which stands for Slotted Coded Random Access Multiplexing, is a hybrid decoding scheme, that jointly resolves collisions and decodes the Low Density Parity Check (LDPC) codewords, in a similar analogy to Belief Propagation (BP) decoding on a joint three-layer Tanner graph. The CoD SCRAM proposed herein tends to enhance the performance of SCRAM by adopting an information-theoretic approach that tends to maximize the attainable Spectral Efficiency. Besides, due to the analogy between the two-layer Tanner graph of classical LDPC codes, and the three-layer Tanner graph of SCRAM, the CoD SCRAM adopts the well-developed tools utilized to design powerful LDPC codes. Finally, the proposed CoD scheme tends to leverage the collisions among the users in order to induce diversity. Results show that the proposed CoD SCRAM scheme surpasses the conventional SCRAM scheme, which is superior to the state-of-the-art Non-Orthogonal Multiple Access (NOMA) schemes. Additionally, by leveraging the collisions, the CoD SCRAM tends to surpass the Sphere-Packing Bound (SPB) at the respective information block length of the underlying LDPC codes of the accommodated users.

## Spectrally Efficient LDPC Codes For IRIG-106 Waveforms via Random Puncturing

- **Status**: ❌
- **Reason**: IRIG-106 텔레메트리 파형용 LDPC 랜덤 펑처링, 무선 응용 특이적 — 기존 코드 적용 수준, 새 ECC 기법 없음
- **ID**: arxiv:2410.05844v1
- **Type**: preprint
- **Published**: 2024-10-08
- **Authors**: Andrew D. Cummins, David G. M. Mitchell, Erik Perrins
- **PDF**: https://arxiv.org/pdf/2410.05844v1
- **Abstract**: Low-density parity-check (LDPC) codes form part of the IRIG-106 standard and have been successfully deployed for the Telemetry Group version of shaped-offset quadrature phase shift keying (SOQPSK-TG) modulation. Recently, LDPC code solutions have been proposed and optimized for continuous phase modulations (CPMs), including the pulse code modulation/frequency modulation (PCM/FM) and the multi-h CPM developed by the Advanced Range TeleMetry program (ARTM CPM). These codes were shown to perform around one dB from the respective channel capacities of these modulations. In this paper, we consider the effect of random puncturing of these LDPC codes to further improve spectrum efficiency. We present numerical simulation results that affirm the robust decoding performance promised by LDPC codes designed for ARTM CPM.

## Single-shot preparation of hypergraph product codes via dimension jump

- **Status**: ❌
- **Reason**: 양자 하이퍼그래프곱 코드 single-shot 준비(dimension jump), 양자 전용 개념(codespace·stabilizer) 의존 — 양자 EC 제외
- **ID**: arxiv:2410.05171v2
- **Type**: preprint
- **Published**: 2024-10-07
- **Authors**: Yifan Hong
- **PDF**: https://arxiv.org/pdf/2410.05171v2
- **Abstract**: Quantum error correction is a fundamental primitive of fault-tolerant quantum computing. But in order for error correction to proceed, one must first prepare the codespace of the underlying error-correcting code. A popular method for encoding quantum low-density parity-check codes is transversal initialization, where one begins in a product state and measures a set of stabilizer generators. In the presence of measurement errors however, this procedure is generically not fault-tolerant, and so one typically needs to repeat the measurements many times, resulting in a deep initialization circuit. We present a protocol that prepares the codespace of constant-rate hypergraph product codes in constant depth with $O(\sqrt{n})$ spatial overhead, and we show that the protocol is robust even in the presence of measurement errors. Our construction is inspired by dimension-jumping in topological codes and leverages two properties that arise from the homological product of codes. We provide some improvements to lower the spatial overhead and discuss applications to fault-tolerant architectures.

## Universal adapters between quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC 간 어댑터·logical Pauli 측정, 양자 전용 개념 의존 — 양자 EC 제외
- **ID**: arxiv:2410.03628v4
- **Type**: preprint
- **Published**: 2024-10-04
- **Authors**: Esha Swaroop, Tomas Jochym-O'Connor, Theodore J. Yoder
- **PDF**: https://arxiv.org/pdf/2410.03628v4
- **Abstract**: We propose the repetition code adapter as a way to perform joint logical Pauli measurements within a quantum low-density parity check (LDPC) codeblock or between separate such codeblocks, thus providing a flexible tool for fault-tolerant computation with quantum LDPC codes. This adapter is universal in the sense that it works regardless of the LDPC codes involved and the logical Paulis being measured. The construction achieves joint logical Pauli measurement of $t$ weight $O(d)$ operators using $O(d)$ time and $\tilde O(td)$ additional qubits and checks, up to a factor polylogarithmic in $d$. As a special case, for some geometrically-local codes in fixed $D\ge2$ dimensions, only $O(td)$ additional qubits and checks are required instead. By extending the adapter in the case $t=2$, we also construct a toric code adapter that uses $O(d^2)$ additional qubits and checks to perform addressable logical CNOT gates on arbitrary LDPC codes via Dehn twists. To obtain these results, we develop a novel weaker form of graph edge expansion and the $\mathsf{SkipTree}$ algorithm, which ensures a sparse transformation between different weight-2 check bases for the classical repetition code.
