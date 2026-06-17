# IEEE Xplore — 2016-06


## Construction of Multiple-Rate QC-LDPC Codes Using Hierarchical Row-Splitting

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7452367
- **Type**: journal
- **Published**: June 2016
- **Authors**: Peiyao Zhao, Zhaocheng Wang, Qi Wang
- **PDF**: https://ieeexplore.ieee.org/document/7452367
- **Abstract**: In this letter, we propose an improved method called hierarchical row-splitting with edge variation for designing multiple-rate quasi-cyclic low-density parity-check (QC-LDPC) codes, which constructs lower-rate codes from a high-rate mother code by row-splitting operations. Consequently, the obtained QC-LDPC codes with various code rates have the same blocklength and can share common hardware resources to reduce the implementation complexity. Compared with the conventional row-combining-based algorithms, a wider range of code rates are supported. Moreover, each individual rate code could be separately optimized, making it easier to find a set of multiple-rate QC-LDPC codes with good performance for all different rates. Simulation results demonstrate that the obtained codes outperform the counterparts from digital video broadcasting-second generation terrestrial.

## New Classes of Partial Geometries and Their Associated LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7355344
- **Type**: journal
- **Published**: June 2016
- **Authors**: Qiuju Diao, Juane Li, Shu Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/7355344
- **Abstract**: The use of partial geometries to construct parity-check matrices for binary low-density parity-check (LDPC) codes has resulted in the design of successful codes with a probability of error on the AWGN channel close to the Shannon capacity at bit error rate down to $10^{-15}$ . Such considerations have motivated this further investigation. A new and simple construction of a type of partial geometries with a quasi-cyclic (QC) structure is given and their properties are investigated. Two new classes of this type of partial geometries, one based on prime fields and the other based on cyclic subgroups of prime orders of finite fields, are constructed. QC-LDPC codes with good error performances are constructed based on these two new classes of partial geometries. The trapping sets of the partial geometry codes were previously considered using the geometric aspects of the underlying structure to derive information on the size of allowable trapping sets. This topic is further considered here. Finally, there is a natural relationship between partial geometries and strongly regular graphs. The eigenvalues of the adjacency matrices of such graphs are well known, and it is of interest to determine if any of the Tanner graphs derived from the partial geometries are good expanders for certain parameter sets, since it can be argued that codes with good geometric and expansion properties might perform well on the AWGN channel under message-passing decoding.

## The ADMM Penalized Decoder for LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7456284
- **Type**: journal
- **Published**: June 2016
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7456284
- **Abstract**: Linear programming (LP) decoding for low-density parity-check codes was introduced by Feldman et al. and has been shown to have theoretical guarantees in several regimes. Furthermore, it has been reported in the literature-via simulation and via instanton analysis-that LP decoding displays better error rate performance at high signal-to-noise ratios (SNR) than does belief propagation (BP) decoding. However, at low SNRs, LP decoding is observed to have worse performance than BP. In this paper, we seek to improve LP decoding at low SNRs while maintaining LP decoding's high SNR performance. Our main contribution is a new class of decoders obtained by applying the alternating direction method of multipliers (ADMM) algorithm to a set of non-convex optimization problems. These non-convex problems are constructed by adding a penalty term to the objective of LP decoding. The goal of the penalty is to make pseudocodewords, which are non-integer vertices of the LP relaxation, more costly. We name this class of decoders-ADMM penalized decoders. For low and moderate SNRs, we simulate ADMM penalized decoding with ℓ1 and ℓ2 penalties. We find that these decoders can outperform both BP and LP decoding. For high SNRs, where it is difficult to obtain data via simulation, we use an instanton analysis and find that, asymptotically, ADMM penalized decoding performs better than BP but not as well as LP. Unfortunately, since ADMM penalized decoding is not a convex program, we have not been successful in developing theoretical guarantees. However, the non-convex program can be approximated using a sequence of linear programs; an approach that yields a reweighted LP decoder. We show that a two-round reweighted LP decoder has an improved theoretical recovery threshold when compared with LP decoding. In addition, we find via simulation that reweighted LP decoding significantly attains lower error rates than LP decoding at low SNRs.

## On Code Design for Joint Energy and Information Transfer

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7462244
- **Type**: journal
- **Published**: June 2016
- **Authors**: Mehdi Dabirnia, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/7462244
- **Abstract**: Harvesting energy from radio frequency signals along with transmitting data through them is appealing for different wireless communication scenarios, such as radio frequency identification (RFID) systems and implantable devices. In this paper, we propose a technique to design nonlinear codes for the use in such systems taking into account both energy transmission and error rate requirements. In particular, we propose using concatenation of a nonlinear trellis code (NLTC) with an outer low-density parity-check (LDPC) code. We design the NLTC based on maximization of its free distance. We give necessary and sufficient conditions for its catastrophicity; in order to avoid catastrophic codes, we connect each designed NLTC to a corresponding linear convolutional code allowing for the use of simpler conditions for verification. Furthermore, we use EXIT charts to design the outer LDPC code while fixing the inner NLTC. Via examples, we demonstrate that our designed codes operate at ~0.8 dB away from the information theoretic limits, and they outperform both regular LDPC codes and optimized irregular LDPC codes for additive white Gaussian noise (AWGN) channels. In addition, we show that the proposed scheme outperforms the reference schemes of concatenating LDPC codes with nonlinear memoryless mappers and using classical linear block codes in a time switching mode.

## BASIC Codes: Low-Complexity Regenerating Codes for Distributed Storage Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7452376
- **Type**: journal
- **Published**: June 2016
- **Authors**: Hanxu Hou, Kenneth W. Shum, Minghua Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/7452376
- **Abstract**: In distributed storage systems, regenerating codes can achieve the optimal tradeoff between storage capacity and repair bandwidth. However, a critical drawback of existing regenerating codes, in general, is the high coding and repair complexity, since the coding and repair processes involve expensive multiplication operations in finite field. In this paper, we present a design framework of regenerating codes, which employ binary addition and bitwise cyclic shift as the elemental operations, named BASIC regenerating codes. The proposed BASIC regenerating codes can be regarded as a concatenated code with the outer code being a binary parity-check code, and the inner code being a regenerating code utilizing the binary parity-check code as the alphabet. We show that the proposed functional-repair BASIC regenerating codes can achieve the fundamental tradeoff curve between the storage and repair bandwidth asymptotically of functional-repair regenerating codes with less computational complexity. Furthermore, we demonstrate that the existing exact-repair product-matrix construction of regenerating codes can be modified to exact-repair BASIC product-matrix regenerating codes with much less encoding, repair, and decoding complexity from the theoretical analysis, and with less encoding time, repair time, and decoding time from the implementation results.

## Constructions of Optimal Binary Locally Repairable Codes With Multiple Repair Groups

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7426763
- **Type**: journal
- **Published**: June 2016
- **Authors**: Jie Hao, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/7426763
- **Abstract**: In distributed storage systems, locally repairable codes (LRCs) have attracted lots of interest recently. If a code symbol can be repaired respectively by t disjoint groups of other symbols, each of which has size at most r, we say that the code symbol has (r, t)-locality. LDPC codes are linear block codes defined by low-density parity-check matrices. A regular (τ, p)-LDPC code has the parity-check matrix with uniform column weight τ and uniform row weight p. In this letter, we employ regular LDPC codes to construct optimal binary LRCs with (r, t)-locality for information symbols. After proposing construction frameworks, three detailed constructions of binary LRCs with information locality are obtained, all of which have a single parity symbol in each repair group. All our codes attain the distance bounds of LRCs when each repair group contains a single parity symbol and thus are optimal. For storage systems with hot data, the proposed binary LRCs seem promising for system implementations since the encoding, repairing, parallel reading, and data reconstruction can be performed by simple XOR operations.

## Tag Memory-Erasure Tradeoff of RFID Grouping Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7440837
- **Type**: journal
- **Published**: June 2016
- **Authors**: Mike Burmester, Jorge Munilla
- **PDF**: https://ieeexplore.ieee.org/document/7440837
- **Abstract**: We analyze the memory-erasure tradeoff of recently proposed radio frequency identification (RFID) grouping codes. Grouping codes make it possible for an RFID reader to automatically verify the integrity of a collection of RFID tagged objects and identify any missing objects without having access to external sources. They add redundancy to the memory of tags that is then used to recover missing tag identification data (forward error correction). We present a lower bound for the redundancy and show that it can be realized asymptotically. We then consider optimized approximations for practical settings and show that their memory-erasure tradeoff is close to optimal and significantly less than that of recently proposed grouping codes.

## Optimizing Transmission Lengths for Limited Feedback With Nonbinary LDPC Examples

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7426758
- **Type**: journal
- **Published**: June 2016
- **Authors**: Kasra Vakilinia, Sudarsan V. S. Ranganathan, Dariush Divsalar +1
- **PDF**: https://ieeexplore.ieee.org/document/7426758
- **Abstract**: This paper presents a general approach for optimizing the number of symbols in increments (packets of incremental redundancy) in a feedback communication system with a limited number of increments. This approach is based on a tight normal approximation on the rate for successful decoding. Applying this approach to a variety of feedback systems using nonbinary (NB) low-density parity-check (LDPC) codes shows that greater than 90% of capacity can be achieved with average blocklengths fewer than 500 transmitted bits. One result is that the performance with ten increments closely approaches the performance with an infinite number of increments. The paper focuses on binary-input additive-white Gaussian noise (BI-AWGN) channels but also demonstrates that the normal approximation works well on examples of fading channels as well as high-SNR AWGN channels that require larger QAM constellations. This paper explores both variable-length feedback codes with termination (VLFT) and the more practical variable length feedback (VLF) codes without termination that require no assumption of noiseless transmitter confirmation. For VLF, we consider both a two-phase scheme and CRC-based scheme.

## ADMM LP Decoding of Non-Binary LDPC Codes in  $ \mathbb {F}_{2^{m}}$

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7453187
- **Type**: journal
- **Published**: June 2016
- **Authors**: Xishuo Liu, Stark C. Draper
- **PDF**: https://ieeexplore.ieee.org/document/7453187
- **Abstract**: In this paper, we develop efficient decoders for non-binary low-density parity-check codes using the alternating direction method of multipliers (ADMM). We apply ADMM to two decoding problems. The first problem is linear programming (LP) decoding. In order to develop an efficient algorithm, we focus on non-binary codes in fields of characteristic two. This allows us to transform each constraint in  $ \mathbb {F}_{2^{m}}$  to a set of constraints in  $ \mathbb {F}_{2}$  that has a factor graph representation. Applying ADMM to the LP decoding problem results in two types of non-trivial sub-routines. The first type requires us to solve an unconstrained quadratic program. We solve this problem efficiently by leveraging new results obtained from studying the above factor graphs. The second type requires Euclidean projections onto polytopes that are studied in the literature. Such projections can be solved efficiently using off-the-shelf techniques, which scale linearly in the dimension of the vector to project. ADMM LP decoding scales linearly with block length, linearly with check degree, and quadratically with field size. The second problem we consider is a penalized LP decoding problem. This problem is obtained by incorporating a penalty term into the LP decoding objective. The purpose of the penalty term is to make non-integer solutions (pseudocodewords) more expensive and hence to improve decoding performance. The ADMM algorithm for the penalized LP problem requires Euclidean projection onto a polytope formed by embedding the constraints specified by the non-binary single parity-check code, which can be solved by applying the ADMM technique to the resulting quadratic program. Empirically, this decoder achieves a much reduced error rate than LP decoding at low signal-to-noise ratios.

## Bounds on the Parameters of Locally Recoverable Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7384487
- **Type**: journal
- **Published**: June 2016
- **Authors**: Itzhak Tamo, Alexander Barg, Alexey Frolov
- **PDF**: https://ieeexplore.ieee.org/document/7384487
- **Abstract**: A locally recoverable code (LRC code) is a code over a finite alphabet, such that every symbol in the encoding is a function of a small number of other symbols that form a recovering set. In this paper, we derive new finite-length and asymptotic bounds on the parameters of LRC codes. For LRC codes with a single recovering set for every coordinate, we derive an asymptotic Gilbert-Varshamov type bound for LRC codes and find the maximum attainable relative distance of asymptotically good LRC codes. Similar results are established for LRC codes with two disjoint recovering sets for every coordinate. For the case of multiple recovering sets (the availability problem), we derive a lower bound on the parameters using expander graph arguments. Finally, we also derive finite-length upper bounds on the rate and the distance of LRC codes with multiple recovering sets.

## Performance Improvement of JSCC Scheme Through Redesigning Channel Code

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7452543
- **Type**: journal
- **Published**: June 2016
- **Authors**: Qiwang Chen, Lin Wang, Shaohua Hong +1
- **PDF**: https://ieeexplore.ieee.org/document/7452543
- **Abstract**: For joint source channel coding (JSCC) scheme based on double protograph low-density parity-check (DP-LDPC) codes, due to joint iterative decoding between the source and channel decoders, it is found that the optimal channel code in separate system is not optimal in joint system. In this letter, a novel joint protograph extrinsic information transfer analysis is proposed for the DP-LDPC system over AWGN and redesigning scheme for channel code is put forward to enhance the performance of DP-LPDC system. Both the EXIT analysis and the simulated results show the performance improvement of proposed systems. This verifies the viewpoint that the channel code should be redesigned for JSCC scheme even if the optimal channel codes are selected over AWGN in separate systems.

## Coding Aspects of Secure GNSS Receivers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7442769
- **Type**: journal
- **Published**: June 2016
- **Authors**: James T. Curran, Monica Navarro, Marco Anghileri +2
- **PDF**: https://ieeexplore.ieee.org/document/7442769
- **Abstract**: This paper presents an overview of the coding aspects of a GNSS receiver. Coding allows detection and correction of channel-induced errors at the receiver, here the focus is on the mitigation of threats from malicious interferences. Although the effects of interference at different stages of GNSS baseband processing has been deeply analyzed in the literature, little attention was devoted to its impact on the navigation message decoding stage. Theis paper provides an introduction to the various coding schemes employed by current GNSS signals, discussing their performance in the presence of noise in terms of block-error rate. Additionally, the benefits of soft-decoding schemes for navigation message decoding are highlighted when jamming interferences are present. The proposed scheme requires estimating the noise plus interference power, yielding to enhanced decoding performances under severe jamming conditions. Finally, cryptographic schemes as a means of providing anti-spoofing for geosecurity location-based services, and their potential vulnerability are discussed, with particular emphasis on the dependence on the dependence of the scheme on successful navigation message decoding.

## Required Bit Rates Analysis for a New Broadcasting Service Using HEVC/H.265

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7454711
- **Type**: journal
- **Published**: June 2016
- **Authors**: Atsuro Ichigaya, Yukihiro Nishida
- **PDF**: https://ieeexplore.ieee.org/document/7454711
- **Abstract**: A novel video coding standard called high efficiency video coding (HEVC)|ITU-T H.265 was released in 2013. HEVC has twice the compression capability of MPEG-4 AVC|ITU-T H.264, a feature that is expected to enhance new broadcasting services. Japanese broadcasters plan to start a new ultra high definition television service using HEVC. To identify the required bit rates for the new broadcasting service, we conducted a subjective evaluation test using the double stimulus impairment scale method in a laboratory environment. The evaluation test was conducted by experts namely the broadcasting engineers and video circuits/signal engineers. For discussing multiformat video quality, the test materials consisted of 1080/60/I, 1080/60/P, 2160/60/P, and 4320/60/P, all of which originate from 4320/60/P video sources, and encoded using the HEVC test model with the Main 10 profile and using bit rate control. We decided to use the Main 10 profile, after comparing the performances of the Main profile and Main 10 profile in the objective evaluation test. The source and encoded test sequences were displayed on monitors compliant with the source video formats. The test results indicate the following required bit rates for the respective video formats: 10-15 Mbit/s for 1080/60/I and 1080/60/P both, 30-40 Mbit/s for 2160/60/P, and 80-100 Mbit/s for 4320/60/P. It also confirmed the possibility to transmit such videos via the existing satellite channel bandwidth.

## A High Throughput List Decoder Architecture for Polar Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7337462
- **Type**: journal
- **Published**: June 2016
- **Authors**: Jun Lin, Chenrong Xiong, Zhiyuan Yan
- **PDF**: https://ieeexplore.ieee.org/document/7337462
- **Abstract**: While long polar codes can achieve the capacity of arbitrary binary-input discrete memoryless channels when decoded by a low complexity successive-cancellation (SC) algorithm, the error performance of the SC algorithm is inferior for polar codes with finite block lengths. The cyclic redundancy check (CRC)-aided SC list (SCL) decoding algorithm has better error performance than the SC algorithm. However, current CRC-aided SCL decoders still suffer from long decoding latency and limited throughput. In this paper, a reduced latency list decoding (RLLD) algorithm for polar codes is proposed. Our RLLD algorithm performs the list decoding on a binary tree, whose leaves correspond to the bits of a polar code. In existing SCL decoding algorithms, all the nodes in the tree are traversed, and all possibilities of the information bits are considered. Instead, our RLLD algorithm visits much fewer nodes in the tree and considers fewer possibilities of the information bits. When configured properly, our RLLD algorithm significantly reduces the decoding latency and, hence, improves throughput, while introducing little performance degradation. Based on our RLLD algorithm, we also propose a high throughput list decoder architecture, which is suitable for larger block lengths due to its scalable partial sum computation unit. Our decoder architecture has been implemented for different block lengths and list sizes using the TSMC 90-nm CMOS technology. The implementation results demonstrate that our decoders achieve significant latency reduction and area efficiency improvement compared with the other list polar decoders in the literature.

## Horizontal and Vertical Side Channel Analysis of a McEliece Cryptosystem

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7360160
- **Type**: journal
- **Published**: June 2016
- **Authors**: Cong Chen, Thomas Eisenbarth, Ingo von Maurich +1
- **PDF**: https://ieeexplore.ieee.org/document/7360160
- **Abstract**: This paper presents horizontal and vertical side channel analysis techniques for an implementation of the McEliece cryptosystem. The target of this side-channel attack is a state-of-the-art field-programmable gate array (FPGA) implementation of the efficient quasi-cyclic moderate-density parity-check McEliece decryption operation, as presented at Design, Automation and Test in Europe (DATE) 2014. The presented cryptanalysis succeeds to recover the complete secret key after a few observed decryptions. It consists of a combination of a differential leakage analysis during the syndrome computation followed by an algebraic step that exploits the relation between the public key and the private key.

## Raptor-coded free-space optical communications experiment

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7494884
- **Type**: journal
- **Published**: June 2016
- **Authors**: Min Lu, Linyan Liu, Steve Hranilovic
- **PDF**: https://ieeexplore.ieee.org/document/7494884
- **Abstract**: While free-space optical (FSO) links have many inherent advantages, such as high data rates and license-free operation, they are sensitive to atmospheric conditions. A promising solution to improve the reliability of such communication links is to combine FSO and radio frequency (RF) channels using Raptor codes. This paper presents a first in-field demonstration of real-time Raptor-coded FSO communication over a 1.87 km urban link. This work serves as an important initial step toward field-programmable gate array (FPGA)-based implementation of Raptor-coded hybrid FSO/RF links. The hardware architecture of a Raptor 10 decoder based on a novel resource- and time-efficient matrix inversion algorithm is presented and implemented in an FPGA platform. The receiver is implemented in a pipelined architecture to maximize link utilization. The throughput of the Raptor-coded FSO link is measured both experimentally and numerically under real-life weather conditions for a continuous period of 8 h. Experimental results demonstrate that Raptor-coded FSO links are capable of tracking changes in the channel state to maximize link utilization.

## Diversity Integration in Hybrid-ARQ With Chase Combining Under Partial CSI

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7452354
- **Type**: journal
- **Published**: June 2016
- **Authors**: Kun Wang, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/7452354
- **Abstract**: We consider a receiver design for a Hybrid Automatic-Repeat-reQuest (HARQ) system protected by polar codes against transmission errors. This integrated detection-decoding receiver targets a packet link for which channel state information during HARQ retransmission is unavailable at the receiver. Under such channel uncertainties, we propose a second-order cone programming (SOCP) approach for diversity combining without resorting to decision-directed channel estimation prone to error propagation. We formulate an integrated SOCP receiver by jointly exploiting the constraints from diversity channel models, subspace separation, and forward error correction codes. Unlike traditional turbo receiver algorithms that require iterative exchange of soft information between detector and decoder, our proposed SOCP receiver solves as a single-integrated convex optimization problem. This formulation is also versatile and extendable to a plurality of practical scenarios. We further investigate the means for enhancing the receiver performance and the HARQ throughput. Numerical results demonstrate the substantial performance benefits of the proposed joint SOCP receiver.

## Efficient Demodulation of General APSK Constellations

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7462233
- **Type**: journal
- **Published**: June 2016
- **Authors**: Magnus Sandell, Filippo Tosato, Amr Ismail
- **PDF**: https://ieeexplore.ieee.org/document/7462233
- **Abstract**: In this letter, we introduce a novel method for demodulation of general amplitude- and phase-shift keying (APSK) constellations. By noting that the max-log log-likelihood ratio (LLR) is a piecewise linear function of the received signal, we devise a scheme to determine in which linear region that the received signal falls, obtain the linear parameters from a lookup table and compute the LLR. This method is general and works for any APSK (two-dimensional) constellation. By pruning the search tree, it also provides a mechanism for performance-complexity tradeoff and we show that its complexity is much lower than a previously published scheme (which only works for regular APSK constellations).

## LDPC performances in multi-carrier systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7528256
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Ioana Marcu, Carmen Voicu, Răzvan Crăciunescu +1
- **PDF**: https://ieeexplore.ieee.org/document/7528256
- **Abstract**: In wireless communication systems data recovery represents an important challenge at receiver's end. The performances of MC-CDMA systems can be improved by using OFDM technique. This paper illustrates the improvement brought in MC-CDMA OFDM systems when choosing the LDPC coding/decoding technique and the appropriate spreading sequences to separate the users. There have been tested the performances of the system in BER vs SNR terms when Walsh, Kasami and PN spreading sequences are used for the MC-CDMA OFDM system. The final goal is to obtain the best combination between LDPC technique and spreading codes in order for the performances to be increased.

## On the BER and spectral efficiency performances of coded QAM configurations that map non-coded bits

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7528253
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Vasile Bota, Mihaly Varga
- **PDF**: https://ieeexplore.ieee.org/document/7528253
- **Abstract**: This paper evaluates the bit-error rate and spectral efficiency performance provided by the convolutional coded Quadrature Amplitude Modulation (QAM) configurations whose global rates are modified mainly by changing the numbers of code and non-coded bits mapped on a QAM symbol. The Bit Error Rate (BER) performance provided are compared to the ones of the convolutional coded modulations which map only code bits and have the same configuration rates, aiming to show that coded configurations mapping non-coded bits as well, ensure a target BER value at smaller values of the Signal/Noise Ratio (SNR) than the ones mapping only code bits The paper also presents an approximate method to compute the BER of the configurations mapping both code and non-coded bits, which is validated by computer simulations and is shown to provide good accuracy in the range of BER values of practical interest.

## Single Pixel Camera with Compressive Sensing by non-uniform sampling

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7528202
- **Type**: conference
- **Published**: 9-10 June 
- **Authors**: Mihai-Alexandru Petrovici, Cristian Damian, Cristian Udrea +2
- **PDF**: https://ieeexplore.ieee.org/document/7528202
- **Abstract**: Compressive Sensing refers to the acquisition in compressed form of sparse signals. One of the CS applications is the Single Pixel Camera that rethinks the conventional imaging systems. The key part of the camera is a Spatial Light Modulator (SLM), which provides the mechanism for taking arbitrary measurements of the scene. The non-uniform sampling (NUS) scenario offers a simple procedure to select random samples from the scene, instead of taking random projections. This paper analyses the Single Pixel Camera performance using NUS in the case of two categories of samples: randomly distributed over the scene and selected from the contours vicinity. The NUS is compared, in terms of reconstructed images, with measurements obtained by projection on a random selection from the S-Transform basis. The results are given on simulated data and on real images obtained with the experimental model of a Single Pixel Camera. The comparison of reconstructed images in the three cases of measurements shows that, in terms of PSNR, the NUS with contour pixels is equivalent with the S-transform based measurement.

## Time-invariant spatially coupled low-density parity-check codes with small constraint length

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7901543
- **Type**: conference
- **Published**: 6-9 June 2
- **Authors**: Marco Baldi, Massimo Battaglioni, Franco Chiaraluce +1
- **PDF**: https://ieeexplore.ieee.org/document/7901543
- **Abstract**: We consider a special family of spatially coupled low-density parity-check (SC-LDPC) codes, that is, time-invariant low-density parity-check convolutional (LDPCC) codes, which are known in the literature for a long time. Codes of this kind are usually designed by starting from quasi-cyclic (QC) block codes, and applying suitable unwrapping procedures. We show that, by directly designing the LDPCC code syndrome former matrix without the constraints of the underlying QC block code, it is possible to achieve smaller constraint lengths with respect to the best solutions available in the literature. We also find theoretical lower bounds on the syndrome former constraint length for codes with a specified minimum length of the local cycles in their Tanner graphs. For this purpose, we exploit a new approach based on a numerical representation of the syndrome former matrix, which generalizes over a technique we already used to study a special subclass of the codes here considered.

## Code-aware quantizer design for finite-precision min-sum decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7901540
- **Type**: conference
- **Published**: 6-9 June 2
- **Authors**: Zeina Mheich, Thien-Truong Nguyen-Ly, Valentin Savin +1
- **PDF**: https://ieeexplore.ieee.org/document/7901540
- **Abstract**: Classically, the quantization of the soft information supplied to a finite-precision decoder is chosen to optimize a certain criterion which does not depend on the characteristics of the existing code. This work studies code-aware quantizers, for finite-precision min-sum decoders, which optimize the noise threshold of the existing family of Low-Density Parity-Check (LDPC) codes. We propose a code-aware quantizer with lower complexity than that obtained by optimizing all decision levels and approaching its performance, for few quantization bits. We show that code-aware quantizers outperform code-independent quantizers in terms of noise threshold for both regular and irregular LDPC codes. To overcome the error floor behavior of LDPC codes, we propose the design of the quantizer for a target error probability at the decoder output. The results show that the quantizer optimized to get a zero error probability could lead to a very bad performance for practical range of signal to noise ratios. Finally, we propose to design jointly irregular LDPC codes and code-aware quantizers for finite-precision min-sum decoders. We show that they achieve significant decoding gains with respect to LDPC codes designed for infinite-precision belief propagation decoding, but decoded by finite-precision min-sum.

## Application specific optimization: Rethinking protocol layering and standards

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7502430
- **Type**: conference
- **Published**: 6-10 June 
- **Authors**: John Peng, Stephen G. Wilson
- **PDF**: https://ieeexplore.ieee.org/document/7502430
- **Abstract**: There is a confluence of recent trends involving data center technology, software defined networks (SDN), and network function virtualization (NFV) that may open a way for general purpose networks to support application specific optimization (ASO). While traditional communications protocol architecture mandates layering where the lowest layers are application agnostic, research in cross layer design attests to the inefficiencies inherent in the “dumb pipes” networking paradigm. This paper investigates the potential of significant performance gains possible over the access network by departing from the traditional layered protocol approach and using a software defined protocol in conjunction with subscriber and application partitioning to provide ASO over the access network, while still maintaining a TCP/IP protocol stack to provide connectivity to the rest of the Internet. As a case study, we examine the potential performance gains provided by ASO of video streaming over the ADSL access network.

## Construction of irregular QC LDPC codes with low error floor for high speed optical communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7788012
- **Type**: conference
- **Published**: 5-10 June 
- **Authors**: Dongdong Wang, Liqian Wang, Xue Chen +5
- **PDF**: https://ieeexplore.ieee.org/document/7788012
- **Abstract**: We propose a construction method of irregular QC LDPC codes for high speed optical communications, by which the constructed codes not only can achieve high coding gain only through a few iterations but also do not exhibit error floor above the BER of 10−10.

## An iterative decoding scheme of concatenated LDPC and BCH codes for optical transport network

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7788004
- **Type**: conference
- **Published**: 5-10 June 
- **Authors**: Wei Zhou, Shaoliang Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7788004
- **Abstract**: An iterative decoding scheme of concatenated LDPC codes is proposed for optical networks. Simulation results show that a coding gain can be improved by 0.8dB compared to the conventional LDPC concatenated codes at a post-FEC BER=10−6.

## A new decryption algorithm of the quasi-cyclic low-density parity-check codes based McEliece cryptosystem

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7586588
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Shuo Zhang, Wenhui Cao, Angyang Li +2
- **PDF**: https://ieeexplore.ieee.org/document/7586588
- **Abstract**: The McEliece public-key cryptosystem is believed to resist quantum attacks, but has not been used because of the extremely large public key size. In order to decrease the public key size, quasi-cyclic low-density parity-check (QC-LDPC) codes were used instead of Goppa codes in McEliece cryptosystem. A modified version of QC-LDPC McEliece is quasi-cyclic moderate density parity-check (QC-MDPC) McEliece, which focuses on ensuring fixed security level other than error-correction capability. The QC-MDPC McEliece scheme furtherly reduces the public key size at the cost of higher decryption complexity. However, the decryption algorithm of QC-LDPC McEliece variant has not been optimized. In this paper, we proposed a new decryption algorithm of the QC-LDPC McEliece variant. With the decryption algorithm we proposed, the key size reduces about 20% than the original algorithm, even 8% smaller than QC-MDPC variant.

## A nonbinary LDPC product network coding scheme with signal space diversity

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7586693
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Chengxin Jiang, Zhanji Wu
- **PDF**: https://ieeexplore.ieee.org/document/7586693
- **Abstract**: A network coding scheme employing nonbinary low density parity check (LDPC) product code with signal space diversity (SSD) is proposed in this paper. The scheme is based on a multiple access relay channel with two users, one relay and one base station. Rotated modulation and component interleaving are introduced in this scheme to realize SSD so that it can enhance the bit error rate (BER) performance for the scheme. Simulation results indicate that the proposed scheme significantly outperforms the conventional binary scheme by 1.9dB in Rayleigh fading channel. Moreover, it also proves that the rotated modulation and component interleaving play an important role in improving the BER performance of the nonbinary LDPC product code.

## A soft-output error control method for wireless video transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7586585
- **Type**: conference
- **Published**: 4-6 June 2
- **Authors**: Bo Zheng, Shaoshuai Gao
- **PDF**: https://ieeexplore.ieee.org/document/7586585
- **Abstract**: With the rapid development of wireless network and multimedia technology, the efficient transmission over unreliable channel is becoming more and more important. The error control technique for video coding and transmission has drawn considerable attention, tries to recover the data loss and bit errors due to congestion or physical channel fading. Currently, there are three kinds of error control schemes, namely, error resilient coding at the encoder, error concealment at the decoder and the retransmission in the transport layer. In this paper, an error control scheme is proposed which uses the soft information in channel decoding to recover the corrupted bit stream. When bit error is detected in a slice, soft information of channel decoding is employed to locate it, and the wrong bits are flipped and decoded again at the beginning of the slice. The combination of XOR at source and the syntax checking of H.264 decoder has increased the error detection rate from around 60% to 99% without increasing source redundancy. Simulation results show that, when the same error concealing algorithm is used, the PSNR of the proposed scheme using soft information of channel decoding at the decoder is 1-2dB higher than that using the traditional method.

## Low Density Parity Check (LDPC) coded MIMO-Constant Envelop Modulation System with IF sampled 1-bit ADC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7518954
- **Type**: conference
- **Published**: 31 May-2 J
- **Authors**: Ahmed S. Mubarak, Amr Amrallah, Hany S. Hussein +1
- **PDF**: https://ieeexplore.ieee.org/document/7518954
- **Abstract**: MIMO-Constant Envelop Modulation (CEM) is a very power and complexity efficient system, which is introduced as alternative candidate to the currently used MIMO-Orthogonal Frequency Division Multiplexing (OFDM). CEM system enables to use high efficient nonlinear power amplifier on the transmitter side and 1 bit (low resolution) analog to digital converter (ADC) on the receiver side. Due to adopting the low resolution at the receiver side a great reduction in hardware complexity and power consumption can be achieved. However, there will be a noticeable degradation on the performance of bit error rate (BER) on the receiver side due to sever quantization error introduced by the low resolution ADC, so a forward error correction coding is essential to enhance the BER. In this paper a LDPC coded MIMO-CEM system was used as a replacement for MIMO-OFDM to deal with the BER degradation problem of the CEM system. The performance of the LDPC coded MIMO-CEM with Gaussian Minimum Phase Shift Keying (GMSK) modulation is evaluated over a multi-path Rayleigh fading channel. It showed that LDPC codes are effective to improve the BER performance of CEM on Rayleigh fading channels. According to the simulation results, the MIMO-CEM system provides a significant improvement in BER performance and outperforms the un-coded and the original convolutional coder based CEM systems.

## Performance analysis of low density parity check codes implemented in second generations of digital video broadcasting standards

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7522195
- **Type**: conference
- **Published**: 30 May-3 J
- **Authors**: Gr. Y. Mihaylov, T. B. Iliev, E. P. Ivanova +2
- **PDF**: https://ieeexplore.ieee.org/document/7522195
- **Abstract**: The newly developed second generations standards for digital video broadcasting (DVB-T2, DVB-S2) emerges as a significant upgrade over its first generation predecessor. Low-Density Parity-Check (LDPC) codes received a lot of attention by their superb error-correcting capability and have been adopted as main error correct coding scheme by second generation Digital Video Broadcasting standards. The goal of this paper is to present the main constructive principle of low-density parity check codes, as well as a design methodology, that gives good performance for many communication systems like latest DVB satellite communications standard. In this paper we analyze the structure of LDPC codes and the iterative algorithms that are used to decode them. An analysis and simulation of the LDPC codes has been conducted using various code rates. The simulation results show that LDPC codes are a powerful error correcting coding technique under SNR environments. It has achieved near Shannon capacity. However, there are many factors needed to be considered in the LDPC code design.

## On the error detection capability of combined LDPC and CRC codes for space telecommand transmissions

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7543876
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Marco Baldi, Nicola Maturo, Giacomo Ricciutelli +1
- **PDF**: https://ieeexplore.ieee.org/document/7543876
- **Abstract**: We present a method for estimating the undetected error rate when a cyclic redundancy check (CRC) is performed on the output of the decoder of short low-density parity-check (LDPC) codes. This system is of interest for telecommand links, where new LDPC codes have been designed for updating the current standard. We show that these new LDPC codes combined with CRC are adequate for complying with the stringent requirements of this kind of transmissions in terms of error detection.

## Link adaptation in FBMC/OQAM systems using NB-LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7560995
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Màrius Caus, Monica Navarro, Xavier Mestre +1
- **PDF**: https://ieeexplore.ieee.org/document/7560995
- **Abstract**: This paper investigates the application of non-binary low density parity check (NB-LDPC) codes to offset-QAM based filter bank multicarrier systems, known as FBMC/OQAM. The analysis conducted in the paper reveals that the mapping scheme can be optimized to simplify detection and minimize the correlation of the noise. Based on the proposed modifications, existing adaptive coding and modulation (ACM) algorithms can be easily tailored to accommodate the characteristics of NB-LDPC and FBMC/OQAM. In this paper, priority has been given to mutual information-based ACM algorithms. Numerical results verify that the proposed algorithm guarantees the target block error rate.

## Study of indoor LTE green small-cells using mobile fronthaul architecture over hybrid fiber-wireless channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7561029
- **Type**: conference
- **Published**: 27-30 June
- **Authors**: Y. Hazan, M. Ran
- **PDF**: https://ieeexplore.ieee.org/document/7561029
- **Abstract**: 6Gbps transmission over low power indoor LTE air-interface is demonstrated by using single-mode fiber based fronthaul architecture combined with plastic optical fiber indoor small-cells. The low power transmission coverage is similar to the classic femtocell coverage and is suitable for most indoor scenarios.

## Variable throughput LDPC decoders using SIMD-based adaptive quantization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7760912
- **Type**: conference
- **Published**: 27-29 June
- **Authors**: Virgil Petcu, Oana Boncalo, Alexandru Amaricai +1
- **PDF**: https://ieeexplore.ieee.org/document/7760912
- **Abstract**: In this paper, we present an LDPC decoder design equipped with an adaptive throughput mechanism achievable using a multiple quantization scheme. Three representations are supported by the proposed architecture: 1-bit (hard decision), 2-bit, and 4-bit messages. A throughput increase by of factor of 4, 2 and 1 can be achieved with respect to the 4-bit message representation version, by simultaneously decoding 4, 2, or 1 codewords. This is done by employing a single instruction multiple data (SIMD) approach at processing unit level which is able to process 4, 2 and 1 operands corresponding to the distinct codewords. We provide implementation results for a partial parallel flooding architecture, with serial processing at processing node level. FPGA implementation results indicate that the proposed SIMD approach has an overhead of about 60% in logic with respect to the fixed 4-bit LDPC decoder, with no memory increase, while having a throughput increase of 4× when the hard-decision decoding is used.

## Reduced-complexity decoding algorithms of Raptor codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7760847
- **Type**: conference
- **Published**: 27-29 June
- **Authors**: Cenk Albayrak, Kadir Turk
- **PDF**: https://ieeexplore.ieee.org/document/7760847
- **Abstract**: In this paper, the belief propagation (BP) based approximation methods which are introduced for low density parity check (LDPC) codes in literature are adapted to the Raptor decoder structure in order to reduce its computational complexity. The bit error rate (BER) performances of the algorithms over the additive white Gaussian noise (AWGN) channel are obtained by both theoretical works and simulations. The Monte-Carlo based density evolution (MC-DE) method is used for theoretical analysis. In addition to this, computational complexity analyses of the considered methods are presented. Results show that the computational complexity can be significantly decreased with a limited performance loss cost.

## Improved iterative convergence method in Q-ary LDPC coded high order PR-CPM

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7514680
- **Type**: journal
- **Published**: 22 June 20
- **Authors**: Danfeng Zhao, Yanbo Sun, Rui Xue
- **PDF**: https://ieeexplore.ieee.org/document/7514680
- **Abstract**: The Q-ary low-density parity-check (LDPC) coded high order partial response continuous phase modulation (PR-CPM) with double iterative loops is investigated. This scheme shows significant improvements in power and bandwidth efficiency, but at the expense of long iterative decoding delay and computational complexity induced by the improper match between the demodulator and the decoder. To address this issue, the convergence behavior of Q-ary LDPC coded CPM is investigated for the Q=2 and Q>2 cases, and an optimized design method based on the extrinsic information transfer chart is proposed to improve the systematic iterative efficiency. Simulation results demonstrate that the proposed method can achieve a perfect tradeoff between iterative decoding delay and bit error rate performance to satisfy real-time applications.

## FPGA implementation of regular random LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7589691
- **Type**: conference
- **Published**: 17-19 June
- **Authors**: Huang Xin, Liu Yong, Ding Kui
- **PDF**: https://ieeexplore.ieee.org/document/7589691
- **Abstract**: In order to ensure the performance at the same time to reduce the complexity of the encoding and decoding, the paper focuses on the binary regular random LDPC codes of fast encoding and decoding and its hardware implementation method. This idea can be effectively realized by using upper triangular and lower triangular (LU) decomposition of the the minimal product of row weight and column weight as the principal component as well as the log domain decoding method. For FPGA design, the key is to solve the contradiction between the amount of resource, encoding and decoding efficiency, so as to achieve a higher efficiency of the compile at the same time the amount of resource is relatively small.

## Non-uniform quantization scheme for the decoding of low-density parity-check codes with the sum-product algorithm

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7589702
- **Type**: conference
- **Published**: 17-19 June
- **Authors**: Xinru Qu, Liuguo Yin
- **PDF**: https://ieeexplore.ieee.org/document/7589702
- **Abstract**: In this paper, a non-uniform quantization scheme is proposed for the decoding of Low-Density Parity-Check (LDPC) codes with the Sum-Product Algorithm (SPA). With the proposed scheme, the quantization-range and quantization-interval for the soft Log-Likelihood-Ratio (LLR) values of the decoder input, the variable nodes, and the check nodes are set separately, and are also adjusted according to the evolution of the probability density distribution of the LLR values in the iterative decoding procedure to minimize the difference between the decoding values before quantization and that after quantization. Simulation results show that decoding with 3-bit non-uniform quantization of the proposed scheme may obtain a BER performance slightly better than that of decoding with 6-bits quantization of the traditional uniform quantization method.

## Improving performance of multithreshold decoder for self-orthogonal codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7525744
- **Type**: conference
- **Published**: 12-16 June
- **Authors**: A.I. Baranchikov, N.N. Grinchenko, G.V. Ovechkin
- **PDF**: https://ieeexplore.ieee.org/document/7525744
- **Abstract**: The article discusses self-orthogonal error-correcting codes (SOC) for the decoding of which multithreshold algorithms (MTD) are usually used. To decode SOC the algorithms used for low-density parity-check (LDPC) codes can also be applied. The article shows that using a min-sum decoder for SOC over a channel with additive white Gaussian noise (AWGN) in case of binary phase shift keying allows to receive additional coding gain about 1..1,5 dB in comparison with MTD usage. At the same time computing complexity in a min-sum algorithm turns out to be 6...7 times higher than MTD. For SOC decoding the work offers a combined decoder including the elements of MTD and min-sum algorithms. The first several decoding iterations require the usage of min-sum decoder while later MTD is added. The results of offered decoder simulation show about 1 dB increase of coding gain in comparison with MTD for SOC over a channel with AWGN with binary phase shift keying in case of twofold increase of computing complexity. The gain received depends on the SOC used, the number of min-sum decoding iterations and MTD.

## Self-corrected UMP-APP decoding of LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7525774
- **Type**: conference
- **Published**: 12-16 June
- **Authors**: V.V. Vityazev, E.A. Likhobabin
- **PDF**: https://ieeexplore.ieee.org/document/7525774
- **Abstract**: In this paper we propose a very simple but powerful self-correction method for the UMP-APP decoding of LDPC codes. Like self-corrected min-sum decoding, our method does not try to correct the check node processing approximation, but it modifies the variable node processing by erasing unreliable messages. Monte-Carlo simulations show that the proposed self-corrected UMP-APP decoding performs better then common UMP-APP decoding. Estimation of the complexity and average number of iteration for self-corrected UMP-APP algorithm are also shown.

## A cycle-based rate-compatible puncturing technique for non-binary LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7746650
- **Type**: conference
- **Published**: 12-15 June
- **Authors**: Kuntal Deka, A. Rajesh, P. K. Bora
- **PDF**: https://ieeexplore.ieee.org/document/7746650
- **Abstract**: This paper presents a cycle-based rate-compatible puncturing technique for non-binary (NB) low-density parity-check (LDPC) codes. The proposed puncturing technique is based on the connectivity of the short non-binary (NB) cycles present in the Tanner graph. The connectivity of a cycle is measured by the extrinsic message degree (EMD). The short cycles with low values of EMD degrade the performance of iterative decoders significantly. The proposed technique selects the variable nodes for puncturing by reckoning their involvements in the short NB cycles with a low EMD. Simulations in different contexts are performed to check the efficiency of the proposed technique.

## On the performance of fixed-length spatially coupled LDPC code

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7521994
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Shuang Chen, Kewu Peng, Huangpin Jin +1
- **PDF**: https://ieeexplore.ieee.org/document/7521994
- **Abstract**: This paper evaluates the rate loss of fixed-length spatially-coupled low-density parity-check (SC-LDPC) code compared to the asymptotic performance of such code. In previous works, SC-LDPC with sufficient length of codeword shows excellent asymptotic performance and attracts a lot of attentions. However, when the length of codeword is limited, the performance of SC-LDPC code with limited codeword-length is not as well studied as its counterpart with infinite codeword-length. In this paper, the rate loss of a fixed-length SC-LDPC will be analyzed from two aspects: the rate loss due to finite length of the uncoupled code, and the rate loss due to finite length of the coupling chain. Furthermore, through trade-off between the length of the coupling chain and that of the uncoupled code, the rate loss of the SC-LDPC is optimized. The optimization results show that the trend of the rate loss of a length-N SC-LDPC is O(N-1/3) and is different from that of a conventional LDPC code [1], which is O(N-1/2). In other words, for achieving similar performance of a conventional length-N LDPC code, the length of an SC-LDPC code should be increased to O(N3/2).

## Implementation of ISDB-T LDM broadcast system using LDPC codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7521986
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: George Henrique Maranhão Garcia de Oliveira, Cristiano Akamine, Yuri Pontes Maciel
- **PDF**: https://ieeexplore.ieee.org/document/7521986
- **Abstract**: This paper presents the scenario of terrestrial broadcast services, the challenges and needed adaptations for the next generation television. It shows promising technologies such as LDM, LDPC, NUC and their advantages in terms of increase of transmission rate, robustness and efficient use of spectrum. It also proposes an adapted ISDB-T system that uses LDM, LDPC, NUC and SDR technologies to increase performance and useful bit rate to DTV applications, while using a layer that would still be compatible with traditional ISDB-T system.

## Variable LLR scaling in LDPC min-sum decoding under horizontal shuffled structure

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7521937
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Kang Zhao, Yin Xu, Dazhi He +2
- **PDF**: https://ieeexplore.ieee.org/document/7521937
- **Abstract**: LDPC was first proposed in 1962, after that considerable achievements have been made both in decoding algorithms and also in the structure of the decoder. In terms of decoding algorithm, from belief propagation (BP) to min-sum (MS), then normalized MS (NMS) and finally to a more performance oriented variable MS (VMS) algorithm. In terms of the decoder structure, there are mainly two, flooding and shuffled structure (FS and SS), and flooding structure is mainly used in the past and the selection of variable factors in FS VMS has already been studied in the literature. As is known, the horizontal shuffled structure (HSS) are more hardware friendly and now widely deployed, thus to apply VMS algorithm to HSS has an important meaning for the industry. However, there is no effective method for the selection of variable factors in HSS VMS. Based on the study of FS VMS, this paper describes how to apply the generalized mutual information (GMI) based metric to HSS VMS reasonably and proposes the modified GMI based formula. Simulation results on a certain DVB-S2's LDPC code show that, by using modified formula for HSS VMS, we can obtain 0.13dB gain over HSS NMS and the performance is only 0.1dB away from that of HSS BP in terms of bit error rate (BER) at level 1e-7. And simulation results on a certain DVB-T2's LDPC code show that, by using modified formula for HSS VMS, we can obtain 0.04dB gain over HSS NMS and the performance is only 0.06dB away from that of HSS BP in terms of bit error rate (BER) at level 1e-7.

## Performance measurement of high-efficient OFDM based transmission system in commercial HFC network

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7522004
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Sang-Jung Ra, JinHyuk Song, JaeHwui Bae +4
- **PDF**: https://ieeexplore.ieee.org/document/7522004
- **Abstract**: This paper describes the results of a field test of an OFDM-based transmission system that uses digital video broadcasting for a cable system and is implemented using field programmable gate arrays (FPGAs). For the field test, a 4096QAM, 4096 Fast Fourier Transform (FFT), 9/10 code rate of a low-density parity check (LDPC), and 6-MHz channel bandwidth were selected. To evaluate the practical performance of the implemented transmission system, a commercial MPEG Analyzer is used for the performance evaluation.

## Pilot optimization for mobile services in ATSC 3.0

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7522005
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Eduardo Garro, Jordi Joan Gimenez, David Gomez-Barquero +1
- **PDF**: https://ieeexplore.ieee.org/document/7522005
- **Abstract**: The Advanced Television System Committee (ATSC) has released ATSC 3.0, the next-generation U.S. Digital Terrestrial Television (DTT) standard. ATSC 3.0 allows a higher flexibility compared to the previous state-of-the-art DTT standard, DVB-T2 (Digital Video Broadcasting - Terrestrial 2nd Generation). This higher flexibility allows broadcasters to adapt transmission configuration to network and reception requirements. Regarding pilot patterns (PP), whereas DVB-T2 provides 8 different PPs with a unique pilot boosting, ATSC 3.0 extends up to 16 different PPs, with 5 different boostings per each one. This paper is focused on the study of the PP and boosting combination that optimizes performance for time (Time Division Multiplexing, TDM) and power (Layered Division Multiplexing, LDM) multiplexing modes of ATSC 3.0 in mobility reception conditions. The selection of the optimum PP is particularly essential in LDM mode, because it must be shared between the two LDM layers.

## Field trial of a redundancy on demand DVB-T2 system

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:7521909
- **Type**: conference
- **Published**: 1-3 June 2
- **Authors**: Fabian Schrieber, Jan Zoellner, Lothar Stadelmeier +3
- **PDF**: https://ieeexplore.ieee.org/document/7521909
- **Abstract**: Different digital terrestrial television (DTT) systems are in use around the world today. A rapidly growing number of TV sets used for terrestrial broadcast reception is also equipped with broadband connectivity. However, the distribution of TV content relies either solely on terrestrial broadcast or on broadband delivery. Redundancy on Demand (RoD) on the other hand utilizes the broadband connectivity to enhance terrestrial broadcast reception. RoD is a fully backward compatible extension to terrestrial broadcast systems. It provides supporting data, i.e. additional redundancy, on demand to broadcast receivers via a broadband connection. Receivers even in unfavorable reception conditions are then able to successfully decode the broadcast signal. The supporting data is provided by an RoD server extending the broadcast network. An RoD DTT receiver is able to estimate the signal quality, request and receive the redundancy data if required and decode the broadcast signal with the help of the broadband data. As the second generation terrestrial Digital Video Broadcasting (DVB-T2) will be introduced in Germany starting in 2016, a DVB-T2 trial network was set up in Berlin. This network gave the opportunity to evaluate the performance of RoD with DVB-T2 in a real world environment. This paper presents results of the field trial.
