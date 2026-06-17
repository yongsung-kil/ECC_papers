# arXiv — 2022-04


## Partitioning qubits in hypergraph product codes to implement logical gates

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2204.10812v3
- **Type**: preprint
- **Published**: 2022-04-22
- **Authors**: Armanda O. Quintavalle, Paul Webster, Michael Vasmer
- **PDF**: https://arxiv.org/pdf/2204.10812v3
- **Abstract**: The promise of high-rate low-density parity check (LDPC) codes to substantially reduce the overhead of fault-tolerant quantum computation depends on constructing efficient, fault-tolerant implementations of logical gates on such codes. Transversal gates are the simplest type of fault-tolerant gate, but the potential of transversal gates on LDPC codes has hitherto been largely neglected. We investigate the transversal gates that can be implemented in hypergraph product codes, a class of LDPC codes. Our analysis is aided by the construction of a symplectic canonical basis for the logical operators of hypergraph product codes, a result that may be of independent interest. We show that in these codes transversal gates can implement Hadamard (up to logical SWAP gates) and control-Z on all logical qubits. Moreover, we show that sequences of transversal operations, interleaved with error correction, allow implementation of entangling gates between arbitrary pairs of logical qubits in the same code block. We thereby demonstrate that transversal gates can be used as the basis for universal quantum computing on LDPC codes, when supplemented with state injection.

## On Quantum-Assisted LDPC Decoding Augmented with Classical Post-Processing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2204.09940v1
- **Type**: preprint
- **Published**: 2022-04-21
- **Authors**: Aditya Das Sarma, Utso Majumder, Vishnu Vaidya +3
- **PDF**: https://arxiv.org/pdf/2204.09940v1
- **Abstract**: Utilizing present and futuristic Quantum Computers to solve difficult problems in different domains has become one of the main endeavors at this moment. Of course, in arriving at the requisite solution both quantum and classical computers work in conjunction. With the continued popularity of Low Density Parity Check (LDPC) codes and hence their decoding, this paper looks into the latter as a Quadratic Unconstrained Binary Optimization (QUBO) and utilized D-Wave 2000Q Quantum Annealer to solve it. The outputs from the Annealer are classically post-processed using simple minimum distance decoding to further improve the performance. We evaluated and compared this implementation against the decoding performance obtained using Simulated Annealing (SA) and belief propagation (BP) decoding with classical computers. The results show that implementations of annealing (both simulated and quantum) are superior to BP decoding and suggest that the advantage becomes more prominent as block lengths increase. Reduced Bit Error Rate (BER) and Frame Error Rate (FER) are observed for simulated annealing and quantum annealing, at useful SNR range - a trend that persists for various codeword lengths.

## LDPC codes: comparing cluster graphs to factor graphs

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2204.06350v2
- **Type**: preprint
- **Published**: 2022-04-13
- **Authors**: J du Toit, J du Preez, R Wolhuter
- **PDF**: https://arxiv.org/pdf/2204.06350v2
- **Abstract**: We present a comparison study between a cluster and factor graph representation of LDPC codes. In probabilistic graphical models, cluster graphs retain useful dependence between random variables during inference, which are advantageous in terms of computational cost, convergence speed, and accuracy of marginal probabilities. This study investigates these benefits in the context of LDPC codes and shows that a cluster graph representation outperforms the traditional factor graph representation.

## LDPC codes: tracking non-stationary channel noise using sequential variational Bayesian estimates

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2204.07037v2
- **Type**: preprint
- **Published**: 2022-04-13
- **Authors**: J du Toit, J du Preez, R Wolhuter
- **PDF**: https://arxiv.org/pdf/2204.07037v2
- **Abstract**: We present a sequential Bayesian learning method for tracking non-stationary signal-to-noise ratios in LDPC codes using probabilistic graphical models. We represent the LDPC code as a cluster graph using a general purpose cluster graph construction algorithm called the layered trees running intersection property (LTRIP) algorithm. The channel noise estimator is a global Gamma cluster, which we extend to allow for Bayesian tracking of non-stationary noise variation. We evaluate our proposed model on real-world 5G drive test data. Our results show that our model is capable of tracking non-stationary channel noise, which outperforms an LDPC code with a fixed knowledge of the actual average channel noise.
