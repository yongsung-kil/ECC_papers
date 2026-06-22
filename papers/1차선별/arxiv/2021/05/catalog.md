# arXiv — 2021-05 (1차선별 통과)


## LDPC Codes with Soft Interference Cancellation for Uncoordinated Unsourced Multiple Access

- **Status**: ✅
- **Reason**: density evolution로 설계한 LDPC + soft interference cancellation BP; 코드설계(E)·디코더(C) 기법 이식 가능성, 애매하여 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2105.13985v1
- **Type**: preprint
- **Published**: 2021-05-28
- **Authors**: Asit Kumar Pradhan, Vamsi K. Amalladinne, Krishna R. Narayanan +1
- **PDF**: https://arxiv.org/pdf/2105.13985v1
- **Abstract**: This article presents a novel enhancement to the random spreading based coding scheme developed by Pradhan et al.\ for the unsourced multiple access channel. The original coding scheme features a polar outer code in conjunction with a successive cancellation list decoder (SCLD) and a hard-input soft-output MMSE estimator. In contrast, the proposed scheme employs a soft-input soft-output MMSE estimator for multi-user detection. This is accomplished by replacing the SCLD based polar code with an LDPC code amenable to belief propagation decoding. This novel framework is leveraged to successfully pass pertinent soft information between the MMSE estimator and the outer code. LDPC codes are carefully designed using density evolution techniques to match the iterative process. This enhanced architecture exhibits significant performance improvements and represents the state-of-the-art over a wide range of system parameters.

## Necessary and Sufficient Girth Conditions for Tanner Graphs of Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC Tanner 그래프 girth 6~12 필요충분조건 및 구성 알고리즘 — 바이너리 코드설계(E) girth/사이클 기법 직접 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:2105.03462v1
- **Type**: preprint
- **Published**: 2021-05-07
- **Authors**: Roxana Smarandache, David G. M. Mitchell
- **PDF**: https://arxiv.org/pdf/2105.03462v1
- **Abstract**: This paper revisits the connection between the girth of a protograph-based LDPC code given by a parity-check matrix and the properties of powers of the product between the matrix and its transpose in order to obtain the necessary and sufficient conditions for a code to have given girth between 6 and 12, and to show how these conditions can be incorporated into simple algorithms to construct codes of that girth. To this end, we highlight the role that certain submatrices that appear in these products have in the construction of codes of desired girth. In particular, we show that imposing girth conditions on a parity-check matrix is equivalent to imposing conditions on a square submatrix obtained from it and we show how this equivalence is particularly strong for a protograph based parity-check matrix of variable node degree 2, where the cycles in its Tanner graph correspond one-to-one to the cycles in the Tanner graph of a square submatrix obtained by adding the permutation matrices (or products of these) in the composition of the parity-check matrix. We end the paper with exemplary constructions of codes with various girths and computer simulations. Although, we mostly assume the case of fully connected protographs of variable node degree 2 and 3, the results can be used for any parity-check matrix/protograph-based Tanner graph.
