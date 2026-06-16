# arXiv — 2013-01


## On the Performance of Low Density Parity Check Codes for Gaussian Interference Channels

- **ID**: arxiv:1301.6643v2
- **Type**: preprint
- **Published**: 2013-01-28
- **Authors**: Shahrouz Sharifi, Tolga M. Duman
- **PDF**: https://arxiv.org/pdf/1301.6643v2
- **Abstract**: In this paper, two-user Gaussian interference channel(GIC) is revisited with the objective of developing implementable (explicit) channel codes. Specifically, low density parity check (LDPC) codes are adopted for use over these channels, and their benefits are studied. Different scenarios on the level of interference are considered. In particular, for strong interference channel examples with binary phase shift keying (BPSK), it is demonstrated that rates better than those offered by single user codes with time sharing are achievable. Promising results are also observed with quadrature-shift-keying (QPSK). Under general interference a Han-Kobayashi coding based scheme is employed splitting the information into public and private parts, and utilizing appropriate iterative decoders at the receivers. Using QPSK modulation at the two transmitters, it is shown that rate points higher than those achievable by time sharing are obtained.

## Linear Programming Decoding of Spatially Coupled Codes

- **ID**: arxiv:1301.6410v2
- **Type**: preprint
- **Published**: 2013-01-27
- **Authors**: Louay Bazzi, Badih Ghazi, Rudiger Urbanke
- **PDF**: https://arxiv.org/pdf/1301.6410v2
- **Abstract**: For a given family of spatially coupled codes, we prove that the LP threshold on the BSC of the graph cover ensemble is the same as the LP threshold on the BSC of the derived spatially coupled ensemble. This result is in contrast with the fact that the BP threshold of the derived spatially coupled ensemble is believed to be larger than the BP threshold of the graph cover ensemble as noted by the work of Kudekar et al. (2011, 2012). To prove this, we establish some properties related to the dual witness for LP decoding which was introduced by Feldman et al. (2007) and simplified by Daskalakis et al. (2008). More precisely, we prove that the existence of a dual witness which was previously known to be sufficient for LP decoding success is also necessary and is equivalent to the existence of certain acyclic hyperflows. We also derive a sublinear (in the block length) upper bound on the weight of any edge in such hyperflows, both for regular LPDC codes and for spatially coupled codes and we prove that the bound is asymptotically tight for regular LDPC codes. Moreover, we show how to trade crossover probability for "LP excess" on all the variable nodes, for any binary linear code.

## A Proof of Threshold Saturation for Spatially-Coupled LDPC Codes on BMS Channels

- **ID**: arxiv:1301.6111v2
- **Type**: preprint
- **Published**: 2013-01-25
- **Authors**: Santhosh Kumar, Andrew J. Young, Nicolas Macris +1
- **PDF**: https://arxiv.org/pdf/1301.6111v2
- **Abstract**: Low-density parity-check (LDPC) convolutional codes have been shown to exhibit excellent performance under low-complexity belief-propagation decoding [1], [2]. This phenomenon is now termed threshold saturation via spatial coupling. The underlying principle behind this appears to be very general and spatially-coupled (SC) codes have been successfully applied in numerous areas. Recently, SC regular LDPC codes have been proven to achieve capacity universally, over the class of binary memoryless symmetric (BMS) channels, under belief-propagation decoding [3], [4].   In [5], [6], potential functions are used to prove that the BP threshold of SC irregular LDPC ensembles saturates, for the binary erasure channel, to the conjectured MAP threshold (known as the Maxwell threshold) of the underlying irregular ensembles. In this paper, that proof technique is generalized to BMS channels, thereby extending some results of [4] to irregular LDPC ensembles. We also believe that this approach can be expanded to cover a wide class of graphical models whose message-passing rules are associated with a Bethe free energy.

## Spatial Coupling as a Proof Technique

- **ID**: arxiv:1301.5676v3
- **Type**: preprint
- **Published**: 2013-01-24
- **Authors**: Andrei Giurgiu, Nicolas Macris, Rüdiger Urbanke
- **PDF**: https://arxiv.org/pdf/1301.5676v3
- **Abstract**: The aim of this paper is to show that spatial coupling can be viewed not only as a means to build better graphical models, but also as a tool to better understand uncoupled models. The starting point is the observation that some asymptotic properties of graphical models are easier to prove in the case of spatial coupling. In such cases, one can then use the so-called interpolation method to transfer known results for the spatially coupled case to the uncoupled one.   Our main use of this framework is for LDPC codes, where we use interpolation to show that the average entropy of the codeword conditioned on the observation is asymptotically the same for spatially coupled as for uncoupled ensembles.   We give three applications of this result for a large class of LDPC ensembles. The first one is a proof of the so-called Maxwell construction stating that the MAP threshold is equal to the Area threshold of the BP GEXIT curve. The second is a proof of the equality between the BP and MAP GEXIT curves above the MAP threshold. The third application is the intimately related fact that the replica symmetric formula for the conditional entropy in the infinite block length limit is exact.

## Binary Diversity for Non-Binary LDPC Codes over the Rayleigh Channel

- **ID**: arxiv:1301.4444v1
- **Type**: preprint
- **Published**: 2013-01-18
- **Authors**: Valentin Savin, David Declercq
- **PDF**: https://arxiv.org/pdf/1301.4444v1
- **Abstract**: In this paper we analyze the performance of several bit-interleaving strategies applied to Non-Binary Low-Density Parity-Check (LDPC) codes over the Rayleigh fading channel. The technique of bit-interleaving used over fading channel introduces diversity which could provide important gains in terms of frame error probability and detection.   This paper demonstrates the importance of the way of implementing the bit-interleaving, and proposes a design of an optimized bit-interleaver inspired from the Progressive Edge Growth algorithm. This optimization algorithm depends on the topological structure of a given LDPC code and can also be applied to any degree distribution and code realization.   In particular, we focus on non-binary LDPC codes based on graph with constant symbol-node connection $d_v = 2$. These regular $(2,dc)$-NB-LDPC codes demonstrate best performance, thanks to their large girths and improved decoding thresholds growing with the order of Finite Field. Simulations show excellent results of the proposed interleaving technique compared to the random interleaver as well as to the system without interleaver.

## A Low-Complexity Encoding of Quasi-Cyclic Codes Based on Galois Fourier Transform

- **ID**: arxiv:1301.3220v1
- **Type**: preprint
- **Published**: 2013-01-15
- **Authors**: Qin Huang, Li Tang, Zulin Wang +2
- **PDF**: https://arxiv.org/pdf/1301.3220v1
- **Abstract**: The encoding complexity of a general (en,ek) quasi-cyclic code is O[(e^2)(n-k)k]. This paper presents a novel low-complexity encoding algorithm for quasi-cyclic (QC) codes based on matrix transformation. First, a message vector is encoded into a transformed codeword in the transform domain. Then, the transmitted codeword is obtained from the transformed codeword by the inverse Galois Fourier transform. For binary QC codes, a simple and fast mapping is required to post-process the transformed codeword such that the transmitted codeword is binary as well. The complexity of our proposed encoding algorithm is O[e(n-k)k] symbol operations for non-binary codes and O[ek(n-k)(log_2 e)] bit operations for binary codes. These complexities are much lower than their traditional counterpart O[(e^2)(n-k)k]. For example, our complexity of encoding a 64-ary (4095,2160) QC code is only 1.59% of that of traditional encoding, and our complexities of encoding the binary (4095, 2160) and (8176, 7154) QC codes are respectively 9.52% and 1.77% of those of traditional encoding. We also study the application of our low-complexity encoding algorithm to one of the most important subclasses of QC codes, namely QC-LDPC codes, especially when their parity-check matrices are rank deficient.
