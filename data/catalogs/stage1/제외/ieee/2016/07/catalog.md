# IEEE Xplore — 2016-07


## Superposition Construction of  $Q$ -Ary LDPC Codes by Jointly Optimizing Girth and Number of Shortest Cycles

- **Status**: ❌
- **Reason**: q-ary(비이진 GF(q)) LDPC 구성 — 비이진 LDPC는 제외 대상
- **ID**: ieee:7466096
- **Type**: journal
- **Published**: July 2016
- **Authors**: Hengzhou Xu, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7466096
- **Abstract**: In this letter, we consider the construction of q-ary low-density parity-check (LDPC) codes by jointly optimizing the girth and number of shortest cycles in the frame of superposition. We begin with constructing binary quasi-cyclic LDPC codes by superposition. By replacing the nonzero entries of the parity-check matrices of the resulting binary codes with the nonzero elements of GF(q), a class of q-ary LDPC codes is obtained. Furthermore, we analyze the cycle structure of the constructed codes for a given degree distribution and code length, and present a search algorithm for finding q-ary LDPC codes with few cycles of length g, where g is the optimized girth value. Simulation results show that the proposed codes perform well under the iterative decoding algorithms.

## The Bethe Free Energy Allows to Compute the Conditional Entropy of Graphical Code Instances: A Proof From the Polymer Expansion

- **Status**: ❌
- **Reason**: Bethe free energy와 조건부엔트로피 관계 순수 이론 증명; 디코더/HW/구성으로 안 이어지는 이론 bound
- **ID**: ieee:7460154
- **Type**: journal
- **Published**: July 2016
- **Authors**: Nicolas Macris, Marc Vuffray
- **PDF**: https://ieeexplore.ieee.org/document/7460154
- **Abstract**: The main objective of this paper is to explore the precise relationship between the Bethe free energy (or entropy) and the Shannon conditional entropy of graphical error correcting codes. The main result shows that the Bethe free energy associated with a low-density parity-check code used over a binary symmetric channel in a large noise regime is, with high probability, asymptotically exact as the block length grows. To arrive at this result, we develop new techniques for rather general graphical models based on the loop sum as a starting point and the polymer expansion from statistical mechanics. The true free energy is computed as a series expansion containing the Bethe free energy as its zeroth-order term plus a series of corrections. It is easily seen that convergence criteria for such expansions are satisfied for general high-temperature models. We apply these general results to the ensembles of low-density generator-matrix and parity-check codes. While the application to generator-matrix codes follows standard high temperature methods, the case of parity-check codes requires non-trivial new ideas, because the hard constraints correspond to a zero-temperature regime. Nevertheless, one can combine the polymer expansion with expander and counting arguments to show that the difference between the true and Bethe free energies vanishes with high probability in the large block length limit.

## A Novel UEP Fountain Coding Scheme for Scalable Multimedia Transmission

- **Status**: ❌
- **Reason**: 스케일러블 멀티미디어용 UEP fountain code; BEC 위 fountain/UEP 응용으로 떼어낼 채널 LDPC ECC 기법 없음
- **ID**: ieee:7457260
- **Type**: journal
- **Published**: July 2016
- **Authors**: Lei Yuan, Huaan Li, Yi Wan
- **PDF**: https://ieeexplore.ieee.org/document/7457260
- **Abstract**: In this paper, we propose an efficient scheme to construct fountain codes that can provide unequal error protection (UEP) property. To reduce the coding complexity and improve the performance of previous duplicate UEP schemes in the literature, we implement different rate low-density parity-check codes instead of the duplication process and replace the high-complexity classical robust soliton distribution by low constant average degree distributions with high intermediate symbol recovery rates. Asymptotic analysis of both the duplicate scheme and our scheme is obtained by deriving unequal density evolution formulas over the binary erasure channel. Compared to previous UEP schemes, our scheme has lower complexity. Experimental results show that our scheme can obtain better decoding performance, especially for smaller input information length. Comparison of peak signal-noise ratio performance for the scalable video coding shows that, for moderate input information length, our scheme can provide a better basic video quality at lower overhead, but needs larger overhead to achieve a high video quality.

## Effect of Reader Sensitivity Rotation in TDMR With Head Skew

- **Status**: ❌
- **Reason**: TDMR 자기기록 reader sensitivity 회전; 표준 LDPC+iterative 디코딩 부수 적용, 신규 디코더/코드설계 기여 없음
- **ID**: ieee:7414518
- **Type**: journal
- **Published**: July 2016
- **Authors**: R. Suzuto, Y. Nakamura, H. Osawa +3
- **PDF**: https://ieeexplore.ieee.org/document/7414518
- **Abstract**: The 2-D magnetic recording (TDMR) by shingled magnetic recording (SMR) draws attention as a technology to increase the recording densities in a hard disk drive. The magnetization pattern is curved by the write field at the corner of the writer in SMR, and the information to read/write (R/W) channel performance is feared. Therefore, it is possible that the bit error rate performance is improved by fitting the reader sensitivity to the bit shape. In this paper, we evaluate the effect of reader sensitivity rotation in the TDMR R/W channel with head skew under a specification of 4 Tb/in2 by computer simulation, applying the low-density parity-check coding and the iterative decoding system with the 2-D finite impulse response filter. The results show that the rotated reader sensitivity fits the recorded bit magnetization shape, and the error-free skew range increases to -3°~6°. Therefore, the reader sensitivity rotation is considered to be an effective way to improve the skew margin in the TDMR system.

## Blind Reconstruction of Binary Cyclic Codes From Unsynchronized Bitstream

- **Status**: ❌
- **Reason**: 바이너리 순환부호 블라인드 재구성(군사 감청); 부호 식별 문제로 LDPC 디코더/구성과 무관
- **ID**: ieee:7464832
- **Type**: journal
- **Published**: July 2016
- **Authors**: Arti D. Yardi, Saravanan Vijayakumaran, Animesh Kumar
- **PDF**: https://ieeexplore.ieee.org/document/7464832
- **Abstract**: The problem of identifying the channel code from a received sequence of noise-affected codewords is known as the blind reconstruction of channel codes. Blind reconstruction of channel codes is an important problem in military surveillance applications to identify the channel code used by an adversary. In this paper, we consider the problem of the blind reconstruction of the binary cyclic codes of unknown length from an unsynchronized bitstream (i.e., when the location of codeword boundaries is not known). For the blind reconstruction of cyclic codes, it is sufficient to identify the correct synchronization, the length, and the factors of the generator polynomial of the code. Toward this, we study the distribution of the syndromes (remainders) of the received polynomials with respect to a candidate factor of the generator polynomial. We prove that the probability of zero syndrome is maximum when all the parameters are correct. Using this result, the problem of the blind reconstruction of cyclic codes is formulated and solved as a hypothesis testing problem.

## Fountain Codes With Nonuniform Selection Distributions Through Feedback

- **Status**: ❌
- **Reason**: 피드백 기반 fountain(rateless) 부호 — fountain/erasure는 떼어낼 채널 ECC 기법 없어 제외
- **ID**: ieee:7471486
- **Type**: journal
- **Published**: July 2016
- **Authors**: Morteza Hashemi, Yuval Cassuto, Ari Trachtenberg
- **PDF**: https://ieeexplore.ieee.org/document/7471486
- **Abstract**: One key requirement for fountain (rateless) coding schemes is to achieve a high intermediate symbol recovery rate. Recent coding schemes have incorporated the use of a feedback channel to improve the intermediate performance of traditional rateless codes; however, these codes with feedback are designed based on uniformly at random selection of input symbols. In this paper, on the other hand, we develop feedback-based fountain codes with dynamically adjusted nonuniform symbol selection distributions, and show that this characteristic can enhance the intermediate decoding rate. We provide an analysis of our codes, including bounds on computational complexity and failure probability for a maximum likelihood decoder; the latter is tighter than bounds known for classical rateless codes. Through numerical simulations, we also show that the feedback information paired with a nonuniform selection distribution can highly improve the symbol recovery rate, and that the amount of feedback sent can be tuned to the specific transmission properties of a given feedback channel.

## Asymmetric Error Correction and Flash-Memory Rewriting Using Polar Codes

- **Status**: ❌
- **Reason**: 플래시 rewriting용 비선형 polar code; LDPC 아니고 polar 특이적 기법이라 바이너리 LDPC BP에 이식 불가, 비-LDPC 제외
- **ID**: ieee:7429782
- **Type**: journal
- **Published**: July 2016
- **Authors**: Eyal En Gad, Yue Li, Jörg Kliewer +3
- **PDF**: https://ieeexplore.ieee.org/document/7429782
- **Abstract**: We propose efficient coding schemes for two communication settings: 1) asymmetric channels and 2) channels with an informed encoder. These settings are important in non-volatile memories, as well as optical and broadcast communication. The schemes are based on non-linear polar codes, and they build on and improve recent work on these settings. In asymmetric channels, we tackle the exponential storage requirement of previously known schemes that resulted from the use of large Boolean functions. We propose an improved scheme that achieves the capacity of asymmetric channels with polynomial computational complexity and storage requirement. The proposed non-linear scheme is then generalized to the setting of channel coding with an informed encoder using a multicoding technique. We consider specific instances of the scheme for flash memories that incorporate error-correction capabilities together with rewriting. Since the considered codes are non-linear, they eliminate the requirement of previously known schemes (called polar write-once-memory codes) for shared randomness between the encoder and the decoder. Finally, we mention that the multicoding scheme is also useful for broadcast communication in Marton's region, improving upon previous schemes for this setting.

## Distance Enumerator Analysis for Interleave-Division Multi-User Codes

- **Status**: ❌
- **Reason**: 인터리브 분할 다중사용자 부호 거리 열거 이론 분석 — LDPC ECC 이식 기법 없음, 순수 이론
- **ID**: ieee:7470535
- **Type**: journal
- **Published**: July 2016
- **Authors**: Guanghui Song, Jun Cheng
- **PDF**: https://ieeexplore.ieee.org/document/7470535
- **Abstract**: Consider an interleave-division multi-user coding model for a Gaussian multiple-access channel (MAC). Each user's message is encoded by a separate channel encoder followed by a user-interleaver, which is employed for user separation. All the users' codewords are jointly regarded as one multi-user codeword, and the distance between two multi-user codewords is defined as the Euclidean distance after the inter-user superposition caused by the MAC. A distance enumerator analysis estimates the multi-user maximum likelihood decoding performance. By introducing user-scramblers, a multi-user code ensemble is defined, and its distance enumerator is calculated as concatenated multiple single-user codes and a superposition code. Both finite-length and asymptotic analyses are given and it is shown that interleave-division multi-user codes have much better distance properties than conventional random direct-sequence code-division multiple-access. In fact, the codes achieve almost the same asymptotic uniquely decodable performance as a multi-user random code.

## An ECC/DCT-Based Robust Video Steganography Algorithm for Secure Data Communication

- **Status**: ❌
- **Reason**: DCT 도메인 비디오 스테가노그래피, Hamming/BCH 사용; LDPC 아니고 보안/은닉 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:11060461
- **Type**: journal
- **Published**: July 2016
- **Authors**: Ramadhan J. Mstafa, Khaled M. Elleithy
- **PDF**: https://ieeexplore.ieee.org/document/11060461
- **Abstract**: Nowadays, the science of information hiding has gained tremendous significance due to advances in information and communication technology. The performance of any steganographic algorithm relies on the embedding efficiency, embedding payload, and robustness against attackers. Low hidden ratio, less security, and low quality of stego videos are the major issues of many existing steganographic methods. In this paper, we propose a novel video steganography method in discrete cosine transform (DCT) domain based on error correcting codes (ECC). To improve the security of the proposed algorithm, a secret message is first encrypted and encoded by using Hamming and BCH codes. Then, it is embedded into the DCT coefficients of video frames. The hidden message is embedded into DCT coefficients of each Y, U, and V planes excluding DC coefficients. The proposed algorithm is tested under two types of videos that contain slow and fast moving objects. The experiential results of the proposed algorithm are compared with three existing methods. The comparison results show that our proposed algorithm outperformed other algorithms. The hidden ratio of the proposed algorithm is approximately 27.53%, which is considered as a high hiding capacity with a minimal tradeoff of the visual quality. The robustness of the proposed algorithm was tested under different attacks.

## Improved decoding for Raptor codes with short block-lengths over BIAWGN channel

- **Status**: ❌
- **Reason**: Raptor/fountain 코드 LT 디코딩 개선(GJE 보조) — fountain 코드 전용, NAND LDPC 이식 기법 없음
- **ID**: ieee:7546447
- **Type**: conference
- **Published**: 6-8 July 2
- **Authors**: Amrit Kharel, Lei Cao
- **PDF**: https://ieeexplore.ieee.org/document/7546447
- **Abstract**: Decoding of Raptor codes consists of decoding of both the LT part and the precode part of the codes. When LT decoding is performed, a scenario may arise where the message passing-based decoding process is unable to provide non-zero log-likelihood ratio (LLR) updates to a fraction of input symbols even if it is mathematically possible to do so. The problem is even more critical for codes with short block-lengths and for smaller overheads. We show that this problem degrades the overall decoding performance of Raptor codes over binary input additive white Gaussian noise (BIAWGN) channel. To combat this problem, the Gauss-Jordan elimination (GJE) is used to assist decoding so that the decoder can continuously provide non-zero LLR updates to all the input symbols connected in the decoding graph. Through simulation results we show that the GJE-assisted method provides significantly better bit error rate (BER) performance of Raptor codes than the traditional method across a wide range of signal to noise ratio (SNR) and transmission overheads.

## A study on turbo equalization for MIMO system based on LDPC codes

- **Status**: ❌
- **Reason**: MIMO+STTC turbo equalization 모델이 기여, LDPC는 외부부호 부수 언급, 이식 가능 ECC 기법 없음
- **ID**: ieee:7537083
- **Type**: conference
- **Published**: 5-8 July 2
- **Authors**: Chang-uk Baek, Ji-won Jung
- **PDF**: https://ieeexplore.ieee.org/document/7537083
- **Abstract**: In this paper, MIMO (Multiple-Input-Multiple Output) system based on turbo equalization techniques which LDPC (Low Density Parity Check) codes were outer code and STTC (Space Time Trellis Code) were employed as an inner code are studied. LDPC may be applied these system, it must make BCJR output be hard decision data. It caused performance degraded. This paper proposed turbo equalization model for LDPC codes able to apply MIMO system combined with STTC codes. By the simulation results, we confirmed performance of proposed turbo equalization model was improved about 2.5 dB than that of turbo codes and about 11.5dB than that of conventional LDPC codes.

## An efficient FTN decoding method using separation Of LDPC decoding symbol

- **Status**: ❌
- **Reason**: 기여는 FTN ISI용 turbo equalization(LDPC심볼 분리)이며 떼어낼 LDPC 디코더/HW/코드설계 기법 없음
- **ID**: ieee:7537075
- **Type**: conference
- **Published**: 5-8 July 2
- **Authors**: Ha-Hyun Sung, Ji-Won Jung
- **PDF**: https://ieeexplore.ieee.org/document/7537075
- **Abstract**: To increase throughput efficiency and improve performance, FTN (Faster Than Nyquist) method and LDPC (Low Density Parity Codes) codes are employed in DVB-S3 system. In this paper, we proposed efficient turbo equalization model to minimize inter symbol interference induced by FTN transmission. To make performance improved in turbo equalization model, the outputs of LDPC and BCJR (Bahl, Cocke, Jelinek and Raviv) equalizer are iteratively exchange probabilistic information. In fed LDPC outputs to extrinsic information of BCJR equalizer, we split output to separate bit probabilities. We confirmed that performance was improved compared to conventional methods as increasing throughput parameters of FTN.

## A Comparison of Error Performance for Iterative Calculation in MSA Decoder for LDPC Nonregular Parity Check Matrix in 16QAM System

- **Status**: ❌
- **Reason**: 표준 802.11n 행렬에 표준 min-sum FPGA 비교연구, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:7545348
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Yi Hua Chen, Mei Lin Su, Hua Ting Syu +1
- **PDF**: https://ieeexplore.ieee.org/document/7545348
- **Abstract**: Based on the lower density parity check matrices in approximate lower triangular form allowed by the IEEE P802.11n/D1.04 (Part 11: Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications) standards, LabVIEW FPGA programming language was used in this study to construct an encoder with a contract advantageous in the implementation of the hardware circuit that can generate codewords in various conditions, including four code rates (1/2, 2/3, 3/4, 5/6) and three subblock sizes (27, 54, and 81 bits), and a decoder that used the minimum sum algorithm. The program can encode and decode signals by first selecting code rate and subblock size and then changing the structure of the check and variable nodes accordingly. In this study, a detailed introduction to minimum-sum algorithm and the decoding mechanism was provided, the decoding program was optimized, and decoding performance was analyzed using bit error rate (BER) efficiency curves. In addition, the decoder was simulated under an additive white Gaussian noise channel with a noise ratio Eb/N0 ranging from 0 dB to 10 dB. Decoding performance for various combinations of code rate and subblock size were compared by generating BER efficiency curves for these combinations. Simulation results showed that subblock size did not affect BER, but code rate did. BER resulting from 16 quadrature amplitude modulation was compared to BER from quadrature phase-shift keying, binary phase-shift keying, and the 802.11n and 802.16e standards.

## A Steganography Scheme Based on Cyclic Codes with Iterative Toggle Search Set

- **Status**: ❌
- **Reason**: cyclic code 기반 스테가노그래피(정보은닉); 채널 ECC 아니고 LDPC 디코더 이식 기법 없음
- **ID**: ieee:7545384
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Hsi-Yuan Chang, Jyun-Jie Wang, Chi-Yuan Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/7545384
- **Abstract**: This paper proposes a cyclic steganographic scheme based on cyclic codes for embedding secret message. This scheme is capable of achieving low complexity and fast embedding time. These are two attractive reasons for this method: first, embedding and secret message extraction can be implemented easily by employing shift registers with feedback connections, and second, because they are rich in coding structure, it is possible to devise various practical methods for decoding or extracting them. Moreover, this work has no need to find the maximum likelihood solution in terms of toggle sequence. Instead of full search method, iteration scheme is employed in this work.

## Finite Geometry Codes Based on Geometry Permutation Decoding

- **Status**: ❌
- **Reason**: 유한기하 부호의 majority-logic 기반 GPD 디코딩; 바이너리 LDPC BP에 이식할 새 기법 아님(MLD 계열), 도메인 특이적
- **ID**: ieee:7545375
- **Type**: conference
- **Published**: 4-6 July 2
- **Authors**: Jyun-Jie Wang, Chi-Yuan Lin
- **PDF**: https://ieeexplore.ieee.org/document/7545375
- **Abstract**: This study proposes a novel coding method, called geometry permutation decoding (GPD). The GPD algorithm provides a two dimension geometry construction and decodes information sequence based on this construction. Majority logic decoding (MLD) algorithm can be used for some specially coding scheme, especially finite geometry codes. MLD algorithms are simple and fast owing to the finite geometry construction, however, they have no good decoding efficiency. Unlike with the majority logic decoding algorithm, this method not only has low decoding complexity but also achieves more decoding efficiency.

## Performance investigation for LDPC-coded upstream transmission systems in IM/DD OFDM-PONs

- **Status**: ❌
- **Reason**: IM/DD OFDM-PON 업스트림 전송 시스템 설계로 LDPC가 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:7718264
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Xiaoxue Gong, Lei Guo, Jingjing Wu
- **PDF**: https://ieeexplore.ieee.org/document/7718264
- **Abstract**: To mitigate interferences of subcarrier-to-subcarrier intermixing and ONU-to-ONU beating, we design a LDPC-coded and spectrum-efficient upstream transmission system. Simulation results demonstrate the receiver sensitivity is improved 3.6 dB under QPSK after 100 km transmission.

## Enabling technologies for high spectral efficiency and high capacity transmission over transoceanic distances

- **Status**: ❌
- **Reason**: 대용량 해저광전송 기술 리뷰로 LDPC 무관
- **ID**: ieee:7718300
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Matt Mazurczyk
- **PDF**: https://ieeexplore.ieee.org/document/7718300
- **Abstract**: We review advances in the technologies used to enable high capacity transoceanic distance transmission including transmitter DSP, advanced modulation formats, and C+L transmission. Demonstrations including transmission of 49.3Tb/s over 9,000km are presented.

## Post-FEC performance comparison of pilotaided phase unwrap and turbo differential decoding for cycle slip mitigation

- **Status**: ❌
- **Reason**: turbo differential decoding+cycle slip mitigation, 비-LDPC이며 LDPC BP에 이식할 기법 없음
- **ID**: ieee:7718463
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Tangqing Liu, Yan Li, Huizhong Chen +3
- **PDF**: https://ieeexplore.ieee.org/document/7718463
- **Abstract**: Post-FEC BER-performance of pilot-aided-phase-unwrap(PAPU) and turbo-differential-decoding(TDD) have been investigated in different laser-linewidths and carrier-phase-estimation(CPE) filter-lengths. TDD outperforms PAPU by 0.3dB with sufficient filter-length, while PAPU has advantages of low or vanished error-floor with short filter-length.

## 3.5-Gbit/s QPSK signal transmission in beam forming of 60-GHz integrated photonic array-antenna

- **Status**: ❌
- **Reason**: 60GHz 광자 배열안테나 빔포밍 QPSK 전송, LDPC/ECC 무관
- **ID**: ieee:7718324
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Kotoko Furuya, Takayoshi Hirasawa, Masayuki Oishi +3
- **PDF**: https://ieeexplore.ieee.org/document/7718324
- **Abstract**: We demonstrate 3.5-Gbit/s QPSK signal transmission in radio-over-fiber system with beam forming of a 60 GHz-band integrated photonic array-antenna. The relationship between beam forming operation and signal quality is quantitatively confirmed.

## Time-frequency packed VCSEL-based IM/DD transmission for WDM access networks

- **Status**: ❌
- **Reason**: VCSEL 기반 광전송(time-frequency packing) 연구로 LDPC 무관
- **ID**: ieee:7718211
- **Type**: conference
- **Published**: 3-7 July 2
- **Authors**: Antonio Malacarne, Francesco Fresi, Gianluca Meloni +2
- **PDF**: https://ieeexplore.ieee.org/document/7718211
- **Abstract**: A commercial 4G 1550nm-VCSEL is employed for wavelength- and polarization-independent 14Gb/s optical transmission up to 25km of SMF, thanks to the time-frequency packing technique that is, for the first time, employed in an IM-DD system.

## A modified design of APSK constellations for AWGN channel

- **Status**: ❌
- **Reason**: APSK 성상도 설계(변조), LDPC 무관 ECC 기법 없음
- **ID**: ieee:7636818
- **Type**: conference
- **Published**: 27-29 July
- **Authors**: Siming Peng, Aijun Liu, Ke Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7636818
- **Abstract**: We consider the power constraint equiprobable uniformly spaced amplitude and phase-shift keying (APSK) constellations capacity and Euclidean distance under additive white Gaussian noise (AWGN) channel. Conventional APSK constellations construction schemes mainly focus on closing the gap between APSK and Gaussian channel capacity or maximizing the minimum Euclidean distance between the signal points. In this paper, we propose to modify the minimum Euclidean distance of APSK constellations based on the Gaussian channel capacity achievable construction technology. We present a novel shaping function which could achieve considerable signal-to-noise ratio (SNR) improvement and faster convergence of APSK to the Gaussian channel capacity than conventional scheme. Numerous simulation results demonstrate the validity of the proposed scheme.

## Multi-code Distributed Storage

- **Status**: ❌
- **Reason**: 분산저장 erasure code(RS/RLNC) 혼합·마이그레이션, 비-LDPC이며 떼어낼 LDPC 디코더/HW 기법 없음
- **ID**: ieee:7820356
- **Type**: conference
- **Published**: 27 June-2 
- **Authors**: Cornelius Hellge, Muriel Medard
- **PDF**: https://ieeexplore.ieee.org/document/7820356
- **Abstract**: Distributed storage systems need to guarantee reliable access to stored data. Resilience to node failures can be increased by using erasure encoding. A variety of erasure codes are discussed in literature and implemented in practice. This multiplicity of codes puts a heavy burden on existing systems. In scenarios such as multi-cloud file delivery or migration of data to a new erasure code, the ability to combine data from diverse erasure codes of multiple cloud systems is essential. The methods presented in this paper enable combining symbols of different erasure codes regardless of their underlying generator matrix, finite field size, and source block size. Mathematical approaches are discussed using Reed-Solomon and RLNC codes as example but without loss of generality. The presented approaches enable multi-cloud file delivery across diverse coding algorithms and permits graceful migration of a legacy erasure coding without the need of re-ingestion of existing data.

## Low Rank Parity Check Codes Against Reed-Solomon Codes for Narrow-Band PLC Smart Grid Networks

- **Status**: ❌
- **Reason**: 랭크메트릭 LRPC 부호(GF(q) 벡터공간 기반), 비이진/비-LDPC라 제외
- **ID**: ieee:7808362
- **Type**: conference
- **Published**: 26-27 July
- **Authors**: Yazbek Abdul Karim, El-Qachchach Imad, Cances Jean-Pierre +1
- **PDF**: https://ieeexplore.ieee.org/document/7808362
- **Abstract**: This paper introduces a new family of rank metric codes: the Low Rank Parity Check Codes (LRPC) for which we propose an efficient probabilistic LRPC decoding algorithm concatenated with convolutional code associated with an interleaver. The main idea of decoding LRPC codes is based on calculations of vector spaces over a finite field F(q). This family of codes can be seen as the equivalent of classical LDPC codes for the rank metric. We compare the performance of this code with the Reed-Solomon Code (RS) through a PLC channel. We propose to replace the Reed-Solomon code with a kind of rank metric code (LRPC code) that can correct a whole line or row of a code word, which is arranged in a matrix. Using OFDM modulation, the columns of code matrix contain the OFDM symbols. Weshow by simulation that the proposed system outperforms the traditional scheme where the PLC channel is subjected to both impulsive noise and narrowband interference.

## A Joint Decoding Strategy of Non-binary LDPC Codes Based on Retention Error Characteristics for MLC NAND Flash Memories

- **Status**: ❌
- **Reason**: 비이진(NB-LDPC) 디코딩 전략으로 바이너리 한정 기준에 의해 제외. NAND 도메인이나 NB-LDPC라 제외
- **ID**: ieee:7774762
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Liyan Qiao, Hefeng Wu, Debao Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/7774762
- **Abstract**: A joint decoding strategy is proposed to reduce the time consumption of non-binary LDPC (NB-LDPC) decoding process. This strategy is based on the retention error characteristics of Multi-Level Cell (MLC) NAND flash memories. The raw bit error rate is estimated by an empirical formula of retention error increasing model. With the bit flip patterns caused by retention errors in a MLC NAND flash cell, the bit-granularity bit error rate (soft information) can be calculated according to the raw bit error rate (RBER). Then, the soft information is used as an input of the NB-LDPC decoder to accelerate the convergence of decoding process. The experimental results show that the proposed joint decoding strategy can reduce an average 20.5% of the time consumption of NB-LDPC decoding process (the maximum reduction reaches 65.1%). In addition, the error correction capability is almost doubled, while experiencing only little overhead.

## An Improved LDPC-based SEC Error Reconciliation Scheme

- **Status**: ❌
- **Reason**: CV-QKD 정보조정(reconciliation) 가속이며 채널 ECC가 아님. 떼어낼 디코더 양자화/HW 기법 명시 없음
- **ID**: ieee:7774838
- **Type**: conference
- **Published**: 21-23 July
- **Authors**: Qiong Li, Rui Zhu, Yaxing Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/7774838
- **Abstract**: CV-QKD has drawn many attentions due to the potential to provide high secret key rate and low cost. Error reconciliation is the key module of post processing of a CV-QKD system. In this paper, an improved LDPC-based SEC error reconciliation scheme is proposed. Through the optimization of inner-level decoding and reduction of the iteration rounds of inter-level decoding, the reconciliation can be accelerated evidently. Simulation results show that the proposed scheme can improve the reconciliation rate to 16.55kbps with the reconciliation efficiency of 91.8% when SNR is 4.5dB.

## Non-binary turbo codes on additive impulsive noise channels

- **Status**: ❌
- **Reason**: 비이진 GF(4) turbo 코드 — 비이진+비-LDPC, 제외 대상
- **ID**: ieee:7574024
- **Type**: conference
- **Published**: 20-22 July
- **Authors**: Wael Abd-Alaziz, Martin Johnston, Stephane Le Goff
- **PDF**: https://ieeexplore.ieee.org/document/7574024
- **Abstract**: It is well known that binary error-correcting codes with iterative decoders can achieve near Shannon-limit performance on the additive white Gaussian noise (AWGN) channel, but their performance on more realistic wireless channels can become degraded due to the presence of burst errors or impulsive noise due to interference. A better performing coding scheme is the class of non-binary codes, which are known to be more effective in correcting burst errors, but interestingly there is no research reported in the literature investigating non-binary codes on impulsive noise channels. In this paper, we investigate the performance of non-binary turbo codes defined in a finite field GF(4) on symmetric alpha-stable impulsive noise channels and compare with comparable binary turbo codes. A Cauchy receiver is also employed to mitigate the effects of the channel to assist the turbo decoding. Our simulation results show that although the non-binary turbo code performs similarly to the binary turbo code on the AWGN channel, it achieves a significant coding gain over the binary turbo code as impulsiveness increases.

## Polar codes based OFDM-PLC systems in the presence of middleton class-A noise

- **Status**: ❌
- **Reason**: polar 코드 PLC 임펄스노이즈 성능평가; 비-LDPC, LDPC는 비교 베이스라인뿐, 떼어낼 기법 없음
- **ID**: ieee:7574022
- **Type**: conference
- **Published**: 20-22 July
- **Authors**: Ammar Hadi, Khaled M. Rabie, Emad Alsusa
- **PDF**: https://ieeexplore.ieee.org/document/7574022
- **Abstract**: The performance of power line communication (PLC) systems suffer mainly from non-Gaussian noise, commonly referred to as impulsive noise. To reduce the effect of this noise, various channel coding techniques have been studied in the literature over PLC channels. Unlike existing works, in this paper we investigate the performance and robustness of polar codes over impulsive noise PLC channels for different codeword lengths and noise scenarios in orthogonal frequency division multiplexing (OFDM) systems. In particular, insightful comparisons between hard decision (HD) decoding and soft decision (SD) decoding for the proposed system are made. Furthermore, we investigate the blanking and clipping techniques with polar codes for impulsive noise mitigation. In addition, for the sake of comparison, results for LDPC coding are also presented. The results show that polar codes can considerably improve the performance of PLC systems. It will also be demonstrated that SD decoding offers better performance than HD decoding and that as the codeword length is increased, the performance can be further improved.

## The benefit of frequency-selective rate adaptation for optical wireless communications

- **Status**: ❌
- **Reason**: 광무선 OFDM rate adaptation/bit-power loading; LDPC ECC 기법 없음, 무선 응용 특이적
- **ID**: ieee:7573926
- **Type**: conference
- **Published**: 20-22 July
- **Authors**: Pablo Wilke Berenguer, Volker Jungnickel, Johannes Karl Fischer
- **PDF**: https://ieeexplore.ieee.org/document/7573926
- **Abstract**: In this paper, we evaluate the potential of adaptive transmission for optical wireless communications, used together with a real-valued, DC-biased optical (DCO) orthogonal frequency-division multiplexing (OFDM) waveform. Particularly, we include frequency-selective bit- and power-loading on top of DCO-OFDM. This combination is well known as discrete multitone (DMT). We work out the significant advantage of frequency-selective rate adaptation for operation in both, low signal-to-noise ratios and non-line-of-sight scenarios, as compared to using a fixed modulation format commonly applied over all subcarriers and switching between these formats. Our evaluation is based on the channel impulse responses (CIRs) provided by the IEEE task group for the 802.15.7r1 standard. Transmission bandwidth is up to 200 MHz, as supported by modern optical wireless frontends.

## Decoding and detection for magnetic recording channel using single parity coding

- **Status**: ❌
- **Reason**: 자기기록채널 single parity-check + BCJR, LDPC 아니고 떼어낼 BP 기법 없음
- **ID**: ieee:7524256
- **Type**: conference
- **Published**: 13-15 July
- **Authors**: Mohammed D Almustapha, Muhammad B Abdulrazaq, Mohammed Z Ahmed +2
- **PDF**: https://ieeexplore.ieee.org/document/7524256
- **Abstract**: High density recording requires high complex decoders/detectors for handling the interference of symbols both across and along the tracks. In this paper, we present a new interleaved constrained single parity-check code with Balh Coke Jelinek Raviv (BCJR) detector. The BCJR detector handled the code constraints whereas the dithered relative prime (DRP) and the square interleaver provided adequate spreading of the data. The results show that the constrained interleaved single parity-check code achieved a coding gain of about 3 dB, providing a better compromise in terms of performance and complexity.

## LDA-lattice aided network coding for two-way relay

- **Status**: ❌
- **Reason**: LDA lattice 기반 네트워크코딩 two-way relay, lattice 디코딩이라 바이너리 LDPC BP 이식 불가
- **ID**: ieee:7556044
- **Type**: conference
- **Published**: 13-15 July
- **Authors**: William Liu, Cong Ling
- **PDF**: https://ieeexplore.ieee.org/document/7556044
- **Abstract**: In this paper a new joint channel coded network coding (JCCNC) scheme is proposed based on low density construction A (LDA) lattices for the two-way relay channel, which we call LDA-lattice aided JCCNC (LDA-JCCNC). In LDA-JCCNC, the channel coding and network coding operations are integrated through the underlying LDA lattice. The arithmetic addition of the channel coded signals from the two source nodes is directly decoded using the LDA lattice decoding algorithm, and mapped to modulo addition codewords. It is shown that the proposed scheme has a lower complexity and yet perform almost on par with one of the best performing JCCNC schemes, the standard modulo sum JCCNC. We also give methodology on how our LDA-JCCNC scheme can be applied to PAM and QAM modulation systems, over Gaussian integers and Eisenstein integers, in contrast with most existing JCCNC schemes, which are restricted to set types of modulation frameworks.

## Set min-sum decoding algorithm for non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC의 min-sum CN 업데이트 복잡도 감소. 비이진 LDPC라 제외 대상
- **ID**: ieee:7541851
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Liyuan Song, Qin Huang, Zulin Wang
- **PDF**: https://ieeexplore.ieee.org/document/7541851
- **Abstract**: This paper reduces the complexity of decoding non-binary low-density parity-check (LDPC) codes by set partition. In the check node update, the input vectors are partitioned into several sets such that different elements in the virtual matrix enjoy various computational strategies. As a result, the proposed algorithm achieves high computational efficiency by setting strategies according to the correct probability of these elements. Simulation results indicate that it significantly decreases the complexity of check node update with negligible performance loss.

## Construction of full-diversity 1-level LDPC lattices for block-fading channels

- **Status**: ❌
- **Reason**: block-fading 채널용 1-level LDPC lattice 구성 — lattice/무선 응용 특이적, 바이너리 NAND ECC로 떼어낼 LDPC 기법 없음
- **ID**: ieee:7541792
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Hassan Khodaiemehr, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/7541792
- **Abstract**: LDPC lattices were the first family of lattices which have an efficient decoding algorithm in high dimensions over an AWGN channel. When we consider Construction D' of lattices with one binary LDPC code as its underlying code, 1-level LDPC lattices are obtained. Block fading channel (BF) is a useful model for various wireless communication channels in both indoor and outdoor environments. In this type of channel, a lattice point is divided into multiple blocks such that fading is constant within a block but changes, independently, across blocks. The design of lattices for BF channels offers a challenging problem, which differs greatly from its counterparts like AWGN channels. In this paper we construct full diversity 1-level LDPC lattices for block fading channels. We propose a new iterative decoding method for these family of lattices which has complexity that grows linearly in the dimension of lattice.

## An extended Tanner graph approach to decoding LDPC codes over decode-and-forward relay channels

- **Status**: ❌
- **Reason**: decode-and-forward 릴레이 채널 특이적 메시지패싱 디코더. 릴레이 오류 표현에 의존, NAND 단일채널로 떼어낼 일반 기법 아님
- **ID**: ieee:7541836
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Bin Qian, Wai Ho Mow
- **PDF**: https://ieeexplore.ieee.org/document/7541836
- **Abstract**: This paper reexamines the decoding problem for LDPC-coded relay channels applying the decode-and-forward protocol. The error-free decoding process at the relay is typically assumed by the conventional MRC based decoder at the destination. However, in practice, the unsuccessful decoding at the relay is unavoidable and the resultant error propagation may become a performance bottleneck. In this paper, we propose a new Tanner graph error representation to accurately characterize the relay decoding errors. Based on the proposed error representation, we derive a new message passing decoder which is implemented on an extended Tanner graph of the system. It is empirically verified that the new decoder can outperform existing decoders, and achieve promising performance improvement in the scenario of symmetric links. Moreover, the proposed error representation allows us to conduct density evolution to analyze the threshold performance of the new decoder for LDPC-coded relay channels.

## Near-capacity protograph doubly-generalized LDPC codes with block thresholds

- **Status**: ❌
- **Reason**: doubly-generalized LDPC(VN/CN에 임의 component code) density evolution threshold — BEC 기반 이론, 표준 바이너리 LDPC NAND ECC와 구조 다르고 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:7541756
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Asit Kumar Pradhan, Andrew Thangaraj
- **PDF**: https://ieeexplore.ieee.org/document/7541756
- **Abstract**: Protograph doubly-generalized low-density parity-check (DGLDPC) codes, which allow for arbitrary component codes at the variable and check nodes of a protograph, are considered. Exact density evolution is derived over the binary erasure channel. Conditions on the protograph and component codes to ensure equality of block-error threshold and density evolution threshold for large-girth ensembles are established. Conditions for stability of density evolution are derived, and block-error threshold property is extended to binary-input symmetric channels. Optimized low-rate protographs for DGLDPC codes over the erasure channel are presented.

## Binary codes with locality for multiple erasures having short block length

- **Status**: ❌
- **Reason**: locality 기반 erasure 복구 바이너리 코드 구성으로 LDPC ECC가 아닌 LRC 이론, 이식할 디코더/HW 기법 없음
- **ID**: ieee:7541380
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: S. B. Balaji, K. P. Prasanth, P. Vijay Kumar
- **PDF**: https://ieeexplore.ieee.org/document/7541380
- **Abstract**: This paper considers linear, binary codes having locality parameter r, that are capable of recovering from t ≥ 2 erasures and which additionally, possess short block length. Both sequential and parallel (through orthogonal parity checks) recovery are considered. In the case of sequential repair, the results include (a) extending and characterizing minimum-block-length constructions for t = 2, (b) providing improved bounds on block length for t = 3 as well as a general construction for t = 3 having short block length, (c) providing high-rate constructions for (r = 2, t ∈ {4, 5, 6, 7}) and (d) providing short-block-length constructions for general (r, t). In the case of parallel repair, minimum-block-length constructions are characterized whenever t|(r2 + r) and examples examined.

## Correction of data and syndrome errors by stabilizer codes

- **Status**: ❌
- **Reason**: 양자 stabilizer/CSS 코드 기반 data-syndrome 정정 — 양자 전용 개념(스태빌라이저)에 의존, 고전 바이너리 LDPC로 이식 불가
- **ID**: ieee:7541704
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Alexei Ashikhmin, Ching-Yi Lai, Todd A. Brun
- **PDF**: https://ieeexplore.ieee.org/document/7541704
- **Abstract**: Performing active quantum error correction to protect fragile quantum states highly depends on the correctness of error information-error syndromes. To obtain reliable error syndromes using imperfect physical circuits, we propose the idea of quantum data-syndrome (DS) codes that are capable of correcting both data qubits and syndrome bits errors. We study fundamental properties of quantum DS codes and provide several CSS-type code constructions of quantum DS codes.

## Channel coding for wireless communication via electromagnetic polarization

- **Status**: ❌
- **Reason**: 무선 편파 변조에 LDPC가 부수 시뮬레이션으로만 언급. 떼어낼 LDPC 신규 기법 없음
- **ID**: ieee:7541838
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Xiaobin Wu, Thomas E. Fuja, Thomas G. Pratt
- **PDF**: https://ieeexplore.ieee.org/document/7541838
- **Abstract**: This paper investigates fundamental properties of polarization-based modulation for wireless communication - and in particular the application of channel coding techniques to such systems. After developing appropriate channel models, bounds on achievable rates are computed, and the performance of exemplary LDPC codes are simulated; this is done for both additive white Gaussian noise channels as well as channels subject to i.i.d. Rayleigh fading. A novel “on/off” modulation scheme is developed that adaptively changes the information-bearing polarization states based on the singular value decomposition (SVD) of the realized channel; this scheme is shown to significantly outperform fixed-constellation schemes as well as adaptive-constellation schemes employing equal energy signals.

## Coding of insertion-deletion-substitution channels without markers

- **Status**: ❌
- **Reason**: 동기화 오류(삽입-삭제) 채널용 spatially-coupled 코드. LDPC는 부수 concatenation, 떼어낼 신규 바이너리 LDPC 디코더/구성 기법 없음
- **ID**: ieee:7541376
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Ryohei Goto, Kenta Kasai, Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/7541376
- **Abstract**: In this paper, we deal with coding for synchronization errors. In conventional studies, to combat such errors, periodic synchronization markers are inserted or specifier and watermark codes are concatenated. These codes enable estimation of synchronous errors, but do not have ability to correct random errors. Low-density parity-check codes are usually concatenate to correct random errors. Due to the lack of dependence of information, periodic synchronization marker insertion prevents codes to approach the capacity. Recently, it is observed that spatially-coupled codes universally approach the symmetric information rate (SIR) of arbitrary finite state Markov channels. We introduce a synchronously erroneous finite state Markov channel model whose SIR is computable. Numerical experiments demonstrate spatially-coupled codes approach the SIR of the channel.

## Short block length code design for interference channels

- **Status**: ❌
- **Reason**: Gaussian 간섭채널용 trellis 부호 설계, 비-LDPC, NAND 이식 기법 없음
- **ID**: ieee:7541631
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Shahrouz Sharifi, Mehdi Dabirnia, A. Korhan Tanc +1
- **PDF**: https://ieeexplore.ieee.org/document/7541631
- **Abstract**: We focus on short block length code design for Gaussian interference channels (GICs) using trellis-based codes. We employ two different decoding techniques at the receiver side, namely, joint maximum likelihood (JML) decoding and single user (SU) minimum distance decoding. For different interference levels (strong and weak) and decoding strategies, we derive error-rate bounds to evaluate the code performance. We utilize the derived bounds in code design and provide several numerical examples for both strong and weak interference cases. We show that under the JML decoding, the newly designed codes offer significant improvements over the alternatives of optimal point-to-point (P2P) trellis-based codes and off-the-shelf low density parity check (LDPC) codes with the same block lengths.

## Capacity-achieving rate-compatible polar codes

- **Status**: ❌
- **Reason**: rate-compatible polar code 구성, polar 전용 sequential 디코더로 LDPC BP 이식 기법 없음
- **ID**: ieee:7541257
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Song-Nam Hong, Dennis Hui, Ivana Marić
- **PDF**: https://ieeexplore.ieee.org/document/7541257
- **Abstract**: We present a method of constructing rate-compatible polar codes that are capacity-achieving with low-complexity sequential decoders. The proposed code construction allows for incremental retransmissions at different rates in order to adapt to channel conditions. The main idea of the construction exploits certain common characteristics of polar codes that are optimized for a sequence of degraded channels. The proposed approach allows for an optimized polar code to be used at every transmission thereby achieving capacity. Due to the length limitation of conventional polar codes, the proposed construction can only support a restricted set of rates that is characterized by the size of the kernel when conventional polar codes are used. We thus consider punctured polar codes which provide more flexibility on block length by controlling a puncturing fraction. We show the existence of capacity-achieving punctured polar codes for any given puncturing fraction. Using punctured polar codes as constituent codes, we show that the proposed rate-compatible polar code is capacity-achieving for an arbitrary sequence of rates and for any class of degraded channels.

## Soft McEliece: MDPC code-based McEliece cryptosystems with very compact keys through real-valued intentional errors

- **Status**: ❌
- **Reason**: MDPC 기반 McEliece 암호시스템, 보안 응용이며 채널 ECC가 아님. soft 디코딩도 암호 키 축소 목적
- **ID**: ieee:7541408
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Marco Baldi, Paolo Santini, Franco Chiaraluce
- **PDF**: https://ieeexplore.ieee.org/document/7541408
- **Abstract**: We propose to use real-valued errors instead of classical bit flipping intentional errors in the McEliece cryptosystem based on moderate-density parity-check (MDPC) codes. This allows to exploit the error correcting capability of these codes to the utmost, by using soft-decision iterative decoding algorithms instead of hard-decision bit flipping decoders. However, soft reliability values resulting from the use of real-valued noise can also be exploited by attackers. We devise new attack procedures aimed at this, and compute the relevant work factors and security levels. We show that, for a fixed security level, these new systems achieve the shortest public key sizes ever reached, with a reduction up to 25% with respect to previous proposals.

## Asymptotic MAP upper bounds for LDPC codes

- **Status**: ❌
- **Reason**: LDPC의 MAP threshold 상한 계산하는 순수 이론 bound. 디코더/HW/구성으로 이어지지 않음
- **ID**: ieee:7541828
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: David Matas, Meritxell Lamarca
- **PDF**: https://ieeexplore.ieee.org/document/7541828
- **Abstract**: This paper aims at computing tight upper bounds for the maximum a posteriori threshold of low-density parity check codes in the asymptotic blocklength regime for the transmission over binary-input memoryless symmetric-output channels. While these bounds are already known, we propose a novel derivation based on a completely different approach: based solely on the concept of the chain rule and the conditional entropy, resorting to the concentration theorem for the code ensemble to compute the syndrome entropy with low complexity employing density evolution.

## Worst case QC-MDPC decoder for McEliece cryptosystem

- **Status**: ❌
- **Reason**: QC-MDPC McEliece 암호용 bit-flipping 디코더의 timing side-channel 대응(worst-case 반복수) - 보안/암호 도메인이며 NAND ECC에 떼어낼 채널코딩 기법 없음
- **ID**: ieee:7541522
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Julia Chaulet, Nicolas Sendrier
- **PDF**: https://ieeexplore.ieee.org/document/7541522
- **Abstract**: QC-MDPC-McEliece is a recent variant of the McEliece encryption scheme which enjoys relatively small key sizes as well as a security reduction to hard problems of coding theory. Furthermore, it remains secure against a quantum adversary and is very well suited to low cost implementations on embedded devices. Decoding MDPC codes is achieved with the (iterative) bit flipping algorithm, as for LDPC codes. Variable time decoders might leak some information on the code structure (that is on the sparse parity check equations) and must be avoided. A constant time decoder is easy to emulate, but its running time depends on the worst case rather than on the average case. So far implementations were focused on minimizing the average cost. We show that the tuning of the algorithm is not the same to reduce the maximal number of iterations as for reducing the average cost. This provides some indications on how to engineer the QC-MDPC-McEliece scheme to resist a timing side-channel attack.

## Computing linear transforms with unreliable components

- **Status**: ❌
- **Reason**: 신뢰불가 회로에서 선형변환 계산(fault-tolerant computation)용 LDPC, 채널 ECC 아님
- **ID**: ieee:7541636
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Yaoqing Yang, Pulkit Grover, Soummya Kar
- **PDF**: https://ieeexplore.ieee.org/document/7541636
- **Abstract**: We consider the problem of computing a binary linear transform when all circuit components are unreliable. We propose a novel “ENCODED” technique that uses LDPC (low-density parity-check) codes and embedded noisy decoders to keep the error probability of the computation below a small constant independent of the size of the linear transform, even when all logic gates in the computation are prone to probabilistic errors. Unlike existing works on applying coding to computing with unreliable components, the “ENCODED” technique explicitly considers the errors that happen during both the encoding and the decoding phases. Further, we show that ENCODED requires fewer operations (in order sense) than repetition techniques.

## Constructing valid convex hull inequalities for single parity-check codes over prime fields

- **Status**: ❌
- **Reason**: prime field(비이진) SPC 부호 convex hull LP, 비이진+순수이론
- **ID**: ieee:7541637
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Eirik Rosnes, Michael Helmling
- **PDF**: https://ieeexplore.ieee.org/document/7541637
- **Abstract**: In this work, we present an explicit construction of valid inequalities (using no auxiliary variables) for the convex hull of the so-called constant-weight embedding of a single parity-check (SPC) code over any prime field. The construction is based on classes of building blocks that are assembled to form the left-hand side of an inequality according to several rules. In the case of almost doubly-symmetric valid classes we prove that the resulting inequalities are all facet-defining, while we conjecture this to be true if and only if the class is valid and symmetric. Such sets of inequalities have not appeared in the literature before, have a strong theoretical interest, and can be used to develop an efficient (relaxed) adaptive linear programming decoder for general (non-SPC) linear codes over prime fields.

## Systematic block Markov superposition transmission of repetition codes

- **Status**: ❌
- **Reason**: BMST 반복부호(비-LDPC), MAP/Viterbi 분석, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7541635
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Kechao Huang, Xiao Ma, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/7541635
- **Abstract**: In this paper, we propose systematic block Markov superposition transmission of repetition (BMST-R) codes, which can support a wide range of code rates but maintain essentially the same encoding/decoding hardware structure. The systematic BMST-R codes resemble the classical rate-compatible punctured convolutional (RCPC) codes, except that they are typically non-decodable by the Viterbi algorithm due to the huge constraint length induced by the block-oriented encoding process. By taking into account that the codes are systematic, the performance of systematic BMST-R codes under maximum a posteriori (MAP) decoding can be analyzed with a simple lower bound and an upper bound with the help of partial input-redundancy weight enumerating function (IRWEF). Numerical results verify our analysis and show that systematic BMST-R codes perform well in a wide range of code rates.

## Simplified Successive-Cancellation List decoding of polar codes

- **Status**: ❌
- **Reason**: polar 코드 SCL 디코딩 단순화. 비-LDPC 부호이며 SCL 기법은 LDPC BP에 이식 불가
- **ID**: ieee:7541412
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Seyyed Ali Hashemi, Carlo Condo, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/7541412
- **Abstract**: The Successive-Cancellation List (SCL) decoding algorithm is one of the most promising approaches towards practical polar code decoding. It is able to provide a good trade-off between error-correction performance and complexity, tunable through the size of the list. In this paper, we show that in the conventional formulation of SCL, there are redundant calculations which do not need to be performed in the course of the algorithm. We simplify SCL by removing these redundant calculations and prove that the proposed simplified SCL and the conventional SCL algorithms are equivalent. The simplified SCL algorithm is valid for any code and can reduce the time-complexity of SCL without affecting the space complexity.

## Finite-blocklength bounds for wiretap channels

- **Status**: ❌
- **Reason**: wiretap 채널 유한블록길이 secrecy rate bound. 순수 이론+보안, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7541867
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Wei Yang, Rafael F. Schaefer, H. Vincent Poor
- **PDF**: https://ieeexplore.ieee.org/document/7541867
- **Abstract**: This paper investigates the maximal secrecy rate over a wiretap channel subject to reliability and secrecy constraints at a given blocklength. New achievability and converse bounds are derived, which are shown to be tighter than existing bounds. The bounds also lead to the tightest second-order coding rate for discrete memoryless and Gaussian wiretap channels.

## SAFFRON: A fast, efficient, and robust framework for group testing based on sparse-graph codes

- **Status**: ❌
- **Reason**: sparse-graph 코드를 group testing(결함 식별)에 응용. 채널 ECC가 아니고 떼어낼 LDPC 디코더/HW/구성 기법 없음
- **ID**: ieee:7541824
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Kangwook Lee, Ramtin Pedarsani, Kannan Ramchandran
- **PDF**: https://ieeexplore.ieee.org/document/7541824
- **Abstract**: The group testing problem is to identify a population of K defective items from a set of n items by pooling groups of items. The result of a test for a group of items is positive if any of the items in the group is defective and negative otherwise. The goal is to judiciously group subsets of items such that defective items can be reliably recovered using the minimum number of tests, while also having a low-complexity decoder. We describe SAFFRON (Sparse-grAph codes Framework For gROup testiNg), a non-adaptive group testing scheme that recovers at least a (1 − ϵ)-fraction (for any arbitrarily small ϵ > 0) of K defective items with high probability with m = 6C(ϵ)K log2 n tests, where C(ϵ) is a precisely characterized constant that depends only on o. For instance, it can provably recover at least (1 − 10−6)K defective items with m ≃ 68K log2 n tests. The computational complexity of the decoding algorithm is O(K log n), which is order-optimal. Further, we describe a systematic methodology to robustify SAFFRON such that it can reliably recover the set of K defective items even in the presence of erroneous or noisy test results. We also propose Singleton-Only-SAFFRON, a variant of SAFFRON, that recovers all the K defective items with m = 2e(1+α)K log K log2 n tests with probability 1 − O(1/Kα), where α > 0 is a constant. Our key intellectual contribution involves the pioneering use of powerful density-evolution methods of modern coding theory (e.g. sparse-graph codes) for efficient group testing design and performance analysis.

## Proof of threshold saturation for spatially coupled sparse superposition codes

- **Status**: ❌
- **Reason**: sparse superposition 코드의 threshold saturation 순수 이론 증명. 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:7541484
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Jean Barbier, Mohamad Dia, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/7541484
- **Abstract**: Recently, a new class of codes, called sparse superposition or sparse regression codes, has been proposed for communication over the AWGN channel. It has been proven that they achieve capacity using power allocation and various forms of iterative decoding. Empirical evidence has also strongly suggested that the codes achieve capacity when spatial coupling and approximate message passing decoding are used, without need of power allocation. In this note we prove that state evolution (which tracks message passing) indeed saturates the potential threshold of the underlying code ensemble, which approaches in a proper limit the optimal threshold. Our proof uses ideas developed in the theory of low-density parity-check codes and compressive sensing.

## Deterministic and ensemble-based spatially-coupled product codes

- **Status**: ❌
- **Reason**: spatially-coupled product code(BCH 등 비-LDPC) DE 분석, 바이너리 LDPC 구성 기여 아님
- **ID**: ieee:7541672
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Christian Häger, Henry D. Pfister, Alexandre Graell i Amat +1
- **PDF**: https://ieeexplore.ieee.org/document/7541672
- **Abstract**: Several authors have proposed spatially-coupled (or convolutional-like) variants of product codes (PCs). In this paper, we focus on a parametrized family of generalized PCs that recovers some of these codes (e.g., staircase and block-wise braided codes) as special cases and study the iterative decoding performance over the binary erasure channel. Even though our code construction is deterministic (and not based on a randomized ensemble), we show that it is still possible to rigorously derive the density evolution (DE) equations that govern the asymptotic performance. The obtained DE equations are then compared to those for a related spatially-coupled PC ensemble. In particular, we show that there exists a family of (deterministic) braided codes that follows the same DE equation as the ensemble, for any spatial length and coupling width.

## Multiplicative repetition based superposition transmission of nonbinary codes

- **Status**: ❌
- **Reason**: non-binary 코드의 곱셈반복 중첩전송(MRST). 비이진+중첩전송 기법으로 제외 대상
- **ID**: ieee:7541854
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Xijin Mu, Baoming Bai, Rui Zhang
- **PDF**: https://ieeexplore.ieee.org/document/7541854
- **Abstract**: This paper presents a new superposition transmission method, called multiplicative repetition based superposition transmission (MRST). It is based on multiplicative repetition and superposition of nonbinary codes. For the encoding process, we use a short nonbinary code as basic code, and superimpose the multiplicatively repeated codewords of the basic code. Two decoding algorithms, the joint decoding algorithm and sliding-window decoding algorithm are proposed. Simulation results show that MRST with joint decoding algorithm is able to achieve to good performance. Compared with block Markov superposition transmission (BMST), MRST with sliding-window decoding algorithm can achieve better performance with less memory order. An improved transmission scheme, which is referred to as punctured multiplicative repetition based superposition transmission (P-MRST), is also proposed to increase the code rate of MRST. Simulation results show that the performance of P-MRST with sliding-window decoding algorithm can be improved by increasing memory order or decoding delay.

## Stopping sets for MDS-based product codes

- **Status**: ❌
- **Reason**: MDS-based product code의 반복 행-열 대수 디코딩 stopping set 분석 - 비-LDPC product code, 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:7541597
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Fanny Jardel, Joseph J. Boutros, Mireille Sarkiss
- **PDF**: https://ieeexplore.ieee.org/document/7541597
- **Abstract**: Stopping sets for MDS-based product codes under iterative row-column algebraic decoding are analyzed in this paper. A union bound to the performance of iterative decoding is established for the independent symbol erasure channel. This bound is tight at low and very low error rates. We also proved that the performance of iterative decoding reaches the performance of Maximum-Likelihood decoding at vanishing channel erasure probability. Numerical results are shown for product codes at different coding rates.

## Reed-muller codes achieve capacity on the quantum erasure channel

- **Status**: ❌
- **Reason**: 양자 erasure 채널에서 CSS stabilizer 부호의 용량달성 - 양자 EC, 스태빌라이저/자기직교성 의존이라 제외
- **ID**: ieee:7541599
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Santhosh Kumar, Robert Calderbank, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/7541599
- **Abstract**: The quantum erasure channel is the simplest example of a quantum communication channel and its information capacity is known precisely. The subclass of quantum error-correcting codes called stabilizer codes is known to contain capacity-achieving sequences for the quantum erasure channel, but no efficient method is known to construct these sequences. In this article, we explicitly describe a capacity-achieving code sequence for the quantum erasure channel. In particular, we show that Calderbank-Shor-Steane (CSS) stabilizer codes constructed from self-orthogonal binary linear codes are capacity-achieving on the quantum erasure channel if the binary linear codes are capacity-achieving on the binary erasure channel. Recently, Reed-Muller codes were shown to achieve capacity on classical erasure channels. Using this, we show that CSS codes constructed from binary Reed-Muller codes achieve the capacity of the quantum erasure channel. The capacity-achieving nature of these CSS codes is also explained from a GF(4) perspective.

## Polar coded non-orthogonal multiple access

- **Status**: ❌
- **Reason**: polar 코드 NOMA 응용. 비-LDPC 부호이며 채널 분극 기법은 LDPC BP에 이식 불가
- **ID**: ieee:7541447
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Jincheng Dai, Kai Niu, Zhongwei Si +1
- **PDF**: https://ieeexplore.ieee.org/document/7541447
- **Abstract**: In this paper, polar codes are first applied in non-orthogonal multiple access (NOMA) and the channel polarization idea is extended to NOMA, which is a major multiple access technique in 5G systems. The polar coded NOMA (PC-NOMA) scheme is proposed, whereby the NOMA channel is decomposed into a series of binary-input channels under a two-stage channel polarization transform. In the first stage, the NOMA channel is divided into a group of user synthesized channels by using the multi-level coding structure. In the second stage, based on the structure of bit-interleaved code modulation, user synthesized channels are further decomposed into binary polarized channels. Then, a joint successive cancellation decoding scheme is given to construct the multiuser receiver of PC-NOMA. Finally, a low complexity search algorithm is proposed to schedule the NOMA decoding order which improves the error performance by enhanced polarization among user synthesized channels. The block error ratio performances over additive white Gaussian noise channels indicate that the proposed PC-NOMA obviously outperforms the turbo coded NOMA scheme due to the advantages of the two-stage polarization.

## Almost universal codes for fading wiretap channels

- **Status**: ❌
- **Reason**: fading wiretap 채널용 lattice 보안 코드. LDPC 아님, 보안/이론 영역으로 제외
- **ID**: ieee:7541866
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Laura Luzzi, Cong Ling, Roope Vehkalahti
- **PDF**: https://ieeexplore.ieee.org/document/7541866
- **Abstract**: We consider a fading wiretap channel model where the transmitter has only statistical channel state information, and the legitimate receiver and eavesdropper have perfect channel state information. We propose a sequence of non-random lattice codes which achieve strong secrecy and semantic security over ergodic fading channels. The construction is almost universal in the sense that it achieves the same constant gap to secrecy capacity over Gaussian and ergodic fading models.

## Using Reed-Solomon codes in the (U | U + V ) construction and an application to cryptography

- **Status**: ❌
- **Reason**: Reed-Solomon 기반 (U|U+V) 코드와 McEliece 암호. 비-LDPC 부호, 보안 응용
- **ID**: ieee:7541435
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Irene Márquez-Corbella, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/7541435
- **Abstract**: In this paper we present a modification of Reed-Solomon codes that beats the Guruswami-Sudan 1 − √R decoding radius of Reed-Solomon codes at low rates R. The idea is to choose Reed-Solomon codes U and V with appropriate rates in a (U | U + V ) construction and to decode them with the Koetter-Vardy soft information decoder. We suggest to use a slightly more general version of these codes (but which has the same decoding performance as the (U | U + V )-construction) for being used in code-based cryptography, namely to build a McEliece scheme. The point is here that these codes not only perform nearly as well (or even better in the low rate regime) as Reed-Solomon codes, but also that their structure seems to avoid the Sidelnikov-Shestakov attack which broke a previous McEliece proposal based on generalized Reed-Solomon codes.

## Optimization of time-switching energy harvesting receivers over multiple transmission blocks

- **Status**: ❌
- **Reason**: 에너지 하베스팅 수신기 최적화 — LDPC 무관, 통신 시스템 최적화 이론
- **ID**: ieee:7541799
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Zhengwei Ni, Mehul Motani
- **PDF**: https://ieeexplore.ieee.org/document/7541799
- **Abstract**: Compared with energy-harvesting transmitters, the performance of energy-harvesting receivers has not been fully investigated. The main consumption of energy at transmitters is for transmission, while that at receivers is for information decoding. Hence, the analysis and optimization of energy-harvesting transmitters and receivers are inherently different. This paper considers optimization of a communication system using an energy-harvesting receiver. We assume that the receiver antenna operates over a relatively wide range of frequencies; hence the receiver can harvest energy from both the in-band signal sent by the transmitter and other possibly out-of-band sources. The receiver adopts a time-switching architecture, i.e., in each block, the receiver first harvests energy then decodes information. We assume the energy consumption for decoding is a non-decreasing convex function of the normalized code rate and dominates the energy used for other processing tasks. In this context, we formulate a non-convex optimization problem to maximize the amount of information decoded over multiple blocks. We solve this non-convex problem by converting it into an equivalent convex problem. We also provide numerical examples to validate the accuracy of our analysis and compare our scheme with two suboptimal schemes requiring less overhead.

## The velocity of the decoding wave for spatially coupled codes on BMS channels

- **Status**: ❌
- **Reason**: SC-LDPC BP 디코딩 wave velocity 공식, 순수 점근 이론으로 디코더/HW/구성 미연결
- **ID**: ieee:7541673
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Rafah El-Khatib, Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/7541673
- **Abstract**: We consider the dynamics of belief propagation decoding of spatially coupled Low-Density Parity-Check codes. It has been conjectured that after a short transient phase, the profile of “error probabilities” along the spatial direction of a spatially coupled code develops a uniquely-shaped wavelike solution that propagates with constant velocity ν. Under this assumption and for transmission over general Binary Memoryless Symmetric channels, we derive a formula for ν. We also propose approximations that are simpler to compute and support our findings using numerical data.

## Decoding analysis accounting for mis-corrections for spatially-coupled split-component codes

- **Status**: ❌
- **Reason**: BCH 성분의 SC split-component 부호 hard-decision 디코딩 분석, 비-LDPC
- **ID**: ieee:7541674
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Dmitri Truhachev, Alireza Karami, Lei Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7541674
- **Abstract**: We consider an asymptotic iterative decoding analysis of spatially-coupled split-component codes used for communication over binary symmetric channel (BSC) with hard-decision decoding at the receiver. The proposed analysis takes into account the impact of mis-corrections that occur in component code decoding. The analysis technique models flows of corrections and mis-corrections that occur throughout the decoding process in the entire coupled code chain. The results for spatially-coupled split-component codes with BCH component codes demonstrate that the analysis provides significantly more accurate estimates of the iterative decoding threshold values.

## A p-ary MDPC scheme

- **Status**: ❌
- **Reason**: 비이진(p-ary/non-binary) MDPC McEliece 암호. 비이진 LDPC이며 보안 응용으로 이중 제외
- **ID**: ieee:7541520
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Qian Guo, Thomas Johansson
- **PDF**: https://ieeexplore.ieee.org/document/7541520
- **Abstract**: The McEliece public key cryptosystem is an attractive general construction that has received extensive attention over the years. Recently, a very promising version called QC-MDPC, was proposed. By using binary quasi-cyclic codes, the size of the public key can be decreased significantly. The decryption step involves iterative decoding of moderate density parity check codes (MDPC). In this paper we propose a non-binary version of QC-MDPC. The errors in the new scheme are discrete Gaussian and the decryption involves a new type of iterative decoding with a non-binary alphabet. The resulting scheme improves upon the binary QC-MDPC in that the size of the pubic key can be even smaller.

## Enhanced recursive Reed-Muller erasure decoding

- **Status**: ❌
- **Reason**: Reed-Muller 부호의 erasure 디코딩 개선 - 비-LDPC 부호(RM)이며 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:7541601
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Alexandre Soro, Jérôme Lacan, Vincent Roca +2
- **PDF**: https://ieeexplore.ieee.org/document/7541601
- **Abstract**: Recent work have shown that Reed-Müller (RM) codes achieve the erasure channel capacity. However, this performance is obtained with maximum-likelihood decoding which can be costly for practical applications. In this paper, we propose an encoding/decoding scheme for Reed-Müller codes on the packet erasure channel based on Plotkin construction. We present several improvements over the generic decoding. They allow, for a light cost, to compete with maximum-likelihood decoding performance, especially on high-rate codes, while significantly outperforming it in terms of speed.

## Bit-additive superposition coding for the bandwidth limited broadcast channel

- **Status**: ❌
- **Reason**: broadcast 채널 superposition/multilevel coding 변조 기법, LDPC ECC 비의존 코드 변조 문제
- **ID**: ieee:7541282
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Ahmed Attia Abotabl, Aria Nosratinia
- **PDF**: https://ieeexplore.ieee.org/document/7541282
- **Abstract**: For the Gaussian broadcast channel, transmission at or near the capacity subject to a specific modulation constraint, has been an essentially open problem. The capacity of the AWGN broadcast is achieved by superposition coding, but superposition of individual coded modulations does not in general obey a predefined constellation. We approach this coded modulation problem with multilevel coding (MLC) which is known to achieve the constellation constrained capacity in the point-to-point channel. In channels involving multiple transmitters or receivers, the application of multilevel coding has received little attention. In this paper, a method is proposed that decomposes superposition coding into binary multilevel superposition coding. The problem of rate allocation through every level for each user is studied and a pragmatic rate allocation procedure is presented. The problem of rate allocation to levels is studied and a pragmatic method for its solution is proposed. The coded modulation with proposed rate allocation achieves rates that are very close to the constellation constrained capacity.

## New error correcting codes for informed receivers

- **Status**: ❌
- **Reason**: informed receiver/index coding용 cyclic·MDS 대수 부호 — 비-LDPC 부호, 이식 가능 디코더 기법 없음
- **ID**: ieee:7541817
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Lakshmi Natarajan, Yi Hong, Emanuele Viterbo
- **PDF**: https://ieeexplore.ieee.org/document/7541817
- **Abstract**: We construct error correcting codes for jointly transmitting a finite set of independent messages to an informed receiver which has prior knowledge of the values of some subset of the messages as side information. The transmitter is oblivious to the message subset already known to the receiver and performs encoding in such a way that any possible side information can be used efficiently at the decoder. We construct and identify several families of algebraic error correcting codes for this problem using cyclic and maximum distance separable (MDS) codes. The proposed codes are of short block length, many of them provide optimum or near-optimum error correction capabilities and guarantee larger minimum distances than known codes of similar parameters for informed receivers. The constructed codes are also useful as error correcting codes for index coding when the transmitter does not know the side information available at the receivers.

## On the capacity of the dirty paper channel with fast fading and discrete channel states

- **Status**: ❌
- **Reason**: dirty paper 채널 용량 이론(state decoding), LDPC와 무관한 정보이론 bound
- **ID**: ieee:7541426
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Stefano Rini, Shlomo Shamai
- **PDF**: https://ieeexplore.ieee.org/document/7541426
- **Abstract**: Interference pre-cancellation as in the “writing onto dirty paper” channel crucially depends on the transmitter having exact knowledge of the way in which input and channel state combine to produce the channel output. The presence of even a small amount of uncertainty in such knowledge, gravely hampers the ability of the encoder to pre-code its transmissions against the channel state. This is particularly disappointing as it implies that interference pre-coding in practical systems is effective only when the channel estimates have very high precision, a condition which is generally unattainable in wireless environments. In this paper we show that state decoding, instead of state pre-cancellation, can be approximately optimal for a channel with discrete states when only partial channel knowledge is available. More specifically, we consider a variation of the “writing onto dirty paper” channel in which a discrete-valued state sequence is multiplied by a fast fading process and derive conditions on the fading distribution for which state decoding closely approaches capacity. This channel model is a special case of the Gelf'and-Pinsker channel and our results show an instance of this problem in which state decoding is approximately optimal.

## Quickest sequence phase detection

- **Status**: ❌
- **Reason**: noisy 관측에서 부분수열 위치 검출 시퀀스 설계 — LDPC/ECC 디코더와 무관
- **ID**: ieee:7541806
- **Type**: conference
- **Published**: 10-15 July
- **Authors**: Lele Wang, Sihuang Hu, Ofer Shayevitz
- **PDF**: https://ieeexplore.ieee.org/document/7541806
- **Abstract**: We consider the problem of designing a length-n binary sequence, such that the location of any length-k contiguous subsequence can be determined from a noisy observation of that subsequence. We derive bounds on the minimal possible k in the limit of n → ∞, and describe some sequence constructions. Both adversarial and probabilistic noise models are addressed. Two applications of the problem include fast positioning and card tricks.

## Bit loading-based irregular LDPC coded-modulation for high-speed optical communications

- **Status**: ❌
- **Reason**: rate-adaptive irregular LDPC + bit-loading 변조 결합, 표준 부호+변조 응용으로 새 디코더/구성 기여 없음
- **ID**: ieee:7550345
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Ding Zou, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7550345
- **Abstract**: In state-of-the-art fibre-optics communication systems, the forward error correction (FEC) and high-order constellation formats are employed. It is important to approach the Shannon limit by using turbo product codes (TPC) and low-density parity-check (LDPC) codes with soft-decision decoding (SDD) algorithms. In this paper, we first study the rate-adaptive irregular LDPC coding technique in wide range of code rates enabling the flexible adjustment according to channel conditions and the simulation results show an improved SNR gain of 0.15 ~ 0.44 dB compared with regular LDPC codes under BPSK transmission. Then we propose a bit-loading rule for irregular LDPC codes combined with 16QAM and demonstrate additional 0.3 dB SNR improvements in low code rate regime, making it a viable solution for next generation high-speed optical communication systems.

## Approaching terabit optical transmission over strong atmospheric turbulence channels

- **Status**: ❌
- **Reason**: FSO/OAM 광전송 데모, large-girth LDPC는 표준 기법 단순 사용, 새 구성 기여 없음
- **ID**: ieee:7550346
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Zhen Qu, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7550346
- **Abstract**: In this invited paper, we experimentally demonstrate high spectral efficiency and large capacity featured free-space optical (FSO) transmission system by using LDPC coded quadrature phase shift keying (QPSK) combined with orbital angular momentum (OAM) multiplexing. The strong atmospheric turbulence channel is emulated by two spatial light modulators on which four randomly generated azimuthal phase patterns from Andrews' spectral density are recorded. The validity of such approach is verified by reproducing the intensity distribution and irradiance correlation function (ICF) from the full-scale simulator. Excellent agreement of experimental, numerical, and analytical results is found. To reduce the azimuthal phase distortion induced by the turbulence emulator, the inexpensive wavefront sensorless adaptive optics (AO) is used. To deal with remaining channel impairments a properly designed large-girth low-density parity-check (LDPC) code is used. To further improve the aggregate data rate, the OAM multiplexing is combined with DWDM and 500 Gb/s optical transmission over the strong atmospheric turbulence channels is demonstrated. By employing both polarization states and frequency-locked lasers, beyond 1 Tb/s serial optical transmission over strong atmospheric turbulence channel can be achieved with the proposed FSO scheme.

## BER analysis of WiMAX on FSO

- **Status**: ❌
- **Reason**: FSO/WiMAX BER 분석, 기존 QC-LDPC 단순 적용으로 새 기여 없음
- **ID**: ieee:7550380
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Goran T. Djordjevic, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/7550380
- **Abstract**: The Worldwide Interoperability for Microwave Access (WiMAX) presented in IEEE 802.16 has the aim to provide wireless broadband services to commercial fixed and mobile users. Free-space-optical (FSO) link can be utilized for establishing the connection between WiMAX base station and core network. This optical wireless technology is used for distributing WiMAX traffic because it represents a cost-effective solution, easy to be installed and supports high data rates. On the other hand, transmission of radio-frequency (RF) signals over a FSO link is strongly dependent on weather conditions. In our work, we study a mixed FSO/WiMAX link with primary aim to determine the overall error rate performance. Firstly, we provide a brief recapitulation of main results in this field. Secondly, we determine error rate dependence on different system and channel parameters. We observe the simultaneous effects of FSO and RF channel conditions on error rate performance. Further, we suggest some quasi cyclic low-density parity-check (LDPC) codes suitable for implementation in these systems and determine their error rate performance for different code words lengths.

## Next steps in elasticity: Enabling signal overlap in optical networks

- **Status**: ❌
- **Reason**: elastic optical network 신호중첩 개념, LDPC ECC 무관
- **ID**: ieee:7550419
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Piero Castoldi, Tommaso Foggi, Francesco Paolucci +1
- **PDF**: https://ieeexplore.ieee.org/document/7550419
- **Abstract**: Elastic optical networks have assumed so far that each optical signal is transmitted along a dedicated frequency slot, avoiding any frequency overlap with other optical signals.

## Ultra-dense space division multiplexing technologies towards multi-Peta bit/s optical transmission

- **Status**: ❌
- **Reason**: SDM 광전송 용량 데모, LDPC 떼어낼 기법 없음
- **ID**: ieee:7550283
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Masatoshi Suzuki, Daiki Soma, Koji Igarashi +6
- **PDF**: https://ieeexplore.ieee.org/document/7550283
- **Abstract**: In this paper, recent progress on ultra-dense, space division multiplexed (SDM) optical transmission towards multi-Peta bit/s are reviewed. By using 6-mode 19-core fiber, we have demonstrated 2.05 Pbit/s transmission over 9.8 km just using C-band. High spatial multiplicity of 114 and ultra-high aggregate spectral efficiency of 456 bit/s/Hz/fiber have been achieved.

## Multi-dimensional demappers for optical fiber systems with soft-decision forward error correction

- **Status**: ❌
- **Reason**: 광섬유 demapper/채널통계 연구, 디코더 자체 기여 아님, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7550340
- **Type**: conference
- **Published**: 10-14 July
- **Authors**: Tobias Fehenberger, Norbert Hanik
- **PDF**: https://ieeexplore.ieee.org/document/7550340
- **Abstract**: We study the impact of demappers using various channel statistics, including circularly symmetric and multi-dimensional Gaussian, in fiber-optic communication systems. In nonlinear dispersion-managed fiber systems, an improvement in achievable information rate (AIR) and bit error ratio (BER) after decoding is obtained from using multi-dimensional non-circularly symmetric Gaussian statistics at the demapper. For fiber systems without in-line dispersion compensation, only minor gains are obtained.

## Serial-inspired diffusion based on message passing for distributed estimation in adaptive networks

- **Status**: ❌
- **Reason**: 분산 추정용 diffusion message-passing, 채널 ECC LDPC 디코더 아님(소스 부호화/추정 영역)
- **ID**: ieee:7569677
- **Type**: conference
- **Published**: 10-13 July
- **Authors**: Cornelius T. Healy, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/7569677
- **Abstract**: Distributed estimation and processing in networks modeled by graphs have received a great deal of interest recently, due to the benefits of decentralised processing in terms of performance and robustness to communications link failure between nodes of the network. Diffusion-based algorithms have been demonstrated to be among the most effective for distributed signal processing problems, through the combination of local node estimate updates and sharing of information with neighbour nodes through diffusion. In this work, we develop a serial-inspired approach based on message-passing strategies that provides a significant improvement in performance over prior art. The concept of serial processing in the graph has been successfully applied in sum-product based algorithms and here provides inspiration for an algorithm which makes use of the most up-to-date information in the graph in combination with the diffusion approach to offer improved performance.
