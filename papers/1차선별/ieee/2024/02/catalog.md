# IEEE Xplore — 2024-02 (1차선별 통과)


## Optimized Non-Surjective FAIDs for 5G LDPC Codes With Learnable Quantization

- **Status**: ✅
- **Reason**: QC-LDPC용 NS-FAID 디코더를 양자화 신경망으로 LUT 최적화 + 2비트 양자화 — 이식 가능 디코더(C), 저비트 양자화는 NAND LDPC에 직접 관련
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10352132
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Yanchen Lyu, Ming Jiang, Yifan Zhang +3
- **PDF**: https://ieeexplore.ieee.org/document/10352132
- **Abstract**: This letter proposes a novel approach for designing non-surjective (NS) finite alphabet iterative decoders (FAIDs) for quasi-cyclic low-density parity-check (LDPC) codes, especially 5G LDPC codes. We employ recurrent quantized neural networks to optimize the look-up tables used in NS-FAIDs, the design of which is the kernel of FAIDs. During the optimization of LUTs, the quantized message alphabets and quantization thresholds are jointly designed. To cope with the untrainable problem of quantization thresholds in the existing neural-network-based linear FAIDs, we use softmax distribution to soften the implied one-hot distribution of quantization thresholds, making it trainable in the neural network. The proposed decoders offer enhanced universality compared to existing neural network-based linear FAIDs, making them directly applicable to 5G LDPC codes with support for 2-bit quantization over the additive white Gaussian noise channel. Additionally, they significantly outperform the original NS-FAID in terms of performance.

## Deep Learning Aided LLR Correction Improves the Performance of Iterative MIMO Receivers

- **Status**: ✅
- **Reason**: DNN 기반 LLR 보정 기법 — 신경망 디코더 보조(C)로 분류 가능, LLR 신뢰도 보정은 NAND LDPC 연판정에 이식 여지. 애매하나 in으로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10246845
- **Type**: journal
- **Published**: Feb. 2024
- **Authors**: Jue Chen, Tsang-Yi Wang, Jwo-Yuh Wu +4
- **PDF**: https://ieeexplore.ieee.org/document/10246845
- **Abstract**: A Deep Learning (DL) aided Logarithmic Likelihood Ratio (LLR) correction method is proposed for improving the performance of Multiple-Input Multiple-Output (MIMO) receivers, where it is typical to adopt reduced-complexity algorithms for avoiding the excessive complexity of optimal full-search algorithms. These sub-optimal techniques typically express the probabilities of the detected bits using LLRs that often have values that are not consistent with their true reliability, either expressing too much confidence or not enough confidence in the value of the corresponding bits, leading to performance degradation. To circumvent this problem, a Deep Neural Network (DNN) is trained for detecting and correcting both over-confident and under-confident LLRs. We demonstrate that the complexity of employing the DL-aided technique is relatively low compared to the popular reduced-complexity receiver detector techniques since it only depends on a small number of real-valued inputs. Furthermore, the proposed approach is applicable to a wild variety of iterative receivers as demonstrated in the context of an iterative detection and decoding aided MIMO system, which uses a low-complexity Smart Ordering and Candidate Adding (SOCA) scheme for MIMO detection and Low-Density Parity Check (LDPC) codes for channel coding. We adopt Extrinsic Information Transfer (EXIT) charts for quantifying the Mutual Information (MI) and show that our DL method significantly improves the BLock Error Rate (BLER). Explicitly, we demonstrate that about 0.9 dB gain can be achieved at a BLER of $10^{-3}$ by employing the proposed DL-aided LLR correction method, at the modest cost of increasing the complexity by 16% compared to a benchmarker dispensing with LLR correction.

## Performance Analysis of LDPC Coded Outdoor Long-Distance Imaging MIMO System

- **Status**: ✅
- **Reason**: 빔별 BER 고려 LDPC 디코딩 방법 제안 — LLR/신뢰도 채널통계 반영 디코더 기법 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10556090
- **Type**: conference
- **Published**: 19-22 Feb.
- **Authors**: Daiki Ishikawa, Chedlia Ben Naila, Hiraku Okada +1
- **PDF**: https://ieeexplore.ieee.org/document/10556090
- **Abstract**: In this work, the performance of light-emitting diode-based (LED-based) imaging Multiple Input Multiple Output (MIMO) system for long-distance outdoor transmission is evaluated, and based on the results, a proposal for improving the performances is presented. We first conducted outdoor communication experiments, and error-free transmission of 200 Mbps over 100 m was achieved without using Forward Error Correction or other error control schemes. Nonetheless, communication errors occurred at distances shorter than 100 m. Furthermore, the bit error rate (BER) differed for each beam from each transmitting LED. Therefore, we introduced Low-density Parity-check (LDPC) codes along with a decoding method that takes into account the BER of each signal beam. The effectiveness of this decoding method is predicated on the time-invariance of the BER, which we have separately confirmed through experimental data. We assume that encoded bit errors for each signal beam would follow the BER observed in our non-encoded communication experiments. Under this assumption, we assessed various LDPC codes with different code lengths and coding rates. Our results demonstrated an improvement in BER performance.
