# arXiv — 2016-04 (1차선별 통과)


## Check-hybrid GLDPC Codes: Systematic Elimination of Trapping Sets and Guaranteed Error Correction Capability

- **Status**: ✅
- **Reason**: check-hybrid GLDPC로 trapping set 체계적 제거+보장 에러정정 — error floor/코드설계(E)+PBF·Gallager B 디코더
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1604.05256v1
- **Type**: preprint
- **Published**: 2016-04-18
- **Authors**: Vida Ravanmehr, Mehrdad Khatami, David Declercq +1
- **PDF**: https://arxiv.org/pdf/1604.05256v1
- **Abstract**: In this paper, we propose a new approach to construct a class of check-hybrid generalized low-density parity-check (CH-GLDPC) codes which are free of small trapping sets. The approach is based on converting some selected check nodes involving a trapping set into super checks corresponding to a 2-error correcting component code. Specifically, we follow two main purposes to construct the check-hybrid codes; first, based on the knowledge of the trapping sets of the global LDPC code, single parity checks are replaced by super checks to disable the trapping sets. We show that by converting specified single check nodes, denoted as critical checks, to super checks in a trapping set, the parallel bit flipping (PBF) decoder corrects the errors on a trapping set and hence eliminates the trapping set. The second purpose is to minimize the rate loss caused by replacing the super checks through finding the minimum number of such critical checks. We also present an algorithm to find critical checks in a trapping set of column-weight 3 LDPC code and then provide upper bounds on the minimum number of such critical checks such that the decoder corrects all error patterns on elementary trapping sets. Moreover, we provide a fixed set for a class of constructed check-hybrid codes. The guaranteed error correction capability of the CH-GLDPC codes is also studied. We show that a CH-GLDPC code in which each variable node is connected to 2 super checks corresponding to a 2-error correcting component code corrects up to 5 errors. The results are also extended to column-weight 4 LDPC codes. Finally, we investigate the eliminating of trapping sets of a column-weight 3 LDPC code using the Gallager B decoding algorithm and generalize the results obtained for the PBF for the Gallager B decoding algorithm.

## Finite-length scaling based on belief propagation for spatially coupled LDPC codes

- **Status**: ✅
- **Reason**: SC-LDPC BP 기반 유한길이 scaling 분석 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1604.05111v1
- **Type**: preprint
- **Published**: 2016-04-18
- **Authors**: Markus Stinner, Luca Barletta, Pablo M. Olmos
- **PDF**: https://arxiv.org/pdf/1604.05111v1
- **Abstract**: The equivalence of peeling decoding (PD) and Belief Propagation (BP) for low-density parity-check (LDPC) codes over the binary erasure channel is analyzed. Modifying the scheduling for PD, it is shown that exactly the same variable nodes (VNs) are resolved in every iteration than with BP. The decrease of erased VNs during the decoding process is analyzed instead of resolvable equations. This quantity can also be derived with density evolution, resulting in a drastic decrease in complexity. Finally, a scaling law using this quantity is established for spatially coupled LDPC codes.
