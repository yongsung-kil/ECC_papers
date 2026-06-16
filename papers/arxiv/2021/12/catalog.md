# arXiv — 2021-12


## Logical blocks for fault-tolerant topological quantum computation

- **ID**: arxiv:2112.12160v2
- **Type**: preprint
- **Published**: 2021-12-22
- **Authors**: Hector Bombin, Chris Dawson, Ryan V. Mishmash +3
- **PDF**: https://arxiv.org/pdf/2112.12160v2
- **Abstract**: Logical gates constitute the building blocks of fault-tolerant quantum computation. While quantum error-corrected memories have been extensively studied in the literature, explicit constructions and detailed analyses of thresholds and resource overheads of universal logical gate sets have so far been limited. In this paper, we present a comprehensive framework for universal fault-tolerant logic motivated by the combined need for platform-independent logical gate definitions, flexible and scalable tools for numerical analysis, and exploration of novel schemes for universal logic that improve resource overheads. Central to our framework is the description of logical gates holistically in a way which treats space and time on a similar footing. Focusing on schemes based on surface codes, we introduce explicit, but platform-independent representations of topological logic gates -- called logical blocks -- and generate new, overhead-efficient methods for universal quantum computation. As a specific example, we propose fault-tolerant schemes based on surface codes concatenated with more general low-density parity check (LDPC) codes. The logical blocks framework enables a convenient mapping from an abstract description of the logical gate to a precise set of physical instructions for both circuit-based and fusion-based quantum computation (FBQC). Using this, we numerically simulate a surface-code-based universal gate set implemented with FBQC, and verify that their thresholds are consistent with the bulk memory threshold. We find that boundaries, defects, and twists can significantly impact the logical error rate scaling, with periodic boundary conditions potentially halving the resource requirements. Motivated by the favorable logical error rates for boundaryless computation, we introduce a novel computational scheme based on the teleportation of twists that may offer further resource reductions.

## Concatenated Code Design for Constrained DNA Data Storage with Asymmetric Errors

- **ID**: arxiv:2112.09417v1
- **Type**: preprint
- **Published**: 2021-12-17
- **Authors**: Yixin Wang, Li Deng, Md. Noor-A-Rahim +4
- **PDF**: https://arxiv.org/pdf/2112.09417v1
- **Abstract**: DNA Data storage has recently attracted much attention due to its durable preservation and extremely high information density (bits per gram) properties. In this work, we propose a hybrid coding strategy comprising of generalized constrained codes to tackle homopolymer (run-length) limit and a protograph based low-density parity-check (LDPC) code to correct asymmetric nucleotide level (i.e., A/T/C/G) substitution errors that may occur in the process of DNA sequencing. Two sequencing techniques namely, Nanopore sequencer and Illumina sequencer with their equivalent channel models and capacities are analyzed. A coding architecture is proposed to potentially eliminate the catastrophic errors caused by the error-propagation in the constrained decoding while enabling high coding potential. We also show the log likelihood ratio (LLR) calculation method for the belief propagation decoding with this coding architecture. The simulation results and the theoretical analysis show that the proposed coding scheme exhibits good bit-error rate (BER) performance and high coding potential ($\sim1.98$ bits per nucleotide).

## Explicit Abelian Lifts and Quantum LDPC Codes

- **ID**: arxiv:2112.01647v1
- **Type**: preprint
- **Published**: 2021-12-02
- **Authors**: Fernando Granha Jeronimo, Tushant Mittal, Ryan O'Donnell +2
- **PDF**: https://arxiv.org/pdf/2112.01647v1
- **Abstract**: For an abelian group $H$ acting on the set $[\ell]$, an $(H,\ell)$-lift of a graph $G_0$ is a graph obtained by replacing each vertex by $\ell$ copies, and each edge by a matching corresponding to the action of an element of $H$.   In this work, we show the following explicit constructions of expanders obtained via abelian lifts. For every (transitive) abelian group $H \leqslant \text{Sym}(\ell)$, constant degree $d \ge 3$ and $ε> 0$, we construct explicit $d$-regular expander graphs $G$ obtained from an $(H,\ell)$-lift of a (suitable) base $n$-vertex expander $G_0$ with the following parameters:   (i) $λ(G) \le 2\sqrt{d-1} + ε$, for any lift size $\ell \le 2^{n^δ}$ where $δ=δ(d,ε)$,   (ii) $λ(G) \le ε\cdot d$, for any lift size $\ell \le 2^{n^{δ_0}}$ for a fixed $δ_0 > 0$, when $d \ge d_0(ε)$, or   (iii) $λ(G) \le \widetilde{O}(\sqrt{d})$, for lift size ``exactly'' $\ell = 2^{Θ(n)}$.   As corollaries, we obtain explicit quantum lifted product codes of Panteleev and Kalachev of almost linear distance (and also in a wide range of parameters) and explicit classical quasi-cyclic LDPC codes with wide range of circulant sizes.   Items $(i)$ and $(ii)$ above are obtained by extending the techniques of Mohanty, O'Donnell and Paredes [STOC 2020] for $2$-lifts to much larger abelian lift sizes (as a byproduct simplifying their construction). This is done by providing a new encoding of special walks arising in the trace power method, carefully "compressing'" depth-first search traversals. Result $(iii)$ is via a simpler proof of Agarwal et al. [SIAM J. Discrete Math 2019] at the expense of polylog factors in the expansion.
