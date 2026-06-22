# arXiv — 2019-02 (1차선별 통과)


## One and Two Bit Message Passing for SC-LDPC Codes with Higher-Order Modulation

- **Status**: ✅
- **Reason**: 1/2비트 메시지패싱 BP 디코더(QMP/TMP/BMP), 밀도진화 분석 — 저비트 양자화 메시지패싱 디코더는 NAND LDPC HW에 이식 가능(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1902.10391v3
- **Type**: preprint
- **Published**: 2019-02-27
- **Authors**: Fabian Steiner, Emna Ben Yacoub, Balazs Matuz +2
- **PDF**: https://arxiv.org/pdf/1902.10391v3
- **Abstract**: Low complexity decoding algorithms are necessary to meet data rate requirements in excess of 1 Tbps. In this paper, we study one and two bit message passing algorithms for belief propagation decoding of low-density parity-check (LDPC) codes and analyze them by density evolution. The variable nodes (VNs) exploit soft information from the channel output. To decrease the data flow, the messages exchanged between check nodes (CNs) and VNs are represented by one or two bits. The newly proposed quaternary message passing (QMP) algorithm is compared asymptotically and in finite length simulations to binary message passing (BMP) and ternary message passing (TMP) for spectrally efficient communication with higher-order modulation and probabilistic amplitude shaping (PAS). To showcase the potential for high throughput forward error correction, spatially coupled LDPC codes and a target spectral efficiency (SE) of 3 bits/QAM symbol are considered. Gains of about 0.7 dB and 0.1 dB are observed compared to BMP and TMP, respectively. The gap to unquantized belief propagation (BP) decoding is reduced to about 0.75 dB. For smaller code rates, the gain of QMP compared to TMP is more pronounced and amounts to 0.24 dB in the considered example.

## Construction of QC-LDPC Codes with Low Error Floor by Efficient Systematic Search and Elimination of Trapping Sets

- **Status**: ✅
- **Reason**: protograph QC-LDPC trapping set 제거로 low error floor 코드 설계 — 바이너리 코드 구성/error floor(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1902.07332v3
- **Type**: preprint
- **Published**: 2019-02-19
- **Authors**: Bashirreza Karimi, Amir. H Banihashemi
- **PDF**: https://arxiv.org/pdf/1902.07332v3
- **Abstract**: We propose a systematic design of protograph-based quasi-cyclic (QC) low-density parity-check (LDPC) codes with low error floor. We first characterize the trapping sets of such codes and demonstrate that the QC structure of the code eliminates some of the trapping set structures that can exist in a code with the same degree distribution and girth but lacking the QC structure. Using this characterization, our design aims at eliminating a targeted collection of trapping sets. Considering the parent/child relationship between the trapping sets in the collection, we search for and eliminate those trapping sets that are in the collection but are not a child of any other trapping set in the collection. An efficient layered algorithm is designed for the search of these targeted trapping sets. Compared to the existing codes in the literature, the designed codes are superior in the sense that they are free of the same collection of trapping sets with a smaller block length, or a larger collection of trapping sets with the same block length. In addition, the efficiency of the search algorithm makes it possible to design codes with larger degrees which are free of trapping sets within larger ranges compared to the state-of-the-art.
