# arXiv — 2007-02 (1차선별 통과)


## On the Complexity of Exact Maximum-Likelihood Decoding for Asymptotically Good Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: expander/LDPC ML 디코딩 LP·O(n^2) 알고리즘과 error floor 제거 가능성 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:cs/0702147v1
- **Type**: preprint
- **Published**: 2007-02-25
- **Authors**: Weiyu Xu, Babak Hassibi
- **PDF**: https://arxiv.org/pdf/cs/0702147v1
- **Abstract**: Since the classical work of Berlekamp, McEliece and van Tilborg, it is well known that the problem of exact maximum-likelihood (ML) decoding of general linear codes is NP-hard. In this paper, we show that exact ML decoding of a classs of asymptotically good error correcting codes--expander codes, a special case of low density parity check (LDPC) codes--over binary symmetric channels (BSCs) is possible with an expected polynomial complexity. More precisely, for any bit-flipping probability, $p$, in a nontrivial range, there exists a rate region of non-zero support and a family of asymptotically good codes, whose error probability decays exponentially in coding length $n$, for which ML decoding is feasible in expected polynomial time. Furthermore, as $p$ approaches zero, this rate region approaches the channel capacity region. The result is based on the existence of polynomial-time suboptimal decoding algorithms that provide an ML certificate and the ability to compute the probability that the suboptimal decoder yields the ML solution. One such ML certificate decoder is the LP decoder of Feldman; we also propose a more efficient $O(n^2)$ algorithm based on the work of Sipser and Spielman and the Ford-Fulkerson algorithm. The results can be extended to AWGN channels and suggest that it may be feasible to eliminate the error floor phenomenon associated with message-passage decoding of LDPC codes in the high SNR regime. Finally, we observe that the argument of Berlekamp, McEliece and van Tilborg can be used to show that ML decoding of the considered class of codes constructed from LDPC codes with regular left degree, of which the considered expander codes are a special case, remains NP-hard; thus giving an interesting contrast between the worst-case and expected complexities.
