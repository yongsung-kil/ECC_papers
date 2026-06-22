# arXiv — 2010-06


## Algebraic Constructions of Graph-Based Nested Codes from Protographs

- **Status**: ❌
- **Reason**: protograph 기반 nested 부호 설계, joint channel-network coding용 — 떼어낼 NAND ECC 기법 없음(네트워크 코딩 응용 특이적)
- **ID**: arxiv:1006.2977v1
- **Type**: preprint
- **Published**: 2010-06-15
- **Authors**: Christine A. Kelley, Joerg Kliewer
- **PDF**: https://arxiv.org/pdf/1006.2977v1
- **Abstract**: Nested codes have been employed in a large number of communication applications as a specific case of superposition codes, for example to implement binning schemes in the presence of noise, in joint network-channel coding, or in physical-layer secrecy. Whereas nested lattice codes have been proposed recently for continuous-input channels, in this paper we focus on the construction of nested linear codes for joint channel-network coding problems based on algebraic protograph LDPC codes. In particular, over the past few years several constructions of codes have been proposed that are based on random lifts of suitably chosen base graphs. More recently, an algebraic analog of this approach was introduced using the theory of voltage graphs. In this paper we illustrate how these methods can be used in the construction of nested codes from algebraic lifts of graphs.

## Tree-structure Expectation Propagation for Decoding LDPC codes over Binary Erasure Channels

- **Status**: ✅
- **Reason**: BEC용 신규 EP 디코더, BP와 동일 복잡도로 더 큰 erasure 정정 — 바이너리 LDPC BP 이식 가능 디코더 기법(C)
- **ID**: arxiv:1006.1535v1
- **Type**: preprint
- **Published**: 2010-06-08
- **Authors**: Pablo M. Olmos, Juan José Murillo-Fuentes
- **PDF**: https://arxiv.org/pdf/1006.1535v1
- **Abstract**: Expectation Propagation is a generalization to Belief Propagation (BP) in two ways. First, it can be used with any exponential family distribution over the cliques in the graph. Second, it can impose additional constraints on the marginal distributions. We use this second property to impose pair-wise marginal distribution constraints in some check nodes of the LDPC Tanner graph. These additional constraints allow decoding the received codeword when the BP decoder gets stuck. In this paper, we first present the new decoding algorithm, whose complexity is identical to the BP decoder, and we then prove that it is able to decode codewords with a larger fraction of erasures, as the block size tends to infinity. The proposed algorithm can be also understood as a simplification of the Maxwell decoder, but without its computational complexity. We also illustrate that the new algorithm outperforms the BP decoder for finite block-size

## A Low-Complexity Joint Detection-Decoding Algorithm for Nonbinary LDPC-Coded Modulation Systems

- **Status**: ❌
- **Reason**: 비이진(q-ary) LDPC coded modulation용 joint detection-decoding — 비이진 LDPC 제외
- **ID**: arxiv:1006.1024v1
- **Type**: preprint
- **Published**: 2010-06-05
- **Authors**: Xuepeng Wang, Baoming Bai, Xiao Ma
- **PDF**: https://arxiv.org/pdf/1006.1024v1
- **Abstract**: In this paper, we present a low-complexity joint detection-decoding algorithm for nonbinary LDPC codedmodulation systems. The algorithm combines hard-decision decoding using the message-passing strategy with the signal detector in an iterative manner. It requires low computational complexity, offers good system performance and has a fast rate of decoding convergence. Compared to the q-ary sum-product algorithm (QSPA), it provides an attractive candidate for practical applications of q-ary LDPC codes.

## Channel Decoding with a Bayesian Equalizer

- **Status**: ❌
- **Reason**: CSI 불확실성 보정 Bayesian equalizer(채널 등화) — LDPC는 베이스라인, 떼어낼 디코더/코드설계 기법 없음(무선 채널추정 특이적)
- **ID**: arxiv:1006.0795v1
- **Type**: preprint
- **Published**: 2010-06-04
- **Authors**: Luis Salamanca, Juan José Murillo-Fuentes, Fernando Pérez-Cruz
- **PDF**: https://arxiv.org/pdf/1006.0795v1
- **Abstract**: Low-density parity-check (LPDC) decoders assume the channel estate information (CSI) is known and they have the true a posteriori probability (APP) for each transmitted bit. But in most cases of interest, the CSI needs to be estimated with the help of a short training sequence and the LDPC decoder has to decode the received word using faulty APP estimates. In this paper, we study the uncertainty in the CSI estimate and how it affects the bit error rate (BER) output by the LDPC decoder. To improve these APP estimates, we propose a Bayesian equalizer that takes into consideration not only the uncertainty due to the noise in the channel, but also the uncertainty in the CSI estimate, reducing the BER after the LDPC decoder.

## EXIT Chart Approximations using the Role Model Approach

- **Status**: ❌
- **Reason**: EXIT chart 근사 측정 기법, 비이진 LDPC check-node 최적화 대상 — 비이진 + 분석 도구, 떼어낼 바이너리 ECC 기법 없음
- **ID**: arxiv:1006.0659v1
- **Type**: preprint
- **Published**: 2010-06-03
- **Authors**: Jossy Sayir
- **PDF**: https://arxiv.org/pdf/1006.0659v1
- **Abstract**: Extrinsic Information Transfer (EXIT) functions can be measured by statistical methods if the message alphabet size is moderate or if messages are true a-posteriori distributions. We propose an approximation we call mixed information that constitutes a lower bound for the true EXIT function and can be estimated by statistical methods even when the message alphabet is large and histogram-based approaches are impractical, or when messages are not true probability distributions and time-averaging approaches are not applicable. We illustrate this with the hypothetical example of a rank-only message passing decoder for which it is difficult to compute or measure EXIT functions in the conventional way. We show that the role model approach (arXiv:0809.1300) can be used to optimize post-processing for the decoder and that it coincides with Monte Carlo integration in the non-parametric case. It is guaranteed to tend towards the optimal Bayesian post-processing estimator and can be applied in a blind setup with unknown code-symbols to optimize the check-node operation for non-binary Low-Density Parity-Check (LDPC) decoders.
