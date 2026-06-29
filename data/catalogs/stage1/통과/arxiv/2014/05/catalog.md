# arXiv — 2014-05 (1차선별 통과)


## A Novel Stochastic Decoding of LDPC Codes with Quantitative Guarantees

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 stochastic 디코딩(배선·복잡도 절감) 신규 알고리즘+정량보증 — 이식 가능 디코더/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1405.6353v1
- **Type**: preprint
- **Published**: 2014-05-25
- **Authors**: Nima Noorshams, Aravind Iyengar
- **PDF**: https://arxiv.org/pdf/1405.6353v1
- **Abstract**: Low-density parity-check codes, a class of capacity-approaching linear codes, are particularly recognized for their efficient decoding scheme. The decoding scheme, known as the sum-product, is an iterative algorithm consisting of passing messages between variable and check nodes of the factor graph. The sum-product algorithm is fully parallelizable, owing to the fact that all messages can be update concurrently. However, since it requires extensive number of highly interconnected wires, the fully-parallel implementation of the sum-product on chips is exceedingly challenging. Stochastic decoding algorithms, which exchange binary messages, are of great interest for mitigating this challenge and have been the focus of extensive research over the past decade. They significantly reduce the required wiring and computational complexity of the message-passing algorithm. Even though stochastic decoders have been shown extremely effective in practice, the theoretical aspect and understanding of such algorithms remains limited at large. Our main objective in this paper is to address this issue. We first propose a novel algorithm referred to as the Markov based stochastic decoding. Then, we provide concrete quantitative guarantees on its performance for tree-structured as well as general factor graphs. More specifically, we provide upper-bounds on the first and second moments of the error, illustrating that the proposed algorithm is an asymptotically consistent estimate of the sum-product algorithm. We also validate our theoretical predictions with experimental results, showing we achieve comparable performance to other practical stochastic decoders.

## Quasi Cyclic LDPC Codes Based on Finite Set Systems

- **Status**: ✅
- **Reason**: FSS 기반 QC-LDPC 신규 구성, 큰 girth·임의 column-weight 분포 — 바이너리 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1405.3775v1
- **Type**: preprint
- **Published**: 2014-05-15
- **Authors**: Mohammad Gholami, Mehdi Samadieh
- **PDF**: https://arxiv.org/pdf/1405.3775v1
- **Abstract**: A finite set system (FSS) is a pair (V; B) where V is a finite set whose members are called points, equipped with a finite collection of its subsets B whose members are called blocks. In this paper, finite set systems are used to define a class of Quasi-cyclic low- density parity-check (LDPC) codes, called FSS codes, such that the constructed codes possess large girth and arbitrary column-weight distributions. Especially, the constructed column weight-2 FSS codes have higher rates than the column weight-2 geometric and cylinder-type codes with the same girths. To find the maximum girth of FSS codes based on (V; B), inevitable walks are defined in B such that the maximum girth is determined by the smallest length of the inevitable walks in B. Simulation results show that the constructed FSS codes have very good performance over the AWGN channel with iterative decoding and achieve significantly large coding gains compared to the random-like LDPC codes of the same lengths and rates.
