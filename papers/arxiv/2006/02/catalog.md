# arXiv — 2006-02


## Bounds on the Threshold of Linear Programming Decoding

- **ID**: arxiv:cs/0602087v1
- **Type**: preprint
- **Published**: 2006-02-26
- **Authors**: Pascal O. Vontobel, Ralf Koetter
- **PDF**: https://arxiv.org/pdf/cs/0602087v1
- **Abstract**: Whereas many results are known about thresholds for ensembles of low-density parity-check codes under message-passing iterative decoding, this is not the case for linear programming decoding. Towards closing this knowledge gap, this paper presents some bounds on the thresholds of low-density parity-check code ensembles under linear programming decoding.

## On the Block Error Probability of LP Decoding of LDPC Codes

- **ID**: arxiv:cs/0602086v1
- **Type**: preprint
- **Published**: 2006-02-26
- **Authors**: Ralf Koetter, Pascal O. Vontobel
- **PDF**: https://arxiv.org/pdf/cs/0602086v1
- **Abstract**: In his thesis, Wiberg showed the existence of thresholds for families of regular low-density parity-check codes under min-sum algorithm decoding. He also derived analytic bounds on these thresholds. In this paper, we formulate similar results for linear programming decoding of regular low-density parity-check codes.

## Low-Density Parity-Check Code with Fast Decoding Speed

- **ID**: arxiv:cs/0602081v1
- **Type**: preprint
- **Published**: 2006-02-23
- **Authors**: Xudong Ma, En-hui Yang
- **PDF**: https://arxiv.org/pdf/cs/0602081v1
- **Abstract**: Low-Density Parity-Check (LDPC) codes received much attention recently due to their capacity-approaching performance. The iterative message-passing algorithm is a widely adopted decoding algorithm for LDPC codes \cite{Kschischang01}. An important design issue for LDPC codes is designing codes with fast decoding speed while maintaining capacity-approaching performance. In another words, it is desirable that the code can be successfully decoded in few number of decoding iterations, at the same time, achieves a significant portion of the channel capacity. Despite of its importance, this design issue received little attention so far. In this paper, we address this design issue for the case of binary erasure channel.   We prove that density-efficient capacity-approaching LDPC codes satisfy a so called "flatness condition". We show an asymptotic approximation to the number of decoding iterations. Based on these facts, we propose an approximated optimization approach to finding the codes with good decoding speed. We further show that the optimal codes in the sense of decoding speed are "right-concentrated". That is, the degrees of check nodes concentrate around the average right degree.

## Incremental Redundancy Cooperative Coding for Wireless Networks: Cooperative Diversity, Coding, and Transmission Energy Gain

- **ID**: arxiv:cs/0602058v2
- **Type**: preprint
- **Published**: 2006-02-15
- **Authors**: Ruoheng Liu, Predrag Spasojevic, Emina Soljanin
- **PDF**: https://arxiv.org/pdf/cs/0602058v2
- **Abstract**: We study an incremental redundancy (IR) cooperative coding scheme for wireless networks. To exploit the spatial diversity benefit we propose a cluster-based collaborating strategy for a quasi-static Rayleigh fading channel model and based on a network geometric distance profile. Our scheme enhances the network performance by embedding an IR cooperative coding scheme into an existing noncooperative route. More precisely, for each hop, we form a collaborating cluster of M-1 nodes between the (hop) sender and the (hop) destination. The transmitted message is encoded using a mother code and partitioned into M blocks corresponding to the each of M slots. In the first slot, the (hop) sender broadcasts its information by transmitting the first block, and its helpers attempt to relay this message. In the remaining slots, the each of left-over M-1 blocks is sent either through a helper which has successfully decoded the message or directly by the (hop) sender where a dynamic schedule is based on the ACK-based feedback from the cluster. By employing powerful good codes (e.g., turbo codes, LDPC codes, and raptor codes) whose performance is characterized by a threshold behavior, our approach improves the reliability of a multi-hop routing through not only cooperation diversity benefit but also a coding advantage. The study of the diversity and the coding gain of the proposed scheme is based on a new simple threshold bound on the frame-error rate (FER) of maximum likelihood decoding. A average FER upper bound and its asymptotic (in large SNR) version are derived as a function of the average fading channel SNRs and the code threshold.

## Analysis of LDGM and compound codes for lossy compression and binning

- **ID**: arxiv:cs/0602046v1
- **Type**: preprint
- **Published**: 2006-02-13
- **Authors**: Emin Martinian, Martin J. Wainwright
- **PDF**: https://arxiv.org/pdf/cs/0602046v1
- **Abstract**: Recent work has suggested that low-density generator matrix (LDGM) codes are likely to be effective for lossy source coding problems. We derive rigorous upper bounds on the effective rate-distortion function of LDGM codes for the binary symmetric source, showing that they quickly approach the rate-distortion function as the degree increases. We also compare and contrast the standard LDGM construction with a compound LDPC/LDGM construction introduced in our previous work, which provably saturates the rate-distortion bound with finite degrees. Moreover, this compound construction can be used to generate nested codes that are simultaneously good as source and channel codes, and are hence well-suited to source/channel coding with side information. The sparse and high-girth graphical structure of our constructions render them well-suited to message-passing encoding.

## Analysis of Belief Propagation for Non-Linear Problems: The Example of CDMA (or: How to Prove Tanaka's Formula)

- **ID**: arxiv:cs/0602028v1
- **Type**: preprint
- **Published**: 2006-02-07
- **Authors**: Andrea Montanari, David Tse
- **PDF**: https://arxiv.org/pdf/cs/0602028v1
- **Abstract**: We consider the CDMA (code-division multiple-access) multi-user detection problem for binary signals and additive white gaussian noise. We propose a spreading sequences scheme based on random sparse signatures, and a detection algorithm based on belief propagation (BP) with linear time complexity. In the new scheme, each user conveys its power onto a finite number of chips l, in the large system limit.   We analyze the performances of BP detection and prove that they coincide with the ones of optimal (symbol MAP) detection in the l->\infty limit. In the same limit, we prove that the information capacity of the system converges to Tanaka's formula for random `dense' signatures, thus providing the first rigorous justification of this formula. Apart from being computationally convenient, the new scheme allows for optimization in close analogy with irregular low density parity check code ensembles.
