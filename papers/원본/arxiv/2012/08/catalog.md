# arXiv — 2012-08


## Wave-Like Solutions of General One-Dimensional Spatially Coupled Systems

- **Status**: ✅
- **Reason**: 공간결합 LDPC threshold saturation, BP/min-sum 디코더 분석 — 코드설계/디코더 이식(E/C)
- **ID**: arxiv:1208.5273v3
- **Type**: preprint
- **Published**: 2012-08-27
- **Authors**: Shrinivas Kudekar, Tom Richardson, Ruediger Urbanke
- **PDF**: https://arxiv.org/pdf/1208.5273v3
- **Abstract**: We establish the existence of wave-like solutions to spatially coupled graphical models which, in the large size limit, can be characterized by a one-dimensional real-valued state. This is extended to a proof of the threshold saturation phenomenon for all such models, which includes spatially coupled irregular LDPC codes over the BEC, but also addresses hard-decision decoding for transmission over general channels, the CDMA multiple-access problem, compressed sensing, and some statistical physics models.   For traditional uncoupled iterative coding systems with two components and transmission over the BEC, the asymptotic convergence behavior is completely characterized by the EXIT curves of the components. More precisely, the system converges to the desired fixed point, which is the one corresponding to perfect decoding, if and only if the two EXIT functions describing the components do not cross. For spatially coupled systems whose state is one-dimensional a closely related graphical criterion applies. Now the curves are allowed to cross, but not by too much. More precisely, we show that the threshold saturation phenomenon is related to the positivity of the (signed) area enclosed by two EXIT-like functions associated to the component systems, a very intuitive and easy-to-use graphical characterization.   In the spirit of EXIT functions and Gaussian approximations, we also show how to apply the technique to higher dimensional and even infinite-dimensional cases. In these scenarios the method is no longer rigorous, but it typically gives accurate predictions. To demonstrate this application, we discuss transmission over general channels using both the belief-propagation as well as the min-sum decoder.

## Performance Analysis of Protograph-based LDPC Codes with Spatial Diversity

- **Status**: ❌
- **Reason**: 무선 수신안테나 다이버시티용 표준 protograph LDPC 성능분석 — 떼어낼 신규 디코더/구성 없음(표준 재사용)
- **ID**: arxiv:1208.2394v1
- **Type**: preprint
- **Published**: 2012-08-12
- **Authors**: Yi Fang, Pingping Chen, Lin Wang +2
- **PDF**: https://arxiv.org/pdf/1208.2394v1
- **Abstract**: In wireless communications, spatial diversity techniques, such as space-time block code (STBC) and single-input multiple-output (SIMO), are employed to strengthen the robustness of the transmitted signal against channel fading. This paper studies the performance of protograph-based low-density parity-check (LDPC) codes with receive antenna diversity. We first propose a modified version of the protograph extrinsic information transfer (PEXIT) algorithm and use it for deriving the threshold of the protograph codes in a single-input multiple-output (SIMO) system. We then calculate the decoding threshold and simulate the bit error rate (BER) of two protograph codes (accumulate-repeat-by-3-accumulate (AR3A) code and accumulate-repeat-by-4-jagged-accumulate (AR4JA) code), a regular (3, 6) LDPC code and two optimized irregular LDPC codes. The results reveal that the irregular codes achieve the best error performance in the low signal-to-noise-ratio (SNR) region and the AR3A code outperforms all other codes in the high-SNR region. Utilizing the theoretical analyses and the simulated results, we further discuss the effect of the diversity order on the performance of the protograph codes. Accordingly, the AR3A code stands out as a good candidate for wireless communication systems with multiple receive antennas.

## Fault-Tolerance of "Bad" Quantum Low-Density Parity Check Codes

- **Status**: ❌
- **Reason**: 양자 LDPC(하이퍼그래프-곱/토릭) 부호의 fault-tolerance 이론, 양자 전용 개념 의존, 고전 바이너리 이식 기법 없음
- **ID**: arxiv:1208.2317v2
- **Type**: preprint
- **Published**: 2012-08-11
- **Authors**: Alexey A. Kovalev, Leonid P. Pryadko
- **PDF**: https://arxiv.org/pdf/1208.2317v2
- **Abstract**: We discuss error-correction properties for families of quantum low-density parity check (LDPC) codes with relative distance that tends to zero in the limit of large blocklength. In particular, we show that any family of LDPC codes, quantum or classical, where distance scales as a positive power of the block length, $d \propto n^α$, $α>0$, can correct all errors with certainty if the error rate per (qu)bit is sufficiently small. We specifically analyze the case of LDPC version of the quantum hypergraph-product codes recently suggested by Tillich and Zémor. These codes are a finite-rate generalization of the toric codes, and, for sufficiently large quantum computers, offer an advantage over the toric codes.

## Biff (Bloom Filter) Codes : Fast Error Correction for Large Data Sets

- **Status**: ❌
- **Reason**: Bloom filter 기반 set reconciliation용 erasure-like 코드(Tornado류), 채널 ECC가 아닌 데이터 reconciliation, 떼어낼 LDPC BP 기법 없음
- **ID**: arxiv:1208.0798v1
- **Type**: preprint
- **Published**: 2012-08-03
- **Authors**: Michael Mitzenmacher, George Varghese
- **PDF**: https://arxiv.org/pdf/1208.0798v1
- **Abstract**: Large data sets are increasingly common in cloud and virtualized environments. For example, transfers of multiple gigabytes are commonplace, as are replicated blocks of such sizes. There is a need for fast error-correction or data reconciliation in such settings even when the expected number of errors is small.   Motivated by such cloud reconciliation problems, we consider error-correction schemes designed for large data, after explaining why previous approaches appear unsuitable. We introduce Biff codes, which are based on Bloom filters and are designed for large data. For Biff codes with a message of length $L$ and $E$ errors, the encoding time is $O(L)$, decoding time is $O(L + E)$ and the space overhead is $O(E)$. Biff codes are low-density parity-check codes; they are similar to Tornado codes, but are designed for errors instead of erasures. Further, Biff codes are designed to be very simple, removing any explicit graph structures and based entirely on hash tables. We derive Biff codes by a simple reduction from a set reconciliation algorithm for a recently developed data structure, invertible Bloom lookup tables. While the underlying theory is extremely simple, what makes this code especially attractive is the ease with which it can be implemented and the speed of decoding. We present results from a prototype implementation that decodes messages of 1 million words with thousands of errors in well under a second.
