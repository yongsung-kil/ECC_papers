# arXiv — 2026-04 (1차선별 통과)


## High-Girth Regular Quantum LDPC Codes from Square-Base Hypergraph Products via CPM Lifts

- **Status**: ✅
- **Reason**: 양자 CSS-LDPC이나 CPM lift·girth 6/8 구성, 짧은사이클 배제 조건, BP+OSD-lite 후처리 — 코드설계(E)·디코더(C) 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.27817v1
- **Type**: preprint
- **Published**: 2026-04-30
- **Authors**: Koki Okada, Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2604.27817v1
- **Abstract**: We study square-base Calderbank--Shor--Steane (CSS) hypergraph-product codes as a finite-length class for regular high-girth quantum low-density parity-check (LDPC) design. For base matrices of small column weight, we give checkable conditions for regularity, rank deficiency, and short-cycle exclusion, and we present explicit column-weight-three and column-weight-four examples with Tanner girth 6 and 8. We also analyze circulant permutation matrix (CPM) lifts of this class. Using the standard voltage-sum criterion, we identify orthogonality-forced Tanner 8-cycles and show that CPM lifting cannot raise the Tanner girth beyond 8 when these cycles are present. As a representative finite-length instance, a randomized CPM lift of the girth-8 base construction gives a $[[28800,62]]$ girth-8 $(3,6)$-regular CSS-LDPC code. Under degeneracy-aware belief-propagation decoding with optional ordered-statistics-decoding-lite post-processing, this code produced zero decoding failures in $2.993\times 10^8$ independent trials at depolarizing probability $p=0.1402$; the Wilson 95% upper confidence bound is $1.28\times 10^{-8}$.

## Turán-Theoretic Bounds on Several Elementary Trapping Sets in LDPC Codes

- **Status**: ✅
- **Reason**: 고전 LDPC elementary trapping set·error floor·QC-LDPC 구성으로 코드 설계(E) 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.12332v2
- **Type**: preprint
- **Published**: 2026-04-14
- **Authors**: Ziyang Zhao, Haoran Xiong, Zicheng Ye +1
- **PDF**: https://arxiv.org/pdf/2604.12332v2
- **Abstract**: LDPC codes have attracted significant attention because of their superior performance close to the Shannon limit. Elementary trapping sets are the main cause of the error floor phenomenon in LDPC codes. We consider typical graphs related to trapping sets, including theta graphs, dumbbell graphs, and short cycles with chords. Based on the Turán numbers of $θ(2,2,2)$, $θ(1,3,3)$ and $D(4,4;0)$, we prove that any $(a,b)$-ETS with $g=8$ variable-regular $γ$ satisfies the inequality $b\geq aγ-\frac{a(\sqrt{24a-23}-1)}{4}$, provided that any two 8-cycles in the Tanner graph do not share common variable node. In addition, we can also eliminate ETSs by removing certain short-cycle structures with chords. The minimum sizes of ETSs obtained through these methods are significantly increased. To assess practical impact , we analyze spectral radii of the ETSs and construct QC-LDPC codes to show frame error rates in the error floor region.

## Scalable Neural Decoders for Practical Fault-Tolerant Quantum Computation

- **Status**: ✅
- **Reason**: qLDPC용 CNN 신경망 디코더지만 코드 기하구조 활용·실시간 처리량 등 디코더 알고리즘이 NAND LDPC로 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.08358v1
- **Type**: preprint
- **Published**: 2026-04-09
- **Authors**: Andi Gu, J. Pablo Bonilla Ataides, Mikhail D. Lukin +1
- **PDF**: https://arxiv.org/pdf/2604.08358v1
- **Abstract**: Quantum error correction (QEC) is essential for scalable quantum computing. However, it requires classical decoders that are fast and accurate enough to keep pace with quantum hardware. While quantum low-density parity-check codes have recently emerged as a promising route to efficient fault tolerance, current decoding algorithms do not allow one to realize the full potential of these codes in practical settings. Here, we introduce a convolutional neural network decoder that exploits the geometric structure of QEC codes, and use it to probe a novel "waterfall" regime of error suppression, demonstrating that the logical error rates required for large-scale fault-tolerant algorithms are attainable with modest code sizes at current physical error rates, and with latencies within the real-time budgets of several leading hardware platforms. For example, for the $[144, 12, 12]$ Gross code, the decoder achieves logical error rates up to $\sim 17$x below existing decoders - reaching logical error rates $\sim 10^{-10}$ at physical error $p=0.1\%$ - with 3-5 orders of magnitude higher throughput. This decoder also produces well-calibrated confidence estimates that can significantly reduce the time overhead of repeat-until-success protocols. Taken together, these results suggest that the space-time costs associated with fault-tolerant quantum computation may be significantly lower than previously anticipated.

## Belief Propagation Convergence Prediction for Bivariate Bicycle Quantum Error Correction Codes

- **Status**: ✅
- **Reason**: BP 수렴 사전예측(mod-w) 기법은 양자 BB코드 대상이나 BP 디코더 일반에 적용 가능한 알고리즘적 통찰(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.07995v1
- **Type**: preprint
- **Published**: 2026-04-09
- **Authors**: Anton Pakhunov
- **PDF**: https://arxiv.org/pdf/2604.07995v1
- **Abstract**: Decoding Bivariate Bicycle (BB) quantum error correction codes typically requires Belief Propagation (BP) followed by Ordered Statistics Decoding (OSD) post-processing when BP fails to converge. Whether BP will converge on a given syndrome is currently determined only after running BP to completion. We show that convergence can be predicted in advance by a single modulo operation: if the syndrome defect count is divisible by the code's column weight w, BP converges with high probability (100% at p <= 0.001, degrading to 87% at p = 0.01); otherwise, BP fails with probability >= 90%. The mechanism is structural: each physical data error activates exactly w stabilizers, so a defect count not divisible by w implies the presence of measurement errors outside BP's model space. Validated on five BB codes with column weights w = 2, 3, and 4, mod-w achieves AUC = 0.995 as a convergence classifier at p = 0.001 under phenomenological noise, dominating all other syndrome features (next best: AUC = 0.52). The false positive rate scales empirically as O(p^2.05) (R^2 = 0.98), confirming the analytical bound from Proposition 2. Among BP failures on mod-w = 0 syndromes, 82% contain weight-2 data error clusters, directly confirming the dominant failure mechanism. The prediction is invariant under BP scheduling strategy and decoder variant, including Relay-BP - the strongest known BP enhancement for quantum LDPC codes. These results apply directly to IBM's Gross code [[144, 12, 12]] and Two-Gross code [[288, 12, 18]], targeted for deployment in 2026-2028.

## Channel Estimation and LDPC Decoding for Bursty Phase Noise

- **Status**: ✅
- **Reason**: 채널추정-LDPC 반복 디코딩 기법이며 무선 응용이나 burst-aware soft-decision LDPC 디코딩 알고리즘 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.07004v1
- **Type**: preprint
- **Published**: 2026-04-08
- **Authors**: Han Cui, Frank R. Kschischang, Magnus Karlsson +1
- **PDF**: https://arxiv.org/pdf/2604.07004v1
- **Abstract**: Time-varying distortions in communication systems can significantly degrade the performance of soft-decision forward error correction. This paper presents a burst-aware (BA) low-density parity-check (LDPC) decoding scheme for channels affected by bursty phase noise. By applying differential coding to a Wiener process with time-varying innovation variance, bursty differential phase noise is obtained. Simulation results demonstrate that, compared to conventional decoding, the BA scheme achieves gains in the signal-to-noise ratio of up to $0.7$~dB at a bit error rate (BER) of $4\cdot10^{-3}$ and more than $1$~dB at a packet error rate (PER) of $1\cdot10^{-2}$. Furthermore, by iterating between channel estimation and \ac{ldpc} decoding, forming the proposed iterative burst-aware (IBA) decoding scheme, the gains increase to $1.4$~dB and more than $3$~dB, respectively. More importantly, the IBA scheme significantly improves robustness to bursty phase noise. Compared with the conventional scheme, the IBA scheme can reduce both \ac{ber} and \ac{per} by up to two orders of magnitude under severe bursty phase noise.

## Affine Subcode Ensemble Decoding of Linear Block Codes

- **Status**: ✅
- **Reason**: 앙상블 디코딩(aSCED)·BP update rule·고성능 parity-check 구성 — LDPC에 직접 적용된 디코더/코드설계 기법(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.06889v1
- **Type**: preprint
- **Published**: 2026-04-08
- **Authors**: Jonathan Mandelbaum, Paul Bezner, Holger Jäkel +2
- **PDF**: https://arxiv.org/pdf/2604.06889v1
- **Abstract**: In the short block length regime, ensemble decoding schemes with their inherently parallel structure can improve error correction performance and reduce latency compared to stand-alone suboptimal decoders such as belief propagation (BP). In this work, we introduce affine subcode ensemble decoding (aSCED), which uses an ensemble of decoders operating on linear block codes and both linear and strictly affine subcodes. This generalizes the recently proposed subcode ensemble decoding (SCED), which is restricted to linear subcodes. We derive BP update rules for affine subcodes and show that aSCED simplifies ensemble design compared to SCED, multiple bases BP, and automorphism ensemble decoding. Monte-Carlo simulations of two low-density parity-check codes and two Bose-Chaudhuri-Hocquenghem (BCH) codes demonstrate improved error correction performance of aSCED over competing existing ensemble schemes. Notably, for one BCH code, when combining ensemble design with algorithms for constructing high-performance parity-check matrices, aSCED achieves near-maximum likelihood performance using only 64 BP decoding paths.

## Quasi-BP for BCH Codes and its Optimization

- **Status**: ✅
- **Reason**: BCH용 quasi-BP 디코더이나 EXIT 차트 최적화·병렬 반복 디코딩 알고리즘이 LDPC BP에 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.04066v1
- **Type**: preprint
- **Published**: 2026-04-05
- **Authors**: Guangwen Li
- **PDF**: https://arxiv.org/pdf/2604.04066v1
- **Abstract**: This paper proposes a quasi-belief propagation decoder for BCH codes that systematically integrates domain knowledge--specifically, channel noise variance, the cyclic property of the codes, and the deliberate redundancy in their parity-check matrices--to enable efficient iterative decoding. We rigorously formalize this parallelizable decoder within an information-theoretic framework by tracking mutual information evolution through the constituent variable and check decoders, thereby validating the use of scattered EXIT charts as a tool for optimizing the decoder's parameters. At each iteration, an input dilation operation expands the set of messages, while a subsequent merging operation accelerates mutual information growth, ensuring rapid convergence. The proposed decoder achieves decoding performance approaching that of LDPC codes with comparable rate and blocklength, effectively pioneering the feasible deployment of BP-like decoding for high-density parity-check codes. The generality and robustness of the scheme are demonstrated through extensive simulations across codes of varying rates and blocklengths.

## Tunneling-Augmented Simulated Annealing for Short-Block LDPC Code Construction

- **Status**: ✅
- **Reason**: 단블록 LDPC parity-check 행렬 구성을 사이클·trapping set 제거로 최적화(TASA) — 코드 설계 기법 직접 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2604.07365v1
- **Type**: preprint
- **Published**: 2026-04-01
- **Authors**: Atharv Kanchi
- **PDF**: https://arxiv.org/pdf/2604.07365v1
- **Abstract**: Designing high-performance error-correcting codes at short blocklengths is critical for low-latency communication systems, where decoding is governed by finite-length and graph-structural effects rather than asymptotic properties. This paper presents a global discrete optimization framework for constructing short-block linear codes by directly optimizing parity-check matrices. Code design is formulated as a constrained binary optimization problem with penalties for short cycles, trapping-set-correlated substructures, and degree violations. We employ a hybrid strategy combining tunneling-augmented simulated annealing (TASA) with classical local refinement to explore the resulting non-convex space. Experiments at blocklengths 64-128 over the AWGN channel show 0.1-1.3 dB SNR gains over random LDPC codes (average 0.45 dB) and performance within 0.6 dB of Progressive Edge Growth. In constrained regimes, the method enables design tradeoffs unavailable to greedy approaches. However, structural improvements do not always yield decoding gains: eliminating 1906 trapping set patterns yields only +0.08 dB improvement. These results position annealing-based global optimization as a complementary tool for application-specific code design under multi-objective constraints.
