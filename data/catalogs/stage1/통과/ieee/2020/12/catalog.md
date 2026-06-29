# IEEE Xplore — 2020-12 (1차선별 통과)


## A Flexible and High Parallel Permutation Network for 5G LDPC Decoders

- **Status**: ✅
- **Reason**: D: 5G QC-LDPC용 고병렬 permutation network 신규 HW — 디코더 셔플 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9117061
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Zhiwei Zhong, Yongming Huang, Zaichen Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9117061
- **Abstract**: Cyclic shifting is usually applied in quasi-cyclic low-density parity-check (QC-LDPC) decoders for permutation operations. In this brief, we propose a flexible and high parallel permutation network for QC-LDPC decoders in the 5th generation (5G) communication systems, which supports LDPC codes with arbitrary code lengths and all lifting sizes in 5G standards. The proposed permutation network can cyclically shift at most 128 frames of data in parallel, which greatly improves the hardware efficiency and decoding throughput. Based on the TSMC 90-nm CMOS technology, synthesis results illustrate the superiority of the proposed design.

## Flexible High Throughput QC-LDPC Decoder With Perfect Pipeline Conflicts Resolution and Efficient Hardware Utilization

- **Status**: ✅
- **Reason**: D/C: QC-LDPC 디코더 파이프라인 해저드 해소 신규 아키텍처+스케줄 GA 최적화 — 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9179021
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Vladimir L. Petrović, Miloš M. Marković, Dragomir M. El Mezeni +2
- **PDF**: https://ieeexplore.ieee.org/document/9179021
- **Abstract**: Modern communication standards, such as 5G new radio (5G NR), require a high speed decoder for highly irregular quasi-cyclic low density parity check (QC-LDPC) codes. A widely used approach in QC-LDPC decoders is a layered decoding schedule which processes the parity check matrix in parts, thus providing faster convergence. However, pipelined layered decoding architecture suffers from data hazards that reduce the throughput. This paper presents a novel architecture, which can facilitate any QC-LDPC decoding without stall cycles caused by pipeline hazards. The decoder conveniently incorporates both the layered and the flooding schedules in cases when hazards occur. The paper also presents the genetic algorithm based optimization of the decoding schedule for better signal-to-noise ratio (SNR) performance. The proposed architecture enables insertion of a large number of pipeline stages, thus providing high operating frequency. As a case study, the FPGA implementation for WiMAX, DVB-S2X, and 5G NR provided coded throughput of up to 1.77 Gbps, 4.32 Gbps, and 4.92 Gbps at 10 iterations, respectively. The results show a strong throughput increase of 30%-109% compared with the conventional layered decoder for 5G NR for the same SNR performance. The decoder provides highly efficient utilization of resources when compared with the state-of-the-art solutions.

## A High-Performance Stochastic LDPC Decoder Architecture Designed via Correlation Analysis

- **Status**: ✅
- **Reason**: C/D: stochastic LDPC 디코더 신규 VN 구조·아키텍처 — 디코더/HW 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9126828
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Qichen Zhang, Yun Chen, Shixian Li +2
- **PDF**: https://ieeexplore.ieee.org/document/9126828
- **Abstract**: This paper presents an area-efficient architecture for stochastic low-density parity-check (LDPC) decoder with high throughput and excellent bit-error-rate (BER) performance. The correlation effects of a stochastic Sum-Product Algorithm (SPA) are analyzed. Based on this analysis, a variable node (VN) structure is proposed and its similarity with a correlation divider (CORDIV) is pointed out. Based on the properties of CORDIV, the area of probability tracer in the VN is reduced significantly. In order to achieve more accurate results when the check-to-variable (C2V) messages are not strong enough, the 3-3 input grouping sub-node is replaced by an adder-based 5-1 input grouping sub-node of the degree-6 VN for (2048,1723) code. An unbiased stochastic sequence generator is adopted to get more accurate results from the smaller probability tracer. Furthermore, the soft bit-flipping prior-processing and the C2V-based hard decision updating method are combined in VN to reduce the decoding latency. A (2048,1723) stochastic LDPC decoder is designed in the TSMC 65 nm process to demonstrate the proposed decoder architecture. With the aid of early termination, the decoder occupies 2.34 mm2 core area and can achieve 116.17 Gb/s at 4.4 dB and 461.99 Gb/s at 5.5 dB under 970 MHz with better decoding performance. Compared with the state-of-the-art stochastic IEEE 802.3an LDPC decoders, the proposed architecture can achieve the best throughput, throughput-to-area ratio, and BER performance.

## Exploiting Error Characteristic to Optimize Read Voltage for 3-D NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND read voltage 최적화·RBER 저감(A) NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9241228
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Meng Zhang, Fei Wu, Qin Yu +3
- **PDF**: https://ieeexplore.ieee.org/document/9241228
- **Abstract**: 3-D NAND flash memory has become increasingly popular nonvolatile storage devices due to large capacity and high performance. With the increase of program/erase (P/E) cycles and retention periods, the threshold voltage distribution of 3-D NAND flash memory is prone to shift such that it is difficult to accurately obtain the read reference voltage (RRV). When reading data, read retry operations perform multiple flash sensing to read bit information correctly, inducing extended read latency. To mitigate the read latency, a method of precisely acquiring the RRV is urgently needed. Using an field-programmable gate array (FPGA) hardware testing platform, this article first studies error characteristics of 3-D triple-level cell (TLC) NAND flash memory with the floating gate (FG) structure, which includes the variations of raw bit error rates (RBERs) in different layers and pages, the variations of block reads under different read modes, and the threshold voltage shifting characteristic. Then, based on these characterizations, this article develops an error characteristic aware RRV acquisition scheme, called ECRRV, to gain optimal RRV by exploiting the least square method. Experimental results show that the proposed scheme can significantly diminish the RBER and block read count.

## Fully Parallel Circular-Shift Rotation Network for Communication Standards

- **Status**: ✅
- **Reason**: D: 새 permutation network(circular-shift rotation) HW 설계 — QC-LDPC 디코더에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9099895
- **Type**: journal
- **Published**: Dec. 2020
- **Authors**: Hassan Harb, Cyrille Chavet
- **PDF**: https://ieeexplore.ieee.org/document/9099895
- **Abstract**: This brief sheds light on a formal approach to design an innovative class of permutation network called Fully Parallel Circular-shift rotation Network. Thus, the contribution of such a design is the capability to process - in parallel - more than one set of elements with different lengths and permutation constraints. Yet, processing several sets simultaneously, arises from the increasing demand for higher throughput rate for applications such as the incoming 5G codes. Furthermore, the ability to handle several different sets of elements in parallel reduces the number of idled components in the designs (which improves the $performances/area$ ratio). Meanwhile, independent circular-shifter network blocks are generated in order to process the different sets simultaneously. Hence, the cost in terms of number of Multiplexers (MUXs) is low compared to the best existing works we know in the state-of-the-art, with the same number of stages.

## A Reconstruction-Computation-Quantization (RCQ) Approach to Node Operations in LDPC Decoding

- **Status**: ✅
- **Reason**: LDPC 유한정밀(4비트) RCQ 디코더 + HDQ 양자화 설계 — min-sum/BP 근사 디코더 및 LLR 양자화 기법, NAND 이식성 높음(C/A).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9348139
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Linfang Wang, Richard D. Wesel, Maximilian Stark +1
- **PDF**: https://ieeexplore.ieee.org/document/9348139
- **Abstract**: This paper proposes a finite-precision decoding method for low-density parity-check (LDPC) codes that features the three steps of Reconstruction, Computation, and Quantization (RCQ). Unlike Mutual-Information-Maximization Quantized Belief Propagation (MIM-QBP), RCQ can approximate either belief propagation or Min-Sum decoding. MIM-QBP decoders do not work well when the fraction of degree-2 variable nodes is large. However, sometimes a large fraction of degree-2 variable nodes is used to facilitate a fast encoding structure, as seen in the IEEE 802.11 standard and the DVB-S2 standard. In contrast to MIM-QBP, the proposed RCQ decoder may be applied to any off-the-shelf LDPC code, including those with a large fraction of degree-2 variable nodes. Simulations show that a 4-bit Min-Sum RCQ decoder delivers frame error rate (FER) performance within 0.1 dB of floating point belief propagation (BP) for the IEEE 802.11 standard LDPC code in the low SNR region. The RCQ decoder actually outperforms floating point BP and Min-Sum in the high SNR region were FER less than 10-5. This paper also introduces Hierarchical Dynamic Quantization (HDQ) to design the time-varying non-uniform quantizers required by RCQ decoders. HDQ is a low-complexity design technique that is slightly sub-optimal. Simulation results comparing HDQ and optimal quantization on the symmetric binary-input memoryless additive white Gaussian noise channel show a mutual information loss of less than 10-6 bits, which is negligible in practice.

## MCMC Decoding of LDPC Codes with BP Preprocessing

- **Status**: ✅
- **Reason**: 단블록 LDPC용 BP-MCMC 하이브리드 디코더 — 새 디코더 알고리즘 기여(C). 바이너리.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9348002
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Jiun-Ting Huang, Young-Han Kim
- **PDF**: https://ieeexplore.ieee.org/document/9348002
- **Abstract**: Monte Carlo Markov chain (MCMC) decoding is a randomized algorithm which has been proven to be near-optimal in terms of decoding error probability. However, the exponentially slow mixing rate of Markov chains seems to preclude MCMC decoding from applications concerning even short blocklength codes. In contrast, belief propagation (BP) is a deterministic algorithm that is empirically fast but sub-optimal in error rate when it is used to decode low-density parity-check (LDPC) codes. In this paper, a code-independent BP-MCMC hybrid decoder is devised for short-blocklength LDPC codes. Theoretical error analysis of the hybrid algorithm is provided. Preliminary experiments show that the preprocessing of BP successfully reduces the time complexity of MCMC decoding and hence significantly improves the applicability of MCMC decoders to short LDPC codes.

## On the Design of Generalized LDPC Codes with Component BCJR Decoding

- **Status**: ✅
- **Reason**: GLDPC 코드 설계 + trellis BCJR 비트단위 컴포넌트 디코더 최적화로 새 코드설계/디코더 기여(E/C). 바이너리.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9322143
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Yanfang Liu, Pablo M. Olmos, David G. M. Mitchell
- **PDF**: https://ieeexplore.ieee.org/document/9322143
- **Abstract**: Generalized low-density parity-check (GLDPC) codes, where the single parity-check (SPC) nodes are replaced by generalized constraint (GC) nodes, are known to offer a reduced gap to capacity when compared with conventional LDPC codes, while also maintaining linear growth of minimum distance. However, for certain classes of practical GLDPC codes, there remains a gap to capacity even when utilizing blockwise decoding algorithm at GC nodes. In this work, we propose to optimize the design of GLDPC codes where the GC nodes are decoded with a trellis-based bit-wise Bahl-Cocke-Jelinek- Raviv (BCJR) component decoding algorithm. We analyze the asymptotic threshold behavior of GLDPC codes and determine the optimal proportion of the GC nodes in the GLDPC Tanner graph.We show significant performance improvements compared to existing designs with the same order of decoding complexity.

## Approximated EM Algorithms for Estimation of Unknown Coded Discrete Memoryless Channels

- **Status**: ✅
- **Reason**: 플래시 메모리 채널(양자화 Normal-Laplace) 대상 LDPC sum-product/min-sum 기반 채널추정 근사 — NAND 채널 직접+min-sum 변형(A/C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9322183
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Naoaki Kokubun, Daiki Watanabe, Hironori Uchikawa +1
- **PDF**: https://ieeexplore.ieee.org/document/9322183
- **Abstract**: Mismatch between the true channel and the channel assumed in the design of a communication system can degrade system performance. Joint channel estimation and data recovery via the Expectation-Maximization (EM) algorithm can overcome this problem. Though stable, the EM algorithm can be complex to implement and can exhibit slow convergence. We present approximations of the EM algorithm that reduce computational complexity and accelerate convergence for LDPC-coded discrete memoryless channels. In place of the exact bit-wise maximum a posteriori probability decoder in the E step of the EM algorithm, we use the sum-product decoder and min-sum decoder. In the M step, we use hard information instead of soft information to estimate the channel parameter. In order to evaluate the approximations in a practical channel mismatch scenario, we use a flash memory channel described by a quantized Normal-Laplace mixture model. The simulation results demonstrate that the approximations in the E step can estimate the true channel with low-complexity decoding and those in the M step can accelerate the convergence with reduced measurement precision.

## Refined Belief-Propagation Decoding of Quantum Codes with Scalar Messages

- **Status**: ✅
- **Reason**: 양자코드용 BP지만 스칼라 메시지로 binary BP 복잡도 달성+message normalization+serial schedule 개선 — 고전 바이너리 BP에서 유래한 이식 가능 디코더 기법(C), 예외 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9367482
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Kao-Yueh Kuo, Ching-Yi Lai
- **PDF**: https://ieeexplore.ieee.org/document/9367482
- **Abstract**: Codes based on sparse matrices have good performance and can be efficiently decoded by belief-propagation (BP). Decoding binary stabilizer codes needs a quaternary BP for (additive) codes over GF(4), which has a higher check-node complexity compared to a binary BP for codes over GF(2). Moreover, BP decoding of stabilizer codes suffers a performance loss from the short cycles in the underlying Tanner graph. In this paper, we propose a refined BP algorithm for decoding quantum codes by passing scalar messages. For a given error syndrome, this algorithm decodes to the same output as the conventional quaternary BP but with a check-node complexity the same as binary BP. As every message is a scalar, the message normalization can be naturally applied to improve the performance. Another observation is that the message-update schedule affects the BP decoding performance against short cycles. We show that running BP with message normalization according to a serial schedule (or other schedules) may significantly improve the decoding performance and error-floor in computer simulation.

## Spatial Coupling In Turbo Equalization

- **Status**: ✅
- **Reason**: 스페이셜 커플링(SC) 코드로 waterfall/error-floor 트레이드오프 해소, window decoder 활용 — E(코드설계) 이식 가능, 바이너리 LDPC 계열
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9348218
- **Type**: conference
- **Published**: 7-11 Dec. 
- **Authors**: Mgeni Makambi Mashauri, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/9348218
- **Abstract**: In this paper we consider spatial coupling in turbo equalization and demonstrate that the code design trade-off between the performance in waterfall and error floor regions can be avoided. We introduce three coupling schemes and compare their performances, where the first method introduces coupling between the encoder and the channel, while the second uses a spatially coupled (SC) code. In the third scheme we use both a coupled code and couple between the code and the channel. We show by computer simulations that, with spatial coupling, we can have good performance in both the error floor and the waterfall region with reasonable decoding latency by using a window decoder. We show this for both the maximum a posteriori (MAP) and linear minimum mean square (MMSE) equalizers.

## An Evaluation of Design Framework for Min-Sum Irregular LDPC Decoders

- **Status**: ✅
- **Reason**: Min-Sum 비정칙 LDPC 디코더의 범용 설계 프레임워크+회로면적 절감 — D(HW 아키텍처) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9306369
- **Type**: conference
- **Published**: 7-10 Dec. 
- **Authors**: Jimpu Suzuki, Hiroshi Tsutsui, Takeo Ohgane
- **PDF**: https://ieeexplore.ieee.org/document/9306369
- **Abstract**: Design of LDPC decoder depends on its check matrix. Since there exist a lot of check matrices with various sizes, it is not feasible to design a dedicated LDPC decoder for each check matrix. This work aims to make a versatile design framework to generate an LDPC decoder for each given check matrix. We consider a method to reduce the circuit area, focusing on the feature of the check matrix of 5G. In this paper, we present evaluation results of our framework, including gate count evaluations. We evaluated circuit areas of the decoders conforming to 5G. In the case of a check matrix where the number of information bits is about 120, the number of gates is about 3.7 M gates.

## LDPC Decoder Based on Chisel

- **Status**: ✅
- **Reason**: AA-LDPC 디코더 HW 아키텍처: 4-cycle 회피 H생성+TDMP/Log-Map, 메모리 6/8bit 양자화 절감, 이식 가능 HW/디코더(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9353021
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Bingrui Wu
- **PDF**: https://ieeexplore.ieee.org/document/9353021
- **Abstract**: This paper proposes a sparse check matrix H generation method and a regular AA-LDPC (architecture-aware low-density parity-check) code decoder architecture. The generated H matrix is suitable for regular LDPC codes, avoiding the appearance of four-line loops. The decoder uses TDMP (turbo-decoding message-passing) and Log-Map algorithms, which can achieve faster convergence speed and higher throughput compared with traditional decoding algorithms. Use the scoreboard algorithm to solve the problem of data conflict between TDMP algorithm initialization and the first iteration. Extrinsic messages and posterior messages are stored in 6bit and 8bit respectively, the memory usage is reduced by more than 60% compared with the traditional method, and the chip area is reduced. The decoder module is written in high-level Chisel language, which effectively improves the development efficiency compared with verilog. Uvm (Universal Verification Methodology) was used to randomly generate 10,000 stimuli to verify the verilog code generated by Chisel. With a clock frequency of 290MHz, this architecture can decode any regular AA-LDPC(3, 27) code with a code rate of 8/9 9216-bit, with ten iterations and a data throughput rate of 450Mbps.

## Optimizing Parametrized Information Bottleneck Compression Mappings with Genetic Algorithms

- **Status**: ✅
- **Reason**: information bottleneck 기반 채널출력 양자화 LUT 디코딩(min-sum 양자화 LLR에 이식 가능), 유전알고리즘 파라미터화 압축 매핑(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9310016
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: Jan Lewandowsky, Sumedh J. Dongare, Marc Adrat +2
- **PDF**: https://ieeexplore.ieee.org/document/9310016
- **Abstract**: Preserving relevant mutual information under compression is the fundamental challenge of the information bottleneck method and has numerous applications in machine learning and in communications. The literature describes very successful applications of this concept in quantized detection and channel decoding schemes. The resulting receiver algorithms only use simple lookup tables and process quantization indices, but can achieve performance close to that of conventional high-precision systems. In some applications, however, it is desirable to design a parametrized compression rule instead of a possibly huge lookup table. Genetic algorithms are very powerful generic optimization algorithms which are inspired from the natural evolution of the species. In this paper, we show that genetic algorithms can be used to optimize parametrized compression mappings that aim for maximum preservation of relevant information, especially in cases where standard optimization methods cannot be applied straightforwardly. We exemplarily investigate the receiver-sided channel output quantization as an important application in communications to illustrate the notable performance and the flexibility of the proposed concept.

## Syndrome-Aided Gradient Descent Bit Flipping Algorithm for LDPC Decoding

- **Status**: ✅
- **Reason**: 신드롬 기반 적응 임계값 GDBF 비트플립 디코딩(SAGDBF) 신규 제안, 저복잡도 바이너리 LDPC 디코더로 직접 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9345227
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Yuang Huang, Haiyang Liu
- **PDF**: https://ieeexplore.ieee.org/document/9345227
- **Abstract**: Gradient descent bit flipping (GDBF) algorithm is an important low-complexity method for decoding LDPC codes. In particular, the multi-bit GDBF decoding has the best decoding performance among BF algorithms if a suitable threshold is prescribed. However, extensive computer searches are needed to find such a threshold for a specific LDPC code. In this paper, we propose a syndrome-aided GDBF (SAGDBF) algorithm to address the problem. The thresholds in our algorithm are adaptively adjusted according to the syndrome values in the iterative process. Simulation results for different LDPC codes suggest that the error performances of the proposed SAGDBF algorithm are close to and even better than the original multi-bit GDBF algorithm at a relatively small number of iterations. In addition, the complexity increased in our proposed algorithm is negligible compared with the original multi-bit GDBF algorithm. Hence, the proposed algorithm is suitable for practical purposes.

## A Novel Soft-Output Demapper for DOCSIS 3.1

- **Status**: ✅
- **Reason**: DOCSIS 3.1 LDPC용 개선 bit LLR 식 제안, 저부호율 QAM LLR 정확도 향상은 NAND LDPC LLR 양자화/연판정 디코딩에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9345192
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Feng Zheng, Bowen Pang
- **PDF**: https://ieeexplore.ieee.org/document/9345192
- **Abstract**: DOCSIS 3.1, the new international standard for high-speed cable television (CATV), uses Low Density Parity Check (LDPC) code for forward error correction (FEC). It is widely known that accurate soft information is critical to the performance of LDPC decoding, but existing bit log-likelihood ratio (LLR) expression only works well under high code rate. In this paper, an improved bit LLR expression is proposed to compensate the difference between the existing LLR expression under low code rate for Gray coded M-ary quadrature amplitude modulation (QAM). In addition to high accuracy, the improved LLR is simple and efficient to manipulate. Besides LDPC, the improved LLR is also applicable to other codes that require soft information. Simulation results show that the improved LLR expression achieves a significant improvement in performance for both LDPC and Turbo decoding.

## Semi-LDPC Convolutional Codes with Low-latency Decoding Algorithm

- **Status**: ✅
- **Reason**: semi-LDPC convolutional code 신규 구성 + 윈도우=2 슬라이딩 윈도우 list 디코딩으로 저지연 코딩이득, 바이너리 LDPC 구성/디코더 기법 이식 가능(E/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9344992
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Zengzhe Chen, Suihua Cai, Li Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/9344992
- **Abstract**: In this paper, we propose a new coding scheme called semi-low-density parity-check (semi-LDPC) convolutional code, whose parity-check matrix consists of both sparse and dense sub-matrices. We propose a sliding-window decoding algorithm with a window size of two, in which a list decoding algorithm is utilized to reduce decoding latency. Simulation results show the proposed semi-LDPC convolutional code with list decoding can obtain a coding gain up to 1 dB over the existing LDPC convolutional codes with the same decoding latency.

## Improving SSD Read Latency via Coding

- **Status**: ✅
- **Reason**: SSD read latency 향상 코딩, NAND 소자 실패+ECC 큐잉 모델. 스토리지 ECC 일반(B) 범주.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9026817
- **Type**: journal
- **Published**: 1 Dec. 202
- **Authors**: Hyegyeong Park, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/9026817
- **Abstract**: We study the potential enhancement of the read access speed in high-performance solid-state drives (SSDs) by coding, given speed variations across the multiple flash interfaces and assuming occasional local memory failures. Our analysis is based on a queuing model that incorporates both read request failures and NAND element failures. The NAND element failure in the present context reflects various limitations on the memory element level such as bad blocks, dies or chips that cannot be corrected by error control coding (ECC) typically employed to protect pages read off the NAND cells. Our analysis provides a clear picture of the storage-overhead and read-latency trade-offs given read failures and NAND element failures. We investigate two different ways to mitigate the effect of NAND element failures using the notion of multi-class jobs with different priorities. A strong motivation for this work is to understand the reliability requirement of NAND chip components given an additional layer of failure protection, under the latency/storage-overhead constraints.
