# arXiv — 2010-04 (1차선별 통과)


## Analysis of Quasi-Cyclic LDPC codes under ML decoding over the erasure channel

- **Status**: ✅
- **Reason**: QC-LDPC의 순환구조를 이용한 행/열 순열로 ML 디코딩 복잡도 저감 기법(E/C, 바이너리)으로 NAND 부호설계/디코더에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1004.5217v1
- **Type**: preprint
- **Published**: 2010-04-29
- **Authors**: Mathieu Cunche, Valentin Savin, Vincent Roca
- **PDF**: https://arxiv.org/pdf/1004.5217v1
- **Abstract**: In this paper, we show that Quasi-Cyclic LDPC codes can efficiently accommodate the hybrid iterative/ML decoding over the binary erasure channel. We demonstrate that the quasi-cyclic structure of the parity-check matrix can be advantageously used in order to significantly reduce the complexity of the ML decoding. This is achieved by a simple row/column permutation that transforms a QC matrix into a pseudo-band form. Based on this approach, we propose a class of QC-LDPC codes with almost ideal error correction performance under the ML decoding, while the required number of row/symbol operations scales as $k\sqrt{k}$, where $k$ is the number of source symbols.

## Threshold Saturation on BMS Channels via Spatial Coupling

- **Status**: ✅
- **Reason**: 공간결합(SC-LDPC) threshold saturation을 일반 BMS 채널로 확장한 구성/분석으로 바이너리 SC-LDPC 부호설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1004.3742v1
- **Type**: preprint
- **Published**: 2010-04-21
- **Authors**: Shrinivas Kudekar, Cyril Measson, Tom Richardson +1
- **PDF**: https://arxiv.org/pdf/1004.3742v1
- **Abstract**: We consider spatially coupled code ensembles. A particular instance are convolutional LDPC ensembles.  It was recently shown that, for transmission over the binary erasure channel, this coupling increases the belief propagation threshold of the ensemble to the maximum a-priori threshold of the underlying component ensemble.  We report on empirical evidence which suggest that the same phenomenon also occurs when transmission takes place over a general binary memoryless symmetric channel. This is confirmed both by simulations as well as by computing EBP GEXIT curves and by comparing the empirical BP thresholds of coupled ensembles to the empirically determined MAP thresholds of the underlying regular ensembles. We further consider ways of reducing the rate-loss incurred by such constructions.

## Circulant Arrays on Cyclic Subgroups of Finite Fields: Rank Analysis and Construction of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: 유한체 순환부분군 기반 신규 바이너리 QC-LDPC 구성+rank 분석+SPA 빠른 수렴 부분집합 제시로 부호설계(E) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1004.1184v1
- **Type**: preprint
- **Published**: 2010-04-07
- **Authors**: Li Zhang, Shu Lin, Khaled Abdel-Ghaffar +2
- **PDF**: https://arxiv.org/pdf/1004.1184v1
- **Abstract**: This paper consists of three parts. The first part presents a large class of new binary quasi-cyclic (QC)-LDPC codes with girth of at least 6 whose parity-check matrices are constructed based on cyclic subgroups of finite fields. Experimental results show that the codes constructed perform well over the binary-input AWGN channel with iterative decoding using the sum-product algorithm (SPA). The second part analyzes the ranks of the parity-check matrices of codes constructed based on finite fields with characteristic of 2 and gives combinatorial expressions for these ranks. The third part identifies a subclass of constructed QC-LDPC codes that have large minimum distances. Decoding of codes in this subclass with the SPA converges very fast.
