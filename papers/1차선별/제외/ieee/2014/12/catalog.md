# IEEE Xplore — 2014-12


## A Hybrid Decoding Scheme for Short Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: short non-binary LDPC 하이브리드 디코딩 — 비이진 LDPC 제외
- **ID**: ieee:6945781
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Marco Baldi, Franco Chiaraluce, Nicola Maturo +2
- **PDF**: https://ieeexplore.ieee.org/document/6945781
- **Abstract**: In this paper, an iterative soft-decision hybrid decoding algorithm for non-binary low-density parity-check (LDPC) codes with short codeword lengths is proposed. The rationale of the approach is to combine the classical belief propagation (BP) iterative LDPC decoding algorithm with the most reliable basis (MRB) decoding algorithm. This allows to achieve significant performance improvements, with a complexity that, for medium/low error rates, is only slightly higher than that of the BP algorithm alone. The performance improvement with respect to pure BP decoding is up to 0.7 dB at codeword error rate (CER) ≈ 10-5. Notably, for a fixed MRB order, hybrid decoding achieves a gain up to 0.5 dB at CER ≈ 10-5 with respect to BP decoding and MRB decoding used alone.

## EXIT Chart Analysis of Puncturing for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: non-binary LDPC puncturing EXIT 분석 — 비이진 LDPC 제외
- **ID**: ieee:6942182
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Kuntal Deka, A. Rajesh, Prabin Kumar Bora
- **PDF**: https://ieeexplore.ieee.org/document/6942182
- **Abstract**: This letter presents an EXtrinsic Information Transfer (EXIT) chart tool for the puncturing of non-binary (NB) low-density parity-check (LDPC) codes. With the help of this tool, we study the dependence of the performance of various bitwise and symbolwise puncturing patterns on the degree of a variable node (VN). The grouping algorithm (GA) is a useful technique for the short-length codes to find the recoverable VNs. By incorporating the GA under the EXIT chart model, we propose a method to find the optimum recoverable puncturing pattern.

## Bit-Reliability Based Low-Complexity Decoding Algorithms for Non-Binary LDPC Codes

- **Status**: ❌
- **Reason**: non-binary LDPC majority-logic 디코딩 — 비이진 LDPC 제외
- **ID**: ieee:6954447
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Qin Huang, Mu Zhang, Zulin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6954447
- **Abstract**: This paper presents bit-reliability based majority-logic decoding (MLgD) algorithms for non-binary LDPC codes. The proposed algorithms pass only one Galois field element and its reliability along each edge of the Tanner graph of a non-binary LDPC code. Since their reliability updates are in terms of bits rather than symbols, they are more efficient than traditional MLgD based decoding algorithms. By weighting the soft reliability of the extrinsic information-sums based on their hard reliability, the proposed algorithms can achieve good error performance for non-binary LDPC codes with various column weights. Moreover, their computational complexity and memory consumption are remarkably reduced compared with existing MLgD based decoding algorithms. As a result, they provide effective tradeoffs between error performance and complexity for decoding of non-binary LDPC codes.

## An Efficient Fully Parallel Decoder Architecture for Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF(256)) 디코더, 바이너리 LDPC만 포함 원칙에 따라 제외
- **ID**: ieee:6687216
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Jun Lin, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/6687216
- **Abstract**: Nonbinary low-density parity-check (NB-LDPC) codes outperform their binary counterparts in some cases, but their high decoding complexity is a significant hurdle to their applications. In this paper, we propose a decoding algorithm with reduced computational complexities and smaller memory requirements for NB-LDPC codes. First, a simplified algorithm is proposed to reduce the computational complexity of variable node processing. To reduce the memory requirements, existing NB-LDPC decoders often truncate the message vectors to a limited number nm of values. However, the memory requirements of these decoders remain high when the field size is large. In this paper, an improved trellis-based check node processing algorithm is proposed to significantly reduce the memory requirement. The number of elements in a variable-to-check message is reduced to nv (nv <; nm). The sorted log likelihood ratio (LLR) vector of a check-to-variable (c-to-v) message is approximated using a piecewise linear function. For each a priori message, most of the LLRs are approximated with a linear function. Two low complexity LLR generation units (LGUs) are proposed to compute LLR vectors for c-to-v messages. A fully parallel NB-LDPC decoder over GF(256) is implemented with 28-nm CMOS technology. The decoder over GF(256) achieves a throughput of 546 Mb/s and an energy efficiency of 0.178 nJ/b/iter.

## Progressive edge-growth algorithm for low-density MIMO codes

- **Status**: ❌
- **Reason**: LDMC(low-density MIMO codes) 구성은 MIMO 검출기-디코더 결합 특화로 NAND LDPC에 떼어낼 일반 코드설계 기법 없음, 무선 MIMO 응용 특이적
- **ID**: ieee:7023292
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Xueqin Jiang, Yi Yang, Moon Ho Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/7023292
- **Abstract**: In low-density parity-check (LDPC) coded multiple-input multiple-output (MIMO) communication systems, probabilistic information are exchanged between an LDPC decoder and a MIMO detector. The MIMO detector has to calculate probabilistic values for each bit which can be very complex. In [1], the authors presented a class of linear block codes named low-density MIMO codes (LDMC) which can reduce the complexity of MIMO detector. However, this code only supports the outer-iterations between the MIMO detector and decoder, but does not support the inner-iterations inside the LDPC decoder. In this paper, a new approach to construct LDMC codes is introduced. The new LDMC codes can be encoded efficiently at the transmitter side and support both of the inner-iterations and outer-iterations at the receiver side. Furthermore they can achieve the design rates and perform very well over MIMO channels.

## A Joint Source/Channel Approach to Strengthen Embedded Programmable Devices against Flash Memory Errors

- **Status**: ❌
- **Reason**: MLC NAND 대상이나 소스/채널 결합(JSCC) 압축 기법, 떼어낼 ECC 디코더/HW 기법 없음
- **ID**: ieee:6891205
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Maurizio Martina, Carlo Condo, Guido Masera +1
- **PDF**: https://ieeexplore.ieee.org/document/6891205
- **Abstract**: Reconfigurable embedded systems can take advantage of programmable devices, such as microprocessors and field-programmable gate arrays (FPGAs), to achieve high performance and flexibility. Support to flexibility often comes at the expense of large amounts of nonvolatile memories. Unfortunately, nonvolatile memories, such as multilevel-cell (MLC) NAND flash, exhibit a high raw bit error rate that is mitigated by employing different techniques, including error correcting codes. Recent results show that low-density-parity-check (LDPC) codes are good candidates to improve the reliability of MLC NAND flash memories especially when page size increases. This letter proposes to use a joint source/channel approach, based on a modified arithmetic code and LDPC codes, to achieve both data compression and improved system reliability. The proposed technique is then applied to the configuration data of FPGAs and experimental results show the superior performance of the proposed system with respect to state of the art. Indeed, the proposed system can achieve bit-error-rates as low as about 10-8 for cell-to-cell coupling strength factors well higher than 1.0.

## Spatial Coupling of Generator Matrices: A General Approach to Design Good Codes at a Target BER

- **Status**: ❌
- **Reason**: 생성행렬 spatial coupling(BMST) — generator matrix 결합 기법으로 LDPC 패리티검사/디코더 ECC 이식 기여 없음
- **ID**: ieee:6940240
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Chulong Liang, Xiao Ma, Qiutao Zhuang +1
- **PDF**: https://ieeexplore.ieee.org/document/6940240
- **Abstract**: For any given short code (referred to as the basic code), block Markov superposition transmission (BMST) provides a simple way to obtain predictable extra coding gain by spatially coupling the generator matrix of the basic code. This paper presents a systematic design methodology for BMST systems to approach the channel capacity at any given target bit error rate (BER) of interest. To simplify the design, we choose the basic code as the Cartesian product of a short block code. The encoding memory is then inferred from the genie-aided lower bound according to the performance gap of the short block code to the corresponding Shannon limit at the target BER. In addition to the sliding-window decoding algorithm, we propose to perform one more phase decoding to remove residual (rare) errors. A new technique that assumes a noisy genie is proposed to upper bound the performance. Under some mild assumptions, these genie-aided bounds can be used to predict the performance of the proposed two-phase decoding algorithm in the extremely low BER region. Using the Cartesian product of a repetition code as the basic code, we construct a BMST system with an encoding memory 30 whose performance at the BER of 10-15 can be predicted within 1 dB away from the Shannon limit over the binary-input additive white Gaussian noise channel.

## Systematic LDPC Convolutional Codes: Asymptotic and Finite-Length Anytime Properties

- **Status**: ❌
- **Reason**: systematic LDPC convolutional의 anytime reliability — BEC 한정 이론적 anytime 특성, 떼어낼 NAND 이식 기법 없음
- **ID**: ieee:6933940
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Leefke Grosjean, Lars Kildehøj Rasmussen, Ragnar Thobaben +1
- **PDF**: https://ieeexplore.ieee.org/document/6933940
- **Abstract**: Here we propose an ensemble of non-terminated systematic LDPC convolutional codes with increasing memory, and show that, over the binary erasure channel (BEC), these codes achieve anytime reliability asymptotically when decoded with an expanding-window message-passing decoder. The corresponding anytime exponents are determined through protograph-based extrinsic information transfer charts. Fundamental complications arising when transmitting with finite block lengths are identified and a combinatorial performance analysis, when transmitting over a static BEC with a fixed number of erasures per codeword block, is developed. Based on the performance analysis, we explore the use of feedback for achieving anytime behavior with constraints on block length. To meet complexity constraints, with or without feedback, the code memory can be limited at the cost of an error floor emerging with a delay proportional to the memory constraint. Although the analysis is developed for a static BEC we show numerically that we can design efficient low-complexity finite-length codes with anytime properties even for the conventional BEC.

## Integer-Forcing Linear Receivers

- **Status**: ❌
- **Reason**: MIMO 정수강제 선형 수신기, LDPC 비의존 통신 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:6918518
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Jiening Zhan, Bobak Nazer, Uri Erez +1
- **PDF**: https://ieeexplore.ieee.org/document/6918518
- **Abstract**: Linear receivers are often used to reduce the implementation complexity of multiple-antenna systems. In a traditional linear receiver architecture, the receive antennas are used to separate out the codewords sent by each transmit antenna, which can then be decoded individually. Although easy to implement, this approach can be highly suboptimal when the channel matrix is near singular. This paper develops a new linear receiver architecture that uses the receive antennas to create an effective channel matrix with integer-valued entries. Rather than attempting to recover transmitted codewords directly, the decoder recovers integer combinations of the codewords according to the entries of the effective channel matrix. The codewords are all generated using the same linear code, which guarantees that these integer combinations are themselves codewords. Provided that the effective channel is full rank, these integer combinations can then be digitally solved for the original codewords. This paper focuses on the special case where there is no coding across transmit antennas and no channel state information at the transmitter(s), which corresponds either to a multiuser uplink scenario or to single-user V-BLAST encoding. In this setting, the proposed integer-forcing linear receiver significantly outperforms conventional linear architectures such as the zero forcing and linear minimum mean-squared error receiver. In the high signal-to-noise ratio regime, the proposed receiver attains the optimal diversity-multiplexing tradeoff for the standard multiple-input multiple-output (MIMO) channel with no coding across transmit antennas. It is further shown that in an extended MIMO model with interference, the integer-forcing linear receiver achieves the optimal generalized degrees of freedom.

## A Framework for the Transmission of Multimedia Traffic using HM and RS Coding over Nakagami-M Channels

- **Status**: ❌
- **Reason**: RS 코딩+계층변조 크로스레이어 UEP, 비-LDPC 부호이며 떼어낼 LDPC 디코더 기법 없음
- **ID**: ieee:8538348
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: T. Quazi, H. Xu, A. Saeed
- **PDF**: https://ieeexplore.ieee.org/document/8538348
- **Abstract**: Hierarchical modulation (HM) provides different levels of error performance for the high and low priority bits modulated. This differentiation can be aligned to various classes of multimedia traffic demanding different levels of error rate performance. In a previous cross-layer design scheme, which combined conventional modulation at physical layer with RS coding at the application layer, an unequal error protection mechanism was used at the application layer for guaranteeing quality of service for various classes of multimedia traffic. Instead of using only a single layer, in this paper we present a more flexible two layer cross-layer design framework for unequal error protection, combining RS coding at the application layer with HM at the physical layer. Furthermore, in order to improve error performance of the system, a signal space diversity (SSD) scheme is also incorporated into the physical layer of the framework. Without consuming additional transmit power and bandwidth, the use of the SSD HM in the cross-layer design system resulted in significant gains when compared to the non-SSD, standard HM system. It is shown that the cross-layer design system with SSD HM has a 10dB gain over the non-SSD HM system in a Nakagami m=1 channel with a frame error rate target of 10−4.

## Performance Analysis of MPSK Phase Detectors for Carrier Synchronization PLLs at Low SNRs

- **Status**: ❌
- **Reason**: MPSK 반송파 동기화 PLL 위상검출기 분석 — LDPC ECC와 무관한 통신 동기화 이론
- **ID**: ieee:6926748
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Wei Jiang, Yifei Cui
- **PDF**: https://ieeexplore.ieee.org/document/6926748
- **Abstract**: In this letter, we analyze the performance of a category of phase detectors (PDs) for carrier synchronization phase-locked loops (PLLs) in M-ary phase shift keying (MPSK) receivers working at low signal-to-noise ratios (SNRs). These PDs have the property that their outputs are functions of the inputs' phase only, and thus, their performance is independent of the automatic gain control (AGC) circuits. We deduce closed-form expressions about the linearized gain and equivalent noise variance of these PDs when SNR goes to zero and sum up simple approximate formulas for three typical PDs at all SNRs. We also prove that the modified Mth-power PD performs asymptotically best in this category of PDs as SNR goes to zero.

## Channel Interleavers for Terrestrial Broadcast: Analysis and Design

- **Status**: ❌
- **Reason**: DVB-T2 지상파 방송용 채널 인터리버 설계, LDPC ECC 디코더/구성 기여 없음
- **ID**: ieee:6912995
- **Type**: journal
- **Published**: Dec. 2014
- **Authors**: Ronald Garzon Bohorquez, Charbel Abdel Nour, Catherine Douillard
- **PDF**: https://ieeexplore.ieee.org/document/6912995
- **Abstract**: A method to design channel interleavers based on span properties and mutual information is presented. Resulting interleavers enjoy better burst error control and can mitigate the effect of regular error patterns. An application example based on the 2nd generation digital video broadcasting terrestrial (DVB-T2) standard is elaborated. Four channel interleaving structures are generated, resulting from a joint optimization of the interleaver span properties in the time and frequency domains, while guaranteeing good interaction with the bit interleaver. Proposed solutions are compared to the standardized DVB-T2 channel interleaver in terms of performance, latency, and complexity. A significant improvement can be observed in severe channel conditions, especially over time and frequency-selective channels with erasures. Moreover, the complexity and latency of the proposed channel interleavers are reduced compared to the original DVB-T2.

## Blind identification of binary LDPC codes for M-QAM signals

- **Status**: ❌
- **Reason**: 바이너리 LDPC 인코더 블라인드 식별(EM/M-QAM) — 채널 ECC 디코더·구성·HW 기여 없음, 통신 식별 응용
- **ID**: ieee:7037355
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Tian Xia, Hsiao-Chun Wu, Shin Yu Chang +2
- **PDF**: https://ieeexplore.ieee.org/document/7037355
- **Abstract**: In this paper, we propose a blind binary low-density parity-check (LDPC) encoder identification scheme for M-quadrature amplitude modulation (M-QAM) signals. The expectation-maximization (EM) algorithm is developed to estimate the unknown signal amplitude, noise variance, and phase offset for M-QAM signals. The a posteriori probabilities (APPs) of the coded bits are obtained from the APPs of the transmitted symbols according to the M-QAM mapper. Monte Carlo simulation results demonstrate the effectiveness of our proposed new blind binary LDPC encoder identification scheme for different modulation orders. The average iteration number needed for the EM algorithm to converge is also investigated for different modulation orders.

## A merry-go-round decoding scheme for non-binary quasi-cyclic LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) QC-LDPC 디코딩·구성 — 비이진 LDPC 제외
- **ID**: ieee:7037020
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Keke Liu, Juane Li, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/7037020
- **Abstract**: This paper presents a reduced-complexity iterative scheme and an algorithm for decoding non-binary quasi-cyclic (QC) LDPC codes of a specific type. The proposed decoding scheme and the algorithm together significantly reduce the hardware implementation complexity of a decoder with no performance degradation. Also presented in the paper is a simple method for constructing a class of non-binary QC-LDPC codes.

## Performance evaluation of transmission system for 8K Super Hi-Vision satellite broadcasting

- **Status**: ❌
- **Reason**: 위성방송 전송시스템에 표준 LDPC 적용, 새 디코더·구성·HW 기여 없음
- **ID**: ieee:7037246
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Yoichi Suzuki, Kenichi Tsuchida, Yoshifumi Matsusaki +4
- **PDF**: https://ieeexplore.ieee.org/document/7037246
- **Abstract**: We developed a new transmission system for 8K Super Hi-Vision satellite broadcasting in Japan. This system has a transmission capacity of over 100 Mbps in a single 34.5MHz satellite transponder. The key technical feature of the new system are lowering roll-off factor to 0.03 and using 16APSK and LDPC code with a coding rate of 7/9. To confirm the transmission performance in a satellite channel, we conducted indoor transmission tests and transmission tests using Japanese communication and broadcasting satellites. This paper shows the transmission performance of this system and similar performance was obtained in indoor-transmission and satellite-transmission tests.

## LDPC encoder identification in time-varying flat-fading channels

- **Status**: ❌
- **Reason**: 플랫페이딩 채널에서 LDPC 인코더 식별(Viterbi/채널추정) — 떼어낼 ECC 기법 없음
- **ID**: ieee:7037356
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Tian Xia, Hsiao-Chun Wu, Supratik Mukhopadhyay
- **PDF**: https://ieeexplore.ieee.org/document/7037356
- **Abstract**: This paper tackles the low-density parity-check (LDPC) encoder identification problem encountered in the time-varying flat-fading channels which are modeled as finite-state Markov chains. The in-phase and quadrature-phase components of the channel coefficients are both represented by a number of states. To greatly simplify the computation of the channel observation probabilities, each channel-state region is further quantized to an interior point. Based on our proposed finite-state Markov model, the Viterbi algorithm is thus invoked to blindly estimate the unknown channel-state sequence from each received signal segment. To mitigate the phase ambiguity which is inherent in the channel-state estimation process, the pilot-aided channel estimation method is also proposed here. The LDPC encoder is finally identified in the framework of the log-likelihood ratio of syndrome a posteriori probability. The performance of our proposed LDPC identification scheme is investigated for different normalized Doppler rates and different mechanisms to reconstruct the channel-state information. Monte Carlo simulation results suggest that pilot symbols are necessary for leading to a satisfactory identification performance for time-varying flat-fading channels.

## Logarithmic quantization scheme for reduced hardware cost and improved error floor in non-binary LDPC decoders

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC 양자화/Min-Max 디코더 기법 — 바이너리 LDPC 아님, 제외
- **ID**: ieee:7037292
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Yuta Toriyama, Behzad Amiri, Lara Dolecek +1
- **PDF**: https://ieeexplore.ieee.org/document/7037292
- **Abstract**: Non-binary low-density parity-check (NB-LDPC) codes exhibit excellent error correction performance at the cost of high computational complexity of the decoding algorithm. A logarithmic quantization scheme is proposed to reduce the VLSI implementation cost of the Min-Max decoding algorithm, by scaling down the complexity of the check node calculations that are the prime bottleneck in NB-LDPC decoding. The proposed scheme is also shown to be robust against certain types of errors, and thus enables excellent error correction capabilities even for aggressively reduced wordlengths, relative to traditional, uniform quantization schemes that exhibit either poor waterfall region performance or high error floors for a similar number of bits. The proposed scheme is directly applicable to existing architectures with few modifications and is shown to reduce the computational complexity by up to 40%, especially for large field orders.

## Interference management via sliding-window superposition coding

- **Status**: ❌
- **Reason**: 슬라이딩윈도우 중첩코딩+LTE turbo, 간섭관리 — 비-LDPC, LDPC ECC 기법 없음
- **ID**: ieee:7063559
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Hosung Park, Young-Han Kim, Lele Wang
- **PDF**: https://ieeexplore.ieee.org/document/7063559
- **Abstract**: The sliding-window superposition coding scheme achieves the performance of simultaneous decoding with point-to-point channel codes and low-complexity decoding. This paper provides a case study of how this conceptual coding scheme can be transformed to a practical coding technique for two-user Gaussian interference channels. Simulation results demonstrate that sliding-window superposition coding can sometimes double the performance of the conventional method of treating interference as noise, still using the standard LTE turbo codes.

## Polar code design for intersymbol interference channels

- **Status**: ❌
- **Reason**: polar code ISI 채널 설계, 부호 비의존적 이식 디코더 기법 아님 — 비-LDPC 제외
- **ID**: ieee:7037160
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Ubaid U. Fayyaz, John R. Barry
- **PDF**: https://ieeexplore.ieee.org/document/7037160
- **Abstract**: We analyze the general form of the extrinsic information transfer curve of polar codes viewed as multilevel codes with multistage decoding. Based on this analysis, we propose a graphical design methodology to construct polar codes for intersymbol interference channels. The method matches the extrinsic information transfer curve of the code to that of the intersymbol interference channels, so that there is an open convergence tunnel between the two. We show that polar codes can provide such a matching to the channel curve under soft-cancellation decoding and propose one such method to achieve it. Example code designs are presented to demonstrate that polar codes that are optimized for an ISI channel can significantly outperform polar codes that are designed for an AWGN channel.

## Asynchronous compute-and-forward/integer-Forcing with quasi-cyclic codes

- **Status**: ❌
- **Reason**: 비동기 compute-and-forward/IDT 무선 네트워크 기법, QC코드는 부수적이고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7037021
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Ping-Chung Wang, Yu-Chih Huang, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/7037021
- **Abstract**: Communication in the presence of bounded timing asynchronism which is known to the receiver but cannot be easily compensated is studied. Examples of such situations include point-to-point communication over inter-symbol interference (ISI) channels and asynchronous wireless networks. In these scenarios, although the receiver may know all the delays, it may not be an easy task for the receiver to compensate the delays as the signals are mixed together. A novel framework called interleave/deinterleave transform (IDT) is proposed to deal with this problem. It is shown that the IDT allows one to design the delays so that quasi-cyclic (QC) codes with a proper shifting constraint can be used accordingly. When used in conjunction with QC codes, IDT provides significantly better performance than existing schemes relying solely on cyclic codes. Two instances of asynchronous physical-layer network coding, namely the integer-forcing equalization for ISI channels and asynchronous compute-and-forward, are then studied where the gap-to-capacity can be bridged for the former and significant gains can be obtained for the later. The proposed IDT can be thought of as a generalization of the interleaving/deinterleaving idea in [1] which allows the use of QC codes thereby substantially increasing the design space.

## Pairwise error probability of turbo codes over joint fading and two-path shadowing channels

- **Status**: ❌
- **Reason**: Turbo 부호 PEP 이론 분석(JFTS 채널) — 비-LDPC, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:7037432
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: I. Dey, G. G. Messier, S. Magierowski
- **PDF**: https://ieeexplore.ieee.org/document/7037432
- **Abstract**: The performance of Turbo coded Binary Phase Shift Keying (BPSK) over the Joint Fading and Two-path Shadowing (JFTS) environment is analyzed. Exact analytical expression for the Pairwise Error Probability (PEP) of Turbo codes over fully interleaved JFTS channels is presented using the probability distribution of the squared independent and identically distributed JFTS random variables. Finally the Turbo coded Average Bit Error Rate (ABER) of a wireless communication system is simulated over JFTS fading / shadowing channels and compared with the derived analytical result.

## Distortion modeling and analysis for multilevel coded APSK with memoryless nonlinearity

- **Status**: ❌
- **Reason**: 멀티레벨 APSK 비선형 왜곡 모델링 무선 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7037244
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Daiki Yoda, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/7037244
- **Abstract**: In order to improve the bandwidth efficiency of communication systems under strict power limitation, the use of multilevel modulation together with near capacity channel coding is essential. However, such an approach is sensitive to nonlinear distortion associated with high peak-to-average power ratio (PAPR) of the resulting signals. We consider the application of the multilevel coded modulation with multi-stage decoding (MLC/MSD) over nonlinear communication channels and propose a robust unconventional set partitioning approach in conjunction with the metric adjusted to the statistical characteristics of nonlinear distortion. Numerical results show that the proposed method outperforms the system with the conventional labeling in terms of achievable average mutual information (AMI) and frame error rate (FER).

## Closed-form CRLBs for SNR estimation from turbo-coded square-QAM-modulated signals

- **Status**: ❌
- **Reason**: turbo/LDPC 부호화 신호의 SNR 추정 CRLB 순수 이론, 디코더·HW·구성 기여 없음
- **ID**: ieee:7037064
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Faouzi Bellili, Achref Methenni, Sofiène Affes
- **PDF**: https://ieeexplore.ieee.org/document/7037064
- **Abstract**: In this contribution, we derive for the first time the closed-form expressions for the Cramér-Rao lower bounds (CRLBs) of the signal-to-noise ratio (SNR) estimates from turbo-coded square-QAM transmissions. By exploiting the structure of the Gray mapping, we are able to factorize the likelihood function thereby linearizing all the derivation steps for the FIM elements. The analytical CRLBs coincide exactly with their empirical counterparts validating thereby our new analytical expressions. Numerical results suggest that the CLRBs for code-aided (CA) SNR estimates range between the CRLBs for non-data-aided (NDA) SNR estimates and those for data-aided (DA) ones, thereby highlighting the effect of the coding gain. At sufficiently high SNR levels, the three CRLBs coincide. The derived bounds are also valid for LDPC-coded systems and they can be evaluated in the same way when the latter are decoded using the turbo principal.

## A single parity check forward error correction method for high speed I/O

- **Status**: ❌
- **Reason**: 고속 I/O용 단일패리티검사(SPC) FEC, 비-LDPC 부호이고 임계검출 결합 wireline 응용
- **ID**: ieee:7032198
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Shiva Kiran, Sebastian Hoyos, Samuel Palermo
- **PDF**: https://ieeexplore.ieee.org/document/7032198
- **Abstract**: Some proposed high speed wireline communications make use of an ADC front end to allow a feedforward equalizer (FFE) to compensate for the frequency dependent loss of the channel. High precision ADCs are expensive in terms of power. The FFE block performs multiplication and addition operations at high speed and further increases the power consumption. This paper proposes a simple forward error correction method by which the ADC resolution and the equalizer complexity can be reduced. A single parity check code implemented together with a threshold detector can provide single error correction capability. With this error correction capability, the number of taps required in the FFE block is shown to be reduced to 3 taps from 6 taps for a channel with 15dB insertion loss at 5GHz frequency with the data rate being 20Gb/s. The effective number of bits (ENOB) required from the ADC is also shown to reduce to about 3.5 bits from 6 bits. The high rate of the code and the very simple decoder architecture make this error correction mechanism well suited for the wireline application.

## FFT based sum product decoding algorithm of LDPC coder for GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC FFT-SPA — 비이진 LDPC는 제외 대상
- **ID**: ieee:7044980
- **Type**: conference
- **Published**: 26-27 Dec.
- **Authors**: Jigisha Patel, Neeta Chapatwala, Mrugesh Patel
- **PDF**: https://ieeexplore.ieee.org/document/7044980
- **Abstract**: Low Density Parity Check (LDPC) codes have excellent error correcting performance. LDPC codes are one of the block coding techniques and it performs near Shannon limit and recommended for many practical applications. Non-binary LDPC codes extension of binary LDPC in error correcting property especially for short and moderate block length. In many digital communication systems these codes have strong competitors of turbo codes for error control. Low Density Parity Check as it name is suggests that in a parity check matrix (H) consists of very small number of non-zero elements comparing with zero elements. The strength of the LDPC code defines Parity Check Matrix (PCM). LDPC code contains two types of decoding algorithms hard and soft decision algorithm. By comparing with other traditional decoding algorithm FFT based sum product algorithm reduced computation complexity with better decoding performance. In this paper, LDPC codes for FFT based sum product decoding algorithm performances are analysed for various order of Galois Field GF(q) using AWGN channel. Decoding performance measured in terms of symbol error rate which improve with increasing order of Galois field.

## Performance analysis of LDPC coded wireless ad-hoc network for emergency response communications

- **Status**: ❌
- **Reason**: 무선 ad-hoc망 LDPC 코딩 성능평가뿐, 표준 LDPC 사용으로 떼어낼 신규 기법 없음
- **ID**: ieee:7073071
- **Type**: conference
- **Published**: 22-23 Dec.
- **Authors**: Nusrat Z. Zenia, Fariha Afsana, M. S. Kaiser +1
- **PDF**: https://ieeexplore.ieee.org/document/7073071
- **Abstract**: In this paper, we present the performance evaluation of coded wireless ad-hoc network for emergency response communication. Due to the limited transmission range, a number of intermediate relaying nodes may exist between source and destination and these convey source transmission using hybrid Amplify-and-forward (AF)/Decode-and-forward (DF) protocol. All nodes contain single antenna and OFDM based Low Density Parity Check (LDPC) coded transmission is considered over Rician fading channel. The closed form bit-error-rate (BER) expression has been deduced for the proposed system. Performance evaluation reveals that BER of the LDPC coded ad-hoc network is better than that of non-coded ad-hoc network.

## Sparse binary matrixes of QC-LDPC code for compressed sensing

- **Status**: ❌
- **Reason**: QC-LDPC를 압축센싱 측정행렬로 재사용 — 채널 ECC 아닌 sensing, 새 디코더 없음
- **ID**: ieee:7073409
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Xiao-Yan Jiang, Zheng-Guang Xie
- **PDF**: https://ieeexplore.ieee.org/document/7073409
- **Abstract**: To overcome the shortcoming that random measurement matrix is hard for hardware implementation. A new structural and sparse deterministic measurement matrix based on parity check matrix in quasi-cyclic low-density parity-check code was proposed by studying the theory of compressed sensing. To verify the performance of the new matrix, reconstruction experiments were conducted. Experimental results show that, compared with the commonly used matrixes, the proposed matrix has lower reconstruction error under the same reconstruction algorithm and compression ratio. The proposed method achieves certain improvement in Peak Signal-to-Noise Ratio. Especially, if it was applied to hardware implementation, the need for physical storage space and the complexity of the hardware implementation should be greatly reduced due to the properties of quasi-cyclic and symmetric in the structure.

## 802.11ad Key Performance Analysis and Its Application in Home Wireless Entertainment

- **Status**: ❌
- **Reason**: 802.11ad PHY 가정용 무선 — LDPC 언급 없고 떼어낼 ECC 기법 없음
- **ID**: ieee:7023805
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Shuyan Jiang, Jie Peng, Zhi Lu +2
- **PDF**: https://ieeexplore.ieee.org/document/7023805
- **Abstract**: In order to analyze the performance of SC (Single-Carrier) 60 GHz communication system, a structure of physical layer is designed based on IEEE 802.11ad standard. Supporting up to 2.16 GHz channel bandwidth, the transmission rate of the physical layer is close to 7G bit/s. At the same time, it adopt to single carrier and OFDM (Orthogonal Frequency Division Multiplexing) technology. In addition, using beam forming technology to offset the high path loss of 60GHz frequency band, and supporting fast session transfer between 2.4GHz, 5GHz and 60GHz frequency band. Existing Wi-Fi cannot be satisfied with the applications demand of the multiple wireless communication technologies, such as HD (High- Definition) video streaming wireless transmission. In the future, the development of smart home entertainment system urgent needs a new broadband wireless communication technology. New broadband smart home network based on 802.11ad will bring a new vitality to the smart home industry, give users abundant and excessive application experience, and open a new era of home entertainment.

## Data Directed Estimation Based Turbo Equalization in HF Communication

- **Status**: ❌
- **Reason**: HF 통신 turbo equalization — LDPC 디코더 아닌 채널등화, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7023690
- **Type**: conference
- **Published**: 19-21 Dec.
- **Authors**: Ma Zhuo, Du Shuanyi
- **PDF**: https://ieeexplore.ieee.org/document/7023690
- **Abstract**: A block turbo equalization algorithm is proposed, which is generalized from Data Directed Estimation (DDE) widely used in HF communications. The convergence rate of our block turbo equalization algorithm is faster than that of the linear MMSE turbo equalizations. Two simplified schemes of this block turbo equalization algorithm are also introduced, which is LC-TDDE algorithm and BSIC algorithm respectively. The LC-TDDE algorithm performs better than linear MMSE algorithm, while its complexity is proportional to the square of the length of data block, the BSIC algorithm possesses a linear complexity with a performance very close to the linear MMSE algorithms.

## Evolution of DVB-S2 from DVB-S for the efficient real time implementation

- **Status**: ❌
- **Reason**: DVB-S2 표준/실시간 구현 개요, 새 디코더·구성·HW 기여 없는 표준 재사용
- **ID**: ieee:7238532
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Sneha Pandya, Charmy Patel
- **PDF**: https://ieeexplore.ieee.org/document/7238532
- **Abstract**: DVB (Digital Video Broadcasting) is the set of international open standards for digital television. DVB standards are maintained by the DVB Project. DVB standards are defining the physical layer and data link layer of the distribution system. DVB standards which are based on MPEG-2 and MPEG-4 standards suggest that all data is transmitted in MPEG Transport Streams. The satellite member of the DVB family, DVB-S, is mentioned in European Standard EN 300 421. In particular it carries the information about the modulation and channel coding system for satellite digital multi program Television (TV)/High Definition Television (HDTV) services which are to be used for primary and secondary distribution in Fixed Satellite. DVB-S is intended to provide Direct-To-Home (DTH) services for consumer Integrated Receiver Decoders (IRD). DVB-S is suitable for the usage on different satellite transponder bandwidths and is compatible with Moving Pictures Experts Group 2 (MPEG 2) coded TV services. Flexibility defined within the specification enables the transmission capacity to be used for a variety of TV service configurations, including sound and data services. DVBS2-Digital satellite transmission technology has evolved considerably since the publication of the original DVB-S specification. New coding and modulation schemes permit greater flexibility and more efficient use of capacity and additional data formats from those originally foreseen can now be handled without significant increment in system complexity.

## A new Luby transform based wireless broadcast system

- **Status**: ❌
- **Reason**: LT(fountain/erasure) 부호 무선 브로드캐스트 시스템, LDPC는 베이스라인, 떼어낼 신규 ECC 기법 없음
- **ID**: ieee:7032622
- **Type**: conference
- **Published**: 17-18 Dec.
- **Authors**: U Rajanasree, V S Lakshmi
- **PDF**: https://ieeexplore.ieee.org/document/7032622
- **Abstract**: Luby Transform (LT) codes are the first realization of a class of erasure codes, usually known as universal erasure codes. LT codes were originally designed for Binary Erasure Channel (BEC), but for the sake of transmitting data reliably over the wireless broadcast channels, LT codes have to be combined with classical channel codes. This paper proposes a new model for LT code based wireless broadcast system by concatenating LT codes with Shannon-limit approaching LDPC codes. The normal Hard decoding scheme of LT codes is replaced with HSHD scheme and iterative channel estimation and decoding is used for LDPC codes. Simulation results show that the iterative channel estimation and decoding combined with HSHD outperforms the other decoding schemes in terms of BER.

## A survey of fault-tolerant processor based on error correction code

- **Status**: ❌
- **Reason**: 프로세서 내부 ECC 서베이, 신규 LDPC 디코더/구성/HW 기여 없음
- **ID**: ieee:7072971
- **Type**: conference
- **Published**: 16-17 Dec.
- **Authors**: Mohd Hafiz Sulaiman, Sani Irwan Md Salim, Anuar Jaafar +1
- **PDF**: https://ieeexplore.ieee.org/document/7072971
- **Abstract**: Fault detection and correction algorithms has been widely adopted in the various data communication system with view to protect the system from crashing due to hard and soft errors. As the system becomes more complex with the reduction of transistor size, fault detection and correction schemes are not limited to data transfer process. Internal components of the system's processor are also susceptible to soft errors that potentially would halt the system operation. This paper is focused on the current implementation of error correction code (ECC) on internal processor architecture. Various ECC algorithms are discussed from theory to its operation. Several researches that implemented ECC in processor architecture are also presented in order to demonstrate the variety of ECC execution to the processor architecture. A custom soft-core processor called UTEMRISC is presented as a study case to execute an ECC algorithm in low-end soft-core processor architecture on FPGA platform. For future work, the FT design will be embedded in UTeMRISC03 processor with further analysis of the fault assessment on each of the processor's components.

## A channel matched design of LDPC based secrecy coding for the fast fading channel

- **Status**: ❌
- **Reason**: Rayleigh 페이딩 보안코딩(인터리빙+더미비트), 보안 응용이며 이식 가능 LDPC 기법 없음
- **ID**: ieee:7021079
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Zhou Zhong, Liang Jin, Kaizhi Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/7021079
- **Abstract**: In this paper, we focus on security problem of low density parity check (LDPC) codes design in Rayleigh fading channel. In our secrecy coding scheme, confidential message bits are first interleaved according to the fading coefficients of authorized channel to hide positions, and then replaced with random dummy bits to conceal information from potential eavesdroppers. Simulation results show that due to different feature of authorized and eavesdropper's channels, the proposed scheme ensures that the authorized receiver is able to reconstruct the confidential message, while the eavesdropper almost can not extract any information with the same transmit power. Furthermore, the security gap can be further reduced.

## Capacity optimization of emerging memory systems: A shannon-inspired approach to device characterization

- **Status**: ❌
- **Reason**: PCM/analog memory capacity via mutual information for read-write circuit design; no transplantable LDPC decoder/code/HW technique
- **ID**: ieee:7047134
- **Type**: conference
- **Published**: 15-17 Dec.
- **Authors**: Jesse H. Engel, S. Burc Eryilmaz, SangBum Kim +5
- **PDF**: https://ieeexplore.ieee.org/document/7047134
- **Abstract**: Traditional approaches to memory characterize the number of distinct states achievable at a given Raw Bit Error Rate (RBER). Using Phase Change Memory (PCM) as an example analog-valued memory, we demonstrate that measuring the mutual information allows optimal design of read-write circuits to increase data storage capacity by 30%. Further, we show the framework can be used for energy efficient memory design by optimizing simulations of a 1Mb memory array to consume 32% less energy/bit. This work provides an information-theoretic framework to guide the design and characterization of other analog-valued emerging memory such as RRAM and CBRAM.

## An LDPC Coded Adaptive Decode-and-Forward Scheme Based on the EESM Model

- **Status**: ❌
- **Reason**: EESM 기반 적응형 DF 협력 통신 기법. LDPC는 부수 언급, 무선 스펙트럼 효율 특이적
- **ID**: ieee:7061713
- **Type**: conference
- **Published**: 13-14 Dec.
- **Authors**: Xiang Chen, Ming-Xiang Xie
- **PDF**: https://ieeexplore.ieee.org/document/7061713
- **Abstract**: User Cooperation is a promising technology to obtain diversity gain at terminals. According to the traditional decode-and-forward scheme, relay node help to transmit source node's information with fixed number of modulation symbols all the time. It is not optimal in view of spectral efficiency, especially when the channel state is good. This paper introduces the adaptive DF scheme based on the minus exponential effective-SNR mapping (EESM) model. The optimal number to relay is predicted accurately. Furthermore, adaptive modulation is supported. The reliability requirement is satisfied, and the radio resource is saved for transmitting new information. Theoretical analysis and simulation results indicate that the adaptive DF scheme improves the spectral efficiency significantly.

## Analog Error Correction Codes Based on Chaotic System: The 2-Dimensional Tent Codes

- **Status**: ❌
- **Reason**: 혼돈계 기반 아날로그 오류정정 코드(2D tent). LDPC가 아닌 아날로그 코드, 비-LDPC 제외
- **ID**: ieee:7061689
- **Type**: conference
- **Published**: 13-14 Dec.
- **Authors**: Xing Hu, Lin-Hua Ma, Le Ru +1
- **PDF**: https://ieeexplore.ieee.org/document/7061689
- **Abstract**: In low signal-to-noise ratio (SNR) scenarios, image wireless transmission is often interrupted due to the "threshold effect" in traditional digital communication system. Fortunately, it can be avoided in analog communication system, owing to its feature of linear degradation to noise. And to design the efficient analog error correction codes is the key to achieve high fidelity image. Considering problems such as low code rate and high encoding and decoding complexity of the existing analog codes, the efficient analog codes based on 2-dimensional tent map are proposed. The new 2-dimensional tent map is built by extending the one-dimensional tent map. The proposed 2-dimensional tent codes perform better than the existing mirrored baker's codes. Simulation results show that compared with the mirrored baker's codes, the peak signal to noise ratio (PSNR) of image can get the gain of more than 3dB, the code rate is doubled, and the encoding and decoding complexity decreases greatly.

## A Multi-base Station Cooperative Algorithm for LDPC-OFDM System in the HF Channel

- **Status**: ❌
- **Reason**: HF 채널 다중기지국 협력 디코딩+정보결합. 무선 협력통신 특이적, NAND ECC에 떼어낼 디코더 기법 없음
- **ID**: ieee:7061687
- **Type**: conference
- **Published**: 13-14 Dec.
- **Authors**: Xiao-Bei Li, Song Zhang, Fei-Hu Zhao +1
- **PDF**: https://ieeexplore.ieee.org/document/7061687
- **Abstract**: Based on LDPC-OFDM system, a multi-base station cooperative algorithm is designed for high frequency (HF) channel, and a LDPC cooperative decoding algorithm is proposed, which adopts information combining strategy based on the probability measure. The center station in the system model uses the multiple signals received from the relay stations to update its received initialization information. This strategy can combine the cooperative communication strategy with LDPC iterative decoding effectively in order to achieve both diversity gain and encoding gain. Simulation results show that the cooperative strategy with the multi-relay stations has better performance in the bit error rate than direct transmission strategy. The decoding performance of DF strategy with a relay station with respect to that of AF strategy has a gain of about 0.7dB at BER = 10-3.

## Modeling and analysis of RFID authentication protocols for supply chain management

- **Status**: ❌
- **Reason**: RFID 인증 프로토콜 보안/공급망 논문, LDPC와 무관
- **ID**: ieee:7030752
- **Type**: conference
- **Published**: 11-13 Dec.
- **Authors**: Adarsh Kumar, Krishna Gopal, Alok Aggarwal
- **PDF**: https://ieeexplore.ieee.org/document/7030752
- **Abstract**: A secure interconnection of objects through RFID technology extends the range of information availability. Security in this integration is achievable through proper identification, authentication, grouping / yoking, distance bounding, and tag and ownership transfer protocols. This work analyzes the computational and communicational cost of group and authentication protocols. Further, these protocols are modeled and analyzed using alloy model. Results show that a network of 255 nodes can be constructed with delays of 9.6 msec and 7.6 msec using peer to peer and centralized connectivity respectively.

## Candidate codeword selection scheme with bit flipping for outer code in overloaded MIMO-OFDM system

- **Status**: ❌
- **Reason**: overloaded MIMO-OFDM 블록부호 joint 디코딩+bit flipping — 무선 응용 특이적, LDPC BP 이식 기법 없음
- **ID**: ieee:7024476
- **Type**: conference
- **Published**: 1-4 Dec. 2
- **Authors**: Yoshihito Doi, Yukitoshi Sanada
- **PDF**: https://ieeexplore.ieee.org/document/7024476
- **Abstract**: This paper presents a candidate codeword selection scheme with bit flipping in two step joint decoding of block coded signals in an overloaded multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) system. In previous literature, the two step joint decoding scheme has been proposed for complexity reduction of maximum likelihood decoding of a block code in the overloaded MIMO system. However, the two step decoding scheme has not been combined with an outer code. The selection of the candidate codewords in the inner block code may not always be able to provide the metric of a binary coded symbol for the outer code. Candidate codewords are then created through bit flipping in the proposed scheme. It is shown that the two step decoding scheme reduces the complexity by about 0.026 for 4 signal streams with the cost of bit error rate degradation within 0.5dB.
