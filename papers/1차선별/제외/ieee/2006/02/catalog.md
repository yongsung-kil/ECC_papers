# IEEE Xplore — 2006-02


## Design and analysis of nonbinary LDPC codes for arbitrary discrete-memoryless channels

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC 설계·분석 — 비이진 제외
- **ID**: ieee:1580795
- **Type**: journal
- **Published**: Feb. 2006
- **Authors**: A. Bennatan, D. Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/1580795
- **Abstract**: We present an analysis under the iterative decoding of coset low-density parity-check (LDPC) codes over GF(q), designed for use over arbitrary discrete-memoryless channels (particularly nonbinary and asymmetric channels). We use a random- coset analysis to produce an effect that is similar to output symmetry with binary channels. We show that the random selection of the nonzero elements of the GF(q) parity-check matrix induces a permutation-invariance property on the densities of the decoder messages, which simplifies their analysis and approximation. We generalize several properties, including symmetry and stability from the analysis of binary LDPC codes. We show that under a Gaussian approximation, the entire q-1-dimensional distribution of the vector messages is described by a single scalar parameter (like the distributions of binary LDPC messages). We apply this property to develop extrinsic information transfer (EXIT) charts for our codes. We use appropriately designed signal constellations to obtain substantial shaping gains. Simulation results indicate that our codes outperform multilevel codes at short block lengths. We also present simulation results for the additive white Gaussian noise (AWGN) channel, including results within 0.56 dB of the unrestricted Shannon limit (i.e., not restricted to any signal constellation) at a spectral efficiency of 6 bits/s/Hz.

## Tensor-product Parity codes: combination with constrained codes and application to perpendicular recording

- **Status**: ❌
- **Reason**: Tensor-product parity + constrained codes for magnetic recording; RS 기반, LDPC 아님. 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:1580677
- **Type**: journal
- **Published**: Feb. 2006
- **Authors**: P. Chaichanavong, P.H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/1580677
- **Abstract**: A parity code and a distance enhancing constrained code are often concatenated with a Reed-Solomon code to form a coding system for magnetic recording. The tensor-product parity coding scheme helps to improve efficiency of the parity code while retaining the same level of performance. In this paper, we present two methods for combining a tensor-product parity code with a distance-enhancing constrained code. The first method incorporates a constrained code with unconstrained positions. The second method uses a new technique, which we call word-set partitioning, to achieve a higher code rate relative to the first method. We simulate the performance of several coding systems based upon the two combination methods on a perpendicular recording channel, and we compare their symbol error rates and sector error rates with those of a system that uses only a Reed-Solomon code.

## Low-density parity-check codes for space-time wireless transmission

- **Status**: ❌
- **Reason**: 공간시간 무선전송, 주로 2^p-ary(비이진) LDPC 설계; 바이너리 부분은 표준 구성 재사용, 신규 이식 기법 없음
- **ID**: ieee:1611055
- **Type**: journal
- **Published**: Feb. 2006
- **Authors**: G. Li, I.J. Fair, W.A. Krzymien
- **PDF**: https://ieeexplore.ieee.org/document/1611055
- **Abstract**: Irregular low-density parity-check (LDPC) codes have shown exceptionally good performance for single antenna systems over a wide class of channels. In this paper, we investigate their application to multiple antenna systems in flat Rayleigh fading channels. For small transmit arrays, we focus mainly on space-time coding with 2/sup p/-ary LDPC codes, where p equals the number of encoded bits transmitted by the transmit antenna array during each signaling interval. For large transmit arrays, we study a layered space-time architecture using binary LDPC codes as component codes of each layer: We show through simulation that, when applied to multiple antenna systems with high diversity order, LDPC codes of quasi-regular construction are able to achieve higher coding gain and/or diversity gain than previously proposed space-time trellis codes, space-time turbo codes, and convolutional codes in a number of fading conditions. Extending the work of density evolution with Gaussian approximation, we study 2/sup p/-ary LDPC codes on multiple antenna fading channels, and search for the optimum 2/sup p/-ary quasi-regular codes in quasi-static fading. We also show that on fast fading channels, 2/sup p/-ary irregular LDPC codes, though designed for static channels, have superior performance to nonbinary quasiregular codes and binary irregular codes specifically designed for fast fading channels.

## Scalable decoding on factor trees: a practical solution for wireless sensor networks

- **Status**: ❌
- **Reason**: 센서망 상관데이터 MMSE 결합디코딩, factor tree sum-product — 채널 ECC 아닌 소스추정, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:1599601
- **Type**: journal
- **Published**: Feb. 2006
- **Authors**: J. Barros, M. Tuchler
- **PDF**: https://ieeexplore.ieee.org/document/1599601
- **Abstract**: We consider the problem of jointly decoding the correlated data picked up and transmitted by the nodes of a large-scale sensor network. Assuming that each sensor node uses a very simple encoder (a scalar quantizer and a modulator), we focus on decoding algorithms that exploit the correlation structure of the sensor data to produce the best possible estimates under the minimum mean-square error (MMSE) criterion. Our analysis shows that a standard implementation of the optimal MMSE decoder is unfeasible for large-scale sensor networks, because its complexity grows exponentially with the number of nodes in the network. Seeking a scalable alternative, we use factor graphs to obtain a simplified model for the correlation structure of the sensor data. This model allows us to use the sum-product decoding algorithm, whose complexity can be made to grow linearly with the size of the network. Considering large sensor networks with arbitrary topologies, we focus on factor trees and give an exact characterization of the decoding complexity, as well as mathematical tools for factorizing Gaussian sources and optimization algorithms for finding optimal factor trees under the Kullback-Leibler criterion.

## Codes for Half Duplex Relay Channels

- **Status**: ❌
- **Reason**: half-duplex relay 채널용 LDPC degree profile 최적화. 무선 응용 특이적, 표준 EXIT/가우시안근사 수준이라 NAND 이식 기법 없음
- **ID**: ieee:1649104
- **Type**: conference
- **Published**: 22-24 Feb.
- **Authors**: A. Chakrabarti, A. de Baynast, A. Sabharwal +1
- **PDF**: https://ieeexplore.ieee.org/document/1649104
- **Abstract**: In this paper, we study LDPC code constructions for the half-duplex relay channels. Our work is motivated by the observation that half-duplex relaying where the relay cannot simultaneously transmit and receive in the same band yields substantially higher rate than both direct and two-hop communication with the same average power constraint. The profile optimization technique and the resulting LDPC codes prove to be very effective in fading environments. The performance thresholds determined using Gaussian approximation are extremely close to theoretical limits

## Iteration based performance evaluation of LDPC coded MIMO-OFDM

- **Status**: ❌
- **Reason**: LDPC-coded MIMO-OFDM 반복횟수 배분 성능평가, 표준 LDPC 사용·새 디코더/구성 없음
- **ID**: ieee:1626018
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Hyoung Soon Kim, Sin Chong Park
- **PDF**: https://ieeexplore.ieee.org/document/1626018
- **Abstract**: In this paper, PER performance of LDPC-coded MIMO-OFDM system is evaluated in the context of iterative demodulation and decoding. Total number of iterations is fixed to 10 and we consider 21 combinations between iteration number of LDPC decoder (LDPC iterations) and iterations number of demodulation and decoding (super iterations). As a result, more than 5dB SNR performance variation at PER 10/sup -1/ is observed by different configurations. When two super iterations and 3, 7 LDPC iterations for each super iteration are performed, we obtain 1.2dB gain in SNR at PER 10/sup -1/ compared to only 10 LDPC iterations performed.

## Trade-off between performance and complexity with various candidates in LDPC coded MIMO-OFDM iterative decoding

- **Status**: ❌
- **Reason**: LDPC-coded MIMO-OFDM에서 LSD 후보 수 trade-off; MIMO 검출기 복잡도 분석으로 NAND LDPC ECC에 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:1625812
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Seongmin Noh, Sin-Chong Park
- **PDF**: https://ieeexplore.ieee.org/document/1625812
- **Abstract**: In the context of MAP estimate performance and comparable complexity, LDPC-coded MIMO-OFDM systems are investigated widely. Specifically, in case of iterative detection using LSD (list sphere decoding), there is trade-off between detection performance and complexity according to the number of candidates N/sub can/. As a system model with 802.11n wireless LAN, simulation results show that performance saturation with candidates over 64, but long latency with more than 16 candidates. Hence, proper N/sub can/ can be chosen between 8 and 16 considering performance degradation and hardware issues.

## Novel techniques of a list sphere decoder for high throughput

- **Status**: ❌
- **Reason**: MIMO sphere/list sphere decoder 복잡도 감소, LDPC 비의존 검출기법으로 떼어낼 BP 기여 없음
- **ID**: ieee:1625940
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Jin Lee, Sin-Chong Park
- **PDF**: https://ieeexplore.ieee.org/document/1625940
- **Abstract**: Since finding the nearest point in a lattice for multi-input multi-output (MIMO) channels is NP-hard, simplified algorithms such as a sphere decoder (SD) have been proposed. List sphere decoder (LSD), which is a modified version of SD, allows soft information to be extracted for channel decoding and iterative detection/decoding. In this paper, recently proposed efficient methods for reducing the computational complexity of a sphere decoder (SD) and a list sphere decoder (LSD) with depth-first tree searching are summarized. Numerous simulations have been carried out and comparison has been made based on of the average number of processing cycles.

## Analysis of energy efficiency for low power transmission in WLAN with MIMO-OFDM and block ack mechanism

- **Status**: ❌
- **Reason**: WLAN MIMO-OFDM 에너지효율 분석, LDPC/ECC 기법 없음
- **ID**: ieee:1625864
- **Type**: conference
- **Published**: 20-22 Feb.
- **Authors**: Hoseok Choi, Sinchong Park
- **PDF**: https://ieeexplore.ieee.org/document/1625864
- **Abstract**: Energy efficiency on wireless communication is an important issue of the battery power based wireless communication devices. This paper presents the energy efficiency model for MIMO OFDM WLAN system with the block ack mechanism and also presents the analysis of the system. Several parameters are considered such as number of antennas, modulation, path loss, payload size and number of burst transmission in block ack mechanism. Our experiment results show that energy efficiency is higher at the lower number of antennas, higher modulation, larger data payload size and burst transmission environment.

## Erasure Codes for Increasing the Availability of Grid Data Storage

- **Status**: ❌
- **Reason**: Grid storage with Reed-Solomon codes; non-LDPC erasure coding, no portable LDPC technique
- **ID**: ieee:1602318
- **Type**: conference
- **Published**: 19-25 Feb.
- **Authors**: M. Pitkanen, R. Moussa, M. Swany +1
- **PDF**: https://ieeexplore.ieee.org/document/1602318
- **Abstract**: In this paper, we describe the design of a highlyavailable Grid data storage system. Increased availability is ensured by data redundancy and file striping. Redundant data is computed using Reed-Solomon (RS) codes. The level of availability can be chosen for each individual file. Storage overhead is minimal compared to traditional redundancy strategies based on complete replication. Our prototype uses existing Grid data management tools (GridFTP) for communication, and the RS encoding and decoding is embedded in the client software. Performance measurements in wide area network prove the efficiency of our design for high-availability and striped file transfers.

## Coding in the Block-Erasure Channel

- **Status**: ❌
- **Reason**: block-erasure 채널 MDS 부호 outage 이론 분석; 순수 이론, 디코더/HW/LDPC 구성으로 안 이어짐
- **ID**: ieee:1625249
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: A. Guillen i Fabregas, Qi Tang
- **PDF**: https://ieeexplore.ieee.org/document/1625249
- **Abstract**: We study an M-ary block-erasure channel with B blocks, where with probability ε a block of L coded symbols is erased. We study the behavior of the error probability of coded systems over such channels, and show that, if the code is diversitywise maximum-distance separable, its word error probability is equal to the outage probability, which admits a very simple expression. This paper is intended to complement the error probability analysis in previous work by Lapidoth and shed some light on the design of coding schemes for nonergodic channels.

## Weighted extrinsic feedback in the iterative multiuser decoding of coded CDMA

- **Status**: ❌
- **Reason**: CDMA 반복 다중사용자 디코딩의 weighted extrinsic feedback; LDPC 부호 비의존 다중사용자검출 응용, 떼어낼 LDPC BP 기법 불명확
- **ID**: ieee:1625256
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: R. Milner, L.K. Rasmussesn
- **PDF**: https://ieeexplore.ieee.org/document/1625256
- **Abstract**: In iterative decoding it is well accepted that extrinsic information is to be exchanged between full-complexity soft-input, soft-output constituent decoder components. It is, however, still an open problem to determine the optimal information for exchange between reduced complexity decoder components that are only approximating posterior probabilities. In this paper we investigate the use of weighted extrinsic feedback in iterative multiuser decoding for coded code-division multiple-access (CDMA) systems. The case of no extrinsic feedback corresponds to the conventional approach of exchanging extrinsic information, while full extrinsic feedback corresponds to exchanging a posteriori information. Weighted extrinsic feedback offers a trade-off between the two extreme cases, which can provide significant improvements. These improvements are demonstrated through simulation of an iterative multiuser decoder using parallel interference cancellation as the soft-input, soft-output multiuser detector.

## Fixed Points of Exit Charts

- **Status**: ❌
- **Reason**: EXIT 차트를 동역학계로 추상화한 순수 수렴해석 이론 — 떼어낼 디코더/HW/코드설계 기법 없음, 순수 이론 bound에 해당
- **ID**: ieee:1625270
- **Type**: conference
- **Published**: 1-3 Feb. 2
- **Authors**: C.M. Kellett, S.R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/1625270
- **Abstract**: Extrinsic Information Transfer (or EXIT) charts have provided a useful tool for analysing the convergence of iterative decoders. In this work, we abstract the EXIT chart as a feedback interconnection of two one-dimensional dynamical systems. For such feedback interconnections, we characterise the local stability properties of fixed points and demonstrate the existence of period two orbits and discuss their stability properties. Finally, we give a graphical procedure for finding the region of attraction for asymptotically stable fixed points or period two orbits.
