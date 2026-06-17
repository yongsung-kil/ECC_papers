# arXiv — 2025-02


## Quantum low-density parity-check codes for erasure-biased atomic quantum processors

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.20189v2
- **Type**: preprint
- **Published**: 2025-02-27
- **Authors**: Laura Pecorari, Guido Pupillo
- **PDF**: https://arxiv.org/pdf/2502.20189v2
- **Abstract**: Identifying the best families of quantum error correction (QEC) codes for near-term experiments is key to enabling fault-tolerant quantum computing. Ideally, such codes should have low overhead in qubit number, high physical error thresholds, and moderate requirements on qubit connectivity to simplify experiments, while allowing for high logical error suppression. Quantum Low-Density Parity-Check (LDPC) codes have been recently shown to provide a path towards QEC with low qubit overhead and small logical error probabilities. Here, we demonstrate that when the dominant errors are erasures -- as can be engineered in different quantum computing architectures -- quantum LDPC codes additionally provide high thresholds and even stronger logical error suppression in parameter regimes that are accessible to current experiments. Using large-scale QEC numerical simulations, we benchmark the performance of two families of high-rate quantum LDPC codes, namely Clifford-deformed La-cross codes and Bivariate Bicycle codes, under a noise model strongly biased towards erasure errors. Both codes outperform the surface code by offering up to orders of magnitude lower logical error probabilities. Interestingly, we find that this decrease in the logical error probability may not be accompanied by an increase in the code threshold, as different QEC codes benefit differently from large erasure fractions. While here we focus on neutral atom qubits, the results also hold for other quantum platforms, such as trapped ions and superconducting qubits, for which erasure conversion has been demonstrated.

## Existence and Characterisation of Bivariate Bicycle Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.17052v4
- **Type**: preprint
- **Published**: 2025-02-24
- **Authors**: Jasper Johannes Postema, Servaas J. J. M. F. Kokkelmans
- **PDF**: https://arxiv.org/pdf/2502.17052v4
- **Abstract**: Encoding quantum information in a quantum error correction (QEC) code offers protection against decoherence and enhances the fidelity of qubits and gate operations. One of the fundamental challenges of QEC is to construct codes with asymptotically good parameters, i.e. a non-vanishing rate and relative minimum distance. Such codes provide compact quantum memory with low overhead and enhanced error correcting capabilities, compared to state-of-the-art topological error correction codes such as the surface or colour codes. Recently, bivariate bicycle (BB) codes have emerged as a promising candidate for such compact memory, though the exact tradeoff of the code parameters $[[n,k,d]]$ remained unknown. In this Article, we explore these codes by leveraging their ring structure, and predict their dimension as well as conditions on their existence. Finally, we highlight asymptotic badness. Though this excludes this subclass of codes from the search towards practical good low-density parity check (LDPC) codes, it does not affect the utility of the moderately long codes that are known, which can already be used to experimentally demonstrate better QEC beyond the surface code.

## Decision-tree decoders for general quantum LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.16408v1
- **Type**: preprint
- **Published**: 2025-02-23
- **Authors**: Kai R. Ott, Bence Hetényi, Michael E. Beverland
- **PDF**: https://arxiv.org/pdf/2502.16408v1
- **Abstract**: We introduce Decision Tree Decoders (DTDs), which rely only on the sparsity of the binary check matrix, making them broadly applicable for decoding any quantum low-density parity-check (qLDPC) code and fault-tolerant quantum circuits. DTDs construct corrections incrementally by adding faults one-by-one, forming a path through a Decision Tree (DT). Each DTD algorithm is defined by its strategy for exploring the tree, with well-designed algorithms typically needing to explore only a small portion before finding a correction. We propose two explicit DTD algorithms that can be applied to any qLDPC code: (1) A provable decoder: Guaranteed to find a minimum-weight correction. While it can be slow in the worst case, numerical results show surprisingly fast median-case runtime, exploring only $w$ DT nodes to find a correction for weight-$w$ errors in notable qLDPC codes, such as bivariate bicycle and color codes. This decoder may be useful for ensemble decoding and determining provable code distances, and can be adapted to compute all minimum-weight logical operators of a code. (2) A heuristic decoder: Achieves higher accuracy and faster performance than BP-OSD on the gross code with circuit noise in realistic parameter regimes.

## Non-Binary LDPC Arithmetic Error Correction For Processing-in-Memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.11487v1
- **Type**: preprint
- **Published**: 2025-02-17
- **Authors**: Daijing Shi, Yihang Zhu, Anjunyi Fan +3
- **PDF**: https://arxiv.org/pdf/2502.11487v1
- **Abstract**: Processing-in-memory (PIM) based on emerging devices such as memristors is more vulnerable to noise than traditional memories, due to the physical non-idealities and complex operations in analog domains. To ensure high reliability, efficient error-correcting code (ECC) is highly desired. However, state-of-the-art ECC schemes for PIM suffer drawbacks including dataflow interruptions, low code rates, and limited error correction patterns. In this work, we propose non-binary low-density parity-check (NB-LDPC) error correction running over the Galois field. Such NB-LDPC scheme with a long word length of 1024 bits can correct up to 8-bit errors with a code rate over 88%. Nonbinary GF operations can support both memory mode and PIM mode even with multi-level memory cells. We fabricate a 40nm prototype PIM chip equipped with our proposed NB-LDPC scheme for validation purposes. Experiments show that PIM with NB-LDPC error correction demonstrates up to 59.65 times bit error rate (BER) improvement over the original PIM without such error correction. The test chip delivers 2.978 times power efficiency enhancement over prior works.

## Demystifying 5G Polar and LDPC Codes: A Comprehensive Review and Foundations

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.11053v3
- **Type**: preprint
- **Published**: 2025-02-16
- **Authors**: Mody Sy
- **PDF**: https://arxiv.org/pdf/2502.11053v3
- **Abstract**: Understanding how 5G networks correct errors is no trivial matter. At the heart of the process lie two sophisticated families of codes: LDPC and polar codes. This paper opens the black box, not only by explaining how these codes are designed, but also by showing how they are encoded and decoded in practice. To map where research currently stands, we present a detailed survey of the literature supplemented with insights that are often buried deep within technical standards. These foundations are not just historical footnotes: they are strong candidates for powering error correction in 6G and beyond. In bringing clarity to these building blocks, we aim to help engineers and researchers navigate what is both a complex and increasingly vital part of wireless communication.

## Semantic Learning for Molecular Communication in Internet of Bio-Nano Things

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.08426v2
- **Type**: preprint
- **Published**: 2025-02-12
- **Authors**: Hanlin Cai, Ozgur B. Akan
- **PDF**: https://arxiv.org/pdf/2502.08426v2
- **Abstract**: Molecular communication (MC) provides a foundational framework for information transmission in the Internet of Bio-Nano Things (IoBNT), where efficiency and reliability are crucial. However, the inherent limitations of molecular channels, such as low transmission rates, noise, and intersymbol interference (ISI), limit their ability to support complex data transmission. This paper proposes an end-to-end semantic learning framework designed to optimize task-oriented molecular communication, with a focus on biomedical diagnostic tasks under resource-constrained conditions. The proposed framework employs a deep encoder-decoder architecture to efficiently extract, quantize, and decode semantic features, prioritizing taskrelevant semantic information to enhance diagnostic classification performance. Additionally, a probabilistic channel network is introduced to approximate molecular propagation dynamics, enabling gradient-based optimization for end-to-end learning. Experimental results demonstrate that the proposed semantic framework improves diagnostic accuracy by at least 25% compared to conventional JPEG compression with LDPC coding methods under resource-constrained communication scenarios.

## Explicit Codes approaching Generalized Singleton Bound using Expanders

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.07308v1
- **Type**: preprint
- **Published**: 2025-02-11
- **Authors**: Fernando Granha Jeronimo, Tushant Mittal, Shashank Srivastava +1
- **PDF**: https://arxiv.org/pdf/2502.07308v1
- **Abstract**: We construct a new family of explicit codes that are list decodable to capacity and achieve an optimal list size of $O(\frac{1}ε)$. In contrast to existing explicit constructions of codes achieving list decoding capacity, our arguments do not rely on algebraic structure but utilize simple combinatorial properties of expander graphs.   Our construction is based on a celebrated distance amplification procedure due to Alon, Edmonds, and Luby [FOCS'95], which transforms any high-rate code into one with near-optimal rate-distance tradeoff. We generalize it to show that the same procedure can be used to transform any high-rate code into one that achieves list decoding capacity. Our proof can be interpreted as a "local-to-global" phenomenon for (a slight strengthening of) the generalized Singleton bound. Using this construction, for every $R, ε\in (0,1)$ and $k \in \mathbb{N}^+$, we obtain an \emph{explicit} family of codes $\mathcal{C} \subseteq Σ^n$, with rate $R$ such that,   - They achieve the $ε$-relaxed generalized Singleton bound: for any $g \in Σ^n$ and any list $\mathcal{H}$ of at most $k$ codewords, we have, \[ \underset{h \in \mathcal{H}}{\mathbb{E}} [Δ(g,h)] ~\geq~ \frac{|\mathcal{H}|-1}{|\mathcal{H}|} \cdot (1 - R - ε). \]   - The alphabet size is a constant depending only on $ε$ and $k$.   - They can be list decoded up to radius $\frac{k-1}{k}(1-R-ε)$, in time $n^{O_{k,ε}(1)}$.   As a corollary of our result, we also obtain the first explicit construction of LDPC codes achieving list decoding capacity, and in fact arbitrarily close to the generalized Singleton bound.

## Practical classical error correction for parity-encoded spin systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.07170v4
- **Type**: preprint
- **Published**: 2025-02-11
- **Authors**: Yoshihiro Nambu
- **PDF**: https://arxiv.org/pdf/2502.07170v4
- **Abstract**: Quantum annealing (QA) has emerged as a promising candidate for fast solvers for combinatorial optimization problems (COPs) and has attracted the interest of many researchers. Since COP is logically encoded in the Ising interaction among spins, its realization necessitates a spin system with all-to-all connectivity, presenting technical challenges in the physical implementation of large-scale QA devices. W. Lechner, P. Hauke, and P. Zoller proposed a parity-encoding (PE) architecture consisting of an expanded spin system with only local connectivity among them to circumvent this difficulty in developing near-future QA devices. They suggested that this architecture not only alleviates implementation challenges and enhances scalability but also possesses intrinsic fault tolerance. This paper proposes a practical decoding method tailored to correlated spin-flip errors in spin readout of PE architecture. Our work is based on the close connection between PE architecture and classical low-density parity-check (LDPC) codes. We show that the bit-flip (BF) decoding algorithm can correct independent and identically distributed errors in the readout of the SLHZ system with comparable performance to the belief propagation (BP) decoding algorithm. Then, we show evidence that the proposed BF decoding algorithm can efficiently correct correlated spinflip errors by simulation. The result suggests that introducing post-readout BF decoding reduces the computational cost of QA using the PE architecture and improves the performance of global optimal solution search. Our results emphasize the importance of the proper selection of decoding algorithms to exploit the inherent fault tolerance potential of the PE architecture.

## Regular LDPC codes on BMS wiretap channels: Security bounds

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2502.06058v1
- **Type**: preprint
- **Published**: 2025-02-09
- **Authors**: Madhura Pathegama, Alexander Barg
- **PDF**: https://arxiv.org/pdf/2502.06058v1
- **Abstract**: We improve the secrecy guarantees for transmission over general binary memoryless symmetric wiretap channels that relies on regular LDPC codes. Previous works showed that LDPC codes achieve secrecy capacity of some classes of wiretap channels while leaking $o(n)$ bits of information over $n$ uses of the channel. In this note, we improve the security component of these results by reducing the leakage parameter to $O(\log^2 n)$. While this result stops short of proving \emph{strong security}, it goes beyond the general secrecy guarantees derived from properties of capacity-approaching code families.
