# IEEE Xplore — 2005-07 (1차선별 통과)


## A new LDPC decoding algorithm aided by segmented cyclic redundancy checks for magnetic recording channels

- **Status**: ✅
- **Reason**: CRC 보조 LDPC 디코딩+조기정지 기준, 부호 비의존 디코더 기법(C)이 NAND LDPC에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1463295
- **Type**: journal
- **Published**: July 2005
- **Authors**: Yeong-Hyeon Kwon, Mi-Kyung Oh, Dong-Jo Park
- **PDF**: https://ieeexplore.ieee.org/document/1463295
- **Abstract**: We introduce a new low-density parity-check (LDPC) decoding algorithm that exploits the cyclic redundancy check (CRC) information of data segments. By using the error detection property of the CRC, we can successively decode data segments of a codeword corrupted by random errors and erasures. The key idea is that the messages from the variable nodes with correct checksum are fixed to deterministic log likelihood ratio values during LDPC iterative decoding. This approach improves the decoding speed and codeword error rate without significant modification of the LDPC decoding structure. Moreover, the CRC is also used for an early stopping criterion of LDPC decoding. Simulation results verify our claims.

## Decreasing the complexity of LDPC iterative decoders

- **Status**: ✅
- **Reason**: 입력 버퍼로 LDPC 반복 디코더 복잡도 감소, 디코더/HW 복잡도 절감 기법(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1461688
- **Type**: journal
- **Published**: July 2005
- **Authors**: G. Bosco, G. Montorsi, S. Benedetto
- **PDF**: https://ieeexplore.ieee.org/document/1461688
- **Abstract**: In this letter we analyze the performance of a low-density parity-check iterative decoder which makes use of an additional buffer at its input, whose function is to decrease the overall complexity of the decoding circuit. We propose a semi-analytical technique that permits the evaluation of the optimum buffer length for each analyzed code.

## Nonuniform error correction using low-density parity-check codes

- **Status**: ✅
- **Reason**: 비균일 채널 LDPC 부호 설계+낮은 error floor+UEP, 코드설계 기법(E)이 NAND 비균일 채널에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1459071
- **Type**: journal
- **Published**: July 2005
- **Authors**: H. Pishro-Nik, N. Rahnavard, F. Fekri
- **PDF**: https://ieeexplore.ieee.org/document/1459071
- **Abstract**: This correspondence introduces a framework to design and analyze low-density parity-check (LDPC) codes over nonuniform channels. We study LDPC codes for channels with nonuniform noise distributions, rate-adaptive coding, and unequal error protection. First, we propose a technique to design LDPC codes for volume holographic memory (VHM) systems for which the noise distribution is nonuniform. We show that the proposed coding scheme has an easy design procedure and results in efficient codes for holographic memories. An important property of the proposed technique is the design of the codes that have a low error floor and low variable node degrees, while maintaining performance close to the Shannon limit. We then show that punctured LDPC codes can be studied as a special case of our design methodology for nonuniform channels. Finally, we propose a method to generate LDPC codes that can provide unequal error protection in addition to having a good overall performance. Moreover, the highly protected bits can be decoded without requiring the entire word to be decoded.

## Reduced-Complexity Decoding of LDPC Codes

- **Status**: ✅
- **Reason**: LLR-BP 감복잡도 디코딩(정규화/오프셋 min-sum, 유한 양자화 분석), NAND LDPC 핵심 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1468447
- **Type**: journal
- **Published**: July 2005
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/1468447
- **Abstract**: Reduced-Complexity Decoding of LDPC Codes Various log-likelihood-ratio-based belief-propagation (LLR- BP) decoding algorithms and their reduced-complexity derivatives for low-density parity-check (LDPC) codes are presented. Numerically accurate representations of the check-node update computation used in LLR-BP decoding are described. Furthermore, approximate representation of the decoding computations are shown to achieve a reduction in complexity, by simplifying the check-node update or symbol-node update, or both. In particular, two main approaches for simplified check-node updates are presented that are based on the so-called min-sum approximation coupled with either a normalization term or an additive offset term. Density evolution is used to analyze the performance of these decoding algorithms, to determine the optimum values of the key parameters, and to evaluate finite quantization effects. Simulation results show that these reduced-complexity decoding algorithms for LDPC codes achieve a performance very close to that of the BP algorithm. The unified treatment of decoding techniques for LDPC codes presented here provides flexibility in selecting the appropriate scheme from a performance, latency, computational complexity, and memory-requirement perspective.
