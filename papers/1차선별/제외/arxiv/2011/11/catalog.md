# arXiv — 2011-11


## Efficient Joint Network-Source Coding for Multiple Terminals with Side Information

- **Status**: ❌
- **Reason**: 네트워크-소스 결합 부호화+신드롬 디코딩 매트릭스 sparsification—소스코딩/rate-distortion 영역이라 채널 ECC 아님, 제외
- **ID**: arxiv:1111.5735v1
- **Type**: preprint
- **Published**: 2011-11-24
- **Authors**: Chen Avin, Michael Borokhovich, Asaf Cohen +1
- **PDF**: https://arxiv.org/pdf/1111.5735v1
- **Abstract**: Consider the problem of source coding in networks with multiple receiving terminals, each having access to some kind of side information. In this case, standard coding techniques are either prohibitively complex to decode, or require network-source coding separation, resulting in sub-optimal transmission rates. To alleviate this problem, we offer a joint network-source coding scheme based on matrix sparsification at the code design phase, which allows the terminals to use an efficient decoding procedure (syndrome decoding using LDPC), despite the network coding throughout the network. Via a novel relation between matrix sparsification and rate-distortion theory, we give lower and upper bounds on the best achievable sparsification performance. These bounds allow us to analyze our scheme, and, in particular, show that in the limit where all receivers have comparable side information (in terms of conditional entropy), or, equivalently, have weak side information, a vanishing density can be achieved. As a result, efficient decoding is possible at all terminals simultaneously. Simulation results motivate the use of this scheme at non-limiting rates as well.

## Efficient Network for Non-Binary QC-LDPC Decoder

- **Status**: ❌
- **Reason**: non-binary QC-LDPC 디코더 네트워크—비이진 LDPC는 NAND 바이너리 표준에서 제외
- **ID**: arxiv:1111.0703v1
- **Type**: preprint
- **Published**: 2011-11-03
- **Authors**: Chuan Zhang, Keshab K. Parhi
- **PDF**: https://arxiv.org/pdf/1111.0703v1
- **Abstract**: This paper presents approaches to develop efficient network for non-binary quasi-cyclic LDPC (QC-LDPC) decoders. By exploiting the intrinsic shifting and symmetry properties of the check matrices, significant reduction of memory size and routing complexity can be achieved. Two different efficient network architectures for Class-I and Class-II non-binary QC-LDPC decoders have been proposed, respectively. Comparison results have shown that for the code of the 64-ary (1260, 630) rate-0.5 Class-I code, the proposed scheme can save more than 70.6% hardware required by shuffle network than the state-of-the-art designs. The proposed decoder example for the 32-ary (992, 496) rate-0.5 Class-II code can achieve a 93.8% shuffle network reduction compared with the conventional ones. Meanwhile, based on the similarity of Class-I and Class-II codes, similar shuffle network is further developed to incorporate both classes of codes at a very low cost.
