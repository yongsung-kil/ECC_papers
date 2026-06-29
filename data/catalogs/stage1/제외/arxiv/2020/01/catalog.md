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

## Construction of Rate (n-1)/n Non-Binary LDPC Convolutional Codes via Difference Triangle Sets

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC convolutional code 구성, 바이너리 한정 기준에 따라 제외
- **ID**: arxiv:2001.07969v1
- **Type**: preprint
- **Published**: 2020-01-22
- **Authors**: Gianira N. Alfarano, Julia Lieb, Joachim Rosenthal
- **PDF**: https://arxiv.org/pdf/2001.07969v1
- **Abstract**: This paper provides a construction of non-binary LDPC convolutional codes, which generalizes the work of Robinson and Bernstein. The sets of integers forming an $(n-1,w)$-difference triangle set are used as supports of the columns of rate $(n-1)/n$ convolutional codes. If the field size is large enough, the Tanner graph associated to the sliding parity-check matrix of the code is free from $4$ and $6$-cycles not satisfying the full rank condition. This is important for improving the performance of a code and avoiding the presence of low-weight codewords and absorbing sets. The parameters of the convolutional code are shown to be determined by the parameters of the underlying difference triangle set. In particular, the free distance of the code is related to $w$ and the degree of the code is linked to the "scope" of the difference triangle set. Hence, the problem of finding families of difference triangle set with minimum scope is equivalent to find convolutional codes with small degree.

## Prefix-Free Code Distribution Matching for 5G New Radio

- **Status**: ❌
- **Reason**: 5G NR rate matching용 PCDM(분포정합/소스코딩계), LDPC는 비교 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:2001.05810v1
- **Type**: preprint
- **Published**: 2020-01-16
- **Authors**: Junho Cho, Ori Shental
- **PDF**: https://arxiv.org/pdf/2001.05810v1
- **Abstract**: We use prefix-free code distribution matching (PCDM) for rate matching (RM) in some 5G New Radio (NR) deployment scenarios, realizing a wide range of information rates from 1.4 to 6.0 bit/symbol in fine granularity of 0.2 bit/symbol. We study the performance and implementation of the PCDM-based RM, in comparison with the low-density parity-check (LDPC)-based RM, as defined in the 5G NR standard. Simulations in the additive white Gaussian noise channel show that up to 2.16 dB gain in the signal-to-noise ratio can be obtained with the PCDM-based RM at a block error rate of 10-2 when compared to LDPC-based RM in the tested scenarios, potentially at a smaller hardware cost.
