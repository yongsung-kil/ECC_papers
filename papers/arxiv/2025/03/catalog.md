# arXiv — 2025-03


## Generative Decoding for Quantum Error-correcting Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.21374v1
- **Type**: preprint
- **Published**: 2025-03-27
- **Authors**: Hanyan Cao, Feng Pan, Dongyang Feng +2
- **PDF**: https://arxiv.org/pdf/2503.21374v1
- **Abstract**: Efficient and accurate decoding of quantum error-correcting codes is essential for fault-tolerant quantum computation, however, it is challenging due to the degeneracy of errors, the complex code topology, and the large space for logical operators in high-rate codes. In this work, we propose a decoding algorithm utilizing generative modeling in machine learning. We employ autoregressive neural networks to learn the joint probability of logical operators and syndromes in an unsupervised manner, eliminating the need for labeled training data. The learned model can approximately perform maximum likelihood decoding by directly generating the most likely logical operators for $k$ logical qubits with $\mathcal O(2k)$ computational complexity. Thus, it is particularly efficient for decoding high-rate codes with many logical qubits. The proposed approach is general and applies to a wide spectrum of quantum error-correcting codes including surface codes and quantum low-density parity-check codes (qLDPC), under noise models ranging from code capacity noise to circuit level noise. We conducted extensive numerical experiments to demonstrate that our approach achieves significantly higher decoding accuracy compared to the minimum weight perfect matching and belief propagation with ordered statistics on the surface codes and high-rate quantum low-density parity-check codes. Our approach highlights generative artificial intelligence as a potential solution for the real-time decoding of realistic and high-rate quantum error correction codes.

## Strongly regular generalized partial geometries and associated LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.14058v1
- **Type**: preprint
- **Published**: 2025-03-18
- **Authors**: Lijun Ma, Changli Ma, Zihong Tian
- **PDF**: https://arxiv.org/pdf/2503.14058v1
- **Abstract**: In this paper, we introduce strongly regular generalized partial geometries of grade $r$, which generalise partial geometries and strongly regular $(α,β)$-geometries. By the properties of quadrics in PG$(2,q)$ and PG$(3,q)$, we construct two classes of strongly regular generalized partial geometries of grade $3$. Besides, we define low-density parity-check (LDPC) codes by considering the combinatorial structures of strongly regular generalized partial geometries and derive bounds on minimum distance, dimension and girth for the LDPC codes.

## Single Sparse Graph Enhanced Expectation Propagation Algorithm Design for Uplink MIMO-SCMA

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.13681v1
- **Type**: preprint
- **Published**: 2025-03-17
- **Authors**: Qu Luo, Jing Zhu, Gaojie Chen +2
- **PDF**: https://arxiv.org/pdf/2503.13681v1
- **Abstract**: Sparse code multiple access (SCMA) and multiple input multiple output (MIMO) are considered as two efficient techniques to provide both massive connectivity and high spectrum efficiency for future machine-type wireless networks. This paper proposes a single sparse graph (SSG) enhanced expectation propagation algorithm (EPA) receiver, referred to as SSG-EPA, for uplink MIMO-SCMA systems. Firstly, we reformulate the sparse codebook mapping process using a linear encoding model, which transforms the variable nodes (VNs) of SCMA from symbol-level to bit-level VNs. Such transformation facilitates the integration of the VNs of SCMA and low-density parity-check (LDPC), thereby emerging the SCMA and LDPC graphs into a SSG. Subsequently, to further reduce the detection complexity, the message propagation between SCMA VNs and function nodes (FNs) are designed based on EPA principles. Different from the existing iterative detection and decoding (IDD) structure, the proposed EPA-SSG allows a simultaneously detection and decoding at each iteration, and eliminates the use of interleavers, de-interleavers, symbol-to-bit, and bit-to-symbol LLR transformations. Simulation results show that the proposed SSG-EPA achieves better error rate performance compared to the state-of-the-art schemes.

## Goal-Oriented Source Coding using LDPC Codes for Compressed-Domain Image Classification

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.11954v1
- **Type**: preprint
- **Published**: 2025-03-15
- **Authors**: Ahcen Aliouat, Elsa Dupraz
- **PDF**: https://arxiv.org/pdf/2503.11954v1
- **Abstract**: In the emerging field of goal-oriented communications, the focus has shifted from reconstructing data to directly performing specific learning tasks, such as classification, segmentation, or pattern recognition, on the received coded data. In the commonly studied scenario of classification from compressed images, a key objective is to enable learning directly on entropy-coded data, thereby bypassing the computationally intensive step of data reconstruction. Conventional entropy-coding methods, such as Huffman and Arithmetic coding, are effective for compression but disrupt the data structure, making them less suitable for direct learning without decoding. This paper investigates the use of low-density parity-check (LDPC) codes -- originally designed for channel coding -- as an alternative entropy-coding approach. It is hypothesized that the structured nature of LDPC codes can be leveraged more effectively by deep learning models for tasks like classification. At the receiver side, gated recurrent unit (GRU) models are trained to perform image classification directly on LDPC-coded data. Experiments on datasets like MNIST, Fashion-MNIST, and CIFAR show that LDPC codes outperform Huffman and Arithmetic coding in classification tasks, while requiring significantly smaller learning models. Furthermore, the paper analyzes why LDPC codes preserve data structure more effectively than traditional entropy-coding techniques and explores the impact of key code parameters on classification performance. These results suggest that LDPC-based entropy coding offers an optimal balance between learning efficiency and model complexity, eliminating the need for prior decoding.

## Fault-tolerant logical state construction based on cavity-QED network

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.11500v2
- **Type**: preprint
- **Published**: 2025-03-14
- **Authors**: Rui Asaoka, Yasunari Suzuki, Yuuki Tokunaga
- **PDF**: https://arxiv.org/pdf/2503.11500v2
- **Abstract**: Exploring an efficient and scalable architecture of fault-tolerant quantum computing (FTQC) is vital for demonstrating useful quantum computing. Here, we propose and evaluate a scalable and practical architecture with a cavity-quantum-electrodynamics (CQED) network. Our architecture takes advantage of the stability of neutral atoms and the flexibility of a CQED network. We show a concrete framework for implementing surface codes and numerically analyze the logical error rate and threshold values beyond the simplified circuit-level noise model on several network structures. Although the requirement of CQED parameters is demanding given the current performance of experimental systems, we show that an error-decoding algorithm tailored to our proposed architecture, where the loss information of ancillary photons is utilized, greatly improves the error threshold. For example, the internal cooperativity, a good figure of merit of the cavity performance for quantum computing, required for FTQC is relaxed to 1/5 compared to the normal error-decoding for the surface code. Since our proposal and results can be extended to other LDPC codes straightforwardly, our approach will lead to achieve more reliable FTQC using CQED.

## Extractors: QLDPC Architectures for Efficient Pauli-Based Computation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.10390v2
- **Type**: preprint
- **Published**: 2025-03-13
- **Authors**: Zhiyang He, Alexander Cowtan, Dominic J. Williamson +1
- **PDF**: https://arxiv.org/pdf/2503.10390v2
- **Abstract**: In pursuit of large-scale fault-tolerant quantum computation, quantum low-density parity-check (LDPC) codes have been established as promising candidates for low-overhead memory when compared to conventional approaches based on surface codes. Performing fault-tolerant logical computation on QLDPC memory, however, has been a long standing challenge in theory and in practice. In this work, we propose a new primitive, which we call an $\textit{extractor system}$, that can augment any QLDPC memory into a computational block well-suited for Pauli-based computation. In particular, any logical Pauli operator supported on the memory can be fault-tolerantly measured in one logical cycle, consisting of $O(d)$ physical syndrome measurement cycles, without rearranging qubit connectivity. We further propose a fixed-connectivity, LDPC architecture built by connecting many extractor-augmented computational (EAC) blocks with bridge systems. When combined with any user-defined source of high fidelity $|T\rangle$ states, our architecture can implement universal quantum circuits via parallel logical measurements, such that all single-block Clifford gates are compiled away. The size of an extractor on an $n$ qubit code is $\tilde{O}(n)$, where the precise overhead has immense room for practical optimizations.

## On the Minimum Distances of Finite-Length Lifted Product Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.07567v1
- **Type**: preprint
- **Published**: 2025-03-10
- **Authors**: Nithin Raveendran, David Declercq, Bane Vasić
- **PDF**: https://arxiv.org/pdf/2503.07567v1
- **Abstract**: Quantum error correction (QEC) is critical for practical realization of fault-tolerant quantum computing, and recently proposed families of quantum low-density parity-check (QLDPC) code are prime candidates for advanced QEC hardware architectures and implementations. This paper focuses on the finite-length QLDPC code design criteria, specifically aimed at constructing degenerate quasi-cyclic symmetric lifted-product (LP-QLDPC) codes. We describe the necessary conditions such that the designed LP-QLDPC codes are guaranteed to have a minimum distance strictly greater than the minimum weight stabilizer generators, ensuring superior error correction performance on quantum channels. The focus is on LP-QLDPC codes built from quasi-cyclic base codes belonging to the class of type-I protographs, and the necessary constraints are efficiently expressed in terms of the row and column indices of the base code. Specifically, we characterize the combinatorial constraints on the classical quasi-cyclic base matrices that guarantee construction of degenerate LP-QLDPC codes. Minimal examples and illustrations are provided to demonstrate the usefulness and effectiveness of the code construction approach. The row and column partition constraints derived in the paper simplify the design of degenerate LP-QLDPC codes and can be incorporated into existing classical and quantum code design approaches.

## Parallel Logical Measurements via Quantum Code Surgery

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.05003v3
- **Type**: preprint
- **Published**: 2025-03-06
- **Authors**: Alexander Cowtan, Zhiyang He, Dominic J. Williamson +1
- **PDF**: https://arxiv.org/pdf/2503.05003v3
- **Abstract**: Quantum code surgery is a flexible and low overhead technique for performing logical measurements on quantum error-correcting codes, which generalises lattice surgery. In this work, we present a code surgery scheme, applicable to any qubit stabiliser low-density parity check (LDPC) code, that fault-tolerantly measures many logical Pauli operators in parallel. For a collection of logically disjoint Pauli product measurements supported on $t$ logical qubits, our scheme uses $O\big(t ω(\log t + \log^3ω)\big)$ ancilla qubits, where $ω\geq d$ is the maximum weight of the single logical Pauli representatives involved in the measurements, and $d$ is the code distance. This is all done in time $O(d)$ independent of $t$. Our proposed scheme preserves both the LDPC property and the fault-distance of the original code, without requiring ancillary logical codeblocks which may be costly to prepare. This addresses a shortcoming of several recently introduced surgery schemes which can only be applied to measure a limited number of logical operators in parallel if they overlap on data qubits.

## Anyon Theory and Topological Frustration of High-Efficiency Quantum Low-Density Parity-Check Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.04699v2
- **Type**: preprint
- **Published**: 2025-03-06
- **Authors**: Keyang Chen, Yuanting Liu, Yiming Zhang +4
- **PDF**: https://arxiv.org/pdf/2503.04699v2
- **Abstract**: Quantum low-density parity-check (QLDPC) codes offer a promising path to low-overhead fault-tolerant quantum computation but lack systematic strategies for exploration. In this Letter, we establish a topological framework for studying the bivariate-bicycle codes, a prominent class of QLDPC codes tailored for real-world quantum hardware. Our framework enables the investigation of these codes through universal properties of topological orders. In addition to efficient characterizations using Gröbner bases, we also introduce a novel algebraic-geometric approach based on the Bernstein--Khovanskii--Kushnirenko theorem. This approach allows us to analytically determine how the topological order varies with the generic choices of bivariate-bicycle codes under toric layouts. Novel phenomena are unveiled, including topological frustration, where ground-state degeneracy on a torus deviates from the total anyon number, and quasi-fractonic mobility, where anyon movement violates energy conservation. We demonstrate their intrinsic link to symmetry-enriched topological orders and derive an efficient method for generating finite-size codes. Furthermore, we extend the connection between anyons and logical operators using Koszul complex theory. Our Letter provides a rigorous theoretical basis for exploring the fault tolerance of QLDPC codes and deepens the interplay among topological order, quantum error correction, and advanced algebraic structures.

## Construction and Decoding of Quantum Margulis Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.03936v3
- **Type**: preprint
- **Published**: 2025-03-05
- **Authors**: Michele Pacenti, Dimitris Chytas, Bane Vasic
- **PDF**: https://arxiv.org/pdf/2503.03936v3
- **Abstract**: Quantum low-density parity-check codes are a promising approach to fault-tolerant quantum computation, offering potential advantages in rate and decoding efficiency. In this work, we introduce quantum Margulis codes, a new class of QLDPC codes derived from Margulis' classical LDPC construction via the two-block group algebra framework. We show that quantum Margulis codes, unlike bivariate bicycle codes which require ordered statistics decoding for effective error correction, can be efficiently decoded using a standard min-sum decoder with linear complexity, when decoded under the code capacity noise model. This is attributed to their Tanner graph structure, which does not exhibit group symmetry, thereby mitigating the well-known problem of error degeneracy in QLDPC decoding. To further enhance performance, we propose an algorithm for constructing 2BGA codes with controlled girth, ensuring a minimum girth of 6 or 8, and use it to generate several quantum Margulis codes of length 240 and 642. We validate our approach through numerical simulations, demonstrating that quantum Margulis codes behave significantly better than BB codes in the error floor region, under min-sum decoding.

## Generalized toric codes on twisted tori for quantum error correction

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.03827v3
- **Type**: preprint
- **Published**: 2025-03-05
- **Authors**: Zijian Liang, Ke Liu, Hao Song +1
- **PDF**: https://arxiv.org/pdf/2503.03827v3
- **Abstract**: The Kitaev toric code is widely considered one of the leading candidates for error correction in fault-tolerant quantum computation. However, direct methods to increase its logical dimensions, such as lattice surgery or introducing punctures, often incur prohibitive overheads. In this work, we introduce a ring-theoretic approach for efficiently analyzing topological CSS codes in two dimensions, enabling the exploration of generalized toric codes with larger logical dimensions on twisted tori. Using Gröbner bases, we simplify stabilizer syndromes to efficiently identify anyon excitations and their geometric periodicities, even under twisted periodic boundary conditions. Since the properties of the codes are determined by the anyons, this approach allows us to directly compute the logical dimensions without constructing large parity-check matrices. Our approach provides a unified method for finding new quantum error-correcting codes and exhibiting their underlying topological orders via the Laurent polynomial ring. This framework naturally applies to bivariate bicycle codes. For example, we construct optimal weight-6 generalized toric codes on twisted tori with parameters $[[ n, k, d ]]$ for $n \leq 400$, yielding novel codes such as $[[120,8,12]]$, $[[186,10,14]]$, $[[210,10,16]]$, $[[248, 10, 18]]$, $[[254, 14, 16]]$, $[[294, 10, 20]]$, $[[310, 10, \leq 22]]$, and $[[340, 16, 18]]$. Moreover, we present a new realization of the $[[360, 12, \leq 24]]$ quantum code using the $(3,3)$-bivariate bicycle code on a twisted torus defined by the basis vectors $(0,30)$ and $(6,6)$, improving stabilizer locality relative to the previous construction. These results highlight the power of the topological order perspective in advancing the design and theoretical understanding of quantum low-density parity-check (LDPC) codes.

## Automorphism Ensemble Decoding of Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2503.01738v1
- **Type**: preprint
- **Published**: 2025-03-03
- **Authors**: Stergios Koutsioumpas, Hasan Sayginel, Mark Webster +1
- **PDF**: https://arxiv.org/pdf/2503.01738v1
- **Abstract**: We introduce AutDEC, a fast and accurate decoder for quantum error-correcting codes with large automorphism groups. Our decoder employs a set of automorphisms of the quantum code and an ensemble of belief propagation (BP) decoders. Each BP decoder is given a syndrome which is transformed by one of the automorphisms, and is run in parallel. For quantum codes, the accuracy of BP decoders is limited because short cycles occur in the Tanner graph and our approach mitigates this effect. We demonstrate decoding accuracy comparable to BP-OSD-0 with a lower time overhead for Quantum Reed-Muller (QRM) codes in the code capacity setting, and Bivariate Bicycle (BB) codes under circuit level noise. We provide a Python repository for use by the community and the results of our simulations.
