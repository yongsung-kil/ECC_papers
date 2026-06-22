# arXiv — 2023-10


## Simple Constructions of Unique Neighbor Expanders from Error-correcting Codes

- **Status**: ❌
- **Reason**: expander 그래프로부터 unique neighbor expander 구성하는 순수 그래프 이론, 디코더/HW/실용 LDPC 코드 설계로 이어지지 않음
- **ID**: arxiv:2310.19149v2
- **Type**: preprint
- **Published**: 2023-10-29
- **Authors**: Swastik Kopparty, Noga Ron-Zewi, Shubhangi Saraf
- **PDF**: https://arxiv.org/pdf/2310.19149v2
- **Abstract**: In this note, we give very simple constructions of unique neighbor expander graphs starting from spectral or combinatorial expander graphs of mild expansion. These constructions and their analysis are simple variants of the constructions of LDPC error-correcting codes from expanders, given by Sipser-Spielman [SS96] (and Tanner [Tan81]), and their analysis. We also show how to obtain expanders with many unique neighbors using similar ideas.   There were many exciting results on this topic recently, starting with Asherov-Dinur [AD23] and Hsieh-McKenzie-Mohanty-Paredes [HMMP23], who gave a similar construction of unique neighbor expander graphs, but using more sophisticated ingredients (such as almost-Ramanujan graphs) and a more involved analysis. Subsequent beautiful works of Cohen-Roth-TaShma [CRT23] and Golowich [Gol23] gave even stronger objects (lossless expanders), but also using sophisticated ingredients.   The main contribution of this work is that we get much more elementary constructions of unique neighbor expanders and with a simpler analysis.

## Low-Complexity and Information-Theoretic Optimal Memory AMP for Coded Generalized MIMO

- **Status**: ❌
- **Reason**: GMIMO 수신기용 MAMP — LDPC는 베이스라인일 뿐, 떼어낼 LDPC 디코더/코드 설계 기법 없음 (무선 응용 특이)
- **ID**: arxiv:2310.17943v1
- **Type**: preprint
- **Published**: 2023-10-27
- **Authors**: Yufei Chen, Lei Liu, Yuhao Chi +2
- **PDF**: https://arxiv.org/pdf/2310.17943v1
- **Abstract**: This paper considers a generalized multiple-input multiple-output (GMIMO) with practical assumptions, such as massive antennas, practical channel coding, arbitrary input distributions, and general right-unitarily-invariant channel matrices (covering Rayleigh fading, certain ill-conditioned and correlated channel matrices). Orthogonal/vector approximate message passing (OAMP/VAMP) has been proved to be information-theoretically optimal in GMIMO, but it is limited to high complexity. Meanwhile, low-complexity memory approximate message passing (MAMP) was shown to be Bayes optimal in GMIMO, but channel coding was ignored. Therefore, how to design a low-complexity and information-theoretic optimal receiver for GMIMO is still an open issue. In this paper, we propose an information-theoretic optimal MAMP receiver for coded GMIMO, whose achievable rate analysis and optimal coding principle are provided to demonstrate its information-theoretic optimality. Specifically, state evolution (SE) for MAMP is intricately multi-dimensional because of the nature of local memory detection. To this end, a fixed-point consistency lemma is proposed to derive the simplified variational SE (VSE) for MAMP, based on which the achievable rate of MAMP is calculated, and the optimal coding principle is derived to maximize the achievable rate. Subsequently, we prove the information-theoretic optimality of MAMP. Numerical results show that the finite-length performances of MAMP with optimized LDPC codes are about 1.0 - 2.7 dB away from the associated constrained capacities. It is worth noting that MAMP can achieve the same performance as OAMP/VAMP with 0.4% of the time consumption for large-scale systems.

## Non-Clifford and parallelizable fault-tolerant logical gates on constant and almost-constant rate homological quantum LDPC codes via higher symmetries

- **Status**: ❌
- **Reason**: 3-manifold 위상학적 homological 양자 LDPC + fault-tolerant 논리 게이트 — 순수 양자, 고전 이식 불가
- **ID**: arxiv:2310.16982v3
- **Type**: preprint
- **Published**: 2023-10-25
- **Authors**: Guanyu Zhu, Shehryar Sikander, Elia Portnoy +2
- **PDF**: https://arxiv.org/pdf/2310.16982v3
- **Abstract**: We study parallel fault-tolerant quantum computing for families of homological quantum low-density parity-check (LDPC) codes defined on 3-manifolds with constant or almost-constant encoding rate. We derive generic formula for a transversal $T$ gate of color codes on general 3-manifolds, which acts as collective non-Clifford logical CCZ gates on any triplet of logical qubits with their logical-$X$ membranes having a $\mathbb{Z}_2$ triple intersection at a single point. The triple intersection number is a topological invariant, which also arises in the path integral of the emergent higher symmetry operator in a topological quantum field theory: the $\mathbb{Z}_2^3$ gauge theory. Moreover, the transversal $S$ gate of the color code corresponds to a higher-form symmetry supported on a codimension-1 submanifold, giving rise to exponentially many addressable and parallelizable logical CZ gates. A construction of constant-depth circuits of the above logical gates via cup product cohomology operation is also presented for three copies of identical toric codes on arbitrary 3-manifolds. We have developed a generic formalism to compute the triple intersection invariants for 3-manifolds. We further develop three types of LDPC codes supporting such logical gates: (1) A quasi-hyperbolic code from the product of 2D hyperbolic surface and a circle, with almost-constant rate $k/n=O(1/\log(n))$ and $O(\log(n))$ distance; (2) A homological fibre bundle code with $O(1/\log^{\frac{1}{2}}(n))$ rate and $O(\log^{\frac{1}{2}}(n))$ distance; (3) A specific family of 3D hyperbolic codes: the Torelli mapping torus code, constructed from mapping tori of a pseudo-Anosov element in the Torelli subgroup, which has constant rate while the distance scaling is currently unknown. We then show a generic constant-overhead scheme for applying a parallelizable universal gate set with the aid of logical-$X$ measurements.

## The Physics of (good) LDPC Codes I. Gauging and dualities

- **Status**: ❌
- **Reason**: good LDPC를 게이지 이론/물성 관점으로 해석하는 물리 이론 — 디코더/HW/실용 코드 구성으로 안 이어짐
- **ID**: arxiv:2310.16032v1
- **Type**: preprint
- **Published**: 2023-10-24
- **Authors**: Tibor Rakovszky, Vedika Khemani
- **PDF**: https://arxiv.org/pdf/2310.16032v1
- **Abstract**: Low-depth parity check (LDPC) codes are a paradigm of error correction that allow for spatially non-local interactions between (qu)bits, while still enforcing that each (qu)bit interacts only with finitely many others. On expander graphs, they can give rise to ``good codes'' that combine a finite encoding rate with an optimal scaling of the code distance, which governs the code's robustness against noise. Such codes have garnered much recent attention due to two breakthrough developments: the construction of good quantum LDPC codes and good locally testable classical LDPC codes, using similar methods. Here we explore these developments from a physics lens, establishing connections between LDPC codes and ordered phases of matter defined for systems with non-local interactions and on non-Euclidean geometries. We generalize the physical notions of Kramers-Wannier (KW) dualities and gauge theories to this context, using the notion of chain complexes as an organizing principle. We discuss gauge theories based on generic classical LDPC codes and make a distinction between two classes, based on whether their excitations are point-like or extended. For the former, we describe KW dualities, analogous to the 1D Ising model and describe the role played by ``boundary conditions''. For the latter we generalize Wegner's duality to obtain generic quantum LDPC codes within the deconfined phase of a Z_2 gauge theory. We show that all known examples of good quantum LDPC codes are obtained by gauging locally testable classical codes. We also construct cluster Hamiltonians from arbitrary classical codes, related to the Higgs phase of the gauge theory, and formulate generalizations of the Kennedy-Tasaki duality transformation. We use the chain complex language to discuss edge modes and non-local order parameters for these models, initiating the study of SPT phases in non-Euclidean geometries.

## Check-Agnosia based Post-Processor for Message-Passing Decoding of Quantum LDPC Codes

- **Status**: ❌
- **Reason**: out 정정(감사): stabilizer-inactivation 기반 후처리로 양자 전용 개념(스태빌라이저)에 의존 → 기준상 제외. (원판정 in, Phase2 검수에서 정정)
- **ID**: arxiv:2310.15000v3
- **Type**: preprint
- **Published**: 2023-10-23
- **Authors**: Julien du Crest, Francisco Garcia-Herrero, Mehdi Mhalla +2
- **PDF**: https://arxiv.org/pdf/2310.15000v3
- **Abstract**: The inherent degeneracy of quantum low-density parity-check codes poses a challenge to their decoding, as it significantly degrades the error-correction performance of classical message-passing decoders. To improve their performance, a post-processing algorithm is usually employed. To narrow the gap between algorithmic solutions and hardware limitations, we introduce a new post-processing algorithm with a hardware-friendly orientation, providing error correction performance competitive to the state-of-the-art techniques. The proposed post-processing, referred to as check-agnosia, is inspired by stabilizer-inactivation, while considerably reducing the required hardware resources, and providing enough flexibility to allow different message-passing schedules and hardware architectures. We carry out a detailed analysis for a set of Pareto architectures with different tradeoffs between latency and power consumption, derived from the results of implemented designs on an FPGA board. We show that latency values close to one microsecond can be obtained on the FPGA board, and provide evidence that much lower latency values can be obtained for ASIC implementations. In the process, we also demonstrate the practical implications of the recently introduced t-covering layers and random-order layered scheduling.

## 4-Cycle Free Spatially Coupled LDPC Codes with an Explicit Construction

- **Status**: ✅
- **Reason**: 4-cycle free SC-LDPC 명시적 구성법 (good sequences) — 바이너리 SC-LDPC 코드 설계·girth 제거 신기여(E)
- **ID**: arxiv:2310.12657v1
- **Type**: preprint
- **Published**: 2023-10-19
- **Authors**: Zeinab Roostaie, Mohammad Gholami, Farzad Parvaresh
- **PDF**: https://arxiv.org/pdf/2310.12657v1
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are a class of capacity approaching LDPC codes with low message recovery latency when a sliding window decoding is used. In this paper, we first present a new method for the construction of a class of SC-LDPC codes by the incidence matrices of a given non-negative integer matrix $E$, and then the relationship of 4-cycles between matrix $E$ and the corresponding SC-LDPC code are investigated. Finally, by defining a new class of integer finite sequences, called {\it good sequences}, for the first time, we give an explicit method for the construction of a class of 4-cycle free SC-LDPC codes that can achieve (in most cases) the minimum coupling width.

## An Efficient Algorithm for Counting Cycles in QC and APM LDPC Codes

- **Status**: ✅
- **Reason**: QC/APM-LDPC Tanner 그래프의 임의 길이 사이클 카운팅 신규 알고리즘 — 바이너리 코드 설계·girth/사이클 분석 이식 가능(E)
- **ID**: arxiv:2310.12556v1
- **Type**: preprint
- **Published**: 2023-10-19
- **Authors**: Mohammad Gholami, Zahra Gholami
- **PDF**: https://arxiv.org/pdf/2310.12556v1
- **Abstract**: In this paper, a new method is given for counting cycles in the Tanner graph of a (Type-I) quasi-cyclic (QC) low-density parity-check (LDPC) code which the complexity mainly is dependent on the base matrix, independent from the CPM-size of the constructed code. Interestingly, for large CPM-sizes, in comparison of the existing methods, this algorithm is the first approach which efficiently counts the cycles in the Tanner graphs of QC-LDPC codes. In fact, the algorithm recursively counts the cycles in the parity-check matrix column-by-column by finding all non-isomorph tailless backtrackless closed (TBC) walks in the base graph and enumerating theoretically their corresponding cycles in the same equivalent class. Moreover, this approach can be modified in few steps to find the cycle distributions of a class of LDPC codes based on Affine permutation matrices (APM-LDPC codes). Interestingly, unlike the existing methods which count the cycles up to $2g-2$, where $g$ is the girth, the proposed algorithm can be used to enumerate the cycles of arbitrary length in the Tanner graph. Moreover, the proposed cycle searching algorithm improves upon various previously known methods, in terms of computational complexity and memory requirements.

## Viderman's algorithm for quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC(hypergraph product) 전용 디코더(Viderman 일반화) — erasure 변환이 양자 스태빌라이저 구조에 의존, 고전 바이너리 NAND로 이식 어려움
- **ID**: arxiv:2310.07868v1
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Anirudh Krishna, Inbal Livni Navon, Mary Wootters
- **PDF**: https://arxiv.org/pdf/2310.07868v1
- **Abstract**: Quantum low-density parity-check (LDPC) codes, a class of quantum error correcting codes, are considered a blueprint for scalable quantum circuits. To use these codes, one needs efficient decoding algorithms. In the classical setting, there are multiple efficient decoding algorithms available, including Viderman's algorithm (Viderman, TOCT 2013). Viderman's algorithm for classical LDPC codes essentially reduces the error-correction problem to that of erasure-correction, by identifying a small envelope $L$ that is guaranteed to contain the error set.   Our main result is a generalization of Viderman's algorithm to quantum LDPC codes, namely hypergraph product codes (Tillich, Zémor, IEEE T-IT, 2013). This is the first erasure-conversion algorithm that can correct up to $Ω(D)$ errors for constant-rate quantum LDPC codes, where $D$ is the distance of the code. In that sense, it is also fundamentally different from existing decoding algorithms, in particular from the small-set-flip algorithm (Leverrier, Tillich, Zémor, FOCS, 2015). Moreover, in some parameter regimes, our decoding algorithm improves on the decoding radius of existing algorithms. We note that we do not yet have linear-time erasure-decoding algorithms for quantum LDPC codes, and thus the final running time of the whole decoding algorithm is not linear; however, we view our linear-time envelope-finding algorithm as an important first step.

## Symmetry-enforced many-body separability transitions

- **Status**: ❌
- **Reason**: 양자 다체계 혼합상태 분리성 전이 물리 연구 — qLDPC를 NLTS 예시로만 언급, 디코더/코드설계 기여 없음
- **ID**: arxiv:2310.07286v2
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Yu-Hsueh Chen, Tarun Grover
- **PDF**: https://arxiv.org/pdf/2310.07286v2
- **Abstract**: We study quantum many-body mixed states with a symmetry from the perspective of separability, i.e., whether a mixed state can be expressed as an ensemble of short-range entangled (SRE) symmetric pure states. We provide evidence for 'symmetry-enforced separability transitions' in a variety of states, where in one regime the mixed state is expressible as a convex sum of symmetric SRE pure states, while in the other regime, such a representation is not feasible. We first discuss Gibbs state of Hamiltonians that exhibit spontaneous breaking of a discrete symmetry, and argue that the associated thermal phase transition can be thought of as a symmetry-enforced separability transition. Next, we study cluster states in various dimensions subjected to local decoherence, and identify several distinct mixed-state phases and associated separability phase transitions, which also provides an alternate perspective on recently discussed 'average SPT order'. We also study decohered p+ip superconductors, and find that if the decoherence breaks the fermion parity explicitly, then the resulting mixed state can be expressed as a convex sum of non-chiral states, while a fermion-parity preserving decoherence results in a phase transition at a non-zero threshold that corresponds to spontaneous breaking of fermion parity. Finally, we briefly discuss systems that satisfy NLTS (no low-energy trivial state) property, such as the recently discovered good LDPC codes, and argue that the Gibbs state of such systems exhibits a temperature-tuned separability transition.

## Boosting Learning for LDPC Codes to Improve the Error-Floor Performance

- **Status**: ✅
- **Reason**: C/E: neural min-sum 디코더 학습기법으로 표준 LDPC error-floor 제거, 추가 HW 없이 기존 디코더에 통합 가능 — NAND ECC 직접 이식 가능
- **ID**: arxiv:2310.07194v2
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Hee-Youl Kwak, Dae-Young Yun, Yongjune Kim +2
- **PDF**: https://arxiv.org/pdf/2310.07194v2
- **Abstract**: Low-density parity-check (LDPC) codes have been successfully commercialized in communication systems due to their strong error correction capabilities and simple decoding process. However, the error-floor phenomenon of LDPC codes, in which the error rate stops decreasing rapidly at a certain level, presents challenges for achieving extremely low error rates and deploying LDPC codes in scenarios demanding ultra-high reliability. In this work, we propose training methods for neural min-sum (NMS) decoders to eliminate the error-floor effect. First, by leveraging the boosting learning technique of ensemble networks, we divide the decoding network into two neural decoders and train the post decoder to be specialized for uncorrected words that the first decoder fails to correct. Secondly, to address the vanishing gradient issue in training, we introduce a block-wise training schedule that locally trains a block of weights while retraining the preceding block. Lastly, we show that assigning different weights to unsatisfied check nodes effectively lowers the error-floor with a minimal number of weights. By applying these training methods to standard LDPC codes, we achieve the best error-floor performance compared to other decoding methods. The proposed NMS decoder, optimized solely through novel training methods without additional modules, can be integrated into existing LDPC decoders without incurring extra hardware costs. The source code is available at https://github.com/ghy1228/LDPC_Error_Floor .

## The impact when neural min-sum variant meets ordered statistics decoding of LDPC codes

- **Status**: ✅
- **Reason**: C: neural min-sum 변형 + OSD 하이브리드 디코더, 저복잡도/고처리율 설계 — 바이너리 LDPC 디코더 기법으로 이식 가능
- **ID**: arxiv:2310.07129v2
- **Type**: preprint
- **Published**: 2023-10-11
- **Authors**: Guangwen Li, Xiao Yu
- **PDF**: https://arxiv.org/pdf/2310.07129v2
- **Abstract**: This paper introduces three key initiatives in the pursuit of a hybrid decoding framework characterized by superior decoding performance, high throughput, low complexity, and independence from channel noise variance.   Firstly, adopting a graphical neural network perspective, we propose a design methodology for a family of neural min-sum variants. Our exploration delves into the frame error rates associated with different decoding variants and the consequential impact of decoding failures on subsequent ordered statistics decoding. Notably, these neural min-sum variants exhibit generally indistinguishable performance, hence the simplest member is chosen as the constituent of the hybrid decoding.   Secondly, to address computational complexities arising from exhaustive searches for authentic error patterns in cases of decoding failure, two alternatives for ordered statistics decoding implementation are proposed. The first approach involves uniformly grouping test error patterns, while the second scheme dynamically generates qualified searching test error patterns with varied sizes for each group. In both methods, group priorities are determined empirically.   Thirdly, iteration diversity is highlighted in the case of LDPC codes requiring high maximum iterations of decoding. This is achieved by segmenting the long iterative decoding trajectory of a decoding failure into shorter segments, which are then independently fed to small models to enhance the chances of acquiring the authentic error pattern.   These ideas are substantiated through extensive simulation results covering the codes with block lengths ranging from one hundred to several hundreds.

## An Optimal Unequal Error Protection LDPC Coded Recording System

- **Status**: ✅
- **Reason**: B/E: 기록(recording) 시스템용 비정칙 LDPC UEP 코드 설계, density evolution/EXIT 최적화 — 스토리지 ECC 코드설계 기법 이식 가능
- **ID**: arxiv:2310.04923v2
- **Type**: preprint
- **Published**: 2023-10-07
- **Authors**: Hong-fu Chou
- **PDF**: https://arxiv.org/pdf/2310.04923v2
- **Abstract**: For efficient modulation and error control coding, the deliberate flipping approach imposes the run-length-limited(RLL) constraint by bit error before recording. From the read side, a high coding rate limits the correcting capability of RLL bit error. In this paper, we study the low-density parity-check (LDPC) coding for RLL constrained recording system based on the Unequal Error Protection (UEP) coding scheme design. The UEP capability of irregular LDPC codes is used for recovering flipped bits. We provide an allocation technique to limit the occurrence of flipped bits on the bit with robust correction capability. In addition, we consider the signal labeling design to decrease the number of nearest neighbors to enhance the robust bit. We also apply the density evolution technique to the proposed system for evaluating the code performances. In addition, we utilize the EXIT characteristic to reveal the decoding behavior of the recommended code distribution. Finally, the optimization approach for the best distribution is proven by differential evolution for the proposed system.
