# arXiv — 2023-07 (1차선별 통과)


## Spherical and Hyperbolic Toric Topology-Based Codes On Graph Embedding for Ising MRF Models: Classical and Quantum Topology Machine Learning

- **Status**: ✅
- **Reason**: 고전 QC-LDPC trapping set·BP·그래프 임베딩 다룸(bin QC-LDPC 유래), 애매하여 Phase3 재검토 위해 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2307.15778v2
- **Type**: preprint
- **Published**: 2023-07-28
- **Authors**: Vasiliy Usatyuk, Sergey Egorov, Denis Sapozhnikov
- **PDF**: https://arxiv.org/pdf/2307.15778v2
- **Abstract**: The paper introduces the application of information geometry to describe the ground states of Ising models by utilizing parity-check matrices of cyclic and quasi-cyclic codes on toric and spherical topologies. The approach establishes a connection between machine learning and error-correcting coding. This proposed approach has implications for the development of new embedding methods based on trapping sets. Statistical physics and number geometry applied for optimize error-correcting codes, leading to these embedding and sparse factorization methods. The paper establishes a direct connection between DNN architecture and error-correcting coding by demonstrating how state-of-the-art architectures (ChordMixer, Mega, Mega-chunk, CDIL, ...) from the long-range arena can be equivalent to of block and convolutional LDPC codes (Cage-graph, Repeat Accumulate). QC codes correspond to certain types of chemical elements, with the carbon element being represented by the mixed automorphism Shu-Lin-Fossorier QC-LDPC code. The connections between Belief Propagation and the Permanent, Bethe-Permanent, Nishimori Temperature, and Bethe-Hessian Matrix are elaborated upon in detail. The Quantum Approximate Optimization Algorithm (QAOA) used in the Sherrington-Kirkpatrick Ising model can be seen as analogous to the back-propagation loss function landscape in training DNNs. This similarity creates a comparable problem with TS pseudo-codeword, resembling the belief propagation method. Additionally, the layer depth in QAOA correlates to the number of decoding belief propagation iterations in the Wiberg decoding tree. Overall, this work has the potential to advance multiple fields, from Information Theory, DNN architecture design (sparse and structured prior graph topology), efficient hardware design for Quantum and Classical DPU/TPU (graph, quantize and shift register architect.) to Materials Science and beyond.

## Absorbing Sets in Quantum LDPC Codes

- **Status**: ✅
- **Reason**: absorbing/trapping set 프레임워크는 고전 바이너리 LDPC 유래, 반복 디코더 실패 분석 이식 여지 — 애매하여 살림(양자 전용 stabilizer 부분은 Phase3 확인)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2307.14532v2
- **Type**: preprint
- **Published**: 2023-07-26
- **Authors**: Kirsten D. Morris, Tefjol Pllaha, Christine A. Kelley
- **PDF**: https://arxiv.org/pdf/2307.14532v2
- **Abstract**: Iterative decoder failures of quantum low density parity check (QLDPC) codes are attributed to substructures in the code's graph, known as trapping sets, as well as degenerate errors that can arise in quantum codes. Failure inducing sets are subsets of codeword coordinates that, when initially in error, lead to decoding failure in a trapping set. The purpose of this paper is to examine failure inducing sets of QLDPC codes under syndrome-based iterative decoding. As for classical LDPC codes, we show that absorbing sets play a central role in understanding decoder failures. Raveendran and Vasic initiated the study of quantum trapping sets, where beyond the classical-type trapping sets, they identified rigid symmetric structures (a.k.a symmetric stabilizers) responsible for degenerate errors. In this paper, we show that this behavior is part of a much more general phenomenon that can be described by the absorbing set framework.

## Deep learning based enhancement of ordered statistics decoding of short LDPC codes

- **Status**: ✅
- **Reason**: 단축 바이너리 LDPC 대상 신경 min-sum + OSD 결합 디코더 개선(신뢰도 측정·적응적 OSD 경로·복잡도 관리). 이식 가능한 새 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2307.06575v3
- **Type**: preprint
- **Published**: 2023-07-13
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://arxiv.org/pdf/2307.06575v3
- **Abstract**: In the search for highly efficient decoders for short LDPC codes approaching maximum likelihood performance, a relayed decoding strategy, specifically activating the ordered statistics decoding process upon failure of a neural min-sum decoder, is enhanced by instilling three innovations. Firstly, soft information gathered at each step of the neural min-sum decoder is leveraged to forge a new reliability measure using a convolutional neural network. This measure aids in constructing the most reliable basis of ordered statistics decoding, bolstering the decoding process by excluding error-prone bits or concentrating them in a smaller area. Secondly, an adaptive ordered statistics decoding process is introduced, guided by a derived decoding path comprising prioritized blocks, each containing distinct test error patterns. The priority of these blocks is determined from the statistical data during the query phase. Furthermore, effective complexity management methods are devised by adjusting the decoding path's length or refining constraints on the involved blocks. Thirdly, a simple auxiliary criterion is introduced to reduce computational complexity by minimizing the number of candidate codewords before selecting the optimal estimate. Extensive experimental results and complexity analysis strongly support the proposed framework, demonstrating its advantages in terms of high throughput, low complexity, independence from noise variance, in addition to superior decoding performance.
