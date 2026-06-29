# arXiv — 2020-01


## Peeling Close to the Orientability Threshold: Spatial Coupling in Hashing-Based Data Structures

- **Status**: ❌
- **Reason**: 해시 자료구조 peelability에 spatial coupling/threshold saturation 차용한 순수 이론, ECC 디코더·구성·HW로 이어지지 않음
- **ID**: arxiv:2001.10500v2
- **Type**: preprint
- **Published**: 2020-01-28
- **Authors**: Stefan Walzer
- **PDF**: https://arxiv.org/pdf/2001.10500v2
- **Abstract**: In multiple-choice data structures each element $x$ in a set $S$ of $m$ keys is associated with a random set $e(x) \subseteq [n]$ of buckets with capacity $\ell \geq 1$ by hash functions. This setting is captured by the hypergraph $H = ([n],\{e(x) \mid x \in S\})$. Accomodating each key in an associated bucket amounts to finding an $\ell$-orientation of $H$ assigning to each hyperedge an incident vertex such that each vertex is assigned at most $\ell$ hyperedges. If each subhypergraph of $H$ has minimum degree at most $\ell$, then an $\ell$-orientation can be found greedily and $H$ is called $\ell$-peelable. Peelability has a central role in invertible Bloom lookup tables and can speed up the construction of retrieval data structures, perfect hash functions and cuckoo hash tables.   Many hypergraphs exhibit sharp density thresholds with respect to $\ell$-orientability and $\ell$-peelability, i.e. as the density $c = \frac{m}{n}$ grows past a critical value, the probability of these properties drops from almost $1$ to almost $0$. In fully random $k$-uniform hypergraphs the thresholds $c_{k,\ell}^*$ for $\ell$-orientability significantly exceed the thresholds for $\ell$-peelability. In this paper, for every $k \geq 2$ and $\ell \geq 1$ with $(k,\ell) \neq (2,1)$ and every $z > 0$, we construct a new family of random $k$-uniform hypergraphs with i.i.d. random hyperedges such that both the $\ell$-peelability and the $\ell$-orientability thresholds approach $c_{k,\ell}^*$ as $z \rightarrow \infty$.   We exploit the phenomenon of threshold saturation via spatial coupling discovered in the context of low-density parity-check codes. Once the connection to data structures is in plain sight, a framework by Kudekar, Richardson and Urbanke (2015) does the heavy lifting in our proof.

## 100Mbps Reconciliation for Quantum Key Distribution Using a Single Graphics Processing Unit

- **Status**: ✅
- **Reason**: QKD reconciliation이나 multi-matrix LDPC 디코딩의 GPU 병렬 구현/처리량 최적화 — 떼어낼 HW/병렬화 기법(D) 가능, 애매하므로 살림
- **ID**: arxiv:2001.07979v1
- **Type**: preprint
- **Published**: 2020-01-22
- **Authors**: Yu Guo, Chaohui Gao, Dong Jiang +1
- **PDF**: https://arxiv.org/pdf/2001.07979v1
- **Abstract**: An efficient error reconciliation scheme is important for post-processing of quantum key distribution (QKD). Recently, a multi-matrix low-density parity-check codes based reconciliation algorithm which can provide remarkable perspectives for high efficiency information reconciliation was proposed. This paper concerns the improvement of reconciliation performance. Multi-matrix algorithm is implemented and optimized on the graphics processing unit (GPU) to obtain high reconciliation throughput. Experimental results indicate that GPU-based algorithm can highly improve reconciliation throughput to an average 85.67 Mbps and a maximum 102.084 Mbps with typical code rate and efficiency. This is the best performance of reconciliation on GPU platform to our knowledge.

## Construction of Rate (n-1)/n Non-Binary LDPC Convolutional Codes via Difference Triangle Sets

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC convolutional code 구성, 바이너리 한정 기준에 따라 제외
- **ID**: arxiv:2001.07969v1
- **Type**: preprint
- **Published**: 2020-01-22
- **Authors**: Gianira N. Alfarano, Julia Lieb, Joachim Rosenthal
- **PDF**: https://arxiv.org/pdf/2001.07969v1
- **Abstract**: This paper provides a construction of non-binary LDPC convolutional codes, which generalizes the work of Robinson and Bernstein. The sets of integers forming an $(n-1,w)$-difference triangle set are used as supports of the columns of rate $(n-1)/n$ convolutional codes. If the field size is large enough, the Tanner graph associated to the sliding parity-check matrix of the code is free from $4$ and $6$-cycles not satisfying the full rank condition. This is important for improving the performance of a code and avoiding the presence of low-weight codewords and absorbing sets. The parameters of the convolutional code are shown to be determined by the parameters of the underlying difference triangle set. In particular, the free distance of the code is related to $w$ and the degree of the code is linked to the "scope" of the difference triangle set. Hence, the problem of finding families of difference triangle set with minimum scope is equivalent to find convolutional codes with small degree.

## Pruning Neural Belief Propagation Decoders

- **Status**: ✅
- **Reason**: neural BP 디코더에서 머신러닝으로 과완비 패리티검사행렬을 가지치기, 반복마다 다른 H 사용 — short LDPC 포함 바이너리 LDPC에 이식 가능한 신경망 디코더 기법(C)
- **ID**: arxiv:2001.07464v2
- **Type**: preprint
- **Published**: 2020-01-21
- **Authors**: Andreas Buchberger, Christian Häger, Henry D. Pfister +2
- **PDF**: https://arxiv.org/pdf/2001.07464v2
- **Abstract**: We consider near maximum-likelihood (ML) decoding of short linear block codes based on neural belief propagation (BP) decoding recently introduced by Nachmani et al.. While this method significantly outperforms conventional BP decoding, the underlying parity-check matrix may still limit the overall performance. In this paper, we introduce a method to tailor an overcomplete parity-check matrix to (neural) BP decoding using machine learning. We consider the weights in the Tanner graph as an indication of the importance of the connected check nodes (CNs) to decoding and use them to prune unimportant CNs. As the pruning is not tied over iterations, the final decoder uses a different parity-check matrix in each iteration. For Reed-Muller and short low-density parity-check codes, we achieve performance within 0.27 dB and 1.5 dB of the ML performance while reducing the complexity of the decoder.

## Prefix-Free Code Distribution Matching for 5G New Radio

- **Status**: ❌
- **Reason**: 5G NR rate matching용 PCDM(분포정합/소스코딩계), LDPC는 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:2001.05810v1
- **Type**: preprint
- **Published**: 2020-01-16
- **Authors**: Junho Cho, Ori Shental
- **PDF**: https://arxiv.org/pdf/2001.05810v1
- **Abstract**: We use prefix-free code distribution matching (PCDM) for rate matching (RM) in some 5G New Radio (NR) deployment scenarios, realizing a wide range of information rates from 1.4 to 6.0 bit/symbol in fine granularity of 0.2 bit/symbol. We study the performance and implementation of the PCDM-based RM, in comparison with the low-density parity-check (LDPC)-based RM, as defined in the 5G NR standard. Simulations in the additive white Gaussian noise channel show that up to 2.16 dB gain in the signal-to-noise ratio can be obtained with the PCDM-based RM at a block error rate of 10-2 when compared to LDPC-based RM in the tested scenarios, potentially at a smaller hardware cost.

## Design of Capacity-Approaching Low-Density Parity-Check Codes using Recurrent Neural Networks

- **Status**: ✅
- **Reason**: RNN으로 Density Evolution 모델링하여 capacity-approaching 바이너리 비정규 LDPC degree 분포 설계 — 이식 가능한 코드 설계 기법(E)
- **ID**: arxiv:2001.01249v1
- **Type**: preprint
- **Published**: 2020-01-05
- **Authors**: Eleni Nisioti, Nikolaos Thomos
- **PDF**: https://arxiv.org/pdf/2001.01249v1
- **Abstract**: In this paper, we model Density Evolution (DE) using Recurrent Neural Networks (RNNs) with the aim of designing capacity-approaching Irregular Low-Density Parity-Check (LDPC) codes for binary erasure channels. In particular, we present a method for determining the coefficients of the degree distributions, characterizing the structure of an LDPC code. We refer to our RNN architecture as Neural Density Evolution (NDE) and determine the weights of the RNN that correspond to optimal designs by minimizing a loss function that enforces the properties of asymptotically optimal design, as well as the desired structural characteristics of the code. This renders the LDPC design process highly configurable, as constraints can be added to meet applications' requirements by means of modifying the loss function. In order to train the RNN, we generate data corresponding to the expected channel noise. We analyze the complexity and optimality of NDE theoretically, and compare it with traditional design methods that employ differential evolution. Simulations illustrate that NDE improves upon differential evolution both in terms of asymptotic performance and complexity. Although we focus on asymptotic settings, we evaluate designs found by NDE for finite codeword lengths and observe that performance remains satisfactory across a variety of channels.
