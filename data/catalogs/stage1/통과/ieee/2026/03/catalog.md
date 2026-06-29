# IEEE Xplore — 2026-03 (1차선별 통과)


## Enhanced LDPC Coding for 3-D TLC NAND Flash Memory: Leveraging RBER Difference From Intralayer Variation

- **Status**: ✅
- **Reason**: 3D TLC NAND 플래시 LDPC 코딩, RBER 인지 read-retry 감소 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11124560
- **Type**: journal
- **Published**: March 2026
- **Authors**: Lanlan Cui, Fei Wu, Meng Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/11124560
- **Abstract**: NAND flash memory employs high code rate low-density parity-check (LDPC) codes to reduce the amount of redundant data that must be added. When the code rate is high, although the redundancy space is small, the error correction capability is inferior to medium or low code rate LDPC. raw bit error rate (RBER) varies among the storage layers for 3-D triple-level cell (TLC) NAND flash memory, which increases the frequency of read retry operations. Repeatedly initiating read retry seriously increases the decoding latency and decreases the performance of the 3-D TLC NAND flash memory. To alleviate this problem, this article proposes IntraLayer Variation aware LDPC coding, called LVLDPC. The proposed LVLDPC scheme establishes the correlation between interlayer interference and RBER based on a neural network model. By analyzing and predicting RBER through the neural network model, we are able to categorize RBER into distinct levels. Then, we then select LDPC codes with appropriate error correction capabilities to decode data with varying levels of RBER. Through this scheme, we do not need to start read retry when RBER  $ \lt 1.56 \times {10^{ - 2}} $ . The iteration number is reduced by 67% in total. This scheme only causes 1.15% space overhead, which is negligible. For the stage with high RBER, the number of iterations of LVLDPC is still large, and the extended LVLDPC scheme (eLVLDPC) is further proposed to reduce the use of high code rate and reduce the number of iterations by 19.1%, expanding the correctable RBER threshold to  $ 2.68 \times {10^{ - 2}} $ .

## HFMLLR: Heterogeneous Feature Mining for Low-Overhead Latency Reduction Scheme of LDPC Codes in 3-D TLC nand Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND LDPC 디코딩 지연감소(LLR/반복) - NAND 플래시 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11373055
- **Type**: journal
- **Published**: March 2026
- **Authors**: Yongchao Wang, Debao Wei, Dixin Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/11373055
- **Abstract**: Low-density parity-check (LDPC) codes have been widely adopted in 3-D nand flash memory systems to enhance data storage reliability. However, when the raw bit error rate (RBER) during data read operations is high, the LDPC decoding process often incurs significant iterative latency, which severely impacts system performance. To address this challenge, this article introduces a novel heterogeneous feature mining for low-overhead latency reduction (HFMLLR) scheme. This scheme reconstructs data based on the distinct characteristics of LDPC codes and flash memory and then further leverages log-likelihood ratio (LLR) and interframe error properties to achieve an organic integration of these features. In detail, this scheme first systematically analyzes the divergent impact of information bits versus check bits on reliability within LDPC codes. By leveraging the inherent characteristic disparity between pages in 3-D TLC nand flash, it proposes a disparity characteristic-based data reconstruction (DCDR) scheme. This approach naturally creates a reliability gradient within data frames without adding extra storage overhead. Furthermore, this article explores the mechanism by which the LLR influences decoding convergence. By taking advantage of the spatial correlation between multiframe errors within the same flash page, the HFMLLR scheme optimizes the decoding process, significantly reducing the number of iterations with minimal computational and storage overhead. Experimental results demonstrate that, compared to traditional schemes, the HFMLLR scheme achieves up to an 83.4% reduction in decoding iteration latency, highlighting its remarkable latency reduction capabilities and practical value.

## Across-Array LDPC Codes Design for Resistive Random-Access Memories

- **Status**: ✅
- **Reason**: ReRAM용 비균일 LDPC 코드 설계+밀도진화+HW 단순화 — 스토리지 ECC, 코드설계 이식 가능(B/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11123581
- **Type**: journal
- **Published**: March 2026
- **Authors**: Qike Pang, Zheng Ma
- **PDF**: https://ieeexplore.ieee.org/document/11123581
- **Abstract**: Resistive random-access memory (ReRAM) has garnered significant attention due to its high storage density, rapid read/write speeds, and compatibility with CMOS devices. However, the simple crossbar structure of ReRAM introduces sneak path (SP) interference, which impairs the storage reliability of the ReRAM system. To address this, we propose a novel zoned namespace (ZNS)-based ReRAM storage scheme, which is well-suited for scenarios with hybrid storage protection of multitype data and employs low-density parity-check (LDPC) codes to mitigate the impact of SPs. Furthermore, considering the asymmetric nature of the ReRAM channel, we first develop a computer-calculable asymmetric discrete density evolution of belief propagation decoding (ADDE-BP). Due to the across-array storage structure, SP interference and noise vary across subarrays, resulting in codewords experiencing a nonuniform “sum channel.” To address this, we further propose criteria based on ADDE-BP for nonuniform error correction, specifically for the design of LDPC codewords. Simulation results show that the proposed codes achieve 1–2 orders of magnitude lower bit error rate (BER) than IEEE standard codes and Mackay codes under most channel conditions, thus demonstrating that our proposed LDPC code design for across-array applications enhances data storage reliability compared to conventional methods. Most importantly, the maximum check node degree and node type of the designed code were reduced, thus greatly simplifying the hardware implementation. This work establishes a co-design framework for ReRAM that simultaneously improves the reliability and efficiency of storage systems.

## A Study on the Fitness of GA for Improving SP Decoding Performance

- **Status**: ✅
- **Reason**: SMR HDD LDPC SP디코더 NN 기반 LLR 보정·GA 최적화 — 스토리지 ECC, 디코더 LLR 기법 이식 가능(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11127112
- **Type**: journal
- **Published**: March 2026
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/11127112
- **Abstract**: We have studied low-density parity-check (LDPC) coding and iterative decoding methods for shingled magnetic recording (SMR) in high-capacity hard disk drives (HDDs), which is an areal recording density of 4 Tbits/inch2. Previously, we applied a neural network to evaluate the log-likelihood ratio (LLR) associated with row operations in the sum-product (SP) decoder for LDPC codes. Then, we emphasized the LLR considering the influence of noise depending on the recording pattern by providing the LLRs for the decoding target and its adjacent bits to the neural network in SP decoding. Furthermore, we explored the optimal parameters to emphasize the LLR by applying the genetic algorithm (GA). In this study, to explore more optimal parameters, we propose a fitness function to improve selection accuracy and increase the number of eligible LLRs. Then, we aim to improve the performance of SP decoding by the effect of GA. As a result, by applying the proposed fitness function to the GA, it is possible to maintain high selection accuracy and to increase the probability that LLRs are emphasized in SP decoding. Therefore, it achieves error-free performance with fewer iterations of turbo equalization compared to the case of a conventional fitness function.

## Pushing the Limits of Areal Density: Fusing Advanced Channel Coding, HAMR, and SMR in Next-Generation HDDs

- **Status**: ✅
- **Reason**: HDD용 변조+LDPC 결합 최적화 채널코딩 - 스토리지 ECC 일반(B), LDPC 코딩 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11301807
- **Type**: journal
- **Published**: March 2026
- **Authors**: Jonas Goode, Roger Wood, Rick Galbraith +7
- **PDF**: https://ieeexplore.ieee.org/document/11301807
- **Abstract**: Pushing hard disk drive (HDD) areal density to new extremes requires a fusion of cutting-edge technologies. This article examines the interplay of advanced coding strategies, heat-assisted magnetic recording (HAMR), and shingled magnetic recording (SMR), and how their integration enables substantial gains in areal density. We present a series of measured results demonstrating how jointly optimized modulation and low-density parity-check (LDPC) coding enhances performance across energy-assisted perpendicular magnetic recording (ePMR), HAMR, and SMR environments. Through these demonstrations, we showcase the tangible gains enabled by these technologies and outline a clear trajectory for continued areal density scaling in next-generation HDDs.

## Research on QC-LDPC Decoding Method With Low Quantization Word Length Based on Adaptive Information Mapping in Passive Optical Network

- **Status**: ✅
- **Reason**: QC-LDPC 저양자화 워드길이 적응 정보매핑 TDMP 디코딩 — 저비트폭 디코더 기법 NAND에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11159213
- **Type**: journal
- **Published**: March 2026
- **Authors**: Tao Zhang, Dehui Kong, Xinwei Fu +5
- **PDF**: https://ieeexplore.ieee.org/document/11159213
- **Abstract**: Passive Optical Networks (PON) have advantages such as stable performance, convenient installation, high bandwidth, and resource saving, making them a mainstream network access technology with broad application prospects. The development of such as 8K video, digital twins, VR and other technologies causes explosive growth of network traffic and drives the next generation of PON to evolve towards higher rates, which results in the use of forward error correction (FEC) coding with higher coding gain to improve the power budget of PON. Quasi-cyclic low density parity check (QC-LDPC) codes are widely utilized in PON systems due to high coding gain and parallel encoding and decoding capabilities. However, the application of turbo-decode message passing (TDMP) decoding method is inevitably equated with high hardware complexity of the decoder caused by storing and processing massive information, which is one of the obstacles to PON evolution. Reducing the quantization word length is effective to reduce hardware complexity, but it also leads to saturation of decoding information, causing errors and affecting decoding performance. This work proposes an nonlinear mapping method which utilizes adaptive compression of decoding information through node saturation state monitoring during the decoding process, in order to ensure that the probability density of node information has a reasonable distribution. The simulation results indicate that the method can effectively mitigate the decline in decoding performance under low-word-length conditions.

## LDPC Decoding Acceleration Architecture on Versal AI Edge for Space Platforms

- **Status**: ✅
- **Reason**: 고처리율 LDPC 디코더 HW 아키텍처(Versal SoC/AIE, 병렬화) — D 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11520106
- **Type**: conference
- **Published**: 7-14 March
- **Authors**: Noah Perryman, Sebastian Sabogal, David Wilson +2
- **PDF**: https://ieeexplore.ieee.org/document/11520106
- **Abstract**: As new space opportunities and missions continue to grow, information mobility and communication resilience are two areas that must be evaluated for routing data through multiple space nodes in communication platforms. These nextgeneration systems will be comprised of both radio frequency (RF) and free-space optical (FSO) communication links, requiring satellites to provide communication services that perform demodulation and forward error correction (FEC) decoding of the received signal before re-encoding and forwarding the signal to other nodes in the network. Although this regenerative capability prevents the accumulation of errors as communications are routed throughout the network, the regenerative process incurs a significant increase in the design complexity of communication satellites, which requires both an effective FEC algorithm and high-performance processor architecture. In this paper, we propose a configurable, highthroughput, low-density parity-check (LDPC) decoder architecture accelerated on the AMD Versal Adaptive System-on-Chip (SoC), leveraging AI Engine (AIE) technology, as a potential solution for future communication networks. First, LDPC codes, a class of FEC algorithms used in advanced communications standards such as Wi-Fi (802.11n) and 10 G Ethernet (IEEE802.3an), are well-suited algorithms for their high-throughput and error-correction capabilities, and the iterative and parallelizable processes in LDPC decoding are highly amenable for acceleration. Second, the Versal SoC, a next-generation space-qualified device, features an adaptive, heterogeneous architecture enabling high-performance onboard processing. When evaluated on the Versal AI Edge, our accelerator can achieve up to 4.458 Gigabits per second (Gbps) at one iteration.

## Unequal Error Protection Scheme Based on Implicit Partial Product-LDPC Codes

- **Status**: ✅
- **Reason**: product-LDPC 기반 UEP 코드설계+turbo-like 반복 디코딩, NAND multi-page 차등보호로 이식 가능한 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11504662
- **Type**: conference
- **Published**: 27-29 Marc
- **Authors**: Xuemei Zhu, Jiawei Duan, Zhicheng Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/11504662
- **Abstract**: This paper proposes an unequal error protection (UEP) scheme based on implicit partial product-LDPC codes. All rows of the source data array are encoded by a low-density parity-check (LDPC) code, while only a prescribed subset of information columns is further protected by a Bose–Chaudhuri–Hocquenghem (BCH) code. The check information generated by the column code is not transmitted explicitly. Instead, it is superimposed on the row LDPC codewords through a free-ride coding mechanism. In this way, the selected columns, referred to as the most important data (MID), are protected by both the row code and the column code, whereas the remaining columns, referred to as the less important data (LID), are protected only by the row code. A turbo-like iterative decoding algorithm is then adopted for the proposed scheme, consisting of free-ride decoding, row decoding, column decoding, and row re-decoding. We further present an approximate performance characterization for the doubly protected MID and a genie-aided lower bound for the singly protected LID. Simulation results show that the proposed scheme provides a substantial reliability gain for the MID, while the LID performance is not sacrificed and can even outperform that of standalone LDPC coding in the medium-to-high signal-to-noise ratio (SNR) region.

## CRC-Aided External Iterative LDPC Decoding Algorithm for Slow Frequency-Hopping Interference Scenarios

- **Status**: ✅
- **Reason**: CRC-aided 외부반복 LDPC 디코딩으로 LLR 재가중·고신뢰 오류전파 억제, NAND LLR 처리에 이식 가능한 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11504822
- **Type**: conference
- **Published**: 27-29 Marc
- **Authors**: Xianbo Yang, Lei Xiao, Ye Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/11504822
- **Abstract**: In short-burst slow frequency-hopping (SFH) gaussian minimum shift keying (GMSK) systems under strong partial-band interference (PBI), the slot-varying interference state causes severe mismatch of the input log-likelihood ratios (LLR) for new radio low-density parity-check (NR-LDPC) decoding when channel state information (CSI) is unavailable. To address this issue, this paper proposes a cyclic redundancy check (CRC)-aided external iterative interference estimation and decoding scheme. Instead of using CRC only for post-decoding error detection, CRC-validated code blocks are exploited to reconstruct reliable reference symbols, based on which a slot-level residual metric is formed to estimate the interference impact and adaptively reweight the LLR in an external loop. The proposed approach effectively suppresses the propagation of high-confidence errors in the Tanner graph and accelerates the convergence of LDPC decoding. Simulation results under typical PBI scenarios demonstrate that the proposed scheme significantly improves the bit error rate (BER) performance and approaches the ideal CSI benchmark without introducing additional pilot overhead.

## Noisy Soft Syndrome Decoding of Quantum LDPC Codes for the Quantum Erasure Channel

- **Status**: ✅
- **Reason**: 양자 소거채널이나 hardware-friendly min-sum 기반 soft-syndrome 반복 디코더로 이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11478883
- **Type**: conference
- **Published**: 26 Feb.-1 
- **Authors**: Gayathri R., Shobhit Bhatnagar, P Vijay Kumar
- **PDF**: https://ieeexplore.ieee.org/document/11478883
- **Abstract**: Erasure decoding of quantum low-density paritycheck (QLDPC) codes has recently received a lot of interest as qubit erasures occur in many physical systems such as neutralatom systems, trapped-ion systems etc. However, decoding of QLDPC codes heavily relies on syndrome information, which may be unreliable as syndrome extraction circuits are prone to errors in practice. While syndrome errors are usually modeled as flipping of a binary syndrome bit, typically, measurement outcomes yield analog voltage/current values, which are then discretized to obtain the binary syndrome. Prior work on correcting qubit errors in the presence of syndrome noise shows that this soft (i.e., analog) information can be exploited to achieve performance improvement. In this paper, we consider the case of qubit erasures and present an iterative decoding algorithm, based on the hardware-friendly min-sum algorithm, that incorporates this soft information to perform check node updates. We show via simulations on hypergraph product codes and lifted product codes that our decoder achieves performance very close to that in the case of noiseless syndrome for a certain noise regime.

## LUT-Optimized RCQ LDPC Decoder for TLC Flash Memory Implementation on Xilinx FPGA

- **Status**: ✅
- **Reason**: TLC NAND 플래시용 RCQ QC-LDPC 디코더 FPGA 구현(A+D), 직접 적용 대상
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11476755
- **Type**: conference
- **Published**: 25-27 Marc
- **Authors**: Yury A. Zamaraev, Vasiliy S. Usatyuk, Sergey I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/11476755
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) decoders are indispensable in high-throughput storage and communication systems. This paper proposes a lookup-table (LUT)-based Reconstruction-Computation-Quantization (RCQ) decoder tailored for triple-level cell (TLC) NAND flash memory and implemented on a Xilinx Zynq UltraScale+ FPGA using high-level synthesis (HLS). By replacing costly arithmetic operations with pre-computed reconstruction and quantization tables, the RCQ architecture markedly reduces routing congestion while preserving decoding performance. We detail the algorithmic formulation, describe the QC-LDPC code, and explain table construction via density evolution coupled with importance-sampling-based error-floor optimization. The hardware design, synthesis results, and a comprehensive throughput analysis are also presented. Compared with state-of-the-art FPGA soft decoders for QC-LDPC codes, our solution-employing (3, 6)-bit quantization-delivers roughly twice the decoding throughput $(5.7 \text{Gb} / \mathrm{s}$ at an average of four iterations) with comparable resource utilization using LUT-based simplified routing. In addition, it achieves a raw bit-error-rate close (gain of 3.3%) relative to the Codelucida QC-LDPC code (code rate $R_{\text{code }}=0.89$, length $\mathrm{N}=32768$). These results demonstrate that LUT-optimized RCQ decoding offers an efficient and high-performance solution for flash memory applications.

## Hybrid Machine Learning Framework for Adaptive Error Correction in 6G Enabled IoT Systems

- **Status**: ✅
- **Reason**: RL 기반 반복 제어 + 신경망 소프트 디시전 결합 적응형 LDPC 디코딩 기법 포함, 이식 가능성 있어 보존(C) — Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11502755
- **Type**: conference
- **Published**: 16-18 Marc
- **Authors**: P Balakrishna, Pramod Kumar, S Gangadhar +3
- **PDF**: https://ieeexplore.ieee.org/document/11502755
- **Abstract**: There is the technology has made switching transition from 5G to 6G networks will bring about the new era of ultradense, intelligent, and latency-critical IoT applications. Energy-efficient and reliable communication is becoming important as IoT devices are exchangingdata among dynamic and heterogeneous channels even in billions. As billions of IoT devices are exchanging data via dynamic and heterogeneous channels, energy-efficient and reliable communication is becoming challenging and critical for thesustainable development of future communication networks. Traditional error correction schemes like Turbo, LDPC and Polar codes are known to bebounded by these effects due to their static decoding strategies. In this paper, we introduce a Hybrid MachineLearning (HML) framework based on supervised and reinforcement learning models to dynamically adapt error correction operations at run-time. The methodology is to merge neural network-aided decoding for soft-decision enhancement with RL-based iteration control for adaptivity and power-efficientcommunication. The results in Python and MATLAB confirm that, the proposed HML scheme can reduce the bit errorrate (BER) by up to 30
