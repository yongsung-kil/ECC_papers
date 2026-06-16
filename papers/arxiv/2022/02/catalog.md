# arXiv — 2022-02


## Analysis of a blockchain protocol based on LDPC codes

- **ID**: arxiv:2202.07265v3
- **Type**: preprint
- **Published**: 2022-02-15
- **Authors**: Massimo Battaglioni, Paolo Santini, Giulia Rafaiani +2
- **PDF**: https://arxiv.org/pdf/2202.07265v3
- **Abstract**: In a blockchain Data Availability Attack (DAA), a malicious node publishes a block header but withholds part of the block, which contains invalid transactions. Honest full nodes, which can download and store the full blockchain, are aware that some data are not available but they have no formal way to prove it to light nodes, i.e., nodes that have limited resources and are not able to access the whole blockchain data. A common solution to counter these attacks exploits linear error correcting codes to encode the block content. A recent protocol, called SPAR, employs coded Merkle trees and low-density parity-check codes to counter DAAs. In this paper, we show that the protocol is less secure than claimed, owing to a redefinition of the adversarial success probability. As a consequence we show that, for some realistic choices of the parameters, the total amount of data downloaded by light nodes is larger than that obtainable with competitor solutions.

## Fold-Transversal Clifford Gates for Quantum Codes

- **ID**: arxiv:2202.06647v3
- **Type**: preprint
- **Published**: 2022-02-14
- **Authors**: Nikolas P. Breuckmann, Simon Burton
- **PDF**: https://arxiv.org/pdf/2202.06647v3
- **Abstract**: We generalize the concept of folding from surface codes to CSS codes by considering certain dualities within them. In particular, this gives a general method to implement logical operations in suitable LDPC quantum codes using transversal gates and qubit permutations only.   To demonstrate our approach, we specifically consider a [[30, 8, 3]] hyperbolic quantum code called Bring's code. Further, we show that by restricting the logical subspace of Bring's code to four qubits, we can obtain the full Clifford group on that subspace.

## An Improved EPA based Receiver Design for Uplink LDPC Coded SCMA System

- **ID**: arxiv:2202.05530v1
- **Type**: preprint
- **Published**: 2022-02-11
- **Authors**: Lingyun Chai, Zilong Liu, Pei Xiao +2
- **PDF**: https://arxiv.org/pdf/2202.05530v1
- **Abstract**: Sparse code multiple access (SCMA) is an emerging paradigm for efficient enabling of massive connectivity in future machine-type communications (MTC). In this letter, we conceive the uplink transmissions of the low-density parity check (LDPC) coded SCMA system. Traditional receiver design of LDPC-SCMA system, which is based on message passing algorithm (MPA) for multiuser detection followed by individual LDPC decoding, may suffer from the drawback of the high complexity and large decoding latency, especially when the system has large codebook size and/or high overloading factor. To address this problem, we introduce a novel receiver design by applying the expectation propagation algorithm (EPA) to the joint detection and decoding (JDD) involving an aggregated factor graph of LDPC code and sparse codebooks. Our numerical results demonstrate the superiority of the proposed EPA based JDD receiver over the conventional Turbo receiver in terms of both significantly lower complexity and faster convergence rate without noticeable error rate performance degradation.

## Efficient ADMM Decoder for Non-binary LDPC Codes with Codeword-Independent Performance

- **ID**: arxiv:2202.02961v1
- **Type**: preprint
- **Published**: 2022-02-07
- **Authors**: Xiaomeng Guo, Yongchao Wang
- **PDF**: https://arxiv.org/pdf/2202.02961v1
- **Abstract**: In this paper, we devote to devise a non-binary low-density parity-check (LDPC) decoder in Galois fields of characteristic two ($\mathbb{F}_{2^q}$) via the alternating direction method of multipliers (ADMM) technique. Through the proposed bit embedding technique and the decomposition technique of the three-variables parity-check equation, an efficient ADMM decoding algorithm for non-binary LDPC codes is proposed. The computation complexity in each ADMM iteration is roughly $\mathcal{O}(nq)$, which is significantly lower than the existing LDPC decoders. Moreover, we prove that the proposed decoder satisfies the favorable property of the codeword-independent. Simulation results demonstrate the outstanding performance of the proposed decoder in contrast with state-of-the-art LDPC decoders.

## Hybrid Neural Coded Modulation: Design and Training Methods

- **ID**: arxiv:2202.01972v1
- **Type**: preprint
- **Published**: 2022-02-04
- **Authors**: Sung Hoon Lim, Jiyong Han, Wonjong Noh +2
- **PDF**: https://arxiv.org/pdf/2202.01972v1
- **Abstract**: We propose a hybrid coded modulation scheme which composes of inner and outer codes. The outer-code can be any standard binary linear code with efficient soft decoding capability (e.g. low-density parity-check (LDPC) codes). The inner code is designed using a deep neural network (DNN) which takes the channel coded bits and outputs modulated symbols. For training the DNN, we propose to use a loss function that is inspired by the generalized mutual information. The resulting constellations are shown to outperform the conventional quadrature amplitude modulation (QAM) based coding scheme for modulation order 16 and 64 with 5G standard LDPC codes.

## Bias-tailored quantum LDPC codes

- **ID**: arxiv:2202.01702v3
- **Type**: preprint
- **Published**: 2022-02-03
- **Authors**: Joschka Roffe, Lawrence Z. Cohen, Armanda O. Quintavalle +2
- **PDF**: https://arxiv.org/pdf/2202.01702v3
- **Abstract**: Bias-tailoring allows quantum error correction codes to exploit qubit noise asymmetry. Recently, it was shown that a modified form of the surface code, the XZZX code, exhibits considerably improved performance under biased noise. In this work, we demonstrate that quantum low density parity check codes can be similarly bias-tailored. We introduce a bias-tailored lifted product code construction that provides the framework to expand bias-tailoring methods beyond the family of 2D topological codes. We present examples of bias-tailored lifted product codes based on classical quasi-cyclic codes and numerically assess their performance using a belief propagation plus ordered statistics decoder. Our Monte Carlo simulations, performed under asymmetric noise, show that bias-tailored codes achieve several orders of magnitude improvement in their error suppression relative to depolarising noise.
