# IEEE Xplore — 2026-02 (1차선별 통과)


## BayesBB: A 9.6-Gb/s 1.61-ms Configurable All-Message-Passing Baseband-Accelerator for B5G/6G Cell-Free Massive-MIMO Systems

- **Status**: ✅
- **Reason**: 구성가능 메시지패싱 디코더 HW(LDPC/polar 언폴디드 아키텍처) — HW 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:11045284
- **Type**: journal
- **Published**: Feb. 2026
- **Authors**: Yi Zhang, Wenyue Zhou, Yiwei Zhang +4
- **PDF**: https://ieeexplore.ieee.org/document/11045284
- **Abstract**: Cell-free massive multi-input multi-output (CF-mMIMO) has emerged as a promising alternative for the forthcoming beyond 5G and 6G (B5G/6G) systems. As an imperative part of supporting B5G/6G applications, baseband (BB) chips encounter more challenging key performance indicator (KPI) requirements. To achieve the B5G/6G goal of higher than 8-Gb/s/user throughput, less than 2-ms latency, and configurable hardware, a Bayesian inference-based all-message-passing baseband-accelerator (BayesBB) is presented in this article. Benefiting from the pipelined and fully unfolded all-message-passing architecture, BayesBB delivers three unexplored merits: high throughput (9.6-Gb/s), low latency (1.61-ms), and good configurability. Specifically, a ten-gigabit ethernet (XGE) interface with 10.3125-Gb/s SerDes is used, resulting in 9.6-Gb/s throughput. A fully unfolded MIMO-BP detector achieves a detection latency of 1.44-ms, contributing to chip latency of 1.61-ms. A configurable architecture is designed, supporting various B5G/6G applications, for example, the decoding of both 3GPP low-density parity-check (LDPC) codes and polar codes. As a system-level implementation, tests have verified that 16 arrays of BayesBB can handle the BB processing of a  $128 \times 128$  CF-mMIMO system with commercial setups, delivering 9.6-Gb/s throughput and >100-b/s/Hz spectrum efficiency (SE).

## Fully Parallelized BP Decoding for Quantum LDPC Codes Can Outperform BP-OSD

- **Status**: ✅
- **Reason**: qLDPC지만 완전병렬 BP 디코더+Chase식 speculative post-processing으로 Gaussian elimination 제거, 디코더 알고리즘/병렬 HW가 명확히 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11408621
- **Type**: conference
- **Published**: 31 Jan.-4 
- **Authors**: Ming Wang, Ang Li, Frank Mueller
- **PDF**: https://ieeexplore.ieee.org/document/11408621
- **Abstract**: This work presents a hardware-efficient and fully parallelizable decoder for quantum LDPC codes that leverages belief propagation (BP) with a speculative post-processing strategy inspired by classical Chase decoding algorithm. By monitoring bit-level oscillation patterns during BP, our method identifies unreliable bits and generates multiple candidate vectors to selectively flip syndromes. Each modified syndrome is then decoded independently using short-depth BP, a process we refer to as BP-SF (syndrome flip). This design eliminates the need for costly Gaussian elimination used in the current BP-OSD approaches. Our implementation achieves logical error rates comparable to or better than BP-OSD while offering significantly lower latency due to its high degree of parallelism for a variety of bivariate bicycle codes. Evaluation on the $\llbracket 144,12,12 \rrbracket$ bivariate bicycle code shows that the proposed decoder reduces average latency to approximately 70% of BP-OSD. When post-processing is parallelized the average latency is reduced by 55% compared to the single process implementation, with the maximum latency reaching as low as 18%. These advantages make it particularly well-suited for real-time and resource-constrained quantum error correction systems.

## Graph Neural Network Approaches to LDPC Decoding in 5G/6G Communications

- **Status**: ✅
- **Reason**: GNN 기반 LDPC 디코딩 — Tanner 그래프 구조 학습형 메시지 패싱(MLP/GRU/LSTM), 오류 바닥 완화 및 지연 감소, 이식 가능한 신경망 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:11460731
- **Type**: conference
- **Published**: 17-21 Feb.
- **Authors**: Juliy Boiko, Ilya Pyatin, Volodymir Druzhynin
- **PDF**: https://ieeexplore.ieee.org/document/11460731
- **Abstract**: This paper investigates Graph Neural Network (GNN)–based decoding of Low-Density Parity-Check (LDPC) codes for fifth- and sixth-generation (5G/6G) communication systems. Classical decoding algorithms, such as Belief Propagation (BP) and Min-Sum (MS), perform well under ideal conditions but degrade in the presence of channel fading, noise, and hardware nonlinearities. GNN-based decoders exploit the Tanner graph structure of LDPC codes, replacing fixed message-passing rules with trainable neural layers, including Multilayer Perceptrons (MLPs), Gated Recurrent Units (GRUs), and Long Short-Term Memory (LSTM) networks. Simulation results obtained using benchmark and 5G New Radio (NR) LDPC codes over Additive White Gaussian Noise (AWGN) and Rayleigh fading channels demonstrate that GNN decoders achieve improved Bit Error Rate (BER) and Block Error Rate (BLER) performance, mitigate error floor effects, and reduce decoding latency and computational complexity compared with BP, MS, and Normalized Min-Sum (NMS) decoders. Consequently, GNN-based LDPC decoding emerges as an adaptive and efficient solution for ultra-reliable low-latency communication in next-generation wireless networks.
