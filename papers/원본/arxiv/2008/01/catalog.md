# arXiv — 2008-01


## The dimensions of LU(3,q) codes

- **Status**: ❌
- **Reason**: LU(3,q) LDPC 부호의 차원 산정에 관한 순수 대수/조합 이론, 디코더·HW·구성으로 이어지지 않음
- **ID**: arxiv:0802.0015v8
- **Type**: preprint
- **Published**: 2008-01-31
- **Authors**: Ogul Arslan
- **PDF**: https://arxiv.org/pdf/0802.0015v8
- **Abstract**: A family of LDPC codes, called LU(3,q) codes, has been constructed from q-regular bipartite graphs. Recently, P. Sin and Q. Xiang determined the dimensions of these codes in the case that q is a power of an odd prime. They also obtained a lower bound for the dimension of an LU(3,q) code when q is a power of 2. In this paper we prove that this lower bound is the exact dimension of the LU(3,q) code. The proof involves the geometry of symplectic generalized quadrangles, the representation theory of Sp(4,q), and the ring of polynomials.

## On the non-existence for quantum LDPC codes of type IEEE802.16e with rates 1/2 and 2/3B

- **Status**: ❌
- **Reason**: 양자 CSS 부호 구성 가능성(불가능성 증명) 논문, 양자 전용이며 고전 바이너리 LDPC 이식 기법 없음
- **ID**: arxiv:0801.1361v2
- **Type**: preprint
- **Published**: 2008-01-09
- **Authors**: Manabu Hagiwara, Hideki Imai
- **PDF**: https://arxiv.org/pdf/0801.1361v2
- **Abstract**: In this paper, we discuss a construction of CSS codes derived from pairs of practical irregular LDPC codes. Our design of irregular LDPC codes is based the design written in the standardization of IEEE802.16e. Our research has tried to make a CSS code with a pair of LDPC codes of type IEEE802.16e. To our regret, we proved that it was impossible to construct a CSS code if one of classical codes was of type IEEE802.16e with rate 1/2 and 2/3B. We would like to report the discussion on its impossibility in this paper. This is the first paper to analyze the possibility of a CSS code construction by using two irregular LDPC codes which are practically useful.

## Hybrid Decoding of Finite Geometry LDPC Codes

- **Status**: ✅
- **Reason**: 유한기하 LDPC용 하이브리드 BF+Min-Sum 디코더로 복잡도 절감, 바이너리 LDPC BP에 이식 가능한 신규 디코더 알고리즘(C)
- **ID**: arxiv:0801.1208v4
- **Type**: preprint
- **Published**: 2008-01-08
- **Authors**: Guangwen Li, Dashe Li, Yuling Wang +1
- **PDF**: https://arxiv.org/pdf/0801.1208v4
- **Abstract**: For finite geometry low-density parity-check codes, heavy row and column weights in their parity check matrix make the decoding with even Min-Sum (MS) variants computationally expensive. To alleviate it, we present a class of hybrid schemes by concatenating a parallel bit flipping (BF) variant with an Min-Sum (MS) variant. In most SNR region of interest, without compromising performance or convergence rate, simulation results show that the proposed hybrid schemes can save substantial computational complexity with respect to MS variant decoding alone. Specifically, the BF variant, with much less computational complexity, bears most decoding load before resorting to MS variant. Computational and hardware complexity is also elaborated to justify the feasibility of the hybrid schemes.

## The Asymptotic Bit Error Probability of LDPC Codes for the Binary Erasure Channel with Finite Iteration Number

- **Status**: ❌
- **Reason**: BEC 유한반복 비트오류확률 점근식(α/n) 계산 이론, 순수 bound로 디코더/HW/구성으로 안 이어짐
- **ID**: arxiv:0801.0931v2
- **Type**: preprint
- **Published**: 2008-01-07
- **Authors**: Ryuhei Mori, Kenta Kasai, Tomoharu Shibuya +1
- **PDF**: https://arxiv.org/pdf/0801.0931v2
- **Abstract**: We consider communication over the binary erasure channel (BEC) using low-density parity-check (LDPC) code and belief propagation (BP) decoding. The bit error probability for infinite block length is known by density evolution and it is well known that a difference between the bit error probability at finite iteration number for finite block length $n$ and for infinite block length is asymptotically $α/n$, where $α$ is a specific constant depending on the degree distribution, the iteration number and the erasure probability. Our main result is to derive an efficient algorithm for calculating $α$ for regular ensembles. The approximation using $α$ is accurate for $(2,r)$-regular ensembles even in small block length.
