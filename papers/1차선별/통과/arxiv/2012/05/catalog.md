# arXiv — 2012-05 (1차선별 통과)


## Blind Reconciliation

- **Status**: ✅
- **Reason**: QKD reconciliation이나 short-length LDPC + blind(사전 에러율 추정 불필요) 저상호작용 프로토콜 + 고처리량 HW 구현 지향, 떼어낼 디코더/HW 기법(C/D) 예외 포함
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1205.5729v2
- **Type**: preprint
- **Published**: 2012-05-25
- **Authors**: Jesus Martinez-Mateo, David Elkouss, Vicente Martin
- **PDF**: https://arxiv.org/pdf/1205.5729v2
- **Abstract**: Information reconciliation is a crucial procedure in the classical post-processing of quantum key distribution (QKD). Poor reconciliation efficiency, revealing more information than strictly needed, may compromise the maximum attainable distance, while poor performance of the algorithm limits the practical throughput in a QKD device. Historically, reconciliation has been mainly done using close to minimal information disclosure but heavily interactive procedures, like Cascade, or using less efficient but also less interactive -just one message is exchanged- procedures, like the ones based in low-density parity-check (LDPC) codes. The price to pay in the LDPC case is that good efficiency is only attained for very long codes and in a very narrow range centered around the quantum bit error rate (QBER) that the code was designed to reconcile, thus forcing to have several codes if a broad range of QBER needs to be catered for. Real world implementations of these methods are thus very demanding, either on computational or communication resources or both, to the extent that the last generation of GHz clocked QKD systems are finding a bottleneck in the classical part. In order to produce compact, high performance and reliable QKD systems it would be highly desirable to remove these problems. Here we analyse the use of short-length LDPC codes in the information reconciliation context using a low interactivity, blind, protocol that avoids an a priori error rate estimation. We demonstrate that 2x10^3 bits length LDPC codes are suitable for blind reconciliation. Such codes are of high interest in practice, since they can be used for hardware implementations with very high throughput.
