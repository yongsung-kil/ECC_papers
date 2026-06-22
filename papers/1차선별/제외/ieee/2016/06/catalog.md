# IEEE Xplore — 2016-06


## On Code Design for Joint Energy and Information Transfer

- **Status**: ❌
- **Reason**: 에너지+정보 동시전송용 비선형 trellis code + LDPC 결합 설계; NLTC 특이적이고 바이너리 LDPC ECC에 이식할 신규 기법 없음
- **ID**: ieee:7462244
- **Type**: journal
- **Published**: June 2016
- **Authors**: Mehdi Dabirnia, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/7462244
- **Abstract**: Harvesting energy from radio frequency signals along with transmitting data through them is appealing for different wireless communication scenarios, such as radio frequency identification (RFID) systems and implantable devices. In this paper, we propose a technique to design nonlinear codes for the use in such systems taking into account both energy transmission and error rate requirements. In particular, we propose using concatenation of a nonlinear trellis code (NLTC) with an outer low-density parity-check (LDPC) code. We design the NLTC based on maximization of its free distance. We give necessary and sufficient conditions for its catastrophicity; in order to avoid catastrophic codes, we connect each designed NLTC to a corresponding linear convolutional code allowing for the use of simpler conditions for verification. Furthermore, we use EXIT charts to design the outer LDPC code while fixing the inner NLTC. Via examples, we demonstrate that our designed codes operate at ~0.8 dB away from the information theoretic limits, and they outperform both regular LDPC codes and optimized irregular LDPC codes for additive white Gaussian noise (AWGN) channels. In addition, we show that the proposed scheme outperforms the reference schemes of concatenating LDPC codes with nonlinear memoryless mappers and using classical linear block codes in a time switching mode.

## BASIC Codes: Low-Complexity Regenerating Codes for Distributed Storage Systems

- **Status**: ❌
- **Reason**: 분산 스토리지 regenerating code(이진 패리티+regenerating), NAND 채널 ECC 디코더·구성 신규 기여 없음
- **ID**: ieee:7452376
- **Type**: journal
- **Published**: June 2016
- **Authors**: Hanxu Hou, Kenneth W. Shum, Minghua Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7452376
- **Abstract**: In distributed storage systems, regenerating codes can achieve the optimal tradeoff between storage capacity and repair bandwidth. However, a critical drawback of existing regenerating codes, in general, is the high coding and repair complexity, since the coding and repair processes involve expensive multiplication operations in finite field. In this paper, we present a design framework of regenerating codes, which employ binary addition and bitwise cyclic shift as the elemental operations, named BASIC regenerating codes. The proposed BASIC regenerating codes can be regarded as a concatenated code with the outer code being a binary parity-check code, and the inner code being a regenerating code utilizing the binary parity-check code as the alphabet. We show that the proposed functional-repair BASIC regenerating codes can achieve the fundamental tradeoff curve between the storage and repair bandwidth asymptotically of functional-repair regenerating codes with less computational complexity. Furthermore, we demonstrate that the existing exact-repair product-matrix construction of regenerating codes can be modified to exact-repair BASIC product-matrix regenerating codes with much less encoding, repair, and decoding complexity from the theoretical analysis, and with less encoding time, repair time, and decoding time from the implementation results.

## Constructions of Optimal Binary Locally Repairable Codes With Multiple Repair Groups

- **Status**: ❌
- **Reason**: 분산 스토리지 LRC를 단순 XOR 패리티/regular LDPC로 구성; NAND 채널 ECC 디코더·HW 신규 기여 없음
- **ID**: ieee:7426763
- **Type**: journal
- **Published**: June 2016
- **Authors**: Jie Hao, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/7426763
- **Abstract**: In distributed storage systems, locally repairable codes (LRCs) have attracted lots of interest recently. If a code symbol can be repaired respectively by t disjoint groups of other symbols, each of which has size at most r, we say that the code symbol has (r, t)-locality. LDPC codes are linear block codes defined by low-density parity-check matrices. A regular (τ, p)-LDPC code has the parity-check matrix with uniform column weight τ and uniform row weight p. In this letter, we employ regular LDPC codes to construct optimal binary LRCs with (r, t)-locality for information symbols. After proposing construction frameworks, three detailed constructions of binary LRCs with information locality are obtained, all of which have a single parity symbol in each repair group. All our codes attain the distance bounds of LRCs when each repair group contains a single parity symbol and thus are optimal. For storage systems with hot data, the proposed binary LRCs seem promising for system implementations since the encoding, repairing, parallel reading, and data reconstruction can be performed by simple XOR operations.

## Tag Memory-Erasure Tradeoff of RFID Grouping Codes

- **Status**: ❌
- **Reason**: RFID grouping code의 memory-erasure tradeoff 이론, LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:7440837
- **Type**: journal
- **Published**: June 2016
- **Authors**: Mike Burmester, Jorge Munilla
- **PDF**: https://ieeexplore.ieee.org/document/7440837
- **Abstract**: We analyze the memory-erasure tradeoff of recently proposed radio frequency identification (RFID) grouping codes. Grouping codes make it possible for an RFID reader to automatically verify the integrity of a collection of RFID tagged objects and identify any missing objects without having access to external sources. They add redundancy to the memory of tags that is then used to recover missing tag identification data (forward error correction). We present a lower bound for the redundancy and show that it can be realized asymptotically. We then consider optimized approximations for practical settings and show that their memory-erasure tradeoff is close to optimal and significantly less than that of recently proposed grouping codes.

## Optimizing Transmission Lengths for Limited Feedback With Nonbinary LDPC Examples

- **Status**: ❌
- **Reason**: 비이진(NB) LDPC 사용 + 피드백 전송길이 최적화로 비이진 LDPC 제외 대상
- **ID**: ieee:7426758
- **Type**: journal
- **Published**: June 2016
- **Authors**: Kasra Vakilinia, Sudarsan V. S. Ranganathan, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/7426758
- **Abstract**: This paper presents a general approach for optimizing the number of symbols in increments (packets of incremental redundancy) in a feedback communication system with a limited number of increments. This approach is based on a tight normal approximation on the rate for successful decoding. Applying this approach to a variety of feedback systems using nonbinary (NB) low-density parity-check (LDPC) codes shows that greater than 90% of capacity can be achieved with average blocklengths fewer than 500 transmitted bits. One result is that the performance with ten increments closely approaches the performance with an infinite number of increments. The paper focuses on binary-input additive-white Gaussian noise (BI-AWGN) channels but also demonstrates that the normal approximation works well on examples of fading channels as well as high-SNR AWGN channels that require larger QAM constellations. This paper explores both variable-length feedback codes with termination (VLFT) and the more practical variable length feedback (VLF) codes without termination that require no assumption of noiseless transmitter confirmation. For VLF, we consider both a two-phase scheme and CRC-based scheme.

## ADMM LP Decoding of Non-Binary LDPC Codes in  $ \mathbb {F}_{2^{m}}$

- **Status**: ❌
- **Reason**: non-binary LDPC(F_2^m) ADMM LP 디코더; 비이진 LDPC는 제외
- **ID**: ieee:7453187
- **Type**: journal
- **Published**: June 2016
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7453187
- **Abstract**: In this paper, we develop efficient decoders for non-binary low-density parity-check codes using the alternating direction method of multipliers (ADMM). We apply ADMM to two decoding problems. The first problem is linear programming (LP) decoding. In order to develop an efficient algorithm, we focus on non-binary codes in fields of characteristic two. This allows us to transform each constraint in  $ \mathbb {F}_{2^{m}}$  to a set of constraints in  $ \mathbb {F}_{2}$  that has a factor graph representation. Applying ADMM to the LP decoding problem results in two types of non-trivial sub-routines. The first type requires us to solve an unconstrained quadratic program. We solve this problem efficiently by leveraging new results obtained from studying the above factor graphs. The second type requires Euclidean projections onto polytopes that are studied in the literature. Such projections can be solved efficiently using off-the-shelf techniques, which scale linearly in the dimension of the vector to project. ADMM LP decoding scales linearly with block length, linearly with check degree, and quadratically with field size. The second problem we consider is a penalized LP decoding problem. This problem is obtained by incorporating a penalty term into the LP decoding objective. The purpose of the penalty term is to make non-integer solutions (pseudocodewords) more expensive and hence to improve decoding performance. The ADMM algorithm for the penalized LP problem requires Euclidean projection onto a polytope formed by embedding the constraints specified by the non-binary single parity-check code, which can be solved by applying the ADMM technique to the resulting quadratic program. Empirically, this decoder achieves a much reduced error rate than LP decoding at low signal-to-noise ratios.

## Bounds on the Parameters of Locally Recoverable Codes

- **Status**: ❌
- **Reason**: Locally Recoverable Code 파라미터 bound 순수 이론으로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7384487
- **Type**: journal
- **Published**: June 2016
- **Authors**: Itzhak Tamo, Alexander Barg, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/7384487
- **Abstract**: A locally recoverable code (LRC code) is a code over a finite alphabet, such that every symbol in the encoding is a function of a small number of other symbols that form a recovering set. In this paper, we derive new finite-length and asymptotic bounds on the parameters of LRC codes. For LRC codes with a single recovering set for every coordinate, we derive an asymptotic Gilbert-Varshamov type bound for LRC codes and find the maximum attainable relative distance of asymptotically good LRC codes. Similar results are established for LRC codes with two disjoint recovering sets for every coordinate. For the case of multiple recovering sets (the availability problem), we derive a lower bound on the parameters using expander graph arguments. Finally, we also derive finite-length upper bounds on the rate and the distance of LRC codes with multiple recovering sets.

## Performance Improvement of JSCC Scheme Through Redesigning Channel Code

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합) DP-LDPC 채널코드 재설계; JSCC는 떼어낼 ECC 기법 없어 제외
- **ID**: ieee:7452543
- **Type**: journal
- **Published**: June 2016
- **Authors**: Qiwang Chen, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/7452543
- **Abstract**: For joint source channel coding (JSCC) scheme based on double protograph low-density parity-check (DP-LDPC) codes, due to joint iterative decoding between the source and channel decoders, it is found that the optimal channel code in separate system is not optimal in joint system. In this letter, a novel joint protograph extrinsic information transfer analysis is proposed for the DP-LDPC system over AWGN and redesigning scheme for channel code is put forward to enhance the performance of DP-LPDC system. Both the EXIT analysis and the simulated results show the performance improvement of proposed systems. This verifies the viewpoint that the channel code should be redesigned for JSCC scheme even if the optimal channel codes are selected over AWGN in separate systems.

## Coding Aspects of Secure GNSS Receivers

- **Status**: ❌
- **Reason**: GNSS 수신기 코딩 개요/서베이성, soft-decoding 언급만이고 신규 LDPC 디코더·구성 없음
- **ID**: ieee:7442769
- **Type**: journal
- **Published**: June 2016
- **Authors**: James T. Curran, Monica Navarro, Marco Anghileri +2
- **PDF**: https://ieeexplore.ieee.org/document/7442769
- **Abstract**: This paper presents an overview of the coding aspects of a GNSS receiver. Coding allows detection and correction of channel-induced errors at the receiver, here the focus is on the mitigation of threats from malicious interferences. Although the effects of interference at different stages of GNSS baseband processing has been deeply analyzed in the literature, little attention was devoted to its impact on the navigation message decoding stage. Theis paper provides an introduction to the various coding schemes employed by current GNSS signals, discussing their performance in the presence of noise in terms of block-error rate. Additionally, the benefits of soft-decoding schemes for navigation message decoding are highlighted when jamming interferences are present. The proposed scheme requires estimating the noise plus interference power, yielding to enhanced decoding performances under severe jamming conditions. Finally, cryptographic schemes as a means of providing anti-spoofing for geosecurity location-based services, and their potential vulnerability are discussed, with particular emphasis on the dependence on the dependence of the scheme on successful navigation message decoding.

## Required Bit Rates Analysis for a New Broadcasting Service Using HEVC/H.265

- **Status**: ❌
- **Reason**: HEVC/H.265 비디오 코딩 비트레이트 분석, ECC/LDPC 무관
- **ID**: ieee:7454711
- **Type**: journal
- **Published**: June 2016
- **Authors**: Atsuro Ichigaya, Yukihiro Nishida
- **PDF**: https://ieeexplore.ieee.org/document/7454711
- **Abstract**: A novel video coding standard called high efficiency video coding (HEVC)|ITU-T H.265 was released in 2013. HEVC has twice the compression capability of MPEG-4 AVC|ITU-T H.264, a feature that is expected to enhance new broadcasting services. Japanese broadcasters plan to start a new ultra high definition television service using HEVC. To identify the required bit rates for the new broadcasting service, we conducted a subjective evaluation test using the double stimulus impairment scale method in a laboratory environment. The evaluation test was conducted by experts namely the broadcasting engineers and video circuits/signal engineers. For discussing multiformat video quality, the test materials consisted of 1080/60/I, 1080/60/P, 2160/60/P, and 4320/60/P, all of which originate from 4320/60/P video sources, and encoded using the HEVC test model with the Main 10 profile and using bit rate control. We decided to use the Main 10 profile, after comparing the performances of the Main profile and Main 10 profile in the objective evaluation test. The source and encoded test sequences were displayed on monitors compliant with the source video formats. The test results indicate the following required bit rates for the respective video formats: 10-15 Mbit/s for 1080/60/I and 1080/60/P both, 30-40 Mbit/s for 2160/60/P, and 80-100 Mbit/s for 4320/60/P. It also confirmed the possibility to transmit such videos via the existing satellite channel bandwidth.

## A High Throughput List Decoder Architecture for Polar Codes

- **Status**: ❌
- **Reason**: polar 코드 전용 SCL 리스트 디코더 아키텍처로 부호 의존적, 바이너리 LDPC BP로 이식 불가
- **ID**: ieee:7337462
- **Type**: journal
- **Published**: June 2016
- **Authors**: Jun Lin, Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/7337462
- **Abstract**: While long polar codes can achieve the capacity of arbitrary binary-input discrete memoryless channels when decoded by a low complexity successive-cancellation (SC) algorithm, the error performance of the SC algorithm is inferior for polar codes with finite block lengths. The cyclic redundancy check (CRC)-aided SC list (SCL) decoding algorithm has better error performance than the SC algorithm. However, current CRC-aided SCL decoders still suffer from long decoding latency and limited throughput. In this paper, a reduced latency list decoding (RLLD) algorithm for polar codes is proposed. Our RLLD algorithm performs the list decoding on a binary tree, whose leaves correspond to the bits of a polar code. In existing SCL decoding algorithms, all the nodes in the tree are traversed, and all possibilities of the information bits are considered. Instead, our RLLD algorithm visits much fewer nodes in the tree and considers fewer possibilities of the information bits. When configured properly, our RLLD algorithm significantly reduces the decoding latency and, hence, improves throughput, while introducing little performance degradation. Based on our RLLD algorithm, we also propose a high throughput list decoder architecture, which is suitable for larger block lengths due to its scalable partial sum computation unit. Our decoder architecture has been implemented for different block lengths and list sizes using the TSMC 90-nm CMOS technology. The implementation results demonstrate that our decoders achieve significant latency reduction and area efficiency improvement compared with the other list polar decoders in the literature.

## Horizontal and Vertical Side Channel Analysis of a McEliece Cryptosystem

- **Status**: ❌
- **Reason**: McEliece 암호 FPGA 사이드채널 공격으로 보안 도메인, 떼어낼 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7360160
- **Type**: journal
- **Published**: June 2016
- **Authors**: Cong Chen, Thomas Eisenbarth, Ingo von Maurich +1
- **PDF**: https://ieeexplore.ieee.org/document/7360160
- **Abstract**: This paper presents horizontal and vertical side channel analysis techniques for an implementation of the McEliece cryptosystem. The target of this side-channel attack is a state-of-the-art field-programmable gate array (FPGA) implementation of the efficient quasi-cyclic moderate-density parity-check McEliece decryption operation, as presented at Design, Automation and Test in Europe (DATE) 2014. The presented cryptanalysis succeeds to recover the complete secret key after a few observed decryptions. It consists of a combination of a differential leakage analysis during the syndrome computation followed by an algebraic step that exploits the relation between the public key and the private key.

## Raptor-coded free-space optical communications experiment

- **Status**: ❌
- **Reason**: FSO용 Raptor(fountain) 코드 FPGA 구현; Raptor 행렬역변환 HW로 LDPC BP 디코더 아키텍처와 무관, 제외 대상 fountain
- **ID**: ieee:7494884
- **Type**: journal
- **Published**: June 2016
- **Authors**: Min Lu, Linyan Liu, Steve Hranilovic
- **PDF**: https://ieeexplore.ieee.org/document/7494884
- **Abstract**: While free-space optical (FSO) links have many inherent advantages, such as high data rates and license-free operation, they are sensitive to atmospheric conditions. A promising solution to improve the reliability of such communication links is to combine FSO and radio frequency (RF) channels using Raptor codes. This paper presents a first in-field demonstration of real-time Raptor-coded FSO communication over a 1.87 km urban link. This work serves as an important initial step toward field-programmable gate array (FPGA)-based implementation of Raptor-coded hybrid FSO/RF links. The hardware architecture of a Raptor 10 decoder based on a novel resource- and time-efficient matrix inversion algorithm is presented and implemented in an FPGA platform. The receiver is implemented in a pipelined architecture to maximize link utilization. The throughput of the Raptor-coded FSO link is measured both experimentally and numerically under real-life weather conditions for a continuous period of 8 h. Experimental results demonstrate that Raptor-coded FSO links are capable of tracking changes in the channel state to maximize link utilization.

## Diversity Integration in Hybrid-ARQ With Chase Combining Under Partial CSI

- **Status**: ❌
- **Reason**: polar code HARQ + SOCP 다이버시티 결합 수신기; 부호 비의존 BP 이식 기법 아님, 비-LDPC
- **ID**: ieee:7452354
- **Type**: journal
- **Published**: June 2016
- **Authors**: Kun Wang, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/7452354
- **Abstract**: We consider a receiver design for a Hybrid Automatic-Repeat-reQuest (HARQ) system protected by polar codes against transmission errors. This integrated detection-decoding receiver targets a packet link for which channel state information during HARQ retransmission is unavailable at the receiver. Under such channel uncertainties, we propose a second-order cone programming (SOCP) approach for diversity combining without resorting to decision-directed channel estimation prone to error propagation. We formulate an integrated SOCP receiver by jointly exploiting the constraints from diversity channel models, subspace separation, and forward error correction codes. Unlike traditional turbo receiver algorithms that require iterative exchange of soft information between detector and decoder, our proposed SOCP receiver solves as a single-integrated convex optimization problem. This formulation is also versatile and extendable to a plurality of practical scenarios. We further investigate the means for enhancing the receiver performance and the HARQ throughput. Numerical results demonstrate the substantial performance benefits of the proposed joint SOCP receiver.

## Efficient Demodulation of General APSK Constellations

- **Status**: ❌
- **Reason**: APSK 복조 LLR 계산(lookup table); 무선 변조 특이적, NAND LDPC에 떼어낼 디코더/코드설계 기법 없음
- **ID**: ieee:7462233
- **Type**: journal
- **Published**: June 2016
- **Authors**: Magnus Sandell, Filippo Tosato, Amr Ismail
- **PDF**: https://ieeexplore.ieee.org/document/7462233
- **Abstract**: In this letter, we introduce a novel method for demodulation of general amplitude- and phase-shift keying (APSK) constellations. By noting that the max-log log-likelihood ratio (LLR) is a piecewise linear function of the received signal, we devise a scheme to determine in which linear region that the received signal falls, obtain the linear parameters from a lookup table and compute the LLR. This method is general and works for any APSK (two-dimensional) constellation. By pruning the search tree, it also provides a mechanism for performance-complexity tradeoff and we show that its complexity is much lower than a previously published scheme (which only works for regular APSK constellations).

## LDPC performances in multi-carrier systems

- **Status**: ❌
- **Reason**: MC-CDMA OFDM 무선 시스템에서 표준 LDPC 부수 적용, 떼어낼 신규 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7528256
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Ioana Marcu, Carmen Voicu, Răzvan Crăciunescu +1
- **PDF**: https://ieeexplore.ieee.org/document/7528256
- **Abstract**: In wireless communication systems data recovery represents an important challenge at receiver's end. The performances of MC-CDMA systems can be improved by using OFDM technique. This paper illustrates the improvement brought in MC-CDMA OFDM systems when choosing the LDPC coding/decoding technique and the appropriate spreading sequences to separate the users. There have been tested the performances of the system in BER vs SNR terms when Walsh, Kasami and PN spreading sequences are used for the MC-CDMA OFDM system. The final goal is to obtain the best combination between LDPC technique and spreading codes in order for the performances to be increased.

## On the BER and spectral efficiency performances of coded QAM configurations that map non-coded bits

- **Status**: ❌
- **Reason**: convolutional coded QAM BER/SE 분석-비-LDPC, 이식 기법 없음
- **ID**: ieee:7528253
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Vasile Bota, Mihaly Varga
- **PDF**: https://ieeexplore.ieee.org/document/7528253
- **Abstract**: This paper evaluates the bit-error rate and spectral efficiency performance provided by the convolutional coded Quadrature Amplitude Modulation (QAM) configurations whose global rates are modified mainly by changing the numbers of code and non-coded bits mapped on a QAM symbol. The Bit Error Rate (BER) performance provided are compared to the ones of the convolutional coded modulations which map only code bits and have the same configuration rates, aiming to show that coded configurations mapping non-coded bits as well, ensure a target BER value at smaller values of the Signal/Noise Ratio (SNR) than the ones mapping only code bits The paper also presents an approximate method to compute the BER of the configurations mapping both code and non-coded bits, which is validated by computer simulations and is shown to provide good accuracy in the range of BER values of practical interest.

## Single Pixel Camera with Compressive Sensing by non-uniform sampling

- **Status**: ❌
- **Reason**: 압축센싱 single pixel camera-소스 코딩/이미징, 채널 ECC 아님
- **ID**: ieee:7528202
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Mihai-Alexandru Petrovici, Cristian Damian, Cristian Udrea +2
- **PDF**: https://ieeexplore.ieee.org/document/7528202
- **Abstract**: Compressive Sensing refers to the acquisition in compressed form of sparse signals. One of the CS applications is the Single Pixel Camera that rethinks the conventional imaging systems. The key part of the camera is a Spatial Light Modulator (SLM), which provides the mechanism for taking arbitrary measurements of the scene. The non-uniform sampling (NUS) scenario offers a simple procedure to select random samples from the scene, instead of taking random projections. This paper analyses the Single Pixel Camera performance using NUS in the case of two categories of samples: randomly distributed over the scene and selected from the contours vicinity. The NUS is compared, in terms of reconstructed images, with measurements obtained by projection on a random selection from the S-Transform basis. The results are given on simulated data and on real images obtained with the experimental model of a Single Pixel Camera. The comparison of reconstructed images in the three cases of measurements shows that, in terms of PSNR, the NUS with contour pixels is equivalent with the S-transform based measurement.

## Application specific optimization: Rethinking protocol layering and standards

- **Status**: ❌
- **Reason**: SDN/NFV 기반 응용특화 네트워크 프로토콜 최적화 논문, LDPC/ECC와 무관
- **ID**: ieee:7502430
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: John Peng, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/7502430
- **Abstract**: There is a confluence of recent trends involving data center technology, software defined networks (SDN), and network function virtualization (NFV) that may open a way for general purpose networks to support application specific optimization (ASO). While traditional communications protocol architecture mandates layering where the lowest layers are application agnostic, research in cross layer design attests to the inefficiencies inherent in the “dumb pipes” networking paradigm. This paper investigates the potential of significant performance gains possible over the access network by departing from the traditional layered protocol approach and using a software defined protocol in conjunction with subscriber and application partitioning to provide ASO over the access network, while still maintaining a TCP/IP protocol stack to provide connectivity to the rest of the Internet. As a case study, we examine the potential performance gains provided by ASO of video streaming over the ADSL access network.

## An iterative decoding scheme of concatenated LDPC and BCH codes for optical transport network

- **Status**: ❌
- **Reason**: LDPC+BCH 연접 반복 디코딩(광 OTN). BCH 연접 구조 의존, 바이너리 LDPC BP로 이식할 신규 디코더 기법 불명확.
- **ID**: ieee:7788004
- **Type**: conference
- **Published**: 5-10 June 
- **Authors**: Wei Zhou, Shaoliang Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7788004
- **Abstract**: An iterative decoding scheme of concatenated LDPC codes is proposed for optical networks. Simulation results show that a coding gain can be improved by 0.8dB compared to the conventional LDPC concatenated codes at a post-FEC BER=10−6.

## A new decryption algorithm of the quasi-cyclic low-density parity-check codes based McEliece cryptosystem

- **Status**: ❌
- **Reason**: QC-LDPC McEliece 암호계 복호 알고리즘, 보안 도메인으로 채널 ECC 디코더 아님
- **ID**: ieee:7586588
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Shuo Zhang, Wenhui Cao, Angyang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7586588
- **Abstract**: The McEliece public-key cryptosystem is believed to resist quantum attacks, but has not been used because of the extremely large public key size. In order to decrease the public key size, quasi-cyclic low-density parity-check (QC-LDPC) codes were used instead of Goppa codes in McEliece cryptosystem. A modified version of QC-LDPC McEliece is quasi-cyclic moderate density parity-check (QC-MDPC) McEliece, which focuses on ensuring fixed security level other than error-correction capability. The QC-MDPC McEliece scheme furtherly reduces the public key size at the cost of higher decryption complexity. However, the decryption algorithm of QC-LDPC McEliece variant has not been optimized. In this paper, we proposed a new decryption algorithm of the QC-LDPC McEliece variant. With the decryption algorithm we proposed, the key size reduces about 20% than the original algorithm, even 8% smaller than QC-MDPC variant.

## A nonbinary LDPC product network coding scheme with signal space diversity

- **Status**: ❌
- **Reason**: 비이진 LDPC product 네트워크부호화, 비이진 제외
- **ID**: ieee:7586693
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Chengxin Jiang, Zhanji Wu
- **PDF**: https://ieeexplore.ieee.org/document/7586693
- **Abstract**: A network coding scheme employing nonbinary low density parity check (LDPC) product code with signal space diversity (SSD) is proposed in this paper. The scheme is based on a multiple access relay channel with two users, one relay and one base station. Rotated modulation and component interleaving are introduced in this scheme to realize SSD so that it can enhance the bit error rate (BER) performance for the scheme. Simulation results indicate that the proposed scheme significantly outperforms the conventional binary scheme by 1.9dB in Rayleigh fading channel. Moreover, it also proves that the rotated modulation and component interleaving play an important role in improving the BER performance of the nonbinary LDPC product code.

## A soft-output error control method for wireless video transmission

- **Status**: ❌
- **Reason**: 무선 비디오(H.264) 소프트정보 오류제어, 응용특이적이며 떼어낼 LDPC 디코더/HW 없음
- **ID**: ieee:7586585
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Bo Zheng, Shaoshuai Gao
- **PDF**: https://ieeexplore.ieee.org/document/7586585
- **Abstract**: With the rapid development of wireless network and multimedia technology, the efficient transmission over unreliable channel is becoming more and more important. The error control technique for video coding and transmission has drawn considerable attention, tries to recover the data loss and bit errors due to congestion or physical channel fading. Currently, there are three kinds of error control schemes, namely, error resilient coding at the encoder, error concealment at the decoder and the retransmission in the transport layer. In this paper, an error control scheme is proposed which uses the soft information in channel decoding to recover the corrupted bit stream. When bit error is detected in a slice, soft information of channel decoding is employed to locate it, and the wrong bits are flipped and decoded again at the beginning of the slice. The combination of XOR at source and the syntax checking of H.264 decoder has increased the error detection rate from around 60% to 99% without increasing source redundancy. Simulation results show that, when the same error concealing algorithm is used, the PSNR of the proposed scheme using soft information of channel decoding at the decoder is 1-2dB higher than that using the traditional method.

## Low Density Parity Check (LDPC) coded MIMO-Constant Envelop Modulation System with IF sampled 1-bit ADC

- **Status**: ❌
- **Reason**: MIMO-CEM 무선 응용에 LDPC를 baseline으로 적용; 표준 LDPC 사용, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:7518954
- **Type**: conference
- **Published**: 31 May-2 J
- **Authors**: Ahmed S. Mubarak, Amr Amrallah, Hany S. Hussein +1
- **PDF**: https://ieeexplore.ieee.org/document/7518954
- **Abstract**: MIMO-Constant Envelop Modulation (CEM) is a very power and complexity efficient system, which is introduced as alternative candidate to the currently used MIMO-Orthogonal Frequency Division Multiplexing (OFDM). CEM system enables to use high efficient nonlinear power amplifier on the transmitter side and 1 bit (low resolution) analog to digital converter (ADC) on the receiver side. Due to adopting the low resolution at the receiver side a great reduction in hardware complexity and power consumption can be achieved. However, there will be a noticeable degradation on the performance of bit error rate (BER) on the receiver side due to sever quantization error introduced by the low resolution ADC, so a forward error correction coding is essential to enhance the BER. In this paper a LDPC coded MIMO-CEM system was used as a replacement for MIMO-OFDM to deal with the BER degradation problem of the CEM system. The performance of the LDPC coded MIMO-CEM with Gaussian Minimum Phase Shift Keying (GMSK) modulation is evaluated over a multi-path Rayleigh fading channel. It showed that LDPC codes are effective to improve the BER performance of CEM on Rayleigh fading channels. According to the simulation results, the MIMO-CEM system provides a significant improvement in BER performance and outperforms the un-coded and the original convolutional coder based CEM systems.

## Performance analysis of low density parity check codes implemented in second generations of digital video broadcasting standards

- **Status**: ❌
- **Reason**: DVB-T2/S2 표준 LDPC 성능분석/시뮬레이션 서베이 수준, 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:7522195
- **Type**: conference
- **Published**: 30 May-3 J
- **Authors**: Gr. Y. Mihaylov, T. B. Iliev, E. P. Ivanova +2
- **PDF**: https://ieeexplore.ieee.org/document/7522195
- **Abstract**: The newly developed second generations standards for digital video broadcasting (DVB-T2, DVB-S2) emerges as a significant upgrade over its first generation predecessor. Low-Density Parity-Check (LDPC) codes received a lot of attention by their superb error-correcting capability and have been adopted as main error correct coding scheme by second generation Digital Video Broadcasting standards. The goal of this paper is to present the main constructive principle of low-density parity check codes, as well as a design methodology, that gives good performance for many communication systems like latest DVB satellite communications standard. In this paper we analyze the structure of LDPC codes and the iterative algorithms that are used to decode them. An analysis and simulation of the LDPC codes has been conducted using various code rates. The simulation results show that LDPC codes are a powerful error correcting coding technique under SNR environments. It has achieved near Shannon capacity. However, there are many factors needed to be considered in the LDPC code design.

## On the error detection capability of combined LDPC and CRC codes for space telecommand transmissions

- **Status**: ❌
- **Reason**: LDPC+CRC 결합 미검출오류율 추정으로 ECC 디코더/HW/구성 신규 기여 없는 검출 분석, 떼어낼 기법 없음
- **ID**: ieee:7543876
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Marco Baldi, Nicola Maturo, Giacomo Ricciutelli +1
- **PDF**: https://ieeexplore.ieee.org/document/7543876
- **Abstract**: We present a method for estimating the undetected error rate when a cyclic redundancy check (CRC) is performed on the output of the decoder of short low-density parity-check (LDPC) codes. This system is of interest for telecommand links, where new LDPC codes have been designed for updating the current standard. We show that these new LDPC codes combined with CRC are adequate for complying with the stringent requirements of this kind of transmissions in terms of error detection.

## Link adaptation in FBMC/OQAM systems using NB-LDPC codes

- **Status**: ❌
- **Reason**: NB-LDPC(비이진) 적용 + FBMC/OQAM 무선 응용 ACM 최적화, 비이진 제외
- **ID**: ieee:7560995
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Màrius Caus, Monica Navarro, Xavier Mestre +1
- **PDF**: https://ieeexplore.ieee.org/document/7560995
- **Abstract**: This paper investigates the application of non-binary low density parity check (NB-LDPC) codes to offset-QAM based filter bank multicarrier systems, known as FBMC/OQAM. The analysis conducted in the paper reveals that the mapping scheme can be optimized to simplify detection and minimize the correlation of the noise. Based on the proposed modifications, existing adaptive coding and modulation (ACM) algorithms can be easily tailored to accommodate the characteristics of NB-LDPC and FBMC/OQAM. In this paper, priority has been given to mutual information-based ACM algorithms. Numerical results verify that the proposed algorithm guarantees the target block error rate.

## Study of indoor LTE green small-cells using mobile fronthaul architecture over hybrid fiber-wireless channels

- **Status**: ❌
- **Reason**: indoor LTE fronthaul 광-무선 전송 데모, LDPC 무관
- **ID**: ieee:7561029
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Y. Hazan, M. Ran
- **PDF**: https://ieeexplore.ieee.org/document/7561029
- **Abstract**: 6Gbps transmission over low power indoor LTE air-interface is demonstrated by using single-mode fiber based fronthaul architecture combined with plastic optical fiber indoor small-cells. The low power transmission coverage is similar to the classic femtocell coverage and is suitable for most indoor scenarios.

## Reduced-complexity decoding algorithms of Raptor codes

- **Status**: ❌
- **Reason**: Raptor(fountain) 코드 BP 근사 복호 적용, LDPC BP 기법을 Raptor에 이식하는 방향이라 NAND LDPC에 떼어낼 신규 기여 없음
- **ID**: ieee:7760847
- **Type**: conference
- **Published**: 27-29 June
- **Authors**: Cenk Albayrak, Kadir Turk
- **PDF**: https://ieeexplore.ieee.org/document/7760847
- **Abstract**: In this paper, the belief propagation (BP) based approximation methods which are introduced for low density parity check (LDPC) codes in literature are adapted to the Raptor decoder structure in order to reduce its computational complexity. The bit error rate (BER) performances of the algorithms over the additive white Gaussian noise (AWGN) channel are obtained by both theoretical works and simulations. The Monte-Carlo based density evolution (MC-DE) method is used for theoretical analysis. In addition to this, computational complexity analyses of the considered methods are presented. Results show that the computational complexity can be significantly decreased with a limited performance loss cost.

## Improved iterative convergence method in Q-ary LDPC coded high order PR-CPM

- **Status**: ❌
- **Reason**: Q-ary(비이진) LDPC coded CPM EXIT 설계 — 비이진 LDPC 제외
- **ID**: ieee:7514680
- **Type**: journal
- **Published**: 22 June 20
- **Authors**: Danfeng Zhao, Yanbo Sun, Rui Xue
- **PDF**: https://ieeexplore.ieee.org/document/7514680
- **Abstract**: The Q-ary low-density parity-check (LDPC) coded high order partial response continuous phase modulation (PR-CPM) with double iterative loops is investigated. This scheme shows significant improvements in power and bandwidth efficiency, but at the expense of long iterative decoding delay and computational complexity induced by the improper match between the demodulator and the decoder. To address this issue, the convergence behavior of Q-ary LDPC coded CPM is investigated for the Q=2 and Q>2 cases, and an optimized design method based on the extrinsic information transfer chart is proposed to improve the systematic iterative efficiency. Simulation results demonstrate that the proposed method can achieve a perfect tradeoff between iterative decoding delay and bit error rate performance to satisfy real-time applications.

## A cycle-based rate-compatible puncturing technique for non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 펑처링 기법 — 바이너리 한정 제외
- **ID**: ieee:7746650
- **Type**: conference
- **Published**: 12-15 June
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/7746650
- **Abstract**: This paper presents a cycle-based rate-compatible puncturing technique for non-binary (NB) low-density parity-check (LDPC) codes. The proposed puncturing technique is based on the connectivity of the short non-binary (NB) cycles present in the Tanner graph. The connectivity of a cycle is measured by the extrinsic message degree (EMD). The short cycles with low values of EMD degrade the performance of iterative decoders significantly. The proposed technique selects the variable nodes for puncturing by reckoning their involvements in the short NB cycles with a low EMD. Simulations in different contexts are performed to check the efficiency of the proposed technique.

## Implementation of ISDB-T LDM broadcast system using LDPC codes

- **Status**: ❌
- **Reason**: ISDB-T LDM 방송에 표준 LDPC 통합 사례로 신규 디코더/코드/HW 기여 없음
- **ID**: ieee:7521986
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: George Henrique Maranhão Garcia de Oliveira, Cristiano Akamine, Yuri Pontes Maciel
- **PDF**: https://ieeexplore.ieee.org/document/7521986
- **Abstract**: This paper presents the scenario of terrestrial broadcast services, the challenges and needed adaptations for the next generation television. It shows promising technologies such as LDM, LDPC, NUC and their advantages in terms of increase of transmission rate, robustness and efficient use of spectrum. It also proposes an adapted ISDB-T system that uses LDM, LDPC, NUC and SDR technologies to increase performance and useful bit rate to DTV applications, while using a layer that would still be compatible with traditional ISDB-T system.

## Performance measurement of high-efficient OFDM based transmission system in commercial HFC network

- **Status**: ❌
- **Reason**: OFDM HFC 필드테스트에 표준 9/10 LDPC 사용, 떼어낼 신규 기법 없음
- **ID**: ieee:7522004
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Sang-Jung Ra, JinHyuk Song, JaeHwui Bae +4
- **PDF**: https://ieeexplore.ieee.org/document/7522004
- **Abstract**: This paper describes the results of a field test of an OFDM-based transmission system that uses digital video broadcasting for a cable system and is implemented using field programmable gate arrays (FPGAs). For the field test, a 4096QAM, 4096 Fast Fourier Transform (FFT), 9/10 code rate of a low-density parity check (LDPC), and 6-MHz channel bandwidth were selected. To evaluate the practical performance of the implemented transmission system, a commercial MPEG Analyzer is used for the performance evaluation.

## Pilot optimization for mobile services in ATSC 3.0

- **Status**: ❌
- **Reason**: ATSC 3.0 파일럿 패턴 최적화; LDPC 언급 없고 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7522005
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Eduardo Garro, Jordi Joan Gimenez, David Gomez-Barquero +1
- **PDF**: https://ieeexplore.ieee.org/document/7522005
- **Abstract**: The Advanced Television System Committee (ATSC) has released ATSC 3.0, the next-generation U.S. Digital Terrestrial Television (DTT) standard. ATSC 3.0 allows a higher flexibility compared to the previous state-of-the-art DTT standard, DVB-T2 (Digital Video Broadcasting - Terrestrial 2nd Generation). This higher flexibility allows broadcasters to adapt transmission configuration to network and reception requirements. Regarding pilot patterns (PP), whereas DVB-T2 provides 8 different PPs with a unique pilot boosting, ATSC 3.0 extends up to 16 different PPs, with 5 different boostings per each one. This paper is focused on the study of the PP and boosting combination that optimizes performance for time (Time Division Multiplexing, TDM) and power (Layered Division Multiplexing, LDM) multiplexing modes of ATSC 3.0 in mobility reception conditions. The selection of the optimum PP is particularly essential in LDM mode, because it must be shared between the two LDM layers.

## Field trial of a redundancy on demand DVB-T2 system

- **Status**: ❌
- **Reason**: DVB-T2 redundancy on demand 필드트라이얼, 응용특이적이며 이식 LDPC 기법 없음
- **ID**: ieee:7521909
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Fabian Schrieber, Jan Zoellner, Lothar Stadelmeier +3
- **PDF**: https://ieeexplore.ieee.org/document/7521909
- **Abstract**: Different digital terrestrial television (DTT) systems are in use around the world today. A rapidly growing number of TV sets used for terrestrial broadcast reception is also equipped with broadband connectivity. However, the distribution of TV content relies either solely on terrestrial broadcast or on broadband delivery. Redundancy on Demand (RoD) on the other hand utilizes the broadband connectivity to enhance terrestrial broadcast reception. RoD is a fully backward compatible extension to terrestrial broadcast systems. It provides supporting data, i.e. additional redundancy, on demand to broadcast receivers via a broadband connection. Receivers even in unfavorable reception conditions are then able to successfully decode the broadcast signal. The supporting data is provided by an RoD server extending the broadcast network. An RoD DTT receiver is able to estimate the signal quality, request and receive the redundancy data if required and decode the broadcast signal with the help of the broadband data. As the second generation terrestrial Digital Video Broadcasting (DVB-T2) will be introduced in Germany starting in 2016, a DVB-T2 trial network was set up in Berlin. This network gave the opportunity to evaluate the performance of RoD with DVB-T2 in a real world environment. This paper presents results of the field trial.
