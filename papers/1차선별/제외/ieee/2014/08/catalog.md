# IEEE Xplore — 2014-08


## A Family of Optimal Locally Recoverable Codes

- **Status**: ❌
- **Reason**: LRC(Reed-Solomon 계열) 비-LDPC 부호, 다항식 보간 복구로 LDPC BP에 이식 불가
- **ID**: ieee:6820791
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Itzhak Tamo, Alexander Barg
- **PDF**: https://ieeexplore.ieee.org/document/6820791
- **Abstract**: A code over a finite alphabet is called locally recoverable (LRC) if every symbol in the encoding is a function of a small number (at most  \(r\) ) other symbols. We present a family of LRC codes that attain the maximum possible value of the distance for a given locality parameter and code cardinality. The codewords are obtained as evaluations of specially constructed polynomials over a finite field, and reduce to a Reed-Solomon code if the locality parameter  \(r\)  is set to be equal to the code dimension. The size of the code alphabet for most parameters is only slightly greater than the code length. The recovery procedure is performed by polynomial interpolation over  \(r\)  points. We also construct codes with several disjoint recovering sets for every symbol. This construction enables the system to conduct several independent and simultaneous recovery processes of a specific symbol by accessing different parts of the codeword. This property enables high availability of frequently accessed data (“hot data”).

## Compressing Encrypted Images With Auxiliary Information

- **Status**: ❌
- **Reason**: 암호화 이미지 압축(소스 코딩/양자화), 채널 ECC 아님
- **ID**: ieee:6784133
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Xinpeng Zhang, Yanli Ren, Liquan Shen +2
- **PDF**: https://ieeexplore.ieee.org/document/6784133
- **Abstract**: This paper proposes a novel scheme of compressing encrypted images with auxiliary information. The content owner encrypts the original uncompressed images and also generates some auxiliary information, which will be used for data compression and image reconstruction. Then, the channel provider who cannot access the original content may compress the encrypted data by a quantization method with optimal parameters that are derived from a part of auxiliary information and a compression ratio-distortion criteria, and transmit the compressed data, which include an encrypted sub-image, the quantized data, the quantization parameters and another part of auxiliary information. At receiver side, the principal image content can be reconstructed using the compressed encrypted data and the secret key. Experimental result shows the ratio-distortion performance of the proposed scheme is better than that of previous techniques.

## Separation of Reliability and Secrecy in Rate-Limited Secret-Key Generation

- **Status**: ❌
- **Reason**: 보안 비밀키 생성/정보조정 순수 정보이론 bound; ECC 디코더/HW 기여 없음
- **ID**: ieee:6814952
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Rémi A. Chou, Matthieu R. Bloch
- **PDF**: https://ieeexplore.ieee.org/document/6814952
- **Abstract**: For a discrete or a continuous source model, we study the problem of secret-key generation with one round of rate-limited public communication between two legitimate users. Although we do not provide new bounds on the wiretap secret-key (WSK) capacity for the discrete source model, we use an alternative achievability scheme that may be useful for practical applications. As a side result, we conveniently extend known bounds to the case of a continuous source model. Specifically, we consider a sequential key-generation strategy, that implements a rate-limited reconciliation step to handle reliability, followed by a privacy amplification step performed with extractors to handle secrecy. We prove that such a sequential strategy achieves the best known bounds for the rate-limited WSK capacity (under the assumption of degraded sources in the case of two-way communication). However, we show that, unlike the case of rate-unlimited public communication, achieving the reconciliation capacity in a sequential strategy does not necessarily lead to achieving the best known bounds for the WSK capacity. Consequently, reliability and secrecy can be treated successively but not independently, thereby exhibiting a limitation of sequential strategies for rate-limited public communication. Nevertheless, we provide scenarios for which reliability and secrecy can be treated successively and independently, such as the two-way rate-limited SK capacity, the one-way rate-limited WSK capacity for degraded binary symmetric sources, and the one-way rate-limited WSK capacity for Gaussian degraded sources.

## Energy-Efficient Soft-Input Soft-Output Signal Detector for Iterative MIMO Receivers

- **Status**: ❌
- **Reason**: MIMO sphere decoder(검출기) VLSI, LDPC 디코더 아키텍처가 아니라 MIMO 검출기 특화로 이식 불가
- **ID**: ieee:6755579
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Liang Liu
- **PDF**: https://ieeexplore.ieee.org/document/6755579
- **Abstract**: This paper presents the VLSI design of an energy-efficient, high-throughput soft-input soft-output signal detector for iterative multiple-input multiple-output (MIMO) receiver. The detector is evolved from our previously developed imbalanced fixed complexity sphere decoder and adopts several new algorithm-level techniques to exploit the available a priori information of transmitted bits. More specifically, an adaptive tree-travel control scheme, a reliability-dependent log-likelihood ratio correction method and an iteration-based hybrid node enumeration technique are proposed to provide near-optimal detection performance with much reduced computational complexity. A multi-stage parallel VLSI architecture is developed to implement the proposed algorithm with high detection throughput. Furthermore, the block-level clock gating is deployed to save power when the tree-search space is reduced, while still preserving the constant-throughput feature. As a proof of concept, we designed the iterative detector using a 65-nm CMOS technology and conducted post-layout simulation. The core area is 0.64 mm 2 with 198.2 k gates. Working at 240-MHz clock frequency with 1.0-V voltage supply, the detector achieves a maximum 1.44-Gbps throughput. Under frequency-selective channels, the detector core consumes 98.5-, 127.9-, and 149.5-pJ energy per bit detection in open-loop, 2-iteration, and 4-iteration modes, respectively.

## Distributed Fountain Codes With Adaptive Unequal Error Protection in Wireless Relay Networks

- **Status**: ❌
- **Reason**: fountain 코드 기반 분산 네트워크 코딩 UEP, fountain/네트워크코딩은 제외이며 떼어낼 LDPC 기법 없음
- **ID**: ieee:6781551
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Jing Yue, Zihuai Lin, Branka Vucetic
- **PDF**: https://ieeexplore.ieee.org/document/6781551
- **Abstract**: In wireless relay networks (WRNs), multiple source nodes communicate with a single destination node through a common relay network. Different source nodes may have different error protection or recovery time requirements. In this paper, we focus on unequal error protection (UEP) distributed network coding (DNC) design for WRNs. Specifically, we propose a continuous UEP method based on fountain codes with the objective of satisfying the UEP or unequal recovery time (URT) requirements. Then based upon this UEP method, we develop an adaptive UEP DNC scheme to realize adaptive UEP in WRNs. We analyze the properties of the proposed adaptive UEP DNC scheme and derive the upper and lower bit error rate (BER) bounds for it over Rayleigh fading channels under maximum-likelihood (ML) decoding. Simulation results show that the proposed adaptive UEP DNC scheme has desirable UEP and URT properties. The transmitted data from the source nodes in different protection groups can be recovered successfully under their performance requirements in a shorter time by using the adaptive UEP DNC scheme.

## Layer-Aligned Multipriority Rateless Codes for Layered Video Streaming

- **Status**: ❌
- **Reason**: rateless/fountain 코드 기반 계층 비디오 스트리밍 UEP, fountain은 기준상 제외이며 떼어낼 ECC 기법 없음
- **ID**: ieee:6727474
- **Type**: journal
- **Published**: Aug. 2014
- **Authors**: Hsu-Feng Hsiao, Yong-Jhih Ciou
- **PDF**: https://ieeexplore.ieee.org/document/6727474
- **Abstract**: There exists a multitude of techniques, including automatic repeat request and error correction codes, to minimize data corruption when transmitting over error-prone networks. Streaming of multimedia data can usually withstand a certain level of data loss, yet have strict limitations on the latency tolerance. To enable acceptable reliability of transmission and low transmission latency, the channel coding approach is usually more appealing at the cost of additional bandwidth. In this paper, an  $N$ -cycle layer-aligned overlapping structure, which is good for layered data, is proposed. Accordingly, layer-aligned multipriority rateless codes were developed with favorable probabilities to control the protection strength for each layer of the streaming data. The major contribution of this paper is the analytical model developed to predict the failure decoding probabilities for each video layer and it is shown to achieve accurate estimation. A prediction model to estimate the expected decompressible video frames was developed for use with the developed codes for streaming scalable videos. By maximizing the number of expected decompressible video frames, the protection strength of the developed codes can then be determined. Simulation results show that the developed codes are good for streaming layered videos, which are difficult to deal with using traditional rateless codes, with or without unequal error protection.

## Application of protograph-based LDPC codes in underwater acoustic channels

- **Status**: ❌
- **Reason**: 수중음향 채널(UWA) ISI 특화 protograph LDPC 코드 설계 — 채널 특이적이고 떼어낼 일반 NAND 이식 기법 없음
- **ID**: ieee:6986332
- **Type**: conference
- **Published**: 5-8 Aug. 2
- **Authors**: Zhenhua Chen, Xiaomei Xu, Yougan Chen
- **PDF**: https://ieeexplore.ieee.org/document/6986332
- **Abstract**: We consider the application of protograph-based low density parity check (LDPC) codes with a remarkable reduction encoding time relative to MacKay's LDPC codes for underwater acoustic (UWA) channels. It's observed that the conventional protograph-based LDPC codes, e.g. AR4JA, which have excellent performance in AWGN channels may not accomplish in UWA channels as well when the code lengths of them are short. In this paper, we propose a protograph LDPC code to adopt the UWA channels which suffer from severe inter-symbol interference (ISI) produced by long multipath delay spreading and bandwidth extremely limited by acoustic propagation loss. The simulation results show that the proposed code outperforms MacKay's (3, 6) LDPC codes by O.SdB and the rate-1/2 of AR4JA code by over ldB with 2048 bits code length in the NSVG and ISVG underwater channels, at near to 10-5 of the BER. In addition, over the two UWA channel models, the performances of the proposed code in BER do not degrade obviously when code lengths are decreasing. Consequently, the proposed code is a good alternative code to improve the operation speed, reliability and robustness of UWA communication system.

## Performance analysis of DVB-NGH MIMO coded modulation system

- **Status**: ❌
- **Reason**: DVB-NGH MIMO 코디드 모듈레이션 성능분석 — LDPC 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:6906355
- **Type**: conference
- **Published**: 4-8 Aug. 2
- **Authors**: Tao Cheng, Kewu Peng, Fang Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/6906355
- **Abstract**: Digital video broadcasting-next generation handheld (DVB-NGH) is the first broadcasting standard that incorporates multiple-input multiple-output (MIMO) techniques to overcome the Shannon limit of single antenna systems. This paper contributes to analyze the performance of the DVB-NGH MIMO coded modulation system. The detailed performance degradation from information-theoretic limit to implementation by average mutual information and extrinsic information transfer analysis is presented, which provides an insight guideline for future system improvement. Finally, bit error rate simulations are carried out to verify the analysis.

## Symbol-based parallel message-passing decoding on partial-response channels

- **Status**: ❌
- **Reason**: PR채널 q-ary(비이진) LDPC와 결합한 심볼기반 병렬 메시지패싱, 비이진 LDPC라 제외
- **ID**: ieee:6916686
- **Type**: conference
- **Published**: 30 July-1 
- **Authors**: Wicharn Singhaudom, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/6916686
- **Abstract**: Idea of parallel message passing (PMP) between detector and decoder has been studied. The PMP aims to achieve very-high speed decoder. This view point is extremely important in magnetic recording systems where data rate must be high but decoding delay should be low. Recently, the result of symbol based (SB) PMP decoding compared with SB-TE (SB-BCJR combined with q-ary LDPC) on PR channels is presented. However, the bit error rate cannot be equivalent to the SB-BCJR. Motivated by this issue, we introduced cycle-free SB-PMP detector combined with usage of optimal schedule in exchanging information between detector and decoder. Our proposed system could achieve both high speed decoding and identical performance to SB-TE. Additional, alternative method to construct a trellis for SB-PMP detector was presented.

## Secret key management and dynamic security coding system

- **Status**: ❌
- **Reason**: 암호화/보안 키관리 시스템, 채널 ECC LDPC 기법 아님(보안 원칙 제외)
- **ID**: ieee:6916762
- **Type**: conference
- **Published**: 30 July-1 
- **Authors**: Thi Huyen Trang Nguyen, Jean-Pierre Barbot
- **PDF**: https://ieeexplore.ieee.org/document/6916762
- **Abstract**: Digital information transmission systems must satisfy two requirements: reliability and confidentiality. In terms of reliability we tend nowadays to the Shannon's capacity, i.e. the limit of errorless data rate. Concerning the confidentiality of transmissions, a perfect secrecy limit was also defined by Shannon but this aspect of the Shannon's work was less adressed. Nevertheless, in order to enhance the security of transmissions, especially with wireless systems, an encryption is often used. In this contribution, we present an encryption scheme that jointly protect the exchange of information against eavesdropper as well as errors due to the propagation channel. The key controlling the encryption scheme is dynamically generated and propagation measurements will be used to illustrate the importance of the key length.

## Noise mitigation over Powerline communication using LDPC-Convolutional Code and fusion of mean and median filters

- **Status**: ❌
- **Reason**: PLC OFDM 임펄스 노이즈 완화 + LDPC-CC; 떼어낼 LDPC 디코더/구성 기여 없고 신호처리(필터 융합) 중심, 통신 응용 특이적
- **ID**: ieee:7514467
- **Type**: conference
- **Published**: 28-30 Aug.
- **Authors**: Yassine Himeur, Abdelkrim Boukabou
- **PDF**: https://ieeexplore.ieee.org/document/7514467
- **Abstract**: In this paper, we propose a new impulse noise mitigation approach in Orthogonal Frequency Division Multiplexing (OFDM) signals over Powerline communication (PLC) channel. Recently LDPC-Convolutional Code (LDPC-CC) has received much interest as an alternative to LDPC codes for its advantages and low complexity. The proposed approach exploits the redundancy introduced by LDPC-CC and cyclic prefix (CP) added to the OFDM transmitter to recover noisy coefficients. It is based on the fusion of median and mean of their neighboring coefficients using a window and a dynamic threshold calculated on the basis of noise variance and the peak value of the noise in the received signal. Detection of noisy coefficients takes into consideration the neighboring coefficients. The proposed technique presents a good robustness to impulse noise performance without adding a big complexity to the transmission system. Promising results have been achieved by the proposed approach when compared to filtering and coding techniques alone.

## Enhancement of practically deployable indoor VLC system with LDPC code

- **Status**: ❌
- **Reason**: 실내 VLC 시스템에 LDPC 적용 시연; LDPC는 부수 FEC, 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:6950627
- **Type**: conference
- **Published**: 27-29 Aug.
- **Authors**: Xiang Zhang, Min Zhang, Dahai Han +2
- **PDF**: https://ieeexplore.ieee.org/document/6950627
- **Abstract**: The enhanced visible light communications (VLC) system with transmission distance of 6m is demonstrated using transmission path design and forward error correction code in this paper. The experimental results suggest that based on the given power and 10-3 bit error rate, in comparison with uncoded system, average communication distance increases 45%, communication area increases 236% with LDPC cod...

## Bit Error Recovery in ECOC Systems through LDPC Codes

- **Status**: ❌
- **Reason**: LDPC를 ECOC 다중분류 시스템에 적용 — 채널 ECC가 아닌 분류기, 떼어낼 디코더/HW/구성 기여 없음
- **ID**: ieee:6976969
- **Type**: conference
- **Published**: 24-28 Aug.
- **Authors**: Claudio Marrocco, Francesco Tortorella
- **PDF**: https://ieeexplore.ieee.org/document/6976969
- **Abstract**: Error Correcting Output Coding (ECOC) is a widely used and successful technique that implements a classification system by splitting a multiclass problem into a set of dichotomies according to a coding matrix. In this paper we propose a new approach for the ECOC systems based on a well-known family of error correcting codes in the Coding Theory: the Low Density Parity Check (LDPC) codes. The goal is twofold: first, to introduce a new coding strategy for determining the code words to be collected in a coding matrix. Second, to exploit the algebraic properties of LDPC codes for recovering the bit errors in the output word and increasing the performance of the classification system. We compare the proposed technique with other commonly used coding strategies on some benchmark data sets achieving very interesting results.

## Information shortening for joint source-channel coding schemes based on low-density parity-check codes

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) shortening — LDPC 베이스라인, 채널 ECC 기법 아님(제외 JSCC)
- **ID**: ieee:6955098
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: H. V. Beltrão Neto, W. Henkel
- **PDF**: https://ieeexplore.ieee.org/document/6955098
- **Abstract**: We propose a simple shortening algorithm for joint source-channel coding schemes based on low-density parity-check codes. Due to finite-length effects, such systems present high error floors when optimised for low-entropy binary symmetric sources and transmission over an AWGN channel. To mitigate such effects, we propose the reduction of the compression rate by inserting infinite reliability variable nodes which form cycles with length equal to the girth of the code used as source compressor. Simulation results show that such a strategy is able to efficiently trade a slight reduction of the compression rate for a significant performance enhancement.

## Low latency-constrained high rate coding: LDPC codes vs. convolutional codes

- **Status**: ❌
- **Reason**: 구조적 지연 관점 LDPC vs 컨볼루셔널 부호 비교, 이론적 latency bound만 다룸 — 떼어낼 신규 디코더/구성/HW 기법 없음
- **ID**: ieee:6955117
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Christoph Rachinger, Ralf Müller, Johannes B. Huber
- **PDF**: https://ieeexplore.ieee.org/document/6955117
- **Abstract**: This paper complements and generalizes the results in [1], [2] while taking new formulas from [3] into account. We compare convolutional and LDPC codes of different rates with respect to their structural delay. This property is intrinsic to the encoding and decoding process and gives a fundamental limit to the achievable latency for end-to-end communication, even when infinite processing speed is assumed. We show that in the case of very low delay convolutional codes perform better than LDPC codes and even break fundamental existence bounds for block codes for some rates. Furthermore, non-punctured convolutional codes can benefit from their shorter constraint length and reduce the delay further.

## Estimation of the decoding threshold of LDPC codes over the q-ary partial erasure channel

- **Status**: ❌
- **Reason**: q-ary partial erasure 채널 비이진 LDPC 디코딩 임계값 — 비이진 LDPC, 순수 임계값 분석이라 제외
- **ID**: ieee:6955113
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Rami Cohen, Yuval Cassuto
- **PDF**: https://ieeexplore.ieee.org/document/6955113
- **Abstract**: In this paper, we discuss bounds and approximations for the decoding threshold of LDPC codes over the q-ary partial erasure channel (QPEC), introduced in [1]. The QPEC has a q-ary input, and its output is either one symbol or a set of 2 ≤ M ≤ q possible symbols. We show how an upper bound on the decoding threshold can be derived using a single-letter recurrence relation, when M > q/2. In addition, we discuss complexity issues in the calculation of the threshold, and provide two approximation models that lead to reasonable results with a fraction of the complexity required for the exact calculation.

## Low-complexity fixed-to-fixed joint source-channel coding

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합 코딩), 표준 QC-LDPC+BP를 베이스라인으로 사용, 떼어낼 신규 ECC 기법 없음 — 제외
- **ID**: ieee:6955100
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Irina E. Bocharova, Albert Guillén i Fabregas, Boris D. Kudryashov +3
- **PDF**: https://ieeexplore.ieee.org/document/6955100
- **Abstract**: A source-channel coding scheme in which source messages are assigned to two classes and encoded using a channel code that depends on the class index is studied. A low-complexity implementation with two quasi-cyclic LDPC codes with belief-propagation decoding achieves a better frame error rate than optimized separate coding. The coding gain obtained by simulation is consistent with the theoretical gain.

## Construction of non-binary LDPC codes: A matrix-theoretic approach

- **Status**: ❌
- **Reason**: 비이진 LDPC 구성(matrix-theoretic) — 비이진 LDPC라 제외
- **ID**: ieee:6955115
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Juane Li, Keke Liu, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/6955115
- **Abstract**: This paper presents a matrix-theoretic approach to the construction of non-binary LDPC codes. Two algebraic methods for constructing non-binary LDPC codes are presented. The proposed construction methods have several ingredients including base matrix, matrix-dispersion, masking and replacement. By proper choice and combination of these ingredients, non-binary LDPC codes with good performance can be constructed.

## A symbol flipping decoder for NB-LDPC relying on multiple votes

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) symbol-flipping 디코더 — 비이진 LDPC라 제외
- **ID**: ieee:6955114
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Francisco García-Herrero, David Declercq, Javier Valls
- **PDF**: https://ieeexplore.ieee.org/document/6955114
- **Abstract**: In this paper, we present an algorithm to decode non-binary LDPC (NB-LDPC) codes, inspired from very-high throughput symbol-flipping decoders that have been proposed recently. Usually, the symbol-flipping decoders suffer from a non-negligible performance degradation compared to soft-decision NB-LDPC decoders. Our improved decoder makes use of a list of syndrome computations instead of a single one, and builds soft information at the symbol node input by assigning votes with different weights to the elements of the list. We show by simulations that using multiple votes results in better performance, while still maintaining the high throughput feature.

## Spatially coupled turbo codes

- **Status**: ❌
- **Reason**: spatially coupled turbo codes — 비-LDPC(turbo) 부호, DE 분석만이고 LDPC BP에 이식할 디코더 기법 없음
- **ID**: ieee:6955090
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Saeedeh Moloudi, Michael Lentmaier, Alexandre Graell i Amat
- **PDF**: https://ieeexplore.ieee.org/document/6955090
- **Abstract**: In this paper, we introduce the concept of spatially coupled turbo codes (SC-TCs), as the turbo codes counterpart of spatially coupled low-density parity-check codes. We describe spatial coupling for both Berrou et al. and Benedetto et al. parallel and serially concatenated codes. For the binary erasure channel, we derive the exact density evolution (DE) equations of SC-TCs by using the method proposed by Kurkoski et al. to compute the decoding erasure probability of convolutional encoders. Using DE, we then analyze the asymptotic behavior of SC-TCs. We observe that the belief propagation (BP) threshold of SC-TCs improves with respect to that of the uncoupled ensemble and approaches its maximum a posteriori threshold. This phenomenon is especially significant for serially concatenated codes, whose uncoupled ensemble suffers from a poor BP threshold.

## Optimized codes for the binary coded side-information problem

- **Status**: ❌
- **Reason**: binary coded side-information(소스 코딩/분산소스) 문제, 채널 ECC가 아님 — 제외
- **ID**: ieee:6955099
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Anne Savard, Claudio Weidmann
- **PDF**: https://ieeexplore.ieee.org/document/6955099
- **Abstract**: This paper analyzes a practical scheme for the binary coded side-information problem based on LDPC codes and trellis quantization. A recently proposed improved decoder is shown to be amenable to numerical density evolution and thus to LDPC code optimization. First results display significant gains compared to off-the-shelf codes, which could be further improved by refined modeling of the system.

## Low-complexity LDPC-coded iterative MIMO receiver based on belief propagation algorithm for detection

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) 기반 MIMO-BP 수신기 — 비이진 LDPC + 무선 응용 특이적이라 제외
- **ID**: ieee:6955116
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Ali Haroun, Charbel Abdel Nour, Matthieu Arzel +1
- **PDF**: https://ieeexplore.ieee.org/document/6955116
- **Abstract**: A low-complexity Multiple Input Multiple Output receiver based on Belief Propagation (MIMO-BP) detector associated with a Non-Binary Low Density Parity Check (NB-LDPC) decoder is proposed in this paper. Such detection and decoding algorithms are represented thanks to a larger Joint Factor Graph. Shuffle schedule is also applied to efficiently exchange information between the detector and the decoder. Actions are undertaken at the detector, decoder and the iterative receiver levels in order to reduce overall computational complexity. An important reduction in terms of operations per iteration is obtained with a negligible performance penalty. Then, EXtrinsic Information Transfer (EXIT) charts are used to find a schedule in terms of number of iterations to be performed for which the proposed receiver achieves error correction performance similar to that of a full-complexity iterative MIMO receiver.

## Density evolution for SUDOKU codes on the erasure channel

- **Status**: ❌
- **Reason**: SUDOKU 부호용 BP(비선형 제약, 알파벳 순열 불변), erasure 채널 — NAND 바이너리 LDPC로 이식할 기법 없음
- **ID**: ieee:6955120
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Caroline Atkins, Jossy Sayir
- **PDF**: https://ieeexplore.ieee.org/document/6955120
- **Abstract**: Codes based on SUDOKU puzzles are discussed, and belief propagation decoding introduced for the erasure channel. Despite the non-linearity of the code constraints, it is argued that density evolution can be used to analyse code performance due to the invariance of the code under alphabet permutation. The belief propagation decoder for erasure channels operates by exchanging messages containing sets of possible values. Accordingly, density evolution tracks the probability mass functions of the set cardinalities. The equations governing the mapping of those probability mass functions are derived and calculated for variable and constraint nodes, and decoding thresholds are computed for long SUDOKU codes with random interleavers.

## A general procedure to design good codes at a target BER

- **Status**: ❌
- **Reason**: BMST(block Markov superposition) 시스템 설계 — LDPC 부호 아님, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6955092
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Chulong Liang, Xiao Ma, Qiutao Zhuang +1
- **PDF**: https://ieeexplore.ieee.org/document/6955092
- **Abstract**: This paper presents a systematic design methodology for block Markov superposition transmission (BMST) systems to approach the channel capacity at any given target bit-error-rate (BER) of interest. To simplify the design, we choose the basic code as the Cartesian product of a short block code. The encoding memory is then inferred from the genie-aided lower bound according to the performance gap of the short block code to the corresponding Shannon limit at the target BER. In addition to the sliding-window decoding algorithm, we propose to perform one more phase decoding to remove residual (rare) errors. A new technique that assumes a noisy genie is proposed to upper bound the performance. Under some assumptions, these genie-aided bounds can be used to predict the performance of the proposed two-phase decoding algorithm in the extremely low BER region. Using the Cartesian product of a repetition code as the basic code, we construct a BMST system with an encoding memory 30 whose performance at the BER of 10-15 can be predicted over the binary-input additive white Gaussian noise channel (BI-AWGNC).

## Asymptotic analysis and design of iterative receivers for non linear ISI channels

- **Status**: ❌
- **Reason**: 비선형 위성채널 반복수신기 EXIT 최적화, 비이진 변조 응용 특이적, 떼어낼 LDPC 기법 없음 — 제외
- **ID**: ieee:6955108
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Bouchra Benammar, Nathalie Thomas, Charly Poulliat +2
- **PDF**: https://ieeexplore.ieee.org/document/6955108
- **Abstract**: In this paper, iterative receiver analysis and design for non linear satellite channels is investigated. To do so, an EXtrinsic Information Transfer (EXIT) chart-based optimization is applied using two major assumptions: the equalizer outputs follow a Gaussian Mixture distribution since we use non-binary modulations and partial interleavers are used between the Low Density Parity Check (LDPC) code and the mapper. Achievable rates, performance and thresholds of the optimized receiver are analysed. The objective in fine is to answer the question: Is it worth optimizing an iterative receiver for non linear satellite channels?

## Soft-in soft-out algorithms for the Nordstrom-Robinson code

- **Status**: ❌
- **Reason**: Nordstrom-Robinson 비선형 블록부호 SISO 복호 — LDPC 아님, 부호 특정 복호
- **ID**: ieee:6955079
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Yannick Saouter
- **PDF**: https://ieeexplore.ieee.org/document/6955079
- **Abstract**: The Nordstrom-Robinson code is a binary nonlinear code of length 16 with 28 = 256 codewords. Its minimum distance which is equal to 6 is greater than that of any binary linear code of length 16 and encoding rate 1/2. For this reason, the Nordstrom-Robinson code has attracted interests in practical applications of the communication area. In this paper, we present two new algorithms for soft decoding of this code.

## The PPM poisson channel: Finite-length bounds and code design

- **Status**: ❌
- **Reason**: 비이진(GF(q)) protograph LDPC + PPM Poisson 채널 유한길이 bound — 비이진 LDPC라 제외
- **ID**: ieee:6955112
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Flavio Zabini, Balázs Matuz, Gianluigi Liva +2
- **PDF**: https://ieeexplore.ieee.org/document/6955112
- **Abstract**: This work investigates the finite-length block error probability for the pulse position modulation (PPM) Poisson channel. Amongst, expressions for the Gallager random coding bound (RCB) and the Gaussian approximation of the converse theorem are derived. Likewise, we introduce an erasure channel (EC) approximation that allows the application of known EC bounds to the PPM Poisson channel by matching the channel capacities. We show that the derived benchmarks are not only simple to compute, but also accurate. Additionally, the design of protograph-based non-binary low-density parity-check (LDPC) codes for the (PPM) Poisson channel is addressed. The order q of the finite field is directly matched to the PPM order, so that no iterative message exchange between the decoder and the demodulator is required. The suggested design turns out to be robust w.r.t. different channel parameters, yielding performances within 0.5 dB from the theoretical benchmarks.

## Low-latency polar codes via hybrid decoding

- **Status**: ❌
- **Reason**: polar code 전용 하이브리드 SC/ML 디코더, polar 구조에 의존 — 바이너리 LDPC BP로 이식 불가
- **ID**: ieee:6955118
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Bin Li, Hui Shen, David Tse +1
- **PDF**: https://ieeexplore.ieee.org/document/6955118
- **Abstract**: In this paper, we propose a family of hybrid decoders for polar codes. By decomposing the overall polar code into an inner code and an outer code, a hybrid decoder in the family uses successive cancellation (SC) to decode the inner code and maximum-likelihood (ML) to decode the outer code. At one extreme in the family is the ML decoder, when the entire polar code is viewed as the outer code; at the other extreme is the SC decoder, when the entire polar code is viewed as the inner code. Since ML decoding has lower latency than SC decoding, a hybrid decoder can achieve lower latency than the conventional SC decoder, at the expense of higher complexity due to the ML decoding of the outer code. We propose a reduction in the complexity of ML decoding by exploiting the structure of polar codes.

## Joint FEC encoder and linear precoder design for MIMO systems with antenna correlation

- **Status**: ❌
- **Reason**: MIMO FEC+선형 프리코더 결합 설계(EXIT chart 매칭), 무선 채널 특이적 — 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:6955126
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Chongbin Xu, Peng Wang, Zhonghao Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6955126
- **Abstract**: We study transmissions in multiple-input multiple-output (MIMO) systems with antenna correlation. We focus on joint forward error correction (FEC) encoder and linear precoder design based on channel covariance information at the transmitter (CCIT). We aim to optimize the system performance using the extrinsic information transfer (EXIT) chart type curve matching principle. By adopting a Hadamard precoding technique, we show that, the EXIT chart type curve of the precoded system is asymptotically determined by the channel correlation matrix at the transmitter as the number of receive antennas tends to infinity. The encoder-precoder curve matching can be made asymptotically accurate even in the lack of full channel state information at the transmitter (CSIT). Excellent performance based on this strategy is demonstrated by simulation results in systems with only a moderately large number of receive antennas.

## Generalized concatenated MIMO system with GMD decoding

- **Status**: ❌
- **Reason**: MIMO용 generalized concatenated code(Golden+RS product), GMD 디코더 — LDPC 아니고 부호 비의존 이식 기법 없음
- **ID**: ieee:6955125
- **Type**: conference
- **Published**: 18-22 Aug.
- **Authors**: Alexey Kreshchuk, Victor Zyablov
- **PDF**: https://ieeexplore.ieee.org/document/6955125
- **Abstract**: In this paper we propose new coded modulation for multiple-input and multiple-output (MIMO) communication systems. This coded modulation is a generalized concatenated code. Its inner code is embedded Golden code which we introduce in this paper with a decoding algorithm. Its outer code is a product code with component Reed-Solomon code. We propose iterative decoding algorithm for this product code. We also propose an generalized minimum distance decoder for generalized concatenated code. The performance of the proposed system is estimated with a computer simulation.

## Coded cooperation with single parity-check turbo-product codes over fast fading channels

- **Status**: ❌
- **Reason**: single parity-check turbo-product 협력통신 부호로 비-LDPC, 무선 협력 응용 특이적, 이식 기법 없음
- **ID**: ieee:6947979
- **Type**: conference
- **Published**: 17-20 Aug.
- **Authors**: Dayan Adionel Guimarães, Geraldo Gil Ramundo Gomes, Guilherme Varela Barbosa +1
- **PDF**: https://ieeexplore.ieee.org/document/6947979
- **Abstract**: This paper describes a new coded cooperation scheme based on single parity-check turbo-product codes. The channel soft-information from the source and the relays are also combined in a novel way at the destination. The scheme has simple encoding and decoding, and unveils potential for large cooperation gains in fast fading channels.

## An unequal coding scheme for remote sensing systems based on CCSDS recommendations

- **Status**: ❌
- **Reason**: CCSDS 영상압축+UEP 채널코딩 결합, LDPC 신규 기법 없음, 떼어낼 ECC 기법 없음
- **ID**: ieee:6947971
- **Type**: conference
- **Published**: 17-20 Aug.
- **Authors**: Christofer Schwartz, Fábio da Silva Marques, Marcelo da Silva Pinho
- **PDF**: https://ieeexplore.ieee.org/document/6947971
- **Abstract**: This paper proposes an unequal error protection (UEP) coding scheme based on two standards recommended by the CCSDS (The Consultative Committee for Space Data Systems). The first recommendation (CCSDS 122.0-B-1) specifies an image compressor for aerospace applications, while the second recommendation (CCSDS 131.0-B-1) specifies channel coding systems on a equal error protection (EEP) scheme. Based on these two recommendations, an UEP can be proposed to enhance the performance of the communication system. The results show gains in PSNR of up to 29 dB on the received image. To achieve these results, a small addition was made into the compressor code to generate a side file with some extra information about the compressed bitstream. This information can be used by the rest of the system to achieve the UEP and helps in some synchronization of the bitstream on the decoder side.

## Proving threshold saturation for nonbinary SC-LDPC codes on the binary erasure channel

- **Status**: ❌
- **Reason**: 비이진(general linear group) SC-LDPC threshold saturation — non-binary LDPC라 제외
- **ID**: ieee:6929239
- **Type**: conference
- **Published**: 16-23 Aug.
- **Authors**: Alexandre Graell i Amat, Iryna Andriyanova, Amina Piemontese
- **PDF**: https://ieeexplore.ieee.org/document/6929239
- **Abstract**: We analyze nonbinary spatially-coupled low-density parity-check (SC-LDPC) codes built on the general linear group for transmission over the binary erasure channel. We prove threshold saturation of the belief propagation decoding to the potential threshold, by generalizing the proof technique based on potential functions recently introduced by Yedla et al. The existence of the potential function is also discussed for a vector sparse system in the general case, and some existence conditions are developed. We finally give density evolution and simulation results for several nonbinary SC-LDPC code ensembles.

## Linear block physical-layer network coding for multiple-user multiple-relay wireless networks

- **Status**: ❌
- **Reason**: 무선 다중릴레이 physical-layer network coding — 떼어낼 LDPC ECC 디코더/HW 기법 없음
- **ID**: ieee:6929288
- **Type**: conference
- **Published**: 16-23 Aug.
- **Authors**: Dong Fang, Alister Burr
- **PDF**: https://ieeexplore.ieee.org/document/6929288
- **Abstract**: We propose a novel scheme for physical-layer network coding (PNC), constructed from linear block codes for multiple-user multiple-relay wireless networks. In the proposed design, each relay computes a linear combination of source symbols, namely, the network coded symbol (NCS) and forwards it to the destination. The destination collects all NCSs and the original source symbols to form a valid codeword of the linear code. The resulting codeword can be decoded to reliably extract the original source symbols. The numerical results show that our proposed design provides m-th order diversity when there are m relays. Moreover, the proposed design provides a significant sum-rate enhancement over the orthogonal multiple access scheme with network coding described in previous literature.

## An introduction to spatially-coupled codes via practical examples

- **Status**: ❌
- **Reason**: spatially-coupled 코드 서베이/사례 소개(braided block, 100G optical) — 신규 디코더/구성/HW 기여 없는 리뷰성, 제외
- **ID**: ieee:6929240
- **Type**: conference
- **Published**: 16-23 Aug.
- **Authors**: Henry D. Pfister, Krishna R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/6929240
- **Abstract**: This paper uses examples to illustrate the ongoing transition in spatially-coupled coding from theory to practice. In the first example, we find that spatially-coupled codes have already been implemented by two different companies for 100 Gb/s optical communications. Both systems use variants of braided block codes, which were introduced even before the term spatial coupling. In the second example, we discuss the multiple-access channel and observe that some gains from spatial coupling were being realized in cellular base stations as early as 2007. Finally, we discuss some open questions regarding spatially-coupled codes.

## Improved multiple folded successive cancellation decoder for polar codes

- **Status**: ❌
- **Reason**: Polar code SC decoder folding 기법 — 부호 의존적이고 LDPC BP에 이식 불가 (비-LDPC 원칙 제외)
- **ID**: ieee:6929238
- **Type**: conference
- **Published**: 16-23 Aug.
- **Authors**: Harish Vangala, Emanuele Viterbo, Yi Hong
- **PDF**: https://ieeexplore.ieee.org/document/6929238
- **Abstract**: Folding is a technique to modify the decoder graph of polar codes based on successive cancellation decoding (SCD). Folding was proposed in [1] and extended to multiple folding (к times) in [2] as a technique to significantly reduce the latency of the SCD of polar codes up to a factor of 2K, without performance loss. The extension in [2] shows folding only for к ≤ 3 due to the rapidly increasing complexity. In this paper, we propose an alternative implementation of the multiple-folding SC decoder, to significantly reduce its complexity. The complexity of the new algorithm is only slightly higher than that of the original SCD for polar codes. As a result, the new algorithm enables to decode longer codes with larger ks, which exhibit significant performance gains, in addition to the latency gain.

## A novel 60 GHz compact-range gigabit wireless access system adopting a large array antenna

- **Status**: ❌
- **Reason**: 60GHz 무선 액세스 시스템/안테나 리뷰, LDPC·ECC 무관
- **ID**: ieee:6929211
- **Type**: conference
- **Published**: 16-23 Aug.
- **Authors**: Miao Zhang, Jiro Hirokawa, Makoto Ando
- **PDF**: https://ieeexplore.ieee.org/document/6929211
- **Abstract**: This paper is a review of a novel compact-range wireless access system proposed for multi-Gb/s data transfer in the 60 GHz band. A large array antenna adopted in the access point generates a quasi-plane wave and forms a stable communication zone proportional to the antenna size. The mobile user standing everywhere within the coverage, receives a stable signal almost free of multi-path. The prototype of a short range gigabit wireless access system including a BB module and a RF front end is established. The system performances such as RF receiving level, bit-error rate and signal-to-noise ratio will be evaluated to verify our proposal.

## The encoding algorithm of non-binary quasi-cyclic LDPC cycle codes on tanner graph

- **Status**: ❌
- **Reason**: non-binary QC-LDPC cycle code 인코딩 — 비이진 LDPC는 제외
- **ID**: ieee:7054293
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Xiuni Wang
- **PDF**: https://ieeexplore.ieee.org/document/7054293
- **Abstract**: A low-density parity-check (LDPC) code of column weight of 2 is known as an LDPC cycle code. In this paper, we study the encoding algorithm about a type of non-binary quasi-cyclic LDPC cycle codes. The position of parity check symbols is located firstly through parity check equations. Then, we show that these parity check symbols can be calculated linearly through the corresponding Tanner graph. It turns out that the decoder can be used as the encoder.

## Work in progress: Data compression of wireless sensor network employing Kalman filter and QC-LDPC codes

- **Status**: ❌
- **Reason**: QC-LDPC를 WSN 데이터 압축(소스코딩)에 사용 — 채널 ECC가 아니고 표준 QC-LDPC 재사용
- **ID**: ieee:7054251
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Jian Zheng, Hongxia Bie, Dijia Xu +2
- **PDF**: https://ieeexplore.ieee.org/document/7054251
- **Abstract**: Considering the fact that the wireless sensor networks (WSNs) need to maintain a long lifetime, there is a great demand to decrease energy dissipation of the sensor. Data compression is an efficient method to solve the problem. This paper proposes a practical and efficient data compression algorithm with high compression and noise-resisted features, in which the quasi-cyclic low-density parity-check (QC-LDPC) codes and the Kalman filters are used to compress the transition data of the sensors and to provide the side information for the joint decoding, respectively. The simulation results prove that the algorithm provides an outstanding performance than the famous syndrome techniques.

## Enhanced MIMO cooperative communication based on signal space diversity

- **Status**: ❌
- **Reason**: MIMO 협력통신 signal space diversity — LDPC 미언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:7054333
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Xiang Gao, Zhanji Wu, Sheng He +2
- **PDF**: https://ieeexplore.ieee.org/document/7054333
- **Abstract**: Cooperative communication enables collaborate mobile terminals to share each other's antennas to construct a virtual multiple-input multiple-output (MIMO) system. Through partitioning a user's code word into two parts, coded cooperation (CC) method integrates cooperation with channel coding and significantly improves the performance. In this paper, CC method is extended to spatial-multiplexing-based MIMO system that terminals and base station (BS) are all equipped with multiple antennas. On the basis of MIMO CC scheme, an enhanced cooperative communication scheme based on signal space diversity (SSD) is proposed. Through jointly using the components interleaver in spatial-multiplexing-based MIMO and mechanism of user collaboration, it can increase the diversity order and achieve impressive gains compared to non-cooperative system and MIMO CC scheme in slow fading channel while maintaining the same information rate, transmit power and bandwidth.

## Research and implementation of adaptive digital pre-distortion in high-speed 32-APSK satellite communication system

- **Status**: ❌
- **Reason**: 32-APSK 위성통신 적응형 디지털 사전왜곡(DPD) — LDPC ECC와 무관
- **ID**: ieee:7054310
- **Type**: conference
- **Published**: 14-16 Aug.
- **Authors**: Celun Liu, Wei Du, Ping Tang +2
- **PDF**: https://ieeexplore.ieee.org/document/7054310
- **Abstract**: Adaptive Digital Pre-distortion (DPD) is applied to the typical traveling wave tube amplifier for high-speed 32-APSK satellite communication system. The paper presents research and implementation of adaptive digital pre-distortion. We show first the transmission system model and the adaptive algorithm based on QR decomposition RLS algorithm to achieve adaptive digital pre-distortion. We also present the hardware architecture of the pre-distorter. Finally, we apply the pre-distorter to an actual satellite communication system whose the modulation is 32-APSK with symbol rate of 162.5MHz. The experimental results show that the linear effect and the performance of the system are greatly improved by the application of adaptive digital pre-distortion.
