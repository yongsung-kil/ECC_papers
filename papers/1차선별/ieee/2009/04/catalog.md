# IEEE Xplore — 2009-04 (1차선별 통과)


## High-Throughput Layered LDPC Decoding Architecture

- **Status**: ✅
- **Reason**: QC-LDPC 고처리율 layered 디코더 HW, row permutation/shuffle network 최적화 — 이식 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4773145
- **Type**: journal
- **Published**: April 2009
- **Authors**: Zhiqiang Cui, Zhongfeng Wang, Youjian Liu
- **PDF**: https://ieeexplore.ieee.org/document/4773145
- **Abstract**: This paper presents a high-throughput decoder architecture for generic quasi-cyclic low-density parity-check (QC-LDPC) codes. Various optimizations are employed to increase the clock speed. A row permutation scheme is proposed to significantly simplify the implementation of the shuffle network in LDPC decoder. An approximate layered decoding approach is explored to reduce the critical path of the layered LDPC decoder. The computation core is further optimized to reduce the computation delay. It is estimated that 4.7 Gb/s decoding throughput can be achieved at 15 iterations using the current technology.

## Memory-efficient and high-throughput decoding of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC용 turbo-sum-product/shuffled-SP 디코딩 알고리즘, 빠른 수렴·저메모리 부분병렬 — 이식 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4814348
- **Type**: journal
- **Published**: April 2009
- **Authors**: Yongmei Dai, Zhiyuan Yan, Ning Chen
- **PDF**: https://ieeexplore.ieee.org/document/4814348
- **Abstract**: We propose turbo-sum-product (TSP) and shuffled-sum-product (SSP) decoding algorithms for quasi-cyclic low-density parity-check codes, which not only achieve faster convergence and better error performance than the sum-product algorithm, but also require less memory in partly parallel decoder architectures. Compared with the turbo decoding algorithm, our TSP algorithm saves the same amount of memory and may achieve a higher decoding throughput. The convergence behaviors of our TSP and SSP algorithms are also compared with those of the SP, turbo, and shuffled algorithms by their extrinsic information transfer (EXIT) charts.

## Hybrid burst erasure correction of LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC 버스트 소거 정정을 위한 패리티검사 증강 기법 - 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4815076
- **Type**: journal
- **Published**: April 2009
- **Authors**: Marc Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/4815076
- **Abstract**: In this letter, burst erasure correction of low density parity check codes based on a hybrid approach is presented. The proposed method preserves as much as possible the original low density representation and augments it by specific check sums judiciously selected.

## Fault Secure Encoder and Decoder for NanoMemory Applications

- **Status**: ✅
- **Reason**: 메모리용 EG-LDPC fault-secure 인코더/디코더, 바이너리 LDPC 코드설계·HW 기여(B/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4796210
- **Type**: journal
- **Published**: April 2009
- **Authors**: Helia Naeimi, AndrÉ DeHon
- **PDF**: https://ieeexplore.ieee.org/document/4796210
- **Abstract**: Memory cells have been protected from soft errors for more than a decade; due to the increase in soft error rate in logic circuits, the encoder and decoder circuitry around the memory blocks have become susceptible to soft errors as well and must also be protected. We introduce a new approach to design fault-secure encoder and decoder circuitry for memory designs. The key novel contribution of this paper is identifying and defining a new class of error-correcting codes whose redundancy makes the design of fault-secure detectors (FSD) particularly simple. We further quantify the importance of protecting encoder and decoder circuitry against transient errors, illustrating a scenario where the system failure rate (FIT) is dominated by the failure rate of the encoder and decoder. We prove that Euclidean geometry low-density parity-check (EG-LDPC) codes have the fault-secure detector capability. Using some of the smaller EG-LDPC codes, we can tolerate bit or nanowire defect rates of 10% and fault rates of 10-18 upsets/device/cycle, achieving a FIT rate at or below one for the entire memory system and a memory density of 1011 bit/cm2 with nanowire pitch of 10 nm for memory blocks of 10 Mb or larger. Larger EG-LDPC codes can achieve even higher reliability and lower area overhead.

## Cross-Layer Iterative Decoding of Irregular LDPC Codes using Cyclic Redundancy Check Codes

- **Status**: ✅
- **Reason**: LDPC+CRC 교차계층 반복 디코더로 error-floor 저감 (C 디코더 개선, BP에 이식 가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4917653
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Zhimin Yang, Shiju Li, Hao Feng +2
- **PDF**: https://ieeexplore.ieee.org/document/4917653
- **Abstract**: This paper presents a cross-layer iterative decoder for irregular low-density parity-check (LDPC) codes which uses cyclic redundancy check (CRC) codes. The key idea of the decoder is to use correctly decoded frames as an aid for correcting the remaining erroneous frames. To accomplish this, the decoder exchanges the relevant information between layers by using the cross-layer design method and an iterative decoding architecture. Moreover, the unequal-error protection (UEP) property of irregular LDPC is exploited and both the multiple-error detection and single-error correction capabilities of the CRC code are used. Simulation results show that the proposed decoder outperforms the pure sum-product algorithm (SPA) decoder by a considerable gain while the increase in complexity is moderate. Furthermore, the error floor of irregular LDPC codes in the high Eb/NO regime can be lowered effectively. The proposed cross-layer iterative decoder can be used for any irregular LDPC coded wireless system to boost the performance and lower the error floor.

## Thresholds Calculation of LDPC Code Ensembles Using a Novel Gaussian Approximation Algorithm

- **Status**: ✅
- **Reason**: sum-product 디코딩 임계값 계산용 새 Gaussian approximation 알고리즘 - 이식 가능 코드설계/분석 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4917989
- **Type**: conference
- **Published**: 5-8 April 
- **Authors**: Piming Ma, Kyungsup Kwak
- **PDF**: https://ieeexplore.ieee.org/document/4917989
- **Abstract**: A novel Gaussian approximation algorithm is proposed for calculating the thresholds of low-density parity- check (LDPC) code ensembles under sum-product decoding. The updating rules of means and error probability are derived. Numerical results show that the thresholds obtained by the proposed algorithm closely coincide with the values computed by density evolution (DE). Moreover, our algorithm can calculate the thresholds of irregular LDPC codes with higher accuracy than the algorithm proposed by Lehmann and Maggio.

## QC-LDPC codes and their performance on Power Line Communications Channel

- **Status**: ✅
- **Reason**: QC-LDPC에 BP+개선된 bit-flipping의 하이브리드 디코딩 기법 제안(C), 도메인은 PLC지만 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4913437
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Nikoleta Andreadou, Fotini-Niovi Pavlidou
- **PDF**: https://ieeexplore.ieee.org/document/4913437
- **Abstract**: In this paper Low Density Parity Check Codes (LDPC) are introduced in the Power Line Communications Channel (PLC). We investigate how different decoding algorithms, which are applied on LDPC codes, affect the system's performance. Therefore, an iterative belief propagation decoding algorithm as well as a proposed variation of the original bit flipping algorithm are exploited. In addition, a hybrid technique combining these two algorithms is proposed. Irregular LDPC codes of various code rates are studied. Specifically, the cases of 1/2, 1/3, 2/3, 3/4 and 4/5 code rates are investigated. Regarding the irregular LDPC codes, they are constructed in a Quasi-Cyclic form. The system's performance is expressed in terms of the resultant Bit Error Rate (BER) versus the Signal to Noise Ratio (SNR). In order to design the power line communications channel, Middleton's class A noise model is used to account for the system's background and impulsive noise, while Zimmermann's channel model is also used. The OFDM transmission technique is taken into account. Results are derived via computer simulations.

## Multi-Rate QC-LDPC Encoder

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 HW(SRAA 기반 메모리 효율)—이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4960843
- **Type**: conference
- **Published**: 28-29 Apri
- **Authors**: Huxing Zhang, Hongyang Yu
- **PDF**: https://ieeexplore.ieee.org/document/4960843
- **Abstract**: A multi-rate memory-efficient encoder for low-density parity-check (LDPC) codes is proposed in this paper based on shift-register-adder-accumulator (SRAA). The SRAA algorithm simplifies the encoder computation module and reduces the complexity of the operation. The LDPC code generator matrix is constructed by lots of quasi-cyclic square matrices in the Chinese digital TV terrestrial broadcasting standard (DMB-T), and the encoder is presented based on the quasi-cyclic character that reduces the memory cost. Simulations demonstrate that the proposed encoder can satisfy the DMB-T in three-rate according to different bit-rate option with lower complexity.

## Modified Iterative Two-Stage Hybrid Decoding Algorithm for Low-Density Parity-Check (LDPC) Codes

- **Status**: ✅
- **Reason**: LDPC 2단 하이브리드 디코딩(soft+hard, 수정 IERRWBF 비트플립) - 부호 비의존 바이너리 LDPC 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5073688
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Hany R. Zeidan, Maha M. Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/5073688
- **Abstract**: This paper considers a modified iterative version of the two-stage hybrid algorithm for decoding low-density parity- check (LDPC) codes. The hybrid-decision scheme is a decoding scheme used that combines two iterative decoding algorithms for decoding LDPC codes. This scheme is suitable for many applications such as audio and video transmission that are sensitive to time. The hybrid-decision scheme mixes between the characteristics of the soft-decision decoding scheme and the hard- decision decoding scheme to reduce the computational complexity of the whole decoding algorithm. The modification proposed in this paper is applied to the implementation-efficient reliability ratio weighted bit-flipping (IERRWBF) algorithm which represents hard-decision scheme in the hybrid algorithm. This modification is capable of achieving better performance than that of the hybrid decoding algorithm with reducing the number of iterations required at each SNR and approaching more to the performance of the SPA. This reduction is more observable as the maximum number of iterations assigned for the algorithm increases or as the code length increases with improving the error performance as proved by simulation results.

## Symbol-Based Belief Propagation Decoding of Reed-Solomon Codes

- **Status**: ✅
- **Reason**: RS용 symbol-based BP에 reliability 기반 패리티검사행렬 적응 제안 - 비-LDPC지만 적응적 PCM/BP 메시지패싱 기법이 LDPC BP에 이식 가능성 있어 애매하게 살림(Phase3)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5073872
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: C. Zhong, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/5073872
- **Abstract**: We propose a symbol-based belief propagation (BP) algorithm for iterative soft-decision decoding of Reed-Solomon (RS) codes. Complexity reduction is achieved by using a fast Fourier transform (FFT)-based BP algorithm. Parity-check matrix adaptation based on the reliability of the codeword symbols is an essential step to make the BP algorithm effective on high-density parity-check matrices characteristic of RS codes. The matrix adaptation, as well as all other operations, is performed at symbol level such that bit-to-symbol and symbol-to- bit conversions are avoided. A moderate coding gain over algebraic hard-decision decoding is achieved on additive white Gaussian noise channels. The symbol-based algorithm presented in this paper addresses the main weakness of its bit-based counterpart, namely the prohibitively high complexity for practical applications that use long codes and large finite fields, albeit with less coding gain.

## Low Complexity DVB-S2 LDPC Decoder

- **Status**: ✅
- **Reason**: DVB-S2 LDPC 저복잡도 디코더, 새 row message-passing offset min-sum + 노드 업데이트/메모리 최적화 - C/D 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5073653
- **Type**: conference
- **Published**: 26-29 Apri
- **Authors**: Botao Zhang, Hengzhu Liu, Xucan Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/5073653
- **Abstract**: The decoding complexity is the main issue in designing DVB-S2 Low Density Parity Check (LDPC) decoder. This paper proposes a low complexity decoder, which is based on a new row message passing Offset Min-Sum algorithm. The proposed algorithm can reduce the complexity of the decoder with no performance loss. The simplified node update units based on the proposed algorithm and the memory organization optimized across different code rates play the key role in reducing the complexity. The synthesized area of the decoder is 9.6 mm2 in Chartered 90 nm COMS technology. When the code rate is 9/10 and the work frequency is 320 MHz, the net throughput of the decoder is 998 Mbps.

## Analysis of threshold of regular and irregular LDPC codes using Gaussian approximation

- **Status**: ✅
- **Reason**: Gaussian approximation으로 regular/irregular LDPC threshold 분석 — 코드설계/density evolution 기법(E), 유한길이 설계에 활용 가능하나 순수 분석성이라 애매→살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5068932
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Chia-Lu Ho
- **PDF**: https://ieeexplore.ieee.org/document/5068932
- **Abstract**: We present the formulas for searching for the thresholds of regular and irregular low-density parity-check (LDPC) codes under message-passing (MP) algorithm. A Gaussian approximation is applied to studying the evolution of the means of the messages of the variable nodes and the check nodes. Accurate numerical integration methods by using transformations are shown for evaluating the expected values of the message of the check nodes. Tables are built first and interpolations are used for further evaluations. Two curves are used to locate the threshold. We utilize an iterative decoding tunnel between these two curves and study the decoding performance by evaluating conditions of the derivatives of these two curves. Using this method the performance of both regular and irregular LDPC codes can be studied in a unified manner without using simulation.

## Cooperative relay channel with LDPC codes constructed from array codes

- **Status**: ✅
- **Reason**: array code 기반 LDPC 구성으로 가변 girth 달성, QC-LDPC 대비 성능 개선 — 바이너리 코드설계 기법(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5068956
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Mingkwan Somphruek, Rolando Carrasco, Stephane Le Goff
- **PDF**: https://ieeexplore.ieee.org/document/5068956
- **Abstract**: Cooperative communication represents a new class of diversity techniques in which multiple nodes each with a single antenna cooperate to generate a virtual multiple-antenna transmission system and thus offer the benefits of spatial diversity. This paper proposes suitable array codes used as low-density parity-check (LDPC) codes to be applied in the cooperative amplify-and-forward (AF) network. A mathematical description of the construction of suitable array codes for a relay fading channel is also presented. Compared with quasi-cyclic (QC) LDPC codes, the array codes have similar encoding complexity and can adaptively generate various desired girth values. This paper shows that array codes with large girths can achieve substantial system performance improvements. Simulation results in this paper show that using array codes as LDPC codes for cooperative relay transmission provides a significant performance improvement over direct transmission. Moreover, it is also shown that its performance is superior to some structured LDPC codes such as QC-LDPC codes, particularly, a coding gain of about 1dB at BER of 10-3 can be provided over its counterpart.

## Fast Parallel Weighted Bit Flipping decoding algorithm for LDPC codes

- **Status**: ✅
- **Reason**: Fast Parallel Weighted Bit Flipping(PWBF) 디코더 — guaranteed bit로 계산 복잡도 감소, 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5068982
- **Type**: conference
- **Published**: 22-24 Apri
- **Authors**: Miroslav Vanek, Peter Farkas
- **PDF**: https://ieeexplore.ieee.org/document/5068982
- **Abstract**: In this paper a fast version of the parallel weighted bit flipping LDPC decoding algorithm (PWBF) is presented. The idea, which allowed decreasing the computational complexity of the PWBF method, is based on the observation that in dependency on signal to noise ratio, many of the received bits in the codeword of LDPC code could be without error. The augmented algorithm makes tests based on syndromes and symbol involvement in parity checks, which are given by the factor graph corresponding to the chosen LDPC code in order to define so called guaranteed bits. These guaranteed bits do not participate in the decoding calculations further. Simulation results are presented, which show that there is not visible any significant performance deterioration by application of this method and that the approximate speed up of the decoding for the tested codes is about 25% on the selected hardware in comparison with the known PWBF.

## A generic architecture of CCSDS Low Density Parity Check decoder for near-earth applications

- **Status**: ✅
- **Reason**: CCSDS QC-LDPC 디코더 제네릭 FPGA 아키텍처 — 병렬화·최적 데이터 저장 HW 기법, NAND LDPC 디코더 HW로 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5090854
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Fabien Demangel, Nicolas Fau, Nicolas Drabik +2
- **PDF**: https://ieeexplore.ieee.org/document/5090854
- **Abstract**: Low Density Parity Check (LDPC) codes have recently been chosen in the CCSDS standard for uses in near-earth applications. The specified code belongs to the class of Quasi-Cyclic LDPC codes which provide very high data rates and high reliability. Even if these codes are suited to high data rate, the complexity of LDPC decoding is a real challenge for hardware engineers. This paper presents a generic architecture for a CCSDS LDPC decoder. This architecture uses the regularity and the parallelism of the code and a genericity based on an optimized storage of the data. Two FPGA implementations are proposed: the first one is low-cost oriented and the second one targets high-speed decoder.

## A novel LDPC decoder for DVB-S2 IP

- **Status**: ✅
- **Reason**: Gauss-Seidel LDPC 디코더+lambda-Min 변형으로 메모리/면적 절감, 부호비의존 디코더·HW 기법 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5090867
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Stefan Muller, Manuel Schreger, Marten Kabutz +3
- **PDF**: https://ieeexplore.ieee.org/document/5090867
- **Abstract**: In this paper a programmable Forward Error Correction (FEC) IP for a DVB-S2 receiver is presented. It is composed of a Low-Density Parity Check (LDPC), a Bose-Chaudhuri-Hoquenghem (BCH) decoder, and pre- and postprocessing units. Special emphasis is put on LDPC decoding, since it accounts for the most complexity of the IP core by far. We propose a highly efficient LDPC decoder which applies Gauss-Seidel decoding. In contrast to previous publications, we show in detail how to solve the well known problem of superpositions of permutation matrices. The enhanced convergence speed of Gauss-Seidel decoding is used to reduce area and power consumption. Furthermore, we propose a modified version of the lambda-Min algorithm which allows to further decrease the memory requirements of the decoder by compressing the extrinsic information. Compared to the latest published DVB-S2 LDPC decoders, we could reduce the clock frequency by 40% and the memory consumption by 16%, yielding large energy and area savings while offering the same throughput.

## Accelerating FPGA-based emulation of quasi-cyclic LDPC codes with vector processing

- **Status**: ✅
- **Reason**: QC-LDPC용 벡터화 overlapped message passing FPGA 아키텍처, 병렬 디코더 HW 기법 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5090905
- **Type**: conference
- **Published**: 20-24 Apri
- **Authors**: Xiaoheng Chen, Jingyu Kang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/5090905
- **Abstract**: FPGAs are widely used for evaluating the error-floor performance of LDPC (low-density parity check) codes. We propose a scalable vector decoder for FPGA-based implementation of quasi-cyclic (QC) LDPC codes that takes advantage of the high bandwidth of the embedded memory blocks (called Block RAMs in a Xilinx FPGA) by packing multiple messages into the same word. We describe a vectorized overlapped message passing algorithm that results in 3.5times to 5.5times speedup over state-of-the-art FPGA implementations in literature.

## Log-likelihood ratio clipping in MIMO-BICM systems: Information geometric analysis and impact on system capacity

- **Status**: ✅
- **Reason**: MIMO-BICM LLR 클리핑의 정보기하 분석+LLR 변환 기법 — LLR 양자화/클리핑은 NAND LDPC LLR 처리(A/C)에 이식 여지, 애매하니 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4960113
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Stefan Schwandter, Peter Fertl, Clemens Novak +1
- **PDF**: https://ieeexplore.ieee.org/document/4960113
- **Abstract**: The clipping of log-likelihood ratios (LLRs) in soft demodulators for multiple-input multiple-output (MIMO) systems with bit-interleaved coded modulation (BICM) was recently observed to allow for enormous complexity savings. In this paper we first provide an information-geometric interpretation of LLR clipping as information projection onto a log-convex manifold. Then we study the system capacity of MIMO-BICM systems that use LLR clipping. Our results show that strong LLR clipping is possible without significant capacity loss. We finally propose an LLR transformation scheme which is necessary for approaching capacity in case of strong clipping. The usefulness of this LLR transformation is illustrated by numerical simulations for MIMO-BICM systems employing low-density parity check (LDPC) codes.
