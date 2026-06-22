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

## Bias-tailored single-shot quantum LDPC codes

- **Status**: ❌
- **Reason**: Bias-tailored single-shot 양자 LDPC(hypergraph product, XZZX surface) — 양자 스태빌라이저 전용, 고전 이식 기법 없음
- **ID**: arxiv:2507.02239v1
- **Type**: preprint
- **Published**: 2025-07-03
- **Authors**: Shixin Wu, Todd A. Brun, Daniel A. Lidar
- **PDF**: https://arxiv.org/pdf/2507.02239v1
- **Abstract**: Quantum hardware rarely suffers equal amounts of bit-flip ($X$) and phase-flip ($Z$) errors; one type is often much more common than the other. A code that is ``bias-tailored'' can exploit this imbalance, lowering the fault-tolerance overhead. A complementary idea, called "single-shot" error correction, aims to recover from data errors and noisy measurements in a single round of stabilizer readout, avoiding slow repetition cycles. In this work, we combine these two ideas and build a hierarchy of new quantum codes.   The full construction starts from the syndrome-encoded hypergraph product code and then tailors it to the dominant error type. The resulting code keeps the single-shot guarantee for every noise model while boosting the threshold whenever $X$ and $Z$ errors are asymmetric.   By removing carefully chosen blocks of stabilizers we obtain two trimmed variants. The first, called the simplified code, cuts the physical-qubit count by $1/6$ and halves the number of stabilizer measurements, yet its minimum distance grows quadratically compared to the standard design and its biased noise threshold is unchanged. The second, called the reduced code, achieves the same hardware savings but trades away single-shot protection for purely $X$ or purely $Z$ noise; instead it remains single-shot under balanced, or depolarizing, noise. In settings where strongly biased noise is likely, either trimmed code offers a less resource-intensive alternative to the full construction.   As a concrete illustration, we lift the two-dimensional XZZX surface code to a three-dimensional cubic lattice and show that this ``3D XZZX'' code is an explicit member of the simplified family.   Taken together, these bias-tailored single-shot codes provide an adjustable set of code design alternatives, allowing tradeoffs between hardware overhead and noise types.
