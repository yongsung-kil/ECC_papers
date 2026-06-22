# arXiv — 2016-11 (1차선별 통과)


## Improving Belief Propagation Decoding of Polar Codes Using Scattered EXIT Charts

- **Status**: ✅
- **Reason**: 폴라+보조 LDPC 코드 설계에 scattered EXIT chart 사용; 보조 LDPC 코드 구성 기법(E)은 바이너리 LDPC에 이식 가능하므로 애매하나 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1611.03655v1
- **Type**: preprint
- **Published**: 2016-11-11
- **Authors**: A. Elkelesh, M. Ebada, S. Cammerer +1
- **PDF**: https://arxiv.org/pdf/1611.03655v1
- **Abstract**: For finite length polar codes, channel polarization leaves a significant number of channels not fully polarized. Adding a Cyclic Redundancy Check (CRC) to better protect information on the semi-polarized channels has already been successfully applied in the literature, and is straightforward to be used in combination with Successive Cancellation List (SCL) decoding. Belief Propagation (BP) decoding, however, offers more potential for exploiting parallelism in hardware implementation, and thus, we focus our attention on improving the BP decoder. Specifically, similar to the CRC strategy in the SCL-case, we use a short-length "auxiliary" LDPC code together with the polar code to provide a significant improvement in terms of BER. We present the novel concept of "scattered" EXIT charts to design such auxiliary LDPC codes, and achieve net coding gains (Le. for the same total rate) of 0.4 dB at BER of 1E-5 compared to the conventional BP decoder.
