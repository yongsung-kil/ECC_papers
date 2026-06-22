# IEEE Xplore — 2009-05


## High Performance Non-Binary Quasi-Cyclic LDPC Codes on Euclidean Geometries LDPC Codes on Euclidean Geometries

- **Status**: ❌
- **Reason**: 비이진(non-binary) QC-LDPC 구성 — 비이진 LDPC는 제외 대상
- **ID**: ieee:4939224
- **Type**: journal
- **Published**: May 2009
- **Authors**: Bo Zhou, Jingyu Kang, Ying Yu Tai +2
- **PDF**: https://ieeexplore.ieee.org/document/4939224
- **Abstract**: This paper presents algebraic methods for constructing high performance and efficiently encodable non-binary quasi-cyclic LDPC codes based on flats of finite Euclidean geometries and array masking. Codes constructed based on these methods perform very well over the AWGN channel. With iterative decoding using a fast Fourier transform based sum-product algorithm, they achieve significantly large coding gains over Reed-Solomon codes of the same lengths and rates decoded with either algebraic hard-decision Berlekamp-Massey algorithm or algebraic soft-decision Kotter-Vardy algorithm. Due to their quasi-cyclic structure, these non-binary LDPC codes on Euclidean geometries can be encoded using simple shift-registers with linear complexity. Structured non-binary LDPC codes have a great potential to replace Reed-Solomon codes for some applications in either communication or storage systems for combating mixed types of noise and interferences.

## Gallager's decoding algorithm Α over high order modulations

- **Status**: ❌
- **Reason**: Gallager 알고리즘A를 고차 PAM 변조에 적용한 성능분석(threshold/stability)으로, 변조 매핑 전략이 핵심이며 NAND LDPC에 이식할 신규 디코더 기여 없음
- **ID**: ieee:4939344
- **Type**: journal
- **Published**: May 2009
- **Authors**: H.-K. Yang, M.-K. Lee, K. Yang
- **PDF**: https://ieeexplore.ieee.org/document/4939344
- **Abstract**: Gallager's decoding algorithm A (GDA) for low density parity check (LDPC) codes is of interest mainly due to its good performance with extremely low complexity. In this paper, we analyze GDA over 2m-ary pulse-amplitude modulation (2m-PAM). Firstly, we represent its average error probability by means of a recursion formula. We then define its threshold for additive white Gaussian noise (AWGN) channels and derive its stability condition. The bit-to-symbol mapping strategies have a strong influence on the performance of LDPC-coded modulation systems. Finally, we show that the bit-reliability mapping strategy proposed by Li and Ryan maximizes the threshold of the LDPC coded modulation system with GDA over Gray-mapped 2m-PAM in the AWGN channel.

## Practical Interleavers for Repeat--Accumulate Codes

- **Status**: ❌
- **Reason**: RA(repeat-accumulate) 부호용 인터리버 설계 — 비-LDPC, 이식 LDPC BP 기법 없음
- **ID**: ieee:4939209
- **Type**: journal
- **Published**: May 2009
- **Authors**: Sarah J. Johnson, Steven R. Weller
- **PDF**: https://ieeexplore.ieee.org/document/4939209
- **Abstract**: In this paper we design practical interleavers for regular, systematic repeat-accumulate (RA) codes. The new interleavers, which we call L-type and modified L-type interleavers, are deterministic, described by a single parameter, and straightforward to implement. Despite their simple description, the new interleavers are shown to perform equally as well as, or better than, traditional interleavers over a wide range of code lengths and rates.

## Two-Dimensional SOVA and LDPC Codes for Holographic Data Storage System

- **Status**: ❌
- **Reason**: 홀로그래픽 스토리지용 2D SOVA 검출기 중심, LDPC는 soft-in 부수 언급일 뿐 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:4815998
- **Type**: journal
- **Published**: May 2009
- **Authors**: Jinyoung Kim, Jaejin Lee
- **PDF**: https://ieeexplore.ieee.org/document/4815998
- **Abstract**: We introduce partial response maximum likelihood (PRML) with the two-dimensional (2D) soft output Viterbi algorithm (SOVA) and 2D equalizer for holographic data storage (HDS) channel. The 2D SOVA output is the average of two 1D SOVAs that are separately operated in horizontal and vertical directions. The complexity of the proposed 2D SOVA is increased only twice compared with 1D SOVA while its performance is superior to that of 1D SOVA. Since the 2D SOVA outputs soft decision value, LDPC can be utilized by the soft-in hard-out decoding. We study for different PR target, comparing 1D Viterbi detection with 2D SOVA detection, different misalignments, and two kinds of LDPC codes.

## Simple Classes of Constrained Systems With Unconstrained Positions That Outperform the Maxentropic Bound

- **Status**: ❌
- **Reason**: WI 변조/ECC 결합 bit-stuffing 제약부호 — LDPC ECC 디코더/구성 기법 아님
- **ID**: ieee:4839041
- **Type**: journal
- **Published**: May 2009
- **Authors**: Kees A. Schouhamer Immink, Kui Cai
- **PDF**: https://ieeexplore.ieee.org/document/4839041
- **Abstract**: The Wijngaarden-Immink (WI) scheme is a combined modulation/ECC coding scheme, where arbitrary user data are translated into a constrained sequence in which predefined positions are reserved for error-correcting codes (ECC) parity. Besides offering the benefit of combined modulation/ECC coding, the WI scheme has two extra benefits. They are (a) error propagation is limited to the constrained symbols, since symbols on the unconstrained positions are not related, and (b) code hardware is limited to a lookup table of the coded part. We will describe classes of simple bit-stuffing schemes that require less redundancy than predicted by the bound based on the performance of maxentropic constrained systems presented by Campello and Poo.

## Optimal Puncturing Ratios and Energy Allocation for Multiple Parallel Concatenated Codes

- **Status**: ❌
- **Reason**: 병렬연접부호(turbo계열) EXIT 차트 펑처링 설계 — 비-LDPC, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:4839034
- **Type**: journal
- **Published**: May 2009
- **Authors**: Fredrik Brannstrom, Lars K. Rasmussen, Alex J. Grant
- **PDF**: https://ieeexplore.ieee.org/document/4839034
- **Abstract**: We propose a systematic design framework for optimal, low-complexity punctured multiple parallel concatenated codes (MPCCs), based on minimizing the convergence threshold using extrinsic information transfer (EXIT) charts. As the convergence threshold is related to the area between the two EXIT curves, the corresponding optimization problem is equivalent to a curve-fitting problem. The EXIT curves are determined by the respective EXIT functions of the constituents, which can be conveniently shaped through the use of random puncturing and unequal energy allocations across parallel coding streams. The design task is therefore to find the optimal combination of constituents, puncturing ratios, and energy allocation for matching the EXIT curves. A search over all rate-one convolutional codes of memory length four or less is performed, identifying 98 classes of codes with unique EXIT functions out of a total of 310 codes. Low-complexity MPCCs with up to four constituents are found, where the convergence thresholds are observed to be within 0.1 dB or less of the fundamental minimum signal-to-noise ratio (SNR) corresponding to the binary phase-shift keying (BPSK) capacity for code rates 1/3 les R les 7/8. Further allowing for unequal energy allocation, the convergence thresholds for lower code rates are similarly improved.

## Nonlinear Sparse-Graph Codes for Lossy Compression

- **Status**: ❌
- **Reason**: sparse-graph code 기반 손실 압축(소스코딩); 채널 ECC 아니라 제외
- **ID**: ieee:4839023
- **Type**: journal
- **Published**: May 2009
- **Authors**: Ankit Gupta, Sergio Verdu
- **PDF**: https://ieeexplore.ieee.org/document/4839023
- **Abstract**: We propose a scheme for lossy compression of discrete memoryless sources: The compressor is the decoder of a nonlinear channel code, constructed from a sparse graph. We prove asymptotic optimality of the scheme for any separable (letter-by-letter) bounded distortion criterion. We also present a suboptimal compression algorithm, which exhibits near-optimal performance for moderate block lengths.

## The Capacity of Finite Abelian Group Codes Over Symmetric Memoryless Channels

- **Status**: ❌
- **Reason**: 유한 아벨 군부호 용량 순수 이론 bound — 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4839038
- **Type**: journal
- **Published**: May 2009
- **Authors**: Giacomo Como, Fabio Fagnani
- **PDF**: https://ieeexplore.ieee.org/document/4839038
- **Abstract**: The capacity of finite Abelian group codes over symmetric memoryless channels is determined. For certain important examples, such as m -PSK constellations over additive white Gaussian noise (AWGN) channels, with m a prime power, it is shown that this capacity coincides with the Shannon capacity; i.e., there is no loss in capacity using group codes. (This had previously been known for binary-linear codes used over binary-input output-symmetric memoryless channels.) On the other hand, a counterexample involving a three-dimensional geometrically uniform constellation is presented in which the use of Abelian group codes leads to a loss in capacity. The error exponent of the average group code is determined, and it is shown to be bounded away from the random-coding error exponent, at low rates, for finite Abelian groups not admitting Galois field structure.

## Analyzing perceptual attributes of 3d video

- **Status**: ❌
- **Reason**: 3D 비디오 JSCC 및 지각품질 분석. LDPC 베이스라인조차 아니며 떼어낼 ECC 기법 없음
- **ID**: ieee:5174467
- **Type**: journal
- **Published**: May 2009
- **Authors**: S.L P. Yasakethu, W.A.C. Fernando, B. Kamolrat +1
- **PDF**: https://ieeexplore.ieee.org/document/5174467
- **Abstract**: The 3D (3 dimensional) video technologies are emerging to provide more immersive media content compared to conventional 2D (2Dimensional) video applications. In this paper we propose a joint source channel coding scheme (JSCC) for colour and depth based 3D video coding using subjective quality of 3D video. We considered different source and channel coding rates to find the optimum JSCC scheme under a given channel bit rate for a WiMAX based communication channel. More often 3D video quality is measured using rigorous and time-consuming subjective evaluation test campaigns. Hence this paper further extends the above study to investigate the relationship between perceptual attributes of 3D video and overall 3D quality and the correlation of these perceptual attributes with several objective quality measures for 3D video content. The results show that, Gaussian and linear polynomial mathematical models can be used to approximate the relationship between depth perception and image quality with overall 3D quality. Also results implies that, VQM and SSIM quality measures of individual left and right views can be effectively used in predicting the image quality and depth perception of 3D video respectively.

## Rate-adaptive compression of LDPC syndromes for Slepian-Wolf coding

- **Status**: ❌
- **Reason**: Slepian-Wolf 신드롬 압축(소스코딩/정보조정 성격) — 채널 ECC 아님
- **ID**: ieee:5167346
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Yong Fang, Gwanggil Jeon, Jechang Jeong
- **PDF**: https://ieeexplore.ieee.org/document/5167346
- **Abstract**: This paper considers the LDPC-based Slepian-Wolf coding with decoder side information. The paper analyzes the statistical properties of LDPC syndromes and shows that there are residual redundancies in LDPC syndromes, especially at low rates. Furthermore, this paper proposes a rate-adaptive way to compress LDPC syndromes.

## An optimal bit allocation framework for error resilient Scalable Video Coding

- **Status**: ❌
- **Reason**: SVC 비트할당 UEP, LDPC는 rate 선택 도구 — 떼어낼 ECC 기법 없음
- **ID**: ieee:5167366
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Yong Liu, Saad B. Qaisar, Hayder Radha +1
- **PDF**: https://ieeexplore.ieee.org/document/5167366
- **Abstract**: In this work, we propose an optimal joint bit allocation framework in order to provide unequal error protection (UEP) for scalable video coding. In the proposed scheme, video sequence is coded based on scalable video coding (SVC) extension of the H.264/AVC standard. We generate different streams according to changing quantization parameters. Each stream divides into different sub-streams in terms of time and quality scalability. These sub-streams with different significance levels are channel-coded using low density parity check (LDPC) codes with different coding rates respectively. Motivated by optimally allocating the bits to achieve resilience against channel induced corruptions, we propose an algorithm that optimally allocates the channel coding rates using a dynamic programming approach. We employ a probability model for decoding failure using LDPC codes. The results achieved clearly establish that the proposed framework can optimally allocate LDPC codes with varying coding rates to different sub-streams with the limited bandwidth.

## Distributed source coding authentication of images with contrast and brightness adjustment and affine warping

- **Status**: ❌
- **Reason**: 분산소스코딩 기반 이미지 인증(Slepian-Wolf) — 채널 ECC 아님
- **ID**: ieee:5167473
- **Type**: conference
- **Published**: 6-8 May 20
- **Authors**: Yao-Chung Lin, David Varodayan, Bernd Girod
- **PDF**: https://ieeexplore.ieee.org/document/5167473
- **Abstract**: Media authentication is important in content delivery via untrusted intermediaries, such as peer-to-peer (P2P) file sharing. Many differently encoded versions of a media file might exist. Our previous work applied distributed source coding not only to distinguish the legitimate diversity of encoded images from tampering but also to localize tampered regions in an image already deemed to be inauthentic. In both cases, authentication requires a Slepian-Wolf encoded image projection that is supplied to the decoder. We extend our scheme to authenticate images that have undergone contrast, brightness, and affine warping adjustment. Our approach incorporates an expectation maximization algorithm into the Slepian-Wolf decoder. Experimental results demonstrate that the proposed algorithm can distinguish legitimate encodings of authentic images from illegitimately modified versions, despite arbitrary contrast, brightness, and affine warping adjustment, using authentication data of less than 250 bytes per image.

## Multirate distributed source coding in wireless sensor network USIND LDPC codes

- **Status**: ❌
- **Reason**: 분산 소스코딩(Slepian-Wolf 압축) 응용으로 LDPC를 베이스라인으로만 사용, 떼어낼 ECC 디코더/HW/구성 기법 없음
- **ID**: ieee:5090114
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Elham Rezayi, Bahman Abolhassani
- **PDF**: https://ieeexplore.ieee.org/document/5090114
- **Abstract**: Energy conservation in wireless sensor networks (WSNs) is the primary performance parameter, because of their limited energy resources. Thus, some energy saving technologies should be applied. One of these technologies for WSNs is distributed source coding (DSC), related to correlation between sensor outputs. In this paper, we propose to apply multirate distributed source coding to reduce energy consumption for a target BER value. Low Density Parity Check (LDPC) code is one of the practical codes that can be used for DSC to compress close to Slepian-Wolf limit. The simulation results for codes of length 1000 and three different compression ratios show that the proposed multirate approach achieves better energy efficiency rather than a single rate code with similar maximum BER value.

## Virtual MIMO-based wireless sensor networks using LDPC codes

- **Status**: ❌
- **Reason**: 가상 MIMO WSN의 분산소스코딩(DSC)에 LDPC 사용 — 소스코딩/압축 응용(Slepian-Wolf), 채널 ECC 아님
- **ID**: ieee:5090113
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Elham Rezayi, Bahman Abolhassani
- **PDF**: https://ieeexplore.ieee.org/document/5090113
- **Abstract**: Energy conservation in wireless sensor networks (WSNs) is one of the primary performance parameters. In this paper, an energy-efficient virtual multiple-input multiple-output (MIMO) communication architecture based on distributed source coding (DSC) is proposed for energy-constrained, distributed wireless sensor networks. Low density parity check (LDPC) code is one of the practical codes that can be used for DSC to compress close to Slepian-Wolf limit. Simulation results show that employing DSC by using a LDPC code with length 1000 and compression ratio of R=3/5 in a virtual MIMO-based WSN achieves better energy efficiency compared to that of a virtual MIMO-based communication system without DSC.

## Implementation of coded cooperation using a kind of convolutional codes

- **Status**: ❌
- **Reason**: convolutional code 기반 coded cooperation으로 비-LDPC 부호이며 이식 가능한 LDPC BP 기법 없음
- **ID**: ieee:5090142
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Linan Sun, Zhongzhao Zhang, Xuejun Sha +1
- **PDF**: https://ieeexplore.ieee.org/document/5090142
- **Abstract**: User cooperative communication can bring spatial diversity, and improve cell boundary uplink quality. This paper gives a kind of convolutional codes suitable for user cooperation with lower complexity than Turbo codes and LDPC codes, and can guarantee good inter-user communication quality when cooperation succeeds, and also good uplink communication quality when cooperation defeats. Simulation results show that when we use 50% cooperation, under the condition that the two users have similar uplink quality and perfect inter-user channel, at BER=10−3, this kind of coded cooperation can provide almost 11 dB performance gains, compared with non-cooperation. Moreover, performance of user cooperation using this kind of convolutional codes is better than that using rate-compatible punctured convolutional codes.

## Signal construction for high-speed access over copper wiring

- **Status**: ❌
- **Reason**: 40GBASE-T copper LDPC coded modulation — 무선/유선 통신 응용 코드 설계, 떼어낼 신규 디코더/구성 기법 없음
- **ID**: ieee:5090089
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Ali Enteshari, Mohsen Kavehrad, Jarir Fadlullah
- **PDF**: https://ieeexplore.ieee.org/document/5090089
- **Abstract**: In this paper, we present signal construction for the future IEEE 40GBASE-T standard. The LDPC assisted coded modulation and demodulation is presented. A code achieving 6 dB gain, which is literally high enough to satisfy reliability constraints for data transmission at a rate of 40 Gbps over 50 m Cat-7A (class FA) copper cable, is designed and the simulation results are presented. The main objective of the presented work is to extensively reduce the power and implementation complexities of a 40GBASE-T system.

## Content-based blind compensation and shaping for streaming video

- **Status**: ❌
- **Reason**: 비디오 스트리밍용 FEC+blind compensation 응용, LDPC 무관하며 떼어낼 디코더/구성 기법 없음
- **ID**: ieee:5090167
- **Type**: conference
- **Published**: 3-6 May 20
- **Authors**: Jun Huang, Funmilayo Lawal, Lei Jin +1
- **PDF**: https://ieeexplore.ieee.org/document/5090167
- **Abstract**: This paper studies video streaming system over a wireless medium. The major challenge is to provide a robust link along the transmission/transport path and most importantly through noisy channels/networks that could add or drop bytes by unforeseeable factors. As a remedy for this phenomenon, we combine forward error correction, blind compensation and traffic shaping to improve the over all performance. We report on the experiments on this unique performance improvement method. The results of our study can find applications in WiMax and AVCP.

## Design of Quasi-Cyclic LDPC Codes Based on Euclidean Geometries

- **Status**: ❌
- **Reason**: 유클리드 기하 기반 QC-LDPC인데 기존 QC-EG-LDPC와 거의 동일 성능, 새 기여 없는 표준 구성 재사용
- **ID**: ieee:5076201
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Yuan-Hua Liu, Xin-Mei Wang, Jian-Hua Ma
- **PDF**: https://ieeexplore.ieee.org/document/5076201
- **Abstract**: This paper presents an algebraic method for constructing quasi-cyclic (QC) low-density parity-check (LDPC) codes based on the structural properties of Euclidean geometries. The construction method results in a class of QC-LDPC codes with girth of at least 6. Codes in this class perform very close to the Shannon limit with iterative decoding. Simulations show that the designed QC-LDPC codes have almost the same performance with the existing QC Euclidean geometry LDPC codes.

## Design of q-ary Irregular Repeat-Accumulate Codes

- **Status**: ❌
- **Reason**: GF(q) 비이진 q-ary IRA/LDPC 부호, EMS 디코딩 - 비이진 LDPC라 제외
- **ID**: ieee:5076200
- **Type**: conference
- **Published**: 26-29 May 
- **Authors**: Wei Lin, Baoming Bai, Ying Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5076200
- **Abstract**: This paper is concerned with the construction of a class of nonbinary irregular repeat accumulate (IRA) codes. Since they are defined on the finite field GF(q) (q>2), we will refer to the constructed codes as q-ary IRA (QIRA) codes. While preserving the excellent error correcting capability of q-ary LDPC codes, QIRA codes can be efficiently encoded like conventional binary IRA codes. By adopting the progressive edge growth (PEG) algorithm to construct the parity check matrices, we can achieve the increased girth of their factor graphs and improved decoding performance. Simulation results show that, using the sum-product algorithm on GF(q), QIRA codes outperform binary LDPC codes and turbo codes in terms of bit error ratio and frame error ratio on AWGN channels. Especially, they could achieve excellent error performance when combined with high order modulations. Feasibility study indicates, with the use of the extended min-sum (EMS) decoding algorithm, QIRA codes are competitive candidates for practical applications.

## Performance analysis of underwater digital speech communication system based on LDPC codes

- **Status**: ❌
- **Reason**: 수중 음성통신에 표준 (864,432) LDPC 단순 선택+turbo 비교 — 표준 부호 재사용, 신규 기여 없음
- **ID**: ieee:5138212
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Wei Han, Jianguo Huang, Min Jiang
- **PDF**: https://ieeexplore.ieee.org/document/5138212
- **Abstract**: To reduce error codes between the receiver and the transmitter and to achieve credible transmission performance of underwater digital speech communication system, low density parity check code (LDPC) is introduced to underwater digital speech communication system. Based on the characteristics of the system, (864,432) LDPC code with code rate 1/2, row weight 6, column weight 3 is selected. We also compare the LDPC code with Turbo code with 1/2 code rate. The experiment results show that digital speech signal transmission is reliable if signal to noise is more than 1.5 dB in the underwater digital speech communication system.

## A novel transmission scheme for irregular LDPC coded OFDM system

- **Status**: ❌
- **Reason**: DD&R LDPC-COFDM 차등보호, OFDM 응용 특이적이고 이식 가능한 디코더/코드설계 기법 없음
- **ID**: ieee:5138422
- **Type**: conference
- **Published**: 25-27 May 
- **Authors**: Yafei Wang, Yiqing Cao, Xuehua Li +1
- **PDF**: https://ieeexplore.ieee.org/document/5138422
- **Abstract**: A novel and practical transmission scheme called Degree Distribution & Reliability Based (DD&R) LDPC - COFDM is proposed for irregular LDPC coded OFDM (LDPC - COFDM) system. Unequal protection of irregular LDPC codes and sub carriers' reliability of OFDM are investigated and combined to enhance the transmission power efficiency. SNR of sub carriers is linearly quantized and defined as reliability. For the irregular LDPC block bits with higher degrees play more important role in the decoding process and hence need more protection during transmission.

## System Model Performance Coupled with DPSK Modulation over Flat Rayleigh Fading Channels

- **Status**: ❌
- **Reason**: 기존 large girth QC-LDPC를 DPSK/Rayleigh에 그대로 적용한 무선 성능평가, 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:5072430
- **Type**: conference
- **Published**: 24-28 May 
- **Authors**: Othman Sidek, Abid Yahya, M. F. M. Salleh
- **PDF**: https://ieeexplore.ieee.org/document/5072430
- **Abstract**: In this paper performance enhancement of the system has been investigated by employing large girth Quasi-Cyclic low-density parity-check (QC-LDPC) codes as forward error correction code, coupled with differential phase shift keying (DPSK) over Rayleigh fading channels. Performance of the system is evaluated by measuring bit error rate (BER) for a given value of Eb/No. Simulation results at diversity level L=4 have confirmed the robustness of the system with a gain of about 1.5 dB as compared to the results of known differential detection system over Rayleigh Fading Channels at a BER of 10-5.

## Adaptive MCS Selection in OFDM Systems Based on Channel Frequency Coherence

- **Status**: ❌
- **Reason**: OFDM 적응 MCS에 SNR 의존 LDPC 부호율 사용 — OFDM 응용 특이적, 표준 LDPC, 떼어낼 기법 없음
- **ID**: ieee:5072427
- **Type**: conference
- **Published**: 24-28 May 
- **Authors**: Muayad S. Al-Janabi, Charalampos C. Tsimenidis, Bayan S. Sharif +1
- **PDF**: https://ieeexplore.ieee.org/document/5072427
- **Abstract**: This paper presents a joint adaptive modulation and coding (AMC) scheme, which exploits the coherence bandwidth of the wireless channel to divide the transmitted frame into independent sub-channels that correspond to the channel coherence bandwidth. This strategy is implemented for orthogonal frequency division multiplexing (OFDM) systems with channel state information (CSI) feedback. Low density parity check (LDPC) codes are utilized for encoding by employing signal-to-noise ratio (SNR) dependent coding rates, as well as distinct modulation schemes to achieve adaptivity to time-varying channel conditions. The performance of the proposed system was tested on Rayleigh fading channels that exhibit frequency coherent bands. Numerical results obtained via simulation demonstrate that the throughput of the proposed system and bit error rate (BER) performance are better than previously suggested approaches.

## Transmitter architecture for faster-than-Nyquist signaling systems

- **Status**: ❌
- **Reason**: FTN OFDM 송신기 아키텍처, LDPC ECC 무관 무선통신 응용
- **ID**: ieee:5117934
- **Type**: conference
- **Published**: 24-27 May 
- **Authors**: Deepak Dasalukunte, Fredrik Rusek, John B. Anderson +1
- **PDF**: https://ieeexplore.ieee.org/document/5117934
- **Abstract**: This paper presents the complexity analysis of a transmitter architecture for a faster-than-Nyquist (FTN) system. Complexity issues in terms of computations and memory requirements to achieve an FTN system are dealt with. An OFDM based multi-carrier system is considered as it is one of the most widely used in upcoming wireless standards. Retaining the modules within the OFDM transmitter helps in exploiting the already optimized and hardware efficient structures, the IFFT being one. From an implementation perspective the introduction of FTN introduces negligible overhead for the transmitter.

## Adaptive Rateless LDPC Code Used for Distributed Video Coding

- **Status**: ❌
- **Reason**: 분산 비디오 코딩용 rateless LDPC+rate estimation, 소스/비디오 압축 응용이라 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:5209178
- **Type**: conference
- **Published**: 19-21 May 
- **Authors**: Cai Shu-ting, Wang Qin-ruo, Xie Yun +1
- **PDF**: https://ieeexplore.ieee.org/document/5209178
- **Abstract**: To overcome the poor adaptive ability of the fixed-LDPC code applied to video compression, a kind of distributed video compression scheme based on rate less LDPC is proposed. A novel rate estimation scheme is also used in both decoder and encoder to reduce the complexity of decoder. While the added complexity of encoder and effected system ratio distortion performance is negligible. And the rateless LDPC supplies to design multiple code modes. Experiments results show that proposed scheme access the 1-2 dB gain of ratio distortion compared with LDPCA.

## Low complexity coded cooperation scheme using non binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC 기반 협력코딩, BP 간소화도 non-binary 전용; 바이너리 LDPC 아님
- **ID**: ieee:5172541
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: V.S. Ganepola, R.A. Carrasco, I. J. Wassell
- **PDF**: https://ieeexplore.ieee.org/document/5172541
- **Abstract**: In this paper we present a coded cooperation scheme using nonbinary LDPC codes and show how it can be used in a multi-user environment to achieve full transmit diversity. It is well known that non-binary LDPC codes over GF(q) outperform binary LDPC codes, but at a cost of increased decoding complexity. To ensure that this scheme can be practically implemented, we demonstrate how the Belief Propagation (BP) algorithm can be simplified, with a complexity dependent only on the row weight of the parity check matrix and independent of the finite field size. We show that this decoding algorithm has only a small degradation in performance compared with BP decoding on quasi-static fading channels and present the performance of a coded cooperation scheme using non-binary LDPC codes defined in GF(4) and GF(16).

## A concatenated space-time transmit diversity system with a class of high-rate low complexity channel codes

- **Status**: ❌
- **Reason**: 다차원 패리티검사코드+STBC 결합, 무선 다이버시티 응용; LDPC 아니고 떼어낼 디코더 기법 없음
- **ID**: ieee:5357984
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: SaiRamesh Nammi
- **PDF**: https://ieeexplore.ieee.org/document/5357984
- **Abstract**: The concatenation of a multidimensional parity check code (MDPC) with space time block codes (STBC) is considered. An approximate expression for the bit error rate of the concatenated system is derived. Effects of imperfect channel estimation on the performance of the system is considered. A comparison with turbo convolutional code (TCC)-STBC system is presented. The error performance of MDPC-STBC system is found to be close to TCC-STBC system but with significantly low complexity.

## Fingerprinting Blank Paper Using Commodity Scanners

- **Status**: ❌
- **Reason**: 종이 질감 지문 인증(물리 보안), ECC/LDPC 무관
- **ID**: ieee:5207652
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: William Clarkson, Tim Weyrich, Adam Finkelstein +3
- **PDF**: https://ieeexplore.ieee.org/document/5207652
- **Abstract**: We develop a novel technique for authenticating physical documents by using random, naturally occurring imperfections in paper texture. To this end, we devised a new method for measuring the three-dimensional surface of a paper without modifying the document in any way, using only a commodity scanner. From this physical feature, we generate a concise fingerprint that uniquely identifies the document. Our method is secure against counterfeiting, robust to harsh handling, and applicable even before any content is printed on a page. It has a wide range of applications, including detecting forged currency and tickets, authenticating passports, and halting counterfeit goods. On a more sinister note, document identification could be used to de-anonymize printed surveys and to compromise the secrecy of paper ballots.

## Performance analysis of multi-user UWB wireless communication systems

- **Status**: ❌
- **Reason**: UWB 다중사용자 통신 성능비교 - LDPC 무관
- **ID**: ieee:5172441
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Yuhong Li, Youzheng Wang, Jianhua Lu
- **PDF**: https://ieeexplore.ieee.org/document/5172441
- **Abstract**: This paper presents a performance comparison of impulse radio ultra wideband (IR-UWB) and multi-band orthogonal frequency division multiplexing (MB-OFDM) for multi-user wireless communication systems. Focusing on the analysis of system performance affected by multi-user interference (MUI) over general additive white Gaussion noise (AWGN) channel, we run a complete system simulation for direct sequence pulse amplitude modulation (DS-PAM), time hopping pulse position modulation (TH-PPM) and MB-OFDM UWB systems. Simulation results show that DS-PAM performs much better than TH-PPM and multi carrier OFDM (MC-OFDM).

## Throughput and outage for block-Markov encoding implementation with network coding for cooperative communications

- **Status**: ❌
- **Reason**: block-Markov 협력통신+네트워크 코딩 처리량/outage 분석; LDPC/디코더/HW 기여 없음, 무선응용 특이적
- **ID**: ieee:5172484
- **Type**: conference
- **Published**: 17-20 May 
- **Authors**: Gordhan Das Menghwar, Wajiha Shah, Christoph F. Mecklenbrauker
- **PDF**: https://ieeexplore.ieee.org/document/5172484
- **Abstract**: In size constraint terminals like in cellular and sensor networks, cooperative communications have been proposed as one of the most efficient way to exploit the benefits of multiple antenna systems. The achievable rates and resulting diversity gains are dependent on information theoretic block-Markov coding. Practical implementation of this information theoretic code design with network coding, as an efficient and low cost option, has recently been proposed. In this paper, we further investigate the resulting benefits in terms of system throughput and outage probability. We also discuss the receiver structure to exploit the resulting cooperative network coding gains and the block-Markov coding in detail. The results show that network coding implementation of block-Markov coding provides considerable gains to cooperative communications

## LDPC-LDGM Based Dirty Paper Coding Techniques for Multicell Cooperative Communication System

- **Status**: ❌
- **Reason**: non-binary LDPC + LDGM 양자화기 기반 dirty paper coding — 비이진 LDPC이고 소스 양자화 응용
- **ID**: ieee:5232273
- **Type**: conference
- **Published**: 16-17 May 
- **Authors**: Haitao Li
- **PDF**: https://ieeexplore.ieee.org/document/5232273
- **Abstract**: The vector dirty paper coding (DPC) can achieve rate region for multicell cooperation system. Conventional DPC implementation approach suffer the capacity loss due to quantization which lead to modulo loss. In this paper, we proposed a vector DPC transmission scheme with non-binary LDPC codes and low density generator matrix based quantizer for multicell processing. And the random coding based proof for the encoding and decoding transmission system is presented. It can achieve a shaping gain and significantly reduce computational complexity.

## A Fast Encoding Method of QC-LDPC Code Used in ABS-S System

- **Status**: ❌
- **Reason**: ABS-S 위성용 표준 QC-LDPC 빠른 인코딩(DVB-S2 변형) — 특정 표준 부호의 인코딩 기법, 새 디코더/구성 기여 없음
- **ID**: ieee:5232297
- **Type**: conference
- **Published**: 16-17 May 
- **Authors**: Shi Yuhai, Liu Chunjiang, Yang Ming
- **PDF**: https://ieeexplore.ieee.org/document/5232297
- **Abstract**: First, the paper introduces a new generation satellite broadcasting system in China named advanced broadcasting system-satellite (ABS-S) that offers system performance and service versatility suitable for future satellite digital broadcasting. Meanwhile the new system utilizes fixed frame structure to realize the CCM, VCM and ACM working modes adopted by DVB-S2 system to further simplify the complexity of the implementation. Secondly, this paper points out the shortcomings of LDPC code used in DVB-S2 and detailedly describes the LDPC code used in ABS-S. Then, based on the simulation result, we can say that the performance of LDPC codes used in ABS-S is better than that of DVB-S2 and the complexity is also lower than that of DVB-S2. At last, we put forward a fast method to encode the QC-LDPC code used in ABS-S system.

## The Application of LDPC Code in ABS-S System

- **Status**: ❌
- **Reason**: ABS-S 위성방송 표준 LDPC 적용/비교 - 표준 부호 응용 비교, 새 디코더/구성 기여 없음
- **ID**: ieee:5231256
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Shi Yuhai, Liu Chunjiang, Yang Ming
- **PDF**: https://ieeexplore.ieee.org/document/5231256
- **Abstract**: The paper firstly describes the new generation satellite broadcasting system used in China named advanced broadcasting system-satellite (ABS-S) that offers system performance and service versatility suitable for future satellite digital broadcasting. Then this paper points out the shortcomings of LDPC code used in DVB-S2 and detailedly describes the LDPC code used in ABS-S. At last, based on the simulation result, we can say that the performance of LDPC codes used in ABS-S is better than that of DVB-S2 and the complexity is also lower than that of DVB-S2.

## Research on An-Based Decode of Tail-Biting Convolutional Codes and Their Performance Analyses Used in LTE System

- **Status**: ❌
- **Reason**: tail-biting convolutional code의 Viterbi 디코딩 - 비-LDPC 부호, BP 비의존 기법
- **ID**: ieee:5231183
- **Type**: conference
- **Published**: 15-17 May 
- **Authors**: Zhang Min, Huang Junwei, Meng Jie +1
- **PDF**: https://ieeexplore.ieee.org/document/5231183
- **Abstract**: Tail-biting convolutional codes has been used in physical broadcast channel and physical downlink control channel of LTE, this paper introduces the architecture of the convolutional encoder and physical broadcast channel used in LTE, elaborating two common Viterbi algorithm, then a new CVA-based improved scheme is proposed, and in Physical broadcast channel system simulation is carried out. The conclusions indicate that the tail-biting convolutional codes can meet the requirements of LTE channel. Furthermore, the result proved that the double traceback Viterbi algorithm process improves the error performance.

## Interactive encoding and decoding based on syndrome accumulation over a binary regular LDPC Enseme

- **Status**: ❌
- **Reason**: 신드롬 누적 기반 대화형 인코딩/디코딩(SA-IED), Slepian-Wolf 소스코딩(H(X|Y)) 대상이지 채널 ECC 아님
- **ID**: ieee:5069517
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Jin Meng, En-hui Yang, Da-ke He
- **PDF**: https://ieeexplore.ieee.org/document/5069517
- **Abstract**: In this paper we investigate the performance of linear interactive encoding and decoding IED based on syndrome accumulation (SA-IED) over a binary regular LDPC ensemble. Assume that the source alphabet is GF(2), and the side information alphabet is finite. It is shown that we can construct universal SA-IED schemes, which are asymptotically optimal for any stationary ergodic source-side information pair. Our analysis further shows that the word error probability will approach 0 sub-exponentially with respect to the block length, while at the same time, the rate approaches H(X|Y) whenever H(X|Y) is within the rate region (isin, 1), where e can be made arbitrarily small by increasing the variable degree of the LDPC code used. Simulation results on binary source-side information pairs show that SA-IED schemes using LDPC codes coupled with linear time belief propagation decoding consistently outperform Slepian-Wolf coding schemes based on LDPC codes.

## Optimized rotations and labeling for non-binary LDPC coded modulation with signal space diversity

- **Status**: ❌
- **Reason**: non-binary LDPC coded modulation, 비이진 제외
- **ID**: ieee:5133820
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Wei Zhou, Li Zou
- **PDF**: https://ieeexplore.ieee.org/document/5133820
- **Abstract**: A non-binary low density parity check (LDPC) coded modulation solution coupling with signal space diversity (SSD) and symbol interleaver is proposed to get performance gains over fading channels for high order modulation. Compared to the traditional binary channel code with bit interleaved coded modulation with iterative demodulation and decode (BICM-ID),it can efficiently avoid the iteration demodulation without performance degradation. And we also analyze the principle of choosing rotation angle and labeling. It is shown that a well-considered choice of the rotation angle and labeling can lead to about 2 dB gain over the conventional unrotated constellation in Rayleigh channel. The related modification in demodulator is also introduced.

## DVB-C2 - The standard for next generation digital cable transmission

- **Status**: ❌
- **Reason**: DVB-C2 표준 소개, 표준 LDPC 단순 사용·신규 기여 없음
- **ID**: ieee:5133812
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: J. Robert, C. Schaaf, L. Stadelmeier
- **PDF**: https://ieeexplore.ieee.org/document/5133812
- **Abstract**: Cable network operators provide a variety of different services, which include analogue and digital TV, Video on Demand (VoD) and also Internet access. The increasing number of these broadband services will require higher bit-rates that are not achievable in many of today's cable networks. The development of DVB-C2 has been finalized recently, providing a cost effective opportunity to upgrade these networks. The new standard utilizes powerful LDPC codes and QAM constellation sizes up to 4096QAM. Additionally, it is based on OFDM instead of single-carrier modulation, which gives additional flexibility and robustness in typical cable channels. This document will give an introduction to the algorithms and the performance of this new DVB-C2 standard.

## Convolutional codes for channels with deletion errors

- **Status**: ❌
- **Reason**: deletion 채널 convolutional code의 Viterbi 디코딩, LDPC 아님·이식 기법 없음
- **ID**: ieee:5069539
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Hugues Mercier, Vijay K. Bhargava
- **PDF**: https://ieeexplore.ieee.org/document/5069539
- **Abstract**: This correspondence studies convolutional codes for channels with deletion errors. We show that the Viterbi decoding algorithm can be modified to correct deletion errors and prove that it is able to find the closest codeword from the received sequence. The computational complexity of the algorithm is comparable to the complexity of the original Viterbi algorithm. We also prove that maximum-likelihood decoding of deletion-correcting trellis codes cannot be achieved using only a forward recursion in the trellis and a single survivor path per state.

## Sparse-graph AL-FEC solutions for IP datacasting in DVB-H

- **Status**: ❌
- **Reason**: DVB-H AL-FEC fountain/erasure sparse-graph 비교, 떼어낼 신규 LDPC ECC 기법 없음
- **ID**: ieee:5133802
- **Type**: conference
- **Published**: 13-15 May 
- **Authors**: Kristian Nybom, Dejan Vukobratovic, Jerker Bjorkqvist
- **PDF**: https://ieeexplore.ieee.org/document/5133802
- **Abstract**: DVB-H is an IP-based wireless broadcast technology in which users are offered, among other services, the IP datacast (IPDC) service for downloading broadcasted files to their mobile terminals. In this paper, we explore different AL-FEC solutions providing simple and efficient file delivery. Our investigation is focused on recently popular classes and design methods of sparse-graph codes decoded using the iterative decoding algorithm. We provide performance comparisons of various possible AL-FEC schemes in a simulated DVB-H environment. The benefits and drawbacks of different sparse-graph AL-FEC solutions are discussed.

## Sparse channel estimation for multicarrier underwater acoustic communication: From subspace methods to compressed sensing

- **Status**: ❌
- **Reason**: 압축센싱 기반 희소 채널추정, ECC/LDPC 디코더와 무관
- **ID**: ieee:5278228
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Christian R. Berger, Shengli Zhou, James C. Preisig +1
- **PDF**: https://ieeexplore.ieee.org/document/5278228
- **Abstract**: In this paper, we present various channel estimators that exploit the channel sparsity in a multicarrier underwater acoustic system, including subspace algorithms from the array precessing literature, namely root-MUSIC and ESPRIT, and recent compressed sensing algorithms in form of Orthogonal Matching Pursuit (OMP) and Basis Pursuit (BP). Numerical simulation and experimental data of an OFDM block-by-block receiver are used to evaluate the proposed algorithms in comparison to the conventional least-squares (LS) channel estimator. We observe that subspace methods can tolerate small to moderate Doppler effects, and outperform the LS approach when the channel is indeed sparse. On the other hand, compressed sensing algorithms uniformly outperform the LS and subspace methods. Coupled with a channel equalizer mitigating intercarrier interference, the compressed sensing algorithms can handle channels with significant Doppler spread.

## Frequency-domain turbo equalization for MIMO underwater acoustic communications

- **Status**: ❌
- **Reason**: 수중음향 MIMO turbo equalization, LDPC 아닌 turbo/LMMSE 채널등화로 부호비의존 이식 기법 없음
- **ID**: ieee:5278227
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Jian Zhang, Yahong Rosa Zheng, Chengshan Xiao
- **PDF**: https://ieeexplore.ieee.org/document/5278227
- **Abstract**: This paper investigates a low-complexity frequency-domain turbo equalization (FDTE) based on linear minimum mean square error (LMMSE) criterion for single-carrier (SC) multiple-input multiple-output (MIMO) underwater acoustic communications (UAC). The receiver incorporates both the equalizer and the decoder which exchange the extrinsic information on the coded bits for each other to implement the iterative detection. The channel impulse responses (CIRs) required in the equalization are estimated in the frequency domain (FD) by inserting the well-designed pilot blocks which are frequency-orthogonal Chu sequences. The proposed SC-MIMO-FDTE architecture is applied to the fixed-to-fixed underwater data gathered during SPACE08 ocean experiments in October 2008, where multiple transducers and hydrophones are deployed in communication ranges of 200 m and 1000 m, and the channel bandwidth is 9.765625 kHz. The phase shift keying (PSK) signals are transmitted from multiple transducers in various block sizes. The proposed transceiver has been demonstrated to improve the bit-error-rate (BER) performance significantly by processing the QPSK data blocks with block length of 1024 in 200 m and 1000 m ranges. The average BERs obtained by turbo detection with 3 iterations can achieve approximately 1.4 times 10-4 for the 200 m system and 4.4 times 10-5 for the 1000 m system.

## Non-perfect channel estimation in OFDM-MIMO-based underwater communication

- **Status**: ❌
- **Reason**: OFDM-MIMO 수중통신 채널추정 MSE 분석, ECC 기법 없음
- **ID**: ieee:5278323
- **Type**: conference
- **Published**: 11-14 May 
- **Authors**: Knut Grythe, Jan Erik Hakegard
- **PDF**: https://ieeexplore.ieee.org/document/5278323
- **Abstract**: The main focus in this publication is on the mean square error of underwater acoustic channel estimators as function of the delay and Doppler spreads of the channel, and the effect this estimation error has on the bit error rate performance of the system both using conventional single antennas (SISO) and when using multiple antennas (MIMO). It is investigated at which delay and Doppler spreads the decoding of the signal in the receiver becomes erroneous. It is assumed that there is no non-uniform Doppler shift. The radio communication standard IEEE 802.16e is modified to match underwater communication conditions. The system parameters are taken from measurements conducted in the Trondheim harbour in Norway in 2007. The channel estimator used is not optimal in the Wiener interpolator sense. Hence, the estimator is sub-optimal, but shows good performance and has relatively low complexity. For the described communication system to perform well the results indicate that movements in the water should be less than 0.01-0.1 m/s, and delay spreads should be less than 0.05-0.5 ms. In systems where the main problem is large Doppler spread, the number of sub-carriers should be small. In systems where the main problem is large delay spread, the number of sub-carriers should be large. The use of MIMO makes the system more robust against estimation errors. The density of pilot symbols may be increased to reduce the channel estimation error somewhat, at the expense of reduced efficiency. Considering the Trondheim harbour channel measurement results and their variability throughout the year, we find that the tested system copes well with the summer conditions while the winter conditions seems to be more challenging.

## Development of a coaxial-type holographic disk system with a small drive

- **Status**: ❌
- **Reason**: 홀로그래픽 디스크 드라이브 광기계 시스템, ECC/LDPC 무관
- **ID**: ieee:5031744
- **Type**: conference
- **Published**: 10-13 May 
- **Authors**: Koji Takasaki, Hidenori Mori, Shinji Yamada +8
- **PDF**: https://ieeexplore.ieee.org/document/5031744
- **Abstract**: We have developed a coaxial-type holographic disk system using the image-stabilizing (IS) technique. The IS technique provides sufficient light energy for recording and retrieving on a continuously rotating disk using a relatively low-power laser diode as the light source. Data-transfer rates of 200 Mbps have been achieved for such drives, but their uses are limited, because its optomechnical unit is merely a testbed settled on a vibration-isolating table. We have developed a small holographic disk drive (footprint 380 x 260 mm, weight 7.5 kg) that operates stably without a vibration-isolating table. In this paper, we describe the drive's key devices, system architecture, and validation results.
