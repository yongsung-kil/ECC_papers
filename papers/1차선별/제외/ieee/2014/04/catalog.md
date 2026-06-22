# IEEE Xplore — 2014-04


## Spatially-Coupled LDPC Codes for Decode-and-Forward Relaying of Two Correlated Sources over the BEC

- **Status**: ❌
- **Reason**: JSCC/네트워크코딩 릴레이용 bilayer SC-LDPC, BEC 비대칭 채널 — 떼어낼 NAND ECC 디코더/HW/구성 기여 없음, JSCC 베이스라인
- **ID**: ieee:6750419
- **Type**: journal
- **Published**: April 2014
- **Authors**: Stefan Schwandter, Alexandre Graell i Amat, Gerald Matz
- **PDF**: https://ieeexplore.ieee.org/document/6750419
- **Abstract**: We present a decode-and-forward transmission scheme based on spatially-coupled low-density parity-check (SC-LDPC) codes for a network consisting of two (possibly correlated) sources, one relay, and one destination. The links between the nodes are modeled as binary erasure channels. Joint source-channel coding with joint channel decoding is used to exploit the correlation. The relay performs network coding. We derive analytical bounds on the achievable rates for the binary erasure time-division multiple-access relay channel with correlated sources. We then design bilayer SC-LDPC codes and analyze their asymptotic performance for this scenario. We prove analytically that the proposed coding scheme achieves the theoretical limit for symmetric channel conditions and uncorrelated sources. Using density evolution, we furthermore demonstrate that our scheme approaches the theoretical limit also for non-symmetric channel conditions and when the sources are correlated, and we observe the threshold saturation effect that is typical for spatially-coupled systems. Finally, we give simulation results for large block lengths, which validate the DE analysis.

## Soft-Decoding-Based Strategies for Relay and Interference Channels: Analysis and Achievable Rates Using LDPC Codes

- **Status**: ❌
- **Reason**: relay/interference 채널 soft-DF·soft-IC 정보이론 분석, LDPC는 해석 편의용 — 떼어낼 디코더/HW 기법 없음, 무선응용 특이적
- **ID**: ieee:6679214
- **Type**: journal
- **Published**: April 2014
- **Authors**: Amir Bennatan, Shlomo Shamai, A. Robert Calderbank
- **PDF**: https://ieeexplore.ieee.org/document/6679214
- **Abstract**: We provide a rigorous mathematical analysis of two communication strategies: soft decode-and-forward (soft-DF) for relay channels and soft partial interference-cancelation (soft-IC) for interference channels. Both strategies involve soft estimation, which assists the decoding process. We consider LDPC codes, not because of their practical benefits, but because of their analytic tractability, which enables an asymptotic analysis similar to random coding methods of information theory. Unlike some works on the closely-related demodulate-and-forward, we assume non-memoryless, code-structure-aware estimation. With soft-DF, we develop simultaneous density evolution to bound the decoding error probability at the destination. This result applies to erasure relay channels. In one variant of soft-DF, the relay applies Wyner–Ziv coding to enhance its communication with the destination, borrowing from compress-and-forward. To analyze soft-IC, we adapt existing techniques for iterative multiuser detection, and focus on binary-input additive white Gaussian noise interference channels. We prove that optimal point-to-point codes are unsuitable for soft-IC, as well as for all strategies that apply partial decoding to improve upon single-user detection and multiuser detection, including Han–Kobayashi.

## Performance of Joint Source-Channel Coding Based on Protograph LDPC Codes over Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: JSCC PEXIT 분석(double protograph LDPC) 페이딩 채널 — JSCC 수렴분석, 떼어낼 NAND ECC 구성/디코더 기여 없음
- **ID**: ieee:6763123
- **Type**: journal
- **Published**: April 2014
- **Authors**: Huihui Wu, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/6763123
- **Abstract**: This letter presents a joint protograph extrinsic information transfer (PEXIT) analysis for joint source and channel coding (JSCC) with double protograph-based low-density parity-check (DP_LDPC) codes over single-input multiple-output (SIMO) Rayleigh fading channels. The impacts of source statistics and receive antenna diversity on convergence performance for the JSCC are investigated, and we find that source sparsity plays a more vital role than diversity orders in improving both convergence and error performances under fading environments.

## Block-Wise Concatenated BCH Codes for NAND Flash Memories

- **Status**: ❌
- **Reason**: NAND MLC 대상이나 BCH 연접부호 + 반복 하드/신뢰도 디코딩 — 비-LDPC, LDPC는 비교군일 뿐, 이식할 LDPC BP 기법 없음
- **ID**: ieee:6750421
- **Type**: journal
- **Published**: April 2014
- **Authors**: Sung-gun Cho, Daesung Kim, Jinho Choi +1
- **PDF**: https://ieeexplore.ieee.org/document/6750421
- **Abstract**: In this work, we consider high-rate error-control systems for storage devices using multi-level per cell (MLC) NAND flash memories. Aiming at achieving a strong error-correcting capability, we propose error-control systems using block-wise parallel/serial concatenations of short Bose-Chaudhuri-Hocquenghem (BCH) codes with two iterative decoding strategies, namely, iterative hard-decision decoding (IHDD) and iterative reliability based decoding (IRBD). It will be shown that a simple but very efficient IRBD is possible by taking advantage of a unique feature of the block-wise concatenation. For tractable performance analysis and design of IHDD and IRBD at very low error rates, we derive semi-analytic approaches. The proposed error-control systems are compared with various error-control systems with well-known coding schemes such as a product code, multiple BCH codes, a single long BCH code, and low-density parity-check codes in terms of page error rates, which confirms our claim: the proposed error-control systems achieve good tradeoffs between error-performance and complexity as compared to the traditional schemes and is also very favorable for implementation.

## Secure Communications with Untrusted Secondary Nodes in Cognitive Radio Networks

- **Status**: ❌
- **Reason**: 인지무선 보안 협력통신 정보이론; LDPC ECC 기법 없음
- **ID**: ieee:6747289
- **Type**: journal
- **Published**: April 2014
- **Authors**: Hyoungsuk Jeon, Steven W. McLaughlin, Il-Min Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/6747289
- **Abstract**: We consider a cooperation scenario between primary users and untrusted secondary users in cognitive radio networks. The secondary users are willing to help the primary users to relay the primary users' messages in reward for being allowed to share the primary users' spectrum bands. However, the primary users might be reluctant to accept this help, since the secondary users are untrustworthy and may try unauthorized decoding of the primary users' messages. This paper will answer the question: when is this cooperation mutually beneficial for primary and secondary users? Taking an approach of information-theoretic secrecy, such as coding techniques for wiretap channels, the primary users can allow the secondary users to sense and relay the message, while ensuring that the secondary users are ignorant of the primary users' messages. We characterize an achievable secrecy rate of primary users with a rate of the secondary users' communication. From the derived rate pairs, an optimization problem is formulated such that the secondary transmitter distributes its transmit power to maximize its data rate while providing a higher secrecy rate to the primary users. We demonstrate that this cooperation can provide a positive secrecy rate, even when a non-cooperative scheme achieves a zero secrecy rate.

## A Least Square Method for Parameter Estimation of RSC Sub-Codes of Turbo Codes

- **Status**: ❌
- **Reason**: 터보(RSC) 부호 파라미터 추정 — 비-LDPC, BP 이식 기법 아님
- **ID**: ieee:6763130
- **Type**: journal
- **Published**: April 2014
- **Authors**: Peidong Yu, Jing Li, Hua Peng
- **PDF**: https://ieeexplore.ieee.org/document/6763130
- **Abstract**: A new algorithm is developed for parameter estimation of the recursive systematic convolutional sub-codes of turbo codes. It is based on a least square cost function of the encoder coefficients. A simple iterative process assisted by a try-again scheme is designed for the optimization of the cost function. Simulation results show that, compared with the existing method, the new algorithm significantly improves the performance while the complexity is quite reasonable.

## Layered Wireless Video Relying on Minimum-Distortion Inter-Layer FEC Coding

- **Status**: ❌
- **Reason**: 계층 비디오 inter-layer FEC(XOR/RSC convolutional) 무선영상 전송 — 비-LDPC, 응용특이적, 이식 기법 없음
- **ID**: ieee:6714525
- **Type**: journal
- **Published**: April 2014
- **Authors**: Yongkai Huo, Mohammed El-Hajjar, Robert G. Maunder +1
- **PDF**: https://ieeexplore.ieee.org/document/6714525
- **Abstract**: Layered video coding is capable of progressively refining the reconstructed video quality with the aid of multiple layers of unequal importance. When the base layer (BL) is corrupted or lost due to channel impairments, the enhancement layers (ELs) must be discarded by the video decoder, regardless whether they are perfectly decoded or not, which implies that the transmission power assigned to the ELs is wasted. To circumvent this problem, we proposed a bit-level inter-layer forward error correction (IL-FEC) scheme for layered video transmission in our previous work, which implanted the systematic bits of the BL into the systematic bits of the ELs using exclusive-OR operations (XOR). This allowed the receiver to exploit the implanted bits of the ELs for assisting the BL's decoding and hence improved the overall system performance of our IL-FEC aided layered video scheme. In this treatise, we find the specific FEC coding rates in a real-time on-line fashion for the sake optimizing the overall system performance. The proposed procedure is widely applicable to diverse wireless transceivers and FEC codecs. Our simulation results show that the proposed optimized IL-FEC system outperforms the traditional optimal UEP by about 1.9 dB of Eb/N0 at a peak signal-to-noise ratio (PSNR) of 38 dB. Viewing the improvements in terms of the video quality, 3.3 dB of PSNR improvement is attained at an Eb/N0 of 10 dB, when employing a recursive systematic convolutional (RSC) code.

## Extended Grouping of RFID Tags Based on Resolvable Transversal Designs

- **Status**: ❌
- **Reason**: RFID 태그 그룹화용 transversal design 패리티검사 — 채널 ECC 아님, 식별/그룹화 응용으로 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:6740004
- **Type**: journal
- **Published**: April 2014
- **Authors**: Yi-Sheng Su
- **PDF**: https://ieeexplore.ieee.org/document/6740004
- **Abstract**: This letter presents a novel scheme for the design of extended grouping of radio-frequency identification (RFID) tags, based on resolvable transversal designs (RTDs). Extended grouping of RFID tags allows identifying missing objects without the requirement for accessing external systems. The original scheme relies on Gallager's parity-check matrices and, as such, it cannot easily achieve designated decoding guarantees due to its pseudo-random nature. In view of the Gallager's parity-check matrix form of incidence matrices of RTDs, this letter proposes extended grouping of RFID tags based on RTDs. The proposed scheme proves to provide designated decoding guarantees more easily than the original scheme. In addition, this letter introduces a simple method, termed group splitting (GS), to improve the performance of extended grouping of RFID tags. Theoretical and simulation results demonstrate that the proposed scheme with or without GS is an efficient approach for the design of extended grouping of RFID tags.

## Delay Outage Probability in Block Fading Channel and Relay-Assisted Hybrid-ARQ Network

- **Status**: ❌
- **Reason**: block fading HARQ 지연 outage 확률 이론 분석 — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:6683122
- **Type**: journal
- **Published**: April 2014
- **Authors**: Mohamad Maaz, Philippe Mary, Maryline Hélard
- **PDF**: https://ieeexplore.ieee.org/document/6683122
- **Abstract**: In this letter, we focus on the delay outage probability in block fading channels and relay-assisted decode-and-forward hybrid-automatic retransmission request (HARQ-I) based systems. The delay outage is defined as the probability that the requirement on the average delay in additive white Gaussian noise (AWGN), could not be sustained in block fading channels. In other words, the system is said to be in outage if the mean delay exceeds a certain threshold θm due to the retransmission mechanism of erroneous packets. Our contribution lies in two folds: A closed form expression of the end-to-end delay in relay-assisted HARQ scheme is derived. Using the derived delay expression, an analytical form of the delay outage probability is proposed which might be very useful to avoid lengthy simulations.

## Transmission Rate Scheduling and Stopping Time for Time-Sensitive Multicast Stream Traffic in Cellular Networks

- **Status**: ❌
- **Reason**: 셀룰러 멀티캐스트 erasure 코딩 전송율 스케줄링 — 채널 ECC 디코더/구성 기여 아님, LDPC 무관
- **ID**: ieee:6760607
- **Type**: journal
- **Published**: April 2014
- **Authors**: Jung-Tsung Tsai
- **PDF**: https://ieeexplore.ieee.org/document/6760607
- **Abstract**: Opportunistic multicast schemes for time-sensitive stream traffic are studied for cellular networks where erasure coded packets are transmitted over discrete-time quasi-static forward-link fading channels. Assume that to successfully decode a transmitted stream fragment, it suffices that one receives k packets from the fragment. Two important issues are thus raised on when to stop transmitting a fragment and how to minimize the stopping time (ST) through transmission rate scheduling. Based on available channel state information and scheduled history, we tackle them particularly for small k required for short latency. If the distribution of IID channel states is available, the scheme is to compute and use the optimal constant transmission rate and minimum fixed ST subject to a reliability constraint. We show that the minimum ST grows with the logarithm of multicast group size. If channel state information is available, we propose to minimize random ST through selecting each optimal instantaneous transmission rate for a utility function. The utility function is specifically designed to exploit system transient states and dynamics. Results show that the scheme with an exponential weighted residual work achieves the least mean ST but the scheme maximizing instantaneous effective sum throughput has an edge of low complexity.

## Bayesian quantized network coding via generalized approximate message passing

- **Status**: ❌
- **Reason**: 양자화 네트워크 코딩의 Bayesian GAMP 디코딩(압축센싱 기반) — 소스압축/네트워크코딩 메시지패싱, 바이너리 LDPC BP ECC로 이식할 기법 아님.
- **ID**: ieee:6834995
- **Type**: conference
- **Published**: 9-11 April
- **Authors**: Mahdy Nabaee, Fabrice Labeau
- **PDF**: https://ieeexplore.ieee.org/document/6834995
- **Abstract**: In this paper, we study message passing-based decoding of real network coded packets. We explain our developments on the idea of using real field network codes for distributed compression of inter-node correlated messages. Then, we discuss the use of iterative message passing-based decoding for the described network coding scenario, as the main contribution of this paper. Motivated by Bayesian compressed sensing, we discuss the possibility of approximate decoding, even with fewer received measurements (packets) than the number of messages. As a result, our real field network coding scenario, called quantized network coding, is capable of inter-node compression without the need to know the inter-node redundancy of messages. We also present our numerical and analytic arguments on the robustness and computational simplicity (relative to the previously proposed linear programming and standard belief propagation) of our proposed decoding algorithm for the quantized network coding.

## Adaptive RC QC-LDPC channel coding for frequency hopping shallow water acoustic communication

- **Status**: ❌
- **Reason**: 표준 RC QC-LDPC를 수중통신에 적용·BER 비교만, 새 디코더·구성 기여 없음
- **ID**: ieee:6964347
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Meiying Lin, Xiaomei Xu, Yougan Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/6964347
- **Abstract**: Shallow water acoustic (SWA) channels are fast varying spatially and temporarily according to environmental conditions. Adaptive coding is appealing for SWA communications to improve the system efficiency by matching transmission parameters to channel variations. In this paper, we construct rate-compatible QC-LDPC (RC QC-LDPC) codes by extending information bits in frequency hopping (FH) SWA communication system. Combining actual channel impulse response measurement in Quangang Xiaocuo harbor, Fujian and Wuyuan bay, Xiamen, we build two SWA channels, and analyze the performances of RC QC-LDPC codes under different channel environment in FH-SWA communication system. Simulation results show that RC QC-LDPC codes can greatly reduce the bit error rate (BER) of the communication system, improve the system performance; The lower the code rate, the better the BER; The harsher the channel (such as longer channel delay, more multipath, lower signal-to-noise ratio), the lower the code rate is needed to meet system communication indicators; And look-up table of RC QC-LDPC code rate to meet communication performance indicator in FH-SWA system under different signal-to-noise ratio is given. The look-up table also calculates the data saving rate of RC QC-LDPC codes relative to 1/2 code rate. RC QC-LDPC codes in FH-SWA communication system can improve channel utilization, with flexible encoding and decoding, has good prospects in SWA communication.

## Dynamic coded cooperative ARQ for multi-hop underwater acoustic networks

- **Status**: ❌
- **Reason**: 수중음향 ARQ + erasure 코드 협력통신 프로토콜, LDPC 아니고 떼어낼 ECC 기법 없음
- **ID**: ieee:6964304
- **Type**: conference
- **Published**: 7-10 April
- **Authors**: Yougan Chen, Xiaomei Xu, Shengli Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/6964304
- **Abstract**: Dynamic coded cooperation (DCC) does not need extra transmission time scheduled for the relay, which is appealing to the bandwidth-limited high-delay underwater acoustic (UWA) environment. In this paper, we propose dynamic coded cooperative automatic repeat request (DCC-ARQ) protocol for multi-hop UWA networks. A transmission packet with multiple blocks is taken as a one-shot unit, where an erasure-correction code is used for inter-block encoding. Adopting the DCC scheme in each hop UWA transmission, the half-duplex cooperative node switches to cooperation phase immediately after it decodes the cooperative message, which provides a more reliable cooperative path for the specific three-node network. Further, if the relay (or destination in the last hop) node sends a negative acknowledgement (NACK) to the upstream cooperative node, the cooperative node only needs to retransmit parts of the packet under DCC-ARQ mechanism, hence a reduced end-to-end transmission latency can be achieved. Simulation results show that for a one-shot transmission, the proposed protocol achieves good balance between the reduced end-to-end delay and decent outage performance, relative to existing protocols.

## Symbol-based BP detection for MIMO systems associated with non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 디코더 + MIMO 검출 결합 — 비이진 LDPC 제외 대상.
- **ID**: ieee:6951949
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Ali Haroun, Charbel Abdel Nour, Matthieu Arzel +1
- **PDF**: https://ieeexplore.ieee.org/document/6951949
- **Abstract**: In this paper, an efficient iterative receiver for digital communication systems is investigated. It combines a Non-Binary Low-Density Parity-Check (NB-LDPC) decoder with a high-order constellation demapper and a Multiple-Input Multiple-Output (MIMO) detector. A suboptimal MIMO detector based on the Belief Propagation (BP) algorithm is investigated as an alternative to a Maximum Likelihood (ML) detector. Extrinsic information is exchanged between the detector and the decoder thanks to an iterative process. EXtrinsic Information Transfer (EXIT) charts enable to analyze the convergence behaviour of the proposed MIMO-BP detector. A suitable schedule for the different types of iterations is finally proposed to reduce the receiver latency and improve its error correction performance.

## A practical dirty paper coding scheme based on LDPC codes

- **Status**: ❌
- **Reason**: LDPC 기반 Dirty Paper Coding(소스/사이드정보 코딩), 채널 ECC 디코더 기법 아님
- **ID**: ieee:6951945
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Kiran M. Rege, Krishna Balachandran, Joseph H. Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/6951945
- **Abstract**: In this paper, we present a practical Dirty Paper Coding (DPC) scheme using sum codes based on LDPC codes. While a typical sum-code-based DPC scheme uses a constrained decoder as part of the encoding operation, such an approach fails in the case of LDPC codes since the constrained decoder based on a standard LDPC decoder tends to get stuck at highly suboptimal points in typical scenarios. We get around this difficulty via a simple code construction method based on bit-mapping or permutation. Examples included in this paper show that compared to standard communication schemes the proposed DPC scheme yields substantial savings in terms of the transmit energy required to attain desired error performance.

## Iterative detection and decoding algorithms for block-fading channels using LDPC codes

- **Status**: ❌
- **Reason**: 블록페이딩 MIMO IDD에서 LDPC를 베이스라인으로 쓴 무선 수신기 — 떼어낼 신규 디코더/구성 기법 없음, 무선 응용 특이적.
- **ID**: ieee:6952171
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Andre G. D. Uchoa, Rodrigo C. de Lamare, Cornelius Healy +1
- **PDF**: https://ieeexplore.ieee.org/document/6952171
- **Abstract**: We propose an Iterative Detection and Decoding (IDD) scheme with Low Density Parity Check (LDPC) codes for Multiple Input Multiple Output (MIMO) systems in block-fading receivers and fast fading Rayleigh channels. An IDD receiver with soft information processing that exploits the code structure and the behaviour of the log likelihood ratios (LLR)'s is developed. Minimum Mean Square Error (MMSE) receivers with Successive Interference Cancellation (SIC) and with Parallel Interference Cancellation (PIC) schemes are considered. The soft a posteriori output of the decoder in a block-fading channel with Root-Check LDPC codes has allowed us to create a new strategy to improve the Bit Error Rate (BER) of a MIMO IDD scheme. The proposed strategy has resulted in up to 3dB of gain in terms of BER for block-fading channels and up to 1dB in fast fading channels.

## Polar coded HARQ scheme with Chase combining

- **Status**: ❌
- **Reason**: Polar 코드 HARQ-CC + SC 디코딩 — 비-LDPC 부호, 떼어낼 BP 이식 기법 없음.
- **ID**: ieee:6952074
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Kai Chen, Kai Niu, Zhiqiang He +1
- **PDF**: https://ieeexplore.ieee.org/document/6952074
- **Abstract**: A hybrid automatic repeat request scheme with Chase combing (HARQ-CC) of polar codes is proposed. The existing analysis tools of the underlying rate-compatible punctured polar (RCPP) codes for additive white Gaussian noise (AWGN) channels are extended to Rayleigh fading channels. Then, an approximation bound of the throughput efficiency for the polar coded HARQ-CC scheme is derived. Utilizing this bound, the parameter configurations of the proposed scheme can be optimized. Simulation results show that, the proposed HARQ-CC scheme under a low-complexity SC decoding is only about 1.0dB away from the existing schemes with incremental redundancy (HARQ-IR). Compared with the polar coded HARQ-IR scheme, the proposed HARQ-CC scheme requires less retransmissions and has the advantage of good compatibility to other communication techniques.

## Channel hardening-exploiting message passing (CHEMP) receiver in large MIMO systems

- **Status**: ❌
- **Reason**: Large MIMO용 message passing 검출기(CHEMP) — LDPC 부호 디코더 아닌 MIMO 검출, NAND ECC 이식성 없음.
- **ID**: ieee:6952193
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: T. Lakshmi Narasimhan, A. Chockalingam
- **PDF**: https://ieeexplore.ieee.org/document/6952193
- **Abstract**: In this paper, we propose a multiple-input multiple-output (MIMO) receiver algorithm that exploits channel hardening that occurs in large MIMO channels. Channel hardening refers to the phenomenon where the off-diagonal terms of the HH H matrix become increasingly weaker compared to the diagonal terms as the size of the channel gain matrix H increases. Specifically, we propose a message passing detection (MPD) algorithm which works with the real-valued matched filtered received vector (whose signal term becomes HT Hx, where x is the transmitted vector), and uses a Gaussian approximation on the off-diagonal terms of the HT H matrix. We also propose a simple estimation scheme which directly obtains an estimate of HT H (instead of an estimate of H), which is used as an effective channel estimate in the MPD algorithm. We refer to this receiver as the channel hardening-exploiting message passing (CHEMP) receiver. The proposed CHEMP receiver achieves very good performance in large-scale MIMO systems (e.g., in systems with 16 to 128 uplink users and 128 base station antennas). For the considered large MIMO settings, the complexity of the proposed MPD algorithm is almost the same as or less than that of the minimum mean square error (MMSE) detection. This is because the MPD algorithm does not need a matrix inversion. It also achieves a significantly better performance compared to MMSE and other message passing detection algorithms using MMSE estimate of H.

## Bit-interleaved polar-coded modulation

- **Status**: ❌
- **Reason**: Bit-interleaved polar-coded modulation + list 디코딩 — 비-LDPC, LDPC BP 이식 기법 없음.
- **ID**: ieee:6952075
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Hüseyin Afşer, Nazli Tirpan, Hakan Deliç +1
- **PDF**: https://ieeexplore.ieee.org/document/6952075
- **Abstract**: A polar coding scheme for bit-interleaved coded modulation (BICM) is proposed. Code construction is performed by extending Arikan's heuristic to parallel channels. A lower-complexity and numerically robust implementation of list decoding with cyclic redundancy check is adopted. The performance of the design methods used for the construction of proposed bit-interleaved polar coded modulation (BIPCM) system is evaluated over 16-ary quadrature-amplitude modulation with different mapping schemes. It is shown that the proposed BIPCM architecture provides significant performance advantages over the BICM schemes implemented with other well-known codes for moderate block lengths.

## An interleaver optimization for BICM-OFDM with convolutional codes over frequency-selective block fading channels

- **Status**: ❌
- **Reason**: BICM-OFDM 컨볼루션 코드용 인터리버 최적화 — 무선 응용 특이적, LDPC 무관.
- **ID**: ieee:6952165
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: Yuta Hori, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/6952165
- **Abstract**: Bit-interleaved coded modulation (BICM) system combined with orthogonal frequency-division multiplexing (OFDM) has been adopted in many recent wireless standards, where the random interleaver is commonly assumed due to its simplicity of analysis for BICM. On the other hand, the recent results have shown that BICM using convolutional code without any interleaving shows better performance than that with bit interleaving over an AWGN channel without fading. Nevertheless, the interleaver design suitable for BICM with convolutional code over general fading channels has not been well studied. In this paper, we propose an approach for optimizing conventional block interleavers in the framework of BICM-OFDM and demonstrate its effectiveness over frequency-selective Rayleigh and Ricean fading channels.

## On the performance of transceiver techniques for the K-user MIMO IFC with LTE-A turbo coding

- **Status**: ❌
- **Reason**: MIMO IFC 송수신 기법 + LTE-A 터보코딩, 비-LDPC 무선 응용
- **ID**: ieee:6934898
- **Type**: conference
- **Published**: 6-9 April 
- **Authors**: George C. Alexandropoulos, Stylianos Papaharalabos, Constantinos B. Papadias
- **PDF**: https://ieeexplore.ieee.org/document/6934898
- **Abstract**: The design of transceiver techniques for optimizing the performance of the K-user multiple-input multiple-output (MIMO) interference channel (IFC) is of great importance and has been the subject of many recent research papers. However, the vast majority of the existing comparative studies for the various techniques capitalizes on their ergodic sum-rate performance and does not quantify their achievable performance with practical error correction coding. In this paper we investigate the achievable performance of different transceiver techniques for the K-user MIMO IFC with the long term evolution advanced (LTE-A) turbo coding scheme. Techniques achieving interference alignment (IA) at the interference-limited regime as well as a technique that reconfigures to the interference conditions are considered. It is shown that, for most of the tested 3-user MIMO IFCs where each transmitter may send more than one data streams, the iterative transceiver techniques result in superior achievable spectral efficiency than conventional IA.

## A comparative performance study of LDPC and Turbo codes for realistic PLC channels

- **Status**: ❌
- **Reason**: PLC용 표준 QC-LDPC vs Turbo 성능 비교만, 새 디코더·구성 기여 없는 표준 부호 단순 재사용
- **ID**: ieee:6812365
- **Type**: conference
- **Published**: 30 March-2
- **Authors**: Gautham Prasad, Haniph A. Latchman, Youngjoon Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/6812365
- **Abstract**: Turbo codes are attractive compared with Low Density Parity Check (LDPC) codes for Forward Error Correction (FEC) applications mainly due to their superior performance, especially at low Signal-to-Noise Ratio (SNR) such as are common in Powerline channels. For example, IEEE 1901-FFT PHY used the Turbo coding scheme defined in the HomePlug AV standards. However, patent fees are usually required for each turbo-code enabled manufactured device. The objective of this paper is to examine whether unlicensed LDPC codes, with optimized choices of block lengths, could be a viable alternative for future Powerline Communications (PLC) applications. The paper shows that the performance of the LDPC codes can approximate that of the Turbo codes with higher block lengths, on channels with typical and realistic PLC characteristics. The paper also shows that the additional complexity associated with this increase in block length can be mitigated by the use of Quasi-Cyclic LDPC (QC-LDPC) codes.

## On impulse noise and its models

- **Status**: ❌
- **Reason**: 임펄스 노이즈 모델 서베이/완화기법 논의로 떼어낼 LDPC 디코더·구성·HW 기여 없음
- **ID**: ieee:6812360
- **Type**: conference
- **Published**: 30 March-2
- **Authors**: Thokozani Shongwey, A. J. Han Vinck, Hendrik C. Ferreira
- **PDF**: https://ieeexplore.ieee.org/document/6812360
- **Abstract**: This article gives a discussion on impulse noise, its models and how it affects communications systems. We discuss the different impulse noise models in the literature, looking at their similarities and differences in communications systems. The impulse noise models discussed are memoryless (Middleton Class A and Bernoulli-Gaussian), and with memory (Markov- Middleton and Markov-Gaussian). We then go further to give performance comparisons in terms of bit error rates for some of the variants of impulse noise models. We also compare the bit error rate performance of single-carrier (SC) and multi-carrier (MC) communications systems operating under impulse noise. It can be seen that MC is not always better than SC under impulse noise. Lastly, the known impulse noise mitigation schemes (clipping/nulling using thresholds, iterative based and error control coding methods) are discussed.

## LDPC-An inevitable code for communication systems

- **Status**: ❌
- **Reason**: LDPC 개요/장점 소개 수준의 서베이성 논문; 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:6949846
- **Type**: conference
- **Published**: 3-5 April 
- **Authors**: N. Vigna Vinod Kumar, M. Sivakumar
- **PDF**: https://ieeexplore.ieee.org/document/6949846
- **Abstract**: Low density parity check codes can be used in Communication systems for the optimal channel coding. LDPC codes are known for its optimal decoding and efficient Error correcting capability. Owing to this property this codes outperformed the other linear block codes like hamming code, Reed Solomon code, and BCH code. This paper investigates problem in channel coding process (i.e) noisy channel coding which leads to non-optimal communication. In addition it visualizes the existing coding schemes for channel coding. Finally, it shows how the LDPC code can be suited for the optimal channel coding scheme.

## Joint source channel network coding using QC LDPC codes

- **Status**: ❌
- **Reason**: QC-LDPC 기반 결합 소스-채널-네트워크 코딩(JSCC), LDPC가 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:6949803
- **Type**: conference
- **Published**: 3-5 April 
- **Authors**: P. Jesy, P. P. Deepthi
- **PDF**: https://ieeexplore.ieee.org/document/6949803
- **Abstract**: Motivated to develop a scheme that compresses, gives high throughput and adds robustness against channel noise, a new joint source channel network coding (JSCNC) using Quasi Cyclic Low Density Parity Check (QCLDPC) code is proposed for a sensor network with two source nodes communicating correlated information to multiple destination nodes. The source coding is performed by transmitting only half of the information bits of QCLDPC code and transmitting the parity bits as such, since the parity bits are usually uncorrelated compared to the corresponding information bits. The correlations in sensor network data are used effectively at the relay node to reconstruct the original information bits transmitted by the source nodes. Relay scheme used in our proposed work is a decode and forward relaying in which masking of information bits are done before network coding at the relay. This helps in low-error decoding at the destination.

## Race among error control codes in OFDM - role of modulation techniques

- **Status**: ❌
- **Reason**: OFDM에서 LDPC vs turbo BER 비교 + 암호화; LDPC가 부수 언급일 뿐 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:6949836
- **Type**: conference
- **Published**: 3-5 April 
- **Authors**: Padmapriya Praveenkumar, K. Thenmozhi, R. Ramya +2
- **PDF**: https://ieeexplore.ieee.org/document/6949836
- **Abstract**: This paper gives an insight on, error control codes, where Low Density Parity Check (LDPC) codes or turbo codes are used to encode the data stream to tolerate channel errors and triple encryption is done to prevent un-authorization before passing the data over Orthogonal Frequency Division Multiplexing (OFDM) system. The system adopts diverse modulation schemes like Binary Phase Shift Keying(BPSK), Quadrature Phase Shift Keying(QPSK) and Quadrature Amplitude Modulation(QAM) using Additive White Gaussian Noise (AWGN) channel. The comparative analysis of LDPC over turbo codes is done and Bit Error Rate(BER) Vs Eb/No values are plotted and correlation values are computed after encryption.

## EXIT-chart-based LDPC code design for spatial modulation

- **Status**: ❌
- **Reason**: Spatial modulation용 EXIT-chart degree distribution 최적화 — 무선 응용 특이적, NAND 이식 가능 디코더/구성 기법 아님
- **ID**: ieee:6920539
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Hong Liu, Jianping Zheng, Jinfang Dou +1
- **PDF**: https://ieeexplore.ieee.org/document/6920539
- **Abstract**: The low-density parity-check (LDPC) code optimization for spatial modulation (SM) is studied using the extrinsic information transfer (EXIT) chart technique. First, for the maximum a posteriori probability (MAP) detector of the SM, its EXIT chart is characterized through Monte Carlo simulations. Then, the optimized degree distribution is acquired by matching the check node decoder curve to the combined detector and variable node decoder curve. Simulation results show that these optimized codes have performance gains from 0.3 to 1.3 dB, compared with the regular code and the optimized code for the additive Gaussian white noise channel, in 4×4 and 16×16 multiple-antenna systems.

## Joint serially concatenated continuous phase modulation and physical-layer network coding

- **Status**: ❌
- **Reason**: CPM+물리계층 네트워크코딩 직렬연접, 콘볼루션 외부코드 — LDPC 무관, 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:6920527
- **Type**: conference
- **Published**: 26-28 Apri
- **Authors**: Nan Sha, Yuanyuan Gao, Xiaoxin Yi +2
- **PDF**: https://ieeexplore.ieee.org/document/6920527
- **Abstract**: This paper presents a joint physical-layer network coding (PNC) and serially concatenated continuous phase modulation (SCCPM) scheme in a two-way relay (TWR) channel. This proposed scheme can be viewed as a serial concatenated codes (SCCs) scheme in which the joint CPM and PNC is the inner code and the convolutional code (CC) is the outer code. It aims to improve the spectral efficiency, error performance and power efficiency of the PNC system by utilizing the technical advantage of CPM and SCCs. An iterative decoding algorithm for the relay receiver over AWGN channels is investigated. Emphasis is put on the extrinsic logarithmic likelihood ratios (LLRs) of the XORed codewords generated by the soft input soft output (SISO) inner decoder. Simulation results are also provided to show the error performance of the joint scheme.

## Spatially-coupled coding based communication over the correlated Nakagami fading channel

- **Status**: ❌
- **Reason**: SC-LDPC window decoding을 상관 Nakagami 페이딩 채널에 적용—무선 응용 특이적, interleaver 기반 방법으로 떼어낼 NAND ECC 신규 기법 없음
- **ID**: ieee:6830343
- **Type**: conference
- **Published**: 23-25 Apri
- **Authors**: Reza A. Ashrafi, Ali E. Pusane
- **PDF**: https://ieeexplore.ieee.org/document/6830343
- **Abstract**: Spatially-coupled LDPC codes have recently gained considerable amount of research interest because of their implementation advantages. In addition to their superior error performance over several communication channels, they are capable of low-delay decoding, achieved via a sliding window decoding architecture. On the other hand, window decoding is highly vulnerable against data transmission over correlated channels that introduce correlation among the received symbols. In this paper, we evaluate the error performance of two novel approaches that have been proposed in the relevant literature for robust spatially-coupled-coded data transmission over the correlated channels. In this scope, we consider the correlated Nakagami-m fading channel and show via simulations that convolutional-interleaver-based method, while maintaining the low-decoding delay, gives a better error performance.

## New results on radiography image transmission with unequal error protection using protograph double LDPC codes

- **Status**: ❌
- **Reason**: protograph double LDPC 기반 JSCC/UEP 이미지전송 — LDPC가 베이스라인, JSCC는 제외
- **ID**: ieee:6825204
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Liangliang Xu, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/6825204
- **Abstract**: In this paper, we propose a new joint source-channel coding (JSCC) system with unequal error protection (UEP) constructed from protograph low-density parity-check (P-LDPC) codes for medical image transmission over additive white Gaussian noise (AWGN) channel to minimize the end to end image distortion. In order to make the P-LDPC codes suitable for the image transmission with UEP system, we combine two Tanner graphs, one of which is derived by protograph. A typical radiography image and other two gray-scale images are applied in our simulation. And we compare the peak signal-to-ratio (PSNR) performance of our codes with a previous work on UEP using P-LDPC codes and some other UEP schemes based on LDPC codes and Turbo codes. Simulation results indicate that the proposed scheme can apparently increase the PSNR value of the received images and reconstruct the transmitted images completely and correctly even at a very low signal-to-noise ratio (SNR). In addition, the proposed scheme can reduce the complexity of the image transmission model of our previous work and is superior than other UEP schemes with 0.5-2.5 dB increase in SNR.

## Iterative demodulation and decoding of LDPC-coded M-ary DCSK modulation over AWGN channel

- **Status**: ❌
- **Reason**: DCSK 변조 LDPC 반복 복조/복호 — LDPC 디코더 베이스라인, 통신 응용 특이, 떼어낼 ECC 기법 없음
- **ID**: ieee:6825214
- **Type**: conference
- **Published**: 2-4 April 
- **Authors**: Yibo Lyu, Guofa Cai, Lin Wang
- **PDF**: https://ieeexplore.ieee.org/document/6825214
- **Abstract**: In this article, an iterative demodulation and decoding receiver for M-ary differential chaos shift keying (DSCK) modulation is proposed over Additive White Gaussian Noise (AWGN) channel. The Log-Likelihood Ratios (LLRs) of coherent DCSK demodulator and decoder are derived assuming that its perfect carrier synchronization happened. The simulation results show that the performance of our proposed iterative receiver outperform that of the noniterative receiver over AWGN channel due to extrinsic information exchanged between demodulator and decoder. Further-more, Extrinsic Information Transfer chart is used to investigate the convergence behavior of our proposed receiver.

## LT codes with block duplication and ring type constellation for unequal error protection

- **Status**: ❌
- **Reason**: LT(fountain) 코드 기반 부등 오류보호 — fountain/erasure, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6863053
- **Type**: conference
- **Published**: 14-16 Apri
- **Authors**: B. Rajkumarsingh, S. Basant Rai
- **PDF**: https://ieeexplore.ieee.org/document/6863053
- **Abstract**: This work describes an unequal error protection using a rateless code namely Luby transform codes (LT codes), with block duplication, over Additive White Gaussian Noise (AWGN) channel. Ring type constellation is used as modulation technique to encode the different levels of data independently. In noisy channels, the index replacing concept cannot be used because all the bits are corrupted by noise; symbols are no more either correctly received or completely lost. In this work, a new method has been proposed to circumvent the need for index replacing in block duplication. This is called Index Averaging. It is found that block duplication applied to the Most Important Bits (MIB) leads to a better performance than previous Unequal Error Protection (UEP) based schemes.
