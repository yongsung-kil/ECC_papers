# arXiv — 2015-05


## Index Codes for the Gaussian Broadcast Channel using Quadrature Amplitude Modulation

- **Status**: ❌
- **Reason**: 인덱스 코드/QAM 변조 설계, LDPC는 off-the-shelf 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:1505.07283v1
- **Type**: preprint
- **Published**: 2015-05-27
- **Authors**: Lakshmi Natarajan, Yi Hong, Emanuele Viterbo
- **PDF**: https://arxiv.org/pdf/1505.07283v1
- **Abstract**: We propose index codes, based on multidimensional QAM constellations, for the Gaussian broadcast channel, where every receiver demands all the messages from the source. The efficiency with which an index code exploits receiver side information in this broadcast channel is characterised by a code design metric called "side information gain". The known index codes for this broadcast channel enjoy large side information gains, but do not encode all the source messages at the same rate, and do not admit message sizes that are powers of two. The index codes proposed in this letter, which are based on linear codes over integer rings, overcome both these drawbacks and yet provide large values of side information gain. With the aid of a computer search, we obtain QAM index codes for encoding up to 5 messages with message sizes 2^m, m <= 6. We also present the simulated performance of a new 16-QAM index code, concatenated with an off-the-shelf LDPC code, which is observed to operate within 4.3 dB of the broadcast channel capacity.

## Simple rate-adaptive LDPC coding for quantum key distribution

- **Status**: ❌
- **Reason**: QKD 정보조정(reconciliation)용 rate-adaptive LDPC — 채널 ECC가 아니고 떼어낼 디코더/HW 기법 없음, 원칙 제외
- **ID**: arxiv:1505.06423v1
- **Type**: preprint
- **Published**: 2015-05-24
- **Authors**: Mo Li, Chun-Mei Zhang, Zhen-Qiang Yin +3
- **PDF**: https://arxiv.org/pdf/1505.06423v1
- **Abstract**: Although quantum key distribution (QKD) comes from the development of quantum theory, the implementation of a practical QKD system does involve a lot of classical process, such as key reconciliation and privacy amplification, which is called post-processing. Post-processing has been a crucial element to high speed QKD systems, even the bottleneck of it because of its relatively high time consumption. Low density parity check (LDPC) is now becoming a promising approach of overcoming the bottleneck due to its good performance in processing throughput. In this article we propose and simulate an easily implemented but efficiently rate-adaptive LDPC coding approach of reconciliation, different from the previously proposed puncturing- and shortening-based approach. We also give a measure for choosing the optimal LDPC parameter for our rate-adaptive approach according to error rates.

## A 2.48Gb/s QC-LDPC Decoder Implementation on the NI USRP-2953R

- **Status**: ✅
- **Reason**: 표준 QC-LDPC지만 massively-parallel FPGA 디코더 아키텍처(D) 제시, NAND 디코더로 이식 가능
- **ID**: arxiv:1505.04339v1
- **Type**: preprint
- **Published**: 2015-05-16
- **Authors**: Swapnil Mhaske, David Uliana, Hojin Kee +3
- **PDF**: https://arxiv.org/pdf/1505.04339v1
- **Abstract**: The increasing data rates expected to be of the order of Gb/s for future wireless systems directly impact the throughput requirements of the modulation and coding subsystems of the physical layer. In an effort to design a suitable channel coding solution for 5G wireless systems, in this brief we present a massively-parallel 2.48Gb/s Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) decoder implementation operating at 200MHz on the NI USRP-2953R, on a single FPGA. The high-level description of the entire massively-parallel decoder was translated to a Hardware Description Language (HDL), namely VHDL, using the algorithmic compiler in the National Instruments LabVIEW Communication System Design Suite (CSDS) in approximately 2 minutes. This implementation not only demonstrates the scalability of our decoder architecture but also, the rapid prototyping capability of the LabVIEW CSDS tools. As per our knowledge, at the time of writing this paper, this is the fastest implementation of a standard compliant QC-LDPC decoder on a USRP using an algorithmic compiler.

## Optimization Design and Analysis of Systematic LT codes over AWGN Channel

- **Status**: ❌
- **Reason**: Systematic LT(fountain) 코드 degree distribution 최적화 — LDPC 비의존, fountain/erasure 제외
- **ID**: arxiv:1505.01944v1
- **Type**: preprint
- **Published**: 2015-05-08
- **Authors**: Shengkai Xu, Dazhuan Xu, Xiaofei Zhang +1
- **PDF**: https://arxiv.org/pdf/1505.01944v1
- **Abstract**: In this paper, we study systematic Luby Transform (SLT) codes over additive white Gaussian noise (AWGN) channel. We introduce the encoding scheme of SLT codes and give the bipartite graph for iterative belief propagation (BP) decoding algorithm. Similar to low-density parity-check codes, Gaussian approximation (GA) is applied to yield asymptotic performance of SLT codes. Recent work about SLT codes has been focused on providing better encoding and decoding algorithms and design of degree distributions. In our work, we propose a novel linear programming method to optimize the degree distribution. Simulation results show that the proposed distributions can provide better bit-error-ratio (BER) performance. Moreover, we analyze the lower bound of SLT codes and offer closed form expressions.
