# arXiv — 2010-02 (1차선별 통과)


## Lowering the Error Floor of LDPC Codes Using Cyclic Liftings

- **Status**: ✅
- **Reason**: cyclic lifting으로 trapping set·짧은 사이클 제거하여 error floor 개선 — 바이너리 LDPC 코드설계 기법(E), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1002.4311v1
- **Type**: preprint
- **Published**: 2010-02-23
- **Authors**: Reza Asvadi, Amir H. Banihashemi, Mahmoud Ahmadian-Attari
- **PDF**: https://arxiv.org/pdf/1002.4311v1
- **Abstract**: Cyclic liftings are proposed to lower the error floor of low-density parity-check (LDPC) codes. The liftings are designed to eliminate dominant trapping sets of the base code by removing the short cycles which form the trapping sets. We derive a necessary and sufficient condition for the cyclic permutations assigned to the edges of a cycle $c$ of length $\ell(c)$ in the base graph such that the inverse image of $c$ in the lifted graph consists of only cycles of length strictly larger than $\ell(c)$. The proposed method is universal in the sense that it can be applied to any LDPC code over any channel and for any iterative decoding algorithm. It also preserves important properties of the base code such as degree distributions, encoder and decoder structure, and in some cases, the code rate. The proposed method is applied to both structured and random codes over the binary symmetric channel (BSC). The error floor improves consistently by increasing the lifting degree, and the results show significant improvements in the error floor compared to the base code, a random code of the same degree distribution and block length, and a random lifting of the same degree. Similar improvements are also observed when the codes designed for the BSC are applied to the additive white Gaussian noise (AWGN) channel.

## Static Address Generation Easing: a Design Methodology for Parallel Interleaver Architectures

- **Status**: ✅
- **Reason**: 병렬 인터리버 아키텍처 충돌없는 메모리 매핑 기법 — LDPC 병렬 디코더 HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1002.3990v1
- **Type**: preprint
- **Published**: 2010-02-21
- **Authors**: Cyrille Chavet, Philippe Coussy, Eric Martin +1
- **PDF**: https://arxiv.org/pdf/1002.3990v1
- **Abstract**: For high throughput applications, turbo-like iterative decoders are implemented with parallel architectures. However, to be efficient parallel architectures require to avoid collision accesses i.e. concurrent read/write accesses should not target the same memory block. This consideration applies to the two main classes of turbo-like codes which are Low Density Parity Check (LDPC) and Turbo-Codes. In this paper we propose a methodology which finds a collision-free mapping of the variables in the memory banks and which optimizes the resulting interleaving architecture. Finally, we show through a pedagogical example the interest of our approach compared to state-of-the-art techniques.
