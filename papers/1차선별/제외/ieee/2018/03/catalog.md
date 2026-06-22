# IEEE Xplore — 2018-03


## High-Throughput Multi-Codeword Decoder for Non-Binary LDPC Codes on GPU

- **Status**: ❌
- **Reason**: 비이진(non-binary/GF(q)) LDPC GPU 디코더 — 비이진 LDPC 제외 대상
- **ID**: ieee:8254357
- **Type**: journal
- **Published**: March 2018
- **Authors**: Zhanxian Liu, Rongke Liu, Yi Hou +1
- **PDF**: https://ieeexplore.ieee.org/document/8254357
- **Abstract**: This letter presents a graphics processing unit (GPU)-based non-binary low density parity check multi-codeword decoder with both kernel execution and data transfer optimizations. A novel multi-codeword data structure and its corresponding parallelism are proposed to boost the compute unified device architecture kernel execution. Moreover, practical methods of hiding the data transfer latency are presented to improve data transfer efficiency. Experimental results demonstrate that the throughput speedups achieved by the proposed decoder range from 3.12x to 185x over various Galois fields compared with the existing works on GPU.

## Basic-Set Trellis Min–Max Decoder Architecture for Nonbinary LDPC Codes With High-Order Galois Fields

- **Status**: ❌
- **Reason**: 비이진 NB-LDPC(GF32/64) 디코더—바이너리 LDPC 한정 기준에 따라 제외
- **ID**: ieee:8171205
- **Type**: journal
- **Published**: March 2018
- **Authors**: Huyen Pham Thi, Hanho Lee
- **PDF**: https://ieeexplore.ieee.org/document/8171205
- **Abstract**: Nonbinary low-density parity-check (NB-LDPC) codes outperform their binary counterparts in terms of error-correction performance. However, the drawback of NB-LDPC decoders is high complexity, especially for the check node unit (CNU), and the complexity increases considerably when increasing the Galois-field (GF) order. In this paper, a novel basic-set trellis min-max algorithm is proposed to greatly reduce not only the CNU complexity but also the number of messages exchanged between the check node and the variable node compared with previous studies, which is highly efficient for higher order GFs. In addition, the proposed CNU is designed to compute the messages in a parallel way. Layered decoder architectures based on the proposed algorithm were implemented for the (837, 726) NB-LDPC code over GF(32) and the (1512, 1323) code over GF(64) using 90-nm CMOS technology, and obtained a reduction in the complexity by 30% and 37% for the CNU, and 40% and 37.4% for the whole decoder, respectively. Moreover, the proposed decoder achieves a higher throughput at 1.67 Gbit/s and 1.4 Gbit/s compared with the other state-of-the-art high-rate NB-LDPC decoders with high-order GFs.

## Design of Channel Coded Heterogeneous Modulation Physical Layer Network Coding

- **Status**: ❌
- **Reason**: RA 부호 기반 물리계층 네트워크코딩으로 비-LDPC(RA) 부호+릴레이 응용 특이적, 이식 ECC 기법 없음
- **ID**: ieee:8082522
- **Type**: journal
- **Published**: March 2018
- **Authors**: Haoyuan Zhang, Lin Cai
- **PDF**: https://ieeexplore.ieee.org/document/8082522
- **Abstract**: In a two-way relay channel network (TWRC), the integration of channel coding into symmetric physical layer network coding (PNC) has been well studied, where both sources use exactly the same channel coding and modulation schemes and the relay decodes and reencodes the codewords obtained from the superimposed signals. How to integrate the channel coding into heterogeneous modulation PNC (HePNC), where the sources apply different modulations, is an open issue. In this paper, we propose a channel coded HePNC (CoHePNC) scheme under asymmetric TWRC. For repeat-accumulate (RA) codes applied at the sources, a full-state sum-product decoding algorithm is proposed which enables the relay to decode the superimposed signals from the sources to the raw decoding results firstly, and then re-encode and obtain the network-coded codewords by mapping the raw decoding results according to the proposed bit-level mapping functions. We further optimized the bit-level mapping functions according to the two source-relay channel conditions. Extensive simulation results demonstrated that the proposed CoHePNC outperforms the existing channel coded PNC schemes in terms of the relay decoding error rate and the end-to-end bit error rate under asymmetric TWRC scenarios.

## Image Processing Unit for General-Purpose Representation and Association System for Recognizing Low-Resolution Digits With Visual Information Variability

- **Status**: ❌
- **Reason**: 랜덤 LDPC를 이미지 인식 IPU에 응용, 부호 최적화 없음(non-optimized) - 떼어낼 새 ECC 기법 없음
- **ID**: ieee:7560636
- **Type**: journal
- **Published**: March 2018
- **Authors**: Bowen Dai, Huihui Li, Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/7560636
- **Abstract**: In this paper, a simple image processing unit (IPU) structure for a general-purpose representation and association machine system is proposed. We immediately apply our IPU to a digit recognition and hyper-acuity test. The quality of the digit images has been severely degraded to mimic visual information variability experienced in human visual systems. The degraded images are then fed to the IPU, which consists of a randomly constructed low-density parity check (LDPC) code, an iterative decoder, a switch, and scaling, and decision devices. The results show that: 1) our IPU can reliably recognize digits despite the image quality being poor; 2) our IPU provides a hyper-acuity capability comparable to human visual systems; and 3) our IPU with the randomly constructed LDPC code can provide significantly improved recognition capability compared with the IPU without coding, even though the code is not optimized for our tasks.

## Analysis and Design of Physical Layer Raptor Codes

- **Status**: ❌
- **Reason**: Raptor(fountain) 코드 DDE 분석/최적화, 비-LDPC fountain 부호로 떼어낼 ECC 기법 없음
- **ID**: ieee:8214248
- **Type**: journal
- **Published**: March 2018
- **Authors**: Amrit Kharel, Lei Cao
- **PDF**: https://ieeexplore.ieee.org/document/8214248
- **Abstract**: In this letter, we first provide the asymptotic analysis of Raptor codes over binary input additive white Gaussian noise channels using discretized density evolution (DDE). We show that the Raptor codes of various realized code-rates using the same output degree distribution perform within 0.4-dB to the Shannon limit. We then prove a necessary condition for the successful decoding of such codes and use it with a DDE-based optimization method to obtain optimized Raptor codes with further improvement in decoding thresholds.

## Spatial Modulation Aided Sparse Code-Division Multiple Access

- **Status**: ❌
- **Reason**: SM-SCDMA 다중접속 검출용 MPA, 무선 응용 특이적이고 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8166802
- **Type**: journal
- **Published**: March 2018
- **Authors**: Yusha Liu, Lie-Liang Yang, Lajos Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/8166802
- **Abstract**: In order to support high-user-load multiple-access (MA), we propose a non-orthogonal MA scheme based on a beneficial amalgam of spatial modulation (SM) and sparse code-division multiple-access (SCDMA), which is termed the SM-SCDMA. Hence, SM-SCDMA inherits both the merits of SM with single radio-frequency MIMO transceiver implementation and the advantages of SCDMA relying on low-complexity signal detection. In this paper, we evaluate the potential of SM-SCDMA as well as its low-complexity near-optimum signal detection. Given these objectives, we consider both the maximum likelihood detection and the message passing algorithm aided detection (MPAD) that is derived based on the maximum a posteriori principles. In order to evaluate the performance of large SM-SCDMA without relying on time-consuming simulations, we propose new approaches for analyzing the performance of SM-SCDMA systems. A range of formulas that are valid in the signal-to-noise ratio region of practical interest are derived. Finally, the performance of SM-SCDMA systems is investigated by addressing diverse design concerns. Our studies and performance results show that SM-SCDMA constitutes a promising MA scheme for the future ultra dense systems. Assisted by the MPAD, it is capable of supporting high-user-load MA transmission associated with a normalized user-load factor of two.

## Performance Analysis of Lossy Decode-and-Forward for Non-Orthogonal MARCs

- **Status**: ❌
- **Reason**: lossy DF relay+Slepian-Wolf 결합소스 무선 협력통신, LDPC 부수적, NAND ECC 이식 기법 없음
- **ID**: ieee:8170333
- **Type**: journal
- **Published**: March 2018
- **Authors**: Jiguang He, Valtteri Tervo, Shen Qian +3
- **PDF**: https://ieeexplore.ieee.org/document/8170333
- **Abstract**: Non-orthogonal transmission is considered to be one of the promising techniques for improving the throughput of the existing and future wireless communication networks. We concentrate on the transmission of both independent and correlated binary sources over a non-orthogonal multiple access relay channel (MARC), which consists of two sources, one relay, and one destination. The lossy decode-and-forward (DF), developed from the conventional DF, is adopted at the relay. Two time slots are required with non-orthogonal transmission over such network setup, while three time slots are required with the conventional orthogonal transmission. We analyze the outage probability of transmission of independent binary sources over the non-orthogonal MARC based on the theorem of multiple access channel (MAC) with a helper, which combines the Slepian-Wolf rate region and the MAC capacity region. For the performance verification, we implement a practical coding-decoding chain, which is applicable to the transmission of both independent and correlated binary sources. Exclusive-OR based multi-user complete decoding is introduced at the relay node, and iterative joint decoding is utilized at the destination by taking into consideration the estimated intra-link error probability and correlation information between the sources. The practical simulation results are well matched with the theoretical analyses.

## New Miller Codes for Run-Length Control in Visible Light Communications

- **Status**: ❌
- **Reason**: VLC용 Miller RLL 부호+Viterbi 변형, LDPC 무관 비-LDPC 부호
- **ID**: ieee:8240732
- **Type**: journal
- **Published**: March 2018
- **Authors**: Xuanxuan Lu, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/8240732
- **Abstract**: Designing run-length limited codes for visible light communication systems must account for multiple performance factors, including spectral efficiency, power efficiency, dc balance, and flicker avoidance. This paper reports a new class of enhanced Miller codes, termed eMiller codes, which are capable of achieving highly desirable performances in all of these accounts. An improved Viterbi algorithm (VA), termed $mn$ VA, is developed to help further enhance the performance of eMiller codes by preserving multiple candidate sequences at each decoding stage. This performance-enhancing algorithm introduces little complexity increase compared with the original VA. Analysis on flicker control, power spectral density, and minimum Hamming distance demonstrates the all-around wellness of these new codes. Extensive simulations are carried out to evaluate eMiller codes by themselves and in practical visible light communication (VLC) systems. It is shown that the original VA already allows eMiller codes to deliver a performance noticeably better than conventional Miller and FM0/FM1 codes (and on par with Manchester codes). This result is particularly exciting, as eMiller codes are also more spectrally efficient than Manchester codes. The $mn$ VA further allows eMiller codes to surpass Manchester codes and 4B6B codes in practical RS-coded VLC systems. Simulation results confirm the superb performance of the RS-eMiller schemes.

## LDA Lattices Without Dithering Achieve Capacity on the Gaussian Channel

- **Status**: ❌
- **Reason**: LDA lattice는 비이진 LDPC 기반 Construction A, 순수 capacity 이론 bound로 디코더/HW/구성 이식 기여 없음
- **ID**: ieee:8122043
- **Type**: journal
- **Published**: March 2018
- **Authors**: Nicola di Pietro, Gilles Zémor, Joseph J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/8122043
- **Abstract**: This paper deals with Low-Density Construction-A (LDA) lattices, which are obtained via Construction A from non-binary low-density parity-check codes. More precisely, a proof is provided that Voronoi constellations of LDA lattices achieve capacity of the AWGN channel under lattice encoding and decoding for every signal-to-noise ratio greater than 1. This is obtained after showing the same result for more general Construction-A lattice constellations. The theoretical analysis is carried out in a way that allows to describe how the prime number underlying Construction A behaves as a function of the lattice dimension. Moreover, no dithering is required in the transmission scheme, simplifying some previous solutions of the problem. Remarkably, capacity is achievable with LDA lattice codes whose parity-check matrices have constant row and column Hamming weights. Some expansion properties of random bipartite graphs constitute an extremely important tool for dealing with sparse matrices and allow to find a lower bound for the minimum Euclidean distance of LDA lattices in our ensemble.

## Priori-Information Hold Subspace Pursuit: A Compressive Sensing-Based Channel Estimation for Layer Modulated TDS-OFDM

- **Status**: ❌
- **Reason**: TDS-OFDM 압축센싱 채널추정으로 LDPC 무관, ECC 기법 없음
- **ID**: ieee:7938332
- **Type**: journal
- **Published**: March 2018
- **Authors**: Jingjing Liu, Chao Zhang, Changyong Pan
- **PDF**: https://ieeexplore.ieee.org/document/7938332
- **Abstract**: Time-domain synchronous orthogonal frequency division multiplexing (TDS-OFDM) has been widely recognized as a fundamental OFDM block transmission scheme because of its advantages in spectral efficiency. However, it suffers from severe performance loss under strong frequency selective channels and thus has difficulty supporting high-order modulations such as 256QAM. In this paper, we proposed a compressive sensing (CS)-based channel estimation (CE) algorithm for layer modulated TDS-OFDM (LM-TDS-OFDM). In the proposed CE algorithm, the low-order modulated symbols will be recovered and then sent to a feedback loop for precise CE. The priori-information hold subspace pursuit algorithm is investigated to achieve accurate estimation of channel. Analyses and simulations show that the proposed algorithm can successfully obtain high-accuracy CE and significantly reduce the computational complexity. Based on the proposed CE scheme, LM-TDS-OFDM can well support 256QAM transmission under severe channel conditions.

## Rate-Compatible Tail-Biting Convolutional Codes for M2M Communications

- **Status**: ❌
- **Reason**: rate-compatible tail-biting convolutional codes 구성, 비-LDPC 부호이고 부호 비의존 디코더 기법 없음
- **ID**: ieee:8239785
- **Type**: journal
- **Published**: March 2018
- **Authors**: Xiaowei Wu, Lei Yang, Jinhong Yuan +2
- **PDF**: https://ieeexplore.ieee.org/document/8239785
- **Abstract**: We propose an algorithm to construct a group of rate-compatible tail-biting convolutional codes (RC-TBCCs) with consistently good frame error rate performance for both short and long information lengths. The algorithm considers the free distance property and the minimum distance profile of a TBCC jointly. We construct a group of RC-TBCCs with code rates 1/n, 3 ≤ n ≤ 12. Numerical results show that the constructed RC-TBCCs have better frame error rate performance than the TBCCs used in LTE standards for various information lengths and code rates.

## Systematic Block Markov Superposition Transmission of Repetition Codes

- **Status**: ❌
- **Reason**: BMST 반복부호+MAP 디코딩, SC-LDPC와 비교만 할 뿐 떼어낼 LDPC BP 기법 없음(비-LDPC 부호)
- **ID**: ieee:8240708
- **Type**: journal
- **Published**: March 2018
- **Authors**: Xiao Ma, Kechao Huang, Baoming Bai
- **PDF**: https://ieeexplore.ieee.org/document/8240708
- **Abstract**: In this paper, we propose systematic block Markov superposition transmission of repetition (BMST-R) codes, which can support a wide range of code rates but maintain essentially the same encoding/decoding hardware structure. The systematic BMST-R codes resemble the classical rate-compatible punctured convolutional codes, except that they are typically non-decodable by the Viterbi algorithm due to the huge constraint length induced by the block-oriented encoding process. The information sequence is partitioned equally into blocks and transmitted directly, while their replicas are interleaved and transmitted in a block Markov superposition manner. By taking into account that the codes are systematic, we derive both upper and lower bounds on the bit-error-rate (BER) under maximum a posteriori decoding. The derived lower bound reveals connections among BER, encoding memory and code rate, which provides a way to design good systematic BMST-R codes and also allows us to make trade-offs among efficiency, performance, and complexity. Numerical results show that: 1) the proposed bounds are tight in the high signal-to-noise ratio region; 2) systematic BMST-R codes perform well in a wide range of code rates; and 3) rate 1/2 systematic BMST-R codes outperform the considered (3,6)- and (4,8)-regular spatially coupled low-density parity-check codes under an equal decoding latency constraint.

## Performance of Energy Harvesting Receivers With Power Optimization

- **Status**: ❌
- **Reason**: 에너지 하베스팅 수신기 전력최적화로 code rate가 부수 변수, 떼어낼 LDPC ECC 디코더/구성 기법 없음
- **ID**: ieee:8116685
- **Type**: journal
- **Published**: March 2018
- **Authors**: Zhengwei Ni, Mehul Motani
- **PDF**: https://ieeexplore.ieee.org/document/8116685
- **Abstract**: The difficulty of modeling energy consumption in communication systems leads to challenges in energy harvesting (EH) systems, in which nodes scavenge energy from their environment. An EH receiver must harvest enough energy for demodulating and decoding. The energy required depends upon factors, such as code rate and signal-to-noise ratio, which can be adjusted dynamically. We consider a receiver which harvests energy from the transmitter and other ambient sources, meaning the received signal is used for both EH and information decoding. Assuming a generalized function for energy consumption, we maximize the total number of information bits decoded, under both average and peak power constraints at the transmitter, by carefully optimizing the power used for EH, power used for information transmission, fraction of time for EH, and code rate. For transmission over a single block, we find there exist problem parameters for which either maximizing power for information transmission or maximizing power for EH is optimal. In the general case, the optimal solution is a tradeoff of the two. For transmission over multiple blocks, we give an upper bound on performance and give sufficient and necessary conditions to achieve this bound. Finally, we give some numerical results to illustrate our results and analysis.

## An Improved Variational Inference Approach to Iterative OFDM Receiver Design for Superimposed Training-Based AF Relay Networks

- **Status**: ❌
- **Reason**: OFDM AF 릴레이 변분베이즈 수신기 설계로 채널추정/복조 결합, 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8082549
- **Type**: journal
- **Published**: March 2018
- **Authors**: Seyed Mohammad Sajad Sadough, Zahra Chamideh
- **PDF**: https://ieeexplore.ieee.org/document/8082549
- **Abstract**: Using variational Bayesian approximation (VBA), we propose a general framework for joint channel estimation, demodulation, and decoding in an orthogonal frequency-division multiplexing (OFDM) amplify-and-forward (AF) relay network. AF relaying is adopted due to its simplicity and ease of implementation, and both cases of fixed- and variable-gain AF protocols are addressed. Unlike the classical approach where a number of subcarriers are solely dedicated to pilots, partial data-dependent superimposed training is considered here, which preserves the spectral efficiency. Assuming a bit-interleaved coded modulation OFDM system at the source, a modified formulation of VBA is proposed, which is, in fact, a Bayesian framework of turbo data detection of OFDM under channel estimation errors. More precisely, by an appropriate exploitation of the inherent “soft” information on channel and data available from the VBA formalism, we derive a modified iterative receiver, which reduces the impact of channel uncertainty by averaging the “soft data decision” over the posterior distribution of the unknown channel at each decoding iteration. The proposed modified VBA approach is contrasted to the conventional VBA and to the mismatched VBA approach, where, in the latter, the unknown channel is just replaced by its imperfect estimate. We show that conventional and mismatched VBA are suboptimal and can be viewed as a particular case of the proposed VBA method. In addition, we show that the VBA approach makes a nice connection between the classical techniques such as pilot-only channel estimation and the expectation-maximization algorithm, which can be viewed as a special case of VBA. By comparison with state-of-the-art VBA-based estimators through numerical analysis, we highlight the superiority of our modified VBA method and demonstrate a notable performance improvement in terms of the bit error rate.

## MIMO Wiretap Channels Based on Generalized Extended Orthogonal STBCs and Feedback

- **Status**: ❌
- **Reason**: MIMO 도청채널 STBC+정보조정 보안 응용으로 LDPC 무관, 제외 대상
- **ID**: ieee:8107567
- **Type**: journal
- **Published**: March 2018
- **Authors**: Yuwen Cao, Xue-Qin Jiang, Hui-Ming Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/8107567
- **Abstract**: This paper presents a two-phase process consisting of advantage distillation (AD) and information reconciliation for achieving secret sharing over a wiretap channel. By using the feedback bits from the legitimate receiver to transmitter, we propose a novel AD scheme for multiple-input multiple-output (MIMO) wiretap (MIMO-WT) channels. We first generalize the extended orthogonal space-time block codes (EO-STBCs). Then, based on the generalized EO-STBCs (GEO-STBCs) and channel state information (CSI), the feedback bits transmitted from the legitimate receiver to the transmitter are generated to increase the signal-to-noise ratio (SNR) gap between the legitimate receiver and the eavesdropper. Simulation results show that the feedback performance gain of the proposed AD scheme increases rapidly with the number of transmit antennas and the value of SNR. A bit error rate (BER) performance gain up to 5.5 dB is obtained by the legitimate receiver over the eavesdropper at the BER of 10-5. Moreover, it is also shown that the secrecy capacity of two-way MIMO-WT channels with feedback grows rapidly in low SNR regime and grows slowly in high SNR regime.

## Techniques for Improving the Finite Length Performance of Sparse Superposition Codes

- **Status**: ❌
- **Reason**: Sparse superposition codes(SPARC)+AMP 디코딩, LDPC는 비교 베이스라인일 뿐 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:8119577
- **Type**: journal
- **Published**: March 2018
- **Authors**: Adam Greig, Ramji Venkataramanan
- **PDF**: https://ieeexplore.ieee.org/document/8119577
- **Abstract**: Sparse superposition codes are a recent class of codes introduced by Barron and Joseph for efficient communication over the AWGN channel. With an appropriate power allocation, these codes have been shown to be asymptotically capacity-achieving with computationally feasible decoding. However, a direct implementation of the capacity-achieving construction does not give good finite length error performance. In this paper, we consider sparse superposition codes with approximate message passing (AMP) decoding, and describe a variety of techniques to improve their finite length performance. These include an iterative algorithm for SPARC power allocation, guidelines for choosing codebook parameters, and estimating a critical decoding parameter online instead of precomputation. We also show how partial outer codes can be used in conjunction with AMP decoding to obtain a steep waterfall in the error performance curves. We compare the error performance of AMP-decoded sparse superposition codes with coded modulation using LDPC codes from the WiMAX standard.

## EXIT-Chart Aided Design of Row-Permutation Assisted Twin-Interleaver BICM-ID

- **Status**: ❌
- **Reason**: BICM-ID 인터리버/매핑 설계로 변조 응용 특이적, EXIT-chart로 RPI 설계 - 떼어낼 LDPC ECC 디코더/구성 기법 없음
- **ID**: ieee:7935441
- **Type**: journal
- **Published**: March 2018
- **Authors**: In-Woong Kang, Hyoung-Nam Kim, Lajos Hanzo Hanzo
- **PDF**: https://ieeexplore.ieee.org/document/7935441
- **Abstract**: Twin-interleaver bit-interleaved LDPC coded modulation (BICM) has been widely adopted and studied in the context of digital terrestrial transmission (DTT) systems. Extrinsic-information transfer (EXIT) charts have been used as an analysis tool to evaluate the iterative decoding performance and to design a twin-interleaver BICM system. Since BICM using iterative decoding (BICM-ID) exhibits capacity-approaching decoding performance, developing the conventional twin-interleaver BICM DTT system to a BICM-ID system has also been attempted. When considering the twin-interleaver BICM-ID systems, there are a couple of aspects that should be taken into account. We will demonstrate that anti-Gray mapping should be adopted for improving the iterative decoding performance instead of the classic Gray symbol mapping. However, the previous literature related to designing the associated row-permutation interleaver (RPI) was mainly focused on BICM systems relying on Gray mapping. Hence, we will design the RPI of the twin-interleaver BICM-ID DTT systems using an anti-Gray mapping. Explicitly, we use: 1) the EXIT-chart analysis that accurately visualizes the overall iterative decoding and demapping performance of the twin-interleaver BICM-ID DTT systems using anti-Gray mapping and 2) a preprocessing stage for eliminating duplicate RPI candidates by using a parameter that roughly predicts the EXIT-chart analysis result before the EXIT-chart analysis is involved. By the elimination of the duplicates, over 99% of the initial candidates of the RPIs can be removed from the original M! candidates, where M stands for the number of modulated bits in a symbol. Given this drastically reduced number of candidates, the proposed design method finds novel RPIs, having superior bit-error ratio performances over the conventional RPIs in the context of the DVB-T2 standard.

## Study of performance comparison of satellite error correction codes for correcting big burst data errors

- **Status**: ❌
- **Reason**: 위성 ECC(RS/conv/turbo/LDPC) 성능 단순 비교 서베이성; 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:8367687
- **Type**: conference
- **Published**: 9-12 March
- **Authors**: Bingrui Wang, Qingli Zhang
- **PDF**: https://ieeexplore.ieee.org/document/8367687
- **Abstract**: Big burst errors often occur in satellite communications, leading to multiple consecutive bit errors. In the paper, we make a comparison among the CCSDS codes, such as RS codes, convolutional codes, Turbo codes and LDPC codes. In addition, the performance analysis of correcting big burst errors of these codes is conducted. The experimental results show that the burst error correction performance of RS codes is the best under CCSDS standard.

## Performance Analysis of Hybrid ARO Buffer Management

- **Status**: ❌
- **Reason**: LTE/5G HARQ 버퍼 관리 기법으로 LDPC ECC와 무관, 떼어낼 디코더/코드 기법 없음
- **ID**: ieee:8390363
- **Type**: conference
- **Published**: 5-8 March 
- **Authors**: Sangmin Kim, Daejung Yoon, Kilsik Ha
- **PDF**: https://ieeexplore.ieee.org/document/8390363
- **Abstract**: In handset modem design, HARQ buffer management techniques to significantly reduce the chip area are critical considerations for LTE-Advanced and prospective 5G technologies. In this paper, we first analyze the relationship between the mutual information of received packets and the soft combining of HARQ retransmissions, and then we propose a novel HARQ buffer management to improve the probability of successful decoding under a reduced HARQ buffer size. Compared to a full-capacity HARQ buffer, it is shown that comparable performance can be achieved by using error distributions of unsuccessful decoded blocks and early combining techniques. The results show a 50% reduction in the HARQ buffer size with a negligible degradation in the decoding performance and throughput at the target block error rate.

## Assessment of potential Mars relay network enhancements

- **Status**: ❌
- **Reason**: 화성 중계망 평가, LDPC 코딩 도입은 부수 언급 - 새 LDPC 기법 없음
- **ID**: ieee:8396682
- **Type**: conference
- **Published**: 3-10 March
- **Authors**: Charles D. Edwards, Roy Gladden, Charles H. Lee +1
- **PDF**: https://ieeexplore.ieee.org/document/8396682
- **Abstract**: In anticipation of increased demands on Mars relay services, including planned arrivals of NASA's InSight Lander in November 2018, and of NASA's Mars 2020 rover and ESA's ExoMars Rover & Surface Platform mission in Feb-Mar. 2021, we have assessed a number of potential modifications and upgrades to Mars relay orbiters and quantified their impacts in terms of key relay support metrics, to support NASA and ESA programmatic decisions. Specific areas of investigation include: 1) implementation of “split-pass” relay capability for support to collocated landers, 2) modifications of the extended mission orbit for the Mars Atmosphere and Volatile EvolutioN Mission (MAVEN), and 3) introduction of Low-Density Parity Check (LDPC) coding. We report here on each of these potential upgrades, quantify the performance implications each would have on future Mars relay services in the context of future mission support scenarios, and provide a status on implementation.

## High-rate Ka-band modulator for the NISAR mission

- **Status**: ❌
- **Reason**: Ka-band 위성 변조기 HW, 7/8 LDPC는 부수 언급 - 떼어낼 LDPC ECC 기법 없음 (RF/변조 중심)
- **ID**: ieee:8396451
- **Type**: conference
- **Published**: 3-10 March
- **Authors**: Michael Pugh, Igor Kuperman, Michael Kobayashi +3
- **PDF**: https://ieeexplore.ieee.org/document/8396451
- **Abstract**: In order to meet ever-increasing data return requirements, more satellites are using the near-Earth Ka-band (25.5-27.0 GHz) to achieve higher downlink rates. The paper discusses the Universal Space Transponder - Ka-band Modulator (UST-KaM) developed at the NASA Jet Propulsion Laboratory for the NASA-ISRO SAR (NISAR) mission, which is capable of transmitting up to 1.74 Gbps with 7/8 LDPC encoding. The UST-KaM utilizes OQPSK with both baseband and RF filtering to contain the 1 Gsps transmission spectrum within the 1.5 GHz Ka-band, even with the use of an external, saturated amplifier. Due to the high data rates involved, several technical hurdles were overcome in both the digital and RF designs. The UST-KaM is a software defined radio with two digital circuit board assemblies: a low speed housekeeper board for commanding and telemetry, and a high-rate signal processing board known as the Signal Processing Module (SPM). The SPM receives data from the spacecraft via a SERDES interface at up to 2 Gbps, processes and encodes the data using a Xilinx Virtex-5 FPGA, and produces 1 Gsps OQPSK I and Q waveforms via synchronized, multiplexed DACs. The RF Electronics in the UST-KaM employ a heterodyne architecture in which the I/Q digital waveforms are filtered and then up-converted using a sub-harmonic IQ mixer. The LO of the converter, which is included in the exciter assembly, is at 13.125GHz, and the RF output is a 26.25GHz carrier which is modulated with the OQPSK waveforms. The output of the mixer is then filtered using low loss quartz thin-film edge coupled Chebyshev filters and amplified through a series of low gain Ka-Band amplifiers. The exciter assembly also has a 2GHz, low-phase-noise, PLL synthesizer to supply the clock to the DACs for the high rate digital waveforms.

## K-Means Algorithm Over Compressed Binary Data

- **Status**: ❌
- **Reason**: 바이너리 sparse matrix 소스 코딩(압축) 위에서 K-means — 채널 ECC가 아닌 소스 코딩, 떼어낼 디코더 기법 없음
- **ID**: ieee:8416624
- **Type**: conference
- **Published**: 27-30 Marc
- **Authors**: Elsa Dupraz
- **PDF**: https://ieeexplore.ieee.org/document/8416624
- **Abstract**: We consider a network of binary-valued sensors with a fusion center. The fusion center has to perform K-means clustering on the binary data transmitted by the sensors. In order to reduce the amount of data transmitted within the network, the sensors compress their data with a source coding scheme based on binary sparse matrices. We propose to apply the K-means algorithm directly over the compressed data without reconstructing the original sensors measurements, in order to avoid potentially complex decoding operations. We provide approximated expressions of the error probabilities of the K-means steps in the compressed domain. From these expressions, we show that applying the K-means algorithm in the compressed domain enables to recover the clusters of the original domain. Monte Carlo simulations illustrate the accuracy of the obtained approximated error probabilities, and show that the coding rate needed to perform K-means clustering in the compressed domain is lower than the rate needed to reconstruct all the measurements.

## Approaching waterfilling capacity of parallel channels by higher order modulation and probabilistic amplitude shaping

- **Status**: ❌
- **Reason**: 확률적 진폭 셰이핑/워터필링 변조 기법; LDPC는 베이스라인 FEC일 뿐 떼어낼 ECC 기법 없음
- **ID**: ieee:8362291
- **Type**: conference
- **Published**: 21-23 Marc
- **Authors**: Fabian Steiner, Patrick Schulte, Georg Bocherer
- **PDF**: https://ieeexplore.ieee.org/document/8362291
- **Abstract**: Parallel, additive white Gaussian noise (AWGN) channels with an average sum power constraint are considered. It is shown how the waterfilling Shannon capacity can be approached by higher order modulation and probabilistic amplitude shaping (PAS). This is achieved by a new distribution matching approach called product distribution matching (PDM). The asymptotic performance of PDM is analyzed by achievable rates. A heuristic for optimizing the input distribution is proposed, which enables signaling at a target spectral efficiency with a fixed-rate forward error correction (FEC) code, while the optimal power allocation is ensured by mercury-waterfilling and a simple bit-loading strategy. Finite blocklength simulation results with 5G low-density parity-check codes show power savings of around 1 dB compared to a conventional scheme with uniform input distributions.

## Polar coded Interleave Division Multiple Access Ultra Wide Band (IDMA-UWB) communication system

- **Status**: ❌
- **Reason**: Polar 부호+IDMA-UWB 무선응용, LDPC는 비교 베이스라인일 뿐 떼어낼 LDPC 기법 없음
- **ID**: ieee:8354375
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Doaa E. El Matary, Esam A. A. Hagras, Hala Mansour Abdel-Kader
- **PDF**: https://ieeexplore.ieee.org/document/8354375
- **Abstract**: In this paper, a Polar code is merged with Interleave Division Multiple Access-Ultra Wide Band (IDMA-UWB) to build a Polar-coded-IDMA-UWB communication system. For a multiuser UWB indoor environment, the performance is mainly limited by multipath fading and interferences as Multiple Access Interference (MAI) which is poorly approximated by a Gaussian distribution due to its impulsive nature. The main contribution of this paper is to study the effect of applying the newly coding technique, polar code, on IDMA-UWB system in terms of BER performance and complexity with good approximation for the interferences by using three different models as, Symmetric Alpha Stable (SαS), Laplace and Gaussian Mixture Model (GMM). Moreover, a comparative analysis is held between the proposed system and Low Density Parity Check (LDPC)-coded-IDMA-UWB system under the studied noise models. The results indicate that the proposed system is robust against noise and interferences with complexity much lower than LDPC-coded system.

## The application of modulo q check codes to increase the efficiency of non-binary multithreshold decoders over q-ary symmetric channel

- **Status**: ❌
- **Reason**: 비이진 multithreshold 디코더(qMTD), q-ary self-orthogonal code - non-binary GF(q) 제외 대상
- **ID**: ieee:8337291
- **Type**: conference
- **Published**: 14-16 Marc
- **Authors**: V. V. Zolotarev, G. V. Ovechkin, P. V. Ovechkin +1
- **PDF**: https://ieeexplore.ieee.org/document/8337291
- **Abstract**: Non-binary multithreshold decoders (qMTD) of q-ary self-orthogonal codes (qSOC) for q-ary symmetric channels are considered. The comparison of their efficiency with the efficiency of decoders for Reed-Solomon codes and non-binary low-density parity-check codes has been made. qMTD has shown to sufficiently exceed other error correcting methods in decoding error probability provided. The operating algorithms for encoder and decoder of concatenated code containing qSOC and modulo q check code have been offered. The application of the decoder offered for a given concatenated code has proved to decrease error decoding probability by two and more decimal orders in comparison with qMTD in the conditions of more than 10% computing complexity increase.

## Adaptive RLS Channel Estimation and SIC for Large-Scale Antenna Systems with 1-Bit ADCs

- **Status**: ❌
- **Reason**: MIMO 1-bit ADC RLS 채널추정/SIC - LDPC 무관, 떼어낼 ECC 기법 없음
- **ID**: ieee:8385500
- **Type**: conference
- **Published**: 14-16 Marc
- **Authors**: Zhichao Shao, Lukas Landau, Rodrigo de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/8385500
- **Abstract**: We propose a novel low-resolution-aware recursive least squares channel estimation algorithm for uplink multi-user multipleinput multiple-output systems. In order to reduce the energy consumption, 1-bit ADCs are used on each receive antenna. The loss of performance can be recovered by the large-scale antenna arrays at the receiver. The proposed adaptive channel estimator can mitigate the distortions due to the coarse quantization. Moreover, we propose a low-resolution-aware minimum mean square error based successive interference canceler to successively mitigate the multiuser interference. Simulation results show good performance of the system in terms of mean square error and bit error rate.

## 41.5 Tb/s Data Transport over 549 km of Field Deployed Fiber Using Throughput Optimized Probabilistic-Shaped 144QAM to Support Metro Network Capacity Demands

- **Status**: ❌
- **Reason**: 확률성형 144QAM 필드 광전송 용량 실증, 떼어낼 ECC 기법 없음
- **ID**: ieee:8386382
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Tiejun J. Xia, Daniel L. Peterson, Glenn A. Wellbrock +5
- **PDF**: https://ieeexplore.ieee.org/document/8386382
- **Abstract**: 41.5-Tb/s over 549 km of deployed SSMF in Verizon's network is achieved using probabilistic-shaped 144QAM to optimize throughput at ultra-fine granularity. This is the highest C-band only capacity and spectral efficiency in metro field environment.

## An Iterative Soft Interference Cancellation for Pilot-Assisted Optical-OFDM with LDPC Code Optimized by EXIT Chart

- **Status**: ❌
- **Reason**: 광-OFDM 간섭제거에 LDPC를 EXIT chart로 최적화 — LDPC가 응용 베이스라인, 떼어낼 ECC 기법 없음, 제외
- **ID**: ieee:8385944
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Noboru Osawa, Shinsuke Ibi, Koji Igarashi +1
- **PDF**: https://ieeexplore.ieee.org/document/8385944
- **Abstract**: This paper proposes an iterative soft interference canceller with the assistance of LDPC code for mitigating beat interference in a pilot-assisted optical-OFDM. The LDPC code is analytically optimized by EXIT chart based on Turbo principle.

## Multilevel Coding with Spatially-Coupled Codes for beyond 400Gbps Optical Transmission

- **Status**: ❌
- **Reason**: 광전송용 spatially-coupled 코드 multilevel coding, 표준 SC-LDPC를 그대로 응용 — 신규 구성/디코더 기여 불명, 제외
- **ID**: ieee:8385942
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Yohei Koganei, Tomofumi Oyama, Kiichi Sugitani +2
- **PDF**: https://ieeexplore.ieee.org/document/8385942
- **Abstract**: We propose a multilevel coding technique inheriting the performance of spatially-coupled codes. Net coding gains of 12.5, 13.2 and 13.7dB are expected for 16, 64 and 256QAM with low implementation complexity.

## Probabilistic Constellation Shaping: Challenges and Opportunities for Forward Error Correction

- **Status**: ❌
- **Reason**: 광통신 probabilistic constellation shaping과 FEC 논의 — LDPC 이식 기법 없는 무선/광통신 응용, 제외
- **ID**: ieee:8385783
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Laurent Schmalen
- **PDF**: https://ieeexplore.ieee.org/document/8385783
- **Abstract**: We discuss the impact of probabilistic amplitude shaping on the forward error correction stage in future optical transceivers and highlight some potential pitfalls, as well as challenges and opportunities for future research that may arise.

## Generation and Intradyne Detection of Single-Wavelength 1.61-Tb/s Using an All-Electronic Digital Band Interleaved Transmitter

- **Status**: ❌
- **Reason**: 단일파장 1.61Tb/s QAM 송신기 생성/검출, ECC 무관 광전송
- **ID**: ieee:8386370
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: X. Chen, S. Chandrasekhar, G. Raybon +4
- **PDF**: https://ieeexplore.ieee.org/document/8386370
- **Abstract**: We generate 100-GHz wide in-phase and quadrature electrical signals via two synchronized digital band interleaved digital-to-analog converters and demonstrate single-wavelength digital band multiplexed QAM with an aggregate all-electronically generated line rate of 1.61 Tb/s.

## Efficient Offline Evaluation of FEC Codes Based on Captured Data with Probabilistic Shaping

- **Status**: ❌
- **Reason**: shaping 신호로 FEC 오프라인 평가 툴 — 떼어낼 ECC 디코더/구성 기법 없음, 제외
- **ID**: ieee:8385846
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Tsuyoshi Yoshida, Magnus Karlsson, Erik Agrell
- **PDF**: https://ieeexplore.ieee.org/document/8385846
- **Abstract**: We propose a tool for reusing experimental or simulation data of probabilistically shaped signals with different FEC codes. A single recorded histogram of log-likelihood ratios is sufficient to examine arbitrary coding at low BERs.

## SDN-Based Application Driven In-Band Adaptive Coding in Data Centers

- **Status**: ❌
- **Reason**: SDN 기반 적응형 코딩 광스위칭, 채널 ECC 디코더/구성 기법 없음
- **ID**: ieee:8386074
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Mingwei Yang, Houman Rastegarfar, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/8386074
- **Abstract**: A software-defined adaptive coding scheme is experimentally implemented and evaluated for 50 Gbps 4-PAM optical switching in wavelength-routing DCs. Up to 1 dB reduction in transmission power is achieved with switching latencies of hundreds of milliseconds.

## Record-High 17.3-bit/s/Hz Spectral Efficiency Transmission over 50 km Using Probabilistically Shaped PDM 4096-QAM

- **Status**: ❌
- **Reason**: 확률성형 4096-QAM 분광효율 전송실험, LDPC 기법 없음
- **ID**: ieee:8386374
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Samuel L.I. Olsson, Junho Cho, Sethumadhavan Chandrasekhar +3
- **PDF**: https://ieeexplore.ieee.org/document/8386374
- **Abstract**: We demonstrate transmission of a 10-subcarrier superchannel with a record-high intra-channel spectral efficiency of 17.3 bit/s/Hz over 50-km backward Raman amplified Corning® Vascade® EX2000 fiber using 3-GBd probabilistically shaped PDM 4096-QAM.

## Single-Channel 480-Gb/s Direct Detection of POL-MUX IQ Signal Using Single-Sideband Stokes Vector Receiver

- **Status**: ❌
- **Reason**: 광 direct detection 수신기, LDPC/ECC 무관 — 제외
- **ID**: ieee:8385890
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Di Che, Chuanbowen Sun, William Shieh
- **PDF**: https://ieeexplore.ieee.org/document/8385890
- **Abstract**: We propose the single-sideband Stokes vector receiver to demultiplex a 4-D signal that fundamentally solves the carrier fading of POL-MUX direct detection, verified by a POL-MUX 60-Gbaud 16-QAM transmission over 80-km SSMF with digital dispersion post-compensation.

## On Joint Design of Probabilistic Shaping and Forward Error Correction for Optical Systems

- **Status**: ❌
- **Reason**: 광시스템 probabilistic shaping+FEC 결합설계 튜토리얼, 신규 디코더/구성 없음 — 제외
- **ID**: ieee:8385842
- **Type**: conference
- **Published**: 11-15 Marc
- **Authors**: Georg Böcherer
- **PDF**: https://ieeexplore.ieee.org/document/8385842
- **Abstract**: These slides provide an extended abstract for the tutorial On Joint Design of Probabilistic Shaping and Forward Error Correction for Optical Systems to be held at the OFC 2018 in San Diego, USA. Recently, many works on probabilistic shaping experiments, e.g., [1][2][3] and work on how to optimize input distributions, e.g., [4][5][6] were presented at optical conferences and in journals on optical communications. Complementary to that, this tutorial presents generic tools to assess optical transmission measurements. Uncertainty is introduced to assess the noise level. The achievable binary code rate, ABC rate, is used to determine the feasible forward error correction (FEC) rates, and probabilistic amplitude shaping, PAS, achievable rates are used to determine feasible spectral efficiencies (SE).

## Hard Decoding Based Design of Regular LDPC using LabVIEW

- **Status**: ❌
- **Reason**: 표준 regular Neal-McKay LDPC를 LabVIEW로 단순 구현, 신규 디코더/구성/HW 기여 없음
- **ID**: ieee:8550941
- **Type**: conference
- **Published**: 1-3 March 
- **Authors**: Ninad Chitnis, Tanvi Joshi, Shreyas Padte +2
- **PDF**: https://ieeexplore.ieee.org/document/8550941
- **Abstract**: High speed internet access for all is fast becoming a reality. Noise and bit errors affecting a bit stream in a medium makes it necessary to encode the voice data being transmitted over IP networks, thereby allowing reduction in noise at the receiving end and accurately reconstruct the transmitted audio data. This paper proposes a LabViewbased implementation of regular Neal and McKay LDPC codes for audio transmission. It examines 2 case studies of such an implementation for 16 bit and 32 bit LDPC with the message vector 8 bit long in both the cases. Pearson's degree of correlation for these two cases shows a greater value for 32 bit code design as compared to 16 bit design. The authors can safely extrapolate from this result that a design with a sufficiently high number of parity check bits, will make it possible to reconstruct an error free audio representation of the transmitted data.
