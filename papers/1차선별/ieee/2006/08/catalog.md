# IEEE Xplore — 2006-08 (1차선별 통과)


## An 860-Mb/s (8158,7136) Low-Density Parity-Check Encoder

- **Status**: ✅
- **Reason**: (8158,7136) LDPC 인코더 CMOS HW 구현, generator 다항식 재구성·partial product로 면적 효율화 — 이식 가능 HW(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:1661745
- **Type**: journal
- **Published**: Aug. 2006
- **Authors**: L.H. Miles, J.W. Gambles, G.K. Maki +2
- **PDF**: https://ieeexplore.ieee.org/document/1661745
- **Abstract**: Low-density parity-check codes achieve coding performance which approaches the Shannon limit. An (8158,7136) encoder was implemented in a five-metal, 0.25-mum CMOS process. Use of generator polynomial reconstruction, partial product multiplication and functional sharing in the parity register results in a highly efficient design. Only 1492 flip-flops along with a programmable 21-bit look-ahead scheme are used to achieve an 860-Mb/s data throughput for this rate 7/8 LDPC code. A comparable two-stage encoder requires 8176 flip-flops

## Nonlinear programming approaches to decoding low-density parity-check codes

- **Status**: ✅
- **Reason**: LDPC 비선형계획 디코딩(box-constrained QP), 선형시간 병렬/직렬 디코더 제시 — 이식 가능 디코더(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1665013
- **Type**: journal
- **Published**: Aug. 2006
- **Authors**: Kai Yang, J. Feldman, Xiaodong Wang
- **PDF**: https://ieeexplore.ieee.org/document/1665013
- **Abstract**: We consider the decoding problem for low-density parity-check codes, and apply nonlinear programming methods. This extends previous work using linear programming (LP) to decode linear block codes. First, a multistage LP decoder based on the branch-and-bound method is proposed. This decoder makes use of the maximum-likelihood-certificate property of the LP decoder to refine the results when an error is reported. Second, we transform the original LP decoding formulation into a box-constrained quadratic programming form. Efficient linear-time parallel and serial decoding algorithms are proposed and their convergence properties are investigated. Extensive simulation studies are performed to assess the performance of the proposed decoders. It is seen that the proposed multistage LP decoder outperforms the conventional sum-product (SP) decoder considerably for low-density parity-check (LDPC) codes with short to medium block length. The proposed box-constrained quadratic programming decoder has less complexity than the SP decoder and yields much better performance for LDPC codes with regular structure

## Analysis of low-density parity-check codes based on EXIT functions

- **Status**: ✅
- **Reason**: EXIT/density evolution(GA) 기반 BP 디코딩 임계값 예측 개선 — 바이너리 LDPC 코드설계/분석 기법(E), 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1673673
- **Type**: journal
- **Published**: Aug. 2006
- **Authors**: E. Sharon, A. Ashikhmin, S. Litsyn
- **PDF**: https://ieeexplore.ieee.org/document/1673673
- **Abstract**: We exploit extrinsic information transfer functions of single parity-check and repetition codes over the binary input additive white Gaussian noise (biAWGN) channel, derived by the authors, for asymptotic performance analysis of belief propagation decoding of low-density parity-check codes. The approach is based on a Gaussian approximation (GA) of the density evolution algorithm using the mutual information measure. We show that this method allows more accurate prediction of the decoding threshold in the biAWGN channel than the earlier known GA methods

## Shortened Array Codes of Large Girth

- **Status**: ✅
- **Reason**: array code 단축으로 girth 증대, circulant permutation 기반 QC-LDPC 사이클 제거 — 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1661848
- **Type**: journal
- **Published**: Aug. 2006
- **Authors**: O. Milenkovic, N. Kashyap, D. Leyba
- **PDF**: https://ieeexplore.ieee.org/document/1661848
- **Abstract**: One approach to designing structured low-density parity-check (LDPC) codes with large girth is to shorten codes with small girth in such a manner that the deleted columns of the parity-check matrix contain all the variables involved in short cycles. This approach is especially effective if the parity-check matrix of a code is a matrix composed of blocks of circulant permutation matrices, as is the case for the class of codes known as array codes. We show how to shorten array codes by deleting certain columns of their parity-check matrices so as to increase their girth. The shortening approach is based on the observation that for array codes, and in fact for a slightly more general class of LDPC codes, the cycles in the corresponding Tanner graph are governed by certain homogeneous linear equations with integer coefficients. Consequently, we can selectively eliminate cycles from an array code by only retaining those columns from the parity-check matrix of the original code that are indexed by integer sequences that do not contain solutions to the equations governing those cycles. We provide Ramsey-theoretic estimates for the maximum number of columns that can be retained from the original parity-check matrix with the property that the sequence of their indices avoid solutions to various types of cycle-governing equations. This translates to estimates of the rate penalty incurred in shortening a code to eliminate cycles. Simulation results show that for the codes considered, shortening them to increase the girth can lead to significant gains in signal-to-noise ratio (SNR) in the case of communication over an additive white Gaussian noise (AWGN) channel.

## Performance evaluation of LDPC codes in bliss scheme-based storage systems using density evolution

- **Status**: ✅
- **Reason**: 스토리지 시스템 LDPC scaled min-sum 디코딩의 최적 scaling factor 결정용 density evolution — 스토리지 ECC(B)+디코더 튜닝(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:1706484
- **Type**: journal
- **Published**: Aug. 2006
- **Authors**: Haibin Zhang, A.P. Hekstra, Bin Yin
- **PDF**: https://ieeexplore.ieee.org/document/1706484
- **Abstract**: Density evolution algorithms for scaled min-sum decoding of both regular and irregular low-density parity-check (LDPC) codes in Bliss scheme-based storage systems are presented, to evaluate the performance of LDPC codes in terms of noise threshold. Firstly, with the assumption of fixed error propagation factor and independently and identically distributed (i.i.d.) messages, density evolution algorithms of regular LDPC codes are derived to compare performance among LDPC codes with the same code rate but different bit/check node degrees and determine the optimum scaling factor of scaled min-sum decoding. Secondly, with the looser assumption of fixed error propagation and independently distributed messages, density evolution algorithms of irregular LDPC codes are derived for performance evaluation of LDPC codes with arbitrary degree distributions. Comparisons with simulations show density evolution is a proper performance evaluation method for LDPC codes in Bliss scheme-based storage systems

## A High Speed Flexible Encoder for Low-Density Parity-Check Codes

- **Status**: ✅
- **Reason**: 고속 LDPC 인코더 FPGA 구현(D 이식 가능 HW), 처리율 향상 설계 제시
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4267145
- **Type**: conference
- **Published**: 6-9 Aug. 2
- **Authors**: Sunitha Kopparthi, Don M. Gruenbacher
- **PDF**: https://ieeexplore.ieee.org/document/4267145
- **Abstract**: Encoder implementations of low-density parity- check codes are typically optimized for area due to their high complexity. Such designs usually have relatively low data throughput. Two new encoder designs are presented here that achieve much higher data rates while requiring more area for the implementation. One of these design achieves encoding rates in excess of 400 Mbps. All of the designs presented can fit on FPGAs currently available. The methodology for both designs and performance results are presented.

## Design, Simulation and Hardware Implementation of a Digital Television System: LDPC channel coding

- **Status**: ✅
- **Reason**: DTV용 LDPC 코드 설계 전략 및 HW 구현 제시; 코드설계+디코더 HW 아키텍처 NAND에 이식 가능(D/E), 애매하므로 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4100552
- **Type**: conference
- **Published**: 28-31 Aug.
- **Authors**: Tarciano F. Pegoraro, Fabio A. L. Gomes, Renato R. Lopes +5
- **PDF**: https://ieeexplore.ieee.org/document/4100552
- **Abstract**: In this paper, we describe a hardware implementation of a low-density parity-check (LDPC) code for the MI-SBTVD project, which aims at the development of an advanced digital television (DTV) system for the SBTVD program. We begin the paper by describing the concept of LDPC codes and the design strategies we have used. We also provide some simulation results that show that the proposed code greatly outperforms codes used by other DTV standards. Finally, we provide details of the hardware implementation of the code

## A High Speed, Low Memory FPGA Based LDPC Decoder Architecture for Quasi-Cyclic LDPC Codes

- **Status**: ✅
- **Reason**: QC-LDPC용 고속·저메모리 FPGA 디코더 아키텍처 신규 제안 — 카테고리 D(HW) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4101090
- **Type**: conference
- **Published**: 28-30 Aug.
- **Authors**: Paul Saunders, Anthony D. Fagan
- **PDF**: https://ieeexplore.ieee.org/document/4101090
- **Abstract**: We propose a novel, high speed, low memory fully programable FPGA decoder architecture to decode quasi-cyclic LDPC codes. By performing optimizations at the code construction, algorithmic and architecture levels we are able to achieve significant throughput and memory storage advantages over current FPGA decoder implementations. Our decoder employs the modified turbo decoding algorithm, to achieve a decoding throughput of 223 Mbps for a frame length of 3200 bits whilst only consuming 71 Kb of memory using a Xilinx Virtex-4 architecture.
