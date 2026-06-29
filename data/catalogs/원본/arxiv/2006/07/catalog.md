# arXiv — 2006-07


## Improving convergence of Belief Propagation decoding

- **Status**: ✅
- **Reason**: BP 디코더 수렴 개선(relaxation 파라미터로 Bethe free energy 최소화)은 부호 비의존 디코더 기법(C), 바이너리 LDPC
- **ID**: arxiv:cs/0607112v1
- **Type**: preprint
- **Published**: 2006-07-25
- **Authors**: M. G. Stepanov, M. Chertkov
- **PDF**: https://arxiv.org/pdf/cs/0607112v1
- **Abstract**: The decoding of Low-Density Parity-Check codes by the Belief Propagation (BP) algorithm is revisited. We check the iterative algorithm for its convergence to a codeword (termination), we run Monte Carlo simulations to find the probability distribution function of the termination time, n_it. Tested on an example [155, 64, 20] code, this termination curve shows a maximum and an extended algebraic tail at the highest values of n_it. Aiming to reduce the tail of the termination curve we consider a family of iterative algorithms modifying the standard BP by means of a simple relaxation. The relaxation parameter controls the convergence of the modified BP algorithm to a minimum of the Bethe free energy. The improvement is experimentally demonstrated for Additive-White-Gaussian-Noise channel in some range of the signal-to-noise ratios. We also discuss the trade-off between the relaxation parameter of the improved iterative scheme and the number of iterations.

## How to Find Good Finite-Length Codes: From Art Towards Science

- **Status**: ✅
- **Reason**: 유한길이 LDPC 코드 최적화(stopping set 기반 erasure 확률 근사)는 코드설계(E)에 이식, BEC지만 바이너리 LDPC 유한길이 설계 기법
- **ID**: arxiv:cs/0607064v1
- **Type**: preprint
- **Published**: 2006-07-13
- **Authors**: Abdelaziz Amraoui, Andrea Montanari, Ruediger Urbanke
- **PDF**: https://arxiv.org/pdf/cs/0607064v1
- **Abstract**: We explain how to optimize finite-length LDPC codes for transmission over the binary erasure channel. Our approach relies on an analytic approximation of the erasure probability. This is in turn based on a finite-length scaling result to model large scale erasures and a union bound involving minimal stopping sets to take into account small error events. We show that the performances of optimized ensembles as observed in simulations are well described by our approximation. Although we only address the case of transmission over the binary erasure channel, our method should be applicable to a more general setting.

## Iterative Decoding Performance Bounds for LDPC Codes on Noisy Channels

- **Status**: ❌
- **Reason**: MS/SP 디코딩 점근 성능의 순수 이론 bound(재귀 상하한)로 디코더/HW/구성으로 이어지지 않음
- **ID**: arxiv:cs/0607020v4
- **Type**: preprint
- **Published**: 2006-07-06
- **Authors**: Chun-Hao Hsu, Achilleas Anastasopoulos
- **PDF**: https://arxiv.org/pdf/cs/0607020v4
- **Abstract**: The asymptotic iterative decoding performances of low-density parity-check (LDPC) codes using min-sum (MS) and sum-product (SP) decoding algorithms on memoryless binary-input output-symmetric (MBIOS) channels are analyzed in this paper. For MS decoding, the analysis is done by upper bounding the bit error probability of the root bit of a tree code by the sequence error probability of a subcode of the tree code assuming the transmission of the all-zero codeword. The result is a recursive upper bound on the bit error probability after each iteration. For SP decoding, we derive a recursively determined lower bound on the bit error probability after each iteration. This recursive lower bound recovers the density evolution equation of LDPC codes on the binary erasure channel (BEC) with inequalities satisfied with equalities. A significant implication of this result is that the performance of LDPC codes under SP decoding on the BEC is an upper bound of the performance on all MBIOS channels with the same uncoded bit error probability. All results hold for the more general multi-edge type LDPC codes.
