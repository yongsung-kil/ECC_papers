# IEEE Xplore — 2024-04 (1차선별 통과)


## Efficient Construction of Quasi-Cyclic LDPC Codes With Multiple Lifting Sizes

- **Status**: ✅
- **Reason**: 다중 lifting size 지원 QC-LDPC 신규 구성법(non-decreasing girth) — 바이너리 코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10418118
- **Type**: journal
- **Published**: April 2024
- **Authors**: Huaan Li, Hengzhou Xu, Chao Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/10418118
- **Abstract**: In this letter, we present an efficient method for constructing a family of quasi-cyclic low-density parity-check (QC-LDPC) codes specified only by one single exponent matrix that can support multiple lifting sizes. Our method adopts the small-lifting-size-first design strategy and the resulting exponent matrix of larger lifting size has non-decreasing girth. Numerical results show that all constituent codes can perform as well as (outperform) the CCSDS (5G) LDPC codes over the AWGN channel with the iterative decoding algorithms. This fact demonstrates the feasibility and validity of our proposed method and makes it competitive in some applications, e.g., enhancing short and medium-length LDPC codes to support longer length.

## Adaptive Granularity Progressive LDPC Decoding for NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시 직접(A): GC-LDPC 기반 적응적 progressive 디코딩, read-retry granularity 최적화 — NAND ECC 핵심
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10318173
- **Type**: journal
- **Published**: April 2024
- **Authors**: Binhao Bao, Qianhui Li, Wu Guan +3
- **PDF**: https://ieeexplore.ieee.org/document/10318173
- **Abstract**: Progressive low-density parity check (LDPC) code decoding has been widely used to correct increasing raw bit errors in NAND Flash memory. Once the decoding of a single logical page fails, the read-retry operation will reprocess at an increased read level with more accurate initial log-likelihood ratio (LLR) messages. However, the traditional progressive LDPC decodings with inappropriate read-level-increase granularities of read-retry operations introduce unnecessary flash read latency. By taking advantage of globally coupled LDPC (GC-LDPC) codes, an improved adaptive granularity progressive LDPC decoding (IAGPD) is proposed. This method can estimate the number of uncorrectable bit errors before each read-retry operation by detecting the unsatisfied local parity checks and general syndrome in the decoding failure. Then, it adaptively selects the optimal read-level-increase granularities for read-retry operations in the progressive LDPC decoding. Compared with the existing decoding methods, only by an extra 0.098% of the decoder area and two clock cycles, our method can reduce the flash read latency by up to 43%. And the solid-state drive (SSD) read response time on MQsim can be reduced by up to 32%.

## LDPC Decoding With Degree-Specific Neural Message Weights and RCQ Decoding

- **Status**: ✅
- **Reason**: 이식 가능 디코더(C): degree별 가중치 공유 신경망 MinSum + RCQ 디코더, HW 부담 감소 — NAND LDPC 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10360862
- **Type**: journal
- **Published**: April 2024
- **Authors**: Linfang Wang, Caleb Terrill, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/10360862
- **Abstract**: Recently, neural networks have improved MinSum message-passing decoders for low-density parity-check (LDPC) codes by multiplying or adding weights to the messages, where the weights are determined by a neural network. The neural network complexity to determine distinct weights for each edge is high, often limiting the application to relatively short LDPC codes. Furthermore, storing separate weights for every edge and every iteration can be a burden for hardware implementations. To reduce neural network complexity and storage requirements, this paper proposes a family of weight-sharing schemes that use the same weight for edges that have the same check node degree and/or variable node degree. Our simulation results show that node-degree-based weight-sharing can deliver the same performance requiring distinct weights for each node. This paper also combines these degree-specific neural weights with a reconstruction-computation-quantization (RCQ) decoder to produce a weighted RCQ (W-RCQ) decoder. The W-RCQ decoder with node-degree-based weight sharing has a reduced hardware requirement compared with the original RCQ decoder. As an additional contribution, this paper identifies and resolves a gradient explosion issue that can arise when training neural LDPC decoders.

## Multi-Impairment Compensation for CO-OFDM System Based on Deep Learning and LDPC Code

- **Status**: ✅
- **Reason**: BP 디코더를 대체하는 DNN 기반 LDPC 디코더 제안 - 신경망 디코더는 이식 가능 디코더 알고리즘(C)에 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10449366
- **Type**: journal
- **Published**: April 2024
- **Authors**: Cong Hu, Yuanxiang Chen, Ying Han +1
- **PDF**: https://ieeexplore.ieee.org/document/10449366
- **Abstract**: In this article, we propose a multi-impairment compensation scheme based on deep learning and low-density parity-check (LDPC) code for the coherent optical orthogonal frequency division multiplexing (CO-OFDM) system. We first propose a multi-impairment compensation autoencoder (MICAE) based on deep neural network (DNN). Then we combine the proposed MICAE with LDPC code and design a DNN-based decoder for LDPC decoding to replace the traditional belief propagation (BP) decoder. The proposed scheme can compensate for multiple impairments simultaneously and has faster decoding speed, greatly improving the performance of the CO-OFDM transmission system. We demonstrate the superiority of the proposed scheme through simulations in different CO-OFDM transmission systems. Simulation results show that the proposed scheme can effectively improve the Q-factor and reduce the bit error rate (BER) of the system, and is more suitable for complex long-distance and high-speed optical transmission scenarios.

## PD-GLDPC Codes With Degree-1 Variable Nodes and Multi-Types of Component Codes

- **Status**: ✅
- **Reason**: BEC 채널이지만 PD-GLDPC 신규 코드 설계(degree-1 VN, MCC 최적화) — 바이너리 코드 설계(E), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10415095
- **Type**: journal
- **Published**: April 2024
- **Authors**: Jae-Won Kim, Jaewha Kim, Hee-Youl Kwak +1
- **PDF**: https://ieeexplore.ieee.org/document/10415095
- **Abstract**: In this letter, we propose a new design method for protograph-based partially doped generalized low-density parity-check (PD-GLDPC) codes over the binary erasure channel (BEC). By extending the block-error threshold condition proposed by A. K. Pradhan et al. for conventional GLDPC codes, we optimize medium to high-rate PD-GLDPC codes with degree-1 variable nodes and multi-types of component codes (MCC). It is shown that the optimized PD-GLDPC codes outperform the conventional LDPC and GLDPC codes at the frame error rate 10−4 over the BEC while having comparable decoding complexity.

## A UnetNND-BP Architecture for Channel Decoding Under Correlated Noise

- **Status**: ✅
- **Reason**: Unet 기반 신경망 디노이저-BP 디코더 신규 아키텍처 — 신경망 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10422741
- **Type**: journal
- **Published**: April 2024
- **Authors**: Huiying Chen, Pengchao Zhao, Chengju Li
- **PDF**: https://ieeexplore.ieee.org/document/10422741
- **Abstract**: In this letter, we introduce a Unet-based neural network denoiser-belief propagation (UnetNND-BP) architecture with two training modes to improve the decoding performance of low-density parity-check (LDPC) codes. In the supervised learning mode, UnetNND-BP achieves better performance than benchmark schemes, while in the self-supervised learning mode, it achieves comparable performance.

## Synodic Period Channel Modeling and Coding Scheme for Deep Space Optical Communications

- **Status**: ✅
- **Reason**: staircase LDPC용 SC-OSD 및 SOSD-SWD 디코더 신규 제안(error floor 개선) — OSD/SWD 디코더 기법(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10399911
- **Type**: journal
- **Published**: April 2024
- **Authors**: Yaosheng Zhang, Jian Jiao, Ke Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10399911
- **Abstract**: In this article, we design an end-to-end free-space optical (FSO) communication coding scheme for deep space exploration. Take the Mars exploration as an example, we first establish the synodic period FSO channel model by taking into account the solar scintillation, and derive the corresponding upper bound of bit error rate (BER) for $L$-ary pulse position modulation (LPPM). Then, we propose a staircase code-ordered statistics decoder (SC-OSD) algorithm for staircase low density parity check (LDPC) codes under synodic period FSO channel, and derive the probability density function (PDF) and Gaussian approximation of the ordered statistics of the SC-OSD algorithm, which provide a guideline to derive a lower bound of block error rate (BLER) and reduce the decoding complexity of SC-OSD. Furthermore, we propose a soft OSD-sliding window decoding (SOSD-SWD) algorithm for staircase LDPC codes under scintillation states to address the error floor problem in conventional SWD decoder. Simulation results validate that the proposed SOSD-SWD algorithm can achieve much lower BER than the related algorithms in all scintillation conditions, and shed light to tradeoff the achievable BER and complexities under different scintillation conditions.

## An efficient Multi-code LDPC Encoder for Deep Space Communication

- **Status**: ✅
- **Reason**: CCSDS LDPC 멀티코드 인코더 HW(RCE 회로) — 인코더 HW 아키텍처 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10602896
- **Type**: conference
- **Published**: 19-22 Apri
- **Authors**: Ruijiang Yin, Guohua Zhang, Ke Jia +1
- **PDF**: https://ieeexplore.ieee.org/document/10602896
- **Abstract**: Channel coding is a key technology for improving the reliability of satellite communication data transmission links. The consultative committee for space data systems (CCSDS) recommends a set of low-density parity-check (LDPC) codes suitable for deep space communication. To meet the different needs of satellite communication, a high-throughput encoder based on recursive convolutional encoder (RCE) circuit is designed, which can achieve all LDPC code encodings recommended in the CCSDS standard for deep space communication. It can reduce hardware usage and improve inter-satellite availability for transplanting.

## An Efficient Partially Parallel Encoder Suitable for 5G-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC 부분병렬 인코더 HW, forward-substitution·GA 최적화 — HW 아키텍처 이식 가능(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10603167
- **Type**: conference
- **Published**: 19-22 Apri
- **Authors**: Ke Jia, GuoHua Zhang, RuiJiang Yin +1
- **PDF**: https://ieeexplore.ieee.org/document/10603167
- **Abstract**: In order to serve as a physical channel encoding solution for the 5G new radio (NR) data channel, and to meet the demand for quasi-cyclic low-density parity-check (QC-LDPC) codes, this paper proposes an efficient parallel encoder with a compatible structure. The design of this encoder is based on a forward substitution efficient encoding algorithm, which is integrated into a configurable circuit structure, allowing it to adapt flexibly to different base graphs of 5G-LDPC codes. Furthermore, the performance of this encoder can be enhanced through the utilization of a genetic algorithm (GA) optimization approach, aimed at achieving higher throughput or improved error correction (EC) capability. The optimized encoder not only provides high throughput, but also achieves optimal HUE (hardware usage efficiency).

## Decoding of 5G NR Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: layered NMS·업데이트 순서 스케줄링 비교 — 디코더 스케줄링 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10602849
- **Type**: conference
- **Published**: 19-22 Apri
- **Authors**: Siqi Yu, Francis C. M. Lau, Kunyang Li
- **PDF**: https://ieeexplore.ieee.org/document/10602849
- **Abstract**: Low-density parity-check (LDPC) codes have been selected as the channel coding scheme for 5G NR standard, which have excellent performance approaching the Shannon limit and are easy to implement in hardware. The decoding algorithm and scheduling scheme of LDPC codes have a significant impact on performance. The row degree (RD) and the number of punctured bits (PBs) are widely used to determine the update order of layers. In this letter, we used Matlab to simulate the error performance of the 5G LDPC codes. We completed the bit error rate and frame error rate simulations of six different decoding algorithms, including flooding LLR-BP, flooding NMS, layered LLR-BP, layered NMS, the lowest degree and least-punctured (LD-LP) layered LLR-BP and LD-LP layered NMS methods, for the 5G LDPC code with a base graph of size [46, 68], code rate 1/3, and code length of 1584.We further compared the performance of LD-LP layered decoding and LP-LD layered decoding. Moreover, we simulated the error performance of the core part of the LDPC code, which consists of four layers. We evaluated the effect of the update order of the four layers on the error performance of the code, and concluded that some update orders might give slightly better error performance than others.

## Optimization of LDPC coded PDMA systems with adaptive overload

- **Status**: ✅
- **Reason**: PDMA 서브매트릭스별 LDPC 부호를 check-concentrated 차수분포로 최적화 — 이식 가능한 코드 설계 기법(E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10743421
- **Type**: conference
- **Published**: 19-21 Apri
- **Authors**: Hanqing Ding, Yanyan Jin, Jian Zeng +3
- **PDF**: https://ieeexplore.ieee.org/document/10743421
- **Abstract**: For low-density parity-check (LDPC) coded pattern division multiple access (PDMA) systems with adaptive overload, the receiver performance is degraded due to the mismatched extrinsic information transfer (EXIT) characteristic between the front-end PDMA-detector and back-end LDPC-decoder when iterative detection and decoding (IDD) is employed. For the overload adaptive system, the PDMA-detector shows differentiated EXIT characteristic for different pattern matrices (PMs), thus a single optimized code is no longer a good choice. In this work, we propose to optimize the corresponding LDPC codes for each submatrix of the nested pattern matrix via a simplified method which uses check-concentrated degree distribution pair. Both EXIT chart-based analysis and bit-error-rate simulation results show a prominent performance gain brought by the proposed method.

## An FPGA-Based QC-LDPC Decoder Design

- **Status**: ✅
- **Reason**: 스토리지 ECC용 QC-LDPC를 PEG로 구성하고 layered min-sum FPGA 디코더 구현 — NAND/스토리지 직접+HW(A/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10743319
- **Type**: conference
- **Published**: 19-21 Apri
- **Authors**: Nan Li, Yunling Yang
- **PDF**: https://ieeexplore.ieee.org/document/10743319
- **Abstract**: LDPC codes have been widely used to deal with noise interference and improve the reliability of the system due to their excellent error correction performance. At the same time, with the increase of storage density in digital storage devices, LDPC codes are also applied to the error check and correction (ECC) module in the storage device controller to solve the random flipping of stored data bits. In this paper, the PEG algorithm is used to construct a QC-LDPC code with high code rate in the ECC module, and the design simulation of the decoder based on the FPGA platform is carried out with reference to the layered minimum sum algorithm. Finally, the decoding results are analyzed under the condition that several bits of data are randomly flipped in the storage device. The decoder in this study can achieve a throughput of 8.49Mbps at a 50MHz clock.

## Adaptive Reweighted Sparse Belief Propagation Decoding for Polar Codes

- **Status**: ✅
- **Reason**: polar 부호용 적응 재가중 sparse BP 디코더 — LDPC SPA에서 영감받은 reweighted LLR 메시지패싱 기법으로 LDPC min-sum/BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10446017
- **Type**: conference
- **Published**: 14-19 Apri
- **Authors**: Robert M. Oliveira, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/10446017
- **Abstract**: In this paper, we present an adaptive reweighted sparse belief propagation (AR-SBP) decoder for polar codes. The AR-SBP technique is inspired by decoders that employ the sum-product algorithm for low-density parity-check codes. In particular, the AR-SBP decoding strategy introduces reweighting of the exchanged log-likelihood-ratio in order to refine the message passing, improving the performance of the decoder and reducing the number of required iterations. An analysis of the convergence of AR-SBP is carried out along with a study of the complexity of the analyzed decoders. Numerical examples show that the AR-SBP decoder outperforms existing decoding algorithms for a reduced number of iterations, enabling low-latency applications.

## An FPGA-based QC-LDPC encoder design

- **Status**: ✅
- **Reason**: 스토리지 ECC용 QC-LDPC를 PEG로 구성하고 FPGA 인코더 설계 — D(HW)/A(스토리지) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10603979
- **Type**: conference
- **Published**: 12-14 Apri
- **Authors**: Yunling Yang, Nan Li
- **PDF**: https://ieeexplore.ieee.org/document/10603979
- **Abstract**: Low-density parity-check (LDPC) codes have been widely used to deal with noise interference and improve the reliability of the system due to their excellent error correction performance. At the same time, with the increase of storage density in digital storage devices, LDPC codes are also applied to the error checking and correcting (ECC) module to solve the situation of random flipping of stored data bits. In this paper, the progressive edge growing (PEG) algorithm is used to construct a high-rate Quasi Cyclic-LDPC (QC-LDPC) code suitable for the ECC module of the storage device, and the generator matrix is analyzed, and finally a high-efficiency encoder is designed based on the FPGA to quickly generate the parity-check bits in the storage device. The encoder in this study can achieve a throughput of 106.4Mbps at a 50MHz clock.

## Iteration-Aware Dynamic Quantization Neural Belief Propagation Decoder

- **Status**: ✅
- **Reason**: iteration별 최적 비트폭 예측하는 동적 양자화 neural BP 디코더 — NAND LLR 양자화/디코더에 직접 이식 가능한 새 기여(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10541458
- **Type**: conference
- **Published**: 12-14 Apri
- **Authors**: Liangsi Ma, Bei Liu, Xin Su
- **PDF**: https://ieeexplore.ieee.org/document/10541458
- **Abstract**: For some linear codes, neural networks have been found to be a way to enhance traditional belief propagation (BP) decoder. When deploying such methods in practice, quantization issues also need to be considered. Considering that the messages of variable/check nodes are variable during the BP decoding process, this paper proposes a dynamic quantization method to predict the optimal bit-width for the node’s message quantization in different decoding iterations. We build a shallow neural network as a bit-width predictor and train it jointly with a neural belief propagation decoding network. During actual decoding, the bit prediction network will generate appropriate bit-width for quantizing the messages of each layer of nodes. Finally, simulation experiments validate the effectiveness of the proposed quantization method.

## Performance Improvement of Flash Memory By Error Pre-checking Scheme and Error Correction

- **Status**: ✅
- **Reason**: 플래시 메모리 신뢰성·오류 사전체크(DEPS)+오류정정 — A(NAND/SSD 직접), 애매하나 in으로 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10576188
- **Type**: conference
- **Published**: 11-13 Apri
- **Authors**: Helen Mary, Anjana Devi S
- **PDF**: https://ieeexplore.ieee.org/document/10576188
- **Abstract**: Flash memory serves as a pivotal nonvolatile data storage technology, ensuring data persistence even in the absence of power, and is ubiquitous in devices such as USB drives, SSDs, and memory cards. The reliability of this technology is paramount for safeguarding valuable data. Establishing robust error check systems, adhering to stringent data integrity policies, and meticulously preventing data corruption during write operations are imperative practices to maintain data integrity. Employing pre-error checking procedures can bolster control over error data, thus diminishing erroneous decisions. Introducing a Dynamic Error Pre-Check Strategy (DEPS) offers a proactive approach to detecting and mitigating data imperfections in Flash memory, thereby enhancing its reliability and performance. Furthermore, enhancing SSD readability can be accomplished by partitioning large files into smaller pages, a strategy that not only enhances SSD readability but also augments average reading speed, optimizes space utilization, and curtails energy consumption in flash memory systems. This optimized approach results in notable reductions in area, on-chip power, junction temperature, and process delay by 60.19%, 65.86%, 51.7%, and 66.5% respectively. These reductions signify improved resource efficiency, decreased power consumption, improved thermal management, and, ultimately, increased reliability and performance of Flash memory systems.
