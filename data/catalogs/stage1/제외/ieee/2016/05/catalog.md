# IEEE Xplore — 2016-05


## Hard-Information Bit-Reliability Based Decoding Algorithm for Majority-Logic Decodable Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(majority-logic decodable nonbinary LDPC) bit-reliability 디코딩 — 비이진 LDPC 제외
- **ID**: ieee:7425163
- **Type**: journal
- **Published**: May 2016
- **Authors**: Xiangcheng Li, Tuanfa Qin, Haiqiang Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/7425163
- **Abstract**: A modified bit-reliability based decoding algorithm is presented based on a recent work by Huang et al. For the presented algorithm, only one Galois field element is passed and exchanged along the edges of the Tanner graph. At variable nodes, full messages rather than extrinsic messages are processed to further reduce the computational complexity. At check nodes, only hard reliability is considered and the main operation is to compute the check-sum and send one extrinsic symbol back to variable nodes. Simulation results show that, even with lower complexity and less memory consumption, the presented algorithm still can perform very closely to the original wBRB algorithm with low quantization bits (3 ~ 4 bits) when decoding the majority-logic decodable nonbinary LDPC codes. For codes constructed in high order fields, the presented algorithm can even outperform the original wBRB algorithm.

## High-Performance NB-LDPC Decoder With Reduction of Message Exchange

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC, GF16/32/64) trellis min-max 디코더 — 비이진 LDPC는 제외
- **ID**: ieee:7328322
- **Type**: journal
- **Published**: May 2016
- **Authors**: Jesús O. Lacruz, Francisco García-Herrero, María José Canet +1
- **PDF**: https://ieeexplore.ieee.org/document/7328322
- **Abstract**: This paper presents a novel algorithm based on trellis min-max for decoding non-binary low-density parity-check (NB-LDPC) codes. This decoder reduces the number of messages exchanged between check node and variable node processors, which decreases the storage resources and the wiring congestion and, thus, increases the throughput of the decoder. Our frame error rate performance simulations show that the proposed algorithm has a negligible performance loss for high-rate codes with GF(16) and GF(32) and a performance loss smaller than 0.07 dB for high-rate codes over GF(64). In addition, a layered decoder architecture is presented and implemented on a 90-nm CMOS process for the following high-rate NB-LDPC codes: (2304, 2048) over GF(16), (837, 726) over GF(32), and (1536, 1344) over GF(64). In all cases, the achieved throughput is higher than 1 Gb/s.

## Bounds on the Belief Propagation Threshold of Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 LDPC BP threshold bound (순수 이론) — 비이진+이론 bound, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7429784
- **Type**: journal
- **Published**: May 2016
- **Authors**: Leonid Geller, David Burshtein
- **PDF**: https://ieeexplore.ieee.org/document/7429784
- **Abstract**: We consider low-density parity-check (LDPC) code ensembles over non-binary Galois fields when used for transmission over arbitrary discrete memoryless channels. Belief propagation decoding for these codes has been shown to achieve excellent results. However, computing the decoding threshold using density evolution is usually impractical, since one needs to propagate multi-dimensional probability distributions, and Monte Carlo simulations are required instead. By considering the evolution of the message Bhattacharyya parameter and the message expected value parameter, we derive a simple lower bound on the performance of the algorithm. This bound applies for both regular and irregular non-binary LDPC ensembles.

## Threshold Saturation for Nonbinary SC-LDPC Codes on the Binary Erasure Channel

- **Status**: ❌
- **Reason**: 비이진 SC-LDPC threshold saturation 이론 — 비이진 LDPC 제외
- **ID**: ieee:7430313
- **Type**: journal
- **Published**: May 2016
- **Authors**: Iryna Andriyanova, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/7430313
- **Abstract**: We analyze the asymptotic performance of nonbinary spatially coupled low-density parity-check (SC-LDPC) code ensembles defined over the general linear group on the binary erasure channel. In particular, we prove the threshold saturation of belief propagation decoding to the so-called potential threshold, using the proof technique based on potential functions introduced by Yedla et al., assuming that the potential function exists. We rewrite the density evolution of nonbinary SC-LDPC codes in an equivalent vector recursion form which is suited for the use of the potential function. We then discuss the existence of the potential function for the general case of vector recursions defined by multivariate polynomials, and give a method to construct it. We define a potential function in a slightly more general form than the one by Yedla et al., in order to make the technique based on potential functions applicable to the case of nonbinary LDPC codes. We show that the potential function exists if a solution to a carefully designed system of linear equations exists. Furthermore, we numerically show the existence of a solution to the system of linear equations for a large number of nonbinary LDPC code ensembles, which allows us to define their potential function and thus prove threshold saturation.

## A Soft Decode–Compress–Forward Relaying Scheme for Cooperative Wireless Networks

- **Status**: ❌
- **Reason**: 협력 무선 soft decode-compress-forward 릴레이 분산 LDPC; 무선 응용 특이적 soft relaying으로 NAND에 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:7118747
- **Type**: journal
- **Published**: May 2016
- **Authors**: Dushantha N. K. Jayakody, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7118747
- **Abstract**: This paper proposes a new technique for soft information relaying, which is based on a soft decode–compress–forward relay protocol. The proposed system provides a means of using distributed low-density parity-check (LDPC) coding in conjunction with higher order modulation, such as pulse amplitude modulation (PAM) and quadrature amplitude modulation (QAM), which is effective even under poor source–relay link conditions. Ordinarily, such schemes suffer from error propagation to the destination caused by incorrect decoding at the relay when the signal-to-noise ratio (SNR) on the source–relay link is low; however, our system avoids this problem by generating soft versions of the additional (parity-bearing) PAM symbols for transmission from the relay. The proposed technique of soft compression does not suffer from parity log-likelihood ratios (LLRs) converging to zero, as do many soft re-encoding techniques for turbo and LDPC codes. In the case of Gray-coded PAM/QAM signaling, we also propose a method of performing exact expectation-based soft modulation with low computational complexity. Furthermore, we propose a new model, which we refer to as the soft scalar model, for the overall source-to-destination channel encountered by the constellation symbols, and this model is used at the destination to compute LLRs for joint decoding of the distributed LDPC code. Simulation results demonstrate that the proposed scheme can provide good coding gain, diversity gain, and spectral efficiency under poor source–relay SNR conditions.

## A Soft-Network-Coded Multilevel Forwarding Scheme for Multiple-Access Relay Systems

- **Status**: ❌
- **Reason**: 릴레이 네트워크 코딩용 LLR 멀티레벨 양자화(MLT-SQ); LDPC는 부수 시뮬레이션 베이스라인, NAND로 떼어낼 ECC 기법 없음
- **ID**: ieee:7120177
- **Type**: journal
- **Published**: May 2016
- **Authors**: Dushantha N. K. Jayakody, Jun Li, Mark F. Flanagan
- **PDF**: https://ieeexplore.ieee.org/document/7120177
- **Abstract**: This paper proposes the novel technique of multilevel-threshold-based soft quantization (MLT-SQ) for a multiple-access relay system (MARS). The scheme is suitable for systems using binary phase-shift keying (BPSK) and network coding at the relay. In the proposed MLT-SQ protocol, the relay evaluates the reliabilities, which are expressed as log-likelihood ratios (LLRs), of the received signals from the two sources. It then computes the LLRs of the network-coded packet and quantizes these using a set of optimized multilevel thresholds, forwarding the resulting “quantized soft symbols” to the destination. We provide the derivation for the bit error rate (BER) at the destination, and based on this, we optimize the multilevel thresholds to minimize the BER. Simulation results are provided for the proposed MLT-SQ system, both without coding and for the case where low-density parity-check (LDPC) coding is employed. The proposed system achieves full diversity order. Compared with competing schemes, the performance of our system is superior in terms of BER when the same amount of channel state information (CSI) is exploited.

## High Capacity Reversible Data Hiding in Encrypted Images by Patch-Level Sparse Representation

- **Status**: ❌
- **Reason**: 암호화 이미지 가역 데이터 은닉/sparse coding; 데이터 하이딩으로 채널 ECC 무관
- **ID**: ieee:7098386
- **Type**: journal
- **Published**: May 2016
- **Authors**: Xiaochun Cao, Ling Du, Xingxing Wei +2
- **PDF**: https://ieeexplore.ieee.org/document/7098386
- **Abstract**: Reversible data hiding in encrypted images has attracted considerable attention from the communities of privacy security and protection. The success of the previous methods in this area has shown that a superior performance can be achieved by exploiting the redundancy within the image. Specifically, because the pixels in the local structures (like patches or regions) have a strong similarity, they can be heavily compressed, thus resulting in a large hiding room. In this paper, to better explore the correlation between neighbor pixels, we propose to consider the patch-level sparse representation when hiding the secret data. The widely used sparse coding technique has demonstrated that a patch can be linearly represented by some atoms in an over-complete dictionary. As the sparse coding is an approximation solution, the leading residual errors are encoded and self-embedded within the cover image. Furthermore, the learned dictionary is also embedded into the encrypted image. Thanks to the powerful representation of sparse coding, a large vacated room can be achieved, and thus the data hider can embed more secret messages in the encrypted image. Extensive experiments demonstrate that the proposed method significantly outperforms the state-of-the-art methods in terms of the embedding rate and the image quality.

## Secure Multiplex Coding With Dependent and Non-Uniform Multiple Messages

- **Status**: ❌
- **Reason**: 보안(wire-tap/secure multiplex coding); 임의 부호를 재료로 쓰는 보안 기법, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7407383
- **Type**: journal
- **Published**: May 2016
- **Authors**: Masahito Hayashi, Ryutaroh Matsumoto
- **PDF**: https://ieeexplore.ieee.org/document/7407383
- **Abstract**: The secure multiplex coding (SMC) is a technique to remove rate loss in the coding for wire-tap channels and broadcast channels with confidential messages caused by the inclusion of random bits into transmitted signals. SMC replaces the random bits by other meaningful secret messages, and a collection of secret messages serves as the random bits to hide the rest of messages. In the previous studies, multiple secret messages were assumed to have independent and uniform distributions, which is difficult to be ensured in practice. We remove this restrictive assumption by a generalization of the channel resolvability technique. We also give practical construction techniques for SMC by using an arbitrary given error-correcting code as an ingredient, and channel-universal coding of SMC. By using the same principle as the channel-universal SMC, we give coding for the broadcast channel with confidential messages universal to both channel and source distributions.

## Polar Coding for the Broadcast Channel With Confidential Messages: A Random Binning Analogy

- **Status**: ❌
- **Reason**: polar 부호 보안 코딩 — 비-LDPC, 부호 의존적 보안 스킴이라 예외 포함 대상 아님
- **ID**: ieee:7426806
- **Type**: journal
- **Published**: May 2016
- **Authors**: Rémi A. Chou, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/7426806
- **Abstract**: We develop a low-complexity polar coding scheme for the discrete memoryless broadcast channel with confidential messages under strong secrecy and randomness constraints. Our scheme extends previous work by using an optimal rate of uniform randomness in the stochastic encoder, and avoiding assumptions regarding the symmetry or degraded nature of the channels. The price paid for these extensions is that the encoder and the decoders are required to share a secret seed of negligible size and to increase the block length through chaining. We also highlight a close conceptual connection between the proposed polar coding scheme and a random binning proof of the secrecy capacity region.

## Hamming coding for multi-relay cooperative quantize and forward networks

- **Status**: ❌
- **Reason**: Hamming code 협력중계 네트워크-비-LDPC 부호, 이식 디코더 기법 없음
- **ID**: ieee:7519426
- **Type**: conference
- **Published**: 9-11 May 2
- **Authors**: Nasaruddin, Rony Kurnia
- **PDF**: https://ieeexplore.ieee.org/document/7519426
- **Abstract**: A cooperative communication system is an effective way to deal with the multipath fading in a wireless channel. However, the data sent from a source to the relay or the destination may experience some losses or corruptions during the transmission, causing error bits. Those errors can degrade the system's performance. In order to detect and correct the errors, it is important to apply a channel coding to the cooperative networks. In this paper, the Hamming Coding for multi-relay cooperative quantize and forward (QF) networks is proposed. The Hamming Codes are the simplest linear codes that can be implemented with low complexity in the proposed networks. The proposed system model is presented with the analytic expressions of the networks. Moreover, the system performance is simulated using the computer simulation in terms of bit error rate (BER). It is shown in the simulation results that the Hamming Code could significantly improve the network's performance when the number of relays is increased. The network's performance is also increased by using high quantization levels in the QF relays. Furthermore, it is found that the performance of the multi-relay QF networks with Hamming Code is better than those of the multi-relay amplify and forward (AF) networks with and without the Hamming Coding. It is concluded that the performance of multi-relay QF network is improved by the use of Hamming Code as well as the advantage of quantization levels.

## Review on enhanced data rate receiver design using efficient modulation techniques for underwater acoustic communication

- **Status**: ❌
- **Reason**: 수중음향 OFDM 변조 서베이, 떼어낼 LDPC 디코더/HW 기법 없음
- **ID**: ieee:7831653
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: M. G. Ravi Kumar, Mrinal Sarvagya
- **PDF**: https://ieeexplore.ieee.org/document/7831653
- **Abstract**: Underwater acoustic (UWA) transmission schemes are an interesting area of communication research, in which achieving high data rate, low latency and high throughput is challenging task. In this paper, we trying to provide a survey on various efficient techniques which that includes channel estimation, channel equalization and efficient modulation schemes to achieve high data rate in the receiver using OFDM scheme for underwater acoustic communication. We are focusing for designing a block-by-block iterative receiver for underwater MIMO-OFDM that includes channel estimation with highly efficient modulation techniques for underwater acoustic communication. Also we found some efficient modulation techniques like BPSK, DPSK and 16-QAM for underwater channel communication which are best in achieving high data rate by considering more subcarriers.

## Transmission of correlated sources over non-orthogonal Gaussian MACs

- **Status**: ❌
- **Reason**: 상관 소스 JSCC(소스-채널 결합) over Gaussian MAC, LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:7503842
- **Type**: conference
- **Published**: 23-27 May 
- **Authors**: Jiguang He, Iqbal Hussain, Markku Juntti +1
- **PDF**: https://ieeexplore.ieee.org/document/7503842
- **Abstract**: We investigate the transmission of multiple correlated binary sources to a single destination over non-orthogonal Gaussian multiple access channels (MACs). By considering a binary codebook, we derive the admissible rate regions of the two-source Gaussian MAC. It is demonstrated that the admissible rate region increases as the correlation between the sources increases. Furthermore, we develop an iterative joint source channel decoding scheme based on systematic irregular low-density parity-check codes by exploiting the correlation between the two sources. The constituent decoders corresponding to each source are implemented in parallel via local iterations, exchanging extrinsic information with each other during the global iterations. Simulation results are provided to verify the performance improvement of the transmission of correlated sources compared to its independent sources counterpart.

## Efficient transmission schemes for correcting insertions/deletions in DPPM

- **Status**: ❌
- **Reason**: DPPM insertion/deletion 채널용 watermark+Viterbi 트렐리스 기법, LDPC는 후단 베이스라인 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7511112
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Weigang Chen, Yuan Liu
- **PDF**: https://ieeexplore.ieee.org/document/7511112
- **Abstract**: Differential pulse-position modulation (DPPM) shows significant power and bandwidth efficiency in wireless optical communications and does not need symbol synchronization, but suffers from serious insertion/deletion errors if the low-complexity symbol-by-symbol detection is used. In this paper, the DPPM transmission scheme combining the watermark with the low-density parity-check (LDPC) code is proposed. Specifically, the equivalent source and channel models are developed to disclose the insertion/deletion characteristics. Then, trellis graphs are built based on the watermark and the equivalent source and channel models. On the trellis, Viterbi algorithm can be executed to convert the insertions/deletions to small number of substitutions, which can be finally recovered using LDPC codes. Simulation results reveal that the scheme performs well with the insertions and deletions introduced by low complexity symbol-by-symbol detection. The proposed method lays the feasibility of the practical applications of DPPM considering the complexity and significant performance.

## Serial quasi-primitive BC-BCH codes for NAND flash memories

- **Status**: ❌
- **Reason**: NAND 대상이나 BC-BCH(비-LDPC) 부호 설계, LDPC는 비교 대상일 뿐 떼어낼 LDPC 기법 없음
- **ID**: ieee:7510725
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Daesung Kim, Jeongseok Ha
- **PDF**: https://ieeexplore.ieee.org/document/7510725
- **Abstract**: In this work, we study high-rate error-control systems with serial quasi-primitive block-wise concatenated Bose-Chaudhuri-Hocquenghem (BC-BCH) codes for storage devices using multi-level per cell (MLC) NAND flash memories. The system targets at achieving a strong error-correcting capability when only hard-decision channel outputs are available. Error-rate performance of the proposed system is compared with those of systems based on various coding schemes including LDPC codes.

## Physical-layer network-coding over block fading channels with root-LDA lattice codes

- **Status**: ❌
- **Reason**: lattice codes(Construction A)+물리계층 네트워크코딩, root-LDPC는 페이딩 다이버시티용 lattice 구성 요소이며 NAND 바이너리 LDPC ECC로 떼어낼 디코더/HW 기법 없음
- **ID**: ieee:7511113
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Ping-Chung Wang, Yu-Chih Huang, Krishna R. Narayanan +1
- **PDF**: https://ieeexplore.ieee.org/document/7511113
- **Abstract**: We consider the problem of physical-layer network coding when the channel exhibits block fading. Specifically, we focus on the use of lattice codes in a compute-and-forward framework for realizing physical-layer network coding. We construct a novel lattice ensemble called the root-Low-Density Construction-A (root-LDA) ensemble which uses Construction A with root-low-density parity check (LDPC) codes. Using extensive simulations, we show that the proposed lattice codes exhibit full diversity when used over the block fading channels. In addition, their performance is comparable to the performance of LDA lattice codes optimized by the progressive edge growth algorithm over the additive white Gaussian noise AWGN channel. This suggests that root-LDA lattice codes provide a robust solution to the problem of implementing physical layer network coding over fading channels.

## Polar codes for noncoherent MIMO signalling

- **Status**: ❌
- **Reason**: polar code+Grassmannian 신호설계(비코히어런트 MIMO), polar 디코더는 부호의존적이고 바이너리 LDPC BP 이식성 없음
- **ID**: ieee:7511290
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Philip R. Balogun, Ian D. Marsland, Ramy H. Gohary +1
- **PDF**: https://ieeexplore.ieee.org/document/7511290
- **Abstract**: Polar codes, ever since their introduction, have been shown to be very effective for various wireless communication channels. This together with their relatively low implementation complexity has made polar codes an attractive coding scheme for wireless communications. On the other hand, within the realm of non-coherent wireless MIMO communication, Grassmannian signalling has been shown to approach the ergodic capacity of frequency-flat block fading channels. In this paper, a novel methodology for designing polar codes that works effectively with Grassmannian signalling and a novel set partitioning algorithm for Grassmannian constellations are proposed. We compare the error rate performance of our design with that of existing schemes and show that a gain of over 1 dB over the previously known best technique, which is based on turbo codes, is possible, at much lower decoding complexity.

## Jointly optimized quadrature amplitude modulation

- **Status**: ❌
- **Reason**: QAM 변조 최적화, turbo code로 검증한 변조/coded modulation 연구이며 LDPC ECC 기법 없음
- **ID**: ieee:7511271
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Sung-Joon Park
- **PDF**: https://ieeexplore.ieee.org/document/7511271
- **Abstract**: Quadrature amplitude modulation has been widely used for high-speed data transmission in modern digital communication systems. In this work, a generalized quadrature amplitude modulation which relaxes the constraint of square lattice is suggested to improve the joint performance of modulation and coding. Bitwise log-likelihood ratios and input signal-to-noise ratios for decoder are analyzed and the strategy minimizing the probability of decoding error is investigated. The analytical argument is consolidated by conducting simulations with a turbo code. According to results, the proposed scheme presents a power gain which depends on Es/N0 and a modulation order.

## Four-dimensional constellations for dual-polarized satellite communications

- **Status**: ❌
- **Reason**: 위성통신 4D 컨스털레이션 설계, 변조 도메인 연구로 떼어낼 LDPC 기법 없음
- **ID**: ieee:7511493
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Nicolò Mazzali, Farbod Kayhan, R Bhavani Shankar Mysore
- **PDF**: https://ieeexplore.ieee.org/document/7511493
- **Abstract**: In this paper, we investigate the performance of constellations optimized for transmissions in dual-polar mobile satellite applications. These four-dimensional constellations (inphase and quadrature per polarization) are designed for joint transmission over the two polarizations. Such constellations enhance the reliability of the system by providing certain redundancy into their design. Their performance is compared with transmission of independent 2D constellations over each polarization. As performance metrics, the pragmatic achievable mutual information and the bit error rate have been considered. The gains serve to indicate the need to further investigate 4D constellation design and its application in dual-polar MIMO systems.

## Enhanced spatial multiplexing — A novel approach to MIMO signal design

- **Status**: ❌
- **Reason**: MIMO 공간다중화 신호설계, 부호화 ECC 기여 없음
- **ID**: ieee:7511274
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Chien-Chun Cheng, Hikmet Sari, Serdar Sezginer +1
- **PDF**: https://ieeexplore.ieee.org/document/7511274
- **Abstract**: In this paper, we present a new type of Spatial Multiplexing (SMX) schemes based on the multiple signal constellation concept, which was recently introduced in the context of Spatial Modulation (SM) by the present authors. The proposed technique, which we refer to as Enhanced SMX or E-SMX, conveys information not only by the transmitted symbols, but also by the antenna and constellation combinations used. In addition to the primary constellation, these schemes make use of one or more specifically-designed secondary constellations, obtained through geometric interpolation in the signal constellation plane. We present the general concept and describe specific schemes for different numbers of transmit antennas and using 16QAM as primary modulation. Our analysis and the simulation results indicate that the proposed schemes provide a significant performance gain over conventional SMX.

## BICM-ID in two-way relaying communications

- **Status**: ❌
- **Reason**: BICM-ID 양방향 중계 통신 응용, XOR 네트워크코딩+반복디코딩으로 LDPC ECC 기여 없음
- **ID**: ieee:7511175
- **Type**: conference
- **Published**: 22-27 May 
- **Authors**: Hongzhong Yan, Ha H. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/7511175
- **Abstract**: This paper studies the technique of bit-interleaved coded modulation with iterative decoding (BICM-ID) in a two-way relaying communication system. Iterative decoding based on the quaternary code representation is adopted at the relay for the multiple access (MA) phase. An upper-bound of the bit error probability (BEP) under the error-free (EF) feedback assumption for BICM-ID in the MA phase is obtained. Based on the obtained EF bound of the BEP, it is found that the multiple-access interference (MAI) is successfully eliminated by performing the iterative decoding and XOR based network coding at the relay. Simulation results are provided to corroborate the analysis and demonstrate the performance superiority of the proposed framework.

## Hardware decoders for polar codes: An overview

- **Status**: ❌
- **Reason**: polar 코드 HW 디코더 서베이(SC/BP/list) - 비-LDPC 부호 리뷰, 떼어낼 LDPC BP 이식 기법 없음
- **ID**: ieee:7527192
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Pascal Giard, Gabi Sarkis, Alexios Balatsoukas-Stimming +5
- **PDF**: https://ieeexplore.ieee.org/document/7527192
- **Abstract**: Polar codes are an exciting new class of error correcting codes that achieve the symmetric capacity of memoryless channels. Many decoding algorithms were developed and implemented, addressing various application requirements: from error-correction performance rivaling that of LDPC codes to very high throughput or low-complexity decoders. In this work, we review the state of the art in polar decoders implementing the successive-cancellation, belief propagation, and list decoding algorithms, illustrating their advantages.

## A cost-effective approach for ubiquitous broadband access based on hybrid PLC-VLC system

- **Status**: ❌
- **Reason**: PLC-VLC 하이브리드 광대역 접속 시스템 - LDPC 언급 없는 통신 인프라 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:7539178
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Jian Song, Sicong Liu, Guangxin Zhou +6
- **PDF**: https://ieeexplore.ieee.org/document/7539178
- **Abstract**: Visible light communication (VLC) using the light emitting diode (LED) will become an appealing alternative to the radio frequency communication technology for indoor wireless broadband access. However, VLC needs a ubiquitous network as its backbone to avoid becoming an information isolated island. Power line communication (PLC) systems could easily solve the informative problem of VLC while powering the LED lamps at the same time, which is considered as a good partner of VLC for the cost-effective implementation. In this paper, a novel and cost-effective framework of ubiquitous indoor broadband access based on deeply integrated VLC and PLC technology with only low-cost modification to the current infrastructure is therefore proposed. The broadband access network supports duplex transmission through each LED using the decode-and-forward (DF) working mode. This paper will present our recent research progress in this area, including a prototyping of duplex voice communications network based on hybrid PLC and VLC in our lab. Our research and development plan in this area for the near future will also be covered.

## Joint detection and decoding for MIMO systems with polar codes

- **Status**: ❌
- **Reason**: MIMO 결합 검출+polar 디코딩(JDD) - 비-LDPC 부호 + 무선 응용 특이적, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7527195
- **Type**: conference
- **Published**: 22-25 May 
- **Authors**: Junmei Yang, Chuan Zhang, Wenqing Song +2
- **PDF**: https://ieeexplore.ieee.org/document/7527195
- **Abstract**: As well known, the near-optimal K-best detection is popular in multiple-input and multiple-output (MIMO) systems. In this paper, we first propose the joint approaches of K-best detection and polar decoding. For joint detection and decoding (JDD) approach, both hard and soft decisions are considered. The simplified successive cancellation (SSC) decoding is exploited for hard decision, and the successive cancellation list (SCL) decoding is used as soft decision. The system setup for JDD is als o introduced, in which the modulation points across several channels are considered together. Simulation results have demonstrated the performance advantage of the JDD algorithms over the separated ones. For 1/2-rate polar codes, JDD schemes show 50% complexity reduction compared to the separated ones. Furthermore, by employing SSC hard decoding, the JDD algorithm is promising for high-throughput and low-complexity application s.

## Concatenations of systematic polar codes with inner repeat accumulate codes

- **Status**: ❌
- **Reason**: Polar+RA 연접(비-LDPC), 바이너리 LDPC BP로 이식할 기법 없음
- **ID**: ieee:7506571
- **Type**: conference
- **Published**: 21-23 May 
- **Authors**: Hao Ye, Zhi Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7506571
- **Abstract**: Polar codes, proposed by Erdal Arikan, have attracted a lot of interest in the field of channel coding for their capacity-achieving trait as well as their low encoding and decoding complexity of the order O(NlogN) under successive cancellation (SC) decoder. However, there remains one significant drawback, that is, the error correction performance of small and moderate length polar codes is unsatisfactory, especially when compared with low density parity check (LDPC) codes and turbo codes. To this end, We propose a novel concatenation scheme which employs interleaved repeat accumulate (RA) codes as inner codes and systematic polar codes as outer codes. At the end of this paper, we present the simulation results in binary-input additive white Gaussian noise (BI-AWGN) channel with binary phase shift keying (BPSK) modulation, and we observe that, our proposed concatenation scheme significantly outperforms the conventional non-systematic inner polar codes in the high signal-to-noise (SNR) regime.

## Simplified BATS codes for deep space multihop networks

- **Status**: ❌
- **Reason**: 심우주 멀티홉용 BATS(fountain/네트워크코딩) 부호, 비-LDPC erasure/fountain 계열로 제외
- **ID**: ieee:7560372
- **Type**: conference
- **Published**: 20-22 May 
- **Authors**: Zhao Huakai, Dong Guangliang, Li Haitao
- **PDF**: https://ieeexplore.ieee.org/document/7560372
- **Abstract**: Deep space multihop networks suffer many challenges such as long propagation delay, high error rate and frequent disturption. Channels above these networks are supposed as multihop erasure channels, on which BATS codes work well. BATS codes is a coding scheme that consists of an outer code and an inner code. The outer code is a matrix generation of a fountain code. It works with the inner code that comprises random linear network coding at the intermediate network nodes. BATS codes are suitable for deep space multihop networks, but have complicated coding rule. This paper proposes a simplified BATS codes. Simulations and analyses are made to evaluate the performance of the simplified BATS codes.

## Performance analysis of concatenated codes for different channels

- **Status**: ❌
- **Reason**: SPC+BCH+LDPC concatenated 부호 BER 비교일 뿐, 새 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:7807917
- **Type**: conference
- **Published**: 20-21 May 
- **Authors**: N K Sharanya, S Jayashree
- **PDF**: https://ieeexplore.ieee.org/document/7807917
- **Abstract**: Forward Error Correction codes are required to remove errors such as noise, crosstalk etc that transpire in communication channel. In this paper, we propose a concatenated (Single Parity Check, BCH and Low Density Parity Check) coding method to remove the errors and improve the efficiency of the system. Simulation results shows that Single Parity Check method along with BCH and Low Density Parity Check gives better results. Performance of these coding methods in different channels such as AWGN, Rayleigh and Rician channels are also simulated. SPC method having simple encoding and decoding mechanism does not give good BER. LDPC in contrast to BCH achieves higher performance and better error correction capability.

## Exploiting latency variation for access conflict reduction of NAND flash memory

- **Status**: ❌
- **Reason**: NAND I/O 스케줄링/지연변이 활용일 뿐 LDPC ECC 디코더/코드 기법 없음
- **ID**: ieee:7897088
- **Type**: conference
- **Published**: 2-6 May 20
- **Authors**: Jinhua Cui, Weiguo Wu, Xingjun Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/7897088
- **Abstract**: NAND flash memory has been widely used in storage systems by offering greater read/write performance and lower power consumption than mechanical hard drives. Recently, the tradeoff between endurance, write speed, and read speed has been exploited from many ways for I/O performance improvement, which also induce the read/write latency variation. In this paper, the latency variation is exploited in I/O scheduling for access characteristic guided read and write latency minimization. First, with the understanding of the relationship among read latency, write latency and raw bit error rates (RBER), different ways to exploit the relationship for read and write latency reduction is discussed. Then, an I/O scheduling scheme is proposed by using hotness and retention age of accessed data to determine the speed of writes or reads, giving scheduling priority to fast writes and fast reads for conflict reduction. Experiments with various traces reveal that the proposed technique achieves significant read and write performance improvements.

## Iterative Detection using MMSE-PIC Demapping for MIMO-GFDM Systems

- **Status**: ❌
- **Reason**: MIMO-GFDM MMSE-PIC 검출, WiMax LDPC는 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:7499256
- **Type**: conference
- **Published**: 18-20 May 
- **Authors**: Maximilian Matthe, Dan Zhang, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/7499256
- **Abstract**: Diverse requirements are foreseen for the 5G cellular system and new waveforms are being researched for the physical layer (PHY), where the non-orthogonal Generalized Frequency Division Multiplexing (GFDM) is one candidate. Its inherent self-interference makes receiver design challenging, particularly when besides inter-carrier interference (ICI) and inter-symbol interference (ISI) also inter-antenna interference (IAI) occurs, as in systems that employ spatial multiplexing (SM) to increase the throughput. To encounter this interference, we apply the prominent minimum mean squared error with parallel interference cancellation (MMSE-PIC) iterative receiver structure to GFDM, and provide a formulation that is suitable for a low-complexity implementation. We analyze the decoding performance employing a well-known current WiMax LDPC code. The proposed demapping algorithm can be implemented with complexity that scales linearly with the number of subcarriers of the system. Analysis of information transfer characteristics shows that the MMSE-PIC demapper for GFDM exhibits potential to outperform the OFDM demapper with a matching code, however, simulations of frame error rate (FER) show inferior performance of GFDM. These results emphasize the importance of a joint waveform and code design in order to exploit the full potential of the MMSE-PIC receiver structure for GFDM.

## BP-based approximation methods for rateless codes

- **Status**: ❌
- **Reason**: rateless/LT(fountain) 부호용 BP 근사 — fountain 부호는 제외 대상이며 새 바이너리 LDPC BP 기법 아님
- **ID**: ieee:7496135
- **Type**: conference
- **Published**: 16-19 May 
- **Authors**: Cenk Albayrak, Kadir Türk
- **PDF**: https://ieeexplore.ieee.org/document/7496135
- **Abstract**: In this letter, belief propagation (BP) based approximation methods for low density parity check (LDPC) codes are adapted to the Luby transform (LT) soft decoder structure in order to reduce its computational complexity. The bit error rate (BER) performances of the algorithms over the binary input additive white Gaussian noise (BIAWGN) channel are obtained by both theoretically and simulations. For theoretical analysis, the Monte-Carlo density evolution (MC-DE) method is used. In addition, computational complexity analyzes of methods are presented. Results show that the computational complexity can be significantly decreased with a limited performance loss cost.

## Non-binary LDPC codes over finite division near rings

- **Status**: ❌
- **Reason**: 비이진 LDPC(near ring/Min-Max)—바이너리 한정 원칙 제외
- **ID**: ieee:7500492
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Matthias Korb, Andrew Blanksby
- **PDF**: https://ieeexplore.ieee.org/document/7500492
- **Abstract**: It is almost always assumed that the algebraic structure underlying non-binary Low-Density Parity-Check (LDPC) codes are Finite Fields. However, when considering non-binary LDPC belief-propagation (BP) decoding, Finite Fields are actually over constrained. In this contribution, we discuss the minimal requirements of the algebraic structure used for non-binary LDPC decoding which we denote Finite Division Near Ring over a Subtractive Near Group. To verify the requirements, a general Min-Max decoding algorithm is derived that incorporates any algebraic structure fulfilling this minimal requirement set. It is shown that by relaxing the mathematical constraints, the decoding performance of non-binary LDPC codes can be incrementally improved compared to a Finite-Field-based LDPC code without any additional hardware cost.

## Optimized constellation design for P-LDPC coded multi-color visible light communications

- **Status**: ❌
- **Reason**: VLC용 컨스텔레이션 설계, LDPC는 베이스라인—떼어낼 ECC 기법 없음
- **ID**: ieee:7500474
- **Type**: conference
- **Published**: 16-18 May 
- **Authors**: Chengjun Tang, Ming Jiang, Hong Shen +1
- **PDF**: https://ieeexplore.ieee.org/document/7500474
- **Abstract**: In this paper, we advocate a novel constellation design methodology for multi-color visible light communication (VLC) systems deploying protograph-based low-density parity-check (P-LDPC) codes. We utilize the protograph-based extrinsic information transfer (PEXIT) analysis to evaluate the coded system performance accurately and employ the differential evolution algorithm for the optimal constellation design. Both numerical analyses and simulations show performance gains of more than 0.9 dB and demonstrate that our constellation design exhibits much better performance than the conventional ones such as the commonly used minimum Euclidean distance maximization design.

## Adaptive granular HARQ LDPC-based coding for secrecy enhancement in wiretap channels

- **Status**: ❌
- **Reason**: wiretap 보안/HARQ LDPC, 보안 도메인 원칙 제외; LLR 기반 재전송은 보안 정보누설 최소화용이라 NAND ECC 이식 기법 아님
- **ID**: ieee:7726710
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Ahmadreza Amirzadeh, Mohamed Haj Taieb, Jean-Yves Chouinard
- **PDF**: https://ieeexplore.ieee.org/document/7726710
- **Abstract**: In this work, reliable and secure transmission over generic-Gaussian wiretap channel model is investigated. An Adaptive Granular Hybrid Automatic Repeat reQuest (AG-HARQ) protocol is proposed which tries to minimize the required rate for successful decoding by the legitimate parties while amplifying the privacy by minimizing the information leakage to a wiretapper. In the case of LDPC decoding failure at the legitimate receiver (Bob), a retransmission is requested until correct decoding or until the maximum number of transmitted packets is reached. As soon as Bob is able to correctly decode the LDPC codeword, the retransmissions are stopped to avoid any additional bits leakage to the eavesdropper (Eve). In our proposed method, to minimize the leakage, a confidence level index, Cj, for correct decoding is defined as the mean of absolute value of the Log-Likelihood Ratio (LLR). In the case of failure, only the sub-packets with the smallest Cj values will be retransmitted since they represent the most unreliable information sub-packets. Frame Error Rate (FER) is used as a metric to show the effectiveness of the proposed method.

## A New Architecture for High Speed, Low Latency NB-LDPC Check Node Processing for GF(256)

- **Status**: ❌
- **Reason**: GF(256) 비이진 LDPC check node HW — 비이진 LDPC는 제외 대상
- **ID**: ieee:7504085
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: V. Rybalkin, P. Schlafer, N. Wehn
- **PDF**: https://ieeexplore.ieee.org/document/7504085
- **Abstract**: Non-binary low-density parity-check codes have superior communications performance compared to their binary counterparts. However, to be an option for future standards, efficient hardware architectures are mandatory. State-of-the-art decoding algorithms result in architectures suffering from low throughput and high latency. The check node function accounts for the largest part of the decoders overall complexity. To the best of our knowledge, we propose the first architecture for high speed, low latency Non-Binary Low-Density Parity-Check Check Node processing for GF(256). It has state-of-the-art communications performance while largely reducing the hardware complexity. The presented architecture has a 3.3 times higher area efficiency, increases the energy efficiency by factor 2.5 and reduces the latency by factor of 5.5 compared to the first implementation of Check Node for GF(256) based on the state-of-the-art FWBW scheme that was also implemented in the scope of this work.

## Design of Short Quasi-Cyclic LDPC Codes for Next Generation Broadcast Wireless Systems

- **Status**: ❌
- **Reason**: 방송무선용 QC-LDPC 부호셋 선택 — 무선 표준 특이, 신규 구성기법 미기술
- **ID**: ieee:7504191
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Fang Wang, Yajun Kou, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/7504191
- **Abstract**: Chinese next generation broadcast wireless (NGB-W) systems are aimed to provide high-speed, ubiquitous, and secure broadcast services and tri-play services to massive users. New terrestrial broadcast techniques are needed to support these services in NGB-W systems. In this paper, a new set of quasi-cyclic (QC) low density parity check (LDPC) codes with a moderate code length and a wide operation range are proposed for NGB-W systems. It is shown by simulations that the perfor-mance of the proposed LDPC codes is much better than that of the LDPC codes used in the second generation television broad-cast of digital video broadcasting (DVB-T2/NGH) systems.

## Modulation assisted preprocessing for non-binary LDPC decoding with extended min-sum algorithm

- **Status**: ❌
- **Reason**: non-binary LDPC EMS 전처리, 비이진 LDPC 제외
- **ID**: ieee:7726728
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Tianqing Wu, Hong-Chuan Yang, Jingwen Yan
- **PDF**: https://ieeexplore.ieee.org/document/7726728
- **Abstract**: We propose a modulation assisted preprocessing scheme to reduce the computational complexity of non-binary LDPC decoding. With the proposed scheme, the received signal is directly mapped onto a truncated symbol vector through table lookup. The mapping table can be built off-line based on the characteristics of the constellation structure. The receiver needs only to calculate and, if necessary, rank the reliability of the symbols in the truncated vectors, which avoids unnecessary reliability calculation and ranking during on-line operation. The complexity analysis shows that the proposed preprocessing scheme leads to much lower computational complexity, in terms of ranking and addition operations, while offering the same error rate performance as conventional EMS preprocessing scheme.

## Construction of High-Rate Generalized Concatenated Codes for Applications in Non-Volatile Flash Memories

- **Status**: ❌
- **Reason**: 플래시용이나 BCH+RS 일반연접부호(비-LDPC), 이식할 LDPC 디코더 기법 없음
- **ID**: ieee:7493571
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Jens Spinner, Mohammed Rajab, Jurgen Freudenberger
- **PDF**: https://ieeexplore.ieee.org/document/7493571
- **Abstract**: This work proposes a construction for high-rate generalized concatenated (GC) codes. The proposed codes are well suited for error correction in flash memories for high reliability data storage. The GC codes are constructed from inner nested binary Bose-Chaudhuri-Hocquenghem (BCH) codes and outer Reed-Solomon (RS) codes. For the inner codes we propose extended BCH codes, where we apply single parity-check codes in the first level of the GC code. This enables high-rate codes.

## LDPC-Coded Index-Modulation Aided OFDM for In-Vehicle Power Line Communications

- **Status**: ❌
- **Reason**: 차량 PLC OFDM-IM 응용, LDPC 부수 사용; soft-detection은 검출기측이고 떼어낼 LDPC 디코더 기여 없음
- **ID**: ieee:7504318
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Hongming Zhang, Lie-Liang Yang, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/7504318
- **Abstract**: The recently developed orthogonal frequency-division multiplexing relying on index modulation (OFDM-IM) is adopted to the in-vehicle power line communications (PLCs) in order to combat the deleterious effects of frequency-selective fading and impulsive noise, whilst improving the energy efficiency of data communications. Furthermore, the low density parity check (LDPC) coding is invoked to further enhance the reliability of in-vehicle PLCs, which is of particular importance in light-weight airborne vehicles. For aiding LDPC decoding, a reduced complexity soft-decision detection scheme is proposed. The performance of the LDPC-coded OFDM-IM system is studied by simulation, when assuming communications over in-vehicle PLC channels. Our studies show that LDPC-coded OFDM-IM is capable of combating frequency-selective fading, mitigating impulsive noise, as well as striking a compelling trade-off between the spectral efficiency and energy efficiency for in-vehicle PLCs.

## Design of LDPC Coded CPM over Burst-Error Channels

- **Status**: ❌
- **Reason**: LDPC coded CPM — LDPC는 베이스라인, 초점은 CPM 복조, 떼어낼 ECC 기법 없음
- **ID**: ieee:7504189
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Chunhui Shen, Li Bing, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7504189
- **Abstract**: In the paper, a class of LDPC coded continuous phase modulation (CPM) systems is proposed for reliable communication over burst-error channels. A series of binary LDPC codes with code rates 1/4, 1/2 and 2/3 are chosen for binary and quaternary CPM schemes. A non-recursive decomposition of CPM is incorporated to eliminate the error propagation caused by burst errors. To reduce the complexity, an improved demodulation algorithm for noncoherent soft in soft out (N-SISO) is considered. Simulation results show that the proposed LDPC coded CPM offers a better error performance and is abler to recover the transmitted information under severe burst errors than current systems.

## Finite Length Design of Precoded EWF Codes

- **Status**: ❌
- **Reason**: BEC용 precoded EWF fountain 부호 — fountain/erasure, LDPC는 precode 베이스라인
- **ID**: ieee:7504247
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Lei Yuan, Huaan Li, Yi Wan
- **PDF**: https://ieeexplore.ieee.org/document/7504247
- **Abstract**: Novel precoded Expanding Window Fountain (EWF) codes, based on low rate low-density parity-check (LDPC) codes, are investigated for finite message length over binary erasure channels (BECs). The proposed codes are obtained by utilizing low rate LDPC codes as precodes and degree distributions with high intermediate symbol recovery rate for EWF codes. Simulation results show that, compared with conventional precoded EWF codes, our proposed codes have better performance in the scenarios of small and moderate message lengths over the BEC.

## Graph-Based Decoding for High-Dense Vehicular Multiway Multirelay Networks

- **Status**: ❌
- **Reason**: 코드-온-그래프 랜덤액세스 무선 네트워크에 SIC 디코딩; LDPC는 구조 비유일 뿐 NAND ECC로 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7504263
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Khoirul Anwar
- **PDF**: https://ieeexplore.ieee.org/document/7504263
- **Abstract**: Densely deployed wireless networks is one of the most important solutions for spectrum shortage expected by 2020 with a huge economic impact. This paper proposes decoding schemes for high- dense vehicular multiway multirelaying (HDV-MWMR) systems comprising multiple multiway relays to serve huge number of users or devices. Due to the nature of huge number, instead of using perfect scheduling, we consider coded random access schemes, where all users transmit their messages uncoordinatedly. Although the transmission is random, the network structures still can be seen as codes-on-the-graph, resembling Low Density Parity Check (LDPC) codes structure, expected to provide an additional gain. The theoretical network capacity bound for HDV-MWMR systems exploiting multiple multiway relays is derived and confirmed via extrinsic information transfer (EXIT) chart analysis and computer simulations. To achieve the network capacity bound, we propose simple decoding schemes based on successive interference cancellation over a sparse graph involving multiple multiway relays. Suitable degree distributions for Rayleigh fading channels are investigated. The results confirm that multiple relays help both on (i) improving the throughput performances, and (ii) capturing the network diversity, which are highly required for future wireless networks.

## Comparison of Interference Cancellation Schemes for Non-Orthogonal Multiple Access System

- **Status**: ❌
- **Reason**: NOMA 간섭제거(repeat-accumulate 부호) — 비-LDPC 무선 검출, 이식 기법 없음
- **ID**: ieee:7504172
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Guanghui Song, Xianbin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7504172
- **Abstract**: Three potential interference cancellation schemes are compared for the application to a non-orthogonal multiple access communication system. One is the conventional hard successive interference cancellation (SIC) scheme based on independent single-user decodings. The other two, proposed in this paper, are a soft-in soft-out parallel interference cancellation (SISO-PIC) and a hybrid interference cancellation (HIC). The SISO-PIC is an improved joint iterative multi-user detection scheme, which has lower complexity than the prevalent multi-user detection. The HIC combines the advantages of the above two schemes to permit users to be successively processed by a SISO-PIC window according to their receive power levels. A comprehensive comparison is given for these three schemes in aspects of error propagation, detection delay, and complexity when a practical channel code, repeat-accumulate code, is employed. Numerical results show that HIC is a trade-off scheme of the three aspects.

## Hybrid Beamforming with Time Delay Compensation for Millimeter Wave MIMO Frequency Selective Channels

- **Status**: ❌
- **Reason**: mmWave MIMO 하이브리드 빔포밍, LDPC 무관
- **ID**: ieee:7504275
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Gaojian Wang, Jiaxin Sun, Gerd Ascheid
- **PDF**: https://ieeexplore.ieee.org/document/7504275
- **Abstract**: The fading channel in mmWave communications has a very high chance to be frequency selective owing to the large transmission bandwidth. To overcome the frequency selectivity we propose a novel method, namely RF beamforming with time delay compensation. Simultaneously, baseband precoder at the transmitter side and the combiner at the receiver side are employed to maximize the capacity of the system. For effectively flattening the channel by beamforming on both sides, it is necessary to separate the individual rays. Motivated by achieving the best case beam separation, a signal-to-interference ratio (SIR) constrained capacity maximization algorithm is proposed in this paper. We also study the influence of the parameters such as the number of antennas at the transmitter side and the SIR threshold on the capacity and the system performance. Finally, the proposed method is validated by providing numerical examples by means of simulation.

## Low-Delay Transmission Scheme Based on LT Code Employing Hybrid Decoding

- **Status**: ❌
- **Reason**: LT(fountain) 코드 하이브리드 디코딩, 비-LDPC fountain/erasure로 원칙 제외
- **ID**: ieee:7504331
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Qixian Zhang, Xuan Feng, Guixing Cao +2
- **PDF**: https://ieeexplore.ieee.org/document/7504331
- **Abstract**: Satellite communication plays an important role in the ubiquitous global communication. However, for a long time, the communication provided by satellite suffers from serious signal attenuation and transmission delay. Conventional techniques such as HARQ couldn't provide timely service unless powerful channel codes are used. Once channel code fails, retransmission will be inevitable, and unbearable delay may be incurred. Fortunately, things started to change when Luby proposed the landmark LT code. As a practical implementation of fountain code, LT code avoids frequent feedback during the transmission. However, due to the high packet error rate (PER), the original LT code couldn't work stably in satellite communication. In this paper, we propose a novel hybrid decoding scheme for LT code. It consists of two decoding procedures: normal decoding using BP algorithm and mining decoding. The idea behind mining decoding is to release as many corrupted original packets as possible and combine the "identical" ones as in HARQ. Actually we develop three types of packet mining techniques to make a tradeoff between performance and computation complexity. The final simulation shows that, the proposed hybrid decoding scheme makes LT code work more stably, and achieves significant advantages over HARQ in terms of delay.

## Performance Advantage of Joint Source-Channel Decoder over Iterative Receiver under M-ary Differential Chaotic Shift Keying Systems

- **Status**: ❌
- **Reason**: DCSK JSCD vs IR 비교, 소스-채널 결합으로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7504399
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Yibo Lyu, Lin Wang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/7504399
- **Abstract**: In order to improve the error performance of M-ary differential chaotic shift keying (DCSK) systems over multi-path fading channel, two types of iterative structures have been employed in receiver design. One is joint source-channel decoder (JSCD), the other is iterative receiver (IR). Although several works have separately addressed the advantages of IR and JSCD, it is not clear which design provides more iterative gain for M-ary DCSK systems over multi-path fading channels. In this work, we employ the extrinsic information transfer (EXIT) chart technique to analyze the iteration behavior of JSCD and IR. Simulation results suggest that with enough source redundancy, JSCD outperforms IR under M-ary DCSK systems over multi-paths fading channels.

## On the Simultaneous Exploitation of Multiple Source-to-Relay Channels in Buffer-Aided Two-Hop Cooperative Networks

- **Status**: ❌
- **Reason**: 버퍼-에이디드 협력 릴레이 프로토콜, 부호화 무관
- **ID**: ieee:7504380
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Miharu Oiwa, Shinya Sugiura
- **PDF**: https://ieeexplore.ieee.org/document/7504380
- **Abstract**: Motivated by the recent buffer-aided cooperative protocols that select the single best link at each time slot, in this paper we introduce additional design degree of freedom into them, by simultaneously exploiting broadcast channels between the source node and the multiple buffer- aided relay nodes. More specifically, our proposed scheme is designed to allow multiple relay nodes to receive a specific source packet through source-to-relay broadcast channels, hence resulting in multiple copies of the source packet, which are stored in buffers of the relay nodes. As the results, our proposed protocol is capable of reducing the overhead required for monitoring the available links and the end-to-end packet delay, in comparison to the conventional buffer-aided cooperative protocols, while attaining a high diversity order comparable to that of the max-link protocol.

## Code-Aided Joint Carrier Phase Estimation and Ambiguity Resolution for APSK Signals

- **Status**: ❌
- **Reason**: APSK 반송파 위상추정/모호성해결 — 무선 응용 특이, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7504164
- **Type**: conference
- **Published**: 15-18 May 
- **Authors**: Desheng Shi, Nan Wu, Hua Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7504164
- **Abstract**: A maximum likelihood-based code-aided joint carrier phase estimation and ambiguity resolution algorithm is proposed for coded amplitude and phase shift keying (APSK) signals. The proposed estimator iteratively uses the a posteriori probability of coded bits obtained from the channel decoder to improve the performance of phase estimation and ambiguity resolution. Two initialization schemes are employed for systems with and without pilot symbols, which reduce the number of initial phase values required to bootstrap the iterative estimation algorithm. Compared with the existing estimators, simulation results demonstrate the performance improvement of the proposed algorithm in both mean-squared estimation error and bit error rate with lower computational complexity.

## High data rate link modulation and coding scheme modeling

- **Status**: ❌
- **Reason**: PSK+Reed-Solomon 위성 변복조(비-LDPC) — 제외
- **ID**: ieee:7491793
- **Type**: conference
- **Published**: 12-14 May 
- **Authors**: Alexander Bakhtin, Anastasia Semenova, Alexey Solodkov
- **PDF**: https://ieeexplore.ieee.org/document/7491793
- **Abstract**: This paper shows the results of simulation of high spectral efficiency modulation and coding scheme (MSC) which consist of modulation PSK-16+4PCM and error-correction Reed-Solomon code in comparison with other high spectral efficiency schemes for different radio link signal distortion ways. Proposed MSC show close result with PSK-64 with FEC and in comparison with QAM-64 with FEC proposed MSC showed faster performances degradation in non-ideal transmission conditions. But overall due the inherent features like low envelope amplitude variation and simple demodulation algorithm with moderate hardware complexity MSC PSK-16+4PCM+RS(253,244,13) can be applied in high-speed satellite radio downlink effectively.

## A low complexity hardware for compressive sensing matrix generation

- **Status**: ❌
- **Reason**: LDPC 패리티검사를 압축센싱 측정행렬 생성에 쓰는 HW로 채널 ECC 디코더/코드 기법 아님
- **ID**: ieee:7585600
- **Type**: conference
- **Published**: 10-12 May 
- **Authors**: Mohammad Fardad, Sayed Masoud Sayedi
- **PDF**: https://ieeexplore.ieee.org/document/7585600
- **Abstract**: In this paper a low complexity hardware is designed to generate a deterministic matrix for compressive sensing systems. The construction of the matrix is based on the connection between the parity check matrix of LDPC codes and the measurement matrix of compressive sensing. For efficient hardware realization, a geometric approach to the construction of LDPC codes is used for matrix generation on the fly without requiring a lot of storage. The performance of generated matrix is approved under ℓ1-minimization and OMP recovery algorithms, and it performs comparably to the corresponding random matrix. The described hardware has been implemented on a Xilinx Spartan 6 FPGA.
