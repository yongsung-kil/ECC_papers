# arXiv — 2018-03


## On LDPC Code Based Massive Random-Access Scheme for the Gaussian Multiple Access Channel

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.08377v1
- **Type**: preprint
- **Published**: 2018-03-22
- **Authors**: Luiza Medova, Anton Glebov, Pavel Rybin +1
- **PDF**: https://arxiv.org/pdf/1803.08377v1
- **Abstract**: This paper deals with the problem of massive random access for Gaussian multiple access channel (MAC). We continue to investigate the coding scheme for Gaussian MAC proposed by A. Vem et al in 2017. The proposed scheme consists of four parts: (i) the data transmission is partitioned into time slots; (ii) the data, transmitted in each slot, is split into two parts, the first one set an interleaver of the low-density parity-check (LDPC) type code and is encoded by spreading sequence or codewords that are designed to be decoded by compressed sensing type decoding; (iii) the another part of transmitted data is encoded by LDPC type code and decoded using a joint message passing decoding algorithm designed for the T-user binary input Gaussian MAC; (iv) users repeat their codeword in multiple slots. In this paper we are concentrated on the third part of considered scheme. We generalized the PEXIT charts to optimize the protograph of LDPC code for Gaussian MAC. The simulation results, obtained at the end of the paper, were analyzed and compared with obtained theoretical bounds and thresholds. Obtained simulation results shows that proposed LDPC code constructions have better performance under joint decoding algorithm over Gaussian MAC than LDPC codes considered by A. Vem et al in 2017, that leads to the better performance of overall transmission system.

## Efficient Search of QC-LDPC Codes with Girths 6 and 8 and Free of Elementary Trapping Sets with Small Size

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.08141v1
- **Type**: preprint
- **Published**: 2018-03-21
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi
- **PDF**: https://arxiv.org/pdf/1803.08141v1
- **Abstract**: One of the phenomena that influences significantly the performance of low-density parity-check codes is known as trapping sets. An $(a,b)$ elementary trapping set, or simply an ETS where $a$ is the size and $b$ is the number of degree-one check nodes and $\frac{b}{a}<1$, causes high decoding failure rate and exert a strong influence on the error floor. In this paper, we provide sufficient conditions for exponent matrices to have fully connected $(3,n)$-regular QC-LDPC codes with girths 6 and 8 whose Tanner graphs are free of small ETSs. Applying sufficient conditions on the exponent matrix to remove some 8-cycles results in removing all 4-cycles, 6-cycles as well as some small elementary trapping sets. For each girth we obtain a lower bound on the lifting degree and present exponent matrices with column weight three whose corresponding Tanner graph is free of certain ETSs.

## Iterative Turbo Receiver for LDPC-Coded MIMO Systems Based on Semi-definite Relaxation

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.05844v3
- **Type**: preprint
- **Published**: 2018-03-15
- **Authors**: Kun Wang, Zhi Ding
- **PDF**: https://arxiv.org/pdf/1803.05844v3
- **Abstract**: In this work, we develop a new iterative turbo receiver for LDPC-coded multi-antenna systems based on semidefinite relaxation (SDR). For a classical turbo receiver, forward error correction (FEC) code is only used at decoder. Nonetheless, by taking advantage of FEC code in the detection stage, our proposed SDR detector can output extrinsic information with much improved reliability to the decoder. We also propose a simplified SDR turbo receiver that solves only one SDR problem per codeword instead of solving multiple SDR problems in the iterative turbo processing. This scheme significantly reduces the time complexity of SDR turbo receiver, while the error performance remains similar as before. In fact, our simplified scheme is generic in the sense that it is applicable to any list-based iterative receivers.

## A Branch-Price-and-Cut Algorithm for Optimal Decoding of LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.04798v1
- **Type**: preprint
- **Published**: 2018-03-13
- **Authors**: Banu Kabakulak, Z. Caner Taşkın, Ali Emre Pusane
- **PDF**: https://arxiv.org/pdf/1803.04798v1
- **Abstract**: Channel coding aims to minimize errors that occur during the transmission of digital information from one place to another. Low-density parity-check (LDPC) codes can detect and correct transmission errors if one encodes the original information by adding redundant bits. In practice, heuristic iterative decoding algorithms are used to decode the received vector. However, these algorithms may fail to decode if the received vector contains multiple errors. We consider decoding the received vector with minimum error as an integer programming problem and propose a branch-and-price method for its solution. We improve the performance of our method by introducing heuristic feasible solutions and adding valid cuts to the mathematical formulation. Computational results reveal that our branch-price-and-cut algorithm significantly improves solvability of the problem compared to a commercial solver in high channel error rates. Our proposed algorithm can find higher quality solutions than commonly used iterative decoding heuristics.

## Finite Length Analysis of Irregular Repetition Slotted ALOHA in the Waterfall Region

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.01368v1
- **Type**: preprint
- **Published**: 2018-03-04
- **Authors**: Alexandre Graell i Amat, Gianluigi Liva
- **PDF**: https://arxiv.org/pdf/1803.01368v1
- **Abstract**: A finite length analysis is introduced for irregular repetition slotted ALOHA (IRSA) that enables to accurately estimate its performance in the moderate-to-high packet loss probability regime, i.e., in the so-called waterfall region. The analysis is tailored to the collision channel model, which enables mapping the description of the successive interference cancellation process onto the iterative erasure decoding of low-density parity-check codes. The analysis provides accurate estimates of the packet loss probability of IRSA in the waterfall region as demonstrated by Monte Carlo simulations.

## Low-Complexity Concatenated LDPC-Staircase Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:1803.01076v2
- **Type**: preprint
- **Published**: 2018-03-02
- **Authors**: Masoud Barakatain, Frank R. Kschischang
- **PDF**: https://arxiv.org/pdf/1803.01076v2
- **Abstract**: A low-complexity soft-decision concatenated FEC scheme, consisting of an inner LDPC code and an outer staircase code is proposed. The inner code is tasked with reducing the bit error probability below the outer-code threshold. The concatenated code is obtained by optimizing the degree distribution of the inner-code ensemble to minimize estimated data-flow, for various choices of outer staircase codes. A key feature that emerges from this optimization is that it pays to leave some inner codeword bits completely uncoded, thereby greatly reducing a significant portion of the decoding complexity. The trade-off between required SNR and decoding complexity of the designed codes is characterized by a Pareto frontier. Computer simulations of the resulting codes reveals that the net coding-gains of existing designs can be achieved with up to 71\% reduction in complexity. A hardware-friendly quasi-cyclic construction is given for the inner codes, which can realize an energy-efficient decoder implementation, and even further complexity reductions via a layered message-passing decoder schedule.
