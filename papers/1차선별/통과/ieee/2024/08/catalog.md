# IEEE Xplore — 2024-08 (1차선별 통과)


## A Neural Network-Based Compressive LDPC Decoder Design Over Correlated Noise Channel

- **Status**: ✅
- **Reason**: BP-DNN 신경망 LDPC 디코더(짧은 사이클 효과 제거); 압축 부분은 별개지만 이식 가능 신경망 디코더 기법 존재 — C (애매, Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10430452
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Ying Li, Baoye Zhang, Bin Tan +2
- **PDF**: https://ieeexplore.ieee.org/document/10430452
- **Abstract**: To combat the correlated noise and utilize the non-equiprobability of the source, we propose a novel Low-density parity-check (LDPC) decoder design based on a priori information and neural network, which includes two neural networks, namely Correlated-Denoising Convolutional Neural Network (Correlated-DnCNN) and Belief Propagation-Deep Neural Network (BP-DNN), respectively. Correlated-DnCNN is used to remove the correlation of channel noise and reduce the noise power. BP-DNN is used to eliminate the harmful effect of short cycles of the Tanner graph and explore the priori information of the source. With the priori information to assist in initializing the input nodes of the BP-DNN network, we introduce compression capability to the LDPC, thus the proposed scheme can improve efficiency significantly when there is a large amount of compressible data in the physical layer. To train the Correlated-DnCNN and BP-DNN jointly, we design a new three-objective joint denoising-decoding loss function, which can not only guarantee the decoding performance, but also constrain the noise to conform to the normal distribution as much as possible, and improve the network convergence performance. Experiments show that the proposed decoding framework can remove the noise correlation, reduce the noise power, and improve the decoding performance effectively.

## An Optimization Model for Offline Scheduling Policy of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: BP 오프라인 스케줄링 최적화로 디코딩 복잡도 20%+ 감소 — 이식 가능한 신규 디코더 스케줄링 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10551701
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Dongxu Chang, Guanghui Wang, Guiying Yan +1
- **PDF**: https://ieeexplore.ieee.org/document/10551701
- **Abstract**: In this study, an optimization model for offline scheduling policy of low-density parity-check (LDPC) codes is proposed to improve the decoding efficiency of the belief propagation (BP). The optimization model uses the number of messages passed (NMP) as a metric to evaluate complexity, and two metrics, average entropy (AE), and gap to maximum a posteriori (GAP), to evaluate BP decoding performance. Based on this model, an algorithm is proposed to optimize the scheduling sequence for reduced decoding complexity and superior performance compared to layered BP (LBP). We validated the proposed algorithm on LDPC codes constructed following 5G New Radio, which resulted in a reduction of decoding complexity of more than 20% compared to LBP.

## Degree-degree correlated low-density parity-check codes and their extensions

- **Status**: ✅
- **Reason**: degree-degree 상관 LDPC 신규 앙상블 구성·밀도진화(바이너리, BEC) — 이식 가능한 신규 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10666064
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Hsiao-Wen Yu, Cheng-En Lee, Ruhui Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10666064
- **Abstract**: Most existing work on analyzing the performance of a random ensemble of low-density parity-check (LDPC) codes assumes that the degree distributions of the two ends of a randomly selected edge are independent. In this paper, we go one step further by considering ensembles of LDPC codes with degree-degree correlations. We propose two methods to construct such an ensemble of degree-degree correlated LDPC codes and derive a system of density evolution equations for these codes over a binary erasure channel (BEC). By conducting extensive numerical experiments, we demonstrate how the degree-degree correlation affects the performance of LDPC codes. Our numerical results suggest that LDPC codes with negative degree-degree correlation could enhance the maximum tolerable erasure probability. Moreover, increasing the negative degree-degree correlation could facilitate better unequal error protection (UEP) design. In the final part of our extension efforts, we extend degree-degree correlated LDPC codes to multi-edge type LDPC codes and leverage these to construct convolutional LDPC codes.

## Protograph LDPC Code and Shaped Index Modulation Design for Multi-Mode OAM Systems

- **Status**: ✅
- **Reason**: OAM용 새 protograph LDPC 코드 구성(PEXIT 기반 설계, 펑처링) — 바이너리 코드 설계 이식 가능 E (도메인 무선이나 코드 구성 기여 존재)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10475375
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Zhaojie Yang, Yao Ge, Yufei Zhao +2
- **PDF**: https://ieeexplore.ieee.org/document/10475375
- **Abstract**: Orbital angular momentum (OAM) is a mode division multiplexing (MDM) technique enabling simpler implementation and higher capacity than conventional multiple-input multiple-output (MIMO) over line-of-sight (LoS) channels. This paper studies the joint design of protograph low-density parity-check (PLDPC) codes and shaping index modulation (IM) in OAM systems. To begin with, we analyze the distribution of extrinsic log-likelihood-ratios (LLRs) for coded bits output from channel detector, and then propose a customized Box-Cox transformation (CBCT) to make the distribution achieve symmetry and Gaussian features. We also devise a CBCT-based protograph extrinsic information transfer (CBCT-PEXIT) algorithm to predict the convergence performance of PLDPC-coded OAM systems. Furthermore, with the aid of such an algorithm, we construct two new types of improved PLDPC codes tailored for OAM systems, including unpunctured codes and rate-compatible punctured codes. In addition, we present a two-step design method, which seamlessly combines the shaping technique and index rule into a novel modulation scheme, called shaping index. Both theoretical analyses and simulation results demonstrate that the proposed PLDPC-coded OAM systems with shaping index significantly outperform state-of-the-art counterparts.

## Weighted Parity-Check Codes for Channels With State and Asymmetric Channels

- **Status**: ✅
- **Reason**: 비대칭 채널용 weighted parity-check 신규 부호류, BP 적용 가능 — NAND 비대칭 채널·신규 디코더 관점 이식 가능성(애매, Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10534819
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Chih Wei Ling, Yanxiao Liu, Cheuk Ting Li
- **PDF**: https://ieeexplore.ieee.org/document/10534819
- **Abstract**: In this paper, we introduce a new class of codes, called weighted parity-check codes, where each parity-check bit has a weight that indicates its likelihood to be one (instead of fixing each parity-check bit to be zero). It is applicable to a wide range of settings, e.g. asymmetric channels, channels with state and/or cost constraints, and the Wyner-Ziv problem, and can provably achieve the capacity. For the channel with state (Gelfand-Pinsker) setting, the proposed coding scheme has two advantages. First, it achieves the capacity of any channel with state (e.g. asymmetric channels). Second, simulation results show that the proposed code achieves a smaller error rate compared to the nested linear codes. We also discuss a sparse construction where the belief propagation algorithm can be applied to improve the coding efficiency.

## Exploiting Parity-Polytope Geometry in Approximate and Randomized Scheduled ADMM-LP Decoding

- **Status**: ✅
- **Reason**: ADMM-LP 디코딩 복잡도 저감(SAPA 투영, 랜덤 레이어 스케줄링) — 이식 가능 디코더 알고리즘 C
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10480433
- **Type**: journal
- **Published**: Aug. 2024
- **Authors**: Amirreza Asadzadeh, Anthony Ho, Frank R. Kschischang +1
- **PDF**: https://ieeexplore.ieee.org/document/10480433
- **Abstract**: We present two strategies to reduce the complexity of the alternating direction method of multipliers when applied to linear programming (ADMM-LP) decoding of low-density parity-check codes. First, to address the high complexity of computing a projection onto the parity polytope, the complexity bottleneck of ADMM-LP decoding, we propose the sparse affine projection algorithm (SAPA). SAPA projects onto the affine hull of  $\chi \leq d$  nearby local codewords where the check degree is d and where  $\chi $  can be significantly smaller than d. Unlike exact projection, SAPA does not require a water-filling process, and thus can be implemented with lower per-iteration complexity. Second, to reduce the number of effective iterations needed for ADMM-LP decoding, we propose a randomized layered scheduling framework. Rather than updating checks in round-robin fashion in each iteration, more “problematic” checks have a higher probability of being updated. The probability mass function that governs the selection of which checks to update is based upon the location of replica vectors inside (or on) the parity polytope. The resultant decoder converges significantly faster under this randomized scheduling than under round-robin scheduling. This makes it well suited for use in applications that limit the number of iterations.

## Construction of Spatially Coupled GC-LDPC Code for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시용 신규 SC-GC-LDPC 코드 구성 + layered SPA/NMS 디코딩, 플래시 채널 성능 검증 — A/E 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10681799
- **Type**: conference
- **Published**: 7-9 Aug. 2
- **Authors**: Jinhong Mo, Xiongfei Zhai, Min Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/10681799
- **Abstract**: With the continuous improvement of data memory density, as the common solution for error correction of NAND flash, the low-density-parity-check (LDPC) code faces more challenges, such as the increasing code length requirements, the worse raw bit error rates (RBER), and the frequently varied channels. In this paper, a new (37536, 33672) spatially coupled and globally coupled LDPC (SC-GC-LDPC) code is constructed to address the above challenge, which outperforms the traditional globally coupled LDPC (GC-LDPC) code with the gaps of 0.065 dB and 0.08 dB by exploiting the layered sumproduct algorithm (SPA) and the layered normalized min-sum (NMS) algorithm, respectively. Moreover, in the flash channel, the SC-GC-LDPC code also shows superior error correction performance as compared with the conventional GC-LDPC codes, which can effectively adapt to flash channels in different pages.

## A Complex Network Approach to Designing Bernoulli Parity-Check Codes

- **Status**: ✅
- **Reason**: 복소 네트워크 기반 패리티검사 부호 설계로 BP 디코딩 성능(워터폴/에러플로어, BER/FER) 개선 — 바이너리 부호설계(E) 새 기여, NAND LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10682017
- **Type**: conference
- **Published**: 7-9 Aug. 2
- **Authors**: Fanhui Meng, Yixin Wang, Qianfan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10682017
- **Abstract**: In this paper, a complex network approach is presented to design the Bernoulli parity-check (BPC) codes with enhanced belief propagation (BP) decoding performance. By investigating the degree correlation between variable and check nodes, we propose the normal graph configuration model (NGCM) to adjust the assortativity coefficient of normal graphs, and investigate the impact of disassortativity on decoding performances. Numerical results demonstrate that, optimizing the disassortativity of normal graphs can significantly enhance the BP decoding performance in both the waterfall and error floor regions. This improvement leads to lower bit-error-rate (BER), frame-error-rate (FER), and decoding complexity. Our study has significant practical and theoretical value, especially for the interdisciplinary research of complex network and coding theory.

## In-Memory Bit Flipping LDPC Decoding

- **Status**: ✅
- **Reason**: 비트플리핑 LDPC를 PiM(processing-in-memory)에 구현한 신규 디코더 HW - 스토리지/이식 가능 디코더 아키텍처(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10715253
- **Type**: conference
- **Published**: 26-30 Aug.
- **Authors**: Oscar Ferraz, Gabriel Falcao, Vitor Silva
- **PDF**: https://ieeexplore.ieee.org/document/10715253
- **Abstract**: Low-density parity-check (LDPC) codes play an important role in several communication and storage applications by providing a versatile and efficient solution for correcting errors. Modern computing systems suffer from data movement bottlenecks, which affect parallel processing systems more dramatically. Several solutions to this bottleneck have been proposed by moving compute units where the data resides, incorporating thousands of low-complexity processing units to perform bit-wise and simple integer operations. This paper presents the first known bit flipping LDPC processing-in-memory (PiM)-based decoder in the UPMEM system. The implementation is able to achieve 2.8 Gbit/$s$ of decoding throughput, which is competitive when compared to implementations in high-end GPUs. The source code can be found at https://github.com/oscarferraz/EUSIPC024

## VLSI Design for Error Correcting Codes in Communication Systems

- **Status**: ✅
- **Reason**: LDPC 포함 ECC의 VLSI 설계로 throughput·전력 최적화(D) — 일반적이나 HW 아키텍처라 애매, 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10731125
- **Type**: conference
- **Published**: 22-23 Aug.
- **Authors**: Amith S, Vrushank Jagadeesh, Raees Irfan +2
- **PDF**: https://ieeexplore.ieee.org/document/10731125
- **Abstract**: Bringing sophisticated technology into communication systems requires effective methods to correct errors and ensure reliable data transmission. This project focuses on the design and implementation of error-correcting codes for communication across an Additive White Gaussian Noise (AWGN) channel. We explore various coding techniques including Low-Density Parity-Check (LDPC), Hamming, and Turbo codes. The primary objective is to optimize hardware performance to achieve high efficiency, low power consumption, and high data throughput. Additionally, we evaluate the performance of these error-correcting codes under diverse communication scenarios. Our research aims to enhance the reliability and efficiency of communication systems by employing intelligent design strategies for error correction.

## Design and Implementation of LDPC Decoder using VHDL for Space application

- **Status**: ✅
- **Reason**: Normalized min-sum 기반 LDPC 디코더 VHDL HW 구현(D) — 표준 구현이나 HW 디코더라 Phase 3 재검토 위해 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10730918
- **Type**: conference
- **Published**: 22-23 Aug.
- **Authors**: B P Swathi, Amulya K, Divya Shree K V +2
- **PDF**: https://ieeexplore.ieee.org/document/10730918
- **Abstract**: With increase in demand for higher data rates and more complex satellite missions, the need for advanced channel coding techniques has become essential to establish robust and efficient communication links. Given the significant challenges posed by long distances and low signal power levels in deep space communication, the Consultative Committee for Space Data Systems (CCSDS) standard recommends Low Density Parity Check (LDPC) codes for robust error-correcting capabilities and efficiency. The design and Implementation details of Normalized min-sum based LDPC Decoder using VHSIC Hardware Description Language (VHDL) for Space application are provided in the paper. The future work is also identified in the paper.

## Reinforcement Learning-Based Read Performance Throttling to Enhance Lifetime of 3D NAND SSD

- **Status**: ✅
- **Reason**: 3D NAND SSD read disturbance/read-retry/ECC 직접 관련(A) — RL 기반 read throttling, NAND 도메인
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10693665
- **Type**: conference
- **Published**: 21-23 Aug.
- **Authors**: Yong-Cheng Liaw, Shuo-Han Chen, Yu-Pei Liang
- **PDF**: https://ieeexplore.ieee.org/document/10693665
- **Abstract**: With high storage density and low cost per bit, 3D NAND flash has dominated the market of modern solid-state drives (SSDs). Nevertheless, the growing number of stacked layers and the evolving multi-bits-per-cell technology of 3D NAND flash have led to the issue of fast accumulated read disturbance. Read disturbance leads to data bit errors and requires the error correction code (ECC) scheme to remove bit errors to correct data retrieval during read operations. Nevertheless, owing to the process of read retry and reference voltage adjustment of the ECC scheme, the read performance of 3D NAND flash deteriorates as the number of error bits grows. To mitigate the unwanted impact of prolonged read latency and maintain top read performance, modern SSDs actively rewrite stored data to remove error bits when the read latency becomes higher. However, actively removing data bit errors through data rewrites could wear out the SSDs prematurely and ultimately consume the whole lifetime of SSDs. To resolve such concerns, this paper proposes lowering the number of data rewrites through throttling the read performance of 3D NAND flash-based SSDs via reinforcement learning techniques to adaptively meet the performance requirements of different applications. Trace-driven experiments have shown promising results.

## Cost-Efficient Partially-Parallel LDPC Decoder Architecture for 50G-PON Standard

- **Status**: ✅
- **Reason**: 부분병렬 layered LDPC 디코더 HW 아키텍처·멀티플렉싱 최적화 — NAND 디코더에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10762337
- **Type**: conference
- **Published**: 19-22 Aug.
- **Authors**: Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/10762337
- **Abstract**: In this paper, we present a cost-efficient low-density parity-check (LDPC) decoder architecture tailored to meet the high throughput demands of 50G passive optical network (PON) systems. Building upon a previous layered decoder architecture, the complex multiplexing networks are specifically optimized for the PON LDPC codes, facilitating partially-parallel processing while minimizing congestion overheads. By incorporating advanced low-cost optimization schemes, the prototype PON LDPC decoder achieves a decoding throughput of 2.94 Gb/s, surpassing state-of-the-art approaches by 2.38-fold.

## An Improved Check Polytope Projection Penalized Algorithm for ADMM Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: ADMM 디코딩 check polytope projection 개선 알고리즘 — 새 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10770364
- **Type**: conference
- **Published**: 19-22 Aug.
- **Authors**: Ziyi Wang, Yun Jiang, Qiaoqiao Xia
- **PDF**: https://ieeexplore.ieee.org/document/10770364
- **Abstract**: The Euclidean projection onto check polytope is the most complicated and time-consuming operation in the alternating direction method of multipliers (ADMM) decoding for Low-Density Parity-Check (LDPC) codes. The check polytope projection penalized algorithm can avoid the tedious work of penalty parameter optimization and simplified the calculation process of check polytope projection. However, the over-punishment of check polytope projection penalized algorithm may lead to poor decoding performance, when combined with the over-relaxation technique. In this paper, an improved check polytope projection penalized algorithm is proposed. In order to reduce the ratio of even-vertex projection, we restrict the points far away from the even-vertex of the check polytope by introducing the penalty constraint condition. Simulation results show that the frame error rate (FER) performance of the proposed algorithm is almost the same as that of the cut search projection algorithm (CSA), and it can save the average decoding time by 22.9%–52%.

## Performance Investigation of OAM-SK Optical Communication System Based on PCNN-NMS

- **Status**: ✅
- **Reason**: CNN 확률을 NMS(Normalized Min-Sum) LDPC 디코딩에 결합하는 신경망-디코더 융합 기법 — NAND LDPC로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10699747
- **Type**: conference
- **Published**: 16-19 Aug.
- **Authors**: Zhengwei Hou, Chen Wei, Lixia Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/10699747
- **Abstract**: This paper introduces a PCNN-NMS demodulation method for an OAM-SK optical communication system operating under atmospheric turbulence, by integrating the data-driven probabilities of a Convolutional Neural Network (CNN) model with the Normalized Min-Sum (NMS) LDPC decoding algorithm. Then we simulated the average bit error rate (ABER). Initially, the transmission of Laguerre-Gaussian (LG) beams through atmospheric turbulence is simulated using the power spectrum inversion method, and a dataset is created for training the CNN network. This training achieves a direct classification accuracy of 97.3% with the CNN demodulator. Subsequently, the classification probabilities from the CNN are incorporated into the NMS algorithm, using the output of the CNN to refine the credibility of channel estimation. The final simulation results show that the PCNN-NMS significantly improves the system's BER performance, offering valuable insights for enhancing the BER performance in free-space optical communication system.

## Evaluations of Distinct Bitonic Sorters for ORBGRAND

- **Status**: ✅
- **Reason**: ORBGRAND용 bitonic sorter HW 평가 — GRAND는 LDPC 비특이적 디코더지만 정렬 HW 아키텍처는 LDPC 디코더에 이식 가능 여지, 애매하여 살림(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10791234
- **Type**: conference
- **Published**: 13-16 Aug.
- **Authors**: Szu-Hao Huang, Cheng-Hung Dixson Lin
- **PDF**: https://ieeexplore.ieee.org/document/10791234
- **Abstract**: Guessing Random Additive Noise Decoding (GRAND) is a recently proposed decoding algorithm for forward error correction codes in fifth-generation (5G) consumer communications. Order Reliability Bits GRAND (ORBGRAND) was proposed to utilize received channel values and sort all of them to get more probable error patterns. Therefore, choosing an efficient algorithm to sort the channel values significantly influences the hardware design of the ORBGRAND. In this study, different bitonic sorters are evaluated in terms of frame error rate, synthesized silicon area, and power consumption. To achieve a low-cost ORBGRAND, the half-output bitonic sorter with segmentation not only reduces the number of the compare and swap unit, but also reduces number of the pipeline register. The evaluation results show that the half-output bitonic sorter with two segmentation can achieve 38% area reduction and 39% power reduction, respectively.
