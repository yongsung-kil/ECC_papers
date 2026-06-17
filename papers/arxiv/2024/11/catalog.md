# arXiv — 2024-11


## Neural Window Decoder for SC-LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.19092v2
- **Type**: preprint
- **Published**: 2024-11-28
- **Authors**: Dae-Young Yun, Hee-Youl Kwak, Yongjune Kim +2
- **PDF**: https://arxiv.org/pdf/2411.19092v2
- **Abstract**: In this paper, we propose a neural window decoder (NWD) for spatially coupled low-density parity-check (SC-LDPC) codes. The proposed NWD retains the conventional window decoder (WD) process but incorporates trainable neural weights. To train the weights of NWD, we introduce two novel training strategies. First, we restrict the loss function to target variable nodes (VNs) of the window, which prunes the neural network and accordingly enhances training efficiency. Second, we employ the active learning technique with a normalized loss term to prevent the training process from biasing toward specific training regions. Next, we develop a systematic method to derive non-uniform schedules for the NWD based on the training results. We introduce trainable damping factors that reflect the relative importance of check node (CN) updates. By skipping updates with less importance, we can omit $\mathbf{41\%}$ of CN updates without performance degradation compared to the conventional WD. Lastly, we address the error propagation problem inherent in SC-LDPC codes by deploying a complementary weight set, which is activated when an error is detected in the previous window. This adaptive decoding strategy effectively mitigates error propagation without requiring modifications to the code and decoder structures.

## Iterative Gradient Descent Decoding for Real Number LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.16203v1
- **Type**: preprint
- **Published**: 2024-11-25
- **Authors**: Oana Boncalo, Alexandru Amaricai
- **PDF**: https://arxiv.org/pdf/2411.16203v1
- **Abstract**: This paper proposes a new iterative gradient descent decoding method for real number parity codes. The proposed decoder, named Gradient Descent Symbol Update (GDSU), is used for a class of low-density parity-check (LDPC) real-number codes that can be defined with parity check matrices which are similar to those of the binary LDPC from communication standards such as WiFi (IEEE 802.11), 5G. These codes have a simple and efficient two stage encoding that is especially appealing for the real number field. The Gradient optimization based decoding has been a relatively simple and fast decoding technique for codes over finite fields. We show that the GDSU decoder outperforms the gradient descent bit-flipping (GDBF) decoder for rates $1/2$, $2/3$, and has similar decoding performance for the $3/4$ rate of the IEEE 802.11 codes standard.

## Classifying Logical Gates in Quantum Codes via Cohomology Operations and Symmetry

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.15848v3
- **Type**: preprint
- **Published**: 2024-11-24
- **Authors**: Po-Shen Hsin, Ryohei Kobayashi, Guanyu Zhu
- **PDF**: https://arxiv.org/pdf/2411.15848v3
- **Abstract**: We systematically construct and classify fault-tolerant logical gates implemented by constant-depth circuits for quantum codes using cohomology operations and symmetry. These logical gates are obtained from unitary operators given by symmetry-protected topological responses, which correspond to generators of group cohomology and can be expressed explicitly on the lattice using cohomology operations including cup product, Steenrod squares and new combinations of higher cup products called higher Pontryagin powers. Our study covers most types of the cohomology operations in the literature. This hence gives rise to logical $C^{n-1}Z$ gates in $n$ copies of quantum codes via the $n$-fold cup product in the usual color code paradigm, as well as several new classes of diagonal and non-diagonal logical gates in increasing Clifford hierarchies beyond the color code paradigm, including the logical $R_k$ and multi-controlled $C^m R_k$ gates for codes defined in projective spaces. Implementing these gates could make it more efficient to compile specific types of quantum algorithms such as Shor's algorithm. We further extend the construction to quantum codes with boundaries, which generalizes the folding approach in color codes. We also present a formalism for addressable and parallelizable logical gates in LDPC codes via higher-form symmetries. We further construct logical Clifford gates in expander-based codes including the asymptotically good LDPC codes and hypergraph-product codes. As a byproduct, we find new topological responses of finite higher-form symmetries using higher Pontryagin powers.

## On fault tolerant single-shot logical state preparation and robust long-range entanglement

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.04405v1
- **Type**: preprint
- **Published**: 2024-11-07
- **Authors**: Thiago Bergamaschi, Yunchao Liu
- **PDF**: https://arxiv.org/pdf/2411.04405v1
- **Abstract**: Preparing encoded logical states is the first step in a fault-tolerant quantum computation. Standard approaches based on concatenation or repeated measurement incur a significant time overhead. The Raussendorf-Bravyi-Harrington cluster state offers an alternative: a single-shot preparation of encoded states of the surface code, by means of a constant depth quantum circuit, followed by a single round of measurement and classical feedforward. In this work we generalize this approach and prove that single-shot logical state preparation can be achieved for arbitrary quantum LDPC codes. Our proof relies on a minimum-weight decoder and is based on a generalization of Gottesman's clustering-of-errors argument. As an application, we also prove single-shot preparation of the encoded GHZ state in arbitrary quantum LDPC codes. This shows that adaptive noisy constant depth quantum circuits are capable of generating generic robust long-range entanglement.

## List Decodable Quantum LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.04306v1
- **Type**: preprint
- **Published**: 2024-11-06
- **Authors**: Thiago Bergamaschi, Fernando Granha Jeronimo, Tushant Mittal +2
- **PDF**: https://arxiv.org/pdf/2411.04306v1
- **Abstract**: We give a construction of Quantum Low-Density Parity Check (QLDPC) codes with near-optimal rate-distance tradeoff and efficient list decoding up to the Johnson bound in polynomial time. Previous constructions of list decodable good distance quantum codes either required access to a classical side channel or were based on algebraic constructions that preclude the LDPC property.   Our construction relies on new algorithmic results for codes obtained via the quantum analog of the distance amplification scheme of Alon, Edmonds, and Luby [FOCS 1995]. These results are based on convex relaxations obtained using the Sum-of-Squares hierarchy, which reduce the problem of list decoding the distance amplified codes to unique decoding the starting base codes. Choosing these base codes to be the recent breakthrough constructions of good QLDPC codes with efficient unique decoders, we get efficiently list decodable QLDPC codes.

## Soft Reverse Reconciliation for Discrete Modulations

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.04063v2
- **Type**: preprint
- **Published**: 2024-11-06
- **Authors**: Marco Origlia, Marco Secondini
- **PDF**: https://arxiv.org/pdf/2411.04063v2
- **Abstract**: The performance of the information reconciliation phase is crucial for quantum key distribution (QKD). Reverse reconciliation (RR) is typically preferred over direct reconciliation (DR) because it yields higher secure key rates. However, a significant challenge in continuous-variable (CV) QKD with discrete modulations (such as QAM) is that Alice lacks soft information about the symbol decisions made by Bob. This limitation restricts error correction to hard-decoding methods, with low reconciliation efficiency. This work introduces a reverse reconciliation softening (RRS) procedure designed for CV-QKD scenarios employing discrete modulations. This procedure generates a soft metric that Bob can share with Alice over a public channel, enabling her to perform soft-decoding error correction without disclosing any information to a potential eavesdropper. After detailing the RRS procedure, we investigate how the mutual information between Alice's and Bob's variables changes when the additional metric is shared. We show numerically that RRS improves the mutual information with respect to RR with hard decoding, practically achieving the same mutual information as DR with soft decoding. Finally, we test the proposed RRS for PAM-4 signalling with a rate 1/2 binary LDPC code and bit-wise decoding through numerical simulations, obtaining more than 1dB SNR improvement compared to hard-decoding RR.

## Polylog-time- and constant-space-overhead fault-tolerant quantum computation with quantum low-density parity-check codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.03683v2
- **Type**: preprint
- **Published**: 2024-11-06
- **Authors**: Shiro Tamiya, Masato Koashi, Hayata Yamasaki
- **PDF**: https://arxiv.org/pdf/2411.03683v2
- **Abstract**: A major challenge in fault-tolerant quantum computation (FTQC) is to reduce both space overhead -- the large number of physical qubits per logical qubit -- and time overhead -- the long physical gate sequences per logical gate. We prove that a protocol using non-vanishing-rate quantum low-density parity-check (LDPC) codes, combined with concatenated Steane codes, achieves constant space overhead and polylogarithmic time overhead, even when accounting for non-zero classical computation time. This protocol offers an improvement over existing constant-space-overhead protocols, which have polynomial time overhead using quantum LDPC codes and quasi-polylogarithmic time overhead using concatenated quantum Hamming codes. To ensure the completeness of this proof, we develop a technique called partial circuit reduction, which enables error analysis for the entire fault-tolerant circuit by examining smaller parts composed of a few gadgets. With this technique, we resolve a previously unaddressed logical gap in the existing arguments and complete the proof of the threshold theorem for the constant-space-overhead protocol with quantum LDPC codes. Our work highlights that the quantum-LDPC-code approach can realize FTQC with a negligibly small slowdown and a bounded overhead of physical qubits, similar to the code-concatenation approach, underscoring the importance of a comprehensive comparison of the future realizability of these two approaches.

## Quantum LDPC Codes of Almost Linear Distance via Homological Products

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.03646v1
- **Type**: preprint
- **Published**: 2024-11-06
- **Authors**: Louis Golowich, Venkatesan Guruswami
- **PDF**: https://arxiv.org/pdf/2411.03646v1
- **Abstract**: We present new constructions of quantum codes of linear or close-to-linear distance and dimension with low-weight stabilizers. Only a few constructions of such codes were previously known, and were primarily based on a specific operation from homological algebra, namely the balanced product. In contrast, our constructions are based on a more basic and widely used product, namely the homological product (i.e. the tensor product of chain complexes). Our results help address the natural question: When do homological products preserve good code distance?   Our first main result constructs asymptotically good $[[N,Θ(N),Θ(N)]]$ quantum codes with small polynomial stabilizer weight from homological products of codes with a property called product-expansion. This notion was recently introduced and used to bound the distance of balanced product quantum codes; we apply it instead to homological products.   For every $ε>0$, our second main result constructs close-to-linear distance $[[N,N^{1-ε},N^{1-ε}]]$ (subsystem) quantum LDPC codes with constant stabilizer weight from iterated homological products of a constant-sized quantum locally testable code. The key insight here is that by using subsystem codes (but still with constant-weight stabilizers), we can circumvent a particular obstruction that limited the distance of many prior product code constructions to at most $\tilde{O}(\sqrt{N})$.

## Generalizing the matching decoder for the Chamon code

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.03443v2
- **Type**: preprint
- **Published**: 2024-11-05
- **Authors**: Zohar Schwartzman-Nowik, Benjamin J. Brown
- **PDF**: https://arxiv.org/pdf/2411.03443v2
- **Abstract**: Different choices of quantum error-correcting codes can reduce the demands on the physical hardware needed to build a quantum computer. To achieve the full potential of a code, we must develop practical decoding algorithms that can correct errors that have occurred with high likelihood. Matching decoders are very good at correcting local errors while also demonstrating fast run times that can keep pace with physical quantum devices. We implement variations of a matching decoder for a three-dimensional, non-CSS, low-density parity check code known as the Chamon code, which has a non-trivial structure that does not lend itself readily to this type of decoding. The non-trivial structure of the syndrome of this code means that we can supplement the decoder with additional steps to improve the threshold error rate, below which the logical failure rate decreases with increasing code distance. We find that a generalized matching decoder that is augmented by a belief-propagation step prior to matching gives a threshold of 10.5% for depolarizing noise.

## LDPC stabilizer codes as gapped quantum phases: stability under graph-local perturbations

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.02384v2
- **Type**: preprint
- **Published**: 2024-11-04
- **Authors**: Wojciech De Roeck, Vedika Khemani, Yaodong Li +2
- **PDF**: https://arxiv.org/pdf/2411.02384v2
- **Abstract**: We generalize the proof of stability of topological order, due to Bravyi, Hastings and Michalakis, to stabilizer Hamiltonians corresponding to low-density parity check (LDPC) codes without the restriction of geometric locality in Euclidean space. We consider Hamiltonians $H_0$ defined by $[[N,K,d]]$ LDPC codes which obey certain topological quantum order conditions: (i) code distance $d \geq c \log(N)$, implying local indistinguishability of ground states, and (ii) a mild condition on local and global compatibility of ground states; these include good quantum LDPC codes, and the toric code on a hyperbolic lattice, among others. We consider stability under weak perturbations that are quasi-local on the interaction graph defined by $H_0$, and which can be represented as sums of bounded-norm terms. As long as the local perturbation strength is smaller than a finite constant, we show that the perturbed Hamiltonian has well-defined spectral bands originating from the $O(1)$ smallest eigenvalues of $H_0$. The band originating from the smallest eigenvalue has $2^K$ states, is separated from the rest of the spectrum by a finite energy gap, and has exponentially narrow bandwidth $δ= C N e^{-Θ(d)}$, which is tighter than the best known bounds even in the Euclidean case. We also obtain that the new ground state subspace is related to the initial code subspace by a quasi-local unitary, allowing one to relate their physical properties. Our proof uses an iterative procedure that performs successive rotations to eliminate non-frustration-free terms in the Hamiltonian. Our results extend to quantum Hamiltonians built from classical LDPC codes, which give rise to stable symmetry-breaking phases. These results show that LDPC codes very generally define stable gapped quantum phases, even in the non-Euclidean setting, initiating a systematic study of such phases of matter.

## Magic states are rarely the best resource to optimize: An analytical tool for qubit resource estimation in concatenated codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.01880v2
- **Type**: preprint
- **Published**: 2024-11-04
- **Authors**: Marco Fellous-Asiani, Hui Khoon Ng, Robert S. Whitney
- **PDF**: https://arxiv.org/pdf/2411.01880v2
- **Abstract**: Concatenated error-correction schemes are well-understood routes to fault-tolerant quantum computing, and research on such schemes continues, including recent claims that they may be competitive with surface codes, and show potential when combined with high-rate Quantum Low Density Parity Check codes. However, there are few tools to evaluate the qubit resources required by concatenated schemes. We propose such a tool here. Its equations are closed-form and remain simple for an arbitrary number of levels of concatenation, making it ideal for comparing and minimizing the resource costs of such schemes. We use this tool to evaluate the resources for gate operations that require the injection of so-called ``magic states'', needed to complete the set of logical operations. It was expected that the complexity of such ``magic operations" would make them dominate the resource costs of a calculation, with numerous works proposing optimizations of these cost. Our work reveals that this expectation is often inaccurate: Magic operations are rarely the dominant cost of concatenated schemes, mirroring similar conclusions from past work for surface codes. Optimizations affecting all operations naturally have more impact than those on magic operations alone, yet we unexpected find that the former can reduce qubit resources by a few orders of magnitude while the latter give only marginal reductions. We show this in detail for a 7-qubit concatenated scheme with Steane error-correction gadgets or flag-qubits gadgets, and argue that our findings are representative of most concatenated schemes.

## Efficient Realization of Multi-channel Visible Light Communication System for Dynamic Cross-Water Surface Channels

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.11866v1
- **Type**: preprint
- **Published**: 2024-11-03
- **Authors**: Han Qi, Tianrui Lin, Tianjian Wei +4
- **PDF**: https://arxiv.org/pdf/2411.11866v1
- **Abstract**: This paper explores the transmission schemes for multi-channel water-to-air optical wireless communication (W2A-OWC) and introduces a prototype of a real-time W2A-OWC system based on a field-programmable gate array (FPGA). Utilizing an LED array as the transmitter and an APD array as the receiver, the system establishes a multi-channel transmission module. Such configuration enables parallel operation of multiple channels, facilitating the simultaneous transmission of multiple data streams and enhancing overall throughput. The FPGA serves as a real-time signal processing unit, handling both signal transmission and reception. By integrating low-density parity-check (LDPC) codes from 5G New Radio, the system significantly boosts its detection capabilities for dynamic W2A-OWC scenarios. The system also optimizes FPGA resource usage through time-multiplexing operation of an LDPC decoder's IP core. To evaluate the system's practicality, experiments were conducted under background radiation in an indoor water tank, measuring the frame error rate under both calm and fluctuating water surfaces. The experimental results confirm the feasibility and effectiveness of the developed W2A-OWC system.

## Study of Iterative Detection and Decoding for RIS-Aided Multiuser Multi-Antenna Systems

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.01388v1
- **Type**: preprint
- **Published**: 2024-11-03
- **Authors**: R. Porto, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2411.01388v1
- **Abstract**: We present a novel iterative detection and decoding (IDD) scheme for Reconfigurable Intelligent Surface (RIS)-assisted multiuser multiple-antenna systems. The proposed approach introduces a joint iterative detection strategy that integrates Low-Density Parity-Check (LDPC) codes, RIS processing and iterative detection and decoding. In particular, we employ a minimum mean square error receive filter that performs truncation at the RIS and soft interference cancelation at the receiver. Simulation results evaluate the system's overall capacity and bit error rate, and demonstrate substantial improvements in bit error rate across block-fading channels.

## Low-density parity-check codes as stable phases of quantum matter

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:2411.01002v2
- **Type**: preprint
- **Published**: 2024-11-01
- **Authors**: Chao Yin, Andrew Lucas
- **PDF**: https://arxiv.org/pdf/2411.01002v2
- **Abstract**: Phases of matter with robust ground-state degeneracy, such as the quantum toric code, are known to be capable of robust quantum information storage. Here, we address the converse question: given a quantum error correcting code, when does it define a stable gapped quantum phase of matter, whose ground state degeneracy is robust against perturbations in the thermodynamic limit? We prove that a low-density parity-check (LDPC) code defines such a phase, robust against all few-body perturbations, if its code distance grows at least logarithmically in the number of degrees of freedom, and it exhibits "check soundness". Many constant-rate quantum LDPC expander codes have such properties, and define stable phases of matter with a constant zero-temperature entropy density, violating the third law of thermodynamics. Our results also show that quantum toric code phases are robust to spatially nonlocal few-body perturbations. Similarly, phases of matter defined by classical codes are stable against symmetric perturbations. In the classical setting, we present improved locality bounds on the quasiadiabatic evolution operator between two nearby states in the same code phase.
