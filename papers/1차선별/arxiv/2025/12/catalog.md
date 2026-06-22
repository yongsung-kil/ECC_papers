# arXiv — 2025-12 (1차선별 통과)


## A 14ns-Latency 9Gb/s 0.44mm$^2$ 62pJ/b Short-Blocklength LDPC Decoder ASIC in 22FDX

- **Status**: ✅
- **Reason**: 신규 short-blocklength 멀티레이트 바이너리 LDPC 부호 + fully-parallel MP 디코더 ASIC(14ns, 22FDX) — 이식 가능 코드설계+HW 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2512.17834v1
- **Type**: preprint
- **Published**: 2025-12-19
- **Authors**: Darja Nonaca, Jérémy Guichemerre, Reinhard Wiesmayr +2
- **PDF**: https://arxiv.org/pdf/2512.17834v1
- **Abstract**: Ultra-reliable low latency communication (URLLC) is a key part of 5G wireless systems. Achieving low latency necessitates codes with short blocklengths for which polar codes with successive cancellation list (SCL) decoding typically outperform message-passing (MP)-based decoding of low-density parity-check (LDPC) codes. However, SCL decoders are known to exhibit high latency and poor area efficiency. In this paper, we propose a new short-blocklength multi-rate binary LDPC code that outperforms the 5G-LDPC code for the same blocklength and is suitable for URLLC applications using fully parallel MP. To demonstrate our code's efficacy, we present a 0.44mm$^2$ GlobalFoundries 22FDX LDPC decoder ASIC which supports three rates and achieves the lowest-in-class decoding latency of 14ns while reaching an information throughput of 9Gb/s at 62pJ/b energy efficiency for a rate-1/2 code with 128-bit blocklength.

## Pseudocodewords of quantum, quasi-cyclic, and spatially-coupled LDPC codes: a fundamental cone perspective

- **Status**: ✅
- **Reason**: QC/SC-LDPC pseudocodeword·fundamental cone 분석으로 iterative/LP 디코더 error floor에 연결 가능, 애매해 살림(Phase3 재검토)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2512.02941v1
- **Type**: preprint
- **Published**: 2025-12-02
- **Authors**: Wittawat Kositwattanarerk, Gretchen L. Matthews, Emily McMillon +1
- **PDF**: https://arxiv.org/pdf/2512.02941v1
- **Abstract**: While low-density parity-check (LDPC) codes are near capacity-achieving when paired with iterative decoders, these decoders may not output a codeword due to the existence of pseudocodewords. Thus, pseudocodewords have been studied to give insight into the performance of modern decoders including iterative and linear programming decoders. These pseudocodewords are found to be dependent on the parity-check matrix of the code and the particular decoding algorithm used. In this paper, we consider LP decoding, which has been linked to graph cover decoding, providing functions which capture these pseudocodewords. In particular, we analyze the underlying structure of pseudocodewords from quantum stabilizer codes that arise from LP decoding, quasi-cyclic LDPC codes, and spatially-coupled LDPC codes.
