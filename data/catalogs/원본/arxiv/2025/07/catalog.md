# arXiv — 2025-07


## Placing and routing quantum LDPC codes in multilayer superconducting hardware

- **Status**: ❌
- **Reason**: 양자 qLDPC 코드의 초전도 HW 배치/라우팅 — 양자 전용 개념(스태빌라이저·논로컬 연결)에 의존, 고전 바이너리 LDPC로 이식 불가, 양자 원칙 제외
- **ID**: arxiv:2507.23011v2
- **Type**: preprint
- **Published**: 2025-07-30
- **Authors**: Melvin Mathews, Lukas Pahl, David Pahl +4
- **PDF**: https://arxiv.org/pdf/2507.23011v2
- **Abstract**: Quantum error-correcting codes with asymptotically lower overheads than the surface code require nonlocal connectivity. Leveraging multilayer routing and long-range coupling capabilities in superconducting qubit hardware, we develop Hardware-Aware Layout, HAL: a robust, runtime-efficient heuristic algorithm that automates and optimizes the placement and routing of arbitrary codes. Using HAL, we generate around 150 explicit layouts of quantum low-density parity-check (qLDPC) codes with topological structure -- such as the bivariate bicycle codes and the open-boundary tile codes -- and find that removing the periodic boundaries significantly lowers the hardware complexity with only a moderate reduction of logical efficiency. We also lay out highly nonlocal qLDPC code families -- quantum radial and Tanner codes -- that achieve competitive tradeoffs between hardware complexity and logical efficiency. Based on our findings, we anticipate many novel qLDPC codes to be realizable on near-term superconducting qubit hardware and inform future directions for the co-design of quantum devices and fault-tolerant architectures.

## Adaptive Learned Belief Propagation for Decoding Error-Correcting Codes

- **Status**: ✅
- **Reason**: 적응형 weighted BP/신경망 가중치 결정 디코더, QC-LDPC에 적용·기존 NMS 대비 개선 — 이식 가능 디코더 알고리즘(C)
- **ID**: arxiv:2507.19941v1
- **Type**: preprint
- **Published**: 2025-07-26
- **Authors**: Alireza Tasdighi, Mansoor Yousefi
- **PDF**: https://arxiv.org/pdf/2507.19941v1
- **Abstract**: Weighted belief propagation (WBP) for the decoding of linear block codes is considered. In WBP, the Tanner graph of the code is unrolled with respect to the iterations of the belief propagation decoder. Then, weights are assigned to the edges of the resulting recurrent network and optimized offline using a training dataset. The main contribution of this paper is an adaptive WBP where the weights of the decoder are determined for each received word. Two variants of this decoder are investigated. In the parallel WBP decoders, the weights take values in a discrete set. A number of WBP decoders are run in parallel to search for the best sequence of weights in real time. In the two-stage decoder, a small neural network is used to dynamically determine the weights of the WBP decoder for each received word. The proposed adaptive decoders demonstrate significant improvements over the static counterparts in two applications. In the first application, Bose-Chaudhuri-Hocquenghem, polar and quasi-cyclic low-density parity-check (QC-LDPC) codes are used over an additive white Gaussian noise channel. The results indicate that the adaptive WBP achieves bit error rates (BERs) up to an order of magnitude less than the BERs of the static WBP at about the same decoding complexity, depending on the code, its rate, and the signal-to-noise ratio. The second application is a concatenated code designed for a long-haul nonlinear optical fiber channel where the inner code is a QC-LDPC code and the outer code is a spatially coupled LDPC code. In this case, the inner code is decoded using an adaptive WBP, while the outer code is decoded using the sliding window decoder and static belief propagation. The results show that the adaptive WBP provides a coding gain of 0.8 dB compared to the neural normalized min-sum decoder, with about the same computational complexity and decoding latency.

## Polar Coding and Linear Decoding

- **Status**: ❌
- **Reason**: Polar 코드 선형 디코딩이 주제, LDPC는 비교 언급뿐 — 떼어낼 LDPC ECC 기법 없음
- **ID**: arxiv:2507.19695v1
- **Type**: preprint
- **Published**: 2025-07-25
- **Authors**: Geraldo A. Barbosa
- **PDF**: https://arxiv.org/pdf/2507.19695v1
- **Abstract**: Polar encoding, described by Arikan in IEEE Transactions on Information Theory, Vol. 55, No. 7, July 2009, was a milestone for telecommunications. A Polar code distributes information among high and low-capacity channels, showing the possibility of achieving perfect channel capacity. The high-capacity channels allow almost noiseless transmission of data. When these channels are not high noise, reliability is achieved in the signal transmission. It starts to compete against codes such a Low-Density Parity-Check (LDPC) codes. Polar code can be also considered error correcting, based on the redundancy inherent in its structure. This feature makes polar encoding also applicable to digital quantum-resistant cryptography protocols. This work explores linear decoding at a first or single trial in the case of small losses or small number of bit-flipping, and repeated transmission for medium level losses. This is distinct from Arikans successive probabilistic decoding by application of probabilistic rules. Linear decoding is done directly from solving the linear equations connecting the codewords x and the received signals y after transmission via noisy channels. Numerical examples will be shown. Along with this work, programming in Mathematica language was used. Codes are available for copy-and-paste for Mathematica users to immediately try the described formalism.

## Directional Codes: a new family of quantum LDPC codes on hexagonal- and square-grid connectivity hardware

- **Status**: ❌
- **Reason**: 양자 qLDPC 신규 코드족(Directional Codes), 스태빌라이저 측정·iSWAP 등 양자 전용 개념 의존 — 양자 원칙 제외
- **ID**: arxiv:2507.19430v2
- **Type**: preprint
- **Published**: 2025-07-25
- **Authors**: György P. Gehér, David Byfield, Archibald Ruban
- **PDF**: https://arxiv.org/pdf/2507.19430v2
- **Abstract**: Utility-scale quantum computing requires quantum error correction (QEC) to protect quantum information against noise. Currently, superconducting hardware is a promising candidate for achieving fault tolerance due to its fast gate times and feasible scalability. However, it is often restricted to two-dimensional nearest-neighbour connectivity, which is thought to be incapable of accommodating high-rate quantum low-density parity-check (qLDPC) codes that promise to greatly reduce the number of physical qubits needed to encode logical qubits. In this paper we construct a new family of qLDPC codes, which we call ``Directional Codes'', that outperforms the rotated planar code (RPC) while naturally meeting the connectivity requirements of the widely adopted square-grid, and some even the sparser hexagonal-grid. The key idea is to utilise the iSWAP gate -- a natural native gate for superconducting qubits -- to construct circuits that measure the stabilisers of these qLDPC codes without the need for any long-range connections or an increased degree of connectivity. We numerically evaluate the performance of directional codes, encoding four, six and twelve logical qubits, using a common superconducting-inspired circuit-level Pauli noise model. We also compare them to the RPC and to the bivariate bicycle (BB) codes, currently the two most popular quantum LDPC code families. As a concrete example, directional codes outperform the RPC by achieving approximately the same logical error probability at physical error rate $p=10^{-3}$ using only $18.75-45\%$ of the physical qubits at distance up to $10$. Our discovery represents a breakthrough in QEC code design that suggests complex long-range, high-connectivity hardware may not be necessary for low-overhead fault-tolerant quantum computation.

## Action-List Reinforcement Learning Syndrome Decoding for Binary Linear Block Codes

- **Status**: ✅
- **Reason**: RL 기반 비트플립 신드롬 디코딩, 바이너리 LDPC over BSC 실험 — 이식 가능 신규 디코더 알고리즘(C)
- **ID**: arxiv:2507.17893v2
- **Type**: preprint
- **Published**: 2025-07-23
- **Authors**: Milad Taghipour, Bane Vasic
- **PDF**: https://arxiv.org/pdf/2507.17893v2
- **Abstract**: This paper explores the application of reinforcement learning techniques to enhance the performance of decoding of linear block codes based on flipping bits and finding optimal decisions. We describe the methodology for mapping the iterative decoding process into Markov Decision Processes (MDPs) and propose different methods to reduce the number of states in the MDP. A truncated MDP is proposed to reduce the number of states in the MDP by learning a Hamming ball with a specified radius around codewords. We then propose a general scheme for reinforcement learning based decoders applicable to any class of codes to improve the performance of decoders. We call this scheme an action-list decoding. We design an action-list decoder based on the Deep-Q network values that substantially enhance performance. We also get benefit of automorphism group of code to further improve the code performance. Additionally, we propose a feedback-based method to exploit and enhance the performance of existing high-performing decoders by applying reinforcement learning algorithms after the existing decoders. These approaches effectively reduces the complexity of the reinforcement learning block. Finally, we present experimental results for the Low-Density Parity Check (LDPC) codes over the Binary Symmetric Channel (BSC) to demonstrate the efficiency of the proposed methods.

## CSS-$T$ codes over Binary Extension Fields and their Physical Foundations

- **Status**: ❌
- **Reason**: 양자 CSS-T 코드, 비이진 확장체 GF(q) 기반 LDPC — 비이진+양자 모두 제외 대상
- **ID**: arxiv:2507.17611v1
- **Type**: preprint
- **Published**: 2025-07-23
- **Authors**: Jasper J. Postema, F. Conca, A. Ravagnani
- **PDF**: https://arxiv.org/pdf/2507.17611v1
- **Abstract**: We investigate the class of CSS-$T$ codes, a family of quantum error-correcting codes that allows for a transversal $T$-gate. We extend the definition of a pair of linear codes $(C_1,C_2)$, $C_i\subseteq\mathbb{F}_q^n$, forming a $q$-ary CSS-$T$ code over binary extension fields, and demonstrate the existence of asymptotically good sequences of LDPC CSS-$T$ codes over any such field.

## Efficient and Robust Semantic Image Communication via Stable Cascade

- **Status**: ❌
- **Reason**: 디퓨전 기반 시맨틱 이미지 통신, LDPC는 JPEG2000+LDPC 베이스라인 비교뿐 — 시맨틱 통신, 떼어낼 ECC 기법 없음
- **ID**: arxiv:2507.17416v1
- **Type**: preprint
- **Published**: 2025-07-23
- **Authors**: Bilal Khalid, Pedro Freire, Sergei K. Turitsyn +1
- **PDF**: https://arxiv.org/pdf/2507.17416v1
- **Abstract**: Diffusion Model (DM) based Semantic Image Communication (SIC) systems face significant challenges, such as slow inference speed and generation randomness, that limit their reliability and practicality. To overcome these issues, we propose a novel SIC framework inspired by Stable Cascade, where extremely compact latent image embeddings are used as conditioning to the diffusion process. Our approach drastically reduces the data transmission overhead, compressing the transmitted embedding to just 0.29% of the original image size. It outperforms three benchmark approaches - the diffusion SIC model conditioned on segmentation maps (GESCO), the recent Stable Diffusion (SD)-based SIC framework (Img2Img-SC), and the conventional JPEG2000 + LDPC coding - by achieving superior reconstruction quality under noisy channel conditions, as validated across multiple metrics. Notably, it also delivers significant computational efficiency, enabling over 3x faster reconstruction for 512 x 512 images and more than 16x faster for 1024 x 1024 images as compared to the approach adopted in Img2Img-SC.

## Hourglass Sorting: A novel parallel sorting algorithm and its implementation

- **Status**: ✅
- **Reason**: FPGA 병렬 정렬기를 (양자)LDPC 디코더 맥락서 구현, 클럭저하 없는 n+log n 정렬 HW — min-sum류 정렬에 이식 가능 HW 아키텍처(D), 애매하나 살림
- **ID**: arxiv:2507.16326v1
- **Type**: preprint
- **Published**: 2025-07-22
- **Authors**: Daniel Bascones, Borja Morcillo
- **PDF**: https://arxiv.org/pdf/2507.16326v1
- **Abstract**: Sorting is one of the fundamental problems in computer science. Playing a role in many processes, it has a lower complexity bound imposed by $\mathcal{O}(n\log{n})$ when executing on a sequential machine. This limit can be brought down to sub-linear times thanks to parallelization techniques that increase the number of comparisons done in parallel. This, however, increases the cost of implementation, which limits the application of such techniques. Moreover, as the size of the arrays increases, a bottleneck arises in moving the vast quantities of data required at the input, and generated at the output of such sorter. This might impose time requirements much stricter than those of the sorting itself. In this paper, a novel parallel sorter is proposed for the specific case where the input is parallel, but the output is serial. The design is then implemented and verified on an FPGA within the context of a quantum LDPC decoder. A latency of $\log{n}$ is achieved for the output of the first element, after which the rest stream out for a total sorting time of $n+\log{n}$. Contrary to other parallel sorting methods, clock speed does not degrade with $n$, and resources scale linearly with input size.

## Transversal non-Clifford gates on qLDPC codes breaking the $\sqrt{N}$ distance barrier and quantum-inspired geometry with $\mathbb{Z}_2$ systolic freedom

- **Status**: ❌
- **Reason**: 양자 qLDPC 코드 거리 한계·횡단 게이트, 호몰로지 곱·systolic freedom 등 순수 양자/위상수학 이론 — 양자 원칙 제외
- **ID**: arxiv:2507.15056v1
- **Type**: preprint
- **Published**: 2025-07-20
- **Authors**: Guanyu Zhu
- **PDF**: https://arxiv.org/pdf/2507.15056v1
- **Abstract**: Historically, a $\sqrt{N}log^{1/2}(N)$ distance barrier for quantum low-density parity-check (LDPC) codes with $N$ qubits persisted for nearly two decades, until the recent discovery of the fibre-bundle code. An open question is whether such a distance barrier can be broken while preserving the ability to perform transversal non-Clifford gates. In this direction, another long-standing distance barrier of $N^{1/3}$ for LDPC stabilizer codes -- present since the discovery of the 3D color code -- was only recently overcome by a construction achieving an $Ω(\sqrt{N})$ distance (arXiv:2501.19375). The present work further breaks the $\sqrt{N}$ distance barrier by taking a homological product of three good qLDPC codes, combined with the Freedman-Hastings code-to-manifold mapping and the triple cup product to implement transversal CCZ gates. The resulting code achieves an $Ω(N^{2/3})$ distance (a linear $X$-distance of $Θ(N)$) and a dimension of $Θ(N^{2/3})$, which enables fault-tolerant preparation of $Θ(N^{1/3})$ independent logical CCZ magic states in a single shot, without distillation (`magic state fountain'). This new quantum code also inspires the discovery of a family of exotic $3q$-dimensional manifolds $\mathcal{M}$, which exhibit both a power-law $\mathbb{Z}_2$-($q$, $2q$)-systolic freedom and $Θ(vol(\mathcal{M}))$ triple intersection points of $2q$-dimensional submanifolds.

## Growing Sparse Quantum Codes from a Seed

- **Status**: ❌
- **Reason**: 양자 LDPC/서브시스템 코드를 반복코드 conjoining으로 구성, CSS 코드 생성 — 양자 전용 구성, 고전 바이너리 LDPC 이식성 없음
- **ID**: arxiv:2507.13496v1
- **Type**: preprint
- **Published**: 2025-07-17
- **Authors**: ChunJun Cao, Brad Lackey
- **PDF**: https://arxiv.org/pdf/2507.13496v1
- **Abstract**: It is generally unclear whether smaller codes can be "concatenated" to systematically create quantum LDPC codes or their sparse subsystem code cousins where the degree of the Tanner graph remains bounded while increasing the code distance. In this work, we use a slight generalization of concatenation called conjoining introduced by the quantum lego formalism. We show that by conjoining only quantum repetition codes, one can construct quantum LDPC codes. More generally, we provide an efficient iterative algorithm for constructing sparse subsystem codes with a distance guarantee that asymptotically saturates $kd^2=O(n)$ in the worst case. Furthermore, we show that the conjoining of even just two-qubit quantum bit-flip and phase-flip repetition codes is quite powerful as they can create any CSS code. Therefore, more creative combinations of these basic code blocks will be sufficient for generating good quantum codes, including good quantum LDPC codes.

## Expansion creates spin-glass order in finite-connectivity models: a rigorous and intuitive approach from the theory of LDPC codes

- **Status**: ❌
- **Reason**: 스핀글래스 물리학 이론(코드 확장성↔자유에너지 지형 등가성) — NAND LDPC에 떼어낼 디코더/HW/코드설계 기여 없음, 순수 이론
- **ID**: arxiv:2507.13342v1
- **Type**: preprint
- **Published**: 2025-07-17
- **Authors**: Benedikt Placke, Grace M. Sommers, Nikolas P. Breuckmann +2
- **PDF**: https://arxiv.org/pdf/2507.13342v1
- **Abstract**: Complex free-energy landscapes with many local minima separated by large barriers are believed to underlie glassy behavior across diverse physical systems. This is the heuristic picture associated with replica symmetry breaking (RSB) in spin glasses, but RSB has only been rigorously verified for certain mean-field models with all-to-all connectivity. In this work, we give a rigorous proof of finite temperature spin glass order for a family of models with local interactions on finite-connectivity, non-Euclidean expander graphs. To this end, we bypass the RSB formalism entirely, and instead exploit the mathematical equivalence of such models to certain low-density parity check (LDPC) codes. We use code expansion, a property of LDPC codes which guarantees extensive energy barriers around ground states. Together with mild additional assumptions, this allows us to construct an explicit decomposition of the low-temperature Gibbs state into disjoint components, each hosting an asymptotically long-lived state associated with a local minimum of the landscape. Each component carries at most an exponentially small fraction of the total weight, and almost all components do not contain ground states -- which we take together to define spin-glass order. The proof is elementary, and treats various expanding graph topologies on the same footing, including those with short loops where existing approaches such as the cavity method fail. Our results apply rigorously to diluted p-spin glasses for sufficiently large p, and while unproven, we also expect our assumptions to hold in a broader family of codes. Motivated by this, we numerically study two simple models, on random regular graphs and a regular tesselation of hyperbolic space. We show that both models undergo two transitions as a function of temperature, corresponding to the onset of weak ergodicity breaking and spin glass order, respectively.

## A mapping of the Min-Sum decoder to reduction operations, and its implementation using CUDA kernels

- **Status**: ✅
- **Reason**: Min-Sum 디코더를 reduction 연산으로 매핑하는 GPU(CUDA) 구현, parity matrix 내용 독립 — 이식 가능 디코더/HW 기법(C/D)
- **ID**: arxiv:2507.10424v1
- **Type**: preprint
- **Published**: 2025-07-14
- **Authors**: Omer Shimon Sella, Thomas Heinis
- **PDF**: https://arxiv.org/pdf/2507.10424v1
- **Abstract**: Decoders for Low Density Parity Check (LDPC) codes are usually tailored to an application and optimized once the specific content and structure of the parity matrix are known. In this work we consider the parity matrix as an argument of the Min-Sum decoder, and provide a GPU implementation that is independent of the content of the parity matrix, and relies only on its dimensions.

## High Girth Spatially-Coupled LDPC Codes with Hierarchical Structure

- **Status**: ✅
- **Reason**: QC SC-LDPC 대girth·소형 lifting 구성 알고리즘(HQC 확장, CRM 기반) — 바이너리 코드설계 새 기여(E)
- **ID**: arxiv:2507.10185v1
- **Type**: preprint
- **Published**: 2025-07-14
- **Authors**: Haizheng Li, Sisi Miao, Laurent Schmalen
- **PDF**: https://arxiv.org/pdf/2507.10185v1
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes are a class of LDPC codes with a simple construction facilitating hardware implementation while achieving excellent performance. In this paper, we introduce an algorithm that constructs QC spatially-coupled (SC) LDPC codes with large girth while keeping the constraint length small. The algorithm offers a "protograph to basegraph" construction, focusing on finding small lifting sizes of QC codes while avoiding short cycles. This work extends the hierarchical quasi-cyclic (HQC) construction for block LDPC codes proposed by Wang et al. to the spatially coupled case. The construction is based on the cycle relevant matrix (CRM) derived from the periodic structure of time-invariant SC-LDPC codes. Numerical results show that the proposed algorithm effectively achieves the target girth with a small lifting factor, enabling low-complexity SC code construction.

## Small Quantum Low Density Parity Check Codes for Near-Term Experiments

- **Status**: ❌
- **Reason**: 양자 LDPC(surface/color, weight-4 패리티, 초전도/스핀큐비트 구현) — 양자 전용, 고전 바이너리 이식 기법 없음, 원칙 제외
- **ID**: arxiv:2507.09690v3
- **Type**: preprint
- **Published**: 2025-07-13
- **Authors**: Christian Kraglund Andersen, Eliška Greplová
- **PDF**: https://arxiv.org/pdf/2507.09690v3
- **Abstract**: It is widely accepted that quantum error correction is essential for realizing large-scale fault-tolerant quantum computing. Recent experiments have demonstrated error correction codes operating below threshold, primarily using local planar codes such as the surface code and color code. In parallel, theoretical advances in quantum low-density parity-check (LDPC) codes promise significantly lower overheads, albeit at the cost of requiring non-local parity checks. While these results are encouraging, implementing such codes remains challenging for near-term experiments, creating obstacles to holistic benchmarking of hardware architectures capable of supporting long-range couplers. In this work, we present a simple construction recipe for small quantum LDPC codes based on recent developments in the field. Our codes are approximately twice as efficient as comparable surface codes, yet require only weight-four parity checks, which simplifies experimental realization compared to other quantum LDPC codes. We provide concrete proposals for implementations with superconducting qubits in flip-chip architectures and with semiconductor spin qubits using shuttling-based approaches.

## Low-depth quantum error correction via three-qubit gates in Rydberg atom arrays

- **Status**: ❌
- **Reason**: Rydberg 원자 어레이 surface code 스태빌라이저 readout 게이트 최적화 — 양자 EC 전용, 이식 가능 고전 LDPC 기법 없음
- **ID**: arxiv:2507.06096v2
- **Type**: preprint
- **Published**: 2025-07-08
- **Authors**: Laura Pecorari, Sven Jandura, Guido Pupillo
- **PDF**: https://arxiv.org/pdf/2507.06096v2
- **Abstract**: Quantum error correction (QEC) requires the execution of deep quantum circuits with large numbers of physical qubits to protect information against errors. Designing protocols that can reduce gate and space-time overheads of QEC is therefore crucial to enable more efficient QEC in near-term experiments. Multiqubit gates offer a natural path towards fast and low-depth stabilizer measurement circuits. However, they typically introduce high-weight correlated errors that can degrade the circuit-level distance, leading to slower scalings of the logical error probabilities. In this work, we show how to realize fast and efficient surface code stabilizer readout using only two singly-controlled $Z$ gates acting simultaneously on two target qubits, i.e. two $CZ_2$ gates -- instead of four $CZ$. We show that this scheme is fault-tolerant, and provide a blueprint for implementation in Rydberg atom arrays. We derive the time-optimal pulses implementing the gates and perform extensive QEC numerical simulations with Rydberg decay errors. Compared to the standard protocol using four $CZ$ gates, our scheme is faster, uses fewer gates and crucially maintains fault tolerance with comparable logical error probabilities. Fault-tolerant generalizations of this scheme to biased and erasure-dominant noise models, as well as to other QEC codes, such as quantum Low-Density Parity-Check codes, are also discussed.

## Unified Framework for Quantum Code Embedding

- **Status**: ❌
- **Reason**: CSS 양자코드 임베딩 통합 프레임워크(호몰로지 대수) — 양자 전용 개념 의존, 고전 바이너리 LDPC 이식 기법 없음
- **ID**: arxiv:2507.05361v3
- **Type**: preprint
- **Published**: 2025-07-07
- **Authors**: Andrew C. Yuan
- **PDF**: https://arxiv.org/pdf/2507.05361v3
- **Abstract**: Given a Calderbank-Shor-Steane (CSS) code, it is sometimes necessary to modify the code by adding an arbitrary number of physical qubits and parity checks. Motivations may include concatenating codes, embedding low-density parity check (LDPC) codes into finite-dimensional Euclidean space, or reducing the weights of parity checks. During this embedding, it is essential that the modified code possesses an isomorphic set of logical qubits as the original code. However, despite numerous explicit constructions, the conditions of when such a property holds true is not known in general. Therefore, using the language of homological algebra, we provide a unified framework that guarantees a natural isomorphism between the output and input codes. In particular, we explicitly show how previous works fit into our framework.

## Learning Variable Node Selection for Improved Multi-Round Belief Propagation Decoding

- **Status**: ✅
- **Reason**: 단블록 LDPC용 multi-round BP에서 perturb할 VN 선택을 학습(SBND 영감 신경망) — 이식 가능 디코더 새 기여(C)
- **ID**: arxiv:2507.03461v1
- **Type**: preprint
- **Published**: 2025-07-04
- **Authors**: Ahmad Ismail, Raphaël Le Bidan, Elsa Dupraz +1
- **PDF**: https://arxiv.org/pdf/2507.03461v1
- **Abstract**: Error correction at short blocklengths remains a challenge for low-density parity-check (LDPC) codes, as belief propagation (BP) decoding is suboptimal compared to maximum-likelihood decoding (MLD). While BP rarely makes errors, it often fails to converge due to a small number of problematic, erroneous variable nodes (VNs). Multi-round BP (MRBP) decoding improves performance by identifying and perturbing these VNs, enabling BP to succeed in subsequent decoding attempts. However, existing heuristic approaches for VN identification may require a large number of decoding rounds to approach ML performance. In this work, we draw a connection between identifying candidate VNs to perturb in MRBP and estimating channel output errors, a problem previously addressed by syndrome-based neural decoders (SBND). Leveraging this insight, we propose an SBND-inspired neural network architecture that learns to predict which VNs MRBP needs to focus on. Experimental results demonstrate that the proposed learning approach outperforms expert rules from the literature, requiring fewer MRBP decoding attempts to reach near-MLD performance. This makes it a promising lead for improving the decoding of short LDPC codes.

## Bias-tailored single-shot quantum LDPC codes

- **Status**: ❌
- **Reason**: Bias-tailored single-shot 양자 LDPC(hypergraph product, XZZX surface) — 양자 스태빌라이저 전용, 고전 이식 기법 없음
- **ID**: arxiv:2507.02239v1
- **Type**: preprint
- **Published**: 2025-07-03
- **Authors**: Shixin Wu, Todd A. Brun, Daniel A. Lidar
- **PDF**: https://arxiv.org/pdf/2507.02239v1
- **Abstract**: Quantum hardware rarely suffers equal amounts of bit-flip ($X$) and phase-flip ($Z$) errors; one type is often much more common than the other. A code that is ``bias-tailored'' can exploit this imbalance, lowering the fault-tolerance overhead. A complementary idea, called "single-shot" error correction, aims to recover from data errors and noisy measurements in a single round of stabilizer readout, avoiding slow repetition cycles. In this work, we combine these two ideas and build a hierarchy of new quantum codes.   The full construction starts from the syndrome-encoded hypergraph product code and then tailors it to the dominant error type. The resulting code keeps the single-shot guarantee for every noise model while boosting the threshold whenever $X$ and $Z$ errors are asymmetric.   By removing carefully chosen blocks of stabilizers we obtain two trimmed variants. The first, called the simplified code, cuts the physical-qubit count by $1/6$ and halves the number of stabilizer measurements, yet its minimum distance grows quadratically compared to the standard design and its biased noise threshold is unchanged. The second, called the reduced code, achieves the same hardware savings but trades away single-shot protection for purely $X$ or purely $Z$ noise; instead it remains single-shot under balanced, or depolarizing, noise. In settings where strongly biased noise is likely, either trimmed code offers a less resource-intensive alternative to the full construction.   As a concrete illustration, we lift the two-dimensional XZZX surface code to a three-dimensional cubic lattice and show that this ``3D XZZX'' code is an explicit member of the simplified family.   Taken together, these bias-tailored single-shot codes provide an adjustable set of code design alternatives, allowing tradeoffs between hardware overhead and noise types.

## Construction of LDPC convolutional codes with large girth from Latin squares

- **Status**: ✅
- **Reason**: Latin square 기반 대girth LDPC convolutional/block 코드 구성, 컴팩트 표현 — 바이너리 코드설계 새 기여(E)
- **ID**: arxiv:2507.00591v1
- **Type**: preprint
- **Published**: 2025-07-01
- **Authors**: Elisa Junghans, Julia Lieb
- **PDF**: https://arxiv.org/pdf/2507.00591v1
- **Abstract**: Due to their capacity approaching performance low-density parity-check (LDPC) codes gained a lot of attention in the last years. The parity-check matrix of the codes can be associated with a bipartite graph, called Tanner graph. To decrease the probability of decoding failure it is desirable to have LDPC codes with large girth of the associated Tanner graph. Moreover, to store such codes efficiently, it is desirable to have compact constructions for them. In this paper, we present constructions of LDPC convolutional codes with girth up to $12$ using a special class of Latin squares and several lifting steps, which enables a compact representation of these codes. With these techniques, we can provide constructions for well-performing and efficiently storable time-varying and time-invariant LDPC convolutional codes as well as for LDPC block codes.
