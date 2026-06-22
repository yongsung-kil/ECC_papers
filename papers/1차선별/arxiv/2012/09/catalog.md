# arXiv — 2012-09 (1차선별 통과)


## LDPC Decoding with Limited-Precision Soft Information in Flash Memories

- **Status**: ✅
- **Reason**: 플래시 메모리 LDPC 제한정밀 soft LLR, MMI 양자화·기준전압 최적화 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1210.0149v1
- **Type**: preprint
- **Published**: 2012-09-29
- **Authors**: Jiadong Wang, Guiqiang Dong, Thomas Courtade +3
- **PDF**: https://arxiv.org/pdf/1210.0149v1
- **Abstract**: This paper investigates the application of low-density parity-check (LDPC) codes to Flash memories. Multiple cell reads with distinct word-line voltages provide limited-precision soft information for the LDPC decoder. The values of the word-line voltages (also called reference voltages) are optimized by maximizing the mutual information (MI) between the input and output of the multiple-read channel. Constraining the maximum mutual-information (MMI) quantization to enforce a constant-ratio constraint provides a significant simplification with no noticeable loss in performance.   Our simulation results suggest that for a well-designed LDPC code, the quantization that maximizes the mutual information will also minimize the frame error rate. However, care must be taken to design the code to perform well in the quantized channel. An LDPC code designed for a full-precision Gaussian channel may perform poorly in the quantized setting. Our LDPC code designs provide an example where quantization increases the importance of absorbing sets thus changing how the LDPC code should be optimized.   Simulation results show that small increases in precision enable the LDPC code to significantly outperform a BCH code with comparable rate and block length (but without the benefit of the soft information) over a range of frame error rates.

## Balanced Modulation for Nonvolatile Memories

- **Status**: ✅
- **Reason**: 비휘발성메모리 balanced LDPC 구성+읽기임계 조정 — NAND/메모리 직접 및 코드설계(A/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1209.0744v1
- **Type**: preprint
- **Published**: 2012-09-04
- **Authors**: Hongchao Zhou,  Anxiao,  Jiang +1
- **PDF**: https://arxiv.org/pdf/1209.0744v1
- **Abstract**: This paper presents a practical writing/reading scheme in nonvolatile memories, called balanced modulation, for minimizing the asymmetric component of errors. The main idea is to encode data using a balanced error-correcting code. When reading information from a block, it adjusts the reading threshold such that the resulting word is also balanced or approximately balanced. Balanced modulation has suboptimal performance for any cell-level distribution and it can be easily implemented in the current systems of nonvolatile memories. Furthermore, we studied the construction of balanced error-correcting codes, in particular, balanced LDPC codes. It has very efficient encoding and decoding algorithms, and it is more efficient than prior construction of balanced error-correcting codes.
