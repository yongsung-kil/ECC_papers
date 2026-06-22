# arXiv — 2012-05


## LDPC for QKD Reconciliation

- **Status**: ❌
- **Reason**: QKD reconciliation에 표준 IEEE/ETSI 패리티검사 행렬을 그대로 적용, 신규 디코더·구성 기여 없음(정밀도 논의만), 원칙 제외
- **ID**: arxiv:1205.4977v2
- **Type**: preprint
- **Published**: 2012-05-22
- **Authors**: Alan Mink, Anastase Nakassis
- **PDF**: https://arxiv.org/pdf/1205.4977v2
- **Abstract**: We present the Low Density Parity Check (LDPC) forward error correction algorithm adapted for the Quantum Key Distribution (QKD) protocol in a form readily applied by developers. A sparse parity check matrix is required for the LDPC algorithm and we suggest using some that have been defined by the IEEE and ETSI standards organizations for use in various communication protocols. We evaluate the QKD performance of these various parity check matrices as a function of the quantum bit error rate. We also discuss the computational precision required for this LPDC algorithm. As QKD evolves towards deployment, complete algorithm descriptions and performance analysis, as we present, will be required.

## Graph-based Code Design for Quadratic-Gaussian Wyner-Ziv Problem with Arbitrary Side Information

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩(압축), reinforced BP는 source coding용 양자화 알고리즘, 채널 ECC가 아님
- **ID**: arxiv:1205.4332v2
- **Type**: preprint
- **Published**: 2012-05-19
- **Authors**: Yi-Peng Wei, Shih-Chun Lin, Yu-Hsiu Lin +1
- **PDF**: https://arxiv.org/pdf/1205.4332v2
- **Abstract**: Wyner-Ziv coding (WZC) is a compression technique using decoder side information, which is unknown at the encoder, to help the reconstruction. In this paper, we propose and implement a new WZC structure, called residual WZC, for the quadratic-Gaussian Wyner-Ziv problem where side information can be arbitrarily distributed. In our two-stage residual WZC, the source is quantized twice and the input of the second stage is the quantization error (residue) of the first stage. The codebook of the first stage quantizer must be simultaneously good for source and channel coding, since it also acts as a channel code at the decoder. Stemming from the non-ideal quantization at the encoder, a problem of channel decoding beyond capacity is identified and solved when we design the practical decoder. Moreover,by using the modified reinforced belief-propagation quantization algorithm, the low-density parity check code (LDPC), whose edge degree is optimized for channel coding, also performs well as a source code. We then implement the residual WZC by an LDPC and a low density generator matrix code (LDGM). The simulation results show that our practical construction approaches the Wyner-Ziv bound. Compared with previous works, our construction can offer more design lexibility in terms of distribution of side information and practical code rate selection.

## A New Ensemble of Rate-Compatible LDPC Codes

- **Status**: ❌
- **Reason**: Rateless Kite codes/rate-compatible LDPC for IR-HARQ wireless; binary LDPC but design is HARQ-application-specific, no NAND-transferable decoder/HW/construction technique
- **ID**: arxiv:1205.4070v1
- **Type**: preprint
- **Published**: 2012-05-18
- **Authors**: Kai Zhang, Xiao Ma, Shancheng Zhao +2
- **PDF**: https://arxiv.org/pdf/1205.4070v1
- **Abstract**: In this paper, we presented three approaches to improve the design of Kite codes (newly proposed rateless codes), resulting in an ensemble of rate-compatible   LDPC codes with code rates varying "continuously" from 0.1 to 0.9 for additive white Gaussian noise (AWGN) channels. The new ensemble rate-compatible LDPC codes can be constructed conveniently with an empirical formula. Simulation results show that, when applied to incremental redundancy hybrid automatic repeat request (IR-HARQ) system, the constructed codes (with higher order modulation) perform well in a wide range of signal-to-noise-ratios (SNRs).

## Spatially-Coupled Random Access on Graphs

- **Status**: ❌
- **Reason**: Spatial coupling applied to coded slotted ALOHA random access; LDPC over BEC is analogy/baseline, no transferable channel-ECC technique for NAND
- **ID**: arxiv:1205.3317v1
- **Type**: preprint
- **Published**: 2012-05-15
- **Authors**: Gianluigi Liva, Enrico Paolini, Michael Lentmaier +1
- **PDF**: https://arxiv.org/pdf/1205.3317v1
- **Abstract**: In this paper we investigate the effect of spatial coupling applied to the recently-proposed coded slotted ALOHA (CSA) random access protocol. Thanks to the bridge between the graphical model describing the iterative interference cancelation process of CSA over the random access frame and the erasure recovery process of low-density parity-check (LDPC) codes over the binary erasure channel (BEC), we propose an access protocol which is inspired by the convolutional LDPC code construction. The proposed protocol exploits the terminations of its graphical model to achieve the spatial coupling effect, attaining performance close to the theoretical limits of CSA. As for the convolutional LDPC code case, large iterative decoding thresholds are obtained by simply increasing the density of the graph. We show that the threshold saturation effect takes place by defining a suitable counterpart of the maximum-a-posteriori decoding threshold of spatially-coupled LDPC code ensembles. In the asymptotic setting, the proposed scheme allows sustaining a traffic close to 1 [packets/slot].

## Time-Varying Space-Only Codes for Coded MIMO

- **Status**: ❌
- **Reason**: MIMO space-only precoding/time-varying inner code; LDPC only as outer-code baseline in simulations, no extractable LDPC technique
- **ID**: arxiv:1205.0699v2
- **Type**: preprint
- **Published**: 2012-05-03
- **Authors**: Dieter Duyck, Sheng Yang, Fambirai Takawira +2
- **PDF**: https://arxiv.org/pdf/1205.0699v2
- **Abstract**: Multiple antenna (MIMO) devices are widely used to increase reliability and information bit rate. Optimal error rate performance (full diversity and large coding gain), for unknown channel state information at the transmitter and for maximal rate, can be achieved by approximately universal space-time codes, but comes at a price of large detection complexity, infeasible for most practical systems. We propose a new coded modulation paradigm: error-correction outer code with space-only but time-varying precoder (as inner code). We refer to the latter as Ergodic Mutual Information (EMI) code. The EMI code achieves the maximal multiplexing gain and full diversity is proved in terms of the outage probability. Contrary to most of the literature, our work is not based on the elegant but difficult classical algebraic MIMO theory. Instead, the relation between MIMO and parallel channels is exploited. The theoretical proof of full diversity is corroborated by means of numerical simulations for many MIMO scenarios, in terms of outage probability and word error rate of LDPC coded systems. The full-diversity and full-rate at low detection complexity comes at a price of a small coding gain loss for outer coding rates close to one, but this loss vanishes with decreasing coding rate.
