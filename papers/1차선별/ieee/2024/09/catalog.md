# IEEE Xplore — 2024-09 (1차선별 통과)


## On Construction of Low-Density Parity-Check Codes for Ultra-Reliable and Low Latency Communications

- **Status**: ✅
- **Reason**: PBRL LDPC 신규 구성법(차수분포 최적화·QR base matrix·masking·수정 PEG), 바이너리 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10507064
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Linqi Zou, Hao Yan, Jie Dong +3
- **PDF**: https://ieeexplore.ieee.org/document/10507064
- **Abstract**: Low-density parity-check (LDPC) codes with protograph-based raptor-like (PBRL) structure have been chosen as the data channel coding scheme for the fifth-generation (5G) enhanced mobile broad band (eMBB) services. However, these 5G LDPC codes are not optimized for the scenarios of Ultra Reliable and Low Latency Communications (URLLC) and massive Machine Type Communications (mMTC) in which small transport block sizes are usually used. In this paper, a new method is proposed to construct PBRL LDPC codes for URLLC and mMTC. This method incorporates degree-distribution optimization, base matrix derived from parity-check matrix of quadratic residue codes, masking technique and modified progressive-edge-growth (PEG) algorithm. Simulation results show that the proposed PBRL LDPC codes outperform 5G LDPC short codes in terms of error-correcting performance.

## Improvement of SP Decoding Considering the Influence of Recording Patterns by Neural Network in SMR

- **Status**: ✅
- **Reason**: SMR 스토리지용 신경망 기반 sum-product 디코딩 LLR 갱신 개선(C) — 이식 가능 디코더 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10534790
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Madoka Nishikawa, Yasuaki Nakamura, Yasushi Kanai +1
- **PDF**: https://ieeexplore.ieee.org/document/10534790
- **Abstract**: We study a low-density parity-check (LDPC) encoding and iterative decoding system for a shingled magnetic recording (SMR). In particular, we show the usefulness of applying a neural network in iterative decoding. We previously adopted the neural network to evaluate the log-likelihood ratio (LLR) related to row operations on the parity check matrix for the decoding target bit and improved the sum-product (SP) decoding. In this study, we propose to update the LLR considering the influence of noise depending on the recording pattern by providing the LLRs for the decoding target and its adjacent bits to the neural network in SP decoding. In addition, we explore the parameters to update the LLRs by applying the genetic algorithm (GA) to achieve more effective iterative decoding.

## High-Throughput and Hardware-Efficient ASIC-Chip Fabrication of Reconfigurable LDPC/Polar Decoder for mMTC and URLLC 5G-NR Applications

- **Status**: ✅
- **Reason**: 재구성형 LDPC/Polar 디코더 ASIC, 신규 데이터플로우·공유메모리 아키텍처 — NAND LDPC HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10607975
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Anuj Verma, Rahul Shrestha
- **PDF**: https://ieeexplore.ieee.org/document/10607975
- **Abstract**: This manuscript proposes hardware-efficient and high-throughput reconfigurable architecture of the channel decoder for unified decoding of LDPC or polar code. It has been designed based on the new dataflow technique for reconfigurable decoding that incurs lesser hardware resources in the decoder design. In addition, this work presents memory-organized architecture that exploits the shared-memory hardware and also excludes various conventional sub modules. Furthermore, this reconfigurable LDPC/polar decoder has been ASIC fabricated in UMC 110 nm-CMOS technology node, occupying an area of 1.96 mm2. It supports multiple code-rates and code-lengths that are compliant to mMTC and URLLC applications of 5G-NR wireless communication standard. At the supply voltage of 1.2 V, the proposed decoder-chip operates at the measured clock frequency of 72.7 MHz and delivers a data throughput of 3.35 Gbps that is  $4{\times }$  higher than the state-of-the-art implementation. It also consumes 15.8% lesser area and achieves  $2.5{\times }$  better hardware-efficiency in comparison to the contemporary works.

## Trainable Joint Channel Estimation, Detection, and Decoding for MIMO URLLC Systems

- **Status**: ✅
- **Reason**: 짧은 LDPC용 ADMM 언폴딩 신경망 JCDD — MIMO 결합이나 언폴딩 디코더 개념 이식 여지(C), 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10506472
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Yi Sun, Hong Shen, Bingqing Li +4
- **PDF**: https://ieeexplore.ieee.org/document/10506472
- **Abstract**: The receiver design for multi-input multi-output (MIMO) ultra-reliable and low-latency communication (URLLC) systems can be a tough task due to the use of short channel codes and few pilot symbols. Consequently, error propagation can occur in traditional turbo receivers, leading to performance degradation. Moreover, the processing delay induced by information exchange between different modules may also be undesirable for URLLC. To address the issues, we advocate to perform joint channel estimation, detection, and decoding (JCDD) for MIMO URLLC systems encoded by short low-density parity-check (LDPC) codes. Specifically, we develop two novel JCDD problem formulations based on the maximum a posteriori (MAP) criterion for Gaussian MIMO channels and sparse mmWave MIMO channels, respectively, which integrate the pilots, the bit-to-symbol mapping, the LDPC code constraints, as well as the channel statistical information. Both the challenging large-scale non-convex problems are then solved based on the alternating direction method of multipliers (ADMM) algorithms, where closed-form solutions are achieved in each ADMM iteration. Furthermore, two JCDD neural networks, called JCDDNet-G and JCDDNet-S, are built by unfolding the derived ADMM algorithms and introducing trainable parameters. It is interesting to find via simulations that the proposed trainable JCDD receivers can outperform the turbo receivers with affordable computational complexities.

## A Threshold-Based Binary Message Passing Decoder With Memory for Product Codes

- **Status**: ✅
- **Reason**: 임계값 기반 바이너리 메시지패싱+메모리 연판정 반복디코더+DE 분석 — 바이너리 반복디코더 기법으로 이식 가능성(C), 애매하여 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10485466
- **Type**: journal
- **Published**: Sept. 2024
- **Authors**: Xinwei Zhao, Shancheng Zhao, Qingyong Deng +2
- **PDF**: https://ieeexplore.ieee.org/document/10485466
- **Abstract**: Product codes (PCs) are typically decoded using iterative bounded distance decoding (iBDD) to ensure a low decoding complexity. To obtain further performance gain, a soft-aided decoding algorithm, termed the iBDD with scaled reliability (iBDD-SR), was proposed for PCs. In this paper, we propose an enhanced iBDD-SR by introducing threshold and memory when passing messages between the component decoders. The resulting algorithm is referred to as the threshold-based binary message passing (TB-BMP) with memory. In the proposed decoding algorithm, the soft reliability of the BDD output at the current half-iteration is a weighted sum of the BDD output, the channel reliability, and the content of the memory unit, where the content of the memory unit at the current half-iteration is related to the selected threshold and the BDD output at last half-iteration. Due to the existence of memory, the Bayesian network is used to model the decoding process of the TB-BMP. Based on the Bayesian network, we derive the density evolution (DE) equations for the TB-BMP under the constraint of extrinsic message passing (EMP). The analytical results of the DE analysis can be used to guide the selection of the parameters of the TB-BMP decoder. Extensive simulation results show that the TB-BMP decoder outperforms the iBDD-SR over the binary-input additive white Gaussian noise (Bi-AWGN) channels. In particular, for a PC based on a two-error-correcting extended Bose-Chaudhuri-Hocquenghem (BCH) code of length 256, the TB-BMP decoder performs about 0.28 dB better than the iBDD-SR at a bit error rate (BER) of 10−7.

## A Relaxation Oscillator-Based Probabilistic Combinatorial Optimization Engine for Soft Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: 오실레이터 기반 조합최적화 엔진으로 LDPC 소프트 디코딩 — 새 디코더/HW 아키텍처(C/D) 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10719549
- **Type**: conference
- **Published**: 9-12 Sept.
- **Authors**: Evangelos Dikopoulos, Luke Wormald, Ying-Tuan Hsu +4
- **PDF**: https://ieeexplore.ieee.org/document/10719549
- **Abstract**: Drawing insights from quantum computing, oscillator-based computing leverages continuous-time operation and massive parallelism to accelerate challenging computational tasks. This work advances the field to demonstrate a Combinatorial Optimization Problem (COP) engine for efficient, robust, one-shot oscillator-based soft decoding of LDPC codes for the first time. We present a 28 nm CMOS prototype that achieves a Frame, Bit Error Rate (FER, BER) of $1.38 \times 10^{-5}, 1.25 \times 10^{-6}$ respectively at 7 dB SNR and an energy efficiency of $5.26 \mathrm{pJ} / \mathrm{bit}$, which surpasses the normalized efficiencies of recent state-of-the-art decoders [1][2][3] by 11x, 3 x, 1.5 x respectively. Tested with more than 100 million frame decodings, the prototype demonstrates consistent performance across a range of SNRs, supply voltages, and temperatures.

## Erasure Decoding for Quantum LDPC Codes via Belief Propagation with Guided Decimation

- **Status**: ✅
- **Reason**: 양자 LDPC지만 BPGD 디코더가 고전 바이너리 BP에서 유래, damping·초기 LLR 조정 등 BP 개선 기법이 스태빌라이저 비의존으로 이식 가능(C) — 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10735275
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Mert Gökduman, Hanwen Yao, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/10735275
- **Abstract**: Quantum low-density parity-check (LDPC) codes are a promising family of quantum error-correcting codes for fault tolerant quantum computing with low overhead. Decoding quantum LDPC codes on quantum erasure channels has received more attention recently due to advances in erasure conversion for various types of qubits including neutral atoms, trapped ions, and superconducting qubits. Belief propagation with guided decimation (BPGD) decoding of quantum LDPC codes has demonstrated good performance in bit-flip and depolarizing noise. In this work, we apply BPGD decoding to quantum erasure channels. Using a natural modification, we show that BPGD offers competitive performance on quantum erasure channels for multiple families of quantum LDPC codes. Furthermore, we show that the performance of BPGD decoding on erasure channels can sometimes be improved significantly by either adding damping or adjusting the initial channel log-likelihood ratio for bits that are not erased. More generally, our results demonstrate BPGD is an effective general-purpose solution for erasure decoding across the quantum LDPC landscape.

## Graph Codes for Dual-Parameter Barrier Channels

- **Status**: ✅
- **Reason**: 두 바이너리 구성부호의 패리티체크 그래프 상 결합 메시지패싱 디코더 신규 제안 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10735324
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Yuval Ben-Hur, Saar Stern, Yoav Cohen +1
- **PDF**: https://ieeexplore.ieee.org/document/10735324
- **Abstract**: A ternary barrier channel is a non-symmetric error model defined previously to address emerging applications. Conveniently, it admits a code-construction method comprising two binary constituent codes. In this paper we propose a decoding algorithm that decodes the two constituent codes jointly by message passing on a graph representing the two codes' parity-check constraints. The messages exchanged by the algorithm are likelihoods calculated from incoming messages, and they are derived in the paper based on the exact dependence between the binary values of the two codewords. Simulation results demonstrate that the proposed decoder has superior error-rate performance compared to prior decoding approaches.

## Design and Implementation of Partially Parallel LDPC Decoder for Low Earth Orbit Micro-Nano Satellites Data Transmission

- **Status**: ✅
- **Reason**: 저궤도 위성용 부분 병렬 LDPC 디코더 FPGA 구현(순환 부행렬→RAM 매핑), 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10881440
- **Type**: conference
- **Published**: 22-25 Sept
- **Authors**: Chong Huang, Zhi Hou, Peng Li +1
- **PDF**: https://ieeexplore.ieee.org/document/10881440
- **Abstract**: This paper proposes a LDPC decoder for Low Orbit Micro-Nano Satellites Date Transmision. By analyzing the H-matrix characteristic, each cyclic sub matrix of the H-matrix is mapped to a Ramdom Access Memory(RAM). The address and data lines of the RAM are fully utilized to realize that RAM can be represented as both an H -matrix and an information storage matrix. The results on FPGA platform show that when the Eb/N0 is 4dB, the throughput of the decoder reaches 145Mbps, which improves the margin of data transmission links and meets the demand for data transmission. The decoder has completed in orbit verification on the experiment verification satellites.

## High-Speed Design Approaches for CCSDS LDPC Encoder Systems

- **Status**: ✅
- **Reason**: AR4JA QC-LDPC 인코더 FPGA HW 구현(블록순환 생성행렬, 속도·자원 개선) — 이식 가능 HW 아키텍처(D), 바이너리 LDPC
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10775118
- **Type**: conference
- **Published**: 21-22 Sept
- **Authors**: Jeeshma T.N, Pargunarajan K
- **PDF**: https://ieeexplore.ieee.org/document/10775118
- **Abstract**: In this paper, the implementation of a QC-LDPC encoder using AR4JA photograph LDPC is presented. This design utilizes a block-cyclic generator matrix from a quasi-cyclic parity check matrix to reduce encoder complexity. Additionally, an increase in speed of 22.87 % and a reduction in resource utilization of 14.28 % is also achieved through this method. The synthesis report of the utilization summary and delay from Vivado is shown and compared with an efficient QC- LDPC encoder using the Richardson Urbanke algorithm. FPGA implementation is also performed for the proposed design.

## Parallel optimization design of LDPC decoder with variable normalization factor

- **Status**: ✅
- **Reason**: 가변 정규화 계수 + 층내 병렬 LDPC 디코더 HW — NMS 변형 및 병렬 아키텍처(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10762031
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Kaidi Liu, Ziwei Guo
- **PDF**: https://ieeexplore.ieee.org/document/10762031
- **Abstract**: In order to solve the problem of poor decoding performance of the fixed normalization factor in the normalized minimum sum algorithm, the article proposes a variable normalization factor LDPC decoder, which improves the decoding performance compared to the fixed normalization factor. 0.2dB. At the same time, in order to solve the problems of low throughput and high storage resource usage of some parallel LDPC decoders, the parallelism of the system is increased by adopting the intra-layer parallel structure, and the consumption of storage resources is saved by time-division multiplexing of node data cache units. Experimental results show that compared with the traditional partially parallel structure, the decoder designed in this paper uses 13% more LUT resources, reduces storage resource consumption by 38%, and increases the decoding throughput by 14.5M.

## Inception-ResNet Assisted Iterative Decoding Algorithm Based on Alternating Direction Multiplier Method

- **Status**: ✅
- **Reason**: Inception-ResNet 신경망 보조 ADMM LDPC 디코더 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10691538
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Cunrui Feng, Fan Zhou, Dengyun Cao
- **PDF**: https://ieeexplore.ieee.org/document/10691538
- **Abstract**: The application of deep learning to channel decoding methods has gradually become a hot research topic. However, the high complexity of deep neural network (DNN) parameters hinders the application of deep neural networks to long codes, and the difficulty of decoding increases exponentially with the increase of code length. To address this problem, this paper proposes a low-density parity-check (LDPC) decoding based on alternating direction multiplier method (ADMM) assisted by Inception-RestNet network. After passing through the channel with the noise codeword through the Inception-RestNet network to achieve the denoising process is input to the traditional ADMM decoder, and then according to the traditional this algorithm calculates the codeword with the original with the noise codeword to be processed and then go to reverse optimization of the denoising network, iterative operation between the Inception-RestNet and the hard verdict decoder can be reduce the effect of noise on the coded modulation system, thus enabling the decoder to obtain more accurate estimates. Experimental results show that the BER performance of this IR-ADMM decoder is improved by 0.5 dB with fewer iterations than the conventional LDPC decoder.

## A CNN-Aided Post-Processing Scheme for Channel Decoding Under Correlated Noise

- **Status**: ✅
- **Reason**: CNN 보조 디코딩 후처리(상관 잡음), 코드 구조 무관 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10762738
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: Junhao Liu, Shaoli Kang, Jing Cheng +2
- **PDF**: https://ieeexplore.ieee.org/document/10762738
- **Abstract**: In this paper, a convolutional neural network-aided post-processing scheme (CNNAPS) is proposed for improving the channel decoding performance of the denoiser under correlated noise. In this scheme, the CNN estimates actual channel noise for computing the error pattern, and then error nodes are identified by a threshold discrimination method. Specifically, the channel log-likelihood ratio (LLR) value of the identified error node is set to zero, while the received signal of the identified correct node is denoised. Furthermore, one of the key dvantages of CNNAPS is that it does not require knowledge of code structure properties, making it applicable to all linear block codes. Simulation results demonstrate that CNNAPS effectively identifies error nodes within error blocks. It is also shown that by implementing the post-processing along with a single redecoding, CNNAPS can significantly improve the error correction performance of the denoiser with minimal increase in complexity.

## Introducing Ambiguity Clustering: An Accurate and Efficient Decoder for qLDPC Codes

- **Status**: ✅
- **Reason**: qLDPC용 Ambiguity Clustering 디코더, BP-OSD 대비 — BP-OSD 유래 군집화 아이디어 이식 가능성 애매, Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10821172
- **Type**: conference
- **Published**: 15-20 Sept
- **Authors**: Stasiu Wolanski, Ben Barber
- **PDF**: https://ieeexplore.ieee.org/document/10821172
- **Abstract**: We introduce Ambiguity Clustering, a new decoder for general quantum low-density parity check codes. On the recently proposed bivariate bicycle codes we find an order of magnitude speedup compared to the state-of-the-art BP-OSD decoder with no reduction in logical fidelity at physically realistic error rates. In particular, a single-threaded CPU implementation of Ambiguity Clustering is fast enough to decode the 144-qubit Gross code in real time for neutral atom and trapped ion systems.
