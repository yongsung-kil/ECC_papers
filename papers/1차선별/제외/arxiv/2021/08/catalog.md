# arXiv — 2021-08


## $\ell_p$-Spread and Restricted Isometry Properties of Sparse Random Matrices

- **Status**: ❌
- **Reason**: 순수 이론(sparse random matrix의 ℓp-spread/RIP); LDPC는 비유로만 언급, 떼어낼 디코더/HW/코드설계 기여 없음
- **ID**: arxiv:2108.13578v2
- **Type**: preprint
- **Published**: 2021-08-31
- **Authors**: Venkatesan Guruswami, Peter Manohar, Jonathan Mosheiff
- **PDF**: https://arxiv.org/pdf/2108.13578v2
- **Abstract**: Random subspaces $X$ of $\mathbb{R}^n$ of dimension proportional to $n$ are, with high probability, well-spread with respect to the $\ell_2$-norm. Namely, every nonzero $x \in X$ is "robustly non-sparse" in the following sense: $x$ is $\varepsilon \|x\|_2$-far in $\ell_2$-distance from all $δn$-sparse vectors, for positive constants $\varepsilon, δ$ bounded away from $0$. This "$\ell_2$-spread" property is the natural counterpart, for subspaces over the reals, of the minimum distance of linear codes over finite fields, and corresponds to $X$ being a Euclidean section of the $\ell_1$ unit ball. Explicit $\ell_2$-spread subspaces of dimension $Ω(n)$, however, are unknown, and the best known constructions (which achieve weaker spread properties), are analogs of low density parity check (LDPC) codes over the reals, i.e., they are kernels of sparse matrices.   We study the spread properties of the kernels of sparse random matrices. Rather surprisingly, we prove that with high probability such subspaces contain vectors $x$ that are $o(1)\cdot \|x\|_2$-close to $o(n)$-sparse with respect to the $\ell_2$-norm, and in particular are not $\ell_2$-spread.   On the other hand, for $p < 2$ we prove that such subspaces are $\ell_p$-spread with high probability. Moreover, we show that a random sparse matrix has the stronger restricted isometry property (RIP) with respect to the $\ell_p$ norm, and this follows solely from the unique expansion of a random biregular graph, yielding a somewhat unexpected generalization of a similar result for the $\ell_1$ norm [BGI+08]. Instantiating this with explicit expanders, we obtain the first explicit constructions of $\ell_p$-RIP matrices for $1 \leq p < p_0$, where $1 < p_0 < 2$ is an absolute constant.

## Reliable Spread Spectrum Communication Systems by Using Low-Density Parity-Check Codes

- **Status**: ❌
- **Reason**: 무선 spread-spectrum에 표준 LDPC 결합 응용; 떼어낼 새 디코더/코드설계 기법 없음
- **ID**: arxiv:2108.09627v1
- **Type**: preprint
- **Published**: 2021-08-22
- **Authors**: Hadi Khodaei Jooshin, Mahdi Nangir
- **PDF**: https://arxiv.org/pdf/2108.09627v1
- **Abstract**: A joint scheme for the channel coding and spectrum spreading communication system is proposed in this paper. The Bit Error Rate (BER) performance of the joint proposed scheme is evaluated and compared with the case of channel coding scheme without spectrum spreading. We employ a single Low-Density Parity Check (LDPC) code for the both channel coding and direct sequence spectrum spreading. We show that the BER performance is significantly improved while the complexity does not increase too. The philosophy behind this achievement is that the spectrum spreading techniques provide the ability of channel noise protection for the communication systems by themselves.

## NB QC-LDPC Coded QAM Signals with Optimized Mapping: Bounds and Simulation Results

- **Status**: ❌
- **Reason**: 비이진(NB GF(2^m)) QC-LDPC + QAM 매핑; non-binary는 제외 대상
- **ID**: arxiv:2108.08716v2
- **Type**: preprint
- **Published**: 2021-08-19
- **Authors**: Irina E. Bocharova, Boris D. Kudryashov, Evgenii P. Ovsyannikov +1
- **PDF**: https://arxiv.org/pdf/2108.08716v2
- **Abstract**: The goal of the paper is to study specific properties of nonbinary low-density parity-check (NB LDPC) codes when used in coded modulation systems. The paper is focused on the practically important NB LDPC codes over extensions of the Galois field GF$(2^m)$ with $m \le 6$ used with QAM signaling. Performance of NB QC LDPC coded transmission strongly depends on mapping of nonbinary symbols to signal constellation points. We obtain a random coding bound on the maximum-likelihood decoding error probability for an ensemble of random irregular NB LDPC codes used with QAM signaling for specific symbol-to-signal point mappings. This bound is based on the ensemble average Euclidean distance spectra derived for these mappings. The simulation results for the belief-propagation decoding in the coded modulation schemes with the NB quasi-cyclic (QC)-LDPC codes under different mappings are given. Comparisons with the optimized binary QC-LDPC codes in the WiFi and 5G standards, as well as with the new bound, are performed.
