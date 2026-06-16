# arXiv — 2021-01


## Ethereum ECCPoW

- **ID**: arxiv:2101.10729v1
- **Type**: preprint
- **Published**: 2021-01-26
- **Authors**: Hyoungsung Kim, Jehyuk Jang, Sangjun Park +1
- **PDF**: https://arxiv.org/pdf/2101.10729v1
- **Abstract**: The error-correction code based proof-of-work (ECCPoW) algorithm is based on a low-density parity-check (LDPC) code. The ECCPoW is possible to impair ASIC with its time-varying capability of the parameters of LDPC code. Previous researches on the ECCPoW algorithm have presented its theory and implementation on Bitcoin. But they do not discuss how stable the block generation time is. A finite mean block generation time (BGT) and none heavy-tail BGT distribution are the ones of the focus in this study. In the ECCPoW algorithm, BGT may show a long-tailed distribution due to time-varying cryptographic puzzles. Thus, it is of interest to see if the BGT distribution is not heavy-tailed and if it shows a finite mean. If the distribution is heavy-tailed, then confirmation of a transaction cannot be guaranteed. We present implementation, simulation, and validation of ECCPoW Ethereum. In implementation, we explain how the ECCPoW algorithm is integrated into Ethereum 1.0 as a new consensus algorithm. In the simulation, we perform a multinode simulation to show that the ECCPoW Ethereum works well with automatic difficulty change. In the validation, we present the statistical results of the two-sample Anderson-Darling test to show that the distribution of BGT satisfies the necessary condition of the exponential distribution. Our implementation is downloadable at https://github.com/cryptoecc/ETH-ECC.

## Codes approaching the Shannon limit with polynomial complexity per information bit

- **ID**: arxiv:2101.10145v1
- **Type**: preprint
- **Published**: 2021-01-25
- **Authors**: Ilya Dumer, Navid Gharavi
- **PDF**: https://arxiv.org/pdf/2101.10145v1
- **Abstract**: We consider codes for channels with extreme noise that emerge in various low-power applications. Simple LDPC-type codes with parity checks of weight 3 are first studied for any dimension $m\rightarrow\infty.$ These codes form modulation schemes: they improve the original channel output for any $SNR>$ $-6$ dB (per information bit) and gain $3$ dB over uncoded modulation as $SNR$ grows. However, they also have a floor on the output bit error rate (BER) irrespective of their length. Tight lower and upper bounds, which are virtually identical to simulation results, are then obtained for BER at any SNR. We also study a combined scheme that splits $m$ information bits into $b$ blocks and protects each with some polar code. Decoding moves back and forth between polar and LDPC codes, every time using a polar code of a higher rate. For a sufficiently large constant $b$ and $m\rightarrow\infty$, this design yields a vanishing BER at any SNR that is arbitrarily close to the Shannon limit of -1.59 dB. Unlike other existing designs, this scheme has polynomial complexity of order $m\ln m$ per information bit.

## Unequal Error Protection Achieves Threshold Gains on BEC and BSC via Higher Fidelity Messages

- **ID**: arxiv:2101.09238v1
- **Type**: preprint
- **Published**: 2021-01-22
- **Authors**: Beyza Dabak, Ahmed Hareedy, Alexei Ashikhmin +1
- **PDF**: https://arxiv.org/pdf/2101.09238v1
- **Abstract**: Because of their capacity-approaching performance, graph-based codes have a wide range of applications, including communications and storage. In these codes, unequal error protection (UEP) can offer performance gains with limited rate loss. Recent empirical results in magnetic recording (MR) systems show that extra protection for the parity bits of a low-density parity-check (LDPC) code via constrained coding results in significant density gains. In particular, when UEP is applied via more reliable parity bits, higher fidelity messages of parity bits are spread to all bits by message passing algorithm, enabling performance gains. Threshold analysis is a tool to measure the effectiveness of a graph-based code or coding scheme. In this paper, we provide a theoretical analysis of this UEP idea using extrinsic information transfer (EXIT) charts in the binary erasure channel (BEC) and the binary symmetric channel (BSC). We use EXIT functions to investigate the effect of change in mutual information of parity bits on the overall coding scheme. We propose a setup in which parity bits of a repeat-accumulate (RA) LDPC code have lower erasure or crossover probabilities than input information bits. We derive the a-priori and extrinsic mutual information functions for check nodes and variable nodes of the code. After applying our UEP setup to the information functions, we formulate a linear programming problem to find the optimal degree distribution that maximizes the code rate under the decoding convergence constraint. Results show that UEP via higher fidelity parity bits achieves up to about $17\%$ and $28\%$ threshold gains on BEC and BSC, respectively.

## Random Fourier Feature Based Deep Learning for Wireless Communications

- **ID**: arxiv:2101.05254v1
- **Type**: preprint
- **Published**: 2021-01-13
- **Authors**: Rangeet Mitra, Georges Kaddoum
- **PDF**: https://arxiv.org/pdf/2101.05254v1
- **Abstract**: Deep-learning (DL) has emerged as a powerful machine-learning technique for several classic problems encountered in generic wireless communications. Specifically, random Fourier Features (RFF) based deep-learning has emerged as an attractive solution for several machine-learning problems; yet there is a lacuna of rigorous results to justify the viability of RFF based DL-algorithms in general. To address this gap, we attempt to analytically quantify the viability of RFF based DL. Precisely, in this paper, analytical proofs are presented demonstrating that RFF based DL architectures have lower approximation-error and probability of misclassification as compared to classical DL architectures. In addition, a new distribution-dependent RFF is proposed to facilitate DL architectures with low training-complexity. Through computer simulations, the practical application of the presented analytical results and the proposed distribution-dependent RFF, are depicted for various machine-learning problems encountered in next-generation communication systems such as: a) line of sight (LOS)/non-line of sight (NLOS) classification, and b) message-passing based detection of low-density parity check codes (LDPC) codes over nonlinear visible light communication (VLC) channels. Especially in the low training-data regime, the presented simulations show that significant performance gains are achieved when utilizing RFF maps of observations. Lastly, in all the presented simulations, it is observed that the proposed distribution-dependent RFFs significantly outperform RFFs, which make them useful for potential machine-learning/DL based applications in the context of next-generation communication systems.

## Deep Joint Source Channel Coding for WirelessImage Transmission with OFDM

- **ID**: arxiv:2101.03909v2
- **Type**: preprint
- **Published**: 2021-01-05
- **Authors**: Mingyu Yang, Chenghong Bian, Hun-Seok Kim
- **PDF**: https://arxiv.org/pdf/2101.03909v2
- **Abstract**: We present a deep learning based joint source channel coding (JSCC) scheme for wireless image transmission over multipath fading channels with non-linear signal clipping. The proposed encoder and decoder use convolutional neural networks (CNN) and directly map the source images to complex-valued baseband samples for orthogonal frequency division multiplexing (OFDM) transmission. The proposed model-driven machine learning approach eliminates the need for separate source and channel coding while integrating an OFDM datapath to cope with multipath fading channels. The end-to-end JSCC communication system combines trainable CNN layers with non-trainable but differentiable layers representing the multipath channel model and OFDM signal processing blocks. Our results show that injecting domain expert knowledge by incorporating OFDM baseband processing blocks into the machine learning framework significantly enhances the overall performance compared to an unstructured CNN. Our method outperforms conventional schemes that employ state-of-the-art but separate source and channel coding such as BPG and LDPC with OFDM. Moreover, our method is shown to be robust against non-linear signal clipping in OFDM for various channel conditions that do not match the model parameter used during the training.
