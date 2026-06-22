# IEEE Xplore — 2012-12


## 4-Cycle Free LDPC Codes Based on Difference Sets

- **Status**: ❌
- **Reason**: difference set 기반 4-cycle-free QC-LDPC 구성이지만 girth>=6 교과서 수준 사이클 제거로 새 기여 약함; 표준 sum-product 사용. 단순 구성 재사용으로 제외(애매하나 신규성 낮음)
- **ID**: ieee:6310171
- **Type**: journal
- **Published**: December 2
- **Authors**: M. Esmaeili, M. Javedankherad
- **PDF**: https://ieeexplore.ieee.org/document/6310171
- **Abstract**: Difference sets are used to give a novel method for constructing structured regular quasi-cyclic low-density parity-check codes. Let Fq be a field with q elements and assume that D={d1,..., dk} is a (v,k,1)-difference set for Zv with d1<;d2<;...<;dk. Depending on v=q-1, v≥ 2dk or v≥ 2dk-1, three code construction methods are given that produce regular 4-cycle free codes, that is codes with girth at least 6. Simulation results show that the constructed codes perform well over the AWGN channel with an iterative sum-product message-passing decoding algorithm.

## Low-Complexity Z_4 LDPC Code Design under a Gaussian Approximation

- **Status**: ❌
- **Reason**: Z4(비이진) LDPC 설계/디코딩 — 비이진 LDPC 제외 대상
- **ID**: ieee:6290311
- **Type**: journal
- **Published**: December 2
- **Authors**: M. Ferrari, S. Bellini, A. Tomasoni
- **PDF**: https://ieeexplore.ieee.org/document/6290311
- **Abstract**: In this paper we propose low complexity LDPC code design and decoding in Z4 which may be useful to combat phase ambiguities in wireless links affected by strong phase noise. We approximate messages exchanged on the Tanner graph using separable probability density functions. This allows a substantial reduction of decoder memory and complexity, with a negligible performance penalty, compared to ideal Z4 decoding. Furthermore, we show that the Density Evolution analysis of this suboptimal decoder leads to irregular LDPC designs matching the criteria of binary LDPC codes.

## Joint Iterative Detection/Decoding Scheme for Discrete Two-Dimensional Interference Channels

- **Status**: ❌
- **Reason**: 2D 간섭채널 합동 검출/디코딩; LDPC는 베이스라인이고 채널검출기가 핵심, NAND에 이식할 LDPC 디코더/구성 기여 없음
- **ID**: ieee:6310167
- **Type**: journal
- **Published**: December 2
- **Authors**: Jun Yao, Kah Chan Teh, Kwok Hung Li
- **PDF**: https://ieeexplore.ieee.org/document/6310167
- **Abstract**: In this paper, we propose a joint iterative detection/decoding scheme for a generalized discrete two-dimensional (2D) interference channel with low-density parity-check (LDPC) codes. A reduced-state form of the channel detector is also proposed to further reduce the system complexity. To achieve better performance, iterations are introduced between the two constituent channel detectors and among the two constituent detectors with the LDPC decoder. The computational complexity and performance of different iteration schemes are analyzed. Simulation results show that the proposed detection scheme can mitigate the 2D interference effectively and the LDPC codes can be well integrated to the 2D iterative detector to further improve the system performance significantly.

## An Adaptive Successive Cancellation List Decoder for Polar Codes with Cyclic Redundancy Check

- **Status**: ❌
- **Reason**: polar code용 적응형 SC-List 디코더; 비-LDPC이고 SC-List는 polar 전용으로 바이너리 LDPC BP 이식 불가
- **ID**: ieee:6355936
- **Type**: journal
- **Published**: December 2
- **Authors**: Bin Li, Hui Shen, David Tse
- **PDF**: https://ieeexplore.ieee.org/document/6355936
- **Abstract**: In this letter, we propose an adaptive SC (Successive Cancellation)-List decoder for polar codes with CRC. This adaptive SC-List decoder iteratively increases the list size until at least one survival path can pass CRC. Simulation shows that the adaptive SC-List decoder provides significant complexity reduction. We also demonstrate that polar code (2048, 1024) with 24-bit CRC decoded by our proposed adaptive SC-List decoder with very large maximum list size can achieve a frame error rate FER ≤ 10-3{-3} at Eb/No = 1.1dB, which is about 0.25dB from the information theoretic limit at this block length.

## Capacity and Coding for Two Common Wireless Erasure Relay Networks with Optimal Bandwidth Allocation

- **Status**: ❌
- **Reason**: 무선 erasure 릴레이 네트워크 용량/코딩; LDPC/Tornado는 BEC 부수 언급, 떼어낼 ECC 기법 없음 (JSCC/fountain류)
- **ID**: ieee:6319331
- **Type**: journal
- **Published**: December 2
- **Authors**: Srinath Puducheri-Sundaravaradhan, Thomas E. Fuja
- **PDF**: https://ieeexplore.ieee.org/document/6319331
- **Abstract**: This paper considers two simple wireless network configurations — the multiple access relay channel (MARC) and the multiple relay channel (MRC) — in which the links making up the network time-share the medium and the assumed loss mechanisms are memoryless packet erasures. The capacity region of the MARC and the capacity of the MRC are derived as functions of the link erasure rates. This is done assuming (i) optimal sharing of bandwidth among the transmitters, and (ii) perfect knowledge at the destination of erasure patterns on all the links. Moreover, it is shown that easily-implemented capacity-approaching codes for the binary erasure channel, such as LDPC or Tornado codes, can be used to attain any achievable rate(s). Finally, these capacity results are unchanged in the presence of feedback of erasure location information to all nodes. For the erasure MARC, the results imply a simple strategy, viz., that the relay should help only those sources that have a weaker direct channel to the destination than the relay itself - regardless of the quality of the source-to-relay channels. For the erasure MRC, the solution has a more complex, inductive structure: the participation of a relay r in the optimal strategy depends on the best throughput that can be achieved using only those relays with a better link to the destination than r.

## Distributed Network Coding for Wireless Sensor Networks Based on Rateless LT Codes

- **Status**: ❌
- **Reason**: WSN용 분산 네트워크 코딩+rateless LT fountain 코드, 채널 ECC 아님, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6261334
- **Type**: journal
- **Published**: December 2
- **Authors**: Kun Pang, Zihuai Lin, Bartolomeu F. Uchoa-Filho +1
- **PDF**: https://ieeexplore.ieee.org/document/6261334
- **Abstract**: In this paper, we propose a distributed network coding (DNC) scheme based on digital fountain rateless LT codes for wireless sensor networks (WSNs), where a group of source nodes communicate with a single destination node through a group of relay nodes in a two-hop fashion. The aim of the proposed scheme is to achieve network coding gains. The relay nodes perform linear combinations by using network coding to form network-coded symbols and send them to the destination node. At the destination, a graph-based, rateless code is formed on the fly. The main contribution of this paper is the derivation of an analytical symbol error rate (SER) bound for the proposed coding scheme.

## Reliable Communication over Non-Binary Insertion/Deletion Channels

- **Status**: ❌
- **Reason**: 비이진 insertion/deletion 채널 watermark+forward-backward; 비이진이며 outer code 비특정, NAND 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:6334504
- **Type**: journal
- **Published**: December 2
- **Authors**: Raman Yazdani, Masoud Ardakani
- **PDF**: https://ieeexplore.ieee.org/document/6334504
- **Abstract**: We consider the problem of reliable communication over non-binary insertion/deletion channels where symbols are randomly deleted from or inserted in the received sequence and all symbols are corrupted by additive white Gaussian noise. To this end, we utilize the inherent redundancy achievable in non-binary symbol sets by first expanding the symbol set and then allocating part of the bits associated with each symbol to watermark symbols. The watermark sequence, known at the receiver, is then used by a forward-backward algorithm to provide soft information for an outer code which decodes the transmitted sequence. Through numerical results and discussions, we evaluate the performance of the proposed solution and show that it leads to significant system ability to detect and correct insertions/deletions. We also provide estimates of the maximum achievable information rates of the system, compare them with the available bounds, and construct practical codes capable of approaching these limits.

## Channel Shortening for Nonlinear Satellite Channels

- **Status**: ❌
- **Reason**: 비선형 위성채널 channel shortener(front-end filter+reduced-state detector); LDPC 무관 채널 등화 기법, 떼어낼 LDPC 기여 없음
- **ID**: ieee:6343252
- **Type**: journal
- **Published**: December 2
- **Authors**: Giulio Colavolpe, Andrea Modenini, Fredrik Rusek
- **PDF**: https://ieeexplore.ieee.org/document/6343252
- **Abstract**: We design of an efficient channel shortener for nonlinear satellite channels. When the memory of the channel is too large to be taken into account by a full complexity detector, excellent performance can be achieved by properly filtering the received signal followed by a reduced-state detector. This letter derives closed-form expressions for the front-end filter and the target response of the reduced-state detector.

## Graph-Based Soft Channel Estimation for Fast Fading Channels

- **Status**: ❌
- **Reason**: 고속 페이딩 채널 그래프기반 소프트 채널추정 수신기; 채널추정/검출 중심, 코드설계 언급뿐 LDPC 디코더 이식 기여 없음
- **ID**: ieee:6353395
- **Type**: journal
- **Published**: December 2
- **Authors**: Tianbin Wo, Peter Adam Hoeher, Zhenyu Shi
- **PDF**: https://ieeexplore.ieee.org/document/6353395
- **Abstract**: In this paper, a graph-based soft iterative receiver (GSIR) for fast fading channels is investigated. Soft channel estimation as well as soft-output data detection are jointly accomplished via Bayesian inference over a general factor graph. The key feature is a transfer node which enables information flow from one channel node to adjacent channel nodes. The performance characteristics of this receiver is investigated via an EXIT chart analysis and simulation results. Particular emphasis is on a proper channel code design. The algorithm is universally applicable to arbitrary (bijective and non-bijective) modulation formats and can easily be extended to multi-dimensional channel estimation.

## Augmented Data Transmission Based on Low Density Parity Check Code for the ATSC Terrestrial DTV System

- **Status**: ❌
- **Reason**: ATSC DTV 부가데이터 전송 시스템에 표준 LDPC 적용; 새 디코더/구성/HW 없는 단순 응용
- **ID**: ieee:6313947
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Sung Ik Park, Heung Mook Kim, Yiyan Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/6313947
- **Abstract**: In this paper, we propose a novel augmented data transmission (ADT) system based on low density parity check (LDPC) code for an additional data stream transmission in the Advanced Television Systems Committee (ATSC) terrestrial digital television system. The LDPC code-based ADT system can provide additional data of rate up to 3 megabits per second (Mbps), which is significantly improved over the conventional data transmission schemes used in the transmitter identification system. Based on the laboratory test, we verify that the LDPC code-based ADT system is only about 1.1 dB away from Shannon limit.

## Binary-input non-line-of-sight solar-blind UV channels: Modeling, capacity and coding

- **Status**: ❌
- **Reason**: UV 무선채널 모델링/용량 중심, 메시지패싱 디코딩은 표준 수준 부수 언급 - 떼어낼 신규 기법 없음
- **ID**: ieee:6392505
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Mohamed A. El-Shimy, Steve Hranilovic
- **PDF**: https://ieeexplore.ieee.org/document/6392505
- **Abstract**: There has been recent interest in establishing non-line-of-sight links in the solar-blind ultraviolet region for outdoor optical wireless communications. This paper presents a novel channel model combining both photon propagation and detection statistics. The channel capacity with binary inputs is numerically computed for on-off keying and 4-pulse-position modulation (4-PPM) at different baud rates. To approach the capacity, error control coding is applied and a message passing decoding technique is outlined. Simulation results for a running example through the paper indicate that, at a given power, there is an optimum transmitted baud rate that maximizes the achievable data rate on such links. With the application of proper coding techniques, it is demonstrated that a near fifty-fold increase in rate over previous reported designs for this channel is feasible.

## Effects of Channel Estimation on Spatial Modulation

- **Status**: ❌
- **Reason**: 공간변조 MIMO 채널추정 기법, LDPC ECC 무관 - 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:6319351
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Shinya Sugiura, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/6319351
- **Abstract**: In this letter, we investigate the effects of training-based channel estimation on the achievable performance of the recent spatial modulation (SM) based multiple-input multiple-output (MIMO) scheme. This is motivated by the fact that the SM transmitter is constituted by a single radio-frequency (RF) branch and multiple antenna elements (AEs), hence simultaneous pilot transmissions from the AEs are impossible, unlike in the classic multiple-RF MIMO transmitters. Our simulation results demonstrate that the SM scheme's BER curve exhibits a performance penalty, while relying on realistic imperfect channel-estimation. In order to combat these limitations, we propose two single-RF arrangements, namely a reduced-complexity joint channel estimation and data detection aided SM scheme as well as a non-coherently detected single-RF space-time shift keying scheme dispensing with channel estimation.

## Robust Distributed Storage of Residue Encoded Data

- **Status**: ❌
- **Reason**: Residue Number System 기반 분산 스토리지 부호; non-LDPC, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6293891
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Stefano Chessa, Piero Maestrini
- **PDF**: https://ieeexplore.ieee.org/document/6293891
- **Abstract**: We consider a problem where a physical quantity is repeatedly measured by replicated devices, yielding a stream of numerical data. Data are stored within the measuring devices and sporadically retrieved by a user. To avoid data losses due to large data streams with insufficient memory, the data are split into fragments, each of which is a compressed encoding of a number in the stream, and different fragments are stored in different, replicated devices. The devices are not allowed to communicate with each other, and they produce the local streams of fragments from independent measurements. Given the independence of measurements, the fragments are corrupted by independent errors, which are likely to be small integers, although errors of unbounded magnitude may also occur due to failures or to interferences. As devices may fail, or communication may be unreliable, the user may be unable to download fragments from some of the replicated devices, leading to fragment erasures. Our approach to the problem is to encode the data in a Residue Number System with Nonpairwise-Prime Moduli, named D-RNS-NPM. With n moduli and n residue digits, every replicated device is tied to a different modulus, with which it produces and stores a residue digit (i.e., a fragment) from the local measurement. Assuming an upper bound z, with z <; n, to the number of erasures, we show that the D-RNS-NPM guarantees the reconstruction of any number from a subset of at least n-z fragments. If fragments bear errors, whose magnitude is unrestricted for at most one error and upper bounded by a small δ for the others, reconstruction is within an approximation of ±δ, and this property is retained when errors cannot be detected due to the unbounded error multiplicity. The time complexity of the decoding algorithm is polynomial. This problem appears to be relevant in wireless sensor networks, and an application in this area is envisioned.

## Using Channel Output Feedback to Increase Throughput in Hybrid-ARQ

- **Status**: ❌
- **Reason**: Hybrid-ARQ throughput 개선+피드백 코드; FEC는 추상적, LDPC 특정 이식 기법 없음
- **ID**: ieee:6268356
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Mayur Agrawal, Zachary Chance, David J. Love +1
- **PDF**: https://ieeexplore.ieee.org/document/6268356
- **Abstract**: Hybrid automatic repeat request (ARQ) protocols have become common in many packet transmission systems due to their incorporation in various standards. Hybrid-ARQ combines the normal ARQ method with forward error correction (FEC) codes to increase reliability and throughput. In this paper, we look at improving upon this performance using feedback information from the destination, in particular, using a powerful FEC code in conjunction with a proposed linear feedback code for the Rayleigh block fading channels. The new hybrid-ARQ scheme is initially developed for full received packet feedback in a point-to-point link. It is then extended to various multiple-antenna scenarios [e.g., multiple-input single-output (MISO), multiple-input multiple-output (MIMO), etc.] with varying amounts of packet feedback information. Simulations illustrate gains in throughput.

## Approximating the LLR Distribution for a Class of Soft-Output MIMO Detectors

- **Status**: ❌
- **Reason**: MIMO soft 검출기 LLR 분포 근사(GMM); 검출기 통계 분석, LDPC 디코더/HW 이식 기법 없음
- **ID**: ieee:6296720
- **Type**: journal
- **Published**: Dec. 2012
- **Authors**: Mirsad Cirkic, Daniel Persson, Jan-Åke Larsson +1
- **PDF**: https://ieeexplore.ieee.org/document/6296720
- **Abstract**: We present approximations of the LLR distribution for a class of fixed-complexity soft-output MIMO detectors, such as the optimal soft detector and the soft-output via partial marginalization detector. More specifically, in a MIMO AWGN setting, we approximate the LLR distribution conditioned on the transmitted signal and the channel matrix with a Gaussian mixture model (GMM). Our main results consist of an analytical expression of the GMM model (including the number of modes and their corresponding parameters) and a proof that, in the limit of high SNR, this LLR distribution converges in probability towards a unique Gaussian distribution.

## Performance Research of Clipping LDPC-OFDM System Based on MMSE Iterative Reception Technology

- **Status**: ❌
- **Reason**: 클리핑 잡음 완화용 MMSE 반복수신/OFDM 응용 특이적; LLR-BP는 표준, 떼어낼 NAND LDPC 기법 없음
- **ID**: ieee:6429169
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: Liu Mingzhu, Zhang Haixia, Li Xin +1
- **PDF**: https://ieeexplore.ieee.org/document/6429169
- **Abstract**: One of the efficient ways to reduce the peak-to-average power ratio in multi-carrier system is clipping method, but it can cause the outspread of frequency spectrum, and then increase the nonlinear distortion and clipping noise. At the same time, it also can worsen the bit error ratio performance in multi-carrier system. In this paper, a nonlinear LDPC-OFDM system has been the research background for reducing the high clipping noise and distortion in clipping system. A novel algorithm named minimum mean square error (MMSE) iterative reception algorithm has been proposed in this paper, which is based on Ochiai clipping distortion mitigating algorithm and clipping distortion reconstructing iteration (CDRI) method. The MMSE iterative reception algorithm combined MMSE algorithm with iterative reception method to reduce clipping noise and distortion under various iteration times. At the same time, LLR-BP process has been intruded to decode LDPC and optimize BER performance. On the other hand, clipping process in LDPC-OFDM system has been mapped to a series of clipping index coding, and maximum likelihood (ML) decision algorithm has been used to recognize them.

## A novel family of nonbinary LDPC codes over finite fields

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 부호족; 비이진은 제외 대상
- **ID**: ieee:6755817
- **Type**: conference
- **Published**: 7-9 Dec. 2
- **Authors**: Lisheng Zhang, Lirui Tan, Fanxin Zeng
- **PDF**: https://ieeexplore.ieee.org/document/6755817
- **Abstract**: In this paper, a family of nonbinary LDPC codes over a finite field GF(q) is presented and its properties are derived. In comparison with the second method presented by Ref. [4], the simulation results show that in 16-ary (75,150), 64-ary (441,882) and 128-ary (1270,2540) LDPC code, the proposed LDPC codes have a slight higher coding gain, 0.25dB, 0.2dB, and 0.15 dB at the BER= 10-4, respectively, which demonstrates that the proposed nonbinary LDPC codes are valid.

## FPGA-based rapid prototyping platform for MIMO-BICM design space exploration

- **Status**: ❌
- **Reason**: MIMO-BICM FPGA 프로토타이핑 플랫폼, 무선 시스템 통합이며 이식할 LDPC 디코더 HW 기법 없음
- **ID**: ieee:6416748
- **Type**: conference
- **Published**: 5-7 Dec. 2
- **Authors**: Christina Gimmler-Dumont, Philipp Schläfer, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/6416748
- **Abstract**: FPGA-based rapid-prototyping becomes more and more important for the design space exploration of wireless systems. FPGA-based platforms allow faster system exploration with a high degree of flexibility. In this paper, we present a rapid-prototyping platform for double-iterative MIMO-BICM systems which belong to the most complex communication systems of current and future (4G, 5G) standards. Unified streaming interfaces simplify the connection of system components and the replacement of individual components without influencing the rest of the system. Hardware verification is often a very time-consuming task. Therefore, the platform offers special testing features. To the best of our knowledge, this is the first hardware implementation of a double-iterative MIMO-BICM system including channel preprocessing, MIMO detection and channel decoding.

## Adaptive coded modulation for nonlinear fiber-optical channels

- **Status**: ❌
- **Reason**: 비이진(non-binary 4D) LDPC coded modulation 광통신 응용, non-binary LDPC 제외
- **ID**: ieee:6477592
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Lotfollah Beygi, Erik Agrell, Magnus Karlsson
- **PDF**: https://ieeexplore.ieee.org/document/6477592
- **Abstract**: A low complexity hybrid polar low-density parity check (LDPC) coded modulation (CM) scheme is introduced for a single-wavelength fiber-optical channel. In the proposed scheme, we exploit a low complexity probabilistic shaping together with a four-dimensional (4D) mapping to reduce the complexity of a 4D non-binary LDPC CM scheme for fiber-optic channels. The proposed scheme has a flexible structure and it can be used as an adaptive-rate CM scheme. The numerical results show that the forward error correction (FEC) threshold of the introduced CM scheme can be significantly improved by probabilistic shaping with a negligible increase in the system complexity. In particular, the FEC threshold for the uncoded symbol error rate of the introduced CM scheme with 4D 16-ary quadrature amplitude modulation can be improved from 0.058 to 0.072 by exploiting a shaping overhead (redundancy) of 0.016 for an information bit error rate of 10-5.

## Write-margin improvement of non-binary LDPC coding and iterative decoding system in BPM R/W channel with write-errors

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC가 핵심 기여(write-margin 개선); 비이진 LDPC는 제외 대상
- **ID**: ieee:6503609
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Yasuaki Nakamura, Yoshihiro Okamoto, Hisashi Osawa +2
- **PDF**: https://ieeexplore.ieee.org/document/6503609
- **Abstract**: The write-margin of the iterative decoding systems for the binary and non-binary low-density parity-check (LDPC) codes are studied in the magnetic recording system using a bit-patterned medium (BPM) R/W channel with write-errors caused by the write-head field gradient, the media switching field distribution (SFD), the magnetization fields from adjacent islands, and the island position deviation. The performances of iterative decoding systems using the binary and non-binary LDPC codes are evaluated by computer simulation at an areal recording density of 2 Tb/inch2. The results show that the non-binary LDPC coding and iterative decoding system improves the write-margin compared with the binary LDPC system. Furthermore it is clarified that in order to obtain the sufficient write-margin, it is important to suppress the influence of the demagnetization fields from adjacent islands.

## Combined constrained code and LDPC code for long-haul fiber-optic communication systems

- **Status**: ❌
- **Reason**: 광섬유 통신용 constrained code+LDPC concatenation; LDPC는 표준 베이스라인이고 떼어낼 신규 디코더/구성/HW 기법 없음 (응용 특이적 inner code)
- **ID**: ieee:6503571
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Houbing Song, Maïté Brandt-Pearce, Tingjun Xie +1
- **PDF**: https://ieeexplore.ieee.org/document/6503571
- **Abstract**: In long-haul fiber-optic communication systems, the system performance is affected adversely by both severe physical impairments and amplified spontaneous emission (ASE) noise. Constrained coding, which avoids waveforms in the transmitted signal that are more likely to be detected incorrectly, has been proved to be an effective approach to suppress some physical impairments. However, the constrained coding schemes proposed in the literature are limited to the suppression of only some “resonant” sequences and their performance is evaluated in the absence of ASE noise. Various error correction codes also have been developed to reduce errors due to ASE noise but their performance is very vulnerable to the strong nonlinear impairments. This paper develops a novel concatenation scheme with the inner code being a constrained code based on Total Impairment Extent Rank (TIER) and the outer code being a low-density parity-check (LDPC) code. The TIER code ranks the bit patterns by order of all physical impairments imposed on them and constrains the bit patterns with large physical impairments. It is based on a discrete-time analytical model of physical impairments in long-haul fiber-optic communication systems. Compared with the current constrained codes, the TIER code offers more flexibility and better effectiveness. The TIER-LDPC concatenation scheme combines the strength of the TIER code in correcting errors due to physical impairments and that of the LDPC code in correcting memoryless errors due to ASE noise. Simulation results in the presence of ASE noise show that the TIER-LDPC concatenation scheme performs significantly better than the LDPC code alone in the case of severe impairments.

## Exploring controllable deterministic bits for LDPC iterative decoding in WiMAX networks

- **Status**: ❌
- **Reason**: WiMAX에서 deterministic bits(MPEG null packet)를 known info로 쓰는 디코딩; 응용/프로토콜 특이적이라 NAND에 이식할 일반 기법 아님
- **ID**: ieee:6503745
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Bo Rong, Yin Xu, Yiyan Wu +4
- **PDF**: https://ieeexplore.ieee.org/document/6503745
- **Abstract**: Low-density parity-check (LDPC) codes are playing an important role in modern wireless communication systems such as WiMAX due to their Shannon limit approaching error correction performance. To lower the decoding threshold of LDPC codes, this paper develops a novel multi-layer iterative decoding scheme using deterministic bits for multimedia communication systems. These deterministic bits serve as known information in the LDPC decoding process to reduce the redundancy during data transmission. Unlike the existing work, our proposed scheme addresses the controllable deterministic bits, such as MPEG null packets, rather than the widely investigated protocol headers. Simulation results show that our proposed scheme can achieve considerable gain in WiMAX networks.

## Multi-level compress and forward coding for half-duplex relays

- **Status**: ❌
- **Reason**: 릴레이용 compress-and-forward 다단부호+IRA, JSCC/distributed 소스-채널 결합으로 떼어낼 ECC 기법 없음
- **ID**: ieee:6503833
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Jaweria Amjad, Momin Uppal, Saad Qaisar
- **PDF**: https://ieeexplore.ieee.org/document/6503833
- **Abstract**: This paper presents a multi-level compress and forward coding scheme for a three-node relay network in which all transmissions are constrained to be from an M-ary PAM constellation. The proposed framework employs a uniform scalar quantizer followed by Slepian-Wolf coding at the relay. We first obtain a performance benchmark for the proposed scheme by deriving the corresponding information theoretical achievable rate. A practical coding scheme involving multi-level codes is then discussed. At the source node, we use multi-level low-density parity-check codes for error protection. At the relay node, we propose a multi-level distributed joint source-channel coding scheme that uses irregular repeat-accumulate codes, the rates of which are carefully chosen using the chain rule of entropy. For a block length of 2×105 symbols, the proposed scheme operates within 0.56 and 0.63 dB of the theoretical limits at transmission rates of 1.0 and 1.5 bits/sample, respectively.

## Structure-based decoding for hierarchically modulated, LDPC coded signals

- **Status**: ❌
- **Reason**: 계층변조 QAM 수신용 구조 디코딩(ILI 완화)으로 무선 응용 특이적, NAND LDPC BP로 떼어낼 부호비의존 기법 없음
- **ID**: ieee:6503748
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Zixia Hu, Hui Liu
- **PDF**: https://ieeexplore.ieee.org/document/6503748
- **Abstract**: In this paper, we present a structured LDPC decoding algorithm for hierarchical QAM modulation systems. Unlike the traditional hierarchical demodulation approaches which suffer from serious inter-layer interference (ILI), the proposed method exploits structure information of the secondary layer to mitigate the ILI impairment, thereby offers significant gains in reception performance. An achievable rate analysis is performed to calculate the theoretical limit of the basic layer in HM reception, which in certain cases is 8 dB better than the required SINR threshold for QAM detection with all Gaussian interference. The new algorithm has been implemented on a broadband in-band on-channel (IBOC) digital radio broadcasting system. Numerical results from both simulations and experiments are provided to quantify the performance advantages of the new algorithm against the DVB-T benchmark.

## Design of small rate, close to ideal, GLDPC-staircase AL-FEC codes for the erasure channel

- **Status**: ❌
- **Reason**: GLDPC-Staircase는 erasure 채널 AL-FEC, RS 결합 일반화 LDPC로 erasure/fountain 계열이며 NAND 채널 ECC로 떼어낼 기법 부족
- **ID**: ieee:6503433
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Ferdaouss Mattoussi, Vincent Roca, Bessem Sayadi
- **PDF**: https://ieeexplore.ieee.org/document/6503433
- **Abstract**: This work introduces the Generalized Low Density Parity Check (GLDPC)-Staircase codes for the erasure channel, that are constructed by extending LDPC-Staircase codes through Reed Solomon (RS) codes based on “quasi” Hankel matrices. This construction has several key benefits: in addition to the LDPC-Staircase repair symbols, it adds extra-repair symbols that can be produced on demand and in large quantities, which provides small rate capabilities. Additionally, with selecting the best internal parameters of GLDPC graph and under hybrid Iterative/Reed-Solomon/Maximum Likelihood decoding, the GLDPC-Staircase codes feature a very small decoding overhead and a low error floor. These excellent erasure capabilities, close to that of ideal, MDS codes, are obtained both with large and very small objects, whereas, as a matter of comparison, LDPC codes are known to be asymptotically good. Therefore, these properties make GLDPC-Staircase codes an excellent AL-FEC solution for many situations that require erasure protection such as media streaming.

## Channel codes for mitigating intersymbol interference in diffusion-based molecular communications

- **Status**: ❌
- **Reason**: 분자통신 ISI 대응 채널코드(ISI-free/반복부호), 비-LDPC 응용특이 부호로 이식 기법 없음
- **ID**: ieee:6503781
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Po-Jen Shih, Chia-han Lee, Ping-Cheng Yeh
- **PDF**: https://ieeexplore.ieee.org/document/6503781
- **Abstract**: Molecular communications emerges as a promising scheme for communication between nanoscale devices. In diffusion-based molecular communications, molecules as information symbols are released by transmitters and diffuse in the fluid or air environments to transmit messages. Under the diffusion channel modeled by Brownian motion, information sequences suffer from molecule crossovers, i.e., molecules released at an earlier time may arrive later, causing intersymbol interference (ISI). In this paper, we investigate practical channel codes for combating ISI. An ISI-free coding scheme is proposed to increase the communication reliability while keeping the encoding/decoding complexity reasonably low. We exemplify an ISI-free code and theoretically approximate its bit error rate (BER) performance. In addition, repetition codes are revisited out of the complexity concern and proved to be desirable. The BER approximations of the repetition code family are given as well. Compared with convolutional codes, the proposed ISI-free code and repetition codes offer comparable performance with much lower complexity for diffusion-based molecular communication systems.

## Constellation design for transmission over nonlinear satellite channels

- **Status**: ❌
- **Reason**: 비선형 위성 채널용 32-신호 constellation/labeling 최적화; LDPC ECC 기법 없음, 변조 설계라 떼어낼 게 없음
- **ID**: ieee:6503640
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Farbod Kayhan, Guido Montorsi
- **PDF**: https://ieeexplore.ieee.org/document/6503640
- **Abstract**: In this paper we use a variation of simulated annealing algorithm for optimizing two-dimensional constellations with 32 signals. The main objective is to maximize the symmetric pragmatic capacity under the peak-power constraint. The method allows the joint optimization of constellation and binary labeling. We also investigate the performance of the optimized constellation over nonlinear satellite channel under additive white Gaussian noise. We consider the performance over systems with and without pre-distorters. In both cases the optimized constellations perform considerably better than the conventional Amplitude Phase Shift Keying (APSK) modulations, used in the current digital video broadcasting standard (DVB-S2) on satellite channels. Based on our optimized constellations, we also propose a new labeling for the 4+12+16-APSK constellation of the DVB-S2 standard which is Gray over all rings.

## Joint compute and forward for the two way relay channel with spatially coupled LDPC codes

- **Status**: ❌
- **Reason**: two-way relay compute-and-forward의 SC-LDPC, erasure noise NC 응용으로 부호 비의존 이식 기법 없음, 무선/NC 특화 제외
- **ID**: ieee:6503465
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Brett Hern, Krishna Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/6503465
- **Abstract**: We consider the design and analysis of coding schemes for the binary input two way relay channel with erasure noise. We focus on reliable physical layer network coding as described in [1] in which the relay performs perfect error correction prior to forwarding messages. The best known achievable rates for this problem can be achieved through either decode and forward or compute and forward relaying. We consider a decoding paradigm called joint compute and forward which we numerically show can achieve the best of these rates with a single encoder and decoder. This is accomplished by deriving the exact performance of a message passing decoder based on joint compute and forward for spatially coupled LDPC ensembles.

## Linear programming based joint detection of LDPC coded MIMO systems

- **Status**: ❌
- **Reason**: MIMO LP 기반 결합검출+디코딩, MIMO 검출에 종속된 무선 응용 특이적 기법으로 NAND ECC 이식성 없음
- **ID**: ieee:6503749
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Yong Li, Lin Wang, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/6503749
- **Abstract**: In this work1, we present a new multiple-input-multiple-output (MIMO) receiver that integrates the MIMO signal detection and the decoding of low density parity check coded data. This joint MIMO detector and decoder utilizes linear programming and achieves about 9.0 dB gain over existing works in terms of bit error rate (BER) of 4 × 10−5 with comparable computational complexity. The proposed detector also outperforms the classic turbo equalizer by achieving up to 4.0 dB improvement over turbo equalizer at frame error rate (FER) of 1 × 104. In fact, we can achieve further gain by improving the proposed joint detector through the use of redundant parity checks.

## User cooperation via rateless coding

- **Status**: ❌
- **Reason**: rateless 협력통신 코드설계(차수분포), fountain/rateless 무선 응용으로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6503758
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Mahyar Shirvanimoghaddam, Yonghui Li, Branka Vucetic
- **PDF**: https://ieeexplore.ieee.org/document/6503758
- **Abstract**: This paper presents a new rateless coded cooperation (CC) scheme for the two-user cooperative multiple access channel (CMAC), where two users cooperatively communicate with a common destination. We consider two rateless CC strategies, a fully coded cooperation (FCC) scheme used in the conventional rateless cooperative schemes and a new partially coded cooperation (PCC) scheme. In FCC, each user starts coded cooperation process only after the whole block of the other user's information symbols are fully recovered. In contrast, in PCC, each user starts cooperation as soon as it receives a fraction of new message sent from the other user. The degree distribution for the PCC scheme is designed to maximize the overall system throughput. Simulation results show that the proposed PCC scheme achieves a considerably higher throughput than the conventional scheme in various scenarios.

## Iterative detection and decoding using approximate bayesian theorem based PDA method over MIMO Nakagami-m fading channels

- **Status**: ❌
- **Reason**: turbo-coded MIMO IDD용 PDA 검출기; turbo+검출기 기법으로 바이너리 LDPC BP에 이식되는 부호 비의존 기법 아님
- **ID**: ieee:6503672
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Shaoshi Yang, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/6503672
- **Abstract**: In this paper, the design of iterative detection and decoding (IDD) schemes relying on a low-complexity probabilistic data association (PDA) aided method is conceived for turbo-coded multiple-input multiple-output (MIMO) systems communicating over Nakagami-m fading channels. The known PDA based MIMO detectors typically operate purely in the probability-domain. We show that the classic relationship where the extrinsic LLRs are given by subtracting the a priori LLRs from the a posteriori LLRs does not hold for the existing PDA based MIMO detectors. Therefore, the PDA method is not readily applicable to the IDD receiver. To overcome this predicament, we propose an approximate Bayesian theorem based log-domain PDA (AB-Log-PDA) detector, as well as a novel simple approach of calculating the bit-wise extrinsic LLRs for the AB-Log-PDA, which makes the AB-Log-PDA well-suited for employment in IDD receivers. It is shown that the proposed AB-Log-PDA based IDD scheme is capable of achieving a comparable performance to that of the optimal maximum a posteriori (MAP) detector based IDD receiver, while imposing a much lower computational complexity in the scenarios considered.

## Performance analysis of code-aided iterative hard/soft decision-directed carrier phase recovery

- **Status**: ❌
- **Reason**: code-aided 반복 carrier phase recovery 성능 해석; 위상 동기화 응용 특이적이고 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:6503711
- **Type**: conference
- **Published**: 3-7 Dec. 2
- **Authors**: Nan Wu, Hua Wang, Zhixin Li +1
- **PDF**: https://ieeexplore.ieee.org/document/6503711
- **Abstract**: Code-aided (CA) iterative carrier phase synchronizer can improve the phase estimation performance significantly. However, due to the coupling involved between phase recovery and decoding, most studies depend on extensive simulations rather than on theoretical analysis to evaluate the performance of CA phase recovery. In this paper, we propose analytical methods to fill this void. The first step is to model the cross-talks caused by phase offset as an additional Gaussian noise at low signal-to-noise ratios (SNRs). Then, a semi-analytical method is proposed to express the distribution of extrinsic information from channel decoder as a function of phase offset. Building on this model, both the open-loop and closed-loop performance of CA iterative hard/soft decision-directed phase synchronizers are derived in closed-form. The analytical results explicitly reveal how extrinsic information contributes to the performance improvement of carrier phase estimation. Monte Carlo simulation results corroborate that the proposed methods are able to accurately characterize the performance of CA iterative carrier phase recovery for systems with different channel codes.

## Hardware architecture design of hybrid distributed video coding with frame level coding mode selection

- **Status**: ❌
- **Reason**: 분산 비디오코딩 HW, LDPC 엔진 부수적·DVC 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:6411963
- **Type**: conference
- **Published**: 3-6 Dec. 2
- **Authors**: Chieh-Chuan Chiu, Hsin-Fang Wu, Shao-Yi Chien +3
- **PDF**: https://ieeexplore.ieee.org/document/6411963
- **Abstract**: Distributed video coding (DVC), a new video coding paradigm based on Slepian-Wolf and Wyner-Ziv theories, is a promising solution for implementing low-power and low-cost distributed wireless video sensors since most of the computation load is moved from the encoder to the decoder. In this paper, the hardware architecture design of an efficient distributed video coding system, hybrid DVC with frame-level coding mode selection, is proposed. With the fully block-pipelined architecture, coding mode pre-decision, and specially-designed LDPC code engine, the proposed hardware is an efficient solution for distributed video sensors with high rate-distortion performance.

## Cooperative coding scheme using polar codes

- **Status**: ❌
- **Reason**: polar code 협력통신 코딩, 비-LDPC 부호이며 LDPC는 비교 베이스라인일 뿐, 떼어낼 기법 없음
- **ID**: ieee:6526009
- **Type**: conference
- **Published**: 29-31 Dec.
- **Authors**: Hui Kong, Chao Xing, Shengmei Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/6526009
- **Abstract**: Cooperative coding technique combines the channel coding technique to cooperative communications, and guarantees the high performance. Polar codes, proposed by Arikan in 2007, have been proven to be capacity-achieving codes with low encoding and decoding complexity. In the paper, we propose a cooperative coding scheme using polar codes. We present the cooperative coding schemes with amplify-forward (AF) mode and decode-forward (DF) mode, respectively. By numerical simulations, we compare the performance of the proposed schemes using polar codes with those schemes using low density parity check (LDPC) codes under the same conditions. The simulation results show that the performance of the proposed schemes with AF and DF modes has been improved significantly compared with those using LDPC codes. We also study the distance factor on the performance of the cooperative communication system. The results show the smaller the distance between R and S, the better the performance of the system is.

## Encrypted polar codes for wiretap channel

- **Status**: ❌
- **Reason**: polar code+암호화 wiretap 보안 스킴, 비-LDPC 부호+보안, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:6526004
- **Type**: conference
- **Published**: 29-31 Dec.
- **Authors**: Fantao Wu, Chao Xing, Shengmei Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/6526004
- **Abstract**: The wiretap channel proposed by Wyner is an important model of physical layer for security, where the channel between legal users (Alice and Bob) is called the main channel and the channel between eavesdropper and legal users is called eavesdropping channel. The channel coding technique has proven to good means to ensure the security of the Wyner wiretap channel. Recently, polar codes attract a lot of attentions due to their capacity-achieving property. In this paper, we propose a novel construction method for achieving more large secrecy capacity of wiretap channel with polar codes. In the scheme, we integrate encryption algorithm to the construction of polar code and prove the validity, reliability, and security of the proposed scheme in theory. Later, we present the transmission rate of the scheme by numerical simulations. The numerical simulation results show that the secrecy transmission rate can be improved significantly and a larger secrecy transmission rate could be achieved by the proposed scheme.

## Performance analysis of an LDPC coded FSO communication system with different modulation technique under turbulent condition

- **Status**: ❌
- **Reason**: FSO 통신 LDPC coded BER 분석, 변조기법 비교만, 떼어낼 ECC 기법 없음 무선응용 특이
- **ID**: ieee:6509706
- **Type**: conference
- **Published**: 22-24 Dec.
- **Authors**: Bobby Barua, S. P. Majumder
- **PDF**: https://ieeexplore.ieee.org/document/6509706
- **Abstract**: Free-space optical (FSO) communication is an attractive and cost-effective solution for high-rate image, voice, and data transmission than an RF channel. Atmospheric turbulence-induced fading is one of the main impairments affecting FSO communications. To design a high performance communication link for the atmospheric FSO channel, it is of great importance to characterize the link with proper model. Different modulation techniques have already been proposed for FSO communication in various publications. In this paper, an analytical approach is presented to evaluate the bit error rate performance of an LDPC coded FSO communication employing on-off keying (OOK), binary phase-shift keying (BPSK) and Q-ary pulse position (QPPM) as modulation technique. The performance results are evaluated in terms of bit error rate (BER). It is found that LDPC coded FSO system with QPPM provides significant coding gain over uncoded system compare than other modulation techniques.

## LDPC coded FSO communication system under strong turbulent condition

- **Status**: ❌
- **Reason**: FSO 통신 응용 특이적, 표준 LDPC를 iterative demapping에 사용한 수준으로 떼어낼 ECC 기법 없음
- **ID**: ieee:6471575
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Bobby Barua, S. P. Majumder
- **PDF**: https://ieeexplore.ieee.org/document/6471575
- **Abstract**: Atmospheric turbulence-induced fading is one of the main impairments affecting free-space optics (FSO) communications. To design a high-performance communication link for the atmospheric FSO channel, it is of great importance to characterize the channel from the perspective of information and coding theory. In this paper, we consider FSO multiple-input multiple-output (MIMO) channel with Q-ary pulse position modulation (QPPM) and transmit repetition under the assumption of non-ideal photodetection is analyzed in terms of its ergodic channel capacity. Instead of using a simple binary channel code, we suggest using low density parity-check (LDPC) code to perform iterative soft demodulation (demapping) and channel decoding at the receiver. The simulation results confirm the analytical findings of this paper.

## Turbo like multi-stage threshold decoding for self-orthogonal convolutional codes

- **Status**: ❌
- **Reason**: 비-LDPC(자기직교 컨볼루션 부호) 임계디코딩, 부호 의존적 기법으로 바이너리 LDPC BP 이식 불가
- **ID**: ieee:6471574
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: Muhammad Ahsan Ullah, Haruo Ogiwara
- **PDF**: https://ieeexplore.ieee.org/document/6471574
- **Abstract**: This paper presents a new dimension of soft decoding turbo-like multi-stage threshold decoding (TLMTD) for self-orthogonal convolutional codes (SOCCs). The TLMTD uses comparatively shorter constraint length conventional code of multi-stage threshold decoding (MTD) system. The bit error performance is considered for several types of soft decoding algorithms on the additive white Gaussian noise (AWGN) channel. When threshold value used as a priori threshold value for other decoding stage, TLMTD realizes better performance in waterfall and error floor regions. Moreover, the TLMTD gives 0.20 dB more coding gain compared to MTD for equivalent SOCCs at the bit error rate less than 10-4.

## An efficient majority-logic based message-passing algorithm for non-binary LDPC decoding

- **Status**: ❌
- **Reason**: non-binary LDPC majority-logic 메시지패싱; 비이진 LDPC라 제외
- **ID**: ieee:6419076
- **Type**: conference
- **Published**: 2-5 Dec. 2
- **Authors**: Yichao Lu, Nanfan Qiu, Zhixiang Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6419076
- **Abstract**: This paper presents a majority-logic based message-passing algorithm for decoding non-binary LDPC codes. Recently, many majority-logic decoding (MLGD) algorithms make huge efforts on reducing the computational complexity for decoding non-binary LDPC codes. Inspired by one step majority-logic decoding and q-ary sum-product algorithm, we devise a novel iterative double-reliability-based (IDRB) MLGD algorithm which carries out an efficient trade-off between decoding computational complexity and error performance. The proposed algorithm achieves a remarkable enhancement on error correct ability and yet requires only integer operations and finite field operations. Simulation results on two NB-LDPC codes show that we succeed in achieving significant coding gain compared with IHRB- and ISRB-MLGD with limited complexity increase.

## A novel hardware-oriented decoding algorithm for non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary GF(2^m)) LDPC 디코딩 알고리즘 — 비이진 LDPC 제외 대상
- **ID**: ieee:6419056
- **Type**: conference
- **Published**: 2-5 Dec. 2
- **Authors**: Hong Yang, Qing-qing Yang, Yuanwei Fang +2
- **PDF**: https://ieeexplore.ieee.org/document/6419056
- **Abstract**: This paper presents a novel hardware-oriented decoding algorithm in the log-domain for non-binary LDPC codes over GF(2m). As for max-log-SPA, only summations and comparisons are required in this new algorithm. During the vertical update, these two operations are divided into layers based on the distribution of variable vectors that satisfy the check function. The number of additions during the vertical update is reduced by a factor of approximately p-2 without a performance loss, where p is the row weight of the parity check matrix.

## Performance analysis of cooperative LDPC coding for wireless network

- **Status**: ❌
- **Reason**: 무선 협력통신 다이버시티용 LDPC, 떼어낼 디코더·구성 기법 없음
- **ID**: ieee:6524244
- **Type**: conference
- **Published**: 16-19 Dec.
- **Authors**: Thomas Chowdhury, Asaduzzaman
- **PDF**: https://ieeexplore.ieee.org/document/6524244
- **Abstract**: Cooperative communication represents a way of achieving diversity in wireless network. Cooperative coding is a channel code that exploits user cooperation gains. In this paper we present LDPC codes that have the capability of providing full cooperation diversity, while achieving maximum possible diversity gain and coding gain. We analyze the performance of cooperative communication with LDPC codes over noncooperative or direct communication in Rayleigh fading channel. A traditional three node model is developed to analyze the performance where relay helps to do the cooperative communication. We illustrate that cooperative LDPC codes offers more than 3 dB gain over direct transmission in the high SNR region for MPSK and MQAM modulation even when the inter-user channel is noisy.

## Soft Interference Cancellation for Nonbinary LDPC Coded Multicarrier MFSK Multiple Access Systems over Rayleigh Fading Channel

- **Status**: ❌
- **Reason**: 비이진(nonbinary GF) LDPC + 무선 MFSK 다중접속 소프트간섭제거, 바이너리 LDPC 비대상
- **ID**: ieee:6519542
- **Type**: conference
- **Published**: 12-16 Dec.
- **Authors**: Szu-Lin Su, Her-Chang Tsai, Ye-Shun Shen
- **PDF**: https://ieeexplore.ieee.org/document/6519542
- **Abstract**: This paper studies an iterative multiuser detection for nonbinary LDPC coded multicarrier MFSK multiple access system to increase system performance under specific signal-to-noise ratio and data rate. When multiuser detection process is carried out, we test the soft outputs of channel decoder. When the soft output exceeds a threshold, the user is declared as a reliable user. For each signal, we count the number of reliable users on it. The reliable information iteratively updates the soft output calculation in the iterative demodulation and decoding process. Numerical results show that system performances are improved after multiuser detection over Rayleigh fading channel.
