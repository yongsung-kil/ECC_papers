# IEEE Xplore — 2013-04 (1차선별 통과)


## The Cycle Consistency Matrix Approach to Absorbing Sets in Separable Circulant-Based LDPC Codes

- **Status**: ✅
- **Reason**: E: SCB/QC-LDPC absorbing set 분석·회피용 CCM 신규 코드설계, error floor 개선(바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6387307
- **Type**: journal
- **Published**: April 2013
- **Authors**: Jiadong Wang, Lara Dolecek, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6387307
- **Abstract**: For low-density parity-check (LDPC) codes operating over additive white Gaussian noise channels and decoded using message-passing decoders with limited precision, absorbing sets have been shown to be a key factor in error floor behavior. Focusing on this scenario, this paper introduces the cycle consistency matrix (CCM) as a powerful analytical tool for characterizing and avoiding absorbing sets in separable circulant-based (SCB) LDPC codes. SCB codes include a wide variety of regular LDPC codes such as array-based LDPC codes as well as many common quasi-cyclic codes. As a consequence of its cycle structure, each potential absorbing set in an SCB LDPC code has a CCM, and an absorbing set can be present in an SCB LDPC code only if the associated CCM has a nontrivial null space. CCM-based analysis can determine the multiplicity of an absorbing set in an SCB code, and CCM-based constructions avoid certain small absorbing sets completely. While these techniques can be applied to an SCB code of any rate, lower rate SCB codes can usually avoid small absorbing sets because of their higher variable-node degree. This paper focuses attention on the high-rate scenario in which the CCM constructions provide the most benefit. Simulation results demonstrate that under limited-precision decoding the new codes have steeper error-floor slopes and can provide one order of magnitude of improvement in the low-frame-error-rate region.

## Design of Binary and Nonbinary Codes from Lifting of Girth-8 Cycle Codes with Minimum Lengths

- **Status**: ✅
- **Reason**: E: girth-8 cycle code의 최소길이 QC-LDPC 신규 구성(바이너리 부분 이식 가능, 애매하나 in으로 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6459503
- **Type**: journal
- **Published**: April 2013
- **Authors**: Mohammad Gholami, Mehdi Samadieh
- **PDF**: https://ieeexplore.ieee.org/document/6459503
- **Abstract**: -In this paper, some regular and irregular girth-8 cycle codes with arbitrarily high code rates are presented which have minimum lengths among all girth-8 cycle codes having parity-check matrices of the same row regularity. The parity-check matrices of the constructed girth-8 cycle codes can be considered as the mother matrices of some quasi-cyclic (QC) cycle codes with maximum-achievable girth 24 having better rates rather than the girth-24 Geometric and Cylinder-type cycle codes. Simulation results show that the binary and nonbinary constructed cycle codes perform better than the repeat accumulate (RA) codes, progressive edge growth (PEG) codes and random-like LDPC codes of the same lengths and rates.

## Windowed Decoding of Spatially Coupled Codes

- **Status**: ✅
- **Reason**: 공간결합(SC-LDPC) windowed 디코딩: 복잡도/지연 저감 디코더 기법과 SC-LDPC 구성으로 이식 가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6374679
- **Type**: journal
- **Published**: April 2013
- **Authors**: Aravind R. Iyengar, Paul H. Siegel, Rüdiger L. Urbanke +1
- **PDF**: https://ieeexplore.ieee.org/document/6374679
- **Abstract**: Spatially coupled codes have been of interest recently owing to their superior performance over memoryless binary-input channels. The performance is good both asymptotically, since the belief propagation thresholds approach the Shannon limit, as well as for finite lengths, since degree-2 variable nodes that result in high error floors can be completely avoided. However, to realize the promised good performance, one needs large blocklengths. This in turn implies a large latency and decoding complexity. For the memoryless binary erasure channel, we consider the decoding of spatially coupled codes through a windowed decoder that aims to retain many of the attractive features of belief propagation, while trying to reduce complexity further. We characterize the performance of this scheme by defining thresholds on channel erasure rates that guarantee a target erasure rate. We give analytical lower bounds on these thresholds and show that the performance approaches that of belief propagation exponentially fast in the window size. We give numerical results including the thresholds computed using density evolution and the erasure rate curves for finite-length spatially coupled codes.

## Stochastic Belief Propagation: A Low-Complexity Alternative to the Sum-Product Algorithm

- **Status**: ✅
- **Reason**: Stochastic BP: 메시지패싱 복잡도를 quadratic→linear로 줄이는 부호 비의존 BP 변형, 바이너리 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6373728
- **Type**: journal
- **Published**: April 2013
- **Authors**: Nima Noorshams, Martin J. Wainwright
- **PDF**: https://ieeexplore.ieee.org/document/6373728
- **Abstract**: The belief propagation (BP) or sum-product algorithm is a widely used message-passing method for computing marginal distributions in graphical models. At the core of the BP message updates, when applied to a graphical model involving discrete variables with pairwise interactions, lies a matrix-vector product with complexity that is quadratic in the state dimension d, and requires transmission of a (d-1)-dimensional vector of real numbers (messages) to its neighbors. Since various applications involve very large state dimensions, such computation and communication complexities can be prohibitively complex. In this paper, we propose a low-complexity variant of BP, referred to as stochastic belief propagation (SBP). As suggested by the name, it is an adaptively randomized version of the BP message updates in which each node passes randomly chosen information to each of its neighbors. The SBP message updates reduce the computational complexity (per iteration) from quadratic to linear in d, without assuming any particular structure of the potentials, and also reduce the communication complexity significantly, requiring only log2d bits transmission per edge. Moreover, we establish a number of theoretical guarantees for the performance of SBP, showing that it converges almost surely to the BP fixed point for any tree-structured graph, and for any graph with cycles satisfying a contractivity condition. In addition, for these graphical models, we provide nonasymptotic upper bounds on the convergence rate, showing that the l∞ norm of the error vector decays no slower than O (1/√t) with the number of iterations t on trees and the normalized mean-squared error decays as O (1/t) for general graphs. This analysis, also supported by experimental results, shows that SBP can provably yield reductions in computational and communication complexities for various classes of graphical models.

## Rate compatible raptor-like LDPC codes with partially decoder for green terrestrial broadcasting system

- **Status**: ✅
- **Reason**: Raptor-like LDPC partial decoding 조기정지 기법 — 이식 가능 디코더 스케줄링(C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6533315
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Wenfeng Ma, Hui Tian, Yang Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6533315
- **Abstract**: In this paper, a partially decoding scheme, combined with the rate compatible Raptor-like low-density parity-check (LDPC) codes, is proposed to provide more robust, power saving solutions for the future terrestrial broadcasting systems. Different from the existing works, the proposed algorithm uses the least information in the codeword and stops immediately after the decoding is successful. We illustrate two different scenarios under which this scheme will be quite useful. Simulation results show that the proposed scheme is effective.

## A high throughput LDPC decoder in CMMB based on virtual radio

- **Status**: ✅
- **Reason**: Normalized Min-Sum LDPC 디코더 SIMD 병렬화·비트폭/메모리 최적화 — 이식 가능 디코더+HW/병렬화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6533323
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Xia Pan, Xiao-fan Lu, Ming-qi Li +1
- **PDF**: https://ieeexplore.ieee.org/document/6533323
- **Abstract**: LDPC (Low Density Parity Check) is widely used in many telecommunication systems due to its excellent performance. However, real-time LDPC decoder in virtual radio system is difficult to realize. Taking CMMB (China Mobile Multimedia Broadcasting) for instance, this paper proposes a method to achieve high throughput decoder based on x86 processors which support SIMD (Single Instruction Multiple Data) instructions. By utilizing Normalized Min Sum decoding algorithm, normalized parameter as well as bit width of input variables and intermediate variables are determined. Then taking advantages of SIMD instructions, updating progress of variable nodes and check nodes in LDPC decoding algorithm is parallelized. Meanwhile, memory access operations are optimized as well. Tested on Intel Core i7-3960X, the throughput of the LDPC decoder using multithread processing can reach 92Mbps ∼ 722Mbps.

## Locally-optimized reweighted belief propagation for decoding finite-length LDPC codes

- **Status**: ✅
- **Reason**: 유한길이 LDPC용 locally-optimized reweighted BP 디코더 신규 제안, 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6555271
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Jingjing Liu, Rodrigo C. de Lamare, Henk Wymeersch
- **PDF**: https://ieeexplore.ieee.org/document/6555271
- **Abstract**: In practice, LDPC codes are decoded using message passing methods. These methods offer good performance but tend to converge slowly and sometimes fail to converge and to decode the desired codewords correctly. Recently, tree-reweighted message passing methods have been modified to improve the convergence speed at little or no additional complexity cost. This paper extends this line of work and proposes a new class of locally optimized reweighting strategies, which are suitable for both regular and irregular LDPC codes. The proposed decoding algorithm first splits the factor graph into subgraphs and subsequently performs a local optimization of reweighting parameters. Simulations show that the proposed decoding algorithm significantly outperforms the standard message passing and existing reweighting techniques.

## Analysis of voltage- and clock-scaling-induced timing errors in stochastic LDPC decoders

- **Status**: ✅
- **Reason**: stochastic LDPC 디코더의 전압/클럭 스케일링 타이밍 오류 내성·에너지 분석으로 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6555268
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Isaac Perez-Andrade, Xin Zuo, Robert G. Maunder +2
- **PDF**: https://ieeexplore.ieee.org/document/6555268
- **Abstract**: Low Density Parity Check (LDPC) decoders have an inherent capability of correcting the transmission errors that occur, when communicating over a hostile wireless channel. This capability allows LDPC-coded schemes to employ lower transmission energies than uncoded schemes, at the cost of introducing a significant processing energy consumption during LDPC decoding. Traditional energy-reduction techniques, such as voltage and clock scaling can be employed for reducing the LDPC decoder's energy consumption. However, these techniques may induce timing errors, which can degrade the LDPC decoder's error correction capability. Our previous work has demonstrated that in contrast to other types of LDPC decoders, stochastic decoders have an inherent tolerance to timing errors, allowing them to maintain a high error correction capability in clockscaling scenarios. In this paper, we investigate this timing error tolerance in voltage-scaling scenarios, by extending our previous model of timing errors using extensive SPICE simulations. Furthermore, we use these SPICE simulations to characterize the processing energy consumption of stochastic LDPC decoders for the first time. We demonstrate that a modified stochastic LDPC decoder can operate at 0.8 V and a clock period of 915.11 ps, while maintaining the error correction capability of a conventional stochastic decoder operating at 1 V and a clock period of 1019.2 ps, offering a 36.7% reduction in processing energy consumption.

## Good coupling between LDPC-staircase and Reed-Solomon for the design of GLDPC codes for the erasure channel

- **Status**: ✅
- **Reason**: GLDPC-staircase 코드설계(DE/EXIT/유한길이 분석), 바이너리 base — 애매하여 Phase3 재검토(RS-component+erasure 의존성 확인 필요)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6554790
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Ferdaouss Mattoussi, Bessem Sayadi, Vincent Roca
- **PDF**: https://ieeexplore.ieee.org/document/6554790
- **Abstract**: In this paper we analyze the design of Generalized LDPC-staircase (GLDPC-staircase) codes, where the base code is an LDPC-Staircase code and component codes are Reed-Solomon codes. More precisely we compare two schemes: scheme A has the property that on each check node of the base code the repair symbol generated by the LDPC code is also a Reed-Solomon repair symbol. On the opposite, with scheme B for each check node the repair symbols generated by the LDPC code are Reed-Solomon source symbols. In this work we perform a behavioral analysis of the two schemes in order to determine the best one for ITerative + Reed Solomon (IT+RS) and Maximum Likelihood (ML) decoding. To that purpose we use an asymptotic analysis using Density evolution (DE) and EXtrinsic Information Transfer techniques, as well as a finite length analysis. We show that scheme A is globally the best solution since it significantly performs better than scheme B with an (IT+RS) decoding and yields similar performance with ML decoding.

## BICM performance improvement via online LLR optimization

- **Status**: ✅
- **Reason**: 온라인 LLR 스케일링(GMI 최대화) — LLR 양자화/스케일링 기법으로 NAND ECC 이식 가능성, 애매하여 Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6555189
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Jinhong Wu, Mostafa El-Khamy, Jungwon Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6555189
- **Abstract**: We consider bit interleaved coded modulation (BICM) receiver performance improvement based on the concept of generalized mutual information (GMI). Increasing achievable rates of BICM receiver with GMI maximization by proper scaling of the log likelihood ratio (LLR) is investigated. While it has been shown in the literature that look-up table based LLR scaling functions matched to each specific transmission scenario may provide close to optimal solutions, this method is difficult to adapt to time-varying channel conditions. To solve this problem, an online adaptive scaling factor searching algorithm is developed. Uniform scaling factors are applied to LLRs from different bit channels of each data frame by maximizing an approximate GMI that characterizes the transmission conditions of current data frame. Numerical analysis on effective achievable rates as well as link level simulation of realistic mobile transmission scenarios indicate that the proposed method is simple yet effective.

## An efficient LDPC encoding scheme for CMMB based on improved LU decomposition

- **Status**: ✅
- **Reason**: 개선 LU분해 기반 LDPC 인코딩(행·열 치환으로 저밀도 삼각화, 선형복잡도, HW절감) — 이식 가능 인코딩 기법(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6617525
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Guoche Qin, Ming Yan, Guorong Hu
- **PDF**: https://ieeexplore.ieee.org/document/6617525
- **Abstract**: Low-density parity-check (LDPC) codes are widely applied in modern communication system for its capability of approaching channel capacity at low complexity. We design an efficient encoding scheme based on LU decomposition for China mobile multimedia broadcasting (CMMB). We search for element with lightest row-multiplying-column weight from the k th row and k th column, and exchange it with diagonal element of k th row. Then we operate Gaussian elimination to generate triangular matrices. We improve classic LU decomposition by performing both row and column permutations to obtain triangular matrices with lower density and demonstrate procedure of the improved algorithm. Encoding complexity of the proposed method is linear in codeword length with small coefficient. We show that the proposed method can significantly reduce computing operation and cost no extra hardware.

## Performance analysis of spatially coupled codes over the correlated erasure channel

- **Status**: ✅
- **Reason**: SC-LDPC + sliding window decoding over burst erasure channel, convolutional interleaver로 디코더 성능 개선 — 바이너리 LDPC 코드설계/디코더 기법(E/C), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6531268
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Reza A. Ashrafi, Ali E. Pusane
- **PDF**: https://ieeexplore.ieee.org/document/6531268
- **Abstract**: Desirable characteristics of spatially-coupled low-density parity-check (LDPC) codes including low implementation complexity, low-delay, and close-to-optimal performance over a wide variety of channels make them a noticeable candidate for the next-generation wireless communication standards. However, error performance of the sliding window decoding scheme used to decode these codes is considerably degraded over channels with memory, such as the burst erasure channel. Traditionally, communication over channels with memory is achieved through the use of block interleavers but as it introduces a large amount of delay, it is not always a viable option. In this paper, employing a convolutional interleaver which benefits from the inherent convolutional nature of the spatially-coupled codes with very low overall delay is considered. The performance of the proposed combination is analyzed using the density evolution technique. The performance improvement of using a convolutional inter-leaver is demonstrated as a function of the added interleaving delay in terms of iterative decoding thresholds.

## Field-programmable gate array implementation of low-density parity-check codes decoder and hardware testbed

- **Status**: ✅
- **Reason**: WiMAX 802.16e용 LDPC 디코더 FPGA 구현, 떼어낼 수 있는 HW 아키텍처 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6584426
- **Type**: conference
- **Published**: 17-19 Apri
- **Authors**: Jutaphet Wetcharungsri, Narong Buabthong, Sakdinan Jantarachote +2
- **PDF**: https://ieeexplore.ieee.org/document/6584426
- **Abstract**: The prototyping design of the channel coding in communication systems such as IEEE 802.16e (WiMAX) has become more sophisticated because of the increasing need for interoperability. Understanding its performance in the design and implementation of forward error correction codes in a real-time manner is necessary for rapid prototyping in research areas that are primarily based on emulation and stand-alone tests. This paper presents the design, implementation, experimental verification, and validation of the proposed LDPC decoder using a real-time FPGA based baseband test. The design of the LDPC decoder is described. In addition, a description of the hardware components that covers the important parts of the system from RF to channel decoding is included. The overall architecture of the baseband digital signal processing is simply illustrated, and details of the data acquisition module are provided. On the implementation and testing results, the throughput and latency at all the code rates specified in IEEE 802.16e are shown. Furthermore, the results for the architectural complexity and performance in terms of the bit error rates over the testbed show that the proposed flexible design for IEEE 802.16e exhibits potential under a practical environment.

## Simulation and implementation of LDPC code in FPGA

- **Status**: ✅
- **Reason**: 바이너리 LDPC bit-flipping 디코더의 FPGA(Virtex5) 구현, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6530944
- **Type**: conference
- **Published**: 16-17 Apri
- **Authors**: Pavel Straus, Zdenek Kolka
- **PDF**: https://ieeexplore.ieee.org/document/6530944
- **Abstract**: The paper deals with implementation of Low-Density Parity-Check (LDPC) codes [1] in FPGA-based bridge for Free-Space Optical link. The coder was designed with a regular parity matrix for code rate 1/2. The matrix of dimension 8×16 for the experimental implementation was found using a random search in MATLAB. The main advantage of this matrix is the decoder can correct all single-bit errors. The simulation for all possible values shows that Bit Error Ratio (BER) is zero. This result was not obtained with other matrices. An experimental communication channel was realized with encoder and decoder implemented in FPGA Virtex 5 development board ML505. DIP switches are sources for information bits and these values are shown on LCD display. The bit-flipping method is used in decoder and result code word is shown in the second line on the LCD display.

## Error-prediction analyses in 1X, 2X and 3Xnm NAND flash memories for system-level reliability improvement of solid-state drives (SSDs)

- **Status**: ✅
- **Reason**: NAND 플래시 직접(A) - EP-LDPC와 1X/2X/3Xnm NAND 신뢰성 정보, SSD ECC 적용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6531979
- **Type**: conference
- **Published**: 14-18 Apri
- **Authors**: Shuhei Tanakamaru, Masafumi Doi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6531979
- **Abstract**: The system-level reliability of solid-state drives (SSDs) is investigated with 1X, 2X and 3Xnm NAND flash memories. The reliability degradation of NAND with scaling is an serious issue. Advanced ECC with signal processing such as error-prediction low-density parity-check (EP-LDPC) and error recovery (ER) scheme will be needed in the future SSDs. In this paper, the NAND reliability information used for EP-LDPC and ER is examined. System-level reliability with conventional ECC and EP-LDPC is measured.
