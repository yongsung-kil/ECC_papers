# IEEE Xplore — 2017-09 (1차선별 통과)


## Lower Bounds on the Size of Smallest Elementary and Non-Elementary Trapping Sets in Variable-Regular LDPC Codes

- **Status**: ✅
- **Reason**: variable-regular LDPC trapping set 크기 하한 - error floor 코드설계(E) 관련, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7935340
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Yoones Hashemi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/7935340
- **Abstract**: Trapping sets are known to be the main cause for the error floor of low-density parity-check (LDPC) codes. They are often classified by their size a and the number of unsatisfied check nodes b in their subgraph. Trapping sets can be partitioned into two categories of elementary and non-elementary, where the first category are those whose subgraph only contains degree-1 and degree-2 check nodes. Empirical results have shown that often the most harmful trapping sets are elementary. In this letter, we derive a lower bound on the size of the smallest non-elementary trapping sets for a given b in variable-regular LDPC codes. The derived lower bound demonstrates that the size of the smallest possible non-elementary trapping set is, in general, larger than that of an elementary trapping set with the same b value. This provides a theoretical justification as to why non-elementary trapping sets are often not among the most harmful trapping sets.

## A Parity Structure for Scalable QC-LDPC Codes With All Nodes of Degree Three

- **Status**: ✅
- **Reason**: degree-3 QC-LDPC BTD 패리티 구조, error floor 개선·저복잡도 인코딩 신규 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7938596
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Xiaoning Wu, Ming Jiang, Chunming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/7938596
- **Abstract**: A novel block triple-diagonal (BTD) parity structure with all nodes of degree three is proposed for quasi-cyclic (QC) low-density parity-check (LDPC) codes. The BTD structure without low node degree can effectively improve the error floor performance and, meanwhile, enable low complexity encoding. With this structure, we use a modulo-lifting technology to construct a family of QC-LDPC codes, which supports scalable code lengths with a simple and flexible encoding solution. The simulation results show that our coding schemes for short and moderate lengths achieve better performance in the error floor region.

## Analysis of Saturated Belief Propagation Decoding of Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: LLR saturation이 BP 디코딩/error-floor에 미치는 영향 분석, 바이너리 LDPC LLR 양자화에 직접 관련(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7968384
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Shrinivas Kudekar, Tom Richardson, Aravind R. Iyengar
- **PDF**: https://ieeexplore.ieee.org/document/7968384
- **Abstract**: We consider the effect of log-likelihood ratio saturation on the belief-propagation decoding of low-density parity-check codes. Saturation is commonly done in practice and is known to have a significant effect on the error-floor performance. Our focus is on threshold analysis and the stability of density evolution. We analyze the decoder for standard low-density parity-check code ensembles and show that belief-propagation decoding generally degrades gracefully with saturation. Stability of density evolution is, on the other hand, rather strongly affected by saturation, and the asymptotic qualitative effect of saturation is similar to reduction by one of variable-node degree. We also describe conditions under which the block-error threshold for saturated belief-propagation decoding equals the bit-error threshold.

## Useful Mathematical Tools for Capacity Approaching Codes Design

- **Status**: ✅
- **Reason**: LDPC density evolution threshold 추정 수학도구 - 코드설계(E) 관련, 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7946147
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Fulvio Babich, Alessandro Soranzo, Francesca Vatta
- **PDF**: https://ieeexplore.ieee.org/document/7946147
- **Abstract**: Focus of this letter is the oldest class of codes that can approach the Shannon limit quite closely, i.e., low-density parity-check (LDPC) codes, and two mathematical tools that can make their design an easier job under appropriate assumptions. In particular, we present a simple algorithmic method to estimate the threshold for regular and irregular LDPC codes on memoryless binary-input continuous-output additive white Gaussian noise (AWGN) channels with sum-product decoding, and, to determine how close are the obtained thresholds to the theoretical maximum, i.e., to the Shannon limit, we give a simple and invertible expression of the AWGN channel capacity in the binary input-soft output case. For these codes, the thresholds are defined as the maximum noise level, such that an arbitrarily small bit-error probability can be achieved as the block length tends to infinity. We assume a Gaussian approximation for message densities under density evolution, a widely used simplification of the decoding algorithm.

## Channel Coding for Nonvolatile Memory Technologies: Theoretical Advances and Practical Considerations

- **Status**: ✅
- **Reason**: NAND 플래시 등 NVM 채널코딩 서베이지만 LDPC 등 구체 기법·정량 비교 다룸, NAND 직접(A) 관련 예외 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7920318
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Lara Dolecek, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/7920318
- **Abstract**: Every bit of information in a storage or memory device is bound by a multitude of performance specifications, and is subject to a variety of reliability impediments. At the other end, the physical processes tamed to remember our bits offer a constant source of risk to their reliability. These include a variety of noise sources, access restrictions, intercell interferences, cell variabilities, and many more issues. Tying together this vector of performance figures with that vector of reliability issues is a rich matrix of emerging coding tools and techniques. Channel coding schemes ensure target reliability and performance and have been at the core of memory systems since their nascent age. In this survey, we first overview the fundamentals of channel coding and summarize well-known codes that have been used in nonvolatile memories (NVMs). Next, we demonstrate why the conventional coding approaches ubiquitously based on symmetric channel models and optimization for the Hamming metric fail to address the needs of modern memories. We then discuss several recently proposed innovative coding schemes. Behind each coding scheme lies an interesting theoretical framework, building on deep ideas from mathematics and the information sciences. We also survey some of the most fascinating bridges between deep theory and storage performance. While the focus of this survey is primarily on the pervasive multilevel NAND Flash, we envision that other benefiting memory technologies will include phase change memory, resistive memories, and others.

## Low-Power LDPC-CC Decoding Architecture Based on the Integration of Memory Banks

- **Status**: ✅
- **Reason**: LDPC-CC 디코더 저전력 메모리뱅크 통합 HW 아키텍처(D) - 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:7781655
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Injae Yoo, In-Cheol Park
- **PDF**: https://ieeexplore.ieee.org/document/7781655
- **Abstract**: This brief proposes a low-power low-density parity check convolutional code (LDPC-CC) decoder that is fully compatible with the IEEE 1901 standard. The proposed architecture merges multiple memory banks into one to make it consume much less power than the conventional architecture. Memory operations conducted by all the unit processors are synchronized in the proposed decoder to merge the memory and avoid any possible data hazard. The data hazard happens when a unit processor tries to read a log-likelihood ratio before a different processor updates it, degrading the error-correcting performance. Memory-access patterns appearing in a memory-based LDPC-CC decoder are formulated to determine the size of a sliding window adequate for decoding. Experimental results show that the decoding architecture employing the merged memory and the proper window size reduces the power consumption by up to 40% compared to the conventional architecture that employs multiple memory banks.

## Approaching Capacity at High Rates With Iterative Hard-Decision Decoding

- **Status**: ✅
- **Reason**: spatially coupled generalized LDPC + 반복 HDD, density evolution 분석 - 신규 디코더·코드설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7954697
- **Type**: journal
- **Published**: Sept. 2017
- **Authors**: Yung-Yih Jian, Henry D. Pfister, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/7954697
- **Abstract**: A variety of low-density parity-check (LDPC) ensembles have now been observed to approach capacity with message-passing decoding. However, all of them use soft (i.e., non-binary) messages and a posteriori probability decoding of their component codes. In this paper, we show that one can approach capacity at high rates using iterative hard-decision decoding (HDD) of generalized product codes. Specifically, a class of spatially coupled generalized LDPC codes with Bose-Chaudhuri-Hocquengham component codes is considered, and it is observed that, in the high-rate regime, they can approach capacity under the proposed iterative HDD. These codes can be seen as generalized product codes and are closely related to braided block codes. An iterative HDD algorithm is proposed that enables one to analyze the performance of these codes via density evolution.

## Estimation of channel state information for non-volatile flash memories

- **Status**: ✅
- **Reason**: A: 플래시 MLC/TLC soft-input 디코딩용 채널상태추정, NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8210594
- **Type**: conference
- **Published**: 3-6 Sept. 
- **Authors**: Jürgen Freudenberger, Mohammed Rajab, Sergo Shavgulidze
- **PDF**: https://ieeexplore.ieee.org/document/8210594
- **Abstract**: Error correction coding based on soft-input decoding can significantly improve the reliability of flash memories. Such soft-input decoding algorithms require reliability information about the state of the memory cell. This work proposes a channel model for soft-input decoding that considers the asymmetric error characteristic of multi-level cell (MLC) and triple-level cell (TLC) memories. Based on this model, an estimation method for the channel state information is devised which avoids additional pilot data for channel estimation. Furthermore, the proposed method supports page-wise read operations.

## An approximate hardware check node for λ-min-based LDPC decoders

- **Status**: ✅
- **Reason**: D: λ-min BP 체크노드 근사 HW 회로(비교기 14→7 절감) — 바이너리 LDPC 디코더 HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8081429
- **Type**: conference
- **Published**: 28 Aug.-2 
- **Authors**: Georgios Perris-Samios, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/8081429
- **Abstract**: In this paper, iterative decoding using Belief Propagation λ-min decoding algorithm is considered. In this algorithm check nodes use only the λ lowest-magnitude messages thus simplifying the hardware complexity and reducing memory usage. A parallel-input architecture is proposed for the check node. We focus on the determination of the sought minima in a parallel fashion. Novel simplified circuits for the derivation of the λ minimum values are introduced here. The main novelty that leads to substantial hardware simplification is the approximate derivation of the λ values. Specifically, We here show that using the introduced approximate computation substantial hardware savings are obtained with no significant degradation in decoding performance. For cases of practical interest the proposed solution is shown to reduce the number of comparisons per check node from 14 down to 7; i.e., 2 times.

## Performance of protograph LDPC codes over ergodic Nakagami fading channels

- **Status**: ✅
- **Reason**: 수정 PEXIT 기반 신규 protograph(IARA) 바이너리 LDPC 구성, 채널 특화지만 설계기법 이식 여지(E, 애매→포함)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8261162
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Yi Fang, Guofa Cai, Zhaojie Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/8261162
- **Abstract**: The protograph low-density parity-check (LDPC) codes have drawn much attention in the past decade due to their simple structures and outstanding error performance. Unfortunately, the conventional protograph codes designed for additive white Gaussian noise (AWGN) channels can not perform well in ergodic Nakagami fading channels. To address this issue, we construct a new rate-1/2 protograph code, called improved accumulate-repeat-accumulate (IARA) code, by exploiting a modified PEXIT algorithm. We compare the decoding threshold and bit error rate (BER) of the IARA code with the existing protograph codes, the regular LDPC code and the irregular code over ergodic Nakagami fading channels. Both analytical and simulated results show that the proposed IARA code can achieve the lowest BER in the high signal-to-noise-ratio region. Hence, the IARA code can be considered as a good candidate for use in wireless communication systems with fast fading.

## A simple design for large girth LDPC matrix

- **Status**: ✅
- **Reason**: 기하수열+소수체 기반 large-girth QC-LDPC 신규 구성법, 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8261240
- **Type**: conference
- **Published**: 25-27 Sept
- **Authors**: Somsak Choomchuay
- **PDF**: https://ieeexplore.ieee.org/document/8261240
- **Abstract**: This paper describes an alternative method for designing regular quasi-cyclic LDPC codes with large girths. The permutation matrix was designed based on the geometric sequence and prime number field. The design starts with a portion of the full-range matrix with column weight of 3. With a decided code rate, elements in the rows are extended by adding a certain column of the same full-range matrix into the designing matrix. Resulted codes can offer relatively good performance compared to the published literatures.

## On the Performance of High-Rate LDPC Codes with Low-Resolution Analog-to-Digital Conversion

- **Status**: ✅
- **Reason**: 저해상도 ADC와 LDPC 결합, soft 정보·LLR 양자화 trade-off — NAND read LLR 양자화에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8287950
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Niklas Doose, Peter A. Hoeher
- **PDF**: https://ieeexplore.ieee.org/document/8287950
- **Abstract**: Future wireless networks put high requirements on many system components. Data rates of the order of 100 Gbps and beyond, currently used in wired optical networks only, are expected for 5G applications. This imposes high effort with respect to code design and decoding algorithms. Due to their low complexity, LDPC codes are an essential part of many modern communication systems. Additionally, high symbol rates will require high-rate analog-to-digital conversion which turns out to be very power consuming. In order to explore trade-offs between hardware complexity and digital baseband processing, this contribution investigates the bit error rate performance and soft Monte Carlo simulation of LDPC codes together with reduced-complexity analog-to-digital conversion.

## Design of Check-Hybrid LDPC Codes for Data Communications over Helicopter-Satellite Channels

- **Status**: ✅
- **Reason**: QC-LDPC 체크노드를 simplex/RM 제약으로 치환한 check-hybrid LDPC 신규 코드설계(E), EXIT 분석 포함 — 바이너리 LDPC 구성 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8287915
- **Type**: conference
- **Published**: 24-27 Sept
- **Authors**: Ping Wang, Liuguo Yin, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/8287915
- **Abstract**: A class of check-hybrid low-density parity-check (CH-LDPC) codes is designed and implemented to mitigate the problem of periodical signal blockage over the helicoptersatellite channels. The CH-LDPC code is derived by replacing one layer check nodes of a quasi-cyclic LDPC (QC-LDPC) code by simplex code constraints or first-order Reed-Muller (RM) code constraints, based on the property that the check matrix of the QC-LDPC code has a layered structure. Moreover, extrinsic information transfer (EXIT) functions are established to analyze the iterative decoding performance of the CH-LDPC codes. Simulation results show that, compared with the QCLDPC coding scheme, the CH-LDPC coding scheme designed in this paper achieves more than 25% bandwidth efficiency improvement over the helicopter-satellite channels.

## Low complexity rate compatible puncturing patterns design for LDPC codes

- **Status**: ✅
- **Reason**: LDPC rate-compatible puncturing 패턴 설계 + 밀도진화 임계값 분석 — 바이너리 LDPC 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8115558
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Fulvio Babich, Matteo Noschese, Alessandro Soranzo +1
- **PDF**: https://ieeexplore.ieee.org/document/8115558
- **Abstract**: In contemporary digital communications design, two major challenges should be addressed: adaptability and flexibility. The system should be capable of flexible and efficient use of all available spectrums and should be adaptable to provide efficient support for the diverse set of service characteristics. These needs imply the necessity of limit-achieving and flexible channel coding techniques, to improve system reliability. Low Density Parity Check (LDPC) codes fit such requirements well, since they are capacity-achieving. Moreover, through puncturing, allowing the adaption of the coding rate to different channel conditions with a single encoder/decoder pair, adaptability and flexibility can be obtained at a low computational cost. In this paper, the design of rate-compatible puncturing patterns for LDPCs is addressed. We use a previously defined formal analysis of a class of punctured LDPC codes through their equivalent parity check matrices. We address a new design criterion for the puncturing patterns using a simplified analysis of the decoding belief propagation algorithm, i.e., considering a Gaussian approximation for message densities under density evolution, and a simple algorithmic method, recently defined by the Authors, to estimate the threshold for regular and irregular LDPC codes on memoryless binary-input continuous-output Additive White Gaussian Noise (AWGN) channels.

## Low complexity ADMM-LP based decoding strategy for LDPC convolutional codes

- **Status**: ✅
- **Reason**: ADMM-LP 디코더 저복잡도 스케줄링(NS-ADMM) 제안 — 부호 비의존적 BP/LP 디코더 알고리즘으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8115500
- **Type**: conference
- **Published**: 21-23 Sept
- **Authors**: Hayfa Ben Thameur, Bertrand Le Gal, Nadia Khouja +2
- **PDF**: https://ieeexplore.ieee.org/document/8115500
- **Abstract**: A node-wise (NS) schedule has been recently proposed for decoding LDPC codes with the linear programming (LP) decoding approach, based on the alternate direction method of multipliers (ADMM). It improves the error correction performances as well as the convergence speed of the ADMM-LP decoder. However, it suffers from a high computational complexity resulted from residuals calculation. In this paper, a new formulation of the ADMM-LP algorithm with a modified computational scheduling is proposed for decoding LDPC convolutional codes. Simulations show that it reduces the computational complexity while improving the error correction performances and speeding up the decoding process. The decoding complexity is further reduced when considering the NS-ADMM approximation which allows savings up to 70% of the residuals calculation.

## Channel characteristics dependence of the performance of decoding algorithms for efficient error-control codes

- **Status**: ✅
- **Reason**: 채널추정 없이 antilog/유클리드거리+진폭리미터 기반 저복잡도 초기화 디코딩 — LDPC에 적용되며 부호 비의존 메시지패싱 초기화 기법으로 이식 가능(C, 애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8211635
- **Type**: conference
- **Published**: 20-22 Sept
- **Authors**: M. C. Liberatori, L. Coppolillo, L. J. Arnone +3
- **PDF**: https://ieeexplore.ieee.org/document/8211635
- **Abstract**: In this paper we study the initialization step of decoding algorithms for efficient error-control coding techniques, and its dependence of the channel characteristics over which transmission is performed. LDPC and Polar codes are selected as efficient error-control codes operating over different channels. Channels under study are the classic Additive White Gaussian noise channel, the Rayleigh fading channel, and the Middleton's Class A impulsive noise channel. An efficient initialization step is performed when the initialization step uses estimates based on the corresponding probability density function of the channel, evaluated for the two possible transmitted signals of a binary transmission. However, real time evaluation of these estimates can be an operation of high complexity. A low complexity alternative decoding strategy is proposed, based on the estimation of square Euclidean distances propagated using antilog operations, in combination with a simple signal amplitude limiter. This low complexity strategy avoids the need of channel characteristics estimation, and results into a reasonable good BER performance, especially for decoding LDPC codes.

## A low complexity encoder construction for systematic quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: systematic QC-LDPC 저복잡도 인코더 생성행렬 구성(새 row reduction), 바이너리 코드설계 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8095475
- **Type**: conference
- **Published**: 18-20 Sept
- **Authors**: Yuval Genga, Olayinka Ogundile, Olutayo Oyerinde +1
- **PDF**: https://ieeexplore.ieee.org/document/8095475
- **Abstract**: For practical applications in forward error correction, the importance of a systematic codeword cannot be overemphasized. Thus, this paper proposes the construction of a systematic quasi-cyclic (QC) LDPC code. This systematic structure is achieved by a row reduction technique different from the conventional Gaussian elimination method. This row reduction technique has the advantage of being easier to implement when compared to Gaussian row reduction techniques. The proposed row reduction technique maintains the quasi cyclic structure and the sparsity of the QC-LDPC parity check matrix while providing a low complexity approach to the construction of the generator matrix. In addition, the proposed construction exhibits a good BER performance for high rate codes.

## Improved Low-Power LDPC FEC for Coherent Optical Systems

- **Status**: ✅
- **Reason**: C/D: 저복잡·저전력 LDPC FEC 구현(에너지/처리량 정량), 바이너리 LDPC 디코더 HW 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8345844
- **Type**: conference
- **Published**: 17-21 Sept
- **Authors**: Kevin Cushon, Per Larsson-Edefors, Peter Andrekson
- **PDF**: https://ieeexplore.ieee.org/document/8345844
- **Abstract**: We propose and demonstrate a low-complexity LDPC FEC system for coherent optical applications. Implementation results show an estimated NCG of 11.0 dB with 20% overhead, 160 Gbps throughput, and energy consumption of 3.4 pJ per bit.

## Adaptive threshold multi bit flipping for low density parity check codes

- **Status**: ✅
- **Reason**: LDPC용 adaptive threshold 다중 비트플립 디코더 알고리즘 제안, 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8125856
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: P. Seetha Ravi, K. Pargunarajan
- **PDF**: https://ieeexplore.ieee.org/document/8125856
- **Abstract**: In this paper an adaptive threshold for flipping intensity based dynamic weighted multi bit flipping algorithm is proposed to overcome the existing complexities in finding the threshold. The change in the check node and bit node status are also considered here. Improvement in performance is observed using the method of adaptive threshold in place of fixed threshold.

## Modified weighted bit flipping algorithm based on intrinsic information for ldpc codes

- **Status**: ✅
- **Reason**: LDPC용 새 weighted bit-flipping 디코더(intrinsic info 기반, 덧셈/뺄셈만)로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:8125854
- **Type**: conference
- **Published**: 13-16 Sept
- **Authors**: M. Velmurugan, K. Pargunarajan
- **PDF**: https://ieeexplore.ieee.org/document/8125854
- **Abstract**: This paper proposes a modified bit flipping algorithm and its weighted variants based on reliability derived from intrinsic information. Compared to other existing algorithms where extrinsic information based reliability was used in the flipping function, here intrinsic information based reliability is also equally considered. This algorithm only uses additions and subtractions to modify reliability as compared to other reliability based BF algorithms, which use multiplications and divisions. Hence, it offers good performance with a minimal increase in computational complexity.

## GPU accelerated gigabit level BCH and LDPC concatenated coding system

- **Status**: ✅
- **Reason**: GPU 병렬 LDPC(내부)+BCH(외부) 연접 디코더 SW 구현 — 병렬화 HW/SW 아키텍처(D)와 error floor 개선, 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:8091021
- **Type**: conference
- **Published**: 12-14 Sept
- **Authors**: Selcuk Keskin, Taskin Kocak
- **PDF**: https://ieeexplore.ieee.org/document/8091021
- **Abstract**: Increasing data traffic and multimedia services in recent years have paved the way for the development of optical transmission methods to be used in high bandwidth communications systems. In order to meet the very high throughput requirements, dedicated application specific integrated circuit and field programmable gate array solutions for low-density parity-check decoding are proposed in recent years. Conversely, software solutions are less expensive, scalable, and flexible and have shorter development cycle. A natural solution to lower the error floor is to concatenate the LDPC code with an algebraic outer code to clean up the residual errors. In this paper, we present the design and parallel software implementation of a major computation algorithm for LDPC decoding on general purpose graphics processing units as inner code and BCH decoding algorithm as outer code to achieve excellent error-correcting performance. The experimental results show that the proposed GPU-based concatenated decoder achieves the maximum decoding throughput of 1.82Gbps at 10 iterations with low bit-error rate (BER).
