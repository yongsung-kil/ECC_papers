# arXiv — 2021-05


## LDPC Codes with Soft Interference Cancellation for Uncoordinated Unsourced Multiple Access

- **ID**: arxiv:2105.13985v1
- **Type**: preprint
- **Published**: 2021-05-28
- **Authors**: Asit Kumar Pradhan, Vamsi K. Amalladinne, Krishna R. Narayanan +1
- **PDF**: https://arxiv.org/pdf/2105.13985v1
- **Abstract**: This article presents a novel enhancement to the random spreading based coding scheme developed by Pradhan et al.\ for the unsourced multiple access channel. The original coding scheme features a polar outer code in conjunction with a successive cancellation list decoder (SCLD) and a hard-input soft-output MMSE estimator. In contrast, the proposed scheme employs a soft-input soft-output MMSE estimator for multi-user detection. This is accomplished by replacing the SCLD based polar code with an LDPC code amenable to belief propagation decoding. This novel framework is leveraged to successfully pass pertinent soft information between the MMSE estimator and the outer code. LDPC codes are carefully designed using density evolution techniques to match the iterative process. This enhanced architecture exhibits significant performance improvements and represents the state-of-the-art over a wide range of system parameters.

## Keeping up with the bits: tracking physical layer latency in millimeter-wave Wi-Fi networks

- **ID**: arxiv:2105.13147v1
- **Type**: preprint
- **Published**: 2021-05-27
- **Authors**: Alexander Marinšek, Liesbet Van der Perre
- **PDF**: https://arxiv.org/pdf/2105.13147v1
- **Abstract**: The wireless communications landscape is anticipated to offer new service levels following the introduction of the millimeter-wave (mmWave) spectrum to consumer electronics. With their broad bandwidths and corresponding multi-Gbps data rates, these mmWaves are a perfect fit for data hungry applications, such as streaming video to extended reality devices. However, the latter are also bound by maximal latency constraints as low as 1 ms. Understanding where such minuscule time delays lurk requires a close-up study of individual layers in the network stack. Starting from the bottom up, the present work describes an endeavor at uncloaking the origins of physical layer (PHY) latency in mmWave Wi-Fi networks. It proposes a newly designed simulation framework and sheds light on how any conventional laboratory can be turned into a virtual experiment setting, speeding up computation. A case study based on the IEEE 802.11ad standard demonstrates the framework's ability to track packet latency at the PHY-level and identify individual bottlenecks. In particular, it evaluates the impact of the number of LDPC decoding iterations on latency in short transmission sequences.

## Communication-Efficient LDPC Code Design for Data Availability Oracle in Side Blockchains

- **ID**: arxiv:2105.06004v2
- **Type**: preprint
- **Published**: 2021-05-12
- **Authors**: Debarnab Mitra, Lev Tauz, Lara Dolecek
- **PDF**: https://arxiv.org/pdf/2105.06004v2
- **Abstract**: A popular method of improving the throughput of blockchain systems is by running smaller side blockchains that push the hashes of their blocks onto a trusted blockchain. Side blockchains are vulnerable to stalling attacks where a side blockchain node pushes the hash of a block to the trusted blockchain but makes the block unavailable to other side blockchain nodes. Recently, Sheng et al. proposed a data availability oracle based on LDPC codes and a data dispersal protocol as a solution to the above problem. While showing improvements, the codes and dispersal protocol were designed disjointly which may not be optimal in terms of the communication cost associated with the oracle. In this paper, we provide a tailored dispersal protocol and specialized LDPC code construction based on the Progressive Edge Growth (PEG) algorithm, called the dispersal-efficient PEG (DE-PEG) algorithm, aimed to reduce the communication cost associated with the new dispersal protocol. Our new code construction reduces the communication cost and, additionally, is less restrictive in terms of system design.

## On Compressed Sensing of Binary Signals for the Unsourced Random Access Channel

- **ID**: arxiv:2105.05350v1
- **Type**: preprint
- **Published**: 2021-05-11
- **Authors**: Elad Romanov, Or Ordentlich
- **PDF**: https://arxiv.org/pdf/2105.05350v1
- **Abstract**: Motivated by applications in unsourced random access, this paper develops a novel scheme for the problem of compressed sensing of binary signals. In this problem, the goal is to design a sensing matrix $A$ and a recovery algorithm, such that the sparse binary vector $\mathbf{x}$ can be recovered reliably from the measurements $\mathbf{y}=A\mathbf{x}+σ\mathbf{z}$, where $\mathbf{z}$ is additive white Gaussian noise. We propose to design $A$ as a parity check matrix of a low-density parity-check code (LDPC), and to recover $\mathbf{x}$ from the measurements $\mathbf{y}$ using a Markov chain Monte Carlo algorithm, which runs relatively fast due to the sparse structure of $A$. The performance of our scheme is comparable to state-of-the-art schemes, which use dense sensing matrices, while enjoying the advantages of using a sparse sensing matrix.

## Necessary and Sufficient Girth Conditions for Tanner Graphs of Quasi-Cyclic LDPC Codes

- **ID**: arxiv:2105.03462v1
- **Type**: preprint
- **Published**: 2021-05-07
- **Authors**: Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://arxiv.org/pdf/2105.03462v1
- **Abstract**: This paper revisits the connection between the girth of a protograph-based LDPC code given by a parity-check matrix and the properties of powers of the product between the matrix and its transpose in order to obtain the necessary and sufficient conditions for a code to have given girth between 6 and 12, and to show how these conditions can be incorporated into simple algorithms to construct codes of that girth. To this end, we highlight the role that certain submatrices that appear in these products have in the construction of codes of desired girth. In particular, we show that imposing girth conditions on a parity-check matrix is equivalent to imposing conditions on a square submatrix obtained from it and we show how this equivalence is particularly strong for a protograph based parity-check matrix of variable node degree 2, where the cycles in its Tanner graph correspond one-to-one to the cycles in the Tanner graph of a square submatrix obtained by adding the permutation matrices (or products of these) in the composition of the parity-check matrix. We end the paper with exemplary constructions of codes with various girths and computer simulations. Although, we mostly assume the case of fully connected protographs of variable node degree 2 and 3, the results can be used for any parity-check matrix/protograph-based Tanner graph.
