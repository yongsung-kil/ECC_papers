# arXiv — 2006-07 (1차선별 통과)


## Improving convergence of Belief Propagation decoding

- **Status**: ✅
- **Reason**: BP 디코더 수렴 개선(relaxation 파라미터로 Bethe free energy 최소화)은 부호 비의존 디코더 기법(C), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:cs/0607112v1
- **Type**: preprint
- **Published**: 2006-07-25
- **Authors**: M. G. Stepanov, M. Chertkov
- **PDF**: https://arxiv.org/pdf/cs/0607112v1
- **Abstract**: The decoding of Low-Density Parity-Check codes by the Belief Propagation (BP) algorithm is revisited. We check the iterative algorithm for its convergence to a codeword (termination), we run Monte Carlo simulations to find the probability distribution function of the termination time, n_it. Tested on an example [155, 64, 20] code, this termination curve shows a maximum and an extended algebraic tail at the highest values of n_it. Aiming to reduce the tail of the termination curve we consider a family of iterative algorithms modifying the standard BP by means of a simple relaxation. The relaxation parameter controls the convergence of the modified BP algorithm to a minimum of the Bethe free energy. The improvement is experimentally demonstrated for Additive-White-Gaussian-Noise channel in some range of the signal-to-noise ratios. We also discuss the trade-off between the relaxation parameter of the improved iterative scheme and the number of iterations.

## How to Find Good Finite-Length Codes: From Art Towards Science

- **Status**: ✅
- **Reason**: 유한길이 LDPC 코드 최적화(stopping set 기반 erasure 확률 근사)는 코드설계(E)에 이식, BEC지만 바이너리 LDPC 유한길이 설계 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:cs/0607064v1
- **Type**: preprint
- **Published**: 2006-07-13
- **Authors**: Abdelaziz Amraoui, Andrea Montanari, Ruediger Urbanke
- **PDF**: https://arxiv.org/pdf/cs/0607064v1
- **Abstract**: We explain how to optimize finite-length LDPC codes for transmission over the binary erasure channel. Our approach relies on an analytic approximation of the erasure probability. This is in turn based on a finite-length scaling result to model large scale erasures and a union bound involving minimal stopping sets to take into account small error events. We show that the performances of optimized ensembles as observed in simulations are well described by our approximation. Although we only address the case of transmission over the binary erasure channel, our method should be applicable to a more general setting.
