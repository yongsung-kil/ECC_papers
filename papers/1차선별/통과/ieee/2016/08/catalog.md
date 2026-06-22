# IEEE Xplore — 2016-08 (1차선별 통과)


## An Area Time-Efficient Structure to Find the Approximate First Two Minima for Min-Sum-Based LDPC Decoders

- **Status**: ✅
- **Reason**: min-sum LDPC 디코더용 first-two-minima 근사 HW 구조 — 바이너리 디코더 HW(C/D) 이식 가능
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7410047
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Xi Zhu, Guanghui He
- **PDF**: https://ieeexplore.ieee.org/document/7410047
- **Abstract**: Aiming at reducing the hardware complexity of low-density parity-check (LDPC) decoders based on min-sum algorithms, this brief presents a general structure to find the minimum value and an approximate second minimum value. The proposed structure is proved to obtain the exact second minimum value with high probability in theory, and simulation results demonstrate that only a negligible degradation of error performance is introduced when adopting the proposed structure in LDPC decoders. Furthermore, mixed radix architecture is investigated to improve the area-time efficiency. Implemented in a SMIC 65-nm CMOS technology, the proposed architecture significantly improves the overall area-time efficiency compared with state-of-the-art works.

## Exploiting Intracell Bit-Error Characteristics to Improve Min-Sum LDPC Decoding for MLC NAND Flash-Based Storage in Mobile Device

- **Status**: ✅
- **Reason**: MLC NAND 인트라셀 비트에러 특성 활용 min-sum LDPC 디코딩 개선 — NAND 직접(A)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7445886
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Hongbin Sun, Wenzhe Zhao, Minjie Lv +3
- **PDF**: https://ieeexplore.ieee.org/document/7445886
- **Abstract**: A multilevel per cell (MLC) technique significantly improves the storage density, but also poses serious data integrity challenge for NAND flash memory. This consequently makes the low-density parity-check (LDPC) code and the soft-decision memory sensing become indispensable in the next-generation flash-based solid-state storage devices. However, the use of LDPC codes inevitably increases memory read latency and, hence, degrades speed performance. Motivated by the observation of intracell unbalanced bit error probability and data dependence in the MLC NAND flash memory, this paper proposes two techniques, i.e., intracell data placement interleaving and intracell data dependence aware LDPC decoding, to efficiently improve the LDPC decoding throughput and energy efficiency for the MLC NAND flash-based storage in a mobile device. Experimental results show that, by exploiting the intracell bit-error characteristics, the proposed techniques together can improve the LDPC decoding throughput by up to 84.6% and reduce the energy consumption by up to 33.2% while only incurring less than 0.2% silicon area overhead.

## Design of LDPC Codes Based on Multipath EMD Strategies for Progressive Edge Growth

- **Status**: ✅
- **Reason**: 신규 multipath EMD 후보선택 메트릭으로 PEG 그래프 구성·error floor 개선(QC-LDPC 포함)→코드설계 기법 이식 가능(E)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7489038
- **Type**: journal
- **Published**: Aug. 2016
- **Authors**: Cornelius T. Healy, Rodrigo C. de Lamare
- **PDF**: https://ieeexplore.ieee.org/document/7489038
- **Abstract**: Low-density parity-check (LDPC) codes are capable of achieving excellent performance and provide a useful alternative for the high-performance applications. However, at medium to high signal-to-noise ratios, an observable error floor arises from the loss of independence of messages passed under iterative graph-based decoding. In this paper, the error floor performance of the short block length codes is improved by the use of a novel candidate selection metric in code graph construction. The proposed multipath extrinsic message degree (EMD) approach avoids harmful structures in the graph by evaluating certain properties of the cycles introduced in each edge placement. We present multipath EMD-based designs for several structured LDPC codes, including quasi-cyclic and the irregular repeat accumulate codes. In addition, an extended class of the diversity-achieving codes on the challenging block fading channel is proposed and considered with the multipath EMD design. This combined approach is demonstrated to provide the gains in decoder convergence and error rate performance. A simulation study evaluates the performance of the proposed and existing state-of-the-art methods.

## expanCodes: Tailored LDPC Codes for Big Data Storage

- **Status**: ✅
- **Reason**: B 스토리지 ECC - 확장가능 크기 LDPC 구성(expanCodes) 신규 코드설계, 빅데이터 스토리지용 바이너리 LDPC
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7588911
- **Type**: conference
- **Published**: 8-12 Aug. 
- **Authors**: Yongmei Wei, Fengmin Chen
- **PDF**: https://ieeexplore.ieee.org/document/7588911
- **Abstract**: Big data storage demands larger cluster. The increasing size of the cluster may lead to failures of larger number of nodes. To provide reliable big data storage, replications are not cost-effective and does not provide a robust solution to prevent data loss. Traditional erasure codes applied in the RAID system such as Reed-Solomon (R-S) based solutions have limitations in providing high reliability. This is because higher reliability requires erasure codes with larger size. The computational cost of the R-S codes increase quadratically with the number of failures the R-S codes can tolerate for the same redundancy rate. It has been shown that Low Density Parity Check (LDPC) codes have lower computational cost and repair network traffic compared with R-S based solutions. Unfortunately, there does not exist a construction method for LDPC codes with larger size to control the computational cost and repair traffic. In this paper, a novel method is proposed to construct a family of LDPC codes - expanCodes with expandable sizes. The proposed expanCodes allows the encoding and decoding complexity remain unchanged with the increase of the size of the LDPC codes. As a result, increased reliability can be achieved without additional computation and repair traffic. The proposed expanCodes is integrated with the Hadoop system. Simulations show that more than 29% decrease in terms of encoding and decoding latency compared with R-S based solutions.

## A construction method of terminated LDPC convolutional codes

- **Status**: ✅
- **Reason**: protograph LDPC convolutional 코드 구성(경계확장+행렬확장 알고리즘) — 이식 가능 코드 설계(E, 바이너리)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7879667
- **Type**: conference
- **Published**: 20-22 Aug.
- **Authors**: Lin Qi, Hao Kang, Tong Liu +1
- **PDF**: https://ieeexplore.ieee.org/document/7879667
- **Abstract**: LDPC convolutional research has far-reaching significance. Its parity check matrix is periodic, which greatly reduces the encoding process and is easy to implement. And different convolutional LDPC codes can carry on the unified coding to the information blocks of the length transformation. The information transfer efficiency can be improved obviously. In the paper, based on the key problem about the construction of the protograph LDPC convolutional codes, the paper studies boundary extension method and matrix extension algorithm. A series of termination convolutional codes are constructed and the performance simulation is carried out. The experimental results show that the structure of terminated LDPC convolutional codes has a better performance than the protograph LDPC codes in the bit error rate.

## Parallelizing LDPC Decoding Using OpenMP on Multicore Digital Signal Processors

- **Status**: ✅
- **Reason**: 정규화 min-sum 디코딩의 멀티코어 OpenMP 병렬화—이식 가능한 디코더 병렬화 기법(C/D)
- **알고리즘 기여**: ✅ 알고리즘/코드 기여
- **ID**: ieee:7576451
- **Type**: conference
- **Published**: 16-19 Aug.
- **Authors**: Murat Sever, Enver Çavus
- **PDF**: https://ieeexplore.ieee.org/document/7576451
- **Abstract**: One attractive solution to long simulation time of LDPC codes is to implement inherently parallel decoding algorithms using multicore platforms. In this paper, we present the first OpenMP parallel implementation of LDPC decoding algorithm on a multicore DSP architecture and report its performance. Parallelized Normalized Min-Sum decoding algorithm is implemented on 8-core Texas Instruments (TI) DSP using OpenMP framework. Performance results are obtained by Unified Instrumentation Architecture (UIA). Our results show that the parallelized decoding on 8-core TI DSP achieves more than 6x speedup compared to single-core version.
