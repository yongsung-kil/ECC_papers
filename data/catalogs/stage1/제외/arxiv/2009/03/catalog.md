# arXiv — 2009-03


## On the Iterative Decoding of High-Rate LDPC Codes With Applications in Compressed Sensing

- **Status**: ❌
- **Reason**: BEC/q-ary 채널 고율 LDPC 검증디코딩 점근 분석+압축센싱 응용, q-ary/소스복원 위주로 바이너리 NAND ECC 신규 기법 없음
- **ID**: arxiv:0903.2232v4
- **Type**: preprint
- **Published**: 2009-03-12
- **Authors**: Fan Zhang, Henry D. Pfister
- **PDF**: https://arxiv.org/pdf/0903.2232v4
- **Abstract**: This paper considers the performance of $(j,k)$-regular low-density parity-check (LDPC) codes with message-passing (MP) decoding algorithms in the high-rate regime. In particular, we derive the high-rate scaling law for MP decoding of LDPC codes on the binary erasure channel (BEC) and the $q$-ary symmetric channel ($q$-SC). For the BEC, the density evolution (DE) threshold of iterative decoding scales like $Θ(k^{-1})$ and the critical stopping ratio scales like $Θ(k^{-j/(j-2)})$. For the $q$-SC, the DE threshold of verification decoding depends on the details of the decoder and scales like $Θ(k^{-1})$ for one decoder.   Using the fact that coding over large finite alphabets is very similar to coding over the real numbers, the analysis of verification decoding is also extended to the the compressed sensing (CS) of strictly-sparse signals. A DE based approach is used to analyze the CS systems with randomized-reconstruction guarantees. This leads to the result that strictly-sparse signals can be reconstructed efficiently with high-probability using a constant oversampling ratio (i.e., when the number of measurements scales linearly with the sparsity of the signal). A stopping-set based approach is also used to get stronger (e.g., uniform-in-probability) reconstruction guarantees.

## Decay of Correlations for Sparse Graph Error Correcting Codes

- **Status**: ❌
- **Reason**: sparse graph 코드 상관 감쇠 순수 이론(클러스터 전개), 디코더/HW/구성으로 안 이어지는 이론 결과
- **ID**: arxiv:0903.1842v1
- **Type**: preprint
- **Published**: 2009-03-10
- **Authors**: Shrinivas Kudekar, Nicolas Macris
- **PDF**: https://arxiv.org/pdf/0903.1842v1
- **Abstract**: The subject of this paper is transmission over a general class of binary-input memoryless symmetric channels using error correcting codes based on sparse graphs, namely low-density generator-matrix and low-density parity-check codes. The optimal (or ideal) decoder based on the posterior measure over the code bits, and its relationship to the sub-optimal belief propagation decoder, are investigated. We consider the correlation (or covariance) between two codebits, averaged over the noise realizations, as a function of the graph distance, for the optimal decoder. Our main result is that this correlation decays exponentially fast for fixed general low-density generator-matrix codes and high enough noise parameter, and also for fixed general low-density parity-check codes and low enough noise parameter. This has many consequences. Appropriate performance curves - called GEXIT functions - of the belief propagation and optimal decoders match in high/low noise regimes. This means that in high/low noise regimes the performance curves of the optimal decoder can be computed by density evolution. Another interpretation is that the replica predictions of spin-glass theory are exact. Our methods are rather general and use cluster expansions first developed in the context of mathematical statistical mechanics.
