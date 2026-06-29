# arXiv — 2022-12 (1차선별 통과)


## Local Probabilistic Decoding of a Quantum Code

- **Status**: ✅
- **Reason**: probabilistic flip + BP 로컬 디코더, O(n) 런타임이 일반 LDPC로 일반화 가능하다고 명시 — 양자 전용 개념 비의존 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2212.06985v3
- **Type**: preprint
- **Published**: 2022-12-14
- **Authors**: T. R. Scruby, K. Nemoto
- **PDF**: https://arxiv.org/pdf/2212.06985v3
- **Abstract**: flip is an extremely simple and maximally local classical decoder which has been used to great effect in certain classes of classical codes. When applied to quantum codes there exist constant-weight errors (such as half of a stabiliser) which are uncorrectable for this decoder, so previous studies have considered modified versions of flip, sometimes in conjunction with other decoders. We argue that this may not always be necessary, and present numerical evidence for the existence of a threshold for flip when applied to the looplike syndromes of a three-dimensional toric code on a cubic lattice. This result can be attributed to the fact that the lowest-weight uncorrectable errors for this decoder are closer (in terms of Hamming distance) to correctable errors than to other uncorrectable errors, and so they are likely to become correctable in future code cycles after transformation by additional noise. Introducing randomness into the decoder can allow it to correct these "uncorrectable" errors with finite probability, and for a decoding strategy that uses a combination of belief propagation and probabilistic flip we observe a threshold of $\sim5.5\%$ under phenomenological noise. This is comparable to the best known threshold for this code ($\sim7.1\%$) which was achieved using belief propagation and ordered statistics decoding [Higgott and Breuckmann, 2022], a strategy with a runtime of $O(n^3)$ as opposed to the $O(n)$ ($O(1)$ when parallelised) runtime of our local decoder. We expect that this strategy could be generalised to work well in other low-density parity check codes, and hope that these results will prompt investigation of other previously overlooked decoders.

## Asymmetric adaptive LDPC-based information reconciliation for industrial quantum key distribution

- **Status**: ✅
- **Reason**: 비대칭 rate-adaptive + blind LDPC information reconciliation — QKD 도메인이나 고전 바이너리 LDPC 기반 레이트적응/블라인드 디코딩 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2212.01121v2
- **Type**: preprint
- **Published**: 2022-12-02
- **Authors**: Nikolay Borisov, Ivan Petrov, Andrey Tayduganov
- **PDF**: https://arxiv.org/pdf/2212.01121v2
- **Abstract**: We develop a new approach for asymmetric LDPC-based information reconciliation in order to adapt to the current channel state and achieve better performance and scalability in practical resource-constrained QKD systems. The new scheme combines the advantages of LDPC codes, a priori error rate estimation, rate-adaptive and blind information reconciliation techniques. We compare the performance of several asymmetric and symmetric error correction schemes using real industrial QKD setup. The proposed asymmetric algorithm achieves significantly higher throughput, providing a secret key rate very close to the symmetric one in a wide range of error rates. Thus, our approach turns out to be particularly efficient for applications with high key rates, limited classical channel capacity and asymmetric computational resource allocation.
