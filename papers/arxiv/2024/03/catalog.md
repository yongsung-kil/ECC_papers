# arXiv — 2024-03


## On the Performance of Low-complexity Decoders of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2403.19266v3
- **Type**: preprint
- **Published**: 2024-03-28
- **Authors**: Qingqing Peng, Dawei Yin, Dongxu Chang +4
- **PDF**: https://arxiv.org/pdf/2403.19266v3
- **Abstract**: Efficient decoding is crucial to high-throughput and power-sensitive wireless communication scenarios. A theoretical analysis of the performance-complexity tradeoff toward low-complexity decoding is required for a better understanding of the fundamental limits in the above-mentioned scenarios. This study aims to explore the performance of LDPC codes under belief propagation (BP) decoding with complexity constraints. In other words, for a small number of iterations, we present a closed-form lower bound on the bit error rate (BER) of LDPC codes as a function of complexity. Specifically, for the regular LDPC code ensembles, the dominant term in the order of the lower bound we provide matches that of the upper bound given by Lentmaier. Furthermore, for irregular LDPC code ensembles, in addition to adopting the approach used for regular codes, we also propose a method to iteratively obtain the lower bound on the average BER.

## Toward Low-latency Iterative Decoding of QLDPC Codes Under Circuit-Level Noise

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2403.18901v1
- **Type**: preprint
- **Published**: 2024-03-27
- **Authors**: Anqi Gong, Sebastian Cammerer, Joseph M. Renes
- **PDF**: https://arxiv.org/pdf/2403.18901v1
- **Abstract**: We introduce a sliding window decoder based on belief propagation (BP) with guided decimation for the purposes of decoding quantum low-density parity-check codes in the presence of circuit-level noise. Windowed decoding keeps the decoding complexity reasonable when, as is typically the case, repeated rounds of syndrome extraction are required to decode. Within each window, we employ several rounds of BP with decimation of the variable node that we expect to be the most likely to flip in each round, Furthermore, we employ ensemble decoding to keep both decimation options (guesses) open in a small number of chosen rounds. We term the resulting decoder BP with guided decimation guessing (GDG). Applied to bivariate bicycle codes, GDG achieves a similar logical error rate as BP with an additional OSD post-processing stage (BP+OSD) and combination-sweep of order 10. For a window size of three syndrome cycles, a multi-threaded CPU implementation of GDG achieves a worst-case decoding latency of 3ms per window for the [[144,12,12]] code.

## Many-hypercube codes: High-rate quantum error-correcting codes for high-performance fault-tolerant quantum computing

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2403.16054v3
- **Type**: preprint
- **Published**: 2024-03-24
- **Authors**: Hayato Goto
- **PDF**: https://arxiv.org/pdf/2403.16054v3
- **Abstract**: Standard approaches to quantum error correction for fault-tolerant quantum computing are based on encoding a single logical qubit into many physical ones, resulting in asymptotically zero encoding rates and therefore huge resource overheads. To overcome this issue, high-rate quantum codes, such as quantum low-density parity-check codes, have been studied over the past decade. In this case, however, it is difficult to perform logical gates in parallel while maintaining low overheads. Here we propose concatenated high-rate small-size quantum error-detecting codes as a new family of high-rate quantum codes. Their simple structure allows for a geometrical interpretation using hypercubes corresponding to logical qubits. We thus call them many-hypercube codes. They can realize both high rates, e.g., 30% (64 logical qubits are encoded into 216 physical ones), and parallelizability of logical gates. Developing dedicated decoder and encoders, we achieve high error thresholds even in a circuit-level noise model. Thus, the many-hypercube codes will pave the way to high-performance fault-tolerant quantum computing.

## Quantum memory at nonzero temperature in a thermodynamically trivial system

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2403.10599v3
- **Type**: preprint
- **Published**: 2024-03-15
- **Authors**: Yifan Hong, Jinkang Guo, Andrew Lucas
- **PDF**: https://arxiv.org/pdf/2403.10599v3
- **Abstract**: Passive error correction protects logical information forever in the thermodynamic limit by updating the system based only on local information and few-body interactions. A paradigmatic example is the classical two-dimensional Ising model: a Metropolis-style Gibbs sampler retains the sign of the initial magnetization (a logical bit) for thermodynamically long times in the low-temperature phase. Known models of passive quantum error correction similarly exhibit thermodynamic phase transitions to a low-temperature phase wherein logical qubits are protected by thermally stable topological order. Here, in contrast, we show that certain families of constant-rate classical and quantum low-density parity check codes have no thermodynamic phase transitions at nonzero temperature, but nonetheless exhibit ergodicity-breaking dynamical transitions: below a critical nonzero temperature, the mixing time of local Gibbs sampling diverges in the thermodynamic limit. Slow Gibbs sampling of such codes enables fault-tolerant passive quantum error correction using finite-depth circuits. This strategy is well suited to measurement-free quantum error correction and may present a desirable experimental alternative to conventional quantum error correction based on syndrome measurements and active feedback.

## Low-density parity-check representation of fault-tolerant quantum circuits

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2403.10268v2
- **Type**: preprint
- **Published**: 2024-03-15
- **Authors**: Ying Li
- **PDF**: https://arxiv.org/pdf/2403.10268v2
- **Abstract**: In fault-tolerant quantum computing, quantum algorithms are implemented through quantum circuits capable of error correction. These circuits are typically constructed based on specific quantum error correction codes, with consideration given to the characteristics of the underlying physical platforms. Optimising these circuits within the constraints of today's quantum computing technologies, particularly in terms of error rates, qubit counts, and network topologies, holds substantial implications for the feasibility of quantum applications in the near future. This paper presents a toolkit for designing and analysing fault-tolerant quantum circuits. We introduce a framework for representing stabiliser circuits using classical low-density parity-check (LDPC) codes. Each codeword in the representation corresponds to a quantum-mechanical equation regarding the circuit, formalising the correlations utilised in parity checks and delineating logical operations within the circuit. Consequently, the LDPC code provides a means of quantifying fault tolerance and verifying logical operations. We outline the procedure for generating LDPC codes from circuits using the Tanner graph notation, alongside proposing graph-theory tools for constructing fault-tolerant quantum circuits from classical LDPC codes. These findings offer a systematic approach to applying classical error correction techniques in optimising existing fault-tolerant protocols and developing new ones.   As an example, we develop a resource-efficient scheme for universal fault-tolerant quantum computing on hypergraph product codes based on the LDPC representation.
