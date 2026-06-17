# arXiv — 2007-10


## Codes from Zero-divisors and Units in Group Rings

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.5893v1
- **Type**: preprint
- **Published**: 2007-10-31
- **Authors**: Paul Hurley, Ted Hurley
- **PDF**: https://arxiv.org/pdf/0710.5893v1
- **Abstract**: We describe and present a new construction method for codes using encodings from group rings. They consist primarily of two types: zero-divisor and unit-derived codes. Previous codes from group rings focused on ideals; for example cyclic codes are ideals in the group ring over a cyclic group. The fresh focus is on the encodings themselves, which only under very limited conditions result in ideals. We use the result that a group ring is isomorphic to a certain well-defined ring of matrices, and thus every group ring element has an associated matrix. This allows matrix algebra to be used as needed in the study and production of codes, enabling the creation of standard generator and check matrices. Group rings are a fruitful source of units and zero-divisors from which new codes result. Many code properties, such as being LDPC or self-dual, may be expressed as properties within the group ring thus enabling the construction of codes with these properties. The methods are general enabling the construction of codes with many types of group rings. There is no restriction on the ring and thus codes over the integers, over matrix rings or even over group rings themselves are possible and fruitful.

## LDPC-Based Iterative Algorithm for Compression of Correlated Sources at Rates Approaching the Slepian-Wolf Bound

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.5640v1
- **Type**: preprint
- **Published**: 2007-10-30
- **Authors**: F. Daneshgaran, Massimiliano Laddomada, M. Mondin
- **PDF**: https://arxiv.org/pdf/0710.5640v1
- **Abstract**: This article proposes a novel iterative algorithm based on Low Density Parity Check (LDPC) codes for compression of correlated sources at rates approaching the Slepian-Wolf bound. The setup considered in the article looks at the problem of compressing one source at a rate determined based on the knowledge of the mean source correlation at the encoder, and employing the other correlated source as side information at the decoder which decompresses the first source based on the estimates of the actual correlation. We demonstrate that depending on the extent of the actual source correlation estimated through an iterative paradigm, significant compression can be obtained relative to the case the decoder does not use the implicit knowledge of the existence of correlation.

## Generalized reliability-based syndrome decoding for LDPC codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.5230v2
- **Type**: preprint
- **Published**: 2007-10-27
- **Authors**: Guangwen Li, Guangzeng Feng
- **PDF**: https://arxiv.org/pdf/0710.5230v2
- **Abstract**: Aiming at bridging the gap between the maximum likelihood decoding (MLD) and the suboptimal iterative decodings for short or medium length LDPC codes, we present a generalized ordered statistic decoding (OSD) in the form of syndrome decoding, to cascade with the belief propagation (BP) or enhanced min-sum decoding. The OSD is invoked only when the decoding failures are obtained for the preceded iterative decoding method. With respect to the existing OSD which is based on the accumulated log-likelihood ratio (LLR) metric, we extend the accumulative metric to the situation where the BP decoding is in the probability domain. Moreover, after generalizing the accumulative metric to the context of the normalized or offset min-sum decoding, the OSD shows appealing tradeoff between performance and complexity. In the OSD implementation, when deciding the true error pattern among many candidates, an alternative proposed proves to be effective to reduce the number of real additions without performance loss. Simulation results demonstrate that the cascade connection of enhanced min-sum and OSD decodings outperforms the BP alone significantly, in terms of either performance or complexity.

## Message passing for the coloring problem: Gallager meets Alon and Kahale

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.3928v1
- **Type**: preprint
- **Published**: 2007-10-21
- **Authors**: Sonny Ben-Shimon, Dan Vilenchik
- **PDF**: https://arxiv.org/pdf/0710.3928v1
- **Abstract**: Message passing algorithms are popular in many combinatorial optimization problems. For example, experimental results show that {\em survey propagation} (a certain message passing algorithm) is effective in finding proper $k$-colorings of random graphs in the near-threshold regime. In 1962 Gallager introduced the concept of Low Density Parity Check (LDPC) codes, and suggested a simple decoding algorithm based on message passing. In 1994 Alon and Kahale exhibited a coloring algorithm and proved its usefulness for finding a $k$-coloring of graphs drawn from a certain planted-solution distribution over $k$-colorable graphs. In this work we show an interpretation of Alon and Kahale's coloring algorithm in light of Gallager's decoding algorithm, thus showing a connection between the two problems - coloring and decoding. This also provides a rigorous evidence for the usefulness of the message passing paradigm for the graph coloring problem. Our techniques can be applied to several other combinatorial optimization problems and networking-related issues.

## Error Correction Capability of Column-Weight-Three LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.3427v1
- **Type**: preprint
- **Published**: 2007-10-18
- **Authors**: Shashi Kiran Chilappagari, Bane Vasic
- **PDF**: https://arxiv.org/pdf/0710.3427v1
- **Abstract**: In this paper, we investigate the error correction capability of column-weight-three LDPC codes when decoded using the Gallager A algorithm. We prove that the necessary condition for a code to correct $k \geq 5$ errors is to avoid cycles of length up to $2k$ in its Tanner graph. As a consequence of this result, we show that given any $α>0, \exists N $ such that $\forall n>N$, no code in the ensemble of column-weight-three codes can correct all $αn$ or fewer errors. We extend these results to the bit flipping algorithm.

## Fast Reliability-based Algorithm of Finding Minimum-weight Codewords for LDPC Codes

- **Status**: 미선별
- **Reason**: N/A
- **ID**: arxiv:0710.1589v1
- **Type**: preprint
- **Published**: 2007-10-08
- **Authors**: Guangwen Li, Guangzeng Feng
- **PDF**: https://arxiv.org/pdf/0710.1589v1
- **Abstract**: Despite the NP hardness of acquiring minimum distance $d_m$ for linear codes theoretically, in this paper we propose one experimental method of finding minimum-weight codewords, the weight of which is equal to $d_m$ for LDPC codes. One existing syndrome decoding method, called serial belief propagation (BP) with ordered statistic decoding (OSD), is adapted to serve our purpose. We hold the conjecture that among many candidate error patterns in OSD reprocessing, modulo 2 addition of the lightest error pattern with one of the left error patterns may generate a light codeword. When the decoding syndrome changes to all-zero state, the lightest error pattern reduces to all-zero, the lightest non-zero error pattern is a valid codeword to update lightest codeword list.   Given sufficient codewords sending, the survived lightest codewords are likely to be the target. Compared with existing techniques, our method demonstrates its efficiency in the simulation of several interested LDPC codes.
