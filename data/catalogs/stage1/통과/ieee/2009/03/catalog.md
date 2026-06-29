# IEEE Xplore — 2009-03 (1차선별 통과)


## Efficient Shuffle Network Architecture and Application for WiMAX LDPC Decoders

- **Status**: ✅
- **Reason**: 유연 LDPC 디코더용 Benes 셔플 네트워크 HW 아키텍처(permutation network)로 NAND 디코더 HW에 이식 가능(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4801645
- **Type**: journal
- **Published**: March 2009
- **Authors**: Jun Lin, Zhongfeng Wang, Li Li +2
- **PDF**: https://ieeexplore.ieee.org/document/4801645
- **Abstract**: In this brief, a new algorithm that can efficiently generate all the control signals for the shuffle network used in flexible low-density parity-check (LDPC) decoders is proposed. Employing the proposed algorithm, the hardware complexity of the controller of shuffle networks using the Benes network structure can be significantly reduced. In addition, a low-complexity reconfigurable shuffle network architecture for flexible LDPC decoders is developed. Both the Benes network and the controller can be tailored to fit specific applications. Consequently, an efficient shuffle network for WiMAX LDPC decoders is presented. Synthesis results demonstrate that with the SMIC 0.18-mum complementary metal-oxide-semiconductor process, the total gate count of the proposed shuffle network is only 16 000. The area saving is between 26.6% and 71.1% compared to related works in the literature.

## Two-staged informed dynamic scheduling for sequential belief propagation decoding of LDPC codes

- **Status**: ✅
- **Reason**: 순차 BP 디코딩의 2단 informed dynamic scheduling 신규 제안 — 바이너리 LDPC BP 디코더 개선(C)으로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4799021
- **Type**: journal
- **Published**: March 2009
- **Authors**: S. Kim, K. Ko, J. Heo +1
- **PDF**: https://ieeexplore.ieee.org/document/4799021
- **Abstract**: Recent studies have shown that sequential belief propagation decoding of low-density parity-check codes can increase the decoding convergence speed while simultaneously improving the asymptotic performance compared to the conventional flooding scheme. Two of the practical sequential decoding schemes known are the ones by Casado et al. [1] in which informed dynamic scheduling is used for scheduling the sequential updates of the messages. In this letter, we propose a two-staged informed dynamic scheduling that unifies and outperforms the two schemes of [1].

## Two bit-flipping decoding algorithms for low-density parity-check codes

- **Status**: ✅
- **Reason**: 바이너리 LDPC용 비트플리핑 디코더에 소프트결정 확장+루프검출 신규 기법, 저복잡도 디코더(C/D)로 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4799029
- **Type**: journal
- **Published**: March 2009
- **Authors**: Telex Magloire, Nkouatchah Ngatched, Martin Bossert +2
- **PDF**: https://ieeexplore.ieee.org/document/4799029
- **Abstract**: In this letter, a low complexity decoding algorithm for binary linear block codes is applied to low-density paritycheck (LDPC) codes and improvements are described, namely an extension to soft-decision decoding and a loop detection mechanism. For soft decoding, only one real-valued addition per code symbol is needed, while the remaining operations are only binary as in the hard decision case. The decoding performance is considerably increased by the loop detection. Simulation results are used to compare the performance with other known decoding strategies for LDPC codes, with the result that the presented algorithms offer excellent performances at smaller complexity.

## Burst erasure correcting LDPC codes

- **Status**: ✅
- **Reason**: 버스트 소거정정 바이너리 LDPC 패리티검사행렬 superposition 구성(E), stopping set 기반 코드설계 신규 기여
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4799040
- **Type**: journal
- **Published**: March 2009
- **Authors**: Sarah J. Johnson
- **PDF**: https://ieeexplore.ieee.org/document/4799040
- **Abstract**: In this paper low-density parity-check (LDPC) codes are designed for burst erasure channels. Firstly, lower bounds for the maximum length erasure burst that can always be corrected with message-passing decoding are derived as a function of the parity-check matrix properties. We then show how parity-check matrices for burst erasure correcting LDPC codes can be constructed using superposition, where the burst erasure correcting performance of the resulting codes is derived as a property of the stopping set size of the base matrices and the choice of permutation matrices for the superposition. This result is then used to design both single burst erasure correcting LDPC codes which are also resilient to the presence of random erasures in the received bits and LDPC codes which can correct multiple erasure bursts in the same codeword.

## Soft decision LSI operating at 32 Gsample/s for LDPC FEC-based optical transmission systems

- **Status**: ✅
- **Reason**: 2-bit soft-decision 32Gsample/s LSI(LDPC FEC용 신뢰도비트 생성 HW); 이식 가능 양자화/soft-info HW 기법, 보존
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:5032874
- **Type**: conference
- **Published**: 22-26 Marc
- **Authors**: T. Kobayashi, S. Kametani, K. Shimizu +3
- **PDF**: https://ieeexplore.ieee.org/document/5032874
- **Abstract**: We have developed a 2-bit 32 Gsample/s soft decision LSI for low-density parity-check code FEC at 100 Gb/s in 0.13 mum SiGe-BiCMOS which generates confidence bit with 25 mVpp sensitivity.

## Noise adaptive LDPC decoding using particle filter

- **Status**: ✅
- **Reason**: particle filter로 채널 노이즈 추정해 BP에 실시간 피드백하는 적응형 LDPC 디코더 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5054686
- **Type**: conference
- **Published**: 18-20 Marc
- **Authors**: Lijuan Cui, Shuang Wang, Samuel Cheng +1
- **PDF**: https://ieeexplore.ieee.org/document/5054686
- **Abstract**: Belief propagation (BP) is a powerful algorithm to decode the low-density parity check (LDPC) codes over the additive white Gaussian noise (AWGN) channel. The traditional BP algorithm cannot adapt efficiently to the statistical change of the AWGN channel. Particle filter is a algorithm to estimate a variable of interest as it evolves over time. In this paper, we use particle filter to estimate the noise power and feed back to the BP algorithm in real time. We found that compared with the traditional BP algorithm with fixed estimated noise power, BP algorithm based on particle filter not only give a good real-time estimate for the channel noise, but also achieve a lower decoding error rate.

## Extrinsic tree decoding

- **Status**: ✅
- **Reason**: 수정된 유한 계산트리상 LDPC 디코딩(extrinsic tree decoding) 신규 디코더 - 이식 가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5054754
- **Type**: conference
- **Published**: 18-20 Marc
- **Authors**: Eric Psota, Lance C. Perez
- **PDF**: https://ieeexplore.ieee.org/document/5054754
- **Abstract**: A new decoding method, called extrinsic tree decoding, is presented for decoding low-density parity-check codes on modified finite computation trees. The proposed method maintains similar performance to that of existing iterative decoders, while providing a decoding method for which realistic upper bounds can be computed for practical codes.

## A random construction of LDPC codes using a sub-optimal search algorithm

- **Status**: ✅
- **Reason**: girth 제약 기반 LDPC 패리티검사행렬 컬럼별 구성(MSP 알고리즘), 코드설계 기법(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:5233993
- **Type**: conference
- **Published**: 17-19 Marc
- **Authors**: Seif Shebl, Nawal El-Fishawy, Atef Abou Elazm +1
- **PDF**: https://ieeexplore.ieee.org/document/5233993
- **Abstract**: In this paper, a method for constructing Low-Density Parity-Check (LDPC) codes of good performance in terms of Bit Error Rate (BER) using a computer search algorithm is presented. First, LDPC codes and encoding along with its Tanner graph representation is described. Then, a detailed description of the proposed construction algorithm is given. A Modified Shortest-Path (MSP) Algorithm of lower complexity is applied to obtain a code graph of the desired structure. The proposed algorithm works directly on the parity-check matrix of the LDPC code. The parity-check matrix of the code is constructed column by column subject to the bit-degree and girth constraints. Using the proposed algorithm, both regular and irregular LDPC codes have been constructed. Furthermore, not only have the girth been improved but also the rate of LDPC codes. Finally, by simulation results the constructed codes were shown to perform well over an additive white Gaussian noise (AWGN) channel.
