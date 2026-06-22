# IEEE Xplore — 2014-02 (1차선별 통과)


## Array Convolutional Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: array LDPC 블록부호에서 출발한 신규 RTI-LDPC convolutional 부호 설계(제약길이 단축·최소거리 증가) — 이식 가능 코드 설계(E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6697911
- **Type**: journal
- **Published**: February 2
- **Authors**: Marco Baldi, Giovanni Cancellieri, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/6697911
- **Abstract**: This paper presents a design technique for obtaining regular time-invariant low-density parity-check convolutional (RTI-LDPCC) codes with low complexity and good performance. We start from previous approaches which unwrap a low-density parity-check (LDPC) block code into an RTI-LDPCC code, and we obtain a new method to design RTI-LDPCC codes with better performance and shorter constraint length. Differently from previous techniques, we start the design from an array LDPC block code. We show that, for codes with high rate, a performance gain and a reduction in the constraint length are achieved with respect to previous proposals. Additionally, an increase in the minimum distance is observed.

## Construction of Irregular QC-LDPC Codes via Masking with ACE Optimization

- **Status**: ✅
- **Reason**: 바이너리 QC-LDPC masking + ACE 최적화 구성으로 error-floor 개선 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6715252
- **Type**: journal
- **Published**: February 2
- **Authors**: Guojun Han, Yong Liang Guan, Lingjun Kong
- **PDF**: https://ieeexplore.ieee.org/document/6715252
- **Abstract**: Quasi-cyclic low-density parity-check (QC-LDPC) codes constructed by using algebraic approaches, such as finite geometry and finite field, generally have good structural properties and very low error-floors, and facilitate hardware implementation. Irregular QC-LDPC codes constructed from such QC-LDPC codes by using the masking technique, when decoded with the sum-product algorithm (SPA), have low decoding complexity, but often show early error-floors. In this paper, the relationship of cycle, girth and approximate cycle EMD (ACE) between the masking matrix and masked matrix is investigated, and the ACE algorithm is modified and used to construct the masking matrix for irregular QC-LDPC codes. Simulations demonstrate that the codes constructed by masking with ACE optimization exhibit much improved waterfall performance and lower error floors.

## High Throughput LDPC Decoder on GPU

- **Status**: ✅
- **Reason**: GPU 고처리량 LDPC 디코더 coalesced 메모리 접근 — 병렬화 HW 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6715256
- **Type**: journal
- **Published**: February 2
- **Authors**: Yong Lin, Wensheng Niu
- **PDF**: https://ieeexplore.ieee.org/document/6715256
- **Abstract**: The available Lower Density Parity Check (LDPC) decoders on Graphics Processing Unit (GPU) do not simultaneously read and write contiguous data blocks in memory because of the random nature of LDPC codes. One of these two operations has to be performed using noncontiguous accesses, resulting in long access time. To overcome this issue, we designed a multi-codeword parallel decoder with fully coalesced memory access. To test the performance of the method, we applied the method using an 8-bit compact data. The experimental results demonstrated that the method achieved more than 550Mbps throughput on Compute Unified Device Architecture (CUDA) enabled GPU.

## Efficient Progressive Edge-Growth Algorithm Based on Chinese Remainder Theorem

- **Status**: ✅
- **Reason**: PEG-CRT 베이스매트릭스 확장 LDPC 구성, on-the-fly HW 저장 이점 — 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6725573
- **Type**: journal
- **Published**: February 2
- **Authors**: Xueqin Jiang, Xiang-Gen Xia, Moon Ho Lee
- **PDF**: https://ieeexplore.ieee.org/document/6725573
- **Abstract**: Progressive edge-growth (PEG) algorithm construction builds a Tanner graph, or equivalently a parity-check matrix, for an LDPC code by establishing edges between the symbol nodes and the check nodes in an edge-by-edge manner and maximizing the girth in a greedy fashion. This approach is simple but the complexity of the PEG algorithm scale is O(nm), where n is the number of symbol nodes and m is the number of check nodes. We deal with this problem by construct a base matrix Hb of size mb × nb with the PEG algorithm and simultaneously expand this base matrix into a parity-check matrix H of size mx n via the the Chinese remainder theorem (CRT), where m ≫ mb and n ≥ nb. The size of the base matrix is expanded without decreasing the girth. For convenience, the PEG and CRT combined algorithm is referred to as the PEG-CRT algorithm in this paper. Since a smaller matrix is constructed with the PEG algorithm and the complexity of the CRT computation is negligible compared to the PEG algorithm, the complexity of the whole code construction process is reduced. Furthermore, the proposed algorithm has a potential advantage of saving storage space by storing a smaller matrix Hb and expanding it to H "on-the-fly" in hardware. The expanded matrix H preserves the important properties of base matrix such as large girth, flexible code rate and low density. The complexity analysis shows that the complexity of the PEG-CRT algorithm does not grow with the code length n. Simulation results show that compared with the PEG LDPC codes of length nb, the expanded PEG-CRT LDPC codes have better bit error rate (BER) performance with the iterative decoding. It is also shown that compared with PEG LDPC codes of length n, which constructed with higher complexities, the PEG-CRT codes have similar BER performance.

## Convergence of Weighted Min-Sum Decoding Via Dynamic Programming on Trees

- **Status**: ✅
- **Reason**: weighted min-sum/attenuated max-product 수렴성 분석, ML/LP 디코딩 보장 weight 조건 — min-sum 변형 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6661340
- **Type**: journal
- **Published**: Feb. 2014
- **Authors**: Yung-Yih Jian, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/6661340
- **Abstract**: Applying the max-product (and sum-product) algorithms to loopy graphs is now quite popular for best assignment problems. This is largely due to their low computational complexity and impressive performance in practice. Still, there is no general understanding of the conditions required for convergence or optimality of converged solutions or both. This paper presents an analysis of both attenuated max-product decoding and weighted min-sum decoding for low-density parity-check (LDPC) codes, which guarantees convergence to a fixed point when a weight factor, β, is sufficiently small. It also shows that, if the fixed point satisfies some consistency conditions, then it must be both a linear-programming (LP) and maximum-likelihood (ML) decoding solution. For (dv, dc)-regular LDPC codes, the weight factor must satisfy β(dv-1) <; 1 to guarantee convergence to a fixed point, whereas the results proposed by Frey and Koetter require instead that β(dv-1)(dc-1) ≤ 1. In addition, the range of the weight factor for a provable ML decoding solution is extended to 0 <; β(dv-1) 1. In addition, counterexamples that show a fixed point might not be the ML decoding solution if β(dv-1) > 1 are given. Finally, connections are explored with recent work on the threshold of LP decoding.

## Low complexity encoding algorithm of RS-based QC-LDPC codes

- **Status**: ✅
- **Reason**: RS기반 QC-LDPC 저복잡도 인코딩(LFSR HW); 바이너리 LDPC 인코더 HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6804249
- **Type**: conference
- **Published**: 9-14 Feb. 
- **Authors**: Mu Zhang, Li Tang, Qin Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/6804249
- **Abstract**: This paper presents a novel encoding algorithm for QC-LDPC codes constructed from Reed-Solomon codes. The encoding is performed in the transform domain via Galois Fourier transformation. Message bits are encoded in sections corresponding to sub-matrices of the parity-check matrix in the transform domain. Because of the structure of the parity-check matrices of these LDPC codes, the encoding can be easily implemented with some linear-feedback shift registers, thus efficiently reduces the hardware cost.

## Decoding of quasi-cyclic LDPC codes with section-wise cyclic structure

- **Status**: ✅
- **Reason**: QC-LDPC section-wise cyclic 구조 기반 저복잡도 디코딩+HW 절감, error-floor 개선(C/D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804221
- **Type**: conference
- **Published**: 9-14 Feb. 
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6804221
- **Abstract**: Presented in this paper is a reduced-complexity iterative decoding scheme for quasi-cyclic (QC) LDPC codes. This decoding scheme is devised based on the section-wise cyclic structure of the parity-check matrix of a QC-LDPC code. Using this decoding scheme, the hardware implementation complexity of a QC-LDPC decoder can be significantly reduced without performance degradation. A high-rate QC-LDPC code that can achieve a very low error-rate without a visible error-floor is used to demonstrate the effectiveness of the proposed decoding scheme. Also presented in this paper are two other high-rate QC-LDPC codes and a method for constructing rate -1/2 QC-LDPC codes whose Tanner graphs have girth 8. All the codes constructed perform well with low error-floor using the proposed decoding scheme.

## Check-hybrid GLDPC codes without small trapping sets

- **Status**: ✅
- **Reason**: GLDPC 트래핑셋 제거 위해 단일체크를 슈퍼체크로 변환하는 신규 코드설계(E), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804215
- **Type**: conference
- **Published**: 9-14 Feb. 
- **Authors**: Vida Ravanmehr, David Declercq, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/6804215
- **Abstract**: In this paper, we propose a new approach to construct a class of check-hybrid generalized low-density parity-check (GLDPC) codes which are free of small trapping sets. The approach is based on converting some selected check nodes involving a trapping set to super checks corresponding to a shorter error-correcting component code. Specifically, we follow two main purposes to construct the check-hybrid codes: First, replacing single parity checks by super checks is done based on the knowledge of the trapping sets of the global LDPC code. We show that by converting some single checks to super checks in a trapping set, the decoder corrects the errors on a trapping set and hence eliminates the trapping set. Second, the rate-loss caused by replacing the super checks is reduced through finding the minimum number of such critical checks. We first present an algorithm to find possible critical checks in a trapping set. We then provide some upper bounds on the minimum number of such critical checks such that the decoder corrects all error patterns on certain trapping sets in the Tanner graph of the global LDPC code. We also provide a potential fixed set for a class of constructed check-hybrid codes.

## LDPC code designs based on √I matrices

- **Status**: ✅
- **Reason**: √I 행렬 기반 LDPC 구성 및 효율적 인코딩 구조 신규 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804247
- **Type**: conference
- **Published**: 9-14 Feb. 
- **Authors**: Shayan G. Srinivasa
- **PDF**: https://ieeexplore.ieee.org/document/6804247
- **Abstract**: LDPC codes can be constructed by tiling permutation matrices that belong to the square root of identity type and similar algebraic structures. We investigate into the properties of such codes. We also present code structures that are amenable for efficient encoding.

## Unconventional behavior of the noisy min-sum decoder over the binary symmetric channel

- **Status**: ✅
- **Reason**: noisy min-sum 디코더 거동 분석, density evolution; min-sum 변형/디코더 분석 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6804283
- **Type**: conference
- **Published**: 9-14 Feb. 
- **Authors**: Christiane L. Kameni Ngassa, Valentin Savin, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6804283
- **Abstract**: This paper investigates the behavior of the noisy Min-Sum decoder over binary symmetric channels. A noisy decoder is a decoder running on a noisy device, which may introduce errors during the decoding process. We show that in some particular cases, the noise introduce by the device can help the Min-Sum decoder to escape from fixed points attractors, and may actually result in an increased correction capacity with respect to the noiseless decoder. We also reveal the existence of a specific threshold phenomenon, referred to as functional threshold. The behavior of the noisy decoder is demonstrated in the asymptotic limit of the code-length, by using “noisy” density evolution equations, and it is also verified in the finite-length case by Monte-Carlo simulation.

## 27.6 An 821MHz 7.9Gb/s 7.3pJ/b/iteration charge-recovery LDPC decoder

- **Status**: ✅
- **Reason**: 576b LDPC 디코더 테스트칩(charge-recovery logic, 65nm) — 에너지효율 디코더 HW 아키텍처, NAND LDPC에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6757514
- **Type**: conference
- **Published**: 9-13 Feb. 
- **Authors**: Tai-Chuan Ou, Zhengya Zhang, Marios C. Papaefthymiou
- **PDF**: https://ieeexplore.ieee.org/document/6757514
- **Abstract**: This paper presents a 576b LDPC decoder test-chip designed using a charge-recovery logic family. The chip has been fabricated in a 65nm CMOS process and relies on 16 integrated inductors to achieve energy-efficient operation by recovering charge from gate fanouts. When self-oscillating at 821MHz, the chip recovers 51.4% of the energy supplied to it. In terms of device count, this chip is more than an order of magnitude larger than the largest previously-reported chips with charge-recovery logic [3-4]. When operating at 821MHz, it achieves a 7.9Gb/s throughput at 7.3pJ/b/iteration, improving on results in [1-2,5] by at least 1.7× in energy efficiency and 2.3× in area efficiency.

## 27.7 A scalable 1.5-to-6Gb/s 6.2-to-38.1mW LDPC decoder for 60GHz wireless networks in 28nm UTBB FDSOI

- **Status**: ✅
- **Reason**: 802.11ad LDPC 디코더(28nm FDSOI) — approximate marginalization 등 신규 디코더 기법+HW 아키텍처, 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6757515
- **Type**: conference
- **Published**: 9-13 Feb. 
- **Authors**: Matthew Weiner, Milovan Blagojevic, Sergey Skotnikov +3
- **PDF**: https://ieeexplore.ieee.org/document/6757515
- **Abstract**: Low-density parity-check (LDPC) codes in modern wireless communications are rate- and throughput-scalable, and despite their complexity, decoding them requires low power consumption. The IEEE 802.11ad standard for Gb/s wireless LANs in the 60GHz band requires an implementation of an LDPC encoder/decoder with throughputs of 1.5, 3, and 6Gb/s, with code rates of 1/2, 5/8, 3/4 and 13/16 [1]. Previous implementations of decoders for these throughputs and levels of reconfiguration have power consumptions on the order of the rest of the baseband processing [2,3]. This paper presents a fully compatible IEEE 802.11ad LDPC decoder in 28nm ultra-thin body and BOX fully-depleted SOI (UTBB FDSOI) technology with a power consumption that is a small fraction of the total baseband power. To achieve this, the decoder introduces an approximate marginalization technique and a simplified reconfiguration method. Forward body biasing of FDSOI technology allows for minimum energy consumption across all decoding modes.

## Coding and signal processing for ultra-high density magnetic recording channels

- **Status**: ✅
- **Reason**: 고밀도 자기기록용 신규 LDPC 코드설계 패러다임 제시, 바이너리 LDPC 코드설계 이식 가능성(E) 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6785330
- **Type**: conference
- **Published**: 3-6 Feb. 2
- **Authors**: Yong Liang Guan, Guojun Han, Lingjun Kong +3
- **PDF**: https://ieeexplore.ieee.org/document/6785330
- **Abstract**: New magnetic recording technologies such as bit-patterned media recording (BPMR), heat (or microwave) assisted magnetic recording (HAMR) and shingled writing (SW)/two-dimensional magnetic recording (TDMR) have been proposed to push the storage density of future hard disks beyond 1Tb/in2. However, at such high recording density, many new challenges from the magnetic recording medium, read/write head as well as writing and reading channels arise. These challenges hinder the realization of Tb/in2 hard disks and should be addressed. In this paper, we review these major challenges from a communication theory perspective, and propose ways to mitigate the channel impairments by using low-complexity two-dimensional (2D) channel detection, new low-density parity-check (LDPC) code design paradigm, as well as re-synchronizable coding schemes.

## Generalized Belief Propagation to break trapping sets in LDPC codes

- **Status**: ✅
- **Reason**: GBP로 trapping set 제거하는 BP+GBP 하이브리드 디코더, error-floor 개선 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6766441
- **Type**: conference
- **Published**: 3-5 Feb. 2
- **Authors**: J. C. Sibel, S. Reynal, D. Declercq
- **PDF**: https://ieeexplore.ieee.org/document/6766441
- **Abstract**: In this paper, we focus on the Generalized Belief Propagation (GBP) algorithm to solve trapping sets in Low-Density Parity-Check (LDPC) codes. Trapping sets are topological structures in Tanner graphs of LDPC codes that are not correctly decoded by Belief Propagation (BP), leading to exhibit an error-floor in the Bit-Error Rate (BER). Stemming from statistical physics of spin glasses, GBP consists in passing messages between clusters of Tanner graph nodes in another graph called the region-graph. Here, we introduce a specific clustering of nodes, based on a novel local loopfree principle, that breaks trapping sets such that the resulting region-graph is locally loopfree. We then construct a hybrid decoder made of BP and GBP that proves to be a powerful decoder as it clearly improves the BER and defeats the error-floor.

## Implementation of a low power LDPC decoder using bit serial architecture

- **Status**: ✅
- **Reason**: 비트직렬 LDPC 디코더 HW + min-sum check update 신규 근사 — 이식 가능 디코더/HW(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7034089
- **Type**: conference
- **Published**: 27-28 Feb.
- **Authors**: M. Revathy, R. Saravanan
- **PDF**: https://ieeexplore.ieee.org/document/7034089
- **Abstract**: A bit serial architecture is used which reduces the interconnect complexity in fully parallel low density parity check (LDPC) decoder. This can achieve better error correcting performance when the code length is moderate. By using a new approximation to the check update function in the Minsum decoding algorithm, the implementation is simplified. This new check update rule finds only the absolute minimum magnitude of the incoming message and if required correction is made to the outgoing messages. The proposed decoder is designed using Verilog HDL, simulated using MODELSEVI 5.7g, synthesized by Xilinx 9.2i and implemented using Spartan 3E. The result shows that the proposed architecture requires fewer slices and LUT's when compared with the existing methods.

## A novel QC-LDPC code with flexible construction and low error floor

- **Status**: ✅
- **Reason**: 신규 QC-LDPC 구성(SRW-QC-LDPC): 4-cycle 제거·degree-2 감소로 error floor 개선 — 바이너리 코드설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6778997
- **Type**: conference
- **Published**: 16-19 Feb.
- **Authors**: Hanxin Wang, Shaoping Chen, Cuitao Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/6778997
- **Abstract**: Slide rectangular window structure for QC-LDPC codes (SRW-QC-LDPC) with flexible code lengths and code rates is proposed, which aim to eliminate the cycles of length 4 without computer search. The parity-check matrix would have different extension factors and structures by using the slide rectangular window in the base matrix, the degree distribution is optimized by the optimal diagonal method. Because the dual-diagonal structure with many variable nodes of degree-2 may lead to high error floor, SRW-QC-LDPC codes with quasi tri-diagonal structure are also proposed by changing the location of the third diagonal to partly eliminate variable nodes of degree-2 for lower error floor. Simulation results show that SRW-QC-LDPC codes with quasi tri-diagonal structure can not only flexibly expand the code lengths and code rates but also reduce the encoding complexity and improve the BER performance compared to quasi dual-diagonal structure in IEEE802.16e QC-LDPC codes. The novel QC-LDPC codes are available and suitable for the adaptive transmission systems and hardware implementation.

## Performance investigation of reduced complexity bit-flipping using variable thresholds and noise perturbation

- **Status**: ✅
- **Reason**: 저복잡도 bit-flipping 변형: 가변 임계값 다중분기+노이즈 섭동으로 stuck 탈출 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6779175
- **Type**: conference
- **Published**: 16-19 Feb.
- **Authors**: Julian Webber, Toshihiko Nishimura, Takeo Ohgane +1
- **PDF**: https://ieeexplore.ieee.org/document/6779175
- **Abstract**: The near Shannon capacity approaching low-density parity-check (LDPC) linear block codes are now in widespread use in modern systems including the long term evolution advanced (LTE-A) cellular, 802.11η Wi-Fi and DVB-S2 satellite communications standards. The decoders based on the iterative belief propagation algorithm provide near optimum performance but also have very high computational complexity. Therefore significant research has recently focused on reduced complexity architectures based on the group of so-called bit-flipping algorithms. In the basic bit-flipping algorithm the number of failed parity checks for each bit is computed and the bit with the maximum failed parity checks is inverted. Inverting bits above a certain threshold removes the complexity involved with a maximum-search and, adaptive thresholds on each bit can further reduce the computation overhead. The criterion for the threshold update affects the error and convergence performances. Here, we describe a low-complexity architecture that has two (or more) decoder branches each with a different threshold scaling factor and select the threshold and bits at each iteration from the branch with the lowest syndrome sum. We then investigate the effect of adding a random Uniform or Gaussian noise perturbation to the threshold in order to reduce the average iteration count further in order to provide the opportunity to escape from stuck decoding states.

## Over-clocked SSD: Safely running beyond flash memory chip I/O clock specs

- **Status**: ✅
- **Reason**: NAND 플래시 SSD에서 ECC 여유분을 활용해 I/O 오버클럭, NAND 직접 응용(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6835962
- **Type**: conference
- **Published**: 15-19 Feb.
- **Authors**: Kai Zhao, Kalyana S. Venkataraman, Xuebin Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/6835962
- **Abstract**: This paper presents a design strategy that enables aggressive use of flash memory chip I/O link over-clocking in solid-state drives (SSDs) without sacrificing storage reliability. The gradual wear-out and process variation of NAND flash memory makes the worst-case oriented error correction code (ECC) in SSDs largely under-utilized most of the time. This work proposes to opportunistically leverage under-utilized error correction strength to allow error-prone flash memory I/O link over-clocking. Its rationale and key design issues are presented and studied in this paper, and its potential effectiveness has been verified through hardware experiments and system simulations. Using sub-22nm NAND flash memory chips with I/O specs of 166MBps, we carried out extensive experiments and show that the proposed design strategy can enable SSDs safely operate with error-prone I/O link running at 275MBps. Trace-driven SSD simulations over a variety of workload traces show the system read response time can be reduced by over 20%.
