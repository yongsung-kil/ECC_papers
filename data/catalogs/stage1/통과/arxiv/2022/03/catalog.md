# arXiv — 2022-03 (1차선별 통과)


## A Unified Spatially Coupled Code Design: Threshold, Cycles, and Locality

- **Status**: ✅
- **Reason**: SC-LDPC 부호 설계 통합 프레임워크(threshold+cycle 동시 최적화, partitioning matrix 탐색) — 새 바이너리 코드설계 기여(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2203.02052v3
- **Type**: preprint
- **Published**: 2022-03-03
- **Authors**: Homa Esfahanizadeh, Eshed Ram, Yuval Cassuto +1
- **PDF**: https://arxiv.org/pdf/2203.02052v3
- **Abstract**: Spatially-Coupled (SC)-LDPC codes are known to have outstanding error-correction performance and low decoding latency. Whereas previous works on LDPC and SC-LDPC codes mostly take either an asymptotic or a finite-length design approach, in this paper we present a unified framework for jointly optimizing the codes' thresholds and cycle counts to address both regimes. The framework is based on efficient traversal and pruning of the code search space, building on the fact that the performance of a protograph-based SC-LDPC code depends on some characteristics of the code's partitioning matrix, which by itself is much smaller than the code's full parity-check matrix. We then propose an algorithm that traverses all nonequivalent partitioning matrices, and outputs a list of codes, each offering an attractive point on the trade-off between asymptotic and finite-length performance. We further extend the framework to designing SC-LDPC codes with sub-block locality, which is a recently introduced feature offering fast access to sub-blocks within the code block. Our simulations show that our framework results in SC-LDPC codes that outperform the state-of-the-art constructions, and that it offers the flexibility to choose low-SNR, high-SNR, or in-between SNR region as the primary design target.
