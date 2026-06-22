# arXiv — 2024-12 (1차선별 통과)


## Spiking Neural Belief Propagation Decoder for LDPC Codes with Small Variable Node Degrees

- **Status**: ✅
- **Reason**: C: SNN 기반 BP 디코더(ML-ELENA-SNN)는 CN update를 신경망으로 근사하는 새 디코더 알고리즘 — 바이너리 LDPC 대상, NAND에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2412.15897v1
- **Type**: preprint
- **Published**: 2024-12-20
- **Authors**: Alexander von Bank, Eike-Manuel Edelmann, Jonathan Mandelbaum +1
- **PDF**: https://arxiv.org/pdf/2412.15897v1
- **Abstract**: Spiking neural networks (SNNs) promise energy-efficient data processing by imitating the event-based behavior of biological neurons. In previous work, we introduced the enlarge-likelihood-each-notable-amplitude spiking-neural-network (ELENA-SNN) decoder, a novel decoding algorithm for low-density parity-check (LDPC) codes. The decoder integrates SNNs into belief propagation (BP) decoding by approximating the check node (CN) update equation using SNNs. However, when decoding LDPC codes with a small variable node(VN) degree, the approximation gets too rough, and the ELENA-SNN decoder does not yield good results. This paper introduces the multi-level ELENA-SNN (ML-ELENA-SNN) decoder, which is an extension of the ELENA-SNN decoder. Instead of a single SNN approximating the CN update, multiple SNNs are applied in parallel, resulting in a higher resolution and higher dynamic range of the exchanged messages. We show that the ML-ELENA-SNN decoder performs similarly to the ubiquitous normalized min-sum decoder for the (38400, 30720) regular LDPC code with a VN degree of dv = 3 and a CN degree of dc = 15.

## Quantum-enhanced belief propagation for LDPC decoding

- **Status**: ✅
- **Reason**: C: QAOA를 BP 전처리로 쓰는 새 디코더(QEBP) — 고전 바이너리 LDPC 디코딩 대상, BP 수렴/BLER 개선 기법 이식 검토 여지(애매하여 살림)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2412.08596v1
- **Type**: preprint
- **Published**: 2024-12-11
- **Authors**: Sheila M. Perez-Garcia, Ashley Montanaro
- **PDF**: https://arxiv.org/pdf/2412.08596v1
- **Abstract**: Decoding low-density parity-check codes is critical in many current technologies, such as fifth-generation (5G) wireless networks and satellite communications. The belief propagation algorithm allows for fast decoding due to the low density of these codes. However, there is scope for improvement to this algorithm both in terms of its computational cost when decoding large codes and its error-correcting abilities. Here, we introduce the quantum-enhanced belief propagation (QEBP) algorithm, in which the Quantum Approximate Optimization Algorithm (QAOA) acts as a pre-processing step to belief propagation. We perform exact simulations of syndrome decoding with QAOA, whose result guides the belief propagation algorithm, leading to faster convergence and a lower block error rate (BLER). In addition, through the repetition code, we study the possibility of having shared variational parameters between syndromes and, in this case, code lengths. We obtain a unique pair of variational parameters for level-1 QAOA by optimizing the probability of successful decoding through a transfer matrix method. Then, using these parameters, we compare the scaling of different QAOA post-processing techniques with code length.

## On the lifting degree of girth-8 QC-LDPC codes

- **Status**: ✅
- **Reason**: E: girth-8 QC-LDPC lifting degree 하한 개선 및 결정론적 구성 — 바이너리 코드 설계 새 기여, NAND LDPC 구성에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2412.02526v1
- **Type**: preprint
- **Published**: 2024-12-03
- **Authors**: Haoran Xiong, Guanghui Wang, Zhiming Ma +1
- **PDF**: https://arxiv.org/pdf/2412.02526v1
- **Abstract**: The lifting degree and the deterministic construction of quasi-cyclic low-density parity-check (QC-LDPC) codes have been extensively studied, with many construction methods in the literature, including those based on finite geometry, array-based codes, computer search, and combinatorial techniques. In this paper, we focus on the lifting degree $p$ required for achieving a girth of 8 in $(3,L)$ fully connected QC-LDPC codes, and we propose an improvement over the classical lower bound $p\geq 2L-1$, enhancing it to $p\geq \sqrt{5L^2-11L+\frac{13}{2}}+\frac{1}{2}$. Moreover, we demonstrate that for girth-8 QC-LDPC codes containing an arithmetic row in the exponent matrix, a necessary condition for achieving a girth of 8 is $p\geq \frac{1}{2}L^2+\frac{1}{2}L$. Additionally, we present a corresponding deterministic construction of $(3,L)$ QC-LDPC codes with girth 8 for any $p\geq \frac{1}{2}L^2+\frac{1}{2}L+\lfloor \frac{L-1}{2}\rfloor$, which approaches the lower bound of $\frac{1}{2}L^2+\frac{1}{2}L$. Under the same conditions, this construction achieves a smaller lifting degree compared to prior methods. To the best of our knowledge, the proposed order of lifting degree matches the smallest known, on the order of $\frac{1}{2}L^2+\mathcal{O} (L)$.
