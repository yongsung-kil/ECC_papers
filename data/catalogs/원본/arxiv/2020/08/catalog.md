# arXiv — 2020-08


## Construction of LDPC convolutional codes via difference triangle sets

- **Status**: ✅
- **Reason**: difference triangle set 기반 LDPC convolutional 코드 구성 + 사이클/absorbing set 제거 — SC-LDPC 코드설계 기법 이식 가능(E)
- **ID**: arxiv:2008.13470v1
- **Type**: preprint
- **Published**: 2020-08-31
- **Authors**: Gianira N. Alfarano, Julia Lieb, Joachim Rosenthal
- **PDF**: https://arxiv.org/pdf/2008.13470v1
- **Abstract**: In this paper, a construction of $(n,k,δ)$ LDPC convolutional codes over arbitrary finite fields, which generalizes the work of Robinson and Bernstein and the later work of Tong is provided. The sets of integers forming a $(k,w)$-(weak) difference triangle set are used as supports of some columns of the sliding parity-check matrix of an $(n,k,δ)$ convolutional code, where $n\in\mathbb{N}$, $n>k$. The parameters of the convolutional code are related to the parameters of the underlying difference triangle set. In particular, a relation between the free distance of the code and $w$ is established as well as a relation between the degree of the code and the scope of the difference triangle set. Moreover, we show that some conditions on the weak difference triangle set ensure that the Tanner graph associated to the sliding parity-check matrix of the convolutional code is free from $2\ell$-cycles not satisfying the full rank condition over any finite field. Finally, we relax these conditions and provide a lower bound on the field size, depending on the parity of $\ell$, that is sufficient to still avoid $2\ell$-cycles. This is important for improving the performance of a code and avoiding the presence of low-weight codewords and absorbing sets.

## Transmitting Extra Bits by Rotating Signal Constellations

- **Status**: ❌
- **Reason**: 회전 성상도로 추가비트 전송하는 변조 기법 — LDPC는 페이로드 부호일 뿐 떼어낼 ECC 기법 없는 통신 응용
- **ID**: arxiv:2008.10818v2
- **Type**: preprint
- **Published**: 2020-08-25
- **Authors**: Jiachen Sun, Hao Liu, Xiao Ma
- **PDF**: https://arxiv.org/pdf/2008.10818v2
- **Abstract**: In this letter, we propose a novel LDPC coding scheme to transmit extra bits aided by rotated signal constellations without any additional cost in transmission power or bandwidth. In the proposed scheme, the LDPC coded data are modulated by a rotated two-dimensional signal constellation, in which the rotation angle is specified by the given extra bits. At the receiver, the rotation angle is estimated with the aid of the statistical learning of the syndrome of the LDPC code. After recovering the rotation angle, the coded payload data can be decoded by the LDPC decoder. The simulation results show that, for an LDPC code of length 2304, up to four extra bits can be transmitted with negligible influence on the reliability of the LDPC coded data.

## New Cosystolic Expanders from Tensors Imply Explicit Quantum LDPC Codes with $Ω(\sqrt{n}\log^kn)$ Distance

- **Status**: ❌
- **Reason**: 양자 LDPC(qLDPC) 부호 구성을 위한 cosystolic expander/Ramanujan complex 이론. 고전 바이너리 LDPC로 이식 불가한 양자 전용 개념.
- **ID**: arxiv:2008.09495v2
- **Type**: preprint
- **Published**: 2020-08-21
- **Authors**: Tali Kaufman, Ran J. Tessler
- **PDF**: https://arxiv.org/pdf/2008.09495v2
- **Abstract**: In this work we introduce a new notion of expansion in higher dimensions that is stronger than the well studied cosystolic expansion notion, and is termed {\em Collective-cosystolic expansion}.   We show that tensoring two cosystolic expanders yields a new cosystolic expander, assuming one of the complexes in the product, is not only cosystolic expander, but rather a collective cosystolic expander.   We then show that the well known bounded degree cosystolic expanders, the Ramanujan complexes are, in fact, collective cosystolic expanders. This enables us to construct new bounded degree cosystolic expanders, by tensoring of Ramanujan complexes.   Using our new constructed bounded degree cosystolic expanders we construct {\em explicit} quantum LDPC codes of distance $\sqrt{n} \log^k n$ for any $k$, improving a recent result of Evra et. al. \cite{EKZ}, and setting a new record for distance of explicit quantum LDPC codes.   The work of \cite{EKZ} took advantage of the high dimensional expansion notion known as cosystolic expansion, that occurs in Ramanujan complexes. Our improvement is achieved by considering tensor product of Ramanujan complexes, and using their newly derived property, the collective cosystolic expansion.
