# arXiv — 2006-02


## Bounds on the Threshold of Linear Programming Decoding

- **Status**: ❌
- **Reason**: LP 디코딩 임계값의 순수 이론 bound, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: arxiv:cs/0602087v1
- **Type**: preprint
- **Published**: 2006-02-26
- **Authors**: Pascal O. Vontobel, Ralf Koetter
- **PDF**: https://arxiv.org/pdf/cs/0602087v1
- **Abstract**: Whereas many results are known about thresholds for ensembles of low-density parity-check codes under message-passing iterative decoding, this is not the case for linear programming decoding. Towards closing this knowledge gap, this paper presents some bounds on the thresholds of low-density parity-check code ensembles under linear programming decoding.

## On the Block Error Probability of LP Decoding of LDPC Codes

- **Status**: ❌
- **Reason**: LP 디코딩 블록오류확률의 순수 이론 임계값 bound, 디코더/HW/구성 기여 없음
- **ID**: arxiv:cs/0602086v1
- **Type**: preprint
- **Published**: 2006-02-26
- **Authors**: Ralf Koetter, Pascal O. Vontobel
- **PDF**: https://arxiv.org/pdf/cs/0602086v1
- **Abstract**: In his thesis, Wiberg showed the existence of thresholds for families of regular low-density parity-check codes under min-sum algorithm decoding. He also derived analytic bounds on these thresholds. In this paper, we formulate similar results for linear programming decoding of regular low-density parity-check codes.

## Incremental Redundancy Cooperative Coding for Wireless Networks: Cooperative Diversity, Coding, and Transmission Energy Gain

- **Status**: ❌
- **Reason**: 무선 협력 통신 IR 코딩 스킴, LDPC는 powerful code 부수 언급일 뿐 떼어낼 디코더/코드설계 기법 없음
- **ID**: arxiv:cs/0602058v2
- **Type**: preprint
- **Published**: 2006-02-15
- **Authors**: Ruoheng Liu, Predrag Spasojevic, Emina Soljanin
- **PDF**: https://arxiv.org/pdf/cs/0602058v2
- **Abstract**: We study an incremental redundancy (IR) cooperative coding scheme for wireless networks. To exploit the spatial diversity benefit we propose a cluster-based collaborating strategy for a quasi-static Rayleigh fading channel model and based on a network geometric distance profile. Our scheme enhances the network performance by embedding an IR cooperative coding scheme into an existing noncooperative route. More precisely, for each hop, we form a collaborating cluster of M-1 nodes between the (hop) sender and the (hop) destination. The transmitted message is encoded using a mother code and partitioned into M blocks corresponding to the each of M slots. In the first slot, the (hop) sender broadcasts its information by transmitting the first block, and its helpers attempt to relay this message. In the remaining slots, the each of left-over M-1 blocks is sent either through a helper which has successfully decoded the message or directly by the (hop) sender where a dynamic schedule is based on the ACK-based feedback from the cluster. By employing powerful good codes (e.g., turbo codes, LDPC codes, and raptor codes) whose performance is characterized by a threshold behavior, our approach improves the reliability of a multi-hop routing through not only cooperation diversity benefit but also a coding advantage. The study of the diversity and the coding gain of the proposed scheme is based on a new simple threshold bound on the frame-error rate (FER) of maximum likelihood decoding. A average FER upper bound and its asymptotic (in large SNR) version are derived as a function of the average fading channel SNRs and the code threshold.

## Analysis of LDGM and compound codes for lossy compression and binning

- **Status**: ❌
- **Reason**: LDGM 손실 소스코딩(rate-distortion)·binning, 채널 ECC가 아닌 소스코딩이며 비-LDPC(LDGM) 압축
- **ID**: arxiv:cs/0602046v1
- **Type**: preprint
- **Published**: 2006-02-13
- **Authors**: Emin Martinian, Martin J. Wainwright
- **PDF**: https://arxiv.org/pdf/cs/0602046v1
- **Abstract**: Recent work has suggested that low-density generator matrix (LDGM) codes are likely to be effective for lossy source coding problems. We derive rigorous upper bounds on the effective rate-distortion function of LDGM codes for the binary symmetric source, showing that they quickly approach the rate-distortion function as the degree increases. We also compare and contrast the standard LDGM construction with a compound LDPC/LDGM construction introduced in our previous work, which provably saturates the rate-distortion bound with finite degrees. Moreover, this compound construction can be used to generate nested codes that are simultaneously good as source and channel codes, and are hence well-suited to source/channel coding with side information. The sparse and high-girth graphical structure of our constructions render them well-suited to message-passing encoding.

## Analysis of Belief Propagation for Non-Linear Problems: The Example of CDMA (or: How to Prove Tanaka's Formula)

- **Status**: ❌
- **Reason**: CDMA 다중사용자 검출 BP 분석, LDPC 앙상블 유사성만 언급, NAND LDPC에 이식할 디코더/코드설계 기법 없음
- **ID**: arxiv:cs/0602028v1
- **Type**: preprint
- **Published**: 2006-02-07
- **Authors**: Andrea Montanari, David Tse
- **PDF**: https://arxiv.org/pdf/cs/0602028v1
- **Abstract**: We consider the CDMA (code-division multiple-access) multi-user detection problem for binary signals and additive white gaussian noise. We propose a spreading sequences scheme based on random sparse signatures, and a detection algorithm based on belief propagation (BP) with linear time complexity. In the new scheme, each user conveys its power onto a finite number of chips l, in the large system limit.   We analyze the performances of BP detection and prove that they coincide with the ones of optimal (symbol MAP) detection in the l->\infty limit. In the same limit, we prove that the information capacity of the system converges to Tanaka's formula for random `dense' signatures, thus providing the first rigorous justification of this formula. Apart from being computationally convenient, the new scheme allows for optimization in close analogy with irregular low density parity check code ensembles.
