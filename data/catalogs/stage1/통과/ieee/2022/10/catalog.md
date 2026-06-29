# IEEE Xplore — 2022-10 (1차선별 통과)


## On the Construction of QC-LDPC Codes Based on Integer Sequence With Low Error Floor

- **Status**: ✅
- **Reason**: 정수 시퀀스 기반 QC-LDPC 구성, girth>=8, elementary trapping set 제거, low error floor — 새 코드 설계 기법(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9810937
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Xiongfei Tao, Xin Chen, Bifang Wang
- **PDF**: https://ieeexplore.ieee.org/document/9810937
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes have efficient hardware implementation and excellent correcting performance. However, the existence of trapping sets can affect the decoding performance. In this letter, a novel class of QC-LDPC codes based on integer sequence with column weight 3 and girth at least 8 is proposed. If the numbers in the sequence are different, the QC-LDPC codes free of elementary trapping sets ( ${a}$ ,  ${b}$ ) with  ${a} \leq10$  and  ${b} \leq $  3 can be constructed. The row weight of the parity check matrix can be arbitrary and we give a lower bound of the circulant permutation matrix (CPM) size. Simulation results show that the generated codes have good performance with low error floor over AWGN channels.

## Adaptive Gradient Descent Bit-Flipping Diversity Decoding

- **Status**: ✅
- **Reason**: 새 BP-초월 비트플리핑 디코더(GDBF-w/M + 유전 최적화) 프레임워크 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9844740
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Srdan Brkic, Predrag Ivaniš, Bane Vasić
- **PDF**: https://ieeexplore.ieee.org/document/9844740
- **Abstract**: In this letter we propose a novel framework for designing decoders, for Low-Density Parity Check (LDPC) codes, that surpasses the frame error rate performance of Belief-Propagation (BP) decoding on binary symmetric channels. Its key component is the adaptation method, based on the genetic optimization algorithm, that is incorporated into the recently proposed Gradient Descent Bit-Flipping Decoding with Momentum (GDBF-w/M). We show that the resulting decoder outperforms all state-of-the-art probabilistic bit-flipping decoders and, additionally, it can be trained to perform beyond BP decoding, which is verified by numerical examples that include codes used in IEEE 802.3an and 5GNR standards. The proposed framework provides a systematic method for decoder optimization without requiring knowledge of trapping sets. Moreover, it is applicable to both regular and irregular LDPC codes.

## A Universal Efficient Circular-Shift Network for Reconfigurable Quasi-Cyclic LDPC Decoders

- **Status**: ✅
- **Reason**: 재구성형 QC-LDPC 디코더용 순환시프트(permutation) 네트워크 HW 개선 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9834322
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Suwen Song, Hangxuan Cui, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/9834322
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes for modern communication standards usually have multiple code rates and block lengths. Therefore, reconfigurable LDPC decoders have received widespread attention, which require circular-shift networks to support various expansion factors. Besides, for inputs smaller than the network size, the circular-shift network is desired to process multiple frames in parallel to maximize hardware utilization efficiency. The increasing demands put severe challenges to low-complexity implementations of shift networks, especially for codes with numerous expansion factors, such as 5G LDPC codes. In this brief, we present a universal design of efficient reconfigurable circular-shift networks. Through an ingenious modification on the order of permutations, the generation of control signals is considerably simplified, leading to a significant reduction of area and critical path. Moreover, a hybrid architecture organically integrating different networks is proposed for further complexity reduction. Implementation results under TSMC 90 nm technology demonstrate that the proposed network can achieve 25% area reduction and 46% area-efficiency (AE) improvement over the state-of-the-art ones.

## NoD: A Neural Network-Over-Decoder for Edge Intelligence

- **Status**: ✅
- **Reason**: 디코더 내부구조와 NN 유사성 활용한 FPGA NN-over-decoder HW — 이식 가능 디코더 HW(C/D), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9793711
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Arash Fouman Ajirlou, Farid Kenarangi, Eli Shapira +1
- **PDF**: https://ieeexplore.ieee.org/document/9793711
- **Abstract**: The ubiquitous applications of the Internet of Things (IoT) devices and the increasing computational capabilities of neural networks (NNs) have led to a new era of edge computing and a paradigm known as edge intelligence (EI). With EI, the goal is to maximize the utilization of resources available within an edge device, offloading only the most compute-intensive operations to the cloud. In this article, we propose to leverage the close similarity between the internal architecture of a typical network decoder and an NN for deep learning on decoders. The proposed NN-over-decoder is developed in Verilog and synthesized on field-programmable gate array (FPGA). Based on experimental results, the system exhibits power consumption of the same order of magnitude as a baseline decoder and negligible memory overhead while increasing local hardware utilization, alleviating the high communication load in typical communication devices, and offering scalable multiply–accumulate (MAC)/cycle performance compared with the state of the art.

## Achievable-Rate-Aware Retention-Error Correction for Multi-Level-Cell NAND Flash Memory

- **Status**: ✅
- **Reason**: MLC NAND 플래시 retention 오류 LLR 보정(MARC)·EM 기반 read voltage 조정 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9586047
- **Type**: journal
- **Published**: Oct. 2022
- **Authors**: Yingcheng Bu, Yi Fang, Guohua Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/9586047
- **Abstract**: Owing to the effect of data retention noise in multi-level-cell NAND flash memory, the initial threshold-voltage distributions and read voltages can no longer be used to accurately calculate log-likelihood ratios (LLRs) as the retention time increases, thus causing retention errors. To solve this problem, we first utilize the so-called “correction factors” to optimize the LLR accuracy by maximizing the achievable rate of a flash-memory system without introducing extra memory-sensing operations. We further prove that the optimization of the correction factors is a convex optimization problem and can be solved analytically. To obtain the optimal correction factors, we propose two retention-error correction schemes, referred to as offline maximum-achievable-rate correction (MARC) algorithm and online MARC algorithm, which enable the flash-memory controller to utilize the corrected LLRs that are stored in a look-up table and correct the inaccurate LLRs in real time, respectively. Motivated by the variation characteristics of the threshold-voltage distributions, we also propose an enhanced expectation–maximization (EM) algorithm to reestimate their corresponding parameters, and then adjust the read voltages. By combining the enhanced EM algorithm with the MARC algorithms, an enhanced EM-based correction strategy is developed to further boost the retention-error endurance of flash memory while avoiding excessive memory-sensing overhead. Theoretical analyses and simulation results illustrate the superiority of the proposed correction mehtods in terms of the robustness against retention errors.

## Work-in-Progress: Prediction-based Fine-Grained LDPC Reading to Enhance High-Density Flash Read Performance

- **Status**: ✅
- **Reason**: A — TLC/QLC 플래시에서 read level 예측 기반 fine-grained LDPC reading으로 read-retry 감소, NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9933162
- **Type**: conference
- **Published**: 7-14 Oct. 
- **Authors**: Yajuan Du, Yuan Gao, Qiao Li
- **PDF**: https://ieeexplore.ieee.org/document/9933162
- **Abstract**: LDPC codes have been widely applied in high-density flash memories, e.g., TLC flash and QLC flash, to ensure data reliability. In order to reduce the read latency of high-density flash memories, this paper proposes a prediction-based fine-grained LDPC reading method, named as PreLDPC. From a preliminary study, we observe that the ratio of cells that lie in error-prone areas (i.e., the areas between two adjacent cell states) is closely related to the final read level for successful decoding. Based on this observation, PreLDPC predicts the read level for LDPC reading, which could avoid excessive unnecessary read-retries. Furthermore, a fine-grained read method with fine sub-levels is used in the read-retry iteration for read latency reduction. From experimental results over real-world workloads on Disksim with SSD extensions, the effectiveness of PreLDPC on reducing read latency is verified in high-density flash memories.

## Work-in-Progress: High-Precision Short-Term Lifetime Prediction in TLC 3D NAND Flash Memory as Hot-data Storage

- **Status**: ✅
- **Reason**: A — 3D TLC NAND read disturb 수명예측으로 LDPC 코드를 동적 조정하는 스토리지 직접 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9933059
- **Type**: conference
- **Published**: 7-14 Oct. 
- **Authors**: Xiaotong Fang, Meng Zhang, Yifan Guo +6
- **PDF**: https://ieeexplore.ieee.org/document/9933059
- **Abstract**: In this paper, read disturb (RD) at various program/erase (P/E) stages has been thoroughly explored, and short-term lifetime prediction models of RD and endurance are proposed. Based on these, a new short-term warning system (STWS) is proposed, which can extend the lifetime of 3D NAND-based storage by adjusting LDPC codes dynamically. The experimental result shows that the proposed prediction models have high reliabilities, and STWS can effectively prolong the lifetime of NAND flash.

## High Throughput FPGA Implementation of LDPC Decoder Architecture for DVB-S2X Standard

- **Status**: ✅
- **Reason**: QC-LDPC FPGA 디코더, 360 병렬코어 layered min-sum HW 아키텍처 — D(이식 가능 HW)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9976733
- **Type**: conference
- **Published**: 3-7 Oct. 2
- **Authors**: E. A. Likhobabin, A. A. Ovinnikov, R. S. Goriushkin +2
- **PDF**: https://ieeexplore.ieee.org/document/9976733
- **Abstract**: This paper is devoted to the design of a decoder structure for Quasi-Cyclic (QC) Low-Density Parity-Check (LDPC) codes of the DVB-S2X standard. The quasi-cyclic form of the matrix representation is the most convenient for the hardware implementation of the LDPC decoder, so the matrices of the DVB-S2X standard are converted to the QC form. The implementation of an LDPC decoder for the DVB-S2X standard is a challenging task, especially because of the long code words and large parity-check matrices. We propose a highly parallel FPGA implementation of LDPC decoder design based on the layered architecture and Min-Sum decoding algorithm. The structure of the decoder consists of 360 parallel cores responsible for the sequential calculation of variable-to-check (VTC), check-to-variable (CTV) messages and update posterior probabilities (APPs). Block RAM memory was used to store intermediate values of APP and CTVs. The decoder design is applicable to all code rates and allows to achieve throughput up to 500 Mbps at a clock frequency of 250 MHz

## Design and Implementation of Hard-Decision LDPC Decoder

- **Status**: ✅
- **Reason**: 새 hard-decision 비트플립 디코더(DPGDBF) 알고리즘+FPGA HW 구현 제시, NAND LDPC에 이식 가능 (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10011285
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Yi Dong, Huimin Du, Shengfei Bai +3
- **PDF**: https://ieeexplore.ieee.org/document/10011285
- **Abstract**: Hard-decision LDPC decoders are widely used in communication and storage systems due to their simple circuits. However, existing hard decision LDPC decoding circuits lead to slow decoding convergence due to flipping according to the maximum energy value, reducing decoding performance. This paper proposes the Dual-Energy Probabilistic Gradient Descent Bit-Flipping (DPGDBF) hard-decision algorithm. If the energy value of the variable node reaches the threshold, all nodes with the threshold energy will be flipped, and the node with the sub-maximum threshold energy will be flipped with a certain probability. otherwise, only all variable nodes with the maximum energy value are flipped. The simulation results show that, in a limited iterative range, compared with Tabu-list Random-Penalty Gradient Descent Bit-Flipping (TRGDBF), for (2048, 1024) codes, the average number of decoding iterations of the algorithm is reduced by 12%, and the decoding performance is improved to a certain extent; for (9216,7680) codes, the average number of decoding iterations of the DPGDBF algorithm is reduced by 18%, and the decoding performance is improved by 4 times. In addition, this paper proposes a hardware implementation of the DPGDBF algorithm for (2048, 1024) codes, with a maximum clock frequency of 305.53MHz and a through-put of 19.52Gbps.

## An Improved Codec Design Architecture for Irregular LDPC Codes Applicable to WiMAX

- **Status**: ✅
- **Reason**: WiMAX irregular LDPC 인코더/디코더 FPGA 구현, irregular용 null bypassing logic 신규 + QC 확장 가능 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9970908
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Divita Shri, Arijit Mondal, Shayan Srinivasa Garani
- **PDF**: https://ieeexplore.ieee.org/document/9970908
- **Abstract**: We propose the design architecture of the Low-density parity-check (LDPC) encoder and decoder based on the WiMAX standard (IEEE 802.16e). The design architectures were implemented on a Kintex-7 KC705 field-programmable gate array (FPGA) kit, for a rate 1/2 WiMAX LDPC code with a code length of 2304, containing twelve layers in the parity check matrix. A new null bypassing logic for irregular LDPC decoder is proposed. The tool reported a total power of 0.677 W for encoder with a throughput of 364 Gbps. The tool reported a total power of 1.009 W for the decoder with a throughput of 0.0785 Gbps (78.5 Mbps) for five iterations. Our architecture is also amenable for constructing non-binary LDPC codes where each bit of the non-binary code is binary coded and interleaved, useful for applications in optical transmission channels. Our architecture is also scalable for a wide range of quasi-cyclic code parameters.

## A Fast Decoding Convergence of SISO Repetition - QC-LDPC Codes Concatenated at the Receiver

- **Status**: ✅
- **Reason**: 수신단 SISO repetition + OMS 연결 디코딩으로 수렴 가속 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9942436
- **Type**: conference
- **Published**: 22-24 Oct.
- **Authors**: Amr Tarek, Amr Abdelaziz, Hisham Al–Dahshan
- **PDF**: https://ieeexplore.ieee.org/document/9942436
- **Abstract**: Low-Density Parity Check (LDPC) is one of the contemporary error-correcting codes that has shown near Shannon capacity performance; it has been implemented into various stan-dards such as the second-generation Digital Video Broadcasting for Satellite (DVB-S2) and eventually made its way toward the 5G New Radio (NR) for the data channel. In an effort to enhance the LDPC decoding performance without a significant increase in the decoding complexity, in this paper, a receiver-based concatenated decoding approach is proposed, which is composed of the soft-input soft-output (SISO) repetition and offset min-sum (OMS) algorithm representing outer and inner decoders, respectively. At the receiver, the received signal is oversampled with an oversampling rate (OSR) faster than multiple integers of the Nyquist rate to produce repeated symbols. Moreover, the repetition employed at the receiver to handle the repeated symbols will not impact the coding rate. Finally, the simulation results revealed that the proposed scheme could accomplish faster-decoding convergence compared to the conventional LDPC decoders and achieve coding gain up to 2.3 dB with OSR = 2. Additionally, the computational complexity does not increase significantly; on the contrary, the achieved gain can be exploited to reduce the number of iterations.

## Modified Noisy Gradient Descent Bit-Flipping Decoding Algorithms for LDPC Codes

- **Status**: ✅
- **Reason**: M-NGDBF 비트플립 디코더 개선(노이즈생성기 제거·tabu-list)으로 새 디코더 알고리즘 — 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9942999
- **Type**: conference
- **Published**: 20-22 Oct.
- **Authors**: Yidong Li, Wai M. Tam, Francis C.M. Lau
- **PDF**: https://ieeexplore.ieee.org/document/9942999
- **Abstract**: In this paper, we propose modified multi-bit noisy gradient descent bit flipping (M-NGDBF) algorithms for decoding low-density parity-check codes. To simplify the decoder design, we eliminate the use of Gaussian noise generators at the decoder and replace them with received signals after simple transformations. We then improve the convergence rate by removing the randomness in the M-NGDBF algorithm during the first few iterations. Subsequently, we construct a tabu-list to record bits that are flipped in the current iteration and allows these bits to be flipped in the next iteration only with a very small probability. Simulation results show that our proposed algorithms outperform the original M-NGDBF algorithm in terms of both bit error rate and convergence rate.

## Detecting Minimum Distance of LDPC Codes with Improved Approximately Nearest Codeword Method

- **Status**: ✅
- **Reason**: LDPC 최소거리 검출 ANC 개선(새 노이즈주입·디코딩·스케줄링·탐색 전략). 코드설계/error floor 분석 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9950957
- **Type**: conference
- **Published**: 20-21 Oct.
- **Authors**: Zhewei Tong, Kewu Peng, Zhitong He
- **PDF**: https://ieeexplore.ieee.org/document/9950957
- **Abstract**: Approximately nearest codeword (ANC) is a classic approach for detecting minimum distance of low-density parity-check (LDPC) codes. With the principle of local search, ANC method is capable of detecting minimum distance of LDPC codes within acceptable time. However, the message passing (MP) decoding algorithm and scheduling scheme, as well as the local search strategy, still have much space to improve. To fill the gap, this paper proposes an improved-ANC method which employs novel noise introduction method, decoding algorithm, scheduling scheme and searching strategy, to accelerate the computation of the minimum distance of LDPC codes significantly. Finally, we run simulations on LDPC codes in Wi-Fi5 and 5G-NR standards. The simulation results are presented and demonstrate the effectiveness of our proposal.

## Low Power Decoder Architecture of Product Code for Storage Controller

- **Status**: ✅
- **Reason**: 3D NAND 스토리지 컨트롤러용 저전력 product code 디코더 HW, LDPC 동급 대비 전력저감(D/A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10031469
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Sumin Kim, Byungmin Ahn, Bohwan Jun +3
- **PDF**: https://ieeexplore.ieee.org/document/10031469
- **Abstract**: Error correction codes (ECCs) are essential for correcting the errors caused by the physical characteristics of 3D NAND flash in flash solution products. In this paper, we introduce low power decoder architecture for product code. Precisely, by using Hamming product code and Chase-Pyndiah algorithm, this work takes not only the same correction capability and area as low-density parity-check decoder, but also less power with relatively simple operation for decoding. Only the log likelihood ratios of error-suspicious bits are gathered in SRAM for the next iteration of decoding, so that the power consumption and area of SRAM read/write decrease. Compared with the conventional ECC decoder with the same correction capability and area, our decoder has achieved an average power reduction of 22.4%.

## A DNN-based Decoding Scheme for Communication Transmission System over AWGN Channel

- **Status**: ✅
- **Reason**: C: DNN 기반 디코딩 스킴, 신경망 디코더로 바이너리 LDPC 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9940380
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Meilin He, Yanchao Lei, Huina Song +3
- **PDF**: https://ieeexplore.ieee.org/document/9940380
- **Abstract**: A communication transmission system with channel coding and deep neural network (DNN)-based decoding is considered. A DNN-based decoding scheme is proposed for reliable transmission. The decoding scheme is accomplished by efficient local decoding at all the neurons and interactions in the input, hidden and output layer. Specifically, firstly, the nonlinear operations at each neuron and the linear operations of the weights and biases at each edge are performed by the local decoding. Secondly, the weights and biases are updated by gradient descent (GD) algorithm, based on the estimated loss value. This process above is performed iteratively until the message sequence has been recovered. Simulation results show that our proposed decoding scheme performs well. Moreover, our decoding scheme performs significantly better than the conventional hard decision.

## The Effect of PEG-Lifting Order on the Performance of Protograph GLDPC Codes

- **Status**: ✅
- **Reason**: PEG-lifting 순서로 GLDPC 로컬 사이클 분포 제어 — 바이너리 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9943671
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Dae-Young Yun, Jae-Won Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/9943671
- **Abstract**: Generalized low density parity check (GLDPC) codes can be constructed by replacing some single parity check (SPC) nodes in LDPC codes with generalized constraint (GC) nodes. GC nodes are defined by component codes whose minimum distance is larger than that of SPC nodes. Therefore, the variable nodes (VNs) connected to GC nodes, which are called doped VNs, are more protected than the undoped VNs. Due to this effect, we observe that the doped VNs are more robust to local cycles. The distribution of local cycles is affected by the processing VN order of the progressive edge growth (PEG) algorithm, where the latter processed (lifted) VNs tend to have more local cycles. Based on the property of doped VNs and the PEG algorithm, we show that a tangible performance gain is achieved by placing the doped VNs in the latter order of the PEG algorithm compared to the former order. The performance gain is shown with a well known GLDPC code in the literature and over both the binary erasure channel and addictive white Gaussian noise channel.

## Current Trends on Deep Learning-aided Channel Coding

- **Status**: ✅
- **Reason**: 딥러닝 기반 채널코딩/LDPC 디코딩 서베이 — 신경망 디코더(C) 관련, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9952535
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Tuyet-Mai Dang, Eunyoung Cho, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/9952535
- **Abstract**: Artificial intelligence (AI)-aided approaches are emerging in solving physical layer communication problems. In this paper, we focus on applications of deep learning (DL) in channel coding for wireless communications and provide a survey on related topics. We describe various decoding problems of short linear codes and LDPC codes assisted by deep neural networks. The survey will be concluded with a list of future research directions.

## Sneak Path Aware Bit-Flipping Algorithm for ReRAM Crossbar Array

- **Status**: ✅
- **Reason**: 신뢰도 side info 활용 bit-flipping 디코딩(ReRAM) — 스토리지 ECC + 이식 가능 BF 디코더(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9952863
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Myungin Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/9952863
- **Abstract**: Resistive random access memory (ReRAM) has unique features such as fast data processing speed, non-volatility and high density and thus has been gaining popularity in a wider range storage applications. Meanwhile, ReRAM suffers from read errors mainly due to the variations of cell resistance and the sneak path problem. There have been efforts to cope with the read errors using error-correcting codes such as low-density parity-check (LDPC) codes and Bose-Chaudhuri-Hocquenghem (BCH) codes. In this paper, we propose a simple bit-flipping (BF) decoding algorithm for correcting read errors in ReRAM due to the sneak paths and show that the proposed algorithm efficiently resolves the sneak path problem at reduced complexity. In particular, we assume that ReRAM provides certain side information about the reliability of retrieved bits, and the proposed algorithm utilizes the side information in the decoding. Error-rate performance of the proposed algorithm is compared with that of an existing BF algorithm, which shows a clear performance improvement with the proposed one.

## Selective Layered BP Decoding for low-latency NR LDPC Codes

- **Status**: ✅
- **Reason**: Selective layered BP 디코딩(펑처드 코드 모호성 제거) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9952457
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Chanho Yoon, Woncheol Cho, Young-Jo Ko
- **PDF**: https://ieeexplore.ieee.org/document/9952457
- **Abstract**: In this paper, we propose selective layered BP decoding approach for decoding 3GPP NR rate compatible punctured LDPC codes that eliminates the ambiguity of BP decoding for information bit punctured codes. Conventional BP or layered BP decoding approach for NR LDPC codes does not perform well in frequency selective fading channels, and, with the sub iteration applying to the sub matrix portion, the proposed SL layered BP decoding improves the performance drastically. We show that faster decoding speed by applying the proposed scheme to the 3GPP NR LDPC code is achieved in terms of decoding latency.

## Performance Analysis of QC-LDPC codes constructed by using Golomb rulers

- **Status**: ✅
- **Reason**: Golomb ruler 기반 girth-8 QC-LDPC 구성법 — 바이너리 코드 설계 기법(E), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9943662
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Daekyeong Kim, Inseon Kim, Hyunwoo Cho +2
- **PDF**: https://ieeexplore.ieee.org/document/9943662
- **Abstract**: In this paper, we analyzes performance of girth-8 regular QC-LDPC codes constructed using Golomb ruler. We conducted simulations to measure FER performance of QC-LDPC codes constructed by changing the last mark of some optimal Golomb ruler and found the value of the mark that shows the best performance.

## Evaluation of the Effects of SEUs on Configuration Memories in FPGA Implemented QC-LDPC Decoders

- **Status**: ✅
- **Reason**: FPGA QC-LDPC 디코더 SEU 신뢰성/병렬화 분석 — HW 아키텍처(D) 관련, 애매하므로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9962337
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Zhen Gao, Yinghao Cheng, Pedro Reviriego
- **PDF**: https://ieeexplore.ieee.org/document/9962337
- **Abstract**: LDPC codes are widely used in wireless communication systems for reliable data transmission due to their excellent error correction capabilities. SRAM-FPGAs are a popular option for the implementation of LDPC decoders due to their excellent computing capabilities and re-configurability. However, when applied in critical environments, e.g. space platforms, the SRAM-FPGA based LDPC decoders will suffer single-event upsets (SEUs) that can cause failures and disrupt communications. Therefore, analyzing the reliability of LDPC decoders to SEUs on the FPGA is important. This paper first analyzes the effects of SEUs on different parts of the FPGA implemented LDPC decoder based on the module functions, including the influence of the parallelism on the decoder reliability. Then fault injection experiments are performed to validate the conclusions of the analysis. Experiment results show that about 98% of SEUs on the configuration memories can be tolerated by the decoder itself, and the modules with more interconnections are less robust to SEUs. In addition, the reliability of LDPC decoders decreases for lower levels of parallelism due to the larger computation load of each unit. These results will be a valuable input to design efficient SEU protection schemes for LDPC decoders.

## A Class of Cyclic Partial Geometries and Their Associated Constant Weight and LDPC Codes

- **Status**: ✅
- **Reason**: 유한체 기반 cyclic/QC-LDPC 새 부호 구성(triplet partial geometries) — 바이너리 코드 설계 기법, 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10683925
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Juane Li, Yi Gong, Xin Xiao +2
- **PDF**: https://ieeexplore.ieee.org/document/10683925
- **Abstract**: This paper presents a class of cyclic partial geometries, called triplet partial geometries, which are constructed based on finite fields of characteristic 2. Using these partial geometries, constant-weight codes and LDPC codes with cyclic and quasi-cyclic structure are constructed.

## Implementation of Multi Bit Error Detection and Correction using Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: Multi-bit error detection/correction(MBE-DCC) 인코더·디코더 구현, 기존 LDPC 대비 성능 향상 주장 — 디코더/구성 기법 가능성, 애매하여 in(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9970166
- **Type**: conference
- **Published**: 15-16 Oct.
- **Authors**: Banoth Suman, M. Jagadeesh Chandra Prasad
- **PDF**: https://ieeexplore.ieee.org/document/9970166
- **Abstract**: Data transmission in advanced space communications are suffering with the different types of noises. Further, these noises cause burst errors in data. Thus, the low-density parity checking codes (LDPC) plays the major role to detect and correct the errors. However, the conventional hamming encoders, decoders were detected and corrected only one bit error. Therefore, this work implementation the Multi-Bit Error Detection and Correction Codes (MBE-DCC) for multiple bits error detection and correction. Initially, MBE-DCC encoding operation is implemented by using generator matrix, which contains both identity bits and parity bits. Then, encoded code word is transmitted into the channel of space communication, where encoded data corrupted by different types of noises, errors. Therefore, the MBE-DCC decoding operation performed at receiver side of space communications, which corrected all the errors using syndrome detection, error location detection, and error correction modules. The simulations revealed that the proposed MBE-DCC resulted in superior performance than conventional LDPC methods.

## Decoder Implementation of Spatially Coupled LDPC Codes

- **Status**: ✅
- **Reason**: SC-LDPC 코덱 FPGA 설계/구현(xc7k325t); 무선이지만 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9998153
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Jian Yang, Danfeng Zhao, Hai Tian +2
- **PDF**: https://ieeexplore.ieee.org/document/9998153
- **Abstract**: In order to meet the requirements of high reliability and high flexibility of wireless communication, the Space-coupled Low-Density Parity-Check (SC-LDPC) codes are deeply studied. At present, the main research direction of SC-LDPC codes is to reduce the complexity of the algorithm and reduce the occupation of decoding resources. In terms of hardware implementation, there is relatively little research. Therefore, in view of the above problems, considering hardware resource occupation and coding and decoding performance, the FPGA design and implementation of the SC-LDPC code codec are carried out, and the functional correctness test is carried out on the Xilinx xc7k325tffg900-2 chip.

## An Improved Hybrid LDPC Decoder over Rayleigh Fading Channel

- **Status**: ✅
- **Reason**: 단순화 SPA + 개선 noisy gradient descent bit-flipping 2단 하이브리드 디코더 — 이식 가능한 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10013650
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Reza Biazaran, Hermann J. Helgert
- **PDF**: https://ieeexplore.ieee.org/document/10013650
- **Abstract**: Soft decision decoders applicable to low density parity check codes such as sum product algorithms provide excellent error performance, however, it comes at the expense of computational complexity. Additionally, many iterations may be required of these decoders to achieve desired error performance. The processing delay associated with too many iterations may be a drawback for cases where low latency is a critical requirement. Conversely, performance of hard decision decoders such as bit flipping decoder and its variants, while improved, generally are not on par with that of soft decision decoders. Such decoders also require many iterations to achieve a given error performance. We have proposed a two-stage hybrid decoder with a simplified sum product algorithm (SPA) in the first stage, and an improved noisy gradient decent bit flipping decoder in the second stage. We have shown that our proposed hybrid decoder outperforms the legacy individual decoders, studied in this paper, from error performance point of view as well as required number of iterations that will reduce the overall network latency.
