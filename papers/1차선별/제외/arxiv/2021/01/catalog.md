# arXiv — 2021-01


## Ethereum ECCPoW

- **Status**: ❌
- **Reason**: ECCPoW 블록체인 합의(Ethereum) — LDPC를 작업증명 퍼즐로 사용, ECC 디코더/구성 새 기여 없음
- **ID**: arxiv:2101.10729v1
- **Type**: preprint
- **Published**: 2021-01-26
- **Authors**: Hyoungsung Kim, Jehyuk Jang, Sangjun Park +1
- **PDF**: https://arxiv.org/pdf/2101.10729v1
- **Abstract**: The error-correction code based proof-of-work (ECCPoW) algorithm is based on a low-density parity-check (LDPC) code. The ECCPoW is possible to impair ASIC with its time-varying capability of the parameters of LDPC code. Previous researches on the ECCPoW algorithm have presented its theory and implementation on Bitcoin. But they do not discuss how stable the block generation time is. A finite mean block generation time (BGT) and none heavy-tail BGT distribution are the ones of the focus in this study. In the ECCPoW algorithm, BGT may show a long-tailed distribution due to time-varying cryptographic puzzles. Thus, it is of interest to see if the BGT distribution is not heavy-tailed and if it shows a finite mean. If the distribution is heavy-tailed, then confirmation of a transaction cannot be guaranteed. We present implementation, simulation, and validation of ECCPoW Ethereum. In implementation, we explain how the ECCPoW algorithm is integrated into Ethereum 1.0 as a new consensus algorithm. In the simulation, we perform a multinode simulation to show that the ECCPoW Ethereum works well with automatic difficulty change. In the validation, we present the statistical results of the two-sample Anderson-Darling test to show that the distribution of BGT satisfies the necessary condition of the exponential distribution. Our implementation is downloadable at https://github.com/cryptoecc/ETH-ECC.

## Random Fourier Feature Based Deep Learning for Wireless Communications

- **Status**: ❌
- **Reason**: RFF 기반 딥러닝 일반론, LDPC는 VLC 채널 검출 예시 중 하나 — 떼어낼 LDPC 디코더 기법 없음, 무선 응용 특이적
- **ID**: arxiv:2101.05254v1
- **Type**: preprint
- **Published**: 2021-01-13
- **Authors**: Rangeet Mitra, Georges Kaddoum
- **PDF**: https://arxiv.org/pdf/2101.05254v1
- **Abstract**: Deep-learning (DL) has emerged as a powerful machine-learning technique for several classic problems encountered in generic wireless communications. Specifically, random Fourier Features (RFF) based deep-learning has emerged as an attractive solution for several machine-learning problems; yet there is a lacuna of rigorous results to justify the viability of RFF based DL-algorithms in general. To address this gap, we attempt to analytically quantify the viability of RFF based DL. Precisely, in this paper, analytical proofs are presented demonstrating that RFF based DL architectures have lower approximation-error and probability of misclassification as compared to classical DL architectures. In addition, a new distribution-dependent RFF is proposed to facilitate DL architectures with low training-complexity. Through computer simulations, the practical application of the presented analytical results and the proposed distribution-dependent RFF, are depicted for various machine-learning problems encountered in next-generation communication systems such as: a) line of sight (LOS)/non-line of sight (NLOS) classification, and b) message-passing based detection of low-density parity check codes (LDPC) codes over nonlinear visible light communication (VLC) channels. Especially in the low training-data regime, the presented simulations show that significant performance gains are achieved when utilizing RFF maps of observations. Lastly, in all the presented simulations, it is observed that the proposed distribution-dependent RFFs significantly outperform RFFs, which make them useful for potential machine-learning/DL based applications in the context of next-generation communication systems.

## Deep Joint Source Channel Coding for WirelessImage Transmission with OFDM

- **Status**: ❌
- **Reason**: 딥러닝 JSCC 무선 이미지 전송, LDPC는 비교 베이스라인일 뿐 — 기준상 JSCC 제외
- **ID**: arxiv:2101.03909v2
- **Type**: preprint
- **Published**: 2021-01-05
- **Authors**: Mingyu Yang, Chenghong Bian, Hun-Seok Kim
- **PDF**: https://arxiv.org/pdf/2101.03909v2
- **Abstract**: We present a deep learning based joint source channel coding (JSCC) scheme for wireless image transmission over multipath fading channels with non-linear signal clipping. The proposed encoder and decoder use convolutional neural networks (CNN) and directly map the source images to complex-valued baseband samples for orthogonal frequency division multiplexing (OFDM) transmission. The proposed model-driven machine learning approach eliminates the need for separate source and channel coding while integrating an OFDM datapath to cope with multipath fading channels. The end-to-end JSCC communication system combines trainable CNN layers with non-trainable but differentiable layers representing the multipath channel model and OFDM signal processing blocks. Our results show that injecting domain expert knowledge by incorporating OFDM baseband processing blocks into the machine learning framework significantly enhances the overall performance compared to an unstructured CNN. Our method outperforms conventional schemes that employ state-of-the-art but separate source and channel coding such as BPG and LDPC with OFDM. Moreover, our method is shown to be robust against non-linear signal clipping in OFDM for various channel conditions that do not match the model parameter used during the training.
