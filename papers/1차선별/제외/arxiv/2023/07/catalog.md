# arXiv — 2023-07


## qecGPT: decoding Quantum Error-correcting Codes with Generative Pre-trained Transformers

- **Status**: ❌
- **Reason**: 양자 EC 디코더(qecGPT). 스태빌라이저·논리연산자 등 양자 전용 개념에 의존하는 생성형 디코더로 고전 바이너리 LDPC에 그대로 이식 불가 → 원칙 제외
- **ID**: arxiv:2307.09025v1
- **Type**: preprint
- **Published**: 2023-07-18
- **Authors**: Hanyan Cao, Feng Pan, Yijia Wang +1
- **PDF**: https://arxiv.org/pdf/2307.09025v1
- **Abstract**: We propose a general framework for decoding quantum error-correcting codes with generative modeling. The model utilizes autoregressive neural networks, specifically Transformers, to learn the joint probability of logical operators and syndromes. This training is in an unsupervised way, without the need for labeled training data, and is thus referred to as pre-training. After the pre-training, the model can efficiently compute the likelihood of logical operators for any given syndrome, using maximum likelihood decoding. It can directly generate the most-likely logical operators with computational complexity $\mathcal O(2k)$ in the number of logical qubits $k$, which is significantly better than the conventional maximum likelihood decoding algorithms that require $\mathcal O(4^k)$ computation. Based on the pre-trained model, we further propose refinement to achieve more accurately the likelihood of logical operators for a given syndrome by directly sampling the stabilizer operators. We perform numerical experiments on stabilizer codes with small code distances, using both depolarizing error models and error models with correlated noise. The results show that our approach provides significantly better decoding accuracy than the minimum weight perfect matching and belief-propagation-based algorithms. Our framework is general and can be applied to any error model and quantum codes with different topologies such as surface codes and quantum LDPC codes. Furthermore, it leverages the parallelization capabilities of GPUs, enabling simultaneous decoding of a large number of syndromes. Our approach sheds light on the efficient and accurate decoding of quantum error-correcting codes using generative artificial intelligence and modern computational power.

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
