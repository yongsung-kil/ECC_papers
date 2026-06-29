# IEEE Xplore — 2014-01 (1차선별 통과)


## A Low Complexity-High Throughput QC-LDPC Encoder

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 HW 아키텍처, 행렬 분해/압축 신규 기법, 다중 rate/길이 지원 — 이식 가능 HW/코드설계(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6781047
- **Type**: journal
- **Published**: May15, 201
- **Authors**: Ahmed Mahdi, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6781047
- **Abstract**: This paper introduces hardware architectures for encoding Quasi-Cyclic Low-Density Parity Check (QC-LDPC) codes. The proposed encoders are based on appropriate factorization and subsequent compression of involved matrices by means of a novel technique, which exploits features of recursively-constructed QC-LDPC codes. The particular approach derives to linear encoding time complexity and requires a constant number of clock cycles for the computation of parity bits for all the constructed codes of various lengths that stem from a common base matrix. The proposed architectures are flexible, as they are parameterized and can support multiple code rates and codes of different lengths simply by appropriate initialization of memories and determination of data bus widths. Implementation results show that the proposed encoding technique is more efficient for some LDPC codes than previously proposed solutions. Both serial and parallel architectures are proposed. Hardware instantiations of the proposed serial encoders demonstrate high throughput with low area complexity for code words of many thousand bits, achieving area reduction compared to prior art. Furthermore, parallelization is shown to efficiently support multi-Gbps solutions at the cost of moderate area increase. The proposed encoders are shown to outperform the current state-of-the-art in terms of throughput-area-ratio and area-time complexity by 10 to up to 80 times for codes of comparable error-correction strength.

## A Flexible NISC-Based LDPC Decoder

- **Status**: ✅
- **Reason**: NISC 기반 유연 LDPC 디코더, layered decoding, 비대칭 PU/MU 매핑 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6766729
- **Type**: journal
- **Published**: May15, 201
- **Authors**: Bertrand Le Gal, Christophe Jego, Camille Leroux
- **PDF**: https://ieeexplore.ieee.org/document/6766729
- **Abstract**: Low density parity-check (LDPC) codes, are widely used for error correction in digital communication systems. Their inclusion in communication standards requires to define decoders able to support efficiently a set of codes with different code length, code rates or code structures. In addition to this high flexibility, these decoders still have to achieve high throughputs in order to comply with standards requirements. In this paper, we propose to address the problem of designing generic and efficient LDPC decoders by using a nonsymmetric NISC-based architecture that performs layered decoding. NISC architectures provide flexibility with a limited loss in hardware efficiency. In addition, an automated design flow is used to efficiently assign computations to the processing units (PU) and to map data to the memory units (MU). Unlike previous works, the NISC decoder can include a number of PUs that is different than the number of MUs. This nonsymmetric characteristic provides a higher degree of freedom during the computation/data assignment phase of the design flow. This whole design framework automatically generates an LDPC decoder able to support any set of predetermined LDPC codes regardless of their parameters. The automated nature of the design framework enables to easily explore the design space for a given set of codes. Compared to state of the art LDPC decoders, the automatically generated decoders achieve higher hardware efficiency even for the challenging-to-implement unstructured LDPC codes.

## Subcarrier Reliability Aware Soft-Decision LDPC Code in CO-OFDM Systems

- **Status**: ✅
- **Reason**: 부반송파별 노이즈 분산을 LLR/디코딩에 반영하는 soft-decision LDPC 기법 — 채널 신뢰도 기반 LLR 가중은 NAND read-retry/LLR에 이식 여지(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6778012
- **Type**: journal
- **Published**: June1, 201
- **Authors**: Di Che, Hamid Khodakarami, An Li +3
- **PDF**: https://ieeexplore.ieee.org/document/6778012
- **Abstract**: We propose a subcarrier reliability aware low-density parity-check (SRA-LDPC) soft-decision coding scheme for coherent optical orthogonal frequency division multiplexing (CO-OFDM) systems. The SRA-LDPC code takes consideration of varying signal-to-noise ratio performance among different OFDM subcarriers. At the SRA-LDPC encoder, flexible forward error correction is applied to different ranges of subcarriers. At the decoder, the algorithm keeps track of noise variance of each subcarrier and utilizes such variance for decoding. Our proposed algorithm is substantiated in a 120-Gb/s CO-OFDM system where near-dc noise originated from the local oscillator is detrimental to the system performance. The experimental results show that the SRA-LDPC code is effective in combating near-dc noise and enhancing the receiver sensitivity.

## Lowering the Error Floor of LDPC Codes Using Multi-Step Quantization

- **Status**: ✅
- **Reason**: LDPC MP 디코더 입력 양자화 다단계 기법으로 error floor 저감, NAND LLR 양자화에 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6676774
- **Type**: journal
- **Published**: January 20
- **Authors**: Sina Tolouei, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/6676774
- **Abstract**: A multi-step scheme is proposed for the input quantization of message-passing decoders for low-density parity-check (LDPC) codes. The proposed scheme, which is applicable to both regular and irregular codes, lowers the error floor significantly at the cost of small increase in complexity, memory and latency.

## Quantized Iterative Message Passing Decoders with Low Error Floor for LDPC Codes

- **Status**: ✅
- **Reason**: (q+1)-bit quasi-uniform 양자화로 LDPC MP 디코더 error floor 저감, NAND LLR 양자화에 직접 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6685976
- **Type**: journal
- **Published**: January 20
- **Authors**: Xiaojie Zhang, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6685976
- **Abstract**: The error floor phenomenon observed with LDPC codes and their graph-based, iterative, message-passing (MP) decoders is commonly attributed to the existence of error-prone substructures - variously referred to as near-codewords, trapping sets, absorbing sets, or pseudocodewords - in a Tanner graph representation of the code. Many approaches have been proposed to lower the error floor by designing new LDPC codes with fewer such substructures or by modifying the decoding algorithm. Using a theoretical analysis of iterative MP decoding in an idealized trapping set scenario, we show that a contributor to the error floors observed in the literature may be the imprecise implementation of decoding algorithms and, in particular, the message quantization rules used. We then propose a new quantization method - (q+1)-bit quasi-uniform quantization - that efficiently increases the dynamic range of messages, thereby overcoming a limitation of conventional quantization schemes. Finally, we use the quasi-uniform quantizer to decode several LDPC codes that suffer from high error floors with traditional fixed-point decoder implementations. The performance simulation results provide evidence that the proposed quantization scheme can, for a wide variety of codes, significantly lower error floors with minimal increase in decoder complexity.

## Gallager B LDPC Decoder with Transient and Permanent Errors

- **Status**: ✅
- **Reason**: 잡음/영구오류 Gallager B LDPC 디코더 분석+패리티체크 활용 오류검출정정, 디코더 신뢰성 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6679370
- **Type**: journal
- **Published**: January 20
- **Authors**: Chu-Hsiang Huang, Yao Li, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6679370
- **Abstract**: This paper studies the performance of a noisy Gallager B decoder for regular LDPC codes. We assume that the noisy decoder is subject to both transient processor errors and permanent memory errors. We permit different error rates at different functional components. In addition, for the sake of generality, we allow asymmetry in the permanent error rates of component outputs, and thus we model error propagation in the decoder via a suitable asymmetric channel. We then develop a density evolution-type analysis on this asymmetric channel. The recursive expression for the bit error probability is derived as a function of the code parameters (node degrees), codeword weight, transmission error rate, and the error rates of the permanent and the transient errors. Based on this analysis, we then derive the residual error of the Gallager B decoder for the regime where the transmission error rate and the processing error rates are small. In this regime, we further observe that the residual error rate can be well approximated by a suitable combination of the transient error rate and the permanent error rate at variable nodes, provided that the check node degree is large enough. Based on this insight, we then propose and analyze a scheme for detecting permanent errors and correcting detected residual errors. The scheme exploits the parity check equations of the code and reuses the existing hardware to locate permanent errors in memory blocks. Performance analysis and simulation results show that, with high probability, the detection scheme discovers correct locations of permanent memory errors, while, with low probability, it mislabels the functional memory as being defective. The proposed error detection-and-correction scheme can be implemented in-circuit and is useful in combating failures arising from aging.

## An LDPC Decoder With Time-Domain Analog and Digital Mixed-Signal Processing

- **Status**: ✅
- **Reason**: 65nm CMOS LDPC 디코더 HW(시간영역 아날로그-디지털 혼합신호, 10.4pJ/bit) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6630119
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Daisuke Miyashita, Ryo Yamaki, Kazunori Hashiyoshi +4
- **PDF**: https://ieeexplore.ieee.org/document/6630119
- **Abstract**: Time-domain analog and digital mixed-signal processing (TD-AMS) is presented. Analog computation is more energy- and area-efficient at the cost of its limited accuracy, whereas digital computation is more versatile and derives greater benefits from technology scaling. Besides, design automation tools for digital circuits are much more sophisticated than those for analog circuits. TD-AMS exploits both advantages, and is a solution better suited to implementing a system on chip including functions for which high computational accuracy is not required, such as error correction, image processing, and machine learning. As an example, a low-density parity-check (LDPC) code decoder with the technique is implemented in 65 nm CMOS and achieves the best reported efficiencies of 10.4 pJ/bit and 6.1 Gbps/mm2.

## On Decoding Irregular Tanner Codes With Local-Optimality Guarantees

- **Status**: ✅
- **Reason**: 이진 Tanner/LDPC용 신규 메시지패싱 디코더 NWMS(normalized weighted min-sum)와 국소최적성·ML 인증서 제시 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6626647
- **Type**: journal
- **Published**: Jan. 2014
- **Authors**: Nissim Halabi, Guy Even
- **PDF**: https://ieeexplore.ieee.org/document/6626647
- **Abstract**: We consider decoding of binary linear Tanner codes using message-passing iterative decoding and linear-programming (LP) decoding in memoryless binary-input output-symmetric (MBIOS) channels. We present new certificates that are based on a combinatorial characterization for the local optimality of a codeword in irregular Tanner codes with respect to any MBIOS channel. This characterization is a generalization of (Arora , Proc. ACM Symp. Theory of Computing, 2009) and (Vontobel, Proc. Inf. Theory and Appl. Workshop, 2010) and is based on a conical combination of normalized weighted subtrees in the computation trees of the Tanner graph. These subtrees may have any finite height h (even equal or greater than half of the girth of the Tanner graph). In addition, the degrees of local-code nodes in these subtrees are not restricted to two (i.e., these subtrees are not restricted to skinny trees). We prove that local optimality in this new characterization implies maximum-likelihood (ML) optimality and LP optimality, and show that a certificate can be computed efficiently. We also present a new message-passing iterative decoding algorithm, called normalized weighted min-sum (NWMS). NWMS decoding is a belief-propagation (BP) type algorithm that applies to any irregular binary Tanner code with single parity-check local codes (e.g., low-density and high-density parity-check codes). We prove that if a locally optimal codeword with respect to height parameter h exists (whereby notably h is not limited by the girth of the Tanner graph), then NWMS decoding finds this codeword in h iterations. The decoding guarantee of the NWMS decoding algorithm applies whenever there exists a locally optimal codeword. Because local optimality of a codeword implies that it is the unique ML codeword, the decoding guarantee also provides an ML certificate for this codeword. Finally, we apply the new local-optimality characterization to regular Tanner codes, and prove lower bounds on the noise thresholds of LP decoding in MBIOS channels. When the noise is below these lower bounds, the probability that LP decoding fails to decode the transmitted codeword decays doubly exponentially in the girth of the Tanner graph.

## High-Throughput Energy-Efficient LDPC Decoders Using Differential Binary Message Passing

- **Status**: ✅
- **Reason**: DD-BMP/MDD-BMP/IDB 차분 바이너리 메시지패싱 디코더 + 65nm CMOS 풀패럴렐 구현 — 디코더(C)+HW(D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6675862
- **Type**: journal
- **Published**: Feb.1, 201
- **Authors**: Kevin Cushon, Saied Hemati, Camille Leroux +2
- **PDF**: https://ieeexplore.ieee.org/document/6675862
- **Abstract**: In this paper, we present energy-efficient architectures for decoders of low-density parity check (LDPC) codes using the differential decoding with binary message passing (DD-BMP) algorithm and its modified variant (MDD-BMP). We also propose an improved differential binary (IDB) decoding algorithm. These algorithms offer significant intrinsic advantages in the energy domain: simple computations, low interconnect complexity, and very high throughput, while achieving error correction performance up to within 0.25 dB of the offset min-sum algorithm. We report on fully parallel decoder implementations of (273, 191), (1023, 781), and (4095, 3367) finite geometry-based LDPC codes in 65 nm CMOS. Using the MDD-BMP algorithm, these decoders achieve respective areas of 0.28 mm2, 1.38 mm2, and 15.37 mm2, average throughputs of 37 Gbps, 75 Gbps, and 141 Gbps, and energy efficiencies of 4.9 pJ/bit, 13.2 pJ/bit, and 37.9 pJ/bit with a 1.0 V supply voltage in post-layout simulations. At a reduced supply voltage of 0.8 V, these decoders achieve respective throughputs of 26 Gbps, 54 Gbps, and 94 Gbps, and energy efficiencies of 3.1 pJ/bit, 8.2 pJ/bit, and 23.5 pJ/bit. We also report on a fully parallel implementation of IDB for the (2048, 1723) LDPC code specified in the IEEE 802.3an (10GBASE-T) standard. This decoder achieves an area of 1.44 mm2, average throughput of 172 Gbps, and an energy efficiency of 2.8 pJ/bit with a 1.0 V supply voltage; at 0.8 V, it achieves throughput of 116 Gbps and energy efficiency of 1.7 pJ/bit.

## An improvement of approximate BP decoding

- **Status**: ✅
- **Reason**: Min-Sum의 piecewise-linear 근사로 BP 성능 근접·저복잡도 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6979829
- **Type**: conference
- **Published**: 2014
- **Authors**: G. Hosoya, H. Yashima
- **PDF**: https://ieeexplore.ieee.org/document/6979829
- **Abstract**: In this study, we present new methods for piece-wise linear approximation of Min-Sum (MS) decoding algorithm with good trade-off between performance and complexity. By analysis based on density evolution, the performance of the proposed method is identical to that of the Belief-Propagation decoding algorithm. The increment of the complexity of the proposed algorithm is small compared with the MS decoding algorithm. Moreover simulation result also shows effectiveness of the proposed algorithm.

## Performance comparison of hybrid partial response detectors over frequency-selective fading channels

- **Status**: ✅
- **Reason**: PRBP(partial response BP) 검출기; 부호 비의존 BP 디코더 기법이며 자기기록 응용 언급, 바이너리 LDPC BP 이식 가능성으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865485
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Peng, X. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6865485
- **Abstract**: Frequency-selective fading channels are encountered in many modern wireless communication systems. In order to combat the intersymbol interference (ISI) introduced by such fading, equalization is required for reliable symbol detection. The maximum-likelihood sequence detector is the optimal equalization scheme; however its implementation complexity increases exponentially with the channel length and thus can be prohibitively high. In this paper, we compare the performance of two practically implementable suboptimal symbol detectors, including the partial response maximum-likelihood (PRML) detector and the partial response belief propagation (PRBP) detector, under frequency-selective fading channels. Both detectors employ a hybrid two-stage scheme, and allow a tradeoff between performance and complexity. The first stage is a partial response equalizer implemented as a linear filter which transforms the original channel impulse response to a target impulse response with reduced ISI. The residual ISI is then cancelled in the second stage using a more sophisticated nonlinear detector. In simulations, we consider a slow fading environment and use the ITU-R 3G channel models. From the numerical results, it is shown that in frequency-selective fading wireless channels, the PRBP detector provides superior performance over both the traditional minimum mean squared error linear equalizer and the PRML detector. Due to the effect of colored noise, the PRML detector in fading wireless channels is not as effective as it is in magnetic recording applications.

## Sparse binary matrices as efficient associative memories

- **Status**: ✅
- **Reason**: 희소 바이너리 행렬 연상메모리를 ECC 디코더로 보고 수렴하는 반복 디코딩 알고리즘 제시 — 이식 가능 디코더(C) 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7028496
- **Type**: conference
- **Published**: 2014
- **Authors**: V. Gripon, V. Skachek, M. Rabbat
- **PDF**: https://ieeexplore.ieee.org/document/7028496
- **Abstract**: Associative memories are widely used devices which can be viewed as universal error-correcting decoders. Employing error-correcting code principles in these devices has allowed to greatly enhance their performance. In this paper we reintroduce a neural-based model using the formalism of linear algebra and extend its functionality, originally limited to erasure retrieval, to handle approximate inputs. In order to perform the retrieval, we use an iterative algorithm that provably converges. We then analyze the performance of the associative memory under the assumption of connection independence. We support our theoretical results with numerical simulations.

## Hybrid DFSF-BP equalization for ATSC DTV receivers

- **Status**: ✅
- **Reason**: BP 기반 반복 MAP 이퀄라이저(DFSF+BP); 부호 비의존 BP 메시지패싱 기법이라 LDPC BP 디코더에 이식 가능성, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865484
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Peng, A. G. Klein, X. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6865484
- **Abstract**: Severe intersymbol interference (ISI) is one of the main obstacles for reliable signal reception in ATSC DTV systems. Decision feedback equalizers (DFEs) are commonly used to suppress the ISI. However, DFEs may suffer from error propagation due to incorrect symbol decisions from the symbol slicer. This phenomenon deteriorates the performance even more when the post-cursor ISI is strong. In order to reduce error propagation, we present a novel hybrid equalization scheme for ATSC channels. The proposed scheme consists of an adaptive decision feedback sparsening filter (DFSF), and an iterative maximum a posteriori (MAP) equalizer based on the belief propagation (BP) algorithm. In the first stage, instead of removing all the ISI from post cursors, the DFSF employs a modified feedback filter which leaves the strongest post-cursor ISI taps uncorrected. As a result, a long ISI channel is equalized to a sparse channel having only a small number of nonzero taps. In the second stage, a belief propagation algorithm is applied to mitigate the residual ISI. Since the channel is typically time-varying and suffers from Doppler fading, the DFSF is adapted using the least mean square (LMS) algorithm, such that the amplitude and the locations of the nonzero taps of the equalized sparse channel appear to be fixed. As such, the channel appears to be static during the second stage of equalization which consists of the BP detector. Simulation results demonstrate that the proposed scheme outperforms the traditional DFE in symbol error rate, under both static channels and dynamic ATSC channels.

## Low power and low voltage SRAM design for LDPC codes hardware applications

- **Status**: ✅
- **Reason**: LDPC 하드웨어용 저전력/저전압 SRAM 셀 설계; 디코더 HW 메모리 구현 기법으로 NAND LDPC HW에 이식 가능(D, 애매하여 살림)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6920865
- **Type**: conference
- **Published**: 2014
- **Authors**: R. Deena Kumari Selvam, C. Senthilpari, L. Lini
- **PDF**: https://ieeexplore.ieee.org/document/6920865
- **Abstract**: The Low Voltage Low Power (LVLP) 8T, 11T, 13T and ZA SRAM cell is designed using the dynamic logic SRAM cell. The SRAM cells are implemented using pass transistor logic technique, which is mainly focused on read and write operation. The circuits are designed by using DSCH2 circuit editor and their layouts are generated by MICROWIND3 layout editor. The Layout Versus Simulation (LVS) design has been verified using BSIM 4 with 65nm technology and with a corresponding voltage of 0.7V respectively. The simulated SRAM layouts are verified and analyzed. The SRAM 8T gives power dissipation of 0.145 microwatts, propagation delay of 37.2 pico seconds, area of 14 × 8 micrometers and a throughput of 4.037 nano seconds.

## Faulty stochastic LDPC decoders over the binary symmetric channel

- **Status**: ✅
- **Reason**: 결함 HW상 stochastic LDPC 디코더 유한길이 분석, 이식 가능한 디코더/HW 강건성 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955096
- **Type**: conference
- **Published**: 2014
- **Authors**: C. L. Kameni Ngassa, V. Savin, D. Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6955096
- **Abstract**: The analysis of error correction decoders running on faulty hardware has attracted an increasing interest in recent years, due to the inherent unreliability of emerging nanodevices. In this paper we investigate the performance of the stochastic decoder running on faulty hardware. To this end, we first introduce two error models to describe the noisy components of the decoder. We then provide a finite-length statistical analysis for each error model and, based on the obtained performance, we conclude that stochastic decoders have an inherent fault tolerant capability.

## Reducing the complexity of LDPC decoding algorithms: An optimization-oriented approach

- **Status**: ✅
- **Reason**: LDPC 디코더 복잡도 절감 최적화 프레임워크(성능-복잡도 트레이드오프) — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7136286
- **Type**: conference
- **Published**: 2014
- **Authors**: M. Sarajlić, L. Liu, O. Edfors
- **PDF**: https://ieeexplore.ieee.org/document/7136286
- **Abstract**: This paper presents a structured optimization framework for reducing the computational complexity of LDPC decoders. Subject to specified performance constraints and adaptive to environment conditions, the proposed framework leverages the adjustable performance-complexity tradeoffs of the decoder to deliver satisfying performance with minimum computational complexity. More specifically, two constraint scenarios are studied: the “good-enough” performance and “as-good-as-possible performance”. Moreover, we also investigate the effects of different degrees of freedom in performance-complexity tradeoff adjustments. The effectiveness of the proposed method has been verified by simulating a set of LDPC codes used in IEEE 802.11 and IEEE 802.16 standards. Computational complexity reductions of up to 35% have been observed.

## Towards energy effective LDPC decoding by exploiting channel noise variability

- **Status**: ✅
- **Reason**: 채널 노이즈 변동성을 활용한 에너지 효율 LDPC 디코딩 + 적응형 전압조절 기법, FPGA 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7004180
- **Type**: conference
- **Published**: 2014
- **Authors**: T. Marconi, C. Spagnol, E. Popovici +1
- **PDF**: https://ieeexplore.ieee.org/document/7004180
- **Abstract**: In communication systems, channel quality variation is a well known phenomenon, which fundamentally influences the decoding process. While most of the time, the transmission takes place in good signal to noise conditions, to satisfy QoS requirements in all cases, telecom platforms rely on largely over-designed hardware, which may result in energy waste during most of their operation. In this paper we propose to exploit the channel noise variability and adapt the platform operation conditions such that QoS requirements are satisfied with the minimum energy consumption. In particular, we propose a technique to exploit channel noise variability towards energy effective LDPC decoding amenable to low-energy operation. Endowed with the channel noise variability knowledge, our technique adaptively tunes the operating voltage at runtime, aiming to achieve the optimal tradeoff between decoder performance and power con-sumption, while fulfilling the QoS requirements. To demonstrate the capabilities of our proposal we implemented it and other state of the art energy reduction methods in conjunction with a fully parallel LDPC decoder on a Virtex-6 FPGA. Our experiments indicate that the proposed technique outperforms state of the art counterparts, in terms of energy reduction, with 71% to 76% and 15% to 28%, w.r.t. early termination without and with DVS, respectively, while maintaining the targeted decoding robustness. Moreover, the measurements suggest that in certain conditions Degradation Stochastic Resonance occurs, i.e., the energy consumption is unexpectedly diminished due to the fact that unpredictable underpowered components facilitate rather than impede the decoding process.

## Reconfigurable FEC codes for software-defined optical transceivers

- **Status**: ✅
- **Reason**: Reconfigurable FEC (variable code length/LLR-width) on FPGA — possibly includes LDPC; portable reconfigurable-decoder HW angle, keep for Phase 3
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6987087
- **Type**: conference
- **Published**: 2014
- **Authors**: C. Kachris, G. Tzimpragos, D. Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6987087
- **Abstract**: Flexible Optical Networks can optimize the network resources by offering increased spectral utilization. However, these networks require the use of novel software-defined Optical Transceivers that can adapt their features to the channel's requirements. This paper presents a novel optical transceiver architecture using a reconfigurable FEC coding scheme for flexible optical networks. The proposed approach can dynamically support different versions of FEC codes (with different overheads, code lengths, and LLR-widths) based on the network's Quality-of-Service requirements, whereas it can also be applied for the dynamic reconfiguration of the DSP units and the realization of dynamic coded-modulation schemes. The proposed approach has been implemented into an FPGA platform. The performance evaluation shows that the reconfiguration time is always less than 12 ms, which means that the proposed scheme could be utilized in many optical networks, where the reconfiguration time (e.g. for the optical switches or the WSS) is in the order of a few ms.

## The effect of saturation on belief propagation decoding of LDPC codes

- **Status**: ✅
- **Reason**: LLR 포화가 BP 디코딩/error floor에 미치는 영향 분석 — NAND LDPC LLR 양자화/포화와 직결(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875305
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Kudekar, T. Richardson, A. Iyengar
- **PDF**: https://ieeexplore.ieee.org/document/6875305
- **Abstract**: We consider the effect of LLR saturation on belief propagation decoding of low-density parity-check codes. Saturation is commonly done in practice and is known to have a significant effect on error floor performance. Our focus is on threshold analysis and the stability of density evolution. We analyze the decoder for certain low-density parity-check code ensembles and show that belief propagation decoding generally degrades gracefully with saturation. Stability of density evolution is, on the other hand, rather strongly affected by saturation and the asymptotic qualitative effect of saturation is similar to reduction of variable node degree by one.

## Advanced coded modulation for ultrahigh speed optical transmission

- **Status**: ✅
- **Reason**: 슬라이드지만 high-girth QC-LDPC 코드설계·iterative decoding·QC-LDPC FPGA 구현 등 구체적 신규 기여 다수(C/D/E 이식 가능, 서베이 예외)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6887154
- **Type**: conference
- **Published**: 2014
- **Authors**: I. B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6887154
- **Abstract**: This article consists of a collection of slides from the author's conference presentation. Some of the specific areas/topics discussed include: LDPC code design & large (high)-girth QC-LDPC Codes; Iterative decoding algorithms; FPGA implementation of decoders for QC-LDPC codes; LDPC codes derived from QC-LDPC code design; Binary/nonbinary irregular QC-LDPC codes derived from PBDs; Optimum signal constellation design & optimized mapping rules; EXIT chart analysis; Rate-adaptive LDPC-coded modulation; Nonbinary LDPC-coded modulation; Hybrid multidimensional coded-modulation; Multilevel/multidimensional LDPC-coded turbo equalization; and Rate-adaptive multidimensional coded-modulation.

## Optimal Joint Viterbi Detector Decoder (JVDD) over AWGN/ISI channel

- **Status**: ✅
- **Reason**: JVDD: SPA 단락사이클 차선성 극복하는 joint 검출/디코딩 알고리즘 — BP 차선성 개선 디코더 기법으로 LDPC BP에 이식 검토 가치(C, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6785346
- **Type**: conference
- **Published**: 2014
- **Authors**: Kheong Sann Chan, S. S. B. Shafiee, E. M. Rachid +1
- **PDF**: https://ieeexplore.ieee.org/document/6785346
- **Abstract**: Communication channels today use a state-of-the art iterative detector/decoder system on its receiver end to detect and decode the transmitted bits. This iterative detection system is comprised of a soft output detector, either the soft output Viterbi algorithm (SOVA) or the Bahl, Cocke, Jelinek and Raviv (BCJR) algorithm, and the Sum Product Algorithm (SPA) is used in the decoder. Although iterations of the soft information between these detector and decoder blocks gives rise to good performance over an inter-symbol-interference (ISI)/additive white Gaussian noise (AWGN) channel when the codeword length (CWL) is large, the iterative detector is sub-optimal. This suboptimality originates from the SPA algorithm that itself is suboptimal whenever there are cycles in the factor graph, in particular, when there are short cycles. Any practical code will have cycles in its factor graph. A second source of suboptimality is the iterative process itself. There exist iterations both within the SPA decoder and between the decoder and the detector. In this work, the authors propose a novel detection/decoding algorithm coined the Joint Viterbi Detector Decoder (JVDD) that functionally replaces the iterative detector/decoder in the channel. Unlike the iterative detector/decoder, the proposed algorithm performs detection and decoding on a single structure and is optimal over an ISI/AWGN channel when there are sufficient computational resources. In this work we describe the JVDD algorithm and perform preliminary analysis on its performance and complexity under various conditions.

## High Order Modulation in Faster-Than-Nyquist Signaling Communication Systems

- **Status**: ✅
- **Reason**: FTN 신호에 맞춘 신규 최적화 QC-LDPC 부호 설계 주장(E); FTN 특화이나 애매하여 Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6965997
- **Type**: conference
- **Published**: 2014
- **Authors**: J. Yu, J. Park, F. Rusek +2
- **PDF**: https://ieeexplore.ieee.org/document/6965997
- **Abstract**: In this paper we investigate the highly bandwidth-efficient Faster-than-Nyquist (FTN) signaling scheme under high order modulations. The FTN system is an emerging technology which has drawn attention in the contemporary spectrum-saving communication environment. Since FTN traditionally achieves high bandwidth efficiency through increased baud-rate, binary modulation is assumed in most research of FTN. The contribution of this paper lies in the extension into high order modulations and its assessment. This enables the communication systems to achieve higher data rates for the same bandwidth and receiver complexity than binary Nyquist signaling systems. Moreover, it is shown that an additional efficiency gain can be achieved by replacing the LDPC codes from the DVB-S2 standard by new optimized quasi-cyclic (QC) LDPC codes whose parameters are matched with FTN signaling.

## Noisy belief propagation decoder

- **Status**: ✅
- **Reason**: 노이즈 HW상 LDPC BP 디코더 분석+averaging BP 구현 — 이식 가능 디코더 기법(C), NAND HW 신뢰성에 직결
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7094847
- **Type**: conference
- **Published**: 2014
- **Authors**: C. -H. Huang, Y. Li, L. Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/7094847
- **Abstract**: This paper analyzes the fundamental performance limits of an LDPC Belief Propagation (BP) decoder implemented on noisy hardware and proposes a robust decoder implementation to improve the resilience to hardware errors. Assuming that the effects of hardware noise in various computational units, i.e., variable nodes and check nodes, can be approximated by Gaussian noise, we develop a Gaussian approximate density evolution for noisy BP decoders. By the Gaussian approximate density evolution, we find that zero residual error rate is achievable for noisy BP decoders as long as the message representations are of arbitrarily high precision. Noisy BP decoding thresholds are then derived for various regular LDPC codes. These decoding thresholds determine maximum allowable communication and computation noise for reliable communication. Next, we propose an averaging BP decoder implementation by averaging over the messages in all up-to-date iterations to cancel out the computation noise. Simulation results demonstrate that on noisy hardware, the averaging BP decoder significantly reduces the residual error rates when compared to the nominal BP decoder.

## Memory sharing techniques for multi-standard high-throughput FEC decoder

- **Status**: ✅
- **Reason**: 멀티표준 FEC 디코더 메모리 공유 HW 기법(D), LDPC 포함, 디코더 메모리 병합 아키텍처 NAND LDPC HW에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6893199
- **Type**: conference
- **Published**: 2014
- **Authors**: Z. Wu, D. Liu
- **PDF**: https://ieeexplore.ieee.org/document/6893199
- **Abstract**: Nowadays multi-standard wireless baseband, Convolutional Code (CC), Turbo code and LDPC code are widely applied and need to be integrated within one FEC module. Since memory occupies half or even more area of the decoder, memory sharing techniques for area saving purpose is valuable to consider. In this work, several memory merging techniques are proposed. A non-conflict access technique for merged path metric buffer is proposed. The results show that 41% of total memory bits are saved when integrating three different decoding schemes including CC (802.11a/g/n), LDPC (802.11n and 802.16e) and Turbo (3GPP-LTE). Synthesis result with 65nm process shows that the merged memory blocks consume merely 1.06mm2 of the chip area.

## Flexible multistandard FEC processor design with ASIP methodology

- **Status**: ✅
- **Reason**: ASIP 기반 멀티표준 FEC 프로세서로 QC-LDPC 디코딩 지원; 디코더 datapath/병렬화 HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6868664
- **Type**: conference
- **Published**: 2014
- **Authors**: Z. Wu, D. Liu
- **PDF**: https://ieeexplore.ieee.org/document/6868664
- **Abstract**: Designing decoder for forward error correction (FEC) is more and more challenging because of the requirements on simultaneous supporting of various wireless standards within one IC module. The flexibility, silicon cost and throughput efficiency are all necessary to be traded off. In this paper, by using ASIP methodology, software-hardware co-design is introduced to offer sufficient flexibility of FEC decoding. The decoding procedure can be programmable for decoding QC-LDPC, Turbo and Convolutional Codes. Firstly, the common features from all mentioned algorithms and their corresponding datapaths are analyzed and a unified multi-standard datapath is introduced. Based on it, an application specific instruction-set is proposed and an ASIP (Application Specific Instruction-set Processor) for the FEC algorithms is designed. The firmware FEC codes are developed to adapt to standards. Synthesis results show that the proposed FEC processor is 1.54mm2 under 65nm CMOS process. It offers QC-LDPC decoding for WiMAX, Turbo decoding for 3GPP-LTE, and 64 states Convolutional code (CC) decoding at the throughput of 193 Mbps, 62 Mbps and 60 Mbps respectively under clock frequency of 200 MHz. The proposed ASIP provides programmable high throughput compared to other tri-mode hardware modules.

## Analysis of one-step majority logic decoding under correlated data-dependent gate failures

- **Status**: ✅
- **Reason**: 신뢰불가 소자(게이트 고장/타이밍 에러) 하 majority-logic LDPC 디코딩 BER 해석 — 디코더 신뢰성 해석 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6875304
- **Type**: conference
- **Published**: 2014
- **Authors**: S. Brkic, P. Ivanis, B. Vasić
- **PDF**: https://ieeexplore.ieee.org/document/6875304
- **Abstract**: In this paper we present analysis of one-step majority logic decoders made of unreliable components in the presence of data-dependent gate failures. Gate failures are modeled by a Markov chain, and based on the combinatorial representation of the fault configurations, a closed-form expression for the average bit error rate is derived for a regular LDPC code ensemble. Presented analysis framework is then used for obtaining upper bounds on decoding performance under timing errors.

## Finite alphabet iterative decoders robust to faulty hardware: Analysis and selection

- **Status**: ✅
- **Reason**: Finite Alphabet Iterative Decoder(FAID)의 결함 HW 강건성 분석+선택, 이식 가능한 바이너리 LDPC 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6955095
- **Type**: conference
- **Published**: 2014
- **Authors**: E. Dupraz, D. Declercq, B. Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/6955095
- **Abstract**: In this paper, we analyze Finite Alphabet Iterative Decoders (FAIDs) running on faulty hardware. Under symmetric error models at the message level, we derive the noisy Density Evolution equations, and introduce a new noisy threshold phenomenon (called functional threshold), which accurately characterizes the convergence behavior of LDPC code ensembles under noisy-FAID decoding. The proposed functional threshold is then used to identify FAIDs which are particularly robust to the transient hardware noise. Finite-length simulations are drawn to verify the validity of the asymptotical study.

## Instanton search algorithm for the ADMM penalized decoder

- **Status**: ✅
- **Reason**: ADMM penalized LP 디코더의 instanton/trapping set 분석 — 부호 비의존 BP 대체 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6874922
- **Type**: conference
- **Published**: 2014
- **Authors**: X. Liu, S. C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/6874922
- **Abstract**: Linear programming (LP) decoding using the alternating direction method of multipliers (ADMM) has been shown to be an efficient algorithm. A non-convex variation based on the ADMM LP decoder called the ADMM penalized decoder was introduced by Liu et al. (IEEE ITW, Sep. 2012) to close the signal-to-noise ratio (SNR) gap between LP decoding and classic belief propagation (BP) decoding. This algorithm was shown to achieve or outperform BP decoding at all SNRs, including high SNRs where BP decoding suffers from the error floor effect. In this paper, we study the behaviors of the ADMM penalized decoder at high SNRs where simulation is infeasible. We use a generic tool called instanton analysis and propose an instanton search algorithm for the ADMM penalized decoder. We then apply the algorithm to the [155, 64] Tanner code and a [1057, 813] LDPC code. We show that the instanton information we obtained provides good predictions for word-error-rate curve at high SNRs. In addition, our results suggest that the ADMM penalized decoder can suffer from trapping sets.

## FPGA implementation of a multi-algorithm parallel FEC for SDR platforms

- **Status**: ✅
- **Reason**: Turbo/QC-LDPC/Conv 다중알고리즘 병렬 FEC FPGA 프로세서; QC-LDPC 병렬 디코더 HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6927446
- **Type**: conference
- **Published**: 2014
- **Authors**: Zhenzhi Wu, D. Liu, Zheng Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6927446
- **Abstract**: Forward Error Correction (FEC) consumes excessive computation in a Software Defined Radio (SDR) system. In this work, a high-throughput flexible FEC processor is proposed for the decoding acceleration. The FEC processor enables Turbo/QC-LDPC/Convolutional Code decoding with software-hardware co-reconfigurability. A multi-algorithm unified trellis processing unit is introduced for resource sharing. A parallel architecture is proposed for high-throughput decoding. The Software Defined FEC (SD-FEC) with Application Specific Instruction-set Processor architecture is introduced for improving flexibility and enabling fast reconfiguration. The proposed SD-FEC can be applied to both low-cost low power applications and high performance applications. Results show that the proposed tri-mode FEC processor achieves high decoding efficiency and enough flexibility, which suits for the flexible SDR platforms.

## Hardware-Oriented Construction of a Family of Rate-Compatible Raptor Codes

- **Status**: ✅
- **Reason**: 아키텍처-aware 구조적 부호 구성(row split-after-merge, 구조화 행 인코딩) — Raptor지만 QC-LDPC HW/코드설계로 이식 여지, 애매하여 보존(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6814837
- **Type**: journal
- **Published**: 2014
- **Authors**: H. Zeineddine, L. M. A. Jalloul, M. M. Mansour
- **PDF**: https://ieeexplore.ieee.org/document/6814837
- **Abstract**: A family of architecture-aware Raptor codes is constructed. The proposed construction scheme is targeted to design rate-compatible structured codes that span a wide range of rates and block sizes while still having hardware-efficient decoder implementations. The codes match the corresponding fixed-rate LDPC codes in error-correcting performance, decoding convergence speed, and message-memory requirements. Three novel steps are incorporated in the scheme: 1) a new group-based design of the code source matrix; 2) an architecture-aware row splitting-after-merging technique to construct irregular precodes; and 3) structured LT row-encoding. A code instance was designed accordingly and compared to standardized LDPC codes. The error-rate performance closely matches that of LDPC, whereas the convergence speed and message count gaps are narrowed down to values between  $[1.1\times, 1.8\times]$ and  $[1.1\times, 1.3\times]$, respectively.

## On Detection Method for Soft Iterative Decoding in the Presence of Impulsive Interference

- **Status**: ✅
- **Reason**: 임펄스(α-stable) 간섭 하 BP 디코더 LLR 근사 기법 — 부호 비의존적 LLR 계산 변형으로 NAND LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6809154
- **Type**: journal
- **Published**: 2014
- **Authors**: V. Dimanche, A. Goupil, L. Clavier +1
- **PDF**: https://ieeexplore.ieee.org/document/6809154
- **Abstract**: This paper deals with the performance improvement of soft iterative decoders in impulsive interference modeled by additive noise. In case of  $\alpha$-stable noise, the inputs of the belief propagation decoder are too complex to compute. We propose to use an approximation of the log likelihood ratio in an impulsive environment. Even with this simplification, we show that the performance stays close to the one obtained using the true probability density function. Moreover, the robustness of our solution against the parameter estimation is investigated.

## A New Soft Decoding Method for Systematic LT Codes

- **Status**: ✅
- **Reason**: LT(fountain)이나 modified Tanner graph 기반 단순화 soft iterative 디코딩+parity check 종결 기법, 바이너리 LDPC BP에 이식 가능성(C) 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6843089
- **Type**: conference
- **Published**: 2014
- **Authors**: M. Zhang, S. Kim
- **PDF**: https://ieeexplore.ieee.org/document/6843089
- **Abstract**: In this paper, we propose a method to construct the modified Tanner graphs for systematic Luby transform (LT) codes. The modified Tanner graph is drawn in terms of bit nodes and check nodes, instead of encoding nodes and information nodes as in the conventional Tanner graphs for LT codes. By using this modified Tanner graph, we can use a more simplified soft iterative decoding algorithm, and also the decoding performance can be improved, compared to the conventional method. Most importantly, we can simply derive the corresponding parity check equation with the modified Tanner graph, and thus the iterative decoding process can be terminated easily. The average number of iterations can be largely reduced. Simulation results in this paper reveal that our proposed method can achieve better performance than the conventional iterative soft decoding with much less complexity.

## Influences of inaccurate estimation of noise variance in sum-product algorithm for DVB-T2 receiver

- **Status**: ✅
- **Reason**: LDPC sum-product 디코더의 잡음분산 부정확 추정 영향 분석, 상수 SNR 근사 — LLR/디코더 단순화 기법으로 NAND LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6775894
- **Type**: conference
- **Published**: 2014
- **Authors**: S. D. You, S. -J. Huang
- **PDF**: https://ieeexplore.ieee.org/document/6775894
- **Abstract**: The low-density parity check decoder in the digital video broadcasting-second generation terrestrial (DVB-T2) receiver usually uses the sum-product algorithm for better bit error performance. However, the algorithm requires estimating noise variance, which is computationally expensive. In this paper, influences of inaccurate estimation of variance are investigated. Based on the simulation results, it is confirmed that a constant SNR may be used in the algorithm with acceptable performance.

## Hybrid solid-state storage system with storage class memory and NAND flash memory for big-data application

- **Status**: ✅
- **Reason**: NAND 플래시 SSD 신뢰성 신호처리/하이브리드 메모리 솔루션; A 카테고리(NAND 직접) 해당, 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6865318
- **Type**: conference
- **Published**: 2014
- **Authors**: K. Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6865318
- **Abstract**: Big-data enterprise storage is escalating demand for SSD, because of SSD's high speed, low power and small form factor. As a high-speed, low power and highly reliable enterprise storage, this paper overviews the high reliability signal processing technologies and hybrid memory solution which is the best mix and match of the high capacity NAND flash memories and storage class memories with non-volatility, speed, page rewritability and high endurance.

## Writing on dirty flash memory

- **Status**: ✅
- **Reason**: 플래시 메모리 ICI를 dirty paper/결함셀 모델로 보고 additive encoding으로 디코딩 실패확률 개선 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7028498
- **Type**: conference
- **Published**: 2014
- **Authors**: Y. Kim, B. V. K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/7028498
- **Abstract**: The most important challenge in the scaling down of flash memory is its increased inter-cell interference (ICI). If side information about ICI is known to the encoder, the flash memory channel can be viewed as similar to Costa's “writing on dirty paper (dirty paper coding).” We first explain why flash memories are dirty due to ICI. We then show that “dirty flash memory” can be changed into “memory with defective cells” model by using only one pre-read operation. The asymmetry between write and erase operations in flash memory plays an important role in this change. Based on the “memory with defective cells” model, we show that additive encoding can significantly improve the probability of decoding failure by using the side information.

## Fault-Tolerant Probabilistic Gradient-Descent Bit Flipping Decoder

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 확률적 gradient-descent bit-flipping 디코더, 로직게이트 결함 내성 — 이식 가능한 신규 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6868233
- **Type**: journal
- **Published**: 2014
- **Authors**: O. A. Rasheed, P. Ivaniš, B. Vasić
- **PDF**: https://ieeexplore.ieee.org/document/6868233
- **Abstract**: We propose a gradient descent type bit flipping algorithm for decoding low density parity check codes on the binary symmetric channel. Randomness introduced in the bit flipping rule makes this class of decoders not only superior to other decoding algorithms of this type, but also robust to logic-gate failures. We report a surprising discovery that for a broad range of gate failure probability our decoders actually benefit from faults in logic gates which serve as an inherent source of randomness and help the decoding algorithm to escape from local minima associated with trapping sets.

## Status and Recent Advances on Forward Error Correction Technologies for Lightwave Systems

- **Status**: ✅
- **Reason**: Tutorial on LDPC + convolutional/SC-LDPC for optical FEC; tutorial-style but discusses SC-LDPC code developments (E) — save for Phase 3
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6805157
- **Type**: journal
- **Published**: 15 Aug.15,
- **Authors**: Andreas Leven, Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/6805157
- **Abstract**: Since the introduction of coherent transponders, forward error correction based on soft decision is now established in optical communication. In this paper, we give a tutorial-style introduction of one class of commonly used codes, namely low-density parity-check (LDPC) codes. Also we discuss new developments such as convolutional LDPC codes and show how they can be employed as potential candidates for future optical communication systems.

## Simplified variable-scaled min sum LDPC decoder for irregular LDPC codes

- **Status**: ✅
- **Reason**: 반복마다 스케일링 팩터를 적응시키는 variable-scaled min-sum 변형 — 이식 가능 BP 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6940497
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Ahmed A. Emran, Maha Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/6940497
- **Abstract**: Min-Sum decoding is widely used for decoding LDPC codes in many modern digital video broadcasting decoding due to its relative low complexity and robustness against quantization error. However, the suboptimal performance of the Min-Sum affects the integrated performance of wireless receivers. In this paper, we present the idea of adapting the scaling factor of the Min-Sum decoder with iterations through a simple approximation. For the ease of implementation the scaling factor can be changed in a staircase fashion. The stair step is designed to optimize the decoder performance and the required storage for its different values. The variable scaling factor proposed algorithm produces a nontrivial improvement of the performance of the Min-Sum decoding as verified by simulation results.

## Efficient implementation of enhanced min-sum algorithm for DVB-S2 LDPC decoder

- **Status**: ✅
- **Reason**: enhanced min-sum(EMSA) forward-backward 체크노드 업데이트 + 9비트 양자화 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6776078
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Sung Ik Park, Heung Mook Kim, Jeongchang Kim
- **PDF**: https://ieeexplore.ieee.org/document/6776078
- **Abstract**: This paper proposes an efficient implementation of enhanced min-sum algorithm (EMSA) for DVB-S2 LDPC decoding. In order to minimize complexity of check node update, the proposed method uses forward and backward algorithm. Simulation results show that the EMSA does not cause serious performance degradation, as compared with sum-product algorithm when decoder input is 9-bit quantized.

## Improvement on a block-serial fully-overlapped QC-LDPC decoder for IEEE 802.11n

- **Status**: ✅
- **Reason**: QC-LDPC block-serial fully-overlapped 디코더 retiming·message bypassing HW 아키텍처(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6776079
- **Type**: conference
- **Published**: 10-13 Jan.
- **Authors**: Chu Yu, Ho-Sheng Chuang, Bor-Shing Lin +2
- **PDF**: https://ieeexplore.ieee.org/document/6776079
- **Abstract**: This paper presents a block-serial fully-overlapped Quasi-Cyclic Low Density Parity Check (QC-LDPC) decoder for IEEE 802.11n. Based on the circuit retiming and message bypassing techniques, this decoder effectively improved the previous work proposed by Xiang et al. with an 11% clock-rate increase and a 3% decoding time reduction on average. Moreover, the proposed chip spends about 3.67 mm in 90 nm CMOS technology, its power approximately consumes 171 mW at 250 MHz, and throughput of the proposed design can reach 672 Mbps.

## Pilot-Tone Assisted Log-Likelihood Ratio for LDPC Coded CO-OFDM System

- **Status**: ✅
- **Reason**: LDPC 코딩 CO-OFDM용 신규 LLR metric(PT-LLR) 제시 — 광 위상잡음 특이지만 새 LLR 산출이라 Phase 3 재검토 위해 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6826532
- **Type**: journal
- **Published**: 1 Aug.1, 2
- **Authors**: Shengjiao Cao, Pooi-Yuen Kam, Changyuan Yu +1
- **PDF**: https://ieeexplore.ieee.org/document/6826532
- **Abstract**: Pilot-tone assisted log-likelihood ratio (PT-LLR) is derived for low-density parity-check coded, coherent optical orthogonal frequency division multiplexing systems in the presence of linear phase noise. The knowledge of common phase error (CPE) obtained from the pilot-tone is incorporated into the new LLR metric, which eliminates the need for prior CPE estimation and compensation. We compare our metric with the conventional LLR (C-LLR) through extensive simulation using their approximate versions (APT-LLR, AC-LLR). APT-LLR has the same order of complexity as AC-LLR while it outperforms AC-LLR for higher order modulation formats (16-QAM, 64-QAM) at smaller pilot-tone-to-signal power ratios. In addition, we show that with the help of time-domain blind intercarrier interference mitigation, both metrics perform better in the presence of larger laser linewidth.
