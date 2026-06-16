# arXiv — 2022-10


## GRAND-assisted Optimal Modulation

- **ID**: arxiv:2210.16187v2
- **Type**: preprint
- **Published**: 2022-10-28
- **Authors**: Basak Ozaydin, Muriel Médard, Ken Duffy
- **PDF**: https://arxiv.org/pdf/2210.16187v2
- **Abstract**: Optimal modulation (OM) schemes for Gaussian channels with peak and average power constraints are known to require nonuniform probability distributions over signal points, which presents practical challenges. An established way to map uniform binary sources to non-uniform symbol distributions is to assign a different number of bits to different constellation points. Doing so, however, means that erroneous demodulation at the receiver can lead to bit insertions or deletions that result in significant binary error propagation. In this paper, we introduce a light-weight variant of Guessing Random Additive Noise Decoding (GRAND) to resolve insertion and deletion errors at the receiver by using a simple padding scheme. Performance evaluation demonstrates that our approach results in an overall gain in demodulated bit-error-rate of over 2 dB Eb/N0 when compared to 128-Quadrature Amplitude Modulation (QAM). The GRAND-aided OM scheme outperforms coding with a low-density parity check code of the same average rate as that induced by our simple padding.

## Design of Protograph LDPC-Coded MIMO-VLC Systems with Generalized Spatial Modulation

- **ID**: arxiv:2210.16007v1
- **Type**: preprint
- **Published**: 2022-10-28
- **Authors**: Lin Dai, Yi Fang, Yong Liang Guan +1
- **PDF**: https://arxiv.org/pdf/2210.16007v1
- **Abstract**: This paper investigates the bit-interleaved coded generalized spatial modulation (BICGSM) with iterative decoding (BICGSM-ID) for multiple-input multiple-output (MIMO) visible light communications (VLC). In the BICGSM-ID scheme, the information bits conveyed by the signal-domain (SiD) symbols and the spatial-domain (SpD) light emitting diode (LED)-index patterns are coded by a protograph low-density parity-check (P-LDPC) code. Specifically, we propose a signal-domain symbol expanding and re-allocating (SSER) method for constructing a type of novel generalized spatial modulation (GSM) constellations, referred to as SSERGSM constellations, so as to boost the performance of the BICGSM-ID MIMO-VLC systems. Moreover, by applying a modified PEXIT (MPEXIT) algorithm, we further design a family of rate-compatible P-LDPC codes, referred to as enhanced accumulate-repeat-accumulate (EARA) codes, which possess both excellent decoding thresholds and linear-minimum-distance-growth property. Both analysis and simulation results illustrate that the proposed SSERGSM constellations and P-LDPC codes can remarkably improve the convergence and decoding performance of MIMO-VLC systems. Therefore, the proposed P-LDPC-coded SSERGSM-mapped BICGSM-ID configuration is envisioned as a promising transmission solution to satisfy the high-throughput requirement of MIMO-VLC applications.

## Opportunities and Challenges in Fault-Tolerant Quantum Computation

- **ID**: arxiv:2210.15844v1
- **Type**: preprint
- **Published**: 2022-10-28
- **Authors**: Daniel Gottesman
- **PDF**: https://arxiv.org/pdf/2210.15844v1
- **Abstract**: I will give an overview of what I see as some of the most important future directions in the theory of fault-tolerant quantum computation. In particular, I will give a brief summary of the major problems that need to be solved in fault tolerance based on low-density parity check codes and in hardware-specific fault tolerance. I will then conclude with a discussion of a possible new paradigm for designing fault-tolerant protocols based on a space-time picture of quantum circuits.

## Entanglement Purification with Quantum LDPC Codes and Iterative Decoding

- **ID**: arxiv:2210.14143v2
- **Type**: preprint
- **Published**: 2022-10-25
- **Authors**: Narayanan Rengaswamy, Nithin Raveendran, Ankur Raina +1
- **PDF**: https://arxiv.org/pdf/2210.14143v2
- **Abstract**: Recent constructions of quantum low-density parity-check (QLDPC) codes provide optimal scaling of the number of logical qubits and the minimum distance in terms of the code length, thereby opening the door to fault-tolerant quantum systems with minimal resource overhead. However, the hardware path from nearest-neighbor-connection-based topological codes to long-range-interaction-demanding QLDPC codes is a challenging one. Given the practical difficulty in building a monolithic architecture for quantum computers based on optimal QLDPC codes, it is worth considering a distributed implementation of such codes over a network of interconnected quantum processors. In such a setting, all syndrome measurements and logical operations must be performed using high-fidelity shared entangled states between the processing nodes. Since probabilistic many-to-1 distillation schemes for purifying entanglement are inefficient, we investigate quantum error correction based entanglement purification in this work. Specifically, we employ QLDPC codes to distill GHZ states, as the resulting high-fidelity logical GHZ states can interact directly with the code used to perform distributed quantum computing (DQC), e.g. for fault-tolerant Steane syndrome extraction. This protocol is applicable beyond DQC since entanglement purification is a quintessential task of any quantum network. We use the min-sum algorithm (MSA) based iterative decoder for distilling $3$-qubit GHZ states using a rate $0.118$ family of lifted product QLDPC codes and obtain an input threshold of $\approx 0.7974$ under i.i.d. single-qubit depolarizing noise. This represents the best threshold for a yield of $0.118$ for any GHZ purification protocol. Our results apply to larger size GHZ states as well, where we extend our technical result about a measurement property of $3$-qubit GHZ states to construct a scalable GHZ purification protocol.

## Implementing Clifford Gates on Stabilizer Codes via Measurement

- **ID**: arxiv:2210.14074v3
- **Type**: preprint
- **Published**: 2022-10-25
- **Authors**: Darren Banfield, Heather Leitch, Alastair Kay
- **PDF**: https://arxiv.org/pdf/2210.14074v3
- **Abstract**: We describe a method to use measurements and correction operations in order to implement the Clifford group in a stabilizer code, generalising a result from [Bombin,2011] for topological subsystem colour codes. In subsystem stabilizer codes of distance at least $3$ the process can be implemented fault-tolerantly. In particular this provides a method to implement a logical Hadamard-type gate within the 15-qubit Reed-Muller quantum code by measuring and correcting only three observables. This is an alternative to the method proposed by [Paetznick and Reichardt, 2013] to generate a set of gates which is universal for quantum computing for this code. The construction is inspired by the description of code rewiring from [Colladay and Mueller, 2018].   Inspired by the code rewiring strategy of [Colladay and Mueller, 2018], we describe a method to use measurements and correction operations in order to implement the Clifford group in the code space of any stabilizer code, and we specify a sufficient set of conditions under which the distance of the code is preserved throughout. In particular this provides a method to implement a logical Hadamard-type gate within the 15-qubit Reed-Muller quantum code by measuring and correcting only two observables, providing the only non-transversal gate required for universality. Furthermore this approach is applicable to the toric code and quantum LDPC code

## Iterative Detection and Decoding for Cell-Free Massive Multiuser MIMO with LDPC Codes

- **ID**: arxiv:2210.12906v1
- **Type**: preprint
- **Published**: 2022-10-24
- **Authors**: T. Ssettumba, R. Di Renna, L. Landau +1
- **PDF**: https://arxiv.org/pdf/2210.12906v1
- **Abstract**: This paper proposes an iterative detection and decoding (IDD) scheme for a cell free massive multiple input multiple output (CF-mMIMO) system. Users send coded data to the access points (APs), which is jointly detected at central processing unit (CPU). The symbols are exchanged iteratively in the form of log likelihood ratios (LLRs) between the detector and the low-density parity check codes (LPDC) decoder, increasing the coded system's performance. We propose a list-based multi-feedback diversity with successive interference cancellation (MF-SIC) to improve the performance of the CF-mMIMO. Furthermore, the proposed detector is compared with the parallel interference cancellation (PIC) and MF-PIC schemes. Finally, the bit error rate (BER) performance of CF-mMIMO is compared with the co-located mMIMO (Col-mMIMO).

## NLTS Hamiltonians from classical LTCs

- **ID**: arxiv:2210.02999v2
- **Type**: preprint
- **Published**: 2022-10-06
- **Authors**: Zhiyang He, Chinmay Nirkhe
- **PDF**: https://arxiv.org/pdf/2210.02999v2
- **Abstract**: We provide a completely self-contained construction of a family of NLTS Hamiltonians [Freedman and Hastings, 2014] based on ideas from [Anshu, Breuckmann, and Nirkhe, 2022], [Cross, He, Natarajan, Szegedy, and Zhu, 2022] and [Eldar and Harrow, 2017]. Crucially, it does not require optimal-parameter quantum LDPC codes and can be built from simple classical LTCs such as the repetition code on an expander graph. Furthermore, it removes the constant-rate requirement from the construction of Anshu, Breuckmann, and Nirkhe.
