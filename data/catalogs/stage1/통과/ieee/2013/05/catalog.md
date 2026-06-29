# IEEE Xplore — 2013-05 (1차선별 통과)


## Construction of Structured Regular LDPC Codes: A Design-Theoretic Approach

- **Status**: ✅
- **Reason**: t-design 기반 girth-6 구조적 바이너리 regular LDPC 신규 구성 기법(E), 바이너리 girth-6 QC-LDPC도 구성하므로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6466338
- **Type**: journal
- **Published**: May 2013
- **Authors**: H. Falsafain, M. Esmaeili
- **PDF**: https://ieeexplore.ieee.org/document/6466338
- **Abstract**: A new combinatorial technique for constructing girth-6 structured binary regular low-density parity-check (LDPC) codes based on special types of t-designs is given. A very large number of well-known t-designs can be used by this method for code construction. Based on this method, a t-(v,k,λ) design D=(X,B) can be exploited for code construction if it satisfies the following three conditions: 1) |B1 ∩ B2|≤ t for any two blocks B1,B2∈ B and B1 ≠ B2; 2) λ>1; and 3) k>t. Though the technique works for any t-design satisfying these conditions, we focus only on the utilization of simple triple systems, super-simple BIBDs, Steiner systems, and large sets (LSs) of t-designs. We also construct binary and non-binary girth-6 QC-LDPC codes from the t-designs satisfying these conditions by using matrix dispersion method. Experimental results show that the constructed non-binary QC-LDPC codes can provide good practical performance under iterative decoding using the fast Fourier transform based q-ary sum-product algorithm (FFT-QSPA) and they can achieve acceptable coding gains over random-like codes of comparable parameters decoded with sum-product algorithm (SPA).

## Gallager B Decoder on Noisy Hardware

- **Status**: ✅
- **Reason**: Gallager B 디코더 noisy hardware 분석 및 density evolution 임계값, 신뢰성 저하 환경 디코더 설계 가이드라인으로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6480915
- **Type**: journal
- **Published**: May 2013
- **Authors**: S. M. Sadegh Tabatabaei Yazdi, Hyungmin Cho, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6480915
- **Abstract**: Conventional communications theory assumes that the data transmission is noisy but the processing at the receiver is entirely error-free. Such assumptions may have to be revisited for advanced (silicon) technologies in which hardware failures are a major concern at the system-level. Hence, it is important to characterize the performance of a communication system with both noisy processing components and noisy data transmission. Coding systems based on low-density parity check (LDPC) codes are widely used for a variety of applications. In this paper, we focus on probabilistic analysis of the LDPC Gallager B decoder built out of faulty components. Using the density evolution technique, we find approximations for the optimal threshold of the decoder and the symbol error rate (SER) of the decoded sequence as functions of both the channel error rate and error rates of the decoder components, for both binary and non-binary regular LDPC codes. Furthermore, we study the convergence of the output SER and the decoding threshold of the decoder for different ranges of error rates. We verify our results using MATLAB simulations and hardware emulation of noisy decoders. Results presented in this paper can serve as systematic design guidelines in resource allocation for noisy decoders. Informed resource allocation is of particular relevance to emerging data storage and processing applications that need to maintain high levels of reliability despite hardware errors in advanced technologies.

## Quantum Dot Cellular Automata Check Node Implementation for LDPC Decoders

- **Status**: ✅
- **Reason**: Normalized Min-Sum 부분병렬 layered LDPC check node HW 아키텍처(C/D), 디코더 알고리즘+HW 기여 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6473892
- **Type**: journal
- **Published**: May 2013
- **Authors**: Muhammad Awais, Marco Vacca, Mariagrazia Graziano +2
- **PDF**: https://ieeexplore.ieee.org/document/6473892
- **Abstract**: The quantum dot Cellular Automata (QCA) is an emerging nanotechnology that has gained significant research interest in recent years. Extremely small feature sizes, ultralow power consumption, and high clock frequency make QCA a potentially attractive solution for implementing computing architectures at the nanoscale. To be considered as a suitable CMOS substitute, the QCA technology must be able to implement complex real-time applications with affordable complexity. Low density parity check (LDPC) decoding is one of such applications. The core of LDPC decoding lies in the check node (CN) processing element which executes actual decoding algorithm and contributes toward overall performance and complexity of the LDPC decoder. This study presents a novel QCA architecture for partial parallel, layered LDPC check node. The CN executes Normalized Min Sum decoding algorithm and is flexible to support CN degree dc up to 20. The CN is constructed using a VHDL behavioral model of QCA elementary circuits which provides a hierarchical bottom up approach to evaluate the logical behavior, area, and power dissipation of the whole design. Performance evaluations are reported for the two main implementations of QCA i.e. molecular and magnetic.

## Using Quasi-EZ-NAND Flash Memory to Build Large-Capacity Solid-State Drives in Computing Systems

- **Status**: ✅
- **Reason**: NAND SSD LDPC ECC+DSP 계층 분산 아키텍처 — NAND 직접(A) 및 HW(D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6158640
- **Type**: journal
- **Published**: May 2013
- **Authors**: Yangyang Pan, Guiqiang Dong, Ningde Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/6158640
- **Abstract**: Future flash-based solid-state drives (SSDs) must employ increasingly powerful error correction code (ECC) and digital signal processing (DSP) techniques to compensate the negative impact of technology scaling on NAND flash memory device reliability. Currently, all the ECC and DSP functions are implemented in a central SSD controller. However, the use of more powerful ECC and DSP makes such design practice subject to significant speed performance degradation and complicated controller implementation. An EZ-NAND (Error Zero NAND) flash memory design strategy is emerging in the industry, which moves all the ECC and DSP functions to each memory chip. Although EZ-NAND flash can simplify controller design and achieve high system speed performance, its high silicon cost may not be affordable for large-capacity SSDs in computing systems. We propose a quasi-EZ-NAND design strategy that hierarchically distributes ECC and DSP functions on both NAND flash memory chips and the central SSD controller. Compared with EZ-NAND design concept, it can maintain almost the same speed performance while reducing silicon cost overhead. Assuming the use of low-density parity-check (LDPC) code and postcompensation DSP technique, trace-based simulations show that SSDs using quasi-EZ-NAND flash can realize almost the same speed as SSDs using EZ-NAND flash, and both can reduce the average SSD response time by over 90 percent compared with conventional design practice. Silicon design at 65 nm node shows that quasi-EZ-NAND can reduce the silicon cost overhead by up to 44 percent compared with EZ-NAND.

## Rate-Compatible Short-Length Protograph LDPC Codes

- **Status**: ✅
- **Reason**: rate-compatible 단블록 protograph LDPC 신규 코드 설계(E), error floor 없는 바이너리 LDPC 구성으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6484236
- **Type**: journal
- **Published**: May 2013
- **Authors**: Thuy Van Nguyen, Aria Nosratinia
- **PDF**: https://ieeexplore.ieee.org/document/6484236
- **Abstract**: This paper produces a rate-compatible protograph LDPC code at 1k information blocklength with superior performance in both waterfall and error floor regions. The design of such codes has proved difficult in the past because the constraints imposed by structured design (protographs), rate-compatibility, as well as small block length, are not easily satisfied together. For example, as the block length decreases, the predominance of decoding threshold as the main parameter in coding design is reduced, thus complicating the search for good codes. Our rate-compatible protograph codes have rates ranging from 1/3 to 4/5 and show no error floor down to 10-6 FER.

## Clipping Demapper for LDPC Decoding in Impulsive Channel

- **Status**: ✅
- **Reason**: Clipping demapper / clipping function parameters for BP decoder LLR input under impulsive noise; LLR-input pre-processing technique is portable to BP decoder front-end (C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6486528
- **Type**: journal
- **Published**: May 2013
- **Authors**: Hassen Ben Maad, Alban Goupil, Laurent Clavier +1
- **PDF**: https://ieeexplore.ieee.org/document/6486528
- **Abstract**: This paper deals with the performance of Low-Density Parity-Check codes in impulsive interference modeled by α-stable random variables. In case of α-stable noise, the optimal inputs of the belief propagation decoder are complex to obtain. We propose to use the simple clipping approach that reduces the impact of large noise values. Our main contribution is to give three different approaches to obtain the parameters of the clipping function and to assess the performance of the decoder. We show that a look-up table whose values are pre-determined, thanks to the Density Evolution tool, is the most efficient approach.

## Relaxed Half-Stochastic Belief Propagation

- **Status**: ✅
- **Reason**: Relaxed Half-Stochastic 바이너리 메시지 BP 신규 디코더(C), 회로 구현 적합 저복잡도 버전, NAND 디코더 HW에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6468990
- **Type**: journal
- **Published**: May 2013
- **Authors**: Francois Leduc-Primeau, Saied Hemati, Shie Mannor +1
- **PDF**: https://ieeexplore.ieee.org/document/6468990
- **Abstract**: Low-density parity-check codes are attractive for high throughput applications because of their low decoding complexity per bit, but also because all the codeword bits can be decoded in parallel. However, achieving this in a circuit implementation is complicated by the number of wires required to exchange messages between processing nodes. Decoding algorithms that exchange binary messages are interesting for fully-parallel implementations because they can reduce the number and the length of the wires, and increase logic density. This paper introduces the Relaxed Half-Stochastic (RHS) decoding algorithm, a binary message belief propagation (BP) algorithm that achieves a coding gain comparable to the best known BP algorithms that use real-valued messages. We derive the RHS algorithm by starting from the well-known Sum-Product algorithm, and then derive a low-complexity version suitable for circuit implementation. We present extensive simulation results on two standardized codes having different rates and constructions, including low bit error rate results. These simulations show that RHS can converge faster on average than existing state-of-the-art decoding algorithms, leading to improvements in throughput and energy efficiency.

## BCH Code Selection and Iterative Decoding for BCH and LDPC Concatenated Coding System

- **Status**: ✅
- **Reason**: Concatenated BCH+QC-LDPC explicitly for flash memory; error-floor-aware outer code selection and iterative BCH<->LDPC decoding directly applicable to NAND ECC (A/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6486533
- **Type**: journal
- **Published**: May 2013
- **Authors**: Pin-Han Chen, Jian-Jia Weng, Chung-Hsuan Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6486533
- **Abstract**: In this letter, we consider a concatenated BCH and QC-LDPC coding system for potential use of data protection on flash memory. Two issues are studied, and strategies to resolve them are proposed. First, in order to guarantee that the concatenated coding system is free from undesired error floor, we propose a strategy to select the outer BCH codes according to the error patterns of inner QC-LDPC code. We next present an iterative decoding algorithm between inner QC-LDPC and outer BCH codes to alleviate the performance degradation in the waterfall region due to code-concatenation rate loss. The two proposals jointly provide a feasible design for the concatenated BCH and QC-LDPC coding system. Simulations to verify the performance of the proposed concatenated coding system design are given at the end.

## Cost-effective scalable QC-LDPC decoder designs for non-volatile memory systems

- **Status**: ✅
- **Reason**: 비휘발성메모리용 QC-LDPC 디코더 — FIFO 제거 재배열 아키텍처, 면적절감 18.5%, scalable datapath, TSMC 90nm 구현(A/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6638131
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Ming-Han Chung, Yu-Min Lin, Cheng-Zhou Zhan +1
- **PDF**: https://ieeexplore.ieee.org/document/6638131
- **Abstract**: This paper presents a cost-effective scalable quasi-cyclic LDPC (QC-LDPC) decoder architecture for non-volatile memory systems (NVMS). A re-arranged architecture is proposed to eliminate the first-in-first-out (FIFO) memory in conventional decoders, where the FIFO size is linearly proportional to the codeword size. The area reduction is 18.5% compared to the conventional decoder architecture. The scalable datapaths of the proposed decoder reduce the re-design cost and enable the flexibility of using QC-LDPC codes for NVMS. A prototyping decoder with maximum codeword size of 9280 bits is implemented in TSMC 90nm CMOS technology, and the core area is only 2.52mm2 at 138.8MHz.

## Soft-input soft-output linear programming decoding

- **Status**: ✅
- **Reason**: SISO LP 디코더; LP soft-output이 BP보다 우수한 경우 제시, 바이너리 LDPC 디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6638642
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Erica L. Daly
- **PDF**: https://ieeexplore.ieee.org/document/6638642
- **Abstract**: This paper presents the soft-input soft-output (SISO) linear programming (LP) decoder. It is shown that the soft information gleaned from a pseudo-codeword solution to the LP optimization is not only useful, but that it can be superior to the soft information output from a SISO belief propagation (BP) decoder in certain situations.

## Analysis of finite-alphabet iterative decoders under processing errors

- **Status**: ✅
- **Reason**: 신뢰성 낮은 HW상 유한알파벳 반복디코더 오류해석·자원할당; min-sum/Gallager류 디코더 HW 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6638630
- **Type**: conference
- **Published**: 26-31 May 
- **Authors**: Chu-Hsiang Huang, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6638630
- **Abstract**: It is widely recognized that emerging hardware technologies will be inherently unreliable. In this paper, we study the performance of finite-alphabet iterative decoders when implemented on noisy hardware built out of unreliable components. We derive a recursive expression for the error probability in terms of both the transmission noise and processing errors. We allow different components of the decoding algorithm associated with certain computational units (i.e., bit and check nodes of varying degrees in the underlying graph) to be implemented using a collection of processors with varying levels of processing error rates. Performance analysis and optimal resource allocation of a noisy Gallager E decoder is presented as an application example of our general derivation. Simulations demonstrate that the implementation of a noisy iterative decoder according to the proposed analysis-guided optimal resource allocation outperforms implementations based on uninformed resource allocation under the common resource budget.

## An efficient LDPC encoder based on block-column-cycle structure for CMMB

- **Status**: ✅
- **Reason**: CMMB용 block-column-cycle 구조 기반 LDPC 인코더로 HW 메모리 절감(D)—QC-LDPC 구조 활용 인코더 기법 이식 가능, 애매해 살림
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6615361
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: Lei Liu, Changyin Liu, Ziliang Lin
- **PDF**: https://ieeexplore.ieee.org/document/6615361
- **Abstract**: Concerning the high encoding complexity of LDPC codes, an efficient encoder based on block-column-cycle structure for CMMB is proposed, which is able to take full advantage of the characteristics of the sparse parity-check matrix, such as cyclicity and equality of column weight. Experimental results show that the proposed encoder can reduce dramatically the memory requirements in hardware implementation, and improve the encoding rate at the same time.

## A pragmatic approach to designing irregular LDPC codes

- **Status**: ✅
- **Reason**: density evolution + differential evolution으로 irregular LDPC degree profile 최적화 — 바이너리 LDPC 코드설계 기법(E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6615336
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: Jiancun Zuo, Fangming Zhao, Qiudong Sun
- **PDF**: https://ieeexplore.ieee.org/document/6615336
- **Abstract**: This paper proposes a pragmatic algorithm to design optimal irregular low-density parity-check codes, which adopts a one-dimensional density evolution to calculate the noise threshold and utilizes fast-convergence differential evolution to search the optimal degree profiles. Simulation results show that the irregular LDPC codes optimized by the presented algorithm can also beat Turbo codes even at moderate block length.

## Lowering Error Floors in Stochastic Decoding of LDPC Codes Based on Wire-Delay Dependent Asynchronous Updating

- **Status**: ✅
- **Reason**: C/D. stochastic LDPC 디코딩 error floor 저감(wire-delay 비동기 업데이트) 신규 디코더 HW 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6524673
- **Type**: conference
- **Published**: 22-24 May 
- **Authors**: Naoya Onizawa, Warren J. Gross, Takahiro Hanyu +1
- **PDF**: https://ieeexplore.ieee.org/document/6524673
- **Abstract**: Stochastic decoding provides ultra-low-complexity hardware for high-throughput parallel low-density parity-check (LDPC) decoders. Asynchronous stochastic decoding was pro- posed to demonstrate the possibility of low power dissipation and high throughput in stochastic decoders, but decoding might stop before convergence due to "lock-up", causing error floors. In this paper, we introduce wire-delay dependent asynchronous stochastic decoding to reduce the error floors. Instead of assigning the same delay to all computation nodes in the previous work, different computation delay is assigned to each computation node depending on its wire length. The variation of update timing increases switching activities to decrease the possibility of the "lock-up", lowering the error floors. BER performance using a regular (1024, 512) (3, 6) LDPC code is simulated based on our timing model that has computation and wire delays estimated under ASPLA 90nm CMOS technology. It is demonstrated that the proposed asynchronous decoder achieves an up to 0.25-dB gain compared with that of the synchronous and the conventional asynchronous decoders.

## Low-complexity finite alphabet iterative decoders for LDPC codes

- **Status**: ✅
- **Reason**: FAID(finite alphabet iterative decoder) 저복잡도 HW 구현, error-floor 개선·bit-serial CNU — 바이너리 LDPC 디코더+HW 핵심(C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6572100
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Fang Cai, Xinmiao Zhang, David Declercq +3
- **PDF**: https://ieeexplore.ieee.org/document/6572100
- **Abstract**: Low-density parity-check (LDPC) codes are adopted in many applications due to their Shannon-limit approaching error-correcting performance. Nevertheless, belief-propagation (BP) based decoding of these codes suffers from the error-floor problem. Recently, a new type of decoders termed finite alphabet iterative decoders (FAIDs) were introduced. The FAIDs use simple Boolean maps for variable node processing. With very short word length, they can surpass the BP-based decoders in the error floor region. This paper develops a low-complexity implementation architecture for FAIDs by making use of their properties. Particularly, an innovative bit-serial check node unit is designed for FAIDs, and the symmetric Boolean maps for variable node processing lead to small silicon area. An optimized data scheduling scheme is also proposed to increase the hardware utilization efficiency. From synthesis results, the proposed FAID implementation needs only 52% area to reach the same throughput as one of the most efficient Min-sum decoders for an example (7807, 7177) LDPC code, while achieving better error-correcting performance in the error-floor region.

## Construction of Quasi-Cyclic LDPC codes with large girth based on circulant permutation matirx

- **Status**: ✅
- **Reason**: QC-LDPC short-cycle 제거 신규 알고리즘(CPM shift 조정, QC 구조 보존) (E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6676434
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Peng Yang, Xiaoxiao Bao, Hui Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6676434
- **Abstract**: In this paper, we propose an algorithm for removing short-cycles in Quasi-Cyclic (QC) Low-density parity-check (LDPC) codes. First using an algorithm with lower computational complexity, all the cycles in the parity check matrix H are found. Then following a ruler, we adjust the shift value of circulant permutation matrix (CPM) to remove the short-cycles. This algorithm could ensure that the code after cycle removal process preserves the quasi-cyclic structure. Simulation results show that: comparing with the codes (504,252) and (1008, 504), we achieve 0.1dB improvement both.

## A simple parity check matrix LDPC code for perpendicular magnetic recording channels

- **Status**: ✅
- **Reason**: 수정 array형 패리티검사행렬 신규 구성(modified array, 2 decision variable), 바이너리 코드설계(E); PMR 도메인이나 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6559665
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Sekson Timakul, Somsak Choochuay
- **PDF**: https://ieeexplore.ieee.org/document/6559665
- **Abstract**: In LDPC code design, the structure of code's parity check matrix can be very crucial to code performance. In this paper, we have investigated a simple designed parity check matrix when the code is applied to a PMR channel of a storage system. Belief propagation algorithm and min-sum algorithm are two major decoding algorithms used to benchmarked the code's merits. Additive white Gaussian noise channel (AWGN) and perpendicular magnetic recording (PMR) channel with SISO equalizer in PR2 target are the conditions of our investigation. The LDPC code itself is a modified array type. Its construction fairly simple compared to normal array and quasi-cyclic code. We used two decision variables to define the permutation matrix. A method proposed by Tanner's et.al had been adapted to the modified array code. The decoders have been tested for 5 and 20. iterations. SNR versus BER and BLER were measured.

## Design of high-throughput QC-LDPC decoder for WiMAX standard

- **Status**: ✅
- **Reason**: WiMAX QC-LDPC 고처리율 디코더 HW 아키텍처(행/열 동시처리) - NAND LDPC HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6599692
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Tahere Heidari, Abumoslem Jannesari
- **PDF**: https://ieeexplore.ieee.org/document/6599692
- **Abstract**: In this paper, a high throughput low-density parity-check (LDPC) decoder for 802.16e standard is presented. With simultaneous rows and columns processing, which reduced the number of clock cycles per iteration, the throughput of the decoder is improved. The proposed decoder architecture was designed for 802.16e standard with rate of 1/2 and code length of 2304 with 7-encodings style. It is synthesized on 130 nm CMOS technology by Synopsys Design Compiler. The obtained result in the operating frequency of 100 MHz shows total power consumption of 242mW and the chip area of 6.9 mm2.

## A new hybrid decoding algorithm for LDPC codes based on the improved variable multi weighted bit-flipping and BP algorithms

- **Status**: ✅
- **Reason**: 새 하이브리드 디코더(IVMWBF+BP) 제안 - 부호 비의존 비트플리핑/BP 개선으로 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6599566
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Ehsan Olyaei Torshizi, Hossein Sharifi, Meysam Seyrafi
- **PDF**: https://ieeexplore.ieee.org/document/6599566
- **Abstract**: In this paper, a new two-stage hybrid algorithm for decoding Low-Density Parity-Check (LDPC) codes is proposed that incorporates two iterative decoding. For the first stage of decoding, we offer a new decoding algorithm called Improved Variable Multi Weighted Bit-Flipping (IVMWBF) algorithm. Since the IVMWBF algorithm is based on the idea of flipping variable multi bits in each iteration, both improvement in performance and reduction in iteration number and computational complexity are observed in this algorithm. The proposed hybrid algorithm which is a combination of the IVMWBF and BP algorithms, while having a performance exactly similar to that of the BP algorithm, has less complexity compared to that algorithm.
