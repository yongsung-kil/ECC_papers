# arXiv — 2017-01


## Tapering off qubits to simulate fermionic Hamiltonians

- **Status**: ❌
- **Reason**: 양자 시뮬레이션 큐빗 인코딩에 고전 LDPC를 도구로 사용; NAND ECC용 떼어낼 디코더/구성 기법 없음
- **ID**: arxiv:1701.08213v1
- **Type**: preprint
- **Published**: 2017-01-27
- **Authors**: Sergey Bravyi, Jay M. Gambetta, Antonio Mezzacapo +1
- **PDF**: https://arxiv.org/pdf/1701.08213v1
- **Abstract**: We discuss encodings of fermionic many-body systems by qubits in the presence of symmetries. Such encodings eliminate redundant degrees of freedom in a way that preserves a simple structure of the system Hamiltonian enabling quantum simulations with fewer qubits. First we consider $U(1)$ symmetry describing the particle number conservation. Using a previously known encoding based on the first quantization method a system of $M$ fermi modes with $N$ particles can be simulated on a quantum computer with $Q=N\log{(M)}$ qubits. We propose a new version of this encoding tailored to variational quantum algorithms. Also we show how to improve sparsity of the simulator Hamiltonian using orthogonal arrays. Next we consider encodings based on the second quantization method. It is shown that encodings with a given filling fraction $ν=N/M$ and a qubit-per-mode ratio $η=Q/M<1$ can be constructed from efficiently decodable classical LDPC codes with the relative distance $2ν$ and the encoding rate $1-η$. A family of codes based on high-girth bipartite graphs is discussed. Graph-based encodings eliminate roughly $M/N$ qubits. Finally we consider discrete symmetries, and show how to eliminate qubits using previously known encodings, illustrating the technique for simple molecular-type Hamiltonians.

## Design of Capacity Approaching Ensembles of LDPC Codes for Correlated Sources using EXIT Charts

- **Status**: ❌
- **Reason**: 상관 소스용 분산 소스코딩 LDPC 앙상블 설계(EXIT)로 채널 ECC가 아닌 소스/joint 디코딩; 떼어낼 NAND ECC 기법 없음
- **ID**: arxiv:1701.08067v1
- **Type**: preprint
- **Published**: 2017-01-27
- **Authors**: Mohamad Khas Mohamadi, Hamid Saeedi, Reza Asvadi
- **PDF**: https://arxiv.org/pdf/1701.08067v1
- **Abstract**: This paper is concerned with the design of capacity approaching ensembles of Low-Densiy Parity-Check (LDPC) codes for correlated sources. We consider correlated binary sources where the data is encoded independently at each source through a systematic LDPC encoder and sent over two independent channels. At the receiver, a iterative joint decoder consisting of two component LDPC decoders is considered where the encoded bits at the output of each component decoder are used at the other decoder as the a priori information. We first provide asymptotic performance analysis using the concept of extrinsic information transfer (EXIT) charts. Compared to the conventional EXIT charts devised to analyze LDPC codes for point to point communication, the proposed EXIT charts have been completely modified to able to accommodate the systematic nature of the codes as well as the iterative behavior between the two component decoders. Then the developed modified EXIT charts are deployed to design ensembles for different levels of correlation. Our results show that as the average degree of the designed ensembles grow, the thresholds corresponding to the designed ensembles approach the capacity. In particular, for ensembles with average degree of around 9, the gap to capacity is reduced to about 0.2dB. Finite block length performance evaluation is also provided for the designed ensembles to verify the asymptotic results.

## Performance Analysis of Low-Density Parity-Check Codes over 2D Interference Channels via Density Evolution

- **Status**: ❌
- **Reason**: 2D 간섭채널 LDPC 성능을 density evolution으로 분석하는 이론분석; 신규 디코더/구성/HW로 이어지지 않음
- **ID**: arxiv:1701.03840v1
- **Type**: preprint
- **Published**: 2017-01-13
- **Authors**: Jun Yao, Kah Chan Teh, Kwok Hung Li
- **PDF**: https://arxiv.org/pdf/1701.03840v1
- **Abstract**: The theoretical analysis of detection and decoding of low-density parity-check (LDPC) codes transmitted over channels with two-dimensional (2D) interference and additive white Gaussian noise (AWGN) is provided in this paper. The detection and decoding system adopts the joint iterative detection and decoding scheme (JIDDS) in which the log-domain sum-product algorithm is adopted to decode the LDPC codes. The graph representations of the JIDDS are explained. Using the graph representations, we prove that the message-flow neighborhood of the detection and decoding system will be tree-like for a sufficiently long code length. We further confirm that the performance of the JIDDS will concentrate around the performance in which message-flow neighborhood is tree-like. Based on the tree-like message-flow neighborhood, we employ a modified density evolution algorithm to track the message densities during the iterations. A threshold is calculated using the density evolution algorithm which can be considered as the theoretical performance limit of the system. Simulation results demonstrate that the modified density evolution is effective in analyzing the performance of 2D interference systems.

## The Velocity of the Decoding Wave for Spatially Coupled Codes on BMS Channels

- **Status**: ❌
- **Reason**: SC-LDPC 디코딩 파동 속도의 순수 이론 분석(BMS), 디코더/HW/구성 기여 없음
- **ID**: arxiv:1701.03764v1
- **Type**: preprint
- **Published**: 2017-01-13
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://arxiv.org/pdf/1701.03764v1
- **Abstract**: We consider the dynamics of belief propagation decoding of spatially coupled Low-Density Parity-Check codes. It has been conjectured that after a short transient phase, the profile of "error probabilities" along the spatial direction of a spatially coupled code develops a uniquely-shaped wave-like solution that propagates with constant velocity v. Under this assumption, and for transmission over general Binary Memoryless Symmetric channels, we derive a formula for v. We also propose approximations that are simpler to compute and support our findings using numerical data.

## The Velocity of the Propagating Wave for General Coupled Scalar Systems

- **Status**: ❌
- **Reason**: 공간결합 시스템의 진행파 속도 공식 도출 — 순수 이론 bound, Generalized LDPC/압축센싱 응용이며 떼어낼 디코더/HW/구성 기법 없음
- **ID**: arxiv:1701.03759v1
- **Type**: preprint
- **Published**: 2017-01-13
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://arxiv.org/pdf/1701.03759v1
- **Abstract**: We consider spatially coupled systems governed by a set of scalar density evolution equations. Such equations track the behavior of message-passing algorithms used, for example, in coding, sparse sensing, or constraint-satisfaction problems. Assuming that the "profile" describing the average state of the algorithm exhibits a solitonic wave-like behavior after initial transient iterations, we derive a formula for the propagation velocity of the wave. We illustrate the formula with two applications, namely Generalized LDPC codes and compressive sensing.
