# arXiv — 2014-07


## Proving Threshold Saturation for Nonbinary SC-LDPC Codes on the Binary Erasure Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.5783v1
- **Type**: preprint
- **Published**: 2014-07-22
- **Authors**: Alexandre Graell i Amat, Iryna Andriyanova, Amina Piemontese
- **PDF**: https://arxiv.org/pdf/1407.5783v1
- **Abstract**: We analyze nonbinary spatially-coupled low-density parity-check (SC-LDPC) codes built on the general linear group for transmission over the binary erasure channel. We prove threshold saturation of the belief propagation decoding to the potential threshold, by generalizing the proof technique based on potential functions recently introduced by Yedla et al.. The existence of the potential function is also discussed for a vector sparse system in the general case, and some existence conditions are developed. We finally give density evolution and simulation results for several nonbinary SC-LDPC code ensembles.

## Quasi-Cyclic LDPC Codes based on Pre-Lifted Protographs

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.5364v1
- **Type**: preprint
- **Published**: 2014-07-21
- **Authors**: David G. M. Mitchell, Roxana Smarandache, Daniel J. Costello
- **PDF**: https://arxiv.org/pdf/1407.5364v1
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes based on protographs are of great interest to code designers because analysis and implementation are facilitated by the protograph structure and the use of circulant permutation matrices for protograph lifting. However, these restrictions impose undesirable fixed upper limits on important code parameters, such as minimum distance and girth. In this paper, we consider an approach to constructing QC-LDPC codes that uses a two-step lifting procedure based on a protograph, and, by following this method instead of the usual one-step procedure, we obtain improved minimum distance and girth properties. We also present two new design rules for constructing good QC-LDPC codes using this two-step lifting procedure, and in each case we obtain a significant increase in minimum distance and achieve a certain guaranteed girth compared to one-step circulant-based liftings. The expected performance improvement is verified by simulation results.

## Rate-Compatible LDPC Codes Based on Puncturing and Extension Techniques for Short Block Lengths

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.5136v1
- **Type**: preprint
- **Published**: 2014-07-19
- **Authors**: J. Liu, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/1407.5136v1
- **Abstract**: In this paper, we investigate novel strategies for generating rate-compatible (RC) irregular low-density parity-check (LDPC) codes with short/moderate block lengths. We propose three puncturing and two extension schemes, which are designed to determine the puncturing positions that minimize the performance degradation and the extension that maximize the performance. The first puncturing scheme employs a counting cycle algorithm and a grouping strategy for variable nodes having short cycles of equal length in the Tanner Graph (TG). The second scheme relies on a metric called Extrinsic Message Degree (EMD) and the third scheme is a simulation-based exhaustive search to find the best puncturing pattern among several random ones. In addition, we devise two layer-structured extension schemes based on a counting cycle algorithm and an EMD metric which are applied to design RC-LDPC codes. Simulation results show that the proposed extension and puncturing techniques achieve greater rate flexibility and good performance over the additive white Gaussian noise (AWGN) channel, outperforming existing techniques.

## Increasing the Speed of Polar List Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.2921v1
- **Type**: preprint
- **Published**: 2014-07-10
- **Authors**: Gabi Sarkis, Pascal Giard, Alexander Vardy +2
- **PDF**: https://arxiv.org/pdf/1407.2921v1
- **Abstract**: In this work, we present a simplified successive cancellation list decoder that uses a Chase-like decoding process to achieve a six time improvement in speed compared to successive cancellation list decoding while maintaining the same error-correction performance advantage over standard successive-cancellation polar decoders. We discuss the algorithm and detail the data structures and methods used to obtain this speed-up. We also propose an adaptive decoding algorithm that significantly improves the throughput while retaining the error-correction performance. Simulation results over the additive white Gaussian noise channel are provided and show that the proposed system is up to 16 times faster than an LDPC decoder of the same frame size, code rate, and similar error-correction performance, making it more suitable for use as a software decoding solution.

## Code optimization, frozen glassy phase and improved decoding algorithms for low-density parity-check codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.0779v2
- **Type**: preprint
- **Published**: 2014-07-03
- **Authors**: Haiping Huang
- **PDF**: https://arxiv.org/pdf/1407.0779v2
- **Abstract**: The statistical physics properties of low-density parity-check codes for the binary symmetric channel are investigated as a spin glass problem with multi-spin interactions and quenched random fields by the cavity method. By evaluating the entropy function at the Nishimori temperature, we find that irregular constructions with heterogeneous degree distribution of check (bit) nodes have higher decoding thresholds compared to regular counterparts with homogeneous degree distribution. We also show that the instability of the mean-field calculation takes place only after the entropy crisis, suggesting the presence of a frozen glassy phase at low temperatures. When no prior knowledge of channel noise is assumed (searching for the ground state), we find that a reinforced strategy on normal belief propagation will boost the decoding threshold to a higher value than the normal belief propagation. This value is close to the dynamical transition where all local search heuristics fail to identify the true message (codeword or the ferromagnetic state). After the dynamical transition, the number of metastable states with larger energy density (than the ferromagnetic state) becomes exponentially numerous. When the noise level of the transmission channel approaches the static transition point, there starts to exist exponentially numerous codewords sharing the identical ferromagnetic energy.

## Lowering the error floor of Gallager codes: a statistical-mechanical view

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1407.0521v2
- **Type**: preprint
- **Published**: 2014-07-02
- **Authors**: Marco Pretti
- **PDF**: https://arxiv.org/pdf/1407.0521v2
- **Abstract**: The problem of error correction for Gallager's low-density parity-check codes is famously equivalent to that of computing marginal Boltzmann probabilities for an Ising-like model with multispin interactions in a non-uniform magnetic field. Since the graph of interactions is locally a tree, the solution is very well approximated by a generalized mean-field (Bethe-Peierls) approximation. Belief propagation (BP) and similar iterative algorithms are an efficient way to perform the calculation, but they sometimes fail to converge, or converge to non-codewords, giving rise to a non-negligible residual error probability (error floor). On the other hand, provably-convergent algorithms are far too complex to be implemented in a real decoder. In this work we consider the application of the probability-damping technique, which can be regarded either as a variant of BP, from which it retains the property of low complexity, or as an approximation of a provably-convergent algorithm, from which it is expected to inherit better convergence properties. We investigate the algorithm behaviour on a real instance of Gallager code, and compare the results with state-of-the-art algorithms.
