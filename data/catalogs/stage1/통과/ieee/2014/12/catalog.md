# IEEE Xplore — 2014-12 (1차선별 통과)


## An Efficient Multirate LDPC-CC Decoder With a Layered Decoding Algorithm for the IEEE 1901 Standard

- **Status**: ✅
- **Reason**: LDPC-CC 레이어드 디코더 + NMS 알고리즘 ASIC, 바이너리 디코더/HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6922500
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Yun Chen, Qichen Zhang, Di Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/6922500
- **Abstract**: An area-efficient multirate low-density parity-check convolutional code (LDPC-CC) decoder is presented in this brief. Using the layered decoding algorithm, the decoder achieves a better performance than the message-passing algorithm; the extrinsic-message storing is switched from variable node based to check node based. Then, using the normalized min-sum (NMS) algorithm, the extrinsic messages can be reduced to the first and second minimum absolute values, the position index of the first minimum absolute value, the signs of all extrinsic messages, and the product of all the signs. A memory-based application-specific integrated circuit architecture of the LDPC-CC decoder that supports these methods is proposed for the IEEE 1901 standard. Based on a SMIC 130-nm complementary metal–oxide–semiconductor process, a decoder that can support all the code rates of the LDPC-CCs defined in IEEE 1901 (1/2, 2/3, 3/4, 4/5) is fabricated and evaluated. The proposed decoder attains a maximum throughput of 300 Mb/s at a maximum operating frequency of 180 MHz. The core area is 3.55  $\hbox{mm}^{2}$ with ten processors. The average power consumption is 200.4 mW at code rate 4/5 and a frequency of 180 MHz, and the power efficiency is 66.8 pJ/bit/proc. The very large scale integration results show that the decoder is both memory and area efficient.

## On the Construction of Low Error Floor LDPC Codes on Rectangular Lattices

- **Status**: ✅
- **Reason**: small trapping set 제거로 low error floor QC-LDPC 구성 — 바이너리 LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6932472
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Xiongfei Tao, Pan Liu, Zhuoming Feng +1
- **PDF**: https://ieeexplore.ieee.org/document/6932472
- **Abstract**: In previous literature, arithmetically constrained slope sequences have been adopted for the construction of girth eight (3, k) LDPC codes on rectangular lattices. This method, however, creates a certain number of small trapping sets, which degrade overall performances. In this letter, an improved construction of a class of (3, k) LDPC codes on rectangular lattices is presented. Relevant constraints are derived to eliminate small trapping sets to improve performance in the error floor region. The check matrices of the proposed codes are introduced into quasi-cyclic structures, where experimental investigation shows favorable error rate performance over AWGN channels.

## Decoding LDPC Codes With Locally Maximum-Likelihood Binary Messages

- **Status**: ✅
- **Reason**: binary message 전달 저복잡도 LDPC 디코더(LMLBM), 양자화 LLR lookup table — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6940269
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Chris Winstead, Emmanuel Boutillon
- **PDF**: https://ieeexplore.ieee.org/document/6940269
- **Abstract**: A new low-complexity message passing algorithm is described for decoding low-density parity-check (LDPC) codes by exchanging binary messages. The algorithm computes the local maximum-likelihood binary message (LMLBM) at each symbol node, given the combination of local channel information and partial syndrome components from adjacent parity check nodes. When channel information is quantized, the locally ML messages are pre-computed and stored in a dynamic global lookup table. The proposed algorithm uses memoryless extrinsic messages so that density evolution thresholds can be directly computed. Thresholds are obtained for regular ensembles, predicting good performance on quantized binary-input additive white Gaussian noise (biAWGN) channels.

## Reliability-Based Iterative Decoding Algorithm for LDPC Codes With Low Variable-Node Degree

- **Status**: ✅
- **Reason**: 저변수노드차수용 신뢰도기반 반복 다수결논리 디코더(HE-RBID), 1비트 메시지 BP 변형 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6924716
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: J. M. Català-Pérez, F. García-Herrero, J. Valls +2
- **PDF**: https://ieeexplore.ieee.org/document/6924716
- **Abstract**: In this letter, a new reliability-based iterative majority-logic decoding (RBI-MLGD) algorithm that computes the extrinsic information of previous iterations of the variable node is proposed. This decoding algorithm is called historical-extrinsic reliability-based iterative decoder (HE-RBID) and improves the bit-error-rate performance of the previous RBI-MLGD. HE-RBID is particularly interesting for codes with a low degree of variable node, where traditional RBI-MLGD algorithms do not provide a good behavior. HE-RBID ensures a good performance without searching for the minimum at the check node and only by exchanging 1-bit messages between variable and check nodes.

## Threshold Saturation for Spatially Coupled LDPC and LDGM Codes on BMS Channels

- **Status**: ✅
- **Reason**: SC-LDPC/LDGM의 BMS 채널 threshold saturation 증명, 바이너리 SC-LDPC 코드설계(E) 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6912949
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Santhosh Kumar, Andrew J. Young, Nicolas Macris +1
- **PDF**: https://ieeexplore.ieee.org/document/6912949
- **Abstract**: Spatially-coupled low-density parity-check (LDPC) codes, which were first introduced as LDPC convolutional codes, have been shown to exhibit excellent performance under low-complexity belief-propagation decoding. This phenomenon is now termed threshold saturation via spatial coupling. Spatially-coupled codes have been successfully applied in numerous areas. In particular, it was proven that spatially-coupled regular LDPC codes universally achieve capacity over the class of binary memoryless symmetric (BMS) channels under belief-propagation decoding. Recently, potential functions have been used to simplify threshold saturation proofs for scalar and vector recursions. In this paper, potential functions are used to prove threshold saturation for irregular LDPC and low-density generator-matrix codes on BMS channels, extending the simplified proof technique to BMS channels. The corresponding potential functions are closely related to the average Bethe free entropy of the ensembles in the large-system limit. These functions also appear in statistical physics when the replica method is used to analyze optimal decoding.

## Error Floor Approximation for LDPC Codes in the AWGN Channel

- **Status**: ✅
- **Reason**: LDPC error floor를 trapping set 상태공간 모델·LLR saturation으로 예측 — 디코더 동작/구성 분석 기법 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6928457
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Brian K. Butler, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6928457
- **Abstract**: This paper addresses the prediction of error floors of low-density parity-check codes transmitted over the additive white Gaussian noise channel. Using a linear state-space model to estimate the behavior of the sum-product algorithm (SPA) decoder in the vicinity of trapping sets (TSs), we study the performance of the SPA decoder in the log-likelihood ratio (LLR) domain as a function of the LLR saturation level. When applied to several widely studied codes, the model accurately predicts a significant decrease in the error floor as the saturation level is allowed to increase. For nonsaturating decoders, however, we find that the state-space model breaks down after a small number of iterations due to the strong correlation of LLR messages. We then revisit Richardson's importance-sampling methodology for estimating error floors due to TSs when those floors are too low for Monte Carlo simulation. We propose modifications that account for the behavior of a nonsaturating decoder and present the resulting error floor estimates for the Margulis code. These estimates are much lower, significantly steeper, and more sensitive to iteration count than those previously reported.

## Variable LLR Scaling in Min-Sum Decoding for Irregular LDPC Codes

- **Status**: ✅
- **Reason**: min-sum LLR 가변 스케일링(GMI 기반 check node degree/iteration별) — 이식 가능 min-sum 변형 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6954486
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Yin Xu, Leszek Szczecinski, Bo Rong +4
- **PDF**: https://ieeexplore.ieee.org/document/6954486
- **Abstract**: Min-sum decoding is a low-complexity alternative to the so-called belief propagation and consists in simplification of the nonlinear operation on the log likelihood ratios (LLRs) in the check nodes. The resulting suboptimality may be tempered via appropriate scaling of the LLRs, e.g., the fixed optimal scaling in the normalized min-sum algorithm, and variable scaling algorithms gradually appearing in the literature. However, up to now, none of the papers studied variable scaling both as per iteration and as per different check node degree, due to the prohibitive complexity of multioptimization over space of too many parameters. In this paper, we propose a generalized mutual information (GMI) of LLRs as the criterion to search for the scaling factors for different check node degrees in every iteration in a 1-D thus low-complexity manner. This approach is first analyzed via density evolution, and in addition can be extended to practical LLRs based formulas via Monte Carlo tools to cope with the mismatch issue. Bit error rate simulation results on two low-density parity-check codes show that our proposed GMI metrics have a noticeable gain over the variable scaling schemes that appeared in the literature.

## Memristive Circuits for LDPC Decoding

- **Status**: ✅
- **Reason**: 멤리스터 CMOL 회로 LDPC 디코더 HW 아키텍처, 패리티검사 매핑·디코딩 회로 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6922162
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Jussi H. Poikonen, Eero Lehtonen, Mika Laiho +1
- **PDF**: https://ieeexplore.ieee.org/document/6922162
- **Abstract**: We present design principles for implementing decoders for low-density parity check codes in CMOL-type memristive circuits. The programmable nonvolatile connectivity enabled by the nanowire arrays in such circuits is used to map the parity check matrix of an LDPC code in the decoder, while decoding operations are realized by a cellular CMOS circuit structure. We perform detailed performance analysis and circuit simulations of example decoders, and estimate how CMOL and memristor characteristics such as the memristor OFF/ON resistance ratio, nanowire resistance, and the total capacitance of the nanowire array affect decoder specification and performance. We also analyze how variation in circuit characteristics and persistent device defects affect the decoders.

## Decoding algorithm of LDPC codes for cascaded BSC-AWGN channels

- **Status**: ✅
- **Reason**: BPM(BSC-AWGN 캐스케이드) 채널에서 crossover 확률을 반영해 check node 계산을 수정한 신규 디코더 기법(C). 스토리지 채널이며 NAND LLR 모델링에 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7041722
- **Type**: conference
- **Published**: 9-12 Dec. 
- **Authors**: Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/7041722
- **Abstract**: The written-in errors in bit patterned media (BPM) recording systems cause the erroneous bits during the writing process, leading to performance degradation. In previous works, the BPM read/write channel is modeled as a binary symmetric channel (BSC) with an additive white Gaussian noise (AWGN) channel or the cascaded BSC-AWGN channels. The initial channel information including the written-in errors probability has been proposed for low-density parity check (LDPC) decoder. However, the decoding algorithm remains the same as in the case of AWGN channels. In this work, we show that the crossover probability of BSC channels will affect the check node processing of LDPC codes. Therefore, we modify the check node computation that takes into account of the crossover probability of BSC channels. The simulation results show that the proposed LDPC decoder outperforms the ones with the conventional and modified likelihood function in terms of the bit error rate performance.

## Partial reverse concatenation for data storage

- **Status**: ✅
- **Reason**: 데이터 스토리지용 LDPC 기반 partial reverse concatenation — 스토리지 ECC 일반(B), 변조코드+ECC 결합 구성 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7041670
- **Type**: conference
- **Published**: 9-12 Dec. 
- **Authors**: Roy D. Cideciyan, Robert Hutchins, Thomas Mittelholzer +1
- **PDF**: https://ieeexplore.ieee.org/document/7041670
- **Abstract**: Coding schemes in data-storage systems use either conventional or reverse concatenation of a modulation code and an error-correction code. A new reverse concatenation scheme, called partial reverse concatenation, is introduced to reduce the coding overhead, improve the error-rate performance and simplify implementation. The proposed concatenation scheme uses an outer error-correction code, a high-rate modulation code and an inner error-correction code. The error-rate performance of partial reverse and conventional concatenation architectures are compared using measurements from tape drive channels. It is shown that, compared with a conventional concatenation scheme, an LDPC-code-based partial reverse concatenation scheme improves the signal-to-noise ratio that is required to achieve a bit-error rate of 1×10-20 by 1.8 dB.

## Low-power dual quantization-domain decoding for LDPC codes

- **Status**: ✅
- **Reason**: 3비트 dual quantization-domain LDPC 디코더, 비선형 매핑·저전력 min-sum 변형 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7037290
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Shadi Abu-Surra, Eran Pisek, Thomas Henige +1
- **PDF**: https://ieeexplore.ieee.org/document/7037290
- **Abstract**: In this paper we propose a new dual quantization-domain LDPC decoder, which requires only 3-bit messages between the check nodes and the variable nodes. To reduce complexity and save power, check nodes processing is entirely in the 3-bit domain. However, to avoid loss in performance, the variable nodes processing is in a higher bit precision domain. A non-linear mapping is used to map the messages from one quantization domain to the other. Simulations and hardware evaluation of the proposed decoder showed greater than 50% reduction in power consumption with only 0.1 dB (0.2 dB) loss in bit-error-performance when compared to a reference 5-bits scaled Min-Sum decoder over the AWGN (fading) channel.

## Modelling of the threshold voltage distributions of sub-20nm NAND flash memory

- **Status**: ✅
- **Reason**: sub-20nm NAND 임계전압 분포 모델링 — NAND 직접(A), LLR/ECC 설계 입력
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7037159
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Thomas Parnell, Nikolaos Papandreou, Thomas Mittelholzer +1
- **PDF**: https://ieeexplore.ieee.org/document/7037159
- **Abstract**: The proliferation of NAND flash memory in consumer devices has driven their aggressive cost reduction by continuous scaling to smaller technology nodes. However, this relentless cost per capacity improvement has diminished the reliability of flash memory to a degree that advanced signal processing and error correction are needed to enhance signal integrity in current flash-based systems. Accurate models of flash readback signals are necessary to properly design such advanced signal enhancement schemes. We propose a new parametric model of the flash readback signal based on fitting threshold voltage distributions from NAND flash devices. We show accurate fitting results for flash devices cycled up to 10 times longer than their nominal endurance specification, and provide simple expressions of the model parameters as a function of program/erase cycles. Finally, we also demonstrate that the proposed model can be used to capture effects such as programming errors, that occur in over-stressed flash devices.

## A hardware generator for factor graph applications

- **Status**: ✅
- **Reason**: FPGA HW generator framework for LDPC decoders (factor graph); portable HW architecture (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7032490
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: James Demma, Peter Athanas
- **PDF**: https://ieeexplore.ieee.org/document/7032490
- **Abstract**: A Factor Graph (FG-http://en.wikipedia.org/wiki/Factor_graph) is a structure used to And solutions to problems that can be represented as a Probabilistic Graphical Model (PGM). They consist of interconnected variable nodes and factor nodes, which iteratively compute and pass messages to each other. FG's can be applied to solve decoding of forward error correcting codes, Markov chains and Markov Random Fields, Kaiman Filtering, Fourier Transforms, and even some games such as Sudoku. In this paper, a framework is presented for rapid prototyping of hardware implementations of FG-based applications. The FG developer specifies aspects of the application, and the framework returns a design. A system of Python scripts and Verilog Hardware Description Language templates together are used to generate the HDL source code for the application. The generated designs are vendor/platform agnostic, but currently target the Xilinx Virtex-6-based ML605. The framework has so far been primarily applied to construct Low Density Parity Check (LDPC) decoders. The characteristics of a large basket of generated LDPC decoders, including contemporary 802.11η decoders, have been examined as a verification of the system and as a demonstration of its capabilities. As a further demonstration, the framework has been applied to construct a Sudoku solver.

## Memory efficient implementation of self-corrected min-sum LDPC decoder

- **Status**: ✅
- **Reason**: Memory-efficient FPGA self-corrected min-sum QC-LDPC decoder; portable decoder + HW technique (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7049980
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Oana Boncalo, Alexandria Amaricai, Valentin Savin
- **PDF**: https://ieeexplore.ieee.org/document/7049980
- **Abstract**: This paper proposes memory efficient FPGA implementations for layered quasi-cyclic (QC) LDPC decoders, based on the Self-Correcting Min-Sum (SCMS) algorithm. We address the problem of high memory overhead required by layered SCMS based decoders compared to conventional Min-Sum (MS), by proposing two improvements. These require changes in the flow/rule of the conventional SCMS algorithm, in order to avoid storing the signs and the erasure bits of the variable node messages. Three layered LDPC decoders with serial a-posteriori log likelihood ratios (AP-LLR) processing have been implemented: (1) conventional SCMS, (2) SCMS with no check node message signs storage, and (3) SCMS with neither check node message signs nor erasure bits storage. FPGA implementation results for WiMAX (1152, 2304) code show that the third architecture has a resource utilization with 17% less with respect to the one implementing conventional SCMS, and with 11% less than the second architecture. Furthermore, it presents a similar cost to conventional MS, while having a 0.5 dB better error correction capability.

## On the construction of LDPC convolutional code ensembles based on permuted circulant unit matrices

- **Status**: ✅
- **Reason**: LDPC convolutional code ensemble construction via permuted circulant matrices; portable binary code-design technique (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7050008
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Fotios Gioulekas, Constantinos Petrou, Athanasios Vgenis +1
- **PDF**: https://ieeexplore.ieee.org/document/7050008
- **Abstract**: In this paper, a construction methodology for ensembles of Low-Density Parity-Check Convolutional Codes (LDPC-CCs) based on permuted circulant unit matrices is proposed. The proposed method directly generates the syndrome former matrices according to specified code parameters and constraints i.e. code-rate, degree-distribution, constraint length, period and memory, in contrast to the majority of the available methodologies that produce relevant error-correcting codes based on either block ones, protographs or spatially-coupled type of codes. Simulation results show that the constructed ensembles demonstrate advanced error-correcting capability of up to 0.5 dB in terms of frame-error and bit-error rates at the convergence region, when compared to the performance of Forward Error Correction schemes adopted by various wireless standards, with comparable hardware complexity even at short codeword-lengths.

## Configurable and high-throughput architectures for Quasi-cyclic low-density parity-check codes

- **Status**: ✅
- **Reason**: QC-LDPC 인코더/디코더 FPGA 아키텍처(병렬화·configurability) — D 이식 가능 HW에 해당
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7050104
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Alaa Aldin Al Hariri, Fabrice Monteiro, Loïc Siéler +1
- **PDF**: https://ieeexplore.ieee.org/document/7050104
- **Abstract**: LDPC codes are currently the most promising coding technique to achieve the Shannon capacity, making them very popular in modern telecommuncation applications. Despite the attractivity stemming from their effectiveness, encoding and decoding LDPC codes is a rather complex task, due to the size and structure of the codes, especially when considering the ever increasing need for higher throughput in communication networks. All these constraints are setting the demand for new encoding/decoding architectures very high. In this paper, we propose effective encoder and decoder architectures for the Quasi-Cycle subclass of LDPC codes. The main features being targeted are pre-synthesis configurability and high throughput. QC-LDPC codes exhibit a highly regular structure in their parity check matrices making easier the design process to obtain the high levels of architectural parallelism necessary to achieve the required high throughputs. In order to validate our design, several encoder and decoder were implemented on FPGAs of the Altera Stratix III and Xilinx Virtex4 using different code parameters (block length and code rate) for QC-LPDC codes from the WiMAX (IEEE 802.16e) and the WiFi (IEEE 802.1 In) protocols. Throughputs up to 32 Gbits/s and 732 Mbits/s have been achieved for the encoder and decoder, respectively.

## A technique for the identification of trapping sets in LDPC codes

- **Status**: ✅
- **Reason**: LDPC trapping set 식별 기법 — error floor 분석/코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7050116
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Christos Vasilopoulos, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/7050116
- **Abstract**: In this paper we consider the problem of identifying trapping sets in Low Density Parity Check codes (LDPC), which is a hard NP-complete problem, as conjectured in [1]. We introduce a method for identifying trapping sets in LDPC codes. The proposed method is flexible and parametric. Furthermore it achieves low complexity and execution time and low memory requirements.

## An improved-performance decoding algorithm of LDPC codes for layered decoding

- **Status**: ✅
- **Reason**: layered+dynamic 결합한 신뢰도 기반 신규 layered 디코딩 알고리즘 — 부호 비의존적 BP 개선, 바이너리 LDPC 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7062283
- **Type**: conference
- **Published**: 5-7 Dec. 2
- **Authors**: Jia Li, Gaigai Yang, Zhiqiang Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7062283
- **Abstract**: In order to reduce the bit error rate of low-density parity-check codes for layered decoding algorithm and improve the decoding convergence speed, an improved layered decoding algorithm is proposed. In layered decoding algorithm, updated bit nodes information can be used by check nodes in the iteration process while in dynamic decoding algorithm check nodes update in order according to the reliability. The proposed algorithm combines advantages of the layered and dynamic decoding algorithm. Moreover, compared with the definition of remaining information for check nodes in the dynamic decoding algorithm, a new method to evaluate the reliability is defined in the proposed algorithm. Based on 1/2 code rate china mobile multimedia broadcasting standard, simulation and comparison between the conventional layered decoding algorithm and the proposed layered decoding algorithm have been carried out. The simulation results show that under the same bit error rate, the signal to noise ratio of the improved algorithm reduces nearly 0.4dB as well as convergence speed improves obviously. The proposed layered decoding algorithm reduces the bit error rate and improves the reliability of data in communication system which uses LDPC codes as the channel coding.

## High-speed multi-block-row layered decoding for Quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 멀티블록행 layered 디코더 임계경로 단축 HW, 처리량/면적 트레이드오프 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7032068
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Xinmiao Zhang, Ying Tai
- **PDF**: https://ieeexplore.ieee.org/document/7032068
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes are used in numerous digital communication and storage systems. Layered LDPC decoding converges faster. To further increase the throughput, multiple block rows of the QC parity check matrix can be included in a layer. However, the maximum achievable clock frequency of the prior multi-block-row layered decoder is limited by the long critical path. This paper reformulates the involved equations so that the updating of the messages belonging to different block rows in a layer does not depend on any common intrinsic message. This enables the removal of one adder and one routing network from the critical path. As a result, the proposed design can reach substantially higher clock frequency than prior design, and achieves effective throughput-area tradeoff.

## The Auto-configurable LDPC Codes for Distributed Storage

- **Status**: ✅
- **Reason**: 분산 스토리지용 구성가능 LDPC — 스토리지 ECC 일반(B), 인코딩/복구 trade-off 분석
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7023764
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Yongmei Wei, Yong Wee Foo, Khai Cher Lim +1
- **PDF**: https://ieeexplore.ieee.org/document/7023764
- **Abstract**: The current distributed storage systems mainly rely on data replication to ensure certain level of data availability and reliability. A recent trend is to introduce erasure codes into the distributed storage. Inspired by the RAID system, early attempts have been focused on designing Reed-Solomon (RS) based solutions and other block codes including Low Density Parity Check (LDPC) codes. This paper investigates in details about the usage of the system resources when different configurations of LDPC codes are applied to distributed storage systems. Auto-configurable LDPC-based method is proposed and integrated with the Hadoop system with various configurations of LDPC codes. Simulations show great improvement in terms of encoding and repairing latencies compared with Reed-Solomon. Simulations also show that trade-off in terms of different system resources is achieved through different configurations.

## Convergence of the Min-Sum Decoding Scheme for LDPC Codes from a Dynamical Systems Perspective

- **Status**: ✅
- **Reason**: Min-Sum 디코더 수렴/동역학 분석 — 디코더 거동·수렴 SNR영역 가이드(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7052031
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Monosij Maitra, Abhik Mukherjee
- **PDF**: https://ieeexplore.ieee.org/document/7052031
- **Abstract**: LDPC codes represent a class of codes for a wide variety of modern day coding applications including wireless communications and also some aspects of Cryptography. The general decoder for these codes, the Sum-Product algorithm can be viewed as a nonlinear dynamical system and has been shown to exhibit bifurcations and chaotic phenomena in the low and waterfall SNR zone in an AWGN channel. It has been attempted to investigate whether the Min-Sum decoder, a major approximation of the Sum-Product decoder, exhibits similar phenomena in its corresponding waterfall SNR zone for a particular Gallager code in the AWGN Channel. The results obtained indicate that the decoder does not show bifurcations and chaos in the waterfall SNR zone. Nevertheless, the decoder converges smoothly when the SNR stays above the waterfall region. This work guides how to find the convergent SNR zone for decoding any particular LDPC code with the Min-Sum decoder.

## An analysis on the applications of Markov random fields in error correcting codes of nano memory cells

- **Status**: ✅
- **Reason**: 나노 메모리 셀 ECC에 MRF/BP 적용 비교, 메모리 ECC 도메인이고 sparse BP HW 이식 가능성(애매하나 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7238542
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: G. Padma
- **PDF**: https://ieeexplore.ieee.org/document/7238542
- **Abstract**: This paper Compares various Error correcting codes in Nano scale Memory cells in terms of Belief Propagation Algorithm which is applied in a Markov Random Field (MRF). Soft error correction is critical for different Nano scale devices performing storage. As the Nano memories are with High fault rates, the conventional Error correcting Codes (ECCs) are not directly applicable. To achieve higher error correcting capability, a system is required that has high error detecting and correcting ability, with toleration to relatively high soft error rates. Also it requires sparse encoding, decoding and checker circuits, So that they can be synthesized using simple Nano scale hardware. In this paper the comparison is made using Belief Propagation Algorithm which is applied on Bipartite Graphs which are the MRFs.

## The design and verification of a novel LDPC decoder with high-efficiency

- **Status**: ✅
- **Reason**: TDMP + Ping-Pong 기반 신규 LDPC 디코더 HW 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7029459
- **Type**: conference
- **Published**: 10-12 Dec.
- **Authors**: Dan Yang, Guoyi Yu, Xuecheng Zou +2
- **PDF**: https://ieeexplore.ieee.org/document/7029459
- **Abstract**: A novel high-performance low density parity check codes (LDPC) decoder with small die size for IEEE802.16e criteria is presented in this paper. It utilizes the decoding technique called “Turbo Decoding Message Passing (TDMP)” and a new hardware architecture based on the Ping-Pong operation. Under the generic digital logic process of UMC, when the working frequency is 67MHz, the decoder presented in this paper has cell area of 7.19mm2, layout size of 10.72mm2, and maximum throughput of 1.1Gbps. The simulation results show that under AWGN channel with SNR of 3dB, the frame error rate of random code words is as low as 10-2.5. Compared with other papers, the LDPC decoder designed in this paper has a good error rate efficiency, higher throughput and smaller die size.
