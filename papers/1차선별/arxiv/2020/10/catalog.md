# arXiv — 2020-10 (1차선별 통과)


## Matched Quantized Min-Sum Decoding of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 양자화 min-sum 변형 디코더 + density evolution 분석 — 부호 비의존적이며 NAND LDPC 디코더에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2010.07538v3
- **Type**: preprint
- **Published**: 2020-10-15
- **Authors**: Emna Ben Yacoub
- **PDF**: https://arxiv.org/pdf/2010.07538v3
- **Abstract**: A quantized message passing decoding algorithm for low-density parity-check codes is presented. The algorithm relies on the min approximation at the check nodes, and on modelling the variable node inbound messages as observations of an extrinsic discrete memoryless channel. The performance of the algorithm is analyzed and compared to quantized min-sum decoding by means of density evolution, and almost closes the gap with the performance of the sum-product algorithm. A stability analysis is derived, which highlights the role played by degree-$3$ variable nodes in the stability condition. Finite-length simulation results confirm large gains predicted by the asymptotic analysis.

## Concentrated Stopping Set Design for Coded Merkle Tree: Improving Security Against Data Availability Attacks in Blockchain Systems

- **Status**: ✅
- **Reason**: EC-PEG로 stopping set 제어하는 신규 바이너리 LDPC 코드 구성 — 블록체인 응용이나 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2010.07363v2
- **Type**: preprint
- **Published**: 2020-10-14
- **Authors**: Debarnab Mitra, Lev Tauz, Lara Dolecek
- **PDF**: https://arxiv.org/pdf/2010.07363v2
- **Abstract**: In certain blockchain systems, light nodes are clients that download only a small portion of the block. Light nodes are vulnerable to data availability (DA) attacks where a malicious node hides an invalid portion of the block from the light nodes. Recently, a technique based on erasure codes called Coded Merkle Tree (CMT) was proposed by Yu et al. that enables light nodes to detect a DA attack with high probability. The CMT is constructed using LDPC codes for fast decoding but can fail to detect a DA attack if a malicious node hides a small stopping set of the code. To combat this, Yu et al. used well-studied techniques to design random LDPC codes with high minimum stopping set size. Although effective, these codes are not necessarily optimal for this application. In this paper, we demonstrate a more specialized LDPC code design to improve the security against DA attacks. We achieve this goal by providing a deterministic LDPC code construction that focuses on concentrating stopping sets to a small group of variable nodes rather than only eliminating stopping sets. We design these codes by modifying the Progressive Edge Growth algorithm into a technique called the entropy-constrained PEG (EC-PEG) algorithm. This new method demonstrates a higher probability of detecting DA attacks and allows for good codes at short lengths.

## Learning to Decode: Reinforcement Learning for Decoding of Sparse Graph-Based Channel Codes

- **Status**: ✅
- **Reason**: RL 기반 CN 스케줄링으로 BP 디코딩 성능/복잡도 개선 — 부호 비의존적 디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2010.05637v2
- **Type**: preprint
- **Published**: 2020-10-12
- **Authors**: Salman Habib, Allison Beemer, Joerg Kliewer
- **PDF**: https://arxiv.org/pdf/2010.05637v2
- **Abstract**: We show in this work that reinforcement learning can be successfully applied to decoding short to moderate length sparse graph-based channel codes. Specifically, we focus on low-density parity check (LDPC) codes, which for example have been standardized in the context of 5G cellular communication systems due to their excellent error correcting performance. These codes are typically decoded via belief propagation iterative decoding on the corresponding bipartite (Tanner) graph of the code via flooding, i.e., all check and variable nodes in the Tanner graph are updated at once. In contrast, in this paper we utilize a sequential update policy which selects the optimum check node (CN) scheduling in order to improve decoding performance. In particular, we model the CN update process as a multi-armed bandit process with dependent arms and employ a Q-learning scheme for optimizing the CN scheduling policy. In order to reduce the learning complexity, we propose a novel graph-induced CN clustering approach to partition the state space in such a way that dependencies between clusters are minimized. Our results show that compared to other decoding approaches from the literature, the proposed reinforcement learning scheme not only significantly improves the decoding performance, but also reduces the decoding complexity dramatically once the scheduling policy is learned.
