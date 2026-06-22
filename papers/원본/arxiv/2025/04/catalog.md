# arXiv — 2025-04


## Quantum Error Correction with Girth-16 Non-Binary LDPC Codes via Affine Permutation Construction

- **Status**: ❌
- **Reason**: 비이진(non-binary) LDPC 명시 + 양자 코드 — 비이진은 즉시 제외
- **ID**: arxiv:2504.17790v2
- **Type**: preprint
- **Published**: 2025-04-24
- **Authors**: Kenta Kasai
- **PDF**: https://arxiv.org/pdf/2504.17790v2
- **Abstract**: We propose a method for constructing quantum error-correcting codes based on non-binary low-density parity-check codes with Tanner graph girth 16. While conventional constructions using circulant permutation matrices are limited to girth 12, our method employs affine permutation matrices and a randomized sequential selection procedure to eliminate short cycles and achieve girth 16.   Numerical experiments show that the proposed codes significantly reduce the number of low-weight codewords. Joint belief propagation decoding over depolarizing channels reveals that although a slight degradation appears in the waterfall region, a substantial improvement is achieved in the error floor performance.   We also evaluated the minimum distance and found that the proposed codes achieve a larger upper bound compared to conventional constructions.

## Subcode Ensemble Decoding of Polar Codes

- **Status**: ✅
- **Reason**: ScED(subcode ensemble decoding)는 본래 바이너리 LDPC용 디코더 기법, 이식 가능성 있어 Phase 3 재검토(C)
- **ID**: arxiv:2504.17511v1
- **Type**: preprint
- **Published**: 2025-04-24
- **Authors**: Henning Lulei, Jonathan Mandelbaum, Marvin Rübenacke +3
- **PDF**: https://arxiv.org/pdf/2504.17511v1
- **Abstract**: In the short block length regime, pre-transformed polar codes together with successive cancellation list (SCL) decoding possess excellent error correction capabilities. However, in practice, the list size is limited due to the suboptimal scaling of the required area in hardware implementations. Automorphism ensemble decoding (AED) can improve performance for a fixed list size by running multiple parallel SCL decodings on permuted received words, yielding a list of estimates from which the final estimate is selected. Yet, AED is limited to appropriately designed polar codes. Subcode ensemble decoding (ScED) was recently proposed for low-density parity-check codes and does not impose such design constraints. It uses multiple decodings in different subcodes, ensuring that the selected subcodes jointly cover the original code. We extend ScED to polar codes by expressing polar subcodes through suitable pre-transformations (PTs). To this end, we describe a framework classifying pre-transformations for pre-transformed polar codes based on their role in encoding and decoding. Within this framework, we propose a new type of PT enabling ScED for polar codes, analyze its properties, and discuss how to construct an efficient ensemble.

## Explicit Lossless Vertex Expanders

- **Status**: ❌
- **Reason**: expander 구성이 양자 LDPC(Lin-Hsieh) 전용, 고전 바이너리 LDPC 이식 기법 부재
- **ID**: arxiv:2504.15087v1
- **Type**: preprint
- **Published**: 2025-04-21
- **Authors**: Jun-Ting Hsieh, Alexander Lubotzky, Sidhanth Mohanty +2
- **PDF**: https://arxiv.org/pdf/2504.15087v1
- **Abstract**: We give the first construction of explicit constant-degree lossless vertex expanders. Specifically, for any $\varepsilon > 0$ and sufficiently large $d$, we give an explicit construction of an infinite family of $d$-regular graphs where every small set $S$ of vertices has $(1-\varepsilon)d|S|$ neighbors (which implies $(1-2\varepsilon)d|S|$ unique-neighbors). Our results also extend naturally to construct biregular bipartite graphs of any constant imbalance, where small sets on each side have strong expansion guarantees. The graphs we construct admit a free group action, and hence realize new families of quantum LDPC codes of Lin and M. Hsieh with a linear time decoding algorithm.   Our construction is based on taking an appropriate product of a constant-sized lossless expander with a base graph constructed from Ramanujan Cayley cubical complexes.

## A Short Proof of Coding Theorems for Reed-Muller Codes Under a Mild Assumption

- **Status**: ❌
- **Reason**: RM=LDPC 부호정리 단증명, 순수 이론(소스코딩 포함), 디코더/HW/구성 신규 기여 없음
- **ID**: arxiv:2504.14842v2
- **Type**: preprint
- **Published**: 2025-04-21
- **Authors**: Xiao Ma
- **PDF**: https://arxiv.org/pdf/2504.14842v2
- **Abstract**: In this paper, by treating Reed-Muller (RM) codes as a special class of low-density parity-check (LDPC) codes and assuming that sub-blocks of the parity-check matrix are randomly interleaved to each other as Gallager's codes, we present a short proof that RM codes are entropy-achieving as source coding for Bernoulli sources and capacity-achieving as channel coding for binary memoryless symmetric (BMS) channels, also known as memoryless binary-input output-symmetric (BIOS) channels, in terms of bit error rate (BER) under maximum-likelihood (ML) decoding.

## Feedforward suppression of readout-induced faults in quantum error correction

- **Status**: ❌
- **Reason**: 양자 readout 결함 억제 프로토콜, 큐비트 측정 전용 — 이식 가능 ECC 기법 없음
- **ID**: arxiv:2504.13083v3
- **Type**: preprint
- **Published**: 2025-04-17
- **Authors**: Liran Shirizly, Dekel Meirom, Malcolm Carroll +1
- **PDF**: https://arxiv.org/pdf/2504.13083v3
- **Abstract**: Qubit measurements in quantum devices involve various types of errors, including erroneous state determination, correlated preparation errors and measurement-induced leakage from the computational states. We propose a feedforward protocol to reduce readout-induced faults, applicable for qubits with errors biased between the different states, in settings like quantum error correction with repeated measurement cycles. The method consists of an adaptive readout sequence conditioned on each check qubit's readout result from the previous cycle, which is optimized for the expected measured state. Focusing on a simple realization of conditionally flipping (by an X gate) the state of check qubits before their measurement, we investigate the effect of such state-dependent errors using simulations in the setup of a low-density parity check code. We show that the suggested protocol can reduce both logical errors and decoding time, two important aspects of fault-tolerant quantum computations.

## Planar quantum low-density parity-check codes with open boundaries

- **Status**: ❌
- **Reason**: 양자 qLDPC(BB/평면 stabilizer 코드) 구성, 양자 전용 개념 의존
- **ID**: arxiv:2504.08887v4
- **Type**: preprint
- **Published**: 2025-04-11
- **Authors**: Zijian Liang, Jens Niklas Eberhardt, Yu-An Chen
- **PDF**: https://arxiv.org/pdf/2504.08887v4
- **Abstract**: Although high-threshold and low-overhead quantum low-density parity-check (qLDPC) codes, such as bivariate bicycle (BB) codes, can reduce the physical-qubit cost by an order of magnitude compared to the Kitaev toric code, their torus layout remains difficult for physical implementation. In this work, we introduce the first systematic procedure to convert BB codes into fully planar, open-boundary qLDPC codes, preserving their performance. We present planar code families with logical dimensions $6 \leq k\leq13$, e.g., $[[78, 6, 6]]$, $[[107, 7, 7]]$, $[[268, 8, 12]]$, $[[405, 9, 15]]$, $[[348, 10, 13]]$, $[[450, 11, 15]]$, $[[386, 12, 12]]$, $[[362, 13, 11]]$, all with geometrically local weight-6 stabilizers. Allowing weight-8 stabilizers produces a $[[282,12,14]]$ code, exhibiting an efficiency metric ($kd^2/n$) an order of magnitude higher than the surface code. The construction combines boundary anyon condensation with the ``lattice grafting'' optimization, yielding high-performance qLDPC codes natively compatible with planar hardware architectures. It also uncovers Sierpinski-type fractal logical operators whose distance scales with the fractal area on finite lattices. These planar qLDPC codes provide an implementable route to resource-efficient, high-threshold fault tolerance and a flexible framework for future code design on realistic two-dimensional hardware.

## Continuous-Variable Quantum Key Distribution with Composable Security and Tight Error Correction Bound for Constrained Devices

- **Status**: ❌
- **Reason**: CV-QKD + 비이진 LDPC — 양자/QKD 및 비이진 모두 제외 대상
- **ID**: arxiv:2504.06384v1
- **Type**: preprint
- **Published**: 2025-04-08
- **Authors**: Panagiotis Papanastasiou, Carlo Ottaviani, Stefano Pirandola +2
- **PDF**: https://arxiv.org/pdf/2504.06384v1
- **Abstract**: Constrained devices, such as smart sensors, wearable devices, and Internet of Things nodes, are increasingly prevalent in society and rely on secure communications to function properly. These devices often operate autonomously, exchanging sensitive data or commands over short distances, such as within a room, house, or warehouse. In this context, continuous-variable quantum key distribution (CV-QKD) offers the highest secure key rate and the greatest versatility for integration into existing infrastructure. A key challenge in this setting, where devices have limited storage and processing capacity, is obtaining a realistic and tight estimate of the CV-QKD secure key rate within a composable security framework, with error correction (EC) consuming most of the storage and computational power. To address this, we focus on low-density parity-check (LDPC) codes with non-binary alphabets, which optimise mutual information and are particularly suited for short-distance communications. We develop a security framework to derive finite-size secret keys near the optimal EC leakage limit and model the related memory requirements for the encoding process in one-way error correction. This analysis facilitates the practical deployment of CV-QKD, particularly in constrained devices with limited storage and computational resources.

## Online Gaussian elimination for quantum LDPC decoding

- **Status**: ❌
- **Reason**: 양자 LDPC union-find용 온라인 가우스 소거 디코더, 양자 신드롬/클러스터 전용
- **ID**: arxiv:2504.05080v2
- **Type**: preprint
- **Published**: 2025-04-07
- **Authors**: Sam J. Griffiths, Asmae Benhemou, Dan E. Browne
- **PDF**: https://arxiv.org/pdf/2504.05080v2
- **Abstract**: Decoders for quantum LDPC codes generally rely on solving a parity-check equation with Gaussian elimination, with the generalised union-find decoder performing this repeatedly on growing clusters. We present an online variant of the Gaussian elimination algorithm which maintains an LUP decomposition in order to process only new rows and columns as they are added to a system of equations. This is equivalent to performing Gaussian elimination once on the final system of equations, in contrast to the multiple rounds of Gaussian elimination employed by the generalised union-find decoder. It thus significantly reduces the number of operations performed by the decoder. We consider the generalised union-find decoder as an example use case and present a complexity analysis demonstrating that both variants take time cubic in the number of qubits in the general case, but that the number of operations performed by the online variant is lower by an amount which itself scales cubically. This analysis is also extended to the regime of 'well-behaved' codes in which the number of growth iterations required is bounded logarithmically in error weight. Finally, we show empirically that our online variant outperforms the original offline decoder in average-case time complexity on codes with sparser parity-check matrices or greater covering radius.

## QUITS: A modular Qldpc code circUIT Simulator

- **Status**: ❌
- **Reason**: qLDPC 회로 시뮬레이터(hypergraph/lifted product, stabilizer) — 양자 전용
- **ID**: arxiv:2504.02673v2
- **Type**: preprint
- **Published**: 2025-04-03
- **Authors**: Mingyu Kang, Yingjia Lin, Hanwen Yao +3
- **PDF**: https://arxiv.org/pdf/2504.02673v2
- **Abstract**: To achieve quantum fault tolerance with lower overhead, quantum low-density parity-check (QLDPC) codes have emerged as a promising alternative to topological codes such as the surface code, offering higher code rates. To support their study, an end-to-end framework for simulating QLDPC codes at the circuit level is needed. In this work, we present QUITS, a modular and flexible circuit-level simulator for QLDPC codes. Its design allows users to freely combine LDPC code constructions, syndrome extraction circuits, decoding algorithms, and noise models, enabling comprehensive and customizable studies of the performance of QLDPC codes under circuit-level noise. QUITS supports several leading QLDPC families, including hypergraph product codes, lifted product codes, and balanced product codes. As part of the framework, we introduce a syndrome extraction circuit improved from Tremblay, Delfosse, and Beverland [Phys. Rev. Lett. 129, 050504 (2022)] that applies to all three code families. In particular, for a small hypergraph product code, our circuit achieves lower depth than the conventional method, resulting in improved logical performance. Using QUITS, we evaluate the performance of state-of-the-art QLDPC codes and decoders under various settings, revealing trade-offs between the decoding runtime and the logical failure rate. The source code of QUITS is available online.

## Linear Time Iterative Decoders for Hypergraph-Product and Lifted-Product Codes

- **Status**: ✅
- **Reason**: QLDPC 디코더지만 트래핑셋 회피 기법이 고전 부모 LDPC 디코더의 트래핑셋 회피에서 유래(classical TS, parent classical LDPC decoder)하고 그대로 이식 가능 — 예외적 포함 후보, Phase3 재검토
- **ID**: arxiv:2504.01728v1
- **Type**: preprint
- **Published**: 2025-04-02
- **Authors**: Asit Kumar Pradhan, Nithin Raveendran, Narayanan Rengaswamy +1
- **PDF**: https://arxiv.org/pdf/2504.01728v1
- **Abstract**: Quantum low-density parity-check (QLDPC) codes with asymptotically non-zero rates are prominent candidates for achieving fault-tolerant quantum computation, primarily due to their syndrome-measurement circuit's low operational depth. Numerous studies advocate for the necessity of fast decoders to fully harness the capabilities of QLDPC codes, thus driving the focus towards designing low-complexity iterative decoders. However, empirical investigations indicate that such iterative decoders are susceptible to having a high error floor while decoding QLDPC codes. The main objective of this paper is to analyze the decoding failures of the \emph{hypergraph-product} and \emph{lifted-product} codes and to design decoders that mitigate these failures, thus achieving a reduced error floor. The suboptimal performance of these codes can predominantly be ascribed to two structural phenomena: (1) stabilizer-induced trapping sets, which are subgraphs formed by stabilizers, and (2) classical trapping sets, which originate from the classical codes utilized in the construction of hypergraph-product and lifted-product codes. The dynamics of stabilizer-induced trapping sets is examined and a straightforward modification of iterative decoders is proposed to circumvent these trapping sets. Moreover, this work proposes a systematic methodology for designing decoders that can circumvent classical trapping sets in both hypergraph product and lifted product codes, from decoders capable of avoiding their trapping set in the parent classical LDPC code. When decoders that can avoid stabilizer-induced trapping sets are run in parallel with those that can mitigate the effect of classical TS, the logical error rate improves significantly in the error-floor region.
