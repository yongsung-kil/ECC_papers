# arXiv — 2020-03 (1차선별 통과)


## Neural Enhanced Belief Propagation on Factor Graphs

- **Status**: ✅
- **Reason**: 신경망 강화 BP(FG-GNN이 BP 메시지 보정), bursty 채널 LDPC 디코딩 개선 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2003.01998v5
- **Type**: preprint
- **Published**: 2020-03-04
- **Authors**: Victor Garcia Satorras, Max Welling
- **PDF**: https://arxiv.org/pdf/2003.01998v5
- **Abstract**: A graphical model is a structured representation of locally dependent random variables. A traditional method to reason over these random variables is to perform inference using belief propagation. When provided with the true data generating process, belief propagation can infer the optimal posterior probability estimates in tree structured factor graphs. However, in many cases we may only have access to a poor approximation of the data generating process, or we may face loops in the factor graph, leading to suboptimal estimates. In this work we first extend graph neural networks to factor graphs (FG-GNN). We then propose a new hybrid model that runs conjointly a FG-GNN with belief propagation. The FG-GNN receives as input messages from belief propagation at every inference iteration and outputs a corrected version of them. As a result, we obtain a more accurate algorithm that combines the benefits of both belief propagation and graph neural networks. We apply our ideas to error correction decoding tasks, and we show that our algorithm can outperform belief propagation for LDPC codes on bursty channels.

## Binary Representaion for Non-binary LDPC Code with Decoder Design

- **Status**: ✅
- **Reason**: 비이진 LDPC의 바이너리 이미지 cycle 제거(EPR-LDPC)와 바이너리 디코더 설계 — 대상이 바이너리 parity-check cycle 제거 기법(E)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2003.00734v1
- **Type**: preprint
- **Published**: 2020-03-02
- **Authors**: Yang Yu, Wen Chen, Jun Li +2
- **PDF**: https://arxiv.org/pdf/2003.00734v1
- **Abstract**: The equivalent binary parity check matrices for the binary images of the cycle-free non-binary LDPC codes have numerous bit-level cycles. In this paper, we show how to transform these binary parity check matrices into their cycle-free forms. It is shown that the proposed methodology can be adopted not only for the binary images of non-binary LDPC codes but also for a large class of binary LDPC codes. Specifically, we present an extended $p$-reducible (EPR) LDPC code structure to eliminate the bit-level cycles. For the non-binary LDPC codes with short length symbol-level cycles, the EPR-LDPC codes can largely avoid the corresponding short length bit-level cycles. As to the decoding of the EPR-LDPC codes, we propose a hybrid hard-decision decoder and a hybrid parallel decoder for binary symmetric channel and binary input Gaussian channel, respectively. A simple code optimization algorithm for these binary decoders is also provided. Simulations show the comparative results and justify the advantages, i.e., better performance and lower decoding complexity, of the proposed binary constructions.
