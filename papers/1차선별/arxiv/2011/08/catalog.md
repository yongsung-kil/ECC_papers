# arXiv — 2011-08 (1차선별 통과)


## Instantons causing iterative decoding to cycle

- **Status**: ✅
- **Reason**: 반복 디코딩 실패 instanton(error floor 원인) 분석, Tanner 바이너리 코드+Gaussian 채널—error floor/디코더 수렴실패 분석으로 코드설계(E)에 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1108.5547v2
- **Type**: preprint
- **Published**: 2011-08-29
- **Authors**: Misha Stepanov
- **PDF**: https://arxiv.org/pdf/1108.5547v2
- **Abstract**: It is speculated that the most probable channel noise realizations (instantons) that cause the iterative decoding of low-density parity-check codes to fail make the decoding not to converge. The Wiberg's formula is generalized for the case when the part of a computational tree that contributes to the output at its center is ambiguous. Two methods of finding the instantons for large number of iterations are presented and tested on Tanner's [155, 64, 20] code and Gaussian channel. The inherently dynamic instanton with effective distance of 11.475333 is found.

## A Design Methodology for Folded, Pipelined Architectures in VLSI Applications using Projective Space Lattices

- **Status**: ✅
- **Reason**: PG 기반 folded/pipelined VLSI 디코더 설계 방법론·툴(D), LDPC 디코더에 직접 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: arxiv:1108.3970v2
- **Type**: preprint
- **Published**: 2011-08-19
- **Authors**: Hrishikesh Sharma, Sachin Patkar
- **PDF**: https://arxiv.org/pdf/1108.3970v2
- **Abstract**: Semi-parallel, or folded, VLSI architectures are used whenever hardware resources need to be saved at design time. Most recent applications that are based on Projective Geometry (PG) based balanced bipartite graph also fall in this category. In this paper, we provide a high-level, top-down design methodology to design optimal semi-parallel architectures for applications, whose Data Flow Graph (DFG) is based on PG bipartite graph. Such applications have been found e.g. in error-control coding and matrix computations. Unlike many other folding schemes, the topology of connections between physical elements does not change in this methodology. Another advantage is the ease of implementation. To lessen the throughput loss due to folding, we also incorporate a multi-tier pipelining strategy in the design methodology. The design methodology has been verified by implementing a synthesis tool in C++, which has been verified as well. The tool is publicly available. Further, a complete decoder was manually protototyped before the synthesis tool design, to verify all the algorithms evolved in this paper, towards various steps of refinement. Another specific high-performance design of an LDPC decoder based on this methodology was worked out in past, and has been patented as well.

## Optimal Rate for Irregular LDPC Codes in Binary Erasure Channel

- **Status**: ✅
- **Reason**: BEC용 불규칙 LDPC 최적 차수분포 설계 방법(E, 바이너리), 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: arxiv:1108.1572v1
- **Type**: preprint
- **Published**: 2011-08-07
- **Authors**: H. Tavakoli, M. Ahmadian Attari, M. Reza Peyghami
- **PDF**: https://arxiv.org/pdf/1108.1572v1
- **Abstract**: In this paper, we introduce a new practical and general method for solving the main problem of designing the capacity approaching, optimal rate, irregular low-density parity-check (LDPC) code ensemble over binary erasure channel (BEC). Compared to some new researches, which are based on application of asymptotic analysis tools out of optimization process, the proposed method is much simpler, faster, accurate and practical. Because of not using any relaxation or any approximate solution like previous works, the found answer with this method is optimal. We can construct optimal variable node degree distribution for any given binary erasure rate, ε, and any check node degree distribution. The presented method is implemented and works well in practice. The time complexity of this method is of polynomial order. As a result, we obtain some degree distribution which their rates are close to the capacity.
