# IEEE Xplore — 2011-04 (1차선별 통과)


## Design of good QC-LDPC codes without small girth in the p-plane

- **Status**: ✅
- **Reason**: p-plane 기반 high-girth QC-LDPC 구성, short cycle 제거 필요충분조건 + stopping distance 향상 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6077622
- **Type**: journal
- **Published**: April 2011
- **Authors**: Lingjun Kong, Yang Xiao
- **PDF**: https://ieeexplore.ieee.org/document/6077622
- **Abstract**: A construction method based on the p-plane to design high-girth quasi-cyclic low-density parity-check (QC-LDPC) codes is proposed. Firstly the good points in every line of the p-plane can be ascertained through filtering the bad points, because the designed parity-check matrixes using these points have the short cycles in Tanner graph of codes. Then one of the best points from the residual good points of every line in the p-plane will be found, respectively. The optimal point is also singled out according to the bit error rate (BER) performance of the QC-LDPC codes at last. Explicit necessary and sufficient conditions for the QC-LDPC codes to have no short cycles are presented which are in favor of removing the bad points in the p-plane. Since preventing the short cycles also prevents the small stopping sets, the proposed construction method also leads to QC-LDPC codes with a higher stopping distance.

## A High-Throughput LDPC Decoder Architecture With Rate Compatibility

- **Status**: ✅
- **Reason**: rate-compatible QC-LDPC 고처리량 디코더 + puncturing + 병렬 layered decoding HW 아키텍처(65nm 구현) — 디코더 HW/코드설계 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5639060
- **Type**: journal
- **Published**: April 2011
- **Authors**: Kai Zhang, Xinming Huang, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/5639060
- **Abstract**: This paper presents a high-throughput decoder architecture for rate-compatible (RC) low-density parity-check (LDPC) codes which supports arbitrary code rates between the rate of mother code and 1. Puncturing techniques are applied to produce different rates for quasi-cyclic (QC) LDPC codes with dual-diagonal parity structure. Simulation results show that our selected puncturing scheme only introduces the BER performance degradation of less than 0.2 dB, compared with the dedicated codes for different rates specified in the IEEE 802.16e (WiMax) standard. Subsequently, parallel layered decoding architecture (PLDA) is employed for high-throughput decoder design. While the original PLDA is lack of rate flexibility, the problem is solved gracefully by incorporating the puncturing scheme. As a case study, an RC-LDPC decoder based on the rate-1/2 WiMax LDPC code is implemented in the CMOS 65-nm process. The clock frequency is 1.1 GHz, and the synthesis core area is 1.96 mm$^{2}$. The decoder can achieve an input throughput of 1.28 Gb/s at ten iterations and supports any rate between 1/2 and 1.

## Lowering the Error Floor of LDPC Codes Using Cyclic Liftings

- **Status**: ✅
- **Reason**: cyclic lifting으로 trapping set/short cycle 제거해 error floor 저감, QC-LDPC 생성 — 바이너리 코드설계(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5730557
- **Type**: journal
- **Published**: April 2011
- **Authors**: Reza Asvadi, Amir H. Banihashemi, Mahmoud Ahmadian-Attari
- **PDF**: https://ieeexplore.ieee.org/document/5730557
- **Abstract**: Cyclic liftings are proposed to lower the error floor of low-density parity-check (LDPC) codes. The liftings are designed to eliminate dominant trapping sets of the base code by removing the short cycles which are part of the trapping sets. We derive a necessary and sufficient condition for the cyclic permutations assigned to the edges of a cycle ξ of length l(ξ) in the base graph such that the inverse image of ξ in the lifted graph consists of only cycles of length strictly larger than l(ξ). The proposed method is universal in the sense that it can be applied to any LDPC code over any channel and for any iterative decoding algorithm. It also preserves important properties of the base code such as degree distributions, and in some cases, the code rate. The constructed codes are quasi-cyclic and thus attractive from a practical point of view. The proposed method is applied to both structured and random codes over the binary symmetric channel (BSC). The error floor improves consistently by increasing the lifting degree, and the results show significant improvements in the error floor compared to the base code, a random code of the same degree distribution and block length, and a random lifting of the same degree. Similar improvements are also observed when the codes designed for the BSC are applied to the additive white Gaussian noise (AWGN) channel.

## Noise Adaptive LDPC Decoding Using Particle Filtering

- **Status**: ✅
- **Reason**: 파티클필터로 시변 SNR 온라인 추정+BP 디코딩 결합 — 노이즈 적응 BP 디코더 기법, NAND 채널추정/LLR 적응으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5699415
- **Type**: journal
- **Published**: April 2011
- **Authors**: Shuang Wang, Lijuan Cui, Samuel Cheng +3
- **PDF**: https://ieeexplore.ieee.org/document/5699415
- **Abstract**: Belief propagation (BP) is a powerful algorithm to decode low-density parity check (LDPC) codes over additive white Gaussian noise (AWGN) channels. However, the traditional BP algorithm cannot adapt efficiently to the statistical change of SNR in an AWGN channel. This paper proposes an adaptive scheme that incorporates a particle filtering (PF) algorithm into the BP based LDPC decoding process. The proposed scheme is capable to perform online estimation of time-varying SNR at the bit-level and enhance the BP decoding performance simultaneously.

## Message-Wise Unequal Error Protection Based on Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: LDPC 기반 UEP — all-odd degree check node 구성 + 반복디코딩 중 unsatisfied check 검출 기법, 코드설계/디코더 이식 여지(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5715839
- **Type**: journal
- **Published**: April 2011
- **Authors**: Chen Gong, Guosen Yue, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/5715839
- **Abstract**: We propose a practical message-wise unequal error protection (UEP) scheme using low-density parity-check (LDPC) codes, where one or more special messages are more protected than other ordinary messages. In contrast to the information theoretic cavity coding scheme, which discards the codewords of ordinary messages near those of special messages, the proposed coding scheme performs codeword flipping to separate the codewords of special and ordinary messages without discarding any codewords. To better distinguish the original and flipped codewords, the LDPC codes with all-odd degree check nodes are employed. The decoder performs message type detection and codeword flipping detection based on the unsatisfied check nodes in iterative decoding. We provide performance analysis for both the message type detection and the codeword flipping detection. Moreover, we provide an asymptotic analysis on the detection error exponent to reveal the relationship between the proposed practical coding scheme and the information theoretically optimal cavity coding. Simulation results are provided to show that the proposed practical message-wise UEP schemes offer capacity-approaching protections to both types of messages as if only one type is transmitted.

## Graph-Based Decoding in the Presence of ISI

- **Status**: ✅
- **Reason**: ISI 채널 그래프 표현으로 등화+LDPC 메시지패싱/LP 결합 디코딩 — 디코더 기법(C) 이식 여지, 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5730584
- **Type**: journal
- **Published**: April 2011
- **Authors**: Mohammad H. Taghavi, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/5730584
- **Abstract**: We propose a new graph representation for ISI channels that can be used for combined equalization and decoding by linear programming (LP) or iterative message-passing (IMP) decoding algorithms. We derive this graph representation by linearizing the ML detection metric, which transforms the equalization problem into a classical decoding problem. We observe that the performance of LP and IMP decoding on this model are very similar in the uncoded case, while IMP decoding significantly outperforms LP decoding when low-density parity-check (LDPC) codes are used. In particular, in the absence of coding, for certain classes of channels, both LP and IMP algorithms always find the exact ML solution using the proposed graph representation, without complexity that is exponential in the size of the channel memory. This applies even to certain two-dimensional ISI channels. However, for some other channel impulse responses, both decoders have nondiminishing probability of failure as SNR increases. We provide analytical explanations for many of these observations. In addition, we study the error events of LP decoding in the uncoded case, and derive a measure that can be used to classify ISI channels in terms of the performance of the proposed detection scheme.

## Reduced complexity of decoding algorithm for irregular LDPC codes using Split Row method

- **Status**: ✅
- **Reason**: Split-Row LDPC 디코딩 기법 — 열처리 병렬화·행처리 단순화, NAND 디코더 HW에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5945639
- **Type**: conference
- **Published**: 7-9 April 
- **Authors**: R. El Alami, C. B. Gueye, M. Mrabti +2
- **PDF**: https://ieeexplore.ieee.org/document/5945639
- **Abstract**: A reduced complexity LDPC decoding method for regular LDPC code is extended to irregular LDPC codes; we present in this paper a full description of this method and its benefits for various row weight and length code word. The Split-Row method makes column processing parallelism easier to exploit and significantly simplifies row processors. Simulation results over an additive white Gaussian channel show that the error performance of high row-weight codes with Split-Row decoding is within 0.3–0.5 dB of the Min-Sum algorithm.

## Dynamic LDPC codes for nanoscale memory with varying fault arrival rates

- **Status**: ✅
- **Reason**: 나노메모리용 동적 LDPC(EG-LDPC) ECC, 동적 정정능력 조정; 메모리 ECC 코드설계(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5941439
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Shalini Ghosh, Patrick D. Lincoln
- **PDF**: https://ieeexplore.ieee.org/document/5941439
- **Abstract**: Modern state-of-the-art nanodevices exhibit remarkable electronic properties, but the current assembly techniques yield very high defect and fault rates. Static errors can be addressed at fabrication time by testing and reconfiguration, but soft errors are problematic since their arrival rates are expected to vary over the lifetime of a part. Usual designs consider error correcting codes that tolerate the maximum failure rate expected over the entire lifetime. In this paper, we propose using a special variant of low-density parity codes (LDPCs) - Euclidean Geometry LDPC (EG-LDPC) codes - to enable dynamic changes in the level of fault tolerance. EG-LDPC codes have high error correcting ability (for large words they can approach the optimal Shannon limit) and they are sparse (circuit implementation requires small fan-in). In addition, a special property of EG-LDPC codes enables us to dynamically adjust the error correcting capacity for improved system performance (e.g., lower power consumption) during periods of expected low fault arrival rate. We present a system architecture for nanomemory based on nanoPLA building blocks using EG-LDPCs, where the encoder/decoder could also have faults, and analyze the fault detection and correction capabilities considering dynamic fault tolerance.

## Unavoidable Cycles in Polynomial-Based Time-Invariant LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: QC 유래 LDPC convolutional의 unavoidable cycle/girth 분석과 양호 코드 설계 규칙 제시, 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5898001
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Hua Zhou, Norbert Goertz
- **PDF**: https://ieeexplore.ieee.org/document/5898001
- **Abstract**: Low-Density Parity-Check convolutional codes (LDPCccs) are very interesting for practical error-correction coding in wireless transmission as they have excellent performance and at the same time they allow for variable block size with low complexity encoding and decoding. As for all LDPC codes that are decoded by the sub-optimal (but highly efficient) Sum Product Algorithm, the cycles in the code graph are very important for the practical performance of the coding scheme. Time-invariant LDPCccs can be defined by a polynomial syndrome former (transposed parity-check matrix in polynomial form), that can be derived from corresponding Quasi-Cyclic (QC) LDPC block codes. Given the polynomial syndrome former with certain structures, unavoidable cycles with lengths ranging from 6 to 12 will be shown to exist.We provide some rules for designing good codes with respect to the shortest cycle in the code-graph, the girth of the code, which is a crucial parameter for its decoding performance.

## A low-complexity LDPC decoder architecture for WiMAX applications

- **Status**: ✅
- **Reason**: WiMAX LDPC 디코더 VLSI 아키텍처 - 통합 태스크 프로세서, modified layered decoding, QC 라우팅 네트워크 등 NAND LDPC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5783633
- **Type**: conference
- **Published**: 25-28 Apri
- **Authors**: Yu-Luen Wang, Yeong-Luh Ueng, Chian-Lien Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/5783633
- **Abstract**: In this paper, we present a low-complexity decoder architecture for WiMAX low-density parity-check (LDPC) codes based on a unified task processor. Memory access is accomplished through routing networks with fixed interconnections and memory address generators, which are quite simple due to the quasi-cyclic structure of the LDPC codes. In order to increase the decoding throughput, the check-node and variable-node operations are performed concurrently, and a modified layered decoding is employed. Based on this architecture, we implemented a full-mode WiMAX codec in a 90-nm process. This codec achieves an encoding (decoding) throughput of 960 Mb/s (240 Mb/s) and occupies an area of 0.679 mm2.

## A macro-layer level fully parallel layered LDPC decoder SOC for IEEE 802.15.3c application

- **Status**: ✅
- **Reason**: fully parallel layered LDPC 디코더 SOC - reusable message permutation network, frame-level pipeline 등 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5783634
- **Type**: conference
- **Published**: 25-28 Apri
- **Authors**: Zhixiang Chen, Xiao Peng, Xiongxin Zhao +4
- **PDF**: https://ieeexplore.ieee.org/document/5783634
- **Abstract**: In this paper, we propose an ultra high-throughput LDPC decoder SOC to fulfill the requirement of IEEE 802.15.3c standard. By implementing a macro-layer fully parallel architecture, our proposed decoder takes only 4 clock cycles to finish one layered decoding iteration. Interconnection complexity problem introduced by high-parallel decoding is nicely solved by proposed reusable message permutation networks utilizing the features of code PCM. Critical path is shortened by applying frame-level pipeline decoding. A 65 nm CMOS chip is fabricated to verify the proposed architecture. Measured at 1.2 V, 400 MHz and 10 iterations the proposed decoder achieves a data throughput 6.72 Gb/s and consumes a power 537.6 mW with an energy efficiency 8.0 pJ/bit·iter.

## A High-Efficiency LDPC Encoder with Optimized Backtracking Algorithm

- **Status**: ✅
- **Reason**: LDPC 인코더 backtracking 최적화(RU 기반)로 인코딩 복잡도 절감 — 코드설계/HW 이식 여지(E/D), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5931243
- **Type**: conference
- **Published**: 18-20 Apri
- **Authors**: Zhibin Zeng
- **PDF**: https://ieeexplore.ieee.org/document/5931243
- **Abstract**: A new LDPC encoder is presented for CMMB in this paper. The encoder uses based on RU method embodies high-efficiency by using the optimized backtracking algorithm. Simulation shows that this method decreases the complexity of encoding and calculation significantly. Implementation of the LDPC encoder for CMMB achieves more efficient encoding rate.

## A time-saving algorithm for constructing QC-LDPC codes based on PEG algorithm

- **Status**: ✅
- **Reason**: PEG 기반 고girth QC-LDPC 구성 + 단cycle 제거 신규 구성법(바이너리), 카테고리E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5768233
- **Type**: conference
- **Published**: 16-18 Apri
- **Authors**: Gong Ping, Huang Liqun
- **PDF**: https://ieeexplore.ieee.org/document/5768233
- **Abstract**: We propose a new algorithm based on PEG algorithm to construct high-girth quasi-cyclic low-density parity check (QC-LDPC) codes. Before our improved algorithm in introduction, we depict the general algorithm based on PEG algorithm to construct QC - LDPC code, if necessary to eliminate the short cycles, that would bring in cycles-search. When code length of basic matrix is not too long, the algorithm is feasible, but with the code length growth, cycles-search will bring large of calculation and time-consuming sharply. Therefore we put forward an improved method by using the specific relation of basic matrix rows to replace traditional cycles-search, effectively eliminates short cycles, and largely reduces the time complexity at the same time. Through the simulation analysis, the performance can also be comparable with random constructed LDPC codes.

## FPGA implementation of two very low complexity LDPC decoders

- **Status**: ✅
- **Reason**: 저복잡도 LDPC 디코더 FPGA 구현, SNR 불요 디코더 포함. 임의 패리티검사행렬 대응 디코더+HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5782617
- **Type**: conference
- **Published**: 13-15 Apri
- **Authors**: J. Castiñeira Moreira, M. Rabini, C. González +2
- **PDF**: https://ieeexplore.ieee.org/document/5782617
- **Abstract**: Low-Density Parity-Check (LDPC) codes are very efficient error control codes that are being considered as part of many next generation communication systems. In this paper FPGA implementations of two low complexity decoders are presented. These two implementations operate over any kind of parity check matrix, (including those randomly generated, structurally generated, either systematic or non systematic) and can be parametrically performed for any code rate k/n. The proposed implementations are both of very low complexity, because they operate using only sums, subtracts and look-up tables. One of these decoders offers the advantage of not requiring the knowledge of the signal-to-noise ratio of the channel, as it usually happens to most of decoders for LDPC codes.
