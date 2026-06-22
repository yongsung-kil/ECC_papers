# IEEE Xplore — 1999-01 (1차선별 통과)


## Constructing low-density parity-check codes with circulant matrices

- **Status**: ✅
- **Reason**: circulant 행렬 기반 LDPC 구성 + 저중량 codeword 제어(error floor) → 바이너리 QC형 LDPC 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:814359
- **Type**: conference
- **Published**: 1999
- **Authors**: J. W. Bond, S. Hui, H. Schmidt
- **PDF**: https://ieeexplore.ieee.org/document/814359
- **Abstract**: This is a report on the authors' ongoing effort to implement low-density parity-check codes with iterative belief propagation decoding in a communication system. The system requires the codes to have block lengths from 1000 to 2000 bits. We describe two different methods of constructing the codes using: (1) a combination of random and circulant matrices, and (2) random and circulant matrices with constraints to control the number of low weight codewords. We illustrate the performances of the different constructions with simulations.

## Good error-correcting codes based on very sparse matrices

- **Status**: ✅
- **Reason**: MacKay-Neal/Gallager 희소행렬 부호 + sum-product 디코딩 — 기초 바이너리 LDPC 부호설계/디코더 (C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:748992
- **Type**: journal
- **Published**: 1999
- **Authors**: D. J. C. MacKay
- **PDF**: https://ieeexplore.ieee.org/document/748992
- **Abstract**: We study two families of error-correcting codes defined in terms of very sparse matrices. "MN" (MacKay-Neal (1995)) codes are recently invented, and "Gallager codes" were first investigated in 1962, but appear to have been largely forgotten, in spite of their excellent properties. The decoding of both codes can be tackled with a practical sum-product algorithm. We prove that these codes are "very good", in that sequences of codes exist which, when optimally decoded, achieve information rates up to the Shannon limit. This result holds not only for the binary-symmetric channel but also for any channel with symmetric stationary ergodic noise. We give experimental results for binary-symmetric channels and Gaussian channels demonstrating that practical performance substantially better than that of standard convolutional and concatenated codes can be achieved; indeed, the performance of Gallager codes is almost as close to the Shannon limit as that of turbo codes.

## Time-varying periodic convolutional codes with low-density parity-check matrix

- **Status**: ✅
- **Reason**: Convolutional codes with low-density parity-check matrix + iterative decoding; LDPC-convolutional construction and BP-style decoder potentially transferable to binary LDPC/SC-LDPC (E), keep for Phase 3.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:782171
- **Type**: journal
- **Published**: 1999
- **Authors**: A. Jimenez Felstrom, K. S. Zigangirov
- **PDF**: https://ieeexplore.ieee.org/document/782171
- **Abstract**: We present a class of convolutional codes defined by a low-density parity-check matrix and an iterative algorithm for decoding these codes. The performance of this decoding is close to the performance of turbo decoding. Our simulation shows that for the rate R=1/2 binary codes, the performance is substantially better than for ordinary convolutional codes with the same decoding complexity per information bit. As an example, we constructed convolutional codes with memory M=1025, 2049, and 4097 showing that we are about 1 dB from the capacity limit at a bit-error rate (BER) of 10/sup -5/ and a decoding complexity of the same magnitude as a Viterbi decoder for codes having memory M=10.

## Reduced complexity iterative decoding of low-density parity check codes based on belief propagation

- **Status**: ✅
- **Reason**: Two simplified BP variants (real additions only, channel-independent, quantization-friendly HW) for binary LDPC -> directly transferable min-sum/BP decoder for NAND (C/D).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:768759
- **Type**: journal
- **Published**: 1999
- **Authors**: M. P. C. Fossorier, M. Mihaljevic, H. Imai
- **PDF**: https://ieeexplore.ieee.org/document/768759
- **Abstract**: Two simplified versions of the belief propagation algorithm for fast iterative decoding of low-density parity check codes on the additive white Gaussian noise channel are proposed. Both versions are implemented with real additions only, which greatly simplifies the decoding complexity of belief propagation in which products of probabilities have to be computed. Also, these two algorithms do not require any knowledge about the channel characteristics. Both algorithms yield a good performance-complexity trade-off and can be efficiently implemented in software as well as in hardware, with possibly quantized received values.

## Comparison of constructions of irregular Gallager codes

- **Status**: ✅
- **Reason**: 불규칙 Gallager(LDPC) 그래프 구성법 비교 + 고속 인코딩 구성 → 바이너리 LDPC 코드 설계 기법(E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:795809
- **Type**: journal
- **Published**: 1999
- **Authors**: D. J. C. MacKay, S. T. Wilson, M. C. Davey
- **PDF**: https://ieeexplore.ieee.org/document/795809
- **Abstract**: The low-density parity check codes whose performance is closest to the Shannon limit are "Gallager codes" based on irregular graphs. We compare alternative methods for constructing these graphs and present two results. First, we find a "super-Poisson" construction which gives a small improvement in empirical performance over a random construction. Second, whereas Gallager codes normally take N/sup 2/ time to encode, we investigate constructions of regular and irregular Gallager codes that allow more rapid encoding and have smaller memory requirements in the encoder. We find that these "fast encoding" Gallager codes have equally good performance.
