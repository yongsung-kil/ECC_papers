# arXiv — 2015-02


## On the Energy Complexity of LDPC Decoder Circuits

- **Status**: ❌
- **Reason**: LDPC 디코더 회로 에너지 복잡도 스케일링 순수 이론 bound, 구체적 디코더/HW/구성으로 안 이어짐
- **ID**: arxiv:1502.07999v1
- **Type**: preprint
- **Published**: 2015-02-27
- **Authors**: Christopher Blake, Frank R. Kschischang
- **PDF**: https://arxiv.org/pdf/1502.07999v1
- **Abstract**: It is shown that in a sequence of randomly generated bipartite configurations with number of left nodes approaching infinity, the probability that a particular configuration in the sequence has a minimum bisection width proportional to the number of vertices in the configuration approaches $1$ so long as a sufficient condition on the node degree distribution is satisfied. This graph theory result implies an almost sure $Ω\left(n^{2}\right)$ scaling rule for the energy of capacity-approaching LDPC decoder circuits that directly instantiate their Tanner Graphs and are generated according to a uniform configuration model, where $n$ is the block length of the code. For a sequence of circuits that have a full set of check nodes but do not necessarily directly instantiate a Tanner graph, this implies an $Ω\left(n^{1.5}\right)$ scaling rule. In another theorem, it is shown that all (as opposed to almost all) capacity-approaching LDPC decoding circuits that directly implement their Tanner graphs must have energy that scales as $Ω\left(n\left(\log n\right)^{2}\right)$. These results further imply scaling rules for the energy of LDPC decoder circuits as a function of gap to capacity.

## An Upper Bound on the Minimum Distance of LDPC Codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC의 최소거리 상한(순수 이론 bound), 디코더/HW/구성으로 안 이어짐 — 비이진+이론 모두 제외
- **ID**: arxiv:1502.06874v1
- **Type**: preprint
- **Published**: 2015-02-24
- **Authors**: Alexey Frolov
- **PDF**: https://arxiv.org/pdf/1502.06874v1
- **Abstract**: In [1] a syndrome counting based upper bound on the minimum distance of regular binary LDPC codes is given. In this paper we extend the bound to the case of irregular and generalized LDPC codes over GF(q). The comparison to the lower bound for LDPC codes over GF(q) and to the upper bound for non-binary codes is done. The new bound is shown to lie under the Gilbert-Varshamov bound at high rates.

## On the Multiple Threshold Decoding of LDPC codes over GF(q)

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC의 다중임계값 다수결 디코딩 — 비이진 LDPC라 제외
- **ID**: arxiv:1502.06871v1
- **Type**: preprint
- **Published**: 2015-02-24
- **Authors**: Alexey Frolov, Victor Zyablov
- **PDF**: https://arxiv.org/pdf/1502.06871v1
- **Abstract**: We consider the decoding of LDPC codes over GF(q) with the low-complexity majority algorithm from [1]. A modification of this algorithm with multiple thresholds is suggested. A lower estimate on the decoding radius realized by the new algorithm is derived. The estimate is shown to be better than the estimate for a single threshold majority decoder. At the same time the transition to multiple thresholds does not affect the order of complexity.

## LDPC Code Design for Noncoherent Physical Layer Network Coding

- **Status**: ❌
- **Reason**: 표준 DVB-S2/WiMAX 코드 기반 무선 PNC 응용 특이적 차수분포 EXIT 최적화, NAND에 떼어낼 신규 기법 없음
- **ID**: arxiv:1502.05784v1
- **Type**: preprint
- **Published**: 2015-02-20
- **Authors**: Terry Ferrett, Matthew C. Valenti
- **PDF**: https://arxiv.org/pdf/1502.05784v1
- **Abstract**: This work considers optimizing LDPC codes in the physical-layer network coded two-way relay channel using noncoherent FSK modulation. The error-rate performance of channel decoding at the relay node during the multiple-access phase was improved through EXIT-based optimization of Tanner graph variable node degree distributions. Codes drawn from the DVB-S2 and WiMAX standards were used as a basis for design and performance comparison. The computational complexity characteristics of the standard codes were preserved in the optimized codes by maintaining the extended irregular repeat-accumulate (eIRA). The relay receiver performance was optimized considering two modulation orders M = {4, 8} using iterative decoding in which the decoder and demodulator refine channel estimates by exchanging information. The code optimization procedure yielded unique optimized codes for each case of modulation order and available channel state information. Performance of the standard and optimized codes were measured using Monte Carlo simulation in the flat Rayleigh fading channel, and error rate improvements up to 1.2 dB are demonstrated depending on system parameters.

## Rewriting Flash Memories by Message Passing

- **Status**: ❌
- **Reason**: 플래시 WOM(rewriting)+BEQ 소스코딩 기반, 채널 ECC가 아니며 BCH 결합 — 소스코딩/비-LDPC라 제외
- **ID**: arxiv:1502.00189v1
- **Type**: preprint
- **Published**: 2015-02-01
- **Authors**: Eyal En Gad, Wentao Huang, Yue Li +1
- **PDF**: https://arxiv.org/pdf/1502.00189v1
- **Abstract**: This paper constructs WOM codes that combine rewriting and error correction for mitigating the reliability and the endurance problems in flash memory. We consider a rewriting model that is of practical interest to flash applications where only the second write uses WOM codes. Our WOM code construction is based on binary erasure quantization with LDGM codes, where the rewriting uses message passing and has potential to share the efficient hardware implementations with LDPC codes in practice. We show that the coding scheme achieves the capacity of the rewriting model. Extensive simulations show that the rewriting performance of our scheme compares favorably with that of polar WOM code in the rate region where high rewriting success probability is desired. We further augment our coding schemes with error correction capability. By drawing a connection to the conjugate code pairs studied in the context of quantum error correction, we develop a general framework for constructing error-correction WOM codes. Under this framework, we give an explicit construction of WOM codes whose codewords are contained in BCH codes.
