# IEEE Xplore — 2013-07


## Layered Dynamic Schedulings for BP Decoding of LDPC Codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC BP 스케줄링 - 비이진 제외
- **ID**: ieee:10284008
- **Type**: journal
- **Published**: July 2013
- **Authors**: Han Guojun, Liu Xingcheng, Gong Yi
- **PDF**: https://ieeexplore.ieee.org/document/10284008
- **Abstract**: A Layered dynamic scheduling (LDS) for Belief-propagation (BP) decoding of LDPC codes over GF(q) is presented, which is derived from the dynamic scheduling for the BP decoding of binary LDPC codes. In order to restrain the LDS from cycling in certain check-nodes, a life-index for each check-node is adopted and the optimal value of the life-index is analyzed. Furthermore, in consideration of hardware implementation and decoding latency, a strategy, which allows many more check-nodes to be updated in parallel, is introduced. Simulations show that the LDS with life-index speeds up the convergence rate and greatly improves the performance of the BP decoding at medium to high signal-to-noise ratio value, and the algorithm employing the LDS with life-index and the new strategy offers good trade-off between the performance and the decoding latency.

## Blind Identification of Nonbinary LDPC Codes Using Average LLR of Syndrome a Posteriori Probability

- **Status**: ❌
- **Reason**: 비이진 LDPC 인코더 블라인드 식별(GF(q)), non-binary+ECC 디코더 아님
- **ID**: ieee:6517357
- **Type**: journal
- **Published**: July 2013
- **Authors**: Tian Xia, Hsiao-Chun Wu
- **PDF**: https://ieeexplore.ieee.org/document/6517357
- **Abstract**: Prevalent adaptive modulation and coding (AMC) techniques can facilitate the flexible strategies subject to the dynamic channel quality. It would be quite intriguing for one to build a blind encoder identification technique without spectrum-efficiency sacrifice for AMC transceivers. In this paper, we make the first-ever attempt to tackle the blind nonbinary low-density parity-check (LDPC) encoder identification given a predefined encoder candidate set over the Galois field GF(q) for q-ary quadrature amplitude modulation (q-QAM) signals. Our proposed method establishes the log-likelihood ratios (LLRs) of syndrome a posteriori probabilities (APPs), which specify the potential correctness of the underlying parity-check relations, and identifies the nonbinary LDPC encoder leading to the maximum average LLR over the candidate set. Monte Carlo simulation results verify the effectiveness of our proposed new scheme.

## Nonbinary LDPC Coding System With Symbol-By-Symbol Turbo Equalizer for Shingled Magnetic Recording

- **Status**: ❌
- **Reason**: 비이진 GF(2^8) LDPC + 심볼단위 turbo equalizer, non-binary는 제외 대상
- **ID**: ieee:6559097
- **Type**: journal
- **Published**: July 2013
- **Authors**: Yasuaki Nakamura, Jun Ueda, Yoshihiro Okamoto +2
- **PDF**: https://ieeexplore.ieee.org/document/6559097
- **Abstract**: Two-dimensional magnetic recording (TDMR) by shingled magnetic recording (SMR) is one of the most promising technologies for realizing high areal densities. The read/write (R/W) channel model based on a discrete Voronoi model is relatively easily implemented to evaluate the performance of signal processing for TDMR. The nonbinary low-density parity-check (LDPC) coding and iterative decoding system provides the better performance compared with the conventional binary LDPC coding system. Furthermore, a two-dimensional equalizer (2D-EQ) can mitigate the influence of the intertrack interference (ITI) in TDMR. In this paper, the symbol-by-symbol turbo equalizer which consists of a symbol-by-symbol a posteriori probability (APP) decoder for a generalized partial response class-I (GPR1) channel with a 2D-EQ and a sum-product (SP) decoder for a nonbinary LDPC coder over Galois field of GF(28) is evaluated by computer simulation at an areal recording density of 4.12 Tbit/in2. The result shows that the symbol-by-symbol turbo equalizing system provides an SNR improvement of about 3.7 dB over the bit-by-bit turbo equalizing system.

## Trellis-Based Extended Min-Sum Algorithm for Non-Binary LDPC Codes and its Hardware Structure

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC GF(q) EMS 디코더→non-binary 제외
- **ID**: ieee:6516166
- **Type**: journal
- **Published**: July 2013
- **Authors**: Erbao Li, David Declercq, Kiran Gunnam
- **PDF**: https://ieeexplore.ieee.org/document/6516166
- **Abstract**: In this paper, we present an improvement and a new implementation of a simplified decoding algorithm for non-binary low density parity-check codes (NB-LDPC) in Galois fields GF(q). The base algorithm that we use is the Extended Min-Sum (EMS) algorithm, which has been widely studied in the recent literature, and has been shown to approach the performance of the belief propagation (BP) algorithm, with limited complexity. In our work, we propose a new way to compute modified configuration sets, using a trellis representation of incoming messages to check nodes. We call our modification of the EMS algorithm trellis-EMS (T-EMS). In the T-EMS, the algorithm operates directly on the deviation space by considering a trellis built from differential messages, which serves as a new reliability measure to sort the configurations. We show that this new trellis representation reduces the computational complexity, without any performance degradation. In addition, we show that our modifications of the algorithm allows to greatly reduce the decoding latency, by using a larger degree of hardware parallelization.

## Distributed Block Arithmetic Coding for Equiprobable Sources

- **Status**: ❌
- **Reason**: 분산 산술부호(소스 코딩), 채널 ECC 아님
- **ID**: ieee:6497476
- **Type**: journal
- **Published**: July 2013
- **Authors**: Junwei Zhou, Kwok-Wo Wong, Jianyong Chen
- **PDF**: https://ieeexplore.ieee.org/document/6497476
- **Abstract**: Distributed arithmetic coding (DAC) is similar to syndrome coding, in the sense that message sequences sharing the same interval can be considered a coset of the space of the source sequences, and the codeword is the index of the coset. In this paper, the minimum Hamming distance of cosets is studied and it is proved that such a distance is as small as one. By only allowing the sequences with a large Hamming distance to overlap in the same interval, an improved DAC scheme is proposed. Simulation results show that, for equiprobable memoryless sources, this approach outperforms DAC in terms of decoding error rate at the same coding cost. In addition, at small sequence length, the decoding error rate of the proposed scheme is lower than that of distributed source coding based on low-density parity-check codes for highly correlated sources.

## On the Mitigation of Impulsive Noise in Power-Line Communications With LT Codes

- **Status**: ❌
- **Reason**: PLC 임펄스잡음 완화 LT+LDPC concatenation, LDPC는 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:6514721
- **Type**: journal
- **Published**: July 2013
- **Authors**: Nikoleta Andreadou, Andrea M. Tonello
- **PDF**: https://ieeexplore.ieee.org/document/6514721
- **Abstract**: In this paper, we present a concatenated coding scheme that mitigates the effect of impulsive noise in orthogonal frequency-division multiplexing-based power-line communications (PLC) systems. What we propose is a novel technique that uses Luby transform (LT) codes as the outer scheme along with irregular low-density parity check (LDPC) codes as the inner code applied on the physical layer. The scheme fully exploits the features of LT codes and mitigates the impulsive noise effect even under high impulse level conditions. By introducing a small percentage of additional packets at the LT transmitter, the packets that are mostly affected by impulsive noise on the PLC channel are treated as erasures at the LT decoding procedure, thus resulting in a reduced error rate. In this innovative scheme, the receiver can identify the packets to be marked as erased even without channel state information, just by taking into account the properties of the inner LDPC code. Furthermore, we propose a method according to which the redundancy introduced by LT codes can be kept at low levels.

## Bounds on the Minimum Distance of Punctured Quasi-Cyclic LDPC Codes

- **Status**: ❌
- **Reason**: punctured QC-LDPC 최소거리 상한의 순수 이론 bound, 디코더/HW/구성 신규 기여 없음
- **ID**: ieee:6482231
- **Type**: journal
- **Published**: July 2013
- **Authors**: Brian K. Butler, Paul H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/6482231
- **Abstract**: Recent work by Divsalar  has shown that properly designed protograph-based low-density parity-check codes typically have minimum (Hamming) distance linearly increasing with block length. This fact rests on ensemble arguments over all possible expansions of the base protograph. However, when implementation complexity is considered, the expansions are frequently selected from a smaller class of structured expansions. For example, protograph expansion by cyclically shifting connections generates a quasi-cyclic (QC) code. Other recent work by Smarandache and Vontobel has provided upper bounds on the minimum distance of QC codes. In this paper, we generalize these bounds to punctured QC codes and then show how to tighten these for certain classes of codes. We then evaluate these upper bounds for the family of protograph codes known as AR4JA codes that have been recommended for use in deep space communications in a standard established by the Consultative Committee for Space Data Systems. At block lengths larger than 4400 bits, these upper bounds fall well below the ensemble lower bounds.

## Performance Evaluation of Neuro ITI Canceller for Two-Dimensional Magnetic Recording by Shingled Magnetic Recording

- **Status**: ❌
- **Reason**: TDMR ITI 캔슬러(neuro-ITIC) 신호처리, LDPC는 부수 언급이며 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:6558943
- **Type**: journal
- **Published**: July 2013
- **Authors**: Masato Yamashita, Yoshihiro Okamoto, Yasuaki Nakamura +2
- **PDF**: https://ieeexplore.ieee.org/document/6558943
- **Abstract**: A neuro intertrack interference canceller (neuro-ITIC) is proposed to diminish the influences of ITI and jitter-like medium noise for two-dimensional magnetic recording (TDMR) by shingled magnetic recording. The bit error rate (BER) performance of a low-density parity-check coding and iterative decoding system including a generalized partial response class-I channel with the neuro-ITIC is also obtained via computer simulation using a read/write channel model under TDMR specifications of 4 Tb/in , and it is compared to those for a two-dimensional neural network equalizer (2D-NNE) and an ITI canceller (ITIC) with a one-dimensional finite impulse response equalizer (1D-FIRE). It is clarified that the BER performance for the neuro-ITIC is far superior to those for the 2D-NNE and the ITIC with the 1D-FIRE.

## An Integrated Linear Programming Receiver for LDPC Coded MIMO-OFDM Signals

- **Status**: ❌
- **Reason**: LDPC-coded MIMO-OFDM 결합 검출/디코딩 LP 수신기, 신호검출 특이적이고 NAND 이식 불가
- **ID**: ieee:6516170
- **Type**: journal
- **Published**: July 2013
- **Authors**: Yong Li, Lin Wang, Zhi Ding
- **PDF**: https://ieeexplore.ieee.org/document/6516170
- **Abstract**: This work investigates the joint detection and decoding of MIMO-OFDM signals. Traditional receivers either utilize disjoint serial detector and decoder or require turbo message passing between the two functional blocks of detection and decoding. We present a novel approach that can jointly achieve detection and decoding of low density parity check (LDPC) coded multiple-input-multiple-output (MIMO) orthogonal-frequency-division-multiplexing (OFDM) signals as a unified optimization algorithm. Our receiver integrates the MIMO-OFDM signal detection and the decoding of LDPC coded data by formulating a linear programming problem regardless of affine or nonaffine quadrature amplitude modulation (QAM) mapping. The proposed joint MIMO-OFDM detector and decoder achieves substantial performance gain over existing joint detection receivers of comparable computational complexity. Furthermore, the proposed receiver also substantially outperforms the more traditional turbo receiver with only modest cost in complexity.

## A Robust Multi-Level Design for Dirty-Paper Coding

- **Status**: ❌
- **Reason**: dirty-paper coding에 multi-level LDPC+TCQ, 표준 LDPC를 컴포넌트로 사용, 떼어낼 신규 BP 기법 없음
- **ID**: ieee:6516169
- **Type**: journal
- **Published**: July 2013
- **Authors**: Momin Uppal, Guosen Yue, Yan Xin +2
- **PDF**: https://ieeexplore.ieee.org/document/6516169
- **Abstract**: We propose a robust close-to-capacity dirty-paper coding (DPC) design framework in which multi-level low density parity check (LDPC) codes and trellis coded quantization (TCQ) are employed as the channel and source coding components, respectively. The proposed design framework is robust in the sense that it yields close to capacity solutions in the high-, medium-, and low-rate regimes. This is in contrast to existing practical DPC schemes that perform well only in one or two of these regimes, but not all three. We design codes for transmission rates of 0.5, 1.0, 1.5, and 2.0 bits/sample (b/s) using one, two, three, and four LDPC levels; at a block length of 2×105, the codes perform 0.95, 0.58, 0.55, and 0.54 dB from the corresponding information theoretic limits, respectively. We also propose a low-complexity decoding scheme that does not involve iterative message passing between the source and channel decoders; the low-complexity scheme performs only 1.08, 0.85, and 0.79 dB away from the theoretical limits at transmission rates of 1.0, 1.5, and 2.0 b/s, respectively.

## Joint and Separate Detection-Decoding on BPMR Channels

- **Status**: ❌
- **Reason**: BPMR Davey-MacKay 검출-복호 결합 알고리즘, LDPC는 외부 부호이며 채널/검출 특이적 기법
- **ID**: ieee:6559239
- **Type**: journal
- **Published**: July 2013
- **Authors**: Tong Wu, Marc A. Armand
- **PDF**: https://ieeexplore.ieee.org/document/6559239
- **Abstract**: The presence of written-in errors is recognized as a challenging issue that limits the performance of bit-patterned media recording (BPMR). In this paper, we consider the Davey-MacKay coding scheme for a BPMR channel model which consists of a write channel producing dependent insertion, deletion, and substitution errors and a single-track equalized read channel with a GPR target. Three detection-decoding algorithms are proposed to work with an outer LDPC decoder to recover data encoded by the DM coding scheme on the BPMR channel. These include the Bahl-Cocke-Jelinek-Raviv binary input inner decoder (BCJR-BIID) algorithm, the joint detection-decoding algorithm and the separate detection-decoding (SDD) algorithm. Computer simulations show that at low to moderate (resp. high) signal-to-noise ratios, SDD (resp. BCJR-BIID) provides good performance-complexity trade-offs.

## Design of Length-Compatible Polar Codes Based on the Reduction of Polarizing Matrices

- **Status**: ❌
- **Reason**: 비-LDPC(polar) 부호 길이호환 설계, SC 디코딩 전용 기법으로 LDPC BP 이식 불가
- **ID**: ieee:6522416
- **Type**: journal
- **Published**: July 2013
- **Authors**: Dong-Min Shin, Seung-Chan Lim, Kyeongcheol Yang
- **PDF**: https://ieeexplore.ieee.org/document/6522416
- **Abstract**: Length-compatible polar codes are a class of polar codes which can support a wide range of lengths with a single pair of encoder and decoder. In this paper we propose a method to construct length-compatible polar codes by employing the reduction of the 2n × 2n polarizing matrix proposed by Arikan. The conditions under which a reduced matrix becomes a polarizing matrix supporting a polar code of a given length are first analyzed. Based on these conditions, length-compatible polar codes are constructed in a suboptimal way by codeword-puncturing and information-refreezing processes. They have low encoding and decoding complexity since they can be encoded and decoded in a similar way as a polar code of length 2n. Numerical results show that length-compatible polar codes designed by the proposed method provide a performance gain of about 1.0 - 5.0 dB over those obtained by random puncturing when successive cancellation decoding is employed.

## From Nominal to True A Posteriori Probabilities: An Exact Bayesian Theorem Based Probabilistic Data Association Approach for Iterative MIMO Detection and Decoding

- **Status**: ❌
- **Reason**: MIMO IDD용 PDA 검출기 기법, LDPC 부호 비의존 검출 알고리즘으로 NAND LDPC ECC와 무관
- **ID**: ieee:6528070
- **Type**: journal
- **Published**: July 2013
- **Authors**: Shaoshi Yang, Tiejun Lv, Robert G. Maunder +1
- **PDF**: https://ieeexplore.ieee.org/document/6528070
- **Abstract**: It was conventionally regarded that the approximate Bayesian theorem based existing probabilistic data association (PDA) algorithms output the estimated symbol-wise a posteriori probabilities (APPs) as soft information. In our recent work, however, we demonstrated that these probabilities are not the true APPs in the rigorous mathematical sense, but a type of nominal APPs, which are unsuitable for the classic architecture of iterative detection and decoding (IDD) aided receivers. To circumvent this predicament, in this paper we propose an exact Bayesian theorem based logarithmic domain PDA (EB-Log-PDA) method, whose output has similar characteristics to the true APPs, and hence it is readily applicable to the classic IDD architecture of multiple-input-multiple-output (MIMO) systems using the general M-ary modulation. Furthermore, we investigate the impact of the EB-Log-PDA algorithm's inner iteration on the design of EB-Log-PDA aided IDD receiver. We demonstrate that introducing inner iterations into EB-Log-PDA, which is common practice in conventional-PDA aided uncoded MIMO systems, would actually degrade the IDD receiver's performance, despite significantly increasing the overall computational complexity of the IDD receiver. Finally, we investigate the relationship between the extrinsic log-likelihood ratios (LLRs) of the proposed EB-Log-PDA and of the approximate Bayesian theorem based logarithmic domain PDA (AB-Log-PDA) reported in our previous work. Despite their difference in extrinsic LLRs, we also show that the IDD schemes employing the EB-Log-PDA and the AB-Log-PDA without incorporating any inner PDA iterations have a similar achievable performance close to that of the optimal maximum a posteriori (MAP) detector based IDD receiver, while imposing a significantly lower computational complexity in the scenarios considered.

## Symbol Error Rate of Space - Time Network Coding in Nakagami-m Fading

- **Status**: ❌
- **Reason**: Space-Time Network Coding SER 분석, LDPC 무관 무선통신
- **ID**: ieee:6416079
- **Type**: journal
- **Published**: July 2013
- **Authors**: Ang Yang, Zesong Fei, Nan Yang +2
- **PDF**: https://ieeexplore.ieee.org/document/6416079
- **Abstract**: In this paper, we analyze the symbol error rate (SER) of space-time network coding (STNC) in a distributed cooperative network over independent but not necessarily identically distributed (i.n.i.d.) Nakagami-m fading channels. In this network, multiple sources communicate with a single destination with the assistance of multiple decode-and-forward (DF) relays. We first derive new exact closed-form expressions for the SER with M-ary phase-shift keying modulation (M-PSK) and M-ary quadrature-amplitude modulation (M-QAM). We then derive new compact expressions for the asymptotic SER to offer valuable insights into the network behavior in the high signal-to-noise ratio (SNR) regime. Importantly, we demonstrate that STNC guarantees full diversity order, which is determined by the Nakagami-m fading parameters of all the channels but independent of the number of sources. Based on the new expressions, we examine the impact of the number of relays, relay location, Nakagami-m fading parameters, power allocation, and nonorthogonal codes on the SER.

## An 0.8-mm$^2$  9.6-mW Iterative Decoder for Faster-Than-Nyquist and Orthogonal Signaling Multicarrier Systems in 65-nm CMOS

- **Status**: ❌
- **Reason**: FTN/직교 멀티캐리어 신호용 반복 디코더, 부호 비의존 LDPC BP 기법 아님(신호검출 특이)
- **ID**: ieee:6493457
- **Type**: journal
- **Published**: July 2013
- **Authors**: Deepak Dasalukunte, Fredrik Rusek, Viktor Öwall
- **PDF**: https://ieeexplore.ieee.org/document/6493457
- **Abstract**: This paper presents an iterative decoder for faster-than-Nyquist (FTN) and orthogonal signaling multi-carrier systems. FTN signaling is a method of improving bandwidth efficiency at the expense of higher processing complexity in the transceiver. The decoder can switch between orthogonal and FTN signaling modes and exploits channel properties to improve bandwidth efficiency. The decoder is fabricated in a 65-nm CMOS process and occupies a total area of 0.8 mm2 with decoder core taking up 0.567 mm2. The power consumption of the chip is 9.6 mW at 1.2 V when clocked at 100 MHz, providing a peak information throughput of 1 Mbps and with an energy efficiency of 0.6 nJ per bit per iteration. To the best of our knowledge, those measurement results are from the first ever silicon implementation of a decoder for FTN signaling.

## LLR Compression for BICM Systems Using Large Constellations

- **Status**: ❌
- **Reason**: BICM 디인터리버 메모리 절감용 LLR 양자화/압축, 채널 ECC 디코더 기법 아님(통신 응용 특이적)
- **ID**: ieee:6522420
- **Type**: journal
- **Published**: July 2013
- **Authors**: S. Rosati, S. Tomasin, M. Butussi +1
- **PDF**: https://ieeexplore.ieee.org/document/6522420
- **Abstract**: Digital video broadcasting (DVB-C2) and other modern communication standards increase diversity by means of a symbol-level interleaver that spans over several codewords. De-interleaving at the receiver requires a large memory, which has a significant impact on the implementation cost. In this paper, we propose a technique that reduces the de-interleaver memory size. By quantizing log-likelihood ratios with bit-specific quantizers and compressing the quantized output, we can significantly reduce the memory size with a negligible increase in computational complexity. Both the quantizer and compressor are designed via a GMI-based maximization procedure. For a typical DVB-C2 scenario, numerical results show that the proposed solution enables a memory saving up to 30%.

## A monolithic optical front-end for soft-decision error correction decoders

- **Status**: ❌
- **Reason**: 100Gb/s 코히어런트 광통신용 soft-decision LDPC 디코더 광 프론트엔드, 떼어낼 LDPC ECC 기법 없음(아날로그 광 HW)
- **ID**: ieee:6614480
- **Type**: conference
- **Published**: 8-10 July 
- **Authors**: M. N. Sakib, M. S. Hai, O. Liboiron-Ladouceur
- **PDF**: https://ieeexplore.ieee.org/document/6614480
- **Abstract**: We investigate a monolithic optical front-end for soft-decision low-density parity-check (LDPC) decoders based on 100 Gb/s polarization division multiplexed quadrature shift keying (PM-QPSK) coherent detection.

## Audio watermarking in frequency domain using Walsh functions and LDPC codes

- **Status**: ❌
- **Reason**: 오디오 워터마킹 dirty-paper 코딩, LDPC 부수 사용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:6623477
- **Type**: conference
- **Published**: 7-9 July 2
- **Authors**: Przemyslaw Dymarski, Robert Markiewicz
- **PDF**: https://ieeexplore.ieee.org/document/6623477
- **Abstract**: An audio watermarking system, operating in logspectrum domain, using M-ary transmission codes based on Walsh functions, is presented. Plain and dirty paper coding schemes are compared. Encouraging results are obtained by using the quaternary dirty paper code and LDPC. The proposed audio watermarking algorithm is robust against MPEG-Audio compression at 96 kbps. The watermark is inaudible according to PEAQ and informal listening tests. Its bit rate, about 40 bps, makes it a useful tool for audio annotation applications.

## Spatially-coupled multi-edge type LDPC codes with bounded degrees that achieve capacity on the BEC under BP decoding

- **Status**: ❌
- **Reason**: SC-MET LDPC의 BEC 용량달성 임계포화 증명(잠재함수)으로 순수 점근 이론, 떼어낼 디코더/HW/유한길이 구성 없음
- **ID**: ieee:6620663
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Naruomi Obata, Yung-Yih Jian, Kenta Kasai +1
- **PDF**: https://ieeexplore.ieee.org/document/6620663
- **Abstract**: Convolutional (or spatially-coupled) low-density parity-check (LDPC) codes have now been shown to approach capacity for a variety of problems. Yet, most of these results require sequences of regular LDPC ensembles with increasing variable and check degrees. Previously, Kasai and Sakaniwa showed empirically that, for the BEC, this limitation can be overcome by using spatially-coupled MacKay-Neal (MN) and Hsu-Anastasopoulos (HA) ensembles. In this paper, we prove this analytically for (k, 2, 2)-MN and (2, k, 2)-HA ensembles when k is at least 3. The proof is based on the simple approach to threshold saturation, introduced by Yedla et al., which relies on potential functions. The key step is verifying the non-negativity of a potential function associated with the uncoupled system. Along the way, we derive the potential function general multi-edge type (MET) LDPC ensembles and establish a duality relationship between dual ensembles of MET LDPC codes.

## Weight distribution for non-binary cluster LDPC code ensemble

- **Status**: ❌
- **Reason**: non-binary cluster LDPC 앙상블 weight distribution 이론. 비이진 LDPC이며 순수 이론, 제외
- **ID**: ieee:6620742
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Takayuki Nozaki, Masaki Maehara, Kenta Kasai +1
- **PDF**: https://ieeexplore.ieee.org/document/6620742
- **Abstract**: In this paper, we derive the average weight distributions for the irregular non-binary cluster low-density parity-check (LDPC) code ensembles. Moreover, we give the exponential growth rate of the average weight distribution in the limit of large code length. We show that there exist (2, dc)-regular non-binary cluster LDPC code ensembles whose normalized typical minimum distances are strictly positive.

## Minimum distance distribution of irregular generalized LDPC code ensembles

- **Status**: ❌
- **Reason**: 비정칙 GLDPC 앙상블 최소거리 분포 순수 이론 - 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:6620511
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Ian P. Mulholland, Mark F. Flanagan, Enrico Paolini
- **PDF**: https://ieeexplore.ieee.org/document/6620511
- **Abstract**: In this paper, the minimum distance distribution of irregular generalized LDPC (GLDPC) code ensembles is investigated. Two classes of GLDPC code ensembles are analyzed; in one case, the Tanner graph is regular from the variable node perspective, and in the other case the Tanner graph is completely unstructured and irregular. In particular, for the former ensemble class we determine exactly which ensembles have minimum distance growing linearly with the block length with probability approaching unity with increasing block length. This work extends previous results concerning LDPC and regular GLDPC codes to the case where a hybrid mixture of check node types is used.

## Near maximum-likelihood decoding of Generalized LDPC and woven graph codes

- **Status**: ❌
- **Reason**: 비이진 LDPC 및 woven graph code 대상 near-ML 디코딩 — 비이진 제외, 짧은 control signaling 특이적
- **ID**: ieee:6620777
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Nikolay I. Makarov +1
- **PDF**: https://ieeexplore.ieee.org/document/6620777
- **Abstract**: Relations between Generalized LDPC codes, nonbinary LDPC codes, and woven graph codes are considered. Focus is on rather short codes suitable, for example, for coding control signaling information in mobile communications. In particular, codes of lengths less than 200 bits are studied. Low-complexity near maximum-likelihood (ML) decoding for these classes of codes is introduced and analyzed. Frame error rate (FER) performance of the new decoding procedure is compared with the same performance of ML and belief propagation (BP) decoding. It is shown that unlike BP decoding whose performances are mainly governed by the girth of the Tanner graph the new decoding procedure has performances which significantly depend on the minimum distance and spectrum of the woven code. Short woven graph codes with large minimum distances are tabulated.

## Asymptotic analysis of LDPC codes with depth-2 connectivity distributions over BEC

- **Status**: ❌
- **Reason**: BEC 위 depth-2 연결성 ensemble의 점근 density evolution 분석뿐, 떼어낼 디코더/HW/구성 없음
- **ID**: ieee:6620515
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Min Jang, Jin Whan Kang, Jong-Hwan Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/6620515
- **Abstract**: This paper deals with the randomness of depth-2 connectivity of LDPC ensembles. We study how the randomness of LDPC graphs affect asymptotic performance over binary erasure channel (BEC). First, a new attribute, degree-spectrum distribution, is defined to specify the connectivity of more detailed ensembles than those defined by degree distribution. With this, specified ensembles become subsets of conventional ensemble, and we develop a new density evolution method. Some extreme cases of specified ensembles are given, and we prove that the random specified ensemble is better than other regularized types.

## Anytime reliable LDPC convolutional codes for networked control over wireless channel

- **Status**: ❌
- **Reason**: networked control용 protograph LDPC convolutional의 anytime reliability/SNR bound, LDPC는 baseline·신규 구성/디코더 없음
- **ID**: ieee:6620589
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Alberto Tarable, Alessandro Nordio, Fabrizio Dabbene +1
- **PDF**: https://ieeexplore.ieee.org/document/6620589
- **Abstract**: This paper deals with the problem of stabilizing an unstable system through networked control over the wireless medium. In such a situation a remote sensor communicates the measurements to the system controller through a noisy channel. In particular, in the AWGN scenario, we show that protograph-based LDPC convolutional codes achieve anytime reliability and we also derive a lower bound to the signal-to-noise ratio required to stabilize the system. Moreover, on the Rayleigh-fading channel, we show by simulations that resorting to multiple sensors reduces the SNR required for system stabilization.

## MDPC-McEliece: New McEliece variants from Moderate Density Parity-Check codes

- **Status**: ❌
- **Reason**: MDPC-McEliece 암호 응용(보안), 채널 ECC 아님 — 제외 대상
- **ID**: ieee:6620590
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Rafael Misoczki, Jean-Pierre Tillich, Nicolas Sendrier +1
- **PDF**: https://ieeexplore.ieee.org/document/6620590
- **Abstract**: In this work, we propose two McEliece variants: one from Moderate Density Parity-Check (MDPC) codes and another from quasi-cyclic MDPC codes. MDPC codes are LDPC codes of higher density (and worse error-correction capability) than what is usually adopted for telecommunication applications. However, in cryptography we are not necessarily interested in correcting many errors, but only a number which ensures an adequate security level. By this approach, we reduce under certain hypotheses the security of the scheme to the well studied decoding problem. Furthermore, the quasi-cyclic variant provides extremely compact-keys (for 80-bits of security, public-keys have only 4801 bits).

## Tradeoffs for reliable quantum information storage in surface codes and color codes

- **Status**: ❌
- **Reason**: 표면/색 부호 양자 LDPC의 최소거리 bound 이론 - 양자 전용 개념 의존, 디코더/HW 기여 없음
- **ID**: ieee:6620360
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Nicolas Delfosse
- **PDF**: https://ieeexplore.ieee.org/document/6620360
- **Abstract**: The family of hyperbolic surface codes is one of the rare families of quantum LDPC codes with non-zero rate and unbounded minimum distance. First, we introduce a family of hyperbolic color codes. This produces a new family of quantum LDPC codes with non-zero rate and with minimum distance logarithmic in the blocklength. Second, we show that the parameters [[n, k, d]] of surface codes and color codes satisfy kd2 ≤ C(log k)2n, where C is a constant that depends only on the row weight of the parity-check matrix. Our results prove that the best asymptotic minimum distance of LDPC surface codes and color codes with non-zero rate is logarithmic in the length.

## Message passing algorithm with MAP decoding on zigzag cycles for non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC의 zigzag cycle MAP+BP 디코딩. 비이진 LDPC 제외 대상
- **ID**: ieee:6620741
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Takayuki Nozaki, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/6620741
- **Abstract**: In this paper, we propose a decoding algorithm which lowers decoding erasure rates in the error floor regions for non-binary low-density parity-check codes transmitted over the binary erasure channels. This decoding algorithm is a combination with belief propagation (BP) decoding and maximum a posteriori (MAP) decoding on zigzag cycles, which cause decoding erasures in the error floor region. We show that MAP decoding on the zigzag cycles is realized by means of a message passing algorithm. A simulation result shows that the decoding erasure rates in the error floor regions by the proposed decoding algorithm are lower than those by the BP decoder.

## Spatially-coupled precoded rateless codes

- **Status**: ❌
- **Reason**: SC-LDGM+SC-LDPC rateless 연접의 BEC 점근 오버헤드 분석, fountain/erasure 베이스라인이며 NAND 이식 ECC 기법 없음
- **ID**: ieee:6620664
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Kosuke Sakata, Kenta Kasai, Kohichi Sakaniwa
- **PDF**: https://ieeexplore.ieee.org/document/6620664
- **Abstract**: Raptor codes are rateless codes that achieve the capacity on the binary erasure channels. However the maximum degree of optimal output degree distribution is unbounded. This leads to a computational complexity problem both at encoders and decoders. Aref and Urbanke investigated the potential advantage of universal achieving-capacity property of proposed spatially-coupled (SC) low-density generator matrix (LDGM) codes. However the decoding error probability of SC-LDGM codes is bounded away from 0. In this paper, we investigate SC-LDGM codes concatenated with SC low-density parity-check codes. The proposed codes can be regarded as SC Hsu-Anastasopoulos rateless codes. We derive a lower bound of the asymptotic overhead from stability analysis for successful decoding by density evolution. The numerical calculation reveals that the lower bound is tight. We observe that with a sufficiently large number of information bits, the asymptotic overhead and the decoding error rate approach 0 with bounded maximum degree.

## Low-complexity encoding of binary quasi-cyclic codes based on Galois Fourier transform

- **Status**: ❌
- **Reason**: Galois Fourier transform 기반 인코딩(소수 e log 복잡도)으로 GF(q) 변환 의존 비이진 성격, 바이너리 NAND QC-LDPC 인코딩과 직접 이식성 약함; 애매하나 NB 변환 기법이라 제외
- **ID**: ieee:6620202
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Li Tang, Qin Huang, Zulin Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/6620202
- **Abstract**: This paper presents a novel low-complexity encoding algorithm for binary quasi-cyclic (QC) codes based on matrix transformation. First, a message vector is encoded into a transformed codeword in the transform domain. Then, the transmitted codeword is obtained from the transformed codeword by the inverse Galois Fourier transform. Moreover, a simple and fast mapping is devised to post-process the transformed codeword such that the transmitted codeword is binary as well. The complexity of our proposed encoding algorithm is less than ek(n-k)log2 e+ne(log22 e+log2 e)+ n/2 elog32 e bit operations for binary codes. This complexity is much lower than its traditional complexity 2e2(n - k)k. In the examples of encoding the binary (4095, 2016) and (15500, 10850) QC codes, the complexities are 12.09% and 9.49% of those of traditional encoding, respectively.

## Array BP-XOR codes for reliable cloud storage systems

- **Status**: ❌
- **Reason**: 클라우드 스토리지용 array BP-XOR/LT/MDS erasure 부호, fountain/erasure 코딩으로 채널 ECC 기법 아님
- **ID**: ieee:6620241
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Yongge Wang
- **PDF**: https://ieeexplore.ieee.org/document/6620241
- **Abstract**: Low Density Parity Check (LDPC) codes such as LT codes have received significant attention from both academics and industry in the past few years. By employing the underlying ideas of efficient Belief Propagation (BP) decoding process in LT codes, this paper introduces array BP-XOR codes and shows the equivalence between the edge-colored graph model and degree-one-and-two encoding symbol based array BP-XOR codes. Using this equivalence result, novel [n, n-2] and [n, 2] MDS array BP-XOR codes are designed in this paper.

## Finite length analysis on listing failure probability of Invertible Bloom Lookup Tables

- **Status**: ❌
- **Reason**: IBLT의 listing 실패확률 유한길이 분석 — peeling/stopping set 분석이나 데이터구조 응용, 채널 ECC 디코더 아님
- **ID**: ieee:6620782
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Daichi Yugawa, Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/6620782
- **Abstract**: The Invertible Bloom Lookup Tables (IBLT) is a data structure which supports insertion, deletion, retrieval and listing operations of the key-value pair. The IBLT can be used to realize efficient set reconciliation for database synchronization. The most notable feature of the IBLT is the complete listing operation of the key-value pairs based on the algorithm similar to the peeling algorithm for low-density parity check (LDPC) codes. In this paper, we will present a stopping set (SS) analysis for the IBLT which reveals finite length behaviors of the listing failure probability. The key of the analysis is enumeration of the number of stopping matrices of given size. We derived a novel recursive formula useful for computationally efficient enumeration. An upper bound on the listing failure probability based on the union bound accurately captures the error floor behaviors. It will be shown that, in the error floor region, the dominant SS have size 2. We propose a simple modification on hash functions, which are called SS avoiding hash functions, for preventing occurrences of the SS of size 2.

## Constructions of quasi-cyclic measurement matrices based on array codes

- **Status**: ❌
- **Reason**: 어레이 LDPC 패리티검사를 압축센싱 측정행렬로 사용하는 소스 코딩 응용 - 채널 ECC 디코더/HW/코드설계 신규 기여 아님
- **ID**: ieee:6620272
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xin-Ji Liu, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/6620272
- **Abstract**: Recently, Dimakis, Smarandache, and Vontobel indicated that the parity-check matrices of good LDPC codes can be used as provably good measurement matrices for compressed sensing (CS) under basis pursuit (BP). In this paper, we consider the parity-check matrix H(r, q) of the array codes, one of the most important kind of structured LDPC codes. The spark, i.e. the smallest number of linearly dependent columns in a matrix, of H(2, q) and H(3, q) are determined and two lower bounds of the sparks of H(r, q) are given for r ≥ 4. Moreover, we carry out numbers of simulations and show that many parity-check matrices of array codes and their submatrices perform better than the corresponding Gaussian random matrices. The proposed measurement matrices have perfect quasi-cyclic structures and can make the hardware realization convenient and easy, thus having great potentials in practice.

## Reconstruction guarantee analysis of binary measurement matrices based on girth

- **Status**: ❌
- **Reason**: 압축센싱 측정행렬의 girth 복원보장 순수 이론 분석, 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:6620271
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xin-Ji Liu, Shu-Tao Xia
- **PDF**: https://ieeexplore.ieee.org/document/6620271
- **Abstract**: Binary 0-1 measurement matrices, especially those from coding theory, were introduced to compressed sensing (CS) recently. Good measurement matrices with preferred properties, e.g., the restricted isometry property (RIP) and nullspace property (NSP), have no known general ways to be efficiently checked. Khajehnejad et al. made use of girth to certify the good performances of sparse binary measurement matrices. In this paper, we examine the performance of binary measurement matrices with uniform column weight and arbitrary girth under basis pursuit. Explicit sufficient conditions of exact reconstruction are obtained, which improve the previous results derived from RIP for any girth g and results from NSP when g/2 is odd. Moreover, we derive explicit l1/l1, l2/l1 and l∞/l1 sparse approximation guarantees. These results further show that large girth has positive impacts on the performance of binary measurement matrices under basis pursuit, and the binary parity-check matrices of good LDPC codes are important candidates of measurement matrices.

## Performance bounds for spatially-coupled LDPC codes over the block erasure channel

- **Status**: ❌
- **Reason**: block erasure channel에서 SC-LDPC 성능의 단순 상하한 bound뿐, 이식 기법 없음
- **ID**: ieee:6620552
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Alan Julé, Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/6620552
- **Abstract**: The paper provides simple lower and upper bounds on block PB and bit Pb performances of spatially-coupled LDPC (SC-LDPC) codes over a particular model of the block erasure channel. As expected, the spatial coupling structure helps in the correction of bursty erasures, and the decoding performance of SC-LDPC codes improves if the coupling parameter w increases.

## A family of quantum codes with performances close to the hashing bound under iterative decoding

- **Status**: ❌
- **Reason**: 공간결합 양자 LDPC + 양자 터보부호 결합 - 양자 EC 전용, 고전 바이너리 LDPC 이식 기법 없음
- **ID**: ieee:6620358
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Denise Maurice, Jean-Pierre Tillich, Iryna Andriyanova
- **PDF**: https://ieeexplore.ieee.org/document/6620358
- **Abstract**: We propose here a new construction of quantum codes combining an improved version of a family of spatially coupled quantum LDPC codes, suggested in [1], with a family of error reducing turbo-codes of [2]. This new construction displays outstanding performances under iterative decoding for noise levels very close to the hashing bound, without needing qubits, protected from noise as in [1].

## Approaching multiple-access channel capacity by nonbinary coding-spreading

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 기반 coding-spreading MAC 기법. 비이진 LDPC는 제외 대상
- **ID**: ieee:6620740
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Yuta Tsujii, Guanghui Song, Jun Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/6620740
- **Abstract**: As a generalization of the binary coding-spreading scheme, nonbinary coding-spreading scheme is proposed for a synchronous binary-input multiple-access channel (MAC) with Gaussian noise, equal-power, and equal-rate users. In this scheme, each user employs the same nonbinary low-density parity-check code serially concatenated with a nonbinary low-rate mapping, referred to as nonbinary spreading. A user-specific interleaving is employed to make the transmitted data of each user random-like. It is shown that the iterative multi-user decoding threshold of nonbinary coding-spreading scheme is less than 0.5 dB away from the MAC capacity at many sum rates.

## Comparison of belief propagation and iterative threshold decoding based on dynamical systems

- **Status**: ❌
- **Reason**: 컨볼루셔널 부호용 iterative threshold decoding과 BP를 동역학계로 비교한 이론. 바이너리 LDPC에 이식할 신규 디코더/구성 없음
- **ID**: ieee:6620775
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Mohamad Mostafa, Werner G. Teich, Jürgen Lindner
- **PDF**: https://ieeexplore.ieee.org/document/6620775
- **Abstract**: For a special class of convolutional codes, iterative threshold decoding (ITD) has been shown by simulations to achieve the same error rate performance as belief propagation (BP). In order to get a better understanding of these iterative decoding algorithms, we describe ITD and BP as discrete-time dynamical systems. Based on the theory of dynamical systems, we compare the dynamical behavior of ITD and BP. For the special case of a linear dynamical system, the behavior can be completely characterized. In this case we show that the fixed points of both ITD and BP are globally stable but they do not coincide. The analysis is extended to the case of a continuous-time dynamical system, which represents an important step for modeling analog iterative decoders.

## Extending Divsalar's bound to nonbinary codes with two dimensional constellations

- **Status**: ❌
- **Reason**: 비이진 부호 2D 성상도 오류확률 상한(Divsalar bound 확장) — 비이진 + 순수 이론 bound, 떼어낼 디코더/HW 없음
- **ID**: ieee:6620780
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/6620780
- **Abstract**: Closed form upper bounds to error probabilities of nonbinary coded systems with two and higher dimensional constellation over the additive white Gaussian noise channel are derived. Computation of these bounds do not require integrations nor parameter optimizations. These bounds are the extension of bounds derived by Divsalar in 1999 for binary codes with binary modulations. The proposed bounds require only the knowledge of the average pairwise Euclidean distance enumerator of the code words when certain symmetry conditions do not hold. The bounds are tight for large block lengths. We also briefly discuss how to extend the pairwise Euclidean distance enumerators to ensembles of nonbinary protograph codes using the notion of frequency weight enumerators.

## Obtaining extra coding gain for short codes by block Markov superposition transmission

- **Status**: ❌
- **Reason**: Hamming 짧은 부호의 block Markov superposition 전송(비-LDPC), sliding-window 디코딩은 LDPC BP 비이식
- **ID**: ieee:6620587
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xiao Ma, Chulong Liang, Kechao Huang +1
- **PDF**: https://ieeexplore.ieee.org/document/6620587
- **Abstract**: In this paper, we present a new approach, called block Markov superposition transmission (BMST), to construct from short codes a class of convolutional codes with large constraint length. The BMST is very similar to superposition block Markov encoding (SBME), which has been widely used to prove multiuser coding theorems. We also present an iterative sliding-window decoding algorithm for the proposed transmission scheme. The extra coding gain obtained by BMST can be bounded in terms of the Markov order and with the help of the input-output weight enumerating function (IOWEF) of the BMST system, which can be computed from that of the short code by performing a trellis-based algorithm. Numerical results verify our analysis and show that an extra coding gain of 6.4 dB at bit-error rate (BER) 10-5 can be obtained by BMST of the [7, 4] Hamming code.

## The capacity of adaptive group testing

- **Status**: ❌
- **Reason**: group testing 용량 정보이론 한계, ECC 디코더/구성과 무관
- **ID**: ieee:6620712
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Leonardo Baldassini, Oliver Johnson, Matthew Aldridge
- **PDF**: https://ieeexplore.ieee.org/document/6620712
- **Abstract**: We define capacity for group testing problems and deduce bounds for the capacity of a variety of noisy models, based on the capacity of equivalent noisy communication channels. For noiseless adaptive group testing we prove an information-theoretic lower bound which tightens a bound of Chan et al. This can be combined with a performance analysis of a version of Hwang's adaptive group testing algorithm, in order to deduce the capacity of noiseless and erasure group testing models.

## Polarization of quasi-static fading channels

- **Status**: ❌
- **Reason**: polar 부호의 블록 페이딩 채널 극화 분석 - 비-LDPC, 부호 비의존 이식 디코더 기법 없음
- **ID**: ieee:6620330
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Joseph J. Boutros, Ezio Biglieri
- **PDF**: https://ieeexplore.ieee.org/document/6620330
- **Abstract**: This work investigates polar coding for block-fading channels. We show that polarization does occur at infinity for three types of channel multiplexers. Nevertheless, the polarization process is not unique, as it is shaped by the choice of the multiplexer. The fading-plane approach is used to study the outage behavior of polar coding at a fixed transmission rate. Two types of multiplexers are shown to provide full diversity at finite and infinite code length.

## An analysis on non-adaptive group testing based on sparse pooling graphs

- **Status**: ❌
- **Reason**: 비적응 그룹테스팅의 sparse pooling graph 정보이론 분석. 채널 ECC가 아닌 그룹테스팅 추정, 떼어낼 디코더/HW/코드설계 없음
- **ID**: ieee:6620713
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Tadashi Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/6620713
- **Abstract**: In this paper, an information theoretic analysis on non-adaptive group testing schemes based on sparse pooling graphs is presented. The binary status of the objects to be tested are modeled by i.i.d. Bernoulli random variables with probability p. An (l, r, n)-regular pooling graph is a bipartite graph with left node degree l and right node degree r, where n is the number of left nodes. Two scenarios are considered: a noiseless setting and a noisy one. The main contributions of this paper are direct part theorems that give conditions for the existence of an estimator achieving arbitrary small estimation error probability. The direct part theorems are proved by averaging an upper bound on estimation error probability of the typical set estimator over an (l, r, n)-regular pooling graph ensemble. Numerical results indicate sharp threshold behaviors in the asymptotic regime.

## A coding approach to guarantee information integrity against a Byzantine relay

- **Status**: ❌
- **Reason**: Byzantine relay 정보무결성 보장 랜덤코딩 capacity 분석. 보안/네트워크코딩 이론, LDPC ECC 무관
- **ID**: ieee:6620732
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Eric Graves, Tan F. Wong
- **PDF**: https://ieeexplore.ieee.org/document/6620732
- **Abstract**: This paper presents a random coding scheme with which two nodes can exchange information with guaranteed integrity over a two-way Byzantine relay. This coding scheme is employed to obtain an inner bound on the capacity region with information integrity. No pre-shared secret or secret transmission is needed for the proposed scheme. Hence the inner bound obtained is generally larger than those achieved based on secret transmission schemes. This approach advocates the separation of supporting information integrity and secrecy.

## Synchronization from insertions and deletions under a non-binary, non-uniform source

- **Status**: ❌
- **Reason**: non-binary non-uniform 소스 파일 동기화(insertion/deletion). 동기화 프로토콜, 채널 ECC 아님
- **ID**: ieee:6620762
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Nicolas Bitouzé, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6620762
- **Abstract**: We study the problem of synchronizing two files X and Y at two distant nodes A and B that are connected through a two-way communication channel. We assume that file Y at node B is obtained from file X at node A by inserting and deleting a small fraction of symbols in X. More specifically, we consider the case where X is a non-binary non-uniform string, and deletions and insertions happen uniformly with rates βd and βi, respectively. We propose a synchronization protocol between node A and node B that needs to transmit O(q/H2(βd+βi)n log 1/βd+βi) bits (where n is the length of X, q is the alphabet size and H2 is the collision entropy of X) and reconstructs X at node B with error probability exponentially low in n. This protocol readily generalizes the recent result by Tabatabaei Yazdi and Dolecek that dealt with synchronization from binary uniform source and under only deletion errors.

## Soft-encoding distributed coding for parallel relay systems

- **Status**: ❌
- **Reason**: 병렬 릴레이용 soft convolutional 분산코딩(range-limited LLR). 비-LDPC(컨볼루셔널) 릴레이 응용, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:6620747
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Xuanxuan Lu, Jing Li Tiffany, Yang Liu
- **PDF**: https://ieeexplore.ieee.org/document/6620747
- **Abstract**: In the paper, a new distributed coding scheme for parallel relay systems is proposed, in which a sender communicates to a destination that is two hops away via two (or more) parallel relays. The key idea is the exploitation of a (rate-1) soft convolutional encoder at each of the parallel relays, to collaboratively form a simple but powerful distributed analog coding scheme to achieve efficient forwarding of soft reliability messages. We detail the encoding and decoding process of the proposed soft-encoding distributed coding. As the input of the encoder would affect the overall performance, we analyze what form of messages at the relay is most appropriate to be forwarded to the destination. The range-limited log likelihood ratio (range-limited LLR) is chosen as the input. The optimality of the range-limited LLRs as the best form of relaying messages is verified by the simulation results. Our new distributed coding scheme can obviously outperform the existing ones.

## Approaching the rate-distortion limit by spatial coupling with belief propagation and decimation

- **Status**: ❌
- **Reason**: 공간결합 LDGM 기반 lossy 압축(rate-distortion) - 소스 코딩이지 채널 ECC 아님
- **ID**: ieee:6620412
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Vahid Aref, Nicolas Macris, Marc Vuffray
- **PDF**: https://ieeexplore.ieee.org/document/6620412
- **Abstract**: We investigate an encoding scheme for lossy compression based on spatially coupled Low-Density GeneratorMatrix codes. The degree distributions are regular, or are Poisson on the code-bit side and check-regular which allows use for any compression rate. The performance of a low complexity Belief Propagation Guided Decimation algorithm is excellent, and for large check degrees it gets close to Shannon's rate-distortion limit. We investigate links between the algorithmic performance and the phase diagram of a relevant random Gibbs measure. The associated dynamical and condensation thresholds are computed within the framework of the cavity method. We observe that: (i) the dynamical threshold of the spatially coupled construction saturates towards the condensation threshold; (ii) for large degrees the condensation threshold approaches the information theoretic test-channel parameter of rate-distortion theory. This provides heuristic insight into the excellent performance of the BPGD algorithm.

## Reliability-based error detection for feedback communication with low latency

- **Status**: ❌
- **Reason**: VLF 피드백 통신 ROVA 기반 정지기준, Viterbi/CRC 대상이며 LDPC ECC 기법 아님
- **ID**: ieee:6620687
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Adam R. Williamson, Tsung-Yi Chen, Richard D. Wesel
- **PDF**: https://ieeexplore.ieee.org/document/6620687
- **Abstract**: This paper presents a reliability-based decoding scheme for variable-length coding with feedback and demonstrates via simulation that it can achieve higher rates than Polyanskiy et al.'s random coding lower bound for variable-length feedback (VLF) coding on both the BSC and AWGN channel. The proposed scheme uses the reliability output Viterbi algorithm (ROVA) to compute the word error probability after each decoding attempt, which is compared against a target error threshold and used as a stopping criterion to terminate transmission. The only feedback required is a single bit for each decoding attempt, informing the transmitter whether the ROVA-computed word-error probability is sufficiently low. Furthermore, the ROVA determines whether transmission/decoding may be terminated without the need for a rate-reducing CRC.

## A reduced-complexity multilevel coded modulation for APSK signaling

- **Status**: ❌
- **Reason**: APSK 위성용 MLC/labeling 변조 기법, LDPC ECC 이식 기법 아님
- **ID**: ieee:6620575
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Daiki Yoda, Hideki Ochiai
- **PDF**: https://ieeexplore.ieee.org/document/6620575
- **Abstract**: The amplitude and phase shift keying (APSK) signal has been adopted in the recent satellite communication standards such as DVB-S2 due to its peak-to-average power ratio (PAPR) property lower than the quadrature amplitude modulation (QAM). Unlike square QAM constellations that allow separate detection of in-phase and quadrature components (i.e., I-Q decomposition), the detection process for APSK is generally complex. This paper investigates the use of multilevel coding (MLC) together with multistage decoding (MSD) for APSK with particular emphasis on an introduction of a novel labeling that allows I-Q decomposition at the highest level, thereby significantly reducing the decoding complexity at the cost of slight performance degradation.

## In-memory computing of Akers logic array

- **Status**: ❌
- **Reason**: in-memory computing/Akers 논리배열, 비이진 알파벳 일반화로 ECC 디코더·코드설계 기법 없음
- **ID**: ieee:6620650
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Eitan Yaakobi, Anxiao Andrew Jiang, Jehoshua Bruck
- **PDF**: https://ieeexplore.ieee.org/document/6620650
- **Abstract**: This work studies memories with the goal of exploring the concept of in-memory computing. Our point of departure is the 1972 classical study on logical arrays by Akers. We demonstrate a number of new ways for these arrays to simultaneously store information and perform logical operations. We first generalize these arrays to non-binary alphabets. We then show how a special structure of these arrays can both store values and output a sorted version of them. In addition we show how the array can tolerate or detect errors in the stored information.

## Coded splitting tree protocols

- **Status**: ❌
- **Reason**: coded splitting tree 다중접속제어 프로토콜(SIC+BP). MAC 프로토콜 응용, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6620748
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Jesper H. Sørensen, Čedomir Stefanović, Petar Popovski
- **PDF**: https://ieeexplore.ieee.org/document/6620748
- **Abstract**: This paper presents a novel approach to multiple access control called coded splitting tree protocol. The approach builds on the known tree splitting protocols, code structure and successive interference cancellation (SIC). Several instances of the tree splitting protocol are initiated, each instance is terminated prematurely and subsequently iterated. The combined set of leaves from all the tree instances can then be viewed as a graph code, which is decodable using belief propagation. The main design problem is determining the order of splitting, which enables successful decoding as early as possible. Evaluations show that the proposed protocol provides considerable gains over the standard tree splitting protocol applying SIC. The improvement comes at the expense of an increased feedback and receiver complexity.

## Scalar Quantize-and-Forward for symmetric half-duplex Two-Way Relay Channels

- **Status**: ❌
- **Reason**: 양방향 릴레이 채널의 스칼라 Quantize-and-Forward 통신 응용 - 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:6620441
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Michael Heindlmaier, Onurcan Işcan, Christopher Rosanka
- **PDF**: https://ieeexplore.ieee.org/document/6620441
- **Abstract**: Scalar Quantize & Forward (QF) schemes are studied for the Two-Way Relay Channel. Different QF approaches are compared in terms of rates as well as relay and decoder complexity. A coding scheme not requiring Slepian-Wolf coding at the relay is proposed and properties of the corresponding sum-rate optimization problem are presented. An iterative numerical scheme is derived that guides optimized quantizer design. The results are supported by simulations.

## The space of solutions of coupled XORSAT formulae

- **Status**: ❌
- **Reason**: coupled XORSAT 해공간의 기하학적 전이 분석, 순수 이론으로 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:6620667
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: S. Hamed Hassani, Nicolas Macris, Rudiger Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6620667
- **Abstract**: The XOR-satisfiability (XORSAT) problem deals with a system of n Boolean variables and m clauses. Each clause is a linear Boolean equation (XOR) of a subset of the variables. A K-clause is a clause involving K distinct variables. In the random K-XORSAT problem a formula is created by choosing m K-clauses uniformly at random from the set of all possible clauses on n variables. The set of solutions of a random formula exhibits various geometrical transitions as the ratio m/n varies. We consider a coupled K-XORSAT ensemble, consisting of a chain of random XORSAT models that are spatially coupled across a finite window along the chain direction. We observe that the threshold saturation phenomenon takes place for this ensemble and we characterize various properties of the space of solutions of such coupled formulae.

## Extended subspace error localization for rate-adaptive distributed source coding

- **Status**: ❌
- **Reason**: DFT 부호 기반 분산 소스코딩의 subspace error localization, 채널 LDPC ECC 아님
- **ID**: ieee:6620611
- **Type**: conference
- **Published**: 7-12 July 
- **Authors**: Mojtaba Vaezi, Fabrice Labeau
- **PDF**: https://ieeexplore.ieee.org/document/6620611
- **Abstract**: A subspace-based approach for rate-adaptive distributed source coding (DSC) based on discrete Fourier transform (DFT) codes is developed. Punctured DFT codes can be used to implement rate-adaptive source coding, however they perform poorly after even moderate puncturing since the performance of the subspace error localization degrades severely. The proposed subspace-based error localization extends and improves the existing one, based on additional syndrome, and is naturally suitable for rate-adaptive distributed source coding architecture.

## Improving the efficiency of the LDPC code-based McEliece cryptosystem through irregular codes

- **Status**: ❌
- **Reason**: LDPC 기반 McEliece 암호시스템 — 보안/암호 응용, 원칙 제외(코드 비밀성 활용, 채널 ECC 기법 이식 불가)
- **ID**: ieee:6754945
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Marco Baldi, Marco Bianchi, Nicola Maturo +1
- **PDF**: https://ieeexplore.ieee.org/document/6754945
- **Abstract**: We consider the framework of the McEliece cryptosystem based on low-density parity-check (LDPC) codes, which is a promising post-quantum alternative to classical public key cryptosystems. The use of LDPC codes in this context allows to achieve good security levels with very compact keys, which is an important advantage over the classical McEliece cryptosystem based on Goppa codes. However, only regular LDPC codes have been considered up to now, while some further improvement can be achieved by using irregular LDPC codes, which are known to achieve better error correction performance than regular LDPC codes. This is shown in this paper, for the first time at our knowledge. The possible use of irregular transformation matrices is also investigated, which further increases the efficiency of the system, especially in regard to the public key size.

## A practical viewpoint on the performance of LDPC codes over the fast Rayleigh fading wire-tap channel

- **Status**: ❌
- **Reason**: wire-tap 채널 LDPC 보안 성능 평가 — 물리계층 보안 응용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:6754961
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Marco Baldi, Marco Bianchi, Nicola Maturo +1
- **PDF**: https://ieeexplore.ieee.org/document/6754961
- **Abstract**: In this paper, we carry out a practical assessment of the performance of finite-length LDPC codes over the wiretap channel with fast Rayleigh fading. Classical metrics for physical layer security, like the secrecy capacity, are based on information theoretic arguments, and provide the ultimate security bounds for these schemes. However, it is difficult to design practical schemes, using some specific finite-length code, able to approach such a performance. Then we use a more practical metric, based on the error probability, which allows assessing the performance achieved in terms of both reliability and security over the fast Rayleigh fading wire-tap channel.

## Recovering erroneous data bits using error estimating code

- **Status**: ❌
- **Reason**: 비-LDPC(EEC/Hamming 기반) 무선 패킷 오류추정·flipping 복구 — LDPC 아니고 부호 비의존 BP 이식 기법 없음
- **ID**: ieee:6755031
- **Type**: conference
- **Published**: 7-10 July 
- **Authors**: Xingshen Wei, Wenzhong Li, Xiaoliang Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/6755031
- **Abstract**: Error correction techniques play an important role to guarantee reliable communication in wireless networks. The widely used error-correcting codes (ECCs) such as Hamming code introduce the benefit of error correction without retransmitting the data packet, but they suffer from high redundancy and communication overhead. In the recent years, error estimating code (EEC) was proposed to estimate the bit-error-rate (BER) of a packet efficiently with very low data redundancy. However, the ability of error correction using EEC remains unexplored. In this paper, we argue that EEC can be used to recover erroneous bits from the data packet. To show the capacity of error recovery with EEC, we propose an error correction scheme based on the parity check information provided by the EEC bits. We first introduce a filtering algorithm to rule out the correct data bits and obtain a set of suspicious bits containing most of the errors. Then we apply a polynomial randomized algorithm called Rand_flipping to examine the suspicious bits and flip the most promising erroneous bits aiming to minimize the total numbers of errors in the packet. Theoretical analysis proves that under some constraints the proposed Rand_flipping algorithm can correct most of the erroneous bits with probability higher than 1-1/e. Extensive experiments based on a real WiFi trace are conducted, which shows that the proposed algorithm corrects over 80% erroneous bits of the trace in practice.

## Joint detection-decoding of majority-logic decodable nonbinary LDPC coded modulation systems: An iterative noise reduction algorithm

- **Status**: ❌
- **Reason**: nonbinary LDPC majority-logic 결합 검출-복호 — 비이진 LDPC 제외 대상
- **ID**: ieee:6625372
- **Type**: conference
- **Published**: 6-10 July 
- **Authors**: Shancheng Zhao, Xuepeng Wang, Teng Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/6625372
- **Abstract**: In this paper, we present a low-complexity iterative joint detection-decoding algorithm for majority-logic decodable nonbinary LDPC coded modulation systems. In the proposed algorithm, a hard-in-hard-out decoder is combined with a hard-decision signal detector in an iterative manner. Each iteration consists of five phases. Firstly, the detector makes hard decisions based on the iteratively updated “received” signals; secondly, these hard-decisions are distributed via variable nodes to check nodes; thirdly, check nodes compute hard extrinsic messages; fourthly, each variable node counts hard extrinsic messages from its adjacent check nodes and feeds back to the detection node the symbol with the most votes as well as the difference between the most votes and the second most votes; finally, these feedbacks are used to shift each “received” signal point along an estimated direction to possibly reduce noise. The proposed algorithm requires only integer operations and finite field operations. Simulation results show that the proposed algorithm performs well and hence serves as an attractive candidate to decode majority-logic decodable nonbinary LDPC codes.

## A low-complexity joint noncoherent demodulation/decoding algorithm for nonbinary LDPC-coded differential modulation systems

- **Status**: ❌
- **Reason**: q-ary(비이진 GF(q)) LDPC 비동기 demod/decode — 비이진 LDPC 제외 대상
- **ID**: ieee:6625370
- **Type**: conference
- **Published**: 6-10 July 
- **Authors**: Minghua Li, Rongting Chen, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/6625370
- **Abstract**: In this paper, we apply q-ary LDPC codes to differential modulation systems, and study the design and performance of the resultant coded modulation systems. A low-complexity joint detection/decoding method for noncoherent demodulation is proposed, in which the hard-message-passing strategy is used for a joint factor graph. It combines trellis-based differential detection aided with channel prediction and the reliability-based decoding of nonbinary LDPC codes introduced in [1]. The Max-Log-MAP algorithm with soft-in hard-out is used for the differential detection. Simulation results show that the proposed method can offer good performances with a greatly reduced complexity.

## On the pragmatic turbo equalizer for optical communications

- **Status**: ❌
- **Reason**: 광통신용 pragmatic turbo equalizer - 비-LDPC, 등화기 기법으로 LDPC BP 이식성 없음
- **ID**: ieee:6597485
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Yequn Zhang, Shaoliang Zhang, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6597485
- **Abstract**: Two types of pragmatic turbo equalizers are implemented and evaluated with either histogram approach or multivariate Gaussian approximation. The latter is found to be more suitable due to its low complexity and less performance degradation.

## Performance improvement of a triple-concatenated FEC by a UEP-BCH product code for 100 Gb/s optical transport networks

- **Status**: ❌
- **Reason**: UEP-BCH product code 기반 concatenated FEC - 비-LDPC 부호, 이식 가능 LDPC 기법 없음
- **ID**: ieee:6597483
- **Type**: conference
- **Published**: 30 June-4 
- **Authors**: Yoshikuni Miyata, Kazuo Kubo, Kenya Sugihara +4
- **PDF**: https://ieeexplore.ieee.org/document/6597483
- **Abstract**: We present an error-correction performance improvement of a triple-concatenated FEC by a UEP-BCH product code for OTU4V frame format. A simulation indicates an NCG of 11.0dB with 20.5% redundancy at a post-FEC BER of 10-15.

## Design, analysis and FPGA implementation LDPC codes with BCH codes

- **Status**: ❌
- **Reason**: LDPC vs BCH FPGA 면적/전력 비교만, 새 디코더·구성·HW 기여 없는 무선 표준 단순 비교
- **ID**: ieee:6675957
- **Type**: conference
- **Published**: 3-3 July 2
- **Authors**: R. Muthammal, S. Srinivasa Rao Madhane
- **PDF**: https://ieeexplore.ieee.org/document/6675957
- **Abstract**: In this work, a analysis is performed between LDPC and BCH codes, the BCH codes[1] and LDPC codes both being an error correcting codes that can be used in wireless standards, by implementing these two error correcting codes in FPGA we analyze the Architectures of Error correcting codes in order to show that LDPC is having low area and less power than BCH codes.

## LDPC-coded A×M-DAPPM systems for simulation of turbulent free-space optical communication system

- **Status**: ❌
- **Reason**: FSO 광통신용 LDPC-DAPPM 응용 BER 시뮬레이션, 표준 LDPC 사용·떼어낼 신규 기법 없음
- **ID**: ieee:6617177
- **Type**: conference
- **Published**: 26-28 July
- **Authors**: Kaimin Wang, Qi Zhang, Yongjun Wang +5
- **PDF**: https://ieeexplore.ieee.org/document/6617177
- **Abstract**: A LDPC coded DAPPM (4×4 & 4×8) modulated scheme for both strong and weak turbulent free-space optical communication is proposed and its BER performance is analyzed by Monte Carlo simulation. Results prove its well reliability especially for weak turbulent channel, and calls for advanced forward error control means to deal with strong turbulent channel.

## Performance evaluation of LDPC coded MIMO transceiver with equalization

- **Status**: ❌
- **Reason**: LDPC 코딩 MIMO 송수신/이퀄라이저 무선 응용 성능평가, 표준 LDPC·떼어낼 디코더 기법 없음
- **ID**: ieee:6844196
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: T. Deepa, R. Kumar
- **PDF**: https://ieeexplore.ieee.org/document/6844196
- **Abstract**: A Multiple Input, Multiple Output (MIMO) system has multiple antennas and multiple radios. In MIMO systems, data will arrive at the receiver at different times through different paths to improve the quality of the data link. MIMO technology has attracted attention in radio communications, because it offers significant increases in data throughput and link range without additional bandwidth or increased transmit power. In the MIMO system, forward error correction coding is essential for high data rate communications. Recently, low-density parity-check (LDPC) codes have attracted much attention as good error correcting codes. In this paper, we propose a new LDPC coded MIMO system with equalization such as minimum mean square error (MMSE) and maximum likelihood detectors (MLD). Simulation result show that the coded MIMO system with MLD can achieve the good error rate performance comparing to coded MIMO system with MMSE.

## Optimizing of iterative turbo equalizer for underwater acoustic channel

- **Status**: ❌
- **Reason**: 수중음향 채널 turbo equalizer 최적화, turbo가 최적이라 결론 — LDPC는 부수 언급, 떼어낼 기법 없음
- **ID**: ieee:6614774
- **Type**: conference
- **Published**: 2-5 July 2
- **Authors**: Hae-chan Kwon, Gun-yeol Park, Ki-man Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/6614774
- **Abstract**: Underwater acoustic communications have multipath errors because of reflection by sea-level and sea-bottom. The multipath of underwater channel causes signal distortion and error floor. In order to improve the performance, it is necessary to employ an iterative coding scheme. Among the iterative coding schemes, turbo codes and LDPC codes are dominant channel coding schemes in recent. This paper concluded that turbo coding scheme is optimal one for underwater communications system in aspect to performance, coded word length, and equalization applications. Also, we confirmed that iterative equalization using soft information from the turbo decoder further enhances the receiver performance in the environment of oceanic experimentation with distance of 5Km and data rate of 1Kbps.

## Security of Biometrics Using Multimodal Approach

- **Status**: ❌
- **Reason**: 바이오메트릭 iris 템플릿 보안에 LDPC channel coding 적용 — 보안 응용, 채널 ECC 아님
- **ID**: ieee:6597679
- **Type**: conference
- **Published**: 2-5 July 2
- **Authors**: Abdulhaseeb Ahmed, Hafiz Malik
- **PDF**: https://ieeexplore.ieee.org/document/6597679
- **Abstract**: Biometric based access control systems (BACS) are widely used for robust and reliable identity verification, but these systems also raise some serious privacy concerns. The biometric templates, used for access control process, are stored in the system database which is vulnerable to variety of attacks. This paper presents a two stage solution for securing human iris templates used for BACS. The proposed method first models the fuzziness of iris template bits, which is used to select a set of stable template bits. Channel coding based on low density parity check coding is then applied to the selected stable bits to protect template against adversary attacks. To enhance the security of the proposed method further, both human irises are used for the access control process. Security performance of the developed algorithm is evaluated using publicly available CASIA database. Simulation results show that the proposed method provides stronger computational security than existing iris template security methods.

## Subchannel ordering scheme for LDPC-coded OFDM transmission over selective channels

- **Status**: ❌
- **Reason**: OFDM 서브채널 순서화 기법으로 비이진 GF(q) LDPC 사용. 비이진 LDPC + 무선 응용 특이적이라 제외.
- **ID**: ieee:6613893
- **Type**: conference
- **Published**: 2-4 July 2
- **Authors**: Grzegorz Dziwoki, Wojciech Sulek
- **PDF**: https://ieeexplore.ieee.org/document/6613893
- **Abstract**: OFDM modulation seems to be a good choice to deal with highly distorted transmission channels, and LDPC error correction codes allow the system performance to get close to the Shannon capacity. Performance improvement of the LDPC-coded OFDM system can be accomplished by use of irregular binary LDPC codes along with an appropriate match between the bits of the codeword and the OFDM subchannels. Non-binary LDPC codes over high order finite fields GF(q) are an additional booster in case of short to moderate codeword lengths. In this paper, a simple practical method of the subchannel ordering for OFDM modulation with non-binary LDPC codes is proposed. The method exploits some special structural properties of the LDPC code parity check matrix generated based on the PEG (Progressive-Edge-Growth) algorithm. A noticeable improvement was achieved for regular codes when the column weights of the parity check matrix is equal to 2.

## Incremental relaying protocols for extended LDPC coded cooperative diversity

- **Status**: ❌
- **Reason**: LDPC 협력다이버시티 증분중계 프로토콜; LDPC 베이스라인, 떼어낼 디코더·구성·HW 기법 없음
- **ID**: ieee:6583706
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Hussain Ali, Maan Kousa
- **PDF**: https://ieeexplore.ieee.org/document/6583706
- **Abstract**: Cooperative diversity achieves the diversity gain without adding physical antennas to the users or mobile stations. Coded cooperative diversity improves the frame-error-rate (FER) performance. The throughput of coded cooperative diversity can be enhanced by incremental relaying protocols which utilize limited feedback from the destination. In this work, we present two feedback-based protocols for extended low-density parity-check (LDPC) coded cooperative diversity framework.

## ARQ-based scheme for coded wireless cooperative communications

- **Status**: ❌
- **Reason**: ARQ 기반 LDPC 협력통신; LDPC는 베이스라인일 뿐 떼어낼 신규 디코더·구성·HW 기법 없음 (무선응용 특이)
- **ID**: ieee:6583585
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Ahmad Suhail Salim, Hussain Ali, Maan Kousa
- **PDF**: https://ieeexplore.ieee.org/document/6583585
- **Abstract**: Cooperative communications have received an increasing attention in the last few years due to the spread of wireless devices. While multi-antenna systems can improve the system performance greatly, it is difficult to implement antenna arrays on hand-held devices due to size, cost and hardware limitation. Cooperation allows the users to share their single-antenna devices to create a virtual multi-antenna system that benefits from the transmit diversity. On the other hand, low density parity check (LDPC) code is a class of linear block codes that can theoretically approach the Shannon limit. In this work, we propose an automatic-repeat-request (ARQ)-based LDPC coded cooperative system that provides an improvement in both error rate and throughput.

## A cooperative network coding approach to reliable Wireless Body Area Networks with demodulate-and-forward

- **Status**: ❌
- **Reason**: WBAN용 XOR 네트워크 코딩; LDPC ECC와 무관, 떼어낼 기법 없음
- **ID**: ieee:6583591
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Samaneh Movassaghi, Mahyar Shirvanimoghaddam, Mehran Abolhasan
- **PDF**: https://ieeexplore.ieee.org/document/6583591
- **Abstract**: In this paper, a novel cooperative transmission scheme via network coding has been proposed for Wireless Body Area Networks (WBANs) to enhance reliability and throughput. In the proposed scheme, namely Random XOR Network Coding (RXNC), each relay demodulates the received signal from each sensor node and then selects d different coded symbols amongst them and XORs them to generate a network coded symbol. We have found the optimum value of d through an analytical approach by minimizing the probability that an XOR network coded symbol is incorrectly generated. Simulation results show that the proposed RXNC scheme outperforms the no-cooperation and conventional bitwise network coding schemes in all channel signal to noise ratios (SNRs) from 0 dB to 18 dB.

## Blind phase estimation algorithm for trellis coded modulation over both AWGN and Rayleigh flat fading channels

- **Status**: ❌
- **Reason**: TCM 블라인드 위상추정; LDPC 무관 비-LDPC 부호
- **ID**: ieee:6583619
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Emna Ben Slimane, Slaheddine Jarboui, Ammar Bouallegue
- **PDF**: https://ieeexplore.ieee.org/document/6583619
- **Abstract**: Carrier phase offset is known as a serious drawback for trellis coded M-PSK systems. In this paper, we investigate the sensitivity of the 8-PSK- trellis coded modulation (8-PSK-TCM) to carrier phase offset over both additive white Gaussian noise (AWGN) and Rayleigh flat fading channels. Then, we design a reliable low complexity blind carrier phase recovery algorithm suited for general TCM schemes. The proposed estimation technique is based on a recursive phase metric that exhibits an absolute minimum at the carrier phase offset. Simulation results show the efficiency of the proposed non-data-aided (NDA) estimation technique for both AWGN and Rayleigh fading channels. The Bit Error Rate (BER) curves also exhibit acceptable performance loss compared to coherent schemes.

## A new look of doping technique in BICM-ID

- **Status**: ❌
- **Reason**: BICM-ID 도핑/SCCC 기법; 컨볼루션 부호 기반 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:6583708
- **Type**: conference
- **Published**: 1-5 July 2
- **Authors**: Tao Cheng, Kewu Peng, Changyong Pan +2
- **PDF**: https://ieeexplore.ieee.org/document/6583708
- **Abstract**: Doping technique was employed to remove the high error floor in conventional bit-interleaved coded modulation with iterative demapping and decoding (BICM-ID). This paper proposes a new look of the doping technique-BICM-ID with serial concatenated convolutional code (SCCC-BICM-ID). Unlike conventional doping decoding scheme which deems the doping decoder and the demapper as a whole doped demapper, we combine the doping code and the outer convolutional code together to form an SCCC, so that iterative demapping and decoding is performed between the demapper and the SCCC decoder. Extrinsic information transfer (EXIT) chart is used to analyze these two decoding schemes and reveals that they both can achieve near-capacity performance with no penalty of error floor. According to the results of EXIT analysis and BER simulations, SCCC-BICM-ID system can achieve the same or even better performance compared to the doping BICM-ID system with lower decoding complexity.
