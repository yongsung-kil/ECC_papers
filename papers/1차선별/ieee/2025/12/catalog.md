# IEEE Xplore — 2025-12 (1차선별 통과)


## VN-Based Tail-Biting Globally-Coupled LDPC Codes

- **Status**: ✅
- **Reason**: VN 기반 TB-GC-LDPC 신규 코드 클래스; girth·degree distribution 최적화(E) + merry-go-round 디코딩 스킴(C) + HW 복잡도 감소(D), NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11184547
- **Type**: journal
- **Published**: Dec. 2025
- **Authors**: Hao Liu, Qi-Yue Yu
- **PDF**: https://ieeexplore.ieee.org/document/11184547
- **Abstract**: In this paper, we propose a new class of globally-coupled low-density parity-check (GC-LDPC) codes, referred to as variable node (VN) based tail-biting (TB) GC-LDPC codes. Unlike conventional check node (CN) based GC-LDPC codes, which rely on the global CNs for coupling, the proposed codes employ global VNs for the coupling with a TB structure. The innovative coupling structure not only eliminates the rate loss problem inherent in CN-based GC-LDPC codes but also provides greater flexibility in adjusting the degree distribution. Moreover, the TB structure can significantly reduce the hardware complexity of the encoder and decoder of the VN-based TB-GC-LDPC code, making them more practical for implementation. To construct the VN-based TB-GC-LDPC codes, we present two methods based on optimizing girth and degree distributions, respectively. In addition, we introduce the low-complexity encoding scheme and decoding scheme tailored to the special structure of the VN-based TB-GC-LDPC codes. Specifically, the proposed merry-go-round (MGR) component-code-based (CCB) decoding scheme can achieve the global coding gain of the time-invariant VN-based TB-GC-LDPC codes. Simulation results demonstrate that the proposed codes not only outperform existing CN-based GC-LDPC codes but also achieve comparable performance to advanced LDPC codes, such as 5G-LDPC codes, while requiring lower hardware implementation complexity.

## Iteration and SDA-Driven LDPC Decoding Latency Reduction for 3-D TLC NAND Flash Memory

- **Status**: ✅
- **Reason**: 3D TLC NAND에서 LDPC 반복 횟수 및 SDA를 활용한 디코딩 지연 최적화 기법 제안 — NAND LDPC 디코더 알고리즘 직접 적용(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11017681
- **Type**: journal
- **Published**: Dec. 2025
- **Authors**: Debao Wei, Yongchao Wang, Dejun Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/11017681
- **Abstract**: To enhance the reliability of 3-D TLC NAND flash memory, low-density parity-check (LDPC) codes have become widely adopted. However, as the number of read, program or erasures increases, the raw bit error rate (RBER) of read data in flash memory chips also rises, leading to the challenge of increased LDPC decoding latency. To address this, an idea of utilizing the decoding correct probability of LDPC to reduce latency is proposed. First, by analyzing the encoding method of TLC NAND flash memory, a single direction characterization error model based on the correlation between individual pages is constructed. Next, through experimental validation, the feasibility of using the number of iterations as an indicator of decoding correct probability is demonstrated, leading to the proposal of a low-overhead and high-performance Iterative Alternative Correct Probability Optimization (IACPO) scheme. Leveraging the fact that LDPC decoding exhibits a high success probability within a specific range of read data, the existence of successful decoding area (SDA) is confirmed through a large number of real experiments, and the distribution characteristics of SDA in TLC NAND flash memory are analyzed. Finally, the Utilizing LDPC Decoding Correct-Probability Optimization (ULDCO) scheme to further optimize latency is proposed. This scheme uses SDA to improve the probability of correct data reading, particularly in the middle and later stages of flash memory life, in combination with the IACPO scheme. Experimental results show that the proposed IACPO and ULDCO schemes are not only generally applicable but also achieve significantly iterative latency reduction by 73.43% and 81.51%, respectively, compared to traditional schemes, with negligible storage and computation overhead. These results clearly demonstrate the superior performance of the proposed schemes in reducing iteration latency.

## FPGA-Based Implementation of Single-Cycle High-Throughput LDPC Encoder for 5G New Radio

- **Status**: ✅
- **Reason**: QC-LDPC 인코더 FPGA 구현, 단일 클럭 사이클 완전 조합회로 설계 — LDPC HW 아키텍처 직접 이식 가능 (D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10906520
- **Type**: journal
- **Published**: Dec. 2025
- **Authors**: A. Sharma, G. Purohit, A. R. Asati
- **PDF**: https://ieeexplore.ieee.org/document/10906520
- **Abstract**: This letter presents a novel architecture for a high-throughput encoder for quasi-cyclic low-density parity-check codes. This low-complexity encoder is specifically tailored for the 5th generation (5G) new radio (NR) standard. To achieve high throughput, we employ an automated approach to design customized encoders for individual base graphs using a Verilog Code Generator (VeCoGen) that we developed in MATLAB. Our proposed architecture improves efficiency by rearranging the wire indices during the hardware design language code generation stage itself, instead of performing shifting operations on the data carried by those wires on the fly. This eliminates the need for RAM (for storing base graph coefficients) and dedicated barrel shifters. The parity bits are computed in parallel, while maintaining optimal performance and gate count through effective exploitation of the base graph’s sparsity. Consequently, the encoder can be designed as a fully combinational circuit between the input and output registers, enabling the generation of the complete codeword within a single clock cycle. This results in exceptionally high throughput, optimal hardware utilization, and minimal number of xor operations, making our approach highly effective for 5G NR applications.

## Adaptive Read Level Recording for Read Performance Improvement in 3-D NAND Flash

- **Status**: ✅
- **Reason**: 3D NAND 플래시에서 LDPC read-retry 지연을 줄이기 위한 적응형 read-level 기록 기법 — NAND LDPC ECC 직접 적용(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10994566
- **Type**: journal
- **Published**: Dec. 2025
- **Authors**: Shiqiang Nie, ZhiKe Li, Fangxing Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/10994566
- **Abstract**: While low-density parity-check code has been adopted in 3-D flash for improving chip reliability, it suffers from severe read latency due to the increasing number of read retries. Recent studies propose read-level recording to mitigate the performance loss from failed read retries. However, existing schemes induce large updating overhead and achieve suboptimal results, making it critical to develop better tradeoffs among storage overhead, process variation, and performance improvement. In this article, we propose AR$^{2}$, an adaptive read-level recording scheme to improve read performance for 3-D NOT AND (NAND) flash. It consists of two designs: AR$^{2}$-win and AR$^{2}$-pre. AR$^{2}$-win records the number of read levels that fit the majority of the last $N$ reads, which prevents the worst page from dominating the read level recording. AR$^{2}$-pre predicts the number of read levels for the next read based on the recorded one and a simple machine learning model, which prevents using stale recorded levels in large-capacity solid-state drives (SSDs). Our experimental results show that AR$^{2}$ significantly improves the read performance for 3-D NAND flash and achieves on average 15% or more read latency reduction over the state-of-the-art.

## LDPC Code Optimisation for OTFS Modulation with MP Detection

- **Status**: ✅
- **Reason**: EXIT 분석 기반 LDPC 코드 설계 임계값 계산 알고리즘 제안 — 무선 OTFS 특화이나 코드 설계 방법론(E) 자체는 NAND LDPC 설계에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11431745
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Chong Zhang, Shenghui Song, Chi-Ying Tsui +1
- **PDF**: https://ieeexplore.ieee.org/document/11431745
- **Abstract**: The orthogonal time frequency space (OTFS) modulation is a promising technique to provide reliable communications in high-mobility scenarios. However, the performance analysis for coded OTFS systems is not available in the literature. This paper investigates the extrinsic information transfer (EXIT) behaviour of LDPC coded OTFS systems with message passing (MP) detection. Different from conventional EXIT analysis, which is normally obtained by Monte Carlo simulation, the exact distribution of the extrinsic information for MP detection is presented in this paper. Then, the EXIT function for the LDPC decoder is given with the prior information of the MP detector, which illustrates the convergence behaviour of the LDPC coded OTFS systems. Finally, an algorithm is proposed for calculating the decoding threshold for LDPC coded OTFS modulation, which can be used to design LDPC codes for OTFS systems. Numerical results verify the accuracy of the EXIT analysis, and the 5G NR LDPC code optimised by the proposed method demonstrates 1 dB to 1.5 dB performance gains over the original codes.

## Quasi-Cyclic LDPC Codes from Generalized Behrend Sequences for Space Applications

- **Status**: ✅
- **Reason**: 임의 column weight·girth 8 이상 QC-LDPC 신규 구성법 제안, HW 구현 적합성 확인 — 코드 설계 기법(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432165
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Suresh Kumar Venkataramanappa, Pavan Kumar, Deepak Mishra +1
- **PDF**: https://ieeexplore.ieee.org/document/11432165
- **Abstract**: We present a novel construction of quasi-cyclic (QC) low-density parity-check (LDPC) codes with arbitrary column weight and girth at least eight. By carefully designing the parity-check matrix, our approach ensures both structural flexibility and improved error-correction capabilities. We evaluate the performance of these codes under the additive white Gaussian noise (AWGN) channel. Simulation results demonstrate that the proposed QC-LDPC codes outperform the protograph LDPC codes included in the Consultative Committee for Space Data Systems (CCSDS) telecommand standards. Additionally, we benchmark our proposed codes against existing short-length codes with girth 8, observing improvements in the decoding performance while ensuring suitability for hardware implementation. The findings of this work contribute to the ongoing development of efficient LDPC codes suitable for ultra-reliable low-latency communications and area-efficient architecture designs for the Internet of Things (IoT), machine-to-machine (M2M), and satellite communications.

## Early Decoding with Globally Coupled LDPC Codes in Heterogeneous NOMA

- **Status**: ✅
- **Reason**: Partially globally coupled LDPC 코드 구조 및 조기 디코딩 알고리즘 설계 — 코드 구조(E)와 디코더 알고리즘(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432476
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Tai-Hsun Chen, Min Qiu, Yu-Chih Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/11432476
- **Abstract**: In this paper, we propose a new coding scheme and decoding algorithms tailored for the coexistence of heterogeneous services with different blocklength and latency requirements in downlink. In such scenarios, early decoding—allowing the receiver to decode messages without receiving the entire transmission frame—is leveraged to perform low-latency multiuser interference cancellation. To facilitate such a decoding scheme with practical channel codes, we design partially globally coupled low-density parity-check (LDPC) codes that enable early decoding of local codes while maintaining connections among them, allowing local decoding processes to support each other for improved overall reliability. In addition, we put forth early decoding based successive interference cancellation (SIC), where the proposed code only requires a portion of the parity-check matrix for decoding. Simulation results show that our proposed design can achieve a 2.4 dB performance gain over 5G NR LDPC codes when using less than one-quarter of the coded symbols for SIC, highlighting its effectiveness in early decoding scenarios. This offers a practical and flexible solution for supporting heterogeneous service coexistence in future wireless systems.

## In-Memory Noise Estimation using LDPC Codes for Reliable Edge Matrix-Vector Multiplication

- **Status**: ✅
- **Reason**: 아날로그 인메모리 연산용이나 bilayer LDPC 설계·차수분포·analog syndrome 등 코드설계 기법(E) 포함 — 애매하여 살림(Phase 3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432726
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Yotam Gershon, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/11432726
- **Abstract**: Reliable matrix-vector multiplication (MVM) in edge devices is a key enabler for modern computational tasks such as AI inference. Novel memory technologies, such as MRAMs, enable highly efficient analog computation of MVM. While significantly improving speed and power consumption, these architectures suffer from reduced reliability. We introduce a coding scheme in which the parity constraints of the code are employed toward in-memory noise estimation, in addition to their traditional role of error correction. Our scheme relies on objects we call analog syndromes, which on one hand can be efficiently computed in memory, and on the other hand are shown analytically to provide more accurate estimation than classical logical syndromes. The scheme utilizes a previously introduced bilayer LDPC design with sub-block locality, and describes how to design the degree distributions.

## GLDPC Codes Based on Polar Constraints and Their Near-Optimal Decoding

- **Status**: ✅
- **Reason**: Polar component를 활용한 GLDPC 코드 구성 + SISO BP 디코더, error floor 개선 명시 — 디코더 알고리즘(C)·코드 설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432491
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Binghui Shi, Yongpeng Wu, Yin Xu +3
- **PDF**: https://ieeexplore.ieee.org/document/11432491
- **Abstract**: In this work, we introduce the integration of generalized low-density parity-check (GLDPC) codes with short polar component codes, termed GLDPC codes with polar component codes (GLDPC-PC). A recently proposed soft-input soft-output (SISO) decoder for polar-like codes enables effective iterative belief propagation decoding for GLDPC-PC. This SISO decoder after a post-processing exhibits little performance loss to the optimal SISO decoder when all the variable nodes have relatively low degrees. A three-step method is introduced to design protograph-based GLDPC codes. The constructed GLDPC codes are compared with 5G LDPC codes. They exhibit little performance loss in the waterfall region and possess better error floor with less iterations.

## End-to-end Neural-Classical Concatenated Feedback Coding with OFDM Guidance

- **Status**: ✅
- **Reason**: 미분가능 SPA를 훈련 루프에 포함한 신경망 디코더 기법(C) — LDPC 외부 코드 + 신경망 내부 인코더 결합, 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432731
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Adnan Can Buyuksirin, Hun-Seok Kim
- **PDF**: https://ieeexplore.ieee.org/document/11432731
- **Abstract**: In this paper, we propose an end-to-end (E2E) optimized concatenated feedback coding scheme that combines a neural inner encoder/decoder with a classical low-density parity-check (LDPC) outer code for reliable feedback-based communication over multipath fading channels. A key contribution of this work is the inclusion of the LDPC decoder within the training loop by exploiting the differentiability of the sum-product algorithm (SPA), allowing gradient-based optimization to flow across the entire feedback-based communication chain. To enhance robustness over multipath fading channels, we integrate orthogonal frequency-division multiplexing (OFDM) guidance as well as the bit-interleaved coded modulation (BICM) paradigm into the proposed concatenated feedback coding approach. The proposed framework supports practical blocklengths and fading scenarios, significantly outperforming both fully neural and non-E2E concatenated baselines.

## Reduced-Complexity Guessing Codeword Decoding of BCH Codes with Most Reliable Cyclic Basis

- **Status**: ✅
- **Reason**: BCH용 GCD(Guessing Codeword Decoding) 개선 알고리즘 — OSD 계열 디코더로 LDPC에도 적용 가능한 유한 길이 ML 디코딩 기법(C), Phase 3 재검토 권장
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11432585
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Yiwen Wang, Qianfan Wang, Xiangping Zheng +2
- **PDF**: https://ieeexplore.ieee.org/document/11432585
- **Abstract**: This paper proposes an enhanced guessing codeword decoding (GCD) algorithm, termed GCD with most reliable cyclic basis (MRCB-GCD), specifically tailored for BCH codes. Unlike original GCD, the proposed method selects the k consecutive bits with the highest aggregate reliability as the re-encoding basis, leveraging the cyclic structure of BCH codes. To further enhance search efficiency, a local constraint (LC) mechanism is introduced, where the extended reliable bits of length k+δ enable the algorithm to skip numerous unnecessary test error patterns (TEPs). To stop the search process, we introduce two termination criteria and prove that the proposed approach with the trivial termination criterion forms a non-exhaustive-search maximum likelihood (ML) decoding algorithm. A saddlepoint-based numerical method is developed to approximately calculate the upper bound on the performance gap to the ML decoding and estimate the average number of searches, showing the advantages of the proposed MRCB-GCD over the original GCD in terms of both decoding performance and search efficiency. Simulation results demonstrate that: 1) MRCB- GCD outperforms original GCD in both frame error rate (FER) and number of searches, 2) the LC mechanism and termination criteria further reduce the number of searches, and 3) the proposed approach achieves finite-length capacity across various code rates but without requiring Gaussian elimination.

## CMOS Physics-Inspired Architectures and Circuits for Combinatorial Optimization Solvers

- **Status**: ✅
- **Reason**: 커플드 완화진동기 기반 물리영감 CMOS 아키텍처로 LDPC 디코더를 구현 — 병렬 HW 디코더 아키텍처(D)로 NAND ECC에 이식 가능성 있음.
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11353785
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: M. P. Flynn, E. Dikopoulos, L. Wormald +4
- **PDF**: https://ieeexplore.ieee.org/document/11353785
- **Abstract**: Recently, physics-inspired computing platforms have shown significant potential in accelerating the solution of combinatorial optimization problems (COPs) by leveraging continuous-time (CT) operation, massive parallelism, and direct mapping to coupled CMOS-based spins, often realized with oscillators. These systems leverage the natural dynamics of coupled oscillators to rapidly converge to COP solutions, resulting in substantial improvements in solution time and energy. This work introduces physics-inspired computing, outlines its advantages, and presents a framework for mapping complex COPs to coupled relaxation-oscillator spins. We demonstrate this approach with two custom solver systems, a direct 3-SAT engine and an LDPC decoder.

## A Survey on the Theoretical Evolution and Algorithmic Innovation of Reed-Solomon Codes

- **Status**: ✅
- **Reason**: RS 부호 디코딩 알고리즘 서베이지만 RS-LDPC 확률적 결합 디코딩·소프트정보 통합 등 이식 가능 디코더 기법 다룸(C), 애매하므로 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11414954
- **Type**: conference
- **Published**: 26-28 Dec.
- **Authors**: Jiahao Wang, Yi Liu
- **PDF**: https://ieeexplore.ieee.org/document/11414954
- **Abstract**: As a classic Maximum Distance Separable code, Reed-Solomon (RS) codes have been an indispensable core technical support in digital communication, data storage and deep space exploration since their proposal in 1960, thanks to their optimal algebraic error-correcting performance and flexible construction. This paper systematically sorts out the theoretical evolution and algorithmic innovation of RS codes: starting from finite field algebra foundations and two classical constructions—one based on evaluation mapping and the other as a special case of BCH codes—it analyzes three key breakthroughs in decoding theory. Classical algebraic decoding including the PGZ, Berlekamp-Massey and Euclidean algorithms lays the foundation for engineering applications, Guruswami-Sudan list decoding breaks the half-minimum distance limit, and the Kotter-Vardy algorithm integrates soft information with algebraic decoding. The paper focuses on cutting-edge progress from 2021 to 2025, covering efficient algorithms such as FFT-based fast joint decoding, symbol-level iterative information set decoding and tree-based Chase-type soft-decision decoding, as well as engineering breakthroughs including domestic FPGA-adapted low-resource encoders/decoders and RS-LDPC probabilistic joint decoding. Finally, it summarizes challenges such as complexity-performance balance, emerging coding competition and probabilistic decoding framework construction, and prospects future directions including AI integration, extreme scenario optimization and deepened domestic adaptation, aiming to provide a comprehensive technical landscape for researchers and engineers.

## Dynamic Scheduling Decoding Algorithms for LDPC Codes in Evaporation Duct Environments

- **Status**: ✅
- **Reason**: 새 디코더 NWRBP(residual 기반 동적 스케줄링 BP) 제안 — 도메인 무관 바이너리 LDPC 디코더로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11414551
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Long Chen, Peng Yu, Longzhi Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/11414551
- **Abstract**: Reliable over-the-horizon (OTH) communication is pivotal for modern naval operations and commercial shipping, yet it is severely hindered by the complex propagation characteristics of evaporation duct channels. These channels exhibit time-varying composite fading - combining log-normal and Rayleigh distributions - and suffer from strong non-Gaussian impulsive interference generated by maritime radar systems. To mitigate these challenges, this paper investigates the performance of Low-Density Parity-Check (LDPC) codes and proposes a novel Node-Weighted Residual Belief Propagation (NWRBP) decoding algorithm. First, we establish a statistical channel model validated by experimental data collected from the South China Sea to ensure simulation fidelity. Subsequently, we introduce the NWRBP algorithm, which dynamically schedules message updates based on residual magnitudes to prevent error propagation typical of static flooding schedules under impulsive noise. Comprehensive simulations demonstrate that NWRBP significantly outperforms both the standard Belief Propagation (BP) algorithm and state-of-the-art Polar codes with Successive Cancellation List (SCL) decoding. Specifically, under strong attenuation conditions, the proposed scheme achieves a coding gain of up to 2.3 dB over BP and 0.8 dB over Polar codes, while reducing average decoding latency by approximately 35%. These findings confirm that dynamic scheduling offers a robust, low-latency solution for critical maritime data links in hostile electromagnetic environments.

## Design and Implementation of CODEC for CCSDS Defined LDPC code for Deep Space Communication

- **Status**: ✅
- **Reason**: CCSDS LDPC용 Min-Sum 완전병렬 FPGA 디코더 HW 구현 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11452816
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Rajagopalan Alias Sabarinathan P, Pradeesh Madhavan, Satish Sharma +3
- **PDF**: https://ieeexplore.ieee.org/document/11452816
- **Abstract**: This paper presents the hardware implementation of Min-Sum based decoder for CCSDS defined LDPC code for deep space communication link. The implementation includes encoder and decoder. The encoder design involves matrix multiplication of input message vector and the Generator matrix. The decoder is a fully parallel architecture controlled by a Finite State Machine for running the algorithm iteratively. The implementation is done in Kintex Ultra scale FPGA. The encoder output is verified by checking the syndrome. The decoder is evaluated by interfacing with the S-band soft decision digital receiver wherein the data to the receiver is from designed encoder. The coding gain achieved for the decoder as a part of decoder evaluation is 5.2 dB

## Quasi-Cyclic Gradient Learning: A Method to Improve Performance of 5G QC-LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC를 gradient descent로 최적화하는 새 코드설계 기법 - 바이너리 QC-LDPC 구성 개선(E)으로 NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11314138
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Emmanuelle Bodji, Emmanuel Boutillon, Bruno Jahan +1
- **PDF**: https://ieeexplore.ieee.org/document/11314138
- **Abstract**: The use of neural networks is advancing across several fields, particularly in digital communications. However, in the domain of error-correcting codes, the prevailing consensus is that Artificial Intelligence (AI) tools can, at best, match the performance of existing methods without offering any significant simplifications or improvements. As a result, the initial enthusiasm for AI-based approaches in this area has substantially declined. Recently, however, it has been demonstrated that gradient descent can be used to guide the optimization process for the code construction of unstructured Low-Density Parity-Check (LDPC) codes. In this paper, we extend and generalize this method to also optimize Quasi-Cyclic LDPC codes (QC-LDPC). More specifically, we propose to apply the new method directly to the base protograph structures of QC-LDPC codes standardized in the fifth generation (5G) New Radio (NR) framework. Experimental results reveal that, for small protograph matrices, the proposed optimization process achieves significant coding gains, with improvements of up to 1.2 dB in signal-to-noise ratio (SNR) at a target frame error rate (FER) of 10−2.

## Efficient Noisy Gradient Descent Bit-Flipping Algorithm for Decoding LDPC Codes

- **Status**: ✅
- **Reason**: 효율적 NGDBF(노이즈 GDBF) 비트플리핑 LDPC 디코더, SNR 추정·스케일링 불필요한 새 디코더로 NAND 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11437873
- **Type**: conference
- **Published**: 12-15 Dec.
- **Authors**: Kaiyang Peng, Jie Peng, Haiyang Liu
- **PDF**: https://ieeexplore.ieee.org/document/11437873
- **Abstract**: In this paper, we propose an efficient noisy gradient descent bit-flipping (NGDBF) algorithm for decoding LDPC codes. The proposed algorithm introduces random noise with uniform distribution on the interval $[-1,1]$ into the inversion function of the GDBF algorithm. The proposed algorithm avoids the complicated operations in the noise generation of the conventional NGDBF algorithm. In addition, our proposed decoding algorithm does not rely on the SNR estimation and the scaling factor. Simulation results indicate that the proposed algorithm can achieve almost the same performance as the conventional NGDBF algorithm. Moreover, even the using of a linear feedback shift register with very small stage can generate sufficient randomness to reach such performance.

## An FPGA-Based LDPC Decoder for Smart-NICs

- **Status**: ✅
- **Reason**: FPGA 기반 LDPC 디코더 HW 아키텍처(다중 base graph, 가변 lifting, dual-clock); D 카테고리 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11302660
- **Type**: conference
- **Published**: 1-3 Dec. 2
- **Authors**: Hassan Chreif, Lounis Zerioul, Julio C. Pérez-García +2
- **PDF**: https://ieeexplore.ieee.org/document/11302660
- **Abstract**: Low-Density Parity-Check (LDPC) codes are a key component of modern wireless standards. Most FPGA-based implementations emphasize decoding performance while overlooking system-level concerns such as network integration and autonomous operation. This paper introduces a configurable FPGA-based LDPC decoder with an integrated UDP/Ethernet stack, enabling direct offloading in real 5G New Radio (NR) deployments for 5G access networks equipped with FPGA-based smart-network interface cards (Smart-NICs). The architecture supports multiple base graphs, variable lifting sizes, and diverse code rates through parameter-driven synthesis, while a dual-clock design ensures reliable timing across heterogeneous interfaces. Implemented on the NetFPGA-SUME platform, the proposed decoder achieves efficient resource utilization (15.09% of FPGA resources), a sustained throughput of $181.51 \text{Mbps}$, and an end-to-end decoding latency of 423.1 microseconds. Experimental evaluation further reports a bit error rate of $4.688 \times 10^{-5}$ at 6 dB of $E_{b} / N_{0}$, confirming good performance and deployment readiness.
