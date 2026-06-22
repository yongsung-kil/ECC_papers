# IEEE Xplore — 2023-07 (1차선별 통과)


## Decoding LDPC Codes by Using Negative Proximal Regularization

- **Status**: ✅
- **Reason**: Novel restartable ADMM decoder with negative proximal regularization for binary LDPC — new portable decoder algorithm (C).
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10122222
- **Type**: journal
- **Published**: July 2023
- **Authors**: Yiming Chen, Rui Wang, Jinglong Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/10122222
- **Abstract**: The low-density parity-check (LDPC) decoding problem can be expressed as an integer linear programming (ILP) problem. One efficient method to solve the ILP problem is to relax the integer constraints and add penalty terms to the objective function, and the revised problem can be solved via the alternating direction method of multipliers (ADMM) algorithm. These penalty terms can punish the non-integral solutions and improve the decoding performance of the decoder. However, ADMM decoders are easily trapped in a local solution, which limits the frame error rate (FER) performance of the decoders at low signal-to-noise ratios (SNR). In this paper, we propose a restartable ADMM-based decoder using a negative proximal regularization. The negative proximal term will be updated whenever the decoder finds a new local solution. Therefore, the decoder can be restarted several times and the candidate solution which satisfies the parity-check equations and has the lowest objective function value can be selected as the decoder’s output. Some properties, together with several choices of penalty terms are discussed. We also investigate the convergence of our proposed decoder, and prove that the possibility of decoding errors is independent of the codeword that is transmitted. Simulation results show that our proposed decoder outperforms other ADMM-based decoders in most cases, while the decoding complexity maintains the same.

## The Syndrome Bit Flipping Algorithm for LDPC Codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 신규 Syndrome Bit Flipping 디코더, 트래핑셋 해소·error floor 저감·HW 후처리 실증—C/D 강하게 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10113636
- **Type**: journal
- **Published**: July 2023
- **Authors**: Emmanuel Boutillon, Chris Winstead, Fakhreddine Ghaffari
- **PDF**: https://ieeexplore.ieee.org/document/10113636
- **Abstract**: Performance of LDPC decoders at high SNR is dominated by trapping sets that induce an error floor in the performance curve. We propose a new algorithm that resolves trapping sets and lowers the error floor. The new algorithm, called Syndrome Bit Flipping (SBF), computes the sum of adjacent parity violations at each symbol node. Bits are flipped by comparing the syndrome sum against a time-varying threshold called the decoding key. SBF is compared to other bit-flipping decoders on the Binary Symmetric Channel (BSC), and is demonstrated as a post-processing step for a Noisy Gradient Descent Bit-Flipping (NGDBF) hardware decoder. We demonstrate the post-processing method for an LDPC code defined in the 802.3an standard, and find that the frame error rate is improved by at least two orders of magnitude, even as the required iterations are reduced by 33%.

## Improving the Thresholds of Generalized LDPC Codes With Convolutional Code Constraints

- **Status**: ✅
- **Reason**: GLDPC with convolutional-code CN constraints, irregularity-optimized BP/MAP thresholds — new binary code-design technique (E), portable.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10121163
- **Type**: journal
- **Published**: July 2023
- **Authors**: Muhammad Umar Farooq, Alexandre Graell i Amat, Michael Lentmaier
- **PDF**: https://ieeexplore.ieee.org/document/10121163
- **Abstract**: CC-GLPDC codes are a class of generalized low-density parity-check (GLDPC) codes where the constraint nodes (CNs) represent convolutional codes. This allows for efficient decoding in the trellis with the forward-backward algorithm, and the strength of the component codes easily can be controlled by the encoder memory without changing the graph structure. In this letter, we extend the class of CC-GLDPC codes by introducing different types of irregularity at the CNs and investigating their effect on the BP and MAP decoding thresholds for the binary erasure channel (BEC). For the considered class of codes, an exhaustive grid search is performed to find the BP-optimized and MAP-optimized ensembles and compare their thresholds with the regular ensemble of the same design rate. The results show that irregularity can significantly improve the BP thresholds, whereas the thresholds of the MAP-optimized ensembles are only slightly different from the regular ensembles. Simulation results for the AWGN channel are presented as well and compared to the corresponding thresholds.

## A Model-Driven Quasi-ResNet Belief Propagation Neural Network Decoder for LDPC Codes

- **Status**: ✅
- **Reason**: C: 바이너리 LDPC BP의 새 신경망 디코더(Quasi-ResNet, shortcut connection) 제안 — NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10217911
- **Type**: conference
- **Published**: 9-12 July 
- **Authors**: Liangsi Ma, Bei Liu, Xin Su +1
- **PDF**: https://ieeexplore.ieee.org/document/10217911
- **Abstract**: For the Belief Propagation (BP) algorithm of low-density parity-check (LDPC) codes, existing deep learning methods have a limited performance improvement and it is difficult to train deep-level networks. In this paper, a model-driven quasi-residual network (Quasi-ResNet) BP decoding architecture is proposed for LDPC codes to further improve the performance of standard BP decoding. This method feeds the reliable messages calculated in current iteration into the next iteration based on the shortcut connection, and adjusts the weight of shortcut connection based on the error Back Propagation algorithm of neural network to determine the optimal genetic proportion of reliable messages. The decoding architecture is composed of a model-driven deep neural network (DNN) and shortcut connection. Simulation results show that the decoder can not only unfold more layers quickly compared with the DNN-based BP decoder, but also further improve the decoding performance.

## Design of F-L-QC-LDPC Decoder Based on LNMS Decoding Algorithm

- **Status**: ✅
- **Reason**: 신규 LNMS(layered min-sum) 디코딩 알고리즘 + QC-LDPC 구성 — 이식 가능 디코더/코드설계(C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10280802
- **Type**: conference
- **Published**: 29-31 July
- **Authors**: Youyao Liu, Haimei Huang, Jialei Gao +1
- **PDF**: https://ieeexplore.ieee.org/document/10280802
- **Abstract**: Low Density Parity Check Code (LDPC) can meet the decoding requirements of a variety of code lengths and rates in different communication scenarios, but the LDPC code check matrix is irregular, which has problems with difficult storage and reading of the check matrix and high coding complexity. For the decoding requirements of multi-code length, this paper proposes a Quasi Crystal Low Density Parity Check Codes (QCLDPC) code based on Fibonacci Lucas sequence, which can obtain the codewords with different code length and code rate by changing the number of rows and columns of the exponential matrix. In terms of decoding algorithms, the Layered Non-Maximum Suppression (LNMS) decoding algorithm, which combines the minimum sum decoding algorithm with the layered algorithm, is proposed to improve the convergence speed of decoding iteration and decoder throughput. Through simulation and comparative experiments, it is proved that this design can support a variety of bit rates, block lengths and sub matrix sizes, and meet the requirements of high throughput and low complexity decoder in modern communication systems.

## Efficient Genetic Algorithm-based LDPC Code Design for IoT Applications

- **Status**: ✅
- **Reason**: 유전알고리즘 기반 LDPC 부호설계 + girth-4 제거 + min-sum — 새 코드설계/디코더 조합 가능성(E/C), 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10227247
- **Type**: conference
- **Published**: 27-28 July
- **Authors**: Loc Nguyen-Van-Thanh, Tan Do-Duy
- **PDF**: https://ieeexplore.ieee.org/document/10227247
- **Abstract**: In this paper, we propose an improved Low-Density Parity-Check (LDPC) code design scheme based on the existing genetic optimization-based LDPC code design scheme proposed in [1]. In particular, we perform the removal of the girth-4 property of the parity check matrix (H-matrix) and utilize the min-sum decoding algorithm instead of the Belief Propagation (BP) algorithm in order to enhance the performance of the LDPC code. Furthermore, an (32,64) LDPC code is considered in this paper. Finally, we evaluate the block error rate (BLER) of the LDPC code over white Gaussian noise channels. By means of evaluation results using Matlab, we indicate that our proposed approach can achieve a gain of more than 11% in terms of BLER compared to the existing schemes without significantly increasing the complexity of the decoding scheme.

## Impact of Non-Gaussian Noise Distribution by Artificial Neural Network-based Equalizers

- **Status**: ✅
- **Reason**: 비가우시안 잡음 분포 기반 정확한 LLR 추정으로 LDPC 성능 개선 — LLR 양자화/추정 기법은 NAND LDPC에 직접 관련(A/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:10209616
- **Type**: conference
- **Published**: 2-6 July 2
- **Authors**: Weiqi Lu, Zexu Liu, Lei Liu +3
- **PDF**: https://ieeexplore.ieee.org/document/10209616
- **Abstract**: The non-Gaussian noise distribution by an artificial neural network (ANN) equalizer causes degradation to LDPC performance. Accurate estimation of LLR based on non-Gaussian noise distribution can improve receiver sensitivity by about 0.7 dB.

## FPGA based High Bandwidth LDPC using Channel Coding Technique

- **Status**: ✅
- **Reason**: FPGA LDPC 디코더 HW 구현, 다중 부호 지원 비용 절감 설계 최적화 — D 이식 가능 HW 아키텍처
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10212353
- **Type**: conference
- **Published**: 19-21 July
- **Authors**: S. Yuvaraj, P. Latha, E. Malarvizhi +1
- **PDF**: https://ieeexplore.ieee.org/document/10212353
- **Abstract**: Error-correcting codeword's using Low-Density Parity Check (LDPC) have been the subject of many studies in the communications field. Because of excellent error correction performance, low-complexity calculations, and appropriateness for parallel hardware design, this has also become typical digital modulation schemes in various protocols. Meanwhile, significant work has gone into creating LDPC decoders that can run on Field-Programmable Gate Array (FPGA) devices instead of Application-Specific Integrated Circuit (ASIC) systems due to their faster processing speeds and parallel processing capabilities. However, it is difficult to compare and even more difficult to implement the FPGA-based LDPC encoder solutions that are available in the open literature. A corrected signal decoding method with several design optimizations that lower the expenses of supporting several different codes The decoder's development findings show that it can achieve better bandwidth utilization than earlier flexible FPGA-based LDPC decoders while still meeting the requisite amount of extensibility and satisfactory error-correcting effectiveness.

## A family of error correcting codes for automotive applications

- **Status**: ✅
- **Reason**: 자동차용 ECC 부호족, 저복잡도 인코딩/디코딩 회로 + rate 적응성 — 부호류/HW 기여 가능성, 초록이 모호하여 in으로 살림(Phase 3 재검토)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:10217205
- **Type**: conference
- **Published**: 17-19 July
- **Authors**: Massimo Battaglioni, Giovanni Cancellieri
- **PDF**: https://ieeexplore.ieee.org/document/10217205
- **Abstract**: In this paper we propose a class of error correcting codes for automotive applications. The main merits of the proposed codes are the low-complexity encoding and decoding circuits, and a fine rate adaptability. A special chip for encoding and decoding operations could be designed, with promising market perspectives.
