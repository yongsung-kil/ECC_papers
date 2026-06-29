# IEEE Xplore — 2008-05 (1차선별 통과)


## Lowering the Error Floor of Optimized Short-Block-Length LDPC-Coded OFDM via Spreading

- **Status**: ✅
- **Reason**: 단블록 LDPC error floor 저감 + girth conditioning + 코드 최적화(E). NAND 짧은코드에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4357432
- **Type**: journal
- **Published**: May 2008
- **Authors**: Ali Serener, Balasubramaniam Natarajan, Don M. Gruenbacher
- **PDF**: https://ieeexplore.ieee.org/document/4357432
- **Abstract**: In this paper, short-block-length low-density parity-check (LDPC) codes are optimized and introduced, along with Walsh-Hadamard spreading, to orthogonal frequency-division multiplexing (OFDM) systems. Prior research has shown that lowering the threshold associated with LDPC codes results in higher error floors. The error floor becomes more pronounced for short-block-length LDPC codes that have been proposed for many wireless standards. In this paper, we show that the use of spreading along with code optimization and girth conditioning not only improves the performance but also lowers the error floor for short-length LDPC codes. Density evolution and differential evolution methods are used during the optimization phase of the codes for the frequency-uncorrelated Rayleigh fading channel. Performance results are obtained for extended irregular repeat-accumulate codes and progressive edge-growth algorithm generated codes. Next, the performances of LDPC-coded OFDM and spread OFDM systems in correlated Rayleigh fading channels are presented. A channel statistic, namely the number of faded bits per OFDM symbol, is theoretically derived, and it is demonstrated that the distribution of this channel statistic can be used to determine how close the correlated channel performance is going to be to that of the uncorrelated fading channel.

## Optimal Overlapped Message Passing Decoding of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC overlapped message passing 디코더 HW 아키텍처(FPGA, 병렬)+coset 구성(D/E). NAND 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4479869
- **Type**: journal
- **Published**: May 2008
- **Authors**: Yongmei Dai, Zhiyuan Yan, Ning Chen
- **PDF**: https://ieeexplore.ieee.org/document/4479869
- **Abstract**: Efficient hardware implementation of low-density parity-check (LDPC) codes is of great interest since LDPC codes are being considered for a wide range of applications. Recently, overlapped message passing (OMP) decoding has been proposed to improve the throughput and hardware utilization efficiency (HUE) of decoder architectures for LDPC codes. In this paper, we first study the scheduling for the OMP decoding of LDPC codes, and show that maximizing the throughput gain amounts to minimizing the intra- and inter-iteration waiting times. We then focus on the OMP decoding of quasi-cyclic (QC) LDPC codes. We propose a partly parallel OMP decoder architecture and implement it using FPGA. For any QC LDPC code, our OMP decoder achieves the maximum throughput gain and HUE due to overlapping, hence has higher throughput and HUE than previously proposed OMP decoders while maintaining the same hardware requirements. We also show that the maximum throughput gain and HUE achieved by our OMP decoder are ultimately determined by the given code. Thus, we propose a coset-based construction method, which results in QC LDPC codes that allow our optimal OMP decoder to achieve higher throughput and HUE.

## Generalized Combining Method for Design of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: E: CRT 일반화 QC-LDPC 구성법, 6-cycle 저감·성능 개선, 바이너리 코드설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4524251
- **Type**: journal
- **Published**: May 2008
- **Authors**: Yuanhua Liu, Xinmei Wang, Ruwei Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/4524251
- **Abstract**: A generalization of the Chinese Remainder Theorem (CRT) combining method is proposed to design much more and better quasi-cyclic (QC) LDPC codes when the parity check matrices of the component codes are given. It can design a much larger class of QC-LDPC codes with similar performance by loosening the condition for determining the intermediate parameters. By permuting the block rows of the parity check matrices of the component codes, a lot of QC-LDPC codes with much less 6-cycles and better performance can be designed. At a BER of 10-6 some QC-LDPC codes designed by the generalized combining method outperform those designed by the CRT combining method by 0.5 dB.

## Efficient Difference-based Decoding Implementations of LDPC Codes

- **Status**: ✅
- **Reason**: C: difference-based SPA 디코더 구현으로 복잡도·지연 저감, 바이너리 LDPC BP에 그대로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4524248
- **Type**: journal
- **Published**: May 2008
- **Authors**: Wu Zhanji, Peng Mugen, Wang Wenbo +1
- **PDF**: https://ieeexplore.ieee.org/document/4524248
- **Abstract**: Efficient implementations of the sum-product algorithm (SPA) for decoding low-density parity-check (LDPC) codes using difference-based messages between bit nodes and check nodes are presented. As for the updates of check nodes, reduced- complexity derivatives are also put forward. As compared with the traditional Log-Likelihood-Ratio(LLR)-based decoding implementations, the proposed method has much lower complexity and latency, while it has no obvious loss of the error performance.

## A 1-Gb/s flexible LDPC decoder supporting multiple code rates and block lengths

- **Status**: ✅
- **Reason**: D: 다중 코드율·블록길이 지원 유연 LDPC 디코더 HW(Benes network, 0.18um), NAND ECC HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4560109
- **Type**: journal
- **Published**: May 2008
- **Authors**: Jong-Yeol Lee, Hye-Jin Ryu
- **PDF**: https://ieeexplore.ieee.org/document/4560109
- **Abstract**: This paper propose a new flexible low-density parity-check (LDPC) decoding architecture that can be dynamically reconfigured according to a parity-check matrix which changes as code rate or block length varies. Since the LDPC codes are adopted in standards such as DVB-S2, IEEE 802.1 In and IEEE 802.16e and each standard allows various code rates and block lengths, an LDPC decoder architecture that could support multiple code rates and code block lengths is needed. The proposed architecture employs Benes network to implement configurable interconnection network. In the proposed architecture the number of levels and the delay of the interconnection network is reduced by using broadcasting technique which transmits reduced messages to save the complexity of the interconnection network. The number of processing units in the proposed partially parallel architecture is determined by investigating the relation between hardware complexity and throughput. By applying pipelining to the processing units, decoding throughput is increased. To verify the proposed architecture, a flexible LDPC decoder is implemented using a 0.18 mum CMOS process. The decoder occupies an area of 16.261 mm and runs correctly at the frequency of 212 MHz resulting in 1 Gbps decoding throughput.

## On the implementation of bus-based architectures for LDPC decoding

- **Status**: ✅
- **Reason**: D: LDPC 디코더 인터커넥션 복잡도 감소 버스 기반 아키텍처, HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4556288
- **Type**: conference
- **Published**: 7-9 May 20
- **Authors**: G. Aggouras, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/4556288
- **Abstract**: Three families of architectures for LDPC decoding are presented in this paper, aiming at the reduction of the interconnection complexity dominant in an LDPC decoder. The proposed architectures explore tradeoffs between the interconnection complexity, delay, and decoding performance. A graph-based technique is introduced that allows the formation of groups of calculations, such that inter-group communication is minimized. The formed groups are subsequently mapped onto processor units. Furthermore, a technique to achieve full utilization of processors under a constraint on the number of busses is discussed and a corresponding architecture, as well as a hybrid of the multi-bus and grouped-calculations architecture.

## Impact of roundoff errors in LDPC decoding

- **Status**: ✅
- **Reason**: C/D: LDPC 메시지패싱 디코딩 유한 워드길이 라운드오프 영향 분석, LLR 양자화 관련 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4556289
- **Type**: conference
- **Published**: 7-9 May 20
- **Authors**: N. Kanistras, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/4556289
- **Abstract**: In this paper the impact of roundoff mechanisms on the performance of message-passing LDPC decoding is studied. It is shown that finite word length introduces error by means of two mechanisms, each of which is analyzed. The impact and behavior of the two mechanisms are clarified by experimental results.

## A probabilistic algorithm for finding the minimum-size stopping sets of LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC stopping set 최소크기 탐색 확률 알고리즘, error floor/유한길이 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4578623
- **Type**: conference
- **Published**: 5-9 May 20
- **Authors**: Masanori Hirotomo, Yoshiho Konishi, Masakatu Morii
- **PDF**: https://ieeexplore.ieee.org/document/4578623
- **Abstract**: On the binary erasure channel, the performance of LDPC codes decoded by iterative algorithms is dominated by small-size stopping sets, especially minimal stopping sets. In this paper, we propose a probabilistic algorithm for computing the minimum size of stopping sets of LDPC codes. In this algorithm, we generate efficiently small-size stopping sets by using the relation between small-size stopping sets and low-weight codewords. In numerical experiments, we could compute the minimum size of stopping sets of LDPC codes of length about 500, 1000 and 5000 with high reliability, and could find smaller stopping sets than that found by conventional methods.

## LDPC codes which can correct three errors under iterative decoding

- **Status**: ✅
- **Reason**: column-weight-3 LDPC가 Gallager A 반복디코딩에서 3-error 정정하는 구성 조건+기법 제시(E 코드설계, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4578696
- **Type**: conference
- **Published**: 5-9 May 20
- **Authors**: Shashi Kiran Chilappagari, Anantha Raman Krishnan, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/4578696
- **Abstract**: In this paper, we provide necessary and sufficient conditions for a column-weight-three LDPC code to correct all patterns up to three errors when decoded using Gallager A algorithm. We then provide a construction technique which results in a code satisfying the above conditions. We also provide numerical assessment of code performance via simulation results.

## A new criterion to compare different LDPC codes for hardware implementation

- **Status**: ✅
- **Reason**: LDPC 코드 HW 구현 복잡도/효율 비교 지표(Goodness Number) 제안; HW 설계 의사결정에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4564647
- **Type**: conference
- **Published**: 4-7 May 20
- **Authors**: Amir Hosein Harati Nejad Torbati, Mahmoud Ahmadian Attari, Amir Moosavinia
- **PDF**: https://ieeexplore.ieee.org/document/4564647
- **Abstract**: In this paper we propose a new combinational criterion as a mean for comparison between different LDPC codes in terms of complexity and efficiency. The main idea behind the proposed criterion is to merge different aspects of a code to a unique number. We will show that the new criterion, named “Goodness Number” or GN, is applicable, and in some circumstances it is preferred to other criteria such as complexity and error probability criteria and at the same time it maintains computational simplicity.

## Dynamic-list joint detection and decoding of LDPC-coded V-BLAST systems

- **Status**: ✅
- **Reason**: LDPC-coded V-BLAST의 동적 리스트 결합검출/디코딩 soft info 개선; BP에 이식 가능한 디코더 기법(C) 여지로 애매시 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4564829
- **Type**: conference
- **Published**: 4-7 May 20
- **Authors**: Meng-Ying Tsai, Shahram Yousefi
- **PDF**: https://ieeexplore.ieee.org/document/4564829
- **Abstract**: Soft iterative detection and decoding techniques have been shown to be able to achieve near-capacity performance in multiple antenna systems. To obtain the optimal soft information by marginalizing over the entire observation space is intractable; and it is not clear what the best way to obtain the suboptimal soft information is. In this talk, an improved scheme is proposed which can be adapted to various list-type detectors and provide superior performance.

## Design of Low-Complexity Well-Structured LDPC Codes Based on Iterative-Filled Approach

- **Status**: ✅
- **Reason**: HW지향 구조적 LDPC 신규 구성(IF-LDPC), 선형 인코딩+부분병렬 디코딩(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4566298
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Wei Zhang, Guangxi Zhu, Li Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/4566298
- **Abstract**: Low density parity check codes are a popular class of linear block codes for forward error correction in communication channels. Recent years have seen a lot of work towards the hardware-oriented constructions for LDPC codes which have comparable error-correcting performance to random construction codes. This paper proposes a novel method called Iterative-filled (IF) to construct LDPC codes and a new kind of LDPC codes named IF-LDPC codes. Based on the properties of the method proved in this paper, we present a design of regular and quasi-regular IF-LDPC encoders which have linear encoding complexity, simple construction, low memory requirement and are suitable for partly parallel decoding. These advantages make them easy to hardware implementation. The IF-LDPC codes exhibit good performance in computer simulations and some even better than MacKay codes.

## Research of Low-Density Parity-Check Decode Algorithms for Digital Subscriber Lines

- **Status**: ✅
- **Reason**: 바이너리 LDPC BP 저복잡도 개선 디코더 알고리즘(C) 제시
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4566277
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Xing-Yu Xiang, Jun Xie
- **PDF**: https://ieeexplore.ieee.org/document/4566277
- **Abstract**: Decoding algorithm complexity influences the application of low-density parity-check (LDPC) codes. This article investigated the Belief-Propagation and improved decode algorithms for a subclass of binary LDPC that can be encoded linearly. Through the comparison of decoding performance, a low complexity one with good performance is preferred. It is shown that the incorporation of LDPC coding techniques into Digital Subscriber Line (DSL) systems appears to be possible.

## LDPC Coded Wireless Networks with Adaptive Spectral Efficiency

- **Status**: ✅
- **Reason**: 다중율 LDPC 모부행렬 설계+범용 FPGA 인코더(1.2Gbps), D/E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4536709
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Zhiyong He, Sebastien Roy
- **PDF**: https://ieeexplore.ieee.org/document/4536709
- **Abstract**: Low-density parity-check (LDPC) codes offer a very powerful error correction technique which allows data transmission in wireless networks at rates near the channel capacity with arbitrarily low probability of error. In this paper, we design a class of linearly encodable LDPC codes with adaptive code rates, i.e. the code rate can be adapted according to channel conditions to maximize the total capacity. Since a unique mother parity check matrix is used to construct LDPC codes with several code rates, the great advantage of the proposed codes is that a single universal encoder (decoder) is adequate to encode (decode) multi-rate codes, which makes it possible to efficiently implement multi-rate LDPC codes in a subscriber station. The implementation results into field programmable gate array (FPGA) devices indicate that a universal layered encoder for LDPC codes with 9 code rates is capable of reaching a throughput above 1.2 Gigabit per second by using 138 exclusive- OR gates and a master clock of 100 MHz. By combining multilevel modulation with the designed multi-rate LDPC codes, a transmission scheme with adaptive spectral efficiency is proposed. The simulation results indicate that the schemes with a spectral efficiency of 1, 2, 3, 4, and 5 bits/symbol/Hz can achieve extremely reliable transmission in a Rayleigh fading channel at signal-to-noise ratios (SNR) per bit of 5, 6, 10, 14, and 16 dB, respectively.

## Efficient Encoder Design of the Q-LDPC Codes

- **Status**: ✅
- **Reason**: N-queens 순환치환 Q행렬 기반 sparse H행렬 구성+4/6-cycle 제거 인코더, E 코드설계
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4536705
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Li Peng, Guangxi Zhu
- **PDF**: https://ieeexplore.ieee.org/document/4536705
- **Abstract**: This paper have developed farther the method of constructing sparse parity-check matrix (H-matrix) with determinate systemic structure as well as designing practice recursive encoding algorithm of the low-density parity-check (LDPC) codes. It discovers that the LDPC codes based on the circulant-shifted permutation Q-matrix created by N-queens searching algorithm perform better than them based on permutation identity matrix when Hd -matrix in H =[ Hp Hd] was constructed by using circulant-shifted permutation Q-matrix and identity matrix, respectively. It presents a simple and efficient algorithm of constructing Hd matrix without 4-cycle and 6-cycle. The presented LDPC encoders require O(M) operation (M is check-bit size). They are rate-compatible and length- compatible encoders that can cover a very wide range of rate from 0.1 to 0.9 and length including any positive integer from 20 to infinity except prime number and multiple prime numbers. The presented LDPC codes with moderate length and 1/2 rate can achieve reliable performance - 10-5~10-6 bit error rate (BER) - on an additive white Gaussian noise (AWGN) channel with signal-to-noise ratio (SNR) Eb/No about 1.42 dB1.

## Hardware Design of Quasi-Cyclic Low-Density Parity-Check Encoder Based on a Novel RC-Scheme

- **Status**: ✅
- **Reason**: 신규 RC-scheme 기반 QC-LDPC 인코더 HW 설계(병렬/직렬, 전력절감) - 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4536824
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Liang Chen, Shijun Yan, Wenjun Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/4536824
- **Abstract**: In this paper, quasi-cyclic low-density parity-check (QC- LDPC) codes are applied to a novel rate-compatible (RC) scheme for multimedia transmission. To ensure that the RC codes over the entire range of rates can be decoded by a single decoder, modified array codes in a lower triangular form are employed as the mother codes. The constructed rate-compatible QC-LDPC codes based on our novel RC- scheme can also be encoded by a single encoder. Hardware design of QC-LDPC encoder for this RC-scheme is proposed in detail. The hardware complexity is determined by the lowest-rate code for serial encoding and by the mother code for parallel encoding. Part of hardware units is disabled in certain cases to reduce power consumption.

## High Throughput Parallel Decoder Design for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC-CC 노드차원 병렬 디코더+코드-디코더 결합설계(Gb/s)로 C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4536707
- **Type**: conference
- **Published**: 26-28 May 
- **Authors**: Zhengang Chen, Stephen Bates, Witold Krzymien
- **PDF**: https://ieeexplore.ieee.org/document/4536707
- **Abstract**: LDPC convolutional code (LDPC-CC) decoders are composed of processors, making them parallel in the iteration dimension. However, for time-varying LDPC-CCs, each individual processor is serial in the node dimension, hindering the throughput increase for such decoders. We propose a joint code-decoder design, which generates architecture-aware LDPC- CCs of good performance, as well as an LDPC-CC decoder architecture parallel in the node dimension. Without increase in the memory bits used, the parallel decoder can achieve throughputs at the level of Gb/s with small parallelization factors.

## Construction of quasi-cyclic LDPC codes from one-coincidence sequences

- **Status**: ✅
- **Reason**: one-coincidence sequence 기반 QC-LDPC 신규 구성, 4-cycle 제거(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4657719
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Chun-Ming Huang, Chao-Chin Yang, Jen-Fa Huang
- **PDF**: https://ieeexplore.ieee.org/document/4657719
- **Abstract**: In this paper, we proposed a new method for constructing quasi-cyclic low-density parity-check (QC-LDPC) codes based on circulant permutation matrices via the one-coincidence sequences. The main advantage is that QC-LDPC codes with a variety of block lengths and rates can be easily constructed with no cycles of length four or less. Simulation results show that the proposed QC-LDPC codes perform slight better than the random regular LDPC codes for short to moderate block lengths and have almost the same performance as Sridara- Fuja-Tanner codes.

## A fast and efficient encoding structure for QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC용 PIPO 인코더 신규 HW 구조(D), 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4657717
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Zhixing Yang, Qiuliang Xie, Kewu Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/4657717
- **Abstract**: Parallel-Input Parallel-Output (PIPO) structure for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes is proposed in this paper to implement a faster and more efficient QC-LDPC encoder than that based on conventional Serial-Input Parallel-Output (SIPO) or Parallel-Input Serial-Output (PISO) structure. An encoding architecture based on the proposed PIPO structure for multi-rate QC-LDPC codes employed by the Chinese Digital Television Terrestrial Broadcasting (DTTB) standard is also presented and discussed.

## High-throughput LDPC decoding architecture

- **Status**: ✅
- **Reason**: QC-LDPC용 normalized UMP-BP 파이프라인 부분병렬 FPGA 디코더 아키텍처, NAND 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4657992
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Zhixing Yang, Nan Jiang, Kewu Peng +1
- **PDF**: https://ieeexplore.ieee.org/document/4657992
- **Abstract**: A high-throughput decoding architecture for quasi-cyclic (QC) low-density parity-check (LDPC) codes is developed in this paper. Regular pipelined schemes of the partially parallel decoder, which are adaptable to various decoding requirements, are derived to simplify the design and implementation. Utilizing normalized uniformly most powerful (UMP) belief propagation (BP) algorithm, pipelined partially parallel decoders for (7493, 3048), (7493, 4572) and (7493, 6096) LDPC codes are implemented on FPGA. Synthesis results show that, with 30 decoding iterations, the decoders for these codes archive throughputs of 108, 172 and 237 Mbps at the maximum operating frequencies of 151, 158 and 163 MHz respectively. The proposed architecture increases decoding throughput by more than four times compared with that of the traditional decoder.

## Efficient encoding of cycle codes on graphs with large girths

- **Status**: ✅
- **Reason**: 큰 girth cycle code(column-weight-2 LDPC) 효율적 인코딩 신규 구조(E), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4657716
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Weigang Chen, Liuguo Yin, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/4657716
- **Abstract**: Low-density parity-check (LDPC) codes of column weight two, also called cycle codes, can be constructed based on connected simple graphs. In this paper, efficiently encodable cycle codes and modified Repeat-Accumulate codes based on Hamiltonian graphs with large girths are devised. Specifically, the Hamiltonian property of the graphs is exploited to obtain efficient encoder structures and a concise description for the Hamiltonian graph named LCF (Lederberg-Coxeter-Frucht) notation is used to reduce the complexity of the encoders, especially the storage requirement. Then, using the Hamiltonian property and the LCF notation, structured cycle codes with large girths and low encoding complexity are devised. Simulation results also reveal that the proposed structured codes exhibit better performance compared with other structured cycle codes.

## A Class of Low-Density Parity-Check Convolutional Codes Based on Difference Families

- **Status**: ✅
- **Reason**: difference family 기반 LDPC convolutional 부호, girth>=10 보장 신규 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533264
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Y.-C. He, C. Cardinal, D. Haccoun
- **PDF**: https://ieeexplore.ieee.org/document/4533264
- **Abstract**: An algebraic construction for a class of low-density parity-check (LDPC) convolutional codes is presented on the basis of difference families associated with the code generator matrix. It can be shown that these codes have girth of at least 10 on the Tanner graph which is independent of either the size of the code generator matrix or the minimum Hamming distance of the codes. The code construction guarantees the independence of the messages exchanged in the belief propagation decoding process during two successive decoding iterations. Computer simulations show that over the additive white Gaussian noise channel, the best error performance of these codes at moderate signal-to- noise ratio values is practically obtained using only three to five iterations.

## Multilevel Structured Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: Multilevel Structured QC-LDPC 신규 구조 코드설계, 저장량 감소·HW친화 인코딩/디코딩(E/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533132
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: N. Bonello, S. Chen, L. Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/4533132
- **Abstract**: Low-density parity-check (LDPC) codes are typically characterized by a relatively high-complexity description, since a considerable amount of memory is required in order to store their code description, which can be represented either by the connections of the edges in their Tanner graph or by the non-zero entries in their parity-check matrix (PCM). This problem becomes more pronounced for pseudo-random LDPC codes, where literally each non-zero entry of their PCM has to be enumerated, and stored in a look-up table. Therefore, they become inadequate for employment in memory- constrained transceivers. Motivated by this, we are proposing a novel family of structured LDPC codes, termed as Multilevel Structured (MLS) LDPC codes, which benefit from reduced storage requirements, hardware-friendly implementations as well as from low-complexity encoding and decoding. Our simulation results demonstrate that these advantages accrue without any compromise in their attainable Bit Error Ratio (BER) performance, when compared to their previously proposed more complex counterparts of the same code-length. In particular, we characterize a half-rate quasi-cyclic (QC) MLS LDPC code having a block length of 8064 that can be uniquely and unambiguously described by as few as 144 edges, despite exhibiting an identical BER performance over both Additive White Gaussian Noise (AWGN) and uncorrelated Rayleigh (UR) channels, when compared to a pseudorandom construction, which requires the enumeration of a significantly higher number of 24,192 edges.

## Lower-Complexity Layered Belief-Propagation Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: Zigzag LBP 신규 순차 스케줄(고율 소-중블록 QC-LDPC 부분병렬 디코딩), 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533261
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Y.-M. Chang, A. I. V. Casado, M.-C. F. Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/4533261
- **Abstract**: The design of LDPC decoders with low complexity, high throughput, and good performance is a critical task. A well-known strategy is to design structured codes such as quasi- cyclic LDPC (QC-LDPC) that allow partially-parallel decoders. Sequential schedules, such as Layered Belief-Propagation (LBP), converge faster than the traditional flooding schedule while allowing parallel decoding of QC-LDPC codes. In this paper, we propose a novel low-complexity sequential schedule called Zigzag LBP (Z-LBP). Current LBP schedules do not allow partially- parallel architectures in the regime of high-rate codes with small- to-medium blocklengths. Our proposed algorithm can still be implemented in a partially-parallel manner in this regime. Z-LBP provides the same benefits as LBP including faster convergence speed and lower frame error rates than flooding.

## Graph-Matched LDPC Codes for Partial-Response Channels

- **Status**: ✅
- **Reason**: RA기반 LDPC graph-matched 부호, 저복잡 디코딩 그래프 신규 구성(E/C) — 바이너리 LDPC 설계 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533432
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: A. P. Legg, B. F. Uchoa-Filho
- **PDF**: https://ieeexplore.ieee.org/document/4533432
- **Abstract**: In this paper, we propose an LDPC coding scheme based on repeat-accumulate (RA) codes for partial-response (PR) channels. We modify the original RA encoder in such a way that there exists a one-to-one relationship between a sequence called the D-codeword (which is not the transmitted codeword but contains the information bits) and the noiseless received sequence at the output of the PR channel. A consequence of this is that the graph used for decoding the D-codeword, which is different from the encoder graph, is of low complexity. Moreover, with the appropriate modification of the RA encoder, the graph used for decoding is the same of any PR channel, which makes sense calling these codes graph-matched. The simplicity of the decoder, resulting from the "binary" interference removal (precoding) and the linear, as opposed to quadratic, complexity of the encoder make the proposed scheme attractive. For a code rate R = 3641/4096 = 0.89 and for the PR4 channel, an LDPC code has been designed and a simulated coding gain of about 5 dB for a bit error rate less than 10-5 was obtained.

## A Modification to Weighted Bit-Flipping Decoding Algorithm for LDPC Codes Based on Reliability Adjustment

- **Status**: ✅
- **Reason**: weighted bit-flipping 신뢰도 조정 변형, 바이너리 LDPC용 신규 디코더 개선으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533262
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: D. Qian, M. Jiang, C. Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/4533262
- **Abstract**: In this paper, a modification to the weighted bit- flipping (WBF) decoding algorithm for low-density parity-check (LDPC) codes is proposed. This modification, based on the adjustment in reliabilities of the check sums during iterative decoding, can be applied to various WBF algorithms. Our studies show that the modification can be achieved with a small increase in complexity, but leads to an appealing improvement in error performance.

## Concatenated eIRA Codes for Tamed Frequency Modulation

- **Status**: ✅
- **Reason**: eIRA(LDPC계) 코딩, Tanner 그래프 short-loop 제거 코드설계(E) 언급 — TFM 종속이나 사이클제거 기법 가능성, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4533398
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: J. Bao, Y. Zhan, J. Lu
- **PDF**: https://ieeexplore.ieee.org/document/4533398
- **Abstract**: A new scheme of the extended irregular repeat- accumulate (eIRA) coded tamed frequency modulation (TFM) for deep space communications is introduced in this paper. It is mainly based on the optimal concatenation of the eIRA code and the continuous phase encoder (CPE) decomposed from TFM. In order to obtain good performance of the eIRA coded TFM, the main principle of our scheme is to jointly optimize the concatenation by eliminating the short loops in the Tanner graph of the eIRA code and the coding part of TFM and to jointly decode between them. Then our scheme without interleaving and the contrast scheme with interleaving are simulated in an additive white Gaussian noise (AWGN) channel which is typical in deep space communications. Simulation results have shown that our scheme can obtain lower complexity and less decoding delay (due to the reduction of interleaving) at the cost of just 0.1-0.15 dB performance loss when compared to the scheme with interleaving given bit-error-ratio (BER) of 10 5. Therefore, our scheme can be used to implement the coded TFM system for deep space communications with good performance and low complexity.

## Multi-mode message passing switch networks applied for QC-LDPC decoder

- **Status**: ✅
- **Reason**: QC-LDPC 디코더용 message passing switch network/permutation 구조, NAND 디코더 HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4541527
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Chih-Hao Liu, Chien-Ching Lin, Hsie-Chia Chang +2
- **PDF**: https://ieeexplore.ieee.org/document/4541527
- **Abstract**: The multi-mode message passing switch networks for multi-standard QC-LDPC decoder are presented. An enhanced self-routing switch network with only one barrel shifter permutation structure and a shifter-based two-way duplicated switch network are proposed to support 19 and 3 different sub-matrices defined in IEEE 802.16e and IEEE 802.11n. These proposed switch networks can route the decoding message in parallel by different sizes without signal congestion. The enhanced self-routing switch network can switch the messages at different expansion factors with the lowest hardware complexity. Under the condition of a smaller expansion factor, the decoder throughput can be enhanced from the two-way duplicated switch network by increasing the parallelism. In the 130nm CMOS synthesis result, the proposed enhanced self-routing and the two-way duplicated switch network gate counts are 21.9k and 37.4k at 384MHz operation frequency.

## VLSI decoding architecture with improved convergence speed and reduced decoding latency for irregular LDPC codes in WiMAX

- **Status**: ✅
- **Reason**: QC-LDPC용 VLSI 디코더 아키텍처+수렴속도 개선 디코딩 알고리즘, NAND LDPC 디코더로 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4541469
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Yeong-Luh Ueng, Chung-Jay Yang, Zong-Cheng Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/4541469
- **Abstract**: In this paper, we modify a previously proposed decoding algorithm and propose a VLSI architecture to decode the quasi-cyclic low-density parity-check (QC-LDPC) code C used in the IEEE 802.16e standard. The modified decoding algorithm sequentially decodes a plurality of block codes for which its code length is much smaller than that of C. The proposed decoder can achieve a faster speed of convergence, lower decoding latency, higher throughput, and lower number of memory access as compared to the decoders using conventional turbo decoding message passing (TDMP) based on similar hardware complexity.

## Area efficient controller design of barrel shifters for reconfigurable LDPC decoders

- **Status**: ✅
- **Reason**: reconfigurable LDPC 디코더용 barrel shifter/Benes 컨트롤러 신규 설계, permutation network HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4541399
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Daesun Oh, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4541399
- **Abstract**: In this paper, we propose an efficient controller design of barrel shifter for reconfigurable low-density parity-check (LDPC) decoders, whcih leads to significant reduction in hardware complexity. Since the structured LDPC codes for the most modern wireless communication systems include multiple code rates, various block lengths, and different sizes of submatrices, a reconfigurable LDPC decoder is desirable and the barrel shifter needs to be programmable. Even though the Benes network can be optimized for the barrel shifting networks of reconfigurable LDPC decoder, it is not trivial to generate all the control signals for numerous 2×2 switches on-the-fly. A novel simplified algorithm capable of generating all the control signals is proposed using the properties that both the full-size Benes network can be broken into two half-size Benes networks and the barrel shifters needed in the structured LDPC decoders require only cyclic shifts. The proposed algorithm can be easily implemented with a small numbers of gates. Compared with the direct implementation using a dedicated look-up table, the proposed algorithm achieves a significant hardware reduction in implementing a reconfigurable LDPC decoder.

## Structured LDPC codes with low error floor based on PEG tanner graphs

- **Status**: ✅
- **Reason**: PEG 기반 구조적 Tanner graph 구성+error floor 저감, HW지향 LDPC 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4541800
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Yi-Kai Lin, Chih-Lung Chen, Yen-Chin Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/4541800
- **Abstract**: Progressive edge-growth (PEG) algorithm was proven to be a simple and effective approach to design good LDPC codes. However, the Tanner graph constructed by PEG algorithm is non-structured which leads the positions of 1’s of the corresponding parity check matrix fully random. In this paper, we propose a general method based on PEG algorithm to construct structured Tanner graphs. These hardware-oriented LDPC codes can reduce the VLSI implementation complexity. Similar to PEG method, our CP-PEG approach can be used to construct both regular and irregular Tanner graphs with flexible parameters. For the consideration of encoding complexity and error floor, the modifications of proposed algorithm are discussed. Simulation results show that our codes, in terms of bit error rate (BER) or packet error rate (PER), outperform other PEG-based LDPC codes and are better than the codes in IEEE 802.16e.

## Switching activity reducing layered decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: switching activity 저감 layered decoding+부분병렬 디코더 아키텍처, 저전력 디코더 HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4541471
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Shu-Cheng Chou, Mong-Kai Ku, Chia-Yu Lin
- **PDF**: https://ieeexplore.ieee.org/document/4541471
- **Abstract**: A switching activity reducing decoding algorithm for Low-Density Parity Check (LDPC) codes is proposed. Our modified horizontal layered decoding algorithm reduces active node switching activities to lower LDPC decoder power consumption. Layered nodes are periodically refreshed to minimize coding gain degradation. A low hardware overhead partially parallel LDPC decoder architecture is also described. Simulation results show that our algorithm reduces the number of LDPC decoder operations up to 62.5% compared to the original layered decoding and improves the original vertical layered Lazy Scheduling much with little performance loss.

## Adaptive quantization in min-sum based irregular LDPC decoder

- **Status**: ✅
- **Reason**: min-sum 적응적 양자화/유한정밀도 LLR 최적 워드길이 설계, NAND LDPC 디코더 양자화로 직접 이식(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4541473
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Sangmin Kim, Gerald E. Sobelman, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/4541473
- **Abstract**: In this paper, we present adaptive quantization schemes in the normalized min-sum decoding algorithm considering scaling effects to improve the performance of irregular low-density parity-check (LDPC) decoder for WirelessMAN (IEEE 802.16e) applications. We discuss the finite precision effects on the performance of irregular LDPC codes and develop optimal finite word lengths of variables over an SNR. For floating point simulation, it is known that in the normalized min-sum or offset min-sum algorithms the performance of a min-sum based decoder is not sensitive to scaling in the log-likelihood ratio (LLR) values. However, when considering the finite precision for hardware implementation, the scaling affects the dynamic range of the LLR values. The proposed adaptive quantization approach provides the optimal performance in selecting suitable input LLR values to the decoder as far as the tradeoffs between error performance and hardware complexity are concerned.

## Enhanced delta-based layered decoding of WiMAX QC-LDPC codes

- **Status**: ✅
- **Reason**: delta-based layered decoding+offset min-sum, 파이프라인 깊이 고려한 처리순서 배치 절차로 임의 QC-LDPC에 적용 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4541470
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Tzu-Chieh Kuo, Alan N. Willson
- **PDF**: https://ieeexplore.ieee.org/document/4541470
- **Abstract**: Rovini, et al., have proposed a delta-based layered decoding algorithm to mitigate the latency constraint imposed by the layered decoding algorithm on QC-LDPC codes whose adjacent block rows overlap. We apply their algorithm and the low-complexity offset-based Min-Sum check equation to the decoding of the codes specified in WiMAX. The performance is simulated for two representative hardware pipeline depths, showing a maximal 0.13-dB performance loss, with respect to the ideal latency-free layered decoding algorithm, for a block error rate of 10−2 in 15 iterations and a pipeline depth of eight. We further develop a systematic procedure to arrange the processing order of the block rows and block columns of a given QC parity check matrix, reducing the aforementioned performance loss to 0.03 dB at no extra hardware cost. The procedure can be applied to any QC-LDPC codes for any given pipeline depths.

## Binary de Bruijn interconnection network for a flexible LDPC/turbo decoder

- **Status**: ✅
- **Reason**: de Bruijn 온칩 인터커넥션 네트워크 LDPC 디코더 HW 아키텍처, 병렬 라우팅 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4541363
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Hazem Moussa, Amer Baghdadi, Michel Jezequel
- **PDF**: https://ieeexplore.ieee.org/document/4541363
- **Abstract**: This paper proposes a novel on-chip interconnection network adapted to a flexible multiprocessor LDPC/turbo decoder and based on the de Bruijn network. The main characteristics of this network -including its logarithmic diameter, scalable aggregate bandwidth, and optimized routing technique- allow it to efficiently support the communication-intensive nature of the two decoding techniques. We present a detailed hardware implementation of the routers and the network interfaces as well as the packet format and the routing algorithm. In order to evaluate the performance of the proposed network, a generic RTL VHDL description has been developed and synthesized with ST CMOS 0.18 μm technology. The flexibility and the scalability of this on-chip communication network enable it to be used in the emerging multi-code applications and standards. In addition, the results obtained for a 16-processor network demonstrate a major aggregate bandwidth of 296 Gbps with a relative small area of 3.56 mm2.

## A 223Mbps FPGA Implementation of (10240, 5120) Irregular Structured Low Density Parity Check Decoder

- **Status**: ✅
- **Reason**: 비정규 구조화 LDPC 디코더 FPGA 구현, semi-parallel 아키텍처/critical path 최적화 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4525724
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Wang Wenjun, Wu Xiaoguang, Zhu Xiaoxuan +2
- **PDF**: https://ieeexplore.ieee.org/document/4525724
- **Abstract**: This paper presents a high speed decoder architecture for irregular structured low density parity check (LDPC) codes and its field programmable gate array (FPGA) implementation. Algorithm transformation and architectural level optimizations are employed to reduce the critical path. The enhanced semi-parallel architecture is easily scalable and reconfigurable for larger block sizes and can be well suited for achieving high decoding throughput. Based on the proposed architecture, a (10240, 5120) irregular structured LDPC decoder is implemented on Xilinx FPGA Virtex-4 VLX80, the FPGA implementation results show that the irregular LDPC decoder can achieve a maximum (information data) decoding throughput of 223 Mbps at 18 iterations.

## LDPC Code Construction and Iterative Receiver Techniques for Channels with Phase Noise

- **Status**: ✅
- **Reason**: 위상잡음에 강건한 바이너리 LDPC 신규 코드 구성기법 — E(코드설계) 이식 검토(애매하므로 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4526186
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Sridhar Karuppasami, William G. Cowley, Steven S. Pietrobon
- **PDF**: https://ieeexplore.ieee.org/document/4526186
- **Abstract**: We present a novel LDPC code construction technique and an algorithm that assists phase estimation on sub- blocks to provide a near-coherent performance on channels with a large phase noise. Sub-blocks are very small observation intervals on the received vector over which phase estimation techniques are applied to provide ambiguous phase estimates. Iterative decoding on LDPC codes are affected by these phase ambiguities on sub- blocks. In our earlier work, we resolved this sub-block phase ambiguity at the start of the decoding based on a set of check nodes called 'local check nodes (LCN)' that are connected locally within the sub-blocks. Due to the poor signal-to-noise ratio at the start of decoding, a large number of LCNs were required to provide a reliable phase ambiguity. In this paper, we show that random LDPC codes can be constructed such that their decoding is not affected by the presence of sub-block phase ambiguities. Because of this, the signal quality is improved due to the code convergence and hence requires significantly less local check nodes to resolve phase ambiguity. We present performance results for a binary LDPC code with BPSK modulation. They show that with little loss, the receiver could tolerate a Wiener phase noise of up to 3deg standard deviation per symbol.

## Linear-Time Encodable Rate-Compatible Punctured LDPC Codes with Low Error Floors

- **Status**: ✅
- **Reason**: E2RC punctured LDPC의 error floor 해소를 위한 구조 수정 제시, 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4525720
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Seungmoon Song, Daesung Hwang, Sunglock Seo +1
- **PDF**: https://ieeexplore.ieee.org/document/4525720
- **Abstract**: We consider efficiently encodable rate-compatible (E2RC) punctured low-density parity-check (LDPC) codes and show that punctured LDPC codes of the E2RC structure have high error floors at their base code rates. Efficient type-II hybrid Automatic Repeat reQuest (ARQ) protocols are possible with punctured LDPC codes since punctured LDPC codes can support a wide range of code rates with incremental redundancy transmissions. However, such high error floors may result in excessive number of retransmission requests and end up with poor efficiency of hybrid ARQ protocols. We find that the problem of the E2RC structure stems from dispersive right degree distribution and high maximum right degree which is an indispensable element in the E2RC structure. In this paper, we propose a modification to E2RC structure which eliminates the error-floor problem without compromising any of important advantages of the E2RC structure such as linear-time encodability and good bit-error rate (BER) performance over a wide range of code rates. Our claims will be verified with BER and frame error rate (FER) simulation results.

## Long Length LDPC Code Construction and the Corresponding Decoder Implementation with Adjustable Parallelism

- **Status**: ✅
- **Reason**: 구조화 H-QC LDPC 구성으로 error floor 저감, 조정 가능 병렬성 디코더 아키텍처 — 코드설계(E)+HW(D), NAND 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4525855
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Chia-Yu Lin, Mong-Kai Ku, Yi-Hsing Chien
- **PDF**: https://ieeexplore.ieee.org/document/4525855
- **Abstract**: In this paper, we propose a class of implementation friendly structured LDPC codes with low error floors. The proposed codes exhibit no apparent error floors as compared with quasi-cyclic (QC) LDPC codes at long block lengths. A modified progressive edge-growth algorithm is used to construct the hierarchical quasi-cyclic (H-QC) LDPC codes. By adding implementation-friendly two-level hierarchy with limited types of second-level submatrices in the parity check matrix, coding performance is improved substantially over QC codes. We also show that QC-based decoder architecture can be easily applied to H-QC decoders to achieve better coding gain and higher throughput performance. Moreover, the degree of decoding parallelism and code length can be adjusted by changing the H-QC code construction parameters.

## A New Approach for the Construction of Powerful LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: 직교성 구조 기반 LDPC convolutional code 대수적 구성, girth>=10 달성 — 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4525805
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Christian Cardinal, Yu-Cheng He, David Haccoun
- **PDF**: https://ieeexplore.ieee.org/document/4525805
- **Abstract**: A novel approach for the algebraic construction of low-density parity-check (LDPC) convolutional codes is presented. It is based on the orthogonality structures of the codes. The proposed code construction leads to a girth of at least 10 in the Tanner graph. The error performance of these codes compares favorably with the usual LDPC convolutional codes, especially at low signal-to-noise ratio rang...

## Link between Sum-Product and Gradient Projection Decoding of LDPC Codes: An Intermediate Algorithm

- **Status**: ✅
- **Reason**: Sum-product과 gradient projection 연결한 중간 디코딩 알고리즘, 복잡도 저감 개선 디코더 제안 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4525856
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Maxime Beaudonnet, C. Kasparis, Barry G. Evans
- **PDF**: https://ieeexplore.ieee.org/document/4525856
- **Abstract**: This paper investigates the connection between the classical sum-product (SP) decoder for low density parity check (LDPC) codes and the recently proposed gradient projection (GP) decoding scheme presented in (Kasparis and Evans, 2007). A graphical model for GP is exhibited based on which we derive an intermediate algorithm which establishes a bridge between graphical based algorithms (SP and variants) and an optimization based algorithm (GP). A more practical decoding algorithm with improved performance and reduced complexity is also proposed. A complexity analysis is provided and performance are studied through Monte-Carlo simulations.
