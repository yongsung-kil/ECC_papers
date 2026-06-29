# IEEE Xplore — 2023-11 (1차선별 통과)


## ALCod: Adaptive LDPC Coding for 3-D NAND Flash Memory Using Inter-Layer RBER Variation

- **Status**: ✅
- **Reason**: A: 3D TLC NAND 직접 - inter-layer RBER 변동 활용 적응형 LDPC 코딩, LLR 개선으로 디코딩 가속 (NAND ECC 핵심)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10265139
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Meng Zhang, Xiaoyi Zhang, Fei Wu +5
- **PDF**: https://ieeexplore.ieee.org/document/10265139
- **Abstract**: Three-dimensional (3D) NAND flash memory has been frequently utilized in consumer electronics as a popular storage device. However, data reliability has become an important problem to be solved. Low-density parity-check (LDPC) codes with superior error correction capability are commonly used in 3D NAND flash memory to ensure data reliability. Unfortunately, high raw bit error rate (RBER) induced by retention time and program/erase (P/E) cycles leads to increased the number of decoding iterations, failing to correct bit errors. Consequently, data reliability cannot be well ensured by using conventional LDPC coding. Moreover, the number of decoding iterations between layers fluctuates greatly due to process variation, which leads to a large difference in decoding latency. To reduce and shorten the gap of inter-layer decoding iterations, this paper proposes ALCod: an adaptive LDPC coding scheme for 3D triple-level cell (TLC) NAND flash memory by exploiting the inter-layer RBER variation. Specifically, this paper first conducts a preliminary experiment, which shows that RBER and the number of decoding iterations between layers and pages have a great difference. And, high RBER induces decreased decoding performance, thus introducing more decoding iterations and time consumption. Then, inspired by these findings, ALCod adaptively performs LDPC coding operations according to the RBER variation induced by retention time and P/E cycles. For pages and layers with higher RBER, by using ALCod, the original bit sequence is split into two parts on average and encoded separately. During decoding, known bits of 0 information are used to improve the initial decoding information (i.e., log-likelihood ratio (LLR) information per bit). To help with the decoding of the codeword’s unknown information, the LLR amplitude of known bits of 0 is increased. The known information and unknown information participate in the same check equation, which, according to the LDPC decoding principle, can provide useful LLR information to speed up decoding update for unknown information. ALCod can improve LDPC decoding performance and effectively eliminate soft decision decoding at higher RBER. Simulation results show ALCod can significantly reduce the uncorrectable bit error rate (UBER), decoding iterations, and time consumption.

## A Study on Accelerating SP Decoding by Neural Network in SMR System

- **Status**: ✅
- **Reason**: C: SMR용 LDPC sum-product 디코딩을 NN으로 가속하는 신경망 디코더 - 고전 바이너리 LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10130306
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/10130306
- **Abstract**: We have previously studied low-density parity-check (LDPC) coding and iterative decoding in the shingled magnetic recording (SMR) system as a signal processing method to realize ultrahigh-density hard disk drives (HDD). In addition, we have proposed the application of the neural network (NN) to improve decoding performance and realize the automation of iterative decoding. In this study, we apply an NN to accelerate iterative decoding in the sum-product (SP) decoder. As the result, the SP decoder with the NN realized “no errors” at the fewest times of the iterative decoding compared to our previous studies.

## Interleaved LDPC Decoding Scheme Improves 3-D TLC NAND Flash Memory System Performance

- **Status**: ✅
- **Reason**: A: 3D TLC NAND용 interleaved LDPC 디코딩으로 FER/iteration/latency 개선 - NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10098900
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Xiaolei Yu, Jing He, Bo Zhang +5
- **PDF**: https://ieeexplore.ieee.org/document/10098900
- **Abstract**: Although NAND flash memory does a lot of work in effectively using error correcting code (ECC) to reduce uncorrectable bit error rate (UBER). However, if the frame error rate (FER) is not reduced, the lower UBER cannot effectively reduce the read latency of the flash memory system. This phenomenon is especially evident at the end of the flash memory lifetime, where conventional methods significantly reduce the UBER but not to zero, and the remaining error bits are still evenly distributed throughout the flash memory page, resulting in a significant increase in read latency. In this article, an interleaved LDPC decoding scheme is proposed. By re-evaluating the flash memory channel during the decoding process, the codewords in the flash memory page are corrected frame by frame, and the problem of high FER is solved at the end of the flash memory lifetime. Compared with the conventional algorithm, the proposed method can reduce the FER by up to 34%, reduce the average decoding iterations by 63.4%, and reduce the read latency by up to 65%.

## An FCResNet-Based Iterative Detection for Protograph LDPC-Coded SRMR-DCSK Systems Under Correlated Noise

- **Status**: ✅
- **Reason**: C: protograph LDPC-coded 시스템에 FCResNet 기반 반복검출+LLR 유도, 신경망 디코더 기법 이식 가능(애매-Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10256136
- **Type**: journal
- **Published**: Nov. 2023
- **Authors**: Chengquan Lu, Yi Fang, Lin Dai +2
- **PDF**: https://ieeexplore.ieee.org/document/10256136
- **Abstract**: In the protograph-coded short reference multifold rate differential chaotic shift keying (SRMR-DCSK) systems, the signal transmission reliability is affected by the channel noise, especially when the noise is correlated. To solve this problem, this letter proposes a fully convolutional residual network (FCResNet)-based iterative detection structure to suppress the correlated noise in the protograph-coded SRMR-DCSK systems. Specifically, we design a new FCResNet tailored for the considered systems to accurately extract the characteristics of correlated noise, and thus the correlated noise can be easily removed from the received signal in an iterative fashion. In addition, we derive the log-likelihood ratio (LLR) expression of the protograph-coded SRMR-DCSK systems to facilitate the proposed detection. Simulation results demonstrate that the proposed FCResNet-based detection structure can obtain more desirable performance gain compared with the existing detection over Gaussian and multipath Rayleigh fading channels.

## HF-LDPC: HLS-friendly QC-LDPC FPGA Decoder with High Throughput and Flexibility

- **Status**: ✅
- **Reason**: HLS-friendly QC-LDPC FPGA 디코더(HF-LDPC): multi-unit 데이터플로우·fine-grained task-level pipeline 신규 HW 아키텍처, 스토리지 명시, NAND 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10360987
- **Type**: conference
- **Published**: 6-8 Nov. 2
- **Authors**: Yifan Zhang, Qiang Cao, Shaohua Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10360987
- **Abstract**: LDPC (Low-Density Parity-Check) codes have become a cornerstone of transforming a noise-filled physical channel into a reliable and high-performance data channel in communication and storage systems. FPGA (Field-Programmable Gate Array) based LDPC hardware, especially for decoding with high complexity, is essential to realizing the high-bandwidth channel prototypes. HLS (High-Level Synthesis) is introduced to speed up the FPGA development of LDPC hardware by automatically compiling high-level abstract behavioral descriptions into RTL-level implementations, but often sub-optimally due to lacking effective low-level descriptions. To overcome this problem, this paper proposes an HLS-friendly QC-LDPC FPGA decoder architecture, HF-LDPC, that employs HLS not only to precisely characterize high-level behaviors but also to effectively optimize low-level RTL implementation, thus achieving both high throughput and flexibility. First, HF-LDPC designs a multi-unit framework with a balanced I/O-computing dataflow to adaptively match code parameters with FPGA configurations. Second, HF-LDPC presents a novel fine-grained task-level pipeline with interleaved updating to eliminate stalls due to data interdependence within each updating task. HF-LDPC also presents several HLS-enhanced approaches. We implement and evaluate HF-LDPC on Xilinx U50, which demonstrates that HF-LDPC outperforms existing implementations by 4× to 84× with the same parameter and linearly scales to up to 116 Gbps actual decoding throughput with high hardware efficiency.

## FPGA Implementation of 5-bit Non-Uniform Quantization LDPC Code for High-speed PON

- **Status**: ✅
- **Reason**: 5-bit 비균일 양자화 LDPC LLR 처리 FPGA 구현, LLR 양자화는 NAND LDPC 핵심 기법으로 이식 가능(A/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10369107
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Zipeng Liang, Tian Qiu, Yang Zou +5
- **PDF**: https://ieeexplore.ieee.org/document/10369107
- **Abstract**: This paper proposes and verifies a resource-efficient 5-bit non-uniform quantization LDPC code for LLR processing. This low power consumption and low latency LDPC decoding method is promising for future high-speed PON.

## A Stepped Low Density Parity Check Codes Punching Algorithm Based on Multiple Check Matrices

- **Status**: ✅
- **Reason**: 다중 검사행렬 기반 stepped LDPC 펑처링 알고리즘으로 적응적 부호율 실현, 코드 설계 기법 이식 가능(E), 애매하면 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10369524
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Rongzhen Xie, Qi Zhang, Xiangjun Xin +6
- **PDF**: https://ieeexplore.ieee.org/document/10369524
- **Abstract**: A stepped low density parity check (LDPC) codes punching algorithm based on multiple check matrices is proposed. The proposed scheme is more flexible to realize the adaptive rate under Gaussian white channel. In a 100Gbit/s optical communication simulation system, the proposed algorithm has about 0.49dB gain after 1000km of transmission, compared to the general punching algorithm.

## A High-Throughput QC-LDPC Encoder

- **Status**: ✅
- **Reason**: HLS 기반 QC-LDPC 인코더 마이크로아키텍처(intra-codeword 병렬), 스토리지용 LDPC HW 설계 이식 가능(B/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10369210
- **Type**: conference
- **Published**: 4-7 Nov. 2
- **Authors**: Yifan Ding, Qiang Cao, Jie Yao
- **PDF**: https://ieeexplore.ieee.org/document/10369210
- **Abstract**: Low Density Parity Check (LDPC) codes have been widely used in communication and storage fields to support high reliability of data channel. Quasi-cyclic (QC)-LDPC as a regular code can sufficiently exploit hardware parallelism of Field-Programmable Gate Array (FPGA) to accelerate the encoding/decoding performance. However, existing FPGA encoders are generally dedicated to a specialized LDPC code and hardware platform with limited flexibility. In this paper, to achieve high throughput and flexibility simultaneously, we propose a High-level synthesis (HLS) based QC-LDPC encoder microarchitecture. The encoder designs a fine-grained partially-parallel iterative process execution to exploit intra-codeword parallelism by fully leveraging capability of HLS. The proposed encoder further optimizes data-layout and HLS-function implementation. The encoding throughput of the proposed encoder achieves 98.4Gbps higher than the state-of-the-art QC-LDPC encoder by up to 14.75x.

## Low Power LDPC Decoding by Reliable Voltage Down-Scaling

- **Status**: ✅
- **Reason**: 전압 다운스케일링 기반 저전력 LDPC 디코더 HW(Zynq SoC, CRC 가이드 적응형 전압) — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10305442
- **Type**: conference
- **Published**: 31 Oct.-1 
- **Authors**: Joonas Valkama, Mehdi Safarpour, Håkan Dicander +3
- **PDF**: https://ieeexplore.ieee.org/document/10305442
- **Abstract**: Low-Density Parity-Check (LDPC) decoder is among the power hungry building blocks of wireless communication systems. Voltage scaling down to Near-Threshold (NT) voltages substantially improves energy efficiency, in theory up 10x. However, tuning the voltage and clock frequency to the optimum error free operating point is challenging. This is mainly due to exacerbated sensitivity to Process, Voltage and Temperature (PVT) variations at reduced voltages. By definition, in many telecommunication standards, a Cyclic Redundancy Check (CRC) error detection is carried out after each forward error correction operation, e.g., LDPC decoding. Given channel information, successful CRC checking opens an opportunity for "safe" voltage down-scaling and optimum frequency tuning of LDPC decoder hardware. The strategy is explored on a Zynq System-on-Chip with CRC guiding the adaptive voltage scaling with microcontroller and LDPC decoder residing in different voltage islands. Around 40% power saving was achieved with negligible degradation in throughput.

## Unlocking the Potential of LDPC Decoders with PiM Acceleration

- **Status**: ✅
- **Reason**: 바이너리 LDPC 디코더의 PiM(in-memory) 가속 신규 HW 아키텍처/병렬화 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10476816
- **Type**: conference
- **Published**: 29 Oct.-1 
- **Authors**: Oscar Ferraz, Yann Falevoz, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/10476816
- **Abstract**: This paper introduces a novel concept for exploiting processing in-memory (PiM) hardware decoding low-density parity-check (LDPC) codes. The PiM hardware can be used to mitigate the high cost of data movement in modern computing systems by placing computing units near memory where data resides. The memory hierarchy and the parallel nature of the limited arithmetic units allow the multithreaded-based paral-lelization of the LDPC decoder inside each data processing unit (DPU) and the simultaneous launch of multiple LDPC decoders. The experiments confirm a speedup of 1155 ×, compared to the baseline, a sequential high-end CPU, for the binary LDPC decoder of CCSDS-231 standard reaching 742 Mbps of global throughput performance in-memory.

## High Performance Error Correction Under Low SNR Based on Deep Neural Network

- **Status**: ✅
- **Reason**: 저SNR 신경망 디코더, LLR-BP 대비 단거리 코드 개선 — 이식 가능 신경망 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10421646
- **Type**: conference
- **Published**: 24-26 Nov.
- **Authors**: Jianxin Gao, Changshui Li, Dongsheng Li +2
- **PDF**: https://ieeexplore.ieee.org/document/10421646
- **Abstract**: The signal-to-noise ratio of long-distance relay free communication systems and quantum secure communication systems is very low, making it difficult to achieve high-performance error correction. In order to achieve effective error correction, longer code words or higher iterations are generally chosen to achieve the highest error correction efficiency as possible. However, this will greatly increase the complexity of the error correction process and reduce real-time performance. To solve this problem, we propose a high-performance error correction algorithm based on deep neural network. In the case of low signal-to-noise ratio, the error correction performance of this method is better than that of the classical LLR-BP algorithm for high-speed short codes. At the same time, the number of hidden layers and neurons were adjusted according to the coding length, and the generalization performance of the model was improved. The results show that our proposed DNN based decoding algorithm can achieve better error correction performance than LLR-BP when the signal-to-noise ratio is less than 9dB.

## Constructions of Girth-Eight QC-LDPC Codes with Dual-Diagonal Structure Based on GCD Framework

- **Status**: ✅
- **Reason**: GCD 프레임워크 기반 girth-8 QC-LDPC 신규 구성(4/6-cycle 제거, dual-diagonal) — 바이너리 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10405132
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Guohua Zhang, Haiyang Liu, Mengjuan Lou +1
- **PDF**: https://ieeexplore.ieee.org/document/10405132
- **Abstract**: A novel class of quasi-cyclic (QC) low-density parity-check (LDPC) codes is explicitly proposed without 4-cycles and 6-cycles via the greatest-common-divisor (GCD) framework. From the new codes, a novel type of girth-eight QC-LDPC codes with a dual-diagonal (DD) structure is presented, in which the single undetermined entry in the associated exponent matrix can be determined by simple formulae. The proposed DD codes have similar or better performance compared with DD codes obtained from computer search. Moreover, a lower bound on circulant sizes which guarantees the existence of qualified undetermined entries is also provided.

## RIS-Assisted Coded Relay Cooperation Based on LDPC Product Codes with Finite Code Length

- **Status**: ✅
- **Reason**: LDPC product code 인코딩+유한길이 joint iterative 디코딩 알고리즘 제안 — 이식 가능 디코더/코드설계 가능성으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10405032
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Jin Wang, Shunwai Zhang, Zhonghui Mei +2
- **PDF**: https://ieeexplore.ieee.org/document/10405032
- **Abstract**: Reconfigurable intelligent surfaces (RIS) is a kind of metamaterial with the ability to regulate and control wireless channels, which can provide additional links for wireless communication systems. Meanwhile, it has low hardware cost, low energy consumption, flexible deployment, and intelligent reconfiguration merits. By combining the RIS technology with coded relay cooperation, we establish the RIS-assisted coded relay cooperation based on low density parity check (LDPC) product codes, and further propose the LDPC product code encoding method and efficient joint iterative decoding algorithm. Then, we theoretically derive the approximate solutions of the outage probability and the channel capacity with finite code length. Theoretical analysis and simulation results show that the proposed system obviously outperforms the traditional coded relay cooperation, and the more number of RIS elements, the more significant advantage can be obtained. Simulation results also demonstrate that the channel capacity with finite code length approaches the ideal channel capacity with the code length of LDPC product codes increasing.

## Coding Principle and Information-Theoretic Limit of OAMP Receiver in Unitary-Transform Generalized Linear Systems

- **Status**: ✅
- **Reason**: GOAMP용 LDPC 코드 설계/임계값 최적화(0.8dB 접근, 발산 극복) — 이식 가능 코드설계 기법 가능성, 애매하여 in
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10404292
- **Type**: conference
- **Published**: 2-4 Nov. 2
- **Authors**: Yuhao Chi, Lei Liu, Xuehui Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/10404292
- **Abstract**: In wireless communications, the unitary-transform generalized linear system (GLS) has been widely used to evaluate the impact of nonlinear preprocessing on transceivers. Generalized approximate message passing (GAMP) is a state-of-the-art low-complexity signal recovery algorithm, but it is only applicable to independent and identically distributed (IID) Gaussian matrices. To overcome this limitation, generalized orthogonal AMP (GOAMP) has been developed for unitarily invariant matrices, however, its information-theoretic limit analysis is numerical and limited by the high-complexity linear minimum mean-squared error (LMMSE), which is difficult to be analyzed analytically. Meanwhile, it is unable to effectively utilize the properties of unitary matrices, rendering the information-theoretic analysis still complex. To address these issues, in this paper, we provide the achievable rate analysis and optimal coding principle for GOAMP in unitary-transform GLS with arbitrary input distributions, establishing its information-theoretic limit (i.e., maximum achievable rate). Specifically, the simplified variational state evaluation (VSE) of GOAMP are developed using the unitary matrix properties to analyze the achievable rate, and the optimal code principle is derived with goal of maximizing the achievable rate. In addition, it is rigorously proved that GOAMP outperforms GAMP in terms of asymptotic MSE with lower complexity. Furthermore, quantization is used as an example to demonstrate the maximum achievable rate and practical low-density parity-check (LDPC) code design for GOAMP. The optimized LDPC code can approach the threshold limit within 0.8 dB and overcome the decoding deterioration and even divergence of the existing state-of-the-art methods.

## Construction of partially-doped generalized LDPC codes over regular LDPC codes

- **Status**: ✅
- **Reason**: partially-doped GLDPC 신규 코드 설계 + 유한길이 분석, 바이너리 LDPC 대비 — 코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10460731
- **Type**: conference
- **Published**: 19-22 Nov.
- **Authors**: Jaewha Kim, Jae-Won Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/10460731
- **Abstract**: In this paper, we propose a new code design technique for GLDPC codes which we call partial doping. The proposed partial doping technique enables higher degrees of freedom in constructing protograph-based GLDPC codes. We optimize the partially-doped generalized LDPC codes over the binary erasure channels and the finite length analysis shows that it outperforms the regular LDPC codes for both code rates 1/2 and 1/4.

## A MATE-GDBF Algorithm for Irregular Punctured LDPC Codes and Its Decoder Implementation

- **Status**: ✅
- **Reason**: MATE-GDBF 신규 디코딩 알고리즘 + ASIC 디코더 구현(저전력 flipping) — 디코더+HW 기여(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10509978
- **Type**: conference
- **Published**: 19-22 Nov.
- **Authors**: Xiao-Juan Huang, Li-Wei Liu, Yen-Chin Liao +2
- **PDF**: https://ieeexplore.ieee.org/document/10509978
- **Abstract**: This paper proposes a MATE-GDBF decoding algorithm and a corresponding decoder architecture for punctured LDPC codes. The proposed algorithm employs majority-vote and tabu-enhancement approaches to improve decoding performance and convergence speed. Additionally, the decoder architecture includes a new flipping access scheme designed to reduce power consumption. The proposed LDPC (9344, 64, 8384) decoder is implemented in TSMC 90nm CMOS process and achieves a 6.39 Gbps throughput at a clock rate of 400 MHz. The decoder's core area is 0.67 mm 2, and its power consumption is 79.6 mW. Overall, the proposed algorithm and decoder architecture offer a promising solution for improving the performance and efficiency of punctured LDPC codes.

## Binary QC-LDPC Codes Based on Whiteman's Generalized Cyclotomy

- **Status**: ✅
- **Reason**: Whiteman 일반화 사이클로토미 기반 바이너리 QC-LDPC 구성, girth-8 보장 신규 구성법 + 스토리지 적합성 명시 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10355791
- **Type**: conference
- **Published**: 17-19 Nov.
- **Authors**: Tao Wang, Zhiping Shi, Li Deng +1
- **PDF**: https://ieeexplore.ieee.org/document/10355791
- **Abstract**: This study introduces a construction method for QC-LDPC codes, ensuring their absence of four-cycles by utilizing Whiteman's generalized cyclotomic (GC) classes. An analysis of the cycle structure within the Tanner graph for the proposed codes, specifically focusing on cycles with length six, is conducted. Moreover, this paper presents the necessary and sufficient conditions for generating GC-QC-LDPC codes with a minimum girth of eight, based on the analysis. Simulation results demonstrate the superior bit error rate (BER) performance of the constructed QC-LDPC codes over the AWGN channel. Compared to other QC-LDPC codes, QC-LDPC codes constructed using this method have a reduced base matrix size for long code lengths. This attribute augments their suitability for integration within storage systems.
