# arXiv — 2024-04


## GNarsil: Splitting Stabilizers into Gauges

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.18302v1
- **Type**: preprint
- **Published**: 2024-04-28
- **Authors**: Oskar Novak, Narayanan Rengaswamy
- **PDF**: https://arxiv.org/pdf/2404.18302v1
- **Abstract**: Quantum subsystem codes have been shown to improve error-correction performance, ease the implementation of logical operations on codes, and make stabilizer measurements easier by decomposing stabilizers into smaller-weight gauge operators. In this paper, we present two algorithms that produce new subsystem codes from a "seed" CSS code. They replace some stabilizers of a given CSS code with smaller-weight gauge operators that split the remaining stabilizers, while being compatible with the logical Pauli operators of the code. The algorithms recover the well-known Bacon-Shor code computationally as well as produce a new $\left[\left[ 9,1,2,2 \right]\right]$ rotated surface subsystem code with weight-$3$ gauges and weight-$4$ stabilizers. We illustrate using a $\left[\left[ 100,25,3 \right]\right]$ subsystem hypergraph product (SHP) code that the algorithms can produce more efficient gauge operators than the closed-form expressions of the SHP construction. However, we observe that the stabilizers of the lifted product quantum LDPC codes are more challenging to split into small-weight gauge operators. Hence, we introduce the subsystem lifted product (SLP) code construction and develop a new $\left[\left[ 775, 124, 20 \right]\right]$ code from Tanner's classical quasi-cyclic LDPC code. The code has high-weight stabilizers but all gauge operators that split stabilizers have weight $5$, except one. In contrast, the LP stabilizer code from Tanner's code has parameters $\left[\left[ 1054, 124, 20 \right]\right]$. This serves as a novel example of new subsystem codes that outperform stabilizer versions of them. Finally, based on our experiments, we share some general insights about non-locality's effects on the performance of splitting stabilizers into small-weight gauges.

## Toward a 2D Local Implementation of Quantum LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.17676v2
- **Type**: preprint
- **Published**: 2024-04-26
- **Authors**: Noah Berthusen, Dhruv Devulapalli, Eddie Schoute +4
- **PDF**: https://arxiv.org/pdf/2404.17676v2
- **Abstract**: Geometric locality is an important theoretical and practical factor for quantum low-density parity-check (qLDPC) codes which affects code performance and ease of physical realization. For device architectures restricted to 2D local gates, naively implementing the high-rate codes suitable for low-overhead fault-tolerant quantum computing incurs prohibitive overhead. In this work, we present an error correction protocol built on a bilayer architecture that aims to reduce operational overheads when restricted to 2D local gates by measuring some generators less frequently than others. We investigate the family of bivariate bicycle qLDPC codes and show that they are well suited for a parallel syndrome measurement scheme using fast routing with local operations and classical communication (LOCC). Through circuit-level simulations, we find that in some parameter regimes bivariate bicycle codes implemented with this protocol have logical error rates comparable to the surface code while using fewer physical qubits.

## GLDPC-PC Codes: Channel Coding Towards 6G Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.14828v2
- **Type**: preprint
- **Published**: 2024-04-23
- **Authors**: Li Shen, Yongpeng Wu, Yin Xu +3
- **PDF**: https://arxiv.org/pdf/2404.14828v2
- **Abstract**: The sixth generation (6G) wireless communication system will improve the key technical indicators by one to two orders of magnitude, and come with some new features. As a crucial technique to enhance the reliability and efficiency of data transmission, the next-generation channel coding is thus confronted with new challenges in terms of complexity, latency, performance. This article supplies an overview of the potential channel codes for 6G communications. In addition, we explore to develop next-generation channel codes based on lowdensity parity-check (LDPC) and polar frameworks, introducing a concept named generalized LDPC with polar-like component(GLDPC-PC) codes. The codes have exhibited promising error correction performance and manageable complexity, which can be further optimized by specific code design. The opportunities and challenges of GLDPC-PC codes are also discussed.

## High-rate quantum LDPC codes for long-range-connected neutral atom registers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.13010v2
- **Type**: preprint
- **Published**: 2024-04-19
- **Authors**: Laura Pecorari, Sven Jandura, Gavin K. Brennen +1
- **PDF**: https://arxiv.org/pdf/2404.13010v2
- **Abstract**: High-rate quantum error correcting (QEC) codes with moderate overheads in qubit number and control complexity are highly desirable for achieving fault-tolerant quantum computing. Recently, quantum error correction has experienced significant progress both in code development and experimental realizations, with neutral atom qubit architecture rapidly establishing itself as a leading platform in the field. Scalable quantum computing will require processing with QEC codes that have low qubit overhead and large error suppression, and while such codes do exist, they involve a degree of non-locality that has yet to be integrated into experimental platforms. In this work, we analyze a family of high-rate Low-Density Parity-Check (LDPC) codes with limited long-range interactions and outline a near-term implementation in neutral atom registers. By means of circuit-level simulations, we find that these codes outperform surface codes in all respects when the two-qubit nearest neighbour gate error probability is below $\sim 0.1\%$. By using multiple laser colors, we show how these codes can be natively integrated in two-dimensional static neutral atom qubit architectures with open boundaries, where the desired long-range connectivity can be targeted via the Rydberg blockade interaction.

## Fault-tolerant quantum computing with the parity code and noise-biased qubits

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.11332v2
- **Type**: preprint
- **Published**: 2024-04-17
- **Authors**: Anette Messinger, Valentin Torggler, Berend Klaver +2
- **PDF**: https://arxiv.org/pdf/2404.11332v2
- **Abstract**: We present a fault-tolerant universal quantum computing architecture based on a code concatenation of biased-noise qubits and the parity architecture. The parity architecture can be understood as an LDPC code tailored specifically to obtain any desired logical connectivity from nearest-neighbor physical interactions. The code layout can be dynamically adjusted to algorithmic requirements on-the-fly. This allows for implementations with any desired code distance with a universal set of fault-tolerant gates. In addition to the previously explored tool-sets for concatenated cat codes, our approach features parallelizable interactions between arbitrary sets of qubits by directly addressing the parity qubits in the code. The proposed scheme enables codes with less physical qubit overhead compared to the repetition code with the same code distances, while requiring only weight-3 and weight-4 stabilizers and nearest-neighbor 2D square-lattice connectivity.

## Robust Performance Over Changing Intersymbol Interference Channels by Spatial Coupling

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.10367v1
- **Type**: preprint
- **Published**: 2024-04-16
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://arxiv.org/pdf/2404.10367v1
- **Abstract**: We show that spatially coupled low-density parity-check (LDPC) codes yield robust performance over changing intersymbol interfere (ISI) channels with optimal and suboptimal detectors. We compare the performance with classical LDPC code design which involves optimizing the degree distribution for a given (known) channel. We demonstrate that these classical schemes, despite working very good when designed for a given channel, can perform poorly if the channel is exchanged. With spatially coupled LDPC codes, however, we get performances close to the symmetric information rates with just a single code, without the need to know the channel and adapt to it at the transmitter. We also investigate threshold saturation with the linear minimum mean square error (LMMSE) detector and show that with spatial coupling its performance can get remarkably close to that of an optimal detector for regular LDPC codes.

## On the Universality of Spatially Coupled LDPC Codes Over Intersymbol Interference Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.10348v1
- **Type**: preprint
- **Published**: 2024-04-16
- **Authors**: Mgeni Makambi Mashauri, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://arxiv.org/pdf/2404.10348v1
- **Abstract**: In this paper, we derive the exact input/output transfer functions of the optimal a-posteriori probability channel detector for a general ISI channel with erasures. Considering three channel impulse responses of different memory as an example, we compute the BP and MAP thresholds for regular spatially coupled LDPC codes with joint iterative detection and decoding. When we compare the results with the thresholds of ISI channels with Gaussian noise we observe an apparent inconsistency, i.e., a channel which performs better with erasures performs worse with AWGN. We show that this anomaly can be resolved by looking at the thresholds from an entropy perspective. We finally show that with spatial coupling we can achieve the symmetric information rates of different ISI channels using the same code.

## Study of Adaptive Reweighted Sparse Belief Propagation Decoders for Polar Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.04674v1
- **Type**: preprint
- **Published**: 2024-04-06
- **Authors**: R. M. Oliveira, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2404.04674v1
- **Abstract**: In this paper, we present an adaptive reweighted sparse belief propagation (AR-SBP) decoder for polar codes. The AR-SBP technique is inspired by decoders that employ the sum-product algorithm for low-density parity-check codes. In particular, the AR-SBP decoding strategy introduces reweighting of the exchanged log-likelihood-ratio in order to refine the message passing, improving the performance of the decoder and reducing the number of required iterations. An analysis of the convergence of AR-SBP is carried out along with a study of the complexity of the analyzed decoders. Numerical examples show that the AR-SBP decoder outperforms existing decoding algorithms for a reduced number of iterations, enabling low-latency applications.

## Fundamental Limits of Optical Fiber MIMO Channels With Finite Blocklength

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.04477v1
- **Type**: preprint
- **Published**: 2024-04-06
- **Authors**: Xin Zhang, Dongfang Xu, Shenghui Song +1
- **PDF**: https://arxiv.org/pdf/2404.04477v1
- **Abstract**: The multiple-input and multiple-output (MIMO) technique is regarded as a promising approach to boost the throughput and reliability of optical fiber communications. However, the fundamental limits of optical fiber MIMO systems with finite block-length (FBL) are not available in the literature. This paper studies the fundamental limits of optical fiber multicore/multimode systems in the FBL regime when the coding rate is a perturbation within $\mathcal{O}(\frac{1}{\sqrt{ML}})$ of the capacity, where M and L represent the number of transmit channels and blocklength, respectively. Considering the Jacobi MIMO channel, which was proposed to model the nearly lossless propagation and the crosstalks in optical fiber systems, we derive the upper and lower bounds for the optimal error probability. For that purpose, we first set up the central limit theorem for the information density in the asymptotic regime where the number of transmit, receive, available channels and the blocklength go to infinity at the same pace. The result is then utilized to derive the upper and lower bounds for the optimal average error probability with the concerned rate. The derived theoretical results reveal interesting physical insights for Jacobi MIMO channels with FBL. First, the derived bounds for Jacobi channels degenerate to those for Rayleigh channels when the number of available channels approaches infinity. Second, the high signal-to-noise (SNR) approximation indicates that a larger number of available channels results in a larger error probability. Numerical results validate the accuracy of the theoretical results and show that the derived bounds are closer to the performance of practical LDPC codes than outage probability.

## Density Evolution Analysis of Generalized Low-density Parity-check Codes under a Posteriori Probability Decoder

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2404.01136v2
- **Type**: preprint
- **Published**: 2024-04-01
- **Authors**: Dongxu Chang, Qingqing Peng, Zhiming Ma +2
- **PDF**: https://arxiv.org/pdf/2404.01136v2
- **Abstract**: In this study, the performance of generalized low-density parity-check (GLDPC) codes under the a posteriori probability (APP) decoder is analyzed. We explore the concentration, symmetry, and monotonicity properties of GLDPC codes under the APP decoder, extending the applicability of density evolution to GLDPC codes. On the binary memoryless symmetric channels, using the BEC and BI-AWGN channels as two examples, we demonstrate that with an appropriate proportion of generalized constraint (GC) nodes, GLDPC codes can reduce the original gap to capacity compared to their original LDPC counterparts. Additionally, on the BI-AWGN channel, we apply and improve the Gaussian approximation algorithm in the density evolution of GLDPC codes. By adopting Gaussian mixture distributions to approximate the message distributions from variable nodes and Gaussian distributions for those from constraint nodes, the precision of the channel parameter threshold can be significantly enhanced while maintaining a low computational complexity similar to that of Gaussian approximations. Furthermore, we identify a class of subcodes that can greatly simplify the performance analysis and practical decoding of GLDPC codes, which we refer to as message-invariant subcodes. Using the aforementioned techniques, our simulation experiments provide empirical evidence that GLDPC codes, when decoded with the APP decoder and equipped with the right fraction of GC nodes, can achieve substantial performance improvements compared to low-density parity-check (LDPC) codes.
