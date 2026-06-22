# arXiv — 2019-09 (1차선별 통과)


## Hyper-Graph-Network Decoders for Block Codes

- **Status**: ✅
- **Reason**: 그래프 신경망 기반 메시지패싱 디코더로 LDPC 포함 vanilla BP 능가, 부호 비의존 신경망 디코더(C) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1909.09036v2
- **Type**: preprint
- **Published**: 2019-09-05
- **Authors**: Eliya Nachmani, Lior Wolf
- **PDF**: https://arxiv.org/pdf/1909.09036v2
- **Abstract**: Neural decoders were shown to outperform classical message passing techniques for short BCH codes. In this work, we extend these results to much larger families of algebraic block codes, by performing message passing with graph neural networks. The parameters of the sub-network at each variable-node in the Tanner graph are obtained from a hypernetwork that receives the absolute values of the current message as input. To add stability, we employ a simplified version of the arctanh activation that is based on a high order Taylor approximation of this activation function. Our results show that for a large number of algebraic block codes, from diverse families of codes (BCH, LDPC, Polar), the decoding obtained with our method outperforms the vanilla belief propagation method as well as other learning techniques from the literature.
