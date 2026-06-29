# arXiv — 2019-03


## Modified belief propagation decoders for quantum low-density parity-check codes

- **Status**: ❌
- **Reason**: GF(4) 비이진 BP 기반 양자 LDPC 디코더 — 비이진 LDPC + 양자 특유 degenerate/CSS 의존, 바이너리 NAND ECC 이식 부적합
- **ID**: arxiv:1903.07404v2
- **Type**: preprint
- **Published**: 2019-03-18
- **Authors**: Alex Rigby, JC Olivier, Peter Jarvis
- **PDF**: https://arxiv.org/pdf/1903.07404v2
- **Abstract**: Quantum low-density parity-check codes can be decoded using a syndrome based $\mathrm{GF}(4)$ belief propagation decoder. However, the performance of this decoder is limited both by unavoidable $4$-cycles in the code's factor graph and the degenerate nature of quantum errors. For the subclass of CSS codes, the number of $4$-cycles can be reduced by breaking an error into an $X$ and $Z$ component and decoding each with an individual $\mathrm{GF}(2)$ based decoder. However, this comes at the expense of ignoring potential correlations between these two error components. We present a number of modified belief propagation decoders that address these issues. We propose a $\mathrm{GF}(2)$ based decoder for CSS codes that reintroduces error correlations by reattempting decoding with adjusted error probabilities. We also propose the use of an augmented decoder, which has previously been suggested for classical binary low-density parity-check codes. This decoder iteratively reattempts decoding on factor graphs that have a subset of their check nodes duplicated. The augmented decoder can be based on a $\mathrm{GF}(4)$ decoder for any code, a $\mathrm{GF}(2)$ decoder for CSS code, or even a supernode decoder for a dual-containing CSS code. For CSS codes, we further propose a $\mathrm{GF}(2)$ based decoder that combines the augmented decoder with error probability adjustment. We demonstrate the performance of these new decoders on a range of different codes, showing that they perform favorably compared to other decoders presented in literature.

## Outage-Limit-Approaching Protograph LDPC Codes for Slow-Fading Wireless Communications

- **Status**: ❌
- **Reason**: slow-fading용 root-protograph QC-LDPC 리뷰 — 무선 특이적 + 서베이 성격, 신규 디코더/HW 기여 없음
- **ID**: arxiv:1903.01223v2
- **Type**: preprint
- **Published**: 2019-03-04
- **Authors**: Yi Fang, Pingping Chen, Guofa Cai +3
- **PDF**: https://arxiv.org/pdf/1903.01223v2
- **Abstract**: Block-fading (BF) channel, also known as slow-fading channel, is a type of simple and practical channel model that can characterize the primary feature of a number of wireless-communication applications with low to moderate mobility. Although the BF channel has received significant research attention in the past twenty years, designing low-complexity outage-limit-approaching error-correction codes (ECCs) is still a challenging issue. For this reason, a novel family of protograph low-density parity-check (LDPC) codes, called root-protograph (RP) LDPC codes, has been conceived recently. The RP codes can not only realize linear-complexity encoding and high-speed decoding with the help of a quasi-cyclic (QC) structure, but also achieve near-outage-limit performance in a variety of BF scenarios. In this article, we briefly review the design guidelines of such protograph codes with the aim of inspiring further research activities in this area.
