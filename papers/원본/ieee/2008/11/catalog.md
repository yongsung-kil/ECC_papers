# IEEE Xplore — 2008-11


## LDPC Code Design for Half-Duplex Cooperative Relay

- **Status**: ✅
- **Reason**: rate-compatible 바이너리 LDPC 코드설계+수정 가우시안근사 density evolution+미분진화 최적화로 코드설계(E) 이식 가능
- **ID**: ieee:4686837
- **Type**: journal
- **Published**: November 2
- **Authors**: Chuxiang Li, Guosen Yue, Xiaodong Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/4686837
- **Abstract**: The authors consider the design of LDPC codes for cooperative relay systems in the half-duplex mode. The capacity of halfduplex relay channels has been studied previously but the design of good channel codes for such channels remains a challenging problem. Employing an efficient relay protocol, we transform the half-duplex relay code design problem into a problem of ratecompatible LDPC code design where different code segments experience different SNRs. The density evolution with conventional Gaussian approximation for single user channels, which assumes invariant SNR within one codeword, is not capable of accurately predicting the code performance for this system. Here we develop a density evolution with a modified Gaussian approximation that takes into account the SNR variation in one received codeword as well as the rate-compatibility constraint. We then optimize the code ensemble using a modified differential evolution procedure. Extensive simulations are carried out to demonstrate that the proposed algorithm offers more accurate prediction of code performance in half-duplex relay channels than the conventional methods, and the optimized codes achieve a significant gain over existing codes.

## CRC-assisted error correction in a convolutionally coded system

- **Status**: ❌
- **Reason**: CRC+CC 시스템의 소프트 신드롬/IDD 디코딩으로 비-LDPC 부호 기반이며 LDPC BP로 이식할 새 기법 없음
- **ID**: ieee:4686263
- **Type**: journal
- **Published**: November 2
- **Authors**: Renqiu Wang, Wanlun Zhao, Georgios B. Giannakis
- **PDF**: https://ieeexplore.ieee.org/document/4686263
- **Abstract**: In communication systems employing a serially concatenated cyclic redundancy check (CRC) code along with a convolutional code (CC), erroneous packets after CC decoding are usually discarded. The list Viterbi algorithm (LVA) and the iterative Viterbi algorithm (IVA) are two existing approaches capable of recovering erroneously decoded packets. We here employ a soft decoding algorithm for CC decoding, and introduce several schemes to identify error patterns using the posterior information from the CC soft decoding module. The resultant iterative decoding-detecting (IDD) algorithm improves error performance by iteratively updating the extrinsic information based on the CRC parity check matrix. Assuming errors only happen in unreliable bits characterized by small absolute values of the log-likelihood ratio (LLR), we also develop a partial IDD (P-IDD) alternative which exhibits comparable performance to IDD by updating only a subset of unreliable bits. We further derive a soft-decision syndrome decoding (SDSD) algorithm, which identifies error patterns from a set of binary linear equations derived from CRC syndrome equations. Being noniterative, SDSD is able to estimate error patterns directly from the decoder output. The packet error rate (PER) performance of SDSD is analyzed following the union bound approach on pairwise errors. Simulations indicate that both IDD and IVA are better tailored for single parity check (PC) codes than for CRC codes. SDSD outperforms both IDD and LVA with weak CC and strong CRC. Applicable to AWGN and flat fading channels, our algorithms can also be extended to turbo coded systems.

## Optimizing Joint Erasure- and Error-Correction Coding for Wireless Packet Transmissions

- **Status**: ❌
- **Reason**: 패킷 단위 erasure/error 결합코딩 자원배분 최적화로 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4686840
- **Type**: journal
- **Published**: November 2
- **Authors**: Christian R. Berger, Shengli Zhou, Yonggang Wen +2
- **PDF**: https://ieeexplore.ieee.org/document/4686840
- **Abstract**: To achieve reliable packet transmission over a wireless link without feedback, we propose a layered coding approach that uses error-correction coding within each packet and erasure-correction coding across the packets. This layered approach is also applicable to an end-to-end data transport over a network where a wireless link is the performance bottleneck. We investigate how to optimally combine the strengths of error- and erasure-correction coding to optimize the system performance with a given resource constraint, or to maximize the resource utilization efficiency subject to a prescribed performance. Our results determine the optimum tradeoff in splitting redundancy between error-correction coding and erasure-correction codes, which depends on the fading statistics and the average signal to noise ratio (SNR) of the wireless channel. For severe fading channels, such as Rayleigh fading channels, the tradeoff leans towards more redundancy on erasure-correction coding across packets, and less so on error-correction coding within each packet. For channels with better fading conditions, more redundancy can be spent on error-correction coding. The analysis has been extended to a limiting case with a large number of packets, and a scenario where only discrete rates are available via a finite number of transmission modes.

## Reduced front-end reception requirements for satellite broadcast using interference processing

- **Status**: ❌
- **Reason**: 위성 수신 안테나 간섭처리로 LDPC ECC와 무관
- **ID**: ieee:4711201
- **Type**: journal
- **Published**: November 2
- **Authors**: Enrico Casini, Gennaro Gallinaro, Joel Grotz
- **PDF**: https://ieeexplore.ieee.org/document/4711201
- **Abstract**: The problem of fixed satellite broadcast reception is considered. The possibility of reducing the requirements on the antenna front-end dimensions is investigated. Interference processing and mitigation techniques are employed to cope with the increased level of adjacent system interference at the satellite broadcast receiver resulting from the less directive antenna. A novel satellite reception front-end antenna based on a multiple input receiver is proposed to adapt the interference processing methods to the broadcast reception scenario. The potential performance of the devised scheme is thoroughly discussed and assessed by extensive software simulations.

## Nonbinary LDPC Codes for 4-kB Sectors

- **Status**: ❌
- **Reason**: nonbinary(GF q) LDPC 코드로 비이진 LDPC는 제외 대상
- **ID**: ieee:4717467
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Wu Chang, J. R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/4717467
- **Abstract**: The performance of nonbinary LDPC codes on perpendicular magnetic recording channels (PMRCs) with 4-kB sectors is investigated. Each sector is encoded by either 4- or 0.5-kB-long codes. Both quasi-cyclic (QC) and nonquasi-cyclic (non-QC) nonbinary low-density parity-check (LDPC) codes are designed, and a set of simulations in a mixture of 10% additive white Gaussian noise (AWGN) and 90% position jitter noise power, with and without turbo equalization and with a rereading technique, is presented. The results show that sector-long codes perform better than 0.5-kB codes for all decoding schemes considered. In addition, the erasure correction capabilities of these nonbinary LDPC codes are calculated under both maximum-likelihood decoding and iterative decoding, and, as expected, longer codes can correct longer erasures. QC and non-QC nonbinary LDPC codes exhibit similar performance and have almost the same erasure correction capability under iterative decoding. Because of their efficient encoding, QC nonbinary LDPC codes are a good choice for perpendicular recording channels with 4-kB sectors, and offer a tradeoff between performance and code length.

## A New Burst Detection Scheme Using Parity Check Matrix of LDPC Code for Bit Flipping Burst-like Signal Degradation

- **Status**: ✅
- **Reason**: LDPC 패리티검사행렬을 이용한 신규 버스트 검출 기법 - 떼어낼 수 있는 BP/디코딩 보조 기법(C)
- **ID**: ieee:4717796
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Yasuaki Nakamura, Mitsuhiro Nishimura, Yoshihiro Okamoto +2
- **PDF**: https://ieeexplore.ieee.org/document/4717796
- **Abstract**: In this paper, a new burst detection method using the check matrix of low-density parity-check (LDPC) code is proposed. The burst detection for the bit flipping burst-like signal degradation which the conventional burst detection using a reproducing waveform, an equalizer output, an a posteriori probability (APP) decoder output and so on cannot detect is studied. The performance of the LDPC coding and iterative decoding system with the proposed burst detector is evaluated by computer simulation for a perpendicular magnetic recording channel with bit flipping burst-like signal degradation, and it is compared with that of the RS encoding and decoding system using the erasure correction. The results show that the LDPC coding and iterative decoding system with our burst detector shows the better performance and has the resistance to the bit flipping burst-like signal degradation of about 1500 bits.

## Fully Parallel Stochastic LDPC Decoders

- **Status**: ✅
- **Reason**: fully parallel stochastic 바이너리 LDPC 디코더 FPGA 아키텍처로 디코더(C)+HW(D) 이식 가능
- **ID**: ieee:4602535
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Saeed Sharifi Tehrani, Shie Mannor, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/4602535
- **Abstract**: Stochastic decoding is a new approach to iterative decoding on graphs. This paper presents a hardware architecture for fully parallel stochastic low-density parity-check (LDPC) decoders. To obtain the characteristics of the proposed architecture, we apply this architecture to decode an irregular state-of-the-art (1056,528) LDPC code on a Xilinx Virtex-4 LX200 field-programmable gate-array (FPGA) device. The implemented decoder achieves a clock frequency of 222 MHz and a throughput of about 1.66 Gb/s at  $E_{b}/N_{0}={\hbox {4.25~dB}}$ (a bit error rate of $10^{-8}$). It provides decoding performance within 0.5 and 0.25 dB of the floating-point sum-product algorithm with 32 and 16 iterations, respectively, and similar error-floor behavior. The decoder uses less than 40% of the lookup tables, flip-flops, and IO ports available on the FPGA device. The results provided in this paper validate the potential of stochastic LDPC decoding as a practical and competitive fully parallel decoding approach.

## Average Stopping Set Weight Distributions of Redundant Random Ensembles

- **Status**: ✅
- **Reason**: redundant random ensemble의 stopping set 분포 분석으로 BEC BP 성능과 error floor 관련 바이너리 LDPC 코드설계(E) 통찰 가능
- **ID**: ieee:4655474
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/4655474
- **Abstract**: In this paper, redundant random ensembles are defined and their average stopping set (SS) weight distributions are analyzed. A redundant random ensemble consists of a set of binary matrices with linearly dependent rows. These linearly dependent rows significantly reduce the number of stopping sets (SS) of small size. Upper and lower bounds on the average SS weight distribution of the redundant random ensembles are proved based on a combinatorial argument. Asymptotic forms of these bounds reveal asymptotic behavior of the average SS weight distributions. From these bounds, a tradeoff between the number of redundant rows (corresponding to decoding complexity of belief propagation on binary erasure channel) and the average SS weight distribution (corresponding to decoding performance) can be derived.

## New List Sphere Decoding (LSD) and Iterative Synchronization Algorithms for MIMO-OFDM Detection With LDPC FEC

- **Status**: ❌
- **Reason**: MIMO-OFDM의 sphere/list 검출기 및 동기화로 LDPC는 FEC 베이스라인일 뿐 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:4451656
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Ahmed D. Kora, Amir Saemi, Jean Pierre Cances +1
- **PDF**: https://ieeexplore.ieee.org/document/4451656
- **Abstract**: New sphere decoding and synchronization algorithms for multiple-input-multiple-output (MIMO) orthogonal frequency-division multiplexing (OFDM) systems are proposed in this paper. In particular, an iterative list branch-and-bound (BB) algorithm based on the basic BB algorithm is described to obtain a candidate list to compute soft information that is used in the iterative detector. Furthermore, an improved algorithm that uses prior information from the preceding iteration to calculate the lower bound is proposed, and the candidate list is updated every iteration. To obtain a complete modem architecture, we propose an efficient expectation-maximization (EM)-based iterative algorithm for synchronization and channel estimation to interface with the proposed list-sphere-decoding detector, and we investigate the performance of the designed MIMO-OFDM modem on a realistic fading channel. The obtained performance results show that it is possible to practically design a performing MIMO-OFDM modem with high spectral efficiency, i.e., 8 bit/s/Hz with a 4times4 16-QAM MIMO-OFDM system.

## Areal-Density Capability of a Magnetic Recording System Using a “747” Test Based Only on Data-Block Failure-Rate

- **Status**: ❌
- **Reason**: 자기기록 면밀도 측정(747 테스트) 방법론. LDPC ECC 디코더/구성/HW 기여 없음
- **ID**: ieee:4717668
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Zhen Jin, Michael Salo, Roger Wood
- **PDF**: https://ieeexplore.ieee.org/document/4717668
- **Abstract**: The ldquo747rdquo test provides a well-established basis for determining the areal-density capability of a magnetic recording system. When new record areal densities are announced, they are usually accompanied by a 747 plot to support the claim. The 747 curve plots how far the read-head can be moved off-track versus the distance to an adjacent ldquosqueezingrdquo track. The criterion for off-track failure is defined as a threshold on raw error-rate, e.g., 1-bit error per 1000 customer bits. There are two concerns with this approach. First, the raw error rate from the readback channel is not the final measure of performance and may vary from channel to channel or, for next generation channels, may not even be defined. Second, the areal densities achieved are usually quoted exclusive of the necessary error correction code (ECC) overhead. So there is no credit given for channels that require little or no ECC. This paper describes the traditional 747 test and then a modification of that test that relies only on measuring the final data-block failure rate. Also, the proposed new definition requires that the resulting areal-densities be quoted inclusive of any added ECC overhead.

## The Read Channel

- **Status**: ❌
- **Reason**: 자기기록 read channel 서베이로 구체적 신규 LDPC 디코더/구성/HW 기여 없는 튜토리얼
- **ID**: ieee:4694140
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Aleksandar Kavcic, Ara Patapoutian
- **PDF**: https://ieeexplore.ieee.org/document/4694140
- **Abstract**: In this paper, we provide a survey of the novel read channel technologies that found their implementation in products over the past decade, and we outline possible technology directions for the future of read channels. Recently, magnetic recording read channels have undergone several changes. In addition to switching from longitudinal to perpendicular recording channels, detectors tuned to media noise sources are now readily implemented in read channel chips. Powerful numerical techniques have emerged to evaluate the capacity of the magnetic recording channel. Further, improved coding/decoding methods have surfaced both for the incumbent Reed–Solomon codes and the promising low-density parity-check codes. The paper is a tutorial-like survey of these emerging technologies with the aim to propel the reader to the forefront of research and development in the areas of signal processing and coding for magnetic recording channels.

## Fixed-Rate Raptor Codes Over Rician Fading Channels

- **Status**: ❌
- **Reason**: Raptor(fountain) 부호로 비-LDPC, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:4490159
- **Type**: journal
- **Published**: Nov. 2008
- **Authors**: Bharathram Sivasubramanian, Harry Leib
- **PDF**: https://ieeexplore.ieee.org/document/4490159
- **Abstract**: This paper considers the newly introduced fountain codes for fixed-rate error control coding, with emphasis on Raptor codes. The performance of Raptor codes of low-to-moderate rates with iterative decoding is evaluated over memoryless, as well as correlated, fading channels. A global decoding algorithm, incorporating feedback between the component codes of the Raptor code, is introduced. Results show that fixed-rate Raptor codes closely approach the capacity limits of memoryless channels. It is also shown that Raptor codes incur a performance degradation over slow-fading channels relative to memoryless fading. Comparison with other state-of-the-art codes reveals that fixed-rate Raptor codes deliver performance that is comparable with, or better than, several high-performance schemes over both memoryless and correlated fading channels.

## Increasing optical fiber transmission capacity beyond next-generation systems

- **Status**: ❌
- **Reason**: 광섬유 전송용량 증대 일반 논의, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4688764
- **Type**: conference
- **Published**: 9-13 Nov. 
- **Authors**: Ezra Ip, Joseph M. Kahn
- **PDF**: https://ieeexplore.ieee.org/document/4688764
- **Abstract**: We discuss how improvements in optical fibers and amplifiers, modulation formats, and digital signal processing algorithms can increase the capacity of long-haul fiber-optic transmission beyond that of next-generation systems.

## A reconfigurable FPGA implementation of an LDPC decoder for unstructured codes

- **Status**: ✅
- **Reason**: D/C: FPGA LDPC 디코더 HW + min-sum with correction factor 변형, NAND 이식 가능
- **ID**: ieee:4746952
- **Type**: conference
- **Published**: 7-9 Nov. 2
- **Authors**: S. M. Ehsan Hosseini, Kheong Sann Chan, Wang Ling Goh
- **PDF**: https://ieeexplore.ieee.org/document/4746952
- **Abstract**: This paper describes the implementation of a general and embedded decoder for the evaluation of unstructured low-density parity-check (LDPC) codes over additive-white Gaussian noise (AWGN) channels. The decoder, which has a serial architecture and moderate throughput, is a peripheral connected to the embedded Power PC processor of a Xilinx Virtex-II Pro FPGA and is managed by the processor. This method of hardware/software implementation provides the maximum flexibility for the development and rapid prototyping of the hardware-based simulator system. The decoding algorithm proposed in this paper belongs to the class of min-sum with correction factor in which the correction factor updates with the log-likelihood ratio (LLR) values.

## A 7.39mm2 76mW (1944, 972) LDPC decoder chip for IEEE 802.11n applications

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 칩의 Group Comparison·Dynamic Wordlength·Data Packet 기법으로 면적·처리량 개선 — 이식 가능 HW(D)
- **ID**: ieee:4708787
- **Type**: conference
- **Published**: 3-5 Nov. 2
- **Authors**: Xin-Yu Shih, Cheng-Zhou Zhan, An-Yeu Wu
- **PDF**: https://ieeexplore.ieee.org/document/4708787
- **Abstract**: This paper presents the LDPC decoder chip for (1944,972) QC-LDPC codes in IEEE 802.11n communication system. The efficient LDPC decoder chip is designed with three design techniques, including Group Comparison (GC), Dynamic Wordlength Assignment (DWA), and Data Packet Scheme (DPS). When the target BER is 10−6, the decoding performance can be improved by the coding gain of 0.48 dB and 0.63 dB with respect to (4,3) and (3,2) fixed-point NMSA, respectively. In addition, the total decoder design area can be reduced by 25% and the decoding throughput can be enhanced by 3X times with respect to conventional direct-mapping method. By using TSMC 0.13um VLSI technology, the core area and die size are only 3.88 mm2 and 7.39 mm2, respectively. The maximum operating frequency is measured at 111.1MHz and the power dissipation is only 76 mW.

## A 820 Mb/s baseband processor LSI based on LDPC coded OFDM for UWB systems

- **Status**: ❌
- **Reason**: UWB용 LDPC-OFDM 베이스밴드 LSI, 시스템 통합 칩으로 떼어낼 신규 디코더/HW 기법 불명확 (무선 응용 특이적)
- **ID**: ieee:4708786
- **Type**: conference
- **Published**: 3-5 Nov. 2
- **Authors**: Shinsuke Ushiki, Koichi Nakamura, Kazunori Shimizu +4
- **PDF**: https://ieeexplore.ieee.org/document/4708786
- **Abstract**: This paper presents a high-throughput and highly-reliable baseband processor LSI based on LDPC coding OFDM UWB. This LSI targets for wireless LAN systems inside a car which enable to translate a high-resolution video under noisy environment. A chip capable of operating at 147 MHz was fabricated using UMC 0.13 mum 1P8M CMOS technology. By adopting the OFDM modulation with 1024 sub-carriers, it achieves a throughput of 820 Mb/s and 10-4 BER performance under 30 dB CNR with 5/6 coding rate. Power dissipation is 189 mW/391 mW (TX/RX).

## Asymmetric quantum BCH codes

- **Status**: ❌
- **Reason**: 비대칭 양자 BCH/RS 부호 — 양자 EC + 비-LDPC, 원칙 제외
- **ID**: ieee:4772987
- **Type**: conference
- **Published**: 25-27 Nov.
- **Authors**: Salah A. Aly
- **PDF**: https://ieeexplore.ieee.org/document/4772987
- **Abstract**: Recently, the theory of quantum error control codes has been extended to include quantum codes over asymmetric quantum channels - qubit-flip and phase-shift errors may have equal or different probabilities. Previous work in constructing quantum error control codes has focused on code constructions for symmetric quantum channels. In this paper we establish a method to construct asymmetric quantum codes based on classical codes. We derive, once again, families of asymmetric quantum codes from classical BCH and RS codes over finite fields. Particularly, we present interesting asymmetric quantum codes based on nonprimitive narrow-sense BCH codes with parameters [[n, k, dz/dx]]q for certain values of code lengths, dimensions, and various minimum distance. Finally, our constructions are well explained by an illustrative example.

## Low complexity iterative decoding algorithm for low-density parity-check (LDPC) codes

- **Status**: ✅
- **Reason**: RRWBF 비트플립 변형(반복수 절감) - 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:4812877
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: Hany R. Zeidan, Maha M. Elsabrouty
- **PDF**: https://ieeexplore.ieee.org/document/4812877
- **Abstract**: The reliability ratio weighted based bit-flipping (RRWBF) algorithm for decoding low-density parity-check (LDPC) codes has recently been developed to provide the best performance among all existing bit-flipping based algorithms. The implementation efficient reliability ratio weighted based bit-flipping (IERRWBF) algorithm speedup the original algorithm to decrease the processing time used. A drawback for this algorithm is the decrease in the improvement as the maximum number of iterations assigned for the algorithm increase as a large percentage of decoding time is spent on the iteration part without any change in the performance. In this paper, a modified version for this algorithm is proposed to solve this drawback by reducing the number of iterations required to achieve the same performance of the existing IERRWBF algorithm using efficient number of iterations instead of using the maximum number of iterations for decoding without any change in the performance of the IERRWBF.

## Decoding architectures for Projective Geometry based LDPC codes

- **Status**: ✅
- **Reason**: PG-LDPC 병렬/반병렬 디코더 아키텍처(BP+MLD 재구성) - HW 아키텍처(D)
- **ID**: ieee:4812880
- **Type**: conference
- **Published**: 24-27 Nov.
- **Authors**: S.G Harihara, M. Girish Chandra, Tarakapraveen Uppalapati +1
- **PDF**: https://ieeexplore.ieee.org/document/4812880
- **Abstract**: Projective Geometry (PG) based Low Density Parity Check (LDPC) codes have many useful properties, including easy encoding and decoding by simple majority logic technique. With these useful features, they can be useful error control codes in future. In this paper, we present three novel architectures comprising of one parallel and two semi-parallel decoder architectures for popular PG-based LDPC codes. These architectures have no memory clash and further are reconfigurable for different lengths (and their corresponding rates). The three architectures can be configured either for the regular belief propagation based decoding or majority logic decoding (MLD).

## New sum-product algorithm using approximation method for low complexity LDPC decoding

- **Status**: ✅
- **Reason**: C: sum-product 근사(곱셈→덧셈, 양자화 테이블)로 저복잡도 LDPC 디코더 기법 이식 가능
- **ID**: ieee:4815676
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Jae Hee Han, Myung Hoon Sunwoo
- **PDF**: https://ieeexplore.ieee.org/document/4815676
- **Abstract**: This paper proposes a new sum-product algorithm to improve BER performance for low-density parity-check codes. The proposed algorithm can replace multiplications and divisions with additions and subtractions by adding the logarithmic and exponential functions. In addition, the proposed algorithm can simplify both the ln[tanh(x)] and tanh-1[exp(x)] functions by using two quantization tables which can reduce tremendous computational complexity. Moreover, the simulation results show that the proposed SP algorithm can improve maximum of 0.8 dB BER performance compared with the existing modified sumproduct algorithm.

## Low complexity soft-decision demapper for high order modulation of DVB-S2 system

- **Status**: ❌
- **Reason**: DVB-S2 soft-decision demapper HW로 LDPC 디코더 자체가 아닌 demapper 인터페이스
- **ID**: ieee:4815678
- **Type**: conference
- **Published**: 24-25 Nov.
- **Authors**: Jang Woong Park, Myung Hoon Sunwoo, Pan Soo Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4815678
- **Abstract**: This paper presents an efficient soft-decision demapper interface and a low complexity demapper for high-order modulation scheme. The proposed soft-decision demapper interface can operate at a symbol rate and replace the parallel to serial converter by locating between the M-PSK demodulator and the soft-decision demapper. In addition, the proposed soft-decision demapper can reduce the hardware complexity by reusing the multipliers. Moreover, the proposed demapper can support high-order modulation modes. The proposed architectures have been thoroughly verified using a FPGA board having the the Xilinxtrade Virtex II.

## Analog Logic Automata

- **Status**: ❌
- **Reason**: 아날로그 logic automata 칩(NLL/뉴로모픽); LDPC ECC로 떼어낼 부호·디코더·HW 기법 없음
- **ID**: ieee:4696906
- **Type**: conference
- **Published**: 20-22 Nov.
- **Authors**: Kailiang Chen, Jonathan Leu, Neil Gershenfeld
- **PDF**: https://ieeexplore.ieee.org/document/4696906
- **Abstract**: Analog logic circuits work on digital problems using an analog representation of the digital variables, relaxing the state space of the digital system from the vertices of a hypercube to the interior. This lets us gain speed, power, and accuracy over digital implementations. Logic automata are distributed, scalable and programmable digital computation media with local connections and logic operations. Here we propose analog logic automata (ALA), which relax binary constraints on logic automata states and introduce programmability into analog logic circuits. The localized interaction and scalability of the ALA provide a new way to do neuromorphic engineering, enabling systematic designs in a digital work flow. Low-power, biomedical, decoding and communication applications are described and a 3times3 ALA chip is prototyped, which works at 50 kHz, with a power consumption of 64 muW. With the chip configured as a programmable noise-locked loop (NLL), we obtain a bit error rate (BER) of 1E-7 at an SNR of -1.13 dB.

## A stopping criterion for nonbinary LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 정지기준 — 비이진 LDPC라 제외
- **ID**: ieee:4737395
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Xin Chen, Aidong Men, Wei Zhou
- **PDF**: https://ieeexplore.ieee.org/document/4737395
- **Abstract**: Nonbinary low-density parity-check (LDPC) codes over finite fields GF(q) have a better performance than those of the binary low-density parity-check codes, at short and medium block lengths, but the decoder of GF(q)-LDPC has more complexity. In this paper, a new stopping criterion is proposed. Based on the changes of the variance of variable node¿s extrinsic information, the criterion can predict a decoding failure and decide whether the iteration of the decoder should be stopped. The simulation results show that the stopping criterion can greatly reduces the average number of required iterations of GF(q)-LDPC decoder with negligible performance loss.

## Compressing construction of QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 압축 구성법(recursive/single-compressing), high girth 유지 — 코드 설계(E)
- **ID**: ieee:4737397
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Shuqi Sun, Wuyang Zhou
- **PDF**: https://ieeexplore.ieee.org/document/4737397
- **Abstract**: Two compressing construction methods of Quasi-Cyclic LDPC (QC-LDPC) codes are proposed, which can be called recursive-compressing and single-compressing respectively. Selecting a good QC-LDPC code as the Mother, the son codes constructed through the compressing methods are still good codes, i.e., have high girth and few short cycles, moreover, they have continuous code length and require smaller memory space. Analysis and simulation results show they can perform well over the AWGN channel.

## Good encodable irregular quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 irregular QC-LDPC 구성, girth/최소거리 동시 보존 신규 구성법 — 코드 설계(E)
- **ID**: ieee:4737391
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Yang Xiao, Kiseon Kim
- **PDF**: https://ieeexplore.ieee.org/document/4737391
- **Abstract**: The existing encodable irregular LDPC codes may have a degraded BER performance when it is derived from classical regular QC LDPC codes since both girth property and weight property are not carefully given attention to two or more thing, which lead to some codes with large girths have small minimum weights and poor BER performance. To solve the problem, we propose a new approach to construct the encodable irregular QC codes, which can not produce new short girths and can keep the large minimum weight and minimum distance of the codes. The theorems of girth 4 and girth 6 are provided to test the girth variance of the obtained irregular QC codes. Simulations verify the construction of the QC LDPC codes to be valid, since better BER performance than that of existing encodable irregular LDPC codes is obtained.

## The analysis of cycle structure for a class of quasi-cyclic LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 사이클 구조 분석 및 분류로 구성 알고리즘 개선 — 코드 설계(E)
- **ID**: ieee:4737394
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Jing Lei, Jianhui Wang, Yongqiang Gao
- **PDF**: https://ieeexplore.ieee.org/document/4737394
- **Abstract**: In this paper, we analyse the cycle structure of a class of quasi-cyclic LDPC codes, and divide the cycles of this kind of LDPC codes into three classes. It offers some help for improving the existing construction algorithms of this kind of LDPC codes. The cycles in base matrix could be extended as long as possible when p the row¿s(or column¿s) number of block-elements was prime.

## Improved performance irregular quasi-cyclic LDPC code design from BIBD’s using threshold minimization

- **Status**: ✅
- **Reason**: BIBD 기반 irregular QC-LDPC 신규 설계 + density evolution threshold 최소화, 바이너리 코드설계 기법 이식 가능(E)
- **ID**: ieee:4766569
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Siddarama R. Patil, Sant S. Pathak
- **PDF**: https://ieeexplore.ieee.org/document/4766569
- **Abstract**: In this paper we propose a novel method for designing irregular quasi-cyclic low-density parity-check (LDPC) codes from Balanced Incomplete Block Designs (BIBDpsilas). The design method hinges around finding the optimum degree profile by minimizing the threshold using density evolution. The approach for designing short block length codes is robust for practical implementation and has been found to exhibit considerable performance gain that may be attributed to a good degree profile for the codes. The design takes into consideration the code rate and code length as variable parameters. The simulation results for the designed codes are compared with regular and irregular quasi-cyclic BIBD based LDPC codes and found a relatively higher performance in terms of BER.

## Log-domain iterative decoding combined USTM with codes over GF(2m) on flat Rayleigh fading channel

- **Status**: ❌
- **Reason**: GF(2m) 비이진 LDPC + log-domain sum-product, USTM/MIMO 응용 — 비이진 LDPC라 제외
- **ID**: ieee:4737274
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Haiyan Cao, Guangqiu Li, Zemao Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/4737274
- **Abstract**: In this paper, a serial concatenated scheme combining USTM with LDPC codes over GF(2m) is presented. A modulation technique of USTM, Unitary space-time modulation, can efficiently work on decoding when the channel state information is unknown at the receiver in multi-input multi output system over flat raleigh fading channel. The BER performance of USTM system in MIMO channel will largely be improved by serially concatenating a good achieving the shannon limit LDPC(low-density parity-check) codes as outer codes, which have attracted much more attention recently, defined by a sparse parity check matrix over GF(2m) in our scheme. The well-known Sum-Product algorithm is also used as the iterative decoding of LDPC codes over GF(2m) , but here the algorithm works in the log-domain other than probability-domain for some advantages, such as implementation, computational complexity and etc. Simulating results show that our scheme works very well and about 20dB coding gain is provided by LDPC codes as an outer codes at a BER of 10-5 than USTM without channel coding. And further simulations assure that USTM concatenating with LDPC codes over GF(2m) outperforms more 5-6dB coding gain that LDPC codes over GF(2).

## Flexible low-complexity decoding architecture for QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 유연 저복잡도 디코딩 아키텍처, 신규 time-sharing 스킴 — HW(D)
- **ID**: ieee:4737396
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Nan Jiang, Kewu Peng, Zhixing Yang
- **PDF**: https://ieeexplore.ieee.org/document/4737396
- **Abstract**: A novel flexible decoding architecture for quasi-cyclic (QC) low-density parity-check (LDPC) code is proposed in this paper to reduce decoding complexity. The novelty of this architecture lies in a new time-sharing scheme of processing units, which provides low complexity and flexible serial factor of decoding hardware. Without loss of coding performance, the architecture requires significantly less processing units compared with known semi-parallel decoders at the expense of throughput decrease, while keeping memory requirement unchanged. As demonstrated by hardware and software implementation results, the proposed architecture is advisable and competent for wireless mobile systems and portable devices.

## Design and optimization of joint network-channel LDPC code for wireless cooperative communications

- **Status**: ❌
- **Reason**: 무선 협력통신용 joint network-channel LDPC 설계, NAND ECC로 떼어낼 코드설계/디코더 기법 없음 (응용 특이적)
- **ID**: ieee:4737457
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Du Bing, Zhang Jun
- **PDF**: https://ieeexplore.ieee.org/document/4737457
- **Abstract**: In this paper, we develop a joint design method of network-channel low density parity check codes (LDPC) codes by constructing joint network-channel parity check matrix. Random network coding is performed to provide side information for both the source and relay¿s transmission. This system matrix makes an easy way to collect all independent signal copies to provide a spatial diversity gain. And the complexity of network coding is linear to the block length ~O(n). Then, the optimization of joint network-channel LDPC code is conducted in term of maximizing the system rate. Based on the joint network-channel LDPC codes, we presents a protocol for wireless cooperative communications, which is very effective to combat the channel fading without much rise in system bandwidth and transmitting power. A traditional three-node model is built to describe the protocol where relay not only helps source to transmit but also has its own information to transmit.

## Comparison of decoding turbo Gallager codes in hybrid decoding arrangements with different iterative decoders over the erasure channel

- **Status**: ✅
- **Reason**: turbo Gallager(LDPC계) 반복 디코더 비교, erasure 채널 BP vs BCJR-LUT+ML 하이브리드 디코더 — 디코더 기법 이식 가능성, Phase3 재검토
- **ID**: ieee:4737183
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Li Yang, Marcel Ambroze, Martin Tomlinson
- **PDF**: https://ieeexplore.ieee.org/document/4737183
- **Abstract**: In this paper, different iterative decoders for turbo Gallager codes are optimised and compared for the binary erasure channel. The complexity and performance differences between turbo decoder, BCJR-based Look-Up Table decoder and belief propagation decoder are analysed and evaluated. A hybrid decoding arrangement, which uses an iterative decoder followed by a maximum likelihood ¿In-Place¿ matrix inversion algorithm, is compared for the different iterative decoders. Results are presented which show that the BCJR-based iterative decoders achieve better performance than using the belief propagation decoder for turbo Gallager codes in the erasure channel. When small encoder memory is selected, the optimised Look-Up Table decoder provides a good balance between convergence performance and complexity.

## Performance analysis of Raptor codes in Wi-Max systems over fading channel

- **Status**: ❌
- **Reason**: Raptor/Fountain 부호 성능분석, 비-LDPC이며 LDPC는 비교 베이스라인, 떼어낼 기법 없음
- **ID**: ieee:4766717
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: P. Palanisamy, T.V.S. Sreedhar
- **PDF**: https://ieeexplore.ieee.org/document/4766717
- **Abstract**: In modern wireless communication systems, forward error correcting codes are employed for efficient transmission of data in noisy environments. Achieving a very less bit error rate (BER) has been the major task in the field of error control coding. The recently developed Raptor codes, which are a class of Fountain codes and the extension of LT codes, tend to give better performance than the low density parity check (LDPC) codes on burst error channels. In this paper, Raptor codes are used for forward error correction in orthogonal frequency division multiplexing (OFDM) , which is a popular multicarrier modulation technique in Wi-Max systems and is currently being used in the IEEE 802.16e (Wi-Max) standard. Simulations are carried out and the bit error rate performance and burst-erasure correction capability of Raptor codes are compared with that of quasi-cyclic LDPC codes over Rayleigh fading channel.

## Shaping gain for AWGN channel by non-uniform constellation in LDPC-Coded system

- **Status**: ❌
- **Reason**: AWGN/멀티패스용 비균일 성상 shaping gain, LDPC는 베이스라인 — 떼어낼 ECC 기법 없음
- **ID**: ieee:4737393
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Xiaoqing Wang, Jian Fu, Jun Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/4737393
- **Abstract**: It is commonly believed that there is a gap between the channel capacity and the highest achievable rate of equiprobable uniform constellation. To achieve shaping gain, non-uniform constellation following a Gaussian distribution has been designed for the AWGN channel and discussed widely along with Turbo codes. In this paper, we investigate the effect of non-uniform constellation and propose a scheme to achieve shaping gain for AWGN channel and also multipath channel using low density parity check (LDPC) codes with different rates of 0.40.6 and 0.8. Simulation results show that, non-uniform 64-QAM or 8-PAM can offer shaping gain of approximately 0.23 dB for LDPC coding rate of 0.6 over AWGN channel in DTMB system.

## An efficient early stopping scheme for LDPC decoding based on check-node messages

- **Status**: ✅
- **Reason**: 체크노드 LLR 기반 LDPC 조기정지 기법 — 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:4737398
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Z. H. Cai, J. Hao, L. Wang
- **PDF**: https://ieeexplore.ieee.org/document/4737398
- **Abstract**: An efficient early stopping method is proposed in this paper to reduce the average number of iterations for low density parity check (LDPC) decoders. The method is very efficient especially when the channel signal-to-noise ratio (SNR) is low. It is based on the estimation of the log-likelihood ratio (LLR) messages of the check nodes.

## Efficient performance evaluation of Forward Error Correcting codes

- **Status**: ❌
- **Reason**: FEC 성능평가용 importance sampling(fast flat histogram) — 시뮬레이션 평가법, 디코더/HW/구성 아님
- **ID**: ieee:4737185
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: S. Kakakhail, S. Reynal, D. Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/4737185
- **Abstract**: Standard Monte Carlo (SMC) simulation is employed to evaluate the performance of forward error correcting (FEC) codes. This performance is in terms of the probability of error during the transmission of information through digital communication systems. The time taken by SMC simulation to estimate the FER increases exponentially with the increase in signal-to-noise ratio (SNR). We hereby present an improved version of fast flat histogram (FFH) method, an adaptive importance sampling (AIS) technique inspired by algorithms existing in statistical physics. We show that the improved FFH method employing Wang Landau algorithm based on a Markov chain Monte Carlo (MCMC) sampler reduces the simulation time of the performance evaluation of complex FEC codes having different code rates.

## Analysis and performance comparison of DVB-T and DTMB systems for terrestrial digital TV

- **Status**: ❌
- **Reason**: DVB-T vs DTMB DTTB 시스템 BER 비교, OFDM 응용 — 떼어낼 LDPC 기법 없음
- **ID**: ieee:4737413
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Ming Liu, Matthieu Crussiere, Jean-Francois Helard +1
- **PDF**: https://ieeexplore.ieee.org/document/4737413
- **Abstract**: Orthogonal frequency-division multiplexing (OFDM) is the most popular transmission technology in digital terrestrial broadcasting (DTTB), adopted by many DTTB standards. In this paper, the bit error rate (BER) performance of two DTTB systems, namely cyclic prefix OFDM (CP-OFDM) based DVB-T and time domain synchronous OFDM (TDS-OFDM) based DTMB, is evaluated in different channel conditions. Spectrum utilization and power efficiency are also discussed to demonstrate the transmission overhead of both systems. Simulation results show that the performances of the two systems are much close. Given the same ratio of guard interval (GI), the DVB-T outperforms DTMB in terms of signal to noise ratio (SNR) in Gaussian and Ricean channels, while DTMB behaves better performance in Rayleigh channel in higher code rates and higher orders of constellation thanks to its efficient channel coding and interleaving scheme.

## A novel space-time FFH-MIMO system with generalized wide-interval fh patterns

- **Status**: ❌
- **Reason**: space-time FFH-MIMO 무선시스템 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:4737273
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Zhao Ying, Xiao Yang
- **PDF**: https://ieeexplore.ieee.org/document/4737273
- **Abstract**: This paper presents a novel space-time fast frequency hopping (FFH) multiple input multiple output (MIMO) wireless communication system over rayleigh fading channel. With the M-ary frequency shifting keying (MFSK) modulation and noncoherent demodulation, the structure of a new system is discussed based on the combination of FFH technique and MIMO system. The concept of generalized wide-interval FH (WFH) pattern is put forward. Corresponding design method of WFH pattern is given and applied to the new system. Because of the high diversity order offered by both FFH technique and multiple receive antennas, this novel system may achieve much higher transmitting rate and favorable bit error ratio (BER) performance at the same time compared with conventional FFH single input single output (SISO) system.

## Iterative coding and decoding algorithm of RS digital fountain code

- **Status**: ❌
- **Reason**: RS digital fountain 반복 디코딩 — 비-LDPC, RS fountain 전용
- **ID**: ieee:4737179
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Weijia Lei, Guangjun Li, Xiangming Li +1
- **PDF**: https://ieeexplore.ieee.org/document/4737179
- **Abstract**: Combining forward error correcting and automatic repeat request is a commonly used method in digital communication system. But in broadcast communication system, this method will compromise the communication efficiency and cause longer transmission delay due to the need of retransmitting data. This problem, however, can be effectively solved by the use of digital fountain code. RS code has the potential to be used as a fountain code, but its complicated conventional decoding methods and great decoding delay have severely limited its application. This paper introduces a new iterative decoding algorithm, which helps overcome the above-mentioned shortcomings of RS code so as to enable it to be practically used as a fountain code. The corresponding coding algorithm of RS fountain code is also introduced here.

## Soft-quantized demodulation for BPSK over discrete-time memoryless fading channel

- **Status**: ✅
- **Reason**: BPSK 균일 소프트 양자화의 채널용량 기준 최적 양자기 설계 — LLR 양자화 기법 이식 가능(C)
- **ID**: ieee:4737307
- **Type**: conference
- **Published**: 19-21 Nov.
- **Authors**: Qiuliang Xie, Kewu Peng, Jian Song +2
- **PDF**: https://ieeexplore.ieee.org/document/4737307
- **Abstract**: The demapping method that simply multiplies the received symbols with channel state information (CSI) coefficients is proved optimal in this paper for any BPSK modulated discrete-time memoryless fading channel (DMFC) from the viewpoint of channel capacity, when CSI is available at the receiver. A generic method to calculate the channel capacity of BPSK modulated DMFC subjected to uniform soft quantization is proposed, which offers a powerful criterion for optimal quantizer design. Numeric results of the Rayleigh fading case are presented, showing that 6-bit uniform quantization offers effective demodulation compared with unquantized demodulation, losing less than 0.1 dB for both with and without CSI cases.

## Bounded angle iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: BA-I 디코딩: 반복 디코더 구조에 추가 조건으로 undetected error rate 감소시키는 신규 BP 변형, C 카테고리 이식 가능
- **ID**: ieee:4753226
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Sam Dolinar, Kenneth Andrews, Fabrizio Pollara +1
- **PDF**: https://ieeexplore.ieee.org/document/4753226
- **Abstract**: A modification to the usual iterative decoding algorithm for LDPC codes, called bounded angle iterative (BA-I) decoding, is introduced. The modified decoder erases codewords detected during iterations that fall outside a maximum decoding angle with respect to the received observation. The new algorithm is applicable in scenarios that demand a very low undetected error rate but require short LDPC codes that are too vulnerable to undetected errors when the usual iterative decoding algorithm is used. BA-I decoding provides a means of reducing the maximum undetected error rate for short LDPC codes significantly, by incorporating a simple extra condition into the iterative decoder structure without redesigning the code. The reduction in undetected error rate comes at a price of increasing the threshold signal-to-noise ratio (SNR) required for achieving a good overall error rate, but this increase in channel threshold can be minimized by allowing the decoderpsilas maximum decoding angle to vary with SNR.

## Adaptive-rate nonbinary LDPC coding for frequency-hop communications

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC + 무선 주파수홉 응용 적응율; 비이진 제외 대상
- **ID**: ieee:4753227
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Michael B. Pursley, Thomas C. Royster
- **PDF**: https://ieeexplore.ieee.org/document/4753227
- **Abstract**: We evaluate the performance of irregular low-density parity-check (LDPC) codes in slow frequency-hop spread-spectrum systems with nonbinary orthogonal modulation. We also evaluate the performance of two adaptive coding protocols for the LDPC codes. The protocols use information derived by the iterative decoder during the decoding of each packet to select the code rate for the next packet. Performance results are presented for static partial-band noise channels and for partial-band noise channels with time-varying interference bandwidth or power. The adaptive coding protocol is shown to have good performance, even on channels that cause some of the individual codes to exhibit nonmonotonic throughput.

## Performance under delay constraints on iterative decoding of LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 지연제약 하 SPA vs TDMP 메시지패싱 디코딩 비교 — 이식 가능 디코더 알고리즘(C)
- **ID**: ieee:4753232
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: JaWone Kennedy, Daniel L. Noneaker
- **PDF**: https://ieeexplore.ieee.org/document/4753232
- **Abstract**: The performance of a system with a quasi-cyclic low-density parity-check code is examined under various constraints on the decoding delay. Two alternatives are considered for the message-passing decoding algorithm: the sum-product algorithm and the turbo-decoding message-passing algorithm. It is shown that their relative performance depends heavily on the stringency of the delay constraint; the TDMP algorithm results in substantially better performance than the SPA if the constraint is stringent.

## The performance of flexible LDPC codes on Gaussian channels with bursty erasures

- **Status**: ❌
- **Reason**: 버스트 소거채널용 F-LDPC + 채널 인터리빙; 무선/소거채널 응용 특이적, 떼어낼 신규 디코더/구성 없음
- **ID**: ieee:4753230
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Cenk Kose, Thomas R. Halford
- **PDF**: https://ieeexplore.ieee.org/document/4753230
- **Abstract**: The burst-erasure channel with additive white Gaussian noise (AWGN), or BuEC-G, is useful both as an abstraction of a number of military communications channels, and as a surrogate for the design of codes on correlated Rayleigh fading channels. While codes for the BuEC-G have been presented in the literature, the focus has largely been on highly optimized inflexible point designs that are not amenable to low-complexity, high-throughput decoder implementation in hardware. In this paper, the performance of TrellisWare Technologies, Inc.psilas Flexible Low-Density Parity-Check (F-LDPC) code family on the BuEC-G is investigated. In order to the improve the burst-erasure correction capability of existing F-LDPC designs, without sacrificing flexibility, partial channel interleaving is employed. The performance of thus modified F-LDPC codes is shown to match that of a number of point designs reported in the literature.

## Error floor analysis for an ensemble of easily implementable irregular (2048, 1024) LDPC codes

- **Status**: ✅
- **Reason**: 바이너리 (2048,1024) 불규칙 LDPC 코드 설계 + error floor/저오류영역 성능 분석 — 이식 가능 코드설계(E)
- **ID**: ieee:4753229
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Chad A. Cole
- **PDF**: https://ieeexplore.ieee.org/document/4753229
- **Abstract**: The following paper describes a design process for constructing semirandom LDPC codes with characteristics that are suitable for a relatively simple implementation for both the encoding and decoding operation. The paper will focus on two particular code ensembles - both rate-1/2 (2048, 1024) designs with a specified irregular degree distribution. These code parameters were chosen simply because they satisfied a project design constraint, but the process described can be extended to most other low-density designs. Some new insights into the codepsilas performance curve behavior in the low error region under message passing decoding are presented.

## Doubly iterative LDPC-coded DS-CDMA receivers with coherent detection, EM channel estimation, and no pilot symbols

- **Status**: ❌
- **Reason**: DS-CDMA EM 채널추정+반복수신; LDPC는 부수, 무선 응용 특이적
- **ID**: ieee:4753265
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Don Torrieri, Amitav Mukherjee, Hyuck M. Kwon
- **PDF**: https://ieeexplore.ieee.org/document/4753265
- **Abstract**: In this paper, we describe direct-sequence code-division multiple-access (CDMA) systems with M-ary modulation in which channel estimation, coherent demodulation, and decoding are iteratively performed without the use of any training or pilot symbols. An expectation-maximization channel-estimation algorithm for the fading amplitude and interference-plus-noise power spectral density (PSD) is proposed for CDMA systems with low-density parity-check codes. The elimination of pilot symbols simplifies the system design and allows either an enhancement in information throughput or greater spectral efficiency by increasing the information-symbol duration. After initial estimates of the fading amplitude and noise PSD are obtained from the received symbols, subsequent values of these parameters are iteratively updated by using the soft feedback from the channel decoder. The updated estimates are combined with the received symbols and iteratively passed to the decoder. Although the bit error rates of the proposed systems may be slightly larger than those of comparable systems with pilot-assisted channel estimation, the throughputs are higher.

## Spectral efficiency maximization using pragmatic modern rate-compatible code families

- **Status**: ❌
- **Reason**: 증분잉여 rate-compatible F-LDPC 스펙트럼효율; 무선 프로토콜 응용, 떼어낼 신규 코드설계 없음
- **ID**: ieee:4753299
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Thomas R. Halford, Cenk Kose
- **PDF**: https://ieeexplore.ieee.org/document/4753299
- **Abstract**: In communication links employing incremental redundancy (IR), the strength of the code used for forward error correction is adapted in order to maximize instantaneous spectral efficiency in time-varying channels. In this paper, a simple two-phase IR transmission scheme is studied in a block-fading channel in order to illuminate the effects on protocol design and achievable spectral efficiency of the performance, rate range, and rate granularity of the chosen rate-compatible (RC) code family. Two pragmatic RC families based on Flexible Low-Density Parity-Check (F-LDPC) codes are studied alongside a notional family with infinite rate precision that matches theoretical guidelines for the performance of practical coding schemes (i.e., limits on finite block size and non-vanishing block error rate transmission over modulation constrained channels) at all points.

## Efficient quantization schemes for LDPC decoders

- **Status**: ✅
- **Reason**: LDPC 디코더 고정소수점 양자화 기법(3/4/5비트) + sum-product 구현/density evolution — 이식 가능 디코더/HW(C/D)
- **ID**: ieee:4753231
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Radivoje Zarubica, Ryan Hinton, Stephen G. Wilson +1
- **PDF**: https://ieeexplore.ieee.org/document/4753231
- **Abstract**: LDPC codes have attracted much attention recently for their near-capacity performance and high throughput owing to parallel decoding architectures. While simulations are normally done with floating point computation, any practical implementation (ASIC or FPGA) will be built with fixed-point computation. Obviously, decoder speed will increase, and resource requirements will drop, with low-precision implementations, say 3,4, or 5-bit architectures. In this paper we study the effects of quantization in this regime, using density evolution and decoder simulation. Detailed sum-product decoder implementations are given, and performance losses relative to floating point decoding are given. In particular, 4-bit decoder architectures sustain only 0.1 dB penalty.

## A soft-decision scaling metric employing receiver statistics for direct-sequence spread-spectrum packet radio networks

- **Status**: ❌
- **Reason**: DS-SS 패킷라디오용 soft-decision scaling 메트릭; LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:4753233
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Steven W. Boyd, Michael B. Pursley, Thomas C. Royster +1
- **PDF**: https://ieeexplore.ieee.org/document/4753233
- **Abstract**: Packet radios for tactical networks must be able to communicate over highly dynamic links that are susceptible to variations in propagation loss, jamming, and multiple-access interference. We describe and evaluate an adaptive scaling metric for soft-decision decoding in direct-sequence spread-spectrum receivers for tactical radio networks. The metric is derived from post-detection signal quality statistics that are developed in the demodulator, and it is applied to the demodulatorpsilas soft-decision outputs before they are sent to the decoder. To maintain efficient use of assigned channel and spectrum resources, our metric exploits the nature of the spread-spectrum signal to obtain demodulator statistics during the reception of the desired transmission and therefore requires no pilot symbols or channel measurements. We compare the performance of our proposed adaptive scaling metric with a fixed soft-decision metric and with the log-likelihood ratio metric.

## Scalar quantizers for decentralized estimation of multiple random sources

- **Status**: ❌
- **Reason**: 분산 센서 추정용 스칼라 양자화/소스코딩; 채널 ECC 아님
- **ID**: ieee:4753286
- **Type**: conference
- **Published**: 16-19 Nov.
- **Authors**: Azadeh Vosoughi, Ren Gang
- **PDF**: https://ieeexplore.ieee.org/document/4753286
- **Abstract**: We consider a new inference-centric application for a distributed sensor network. Consider multiple signal sources, i.e., acoustic sources, in the field being monitored. Governed by physics law each sensor’s measurement can be modeled as a linear combination of the original multiple signal sources, corrupted by the additive measurement noise. In a non-cooperative communication scenario, each sensor transmits (a summary of) its own observations to the fusion center (FC), that is interested in reconstruction of all the original signal sources. We show that the inherent correlation among sensors’ measurements, which is due to their spatial proximity, can be effectively exploited to compress sensors’ data and reduce the transmission rate, without necessarily comprising the inference performance, i.e., quality of the reconstructed sources at the FC. In particular, we propose a practically simple and yet effective encoding algorithm for sensors, built on the concept of distributed source coding, two data reconstruction schemes for the FC (referred to as pairing and sequential schemes), and two corresponding rate allocation policies. The proposed compression algorithm is developed based on the side information coding technique in [10]. We further investigate the trade off between rate and source reconstruction quality for the proposed compression/reconstruction schemes and verify their effectiveness via simulations.

## Reduced complexity and improved performance decoding algorithm for nonbinary LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC용 BP 디코더—비이진 LDPC 제외 대상
- **ID**: ieee:4716279
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Xin Chen, Aidong Men
- **PDF**: https://ieeexplore.ieee.org/document/4716279
- **Abstract**: Low-density parity-check (LDPC) codes over finite fields GF(q) have a better performance than those of the binary low-density parity-check codes, at short and medium block lengths, but the decoder of GF(q)-LDPC has more complexity. In this paper, we present a new reduced-complexity belief propagation (BP) decoding algorithm for GF(q)-LDPC codes by analyzing the reliability of code symbols. Instead of update all the variable nodes during iteration, we just update variable nodes which are mostly to be in an error. The algorithm also shows a property to reduce the effects of oscillating on decoding. The simulations prove that we could improve performance and reduce complexity at the same time for short and medium GF(q)-LDPC codes.

## A novel mapping scheme in non-binary LDPC coded modulation system

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 변조 매핑—비이진 LDPC는 제외 대상
- **ID**: ieee:4716209
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Chen Luo, Keke Liu, Zesong Fei +1
- **PDF**: https://ieeexplore.ieee.org/document/4716209
- **Abstract**: In this paper, we propose a novel mapping scheme in non-binary LDPC coded modulation system. Contrary to the mapping method in [1], we assign the variable node of less degree to the more significant bits(MSBs) of signal constellation, for the purpose of the balanced protection. Simulation results show that compare to the traditional mapping scheme, the proposed method gives 0.1dB–0.5dB performance gain at BER=10−5 without additional complexity.

## Prediction of hybrid-ARQ based on mutual information model for LDPC coded OFDM system

- **Status**: ❌
- **Reason**: LDPC coded OFDM의 HARQ 재전송 길이 예측(MI 모델)—무선 링크적응 응용, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4716208
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Xiang Chen, Zesong Fei, Jingming Kuang +1
- **PDF**: https://ieeexplore.ieee.org/document/4716208
- **Abstract**: An accurate and simple link quality model is of utmost importance in link adaptation (LA) design. Our previous work in has verified the good accuracy of the mutual information (MI) model for rate compatible (RC) LDPC coded OFDM system. In this paper, the MI model is used to predict the retransmission length T of two hybrid ARQ schemes, partial chase combining (PCC) and incremental redundancy (IR). Simulation results verified that the one time retransmission satisfied a certain target BELR with predicted T, i.e. the needed minimum retransmission length. Thus the MI model can serve as an accurate prediction model for high spectrum efficiency hybrid ARQ design of LDPC coded OFDM system.

## Keynote Address IV Gbps wireless communication system

- **Status**: ❌
- **Reason**: Gbps 무선시스템 키노트, LDPC 부수 언급뿐 — 떼어낼 기법 없음
- **ID**: ieee:4716165
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Zhang Ping
- **PDF**: https://ieeexplore.ieee.org/document/4716165
- **Abstract**: This paper introduces the developments of TDD based Giga bits per second (Gbps) wireless communication system in wireless technology innovation (WTI) institute of BUPT. Radio link transmission design are presented in this paper, including promising key techniques of physical layer such as Channel measurement and modeling, multiple input multiple output (MIMO), low density parity check (LDPC) code, channel estimation and PAPR suppression etc., and MAC layer design such as access network architecture and scheduling. Link-level simulations prove the advantages of the design.

## A decode-and-forward relaying scheme based on orthogonal superposition modulation

- **Status**: ❌
- **Reason**: 직교중첩변조 협력 릴레이 기법—LDPC ECC 무관, 이식할 디코더/코드 기법 없음
- **ID**: ieee:4716217
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Li Huang, Zesong Fei, Jingming Kuang
- **PDF**: https://ieeexplore.ieee.org/document/4716217
- **Abstract**: In this paper, we proposed a new scheme of cooperative relaying scheme base on orthogonal superposition modulation and soft demodulation which is similar with multiuser detection. The new scheme can be considered as a different way to achieve a similar purpose with superposition modulation [6]. We optimized the parameter in order to achieve the best performance. Simulation results show that our new scheme outperform the classical cooperation based on decode-and-forward by about 1-2 dB at the same complexity.

## A new paradigm of coding for scalable video coding with wavelet-based

- **Status**: ❌
- **Reason**: 웨이블릿 기반 스케일러블 Wyner-Ziv 비디오 코딩 — LDPC ECC 기법 없음
- **ID**: ieee:4716182
- **Type**: conference
- **Published**: 10-12 Nov.
- **Authors**: Zhe Li, Sheng Fang, Xujian Li +1
- **PDF**: https://ieeexplore.ieee.org/document/4716182
- **Abstract**: In this paper, we propose a new wavelet video coding based on MCTF-WZ through introducing Wyner-Ziv coding, which is a new coding structure. Low and high frequency frames in temporal domain are encoded through the distinct coding manner, where the former is encoded by the BISK algorithm after spatial analysis. But the latter is encoded by two distinct ways according to the correlation between the reference and current frames. In this way, regions which have high correlations are coded by Wyner-Ziv coding, and regions which only have short correlations are coded by BISK after discrete wavelet transform. The coding efficiency of this scheme is close to H.264 and MC-EZBC or even better.
