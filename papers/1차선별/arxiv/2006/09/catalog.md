# arXiv — 2006-09 (1차선별 통과)


## Loop Calculus Helps to Improve Belief Propagation and Linear Programming Decodings of Low-Density-Parity-Check Codes

- **Status**: ✅
- **Reason**: loop calculus로 BP/LP 디코딩 개선, pseudo-codeword 제거로 error-floor 저감하는 신규 디코더 기법(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:cs/0609154v1
- **Type**: preprint
- **Published**: 2006-09-28
- **Authors**: Michael Chertkov, Vladimir Y. Chernyak
- **PDF**: https://arxiv.org/pdf/cs/0609154v1
- **Abstract**: We illustrate the utility of the recently developed loop calculus for improving the Belief Propagation (BP) algorithm. If the algorithm that minimizes the Bethe free energy fails we modify the free energy by accounting for a critical loop in a graphical representation of the code. The log-likelihood specific critical loop is found by means of the loop calculus. The general method is tested using an example of the Linear Programming (LP) decoding, that can be viewed as a special limit of the BP decoding. Considering the (155,64,20) code that performs over Additive-White-Gaussian-Noise channel we show that the loop calculus improves the LP decoding and corrects all previously found dangerous configurations of log-likelihoods related to pseudo-codewords with low effective distance, thus reducing the code's error-floor.

## Exhausting Error-Prone Patterns in LDPC Codes

- **Status**: ✅
- **Reason**: trapping set/stopping set 완전탐색 알고리즘+BER/FER 상한으로 유한길이 LDPC error floor 분석·코드설계(E)에 이식 가능, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:cs/0609046v1
- **Type**: preprint
- **Published**: 2006-09-11
- **Authors**: Chih-Chun Wang, Sanjeev R. Kulkarni, H. Vincent Poor
- **PDF**: https://arxiv.org/pdf/cs/0609046v1
- **Abstract**: It is proved in this work that exhaustively determining bad patterns in arbitrary, finite low-density parity-check (LDPC) codes, including stopping sets for binary erasure channels (BECs) and trapping sets (also known as near-codewords) for general memoryless symmetric channels, is an NP-complete problem, and efficient algorithms are provided for codes of practical short lengths n~=500. By exploiting the sparse connectivity of LDPC codes, the stopping sets of size <=13 and the trapping sets of size <=11 can be efficiently exhaustively determined for the first time, and the resulting exhaustive list is of great importance for code analysis and finite code optimization. The featured tree-based narrowing search distinguishes this algorithm from existing ones for which inexhaustive methods are employed. One important byproduct is a pair of upper bounds on the bit-error rate (BER) & frame-error rate (FER) iterative decoding performance of arbitrary codes over BECs that can be evaluated for any value of the erasure probability, including both the waterfall and the error floor regions. The tightness of these upper bounds and the exhaustion capability of the proposed algorithm are proved when combining an optimal leaf-finding module with the tree-based search. These upper bounds also provide a worst-case-performance guarantee which is crucial to optimizing LDPC codes for extremely low error rate applications, e.g., optical/satellite communications. Extensive numerical experiments are conducted that include both randomly and algebraically constructed LDPC codes, the results of which demonstrate the superior efficiency of the exhaustion algorithm and its significant value for finite length code optimization.
