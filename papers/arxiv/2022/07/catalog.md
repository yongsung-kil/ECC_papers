# arXiv — 2022-07


## Time-Efficient Constant-Space-Overhead Fault-Tolerant Quantum Computation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2207.08826v3
- **Type**: preprint
- **Published**: 2022-07-18
- **Authors**: Hayata Yamasaki, Masato Koashi
- **PDF**: https://arxiv.org/pdf/2207.08826v3
- **Abstract**: Scaling up quantum computers to attain substantial speedups over classical computing requires fault tolerance. Conventionally, protocols for fault-tolerant quantum computation demand excessive space overheads by using many physical qubits for each logical qubit. A more recent protocol using quantum analogues of low-density parity-check codes needs only a constant space overhead that does not grow with the number of logical qubits. However, the overhead in the processing time required to implement this protocol grows polynomially with the number of computational steps. To address these problems, here we introduce an alternative approach to constant-space-overhead fault-tolerant quantum computing using a concatenation of multiple small-size quantum codes rather than a single large-size quantum low-density parity-check code. We develop techniques for concatenating different quantum Hamming codes with growing sizes. As a result, we construct a low-overhead protocol to achieve constant space overhead and only quasi-polylogarithmic time overhead simultaneously. Our protocol is fault tolerant even if a decoder has a non-constant runtime, unlike the existing constant-space-overhead protocol. This code concatenation approach will make possible a large class of quantum speedups within feasibly bounded space overhead yet negligibly short time overhead.

## Conservation laws and quantum error correction: towards a generalised matching decoder

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2207.06428v2
- **Type**: preprint
- **Published**: 2022-07-13
- **Authors**: Benjamin J. Brown
- **PDF**: https://arxiv.org/pdf/2207.06428v2
- **Abstract**: Decoding algorithms are essential to fault-tolerant quantum-computing architectures. In this perspective we explore decoding algorithms for the surface code; a prototypical quantum low-density parity-check code that underlies many of the leading efforts to demonstrate scalable quantum computing. Central to our discussion is the minimum-weight perfect-matching decoder. The decoder works by exploiting underlying structure that arises due to materialised symmetries among surface-code stabilizer elements. By concentrating on these symmetries, we begin to address the question of how a minimum-weight perfect-matching decoder might be generalised for other families of codes. We approach this question first by investigating examples of matching decoders for other codes. These include decoding algorithms that have been specialised to correct for noise models that demonstrate a particular structure or bias with respect to certain codes. In addition to this, we propose a systematic way of constructing a minimum-weight perfect-matching decoder for codes with certain characteristic properties. The properties we make use of are common among topological codes. We discuss the broader applicability of the proposal, and we suggest some questions we can address that may show us how to design a generalised matching decoder for arbitrary stabilizer codes.

## Belief Propagation with Quantum Messages for Symmetric Classical-Quantum Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2207.04984v1
- **Type**: preprint
- **Published**: 2022-07-11
- **Authors**: S. Brandsen, Avijit Mandal, Henry D. Pfister
- **PDF**: https://arxiv.org/pdf/2207.04984v1
- **Abstract**: Belief propagation (BP) is a classical algorithm that approximates the marginal distribution associated with a factor graph by passing messages between adjacent nodes in the graph. It gained popularity in the 1990's as a powerful decoding algorithm for LDPC codes. In 2016, Renes introduced a belief propagation with quantum messages (BPQM) and described how it could be used to decode classical codes defined by tree factor graphs that are sent over the classical-quantum pure-state channel. In this work, we propose an extension of BPQM to general binary-input symmetric classical-quantum (BSCQ) channels based on the implementation of a symmetric "paired measurement". While this new paired-measurement BPQM (PMBPQM) approach is suboptimal in general, it provides a concrete BPQM decoder that can be implemented with local operations.

## High-throughput decoder of quasi-cyclic LDPC codes with limited precision for continuous-variable quantum key distribution systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2207.01860v1
- **Type**: preprint
- **Published**: 2022-07-05
- **Authors**: Chuang Zhou, Yang Li, Li Ma +7
- **PDF**: https://arxiv.org/pdf/2207.01860v1
- **Abstract**: More than Mbps secret key rate was demonstrated for continuous-variable quantum key distribution (CV-QKD) systems, but real-time postprocessing is not allowed, which is restricted by the throughput of the error correction decoding in postprocessing. In this paper, a high-throughput FPGA-based quasi-cyclic LDPC decoder is proposed and implemented to support Mbps real-time secret key rate generation for CV-QKD for the first time. A residual bit error correction algorithm is used to solve the problem of high frame errors rate (FER) caused by the limited precision of the decoder. Specifically, real-time high-speed decoding for CV-QKD systems with typical code rates 0.2 and 0.1 is implemented on a commercial FPGA, and two throughputs of 360.92Mbps and 194.65Mbps are achieved, respectively, which can support 17.97 Mbps and 2.48 Mbps real-time generation of secret key rates under typical transmission distances of 25km and 50km, correspondingly. The proposed method paves the way for high-rate real-time CV-QKD deployment in secure metropolitan area network.

## Grant-Free Transmission by LDPC Matrix Mapping and Integrated Cover-MPA Detector

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:2207.00272v1
- **Type**: preprint
- **Published**: 2022-07-01
- **Authors**: Linjie Yang, Pingzhi Fan, Li Li +2
- **PDF**: https://arxiv.org/pdf/2207.00272v1
- **Abstract**: In this paper, a novel transceiver architecture is proposed to simultaneously achieve efficient random access and reliable data transmission in massive IoT networks. At the transmitter side, each user is assigned a unique protocol sequence which is used to identify the user and also indicate the user's channel access pattern. Hence, user identification is completed by the detection of channel access patterns. Particularly, the columns of a parity check matrix of low-density-parity-check (LDPC) code are employed as protocol sequences. The design guideline of this LDPC parity check matrix and the associated performance analysis are provided in this paper.At the receiver side, a two-stage iterative detection architecture is designed, which consists of a group testing component and a payload data decoding component. They collaborate in a way that the group testing component maps detected protocol sequences to a tanner graph, on which the second component could execute its message passing algorithm. In turn, zero symbols detected by the message passing algorithm of the second component indicate potential false alarms made by the first group testing component. Hence, the tanner graph could iteratively evolve.The provided simulation results demonstrate that our transceiver design realizes a practical one-step grant-free transmission and has a compelling performance.
