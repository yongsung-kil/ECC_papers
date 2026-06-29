# arXiv — 2010-04


## On Distance Properties of Quasi-Cyclic Protograph-Based LDPC Codes

- **Status**: ❌
- **Reason**: QC 프로토그래프 부호의 최소거리 상한(이론 bound) 분석으로 deep-space AR4JA 대상, 떼어낼 디코더/HW/신규 구성 기법 없음
- **ID**: arxiv:1004.5429v1
- **Type**: preprint
- **Published**: 2010-04-30
- **Authors**: Brian K. Butler, Paul H. Siegel
- **PDF**: https://arxiv.org/pdf/1004.5429v1
- **Abstract**: Recent work has shown that properly designed protograph-based LDPC codes may have minimum distance linearly increasing with block length. This notion rests on ensemble arguments over all possible expansions of the base protograph. When implementation complexity is considered, the expansion is typically chosen to be quite orderly. For example, protograph expansion by cyclically shifting connections creates a quasi-cyclic (QC) code. Other recent work has provided upper bounds on the minimum distance of QC codes. In this paper, these bounds are expanded upon to cover puncturing and tightened in several specific cases. We then evaluate our upper bounds for the most prominent protograph code thus far, one proposed for deep-space usage in the CCSDS experimental standard, the code known as AR4JA.

## Optimized puncturing distributions for irregular non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 펑처링 분포 최적화로 기준상 비이진 LDPC는 제외
- **ID**: arxiv:1004.5216v2
- **Type**: preprint
- **Published**: 2010-04-29
- **Authors**: Matteo Gorgoglione, Valentin Savin, David Declercq
- **PDF**: https://arxiv.org/pdf/1004.5216v2
- **Abstract**: In this paper we design non-uniform bit-wise puncturing distributions for irregular non-binary LDPC (NB-LDPC) codes. The puncturing distributions are optimized by minimizing the decoding threshold of the punctured LDPC code, the threshold being computed with a Monte-Carlo implementation of Density Evolution. First, we show that Density Evolution computed with Monte-Carlo simulations provides accurate (very close) and precise (small variance) estimates of NB-LDPC code ensemble thresholds. Based on the proposed method, we analyze several puncturing distributions for regular and semi-regular codes, obtained either by clustering punctured bits, or spreading them over the symbol-nodes of the Tanner graph. Finally, optimized puncturing distributions for non-binary LDPC codes with small maximum degree are presented, which exhibit a gap between 0.2 and 0.5 dB to the channel capacity, for punctured rates varying from 0.5 to 0.9.

## Split-Extended LDPC codes for coded cooperation

- **Status**: ❌
- **Reason**: 릴레이 협력통신용 split-extend LDPC 코드 설계로 무선 협력 응용 특이적, NAND로 떼어낼 ECC 기법 없음
- **ID**: arxiv:1004.5214v1
- **Type**: preprint
- **Published**: 2010-04-29
- **Authors**: Valentin Savin
- **PDF**: https://arxiv.org/pdf/1004.5214v1
- **Abstract**: We propose a new code design that aims to distribute an LDPC code over a relay channel. It is based on a split-and-extend approach, which allows the relay to split the set of bits connected to some parity-check of the LDPC code into two or several subsets. Subsequently, the sums of bits within each subset are used in a repeat-accumulate manner in order to generate extra bits sent from the relay toward the destination. We show that the proposed design yields LDPC codes with enhanced correction capacity and can be advantageously applied to existing codes, which allows for addressing cooperation issues for evolving standards. Finally, we derive density evolution equations for the proposed design, and we show that Split-Extended LDPC codes can approach very closely the capacity of the Gaussian relay channel.

## Apologizing Comment on `Quantum Quasi-Cyclic Low-Density Parity-Check codes$\,$"

- **Status**: ❌
- **Reason**: 양자 QC-LDPC 구성에 대한 사과/정정 코멘트로 양자 EC 영역이며 신규 고전 바이너리 이식 기법 없음
- **ID**: arxiv:1004.4488v3
- **Type**: preprint
- **Published**: 2010-04-26
- **Authors**: Dazu Huang, Zhigang Chen, Xin Li +1
- **PDF**: https://arxiv.org/pdf/1004.4488v3
- **Abstract**: In our recent paper entitled "Quantum Quasi-Cyclic Low-Density Parity-Check codes" [ICIC 2009. LNCS 5754], it was claimed that some new quantum codes can be constructed via the CSS encoding/decoding approach with various lengths and rates. However, the further investigation shows that the proposed construction may steal some ideas from the paper entitled "Quantum Quasi-Cyclic LDPC codes" [quant-ph/0701020v2]. We feel that the apologizing point of the original protocol is that some results are almost similar to that of construction methods with algebraic combinatorics although we suggest the different approach for improving them. Also, there is a weak point of the original coding approach while considering the application of codes in imperfect channels.

## Capacity Achieving Low Density Parity Check Lattices

- **Status**: ❌
- **Reason**: LDPC 격자(lattice)의 capacity/sphere-bound 달성 이론 분석으로 순수 이론 bound, NAND ECC 디코더/구성 신규 기법 부재
- **ID**: arxiv:1004.1749v4
- **Type**: preprint
- **Published**: 2010-04-10
- **Authors**: Mohammad-Reza Sadeghi, Amin Sakzad
- **PDF**: https://arxiv.org/pdf/1004.1749v4
- **Abstract**: The concept and existence of sphere-bound-achieving and capacity-achieving lattices has been explained on AWGN channels by Forney. LDPC lattices, introduced by Sadeghi, perform very well under iterative decoding algorithm. In this work, we focus on an ensemble of regular LDPC lattices. We produce and investigate an ensemble of LDPC lattices with known properties. It is shown that these lattices are sphere-bound-achieving and capacity-achieving. As byproducts we find the minimum distance, coding gain, kissing number and an upper bound for probability of error for this special ensemble of regular LDPC lattices.
