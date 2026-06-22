# arXiv — 2025-04 (1차선별 통과)


## Subcode Ensemble Decoding of Polar Codes

- **Status**: ✅
- **Reason**: ScED(subcode ensemble decoding)는 본래 바이너리 LDPC용 디코더 기법, 이식 가능성 있어 Phase 3 재검토(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2504.17511v1
- **Type**: preprint
- **Published**: 2025-04-24
- **Authors**: Henning Lulei, Jonathan Mandelbaum, Marvin Rübenacke +3
- **PDF**: https://arxiv.org/pdf/2504.17511v1
- **Abstract**: In the short block length regime, pre-transformed polar codes together with successive cancellation list (SCL) decoding possess excellent error correction capabilities. However, in practice, the list size is limited due to the suboptimal scaling of the required area in hardware implementations. Automorphism ensemble decoding (AED) can improve performance for a fixed list size by running multiple parallel SCL decodings on permuted received words, yielding a list of estimates from which the final estimate is selected. Yet, AED is limited to appropriately designed polar codes. Subcode ensemble decoding (ScED) was recently proposed for low-density parity-check codes and does not impose such design constraints. It uses multiple decodings in different subcodes, ensuring that the selected subcodes jointly cover the original code. We extend ScED to polar codes by expressing polar subcodes through suitable pre-transformations (PTs). To this end, we describe a framework classifying pre-transformations for pre-transformed polar codes based on their role in encoding and decoding. Within this framework, we propose a new type of PT enabling ScED for polar codes, analyze its properties, and discuss how to construct an efficient ensemble.

## Linear Time Iterative Decoders for Hypergraph-Product and Lifted-Product Codes

- **Status**: ✅
- **Reason**: QLDPC 디코더지만 트래핑셋 회피 기법이 고전 부모 LDPC 디코더의 트래핑셋 회피에서 유래(classical TS, parent classical LDPC decoder)하고 그대로 이식 가능 — 예외적 포함 후보, Phase3 재검토
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2504.01728v1
- **Type**: preprint
- **Published**: 2025-04-02
- **Authors**: Asit Kumar Pradhan, Nithin Raveendran, Narayanan Rengaswamy +1
- **PDF**: https://arxiv.org/pdf/2504.01728v1
- **Abstract**: Quantum low-density parity-check (QLDPC) codes with asymptotically non-zero rates are prominent candidates for achieving fault-tolerant quantum computation, primarily due to their syndrome-measurement circuit's low operational depth. Numerous studies advocate for the necessity of fast decoders to fully harness the capabilities of QLDPC codes, thus driving the focus towards designing low-complexity iterative decoders. However, empirical investigations indicate that such iterative decoders are susceptible to having a high error floor while decoding QLDPC codes. The main objective of this paper is to analyze the decoding failures of the \emph{hypergraph-product} and \emph{lifted-product} codes and to design decoders that mitigate these failures, thus achieving a reduced error floor. The suboptimal performance of these codes can predominantly be ascribed to two structural phenomena: (1) stabilizer-induced trapping sets, which are subgraphs formed by stabilizers, and (2) classical trapping sets, which originate from the classical codes utilized in the construction of hypergraph-product and lifted-product codes. The dynamics of stabilizer-induced trapping sets is examined and a straightforward modification of iterative decoders is proposed to circumvent these trapping sets. Moreover, this work proposes a systematic methodology for designing decoders that can circumvent classical trapping sets in both hypergraph product and lifted product codes, from decoders capable of avoiding their trapping set in the parent classical LDPC code. When decoders that can avoid stabilizer-induced trapping sets are run in parallel with those that can mitigate the effect of classical TS, the logical error rate improves significantly in the error-floor region.
