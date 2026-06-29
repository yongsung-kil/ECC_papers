# IEEE Xplore — 2006-10


## Decoding LDPC Codes Over Integer Residue Rings

- **Status**: ❌
- **Reason**: 정수 잉여환 Z_q(q=p^m) 위 LDPC 다단 BP 디코딩 — 비이진/링 기반 LDPC라 제외(바이너리 한정)
- **ID**: ieee:1705029
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: M.A. Armand, K.S. Ng
- **PDF**: https://ieeexplore.ieee.org/document/1705029
- **Abstract**: This correspondence presents a multistage decoding approach for a free Zopfq-submodule of Zopfq N of rank K defined by a sparse (N-K)timesN parity-check matrix overZopf q where q=pm, p=2 and m>1. The proposed method involves the repeated application of belief propagation decoding to exploit the natural ring epimorphism ZopfqrarrZopfp l:r|rarr Sigma i=0 l-1r(i)pi with kernel p lZopfq for each l, 1lesllesm, where Sigma i=0 m-1r(i)pi is the p-adic expansion of r. Computer simulations for codes of rate half and moderate length on an additive white Gaussian noise (AWGN) channel with various modulation schemes show that such a decoding strategy offers an additional coding gain of between 0.07-0.1 dB over a single-stage decoding approach

## Low-Density Parity-Check Lattices: Construction and Decoding Analysis

- **Status**: ❌
- **Reason**: LDPC lattice 구성 + max-sum을 격자 Tanner 그래프로 일반화 — 격자 부호 전용이고 바이너리 LDPC ECC가 아님(Construction D' 격자)
- **ID**: ieee:1705007
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: M.-R. Sadeghi, A.H. Banihashemi, D. Panario
- **PDF**: https://ieeexplore.ieee.org/document/1705007
- **Abstract**: Low-density parity-check codes (LDPC) can have an impressive performance under iterative decoding algorithms. In this paper we introduce a method to construct high coding gain lattices with low decoding complexity based on LDPC codes. To construct such lattices we apply Construction D', due to Bos, Conway, and Sloane, to a set of parity checks defining a family of nested LDPC codes. For the decoding algorithm, we generalize the application of max-sum algorithm to the Tanner graph of lattices. Bounds on the decoding complexity are derived and our analysis shows that using LDPC codes results in low decoding complexity for the proposed lattices. The progressive edge growth (PEG) algorithm is then extended to construct a class of nested regular LDPC codes which are in turn used to generate low density parity check lattices. Using this approach, a class of two-level lattices is constructed. The performance of this class improves when the dimension increases and is within 3 dB of the Shannon limit for error probabilities of about 10-6. This is while the decoding complexity is still quite manageable even for dimensions of a few thousands

## Turbo Equalization With Single-Parity Check Codes and Unequal Error Protection Codes

- **Status**: ❌
- **Reason**: single-parity check + turbo equalization, 비-LDPC 부호이고 떼어낼 LDPC BP 이식 기법 없음
- **ID**: ieee:1704370
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: B.M. Kurkoski, K. Yamaguchi, K. Kobayashi
- **PDF**: https://ieeexplore.ieee.org/document/1704370
- **Abstract**: The performance of turbo equalization with interleaved single-parity check codes on partial-response channels is evaluated. Single-parity check codes are weak codes, but are shown to have modest performance gain. The proposed system achieves gains of 3.5, 3.4, 2.7, and 2.4 dB with code rates of 19/20,24/25,49/50, and 63/64, respectively, at a BER of 10-5. The complexity of the proposed decoder is significantly lower than that of turbo equalization using standard low-density parity-check codes. These single-parity check codes are modified to be unequal error protection codes, designed to decrease the probability that Viterbi error events span Reed-Solomon symbol boundaries, resulting in a decrease of the sector error rate. Once such code gains an additional 0.1 dB over a single-parity check code of the same code rate of 24/25

## A hybrid coding scheme for the Gilbert-Elliott channel

- **Status**: ❌
- **Reason**: Gilbert-Elliott 채널용 parity+Hamming 하이브리드 부호. 비-LDPC 결합이고 채널 특이적, NAND로 떼어낼 LDPC 기법 없음
- **ID**: ieee:1710334
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: Jinghu Chen, R.M. Tanner
- **PDF**: https://ieeexplore.ieee.org/document/1710334
- **Abstract**: In this paper, we study the performance of different graph-based error-correcting codes over Gilbert-Elliott (GE) channels. We propose a hybrid coding scheme in which each code bit is checked by both a parity-check code and a Hamming code. A hybrid code can be represented by a code-to-code graph, which can be used to optimize the code. Asymptotic minimum distance properties of the hybrid code are derived, and it is shown that the expected minimum distance of the hybrid code increases linearly with respect to the code length. Simulation results show that for a typical GE channel, hybrid codes can outperform regular low-density parity-check codes by more than an order of magnitude, in terms of bit-error rate.

## Slepian-Wolf Coded Nested Lattice Quantization for Wyner-Ziv Coding: High-Rate Performance Analysis and Code Design

- **Status**: ❌
- **Reason**: Wyner-Ziv/Slepian-Wolf 소스코딩(압축), 채널 ECC 아님 — LDPC는 소스코딩 도구로 부수 사용
- **ID**: ieee:1704999
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: Zhixin Liu, S. Cheng, A.D. Liveris +1
- **PDF**: https://ieeexplore.ieee.org/document/1704999
- **Abstract**: Nested lattice quantization provides a practical scheme for Wyner-Ziv coding. This paper examines the high-rate performance of nested lattice quantizers and gives the theoretical performance for general continuous sources. In the quadratic Gaussian case, as the rate increases, we observe an increasing gap between the performance of finite-dimensional nested lattice quantizers and the Wyner-Ziv distortion-rate function. We argue that this is because the boundary gain decreases as the rate of the nested lattice quantizers increases. To increase the boundary gain and ultimately boost the overall performance, a new practical Wyner-Ziv coding scheme called Slepian-Wolf coded nested lattice quantization (SWC-NQ) is proposed, where Slepian-Wolf coding is applied to the quantization indices of the source for the purpose of compression with side information at the decoder. Theoretical analysis shows that for the quadratic Gaussian case and at high rate, SWC-NQ performs the same as conventional entropy-coded lattice quantization with the side information available at both the encoder and the decoder. Furthermore, a nonlinear minimum mean-square error (MSE) estimator is introduced at the decoder, which is theoretically proven to degenerate to the linear minimum MSE estimator at high rate and experimentally shown to outperform the linear estimator at low rate. Practical designs of one- and two-dimensional nested lattice quantizers together with multilevel low-density parity-check (LDPC) codes for Slepian-Wolf coding give performance close to the theoretical limits of SWC-NQ

## Sensor Networks With Mobile Access: Energy and Capacity Considerations

- **Status**: ❌
- **Reason**: 센서네트워크 에너지/용량 정보이론. 코딩 기법 없음
- **ID**: ieee:1710346
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: G. Mergen, Q. Zhao, L. Tong
- **PDF**: https://ieeexplore.ieee.org/document/1710346
- **Abstract**: Sensor network with mobile access (SENMA) is an architecture in which randomly deployed low-power sensors are orchestrated by a few powerful mobile access points. This paper considers SENMA from energy-efficiency and information-theoretic perspectives. By allowing sensors to propagate data directly to mobile access points over multiaccess channels and relieving sensors from energy-consuming network functions, SENMA has the potential of offering orders of magnitude of improvement in energy efficiency over the multihop ad hoc architecture, as demonstrated by our analysis on scalability. Optimization configurations of SENMA such as the altitude, the trajectory, and the coverage of access points are considered next, using the sum-rate as the performance metric. Optimal strategies for single and multiple access points are determined. For multiple access points, the possibility of and the gain due to cooperation (i.e., joint decoding of signals received at different access points) are investigated.

## Constellation Design for Trellis-Coded Unitary Space–Time Modulation

- **Status**: ❌
- **Reason**: trellis-coded 유니터리 공간-시간 변조 성좌 설계. LDPC 무관
- **ID**: ieee:1710349
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: Y. Wu, V. Lau, M. Patzold
- **PDF**: https://ieeexplore.ieee.org/document/1710349
- **Abstract**: We consider the problem of creating signal constellations for trellis-coded unitary space–time communication links, where neither the transmitter nor the receiver knows the fading gains of the channel. Our study includes design techniques for trellis-coded schemes with and without parallel paths, which allows us to find a tradeoff between low complexity and high performance. We present a new formulation of the constellation design problem for trellis-coded unitary space–time modulation schemes. The two key differences in our approach against those of other authors are that we not only combine the constellation design and mapping by set partitioning into one step, but we also use directly the Chernoff bound of the pairwise error probability as a design metric. By novelly employing a theorem for the Clarke subdifferential of the sum of the$k$largest singular values of the unitary matrix, we also present a numerical optimization procedure for finding signal constellations resulting in high-performance communications systems. To demonstrate the advantages of our new design method, we report the best constellations found for trellis-coded unitary space–time modulation systems. Simulation results show that these constellations achieve 1 dB coding gain against the usually used constellations.

## Channel Estimation for MIMO-OFDM Systems by Modal Analysis/Filtering

- **Status**: ❌
- **Reason**: MIMO-OFDM 채널 추정. ECC 아님, LDPC 무관
- **ID**: ieee:1710345
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: M. Cicerone, O. Simeone, U. Spagnolini
- **PDF**: https://ieeexplore.ieee.org/document/1710345
- **Abstract**: In this paper, we investigate the benefits of exploiting the a priori information about the structure of the multipath channel on the performance of channel estimation for multiple-input multiple-output (MIMO)-orthogonal frequency-division multiplexing (OFDM) systems. We first approach this problem from the point of view of estimation theory by computing a lower bound on the estimation error and studying its properties. Then, based on the insight obtained from the analysis, efficient channel estimators are designed that perform close to the derived limit. The proposed channel estimators compute the long-term features of the multipath channel model through a subspace tracking algorithm by identifying the invariant (over multiple OFDM symbols) space/time modes of the channel (modal analysis). On the other hand, the fast-varying fading amplitudes are tracked by using least-squares techniques that exploit temporal correlation of the fading process (modal filtering). The analytic treatment is complemented by thorough numerical investigation in order to validate the performance of the proposed techniques. MIMO-OFDM with bit-interleaved coded modulation and MIMO-turbo equalization is selected as a benchmark for performance evaluation in terms of bit-error rate.

## Timing Recovery With Frequency Offset and Random Walk: Cramer–Rao Bound and a Phase-Locked Loop Postprocessor

- **Status**: ❌
- **Reason**: 타이밍 복구/PLL CRB. ECC 아님
- **ID**: ieee:1710347
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: A.R. Nayak, J.R. Barry, G. Feyh +1
- **PDF**: https://ieeexplore.ieee.org/document/1710347
- **Abstract**: We consider the problem of timing recovery for bandlimited, baud-rate sampled systems with intersymbol interference and a timing offset that can be modeled as a combination of a frequency offset and a random walk. We first derive the Cramer–Rao bound (CRB), which is a lower bound on the estimation-error variance for any timing estimator. Conventional timing recovery is based on a phase-locked loop (PLL). We compare the conventional timing recovery method with the CRB for realistic timing parameters for the magnetic recording channel, and observe a 7 dB signal-to-noise ratio gap between the two. Next, we propose a PLL postprocessor based on the maximum a posteriori estimation principle that performs to within 1.5 dB of the CRB. This postprocessor performs time-invariant filtering and time-varying scaling of the PLL timing estimates. The refined timing estimates from the postprocessor are then used to get refined samples by interpolating the samples taken at the PLL's timing estimates. Finally, we present suboptimal implementations that allow a performance-complexity tradeoff.

## Reliability-Based Reed-Solomon Decoding for Magnetic Recording Channels

- **Status**: ❌
- **Reason**: Reed-Solomon 소프트디코딩(Chase-type), 비-LDPC 부호이고 RS 전용 기법으로 LDPC BP 이식성 없음
- **ID**: ieee:1704378
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: H. Xia, J.R. Cruz
- **PDF**: https://ieeexplore.ieee.org/document/1704378
- **Abstract**: The performance of soft-decision Reed-Solomon decoding using belief propagation (BP) is investigated on partial-response equalized magnetic recording channels. A simplification of the BP algorithm, which can be viewed as a Chase-type algorithm, is presented and analyzed

## A hybrid PAPR reduction scheme for coded OFDM

- **Status**: ❌
- **Reason**: OFDM PAPR 감소 + IRA 코드 EXIT 최적화, 무선 응용 특이적이고 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:1705933
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: Guosen Yue, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/1705933
- **Abstract**: We consider schemes for reducing the peak-to-average power ratio (PAPR) in coded orthogonal frequency-division multiplexing (OFDM) systems. We develop a new PAPR reduction technique using the label-inserted encoder of a random-like code and the soft amplitude limiter (SAL). Using this hybrid scheme provides 5.5 dB PAPR reduction in an OFDM system with 128 subcarriers, 4-bit selection and 3 dB clipping. Besides the significant PAPR reduction, the scheme also enjoys other advantages such as small overhead, low complexity, no side information transmission, and little performance loss. Among various random-like codes, the irregular repeat accumulate (IRA) code is the best choice for its simple encoder and capacity achieving performance. The scheme can be directly applied to multiple-input multiple-output (MIMO) OFDM systems. The capacity of the clipped MIMO-OFDM systems is analyzed based on a Gaussian approximation of the clipping noise. We consider an iterative receiver with soft MAP MIMO-OFDM detector. For both single antenna and multiple antenna systems, the encoder part is independent in the hybrid scheme, thus no additional constraint is applied to the IRA code optimization. The IRA codes are designed for the ergodic MIMO-OFDM systems with different PAPR reduction settings, more specifically different clipping ratios, based on the extrinsic information transfer (EXIT) charts. Simulation results show that the hybrid scheme with 3 dB clipping can achieve as good PAPR reduction performance as the simple clipping with 0 dB ratio but incurs much less performance loss at the receiver

## Enhanced carrier frequency offset estimation for OFDM using channel side information

- **Status**: ❌
- **Reason**: OFDM CFO 추정, LDPC 무관한 무선 동기화 기법
- **ID**: ieee:1705940
- **Type**: journal
- **Published**: Oct. 2006
- **Authors**: D. Huang, K.B. Letaief
- **PDF**: https://ieeexplore.ieee.org/document/1705940
- **Abstract**: Carrier frequency offset (CFO) in OFDM systems, which induces the loss of orthogonality among OFDM subcarriers, can result in significant performance degradation. As a result, it needs to be estimated and compensated for. In this paper, we present a general CFO estimator based on the maximum likelihood (ML) estimation criterion, with which CFO can be obtained using training OFDM symbols, pilot tones, null subcarriers, or a combination of them. Using the proposed CFO estimator, the performance of CFO estimation can be significantly improved by taking advantage of the channel side information. In particular, using the channel statistics information, such performance improvement can be achieved for low SNR values and all SNR values over Rayleigh fading channels and Ricean fading channels, respectively. When the complete channel impulse response (CIR) information is available, simulation results will show that the performance improvement can be more than 6 dB. To further demonstrate the capability of the proposed CFO estimator, we will consider an OFDM system using the signal structure of the IEEE WLAN standard 802.11a. Compared with previous work using null sub-carriers alone, we will show that by taking advantage of the pilot tones, null sub-carriers, and channel statistics, the performance of CFO estimation can be improved by about 2 dB

## Dependency channel modeling for a LDPC-based Wyner-Ziv video compression scheme

- **Status**: ❌
- **Reason**: Wyner-Ziv 비디오 압축의 dependency channel 모델링; 분산 소스코딩, 채널 ECC 아님
- **ID**: ieee:4106520
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Ronald P. Westerlaken, Stefan Borchert, Rene Klein Gunnewiek +1
- **PDF**: https://ieeexplore.ieee.org/document/4106520
- **Abstract**: Research in distributed video coding for low complexity encoding has shown that without knowledge of the correlation between source and side information (i.e. the behavior of the dependency channel), the performance is substantially below that of well known state-of-the-art video coders. In a practical system the decoder needs to estimate the statistics in this dependency channel. In this paper we investigate the relation between the compression ratio and the sensitivity of the estimated channel model parameter at the decoder side. We observe that this is a hard task, but not unrealistic. We show that the tolerable parameter range is very dependent on the compression ratio and the (actual) statistics in the dependency channel.

## Combined Error Protection and Compression with Turbo Codes for Image Transmission using a JPEG2000-Like Architecture

- **Status**: ❌
- **Reason**: 터보 부호 기반 JSCC 이미지 전송; 비-LDPC, 디코더 기법 LDPC 이식 근거 없음
- **ID**: ieee:4106656
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Maria Fresia, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/4106656
- **Abstract**: In this paper, a joint source channel coding scheme for error resilient image transmission is proposed. Instead of compressing the image using the classical entropy coder, the redundancy of the image is exploited by using turbo codes for both data compression and error protection. At the decoder, the bit-planes are reconstructed in sequence by a multistage decoder. By properly choosing rate and puncturing, the system is able to approach the limit theoretically attainable and to outperform the separated approach of a JPEG2000 compressed image and the best turbo codes for the same overall length.

## Video Multicast over Heterogeneous Networks Based on Distributed Source Coding Principles

- **Status**: ❌
- **Reason**: 분산 소스코딩 기반 비디오 멀티캐스트; LDPC 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:4106634
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Vladimir Stankovic, Yang Yang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/4106634
- **Abstract**: Real-time multimedia multicast over wireless networks is an exciting application that has generated a lot of interest recently. Its main challenge lies in the stringent bandwidth and time-delay requirements of real-time multimedia and severe impairments of the wireless channels. We develop a system for multimedia multicast over wireless-wireline networks, that leverages the knowledge on network information theory, multimedia processing, error control, and networking. In particular, the encoded multimedia data are broadcast to multiple Internet servers over a wireless channel. Each server merely compresses the signal it has received using distributed source coding. The receiver collects bitstreams from the servers before performing joint decoding. Due to spatial diversity gain and distributed source coding, our system significantly outperforms conventional solutions.

## On Compression of Encrypted Images

- **Status**: ❌
- **Reason**: 암호화 이미지 압축(소스 코딩); LDPC를 압축에 사용, 채널 ECC 아님
- **ID**: ieee:4106518
- **Type**: conference
- **Published**: 8-11 Oct. 
- **Authors**: Daniel Schonberg, Stark Draper, Kannan Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/4106518
- **Abstract**: Coding schemes for secure and efficient communication over noiseless public channels traditionally compress and then encrypt the source data. In some cases reversing the ordering of compression and encryption would be useful, e.g., in enabling the efficient distribution of protected media content. Indeed, not only is it possible to reverse the order, but under some conditions neither security nor compression efficiency need be sacrificed. In earlier work on this problem we have assumed that the source data is either memoryless or has a 1-D Markov structure. Such models are poor matches for the 2-D structure of images. In this work, we use a 2-D source model, and develop a scheme to compress encrypted images based on LDPC codes. We present practical simulation results for compressing bi-level images. In tests, we are able to compress an encrypted 10, 000 bit bi-level image to 4, 299 bits and successfully recover the image exactly. In previous works, the best analogous 1-D model (operating on a raster scanned data sequence of the same source) could only compress the image to 7, 710 bits.

## Robust Video Transmission Scheme Using Dynamic Rate Selection LDPC and RS codes

- **Status**: ❌
- **Reason**: 비디오 전송용 LDPC+RS 하이브리드 FEC, 응용 특이적이고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4281906
- **Type**: conference
- **Published**: 4-6 Oct. 2
- **Authors**: Liu Qi, Lu Yang, Wang Wensheng +2
- **PDF**: https://ieeexplore.ieee.org/document/4281906
- **Abstract**: Compressed video is very vulnerable to bit errors or erasure errors introduced during transmission. Thus FEC is necessary to achieve robust video communication. In this paper, we propose a hybrid dynamic rate selection FEC scheme to utilize low density parity check (LDPC) codes and Reed-Solomon (RS) code to achieve robust video communication. We use the powerful LDPC error correcting code to combat bit-errors and RS code to combat erasure errors. The code rates of the LDPC code and RS code are dynamically adjusted according to the channel bit-error rate and erasure error rate. But the overall code rate in the transmission is fixed. We compare the considered schemes in terms of video quality using the new H.264/AVC video standard. Simulation results show that with this hybrid FEC scheme, robust video transmission can be achieved and the video quality is greatly improved compared with the constant code rate FEC scheme

## Distributed Coding of Random Dot Stereograms with Unsupervised Learning of Disparity

- **Status**: ❌
- **Reason**: 분산 소스 압축(스테레오) EM 학습, 채널 ECC 아님 - 소스 코딩 제외
- **ID**: ieee:4064507
- **Type**: conference
- **Published**: 3-6 Oct. 2
- **Authors**: David Varodayan, Aditya Mavlankar, Markus Flierl +1
- **PDF**: https://ieeexplore.ieee.org/document/4064507
- **Abstract**: Distributed compression is particularly attractive for stereoscopic images since it avoids communication between cameras. Since compression performance depends on exploiting the redundancy between images, knowing the disparity is important at the decoder. Unfortunately, distributed encoders cannot calculate this disparity and communicate it. We consider a toy problem, the compression of random dot stereograms, and propose an expectation maximization algorithm to perform unsupervised learning of disparity during the decoding procedure. Our experiments show that this can achieve twice as efficient compression compared to a system with no disparity compensation and perform nearly as well as a system which knows the disparity through an oracle

## Variable Rate LDPC Codes for Wireless Applications

- **Status**: ❌
- **Reason**: 무선용 가변레이트 LDPC의 pseudo-puncturing 전략, 떼어낼 신규 디코더/HW 없이 무선 응용 특이적
- **ID**: ieee:4129922
- **Type**: conference
- **Published**: 29 Sept.-1
- **Authors**: Marco Baldi, Giovanni Cancellieri, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/4129922
- **Abstract**: This paper deals with the problem of designing good rate-variable LDPC codes for wireless applications, where fast link adaptation is required in order to maximize the system efficiency. In particular, we show that the so-called "pseudo-puncturing" strategy, recently introduced, can be used as a valid alternative to more conventional solutions, by ensuring good performance while maintaining limited complexity

## Proposal of a novel punctured LDPC coding scheme for Ultra Wide Band system

- **Status**: ❌
- **Reason**: UWB용 펑처링 LDPC 방식이나 펄스 반복 후 펑처링이라는 UWB 시스템 특이 기법, NAND 이식 가능한 부호설계 기여 아님
- **ID**: ieee:4168371
- **Type**: conference
- **Published**: 26-29 Oct.
- **Authors**: Fangni Chen, Shiju Li
- **PDF**: https://ieeexplore.ieee.org/document/4168371
- **Abstract**: As a new spread spectrum system, an ultra wide band technology has attracted much attention in high speed indoor multiple access radio communications. An UWB communication system with channel coding is noticing for avoiding the performance degradation due to adverse channel propagation conditions. In this paper, we propose a novel punctured low-density parity-check (LDPC) coding scheme for UWB systems. Differently from the conventional puncture coding, we puncture the pulses after the UWB system repeating the LDPC coded bits. From our analysis and numerical results, we find this new scheme give a significant performance gain compared with the conventional scheme. Furthermore, the receiver construction is simpler since the puncture position information is not needed.

## LDPC/RS Concatenated Codes for Frequency-Hop Packet Radio Networks with Partial-Band Interference

- **Status**: ❌
- **Reason**: LDPC/RS concatenated, packet erasure correction (fountain/erasure형) 무선 응용; 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:4149764
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Le Ru, Xingmin Du, Duyan Bi +2
- **PDF**: https://ieeexplore.ieee.org/document/4149764
- **Abstract**: In this paper, we introduce packet low-density parity-check (packet-LDPC) code for frequency-hop packet radio networks. We propose one concatenated coded architecture of employding an inner RS code and a packet-LDPC code as the outer code. Then we present simulation results of the LDPCIRS concatenated coded system compared with RSIRS concatenated coded system with noise and partial-band interference. Results show that this proposed LDPCIRS concatenated coded architecture provides good packet erasure correction performance and very low encoding and decoding complexity forfrequency-hop packet radio system with the presence of noise and partial-band interference.

## Performance of Low-Density Parity-Check (LDPC) Coded OFDM system based on Adaptive Power Allocation Algorithm

- **Status**: ❌
- **Reason**: LDPC-COFDM 적응 전력할당 무선 응용; LLR 디코딩 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4149718
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Xiaoguang Wu, Zhi Zhang, Jun Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/4149718
- **Abstract**: A LDPC-COFDM system model based on adaptive algorithm can allocate transmit power and bits among sub-carriers according to the channel gain of each sub-channel. An adaptive power allocation algorithm, which is beneficial for log likelihood ratio decoding of LDPC coded modulation, is proposed in this paper. The simulation results show that the model can effectively improve the bit-error-rate (BER) performance of the system, compared with the traditional OFDM system based on equal power allocation, adapting to the time-variant behavior of the multi-path fading channel.

## Blocking Probability Computation of Optical Networks: A Factor Graph Model Approach

- **Status**: ❌
- **Reason**: 광 네트워크 blocking probability를 factor graph로 계산 — ECC 아님, 디코더/구성 기여 없음
- **ID**: ieee:4149789
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Ziyu Shao, Jian Ni, Zhengbin Li
- **PDF**: https://ieeexplore.ieee.org/document/4149789
- **Abstract**: How to compute the blocking probability of optical networks quickly and exactly is an open problem. Thus many exact and approximate methods are proposed to tackle this problem. In this paper, we introduce the factor graph model approach . The relationship between network topology and corresponding factor graph representation is also discussed. Simulation results show that in cyclic factor graph representation, the proposed approach outperforms the reduced load approximation scheme, a commonly used method in the field of optical network

## Protograph LDPC Codes over Burst Erasure Channels

- **Status**: ❌
- **Reason**: burst erasure 채널용 protograph LDPC, erasure 응용 특이적이며 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4086595
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Dariush Divsalar, Sam Dolinar, Christopher Jones
- **PDF**: https://ieeexplore.ieee.org/document/4086595
- **Abstract**: In this paper we design high rate protograph based LDPC codes suitable for binary erasure channels. To simplify the encoder and decoder implementation for high data rate transmission, the structure of codes are based on protographs and circulants. These LDPC codes can improve data link and network layer protocols in support of communication networks. Two classes of codes were designed. One class is designed for large block sizes with an iterative decoding threshold that approaches capacity of binary erasure channels. The other class is designed for short block sizes based on maximizing minimum stopping set size. For high code rates and short blocks the second class outperforms the first class. A scheme is proposed to use these LDPC codes over burst erasure channels. The proposed encoding method is also applicable to cases when packets are frequency hopped over channels with partial band jamming or frequency selective fading. Various LDPC codes are compared and simulation results are provided

## Performance Comparison Between Turbo Code and Rate-Compatible LDPC Code for Evolved Utra Downlink OFDM Radio Access

- **Status**: ❌
- **Reason**: 터보 vs LDPC PER/복잡도 비교 무선 OFDM 응용, 표준 layered BP/delta-min만 언급, 떼어낼 신규 디코더 기여 없음
- **ID**: ieee:4086445
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Naoto Ohkubo, Nobuhiko Miki, Yoshihisa Kishiyama +2
- **PDF**: https://ieeexplore.ieee.org/document/4086445
- **Abstract**: This paper compares the Release 6 turbo code and rate-compatible low-density parity-check (LDPC) codes based on the packet error rate (PER) performance and decoding complexity in order to clarify the most appropriate channel coding scheme in the OFDM based evolved UTRA (E-UTRA) downlink. Simulation results and manipulation of the decoding complexity show that although the rate-compatible/quasi-cyclic (RC/QC)-LDPC code employing a normalized layered belief propagation (BP) method can reduce the computational complexity by approximately 30% for the channel coding rate of R=3/4, the required average received signal energy per bit-to-noise power spectrum density ratio (Eb/N 0) is degraded by approximately 0.2-0.3 dB both for R=1/3 and 3/4 compared to that for the turbo code. Moreover, the decoding complexity level of the RC/QC-LDPC code with the delta-min algorithm is almost the same or higher than that for the turbo code with a slight degradation in the required received Eb/N0. Although the decoding complexity level of the ZigZag code is decreased compared to that of the turbo code, the code brings about a distinct loss in the required average received Eb/N0 of approximately 0.4 dB. Finally, the turbo single parity check (SPC) code improves the PER performance compared to the ZigZag code, i.e., achieves almost the same PER performance as that for the turbo code, at the cost of a two-fold increase in the decoding complexity. As a result, we conclude that the turbo code is more promising than the LDPC codes for prioritizing the achievable performance and as the channel coding scheme for the shared data channel in the E-UTRA

## Irregular Designs for Two-State Systematic with Serial Concatenated Parity Codes

- **Status**: ❌
- **Reason**: IRA/S-SCP turbo-like 코드 불규칙 설계, EXIT 기반 — 바이너리 LDPC BP에 직접 이식할 비의존적 기법 불명확, 무선 캐파시티 설계 중심
- **ID**: ieee:4086358
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Jordan Melzer, Keith M. Chugg
- **PDF**: https://ieeexplore.ieee.org/document/4086358
- **Abstract**: The irregular repeat accumulate (IRA) codes introduced by Jin et al. (2000) are structured low density parity check (LDPC) codes that are known to perform as well as the best unstructured LDPCs. IRAs reach rates that are quite close to capacity on the additive white Gaussian noise (AWGN) channel, can be both encoded and decoded in linear time, are perceived to be low complexity codes, and have been adopted into recent standards. Systematic with serially concatenated parity (S-SCP) codes were recently introduced as a class of turbo like codes with members that exhibit good performance over a wide range of block sizes, code rates, and target error probabilities. In this paper we introduce irregular designs for systematic with serially concatenated parity (Ir-S-SCP) codes and show that both for near-capacity and more practical lower-complexity designs, irregular two-state S-SCP codes can be designed to achieve the performance of IRA codes at lower complexity

## Design of Nonbinary LDPC Codes over GF(q) for Multiple-Antenna Transmission

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC — 명시적 제외 대상
- **ID**: ieee:4086398
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Rong-hui Peng, Rong-rong Chen
- **PDF**: https://ieeexplore.ieee.org/document/4086398
- **Abstract**: In this paper, we investigate the application of nonbinary low density parity check (LDPC) codes over Galois field GF(q) for multiple-input multiple-output (MIMO) fading channels. Depending on the size of the Galois field GF(q), we study both iterative systems which employ joint MIMO detection and channel decoding, and non-iterative systems which employ separate MIMO detection and channel decoding. Based on the concept of coset LDPC code and coset MIMO detector, we develop extrinsic information transfer chart (EXIT) approaches for the design of nonbinary LDPC codes for MIMO channels. Simulation results show that the proposed systems employing the designed nonbinary LDPC codes achieve a superior performance than that of the best optimized binary LDPC codes at a reduced complexity

## Space-Time Block Codes for Quasi-synchronous Cooperative Diversity

- **Status**: ❌
- **Reason**: space-time block code 설계, LDPC 무관 비-LDPC 부호
- **ID**: ieee:4086583
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: A. Roger Hammons, Ross E. Conklin
- **PDF**: https://ieeexplore.ieee.org/document/4086583
- **Abstract**: Li and Xia have recently investigated the design of space-time codes that achieve full spatial diversity for quasi-synchronous cooperative communications. They show that certain of the binary space-time trellis codes derived from the Hammons-El Gamal stacking construction are delay tolerant and can be used in the multilevel code constructions by Lu and Kumar to produce delay tolerant space-time codes for PSK and QAM signaling. In prior work, the first author has developed generalizations of the Lu-Kumar construction for more general AM-PSK constellations that also preserve the delay tolerance of the underlying constituent codes and exhibited a new construction of short block codes that achieve significant levels of delay tolerance. Use of space-time block codes (STBC) of short length in the Li-Xia transmission framework results in a significant loss of rate. We present generalizations of that framework that make short STBC a potentially attractive option for quasi-synchronous cooperative diversity

## Secure Spread Spectrum Communication Using Ultrawideband Random Noise Signals

- **Status**: ❌
- **Reason**: UWB 랜덤노이즈 보안 통신, LDPC는 채널코딩 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:4086414
- **Type**: conference
- **Published**: 23-25 Oct.
- **Authors**: Jack Chuang, Matthew W. DeMay, Ram M. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/4086414
- **Abstract**: Ultrawideband (UWB) random noise signals provide secure communications because they cannot, in general, be detected using conventional receivers and are jam-resistant. We describe the theoretical underpinnings of a novel spread spectrum technique that can be used for covert communications using transmissions over orthogonal polarization channels. The technique is based on the use of heterodyne correlation techniques to inject coherence in a random noise signal. The transmitted signal is featureless and appears unpolarized and noise-like; thus linearly polarized receivers are unable to identify, detect, or otherwise extract useful information from the signal. The system is immune from interference caused by high power linearly polarized signals. Dispersive effects caused by the atmosphere and other factors are significantly reduced since both polarization channels operate over the same frequency band. Our results indicate that the proposed scheme can recover voice and data signals with superior fidelity. Simulations show that we can achieve BER values of 10 at an SNR of around -6 dB without channel coding and BER values sufficient for data and video at much lower SNRs when channel coding is employed, which indicates excellent performance under covert conditions such as operating under the enemy receiver's thermal noise floor. We also show preliminary field test results with the baseband processing implemented within a software defined radio architecture that clearly validate the system concept

## LDPC-Based Secure Wireless Communication with Imperfect Knowledge of the Eavesdropper's Channel

- **Status**: ❌
- **Reason**: 물리계층 보안/비밀키합의(Gaussian reconciliation+privacy amplification); 보안·reconciliation 원칙 제외, 떼어낼 디코더기법 없음
- **ID**: ieee:4119276
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Matthieu Bloch, Joao Barros, Miguel R. D. Rodrigues +1
- **PDF**: https://ieeexplore.ieee.org/document/4119276
- **Abstract**: We present a physical layer approach aimed at providing information-theoretic security in wireless communication systems. Our secret key agreement scheme, which uses state-of-the-art error correcting codes and borrows ideas from quantum key distribution such as Gaussian reconciliation and privacy amplification, is capable of exploiting the physical properties of wireless fading channels in order to generate secret encryption keys. Focusing on the case of imperfect channel knowledge, we provide a performance analysis of the proposed security sub-system - both In theory and in practice

## Minimum Pseudo-Codewords of LDPC Codes

- **Status**: ❌
- **Reason**: LP 디코딩 pseudo-codeword 최소 weight 순수 이론 분석, 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:4119265
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Shu-Tao Xia, Fang-Wei Fu
- **PDF**: https://ieeexplore.ieee.org/document/4119265
- **Abstract**: In this paper, we study the minimum pseudo-weight and minimum pseudo-codewords of low-density parity-check (LDPC) codes under linear programming (LP) decoding. First, we show that the lower bound of Kelly, Sridhara, Xu and Rosenthal on the pseudo-weight of a pseudo-codeword of an LDPC code with girth greater than 4 is tight if and only if this pseudo-codeword is a real multiple of a codeword. Then, we show that the lower bound of Kashyap and Vardy on the stopping distance of an LDPC code is also a lower bound on the pseudo-weight of a pseudo-codeword of this LDPC code with girth 4, and this lower bound is tight if and only if this pseudo-codeword is a real multiple of a codeword. Using these results we further show that for some LDPC codes, there are no other minimum pseudo-codewords except the real multiples of minimum codewords. This means that LP decoding for these LDPC codes is asymptotically optimal in the sense that the ratio of the probabilities of decoding errors of LP decoding and maximum-likelihood (ML) decoding approaches to 1 as the signal-to-noise ratio leads to infinity. Finally, some LDPC codes are listed to illustrate these results

## Non-binary Hybrid LDPC Codes: structure, decoding and optimization

- **Status**: ❌
- **Reason**: Hybrid/non-binary LDPC (GF(q) variable nodes) - 비이진 LDPC 제외
- **ID**: ieee:4119257
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Lucile Sassatelli, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/4119257
- **Abstract**: In this paper, we propose to study and optimize a very general class of LDPC codes whose variable nodes belong to finite sets with different orders. We named this class of codes hybrid LDPC codes. Although efficient optimization techniques exist for binary LDPC codes and more recently for non-binary LDFC codes, they both exhibit drawbacks due to different reasons. Our goal is to capitalize on the advantages of both families by building codes with binary (or small finite set order) and non-binary parts of their factor graph representation. The class of hybrid LDPC codes is obviously larger than existing types of codes, which gives more degrees of freedom to find good codes where the existing codes show their limits. We gave two examples where hybrid LDPC codes show their interest

## Application of the Low Density Parity-Check Codes in the MBC System

- **Status**: ❌
- **Reason**: MBC(meteor burst) 무선 시스템에 표준 LDPC 적용, 새 디코더/구성 기여 없는 응용
- **ID**: ieee:4119269
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Rong Sun, Jingwei Liu, Arika Fukuda +2
- **PDF**: https://ieeexplore.ieee.org/document/4119269
- **Abstract**: Different channel coding schemes, such as the merely CRC scheme and the FEC coding scheme and so on, used in MBC system are described mainly. The utilization of low density parity-check (LDPC) coding scheme in the MBC system is analyzed and explained detailedly, and some criteria are presented. It is proved that the use of LDPC codes in MBC system can simplify the system structure and improve the system performance because the LDPC codes have both the superior error correcting ability and the good error detecting ability. Considering the SNR-time-varying property of the underdense MBC channel, the irregular short-length LDPC codes used in MBC system are proposed and better performance is obtained

## Error Exponents of Low-Density Parity-Check Codes on the Binary Erasure Channel

- **Status**: ❌
- **Reason**: BEC error exponent 순수 이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4119259
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Thierry Mora, Olivier Rivoire
- **PDF**: https://ieeexplore.ieee.org/document/4119259
- **Abstract**: We introduce a thermodynamic (large deviation) formalism for computing error exponents in error-correcting codes. Within this framework, we apply the heuristic cavity method from statistical mechanics to derive the average and typical error exponents of low-density parity-check (LDPC) codes on the binary erasure channel (BEC) under maximum-likelihood decoding.

## Non-binary adaptive LDPC codes for frequency selective channels: code construction and iterative decoding

- **Status**: ❌
- **Reason**: multi-Galois 비이진 LDPC 코드 — 비이진(GF(q)) LDPC 제외 대상
- **ID**: ieee:4119282
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Joseph J. Boutros, Alaa Ghaith, Yi Yuan-Wu
- **PDF**: https://ieeexplore.ieee.org/document/4119282
- **Abstract**: We propose a new type of non-binary LDPC codes defined over multiple Galois fields. The so called multi-Galois LDPC code can adapt to the profile of a frequency selective channel and is suitable for multi-carrier transmissions with quadrature amplitude modulations

## A Modified Iterative Joint Source-Channel Decoding Algorithm Based on LDPC Codes and HMMs

- **Status**: ❌
- **Reason**: LDPC+HMM 결합 소스-채널 디코딩(JSCD), Rayleigh 페이딩 — LDPC가 베이스라인, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:4119321
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Rongke Liu, Jie Gao, Xiaolin Zhang
- **PDF**: https://ieeexplore.ieee.org/document/4119321
- **Abstract**: A modified joint source-channel decoding (JSCD) algorithm based on low-density parity-check (LDPC) codes and hidden Markov estimation has been presented and extended to applying over Rayleigh fading channels. The proposed algorithm utilizes the source residual redundancy lack of any priori information of the source parameters, and the modifications employ the self-checking and convergence mechanisms of LDPC codes in adjusting the error probability of the hidden Markov model (HMM). To show the validation of the proposed JSCD methods, we also give a framework for the density evolution analysis for JSCD. Simulation results show that the joint decoding scheme on Rayleigh fading channels greatly reduces the number of iterations and improves the system performance more than 0.7 dB. Moreover, the modified JSCD algorithm leads to the joint decoder to converge at least 10% faster than the unmodified method without any degradation in the decoding performance

## Comparison of Concatenated Reed-Solomon Coding with Hard-decision to Soft-decision LDPC Coding for the Rayleigh Fading Channel

- **Status**: ❌
- **Reason**: RS+BCH 경판정 vs LDPC 연판정 성능 비교; 비-LDPC 부호 중심이라 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:4119271
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: J. Cai, M. Tomlinson, C. Tjhai +2
- **PDF**: https://ieeexplore.ieee.org/document/4119271
- **Abstract**: Reed-Solomon (RS) codes C(n, k, n - k + 1) are commonly used error-control codes, because they are Maximum Distance Separable (MDS) codes. Over a Binary Erasure Channel, RS codes perform with optimal results and approach the maximum channel capacity. In this paper, we apply RS codes to packet wireless transmission over the uncorrelated flat Rayleigh fading channel. It is shown that by using an RS code concatenated with BCH codes and using hard decisions, better results are obtained than using bit interleaved LDPC codes, with soft-decision decoding. The BCH code is used to correct small numbers of errors due to noise and also to detect the presence of deep fades, in which case the entire packet is erased. Erased packets are corrected by the RS code. We also discuss the effect of overall code rate on the net performance.

## A Parallel Iterative Acquisition Algorithm for Multiple PN Codes

- **Status**: ❌
- **Reason**: 다중 PN 코드 병렬 획득용 factor graph/sum-product — 동기화 응용, 떼어낼 채널 디코더 기법 없음
- **ID**: ieee:4119359
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Zhisong Bie, Kai Niu, Weiling Wu
- **PDF**: https://ieeexplore.ieee.org/document/4119359
- **Abstract**: Based on factor graph and sum-product algorithm, an iterative acquisition algorithm for multiple PN codes is proposed. This algorithm combines the BP decoding algorithm and the chip level MUD as an iterative loop to fulfil the task of parallel acquisition for multiple PN codes. Simulation and analysis results show that the performance of this algorithm is slightly poorer than the full parallel search method, but the computational costs are decreased dramatically

## Stopping Set Distributions of Some Linear Codes

- **Status**: ❌
- **Reason**: Hamming/simplex/RM 등 선형부호 stopping set 분포 이론, 비-LDPC, 떼어낼 디코더 기법 없음
- **ID**: ieee:4119252
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Shu-Tao Xia, Fang-Wei Fu
- **PDF**: https://ieeexplore.ieee.org/document/4119252
- **Abstract**: In this paper, the stopping set distributions (SSD) of some well-known binary linear codes are determined by using finite geometry theory. Similar to the weight distribution of a binary linear code, the SSD {Ti(H)}n i=0 enumerates the number of stopping sets with size i of a linear code with parity-check matrix H. First, we deal with the simplex codes and Hamming codes. With parity-check matrix formed by all the weight 3 codewords of the Hamming code, the SSD of the simplex code is completely determined with explicit formula. With parity-check matrix formed by all the nonzero codewords of the simplex code, the SSD of the Hamming code is completely determined with two recursive equations. Then, the first order Reed-Muller codes and the extended Hamming codes are discussed. With parity-check matrix formed by all the weight 4 codewords of the extended Hamming code, the SSD of the first order Reed-Muller code is completely determined with explicit formula. With parity-check matrix formed by all the minimum codewords of the first order Reed-Muller code, the SSD of the extended Hamming code is completely determined with two recursive equations

## An Introduction to Tensor Product Codes and Applications to Digital Storage Systems

- **Status**: ❌
- **Reason**: tensor product 부호 리뷰, 비-LDPC 구성 부호 조합, 신규 LDPC 디코더/구성 기여 없음
- **ID**: ieee:4119243
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Jack Keil Wolf
- **PDF**: https://ieeexplore.ieee.org/document/4119243
- **Abstract**: Tensor product (TP) codes result from combining two constituent error control codes in a particular manner. Depending upon the types of constituent codes used, the resulting codes can be error detection codes, error correction codes, error location codes, or some combination thereof. In this paper a review of these codes will be given and possible applications to digital storage systems will be discussed

## An Efficient Iterative Synchronization Scheme for LDPC-Coded DS-SS Systems Using two Samples per Chip

- **Status**: ❌
- **Reason**: LDPC-coded DS-SS 동기화(타이밍/위상 복구) — 무선 동기화 기법, LDPC는 부수, 떼어낼 ECC 기법 없음
- **ID**: ieee:4119352
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Liu An, Luo Wu
- **PDF**: https://ieeexplore.ieee.org/document/4119352
- **Abstract**: In this paper, an efficient iterative timing and carrier phase recovery scheme is proposed for LDPC-coded direct sequence spread spectrum (DS-SS) systems. The received signal after the chip-matched filter is two times over sampled per chip. The characteristics of DS-SS signal and LDPC decoder are explored to make the synchronization scheme efficient and simple in such a low sampling ratio. Three sets of correlation values provided by three correlators with different timing offsets are stored to estimate timing and carrier phase. The estimation is performed once per decoding iteration based on the maximum likelihood theory aided by hard decision obtained from LDPC decoder. The overall complexity of this scheme is very low and the performance of the proposed scheme approaches that with the ideal synchronization on AWGN channels

## Non-Coherent LDPC Decoding on Graphs

- **Status**: ❌
- **Reason**: non-coherent 검출 특화 디코딩, 무선 응용 특이적이며 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4119268
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Ansgar Scherb, Karl-Dirk Kammeyer
- **PDF**: https://ieeexplore.ieee.org/document/4119268
- **Abstract**: Within this paper graph based non-coherent decoding algorithms for LDPC encoded systems are proposed. We study a class of LDPC codes suitable for non-coherent detection. On the basis of the related graphs a non-coherent decoding algorithm with variable trade-off between computational complexity and BER performance is derived. The proposed scheme is also capable to deal with pilot symbols if available. Finally, the excellent performance of the proposed methods is verified by simulations

## Fast Min-Sum Algorithms for Decoding of LDPC over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC min-sum 디코딩 - 비이진 LDPC 제외
- **ID**: ieee:4119262
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Xiaofei Huang, Suquan Ding, Zhixing Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/4119262
- **Abstract**: In this paper, we present a fast min-sum algorithm for decoding LDPC codes over GF(q). Our algorithm is different from the one presented by David Declercq and Marc Fossorier (2005) only at the way of speeding up the horizontal scan in the min-sum algorithm. The Declercq and Fossorier's algorithm speeds up the computation by reducing the number of configurations, while our algorithm uses the dynamic programming instead. Compared with the configuration reduction algorithm, the dynamic programming one is simpler at the design stage because it has less parameters to tune. Furthermore, it does not have the performance degradation problem caused by the configuration reduction because it searches the whole configuration space efficiently through dynamic programming. Both algorithms have the same level of complexity and use simple operations which are suitable for hardware implementations

## On Decoding Failure Probabilities for Linear Block Codes on the Binary Erasure Channel

- **Status**: ❌
- **Reason**: BEC stopping set/디코딩 실패확률 순수 이론 분석, 디코더/HW/구성 산출물 없음
- **ID**: ieee:4119247
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Jos H. Weber, Khaled A.S. Abdel-Ghaffar
- **PDF**: https://ieeexplore.ieee.org/document/4119247
- **Abstract**: It has been claimed that the performance of a linear block code under iterative decoding on the binary erasure channel is determined by the stopping distance, i.e., the size of the smallest non-empty stopping set in the associated Tanner graph. Indeed, this is true from the perspective of code word retrieval. However, we show that with respect to the retrieval of just the information bits within the code word, the stopping distance may not be the main performance indicator since the smallest non-empty stopping sets might not hit the information set. We present expressions for decoding failure probabilities for code/information words/bits under optimal or iterative decoding and demonstrate the importance of the choice of the set of bits carrying the information for a fixed code with a fixed decoder

## On the Bhattacharyya Rate for BISOM Channels and Its Code Threshold

- **Status**: ❌
- **Reason**: BISOM 채널의 Bhattacharyya rate 코드 임계값 — 순수 이론 bound, 떼어낼 디코더/HW/구성 없음
- **ID**: ieee:4119290
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Ruoheng Liu, Predrag Spasojevic
- **PDF**: https://ieeexplore.ieee.org/document/4119290
- **Abstract**: In this paper, we study the properties of the Bhattacharyya noise parameter γ for binary-input symmetric-output memoryless (BISOM) channels. A channel quality measure Bhattacharyya rate ß ≜ 1 - γ is shown to be, for an arbitrary BISOM channel, between the cutoff rate R and the channel capacity C, i.e., R0 ≤ ß ≤ C. Based on this relationship and the modified Shulman-Feder bound, a Bhattacharyya rate code threshold is proposed. We show that the derived code threshold is tighter than the corresponding threshold due to Jin and McEliece.

## Bidirectional Viterbi Decoding using the Levenshtein Distance Metric for Deletion Channels

- **Status**: ❌
- **Reason**: deletion 채널용 양방향 Viterbi 디코딩(컨볼루션 부호) — 비-LDPC, 부호 비의존적 BP 이식 기법 아님
- **ID**: ieee:4119296
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Ling Cheng, Hendrik C. Ferreira, Theo G. Swart
- **PDF**: https://ieeexplore.ieee.org/document/4119296
- **Abstract**: In this paper, we present a bidirectional Viterbi decoding algorithm using the Levenshtein distance metric for a regular convolutional encoding system. For a deletion channel, this decoding algorithm can correct an average of 30 deletion errors within a 6000 bit frame, when using an r = 0.67 regular convolutional code; and it can correct an average of 80 deletion errors within a 4000 bit frame, when using an r = 0.25 regular convolutional code

## Efficiency of Precode-Only Raptor codes and Turbo-Fountain Codes

- **Status**: ❌
- **Reason**: precode-only Raptor/turbo-fountain 부호 효율 분석, fountain 비-LDPC, 떼어낼 기법 없음
- **ID**: ieee:4119255
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Alberto Tarable, Sergio Benedetto
- **PDF**: https://ieeexplore.ieee.org/document/4119255
- **Abstract**: This paper deals with precode-only (PCO) Raptor and turbo fountain codes used on a noiseless channel, as it is the case for the BEC or the AWGN channel with high SNR. We find an expression for the performance of an ML-decoded PCO Raptor code. The performance parameter is the inefficiency of the code, i.e., the average amount of redundancy needed to decode the information bits. The inefficiency is expressed in terms of a generalized weight enumerating function. Also, we characterize the behavior of the Shannon ensemble in the same conditions. Finally, we extend the analysis to turbo fountain codes, which are iteratively decoded. We obtain an upper bound to the turbo code inefficiency when the deterministic interleaver is replaced by a uniform interleaver

## Raptor Codes with Fast Hard Decision Decoding Algorithms

- **Status**: ❌
- **Reason**: Raptor(fountain) 부호 hard-decision 디코딩, fountain/erasure 비-LDPC, 떼어낼 ECC 기법 없음
- **ID**: ieee:4119254
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Soheil Mohajer, Amin Shokrollahi
- **PDF**: https://ieeexplore.ieee.org/document/4119254
- **Abstract**: In this paper we will investigate the performance of Raptor codes using Gallager's majority decoding algorithm on the binary symmetric channels. We obtain equations which relate the error probability to the outputnode degree distribution and then we design good degree distributions using the differential evolution (DE) method

## New Recursive Space-Time Trellis Codes From General Differential Encoding

- **Status**: ❌
- **Reason**: 차분 부호화 기반 재귀 space-time trellis 코드 — 비-LDPC 무선 부호 설계, 이식 기법 없음
- **ID**: ieee:4119370
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Shengli Fu, Haiquan Wang, Xiang-Gen Xia
- **PDF**: https://ieeexplore.ieee.org/document/4119370
- **Abstract**: In this paper, a recursive space-time trellis coding (RSTTC) from general differential encoding is proposed for multiple antenna systems, where general differential encoding is implemented separately from the space-time matrix modulation. The general differential encoding is achieved by introducing a new multiplication on a set of symbols (called trellis codewords) such that the corresponding RSTTC has its minimum error event length 3 or above and in the meantime it has the minimum number of states. The space-time matrix modulation is the mapping of the differentially encoded symbols to a set of space-time matrices (called modulation codewords). Due to the separation of differential encoding and space-time matrix modulation, more freedom on the design of modulation codewords (or a space-time code) exists, which may result in a larger diversity product (or determinant distance or product distance or coding advantage) than that the existing combined differential encoding and space-time matrix modulation can achieve in the concatenation with an outer binary channel encoder proposed by Schlegel and Grant. A new design of modulation codewords is then proposed for the RSTTC with larger diversity products than the existing schemes. Simulation results are finally presented to show that our new design significantly outperforms the existing schemes

## Gallager Bounds for Space-Time Codes in Quasi-Static Fading Channels

- **Status**: ❌
- **Reason**: space-time 코드의 Gallager bound — 순수 이론 bound, 무선 특이, 디코더/HW 없음
- **ID**: ieee:4119340
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Cong Ling
- **PDF**: https://ieeexplore.ieee.org/document/4119340
- **Abstract**: Gallager's bounding techniques are employed to derive tight upper bounds on the decoding error probability of space-time codes in quasi-static Rayleigh fading channels. The bounds converge rapidly and are within a few decibels from simulation results. Moreover, they permit efficient numerical computation, which represents a major advantage over the existing limit-before-average technique. Therefore, the proposed bounds are a meaningful and practical tool for performance analysis and computer search of good space-time codes

## On Reduced Complexity Decoding Algorithms for STBC-MTCM in Fast Fading Channels

- **Status**: ❌
- **Reason**: STBC-MTCM 페이딩 채널용 ZF/LMMSE 검출기 — 비-LDPC, 무선 MIMO 특이, 이식 기법 없음
- **ID**: ieee:4119339
- **Type**: conference
- **Published**: 22-26 Oct.
- **Authors**: Daniel N. Liu, Michael P. Fitz
- **PDF**: https://ieeexplore.ieee.org/document/4119339
- **Abstract**: STBC-MTCM scheme which achieves high rate, full diversity and large coding gains is an outstanding example of transmit diversity scheme for multiple-antenna system. In the case of time selective fast fading (TSFF) or frequency selective fading (FSF) channels, the performance of current existing STBC-MTCM decoder suffers from an irreducible error floor. In this paper, we present two computational efficient decoding algorithms: zero-forcing (ZF) detector and linear minimum mean square error (LMMSE) detector to combat the fast fading channels. The proposed decoding algorithms provide a robust performance across range of channel conditions from quasi-static (slow) fading to TSFF or FSF. Simulation results suggest that our proposed decoding algorithms have near maximum-likelihood (ML) performance while being computational more efficient

## On the Effects of Colored Noise on the Performance of LDPC Codes

- **Status**: ❌
- **Reason**: Performance evaluation of LDPC under colored noise; no new decoder/HW/code-design technique to port
- **ID**: ieee:4161856
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Saeed Sharifi Tehrani, Bruce F. Cockburn, Stephen Bates
- **PDF**: https://ieeexplore.ieee.org/document/4161856
- **Abstract**: The class of low-density parity-check (LDPC) codes includes some of the most powerful capacity-approaching codes reported to date. As a result, LDPC codes have been considered for many new communication applications. However, a better understanding of the effects of the signal impairments that exist in such applications is required. In this paper, the performance of various LDPC codes, including recent candidate LDPC codes for 10GBASE-T Ethernet, in the presence of colored noise is evaluated and compared with the effects of conventional additive white Gaussian noise (AWGN). The colored noise models in this study include high-frequency and low-frequency additive colored Gaussian noise (ACGN), and 1/f noise. The results show that LDPC codes are more vulnerable to colored noise than to AWGN and as the correlation between noise samples becomes stronger, their performance becomes more degraded. However, at the same level of colored noise power, the performance is increasingly degraded as noise correlation is spread over more noise samples

## A Reconfigurable Applcation Specific Instruction Set Processor for Viterbi and Log-MAP Decoding

- **Status**: ❌
- **Reason**: Viterbi/Log-MAP ASIP for convolutional/turbo codes; non-LDPC, decoder tied to trellis codes, no LDPC BP-portable technique
- **ID**: ieee:4161840
- **Type**: conference
- **Published**: 2-4 Oct. 2
- **Authors**: Timo Vogt, Norbert Wehn
- **PDF**: https://ieeexplore.ieee.org/document/4161840
- **Abstract**: Future mobile and wireless communications networks require flexible modem architectures with high performance. This paper presents a dynamically reconfigurable application specific instruction set processor (dr-ASIP) for the application domain of channel coding in wireless communications systems: FlexiTreP. It features Viterbi and Log-MAP decoding for support of binary convolutional codes and binary as well as duobinary turbo codes. The FlexiTreP can support more than 10 current wireless communication standards. Furthermore, its flexibility allows for adaptation to future systems. It consists of a specialized pipeline and a dedicated communication and memory infrastructure. Simulation and synthesis results obtained for Log-MAP and Viterbi applications demonstrate maximum throughput of 200 and 133 Mbps, respectively

## Biometric Image Authentication using Watermarking

- **Status**: ❌
- **Reason**: 바이오메트릭 이미지 워터마킹/인증(CRC·해시), LDPC ECC와 무관
- **ID**: ieee:4108459
- **Type**: conference
- **Published**: 18-21 Oct.
- **Authors**: Hyobin Lee, Jaehyuck Lim, Sunjin Yu +2
- **PDF**: https://ieeexplore.ieee.org/document/4108459
- **Abstract**: In this paper, we propose an invertible authentication watermarking algorithm which can detect block-wise malicious manipulations in biometric images. Our method uses an invertible watermark that can also detect manipulated area simultaneously. Virtually all watermarking schemes introduce a small amount of irrecoverable distortion in original biometric images. But our new method is invertible in the sense that, if the data is deemed authentic, distortion due to authentication can be removed if it becomes necessary to obtain the original biometric image. In our method two watermarks are embedded into biometric image. The first one is based on the conventional method which can completely remove the distortion due to authentication if the data is deemed authentic. The second one can detect the block-wise malicious manipulation using the cyclic redundancy check (CRC) concept in the image block. Our proposed method can classify a test image into two types; authentic, and manipulated. Also, this technique provides cryptographic strength when verifying image integrity because the probability of making an undetectable modification to the image can be directly related to a secure cryptographic element, such as a hash function

## Noise Correlation-Aided Iterative Decoding for Magnetic Recording Channels

- **Status**: ❌
- **Reason**: 자기기록 채널 노이즈상관 BCJR/Viterbi 검출, turbo 기반-LDPC 비의존 검출기법
- **ID**: ieee:4141341
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Pisit Vanichchanunt, Kampol Woradit, Suvit Nakpeerayuth +2
- **PDF**: https://ieeexplore.ieee.org/document/4141341
- **Abstract**: In this paper, three noise correlation-aided iterative decoding schemes are proposed for magnetic recording channels, where the correlation is imposed by the equalizer's spectral shaping effect. The first approach exploits the noise' correlation in the form of linear prediction-aided detection by increasing the number of detector trellis states invoked by the Bahl, Cocke, Jelinek, and Raviv (BCJR) detection algorithm. In the second approach, we have extended the first technique by employing both previous and future correlated noise samples in order to attain noise estimates. In order to achieve this objective, the classic BCJR algorithm has to be modified for the sake of additionally exploiting future noise samples. The third approach is designed for reducing the decoding complexity by applying the Viterbi algorithm (VA) to assist the detector in finding the encoded sequences associated with the survivor paths in the detector's trellis, without increasing the number of trellis states. We will demonstrate that for the classic PR4-equalized Lorentzian channel, the proposed schemes are capable of offering a performance gain in the range of 1.1-3.7 dB over that of a benchmark turbo decoding system at the BER of 10-5 and at a recording density of 2.86

## Performance analysis of the detector for structured irregular LDPC coded MIMO-OFDM system

- **Status**: ❌
- **Reason**: LDPC-MIMO-OFDM 검출기 EXIT 분석, 무선 검출 응용 특이적, LDPC 디코더 신규기여 없음
- **ID**: ieee:1615136
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Kyeong Jin Kim, T. Bhatt, V. Stolpman +1
- **PDF**: https://ieeexplore.ieee.org/document/1615136
- **Abstract**: In this paper, we evaluate the performance of the MIMO data detector with various decoding architectures in the structured irregular LDPC coded MIMO-OFDM system. Using the EXIT chart analysis, the performance of the data detector in the iterative MIMO-OFDM system with various approximate decoding algorithms is analyzed.

## On the Usage of Quasi-Cyclic Low-Density Parity-Check Codes in the McEliece Cryptosystem

- **Status**: ❌
- **Reason**: QC-LDPC를 McEliece 암호시스템에 적용; 보안 응용, 표준 부호 사용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:4156475
- **Type**: conference
- **Published**: 10-11 Oct.
- **Authors**: Marco Baldi, Franco Chiaraluce, Roberto Garello
- **PDF**: https://ieeexplore.ieee.org/document/4156475
- **Abstract**: We consider possible inclusion of quasi-cyclic low-density parity-check codes in the McEliece cryptosystem, in order to verify the joined security/error control action that this scheme can potentially achieve. As the linearity of the transformation from the private key to the public key exposes the system to the risk of a total break attack, suitable conditions tailored for this class of codes are presented and discussed.

## Applications of Integrated Interleaving BC scheme and High Dimensional Parity Codes with High Code Rates to PR Channels

- **Status**: ❌
- **Reason**: 고차원 패리티검사 코드+integrated interleaving (비-LDPC 부호); 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:4156459
- **Type**: conference
- **Published**: 10-11 Oct.
- **Authors**: Hiroshi Kamabe, Tomoyuki Kado
- **PDF**: https://ieeexplore.ieee.org/document/4156459
- **Abstract**: In signal processing for high density magnetic recording systems, it is important to combine a signal detection method and an error correction scheme. Error correcting codes for magnetic recording channels are required to be easily implemented and to have high code rates. High dimensional parity check codes with high code rates satisfy these requirements. We show the error correcting performance of the high dimensional parity check codes with high code rates when we apply them to PR channels. We also show that the integrated interleaving ECC technique is useful for a PR channel.
