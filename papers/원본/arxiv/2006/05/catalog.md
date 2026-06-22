# arXiv — 2006-05


## Parallel vs. Sequential Belief Propagation Decoding of LDPC Codes over GF(q) and Markov Sources

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 대상의 sequential BP 갱신 기법, 비이진 LDPC는 제외
- **ID**: arxiv:cs/0605069v1
- **Type**: preprint
- **Published**: 2006-05-16
- **Authors**: Nadav Yacov, Hadar Efraim, Haggai Kfir +2
- **PDF**: https://arxiv.org/pdf/cs/0605069v1
- **Abstract**: A sequential updating scheme (SUS) for belief propagation (BP) decoding of LDPC codes over Galois fields, $GF(q)$, and correlated Markov sources is proposed, and compared with the standard parallel updating scheme (PUS). A thorough experimental study of various transmission settings indicates that the convergence rate, in iterations, of the BP algorithm (and subsequently its complexity) for the SUS is about one half of that for the PUS, independent of the finite field size $q$. Moreover, this 1/2 factor appears regardless of the correlations of the source and the channel's noise model, while the error correction performance remains unchanged. These results may imply on the 'universality' of the one half convergence speed-up of SUS decoding.

## A General Method for Finding Low Error Rates of LDPC Codes

- **Status**: ✅
- **Reason**: BP/min-sum 디코더의 저BER 성능 곡선 평가 방법(dominant error event 기반)은 디코더 분석·코드설계(E)에 이식, 바이너리 LDPC
- **ID**: arxiv:cs/0605051v1
- **Type**: preprint
- **Published**: 2006-05-11
- **Authors**: Chad A. Cole, Stephen G. Wilson, Eric. K. Hall +1
- **PDF**: https://arxiv.org/pdf/cs/0605051v1
- **Abstract**: This paper outlines a three-step procedure for determining the low bit error rate performance curve of a wide class of LDPC codes of moderate length. The traditional method to estimate code performance in the higher SNR region is to use a sum of the contributions of the most dominant error events to the probability of error. These dominant error events will be both code and decoder dependent, consisting of low-weight codewords as well as non-codeword events if ML decoding is not used. For even moderate length codes, it is not feasible to find all of these dominant error events with a brute force search. The proposed method provides a convenient way to evaluate very low bit error rate performance of an LDPC code without requiring knowledge of the complete error event weight spectrum or resorting to a Monte Carlo simulation. This new method can be applied to various types of decoding such as the full belief propagation version of the message passing algorithm or the commonly used min-sum approximation to belief propagation. The proposed method allows one to efficiently see error performance at bit error rates that were previously out of reach of Monte Carlo methods. This result will provide a solid foundation for the analysis and design of LDPC codes and decoders that are required to provide a guaranteed very low bit error rate performance at certain SNRs.
