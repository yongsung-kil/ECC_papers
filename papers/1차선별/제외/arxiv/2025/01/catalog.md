# arXiv — 2025-01


## A topological theory for qLDPC: non-Clifford gates and magic state fountain on homological product codes with constant rate and beyond the $N^{1/3}$ distance barrier

- **Status**: ❌
- **Reason**: 양자 qLDPC 위상수학 이론, non-Clifford 게이트·magic state — 양자 전용 개념(CSS·스태빌라이저)에 의존, 고전 이식 불가
- **ID**: arxiv:2501.19375v3
- **Type**: preprint
- **Published**: 2025-01-31
- **Authors**: Guanyu Zhu
- **PDF**: https://arxiv.org/pdf/2501.19375v3
- **Abstract**: We develop a topological theory for fault-tolerant quantum computation in quantum low-density parity-check (qLDPC) codes. We show that there exist hidden simplicial or CW complex structures encoding the topological data for all qLDPC and CSS codes obtained from product construction by generalizing the Freedman-Hastings code-to-manifold mapping. This is achieved by building manifolds from the Tanner graphs of the skeleton classical or quantum codes, which further form a product manifold and an associated thickened product code defined on its triangulation. One can further deformation retract the manifold back to a CW complex which supports a non-topological code with minimal overhead suitable for near-term implementation. Both types of codes admit cohomology operations including cup product which can induce non-Clifford gates. When applying this mapping to a 3D hypergraph product code obtained from the product of 3 copies of good classical expander codes, we obtain non-Clifford logical CCZ gates via constant depth circuits on a code with constant stabilizer weight $w=O(1)$, constant rate $K=Θ(N)$, and polynomial distance $D=Ω(N^{1/3})$. When applied to logical CCZ on 3D homological product codes consisting of the product of a pair of good quantum and classical LDPC codes, we can further improve the distance to $D=Ω(\sqrt{N})$ exceeding the $N^{1/3}$ distance barrier implied by the Bravyi-König bound for conventional topological codes with the aid of non-Euclidean geometries. Our work suggests that it is feasible to apply native logical non-Clifford gates on qLDPC codes or directly inject high-fidelity magic states as resources ('magic state fountain') without the distillation process. For the homological product construction, the fountain can inject $Θ(\sqrt{N})$ magic states in parallel in a single round.

## Upper Bounds on the Minimum Distance of Structured LDPC Codes

- **Status**: ❌
- **Reason**: 구조적 바이너리 LDPC 최소거리 상한 개선 — 순수 이론 bound, 새 디코더/HW/구성으로 안 이어짐
- **ID**: arxiv:2501.19125v1
- **Type**: preprint
- **Published**: 2025-01-31
- **Authors**: François Arnault, Philippe Gaborit, Wouter Rozendaal +2
- **PDF**: https://arxiv.org/pdf/2501.19125v1
- **Abstract**: We investigate the minimum distance of structured binary Low-Density Parity-Check (LDPC) codes whose parity-check matrices are of the form $[\mathbf{C} \vert \mathbf{M}]$ where $\mathbf{C}$ is circulant and of column weight $2$, and $\mathbf{M}$ has fixed column weight $r \geq 3$ and row weight at least $1$. These codes are of interest because they are LDPC codes which come with a natural linear-time encoding algorithm. We show that the minimum distance of these codes is in $O(n^{\frac{r-2}{r-1} + ε})$, where $n$ is the code length and $ε> 0$ is arbitrarily small. This improves the previously known upper bound in $O(n^{\frac{r-1}{r}})$ on the minimum distance of such codes.

## Explicit Construction of Quantum Quasi-Cyclic Low-Density Parity-Check Codes with Column Weight 2 and Girth 12

- **Status**: ❌
- **Reason**: 양자 QC-LDPC 구성, 직교성 유지 전제 + 비이진 LDPC로 확장 — 양자 전용 개념(직교성) 의존, 비이진, 이중 제외
- **ID**: arxiv:2501.13444v2
- **Type**: preprint
- **Published**: 2025-01-23
- **Authors**: Daiki Komoto, Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2501.13444v2
- **Abstract**: This study proposes an explicit construction method for quantum quasi-cyclic low-density parity-check (QC-LDPC) codes with a girth of 12. The proposed method designs parity-check matrices that maximize the girth while maintaining an orthogonal structure suitable for quantum error correction. By utilizing algebraic techniques, short cycles are eliminated, which improves error correction performance. Additionally, this method is extended to non-binary LDPC codes and spatially-coupled LDPC codes, demonstrating that both the girth and orthogonality can be preserved. The results of this study enable the design of high-performance quantum error-correcting codes without the need for random search.

## Soft-Decision Decoding for LDPC Code-Based Quantitative Group Testing

- **Status**: ❌
- **Reason**: LDPC 기반 quantitative group testing용 BP 디코더 — group testing 응용 특이적, NAND ECC 채널코딩에 떼어낼 새 기법 없음
- **ID**: arxiv:2501.12167v1
- **Type**: preprint
- **Published**: 2025-01-21
- **Authors**: Marvin Xhemrishi, Johan Östman, Alexandre Graell i Amat
- **PDF**: https://arxiv.org/pdf/2501.12167v1
- **Abstract**: We consider the problem of identifying defective items in a population with non-adaptive quantitative group testing. For this scenario, Mashauri et al. recently proposed a low-density parity-check (LDPC) code-based quantitative group testing scheme with a hard-decision decoding approach (akin to peeling decoding). This scheme outperforms generalized LDPC code-based quantitative group testing schemes in terms of the misdetection rate. In this work, we propose a belief-propagation-based decoder for quantitative group testing with LDPC codes, where the messages being passed are purely soft. Through extensive simulations, we show that the proposed soft-information decoder outperforms the hard-decision decoder Mashauri et al.

## Faster-Than-Nyquist Equalization with Convolutional Neural Networks

- **Status**: ❌
- **Reason**: FTN ISI 등화·복조용 CNN, LDPC는 부수 코딩 베이스라인 — 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: arxiv:2501.11594v2
- **Type**: preprint
- **Published**: 2025-01-20
- **Authors**: Bruno De Filippo, Carla Amatetti, Alessandro Vanelli-Coralli
- **PDF**: https://arxiv.org/pdf/2501.11594v2
- **Abstract**: Faster-than-Nyquist (FTN) signaling aims at improving the spectral efficiency of wireless communication systems by exceeding the boundaries set by the Nyquist-Shannon sampling theorem. 50 years after its first introduction in the scientific literature, wireless communications have significantly changed, but spectral efficiency remains one of the key challenges. To adopt FTN signaling, inter-symbol interference (ISI) patterns need to be equalized at the receiver. Motivated by the pattern recognition capabilities of convolutional neural networks with skip connections, we propose such deep learning architecture for ISI equalization and symbol demodulation in FTN receivers. We investigate the performance of the proposed model considering quadrature phase shift keying modulation and low density parity check coding, and compare it to a set of benchmarks, including frequency-domain equalization, a quadratic-programming-based receiver, and an equalization scheme based on a deep neural network. We show that our receiver outperforms any benchmark, achieving error rates comparable to those in additive white Gaussian noise channel, and higher effective throughput, thanks to the increased spectral efficiency of FTN signaling. With a compression factor of 60% and code rate 3/4, the proposed model achieves a peak effective throughput of 2.5 Mbps at just 10dB of energy per bit over noise power spectral density ratio, with other receivers being limited by error floors due to the strong inter-symbol interference. To promote reproducibility in deep learning for wireless communications, our code is open source at the repository provided in the references.

## Few-shot Policy (de)composition in Conversational Question Answering

- **Status**: ❌
- **Reason**: LDPC=Logical Decomposition for Policy Compliance(LLM NLP), LDPC 부호와 무관 — 약어 충돌
- **ID**: arxiv:2501.11335v1
- **Type**: preprint
- **Published**: 2025-01-20
- **Authors**: Kyle Erwin, Guy Axelrod, Maria Chang +8
- **PDF**: https://arxiv.org/pdf/2501.11335v1
- **Abstract**: The task of policy compliance detection (PCD) is to determine if a scenario is in compliance with respect to a set of written policies. In a conversational setting, the results of PCD can indicate if clarifying questions must be asked to determine compliance status. Existing approaches usually claim to have reasoning capabilities that are latent or require a large amount of annotated data. In this work, we propose logical decomposition for policy compliance (LDPC): a neuro-symbolic framework to detect policy compliance using large language models (LLMs) in a few-shot setting. By selecting only a few exemplars alongside recently developed prompting techniques, we demonstrate that our approach soundly reasons about policy compliance conversations by extracting sub-questions to be answered, assigning truth values from contextual information, and explicitly producing a set of logic statements from the given policies. The formulation of explicit logic graphs can in turn help answer PCDrelated questions with increased transparency and explainability. We apply this approach to the popular PCD and conversational machine reading benchmark, ShARC, and show competitive performance with no task-specific finetuning. We also leverage the inherently interpretable architecture of LDPC to understand where errors occur, revealing ambiguities in the ShARC dataset and highlighting the challenges involved with reasoning for conversational question answering.

## Efficient Reconciliation of Continuous Variable Quantum Key Distribution with Multiplicatively Repeated Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(GF) LDPC + CV-QKD reconciliation — 비이진이라 즉시 제외, 이식할 바이너리 ECC 기법 없음
- **ID**: arxiv:2501.11009v2
- **Type**: preprint
- **Published**: 2025-01-19
- **Authors**: Jesus Martinez-Mateo, David Elkouss
- **PDF**: https://arxiv.org/pdf/2501.11009v2
- **Abstract**: Continuous variable quantum key distribution bears the promise of simple quantum key distribution directly compatible with commercial off the shelf equipment. However, for a long time its performance was hindered by the absence of good classical postprocessing capable of distilling secret-keys in the noisy regime. Advanced coding solutions in the past years have partially addressed this problem enabling record transmission distances of up to 165 km, and 206 km over ultra-low loss fiber. In this paper, we show that a very simple coding solution with a single code is sufficient to extract keys at all noise levels. This solution has performance competitive with prior results for all levels of noise, and we show that non-zero keys can be distilled up to a record distance of 192 km assuming the standard loss of a single-mode optical fiber, and 240 km over ultra-low loss fibers. Low-rate codes are constructed using multiplicatively repeated non-binary low-density parity-check codes over a finite field of characteristic two. This construction only makes use of a (2,k)-regular non-binary low-density parity-check code as mother code, such that code design is in fact not required, thus trivializing the code construction procedure. The construction is also inherently rate-adaptive thereby allowing to easily create codes of any rate. Rate-adaptive codes are of special interest for the efficient reconciliation of errors over time or arbitrary varying channels, as is the case with quantum key distribution. In short, these codes are highly efficient when reconciling errors over a very noisy communication channel, and perform well even for short block-length codes. Finally, the proposed solution is known to be easily amenable to hardware implementations, thus addressing also the requirements for practical reconciliation in continuous variable quantum key distribution.

## Decoding Quantum LDPC Codes using Collaborative Check Node Removal

- **Status**: ❌
- **Reason**: QLDPC 디코딩이 스태빌라이저 check node 제거·degeneracy·qubit separation 등 양자 전용 개념에 의존 — 고전 이식 불가
- **ID**: arxiv:2501.08036v3
- **Type**: preprint
- **Published**: 2025-01-14
- **Authors**: Mainak Bhattacharyya, Ankur Raina
- **PDF**: https://arxiv.org/pdf/2501.08036v3
- **Abstract**: Fault tolerance in quantum protocols requires contributions from error-correcting codes and their suitable decoders. Quantum Low-Density Parity Check (QLDPC) codes are one of the most explored quantum codes that have good coding rate and efficient decoders. Iterative message passing-based decoders, although fast, fail to produce suitable success rates due to the colossal degeneracy and short cycles intrinsic to these codes. In this work we present a strategy to improve the performance of the Belief Propagation (BP) decoding, specifically the min-sum algorithm. We propose a collaborative decoding framework that integrates message passing with stabilizer check node removals. We further introduce the concept of ``qubit separation" and show that the improved decoding performance is directly related to the generation of highly separated trapped data qubits. To guide a more selective removal of check nodes that constrain the separation of the trapped data qubits, we introduce information measurements (IMs) for the data qubits and their adjacent stabilizer checks. We evaluate the performance of the proposed collaborative decoder on Generalized Hypergraph Product (GHP) codes and demonstrate that appropriate decoder configurations mitigate trapping sets in min-sum decoding without significant overhead.

## Design and Analysis of a Concatenated Code for Intersymbol Interference Wiretap Channels

- **Status**: ❌
- **Reason**: ISI wiretap 보안용 LDPC+trellis 연접, LDPC는 secrecy 베이스라인 — 떼어낼 NAND ECC 기법 없음
- **ID**: arxiv:2501.07561v5
- **Type**: preprint
- **Published**: 2025-01-13
- **Authors**: Aria Nouri, Reza Asvadi, Jun Chen
- **PDF**: https://arxiv.org/pdf/2501.07561v5
- **Abstract**: We propose a two-stage concatenated coding scheme for reliable and secure communication over intersymbol interference wiretap channels. We first establish the secrecy capacity. Then, motivated by the theoretical codes that achieve the secrecy capacity, our scheme integrates low-density parity-check (LDPC) codes in the outer stage, forming a nested structure of wiretap codes, with trellis codes in the inner stage to improve achievable secure rates. The trellis code is specifically designed to transform the uniformly distributed codewords produced by the LDPC code stage into a Markov process, achieving tight lower bounds on the secrecy capacity. We further estimate the information leakage rate of the proposed scheme using an upper bound. To meet the weak secrecy criterion, we optimize degree distributions of the irregular LDPC codes at the outer stage, essentially driving the estimated upper bound on the information leakage rate to zero.

## Entanglement-Assisted Quantum Quasi-Cyclic LDPC Codes with Transversal Logical Operators

- **Status**: ❌
- **Reason**: Entanglement-assisted QC-QLDPC, quaternary(비이진) 디코더·transversal logical operator 등 양자 전용 — 제외
- **ID**: arxiv:2501.07363v2
- **Type**: preprint
- **Published**: 2025-01-13
- **Authors**: Pavan Kumar, Abhi Kumar Sharma, Shayan Srinivasa Garani
- **PDF**: https://arxiv.org/pdf/2501.07363v2
- **Abstract**: We derive two families of EA-QC quantum LDPC (EA-QC-QLDPC) codes by tiling permutation matrices of prime and composite orders. The unassisted portion of the Tanner graphs corresponding to these codes, constructed from two distinct classical QC-LDPC codes, exhibits girth greater then 4 an essential property for effective error correction. We analytically derive the exact code rate of the proposed constructions. Remarkably, one of these families requires only a single Bell pair to be shared between the quantum transmitter and receiver. Furthermore, two additional families of EA-QC-QLDPC codes are constructed based on a single classical code, whose Tanner graphs exhibit girths exceeding six, thereby further enhancing the error-correction capability. For one of these families, we explicitly determine the transversal logical operators an aspect that is typically non-trivial for random quasi-cyclic codes. The performance of the proposed codes is assessed under both random and burst error models under the depolarizing and Markovian noise actions. Employing a modified sum-product decoding algorithm over a quaternary alphabet, we demonstrate that correlated Pauli errors can be effectively addressed within the decoding framework. Simulation results reveal nearly an order of improvement in error-correction performance with the quaternary decoder compared to the binary decoder over both depolarizing and Markovian channels. Further, the proposed codes are compared with existing ones, demonstrating significant improvement.

## A graph-based approach to entanglement entropy of quantum error correcting codes

- **Status**: ❌
- **Reason**: CSS 양자코드 entanglement entropy 그래프 이론 — 디코더/HW/구성으로 안 이어지는 순수 이론
- **ID**: arxiv:2501.06407v3
- **Type**: preprint
- **Published**: 2025-01-11
- **Authors**: Wuxu Zhao, Menglong Fang, Daiqin Su
- **PDF**: https://arxiv.org/pdf/2501.06407v3
- **Abstract**: We develop a graph-based method to study the entanglement entropy of Calderbank-Shor-Steane quantum codes. This method offers a straightforward interpretation for the entanglement entropy of quantum error correcting codes through graph-theoretical concepts, shedding light on the origins of both the local and long-range entanglement. Furthermore, it inspires an efficient computational scheme for evaluating the entanglement entropy. We illustrate the method by calculating the von Neumann entropy of subsystems in toric codes and two types of quantum low-density-parity check codes, and by comparing the scaling behavior of the entanglement entropy with respect to the subsystem size. Our method provides a new perspective for understanding the entanglement structure in quantum many-body systems.

## Maximally Extendable Product Codes are Good Coboundary Expanders

- **Status**: ❌
- **Reason**: product/coboundary expansion 순수 이론 bound, good QLDPC·LTC 구성 — 디코더/HW로 안 이어짐
- **ID**: arxiv:2501.01411v2
- **Type**: preprint
- **Published**: 2025-01-02
- **Authors**: Gleb Kalachev, Pavel Panteleev
- **PDF**: https://arxiv.org/pdf/2501.01411v2
- **Abstract**: We investigate the coboundary expansion property of tensor product codes, known as product expansion, which plays an important role in recent constructions of good quantum LDPC codes and classical locally testable codes. Prior research has shown that this property is equivalent to agreement testability and robust testability for products of two codes with linear distance. However, for products of more than two codes, product expansion is a strictly stronger property. In this paper, we prove that a collection of an arbitrary number of random codes over a sufficiently large field has good product expansion. We believe that, in the case of four codes, the same ideas can be used to construct good quantum locally testable codes, in a way similar to the current constructions that use only products of two codes.
