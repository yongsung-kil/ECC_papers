# IEEE Xplore — 2005-05


## The ML decoding performance of LDPC ensembles over Z/sub q/

- **Status**: ❌
- **Reason**: Z/q 상의 LDPC ML 디코딩 성능 (비이진 q-ary LDPC 앙상블 스펙트라), 순수 이론 bound — 비이진+이론으로 제외
- **ID**: ieee:1424328
- **Type**: journal
- **Published**: May 2005
- **Authors**: U. Erez, G. Miller
- **PDF**: https://ieeexplore.ieee.org/document/1424328
- **Abstract**: We derive the asymptotic spectra of low-density parity-check (LDPC) ensembles over Z/sub q/. We consider two ensembles of LDPC matrices, one is binary and the other q-ary. We also show that for modulo-additive noise channels, both ensembles achieve the random coding error exponent, for graphs with sufficiently large connectivity.

## Analysis and design of LDPC codes for time-selective complex-fading channels

- **Status**: ❌
- **Reason**: time-selective fading용 PSA-LDPC density evolution 설계 — 무선 채널 특이적 코드 설계, NAND 이식할 신규 디코더/구성 없음
- **ID**: ieee:1427707
- **Type**: journal
- **Published**: May 2005
- **Authors**: K. Fu, A. Anastasopoulos
- **PDF**: https://ieeexplore.ieee.org/document/1427707
- **Abstract**: Pilot-symbol-assisted (PSA) low-density parity-check (LDPC) codes are analyzed using density evolution techniques for a frequency-nonselective, time-selective fading channel where the fading affects both the amplitude and the phase of the transmitted signal. The performance of several message-passing estimation/decoding receivers is investigated, and the optimal energy allocation between pilot and coded symbols is evaluated. Several message-passing estimation/decoding receivers are shown to fall under a single unifying description which leads to significant simplification of the analysis and design of the PSA LDPC codes and receivers. The immediate surprising result is that for the described class of receivers, the best codes for the case of perfect channel state information (CSI) at the receiver are also the best codes when no CSI is available at the receiver, regardless of the channel dynamics. A class of more elaborate receivers that perform iterative joint decoding/estimation is also presented and it is shown that codes designed specifically for these receivers provide an additional performance gain.

## Robust iterative tree-pruning detection and LDPCC decoding

- **Status**: ❌
- **Reason**: MIMO ISI 채널 tree-pruning 등화+turbo 디코딩 — equalizer 트리 탐색 기법, LDPCC는 부수, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1425645
- **Type**: journal
- **Published**: May 2005
- **Authors**: Heung-No Lee, Xinde Hu
- **PDF**: https://ieeexplore.ieee.org/document/1425645
- **Abstract**: A novel suboptimal low-complexity equalization and turbo-iterative decoding scheme is proposed in this paper. The scheme is developed for multiple transmit- and multiple receive-antenna systems operating over severe frequency-selective fading intersymbol interference channels. The signal-processing complexity may be of a concern for such systems. The complexity of a full-search equalization grows in a power-law manner O(M/sup NtL/), where M denotes for M-ary channel symbols, N/sub t/ the number of transmit-antennas, and L the number of delay channel taps. A low-complexity solution can be obtained by pruning an equalizer tree. The two main operations include a sphere list detection and a threshold-based tree-search. In the operation of extracting extrinsic messages from the pruned tree, a set of explored paths with different survival lengths poses a fairness problem: a longer-lived path naturally builds a larger discrepancy-metric than a shorter lived path does. A novel survival-length compensation-rule is devised so that all explored paths with different survival lengths are utilized fairly in generating the output message. Simulation results are obtained for multi-input and multi-output systems equipped with four transmit and four receive antennas. They indicate the performance of the receiver is very robust.

## A new approach to rapid PN code acquisition using iterative message passing techniques

- **Status**: ❌
- **Reason**: PN code acquisition에 메시지패싱 적용 — 부호 ECC가 아닌 동기화 응용, 떼어낼 LDPC BP 디코더 기법 없음
- **ID**: ieee:1425635
- **Type**: journal
- **Published**: May 2005
- **Authors**: K.M. Chugg, Mingrui Zhu
- **PDF**: https://ieeexplore.ieee.org/document/1425635
- **Abstract**: Iterative message passing algorithms on graphs, which are generalized from the well-known turbo decoding algorithm, have been studied intensively in recent years because they can provide near-optimal performance and significant complexity reduction. In this paper, we demonstrate that this technique can be applied to pseudorandom code acquisition problems as well. To do this, we represent good pseudonoise (PN) patterns using sparse graphical models, then apply the standard iterative message passing algorithms over these graphs to approximate maximum-likelihood synchronization. Simulation results show that the proposed algorithm achieves better performance than both serial and hybrid search strategies in that it works at low signal-to-noise ratios and is much faster. Compared with full parallel search, this approach typically provides significant complexity reduction.

## Concatenated codes: serial and parallel

- **Status**: ❌
- **Reason**: concatenated/expander codes — 비-LDPC 부호, soft-decision 디코더가 expander 구조에 의존하여 바이너리 LDPC BP에 그대로 이식 불가
- **ID**: ieee:1424305
- **Type**: journal
- **Published**: May 2005
- **Authors**: A. Barg, G. Zemor
- **PDF**: https://ieeexplore.ieee.org/document/1424305
- **Abstract**: An analogy is examined between serially concatenated codes and parallel concatenations whose interleavers are described by bipartite graphs with good expanding properties. In particular, a modified expander code construction is shown to behave very much like Forney's classical concatenated codes, though with improved decoding complexity. It is proved that these new codes achieve the Zyablov bound /spl delta//sub Z/ on the minimum distance. For these codes, a soft-decision, reliability-based, linear-time decoding algorithm is introduced, that corrects any fraction of errors up to almost /spl delta//sub Z//2. For the binary-symmetric channel, this algorithm's error exponent attains the Forney bound previously known only for classical (serial) concatenations.

## On factor graphs and the Fourier transform

- **Status**: ❌
- **Reason**: factor graph와 Fourier transform 듀얼리티 (순수 이론), 코드 표현 구조론 — 떼어낼 디코더/구성/HW 기여 없음
- **ID**: ieee:1424306
- **Type**: journal
- **Published**: May 2005
- **Authors**: Yongyi Mao, F.R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/1424306
- **Abstract**: We introduce the concept of convolutional factor graphs, which represent convolutional factorizations of multivariate functions, just as conventional (multiplicative) factor graphs represent multiplicative factorizations. Convolutional and multiplicative factor graphs arise as natural Fourier transform duals. In coding theory applications, algebraic duality of group codes is essentially an instance of Fourier transform duality. Convolutional factor graphs arise when a code is represented as a sum of subcodes, just as conventional multiplicative factor graphs arise when a code is represented as an intersection of supercodes. With auxiliary variables, convolutional factor graphs give rise to "syndrome realizations" of codes, just as multiplicative factor graphs with auxiliary variables give rise to "state realizations." We introduce normal and co-normal extensions of a multivariate function, which essentially allow a given function to be represented with either a multiplicative or a convolutional factorization, as is convenient. We use these function extensions to derive a number of duality relationships among the corresponding factor graphs, and use these relationships to obtain the duality properties of Forney graphs as a special case.

## Wireless Wednesday at DAC

- **Status**: ❌
- **Reason**: DAC 행사 홍보 블러브, LDPC는 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:6500095
- **Type**: journal
- **Published**: May 2005
- **Authors**: Ingrid Verbauwhede
- **PDF**: https://ieeexplore.ieee.org/document/6500095
- **Abstract**: A complete wireless system is a very complex design problem. It requires designers from very different backgrounds. The communication engineer needs to figure out the wireless system performance, and will run lots of simulations in Matlab or Simulink to get the bit error rate (BER) that he or she needs. The team will also need a MAC designer who is willing to dig into the standards and implement the MAC protocols with minimum resources and within the latency and throughput requirements. The hardware or digital designer will develop the building blocks to implement the next generation LDPC coder or Turbo accelerator. The analog and RF designers are probably in a different department worrying about getting the power amplifiers, LNAs, D/As and A/Ds operating at 1V and with a minimal power budget. Then there is the poor system designer that needs to figure out how all the modules communicate, can be integrated and tested.

## Study of the technology migration path of the cellular wireless industry from 3G to 3.5G and beyond

- **Status**: ❌
- **Reason**: 초록 없음, 셀룰러 3G→3.5G 기술 마이그레이션 경로 연구로 LDPC ECC 무관
- **ID**: ieee:1515625
- **Type**: conference
- **Published**: 6-6 May 20
- **Authors**: B. Beheshti
- **PDF**: https://ieeexplore.ieee.org/document/1515625
- **Abstract**: N/A

## Performance comparison between non-binary LDPC codes and Reed-Solomon codes over noise bursts channels

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 코드로 NAND 표준 바이너리 LDPC 대상 제외, RS 비교 자기 영역
- **ID**: ieee:1493349
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Junbin Chen, Lin Wang, Yong Li
- **PDF**: https://ieeexplore.ieee.org/document/1493349
- **Abstract**: In this paper, the performance of non-binary low-density parity-check (LDPC) codes is investigated with high rates (R > 2/3), and small block lengths (N < 5000 bits) over noise bursts channels, and is compared with that of Reed-Solomon (RS) codes. Meanwhile, a new optimized encoding scheme of non-binary LDPC codes is presented, and a new decoding algorithm with reduced-complexity is introduced. The simulation results indicate that the non-binary LDPC codes are very effective against noise bursts, and are about 2.7 dB superior to the RS codes at a frame error rate (FER) of FER=10/sup -4/, even when the burst length is up to 144 bits long. It is of important value in magnetic recording systems.

## The scheme of coded modulation based on low-density parity-check codes

- **Status**: ❌
- **Reason**: LDPC coded modulation 무선 채널(AWGN/Rayleigh) 응용, LDPC가 부수적이고 떼어낼 디코더/구성 신규 기법 없음
- **ID**: ieee:1493380
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Li Qiang, Shaoqian Li
- **PDF**: https://ieeexplore.ieee.org/document/1493380
- **Abstract**: Coded modulation is a bandwidth efficient scheme that combines the functions of coding and modulation. We proposed a new scheme of low-density parity-check coded modulation. Its performance is also analyzed over AWGN and Rayleigh fading channels. Both theoretical analysis and simulation results show that this new scheme can obtain better performance of bit error rate without increasing bandwidth for both AWGN and Rayleigh fading channels.

## Efficient frequency domain decoding of binary BCH codes based on prime-factor FFT

- **Status**: ❌
- **Reason**: 바이너리 BCH 코드의 FFT 기반 주파수영역 디코딩, 비-LDPC 부호이며 BP 비의존 기법으로 이식 불가
- **ID**: ieee:1493352
- **Type**: conference
- **Published**: 27-30 May 
- **Authors**: Suquan Ding, Zhixing Yang, Changyong Pan
- **PDF**: https://ieeexplore.ieee.org/document/1493352
- **Abstract**: By introducing the ideas of reducing computation complexity in the fast Fourier transform (FFT) to decoding, a low complexity decoding of binary BCH codes is derived which transforms the determination of one-dimensional error word into two-dimensional matrix. For the case of double-error-correcting binary BCH codes, the frequency domain decoding based on prime-factor FFT (in short, PF-FDD) was designed. Compared with the conventional frequency domain decoding algorithm, PF-FDD has the advantages of lower decoding complexity and faster decoding speed at the expense of increasing storage memory. When compared with the ordinary look-up table decoding scheme, the error patterns to store are decreased greatly. Hence, PF-FDD achieves a better tradeoff between decoding complexity and hardware complexity. The proposed low complexity decoding scheme is suitable for binary BCH codes whose block length has prime factors and error correcting capacity is relatively small, and is expected to apply to soft-decision decoding.

## Quasi-cyclic low-density parity-check coded multi-band-OFDM UWB systems

- **Status**: ❌
- **Reason**: IO-LDPC 변형 QC-LDPC를 MB-OFDM UWB에 적용·성능평가, 새 구성기법 기여 미미한 무선응용
- **ID**: ieee:1464525
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: Sang-Min Kim, Jun Tang, K.K. Parhi
- **PDF**: https://ieeexplore.ieee.org/document/1464525
- **Abstract**: Multi-band orthogonal frequency division multiplexing (MB-OFDM) has been considered as a prominent solution for ultra wideband (UWB) technology supporting high speed, short range and point-to-point wireless communications. In this paper, we design quasi-cyclic (QC) low-density parity-check (LDPC) codes that are modified from implementation-oriented (IO) LDPC codes and examine their capability and suitability for MB-OFDM systems in terms of performance and implementation complexity. We evaluate the performance of QC-LDPC codes over MB-OFDM systems for four different data rates. By simulations, it is shown that the transmission distance of QC-LDPC coded MB-OFDM systems can increase by 29%-73% compared with that of convolutional codes. In addition, it is shown that QC-LDPC codes can be realized by a rate-configurable encoder and decoder.

## An analog/digital mode-switching LDPC codec

- **Status**: ❌
- **Reason**: 아날로그/디지털 모드전환 LDPC 코덱 — 아날로그 소프트 디코딩 회로 특이적, NAND 디지털 LDPC에 이식 불가
- **ID**: ieee:1465954
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: D. Haley, C. Winstead, A. Grant +2
- **PDF**: https://ieeexplore.ieee.org/document/1465954
- **Abstract**: We present a novel time-multiplexed codec for a class of low-density parity-check codes, which switches between analog decode and digital encode modes. In order to achieve this behaviour from a single circuit we have developed mode-switching gates. These logic gates are able to switch between analog (soft) and digital (hard) computation. Only a small overhead in circuit area is required to transform the analog decoder into a full codec. The encode operation can be performed two orders of magnitude faster than the decode operation, making the circuit suitable for full-duplex applications. Throughput of the codec scales linearly with block size, for both encode and decode operations. The low power and small area requirements of the circuit make it an attractive option for small portable devices.

## Parallelism/regularity-driven MIMO detection algorithm design

- **Status**: ❌
- **Reason**: MIMO 검출 알고리즘 VLSI 설계 — LDPC 부호/디코더 기여 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:1465746
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: Tong Zhang, Yan Xin, Sizhong Chen
- **PDF**: https://ieeexplore.ieee.org/document/1465746
- **Abstract**: Efficient VLSI implementation of multiple-input multiple-output (MIMO) detectors plays an important role in the real-life implementation of MIMO communication systems. However, most high-performance MIMO detection algorithms developed so far largely lack the operational parallelism and regularity that are essential for high-throughput and low-power VLSI implementations. Following the theme of parallelism/regularity-driven algorithm design, we propose hard/soft-output MIMO detection algorithms that have high operational parallelism and a regular/static data flow structure with fixed detection delay. Besides those properties desirable for VLSI implementations, such algorithms can achieve superior detection performance, as demonstrated in the simulations.

## Digital built-in self-test of CMOS analog iterative decoders

- **Status**: ❌
- **Reason**: 아날로그 반복디코더의 디지털 BIST 테스트 기법 - ECC 디코더/구성/HW아키텍처 기여 아님(테스트 전용)
- **ID**: ieee:1465059
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: M. Yiu, V.C. Gaudet, C. Schlegel +1
- **PDF**: https://ieeexplore.ieee.org/document/1465059
- **Abstract**: A design method is presented for testing of analog iterative decoders using digital built-in self-test (BIST). Mixed-signal BIST schemes are often complex and demand larger than acceptable hardware cost. By using a digital BIST scheme, analog iterative decoders can easily be tested in the digital domain. A BIST was designed and simulated for an (8,4,4) extended Hamming decoder using 0.18 /spl mu/m CMOS. It is capable of detecting transistor faults in the decoder. A decoding rate of 444 kbps is achieved. The digital BIST scheme is suitable for any iterative decoder using the sum-product algorithm.

## Optimal packet length with energy efficiency for wireless sensor networks

- **Status**: ❌
- **Reason**: WSN 패킷길이·에너지효율 최적화, BCH 부호 사용 - 비-LDPC 무선응용
- **ID**: ieee:1465247
- **Type**: conference
- **Published**: 23-26 May 
- **Authors**: Inwhee Joe
- **PDF**: https://ieeexplore.ieee.org/document/1465247
- **Abstract**: In this paper, we propose to improve energy efficiency in wireless sensor networks using optimal packet length in terms of power management and channel coding. The use of power management cannot improve energy efficiency, but it saves a lot of energy because the transceiver is turned off while it is not used. Also, we evaluate optimal packet length without power management, such that the energy efficiency can be maximized. Finally, we show that the BCH code for channel coding can improve energy efficiency significantly compared to the convolutional code.

## A parallel implementation of the message-passing decoder of LDPC codes using a reconfigurable optical model

- **Status**: ❌
- **Reason**: 재구성 광학 모델(LARPBS) 기반 메시지패싱 병렬 구현 — 광학 버스 특이적 HW로 NAND 디지털 ECC에 이식 불가
- **ID**: ieee:1434902
- **Type**: conference
- **Published**: 23-25 May 
- **Authors**: S. Babvey, A.G. Bourgeois, J.A. Fernandez-Zepeda +1
- **PDF**: https://ieeexplore.ieee.org/document/1434902
- **Abstract**: In this paper we propose a constant-time algorithm for parallel implementation of the message-passing decoder of low density parity check (LDPC) codes on the linear array with a reconfigurable pipelined bus system (LARPBS), achieving the minimum number of processors required for a fully parallel implementation. Dynamic reconfiguration provides flexibility to code changes and efficient message routing. To decode a different code, we may simply set up the required connections between the bit-nodes and check-nodes by modifying the initialization phase of the LARPBS algorithm. No extra wiring or hardware changes are required, as compared to other existing approaches. Moreover, the same hardware can implement the decoder in both probability and logarithm domains. The LARPBS also allows reducing the number of the bus cycles required for processor communications to a small constant, regardless of the code length. We illustrate that the LARPBS is an efficient and fast model for implementing the decoder.

## EXIT charts for non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC EXIT chart 설계 - 비이진 LDPC는 제외
- **ID**: ieee:1494432
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: G.J. Byers, F. Takawira
- **PDF**: https://ieeexplore.ieee.org/document/1494432
- **Abstract**: In this paper extrinsic information transfer (EXIT) charts are proposed to design non-binary low-density parity-check (LDPC) codes for the AWGN channel. A new metric is presented to describe the mutual information of the non-binary messages. The a priori information is modelled using a Gaussian mixture distribution. Analytical expressions are given for the EXIT curves of the variable and check node decoders for both regular and irregular LDPC codes. The analytical expressions are shown to agree well with simulation results. Finally, by matching the variable and check node EXIT curves, it is shown that good nonbinary LDPC can be designed for the AWGN channel.

## On the performance of LDPC-coded OFDM system with periodically terminated differential phase modulation

- **Status**: ❌
- **Reason**: OFDM 차동변조 심볼검출(SMC) 중심, LDPC는 부수 언급뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:1494681
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: T.S. John, A. Nallanathan, M.A. Armand
- **PDF**: https://ieeexplore.ieee.org/document/1494681
- **Abstract**: In this paper, we consider the problem of symbol detection in a differentially encoded orthogonal frequency division multiplexing (OFDM) system over frequency selective fading channel. We first propose the periodical termination of differential phase trellis at predetermined indices. When the sequential Monte Carlo (SMC) methodology is applied to symbol detection in the proposed system, it is seen that accelerated weight degeneracy and impoverished trajectory diversity-problems that are encountered in conventional SMC methods-are mitigated. Furthermore, the terminated indices may also act as pilots, thus enabling pilot-aided SMC detection. Using these observations, we then propose a pilot-aided SMC detector that circumvents resampling. The effect of varying termination periods on the performance of the non-resampling detector is investigated. We also consider a low-density parity check (LDPC)-coded OFDM system and simulation results suggest the near bound performance of the proposed pilot-aided non-resampling SMC detector.

## Phase detection involving parity-check equations and suited to transmissions at low signal to noise ratio

- **Status**: ❌
- **Reason**: 패리티검사 기반 반송파 위상검출(동기화), 채널 ECC 디코더 기여 없음
- **ID**: ieee:1494704
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: M. Dervin, M.L. Boucheret, G. Mesnager +1
- **PDF**: https://ieeexplore.ieee.org/document/1494704
- **Abstract**: We introduce in this paper a carrier phase detector suited to transmissions at very low signal to noise ratio. Based on the soft decoding of parity check equations, the synchronization scheme proposed here for a QPSK modulation outperforms a classical decision directed algorithm over a Gaussian channel, and is notably well adapted to satellite applications.

## High-rate serially concatenated codes using Hamming codes

- **Status**: ❌
- **Reason**: 직렬연접부호(convolutional+Hamming) 설계, 비-LDPC 부호이며 떼어낼 LDPC BP 이식 기법 없음
- **ID**: ieee:1494429
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: M. Isaka
- **PDF**: https://ieeexplore.ieee.org/document/1494429
- **Abstract**: This paper studies (very) high-rate serially concatenated codes employing rate-1 recursive convolutional encoders and Hamming codes. We show that these codes exhibit capacity-approaching performance by the EXIT chart analysis and simulations, and that they outperform many known codes of similar parameters with respect to error rates. The serially concatenated codes can be decoded with (relatively) low complexity, and have large flexibility in code lengths and code rates.

## Joint iterative detection and decoding in the presence of phase noise and frequency offset

- **Status**: ❌
- **Reason**: 위상잡음/주파수오프셋 채널의 결합검출-디코딩, 무선통신 특이적이며 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1494446
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: A. Barbieri, G. Colavolpe, G. Caire
- **PDF**: https://ieeexplore.ieee.org/document/1494446
- **Abstract**: In this paper, we present an iterative decoding algorithm for turbo and LDPC codes transmitted over channels affected by a time-varying phase noise and an uncompensated frequency offset. The proposed algorithm is obtained as an application of the sum-product algorithm to the factor graph representing the joint a posteriori distribution of the information symbols and the channel parameters given the channel output. The resulting algorithm employs the soft-output information on the coded symbols provided by the decoder and performs forward-backward recursions taking into account the joint probability distribution of phase and frequency offset. We present numerical results for binary LDPC codes and LDPC-coded modulation schemes, showing that, despite its low complexity, the algorithm is able to cope with a strong phase noise and a significant uncompensated frequency offset, thus avoiding the use of complicated data-aided frequency estimation schemes operating on a known preamble.

## The utility of hybrid error-erasure LDPC (HEEL) codes for wireless multimedia

- **Status**: ❌
- **Reason**: hybrid erasure-error 채널용 RS/LDPC FEC, fountain/erasure 결합이며 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:1494539
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: S.S. Karande, H. Radha
- **PDF**: https://ieeexplore.ieee.org/document/1494539
- **Abstract**: Traditional wireless communication protocols do not relay corrupted packets towards the application layer and neither do they forward such packets over multiple hops. Such an approach can lead to a significant number of packet drops and thus a severe deterioration in performance of high bandwidth applications. Cross-layer protocols which do relay and forward corrupted packets have exhibited substantial promise to mitigate the above problem and thus their utility for wireless multimedia needs to be explored further. Moreover, there is a need to identify efficient channel coding methods for the cross-layer channel. Unlike the traditional schemes, where the channel observed at the application layer is a pure erasure channel, in the cross-layer schemes the application layer channel exhibits hybrid erasure-error impairments. Thus in this paper, we use a rather abstract link-layer model on the basis of which we compare the performance of cross-layer and conventional schemes. We identify the modifications required to be made to RS and LDPC based FEC schemes in order to use them over hybrid erasure-error channels. Finally we compare the considered schemes in terms of video quality using the emerging H.264 video standard. Our video analysis is based on employing a hybrid error-erasure channel coding FEC for the cross-layer schemes versus employing erasure recovery FEC for the traditional protocols. We show that cross-layer schemes can lead to a significant improvement in video quality.

## Detection of prescribed error events: application to perpendicular recording

- **Status**: ❌
- **Reason**: 수직자기기록용 특정 에러이벤트 검출 패리티검사 + post-Viterbi, LDPC ECC 아님
- **ID**: ieee:1494700
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: J. Moon, J. Park
- **PDF**: https://ieeexplore.ieee.org/document/1494700
- **Abstract**: We discuss an error detection technique geared to a prescribed set of error events. The traditional method of error detection and correction attempts to detect/correct as many erroneous bits as possible within a codeword, irrespective of the pattern of the error events. The proposed approach, on the other hand, is less concerned about the total number of erroneous bits it can detect, but focuses on specific error events of known types. We take perpendicular recording systems as an application example. Distance analysis and simulation can easily identify the dominant error events for the given noise environment and operating density. We develop a class of simple error detection parity check codes that can detect these specific error events. The proposed coding method, when used in conjunction with post-Viterbi error correction processing, provides a substantial performance gain compared to the uncoded perpendicular recording system.

## Optimal rate-compatible punctured concatenated zigzag codes

- **Status**: ❌
- **Reason**: rate-compatible punctured concatenated zigzag 부호, 비-LDPC 구성, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:1494427
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Song-Nam Hong, Dong-Joon Shin
- **PDF**: https://ieeexplore.ieee.org/document/1494427
- **Abstract**: In the next-generation mobile communication systems for various high-speed data services, the error correcting codes are required to have rate-compatibility, low decoding complexity and good performance for various frame lengths. In this paper, new rate-compatible punctured concatenated zigzag (RCPCZ) codes are proposed and analyzed by using the density evolution. As their application, type-II HARQ using RCPCZ code is shown to have better throughput at short frame lengths than yype-II HARQ using turbo code.

## Bitplane coding for correlations exploitation in wireless sensor networks

- **Status**: ❌
- **Reason**: Slepian-Wolf 기반 소스 코딩(센서 데이터 압축), 채널 ECC 아님
- **ID**: ieee:1494482
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Caimu Tang, C.S. Raghavendra
- **PDF**: https://ieeexplore.ieee.org/document/1494482
- **Abstract**: In this paper, we propose a compression scheme called spatial set-partitioning in hierarchical trees which exploits the spatial and temporal correlations present in sensor data. This scheme allows progressive transmission and provides scalability in adapting to the underlying correlation structure of sensed data. It uses flexible Slepian-Wolf coding based on low density parity-check codes. Two different decoding schemes are proposed for different types of resource constrained sensor nodes. This scheme outperforms known codecs by a large margin of decibel in terms of the signal-to-noise ratio. This scheme has O(n) complexity for encoding and O(nlog(n)) complexity for decoding using message passing, where n is the codeword length. Experiments and simulation results with field data sets demonstrate the viability of our proposed scheme to wireless sensor networks.

## Dc-free convolutional codes and dc-free turbo codes

- **Status**: ❌
- **Reason**: DC-free 컨볼루션/터보 부호 스펙트럼 정형, 비-LDPC, 이식 가능 ECC 기법 없음
- **ID**: ieee:1494428
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Fengqin Zhai, Yan Xin, I.J. Fair
- **PDF**: https://ieeexplore.ieee.org/document/1494428
- **Abstract**: In this paper we integrate convolutional/turbo encoding with multimode encoding to generate dc-free convolutional/turbo codes. Based on the generators of error-control codes, we employ flipping or puncturing to ensure that the coded sequences are dc-balanced. At the receiver, the channel output is first decoded by a convolutional/turbo decoder (with consideration of detection when flipping is used during encoding), and then by a dc-free decoder. We show that good spectrum performance can be obtained at the cost of an increase in complexity in the encoder and that excellent bit error rate (BER) performance can be obtained particularly when source data logic values are not equiprobable.

## Performance analysis on coded system over quasi-static (MIMO) fading channels

- **Status**: ❌
- **Reason**: MIMO 페이딩 채널 union bound 성능분석, 순수 이론 bound이며 turbo 디코더 - 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1494462
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: Jingqiao Zhang, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/1494462
- **Abstract**: In this paper, we derive closed-form upper bounds on the error probability of coded modulation schemes used for multi-input multi-output (MIMO) quasi-static fading channels. The bounds are obtained from new tight union-bound techniques, and can be readily calculated when the distance spectrum is given. In deriving the bounds for the MIMO system, we assume the use of orthogonal space-time block code (OSTBC) as the inner code. The outer code is the block code. We obtain an equivalent single-input single-output (SISO) channel model for this concatenated coded-modulation system. The upper bounds derived here indicate good match with the simulation results of the complete transceiver the system in which the turbo-iterative decoding algorithm is employed at the receiver.

## 2005 IEEE International Conference on Communications (IEEE Cat. No. 05CH37648)

- **Status**: ❌
- **Reason**: 학회 논문집 목차(table of contents), 논문 아님
- **ID**: ieee:1494258
- **Type**: conference
- **Published**: 16-20 May 
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1494258
- **Abstract**: The following topics are dealt with: traffic control technology; traffic engineering; bandwidth management and multicast technology; performance modeling and analysis; routing technology; QoS and wireless networks; network reliability and security; performance evaluation and simulation; scheduling technology; ultra wideband systems; multiple access systems; diversity/multiplexing trade-off; communication theory; iterative techniques; information theory; space-time codes; coding and modulation; OFDM; turbo codes; LDPC codes; decoding algorithms; signal processing for communications/storage; ad hoc networks; noncoherent/differential ST codes; MIMO systems; resource allocation; distributed detection and distributive simulation; UWB and broadband communication; switching and routing; wireless sensor networks; source coding; multicarrier systems; iterative receivers and diversity; wireless networking for multimedia communication; multimedia coding and transport over wireless networks; real-time and streaming media; overlay multicast; networked multimedia delivery; media security and home networking; mobile network architectures and services; wireless LAN; 3G services and standards; transport layer protocols; satellite services; content distribution networks; universal services; service management; service provisioning; CDMA in optical networking; multicasting WDM networks; optical burst switching/optical packet switching; GMPLS; protection and restoration; optical communication systems; optical switches and cross-connects; Ethernet passive optical networks; signal processing for wireless systems; DSL; detection techniques; channel estimation and equalization; 3G/4G systems; radio resource management; space time processing; medium access control; mobility management; QoS aware resource management; power-aware techniques; admission control in 3G networks; broadband wireless access; wireless TCP; mobile IP.

## Performance improvement of turbo coded multi-route multi-hop networks using parity check codes

- **Status**: ❌
- **Reason**: turbo 부호 멀티홉 네트워크 패리티비트 채널추정, 비-LDPC이며 이식 디코더 기법 없음
- **ID**: ieee:1503237
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: T. Wada, N. Nakagawa, H. Okada +3
- **PDF**: https://ieeexplore.ieee.org/document/1503237
- **Abstract**: Wireless multi-hop networks are promising techniques for next generation wireless communications. Multi-hop networks have large channel capacity and can achieve multi-route transmissions. By using multi-route transmissions, we can obtain a route diversity effect at the destination nodes. In order to enhance the diversity effect, we usually adopt forward error correction techniques. Forward error correction techniques and turbo codes effectively work against severe wireless environment including fading channels. The iterative turbo decoder requires accurate channel information to achieve good decoding performance. In multi-hop transmissions, however, the receiver usually measures only the channel information of the last hop and it does not know the channel information of the whole route. In this paper, we propose the turbo coded multi-route multi-hop networks using parity check bits. By using parity bits, we can easily estimate the whole channel information in multi-route multi-hop networks. Using numerical examples, we show that the proposed scheme improves the performance in the fast fading channel conditions.

## Synthesis of low power CED circuits based on parity codes

- **Status**: ❌
- **Reason**: 패리티검사 기반 저전력 CED 회로 합성, LDPC ECC가 아니라 동시오류검출 로직 설계
- **ID**: ieee:1443443
- **Type**: conference
- **Published**: 1-5 May 20
- **Authors**: S. Ghosh, N.A. Touba, S. Basu
- **PDF**: https://ieeexplore.ieee.org/document/1443443
- **Abstract**: An automated design procedure is described for synthesizing circuits with low power concurrent error detection. It is based on pre-synthesis selection of a parity-check code followed by structure constrained logic optimization that produces a circuit in which all single point faults are guaranteed to be detected. Two new contributions over previous work include (1) the use of a k-way partitioning algorithm combined with local search to select a parity-check code, and (2) a methodology for minimizing power consumption in the CED circuitry. Results indicate significant reductions in area overhead due to the new code selection procedure as well as the ability to find low power implementations for use in power conscious applications.

## Performance evaluation of LDPC codes in the presence of ISI with application to 10GBASE-T Ethernet

- **Status**: ❌
- **Reason**: 10GBASE-T용 LDPC의 ISI 채널 성능 평가뿐, 떼어낼 신규 디코더·구성·HW 없음
- **ID**: ieee:1557399
- **Type**: conference
- **Published**: 1-4 May 20
- **Authors**: S.S. Tehrani, B.F. Cockburn, S. Bates
- **PDF**: https://ieeexplore.ieee.org/document/1557399
- **Abstract**: Low density party check (LDPC) codes are among the most powerful error control codes known. They can produce error correcting performance close to the Shannon limit and can be decoded using iterative decoding algorithms with linear complexity. These key advantages have made LDPC codes a candidate coding scheme for various novel applications and standards, such as 10GBASE-T Ethernet, in which both coding performance and implementation complexity are important considerations. In this paper, we investigate the performance of a recent LDPC code candidate for 10GBASE-T Ethernet, as well as a standard LDPC code, over additive white Gaussian noise (AWGN) channels with inter-symbol interference (ISI). We show that in comparison with AWGN, ISI introduces less performance degradation at the same level of signal-to-noise-and-interference ratio (SNIR). Given this SNIR scenario, we give simulation evidence that the performance of LDPC codes over ISI channels is upper-bounded by their performance over a AWGN channel. These results provide insight into the performance evaluation of LDPC codes in practical systems. In particular, the results allow us to characterize the equivalent AWGN for given amounts of ISI
