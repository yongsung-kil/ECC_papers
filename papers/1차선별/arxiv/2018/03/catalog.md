# arXiv — 2018-03 (1차선별 통과)


## Efficient Search of QC-LDPC Codes with Girths 6 and 8 and Free of Elementary Trapping Sets with Small Size

- **Status**: ✅
- **Reason**: girth 6/8 QC-LDPC 탐색 + elementary trapping set 제거 — 바이너리 코드설계/error floor(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1803.08141v1
- **Type**: preprint
- **Published**: 2018-03-21
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi
- **PDF**: https://arxiv.org/pdf/1803.08141v1
- **Abstract**: One of the phenomena that influences significantly the performance of low-density parity-check codes is known as trapping sets. An $(a,b)$ elementary trapping set, or simply an ETS where $a$ is the size and $b$ is the number of degree-one check nodes and $\frac{b}{a}<1$, causes high decoding failure rate and exert a strong influence on the error floor. In this paper, we provide sufficient conditions for exponent matrices to have fully connected $(3,n)$-regular QC-LDPC codes with girths 6 and 8 whose Tanner graphs are free of small ETSs. Applying sufficient conditions on the exponent matrix to remove some 8-cycles results in removing all 4-cycles, 6-cycles as well as some small elementary trapping sets. For each girth we obtain a lower bound on the lifting degree and present exponent matrices with column weight three whose corresponding Tanner graph is free of certain ETSs.

## A Branch-Price-and-Cut Algorithm for Optimal Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 최적(ML) 디코딩 branch-price-and-cut 신규 디코더 — 이식 가능 디코더 연구(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1803.04798v1
- **Type**: preprint
- **Published**: 2018-03-13
- **Authors**: Banu Kabakulak, Z. Caner Taşkın, Ali Emre Pusane
- **PDF**: https://arxiv.org/pdf/1803.04798v1
- **Abstract**: Channel coding aims to minimize errors that occur during the transmission of digital information from one place to another. Low-density parity-check (LDPC) codes can detect and correct transmission errors if one encodes the original information by adding redundant bits. In practice, heuristic iterative decoding algorithms are used to decode the received vector. However, these algorithms may fail to decode if the received vector contains multiple errors. We consider decoding the received vector with minimum error as an integer programming problem and propose a branch-and-price method for its solution. We improve the performance of our method by introducing heuristic feasible solutions and adding valid cuts to the mathematical formulation. Computational results reveal that our branch-price-and-cut algorithm significantly improves solvability of the problem compared to a commercial solver in high channel error rates. Our proposed algorithm can find higher quality solutions than commonly used iterative decoding heuristics.

## Low-Complexity Concatenated LDPC-Staircase Codes

- **Status**: ✅
- **Reason**: 내부 LDPC 코드의 degree distribution 최적화+QC 구성+layered message-passing 디코더 스케줄 등 이식 가능한 코드설계/디코더 기법(C/E) 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1803.01076v2
- **Type**: preprint
- **Published**: 2018-03-02
- **Authors**: Masoud Barakatain, Frank R. Kschischang
- **PDF**: https://arxiv.org/pdf/1803.01076v2
- **Abstract**: A low-complexity soft-decision concatenated FEC scheme, consisting of an inner LDPC code and an outer staircase code is proposed. The inner code is tasked with reducing the bit error probability below the outer-code threshold. The concatenated code is obtained by optimizing the degree distribution of the inner-code ensemble to minimize estimated data-flow, for various choices of outer staircase codes. A key feature that emerges from this optimization is that it pays to leave some inner codeword bits completely uncoded, thereby greatly reducing a significant portion of the decoding complexity. The trade-off between required SNR and decoding complexity of the designed codes is characterized by a Pareto frontier. Computer simulations of the resulting codes reveals that the net coding-gains of existing designs can be achieved with up to 71\% reduction in complexity. A hardware-friendly quasi-cyclic construction is given for the inner codes, which can realize an energy-efficient decoder implementation, and even further complexity reductions via a layered message-passing decoder schedule.
