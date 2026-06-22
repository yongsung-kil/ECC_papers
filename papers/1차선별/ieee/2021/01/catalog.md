# IEEE Xplore — 2021-01 (1차선별 통과)


## Hard-input FEC evaluation using Markov models for equalization-induced correlated errors in 50G PON

- **Status**: ✅
- **Reason**: 50G PON에서 상관오류 환경 LDPC 하드입력 디코딩 평가 - 상관오류 모델링·인터리빙 기법이 NAND ECC에 이식 가능(B/E), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9284961
- **Type**: journal
- **Published**: January 20
- **Authors**: Amitkumar Mahadevan, Doutje van Veen, Noriaki Kaneda +3
- **PDF**: https://ieeexplore.ieee.org/document/9284961
- **Abstract**: Channel measurements for a 50G passive optical network (PON) show a significant amount of intersymbol interference (ISI) due to chromatic dispersion (CD) and the use of low-cost, bandwidth-limited 25 Gbaud class components. The channel characteristics at the input of the forward error correction (FEC) decoder are measured for several receiver equalization schemes, and the error correlation at the output of each equalizer is characterized using a sub-class of a Fritchman’s Markov model. This model is used to generate error sequences that match the observed correlation statistics, and these sequences are then used to evaluate the performance of a candidate low-density parity-check (LDPC) code with lifting factor 256 and hard-input decoding. It is shown that for a bandwidth-limited 50G PON system with 83 ps/nm dispersion, the optical power sensitivity penalty (OPSP) due to a reduction in error correction performance caused by correlated errors is 0.3–0.6 dB. Precoding, i.e., differential encoding of the input data and differential decoding, helps to reduce the OPSP for some equalizers, but the penalty increases for other equalizers. The use of a 256-bit segment-interleaver only marginally improves the decoding performance, whereas bit-interleaving across four codewords reduces the penalty to within 0.05 dB relative to the binary symmetric channel.

## A Multirate Fully Parallel LDPC Encoder for the IEEE 802.11n/ac/ax QC-LDPC Codes Based on Reduced Complexity XOR Trees

- **Status**: ✅
- **Reason**: QC-LDPC 인코더의 XOR 트리 기반 저복잡도 full-parallel VLSI 아키텍처 — D(이식 가능 HW). 표준코드지만 새 인코딩/HW 기여
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9257473
- **Type**: journal
- **Published**: Jan. 2021
- **Authors**: Ahmed Mahdi, Nikos Kanistras, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/9257473
- **Abstract**: This article proposes an encoding method based on a two-step encoding algorithm for the 12 quasi-cyclic (QC)-low-density parity-check (LDPC) (QC-LDPC) codes specified in the IEEE 802.11n/ac/ax standards. The proposed approach jointly considers all codes of the particular set, instead of targeting each code separately. The proposed algorithm performs multiplication by inverse matrices. The complexity of the multiplications is significantly reduced by the introduced encoding method. It allows the implementation of full-parallel architectures that execute the encoding process within a single clock cycle, or more for pipelined implementations, for any of the supported codes. A corresponding VLSI encoding architecture based on XOR-gate trees is also proposed. The proposed solution exploits the structure and features of the involved matrices to extract common subexpressions (CSs) using common sub-expression sharing techniques (CSST). Such expressions result due to common features of the original matrices and the corresponding inverses, identified in this article. Innovative subexpression extraction procedures that target the specific codes as a set are introduced here. Furthermore, illustrative single-clock hardware encoders derived by the proposed technique are integrated into 90- and 45-nm technologies at 1 GHz occupying 125 and 107 KGates, respectively, achieving throughput rates up to 1.62 Tbps.

## Construction of Irregular Protograph-Based QC-LDPC Codes With Low Error Floor

- **Status**: ✅
- **Reason**: 불규칙 protograph QC-LDPC를 dominant ETS 제거로 low error floor 설계—코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9211414
- **Type**: journal
- **Published**: Jan. 2021
- **Authors**: Bashirreza Karimi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/9211414
- **Abstract**: In this article, we design finite-length irregular protograph-based quasi-cyclic (QC) low-density parity-check (LDPC) codes with good waterfall performance and low error floor. To achieve a low error floor, we eliminate a targeted set of dominant elementary trapping sets (ETS) £ in the Tanner graph of the code. For a given rate and girth, the codes are designed to be free of the largest set of problematic ETSs for a given block length, or to have the shortest block length while a given set of ETSs is avoided. The design is based on a search algorithm that identifies whether any instance of any structure within £ exists in the Tanner graph of the constructed code or not. The search algorithm performs this task with minimal complexity, making it feasible to construct practical codes by running the search algorithm a large number of times. Simulation results are provided to demonstrate the superior performance of designed codes compared to similar state-of-the-art irregular QC-LDPC codes.

## A Hybrid Check Polytope Projection Algorithm for ADMM Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: ADMM 디코딩의 check polytope projection 가속 하이브리드 알고리즘—이식 가능한 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9194708
- **Type**: journal
- **Published**: Jan. 2021
- **Authors**: Qiaoqiao Xia, Xin Wang, Huajun Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/9194708
- **Abstract**: The Euclidean projection onto check polytope is the most complicated and time-consuming operation in the alternating direction method of multipliers (ADMM) decoding algorithm for low-density parity-check (LDPC) codes. Existing approximate even-vertex projection algorithm (EVA) can simplify the projection operation, but yields poor decoding performance. By alternately adopting EVA and other accurate projection algorithms, this letter proposes an innovative and simple hybrid projection algorithm (HPA) which can increase the percentage of unuseful projections. Simulation results show that the proposed algorithm can substantially reduce the projection time while achieving better frame error rate (FER) performance when compared with the standard ADMM decoding and the ADMM penalized decoding in the case of avoiding the tedious work of penalty parameter optimization. More importantly, compared with cut search algorithm (CSA), the proposed algorithm can significantly save the average projection time by nearly 80%, and the average decoding time by about 85%.

## Error Floor Estimation of QC-LDPC Coded Modulation With Importance Sampling

- **Status**: ✅
- **Reason**: QC-LDPC error floor을 trapping set 기반 importance sampling으로 추정—코드설계/floor 분석 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9186682
- **Type**: journal
- **Published**: Jan. 2021
- **Authors**: Mingyang Zhu, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9186682
- **Abstract**: This letter presents a low-complexity error floors estimation method for bit-interleaved coded modulation with quasi-cyclic low-density parity-check (LDPC) codes. Using surrogate bit-channels (SBCs) as hypothetic equivalent channels, the importance sampling method based on the stable trapping sets is applied to evaluate the error floors. It is shown that the error floors of bit-interleaved coded modulation systems can be effectively estimated, and the presented method is appropriate for various types of modulators and interleavers.

## DEPS: Exploiting a Dynamic Error Prechecking Scheme to Improve the Read Performance of SSD

- **Status**: ✅
- **Reason**: 3D NAND SSD 동적 오류 프리체킹으로 ECC 디코딩 우회·read 성능 개선 - NAND/SSD 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9091550
- **Type**: journal
- **Published**: Jan. 2021
- **Authors**: Weihua Liu, Fei Wu, Meng Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/9091550
- **Abstract**: 3-D NAND flash memory is gradually being widely used in solid state drives (SSDs), leading to increasing storage capacity. However, the read performance of SSD is sacrificed for decoding operations which are executed to guarantee the data reliability. No matter whether the data have bit errors, they will be sent to error correcting code (ECC) engine to decode, introducing a high read delay of SSD. Error prechecking can help to avoid the redundant decoding operations for the error-free data, but it induces extra checking overhead to the error data. Motivated by this, we carry out comprehensive experiments to analyze the distribution of bit errors in 3-D NAND flash memory. The preliminary experimental results show that there are a large number of pages read without errors in the early lifetime of 3-D NAND flash memory. Based on the observations and analyses, we propose a model to estimate the error-free ratio, and utilize it to design a dynamic error prechecking scheme (DEPS) to bypass the decoding operation for the error-free data in 3-D NAND flash memory and improve the read performance of SSD. Furthermore, by dividing a large page into small subpages, DEPS releases more error-free data, which significantly improves the read performance of SSD. Evaluation results from real-world traces demonstrate that by implementing DEPS, the average read performance of SSD is enhanced by 35%-55% with 3-D MLC NAND flash memory.

## Dynamic Dual Quantization-Domain Self-Corrected LDPC Decoder

- **Status**: ✅
- **Reason**: 이식 가능 디코더: dual quantization-domain(CN 3bit/VN 고bit) + self-correction, LLR 양자화 신규 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9369450
- **Type**: conference
- **Published**: 9-12 Jan. 
- **Authors**: Taehyun Kim, JooSung Park
- **PDF**: https://ieeexplore.ieee.org/document/9369450
- **Abstract**: In this paper, we propose a low-density parity-check (LDPC) decoder with a dynamic dual quantization-domain (DQD) that check nodes are operated in a 3-bit domain while variable nodes are operated in a higher bits domain. The mappings to transform messages from a domain to another domain gradually changes during the LDPC decoding process and is optimized by differential evolution and machine learning. In addition, for performance improvement, the variable node performs self-correction (SC) that the unreliable messages are erased. Simulation results show that the proposed dynamic DQD-SC decoder has better error correction performance compared to a previously proposed hybrid DQD decoder.

## Logistic Regression for LDPC Decoding Failure Prediction

- **Status**: ✅
- **Reason**: logistic regression 기반 early-stopping/디코딩 실패 예측, 반복수/UPC 활용 디코더 복잡도 저감(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9369532
- **Type**: conference
- **Published**: 9-12 Jan. 
- **Authors**: Taehyun Kim, JooSung Park
- **PDF**: https://ieeexplore.ieee.org/document/9369532
- **Abstract**: In this paper, we propose a regression analysis for the early stopping of low-density parity-check (LDPC) decoder to reduce computational complexity and decoding latency. The proposed scheme predicts the decoding failure of the LDPC decoder using logistic regression. The data sets for the decodability classification consist of the index of iteration and the number of unsatisfied parity checks. Simulation results show that with the proposed scheme, the average number of iterations of the LDPC decoder can be significantly reduced without performance loss. In addition, since the proposed scheme determines the decoding failure based on the instantaneous value, it has advantages in terms of memory and computational complexity compared to the early stopping schemes based on the changes in parameters.

## Boosting Belief Propagation for LDPC Codes with Deep Convolutional Neural Network Predictors

- **Status**: ✅
- **Reason**: 신경망 디코더: BP에 deep CNN predictor 통합, generic LDPC 디코더 개선, NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9369460
- **Type**: conference
- **Published**: 9-12 Jan. 
- **Authors**: Xiwen Chen, Huayu Li, Junsuo Qu +1
- **PDF**: https://ieeexplore.ieee.org/document/9369460
- **Abstract**: Conventional channel codes are designed to recover channel errors by adding controlled redundancy to transmit bits; however, the main underlying assumption is that information bits are independent and identically distributed (i.i.d.). Short term and linear temporal correlations are assumed to be exploited by the preceding source encoders. This assumption is flawed in some scenarios since many types of data (e.g, audio samples, video frames, and sensor measurements) exhibit long-term relations and intricate dependencies that are not exploitable by conventional source encoders. Furthermore, sending plain information is still commonplace in wireless networks. Therefore, it is essential to design channel encoders that accommodate these conditions. It is well-known that the underlying hidden patterns can be captured by deep learning methods. This important capability is not yet fully utilized in channel encoder design. This work is a primary step towards developing a predictive channel decoder that learns the intricate dependencies within and between data frames using an embedded learning module at the receiver to enhance the bit decoding performance, especially in high-noise regimes. The learning module is integrated with the belief propagation algorithm over bipartite graphs appropriate for low-density parity-check (LDPC) codes. The proposed method is universal since no specific correlation model is adopted and the learning-based prediction is performed at the bit level. The proposed method is fully implemented at the receiver side, making it compatible with generic LDPC encoders. Our simulations demonstrate the superior performance of the proposed method compared to standard LDPC decoders. For instance, about 1.7 dB gain at the 10−4 BER level is achieved when recovering noisy audio files 11This material is based upon work supported by the National Science Foundation under Grants No. 1755984 and 2008784.

## Optimizing Code Parameters of Finite-Length SC-LDPC Codes Using the Scaling Law

- **Status**: ✅
- **Reason**: Binary SC-LDPC finite-length scaling-law parameter optimization — new code-design technique (E), transferable to NAND LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9521873
- **Type**: journal
- **Published**: 2021
- **Authors**: Hee-Youl Kwak, Jae-Won Kim, Jong-Seon No
- **PDF**: https://ieeexplore.ieee.org/document/9521873
- **Abstract**: In this paper, we optimize code parameters of finite-length spatially coupled low-density parity-check (SC-LDPC) codes, represented by a set of code parameters  $(l,r,w,L,M)$ . Although the finite-length scaling behavior of SC-LDPC codes was studied in the existing literature, the previous works impose a constraint such that the coupling width  $w$  is equal to the variable node degree  $l$  and they do not focus on optimizing the code parameters for given code and decoder specifications such as the code rate, frame size, and decoding complexity. In order to optimize the code parameters with the target specifications, we first extend the scaling law of SC-LDPC codes without the constraint  $w=l$ . Using the scaling law formulated with a new variable  $w$ , we show that the coupling width  $w$  directly affects the slope of the performance curve and performance comparisons are given to investigate trade-offs inherent in the code parameters. It is shown that there are trade-offs for the code parameters in the perspective of the asymptotic performance limit, code rate, and scaling behaviors. In addition, the scaling law allows us to find the optimal code parameter set showing the best finite-length performance. Interestingly, the optimal code parameter set  $(l,r,w)$  varies depending on the coupling length  $L$  and uncoupled code length  $M$  that determine the code and decoder specifications, which means there is no specific code parameter set prevailing over different kinds of applications. Finally, we illustrate this result using the investigated trade-offs on the code parameters, which gives us useful insight on how to choose the code parameters.

## GPU-Based, LDPC Decoding for 5G and Beyond

- **Status**: ✅
- **Reason**: 5G 바이너리 LDPC GPU 디코딩 병렬화 전략(코드워드/레이턴시 트레이드오프) — 이식 가능 디코더 병렬화 기법(D), Phase 3 검토
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9336349
- **Type**: journal
- **Published**: 2021
- **Authors**: Chance Tarver, Matthew Tonnemacher, Hao Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/9336349
- **Abstract**: In 5G New Radio (NR), low-density parity-check (LDPC) codes are included as the error correction codes (ECC) for the data channel. While LDPC codes enable a low, near Shannon capacity, bit error rate (BER), they also become a computational bottleneck in the physical layer processing. Moreover, 5G LDPC has new challenges not seen in previous LDPC implementations, such as Wi-Fi. The LDPC specification in 5G includes many reconfigurations to support a variety of rates, block sizes, and use cases. 5G also creates targets for supporting high-throughput and low-latency applications. For this new, flexible standard, traditional hardware-based solutions in FGPA and ASIC may struggle to support all cases and may be cost-prohibitive at scale. Software solutions can trivially support all possible reconfigurations but struggle with performance. This article demonstrates the high-throughput and low-latency capabilities of graphics processing units (GPUs) for LDPC decoding as an alternative to FPGA and ASIC decoders, effectively providing the high performance needed while maintaining the benefits of a software-based solution. In particular, we highlight how by varying the parallelization strategy for mapping GPU kernels to blocks, we can use the many GPU cores to compute one codeword quickly to target low-latency, or we can use the cores to work on many codewords simultaneously to target high throughput applications. This flexibility is particularly useful for virtualized radio access networks (vRAN), a next-generation technology that is expected to become more prominent in the coming years. In vRAN, the hardware computational resources will become decoupled from the specific computational functions in the RAN through virtualization, allowing for benefits such as load-balancing, improved scalability, and reduced costs. To highlight and investigate how the GPU can accelerate tasks such as LDPC decoding when containerizing vRAN functionality, we integrate our decoder into the Open Air Interface (OAI) NR software stack. With our GPU-based decoder, we measure a best case-latency of  $87~\mu \text{s}$  and a best-case throughput of nearly 4 Gbps using the Titan RTX GPU.

## Analytical Determination of Thresholds of LDPC Codes in Free Space Optical Channel

- **Status**: ✅
- **Reason**: LDPC BP 임계값을 비가우시안 FSO 채널에서 결정하는 divide-and-conquer 알고리즘; 비가우시안 LLR 임계값 해석은 NAND(비대칭/비가우시안 채널) 코드설계에 이식 가능성, 애매하여 살림(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9272655
- **Type**: journal
- **Published**: 2021
- **Authors**: Sonali, Abhishek Dixit, Virander Kumar Jain
- **PDF**: https://ieeexplore.ieee.org/document/9272655
- **Abstract**: Free-space optical (FSO) communication is crucial for the next-generation 5G+ wireless networks. The FSO links suffer from atmospheric-turbulence-induced bit errors. For the increasing link's performance, low-density parity-check (LDPC) codes, complemented by the belief-propagation (BP) algorithm, are an excellent option. The bit error rate (BER) of the LDPC code is characterized by a parameter called the threshold. The threshold is the signal-to-noise ratio (SNR), after which the BER falls arbitrarily and becomes close to zero. We derive the threshold for the LDPC codes under the BP algorithm for an uncorrelated flat FSO channel. The determination of the FSO channel threshold is a tedious task as the density of the log-likelihood ratio from the FSO channel cannot be assumed as Gaussian and is available only in a numerical form. It, thus, requires testing different values of SNR as a possible threshold systematically. Therefore, we propose the divide and conquer algorithm. The threshold depends on the degree distributions, channel state information (CSI), and the turbulence level. When CSI is known, we obtain the threshold at an SNR of 8.10 dB in high turbulence for a regular (3, 6) LDPC code. This threshold steps up to 12.48 dB when the CSI is unknown at the receiver. We evaluate the threshold values for various degree distributions (regular and irregular LDPC codes) under high, moderate, and low turbulence levels for both channel models (CSI known and unknown at the receiver). We also confirm the derived threshold values with MATLAB simulations.

## Review on 5G NR LDPC Code: Recommendations for DTTB System

- **Status**: ✅
- **Reason**: 5G NR LDPC 코드의 코드설계·디코딩 알고리즘·디코더 아키텍처 리뷰로 바이너리 LDPC 디코더/HW/구성 기법 이식 가능 → C/D/E 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9580903
- **Type**: journal
- **Published**: 2021
- **Authors**: Fengshuang Li, Chao Zhang, Kewu Peng +6
- **PDF**: https://ieeexplore.ieee.org/document/9580903
- **Abstract**: The freeze of the 5th generation new radio (5G NR) Release 16 indicates that 5G development has stepped into a new stage. The application of a dedicated low-density parity-check (LDPC) code for channel coding is an important technical advance that distinguishes 5G NR from the 4th generation (4G) long-term evolution (LTE) and LTE-advanced. Although LDPC codes have been used in many different systems, the newly developed LDPC code in 5G NR integrates many cutting-edge technologies to provide better performance and attractive features. Thus, it can be a good reference for channel coding in other evolving systems headed by digital terrestrial television broadcasting (DTTB). In emerging applications, the DTTB system needs to carry information with higher density, while meeting the high requirements for real-time, coverage, and bit error rate of broadcasting. To provide a reference for DTTB channel coding that improves its performance and supports new services, a review of 5G NR LDPC code implementation is carried out from three aspects: code analysis and design, decoding algorithm, and decoder architecture. We thoroughly evaluate each solution and highlight some candidates for existing implementations or directions for further development of the DTTB system.

## An FPGA-Based LDPC Decoder With Ultra-Long Codes for Continuous-Variable Quantum Key Distribution

- **Status**: ✅
- **Reason**: 초장 QC-LDPC용 레이어드 SP 디코더 HW(균일 양자화, Ψ(x) 2차근사, 충돌방지 H행렬, FPGA) — CV-QKD 정보조정용이나 고전 바이너리 LDPC 디코더·HW 기법으로 NAND 이식 가능(C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9376906
- **Type**: journal
- **Published**: 2021
- **Authors**: Shen-Shen Yang, Jian-Qiang Liu, Zhen-Guo Lu +3
- **PDF**: https://ieeexplore.ieee.org/document/9376906
- **Abstract**: In this paper, we propose a good decoding performance, low-complexity, and high-speed decoder architecture for ultra-long quasi-cyclic LDPC codes by using the layered sum-product decoding scheme. To reduce implementation complexity and hardware resource consumption, the messages in the iteration process are uniformly quantified and the function Ψ(x) is approximated with second-order functions. The decoder architecture improves the decoding throughput by using partial parallel and pipeline structures. A modified construction method of parity check matrices was applied to prevent read&write conflicts and achieve high-speed pipeline structure. The simulation results show that our decoder architecture has good performance at signal-to-noise ratios (SNRs) as low as -0.6 dB. We have implemented our decoder architecture on a Virtex-7 XC7VX690T field programmable gate array (FPGA) device. The implementation results show that the FPGA-based LDPC decoder can achieve throughputs of 108.64 Mb/s and 70.32 Mb/s at SNR of 1.0 dB when the code length is 262,144 and 349,952, respectively. The decoder can find useful applications in those scenarios that require very low SNRs and high throughputs, such as the information reconciliation of continuous-variable quantum key distribution.

## On the Construction of Multitype Quasi-Cyclic Low-Density Parity-Check Codes With Different Girth and Length

- **Status**: ✅
- **Reason**: 멀티타입 QC-LDPC 구성 — 최대달성 girth 탐색·slope행렬 설계로 길이/레이트/최소거리 개선, 바이너리 QC-LDPC 코드설계 기여(E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9399069
- **Type**: journal
- **Published**: 2021
- **Authors**: Farzaneh Abedi, Mohammad Gholami
- **PDF**: https://ieeexplore.ieee.org/document/9399069
- **Abstract**: Multitype quasi-cyclic (QC) low-density parity-check (LDPC) codes are a class of protograph LDPC codes lifted cyclically from protographs with multiple edges, represented by two weight and slope matrices. For a given weight-matrix, an approach is proposed to find the maximum-achievable girth  $g_{\max }$  of the corresponding multitype QC-LDPC codes by some inevitable chains having less complexity than the existing methods. This advantage leads to some new patterns of the weight matrices such that the corresponding codes have some improvements in terms of the maximum-achievable girths or the minimum-distance upper-bounds. In continue, for a given weight-matrix with maximum-achievable girth  $g_{\max }$ , some slope-matrices are constructed by a depth-first search algorithm for which the corresponding multitype QC-LDPC codes with even girth  $g$ ,  $g\le g_{\max }$ , have smaller lengths, higher rates, or larger minimum-distances than the state-of-the-art achievements. Simulation results show that the constructed codes have some error-rate advantages than PEG, random-like, CCSDS, and 802.11n/ac IEEE standard LDPC codes.

## Joint Detection and Decoding of Mixed-ADC Large-Scale MIMO Communication Systems With Protograph LDPC Codes

- **Status**: ✅
- **Reason**: Protograph LDPC + mixed-ADC 양자화 결합 메시지패싱 복호·PEXIT 분석 — 저해상도 양자화 LLR 처리는 NAND LDPC 이식 검토 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9486961
- **Type**: journal
- **Published**: 2021
- **Authors**: Hung N. Dang, Hieu T. Nguyen, Thuy V. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9486961
- **Abstract**: Nowadays, large-scale multiple-input multiple-output (LS-MIMO) with low-resolution analog-to-digital converters (ADCs) is a favorable transmission scheme for 5G and beyond wireless networks to reduce the power consumption of the radio frequency chains and to increase the network capacity. This paper derives the joint message-passing detection and decoding algorithm based on the double-layer graph for LS-MIMO communication systems with mixed-ADCs. The new protograph extrinsic information chart (PEXIT) algorithm is developed to analytically evaluate the performance of protograph low-density parity-check code under various mixed-ADC combinations and LS-MIMO configuration scenarios. The simulation results validate the accuracy of the proposed algorithm. Furthermore, our experiments show that the mixed-ADC system can achieve a significant power gain even when only one received antenna is equipped with high-resolution ADCs. It is observed that 4-bit or 5-bit resolution is an optimal choice for the high-resolution receive antennas. Interestingly, mixed-ADC systems with Ternay-ADCs generally provide significant gains at the cost of the increase in the average resolution by a fraction of a bit. There are specific scenarios where the Ternary-ADC-based system outperforms the 1-bit-ADC based system at the same or lower average resolution. In the particular case of 16 ×16 MIMO configuration where the number of low-resolution antennas is NL = 12 and the number of high-resolution antennas is NH = 4, the Ternary-ADC based system can obtain a power gain of about 2 dB at the frame error rate (FER) or bit error rate (BER) level of 10-5.

## LDPC Decoding Techniques for Free-Space Optical Communications

- **Status**: ✅
- **Reason**: WBF/IERRWBF 비트플리핑 디코딩 기법 비교 개선; FSO 응용이나 디코더 알고리즘은 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9551206
- **Type**: journal
- **Published**: 2021
- **Authors**: Albashir Adel Youssef, Mohamed Abaza, Ayshah S. Alatawi
- **PDF**: https://ieeexplore.ieee.org/document/9551206
- **Abstract**: There has been significant interest in free-space optical (FSO) communication by the research community in recent years. This is due to its high data rate, unlicensed spectrum, low cost, and immense security for FSO systems. Due to these advantages, FSO can have broader applications that extend from terrestrial to satellite communication. Atmospheric turbulence (AT) induced fading is a primary problem in the FSO link since it significantly impairs its performance. Atmospheric turbulence occurs due to the random variation of the air refractive index with time. Several statistical models are introduced to characterize the AT. The Log-normal (LN) model represents weak and moderate turbulence, and the Gamma-Gamma (G-G) model is employed for strong turbulence. These models are used with the effect of weather attenuation, geometric losses, and misalignment errors. One possible solution is channel coding, such as low-density parity-check (LDPC) codes. This paper proposed employing Weighted Bit Flipping (WBF) and Implementation Efficient Reliability Ratio Weighted Bit Flipping (IERRWBF) decoding techniques to improve FSO link performance. The results show a superior improvement in the bit error rate (BER) than the uncoded FSO system. In addition, the obtained results prove that the IERRWBF technique is more optimized than WBF from the point of the number of iterations, especially in weak and moderate turbulence FSO channels. In the calculation of decoders processing time, the WBF maintained lower decoding time than the IERRWBF technique, while in higher  $E_{b}/N_{o}\text{s}$ , they have the same level. The same response for both techniques in the case of resultant throughput. Finally, both methods are evaluated from the point of convergence. IERRWBF technique achieved faster convergence than WBF in all FSO channels under study.

## A Review of Deep Learning in 5G Research: Channel Coding, Massive MIMO, Multiple Access, Resource Allocation, and Network Security

- **Status**: ✅
- **Reason**: 5G 딥러닝 리뷰에 LDPC 코딩 포함 — 신경망 디코더(C) 관련 기법 단서, 애매하므로 살림(Phase 3 검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9353849
- **Type**: journal
- **Published**: 2021
- **Authors**: Amanda Ly, Yu-Dong Yao
- **PDF**: https://ieeexplore.ieee.org/document/9353849
- **Abstract**: The current development of 5G technology is flourishing with widespread deployment across the world at a rapid pace. However, there is still a demand concerning 5G research for service and performance improvement. Research tasks include but are not limited to quality-of-service (QoS), energy efficiency, massive connectivity, reliable communications, and security. Due to the advancement of deep learning, numerous such research has utilized this technique. This article provides a comprehensive review of 5G communications research using deep learning. Specifically, we address the issues of low-density parity-check (LDPC) coding, massive multiple-input multiple-output (MIMO), non-orthogonal multiple access (NOMA), resource allocation, and security.

## Syndrome-Based Min-Sum vs OSD-0 Decoders: FPGA Implementation and Analysis for Quantum LDPC Codes

- **Status**: ✅
- **Reason**: QLDPC지만 BP min-sum + OSD-0 디코더의 FPGA HW 구현/지연·클럭 분석으로, 디코더가 고전 바이너리 LDPC에서 유래하고 양자 전용 개념 비의존 → C/D 예외 포함, Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9562513
- **Type**: journal
- **Published**: 2021
- **Authors**: Javier Valls, Francisco Garcia-Herrero, Nithin Raveendran +1
- **PDF**: https://ieeexplore.ieee.org/document/9562513
- **Abstract**: Quantum processors need to improve their reliability to scale up the number of qubits and increase the number of algorithms that can execute. To reduce the logical error rate of the quantum systems, the use of error correction codes and decoders has been established as a low-cost and feasible approach, with good results from a theoretical perspective, for mid and long-term architectures. While most of the authors are focused on the algorithms to improve the correction capability of quantum computers, without taking into account a fundamental implementation aspect for their deployment in a real system, i.e., their latency must be bounded to avoid the qubit decoherence, only a few propose hardware architectures and they just include time estimations of their decoding latency. However, a real implementation has not been shown yet. In this work, we analyze from the point of view of hardware implementation two algorithmic options based on quantum low-density parity-check (QLDPC) codes: a) belief propagation min-sum decoders combined with codes with good error-floor behavior and b) belief propagation min-sum decoders concatenated with ordered statistics decoders (OSDs) for codes with early error-floor. The bounds for the maximum clock frequency required by the decoders to decode within the qubit coherence time are established as a parameter to show if a practical implementation is possible with the present or near future FPGA technology. Furthermore, real implementation results for a Xilinx FPGA device are provided, showing that some solutions can meet the timing constraints set up by the state-of-the-art quantum processors.

## Efficient Hardware Implementation of the LEDAcrypt Decoder

- **Status**: ✅
- **Reason**: LEDAcrypt 반복 디코더의 FPGA/ASIC HW 구현(곱셈기 최적화, 면적/지연 최적화)으로 D 카테고리 이식 가능 HW 아키텍처. 암호 기반이나 LDPC 디코더 HW 기법 떼어낼 수 있어 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9417170
- **Type**: journal
- **Published**: 2021
- **Authors**: Kristjane Koleci, Paolo Santini, Marco Baldi +3
- **PDF**: https://ieeexplore.ieee.org/document/9417170
- **Abstract**: This work describes an efficient implementation of the iterative decoder that is the main part of the decryption stage in the LEDAcrypt cryptosystem, recently proposed for post-quantum cryptography based on low-density parity-check (LDPC) codes. The implementation we present exploits the structure of the variables in order to accelerate the decoding process while keeping the area bounded. In particular, our focus is on the design of an efficient multiplier, the latter being a fundamental component also in view of considering different values of the cryptosystem's parameters, as it might be required in future applications. We aim to provide an architecture suitable for low cost implementation on both Field Programmable Gate Array (FPGA) and Application Specific Integrated Circuit (ASIC) implementations. As for the FPGA, the total execution time is 0.6 ms on the Artix-7 200 platform, employing at most 30% of the total available memory, 15% of the total available Look-up Tables and 3% of the Flip-Flops. The ASIC synthesis has been performed for both STM FDSOI 28 nm and UMC CMOS 65 nm technologies. After logic synthesis with the STM FDSOI 28 nm, the proposed decoder achieves a total latency of 0.15 ms and an area occupation of 0.09 mm2. The post-Place&Route implementation results for the UMC 65 nm show a total execution time of 0.3 ms, with an area occupation of 0.42 mm2 and a power consumption of at most 10.5 mW.

## LDPC Hardware Acceleration in 5G Open Radio Access Network Platforms

- **Status**: ✅
- **Reason**: 5G LDPC FPGA 가속기 아키텍처(1.6Gbps, SW 대비 13배); 이식 가능 HW 디코더 기여(D).
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9610039
- **Type**: journal
- **Published**: 2021
- **Authors**: Elissaios Alexios Papatheofanous, Dionysios Reisis, Konstantinos Nikitopoulos
- **PDF**: https://ieeexplore.ieee.org/document/9610039
- **Abstract**: The Open Radio Access Network (RAN) concept has been gaining wide acceptance in recent network architectures, including 5G New Radio (NR) network deployments. Current Open RAN radio implementation efforts, aim at integrating several white-box hardware elements and executing digital processing on open-source software. When building such a software-based, 5G Open RAN platform, challenges include achieving real-time execution times for demanding computational blocks of the 5G NR physical layer processing, such as Low Density Parity Check (LDPC) decoding. In this context, having already identified both the capabilities as well as the challenges that Field-programmable Gate Arrays (FPGAs) offer for accelerating LDPC, we present our novel LDPC FPGA accelerator system. In this paper, we contribute the implementation details of our FPGA accelerator design as well as the process of integrating the accelerator with OpenAirInterface (OAI), the basis for our 5G NR platform. For the first time in the literature, we show an FPGA-based LDPC accelerator fully integrated with a complete software platform, that is able to achieve more than  $1.6Gbps$  decoding throughput and up to 13 times faster execution times compared to single core software implementations. Finally, in our results, we show that LDPC encoding is more challenging to accelerate due to lower computational complexity.

## Discrete BP Polar Decoder Using Information Bottleneck Method

- **Status**: ✅
- **Reason**: Information Bottleneck 기반 LDPC BP 양자화 LUT 디코더 기법 — LLR 양자화/이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9319186
- **Type**: journal
- **Published**: 2021
- **Authors**: Akira Yamada, Tomoaki Ohtsuki
- **PDF**: https://ieeexplore.ieee.org/document/9319186
- **Abstract**: Polar code is one of the channel codes and is used in the 5th generation of mobile communication system (5G). This encoding scheme is based on the operation of channel polarization, and it is possible to achieve the capacity of arbitrary binary-input symmetric discrete memoryless channels. Compared with Turbo codes and LDPC (Low-Density Parity-Check) codes, the implementation of the encoder and decoder is easier. BP (Belief Propagation) decoding, one of the decoding methods of the polar codes, can be performed at high speed because it can decode in parallel. However, the disadvantages of the BP decoding are the hardware and computational complexities. The technique of quantization can be used to reduce complexities of hardware and calculation. One of the quantization methods is the information bottleneck method, which allows an observation variable to compressed one while trying to preserve the mutual information shared with a relevant variable. As a novel approach, the information bottleneck method is used in the design of quantizers for the BP decoding of LDPC codes. In this paper, we propose a discrete BP polar decoder that can use only unsigned integers in the decoding process by using the information bottleneck method. Thus, we can replace complex calculations of BP decoding with simple lookup tables. We also investigate the minimum bit width for quantization with negligible degradation and the suboptimal  $E_{b}/N_{0}$  for designing lookup tables, where  $E_{b}$  and  $N_{0}$  denote energy per bit and noise power density, respectively. The simulation results show that the proposed method can achieve almost the same error correcting capability compared with the BP decoding without compression in the range of low  $E_{b}/N_{0}$ . Besides, we show that the proposed decoder can compress both channel outputs and BP messages with small loss compared with the uniform quantization decoder.

## Concatenated Codes for Recovery From Multiple Reads of DNA Sequences

- **Status**: ✅
- **Reason**: DNA 저장용 concatenated LDPC, insertion/deletion/substitution 채널에 대한 새 다중 수신 APP 디코딩 알고리즘 제시 (C, 이식 가능 디코더)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9457675
- **Type**: conference
- **Published**: 2021
- **Authors**: A. Lenz, I. Maarouf, L. Welter +3
- **PDF**: https://ieeexplore.ieee.org/document/9457675
- **Abstract**: Decoding sequences that stem from multiple transmissions of a codeword over an insertion, deletion, and substitution channel is a critical component of efficient deoxyribonucleic acid (DNA) data storage systems. In this paper, we consider a concatenated coding scheme with an outer low-density parity-check code and either an inner convolutional code or a block code. We propose two new decoding algorithms for inference from multiple received sequences, both combining the inner code and channel to a joint hidden Markov model to infer symbolwise a posteriori probabilities (APPs). The first decoder computes the exact APPs by jointly decoding the received sequences, whereas the second decoder approximates the APPs by combining the results of separately decoded received sequences. Using the proposed algorithms, we evaluate the performance of decoding multiple received sequences by means of achievable information rates and Monte-Carlo simulations. We show significant performance gains compared to a single received sequence.

## Adjustable Ordered Statistic Decoder for Short Block Length Code towards URLLC

- **Status**: ✅
- **Reason**: 단블록 OSD 디코더 개선(TEP/WHD 임계 조정으로 복잡도 80% 절감); 이식 가능 디코더 알고리즘(C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9613322
- **Type**: conference
- **Published**: 2021
- **Authors**: F. Wang, J. Jiao, K. Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/9613322
- **Abstract**: The fifth generation (5G) ultra-reliable low latency communications (uRLLC) needs short block length codes to ensure the low latency requirement, which also brings the challenge in the design of maximum likelihood decoder (MLD) with practical complexity. In this paper, an adjustable-ordered statistics decoder (OSD) algorithm is proposed for short block length code to achieve the MLD performance with much lower decoding complexity, by finding the reasonable thresholds of the test error patterns (TEP) likelihood and weighted Hamming distance (WHD) in OSD decoding. In addition, we drive the closed-form expressions to the TEP likelihood and WHD thresholds, respectively, and construct the adjustable-OSD parameter table of reasonable thresholds of TEP and WHD according to the required block error rate (BLER). Simulation results validate the accuracy of our theoretical derivations, and also show that our adjustable-OSD can achieve 10−5 BLER at 4 dB, where the decoding complexity is reduced up to 80% compared with the full OSD.

## Fault Organized Decoders Using Analog VLSI Implementations- A Survey

- **Status**: ✅
- **Reason**: factor graph/sum-product 기반 fault-tolerant 디코더 아날로그 VLSI 구현 서베이; LDPC 포함 sum-product 디코더 HW 기법 다룸(D), 애매하나 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:9591960
- **Type**: conference
- **Published**: 2021
- **Authors**: A. Deepika, K. Manjunathachari
- **PDF**: https://ieeexplore.ieee.org/document/9591960
- **Abstract**: VLSI technology had a key role in the design of most of today’s high-tech electronic circuits. Though smaller, less expensive, requiring less power, highly dependable, and full of functionality, VLSI design takes an extended amount of time to manufacture a high-risk product. The complexity of computing of such default coding systems however stands in the way of its application. Many researchers have shown that fault checking decoders can be construed on the Probability Spread Network as a type of factor graph as a Sum-Product Algorithm operation. The most advanced communication systems are based on fault structured codes. The most famous codes of this kind include turbo codes, low-density parity tests and versions for performing the closest to the theoretical Shannon limit. These are decoded by the ’Generic Summary Model Probability’ or by the versions thereof. In this document, many of the most often used fault organizing codes are fully analyzed and investigated.

## A Novel Iterative Soft-Decision Decoding Algorithm for RS-SPC Product Codes

- **Status**: ✅
- **Reason**: RS-SPC 패리티검사 바이너리 전개에 BP 반복디코딩, 부호 비의존적 BP 기법 이식 여지(C)—Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9685385
- **Type**: conference
- **Published**: 2021
- **Authors**: M. Zhu, M. Jiang, C. Zhao
- **PDF**: https://ieeexplore.ieee.org/document/9685385
- **Abstract**: This paper presents a generalized construction of RS-SPC product codes. A low-complexity joint-decoding scheme is proposed for these codes, in which a BP-based iterative decoding is performed based on the binary expansion of the whole parity-check matrix. Various powerful RS codes can be used as the component codes for RS-SPC product codes, which gives a good performance for local decoding (decode a single component codeword). The proposed BP-based iterative decoding is a global decoding, and it achieves an error-correcting capability compa-rable to codes of large blocklengths. This two-phase decoding scheme preserves the low decoding latency and complexity of the local decoding while achieves high reliability through the global decoding. The complexity of the proposed iterative decoding is discussed, and the simulation results show the proposed scheme offers a good trade-off between the complexity and the error performance.

## Enhanced Loop-weakened Belief Propagation Algorithm for Performance Enhanced Polar Code Decoders

- **Status**: ✅
- **Reason**: 폴라 BP에서 factor graph 단주기(short cycle) 영향 완화 연산 변형 — 사이클 완화 BP 기법이 LDPC BP에 이식 가능성, 애매해서 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9689661
- **Type**: conference
- **Published**: 2021
- **Authors**: A. B. Van Den Brink, M. J. G. Bekooij
- **PDF**: https://ieeexplore.ieee.org/document/9689661
- **Abstract**: A polar code decoder based on the belief propagation algorithm is desirable because of the potentially low latency and its suitability for parallel execution on multicore and SIMD processors. However, current state-of-the-art algorithms require many iterations to achieve comparable bit and frame error rate compared to successive cancellation algorithms. Also, the current state-of-the-art belief propagation algorithms have a high computational complexity compared to successive cancellation. In this paper we present an enhanced belief propagation algorithm, in which parts of the computations are altered to reduce the negative effect of the short cycles in the polar code factor graph. Our proposed algorithm has a gain of $\approx+0.4\mathbf{dB}$ in both frame and bit error rate compared to successive cancellation and a gain of $\approx+0.16\mathbf{dB}$ and $\approx+0.13\mathbf{dB}$ at a frame and bit error rate of 10−3 respectively, compared to belief propagation. Also, the maximum number of iterations of our algorithm is reduce to $0.6\cdot I_{max}$. As a result, the latency is up to $\approx 11$ times lower compared to successive cancellation and up to $\approx 1.8$ times lower compared to the current state-of-the-art belief propagation polar code algorithm. Furthermore, the reduction in the maximum iteration count results in a lower power consumption after implementation.

## Computational Complexity Reduced Belief Propagation Algorithm for Polar Code Decoders

- **Status**: ✅
- **Reason**: 폴라 BP 디코더 노드 산술복잡도 축소(가산·비교·곱셈 감소) — 부호 비의존 BP 단순화 가능성, 애매해서 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9689482
- **Type**: conference
- **Published**: 2021
- **Authors**: A. B. Van Den Brink, M. J. G. Bekooij
- **PDF**: https://ieeexplore.ieee.org/document/9689482
- **Abstract**: The belief propagation algorithm is desirable for a polar code based decoder, because of the potentially low latency and the ability of integration in digital signal processing units or other multi-core processor systems to parallelize the computations. Although belief propagation polar code decoder algorithms have the ability for a highly parallelized imple-mentation, the algorithms require many iterations to achieve a comparable frame error rate and bit error rate with respect to a successive cancellation polar code algorithm. The iterative nature of the belief propagation algorithms also result in a higher computational complexity, i.e. $O(IN(2\log_{2} N-1))$ compared to the computational complexity $O(N\log_{2}N)$ of the successive cancellation decoder algorithm. In this paper we propose several simplifications for a simplified belief propagation algorithm for polar code decoders, where the arithmetic complexity of the nodes is reduced. The proposed belief propagation algorithm shows preliminary results of a net reduction of the arithmetic complexity of ≈ 13%. This reduction is a result of the reduced number of arithmetic operations, i.e., additions, compares, and multiplications, without a lost in error-correcting performance.

## GRADE-AO: Towards Near-Optimal Spatially-Coupled Codes With High Memories

- **Status**: ✅
- **Reason**: 고메모리 QC-SC-LDPC near-optimal 구성(파티셔닝 밀도분포 최적화+사이클 최적화) — 바이너리 SC-LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9517931
- **Type**: conference
- **Published**: 2021
- **Authors**: S. Yang, A. Hareedy, S. Venkatasubramanian +2
- **PDF**: https://ieeexplore.ieee.org/document/9517931
- **Abstract**: Spatially-coupled (SC) codes, known for their threshold saturation phenomenon and low-latency windowed decoding algorithms, are ideal for streaming applications and data storage systems. SC codes are constructed by partitioning an underlying block code, followed by rearranging and concatenating the partitioned components in a “convolutional” manner. The number of partitioned components determines the “memory” of SC codes. While adopting higher memories results in improved SC code performance, obtaining optimal SC codes with high memory is known to be hard. In this paper, we investigate the relation between the performance of SC codes and the density distribution of partitioning matrices. We propose a probabilistic framework that obtains (locally) optimal density distributions via gradient descent. Starting from random partitioning matrices abiding by the obtained distribution, we perform low complexity optimization algorithms over the cycle properties to construct high memory, high performance quasi-cyclic SC codes. Simulation results show that codes obtained through our proposed method notably outperform state-of-the-art SC codes with the same constraint length and codes with uniform partitioning.

## Optimizing Deep Learning Decoders for FPGA Implementation

- **Status**: ✅
- **Reason**: DL 디코더 FPGA 구현 + 압축/근사로 복잡도 저감; 신경망 디코더 HW 아키텍처 NAND LDPC 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9556409
- **Type**: conference
- **Published**: 2021
- **Authors**: E. Kavvousanos, V. Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/9556409
- **Abstract**: Recently, Deep Learning (DL) methods have been proposed for use in the decoding of linear block codes. While novel DL decoders show promising error correcting performance, they suffer from computational complexity issues, which prevent their usage with large block codes and make their implementation in digital hardware inefficient. The subject of the presented doctoral research is the design of DL decoding methods with low computational complexity and resource requirements, by applying compression and approximation techniques to the employed Neural Networks. Efficient hardware architectures are expected to be designed for these optimized DL decoders on FPGA devices, which will overcome the current performance limitations.

## Minimum-Variance Importance Sampling Estimator for Fast Simulation of Linear Block Codes over Binary Erasure Channels

- **Status**: ✅
- **Reason**: BEC상 선형블록부호 오류성능 고속 시뮬레이션용 importance sampling 추정기; LDPC error floor/유한길이 평가에 이식 가능(E) 가능성으로 애매하게 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9443863
- **Type**: conference
- **Published**: 2021
- **Authors**: J. Pan, W. H. Mow
- **PDF**: https://ieeexplore.ieee.org/document/9443863
- **Abstract**: In this paper, the problem of efficiently evaluating the error performance of linear block codes over binary erasure channels (BECs) is considered. We propose a novel importance sampling (IS) estimator by deriving the optimal IS distribution of the erasure pattern size. Consequently, a corresponding iterative algorithm for fast simulation purpose is proposed. The effectiveness of the proposed IS algorithm compared to Monte Carlo simulation is demonstrated in estimating the block erasure rate of low-density parity-check codes, and IS gains of almost ten orders of magnitude is achieved.

## Joint Demodulation and Decoding with Multi-Label Classification Using Deep Neural Networks

- **Status**: ✅
- **Reason**: DNN 기반 결합 복조/복호기; 신경망 디코더 기법(C)으로 LDPC 복호 이식 가능성 있어 Phase 3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9415182
- **Type**: conference
- **Published**: 2021
- **Authors**: I. Ahmed, W. Xu, R. Annavajjala +1
- **PDF**: https://ieeexplore.ieee.org/document/9415182
- **Abstract**: In this paper, we leverage the power of artificial intelligence in the receiver design for joint baseband demodulation and channel decoding. We consider a point-to-point communication system and develop a deep neural network (DNN) based joint demodulator and decoder (DeModCoder) that accomplishes the tasks of demodulation and decoding in a single operational block. We incorporate a multi-label classification (MLC) scheme for the considered DNN framework, which is trained offline over a wide-range of signal-to-noise ratios (SNRs) in a supervised learning manner and deployed online in real-time applications. Simulation results demonstrate that our developed DeModCoder outperforms the conventional block-based sequential demodulation and decoding schemes. We also observe that the MLC DeModCoder shows better performance than conventional multiple output classifier in high SNR region while incurring lower computational complexity.

## A Weighted Bit Flipping Decoder for QC-MDPC-based Cryptosystems

- **Status**: ✅
- **Reason**: QC-MDPC용 weighted bit-flipping 반복 디코더 개선(DFR 분석, 하이브리드) — bit-flipping 디코더 기법은 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9517902
- **Type**: conference
- **Published**: 2021
- **Authors**: A. Nilsson, I. E. Bocharova, B. D. Kudryashov +1
- **PDF**: https://ieeexplore.ieee.org/document/9517902
- **Abstract**: A new “Weighted Bit-flipping” (WBF) iterative decoder is presented and analyzed with respect to its Decoding Failure Rate (DFR). We show that the DFR is indeed lower than that of the BGF decoder as suggested by the BIKE third round submission to the NIST PQC standardization process. The WBF decoder requires more iterations to complete than BGF, but by creating a hybrid decoder we show that a lower DFR compared to that of the BGF decoder can still be achieved while keeping the computational tradeoff to a minimum.

## Joint Activity Detection and Data Decoding for Grant-Free Massive MIMO Systems

- **Status**: ✅
- **Reason**: 동적 메시지 스케줄링(RBP) 기반 BP 개선; 메시지패싱 스케줄링 기법은 바이너리 LDPC 디코더에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9562217
- **Type**: conference
- **Published**: 2021
- **Authors**: R. B. Di Renna, R. C. De Lamare
- **PDF**: https://ieeexplore.ieee.org/document/9562217
- **Abstract**: This work addresses the problem of joint active device detection and data decoding in an uplink grant-free massive multiple-input multiple-output (MIMO) scenario. We develop a message-passing solution that uses channel decoder beliefs to refine the activity detection and data decoding. In order to improve the detection and decoding performance, we introduce a dynamic message-scheduling concept, where we apply scheduling techniques according to the activity user detection (AUD) and the residual belief propagation (RBP). Simulation results show that our proposed schemes outperform state-of-the-art algorithms in terms of frame error rate (FER), false alarms (FAR) and missed detection rates (MDR), requiring a small number of iterations for convergence and lower complexity.

## NAND Flash Memory and Its Place in IoT

- **Status**: ✅
- **Reason**: NAND 플래시(2D/3D TLC/QLC) 신뢰성·에러·웨어아웃 직접 논의 (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9467859
- **Type**: conference
- **Published**: 2021
- **Authors**: S. Bennett, J. Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/9467859
- **Abstract**: Data storage requires an answer to the constantly evolving question - how best to store the mammoth amount of data being generated? There is a great diversity of storage solutions currently, ranging from personal USB devices, personal Solid State Drives (SSD) and HardDrives (HD) to Cloud storage and server farms. However, the right storage solution depends on how the data will be used. As Flash memory plays a key role in all the hierarchy levels of Internet of Things (IoT) systems, this paper will lay out a broad discussion on both IoT and Solid State Memory (SSM), followed by an attempt to link these two fields. The topics mentioned under IoT include: Big Data and the Cloud, The Cloud of Things, Flash in the Datacentre, Scalability and Reliability, Edge Computing, Fog Computing and Osmotic Computation. While, topics under SSM include: Non-volatile Reliability, Errors and Wearout, NOR v NAND, 2D TLC, 3D TLC, QLC and Optane.

## Optimal Thresholding Quantizer Maximizing Mutual Information of Discrete Multiple-Input Continuous One-Bit Output Quantization

- **Status**: ✅
- **Reason**: 상호정보량 최대화 1비트 출력 양자화 임계값 최적화 — NAND LLR 양자화(read threshold) 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9518029
- **Type**: conference
- **Published**: 2021
- **Authors**: T. Nguyen, T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/9518029
- **Abstract**: In this paper, we consider the problem of one-bit (two-level) output-quantization maximizing mutual information between quantizer-output and channel-input using a single threshold for a discrete signal that is corrupted by a continuous additive noise. A necessary condition is constructed for which the thresholding quantizer is optimal. In addition, we show that if the distribution of the additive noise satisfies a mild condition, then a global optimal threshold can be found efficiently via a modified fixed-point algorithm.

## Relative Entropy based Message Combining for Exploiting Diversity in Information Optimized Processing

- **Status**: ✅
- **Reason**: 저비트 해상도 정보최적화 처리의 이산 메시지 결합(REMC) — 양자화 min-sum/LLR 양자화 디코더에 이식 가능성, 애매해서 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9739149
- **Type**: conference
- **Published**: 2021
- **Authors**: T. Monsees, D. Wuebben, A. Dekorsy
- **PDF**: https://ieeexplore.ieee.org/document/9739149
- **Abstract**: Maximizing information has become a powerful technique for the design of efficient receiver components with very low bit resolution. In the established information processing approach, the algorithmic tasks are executed on discrete messages and the processing steps are designed to optimize the mutual information. In this paper, we extend the concept of information optimized processing for exploiting diversity. To that end, we propose the Relative Entropy based Message Combining (REMC) approach in order to merge discrete messages with different underlying distributions, e.g., stemming from different diversity branches. We exemplary evaluate the proposed REMC for a single-user uplink-model with multiple Radio Access Points (RAPs) and higher order modulation schemes. The numerical results show that message combining is required to leverages diversity gains in an information optimized receiver.

## Refined Reliability Combining for Binary Message Passing Decoding of Product Codes

- **Status**: ✅
- **Reason**: product code(GLDPC) 대상 iBDD-CR: BDD 출력 신뢰도 결합 소프트 디코딩+밀도진화 분석, 이식 가능 디코더 기법(C)으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9435057
- **Type**: journal
- **Published**: 2021
- **Authors**: A. Sheikh, A. Graell i Amat, G. Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/9435057
- **Abstract**: We propose a novel soft-aided iterative decoding algorithm for product codes (PCs). The proposed algorithm, named iterative bounded distance decoding with combined reliability (iBDD-CR), enhances the conventional iterative bounded distance decoding (iBDD) of PCs by exploiting some level of soft information. In particular, iBDD-CR can be seen as a modification of iBDD where the hard decisions of the row and column decoders are made based on a reliability estimate of the BDD outputs. The reliability estimates are derived by analyzing the extrinsic message passing of generalized low-density-parity check (GLDPC) ensembles, which encompass PCs. We perform a density evolution analysis of iBDD-CR for transmission over the additive white Gaussian noise channel for the GLDPC ensemble. We consider both binary transmission and bit-interleaved coded modulation with quadrature amplitude modulation. We show that iBDD-CR achieves performance gains up to 0.51 dB compared to iBDD with the same internal decoder data flow. This makes the algorithm an attractive solution for very high-throughput applications such as fiber-optic communications.

## An Early-Life NAND Flash Endurance Prediction System

- **Status**: ✅
- **Reason**: NAND 플래시 endurance/RBER/ECC 직접(A) — ML 기반 endurance 예측이지만 NAND ECC 임계치 운영과 직결, 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9597529
- **Type**: journal
- **Published**: 2021
- **Authors**: B. Fitzgerald, C. Ryan, J. Sullivan
- **PDF**: https://ieeexplore.ieee.org/document/9597529
- **Abstract**: NAND flash memory – ubiquitous in today’s world of smart phones, SSDs (solid state drives), and cloud storage – has a number of well-known reliability problems. NAND data contains bit errors, which require the use of error correcting codes (ECCs). The raw bit error rate (RBER) increases with program-erase (P-E) cycling, and the number of P-E cycles the device can withstand before the RBER exceeds the ECC capability is called its endurance. ECC operates on data stored in a sector of NAND, and there is a large variation in the endurance of sectors within a device and across devices, resulting in excessively conservative endurance specifications. This research shows, for the first time, that a sector’s true endurance can be predicted with remarkable accuracy, using a combination of the sector’s location within the device, and measurements taken at the very beginning of life. Real-world data is gathered on millions of NAND sectors using a custom-built test platform. Optimised machine learning classification models are built from the raw data to predict if a sector will pass or fail to a fixed ECC threshold, after a target P-E cycling level has been reached. A novel technique is demonstrated that uses different ECC thresholds for model training and testing, which allows the models to be tuned so that they never misclassify samples that would fail. This eliminates ECC failures and data loss, allowing simpler, less expensive ECC schemes to be used for modern NAND devices. It also enables significant endurance extensions to be achieved.

## A Revisit to Ordered Statistics Decoding: Distance Distribution and Decoding Rules

- **Status**: ✅
- **Reason**: OSD 알고리즘 거리분포 분석 및 stopping/discarding 규칙으로 복잡도 저감 — C 카테고리 이식 가능 디코더(OSD)에 새 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9427228
- **Type**: journal
- **Published**: 2021
- **Authors**: C. Yue, M. Shirvanimoghaddam, B. Vucetic +1
- **PDF**: https://ieeexplore.ieee.org/document/9427228
- **Abstract**: This paper revisits the ordered statistics decoding (OSD). It provides a comprehensive analysis of the OSD algorithm by characterizing the statistical properties, evolution and the distribution of the Hamming distance and weighted Hamming distance from codeword estimates to the received sequence in the reprocessing stages of the OSD algorithm. We prove that the Hamming distance and weighted Hamming distance distributions can be characterized as mixture models capturing the decoding error probability and code weight enumerator. Simulation and numerical results show that our proposed statistical approaches can accurately describe the distance distributions. Based on these distributions and with the aim to reduce the decoding complexity, several techniques, including stopping rules and discarding rules, are proposed, and their decoding error performance and complexity are accordingly analyzed. Simulation results for decoding various eBCH codes demonstrate that the proposed techniques can significantly reduce the decoding complexity with a negligible loss in the decoding error performance.

## Radiation-Induced Error Mitigation by Read-Retry Technique for MLC 3-D NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D MLC NAND read-retry로 방사선 오류 완화 + ECC 연계 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9328477
- **Type**: journal
- **Published**: 2021
- **Authors**: P. Kumari, U. Surendranathan, M. Wasiolek +3
- **PDF**: https://ieeexplore.ieee.org/document/9328477
- **Abstract**: In this article, we have evaluated the Read-Retry (RR) functionality of the 3-D NAND chip of multilevel-cell (MLC) configuration after total ionization dose (TID) exposure. The RR function is typically offered in the high-density state-of-the-art NAND memory chips to recover data once the default memory read method fails to correct data with error correction codes (ECCs). In this work, we have applied the RR method on the irradiated 3-D NAND chip that was exposed with a Co-60 gamma-ray source for TID up to 50 krad (Si). Based on our experimental evaluation results, we have proposed an algorithm to efficiently implement the RR method to extend the radiation tolerance of the NAND memory chip. Our experimental evaluation shows that the RR method coupled with ECC can ensure data integrity of MLC 3-D NAND for TID up to 50 krad (Si).

## A Soft-Aided Staircase Decoder Using Three-Level Channel Reliabilities

- **Status**: ✅
- **Reason**: iSABM soft-aided 3-level LLR 마킹/bit-flip 복호 — HD 코드용이나 LLR 신뢰도 임계·BF 기법은 LDPC 복호에 이식 검토 여지, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9483624
- **Type**: journal
- **Published**: 2021
- **Authors**: Y. Lei, B. Chen, G. Liga +3
- **PDF**: https://ieeexplore.ieee.org/document/9483624
- **Abstract**: The soft-aided bit-marking (SABM) algorithm is based on the idea of marking bits as highly reliable bits (HRBs), highly unreliable bits (HUBs), and uncertain bits to improve the performance of hard-decision (HD) decoders. The HRBs and HUBs are used to assist the HD decoder to prevent miscorrections and to decode those originally uncorrectable cases via bit flipping (BF), respectively. In this paper, an improved SABM algorithm (called iSABM) is proposed for staircase codes (SCCs). Similar to the SABM, iSABM marks bits with the help of channel reliabilities, i.e., using the absolute values of the log-likelihood ratios. The improvements offered by iSABM include: (i) HUBs being classified using a reliability threshold, (ii) BF randomly selecting HUBs, and (iii) soft-aided decoding over multiple SCC blocks. The decoding complexity of iSABM is comparable of that of SABM. This is due to the fact that on the one hand no sorting is required (lower complexity) because of the use of a threshold for HUBs, while on the other hand multiple SCC blocks use soft information (higher complexity). The gains achieved by iSABM are up to 0.53 dB with respect to SABM and up to 0.91 dB with respect to standard decoding of SCCs at a bit error rate of $10^{-6}$. Furthermore, it is shown that using 1-bit reliability marking, i.e., only having HRBs and HUBs, only causes a gain penalty of up to 0.25 dB with a significantly reduced memory requirement.

## Spatially Coupled Protograph LDPC-Coded Hierarchical Modulated BICM-ID Systems: A Promising Transmission Technique for 6G-Enabled Internet of Things

- **Status**: ✅
- **Reason**: SC protograph LDPC 코드 설계 + EXIT 임계값 분석, 바이너리 LDPC 구성/분석 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9210097
- **Type**: journal
- **Published**: 1 April1, 
- **Authors**: Zhaojie Yang, Yi Fang, Guojun Han +1
- **PDF**: https://ieeexplore.ieee.org/document/9210097
- **Abstract**: As a spectral-efficiency technique for unequal error protection (UEP), hierarchical modulation (HM) bit-interleaved coded modulation (BICM) with iterative decoding (ID) has attracted interests in the wireless communication community. In this article, we conduct an investigation on spatially coupled (SC) protograph low-density parity-check (P-LDPC)-coded  $M$ -ary quadrature amplitude modulation (QAM) HM-BICM-ID systems. We first develop an information-theoretic methodology to calculate  $(\log _{2}M)/2$  types of constellation-constrained average mutual information (AMI), which can be used to characterize the performance limits of different layers in the HM-BICM systems. We further propose a two-stage design approach to construct a novel type of constellations, called as structural quadrant (SQ) constellations, and develop a quadrant-based harmonic mean analysis to evaluate the nonfeedback and iterative-feedback asymptotic performance of the proposed constellations. In addition, we conceive a performance-analysis tool, referred to as multistream-based extrinsic information transfer (MS-EXIT) algorithm, for predicting the decoding thresholds of all individual coded-bit streams in the proposed SC P-LDPC-coded HM-BICM-ID systems. Simulation results not only agree well with the theoretical analyses but also indicate that the proposed SC P-LDPC-coded HM-BICM-ID systems are remarkably superior to the state-of-the-art counterparts. Thereby, the proposed SC P-LDPC-coded HM-BICM-ID systems are competent to provide diverse Quality of Service (QoS) for future wireless applications, such as 6G-enabled Internet of Things (IoT).

## Low-Complexity Rate- and Channel-Configurable Concatenated Codes

- **Status**: ✅
- **Reason**: 내부 QC-LDPC + 외부 zipper 연접부호, rate/channel-configurable 다단 구조 최적화로 디코딩 복잡도 절감 — 이식 가능한 코드설계/HW 기법(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9302648
- **Type**: journal
- **Published**: 1 April1, 
- **Authors**: Masoud Barakatain, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/9302648
- **Abstract**: A low-complexity rate- and channel-configurable forward error-correction (FEC) scheme is proposed, consisting of an inner low-density parity-check code concatenated with an outer zipper code. A tool is developed to optimize a multi-level code architecture so that it can operate at multiple transmission rates, channel qualities, and modulation orders. The optimization criterion is selected to maintain a low estimated data-flow in its decoding operation. A hardware-friendly quasi-cyclic structure is considered for the inner code and the performance and complexity is reported for various designed FEC configurations. Compared to existing FEC schemes, the proposed designs deliver a similar performance with up to 63% reduction in decoding complexity or provide up to 0.6 dB coding gain at a similar decoding complexity.
