# arXiv — 2007-05 (1차선별 통과)


## Interior Point Decoding for Linear Vector Channels

- **Status**: ✅
- **Reason**: Interior point decoding — 볼록최적화 기반 신규 LDPC 디코더, 부분응답/ISI 채널서 BER 개선, 이식 가능(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:0705.3990v2
- **Type**: preprint
- **Published**: 2007-05-28
- **Authors**: Tadashi Wadayama
- **PDF**: https://arxiv.org/pdf/0705.3990v2
- **Abstract**: In this paper, a novel decoding algorithm for low-density parity-check (LDPC) codes based on convex optimization is presented. The decoding algorithm, called interior point decoding, is designed for linear vector channels. The linear vector channels include many practically important channels such as inter symbol interference channels and partial response channels. It is shown that the maximum likelihood decoding (MLD) rule for a linear vector channel can be relaxed to a convex optimization problem, which is called a relaxed MLD problem. The proposed decoding algorithm is based on a numerical optimization technique so called interior point method with barrier function. Approximate variations of the gradient descent and the Newton methods are used to solve the convex optimization problem. In a decoding process of the proposed algorithm, a search point always lies in the fundamental polytope defined based on a low-density parity-check matrix. Compared with a convectional joint message passing decoder, the proposed decoding algorithm achieves better BER performance with less complexity in the case of partial response channels in many cases.

## Degree Optimization and Stability Condition for the Min-Sum Decoder

- **Status**: ✅
- **Reason**: Min-sum 디코더의 안정성 조건·차수분포 최적화 및 스케일링 MS(1/alpha) 변형 — 이식 가능 디코더 알고리즘(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:0705.1345v1
- **Type**: preprint
- **Published**: 2007-05-09
- **Authors**: Kapil Bhattad, Vishwambhar Rathi, Ruediger Urbanke
- **PDF**: https://arxiv.org/pdf/0705.1345v1
- **Abstract**: The min-sum (MS) algorithm is arguably the second most fundamental algorithm in the realm of message passing due to its optimality (for a tree code) with respect to the {\em block error} probability \cite{Wiberg}. There also seems to be a fundamental relationship of MS decoding with the linear programming decoder \cite{Koetter}. Despite its importance, its fundamental properties have not nearly been studied as well as those of the sum-product (also known as BP) algorithm.   We address two questions related to the MS rule. First, we characterize the stability condition under MS decoding. It turns out to be essentially the same condition as under BP decoding. Second, we perform a degree distribution optimization. Contrary to the case of BP decoding, under MS decoding the thresholds of the best degree distributions for standard irregular LDPC ensembles are significantly bounded away from the Shannon threshold. More precisely, on the AWGN channel, for the best codes that we find, the gap to capacity is 1dB for a rate 0.3 code and it is 0.4dB when the rate is 0.9 (the gap decreases monotonically as we increase the rate).   We also used the optimization procedure to design codes for modified MS algorithm where the output of the check node is scaled by a constant $1/α$. For $α= 1.25$, we observed that the gap to capacity was lesser for the modified MS algorithm when compared with the MS algorithm. However, it was still quite large, varying from 0.75 dB to 0.2 dB for rates between 0.3 and 0.9.   We conclude by posing what we consider to be the most important open questions related to the MS algorithm.

## The Design of Efficiently-Encodable Rate-Compatible LDPC Codes

- **Status**: ✅
- **Reason**: rate-compatible puncturing용 비정규 LDPC 구성 + shift-register 선형부호화 — 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:0705.0543v1
- **Type**: preprint
- **Published**: 2007-05-03
- **Authors**: Jaehong Kim, Aditya Ramamoorthy, Steven W. McLaughlin
- **PDF**: https://arxiv.org/pdf/0705.0543v1
- **Abstract**: We present a new class of irregular low-density parity-check (LDPC) codes for moderate block lengths (up to a few thousand bits) that are well-suited for rate-compatible puncturing. The proposed codes show good performance under puncturing over a wide range of rates and are suitable for usage in incremental redundancy hybrid-automatic repeat request (ARQ) systems. In addition, these codes are linear-time encodable with simple shift-register circuits. For a block length of 1200 bits the codes outperform optimized irregular LDPC codes and extended irregular repeat-accumulate (eIRA) codes for all puncturing rates 0.6~0.9 (base code performance is almost the same) and are particularly good at high puncturing rates where good puncturing performance has been previously difficult to achieve.

## Reliable Memories Built from Unreliable Components Based on Expander Graphs

- **Status**: ✅
- **Reason**: LDPC 기반 신뢰메모리 아키텍처, Gallager B/expander 디코딩 — 결함성분 메모리 ECC로 이식 가능(B/C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:0705.0044v1
- **Type**: preprint
- **Published**: 2007-05-01
- **Authors**: Shashi Kiran Chilappagari, Bane Vasic
- **PDF**: https://arxiv.org/pdf/0705.0044v1
- **Abstract**: In this paper, memories built from components subject to transient faults are considered. A fault-tolerant memory architecture based on low-density parity-check codes is proposed and the existence of reliable memories for the adversarial failure model is proved. The proof relies on the expansion property of the underlying Tanner graph of the code. An equivalence between the Taylor-Kuznetsov (TK) scheme and Gallager B algorithm is established and the results are extended to the independent failure model. It is also shown that the proposed memory architecture has lower redundancy compared to the TK scheme. The results are illustrated with specific numerical examples.
