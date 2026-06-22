# IEEE Xplore — 2014-06


## Low-Complexity Encoding of Quasi-Cyclic Codes Based on Galois Fourier Transform

- **Status**: ❌
- **Reason**: Galois Fourier transform 기반 QC 부호 인코딩 — 비이진/GF, RS-LDPC 인코더로 바이너리 LDPC ECC 이식 기법 아님
- **ID**: ieee:6784391
- **Type**: journal
- **Published**: June 2014
- **Authors**: Qin Huang, Li Tang, Shanbao He +2
- **PDF**: https://ieeexplore.ieee.org/document/6784391
- **Abstract**: This paper presents two novel low-complexity encoding algorithms for quasi-cyclic (QC) codes based on Galois Fourier transform. The key idea behind them is making use of the block diagonal structure of the transformed generator matrix. The first one, named encoding by Galois Fourier transform, is equivalent to the fast implementations of the traditional encoding by Galois Fourier transform. The second one, named encoding in the transform domain (ETD), requires much less computational complexity for encoding binary QC codes. It skips the first step of the first algorithm and applies post-processing to save a large number of Galois field multiplications. Its application to QC-LDPC codes is also studied in this paper. Particularly, the hardware cost of the ETD for RS-based LDPC codes can be greatly reduced by short linear-feedback shift registers.

## On Optimum Decoding of Certain Product Codes

- **Status**: ❌
- **Reason**: product code(SPC+선형블록) MAP 디코딩 — 비-LDPC, BP 이식 기법 아님
- **ID**: ieee:6784127
- **Type**: journal
- **Published**: June 2014
- **Authors**: Gianluigi Liva, Enrico Paolini, Marco Chiani
- **PDF**: https://ieeexplore.ieee.org/document/6784127
- **Abstract**: Optimum decoding of a class of product codes is investigated. The class is the one given by the serial concatenation of a binary single-parity-check code with a low-dimension binary linear block code. It was proved by Wolf that maximum likelihood decoding for this class of product codes can be efficiently performed through the Viterbi algorithm over a compact trellis representation of the code. In this letter, it is showed that the decoding complexity can be further reduced by formulating the decoding problem as a symbol-wise maximum-a-posteriori decision problem. Results illustrated for suitably designed codes show that the proposed algorithm significantly outperforms conventional iterative decoders. Finally, a generalization of the code construction, enjoying the same low-complexity decoding principle is presented and analyzed, achieving tangible coding gains at moderate error rates.

## Nonbinary LDPC Decoder Based on Simplified Enhanced Generalized Bit-Flipping Algorithm

- **Status**: ❌
- **Reason**: GF(32) 비이진 LDPC 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6583270
- **Type**: journal
- **Published**: June 2014
- **Authors**: Francisco García-Herrero, María José Canet, Javier Valls
- **PDF**: https://ieeexplore.ieee.org/document/6583270
- **Abstract**: A simplified version of the enhanced serial generalized bit-flipping algorithm is proposed in this brief. This new algorithm reduces the quantity of information that is stored with a negligible performance loss of 0.05 dB compared with previous proposals. In addition, the algorithm allows us not only to save memory, but also to reduce the number of arithmetic resources needed. In addition, a new initialization of the algorithm avoids using techniques to control data growth without any performance degradation, reduces routing, increasing the maximum frequency achievable, and saves logic. The decoder derived from the simplified algorithm requires almost half the area of previous architectures, with a throughput of 716 Mbps on a 90-nm CMOS process for the (837, 723) nonbinary code over GF(32) at ten iterations.

## A Single-Bit and Double-Adjacent Error Correcting Parallel Decoder for Multiple-Bit Error Correcting BCH Codes

- **Status**: ❌
- **Reason**: 비-LDPC BCH 디코더(double-adjacent 정정), 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:6757028
- **Type**: journal
- **Published**: June 2014
- **Authors**: Kazuteru Namba, Salvatore Pontarelli, Marco Ottavi +1
- **PDF**: https://ieeexplore.ieee.org/document/6757028
- **Abstract**: This paper presents a novel high-speed BCH decoder that corrects double-adjacent and single-bit errors in parallel and serially corrects multiple-bit errors other than double-adjacent errors. Its operation is based on extending an existing parallel BCH decoder that can only correct single-bit errors and serially corrects double-adjacent errors at low speed. The proposed decoder is constructed by a novel design and is suitable for nanoscale memory systems, in which multiple-bit errors occur at a probability comparable to single-bit errors and double-adjacent errors occur at a higher probability (nearly two orders of magnitude) than other multiple-bit errors. Extensive simulation results are reported. Compared with the existing scheme, the area and delay time of the proposed decoder are on average 11% and 6% higher, but its power consumption is reduced by 9% on average. This paper also shows that the area, delay, and power overheads incurred by the proposed scheme are significantly lower than traditional fully parallelized BCH decoders capable of correcting any double-bit errors in parallel.

## Distributed Reception with Hard Decision Exchanges

- **Status**: ❌
- **Reason**: 분산 수신 hard decision 교환/빔포밍; LDPC는 베이스라인일 뿐, 무선 응용 특이적
- **ID**: ieee:6836138
- **Type**: journal
- **Published**: June 2014
- **Authors**: D. Richard Brown III, Upamanyu Madhow, Min Ni +2
- **PDF**: https://ieeexplore.ieee.org/document/6836138
- **Abstract**: This paper considers the problem of jointly processing messages received over a forward link from a single distant transmitter to a cooperative receive cluster connected by a local area network with finite available throughput. For N cooperating receivers, ideal distributed receive beamforming with direct exchange of unquantized observations leads to an N-fold gain in signal-to-noise ratio (SNR) for equal-gain additive white Gaussian noise channels, with significant additional gains over fading channels due to diversity. It is shown in this paper that a significant portion of these gains can be obtained simply by exchanging hard decisions among some or all of the nodes in the receive cluster. Mutual information computations and simulations of LDPC-coded systems show that optimal combining of hard decisions tends to perform within 0.5-2 dB of ideal receive beamforming. For the low per-node SNR regime of interest with large receive clusters, asymptotic analysis of a suboptimal combining technique termed "pseudo-beamforming" shows that distributed reception with hard decision exchanges performs within 1-2 dB of ideal receive beamforming.

## A Low-Complexity Decoding Algorithm for Coded Hierarchical Modulation in Single Frequency Networks

- **Status**: ❌
- **Reason**: 계층변조 SIC 디코딩(SFN); 변조/간섭제거 기법으로 LDPC BP 비의존, 떼어낼 ECC 기법 없음
- **ID**: ieee:6819042
- **Type**: journal
- **Published**: June 2014
- **Authors**: Zixia Hu, Hong Jiang, Hongxiang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/6819042
- **Abstract**: In this paper, the hierarchical modulation (HM) technique is adopted in a single frequency network (SFN) to provide both global and local information. In order to mitigate the interlayer interference and intercell interference, we develop a low-complexity successive interference cancellation (SIC) algorithm for the coded HM signals in the SFN. The proposed decoding algorithm can be applied to different soft-decision channel coding schemes (e.g., Turbo codes, LDPC codes) under various channel profiles. We analyzed the decoding complexity of the proposed algorithm, and evaluated the bit error rate performance. The simulations show that the new decoding algorithm can offer up to 0.7 dB carrier to noise ratio ((C/N)) gain compared with the traditional SIC approach under different channel models, while providing the comparable performance (up to 95% decoding complexity savings) with the multilayer iterative decoding approach. The performance evaluation and decoding complexity comparisons indicate that the proposed structured SIC approach offers a good performance-complexity trade-off, especially for the HM-based SFN scenarios.

## Group Testing Algorithms: Bounds and Simulations

- **Status**: ❌
- **Reason**: group testing 검출 알고리즘 — 채널 ECC/LDPC 디코더 아님
- **ID**: ieee:6781038
- **Type**: journal
- **Published**: June 2014
- **Authors**: Matthew Aldridge, Leonardo Baldassini, Oliver Johnson
- **PDF**: https://ieeexplore.ieee.org/document/6781038
- **Abstract**: We consider the problem of nonadaptive noiseless group testing of  $N$  items of which  $K$  are defective. We describe four detection algorithms, the  ${\tt COMP}$  algorithm of Chan et al. , two new algorithms,  ${\tt DD}$  and  ${\tt SCOMP}$ , which require stronger evidence to declare an item defective, and an essentially optimal but computationally difficult algorithm called  ${\tt SSS}$ . We consider an important class of designs for the group testing problem, namely those in which the test structure is given via a Bernoulli random process. In this class of Bernoulli designs, by considering the asymptotic rate of these algorithms, we show that  ${\tt DD}$  outperforms  ${\tt COMP}$ , that  ${\tt DD}$  is essentially optimal in regimes where  $K\geq\sqrt N$ , and that no algorithm can perform as well as the best nonrandom adaptive algorithms when  $K>N^{0.35}$ . In simulations, we see that  ${\tt DD}$  and  ${\tt SCOMP}$  far outperform  ${\tt COMP}$ , with  ${\tt SCOMP}$  very close to the optimal  ${\tt SSS}$ , especially in cases with larger  $K$ .

## DVB-NGH: The Next Generation of Digital Broadcast Services to Handheld Devices

- **Status**: ❌
- **Reason**: DVB-NGH 방송표준 리뷰; LDPC는 부수 언급, 떼어낼 신규 기법 없음
- **ID**: ieee:6812187
- **Type**: journal
- **Published**: June 2014
- **Authors**: David Gómez-Barquero, Catherine Douillard, Peter Moss +1
- **PDF**: https://ieeexplore.ieee.org/document/6812187
- **Abstract**: This paper reviews the main technical solutions adopted by the next-generation mobile broadcasting standard DVB-NGH, the handheld evolution of the second-generation digital terrestrial TV standard DVB-T2. The main new technical elements introduced with respect to DVB-T2 are: layered video coding with multiple physical layer pipes, time-frequency slicing, full support of an IP transport layer with a dedicated protocol stack, header compression mechanisms for both IP and MPEG-2 TS packets, new low-density parity check coding rates for the data path (down to 1/5), nonuniform constellations for 64 Quadrature Amplitude Modulation (QAM) and 256QAM, 4-D rotated constellations for Quadrature Phase Shift Keying (QPSK), improved time interleaving in terms of zapping time, end-to-end latency and memory consumption, improved physical layer signaling in terms of robustness, capacity and overhead, a novel distributed multiple input-single output transmit diversity scheme for single-frequency networks (SFNs), and efficient provisioning of local content in SFNs. All these technological solutions, together with the high performance of DVB-T2, make DVB-NGH a real next-generation mobile multimedia broadcasting technology. In fact, DVB-NGH can be regarded the first third-generation broadcasting system because it allows for the possibility of using multiple input-multiple output antenna schemes to overcome the Shannon limit of single antenna wireless communications. Furthermore, DVB-NGH also allows the deployment of an optional satellite component forming a hybrid terrestrial-satellite network topology to improve the coverage in rural areas where the installation of terrestrial networks could be uneconomical.

## Achieving Secure Communications over Wiretap Channels via Security Codes from Resilient Functions

- **Status**: ❌
- **Reason**: wiretap 보안 코드 생성(resilient functions) — 비-LDPC 보안, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6774840
- **Type**: journal
- **Published**: June 2014
- **Authors**: Hong Wen, Pin-Han Ho, Bin Wu
- **PDF**: https://ieeexplore.ieee.org/document/6774840
- **Abstract**: By manipulating both binary and non-binary resilient functions, a novel approach for generating security codes is introduced and their threshold probabilities are derived, which provides the security condition proof for the proposed security codes. In particular, by taking advantage of matrix general inverse algorithms the encoding method of the proposed security codes is derived and is practically implementable due to low complexity. Experiments are conducted to examine the proposed security codes and the security system over Binary Symmetric Channel (BSC).

## Cross-Layer Forward Error Correction Scheme Using Raptor and RCPC Codes for Prioritized Video Transmission Over Wireless Channels

- **Status**: ❌
- **Reason**: Raptor+RCPC UEP 비디오 전송, 비-LDPC 부호와 응용특이 GA 최적화로 이식 기법 없음
- **ID**: ieee:6719541
- **Type**: journal
- **Published**: June 2014
- **Authors**: Yeqing Wu, Sunil Kumar, Fei Hu +2
- **PDF**: https://ieeexplore.ieee.org/document/6719541
- **Abstract**: The unequal error protection (UEP) has shown promising results for transmitting video over error-prone wireless channels. In this paper, we investigate the cross-layer design of forward error correction (FEC) schemes by using the UEP Raptor codes at the application layer (AL) and UEP rate compatible punctured convolutional (RCPC) codes at physical layer (PHY) for prioritized video packets. The video packets are prioritized based on their contribution to the received video quality. A genetic algorithm (GA)-based optimization algorithm is proposed to find the optimal parameters for both Raptor and RCPC codes, to minimize the video distortion and maximize the peak signal-to-noise-ratio for the given video bit rates and channel constraints (i.e., SNR and available bandwidth). We evaluate the performance of four combinations of the UEP schemes for H.264/AVC encoded video sequences over the AWGN and Rayleigh fading channels and show the superiority of the optimized cross-layer UEP FEC scheme. For Rayleigh fading channel, the proposed cross-layer optimization uses two different time-scales at AL and PHY which allows PHY to adapt faster to the changing channel quality.

## FOBTV: Worldwide Efforts in Developing Next-Generation Broadcasting System

- **Status**: ❌
- **Reason**: 차세대 방송 시스템 이니셔티브 개관 — LDPC ECC 기법 없음
- **ID**: ieee:6778070
- **Type**: journal
- **Published**: June 2014
- **Authors**: Wenjun Zhang, Yiyan Wu, Namho Hur +2
- **PDF**: https://ieeexplore.ieee.org/document/6778070
- **Abstract**: The challenges facing the terrestrial broadcast industry are to how more efficiently and effectively use the scarce spectrum to deliver the vast amount of media data to the general public. Future of Broadcast Television Initiative (FOBTV) was founded by the broadcasters, manufacturers, network operators, standardization organizations, research institutes, and universities around the world, aiming at better solving these problems through global collaboration. Since its establishment, use cases for the future broadcast applications have been extensively collected and classified. Potential technologies applied for the summarized new application scenarios have been carefully studied and the most effective ones are highlighted. Moreover, FOBTV is trying to develop a layered model for the next-generation broadcasting system and taking great efforts toward the ultimate goal of a global harmonized terrestrial broadcasting system.

## Design and Analysis of Multi-Level Physical-Layer Network Coding for Gaussian Two-Way Relay Channels

- **Status**: ❌
- **Reason**: 양방향 중계채널 물리계층 네트워크코딩; LDPC ECC 기법 아님, 무선 응용 특이적
- **ID**: ieee:6800073
- **Type**: journal
- **Published**: June 2014
- **Authors**: Zhiyong Chen, Bin Xia, Zixia Hu +1
- **PDF**: https://ieeexplore.ieee.org/document/6800073
- **Abstract**: In this paper, we propose a multi-level physical-layer network coding (MPLNC) scheme that optimizes the relay performance for both symmetric and asymmetric traffic in a Gaussian two-way relay channel. The proposed MPLNC scheme enables each source to employ multiple linear binary codes for encoding, one per modulation level, and the relay node to decode superimposed network codewords at each modulation level. We first derive the achievable rate for the transmission of arbitrary constellations and then prove that MPLNC with multistage decoding (MPLNC/MSD) can achieve the achievable rate if binary code rates are properly chosen for both sources. Furthermore, the design criteria for the proposed MPLNC scheme is investigated, which includes the rate design rule and the labeling strategy. Moreover, we derive the error exponent and an upper bound of the overall error probability for MPLNC. Our analysis and simulation results show that MPLNC/MSD has a significant performance advantage in comparison to the existing bit-interleaved coded modulation (BICM)-based PLNC scheme.

## Towards Differential Query Services in Cost-Efficient Clouds

- **Status**: ❌
- **Reason**: 클라우드 프라이버시 정보검색 스킴, ECC·LDPC 무관
- **ID**: ieee:6515116
- **Type**: journal
- **Published**: June 2014
- **Authors**: Qin Liu, Chiu C. Tan, Jie Wu +1
- **PDF**: https://ieeexplore.ieee.org/document/6515116
- **Abstract**: Cloud computing as an emerging technology trend is expected to reshape the advances in information technology. In a cost-efficient cloud environment, a user can tolerate a certain degree of delay while retrieving information from the cloud to reduce costs. In this paper, we address two fundamental issues in such an environment: privacy and efficiency. We first review a private keyword-based file retrieval scheme that was originally proposed by Ostrovsky. Their scheme allows a user to retrieve files of interest from an untrusted server without leaking any information. The main drawback is that it will cause a heavy querying overhead incurred on the cloud and thus goes against the original intention of cost efficiency. In this paper, we present three efficient information retrieval for ranked query (EIRQ) schemes to reduce querying overhead incurred on the cloud. In EIRQ, queries are classified into multiple ranks, where a higher ranked query can retrieve a higher percentage of matched files. A user can retrieve files on demand by choosing queries of different ranks. This feature is useful when there are a large number of matched files, but the user only needs a small subset of them. Under different parameter settings, extensive evaluations have been conducted on both analytical models and on a real cloud environment, in order to examine the effectiveness of our schemes.

## Spatial-Temporal Enhancement of ACO-Based Selection Schemes for Adaptive Routing in Network-on-Chip Systems

- **Status**: ❌
- **Reason**: NoC 적응 라우팅 ACO 알고리즘, ECC 무관
- **ID**: ieee:6678514
- **Type**: journal
- **Published**: June 2014
- **Authors**: Hsien-Kai Hsin, En-Jui Chang, An-Yeu Wu
- **PDF**: https://ieeexplore.ieee.org/document/6678514
- **Abstract**: Networks-on-Chip (NoC) provides a regular and scalable design architecture for chip multi-processor (CMP) systems. The Ant Colony Optimization (ACO) is a distributed algorithm. Applying ACO to selection models of adaptive routing can improve NoC performance. Currently, ACO-based selection only uses the historical traffic information. While additional temporal and spatial information provides better approximation of network status for global load-balancing. In this paper, we first consider the temporal enhancement of congestion information. We propose the Multi-Pheromone ACO-based (MP-ACO) selection scheme which adopts the concept of Exponential Moving Average (EMA) from stock market. We implement a novel ACO system where ants lay two kinds of pheromones with different evaporation rates. The temporal pheromone variation can help to capture hidden-state dependencies of upcoming congestion status. Secondly, to acquire the spatial range of congestion information, we propose Regional-Aware ACO-based (RA-ACO) selection to record historical buffer information from routers within two-hop of distances, which helps to extend spatial pheromone coverage. Information provided by the proposed two schemes improves the system performance. Simulation results show that MP-ACO and RA-ACO with Odd-Even routing algorithm yields an improvement in saturation throughput over OBL and NoP selection by 14.38 percent and 18.64 percent, respectively. The router architectures for the proposed schemes are also implemented and analyze with small hardware overhead.

## A Study of Multitrack Joint 2-D Signal Detection Performance and Implementation Cost for Shingled Magnetic Recording

- **Status**: ❌
- **Reason**: SMR 2D 신호검출 ASIC 연구, 채널 검출기로 LDPC ECC 디코더·코드설계 기법 없음
- **ID**: ieee:6714532
- **Type**: journal
- **Published**: June 2014
- **Authors**: Ning Zheng, Kalyana Sundaram Venkataraman, Aleksandar Kavcic +1
- **PDF**: https://ieeexplore.ieee.org/document/6714532
- **Abstract**: Shingled magnetic recording is a promising option to sustain the historical areal density growth of hard disk drives while retaining conventional heads and media. Nevertheless, highly scaled shingled magnetic recording is subject to severe intertrack interference (ITI), fewer grains per channel bit and therefore lower signal-to-noise ratio (SNR). This naturally demands 2-D read channel signal processing, which has an inherently large spectrum of detection performance versus computational complexity tradeoff. By concurrently detecting multitrack readback signals from a read head array, joint 2-D signal detection can fully utilize the 2-D interference to maximize the detection performance at the penalty of the highest computational complexity. Multitrack joint 2-D detection has not been thoroughly studied from either the detection performance or silicon implementation perspective because of the justifiable concern on its practical feasibility. To fill this missing link, this paper presents a comprehensive study of multitrack joint 2-D signal detection performance and silicon implementation cost. We further present an interleaved pipelining strategy to reduce joint 2-D signal detector silicon consumption. By carrying out comprehensive simulations and application-specific integrated circuit (ASIC) design, this paper shows that multitrack joint 2-D signal detection is a practically attractive option with superior detection performance and affordable silicon cost, especially when considering projected CMOS technology scaling toward 16 nm and below.

## Decoder-Assisted Timing Synchronization in Multiuser CDMA Systems

- **Status**: ❌
- **Reason**: CDMA 다중사용자 타이밍 동기화 — 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6786051
- **Type**: journal
- **Published**: June 2014
- **Authors**: Jeewani Kodithuwakku, Nick Letzepis, Robby McKilliam +1
- **PDF**: https://ieeexplore.ieee.org/document/6786051
- **Abstract**: The problem of synchronizing weak user signals in multiuser code-division multiple access systems is addressed. We integrate timing synchronization into an iterative multiuser detection (MUD) framework for the improved synchronization performance of weak users. First, the effect of correctly detected users on the remaining undetected users is suppressed via soft parallel interference cancellation. Then, the time offset (TO) of each undetected user is estimated. To speed up the MUD, interference cancellation is performed after only a few decoder iterations of the detected users, and the TO estimator is designed taking into account the residual multiple access interference. A low-complexity non-data-aided TO estimator that estimates the TO of each undetected user separately is proposed. The proposed technique significantly improves the synchronization performance of weak users under high near-far conditions compared to the full interference case. Assuming Gaussian distributed log-likelihood ratios at the decoder outputs, we directly relate the missed detection probability of a desired user to the root-mean-squared error of the detected user's data sequences. The extrinsic information transfer chart of the decoder is used to analyze the acquisition performance of the desired user with the number of decoder iterations of the detected users. An upper bound for the missed detection probability of the proposed estimator is derived.

## Capacity-Achieving Codes for Noisy Feedback Channels: A Necessary Condition

- **Status**: ❌
- **Reason**: 피드백 채널 용량달성 필요조건, 순수 이론 bound; 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6804667
- **Type**: journal
- **Published**: June 2014
- **Authors**: Chong Li
- **PDF**: https://ieeexplore.ieee.org/document/6804667
- **Abstract**: In this letter, we consider a class of channels where feedback cannot increase the capacity (e.g., discrete memoryless channels). We derive a necessary condition, characterized by the directed information, on capacity-achieving channel codes for such a class of channels with noisy feedback. This condition implies that using feedback information is detrimental to the transmission rate and should be abandoned in the design of capacity-achieving channel codes.

## An Adaptive Mechanism for Optimal Content Download in Wireless Networks

- **Status**: ❌
- **Reason**: FLUTE 멀티캐스트 AL-FEC 레이트 적응, 응용계층 erasure FEC로 떼어낼 LDPC 기법 없음
- **ID**: ieee:6746196
- **Type**: journal
- **Published**: June 2014
- **Authors**: Ismael de Fez, Juan Carlos Guerri
- **PDF**: https://ieeexplore.ieee.org/document/6746196
- **Abstract**: This paper presents an adaptive mechanism for improving the content download in wireless environments. The solution is based on the use of the file delivery over unidirectional transport (FLUTE) protocol in multicast networks, which reduce considerably the bandwidth when there are many users interested in the same contents. Specifically, the system proposed reduces the average download time of clients within the coverage area, thus improving the Quality of Experience. To that extent, clients send periodically feedback messages to the server reporting the losses they are experiencing. With this information, the server decides which is the optimum application layer-forward error correction (AL-FEC) code rate that minimizes the average download time, taking into account the channel bandwidth, and starts sending data with that code rate. The system proposed is evaluated in various scenarios, considering different distributions of losses in the coverage area. Results show that the adaptive solution proposed is very suitable in wireless networks with limited bandwidth.

## Joint Adaptive Network–Channel Coding for Energy-Efficient Multiple-Access Relaying

- **Status**: ❌
- **Reason**: 무선 MARC 네트워크-채널 결합 코딩(JANCC); LDPC ECC 기법 아님, 떼어낼 디코더/HW 없음
- **ID**: ieee:6675040
- **Type**: journal
- **Published**: Jun 2014
- **Authors**: Pen-Shun Lu, Xiaobo Zhou, Khoirul Anwar +1
- **PDF**: https://ieeexplore.ieee.org/document/6675040
- **Abstract**: An energy-efficient orthogonal multiple-access relay channel (MARC) system is developed, where accumulator and differential detection (DD) are used at the source and relay nodes, respectively. However, the weak decoding capability of DD degrades the frame error rate (FER) performance of the orthogonal MARC system if the conventional decode-and-forward relaying strategy is applied. In this paper, a novel joint adaptive network-channel coding (JANCC) technique is proposed to support DD by making efficient use of the erroneous estimates output from DD. In the JANCC technique, the destination constructs a vector identifying the indexes of the source nodes whose information parts contain errors and sends it to the relay to request a retransmission. The relay performs network coding by taking the exclusive-or (xor)-operation only over the stored estimates specified by the identifier vector, which aims to avoid unnecessary erroneous estimates being coded. In addition, a bit-flipping probability pnc is obtained between the two sequences; one is the network-coded sequence sent from the relay, and the other is their corresponding xor-ed information sequence. The decoding algorithm of JANCC exploits probability pnc at the destination to update the log-likelihood ratio during the iterative decoding process. Hence, the information sequences received at the destination are able to be recovered, although the redundancy forwarded from the relay is generated from the erroneous estimates. Compared with the system where iterative decoding is performed at the relay, the utilization of DD significantly reduces the computational complexity, which leads to meaningful power savings with only a small loss in FER performance.

## Investigation of coded OFDM system over Rayleigh fading channel

- **Status**: ❌
- **Reason**: OFDM에서 LDPC+BCH 연접부호를 표준(ETSI EN 302 755)대로 사용 — 새 디코더/구성 없음, 무선 응용 특이적.
- **ID**: ieee:6931157
- **Type**: conference
- **Published**: 9-11 June 
- **Authors**: Maw-Yang Liu, Chien-Hsien Chiang, Chia-Fu Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/6931157
- **Abstract**: This paper presents a channel coding scheme for OFDM with 64-QAM and 256-QAM over Rayleigh channel. In our proposed scheme, the OFDM system employs three mode of IFFT with 4k, 16k, and 32k. In addition, the concatenated coding scheme of LDPC and BCH code is utilized as channel code referring to the standard from ETSI EN 302 755. Aside from the simulation, we also measure the system performance via the instrument that using DVB-T2 transmitter and receiver. Finally, the comparison and discussion of the simulation and trial measurement are demonstrated.

## Trade-off in LDPC coded MIMO systems with iterative and independent demapping

- **Status**: ❌
- **Reason**: LDPC-MIMO BICM 시스템 트레이드오프 EXIT 분석, LDPC는 베이스라인뿐
- **ID**: ieee:6873526
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Shuang Chen, Kewu Peng, Tao Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6873526
- **Abstract**: The combination of low-density parity-check (LDPC) codes and bit-interleaved coded modulation (BICM) scheme, could easily break the bound of the cut-off rate and achieve capacity-approaching performance. To overcome the independent demapping loss in BICM scheme, the iterative demapping counterpart of BICM (BICM-ID) was further proposed. In this paper, we will present a viewpoint that the performance of BICM and BICM-ID system cannot be optimized simultaneously, especially for LDPC coded multiple-input multiple-output (MIMO) systems. Furthermore, we use a Monte Carlo method to estimate the achievable SNR region of the BICM and BICM-ID system with the aid of extrinsic information transfer (EXIT) chart tool. Such joint-bound of the achievable SNR region provides a practical and effective way to evaluate existing schemes, and guides the system design in the future.

## Design of a bit interleaver for the high-order constellation DVB-T2 system

- **Status**: ❌
- **Reason**: DVB-T2 비트 인터리버 설계(변조/디먹스 결합), LDPC 부호/디코더 기여 아님
- **ID**: ieee:6873528
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Inwoong Kang, Kyu-Soon Ok, Youngmin Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/6873528
- **Abstract**: Since the DVB-T2 system provides high spectral efficiency among commercialized digital terrestrial transmission (DTT) systems, it has been considered as a prospective option for the base system of next generation DTT systems providing UHDTV service. However, when the high order modulation scheme such as 1024-QAM is employed, a bit interleaver in DVB-T2 should be newly designed. The design of a bit interleaver aims to improve the decoding performance not only by obtaining time diversity gain but also by eliminating multi-edge symbols. Although there are a few literatures about the design of a bit interleaver exploiting the multi-edge elimination, they cannot be directly applied to the bit interleaver of the DVB-T2 because they work as a group with a bit-to-cell demultiplexer. In this respect, this paper presents a bit interleaver design procedure for the high-order constellation DVB-T2 system. The proposed procedure generates bit interleavers for any modulation orders and makes it possible that a newly designed bit interleaver performs multi-edge elimination with all the LDPC code rates. Simulation results show that a newly designed bit interleaver for 1024-QAM achieves about 0.6dB SNR gain over a random interleaver under a Rayleigh fading channel.

## Analysis on two dimensional block interleaver for the cloud transmission system

- **Status**: ❌
- **Reason**: 2D 블록 인터리버 크기/복잡도 분석, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6873530
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Sunhyoung Kwon, Sung Ik Park, Yiyan Wu +4
- **PDF**: https://ieeexplore.ieee.org/document/6873530
- **Abstract**: This paper analyzes a interleaver size and its complexity of 2D block code, which consists of vertical raptor-like rate-compatible LDPC code and horizontal Reed Solomon (RS) code. An adequate size of 2D interleaver should be reasonably chosen by considering not only the performance and user satisfaction, but also the required memory size at a receiver side.

## Channel capacity distribution of Layer-Division-Multiplexing system for next generation digital broadcasting transmission

- **Status**: ❌
- **Reason**: LDM 방송 PHY 채널용량 분석, 떼어낼 LDPC 기법 없음
- **ID**: ieee:6873500
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Liang Zhang, Yiyan Wu, Wei Li +5
- **PDF**: https://ieeexplore.ieee.org/document/6873500
- **Abstract**: Cloud transmission (Cloud-Txn) with Layer-Division-Multiplexing (LDM) was proposed as a candidate Physical Layer (PHY) technology for next generation digital TV broadcasting system. This paper presents a fundamental analysis on the channel capacity allocation among the different layers of a LDM-based transmission system. The analysis reveals that, for delivering fixed and mobile TV services in the same RF channel, by controlling the power allocation among the layers, the LDM-based system provides much better efficient usage of the spectrum as compared to the single-layer Time-Division-Multiplexing (TDM) or Frequency-Division-Multiplexing (FDM)-based systems. The spectrum efficiency of LDM allows the simultaneous delivery of a high-data-rate UHDTV service and a mobile HDTV service within a single 6 MHz channel.

## Improvements to APSK constellation with gray mapping

- **Status**: ❌
- **Reason**: APSK 그레이매핑 변조 개선만, LDPC 디코더/HW/코드설계 기여 없음
- **ID**: ieee:6873488
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Dazhi He, Yijun Shi, Yunfeng Guan +4
- **PDF**: https://ieeexplore.ieee.org/document/6873488
- **Abstract**: Amplitude phase shift keying (APSK) constellation with gray mapping proposed in [2] provides considerable shaping gain compared with quadrature amplitude modulation (QAM). In this paper, some improvements to APSK Constellation with gray mapping are addressed. AP-SK constellation with gray mapping could be adjusted according to different SNR levels to increase its average mutual information (AMI). Two methods to improve AMI, on phase and on amplitude, are proposed. Both AMI of coded modulation (CM-AMI) and AMI of bit-interleaved coded modulation (BICM-AMI) are considered. The improvements are verified by bit error rate simulations in both independent and iterative demapping scenarios.

## Field trials based validation of the suitable configuration parameters for mobile urban reception, using the new generation broadcasting systems

- **Status**: ❌
- **Reason**: OFDM 구성 현장시험 커버리지 비교, LDPC 기법 없음
- **ID**: ieee:6873507
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: I. Fernandez, I. Eizmendi, J. Montalban +5
- **PDF**: https://ieeexplore.ieee.org/document/6873507
- **Abstract**: This paper presents a field trials based comparison between different OFDM configuration parameters (FFT and code rates) in order to determine the best choices in a trade-off between capacity and coverage in mobile urban environments. The field trials have been carried out using the Cloud Transmission broadcasting system and the main purpose has been to compare the coverage obtained for each OFDM configuration. The results provide reference values that can be used for planning purposes in this kind of scenarios.

## When do rotated constellations provide gains?

- **Status**: ❌
- **Reason**: 회전 성상도 변조 이득 가이드라인, LDPC 기법 없음
- **ID**: ieee:6873556
- **Type**: conference
- **Published**: 25-27 June
- **Authors**: Marco Breiling, Jan Zöllner, Jörg Robert
- **PDF**: https://ieeexplore.ieee.org/document/6873556
- **Abstract**: This paper aims at providing guidelines to network operators and device manufacturers, for which scenarios (e.g. target spectral efficiencies and propagation channels) rotated constellations are able to provide gains over conventional (non-rotated) constellations.

## A soft-input/soft-output dequantizer for cloud-based mobile networks

- **Status**: ❌
- **Reason**: 클라우드 모바일망 fronthaul용 soft 디퀀타이저(소스/양자화 영역), 채널 ECC 디코더 아님
- **ID**: ieee:6941808
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Jens Bartelt, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/6941808
- **Abstract**: The use of soft information instead of hard bits has been widely adapted in signal processing for digital communication to improve the reliability of data transmission by techniques like turbo equalization, turbo decoding, or LDPC codes. For future mobile networks employing a centralized architecture in which the antenna and the baseband processing are separated by an additional fronthaul channel that forwards digitalized samples, we have identified another process that can be redesigned to embrace the concept of soft information: the dequantizer. A dequantizer transforms a vector of bits into amplitudes representing digitalized samples. However, if the bits were transmitted through a lossy fronthaul channel, the soft information that can be extracted from this channel's detection process is lost in a classical dequantizer. In this work, we propose a soft-input/soft-output dequantizer that passes this information through to the subsequent signal processing steps and can thereby improve the overall reliability of centralized, cloud-based mobile networks.

## Modulation and Coding Classification for Adaptive Power Control in 5G Cognitive Communications

- **Status**: ❌
- **Reason**: 5G 인지통신 적응전력제어/변조분류, LDPC는 부수 언급(code syndrome LLR)뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:6941505
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Anestis Tsakmalis, Symeon Chatzinotas, Björn Ottersten
- **PDF**: https://ieeexplore.ieee.org/document/6941505
- **Abstract**: A key concept suggested for 5G networks is spectrum sharing within the context of Cognitive Communications (CC). This efficient spectrum usage has been explored intensively the last years. In this paper, a mechanism is proposed to allow a cognitive user, also called Secondary User (SU), to access the frequency band of a Primary User (PU) operating based on an Adaptive Coding and Modulation (ACM) protocol. The Spectrum Sensing (SS) technique used considers Higher Order Statistical (HOS) features of the signal and log-likelihood ratios (LLRs) of the code syndromes in order to constantly monitor the modulation and coding scheme (MODCOD) of the PU respectively. Once the Modulation and Coding Classification (MCC) is completed, a Power Control (PC) scheme is enabled. The SU can attempt to access the frequency band of the PU and increase its transmitting power until it causes a change of the PU's transmission scheme due to interference. When the SU detects the change of the PU's MODCOD, then it reduces its transmitting power to a lower level so as to regulate the induced interference. The proposed blind Adaptive Power Control (APC) algorithm converges without any interference channel information to the aforementioned interference limit and guarantees the preservation of the PU link throughput.

## Optimization of BICM mutual information and bit error rate of 8-ary signal constellations using genetic algorithms

- **Status**: ❌
- **Reason**: 유전알고리즘으로 8-ary 신호 성상도(constellation) 최적화—변조/성상 설계, LDPC ECC 무관
- **ID**: ieee:6941465
- **Type**: conference
- **Published**: 22-25 June
- **Authors**: Benjamin Müller, Bjöm Zessack, Udo Zölzer
- **PDF**: https://ieeexplore.ieee.org/document/6941465
- **Abstract**: We propose the use of genetic algorithms for optimizing 8-ary signal constellations. The constellations are either optimized for a high bit interleaved coded modulation (BICM) mutual information or a low bit error rate (BER) in the additive white Gaussian noise channel (AWGN). We obtained a constellation that outperforms the 8-cross by 0.25 dB for a BICM mutual information of 2 bit/symbol. The optimized constellation for a low bit error rate requires a 0.4 dB lower SNR compared to the 8-cross for a BER of 10−3.

## Synthesis of signal-code sequence for OFDM in the channel with permanent parameters

- **Status**: ❌
- **Reason**: OFDM 신호-코드 시퀀스 합성, 무선 응용 특이적이며 떼어낼 LDPC 디코더/HW/구성 기법 없음
- **ID**: ieee:6869228
- **Type**: conference
- **Published**: 16-18 June
- **Authors**: Leonid Uryvsky, Serhii Osypchuk
- **PDF**: https://ieeexplore.ieee.org/document/6869228
- **Abstract**: The signal-code sequence (SCS) synthesis method for OFDM (orthogonal frequency division multiplexing) subcarriers is presented for achievement the required bit error rate (BER) on the receiver side in the channel with permanent parameters. The method is proposed as an alternative against the single carrier (SC) transmission and for achievement the required BER.

## Joint blind frame synchronization and encoder identification for LDPC codes

- **Status**: ❌
- **Reason**: 바이너리 LDPC 블라인드 프레임 동기·인코더 식별로 ECC 디코더·HW·코드설계 기여 아님
- **ID**: ieee:6884150
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Tian Xia, Hsiao-Chun Wu, Shih Yu Chang
- **PDF**: https://ieeexplore.ieee.org/document/6884150
- **Abstract**: In this paper, we would like to tackle joint blind frame synchronization and encoder identification of binary low-density parity-check (LDPC) codes for binary phase-shift keying (BPSK) signals. The unknown encoder and the unknown time-delay can be blindly estimated at the same time using the average log-likelihood ratios (LLRs) of syndrome a posteriori probability (APP). To reduce the complexity of the blind frame synchronization, we propose a two-stage search method with a search step-size q by exploiting the quasi-cyclic property of the parity-check matrix. Our proposed new joint scheme is evaluated by the probability of detection resulting from numerous Monte Carlo simulations. The simulation results demonstrate the effectiveness of our proposed joint blind frame-synchronization and encoder-identification scheme for multi-path situations.

## Joint decoding of multiple non-binary LDPC codewords

- **Status**: ❌
- **Reason**: non-binary q-ary LDPC 다중 코드워드 결합 BP 디코더 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6881250
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Stephan Pfletschinger
- **PDF**: https://ieeexplore.ieee.org/document/6881250
- **Abstract**: We develop a belief-propagation (BP) decoder for the joint decoding of multiple codewords which belong to the same non-binary LDPC code. Decoding is based on soft information in form of joint channel-posterior probabilities of all codeword symbols. We extend the BP algorithm for q-ary LDPC codes such that the FFT-based check node processing is preserved and the complexity remains manageable. This joint decoding is useful in settings in which multiple codewords are transmitted in a non-orthogonal way over the same channel, including multiple-access with packet collisions, physical-layer network coding and multi-resolution broadcasting. We show in an example that joint decoding can be far superior to separate decoding.

## Practical LDPC coded modulation schemes for the fading broadcast channel with confidential messages

- **Status**: ❌
- **Reason**: 기밀 메시지 페이딩 방송채널용 LDPC 부등오류보호 변조, 보안/무선 응용 특이적이며 표준 LDPC 사용
- **ID**: ieee:6881291
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Marco Baldi, Nicola Maturo, Giacomo Ricciutelli +1
- **PDF**: https://ieeexplore.ieee.org/document/6881291
- **Abstract**: The broadcast channel with confidential messages is a well studied scenario from the theoretical standpoint, but there is still lack of practical schemes able to achieve some fixed level of reliability and security over such a channel. In this paper, we consider a quasi-static fading channel in which both public and private messages must be sent from the transmitter to the receivers, and we aim at designing suitable coding and modulation schemes to achieve such a target. For this purpose, we adopt the error rate as a metric, by considering that reliability (security) is achieved when a sufficiently low (high) error rate is experienced at the receiving side. We show that some conditions exist on the system feasibility, and that some outage probability must be tolerated to cope with the fading nature of the channel. The proposed solution exploits low-density parity-check codes with unequal error protection, which are able to guarantee two different levels of protection against noise for the public and the private information, in conjunction with different modulation schemes for the public and the private message bits.

## Low-complexity layered BP-based detection and decoding for a NB-LDPC coded MIMO system

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) MIMO 디코딩이라 바이너리 한정 원칙에 따라 제외
- **ID**: ieee:6884131
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Ali Haroun, Charbel Abdel Nour, Matthieu Arzel +1
- **PDF**: https://ieeexplore.ieee.org/document/6884131
- **Abstract**: In this paper, the combination of a low-complexity Multiple-input Multiple-output based on belief propagation (MIMO-BP) detector with a Non-Binary Low-Density Parity-Check (NB-LDPC) decoder is investigated. Such detection and decoding algorithms can enable an equivalent representation based on a larger Joint Factor Graph (JFG). Shuffle schedule can therefore be used jointly and simultaneously on the detector and the decoder. Actions are undertaken at the detector, decoder and the iterative receiver levels in order to reduce overall complexity. Indeed, applying the proposed low-complexity BP-based detection greatly reduces the number of operations per iteration (divided by ten), with a negligible performance penalty. EXtrinsic Information Transfer (EXIT) charts enable to analyze the convergence behaviour of the proposed iterative receiver. This analysis is used to find the best set of parameters enabling a detection-decoding process with a performance closest to the full-complexity system.

## A robust pulse position coded modulation scheme for the Poisson channel

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC + q-ary PPM Poisson 채널 코딩 변조 — 비이진 LDPC라 제외
- **ID**: ieee:6883636
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Balázs Matuz, Giuseppe Toscano, Gianluigi Liva +2
- **PDF**: https://ieeexplore.ieee.org/document/6883636
- **Abstract**: A coded modulation scheme for the Poisson channel is investigated. The scheme relies on the serial concatenation of an outer low-density parity-check (LDPC) code over an order-q finite field and q-ary pulse position modulation (PPM). Due to the matching between code and modulation symbols, no iterative message exchange between the decoder and the modulator is required. The PPM capacity limit serves as a reference to evaluate the efficiency of the proposed scheme in the asymptotic setting via density evolution. A simplified form of the Gallager random coding bound (RCB) is also developed and used as a reference for the finite-length performance of the coded modulation scheme. The optimization via density evolution is performed on a surrogate (erasure) channel, yielding excellent iterative decoding thresholds for a wide range of channel parameters. The proposed coded modulation technique performs close to the theoretical bounds not only asymptotically, but also for moderate block lengths. It turns to represent a viable solution for deep-space direct detection optical links, for which the Poisson channel is adopted as a model.

## Measurement-based study of the performance of IEEE 802.11ac in an indoor environment

- **Status**: ❌
- **Reason**: 802.11ac 실내 성능 측정 연구로 LDPC ECC 무관
- **ID**: ieee:6884242
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Mihaela-Diana Dianu, Janne Riihijärvi, Marina Petrova
- **PDF**: https://ieeexplore.ieee.org/document/6884242
- **Abstract**: We present results from a measurement-based study of the performance of the emerging IEEE 802.11ac Wi-Fi standard in an indoor environment. The measurements were conducted in a typical office building, and show that for small distances IEEE 802.11ac offers significantly improved performance compared to IEEE 802.11n. However, these performance improvements were also found to be quite sensitive to channel conditions, with the achieved data rates rapidly declining as the distance between the transmitter and the receiver is increased. We also studied the coexistence properties of IEEE 802.11ac through measurements, observing that adjacent channel interference from legacy Wi-Fi devices can have a severe performance impact. For co-channel interference, the medium access control mechanism of IEEE 802.11ac allows it to share the channel effectively with other Wi-Fi devices.

## Rate-adaptive constellation shaping for near-capacity achieving turbo coded BICM

- **Status**: ❌
- **Reason**: Turbo coded BICM constellation shaping — turbo·변조 매핑 중심, LDPC BP 이식 기법 없음
- **ID**: ieee:6883635
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Metodi Yankov, Søren Forchhammer, Knud J. Larsen +1
- **PDF**: https://ieeexplore.ieee.org/document/6883635
- **Abstract**: In this paper the problem of constellation shaping is considered. Mapping functions are designed for a many-to-one signal shaping strategy, combined with a turbo coded Bit-interleaved Coded Modulation (BICM), based on symmetric Huffman codes with binary reflected Gray-like properties. An algorithm is derived for finding the Huffman code with such properties for a variety of alphabet sizes, and near-capacity performance is achieved for a wide SNR region by dynamically choosing the optimal code rate, constellation size and mapping function based on the operating SNR point and assuming perfect channel quality estimation. Gains of more than 1dB are observed for high SNR compared to conventional turbo coded BICM, and it is shown that the mapping functions designed here significantly outperform current state of the art Turbo-Trellis Coded Modulation and other existing constellation shaping methods.

## Seek and decode: Random multiple access with multiuser detection and physical-layer network coding

- **Status**: ❌
- **Reason**: 랜덤 다중접속 + PLNC over EGF, 비이진(EGF) 결합 디코더 — 비이진이며 NAND 이식 기법 없음
- **ID**: ieee:6881248
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Giuseppe Cocco, Stephan Pfletschinger
- **PDF**: https://ieeexplore.ieee.org/document/6881248
- **Abstract**: We present a novel random multiple access scheme that combines joint multiuser detection (MUD) with physical layer network coding (PLNC) over extended Galois fields (EGF). We derive an analytical bound on the throughput at the system level and present simulation results for the decoding at the physical level in both fast fading and block fading channels. We adopt a cross layer approach in which a non-binary joint multiuser decoder is used in combination with PLNC at slot level, while the use of EGF aims at increasing the system diversity at frame level. The results we present are encouraging and suggest that the combination of these two interference management techniques can significantly enhance the performance of random multiple access systems.

## K-user nonbinary parallel concatenated code for Gaussian multiple-access channel

- **Status**: ❌
- **Reason**: 비이진 GF(q) parallel concatenated code — 비이진·비-LDPC, 제외
- **ID**: ieee:6883626
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Haifeng Han, Guanghui Song, Masakazu Yoshida +1
- **PDF**: https://ieeexplore.ieee.org/document/6883626
- **Abstract**: A K-user nonbinary parallel concatenated code (PCC) is proposed for a Gaussian MAC with symbol synchronization, equal-power, and equal-rate users. In a K-user q-ary PCC over finite field GF(q), each user employs a parallel concatenated code, with a rate-(1/r) q-ary repetition component code and M rate-1 q-ary accumulation component codes. Employing q-ary repetition code is to overcome the multi-user interference and also provide coding gain. The K-user q-ary PCC is not only rate compatible, but also with very low encoding and decoding complexities due to employing such simple component codes. An EXIT chart analysis is given to estimate the decoding threshold of the K-user q-ary PCC. Numerical results show that the decoding threshold of K-user q-ary PCC improves as the field order q increases. The 10-user 64-ary PCC improves the decoding threshold by 1.88 dB over the binary case. The decoding threshold of 15-user 64-ary PCC at sum rate 3/4 is only 0.75 dB away from the Shannon bound. Bit-error-rate simulations are provided to verify the analysis.

## An accurate frame error rate approximation of coded diversity systems with non-identical diversity branches

- **Status**: ❌
- **Reason**: 수신 다이버시티 시스템 FER 근사 이론, 디코더/HW/코드설계로 이어지지 않음
- **ID**: ieee:6884165
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Gang Wang, Jingxian Wu, Yahong Rosa Zheng
- **PDF**: https://ieeexplore.ieee.org/document/6884165
- **Abstract**: This paper presents an accurate approximation of the frame error rate (FER) of coded wireless communication systems with receiver diversity, such as single-input multiple-output (SIMO) systems with maximum ratio combining (MRC) or hybrid automatic repeat request (HARQ) systems with Chase combining. The signals at different diversity branches experience independent but non-identically distributed Rayleigh fading. The FER approximation is obtained with a threshold-based method. Specifically, the threshold value, which is critical to the FER approximation accuracy, is modeled as a linear function of the frame length in the log-domain, with the slope and intercept of the linear function determined by the underlying modulation and channel coding schemes. The analytical FER approximation is expressed as an explicit function of parameters related to modulation, coding, frame length, number of diversity branches, and the power distribution across the diversity branches. Such an FER approximation summarizes the complex physical layer operations into a few parameters, and it provides the parametric flexibility that is not available in most existing FER approximations. Simulation results show that the proposed FER approximation can accurately predict the FER performance of a wide range of receiver diversity systems.

## Low latency radio interface for 5G flexible TDD local area communications

- **Status**: ❌
- **Reason**: 5G TDD 저지연 라디오 인터페이스 설계, LDPC ECC 기법 없음
- **ID**: ieee:6881164
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Toni Levanen, Juho Pirskanen, Timo Koskela +2
- **PDF**: https://ieeexplore.ieee.org/document/6881164
- **Abstract**: This paper presents a low latency radio interface design for future 5G local area communications that provides transmission latencies less than 1 ms while providing sufficient spectral efficiency. We concentrate on the excellent latency aspects of the proposed 5GETLA radio interface and discuss the factors leading to very low latency and high energy efficiency. In addition, we study two different radio interface parameterizations and compare their total overheads and achievable transmission times.

## BER of IEEE 802.11ad OFDM radios vs. carrier frequency in real 60 GHz indoor channels

- **Status**: ❌
- **Reason**: 802.11ad 60GHz 채널 BER 측정 연구로 LDPC ECC 이식 기법 없음
- **ID**: ieee:6884260
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Nikola Rendevski, Dajana Cassioli
- **PDF**: https://ieeexplore.ieee.org/document/6884260
- **Abstract**: Multi-gigabit 60 GHz radios are expected to match QoS requirements of modern multimedia applications. Several published standards were defined based on performance evaluations over standard channel models. Unfortunately, those models, and most models available in the literature, do not take into account the behavior of 60 GHz channels at different carrier frequencies, thus no guidelines are provided for the selection of the best suitable frequency band for a given service. This paper analyzes the impact of changes in multipath profiles, due to both frequency and distance, on the BER performance achieved by IEEE 802.11ad 60 GHz radios. Our analysis is based on real experimental channel impulse responses recorded through an indoor measurement campaign in seven sub-bands from 54 to 65 GHz with a break at 60 GHz at distances from 1 to 5 m. The small-scale fading is modeled by Rician distributions with K-factors extracted from experimental data, which are shown to give good agreement with the empirical distributions. A strong dependence of performance on both frequency and distance due to the sole multipath is observed, which calls for an appropriate selection of the best suitable frequency band according to the service required by the current session over the 802.11ad link.

## Analog fountain codes with unequal error protection property

- **Status**: ❌
- **Reason**: Analog fountain code의 UEP — fountain/rateless로 떼어낼 LDPC ECC 기법 없음, 원칙 제외
- **ID**: ieee:6883622
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Mahyar Shirvanimoghaddam, Yonghui Li, Branka Vucetic
- **PDF**: https://ieeexplore.ieee.org/document/6883622
- **Abstract**: In this paper, we propose a novel rateless code with unequal error protection (UEP) property based on recently proposed analog fountain codes (AFCs). AFCs have been originally designed and optimized to approach the capacity of a Gaussian channel in a wide range of signal to noise ratios (SNRs). In this paper, we are particularly interested in the UEP property of AFC codes, providing different levels of error protection for various sets of information symbols. In the proposed AFC code with UEP property (AFC-UEP), the whole block of information symbols is partitioned into several parts, where each part requires a certain level of error protection. Each part is then assigned with a selection probability and a code degree, which are optimized based on the error probability analysis of the AFC code to satisfy the required error protection levels of all information parts. Simulation results show that the proposed scheme can effectively provide an unequal error protection for different sets of information symbols. Moreover, various error protection requirements can be simply achieved by optimizing the code degree and the selection probability of each part; thus, achieving the desired level of error protection for each part.

## Rate optimization for repeat-accumulate interleave-division system by fixed-point analysis

- **Status**: ❌
- **Reason**: Repeat-accumulate interleave-division 멀티유저 rate 최적화 — RA/spreading 멀티유저 GMAC 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6883633
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Meilin He, Guanghui Song, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/6883633
- **Abstract**: A K-user repeat-accumulate interleave-division (RAID) system is considered for a Gaussian multiple access channel (GMAC) with binary inputs, equal-power, and symbol synchronization. In this system, a regular repeat accumulate (RA) code serially concatenated with spreading, where the rate of RA code and spreading length both can be changed, is employed for each user. K users are divided into M groups equally. The mth group contains K/M users with rate Rm (1 ≤ m ≤ M). At the receiver, multiuser message-passing decoding is performed on a single factor graph. A fixed point analysis is developed to obtain all achievable rate profiles for an arbitrary small decoding error rate over the GMAC. It shows that the sum rate of our optimal rate profile is superior to that of conventional multiuser RAID scheme with equal rate.

## Low complexity block pre-distortion of a multi-carrier non-linear satellite channel

- **Status**: ❌
- **Reason**: 위성 다중반송파 비선형 채널 사전왜곡(pre-distortion) 알고리즘으로 LDPC/ECC 무관, 떼어낼 디코더·HW 기법 없음
- **ID**: ieee:6884000
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Th. Deleu, M. Dervin, F. Horlin
- **PDF**: https://ieeexplore.ieee.org/document/6884000
- **Abstract**: In a multi-carrier non-linear satellite communication channel, inter-symbol interference (ISI) and adjacent channel interference (ACI) occur due to the non-linear power amplifier aboard the satellite. In order to prevent a too high performance degradation, large input back-offs (IBO) are generally considered. However, if all carriers are issued from the same ground station, pre-distortion of the whole transmitted signal can be a better solution to achieve higher power efficiency aboard the satellite and/or spectral efficiency. The relation between the symbols transmitted on the channel and the received symbols is tricky for a multi-carrier system, as it involves several symbol flows. Few approaches have been proposed yet to provide an efficient algorithm with reasonable complexity in such context. In this paper, we will derive a sub-optimum algorithm for the pre-distortion of a multi-carrier non-linear satellite channel which offers a good trade-off between performance and complexity.

## Packet acquisition for spatially coupling information transmission

- **Status**: ❌
- **Reason**: spatially-coupled 전송의 패킷 타이밍 획득/다중접속 수신 — 떼어낼 LDPC 디코더/코드설계 기법 없음
- **ID**: ieee:6881247
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Dmitri Truhachev
- **PDF**: https://ieeexplore.ieee.org/document/6881247
- **Abstract**: The problem of packet timing acquisition for random access multi-user communications is considered. The users employ coupling information transmission format to encode and modulate their data packets and communicate them to the common receiver. Two reception strategies are studied: the case in which packet acquisition is followed by multi-user decoding of the coupled data packets and the case in which packet acquisition is included into the iterative multi-user decoding loop. An analysis of the iterative acquisition and decoding is presented and communication rates achievable for various preamble lengths are computed. It is demonstrated that incorporation of packet acquisition into the data decoding and interference cancellation loop is essential for establishing near-capacity communications with practical preamble lengths.

## Reliable and energy-efficient OFDM based on structured compressive sensing

- **Status**: ❌
- **Reason**: Compressive sensing 기반 OFDM 채널 추정 — LDPC ECC 무관, 무선 응용 특이적
- **ID**: ieee:6883940
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Linglong Dai, Zhaocheng Wang, Zhixing Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6883940
- **Abstract**: Compared with standard cyclic prefix OFDM (CP-OFDM), time domain synchronous OFDM (TDS-OFDM) can achieve a higher spectrum efficiency by using the known training sequence instead of CP as the guard interval. However, TDS-OFDM suffers from reduced energy efficiency and performance loss due to the existing mutual inferences. In this paper, based on the newly emerging theory of structured compressive sensing (SCS), we propose a reliable and energy-efficient TDS-OFDM transmission scheme with reduced guard interval power (which is impossible for CP-OFDM) by designing a channel estimation scheme with high accuracy. The wireless channel properties including channel sparsity and inter-channel correlation, which are usually not considered in conventional OFDM schemes, have been exploited. We further exploit the worst-case system design principle to extract multiple interference-free regions of small size to simultaneously reconstruct multiple channels of large size without iterative interference cancellation. In this way, the guard interval power in TDS-OFDM can be reduced to achieve a 20% higher energy efficiency than standard CP-OFDM, and the system reliability can be also improved in fast fading channels.

## Iterative multistage decoding of polar code based multilevel codes

- **Status**: ❌
- **Reason**: Polar code 기반 multilevel code의 iterative multistage 디코딩 — polar 전용이고 LDPC BP에 부호 비의존적으로 이식할 기법 없음, 비-LDPC 원칙 제외
- **ID**: ieee:6883620
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Liang Zhang, Zhaoyang Zhang, Xianbin Wang
- **PDF**: https://ieeexplore.ieee.org/document/6883620
- **Abstract**: Some multilevel codes which are constructed based on polar codes have been introduced recently, and show good performance with elaborately designed rates at each level and special multistage decoder. However, the multistage decoding is usually implemented in a sequential manner, which might yield poor performance at lower levels since the corresponding component codes are decoded without any information from higher levels, and the decoding errors occurred at previous stages could hardly be corrected. Thus, an iterative multistage decoding algorithm for polar code based multilevel codes is introduced in this paper, which could further improve the performance by feeding the reliable information obtained at higher levels back to the first level, and correct the decoding errors occurred at lower levels. Our proposed algorithm has only moderate complexity, and it is found that, the first iteration contributes the most performance improvement.

## Simple turbo MIMO scheme using arithmetic extended mapping and repetition codes

- **Status**: ❌
- **Reason**: turbo MIMO + repetition code 무선 응용, 비-LDPC 부호이며 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:6884097
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Keisuke Yamamoto, Takashi Yano, Takehiko Kobayashi
- **PDF**: https://ieeexplore.ieee.org/document/6884097
- **Abstract**: A simple turbo multi-input multi-output (MIMO) scheme using arithmetic-extended mapping and repetition codes is proposed. To mitigate performance degradation of MIMO schemes caused by spatial correlation, a soft canceller followed by minimum-mean-squared-error filter (SC-MMSE) and an iterative-decoding technique based on the turbo principle are adopted. This turbo MIMO scheme is designed by using 8-amplitude-shift keying (8-ASK) arithmetic extended mapping and a 1/4-rate repetition code. The performance of the proposed turbo MIMO scheme is verified in terms of bit error rate (BER) for a spatially correlated Rayleigh channel. The scheme exhibits a “turbo cliff” at signal-to-noise ratio (SNR) of 28 dB. Compared to a conventional MIMO scheme using MMSE with 64-quadrature-amplitude-modulation (64-QAM) mapping and a 1/2-rate turbo code, the proposed scheme improves SNR by 1.8 dB at BER of 104.

## Algebraic and linear programming decoding of the (73, 37, 13) quadratic residue code

- **Status**: ❌
- **Reason**: (73,37,13) QR 코드의 대수적/LP 디코딩 — 비-LDPC 부호이며 부호 의존적 BM/QR 기법, 바이너리 LDPC BP 이식 불가
- **ID**: ieee:6883619
- **Type**: conference
- **Published**: 10-14 June
- **Authors**: Yong Li, Hongqing Liu, Qianbin Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6883619
- **Abstract**: In this paper1, a method to search the subsets I and J needed in computing the unknown syndromes for the (73, 37, 13) quadratic residue (QR) code is proposed. According to the resulting I and J, one computes the unknown syndromes, and thus finds the corresponding error-locator polynomial by using an inverse-free BM algorithm. Based on the modified Chase-II algorithm, the performance of soft-decision decoding for the (73, 37, 13) QR code is given. This result is never seen in the literature, to our knowledge. Moreover, the error-rate performance of linear programming (LP) decoding for the (73, 37, 13) QR code is also investigated, and LP-based decoding is shown to be significantly superior in performance to the algebraic soft-decision decoding while requiring almost the same computational complexity.

## Area-efficient TFM-based stochastic decoder design for non-binary LDPC codes

- **Status**: ❌
- **Reason**: GF(32) non-binary LDPC stochastic 디코더 — 비이진은 제외
- **ID**: ieee:6865152
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Chih-Wen Yang, Xin-Ru Lee, Chih-Lung Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/6865152
- **Abstract**: This paper presents a non-binary LDPC decoder based on stochastic arithmetic. Although the previous stochastic works reduce the complexity of check node by transforming the convolution of the SPA algorithm to the finite field summation, the stochastic decoder still has a implementation bottleneck due to large storage introduced by the variable node process. Considering a balance between algorithm level and implementation level, we propose a shortened TFM architecture as well as its updating criterion. A compare-and-alter counter architecture is also proposed to avoid sorting among counters which decide the decoded codeword. With these features, the proposed (136, 68) fully-parallel stochastic NB-LDPC decoder over GF(32) implemented in UMC 90-nm can achieve 120 Mb/s throughput while operating under 455 MHz with 740 k gate counts which are only 10 % of the original TFM decoder.

## Efficient symbol reliability based decoding for QCNB-LDPC codes

- **Status**: ❌
- **Reason**: QCNB-LDPC (non-binary) 디코딩 — 비이진은 제외
- **ID**: ieee:6865151
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Leixin Zhou, Jin Sha, Yun Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/6865151
- **Abstract**: As an extension of binary low-density parity-check (LDPC) codes, non-binary LDPC (NB-LDPC) codes show significantly better performance when the code length is moderate or small. Recently, enhanced iterative hard reliability based (EIHRB) decoding algorithm is proposed to reduce the computation complexity. However, the EIHRB algorithm suffers a lot from significant performance degradation when the column weight is small. In this paper, a symbol reliability based (SRB) decoding algorithm, which also performs well when the column weight is low, is proposed for NB-LDPC decoding to improve the decoding performance. With the same maximum iteration number, around 0.38 dB extra coding gain is achieved. Furthermore, the corresponding efficient decoder architecture is proposed. Comparison results have shown that the proposed SRB algorithm can not only achieve good coding gain, but the cost for hardware implementation is reasonable.

## An efficient decoder architecture for cyclic non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary NB-LDPC 디코더 — 비이진은 제외
- **ID**: ieee:6865149
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Yichao Lu, Guifen Tian, Satoshi Goto
- **PDF**: https://ieeexplore.ieee.org/document/6865149
- **Abstract**: This paper proposes a hybrid message-passing decoding algorithm which consumes very low computational complexity, while achieving competitive error performance compared with conventional min-max algorithm. Simulation result on a (255,175) cyclic code shows that this algorithm obtains at least 0.5dB coding gain over other state-of-the-art low-complexity non-binary LDPC (NB-LDPC) decoding algorithms. Based on this algorithm, a partial-parallel decoder architecture is implemented for cyclic NB-LDPC codes, where the variable node units are redesigned and the routing network is optimized for the proposed algorithm. Synthesis results demonstrate that about 24.3% gates and 12% memories can be saved over previous works.

## A novel secure MIMO cognitive network

- **Status**: ❌
- **Reason**: MIMO 인지무선 보안 응용에 LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:6865425
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Yang Xiao, Pengpeng Lan, Dong Wang
- **PDF**: https://ieeexplore.ieee.org/document/6865425
- **Abstract**: The existing cognitive radio networks (CRNs) lack the ability to deal with the electronic attack of malicious users, which can destroy the normal communication of the cognitive users. To solve the problem, we propose a novel secure CRN by combining MIMO technique and low density parity check (LDPC) codes at the base-station (BS) and mobile stations (MSs), the electronic interference of the malicious users can be effectively weakened. The capacity and the outage probability of the proposed MIMO CRN are analyzed. The simulation results in quasi-static Rayleigh flat-fading channel show that the proposed secure MIMO CRN can effectively cancel electronic interference from the malicious users.

## The accuracy and scalability of continuous-time Bayesian inference in analogue CMOS circuits

- **Status**: ❌
- **Reason**: 아날로그 CMOS factor-graph Bayesian inference 일반론, LDPC 디코더 기여 아님
- **ID**: ieee:6865450
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Przemyslaw Mroszczyk, Piotr Dudek
- **PDF**: https://ieeexplore.ieee.org/document/6865450
- **Abstract**: This paper discusses the idea of Bayesian inference in factor graphs implemented as continuous-time current-mode analogue CMOS circuits using Gilbert multipliers for arithmetic operations. The computational accuracy, accounting for the systematic and random (fabrication mismatch) errors, and the scalability of such realisations were verified in simulations of networks consisting of 5 - 121 nodes implemented using models from a standard 90 nm CMOS technology. The obtained results show a relatively short settling time, typically below 3 μs at a power less than 7 mW, with the equivalent computational speed of over 35 arithmetic operations per nanosecond but with a limited accuracy, mainly affected by fabrication mismatch. Such realisations could be used in applications requiring fast and low power approximate Bayesian inference.

## On jamming-proof signal-code constructions for a multiple access system

- **Status**: ❌
- **Reason**: 비이진(nonbinary) 내부 부호 기반 재밍 대응 신호-코드 구성; 비이진 LDPC/비-LDPC, NAND 이식 기법 없음
- **ID**: ieee:7016710
- **Type**: conference
- **Published**: 1-5 June 2
- **Authors**: Dmitry Osipov
- **PDF**: https://ieeexplore.ieee.org/document/7016710
- **Abstract**: In what follows signal-code constructions employing block and convolutional nonbinary inner codes that can perform under severe jamming are proposed. Robustness of the proposed signal-code constructions to jamming is verified by means of simulation.

## Left degree distribution shaping for LT codes over the binary erasure channel

- **Status**: ❌
- **Reason**: LT/fountain BEC용 left degree 분포 설계 — fountain/erasure, NAND 채널 ECC 이식 기법 없음
- **ID**: ieee:6841213
- **Type**: conference
- **Published**: 1-4 June 2
- **Authors**: Khaled F. Hayajneh, Shahram Yousefi, Mehrdad Valipour
- **PDF**: https://ieeexplore.ieee.org/document/6841213
- **Abstract**: Fountain codes were introduced to provide higher reliability, lower complexities, and more scalability for networks such as the Internet. Luby-Transform (LT) codes, which are the first realization of Fountain codes, achieve the capacity of the binary erasure channel (BEC) asymptotically and universally. For finite lengths, the search is continued to find codes closer to the capacity limits at even lower encoding and decoding complexities. Most previous work on single-layer Fountain coding targets the design via the right degree distribution. The left degree distribution of an LT code is left as Poisson to protect the universality. For finite lengths, this is no longer an issue; thus, we focus on the design of better codes for the BEC at practical lengths. Our left degree shaping provides codes outperforming LT and all other competing schemes in the literature. At a bit error rate of 10−7 and packet length k = 256, our scheme provides a realized rate of 0.6 which is 23.5% higher than Sorensen et al.'s scheme [1].
