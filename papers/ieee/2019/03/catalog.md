# IEEE Xplore — 2019-03


## Performance Analysis of Practical QC-LDPC Codes: From DVB-S2 to ATSC 3.0

- **ID**: ieee:8554116
- **Type**: journal
- **Published**: March 2019
- **Authors**: Shuang Chen, Kewu Peng, Jian Song +1
- **PDF**: https://ieeexplore.ieee.org/document/8554116
- **Abstract**: In this paper, a new analysis method is introduced to predict the gap between Shannon limit and successful decoding signal-to-noise ratio threshold (SNR loss) of practical quasi-cyclic low-density parity check (QC-LDPC) codes. The SNR loss of a QC-LDPC code is summed up from three aspects: 1) the base matrix; 2) the number of iterations for decoding; and 3) the finite codeword length. As an example, the SNR loss of DVB-S2 and ATSC 3.0 LDPC codes is analyzed with the proposed method. Results show that a large portion of the SNR loss of DVB-S2 LDPC codes is due to their base matrices, which is significantly improved in latest ATSC 3.0 standard. Furthermore, with the aid of the proposed analysis method, newly designed QC-LDPC codes with raptor-like structure are proposed. Bit-error rate simulations show that the proposed codes are only 0.4 dB away from Shannon limit under binary-input additive white Gaussian noise channel and only 0.65 dB away from Shannon limit under binary-input Rayleigh fading channel, which are comparable with state-of-art design.

## Analysis of the Joint Viterbi Detector/Decoder (JVDD) Over a Coded AWGN/ISI System ss an LDPC Alternative

- **ID**: ieee:8434235
- **Type**: journal
- **Published**: March 2019
- **Authors**: Kheong Sann Chan, Susanto Rahardja
- **PDF**: https://ieeexplore.ieee.org/document/8434235
- **Abstract**: The joint Viterbi detector/decoder (JVDD) has been proposed as an alternative to the powerful and ubiquitous low-density parity check (LDPC) coding schemes, that are used in the majority of channel coding applications today. At shorter block lengths, the JVDD is able to outperform the state-of-the-art LDPC decoder that can be found in many of today's systems, from deep-space communications to the digital video broadcasting standard, to the advanced television standard committee 3.0. Researchers have developed the tools to analyze the performance of the LDPC decoder, which is known as the sum-product algorithm or message passing algorithm. These tools include density evolution (DE) and extrinsic information transfer (EXIT) charts. To date, no similar such analysis exists for the JVDD. In the current paper we perform a similar preliminary analysis on the JVDD algorithm akin to what DE and EXIT charts are for the LDPC decoder. The current new analysis of the JVDD allows prediction of its probability of error based on the probability distribution functions of the metrics used within the algorithm. Our analysis plays a similar role to the abovementioned tools developed for the LDPC decoder: it allows us to predict the performance of the JVDD under various conditions (such as varying SNR's, thresholds, and block lengths), it improves our understanding of the JVDD algorithm and the match against Monte-Carlo simulations verifies our assumptions on the main error-causing mechanisms within the JVDD.

## An Efficient Post-Processor for Lowering the Error Floor of LDPC Codes

- **ID**: ieee:8395069
- **Type**: journal
- **Published**: March 2019
- **Authors**: Hangxuan Cui, Jun Lin, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/8395069
- **Abstract**: Error floor is one major reason for limited use of low-density parity-check (LDPC) codes in applications requiring very low bit error rate. In this brief, an efficient erasure searching post-processor (ESPP) is proposed to lower the error floor of LDPC codes. Here, when a decoding failure is detected, the most unreliable symbols in the decoder output vector are erased, then their values are re-calculated by solving a system of linear equations with a sparse coefficient matrix. Compared to the state-of-the-art post processors, the ESPP has much lower computation complexity. Simulation results show that the proposed method significantly improves the decoding performance of LDPC codes in the error-floor region. Additionally, a well-optimized hardware architecture is developed for the proposed post-processor. Algorithmic transformation and architecture optimization are well explored to reduce the hardware complexity and latency. Synthesis results demonstrate the effectiveness of the proposed architecture.

## LDPC Codes Over the BEC: Bounds and Decoding Algorithms

- **ID**: ieee:8519768
- **Type**: journal
- **Published**: March 2019
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek +2
- **PDF**: https://ieeexplore.ieee.org/document/8519768
- **Abstract**: The performance of maximum-likelihood (ML) decoding on the binary erasure channel for finite-length low-density parity-check (LDPC) codes from two random ensembles is studied. A tightened union-type upper bound on the ML decoding error probability based on the precise coefficients of the average weight spectrum is presented. For LDPC codes from the Gallager ensemble and the Richardson-Urbanke ensemble, new upper bounds on the ML decoding performance based on computing the rank of submatrices of the code parity-check matrix are derived. A new lower bound on the ML decoding threshold followed from the latter error probability bound is obtained. An improved lower bound on the error probability for codes with a known estimate on the minimum distance is presented as well. A new low-complexity near-ML decoding algorithm for quasi-cyclic LDPC codes is proposed and simulated. Its performance is compared to the simulated belief propagation and ML decoding performance and simulated performance of the best known improved iterative decoding techniques, as well as, with the derived upper bounds on the ML decoding performance and with decoding thresholds obtained by the density evolution technique.

## LDPC Code Design for Fading Interference Channels

- **ID**: ieee:8606262
- **Type**: journal
- **Published**: March 2019
- **Authors**: Mahdi Shakiba-Herfeh, A. Korhan Tanc, Tolga M. Duman
- **PDF**: https://ieeexplore.ieee.org/document/8606262
- **Abstract**: We focus on the two-user Gaussian interference channel (IC) with fading and study implementation of different encoding/decoding schemes with low-density parity-check (LDPC) codes for both quasi-static and fast fading scenarios. We adopt Han-Kobayashi encoding, derive stability conditions on the degree distributions of LDPC code ensembles, and obtain explicit and practical code designs. In order to estimate the decoding thresholds, a modified form of the extrinsic information transfer chart analysis based on binary erasure channel approximation for the incoming messages from the component LDPC decoders to state nodes is developed. The proposed code design is employed in several examples for both fast and quasi-static fading cases. Comprehensive set of examples demonstrate that the designed codes perform close to the achievable information theoretic limits. Furthermore, multiple antenna transmissions employing the Alamouti scheme for fading ICs are studied, a special receiver structure is developed, and specific codes are explored. Finally, advantages of the designed codes over point-to-point optimal ones are demonstrated via both asymptotic and finite block length simulations.

## BP-LED Decoding Algorithm for LDPC Codes Over AWGN Channels

- **ID**: ieee:8445606
- **Type**: journal
- **Published**: March 2019
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Vitaly Skachek +1
- **PDF**: https://ieeexplore.ieee.org/document/8445606
- **Abstract**: A new method is presented for low-complexity near-maximum-likelihood (ML) decoding of low-density parity-check (LDPC) codes over the additive white Gaussian noise channel. The proposed method termed belief-propagation-list erasure decoding (BP-LED) is based on erasing carefully chosen unreliable bits performed in case of BP decoding failure. A strategy of introducing erasures into the received vector and a new erasure decoding algorithm are proposed. The new erasure decoding algorithm, called list erasure decoding, combines ML decoding over the BEC with list decoding applied if the ML decoder fails to find a unique solution. The asymptotic exponent of the average list size for random regular LDPC codes from the Gallager ensemble is analyzed. Furthermore, a few examples of irregular quasi-cyclic LDPC as well as randomly constructed regular LDPC codes of short and moderate lengths are studied by simulations and their performance is compared to the tightened upper bound on the LDPC ensemble-average performance and the upper bound on the average performance of random linear codes under ML decoding. A comparison of the BP decoding and BP-LED performance of the WiMAX standard codes and performance of the near-ML BEAST decoding are presented. The new algorithm is applied to decoding a short nonbinary (NB) LDPC code over extensions of the binary Galois field. The obtained simulation results are compared to the tightened upper bound on the ensemble-average performance of the binary image of regular NB LDPC codes.

## Adaptive Artificial Neural Network-Coupled LDPC ECC as Universal Solution for 3-D and 2-D, Charge-Trap and Floating-Gate NAND Flash Memories

- **ID**: ieee:8599122
- **Type**: journal
- **Published**: March 2019
- **Authors**: Toshiki Nakamura, Yoshiaki Deguchi, Ken Takeuchi
- **PDF**: https://ieeexplore.ieee.org/document/8599122
- **Abstract**: Adaptive artificial neural network (ANN)coupled low-density parity-check (LDPC) error-correcting code (ECC) (ANN-LDPC ECC) is proposed to increase acceptable errors for various NAND flash memories. The proposed ANN-LDPC ECC can be the universal solutions for 3-D and 2-D, charge-trap and floating-gate NAND flash memories. In 3-D NAND flash, lateral charge migration, vertical charge de-trap, inter floating-gate capacitive coupling noise, and inter word-line variations cause errors. On the other hand, in 2-D NAND flash, the charge de-trap and the harsh inter floating-gate capacitive coupling of adjacent word-lines and bit-lines cause errors. To solve these reliability problems, the proposed ANN automatically and adaptively compensates for complex memory cell errors. Moreover, the proposed ANNLDPC can reproduce the dynamic endurance and data-retention time dependence of errors. In addition, this paper evaluates the impacts of the chip-to-chip variations on the proposed ANN-LDPC. The proposed ANN-LDPC is implemented in the storage controller and can precisely and adaptively estimate bit-error rate (BER) and log-likelihood ratio (LLR). By using the precise LLR, LDPC decoder effectively corrects errors. As a result, ANN-LDPC extends the acceptable data-retention time by over 76× and 45× compared with conventional Bose-Chaudhuri-Hocquenghem (BCH) ECC in 3-D and 2-D triple-level cell (TLC) NAND flash memories, respectively.

## A (21150, 19050) GC-LDPC Decoder for NAND Flash Applications

- **ID**: ieee:8528505
- **Type**: journal
- **Published**: March 2019
- **Authors**: Yen-Chin Liao, Chien Lin, Hsie-Chia Chang +1
- **PDF**: https://ieeexplore.ieee.org/document/8528505
- **Abstract**: In this paper, a (21150, 19050) globally-coupled low-density parity check (GC-LDPC) code designed for NAND flash memories is presented. The proposed LDPC code comprises three disjoint subcodes which can be decoded independently. This highly structural parity check matrix contributes to efficient decoder implementation and flexible decoding flow control. Moreover, a two-phase local/global decoding procedure optimized for the proposed GC-LDPC code is introduced. Scenarios of collaborative decoding that leverages the special code structures are discussed. In the proposed decoder architecture, the pipelined processing elements with scheduling are employed to reduce the critical path and decoding latency as well. Implemented in UMC 65 nm process, the post-layout simulation shows a maximum decoding throughput of 4.32 Gb/s with the chip area 3.376 mm2.

## Performance Analysis of LDPC-BICM System Based on Gaussian Approximation

- **ID**: ieee:8566157
- **Type**: journal
- **Published**: March 2019
- **Authors**: Genning Zhang, Yin Xu, Dazhi He +2
- **PDF**: https://ieeexplore.ieee.org/document/8566157
- **Abstract**: In this paper, we propose a performance analysis algorithm of low density parity check-bit interleaved coded modulation (LDPC-BICM) system. First, we introduce the Gaussian mixture approximation method of the LLR messages output from the demodulator over the AWGN channel. Then, we analyze the density evolution based on these Gaussian mixture approximation LLR messages. During the analysis, the Gaussian approximation is applied to simplify the calculation. Some LDPC-BICM systems (which are adopted by ATSC3.0 standard) are used to evaluate the proposed algorithm. We also employ the actual performances and the thresholds obtained by the multi-edge type (MET) discretized density evolution algorithm as the references. The simulation results prove that our proposed algorithm can work well in most cases. Furthermore, the proposed algorithm is simpler than the MET algorithm because of the Gaussian or Gaussian mixture approximations.

## Multiset-Partition Distribution Matching

- **ID**: ieee:8533438
- **Type**: journal
- **Published**: March 2019
- **Authors**: Tobias Fehenberger, David S. Millar, Toshiaki Koike-Akino +2
- **PDF**: https://ieeexplore.ieee.org/document/8533438
- **Abstract**: Distribution matching is a fixed-length invertible mapping from a uniformly distributed bit sequence to shaped amplitudes and plays an important role in the probabilistic amplitude shaping framework. With conventional constant-composition distribution matching (CCDM), all output sequences have identical composition. In this paper, we propose multiset-partition distribution matching (MPDM), where the composition is constant over all output sequences. When considering the desired distribution as a multiset, MPDM corresponds to partitioning this multiset into equal-sized subsets. We show that MPDM allows addressing more output sequences and, thus, has a lower rate loss than CCDM in all nontrivial cases. By imposing some constraints on the partitioning, a constructive MPDM algorithm is proposed which comprises two parts. A variable-length prefix of the binary data word determines the composition to be used, and the remainder of the input word is mapped with a conventional CCDM algorithm, such as arithmetic coding, according to the chosen composition. Simulations of 64-ary quadrature amplitude modulation over the additive white Gaussian noise channel demonstrate that the block-length saving of MPDM over CCDM for a fixed gap to capacity is approximately a factor of 2.5-5 at medium to high signal-to-noise ratios.

## A Key Recovery Reaction Attack on QC-MDPC

- **ID**: ieee:8502112
- **Type**: journal
- **Published**: March 2019
- **Authors**: Qian Guo, Thomas Johansson, Paul Stankovski Wagner
- **PDF**: https://ieeexplore.ieee.org/document/8502112
- **Abstract**: Algorithms for secure encryption in a post-quantum world are currently receiving a lot of attention in the research community. One of the most promising such algorithms is the code-based scheme called QC-MDPC, which has excellent performance and a small public key size. In this paper, we present a very efficient key recovery attack on the QC-MDPC scheme using the fact that decryption uses an iterative decoding step, and this can fail with some small probability. We identify a dependence between the secret key and the failure in decoding. This can be used to build what we refer to as a distance spectrum for the secret key, which is the set of all distances between any two ones in the secret key. In a reconstruction step, we then determine the secret key from the distance spectrum. The attack has been implemented and tested on a proposed instance of QC-MDPC for 80-bit security. It successfully recovers the secret key in minutes. A slightly modified version of the attack can be applied on proposed versions of the QC-MDPC scheme that provides IND-CCA security. The attack is a bit more complex in this case, but still very much below the security level. The reason why we can break schemes with proved CCA security is that the model for these proofs typically does not include the decoding error possibility. At last, we present several algorithms for key reconstruction from an empirical distance spectrum. We first improve the naïve algorithm for key reconstruction by a factor of about 3 0000, when the parameters for 80-bit security are implemented. We further develop the algorithm to deal with errors in the distance spectrum. This ultimately reduces the requirement on the number of ciphertexts that need to be collected for a successful key recovery.

## Key Technologies and Measurements for DTMB-A System

- **ID**: ieee:8368065
- **Type**: journal
- **Published**: March 2019
- **Authors**: Jian Song, Chao Zhang, Kewu Peng +8
- **PDF**: https://ieeexplore.ieee.org/document/8368065
- **Abstract**: Digital terrestrial television multimedia broadcasting-advanced (DTMB-A), the new digital terrestrial television broadcasting (DTTB) system proposed by China, has been accepted by International Telecommunications Union as the international DTTB standard in July, 2015. By adopting several advanced technologies, such as near-capacity channel coding and modulation as well as improved frame structure, DTMB-A can provide faster system synchronization, higher receiving sensitivity, better performance against multipath effect, higher spectrum efficiency, and the flexibility for future extension, compared with its previous generation, DTMB system. This paper provides the technical analyses on the physical layer specifications of DTMB-A system in detail, together with the discussion on the key technologies adopted. Laboratory test and field trial results are also given which demonstrate that DTMB-A can offer excellent overall system performance for both fixed and mobile receptions under complicated terrestrial broadcasting conditions, and is capable of supporting multiple services with different quality of service requirements.

## Performance of Interleaved Block Codes With Burst Errors

- **ID**: ieee:8464100
- **Type**: journal
- **Published**: March 2019
- **Authors**: Roy D. Cideciyan, Simeon Furrer, Mark A. Lantz
- **PDF**: https://ieeexplore.ieee.org/document/8464100
- **Abstract**: A Gilbert-Elliott channel for symbol errors is considered to analyze the performance of interleaved error correction codes with a fixed block size in the presence of burst errors. The proposed channel model for symbol errors is based on a simplified Gilbert channel for bit errors, which enables direct comparisons of the performance of block codes with different symbol sizes. The autocorrelation function between two erroneous symbols within an interleaved codeword is computed. An exact expression for the codeword-error probability is derived from the symbol-based channel model. A tight lower bound on the codeword-error probability and error floors, which are observed when the average raw bit-error rate is low, are analyzed using the bit-based channel model.

## Learning Mixtures of Sparse Linear Regressions Using Sparse Graph Codes

- **ID**: ieee:8429915
- **Type**: journal
- **Published**: March 2019
- **Authors**: Dong Yin, Ramtin Pedarsani, Yudong Chen +1
- **PDF**: https://ieeexplore.ieee.org/document/8429915
- **Abstract**: In this paper, we consider the mixture of sparse linear regressions model. Let β(1), . . ., β(L) ∈ ℂn be L unknown sparse parameter vectors with a total of K non-zero elements. Noisy linear measurements are obtained in the form yi = xiH β(ℓi) + wi, each of which is generated randomly from one of the sparse vectors with the label ℓi unknown. The goal is to estimate the parameter vectors efficiently with low sample and computational costs. This problem presents significant challenges as one needs to simultaneously solve the demixing problem of recovering the labels ℓi as well as the estimation problem of recovering the sparse vectors β(ℓ). Our solution to the problem leverages the connection between modern coding theory and statistical inference. We introduce a new algorithm, MixedColoring, which samples the mixture strategically using query vectors xi constructed based on ideas from sparse graph codes. Our novel code design allows for both efficient demixing and parameter estimation. To find K non-zero elements, it is clear that we need at least Θ(K) measurements, and thus the time complexity is at least (K). In the noiseless setting, for a constant number of sparse parameter vectors, our algorithm achieves the order-optimal sample and time complexities of Θ(K). In the presence of Gaussian noise,1 for the problem with two parameter vectors (i.e., L = 2), we show that the Robust Mixed-Coloring algorithm achieves near-optimal Θ(K polylog(n)) sample and time complexities. When K = O(nα) for some constant α ∈ (0, 1) (i.e., K is sublinear in n), we can achieve sample and time complexities both sublinear in the ambient dimension. In one of our experiments, to recover a mixture of two regressions with dimension n = 500 and sparsity K = 50, our algorithm is more than 300 times faster than EM algorithm, with about one third of its sample cost.

## FPGA Implementation of FEC Encoder with BCH & LDPC Codes for DVB S2 System

- **ID**: ieee:8711664
- **Type**: conference
- **Published**: 7-8 March 
- **Authors**: Durga Digdarsini, Deepak Mishra, Sanjay Mehta +1
- **PDF**: https://ieeexplore.ieee.org/document/8711664
- **Abstract**: This paper gives the design and implementation of Xilinx FPGA based Forward Error Correction (FEC) encoder for DVB S2 system which includes BCH code followed by LDPC code and finally bit mapped to constellation for QPSK modulation. DVB-S2 FEC: ($\mathbf{n}=64800,\ \mathbf{k}=32400$) rate 1/2 code, with QPSK modulation scheme is considered as target for FPGA implementation. The architecture in this design efficiently uses pipeline technique along with parallel processing to optimize the hardware resources and overall latency, to accomplish FEC encoding for DVB S2 system. Coding is completed in Verilog HDL with Xilinx Virtex6 XC6VLX240T FPGA as target for hardware realization and QuestaSim simulator is used to complete the functional simulation.

## Performance Analysis of Mixed-Scheduling Belief Propagation for LDPC Decoders in OFDM System under Double Fading Channels

- **ID**: ieee:8938879
- **Type**: conference
- **Published**: 6-8 March 
- **Authors**: Mayura Prakodrat, Thanomsak Sopon, Kidsanapong Puntsri +2
- **PDF**: https://ieeexplore.ieee.org/document/8938879
- **Abstract**: This paper presents the performance analysis of orthogonal frequency division multiplexing (OFDM) system using a mixed-scheduling belief propagation (MBP) algorithm for LDPC decoding where a double fading channels is considered. The MBP method is designed based on the LBP algorithm for the left-to-right direction (LBP-LR) and right-to-left direction (LBP-RL). Additionally, the bit error rate (BER) performance comparison of the BP, LBP, and MBP algorithms for LDPC decoding is proposed. The simulation results showed that the bit error rate (BER) performance of the MBP gave better BER than the BP and LBP algorithms, respectively.

## FPGA-Based Real-Time Soft-Decision LDPC Performance Verification for 50G-PON

- **ID**: ieee:8696463
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Mingwei Yang, Linlin Li, Xiang Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/8696463
- **Abstract**: We have studied the combined use of the mother LDPC code from ongoing industrial standards and soft-decision to further improve the performance of the FEC. Through experimental measurements based on a real-time FPGA platform, we found that this approach offers ∼1.3 dB more gross coding gain.

## Nonbinary Polar Coding for Multilevel Modulation

- **ID**: ieee:8696792
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Semih Cayci, Toshiaki Koike-Akino, Ye Wang
- **PDF**: https://ieeexplore.ieee.org/document/8696792
- **Abstract**: We investigate nonbinary polar-coded modulations, which achieve a significant performance gain of at least 1 dB compared to binary counterparts at a short block-length of 2048 bits.

## Partition-Based Probabilistic Shaping for Fiber-Optic Communication Systems

- **ID**: ieee:8696571
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Tobias Fehenberger, David S. Millar, Toshiaki Koike-Akino +2
- **PDF**: https://ieeexplore.ieee.org/document/8696571
- **Abstract**: Various aspects of distribution matchers (DMs) with constant and variable composition are reviewed. LDPC-coded fiber simulations of 64QAM shaped via a multiset-partition DM show significantly increased reach and information rate over a constant-composition DM.

## Rate-Adaptive Probabilistic Shaping Enabled by Punctured Polar Codes with Pre-Set Frozen Bits

- **ID**: ieee:8696832
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Shajeel Iqbal, Metodi Plamenov Yankov, S⊘ren Forchhammer
- **PDF**: https://ieeexplore.ieee.org/document/8696832
- **Abstract**: We propose to pre-set the frozen bits of a rate-adaptive punctured polar-coded system to pseudo-random sequences. The many-to-one probabilistic shaping gains are improved to 2 dB («160 km) w.r.t. the standard punctured polar-coded system.

## Joint Source-Channel Coding via Compressed Distribution Matching in Fiber-Optic Communications

- **ID**: ieee:8696846
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Tsuyoshi Yoshida, Magnus Karlsson, Erik Agrell
- **PDF**: https://ieeexplore.ieee.org/document/8696846
- **Abstract**: The variability of source entropy due to data idling is inconsistent with most studies' assumptions in probabilistic shaping. We propose a distribution matcher sensitive to the source entropy, and discuss its impacts on fiber-optic communications.

## Single-Wavelength and Single-Photodiode Entropy-Loaded 554-Gb/s Transmission Over 22-km SMF

- **ID**: ieee:8696539
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Xi Chen, Sethumadhavan Chandrasekhar, Junho Cho +1
- **PDF**: https://ieeexplore.ieee.org/document/8696539
- **Abstract**: We demonstrate the transmission of intensity-modulated and direct-detected (IM-DD) entropy-loaded signals over 22-km SMF with 554-Gb/s line rate and 460.9-Gb/s net bit rate.

## 74.38 Tb/s Transmission Over 6300 km Single Mode Fiber with Hybrid EDFA/Raman Amplifiers

- **ID**: ieee:8696534
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: M. Ionescu, D. Lavery, A. Edwards +7
- **PDF**: https://ieeexplore.ieee.org/document/8696534
- **Abstract**: Transmission of 306×35 GBd, dual polarization, 64-ary geometrically shaped channels over 90× 70 km of SMF was demonstrated, achieving a net throughput of 74.38 Tb/s. A combination of hybrid fiber spans and EDFA/Raman amplifiers enabled a continuous gain bandwidth of 10.8 THz.

## 35-Tb/s C-Band Transmission Over 800 km Employing 1-Tb/s PS-64QAM Signals Enhanced by Complex 8 × 2 MIMO Equalizer

- **ID**: ieee:8696972
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: T. Kobayashi, M. Nakamura, F. Hamaoka +6
- **PDF**: https://ieeexplore.ieee.org/document/8696972
- **Abstract**: We demonstrate the full C-band 1-Tb/s/λ WDM 800-km transmission with 35-Tb/s capacity employing novel complex 8 × 2 MIMO equalizer which enables simultaneous compensation of imperfections of transmitter and receiver of 120-Gbaud probabilistically-shaped-64QAM signals.

## Single-Wavelength Symmetric 50 Gbit/s Equalization-Free NRZ IM/DD PON with up to 33 dB Loss Budget and Fiber Transmission over >40 km

- **ID**: ieee:8696513
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Robert Borkowski, Harald Schmuck, Giancarlo Cerulo +2
- **PDF**: https://ieeexplore.ieee.org/document/8696513
- **Abstract**: We demonstrate burst-mode upstream and continuous-mode downstream transmission in a 50G TDM-PON system, achieving up to 33-dB loss budget with a maximum of 77-km SMF transmission before any equalization. The system is enabled by semiconductor optical amplifiers at the transceivers.

## Demonstration of 100-Gb/s/λ PAM-4 TDM-PON Supporting 29-dB Power Budget with 50-km Reach using 10G-class O-Band DML Transmitters

- **ID**: ieee:8696951
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Jiao Zhang, Jianjun Yu, Hungchang Chien +4
- **PDF**: https://ieeexplore.ieee.org/document/8696951
- **Abstract**: We experimentally demonstrated 100-Gb/s/λ PAM-4 TDM-PON downstream transmission in O-band using 10G-class DML and SOA pre-amplifier at the receivers. Power budget of 29 dB was achieved after 50-km transmission at pre-FEC BER threshold of 1 × 10-2.

## Single-Channel Direct Detection Reception Beyond 1 Tb/s

- **ID**: ieee:8696932
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: D. Che, S. Chandrasekhar, X. Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/8696932
- **Abstract**: We demonstrate the world-first single-channel direct detection beyond 1-Tb/s with 1.26-Tb/s line rate and 1.02-Tb/s net rate after 100-km SSMF, via an 86-GHz Stokes vector receiver that recovers totally single-polarization-equivalent 252-Gbaud probabilistic-shaped 64-QAM signal.

## Multi-Rate Prefix-Free Code Distribution Matching

- **ID**: ieee:8696370
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Junho Cho, Peter J. Winzer
- **PDF**: https://ieeexplore.ieee.org/document/8696370
- **Abstract**: We propose a multi-rate prefix-free code distribution matching (PCDM) algorithm that implements a fixed-length probabilistic constellation shaping. It uses various small codebooks in an adaptive manner, thereby improving the shaping performance of PCDM.

## Optimum Bit-Level Distribution Matching with at Most O(N3) Implementation Complexity

- **ID**: ieee:8696977
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Yohei Koganei, Kiichi Sugitani, Hisao Nakashima +1
- **PDF**: https://ieeexplore.ieee.org/document/8696977
- **Abstract**: An algorithm of distribution matching which could be effectively implemented for short block lengths of around 100 bit or less is proposed, enabling better performance than the constant composition schemes with the same block lengths.

## Integrated Dual-DFB Laser for 408 GHz Carrier Generation Enabling 131 Gbit/s Wireless Transmission over 10.7 Meters

- **ID**: ieee:8697005
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Shi Jia, Mu-Chieh Lo, Lu Zhang +12
- **PDF**: https://ieeexplore.ieee.org/document/8697005
- **Abstract**: A monolithically integrated dual-DFB laser generates a 408 GHz carrier used for demonstrating a record-high single-channel bit rate of 131 Gbit/s transmitted over 10.7 m. 16-QAM-OFDM modulation and specific nonlinear equalization techniques are employed.

## 5×510 Gbps Single-Polarization Direct-Detection WDM Transmission over 80 km of SSMF

- **ID**: ieee:8696275
- **Type**: conference
- **Published**: 3-7 March 
- **Authors**: Son Thai Le, Karsten Schuh, Roman Dischler +3
- **PDF**: https://ieeexplore.ieee.org/document/8696275
- **Abstract**: We demonstrate 5-channel WDM DD transmissions over 80 km of SSMF with a net data rate per channel of 432 Gbps using either Kramers-Kronig detection or a low-complexity interference cancellation scheme.

## Design of Unequal Error Protection LDPC Code in PPM and LDPC Optical Communication System

- **ID**: ieee:8873472
- **Type**: conference
- **Published**: 29-31 Marc
- **Authors**: Jingsong Xiang, Yimiao Wu, Xiaohui Lu +1
- **PDF**: https://ieeexplore.ieee.org/document/8873472
- **Abstract**: In the space optical communication system, the link power loss is large, and the unequal error protection (UEP) scheme can effectively protect more important data in the transmission process and save transmission power. However, the performance of existing unequal error protection LDPC codes used directly in space optical communication systems is not ideal. In this paper, a design scheme of LDPC codes with multilevel unequal error protection performance is proposed for pulse position modulation (PPM) and Low-density parity-check (LDPC) codes iterative demodulation system. The scheme is aimed at maximizing the average variable node degree of each protection level to improve the unequal error protection characteristics of LDPC codes while combining the improved external information in the BICM-ID system extrinsic information transfer(EXIT) method to analyze the convergence threshold of degree distribution and optimize the degree distribution of UEP-LDPC code by iterative linear programming to obtain the minimum threshold and satisfy the unequal error protection characteristics. The simulation results show that the UEP-LDPC code constructed in this paper has improved performance compared with the existing UEP-LDPC code.

## Wireless Sensors Converged Network Enhancement

- **ID**: ieee:8893181
- **Type**: conference
- **Published**: 21-24 Marc
- **Authors**: Omar R. Daoud, Ahlam A. Damati
- **PDF**: https://ieeexplore.ieee.org/document/8893181
- **Abstract**: This work deals with the proposition of machine-to-machine communications enhancement. Thus, a convergence between the wireless sensor network and the wireless mobile network has been studied. It is divided into three main parts; making use of one of our previously published work to enhance the wireless mobile network based on combatting the peak-to-average power ratio problem, building an actual wireless sensor network to observe a real data, and proposing a converged network as an enhancement. To validate the proposition, an extensive simulation has been performed based on observing some cretin performance parameters such as the round, the dying time, the consumed energy. Thus, the comparison has been made between the conventional wireless sensor network and the converged one. It shows a remarkable results and reaches 78% delay reduction. However, further studies should be made to investigate the routing algorithms in order to enhance the consumed energy by the sensor nodes.

## Improving Short-Length LDPC Codes with a CRC and Iterative Ordered Statistic Decoding : (Invited Paper)

- **ID**: ieee:8693053
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Wei Zhou, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/8693053
- **Abstract**: The following topics are dealt with: learning (artificial intelligence); optimisation; channel coding; neural nets; probability; statistical analysis; pattern classification; stochastic processes; 5G mobile communication; gradient methods.

## Protograph-Based LDPC Code Design for Probabilistic Shaping with On-Off Keying

- **ID**: ieee:8693049
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Alexandru Dominic Git, Balázs Matuz, Fabian Steiner
- **PDF**: https://ieeexplore.ieee.org/document/8693049
- **Abstract**: This work investigates protograph-based low-density parity-check (LDPC) codes for the additive white Gaussian noise (AWGN) channel with on-off keying (OOK) modulation. A non-uniform distribution of the OOK modulation symbols is considered to improve the power efficiency especially for low signal-to-noise ratios (SNRs). To this end, a specific transmitter architecture based on time sharing is proposed that allows probabilistic shaping of (some) OOK modulation symbols. Tailored protograph-based LDPC code designs outperform standard schemes with uniform signaling and off-the-shelf codes by 1.1 dB for a transmission rate of 0.25 bits/channel use and by 0.9 dB for 0.67 bits/channel use.

## Discretized Density Evolution for Rate Compatible Modulation : Invited Presentation

- **ID**: ieee:8693058
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Mariano Eduardo Burich, Richard Demo Souza, Javier Garcia-Frias
- **PDF**: https://ieeexplore.ieee.org/document/8693058
- **Abstract**: In this paper, we develop, for the first time in the literature, a Density Evolution analysis of Rate Compatible Modulation (RCM), which is challenging due to the way symbols in RCM are generated as weighted sums of the input bits. We consider uniform and non-uniform memoryless binary sources. By allowing the weights to be real numbers, rather than integers as in previous work, we propose, for the first time in the literature, an optimization procedure that automatically obtains the weights of the RCM scheme for a desired source entropy, signal to noise ratio, and information rate.

## Binary Message Passing Decoding of Product Codes Based on Generalized Minimum Distance Decoding : (Invited Paper)

- **ID**: ieee:8692862
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Alireza Sheikh, Alexandre Graell i Amat, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/8692862
- **Abstract**: We propose a binary message passing decoding algorithm for product codes based on generalized minimum distance decoding (GMDD) of the component codes, where the last stage of the GMDD makes a decision based on the Hamming distance metric. The proposed algorithm closes half of the gap between conventional iterative bounded distance decoding (iBDD) and turbo product decoding based on the Chase-Pyndiah algorithm, at the expense of some increase in complexity. Furthermore, the proposed algorithm entails only a limited increase in data flow compared to iBDD.

## Spatially Coupled LDPC Codes and the Multiple Access Channel

- **ID**: ieee:8692899
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Sebastian Cammerer, Xiaojie Wang, Yingyan Ma +1
- **PDF**: https://ieeexplore.ieee.org/document/8692899
- **Abstract**: We consider spatially coupled low-density parity-check (SC-LDPC) codes within a non-orthogonal interleave division multiple access (IDMA) scheme to avoid cumbersome degree profile matching of the LDPC code components to the iterative multi-user detector (MUD). Besides excellent decoding thresholds, the approach benefits from the possibility of using rather simple and regular underlying block LDPC codes owing to the universal behavior of the resulting coupled code with respect to the channel front-end, i.e., the iterative MUD. Furthermore, an additional outer repetition code makes the scheme flexible to cope with a varying number of users and user rates, as the SC-LDPC itself can be kept constant for a wide range of different user loads. The decoding thresholds are obtained via density evolution (DE) and verified by bit error rate (BER) simulations. To keep decoding complexity and latency small, we introduce a joint iterative windowed detector/decoder imposing carefully adjusted sub-block interleavers. Finally, we show that the proposed coding scheme also works for Rayleigh channels using the same code with tolerable performance loss compared to the additive white Gaussian noise (AWGN) channel.

## Performance of Self-Corrected Min-Sum Decoding Algorithm for Decoders with Quantized Input

- **ID**: ieee:8717757
- **Type**: conference
- **Published**: 20-22 Marc
- **Authors**: Aleksei Kharin, Igor Volkov, Aleksei Ovinnikov +2
- **PDF**: https://ieeexplore.ieee.org/document/8717757
- **Abstract**: In this paper we explore the Min-Sum decoding algorithm for LDPC codes with self-correction (SC-MS) modification and how it affects the error correction performance for quantized input data. Three levels of quantization are observed: 3-, 2- and 1-bit.It was shown that the self-corrected modification significantly improves the performance of Min-Sum decoding algorithm with quantized input in comparison with basic Min-Sum decoding algorithm. Convergence of the algorithm is also better than for basic Min-Sum algorithm.Results of error correction performance and convergence are presented for two codes: CCSDS (8176, 7156) and IEEE 802.3an (2048, 1723) LDPC. The results are also presented for the SC APP-based and basic Min-Sum decoding algorithms.

## Scaling the Fast x86 DVB-S2 Decoder to 1 Gbps

- **ID**: ieee:8742225
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Eugene Grayver
- **PDF**: https://ieeexplore.ieee.org/document/8742225
- **Abstract**: Software implementation of LDPC decoders has been an active area of development for the last 10 years. Researchers have focused on implementing the computationally expensive algorithm on both GPPs and GPUs. A major leap in performance was reported in the groundbreaking paper by Bertrand le Gal [2]. This paper builds on the work in [2] by considering the scaling of that implementation on modern many-core processors. We look at the performance of LDPC code specified in the DVB-S2 standard. The large block size of the DVB-S2 code makes the memory architecture of the processor just as important as the clock rate and instruction set. We present results for two generations of Intel Xeons, an Intel Phi (KNL), the recently released AMD EPYC. The key finding is that performance scaling is limited by the amount of available cache memory rather than the number of cores. We also find that heavily multi-threaded, but deterministic software architecture benefits from explicit allocation of threads to cores vs. allowing the operating system to manage threading. The maximum throughput of 1 Gbps was achieved on a mid-range AMD server - issuing a new era of all-software receivers for very high rate waveforms. We also present the performance of the algorithm ported to a low-power ARM processor and compare that to a low-end Intel Core.

## Acquisition and tracking for communications between Lunar South Pole and Earth

- **ID**: ieee:8742112
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Dariush Divsalar, Marc Sanchez Net, Kar-Ming Cheung
- **PDF**: https://ieeexplore.ieee.org/document/8742112
- **Abstract**: In this paper we design and analyze an end-to-end communication system between a lander/rover on the surface of the lunar South Pole and an Earth station. The acquisition and tracking system is discussed in detail. The communication system on the lander or rover could be used for the Earth-to-Moon communication. To communicate to and from the lander/rover on the lunar South Pole, low and/or medium directional antennas onboard the lander/rover will have to be pointed at low elevation angles between 2 to 10 degrees, thus causing multipath fading effects due to reflection of a portion of the transmitted electromagnetic waves from the surface of the Moon that are not commonly encountered in traditional deep space communications between a spacecraft and a ground station. To design and analyze such a communication system, and in particular the acquisition and tracking system, in the presence of multipath fading, first we model the fading channel based on existing and simulated data. In addition to multipath fading, the channel also introduces Doppler frequency up to 11.5 KHz, and Doppler rate up to 0.735 Hz/sec. For coherent reception the Doppler frequency, which is time varying, should be acquired and the incoming carrier phase, which includes the fading phase, should be tracked in the presence of multipath fading. For this communication system in addition to estimating the received carrier phase, the amplitude of the fading signal should also be estimated, in particular to be used in the decoder. In addition to acquisition and tracking, we consider simple modulation and coding schemes. Space diversity using two antennas on Earth to mitigate the effects of fading could also be used. We design phase-locked loops and frequency sweeping schemes robust to the attenuations due to fading. After designing various components of the communication system, we use Simulink models to obtain the end-to-end performance of the communication link under investigation. Based on the available data, the fading channel can be accurately modeled as a Rician fading channel with Rician parameter of 10 dB, and Doppler spread that depends on the Doppler frequency and the transmit/receive antenna patterns. The challenge is how to make such a communication system robust in the presence of the multipath fading where the Doppler spread changes in time and thus produces fading with time-varying durations (short and very long fades). In summary, this paper covers communication system design, performance analysis, and simulations for performance of Doppler frequency acquisition, tracking, uncoded system, and coded system under ideal interleaving assumption with hard decision over communication link between a lander/rover at the Lunar south pole and a DSN Earth station in presence of Rician fading.

## Proximity Link Telecommunication and Tracking Scenarios for a Potential Mars Sample Return Campaign

- **ID**: ieee:8741917
- **Type**: conference
- **Published**: 2-9 March 
- **Authors**: Charles D. Edwards, Allen H. Farrington, Roy E. Gladden +6
- **PDF**: https://ieeexplore.ieee.org/document/8741917
- **Abstract**: A Mars Sample Return (MSR) campaign would involve a series of three flight missions to acquire and cache Mars samples, retrieve those samples and launch them into Mars orbit, and then capture these samples and return them to Earth. Relay communications would be crucial for supporting this campaign, characterized by multiple critical events, complex surface operations, and an on-orbit Mars rendezvous. The existing Mars relay network offers significant capability, and efforts are underway to maximize the likelihood that one or more of these current assets will still be operational in the timeframe of an MSR campaign. In addition, the Earth Return Orbiter (ERO) element of a campaign could serve as a primary relay asset, if it can achieve a useful relay orbit by the time of arrival of the Sample Retrieval Lander mission. We describe key operational challenges of the MSR campaign that would drive the required relay capabilities, and characterize the performance of the existing relay orbiters as well as ERO itself in meeting those relay needs.

## Performance of 5GNR with Interference Alignment

- **ID**: ieee:8713752
- **Type**: conference
- **Published**: 19-21 Marc
- **Authors**: Khawla A. Alnajjar, Mohamed El-Tarhuni
- **PDF**: https://ieeexplore.ieee.org/document/8713752
- **Abstract**: Recently, a New Radio (NR) structure has been proposed for fifth generation (5G) mobile radio systems to support higher data rates and low latency scenarios. In this paper, we investigate the performance of 5G New Radio (5GNR) using precoding for Interference Alignment (IA). The system is based on an OFDM structure following the NR scheme with zero forcing receiver. It is shown that with proper selection of the precoder, an improvement of about one order of magnitude in the bit error rate due to IA is achieved.

## Iterative Carrier Phase Recovery for MPSK Systems Based on Simplified EM Algorithm

- **ID**: ieee:8729542
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Xin Man, Dun Mao, Xiaohong Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/8729542
- **Abstract**: This letter deals with the problem of carrier phase recovery for low-density parity-check (LDPC) coded MPSK systems at low signal-to-noise ratios (SNR). By utilizing Taylor series expansion and the constant-envelope characteristic of PSK signals, we greatly simplify the expectation maximization (EM) algorithm to recover the carrier phase. The proposed method works with simple operations of phase subtraction and accumulation instead of complex multiplication and accumulation in the EM algorithm. Apart from its low complexity, the simulation results for the case of 8-PSK system with a (1944; 972) irregular LDPC code show that the performance loss compared to the EM algorithm is negligible.

## Short Polar-coded Non-coherent Receiver

- **ID**: ieee:8729533
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Huangxia Xu, Chaofan Chen, Yanming Xue
- **PDF**: https://ieeexplore.ieee.org/document/8729533
- **Abstract**: Emergency communications will be the key to deal with natural or man-made emergencies. Their prerequisites are the short frame burst under limited resources, as well as reliable bit error rate (BER) performance in low signal to noise ratio (SNR). With respect to short codes, polar codes normally outperform Low Density Parity Check (LDPC) codes and convolutional codes, which makes them more suitable for the emergency communications. However, the traditional polarcoded receiver either has a large discrepancy between the practical receiving performance and the theoretical one, or has high complexity, which limits its applications for emergency communications. Hence, to adapt to such scenario, in this paper we invoke an iterative mechanism into the receiver and propose a new non-coherent detection module, namely, short polar-coded non-coherent detection (SPND) module, as well as its corresponding detection algorithm, namely, outercode-feedback-innercode (OCFIC) BCJR-based algorithm. The simulations demonstrate that, with the condition of non-coherent channel and of the target BER of 10-5, the performance gap between the noncoherent detection scheme with the proposed SPND module and the coherent counterpart can be reduced to around 1dB. Meanwhile, the SPND module with short polar codes is superior to conventional non-coherent receiver with short LDPC codes, short polar codes and (2,1,7) convolutional codes by 1.2dB, 2.8dB and 3dB, respectively. Hardware implementation of the module is also presented in this paper.

## Research on Polarization Code Encoding and Decoding Algorithm Based on HARQ Technology

- **ID**: ieee:8729289
- **Type**: conference
- **Published**: 15-17 Marc
- **Authors**: Tingting Yu, Wei Nie
- **PDF**: https://ieeexplore.ieee.org/document/8729289
- **Abstract**: As a 5G control channel coding scheme, the polarization code can reach the Shannon limit theoretically. However, under the condition of medium and short code, the communicationeffect of polarization code is not ideal. To solve this problem, a de-coding based on HARQ technology is proposed. The algorithm adds feedback retransmission based on CA-SCL decoding, and retransmits some information bits by using a highly polarized channel, which can compensate for the problem that channel polarization is not sufficient in the case of medium and short codes, and reduces the bit error rate. However, adding a retransmission will increase the decoding delay. Therefore, the algorithm is applicable to scenarios with low latency requirements. Through theoretical analysis and MATLAB simulation, when N=256, when the bit error rate is 0.01, the improved algorithm obtains a gain of 0.5dB compared with the CA-SCL decoding algorithm. The decoding performance of the improved algorithm is verified under different code lengths. It can be seen that as the code length increases, the advantage of the improved algorithm is gradually reduced. Therefore, the algorithm is more suitable for short code.

## Error correction using LDPC code for performance improvement in clipped and biased OFDM with direct detection over optical fiber

- **ID**: ieee:8877013
- **Type**: conference
- **Published**: 13-15 Marc
- **Authors**: Usha Choudhary, Vijay Janyani
- **PDF**: https://ieeexplore.ieee.org/document/8877013
- **Abstract**: Paper presents a performance comparison for DC-biased OFDM and clipped OFDM for unipolar transmission over optical fiber communication systems with forward error check encoder, LDPC (32400, 64800). Asymmetrically clipped OFDM is being studied intensively for possible future technology in a short range optical channel with low power applications as well as adaptive data rate allocation in network because same optimized design parameters can be used for large constellation size (up to QAM-1024). OFDM over optical fiber comes with several challenges like accommodation of existing opto-electric resources for futuristic approach. Inclusion of FEC scheme improves the BER performance, although data array size for transmission and total electrical power has increased. For OFDM without FEC we need laser power 3 dBm for lowest BER in range ($1^{*}10^{-5}$ and $1^{*}10^{-7}$) where as in LDPC coded OFDM lowest BER ($1^{*}10^{-5}$ and $1^{*}10^{-s}$) is observed for biased and clipped OFDM respectively.
