# arXiv — 2021-12 (1차선별 통과)


## Concatenated Code Design for Constrained DNA Data Storage with Asymmetric Errors

- **Status**: ✅
- **Reason**: DNA 스토리지용 protograph LDPC 코드 설계 + BP용 LLR 계산법 제시 — 바이너리 코드설계/디코더 기법 이식 가능(B/C/E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2112.09417v1
- **Type**: preprint
- **Published**: 2021-12-17
- **Authors**: Yixin Wang, Li Deng, Md. Noor-A-Rahim +4
- **PDF**: https://arxiv.org/pdf/2112.09417v1
- **Abstract**: DNA Data storage has recently attracted much attention due to its durable preservation and extremely high information density (bits per gram) properties. In this work, we propose a hybrid coding strategy comprising of generalized constrained codes to tackle homopolymer (run-length) limit and a protograph based low-density parity-check (LDPC) code to correct asymmetric nucleotide level (i.e., A/T/C/G) substitution errors that may occur in the process of DNA sequencing. Two sequencing techniques namely, Nanopore sequencer and Illumina sequencer with their equivalent channel models and capacities are analyzed. A coding architecture is proposed to potentially eliminate the catastrophic errors caused by the error-propagation in the constrained decoding while enabling high coding potential. We also show the log likelihood ratio (LLR) calculation method for the belief propagation decoding with this coding architecture. The simulation results and the theoretical analysis show that the proposed coding scheme exhibits good bit-error rate (BER) performance and high coding potential ($\sim1.98$ bits per nucleotide).

## Explicit Abelian Lifts and Quantum LDPC Codes

- **Status**: ✅
- **Reason**: abelian lift로 다양한 circulant 크기의 고전 QC-LDPC 구성을 부산물로 산출 — 바이너리 QC-LDPC 구성 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2112.01647v1
- **Type**: preprint
- **Published**: 2021-12-02
- **Authors**: Fernando Granha Jeronimo, Tushant Mittal, Ryan O'Donnell +2
- **PDF**: https://arxiv.org/pdf/2112.01647v1
- **Abstract**: For an abelian group $H$ acting on the set $[\ell]$, an $(H,\ell)$-lift of a graph $G_0$ is a graph obtained by replacing each vertex by $\ell$ copies, and each edge by a matching corresponding to the action of an element of $H$.   In this work, we show the following explicit constructions of expanders obtained via abelian lifts. For every (transitive) abelian group $H \leqslant \text{Sym}(\ell)$, constant degree $d \ge 3$ and $ε> 0$, we construct explicit $d$-regular expander graphs $G$ obtained from an $(H,\ell)$-lift of a (suitable) base $n$-vertex expander $G_0$ with the following parameters:   (i) $λ(G) \le 2\sqrt{d-1} + ε$, for any lift size $\ell \le 2^{n^δ}$ where $δ=δ(d,ε)$,   (ii) $λ(G) \le ε\cdot d$, for any lift size $\ell \le 2^{n^{δ_0}}$ for a fixed $δ_0 > 0$, when $d \ge d_0(ε)$, or   (iii) $λ(G) \le \widetilde{O}(\sqrt{d})$, for lift size ``exactly'' $\ell = 2^{Θ(n)}$.   As corollaries, we obtain explicit quantum lifted product codes of Panteleev and Kalachev of almost linear distance (and also in a wide range of parameters) and explicit classical quasi-cyclic LDPC codes with wide range of circulant sizes.   Items $(i)$ and $(ii)$ above are obtained by extending the techniques of Mohanty, O'Donnell and Paredes [STOC 2020] for $2$-lifts to much larger abelian lift sizes (as a byproduct simplifying their construction). This is done by providing a new encoding of special walks arising in the trace power method, carefully "compressing'" depth-first search traversals. Result $(iii)$ is via a simpler proof of Agarwal et al. [SIAM J. Discrete Math 2019] at the expense of polylog factors in the expansion.
