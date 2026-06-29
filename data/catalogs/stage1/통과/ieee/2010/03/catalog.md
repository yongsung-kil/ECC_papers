# IEEE Xplore — 2010-03 (1차선별 통과)


## Improving Burst Error Tolerance of LDPC-Centric Coding Systems in Read Channel

- **Status**: ✅
- **Reason**: 스토리지(magnetic recording) read channel용 LDPC-centric concatenated coding의 버스트 에러 내성 향상 기법(B), 디코딩에 버스트 위치 활용
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5286314
- **Type**: journal
- **Published**: March 2010
- **Authors**: Ningde Xie, Tong Zhang, Erich F. Haratsch
- **PDF**: https://ieeexplore.ieee.org/document/5286314
- **Abstract**: We report on the use of low-density parity check (LDPC)-centric error correction coding (ECC) for magnetic recording read channel in the presence of significant burst errors. Since an LDPC code by itself is severely vulnerable to burst errors due to its soft-decision probability-based decoding, we focus on LDPC-centric concatenated coding in which LDPC code is used as inner code. To improve the burst error tolerance, we propose a hybrid LDPC-centric concatenated coding strategy in which one inner LDPC codeword is replaced by another codeword with much stronger burst error correction capability. This special inner codeword reveals the burst error location information, which can be leveraged by the inner LDPC code decoding to largely improve the overall robustness to burst errors. Using a hybrid BCH-LDPC/RS concatenated coding system as a test vehicle, we demonstrate a significant performance advantage over its RS-only and LDPC-only counterparts in the presence of three different types of burst errors.

## Capacity-Achieving Codes With Bounded Graphical Complexity and Maximum Likelihood Decoding

- **Status**: ✅
- **Reason**: 바이너리 MBIOS 채널 LDPC-GM 신규 부호족 구성+BP/ML 디코딩, 유한 그래프 복잡도와 최소거리 보장 — 이식 가능 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5429143
- **Type**: journal
- **Published**: March 2010
- **Authors**: Chun-Hao Hsu, Achilleas Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/5429143
- **Abstract**: In this paper, the existence of capacity-achieving codes for memoryless binary-input output-symmetric (MBIOS) channels under maximum-likelihood (ML) decoding with bounded graphical complexity is investigated. Graphical complexity of a code is defined as the number of edges in the graphical representation of the code per information bit and is proportional to the decoding complexity per information bit per iteration under iterative decoding. Irregular repeat-accumulate (IRA) codes are studied first. Utilizing the asymptotic average weight distribution (AAWD) of these codes and invoking Divsalar's bound on the binary-input additive white Gaussian noise (BIAWGN) channel, it is shown that simple nonsystematic IRA ensembles outperform systematic IRA and regular low-density parity-check (LDPC) ensembles with the same graphical complexity, and are at most 0.124 dB away from the Shannon limit. However, a conclusive result as to whether these nonsystematic IRA codes can really achieve capacity cannot be reached. Motivated by this inconclusive result, a new family of codes is proposed, called low-density parity-check and generator matrix (LDPC-GM) codes, which are serially concatenated codes with an outer LDPC code and an inner low-density generator matrix (LDGM) code. It is shown that these codes can achieve capacity on any MBIOS channel using ML decoding and also achieve capacity on any BEC using belief propagation (BP) decoding, both with bounded graphical complexity. Moreover, it is shown that, under certain conditions, these capacity-achieving codes have linearly increasing minimum distances and achieve the asymptotic Gilbert–Varshamov bound for all rates.

## Improved Decoding Algorithm of Bit-Interleaved Coded Modulation for LDPC Code

- **Status**: ✅
- **Reason**: BICM-ISPA: 복조+디코딩 결합 SPA 디코더 개선 기법. 바이너리 LDPC BP에 이식 가능한 메시지패싱 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5357453
- **Type**: journal
- **Published**: March 2010
- **Authors**: Ying Wang, Lei Xie, Huifang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/5357453
- **Abstract**: Bit-interleaved coded modulation (BICM), which has been proven to be powerful when applied in low-density parity-check (LDPC) sum-product algorithm (SPA) decoder, is a bandwidth efficient coding scheme. However, the BICM-SPA decoder does not take the statistical dependencies between bits from the same L-ary modulated symbol into account so that it cannot converge to the maximum a-posteriori (MAP) decoding algorithm. In this paper, an improved SPA decoding algorithm for the LDPC code, which combines decoding and demodulation, is proposed. The proposed decoding algorithm, referred to as the BICM-ISPA, is based on generalized distributive law and derived from the generalized symbol SPA under certain rational assumptions. And the BICM-ISPA can asymptotically converge to the MAP decoding solution algorithm. Simulation results show that the BICM-ISPA decoder jointly optimizes the decoding error performance and the computational complexity of the LDPC code over the additive white Gaussian noise channel. Compared with the BICM-SPA decoder, the advantage of the BICM-ISPA is quite significant with a large modulation size and in the scenario where Gray mapping cannot be used.

## Design of High-Throughput Fully Parallel LDPC Decoders Based on Wire Partitioning

- **Status**: ✅
- **Reason**: fully parallel LDPC 디코더의 wire partitioning 기반 파이프라인 HW 설계(D), 처리율·에너지 개선 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4814500
- **Type**: journal
- **Published**: March 2010
- **Authors**: Naoya Onizawa, Takahiro Hanyu, Vincent C. Gaudet
- **PDF**: https://ieeexplore.ieee.org/document/4814500
- **Abstract**: We present a method to design high-throughput fully parallel low-density parity-check (LDPC) decoders. With our method, a decoder's longest wires are divided into several short wires with pipeline registers. Log-likelihood ratio messages transmitted along with these pipelined paths are thus sent over multiple clock cycles, and the decoder's critical path delay can be reduced while maintaining comparable bit error rate performance. The number of registers inserted into paths is estimated by using wiring information extracted from initial placement and routing information with a conventional LDPC decoder, and thus only necessary registers are inserted. Also, by inserting an even number of registers into the longer wires, two different codewords can be simultaneously decoded, which improves the throughput at a small penalty in area. We present our design flow as well as post-layout simulation results for several versions of a length-1024, (3,6)-regular LDPC code. Using our technique, we achieve a maximum uncoded throughput of 13.21 Gb/s with an energy consumption of 0.098 nJ per uncoded bit at E b/N0 = 5 dB. This represents a 28% increase in throughput, a 30% decrease in energy per bit, and a 1.6% increase in core area with respect to a conventional parallel LDPC decoder, using a 90-nm CMOS technology.

## Architecture and Implementation of a First-Generation Iterative Detection Read Channel

- **Status**: ✅
- **Reason**: iterative detection read channel: LDPC+SISO/MP 반복 검출 HW 구현(65nm), ISI 대응 코드. 스토리지 ECC HW/구조(B/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5415775
- **Type**: journal
- **Published**: March 2010
- **Authors**: Richard L. Galbraith, Travis Oenning, Michael Ross +3
- **PDF**: https://ieeexplore.ieee.org/document/5415775
- **Abstract**: This paper explores the architecture of a first-generation iterative detection read channel solution that delivers up to an 8% increase in drive capacity compared to previous generation electronics. Using low density parity check (LDPC) coding, detected data is continually improved by a detection structure that implements multiple iterations through a set of soft-input soft-output (SISO) and message-passing (MP) blocks. A specially constructed LDPC code is used to optimize performance in the presence of inter-symbol interference (ISI). Also, Reed-Solomon error correction coding (ECC) is retained for optimal data integrity. A 65 nm technology is used in the implementation of this design.

## Performance of low-density parity-check coded modulation

- **Status**: ✅
- **Reason**: LLR 근사식(범용 일반식)이 디코더 입력 LLR 계산에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5446927
- **Type**: conference
- **Published**: 6-13 March
- **Authors**: Jon Hamkins
- **PDF**: https://ieeexplore.ieee.org/document/5446927
- **Abstract**: This paper reports the performance of a family of nine accumulate-repeat-4-jagged-accumulate (AR4JA) low-density parity-check (LDPC) codes [4] when used in conjunction with binary phase-shift-keying (BPSK), quadrature PSK (QPSK), 8-PSK, 16-ary amplitude PSK (16-APSK), and 32-APSK. We also report the performance under various mappings of bits to modulation symbols, hard decision decoding, log-likelihood ratio (LLR) approximations, and decoder iterations. One of the simple and well-performing LLR approximations can be expressed in a general equation that applies to all of the modulation types.

## λ-min algorithm using TAP approach

- **Status**: ✅
- **Reason**: LLR-BP의 단순화인 lambda-min 알고리즘 - 부호 비의존적 BP 디코더 변형, 바이너리 LDPC에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5463402
- **Type**: conference
- **Published**: 3-5 March 
- **Authors**: M. Abdelhedi, O. Hamdi, A. Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/5463402
- **Abstract**: In this paper, we present the decoding algorithms of Low-density parity-check (LDPC) codes using statistical physics arguments. Previous works, have shown that the Belief-Propagation (BP) algorithm, is equivalent to the Thouless-Anderson-Palmer (TAP) [1] approach. In this paper, we develop the log-likelihood ratios-Belief Propagation (LLR-BP) algorithm and its simplification, the λ-min algorithm using this method developed in the study of disordered systems. The obtained results by simulation confirm that the λ-min algorithm gets closer to the LLR-BP algorithm as λ increases.

## Maximum Mutual Information Vector Quantization of Log-Likelihood Ratios for Memory Efficient HARQ Implementations

- **Status**: ✅
- **Reason**: LLR 벡터양자화(MMI/KL)—NAND LLR 양자화(A)에 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5453440
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Matteo Danieli, Søren Forchhammer, Jakob Dahl Andersen +2
- **PDF**: https://ieeexplore.ieee.org/document/5453440
- **Abstract**: Modern mobile telecommunication systems, such as 3GPP LTE, make use of Hybrid Automatic Repeat reQuest (HARQ) for efficient and reliable communication between base stationsand mobile terminals. To this purpose, marginal posterior probabilities of the received bits are stored in the form of log-likelihood ratios (LLR) in order to combine information sent across different transmissions due to requests. To mitigate the effects of ever-increasing data rates that call for larger HARQ memory, vector quantization (VQ) is investigated as a technique for temporary compression of LLRs on the terminal. A capacity analysis leads to using maximum mutual information (MMI) as optimality criterion and in turn Kullback-Leibler (KL) divergence as distortion measure. Simulations run based on an LTE-like system have proven that VQ can be implemented in a computationally simple way at low rates of 2-3 bits per LLR value without compromising the system throughput.

## Using time-aware memory sensing to address resistance drift issue in multi-level phase change memory

- **Status**: ✅
- **Reason**: PCM multi-level ECC에서 LDPC soft-decision LLR sensing/LLR 양자화 논의 — NAND read-retry/LLR 양자화(A/C)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5450549
- **Type**: conference
- **Published**: 22-24 Marc
- **Authors**: Wei Xu, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/5450549
- **Abstract**: Because of its great scalability potential and support of multi-level per cell storage, phase change memory has become a topic of great current interest. However, recent studies show that structural relaxation effect makes the resistance of phase change material drift over the time, which can severely degrade multi-level phase change memory storage reliability. This paper studies the potential of using a time-aware memory sensing strategy to address this challenge. The basic idea is to keep track of memory content lifetime and, when memory is being read, accordingly adjust the memory sensing configuration to minimize the negative impact of time-dependent resistance drift on memory storage reliability. Because multi-level phase change memory may demand the use of powerful error correction code (ECC) whose decoding can request either hard-decision or soft-decision log-likelihood (LLR) memory sensing, we discuss both hard-decision and soft-decision time-aware memory sensing in details. Using BCH code and LDPC code as ECC for 4-level/cell and 8-level/cell phase change memory, we carry out simulations and the results show that, compared with time-independent static memory sensing, time-aware memory sensing can increase allowable memory content lifetime by several orders of magnitude.

## Quasi-cyclic ldpc code design for block-fading channels

- **Status**: ✅
- **Reason**: block-fading용 QC-LDPC 신규 구성·효율 인코딩, 바이너리 코드설계 E 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5464729
- **Type**: conference
- **Published**: 17-19 Marc
- **Authors**: Yueqian Li, Masoud Salehi
- **PDF**: https://ieeexplore.ieee.org/document/5464729
- **Abstract**: We investigate quasi-cyclic low-density parity-check (QC-LDPC) codes for nonergodic block-fading channels. A construction method for designing QC-LDPC codes is presented. With careful design, the proposed QC-LDPC codes exhibit the same good performance as their corresponding random root- LDPC codes introduced in using iterative belief-propagation (BP) decoding. Moreover, the structure of the proposed QCLDPC codes makes an efficient encoding method possible.

## Static Address Generation Easing: a design methodology for parallel interleaver architectures

- **Status**: ✅
- **Reason**: 병렬 인터리버 메모리 collision-free 매핑 방법론, LDPC 디코더에 명시적 적용 — D HW 아키텍처 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5495535
- **Type**: conference
- **Published**: 14-19 Marc
- **Authors**: C. Chavet, P. Coussy, P. Urard +1
- **PDF**: https://ieeexplore.ieee.org/document/5495535
- **Abstract**: For high throughput applications, turbo-like iterative decoders are implemented with parallel architectures. However, to be efficient parallel architectures require to avoid collision accesses i.e. concurrent read/write accesses should not target the same memory block. This consideration applies to the two main classes of turbo-like codes which are Low Density Parity Check (LDPC) and Turbo-Codes. In this paper we propose a methodology which finds a collision-free mapping of the variables in the memory banks and which optimizes the resulting interleaving architecture. Finally, we show through a pedagogical example the interest of our approach compared to state-of-the-art techniques.
