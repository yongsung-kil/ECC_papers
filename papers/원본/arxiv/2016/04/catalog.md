# arXiv — 2016-04


## Check-hybrid GLDPC Codes: Systematic Elimination of Trapping Sets and Guaranteed Error Correction Capability

- **Status**: ✅
- **Reason**: check-hybrid GLDPC로 trapping set 체계적 제거+보장 에러정정 — error floor/코드설계(E)+PBF·Gallager B 디코더
- **ID**: arxiv:1604.05256v1
- **Type**: preprint
- **Published**: 2016-04-18
- **Authors**: Vida Ravanmehr, Mehrdad Khatami, David Declercq +1
- **PDF**: https://arxiv.org/pdf/1604.05256v1
- **Abstract**: In this paper, we propose a new approach to construct a class of check-hybrid generalized low-density parity-check (CH-GLDPC) codes which are free of small trapping sets. The approach is based on converting some selected check nodes involving a trapping set into super checks corresponding to a 2-error correcting component code. Specifically, we follow two main purposes to construct the check-hybrid codes; first, based on the knowledge of the trapping sets of the global LDPC code, single parity checks are replaced by super checks to disable the trapping sets. We show that by converting specified single check nodes, denoted as critical checks, to super checks in a trapping set, the parallel bit flipping (PBF) decoder corrects the errors on a trapping set and hence eliminates the trapping set. The second purpose is to minimize the rate loss caused by replacing the super checks through finding the minimum number of such critical checks. We also present an algorithm to find critical checks in a trapping set of column-weight 3 LDPC code and then provide upper bounds on the minimum number of such critical checks such that the decoder corrects all error patterns on elementary trapping sets. Moreover, we provide a fixed set for a class of constructed check-hybrid codes. The guaranteed error correction capability of the CH-GLDPC codes is also studied. We show that a CH-GLDPC code in which each variable node is connected to 2 super checks corresponding to a 2-error correcting component code corrects up to 5 errors. The results are also extended to column-weight 4 LDPC codes. Finally, we investigate the eliminating of trapping sets of a column-weight 3 LDPC code using the Gallager B decoding algorithm and generalize the results obtained for the PBF for the Gallager B decoding algorithm.

## Finite-length scaling based on belief propagation for spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC BP 기반 유한길이 scaling 분석 — 바이너리 코드설계(E)
- **ID**: arxiv:1604.05111v1
- **Type**: preprint
- **Published**: 2016-04-18
- **Authors**: Markus Stinner, Luca Barletta, Pablo M. Olmos
- **PDF**: https://arxiv.org/pdf/1604.05111v1
- **Abstract**: The equivalence of peeling decoding (PD) and Belief Propagation (BP) for low-density parity-check (LDPC) codes over the binary erasure channel is analyzed. Modifying the scheduling for PD, it is shown that exactly the same variable nodes (VNs) are resolved in every iteration than with BP. The decrease of erased VNs during the decoding process is analyzed instead of resolvable equations. This quantity can also be derived with density evolution, resulting in a drastic decrease in complexity. Finally, a scaling law using this quantity is established for spatially coupled LDPC codes.

## Low-density locality-sensitive hashing boosts metagenomic binning

- **Status**: ❌
- **Reason**: 메타게놈 binning용 Gallager LSH — ECC 아님, 떼어낼 디코더/HW 없음
- **ID**: arxiv:1604.02699v1
- **Type**: preprint
- **Published**: 2016-04-10
- **Authors**: Yunan Luo, Jianyang Zeng, Bonnie Berger +1
- **PDF**: https://arxiv.org/pdf/1604.02699v1
- **Abstract**: Metagenomic binning is an essential task in analyzing metagenomic sequence datasets. To analyze structure or function of microbial communities from environmental samples, metagenomic sequence fragments are assigned to their taxonomic origins. Although sequence alignment algorithms can readily be used and usually provide high-resolution alignments and accurate binning results, the computational cost of such alignment-based methods becomes prohibitive as metagenomic datasets continue to grow. Alternative compositional-based methods, which exploit sequence composition by profiling local short k-mers in fragments, are often faster but less accurate than alignment-based methods. Inspired by the success of linear error correcting codes in noisy channel communication, we introduce Opal, a fast and accurate novel compositional-based binning method. It incorporates ideas from Gallager's low-density parity-check code to design a family of compact and discriminative locality-sensitive hashing functions that encode long-range compositional dependencies in long fragments. By incorporating the Gallager LSH functions as features in a simple linear SVM, Opal provides fast, accurate and robust binning for datasets consisting of a large number of species, even with mutations and sequencing errors. Opal not only performs up to two orders of magnitude faster than BWA, an alignment-based binning method, but also achieves improved binning accuracy and robustness to sequencing errors. Opal also outperforms models built on traditional k-mer profiles in terms of robustness and accuracy. Finally, we demonstrate that we can effectively use Opal in the "coarse search" stage of a compressive genomics pipeline to identify a much smaller candidate set of taxonomic origins for a subsequent alignment-based method to analyze, thus providing metagenomic binning with high scalability, high accuracy and high resolution.

## Probabilistic bounds on the trapping redundancy of linear codes

- **Status**: ❌
- **Reason**: trapping redundancy 확률적 bound — 순수 이론, 디코더/HW/구성으로 안 이어짐
- **ID**: arxiv:1604.00761v1
- **Type**: preprint
- **Published**: 2016-04-04
- **Authors**: Yu Tsunoda, Yuichiro Fujiwara
- **PDF**: https://arxiv.org/pdf/1604.00761v1
- **Abstract**: The trapping redundancy of a linear code is the number of rows of a smallest parity-check matrix such that no submatrix forms an $(a,b)$-trapping set. This concept was first introduced in the context of low-density parity-check (LDPC) codes in an attempt to estimate the number of redundant rows in a parity-check matrix suitable for iterative decoding. Essentially the same concepts appear in other contexts as well such as robust syndrome extraction for quantum error correction. Among the known upper bounds on the trapping redundancy, the strongest one was proposed by employing a powerful tool in probabilistic combinatorics, called the Lovász Local Lemma. Unfortunately, the proposed proof invoked this tool in a situation where an assumption made in the lemma does not necessarily hold. Hence, although we do not doubt that nonetheless the proposed bound actually holds, for it to be a mathematical theorem, a more rigorous proof is desired. Another disadvantage of the proposed bound is that it is only applicable to $(a,b)$-trapping sets with rather small $a$. Here, we give a more general and sharper upper bound on trapping redundancy by making mathematically more rigorous use of probabilistic combinatorics without relying on the lemma. Our bound is applicable to all potentially avoidable $(a,b)$-trapping sets with $a$ smaller than the minimum distance of a given linear code, while being generally much sharper than the bound through the Lovász Local Lemma. In fact, our upper bound is sharp enough to exactly determine the trapping redundancy for many cases, thereby providing precise knowledge in the form of a more general bound with mathematical rigor.
