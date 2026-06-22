# IEEE Xplore — 2021-03 (1차선별 통과)


## Noisy Density Evolution With Asymmetric Deviation Models

- **Status**: ✅
- **Reason**: 결함소자상 noisy LDPC 디코더(BP/Gallager B/양자화 min-sum) 비대칭편차 DE+보상 디코더 제안, HW 이식가능(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9266091
- **Type**: journal
- **Published**: March 2021
- **Authors**: Elsa Dupraz, François Leduc-Primeau
- **PDF**: https://ieeexplore.ieee.org/document/9266091
- **Abstract**: This paper considers low-density parity-check (LDPC) decoders affected by deviations introduced by the electronic device on which the decoder is implemented. Noisy density evolution (DE) that allows to theoretically study the performance of these LDPC decoders can only consider symmetric deviation models due to the all-zero codeword assumption. A novel DE method is proposed that admits the use of asymmetric deviation models, thus widening the range of faulty implementations that can be analyzed. DE equations are provided for three noisy decoders: belief propagation, Gallager B, and quantized min-sum (MS). Simulation results confirm that the proposed DE accurately predicts the performance of LDPC decoders with asymmetric deviations. Furthermore, asymmetric versions of the Gallager B and MS decoders are proposed to compensate the effect of asymmetric deviations. The parameters of these decoders are then optimized using the proposed DE, leading to better ensemble thresholds and improved finite-length performance in the presence of asymmetric deviations.

## Low Complexity Generalized-LDPC Decoder Based on Trellis Splicing

- **Status**: ✅
- **Reason**: G-LDPC 트렐리스 스플라이싱+조기정지로 복잡도 저감하는 새 디코더 알고리즘(C), 바이너리
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9246528
- **Type**: journal
- **Published**: March 2021
- **Authors**: Xuan Zhou, Zheng Ma, Li Li +1
- **PDF**: https://ieeexplore.ieee.org/document/9246528
- **Abstract**: The high reliability short length low-density parity-check (LDPC) codes for Ultra Reliable Low Latency Communication (URLLC) are particularly important to future wireless communication systems. Even though the error floor region performance can be improved by using generalized-LDPC (G-LDPC) decoder, its penalty of increasing complexity can not be ignored. In this letter, we invoke the early stop criterion and the trellis splicing (TS) method to G-LDPC decoder. Hence, a G-LDPC-TS decoder is proposed. The proposed method can effectively reduce the number of variable nodes (VNs) involved in BCJR (Bahl-Cocke-Jelinek-Raviv) decoding of G-LDPC; thus, it yields a lower computational complexity. The results confirm that our G-LDPC-TS decoder can achieve a significant complexity reduction without sacrificing the performance.

## Quasi-Cyclic LDPC Codes for Short Block-Lengths

- **Status**: ✅
- **Reason**: Novel binary QC-LDPC construction (Euclidean geometry + circulant decomposition, girth avoidance) distinct from standard methods; portable code design (E).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9438238
- **Type**: conference
- **Published**: 6-13 March
- **Authors**: Muhammad Nauman Danish, Syed Ahmed Pasha, Ali Javed Hashmi
- **PDF**: https://ieeexplore.ieee.org/document/9438238
- **Abstract**: In wireless communication, transmission error can be caused by multi-path fading, shadowing, scattering, interference and noise. As a result, errors generated in digital communication can be classified as burst errors, random bit errors, crosstalk and echo. For reliable communication, channel coding is used which adds redundancy to the information bits. Reliable and low latency communication are crucial for future communication systems involving satellite constellations and 5G communication systems, which underscores the importance of channel coding. Various codes exist for channel coding, among which low-density parity-check (LDPC) codes, polar codes and tail biting convolution codes are mentioned for 5G ultra-reliable low latency communication and enhanced mobile broadband systems. In the literature, the performance of large block-length codes has been well-studied. But these codes lead to high latency. The design of short block-length codes remains an open problem due to the trade-off between latency and performance. In this paper, we develop a systematic procedure for construction of hybrid quasi-cyclic LDPC (QC-LDPC) codes and compare the performance of the proposed approach with random LDPC and existing QC-LDPC codes for short block-lengths and phase shift keying (PSK) signal characteristics. The proposed method exploits Euclidean geometry and circulant decomposition resulting in a QC-LDPC matrix that avoids shorter girths for iterative decoding cycles. We emphasize that the proposed approach is different from the protographic construction method, masking method, identity matrix replacement method, algebraic based construction method, and base graph method used for the construction of QC-LDPC codes.

## Improvement of the Bit Duplication Method for Rate-Compatible Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: rate-compatible LDPC bit duplication 개선 — 바이너리 LDPC 코드 설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9535844
- **Type**: conference
- **Published**: 24-26 Marc
- **Authors**: Son Le, Evgeny Likhobabin
- **PDF**: https://ieeexplore.ieee.org/document/9535844
- **Abstract**: In this paper, we propose a principle for improving the “bit duplication” method for designing rate-compatible low-density parity-check (LDPC) codes. An experiment was carried out in the Matlab to obtain codes of rate-1/4 with different variants for duplicating bits from the original irregular DVB-S2 code of rate-1/2. Experimental results show that different bit duplication variants give different performance, moreover, codes using duplication of that part of the code word, where, respectively, the columns of the check matrix have the majority of the nonzero elements, turn out to be the best.
