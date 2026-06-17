# arXiv — 2024-10


## A Comparative Study of Ensemble Decoding Methods for Short Length LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.23980v1
- **Type**: preprint
- **Published**: 2024-10-31
- **Authors**: Felix Krieg, Jannis Clausius, Marvin Geiselhart +1
- **PDF**: https://arxiv.org/pdf/2410.23980v1
- **Abstract**: To alleviate the suboptimal performance of belief propagation (BP) decoding of short low-density parity-check (LDPC) codes, a plethora of improved decoding algorithms has been proposed over the last two decades. Many of these methods can be described using the same general framework, which we call ensemble decoding: A set of independent constituent decoders works in parallel on the received sequence, each proposing a codeword candidate. From this list, the maximum likelihood (ML) decision is designated as the decoder output. In this paper, we qualitatively and quantitatively compare different realizations of the ensemble decoder, namely multiple-bases belief propagation (MBBP), automorphism ensemble decoding (AED), scheduling ensemble decoding (SED), noise-aided ensemble decoding (NED) and saturated belief propagation (SBP). While all algorithms can provide gains over traditional BP decoding, ensemble methods that exploit the code structure, such as MBBP and AED, typically show greater performance improvements.

## KALAM: toolKit for Automating high-Level synthesis of Analog computing systeMs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.22946v1
- **Type**: preprint
- **Published**: 2024-10-30
- **Authors**: Ankita Nandi, Krishil Gandhi, Mahendra Pratap Singh +2
- **PDF**: https://arxiv.org/pdf/2410.22946v1
- **Abstract**: Diverse computing paradigms have emerged to meet the growing needs for intelligent energy-efficient systems. The Margin Propagation (MP) framework, being one such initiative in the analog computing domain, stands out due to its scalability across biasing conditions, temperatures, and diminishing process technology nodes. However, the lack of digital-like automation tools for designing analog systems (including that of MP analog) hinders their adoption for designing large systems. The inherent scalability and modularity of MP systems present a unique opportunity in this regard. This paper introduces KALAM (toolKit for Automating high-Level synthesis of Analog computing systeMs), which leverages factor graphs as the foundational paradigm for synthesizing MP-based analog computing systems. Factor graphs are the basis of various signal processing tasks and, when coupled with MP, can be used to design scalable and energy-efficient analog signal processors. Using Python scripting language, the KALAM automation flow translates an input factor graph to its equivalent SPICE-compatible circuit netlist that can be used to validate the intended functionality. KALAM also allows the integration of design optimization strategies such as precision tuning, variable elimination, and mathematical simplification. We demonstrate KALAM's versatility for tasks such as Bayesian inference, Low-Density Parity Check (LDPC) decoding, and Artificial Neural Networks (ANN). Simulation results of the netlists align closely with software implementations, affirming the efficacy of our proposed automation tool.

## Testing Tensor Products of Algebraic Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.22606v2
- **Type**: preprint
- **Published**: 2024-10-30
- **Authors**: Sumegha Garg, Madhu Sudan, Gabriel Wu
- **PDF**: https://arxiv.org/pdf/2410.22606v2
- **Abstract**: Motivated by recent advances in locally testable codes and quantum LDPCs based on robust testability of tensor product codes, we explore the local testability of tensor products of (an abstraction of) algebraic geometry codes. Such codes are parameterized by, in addition to standard parameters such as block length $n$ and dimension $k$, their genus $g$. We show that the tensor product of two algebraic geometry codes is robustly locally testable provided $n = Ω((k+g)^2)$. Apart from Reed-Solomon codes, this seems to be the first explicit family of two-wise tensor codes of high dual distance that is robustly locally testable by the natural test that measures the expected distance of a random row/column from the underlying code.

## Quantum LDPC Codes with Transversal Non-Clifford Gates via Products of Algebraic Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.14662v1
- **Type**: preprint
- **Published**: 2024-10-18
- **Authors**: Louis Golowich, Ting-Chun Lin
- **PDF**: https://arxiv.org/pdf/2410.14662v1
- **Abstract**: For every integer $r\geq 2$ and every $ε>0$, we construct an explicit infinite family of quantum LDPC codes supporting a transversal $C^{r-1}Z$ gate with length $N$, dimension $K\geq N^{1-ε}$, distance $D\geq N^{1/r}/\operatorname{poly}(\log N)$, and stabilizer weight $w\leq\operatorname{poly}(\log N)$. The previous state of the art construction (in most parameter regimes) was the $r$-dimensional color code, which has only constant dimension $K=O(1)$, and otherwise has the same parameters up to polylogarithmic factors. Our construction provides the first known codes with low-weight stabilizers that are capable of magic state distillation with arbitrarily small yield parameter $γ=\log(N/K)/\log(D)>0$.   A classical analogue of transversal $C^{r-1}Z$ gates is given by the multiplication property, which requires component-wise products of classical codewords to belong to another similar code. As a byproduct of our techniques, we also obtain a new construction of classical locally testable codes with such a multiplication property.   We construct our codes as products of chain complexes associated to classical LDPC codes, which in turn we obtain by imposing local Reed-Solomon codes on a specific spectral expander that we construct. We prove that our codes support the desired transversal $C^{r-1}Z$ gates by using the multiplication property to combine local circuits based on the topological structure.

## Transversal non-Clifford gates for quantum LDPC codes on sheaves

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.14631v1
- **Type**: preprint
- **Published**: 2024-10-18
- **Authors**: Ting-Chun Lin
- **PDF**: https://arxiv.org/pdf/2410.14631v1
- **Abstract**: A major goal in quantum computing is to build a fault-tolerant quantum computer. One approach involves quantum low-density parity-check (qLDPC) codes that support transversal non-Clifford gates. In this work, we provide a large family of such codes. The key insight is to interpret the logical operators of qLDPC codes as geometric surfaces and use the intersection number of these surfaces to define the non-Clifford operation. At a more abstract level, this construction is based on defining the cup product on the chain complex induced from a sheaf.

## Study of Weighted Residual Layered Belief Propagation for Decoding of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.13131v1
- **Type**: preprint
- **Published**: 2024-10-17
- **Authors**: H. Touati, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2410.13131v1
- **Abstract**: In this work, we investigate the decoding of Low-Density Parity-Check (LDPC) codes using informed dynamic scheduling algorithms that require a reduced number of iterations. In particular, we devise the weighted residual layered belief propagation (WR-LBP) decoding algorithm, which exploits the residual within a structured layer framework to speed the number of required decoding iterations. The proposed WR-LBP algorithm is assessed against important LDPC decoding algorithms, in terms of the number of iterations required for convergence and the bit error rates.

## Operator algebra and algorithmic construction of boundaries and defects in (2+1)D topological Pauli stabilizer codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.11942v5
- **Type**: preprint
- **Published**: 2024-10-15
- **Authors**: Zijian Liang, Bowen Yang, Joseph T. Iosue +1
- **PDF**: https://arxiv.org/pdf/2410.11942v5
- **Abstract**: Quantum low-density parity-check codes, such as the Kitaev toric code and bivariate bicycle codes, are often defined with periodic boundary conditions, which are difficult to realize in physical systems. In this paper, we present an algorithm for constructing all gapped boundaries and defects of two-dimensional Pauli stabilizer codes. Using the operator algebra formalism, we establish a one-to-one correspondence between the topological data, such as anyon fusion rules and topological spins, of two-dimensional bulk stabilizer codes and one-dimensional boundary anomalous subsystem codes. To make the operator algebra computationally accessible, we adapt Laurent polynomials and convert the tasks into matrix operations, e.g., the Hermite normal form for obtaining boundary anyons and the Smith normal form for determining fusion rules. This approach enables computers to automatically generate all possible gapped boundaries and defects for topological Pauli stabilizer codes through boundary anyon condensation and topological order completion. This streamlines the analysis of surface codes and associated logical operations for fault-tolerant quantum computation. Our algorithm applies to $\mathbb{Z}_d$ qudits for both prime and nonprime $d$, enabling exploration of topological phases beyond the Kitaev toric code. We have applied the algorithm and explicitly demonstrated the lattice constructions of 2 boundaries and 6 defects in the $\mathbb{Z}_2$ toric code, 3 boundaries and 22 defects in the $\mathbb{Z}_4$ toric code, 1 boundary and 2 defects in the double semion code, 1 boundary and 22 defects in the six-semion code, 6 boundaries and 270 defects in the color code, and 6 defects in the anomalous three-fermion code. Finally, we study the boundaries of bivariate bicycle codes, showing that they exhibit large logical dimensions and anyons with long translation periods.

## A Combinatorial Approach to Avoiding Weak Keys in the BIKE Cryptosystem

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.11111v2
- **Type**: preprint
- **Published**: 2024-10-14
- **Authors**: Gretchen L Matthews, Emily McMillon
- **PDF**: https://arxiv.org/pdf/2410.11111v2
- **Abstract**: Bit Flipping Key Encapsulation (BIKE) is a code-based cryptosystem that was considered in Round 4 of the NIST Post-Quantum Cryptography Standardization process. It is based on quasi-cyclic moderate-density parity-check (QC-MDPC) codes paired with an iterative decoder. While (low-density) parity-check codes have been shown to perform well in practice, their capabilities are governed by the code's graphical representation and the choice of decoder rather than the traditional code parameters, making it difficult to determine the decoder failure rate (DFR). Moreover, decoding failures have been demonstrated to lead to attacks that recover the BIKE private key. In this paper, we demonstrate a strong correlation between weak keys and $4$-cycles in their associated Tanner graphs. We give concrete ways to enumerate the number of 4-cycles in a BIKE key and use these results to present a filtering algorithm that will filter BIKE keys with large numbers of 4-cycles. These results also apply to more general parity check codes.

## A Graphical Correlation-Based Method for Counting the Number of Global 8-Cycles on the SCRAM Three-Layer Tanner Graph

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.07998v1
- **Type**: preprint
- **Published**: 2024-10-10
- **Authors**: Sally Nafie, Joerg Robert, Albert Heuberger
- **PDF**: https://arxiv.org/pdf/2410.07998v1
- **Abstract**: This paper presents a novel graphical approach that counts the number of global 8-cycles on the SCRAM three-layer Tanner graph. SCRAM, which stands for Slotted Coded Random Access Multiplexing, is a joint decoder that is meets challenging requirements of 6G. At the transmitter side, the data of the accommodated users is encoded by Low Density Parity Check (LDPC) codes, and the codewords are transmitted over the shared channel by means of Slotted ALOHA. Unlike the state-of-the-art sequential decoders, the SCRAM decoder jointly resolves collisions and decodes the LDPC codewords, in a similar analogy to Belief Propagation on a three-layer Tanner graph. By leveraging the analogy between the two-layer Tanner graph of conventional LDPC codes and the three-layer Tanner graph of SCRAM, the well-developed analysis tools of classical LDPC codes could be utilized to enhance the performance of SCRAM. In essence, the contribution of this paper is three-fold; First it proposes the methodology to utilize these tools to assess the performance of SCRAM. Second, it derives a lower bound on the shortest cycle length of an arbitrary SCRAM Tanner graph. Finally, the paper presents a novel graphical method that counts the number of cycles of length that corresponds to the girth.

## Collision Diversity SCRAM: Beyond the Sphere-Packing Bound

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.07887v1
- **Type**: preprint
- **Published**: 2024-10-10
- **Authors**: Sally Nafie, Joerg Robert, Albert Heuberger
- **PDF**: https://arxiv.org/pdf/2410.07887v1
- **Abstract**: This paper presents a novel scheme dubbed Collision Diversity (CoD) SCRAM, which is provisioned to meet the challenging requirements of the future 6G, portrayed in massive connectivity, reliability, and ultra-low latency. The conventional SCRAM mechanism, which stands for Slotted Coded Random Access Multiplexing, is a hybrid decoding scheme, that jointly resolves collisions and decodes the Low Density Parity Check (LDPC) codewords, in a similar analogy to Belief Propagation (BP) decoding on a joint three-layer Tanner graph. The CoD SCRAM proposed herein tends to enhance the performance of SCRAM by adopting an information-theoretic approach that tends to maximize the attainable Spectral Efficiency. Besides, due to the analogy between the two-layer Tanner graph of classical LDPC codes, and the three-layer Tanner graph of SCRAM, the CoD SCRAM adopts the well-developed tools utilized to design powerful LDPC codes. Finally, the proposed CoD scheme tends to leverage the collisions among the users in order to induce diversity. Results show that the proposed CoD SCRAM scheme surpasses the conventional SCRAM scheme, which is superior to the state-of-the-art Non-Orthogonal Multiple Access (NOMA) schemes. Additionally, by leveraging the collisions, the CoD SCRAM tends to surpass the Sphere-Packing Bound (SPB) at the respective information block length of the underlying LDPC codes of the accommodated users.

## Spectrally Efficient LDPC Codes For IRIG-106 Waveforms via Random Puncturing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.05844v1
- **Type**: preprint
- **Published**: 2024-10-08
- **Authors**: Andrew D. Cummins, David G. M. Mitchell, Erik Perrins
- **PDF**: https://arxiv.org/pdf/2410.05844v1
- **Abstract**: Low-density parity-check (LDPC) codes form part of the IRIG-106 standard and have been successfully deployed for the Telemetry Group version of shaped-offset quadrature phase shift keying (SOQPSK-TG) modulation. Recently, LDPC code solutions have been proposed and optimized for continuous phase modulations (CPMs), including the pulse code modulation/frequency modulation (PCM/FM) and the multi-h CPM developed by the Advanced Range TeleMetry program (ARTM CPM). These codes were shown to perform around one dB from the respective channel capacities of these modulations. In this paper, we consider the effect of random puncturing of these LDPC codes to further improve spectrum efficiency. We present numerical simulation results that affirm the robust decoding performance promised by LDPC codes designed for ARTM CPM.

## Single-shot preparation of hypergraph product codes via dimension jump

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.05171v2
- **Type**: preprint
- **Published**: 2024-10-07
- **Authors**: Yifan Hong
- **PDF**: https://arxiv.org/pdf/2410.05171v2
- **Abstract**: Quantum error correction is a fundamental primitive of fault-tolerant quantum computing. But in order for error correction to proceed, one must first prepare the codespace of the underlying error-correcting code. A popular method for encoding quantum low-density parity-check codes is transversal initialization, where one begins in a product state and measures a set of stabilizer generators. In the presence of measurement errors however, this procedure is generically not fault-tolerant, and so one typically needs to repeat the measurements many times, resulting in a deep initialization circuit. We present a protocol that prepares the codespace of constant-rate hypergraph product codes in constant depth with $O(\sqrt{n})$ spatial overhead, and we show that the protocol is robust even in the presence of measurement errors. Our construction is inspired by dimension-jumping in topological codes and leverages two properties that arise from the homological product of codes. We provide some improvements to lower the spatial overhead and discuss applications to fault-tolerant architectures.

## Universal adapters between quantum LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2410.03628v4
- **Type**: preprint
- **Published**: 2024-10-04
- **Authors**: Esha Swaroop, Tomas Jochym-O'Connor, Theodore J. Yoder
- **PDF**: https://arxiv.org/pdf/2410.03628v4
- **Abstract**: We propose the repetition code adapter as a way to perform joint logical Pauli measurements within a quantum low-density parity check (LDPC) codeblock or between separate such codeblocks, thus providing a flexible tool for fault-tolerant computation with quantum LDPC codes. This adapter is universal in the sense that it works regardless of the LDPC codes involved and the logical Paulis being measured. The construction achieves joint logical Pauli measurement of $t$ weight $O(d)$ operators using $O(d)$ time and $\tilde O(td)$ additional qubits and checks, up to a factor polylogarithmic in $d$. As a special case, for some geometrically-local codes in fixed $D\ge2$ dimensions, only $O(td)$ additional qubits and checks are required instead. By extending the adapter in the case $t=2$, we also construct a toric code adapter that uses $O(d^2)$ additional qubits and checks to perform addressable logical CNOT gates on arbitrary LDPC codes via Dehn twists. To obtain these results, we develop a novel weaker form of graph edge expansion and the $\mathsf{SkipTree}$ algorithm, which ensures a sparse transformation between different weight-2 check bases for the classical repetition code.
