# IEEE Xplore — 2007-05 (1차선별 통과)


## Analysis and Design of Finite-Length LDPC Codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC 코드 구성: IRA 부호 사이클 제어 + 수정 bit-filling으로 low error floor 달성 (E: 코드설계, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4201074
- **Type**: journal
- **Published**: May 2007
- **Authors**: Guosen Yue, Ben Lu, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/4201074
- **Abstract**: We consider the performance analysis and code construction of finite-length low-density parity-check (LDPC) codes. First, by convergence analysis based on the extrinsic information evolution, we analyze the performance of both regular and irregular finite-length LDPC codes under iterative decoding. Next, by focusing on a special class of LDPC codes, namely, systematic irregular repeat-accumulate (IRA) codes, we propose a design procedure to construct finite-length LDPC codes. In addition to giving rise to a simple encoding structure, the special structure of IRA codes can be exploited to introduce unequal protection with cycle control for different types of nodes in the factor-graph code representation. We propose a modified bit-filling algorithm that leads to the construction of a set of finite-length IRA codes with low error floors.

## Iterative Decoding With Replicas

- **Status**: ✅
- **Reason**: replica shuffled iterative 디코더 — 바이너리 LDPC BP 스케줄 개선(수렴 가속). 부호 비의존 디코더 기법, 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4167737
- **Type**: journal
- **Published**: May 2007
- **Authors**: Juntan Zhang, Yige Wang, Marc P. C. Fossorier +1
- **PDF**: https://ieeexplore.ieee.org/document/4167737
- **Abstract**: Replica shuffled versions of iterative decoders for low-density parity-check (LDPC) codes and turbo codes are presented. The proposed schemes can converge faster than standard and plain shuffled approaches. Two methods, density evolution and extrinsic information transfer (EXIT) charts, are used to analyze the performance of the proposed algorithms. Both theoretical analysis and simulations show that the new schedules offer good tradeoffs with respect to performance, complexity, latency, and connectivity

## Layered BP Decoding for Rate-Compatible Punctured LDPC Codes

- **Status**: ✅
- **Reason**: Layered BP 디코딩의 check node 업데이트 스케줄링 개선으로 수렴 가속 - 부호 비의존적 BP 개선 기법 이식 가능 (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4202100
- **Type**: journal
- **Published**: May 2007
- **Authors**: Jeongseok Ha, Demijan Klinc, Jini Kwon +1
- **PDF**: https://ieeexplore.ieee.org/document/4202100
- **Abstract**: Rate-compatible punctured LDPC codes have shown to perform well over a wide variety of code rates, both theoretically and practically. However it has been reported that the belief propagation (BP) decoding for these codes converges slower than for unpunctured codes. Layered BP algorithm is a modified BP algorithm that accelerates the decoding convergence by means of sequential scheduling of check node updates. In this letter, we propose an efficient scheduling of check node updates for rate-compatible punctured LDPC codes that performs well. We show that the convergence speed of the proposed scheduling outperforms conventional (random) scheduling and conventional BP decoding. Performance improvements become more distinctive with the growing fraction of punctured bits

## Performance of Quantized Min-Sum Decoding Algorithms for Irregular LDPC Codes

- **Status**: ✅
- **Reason**: 양자화 min-sum(normalized/offset) 신규 개선 기법, finite precision HW (C 디코더)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4253249
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Daesun Oh, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4253249
- **Abstract**: In this paper, we analyze the performance of quantized min-sum decoding algorithms for irregular low-density parity-check (LDPC) codes. For regular LDPC codes, it is known that the normalized or offset min-sum decoding algorithm with quantization bits less than 6 bits achieves good performances over wide range of signal-to-noise ratios (SNR). However, finite precision effects in decoding irregular LDPC codes are different from that in decoding regular LDPC codes which is caused by the difference of convergence speeds between low degree nodes and high degree nodes. This paper proposes a novel method to improve the performance of the conventional normalized or offset min-sum decoding algorithm when it is approximated with finite precision for hardware implementations. The proposed method applies down-scaling factors to intrinsic information which has effects on increasing the reliability of extrinsic information at variable nodes and compensating the quantization errors caused by finite precision. Computer simulation results for irregular LDPC codes show that our proposed normalized and offset min-sum decoding algorithms achieve much better performances at high SNR compared to the conventional normalized and offset min-sum algorithms under (6:2) quantization scheme.

## VLSI Decoder Architecture for High Throughput, Variable Block-size and Multi-rate LDPC Codes

- **Status**: ✅
- **Reason**: 가변블록·멀티레이트 QC-LDPC VLSI 디코더 아키텍처, 실측 칩 (D 이식가능 HW)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4253085
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Yang Sun, Marjan Karkooti, Joseph R. Cavallaro
- **PDF**: https://ieeexplore.ieee.org/document/4253085
- **Abstract**: A low-density parity-check (LDPC) decoder architecture that supports variable block sizes and multiple code rates is presented. The proposed architecture is based on the structured quasi-cyclic (QC-LDPC) codes whose performance compares favorably with that of randomly constructed LDPC codes for short to moderate block sizes. The main contribution of this work is to address the variable block-size and multi-rate decoder hardware complexity that stems from the irregular LDPC codes. The overall decoder, which was synthesized, placed and routed on TSMC 0.13-micron CMOS technology with a core area of 4.5 square millimeters, supports variable code lengths from 360 to 4200 bits and multiple code rates between 1/4 and 9/10. The average throughput can achieve 1 Gbps at 2.2 dB SNR.

## A High Throughput H-QC LDPC Decoder

- **Status**: ✅
- **Reason**: H-QC LDPC 고처리율 디코더, overlapped message passing 스케줄링으로 메모리 충돌 회피+메모리 절반, 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4252972
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Yi-Hsing Chien, Mong-Kai Ku
- **PDF**: https://ieeexplore.ieee.org/document/4252972
- **Abstract**: In this paper, design of a high throughput low-density parity-check (LDPC) decoder using overlapped message passing scheduling algorithm is presented. Regular hierarchical quasi-cyclic (H-QC) LDPC code is used in this design to provide good coding performance at long code length. The two-level regular H-QC LDPC code matrix structure is exploited to parallelize the row and column decoding operations. Our scheduling algorithm re-arranges these operations across iteration boundaries to avoid memory access conflicts. The memory requirement is reduced by half compared to pipelined decoders without scheduling. A (12288, 6144) LDPC decoder implemented in FPGA achieves 298 Mbps throughput performance.

## Efficient Highly-Parallel Decoder Architecture for Quasi-Cyclic Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: QC-LDPC 고도병렬 디코더 아키텍처, partially overlapped로 HW 복잡도 저감 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4253023
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Daesun Oh, Keshab K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/4253023
- **Abstract**: In this paper, we propose an efficient highly-parallel decoder architecture using partially overlapped decoding scheme for quasi-cyclic (QC) low-density parity-check (LDPC) codes, which leads to reduction in hardware complexity and power consumption. Generally, due to the regularly structured parity-check matrix H of QC LDPC codes, the message updating computations in the check node unit (CNU) and the variable node unit (VNU) can be efficiently overlapped, which increases the decoding throughput by maximizing the hardware utilization efficiency (HUE). However, the partially overlapped decoding scheme cannot be used to design a highly-parallel decoding architecture for high-throughput applications. For (3, 5)-regular QC LDPC codes, our proposed method could reduce the hardware complexity by approximately 33% for the CNU and 20% for the VNU in the highly-parallel decoder architecture without any performance degradation. In addition, the power consumption can be minimized by reducing the total number of memory accesses for updated messages.

## Efficient Message Passing Architecture for High Throughput LDPC Decoder

- **Status**: ✅
- **Reason**: permutation matrix LDPC용 min-sum 재구성 메시지패싱 아키텍처+비균일 3비트 양자화, 이식 가능 HW/양자화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4252785
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Zhiqiang Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/4252785
- **Abstract**: In this paper, we propose an efficient message passing architecture for permutation matrices based LDPC code decoders. Min-Sum algorithm is reformulated to facilitate significant reduction of routing complexity and memory usage. For a (2048, 1723) (6, 32) LDPC code with 4-bit quantization, 54% outgoing wires per variable node unit and 90% outgoing wires per check node unit can be saved. To further reduce hardware complexity, an optimized non-uniform quantization scheme using only 3 bits to represent each message has been investigated. The simulation result shows that it has only 0.25dB performance loss from the floating-point SPA.

## Multi-Rate Layered Decoder Architecture for Block LDPC Codes of the IEEE 802.11n Wireless Standard

- **Status**: ✅
- **Reason**: block QC-LDPC 멀티레이트 layered 디코더 아키텍처(offset min-sum value-reuse, 메모리/라우터 절감), 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4252971
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Kiran Gunnam, Gwan Choi, Weihuang Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4252971
- **Abstract**: We present a new multi-rate architecture for decoding block LDPC codes in IEEE 802.11n standard. The proposed architecture utilizes the value-reuse property of offset min-sum, block-serial scheduling of computations and turbo decoding message passing algorithm. Techniques of data-forwarding and out-of-order processing are used to deal with the irregularity of the codes. The decoder has the following advantages when compared to recent state-of-the-art architectures: 55% savings in memory, reduction of routers by 50% and increase of throughput by 2x.

## Towards a GBit/s Programmable Decoder for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional 디코더 병렬화/저복잡도 프로그래머블 HW 아키텍처 (D 이식가능 HW)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4252974
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Emil Matus, Marcos B.S. Tavares, Marcel Bimberg +1
- **PDF**: https://ieeexplore.ieee.org/document/4252974
- **Abstract**: We analyze the decoding algorithm for regular time-invariant LDPC convolutional codes as a 3D signal processing scheme and derive several parallelization concepts, which were used to design a novel low-complexity programmable decoder architecture with throughput in the range of 1 Gbit/s at moderate system clock frequencies. The synthesis results indicate that the decoder requires relatively small areas, even when high levels of parallelism are used.

## FPGA Implementation of LDPC Decoders Based on Joint Row-column Decoding Algorithm

- **Status**: ✅
- **Reason**: joint row-column 디코딩 알고리즘 FPGA 구현, 메모리 충돌/라우팅 회피+error floor 개선, 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4252973
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Zhiyong He, Sebastien Roy, Paul Fortier
- **PDF**: https://ieeexplore.ieee.org/document/4252973
- **Abstract**: This paper presents a joint row-column decoding algorithm for the decoding of low-density parity-check (LDPC) codes. Simulation indicates that the proposed algorithm improves the performance in both the waterfall region and the error floor region. By combining row processing with column processing, the joint row-column decoding algorithm reduces the storage requirements of extrinsic messages and avoids memory conflicts and routing congestion during the exchanges of extrinsic messages. Implementation results into field programmable gate array (FPGA) devices indicate that the proposed algorithm reduces the hardware costs by 30% and increases the decoding speed by a factor of four. A 40-parallel decoder attains a throughput of 2 Gbits/sec by using up to 20% of the generic logic resources in a Xilinx XC4LX160 device.

## Design and Realization of Analog Phi-Function for LDPC Decoder

- **Status**: ✅
- **Reason**: log-SP Phi-function의 아날로그 구현으로 LUT 대체, 디코더 HW 기법 (C/D 이식가능)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4252975
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Abu Baker, Soumik Ghosh, Ashok Kumar +2
- **PDF**: https://ieeexplore.ieee.org/document/4252975
- **Abstract**: One of the ambitious design goals of future generations of wireless systems, including 4G, IEEE 802.11n/802.16 standards, is to reliably provide very high data rate transmission in real-time. This poses a challenge to find an optimal coding scheme that has good performance and can be efficiently implemented in hardware. The most well-known LDPC decoding algorithm is log sum product (log-SP) in which a set of calculations on a non-linear function called Phi-function is approximated by a minimum function. Until now this function has been implemented through look up tables (LUT). But this direct implementation is costly for hardware. Also LUTs are very sensitive to the number of quantization bits and number of LUT values. Therefore, we have proposed analog Phi-function. The design is easily scalable and reconfigurable for larger block sizes. Simulation results show that our proposed design dissipates only 18 nW.

## Designing near Shannon limit LDPC codes using particle swarm optimization algorithm

- **Status**: ✅
- **Reason**: PSO로 LDPC variable/check 차수분포 최적화하는 신규 코드 설계 기법(E), 바이너리 LDPC 가정
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4448612
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: Fatma A. Newagy, Yasmine A. Fahmy, Magdi M. S. El-Soudani
- **PDF**: https://ieeexplore.ieee.org/document/4448612
- **Abstract**: This paper presents a new design methodology/process for low-density parity-check codes (LDPC). To minimize the gap to Shannon limit, the particle swarm optimizer is applied to optimize the variable and check node degree distribution lambda and p respectively in case of irregular LDPC codes. discrete fast density evolution (FDE) is used (as the analysis technique) to compute the threshold value of LDPC code and the Shannon limit is evaluated based on Butman and McEliece formula. The results conducted show that, our proposed distributions with low degrees of (lambda, p) outperform other comparable distributions.

## MP&A Mixed Decoding Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: MP+A* 하이브리드 LDPC 디코딩으로 일부 시퀀스만 A*로 전환해 최적해 근접, 이식 가능 BP 개선 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4215518
- **Type**: conference
- **Published**: 14-17 May 
- **Authors**: C.L. Ho, Hsu-Hung Yang
- **PDF**: https://ieeexplore.ieee.org/document/4215518
- **Abstract**: Because the message passing (MP) method is suboptimum and optimum solutions are not guaranteed, we present a hybrid decoding method by combing the MP and the A* methods. We first make comparison between the MP and A* method and then show their combined performance. Using the hybrid structure, its decoding gain is the same as that of A* method. Moreover, decoding complexity is slightly greater than that of MP one. For codeword length 96 bits and coding rate 1/2 and BER = 10-5 , the hybrid structure outperforms 1.4 dB decoding gain than the MP method. This improvement only required 1% received sequences to be transferred to A* decoding block. Our newly designed hybrid structure can solve both of the high decoding gain and low decoding complexity while it has the ability to yield the optimum solution.
