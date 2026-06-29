# arXiv — 2014-01


## Probabilistic Signal Shaping for Bit-Metric Decoding

- **Status**: ❌
- **Reason**: 확률적 신호 셰이핑+bit-metric 디코딩(BICM/coded modulation), LDPC는 베이스라인일 뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:1401.6190v3
- **Type**: preprint
- **Published**: 2014-01-23
- **Authors**: Georg Böcherer
- **PDF**: https://arxiv.org/pdf/1401.6190v3
- **Abstract**: A scheme is proposed that combines probabilistic signal shaping with bit-metric decoding. The transmitter generates symbols according to a distribution on the channel input alphabet. The symbols are labeled by bit strings. At the receiver, the channel output is decoded with respect to a bit-metric. An achievable rate is derived using random coding arguments. For the 8-ASK AWGN channel, numerical results show that at a spectral efficiency of 2 bits/s/Hz, the new scheme outperforms bit-interleaved coded modulation (BICM) without shaping and BICM with bit shaping (i Fabregas and Martinez, 2010) by 0.87 dB and 0.15 dB, respectively, and is within 0.0094 dB of the coded modulation capacity. The new scheme is implemented by combining a distribution matcher with a systematic binary low-density parity-check code. The measured finite-length gains are very close to the gains predicted by the asymptotic theory.

## Image Block Loss Restoration Using Sparsity Pattern as Side Information

- **Status**: ❌
- **Reason**: 이미지 블록 손실 복원에 LDPC를 side info 보호용으로 부수 사용, 채널 ECC 신규 기법 없음
- **ID**: arxiv:1401.5966v2
- **Type**: preprint
- **Published**: 2014-01-23
- **Authors**: Hossein Hosseini, Ali Goli, Neda Barzegar Marvasti +2
- **PDF**: https://arxiv.org/pdf/1401.5966v2
- **Abstract**: In this paper, we propose a method for image block loss restoration based on the notion of sparse representation. We use the sparsity pattern as side information to efficiently restore block losses by iteratively imposing the constraints of spatial and transform domains on the corrupted image. Two novel features, including a pre-interpolation and a criterion for stopping the iterations, are proposed to improve the performance. Also, to deal with practical applications, we develop a technique to transmit the side information along with the image. In this technique, we first compress the side information and then embed its LDPC coded version in the least significant bits of the image pixels. This technique ensures the error-free transmission of the side information, while causing only a small perturbation on the transmitted image. Mathematical analysis and extensive simulations are performed to validate the method and investigate the efficiency of the proposed techniques. The results verify that the proposed method outperforms its counterparts for image block loss restoration.

## Upper Bounds on the Minimum Distance of Quasi-Cyclic LDPC codes Revisited

- **Status**: ❌
- **Reason**: QC-LDPC 최소거리 상계 순수 이론 bound, 디코더/HW/구성 신규 기여로 이어지지 않음
- **ID**: arxiv:1401.2120v1
- **Type**: preprint
- **Published**: 2014-01-09
- **Authors**: Alexey Frolov, Pavel Rybin
- **PDF**: https://arxiv.org/pdf/1401.2120v1
- **Abstract**: Two upper bounds on the minimum distance of type-1 quasi-cyclic low-density parity-check (QC LDPC) codes are derived. The necessary condition is given for the minimum code distance of such codes to grow linearly with the code length.
