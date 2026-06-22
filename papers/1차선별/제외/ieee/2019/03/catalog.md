# IEEE Xplore — 2019-03


## LDPC Code Design for Fading Interference Channels

- **Status**: ❌
- **Reason**: 페이딩 간섭채널용 LDPC 코드설계(Han-Kobayashi/EXIT) — 무선 응용 특이적 차수분포 설계, NAND 이식할 신규 디코더·HW 없음
- **ID**: ieee:8606262
- **Type**: journal
- **Published**: March 2019
- **Authors**: Mahdi Shakiba-Herfeh, A. Korhan Tanc, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8606262
- **Abstract**: We focus on the two-user Gaussian interference channel (IC) with fading and study implementation of different encoding/decoding schemes with low-density parity-check (LDPC) codes for both quasi-static and fast fading scenarios. We adopt Han-Kobayashi encoding, derive stability conditions on the degree distributions of LDPC code ensembles, and obtain explicit and practical code designs. In order to estimate the decoding thresholds, a modified form of the extrinsic information transfer chart analysis based on binary erasure channel approximation for the incoming messages from the component LDPC decoders to state nodes is developed. The proposed code design is employed in several examples for both fast and quasi-static fading cases. Comprehensive set of examples demonstrate that the designed codes perform close to the achievable information theoretic limits. Furthermore, multiple antenna transmissions employing the Alamouti scheme for fading ICs are studied, a special receiver structure is developed, and specific codes are explored. Finally, advantages of the designed codes over point-to-point optimal ones are demonstrated via both asymptotic and finite block length simulations.

## Performance Analysis of LDPC-BICM System Based on Gaussian Approximation

- **Status**: ❌
- **Reason**: LDPC-BICM 시스템 성능분석(가우시안 근사 밀도진화) — 무선 변조 응용 특이적, 새 디코더·구성·HW 기여 없음
- **ID**: ieee:8566157
- **Type**: journal
- **Published**: March 2019
- **Authors**: Genning Zhang, Yin Xu, Dazhi He +2
- **PDF**: https://ieeexplore.ieee.org/document/8566157
- **Abstract**: In this paper, we propose a performance analysis algorithm of low density parity check-bit interleaved coded modulation (LDPC-BICM) system. First, we introduce the Gaussian mixture approximation method of the LLR messages output from the demodulator over the AWGN channel. Then, we analyze the density evolution based on these Gaussian mixture approximation LLR messages. During the analysis, the Gaussian approximation is applied to simplify the calculation. Some LDPC-BICM systems (which are adopted by ATSC3.0 standard) are used to evaluate the proposed algorithm. We also employ the actual performances and the thresholds obtained by the multi-edge type (MET) discretized density evolution algorithm as the references. The simulation results prove that our proposed algorithm can work well in most cases. Furthermore, the proposed algorithm is simpler than the MET algorithm because of the Gaussian or Gaussian mixture approximations.

## Multiset-Partition Distribution Matching

- **Status**: ❌
- **Reason**: 분포정합(distribution matching)/확률적 진폭쉐이핑 — LDPC ECC 아니고 떼어낼 디코더·코드설계 기법 없음
- **ID**: ieee:8533438
- **Type**: journal
- **Published**: March 2019
- **Authors**: Tobias Fehenberger, David S. Millar, Toshiaki Koike-Akino +2
- **PDF**: https://ieeexplore.ieee.org/document/8533438
- **Abstract**: Distribution matching is a fixed-length invertible mapping from a uniformly distributed bit sequence to shaped amplitudes and plays an important role in the probabilistic amplitude shaping framework. With conventional constant-composition distribution matching (CCDM), all output sequences have identical composition. In this paper, we propose multiset-partition distribution matching (MPDM), where the composition is constant over all output sequences. When considering the desired distribution as a multiset, MPDM corresponds to partitioning this multiset into equal-sized subsets. We show that MPDM allows addressing more output sequences and, thus, has a lower rate loss than CCDM in all nontrivial cases. By imposing some constraints on the partitioning, a constructive MPDM algorithm is proposed which comprises two parts. A variable-length prefix of the binary data word determines the composition to be used, and the remainder of the input word is mapped with a conventional CCDM algorithm, such as arithmetic coding, according to the chosen composition. Simulations of 64-ary quadrature amplitude modulation over the additive white Gaussian noise channel demonstrate that the block-length saving of MPDM over CCDM for a fixed gap to capacity is approximately a factor of 2.5-5 at medium to high signal-to-noise ratios.

## A Key Recovery Reaction Attack on QC-MDPC

- **Status**: ❌
- **Reason**: QC-MDPC 암호 키복구 공격(보안). 디코딩 실패 활용 공격이라 ECC 디코더/구성 기여 아님, 원칙 제외.
- **ID**: ieee:8502112
- **Type**: journal
- **Published**: March 2019
- **Authors**: Qian Guo, Thomas Johansson, Paul Stankovski Wagner
- **PDF**: https://ieeexplore.ieee.org/document/8502112
- **Abstract**: Algorithms for secure encryption in a post-quantum world are currently receiving a lot of attention in the research community. One of the most promising such algorithms is the code-based scheme called QC-MDPC, which has excellent performance and a small public key size. In this paper, we present a very efficient key recovery attack on the QC-MDPC scheme using the fact that decryption uses an iterative decoding step, and this can fail with some small probability. We identify a dependence between the secret key and the failure in decoding. This can be used to build what we refer to as a distance spectrum for the secret key, which is the set of all distances between any two ones in the secret key. In a reconstruction step, we then determine the secret key from the distance spectrum. The attack has been implemented and tested on a proposed instance of QC-MDPC for 80-bit security. It successfully recovers the secret key in minutes. A slightly modified version of the attack can be applied on proposed versions of the QC-MDPC scheme that provides IND-CCA security. The attack is a bit more complex in this case, but still very much below the security level. The reason why we can break schemes with proved CCA security is that the model for these proofs typically does not include the decoding error possibility. At last, we present several algorithms for key reconstruction from an empirical distance spectrum. We first improve the naïve algorithm for key reconstruction by a factor of about 3 0000, when the parameters for 80-bit security are implemented. We further develop the algorithm to deal with errors in the distance spectrum. This ultimately reduces the requirement on the number of ciphertexts that need to be collected for a successful key recovery.

## Key Technologies and Measurements for DTMB-A System

- **Status**: ❌
- **Reason**: DTMB-A 지상파 방송 시스템 표준 분석. LDPC 부수 언급, 떼어낼 신규 디코더/구성 없음.
- **ID**: ieee:8368065
- **Type**: journal
- **Published**: March 2019
- **Authors**: Jian Song, Chao Zhang, Kewu Peng +8
- **PDF**: https://ieeexplore.ieee.org/document/8368065
- **Abstract**: Digital terrestrial television multimedia broadcasting-advanced (DTMB-A), the new digital terrestrial television broadcasting (DTTB) system proposed by China, has been accepted by International Telecommunications Union as the international DTTB standard in July, 2015. By adopting several advanced technologies, such as near-capacity channel coding and modulation as well as improved frame structure, DTMB-A can provide faster system synchronization, higher receiving sensitivity, better performance against multipath effect, higher spectrum efficiency, and the flexibility for future extension, compared with its previous generation, DTMB system. This paper provides the technical analyses on the physical layer specifications of DTMB-A system in detail, together with the discussion on the key technologies adopted. Laboratory test and field trial results are also given which demonstrate that DTMB-A can offer excellent overall system performance for both fixed and mobile receptions under complicated terrestrial broadcasting conditions, and is capable of supporting multiple services with different quality of service requirements.

## Performance of Interleaved Block Codes With Burst Errors

- **Status**: ❌
- **Reason**: 인터리브드 블록부호 버스트오류 성능 이론분석. LDPC 아닌 일반 블록부호, 디코더/HW/구성 기여 없음.
- **ID**: ieee:8464100
- **Type**: journal
- **Published**: March 2019
- **Authors**: Roy D. Cideciyan, Simeon Furrer, Mark A. Lantz
- **PDF**: https://ieeexplore.ieee.org/document/8464100
- **Abstract**: A Gilbert-Elliott channel for symbol errors is considered to analyze the performance of interleaved error correction codes with a fixed block size in the presence of burst errors. The proposed channel model for symbol errors is based on a simplified Gilbert channel for bit errors, which enables direct comparisons of the performance of block codes with different symbol sizes. The autocorrelation function between two erroneous symbols within an interleaved codeword is computed. An exact expression for the codeword-error probability is derived from the symbol-based channel model. A tight lower bound on the codeword-error probability and error floors, which are observed when the average raw bit-error rate is low, are analyzed using the bit-based channel model.

## Learning Mixtures of Sparse Linear Regressions Using Sparse Graph Codes

- **Status**: ❌
- **Reason**: sparse graph code로 sparse linear regression 추정. 채널 ECC 아닌 통계추론 응용, 떼어낼 LDPC 디코더 없음.
- **ID**: ieee:8429915
- **Type**: journal
- **Published**: March 2019
- **Authors**: Dong Yin, Ramtin Pedarsani, Yudong Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8429915
- **Abstract**: In this paper, we consider the mixture of sparse linear regressions model. Let β(1), . . ., β(L) ∈ ℂn be L unknown sparse parameter vectors with a total of K non-zero elements. Noisy linear measurements are obtained in the form yi = xiH β(ℓi) + wi, each of which is generated randomly from one of the sparse vectors with the label ℓi unknown. The goal is to estimate the parameter vectors efficiently with low sample and computational costs. This problem presents significant challenges as one needs to simultaneously solve the demixing problem of recovering the labels ℓi as well as the estimation problem of recovering the sparse vectors β(ℓ). Our solution to the problem leverages the connection between modern coding theory and statistical inference. We introduce a new algorithm, MixedColoring, which samples the mixture strategically using query vectors xi constructed based on ideas from sparse graph codes. Our novel code design allows for both efficient demixing and parameter estimation. To find K non-zero elements, it is clear that we need at least Θ(K) measurements, and thus the time complexity is at least (K). In the noiseless setting, for a constant number of sparse parameter vectors, our algorithm achieves the order-optimal sample and time complexities of Θ(K). In the presence of Gaussian noise,1 for the problem with two parameter vectors (i.e., L = 2), we show that the Robust Mixed-Coloring algorithm achieves near-optimal Θ(K polylog(n)) sample and time complexities. When K = O(nα) for some constant α ∈ (0, 1) (i.e., K is sublinear in n), we can achieve sample and time complexities both sublinear in the ambient dimension. In one of our experiments, to recover a mixture of two regressions with dimension n = 500 and sparsity K = 50, our algorithm is more than 300 times faster than EM algorithm, with about one third of its sample cost.

## FPGA Implementation of FEC Encoder with BCH & LDPC Codes for DVB S2 System

- **Status**: ❌
- **Reason**: DVB-S2용 BCH+LDPC FEC 인코더 FPGA 구현, 인코더만이고 표준 부호 단순 구현이라 새 디코더/구성 기여 없음
- **ID**: ieee:8711664
- **Type**: conference
- **Published**: 7-8 March 
- **Authors**: Durga Digdarsini, Deepak Mishra, Sanjay Mehta +1
- **PDF**: https://ieeexplore.ieee.org/document/8711664
- **Abstract**: This paper gives the design and implementation of Xilinx FPGA based Forward Error Correction (FEC) encoder for DVB S2 system which includes BCH code followed by LDPC code and finally bit mapped to constellation for QPSK modulation. DVB-S2 FEC: ($\mathbf{n}=64800,\ \mathbf{k}=32400$) rate 1/2 code, with QPSK modulation scheme is considered as target for FPGA implementation. The architecture in this design efficiently uses pipeline technique along with parallel processing to optimize the hardware resources and overall latency, to accomplish FEC encoding for DVB S2 system. Coding is completed in Verilog HDL with Xilinx Virtex6 XC6VLX240T FPGA as target for hardware realization and QuestaSim simulator is used to complete the functional simulation.

## Nonbinary Polar Coding for Multilevel Modulation

- **Status**: ❌
- **Reason**: 비이진 polar 부호화; 비-LDPC이며 비이진, 부호 비의존적 이식 디코더 기법 없음
- **ID**: ieee:8696792
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Semih Cayci, Toshiaki Koike-Akino, Ye Wang
- **PDF**: https://ieeexplore.ieee.org/document/8696792
- **Abstract**: We investigate nonbinary polar-coded modulations, which achieve a significant performance gain of at least 1 dB compared to binary counterparts at a short block-length of 2048 bits.

## Partition-Based Probabilistic Shaping for Fiber-Optic Communication Systems

- **Status**: ❌
- **Reason**: 확률적 성형(distribution matcher) 리뷰+시뮬; LDPC는 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8696571
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Tobias Fehenberger, David S. Millar, Toshiaki Koike-Akino +2
- **PDF**: https://ieeexplore.ieee.org/document/8696571
- **Abstract**: Various aspects of distribution matchers (DMs) with constant and variable composition are reviewed. LDPC-coded fiber simulations of 64QAM shaped via a multiset-partition DM show significantly increased reach and information rate over a constant-composition DM.

## Rate-Adaptive Probabilistic Shaping Enabled by Punctured Polar Codes with Pre-Set Frozen Bits

- **Status**: ❌
- **Reason**: punctured polar 부호 기반 성형; 비-LDPC, 떼어낼 BP 이식 기법 없음
- **ID**: ieee:8696832
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Shajeel Iqbal, Metodi Plamenov Yankov, S⊘ren Forchhammer
- **PDF**: https://ieeexplore.ieee.org/document/8696832
- **Abstract**: We propose to pre-set the frozen bits of a rate-adaptive punctured polar-coded system to pseudo-random sequences. The many-to-one probabilistic shaping gains are improved to 2 dB («160 km) w.r.t. the standard punctured polar-coded system.

## Joint Source-Channel Coding via Compressed Distribution Matching in Fiber-Optic Communications

- **Status**: ❌
- **Reason**: 압축 분포정합 기반 JSCC; 소스-채널 결합으로 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8696846
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Tsuyoshi Yoshida, Magnus Karlsson, Erik Agrell
- **PDF**: https://ieeexplore.ieee.org/document/8696846
- **Abstract**: The variability of source entropy due to data idling is inconsistent with most studies' assumptions in probabilistic shaping. We propose a distribution matcher sensitive to the source entropy, and discuss its impacts on fiber-optic communications.

## Single-Wavelength and Single-Photodiode Entropy-Loaded 554-Gb/s Transmission Over 22-km SMF

- **Status**: ❌
- **Reason**: entropy-loaded IM-DD 전송 시연; 엔트로피 성형 위주, 떼어낼 LDPC 디코더·HW 기법 없음
- **ID**: ieee:8696539
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Xi Chen, Sethumadhavan Chandrasekhar, Junho Cho +1
- **PDF**: https://ieeexplore.ieee.org/document/8696539
- **Abstract**: We demonstrate the transmission of intensity-modulated and direct-detected (IM-DD) entropy-loaded signals over 22-km SMF with 554-Gb/s line rate and 460.9-Gb/s net bit rate.

## 74.38 Tb/s Transmission Over 6300 km Single Mode Fiber with Hybrid EDFA/Raman Amplifiers

- **Status**: ❌
- **Reason**: 74.38Tb/s 장거리 광전송 시연; 증폭기·성형 위주, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8696534
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: M. Ionescu, D. Lavery, A. Edwards +7
- **PDF**: https://ieeexplore.ieee.org/document/8696534
- **Abstract**: Transmission of 306×35 GBd, dual polarization, 64-ary geometrically shaped channels over 90× 70 km of SMF was demonstrated, achieving a net throughput of 74.38 Tb/s. A combination of hybrid fiber spans and EDFA/Raman amplifiers enabled a continuous gain bandwidth of 10.8 THz.

## 35-Tb/s C-Band Transmission Over 800 km Employing 1-Tb/s PS-64QAM Signals Enhanced by Complex 8 × 2 MIMO Equalizer

- **Status**: ❌
- **Reason**: C-band WDM 전송 + MIMO equalizer 데모 — LDPC/ECC 기여 없음, 통신 응용
- **ID**: ieee:8696972
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: T. Kobayashi, M. Nakamura, F. Hamaoka +6
- **PDF**: https://ieeexplore.ieee.org/document/8696972
- **Abstract**: We demonstrate the full C-band 1-Tb/s/λ WDM 800-km transmission with 35-Tb/s capacity employing novel complex 8 × 2 MIMO equalizer which enables simultaneous compensation of imperfections of transmitter and receiver of 120-Gbaud probabilistically-shaped-64QAM signals.

## Single-Wavelength Symmetric 50 Gbit/s Equalization-Free NRZ IM/DD PON with up to 33 dB Loss Budget and Fiber Transmission over >40 km

- **Status**: ❌
- **Reason**: 50G TDM-PON NRZ IM/DD 전송 시연; ECC/LDPC 무관, 떼어낼 기법 없음
- **ID**: ieee:8696513
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Robert Borkowski, Harald Schmuck, Giancarlo Cerulo +2
- **PDF**: https://ieeexplore.ieee.org/document/8696513
- **Abstract**: We demonstrate burst-mode upstream and continuous-mode downstream transmission in a 50G TDM-PON system, achieving up to 33-dB loss budget with a maximum of 77-km SMF transmission before any equalization. The system is enabled by semiconductor optical amplifiers at the transceivers.

## Demonstration of 100-Gb/s/λ PAM-4 TDM-PON Supporting 29-dB Power Budget with 50-km Reach using 10G-class O-Band DML Transmitters

- **Status**: ❌
- **Reason**: PAM-4 TDM-PON 광전송 데모, pre-FEC BER만 언급 — 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8696951
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Jiao Zhang, Jianjun Yu, Hungchang Chien +4
- **PDF**: https://ieeexplore.ieee.org/document/8696951
- **Abstract**: We experimentally demonstrated 100-Gb/s/λ PAM-4 TDM-PON downstream transmission in O-band using 10G-class DML and SOA pre-amplifier at the receivers. Power budget of 29 dB was achieved after 50-km transmission at pre-FEC BER threshold of 1 × 10-2.

## Single-Channel Direct Detection Reception Beyond 1 Tb/s

- **Status**: ❌
- **Reason**: 1Tb/s 직접검파 광전송 데모, ECC/LDPC 기법 없음 — 통신 응용, 떼어낼 기법 없음
- **ID**: ieee:8696932
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: D. Che, S. Chandrasekhar, X. Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/8696932
- **Abstract**: We demonstrate the world-first single-channel direct detection beyond 1-Tb/s with 1.26-Tb/s line rate and 1.02-Tb/s net rate after 100-km SSMF, via an 86-GHz Stokes vector receiver that recovers totally single-polarization-equivalent 252-Gbaud probabilistic-shaped 64-QAM signal.

## Multi-Rate Prefix-Free Code Distribution Matching

- **Status**: ❌
- **Reason**: 확률적 성형용 prefix-free 분포정합 알고리즘; 채널 ECC가 아닌 distribution matching, 떼어낼 LDPC 기법 없음
- **ID**: ieee:8696370
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Junho Cho, Peter J. Winzer
- **PDF**: https://ieeexplore.ieee.org/document/8696370
- **Abstract**: We propose a multi-rate prefix-free code distribution matching (PCDM) algorithm that implements a fixed-length probabilistic constellation shaping. It uses various small codebooks in an adaptive manner, thereby improving the shaping performance of PCDM.

## Optimum Bit-Level Distribution Matching with at Most O(N3) Implementation Complexity

- **Status**: ❌
- **Reason**: distribution matching(확률성형) 알고리즘 — ECC 채널코딩 아님(소스/성형), 떼어낼 LDPC 기법 없음
- **ID**: ieee:8696977
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Yohei Koganei, Kiichi Sugitani, Hisao Nakashima +1
- **PDF**: https://ieeexplore.ieee.org/document/8696977
- **Abstract**: An algorithm of distribution matching which could be effectively implemented for short block lengths of around 100 bit or less is proposed, enabling better performance than the constant composition schemes with the same block lengths.

## Integrated Dual-DFB Laser for 408 GHz Carrier Generation Enabling 131 Gbit/s Wireless Transmission over 10.7 Meters

- **Status**: ❌
- **Reason**: 408GHz 무선전송 데모(레이저/equalization) — ECC/LDPC 기법 없음
- **ID**: ieee:8697005
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Shi Jia, Mu-Chieh Lo, Lu Zhang +12
- **PDF**: https://ieeexplore.ieee.org/document/8697005
- **Abstract**: A monolithically integrated dual-DFB laser generates a 408 GHz carrier used for demonstrating a record-high single-channel bit rate of 131 Gbit/s transmitted over 10.7 m. 16-QAM-OFDM modulation and specific nonlinear equalization techniques are employed.

## 5×510 Gbps Single-Polarization Direct-Detection WDM Transmission over 80 km of SSMF

- **Status**: ❌
- **Reason**: WDM 직접검출 광전송 시연; LDPC/ECC 언급 없고 떼어낼 디코더·HW·코드설계 기법 없음
- **ID**: ieee:8696275
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Son Thai Le, Karsten Schuh, Roman Dischler +3
- **PDF**: https://ieeexplore.ieee.org/document/8696275
- **Abstract**: We demonstrate 5-channel WDM DD transmissions over 80 km of SSMF with a net data rate per channel of 432 Gbps using either Kramers-Kronig detection or a low-complexity interference cancellation scheme.

## Design of Unequal Error Protection LDPC Code in PPM and LDPC Optical Communication System

- **Status**: ❌
- **Reason**: 광통신 PPM 결합 UEP-LDPC 차수분포 설계 — 비등보호+PPM 응용 특이적, NAND ECC로 떼어낼 일반 구성기법 없음
- **ID**: ieee:8873472
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Jingsong Xiang, Yimiao Wu, Xiaohui Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/8873472
- **Abstract**: In the space optical communication system, the link power loss is large, and the unequal error protection (UEP) scheme can effectively protect more important data in the transmission process and save transmission power. However, the performance of existing unequal error protection LDPC codes used directly in space optical communication systems is not ideal. In this paper, a design scheme of LDPC codes with multilevel unequal error protection performance is proposed for pulse position modulation (PPM) and Low-density parity-check (LDPC) codes iterative demodulation system. The scheme is aimed at maximizing the average variable node degree of each protection level to improve the unequal error protection characteristics of LDPC codes while combining the improved external information in the BICM-ID system extrinsic information transfer(EXIT) method to analyze the convergence threshold of degree distribution and optimize the degree distribution of UEP-LDPC code by iterative linear programming to obtain the minimum threshold and satisfy the unequal error protection characteristics. The simulation results show that the UEP-LDPC code constructed in this paper has improved performance compared with the existing UEP-LDPC code.

## Wireless Sensors Converged Network Enhancement

- **Status**: ❌
- **Reason**: WSN/모바일 융합망 PAPR·에너지 enhancement, LDPC 무관
- **ID**: ieee:8893181
- **Type**: conference
- **Published**: 21-24 Marc
- **Authors**: Omar R. Daoud, Ahlam A. Damati
- **PDF**: https://ieeexplore.ieee.org/document/8893181
- **Abstract**: This work deals with the proposition of machine-to-machine communications enhancement. Thus, a convergence between the wireless sensor network and the wireless mobile network has been studied. It is divided into three main parts; making use of one of our previously published work to enhance the wireless mobile network based on combatting the peak-to-average power ratio problem, building an actual wireless sensor network to observe a real data, and proposing a converged network as an enhancement. To validate the proposition, an extensive simulation has been performed based on observing some cretin performance parameters such as the round, the dying time, the consumed energy. Thus, the comparison has been made between the conventional wireless sensor network and the converged one. It shows a remarkable results and reaches 78% delay reduction. However, further studies should be made to investigate the routing algorithms in order to enhance the consumed energy by the sensor nodes.

## Discretized Density Evolution for Rate Compatible Modulation : Invited Presentation

- **Status**: ❌
- **Reason**: Rate Compatible Modulation DE 분석, 소스 엔트로피 기반 가중치 최적화; LDPC ECC 디코더/구성 기여 아님
- **ID**: ieee:8693058
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Mariano Eduardo Burich, Richard Demo Souza, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/8693058
- **Abstract**: In this paper, we develop, for the first time in the literature, a Density Evolution analysis of Rate Compatible Modulation (RCM), which is challenging due to the way symbols in RCM are generated as weighted sums of the input bits. We consider uniform and non-uniform memoryless binary sources. By allowing the weights to be real numbers, rather than integers as in previous work, we propose, for the first time in the literature, an optimization procedure that automatically obtains the weights of the RCM scheme for a desired source entropy, signal to noise ratio, and information rate.

## Acquisition and tracking for communications between Lunar South Pole and Earth

- **Status**: ❌
- **Reason**: 달 남극-지구 통신의 acquisition/tracking·페이딩 채널 설계, 코딩은 simple scheme 언급뿐 — 떼어낼 LDPC 기법 없음
- **ID**: ieee:8742112
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Dariush Divsalar, Marc Sanchez Net, Kar-Ming Cheung
- **PDF**: https://ieeexplore.ieee.org/document/8742112
- **Abstract**: In this paper we design and analyze an end-to-end communication system between a lander/rover on the surface of the lunar South Pole and an Earth station. The acquisition and tracking system is discussed in detail. The communication system on the lander or rover could be used for the Earth-to-Moon communication. To communicate to and from the lander/rover on the lunar South Pole, low and/or medium directional antennas onboard the lander/rover will have to be pointed at low elevation angles between 2 to 10 degrees, thus causing multipath fading effects due to reflection of a portion of the transmitted electromagnetic waves from the surface of the Moon that are not commonly encountered in traditional deep space communications between a spacecraft and a ground station. To design and analyze such a communication system, and in particular the acquisition and tracking system, in the presence of multipath fading, first we model the fading channel based on existing and simulated data. In addition to multipath fading, the channel also introduces Doppler frequency up to 11.5 KHz, and Doppler rate up to 0.735 Hz/sec. For coherent reception the Doppler frequency, which is time varying, should be acquired and the incoming carrier phase, which includes the fading phase, should be tracked in the presence of multipath fading. For this communication system in addition to estimating the received carrier phase, the amplitude of the fading signal should also be estimated, in particular to be used in the decoder. In addition to acquisition and tracking, we consider simple modulation and coding schemes. Space diversity using two antennas on Earth to mitigate the effects of fading could also be used. We design phase-locked loops and frequency sweeping schemes robust to the attenuations due to fading. After designing various components of the communication system, we use Simulink models to obtain the end-to-end performance of the communication link under investigation. Based on the available data, the fading channel can be accurately modeled as a Rician fading channel with Rician parameter of 10 dB, and Doppler spread that depends on the Doppler frequency and the transmit/receive antenna patterns. The challenge is how to make such a communication system robust in the presence of the multipath fading where the Doppler spread changes in time and thus produces fading with time-varying durations (short and very long fades). In summary, this paper covers communication system design, performance analysis, and simulations for performance of Doppler frequency acquisition, tracking, uncoded system, and coded system under ideal interleaving assumption with hard decision over communication link between a lander/rover at the Lunar south pole and a DSN Earth station in presence of Rician fading.

## Proximity Link Telecommunication and Tracking Scenarios for a Potential Mars Sample Return Campaign

- **Status**: ❌
- **Reason**: Mars Sample Return 중계 통신 시나리오·궤도 분석, LDPC/ECC 언급 없음
- **ID**: ieee:8741917
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Charles D. Edwards, Allen H. Farrington, Roy E. Gladden +6
- **PDF**: https://ieeexplore.ieee.org/document/8741917
- **Abstract**: A Mars Sample Return (MSR) campaign would involve a series of three flight missions to acquire and cache Mars samples, retrieve those samples and launch them into Mars orbit, and then capture these samples and return them to Earth. Relay communications would be crucial for supporting this campaign, characterized by multiple critical events, complex surface operations, and an on-orbit Mars rendezvous. The existing Mars relay network offers significant capability, and efforts are underway to maximize the likelihood that one or more of these current assets will still be operational in the timeframe of an MSR campaign. In addition, the Earth Return Orbiter (ERO) element of a campaign could serve as a primary relay asset, if it can achieve a useful relay orbit by the time of arrival of the Sample Retrieval Lander mission. We describe key operational challenges of the MSR campaign that would drive the required relay capabilities, and characterize the performance of the existing relay orbiters as well as ERO itself in meeting those relay needs.

## Performance of 5GNR with Interference Alignment

- **Status**: ❌
- **Reason**: 5GNR 간섭정렬 프리코딩, LDPC 무관 - 떼어낼 ECC 기법 없음
- **ID**: ieee:8713752
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Khawla A. Alnajjar, Mohamed El-Tarhuni
- **PDF**: https://ieeexplore.ieee.org/document/8713752
- **Abstract**: Recently, a New Radio (NR) structure has been proposed for fifth generation (5G) mobile radio systems to support higher data rates and low latency scenarios. In this paper, we investigate the performance of 5G New Radio (5GNR) using precoding for Interference Alignment (IA). The system is based on an OFDM structure following the NR scheme with zero forcing receiver. It is shown that with proper selection of the precoder, an improvement of about one order of magnitude in the bit error rate due to IA is achieved.

## Iterative Carrier Phase Recovery for MPSK Systems Based on Simplified EM Algorithm

- **Status**: ❌
- **Reason**: LDPC-coded MPSK의 반송파 위상복구(EM 단순화) — 채널 추정 기법이고 떼어낼 LDPC 디코더/HW/구성 기여 없음
- **ID**: ieee:8729542
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Xin Man, Dun Mao, Xiaohong Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8729542
- **Abstract**: This letter deals with the problem of carrier phase recovery for low-density parity-check (LDPC) coded MPSK systems at low signal-to-noise ratios (SNR). By utilizing Taylor series expansion and the constant-envelope characteristic of PSK signals, we greatly simplify the expectation maximization (EM) algorithm to recover the carrier phase. The proposed method works with simple operations of phase subtraction and accumulation instead of complex multiplication and accumulation in the EM algorithm. Apart from its low complexity, the simulation results for the case of 8-PSK system with a (1944; 972) irregular LDPC code show that the performance loss compared to the EM algorithm is negligible.

## Short Polar-coded Non-coherent Receiver

- **Status**: ❌
- **Reason**: Polar 부호 비상통신 수신기, BCJR 기반 검출 알고리즘으로 바이너리 LDPC BP에 이식할 기법 없음
- **ID**: ieee:8729533
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Huangxia Xu, Chaofan Chen, Yanming Xue
- **PDF**: https://ieeexplore.ieee.org/document/8729533
- **Abstract**: Emergency communications will be the key to deal with natural or man-made emergencies. Their prerequisites are the short frame burst under limited resources, as well as reliable bit error rate (BER) performance in low signal to noise ratio (SNR). With respect to short codes, polar codes normally outperform Low Density Parity Check (LDPC) codes and convolutional codes, which makes them more suitable for the emergency communications. However, the traditional polarcoded receiver either has a large discrepancy between the practical receiving performance and the theoretical one, or has high complexity, which limits its applications for emergency communications. Hence, to adapt to such scenario, in this paper we invoke an iterative mechanism into the receiver and propose a new non-coherent detection module, namely, short polar-coded non-coherent detection (SPND) module, as well as its corresponding detection algorithm, namely, outercode-feedback-innercode (OCFIC) BCJR-based algorithm. The simulations demonstrate that, with the condition of non-coherent channel and of the target BER of 10-5, the performance gap between the noncoherent detection scheme with the proposed SPND module and the coherent counterpart can be reduced to around 1dB. Meanwhile, the SPND module with short polar codes is superior to conventional non-coherent receiver with short LDPC codes, short polar codes and (2,1,7) convolutional codes by 1.2dB, 2.8dB and 3dB, respectively. Hardware implementation of the module is also presented in this paper.

## Research on Polarization Code Encoding and Decoding Algorithm Based on HARQ Technology

- **Status**: ❌
- **Reason**: polar code HARQ 디코딩, 비-LDPC이고 polar 전용
- **ID**: ieee:8729289
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Tingting Yu, Wei Nie
- **PDF**: https://ieeexplore.ieee.org/document/8729289
- **Abstract**: As a 5G control channel coding scheme, the polarization code can reach the Shannon limit theoretically. However, under the condition of medium and short code, the communicationeffect of polarization code is not ideal. To solve this problem, a de-coding based on HARQ technology is proposed. The algorithm adds feedback retransmission based on CA-SCL decoding, and retransmits some information bits by using a highly polarized channel, which can compensate for the problem that channel polarization is not sufficient in the case of medium and short codes, and reduces the bit error rate. However, adding a retransmission will increase the decoding delay. Therefore, the algorithm is applicable to scenarios with low latency requirements. Through theoretical analysis and MATLAB simulation, when N=256, when the bit error rate is 0.01, the improved algorithm obtains a gain of 0.5dB compared with the CA-SCL decoding algorithm. The decoding performance of the improved algorithm is verified under different code lengths. It can be seen that as the code length increases, the advantage of the improved algorithm is gradually reduced. Therefore, the algorithm is more suitable for short code.

## Error correction using LDPC code for performance improvement in clipped and biased OFDM with direct detection over optical fiber

- **Status**: ❌
- **Reason**: 광섬유 OFDM에 표준 LDPC(32400,64800) 단순 적용, 새 디코더/구성/HW 기여 없음
- **ID**: ieee:8877013
- **Type**: conference
- **Published**: 13-15 Marc
- **Authors**: Usha Choudhary, Vijay Janyani
- **PDF**: https://ieeexplore.ieee.org/document/8877013
- **Abstract**: Paper presents a performance comparison for DC-biased OFDM and clipped OFDM for unipolar transmission over optical fiber communication systems with forward error check encoder, LDPC (32400, 64800). Asymmetrically clipped OFDM is being studied intensively for possible future technology in a short range optical channel with low power applications as well as adaptive data rate allocation in network because same optimized design parameters can be used for large constellation size (up to QAM-1024). OFDM over optical fiber comes with several challenges like accommodation of existing opto-electric resources for futuristic approach. Inclusion of FEC scheme improves the BER performance, although data array size for transmission and total electrical power has increased. For OFDM without FEC we need laser power 3 dBm for lowest BER in range ($1^{*}10^{-5}$ and $1^{*}10^{-7}$) where as in LDPC coded OFDM lowest BER ($1^{*}10^{-5}$ and $1^{*}10^{-s}$) is observed for biased and clipped OFDM respectively.
