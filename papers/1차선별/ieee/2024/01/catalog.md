# IEEE Xplore — 2024-01 (1차선별 통과)


## Construction of Protograph-Based LDPC Codes With Chordless Short Cycles

- **Status**: ✅
- **Reason**: 프로토그래프 바이너리 LDPC의 chordless short cycle 제거 구성 — trapping set/d_min 개선 새 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10226284
- **Type**: journal
- **Published**: Jan. 2024
- **Authors**: Farzane Amirzade, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/10226284
- **Abstract**: There is a concept in graph theory known as a chord which has not been considered before in relation to trapping sets of Tanner graphs. A chord of a cycle is an edge outside the cycle which connects two vertices of that cycle. It is proved that short cycles with a chord are the root of several trapping sets and eliminating them increases the minimum distance  $d_{\min }$  of a code. We provide new analytic lower bounds on  $d_{\min }$  of LDPC codes with girths 6 and 8 and column weight  $\gamma $  in which the short cycles are all chordless. We prove, analytically, that  $d_{\min }\geq 2\gamma $  for girth 6 and  $d_{\min }\geq \frac {3(\gamma -1)^{2}}{\gamma \ln \gamma -\gamma +1}$  for girth 8. Comparing these bounds with the existing bound  $\gamma +1$  for girth-6 LDPC codes shows the positive and significant influence of eliminating these cycles. A method to construct protograph-based LDPC codes with different girths and free of short cycles with a chord is given which is applicable to any type of protographs, simple and multi-edge, regular and irregular. The conditions to remove small trapping sets from the Tanner graph of a multi-edge QC-LDPC code are given. Numerical results indicate that the application of our method to QC-LDPC codes improves existing results.

## Utilizing Multi-Body Interactions in a CMOS-Based Ising Machine for LDPC Decoding

- **Status**: ✅
- **Reason**: CMOS Ising machine 기반 LDPC 디코더 + multi-body interaction으로 order-reduction 없이 고차항 구현; 새 디코더 HW 아키텍처(D) 이식 가능성
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10285565
- **Type**: journal
- **Published**: Jan. 2024
- **Authors**: Eslam Elmitwalli, Zeljko Ignjatovic, Selcuk Kose
- **PDF**: https://ieeexplore.ieee.org/document/10285565
- **Abstract**: Ising machines have shown great promise in solving combinatorial optimization problems (COPs) using nature-inspired computation with higher speed and efficiency over traditional von Neumann computing systems. CMOS-based implementations combine the maturity and scaling ability of CMOS with the efficacy of Ising machines. In this paper, a low-density parity-check (LDPC) decoding solution is implemented with a CMOS-based resistively-coupled Ising machine known as (QuBRIM), using multi-body interactions among CMOS-based Ising machine nodes for the first time. State-of-the-art CMOS-based Ising implementations currently utilize order reduction to solve problems with higher-than-quadratic terms. In this paper, a new mechanism is proposed to implement higher-than-quadratic terms on Ising machines without the need for order reduction. The proposed methodology is implemented and verified with CMOS technology using 45 nm Generic PDK (GPDK). High accuracy rates are reported for the LDPC decoder based on the proposed methodology, comparable to Normalized Min-Sum, Offset Min-Sum, and Layered Belief-Propagation decoders, with a bit error rate (BER) as low as  $4 \times 10^{-8}$  at a signal-to-noise ratio (SNR) of 4dB. Furthermore, the proposed LDPC decoder attains a normalized energy efficiency (NEE) of 1.29 pJ/bit/iteration, surpassing the state-of-the-art decoders by a minimum factor of 2.4 and as much as 7.6 times.

## Optimization of Finite-Length Protograph-Based SC-LDPC Anytime Codes

- **Status**: ✅
- **Reason**: Protograph SC-LDPC anytime 유한길이 최적화 기법(delay-exponent metric, multi-objective opt)이 바이너리 SC-LDPC 코드설계(E)로 이식 가능, 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10319293
- **Type**: journal
- **Published**: Jan. 2024
- **Authors**: Xiaoxi Yu, Li Deng, Yong Liang Guan +1
- **PDF**: https://ieeexplore.ieee.org/document/10319293
- **Abstract**: In this letter, we present an optimization method for designing Protograph-based spatially coupled low-density parity-check anytime (P-anytime) codes with outstanding finite-length performance. We first introduce two performance metrics, namely the delay-exponent and anytime mean parameters, to effectively capture the finite-length behavior of P-anytime codes. We then propose a multi-objective optimization algorithm to optimize these performance metrics and design novel P-anytime codes. Simulation results demonstrate that our proposed P-anytime codes achieve one to two orders of magnitude improvement in both bit erasure rate and bit error rate compared with prior-art anytime codes.

## Adaptive Differential Wearing for Read Performance Optimization on High-Density nand Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND 플래시 read 성능·수명 최적화(adaptive differential wearing) — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10190114
- **Type**: journal
- **Published**: Jan. 2024
- **Authors**: Yunpeng Song, Yina Lv, Liang Shi
- **PDF**: https://ieeexplore.ieee.org/document/10190114
- **Abstract**: With cost reduction and density optimization, high-density NAND flash memory has been widely deployed in data centers and consumer devices. However, this trend has significantly degraded the read performance and lifetime of high-density NAND flash memory during the last decade. Previous works proposed to optimize flash lifetime with wear leveling (WL) and optimize read performance with reliability improvement. Although WL can improve flash lifetime, it leads to the reliability of all blocks in 3-D NAND flash decreasing simultaneously. The reliability and read performance will be degraded with flash wearing. To solve this problem, an adaptive differential wearing (ADWR) scheme is proposed to optimize the read performance and lifetime in this work. The basic idea of ADWR is to determine the size of the high-reliability area to serve hot reads based on workload characteristics. Specifically, first, a differential wearing scheme is proposed to construct different reliability areas based on the characteristics of the data. Second, a lifetime model is constructed for the ADWR to clarify the lifetime impact. Based on this, a lifetime optimization scheme is proposed to improve the flash lifetime. Finally, a differential refresh scheme is proposed to reduce the impact of read disturbance on read performance. The experiments on real-life workloads show that ADWR achieves encouraging read performance optimization with negligible impacts on the lifetime of 3-D TLC NAND flash memory.

## Margin Propagation based Analog Soft-Gates for Probabilistic Computing

- **Status**: ✅
- **Reason**: 아날로그 Soft-Gate를 에러정정 디코딩에 적용한 HW 기법 — 확률계산 디코더 HW 이식 가능성(D), 애매하여 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10483323
- **Type**: conference
- **Published**: 6-10 Jan. 
- **Authors**: Ankita Nandi, Pratik Kumar, Shantanu Chakrabartty +1
- **PDF**: https://ieeexplore.ieee.org/document/10483323
- **Abstract**: Soft computing gates offer a promising approach for efficient and parallel processing of probabilistic signals. These gates are widely used in Bayesian networks and various machine learning models. However, unlike digital logic gates, the design and scaling of analog Soft-Gates is challenging due to analog artifacts, i.e., sensitivity to biasing, mismatch, and temperature variations. In this paper, we present a systematic framework for designing analog Soft-Gates that leverage the bias and temperature scalability of the Margin Propagation principle. Specifically, the paper proposes an adaptive design strategy to alleviate mismatch artifacts and to trade-off probabilistic computational accuracy, area efficiency, and power consumption. We demonstrate the design synthesis of a Soft-Gate and apply it to error correction decoding and filtering tasks. The reported Mean Square Error of the Soft-Gate is less than $10 ^{-2}$, indicating its accuracy in probabilistic computations. For edge filtering applications, the proposed Soft-Gates can achieve an average Structural Similarity Index of 0.95. The estimated energy consumption in 180nm CMOS technology is in the order of pico-Joules, validating the gate’s energy efficiency.

## GC-Like LDPC Code Construction and its NN-Aided Decoder Implementation

- **Status**: ✅
- **Reason**: NN-aided vwMS 디코더 + GC-like LDPC 구성, NAND flash용 (9126,8197) 디코더 구현 — A/C/D/E 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10423290
- **Type**: journal
- **Published**: 2024
- **Authors**: Yu-Lun Hsu, Li-Wei Liu, Yen-Chin Liao +1
- **PDF**: https://ieeexplore.ieee.org/document/10423290
- **Abstract**: The trade-off between decoding performance and hardware costs has been a long-standing challenge in Low-Density Parity Check (LDPC) decoding. Based on model-driven methodology, the Neural Network-Aided Variable Weight Min-Sum (NN-aided vwMS) algorithm is proposed to address this dilemma in this paper. Not only eliminating the second minimum value in the check node update process for reducing hardware complexity, our approach featuring a fast-convergent shuffled scheduling method proposed to enhance convergence speed can also maintain similar decoding performance as compared to the traditional normalized min-sum algorithm. Different from existing model-driven methodologies only suitable for short codes, a Globally-Coupled Like (GC-like) LDPC code construction is presented to enable efficient training with simplified neural networks for longer LDPC codes. To demonstrate the capability of the NN-aided vwMS algorithm with the fast-convergent shuffled scheduling method, a GC-like (9126,8197) LDPC decoder is implemented for NAND flash applications, achieving a 6.56 Gbps throughput with a core area of  $0.58~mm^{2}$  under the 40-nm CMOS TSMC process, and average power consumption of 288 mW under the frame error rate of  $2.64 \times 10^{-5}$  at 4.5dB. Our decoder architecture achieves a superior normalized throughput-to-area ratio of  $11.31~Gbps/mm^{2}$ , demonstrating a 2.4x improvement among previous works.

## Highly Reliable and Secure System With Multi-Layer Parallel LDPC and Kyber for 5G Communications

- **Status**: ✅
- **Reason**: MLP-LDPC: parity check matrix를 처리 그룹으로 분할해 병렬 디코딩·메시지 충돌 최소화 — 이식 가능 병렬 디코더 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10734120
- **Type**: journal
- **Published**: 2024
- **Authors**: Linh Nguyen, Quoc Bao Phan, Tuy Tan Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/10734120
- **Abstract**: The development of fifth-generation (5G) technology marks a significant milestone for digital communication systems, providing substantial improvements in data transmission speeds and enabling enhanced connectivity across a wider range of devices. However, this rapid increase in data volume also introduces new challenges related to transmission latency, reliability, and security. This paper introduces KyMLP-LDPC, a novel approach that integrates a multi-layer parallel LDPC (MLP-LDPC) algorithm with Kyber, a post-quantum cryptography scheme, to accelerate and enable reliable and secure transmission. MLP-LDPC partitions the LDPC parity check matrix into processing groups to streamline parallel decoding and minimize message collisions during transmission, thereby accelerating error correction operations. Kyber encrypts data preemptively to safeguard against potential attacks. The effectiveness of our proposed method is evaluated using both image data and signals transmitted through an additive white Gaussian noise communication channel. Evaluation results demonstrate that the proposed method achieves superior performance in terms of error correction capabilities and data security compared to existing approaches.

## Tanner (3, 23)-Regular QC-LDPC Codes: Cycle Structure and Girth Distribution

- **Status**: ✅
- **Reason**: Tanner (3,23)-regular QC-LDPC의 사이클 구조/girth 분포 분석 — 바이너리 QC-LDPC 코드 설계(E, girth/사이클 제거)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10409168
- **Type**: journal
- **Published**: 2024
- **Authors**: Qi Wang, Jingping Che, Huaan Li +3
- **PDF**: https://ieeexplore.ieee.org/document/10409168
- **Abstract**: This paper studies a class of quasi-cyclic LDPC (QC-LDPC) codes, i.e., Tanner (3, 23)-regular QC-LDPC codes of code length  $23p$  with  $p$  being a prime and  $p \equiv 1 (\mathrm {mod} 69)$ . We first analyze the cycle structure of Tanner (3, 23)-regular QC-LDPC codes, and divide their cycles of lengths 4, 6, 8, and 10 into five equivalent types. We propose the sufficient and necessary condition for the existence of these five types of cycles, i.e., the polynomial equations in a 69th unit root of the prime field  $\mathbb {F}_{p}$ . We check the existence of solutions for such polynomial equations by using the Euclidean division algorithm and obtain the candidate girth values of Tanner (3, 23)-regular QC-LDPC codes. We summarize the results and determine the girth distribution of Tanner (3, 23)-regular QC-LDPC codes.

## Scalable High-Throughput and Low-Latency DVB-S2(x) LDPC Decoders on SIMD Devices

- **Status**: ✅
- **Reason**: DVB-S2(x) LDPC 디코더의 SIMD 병렬화 전략 — 이식 가능 디코더 병렬화/HW 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10747211
- **Type**: journal
- **Published**: 2024
- **Authors**: Bertrand Le Gal
- **PDF**: https://ieeexplore.ieee.org/document/10747211
- **Abstract**: Low-density parity-check (LDPC) codes are error correction codes (ECC) with near Shannon correction performances limit boosting the reliability of digital communication systems using them. Their efficiency goes hand in hand with their high computational complexity resulting in a computational bottleneck in physical layer processing. Solutions based on multicore and many-core architectures have been proposed to support the development of software-defined radio and virtualized radio access networks (vRANs). Many studies focused on the efficient parallelization of LDPC decoding algorithms. In this study, we propose an efficient SIMD parallelization strategy for DVB-S2(x) LDPC codes. It achieves throughputs from 7 Gbps to 12 Gbps on an INTEL Xeon Gold target when 10 layered decoding iterations are executed. Simultaneously, the latencies are lower than  $400~\mu $ s. These performances are equivalent to FPGA-based solutions and overclass CPU and GPU related works by factors up to  $5\times $ .

## Universal High-Throughput and Low-Complexity LDPC Decoder for Laser Communications

- **Status**: ✅
- **Reason**: 레이저통신용 고처리율 저복잡도 바이너리 LDPC 디코더 HW(IFPP-IFP, FOMP, DAA)—FPGA 디코더 아키텍처로 NAND ECC에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10452351
- **Type**: journal
- **Published**: 2024
- **Authors**: Jing Kang, Junshe An, Yan Zhu
- **PDF**: https://ieeexplore.ieee.org/document/10452351
- **Abstract**: To address the challenges posed by propagation channel impairments and to meet the high data rate requirements of laser communications, this study introduces a pioneering low-density parity-check (LDPC) decoder characterized by its high throughput and low complexity. The unique design of this decoder, based on an inter-frame pipeline and intra-frame parallel (IFPP-IFP) scheme, is specifically tailored to maximize the efficiency of processing units, leading to a substantial increase in decoding throughput. The implementation of IFPP is realized through a novel full-overlap message passing (FOMP) scheme and a dynamic address access (DAA) algorithm, distinguishing it from current solutions. Additionally, the decoder employs a message packing strategy and low-complexity data alignment units to effectively achieve IFP. Compared to existing solutions, our hardware implementation on the Xilinx XCKU060 FPGA demonstrates significant progress. The decoder achieves a decoding throughput of 2.67 Gb/s at 10 iterations and 350MHz. Remarkably, when five decoders are used on a single FPGA device, the throughput soars to 13.3 Gb/s, outperforming state-of-the-art designs by 1.3 times and concurrently reducing resource consumption by half. This combination of resource efficiency and enhanced throughput highlights the innovative and superior nature of our proposed approach.

## Adaptive Sliding Window Decoding of Spatially Coupled Low-Density Parity-Check Codes: Algorithms and Energy Efficient Implementations

- **Status**: ✅
- **Reason**: SC-LDPC 적응형 슬라이딩윈도 디코딩 신규 알고리즘+에너지효율 HW(12nm), 바이너리, NAND 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10802915
- **Type**: journal
- **Published**: 2024
- **Authors**: Oliver Griebel, Bilal Hammoud, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/10802915
- **Abstract**: In channel coding, reducing power consumption and improving energy efficiency are major challenges in sliding window decoding (SWD) architectures for spatially coupled low-density parity-check (SC-LDPC) codes. In contrast to the well-elaborated literature on energy-efficient decoder implementations of classical LDPC block codes (LDPC-BCs), there is little research on the aforementioned challenges for SC-LDPC codes. Thus, in this paper, we investigate a novel approach for energy-efficient implementation of very high-throughput SWD for SC-LDPC codes. First, our approach proposes an analogy to state-ofthe- art iteration control techniques for LDPC-BC decoders, by dynamically adapting the window size for the decoding of SC-LDPC codes. For this purpose, we derive new algorithms that sequentially activate and/or deactivate the processors inside the window, without loss in error correction performance. Second, we propose an architecture for very high-throughput decoder implementations. Furthermore, to meet the high throughput requirements and improve energy efficiency, we revisit the window-size adaption criteria and slightly relax the derived algorithms in terms of error correction capability. Implementation results of the new revisited full-adaptive decoder in a 12 nm technology show that, at a negligible loss in error correction performance, the proposed adaptive SWD approach improves the energy efficiency by a factor of 1.4 to 3.4 compared to the state-of-the-art in the 4 dB to 7 dB signal-to-noise-ratio (SNR) range. This improvement is further increased up to a factor of 6.5 at higher SNRs.

## Channel Coding Toward 6G: Technical Overview and Outlook

- **Status**: ✅
- **Reason**: 6G 채널코딩 서베이지만 LDPC 디코더/HW 구현 성능 비교 포함 — 애매하여 in으로 살림(Phase 3 재검토)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10502324
- **Type**: journal
- **Published**: 2024
- **Authors**: Mohammad Rowshan, Min Qiu, Yixuan Xie +2
- **PDF**: https://ieeexplore.ieee.org/document/10502324
- **Abstract**: Channel coding plays a pivotal role in ensuring reliable communication over wireless channels. With the growing need for ultra-reliable communication in emerging wireless use cases, the significance of channel coding has amplified. Furthermore, minimizing decoding latency is crucial for critical-mission applications, while optimizing energy efficiency is paramount for mobile and the Internet of Things (IoT) communications. As the fifth generation (5G) of mobile communications is currently in operation and 5G-advanced is on the horizon, the objective of this paper is to assess prominent channel coding schemes in the context of recent advancements and the anticipated requirements for the sixth generation (6G). In this paper, after considering the potential impact of channel coding on key performance indicators (KPIs) of wireless networks, we review the evolution of mobile communication standards and the organizations involved in the standardization, from the first generation (1G) to the current 5G, highlighting the technologies integral to achieving targeted KPIs such as reliability, data rate, latency, energy efficiency, spectral efficiency, connection density, and traffic capacity. Following this, we delve into the anticipated requirements for potential use cases in 6G. The subsequent sections of the paper focus on a comprehensive review of three primary coding schemes utilized in past generations and their recent advancements: low-density parity-check (LDPC) codes, turbo codes (including convolutional codes), and polar codes (alongside Reed-Muller codes). Additionally, we examine alternative coding schemes like Fountain codes (also known as rate-less codes), sparse regression codes, among others. Our evaluation includes a comparative analysis of error correction performance and the performance of hardware implementation for these coding schemes, providing insights into their potential and suitability for the upcoming 6G era. Lastly, we will briefly explore considerations such as higher-order modulations and waveform design, examining their contributions to enhancing key performance indicators in conjunction with channel coding schemes.

## CNN-Based Approach for Enhancing 5G LDPC Code Decoding Performance

- **Status**: ✅
- **Reason**: Novel CNN+stochastic decoder for binary 5G LDPC with hardware-efficiency focus; ietransplantable neural decoder (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10574527
- **Type**: journal
- **Published**: 2024
- **Authors**: Sivarama Prasad Tera, Ravikumar Chinthaginjala, Priya Natha +3
- **PDF**: https://ieeexplore.ieee.org/document/10574527
- **Abstract**: This paper presents the novel Stochastic decoding-convolutional neural network (SD-CNN) structure, with the goal of enhancing 5G LDPC code’s decoding efficiency in the presence of correlated noise of the channel. Applying the stochastic approach acts as an alternate technique to fixed-point LDPC decoding to enhance the decoder’s hardware efficiency. In order to improve the efficacy of the decoder, we adopted deep learning method such as Convolutional neural network (CNN). CNNs can be employed for denoising purposes in communication systems, where signals may be compromised by diverse forms of noise while being transmitted, with the aim of enhancing signal quality and dependability. The SD-CNN architecture combines a trained CNN with a stochastic decoder of 5G LDPC codes, thereby utilizing the CNN’s capability to accurately estimate channel noise and, consequently, enhance the error correction capabilities of the decoder. The generated output of the trained CNN is then fed back into the stochastic decoder, creating an iterative process between the SD and CNN that ultimately leads to superior decoding performance. For 5G LDPC code word length  $N = 3808$ , with a base code rate  $R = 1/3$ , the suggested SD-CNN architecture achieves a BER of  $10^{-6}$  at 0.6 dB of SNR per bit in the strong correlation of channel noise condition, in comparison to SD, which achieves a BER of  $10^{-6}$  at 3.5 dB of SNR per bit. The results demonstrate that there is a 2.9 dB improvement.

## Recent Advances in Deep Learning for Channel Coding: A Survey

- **Status**: ✅
- **Reason**: 딥러닝 채널코딩 서베이로 LDPC 코드설계·신경망 디코더 다룸 — 이식 가능 디코더(C) 단서, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10702508
- **Type**: journal
- **Published**: 2024
- **Authors**: Toshiki Matsumine, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/10702508
- **Abstract**: This paper provides a comprehensive survey of recent advances in deep learning (DL) techniques for channel coding problems. Inspired by the recent successes of DL in a variety of research domains, its applications to physical layer technologies have been extensively studied in recent years, and they are expected to be a potential breakthrough in supporting the emerging use cases of the next generation wireless communication systems such as 6G. In this paper, we focus exclusively on channel coding problems and review existing approaches that incorporate advanced DL techniques into code design and channel decoding. After briefly introducing the background of recent DL techniques, we categorize and summarize a variety of approaches, including model-free and model-based DL, for the design and decoding of modern error-correcting codes, such as low-density parity check (LDPC) codes and polar codes, to highlight their potential advantages and challenges. Finally, the paper concludes with a discussion of open issues and future research directions in channel coding.

## Hierarchical Interleaving and Chained Recovery Schemes of LDPC Codes for Noisy Insertion and Deletion Channels

- **Status**: ✅
- **Reason**: 바이너리 LDPC 기반 ID채널 계층 인터리빙+체인복구 디코딩 — 새 코딩/디코딩 기법, 스토리지 관련(애매하면 in)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10666496
- **Type**: journal
- **Published**: 2024
- **Authors**: Ryo Shibata
- **PDF**: https://ieeexplore.ieee.org/document/10666496
- **Abstract**: Error-correcting codes for insertion and deletion (ID) errors have attracted considerable attention because of their potential in future communication and storage systems. Existing schemes based on modern coding approaches approach the information-theoretical limits of an ID channel. However, a scheme that universally performs well across various channel impairments, such as Gaussian noise and bit-flipping noise, is yet to be established. In this study, we proposed a novel coding scheme for cascaded ID-noisy channels. The scheme manages the transmission of multiple codewords using a low-density parity-check code. In the transmitter, a two-stage hierarchical interleaving with the codewords is used, whereas in the receiver, an efficient decoding strategy is used to sequentially estimate the original codewords with a decoding delay. We evaluated the performance of the proposed scheme through achievable information rates, asymptotic analysis, and numerical simulations. The results demonstrated that the proposed scheme achieved universal performance over ID-noisy channels with reduced complexity. Furthermore, to improve performance within the constraints of limited complexity and latency, we proposed an optimization method specifically for the proposed scheme.

## Deep Learning Approach for Efficient 5G LDPC Decoding in IoT

- **Status**: ✅
- **Reason**: Normalized Min-Sum + CNN으로 5G LDPC 디코딩 개선 — 이식 가능 디코더 알고리즘(C), 신경망 NMS 개선
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10703047
- **Type**: journal
- **Published**: 2024
- **Authors**: Sivarama Prasad Tera, Ravikumar V. Chinthaginjala, Priya Natha +2
- **PDF**: https://ieeexplore.ieee.org/document/10703047
- **Abstract**: The tremendous progress of 5G technology has transformed the landscape of the Internet of Things (IoT), allowing for fast data speeds, low delay, and widespread connection that is crucial for a variety of applications, including smart cities and industrial automation. In the context of 5G enabled IoT networks, colored noise introduces varying levels of interference across different frequency bands, which can significantly degrade the performance of 5G LDPC decoding. This paper presents a novel Deep learning approach for 5G channel LDPC code decoding tailored for next-generation IoT applications. The proposed method integrates an Iterative Normalized Min-Sum (NMS) algorithm with a Convolutional Neural Network (CNN) to enhance the performance of LDPC decoding in the presence of colored noise, a common interference in real-world communication channels. Through extensive simulations and analysis, our approach demonstrates a significant performance improvement, achieving a 3.8 dB enhancement at a Bit error rate of  $10^{-6}$ . This is achieved by accurately estimating and mitigating channel noise, thereby ensuring reliable data transmission for critical IoT applications. The findings indicate that our approach to decoding technique not only enhances error correction capabilities but also adapts to varying channel conditions, optimizing IoT network performance and efficiency. This research contributes a robust solution to the challenges posed by colored noise in 5G-enabled IoT networks, promoting the deployment of more reliable and efficient IoT systems.

## High-Performance QC-LDPC Layered Decoder Based on Shortcut Updating

- **Status**: ✅
- **Reason**: QC-LDPC 레이어드 디코더의 shortcut updating으로 업데이트 충돌 완화 — 새 HW 디코더 아키텍처(D)로 NAND에 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10420453
- **Type**: journal
- **Published**: 2024
- **Authors**: Zhongyong Wang, Zhaoyan Xie, Kexian Gong +2
- **PDF**: https://ieeexplore.ieee.org/document/10420453
- **Abstract**: Quasi-cyclic low density parity check (QC-LDPC) is widely used in various modern communication standards due to its excellent performance and convenient hardware implementation, but its commonly used pipelined layered decoder faces update conflicts that lead to performance degradation. This letter proposes a shortcut-based decoder to mitigate this problem. When the conflicts occur, we avoid the read/write operations of the log-likelihood ratios (LLRs) and abandon the use of the barrel shifters, and feed those LLRs directly to the next layer. we also attempt to utilize the latest messages for inevitable conflicts. Moreover, the proposed architecture significantly reduces the possibility of conflicts by reordering the base graph matrix (BGM) with a shorter update interval of LLRs, which can achieve maximum utilization in the updated messages. Compared to the state-of-the-art approach in the case of DVB-S2, the proposed architecture can deliver up to 0.25 dB performance gain with faster convergence.

## Modified CC-PEG Algorithm for Protograph-Based QC-LDPC Codes Over Non-Uniform Channel

- **Status**: ✅
- **Reason**: 프로토그래프 QC-LDPC lifting을 위한 수정 CC-PEG 알고리즘 제안; girth/cycle/ACE 기반 새 코드설계 기여(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10758647
- **Type**: journal
- **Published**: 2024
- **Authors**: Hyeon-Bhin Lee, Jae-Won Kim
- **PDF**: https://ieeexplore.ieee.org/document/10758647
- **Abstract**: In this paper, we propose the modified cycle-concentrating progressive-edge-growth (CC-PEG) algorithm for lifting protograph-based quasi-cyclic low-density parity-check (QC-LDPC) codes over the non-uniform additive white Gaussian noise (AWGN) channel. By introducing various selection criteria for shift values based on the non-uniform channel characteristics, we improve the decoding performances of lifted LDPC codes. From numerous simulation results, we demonstrate that each selection criterion is effective for the performance improvement and the modified CC-PEG algorithm outperforms the conventional lifting methods over the non-uniform AWGN channel. Furthermore, we analyze these simulation results based on some metrics such as the girth, number of cycles, and approximate cycle extrinsic message degree (ACE).

## Minimizing Low-Rank Models of High-Order Tensors: Hardness, Span, Tight Relaxation, and Applications

- **Status**: ✅
- **Reason**: 텐서 저랭크 최소화로 LDPC·일반 패리티체크 부호 ML 디코딩 SOTA 주장 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10342630
- **Type**: journal
- **Published**: 2024
- **Authors**: Nicholas D. Sidiropoulos, Paris A. Karakasis, Aritra Konar
- **PDF**: https://ieeexplore.ieee.org/document/10342630
- **Abstract**: We consider the problem of finding the smallest or largest entry of a tensor of order $N$ that is specified via its rank decomposition. Stated in a different way, we are given $N$ sets of $R$-dimensional vectors and we wish to select one vector from each set such that the sum of the Hadamard product of the selected vectors is minimized or maximized. We show that this fundamental tensor problem is NP-hard for any tensor rank higher than one, and polynomial-time solvable in the rank-one case. We also propose a continuous relaxation and prove that it is tight for any rank. For low-enough ranks, the proposed continuous reformulation is amenable to low-complexity gradient-based optimization, and we propose a suite of gradient-based optimization algorithms drawing from projected gradient descent, Frank-Wolfe, or explicit parametrization of the relaxed constraints. We also show that our core results remain valid no matter what kind of polyadic tensor model is used to represent the tensor of interest, including Tucker, HOSVD/MLSVD, tensor train, or tensor ring. Next, we consider the class of problems that can be posed as special instances of the problem of interest. We show that this class includes the partition problem (and thus all NP-complete problems via polynomial-time transformation), integer least squares, integer linear programming, integer quadratic programming, sign retrieval (a special kind of mixed integer programming / restricted version of phase retrieval), and maximum likelihood decoding of parity check codes. We demonstrate promising experimental results on a number of hard problems, including state-of-art performance in decoding low density parity check codes and general parity check codes.

## Hypernetwork Based Model-Driven Channel Neural Decoding

- **Status**: ✅
- **Reason**: 하이퍼네트워크 기반 신경망 BP 디코더(NNMS/NOMS) — 재학습 없이 파라미터 갱신, LDPC에 적용, 이식 가능한 신경망 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10530040
- **Type**: journal
- **Published**: 2024
- **Authors**: Yuanhui Liang, Chan-Tong Lam, Qingle Wu +2
- **PDF**: https://ieeexplore.ieee.org/document/10530040
- **Abstract**: Channel decoding algorithms based on model-driven deep learning, also known as channel neural decoding algorithms, have received a lot of attention in recent years. However, the internal parameters and number of layers of the current channel neural decoding algorithm cannot be changed after training. Once changed, retraining of the channel neural decoding network is required. Hypernetwork is a neural network that can generate internal parameters for the main neural network to reduce the training cost of the main neural network and improve the flexibility of the main neural network. In this study, a novel hypernetwork based channel neural decoder is proposed for neural belief propagation algorithms (NBP), including the neural normalized min-sum (NNMS) and neural offset min-sum (NOMS) algorithms. According to the type of information interaction between the hypernetwork and the main decoding network, hypernetwork-based channel neural decoders can be divided into two types: static and dynamic. The internal parameters of the static hypernetwork-based channel neural decoder can be updated as needed without retraining of the main network. In addition to this benefit, the number of layers of the dynamic hypernetwork-based channel neural decoder can also be adjusted. Experimental results show that, compared with the existing NNMS decoding algorithms, the proposed hypernetwork-based NNMS decoding algorithms can achieve better performance on both low-density parity-check (LDPC) and Bose-Chaudhuri-Hocquenghem (BCH) codes.

## WiFaKey: Generating Cryptographic Keys From Face in the Wild

- **Status**: ✅
- **Reason**: 신경망 기반 neural-MS(min-sum) 디코더를 제시 — 이식 가능 디코더 알고리즘(C). 응용은 생체인증이나 디코더 기법 떼어낼 수 있음
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10731948
- **Type**: journal
- **Published**: 2024
- **Authors**: Xingbo Dong, Hui Zhang, Yen Lung Lai +4
- **PDF**: https://ieeexplore.ieee.org/document/10731948
- **Abstract**: Deriving a unique cryptographic key from biometric measurements is a challenging task due to the existing noise gap between the biometric measurements and error correction coding. Additionally, privacy and security concerns arise as biometric measurements are inherently linked to the user. Bio-cryptosystems represent a key branch of solutions aimed at addressing these issues. However, many existing bio-cryptosystems rely on handcrafted feature extractors and error correction codes (ECC), often leading to performance degradation. To address these challenges and improve the reliability of biometric measurements, we propose a novel biometric cryptosystem (BC) named WiFaKey, for generating cryptographic keys from face in unconstrained settings. Specifically, WiFaKey first introduces an adaptive random masking-driven feature transformation pipeline, AdaMTrans. AdaMTrans effectively quantizes and binarizes real-valued features and incorporates an adaptive random masking scheme to align the bit error rate (BER) with error correction requirements, thereby mitigating the noise gap. Besides, WiFaKey incorporates a supervised learning-based neural decoding scheme called neural-MS decoder, which delivers a more robust error correction performance with less iteration than nonlearning decoders, thereby alleviating the performance degradation. We evaluated WiFaKey using widely adopted face feature extractors on six large unconstrained and two constrained datasets. On the labeled faces in the wild database (LFW) dataset, WiFaKey achieved an average genuine match rate (GMR) of 85.45% and 85.20% at a 0% false match rate (FMR) for MagFace and AdaFace features, respectively. Our comprehensive comparative analysis shows a significant performance improvement of WiFaKey. The source code of our work is available at github.com/xingbod/WiFaKey.

## New Systematic MDS Array Codes With Two Parities

- **Status**: ✅
- **Reason**: 스토리지 MDS array code(RDP 계열) 신규 구성·비트 permutation 인코딩 최적화 — 스토리지 ECC 일반(B)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10695780
- **Type**: journal
- **Published**: 2024
- **Authors**: Lan Ma, Liyang Zhou, Shaoteng Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/10695780
- **Abstract**: Row-diagonal parity (RDP) code is a classical  $(k+2,~k)$  systematic maximum distance separable (MDS) array code with  $k \leq L-1$  under sub-packetization level  $l = L-1$ , where L is a prime integer. When  $k = L-1$ , its encoding requires  $2-{}\frac {2}{k}$  XORs per original data bit, which exactly achieves theoretical optimal lower bound. In this paper, we present three new constructions of  $(k+2,~k)$  systematic MDS array codes. First, under sub-packetization level  $l = 4$ , we novelly design a  $(17,~15)$  array code  ${\mathcal {C}}_{1}$ , where k can reach the largest possible value to satisfy the MDS property. Moreover, when  $k \leq 7$ , the encoding complexity of its subcodes can exactly achieve the theoretical optimal  $2-{}\frac {2}{k}$  XORs per original data bit, and likewise, the decoding complexity of the subcodes with  $k \leq 4$  is also exactly optimal. Under sub-packetization level  $l = L-1$  with certain primes L, the second construction yields an MDS array code  ${\mathcal {C}}_{2}$  with  $k \leq {}\frac {L(L-1)}{2}$ , and the encoding complexity of  ${\mathcal {C}}_{2}$  is also exactly optimal for  $k = L-1$ ,  $2L-3$ . Furthermore, based on bit permutation, the third MDS array code  ${\mathcal {C}}_{3}$  is obtained with  $k \leq L(L-1)$  under sub-packetization level  $l = 2(L-1)$  with certain primes L. In particular, as an extension of  ${\mathcal {C}}_{2}$ ,  ${\mathcal {C}}_{3}$  exactly achieves the optimal encoding complexity for  $k = 2(2L-3)$ , which does not hold for other array codes in the literature.

## Heuristic Number Geometry Method for Finding Low-Weight Codeword in Linear Block Codes

- **Status**: ✅
- **Reason**: 선형 블록 부호의 저중량 코드워드 탐색 기법(이진 부호 포함, 패리티검사행렬 기반) — error floor/최소거리 분석에 이식 가능한 코드설계 기법(E)이라 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10510086
- **Type**: conference
- **Published**: 2024
- **Authors**: V. S. Usatyuk, S. I. Egorov
- **PDF**: https://ieeexplore.ieee.org/document/10510086
- **Abstract**: The article introduces a novel method for finding low-weight words in linear block binary and ternary codes by leveraging the Number Geometry. The methodology involves employing a set of heuristics related to vector lengths, lattice densities, dual space operations, permutations of lattice basis, and the search for short vectors within it. Notably, this proposed method secured the top position in the international low-weight codeword search competition organized by prominent institutions, including the French National Center for Scientific Research (CNRS), Inria Paris, and the National Research Institute for Mathematics and Informatics in the Netherlands (CWI). In a remarkable display of its effectiveness, the method successfully discovered a codeword of weight 212 in the parity-check matrix of a block binary code with a rate of 0.5 and a code length of 1280. Importantly, this accomplishment was realized within a timeframe of 4,147,201 seconds, utilizing an Intel 7700K 64GB system with a 1070 8GB video card. The search specifically excluded automorphisms and other symmetry properties, such as cyclicity and quasi-cyclicity. Furthermore, when applied to the low-weight word search problem (weight 228) in the mentioned competition, our proposed method exhibited a remarkable acceleration, being 3172.9 times faster than the Brouwer-Zimmerman algorithm implemented in the MAGMA Version 2.22-3 package. Additionally, it surpassed the best standalone implementation with vectorization and parallelization by 899 times. This noteworthy speedup underscores the efficiency and competitiveness of the introduced approach in effectively addressing the intricate task of identifying low-weight codewords in linear block codes.

## Lightweight Error Correction for In-Storage Acceleration of Large Language Model Inference

- **Status**: ✅
- **Reason**: NAND 플래시 기반 LLM 추론 가속기의 경량 ECC—플래시 에러가 ECC 대역폭에 미치는 영향 분석, NAND/SSD ECC 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10457117
- **Type**: conference
- **Published**: 2024
- **Authors**: J. Jeong, B. Ahn, D. Shin +1
- **PDF**: https://ieeexplore.ieee.org/document/10457117
- **Abstract**: As large language models (LLMs) expand their sizes, conventional GPU-based LLM inference systems face memory bandwidth and capacity limitations. An LLM inference accelerator using NAND flash storage has been proposed to overcome these challenges. However, this necessitates a significant expansion of flash channels to ensure adequate bandwidth for inference, subsequently escalating error correction code (ECC) costs. This paper examines the impact of flash memory errors on LLM inference accuracy and explores the possibility of lightweight ECC by leveraging LLM's inherent error resilience. We analyze the impact of 1) high-order bit indices masking for FP32 LLM parameters, 2) clipping, and 3) a dependency by parameter type of error robustness, and show that a combination of them can reduce ECC bandwidth by up to 9.38%.

## Methods of Multi-Threshold Decoders Use in Mimo Systems And Methods of Assessing Their Performance

- **Status**: ✅
- **Reason**: 저복잡도 multi-threshold decoder — LDPC는 아니나 저복잡도 디코더 알고리즘 기법, 이식 가능성 애매하여 보존(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10845577
- **Type**: conference
- **Published**: 2024
- **Authors**: G. Ovechkin, D. Satybaldina, Z. Sailaukyzy +2
- **PDF**: https://ieeexplore.ieee.org/document/10845577
- **Abstract**: This paper discusses use of multi-threshold decoders in the Multiple Input Multiple Output systems with fading radio channels. The main attention is paid to the problems of implementation of the multi-threshold decoders and performance, with a focus on preserving low complexity, which is critically important for achieving high speed of decoding. In modern communication systems, where data communication rates reach dozens and hundreds of Gbit/sec, decoding efficiency becomes a determinant in ensuring stable and reliable information transfer. The obtained results have shown that multi-threshold decoders due to its ability to almost optimally decode even very long codes with low computational complexity ensures high efficiency in channels with different types of fading, including multipath channels with intersymbol influence, when it is used jointly with the orthogonal frequency division multiplexing. Under these conditions, many noise-resistant codes are unfit for service due to their small length, which highlights the multi-threshold decoders advantages. These results confirm the possibility of multi-threshold decoders application in modern high-speed systems of digital data communication with complex nature of errors.

## RiF: Improving Read Performance of Modern SSDs Using an On-Die Early-Retry Engine

- **Status**: ✅
- **Reason**: 3D NAND read-retry 최적화(on-die early-retry) — 카테고리 A NAND 직접, retention/read-reference voltage 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10476412
- **Type**: conference
- **Published**: 2024
- **Authors**: M. Chun, J. Lee, M. Kim +2
- **PDF**: https://ieeexplore.ieee.org/document/10476412
- **Abstract**: Modern high-performance SSDs have multiple flash channels operating in parallel to achieve their high I/O bandwidth. However, when the effective bandwidth of these flash channels declines, the SSD's overall bandwidth is substantially impacted. In contemporary SSDs featuring high-density 3D NAND flash memory, frequent invocations of a read-retry procedure pose a significant challenge to fully utilizing the maximum I/O bandwidth of a flash channel. In this paper, we propose a novel read-retry optimization scheme, Retry-in-Flash (RiF), which proactively minimizes the amount of time wasted in conventional read-retry procedures. Unlike existing read-retry solutions that focus on identifying an optimal read-reference voltage for a sensed page, the RiF scheme focuses on determining early on whether a read-retry will be required for the sensed data. To know if a read-retry is needed or not at the earliest possible time, we propose a RiF-enabled flash chip with an on-die early-retry (ODEAR) engine. When the ODEAR engine determines that a sensed page requires a read-retry, a readreference voltage is immediately adjusted and the same page is re-read while ignoring the previously sensed page. By performing the key steps of a read-retry procedure inside a RiF flash chip without transferring the sensed uncorrectable page to an offchip controller, the RiF scheme prevents the read bandwidth of a flash channel from being wasted due to failed read data. To evaluate the RiF scheme, we developed a prototype RiF-enabled flash chip and constructed a RiF-aware SSD simulator using RiF flash chips. Our evaluation results show that the proposed RiF scheme improves the effective SSD bandwidth by 72.1% on average over a state-of-the-art read-retry solution at 2K P/E cycles with negligible power and area overheads.

## Graph Neural Network Pooling for BCH Channel Decoding in Software Defined Satellites

- **Status**: ✅
- **Reason**: GNN 기반 message-passing 디코딩에 top-k pooling으로 복잡도/지연 30-35% 절감 — BCH 대상이나 신경망 디코더 기법이 LDPC BP에 이식 가능(C), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10615375
- **Type**: conference
- **Published**: 2024
- **Authors**: S. Varadarajulu, V. M. Baeza, J. Querol +2
- **PDF**: https://ieeexplore.ieee.org/document/10615375
- **Abstract**: This paper delves into the transformative impact of Deep Learning (DL) techniques on decoding tasks at the physical layer onboard regenerative software-defined satellites, reshaping traditional error correction methodologies. Specifically, we focus on the integration of Graph Neural Networks (GNNs) for channel decoding, which offers a fresh perspective by adeptly handling graph-structured data and effectively modelling intricate interference and channel dependencies. The study systematically explores the potential performance tradeoffs that arise from modifying the graph structure. Furthermore, we extend our investigation by implementing the message-passing algorithm with GNN, employing a topk pooling method following pick, prune, and link optimization strategies. This strategic approach aims to mitigate computational complexity and minimize latency, by 30 to 35 % which is particularly advantageous for decoding BCH codes. This advancement promises to enhance the efficiency of communication systems sianificantly,

## Cellrejuvo: Rescuing the Aging of 3D Nand Flash Cells with Dense-Sparse Cell Reprogramming

- **Status**: ✅
- **Reason**: 3D NAND 플래시 셀 재프로그래밍으로 신뢰성/에러율 개선 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11126375
- **Type**: conference
- **Published**: 2024
- **Authors**: H. -Y. Liao, Y. -S. Chen, J. -W. Hsieh +2
- **PDF**: https://ieeexplore.ieee.org/document/11126375
- **Abstract**: 3D NAND flash memory is one of the most important storage technologies in modern computer systems because of its non-volatile nature and excellent data access performance. However, it suffers from aging and reliability issues due to its inherent property. In contrast to the previous research that tried to recover the data with additional encoding techniques, we propose a novel reprogramming technique, called CellRejuvo, to improve the reliability of NAND flash cells. To the best of our knowledge, CellRejuvo is the pioneer for data recovery technique that cleverly leverages reprogramming to alleviate cell aging, extending the lifespan of solid-state drives. We implement CellRejuvo on a real 3D NAND flash-based SSD and evaluate its capability on various realistic workloads. The extensive experimental results show that CellRejuvo successfully reduces the error rate of SSD by an average of 38.28 % under various retention times.

## On the use of AI for 6G Signal Decoding in DVB – S.2 Applications

- **Status**: ✅
- **Reason**: LLR 신경망 디코더(LLRNnet)로 log-MAP 대체 — 신경망 디코더 기법(C), LDPC로 이식 가능성 있어 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10849750
- **Type**: conference
- **Published**: 2024
- **Authors**: A. Christopoulou, C. Chaikalis, D. Kosmanos +2
- **PDF**: https://ieeexplore.ieee.org/document/10849750
- **Abstract**: The use of Artificial Intelligence (AI) techniques and algorithms increases the last few years at all layers of wireless signal processing chain, paving the path towards $6^{\text {th }}$ Generation (6 G) networks. In this work, we focus on physical layer and we examine the use of Log – Likelihood Ratio Neural Network (LLRNnet), at the well – known decoding and demodulation receiver processes. Digital Video Broadcasting (DVB) – S. 2 Satellite communications standard covers a variety of modulation and channel coding rates combinations at physical layer. Our work analyzes and compares Packet Error Rate (PER) performance of all these combinations for three decoding options: Neural Network (NN), log – MAP, max log – MAP. Additionally, we examine 3 hidden layer sizes. Our analysis shows that for 16 simulation scenarios derived from the DVB–S. 2 standard, NN and log – MAP exhibit nearly the same PER, verifying the use of NN as a potential decoding option with negligible loss, as compared to traditional options. Finally, the effect of modulation scheme, coding rate and NN size on PER is investigated.

## New Constructions of MDS Array Codes and Optimal Locally Repairable Array Codes

- **Status**: ✅
- **Reason**: 스토리지용 바이너리 MDS/LRAC 부호 신규 구성 + 신드롬 스케줄링 알고리즘 — 스토리지 ECC(B), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10388476
- **Type**: journal
- **Published**: 2024
- **Authors**: W. Fang, J. Lv, B. Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10388476
- **Abstract**: MDS array codes have been extensively studied due to their applications in storage systems. In this paper, we first propose a novel method of constructing MDS array codes by deleting one row and one column from the circulant matrices associated to some polynomials. Several new classes of MDS array codes with flexible parameters are constructed. In particular, we give a new algebraic presentation of the Blaum-Roth codes with sparser parity-check matrices. We also obtain a family of MDS array codes over finite fields with even characteristics whose parity-check matrices have the lowest density. Furthermore, based on these new MDS array codes, we give a general construction of optimal locally repairable array codes (LRACs) achieving the Singleton-type bound. Additionally, we obtain some new optimal LRACs of long lengths. Finally, we present a scheduled algorithm for syndrome computations of binary optimal LRACs with redundancy 4, which can tolerate three failures. The number of XORs per data bit required in our algorithm approaches 2 as the length approaches infinity, which is the same as the MDS codes tolerating three failures. However, the number of nodes required during the repair of a failed node in our optimal LRACs is only about half of that in MDS array codes.

## A Novel EICNet-Based Iterative Receiver for PLDPC-Coded M -ary DCSK Systems

- **Status**: ✅
- **Reason**: PLDPC 코드용 신경망 보조 반복 디코딩(EICNet-ID), extrinsic info로 디코더 입력 갱신; 프로토그래프 LDPC 신경망 디코더 기법은 NAND LDPC에 이식 가능성 있어 Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10716660
- **Type**: journal
- **Published**: 2024
- **Authors**: Y. He, L. Lv, Y. Fang +2
- **PDF**: https://ieeexplore.ieee.org/document/10716660
- **Abstract**: In this letter, we propose a novel neural network-aided receiver, called extrinsic-information chaos network-aided iterative decoding (EICNet-ID) receiver, for protograph low-density parity-check (PLDPC)-coded  $\boldsymbol {M}$ -ary differential chaos shift keying (DCSK) systems. Specifically, the EICNet structure captures the correlation features between the chaotic sequences of the received  $\boldsymbol {M}$ -ary DCSK symbol to obtain more accurate a-priori log-likelihood ratio (LLR) without requiring the channel state information (CSI). Moreover, the EICNet structure considers both the received symbol and its a-posteriori probabilities, allowing the extrinsic information provided by the PLDPC decoder to update network input and enhance error performance. Both simulation and analysis results demonstrate that the proposed EICNet-ID receiver exhibits desirable performance compared to the existing counterparts.

## Low Complexity State Metric Memory Reduction for Turbo Decoding With Stochastic Quantization

- **Status**: ✅
- **Reason**: Turbo 디코더 state metric 메모리 stochastic quantization HW 기법; LLR/메트릭 비트폭 축소·메모리 절감은 NAND LDPC 디코더 HW에 이식 가능성 있어 살림(Phase 3 재검토)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10198321
- **Type**: journal
- **Published**: 2024
- **Authors**: S. Hu, K. Han, J. Hu
- **PDF**: https://ieeexplore.ieee.org/document/10198321
- **Abstract**: The size of the state metrics cache (SMC) has a predominant impact on the overall hardware consumption of the Turbo decoder. This brief presents a low complexity SMC reduction algorithm based on the proposed stochastic quantization (SQ) technique, which reduces the size of the SMC by randomly quantizing the state metrics to different small bit-width numbers. The selection of the random source and the updating method of the extrinsic information are further explored to minimize the performance loss caused by bit-width reduction. The simulation and synthesis results show that the proposed algorithm can achieve the best bit error rate (BER) performance with the lowest hardware consumption among the compared SMC reduction algorithms.

## Random Flip Bit Aware Reading for Improving High-Density 3-D NAND Flash Performance

- **Status**: ✅
- **Reason**: 3D NAND 플래시 RRV 캘리브레이션(random bit flip 기반 read reference 보정)—NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10452810
- **Type**: journal
- **Published**: 2024
- **Authors**: H. Feng, D. Wei, S. Gu +3
- **PDF**: https://ieeexplore.ieee.org/document/10452810
- **Abstract**: With the explosive growth of data storage demands, the storage density of flash memory continues to increase. However, the reliability and read performance of high-density flash memory are constantly declining. To address this issue, this study proposes a low-cost read reference voltage (RRV) calibration strategy based on random bit flips. In this study, the relationship between the random bit flips count (RFBC) of flash memory and the read reference voltage offset level (RRVOL) is characterized, and an RFBC-RRVOL conversion model is constructed. Subsequently, the characteristics of 3D flash memory RRV offset are thoroughly studied, and based on the observation results. A RRV grouping optimization scheme and RRV calibration range WL expansion scheme are proposed to achieve generalized calibration of all WLs in flash memory blocks. Experimental results indicate that the proposed strategy introduces a minimal storage overhead of only 15.26 KB, which reduces the raw bit error rate (RBER) of flash memory at the end of life (EOL) and increases the success rate of one time read to 99.89%. Such improvements greatly enhance the reliability of data storage and reading performance. These results demonstrate that the strategy has good practicality and effectiveness in addressing the reliability and read performance issues of high-density flash memory.

## An Efficient Dynamic Threshold Voltage Detection Scheme for Improving 3-D NAND Flash Reliability

- **Status**: ✅
- **Reason**: 3D NAND 플래시 동적 임계전압 검출(EDTVD)로 RBER 저감 — 카테고리 A NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10663438
- **Type**: journal
- **Published**: 2024
- **Authors**: L. Yin, Y. Li, X. Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10663438
- **Abstract**: With high storage density and large capacity, three-dimensional (3D) NAND flash utilizing multi-level storage technology has become the mainstream storage medium. Furthermore, by storing multiple bits in each flash cell, 3D NAND flash memory can achieve much larger storage capacity. However, the threshold voltage distribution in 3D NAND flash memory tends to shift after repeated program/erase and long retention time, leading to more detection error when adopting conventional fixed read reference voltage (RRV). To address this issue, in this work we investigate error characteristics of 3D floating-gate (FG) and charge-trap (CT) NAND flash memory, including the reliability variations of different layers and pages, and threshold voltage shifting. We propose an efficient dynamic threshold voltage detection (EDTVD) scheme by exploiting the error characteristics and the features of the data writing process of NAND flash to optimize RRV. Based on the Nanocycler test platform, the test results show that our proposed scheme can significantly reduce raw bit error rates (RBER) during reading processes and the step count is relatively low. The RBER of the EDTVD scheme is almost equal to the optimal read scheme, and the number of step count is close to 3 fixed-step read scheme.
