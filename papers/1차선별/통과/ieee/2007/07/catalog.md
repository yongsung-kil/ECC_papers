# IEEE Xplore — 2007-07 (1차선별 통과)


## Construction of Quasi-Cyclic LDPC Codes for AWGN and Binary Erasure Channels: A Finite Field Approach

- **Status**: ✅
- **Reason**: 유한체 기반 QC-LDPC 구성법, 낮은 error floor 바이너리 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4252336
- **Type**: journal
- **Published**: July 2007
- **Authors**: Lan Lan, Lingqi Zeng, Ying Y. Tai +3
- **PDF**: https://ieeexplore.ieee.org/document/4252336
- **Abstract**: In the late 1950s and early 1960s, finite fields were successfully used to construct linear block codes, especially cyclic codes, with large minimum distances for hard-decision algebraic decoding, such as Bose-Chaudhuri-Hocquenghem (BCH) and Reed-Solomon (RS) codes. This paper shows that finite fields can also be successfully used to construct algebraic low-density parity-check (LDPC) codes for iterative soft-decision decoding. Methods of construction are presented. LDPC codes constructed by these methods are quasi-cyclic (QC) and they perform very well over the additive white Gaussian noise (AWGN), binary random, and burst erasure channels with iterative decoding in terms of bit-error probability, block-error probability, error-floor, and rate of decoding convergence, collectively. Particularly, they have low error floors. Since the codes are QC, they can be encoded using simple shift registers with linear complexity.

## Augmented Belief Propagation Decoding of Low-Density Parity Check Codes

- **Status**: ✅
- **Reason**: augmented BP 디코더로 pseudocodeword 제거·error floor 저감하는 short LDPC 이식가능 디코더 기법(C)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4273701
- **Type**: journal
- **Published**: July 2007
- **Authors**: Nedeljko Varnica, Marc P. C. Fossorier, Aleksandar Kavcic
- **PDF**: https://ieeexplore.ieee.org/document/4273701
- **Abstract**: We propose an augmented belief propagation (BP) decoder for low-density parity check (LDPC) codes which can be utilized on memoryless or intersymbol interference channels. The proposed method is a heuristic algorithm that eliminates a large number of pseudocodewords that can cause nonconvergence in the BP decoder. The augmented decoder is a multistage iterative decoder, where, at each stage, the original channel messages on select symbol nodes are replaced by saturated messages. The key element of the proposed method is the symbol selection process, which is based on the appropriately defined subgraphs of the code graph and/or the reliability of the information received from the channel. We demonstrate by examples that this decoder can be implemented to achieve substantial gains (compared to the standard locally-operating BP decoder) for short LDPC codes decoded on both memoryless and intersymbol interference Gaussian channels. Using the Margulis code example, we also show that the augmented decoder reduces the error floors. Finally, we discuss types of BP decoding errors and relate them to the augmented BP decoder.

## LDPC Code Construction with Low Error Floor Based on the IPEG Algorithm

- **Status**: ✅
- **Reason**: IPEG 알고리즘 수정으로 stopping set 축소·error floor 저감하는 신규 바이너리 LDPC 코드설계(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4273776
- **Type**: journal
- **Published**: July 2007
- **Authors**: Sung-ha Kim, Joon-sung Kim, Dae-son Kim +1
- **PDF**: https://ieeexplore.ieee.org/document/4273776
- **Abstract**: We propose a modification on the improved progressive-edge-growth(IPEG) algorithm. Proposed modification increases the connectivity of variable nodes using extrinsic message degree of variable nodes, which results in reducing the small stopping sets. Through computer simulation, we confirm that the codes constructed by the proposed algorithm have lower error floor than those constructed by the original IPEG algorithm.

## CASCADE: A Standard Supercell Design Methodology With Congestion-Driven Placement for Three-Dimensional Interconnect-Heavy Very Large-Scale Integrated Circuits

- **Status**: ✅
- **Reason**: 4M게이트 LDPC 디코더 3D VLSI 구현/설계 방법론, 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4237248
- **Type**: journal
- **Published**: July 2007
- **Authors**: Lili Zhou, Cherry Wakayama, C.-J. Richard Shi
- **PDF**: https://ieeexplore.ieee.org/document/4237248
- **Abstract**: In this paper, CASCADE, a standard supercell-based design methodology, its supporting automated design flow, and associated design tools, are presented for 3D implementations of a class of interconnect-heavy application-specific very large-scale integrated circuits. In CASCADE, a system is first partitioned and synthesized using standard 2D design tools to a set of supercells with the same height and varying widths. With this, the 3D design is reduced to 3D supercell placement and 3D-via assignment. A congestion-driven simulated-annealing method is used to find a 3D placement of supercells to minimize the total wire length, the longest wire length, and the number of 3D vias and routing density. To efficiently estimate the routing density of a 3D grid space within the optimization loop, a simple probabilistic congestion model with an incremental congestion computation has been developed. Once the supercell placement is fixed, the problem of assigning 3D vias to accomplish minimal 2D routing densities and uniform 3D-via distribution is solved by an efficient min-cost-max-flow method. The proposed methods have been implemented and tested on a set of ISPD98 circuit benchmarks. Experimental results have shown that the proposed congestion-driven 3D supercell placement and flow-based 3D-via-assignment tools have yielded satisfactory placement with small-area, low-congestion, short-wire-length, few, and uniformly distributed 3D vias. Furthermore, an excellent correlation between routing-density estimation by our model and the actual routing performed by a commercial router has been observed. We have applied the proposed 3D design methodology, tools, and flows to tape out an over 4-million-gate low-density parity-check decoder in a three-tier 0.18- fully depleted silicon-on-insulator 3D CMOS process manufactured by MIT Lincoln Laboratory. The postlayout simulation of this DRC-clean layout design showed an about ten times improvement on the power-delay-area product compared to a 2D implementation in the same process.

## A High-Throughput Programmable Decoder for LDPC Convolutional Codes

- **Status**: ✅
- **Reason**: LDPC convolutional 부호용 고처리율 프로그래머블 SIMD ASIC 디코더 — 이식 가능 HW 아키텍처(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:4429987
- **Type**: conference
- **Published**: 9-11 July 
- **Authors**: Marcel Bimberg, Marcos B. S. Tavares, Emil Matus +1
- **PDF**: https://ieeexplore.ieee.org/document/4429987
- **Abstract**: In this paper, we present and analyze a novel decoder architecture for LDPC convolutional codes (LDPCCCs). The proposed architecture enables high throughput and can be programmed to decode different codes and blocklengths, which might be necessary to cope with the requirements of future communication systems. To achieve high throughput, the SIMD paradigm is applied on the regular graph structure typical to LDPCCCs. We also present the main components of the proposed architecture and analyze its programmability. Finally, synthesis results for a prototype ASIC show that the architecture is capable of achieving decoding throughputs of several hundreds MBits/s with attractive complexity and power consumption.

## Performance Optimization of Soft-decision FEC Receivers

- **Status**: ✅
- **Reason**: 3-bit soft-decision FEC 임계값 추적/최적화 — LLR 양자화 임계값 제어 기법 이식 가능(A/C), 애매하나 살림
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4288317
- **Type**: conference
- **Published**: 23-25 July
- **Authors**: Kiyoshi Onohara, Takashi Mizuochi
- **PDF**: https://ieeexplore.ieee.org/document/4288317
- **Abstract**: We present threshold tracking of a soft-decision based forward error correction system as an application of digital signal processing for optical communications. The 3-bit soft-decision thresholds are closely controlled to obtain the best possible error-correction performance.

## Multi-rate LDPC decoder implementation for china digital television terrestrial broadcasting standard

- **Status**: ✅
- **Reason**: multi-rate QC-LDPC 디코더 semi-parallel HW 구현, 저장/처리유닛 멀티플렉스로 자원효율 개선(D)
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6247588
- **Type**: conference
- **Published**: 11-13 July
- **Authors**: Dimin Niu, Kewu Peng, Jian Song +2
- **PDF**: https://ieeexplore.ieee.org/document/6247588
- **Abstract**: The China national standard of digital television terrestrial broadcasting employs Low-Density Parity-Check (LDPC) codes of three different rates as the inner Forward Error Correction (FEC) Codes. In this paper, according to the structure of the quasi-cyclic LDPC (QC-LDPC) code, an implementation of multi-rate LDPC decoder is proposed using semi-parallel structure, achieving the appropriate balance between decoding throughput and the utilization of hardware resource. Meanwhile, a novel multiplex model of storage space and processing units is proposed to increase the resource efficiency of this decoder, which is much better than that of simple combination of three single-rate decoders. Simulation results demonstrate that this multi-rate decoder's performance under AWGN channel is the same as that of single rate decoders, while it has higher resource utilization efficiency. Therefore it could help reduce the chip size of the decoder greatly. In addition, the multi-rate strategy can also be applied to other QC-LDPC codes.

## Design of LDPC coded recursive MSK systems

- **Status**: ✅
- **Reason**: MSK 응용이나 error correlation 줄이는 새 LDPC 코드 설계 규칙(E) 제시, 코드설계 기법 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:6247577
- **Type**: conference
- **Published**: 11-13 July
- **Authors**: Jianzhong Huang, Shuling Che, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/6247577
- **Abstract**: This paper investigates a low-density parity-check (LDPC) coded recursive minimum shift keying (MSK) scheme when the receiver employs iterative decoding and demodulation. Since the recursive continuous phase encoder (RCPE) of MSK can be expressed by a bipartite graph, the overall system can be viewed as a concatenation of two Tanner graphs. By analyzing the error correlation in the MSK demodulator and the overall loop in the joint Tanner graph, we show that the error correlation has a great impact on the performance of the iterative system when the LDPC codes are not well designed and interleavers are not employed. We develop a new design rule of LDPC codes to reduce the impact of the error correlation on the system performance while without interleavers. Simulation results show that the proposed design rule can reduce the impact of the error correlation in a simple and effective way.

## Efficient encoding of low-density parity-check codes in chinese digital terrestrial television broadcasting standard

- **Status**: ✅
- **Reason**: QC-LDPC 고속 인코딩 회로(직렬/병렬/부분병렬) HW 구현 기법(D) 이식 가능
- **알고리즘 기여**: 🔧 하드웨어 수정만
- **ID**: ieee:6247586
- **Type**: conference
- **Published**: 11-13 July
- **Authors**: Jingli Lin, Longjiang Jing, Weile Zhu +1
- **PDF**: https://ieeexplore.ieee.org/document/6247586
- **Abstract**: Since Quasi-Cyclic LDPC (QC-LDPC) codes have many advantages for fast encoding, they are adopted in channel coding of the Chinese Digital Terrestrial Television Broadcasting (DTTB) Standard. The construction of QC-LDPC codes in Chinese DTTB standard, which is based on the structure of RS codes with two information symbols, is described. Also, three fast encoding circuits are presented, which encode in serial, parallel and partial parallel, respectively. They have speeds and complexities that differ with each other. According to the requirements of the system, one of them can be chosen carefully.

## On the Effects of Pseudo-Codewords on Independent Rayleigh Flat-Fading Channels

- **Status**: ✅
- **Reason**: LP 디코딩의 pseudo-codeword/stopping set 분석으로 바이너리 LDPC 디코더 성능에 이식 가능한 이론 기법(C). 채널이 fading이나 Tanner graph stopping set 관점은 일반적.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4318057
- **Type**: conference
- **Published**: 1-6 July 2
- **Authors**: Eirik Rosnes
- **PDF**: https://ieeexplore.ieee.org/document/4318057
- **Abstract**: In this work, we consider the pairwise error probability (PEP) of a linear programming (LP) decoder for a general binary linear code as formulated by Feldman et al. (IEEE Trans. Inform. Theory, Mar. 2005) on an independent (or memoryless) Rayleigh flat-fading channel with coherent detection and perfect channel state information (CSI) at the receiver. Let H be a parity-check matrix of a binary linear code and consider LP decoding based on H. The output of the LP decoder is always a pseudo-codeword. We will show that the PEP of decoding to a pseudo-codeword omega when the all-zero codeword is transmitted on an independent Rayleigh flat-fading channel with coherent detection and perfect CSI at the receiver, behaves asymptotically as K(omega)ldr(Es/NO)-chi(omega), where chi(omega) is the support set of omega, i.e., the set of non-zero coordinates, Es/NO is the average signal-to-noise ratio (SNR), and K(omega) is a constant independent of the SNR. Thus, the asymptotic decay rate of the error probability with the average SNR is determined by the size of the smallest non-empty stopping set in the Tanner graph of H.

## Construction of Girth 8 LDPC Codes based on Multidimensional Finite Lattices

- **Status**: ✅
- **Reason**: 유한 격자 기반 girth 8 LDPC 신규 구성법(E). 바이너리 LDPC 코드 설계 기법으로 이식 가능.
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:4381604
- **Type**: conference
- **Published**: 1-4 July 2
- **Authors**: John Craddock, Mark Flanagan, Stephen J. Redmond +1
- **PDF**: https://ieeexplore.ieee.org/document/4381604
- **Abstract**: This paper presents a novel method for constructing low density parity check (LDPC) codes with a girth of up to 8. These codes are based on the structural properties of finite lattices. Results are presented which show that these codes perform well over AWGN channels with iterative decoding.
