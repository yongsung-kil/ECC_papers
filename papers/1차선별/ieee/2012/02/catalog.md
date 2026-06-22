# IEEE Xplore — 2012-02 (1차선별 통과)


## Asynchronous Physical-Layer Network Coding

- **Status**: ✅
- **Reason**: 물리계층 네트워크코딩 BP 디코딩 프레임워크 — 채널코딩과 통합한 BP 메시지패싱 개선 기법, 부호 비의존적 BP 개선으로 바이너리 LDPC BP 이식 가능성(C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6108306
- **Type**: journal
- **Published**: February 2
- **Authors**: Lu Lu, Soung Chang Liew
- **PDF**: https://ieeexplore.ieee.org/document/6108306
- **Abstract**: A key issue in physical-layer network coding (PNC) is how to deal with the asynchrony between signals transmitted by multiple transmitters. That is, symbols transmitted by different transmitters could arrive at the receiver with symbol misalignment as well as relative carrier-phase offset. A second important issue is how to integrate channel coding with PNC to achieve reliable communication. This paper investigates these two issues and makes the following contributions: 1) We propose and investigate a general framework for decoding at the receiver based on belief propagation (BP). The framework can effectively deal with symbol and phase asynchronies while incorporating channel coding at the same time. 2) For unchannel-coded PNC, we show that for BPSK and QPSK modulations, our BP method can significantly reduce the asynchrony penalties compared with prior methods. 3) For QPSK unchannel-coded PNC, with a half symbol offset between the transmitters, our BP method can drastically reduce the performance penalty due to phase asynchrony, from more than 6 dB to no more than 1 dB. 4) For channel-coded PNC, with our BP method, both symbol and phase asynchronies actually improve the system performance compared with the perfectly synchronous case. Furthermore, the performance spread due to different combinations of symbol and phase offsets between the transmitters in channel-coded PNC is only around 1 dB. The implication of 3) is that if we could control the symbol arrival times at the receiver, it would be advantageous to deliberately introduce a half symbol offset in unchannel-coded PNC. The implication of 4) is that when channel coding is used, symbol and phase asynchronies are not major performance concerns in PNC.

## Quasi-Cyclic LDPC Codes: Influence of Proto- and Tanner-Graph Structure on Minimum Hamming Distance Upper Bounds

- **Status**: ✅
- **Reason**: QC-LDPC 최소해밍거리 상한과 프로토/Tanner 그래프 구조 기반 신규 구성 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6145509
- **Type**: journal
- **Published**: Feb. 2012
- **Authors**: Roxana Smarandache, Pascal O. Vontobel
- **PDF**: https://ieeexplore.ieee.org/document/6145509
- **Abstract**: Quasi-cyclic (QC) low-density parity-check (LDPC) codes are an important instance of proto-graph-based LDPC codes. In this paper we present upper bounds on the minimum Hamming distance of QC LDPC codes and study how these upper bounds depend on graph structure parameters (like variable degrees, check node degrees, girth) of the Tanner graph and of the underlying proto-graph. Moreover, for several classes of proto-graphs we present explicit QC LDPC code constructions that achieve (or come close to) the respective minimum Hamming distance upper bounds. Because of the tight algebraic connection between QC codes and convolutional codes, we can state similar results for the free Hamming distance of convolutional codes. In fact, some QC code statements are established by first proving the corresponding convolutional code statements and then using a result by Tanner that says that the minimum Hamming distance of a QC code is upper bounded by the free Hamming distance of the convolutional code that is obtained by “unwrapping” the QC code.

## On Generic Erasure Correcting Sets and Related Problems

- **Status**: ✅
- **Reason**: 바이너리 erasure 채널 반복디코딩용 generic erasure correcting set / 패리티검사행렬 구성 — 코드설계(E) 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6145473
- **Type**: journal
- **Published**: Feb. 2012
- **Authors**: Rudolf Ahlswede, Harout Aydinian
- **PDF**: https://ieeexplore.ieee.org/document/6145473
- **Abstract**: Motivated by iterative decoding techniques for the binary erasure channel Hollmann and Tolhuizen introduced and studied the notion of generic erasure correcting sets for linear codes. A generic (r,s)-erasure correcting set generates for all codes of codimension r a parity check matrix that allows iterative decoding of all correctable erasure patterns of size s or less. The problem is to derive bounds on the minimum size F(r,s) of generic erasure correcting sets and to find constructions for such sets. In this paper, we continue the study of these sets. We derive better lower and upper bounds. Hollmann and Tolhuizen also introduced the stronger notion of (r,s)-sets and derived bounds for their minimum size G(r,s) . Here also we improve these bounds. We observe that these two conceps are closely related to so called s -wise intersecting codes, an area, in which G(r,s) has been studied primarily with respect to ratewise performance. We derive connections. Finally, we observed that hypergraph covering can be used for both problems to derive good upper bounds.

## Quasi-cyclic LDPC codes: Construction and rank analysis of their parity-check matrices

- **Status**: ✅
- **Reason**: QC-LDPC 신규 구성법(유한체 분할 기반 Fourier 변환 영역), 바이너리 포함 명시 - 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6181797
- **Type**: conference
- **Published**: 5-10 Feb. 
- **Authors**: Keke Liu, Qin Huang, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6181797
- **Abstract**: A construction of binary and non-binary quasi-cyclic (QC)-LDPC codes based on partitions of finite fields of characteristic 2 is proposed. The construction is carried out in the Fourier transform domain. The parity-check matrices of these QC-LDPC codes are arrays of circulant permutation matrices. The ranks of these arrays are analyzed and combinatorial expressions are derived. Example codes are given and simulations show that they perform well over the AWGN channel decoded with message-passing decoding algorithms.

## A transform approach for constructing quasi-cyclic Euclidean geometry LDPC codes

- **Status**: ✅
- **Reason**: QC-EG-LDPC 신규 구성(trapping set 없는 large min-dist 서브클래스), 바이너리 - 코드설계 E
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6181800
- **Type**: conference
- **Published**: 5-10 Feb. 
- **Authors**: Qiuju Diao, Wei Zhou, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6181800
- **Abstract**: A method for constructing quasi-cyclic Euclidean geometry (QC-EG) LDPC codes in the Fourier transform domain is presented. Given a Euclidean geometry over a finite field of characteristic 2, base matrices in the Fourier transform domain are first constructed. Then the inverse Fourier transforms of these base matrices, combined with row and column permutations, result in low-density arrays of circulant permutation matrices and/or zero matrices. The null spaces of these low-density arrays give a family of QC-EG-LDPC codes. Codes in a special subclass have large minimum distances and their Tanner graphs contain no harmful trapping sets with sizes smaller than their minimum distances.

## New codes on graphs constructed by connecting spatially coupled chains

- **Status**: ✅
- **Reason**: SC-LDPC 체인 연결 신규 구성으로 디코딩 임계·복잡도 개선 — E 코드설계(바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6181771
- **Type**: conference
- **Published**: 5-10 Feb. 
- **Authors**: Dmitri Truhachev, David G. M. Mitchell, Michael Lentmaier +1
- **PDF**: https://ieeexplore.ieee.org/document/6181771
- **Abstract**: A novel code construction based on spatially coupled low-density parity-check (SC-LDPC) code chains is presented. The proposed code ensembles are described by graphs in which individual SC-LDPC code chains of various lengths serve as edges. We demonstrate that connecting several appropriately chosen SC-LDPC code chains results in improved iterative decoding thresholds compared to those of a single coupled chain in addition to reducing the decoding complexity required to achieve a specific bit error probability.

## A single-routing layered LDPC decoder for 10Gbase-T Ethernet in 130nm CMOS

- **Status**: ✅
- **Reason**: layered LDPC 디코더 HW 아키텍처(단일라우팅, 파이프라인, early-termination)로 D 카테고리 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6165020
- **Type**: conference
- **Published**: 30 Jan.-2 
- **Authors**: Dan Bao, Xubin Chen, Yuebin Huang +3
- **PDF**: https://ieeexplore.ieee.org/document/6165020
- **Abstract**: A highly-parallel LDPC decoder architecture for 10Gbase-T applications is designed in this paper. Firstly, we reduce the routing complexity and corresponding power consumption by the proposed decoder architecture based on single routing networks. Secondly, the proposed architecture is designed with pipelined layered scheduling and multi-block parallel decoding, which improves operation speed and removes pipeline stalls in conventional highly-parallel layered scheduling. Thirdly, we trade off between hardware cost and throughput by a digit-serial data-path. Fourthly, an efficient early-termination circuit suitable for layered decoding is designed. The decoder is implemented in 130nm 1P8M CMOS process. The core area is 18.4mm2 with 14% reduction, and the decoding throughput is 9.48Gbps operating at 278MHz and 5 iterations. The tested power consumption is 774mW at 1.2V and 80MHz.

## Exploiting the shift property of structured LDPC codes for reduced-complexity sliced message passing based decoder design

- **Status**: ✅
- **Reason**: 구조화 LDPC의 shift property로 permutation network 59% 축소한 SMP 디코더 HW 기법(스토리지 언급), D 카테고리
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6167467
- **Type**: conference
- **Published**: 30 Jan.-2 
- **Authors**: Xiaoheng Chen, Chung-Li Wang
- **PDF**: https://ieeexplore.ieee.org/document/6167467
- **Abstract**: The sliced message passing (SMP) scheme breaks the sequential tie of CN update and VN update and presents an efficient way of elevating the hardware utilization ratio and increasing throughput. However, the forward and backward permutation networks complicate the message routing and make the SMP-based decoder not amenable for codes with large CN degrees. By utilizing the shift property in some structured codes, we reduced the permutation network by almost 59% when compared with the state-of-art designs. Overall, this design technique will make SMP-based decoder more cost-efficient and applicable for the future communications and storage systems.

## ASIC design of a Gbit/s LDPC decoder for iterative MIMO systems

- **Status**: ✅
- **Reason**: 유연한 블록/레이트 LDPC 디코더 ASIC HW 설계로 D 카테고리 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6167409
- **Type**: conference
- **Published**: 30 Jan.-2 
- **Authors**: Christina Gimmler, Frank Kienle, Christian Weis +2
- **PDF**: https://ieeexplore.ieee.org/document/6167409
- **Abstract**: The design of double-iterative systems like turbo synchronization or iterative demapping and decoding will be one of the big challenges in the next years. The components of such systems need to fulfill stringent conditions on throughput and flexibility thus making a reuse of available standard components difficult. We present a high throughput ASIC design for LDPC decoding in iterative MIMO systems with a high flexibility on block sizes (3720 to 14880 bits, granularity 186 bits) and code rates (1/2 to 4/5). After P&R, the ASIC design has an area of 4.588 mm2 and consumes 1271 mW at a clock frequency of 275 MHz. The LDPC decoder has a throughput of 3.5 Gbit/s (@5 iterations) while the resulting iterative MIMO system (4 feedback loops with 5 LDPC iterations each) runs at 275 Mbit/s.

## Coding for the binary asymmetric channel

- **Status**: ✅
- **Reason**: 스토리지 비대칭채널(Z-channel)용 LDPC 코드 변환 구성, 스토리지 ECC+코드설계로 B/E 해당
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6167465
- **Type**: conference
- **Published**: 30 Jan.-2 
- **Authors**: Ryan Gabrys, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6167465
- **Abstract**: Motivated by the recent emergence of storage technologies characterized by the intrinsic asymmetries in data recording, this work presents a preliminary look of two simple but practical high-rate code constructions for the Z-channel. The constructions are based on transforming LDPC codes designed for the binary symmetric channel to bias the number of ones that are sent through the channel. Using simulation results, the performance of this new class of codes is compared against some existing codes, and under certain conditions, new codes are shown to be superior existing asymmetric error correcting codes.

## Characterization and error-correcting codes for TLC flash memories

- **Status**: ✅
- **Reason**: TLC 플래시 에러 특성화 및 신규 ECC 제안(BCH/LDPC 비교), A 카테고리 NAND 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6167470
- **Type**: conference
- **Published**: 30 Jan.-2 
- **Authors**: Eitan Yaakobi, Laura Grupp, Paul H. Siegel +2
- **PDF**: https://ieeexplore.ieee.org/document/6167470
- **Abstract**: Flash memory has become the storage medium of choice in portable consumer electronic applications, and high performance solid state drives (SSDs) are also being introduced into mobile computing, enterprise storage, data warehousing, and data-intensive computing systems. On the other hand, flash memory technologies present major challenges in the areas of device reliability, endurance, and energy efficiency. In this work, the error behavior of TLC flash is studied through an empirical database of errors which were induced by write, read, and erase operations. Based on this database, error characterization at the block and page level is given. To address the observed error behavior, a new error-correcting scheme for TLC flash is given and is compared with BCH and LDPC codes.

## Additional check node to improve the performance of LDPC codes in the error floor region

- **Status**: ✅
- **Reason**: 체크노드 1개 추가로 trapping set 완화해 error floor 개선 — 신규 코드설계 기법(E), 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6176774
- **Type**: conference
- **Published**: 3-5 Feb. 2
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/6176774
- **Abstract**: This paper presents a new scheme to reduce the detrimental effect of the trapping sets in the regular and irregular low density parity check (LDPC) codes. By adding only one new check node and properly selecting its edges, the performance in the error floor region can be improved. Simulation results show that the proposed scheme decreases the bit error rate (BER) and frame error rate (FER) significantly in the high signal-to-noise ratio (SNR) region at the expense of negligible rate loss.

## Over-10×-extended-lifetime 76%-reduced-error solid-state drives (SSDs) with error-prediction LDPC architecture and error-recovery scheme

- **Status**: ✅
- **Reason**: SSD error-prediction LDPC ECC + error-recovery 기법 — A NAND/SSD 직접
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6177074
- **Type**: conference
- **Published**: 19-23 Feb.
- **Authors**: Shuhei Tanakamaru, Yuki Yanagihara, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/6177074
- **Abstract**: This paper presents solid-state drives (SSDs) with two high reliability techniques. First, an error-prediction (EP) low-density-parity-check (LDPC) error-correcting code (ECC) that realizes an over 10× extended lifetime. Second, an error-recovery (ER) scheme that decreases the program-disturb error rate and the data-retention error rate by 74% and 56%, respectively.

## Intensity reflection coefficient based Min-Sum decoding for Low Density Parity Check Codes

- **Status**: ✅
- **Reason**: 표준 Min-Sum에 IRC 계수를 도입한 신규 디코더 변형(C) - 바이너리 LDPC BP에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6174757
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Md. Moshiur Rahman Farazi, Mohammad Rakibul Islam, Khandaker Sultan Mahmood +1
- **PDF**: https://ieeexplore.ieee.org/document/6174757
- **Abstract**: Low Density Parity Check Codes (LDPC) give groundbreaking performance which is known to approach Shannon's limits for sufficiently large block length. Historically and recently, LDPC have been known to give superior performance than concatenated coding. In the following paper, a proposal to modify the standard Min-Sum (MS) algorithm for decoding LDPC codes is presented. This is done by introduction of a factor, intensity reflection coefficient (IRC) in the check to bit node updating process. Simulation results demonstrate that the proposed algorithms are effective in imparting a better performance in terms of a lower bit error rate (BER) at low to medium signal to noise ratio (SNR) when compared to the traditional MS or Belief Propagation (BP) algorithm while adding a minimum amount of complexity.

## Optimized Min-Sum decoding algorithm for Low Density PC codes

- **Status**: ✅
- **Reason**: 최적화 인자 도입 min-sum 디코딩 알고리즘(저복잡도) — C 이식 가능 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6174654
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Dewan Siam Shafiullah, Mohammad Rakibul Islam, Mohammad Mostafa Amir Faisal +1
- **PDF**: https://ieeexplore.ieee.org/document/6174654
- **Abstract**: Low Density Parity Check (LDPC) approaches Shannon -limit performance for binary field and long code lengths. However performance of binary LDPC code is degraded when the code word length is small. An optimized min-sum algorithm for LDPC code is proposed in this paper. In this algorithm unlike other decoding methods an optimization factor has been introduced in both check node and bit node of the Min-sum algorithm. The optimization factor is obtained before decoding program and the same factor is multiplied twice in one cycle. So the increased complexity is fairly low. Simulation results show that the proposed Optimized Min-Sum decoding algorithm performs very close to the Sum-Product decoding, while preserving the main features of the Min-Sum decoding, that is low complexity and independence with respect to noise variance estimation errors.

## A study on adaptive thresholds for reduced complexity bit-flip decoding

- **Status**: ✅
- **Reason**: 적응 임계값 저복잡도 bit-flip 디코딩 + 랜덤 perturbation 탈출 기법 — C 이식 가능 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6174716
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Julian Webber, Toshihiko Nishimura, Takeo Ohgane +1
- **PDF**: https://ieeexplore.ieee.org/document/6174716
- **Abstract**: Low-density parity-check (LDPC) codes are capacity approaching codes that have rapidly been adopted in modern systems such as the IEEE 802.11n and long term evolution advanced (LTE-A) communications standards. The decoders based on the iterative belief propagation offer exceedingly high performance but unfortunately have high computational complexity. Therefore significant research has focused on lower complexity architectures based on the family of so-called bit-flipping algorithms. In the basic bit-flipping algorithm the number of failed parity checks for each bit is calculated and the sign of the bit with the maximum failed checks is inverted. Inverting bits above a certain threshold removes the complexity of calculating a maximum function and adaptive thresholds on each bit further simplifies the design. The choice of threshold updates directly affects the error and convergence performances. Here we describe a simple architecture that has two decoders with different scaling factors and select the branch with the lowest syndrome sum. It is shown that the addition of a random uniform perturbation to the threshold can reduce the average iteration count further by providing an escape from stuck decoding states.

## LDPC Decoding on the Intel SCC

- **Status**: ✅
- **Reason**: LDPC 디코더 병렬화 구현(many-core SCC) - NAND ECC HW 병렬화에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6169530
- **Type**: conference
- **Published**: 15-17 Feb.
- **Authors**: Andreas Diavastos, Panayiotis Petrides, Gabriel Falcao +1
- **PDF**: https://ieeexplore.ieee.org/document/6169530
- **Abstract**: Low-Density Parity-Check (LDPC) codes are powerful error correcting codes used today in communication standards such as DVB-S2 and WiMAX to transmit data inside noisy channels with high error probability. LDPC decoding is computationally demanding and requires irregular accesses to memory which makes it suitable for parallelization. The recent introduction of the many-core Single-chip Cloud Computer (SCC) from Intel research Labs has created new opportunities and also new challenges for programmers that wish to exploit conveniently the high level of parallelism available in the architecture. In this paper we propose three different implementations: a distributed, a shared and a multi-codeword implementation, for LDPC decoding algorithms that explore the Intel SCC scaling opportunities. From the experimental results we observed that the distributed memory model couldn't scale due to the large number of messages exchanged by the parallel kernels, while the shared memory model had a limited scaling due to the overhead added by the uncacheable shared memory. On the other hand, the multi-codeword implementation scales almost linearly acheving a relative throughput of 28 for 32 cores.
