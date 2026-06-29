# IEEE Xplore — 2016-02


## Finite-Length Algebraic Spatially-Coupled Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: SC-QC-LDPC R&M 구성(코드설계 E)—nonbinary 시연이나 R&M이 matrix unwrapping 일반화라 바이너리 이식 여지, Phase3 재검토
- **ID**: ieee:7347352
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Keke Liu, Mostafa El-Khamy, Jungwon Lee
- **PDF**: https://ieeexplore.ieee.org/document/7347352
- **Abstract**: The replicate-and-mask (R&M) construction of finite-length spatially-coupled (SC) LDPC codes is proposed in this paper. The proposed R&M construction generalizes the conventional matrix unwrapping construction and contains it as a special case. The R&M construction of a class of algebraic spatially coupled (SC) quasi-cyclic (QC) LDPC codes over arbitrary finite fields is demonstrated. The girth, rank, and time-varying periodicity of the proposed R&M SC QC LDPC codes are analyzed. The error rate performance of finite-length nonbinary algebraic SC QC LDPC codes is investigated with window decoding. Compared to the conventional unwrapping construction, it is found through numerical simulations that the R&M construction resulted in SC QC LDPC codes with better block error rate performance and lower error floors. With a flooding schedule decoder, it is shown that the proposed R&M algebraic SC QC LDPC codes have better error performance than the corresponding LDPC block codes and random SC codes. The R&M construction of irregular SC QC LDPC codes is demonstrated. It is shown that low-complexity regular puncturing schemes can be deployed on these codes to construct families of rate-compatible irregular SC QC LDPC codes with good performance.

## On the Total Power Capacity of Regular-LDPC Codes With Iterative Message-Passing Decoders

- **Status**: ❌
- **Reason**: 정규 LDPC의 총전력 스케일링 이론 bound(node/wire 모델); 새 디코더·구성·HW 없이 순수 이론 한계
- **ID**: ieee:7339416
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Karthik Ganesan, Pulkit Grover, Jan Rabaey +1
- **PDF**: https://ieeexplore.ieee.org/document/7339416
- **Abstract**: Motivated by recently derived fundamental limits on total (transmit + decoding) power for coded communication with VLSI decoders, this paper investigates the scaling behavior of the minimum total power needed to communicate over AWGN channels as the target bit-error-probability tends to zero. We focus on regular-LDPC codes and iterative message-passing decoders. We analyze scaling behavior under two VLSI complexity models of decoding. One model abstracts power consumed in processing elements (node model), and another abstracts power consumed in wires which connect the processing elements (wire model). We prove that a coding strategy using regular-LDPC codes with Gallager-B decoding achieves order-optimal scaling of total power under the node model. However, we also prove that regular-LDPC codes and iterative message-passing decoders cannot meet existing fundamental limits on total power under the wire model. Furthermore, if the transmit energy-per-bit is bounded, total power grows at a rate that is worse than uncoded transmission. Complementing our theoretical results, we develop detailed physical models of decoding implementations using post-layout circuit simulations. Our theoretical and numerical results show that approaching fundamental limits on total power requires increasing the complexity of both the code design and the corresponding decoding algorithm as communication distance is increased or error-probability is lowered.

## Randomly Punctured LDPC Codes

- **Status**: ✅
- **Reason**: 랜덤 펑처링 LDPC 부호 앙상블 BP 임계값 분석+protograph/SC-LDPC 구성 - 바이너리 LDPC 코드설계(E) 이식 가능
- **ID**: ieee:7353121
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: David G. M. Mitchell, Michael Lentmaier, Ali E. Pusane +1
- **PDF**: https://ieeexplore.ieee.org/document/7353121
- **Abstract**: In this paper, we present a random puncturing analysis of low-density parity-check (LDPC) code ensembles. We derive a simple analytic expression for the iterative belief propagation (BP) decoding threshold of a randomly punctured LDPC code ensemble on the binary erasure channel (BEC) and show that, with respect to the BP threshold, the strength and suitability of an LDPC code ensemble for random puncturing is completely determined by a single constant that depends only on the rate and the BP threshold of the mother code ensemble. We then provide an efficient way to accurately predict BP thresholds of randomly punctured LDPC code ensembles on the binary-input additive white Gaussian noise channel (BI-AWGNC), given only the BP threshold of the mother code ensemble on the BEC and the design rate, and we show how the prediction can be improved with knowledge of the BI-AWGNC threshold. We also perform an asymptotic minimum distance analysis of randomly punctured code ensembles and present simulation results that confirm the robust decoding performance promised by the asymptotic results. Protograph-based LDPC block code and spatially coupled LDPC code ensembles are used throughout as examples to demonstrate the results.

## Two Enhanced Reliability-Based Decoding Algorithms for Nonbinary LDPC Codes

- **Status**: ❌
- **Reason**: 비이진(nonbinary) LDPC 신뢰도기반 디코딩 - 비이진 LDPC는 명시적 제외
- **ID**: ieee:7366559
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Liyuan Song, Qin Huang, Zulin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7366559
- **Abstract**: The weighted bit-reliability-based (wBRB) algorithm for nonbinary LDPC codes suffers certain loss of symbol-reliability. Thus, this paper enhances its soft-decision version by passing multiple symbol-reliability instead of bit-reliability. Furthermore, it demonstrates that plurality robustly indicates symbol-reliability of extrinsic information-sums. Thus, this paper enhances the hard-decision version by introducing symbol-reliability from plurality. Analysis results show that these two enhanced decoding algorithms significantly outperform the wBRB algorithm with reasonable overhead.

## Protograph-Based LDPC Code Design for Shaped Bit-Metric Decoding

- **Status**: ✅
- **Reason**: 프로토그래프 기반 LDPC 코드설계(노드차수+BICM 매핑 공동최적화); 바이너리 LDPC 구성 기법 이식 가능(E)
- **ID**: ieee:7339431
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Fabian Steiner, Georg Böcherer, Gianluigi Liva
- **PDF**: https://ieeexplore.ieee.org/document/7339431
- **Abstract**: A protograph-based low-density parity-check (LDPC) code design technique for bandwidth-efficient coded modulation with probabilistic shaping is presented. The approach jointly optimizes the LDPC code node degrees and the mapping of the coded bits to the bit-interleaved coded modulation (BICM) bit-channels. For BICM with uniform inputs and for BICM with probabilistic shaping, binary-input symmetric-output surrogate channels for the code design are used. The constructed codes for uniform inputs perform as good as the multi-edge type codes of Zhang and Kschischang (2013). For 8-ASK and 64-ASK with probabilistic shaping, codes of rates 2/3 and 5/6 with blocklength 64800 are designed, which operate within 0.63 and 0.69 dB of $\frac{1}{2}\,\log_2(1+\text{SNR})$ for a target frame error rate of $10^{-3}$ at spectral efficiencies of 1.38 and 4.25 bits/channel use, respectively.

## Message Passing-Based Decoding of Convolutional Codes: Performance and Complexity Analysis

- **Status**: ✅
- **Reason**: 컨볼루션 부호에 메시지패싱 디코딩 적용 - 부호 비의존적 메시지패싱 복잡도 절감 기법, 바이너리 LDPC BP에 이식 가능성(C, 애매하여 살림)
- **ID**: ieee:7355317
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Hossein Mani, Hamid Saeedi
- **PDF**: https://ieeexplore.ieee.org/document/7355317
- **Abstract**: In this letter, we propose to apply message passing algorithms to decode standard convolutional codes and assess the resulting performance and the required complexity compared to conventional decoding algorithms for convolutional codes by concentrating on the Viterbi algorithm (VA). We show that, in contrast to the VA for which the decoding complexity increases exponentially with $m$, the number of memory blocks for the proposed framework, such an increase, is only linear in $m$. This suggests that applying message passing algorithms can provide considerable savings in the required computational power if it can also exhibit a comparable bit-error-rate performance to that of the VA. In this letter, we show via simulations that this is in fact the case for convolutional codes.

## On the Waterfall Performance of Finite-Length SC-LDPC Codes Constructed From Protographs

- **Status**: ✅
- **Reason**: 프로토그래프 기반 SC-LDPC 유한길이 워터폴 스케일링 분석·구조 비교(카테고리 E, 바이너리 LDPC 코드설계)
- **ID**: ieee:7339427
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Markus Stinner, Pablo M. Olmos
- **PDF**: https://ieeexplore.ieee.org/document/7339427
- **Abstract**: An analysis of spatially coupled low-density parity-check (SC-LDPC) codes constructed from protographs is proposed. Given the protograph used to generate the SC-LDPC code ensemble, a set of scaling parameters to characterize the average finite-length performance in the waterfall region is computed. The error performance of structured SC-LDPC code ensembles is shown to follow a scaling law similar to that of unstructured randomly constructed SC-LDPC codes. Under a finite-length perspective, some of the most relevant SC-LDPC protograph structures proposed to date are compared. The analysis reveals significant differences in their finite-length scaling behavior, which is corroborated by simulation. Spatially coupled repeat-accumulate codes present excellent finite-length performance, as they outperform in the waterfall region SC-LDPC codes of the same rate and better asymptotic thresholds.

## On Progressive Edge-Growth Interleavers for Turbo Codes

- **Status**: ❌
- **Reason**: PEG는 표준 LDPC 기법인데 여기선 turbo 인터리버 최소거리에만 적용, 신규 LDPC 기여 없음
- **ID**: ieee:7339667
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Ghassan M. Kraidy
- **PDF**: https://ieeexplore.ieee.org/document/7339667
- **Abstract**: In this letter, we show that the family of progressive edge growth interleavers ensures optimal growth of the minimum distance of turbo codes, which grows as log(N), where N is the interleaver size. This family of interleavers fits well the self-concatenated structure of turbo codes, hence it works with irregular turbo codes as well. We will start by introducing the self-concatenated structure of turbo codes. We then recall the progressive edge-growth interleaver construction, and we show that the minimum distance grows optimally with such interleavers. We end up by showing simulation comparisons with other families of interleavers.

## Multi-CRC Polar Codes and Their Applications

- **Status**: ❌
- **Reason**: Polar 부호 SCL 디코딩+CRC 메모리/지연 절감 - polar 전용 기법, 바이너리 LDPC BP 이식성 없음(비-LDPC 제외)
- **ID**: ieee:7353162
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Jianfeng Guo, Zhiping Shi, Zilong Liu +2
- **PDF**: https://ieeexplore.ieee.org/document/7353162
- **Abstract**: Polar codes under successive cancelation list (SCL) decoding are capable of achieving almost the same or better performance than turbo codes or low density parity-check codes with the help of single cyclic redundancy check (CRC). This decoding scheme, however, suffers from very high complexity with long delay and large memory space. Motivated by this research problem, we propose a novel coding scheme called multi-CRC polar code for significant reduction of memory size and decoding delay but with negligible performance loss. Our analysis and simulation have shown that about half reduction of memory size and decoding delay can be achieved in SCL decoding. We also apply this scheme to hybrid automatic repeat request (HARQ) system to aid retransmission and show that the throughput of multi-CRC polar code is higher than that of the single-CRC one.

## Fast List Decoders for Polar Codes

- **Status**: ❌
- **Reason**: Polar list 디코더 SW 고속화, 폴라 전용이라 LDPC 비이식
- **ID**: ieee:7339671
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Gabi Sarkis, Pascal Giard, Alexander Vardy +2
- **PDF**: https://ieeexplore.ieee.org/document/7339671
- **Abstract**: Polar codes asymptotically achieve the symmetric capacity of memoryless channels, yet their error-correcting performance under successive-cancellation (SC) decoding for short and moderate length codes is worse than that of other modern codes such as low-density parity-check (LDPC) codes. Of the many methods to improve the error-correction performance of polar codes, list decoding yields the best results, especially when the polar code is concatenated with a cyclic redundancy check (CRC). List decoding involves exploring several decoding paths with SC decoding, and therefore tends to be slower than SC decoding itself, by an order of magnitude in practical implementations. In this paper, we present a new algorithm based on unrolling the decoding tree of the code that improves the speed of list decoding by an order of magnitude when implemented in software. Furthermore, we show that for software-defined radio applications, our proposed algorithm is faster than the fastest software implementations of LDPC decoders in the literature while offering comparable error-correction performance at similar or shorter code lengths.

## Practical Dirty Paper Coding With Sum Codes

- **Status**: ❌
- **Reason**: Dirty paper coding sum codes(선형블록부호), LDPC 아님·이식 기법 없음
- **ID**: ieee:7350223
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Kiran M. Rege, Krishna Balachandran, Joseph H. Kang +1
- **PDF**: https://ieeexplore.ieee.org/document/7350223
- **Abstract**: In this paper, we present a practical method to construct dirty paper coding (DPC) schemes using sum codes. Unlike the commonly used approach to DPC where the coding scheme involves concatenation of a channel code and a quantization code, the proposed method embodies a unified approach that emulates the binning method used in the proof of the DPC result. Auxiliary bits are used to create the desired number of code vectors in each bin. Sum codes are obtained when information sequences augmented with auxiliary bits are encoded using linear block codes. Sum-code-based DPC schemes can be implemented using any linear block code, and entail a relatively small increase in decoder complexity when compared to standard communication schemes. They can also lead to significant reduction in transmit power in comparison to standard schemes.

## Practical Design and Decoding of Parallel Concatenated Structure for Systematic Polar Codes

- **Status**: ❌
- **Reason**: polar+convolutional 연접 부호의 가중 반복 디코딩; polar/RSC 특이적이고 LDPC BP로 이식할 부호 비의존 기법 없음
- **ID**: ieee:7332771
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Qingshuang Zhang, Aijun Liu, Yingxian Zhang +1
- **PDF**: https://ieeexplore.ieee.org/document/7332771
- **Abstract**: In this paper, a parallel concatenated structure is proposed to improve the performance of polar codes in finite length in which multiblocks systematic polar codes (SPC) and recursive systematic convolutional codes (RSC) are combined. We first design a weighted iterative decoding algorithm for the proposed structure such that better bit error rate performance can be obtained. Then, a deliberated interleaver is optimized for the new scheme. Thereafter, we introduce a strategy to estimate the minimum distance of the concatenation codeword, where an asymptotic performance and convergence behavior analysis are elaborated. Finally, the error performance of the proposed scheme is evaluated via simulations. The results show that our scheme almost outperforms all the existed concatenation ones using polar codes, making the codes more practical.

## Distance Spectrum of Fixed-Rate Raptor Codes With Linear Random Precoders

- **Status**: ❌
- **Reason**: Raptor/LT fountain 부호의 거리스펙트럼 이론; erasure fountain이라 떼어낼 LDPC ECC 기법 없음
- **ID**: ieee:7339429
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Francisco Lázaro, Enrico Paolini, Gianluigi Liva +1
- **PDF**: https://ieeexplore.ieee.org/document/7339429
- **Abstract**: Raptor code ensembles with linear random outer codes in a fixed-rate setting are considered. An expression for the average distance spectrum is derived and this expression is used to obtain the asymptotic exponent of the weight distribution. The asymptotic growth rate analysis is then exploited to develop a necessary and sufficient condition under which the fixed-rate Raptor code ensemble exhibits a strictly positive typical minimum distance. The condition involves the rate of the outer code, the rate of the inner fixed-rate Luby Transform (LT) code and the LT code degree distribution. Additionally, it is shown that for ensembles fulfilling this condition, the minimum distance of a code randomly drawn from the ensemble has a linear growth with the block length. The analytical results can be used to make accurate predictions of the performance of finite length Raptor codes. These results are particularly useful for fixed-rate Raptor codes under maximum likelihood erasure decoding, whose performance is driven by their weight distribution.

## Performance Analysis of Block Markov Superposition Transmission of Short Codes

- **Status**: ❌
- **Reason**: BMST(생성행렬 결합 SC 코드) 단축코드 성능분석; SC-LDPC는 비교 대상일 뿐 떼어낼 LDPC 설계 기여 아님
- **ID**: ieee:7339426
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Kechao Huang, Xiao Ma
- **PDF**: https://ieeexplore.ieee.org/document/7339426
- **Abstract**: In this paper, we consider the asymptotic and finite-length performance of block Markov superposition transmission (BMST) of short codes, which can be viewed as a new class of spatially coupled (SC) codes where the generator matrices of short codes (referred to as basic codes) are coupled. A modified extrinsic information transfer (EXIT) chart analysis that takes into account the relation between mutual information (MI) and bit-error-rate (BER) is presented to study the convergence behavior of BMST codes. Using the modified EXIT chart analysis, we investigate the impact of various parameters on BMST code performance, thereby providing theoretical guidance for designing and implementing practical BMST codes suitable for window decoding. Then, we present a performance comparison of BMST codes and SC low-density parity-check (SC-LDPC) codes on the basis of equal decoding latency. Also presented is a comparison of computational complexity. Simulation results show that, under the equal decoding latency constraint, BMST codes using the repetition code as the basic code can outperform both (3,6)-regular SC-LDPC codes and (4,8)-regular SC-LDPC codes in the waterfall region but have a higher computational complexity.

## On the Complexity of the Rank Syndrome Decoding Problem

- **Status**: ❌
- **Reason**: Rank syndrome decoding 암호공격 복잡도 - 코드기반 암호/이론, 디코더·HW·구성 이식성 없음
- **ID**: ieee:7364245
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Philippe Gaborit, Olivier Ruatta, Julien Schrek
- **PDF**: https://ieeexplore.ieee.org/document/7364245
- **Abstract**: In this paper, we propose two new generic attacks on the rank syndrome decoding (RSD) problem. Let C be a random [n, k] rank code over GF(qm) and let y = x + e be a received word, such that x ∈ C and rank(e) = r. The first attack, the support attack, is combinatorial and permits to recover an error e of rank weight r in min(O((n - k)3m3qr1(km/n)J, O((n - k)3m3q⌈(r-1)I(((k+1)m)/n)J))⌉ operations on GF(q). This new attack improves the exponent for the best generic attack for the RSD problem in the case n > m, by introducing the ratio m/n in the exponential coefficient of the previously best known attacks. The second attack, the annulator polynomial attack, is an algebraic attack based on the theory of q-polynomials introduced by Ore. We propose a new algebraic setting for the RSD problem that permits to consider equations and unknowns in the extension field GF(qm) rather than in GF(q) as it is usually the case. We consider two approaches to solve the problem in this new setting. The linearization technique shows that if n ≥ (k + 1) (r + 1) - 1 the RSD problem can be solved in polynomial time. More generally, we prove that if [(((r + 1)(k + 1)- (n + 1))/r)1 ≤ k, the RSD problem can be solved with an average complexity of O(r3k3qrΓ(((r+1)(k+1)-(n+1))/r)l)⌉ operations in the base field GF(q). We also consider solving with Gröbner bases for which we discuss theoretical complexity, we also consider hybrid solving with Gröbner bases on practical parameters. As an example of application, we use our new attacks on all recent cryptosystems parameters, which repair the GPT cryptosystem, we break all examples of published proposed parameters, and some parameters are broken in less than 1 s in certain cases.

## Reduce the Complexity of List Decoding of Polar Codes by Tree-Pruning

- **Status**: ❌
- **Reason**: Polar CA-SCL 트리프루닝, 폴라 path metric 기반이라 LDPC 비이식
- **ID**: ieee:7348682
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Kai Chen, Bin Li, Hui Shen +2
- **PDF**: https://ieeexplore.ieee.org/document/7348682
- **Abstract**: Polar codes under cyclic redundancy check-aided successive cancellation list (CA-SCL) decoding can outperform the turbo codes and the LDPC codes when code lengths are configured to be several kilobits. In order to reduce the decoding complexity, a novel tree-pruning scheme for the SCL/CA-SCL decoding algorithms is proposed in this letter. In each step of the decoding procedure, the candidate paths with metrics less than a threshold are dropped directly to avoid the unnecessary computations for the path searching on the descendant branches of them. Given a candidate path, an upper bound of the path metric of its descendants is proposed to determined how much pruning this candidate path would affect frame error rate (FER) performance. By utilizing this upper bounding technique and introducing a dynamic threshold, the proposed scheme deletes as many as possible of the redundant candidate paths while keeping the performance deterioration in a tolerant region, thus it is much more efficient than the existing pruning scheme. With only a negligible loss of FER performance, the computational complexity of the proposed pruned decoding scheme is only about 40% of the standard algorithm in the low signal-to-noise ratio (SNR) region (where the FER under CA-SCL decoding is about $0.1 \sim 0.001$), and it can be very close to that of the successive cancellation (SC) decoder in the moderate- and high-SNR regions.

## Polar Subcodes

- **Status**: ❌
- **Reason**: polar subcodes(dynamic frozen) 부호 구성+SC 디코딩; polar 특이적이라 LDPC BP 이식 기법 없음
- **ID**: ieee:7339451
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Peter Trifonov, Vera Miloslavskaya
- **PDF**: https://ieeexplore.ieee.org/document/7339451
- **Abstract**: An extension of polar codes is proposed, which allows some of the frozen symbols, called dynamic frozen symbols, to be data-dependent. A construction of polar codes with dynamic frozen symbols, being subcodes of extended BCH codes, is proposed. The proposed codes have higher minimum distance than classical polar codes, but still can be efficiently decoded using the successive cancellation algorithm and its extensions. The codes with Arikan, extended BCH and Reed-Solomon kernel are considered. The proposed codes are shown to outperform LDPC and turbo codes, as well as polar codes with CRC.

## A MAP Decoder for TVB Codes on a Generalized Iyengar–Siegel–Wolf BPMR Markov Channel Model

- **Status**: ❌
- **Reason**: TVB 코드 MAP 디코더와 BPMR Markov 채널 모델 특이적; LDPC는 연접 베이스라인일 뿐 떼어낼 바이너리 LDPC 기법 없음
- **ID**: ieee:7294692
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Johann A. Briffa, Victor Buttigieg
- **PDF**: https://ieeexplore.ieee.org/document/7294692
- **Abstract**: We present a generalization of the Iyengar-Siegel-Wolf Markov channel model for bit-patterned media recording media to allow negative drift, and adapt the maximum a posteriori decoder for time-varying block codes to work on this generalized model while minimizing complexity. We also describe a method for designing near-optimal codes for this channel using simulated annealing, obtaining better performance than alternative designs. In concatenation with a (999, 888)16 low-density parity-check (LDPC) code, we achieve a frame error rate (FER) of 10-3 at a channel error rate that is 1.73× higher than the best result with existing designs. A simple extension to include substitution errors allows the channel to approximate the dependent insertion, deletion, and substitution (DIDS) channel, with a decoding complexity that is 10× lower than that of Wu and Armand's RC2 decoder. The performance in the absence of burst errors is almost identical. When the DIDS channel includes burst substitution errors, our decoder performs worse than the RC2 decoder, but maintains its complexity advantage. For the same concatenated code, our decoder achieves an FER of 10-3 at a channel error rate that is 1.68× lower than the RC2 decoder. Finally, simulation results show that our code designs improve on existing constructions for the DIDS channel.

## Interleaved Concatenations of Polar Codes With BCH and Convolutional Codes

- **Status**: ❌
- **Reason**: BCH/convolutional+polar 연접 부호의 soft-output 다단 반복 디코딩; polar/BCH 특이적, LDPC 비의존 이식 기법 없음
- **ID**: ieee:7339653
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Ying Wang, Krishna R. Narayanan, Yu-Chih Huang
- **PDF**: https://ieeexplore.ieee.org/document/7339653
- **Abstract**: We analyze interleaved concatenation schemes of polar codes with outer binary BCH codes and convolutional codes. We show that both BCH-polar and Conv-polar codes can have a frame error rate that decays exponentially with the code length for all rates up to capacity, which is a substantial improvement in the error exponent over stand-alone polar codes. Interleaved concatenation with long constraint length convolutional codes is an effective way to leverage the fact that polarization increases the cutoff rate of the channel. Simulation results show that Conv-polar codes when decoded with the proposed soft-output multistage iterative decoding algorithm can outperform stand-alone polar codes decoded with successive cancellation or belief propagation decoding. It may be comparable to stand-alone polar codes with list decoding in the high SNR regime. In addition to this, we show that the proposed concatenation scheme requires lower memory and decoding complexity in comparison to belief propagation and list decoding of polar codes. Practically, the scheme enables rate compatible outer codes which ease hardware implementation. Our results suggest that the proposed method may strike a better balance between performance and complexity compared to existing methods in the finite-length regime.

## A Split-Reduced Successive Cancellation List Decoder for Polar Codes

- **Status**: ❌
- **Reason**: Polar SCL 분할 규칙, 폴라 전용 path-pruning이라 LDPC BP 비이식
- **ID**: ieee:7339660
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Zhaoyang Zhang, Liang Zhang, Xianbin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7339660
- **Abstract**: This paper focuses on low complexity successive cancellation list (SCL) decoding of polar codes. In particular, using the fact that splitting may be unnecessary when the reliability of decoding the unfrozen bit is sufficiently high, a novel splitting rule is proposed. Based on this rule, it is conjectured that, if the correct path survives at some stage, it tends to survive till termination without splitting with high probability. On the other hand, the incorrect paths are more likely to split at the following stages. Motivated by these observations, a simple counter that counts the successive number of stages without splitting is introduced for each decoding path to facilitate the identification of correct and incorrect paths. Specifically, any path with counter value larger than a predefined threshold ω is deemed to be the correct path, which will survive at the decoding stage, while other paths with counter value smaller than the threshold will be pruned, thereby reducing the decoding complexity. Furthermore, it is proved that there exists a unique unfrozen bit uN-K1+1, after which the successive cancellation decoder achieves the same error performance as the maximum likelihood decoder if all the prior unfrozen bits are correctly decoded, which enables further complexity reduction. Simulation results demonstrate that the proposed low complexity SCL decoder attains performance similar to that of the conventional SCL decoder, while achieving substantial complexity reduction.

## Low Complexity Iterative MMSE-PIC Detection for Medium-Size Massive MIMO

- **Status**: ❌
- **Reason**: Massive MIMO MMSE-PIC 검출기, LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:7339655
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Licai Fang, Lu Xu, Defeng David Huang
- **PDF**: https://ieeexplore.ieee.org/document/7339655
- **Abstract**: In medium-size massive MIMO systems, the minimum mean-square-error parallel interference cancellation (MMSE-PIC)-based soft-input soft-output (SISO) detector is often used due to its relatively low complexity and good bit error rate (BER) performance. The computational complexity of MMSE-PIC for detecting a block of data is dominated by the computation of a Gram matrix and a matrix inversion. They have computational complexity of O(K2M) and O(K3), respectively, where K is the number of uplink users with one transmit antenna each and M is the number of receive antennas at the base station. In this letter, by using an L (typically L ≤ 3) terms of Neumann series expansion to approximate the matrix inversion, we reduce the total computational complexity to O(LK M). Compared with alternative algorithms, which focus on reducing the complexity of the matrix inversion only, the proposed method can also avoid calculating the Gram matrix explicitly and thus significantly reducing the total complexity.

## A Low-Latency List Successive-Cancellation Decoding Implementation for Polar Codes

- **Status**: ❌
- **Reason**: Polar 코드 전용 LSCD VLSI, 바이너리 LDPC BP에 이식 불가
- **ID**: ieee:7339658
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: YouZhe Fan, ChenYang Xia, Ji Chen +4
- **PDF**: https://ieeexplore.ieee.org/document/7339658
- **Abstract**: Due to their provably capacity-achieving performance, polar codes have attracted a lot of research interest recently. For a good error-correcting performance, list successive-cancellation decoding (LSCD) with large list size is used to decode polar codes. However, as the complexity and delay of the list management operation rapidly increase with the list size, the overall latency of LSCD becomes large and limits the applicability of polar codes in high-throughput and latency-sensitive applications. Therefore, in this work, the low-latency implementation for LSCD with large list size is studied. Specifically, at the system level, a selective expansion method is proposed such that some of the reliable bits are not expanded to reduce the computation and latency. At the algorithmic level, a double thresholding scheme is proposed as a fast approximate-sorting method for the list management operation to reduce the LSCD latency for large list size. A VLSI architecture of the LSCD implementing the selective expansion and double thresholding scheme is then developed, and implemented using a UMC 90 nm CMOS technology. Experimental results show that, even for a large list size of 16, the proposed LSCD achieves a decoding throughput of 460 Mbps at a clock frequency of 658 MHz.

## On the Origin of Polar Coding

- **Status**: ❌
- **Reason**: Polar coding 기원 해설(리뷰성), 신규 디코더·구성 없음
- **ID**: ieee:7342879
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Erdal Arıkan
- **PDF**: https://ieeexplore.ieee.org/document/7342879
- **Abstract**: Polar coding was conceived originally as a technique for boosting the cutoff rate of sequential decoding, along the lines of earlier schemes of Pinsker and Massey. The key idea in boosting the cutoff rate is to take a vector channel (either given or artificially built), split it into multiple correlated subchannels, and employ a separate sequential decoder on each subchannel. Polar coding was originally designed to be a low-complexity recursive channel combining and splitting operation of this type, to be used as the inner code in a concatenated scheme with outer convolutional coding and sequential decoding. However, the polar inner code turned out to be so effective that no outer code was actually needed to achieve the original aim of boosting the cutoff rate to channel capacity. This paper explains the cutoff rate considerations that motivated the development of polar coding.

## Dynamic Grain State Estimation for High-Density TDMR: Progress and Future Directions

- **Status**: ❌
- **Reason**: TDMR grain 상태추정 GBP 검출기 — 채널 검출(detector) 특이, NAND LDPC ECC 이식 기법 아님
- **ID**: ieee:7247749
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Xueliang Sun, Benjamin J. Belzer, Krishnamoorthy Sivakumar
- **PDF**: https://ieeexplore.ieee.org/document/7247749
- **Abstract**: Dynamic grain state estimation (DGSE) algorithms for 2-D magnetic recording (TDMR) employ probabilistic message-passing algorithms that jointly estimate magnetic grain configurations and coded data bits, in order to iteratively assist channel decoding. At high densities (e.g., between 1 and 3 magnetic grains per coded bit), occasionally, a bit will not be written on any grain, and hence will effectively be overwritten (or erased) by bits on surrounding grains. DGSE enables the detection of overwritten bits so that their log-likelihood ratios are assigned small magnitudes, effectively making them erasures, which are easily filled in by linear channel codes. Past papers employing Bahl-Cocke-Jelinek-Raviv-based detectors on a simple four-rectangular-grain model have shown that the DGSE is surprisingly resilient to mismatch between the detector's assumed grain model and the actual model generating the data. This paper presents a novel DGSE-TDMR detector based on the generalized belief propagation (GBP) algorithm. The new detector employs a random discretized-nuclei Voronoi grain model. Simulation results show that the GBP-based TDMR turbo-detector accurately detects the overwritten bits and that it achieves low decoded bit error rates at densities as high as 0.4966 user bits per grain.

## Codes for Partially Stuck-At Memory Cells

- **Status**: ❌
- **Reason**: Partially stuck-at 멀티레벨 셀 마스킹 부호 - 비휘발성메모리 결함 셀 부호이나 LDPC ECC 아닌 마스킹 부호 구성, 떼어낼 LDPC 기법 없음
- **ID**: ieee:7369966
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Antonia Wachter-Zeh, Eitan Yaakobi
- **PDF**: https://ieeexplore.ieee.org/document/7369966
- **Abstract**: In this paper, we study a new model of defect memory cells, called partially stuck-at memory cells, which is motivated by the behavior of multi-level cells in non-volatile memories, such as flash memories and phase change memories. If a cell can store the  $q$  levels  $0, 1, {\dots }, q-1$ , we say that it is partially stuck-at level  $s$ , where  $1 \leq s \leq q-1$ , if it can only store values, which are at least  $s$ . We follow the common setup where the encoder knows the positions and levels of the partially stuck-at cells whereas the decoder does not. Our main contribution in this paper is the study of codes for masking  $u$  partially stuck-at cells. We first derive lower and upper bounds on the redundancy of such codes. The upper bounds are based on two trivial constructions. We then present three code constructions over an alphabet of size  $q$ , by first considering the case where the cells are partially stuck-at level  $s=1$ . The first construction works for  $u<q$  and is asymptotically optimal if  $u+1$  divides  $q$ . The second construction uses the reduced row echelon form of matrices to generate codes for the case  $u\geq q$ , and the third construction solves the case of arbitrary  $u$  by using codes, which mask binary stuck-at cells. We then show how to generalize all constructions to arbitrary stuck levels. Furthermore, we study the dual defect model, in which cells cannot reach higher levels, and show that codes for partially stuck-at cells can be used to mask this type of defects as well. Last, we analyze the capacity of the partially stuck-at memory channel and study how far our constructions are from the capacity.

## Two-Layer Coded Spatial Modulation With Block Markov Superposition Transmission

- **Status**: ❌
- **Reason**: 공간변조+BMST 부호, MIMO 응용 특이적이고 떼어낼 LDPC 기법 없음
- **ID**: ieee:7348663
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Leijun Wang, Chulong Liang, Zhihua Yang +1
- **PDF**: https://ieeexplore.ieee.org/document/7348663
- **Abstract**: This paper is concerned with the spatial modulation (SM), a multiple-input multiple-output (MIMO) transmission technique, that maps information bits not only into the conventional two-dimensional signal points but also into the indices of active transmit antennas. We present a two-layer coded SM scheme, in which the spatial bits carried by the antenna indices and the signal bits carried by the conventional signals are protected separately by two error correction codes. For the ease of decoding process, the code rates are allocated according to the chain rule of the mutual information. We choose block Markov superposition transmission (BMST) codes for each layer, since they are easily designed for any given code rate with a predictable performance lower bound. An iterative sliding-window decoding algorithm is also presented by exchanging messages iteratively between the two BMST decoders and the soft-in soft-out (SISO) demapper of the SM. To reduce the computational complexity, we propose to implement the SISO demapping algorithm by employing only partial soft inputs. Numerical results show that the BMST-SM system performs well over uncorrelated Rayleigh fading channels.

## Comparison of Two-Reader and Three-Reader 2-D Magnetic Recording Systems

- **Status**: ❌
- **Reason**: 2/3-reader TDMR 시스템 비교·reader 배치 최적화 — LDPC ECC 신규 기법 없음
- **ID**: ieee:7258393
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Nedeljko Varnica, Rathnakumar Radhakrishnan, Shashi Kiran Chilappagari +2
- **PDF**: https://ieeexplore.ieee.org/document/7258393
- **Abstract**: Two-reader two-dimensional magnetic recording (TDMR) system is expected to improve areal density by about 10%, although practical considerations may limit the realization of all of the available gain. As a result, for further growth, hard-disk drive industry has started to develop the second-generation TDMR system, consisting of three readers. Although a natural evolution of the first-generation, it brings its own issues and challenges. In this paper, we study the behavior and optimization of the three-reader system with a particular focus on reader placement and cross-track error-correction coding gains. In addition, we consider a lower cost two-reader solution with streaming intertrack interference cancellation as an alternative to employing three readers.

## Multilevel Reed–Solomon Codes for PMR Channels

- **Status**: ❌
- **Reason**: 비-LDPC 부호(Reed-Solomon) 멀티레벨 코딩+SOVA, 자기기록 특이적, LDPC BP 이식 기법 없음
- **ID**: ieee:7307210
- **Type**: journal
- **Published**: Feb. 2016
- **Authors**: Ismail Demirkan, Gregory Silvus
- **PDF**: https://ieeexplore.ieee.org/document/7307210
- **Abstract**: Reed-Solomon (RS) codes are commonly utilized in magnetic recording systems to correct error bursts. A soft-output Viterbi algorithm (SOVA) is a commonly used detector to provide soft information to error-correcting decoders. We propose a novel architecture of a multilevel interleaved RS coding scheme that not only provides better performance but also has less complexity than an equivalent RS code. This architecture implements an error event detector using the soft information generated by the SOVA detector. The performance and complexity of the decoding technique are compared with the well-known soft-decoding techniques, such as generalized minimum distance decoding and Chase decoding techniques.

## Globally coupled LDPC codes

- **Status**: ✅
- **Reason**: globally coupled LDPC 신규 구성+2-phase local/global 반복 디코딩, 바이너리 채널 코드설계+디코더(E/C)
- **ID**: ieee:7888167
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Juane Li, Shu Lin, Khaled Abdel-Ghaffar +2
- **PDF**: https://ieeexplore.ieee.org/document/7888167
- **Abstract**: This paper presents a special type of LDPC codes with a structure related to but different from that of the spatially coupled LDPC codes. For an LDPC code of this type, its Tanner graph is composed of a set of small disjoint Tanner graphs which are connected together by a group of overall check-nodes, called global check-nodes. Codes of this type are called globally coupled LDPC codes and they perform well over both the additive Gaussian white noise and the binary-erasure channels. Furthermore, they are very effective at correcting erasures clustered in bursts. Two algebraic methods are presented for constructing these codes. A two-phase local/global iterative scheme for decoding these codes is presented. This decoding scheme allows correction of local random and global errors and/or erasures in two phases.

## Some results on spatially coupled protograph LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC 프로토그래프 신규 설계+RCA threshold 분석(바이너리 채널), 이식 가능 코드설계(E)
- **ID**: ieee:7888150
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Sudarsan V. S. Ranganathan, Kasra Vakilinia, Lara Dolecek +2
- **PDF**: https://ieeexplore.ieee.org/document/7888150
- **Abstract**: Spatially coupled low-density parity-check block codes (SC-LDPC-BCs) are a class of LDPC codes in which certain ensembles achieve capacity under iterative belief propagation decoding. Prior work has considered these codes mostly from a protograph perspective. Following this viewpoint, our work presents new protographs for the design of protograph-based SC-LDPC-BCs. A reciprocal channel approximation (RCA) analysis of the terminated protographs yields the asymptotic performance limits of the ensembles in terms of their iterative decoding thresholds. Our protographs possess the properties of linear minimum distance growth rate and excellent thresholds. We consider the following channels in our work: binary-input additive white Gaussian noise channel (BI-AWGNC), binary erasure channel (BEC), and binary symmetric channel (BSC). Our work focuses on obtaining good designs, with two classes of ensembles being asymptotically regular, for all the three channels while minimizing rate loss.

## Approaching maximum likelihood performance of LDPC codes by stochastic resonance in noisy iterative decoders

- **Status**: ✅
- **Reason**: noisy iterative decoder의 stochastic resonance로 ML 성능 접근, error-floor 탈출 신규 디코딩 통찰=이식 가능 디코더(C)
- **ID**: ieee:7888185
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Bane Vasić, Predrag Ivaniš, David Declercq +1
- **PDF**: https://ieeexplore.ieee.org/document/7888185
- **Abstract**: In the 1960s-70s, Taylor and Kuznetsov obtained a remarkable result that information can be reliably retrieved from a noisy channel even if a decoder is made of noisy components. The results of Vasic and Chilappagari presented at the ITA Workshop ten years ago have revived the interest in decoders made of noisy hardware and since then a number of improvements of the iterative decoders have been made to bring their performance closer to that of their perfect counterparts. However, a common mantra has been that noisy decoders cannot be better than their perfect counterparts. In this talk we report an unexpected phenomenon we have recently discovered - noise can actually improve the error correction process by reducing the probability of decoding error, in some cases by more that two orders of magnitude. This new form of stochastic resonance enables us to use logic gate errors to correct channel errors. This novelty recognizes that the decoder - essentially an iterative minimization of the Bethe free energy on the code graph - can get trapped in local minima, and random perturbations help the decoder to escape from these minima and converge to a correct code-word. In the spirit of Marcus Tullius Cicero's “Clavus clavo eicitur,” (“one nail drives out another”) they operate on the principle: Error errore eicitur” - “one error drives out another.” Crucially, such useful random perturbations require neither additional hardware nor energy, as they are built into the low-powered, noisy hardware itself.

## On adaptive linear programming decoding of linear codes over GF(8)

- **Status**: ❌
- **Reason**: GF(8) 비이진 부호의 적응적 LP 디코딩; 비이진 LDPC 제외 대상
- **ID**: ieee:7888132
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Eirik Rosnes, Michael Helmling
- **PDF**: https://ieeexplore.ieee.org/document/7888132
- **Abstract**: In this work, we consider adaptive linear programming (LP) decoding of linear codes over GF(8). In particular, we give explicit constructions of valid inequalities (using no auxiliary variables) for the codeword polytope (or the convex hull) of the so-called constant-weight embedding of a single parity-check code over GF(8) that all are facet-defining. We conjecture that these inequalities together with so-called simplex constraints give a complete and irredundant description of the embedded (under the constant-weight embedding) codeword polytope. Furthermore, these sets of inequalities are used to develop an efficient (as compared to a static approach) exact (assuming that the conjecture is true) adaptive LP decoder for linear codes over GF(8). Numerical results show that only a very small subset of these inequalities is necessary for achieving close-to-exact LP decoding performance.

## Message-aggregation enhanced iterative hard-decision decoders

- **Status**: ✅
- **Reason**: message-aggregation으로 trapping set 제거하는 신규 hard-decision 디코더(error-floor 개선)=이식 가능 디코더(C)
- **ID**: ieee:7888184
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Srdan Brkic, Predrag Ivanis, Bane Vasić +1
- **PDF**: https://ieeexplore.ieee.org/document/7888184
- **Abstract**: We present an iterative decoding algorithm for annihilating trapping sets in low-density parity-check codes. In addition to classic messages, subsets of variable nodes communicate directly. We show that by allowing variable nodes to collect information from a larger part of a graph, significant improvement can be achieved in the error-floor region, compared to the classic hard decision decoders. We also propose a new hybrid hard-decision decoding algorithm which employs described strategy and the Gallager B decoders as its components. Our decoder outperforms all known hard-decision decoders of same or higher complexity.

## Duality between erasures and defects

- **Status**: ❌
- **Reason**: BEC/BDC 이중성, RM/polar 부호+LWC 저항메모리; 바이너리 LDPC ECC 디코더 기법 아님(소스/이론·비-LDPC)
- **ID**: ieee:7888148
- **Type**: conference
- **Published**: 31 Jan.-5 
- **Authors**: Yongjune Kim, B.V.K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/7888148
- **Abstract**: We investigate the duality of the binary erasure channel (BEC) and the binary defect channel (BDC). This duality holds for channel capacities, capacity achieving schemes, minimum distances, and upper bounds on the probability of failure to retrieve the original message. In addition, the relations between BEC, BDC, binary erasure quantization (BEQ), and write-once memory (WOM) are described. From these relations we claim that the capacity of the BDC can be achieved by Reed-Muller (RM) codes under maximum a posterior (MAP) decoding. Also, polar codes with a successive cancellation encoder achieve the capacity of the BDC. Inspired by the duality between the BEC and the BDC, we introduce locally rewritable codes (LWC) for resistive memories, which are the counterparts of locally repairable codes (LRC) for distributed storage systems. The proposed LWC can improve endurance limit and power efficiency of resistive memories.

## Joint iterative channel estimation and decoding under impulsive interference condition

- **Status**: ❌
- **Reason**: 7423584 중복 논문, 동일 사유로 제외
- **ID**: ieee:7423585
- **Type**: conference
- **Published**: 31 Jan.-3 
- **Authors**: Patcharin Insom, Piyakiat Insom, Pisit Boonsrimuang
- **PDF**: https://ieeexplore.ieee.org/document/7423585
- **Abstract**: Even though Low-Density-Parity-Check (LDPC) code which has the decoding performance close to the Shannon Limit and it is designed as a powerful forward-error-correction (FEC) code in the Additive White Gaussian Noise (AWGN) channel, simulation results show that the performance of LDPC decoder is degraded when exposed to the impulsive noise. According to such a impulsive noise impact, joint iterative channel estimation and decoding technique is proposed in this paper so as to decrease the effect of impulsive interference while less complicated in processing. The proposed methods decreases the complexity by implementing the simple way of channel estimation and applying joint iterative technique between channel estimation and LDPC decoding under two kind of impulsive noise; pulsed radio frequency interference(RFI) and symmetric alpha-stable (SαS). In the optimal decoder, channel parameter estimation can be as accurate as possible. Because computed in every time of iterative decoder, channel parameters have been always optimized resulting in the enhancement of LDPC decoder performance.

## Joint iterative channel estimation and decoding under impulsive interference condition

- **Status**: ❌
- **Reason**: 무선 임펄스 잡음용 joint 채널추정+LDPC 디코딩, LDPC는 베이스라인이고 떼어낼 NAND 이식 디코더/HW 기법 없음
- **ID**: ieee:7423584
- **Type**: conference
- **Published**: 31 Jan.-3 
- **Authors**: Patcharin Insom, Piyakiat Insom, Pisit Boonsrimuang
- **PDF**: https://ieeexplore.ieee.org/document/7423584
- **Abstract**: Even though Low-Density-Parity-Check (LDPC) code which has the decoding performance close to the Shannon Limit and it is designed as a powerful forward-error-correction (FEC) code in the Additive White Gaussian Noise (AWGN) channel, simulation results show that the performance of LDPC decoder is degraded when exposed to the impulsive noise. According to such a impulsive noise impact, joint iterative channel estimation and decoding technique is proposed in this paper so as to decrease the effect of impulsive interference while less complicated in processing. The proposed methods decreases the complexity by implementing the simple way of channel estimation and applying joint iterative technique between channel estimation and LDPC decoding under two kind of impulsive noise; pulsed radio frequency interference(RFI) and symmetric alpha-stable (SαS). In the optimal decoder, channel parameter estimation can be as accurate as possible. Because computed in every time of iterative decoder, channel parameters have been always optimized resulting in the enhancement of LDPC decoder performance.

## Comparative performance analysis of forward error correcting codes for Free Space Optical communication

- **Status**: ❌
- **Reason**: FEC 부호 BER 단순 비교(Hamming/LDPC/Turbo), 새 디코더·구성·HW 기여 없음 — 표준 비교 수준
- **ID**: ieee:7603067
- **Type**: conference
- **Published**: 24-26 Feb.
- **Authors**: R. Leoraj, J. Arputha Vijaya Selvi
- **PDF**: https://ieeexplore.ieee.org/document/7603067
- **Abstract**: Free Space Optical communication system communicates data's which are interleaved with errors during the transmission. These errors occur because of various atmospheric turbulence conditions. The Bit Error Rate (BER) is an important measurement in laser communication link to estimate the quality of the data link connection. Forward Error Correction (FEC) codes are used to detect and correct the errors, so that the original data can be recovered at the receiving end. The performance of Hamming code, Low Density Parity Check (LDPC) code and Turbo code are compared based on Bit Error Rate. Simulation is done using MATLAB and it is observed that LDPC code exhibits low bit error rate compared to other two codes.

## Modified PEG algorithm for large girth Quasi-cyclic protograph LDPC codes

- **Status**: ✅
- **Reason**: 수정 PEG 알고리즘으로 QC protograph LDPC large girth 구성+permutation shift 최적화 — 바이너리 코드설계(E)
- **ID**: ieee:7440704
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Xue-Qin Jiang, Moon Ho Lee, Hui-Ming Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/7440704
- **Abstract**: For a given base graph, the protograph can be obtained by a copy-and-permute procedure. If the permutation is cyclic, the protograph corresponds to a quasi-cyclic (QC) protograph LDPC code. The girth of the QC protograph LDPC code is determined by the girth of the base graph and the permutation shifts. Progressive edge-growth (PEG) construction builds up a Tanner graph, or equivalently a parity-check matrix, for an LDPC code by maximizing the local girth at symbol nodes in a greedy algorithm. In this paper, we introduce a modified version of the PEG algorithm which can construct large girth base graph and determine the optimal permutation shifts, simultaneously, for QC protograph LDPC codes. Simulation results show that the QC protograph LDPC codes constructed by the proposed modified PEG algorithm have good frame error rate (FER) performance over the AWGN channel.

## Improved trellis-based decoder for non-binary LDPC codes

- **Status**: ❌
- **Reason**: non-binary LDPC trellis 디코더 — 비이진 LDPC 제외 대상
- **ID**: ieee:7440727
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Sangmin Kim
- **PDF**: https://ieeexplore.ieee.org/document/7440727
- **Abstract**: In this paper, we use a column-wise, row-wise approach for efficiently choosing reliable messages in decoding non-binary Low-Density Parity-Check (LDPC) codes, and build configurations with those reliable messages for updating check nodes. This method decreases the number of configurations compared to conventional trellis-based decoding algorithms. In addition, a novel algorithm with precomputed messages is proposed which improves decoding performance. Using the reduced configuration set with the improved message updating scheme it is shown that we can achieve an improved decoding performance while reducing the hardware complexity. Compared to trellis-based decoders, the proposed decoder reduces the number of required operations in computing check-to-variable messages and achieves better error-correcting performance.

## Joint source-channel decoding for LDPC-coded error-corrupted binary Markov sources

- **Status**: ❌
- **Reason**: JSCD(소스-채널 결합) CEO 문제, SP-BCJR serial concat — LDPC 베이스라인이고 떼어낼 ECC 기법 없음
- **ID**: ieee:7440677
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Amin Zribi, Tad Matsumoto, Ramesh Pyndiah
- **PDF**: https://ieeexplore.ieee.org/document/7440677
- **Abstract**: We consider the problem of joint decoding and data fusion in data gathering for densely deployed sensor networks modeled by the Chief Executive Officer (CEO) problem. More specifically, we consider the binary CEO problem where all sensors observe the same time-correlated binary Markov source corrupted by independent binary noises. Hence, the observations are two-dimensionally (temporary and spatially) correlated. In the proposed scheme, every sensor apply a low-density parity-check (LDPC) code and transmit the corresponding codeword independently over additive white Gaussian noise (AWGN) channels. To reconstruct the original bit sequence, an iterative joint source-channel decoding (JSCD) technique is considered. To exploit the knowledge about the source correlations, we consider an iterative decoding between a sum-product (SP) decoder serially concatenated with BCJR decoder which is applied for every sensor as local iterations. Then, correlation between sensors' data is employed to update extrinsic information received from the SP-BCJR decoders of the different sensors during global iterations. We illustrate the performance of the joint decoder for different correlation setups and with different number of sensors. Simulation results, in terms of bit error rate show promising improvements compared with the separate decoding scheme where the correlation knowledge is not completely utilized in the decoder.

## Optimization of codes for the joint Viterbi detector decoder (JVDD)

- **Status**: ✅
- **Reason**: JVDD용 LDPC 코드 4종 신규 설계(고정/비례 행·열 가중치) — 바이너리 LDPC 코드설계 기여(E), DOE 최적화
- **ID**: ieee:7440607
- **Type**: conference
- **Published**: 15-18 Feb.
- **Authors**: Sari Shafidah Bte Shafiee, Chan Kheong Sann, Goh Wang Ling
- **PDF**: https://ieeexplore.ieee.org/document/7440607
- **Abstract**: The joint Viterbi detector decoder (JVDD) was recently proposed as an alternative to iterative detector/decoder systems (also known as turbo equalizers) used in communication applications today. Despite being conditionally optimal over coded additive white Gaussian noise (AWGN)/inter-symbol interference (ISI) channels, the JVDD suffers from an exponential growth in the number of survivors when used with existing codes such as random low-density parity check (LDPC) codes. This paper proposes a class of JVDD codes designed for the JVDD which mitigate this undesirable trait. This class of codes consists of 4 code designs — 1) fixed row weight, 2) fixed column weight, 3) proportionate row weight and 4) proportionate column weight. While the proposed JVDD codes do effectively bring about a reduction in complexity and enhance the performance of the JVDD, the design parameters of these codes require optimization. In this paper, a design of experiment (DOE) technique that employs the response surface methodology (RSM) is used as a tool to optimize the parameters of each of the proposed codes.
