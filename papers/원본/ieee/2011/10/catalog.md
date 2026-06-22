# IEEE Xplore — 2011-10


## LDPCA Code Construction for Slepian-Wolf Coding

- **Status**: ❌
- **Reason**: Slepian-Wolf 분산소스코딩용 LDPCA 구성 — 소스코딩(채널 ECC 아님), 원칙 제외
- **ID**: ieee:5992705
- **Type**: journal
- **Published**: October 20
- **Authors**: Jeffrey J. Micallef, Reuben A. Farrugia, Carl J. Debono
- **PDF**: https://ieeexplore.ieee.org/document/5992705
- **Abstract**: Error correcting codes used for Distributed Source Coding (DSC) generally assume a random distribution of errors. However, in certain DSC applications, prediction of the error distribution is possible and thus this assumption fails, resulting in a sub-optimal performance. This letter considers the construction of rate-adaptive Low-Density Parity-Check (LDPC) codes where the edges of the variable nodes receiving unreliable information are distributed evenly among all the check nodes. Simulation results show that the proposed codes can reduce the gap to the theoretical bounds by up to 56% compared to traditional codes.

## Designing Rate-Compatible Irregular Repeat Accumulate Codes through Splitting

- **Status**: ✅
- **Reason**: rate-compatible IRA 부호의 splitting 기반 신규 구성 — 바이너리 LDPC 계열 코드설계 기법(E), 애매하나 살림
- **ID**: ieee:5992709
- **Type**: journal
- **Published**: October 20
- **Authors**: Min Xiao, Lin Wang, Jing Li
- **PDF**: https://ieeexplore.ieee.org/document/5992709
- **Abstract**: A new scheme of rate-compatible (RC) irregular repeat accumulate (IRA) codes is proposed which can be encoded and decoded using a single encoder-decoder pair and which can provide good performance across a wide range of code rates. Conventional strategies generally start from a low-rate mother code and puncture the rate up. Considering that the initial transmissions (and hence the higher-rate codes) are most important, we propose to start from a good high-rate code and "split" the rate down. Rather than do it gradually in a greedy manner, we propose to design a good one-shot-split to control the worst-case (lowest-rate) performance, and subsequently work out all the intermediate rates. We show the proposed strategy is both simple and powerful resulting in RC-IRA codes that outperform the existing ones.

## Comments on "Theoretical Analysis of a MAP Based Blind Frame Synchronizer"

- **Status**: ❌
- **Reason**: LDPC blind 프레임 동기화 오류율 추정 코멘트 — 동기화 응용, 떼어낼 ECC 기법 없음
- **ID**: ieee:6002429
- **Type**: journal
- **Published**: October 20
- **Authors**: Yinghao Qi, Bo Wang, Mengtian Rong +1
- **PDF**: https://ieeexplore.ieee.org/document/6002429
- **Abstract**: In this comment, we present a new estimation procedure for the blind frame synchronization error rate (FSER) based on analysis in . Simulations verify that the estimate is tight for low density parity check (LDPC) codes having large column weight. We show that regular LDPC codes have better synchronization performance than irregular LDPC codes having the same row weight distribution.

## Effective Informed Dynamic Scheduling for Belief Propagation Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LDPC BP의 informed dynamic scheduling(residual 기반, trapping set 극복) — 이식 가능한 디코더 알고리즘(C)
- **ID**: ieee:5963620
- **Type**: journal
- **Published**: October 20
- **Authors**: Yi Gong, Xingcheng Liu, Weicai Ye +1
- **PDF**: https://ieeexplore.ieee.org/document/5963620
- **Abstract**: The simultaneous flooding scheduling is popular for Low-Density Parity-Check (LDPC) Belief Propagation (BP) decoding. Non-simultaneous sequential scheduling is superior to the flooding scheduling, and asynchronous dynamic scheduling has better FER performance than the sequential scheduling. However, all strategies encounter the trouble of locating the error variable node. This paper proposes an informed dynamic scheduling strategy, which utilizes the instability of the variable node and the residual of the variable-to-check message to locate the message to be updated first. The informed dynamic scheduling overcomes the trapping sets effectively. This paper also designs an informed dynamic scheduling strategy with adaptivity to pass more messages in parallel, which effectively postpones the influence of cycles in the Tanner graph. In some sense, the strategy lengthens cycles. Simulation results show that the two informed dynamic scheduling strategies outperform other algorithms.

## Serial Decoding of Rateless Code Over Noisy Channels

- **Status**: ❌
- **Reason**: rateless 부호의 serial BP 디코딩 — fountain/rateless 응용 특이적, NAND 채널 ECC로 이식할 기법 없음
- **ID**: ieee:11285768
- **Type**: journal
- **Published**: October 20
- **Authors**: Ke-Di Wu, Zhao-Yang Zhanc, Shao-Lei Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/11285768
- **Abstract**: Rateless code usually generates a potentially infinite number of coded packets at the encoder and collects enough packets at the decoder to ensure reliable recovery of multiple information packets. The conventional rateless decoder usually works in a parallel manner which needs to initiate a new belief propagation (BP) decoding procedure upon each newly received collection of coded packets, thereby resulting in prohibitive decoding complexity in practice. In this paper, we present a novel serial decoding algorithm, i.e., the serial storage belief propagation (SS BP) algorithm, for rateless codes over noisy channels. Specifically, upon receiving a new group of coded packets, the decoder initiates a new attempt to decode all the packets received so far, using the results of the previous attempt as initial input. Moreover, in each iteration of the new attempt, the decoder serially propagates the messages group by group from the most recent one to the earliest one. In this way, the newly updated messages can be propagated faster, expediting the recovery of information packets. In addition, the proposed serial decoding algorithm has significantly lower complexity than the existing parallel decoding algorithms. Simulation results validate its effectiveness in AWGN, Rayleigh, and Rician fading channels.

## Frame Synchronization of Coded Modulations in Time-Varying Channels via Per-Survivor Processing

- **Status**: ❌
- **Reason**: coded modulation 프레임 동기화(trellis/per-survivor) — 동기화 응용, LDPC ECC 기법 아님
- **ID**: ieee:5963618
- **Type**: journal
- **Published**: October 20
- **Authors**: Heon Huh, James V. Krogmeier
- **PDF**: https://ieeexplore.ieee.org/document/5963618
- **Abstract**: In this letter, an optimum frame synchronizer is proposed for coded modulations in channels with uncertainties. Coded modulations include various frame synchronization scenarios, e.g., convolutionally coded transmissions and nonlinear modulations with memory. Frame synchronization is proposed as a maximum a posteriori probability estimation implemented using trellis path search for Markov chain decoding. In addition, time-varying uncertainties such as frequency offset and phase noise are jointly estimated via per-survivor processing as frame synchronization proceeds. The proposed frame synchronizer exploits the coding gain of coded modulations to achieve better performance than conventional frame synchronizers. We show that the resulting frame synchronizer consists of a correlation term and two data correction terms. Numerical results show that the proposed frame synchronizer is robust to uncertainties at the receiver and it exhibits improved performance.

## A Study on Nonbinary LDPC Coding and Iterative Decoding System in BPM R/W Channel

- **Status**: ❌
- **Reason**: 비이진 GF(2^8) LDPC 연구로 바이너리 한정 기준에서 제외
- **ID**: ieee:6028104
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Yasuaki Nakamura, Yasuhisa Bandai, Yoshihiro Okamoto +3
- **PDF**: https://ieeexplore.ieee.org/document/6028104
- **Abstract**: In this paper, the iterative decoding system using the nonbinary low-density parity-check (LDPC) code is studied in the magnetic recording system using a bit-patterned media (BPM) R/W channel affected by the write head field gradient, the media switching field distribution (SFD), the demagnetization field from adjacent dots, and the dot position deviation in an areal recording density of 2 Tb/in2. The performance of iterative decoding system using the nonbinary LDPC code over Galois field of GF(28) is evaluated by the computer simulation, and it is compared with the conventional iterative decoding system using the binary LDPC code. The results show that the nonbinary LDPC system provides better performance compared with the binary LDPC system.

## Construction of protograph LDPC codes with circular generator matrices

- **Status**: ✅
- **Reason**: 바이너리 protograph QC-LDPC + circular generator로 인코딩 복잡도 저감(코드설계 E)
- **ID**: ieee:6077669
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Kaiyao Wang, Yang Xiao, Kiseon Kim
- **PDF**: https://ieeexplore.ieee.org/document/6077669
- **Abstract**: The application of protograph low density parity check (LOpe) codes involves the encoding complexity problem. Since the generator matrices are dense, and if the positions of “1” s are irregularity, the encoder needs to store every “1” of the generator matrices by using huge chip area. In order to solve this problem, we need to design the protograph LDPC codes with circular generator matrices. A theorem concerning the circulating property of generator matrices of nonsingular protograph LDPC codes is proposed. The circulating property of generator matrix of nonsingular protograph LDPC codes can be obtained from the corresponding quasi-cyclic parity check matrix. This paper gives a scheme of constructing protograph LDPC codes with circulating generator matrices, and it reveals that the fast encoding algorithm of protograph LDPC codes has lower encoding complexity under the condition of the proposed theorem. Simulation results in additive white Gaussian noise (AWGN) channels show that the bit error rate (BER) performance of the designed codes based on the proposed theorem is much better than that of GB20600 LDPC codes and Tanner LDPC codes.

## Multiplicatively Repeated Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC — 바이너리 한정 기준에 따라 제외
- **ID**: ieee:6034722
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Kenta Kasai, David Declercq, Charly Poulliat +1
- **PDF**: https://ieeexplore.ieee.org/document/6034722
- **Abstract**: We propose nonbinary LDPC codes concatenated with multiplicative repetition codes. By multiplicatively repeating the (2,3)-regular nonbinary LDPC mother code of rate 1/3, we construct rate-compatible codes of lower rates 1/6, 1/9, 1/12,.... Surprisingly, such simple low-rate nonbinary LDPC codes outperform the best low-rate binary LDPC codes so far. Moreover, we propose the decoding algorithm for the proposed codes, which can be decoded with almost the same computational complexity as that of the mother code.

## Serial Belief Propagation for The High-Rate LDPC Decoders and Performances in The Bit Patterned Media Systems With Media Noise

- **Status**: ✅
- **Reason**: serial BP(직렬 스케줄링) 디코더로 수렴속도·BER 개선 제시, 부호 비의존 BP 개선 기법으로 바이너리 LDPC에 이식 가능(카테고리C)
- **ID**: ieee:6028143
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Watid Phakphisut, Pornchai Supnithi, Thanomsak Sopon +1
- **PDF**: https://ieeexplore.ieee.org/document/6028143
- **Abstract**: In this work, we propose to use the serial belief propagation or serial scheduling in the 2-D bit patterned media (BPM) system with media noise. The serial scheduling methods are applied to the random LDPC codes and quasi-cyclic LDPC (QC-LDPC) codes of high code rates. Both are constructed from the progress-edge growth (PEG) algorithm. We compare the performance of the LDPC codes using the serial belief propagation and the conventional belief propagation (BP) decoding. The simulation results show that the serial scheduling provides a faster convergence speed and a better bit error rate performance than the conventional BP in an AWGN channel. The serial belief propagation is also shown to offer the performance gains over the BP decoding for the BPM system with various media noise levels.

## New Method of Areal Density Capability Determination for Digital Magnetic Recording System

- **Status**: ❌
- **Reason**: 자기기록 면밀도 측정 방법론 연구; ECC/LDPC 디코더·코드·HW 기여 전무
- **ID**: ieee:6028223
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Xinzhi Xing, Davide Guarisco, Guang Yang +3
- **PDF**: https://ieeexplore.ieee.org/document/6028223
- **Abstract**: Areal density capability of a recording system is traditionally determined in two steps. Linear density is first determined by on-track error rate. Track density is then determined by off-track read capability (OTRC) at the linear density chosen in step one (IEEE Transactions on Magnetics, vol. MAG-26, no. 5, pp. 1689-1693, Sep. 1990). With advances in technologies and changes in drive requirements, this traditional method does not necessarily reflect the current requirements and limitations of high density recording. In this paper, a new method to experimentally determine areal density capability is proposed. The limiting factors and demands to recording components will also be discussed.

## A Construction of Quantum Stabilizer Codes Based on Syndrome Assignment by Classical Parity-Check Matrices

- **Status**: ❌
- **Reason**: 양자 stabilizer 부호 구성; commutative/스태빌라이저 조건에 의존하여 고전 바이너리 LDPC 이식 불가
- **ID**: ieee:6034728
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Ching-Yi Lai, Chung-Chin Lu
- **PDF**: https://ieeexplore.ieee.org/document/6034728
- **Abstract**: In this paper, a new but simple construction of stabilizer codes and related entanglement-assisted quantum error-correcting codes is proposed based on syndrome assignment by classical parity-check matrices. This method turns the construction of quantum stabilizer codes to the construction of classical parity-check matrices satisfying a specific commutative condition. The designed minimum distance 2t*+1 of the constructed quantum stabilizer codes can be achieved by a commutative classical parity-check matrix with classical minimum distance 4t*-m, where the parameter m, 0 ≤ m ≤ 2t*, depends on a property of the parity-check matrix. As m decreases, there is an increasing set of additional correctable error operators beyond the designed error correcting capability t*. The (asymptotic) coding efficiency is at least comparable to that of CSS codes. A class of quantum Reed-Muller codes is constructed and codes in this class have a larger set of correctable error operators than that of the quantum Reed-Muller codes previously developed in the literature. Quantum circulant codes are also constructed and many of them are optimal in terms of their coding parameters.

## A Novel Error-Correcting System Based on Product Codes for Future Magnetic Recording Channels

- **Status**: ✅
- **Reason**: 바이너리 LDPC+RS 곱부호 신규 구성과 신규 디코딩 알고리즘 2종 제시; 코드설계/디코더 측면 이식 검토 가치 있어 in으로 살림(Phase3 재검토)
- **ID**: ieee:6028152
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Tam Van Vo, Seiichi Mita
- **PDF**: https://ieeexplore.ieee.org/document/6028152
- **Abstract**: We propose a novel construction of product codes for high-density magnetic recording based on binary low-density parity check (LDPC) codes and binary image of Reed-Solomon (RS) codes. Moreover, two novel algorithms are proposed to decode the codes in the presence of AWGN errors and scattered hard errors (SHEs). Simulation results show that at a bit-error rate (BER) of approximately 10-8 , our method allows improving the error performance by approximately 1.9 dB compared with that of a hard decision decoder of RS codes of the same length and code rate. For the mixed error channel, including random noise and SHEs, the signal-to-noise ratio is set at 5 dB, and 150 to 400 SHEs are randomly generated. The bit-error performance of the proposed product code shows a significant improvement over that of equivalent random LDPC codes or serial concatenation of LDPC and RS codes.

## Weighted symbol-flipping decoding algorithm for nonbinary LDPC codes with flipping patterns

- **Status**: ❌
- **Reason**: 비이진(nonbinary) GF(q) LDPC symbol-flipping — 바이너리 한정 기준에 따라 제외
- **ID**: ieee:6077670
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Bing Liu, Jun Gao, Wei Tao +1
- **PDF**: https://ieeexplore.ieee.org/document/6077670
- **Abstract**: A novel low-complexity weighted symbol-flipping algorithm with flipping patterns to decode nonbinary low-density parity-check codes is proposed. The proposed decoding procedure updates the hard-decision received symbol vector iteratively in search of a valid codeword in the symbol vector space. Only one symbol is flipped in each iteration, and symbol flipping function, which is employed as the symbol flipping metric, combines the number of failed checks and the reliabilities of the received bits and calculated symbols. A scheme to avoid infinite loops and select one symbol to flip in high order Galois field search is also proposed. The design of flipping pattern's order and depth, which is dependent of the computational requirement and error performance, is also proposed and exemplified. Simulation results show that the algorithm achieves an appealing tradeoff between performance and computational requirement over relatively low Galois field for short to medium code length.

## Reduction of Bit Errors Due to Intertrack Interference Using LLRs of Neighboring Tracks

- **Status**: ❌
- **Reason**: 인접트랙 LLR 활용 ITI/ISI 반복 제거(자기기록 채널 검출기 특이적); NAND로 떼어낼 LDPC 디코더·코드 기법 없음
- **ID**: ieee:6028085
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Seiichi Mita, Vo Tam Van, Fumiya Haga
- **PDF**: https://ieeexplore.ieee.org/document/6028085
- **Abstract**: Suppressing intertrack interference (ITI) and intersymbol interference (ISI) is crucial for achieving high-density magnetic recording beyond 10 Tera bits/inch2. We propose a novel iterative method for reducing errors caused by ITI and ISI involving the adaptive estimation of ITI and the log likelihood ratios obtained from signals of neighboring tracks. This method is useful for decoding signals recorded by bit-patterned media and conventional media. Moreover, the method is extended to decode signals from the Voronoi-based discrete grain model for shingled write recording (SWR), accounting for four neighboring bits. Bit errors due to both neighboring track shifts of approximately 20% can be canceled for BPM and SWR.

## Analysis of Verification-Based Decoding on the $q$-ary Symmetric Channel for Large $q$

- **Status**: ❌
- **Reason**: verification-based 디코더지만 q-ary symmetric channel(비이진) 대상, 심볼 리스트 기반으로 바이너리 BP에 이식 부적합
- **ID**: ieee:6034757
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Fan Zhang, Henry D. Pfister
- **PDF**: https://ieeexplore.ieee.org/document/6034757
- **Abstract**: A new verification-based message-passing decoder for low-density parity-check (LDPC) codes is introduced and analyzed for the q-ary symmetric channel (q-SC). Rather than passing messages consisting of symbol probabilities, this decoder passes lists of possible symbols and marks some lists as verified. The density evolution (DE) equations for this decoder are derived and used to compute decoding thresholds. If the maximum list size is unbounded, then one finds that any capacity-achieving LDPC code for the binary erasure channel can be used to achieve capacity on the q -SC for large q. The decoding thresholds are also computed via DE for the case where each list is truncated to satisfy a maximum list-size constraint. Simulation results are also presented to confirm the DE results. During the simulations, we observed differences between two verification-based decoding algorithms, introduced by Luby and Mitzenmacher, that were implicitly assumed to be identical. In this paper, the node-based algorithms are evaluated via analysis and simulation. The probability of false verification (FV) is also considered and techniques are discussed to mitigate the FV. Optimization of the degree distribution is also used to improve the threshold for a fixed maximum list size. Finally, the proposed algorithm is compared with a variety of other algorithms using both density evolution thresholds and simulation results.

## Concatenated Coding for the AWGN Channel With Noisy Feedback

- **Status**: ❌
- **Reason**: 피드백 기반 concatenated coding; LDPC/turbo는 시뮬레이션 베이스라인일 뿐 이식 가능 ECC 기법 없음
- **ID**: ieee:6034712
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Zachary Chance, David J. Love
- **PDF**: https://ieeexplore.ieee.org/document/6034712
- **Abstract**: The use of open-loop coding can be easily extended to a closed-loop concatenated code if the transmitter has access to feedback. This can be done by introducing a feedback transmission scheme as an inner code. In this paper, this process is investigated for the case when a linear feedback scheme is implemented as an inner code and, in particular, over an additive white Gaussian noise (AWGN) channel with noisy feedback. To begin, we look to derive an optimal linear feedback scheme by optimizing over the received signal-to-noise ratio (SNR). From this optimization, a linear feedback scheme is produced that is asymptotically optimal in the sense of blocklength-normalized SNR; it is then compared to other well-known schemes. Then, the linear feedback scheme is implemented as an inner code to a concatenated code over the AWGN channel with noisy feedback. This code shows improvements not only in error exponent bounds, but also in bit error rate (BER) and frame error rate (FER). It is also shown that if the concatenated code has total blocklength L and the inner code has blocklength, N, the inner code blocklength should scale as N = O(C/R), where C is the capacity of the channel and R is the rate of the concatenated code. Simulations with low-density parity-check (LDPC) and turbo codes are provided to display practical applications and their error rate benefits.

## Intertrack Interference Cancellation for Shingled Magnetic Recording

- **Status**: ❌
- **Reason**: HDD ITI 캔슬레이션 채널 신호처리/구현; LDPC 디코더·코드 기여 없음, NAND 이식 기법 없음
- **ID**: ieee:6028121
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Erich F. Haratsch, George Mathew, Jongseung Park +3
- **PDF**: https://ieeexplore.ieee.org/document/6028121
- **Abstract**: The intertrack interference in squeezed tracks of a magnetic hard disk drive is investigated based on captured waveforms. Specifically, extracted intertrack interference impulses and statistics are presented as a function of track squeeze and read offset. The bit-error-rate improvement of intertrack interference cancellation is shown based on simulations with captured drive waveforms. Architecture and implementation aspects for hard disk drives with intertrack interference cancellation are described.

## Compressive Sampling With Generalized Polygons

- **Status**: ❌
- **Reason**: 압축센싱(compressed sensing) 측정행렬 구성 및 복원 알고리즘으로 채널 ECC 아님; BP는 부수 언급일 뿐 NAND LDPC 이식 기법 없음
- **ID**: ieee:5934614
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Kanke Gao, Stella N. Batalama, Dimitris A. Pados +1
- **PDF**: https://ieeexplore.ieee.org/document/5934614
- **Abstract**: We consider the problem of compressed sensing and propose new deterministic low-storage constructions of compressive sampling matrices based on classical finite-geometry generalized polygons. For the noiseless measurements case, we develop a novel exact-recovery algorithm for strictly sparse signals that utilizes the geometry properties of generalized polygons and exhibits complexity that depends on the sparsity value only. In the presence of measurement noise, recovery of the generalized-polygon sampled signals can be carried out effectively using a belief propagation algorithm. Experimental studies included in this paper illustrate our theoretical developments.

## Performance Evaluation of ITI Canceller Using Granular Medium Model

- **Status**: ❌
- **Reason**: SMR ITI 캔슬러 채널 검출 연구; LDPC 신규 디코더·코드설계 기여 없는 채널 특이적 신호처리
- **ID**: ieee:6027766
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Yoshihiro Okamoto, Kazumasa Ozaki, Masato Yamashita +3
- **PDF**: https://ieeexplore.ieee.org/document/6027766
- **Abstract**: The performance of an iterative decoding system is evaluated in shingled magnetic recording (SMR). The medium model is made by a discrete Voronoi model, and the 2-D sensitivity function of reader is used to obtain the reproducing waveform. As the sensitivity function extends to adjacent tracks, intertrack interference (ITI) deteriorates the signal detection system. In order to recover the intrinsic performance, it is required to reduce the influence of ITI to the system. Then, the ITI canceller is employed to combat ITI for the iterative decoding system, and the performance is evaluated by computer simulation. The results show that the introduction of ITI canceller improves the bit-error-rate performance in SMR system.

## Timing and Written-In Errors Characterization for Bit Patterned Media

- **Status**: ❌
- **Reason**: BPMR/HDD write-in error 특성화만; 떼어낼 LDPC 디코더/HW/코드설계 기법 없음
- **ID**: ieee:6028267
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Songhua Zhang, Kui Cai, Maria Lin-Yu +5
- **PDF**: https://ieeexplore.ieee.org/document/6028267
- **Abstract**: Synchronous writing in BPMR has been recognized as a crucial yet challenging issue. It has been shown that position jitter and switching field distribution can lead to spatially uncorrelated random write failures. On top of that, the spindle speed variation and other mechanical vibration may lead to accumulative phase drift during writing which causes long streams of insertion/deletion write failures. However no experiments have been conducted to quantitatively testify the later concept, nor provide precise written-in error characteristics when both phenomena are present in BPMR systems. This gap of understanding is filled by this work through spinstand and hard disk measurements and analysis. It is shown that timing inaccuracy not only introduces insertion/deletion write failures but also given rise to substantial increase of substitution (random) write errors. It also reveals that instead of the commonly accused spindle motor speed variation, timing error in BPMR based HDD may well be the result of estimation error due to limited or improperly configured timing preambles.

## Modeling of 2-D Magnetic Recording and a Comparison of Data Detection Schemes

- **Status**: ❌
- **Reason**: 2D 자기기록 GFP/GMM 검출 모델링 및 면밀도 비교 연구; 표준 random/QC-LDPC 그대로 사용, 새 디코더·구성 기여 없음
- **ID**: ieee:6027618
- **Type**: journal
- **Published**: Oct. 2011
- **Authors**: Moulay Rachid Elidrissi, Kheong Sann Chan, Kim Keng Teo +4
- **PDF**: https://ieeexplore.ieee.org/document/6027618
- **Abstract**: Two-dimensional magnetic recording (TDMR) together with shingled magnetic recording (SMR) are technologies proposed to extend the life of conventional granular magnetic recording. The grain flipping probability (GFP) model has been proposed to mimic the performance of micromagnetic ( μ-mag) simulations for the purpose of signal reproduction. Other work in TDMR includes the proposal of a Gaussian mixture model (GMM) that produces improved likelihood information at the output of the detector, combined with low density parity check (LDPC) codes. The contribution of this paper is threefold. First, we aim to simulate a TDMR/SMR recording system with the GFP model, both with and without the GMM detector, and with various random and structured LDPC codes, of both 4 k and 16 k block lengths, to determine areal densities that might be achieved. Second, we perform a comparison of the various model order reduced (MOR) GFP implementations to compare the effect of writing with various factors taken out of the picture. Third, we perform a validation of the GFP model and the setup as a whole, by running the system with a parameter set close to that of conventional recording. The results of these experiments give an assurance of the validity of our model, give an indication of the expected density that might be achieved in a TDMR/SMR system, and give a direction for which parameter(s) in magnetic recording systems might be optimized to yield the most gain.

## An experimental investigation of high-rate nonbinary quasi-cyclic LDPC-coded modulation for coherent optical communication

- **Status**: ❌
- **Reason**: 비이진(nonbinary) QC-LDPC coded modulation 광통신 실험 — 비이진 LDPC는 제외 대상
- **ID**: ieee:6110474
- **Type**: conference
- **Published**: 9-13 Oct. 
- **Authors**: Xuezhi Hong, Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6110474
- **Abstract**: A rate-0.83 nonbinary quasi-cyclic LDPC-coded modulation scheme is experimentally investigated in a coherent optical QPSK system. Large coding gains are observed for both I/Q well balanced and highly imbalanced cases. By increasing the BCJR equalizer's memory, degradation caused by insufficient receiver bandwidth is successfully mitigated.

## Polarization-multiplexed nonbinary LDPC-coded modulation with optimal signal constellations

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC-coded modulation, 바이너리 한정 위배
- **ID**: ieee:6110475
- **Type**: conference
- **Published**: 9-13 Oct. 
- **Authors**: Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6110475
- **Abstract**: We propose using nonbinary LDPC-coded modulation with optimal constellations obtained via iterative polar quantization (IPQ). The proposed scheme significantly outperforms its prior-art bit-interleaved LDPC-coded modulation counterpart, e.g., by 2.78 dB for the 128-point IPQ constellation.

## Exploring the vulnerability of CMPs to soft errors with 3D stacked non-volatile memory

- **Status**: ❌
- **Reason**: STT-RAM 3D 스택 소프트에러 내성 아키텍처, ECC/LDPC 기법 없음
- **ID**: ieee:6081425
- **Type**: conference
- **Published**: 9-12 Oct. 
- **Authors**: Guangyu Sun, Eren Kursun, Jude A. Rivers +1
- **PDF**: https://ieeexplore.ieee.org/document/6081425
- **Abstract**: Spin-transfer Torque Random Access Memory (STT-RAM) emerges for on-chip memory in microprocessor architectures. Thanks to the magnetic field based storage STT-RAM cells have immunity to radiation induced soft errors that affect electrical charge based data storage, which is a major challenge in SRAM based caches in current microprocessors. In this study we explore the soft error resilience benefits and design trade offs of 3D-stacked STT-RAM for multi-core architectures. We use 3D stacking as an enabler for modular integration of STT-RAM caches with minimum disruption in the baseline processor design flow, while providing further interconnectivity and capacity advantages. We take an in-depth look at alternative replacement schemes in terms of performance, power, temperature, and reliability trade-offs to capture the multi-variable optimization challenges microprocessor architectures face. We analyze and compare the characteristics of STT-RAM, SRAM, and DRAM alternatives for various levels of the cache hierarchy in terms of reliability.

## Probabilistic fault diagnosis and its analysis in multicomputer systems

- **Status**: ❌
- **Reason**: 멀티컴퓨터 결함진단 모델/알고리즘, ECC/LDPC와 무관
- **ID**: ieee:6083862
- **Type**: conference
- **Published**: 9-12 Oct. 
- **Authors**: Manabu Kobayashi, Toshinori Takabatake, Toshiyasu Matsushima +1
- **PDF**: https://ieeexplore.ieee.org/document/6083862
- **Abstract**: F.P.Preparata et al. have proposed a fault diagnosis model to find all faulty units in the multicomputer system by using outcomes which each unit tests some other units. In this paper, for probabilistic diagnosis models, we show an efficient diagnosis algorithm to obtain a posteriori probability that each of units is faulty given the test outcomes. Furthermore, we propose a method to analyze the diagnostic error probability of this algorithm.

## Comparative Analysis of Various Optimization Techniques with Coded MIMO-OFDM Transmission

- **Status**: ❌
- **Reason**: MIMO-OFDM 검출기 비교, LDPC는 부수 언급 — 떼어낼 ECC 기법 없음
- **ID**: ieee:6112868
- **Type**: conference
- **Published**: 7-9 Oct. 2
- **Authors**: Shivendra Singh, Sumit Raghuvanshi
- **PDF**: https://ieeexplore.ieee.org/document/6112868
- **Abstract**: This paper deals with the comparison of various optimization techniques used for detection of spatially multiplexed transmitted symbols in multiple input multiple output orthogonal frequency division multiplexing (MIMO OFDM) system. It may be helpful in evaluating the performance of the detection techniques viz zero forcing (ZF), minimum mean square error (MMSE) and maximum likelihood (ML) on the basis of the bit error rate (BER) for a given signal to noise ratio (SNR). A 2×2 MIMO system is used for the performance evaluation in simulation. The receiver decodes the binary phase shift keying (BPSK) signal through low density parity check (LDPC) decoder. A simulation result shows that ML is having a better performance over ZF and MMSE.

## Memory efficient LDPC decoder design

- **Status**: ✅
- **Reason**: LDPC 디코더 양자화 워드길이 단축 스킴으로 메모리 HW 복잡도 저감; 이식 가능 양자화/HW 기법(C/D)
- **ID**: ieee:6075087
- **Type**: conference
- **Published**: 6-7 Oct. 2
- **Authors**: Yuan Yao, Wei Liang, Fan Ye +1
- **PDF**: https://ieeexplore.ieee.org/document/6075087
- **Abstract**: Hardware complexity of LDPC decoders, which is caused by storage and processing of massive information, is the major reason that encumbers LDPC codes from widely application. Reducing the quantization word length of decoding information can effectively decrease the hardware complexity. But for the absolute value of information keeps increasing during decoding, short word length with finite quantization ranges will lead to serious saturation errors and damage decoding performance. Two quantization schemes is proposed in this paper to reduce the number of memory bits required by decoder design by using short word length while guarantee bit-error-rate (BER) performance. Results shows that these two quantization schemes can simplify the hardware complexity with very little loss of decoding performance.

## Binary and nonbinary LDPC-coded modulations for generalized fading channels

- **Status**: ❌
- **Reason**: 바이너리/비이진 LDPC-coded modulation 페이딩 비교 — 표준 부호 비교, 떼어낼 신규 디코더/구성 없음(무선 응용)
- **ID**: ieee:6112023
- **Type**: conference
- **Published**: 5-8 Oct. 2
- **Authors**: Murat Arabaci, Ivan B. Djordjevic
- **PDF**: https://ieeexplore.ieee.org/document/6112023
- **Abstract**: In this paper, we compare binary and nonbinary LDPC-coded modulation schemes with high-rate component codes, which are more suitable for high-speed wireless communication applications than schemes employing low-rate codes. In order to test the performance of these schemes under various fading conditions, we use two generalized fading distributions, namely the a-μ distribution and the K-μ distribution. By adjusting the parameters a, k, and μ, we simulate the conventional Rician, Rayleigh, and Nakagami-m fading cases. Further, to provide an example for cases where the field measurements may exhibit better fit to nonconventional distributions, we also study a heuristic fading scenario. Using QPSK modulation, we observe that binary and nonbinary LDPC-coded modulation schemes perform closely under all fading conditions considered. However, in terms of receiver latency, the nonbinary LDPC-coded modulation scheme may lower receiver latency especially when complex equalization schemes are employed since NB-LDPC-CM avoids using iterative equalization and decoding which is a crucial component in binary LDPC-coded modulation schemes.

## MAP decoding of MTR codes in multiple-head magnetic recording systems

- **Status**: ❌
- **Reason**: MTR 부호 MAP 디코딩(자기기록), LDPC는 부수 — 떼어낼 신규 LDPC 기법 없음
- **ID**: ieee:6112028
- **Type**: conference
- **Published**: 5-8 Oct. 2
- **Authors**: Nikola Djuric, Vojin Senk, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/6112028
- **Abstract**: This paper considers maximum a posteriori (MAP) decoding of the maximum transition run (MTR) codes, over two-head digital magnetic recording system. Decoding is based on Bayesian algorithm and computes a posteriori log-likelihood ratios (LLR) from codewords of the MTR code. In this paper we present simulation results for performance of the joint soft detection-decoding of a concatenation of MTR code and low-density parity-check (LDPC) code over the two-track two-head extended class four partial response channel (E2PR4). In channels with low inter-track interference (ITI), the joint detector-decoder exhibits 1.7dB gain.

## Graph-based iterative reconstruction of sparse signals for compressed sensing

- **Status**: ✅
- **Reason**: LDPC 그래프 기반 디코딩을 압축센싱 복원에 적용한 신규 반복 알고리즘 — 그래프 디코더 알고리즘 기법 이식 가능(애매→살림)
- **ID**: ieee:6112021
- **Type**: conference
- **Published**: 5-8 Oct. 2
- **Authors**: Anantha Raman Krishnan, Swaminathan Sankararaman, Bane Vasic
- **PDF**: https://ieeexplore.ieee.org/document/6112021
- **Abstract**: In this paper, we consider the problem of reconstruction of sparse signals in compressed sensing. In particular, we introduce a novel iterative algorithm based on graph-based decoding of low-density parity-check codes which possesses desirable properties like good performance, low complexity and running time, and ease of implementation. In this work, we outline the reconstruction algorithm, and analyze its performance on some measurement matrices. Furthermore, we also provide some initial results on the theoretical performance limits of this algorithm.

## A novel conflict-free memory and processor architecture for DVB-T2 LDPC decoding

- **Status**: ✅
- **Reason**: D: DVB-T2 LDPC 디코더의 무충돌 메모리/프로세서 아키텍처, flooding schedule, 알고리즘 비의존 구조-NAND 디코더 HW에 이식 가능.
- **ID**: ieee:6078930
- **Type**: conference
- **Published**: 5-7 Oct. 2
- **Authors**: Alberto Jiménez-Pacheco, Onkar Dabeer
- **PDF**: https://ieeexplore.ieee.org/document/6078930
- **Abstract**: In this paper, we present a flexible architecture for an LDPC decoder that fully exploits the structure of the codes defined in the DVB-T2 standard (Digital Video Broadcasting — Second Generation Terrestrial). We propose a processor and memory architecture which uses the flooding schedule and has no memory access conflicts, which are encountered in serial schedule decoders proposed in the literature. Thus, unlike previous works, we do not require any extra logic or ad hoc designs to resolve memory conflicts. Despite the typically slower convergence of flooding schedule compared to serial schedule decoders, our architecture meets the throughput and BER requirements specified in the DVB-T2 standard. Our design allows a trade-off between memory size and performance by the selection of the number of bits per message without affecting the general memory arrangement. Besides, our architecture is not algorithm specific: any check-node message processing algorithm can be used (Sum-Product, Min-Sum, etc.) without modifying the basic architecture. Furthermore, by simply adding relevant small ROM tables, we get a decoder that is fully compatible with all three second generation DVB standards (DVB-T2, DVB-S2 and DVB-C2). We present simulation results to demonstrate the viability of our solution both functionally and in terms of the bit-error rate performance. We also discuss the memory requirements and the throughput of the architecture, and present preliminary synthesis results in CMOS 130nm technology.

## A reconfigurable software radio framework for accessing diverse resources in distributed nodes

- **Status**: ❌
- **Reason**: 소프트웨어 라디오 분산 컴퓨팅 프레임워크, LDPC/ECC 무관.
- **ID**: ieee:6078919
- **Type**: conference
- **Published**: 5-7 Oct. 2
- **Authors**: Haopeng Liu, Xin Su, Yuan You +1
- **PDF**: https://ieeexplore.ieee.org/document/6078919
- **Abstract**: Highly reconfigurable software radio is a key technology in B3G/4G wireless communication systems. Realistic experimentation in such systems has contributed significantly to the research of wireless communication. With increasing computational requirement, distributed cluster and dedicated hardware are demanded in real system. In addition, lots of existing computing resources in different platforms scatter around many research institutions. In this paper, we propose a novel reconfigurable software radio framework for accessing diverse computing resource in distributed nodes. Diverse computing resource is wrapped in a component, providing common interface. Dynamic reconfigurability is also supported in this framework by means of registered event for altering component parameter, which is described in XML file. Based on the proposed framework, we also present the radio application design flow, which facilitates implementation of a radio application, allowing researchers to make use of component in other platforms. The development of a realistic radio application is also presented to demonstrate the features and technique in this framework.

## A high parallel macro block level layered LDPC decoding architecture based on dedicated matrix reordering

- **Status**: ✅
- **Reason**: D: WiMAX QC-LDPC layered 고병렬 디코더 아키텍처, 행렬 재배열 전략으로 메모리/병렬도 개선-NAND 디코더 HW 이식 가능.
- **ID**: ieee:6088961
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: Qian Xie, Qian He, Xiao Peng +4
- **PDF**: https://ieeexplore.ieee.org/document/6088961
- **Abstract**: This paper presents a high parallel macro block level layered LDPC decoder architecture for the quasi-cyclic low-density parity-check (QC-LDPC) codes with various code rates and code lengths. LDPC codes defined in WiMAX standard with 6 code rates and 19 code lengths are chosen as the demonstration of this architecture. Based on the proposed dedicated matrix reordering strategy, this decoder costs 12-24 clock cycles per iteration for different code rates. Compared with the state-of-art work, this decoder reduces total memory bits to a great extent and achieves 2x-4.3x higher parallelism with 1.2x hardware cost. The synthesis result proves the low power potential of this architecture.

## Combining LDPC, turbo and Viterbi decoders: Benefits and costs

- **Status**: ✅
- **Reason**: 멀티모드 FEC ASIP 디코더 아키텍처에 LDPC 디코더 포함, HW 구현/병렬화 기법 이식 가능(D)
- **ID**: ieee:6088977
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: S. Kunze, E. Matuš, G. Fettweis +1
- **PDF**: https://ieeexplore.ieee.org/document/6088977
- **Abstract**: In this paper we present a detailed analysis into the benefits and costs of merging decoders for different channel code types such as convolutional, turbo and LDPC codes. An ASIP (application-specific instruction set processor)-based framework for multi-code forward error correction (FEC) architectures is applied to implement three dedicated decoders for convolutional, turbo and LDPC codes respectively as well as one decoder capable of decoding all three. Synthesis results and performance estimations for all architectures are presented and used to draw a clear and fair comparison between single-mode and multi-mode decoders.

## An encoding scheme and encoder architecture for rate-compatible QC-LDPC codes

- **Status**: ✅
- **Reason**: rate-compatible QC-LDPC용 신규 인코더 VLSI 아키텍처 및 펑처링/패리티검사행렬 구성 제시(D/E)
- **ID**: ieee:6088997
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: Ahmed Mahdi, Nikos Kanistras, Vassilis Paliouras
- **PDF**: https://ieeexplore.ieee.org/document/6088997
- **Abstract**: We consider the problem of rate-compatible (RC)-encoder and RC-puncturing of LDPC codes. The proposed encoder is based on a modification of MacKay encoding scheme. The introduced modification enables the application of MacKay scheme for quasi-cyclic (QC) LDPC codes combined with a proposed matrix puncturing scheme based on an also proposed parity-check matrix construction to achieve code-rate compatibility. The proposed encoding scheme and VLSI encoder architecture address the problem of encoding complexity, since about 80% of MacKay encoding algorithm complexity is linearly depended on LDPC check node degree. The proposed matrix puncturing scheme can produce good BER performance especially for high puncturing rates, where only a few parity check symbols are transmitted. A comparison with prior art in puncturing is offered, which shows superior performance of the proposed scheme, in terms of coding gain without any hardware cost.

## The power cost of over-designing codes

- **Status**: ✅
- **Reason**: E/D: girth 과설계의 디코딩 전력 비용 분석, 코드설계가 HW 전력에 미치는 영향-error floor/girth 설계 트레이드오프 이식 가능.
- **ID**: ieee:6088962
- **Type**: conference
- **Published**: 4-7 Oct. 2
- **Authors**: Karthik Ganesan, Pulkit Grover, Jan Rabaey
- **PDF**: https://ieeexplore.ieee.org/document/6088962
- **Abstract**: In “modern” coding theory, the goal of code-design often boils down to maximizing the code girth because from a traditional transmit-power perspective, larger girths ensure better performance. In this paper, we provide an experimental example showing that maximizing code girth can hurt: codes with larger girth can consume significantly larger decoding power. This is because larger girths require increased length of decoder interconnects. Concretely, we show that for (3,4)-regular LDPC codes of girth 6 and 8 decoded using Gallager-A decoding algorithm, the decoders for girth 8 codes can consume up to 36% more power than those for girth 6 codes at high decoding throughputs. Existing results in theoretical literature suggest that this effect will be greatly exaggerated at larger girths and degrees.

## Multi-source cooperative communications using low-density parity-check product codes

- **Status**: ❌
- **Reason**: 멀티소스 릴레이용 LDPC product code(M-SC-MPC 연접)로 네트워크 코딩 특이적, 표준 sum-product 사용, NAND 이식 가능한 신규 기법 없음
- **ID**: ieee:6081463
- **Type**: conference
- **Published**: 3-7 Oct. 2
- **Authors**: Yizhi Yin, Ramesh Pyndiah, Karine Amis
- **PDF**: https://ieeexplore.ieee.org/document/6081463
- **Abstract**: In this paper, we investigate the performance of low-density parity-check (LDPC) product codes in a multisource relay network where multiple sources transmit data to a same destination with the help of a noisy relay. We consider an LDPC product code resulting from the concatenation of Multiple Serially Concatenated Multiple Parity-Check (M-SC-MPC) codes. Every source encodes its data using the same M-SC-MPC code and broadcasts the codeword to relay and destination. The relay decodes and stores all codewords from sources in the rows of a matrix and encodes the columns using another M-SC-MPC code. Only the redundancy part generated by the relay is forwarded to the destination. At the destination, the codewords from the sources and the redundancy part from the relay form an observation of a product codeword whose parity check matrix is sparse. This LDPC product code can be iteratively decoded at destination using the low complexity sum-product algorithm. Since there are errors at the input of the relay-destination channel, an appropriate log-likelihood ratio is used in the LDPC decoding at destination in order to reduce the error propagation effect. The system error performance is given on the additive white Gaussian noise (AWGN) channel and the Rayleigh flat fading channel.

## Investigation of simple threshold shifting for bit-flip decoding

- **Status**: ✅
- **Reason**: 적응형 임계값 bit-flipping의 dual scaling(shift+add 구현, syndrome sum 기반 전환)으로 반복횟수 감소 - 부호 비의존적 디코더 기법, NAND LDPC에 이식 가능(C)
- **ID**: ieee:6081517
- **Type**: conference
- **Published**: 3-7 Oct. 2
- **Authors**: Julian Webber, Toshihiko Nishimura, Takeo Ohgane +1
- **PDF**: https://ieeexplore.ieee.org/document/6081517
- **Abstract**: Remarkably low error rates can be obtained using low-density parity-check (LDPC) codes and their use is now an increasingly common option in communications standards. The classic decoders based on belief propagation offer very high performance but have high implementation complexity. Therefore over the last decade simpler architectures such as the bit flipping class of algorithms have been researched. Recently, a number of adaptive threshold algorithms have been proposed in which at each iteration a bit is either flipped if it is below an inversion threshold, or the threshold is lowered. By choosing certain values of the scaling factor, the scaling can be efficiently implemented using a small number of shift and add operations. This work looks at how the scaling factor affects the convergence and error performance, and investigates an algorithm that switches between two scaling values based on the syndrome sum. The dual scaling method maintained the error performance compared to that with a single scaling but the iteration count was significantly reduced.

## A comparative study on MIMO MLSE turbo equalizer on frequency selective channels

- **Status**: ❌
- **Reason**: MIMO MLSE 터보 등화기에 LDPC가 부수 사용, LDPC는 베이스라인이고 떼어낼 디코더/구성 기법 없음 (무선 등화 응용 특이적)
- **ID**: ieee:6081455
- **Type**: conference
- **Published**: 3-7 Oct. 2
- **Authors**: Yuya Takahashi, Yasunori Iwanami, Eiji Okamoto
- **PDF**: https://ieeexplore.ieee.org/document/6081455
- **Abstract**: In this paper, we propose an LDPC (Low Density Parity Check) coded MLSE turbo equalizer for the spatially multiplexed transmission on MIMO (Multiple Input Multiple Output) frequency selective channels. When the Channel State Information (CSI) is available at the receiver, Maximum Likelihood Sequence Estimation (MLSE) using Viterbi algorithm is effective to compensate the Inter Symbol Interference (ISI) and Inter Antenna Interference (IAI) on MIMO frequency selective channels [1]. We consider here the LDPC coded case where the reliable decoder output from LDPC decoder is fed back to the MLSE equalizer to enhance the ability of MLSE for compensating the ISI and IAI. The output from the MLSE equalizer is then LDPC decoded and its output is again fed back to the MLSE decoder. This feedback is repeated several times. We compared the proposing LDPC coded MIMO MLSE turbo equalizer with the conventional LDPC coded MIMO SC/MMSE (Soft Canceller with MMSE filter) turbo equalizer [2], [3] and compared their BER characteristics.

## Deletion/Insertion/Reversal Error Correcting Codes for Bit-Patterned Media Recording

- **Status**: ❌
- **Reason**: 비트패턴매체 기록의 deletion/insertion/reversal 정정부호로 동기화 오류 대상, LDPC 무관한 비-LDPC 부호 (원칙 제외)
- **ID**: ieee:6104454
- **Type**: conference
- **Published**: 3-5 Oct. 2
- **Authors**: Masato Inoue, Haruhiko Kaneko
- **PDF**: https://ieeexplore.ieee.org/document/6104454
- **Abstract**: Missynchronization in bit-patterned media recording (BPMR) causes deletion/insertion errors. This paper describes a model for BPMR and examines the applicability of deletion/insertion/reversal error-correcting codes based on the model. The decoded word error rates for single and double deletion/insertion/reversal error-correcting codes are compared.

## Circulant search algorithm for the construction of QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC circulant 탐색 알고리즘으로 큰 girth 구성(E, 바이너리) — 새 구성 기법
- **ID**: ieee:6155922
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Xiongfei Tao, Xiaofeng Zhou, Deyu Feng +1
- **PDF**: https://ieeexplore.ieee.org/document/6155922
- **Abstract**: A circulant permutation search algorithm is present in this paper, which can be employed to search appopriate circulant permutation to construct QC-LDPC codes with desired girth. The algorithm is based on a tree expansion mechanism and a select-and-discard procedure. By proposed method, a practical (3, 4) code with code length n=37368 and girth g=18 is constructed. The experiment shows that the codes construct in this paper have large girth and minimum distance, and the bit error rate performance over AWGN channels is excellent.

## An improved LDPC coding scheme with motion decision for distributed video codec

- **Status**: ✅
- **Reason**: PEG 기반 Weight-Increasing parity-check 행렬 구성+가변노드 매핑(E/C), DVC 응용이나 코드설계 기법 이식 가능 — 애매하여 살림
- **ID**: ieee:6155993
- **Type**: conference
- **Published**: 28-30 Oct.
- **Authors**: Bin Li, Yumei Wang, Yu Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6155993
- **Abstract**: In conventional distributed video coding (DVC), we exploit a random irregular check matrix to realize LDPC coding. However, for DVC this method does not fully exploit the character that the bits corresponding to this random matrix with different significance can be protected in different degrees. Therefore, in this paper we propose an improved LDPC coding scheme with motion decision to improve the LDPC decoding performance. Considering the movement of the objects in the video sequence, all of blocks in the frame are classified as different motion areas which need the protection with varying degrees. Meanwhile, we exploit the progressive edge-growth (PEG) algorithm to generate a Weight-Increasing Parity-Check (WIPC) matrix for LDPC coding. Finally, the corresponding bits of the pixels located in the motion areas could be mapped to the variable nodes with different degrees in the generated matrix to proceed decoding. The experimental results show that compared with the conventional LDPC coding scheme in DISCOVER, the PSNR gain for our proposed coding scheme can reach up to 0.6db.

## High efficiency and low power multi-rate LDPC decoder design for CMMB

- **Status**: ✅
- **Reason**: layered min-sum+메모리 압축+충돌해소 백업메모리 등 디코더 HW 기법 이식 가능(C/D)
- **ID**: ieee:6157295
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Jiang xiaobo, li hongyuan
- **PDF**: https://ieeexplore.ieee.org/document/6157295
- **Abstract**: High efficiency and low power LDPC decoder for CMMB that supports two rates has been designed in the paper. Layered min-sum algorithm and memory compression technology are adopted to reduce the usage of memory; backup memory method is applied to solve memory read/write conflict existing in CMMB LDPC code at a low cost of memory resource; operational unit multiplexing which can process 1/2 bit rate and 3/4 bit rate simultaneously is used so that the resource consumption of operational unit is reduced. The LDPC decoder designed in this paper is synthesized in the SMC0.18um process. The synthesized result has indicated that the area of designed CMMB LDPC decoder is 7.6mm2 and its power consumption is 132.8mW.

## High-parallel LDPC decoder with power gating design

- **Status**: ✅
- **Reason**: high-parallel LDPC 디코더의 power gating(전력 도메인 분할) HW 아키텍처 기법(D)
- **ID**: ieee:6157112
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Ying Cui, Xiao Peng, Yu Jin +3
- **PDF**: https://ieeexplore.ieee.org/document/6157112
- **Abstract**: Leakage power is growing comparable to dynamic power dissipation as a result of technology trends, and thus it has become an important issue in low-power circuit design. As a popular technique for standby power reduction, power gating is applied to high-parallel LDPC decoder for WiMAX standard. The clustered-block processing engine (CBPE) array are divided into 9 power domains, and they are switched on or off according to different code lengths of LDPC code defined in WiMAX standard. As CBPE array occupies about 70% of the decoder system, the dedicated power gating strategy is very effective in shorter code length case since more power domains can be switched off. At shortest code length, power gating design brings about 55% power reduction compared to that of longest code length.

## AProgrammable IP Core for LDPC Decoder Based onASIP

- **Status**: ✅
- **Reason**: ASIP 기반 프로그래머블 LDPC 디코더 6단 파이프라인 HW 아키텍처(D)
- **ID**: ieee:6157317
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Jun Deng, Bing Li, Lintao Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/6157317
- **Abstract**: This paper proposes a programmable soft IP core of a LDPC decoder based on ASIP (application-specific instruction set processor) which can support multi-mode specified in the IEEE802.11n standard. With the presented specific microinstructions based on ASIP architecture, the decoder can process all the codes for the IEEE802.11n standard in a programmable approach, effectively, and due to the proposed 6-stage pipeline, the decoder performance is improved greatly. To verify the design, the IP has been integrated into a embedded processor system based on Xilinx EDK on a Xilinx Virtex5 FPGA component. Finally, the Logic synthesis on 0.18μm CMOS technology from UMC reveals a maximum clock frequency of 203MHz and a total area of 3.94mm2, and the corresponding power consumption is below 326.49mW.

## Area efficient LDPC decoder design for parallel layered decoding

- **Status**: ✅
- **Reason**: parallel layered decoding의 shift register chain 면적효율 HW 아키텍처(D)
- **ID**: ieee:6157296
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Yuan Yao, Fan Ye, Junyan Ren
- **PDF**: https://ieeexplore.ieee.org/document/6157296
- **Abstract**: An area efficient LDPC decoder hardware design for parallel layered decoding algorithm is proposed. Shift register chain is used to reduce the chip area. Puncturing technique is employed to produce arbitrary rate between 1/2 and 1. This design is implemented based on rate-1/2 LDPC in 802.16e with 65nm CMOS. The decoder achieves a throughput of 1.2 Gb/s at 10 iterations with an area of 1.14mm2 and support any rate between 1/2 and 1.

## A study on channel polarization and polar coding

- **Status**: ❌
- **Reason**: polar code 개요/SC 디코딩 — 비-LDPC 부호이고 이식 가능한 BP 기법 없는 소개성 논문
- **ID**: ieee:6157327
- **Type**: conference
- **Published**: 25-28 Oct.
- **Authors**: Yichao Lu, Satoshi Goto
- **PDF**: https://ieeexplore.ieee.org/document/6157327
- **Abstract**: In 2006, Arikan introduced the method of channel polarization on which one can construct efficient capacity-achieving codes, called polar codes, for any binary discrete memoryless channel (B-DMC). In this letter, we will give a description of the main ideas and mechanisms of this kind of codes. The codes construction, decoding algorithm as well as the probability of block error under successive cancellation (SC) decoding are also discussed.

## A LDPC-based IR scheme for cooperative relay system

- **Status**: ❌
- **Reason**: 협력 릴레이 IR(증분잉여) LDPC 코드 최적화—무선 응용 특이적, Gaussian Approximation 표준기법, NAND에 떼어낼 신규 디코더/HW/구성 없음
- **ID**: ieee:6089780
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Qin Zhang, Dengsheng Lin, Gang Wu
- **PDF**: https://ieeexplore.ieee.org/document/6089780
- **Abstract**: A cooperative IR (Incremental Redundancy) scheme in a three-node relay system is studied in this paper. The soft encoding at the relay is adopted to avoid the error propagation and improve the transmission efficiency. Alamouti coding is considered at the source and the relay to get cooperative transmitting diversity. We also derive the optimal IR LDPC codes by linear optimization of the whole code under Gaussian Approximation. At last, we simulate the proposed scheme under Rayleigh channel, the results show that the proposed scheme significantly outperforms the traditional IR strategy without the relay.

## A Modified Construction Method of Low-Density Parity-Check Codes Based on PEGPC

- **Status**: ✅
- **Reason**: PEG 기반 사이클 다항식·ACE로 short cycle 제거·girth 개선한 신규 QC-LDPC 구성법(HW 친화)으로 카테고리 E 이식 가능
- **ID**: ieee:6086319
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Jiwei Chen, Zemao Zhao, Jianrong Bao
- **PDF**: https://ieeexplore.ieee.org/document/6086319
- **Abstract**: A modified construction method of LDPC (Low-density Parity-check) codes based on polynomial of cycles of PEG (Progressive-Edge-Growth) is proposed according to reaction on the performance of LDPC codes by polynomial of cycles based on PEG and connectivity of cycles. It can reduce the number of the shortest cycles, increase average local girth and improve connectivity of cycles while deleting short cycles by considering girth of check matrix, number of the shortest cycles and ACE (Approximate Cycle EMD), so that it can improve performance of decoding. At the same time, a construction method of QC-LDPC (quasi-cyclic-LDPC) codes based on ACE and polynomial of cycles of PEG is also proposed to deal with the complexity of implementation on hardware of unstructured codes. Simulation results show that the performance of this code is better than unstructured Mackay code and it is easier for implementation on hardware.

## Reduced-routing complexity decoder for high-rate QC-LDPC codes

- **Status**: ✅
- **Reason**: QC-LDPC 디코더 라우팅 복잡도 감소+고정 배선 메시지경로 신규 HW 아키텍처(D)—FPGA 구현, 바이너리 QC-LDPC, NAND 디코더 HW에 이식 가능
- **ID**: ieee:6089946
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Yong Niu, Zhenyu Xiao, Depeng Jin +2
- **PDF**: https://ieeexplore.ieee.org/document/6089946
- **Abstract**: This paper presents a high-throughput and routing complexity reduced decoder for Quasi-Cyclic Low-Density Parity-Check (QC-LDPC) codes in the high rate wireless personal area network applications (WPAN). Our selected code is the rate-1/2 QC-LDPC code in IEEE P802.11ad/D1.0. A new decoder architecture is proposed. The message paths between variable nodes and check nodes are constructed by a fixed wire network. Compared to the fully parallel architecture, routing complexity of the new architecture is reduced greatly. The decoder is implemented using FPGA, and a data rate of 1.21 Gbps can be achieved in the air.

## Comparison of decoding algorithms for LDPC codes of IEEE 802.16e standard

- **Status**: ❌
- **Reason**: 802.16e 표준 LDPC에 표준 SP/MS/MS+보정 디코더 단순 비교, 신규 기여 없음
- **ID**: ieee:6095450
- **Type**: conference
- **Published**: 20-21 Oct.
- **Authors**: Muhammad Daud, Andriyan B. Suksmono, Hendrawan +1
- **PDF**: https://ieeexplore.ieee.org/document/6095450
- **Abstract**: One of forward error correction codes that were defined in the IEEE 802.16e standard was the LDPC code. This paper presents the simulation of the LDPC codes using three decoding algorithms, i.e. sum-product algorithm, min-sum algorithm, and min-sum-plus-correction-factor algorithm. Simulation results show the decoding with sum-product algorithm and min-sum-plus-correction-factor algorithm provide BER performances better than the min-sum algorithm.

## LDPC decoding for CMMB utilizing OpenMP and CUDA parallelization

- **Status**: ✅
- **Reason**: regular H-matrix 활용 OpenMP+CUDA 병렬 LDPC 디코딩, 병렬 구현 기법 이식 가능성(D, 애매하면 in)
- **ID**: ieee:6152939
- **Type**: conference
- **Published**: 2-5 Oct. 2
- **Authors**: Joo-Yul Park, Ki-Seok Chung
- **PDF**: https://ieeexplore.ieee.org/document/6152939
- **Abstract**: As the 4G mobile communication systems require high transmission rate with reliability, the demand for efficient error correcting code increases. In this paper, a novel LDPC (Low Density Parity Check) decoding method is introduced. We address a parallel software implementation of LDPC decoding for CMMB (China Multimedia Mobile Broadcasting) standard. LDPC codes for CMMB employ a regular H-matrix which has the fixed row and column weights. While effectively utilizing the regularity of the H-matrix, we process information on H-matrices for multiple code rates using OpenMP pragmas on a multi-core processor and execute the decoding algorithm in parallel using CUDA (Compute Unified Device Architecture) on a GPU (Graphics Processing Unit). We evaluated the performance of the proposed implementation with respect to two different code rates, and verified that the proposed implementation satisfies the bandwidth requirement for CMMB.

## Future Design of Channel Codes: A Complex Network Perspective

- **Status**: ❌
- **Reason**: complex network 관점 채널코딩 future-directions 리뷰, 구체적 신규 디코더·구성·HW 기여 없음
- **ID**: ieee:6093513
- **Type**: conference
- **Published**: 19-22 Oct.
- **Authors**: Francis C. M. Lau, Chi K. Tse, Zhiliang Zhu
- **PDF**: https://ieeexplore.ieee.org/document/6093513
- **Abstract**: Channel coding has been studied for over 60 years while complex network has not been intensively investigated until recently. In this review paper, we aim to establish a linkage between channel coding and complex networks - two seemingly unrelated topics. We show by two examples how the characteristics of complex networks can inspire new ways of designing channel codes. Finally, we give some future directions in this promising research area.

## Opportunistic Network Erasure Coding in Disruptive Sensor Networks

- **Status**: ❌
- **Reason**: 센서망 fountain/erasure 코딩(degree distribution) — LDPC ECC 채널코딩 아님, 분산 데이터수집 프로토콜
- **ID**: ieee:6076670
- **Type**: conference
- **Published**: 17-22 Oct.
- **Authors**: Mingsen Xu, Wen-Zhan Song, Yichuan Zhao
- **PDF**: https://ieeexplore.ieee.org/document/6076670
- **Abstract**: Sensor network has found critical applications in extreme environments. However, in the extreme environments, a predictable and stable path may never exist, since the transient network connectivity, asymmetric links and unstable nodes are prevalent. Thus, the extreme environments severely challenge its basic function of data collection. Particularly, those disruptive conditions make traditional data collection protocols inefficient. In this paper, we design Opportunistic Network Erasure Coding (ONEC) protocol for collaborative data collection in disruptive sensor networks. The idea behind ONEC protocol is to study how each node determines code degree distribution and receding strategies in a distributed fashion, so that all data of network can be recovered with high probability upon receiving any sufficient amount of encoded packets. First, each node derives code degree distribution through recursive discrete deconvolution. Second, every node conducts selective receding of its own sensing data and opportunistically received data. Last, the ONEC ensures decoder can recover all data from any sufficient amount of encoded packets with high probability. The performance evaluations through extensive simulation validate that ONEC can truly achieve efficient data collection with high reliability in disruptive sensor networks and outperform other existing approaches in terms of network goodput, message complexity and buffer space.

## Augmented LDPC graph for distributed video coding with multiple side information

- **Status**: ❌
- **Reason**: 분산 비디오 소스코딩(Slepian-Wolf, multiple SI) — 소스코딩 신드롬 디코딩, 채널 ECC 아님
- **ID**: ieee:6093788
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: João Ascenso, Catarina Brites, Fernando Pereira
- **PDF**: https://ieeexplore.ieee.org/document/6093788
- **Abstract**: The advances made in channel-capacity codes, such as turbo codes and low-density parity-check (LDPC) codes, have played a major role in the emerging distributed source coding paradigm. LDPC codes can be easily adapted to new source coding strategies due to their natural representation as bipartite graphs and the use of quasi-optimal decoding algorithms, such as belief propagation. This paper tackles a relevant scenario in distributed video coding: lossy source coding when multiple side information (SI) hypotheses are available at the decoder, each one correlated with the source according to different correlation noise channels. Thus, it is proposed to exploit multiple SI hypotheses through an efficient joint decoding technique with multiple LDPC syndrome decoders that exchange information to obtain coding efficiency improvements. At the decoder side, the multiple SI hypotheses are created with motion compensated frame interpolation and fused together in a novel iterative LDPC based Slepian-Wolf decoding algorithm. With the creation of multiple SI hypotheses and the proposed decoding algorithm, bitrate savings up to 8.0% are obtained for similar decoded quality.

## Depth camera assisted multiterminal video coding

- **Status**: ❌
- **Reason**: 멀티터미널 비디오 코딩(Wyner-Ziv 소스코딩), LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:6093808
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Yifu Zhang, Yang Yang, Zixiang Xiong
- **PDF**: https://ieeexplore.ieee.org/document/6093808
- **Abstract**: This paper addresses multiterminal video coding with the help of a low-resolution depth camera. In this setup, the depth sequence, together with the high-resolution texture sequences, are collected, compressed and transmitted separately to the joint decoder in order to obtain more accurate depth information and consequently better rate-distortion performance. At the decoder end, side information (for Wyner-Ziv coding) is generated based on successive refinement of the decompressed low-resolution depth map and texture frame warped from other terminals. Experimental results show sum-rate savings with the depth camera than without for the same PSNR performance. Comparisons to simulcast and JMVM coding are also provided. Although the sum-rate gain of our multiterminal video coding scheme (with or without the depth camera) over simulcast is relatively small, this work is the first that incorporates depth camera in a multiterminal setting.

## Design of RC-LDPC codes and its application in codes SC-FDE systems

- **Status**: ✅
- **Reason**: RC-LDPC 신규 코드행렬 구조 설계(PEG 기반 수정)→코드설계(E) 바이너리, SC-FDE는 응용일 뿐
- **ID**: ieee:6103913
- **Type**: conference
- **Published**: 17-18 Oct.
- **Authors**: Jianwu Zhang, Huan Yan, Jianrong Bao
- **PDF**: https://ieeexplore.ieee.org/document/6103913
- **Abstract**: This paper proposes a new scheme of the rate compatible low-density parity-check (RC-LDPC) coded single carrier-frequency domain equalization (SC-FDE) system where RC-LDPC codes are combined with SC-FDE modulations. To construct a class of different RC-LDPC codes, we take advantage of a base matrix constructed by the progressive edge growth (PEG) algorithm. A special code matrix structure is used and modified to meet requirements of the different code rate. In addition, a pseudorandom sequence instead of traditional cyclic prefix (CP) is proposed to estimate the channel noise variance for LDPC decoding. The simulation results show that the modified RC-LDPC codes have better performance than that of current method and the RC-LDPC coded SC-FDE system obtains better performance compared with uncoded SC-FDE system.

## Optimal rate for irregular LDPC codes in binary erasure channel

- **Status**: ❌
- **Reason**: BEC용 irregular LDPC 최적 rate degree distribution 설계 — 순수 이론/소거채널 최적화, NAND 채널 ECC로 이어지는 디코더·HW 기법 없음
- **ID**: ieee:6089360
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: H. Tavakoli, M. Ahmadian Attari, M. Reza Peyghami
- **PDF**: https://ieeexplore.ieee.org/document/6089360
- **Abstract**: In this paper, we introduce a new practical and general method for solving the main problem of designing the capacity approaching, optimal rate, irregular low-density parity-check (LDPC) code ensemble over binary erasure channel (BEC). Compared to some new researches, which are based on application of asymptotic analysis tools out of optimization process, the proposed method is much simpler, faster, accurate and practical. Because of not using any relaxation or any approximate solution like previous works, the found answer with this method is optimal. We can construct optimal variable node degree distribution for any given binary erasure rate, e, and any check node degree distribution. The presented method is implemented and it works well in practice. The time complexity of this method is of polynomial order. As a result, we obtain some degree distribution which their rates are close to the capacity.

## Multi-edge type unequal error protecting low-density parity-check codes

- **Status**: ❌
- **Reason**: 통신 UEP 특화 LDPC 연결프로파일 최적화, NAND 이식할 새 디코더/구성 없음
- **ID**: ieee:6089474
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: H. V. Beltrão Neto, W. Henkel, V. C. da Rocha
- **PDF**: https://ieeexplore.ieee.org/document/6089474
- **Abstract**: Irregular low-density parity-check (LDPC) codes are particularly well-suited for transmission schemes that require unequal error protection (UEP) of the transmitted data due to the different connection degrees of its variable nodes. However, this UEP capability is strongly dependent on the connection profile among the protection classes. This paper applies a multi-edge type analysis of LDPC codes for optimizing such a connection profile according to the performance requirements of each protection class. This allows the construction of UEP-LDPC codes where the difference between the performance of the protection classes can be adjusted and with an UEP capability that does not vanish as the number of decoding iterations grows.

## Operating LDPC codes with zero shaping gap

- **Status**: ❌
- **Reason**: shaping gap용 matching/dematching, off-the-shelf LDPC 그대로 사용, 새 코드/디코더 기여 없음
- **ID**: ieee:6089473
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Georg Böcherer, Rudolf Mathar
- **PDF**: https://ieeexplore.ieee.org/document/6089473
- **Abstract**: Unequal transition probabilities between input and output symbols, input power constraints, or input symbols of unequal durations can lead to non-uniform capacity achieving input distributions for communication channels. Using uniform input distributions reduces the achievable rate, which is called the shaping gap. Gallager's idea for reliable communication with zero shaping gap is to do encoding, matching, and jointly decoding and dematching. In this work, a scheme is proposed that consists in matching, encoding, decoding, and dematching. Only matching is channel specific whereas coding is not. Thus off-the-shelf LDPC codes can be applied. Analytical formulas for shaping and coding gap of the proposed scheme are derived and it is shown that the shaping gap can be made zero. Numerical results show that the proposed scheme allows to operate off-the-shelf LDPC codes with zero shaping gap and a coding gap that is unchanged compared to uniform transmission.

## Coupled LDPC codes: Complexity aspects of threshold saturation

- **Status**: ✅
- **Reason**: coupled(SC) LDPC threshold saturation의 디코딩 복잡도와 효율적 메시지패싱 스케줄 제안 — 이식 가능 디코더 스케줄/코드설계(C/E)
- **ID**: ieee:6089581
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Michael Lentmaier, Gerhard P. Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/6089581
- **Abstract**: We analyze the convergence behavior of iteratively decoded coupled LDPC codes from a complexity point of view. It can be observed that the thresholds of coupled regular LDPC codes approach capacity as the node degrees and the number L of coupled blocks tend to infinity. The absence of degree two variable nodes in these capacity achieving ensembles implies for any fixed L a doubly exponential decrease of the error probability with the number of decoding iterations I, which guarantees a vanishing block error probability as the overall length n of the coupled codes tends to infinity at a complexity of O(n log n). On the other hand, an initial number of iterations Ibr is required until this doubly exponential decrease can be guaranteed, which for the standard flooding schedule increases linearly with L. This dependence of the decoding complexity on L can be avoided by means of efficient message passing schedules that account for the special structure of the coupled ensembles.

## Ensemble analysis of pseudocodewords of protograph-based non-binary LDPC codes

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC pseudocodeword 분석, 비이진 제외
- **ID**: ieee:6089475
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Dariush Divsalar, Lara Dolecek
- **PDF**: https://ieeexplore.ieee.org/document/6089475
- **Abstract**: This paper presents a method for evaluating pseudocodeword weight enumerators of nonbinary LDPC codes built out of protographs. The ensemble enumerators are evaluated for both the finite-length and infinite-length regimes. Results of this type can be particularly useful for designing structured non-binary LDPC codes with good properties under message passing or linear programming decoding.

## On the selection of finite alphabet iterative decoders for LDPC codes on the BSC

- **Status**: ✅
- **Reason**: FAID 유한알파벳 반복디코더 선택 알고리즘, error floor 개선 column-weight-3 코드용 디코더 기법(C)
- **ID**: ieee:6089476
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Ludovic Danjean, David Declercq, Shiva K. Planjery +1
- **PDF**: https://ieeexplore.ieee.org/document/6089476
- **Abstract**: Recently new message passing decoders for LDPC codes, called finite alphabet iterative decoders (FAIDs) were proposed. The messages belong to a finite alphabet and the update functions are simple boolean maps different from the functions used for the belied propagation (BP) decoder. The maps can be chosen using the knowledge of potential trapping sets such that the decoders surpass the BP decoder in the error floor. In this paper, we address the issue of selecting good FAIDs which perform well in the error floor for column weight three codes. We introduce the notion of noisy trapping set which is a generalization based on analyzing the local dynamic behaviour of a given FAID on a trapping set. Using this notion as the core, we provide an iterative greedy algorithm that outputs a set of candidate FAIDs containing potentially good decoders for any given code. To illustrate the appliance of the methodology on several codes, we show that the set of candidate FAIDs contains particularly good FAIDs for different codes with different rates and lengths.

## Gigabit rate low-power LDPC decoder

- **Status**: ✅
- **Reason**: 새 LDPC 디코딩 스케줄 PPL(Parallel Processing Layered)로 latency/전력 최적화, 수렴 2배 — 이식 가능 디코더/HW 기법(C/D)
- **ID**: ieee:6089516
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Eran Pisek, Dinesh Rajan, Joseph Cleveland
- **PDF**: https://ieeexplore.ieee.org/document/6089516
- **Abstract**: LDPC codes are becoming popular in next generation high throughput wireless standards since they can provide a level of parallelism with sufficient performance to support the high gigabit rate. In this paper, we propose a new method for LDPC decoding called Parallel Processing Layered (PPL). The new method aims to optimize the latency and power efficiency of LDPC decoding to enable significant increase of the processing rate, thereby saving battery power for mobile devices. We provide performance results in different channel models using the newly defined WiGig standards, and compare them to the conventional decoding methods. We show that the new proposed LDPC decoding architecture converges 2x faster than conventional (i.e. Flooding) methods.

## MAP decoding for LDPC codes over the binary erasure channel

- **Status**: ❌
- **Reason**: BEC MAP 디코딩(GTEP peeling decoder) — 소거채널 전용 peeling, NAND 연판정 BP로 이식 불가
- **ID**: ieee:6089364
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Luis Salamanca, Pablo M. Olmos, Juan José Murillo-Fuentes +1
- **PDF**: https://ieeexplore.ieee.org/document/6089364
- **Abstract**: In this paper, we propose a decoding algorithm for LDPC codes that achieves the MAP solution over the BEC. This algorithm, denoted as generalized tree-structured expectation propagation (GTEP), extends the idea of our previous work, the TEP decoder. The GTEP modifies the graph by eliminating a check node of any degree and merging this information with the remaining graph. The GTEP decoder upon completion either provides the unique MAP solution or a tree graph in which the number of parent nodes indicates the multiplicity of the MAP solution. This algorithm can be easily described for the BEC, and it can be cast as a generalized peeling decoder. The GTEP naturally optimizes the complexity of the decoder, by looking for checks nodes of minimum degree to be eliminated first.

## Quasi-cyclic LDPC codes based on pre-lifted protographs

- **Status**: ✅
- **Reason**: QC-LDPC pre-lifted protograph 2단계 lifting으로 최소거리 향상, 바이너리 코드설계 기법(E)
- **ID**: ieee:6089477
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: David G. M. Mitchell, Roxana Smarandache, Daniel J. Costello
- **PDF**: https://ieeexplore.ieee.org/document/6089477
- **Abstract**: Quasi-cyclic Low-Density Parity-Check (QC-LDPC) codes based on protographs are of great interest to code designers because of their implementation advantages and algebraic properties that make them easy to analyze. However, the protograph structure imposes undesirable fixed upper limits on important code parameters. In this paper, we show that the upper bound on the minimum Hamming distance of protograph-based QC codes can be improved by the careful application of a two-step lifting procedure applied to the protograph. The promised improvement is validated by constructing codes with minimum distance exceeding the upper bound for QC codes based on a particular protograph.

## Kite codes over groups

- **Status**: ❌
- **Reason**: Kite codes를 abelian group/lattice/M-PSK로 일반화 — 비이진 rateless 부호, 바이너리 NAND LDPC ECC에 떼어낼 기법 없음
- **ID**: ieee:6089507
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Xiao Ma, Shancheng Zhao, Kai Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/6089507
- **Abstract**: Kite codes, which were originally defined over the binary field, are generalized to arbitrary abelian groups in this paper. Kite codes are a special class of prefix rateless codes over groups, which can generate potentially infinite (or as many as required) random-like parity-check symbols. In this paper, we consider four kinds of Kite codes, which are binary Kite codes, Kite codes over one-dimensional lattices, Kite codes over M-PSK signal constellations and Kite codes over multi-dimensional lattices. It is shown by simulations that the proposed codes perform well over additive white Gaussian noise channels.

## Iterative soft decoding of binary linear codes using a generalized Tanner graph

- **Status**: ✅
- **Reason**: 바이너리 선형부호 일반화 Tanner graph 반복연판정 디코딩, 소사이클 완화+복잡도 감소 기법 BP 이식 가능(C)
- **ID**: ieee:6089431
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/6089431
- **Abstract**: In this work, we consider iterative soft-decision decoding of binary linear codes using a generalized Tanner graph. A generalized Tanner graph is constructed from the code's Tanner graph representation under the objective of mitigating the effect of small cycles. Then, iterative decoding is applied to the generalized Tanner graph using trellis-based soft-input soft-output decoding in the generalized check nodes. When combined with the stochastic shifting algorithm of Jiang and Narayanan (IEEE Commun. Letters, 2004), the proposed decoding method provides both improved error rate performance and reduced average decoding complexity, without increasing the worst-case decoding complexity.

## Rate-compatible LDPC convolutional codes for capacity-approaching hybrid ARQ

- **Status**: ❌
- **Reason**: BEC용 rate-compatible LDPC convolutional HARQ 부호, capacity-achieving 이론 구성 — NAND 채널 ECC 아닌 HARQ/erasure 응용, 떼어낼 신규 디코더/HW 없음
- **ID**: ieee:6089515
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Zhongwei Si, Mattias Andersson, Ragnar Thobaben +1
- **PDF**: https://ieeexplore.ieee.org/document/6089515
- **Abstract**: In this paper we construct a family of rate-compatible LDPC convolutional codes for Type-II HARQ systems. For each code family, the codes of lower rates are constructed by successively extending the graph of the high-rate base code. Theoretically, the proposed rate-compatible family includes all rates from 0 to 1. We prove analytically that all LDPC convolutional codes in the family are capacity achieving over the binary erasure channel (BEC). Thus, if applied to an idealized HARQ system over the BEC where the channel parameter stays constant within one complete information delivery, the throughput achieves the capacity of the channel. Moreover, the code construction is realized by regular degree distributions, which greatly simplifies the optimization.

## Extended bit-flipping algorithm for solving sparse linear systems of equations modulo p

- **Status**: ❌
- **Reason**: LDPC bit-flipping을 mod-p 희소 선형방정식 풀이로 변형 — ECC 디코딩이 아닌 선형대수 응용, NAND ECC에 이식할 부호 ECC 기법 아님
- **ID**: ieee:6089585
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Asie Abolpour, Mohammad-Reza Sadeghi, Daniel Panario
- **PDF**: https://ieeexplore.ieee.org/document/6089585
- **Abstract**: Let p be a prime number. We propose a new method for solving sparse linear systems of equations modulo p when the coefficient matrix has column degree at most 2. This algorithm is based on a well-known decoding algorithm for Low-Density Parity-Check (LDPC) codes called bit-flipping (BF) algorithm. We modify and extend this hard-decision decoding algorithm. The complexity of this algorithm is linear in terms of the number of columns n and the number of nonzero coefficients u of the matrix. We give a detailed small example, and report on computational results for larger systems.

## Quantized compute and forward: A low-complexity architecture for distributed antenna systems

- **Status**: ❌
- **Reason**: 비이진 LDPC compute-and-forward 분산안테나, 비이진 제외
- **ID**: ieee:6089493
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Song-Nam Hong, Giuseppe Caire
- **PDF**: https://ieeexplore.ieee.org/document/6089493
- **Abstract**: We consider a low-complexity version of the Compute and Forward scheme that involves only scaling, offset (dithering removal) and scalar quantization at the relays. The proposed scheme is suited for the uplink of a distributed antenna system where the antenna elements must be very simple and are connected to a joint processor via orthogonal perfect links of given rate R0. We consider the design of non-binary LDPC codes naturally matched to the proposed scheme. Each antenna element performs individual (decentralized) Belief Propagation decoding of its own quantized signal, and sends a linear combination of the users' information messages via the noiseless link to the joint processor, which retrieves the users' messages by Gaussian elimination. The complexity of this scheme is linear in the coding block length and polynomial in the system size (number of relays).

## Non-malleable codes from the wire-tap channel

- **Status**: ❌
- **Reason**: non-malleable codes(암호/wire-tap, coset-coding) — 보안 응용이며 LDPC ECC와 무관, 떼어낼 채널 ECC 기법 없음
- **ID**: ieee:6089565
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Hervé Chabanne, Gérard Cohen, Jean-Pierre Flori +1
- **PDF**: https://ieeexplore.ieee.org/document/6089565
- **Abstract**: Recently, Dziembowski et al. introduced the notion of non-malleable codes (NMC), inspired from the notion of non-malleability in cryptography and the work of Gennaro et al. in 2004 on tamper proof security. Informally, when using NMC, if an attacker modifies a codeword, decoding this modified codeword will return either the original message or a completely unrelated value. The definition of NMC is related to a family of modifications authorized to the attacker. In their paper, Dziembowski et al. propose a construction valid for the family of all bit-wise independent functions. In this article, we study the link between the second version of the Wire-Tap (WT) Channel, introduced by Ozarow and Wyner in 1984, and NMC. Using coset-coding, we describe a new construction for NMC w.r.t. a subset of the family of bit-wise independent functions. Our scheme is easier to build and more efficient than the one proposed by Dziembowski et al.

## Universal rateless codes from coupled LT codes

- **Status**: ❌
- **Reason**: low-density generator-matrix rateless 코드(fountain), 채널 ECC LDPC 기법 아님
- **ID**: ieee:6089436
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Vahid Aref, Rüdiger L. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/6089436
- **Abstract**: It was recently shown that spatial coupling of individual low-density parity-check codes improves the belief-propagation threshold of the coupled ensemble essentially to the maximum a posteriori threshold of the underlying ensemble. We study the performance of spatially coupled low-density generator-matrix ensembles when used for transmission over binary-input memoryless output-symmetric channels. We show by means of density evolution that the threshold saturation phenomenon also takes place in this setting. Our motivation for studying low-density generator-matrix codes is that they can easily be converted into rateless codes. Although there are already several classes of excellent rateless codes known to date, rateless codes constructed via spatial coupling might offer some additional advantages. In particular, by the very nature of the threshold phenomenon one expects that codes constructed on this principle can be made to be universal, i.e., a single construction can uniformly approach capacity over the class of binary-input memoryless output-symmetric channels. We discuss some necessary conditions on the degree distribution which universal rateless codes based on the threshold phenomenon have to fulfill. We then show by means of density evolution and some simulation results that indeed codes constructed in this way perform very well over a whole range of channel types and channel conditions.

## Quantum turbo codes with unbounded minimum distance and excellent error-reducing performance

- **Status**: ❌
- **Reason**: Quantum turbo codes — 양자 부호 + 비-LDPC(turbo), 제외 대상
- **ID**: ieee:6089430
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: Mamdouh Abbara, Jean-Pierre Tillich
- **PDF**: https://ieeexplore.ieee.org/document/6089430
- **Abstract**: We construct here a new family of quantum codes related to serial turbo-codes which are excellent error-reducing codes under iterative decoding for very large channel noise values. Moreover we also show that this family of codes has unbounded minimum distance.

## Multi-edge framework for unequal error protecting LT codes

- **Status**: ❌
- **Reason**: UEP LT(fountain/rateless) 부호 설계, 떼어낼 ECC 디코더 기법 없음
- **ID**: ieee:6089434
- **Type**: conference
- **Published**: 16-20 Oct.
- **Authors**: H. V. Beltrão Neto, W. Henkel, V. C. da Rocha
- **PDF**: https://ieeexplore.ieee.org/document/6089434
- **Abstract**: A multi-edge framework for unequal error protecting (UEP) LT codes is derived by distinguishing between the edges connected to each protection class. Under the framework introduced, two existing techniques for the design of unequal error protecting LT codes can be evaluated and explained in a unified way. Furthermore, a simple and flexible design technique is proposed for UEP LT codes with good performance.

## Performance analysis of multicast coded relay network with LDPC and Convolutional codes

- **Status**: ❌
- **Reason**: 멀티캐스트 릴레이 JNCC 무선 응용, LDPC vs convolutional 성능비교만, 떼어낼 ECC 기법 없음
- **ID**: ieee:6192840
- **Type**: conference
- **Published**: 14-16 Oct.
- **Authors**: Tariq Aziz, Muhammad Adnan, She Hao Qiu +2
- **PDF**: https://ieeexplore.ieee.org/document/6192840
- **Abstract**: In this paper, we have compared the performance of joint network channel coding (JNCC) for multicast relay network using low density parity check (LDPC) codes and Convolutional codes. Multicast relay transmission is a type of transmission scheme in which two fixed relay nodes contribute in the second hop of end-to-end transmission between BTS and a pair of mobile stations. Assuming no line of sight (LOS) between source and the destination we have considered one way and two way multicast scenarios and evaluated the bit error rate (BER) and throughput performance using LDPC and Convolutional block codes. In the proposed scheme we have implemented Exclusive-OR (XOR) based network coding at the intermediate relays in such a way that both diversity and multiplexing gain is achieved. It is worth notifying that BER and end-to-end throughput achieved for LDPC codes is better than Convolutional codes with JNCC implemented.

## Design EG-LDPC codes for soft error mitigation in memory

- **Status**: ✅
- **Reason**: EG-LDPC 메모리 ECC, majority decoding 2단계 가속 알고리즘+fault-secure 디코더 구조(C/D 이식 가능). 바이너리 LDPC 메모리 적용.
- **ID**: ieee:6159384
- **Type**: conference
- **Published**: 12-16 Oct.
- **Authors**: Xiao Li Yi, Zhu Ming, Zhang Yan Jing +1
- **PDF**: https://ieeexplore.ieee.org/document/6159384
- **Abstract**: As the feature sizes of integrated circuits decreasing, single event transient (SET) in combinational circuits can not been ignored any longer. In this paper, a novel fault-secure scheme for memory has been proposed by studying the structural features of Euclidean Geometry-Low Density Parity Check (EG-LDPC) codes. The proposed fault-secure scheme can tolerate transient faults both in the storage cell and in the encoder and decoder, using the parallel majority decoding and the feedback loop structure. In order to improve the decoding speed, an algorithm is presented, which can reduce the majority decoding of EG-LDPC codes into two steps. Furthermore, the proposed scheme can suit ordinary data width (e.g., 2n bits) in memory. Finally, the correcting capability and the reliability of the proposed scheme are analyzed. The experiment results reveal that the Mean Time to Failure (MTTF) of the proposed scheme is 419%, 104% and 118% compared with that of Hamming code, Matrix code and Reed-Muller code, respectively.

## A simple algorithm for a high code rate LDPC parity matrix design

- **Status**: ❌
- **Reason**: arithmetic sequence로 4-cycle 없는 QC/array 패리티행렬 설계, 표준 수준 구성으로 신규 기여 미약(E의 단순 재사용).
- **ID**: ieee:6092182
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Sekson Timakul, Somsak Choomchuay
- **PDF**: https://ieeexplore.ieee.org/document/6092182
- **Abstract**: This paper presents a simple method in designing a parity matrix of low density parity check codes. According to its use the use of arithmetic sequence is ideal for high rate code with no existing of cycle 4. The design is applicable to array code, modified array code, and quasi cyclic code. Upon the investigation, the designed code has delivered a similar BER-SNR performance when compared with that of more complicate designed matrices.

## An improved LDPC decoding algorithm based on min-sum algorithm

- **Status**: ✅
- **Reason**: min-sum 선형근사 개선 디코더 알고리즘(C). 바이너리 LDPC BP에 직접 이식 가능.
- **ID**: ieee:6089747
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Yue Cao
- **PDF**: https://ieeexplore.ieee.org/document/6089747
- **Abstract**: Low density parity check code is a kind of high-performance linear block code. It has excellent performance which is near the Shannon limit. LDPC has low decoding complexity, free structure and receives extensive attention. The typical decoding algorithm of LDPC is LLR BP algorithm, which is also called “sum-product algorithm”. LLR BP algorithm is the best algorithm at present. But it needs complex computation, which causes great difficulty in its hardware design. To solve this problem, an algorithm that gets approximation of LLR BP algorithm is put forward, which is called min-sum algorithm. Min-sum algorithm greatly reduces the computation and makes the hardware design simpler, but its accuracy has a wide gap with BP algorithm. This article analyzes the reason why min-sum algorithm has errors, and puts forward an improved algorithm called min-sum linear approximation algorithm based on min-sum algorithm.

## Scalability of two-way relay channel network coding in a relay enhanced LTE cell

- **Status**: ❌
- **Reason**: LTE 양방향 릴레이 네트워크코딩 확장성, LDPC ECC와 무관.
- **ID**: ieee:6089723
- **Type**: conference
- **Published**: 12-14 Oct.
- **Authors**: Hassan Hamdoun, Pavel Loskot, Timothy O'Farrell
- **PDF**: https://ieeexplore.ieee.org/document/6089723
- **Abstract**: Scalability of network coding (NC) for a two-way relay channel (TWRC) is investigated in a scenario where the multiple user equipments (UEs) are served by one relay station (RS) in a single Long Term Evolution (LTE) cell. In this context, the NC is employed independently over the multiple TWRCs formed by each UE, and more importantly, assuming that the radio resources are shared by all the UEs in the cell. The performance of this NC scheme is assessed in terms of the radio overhead energy reduction gain (ERG), the throughput gain and the number of resource blocks (RBs) saved due to NC. The operational energy consumptions of the base station (eNB) and of the RS are also considered in our analysis. It is found that the gains due to NC are scalable with the number of UEs and with the offered traffic load in the cell. Furthermore, since the operational energy dominates the overall energy consumption, the corresponding ERG of the NC is almost independent of the number of UEs.

## Efficient decoding over power-line channels

- **Status**: ❌
- **Reason**: 전력선 채널 Viterbi 기반 erasure 디코딩, 비-LDPC이고 LDPC BP 이식성 없음
- **ID**: ieee:6159408
- **Type**: conference
- **Published**: 10-14 Oct.
- **Authors**: Der-Feng Tseng, Yunghsiang S. Han, Wai Ho Mow +1
- **PDF**: https://ieeexplore.ieee.org/document/6159408
- **Abstract**: Power-line communications, conceived as an enabling technology for data networking alternative, is known to be susceptible to impulsive noises to attain assured transmission rate. To combat this obstacle, we design an efficient decoding scheme to incorporate erasures into the Viterbi algorithm. A unique feature of the decoding scheme is that it does not need the detailed knowledge of impulse statistics and only requires an estimate of impulse arrival probability. Surprisingly, our simulation results show that the proposed decoding scheme is on par with its optimal counterpart, where the exact impulse statistics is assumed to be known at receiver, in terms of bit error rate.

## Quasi-cyclic low-density parity-check convolutional code

- **Status**: ✅
- **Reason**: QC-LDPC convolutional code 신규 구성+수정 PEG+수정 min-sum 디코더+encoder/decoder HW 아키텍처 제시 (C/D/E)
- **ID**: ieee:6085376
- **Type**: conference
- **Published**: 10-12 Oct.
- **Authors**: Yixiang Wang, Hui Yu, Youyun Xu
- **PDF**: https://ieeexplore.ieee.org/document/6085376
- **Abstract**: This paper proposes a novel quasi-cyclic low-density parity-check convolutional code, and a two-stage construction algorithm with modified progressive edge growth (PEG) method is provided. We propose both encoder and decoder implementation architecture for this code. The quasi-cyclic form provides the parallelism for encoder and decoder, which can increase the throughput and decrease the delay significantly. The proposed modified min-sum decoding algorithm can speed up the process of convergence and reduce the hardware complexity. We also designed a GPU based simulation platform to speed up about 200 times against CPU to verify the code performance. Simulation results show the proposed code can get 0.5~1dB coding gain and lower error floor compared with the LDPC codes in WiMAX standard with the same code length, while the decoder only has 20 iterators.
