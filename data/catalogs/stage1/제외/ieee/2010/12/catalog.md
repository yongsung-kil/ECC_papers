# IEEE Xplore — 2010-12


## Large-Girth Nonbinary QC-LDPC Codes of Various Lengths

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC 구성, 바이너리만 포함 원칙에 의해 제외
- **ID**: ieee:5605922
- **Type**: journal
- **Published**: December 2
- **Authors**: Jie Huang, Lei Liu, Wuyang Zhou +1
- **PDF**: https://ieeexplore.ieee.org/document/5605922
- **Abstract**: In this paper, we construct nonbinary quasi-cyclic low-density parity-check (QC-LDPC) codes whose parity check matrices consist of an array of square sub-matrices which are either zero matrices or circulant permutation matrices. We propose a novel method to design the shift offset values of the circulant permutation sub-matrices, so that the code length can vary while maintaining a large girth. Extensive Monte Carlo simulations demonstrate that the obtained codes of a wide range of rates (from 1/2 to 8/9) with length from 1000 to 10000 bits have very good performance over both AWGN and Rayleigh fading channels. Furthermore, the proposed method is extended to design multiple nonbinary QC-LDPC codes simultaneously where each individual code can achieve large girth with variable lengths. The proposed codes are appealing to practical adaptive systems where the block length and code rate need to be adaptively adjusted depending on traffic characteristics and channel conditions.

## EXIT Function Aided Design of Iteratively Decodable Codes for the Poisson PPM Channel

- **Status**: ❌
- **Reason**: Poisson PPM 광통신용 EXIT 기반 코드설계, PPM 채널 특이적이고 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:5629496
- **Type**: journal
- **Published**: December 2
- **Authors**: Maged F. Barsoum, Bruce Moision, Michael P. Fitz +2
- **PDF**: https://ieeexplore.ieee.org/document/5629496
- **Abstract**: This paper presents and compares two iterative coded modulation techniques for deep-space optical communications using pulse-position modulation (PPM). The first code, denoted by SCPPM, consists of the serial concatenation of an outer convolutional code, an interleaver, a bit accumulator, and PPM. The second code, denoted by LDPC-PPM, consists of the serial concatenation of an LDPC code and PPM. We employ Extrinsic Information Transfer (EXIT) charts for their analysis and design. Under conditions typical of a communications link from Mars to Earth, SCPPM is 1 dB away from capacity, while LDPC-PPM is 1.4 dB away from capacity, at a Bit Error Rate (BER) of approximately 10-5. However, LDPC-PPM lends itself naturally to low latency parallel processing in contrast to SCPPM.

## Signal Shaping for Bit-Interleaved Coded Modulation on the AWGN Channel

- **Status**: ❌
- **Reason**: BICM 신호 셰이핑/변조 매핑 기법, LDPC는 부수 결합일 뿐 떼어낼 ECC 디코더·구성 기여 없음
- **ID**: ieee:5601659
- **Type**: journal
- **Published**: December 2
- **Authors**: Harm S. Cronie
- **PDF**: https://ieeexplore.ieee.org/document/5601659
- **Abstract**: In this paper a coded modulation method for the additive white Gaussian noise channel is presented which incorporates signal shaping. The scheme uses a modulation map to map bits to channel inputs. A modulation map is considered that has the advantage it is can easily be combined with binary error-correcting codes. The decoding strategy is a combination of bit-interleaved coded modulation and multistage decoding. The number of required decoding stages is only small compared to other multistage decoding schemes for coded modulation. It is shown that modulation maps can be designed with a constrained capacity limit very close to the capacity of the AWGN channel. When combined with low-density parity-check codes, simulation results show that a near-capacity performance is achieved for high spectral efficiencies.

## FTS: A Distributed Energy-Efficient Broadcasting Scheme Using Fountain Codes for Multihop Wireless Networks

- **Status**: ❌
- **Reason**: fountain/rateless 코드 기반 무선 브로드캐스팅, LDPC ECC 떼어낼 기법 없음
- **ID**: ieee:5605924
- **Type**: journal
- **Published**: December 2
- **Authors**: Badri N. Vellambi, Nazanin Rahnavard, Faramarz Fekri
- **PDF**: https://ieeexplore.ieee.org/document/5605924
- **Abstract**: We investigate the problem of reliable and energy-efficient one-to-all broadcasting in multihop wireless networks, and propose fractional transmission scheme (FTS) - a low-complexity and scalable broadcasting scheme. FTS exploits the broadcasting nature of wireless channels and random encoding of rateless codes to reduce energy consumption while ensuring reliable delivery of packets to all nodes in the network. In the proposed scheme, different neighbors of a node share the responsibility of transmitting packets by sending only a fraction of encoded packets required by the node to successfully receive the data sent by the source. A detailed analysis of the performance of FTS is presented for grid and random deployment networks. Further, extensive simulations compare our scheme with present energy-efficient methods such as random linear coding, multipoint relaying, dominant pruning, and broadcast incremental power scheme. Simulations reveal that FTS offers good performance and adaptability at a low computational cost.

## New Sequences of Capacity Achieving LDPC Code Ensembles Over the Binary Erasure Channel

- **Status**: ❌
- **Reason**: BEC 용량달성 LDPC 앙상블 시퀀스 점근 이론(차수분포·임계값), erasure 채널 점근 bound이고 NAND용 유한길이 디코더/구성으로 안 이어짐
- **ID**: ieee:5625640
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Hamid Saeedi, Amir H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/5625640
- **Abstract**: In this paper, new sequences $(\lambda ^{n},\rho ^{n})$  of capacity achieving low-density parity-check (LDPC) code ensembles over the binary erasure channel (BEC) is introduced. These sequences include the existing sequences by Shokrollahi  as a special case. For a fixed code rate  $R$, in the set of proposed sequences, Shokrollahi's sequences are superior to the rest of the set in that for any given value of  $n$, their threshold is closer to the capacity upper bound  $1- R$. For any given $\delta $,  $0 < \delta < 1-R$, however, there are infinitely many sequences in the set that are superior to Shokrollahi's sequences in that for each of them, there exists an integer number $n_{0}$ , such that for any $n > n_{0}$, the sequence  $(\lambda ^{n},\rho ^{n})$ requires a smaller maximum variable node degree as well as a smaller number of constituent variable node degrees to achieve a threshold within $\delta $-neighborhood of the capacity upper bound  $1-R$. Moreover, it is proven that the check-regular subset of the proposed sequences are asymptotically quasi-optimal, i.e., their decoding complexity increases only logarithmically with the relative increase of the threshold. A stronger result on asymptotic optimality of some of the proposed sequences is also established.

## Maximal Recovery Network Coding Under Topology Constraint

- **Status**: ❌
- **Reason**: WSN 네트워크코딩 위 LDPC 매핑 + erasure BP 복구, 무선 네트워크 응용 특이적이고 떼어낼 NAND ECC 코드설계 기법 없음
- **ID**: ieee:5625625
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Kiran Misra, Shirish Karande, Hayder Radha
- **PDF**: https://ieeexplore.ieee.org/document/5625625
- **Abstract**: Network coding (NC) within wireless sensor networks (WSNs) can be viewed as the mapping of efficient channel codes to the data generated within the network. In particular, this perspective of code-on-network-graphs (CNG) can be exploited to map source data generated within WSN (of size K) to a variable nodes subset in low-density parity check (LDPC) codes. The resulting fixed size symbol stream when transmitted through the network suffers erasures. At sink, an average of z source symbols can be recovered by employing belief propagation decoding. In this paper, we determine CNG code ensembles that achieve maximal recovery (z/K) for different erasure rates and network topological constraints corresponding to node transmission range. An analytic framework to predict code performance under transmission range constraints is developed. Additionally, necessary condition for code stability was derived using fixed-point stability analysis. Optimal solutions for a WSN with 1000 nodes are determined using differential evolution algorithm. We outline a distributed algorithm for generating a sequence of encoded symbols adhering to the designed code ensemble. The performance of the designed CNG code is demonstrated to be superior to random NC and growth code based ensembles, as well as resilient to network size and inter-connectivity variations.

## Stochastic Decoding of Turbo Codes

- **Status**: ❌
- **Reason**: 확률적(stochastic) 컴퓨팅 turbo 디코더로 turbo 부호 전용, 바이너리 LDPC BP로 직접 이식할 기법 없음 → 비-LDPC 제외
- **ID**: ieee:5560886
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Quang Trung Dong, Matthieu Arzel, Christophe Jego +1
- **PDF**: https://ieeexplore.ieee.org/document/5560886
- **Abstract**: Stochastic computation is a technique in which operations on probabilities are performed on random bit streams. Stochastic decoding of forward error-correction (FEC) codes is inspired by this technique. This paper extends the application of the stochastic decoding approach to the families of convolutional codes and turbo codes. It demonstrates that stochastic computation is a promising solution to improve the data throughput of turbo decoders with very simple implementations. Stochastic fully-parallel turbo decoders are shown to achieve the error correction performance of conventional a posteriori probability (APP) decoders. To our knowledge, this is the first stochastic turbo decoder which decodes a state-of-the-art turbo code. Additionally, an innovative systematic technique is proposed to cope with stochastic additions, responsible for the throughput bottleneck.

## Error-Resilient Scheme for Wavelet Video Codec Using Automatic ROI Detection and Wyner-Ziv Coding Over Packet Erasure Channel

- **Status**: ❌
- **Reason**: Wyner-Ziv 비디오 코덱 erasure 채널 보호, 소스-채널/패킷레벨 LDPC 응용, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:5535201
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Zhuo Xue, Kok Keong Loo, John Cosmas +3
- **PDF**: https://ieeexplore.ieee.org/document/5535201
- **Abstract**: The error-resilient for video transmission over the Internet in which regarded as the packet erasure channel is always a tough task and has gained lots of attentions. The main contradictory problem lies between error-resilient and bandwidth usage. Additional redundant data has to be added to achieve robust transmission which leads to huge bandwidth usage. In this paper, an error-resilient scheme called Wyner-Ziv Error-Resilient (WZER) based on a receiver driven layered Wyner-Ziv (WZ) coding framework is proposed. The WZER purposely emphasizes on the protection of the Region of Interest (ROI) area in the frame thus to achieve the better tradeoff between the bandwidth usage and error-resilience. WZER is designed to work for the scenario of wavelet based video coding over packet erasure channel, where several techniques including automatic ROI detection, ROI mask generation, Rate distortion optimization (RDO) quantization, WZ coding with layer design, and packet level Low Density Parity Check (LDPC) code are used. The performances of the proposed WZER are simulated based on average PSNR of luminance, perceptual reconstruction and bandwidth usage and compared with normal Forward Error Correction (FEC) full protection scheme and no protection scheme. The results show the advantages of the proposed WZER over traditional FEC protection, especially in the aspects of the recovery of the subject area and bandwidth efficiency.

## Magnitude modulation for VSAT's low back-off transmission

- **Status**: ❌
- **Reason**: VSAT 단일반송파 magnitude modulation으로 PAPR 저감(전력증폭기 back-off), ECC/LDPC 무관
- **ID**: ieee:6388301
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Marco Gomes, Francisco Cercas, Vitor Silva +1
- **PDF**: https://ieeexplore.ieee.org/document/6388301
- **Abstract**: This paper addresses the problem of controlling the envelope's power peak of single carrier modulated signals, band limited by root-raised cosine (RRC) pulse shaping filters, in order to reduce power amplifier back-off for very small aperture terminals ground stations. Magnitude modulation (MM) is presented as a very efficient solution to the peak-to-average power ratio problem. This paper gives a detailed description of the MM concept and its recent evolutions. It starts by extending the look-up-table (LUT) based approach of the MM concept to M-ary constellations with M ≤ 16. The constellation and RRC symmetries are explored, allowing considerable reduction on LUT computation complexity and storage requirements. An effective multistage polyphase (MPMM) approach for the MM concept is then proposed. As opposed to traditional LUT-MM solutions, MM coefficients are computed in real-time by a low complexity multirate filter system. The back-off from high-power amplifier saturation is almost eliminated (reduction is greater than 95%) with just a 2-stage MPMM system even for very demanding roll-off cases (e.g., α = 0.1). Also, the MPMM is independent of modulation in use, allowing its easy application to constellations with M > 16.

## Code-Aided Maximum-Likelihood Ambiguity Resolution Through Free-Energy Minimization

- **Status**: ❌
- **Reason**: 코드기반 타이밍/위상 모호성 해소(수신기 동기화) factor-graph 알고리즘으로 LDPC ECC 디코더 비의존, 떼어낼 NAND 기법 없음
- **ID**: ieee:5551242
- **Type**: journal
- **Published**: Dec. 2010
- **Authors**: Cédric Herzet, Kampol Woradit, Henk Wymeersch +1
- **PDF**: https://ieeexplore.ieee.org/document/5551242
- **Abstract**: In digital communication receivers, ambiguities in terms of timing and phase need to be resolved prior to data detection. In the presence of powerful error-correcting codes, which operate in low signal-to-noise ratios (SNR), long training sequences are needed to achieve good performance. In this contribution, we develop a new class of code-aided ambiguity resolution algorithms, which require no training sequence and achieve good performance with reasonable complexity. In particular, we focus on algorithms that compute the maximum-likelihood (ML) solution (exactly or in good approximation) with a tractable complexity, using a factor-graph representation. The complexity of the proposed algorithm is discussed and reduced complexity variations, including stopping criteria and sequential implementation, are developed.

## Polarization-multiplexed LDPC-coded QAM robust to I-Q imbalance and polarization offset

- **Status**: ❌
- **Reason**: LDPC-coded QAM 편광다중 광통신 turbo equalization, I-Q imbalance 보상 응용으로 떼어낼 ECC 기법 없음
- **ID**: ieee:5682630
- **Type**: conference
- **Published**: 8-12 Dec. 
- **Authors**: Ivan B. Djordjevic, Lei Xu, Lybomir L. Minkov +2
- **PDF**: https://ieeexplore.ieee.org/document/5682630
- **Abstract**: Polarization-multiplexed LDPC-coded QAM robust to I-Q imbalance and polarization offset is proposed. Efficient mitigation of I-Q imbalance and polarization offset is demonstrated with LDPC-coded turbo equalization by simultaneous MAP detection of symbols transmitted over two orthogonal polarizations. The proposed scheme is much more efficient in I-Q imbalance and polarization offset compensation than conventional approaches.

## Wyner-Ziv coding of multispectral images for space and airborne platforms

- **Status**: ❌
- **Reason**: Wyner-Ziv 분산소스코딩(다중스펙트럼 이미지 압축). LDPC가 소스코딩 신드롬에 사용, 채널 ECC 아님
- **ID**: ieee:5702474
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: Shantanu Rane, Yige Wang, Petros Boufounos +1
- **PDF**: https://ieeexplore.ieee.org/document/5702474
- **Abstract**: This paper investigates the application of lossy distributed source coding to high resolution multispectral images. The choice of distributed source coding is motivated by the need for very low encoding complexity on space and airborne platforms. The data consists of red, blue, green and infra-red channels and is compressed in an asymmetric Wyner-Ziv setting. One image channel is compressed using traditional JPEG and transmitted to the ground station where it is available as side information for Wyner-Ziv coding of the other channels. Encoding is accomplished by quantizing the image data, applying a Low-Density Parity Check code to the remaining three image channels, and transmitting the resulting syndromes. At the ground station, the image data is recovered from the syndromes by exploiting the correlation in the frequency spectrum of the band being decoded and the JPEG-decoded side information band. In experiments with real uncompressed images obtained by a satellite, the rate-distortion performance is found to be vastly superior to JPEG compression of individual image channels and rivals that of JPEG2000 at much lower encoding complexity.

## Implementation of Code Shift Keying signalling technique in GALILEO E1 signal

- **Status**: ❌
- **Reason**: GNSS Code Shift Keying 신호기법, LDPC 무관 비-ECC 통신 응용
- **ID**: ieee:5708056
- **Type**: conference
- **Published**: 8-10 Dec. 
- **Authors**: Axel Garcia Peña, Lionel Ries, Marie-Laure Boucheret +4
- **PDF**: https://ieeexplore.ieee.org/document/5708056
- **Abstract**: One of limitations of the current GNSS signals is their low data information rate. This low data information rate does not allow, for example, the transmission of additional commercial services or the transmission of redundant ephemeris data. The Code Shift Keying (CSK) is a signaling technique specifically designed to increase the transmission bit rate of a spreading spectrum signal. Therefore, one solution to increase the data information rate of the GNSS signals is to introduce the CSK technique in them. In this paper, the implementation of the CSK technique into GNSS signals is inspected through the development and analysis of the likelihood ratio expression of the bits transmitted inside a CSK symbol, and through the identification of the best mapping between bits belonging to a word and bits transmitted inside a CSK symbol. Finally, the impact of the CSK technique on the GALILEO E1 signal is analyzed by calculating the CSK demodulation performance for a given scenario and the drawbacks of the technique on the signal acquisition and tracking processes.

## Reduced-latency scheduling scheme for min-max non-binary LDPC decoding

- **Status**: ❌
- **Reason**: 비이진(NB) QC-LDPC Min-max 디코딩 스케줄링 - 비이진 LDPC는 제외 대상
- **ID**: ieee:5774734
- **Type**: conference
- **Published**: 6-9 Dec. 2
- **Authors**: Xinmiao Zhang, Fang Cai
- **PDF**: https://ieeexplore.ieee.org/document/5774734
- **Abstract**: Compared to binary low-density parity-check (LDPC) codes, non-binary (NB) LDPC codes can achieve higher coding gain when the code length is moderate. On the other hand, the decoding of NB-LDPC codes is more complicated since a vector of messages instead of a single message is passed along each edge of the associated Tanner graph. Layered decoding can be employed to simplify LDPC decoding. However, there is extra latency between the decoding of layers caused by check node processing, message permutation and updating when applied to NB-LDPC codes. In this paper, a novel scheduling scheme is developed to eliminate the extra latency for the Min-max decoding of quasi-cyclic (QC) NB-LDPC codes using trellis-based check node processing. Assume that each row of sub-matrices in the parity check matrix of a QCNB-LDPC code is divided into two layers, the proposed scheme can reduce the decoding latency by a factor of around (2dc + 5)/2dc, where dc is the check node degree. It leads to significant speedup when dc is not large. Moreover, the area overhead of the proposed scheme is less than 10%.

## LDPC decoder performance under different number of iterations in mobile WiMax

- **Status**: ❌
- **Reason**: WiMax LDPC 반복횟수별 BER 비교만, 표준 min-sum/sum-product 그대로 사용, 새 기법 없음
- **ID**: ieee:5704626
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Anugrah Salbiyono, Trio Adiono
- **PDF**: https://ieeexplore.ieee.org/document/5704626
- **Abstract**: We investigate low-density parity-check (LDPC) codes performance used in the IEEE 802.16e under different number of iterations. We use min sum algorithm and sum product algorithm to decode the LDPC codes in various modulation schemes. Simulations are done in Rayleigh channel. From our simulations, we can get better improvement in term of bit error rate (BER) when we increase the iterations from 5 to 10. When we increase the iterations further, we observe slight improvement in BER. Later, we also discuss the simulation results when using sum-product algorithm and min-sum algorithm.

## Iterative multiple-symbol differential detection of differential LDPC codes

- **Status**: ❌
- **Reason**: differential LDPC의 iterative MSDD - fading 채널 differential detection 무선응용 특이적, LDPC는 부수, 떼어낼 디코더/HW/구성 기법 없음
- **ID**: ieee:5704614
- **Type**: conference
- **Published**: 6-8 Dec. 2
- **Authors**: Yang Yu, Shiro Handa, Fumihito Sasamori
- **PDF**: https://ieeexplore.ieee.org/document/5704614
- **Abstract**: In this paper, an iterative multiple-symbol differential detection (MSDD) scheme for differential LDPC codes is considered over slow and fast Rayleigh fading channels. The metric computation algorithm and its simplified algorithm used to output soft information for MSDD are derived. Simulation results demonstrate that the bit error rate (BER) performance of the proposed system is close to that of coherent detection by extending the observation interval and iterative decoding. In addition, the simulation results show that the proposed system, which can exploit the time diversity benefit of the fast fading channels, has much better performance over fast fading channels.

## Frame Synchronization Techniques for Non-Binary LDPC Codes over GF(q)

- **Status**: ❌
- **Reason**: 비이진 GF(q) LDPC 프레임 동기화 기법 — 비이진 + ECC 디코더/구성이 아님, 제외
- **ID**: ieee:5683422
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Rodrigue Imad, Charly Poulliat, Sebastien Houcke
- **PDF**: https://ieeexplore.ieee.org/document/5683422
- **Abstract**: The problem of frame synchronization of non-binary Low-Density Parity-Check (LDPC) codes is considered in this paper. We propose two techniques of blind frame synchronization that are based on syndrome calculation over the Galois Field GF(q). While the first technique computes hard values of the syndrome, the second one deals with probabilities. Furthermore, we present in this paper a theoretical analysis on the proposed synchronization criteria. This analysis is validated by comparison to simulated results. Although non-binary LDPC codes have short lengths and their decoding is very effective even at low Signal-to-Noise Ratio (SNR), simulation results have shown that the proposed Non-Binary Soft Syndrome (NBSS) based synchronization algorithm is well adapted to such codes. The Frame Error Rate (FER) curves obtained after synchronization and decoding are very close to the perfect synchronization case.

## Generalized Sum-Product Algorithm for Joint Channel Decoding and Physical-Layer Network Coding in Two-Way Relay Systems

- **Status**: ❌
- **Reason**: 양방향 릴레이 물리계층 네트워크코딩용 일반화 SPA — 통신 응용 특이적, NAND BP에 떼어낼 ECC 기법 없음
- **ID**: ieee:5683819
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Dirk Wübben, Yidong Lang
- **PDF**: https://ieeexplore.ieee.org/document/5683819
- **Abstract**: In this paper a physical-layer network coded two-way relay system applying Low-Density Parity-Check (LDPC) codes for error correction is considered, where two sources A and B desire to exchange information with each other by the help of a relay R. The critical process in such a system is the calculation of the network-coded transmit word at the relay on basis of the superimposed channel-coded words of the two sources. For this joint channel-decoding and network-encoding task a generalized Sum-Product Algorithm (SPA) is developed. This novel iterative decoding approach outperforms other recently proposed schemes as demonstrated by simulation results.

## Short Erasure Correcting LDPC IRA Codes over GF(q)

- **Status**: ❌
- **Reason**: 비이진 GF(q) IRA erasure 코드 — 비이진 + fountain/erasure 성격, 제외
- **ID**: ieee:5683889
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Giuliano Garrammone, Balazs Matuz
- **PDF**: https://ieeexplore.ieee.org/document/5683889
- **Abstract**: This paper investigates non-binary low-density parity-check (LDPC) erasure correcting codes suitable to guarantee reliable transmission in wireless communications systems. In particular, irregular repeat-accumulate (IRA) codes are considered, characterized by linear-time encoding complexity. The performance of non-binary IRA codes is compared with their binary counterparts on the packet erasure channel (PEC), with considerable advantages for the non-binary construction. Particularly, it is illustrated that the performance of short-block-length erasure correcting IRA codes over Galois fields (GFs) of order q >; 2 approaches, under maximum-likelihood (ML) decoding, the performance of ideal maximum distance separable (MDS) codes. This is especially appealing in the context of satellite communications, where efficient codes are required to cope with small link margins.

## Getting Closer to MIMO Capacity with Non-Binary Codes and Spatial Multiplexing

- **Status**: ❌
- **Reason**: 비이진 LDPC + MIMO 공간다중화 — 비이진 + 무선 응용, 제외
- **ID**: ieee:5684077
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Stephan Pfletschinger, David Declercq
- **PDF**: https://ieeexplore.ieee.org/document/5684077
- **Abstract**: In this paper, we discuss the combination of non-binary channel coding with higher-order modulation and MIMO transmission in the form of spatial multiplexing. In addition to the benefits of non-binary LDPC codes on the AWGN channel, we identify an inherent advantage for non-binary coding in multiple antenna schemes. By comparing binary and q-ary information processing at the receiver, we highlight the intrinsic advantages of non-binary coding. A performance comparison based on simulation results shows that, at similar system complexity, non-binary information processing can actually outperform the Shannon limit of its binary counterpart.

## On Design of Doubly-Generalized LDPC Codes Based on Multi-Type Information Functions

- **Status**: ❌
- **Reason**: D-GLDPC EXIT 기반 threshold 분석(BEC) — 디코더/HW/구성 신규 이식 기법 아닌 ensemble 해석 이론
- **ID**: ieee:5684185
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Enrico Paolini, Marco Chiani, Marc P. C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/5684185
- **Abstract**: Ensemble design of low-density parity-check (LDPC) codes and their generalizations is usually performed via numerical optimization techniques, such as differential evolution, in which a threshold analysis tool is always necessary. Threshold analysis of unstructured doubly-generalized LDPC (D-GLDPC) code ensembles over the binary erasure channel (BEC) can be performed via extrinsic information transfer (EXIT) chart, exploiting the information functions and split information functions of the check and variable component codes, respectively. In this paper, multi-type information functions of linear block codes are introduced as an extension of the concept of information functions, when the bit positions are assumed to be associated with different types. It is shown how multi-type information functions (together with their split counterparts) can be exploited within an EXIT analysis approach to perform threshold analysis over the BEC of multi-edge type D-GLDPC code ensembles. The proposed technique for threshold analysis captures D-GLDPC codes based on protographs as a special case.

## Modeling, detection, and LDPC codes for bit-patterned media recording

- **Status**: ❌
- **Reason**: 비트패턴드 미디어 기록(BPMR) 2D 검출/LDPC — 자기기록 채널 특이적 검출 기법, 표준 LDPC 사용
- **ID**: ieee:5700275
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Kui Cai, Zhiliang Qin, Songhua Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/5700275
- **Abstract**: In this paper, we present a thorough and comprehensive study for bit-patterned media recording (BPMR), from a signal processing and coding perspective. We first propose a recording-physics-based generic channel model for BPMR, which includes all the major characteristics and impairments of the system. It also provides a fair basis for the performance comparison of different coding and detection schemes. We further propose various channel algorithms and techniques for BPMR, including a two-dimensional (2D) equalization scheme with one-dimensional (1D) generalized partial response (GPR) target to mitigate inter-track interference (ITI) and media noise, a maximum a posteriori (MAP) detector for BPMR with write errors, various low-density parity-check (LDPC) codes, as well as the iterative detection and decoding schemes. The corresponding performance gains are illustrated at 4Tb/in2.

## Performance Evaluation of Iterative Channel Codes for Digital Data Storage on Microfilm

- **Status**: ❌
- **Reason**: 마이크로필름 저장채널용 반복부호 성능평가 — 표준 LDPC/터보 단순 적용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:5683965
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Florian Pflug, Christoph Voges, Tim Fingscheidt
- **PDF**: https://ieeexplore.ieee.org/document/5683965
- **Abstract**: In the past few years microfilm has gained new research interest as a medium for long-term storage of digital data. This became particularly possible by recent advances in laser film recording technology. In contrast to other optical or magnetic storage media, the microfilm digital channel (MDC) still has been subject to characterization in only a few publications. In this paper we investigate iterative channel codes for the MDC, in particular low-density parity-check and turbo convolutional codes. Simulation results show that practically error-free storage can be achieved with code rates even above 0.85 on a monochrome MDC with binary amplitude-shift keying modulation.

## A multibit-per-cell memory model and nonbinary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 코드 — 비이진 LDPC 제외
- **ID**: ieee:5700272
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Seungjune Jeon, Euiseok Hwang, B. V. K. Vijaya Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/5700272
- **Abstract**: Protecting nonvolatile memory systems in harsh radiation environments encountered in space missions is important and error correcting schemes can extend the lifetime of those memory systems. For example, recent research has shown that LDPC codes can extend the lifetime of nonvolatile memory under space radiation environment more than Bose-Chaudhuri-Hocquenghem (BCH) or Reed-Solomon (RS) codes at fixed codeword error rates. However, conventional memory models assume that bit errors are independent, but multibit errors were reported in satellite experiments. Moreover, memory feature sizes are shrinking and multibit-per-cell structures are becoming standard so radiation will increasingly lead to multibit errors. For these reasons, we can expect that the bit errors in memory systems will be correlated. In this work, we develop a mathematical multibit-per-cell memory model under a radiation environment. In this memory model, bit errors are correlated and the probability of errors depends on radiation parameters and time. For correlated bit errors, nonbinary codes can be more effective than binary codes. We will demonstrate that nonbinary LDPC code can outperform conventional BCH and RS codes in a correlated multibit error environment.

## Approximation of Log-Likelihood Ratio for Wireless Channels Based on Taylor Series

- **Status**: ❌
- **Reason**: 무선 Rayleigh 페이딩 채널 LLR 근사 — 무선 채널 특이적, NAND에 떼어낼 ECC 기법 없음
- **ID**: ieee:5684360
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Reza Asvadi, Amir H. Banihashemi, Mahmoud Ahmadian-Attari
- **PDF**: https://ieeexplore.ieee.org/document/5684360
- **Abstract**: A new approach for the approximation of the channel log-likelihood ratio (LLR) for wireless channels based on Taylor series is proposed. The approximation is applied to the uncorrelated flat Rayleigh fading channel with unknown channel side information at the receiver. It is shown that the proposed approximation greatly simplifies the calculation of channel LLRs, and yet provides results almost identical to those based on the exact calculation of channel LLRs. The results are obtained in the context of iterative decoding of low-density parity-check (LDPC) codes and include threshold calculations and error rate performance of finite-length codes. Compared to the existing approximations, the proposed method is either significantly less complex, or considerably more accurate.

## Scrubbing with partial side information for radiation-tolerant memory

- **Status**: ❌
- **Reason**: 스크러빙+부분 CSI(stuck-at), BCH 기반 — 비-LDPC, 메모리 방어이나 떼어낼 LDPC 기법 없음
- **ID**: ieee:5700282
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Euiseok Hwang, Seungjune Jeon, Rohit Negi +2
- **PDF**: https://ieeexplore.ieee.org/document/5700282
- **Abstract**: Memory systems used in space applications suffer from radiation-induced errors, either temporary upsets (soft errors) or permanent defects (hard errors or stuck-at errors). Scrubbing is a method to protect memory contents by periodically decoding the stored data to correct those soft and stuck-at errors then rewriting the corrected data back into memory. However, defective cells will remain and accumulate over time. Conventional coding disregards defective cells, however this may be inefficient for memory protection in space. In this study, alternative coding schemes for scrubbing are investigated, where the channel model depends on the cell states, defective or not, and the encoder uses channel state information (CSI) or side information. At every scrubbing, the error correcting code (ECC) decoder provides partial CSI back to the encoder and the encoder uses the CSI to improve the performance of memory systems with scrubbing. Information theoretic limits of the channel with partial CSI are investigated and several coding schemes are introduced to mitigate the effects of defective cells, particularly those caused by stuck-at defects. In addition, coding schemes with partial CSI are concatenated with binary Bose-Chaudhuri-Hocquenghem (BCH) codes to protect memory contents from both soft and stuck-at errors in space radiation environments. Numerical simulation results show that scrubbing with partial CSI improves reliability over the state-agnostic approaches.

## MIMO Maximum Likelihood Soft Demodulation Based on Dimension Reduction

- **Status**: ❌
- **Reason**: MIMO ML 소프트 복조기(차원축소) — LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:5683917
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Jungwon Lee, Ji-Woong Choi, Hui-Ling Lou
- **PDF**: https://ieeexplore.ieee.org/document/5683917
- **Abstract**: This paper proposes a dimension reduction maximum likelihood (ML) soft demodulator for multiple-input multiple-output (MIMO) system. The proposed dimension reduction soft demodulator reduces the dimension of the search space for minimum Euclidean distance calculation by exploiting ML hard detection algorithms and can achieve significantly lower complexity than existing optimal soft demodulators based on exhaustive or near-exhaustive search. The dimension reduction can be realized through the use of optimum MIMO hard detectors such as a sphere decoder, resulting in optimal performance. It can also be implemented using suboptimum low-complexity MIMO hard detectors such as various conventional MIMO equalizers, further reducing the complexity with slight performance degradation.

## Compressive Data Persistence in Large-Scale Wireless Sensor Networks

- **Status**: ❌
- **Reason**: WSN 압축센싱 기반 데이터 persistence — 소스코딩/fountain 성격, 채널 ECC 아님
- **ID**: ieee:5684035
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Mu Lin, Chong Luo, Feng Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/5684035
- **Abstract**: This paper considers a large-scale wireless sensor network where sensor readings are occasionally collected by a mobile sink, and sensor nodes are responsible for temporarily storing their own readings in an energy-efficient and storage-efficient way. Existing data persistence schemes based on erasure codes do not utilize the correlation between sensor data, and their decoding ratio is always larger than one. Motivated by the emerging compressive sensing theory, we propose compressive data persistence which simultaneously achieves data compression and data persistence. In the development of compressive data persistence scheme, we design a distributed compressive sensing encoding approach based on Metropolis-Hastings random walk. When the maximum step of random walk is 400, our proposed scheme can achieve a decoding ratio of 0.36 for 10%-sparse data. We also compare our scheme with a state-of-the-art Fountain code based scheme. Simulation shows that our scheme can significantly reduce the decoding ratio by up to 63%.

## Frequency-Domain Oversampling for Zero-Padded OFDM in Underwater Acoustic Communications

- **Status**: ❌
- **Reason**: 수중음향 OFDM 주파수 오버샘플링, LDPC 무관 통신 응용
- **ID**: ieee:5683290
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Zhaohui Wang, Shengli Zhou, Georgios B. Giannakis +2
- **PDF**: https://ieeexplore.ieee.org/document/5683290
- **Abstract**: Although time-domain oversampling of the received baseband signal is common for single-carrier transmissions, the counterpart of frequency-domain oversampling is rarely used for multicarrier transmissions. In this paper, we explore frequency-domain oversampling to improve the system performance of zero-padded OFDM transmissions over underwater acoustic channels with large Doppler spread. We use a signal design that enables separate sparse channel estimation and data detection, rendering a low complexity receiver. Based on both simulation and experimental results, we observe that the receiver with frequency-domain oversampling outperforms the conventional one considerably in channels with moderate and large Doppler spreads, and the gain increases as the Doppler spread increases. Although a raised-cosine pulse-shaping window can be used to improve the system performance relative to a rectangular window at the expense of data rate reduction, the performance gain is much less than that brought by frequency-domain oversampling in the considered OFDM system for Doppler spread channels.

## Contention Resolution Diversity Slotted ALOHA with Variable Rate Burst Repetitions

- **Status**: ❌
- **Reason**: CRDSA 슬롯 ALOHA 간섭제거의 그래프부호 유추 — 무선 MAC 응용, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:5684049
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/5684049
- **Abstract**: Contention resolution diversity slotted ALOHA is a simple but effective improvement of slotted ALOHA. It relies on MAC bursts repetition and on interference cancellation to increase the throughput of a classic slotted ALOHA access scheme. This improvement permits to achieve a throughput up to T ≃ 0.55, whereas slotted ALOHA is capable of providing T ≃ 0.37. In this paper we show that the iterative interference cancellation process used in contention resolution diversity slotted ALOHA can be described by a bipartite graph. Such representation permits to establish a bridge between the iterative interference cancellation process and the iterative erasure recovery process of graph-based codes. Exploiting this analogy, we show how a higher throughput (close to T ≃ 0.9) can be achieved by selecting variable burst repetition rates, leading to irregular graphs, according to given probability distributions. A framework for the probability distribution optimization is provided as well. Simulation results including the actual interference cancellation mechanism confirm the high efficiency of the proposed approach.

## Raptor code for wireless ad hoc vehicular safety broadcast

- **Status**: ❌
- **Reason**: 차량 V2V Raptor(fountain) 코드 응용 — 비-LDPC, erasure/fountain 응용
- **ID**: ieee:5700102
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Nor Fadzilah Abdullah, Robert J. Piechocki, Angela Doufexi
- **PDF**: https://ieeexplore.ieee.org/document/5700102
- **Abstract**: This paper proposes an implementation of systematic Raptor code in an ad hoc V2V (vehicular-to-vehicular) environment for post-crash safety broadcast. This is to address the latency problem caused by use of repetition code in a high speed vehicular environment for time-sensitive safety applications. The highly dynamic topology and challenging RF behavior of vehicular networks necessitate the use of a robust error control mechanism even with the use of spatial diversity techniques such as STBC-MIMO scheme. A cross-layer simulator model is used to evaluate the delay performance of Raptor codes against a low complexity repetition code. The numerical analysis demonstrates that the end-to-end delay performance is significantly reduced when Raptor codes are used, especially at higher distances from the source node. This is true in the case of single antenna as well as multiple antenna schemes.

## Adaptive Wyner-Ziv Decoding Using Particle-Based Belief Propagation

- **Status**: ❌
- **Reason**: 비이진 소스 대상 Wyner-Ziv/Slepian-Wolf 소스코딩 + 비이진 BP, 채널 ECC 아님, 제외
- **ID**: ieee:5683748
- **Type**: conference
- **Published**: 6-10 Dec. 
- **Authors**: Shuang Wang, Lijuan Cui, Samuel Cheng
- **PDF**: https://ieeexplore.ieee.org/document/5683748
- **Abstract**: In this paper we propose an adaptive Wyner-Ziv (WZ) coding scheme for non-binary correlated sources with side information at the decoder. At the encoder, a low density parity check (LDPC) code is employed to implement Slepian-Wolf (SW) coding for each bit-plane independently. The joint "source-channel" decoder, which combines SW decoding and dequantizing in a single step, preserves the symbol-domain correlation and decreases the distortion. Moreover, the incorporation of particle-based belief propagation (BP) in the decoder can extend the scheme to perform an online estimation of the correlation and enhance the BP decoding performance simultaneously. Our proposed framework is universal and can be applied to any parametric correlation model.

## Comparative performance evaluation of LDPC coded and turbo coded OFDM systems in SUI multipath channel models

- **Status**: ❌
- **Reason**: LDPC vs turbo OFDM 성능 비교 평가만, 표준 부호 사용·떼어낼 신규 디코더/HW/구성 기법 없음
- **ID**: ieee:5771165
- **Type**: conference
- **Published**: 5-8 Dec. 2
- **Authors**: M. Shahzad Anwar, M. Zeeshan, Saira Aslam +2
- **PDF**: https://ieeexplore.ieee.org/document/5771165
- **Abstract**: In this research paper, we carry out comparative performance evaluation of Low Density Parity- Check (LDPC) coded and Turbo coded orthogonal frequency division multiplexing (OFDM) systems by varying a number of parameters/factors including channel types, data block size, and number of decoding iterations. OFDM possesses the ability to counter sever channel conditions if coded with a suitable error correction scheme. LDPC coding is appearing as most promising combination in upcoming communication standards. The error rate behavior of LDPC coded OFDM system has been compared with its toughest competitor i.e. Turbo Coded OFDM system, especially on six Stanford University Interim (SUI) multipath channel models. Their computational complexities have also been worked out to evaluate the latency, efficiency, cost effect and ease of implementation.

## Implementation of DTTB LDPC encoder based on FPGA

- **Status**: ❌
- **Reason**: DTTB QC-LDPC 인코더 FPGA 구현, 표준 QC-LDPC 생성행렬 단순 구현으로 신규 기여 미흡하나 HW 인코더이므로 애매-그래도 표준 재사용 수준
- **ID**: ieee:5690219
- **Type**: conference
- **Published**: 4-6 Dec. 2
- **Authors**: Zhou Wen, Ye Yu-huang, Su Kai-Xiong
- **PDF**: https://ieeexplore.ieee.org/document/5690219
- **Abstract**: QC-LDPC code is used as the inner channel code in DTTB. In this paper, FPGA implementation of QC-LDPC code based on SRAA is introduced according to the features of QC-LDPC generator matrix. At the same time, the results are verified in the Altera Stratix device.

## A joint source-channel coding scheme for unequal protection of SVC video using LDPC codes

- **Status**: ❌
- **Reason**: SVC 비디오 JSCC 부등보호, LDPC가 베이스라인 도구일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:5696040
- **Type**: conference
- **Published**: 3-5 Dec. 2
- **Authors**: Xiangxue Wu, Xiaofeng Li, Jin Xu +1
- **PDF**: https://ieeexplore.ieee.org/document/5696040
- **Abstract**: This paper proposes a joint source-channel coding (JSCC) scheme for unequal protection of SVC video coding over packet loss channels. The SVC sub-streams with different importance are unequally protected using Low Density Parity Check (LDPC) codes with five different coding rates respectively. The proposed JSCC scheme for SVC can optimize the rate allocation between source coding and channel coding according to the characteristic of SVC, the actual bandwidth of current wireless channel and the average rate of packet loss. Simulation results show that the proposed JSCC scheme can adapt the changing of network condition and achieve good reconstructed video quality at the receiver.

## Design of Concatenation of Fountain and Non-Binary LDPC Codes for Satellite Communications

- **Status**: ❌
- **Reason**: Fountain+Non-binary LDPC concatenation, 위성통신 — 비이진 LDPC+fountain, 제외
- **ID**: ieee:5678313
- **Type**: conference
- **Published**: 25-26 Dec.
- **Authors**: Lei Wen, Jing Lei, Ji bo Wei
- **PDF**: https://ieeexplore.ieee.org/document/5678313
- **Abstract**: This paper researches channel coding for satellite communications. Fountain codes and Non-binary LDPC codes are introduced, including their encoding and decoding algorithm. Taking advantage of similar characteristic of sparse graph codes, concatenation of fountain codes and Non-binary LDPC codes is proposed. Simulation result shows good performance of the concatenated codes. This work gives us some inspirations for deep space applications.

## Performance Analysis of PA Coded Pulse-Position Modulation for Space Optical Communications

- **Status**: ❌
- **Reason**: PA(product accumulate) 부호+PPM, 비-LDPC, 광통신 특이적 — 제외
- **ID**: ieee:5678325
- **Type**: conference
- **Published**: 25-26 Dec.
- **Authors**: Jianzhong Guo, Chongtao Zou, Yukang Tian +1
- **PDF**: https://ieeexplore.ieee.org/document/5678325
- **Abstract**: A scheme of PA (product accumulate) code employing pulse-position modulation is investigated for space optical communications. Over a Poisson channel, simulation is conducted. Simulation results show that the PA code has excellent BER (bit error rate) and low error floor. In addition, EXIT (extrinsic information transfer) chart is employed to analyze the BER performance and error floor for PA code. The results are in accord with that of the simulations.

## Design and Implementation of LDPC Codec for Aircraft Control and Simulation

- **Status**: ❌
- **Reason**: 위성/항공통신용 LDPC codec FPGA 구현이나 시스템 통합/통신 응용 위주, 떼어낼 신규 디코더·코드설계·HW 아키텍처 기여 불명확
- **ID**: ieee:5945088
- **Type**: conference
- **Published**: 24-26 Dec.
- **Authors**: Jinqing Qi, Jingbin Zhang, Xiaohong Ma +2
- **PDF**: https://ieeexplore.ieee.org/document/5945088
- **Abstract**: The system is based on the platform of Altera DE2 SOPC and RS232 interface using a wireless channel environment. NIOS_II processor and FPGA hardware co-design methodology is adopted. The soft-core processor asks for a request to send codec allocation and other operations and FPGA is responsible for the major hardware codec. The LDPC codec system can achieve a two-way communication with flexible configuration, which is particularly suitable for satellite communications.

## Multiple Bit Error Detection and Correction in GF Arithmetic Circuits

- **Status**: ❌
- **Reason**: GF(2^m) 암호 곱셈기 fault tolerance에 LDPC 패리티예측 사용; 채널 ECC 디코더/구성 아님, RS+LDPC 회로 오류검출
- **ID**: ieee:5715158
- **Type**: conference
- **Published**: 20-22 Dec.
- **Authors**: J. Mathew, S. Banerjee, P. Mahesh +3
- **PDF**: https://ieeexplore.ieee.org/document/5715158
- **Abstract**: This paper presents a design technique for multiple bit error correctable (fault tolerant) polynomial basis (PB) multipliers over GF(2^m). These multipliers are the building blocks in certain types of cryptographic hardware, e.g. the Elliptic Curve Crypto systems (ECC). One of the drawbacks in the existing techniques is their inability to correct multiple bit errors at the outputs. Also, much attention has been given to error detection, as opposed to error correction. However, owing to possible security threats induced by soft or transient faults in cryptographic hardware, in certain cases multiple bit error correction, as a way of mitigating attacks, is more important than detection. To this end, we use multiple parity predictions to detect multiple errors based on popular error correcting codes. First, we present a multiple error detection scheme using Low Density Parity Check Codes (LDPC). The expressions for the parity prediction are derived from the input operands, and are based on the primitive polynomials of the fields. For multiple bit error correction we use Reed Solomon codes. Comparison with traditional techniques shows improved area and power performance.

## Cooperative communication in wireless sensor network using low density parity check codes

- **Status**: ❌
- **Reason**: WSN 협력통신 LDPC 적용 BER 분석, 표준 LDPC 응용일 뿐 떼어낼 신규 기법 없음
- **ID**: ieee:5700780
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Mohammad Rakibul Islam, Md. Ashraful Hoque, Kazi Khairul Islam +1
- **PDF**: https://ieeexplore.ieee.org/document/5700780
- **Abstract**: Energy efficient data transmission is one of the key factors for energy constraint wireless sensor network (WSN). Cooperative communication explores the energy efficient wireless communication schemes between multiple sensors and data gathering node (DGN). In this paper, an energy efficient cooperative technique is proposed considering low density parity check (LDPC) codes. The result shows that the proposed cooperative communication outperforms SISO transmission when the error correction code is considered. Bit error rate (BER) analysis is also performed. In this work, it shows that the lower encoding rate offers better error characteristics for same signal to noise ratio (SNR)

## Performance analysis of a LDPC coded multiple input/multiple output free-space optical system with Q-ary pulse-position modulation

- **Status**: ❌
- **Reason**: FSO Q-ary PPM LDPC 코딩 BER 성능평가, 표준 LDPC 응용일 뿐 신규 디코더·구성 없음
- **ID**: ieee:5700707
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Bobby Barua, S. P. Majumder
- **PDF**: https://ieeexplore.ieee.org/document/5700707
- **Abstract**: The use of multiple laser transmitters combined with multiple photo detectors has the potential for combating fading effects on turbulent optical channels. In this paper, an analytical approach is presented to evaluate the bit error rate performance of a free space optical link using LDPC coded Q-ary optical PPM over atmospheric turbulence channel. Performance results are evaluated for multiple-laser and multiple photo-detector combination without and with LDPC code to combat the effect of atmospheric turbulence. The performance results are evaluated in terms of bit error rate (BER) and coding gain for several system parameters. It is found that LDPC coded system provides significant coding gain of 10 to 20dB over uncoded system can be evaluated at BER 10-12 for multiple source and photo-detector combinations.

## Selection of error control/correction codes in wireless sensor network

- **Status**: ❌
- **Reason**: WSN용 ECC(RS코드) 선택 연구, 결론도 RS(31,21); LDPC 디코더/구성 기여 없음
- **ID**: ieee:5700783
- **Type**: conference
- **Published**: 18-20 Dec.
- **Authors**: Mohammad Rakibul Islam
- **PDF**: https://ieeexplore.ieee.org/document/5700783
- **Abstract**: Error control coding (ECC) is a classic approach used to increase link reliability and lower the required transmitted power. It provides coding gain, resulting in transmitter energy savings, at the cost of added decoder power consumption. But the choice of ECC is very critical in the case of wireless sensor network (WSN). Since the WSNs are energy constraint in nature, both the BER and power consumption has to be taken into count. This paper develops a step by step approach in finding suitable error control codes for WSNs. Several simulations are taken considering different error control codes and the result shows that the RS(31,21) fits both in BER and power consumption criteria.

## Iterative multi-channel equalization and LDPC decoding for underwater acoustic coherent communications

- **Status**: ❌
- **Reason**: 수중음향 통신 turbo equalization+LDPC 반복복호, 채널 등화기 응용 특이적이라 NAND 이식 기법 없음
- **ID**: ieee:5689737
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Liang Zhao, Jianhua Ge
- **PDF**: https://ieeexplore.ieee.org/document/5689737
- **Abstract**: Multi-Channel adaptive decision feedback equalizer (MC-ADFE) is a main method to overcome multi-path distortion and eliminate Inter-Symbol Interference (ISI) for underwater acoustic channel. LDPC codes are capacity achieving codes, which can provide considerable coding gain. In this paper, the turbo theory is applied to form iterative multi-channel adaptive decision feedback equalizer (MC-ADFE) and LDPC decoder. In iterative equalization and decoding algorithm (IED), the MC-ADFE and LDPC decoder exchange soft information in an iterative manner, which can enhance the equalizer performance using significant decoding gain. The simulation results show that proposed system scheme can improve the performance of equalizer and get considerable coding gain. So, the performance of underwater acoustic communication system can be improved greatly.

## Low-Density Parity-Check codes for asymmetric distributed source coding

- **Status**: ❌
- **Reason**: 분산소스코딩(DSC, Slepian-Wolf) 소스코딩 응용으로 채널 ECC 아님, 떼어낼 신규 기법 없음
- **ID**: ieee:5689658
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Jeffrey J. Micallef, Reuben A. Farrugia, Carl J. Debono
- **PDF**: https://ieeexplore.ieee.org/document/5689658
- **Abstract**: Low-Density Parity-Check (LDPC) codes achieve good performance, tending towards the Slepian-Wolf bound, when used as channel codes in Distributed Source Coding (DSC). Most LDPC codes found in literature are designed assuming random distribution of transmission errors. However, certain DSC applications can predict the error location within a certain level of accuracy. This feature can be exploited in order to design application specific LDPC codes to enhance the performance of traditional LDPC codes. This paper proposes a novel architecture for asymmetric DSC where the encoder is able to estimate the location of the errors within the side information. It then interleaves the bits having a high probability of error to the beginning of the codeword. The LDPC codes are designed to provide a higher level of protection to the front bits. Simulation results show that correct localization of errors pushes the performance of the system on average 13.3% closer to the Slepian-Wolf bound, compared to the randomly constructed LDPC codes. If the error localization prediction fails, such that the errors are randomly distributed, the performance is still in line with that of the traditional DSC architecture.

## Downlink multimedia services in CDMA network with fountain code and soft handoff

- **Status**: ❌
- **Reason**: CDMA fountain/Raptor+LDPC erasure 채널 성능분석, 응용 특이적·떼어낼 기법 없음
- **ID**: ieee:5712720
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Sanjay Dhar Roy, Priyobrata Parida, Sumit Kundu
- **PDF**: https://ieeexplore.ieee.org/document/5712720
- **Abstract**: In this paper, we propose a framework for analyzing downlink performance of cellular CDMA network without considering retransmission protocol in MAC layer. More specifically, we develop a simulation testbed for analyzing broadcast performance of WCDMA network in presence of both PHY layer and application layer forward error correction (FEC) codes only. In physical layer, low density parity check (LDPC) code is considered. Raptor code is considered as application layer FEC. Packet data performance is estimated in terms of file delivery failure probability in an erasure channel. Tradeoff between Raptor code and LDPC code is also shown.

## A novel downlink signaling method for OFDM based cognitive radio system

- **Status**: ❌
- **Reason**: OFDM 인지무선 다운링크 시그널링 응용, LDPC는 부수 언급, 떼어낼 ECC 기법 없음
- **ID**: ieee:5689724
- **Type**: conference
- **Published**: 17-19 Dec.
- **Authors**: Haigang Zhang, Dongfeng Yuan
- **PDF**: https://ieeexplore.ieee.org/document/5689724
- **Abstract**: The Cognitive radio (CR) is an efficient approach for future wireless communication system. In CR system the rental users can identify the spectrum information and access the unoccupied spectrum hole under the interference constraint to the licensed users. The spectrum is allocated and utilized dynamically nearly without adjusting of existing systems. Orthogonal frequency division multiplexing (OFDM) is a good candidate technology for rental users in CR system especially in the system with a base station. The spectrum assignment can be realized easily through sub-carrier allocation. The interference constraint can be fulfilled by sub-carrier and power allocation. The resource allocation scheme should vary corresponding to the variation of the environment. So the signaling method takes very important role in the resource allocation which guarantees the realization and efficiency. Traditional signaling message is usually transmitted through high layer packet. It is error-prone and low efficient. In this paper a novel downlink signaling method for OFDM based CR system is proposed. It is based on low density parity check (LDPC) codes and constellation rotation. It can transmit the sub-carrier allocation message reliably without extra difficulty for the resource allocation scheme. The method also adapts to different transmit power on sub-carrier.

## Wavelength/Time orthogonal codes with FEC offer dual advantage

- **Status**: ❌
- **Reason**: FO-CDMA 광통신 W/T 코드+FEC, LDPC 아님·떼어낼 디코더/구성 기법 없음
- **ID**: ieee:5706107
- **Type**: conference
- **Published**: 14-16 Dec.
- **Authors**: E. S. Shivaleela
- **PDF**: https://ieeexplore.ieee.org/document/5706107
- **Abstract**: To meet the growing demands of the high data rate applications, suitable asynchronous schemes such as Fiber-Optic Code Division Multiple Access (FO-CDMA) are required in the last mile. FO-CDMA scheme offers potential benefits and at the same time it faces many challenges. Wavelength/Time (W/T) 2-D codes for use in FO-CDMA, can be classified mainly into two types: 1) hybrid codes and 2) matrix codes, to reduce the 'time' like property, have been proposed. W/T single-pulse-per-row (SPR) are energy efficient codes as this family of codes have autocorrelation sidelobes of '0', which is unique to this family and the important feature of the W/T multiple-pulses-per-row (MPR) codes is that the aspect ratio can be varied by trade off between wavelength and temporal lengths. These W/T codes have improved cardinality and spectral efficiency over other W/T codes and at the same time have lowest crosscorrelation values. In this paper, we analyze the performances of the FO-CDMA networks using W/T SPR codes and W/T MPR codes, with and without forward error correction (FEC) coding and show that with FEC there is dual advantage of error correction and reduced spread sequence length.

## Efficient BER computation of LDPC coded SC/MRC systems over Rayleigh fading

- **Status**: ❌
- **Reason**: Rayleigh fading SC/MRC LDPC의 BER 계산식(가우시안 근사) — 무선응용 성능분석, 떼어낼 디코더/HW/구성 신규 기법 없음
- **ID**: ieee:5709680
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Beng Soon Tan, Kwok Hung Li, Kah Chan Teh
- **PDF**: https://ieeexplore.ieee.org/document/5709680
- **Abstract**: Selection combining cascaded with maximum-ratio combining (SC/MRC), which is particularly useful when site diversity is available, combined with low-density parity-check (LDPC) codes is able to combat the effects of fading. The bit-error rate (BER) expressions of uncoded SC/MRC and SC/MRC with LDPC codes over an independent and identically distributed Rayleigh-fading channel are derived based on the Gaussian approximation approach. These expressions are also applicable to the selection combining and maximum-ratio combining as special cases. The derived expressions are in good agreement with simulation results and approach the density evolution (DE) thresholds. These expressions are able to achieve a significant reduction in computational time with a reasonable accuracy for analyzing the BER performance as compared to simulations and DE.

## Another approach to save energy in OFDM systems

- **Status**: ❌
- **Reason**: fountain code 기반 OFDM ADC 에너지 절감, 떼어낼 바이너리 LDPC ECC 기법 없음
- **ID**: ieee:5709669
- **Type**: conference
- **Published**: 13-15 Dec.
- **Authors**: Xiaoying Shao, Cornelis H. Slump
- **PDF**: https://ieeexplore.ieee.org/document/5709669
- **Abstract**: In this paper, we propose an energy-efficient error correction scheme to lower the power consumption of the ADCs in the OFDM system. The proposed opportunistic error correction scheme is based on resolution adaptive ADCs and fountain codes. The key idea is to reduce the dynamic range of the channel by discarding part of the channel in deep fading. Correspondingly, the power consumption in ADCs can be decreased. In our approach, each sub-carrier transports a fountain-encoded packet. The receiver only decodes fountain-encoded packets with high SNR. Others are discarded. To compensate for the discarded packets, a high order modulation is used. The new error correction layer does not require perfect channel knowledge, so it can be applied in a real system. With our approach and 16-QAM, the energy consumption in ADCs is reduced by around 73% with non-perfect channel estimation comparing to the traditional IEEE 802.11a system under the same channel conditions and throughput.

## A new parallel algorithm for full-digital phase-locked loop for high-throughput carrier and timing recovery systems

- **Status**: ❌
- **Reason**: 디지털 PLL 캐리어/타이밍 복원 병렬 알고리즘, LDPC와 무관
- **ID**: ieee:5724722
- **Type**: conference
- **Published**: 12-15 Dec.
- **Authors**: Keitarou Kondou, Makoto Noda
- **PDF**: https://ieeexplore.ieee.org/document/5724722
- **Abstract**: A parallel algorithm for a full-digital phase-locked loop for high-throughput adaptive carrier and timing recovery systems has been developed. The proposed algorithm separately estimates an initial phase and a period fluctuation for a sampled signal, whereas they are simultaneously estimated by conventional algorithms. The new algorithm increases the pull-in frequency range by 1.6 times and reduces the convergence time by 41 %, compared to those of conventional parallel algorithms. Hardware for a carrier and timing recovery system utilizing interpolation with the maximum bit rate of 6.9 Gb/s was designed using 40 nm CMOS technology, resulting in a practical cell area of 0.081 μm2 for a 60 GHz millimeter-wave-based wireless communication application.

## A BCH Code with the Distance 11 for Sensornets

- **Status**: ❌
- **Reason**: BCH 부호 구성(센서넷), 비-LDPC 부호로 제외
- **ID**: ieee:5696369
- **Type**: conference
- **Published**: 11-14 Dec.
- **Authors**: Gao-chang Zhao, Xiao-lin Yang
- **PDF**: https://ieeexplore.ieee.org/document/5696369
- **Abstract**: Many application scenarios have been revealed with Sensornets. An Error Correcting Code (ECC) will be advantageous to communications in these applications. With the different expecting on efficiency, security, usability, etc, different codes have been constructed for various purposes. The methods based on algebra theory can work well for constructing simple and usability codes. The theory of algebraic geometry can help construct more complex codes with different properties. With the applications of these codes, it is convenient to arrive the purpose in digital communications.
