# arXiv — 2020-11


## Topologically Driven Methods for Construction Of Multi-Edge Type (Multigraph with nodes puncturing) Quasi-Cyclic Low-density Parity-check Codes for Wireless Channel, WDM Long-Haul and Archival Holographic Memory

- **ID**: arxiv:2011.14753v3
- **Type**: preprint
- **Published**: 2020-11-30
- **Authors**: Vasiliy Stanislavovich Usatyuk
- **PDF**: https://arxiv.org/pdf/2011.14753v3
- **Abstract**: In this Phd thesis discusses modern methods for constructing MET QC-LDPC codes with a given error correction ("waterfall, error-floor") and complexity (parallelism level according circulant size plus scheduler orthogonality of checks) profiles: 1. weight enumerators optimization, protograph construction using Density Evolution, MI (P/Exit-chart) and it approximation: Gaussian Approximation, Reciprocal-channel approximation and etc; 2. Covariance evolution and it approximation; 3. Lifting methods for QC codes construction:PEG, Guest-and-Test, Hill-Climbing with girth, EMD, ACE optimization; 4. Upper and lower bounds on code distance estimation and its parallel implementation using CPU/GPU; 5. Brouwer-Zimmerman and Number Geometry code distance estimation methods; 6. Importance Sampling for error-floor estimation; 7. Length and rate adaption methods for QC codes based on cyclic group decomposition; 8. Methods for interaction screening which allow to improve performance (decorrelate variables) under BP and it's approximation. We proposed several state-of-the-art methods: Simulated Annealing lifting for MET QC-LDPC codes construction; fast EMD and code distance estimation; floor scale modular lifting for lenght adaption; fast finite-length covariance evolution rate penalty from threshold for code construction and it hardware friendly compression for fast decoder's LLRs unbiasing due SNR's estimation error. We found topology reason's of efficient of such methods using topology thickening (homotopy of continuous and discrete curvature) under matched metric space which allow to generalize this idea to a class of nonlinear codes for Signal Processing and Machine Learning. Using the proposed algorithms several generations of WDM Long-Haul error-correction codes were built. It was applied for "5G eMBB" 3GPP TS38.212 and other applications like Flash storage, Compressed sensing measurement matrix.

## Quantum XYZ Product Codes

- **ID**: arxiv:2011.09746v3
- **Type**: preprint
- **Published**: 2020-11-19
- **Authors**: Anthony Leverrier, Simon Apers, Christophe Vuillot
- **PDF**: https://arxiv.org/pdf/2011.09746v3
- **Abstract**: We study a three-fold variant of the hypergraph product code construction, differing from the standard homological product of three classical codes. When instantiated with 3 classical LDPC codes, this "XYZ product" yields a non CSS quantum LDPC code which might display a large minimum distance. The simplest instance of this construction, corresponding to the product of 3 repetition codes, is a non CSS variant of the 3-dimensional toric code known as the Chamon code. The general construction was introduced in Denise Maurice's PhD thesis, but has remained poorly understood so far. The reason is that while hypergraph product codes can be analyzed with combinatorial tools, the XYZ product codes also depend crucially on the algebraic properties of the parity-check matrices of the three classical codes, making their analysis much more involved.   Our main motivation for studying XYZ product codes is that the natural representatives of logical operators are two-dimensional objects. This contrasts with standard hypergraph product codes in 3 dimensions which always admit one-dimensional logical operators. In particular, specific instances of XYZ product codes with constant rate might display a minimum distance as large as $Θ(N^{2/3})$. While we do not prove this result here, we obtain the dimension of a large class of XYZ product codes, and when restricting to codes with dimension 1, we reduce the problem of computing the minimum distance to a more elementary combinatorial problem involving binary 3-tensors. We also discuss in detail some families of XYZ product codes that can be embedded in three dimensions with local interaction. Some of these codes seem to share properties with Haah's cubic codes and might be interesting candidates for self-correcting quantum memories with a logarithmic energy barrier.

## Learned Decimation for Neural Belief Propagation Decoders

- **ID**: arxiv:2011.02161v1
- **Type**: preprint
- **Published**: 2020-11-04
- **Authors**: Andreas Buchberger, Christian Häger, Henry D. Pfister +2
- **PDF**: https://arxiv.org/pdf/2011.02161v1
- **Abstract**: We introduce a two-stage decimation process to improve the performance of neural belief propagation (NBP), recently introduced by Nachmani et al., for short low-density parity-check (LDPC) codes. In the first stage, we build a list by iterating between a conventional NBP decoder and guessing the least reliable bit. The second stage iterates between a conventional NBP decoder and learned decimation, where we use a neural network to decide the decimation value for each bit. For a (128,64) LDPC code, the proposed NBP with decimation outperforms NBP decoding by 0.75 dB and performs within 1 dB from maximum-likelihood decoding at a block error rate of $10^{-4}$.

## Circuit lower bounds for low-energy states of quantum code Hamiltonians

- **ID**: arxiv:2011.02044v5
- **Type**: preprint
- **Published**: 2020-11-03
- **Authors**: Anurag Anshu, Chinmay Nirkhe
- **PDF**: https://arxiv.org/pdf/2011.02044v5
- **Abstract**: The No Low-energy Trivial States (NLTS) conjecture of Freedman and Hastings, 2014 -- which posits the existence of a local Hamiltonian with a super-constant quantum circuit lower bound on the complexity of all low-energy states -- identifies a fundamental obstacle to the resolution of the quantum PCP conjecture. In this work, we provide new techniques, based on entropic and local indistinguishability arguments, that prove circuit lower bounds for all the low-energy states of local Hamiltonians arising from quantum error-correcting codes.   For local Hamiltonians arising from nearly linear-rate or nearly linear-distance LDPC stabilizer codes, we prove super-constant circuit lower bounds for the complexity of all states of energy o(n). Such codes are known to exist and are not necessarily locally testable, a property previously suspected to be essential for the NLTS conjecture. Curiously, such codes can also be constructed on a two-dimensional lattice, showing that low-depth states cannot accurately approximate the ground-energy even in physically relevant systems.
