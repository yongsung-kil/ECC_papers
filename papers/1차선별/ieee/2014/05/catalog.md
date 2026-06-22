# IEEE Xplore — 2014-05 (1차선별 통과)


## Rate-0.96 LDPC Decoding VLSI for Soft-Decision Error Correction of NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시 soft-decision LDPC 디코딩 VLSI, EG-LDPC + APP 기반 알고리즘 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6547748
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jonghong Kim, Wonyong Sung
- **PDF**: https://ieeexplore.ieee.org/document/6547748
- **Abstract**: The reliability of data stored in high-density Flash memory devices tends to decrease rapidly because of the reduced cell size and multilevel cell technology. Soft-decision error correction algorithms that use multiple-precision sensing for reading memory can solve this problem; however, they require very complex hardware for high-throughput decoding. In this paper, we present a rate-0.96 (68254, 65536) shortened Euclidean geometry low-density parity-check code and its VLSI implementation for high-throughput NAND Flash memory systems. The design employs the normalized a posteriori probability (APP)-based algorithm, serial schedule, and conditional update, which lead to simple functional units, halved decoding iterations, and low-power consumption, respectively. A pipelined-parallel architecture is adopted for high-throughput decoding, and memory-reduction techniques are employed to minimize the chip size. The proposed decoder is implemented in 0.13-μm CMOS technology, and the chip size and energy consumption of the decoder are compared with those of a BCH (Bose-Chaudhuri-Hocquenghem) decoding circuit showing comparable error-correcting performance and throughput.

## Enhanced Precision Through Multiple Reads for LDPC Decoding in Flash Memories

- **Status**: ✅
- **Reason**: NAND 플래시 LDPC 직접 적용: multiple-read MI 기반 word-line 전압 양자화/LLR 정밀도 최적화, absorbing set 대응 — 카테고리 A/C 핵심
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804933
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jiadong Wang, Kasra Vakilinia, Tsung-Yi Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/6804933
- **Abstract**: Multiple reads of the same Flash memory cell with distinct word-line voltages provide enhanced precision for LDPC decoding. In this paper, the word-line voltages are optimized by maximizing the mutual information (MI) of the quantized channel. The enhanced precision from a few additional reads allows frame error rate (FER) performance to approach that of full-precision soft information and enables an LDPC code to significantly outperform a BCH code. A constant-ratio constraint provides a significant simplification in the optimization with no noticeable loss in performance. For a well-designed LDPC code, the quantization that maximizes the mutual information also minimizes the FER in our simulations. However, for an example LDPC code with a high error floor caused by small absorbing sets, the MMI quantization does not provide the lowest frame error rate. The best quantization in this case introduces more erasures than would be optimal for the channel MI in order to mitigate the absorbing sets of the poorly designed code. The paper also identifies a trade-off in LDPC code design when decoding is performed with multiple precision levels; the best code at one level of precision will typically not be the best code at a different level of precision.

## Density Evolution for Min-Sum Decoding of LDPC Codes Under Unreliable Message Storage

- **Status**: ✅
- **Reason**: 양자화 min-sum 디코더의 신뢰성 없는 메시지 저장 모델·밀도진화 분석. 양자화 비트 트레이드오프는 NAND LDPC 디코더(C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6774414
- **Type**: journal
- **Published**: May 2014
- **Authors**: Alexios Balatsoukas-Stimming, Andreas Burg
- **PDF**: https://ieeexplore.ieee.org/document/6774414
- **Abstract**: We analyze the performance of quantized min-sum decoding of low-density parity-check codes under unreliable message storage. To this end, we introduce a simple bit-level error model and show that decoder symmetry is preserved under this model. Subsequently, we formulate the corresponding density evolution equations to predict the average bit error probability in the limit of infinite block length. We present numerical threshold results and we show that using more quantization bits is not always beneficial in the context of faulty decoders.

## Finite Alphabet Iterative Decoders for LDPC Codes: Optimization, Architecture and Analysis

- **Status**: ✅
- **Reason**: FAID 디코더의 저복잡도 HW 아키텍처(bit-serial CNU, error-floor 개선) — 이식 가능 디코더+HW (C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6776564
- **Type**: journal
- **Published**: May 2014
- **Authors**: Fang Cai, Xinmiao Zhang, David Declercq +2
- **PDF**: https://ieeexplore.ieee.org/document/6776564
- **Abstract**: Low-density parity-check (LDPC) codes are adopted in many applications due to their Shannon-limit approaching error-correcting performance. Nevertheless, belief-propagation (BP) based decoding of these codes suffers from the error-floor problem, i.e., an abrupt change in the slope of the error-rate curve that occurs at very low error rates. Recently, a new type of decoders termed finite alphabet iterative decoders (FAIDs) were introduced. The FAIDs use simple Boolean maps for variable node processing, and can surpass the BP-based decoders in the error floor region with very short word length. We restrict the scope of this paper to regular dv=3 LDPC codes on the BSC channel. This paper develops a low-complexity implementation architecture for the FAIDs by making use of their properties. Particularly, an innovative bit-serial check node unit is designed for the FAIDs, and a small-area variable node unit is proposed by exploiting the symmetry in the Boolean maps. Moreover, an optimized data scheduling scheme is proposed to increase the hardware utilization efficiency. From synthesis results, the proposed FAID implementation needs only 52% area to reach the same throughput as one of the most efficient standard Min-Sum decoders for an example (7807, 7177) LDPC code, while achieving better error-correcting performance in the error-floor region. Compared to an offset Min-Sum decoder with longer word length, the proposed design can achieve higher throughput with 45% area, and still leads to possible performance improvement in the error-floor region.

## Classification Codes for Soft Information Generation from Hard Flash Reads

- **Status**: ✅
- **Reason**: 플래시 hard read로부터 LDPC용 soft 정보 생성하는 classification code, 간단 HW 구현 — NAND LDPC ECC 직접 (A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804934
- **Type**: journal
- **Published**: May 2014
- **Authors**: Mustafa N. Kaynak, Patrick R. Khayat, Sivagnanam Parthasarathy
- **PDF**: https://ieeexplore.ieee.org/document/6804934
- **Abstract**: In this paper, a tensor product-based classification code (CC) is proposed to generate coarse soft information based on the hard flash reads for use in soft information-utilizing error correction codes (ECCs), particularly low-density parity check (LDPC) codes. Analysis and simulation results have shown that with a small ECC overhead, CC helps the LDPC code decoder achieve better performance compared to a hard-input case. Furthermore, the proposed code has very simple encoding and decoding algorithms; therefore, it can be easily implemented in hardware to aid existing ECC systems.

## Structured Bit-Interleaved LDPC Codes for MLC Flash Memory

- **Status**: ✅
- **Reason**: MLC 플래시용 bit-interleaved 이진 regular LDPC 코드 설계, 비트 타입별 오류확률 반영 디코딩 threshold 최적화 — A/E 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804932
- **Type**: journal
- **Published**: May 2014
- **Authors**: Kathryn Haymaker, Christine A. Kelley
- **PDF**: https://ieeexplore.ieee.org/document/6804932
- **Abstract**: Due to a structural feature in the programming process of MLC (two bits per cell) and TLC (three bits per cell) flash memory, the majority of errors that occur are single-bit errors. Moreover, the voltages used to store the bits typically result in different bit error probabilities for the two or three types of bits. In this work we analyze binary regular LDPC codes in the standard bit-interleaved coded modulation implementation, assuming different probabilities on the bits, to determine what ratio of each type of bit should be connected at the check nodes to improve the decoding threshold. We then propose a construction of nonbinary LDPC codes using their binary images, resulting in check node types that come close to these optimal ratios.

## Concatenated Raptor Codes in NAND Flash Memory

- **Status**: ✅
- **Reason**: NAND 플래시용 concatenated Raptor 코드. 비-LDPC지만 NAND ECC 직접 적용(A)이고 product code 내부코드 구조 참고 가치, 애매하면 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804931
- **Type**: journal
- **Published**: May 2014
- **Authors**: Geunyeong Yu, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/6804931
- **Abstract**: Two concatenated coding schemes based on fixed-rate Raptor codes are proposed for error control in NAND flash memory. One is geared for off-line recovery of uncorrectable pages and the other is designed for page error correction during the normal read mode. Both proposed coding strategies assume hard-decision decoding of the inner code with inner decoding failure generating erasure symbols for the outer Raptor code. Raptor codes allow low-complexity decoding of very long codewords while providing capacity-approaching performance for erasure channels. For the off-line page recovery scheme, one whole NAND block forms a Raptor codeword with each inner codeword typically made up of several Raptor symbols. An efficient look-up-table strategy is devised for Raptor encoding and decoding which avoids using large buffers in the controller despite the substantial size of the Raptor code employed. The potential performance benefit of the proposed scheme is evaluated in terms of the probability of block recovery conditioned on the presence of uncorrectable pages. In the suggested page-error-correction strategy, on the other hand, a hard-decision-iterating product code is used as the inner code. The specific product code employed in this work is based on row-column concatenation with multiple intersecting bits to allow the use of longer component codes. In this setting the collection of bits captured within each intersection of the row-column codes acts as the Raptor symbol(s), and the intersections of failed row codes and column codes are declared as erasures. The error rate analysis indicates that the proposed concatenation provides a considerable performance boost relative to the existing error correcting system based on long Bose-Chauduri-Hocquenghem (BCH) codes.

## Optimal Detector for Multilevel NAND Flash Memory Channels with Intercell Interference

- **Status**: ✅
- **Reason**: MLC NAND 플래시 ICI 채널의 최적 검출기(soft-output) 유도 — A 직접 해당, soft LLR 검출 기법
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804928
- **Type**: journal
- **Published**: May 2014
- **Authors**: Meysam Asadi, Xiujie Huang, Aleksandar Kavcic +1
- **PDF**: https://ieeexplore.ieee.org/document/6804928
- **Abstract**: In this paper we derive the optimal detector for multilevel cell (MLC) flash memory channels with intercell interference (ICI). We start with the MLC channel model proposed by Dong et al. and just slightly alter the model to guarantee mathematical tractability of the optimal detectors (maximum likelihood and maximum a-posteriori sequence and symbol detectors). The optimal detector is obtained by computing branch metrics using Fourier transforms of analytically computable characteristic functions (corresponding to likelihood functions). We derive the detectors for both simple one-dimensional (1D) channel models and more realistic page-orientated two-dimensional (2D) channel models. Simulation results show that the hard-output bit error rate (BER) performance matches some previously known detectors, but that the soft-output detector outperforms previously known detectors by 0.35 dB.

## Realizing Unequal Error Correction for nand Flash Memory at Minimal Read Latency Overhead

- **Status**: ✅
- **Reason**: NAND 플래시 unequal error correction을 concatenated coding으로 구현, read latency 최소화 — A 직접 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6803051
- **Type**: journal
- **Published**: May 2014
- **Authors**: Jiangpeng Li, Kai Zhao, Jun Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/6803051
- **Abstract**: In nand Flash memory, all pages have the same storage capacity and hence accommodate the same amount of redundancy in support of error correction. In current practice, user data in all the pages are protected by the same error correction code. However, different types of pages in multibit per cell memory have largely different bit error rates, for which appropriate unequal error correction can achieve a better utilization of memory redundancy and hence improve program/erase (P/E) cycling endurance. Nevertheless, a straightforward realization of unequal error correction suffers from severe memory read latency penalty. This brief presents a design strategy to implement unequal error correction through concatenated coding, which can well match the unequal error rates among different types of pages at minimal memory read latency penalty. Based on measurement results from commercial sub-22-nm 2 bits/cell nand Flash memory chips, we carried out simulations from both the coding and storage system perspectives, and the results show that this design strategy can improve the P/E cycling endurance by 20% and only incur less than 7% increase of storage system read response time at the end of Flash memory lifetime with the P/E cycling of around 1800.

## A high throughput LDPC decoder using a mid-range GPU

- **Status**: ✅
- **Reason**: GPU 기반 고처리량 LDPC 디코더 + TDMP/메모리 접근 최적화 — HW/병렬화 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6855061
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Xie Wen, Jiao Xianjun, Pekka Jääskeläinen +4
- **PDF**: https://ieeexplore.ieee.org/document/6855061
- **Abstract**: A standard-throughput-approaching LDPC decoder has been implemented on a mid-range GPU in this paper. Turbo-Decoding Message-Passing algorithm is applied to achieve high throughput. Different from traditional host managed multi-streams to hide host-device transfer delay, we use kernel maintained data transfer scheme to achieve implicit data transfer between host memory and device shared memory, which eliminates an intermediate stage of global memory. Data type optimization, memory accessing optimization, and low complexity Soft-In Soft-Out algorithm are also used to improve efficiency. Through these optimization methods, the 802.11n LDPC decoder on NVIDIA GTX480 GPU, which is released in 2010 with Fermi architecture, has achieved a high throughput of 295Mb/s when decoding 512 codewords simultaneously, which is close to highest bit rate 300Mb/s with 20MHz bandwidth in 802.11n standard. Decoding 1024 and 4096 codewords achieve 330 and 365Mb/s. A 802.16e LDPC decoder is also implemented, 374Mb/s (512 codewords), 435Mb/s (1024 codewords) and 507Mb/s (4096 codewords) throughputs have been achieved.

## Joint detection and decoding of LDPC coded distributed space-time signaling in wireless relay networks via linear programming

- **Status**: ✅
- **Reason**: LP 기반 LDPC 디코딩 + 패리티검사 부등식 수를 줄이는 적응적 절차 — 바이너리 LDPC LP 디코더 복잡도 저감 기법, 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6853930
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Kun Wang, Wenhao Wu, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/6853930
- **Abstract**: We develop a linear programming based approach for the joint detection and decoding of LDPC coded distributed space-time signaling transmitted in a wireless relay network. Traditional receivers typically decouple the detection and decoding processes as two separate blocks or require iterative turbo exchange of extrinsic information between the soft detector and decoder. We exploit the constraints imposed on the channel input signals and jointly consider the training symbols as well as the LDPC code information by formulating a unified linear programming (LP) receiver. Moreover, in consideration of the vast amount of LDPC parity check inequalities, we present an adaptive procedure to significantly reduce the complexity of the proposed LP receiver.

## A fast architecture for finding maximum (or minimum) values in a set

- **Status**: ✅
- **Reason**: min-sum 디코더의 두 최솟값 탐색용 고속 정렬 아키텍처 — LDPC 디코더 HW(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6855071
- **Type**: conference
- **Published**: 4-9 May 20
- **Authors**: Andrea Dario Giancarlo Biroli, Juan Chi Wang
- **PDF**: https://ieeexplore.ieee.org/document/6855071
- **Abstract**: High speed architectures for extracting the best (maximum or minimum) values in a given set and their positions is of high importance in many signal processing applications. For example, the search of the two minimum values is an important part in iterative channel decoders for turbo and low-density-parity-check codes. In this paper, a new architecture is proposed to find the gth best value in an unsorted list of k elements, where the ranking position g can be any integer between 1 and k. The architecture can also be used to find in the assigned set a generic subset of the largest or smallest values. The proposed solution is particularly efficient in terms of hardware complexity and latency when the cardinality of the assigned set k is large and the values are represented on a reduced number of bits n. Synthesis results obtained with a 90-nm CMOS standard cell technology are provided for specific choices of g, k and n. Moreover, the nice properties of regularity and scalability of the proposed architecture are exploited to develop a QCA (quantum cellular automata) based implementation, which achieves lower power consumption or higher speed.

## Asymptotic and finite-length performance of irregular spatially-coupled codes

- **Status**: ✅
- **Reason**: 이식 가능 코드설계(E): irregular SC-LDPC 유한길이/임계 분석 + PEG로 error floor 저감, 바이너리 SC-LDPC 구성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6849017
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Reza A. Ashrafi, Abdullah Sarıduman, Ali E. Pusane
- **PDF**: https://ieeexplore.ieee.org/document/6849017
- **Abstract**: The newest family of low-density parity-check (LDPC) codes, spatially-coupled (SC) codes, is shown to have several desirable characteristics including low implementation complexity and close-to-optimal performance over a range of channels. Furthermore, because of their ribbon-shaped parity-check matrices, window decoding can be used to decode these codes, which leads to low-delay implementations. Researchers have focused on asymptotically regular SC code ensembles and have examined several aspects of the code construction processes. In this paper, we concentrate on irregular SC code ensembles. We evaluate their decoding thresholds over the binary erasure channel and show that their performance is better than their regular SC counterparts. It is also shown that the gap between asymptotic coding thresholds of irregular SC ensembles and the fundamental Shannon limit gets negligibly small. For the sake of a better comparison, we have also evaluated the finite-length error performance of selected regular and irregular SC codes over the additive white Gaussian channel and it is also observed that finite-length error performance of these irregular SC codes outperforms regular SC codes. To further improve the error performance of these codes and to lower the possible error floors, progressive edge growth algorithm has also been considered in the finite-length performance analysis.

## Iterative receiver for Qc-LDPC coded underwater acoustic communication systems

- **Status**: ✅
- **Reason**: QC-LDPC + MMSE-DFE turbo 반복 수신기로 소프트정보 교환 — BP-기반 반복 디코더 기법 이식 여지(C), 애매하므로 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6859617
- **Type**: conference
- **Published**: 26-30 May 
- **Authors**: Liang Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6859617
- **Abstract**: Quasi Cyclic-Low Density Parity Check (QC-LDPC) codes are easy to construct and provide the considerable coding gain, which is suitable for underwater acoustic communication (UWAC). Single-carrier (SC) transmission with frequency-domain equalization (FDE) is today recognized as an attractive alternative to orthogonal frequency-division multiplexing (OFDM) for communication application with the inter-symbol interference (ISI) caused by multi-path propagation, especially in shallow water channel. In this paper, the turbo theory is applied on the QC-LDPC codes and minimum mean square error (MMSE) decision feedback equalizer (DFE) to design iterative data processing for underwater acoustic communication system. In the proposed iterative structure, the MMSE based FD-DFE and QC-LDPC decoder exchange soft information through an iterative manner so that the performance of underwater acoustic communication system can be improved greatly. Based on sound speed profiles (SSP) measured in the lake and finite-element ray tracking method, the shallow water channel is constructed to verify the validity of the proposed system structure.

## A new hybrid decoding algorithm based on multi-dimensional searching for regular LDPC codes in finite geometries

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 다차원 탐색 기반 하이브리드 비트플리핑 디코딩 알고리즘 — 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6999766
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Ehsan Olyaei Torshizi, Hossein Sharifi, Azadeh Daneshgar +1
- **PDF**: https://ieeexplore.ieee.org/document/6999766
- **Abstract**: In this paper, a new fast convergence hybrid decoding algorithm based on multi-dimensional searhing is proposed for decoding LDPC codes. The main idea of this algorithm is flipping variable multi bits in each iteration, change in which leads to the syndrome vector with least hamming weight. To this end, the algorithm does multidimensional searching between all possible bit positions that could flip in each iteration to select the best choices. Simulation results illustrate that the proposed algorithm converge significantly faster and have reduction in iteration number and also have excellent performance but with little performance difference than the robust Sum-Product algorithm.

## A Low-Latency Algorithm and FPGA Design for the Min-Search of LDPC Decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 min-search 저지연 알고리즘+FPGA 설계, 이식 가능 HW 기법(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6969398
- **Type**: conference
- **Published**: 19-23 May 
- **Authors**: Georgios Tzimpragos, Christoforos Kachris, Dimitrios Soudris +1
- **PDF**: https://ieeexplore.ieee.org/document/6969398
- **Abstract**: The problem of finding efficiently the first k minimum or maximum values is generally met in many application fields, such as error control coding. More specifically, optimized solutions for the selection of the two or three smallest elements out of a given set of numbers are greatly needed for the design of high-speed Low-Density Parity-Check (LDPC) decoders, as this min-search can be the bottleneck. This paper aims to tackle current limitations by proposing a novel algorithm for solving this problem, where the searching is based on scanning from the most significant bit (MSB) to the least significant bit (LSB) of each input data. A design mapped to reconfigurable logic and a software tool for the automatic generation of synthesizable VHDL codes, implementing such low-latency components are presented as well. Experimental results show that compared to existing solutions, the proposed scheme achieves an up to 42% reduction in latency even at worst case. Since the hardware unit is repeatedly used in the LDPC decoder design, the described high-speed approach is strongly recommended.

## Advanced error prediction LDPC for high-speed reliable TLC nand-based SSDs

- **Status**: ✅
- **Reason**: TLC NAND용 AEP-LDPC(program disturb/retention/coupling 모델링한 LLR 예측), NAND 직접(A) 핵심
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6849375
- **Type**: conference
- **Published**: 18-21 May 
- **Authors**: Tsukasa Tokutomi, Shuhei Tanakamaru, Tomoko Ogura Iwasaki +1
- **PDF**: https://ieeexplore.ieee.org/document/6849375
- **Abstract**: Highly reliable solid-state drives (SSDs) with triple-level-cell (TLC) NAND flash and Advanced Error-Prediction Low-Density Parity-Check (AEP-LDPC) are proposed. To increase NAND flash's capacity, bits/cell have been doubled and tripled, which causes reliability to drastically degrade due to narrower VTH margins. Previously proposed Error-Prediction LDPC (EP-LDPC) error-correcting code (ECC) improved reliability for Multi-Level-Cell (MLC) NAND flash [4]. However, in EP-LDPC program disturb is not modeled, so precision is limited, especially in short data retention <; 2 days. Here, AEP-LDPC is proposed for TLC NAND flash. By considering effects of program disturb, data retention and floating-gate capacitive coupling, the most accurate SSDs can be realized, with high speed read capability. The SSD's data-retention time increases by more than 12x, decode iterations decrease 57% and acceptable TLC NAND BER increases by more than 2.8 ×.

## Design and Test of Adaptive Computing Fabrics for Scalable and High-Efficiency Cognitive SoC Applications

- **Status**: ✅
- **Reason**: 불신뢰 회로 환경에서 error floor 낮추고 수렴 가속하는 적응형 LDPC 디코더 VLSI/FPGA 아키텍처 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6875448
- **Type**: conference
- **Published**: 14-16 May 
- **Authors**: Pascal Nsame, Guy Bois, Yvon Savaria
- **PDF**: https://ieeexplore.ieee.org/document/6875448
- **Abstract**: In this paper, a new adaptive computing fabric (ACF) that achieves both real-time multi-mode/multi-rate adaptation and lower error floor for cognitive SoC applications is presented. The VLSI architecture of the ACF is experimentally shown to meet the DVB, 802.3an and 802.ad target specifications. Our design delivers a 10-14 bit error rate (BER) with a bit energyto- noise density of Eb/N0=5dB with an energy-efficiency of 0.61pJ/bit. Experiments are conducted comparing Low-Density Parity-Check (LDPC) codes error correction performance in the presence of unreliable circuits due to aggressive manufacturing defect rates and/or run-time defect rates from components enabled by SoC integration. We report on a 201.6Gbps 65nm CMOS design and Xilinx FPGA prototype, which demonstrates in hardware how real-time adaptive techniques can accelerate decoding convergence and lower the error floor. Finally, We show experimentally that our ACF design can achieve energyefficiency throughput speed-ups at scale in the range of 200x to 5000x as compared to the same algorithm running in software (optimized C program) on a single CPU core.
