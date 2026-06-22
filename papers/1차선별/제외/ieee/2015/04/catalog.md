# IEEE Xplore — 2015-04


## A Matrix-Theoretic Approach to the Construction of Non-Binary Quasi-Cyclic LDPC Codes

- **Status**: ❌
- **Reason**: non-binary QC-LDPC 구성 - 비이진 LDPC는 제외 대상
- **ID**: ieee:7042290
- **Type**: journal
- **Published**: April 2015
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/7042290
- **Abstract**: This paper presents two simple and very flexible methods for constructing non-binary (NB) quasi-cyclic (QC) LDPC codes. The proposed construction methods have several known ingredients including base array, masking, binary to nonbinary replacement, and matrix-dispersion. By proper choice and combination of these ingredients, NB-QC-LDPC codes with excellent performance can be constructed. The constructed codes can be decoded with a reduced-complexity iterative decoding scheme which significantly reduces the hardware implementation complexity.

## Linear Precoding for MIMO With LDPC Coding and Reduced Complexity

- **Status**: ❌
- **Reason**: MIMO용 선형 프리코더(PGP) 설계, LDPC는 베이스라인 부호일 뿐 EXIT chart 디코딩 복잡도만 언급, 떼어낼 새 디코더 기법 없음
- **ID**: ieee:6998869
- **Type**: journal
- **Published**: April 2015
- **Authors**: Thomas Ketseoglou, Ender Ayanoglu
- **PDF**: https://ieeexplore.ieee.org/document/6998869
- **Abstract**: In this paper, the problem of designing a linear precoder for Multiple-Input Multiple-Output (MIMO) systems employing Low-Density Parity-Check (LDPC) codes is addressed under the constraint of minimizing the dependence between the system's receiving branches, thus reducing the relevant transmitter and receiver complexities. Our approach constitutes an interesting generalization of Bit-Interleaved Coded Modulation with Multiple Beamforming (BICMB) which has shown many benefits in MIMO systems. We start with a Pareto optimal surface modeling of the system and show the difficulty involved in the corresponding optimization problem. We then propose an alternative, practical technique, called Per-Group Precoding (PGP), which groups together multiple input symbol streams and corresponding receiving branches in the “virtual” channel domain (after singular value decomposition of the original MIMO channel), and thus results in independent transmitting/receiving streams between groups. We show with numerical results that PGP offers almost optimal performance, albeit with significant reduction both in the precoder optimization and LDPC EXIT chart based decoding complexities.

## Low-Density Lattice Codes for Full-Duplex Relay Channels

- **Status**: ❌
- **Reason**: low-density lattice codes(LDLC)는 격자부호로 바이너리 LDPC가 아님, 릴레이 채널 응용
- **ID**: ieee:6994267
- **Type**: journal
- **Published**: April 2015
- **Authors**: Nuwan S. Ferdinand, Matthew Nokleby, Behnaam Aazhang
- **PDF**: https://ieeexplore.ieee.org/document/6994267
- **Abstract**: We propose a class of practical efficient lattice codes for real-valued full-duplex one- and two-way relay channels. First, we investigate the problem from a theoretical perspective, proposing lattice-coding instantiations of superposition block Markov encoding. Our encoding/decoding strategies recover the well-known decode-and-foward rates for the one-way relay channel and a previously-proven rate region for the two-way relay channel. Then, we construct practical, low-complexity implementations of these schemes using low-density lattice codes. Simulations show that our schemes achieve performance as close as 2.5 dB away from theoretical limits. Finally, we show that, due to features inherent to full-duplex relaying and practical codes, the gap to theoretical limits depends on the channel gains and transmit power of the relay relative to the source(s). We characterize this gap analytically, providing insight into the design of practical full-duplex relay systems.

## Design of Joint Sparse Graph for OFDM System

- **Status**: ❌
- **Reason**: LDS-OFDM과 LDPC 결합 sparse graph 다중사용자검출(JMUDD) — 통신 응용 결합 그래프, NAND LDPC BP에 떼어낼 디코더 기법 없음
- **ID**: ieee:6964791
- **Type**: journal
- **Published**: April 2015
- **Authors**: Lei Wen, Razieh Razavi, Muhammad Ali Imran +1
- **PDF**: https://ieeexplore.ieee.org/document/6964791
- **Abstract**: Low density signature orthogonal frequency division multiplexing (LDS-OFDM) and low density parity-check (LDPC) codes are multiple access and forward error correction (FEC) techniques, respectively. Both of them can be expressed by a bipartite graph. In this paper, we construct a joint sparse graph combining the single graphs of LDS-OFDM and LDPC codes, namely joint sparse graph for OFDM (JSG-OFDM). Based on the graph model, a low complexity approach for joint multiuser detection and FEC decoding (JMUDD) is presented. The iterative structure of JSG-OFDM receiver is illustrated and its extrinsic information transfer (EXIT) chart is researched. Furthermore, design guidelines for the joint sparse graph are derived through the EXIT chart analysis. By offline optimization of the joint sparse graph, numerical results show that the JSG-OFDM brings about 1.5-1.8 dB performance improvement at bit error rate (BER) of 10-5 over similar well-known systems such as group-orthogonal multi-carrier code division multiple access (GO-MC-CDMA), LDS-OFDM, and turbo structured LDS-OFDM.

## Steepest-Descent Optimization of CDMA Signatures for Multiple Correlated Sources With Applications to Joint Source-Channel Coding

- **Status**: ❌
- **Reason**: CDMA signature 최적화·JSCC 무선센서망 응용, LDPC ECC 아님 - 떼어낼 기법 없음
- **ID**: ieee:7050310
- **Type**: journal
- **Published**: April 2015
- **Authors**: Pradeepa Yahampath
- **PDF**: https://ieeexplore.ieee.org/document/7050310
- **Abstract**: An approach to transmitting multiple correlated sources over a Gaussian multiple-access channel (GMAC) using code-division multiple-access (CDMA) is investigated. A block coordinate descent (BCD) algorithm is presented which can be used to optimize CDMA signatures for a given source covariance matrix under individual transmitter power constraints. This algorithm can be used to design non-orthogonal CDMA signatures for GMACs with arbitrary input alphabets, fading, and colored noise. While the main focus has been the design of signatures which minimize the mean square error (MSE) of linear decoding, the algorithm can also be used to design signatures which maximize the input-output mutual information of the channel. This paper investigates the uncoded transmission of Gaussian sources and the coded transmission of binary sources over a GMAC using joint source-channel (JSC) optimized CDMA signatures under constraints on transmitter power and channel bandwidth, scenarios relevant to wireless sensor networks. By using simple coding schemes which only rely on linear multi-user detection and independent channel decoding of a large number of sources, it is demonstrated that CDMA-based JSC coding can exploit inter-source correlation to achieve lower distortion (Gaussian sources) or higher rates (binary sources) compared to conventional separate source-channel (SSC) coding over the same channel bandwidth.

## Adaptive Modulation and Coding for Underwater Acoustic OFDM

- **Status**: ❌
- **Reason**: 수중음향 OFDM 적응변조코딩 — LDPC 부수 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:6840859
- **Type**: journal
- **Published**: April 2015
- **Authors**: Lei Wan, Hao Zhou, Xiaoka Xu +4
- **PDF**: https://ieeexplore.ieee.org/document/6840859
- **Abstract**: Underwater acoustic channels are fast varying spatially and temporally according to environmental conditions. Adaptive modulation and coding (AMC) is appealing for underwater acoustic communications to improve the system efficiency by matching transmission parameters to channel variations. In this paper, we construct an AMC system with a finite number of transmission modes in the context of underwater orthogonal frequency-division multiplexing (OFDM). We propose the effective signal-to-noise ratio (SNR) computed after channel estimation and channel decoding as a new performance metric for mode switching, which is shown to predict the system performance more consistently than the input SNR and the pilot SNR. Real-time AMC tests have been conducted in a recent sea experiment to maximize the transmission rate with a given transmission power.

## FMTCP: A Fountain Code-Based Multipath Transmission Control Protocol

- **Status**: ❌
- **Reason**: Fountain 코드 기반 멀티패스 TCP 전송 — 비-LDPC, 떼어낼 ECC 기법 없음
- **ID**: ieee:6729115
- **Type**: journal
- **Published**: April 2015
- **Authors**: Yong Cui, Lian Wang, Xin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/6729115
- **Abstract**: Ideally, the throughput of a Multipath TCP (MPTCP) connection should be as high as that of multiple disjoint single-path TCP flows. In reality, the throughput of MPTCP is far lower than expected. In this paper, we conduct an extensive simulation-based study on this phenomenon, and the results indicate that a subflow experiencing high delay and loss severely affects the performance of other subflows, thus becoming the bottleneck of the MPTCP connection and significantly degrading the aggregate goodput. To tackle this problem, we propose Fountain code-based Multipath TCP (FMTCP), which effectively mitigates the negative impact of the heterogeneity of different paths. FMTCP takes advantage of the random nature of the fountain code to flexibly transmit encoded symbols from the same or different data blocks over different subflows. Moreover, we design a data allocation algorithm based on the expected packet arriving time and decoding demand to coordinate the transmissions of different subflows. Quantitative analyses are provided to show the benefit of FMTCP. We also evaluate the performance of FMTCP through ns-2 simulations and demonstrate that FMTCP outperforms IETF-MPTCP, a typical MPTCP approach, when the paths have diverse loss and delay in terms of higher total goodput, lower delay, and jitter. In addition, FMTCP achieves high stability under abrupt changes of path quality.

## Differentially Coherent Multichannel Detection of Acoustic OFDM Signals

- **Status**: ❌
- **Reason**: 수중음향 OFDM 도플러 보상/FFT 복조 검출 기법으로 LDPC ECC와 무관, 떼어낼 디코더/HW 없음
- **ID**: ieee:6840861
- **Type**: journal
- **Published**: April 2015
- **Authors**: Yashar M. Aval, Milica Stojanovic
- **PDF**: https://ieeexplore.ieee.org/document/6840861
- **Abstract**: In this paper, we propose a class of methods for compensating for the Doppler distortions of the underwater acoustic channel for differentially coherent detection of orthogonal frequency-division multiplexing (OFDM) signals. These methods are based on multiple fast Fourier transform (FFT) demodulation, and are implemented as partial (P), shaped (S), fractional (F), and Taylor (T) series expansion FFT demodulation. They replace the conventional FFT demodulation with a few FFTs and a combiner. The input to each FFT is a specific transformation of the input signal, and the combiner performs weighted summation of the FFT outputs. The four methods differ in the choice of the pre-FFT transformation (P, S, F, T), while the rest of the receiver remains identical across these methods. We design an adaptive algorithm of stochastic gradient type to learn the combiner weights for differentially coherent detection. The algorithm is cast into the multichannel framework to take advantage of spatial diversity. The receiver is also equipped with an improved synchronization technique for estimating the dominant Doppler shift and resampling the signal before demodulation. An additional technique of carrier sliding is introduced to aid in the post-FFT combining process when residual Doppler shift is nonnegligible. Synthetic data, as well as experimental data from a recent mobile acoustic communication experiment (few kilometers in shallow water, 10.5-15.5-kHz band) are used to demonstrate the performance of the proposed methods, showing significant improvement over conventional detection techniques with or without intercarrier interference equalization (5-7 dB on average over multiple hours), as well as improved bandwidth efficiency [ability to support up to 2048 quadrature phase-shift keying (QPSK) modulated carriers].

## Multicarrier Successive Predistortion for Nonlinear Satellite Systems

- **Status**: ❌
- **Reason**: 위성 비선형 다중반송파 predistortion 기법, LDPC/ECC 무관 - 떼어낼 디코더·코드 기법 없음
- **ID**: ieee:7041235
- **Type**: journal
- **Published**: April 2015
- **Authors**: Bassel F. Beidas, Rohit Iyer Seshadri, Neal Becker
- **PDF**: https://ieeexplore.ieee.org/document/7041235
- **Abstract**: To satisfy the aggressive demand for higher satellite throughput, industry trend is moving toward sharing the transponder amplifier by multiple carriers, each employing high-order modulations that are spectrally compact. This trend, in conjunction with the inherently nonlinear nature of the amplifier when driven efficiently closer to saturation, creates significant intermodulation distortion that needs to be appropriately compensated. This paper presents a powerful compensation technique that is capable of mitigating the nonlinear intermodulation distortion and is placed at the transmitter or gateway. It is a novel multicarrier data predistortion technique that successively modifies the transmitted symbols to drive multicarrier distortion vector toward zero. This distortion vector results from passing the transmitted symbols from the multiple carriers, intrinsically accessible at the gateway, through the nonlinear satellite channel model. The novel successive predistortion technique and methods of estimating the distortion are described in detail. It is demonstrated using extensive computer simulations that the proposed multicarrier predistortion technique is capable of achieving near-optimum performance, even when only a simple linear receiver is employed and no exchange of data is assumed between receivers.

## Transmitter Design for Uplink MIMO Systems With Antenna Correlation

- **Status**: ❌
- **Reason**: 상관 MIMO 업링크 송신기/프리코더 설계, LDPC 부수 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:6963395
- **Type**: journal
- **Published**: April 2015
- **Authors**: Chongbin Xu, Peng Wang, Zhonghao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6963395
- **Abstract**: We study the uplink transmission in multiple-input multiple-output (MIMO) systems with antenna correlation. We focus on schemes that require only channel covariance information at the transmitter (CCIT), which involves lower cost than full channel state information at the transmitter (CSIT). We start from mutual information analysis and show that a simple CCIT-based scheme, referred to as statistical water-filling (SWF), can perform close to the optimal full CSIT-based one in MIMO systems with more receive antennas than transmit ones. We then focus on the implementation of SWF in practically coded systems. An iterative linear minimum mean squared error (LMMSE) receiver is assumed and an extrinsic information transfer (EXIT) chart type curve matching technique is developed based on Hadamard precoding techniques. Simulation results show that the proposed scheme can obtain significant performance improvement compared to the conventional equal power transmission. Finally, we show that the proposed scheme is also very efficient in multi-user uplink MIMO systems with distributed channel information.

## Design of Low-Complexity 2-D SOVA Detector for Shingled Magnetic Recording

- **Status**: ❌
- **Reason**: SMR용 2D SOVA 검출기 — Viterbi 기반 채널 검출 HW, LDPC 디코더가 아니고 BP에 이식할 기법 없음
- **ID**: ieee:6920058
- **Type**: journal
- **Published**: April 2015
- **Authors**: Ning Zheng, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/6920058
- **Abstract**: Shingled magnetic recording emerges as a promising near-term option to sustain the historical areal density growth of hard-disk drives while retaining conventional heads and media. Highly scaled shingled magnetic recording is subject to severe intertrack interference, which naturally demands 2-D read channel signal processing. By concurrently detecting multitrack read-back signals from a read head array, joint 2-D signal detection can fully exploit the 2-D interference to maximize the detection performance at the penalty of very high computational complexity. As modern read channel employs iterative signal detection and decoding and hard-disk drives are very cost sensitive, it is highly desirable to effectively reduce the 2-D signal detection computational complexity and hence silicon cost at minimal detection performance loss. This paper presents two low-complexity 2-D soft-output Viterbi algorithm (SOVA) detector design strategies for realizing multitrack joint 2-D detection, which represent different complexity versus performance tradeoffs. By carrying out simulations and application-specific integrated circuit design, this paper shows that, compared with the best symbol-based 2-D SOVA, it is feasible to achieve almost the same detection performance and meanwhile reduce the silicon area by more than 60% in three-track joint detection.

## On the Capacity of Slotted Aloha With Ancillary Channels

- **Status**: ❌
- **Reason**: slotted Aloha + codes-on-graphs 용량 분석 — MAC 프로토콜/이론적 bound, 채널 ECC 디코더/HW로 안 이어짐
- **ID**: ieee:7036076
- **Type**: journal
- **Published**: April 2015
- **Authors**: Andrea Munari, Gianluigi Liva, Matteo Berioli
- **PDF**: https://ieeexplore.ieee.org/document/7036076
- **Abstract**: In this letter, we focus on a legacy system operated with slotted-Aloha and complemented by a redundancy channel where nodes transmit replicas of their packets. The number of replicas follows a probability distribution, and successive interference cancelation is applied across channels. Leaning on the theory of codes on graphs and algebraic tools, we prove that the system can provide arbitrarily small error rate up to a certain load, beyond which packet losses have to be undergone with finite probability. Tight upper bounds on capacity are derived for both regions, characterizing the achievable performance as a function of the deployed ancillary resources. Simulation results for moderate MAC frame length are also provided.

## Performance of polar codes with successive cancellation decoding over PLC channels

- **Status**: ❌
- **Reason**: 비-LDPC 부호(polar+SC 디코딩) PLC 채널 성능 분석, 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:7147584
- **Type**: conference
- **Published**: 29 March-1
- **Authors**: Ju Jin, Hui-Myoung Oh, Sungsoo Choi +2
- **PDF**: https://ieeexplore.ieee.org/document/7147584
- **Abstract**: Polar codes are the first proven capacity achieving codes for a wide array of channels with low complexity. It is considered a next generation candidate for error-correcting codes (ECC) with turbo codes and low-density parity check (LDPC) codes. The aim of this paper is to analyze the bit error rate (BER) performance of polar codes with successive cancellation (SC) decoding over power line communication (PLC) channels. First, the performance of polar codes in additive white Gaussian noise (AWGN) and impulsive noise channels will be shown. In addition, a signal level limiter is used to mitigate the degradation of the performance over the impulse noise channels. Thereafter, the performance over real PLC channels is investigated. Simulation results show that polar codes are applicable to PLC channels with lower complexity than a turbo or a LDPC code.

## Syndrome based check node processing of high order NB-LDPC decoders

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) 체크노드 처리 — 비이진 LDPC는 제외
- **ID**: ieee:7124675
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Philipp Schläfer, Norbert Wehn, Matthias Alles +2
- **PDF**: https://ieeexplore.ieee.org/document/7124675
- **Abstract**: Non-binary low-density parity-check codes have superior communications performance compared to their binary counterparts. However, to be an option for future standards, efficient hardware architectures must be developed. State-of-the-art decoding algorithms lead to architectures suffering from low throughput and high latency. The check node function accounts for the largest part of the decoders overall complexity. In this paper a new, hardware aware check node algorithm is proposed. It has state-of-the-art communications performance while reducing the decoding complexity. Moreover the presented algorithm allows for partially or even fully parallel processing of the check node operations which is not applicable with currently used algorithms. It is therefore an excellent candidate for future high throughput hardware implementations.

## Design of non-binary irregular repeat-accumulate codes for reliable physical-layer network coding

- **Status**: ❌
- **Reason**: GF(q) 비이진 IRA 코드 설계(물리계층 네트워크 코딩) — 비이진 LDPC 제외
- **ID**: ieee:7124694
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Jinhong Yuan, Lei Yang, Tao Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/7124694
- **Abstract**: This paper investigates the design of practical non-binary irregular repeat-accumulate (IRA) codes for reliable physical-layer network coding. In the scheme, a same random-coset IRA code over Galois field GF(q) is employed at the two users. The relay computes the network coded message sequence directly from the superimposed signal using an iterative belief propagation algorithm. We explore the symmetry and permutation-invariant properties of the decoder's soft information distribution and adopt a two-dimension extrinsic information transfer chart to analyze and optimize the coding scheme. Numerical results demonstrate that our developed scheme achieves near-capacity performance in Gaussian two-way relay channels.

## Diversity of low-density lattices

- **Status**: ❌
- **Reason**: full-diversity 저밀도 격자 구성(integer-check matrix) — 격자 코드 전용, 바이너리 LDPC ECC 이식성 낮음
- **ID**: ieee:7124696
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Mayur Punekar, Joseph Jean Boutros
- **PDF**: https://ieeexplore.ieee.org/document/7124696
- **Abstract**: We describe full-diversity constructions of real lattices defined by their integer-check matrix, i.e. the inverse of their generator matrix. In the first construction suited to maximum-likelihood decoding, these lattices are defined by sparse (low-density) or non-sparse integer-check matrices. Based on a special structure of the lattice binary image, a second full-diversity lattice construction is described for sparse integer-check matrices in the context of iterative probabilistic decoding. Full diversity is theoretically proved in both cases. Computer simulation results also confirm that the proposed low-density lattices attain the maximal diversity order.

## On decoding algorithms for construction πA lattices

- **Status**: ❌
- **Reason**: Construction πA 격자 디코딩 — 격자 코드 전용, 바이너리 LDPC ECC와 무관
- **ID**: ieee:7124693
- **Type**: conference
- **Published**: 27-29 Apri
- **Authors**: Yu-Chih Huang, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/7124693
- **Abstract**: This paper revisits the Construction πA lattices recently proposed by Huang and Narayanan. This lattice construction is a generalization of the famous Construction A to the multilevel coding setting which preserves most of the structures of Construction A. Decoding algorithms of the Construction πA lattices are then studied. Two low complexity decoders are proposed to take advantage of the additional structure of the Construction πA lattices.

## Algorithms and Implementation of Long Euclidean-Geometry LDPC Codes for Space Communications

- **Status**: ❌
- **Reason**: 표준 EG-LDPC 인코딩 + QC 시프트레지스터 인코더(교과서 수준), 새 디코더/구성 기여 없음; 인코딩 회로는 NAND ECC 디코더 관점 기여 미미
- **ID**: ieee:7120571
- **Type**: conference
- **Published**: 24-26 Apri
- **Authors**: Mingxiao Ma, Junshe An
- **PDF**: https://ieeexplore.ieee.org/document/7120571
- **Abstract**: The encoding technique of long Euclidean-geometry LDPC codes is studied to meet the need of space missions. Firstly, the encoding algorithm is analyzed. The parity-check matrix is constructed by the incidence vector of points and lines in Euclidean geometry. The method for computing generator matrix is derived from solving matrix equation over GF(2). Secondly, according to the characteristics of quasi-cyclic matrix, a new encoding circuit of using feedback shift registers is proposed. Last, serial encoding circuit for resource-optimization and parallel encoding circuit for speed-optimization are designed respectively and implemented on Xilinx XC4V SX55 FPGA, with both reaching high encoding speed. The results show that the encoding scheme in this paper performs efficiently enough for space communications.

## Application of LT code technology in deep space communication

- **Status**: ❌
- **Reason**: LT(fountain) 부호와 LDPC 연접, 심우주 통신 응용. 떼어낼 신규 LDPC 디코더/구성 기법 없음 — fountain/연접 응용
- **ID**: ieee:7342800
- **Type**: conference
- **Published**: 23-24 Apri
- **Authors**: J Jane Sofia, J Jayakumari
- **PDF**: https://ieeexplore.ieee.org/document/7342800
- **Abstract**: Deep space communications have characteristics such as long delay, high code error rate and easily broken link etc. Easily broken links may lead to a certain degree of random flash break of Telemetry Tracking & Command signals, which in turn will result in the inconsiderable loss of data. Reliable downlink channel is necessary for deep space communication due to the distance between spacecraft and ground control station, the channel is effected by many interference factors so random and burst error are unavoidable. Integrity of fountain code can be considered in deep space communication. A special class of fountain code is furnished by LT code which solves the issue of data frames in deep space communication. Based on the performance concatenation of LT code and LDPC code provide more reliable solution for acquisition of deep space communication.

## Separation of encrypted and compressed image with auxillary information

- **Status**: ❌
- **Reason**: 암호화/압축 이미지 분리 + 보조정보 — LDPC ECC 무관, 소스코딩/보안 도메인
- **ID**: ieee:7322737
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Sam B. Baron, K. Ashokkumar, S. G. Surya Prakash +2
- **PDF**: https://ieeexplore.ieee.org/document/7322737
- **Abstract**: This paper proposes a novel plan of compacting encoded pictures with helper data. The substance manager scrambles the first uncompressed pictures furthermore creates some helper data, which will be utilized for information pressure and picture recreation. At that point, the channel supplier who can't get to the first substance may pack the encoded information by a quantization technique with ideal parameters that are gotten from a piece of helper data and a pressure proportion mutilation criteria, and transmit the packed information, which incorporate a scrambled sub-picture, the quantized information, the quantization parameters and an alternate piece of assistant data. At recipient side, the key picture substance can be reproduced utilizing the packed scrambled information and the mystery key.

## Approach to frame-misalignment in physical-layer network coding

- **Status**: ❌
- **Reason**: 물리계층 네트워크코딩 프레임 정렬 문제 해결에 EG-LDPC 부수 사용 — 무선 응용 특이적, 떼어낼 ECC 기법 없음
- **ID**: ieee:7178546
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: B. Nguyen, D. Haley, Y. Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7178546
- **Abstract**: By exploiting superimposed signals at relays, physicallayer network coding (PNC) could significantly improve the throughput of wireless communications systems. However, it is challenging to achieve perfect synchronization between superimposed signals at the relay. In this paper, we propose an approach to resolve the issue of frame-misalignment in PNC using type-I Euclidean geometry low-density parity-check (EG-LDPC) codes with cyclic prefix or zero padding. To estimate the arrival delay between two transmitted signals at the relay, Gold sequences are adopted as pilot sequences in our transmit frames. Simulation results show that our approach can effectively resolve the frame-misalignment issue in PNC.

## Diversity combining in wireless relay networks with partial channel state information

- **Status**: ❌
- **Reason**: 무선 릴레이망 다이버시티 컴바이너(SOCP 수신기) — LDPC ECC 무관, 무선 통신 도메인
- **ID**: ieee:7178549
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Kun Wang, Wenhao Wu, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/7178549
- **Abstract**: We develop a novel diversity combiner for joint reception in wireless relay networks with unknown relay-to-destination channel. The partially available channel information poses an obstacle for utilization of the relay diversity. We tackle this problem by formulating a unified second-order cone programming (SOCP) receiver which jointly detects and decodes transmitted signals from both source and relay nodes. Our results demonstrate that the proposed diversity combiners can achieve performance close to that of the maximum-ratio combiner based on full channel information.

## Deterministic constructions of binary measurement matrices with various sizes

- **Status**: ❌
- **Reason**: 압축센싱용 이진 측정행렬 결정적 구성 — 채널코딩 ECC 아님, 소스/CS 도메인
- **ID**: ieee:7178650
- **Type**: conference
- **Published**: 19-24 Apri
- **Authors**: Xin-Ji Liu, Shu-Tao Xia, Tao Dai
- **PDF**: https://ieeexplore.ieee.org/document/7178650
- **Abstract**: We introduce a general framework to deterministically construct binary measurement matrices for compressed sensing. The proposed matrices are composed of (circulant) permutation submatrix blocks and zero submatrix blocks, thus making their hardware realization convenient and easy. Firstly, using the famous Johnson bound for binary constant weight codes, we derive a new lower bound for the coherence of binary matrices with uniform column weights. Afterwards, a large class of binary base matrices with coherence asymptotically achieving this new bound are presented. Finally, by choosing proper rows and columns from these base matrices, we construct the desired measurement matrices with various sizes and they show empirically comparable performance to that of the corresponding Gaussian matrices.

## MIMO linear precoders with reduced complexity

- **Status**: ❌
- **Reason**: MIMO 선형 프리코더(PGP) 설계; LDPC는 EXIT 차트 복호 복잡도 언급뿐, 떼어낼 디코더 기법 없음
- **ID**: ieee:7117243
- **Type**: conference
- **Published**: 15-17 Apri
- **Authors**: Thomas Ketseoglou, Ender Ayanoglu
- **PDF**: https://ieeexplore.ieee.org/document/7117243
- **Abstract**: In this paper, the problem of designing a linear precoder for Multiple-Input Multiple-Output (MIMO) systems employing Low-Density Parity-Check (LDPC) codes is addressed under the constraint of independent receiving virtual antenna output groups, thus reducing the relevant transmitter and receiver complexities. Our approach constitutes an interesting generalization of Bit-Interleaved Coded Multiple Beamforming (BICMB) which has shown many benefits in MIMO systems. After examining the properties associated with independent output grouping, we proceed to propose an alternative, practical technique, called Per-Group Precoding (PGP), which groups together multiple input symbol streams and corresponding receiving branches in the “virtual” channel domain (after singular value decomposition of the original MIMO channel), and thus results in independent transmitting/receiving streams between groups. We show with numerical results that PGP offers almost optimal performance, albeit with significant reduction both in the precoder optimization and LDPC EXIT chart based decoding complexities.

## A high payload video steganography algorithm in DWT domain based on BCH codes (15, 11)

- **Status**: ❌
- **Reason**: BCH(15,11) 기반 비디오 스테가노그래피; 비-LDPC, ECC 디코더 이식 기법 없음
- **ID**: ieee:7117257
- **Type**: conference
- **Published**: 15-17 Apri
- **Authors**: Ramadhan J. Mstafa, Khaled M. Elleithy
- **PDF**: https://ieeexplore.ieee.org/document/7117257
- **Abstract**: Video steganography has become a popular topic due to the significant growth of video data over the Internet. The performance of any steganography algorithm depends on two factors: embedding efficiency and embedding payload. In this paper, a high embedding payload of video steganography algorithm has been proposed based on the BCH coding. To improve the security of the algorithm, a secret message is first encoded by BCH(n, k, t) coding. Then, it is embedded into the discrete wavelet transform (DWT) coefficients of video frames. As the DWT middle and high frequency regions are considered to be less sensitive data, the secret message is embedded only into the middle and high frequency DWT coefficients. The proposed algorithm is tested under two types of videos that contain slow and fast motion objects. The results of the proposed algorithm are compared to both the Least Significant Bit (LSB) and [1] algorithms. The results demonstrate better performance for the proposed algorithm than for the others. The hiding ratio of the proposed algorithm is approximately 28%, which is evaluated as a high embedding payload with a minimal tradeoff of visual quality. The robustness of the proposed algorithm was tested under various attacks. The results were consistent.

## Enhancing satellite system throughput using adaptive HARQ for delay tolerant services in mobile communications

- **Status**: ❌
- **Reason**: 위성 적응형 HARQ 처리량 향상; 상호정보 기반 재전송 기법, 떼어낼 LDPC 디코더/구성 없음
- **ID**: ieee:7117278
- **Type**: conference
- **Published**: 15-17 Apri
- **Authors**: Rami Ali Ahmad, Jérôme Lacan, Fabrice Arnal +2
- **PDF**: https://ieeexplore.ieee.org/document/7117278
- **Abstract**: We propose the introduction of adaptive hybrid automatic repeat request (HARQ) in the context of mobile satellite communications. HARQ schemes which are commonly used in terrestrial links, can be adapted to improve the throughput for delay tolerant services. The proposed method uses the estimation of the mutual information between the received and the sent symbols, in order to estimate the number of bits necessary to decode the message at next transmission. We evaluate the performance of our method by simulating a land mobile satellite (LMS) channel. We compare our results with the static HARQ scheme, showing that our adaptive retransmission technique has better efficiency while keeping an acceptable delay for services.
