# arXiv — 2023-04


## Spatially-Coupled QLDPC Codes

- **ID**: arxiv:2305.00137v6
- **Type**: preprint
- **Published**: 2023-04-29
- **Authors**: Siyi Yang, Robert Calderbank
- **PDF**: https://arxiv.org/pdf/2305.00137v6
- **Abstract**: Spatially-coupled (SC) codes is a class of convolutional LDPC codes that has been well investigated in classical coding theory thanks to their high performance and compatibility with low-latency decoders. We describe toric codes as quantum counterparts of classical two-dimensional spatially-coupled (2D-SC) codes, and introduce spatially-coupled quantum LDPC (SC-QLDPC) codes as a generalization. We use the convolutional structure to represent the parity check matrix of a 2D-SC code as a polynomial in two indeterminates, and derive an algebraic condition that is both necessary and sufficient for a 2D-SC code to be a stabilizer code. This algebraic framework facilitates the construction of new code families. While not the focus of this paper, we note that small memory facilitates physical connectivity of qubits, and it enables local encoding and low-latency windowed decoding. In this paper, we use the algebraic framework to optimize short cycles in the Tanner graph of 2D-SC hypergraph product (HGP) codes that arise from short cycles in either component code. While prior work focuses on QLDPC codes with rate less than 1/10, we construct 2D-SC HGP codes with small memories, higher rates (about 1/3), and superior thresholds.

## Spacetime codes of Clifford circuits

- **ID**: arxiv:2304.05943v2
- **Type**: preprint
- **Published**: 2023-04-12
- **Authors**: Nicolas Delfosse, Adam Paetznick
- **PDF**: https://arxiv.org/pdf/2304.05943v2
- **Abstract**: We propose a scheme for detecting and correcting faults in any Clifford circuit. The scheme is based on the observation that the set of all possible outcome bit-strings of a Clifford circuit is a linear code, which we call the outcome code. From the outcome code we construct a corresponding stabilizer code, the spacetime code. Our construction extends the circuit-to-code construction of Bacon, Flammia, Harrow and Shi [2], revisited recently by Gottesman [16], to include intermediate and multi-qubit measurements. With this correspondence, we reduce the problem of correcting faults in a circuit to the well-studied problem of correcting errors in a stabilizer code. More precisely, a most likely error decoder for the spacetime code can be transformed into a most likely fault decoder for the circuit. We give efficient algorithms to construct the outcome and spacetime codes. We also identify conditions under which these codes are LDPC, and give an algorithm to generate low-weight checks, which can then be combined with effcient LDPC code decoders.

## List-Based Detection and Selection of Access Points in Cell-Free Massive MIMO Networks

- **ID**: arxiv:2304.04159v1
- **Type**: preprint
- **Published**: 2023-04-09
- **Authors**: T. Ssettumba, L. T. N. Landau, R. C. de Lamare
- **PDF**: https://arxiv.org/pdf/2304.04159v1
- **Abstract**: This paper proposes a cell-free massive multiple-input multiple-output (CF-mMIMO) architecture with joint list-based detection with soft interference cancelation (soft-IC) and access points (APs) selection. In particular, we derive a new closed-form expression for the minimum mean-square error receive filter while taking the uplink transmit powers and APs selection into account. This is achieved by optimizing the receive combining vector by minimizing the mean square error between the detected symbol estimate and transmitted symbol, after canceling the multi-user interference (MUI). By using low-density parity check (LDPC) codes, an iterative detection and decoding (IDD) scheme based on a message passing is devised. In order to perform joint detection at the central processing unit (CPU), the access points locally estimate the channel and send their received sample data to the CPU via the front haul links. In order to enhance the system's bit error rate performance, the detected symbols are iteratively exchanged between the joint detector and the LDPC decoder in log likelihood ratio form. Furthermore, we draw insights into the derived detector as the number of IDD iterations increase. Finally, the proposed list detector is compared with existing detection techniques.
