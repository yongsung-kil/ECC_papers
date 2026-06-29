# arXiv — 2023-07


## Spherical and Hyperbolic Toric Topology-Based Codes On Graph Embedding for Ising MRF Models: Classical and Quantum Topology Machine Learning

- **Status**: ✅
- **Reason**: 고전 QC-LDPC trapping set·BP·그래프 임베딩 다룸(bin QC-LDPC 유래), 애매하여 Phase3 재검토 위해 살림
- **ID**: arxiv:2307.15778v2
- **Type**: preprint
- **Published**: 2023-07-28
- **Authors**: Vasiliy Usatyuk, Sergey Egorov, Denis Sapozhnikov
- **PDF**: https://arxiv.org/pdf/2307.15778v2
- **Abstract**: The paper introduces the application of information geometry to describe the ground states of Ising models by utilizing parity-check matrices of cyclic and quasi-cyclic codes on toric and spherical topologies. The approach establishes a connection between machine learning and error-correcting coding. This proposed approach has implications for the development of new embedding methods based on trapping sets. Statistical physics and number geometry applied for optimize error-correcting codes, leading to these embedding and sparse factorization methods. The paper establishes a direct connection between DNN architecture and error-correcting coding by demonstrating how state-of-the-art architectures (ChordMixer, Mega, Mega-chunk, CDIL, ...) from the long-range arena can be equivalent to of block and convolutional LDPC codes (Cage-graph, Repeat Accumulate). QC codes correspond to certain types of chemical elements, with the carbon element being represented by the mixed automorphism Shu-Lin-Fossorier QC-LDPC code. The connections between Belief Propagation and the Permanent, Bethe-Permanent, Nishimori Temperature, and Bethe-Hessian Matrix are elaborated upon in detail. The Quantum Approximate Optimization Algorithm (QAOA) used in the Sherrington-Kirkpatrick Ising model can be seen as analogous to the back-propagation loss function landscape in training DNNs. This similarity creates a comparable problem with TS pseudo-codeword, resembling the belief propagation method. Additionally, the layer depth in QAOA correlates to the number of decoding belief propagation iterations in the Wiberg decoding tree. Overall, this work has the potential to advance multiple fields, from Information Theory, DNN architecture design (sparse and structured prior graph topology), efficient hardware design for Quantum and Classical DPU/TPU (graph, quantize and shift register architect.) to Materials Science and beyond.

## Absorbing Sets in Quantum LDPC Codes

- **Status**: ✅
- **Reason**: absorbing/trapping set 프레임워크는 고전 바이너리 LDPC 유래, 반복 디코더 실패 분석 이식 여지 — 애매하여 살림(양자 전용 stabilizer 부분은 Phase3 확인)
- **ID**: arxiv:2307.14532v2
- **Type**: preprint
- **Published**: 2023-07-26
- **Authors**: Kirsten D. Morris, Tefjol Pllaha, Christine A. Kelley
- **PDF**: https://arxiv.org/pdf/2307.14532v2
- **Abstract**: Iterative decoder failures of quantum low density parity check (QLDPC) codes are attributed to substructures in the code's graph, known as trapping sets, as well as degenerate errors that can arise in quantum codes. Failure inducing sets are subsets of codeword coordinates that, when initially in error, lead to decoding failure in a trapping set. The purpose of this paper is to examine failure inducing sets of QLDPC codes under syndrome-based iterative decoding. As for classical LDPC codes, we show that absorbing sets play a central role in understanding decoder failures. Raveendran and Vasic initiated the study of quantum trapping sets, where beyond the classical-type trapping sets, they identified rigid symmetric structures (a.k.a symmetric stabilizers) responsible for degenerate errors. In this paper, we show that this behavior is part of a much more general phenomenon that can be described by the absorbing set framework.

## qecGPT: decoding Quantum Error-correcting Codes with Generative Pre-trained Transformers

- **Status**: ❌
- **Reason**: 양자 EC 디코더(qecGPT). 스태빌라이저·논리연산자 등 양자 전용 개념에 의존하는 생성형 디코더로 고전 바이너리 LDPC에 그대로 이식 불가 → 원칙 제외
- **ID**: arxiv:2307.09025v1
- **Type**: preprint
- **Published**: 2023-07-18
- **Authors**: Hanyan Cao, Feng Pan, Yijia Wang +1
- **PDF**: https://arxiv.org/pdf/2307.09025v1
- **Abstract**: We propose a general framework for decoding quantum error-correcting codes with generative modeling. The model utilizes autoregressive neural networks, specifically Transformers, to learn the joint probability of logical operators and syndromes. This training is in an unsupervised way, without the need for labeled training data, and is thus referred to as pre-training. After the pre-training, the model can efficiently compute the likelihood of logical operators for any given syndrome, using maximum likelihood decoding. It can directly generate the most-likely logical operators with computational complexity $\mathcal O(2k)$ in the number of logical qubits $k$, which is significantly better than the conventional maximum likelihood decoding algorithms that require $\mathcal O(4^k)$ computation. Based on the pre-trained model, we further propose refinement to achieve more accurately the likelihood of logical operators for a given syndrome by directly sampling the stabilizer operators. We perform numerical experiments on stabilizer codes with small code distances, using both depolarizing error models and error models with correlated noise. The results show that our approach provides significantly better decoding accuracy than the minimum weight perfect matching and belief-propagation-based algorithms. Our framework is general and can be applied to any error model and quantum codes with different topologies such as surface codes and quantum LDPC codes. Furthermore, it leverages the parallelization capabilities of GPUs, enabling simultaneous decoding of a large number of syndromes. Our approach sheds light on the efficient and accurate decoding of quantum error-correcting codes using generative artificial intelligence and modern computational power.

## Deep learning based enhancement of ordered statistics decoding of short LDPC codes

- **Status**: ✅
- **Reason**: 단축 바이너리 LDPC 대상 신경 min-sum + OSD 결합 디코더 개선(신뢰도 측정·적응적 OSD 경로·복잡도 관리). 이식 가능한 새 디코더 기법(C)
- **ID**: arxiv:2307.06575v3
- **Type**: preprint
- **Published**: 2023-07-13
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://arxiv.org/pdf/2307.06575v3
- **Abstract**: In the search for highly efficient decoders for short LDPC codes approaching maximum likelihood performance, a relayed decoding strategy, specifically activating the ordered statistics decoding process upon failure of a neural min-sum decoder, is enhanced by instilling three innovations. Firstly, soft information gathered at each step of the neural min-sum decoder is leveraged to forge a new reliability measure using a convolutional neural network. This measure aids in constructing the most reliable basis of ordered statistics decoding, bolstering the decoding process by excluding error-prone bits or concentrating them in a smaller area. Secondly, an adaptive ordered statistics decoding process is introduced, guided by a derived decoding path comprising prioritized blocks, each containing distinct test error patterns. The priority of these blocks is determined from the statistical data during the query phase. Furthermore, effective complexity management methods are devised by adjusting the decoding path's length or refining constraints on the involved blocks. Thirdly, a simple auxiliary criterion is introduced to reduce computational complexity by minimizing the number of candidate codewords before selecting the optimal estimate. Extensive experimental results and complexity analysis strongly support the proposed framework, demonstrating its advantages in terms of high throughput, low complexity, independence from noise variance, in addition to superior decoding performance.

## Improved rate-distance trade-offs for quantum codes with restricted connectivity

- **Status**: ❌
- **Reason**: 양자코드 rate-distance 트레이드오프 순수 이론 bound. 디코더/HW/구성으로 안 이어지는 양자 이론 → 제외
- **ID**: arxiv:2307.03283v1
- **Type**: preprint
- **Published**: 2023-07-06
- **Authors**: Nouédyn Baspin, Venkatesan Guruswami, Anirudh Krishna +1
- **PDF**: https://arxiv.org/pdf/2307.03283v1
- **Abstract**: For quantum error-correcting codes to be realizable, it is important that the qubits subject to the code constraints exhibit some form of limited connectivity. The works of Bravyi & Terhal (BT) and Bravyi, Poulin & Terhal (BPT) established that geometric locality constrains code properties -- for instance $[[n,k,d]]$ quantum codes defined by local checks on the $D$-dimensional lattice must obey $k d^{2/(D-1)} \le O(n)$. Baspin and Krishna studied the more general question of how the connectivity graph associated with a quantum code constrains the code parameters. These trade-offs apply to a richer class of codes compared to the BPT and BT bounds, which only capture geometrically-local codes. We extend and improve this work, establishing a tighter dimension-distance trade-off as a function of the size of separators in the connectivity graph. We also obtain a distance bound that covers all stabilizer codes with a particular separation profile, rather than only LDPC codes.

## Physical Layer Secret Key Agreement Using One-Bit Quantization and Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 무선 물리계층 비밀키 합의용 LLR 계산. Slepian-Wolf LDPC는 소스코딩/정보조정 베이스라인, 떼어낼 채널 ECC 기법 없음 → 제외
- **ID**: arxiv:2307.02391v2
- **Type**: preprint
- **Published**: 2023-07-05
- **Authors**: John A. Snoap
- **PDF**: https://arxiv.org/pdf/2307.02391v2
- **Abstract**: Physical layer approaches for generating secret encryption keys for wireless systems using channel information have attracted increased interest from researchers in recent years. This paper presents a new approach for calculating log-likelihood ratios (LLRs) for secret key generation that is based on one-bit quantization of channel measurements and the difference between channel estimates at legitimate reciprocal nodes. The studied secret key agreement approach, which implements advantage distillation along with information reconciliation using Slepian-Wolf low-density parity-check (LDPC) codes, is discussed and illustrated with numerical results obtained from simulations. These results show the probability of bit disagreement for keys generated using the proposed LLR calculations compared with alternative LLR calculation methods for key generation based on channel state information. The proposed LLR calculations are shown to be an improvement to the studied approach of physical layer secret key agreement.

## Efficient Information Reconciliation for High-Dimensional Quantum Key Distribution

- **Status**: ❌
- **Reason**: QKD 정보조정 + 비이진(nonbinary q-ary) LDPC. 비이진 LDPC이자 채널 ECC 아님 → 제외
- **ID**: arxiv:2307.02225v2
- **Type**: preprint
- **Published**: 2023-07-05
- **Authors**: Ronny Müller, Domenico Ribezzo, Mujtaba Zahidy +3
- **PDF**: https://arxiv.org/pdf/2307.02225v2
- **Abstract**: The Information Reconciliation phase in quantum key distribution has significant impact on the range and throughput of any QKD system. We explore this stage for high-dimensional QKD implementations and introduce two novel methods for reconciliation. The methods are based on nonbinary LDPC codes and the Cascade algorithm, and achieve efficiencies close the the Slepian-Wolf bound on q-ary symmetric channels.
