# IEEE Xplore — 2022-02 (1차선별 통과)


## Reliability Ratio-Based Serial Algorithm of LDPC Decoder for Turbo Equalization Schemes

- **Status**: ✅
- **Reason**: 신뢰도비 기반 적응적 직렬 LDPC 디코딩(SBP 개선, 수렴 가속) — 이식 가능한 새 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9435416
- **Type**: journal
- **Published**: Feb. 2022
- **Authors**: Sirawit Khittiwitchayakul, Watid Phakphisut, Pornchai Supnithi
- **PDF**: https://ieeexplore.ieee.org/document/9435416
- **Abstract**: Serial decoding algorithms of low-density parity-check (LDPC) code converge efficiently with low errors. Previously, a serial decoding algorithm, named a shuffled belief-propagation (SBP), was applied in turbo equalization of bit-patterned magnetic recording (BPMR) systems. With the SBP algorithm, an LDPC decoder converged twice as fast as one using conventional BP algorithms. We further improved the convergence speed of SBP by updating the messages in an adaptive order, which played a flexible role throughout decoding. We proposed two adaptive-serial algorithms for LDPC codes in turbo equalization. One updated the messages using the extrinsic loglikelihood ratio (LLR) and the result of the parity-check equation checking. The second contained an additional rule that tracked the LLR sign changes in each iteration. Both algorithms converged faster and with lower bit error rates (BERs) than the SBP and previous adaptive-serial algorithms in a BPMR system with media noise.

## Parity-Check Coding Transmit Diversity for Wireless Communications With High Mobility

- **Status**: ✅
- **Reason**: half-rate invertible LDPC 기반 송신 다이버시티 + chase-combining MPA 디코딩 — MPA 변형은 디코더 기법(C)으로 검토 여지, 애매하여 보존
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9647964
- **Type**: journal
- **Published**: Feb. 2022
- **Authors**: Qi-Yue Yu, Tang Li, Hong-Ru Lin +1
- **PDF**: https://ieeexplore.ieee.org/document/9647964
- **Abstract**: Highmobility is an important scenario for the 5G wireless communications. However, the high mobility results in serious time-varying fading, bringing challenges to the reliabilities of wireless transmission. Diversity technique is an essential method to overcome the effect of fading. It is noted that an LDPC (low-density parity-check) code is a concatenation of single parity-check codes (SPC) and repetition codes (REP) by a random interleaver, and a REP can be viewed as a typical example for achieving time/frequency diversity. Thus, it is appealing to jointly consider LDPC codes and diversity techniques. This paper presents parity-check coding transmit diversity (PCTD) schemes based on half-rate invertible LDPC codes, which are capable of achieving both diversity and coding gains from the time-varying fading channels. Besides, we investigate two types of PCTD schemes, and take into consideration two transmission modes, which are single-carrier (SC) and orthogonal frequency division multiplexing (OFDM) transmission modes. A chase combining based message passing algorithm (CC-MPA) is proposed for the proposed schemes, which can take full advantages of signal processing and coding gains. Furthermore, the Shannon limits of time-varying fading channels with BPSK signaling are deduced. Simulation results show that the proposed PCTD with CC-MPA algorithm can provide better BER performances than the classical time-domain diversity scheme in time-varying fading channels, which is appealing for the high mobility communications.

## Neural Network Aided Impulsive Perturbation Decoding for Short Raptor-Like LDPC Codes

- **Status**: ✅
- **Reason**: 짧은 LDPC용 신경망 기반 perturbation 심볼선택 BP 디코딩(MBPD-IP) — 이식 가능한 새 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9601295
- **Type**: journal
- **Published**: Feb. 2022
- **Authors**: Hyunjae Lee, Yong-Sung Kil, Min Young Chung +1
- **PDF**: https://ieeexplore.ieee.org/document/9601295
- **Abstract**: As short packet communications become more important, multi-round belief propagation decoding with impulsive perturbation (MBPD-IP) was proposed to improve the decoding of short low-density parity-check (LDPC) codes. To operate the MBPD-IP effectively, it is crucial to select proper symbols to be perturbed in as few trials as possible. Unfortunately, existing perturbation symbol selection criteria are heuristic and not effective for special codes such as raptor-like (RL) LDPC codes. In this letter, a neural network (NN) based perturbation symbol selection scheme for MBPD-IP is proposed where the symbols to be perturbed are selected from a pre-trained NN. It is shown that the proposed scheme performs significantly better than existing schemes for the RL LDPC code of 5G new radio and still works well for plain code structures.

## A Low-Complexity Endurance Modulation for Flash Memory

- **Status**: ✅
- **Reason**: 플래시 endurance modulation을 ECC와 결합해 max-log 복조로 복원 — NAND 직접 + ECC 활용(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9502845
- **Type**: journal
- **Published**: Feb. 2022
- **Authors**: Amr Ismail, Magnus Sandell
- **PDF**: https://ieeexplore.ieee.org/document/9502845
- **Abstract**: The repeated program/erase (P/E) cycles wear out flash memory cells which limits the device’s lifetime. The larger the injected/erased charge, the faster the wear out rate and thus there is interest in reducing the percentage of cells programmed to high voltage levels. Conventional data shaping techniques often introduce a nonnegligible overhead as well as incurring additional complexity to encode the input data into shaped codewords and decode the read data. We propose a novel lossless yet simple endurance modulation technique that relies solely on the error-correction code (ECC) to retrieve the original data. This idea is motivated by the fact that ECCs are usually designed to correct channel errors towards the end of the device’s lifetime and hence at early age, the ECC can be jointly used for channel error correction and endurance demodulation. The proposed scheme consists of data shaping by flipping bits in a controlled manner and simple max-log demodulation to recover those flipped bits. The simulation results show that the proposed scheme does not undermine the device’s ability to recover the original data if the shaping gain is adjusted as the device ages. Once the channel errors exceed a prescribed threshold, the controller disables the endurance modulation and operates in normal mode.

## STNet: Low-Complexity Neural Network Decoder With Network Pruning

- **Status**: ✅
- **Reason**: Sigmoid-Tanh 신경망 채널 디코더 + 네트워크 프루닝으로 저복잡도화 — LDPC에 이식 가능한 신경망 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9614188
- **Type**: journal
- **Published**: Feb. 2022
- **Authors**: Zhiyuan Ren, Ling Zhao, Chuanyang Wei +1
- **PDF**: https://ieeexplore.ieee.org/document/9614188
- **Abstract**: In this letter, a novel and compact neural network called Sigmoid-Tanh Network (STNet) is proposed for channel decoding, which is only composed of sigmoid and tanh activation functions. To address the structural redundancy problem in long and short-term memory network (LSTM), the neurons in the STNet are redesigned with the most effective structure in the LSTM cell for decoding. To further reduce the computational complexity, we propose an automatic pruning method based on multiple layer sensitivity, which can effectively remove redundant weights in STNet decoder with slight performance loss. Simulation results show that the proposed STNet decoder achieves near-maximum likelihood (ML) performance with only 17.1% trainable parameters compared to LSTM. Moreover, our pruning method achieves comparable decoding performance when reducing 58.3% Floating-point operations (FLOPs) for STNet.

## Performance Analysis of Mixed MIMO RF/FSO DF Relaying Based on Globally Coupled Low Density Parity Check (GC-LDPC) Codes

- **Status**: ✅
- **Reason**: GC-LDPC(글로벌 결합) 코드 + two-phase local-global 디코딩 — 이식 가능 코드설계/디코더(E/C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:9728906
- **Type**: conference
- **Published**: 13-16 Feb.
- **Authors**: Ibrahima Gueye, Idy Diop, Ibra Dioum +4
- **PDF**: https://ieeexplore.ieee.org/document/9728906
- **Abstract**: In this work, we analyze the performance of the use of error correcting codes in particular the LDPC codes with global coupling (GC-LDPC) in a double-hop relay system composed of links with multiple inputs and multiple outputs at radio frequency/ free space optics (MIMO-RF/FSO). A multi-antenna listener listens to the information by decoding the signals received from the source node. In addition, to decode the signals we use two-phase local-global decoding. To eliminate interference in the first hop we use the interference alignment technique (IA) we also assume that the source-relay link undergoes Rayleigh fading, and that the relay-destination link is affected by the degradations of the channel optics, including path loss, atmospheric turbulence, and pointing errors. Using DF relay technology, mixed MIMO-RF/FSO systems combine the advantages of RF and FSO communication technologies. The use of mixed MIMO-RF/FSO cooperative transmission systems can improve network reliability and transmission. Results demonstrate improved performance of MIMO-RF/FSO DF cooperative relay system based on GC-LDPC codes with multiple antennas compared to MIMO-RF/FSO systems without the use of GC-LDPC codes, but also to systems SISO (Single-Input Single-Output) RF-FSO DF proposed in the existing literature.
