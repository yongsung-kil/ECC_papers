# IEEE Xplore — 2005-04 (1차선별 통과)


## Block-LDPC: a practical LDPC coding system design approach

- **Status**: ✅
- **Reason**: Block-LDPC 코드-인코더-디코더 공동설계+HW지향 제약, 부분병렬 디코더 아키텍처(D/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1417070
- **Type**: journal
- **Published**: April 2005
- **Authors**: Hao Zhong, Tong Zhang
- **PDF**: https://ieeexplore.ieee.org/document/1417070
- **Abstract**: This paper presents a joint low-density parity-check (LDPC) code-encoder-decoder design approach, called Block-LDPC, for practical LDPC coding system implementations. The key idea is to construct LDPC codes subject to certain hardware-oriented constraints that ensure the effective encoder and decoder hardware implementations. We develop a set of hardware-oriented constraints, subject to which a semi-random approach is used to construct Block-LDPC codes with good error-correcting performance. Correspondingly, we develop an efficient encoding strategy and a pipelined partially parallel Block-LDPC encoder architecture, and a partially parallel Block-LDPC decoder architecture. We present the estimation of Block-LDPC coding system implementation key metrics including the throughput and hardware complexity for both encoder and decoder. The good error-correcting performance of Block-LDPC codes has been demonstrated through computer simulations. With the effective encoder/decoder design and good error-correcting performance, Block-LDPC provides a promising vehicle for real-life LDPC coding system implementations.

## On implementation of min-sum algorithm and its modifications for decoding low-density Parity-check (LDPC) codes

- **Status**: ✅
- **Reason**: min-sum 클리핑/양자화(4비트) 영향 분석+성능개선 변형, NAND LLR 양자화 디코더에 직접 이식(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1425734
- **Type**: journal
- **Published**: April 2005
- **Authors**: Jianguang Zhao, F. Zarkeshvari, A.H. Banihashemi
- **PDF**: https://ieeexplore.ieee.org/document/1425734
- **Abstract**: The effects of clipping and quantization on the performance of the min-sum algorithm for the decoding of low-density parity-check (LDPC) codes at short and intermediate block lengths are studied. It is shown that in many cases, only four quantization bits suffice to obtain close to ideal performance over a wide range of signal-to-noise ratios. Moreover, we propose modifications to the min-sum algorithm that improve the performance by a few tenths of a decibel with just a small increase in decoding complexity. A quantized version of these modified algorithms is also studied. It is shown that, when optimized, modified quantized min-sum algorithms perform very close to, and in some cases even slightly outperform, the ideal belief-propagation algorithm at observed error rates.

## Optimization of LDPC-coded turbo CDMA systems

- **Status**: ✅
- **Reason**: CDMA용이나 density evolution 기반 불규칙 LDPC 임계값/코드설계 기법은 바이너리 LDPC 설계에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1408199
- **Type**: journal
- **Published**: April 2005
- **Authors**: Xiaodong Wang, Guosen Yue, K.R. Narayanan
- **PDF**: https://ieeexplore.ieee.org/document/1408199
- **Abstract**: We consider the analysis and design of low-density parity-check (LDPC) codes for turbo multiuser detection in multipath code division multiple access (CDMA) channels. We develop techniques for computing the probability density function (pdf) of the extrinsic messages at the output of the soft-input soft-output (SISO) multiuser detectors as a function of the pdf of input extrinsic messages, user spreading codes, channel impulse responses, and signal-to-noise ratios. Of particular interest is the soft interference cancellation plus minimum mean square error (SIC-MMSE) multiuser detector, for which the pdf of the extrinsic messages can be characterized analytically. For the case of additive white Gaussian noise (AWGN) channels, the extrinsic messages can be well approximated as symmetric Gaussian distributed. For the case of asynchronous multipath fading channels, the extrinsic messages can be approximated by a mixture of symmetric Gaussian distributions. We show that the expectation-maximization (EM) algorithm can be used to compute the parameters of this mixture. Using these techniques, we are able to accurately compute the thresholds for LDPC codes and design good irregular LDPC codes. Simulation results are in good agreement with the computed thresholds, and the designed irregular LDPC codes outperform regular ones significantly.

## Improved bit-flipping decoding of low-density parity-check codes

- **Status**: ✅
- **Reason**: 개선된 확률적 bit-flipping 하드디시전 디코딩 알고리즘, 바이너리 LDPC에 이식 가능한 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1412054
- **Type**: journal
- **Published**: April 2005
- **Authors**: N. Miladinovic, M.P.C. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1412054
- **Abstract**: In this correspondence, a new method for improving hard-decision bit-flipping decoding of low-density parity-check (LDPC) codes is presented. Bits with a number of unsatisfied check sums larger than a predetermined threshold are flipped with a probability p /spl les/ 1 which is independent of the code considered. The probability p is incremented during decoding according to some rule. With a proper choice of the initial p, the proposed improved bit-flipping (BF) algorithm achieves gain not only in performance, but also in average decoding time for signal-to-noise ratio (SNR) values of interest with respect to p = 1.

## Extremes of information combining

- **Status**: ✅
- **Reason**: information combining 극값으로 LDPC 앙상블 MAP 임계값 분석, 코드설계/DE 분석 기법 이식 가능(E), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1412027
- **Type**: journal
- **Published**: April 2005
- **Authors**: I. Sutskover, S. Shamai, J. Ziv
- **PDF**: https://ieeexplore.ieee.org/document/1412027
- **Abstract**: Extreme densities for information combining are found for two important channel models: the binary-input symmetric parallel broadcast channel and the parity-constrained-input symmetric parallel channels. Following, upper and lower mutual information thresholds are stated for per-bit maximum a posteriori probability (MAP) decoding and low-density parity-check (LDPC) code ensembles.

## Short-block LDPC codes for a low-frequency power-line communications system

- **Status**: ✅
- **Reason**: 고율 short-block LDPC에서 cycle 밀도-검출/정정 trade-off 코드설계(E), 유한길이 바이너리 LDPC 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1430473
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: Q.H. Spencer
- **PDF**: https://ieeexplore.ieee.org/document/1430473
- **Abstract**: The TWACS power-line communication system is used by electric utilities for communicating over long distances with power meters and other devices. Data packets tend to be short, and increasing demand for bandwidth requires that error detection and correction add minimal overhead. We have investigated low-density parity-check (LDPC) codes as a replacement for the existing error control coding scheme. In this paper we investigate the error detection capabilities of LDPC codes with high rate and short block size. Under these constraints, increasing the density of the code adds short cycles to the Tanner graph of the code. This degrades the overall error rate, but we have found that it also improves the undetected error rate, resulting in a trade-off between error correction and detection that can be adjusted by changing the density of the code. Using this approach, an LDPC code can be designed that improves on both the error detection and correction capabilities of the existing scheme.

## A decoding for low density parity check codes over impulsive noise channels

- **Status**: ✅
- **Reason**: 임펄스 노이즈(class A) 채널용 sum-product 디코딩 변형 제안, 디코더 알고리즘(C) 이식 가능성
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1430471
- **Type**: conference
- **Published**: 6-8 April 
- **Authors**: H. Nakagawa, D. Umehara, S. Denno +1
- **PDF**: https://ieeexplore.ieee.org/document/1430471
- **Abstract**: Power line channel often suffers from impulsive interference generated by electrical appliances. Therefore, power line communication makes degradation due to such impulsive interference. We introduce Middleton's class a noise model into a statistical model of impulsive noise environment. In this paper, we apply LDPC (low density parity check) codes and sum-product decoding to additive white class a noise (AWAN) channels. We propose a sum-product decoding which is suitable for AWAN channels. In addition, we show the BER (bit error rate) performance of the proposed sum-product decoding in class a noise environment by computer simulation.

## Partition-and-shift LDPC codes for high density magnetic recording

- **Status**: ✅
- **Reason**: large girth·flexible rate 구조 LDPC 신규 구성(partition-and-shift); 이식 가능 코드 설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1463924
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: Jin Lu, M.F. Moura
- **PDF**: https://ieeexplore.ieee.org/document/1463924
- **Abstract**: High-rate low-density parity-check (LDPC) codes are the focus of intense research in magnetic recording because, when decoded by the iterative sum-product algorithm, they show decoding performance close to the Shannon capacity. LDPC codes can be described by a bipartite graph called Tanner graph. The length g of the shortest cycle in a Tanner graph is referred to as the girth g of the graph. Since large girth leads to more efficient decoding and large minimum distance, LDPC codes with large girth are particularly desired. We propose a class of structured LDPC codes with large girth and flexible code rates, called partition-and-shift LDPC codes (PS-LDPC).

## On LDPC codes satisfying the (0, k) constraint

- **Status**: ✅
- **Reason**: message-passing 디코더와 협력하는 flip decoder로 error floor 제거; 이식 가능 BP 디코더 개선(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1463928
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: S. Babvey, S.W. McLaughlin
- **PDF**: https://ieeexplore.ieee.org/document/1463928
- **Abstract**: In this paper, we use the stochastic expectation-maximization method to illustrate how to come close to achieving the capacity of the noisy (0, k) constrained AWGN channels. We use the bit-flipping based constrained coding system proposed by Vasic to transmit (0, k) constrained LDPC codewords over an AWGN channel. In the original approach of Vasic, if the number of flipped bits is large, the message-passing decoder of LDPC codes fails to correct all the errors and the system is prone to an error floor even at high SNR values [Vasic, B et al., 2003]. We propose a flip decoder that exploits the information from the message-passing decoder to correct the flipped bits. We illustrate that the message-passing decoder and the flip decoder together correct both the channel and flip errors, and achieve rates close to the noisy (0, k) channel capacity.

## Low-density parity-check codes with variable rate and randomized constraints for advanced magnetic tape recording

- **Status**: ✅
- **Reason**: RLL 제약을 비트플립으로 LDPC와 결합, 디코더가 의도적 에러 복구하는 코드설계 기법(E) 이식 여지
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1464239
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: Zongwang Li, Jin Xie, B.V.K. Vijaya Kumar
- **PDF**: https://ieeexplore.ieee.org/document/1464239
- **Abstract**: Variable rate and randomized run length limited (VR/sup 2/ RLL) constraint is used in some magnetic tape recording systems. The variable rate encoding algorithm monitors the incoming data stream for conditions such as run length limit (RLL) constraints. If one of the conditions is violated, a bit is inserted into the data stream. The purpose of the VR/sup 2/ RLL constraint is to ensure that the encoded data contains adequate tracking and amplitude information for reliable data detection and prevent the preamble pattern from occurring during the data field. Although the VR/sup 2/ approach to RLL constraint is effective, it has the disadvantages of variable block length and error propagation. Furthermore, VR/sup 2/ is not suitable for soft decision decoding needed by low-density parity check (LDPC) codes being investigated because of their good performance, low complexity and inherent parallel decoding architecture. LDPC codes usually exhibit excellent error correction performance and the LDPC decoder may be able to recover the codeword even if we deliberately introduce some errors in the codeword in order to satisfy RLL constraints. Based on this observation, the paper proposes a scheme of combining LDPC codes with the VR/sup 2/ RLL constraint based on bit flipping. In addition to providing soft decision decoding to achieve large coding gain, the proposed scheme has the advantages of no error propagation and fixed block length.

## Field programmable gate array-based investigation of the error floor of low density parity check (LDPC) codes for magnetic recording channel

- **Status**: ✅
- **Reason**: LDPC error floor 평가용 FPGA 플랫폼·아키텍처 제시(D) — 자기기록이나 디코더 HW 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1464236
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: Lingyan Sun, Hongwei Song, B.V.K. Vijaya Kumar +1
- **PDF**: https://ieeexplore.ieee.org/document/1464236
- **Abstract**: Low density parity check (LDPC) codes have shown 3 to 5 dB coding gain, at bit error rates (BER) around 10/sup -5/, over the uncoded partial response maximum-likelihood (PRML) channels. However, the error floor of LDPC codes is still an open question and is one of the major concerns in applying LDPC codes in high density receding channel. Due to the suboptimal nature of decoding schemes and the difficulties in code spectrum analysis, the performance analysis of LDPC code at very low BER region is very difficult, if not impossible. Therefore, the performance of LDPC codes is usually evaluated through Monte Carlo simulations. The sequential nature of the conventional C simulations limits their capability for BER investigation. It takes months to evaluate the performance of codes in partial response (PR) channel at 10/sup -9/ BER using optimized C code and a 2 GHz computer. To investigate the error floors, a high-throughput, fully-reconfigurable field programmable gate array (FPGA) platform was developed for the evaluation of LDPC codes in PR channel. In this paper, the architecture, main features and throughput of the channel simulator on FPGA was described. The error floor of one type of LDPC code is shown as an example.

## An efficient R-Mesh implementation of LDPC codes message-passing decoder

- **Status**: ✅
- **Reason**: R-Mesh 상 message-passing 디코더 병렬 구현; 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1420099
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: S. Babvey, A.G. Bourgeois, J.A. Fernandez-Zepeda +1
- **PDF**: https://ieeexplore.ieee.org/document/1420099
- **Abstract**: In this paper we propose a constant-time parallel algorithm for implementing the message-passing decoder of LDPC codes on a two dimensional R-Mesh, trying to keep the number of processors small. The R-Mesh provides dynamic reconfiguration, hardware reuse, and flexibility to problem changes. To decode a different code, we may simply set up the required connections between the bit-nodes and check-nodes by modifying the initialization phase of the R-Mesh algorithm. No extra wiring or hardware changes are required, as compared to other existing approaches. Moreover, the same hardware can implement the decoder in both probability and logarithm domains. We illustrate that the R-Mesh is an efficient model for parallel implementation of the decoder in terms of time complexity, flexibility to problem changes and simplicity of routing messages.

## Decoding for magnetic recording media with overlapping tracks

- **Status**: ✅
- **Reason**: 채널 ISI와 ECC 결합 그래프 상 joint message-passing 디코딩; 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1463921
- **Type**: conference
- **Published**: 4-8 April 
- **Authors**: N. Singla, J.A. O'Sullivan, C.T. Miller +1
- **PDF**: https://ieeexplore.ieee.org/document/1463921
- **Abstract**: This paper studies the effects of track overlap in magnetic recording medium vis-a-vis the decoding performance and user bit-density. In this paper, we use the full graph algorithm, which performs message-passing on the joint graph of the channel ISI and the error-control code for decoding.

## Forced Convergence Decoding of LDPC Codes - EXIT Chart Analysis and Combination with Node Complexity Reduction Techniques

- **Status**: ✅
- **Reason**: forced convergence 디코딩(노드 복잡도 감소)+EXIT 분석 — 이식 가능한 저복잡도 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5755261
- **Type**: conference
- **Published**: 10-13 Apri
- **Authors**: Ernesto Zimmermann, Wolfgang Rave, Gerhard Fettweis
- **PDF**: https://ieeexplore.ieee.org/document/5755261
- **Abstract**: Recently, the concept of forced convergence decoding for Low-Density Parity-Check Codes has been introduced. Restricting the message passing in the iterative process to the nodes that still significantly contribute to the decoding result, this approach allows for substantial reduction in decoding complexity at negligible deterioration in performance. We analyze this novel technique using EXIT charts and show how it compares to and can be combined with other complexity reduction techniques. Our findings imply that forced convergence works effectively in conjunction with other complexity reduction techniques while retaining its attractiveness in terms of the complexity-performance trade-off.
