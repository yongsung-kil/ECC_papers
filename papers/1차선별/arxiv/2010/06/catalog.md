# arXiv — 2010-06 (1차선별 통과)


## Tree-structure Expectation Propagation for Decoding LDPC codes over Binary Erasure Channels

- **Status**: ✅
- **Reason**: BEC용 신규 EP 디코더, BP와 동일 복잡도로 더 큰 erasure 정정 — 바이너리 LDPC BP 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1006.1535v1
- **Type**: preprint
- **Published**: 2010-06-08
- **Authors**: Pablo M. Olmos, Juan José Murillo-Fuentes
- **PDF**: https://arxiv.org/pdf/1006.1535v1
- **Abstract**: Expectation Propagation is a generalization to Belief Propagation (BP) in two ways. First, it can be used with any exponential family distribution over the cliques in the graph. Second, it can impose additional constraints on the marginal distributions. We use this second property to impose pair-wise marginal distribution constraints in some check nodes of the LDPC Tanner graph. These additional constraints allow decoding the received codeword when the BP decoder gets stuck. In this paper, we first present the new decoding algorithm, whose complexity is identical to the BP decoder, and we then prove that it is able to decode codewords with a larger fraction of erasures, as the block size tends to infinity. The proposed algorithm can be also understood as a simplification of the Maxwell decoder, but without its computational complexity. We also illustrate that the new algorithm outperforms the BP decoder for finite block-size
