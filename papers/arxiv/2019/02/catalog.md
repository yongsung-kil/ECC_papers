# arXiv — 2019-02


## Probabilistic Parity Shaping for Linear Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1902.10648v1
- **Type**: preprint
- **Published**: 2019-02-27
- **Authors**: Georg Böcherer, Diego Lentner, Alessandro Cirino +1
- **PDF**: https://arxiv.org/pdf/1902.10648v1
- **Abstract**: Linear layered probabilistic shaping (LLPS) is proposed, an architecture for linear codes to efficiently encode to shaped code words. In the previously proposed probabilistic amplitude shaping (PAS) architecture, a distribution matcher (DM) maps information bits to shaped bits, which are then systematically encoded by appending uniformly distributed parity bits. LLPS extends PAS by probabilistic parity shaping (PPS), which uses a syndrome DM to calculate shaped parity bits. LLPS enables the transmission with any desired distribution using linear codes, furthermore, by LLPS, a given linear code with rate $R_\text{fec}$ can be operated at any rate $R\leq R_\text{fec}$ by changing the distribution. LLPS is used with an LDPC code for dirty paper coding against an interfering BPSK signal, improving the energy efficiency by 0.8 dB.

## One and Two Bit Message Passing for SC-LDPC Codes with Higher-Order Modulation

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1902.10391v3
- **Type**: preprint
- **Published**: 2019-02-27
- **Authors**: Fabian Steiner, Emna Ben Yacoub, Balazs Matuz +2
- **PDF**: https://arxiv.org/pdf/1902.10391v3
- **Abstract**: Low complexity decoding algorithms are necessary to meet data rate requirements in excess of 1 Tbps. In this paper, we study one and two bit message passing algorithms for belief propagation decoding of low-density parity-check (LDPC) codes and analyze them by density evolution. The variable nodes (VNs) exploit soft information from the channel output. To decrease the data flow, the messages exchanged between check nodes (CNs) and VNs are represented by one or two bits. The newly proposed quaternary message passing (QMP) algorithm is compared asymptotically and in finite length simulations to binary message passing (BMP) and ternary message passing (TMP) for spectrally efficient communication with higher-order modulation and probabilistic amplitude shaping (PAS). To showcase the potential for high throughput forward error correction, spatially coupled LDPC codes and a target spectral efficiency (SE) of 3 bits/QAM symbol are considered. Gains of about 0.7 dB and 0.1 dB are observed compared to BMP and TMP, respectively. The gap to unquantized belief propagation (BP) decoding is reduced to about 0.75 dB. For smaller code rates, the gain of QMP compared to TMP is more pronounced and amounts to 0.24 dB in the considered example.

## Construction of QC-LDPC Codes with Low Error Floor by Efficient Systematic Search and Elimination of Trapping Sets

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1902.07332v3
- **Type**: preprint
- **Published**: 2019-02-19
- **Authors**: Bashirreza Karimi, Amir. H Banihashemi
- **PDF**: https://arxiv.org/pdf/1902.07332v3
- **Abstract**: We propose a systematic design of protograph-based quasi-cyclic (QC) low-density parity-check (LDPC) codes with low error floor. We first characterize the trapping sets of such codes and demonstrate that the QC structure of the code eliminates some of the trapping set structures that can exist in a code with the same degree distribution and girth but lacking the QC structure. Using this characterization, our design aims at eliminating a targeted collection of trapping sets. Considering the parent/child relationship between the trapping sets in the collection, we search for and eliminate those trapping sets that are in the collection but are not a child of any other trapping set in the collection. An efficient layered algorithm is designed for the search of these targeted trapping sets. Compared to the existing codes in the literature, the designed codes are superior in the sense that they are free of the same collection of trapping sets with a smaller block length, or a larger collection of trapping sets with the same block length. In addition, the efficiency of the search algorithm makes it possible to design codes with larger degrees which are free of trapping sets within larger ranges compared to the state-of-the-art.

## Multi-Matrix Post-Processing for Quantum Key Distribution

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: arxiv:1902.05263v1
- **Type**: preprint
- **Published**: 2019-02-14
- **Authors**: Chaohui Gao, Dong Jiang, Liangliang Lu +2
- **PDF**: https://arxiv.org/pdf/1902.05263v1
- **Abstract**: Post-processing is a significant step in quantum key distribution(QKD), which is used for correcting the quantum-channel noise errors and distilling identical corrected keys between two distant legitimate parties. Efficient error reconciliation protocol, which can lead to an increase in the secure key generation rate, is one of the main performance indicators of QKD setups. In this paper, we propose a multi-low-density parity-check codes based reconciliation scheme, which can provide remarkable perspectives for highly efficient information reconciliation. With testing our approach through data simulation, we show that the proposed scheme combining multi-syndrome-based error rate estimation allows a more accurate estimation about the error rate as compared with random sampling and single-syndrome estimation techniques before the error correction, as well as a significant increase in the efficiency of the procedure without compromising security and sacrificing reconciliation efficiency.
