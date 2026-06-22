# arXiv — 2010-01 (1차선별 통과)


## Worst Configurations (Instantons) for Compressed Sensing over Reals: a Channel Coding Approach

- **Status**: ✅
- **Reason**: LDPC error floor의 instanton(최악 에러패턴) 탐색 알고리즘 일반화 — error floor 분석 기법으로 코드설계에 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1001.5113v2
- **Type**: preprint
- **Published**: 2010-01-28
- **Authors**: Shashi Kiran Chilappagari, Michael Chertkov, Bane Vasic
- **PDF**: https://arxiv.org/pdf/1001.5113v2
- **Abstract**: We consider the Linear Programming (LP) solution of the Compressed Sensing (CS) problem over reals, also known as the Basis Pursuit (BasP) algorithm. The BasP allows interpretation as a channel-coding problem, and it guarantees error-free reconstruction with a properly chosen measurement matrix and sufficiently sparse error vectors. In this manuscript, we examine how the BasP performs on a given measurement matrix and develop an algorithm to discover the sparsest vectors for which the BasP fails. The resulting algorithm is a generalization of our previous results on finding the most probable error-patterns degrading performance of a finite size Low-Density Parity-Check (LDPC) code in the error-floor regime. The BasP fails when its output is different from the actual error-pattern. We design a CS-Instanton Search Algorithm (ISA) generating a sparse vector, called a CS-instanton, such that the BasP fails on the CS-instanton, while the BasP recovery is successful for any modification of the CS-instanton replacing a nonzero element by zero. We also prove that, given a sufficiently dense random input for the error-vector, the CS-ISA converges to an instanton in a small finite number of steps. The performance of the CS-ISA is illustrated on a randomly generated $120\times 512$ matrix. For this example, the CS-ISA outputs the shortest instanton (error vector) pattern of length 11.

## Girth-12 Quasi-Cyclic LDPC Codes with Consecutive Lengths

- **Status**: ✅
- **Reason**: girth-12 (3,6) QC-LDPC 구성법(연속 길이) — 바이너리 QC-LDPC 코드설계 기법(E), NAND 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1001.3916v1
- **Type**: preprint
- **Published**: 2010-01-22
- **Authors**: Guohua Zhang, Xinmei Wang
- **PDF**: https://arxiv.org/pdf/1001.3916v1
- **Abstract**: A method to construct girth-12 (3,L) quasi-cyclic low-density parity-check (QC-LDPC) codes with all lengths larger than a certain given number is proposed, via a given girth-12 code subjected to some constraints. The lengths of these codes can be arbitrary integers of the form LP, provided that P is larger than a tight lower bound determined by the maximal element within the exponent matrix of the given girth-12 code. By applying the method to the case of row-weight six, we obtained a family of girth-12 (3,6) QC-LDPC codes for arbitrary lengths above 2688, which includes 30 member codes with shorter code lengths compared with the shortest girth-12 (3,6) QC-LDPC codes reported by O'Sullivan.

## Multilevel Decoders Surpassing Belief Propagation on the Binary Symmetric Channel

- **Status**: ✅
- **Reason**: trapping set 기반 신규 3비트 양자화 메시지패싱 디코더(BP/min-sum 능가) — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1001.3421v2
- **Type**: preprint
- **Published**: 2010-01-19
- **Authors**: Shiva Kumar Planjery, David Declercq, Shashi Kiran Chilappagari +1
- **PDF**: https://arxiv.org/pdf/1001.3421v2
- **Abstract**: In this paper, we propose a new class of quantized message-passing decoders for LDPC codes over the BSC. The messages take values (or levels) from a finite set. The update rules do not mimic belief propagation but instead are derived using the knowledge of trapping sets. We show that the update rules can be derived to correct certain error patterns that are uncorrectable by algorithms such as BP and min-sum. In some cases even with a small message set, these decoders can guarantee correction of a higher number of errors than BP and min-sum. We provide particularly good 3-bit decoders for 3-left-regular LDPC codes. They significantly outperform the BP and min-sum decoders, but more importantly, they achieve this at only a fraction of the complexity of the BP and min-sum decoders.

## Check Reliability Based Bit-Flipping Decoding Algorithms for LDPC Codes

- **Status**: ✅
- **Reason**: LDPC용 신규 check-reliability 기반 bit-flipping 디코더(HD/SD), 부호 비의존 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1001.2503v1
- **Type**: preprint
- **Published**: 2010-01-14
- **Authors**: Chi-Yuan Chang, Yu T. Su, Yu-Liang Chen +1
- **PDF**: https://arxiv.org/pdf/1001.2503v1
- **Abstract**: We introduce new reliability definitions for bit and check nodes. Maximizing global reliability, which is the sum reliability of all bit nodes, is shown to be equivalent to minimizing a decoding metric which is closely related to the maximum likelihood decoding metric. We then propose novel bit-flipping (BF) decoding algorithms that take into account the check node reliability. Both hard-decision (HD) and soft-decision (SD) versions are considered. The former performs better than the conventional BF algorithm and, in most cases, suffers less than 1 dB performance loss when compared with some well known SD BF decoders. For one particular code it even outperforms those SD BF decoders. The performance of the SD version is superior to that of SD BF decoders and is comparable to or even better than that of the sum-product algorithm (SPA). The latter is achieved with a complexity much less than that required by the SPA.

## Divide & Concur and Difference-Map BP Decoders for LDPC Codes

- **Status**: ✅
- **Reason**: Divide&Concur 기반 DMBP 디코더로 LDPC error-floor 대폭 개선, 이식 가능 BP 변형 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1001.1730v1
- **Type**: preprint
- **Published**: 2010-01-11
- **Authors**: Jonathan S. Yedidia, Yige Wang, Stark C. Draper
- **PDF**: https://arxiv.org/pdf/1001.1730v1
- **Abstract**: The "Divide and Concur'' (DC) algorithm, recently introduced by Gravel and Elser, can be considered a competitor to the belief propagation (BP) algorithm, in that both algorithms can be applied to a wide variety of constraint satisfaction, optimization, and probabilistic inference problems. We show that DC can be interpreted as a message-passing algorithm on a constraint graph, which helps make the comparison with BP more clear. The "difference-map'' dynamics of the DC algorithm enables it to avoid "traps'' which may be related to the "trapping sets'' or "pseudo-codewords'' that plague BP decoders of low-density parity check (LDPC) codes in the error-floor regime.   We investigate two decoders for low-density parity-check (LDPC) codes based on these ideas. The first decoder is based directly on DC, while the second decoder borrows the important "difference-map'' concept from the DC algorithm and translates it into a BP-like decoder. We show that this "difference-map belief propagation'' (DMBP) decoder has dramatically improved error-floor performance compared to standard BP decoders, while maintaining a similar computational complexity. We present simulation results for LDPC codes on the additive white Gaussian noise and binary symmetric channels, comparing DC and DMBP decoders with other decoders based on BP, linear programming, and mixed-integer linear programming.
