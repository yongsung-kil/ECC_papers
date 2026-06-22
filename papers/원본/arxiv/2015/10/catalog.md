# arXiv — 2015-10


## Some problems of Graph Based Codes for Belief Propagation decoding

- **Status**: ✅
- **Reason**: C/E: HW-friendly QC-LDPC의 trapping set/pseudocodeword 측정·BP 디코딩 개선 기법 — 이식 가능
- **ID**: arxiv:1511.00133v3
- **Type**: preprint
- **Published**: 2015-10-31
- **Authors**: Vasiliy Usatyuk
- **PDF**: https://arxiv.org/pdf/1511.00133v3
- **Abstract**: Short survey about code on the graph by example of hardware friendly quasi-cycle LDPC code. We consider two main properties of code: weight enumerator (well known from classic code theory) and Trapping sets pseudocodewords weight spectrum (a subgraph in code graph's which become reasone of decoding failure under Belief propagation). In paper we show fast methods to measure first components of TS enumerator using EMD=ACE constrains for high girth codes on the graph using graph spectral classification method. This approach simplify solving trouble of agreed between minimal TS pseudocode weight and code distance (which can be measure using knowledge of Authomorphism for algebraic code design methods or measure using lattice reduction(LLL,BKZ) for random graph design methods). In the end of article author raise several challenge problems to improve Sparse and Dense parity-check codes decoding under Belief propagation.

## Computing the minimum distance of nonbinary LDPC codes using block Korkin-Zolotarev method

- **Status**: ❌
- **Reason**: 비이진(ternary) 포함 LDPC minimum distance 측정 알고리즘, 순수 코드거리 계산 도구 — non-binary + 디코더/HW/구성으로 안 이어짐
- **ID**: arxiv:1511.00125v1
- **Type**: preprint
- **Published**: 2015-10-31
- **Authors**: Vasily Usatyuk
- **PDF**: https://arxiv.org/pdf/1511.00125v1
- **Abstract**: In article present measure code distance algorithm of binary and ternary linear block code using block Korkin-Zolotarev (BKZ). Proved the upper bound on scaling constant for measure code distance of non-systematic linear block code using BKZ-method for different value of the block size. Introduced method show linear decrease of runtime from number of threads and work especially good under not dense lattices of LDPC-code. These properties allow use this algorithm to measure the minimal distance of code with length several thousand. The algorithm can further improve by transform into probabilistic algorithm using lattice enumerating pruning techniques

## Error correction for encoded quantum annealing

- **Status**: ❌
- **Reason**: 양자 어닐링 인코딩용 EC, BP 디코딩이나 양자 어닐링 아키텍처 특이적 — 양자 EC 제외
- **ID**: arxiv:1511.00004v3
- **Type**: preprint
- **Published**: 2015-10-30
- **Authors**: Fernando Pastawski, John Preskill
- **PDF**: https://arxiv.org/pdf/1511.00004v3
- **Abstract**: Recently, Lechner, Hauke and Zoller [Science Advances, 1(9)e1500838, (2015)] have proposed a quantum annealing architecture, in which a classical spin glass with all-to-all connectivity is simulated by a spin glass with geometrically local interactions. We interpret this architecture as a classical error-correcting code, which is highly robust against weakly correlated bit-flip noise, and we analyze the code's performance using a belief-propagation decoding algorithm. Our observations may also apply to more general encoding schemes and noise models.

## Iterative Decoding of LDPC Codes over the q-ary Partial Erasure Channel

- **Status**: ❌
- **Reason**: q-ary partial erasure channel용 비이진 LDPC density evolution — 비이진(GF(q)) LDPC라 제외, NAND multi-level read 동기이나 바이너리 한정 기준에 미달
- **ID**: arxiv:1510.05311v2
- **Type**: preprint
- **Published**: 2015-10-18
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://arxiv.org/pdf/1510.05311v2
- **Abstract**: In this paper, we develop a new channel model, which we name the $q$-ary partial erasure channel (QPEC). The QPEC has a $q$-ary input, and its output is either the input symbol or a set of $M$ ($2 \le M \le q$) symbols, containing the input symbol. This channel serves as a generalization to the binary erasure channel, and mimics situations when a symbol output from the channel is known only partially, that is, the output symbol contains some ambiguity, but is not fully erased. This type of channel is motivated by non-volatile memory multi-level read channels. In such channels the readout is obtained by a sequence of current/voltage measurements, which may terminate with partial knowledge of the stored level. Our investigation is concentrated on the performance of low-density parity-check (LDPC) codes when used over this channel, thanks to their low decoding complexity using belief propagation. We provide the exact QPEC density-evolution equations that govern the decoding process, and suggest a cardinality-based approximation as a proxy. We then provide several bounds and approximations on the proxy density evolutions, and verify their tightness through numerical experiments. Finally, we provide tools for the practical design of LDPC codes for use over the QPEC.

## New Characterization and Efficient Exhaustive Search Algorithm for Elementary Trapping Sets of Variable-Regular LDPC Codes

- **Status**: ✅
- **Reason**: variable-regular 바이너리 LDPC의 elementary trapping set 신규 특성화·탐색 알고리즘 — error floor/코드설계(E)에 직접 이식 가능
- **ID**: arxiv:1510.04954v1
- **Type**: preprint
- **Published**: 2015-10-16
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://arxiv.org/pdf/1510.04954v1
- **Abstract**: In this paper, we propose a new characterization for elementary trapping sets (ETSs) of variable-regular low-density parity-check (LDPC) codes. Recently, Karimi and Banihashemi proposed a characterization of ETSs, which was based on viewing an ETS as a layered superset (LSS) of a short cycle in the code's Tanner graph. A notable advantage of LSS characterization is that it corresponds to a simple LSS-based search algorithm that starts from short cycles of the graph and finds the ETSs with LSS structure efficiently. Compared to the LSS-based characterization of Karimi and Banihashemi, which is based on a single LSS expansion technique, the new characterization involves two additional expansion techniques. The introduction of the new techniques mitigates two problems that LSS-based characterization/search suffers from: (1) exhaustiveness, (2) search efficiency. We prove that using the three expansion techniques, any ETS structure can be obtained starting from a simple cycle, no matter how large the size of the structure $a$ or the number of its unsatisfied check nodes $b$ are. We also demonstrate that for the proposed characterization/search to exhaustively cover all the ETS structures within the $(a,b)$ classes with $a \leq a_{max}, b \leq b_{max}$, for any value of $a_{max}$ and $b_{max}$, the length of the short cycles required to be enumerated is less than that of the LSS-based characterization/search. We also prove that the three expansion techniques, proposed here, are the only expansions needed for characterization of ETS structures starting from simple cycles in the graph, if one requires each and every intermediate sub-structure to be an ETS as well. Extensive simulation results are provided to show that, compared to LSS-based search, significant improvement in search speed and memory requirements can be achieved.

## Density Evolution Analysis of Spatially Coupled LDPC Codes Over BIAWGN Channel

- **Status**: ✅
- **Reason**: SC-LDPC density evolution에 reciprocal channel/Gaussian 근사로 복잡도 저감 신규 기법 — 바이너리 LDPC 코드설계(E) 이식 가능
- **ID**: arxiv:1510.04763v1
- **Type**: preprint
- **Published**: 2015-10-16
- **Authors**: Md. Noor-A-Rahim, Gottfried Lechner, Khoa D. Nguyen
- **PDF**: https://arxiv.org/pdf/1510.04763v1
- **Abstract**: In this paper, we study the density evolution analysis of spatially coupled low-density parity-check (SC-LDPC) codes over binary input additive white Gaussian noise (BIAWGN) channels under the belief propagation (BP) decoding algorithm. Using reciprocal channel approximation and Gaussian approximation, we propose averaging techniques for the density evolution of SC-LDPC codes over BIAWGN channels. We show that the proposed techniques can closely predict the decoding threshold while offering reduced complexity compared to the existing multi-edge-type density evolution.

## A Fully-Unrolled LDPC Decoder Based on Quantized Message Passing

- **Status**: ✅
- **Reason**: LUT 기반 finite-alphabet 메시지패싱(min-sum 대체)으로 비트폭 축소 + fully-unrolled HW 아키텍처 — 디코더(C)+HW(D) 핵심 이식 대상
- **ID**: arxiv:1510.04589v1
- **Type**: preprint
- **Published**: 2015-10-15
- **Authors**: Alexios Balatsoukas-Stimming, Michael Meidlinger, Reza Ghanaatian +2
- **PDF**: https://arxiv.org/pdf/1510.04589v1
- **Abstract**: In this paper, we propose a finite alphabet message passing algorithm for LDPC codes that replaces the standard min-sum variable node update rule by a mapping based on generic look-up tables. This mapping is designed in a way that maximizes the mutual information between the decoder messages and the codeword bits. We show that our decoder can deliver the same error rate performance as the conventional decoder with a much smaller message bit-width. Finally, we use the proposed algorithm to design a fully unrolled LDPC decoder hardware architecture.

## Local Hamiltonians Whose Ground States are Hard to Approximate

- **Status**: ❌
- **Reason**: qLDPC/NLTS 추측 관련 local Hamiltonian 양자복잡도 이론 — 양자 전용·순수이론, 고전 바이너리 LDPC로 이어질 이식 기법 없음
- **ID**: arxiv:1510.02082v3
- **Type**: preprint
- **Published**: 2015-10-07
- **Authors**: Lior Eldar, Aram W. Harrow
- **PDF**: https://arxiv.org/pdf/1510.02082v3
- **Abstract**: Ground states of local Hamiltonians can be generally highly entangled: any quantum circuit that generates them (even approximately) must be sufficiently deep to allow coupling (entanglement) between any pair of qubits. Until now this property was not known to be "robust" - the marginals of such states to a subset of the qubits containing all but a small constant fraction of them may be only locally entangled, and hence approximable by shallow quantum circuits. In this work we construct a family of 16-local Hamiltonians for which any 1-10^{-9} fraction of qubits of any ground state must be highly entangled.   This provides evidence that quantum entanglement is not very fragile, and perhaps our intuition about its instability is an artifact of considering local Hamiltonians which are not only local but spatially local. Formally, it provides positive evidence for two wide-open conjectures in condensed-matter physics and quantum complexity theory which are the qLDPC conjecture, positing the existence of "good" quantum LDPC codes, and the NLTS conjecture due to Freedman and Hastings positing the existence of local Hamiltonians in which any low-energy state is highly-entangled.   Our Hamiltonian is based on applying the hypergraph product by Tillich and Zemor to a classical locally testable code. A key tool in our proof is a new lower bound on the vertex expansion of the output of low-depth quantum circuits, which may be of independent interest.
