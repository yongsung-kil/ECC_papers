# arXiv — 2023-09


## Layer Codes

- **ID**: arxiv:2309.16503v2
- **Type**: preprint
- **Published**: 2023-09-28
- **Authors**: Dominic J. Williamson, Nouédyn Baspin
- **PDF**: https://arxiv.org/pdf/2309.16503v2
- **Abstract**: The surface code is a two-dimensional topological code with code parameters that scale optimally with the number of physical qubits, under the constraint of two-dimensional locality. In three spatial dimensions an analogous simple yet optimal code was not previously known. Here, we introduce a construction that takes as input a stabilizer code and produces as output a three-dimensional topological code with related code parameters. The output codes have the special structure of being topological defect networks formed by layers of surface code joined along one-dimensional junctions, with a maximum stabilizer check weight of six. When the input is a family of good low-density parity-check codes, the output is a three-dimensional topological code with optimal scaling code parameters and a polynomial energy barrier.

## Towards surgery with good quantum LDPC codes

- **ID**: arxiv:2309.16406v2
- **Type**: preprint
- **Published**: 2023-09-28
- **Authors**: Alexander Cowtan
- **PDF**: https://arxiv.org/pdf/2309.16406v2
- **Abstract**: We show that the good quantum LDPC codes of Panteleev-Kalachev \cite{PK} allow for surgery using any logical qubits, albeit incurring an asymptotic penalty which lowers the rate and distance scaling. We also prove that we can satisfy 3 of the 4 conditions for performing surgery \textit{without} incurring an asymptotic penalty. If the last condition is also satisfied then we can perform code surgery while maintaining $k, d\in Θ(n)$.

## Limitations of local update recovery in stabilizer-GKP codes: a quantum optimal transport approach

- **ID**: arxiv:2309.16241v1
- **Type**: preprint
- **Published**: 2023-09-28
- **Authors**: Robert König, Cambyse Rouzé
- **PDF**: https://arxiv.org/pdf/2309.16241v1
- **Abstract**: Local update recovery seeks to maintain quantum information by applying local correction maps alternating with and compensating for the action of noise. Motivated by recent constructions based on quantum LDPC codes in the finite-dimensional setting, we establish an analytic upper bound on the fault-tolerance threshold for concatenated GKP-stabilizer codes with local update recovery. Our bound applies to noise channels that are tensor products of one-mode beamsplitters with arbitrary environment states, capturing, in particular, photon loss occurring independently in each mode. It shows that for loss rates above a threshold given explicitly as a function of the locality of the recovery maps, encoded information is lost at an exponential rate. This extends an early result by Razborov from discrete to continuous variable (CV) quantum systems.   To prove our result, we study a metric on bosonic states akin to the Wasserstein distance between two CV density functions, which we call the bosonic Wasserstein distance. It can be thought of as a CV extension of a quantum Wasserstein distance of order 1 recently introduced by De Palma et al. in the context of qudit systems, in the sense that it captures the notion of locality in a CV setting. We establish several basic properties, including a relation to the trace distance and diameter bounds for states with finite average photon number. We then study its contraction properties under quantum channels, including tensorization, locality and strict contraction under beamsplitter-type noise channels. Due to the simplicity of its formulation, and the established wide applicability of its finite-dimensional counterpart, we believe that the bosonic Wasserstein distance will become a versatile tool in the study of CV quantum systems.

## Geometrically Local Quantum and Classical Codes from Subdivision

- **ID**: arxiv:2309.16104v2
- **Type**: preprint
- **Published**: 2023-09-28
- **Authors**: Ting-Chun Lin, Adam Wills, Min-Hsiu Hsieh
- **PDF**: https://arxiv.org/pdf/2309.16104v2
- **Abstract**: A geometrically local quantum code is an error correcting code situated within $\mathbb{R}^D$, where the checks only act on qubits within a fixed spatial distance. The main question is: What is the optimal dimension and distance for a geometrically local code? Recently, Portnoy made a significant breakthrough with codes achieving optimal dimension and distance up to polylogs. However, the construction invokes a somewhat advanced mathematical result that involves lifting a chain complex to a manifold. This paper bypasses this step and streamlines the construction by noticing that a family of good quantum low-density parity-check codes, balanced product codes, naturally carries a two-dimensional structure. Together with a new embedding result that will be shown elsewhere, this quantum code achieves the optimal dimension and distance in all dimensions. In addition, we show that the code has an optimal energy barrier. We also discuss similar results for classical codes.

## Splitting decoders for correcting hypergraph faults

- **ID**: arxiv:2309.15354v1
- **Type**: preprint
- **Published**: 2023-09-27
- **Authors**: Nicolas Delfosse, Adam Paetznick, Jeongwan Haah +1
- **PDF**: https://arxiv.org/pdf/2309.15354v1
- **Abstract**: The surface code is one of the most popular quantum error correction codes. It comes with efficient decoders, such as the Minimum Weight Perfect Matching (MWPM) decoder and the Union-Find (UF) decoder, allowing for fast quantum error correction. For a general linear code or stabilizer code, the decoding problem is NP-hard. What makes it tractable for the surface code is the special structure of faults and checks: Each X and Z fault triggers at most two checks. As a result, faults can be interpreted as edges in a graph whose vertices are the checks, and the decoding problem can be solved using standard graph algorithms such as Edmonds' minimum-weight perfect matching algorithm. For general codes, this decoding graph is replaced by a hypergraph making the decoding problem more challenging. In this work, we propose two heuristic algorithms for splitting the hyperedges of a decoding hypergraph into edges. After splitting, hypergraph faults can be decoded using any surface code decoder. Due to the complexity of the decoding problem, we do not expect this strategy to achieve a good error correction performance for a general code. However, we empirically show that this strategy leads to a good performance for some classes of LDPC codes because they are defined by low weight checks. We apply this splitting decoder to Floquet codes for which some faults trigger up to four checks and verify numerically that this decoder achieves the maximum code distance for two instances of Floquet codes.

## Long-range-enhanced surface codes

- **ID**: arxiv:2309.11719v4
- **Type**: preprint
- **Published**: 2023-09-21
- **Authors**: Yifan Hong, Matteo Marinelli, Adam M. Kaufman +1
- **PDF**: https://arxiv.org/pdf/2309.11719v4
- **Abstract**: The surface code is a quantum error-correcting code for one logical qubit, protected by spatially localized parity checks in two dimensions. Due to fundamental constraints from spatial locality, storing more logical qubits requires either sacrificing the robustness of the surface code against errors or increasing the number of physical qubits. We bound the minimal number of spatially nonlocal parity checks necessary to add logical qubits to a surface code while maintaining, or improving, robustness to errors. We saturate the lower limit of this bound, when the number of added logical qubits is a constant, using a family of hypergraph product codes, interpolating between the surface code and constant-rate low-density parity-check codes. Fault-tolerant protocols for logical gates in the quantum code can be inherited from its classical parent codes. We provide near-term practical implementations of this code for hardware based on trapped ions or neutral atoms in mobile optical tweezers. Long-range-enhanced surface codes outperform conventional surface codes using hundreds of physical qubits, and represent a practical strategy to enhance the robustness of logical qubits to errors in near-term devices.

## Efficient LDPC Decoding using Physical Computation

- **ID**: arxiv:2312.02161v1
- **Type**: preprint
- **Published**: 2023-09-21
- **Authors**: Uday Kumar Reddy Vengalam, Andrew Hahn, Yongchao Liu +3
- **PDF**: https://arxiv.org/pdf/2312.02161v1
- **Abstract**: Due to 5G deployment, there is significant interest in LDPC decoding. While much research is devoted on efficient hardwiring of algorithms based on Belief Propagation (BP), it has been shown that LDPC decoding can be formulated as a combinatorial optimization problem, which could benefit from significant acceleration of physical computation mechanisms such as Ising machines. This approach has so far resulted in poor performance. This paper shows that the reason is not fundamental but suboptimal hardware and formulation. A co-designed Ising machine-based system can improve speed by 3 orders of magnitude. As a result, a physical computation approach can outperform hardwiring state-of-the-art algorithms. In this paper, we show such an augmented Ising machine that is 4.4$\times$ more energy efficient than the state of the art in the literature.

## New Quantum LDPC Codes Based on Euclidean Geometry

- **ID**: arxiv:2310.02197v1
- **Type**: preprint
- **Published**: 2023-09-07
- **Authors**: Ya'nan Feng, Chuchen Tang, Chenming Bai
- **PDF**: https://arxiv.org/pdf/2310.02197v1
- **Abstract**: With the development of quantum error correction techniques, quantum low density parity check (QLDPC) codes become a promising area in quantum error correction codes. In this paper, the requirements of QLDPC codes based on points except the origin and lines not passing through the origin of Euclidean geometry are given. QLDPC codes based on all the lines and parallel classes are obtained respectively.
