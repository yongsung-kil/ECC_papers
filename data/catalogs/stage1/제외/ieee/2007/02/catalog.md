# IEEE Xplore — 2007-02


## Low density parity check codes for the relay channel

- **Status**: ❌
- **Reason**: 릴레이 채널용 LDPC 프로파일 설계(density evolution), 무선 릴레이 특이적이며 NAND 이식 기법 없음
- **ID**: ieee:4107948
- **Type**: journal
- **Published**: February 2
- **Authors**: Arnab Chakrabarti, Alexandre De Baynast, Ashutosh Sabharwal +1
- **PDF**: https://ieeexplore.ieee.org/document/4107948
- **Abstract**: We propose Low Density Parity Check (LDPC) code designs for the half-duplex relay channel. Our designs are based on the information theoretic random coding scheme for decode-and-forward relaying. The source transmission is decoded with the help of side information in the form of additional parity bits from the relay. We derive the exact relationships that the component LDPC code profiles in the relay coding scheme must satisfy. These relationships act as constraints for the density evolution algorithm which is used to search for good relay code profiles. To speed up optimization, we outline a Gaussian approximation of density evolution for the relay channel. The asymptotic noise thresholds of the discovered relay code profiles are a fraction of a decibel away from the achievable lower bound for decode-and-forward relaying. With random component LDPC codes, the overall relay coding scheme performs within 1.2 dB of the theoretical limit.

## On Achievable Rates and Complexity of LDPC Codes Over Parallel Channels: Bounds and Applications

- **Status**: ❌
- **Reason**: 병렬채널에서 LDPC 달성률 상한·디코딩 복잡도 하한의 순수 이론 bound; 새 디코더/구성으로 안 이어짐
- **ID**: ieee:4069158
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Igal Sason, Gil Wiechman
- **PDF**: https://ieeexplore.ieee.org/document/4069158
- **Abstract**: A variety of communication scenarios can be modeled by a set of parallel channels. Upper bounds on the achievable rates under maximum-likelihood (ML) decoding, and lower bounds on the decoding complexity per iteration of ensembles of low-density parity-check (LDPC) codes are presented. The communication of these codes is assumed to take place over statistically independent parallel channels where the component channels are memoryless, binary-input, and output-symmetric. The bounds are applied to ensembles of punctured LDPC codes where the puncturing patterns are either random or possess some structure. Our discussion is concluded by a diagram showing interconnections between the new theorems and some previously reported results.

## Upper Bounds on the Rate of LDPC Codes for a Class of Finite-State Markov Channels

- **Status**: ❌
- **Reason**: FSMC 채널에서 LDPC 부호율 상한·패리티 밀도 하한의 순수 이론 bound; 디코더/HW/구성으로 안 이어짐
- **ID**: ieee:4069140
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Pulkit Grover, Ajit Kumar Chaturvedi
- **PDF**: https://ieeexplore.ieee.org/document/4069140
- **Abstract**: In this correspondence, we consider the class of finite-state Markov channels (FSMCs) in which the channel behaves as a binary symmetric channel (BSC) in each state. Upper bounds on the rate of LDPC codes for reliable communication over this class of FSMCs are found. A simple upper bound for all noninverting FSMCs is first derived. Subsequently, tighter bounds are derived for the special case of Gilbert–Elliott (GE) channels. Tighter bounds are also derived over the class of FSMCs considered. The latter bounds hold almost-surely for any sequence of randomly constructed LDPC codes of given degree distributions. Since the bounds are derived for optimal maximum-likelihood decoding, they also hold for belief propagation decoding. Using the derivations of the bounds on the rate, some lower bounds on the density of parity check matrices for given performance over FSMCs are derived.

## Parity-Check Density Versus Performance of Binary Linear Block Codes: New Bounds and Applications

- **Status**: ❌
- **Reason**: 패리티검사 밀도 vs 성능의 정보이론적 bound(ML 디코딩), 디코더/HW/구성으로 안 이어지는 순수 이론 bound
- **ID**: ieee:4069163
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Gil Wiechman, Igal Sason
- **PDF**: https://ieeexplore.ieee.org/document/4069163
- **Abstract**: The moderate complexity of low-density parity-check (LDPC) codes under iterative decoding is attributed to the sparseness of their parity-check matrices. It is therefore of interest to consider how sparse parity-check matrices of binary linear block codes can be a function of the gap between their achievable rates and the channel capacity. This issue was addressed by Sason and Urbanke, and it is revisited in this paper. The remarkable performance of LDPC codes under practical and suboptimal decoding algorithms motivates the assessment of the inherent loss in performance which is attributed to the structure of the code or ensemble under maximum-likelihood (ML) decoding, and the additional loss which is imposed by the suboptimality of the decoder. These issues are addressed by obtaining upper bounds on the achievable rates of binary linear block codes, and lower bounds on the asymptotic density of their parity-check matrices as a function of the gap between their achievable rates and the channel capacity; these bounds are valid under ML decoding, and hence, they are valid for any suboptimal decoding algorithm. The new bounds improve on previously reported results by Burshtein  and by Sason and Urbanke, and they hold for the case where the transmission takes place over an arbitrary memoryless binary-input output-symmetric (MBIOS) channel. The significance of these information-theoretic bounds is in assessing the tradeoff between the asymptotic performance of LDPC codes and their decoding complexity (per iteration) under message-passing decoding. They are also helpful in studying the potential achievable rates of ensembles of LDPC codes under optimal decoding; by comparing these thresholds with those calculated by the density evolution technique, one obtains a measure for the asymptotic suboptimality of iterative decoding algorithms.

## Griffith–Kelly–Sherman Correlation Inequalities: A Useful Tool in the Theory of Error Correcting Codes

- **Status**: ❌
- **Reason**: 상관 부등식으로 LDPC 성장률·GEXIT 곡선을 이론적으로 정밀화; 순수 이론, 새 디코더/HW/구성 없음
- **ID**: ieee:4069148
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Nicolas Macris
- **PDF**: https://ieeexplore.ieee.org/document/4069148
- **Abstract**: It is shown that a correlation inequality of statistical mechanics can be applied to linear low-density parity-check codes. Thanks to this tool we prove that, under a natural assumption, the exponential growth rate of regular low-density parity-check (LDPC) codes, can be computed exactly by iterative methods, at least on the interval where it is a concave function of the relative weight of code words. Then, considering communication over a binary input additive white Gaussian noise channel with a Poisson LDPC code we prove that, under a natural assumption, part of the GEXIT curve (associated to MAP decoding) can also be computed exactly by the belief propagation algorithm. The correlation inequality yields a sharp lower bound on the GEXIT curve. We also make an extension of the interpolation techniques that have recently led to rigorous results in spin glass theory and in the SAT problem

## LDPC-Based Iterative Joint Source-Channel Decoding for JPEG2000

- **Status**: ❌
- **Reason**: JPEG2000 결합 소스-채널 복호(JSCC), 제외 카테고리이며 떼어낼 ECC 기법 없음
- **ID**: ieee:4060950
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Lingling Pu, Zhenyu Wu, Ali Bilgin +2
- **PDF**: https://ieeexplore.ieee.org/document/4060950
- **Abstract**: A framework is proposed for iterative joint source-channel decoding of JPEG2000 codestreams. At the encoder, JPEG2000 is used to perform source coding with certain error-resilience (ER) modes, and LDPC codes are used to perform channel coding. During decoding, the source decoder uses the ER modes to identify corrupt sections of the codestream and provides this information to the channel decoder. Decoding is carried out jointly in an iterative fashion. Experimental results indicate that the proposed method requires fewer iterations and improves overall system performance

## On Minimum-WER Performance of a Class of LDPC Codes for the BSC/E Under Extended Bounded-Distance Decoding

- **Status**: ❌
- **Reason**: RCD array code의 bounded-distance 디코딩 WER 임계값 분석, LDPC BP 비의존적 하드디시전 BDD로 떼어낼 ECC 기법 없음
- **ID**: ieee:4100907
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Amitkumar Mahadevan, Joel M. Morris
- **PDF**: https://ieeexplore.ieee.org/document/4100907
- **Abstract**: We study the word-error-rate (WER) performance and the WER-minimizing decision thresholds  $\pm t^{\ast}$ for the class of row-column-diagonal (RCD) array codes and their generalizations on the binary symmetric channel with erasures (BSC/E) where decoding is via an extended bounded-distance decoder (e-BDD). This model applies to very-high-data-rate systems where soft-decision iterative decoding is impractical. We demonstrate that substantial WER performance gain can be obtained, especially at higher channel signal-to-noise ratio (CSNR) ($\hbox{CSNR}\triangleq 10\log_{10} (1/2\sigma^{2})$) values, by employing two optimal thresholds  $(\pm t^{\ast})$ chosen to minimize WER. We study the WER improvement and signal-to-noise ratio (SNR) performance gain as a function of code length  $(n)$ for fixed minimum distance $(d_{\min})$ , and as a function of  $(d_{\min})$ for fixed $(n)$ . A distinct difference in the behavior of WER versus the threshold $t$ , and the optimal threshold $t^{\ast}$  versus SNR, is observed between codes with odd and even $d_{\min}$  , with the even $d_{\min}$ codes exhibiting larger performance improvements when employing a BSC/E instead of a BSC.

## Representation of Mutual Information Via Input Estimates

- **Status**: ❌
- **Reason**: 상호정보-추정 관계의 일반화, MI 수치계산; 정보이론 일반론, LDPC ECC 기법 없음
- **ID**: ieee:4069154
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Daniel P. Palomar, Sergio Verdu
- **PDF**: https://ieeexplore.ieee.org/document/4069154
- **Abstract**: A relationship between information theory and estimation theory was recently shown for the Gaussian channel, relating the derivative of mutual information with the minimum mean-square error. This paper generalizes the link between information theory and estimation theory to arbitrary channels, giving representations of the derivative of mutual information as a function of the conditional marginal input distributions given the outputs. We illustrate the use of this representation in the efficient numerical computation of the mutual information achieved by inputs such as specific codes or natural language

## A Successive Decoding Strategy for Channels With Memory

- **Status**: ❌
- **Reason**: 메모리 채널 successive decoding+interleaver 정보이론 프레임워크; 부호 비의존 채널추정/디코딩 분리, 바이너리 LDPC BP 이식 기법 없음
- **ID**: ieee:4069147
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Teng Li, Oliver M. Collins
- **PDF**: https://ieeexplore.ieee.org/document/4069147
- **Abstract**: This paper presents a new technique for communication over channels with memory where the channel state is unknown at the transmitter and receiver. A deep interleaver combined with successive decoding decomposes a channel with memory into an array of parallel memoryless channels on which a conventional coding system can operate individually. The problems of joint channel estimation and decoding thus are separated without loss of capacity. This technique achieves channel capacity and so may be used to evaluate the capacities of different channels. A general information-theoretic framework is developed and applied to intersymbol interference (ISI), finite-state Markov, and Rayleigh-fading channels. A full system implementation, which performs within 1.1 dB of the channel capacity upper bound, is presented for the Rayleigh-fading channel

## Maximum a Posteriori Estimation Using the EM Algorithm for Linear Codes With Low-Density Generator Matrix in Magnetic Recording Systems

- **Status**: ❌
- **Reason**: 저밀도 생성행렬(LDGM) 선형부호의 EM 기반 MAP/시퀀스 추정; LDPC ECC 아님(소거 추정), 떼어낼 BP 디코더 기법 없음
- **ID**: ieee:4069065
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Hidetoshi Saito, Masayuki Hayashi, Ryuji Kohno
- **PDF**: https://ieeexplore.ieee.org/document/4069065
- **Abstract**: In high-density digital magnetic recording channels, magnetic recording systems are influenced by media noise. It is known that jitter noise is one of the principal sources of the media noise and depends on recording signal patterns. For such a jitter-noise dominant recording channel with continuous erasures, maximum a posteriori (MAP) decoding is hard to minimize the error rate performance of signal processing systems. To improve MAP decoding performance, sequence estimation using the expectation maximization (EM) algorithm is introduced to identify each distribution of the jitter noise in the normal mixture model and estimates the missing sequences which are caused by continuous erasures

## Hybrid Erasure-Error Protocols for Wireless Video

- **Status**: ❌
- **Reason**: 무선 비디오 cross-layer 프로토콜; RS/LDPC는 FEC 베이스라인 부수 언급, 떼어낼 디코더/HW/코드설계 기법 없음
- **ID**: ieee:4066997
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Shirish S. Karande, Hayder Radha
- **PDF**: https://ieeexplore.ieee.org/document/4066997
- **Abstract**: Many recently proposed cross-layer protocols for wireless video, have advocated the relay of corrupted packet to higher layers. Such protocols lead to both errors and erasures at the compressed video application layer. We generically refer to such schemes as hybrid erasure-error protocols (HEEPs). In this paper, we analyze the utility of HEEPs for efficient transmission of video over wireless channels. In order to maintain the generic nature of the deductions in this paper, we base our analysis on two (rather abstract) communication schemes for wireless video: hybrid error-erasure cross-layer design (CLD) and hybrid error-erasure cross-layer design with side-information (CLDS). We make a comparative analysis of the channel capacities of these schemes over single and multi-hop wireless channels to identify the conditions under which the HEEPs can provide improved performance over conventional (CON) protocols. In addition, we employ Reed Solomon (RS) and low-density parity check (LDPC)-code-based forward-error correction (FEC) schemes to illustrate that the improvement in capacity can easily enable an FEC scheme employed in conjunction with a HEEP to provide improved throughput. Finally we compare the performance of CON, CLD, and CLDS in terms of video quality using the H.264 video standard. The simulation results show a significant advantage for the HEEPs

## Lattice Quantization With Side Information: Codes, Asymptotics, and Applications in Sensor Networks

- **Status**: ❌
- **Reason**: Wyner-Ziv 소스코딩(side-info 양자화) 격자 양자화; 채널코딩 ECC 아님(소스 코딩)
- **ID**: ieee:4069160
- **Type**: journal
- **Published**: Feb. 2007
- **Authors**: Sergio D. Servetto
- **PDF**: https://ieeexplore.ieee.org/document/4069160
- **Abstract**: In this paper, we consider the problem of rate/distortion with side information available only at the decoder. For the case of jointly Gaussian source X and side information Y, and mean-squared error distortion, Wyner proved in 1976 that the rate/distortion function for this problem is identical to the conditional rate/distortion function R X|Y, assuming the side information Y is available at the encoder. In this paper we construct a structured class of asymptotically optimal quantizers for this problem: under the assumption of high correlation between source X and side information Y, we show there exist quantizers within our class whose performance comes arbitrarily close to Wyner's bound. As an application illustrating the relevance of the high-correlation asymptotics, we also explore the use of these quantizers in the context of a problem of data compression for sensor networks, in a setup involving a large number of devices collecting highly correlated measurements within a confined area. An important feature of our formulation is that, although the per-node throughput of the network tends to zero as network size increases, so does the amount of information generated by each transmitter. This is a situation likely to be encountered often in practice, which allows us to cast under new-and more "optimistic"-light some negative results on the transport capacity of large-scale wireless networks

## Ensemble Weight Enumerators for Protograph-Based Generalized LDPC Codes

- **Status**: ❌
- **Reason**: protograph G-LDPC ensemble weight enumerator 순수 이론(최소거리 성장), 디코더/HW/구성으로 안 이어지는 bound 분석
- **ID**: ieee:4357601
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Shadi Abu-Surra, William E. Ryan, Dariush Divsalar
- **PDF**: https://ieeexplore.ieee.org/document/4357601
- **Abstract**: Protograph-based LDPC codes have the advantages of a simple design (or search) procedure and highly structured encoders and decoders. These advantages have also been exploited in the design of protograph-based generalized LDPC (G-LDPC) codes. Recently, a technique for computing ensemble weight enumerators for protograph-based LDPC codes has been published. In the current paper, we extend those results to protograph-based G-LDPC codes. That is, we first derive ensemble weight enumerators for finite-length G-LDPC codes based on protographs, and then we consider the asymptotic case. The asymptotic results allow us to determine whether or not the typical minimum distance in the ensemble grows linearly with codeword length.

## Space-Time Mesh Codes for the Multiple-Access Relay Network: Space vs. Time Diversity Benefits

- **Status**: ❌
- **Reason**: 릴레이 네트워크 space-time mesh code 무선 응용 특이적, 떼어낼 NAND ECC 기법 없음
- **ID**: ieee:4357565
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Cheng-Chun Chang, Heung-No Lee
- **PDF**: https://ieeexplore.ieee.org/document/4357565
- **Abstract**: We consider a wireless multiple access network where the sender nodes are aided by a number of relay nodes. A transmission of bit-messages is completed in two phases: in the first phase each sender node originates its message which is overheard at the relay node, and in the second phase each relay node transmits the parity bit calculated from the overheard bit-messages. The low-density parity-check codes are used at the sender nodes in the time-domain, and the low-density generator-matrix code is formed across the spatial domain. At the access node, the received bits from multiple sender nodes and relay nodes are thus encoded in both the time and the spatial domain. We call this combination a space-time mesh code here. In this paper, an iterative decoding scheme is designed for the mesh code and its BER performance in AWGN, fast Rayleigh fading, and quasi-static Rayleigh fading channels are investigated. We note that there is an important trade-off relation between the time-domain and the spatial domain coding. Namely, the time-domain coding is desired when the channel exhibits fast fading; while the spatial domain coding is preferred when the channel is in quasi-static fading state.

## Density Evolution for GF(q) LDPC Codes Via Simplified Message-passing Sets

- **Status**: ❌
- **Reason**: GF(q) 비이진 LDPC density evolution 메시지패싱, 비이진 LDPC라 제외
- **ID**: ieee:4357586
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Brian M. Kurkoski, Kazuhiko Yamaguchi, Kingo Kobayashi
- **PDF**: https://ieeexplore.ieee.org/document/4357586
- **Abstract**: A message-passing decoder for GF(q) low-density parity-check codes is defined, which uses discrete messages from a subset of all possible binary vectors of length q. The proposed algorithm is a generalization to GF(q) of Richardson and Urbanke's decoding "Algorithm E" for binary codes. Density evolution requires a mapping between the probability distribution spaces for the channel, variable and check messages, and under the proposed algorithm, exact density evolution is possible. Symmetries in the message densities permit reduction in the size of the probability distribution space. Noise thresholds are obtained for LDPC codes on discrete memoryless channels, and as with Algorithm E, are remarkably close to noise thresholds under more complex belief propagation decoding.

## On the Codebook-Level Duality Between Slepian-Woif Coding and Channel Coding

- **Status**: ❌
- **Reason**: Slepian-Wolf/채널코딩 듀얼리티 순수 이론, Z_M 링 코드(비이진), 떼어낼 NAND용 디코더/HW/구성 기법 없음
- **ID**: ieee:4357566
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Jun Chen, Da-ke He, En-hui Yang
- **PDF**: https://ieeexplore.ieee.org/document/4357566
- **Abstract**: A codebook-level duality between Slepian-Wolf coding and channel coding is established. Specifically, it is shown that using linear codes over Z M  (the ring of integers mod M), each Slepian-Wolf coding problem is equivalent to a channel coding problem for a semi-symmetric additive channel under optimal decoding, belief propagation decoding, and minimum entropy decoding. Various notions of symmetric channels are discussed and their connections with semi-symmetric additive channels are clarified.

## Group Factorizations and Information Theory

- **Status**: ❌
- **Reason**: 그룹 분해의 정보이론 응용 서베이, girth 큰 그래프 구성 언급뿐 구체 신규 LDPC 디코더·구성 기여 없음
- **ID**: ieee:4357607
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Ulrich Tamm
- **PDF**: https://ieeexplore.ieee.org/document/4357607
- **Abstract**: A factorization of a group G is a collection of subsets (A1, A2,...,Ar) such that every element g isin G has a unique representation g =a1ldr a2ldr...ldrar where a1 isin Ai for i = 1,..., r. We shall survey several applications of group factorizations in information theory. They occur in the analysis of syndromes of integer codes, several graphs with large girth important for LDPC codes can be constructed using group factorizations, and various cryptosystems are based on them.

## Generalized Stopping Sets and Stopping Redundancy

- **Status**: ❌
- **Reason**: erasure 채널 stopping set/stopping redundancy 이론, fountain/erasure 계열로 NAND 채널 ECC에 떼어낼 기법 없음
- **ID**: ieee:4357610
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Khaled A.S. Abdel-Ghaffar, Jos H. Weber
- **PDF**: https://ieeexplore.ieee.org/document/4357610
- **Abstract**: Iterative decoding for linear block codes over erasure channels may be much simpler than optimal decoding but its performance is usually not as good. Here, we present a general iterative decoding technique that gives a more refined trade-off between complexity and performance. In each iteration, a system of equations is solved. In case the maximum number of equations to be solved is just one, the general iterative decoder reduces to the well-known iterative decoder. On the other hand, if the maximum number is set to the redundancy of the codes, the general iterative decoder gives the same performance as the optimal decoder. Varying the maximum number of equations to be solved in each iteration between these two extremes allows for a better match, in terms of performance and complexity, to the system specifications. Stopping sets and stopping redundancy are important concepts in the analysis of the performance and complexity of iterative decoders on the erasure channel. In consequence of the new generalized decoding procedure, the notions of stopping sets and stopping redundancy are generalized as well. Basic properties and examples of both generalized stopping sets and generalized stopping redundancy are presented in this paper.

## A Pragmatic Approach to Coded Continuous-Phase Modulation

- **Status**: ❌
- **Reason**: 코딩된 CPM(연속위상변조) 무선 변조 기법, LDPC 무관·떼어낼 ECC 기법 없음
- **ID**: ieee:4357559
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Sergio Benedetto, Guido Montorsi, Alberto Perotti +1
- **PDF**: https://ieeexplore.ieee.org/document/4357559
- **Abstract**: In this paper, we show that a "pragmatic" approach to coded CPM schemes suffers from a significant capacity loss. This loss can be greatly reduced by choosing an appropriate mapping different from natural or Gray, adopted so far. We propose to add to the CPM modulator a linear feedback, optimized through capacity arguments, that permits to achieve performance within 1 dB from the CPM capacity.

## Searching for low weight pseudo-codewords

- **Status**: ❌
- **Reason**: Slepian-Wolf 소스코딩과 채널코딩 쌍대성, Z_M 비이진 선형부호 이론, 소스코딩+비이진이라 제외
- **ID**: ieee:4357567
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Michael Chertkov, Mikhail Stepanov
- **PDF**: https://ieeexplore.ieee.org/document/4357567
- **Abstract**: Belief propagation (BP) and linear programming (LP) decodings of low density parity check (LDPC) codes are discussed. We summarize results of instanton/pseudo-codeword approach developed for analysis of the error-floor domain of the codes. Instantons are special, code and decoding specific, configurations of the channel noise contributing most to the Frame-Error-Rate (FER). Instantons are decoded into pseudo- codewords. Instanton/pseudo-codeword with the lowest weight describes the largest Signal-to-Noise-Ratio (SNR) asymptotic of FER, while the whole spectra of the low weight instantons is descriptive of the FER vs SNR profile in the extended error-floor domain. First, we describe a general optimization method that allows to find the instantons for any coding/decoding. Second, we introduce LP-specific pseudo-codeword search algorithm that allows efficient calculations of the pseudo-codeword spectra. Finally, we discuss results of combined BP/LP error-floor exploration experiments for two model codes.

## Joint Source-Channel Coding: a Practical Approach and an implementation Example

- **Status**: ❌
- **Reason**: JSCC(소스-채널 결합)+punctured turbo 부호, 채널 ECC가 아닌 결합코딩이라 제외
- **ID**: ieee:4357563
- **Type**: conference
- **Published**: 29 Jan.-2 
- **Authors**: Giuseppe Caire, Maria Fresia
- **PDF**: https://ieeexplore.ieee.org/document/4357563
- **Abstract**: The basic building blocks of most state-of the art source coders are: a linear transformation; scalar quantization of the transform coefficients; probability modeling of the sequence of quantization indices; an entropy coding stage. The weakness of conventional separated source-channel coding approaches lies in the catastrophic behavior of the entropy coding stage. Hence, we replace this stage with linear coding, that maps directly the sequence of redundant quantizer output symbols into a channel codeword. We show that this approach does not entail any loss of optimality in the asymptotic regime of large block length. Furthermore, for practical block lengths and moderate complexity, our approach yields very significant improvements. We develop a full implementation example based on the JPEG2000 image coder and punctured turbo codes. The gain over a conventional separated scheme is demonstrated by extensive numerical experiments on test images.

## Turbo-like MIMO systems with and without space-time codes

- **Status**: ❌
- **Reason**: SCLDGM(LDGM) 부호+MIMO/STBC 무선응용, 비-LDPC 계열이고 떼어낼 바이너리 LDPC BP 기법 없음
- **ID**: ieee:4555628
- **Type**: conference
- **Published**: 12-15 Feb.
- **Authors**: M. Gonzalez-Lopez, F.J. Vazquez-Araujo, L. Castedo +1
- **PDF**: https://ieeexplore.ieee.org/document/4555628
- **Abstract**: We analyze MIMO systems where either Bit-Interleaved Coded Modulation (BICM) by itself or in concatenation with Space-Time Block Codes (STBCs) is used at transmission, assuming iterative Turbo-like decoding at reception. We employ Serially-Concatenated Low-Density Generator Matrix (SCLDGM) codes specifically optimized for each system configuration, and focus on two relevant STBCs: the Golden code, which provides a capacity increase, and Linear Dispersion (LD) codes, which enable practical detection in asymmetrical antenna configurations (i.e., more transmit than receive antennas) for cases in which optimum detection is infeasible.

## Turbo Receiver Design with Carrier-Frequency Offset Estimation for LDPC-Coded MIMO OFDM Systems

- **Status**: ❌
- **Reason**: LDPC-coded MIMO OFDM CFO 추정 turbo 수신기, 무선 응용 특이적이고 LDPC는 베이스라인, 떼어낼 ECC 기법 없음
- **ID**: ieee:4195546
- **Type**: conference
- **Published**: 12-14 Feb.
- **Authors**: S. Salari, M. Ardebilipour, M. Ahmadian +2
- **PDF**: https://ieeexplore.ieee.org/document/4195546
- **Abstract**: This paper proposes an iterative maximum a posteriori probability (MAP) receiver for low-density parity-check (LDPC)-coded multiple-input multiple-output (MIMO) orthogonal frequency division multiplexing (OFDM) systems with the presence of carrier-frequency offset (CFO). The turbo receiver employs the expectation maximization (EM) algorithm so as to improve the performance of the approximated MAP detection, and applies a pilot-aided CFO estimator which can work well with the EM algorithm. Simulation results show the effectiveness of our turbo receiver design in combating CFO over unknown frequency selective fading channels.

## Development of Prototype Board for IEEE802.11n and IP Set

- **Status**: ❌
- **Reason**: 802.11n FPGA 프로토타입 보드, LDPC는 부수 언급일 뿐 떼어낼 신규 디코더·HW 기법 없음
- **ID**: ieee:4195098
- **Type**: conference
- **Published**: 12-14 Feb.
- **Authors**: Yuki Yamanaka, Yuhei Nagao, Kota Higashi +2
- **PDF**: https://ieeexplore.ieee.org/document/4195098
- **Abstract**: A field-programmable gate array (FPGA) prototyping board and several IP sets have been developed for the next generation wireless LAN standard, IEEE802.11n. This standard specifies the use of state-of-the-art wireless technologies such as MIMO-OFDM (multiple-input multiple-output orthogonal frequency division multiplexing) and LDPC(low-density parity check code) error correction, which means that larger LSI chips are needed. The board has five large-scale FPGAs with mesh connections, so it can easily implement MIMO-OFDM systems. The report also presents some RTL-based IP for 11n system such as frame synchronization, carrier synchronization, co-channel interference cancellation, LDPC error correction, fast Fourier transformation (FFT), and inverse fast Fourier transformation (IFFT).

## [Teaser abstract]

- **Status**: ❌
- **Reason**: 컨퍼런스 teaser abstract, 내용 없음
- **ID**: ieee:4252460
- **Type**: conference
- **Published**: 12-14 Feb.
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/4252460
- **Abstract**: Presents abstracts of presentations from the conference proceedings.

## [Teaser abstract]

- **Status**: ❌
- **Reason**: 컨퍼런스 teaser abstract, 내용 없음
- **ID**: ieee:4252458
- **Type**: conference
- **Published**: 12-14 Feb.
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/4252458
- **Abstract**: Presents abstracts of presentations from the conference proceedings.

## [Teaser abstract]

- **Status**: ❌
- **Reason**: 학회 발표 초록 모음(teaser) - 기술 내용 없음
- **ID**: ieee:4252533
- **Type**: conference
- **Published**: 12-14 Feb.
- **Authors**: 
- **PDF**: https://ieeexplore.ieee.org/document/4252533
- **Abstract**: Presents abstracts of presentations from the conference proceedings.
