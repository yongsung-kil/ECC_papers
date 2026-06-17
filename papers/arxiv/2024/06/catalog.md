# arXiv — 2024-06


## Recent Advances in Deep Learning for Channel Coding: A Survey

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.19664v1
- **Type**: preprint
- **Published**: 2024-06-28
- **Authors**: Toshiki Matsumine, Hideki Ochiai
- **PDF**: https://arxiv.org/pdf/2406.19664v1
- **Abstract**: This paper provides a comprehensive survey on recent advances in deep learning (DL) techniques for the channel coding problems. Inspired by the recent successes of DL in a variety of research domains, its applications to the physical layer technologies have been extensively studied in recent years, and are expected to be a potential breakthrough in supporting the emerging use cases of the next generation wireless communication systems such as 6G. In this paper, we focus exclusively on the channel coding problems and review existing approaches that incorporate advanced DL techniques into code design and channel decoding. After briefly introducing the background of recent DL techniques, we categorize and summarize a variety of approaches, including model-free and mode-based DL, for the design and decoding of modern error-correcting codes, such as low-density parity check (LDPC) codes and polar codes, to highlight their potential advantages and challenges. Finally, the paper concludes with a discussion of open issues and future research directions in channel coding.

## Localized statistics decoding for quantum low-density parity-check codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.18655v2
- **Type**: preprint
- **Published**: 2024-06-26
- **Authors**: Timo Hillmann, Lucas Berent, Armanda O. Quintavalle +3
- **PDF**: https://arxiv.org/pdf/2406.18655v2
- **Abstract**: Quantum low-density parity-check codes are a promising candidate for fault-tolerant quantum computing with considerably reduced overhead compared to the surface code. However, the lack of a practical decoding algorithm remains a barrier to their implementation. In this work, we introduce localized statistics decoding, a reliability-guided inversion decoder that is highly parallelizable and applicable to arbitrary quantum low-density parity-check codes. Our approach employs a parallel matrix factorization strategy, which we call on-the-fly elimination, to identify, validate, and solve local decoding regions on the decoding graph. Through numerical simulations, we show that localized statistics decoding matches the performance of state-of-the-art decoders while reducing the runtime complexity for operation in the sub-threshold regime. Importantly, our decoder is more amenable to implementation on specialized hardware, positioning it as a promising candidate for decoding real-time syndromes from experiments.

## Decentralized and Centralized IDD Schemes for Cell-Free Networks

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.16675v1
- **Type**: preprint
- **Published**: 2024-06-24
- **Authors**: T. Ssettumba, Z. Shao, L. Landau +1
- **PDF**: https://arxiv.org/pdf/2406.16675v1
- **Abstract**: In this paper, we propose iterative interference cancellation schemes with access points selection (APs-Sel) for cell-free massive multiple-input multiple-output (CF-mMIMO) systems. Closed-form expressions for centralized and decentralized linear minimum mean square error (LMMSE) receive filters with APs-Sel are derived assuming imperfect channel state information (CSI). Furthermore, we develop a list-based detector based on LMMSE receive filters that exploits interference cancellation and the constellation points. A message-passing-based iterative detection and decoding (IDD) scheme that employs low-density parity-check (LDPC) codes is then developed. Moreover, log-likelihood ratio (LLR) refinement strategies based on censoring and a linear combination of local LLRs are proposed to improve the network performance. We compare the cases with centralized and decentralized processing in terms of bit error rate (BER) performance, complexity, and signaling under perfect CSI (PCSI) and imperfect CSI (ICSI) and verify the superiority of the distributed architecture with LLR refinements.

## Perturbative stability and error correction thresholds of quantum codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.15757v3
- **Type**: preprint
- **Published**: 2024-06-22
- **Authors**: Yaodong Li, Nicholas O'Dea, Vedika Khemani
- **PDF**: https://arxiv.org/pdf/2406.15757v3
- **Abstract**: Topologically-ordered phases are stable to local perturbations, and topological quantum error-correcting codes enjoy thresholds to local errors. We connect the two notions of stability by constructing classical statistical mechanics models for decoding general CSS codes and classical linear codes. Our construction encodes correction success probabilities under uncorrelated bit-flip and phase-flip errors, and simultaneously describes a generalized Z2 lattice gauge theory with quenched disorder. We observe that the clean limit of the latter is precisely the discretized imaginary time path integral of the corresponding quantum code Hamiltonian when the errors are turned into a perturbative X or Z magnetic field. Motivated by error correction considerations, we define general order parameters for all such generalized Z2 lattice gauge theories, and show that they are generally lower bounded by success probabilities of error correction. For CSS codes satisfying the LDPC condition and with a sufficiently large code distance, we prove the existence of a low temperature ordered phase of the corresponding lattice gauge theories, particularly for those lacking Euclidean spatial locality and/or when there is a nonzero code rate. We further argue that these results provide evidence to stable phases in the corresponding perturbed quantum Hamiltonians, obtained in the limit of continuous imaginary time. To do so, we distinguish space- and time-like defects in the lattice gauge theory. A high free-energy cost of space-like defects corresponds to a successful "memory experiment" and suppresses the energy splitting among the ground states, while a high free-energy cost of time-like defects corresponds to a successful "stability experiment" and points to a nonzero gap to local excitations.

## High-threshold, low-overhead and single-shot decodable fault-tolerant quantum memory

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.14445v2
- **Type**: preprint
- **Published**: 2024-06-20
- **Authors**: Thomas R. Scruby, Timo Hillmann, Joschka Roffe
- **PDF**: https://arxiv.org/pdf/2406.14445v2
- **Abstract**: We present a new family of quantum low-density parity-check codes, which we call radial codes, obtained from the lifted product of a specific subset of classical quasi-cyclic codes. The codes are defined using a pair of integers $(r,s)$ and have parameters $[\![2r^2s,2(r-1)^2,\leq2s]\!]$, with numerical studies suggesting average-case distance linear in $s$. In simulations of circuit-level noise, we observe comparable error suppression to surface codes of similar distance while using approximately five times fewer physical qubits. This is true even when radial codes are decoded using a single-shot approach, which can allow for faster logical clock speeds and reduced decoding complexity. We describe an intuitive visual representation, canonical basis of logical operators and optimal-length stabiliser measurement circuits for these codes, and argue that their error correction capabilities, tunable parameters and small size make them promising candidates for implementation on near-term quantum devices.

## Factor Graph Optimization of Error-Correcting Codes for Belief Propagation Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.12900v2
- **Type**: preprint
- **Published**: 2024-06-09
- **Authors**: Yoni Choukroun, Lior Wolf
- **PDF**: https://arxiv.org/pdf/2406.12900v2
- **Abstract**: The design of optimal linear block codes capable of being efficiently decoded is of major concern, especially for short block lengths. As near capacity-approaching codes, Low-Density Parity-Check (LDPC) codes possess several advantages over other families of codes, the most notable being its efficient decoding via Belief Propagation. While many LDPC code design methods exist, the development of efficient sparse codes that meet the constraints of modern short code lengths and accommodate new channel models remains a challenge. In this work, we propose for the first time a gradient-based data-driven approach for the design of sparse codes. We develop locally optimal codes with respect to Belief Propagation decoding via the learning of the Factor graph under channel noise simulations. This is performed via a novel complete graph tensor representation of the Belief Propagation algorithm, optimized over finite fields via backpropagation and coupled with an efficient line-search method. The proposed approach is shown to outperform the decoding performance of existing popular codes by orders of magnitude and demonstrates the power of data-driven approaches for code design.

## Entangling four logical qubits beyond break-even in a nonlocal code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.02666v2
- **Type**: preprint
- **Published**: 2024-06-04
- **Authors**: Yifan Hong, Elijah Durso-Sabina, David Hayes +1
- **PDF**: https://arxiv.org/pdf/2406.02666v2
- **Abstract**: Quantum error correction protects logical quantum information against environmental decoherence by encoding logical qubits into entangled states of physical qubits. One of the most important near-term challenges in building a scalable quantum computer is to reach the break-even point, where logical quantum circuits on error-corrected qubits achieve higher fidelity than equivalent circuits on uncorrected physical qubits. Using Quantinuum's H2 trapped-ion quantum processor, we encode the GHZ state in four logical qubits with fidelity $ 99.5 \pm 0.15 \% \le F \le 99.7 \pm 0.1\% $ (after postselecting on over 98% of outcomes). Using the same quantum processor, we can prepare an uncorrected GHZ state on four physical qubits with fidelity $97.8 \pm 0.2 \% \le F\le 98.7\pm 0.2\%$. The logical qubits are encoded in a $[\![ 25,4,3 ]\!]$ Tanner-transformed long-range-enhanced surface code. Logical entangling gates are implemented using simple swap operations. Our results are a first step towards realizing fault-tolerant quantum computation with logical qubits encoded in geometrically nonlocal quantum low-density parity check codes.

## Improved Generalized Automorphism Belief Propagation Decoding

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.02012v2
- **Type**: preprint
- **Published**: 2024-06-04
- **Authors**: Jonathan Mandelbaum, Sisi Miao, Nils Albert Schwendemann +2
- **PDF**: https://arxiv.org/pdf/2406.02012v2
- **Abstract**: With the increasing demands on future wireless systems, new design objectives become eminent. Low-density parity-check codes together with belief propagation (BP) decoding have outstanding performance for large block lengths. Yet, for future wireless systems, good decoding performance for short block lengths is mandatory, a regime in which BP decoding typically shows a significant gap to maximum likelihood decoding. Automorphism ensemble decoding (AED) is known to reduce this gap effectively and, in addition, enables an easy trade-off between latency, throughput, and complexity. Recently, generalized AED (GAED) was proposed to increase the set of feasible automorphisms suitable for ensemble decoding. By construction, GAED requires a preprocessing step within its constituent paths that results in information loss and potentially limits the gains of GAED. In this work, we show that the preprocessing step can be merged with the Tanner graph of BP decoding, thereby improving the performance of the constituent paths. Finally, we show that the improvement of the individual paths also enhances the overall performance of the ensemble.

## High Throughput Polar Code Decoders with Information Bottleneck Quantization

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2406.01426v1
- **Type**: preprint
- **Published**: 2024-06-03
- **Authors**: Claus Kestel, Lucas Johannsen, Norbert Wehn
- **PDF**: https://arxiv.org/pdf/2406.01426v1
- **Abstract**: In digital baseband processing, the forward error correction (FEC) unit belongs to the most demanding components in terms of computational complexity and power consumption. Hence, efficient implementation of FEC decoders is crucial for next generation mobile broadband standards and an ongoing research topic. Quantization has a significant impact on the decoder area, power consumption and throughput. Thus, lower bit-widths are preferred for efficient implementations but degrade the error-correction capability. To address this issue, a non-uniform quantization based on the Information Bottleneck (IB) method was proposed that enables a low bit width while maintaining the essential information. Many investigations on the use of IB method for Low-density parity-check code (LDPC) decoders exist and have shown its advantages from an implementation perspective. However, for polar code decoder implementations, there exists only one publication that is not based on the state-of-the-art Fast-SSC decoding algorithm, and only synthesis implementation results without energy estimation are shown. In contrast, our paper presents several optimized Fast Simplified Successive-Cancellation (Fast-SSC) polar code decoder implementations using IB-based quantization with placement&routing results in an advanced 12 nm FinFET technology. Gains of up to 16% in area and 13% in energy efficiency are achieved with IB-based quantization at a Frame Error Rate (FER) of 10-7 and a Polar Code of N = 1024, R = 0.5 compared to state-of-the-art decoders.
