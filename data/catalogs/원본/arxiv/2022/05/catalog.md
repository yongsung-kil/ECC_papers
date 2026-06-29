# arXiv — 2022-05


## SPANSE: combining sparsity with density for efficient one-time code-based digital signatures

- **Status**: ❌
- **Reason**: QC-LDPC/MDPC 기반 코드기반 디지털 서명(암호) — 채널코딩 ECC 아님, 보안 응용, 떼어낼 디코더/HW 기여 없음
- **ID**: arxiv:2205.12887v1
- **Type**: preprint
- **Published**: 2022-05-25
- **Authors**: Marco Baldi, Franco Chiaraluce, Paolo Santini
- **PDF**: https://arxiv.org/pdf/2205.12887v1
- **Abstract**: The use of codes defined by sparse characteristic matrices, like QC-LDPC and QC-MDPC codes, has become an established solution to design secure and efficient code-based public-key encryption schemes, as also witnessed by the ongoing NIST post-quantum cryptography standardization process. However, similar approaches have been less fortunate in the context of code-based digital signatures, since no secure and efficient signature scheme based on these codes is available to date. The main limitation of previous attempts in this line of research has been the use of sparse signatures, which produces some leakage of information about the private key. In this paper, we propose a new code-based digital signature scheme that overcomes such a problem by publishing signatures that are abnormally dense, rather than sparse. This eliminates the possibility of deducing information from the sparsity of signatures, and follows a recent trend in code-based cryptography exploiting the hardness of the decoding problem for large-weight vectors, instead of its classical version based on small-weight vectors. In this study we focus on one-time use and provide some preliminary instances of the new scheme, showing that it achieves very fast signature generation and verification with reasonably small public keys.

## Data post-processing for the one-way heterodyne protocol under composable finite-size security

- **Status**: ❌
- **Reason**: CV-QKD 후처리(비이진 LDPC 사용) — 비이진 LDPC이며 QKD 보안 응용, 이중으로 제외
- **ID**: arxiv:2205.10142v2
- **Type**: preprint
- **Published**: 2022-05-20
- **Authors**: Alexander George Mountogiannakis, Panagiotis Papanastasiou, Stefano Pirandola
- **PDF**: https://arxiv.org/pdf/2205.10142v2
- **Abstract**: The performance of a practical continuous-variable (CV) quantum key distribution (QKD) protocol depends significantly, apart from the loss and noise of the quantum channel, on the post-processing steps which lead to the extraction of the final secret key. A critical step is the reconciliation process, especially when one assumes finite-size effects in a composable framework. Here, we focus on the Gaussian-modulated coherent-state protocol with heterodyne detection in a high signal-to-noise ratio regime. We simulate the quantum communication process and we post-process the output data by applying parameter estimation, error correction (using high-rate, non-binary low-density parity-check codes), and privacy amplification. This allows us to study the performance for practical implementations of the protocol and optimize the parameters connected to the steps above. We also present an associated Python library performing the steps above.

## A Novel K-Repetition Design for SCMA

- **Status**: ❌
- **Reason**: SCMA용 K-Repetition HARQ + 네트워크코딩 — LDPC는 베이스라인, 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: arxiv:2205.08149v1
- **Type**: preprint
- **Published**: 2022-05-17
- **Authors**: Ke Lai, Zilong Liu, Jing Lei +3
- **PDF**: https://arxiv.org/pdf/2205.08149v1
- **Abstract**: This work presents a novel K-Repetition based HARQ scheme for LDPC coded uplink SCMA by employing a network coding (NC) principle to encode different packets, where K-Repetition is an emerging technique (recommended in 3GPP Release 15) for enhanced reliability and reduced latency in future massive machine-type communication. Such a scheme is referred to as the NC aided K-repetition SCMA (NCK-SCMA). We introduce a joint iterative detection algorithm for improved detection of the data from the proposed LDPC coded NCKSCMA systems. Simulation results demonstrate the benefits of NCK-SCMA with higher throughput and improved reliability over the conventional K-Repetition SCMA.

## Stabilizer Inactivation for Message-Passing Decoding of Quantum LDPC Codes

- **Status**: ❌
- **Reason**: 양자 LDPC MP 디코딩 후처리(stabilizer-inactivation) — 스태빌라이저 개념에 의존, 양자 전용, 고전 이식 불가, 원칙 제외
- **ID**: arxiv:2205.06125v3
- **Type**: preprint
- **Published**: 2022-05-12
- **Authors**: Julien du Crest, Mehdi Mhalla, Valentin Savin
- **PDF**: https://arxiv.org/pdf/2205.06125v3
- **Abstract**: We propose a post-processing method for message-passing (MP) decoding of CSS quantum LDPC codes, called stabilizer-inactivation (SI). It relies on inactivating a set of qubits, supporting a check in the dual code, and then running the MP decoding again. This allows MP decoding to converge outside the inactivated set of qubits, while the error on these is determined by solving a small, constant size, linear system. Compared to the state of the art post-processing method based on ordered statistics decoding (OSD), we show through numerical simulations that MP-SI outperforms MP-OSD for different quantum LDPC code constructions, different MP decoding algorithms, and different MP scheduling strategies, while having a significantly reduced complexity.

## Soft Syndrome Decoding of Quantum LDPC Codes for Joint Correction of Data and Syndrome Errors

- **Status**: ✅
- **Reason**: syndrome soft-information을 활용한 BP 반복 디코더 개선 — 양자 코드지만 소프트 신드롬+BP 기법이 고전 바이너리 LDPC 소프트정보 디코딩에 이식 가능성, 애매하여 살림(Phase 3)
- **ID**: arxiv:2205.02341v1
- **Type**: preprint
- **Published**: 2022-05-04
- **Authors**: Nithin Raveendran, Narayanan Rengaswamy, Asit Kumar Pradhan +1
- **PDF**: https://arxiv.org/pdf/2205.02341v1
- **Abstract**: Quantum errors are primarily detected and corrected using the measurement of syndrome information which itself is an unreliable step in practical error correction implementations. Typically, such faulty or noisy syndrome measurements are modeled as a binary measurement outcome flipped with some probability. However, the measured syndrome is in fact a discretized value of the continuous voltage or current values obtained in the physical implementation of the syndrome extraction. In this paper, we use this "soft" or analog information without the conventional discretization step to benefit the iterative decoders for decoding quantum low-density parity-check (QLDPC) codes. Syndrome-based iterative belief propagation decoders are modified to utilize the syndrome-soft information to successfully correct both data and syndrome errors simultaneously, without repeated measurements. We demonstrate the advantages of extracting the soft information from the syndrome in our improved decoders, not only in terms of comparison of thresholds and logical error rates for quasi-cyclic lifted-product QLDPC code families, but also for faster convergence of iterative decoders. In particular, the new BP decoder with noisy syndrome performs as good as the standard BP decoder under ideal syndrome.

## A recipe of training neural network-based LDPC decoders

- **Status**: ✅
- **Reason**: 신경망 기반 LDPC 디코더 훈련법(가중치 결정·파라미터 축소) — 이식 가능 디코더 알고리즘(C), 고전 바이너리 LDPC BP-unrolling, 포함
- **ID**: arxiv:2205.00481v2
- **Type**: preprint
- **Published**: 2022-05-01
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://arxiv.org/pdf/2205.00481v2
- **Abstract**: It is known belief propagation decoding variants of LDPC codes can be unrolled easily as neural networks after assigning differed weights to message passing edges flexibly. In this paper we focus on how to determine these weights, in the form of trainable paramters, within a framework of deep learning. Firstly, a new method is proposed to generate high-quality training data via exploiting an approximation to the targeted mixture density. Then the strong positive correlation between training loss and decoding metrics is fully exposed after tracing the training evolution curves. Lastly, for the purpose of facilitating training convergence and reducing decoding complexity, we highlight the necessity of slashing the number of trainable parameters while emphasizing the locations of these survived ones, which is justified in the extensive simulation.
