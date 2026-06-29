# IEEE Xplore — 2017-05


## Two-Extra-Column Trellis Min–Max Decoder Architecture for Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(32)) trellis min-max 디코더, 바이너리 LDPC 아님→제외
- **ID**: ieee:7822934
- **Type**: journal
- **Published**: May 2017
- **Authors**: Huyen Pham Thi, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/7822934
- **Abstract**: In this brief, a novel two-extra-column trellis min-max algorithm and the decoder architecture based on only the first minimum values are proposed for nonbinary low-density parity-check (NB-LDPC) codes. The algorithm greatly reduces the hardware complexity and improves the latency as well as the throughput of the proposed decoder architecture compared with the previous works. A layered decoder architecture based on the proposed algorithm for (837, 726) NB-LDPC code over GF(32) is implemented with a 90-nm CMOS technology. The results show a decrease in the area of 24.6% for the check node unit and 75.6% for the whole decoder with a throughput of 1.27 Gb/s. The proposed decoder provides a lower area and a higher efficiency compared with the state of the art of high-rate NB-LDPC codes with high Galois-field order.

## On the VLSI Energy Complexity of LDPC Decoder Circuits

- **Status**: ❌
- **Reason**: LDPC 디코더 회로 에너지 복잡도 하한 이론, 디코더/HW/구성 신규 기법으로 안 이어짐
- **ID**: ieee:7862885
- **Type**: journal
- **Published**: May 2017
- **Authors**: Christopher G. Blake, Frank R. Kschischang
- **PDF**: https://ieeexplore.ieee.org/document/7862885
- **Abstract**: Sequences of randomly generated bipartite configurations are analyzed; under mild conditions almost surely such configurations have minimum bisection width proportional to the number of vertices. This implies an almost sure Ω(n2/dmax2) scaling rule for the energy of directlyimplemented low-density parity-check (LDPC) decoder circuits for codes of block length n and maximum node degree dmax. It also implies an Ω(n3/2/dmax) lower bound for serialized LDPC decoders. It is also shown that all (as opposed to almost all) capacity-approaching, directly-implemented non-split-node LDPC decoding circuits, have energy, per iteration, that scales as Ω(χ2 ln3 χ), where χ = (1 - R/C)-1 is the reciprocal gap to capacity, R is code rate, and C is channel capacity.

## Symbol Flipping Decoding Algorithms Based on Prediction for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC symbol flipping 예측 알고리즘, 바이너리 LDPC 아님→제외
- **ID**: ieee:7869258
- **Type**: journal
- **Published**: May 2017
- **Authors**: Shuai Wang, Qin Huang, Zulin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7869258
- **Abstract**: This paper constructs an objective function for symbol flipping decoding algorithms, considering not only soft reliability, but also hard reliability. The maximization of this objective function indicates that the flipping metric should involve both the information before and after symbol flipping, while the existing algorithms consider the information before symbol flipping. Theoretical analysis shows that such prediction mechanism, together with hard reliability, can significantly improve the error performance of symbol flipping algorithms. Simulation results show that the proposed algorithms provide effective tradeoff between error performance and complexity for decoding non-binary LDPC codes.

## Reconstruction Guarantee Analysis of Basis Pursuit for Binary Measurement Matrices in Compressed Sensing

- **Status**: ❌
- **Reason**: 압축센싱 바이너리 측정행렬 복원보장 이론, 채널 ECC 디코더 기법 아님
- **ID**: ieee:7870658
- **Type**: journal
- **Published**: May 2017
- **Authors**: Xin-Ji Liu, Shu-Tao Xia, Fang-Wei Fu
- **PDF**: https://ieeexplore.ieee.org/document/7870658
- **Abstract**: Recently, binary 0-1 measurement matrices, especially those from coding theory, were introduced to compressed sensing. Dimakis et al. found that the linear programming (LP) decoding of LDPC codes is very similar to the LP reconstruction of compressed sensing, and they further showed that the sparse binary parity-check matrices of good LDPC codes can be used as provably good measurement matrices for compressed sensing under basis pursuit (BP). Moreover, Khajehnejad et al. made use of girth to certify the good performances of sparse binary measurement matrices. In this paper, we examine the performance of binary measurement matrices with uniform column weight and arbitrary girth under BP. For a fixed measurement matrix, we first introduce a performance indicator wminBP called minimum BP weight, and show that any k-sparse signals could be exactly recovered by BP if and only if k ≤ (wminBP - 1)/2. Then, lower bounds of wminBP are studied. Borrowing ideas from the tree bound for the LDPC codes, we obtain several explicit lower bounds of wBPmin, which improve on the previous results in some cases. These lower bounds also imply explicit ℓ1/ℓ1, ℓ2/ℓ1 and ℓ∞/ℓ1 sparse approximation guarantees, and further confirm that large girth has positive impacts on the performance of binary measurement matrices under BP.

## Jointly Optimized Reed–Muller Codes for Multilevel Multirelay Coded-Cooperative VANETS

- **Status**: ❌
- **Reason**: Reed-Muller 부호 협력통신 설계, LDPC 아님·떼어낼 BP 기법 없음
- **ID**: ieee:7556365
- **Type**: journal
- **Published**: May 2017
- **Authors**: Saqib Ejaz, Yang FengFan
- **PDF**: https://ieeexplore.ieee.org/document/7556365
- **Abstract**: In this paper, we present the well-known Reed-Muller (RM) codes for multilevel multirelay vehicular adhoc networks, which can enjoy coded-cooperation among network nodes. At first, we present the code construction principles for a single node/relay scenario and then extend the design principles to the two-level two-relay and, finally, to multilevel multirelay scenarios. The term “level” refers to the fact that different order RM code is used at each relaying node. Plotkin's construction is exploited to utilize RM codes in such coded-cooperative schemes. To achieve an optimum code at the destination node, proper encoding strategy needs to be employed at the relay node. Therefore, we propose a design criteria and an efficient algorithm for proper bit selection at the relay nodes to achieve the best possible code at the destination. It is observed that the increase in the number of levels as well as relays result in better channel code at the destination, as compared to the lesser number of relays, however, at the cost of increased decoding complexity. The channels considered to analyze the bit error rate (BER) performances of proposed coded-cooperative schemes are fast and slow Rayleigh fading channels. At the destination, soft decision maximum likelihood decoding is employed. Numerical simulations show that the single-relay RM coded-cooperative scheme provides significant BER performance gains over the noncooperative and state-of-the-art distributed turbo coded-cooperative schemes under identical conditions.

## MIMO Sphere Decoding With Successive Interference Cancellation for Two-Dimensional Non-Uniform Constellations

- **Status**: ❌
- **Reason**: MIMO 구면디코딩/NUC 디매핑, 채널부호 ECC 아님·LDPC 무관
- **ID**: ieee:7819430
- **Type**: journal
- **Published**: May 2017
- **Authors**: Carlos Barjau, Manuel Fuentes, Takuya Shitomi +1
- **PDF**: https://ieeexplore.ieee.org/document/7819430
- **Abstract**: Non-uniform constellations (NUCs) have been introduced to improve the performance of quadrature amplitude modulation constellations. 1D-NUCs keep the squared shape, while 2D-NUCs break that constraint to provide robustness. An impending problem with multiple-input multiple-output (MIMO) is the optimum demapping complexity, which grows exponentially with the number of antennas and the constellation order. Some well-known sub-optimum MIMO demappers, such as soft fixed-complexity sphere decoders (SFSD), can reduce that complexity. However, SFSD demappers do not work with the 2D-NUCs, since they perform a quantization step in separated I/Q components. In this letter, we provide an efficient solution for the 2D-NUCs based on Voronoi regions. Both complexity implications and SNR performance are also analyzed.

## Almost Universal Codes Achieving Ergodic MIMO Capacity Within a Constant Gap

- **Status**: ❌
- **Reason**: MIMO lattice 부호 용량격차 수론적 설계, LDPC 무관
- **ID**: ieee:7879826
- **Type**: journal
- **Published**: May 2017
- **Authors**: Laura Luzzi, Roope Vehkalahti
- **PDF**: https://ieeexplore.ieee.org/document/7879826
- **Abstract**: This paper addresses the question of achieving capacity with lattice codes in multi-antenna block fading channels when the number of fading blocks tends to infinity. A design criterion based on the normalized minimum determinant is proposed for division algebra multi-block space-time codes over fading channels; this plays a similar role to the Hermite invariant for Gaussian channels. Under maximum likelihood decoding, it is shown that this criterion is sufficient to guarantee transmission rates within a constant gap from capacity both for deterministic channels and ergodic fading channels. Moreover, if the number of receive antennas is greater than or equal to the number of transmit antennas, the same constant gap is achieved under naive lattice decoding as well. In the case of independent identically distributed Rayleigh fading, the error probability vanishes exponentially fast. In contrast to the standard approach in the literature, which employs random lattice ensembles, the existence results in this paper are derived from the number theory. First, the gap to capacity is shown to depend on the discriminant of the chosen division algebra; then, class field theory is applied to build families of algebras with small discriminants. The key element in the construction is the choice of a sequence of division algebras whose centers are number fields with small root discriminants.

## Probabilistic Equalization With a Smoothing Expectation Propagation Approach

- **Status**: ❌
- **Reason**: EP 기반 소프트 이퀄라이저, LDPC는 베이스라인 디코더로만 사용·떼어낼 ECC 기법 없음
- **ID**: ieee:7880668
- **Type**: journal
- **Published**: May 2017
- **Authors**: Irene Santos, Juan José Murillo-Fuentes, Eva Arias-de-Reyna +1
- **PDF**: https://ieeexplore.ieee.org/document/7880668
- **Abstract**: In this paper, we face the soft equalization of channels with inter-symbol interference for large constellation sizes, M. In this scenario, the optimal BCJR solution and most of their approximations are intractable, as the number of states they track grows fast with M. We present a probabilistic equalizer to approximate the posterior distributions of the transmitted symbols using the expectation propagation (EP) algorithm. The solution is presented as a recursive sliding window approach to ensure that the computational complexity is linear with the length of the frame. The estimations can be further improved with a forward-backward approach. This novel soft equalizer, denoted as smoothing EP (SEP), is also tested as a turbo equalizer, with a low-density parity-check (LDPC) channel decoder. The extensive results reported reveal remarkably good behavior of the SEP. In low dimensional cases, the bit error rate (BER) curves after decoding are closer than 1 dB from those of the BJCR, robust to the channel response. For large M, the SEP exhibits gains in the range of 3-5 dB compared to the linear minimum mean square error algorithm.

## Opportunistic automotive radar using the IEEE 802.11ad standard

- **Status**: ❌
- **Reason**: 802.11ad 기회적 차량 레이더 탐지/추정, ECC 무관
- **ID**: ieee:7944386
- **Type**: conference
- **Published**: 8-12 May 2
- **Authors**: Emanuele Grossi, Marco Lops, Luca Venturino +1
- **PDF**: https://ieeexplore.ieee.org/document/7944386
- **Abstract**: In this work, we focus on vehicular networks employing the IEEE 802.11ad standard and show the feasibility of an opportunistic radar system. The echo generated by the beacon transmitted during the sector level sweep of the beamforming protocol is exploited to perform target detection and range/velocity estimation. Two solutions, which differ in the amount of prior information on the transmitted waveform, are developed, and numerical results showing their detection and estimation performance are provided.

## Interference mitigation in coexistence of WLAN network with radar

- **Status**: ❌
- **Reason**: WLAN-레이더 공존 간섭완화용 인터리버+LLR 매핑; 표준 802.11n/ac LDPC 사용, 응용 특이적 새 LDPC ECC 기법 없음
- **ID**: ieee:7944208
- **Type**: conference
- **Published**: 8-12 May 2
- **Authors**: Morteza Mehrnoush, Sumit Roy
- **PDF**: https://ieeexplore.ieee.org/document/7944208
- **Abstract**: Coexistence between 802.11 wireless local area network (WLAN) and radars operating in co/adjacent channel scenarios (notably 5 GHz) is a problem of considerable importance that requires new innovations. We propose a modified Wi-Fi link design that mitigates the interference from a pulsed search radar such that the WLAN network continues to operate outside the exclusion region with no noticeable performance degradation. For low density parity check (LDPC) encoding adopted in high throughput WLANs such as 802.11n and .ac, the modified receiver includes a new interleaver and a log-likelihood ratio (LLR) mapping function to successfully mitigate the impact of radar interference. We evaluate, via simulations, the impact of interleaver length and LLR mapping function parameters to determine the optimum combination that yields the desirable frame error rate (FER) performance.

## PAPR reduction with invertible subset LDPC codes in downlink OFDMA systems

- **Status**: ❌
- **Reason**: IS-LDPC를 OFDMA PAPR 저감에 응용 — LDPC가 송신 부수 용도, NAND ECC로 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:8230157
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Bo Wang, Daiming Qu
- **PDF**: https://ieeexplore.ieee.org/document/8230157
- **Abstract**: A new family of low density parity-check (LDPC) codes, called as invertible subset LDPC (IS-LDPC) codes, was proposed for peak-to-average power ratio (PAPR) reduction in OFDM systems recently. In this paper, we propose a PAPR reduction scheme for orthogonal frequency-division multiple access (OFDMA) systems based on IS-LDPC codes. The proposed scheme maps the invertible subsets of IS-LDPC codewords onto subcarriers to construct invertible symbol subsets. Then, the invertible symbol subsets are inverted independently for reducing the PAPR of downlink OFDMA systems. There is no need to transmit the side information by extra channels, which significantly reduces the system overhead and eases the system design. Simulation results show that the PAPR reduction scheme based on IS-LDPC codes produces remarkable PAPR reduction performance and good error correction performance in downlink OFDMA systems. Therefore, the proposed PAPR reduction scheme could be an efficient solution to reduce the PAPR of downlink OFDMA systems.

## LDPC code design for quadrature-quadrature phase shift keying

- **Status**: ❌
- **Reason**: UAV 다운링크용 LDPC+Q2PSK 변조 결합 설계, 통신 응용 특이적이라 이식 기법 없음
- **ID**: ieee:8230070
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Fei Wang, Jian Liu, Shuai Wang
- **PDF**: https://ieeexplore.ieee.org/document/8230070
- **Abstract**: We introduce a model of a combination of particular low density parity check (LDPC) code and quadrature-quadrature phase shift keying (Q2PSK) constellation for the application of the downlink of the unmanned aerial vehicle (UAV) data chain. This model is a modification of the combination of LDPC code and constant envelope Q2PSK (CEQ2PSK) constellation. It achieves higher bandwidth efficiency of 4/3 times while ensures high power utilization and not increases the complexity of the algorithm implementation. The encoding algorithm of the particular LDPC code which can make the envelope of the output signal of Q2PSK to be a constant is the focal point of this paper. However, the model we proposed suffers from a loss of about 0.82dB compared with the unmodified model at bit error rate (BER) of 10-6. Considering the downlink is mainly used to transmit telemetry image data, and the impact of 0.82dB on such data is reflected by the fact that the images restored at the receiving end are slightly blurred, so we believe that it is acceptable to use the sacrifice of 0.82dB reliability for higher bandwidth efficiency.

## Video steganography techniques: Taxonomy, challenges, and future directions

- **Status**: ❌
- **Reason**: 비디오 스테가노그래피 서베이 — LDPC/ECC와 무관
- **ID**: ieee:8001965
- **Type**: conference
- **Published**: 5-5 May 20
- **Authors**: Ramadhan J. Mstafa, Khaled M. Elleithy, Eman Abdelfattah
- **PDF**: https://ieeexplore.ieee.org/document/8001965
- **Abstract**: Nowadays, video steganography has become important in many security applications. The performance of any steganographic method ultimately relies on the imperceptibility, hiding capacity, and robustness. In the past decade, many video steganography methods have been proposed; however, the literature lacks of sufficient survey articles that discuss all techniques. This paper presents a comprehensive study and analysis of numerous cutting edge video steganography methods and their performance evaluations from literature. Both compressed and raw video steganographic methods are surveyed. In the compressed domain, video steganographic techniques are categorized according to the video compression stages as venues for data hiding such as intra frame prediction, inter frame prediction, motion vectors, transformed and quantized coefficients, and entropy coding. On the other hand, raw video steganographic methods are classified into spatial and transform domains. This survey suggests current research directions and recommendations to improve on existing video steganographic techniques.

## Multi-track 2D joint signal detection and decoding for TDMR system using single parity-check coding

- **Status**: ❌
- **Reason**: TDMR 2D BCJR 검출+single parity check 코딩 — LDPC 아닌 SPC, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:7946623
- **Type**: conference
- **Published**: 30 April-3
- **Authors**: Mohammed D. Almustapha, Mohammed Z. Ahmed, Marcel A. Ambroze +1
- **PDF**: https://ieeexplore.ieee.org/document/7946623
- **Abstract**: A combination of single parity check-code and Two-Dimensional (2D) Bahl Cocke Jelinek Raviv (BCJR) detector is used in this paper for joint detection and decoding of 2D interference channel. This is applied to a multi-track two dimensional magnetic recording (TDMR) system. The multi-level 2D BCJR detector handled the code constraint while performing joint detection and single parity decoding. Two coding approaches are presented in this paper: 1) parity bits are applied along-track direction only, separated with a dithered relative prime (DRP) interleaver, and 2) parity bits are applied in both along-track and across-tracks directions. The results show that the new constrained coded multi-track 2D BCJR joint detector provides improved performance with low detection complexity.

## Experimental Alamouti-STBC using LDPC codes for MIMO channels over SDR systems

- **Status**: ❌
- **Reason**: MIMO Alamouti-STBC에 LDPC 부수 적용, 표준 LDPC 사용 — 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:7946842
- **Type**: conference
- **Published**: 30 April-3
- **Authors**: Ricardo Prieto, Ana Abril, Andres Ortega
- **PDF**: https://ieeexplore.ieee.org/document/7946842
- **Abstract**: The legacy access networks should provide higher capacity, rate and spectral efficiency due to high demand of data transmission. In this context our proposal is the combining of LDPC codes with MIMO systems channels in order to improve the reliability and capacity in the transmission for massive connectivity. This system is proposed for the development of new technologies over SDR systems. MIMO techniques such as Alamouti-STBC offer some benefits such as greater network access capabilities that help to make transmission more reliable, while LDPC codes give higher transmission reliability because they have a good error correction codes and offer an approximation to the limit of capacity established by Shannon. The results show that the BER performance and the capacity improves when the Rayleigh channel is used. In this context, the system can support high quality of information and high rates in the transmission. In addition, we present the techniques of frame synchronization for real transmission as Barker codes, in order to reduce the error of transmission.

## BER comparison between Convolutional, Turbo, LDPC, and Polar codes

- **Status**: ❌
- **Reason**: Conv/Turbo/LDPC/Polar BER 비교 연구 — 표준 부호 단순 비교, 신규 디코더·구성 기여 없음
- **ID**: ieee:7998249
- **Type**: conference
- **Published**: 3-5 May 20
- **Authors**: Bashar Tahir, Stefan Schwarz, Markus Rupp
- **PDF**: https://ieeexplore.ieee.org/document/7998249
- **Abstract**: Channel coding is a fundamental building block in any communications system. High performance codes, with low complexity encoding and decoding are a must-have for future wireless systems, with requirements ranging from the operation in highly reliable scenarios, utilizing short information messages and low code rates, to high throughput scenarios, working with long messages, and high code rates. We investigate in this paper the performance of Convolutional, Turbo, Low-Density Parity-Check (LDPC), and Polar codes, in terms of the Bit-Error-Ratio (BER) for different information block lengths and code rates, spanning the multiple scenarios of reliability and high throughput. We further investigate their convergence behavior with respect to the number of iterations (turbo and LDPC), and list size (polar), as well as how their performance is impacted by the approximate decoding algorithms.

## Algorithm and architecture for joint detection and decoding for MIMO with LDPC codes

- **Status**: ❌
- **Reason**: MIMO 결합 검출/복호(JDD) - K-best 트리탐색 가지치기는 MIMO 검출 특이적, NAND ECC로 떼어낼 LDPC 기법 없음
- **ID**: ieee:8050314
- **Type**: conference
- **Published**: 28-31 May 
- **Authors**: Shusen Jing, Junmei Yang, Zhongfeng Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/8050314
- **Abstract**: With better spectral efficiency, multiple-input and multiple-output (MIMO) systems have drawn increasing attentions. Due to its near-optimal performance, K-best algorithm has been widely adopted for MIMO detection. To the best knowledge of the authors, this paper first proposes a joint detection and decoding (JDD) method for MIMO with low-density parity-check (LDPC) codes. By pruning the searching tree of K-best detection with LDPC coding constraint, the proposed JDD scheme benefits from both reduced tree-search complexity and improved performance compared to its uncoded MIMO counterpart. Numerical results of 16-QAM MIMO with (8, 2) LDPC code and 64-QAM MIMO with (18, 6) LDPC code have shown that, the proposed JDD scheme's performance is evidently superior over separated detection and decoding (SDD) scheme. More specifically, for the latter case with 12 antennas, JDD shows nearly 10 dB performance improvement than SDD when BER = 10-3. Hardware architecture and complexity analysis are also given in this paper to demonstrate JDD's advantages.

## QoS in industrial wireless networks using LDM

- **Status**: ❌
- **Reason**: 산업용 무선망 QoS/LDM 통신 시스템 논문, LDPC 부수 언급도 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:7945910
- **Type**: conference
- **Published**: 24-26 May 
- **Authors**: Egoitz Arruti, Mikel Mendicute, Maitane Barrenechea
- **PDF**: https://ieeexplore.ieee.org/document/7945910
- **Abstract**: One of the main challenges in mechatronics is to manage large amount of information data. This information is used to control the process, manage critical errors or perform maintenance actions. The traditional communication buses are wired buses which have great reliability. But with the revolution of industry 4.0, industry and mechatronic systems increased sensor and data acquisition nodes, from few devices to several sensors and actuators interconnected between them. In this new scenario the traditional wired communications systems are more complex to deploy and to maintain, and the trend is to replace wired by wireless systems, ensuring that the reliability of the wireless systems is comparable to the wired one. A communication system based on LDM (Layered Division Multiplexing) is proposed in this article to guarantee the reliability level of a wireless system where two types of data need to be transmitted over the same physical layer, critical data and non critical data. In order to prove that the proposed system is more reliable than the traditional TDM/FDM systems and can enhance throughput, BER and throughput simulations are provided.

## An impulsive noise resistant physical layer for smart grid communications

- **Status**: ❌
- **Reason**: 임펄스노이즈 물리계층에 LRPC(rank metric)·polar; 비-LDPC, 무선 특이적
- **ID**: ieee:7996876
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Ndéye Bineta Sarr, Abdul Karim Yazbek, Herve Boeglen +3
- **PDF**: https://ieeexplore.ieee.org/document/7996876
- **Abstract**: Integrating wireless sensor networks (WSNs) in power substations for the future smart grid is growing in interest. Nevertheless, high voltage (HV) substations are harsh environments. In particular, impulsive noise needs to be taken into account. To tackle the constraints of these environments, we propose in this paper an efficient wideband channel coding scheme. The proposed approach consists in a robust physical layer based on the integration of several very interesting error correcting codes with Orthogonal Frequency Division Multiplexing (OFDM). Using real measurements of impulsive noise, the impact of rank metric (RC), Low Rank Parity Check codes (LRPC) and polar codes is evaluated in terms of BER and PER in a realistic multipath channel. The results show that using this coding scheme is very efficient in mitigating the bursty nature of impulsive noise while having a quite low level of complexity.

## Stochastic resonance decoding for quantum LDPC codes

- **Status**: ❌
- **Reason**: 양자 LDPC(CSS/dual-containing) 확률공명 디코딩; 노이즈게이트 회로·양자 전용 개념 의존
- **ID**: ieee:7996747
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Nithin Raveendran, Priya J. Nadkarni, Shayan Srinivasa Garani +1
- **PDF**: https://ieeexplore.ieee.org/document/7996747
- **Abstract**: We introduce a stochastic resonance based decoding paradigm for quantum codes using an error correction circuit made of a combination of noisy and noiseless logic gates. The quantum error correction circuit is based on iterative syndrome decoding of quantum low-density parity check codes, and uses the positive effect of errors in gates to correct errors due to decoherence. We analyze how the proposed stochastic algorithm can escape from short cycle trapping sets present in the dual containing Calderbank, Shor and Steane (CSS) codes. Simulation results show improved performance of the stochastic algorithm over the deterministic decoder.

## Non-binary LDPC codes for orthogonal modulations: Analysis and code design

- **Status**: ❌
- **Reason**: 직교변조용 비이진 LDPC ensemble 설계; 비이진 제외
- **ID**: ieee:7996749
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Gianluigi Liva, Balazs Matuz, Enrico Paolini +1
- **PDF**: https://ieeexplore.ieee.org/document/7996749
- **Abstract**: In this paper, we present a low-density parity-check coded modulation approach addressing orthogonal modulations with moderate order (between 8 and 32) over the additive white Gaussian noise channel. The proposed design is based on a constrained optimization of a non-binary low-density parity-check ensemble degree distribution, where the iterative decoding threshold is optimized via extrinsic information transfer analysis while restricting the search to degree distributions that target low error floors. For various orthogonal modulation orders, we provide useful approximations to the extrinsic information transfer functions, which enable a fast optimization with respect to the iterative decoding threshold. The approach is validated via codeword error rate Monte Carlo simulations and complemented by an error floor analysis, showing gains up to 0.8 dB at a codeword error rate of 10-4 with respect to existing designs, down to information block lengths as short as 192 bits.

## Non-binary LDPC coded DPSK modulation for phase noise channels

- **Status**: ❌
- **Reason**: 비이진 LDPC/LDGM coded DPSK; 비이진 제외
- **ID**: ieee:7996748
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Tudor Ninacs, Balázs Matuz, Gianluigi Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/7996748
- **Abstract**: In this paper, we study digital transmission over an additive white Gaussian noise (AWGN) channel with mary differential phase-shift keying (DPSK) modulation in the presence of phase noise. At the receiver side, non-coherent iterative detection and decoding is assumed. We present a non-binary low-density generator matrix (LDGM) code design which is suitable for both coherent and non-coherent channels. The code construction is strongly related to the one of non-binary irregular repeat-accumulate (IRA) low-density parity-check (LDPC) codes.

## Noncoherent analog network coding using LDPC-coded FSK

- **Status**: ❌
- **Reason**: ANC용 noncoherent FSK 복조기, DVB-S2 LDPC는 베이스라인 — LDPC 자체 신규 기법 없음, 무선 응용 특이적
- **ID**: ieee:7997179
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Terry Ferrett, Matthew C. Valenti
- **PDF**: https://ieeexplore.ieee.org/document/7997179
- **Abstract**: Analog network coding (ANC) is a throughput increasing technique for the two-way relay channel (TWRC) whereby two end nodes transmit simultaneously to a relay at the same time and band, followed by the relay broadcasting the received sum of signals to the end nodes. Coherent reception under ANC is challenging due to requiring oscillator synchronization for all nodes, a problem further exacerbated by Doppler shift. This work develops a noncoherent M-ary frequency-shift keyed (FSK) demodulator implementing ANC. The demodulator produces soft outputs suitable for use with capacity-approaching channel codes and supports information feedback from the channel decoder. A unique aspect of the formulation is the presence of an infinite summation in the received symbol probability density function. Detection and channel decoding succeed when the truncated summation contains a sufficient number of terms. Bit error rate performance is investigated by Monte Carlo simulation, considering modulation orders two, four and eight, channel coded and uncoded operation, and with and without information feedback from decoder to demodulator. The channel code considered for simulation is the LDPC code defined by the DVB-S2 standard. To our knowledge this work is the first to develop a noncoherent soft-output demodulator for ANC.

## Low-complexity concatenated polar codes with excellent scaling behavior

- **Status**: ❌
- **Reason**: 연접 polar+SPC 코드로 비-LDPC 부호, 이식 가능한 바이너리 LDPC BP 기법 없음
- **ID**: ieee:7962781
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Sung Whan Yoon, Jaekyun Moon
- **PDF**: https://ieeexplore.ieee.org/document/7962781
- **Abstract**: In this paper, highly efficient practical concatenated coding schemes with multiple short length polar codes and single-parity-check codes are proposed. As for hardware complexity, required memory space is significantly reduced by utilizing small decoding units geared to serialized decoding of short-length component polar codes. In theoretic analysis, each component short polar code shows much improved error-rate scaling-behavior thanks to simple single-parity-check decoding; the error rate decays with increasing overall code length as fast as in single stand alone code while retaining considerable hardware-memory advantage. Moreover, by applying list decoding and cyclic-redundancy-checking to each short component polar code, finite-length error-rate performance is comparable to list decoding of CRC-aided long polar codes while offering much lower memory-complexity implementation options.

## Bit-interleaved polar-coded OFDM for low-latency M2M wireless communications

- **Status**: ❌
- **Reason**: polar-coded OFDM 무선 M2M; 비-LDPC, 무선 응용 특이적
- **ID**: ieee:7996931
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Toshiaki Koike-Akino, Ye Wang, Stark C. Draper +2
- **PDF**: https://ieeexplore.ieee.org/document/7996931
- **Abstract**: Machine-to-machine (M2M) communications play an important role for applications that involve connections between a massive number of heterogeneous devices in home and industrial networks. For M2M networks, realizing low latency and high reliability is of great importance. In this paper, we show the great potential of polar-coded orthogonal frequency-division multiplexing (OFDM) to fulfill those requirements. We show that polar codes with list decoding plus cyclic redundancy check (CRC) can outperform state-of-the-art low-density parity-check (LDPC) codes at short block lengths. In addition, we introduce an efficient interleaver and constellation shaping for polar-coded high-order modulations, where a coded sequence is carefully mapped across subcarriers and modulation bits to exploit non-uniform reliability for higher diversity gains. Through computer simulations, we demonstrate that a significant gain greater than 2 dB can be achieved by quadratic polynomial permutation (QPP) interleaver with optimized parameters in comparison to the conventional random interleaver for high-order 256-ary quadrature-amplitude modulation (QAM) OFDM transmission in frequency-selective wireless channels.

## Hard switching in hybrid FSO/RF link: Investigating data rate and link availability

- **Status**: ❌
- **Reason**: 하이브리드 FSO/RF 링크 데이터율/가용성 분석으로 LDPC와 무관
- **ID**: ieee:7962701
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Mojtaba Mansour Abadi, Zabih Ghassemlooy, Stanislav Zvanovec +2
- **PDF**: https://ieeexplore.ieee.org/document/7962701
- **Abstract**: This paper investigates the performance dependence of a hybrid free space optical (FSO)/radio frequency (RF) communication system on the data rate, link distance and link availability. In existing hybrid FSO/RF systems with hard switching, an algorithm is used to switch between FSO and RF and vice versa based on the feedback of the channel state information. In particular, two methods based on time hysteresis (TH) and power hysteresis (PH) are widely used in hard switching protocols. Although switching parameters including the time and power thresholds have been studied, the effect of link parameters has not been investigated in the literature. In this paper, we analyse the performance of a hybrid FSO/RF system under realistic channel conditions for both TH and PH switching schemes. By means of analysis and simulation, we show that increasing the data rate of individual FSO or RF link does not necessarily result in higher data rate and improved link availability in a hybrid FSO/RF system.

## A biological circuit design for modulated parity-check encoding in molecular communication

- **Status**: ❌
- **Reason**: 분자통신용 생물회로 패리티검사 인코더/변조기 설계 — NAND LDPC에 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7997032
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Alessio Marcone, Massimiliano Pierobon, Maurizio Magarini
- **PDF**: https://ieeexplore.ieee.org/document/7997032
- **Abstract**: Regarded as one of the future enabling technologies of the Internet of Things at the biological and nanoscale domains, Molecular Communication (MC) promises to enable applications in healthcare, environmental protection, and bioremediation, amongst others. Since MC is directly inspired by communication processes in biological cells, the engineering of biological circuits through cells' genetic code manipulation, which enables access to the cells' information processing abilities, is a candidate technology for the future realization of MC components. In this paper, inspired by previous research on channel coding schemes for MC and biological circuits for cell communications, a joint encoder and modulator design is proposed for the transmission of cellular information through signaling molecules. In particular, the information encoding and modulation are based on a binary parity check scheme, and they are implemented by interconnecting biological circuit components based on gene expression and mass action reactions. Each component is mathematically modeled and tuned according to the desired output. The implementation of the biological circuit in a simulation environment is then presented along with the corresponding numerical results, which validate the proposed design by showing agreement with an ideal encoding and modulator scheme.

## Unequal error protection for video streaming using delay-aware fountain codes

- **Status**: ❌
- **Reason**: 비디오용 fountain/UEP; erasure fountain 부호로 LDPC ECC 기법 없음
- **ID**: ieee:7996740
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Kairan Sun, Dapeng Wu
- **PDF**: https://ieeexplore.ieee.org/document/7996740
- **Abstract**: Recently, the forward error correction (FEC) codes are gaining popularity in video transmission community because of its capability of recovering lost packets in lossy wireless networks. The state-of-the-art scheme for FEC video transmission are the delay-aware fountain codes (DAF), which combine the ratelessness of fountain codes with the property of video coding. However, DAF assumes that all the data in the video has the same importance, thus every packet should have the equal chance to be decoded. In this work, in order to further adapt DAF to real-world video coding, we propose a method to integrate the unequal error protection (UEP) into DAF to provide additional protection for important bits. Different from the existing schemes, the proposed scheme does not impose any restriction on the importance profile, and it does not rely on any specific video coding standard. Most importantly, the proposed scheme is designed within the framework of DAF, so it neither requires any change on the DAF decoder or the protocol, nor any additional coordination between encoder and decoder. Simulation experiments show the proposed system achieves higher decoding ratios and PSNR compared to equal error protection (EEP) under the same network conditions.

## Finite length performance of random MAC strategies

- **Status**: ❌
- **Reason**: IRSA(슬롯ALOHA) BP-on-erasure 유한길이 분석 — MAC 프로토콜 분석이지 NAND ECC 디코더/코드설계 기여 아님
- **ID**: ieee:7997448
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Konstantinos Dovelos, Laura Toni, Pascal Frossard
- **PDF**: https://ieeexplore.ieee.org/document/7997448
- **Abstract**: The Internet of Things (IoT) is fueling innovation in nearly every part of our lives. From smart homes, cars, and cities, the Internet of Things is creating a more convenient, secure, intelligent, and personalized experience. While for any final user this IoT vision is a substantial innovation step, for communication providers is a compelling thread with massive number of devices connected to the Internet. Multiple connected devices sharing common wireless resources might create interference if they access the channel simultaneously. Medium access control protocols generally regulate the access of the devices to the shared channel to limit signal interference. In particular, irregular repetition slotted ALOHA (IRSA) techniques can achieve high-throughput performance when interference cancellation methods are adopted to recover from collisions. In this work, we study the finite length performance of IRSA schemes by building on the analogy between successive interference cancellation and iterative belief-propagation on erasure channels. We use a novel combinatorial derivation based on the matrix-occupancy theory to compute the error probability and we validate our method with simulation results.

## A union bound analysis for codes over binary asymmetric channels

- **Status**: ❌
- **Reason**: 이진 비대칭 채널 union bound 순수 이론; 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7996745
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Guanghui Song, Kui Cai, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/7996745
- **Abstract**: A union bound analysis is given for codes over binary asymmetric channels. By considering a random mapping that modulates each coded bit equiprobably to the signal constellation point, an average union bound is derived explicitly as a function of the code's weight spectrum. The bound can be used for estimating the error floor performance of maximum-likelihood decoding or near optimal decodings.

## A structured irregular repetition slotted ALOHA scheme with low error floors

- **Status**: ❌
- **Reason**: IRSA 랜덤액세스 프로토콜을 BEC-LDPC로 캐스팅한 설계; NAND 채널 ECC로 뗄 코드설계 기법 없음(JSCC/프로토콜 유사성)
- **ID**: ieee:7996564
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Enrico Paolini, Gianluigi Liva, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/7996564
- **Abstract**: We propose graph-defined IRSA (G-IRSA), a new approach to design irregular repetition slotted ALOHA (IRSA) uncoordinated multiple access schemes for a controlled-size population of users that become active sporadically. The proposed scheme considers a joint design of the distribution according to which users select their repetition factors and the distribution determining how many packet replicas are transmitted per slot, as well as the connectivity of the underlying graph, i.e., to which slots users transmit. This is in sharp contrast to standard IRSA, where only the users degree distribution is optimized, while active users place their packet replicas uniformly at random and thus there is no control on how many replicas are transmitted per slot and in which slots users transmit. The key idea is to establish a link between the IRSA for the considered scenario and low-density parity-check (LDPC) codes for transmission over the binary erasure channel (BEC). Using this parallelism, the design of a G-IRSA scheme can be cast as the design of a high-rate LDPC code over the BEC. We show that the proposed scheme achieves significantly lower error floors than the original IRSA and very good decoding thresholds.

## Adaptive polar coding with high order modulation for block fading channels

- **Status**: ❌
- **Reason**: 블록 페이딩용 적응 polar 코딩으로 비-LDPC 부호이며 이식 BP 기법 없음
- **ID**: ieee:7962749
- **Type**: conference
- **Published**: 21-25 May 
- **Authors**: Shuiyin Liu, Yi Hong, Emanuele Viterbo
- **PDF**: https://ieeexplore.ieee.org/document/7962749
- **Abstract**: We consider the design of polar codes for block fading channels. The key idea is to combine modulation, fading, and coding in a single entity. This design is based on two facts: (i) for each fading block, symbols with different fading coefficient has different reliability; (ii) for each symbol, different bit levels of a high order modulation observe different noise levels. In other words, the bit channels are partially polarized by modulation and fading. This new viewpoint inspires us to construct polar codes by matching code polarization perfectly with modulation polarization and fading polarization. The resulting codes adapt to the channel quality fluctuation, thus provide better performance than conventional polar BICM schemes and LDPC codes.

## Comparitive analysis of channel coding using BPSK modulation

- **Status**: ❌
- **Reason**: 여러 채널코드(Hamming/RS/Turbo/LDPC/Polar) BER 단순 비교, 신규 기여 없음
- **ID**: ieee:8256819
- **Type**: conference
- **Published**: 19-20 May 
- **Authors**: M N Meghana, B. Roja Reddy, B. Krishnam Prasad
- **PDF**: https://ieeexplore.ieee.org/document/8256819
- **Abstract**: Minimum Bit Error Rate is the aspiration of any communication system, so the performance of the system is improved. To achieve this, the best way is the use of channel codes in communication system. In this paper the Hamming Code, Convolution code, RS code, Turbo codes, LDPC codes and Polar codes with BPSK modulations are implemented in Matlab. The performance is compared for these channel codes in terms of BER.

## Optimization of ldpc codes used in cooperative relay systems: Case of mobile telephony

- **Status**: ❌
- **Reason**: 협력 릴레이/이동통신 응용 특이적 soft parity 생성; NAND LDPC에 떼어낼 디코더·HW·코드설계 기법 없음
- **ID**: ieee:8071974
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Idy Diop, Idrissa P. Ndiaye, Papa Alioune Fall +1
- **PDF**: https://ieeexplore.ieee.org/document/8071974
- **Abstract**: This paper analyzes the Soft Information Relaying (SIR) for LDPC (Low Density Parity Check) codes in cellular networks. We propose a new way to generate soft parity bits at the relay. This generation of soft parity bits will be done in two steps and will be made to the Cholesky decomposition for one of the submatrices of the global matrix implemented at the destination. In addition to this generation of two-step, we offer an efficient way/manner to compute the logarithms of the Likelihood Ratio (LLR) to the destination. Simulation results show that this technique has advantages over some previous work.

## On the design of LDPC-based Raptor codes for single carrier Internet of Things (SC-IoT)

- **Status**: ❌
- **Reason**: LDPC-precode Raptor/fountain codes for IoT; rateless/erasure, LDPC baseline, no extractable channel-ECC technique
- **ID**: ieee:7967024
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Nur Kamila, Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/7967024
- **Abstract**: In this paper, we propose new Raptor codes suitable for uplink Internet of Things using single carrier transmission technique (SC-IoT) with low density parity check (LDPC) codes as the precode, called LDPC-Raptor codes. The utilization of LDPC as the precode is to guarantee high capability of error correction for better Raptor codes performance while keeping the computational complexity low. Raptor Codes are preferable for SC-IoT because of their flexibility with both fixed/non-fixed rate (rateless) and simplicity in decoding. The LDPC-Raptor codes is designed (sub)-optimally using Extrinsic Information Transfer (EXIT) chart to meet requirements of SC-IoT. We evaluate the performance of the proposed LDPC-Raptor codes to achieve the Shannon capacity over Binary Erasure Channels (BEC)-based equivalent additive white Gaussian noise (AWGN) and frequency-flat Rayleigh fading and show that LDPC-Raptor codes provide significant contributions than Luby Transform (LT) codes for SC-IoT.

## Header detection for massive IoT wireless networks over Rayleigh fading channels

- **Status**: ❌
- **Reason**: Header detection via Hadamard codes; not LDPC ECC
- **ID**: ieee:7967038
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Juansyah, Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/7967038
- **Abstract**: In this paper, we propose header detection technique for massive internet of things (IoT) networks over Rayleigh fading channels. We consider coded random access (CRA) as a multiple access scheme for IoT to keep low computational complexity of detection, where header detection is of significant important. We perform header detection by computing cross correlation using Hadamard codes. Hadamard codes are chosen because of its simplicity to be generated, where the value of the matrix component is only ±1. To avoid data rate loss due to bits allocation to header, the length of the header should be kept small. We use Hadamard codes with size of 128×128 as a header for packets suffering from Rayleigh fading channels. We also use capture effect algorithm to improve detection performances when multiple IoT devices are transmitting at the same time-slot. Although the algorithms is simple, we found that header detection using Hadamard codes for massive IoT connections over Rayleigh fading channels is still providing high accuracy, which is suitable for future massive IoT wireless networks.

## Mojette transform based LDPC erasure correction codes for distributed storage systems

- **Status**: ❌
- **Reason**: Mojette transform 기반 erasure LDPC; 비표준 구성이나 분산스토리지 repair 특이적, NAND 바이너리 채널 LDPC에 이식할 디코더/HW 기법 없음 (애매하나 erasure/repair 도메인 한정)
- **ID**: ieee:7960333
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Şuayb Ş. Arslan, Benoît Parrein, Nicolas Normand
- **PDF**: https://ieeexplore.ieee.org/document/7960333
- **Abstract**: Mojette Transform (MT) based erasure correction coding possesses extremely efficient encoding/decoding algorithms and demonstrate promising burst erasure recovery performance. MT codes are based on discrete geometry and provide redundancy through creating projections. Projections are made of smaller data structures called bins and are generated from a two dimensional convex-shaped data. For exact data recovery, only a subset of projections are needed by the decoder. We realize that the discrete geometry definition of MT erasure codes corresponds to creating structured/deterministic generator matrices. In this study, we show an alternative Low Density Parity Check (LDPC) code construction methodology through investigating parity check matrices of MT codes which shows sparseness as the blocklength of the code gets large. In a distributed storage setting, we also quantify the repair bandwidth and show that this novel interpretation can be used to facilitate bin-level local repairs.

## Error Performance of LDPC Coded Spatial Modulation Technique

- **Status**: ❌
- **Reason**: LDPC+공간변조 무선 응용; LDPC는 부수 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:7960403
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ferhat Bayar, Hacı İlhan
- **PDF**: https://ieeexplore.ieee.org/document/7960403
- **Abstract**: In this paper, spatial modulation (SM) technique and low density parity check code (LDPC) are combined. SM technique seems to provide transmissions speed and spectral efficiency at same levels under the low system complexity and cost compared to traditional multiple input multiple output (MIMO) transmission systems. However, SM may give high bit error rate (BER) values at low signal to noise ratios (SNR). Therefore, need of excessive power consumption is emerging for compensate of this. In this context, spatial modulation system with LDPC coding is proposed to improve error performance and superiority of system is presented by performed computer simulation.

## R2D: Combining replication and redundancy to enhance the performance and reliability of storage systems

- **Status**: ❌
- **Reason**: 스토리지 복제+이중화 시스템 설계로 read amplification 완화, LDPC ECC 기법 아님
- **ID**: ieee:7988175
- **Type**: conference
- **Published**: 13-17 May 
- **Authors**: Min-Chun Chen, Yun-Shan Hsieh, Hsin-Hsin Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/7988175
- **Abstract**: Due to the continuous upscaling of the storage capacity and downscaling of the physical size of storage systems, the data reliability problem has become a research highlight. While various redundancy schemes have been proposed to include extra redundant data to ensure that the correct data can be recovered even in the presence of bit errors or bad blocks, they might introduce unexpected performance overheads on data accesses. In particular, in the case of unreliable block devices, as a number of data blocks are grouped together for redundant data computation, even reading a single bad block might require to read out the whole set, including the data blocks and their redundant blocks, to recover the correct data, thereby considerably amplifying the read traffic. On the other hand, the replication scheme does not have such a serious overhead of read amplification, but introduces a serious space overhead to keep multiple copies of the same data. In this work, we propose to integrate redundancy and replication schemes according to the access patterns of different data, which can strike a proper balance between the space and performance overheads. The proposed scheme, “redundant or replicated data (R2D),” is then verified through experimental studies, where the results are quite encouraging.

## A parity check analog decoder for molecular communication based on biological circuits

- **Status**: ❌
- **Reason**: 분자통신 생물학 회로 기반 아날로그 패리티체크 디코더, 바이오 도메인 특이적이라 NAND HW 이식 불가.
- **ID**: ieee:8057131
- **Type**: conference
- **Published**: 1-4 May 20
- **Authors**: Alessio Marcone, Massimiliano Pierobon, Maurizio Magarini
- **PDF**: https://ieeexplore.ieee.org/document/8057131
- **Abstract**: Molecular Communication (MC) is an enabling paradigm for the interconnection of future devices and networks in the biological environment, with applications ranging from bio-medicine to environmental monitoring and control. The engineering of biological circuits, which allows to manipulate the molecular information processing abilities of biological cells, is a candidate technology for the realization of MC-enabled devices. In this paper, inspired by recent studies favoring the efficiency of analog computation over digital in biological cells, an analog decoder design is proposed based on biological circuit components. In particular, this decoder computes the a-posteriori log-likelihood ratio of parity-check-encoded bits from a binary-modulated concentration of molecules. The proposed design implements the required L-value and the box-plus operations entirely in the biochemical domain by using activation and repression of gene expression, and reactions of molecular species. Each component of the circuit is designed and tuned in this paper by comparing the resulting functionality with that of the corresponding analytical expression. Despite evident differences with classical electronics, biochemical simulation data of the resulting biological circuit demonstrate very close performance in terms of Mean Squared Error (MSE) and Bit Error Rate (BER), and validate the proposed approach for the future realization of MC components.
