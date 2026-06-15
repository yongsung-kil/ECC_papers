# IEEE Xplore — 2024-04


## Adaptive Granularity Progressive LDPC Decoding for NAND Flash Memory

- **ID**: ieee:10318173
- **Published**: April 2024
- **Authors**: Binhao Bao, Qianhui Li, Wu Guan +3
- **PDF**: https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10318173
- **Abstract**: Progressive low-density parity check (LDPC) code decoding has been widely used to correct increasing raw bit errors in NAND Flash memory. Once the decoding of a single logical page fails, the read-retry operation will reprocess at an increased read level with more accurate initial log-likelihood ratio (LLR) messages. However, the traditional progressive LDPC decodings with inappropriate read-level-increase granularities of read-retry operations introduce unnecessary flash read latency. By taking advantage of globally coupled LDPC (GC-LDPC) codes, an improved adaptive granularity progressive LDPC decoding (IAGPD) is proposed. This method can estimate the number of uncorrectable bit errors before each read-retry operation by detecting the unsatisfied local parity checks and general syndrome in the decoding failure. Then, it adaptively selects the optimal read-level-increase granularities for read-retry operations in the progressive LDPC decoding. Compared with the existing decoding methods, only by an extra 0.098% of the decoder area and two clock cycles, our method can reduce the flash read latency by up to 43%. And the solid-state drive (SSD) read response time on MQsim can be reduced by up to 32%.
