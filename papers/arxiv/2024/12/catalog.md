# arXiv — 2024-12


## Quantum Error Correction near the Coding Theoretical Bound

- **ID**: arxiv:2412.21171v4
- **Type**: preprint
- **Published**: 2024-12-30
- **Authors**: Daiki Komoto, Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2412.21171v4
- **Abstract**: Recent progress in quantum computing has enabled systems with tens of reliable logical qubits, built from thousands of noisy physical qubits. However, many impactful applications demand quantum computations with millions of logical qubits, necessitating highly scalable quantum error correction. In classical information theory, low-density parity-check (LDPC) codes can approach channel capacity efficiently. Yet, no quantum error-correcting codes with efficient decoding have been shown to approach the hashing bound - a fundamental limit on quantum capacity - despite decades of research. Here, we present quantum LDPC codes that not only approach the hashing bound but also allow decoding with computational cost linear in the number of physical qubits. This breakthrough paves the way for large-scale, fault-tolerant quantum computation. Combined with emerging hardware that manages many qubits, our approach brings quantum solutions to important real-world problems significantly closer to reality.

## Fundamental thresholds for computational and erasure errors via the coherent information

- **ID**: arxiv:2412.16727v2
- **Type**: preprint
- **Published**: 2024-12-21
- **Authors**: Luis Colmenarez, Seyong Kim, Markus Müller
- **PDF**: https://arxiv.org/pdf/2412.16727v2
- **Abstract**: Quantum error correcting (QEC) codes protect quantum information against environmental noise. Computational errors caused by the environment change the quantum state within the qubit subspace, whereas quantum erasures correspond to the loss of qubits at known positions. Correcting either type of error involves different correction mechanisms, which makes studying the interplay between erasure and computational errors particularly challenging. In this work, we propose a framework based on the coherent information (CI) of the mixed-state density operator associated to noisy QEC codes, for treating both types of errors together. We show how to rigorously derive different families of statistical mechanics mappings for generic stabilizer QEC codes in the presence of both types of errors. Further, we show that computing the CI for erasure errors only can be done efficiently upon sampling over erasure configurations. We then test our approach on the 2D toric and color codes and compute optimal thresholds for erasure errors only, finding a 50 percent threshold for both codes. This strengthens the notion that both codes share the same optimal thresholds. When considering both computational and erasure errors, the CI of small-size codes yields thresholds in very accurate agreement with established results that have been obtained in the thermodynamic limit. Next, we perform a similar analysis for a low-density parity-check (LDPC) code, the lift-connected surface code. We find a 50 percent threshold under erasure errors alone and, for the first time, derive the exact statistical mechanics mappings in the presence of both computational and erasure errors. We thereby further establish the CI as a practical tool for studying optimal thresholds for code classes beyond topological codes under realistic noise, and as a means for uncovering new relations between QEC codes and statistical physics models.

## Spiking Neural Belief Propagation Decoder for LDPC Codes with Small Variable Node Degrees

- **ID**: arxiv:2412.15897v1
- **Type**: preprint
- **Published**: 2024-12-20
- **Authors**: Alexander von Bank, Eike-Manuel Edelmann, Jonathan Mandelbaum +1
- **PDF**: https://arxiv.org/pdf/2412.15897v1
- **Abstract**: Spiking neural networks (SNNs) promise energy-efficient data processing by imitating the event-based behavior of biological neurons. In previous work, we introduced the enlarge-likelihood-each-notable-amplitude spiking-neural-network (ELENA-SNN) decoder, a novel decoding algorithm for low-density parity-check (LDPC) codes. The decoder integrates SNNs into belief propagation (BP) decoding by approximating the check node (CN) update equation using SNNs. However, when decoding LDPC codes with a small variable node(VN) degree, the approximation gets too rough, and the ELENA-SNN decoder does not yield good results. This paper introduces the multi-level ELENA-SNN (ML-ELENA-SNN) decoder, which is an extension of the ELENA-SNN decoder. Instead of a single SNN approximating the CN update, multiple SNNs are applied in parallel, resulting in a higher resolution and higher dynamic range of the exchanged messages. We show that the ML-ELENA-SNN decoder performs similarly to the ubiquitous normalized min-sum decoder for the (38400, 30720) regular LDPC code with a VN degree of dv = 3 and a CN degree of dc = 15.

## Turbo product decoding of cubic tensor codes

- **ID**: arxiv:2412.14017v1
- **Type**: preprint
- **Published**: 2024-12-18
- **Authors**: Sarah Khalifeh, Ken R. Duffy, Muriel Medard
- **PDF**: https://arxiv.org/pdf/2412.14017v1
- **Abstract**: Long, powerful soft detection forward error correction codes are typically constructed by concatenation of shorter component codes that are decoded through iterative Soft-Input Soft-Output (SISO) procedures. The current gold-standard is Low Density Parity Check (LDPC) codes, which are built from weak single parity check component codes that are capable of producing accurate SO. Due to the recent development of SISO decoders that produce highly accurate SO with codes that have multiple redundant bits, square product code constructions that can avail of more powerful component codes have been shown to be competitive with the LDPC codes in the 5G New Radio standard in terms of decoding performance while requiring fewer iterations to converge. Motivated by applications that require more powerful low-rate codes, in the present paper we explore the possibility of extending this design space by considering the construction and decoding of cubic tensor codes.

## Topological Quantum Spin Glass Order and its realization in qLDPC codes

- **ID**: arxiv:2412.13248v1
- **Type**: preprint
- **Published**: 2024-12-17
- **Authors**: Benedikt Placke, Tibor Rakovszky, Nikolas P. Breuckmann +1
- **PDF**: https://arxiv.org/pdf/2412.13248v1
- **Abstract**: Ordered phases of matter have close connections to computation. Two prominent examples are spin glass order, with wide-ranging applications in machine learning and optimization, and topological order, closely related to quantum error correction. Here, we introduce the concept of topological quantum spin glass (TQSG) order which marries these two notions, exhibiting both the complex energy landscapes of spin glasses, and the quantum memory and long-range entanglement characteristic of topologically ordered systems. Using techniques from coding theory and a quantum generalization of Gibbs state decompositions, we show that TQSG order is the low-temperature phase of various quantum LDPC codes on expander graphs, including hypergraph and balanced product codes. Our work introduces a topological analog of spin glasses that preserves quantum information, opening new avenues for both statistical mechanics and quantum computer science.

## Iterative Detection and Decoding for Clustered Cell-Free Massive MIMO Networks

- **ID**: arxiv:2412.10956v1
- **Type**: preprint
- **Published**: 2024-12-14
- **Authors**: T. Ssettumba, S. Mashdour, L. Landau +2
- **PDF**: https://arxiv.org/pdf/2412.10956v1
- **Abstract**: In this letter, we propose an iterative soft interference cancellation scheme for intra-cluster (ICL) and out-of-cluster (OCL) interference mitigation in user-centric clustered cell-free massive multiple-antenna networks. We propose a minimum mean-square error receive filter with a novel modified parallel interference cancellation scheme to mitigate ICL and OCL interference. Unlike prior work, we model the OCL interference and devise a least squares estimator to perform OCL interference estimation. An iterative detection and decoding scheme that adopts low-density parity check codes and incorporates the OCL interference estimate is developed. Simulations assess the proposed scheme against existing techniques in terms of bit error rate performance.

## Study of Iterative Detection and Decoding for Multiuser Systems and MMSE Refinements with Active or Passive RIS

- **ID**: arxiv:2412.10642v1
- **Type**: preprint
- **Published**: 2024-12-14
- **Authors**: R. Porto, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2412.10642v1
- **Abstract**: An iterative detection and decoding (IDD) scheme is proposed for multiuser multiple-antenna systems assisted by an active or a passive Reconfigurable Intelligent Surface (RIS). The proposed approach features an IDD strategy that incorporates Low-Density Parity-Check (LDPC) codes, RIS processing with refinements of soft information in the form of log likelihood ratios (LLRs) and truncation. Specifically, a minimum mean square error (MMSE) receive filter is used for refinement of LLRs and truncation at the RIS, and for soft interference cancellation at the receiver. An analysis of the proposed MMSE refinement is also devised along with a study of the computational complexity of the proposed and existing schemes. Simulation results demonstrate significant improvements in system capacity and bit error rate in the presence of block-fading channels

## Quantum-enhanced belief propagation for LDPC decoding

- **ID**: arxiv:2412.08596v1
- **Type**: preprint
- **Published**: 2024-12-11
- **Authors**: Sheila M. Perez-Garcia, Ashley Montanaro
- **PDF**: https://arxiv.org/pdf/2412.08596v1
- **Abstract**: Decoding low-density parity-check codes is critical in many current technologies, such as fifth-generation (5G) wireless networks and satellite communications. The belief propagation algorithm allows for fast decoding due to the low density of these codes. However, there is scope for improvement to this algorithm both in terms of its computational cost when decoding large codes and its error-correcting abilities. Here, we introduce the quantum-enhanced belief propagation (QEBP) algorithm, in which the Quantum Approximate Optimization Algorithm (QAOA) acts as a pre-processing step to belief propagation. We perform exact simulations of syndrome decoding with QAOA, whose result guides the belief propagation algorithm, leading to faster convergence and a lower block error rate (BLER). In addition, through the repetition code, we study the possibility of having shared variational parameters between syndromes and, in this case, code lengths. We obtain a unique pair of variational parameters for level-1 QAOA by optimizing the probability of successful decoding through a transfer matrix method. Then, using these parameters, we compare the scaling of different QAOA post-processing techniques with code length.

## Pruning qLDPC codes: Towards bivariate bicycle codes with open boundary conditions

- **ID**: arxiv:2412.04181v1
- **Type**: preprint
- **Published**: 2024-12-05
- **Authors**: Jens Niklas Eberhardt, Francisco Revson F. Pereira, Vincent Steffan
- **PDF**: https://arxiv.org/pdf/2412.04181v1
- **Abstract**: Quantum low-density parity-check codes are promising candidates for quantum error correcting codes as they might offer more resource-efficient alternatives to surface code architectures. In particular, bivariate bicycle codes have recently gained attention due to their 2D-local structure, high encoding rate, and promising performance under simulation. In this work, we will explore how one can transform bivariate bicycle codes defined on lattices with periodic boundary conditions to codes with the same locality properties on a 2D lattice with open boundary conditions. For this, we introduce the concept of pruning quantum codes. We explain how pruning bivariate bicycle codes is always possible when the codes are hypergraph products of two classical cyclic codes. We also indicate that this might be possible for more general bivariate bicycle codes by constructing explicit examples. Finally, we investigate fault-tolerant quantum computation using the constructed pruned codes by describing fold-transversal gates.

## SymBreak: Mitigating Quantum Degeneracy Issues in QLDPC Code Decoders by Breaking Symmetry

- **ID**: arxiv:2412.02885v1
- **Type**: preprint
- **Published**: 2024-12-03
- **Authors**: Keyi Yin, Xiang Fang, Jixuan Ruan +7
- **PDF**: https://arxiv.org/pdf/2412.02885v1
- **Abstract**: Quantum error correction (QEC) is critical for scalable and reliable quantum computing, but existing solutions, such as surface codes, incur significant qubit overhead. Quantum low-density parity check (qLDPC) codes have recently emerged as a promising alternative, requiring fewer qubits. However, the lack of efficient decoders remains a major barrier to their practical implementation. In this work, we introduce SymBreak, a novel decoder for qLDPC codes that adaptively modifies the decoding graph to improve the performance of state-of-the-art belief propagation (BP) decoders. Our key contribution is identifying quantum degeneracy as a root cause of the convergence issues often encountered in BP decoding of quantum LDPC codes. We propose a solution that mitigates this issue at the decoding graph level, achieving both fast and accurate decoding. Our results demonstrate that SymBreak outperforms BP and BP+OSD-a more complex variant of BP-with a $16.17\times$ reduction in logical error rate compared to BP and $3.23\times$ compared to BP+OSD across various qLDPC code families. With only an $18.97$% time overhead compared to BP, SymBreak provides significantly faster decoding times than BP+OSD, representing a major advancement in efficient and accurate decoding for qLDPC-based QEC architectures.

## On the lifting degree of girth-8 QC-LDPC codes

- **ID**: arxiv:2412.02526v1
- **Type**: preprint
- **Published**: 2024-12-03
- **Authors**: Haoran Xiong, Guanghui Wang, Zhiming Ma +1
- **PDF**: https://arxiv.org/pdf/2412.02526v1
- **Abstract**: The lifting degree and the deterministic construction of quasi-cyclic low-density parity-check (QC-LDPC) codes have been extensively studied, with many construction methods in the literature, including those based on finite geometry, array-based codes, computer search, and combinatorial techniques. In this paper, we focus on the lifting degree $p$ required for achieving a girth of 8 in $(3,L)$ fully connected QC-LDPC codes, and we propose an improvement over the classical lower bound $p\geq 2L-1$, enhancing it to $p\geq \sqrt{5L^2-11L+\frac{13}{2}}+\frac{1}{2}$. Moreover, we demonstrate that for girth-8 QC-LDPC codes containing an arithmetic row in the exponent matrix, a necessary condition for achieving a girth of 8 is $p\geq \frac{1}{2}L^2+\frac{1}{2}L$. Additionally, we present a corresponding deterministic construction of $(3,L)$ QC-LDPC codes with girth 8 for any $p\geq \frac{1}{2}L^2+\frac{1}{2}L+\lfloor \frac{L-1}{2}\rfloor$, which approaches the lower bound of $\frac{1}{2}L^2+\frac{1}{2}L$. Under the same conditions, this construction achieves a smaller lifting degree compared to prior methods. To the best of our knowledge, the proposed order of lifting degree matches the smallest known, on the order of $\frac{1}{2}L^2+\mathcal{O} (L)$.
