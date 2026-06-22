# arXiv — 2016-05 (1차선별 통과)


## New Density Evolution Approximation for LDPC and Multi-Edge Type LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC/MET-LDPC 코드 임계값 추정용 신규 density evolution 근사 — 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1605.04665v1
- **Type**: preprint
- **Published**: 2016-05-16
- **Authors**: Sachini Jayasooriya, Mahyar Shirvanimoghaddam, Lawrence Ong +2
- **PDF**: https://arxiv.org/pdf/1605.04665v1
- **Abstract**: This paper considers density evolution for lowdensity parity-check (LDPC) and multi-edge type low-density parity-check (MET-LDPC) codes over the binary input additive white Gaussian noise channel. We first analyze three singleparameter Gaussian approximations for density evolution and discuss their accuracy under several conditions, namely at low rates, with punctured and degree-one variable nodes. We observe that the assumption of symmetric Gaussian distribution for the density-evolution messages is not accurate in the early decoding iterations, particularly at low rates and with punctured variable nodes. Thus single-parameter Gaussian approximation methods produce very poor results in these cases. Based on these observations, we then introduce a new density evolution approximation algorithm for LDPC and MET-LDPC codes. Our method is a combination of full density evolution and a single-parameter Gaussian approximation, where we assume a symmetric Gaussian distribution only after density-evolution messages closely follow a symmetric Gaussian distribution. Our method significantly improves the accuracy of the code threshold estimation. Additionally, the proposed method significantly reduces the computational time of evaluating the code threshold compared to full density evolution thereby making it more suitable for code design.

## A Joint Optimization Technique for Multi-Edge Type LDPC Codes

- **Status**: ✅
- **Reason**: MET-LDPC degree distribution joint 최적화 — 디코딩 임계값 향상, 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1605.04664v1
- **Type**: preprint
- **Published**: 2016-05-16
- **Authors**: Sachini Jayasooriya, Mahyar Shirvanimoghaddam, Lawrence Ong +1
- **PDF**: https://arxiv.org/pdf/1605.04664v1
- **Abstract**: This paper considers the optimization of multi-edge type low-density parity-check (METLDPC) codes to maximize the decoding threshold. We propose an algorithm to jointly optimize the node degree distribution and the multi-edge structure of MET-LDPC codes for given values of the maximum number of edge-types and maximum node degrees. This joint optimization is particularly important for MET-LDPC codes as it is not clear a priori which structures will be good. Using several examples, we demonstrate that the MET-LDPC codes designed by the proposed joint optimization algorithm exhibit improved decoding thresholds compared to previously reported MET-LDPC codes.

## Optimization of Graph Based Codes for Belief Propagation Decoding

- **Status**: ✅
- **Reason**: Tanner 그래프 최적화로 BP 디코딩 임계값 향상하는 신규 코드 최적화 기법 — 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1605.04661v1
- **Type**: preprint
- **Published**: 2016-05-16
- **Authors**: Sachini Jayasooriya, Sarah J. Johnson, Lawrence Ong +1
- **PDF**: https://arxiv.org/pdf/1605.04661v1
- **Abstract**: A low-density parity-check (LDPC) code is a linear block code described by a sparse parity-check matrix, which can be efficiently represented by a bipartite Tanner graph. The standard iterative decoding algorithm, known as belief propagation, passes messages along the edges of this Tanner graph. Density evolution is an efficient method to analyze the performance of the belief propagation decoding algorithm for a particular LDPC code ensemble, enabling the determination of a decoding threshold. The basic problem addressed in this work is how to optimize the Tanner graph so that the decoding threshold is as large as possible. We introduce a new code optimization technique which involves the search space range which can be thought of as minimizing randomness in differential evolution or limiting the search range in exhaustive search. This technique is applied to the design of good irregular LDPC codes and multiedge type LDPC codes.
