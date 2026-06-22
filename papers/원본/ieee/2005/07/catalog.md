# IEEE Xplore — 2005-07


## A new LDPC decoding algorithm aided by segmented cyclic redundancy checks for magnetic recording channels

- **Status**: ✅
- **Reason**: CRC 보조 LDPC 디코딩+조기정지 기준, 부호 비의존 디코더 기법(C)이 NAND LDPC에 이식 가능
- **ID**: ieee:1463295
- **Type**: journal
- **Published**: July 2005
- **Authors**: Yeong-Hyeon Kwon, Mi-Kyung Oh, Dong-Jo Park
- **PDF**: https://ieeexplore.ieee.org/document/1463295
- **Abstract**: We introduce a new low-density parity-check (LDPC) decoding algorithm that exploits the cyclic redundancy check (CRC) information of data segments. By using the error detection property of the CRC, we can successively decode data segments of a codeword corrupted by random errors and erasures. The key idea is that the messages from the variable nodes with correct checksum are fixed to deterministic log likelihood ratio values during LDPC iterative decoding. This approach improves the decoding speed and codeword error rate without significant modification of the LDPC decoding structure. Moreover, the CRC is also used for an early stopping criterion of LDPC decoding. Simulation results verify our claims.

## Irregular LDPC codes as concatenation regular LDPC codes

- **Status**: ❌
- **Reason**: 정규 LDPC 연접으로 비정규 구성하는 threshold 분석, 새 디코더/HW 없는 분석 위주이나 코드설계 변형 가능성 약함
- **ID**: ieee:1461686
- **Type**: journal
- **Published**: July 2005
- **Authors**: M. Fossorier, N. Miladinovic
- **PDF**: https://ieeexplore.ieee.org/document/1461686
- **Abstract**: In this letter, the construction of irregular LDPC codes obtained by concatenating regular ones is considered. These codes are analyzed for the binary symmetric channel (BSC). It is shown via proper distribution evolution that such concatenated codes have in general a threshold value weaker (but not necessarily much different) than their unconstrained counterparts for the BSC. On the other hand, they can offer advantages in term of convergence and error performance for lengths of practical interest and long enough to validate the degree distribution selection.

## A factor graph approach to iterative channel estimation and LDPC decoding over fading channels

- **Status**: ❌
- **Reason**: fading 채널 결합 채널추정+LDPC 디코딩, 무선 채널 특이적이고 떼어낼 ECC 기법 없음
- **ID**: ieee:1512089
- **Type**: journal
- **Published**: July 2005
- **Authors**: Huaning Niu, Manyuan Shen, J.A. Ritcey +1
- **PDF**: https://ieeexplore.ieee.org/document/1512089
- **Abstract**: This letter provides a comparative study of joint channel estimation and low-density parity-check decoding algorithms for flat Rayleigh fading channels based on the receiver factor graphs. Two approaches for joint channel estimation and decoding are proposed. Intensive simulation studies are carried out to evaluate the receiver sensitivity to the choice of the factor graph. Results show that when channel statistical information is not available at the receiver, a low-pass filtering approach gives a more robust and simpler solution, and it is only 0.5 dB worse than the optimum Wiener filtering. All methods have about 2 dB improvements over the noniterative receivers.

## Average coset weight distributions of Gallager's LDPC code ensemble

- **Status**: ❌
- **Reason**: Gallager 앙상블 coset weight 분포의 순수 조합론적 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:1459072
- **Type**: journal
- **Published**: July 2005
- **Authors**: T. Wadayama
- **PDF**: https://ieeexplore.ieee.org/document/1459072
- **Abstract**: In this correspondence, the average coset weight distributions of Gallager's low-density parity-check (LDPC) code ensemble are investigated. Gallager's LDPC code ensemble consists of regular mtimesn-LDPC matrices with column weight j and row weight k. The average coset weight distribution can be derived by enumerating the number of parity-check matrices in the ensemble satisfying certain conditions. Based on combinatorial arguments, a formula for the average coset weight distribution will be proved. From the formula, we can show some properties of the average coset weight distributions such as equivalence classes of syndromes, symmetry of the distributions, and a lower bound on coset weight

## Decreasing the complexity of LDPC iterative decoders

- **Status**: ✅
- **Reason**: 입력 버퍼로 LDPC 반복 디코더 복잡도 감소, 디코더/HW 복잡도 절감 기법(C/D) 이식 가능
- **ID**: ieee:1461688
- **Type**: journal
- **Published**: July 2005
- **Authors**: G. Bosco, G. Montorsi, S. Benedetto
- **PDF**: https://ieeexplore.ieee.org/document/1461688
- **Abstract**: In this letter we analyze the performance of a low-density parity-check iterative decoder which makes use of an additional buffer at its input, whose function is to decrease the overall complexity of the decoding circuit. We propose a semi-analytical technique that permits the evaluation of the optimum buffer length for each analyzed code.

## Nonuniform error correction using low-density parity-check codes

- **Status**: ✅
- **Reason**: 비균일 채널 LDPC 부호 설계+낮은 error floor+UEP, 코드설계 기법(E)이 NAND 비균일 채널에 이식 가능
- **ID**: ieee:1459071
- **Type**: journal
- **Published**: July 2005
- **Authors**: H. Pishro-Nik, N. Rahnavard, F. Fekri
- **PDF**: https://ieeexplore.ieee.org/document/1459071
- **Abstract**: This correspondence introduces a framework to design and analyze low-density parity-check (LDPC) codes over nonuniform channels. We study LDPC codes for channels with nonuniform noise distributions, rate-adaptive coding, and unequal error protection. First, we propose a technique to design LDPC codes for volume holographic memory (VHM) systems for which the noise distribution is nonuniform. We show that the proposed coding scheme has an easy design procedure and results in efficient codes for holographic memories. An important property of the proposed technique is the design of the codes that have a low error floor and low variable node degrees, while maintaining performance close to the Shannon limit. We then show that punctured LDPC codes can be studied as a special case of our design methodology for nonuniform channels. Finally, we propose a method to generate LDPC codes that can provide unequal error protection in addition to having a good overall performance. Moreover, the highly protected bits can be decoded without requiring the entire word to be decoded.

## Capacity-achieving ensembles for the binary erasure channel with bounded complexity

- **Status**: ❌
- **Reason**: BEC용 capacity-achieving IRA 앙상블+디코딩 복잡도 이론 하한; 순수 이론으로 NAND 이식 디코더·구성 없음
- **ID**: ieee:1459047
- **Type**: journal
- **Published**: July 2005
- **Authors**: H.D. Pfister, I. Sason, R. Urbanke
- **PDF**: https://ieeexplore.ieee.org/document/1459047
- **Abstract**: We present two sequences of ensembles of nonsystematic irregular repeat-accumulate (IRA) codes which asymptotically (as their block length tends to infinity) achieve capacity on the binary erasure channel (BEC) with bounded complexity per information bit. This is in contrast to all previous constructions of capacity-achieving sequences of ensembles whose complexity grows at least like the log of the inverse of the gap (in rate) to capacity. The new bounded complexity result is achieved by puncturing bits, and allowing in this way a sufficient number of state nodes in the Tanner graph representing the codes. We derive an information-theoretic lower bound on the decoding complexity of randomly punctured codes on graphs. The bound holds for every memoryless binary-input output-symmetric (MBIOS) channel and is refined for the binary erasure channel.

## Reduced-Complexity Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LLR-BP 감복잡도 디코딩(정규화/오프셋 min-sum, 유한 양자화 분석), NAND LDPC 핵심 디코더 기법(C)
- **ID**: ieee:1468447
- **Type**: journal
- **Published**: July 2005
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1468447
- **Abstract**: Reduced-Complexity Decoding of LDPC Codes Various log-likelihood-ratio-based belief-propagation (LLR- BP) decoding algorithms and their reduced-complexity derivatives for low-density parity-check (LDPC) codes are presented. Numerically accurate representations of the check-node update computation used in LLR-BP decoding are described. Furthermore, approximate representation of the decoding computations are shown to achieve a reduction in complexity, by simplifying the check-node update or symbol-node update, or both. In particular, two main approaches for simplified check-node updates are presented that are based on the so-called min-sum approximation coupled with either a normalization term or an additive offset term. Density evolution is used to analyze the performance of these decoding algorithms, to determine the optimum values of the key parameters, and to evaluate finite quantization effects. Simulation results show that these reduced-complexity decoding algorithms for LDPC codes achieve a performance very close to that of the BP algorithm. The unified treatment of decoding techniques for LDPC codes presented here provides flexibility in selecting the appropriate scheme from a performance, latency, computational complexity, and memory-requirement perspective.

## Trellis and convolutional precoding for transmitter-based interference presubtraction

- **Status**: ❌
- **Reason**: THP 프리코딩+trellis shaping, LDPC 무관 비-LDPC 통신 특이 기법
- **ID**: ieee:1468444
- **Type**: journal
- **Published**: July 2005
- **Authors**: Wei Yu, D.P. Varodayan, J.M. Cioffi
- **PDF**: https://ieeexplore.ieee.org/document/1468444
- **Abstract**: This paper studies the combination of practical trellis and convolution codes with Tomlinson-Harashima precoding (THP) for the presubtraction of multiuser interference that is known at the transmitter but not known at the receiver. It is well known that a straightforward application of THP suffers power, modulo, and shaping losses. This paper proposes generalizations of THP that recover some of these losses. At a high signal-to-noise ratio (SNR), the precoding loss is dominated by the shaping loss, which is about 1.53 dB. To recover shaping loss, a trellis-shaping technique is developed that takes into account the knowledge of a noncausal interfering sequence, rather than just the instantaneous interference. At rates of 2 and 3 bits per transmission, trellis shaping is shown to be able to recover almost all of the 1.53-dB shaping loss. At a low SNR, the precoding loss is dominated by power and modulo losses, which can be as large as 3-4 dB. To recover these losses, a technique that incorporates partial interference presubtraction (PIP) within convolutional decoding is developed. At rates of 0.5 and 0.25 bits per transmission, PIP is able to recover 1-1.5 dB of the power loss. For intermediate SNR channels, a combination of the two schemes is shown to recover both power and shaping losses.

## Estimating the minimum distance of turbo-codes using double and triple impulse methods

- **Status**: ❌
- **Reason**: 터보부호 최소거리 추정 기법, 비-LDPC이고 BP에 이식할 디코더 기법 없음
- **ID**: ieee:1461687
- **Type**: journal
- **Published**: July 2005
- **Authors**: S. Crozier, P. Guinand, A. Hunt
- **PDF**: https://ieeexplore.ieee.org/document/1461687
- **Abstract**: A long-standing problem for turbo-codes has been the efficient and accurate determination of the distance spectrum, or even just the minimum distance, for specific interleavers. This letter compares a number of distance estimation techniques and introduces two new approaches based on iterative processing. The new approaches are more reliable and are particularly useful for long blocks with high minimum distances. Distance measurement results are presented for random, high-spread random (HSR) and dithered relative prime (DRP) interleavers.

## Corrections to “Shuffled Iterative Decoding”

- **Status**: ❌
- **Reason**: Shuffled Iterative Decoding 정정문(errata), 초록 없고 신규 기여 없음
- **ID**: ieee:1468445
- **Type**: journal
- **Published**: July 2005
- **Authors**: J. Zhang, M. Fossorier
- **PDF**: https://ieeexplore.ieee.org/document/1468445
- **Abstract**: N/A

## Efficient error correction solutions for OFDM-based wireless video

- **Status**: ❌
- **Reason**: OFDM 무선 비디오용 turbo coding+인터리빙 - 비-LDPC 부호이며 떼어낼 부호 비의존 BP 기법 없음
- **ID**: ieee:1543040
- **Type**: conference
- **Published**: 28-28 July
- **Authors**: M. Lattuada, R. Posega, M. Mattavelli +1
- **PDF**: https://ieeexplore.ieee.org/document/1543040
- **Abstract**: This paper describes a new error correction scheme for flexible and robust high-throughput real time video transmission systems able to cope with difficult high mobility channels. The scheme is based on combining OFDM transmission with turbo coding and deep time interleaving. Simulations of different channel models and field test has shown that the provided solution provides relevant improvement versus DVB-T based solutions.

## Assessing the performance of erasure codes in the wide-area

- **Status**: ❌
- **Reason**: 광역 erasure 코드(RS vs LDPC) 성능 비교, LDPC가 erasure 베이스라인일 뿐 떼어낼 디코더/구성/HW 신규 기법 없음
- **ID**: ieee:1467792
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: R.L. Collins, J.S. Plank
- **PDF**: https://ieeexplore.ieee.org/document/1467792
- **Abstract**: The problem of efficiently retrieving a file that has been broken into blocks and distributed across the wide-area pervades applications that utilize grid, peer-to-peer, and distributed file systems. While the use of erasure codes to improve the fault-tolerance and performance of wide-area file systems has been explored, there has been little work that assesses the performance and quantifies the impact of modifying various parameters. This paper performs such an assessment. We modify our previously defined framework for studying replication in the wide-area to include both Reed-Solomon and low-density parity-check (LDPC) erasure codes. We then use this framework to compare Reed-Solomon and LDPC erasure codes in three wide-area, distributed settings. We conclude that although LDPC codes have an advantage over Reed-Solomon codes in terms of decoding cost, this advantage does not always translate to the best overall performance in wide-area storage situations.

## Small parity-check erasure codes - exploration and observations

- **Status**: ❌
- **Reason**: 소규모 parity-check erasure 코드 탐색, erasure 채널 한정이며 NAND BP ECC에 이식할 디코더/구성 기법 없음
- **ID**: ieee:1467807
- **Type**: conference
- **Published**: 28 June-1 
- **Authors**: J.S. Plank, A.L. Buchsbaum, R.L. Collins +1
- **PDF**: https://ieeexplore.ieee.org/document/1467807
- **Abstract**: Erasure codes have profound uses in wide- and medium-area storage applications. While infinite-size codes have been developed with optimal properties, there remains a need to develop small codes with optimal properties. In this paper, we provide a framework for exploring very small codes, and we use this framework to derive optimal and near-optimal ones for discrete numbers of data bits and coding bits. These codes have heretofore been unknown and unpublished, and should be useful in practice. We also use our exploration to make observations about upper bounds for these codes, in order to gain a better understanding of them and to spur future derivations of larger, optimal and near-optimal codes.

## Application of erasure decoding in fiber optical systems with FEC

- **Status**: ❌
- **Reason**: 광통신 RS(255,239) error-and-erasure 디코딩 - 비-LDPC(RS) 부호, 떼어낼 LDPC BP 기법 없음
- **ID**: ieee:1528048
- **Type**: conference
- **Published**: 25-27 July
- **Authors**: Bing Xie, Yong Liang Guam, Jian Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/1528048
- **Abstract**: Error-and-erasure decoding scheme is first proposed in optical receivers using FEC. Almost 1.3 dB of additional coding gain at output BER of 10/sup -12/ can be estimated for the intact RS (255,239) coding scheme.

## 10 GBPS over copper lines - state of the art in VLSI

- **Status**: ❌
- **Reason**: 10GBASE-T copper VLSI 일반론, 떼어낼 LDPC 디코더/코드설계 기법 없음
- **ID**: ieee:1530996
- **Type**: conference
- **Published**: 20-24 July
- **Authors**: S. Bates, K. Iniewski
- **PDF**: https://ieeexplore.ieee.org/document/1530996
- **Abstract**: This paper outlines some of the problems that VLSI designers are solving and provides some estimates on feasibility of future CMOS devices. We outline some of the challenges for 10GBASE-T and present some of the performance figures that a 10GBASE-T PHY have to meet.

## LDPC code design for OFDM channel: graph connectivity and information bits positioning

- **Status**: ❌
- **Reason**: OFDM 무선 채널용 irregular LDPC graph connectivity·정보비트 배치 최적화 — 채널 특이적, NAND에 떼어낼 코드설계 기법 없음
- **ID**: ieee:1511324
- **Type**: conference
- **Published**: 14-15 July
- **Authors**: A. de Baynast, A. Sabharwal, B. Aazhang
- **PDF**: https://ieeexplore.ieee.org/document/1511324
- **Abstract**: We present an optimized channel coding scheme for OFDM transmission. In the future wireless standards such IEEE 802.11n, frame error rates (FER) as low as 0.0001 are targeting. Irregular LDPC codes have excellent performance at moderate computational complexity: they are strong candidates for channel coding in such systems. In the context of an OFDM transmission, Mannoni et al. (2002) proposed to optimize the graph connectivity of the irregular LDPC code accordingly to the channel spectrum. However, their codes did not have good performance for a FER range of 0.001-0.0001. In this paper, we propose to optimize the LDPC code in two steps: first, we optimize the graph connectivity in order to get a minimum operational average SNR and therefore excellent FER; then we optimize the information bits placement accordingly to the channel. By simulation, we show that our approach provides substantial performance gain in term of FER over the existing methods (1 dB or more for FER equal to 10/sup -4/).
