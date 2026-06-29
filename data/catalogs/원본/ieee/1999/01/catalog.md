# IEEE Xplore — 1999-01


## Constructing low-density parity-check codes with circulant matrices

- **Status**: ✅
- **Reason**: circulant 행렬 기반 LDPC 구성 + 저중량 codeword 제어(error floor) → 바이너리 QC형 LDPC 코드 설계(E)
- **ID**: ieee:814359
- **Type**: conference
- **Published**: 1999
- **Authors**: J. W. Bond, S. Hui, H. Schmidt
- **PDF**: https://ieeexplore.ieee.org/document/814359
- **Abstract**: This is a report on the authors' ongoing effort to implement low-density parity-check codes with iterative belief propagation decoding in a communication system. The system requires the codes to have block lengths from 1000 to 2000 bits. We describe two different methods of constructing the codes using: (1) a combination of random and circulant matrices, and (2) random and circulant matrices with constraints to control the number of low weight codewords. We illustrate the performances of the different constructions with simulations.

## Channel code blocklength and rate optimization for progressive image transmission

- **Status**: ❌
- **Reason**: 터보코딩 기반 점진적 영상전송의 블록길이/부호율 최적화 — JSCC 응용 특이적, LDPC ECC 기법 없음
- **ID**: ieee:796817
- **Type**: conference
- **Published**: 1999
- **Authors**: P. G. Sherwood, Xiaodong Tian, K. Zeger
- **PDF**: https://ieeexplore.ieee.org/document/796817
- **Abstract**: We investigate the problem of selecting blocklength and code rate for progressive image transmission, motivated by turbo coding methods where the performance improves with blocklength. The problem is to balance the tradeoff among error protection, source coding rate, and delay. We propose a general performance measure for evaluating progressive transmission and use dynamic programming to determine the channel code parameters based on the progressive performance. Performance results are provided for the evaluation of the gains over less complex methods as a function of channel error rate.

## The impact of using multicode transmission in the WCDMA system

- **Status**: ❌
- **Reason**: WCDMA multicode transmission with simple parity precoder for PAPR; wireless-specific, no transferable LDPC ECC technique.
- **ID**: ieee:780607
- **Type**: conference
- **Published**: 1999
- **Authors**: T. Ottosson, T. Palenius
- **PDF**: https://ieeexplore.ieee.org/document/780607
- **Abstract**: The multicode transmission scheme for achieving higher data rates in the WCDMA system is studied especially considering envelope variations and nonlinear power amplifiers. Results show that using three codes instead of a single code reduces the power efficiency of the power amplifier from about 40% down to 25% at a adjacent channel power ratio of -40 dB. However, by the introduction of a simple but very effective precoder it is possible to maintain the power efficiency of the amplifier at 40%. This precoder is a simple parity check code where the fourth bit is the parity of the three first bits. Assuming that four orthogonal spreading codes are used this precoder construction limits the envelope variations to that of a single code transmission thus allowing for the same output backoff of the power amplifier as for the single code transmission scheme. It is furthermore shown that the precoded scheme performs as well as the multicode scheme using three codes.

## Parity check codes for partial response channels

- **Status**: ❌
- **Reason**: 부분응답 채널용 outer 패리티체크+터보 직렬연접 APP 반복디코딩 — 채널검출기 결합 응용, LDPC BP에 떼어낼 부호비의존 기법 약함; 다만 애매하나 비-LDPC 연접+채널특이
- **ID**: ieee:830156
- **Type**: conference
- **Published**: 1999
- **Authors**: M. Oberg, P. H. Siegel
- **PDF**: https://ieeexplore.ieee.org/document/830156
- **Abstract**: The use of turbo coding and decoding techniques in digital magnetic recording is now being given serious consideration. Major technical concerns are implementation complexity and decoding delay. In this paper, we present and analyze the performance of a simple, serial concatenation scheme comprising an outer parity check code, interleaver, and a precoded partial response channel. We apply an iterative decoding procedure incorporating separate a posteriori probability (APP) detectors for the code and precoded channel. Simulation results for a dicode channel show a bit-error-rate (BER) of 10/sup -5/ at rate-normalized signal-to-noise ratio SNR=6.7 dB for a rate 8/9 code, representing a gain of about 3.5 dB over the uncoded channel. We also present simulation results for higher-rate codes and other partial response channels, confirming the performance benefits of the new scheme.

## Interleaved parity check codes and reduced complexity detection

- **Status**: ❌
- **Reason**: Interleaved parity-check codes for magnetic recording with joint channel detection; non-LDPC parity codes, no transferable binary LDPC BP/HW/code-design technique.
- **ID**: ieee:765514
- **Type**: conference
- **Published**: 1999
- **Authors**: Zi-Ning Wu, P. A. McEwan, K. K. Fitzpatrick +1
- **PDF**: https://ieeexplore.ieee.org/document/765514
- **Abstract**: We show that high rate interleaved parity check (IPC) codes provide significant coding gain on the magnetic recording channel. A reduced complexity detector performing joint channel detection and IPC decoding is introduced. Simulation result shows an SNR gain of 1.6 dB for the E/sup 2/PR4 channel at a bit error rate of 10/sup -5/, using a rate 196/200 4-way interleaved parity check code.

## Impact of amplifier constraints on modem design for broadband wireless links

- **Status**: ❌
- **Reason**: 광대역 무선 모뎀 설계/비용 튜토리얼 — ECC 부호 기법 없음
- **ID**: ieee:810917
- **Type**: conference
- **Published**: 1999
- **Authors**: B. Cochran, R. McCallister, J. Lieberreu
- **PDF**: https://ieeexplore.ieee.org/document/810917
- **Abstract**: Broadband wireless access (BWA) must make sound business sense to be a successful 'last-mile' solution technology, for it faces stiff cost competition from phone-line and cable broadband-access alternatives. The challenge to modem designers is to develop technology which improves the BWA return-on-investment (ROI), to wit: minimize the installed equipment (total system, not just modem) cost while maximizing the data-bearing capacity of millimeter-wave links. BWA links exhibit pathologies and cost models distinct from those of wired links, and these distinctions should be reflected in a well-designed BWA modem. This tutorial paper discusses BWA ROI within the context of a system-level cost concept relates this model to primary LMDS link pathologies, and suggests several modem-level features which will be required to address BWA ROI challenges. A few specific modem design approaches are noted to demonstrate that these BWA design challenges are readily addressable.

## Generalized low density (Tanner) codes

- **Status**: ❌
- **Reason**: GLD/Tanner codes using algebraic block-code SISO component decoders, not binary LDPC BP; generalized LDPC relying on non-LDPC component decoding -> excluded.
- **ID**: ieee:767979
- **Type**: conference
- **Published**: 1999
- **Authors**: J. Boutros, O. Pothier, G. Zemor
- **PDF**: https://ieeexplore.ieee.org/document/767979
- **Abstract**: We build a class of pseudo-random error correcting codes, called generalized low density codes (GLD), from the intersection of two interleaved block codes. GLD code performance approaches the channel capacity limit and the GLD decoder is based on simple and fast SISO (soft input-soft output) decoders of smaller block codes. GLD codes are a special case of Tanner codes and a generalization of Gallager's LDPC codes. It is also proved by an ensemble performance argument that these codes are asymptotically good in the sense of the minimum distance criterion. The flexibility in selecting the parameters of GLD codes makes them suitable for small and large block length forward error correcting schemes.

## A low complexity FEC scheme based on the intersection of interleaved block codes

- **Status**: ❌
- **Reason**: GLD codes from interleaved BCH with component-code iterative decoding; generalized LDPC on algebraic decoders, ensemble/ML theory, no transferable binary LDPC BP/HW.
- **ID**: ieee:778060
- **Type**: conference
- **Published**: 1999
- **Authors**: O. Pothier, L. Brunel, J. Boutros
- **PDF**: https://ieeexplore.ieee.org/document/778060
- **Abstract**: We describe a class of asymptotically good codes built from the intersection of randomly permuted binary BCH codes. This family of pseudo-random error correcting codes, called generalized low density (GLD) codes, is a direct generalization of Gallager's low density parity check (LDPC) codes. GLD codes belong to the larger family of Tanner codes based on a random bipartite graph. We study the GLD ensemble performance and prove the asymptotically good property. We also compare GLD codes minimum distance and performance to the Varshamov-Gilbert bound and BSC capacity respectively. The results show that maximum-likelihood decoding of GLD codes achieves near capacity efficiency. The suboptimal iterative decoding of GLD codes is briefly presented. Experimental results of small and large blocklength codes are finally illustrated on both AWGN and Rayleigh fading channels.

## Good error-correcting codes based on very sparse matrices

- **Status**: ✅
- **Reason**: MacKay-Neal/Gallager 희소행렬 부호 + sum-product 디코딩 — 기초 바이너리 LDPC 부호설계/디코더 (C/E)
- **ID**: ieee:748992
- **Type**: journal
- **Published**: 1999
- **Authors**: D. J. C. MacKay
- **PDF**: https://ieeexplore.ieee.org/document/748992
- **Abstract**: We study two families of error-correcting codes defined in terms of very sparse matrices. "MN" (MacKay-Neal (1995)) codes are recently invented, and "Gallager codes" were first investigated in 1962, but appear to have been largely forgotten, in spite of their excellent properties. The decoding of both codes can be tackled with a practical sum-product algorithm. We prove that these codes are "very good", in that sequences of codes exist which, when optimally decoded, achieve information rates up to the Shannon limit. This result holds not only for the binary-symmetric channel but also for any channel with symmetric stationary ergodic noise. We give experimental results for binary-symmetric channels and Gaussian channels demonstrating that practical performance substantially better than that of standard convolutional and concatenated codes can be achieved; indeed, the performance of Gallager codes is almost as close to the Shannon limit as that of turbo codes.

## Time-varying periodic convolutional codes with low-density parity-check matrix

- **Status**: ✅
- **Reason**: Convolutional codes with low-density parity-check matrix + iterative decoding; LDPC-convolutional construction and BP-style decoder potentially transferable to binary LDPC/SC-LDPC (E), keep for Phase 3.
- **ID**: ieee:782171
- **Type**: journal
- **Published**: 1999
- **Authors**: A. Jimenez Felstrom, K. S. Zigangirov
- **PDF**: https://ieeexplore.ieee.org/document/782171
- **Abstract**: We present a class of convolutional codes defined by a low-density parity-check matrix and an iterative algorithm for decoding these codes. The performance of this decoding is close to the performance of turbo decoding. Our simulation shows that for the rate R=1/2 binary codes, the performance is substantially better than for ordinary convolutional codes with the same decoding complexity per information bit. As an example, we constructed convolutional codes with memory M=1025, 2049, and 4097 showing that we are about 1 dB from the capacity limit at a bit-error rate (BER) of 10/sup -5/ and a decoding complexity of the same magnitude as a Viterbi decoder for codes having memory M=10.

## On generalized low-density parity-check codes based on Hamming component codes

- **Status**: ❌
- **Reason**: GLD codes with Hamming component codes; min-distance theory + iterative decoding relying on component-code decoding -> generalized LDPC excluded, no transferable binary LDPC BP.
- **ID**: ieee:781010
- **Type**: journal
- **Published**: 1999
- **Authors**: M. Lentmaier, K. S. Zigangirov
- **PDF**: https://ieeexplore.ieee.org/document/781010
- **Abstract**: In this paper we investigate a generalization of Gallager's (1963) low-density (LD) parity-check codes, where as component codes single error correcting Hamming codes are used instead of single error detecting parity-check codes. It is proved that there exist such generalized low-density (GLD) codes for which the minimum distance is growing linearly with the block length, and a lower bound of the minimum distance is given. We also study iterative decoding of GLD codes for the communication over an additive white Gaussian noise channel. The performance in terms of the bit error rate, obtained by computer simulations, is presented for GLD codes of different lengths.

## Type II codes over F/sub 2/+uF/sub 2/

- **Status**: ❌
- **Reason**: F2+uF2 자기쌍대 Type II 부호·격자 — 대수 부호이론, LDPC 아님
- **ID**: ieee:746770
- **Type**: journal
- **Published**: 1999
- **Authors**: S. T. Dougherty, P. Gaborit, M. Harada +1
- **PDF**: https://ieeexplore.ieee.org/document/746770
- **Abstract**: The alphabet F/sub 2/+uF/sub 2/ is viewed here as a quotient of the Gaussian integers by the ideal (2). Self-dual F/sub 2/+uF/sub 2/ codes with Lee weights a multiple of 4 are called Type II. They give even unimodular Gaussian lattices by Construction A, while Type I codes yield unimodular Gaussian lattices. Construction B makes it possible to realize the Leech lattice as a Gaussian lattice. There is a Gray map which maps Type II codes into Type II binary codes with a fixed point free involution in their automorphism group. Combinatorial constructions use weighing matrices and strongly regular graphs. Gleason-type theorems for the symmetrized weight enumerators of Type II codes are derived. All self-dual codes are classified for length up to 8. The shadow of the Type I codes yields bounds on the highest minimum Hamming and Lee weights.

## Which codes have cycle-free Tanner graphs?

- **Status**: ❌
- **Reason**: Theoretical result that cycle-free Tanner graphs cannot support good codes; pure bound, no decoder/HW/construction to transfer.
- **ID**: ieee:782170
- **Type**: journal
- **Published**: 1999
- **Authors**: T. Etzion, A. Trachtenberg, A. Vardy
- **PDF**: https://ieeexplore.ieee.org/document/782170
- **Abstract**: If a linear block code C of length n has a Tanner graph without cycles, then maximum-likelihood soft-decision decoding of C can be achieved in time O(n/sup 2/). However, we show that cycle-free Tanner graphs cannot support good codes. Specifically, let C be an (n,k,d) linear code of rate R=k/n that can be represented by a Tanner graph without cycles. We prove that if R/spl ges/0.5 then d/spl les/2, while if R<0.5 then C is obtained from a code of rate /spl ges/0.5 and distance /spl les/2 by simply repeating certain symbols. In the latter case, we prove that d/spl les/[n/k+1]+[n+1/k+1]<2/R. Furthermore, we show by means of an explicit construction that this bound is tight for all values of n and k. We also prove that binary codes which have cycle-free Tanner graphs belong to the class of graph-theoretic codes, known as cut-set codes of a graph. Finally, we discuss the asymptotics for Tanner graphs with cycles, and present a number of open problems for future research.

## High-speed indoor wireless communications at 60 GHz with coded OFDM

- **Status**: ❌
- **Reason**: 60GHz 실내 무선 coded OFDM 시스템, 블록코딩 부수 언급 — 무선 응용 특이적, 떼어낼 LDPC 기법 없음
- **ID**: ieee:803506
- **Type**: journal
- **Published**: 1999
- **Authors**: D. Dardari, V. Tralli
- **PDF**: https://ieeexplore.ieee.org/document/803506
- **Abstract**: A high-speed indoor wireless communication system using coded orthogonal frequency-division multiplexing (OFDM) and working at 60 GHz is proposed and analyzed. An actual propagation environment consisting of a medium sized research laboratory, characterized by means of a ray-tracing technique, is considered for the analysis. In this contest the paper investigates and discusses the effects of frequency diversity, antenna sectorization, OFDM clustering, and different block coding strategies. Moreover, to characterize the communication between stationary indoor terminals at millimeter waves, a new definition of coverage is introduced. In order to evaluate the performance of the coded system in the actual environment, a suitable semianalytical algorithm is defined and applied. In the results the feasibility of a coded OFDM system for 155 Mbit/s packet transmission is checked. It is shown that all the line-of-sight (LOS) positions and 70% of the no LOS points can be covered in the scenario considered with a transmitted power of 10 dBm.

## Symbol-based turbo codes

- **Status**: ❌
- **Reason**: 심볼기반 터보부호 + 변조, 비-LDPC 부호이고 LDPC BP에 이식할 부호비의존 디코더 기여 없음
- **ID**: ieee:798019
- **Type**: journal
- **Published**: 1999
- **Authors**: M. Bingeman, A. K. Khandani
- **PDF**: https://ieeexplore.ieee.org/document/798019
- **Abstract**: We present a new turbo-coding method which parses the input block into n-bit symbols and interleaves on a symbol-by-symbol basis. This is used in conjunction with different modulation techniques to take advantage of tradeoffs between bit error rate performance, code-rate, spectral efficiency, and decoder complexity. The structure of the encoder and decoder of these codes, which We call symbol-based turbo codes, are outlined. The bit error rate performance of a few specific codes are examined. A discussion on decoder complexity is also included. Symbol-based turbo codes are good candidates for low delay transmission of speech and data in spread spectrum communication systems.

## Reduced complexity iterative decoding of low-density parity check codes based on belief propagation

- **Status**: ✅
- **Reason**: Two simplified BP variants (real additions only, channel-independent, quantization-friendly HW) for binary LDPC -> directly transferable min-sum/BP decoder for NAND (C/D).
- **ID**: ieee:768759
- **Type**: journal
- **Published**: 1999
- **Authors**: M. P. C. Fossorier, M. Mihaljevic, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/768759
- **Abstract**: Two simplified versions of the belief propagation algorithm for fast iterative decoding of low-density parity check codes on the additive white Gaussian noise channel are proposed. Both versions are implemented with real additions only, which greatly simplifies the decoding complexity of belief propagation in which products of probabilities have to be computed. Also, these two algorithms do not require any knowledge about the channel characteristics. Both algorithms yield a good performance-complexity trade-off and can be efficiently implemented in software as well as in hardware, with possibly quantized received values.

## Comparison of constructions of irregular Gallager codes

- **Status**: ✅
- **Reason**: 불규칙 Gallager(LDPC) 그래프 구성법 비교 + 고속 인코딩 구성 → 바이너리 LDPC 코드 설계 기법(E), 이식 가능
- **ID**: ieee:795809
- **Type**: journal
- **Published**: 1999
- **Authors**: D. J. C. MacKay, S. T. Wilson, M. C. Davey
- **PDF**: https://ieeexplore.ieee.org/document/795809
- **Abstract**: The low-density parity check codes whose performance is closest to the Shannon limit are "Gallager codes" based on irregular graphs. We compare alternative methods for constructing these graphs and present two results. First, we find a "super-Poisson" construction which gives a small improvement in empirical performance over a random construction. Second, whereas Gallager codes normally take N/sup 2/ time to encode, we investigate constructions of regular and irregular Gallager codes that allow more rapid encoding and have smaller memory requirements in the encoder. We find that these "fast encoding" Gallager codes have equally good performance.

## Type IV self-dual codes over rings

- **Status**: ❌
- **Reason**: Z/4·F2+uF2 환 위 Type IV self-dual 부호 분류, LDPC 아닌 대수부호 이론 — 떼어낼 디코더/HW 없음
- **ID**: ieee:796375
- **Type**: journal
- **Published**: 1999
- **Authors**: S. T. Dougherty, P. Gaborit, M. Harada +2
- **PDF**: https://ieeexplore.ieee.org/document/796375
- **Abstract**: We study Type IV self-dual codes over the commutative rings of order 4. Gleason-type theorems of Type IV codes and their shadow codes are investigated. A mass formula of Type IV codes over these rings are given. We give a classification of Type TV codes over Z/sub 4/ and F2+uF/sub 2/ for reasonable lengths. We also construct a number of optimal Type TV codes.

## Throughput analysis of the go-back-N protocol in fading radio channels

- **Status**: ❌
- **Reason**: Go-back-N ARQ throughput analysis in fading channels; no LDPC or transferable ECC technique.
- **ID**: ieee:768202
- **Type**: journal
- **Published**: 1999
- **Authors**: W. Turin
- **PDF**: https://ieeexplore.ieee.org/document/768202
- **Abstract**: We derive a formula for calculating the throughput efficiency of the go-back-N (GBN) protocol when error sources in the forward and backward channels are modeled by a hidden Markov model. The result is presented in the matrix form which makes it applicable to models with any number of states. We consider also the relationship between bit-level and block-level models and obtain the probability distribution of the time that a message spends in the system.

## Constrained coding techniques for soft iterative decoders

- **Status**: ❌
- **Reason**: 기록채널 변조제약 + BCJR 기반 soft 디코딩 연접 기법 — 변조제약 SISO 특이적, LDPC ECC로 떼어낼 일반 디코더 기법 없음
- **ID**: ieee:830157
- **Type**: conference
- **Published**: 1999
- **Authors**: J. L. Fan, J. M. Cioffi
- **PDF**: https://ieeexplore.ieee.org/document/830157
- **Abstract**: Soft iterative decoding of turbo codes and low-density parity check codes has been shown to offer significant improvements in performance. To apply soft iterative decoding to digital recorders, where binary modulation constraints are often used, modifications must be made to allow reliability information to be accessible by the decoder. A solution is proposed which uses a modified concatenation scheme, in which the positions of the modulation and error-correcting codes are reversed. In addition, a soft decoder based on the BCJR algorithm is introduced for the modulation constraint, and improved performance is obtained by iterating with this soft constraint decoder.

## On bootstrap iterative Viterbi algorithm

- **Status**: ❌
- **Reason**: 부트스트랩 반복 Viterbi 알고리즘 — 비-LDPC, 이식 가능 LDPC 기법 없음
- **ID**: ieee:765492
- **Type**: conference
- **Published**: 1999
- **Authors**: Lei Wei
- **PDF**: https://ieeexplore.ieee.org/document/765492
- **Abstract**: A bootstrap iterative Viterbi algorithm (BIVA) is proposed based on a bootstrap structure. Two different modifications are then considered for both very short size blocks (say 100-250 bits) and the medium size blocks (1000-3000 bits). It shows that the iterative decoding can be achieved by using the conventional Viterbi algorithm, which does not require the noise variance estimation. The numerical results show the significant performance improvement over the standard Viterbi algorithm is possible. For a block length of 1500 bits and with a 32 state VA, the 2D BIVA can achieve a bit error rate of 2/spl times/10/sup -5/ at an E/sub b//E/sub 0/ of 2.3 dB away from the Shannon limit. For both information block lengths of 1944 and 11970 bits, in term of its performance respect to the Shannon limit and the Shannon sphere packing bound, the 2D-BIVA is about 0.2-0.3 dB worse than the best known rate 1/2 JPL turbo codes of similar information block sizes. With some simple modifications, most of current systems (where the Viterbi algorithms used) can benefit significantly from this iterative decoding procedure.

## Fault-tolerant linear finite state machines

- **Status**: ❌
- **Reason**: 선형 유한상태기계 결함내성, 선형부호+동적시스템 — LDPC 아닌 신뢰성 HW 프레임워크, 이식 디코더/구성 없음
- **ID**: ieee:813422
- **Type**: conference
- **Published**: 1999
- **Authors**: C. N. Hadjicostis, G. C. Verghese
- **PDF**: https://ieeexplore.ieee.org/document/813422
- **Abstract**: In this paper we develop a framework for constructing fault-tolerant dynamic systems, focusing primarily on linear finite state machines (LFSMs). Modular redundancy, the traditional approach to fault tolerance, is expensive because of the overhead in replicating the hardware and its reliance on the assumption that the error-correcting (voting) mechanism is fault-free. Our approach is more general, makes efficient use of redundancy, and relaxes the strict requirements regarding the reliability of the error corrector. By combining linear coding techniques and dynamic system theory, we characterize the class of all appropriate redundant implementations. Furthermore, we construct reliable LFSM's assembled exclusively from unreliable components, including unreliable voters and parity checkers in the error correcting mechanism. Using constant redundancy per system, we obtain implementations of identical LFSM's that operate in parallel on distinct input sequences and achieve arbitrarily low probability of failure during any specified finite time interval.

## On lowest density MDS codes

- **Status**: ❌
- **Reason**: GF(q) 저밀도 MDS 부호 — 비이진, LDPC BP 아님
- **ID**: ieee:746771
- **Type**: journal
- **Published**: 1999
- **Authors**: M. Blaum, R. M. Roth
- **PDF**: https://ieeexplore.ieee.org/document/746771
- **Abstract**: Let F/sub q/ denote the finite field GF(q) and let h be a positive integer. MDS (maximum distance separable) codes over the symbol alphabet F/sub q//sup b/ are considered that are linear over F/sub q/ and have sparse ("low-density") parity-check and generator matrices over F/sub q/ that are systematic over F/sub q//sup b/. Lower bounds are presented on the number of nonzero elements in any systematic parity-check or generator matrix of an F/sub q/-linear MDS code over F/sub q//sup b/, along with upper bounds on the length of any MDS code that attains those lower bounds. A construction is presented that achieves those bounds for certain redundancy values. The building block of the construction is a set of sparse nonsingular matrices over F/sub q/ whose pairwise differences are also nonsingular. Bounds and constructions are presented also for the case where the systematic condition on the parity-check and generator matrices is relaxed to be over F/sub q/, rather than over F/sub q//sup b/.

## Low-density MDS codes and factors of complete graphs

- **Status**: ❌
- **Reason**: Low-density MDS array codes (B-Code) for erasure/error with graph-theory construction; not binary LDPC BP, no transferable iterative decoder/HW for NAND LDPC.
- **ID**: ieee:782102
- **Type**: journal
- **Published**: 1999
- **Authors**: Lihao Xu, V. Bohossian, J. Bruck +1
- **PDF**: https://ieeexplore.ieee.org/document/782102
- **Abstract**: We present a class of array code of size n/spl times/l, where l=2n or 2n+1, called B-Code. The distances of the B-Code and its dual are 3 and l-1, respectively. The B-Code and its dual are optimal in the sense that i) they are maximum-distance separable (MDS), ii) they have an optimal encoding property, i.e., the number of the parity bits that are affected by change of a single information bit is minimal, and iii) they have optimal length. Using a new graph description of the codes, we prove an equivalence relation between the construction of the B-Code (or its dual) and a combinatorial problem known as perfect one-factorization of complete graphs, thus obtaining constructions of two families of the B-Code and its dual, one of which is new. Efficient decoding algorithms are also given, both for erasure correcting and for error correcting. The existence of perfect one-factorizations for every complete graph with an even number of nodes is a 35 years long conjecture in graph theory. The construction of B-Codes of arbitrary odd length will provide an affirmative answer to the conjecture.
