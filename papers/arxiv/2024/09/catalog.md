# arXiv — 2024-09


## Fault-Tolerant Belief Propagation for Practical Quantum Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.18689v1
- **Type**: preprint
- **Published**: 2024-09-27
- **Authors**: Kao-Yueh Kuo, Ching-Yi Lai
- **PDF**: https://arxiv.org/pdf/2409.18689v1
- **Abstract**: A fault-tolerant approach to reliable quantum memory is essential for scalable quantum computing, as physical qubits are susceptible to noise. Quantum error correction (QEC) must be continuously performed to prolong the memory lifetime. In QEC, error syndromes are generated rapidly, often within the execution time of a few quantum gates, requiring decoders to process this error data with equal speed. A typical QEC cycle involves multiple rounds of syndrome measurements, causing potential error locations to scale rapidly with the code size and the number of measurement rounds. However, no such decoders currently exist for general quantum low-density parity-check codes. In this paper, we propose a fault-tolerant belief propagation (FTBP) decoder that utilizes a space-time Tanner graph across multiple rounds of syndrome extraction with mixed-alphabet error variables. To enhance FTBP, we introduce a technique of probabilistic error consolidation to mitigate degeneracy effects and short cycles. Additionally, we propose an adaptive sliding window procedure that captures long error events across window boundaries and adjusts the decoding in real time. Our simulations demonstrate high error thresholds of 0.4%-0.87% and strong error-floor performance for topological code families, including rotated toric, toric color, and twisted XZZX toric codes.

## Computational Ghost Imaging with Low-Density Parity-Check Code

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.15596v1
- **Type**: preprint
- **Published**: 2024-09-23
- **Authors**: Shuang Liu, Yunkai Hu, Jinquan Qi +2
- **PDF**: https://arxiv.org/pdf/2409.15596v1
- **Abstract**: Ghost imaging (GI) is a high-resolution imaging technology that has been a subject of interest to many fields in the past 20 years. Most GI researchers focus on the reconstruction of signal under-sampling, nevertheless, how to use information redundancy to improve the result's belief in a complex environment has hardly been studied. Motivated by this, we propose a computational GI system based on the low-density parity-check (LDPC) coded radiation field by exploiting the signal redundancy. The non-ideal factors generated within the imaging process can be eliminated by setting up the matching fading channel model. We have derived the analytical lower bound on the bit error rate for the proposed LDPC-coded GI system. The effectiveness and performance of the LDPC-coded GI system are further validated through numerical and experiment results.

## LDPC Codes in Cooperative Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.15559v1
- **Type**: preprint
- **Published**: 2024-09-23
- **Authors**: Ali Mehrban
- **PDF**: https://arxiv.org/pdf/2409.15559v1
- **Abstract**: In fact, the broadcast nature of every transmitter makes it possible for other transceivers in the channel to overhear the broadcasted signal. The proposed idea in cooperative communication is to use these intermediate transceivers as relay for the transmitted signal, therefore we will have spatial diversity which can improve throughput and received data reliability in the system. In this dissertation we consider some important aspects of cooperative communication in a network composed of three nodes. First, we verify the increase of reliability for the received signal by comparing the reliability of the received bits in a cooperative network with a non-cooperative one. Then we step forward and use LDPC error correction technique to improve the reliability of the received bits even more and compare it with a network without LDPC codes (encoder and decoder) to measure the level of improvement for different SNRs. The overall aim of this dissertation is to deploy cooperative communication idea to consider and test its claimed aspects and also enhance its performance by using LDPC error correction technique.

## Flag Proxy Networks: Tackling the Architectural, Scheduling, and Decoding Obstacles of Quantum LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.14283v1
- **Type**: preprint
- **Published**: 2024-09-22
- **Authors**: Suhas Vittal, Ali Javadi-Abhari, Andrew W. Cross +2
- **PDF**: https://arxiv.org/pdf/2409.14283v1
- **Abstract**: Quantum error correction is necessary for achieving exponential speedups on important applications. The planar surface code has remained the most studied error-correcting code for the last two decades because of its relative simplicity. However, encoding a singular logical qubit with the planar surface code requires physical qubits quadratic in the code distance~($d$), making it space-inefficient for the large-distance codes necessary for promising applications. Thus, {\em Quantum Low-Density Parity-Check (QLDPC)} have emerged as an alternative to the planar surface code but require a higher degree of connectivity. Furthermore, the problems of fault-tolerant syndrome extraction and decoding are understudied for these codes and also remain obstacles to their usage.   In this paper, we consider two under-studied families of QLDPC codes: hyperbolic surface codes and hyperbolic color codes. We tackle the three challenges mentioned above as follows. {\em First}, we propose {\em Flag-Proxy Networks (FPNs)}, a generalizable architecture for quantum codes that achieves low connectivity through flag and proxy qubits. {\em Second}, we propose a {\em greedy syndrome extraction scheduling} algorithm for general quantum codes and further use this algorithm for fault-tolerant syndrome extraction on FPNs. {\em Third}, we present two decoders that leverage flag measurements to decode the hyperbolic codes accurately. Our work finds that degree-4 FPNs of the hyperbolic surface and color codes are respectively $2.9\times$ and $5.5\times$ more space-efficient than the $d = 5$ planar surface code, and become even more space-efficient when considering higher distances. The hyperbolic codes also have error rates comparable to their planar counterparts.

## Information Reconciliation for Continuous-Variable Quantum Key Distribution with $β> 1$ Using Short Blocklength Error Correction Codes: Proposal and Concerns

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.13667v2
- **Type**: preprint
- **Published**: 2024-09-20
- **Authors**: Kadir Gümüş, João dos Reis Frazão, Aaron Albores-Mejia +5
- **PDF**: https://arxiv.org/pdf/2409.13667v2
- **Abstract**: In this paper, we introduce a reconciliation protocol with a two-step error correction scheme that uses a short-blocklength, low-rate code and a long-blocklength, high-rate code. We simulate the protocol using a short-block-length low-density parity-check code and show that we can achieve reconciliation efficiencies above 1 using this method. We discuss the necessary steps required regarding security proofs before this protocol can be securely implemented.

## Mechanical Wannier-Stark Ladder of Diamond Spin-Mechanical Lamb Wave Resonators

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.12149v2
- **Type**: preprint
- **Published**: 2024-09-18
- **Authors**: Philip Andrango, Hailin Wang
- **PDF**: https://arxiv.org/pdf/2409.12149v2
- **Abstract**: We report the design and theoretical analysis of Wannier-Stark ladders of diamond Lamb wave resonators that feature mechanical compression modes with ultralow damping rates and host spin qubits with excellent optical and spin properties. The degree of localization in the mechanical Wannier-Stark ladder, which is determined by the ratio of coupling rate to frequency spacing between adjacent resonators, sets the effective range of phonon-mediated coupling between spin qubits. Three nearest-neighbor coupling schemes with distinct geometric configurations and a large range of coupling rates have been developed and analyzed. Additional analysis on the effects of disorder indicates that the proposed Wannier-Stark ladder can be robust against realistic experimental imperfections. The development of quantum networks of spin qubits with long-range connectivity can open the door to the implementation of newly developed quantum low-density parity-check codes in a solid-state system.

## Non-local resources for error correction in quantum LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.05818v2
- **Type**: preprint
- **Published**: 2024-09-09
- **Authors**: Omprakash Chandra, Gopikrishnan Muraleedharan, Gavin K. Brennen
- **PDF**: https://arxiv.org/pdf/2409.05818v2
- **Abstract**: Quantum low density parity check (qLDPC) codes are an attractive alternative to the surface code due to their relatively high code rate and distance. However, unlike the surface code which has simple, geometrically local, stabilizer checks, high performing qLDPC codes have non-local stabilizers that are challenging to measure. Recent advancements have shown how to deterministically perform high-fidelity, cavity mediated many-body gates, enabling the encoding and decoding of non-local GHZ states. We integrate this non-local resource into the DiVincenzo-Aliferis method of fault-tolerant stabilizer measurement for quantum hypergraph product and lifted product codes. Using circuit-level noise simulations, including the noise optimized cavity mediated gate, we find promising thresholds of $0.84 \%-0.60 \%$ for the hypergraph product code and psuedo-threshold of $0.3\%-0.4\%$ for the lifted product codes, with cavity cooperativities in the range $C\sim 10^4-10^6$. We propose a compatible tri-layer architectural layout for scheduling stabilizer measurements, enhancing circuit parallelizability.

## Effective Distance of Higher Dimensional HGPs and Weight-Reduced Quantum LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.02193v5
- **Type**: preprint
- **Published**: 2024-09-03
- **Authors**: Shi Jie Samuel Tan, Lev Stambler
- **PDF**: https://arxiv.org/pdf/2409.02193v5
- **Abstract**: Quantum error correction plays a prominent role in the realization of quantum computation, and quantum low-density parity-check (qLDPC) codes are believed to be practically useful stabilizer codes. While qLDPC codes are defined to have constant weight parity-checks, the weight of these parity checks could be large constants that make implementing these codes challenging. Large constants can also result in long syndrome extraction times and bad error propagation that can impact error correction performance. Hastings recently introduced weight reduction techniques for qLDPC codes that reduce the weight of the parity checks as well as the maximum number of checks that acts on any data qubit. However, the fault tolerance of these techniques remains an open question. In this paper, we analyze the effective distance of the weight-reduced code when single-ancilla syndrome extraction circuits are considered for error correction. We prove that there exists single-ancilla syndrome extraction circuits that largely preserve the effective distance of the weight-reduced qLDPC codes. In addition, we also show that the distance balancing technique introduced by Evra et al. preserves effective distance. As a corollary, our result shows that higher-dimensional hypergraph product (HGP) codes, also known as homological product codes corresponding to the product of 1-complexes, have no troublesome hook errors when using any single-ancilla syndrome extraction circuit.

## An almost-linear time decoding algorithm for quantum LDPC codes under circuit-level noise

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2409.01440v2
- **Type**: preprint
- **Published**: 2024-09-02
- **Authors**: Antonio deMarti iOlius, Imanol Etxezarreta Martinez, Joschka Roffe +1
- **PDF**: https://arxiv.org/pdf/2409.01440v2
- **Abstract**: Fault-tolerant quantum computers must be designed in conjunction with classical co-processors that decode quantum error correction measurement information in real-time. In this work, we introduce the belief propagation plus ordered Tanner forest (BP+OTF) algorithm as an almost-linear time decoder for quantum low-density parity-check codes. The OTF post-processing stage removes qubits from the decoding graph until it has a tree-like structure. Provided that the resultant loop-free OTF graph supports a subset of qubits that can generate the syndrome, BP decoding is then guaranteed to converge. To enhance performance under circuit-level noise, we introduce a technique for sparsifying detector error models. This method uses a transfer matrix to map soft information from the full detector graph to the sparsified graph, preserving critical error propagation information from the syndrome extraction circuit. Our BP+OTF implementation first applies standard BP to the full detector graph, followed by BP+OTF post-processing on the sparsified graph. Numerical simulations show that the BP+OTF decoder achieves similar logical error suppression compared to state-of-the-art inversion-based and matching decoders for bivariate bicycle and surface codes, respectively, while maintaining almost-linear runtime complexity across all stages.
