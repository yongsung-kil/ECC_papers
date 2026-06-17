# IEEE Xplore — 2024-10


## LLD: Lightweight Latency Decrease Scheme of LDPC Hard Decision Decoding for 3-D TLC NAND Flash Memory

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10681227
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Debao Wei, Yongchao Wang, Hua Feng +2
- **PDF**: https://ieeexplore.ieee.org/document/10681227
- **Abstract**: The low-density parity-check code (LDPC) has been widely used to significantly enhance the reliability of 3-D NAND flash memory. However, in cases where the raw bit error rate (RBER) of the data is high, it not only demands more sense levels but also requires a large number of iterations, leading to a notable read latency issue. To mitigate this challenge, this paper introduces an innovative lightweight latency decrease (LLD) scheme. Initially, by examining the correlation between the number of iterations and the hard decision level (HDL), a functional model that encapsulates the relationship between iteration and offset is established. Building upon this model, the all-wordlines latency decrease (AWLD) scheme is proposed. In an effort to further decrease latency, an in-depth analysis of the similarities among different wordlines within a flash memory block is conducted, leading to the development of an optimized one-wordline lightweight latency decrease (OWLLD) scheme. For scenarios involving random reading of small data volumes, the interplay between function models of various overlapping regions is delved into, which ultimately results in the proposal of a further optimized one-page lightweight latency decrease (OPLLD) scheme. Experimental findings reveal that the OPLLD scheme can enhance the iterative performance of LDPC by up to 94.63% and reduce latency by up to 66.89% compared to traditional algorithms, while incurring minimal storage and computational overhead. This clearly indicates that the proposed scheme substantially enhances the read latency performance of LDPC in flash memory.

## Adaptive Interleaver and Rate-Compatible PLDPC Code Design for MIMO FSO-RF Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10538442
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Liang Lv, Zhaojie Yang, Yi Fang +1
- **PDF**: https://ieeexplore.ieee.org/document/10538442
- **Abstract**: This paper conducts an in-depth investigation on the interleaver and error-correction codes for multiple-input multiple-output (MIMO) hybrid free space optical-radio frequency (FSO-RF) systems. Specifically, based on the unequal error protection (UEP) property between the FSO links and RF links, we first propose a novel adaptive interleaver, called protograph variable-node mutual information growth match (PVMIGM) mapping scheme, to boost the performance of MIMO FSO-RF systems with protograph low-density parity-check (PLDPC) codes. Furthermore, by exploiting the protograph extrinsic information transfer (PEXIT) algorithm, we design a type of rate-compatible PLDPC code, called improved rate-compatible PLDPC (IRP) codes, which have both low decoding thresholds and effective typical minimum distance ratios (TMDRs). Simulation results demonstrate that our proposed designs outperform the state-of-the-art counterparts.

## A Heterogeneous and Reconfigurable Decoder for the IEEE 1901 Standard

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10633815
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Yuxing Chen, Zhongfeng Wang
- **PDF**: https://ieeexplore.ieee.org/document/10633815
- **Abstract**: The IEEE 1901 standard plays a crucial role in the extensive fields of smart grids, electric vehicles, and the Internet of Things. The forward error correction (FEC) codes specified in this standard include low-density parity-check convolutional codes (LDPC-CCs), Reed-Solomon (RS) codes, and RS convolutional concatenated (RSCC) codes. This work proposes a low-complexity decoder fully compliant with the standard. First, a heterogeneous scheme is introduced to LDPC-CC decoding. The new scheme assigns different data formats among processing elements (PEs), which reduces the overall storage size and enables a customized datapath down to the PE level. Then, to efficiently support diverse FEC demands in the standard, a reconfigurable architecture is thoroughly explored from both memory and datapath aspects. Leveraging these techniques, the first decoder compatible with the IEEE 1901 standard is developed and implemented with 55nm technology. Implementation results demonstrate that the proposed decoder satisfies the standard’s requirements while exhibiting low hardware complexity.

## GAMP or GOAMP/GVAMP Receiver in Generalized Linear Systems: Achievable Rate, Coding Principle, and Comparative Study

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10511067
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Yuhao Chi, Xuehui Chen, Lei Liu +4
- **PDF**: https://ieeexplore.ieee.org/document/10511067
- **Abstract**: This paper investigates the generalized linear system (GLS), widely employed to evaluate the impact of nonlinear preprocessing on wireless transceivers. Two state-of-the-art signal recovery algorithms, namely generalized approximate message passing (GAMP) and generalized orthogonal/vector AMP (GOAMP/GVAMP), are comparatively studied. They have demonstrated Bayesian optimality for independently and identically distributed (IID) Gaussian matrices and unitary matrices, respectively. However, Bayesian optimality does not inherently guarantee error-free signal recovery. For coded GLS, the information-theoretic (i.e., achievable rate) limit of GAMP remains unknown, and there are still no analytical comparisons between GAMP and GOAMP/GVAMP in terms of the mean-square error and information-theoretic limit. To address these issues, we present the achievable rate analysis and optimal coding principle for GAMP with IID Gaussian matrices, as well as provide comprehensive comparisons with GOAMP/GVAMP with unitary matrices. Specifically, based on the celebrated I-MMSE lemma and the preconditions for state evolution (SE) to hold, the simplified variational SEs of GAMP and GOAMP/GVAMP are derived, leveraging the IID and unitary matrix properties to analyze the achievable rate and optimal coding principle, respectively. On this basis, it is proven that GOAMP/GVAMP outperforms GAMP in terms of asymptotic MSE and maximum achievable rate while requiring less complexity. Furthermore, two common nonlinear functions, clipping and quantization, are used as examples to demonstrate the theoretical comparisons and practical low-density parity-check (LDPC) code design for GAMP and GOAMP/GVAMP. Numerical results show that GAMP and GOAMP/GVAMP with optimized LDPC codes can approach the theoretical limits within 0.3 dB and overcome the decoding deterioration and even divergence of the existing state-of-the-art methods, particularly under low-resolution quantization.

## Intelligent FCDAE Denoiser for Reliable Decoding Over Correlated Noise Channel

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10533442
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Yan Li, Huaiyin Lu, Lin Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10533442
- **Abstract**: In practical systems, colored noise commonly imposes on the data delivered, since the ideal white noise can hardly be achieved. In order to suppress the noise, we propose a denoiser based on a fully convolutional denoising autoencoder (FCDAE) for more reliable information recovery. The smart FCDAE consists of a fully convolution-based encoder and decoder to learn the noise structure distribution in the received signals. Besides, the loss function is selected as a combination of mean square error (MSE) and normality test loss. The proposed denoiser can be further combined with decoders such as the low-density parity-check (LDPC) codes. The simulation results over channels with correlated noise demonstrate that the proposed FCDAE denoiser can effectively improve the signal-to-noise ratio (SNR) and bit error rate (BER) performance, thereby achieving superior reliability performance to benchmark systems.

## Deep Joint Source-Channel Coding for Adaptive Image Transmission Over MIMO Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10597355
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Haotian Wu, Yulin Shao, Chenghong Bian +2
- **PDF**: https://ieeexplore.ieee.org/document/10597355
- **Abstract**: We introduce a vision transformer (ViT)-based deep joint source and channel coding (DeepJSCC) scheme for wireless image transmission over multiple-input multiple-output (MIMO) channels, called DeepJSCC-MIMO. We employ DeepJSCC-MIMO in both open-loop and closed-loop MIMO systems. The novel DeepJSCC-MIMO architecture surpasses the classical separation-based benchmarks, while exhibiting robustness to channel estimation errors and flexibility in adapting to diverse channel conditions and antenna configurations without requiring retraining. Specifically, by harnessing the self-attention mechanism of the ViT, DeepJSCC-MIMO intelligently learns feature mapping and power allocation strategies tailored to the unique characteristics of the source image and prevailing channel conditions. Extensive numerical experiments validate the significant improvements in both distortion quality and perceptual quality achieved by DeepJSCC-MIMO for both open-loop and closed-loop MIMO systems across a wide range of scenarios. Moreover, DeepJSCC-MIMO exhibits robustness to varying channel conditions, channel estimation errors, and different antenna numbers, making it an appealing technology for emerging semantic communication systems.

## Toward Generic Cross-Modal Transmission Strategy

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10507006
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Xin Wei, Junqi Liao, Liang Zhou +2
- **PDF**: https://ieeexplore.ieee.org/document/10507006
- **Abstract**: Multi-modal services, integrating various modalities such as audio, visual, and haptic, have emerged as leading multimedia applications in the 5G era and beyond. To fulfill the demands for low latency, high reliability, and large capacity, cross-modal transmission schemes have been proposed. Typically, these schemes emphasize on either audio-visual or haptic modality, and prioritize flawless transmission of one modality to assist the other modality streaming. However, these prerequisite and assumption do not hold for generic multi-modal services and communication environments, where determining the priority of modality and guaranteeing flawless transmission becomes challenging. To address this fundamental problem, in this paper, we introduce a strategy toward generic cross-modal transmission, enabling visual and haptic modalities to assist each other as needed. The strategy includes a visual-haptic mutual stream delivery mechanism at the sender and a visual-haptic mutual signal reconstruction approach at the receiver. The former aims to eliminate redundancy in visual and haptic streams through mutual assistance, while the latter adaptively handles impaired, missing, or delayed visual or haptic signals by leveraging modality-aware knowledge transfer and semantic-aware signal generation techniques. The proposed strategy demonstrates excellent performance through experiments conducted on a standard multi-modal dataset and a practical visual-haptic communication platform.

## Deep Learning-Based Detection for Marker Codes Over Insertion and Deletion Channels

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10509546
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Guochen Ma, Xiaopeng Jiao, Jianjun Mu +2
- **PDF**: https://ieeexplore.ieee.org/document/10509546
- **Abstract**: Marker code is an effective coding scheme to protect data from insertions and deletions. It has potential applications in future storage systems, such as DNA storage and racetrack memory. When decoding marker codes, perfect channel state information (CSI), i.e., insertion and deletion probabilities, are required to detect insertion and deletion errors. Sometimes, the perfect CSI is not easy to obtain or the accurate channel model is unknown. Therefore, it is deserved to develop detecting algorithms for marker code without the knowledge of perfect CSI. In this paper, we propose two CSI-agnostic detecting algorithms for marker code based on deep learning. The first one is a model-driven deep learning method, which deep unfolds the original iterative detecting algorithm of marker code. In this method, CSI become weights in neural networks and these weights can be learned from training data. The second one is a data-driven method which is an end-to-end system based on the deep bidirectional gated recurrent unit network. Simulation results show that error performances of the proposed methods are significantly better than that of the original detection algorithm with CSI uncertainty. Furthermore, the proposed data-driven method exhibits better error performances than other methods for unknown channel models.

## QAMA: Hierarchical QAM Based Downlink Multiple Access With a Simple Receiver

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10517911
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Jinkang Zhu, Shengli Zhou, Ming Zhao
- **PDF**: https://ieeexplore.ieee.org/document/10517911
- **Abstract**: In this paper, we propose a nonorthogonal downlink multiple access scheme, where the base station assigns the bit streams to different users from an adjustable hierarchical quadrature-amplitude-modulation (QAM) constellation and all users deploy a simple non-iterative receiver with the same complexity as in an orthogonal multiple access (OMA) system. We analyze the achievable information rates of the proposed scheme, termed as QAMA, and show that it possesses a similar rate region as the hybrid OMA and MUST approach in the 5G standard, while the latter relies on successive interference cancellation (SIC) receivers and dynamic switching of two distinct modules. We propose a design procedure to determine a few transmission modes that closely approximate the rate region via a simple polygon. Thanks to the receiver simplicity, easy scalability to more than two users, and the near-optimal rate region, QAMA is an appealing candidate for 6G cellular and other advanced wireless systems.

## Successive interference cancellation-based channel estimation for self-interference cancellation in in-band full-duplex systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10748583
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Jin Kwan Kim, Yunjoong Park, Joon Young Kim
- **PDF**: https://ieeexplore.ieee.org/document/10748583
- **Abstract**: The integrated sensing and communications (ISAC) system has become a promising scheme for combining sensing and communication features to send data and sense the physical space concurrently. Although it aims to understand the channel condition and communication environment with sensing capability, it still requires sustainable high-data transmission with efficient spectrum usage. The in-band full-duplex (IBFD) system can be a possible solution to support high data transmission while increasing spectrum efficiency. Since IBFD has a self-interference issue, one of the significant factors that deteriorate its performance, we need to investigate possible solutions to resolve this matter. In this paper, we present an improved self-interference cancellation receiver with successive interference cancellation (SIC)-based channel estimation for the IBFD system. Since SIC aims to mitigate the multiple interference effects, our proposed algorithm applied SIC to the channel estimation for the performance gain. Our results show that SI cancellation with SIC-based channel estimation improves the IBFD bit error rate (BER) of the new radio (NR) for the ISAC system.

## Soft Demodulator for Symbol-Level Precoding in Coded Multiuser MISO Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10584439
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Yafei Wang, Hongwei Hou, Wenjin Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10584439
- **Abstract**: In this paper, we consider symbol-level precoding (SLP) in channel-coded multiuser multi-input single-output (MISO) systems. It is observed that the received SLP signals do not always follow Gaussian distribution, rendering the conventional soft demodulation with the Gaussian assumption unsuitable for the coded SLP systems. It, therefore, calls for novel soft demodulator designs for non-Gaussian distributed SLP signals with accurate log-likelihood ratio (LLR) calculation. To this end, we first investigate the non-Gaussian characteristics of both phase-shift keying (PSK) and quadrature amplitude modulation (QAM) received signals with existing SLP schemes and categorize the signals into two distinct types. The first type exhibits an approximate-Gaussian distribution with the outliers extending along the constructive interference region (CIR). In contrast, the second type follows some distribution that significantly deviates from the Gaussian distribution. To obtain accurate LLR, we propose the modified Gaussian soft demodulator and Gaussian mixture model (GMM)-expectation-maximization (EM) soft demodulators to deal with two types of signals respectively. Subsequently, to further reduce the computational complexity and pilot overhead, we put forward a novel neural network named pilot feature extraction network (PFEN) to replace the EM algorithm, leveraging the transformer mechanism in deep learning. Simulation results show that the proposed soft demodulators dramatically improve the throughput of existing SLPs for both PSK and QAM transmission in coded systems.

## Multiplexed Streaming Codes for Multi-Hop Multi-Link Communication Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10516574
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Gustavo Kasper Facenda, Ashish Khisti, Wai-Tian Tan +1
- **PDF**: https://ieeexplore.ieee.org/document/10516574
- **Abstract**: This paper studies the transmission of a stream of data packets through a multi-hop multi-link communication network. The source generate sequential source packets and transmits them through a network to a destination. Each intermediary node is allowed to perform any processing operation in order to successfully forward the message to the destination. Each link connecting two nodes is subject to an adversarial packet erasure channel, where the number of erasures is limited. The destination must recover each source packet within a delay deadline, otherwise that packet is considered lost. The particular case when each hop consists of only one link has been studied by Domanovitz et al. (2020). We extend this work to the multi-link scenario by multiplexing multiple copies of streaming codes in Domanovitz et al. (2020) and optimizing the rate using a linear programming framework. We also demonstrate how our framework can be naturally extended when there is a different propagation delay on each link. Numerical results demonstrate that our proposed approach provides significant improvements over baseline schemes. We further demonstrate that our proposed scheme also provides improved audio quality over baseline schemes in experiments involving Gilbert-Elliott channels.

## Guessing Cost: Bounds and Applications to Data Repair in Distributed Storage

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10341332
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Suayb S. Arslan, Elif Haytaoglu
- **PDF**: https://ieeexplore.ieee.org/document/10341332
- **Abstract**: The guesswork refers to the distribution of the minimum number of trials needed to guess a realization of a random variable accurately. In this study, a non-trivial generalization of the guesswork called guessing cost (also referred to as cost of guessing) is introduced, and an optimal strategy for finding the  $\rho $ -th moment of guessing cost is provided for a random variable defined on a finite set whereby each choice is associated with a positive finite cost value (unit cost corresponds to the original guesswork). Moreover, we drive asymptotically tight upper and lower bounds on the logarithm of guessing cost moments. Similar to previous studies on the guesswork, established bounds on the moments of guessing cost quantify the accumulated cost of guesses required for correctly identifying the unknown choice and are expressed in terms of Rényi’s entropy. Moreover, new random variables are introduced to establish connections between the guessing cost and the guesswork, leading to induced strategies. Establishing this implicit connection helped us obtain improved bounds for the non-asymptotic region. As a consequence, we establish the guessing cost exponent in terms of Rényi entropy rate on the moments of the guessing cost using the optimal strategy by considering a sequence of independent random variables with different cost distributions. Finally, with slight modifications to the original problem, these results are shown to be applicable for bounding the overall repair bandwidth for distributed data storage systems backed up by base stations and protected by bipartite graph codes.

## Efficient Address-Embedded Time-Domain Implementation of Minima Finders for Soft Error-Correction Decoders

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10531794
- **Type**: journal
- **Published**: Oct. 2024
- **Authors**: Yang Ge, Dmitri Truhachev, Abolfazl Zokaei +3
- **PDF**: https://ieeexplore.ieee.org/document/10531794
- **Abstract**: This brief presents a novel algorithm that identifies the first six smallest values and their positions in a vector of 256 quantized positive real numbers. The proposed technique is designed for efficient time domain implementation. It operates with signals that are specially structured to contain a pulse width representation of a real number and a pulse-code of its address. The signals are passed through a tree structure where the number of stages and the comparison blocks are devised to yield the best overall performance. To demonstrate the hardware efficiency of this technique, it was successfully implemented using TSMC 65-nm CMOS technology. Experimental results unequivocally showcase that the proposed “minima finder” (MF) algorithm outperforms state-of-the-art solutions in terms of latency and complexity. This makes the proposed architecture a compelling candidate for the hardware implementation of the next-generation high-throughput forward error-correction (FEC) decoders in the realm of fiber-optical communications.

## Simulation Research of LDPC Coding Schemes in Satellite Communication with SC-FDMA

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757587
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Nengtang Hua, Jie Wang, Ming Chen +2
- **PDF**: https://ieeexplore.ieee.org/document/10757587
- **Abstract**: Single Carrier Frequency Division Multiple Access (SC-FDMA) is a promising technology for uplink communication in satellite communication systems due to its advantages such as low peak-to-average ratio, high spectral efficiency, and flexible resource allocation. This paper designs a physical layer model for the satellite communication return link with SC-FDMA modulation. Based on an established satellite return link, we employ a localized FDMA (L-FDMA) subcarrier mapping scheme to compare the burst error rate (BER) simulation performance of three coding schemes: New Radio (NR) LDPC, Wireless Local Area Network (WLAN) LDPC, and Digital Video Broadcasting - Satellite - Second Generation (DVB-S2) LDPC. The simulation results propose that the NR LDPC coding scheme has better BER performance compared to the other two LDPC coding schemes, and the NR LDPC coding scheme is more suitable for satellite burst communication.

## BLER-SNR Curves for 5G NR MCS under AWGN Channel with Optimum Quantization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757540
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Lianet Méndez-Monsanto, Abigail MacQuarrie, Mostafa Rahmani Ghourtani +3
- **PDF**: https://ieeexplore.ieee.org/document/10757540
- **Abstract**: This paper contributes by providing a comprehensive set of block error rate (BLER) vs. signal-to-noise ratio (SNR) curves under additive white Gaussian noise (AWGN) channel conditions for 5G new radio (NR) modulation and coding schemes (MCS) belonging to the 3GPP 5G NR TS 38.214 standard, with low-density parity check (LDPC) coded scenario according to TS 38.212. To enhance practical relevance in the context of O-RAN networks, this paper also introduces the effect of optimum quantization and compares the results without quantization, showing that despite system degradation, the performance remains very close to the unquantized case. By providing this comprehensive dataset, the paper offers valuable insights to support the selection of the most appropriate MCS depending on the required BLER-SNR scenario, serving as a guide in the design of 5G communication systems, for the scheduler, and as lookup tables for the physical layer (PHY) abstraction in link-level simulators (LLS).

## Polar Coded HARQ NOMA in Block Fading Channel with Short Code Length

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757571
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Huan-Lin Lai, Hsuan-Jung Su
- **PDF**: https://ieeexplore.ieee.org/document/10757571
- **Abstract**: Polar codes are known for their good performance relative to other channel codes in the short-code regime. Thus they are suitable for internet of things (IoT) applications that have short transmission bursts and require low latency. To improve the communication reliability and throughput without significantly increasing the transmission power, hybrid automatic repeat request (HARQ) is often used. In this paper, we propose two new algorithms to decide on the number of re-transmission bits in an incremental redundancy (IR) HARQ system with short code length. The first algorithm is based on achieving a certain sequence of probabilities of successful decoding in retransmissions. The second maximizes the expected throughput of the HARQ system. We consider additive white Gaussian noise (AWGN) and Markov model for the block fading channel. The equivalent-length-based method is applied in our system to achieve higher throughput. For both designs, we derive an upper bound on the throughput. Simulations show that the proposed methods outperform the existing methods. We also apply our designs to a non-orthogonal multiple access (NOMA) system. In the NOMA system, we approximate parameters used in our algorithms to prevent storing too many parameters of the combination of the signal-to-noise ratio (SNR). It is found that the set of information bits should be chosen carefully to avoid puncturing bits with high reliability.

## Performance Evaluation of Low Sub-THz 5G NR Sidelink for Ultra-Wideband Short-Range Communication

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757570
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Ryogo Okura, Yusuke Koda, Hiroshi Harada
- **PDF**: https://ieeexplore.ieee.org/document/10757570
- **Abstract**: To meet increasing demands for higher-rate communication, exploring the sub-terahertz (THz) band is attracting huge attention. The first standardization of a sub-THz communication was performed at the IEEE 802.15.3d task group, which designed an ultra-wideband short-range communication operating in a 300 GHz band. However, to alleviate hardware challenges, the usage of a much lower-sub-THz band around 100 GHz should also be considered. Moreover, in terms of the advantage of using shared signal processing circuits with the 5G new radio (NR), the frame format should be designed in a compatible manner with the commercially pervasive 5G NR, which cannot be reached by IEEE 802.15.3d. Motivated by these backgrounds, this paper proposes a 5G NR-based ultra-wideband short-range communication operating in a low sub-THz band that lies in 90–110 GHz. This can be achieved by using 5G NR sidelink communication with the bandwidth expansion to several GHz, and no changes are made for the frame format to retain compatibility. This study conducts a performance evaluation of such a 5G NR sidelink system with a 4 GHz bandwidth by using a channel model at the 93–97 GHz band recently developed for device-to-device short-range communications. The evaluation reveals that the proposed communication system using the 5G NR sidelink can achieve the required block error rate (BLER) equal of 0.1 for both control and user-data transmissions even when a 4 GHz bandwidth is utilized. Moreover, it is shown that transmission at a meter-level distance is feasible even when an omnidirectional antenna in an azimuth plane is used.

## Leveraging parallelizability and channel structure in THz-band, Tbps channel-code decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757607
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Hakim Jemaa, Hadi Sarieddeen, Simon Tarboush +2
- **PDF**: https://ieeexplore.ieee.org/document/10757607
- **Abstract**: As advancements close the gap between current device capabilities and the requirements for terahertz (THz)-band communications, the demand for terabit-per-second (Tbps) circuits is on the rise. This paper addresses the challenge of achieving Tbps data rates in THz-band communications by focusing on the baseband computation bottleneck. We propose leveraging parallel processing and pseudo-soft information (PSI) across multicarrier THz channels for efficient channel code decoding. We map bits to transmission resources using shorter code-words to enhance parallelizability and reduce complexity. Additionally, we integrate channel state information into PSI to alleviate the processing overhead of soft decoding. Results demonstrate that PSI-aided decoding of 64-bit code-words halves the complexity of 128-bit hard decoding under comparable effective rates, while introducing a 4dB gain at a 10−3 block error rate. The proposed scheme approximates soft decoding with significant complexity reduction at a graceful performance cost.

## Nonlinearity-Aided Hybrid ARQ for Satellite Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757736
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: João Madeira, Zahra Mokhtari, João Guerreiro +1
- **PDF**: https://ieeexplore.ieee.org/document/10757736
- **Abstract**: In satellite communications power consumption and reliability are key concerns. The unreliable nature of the wireless channel can cause erroneous transmissions, which must be compensated using retransmissions, at the expense of more power. This issue is aggravated by the low amplification efficiency of high data rate schemes such as Orthogonal Frequency Division Multiplexing (OFDM). Ideally, retransmissions could be avoided entirely by increasing transmission power, however, this would drastically lower the overall energy efficiency of the system. Sophisticated Hybrid Automatic Repeat Request (HARQ) techniques can simultaneously reduce the need for retransmissions and increase the success likelihood of each retransmission attempt (a critical aspect for delay-constraint services over satellite links), while minimizing average consumed power. In this work, we propose a novel HARQ technique where retransmitted signals are submitted to a soft clipping operation that lowers the Peak-to-Average Power Ratio (PAPR) of the OFDM signal, thereby increasing the amplification efficiency. A Generalized Approximate Message Passing (GAMP) based receiver makes use of the additional distortion in the retransmission to increase the likelihood of a successful decoding. It is shown that this approach can outperform Chase Combining (CC) schemes even for Super Quadrature Amplitude Modulation (Super-QAM), while decreasing the power expended during retransmissions.

## Experimental Evaluation of OTFS for Underwater Acoustic Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757871
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Yukang Xue, Xiyuan Zhu, Uzma Khan +1
- **PDF**: https://ieeexplore.ieee.org/document/10757871
- **Abstract**: This paper applies the Orthogonal Time-Frequency Space (OTFS) modulation to underwater mobile acoustic communications where the communication channel suffers from severe multipath and Doppler effects simultaneously. Field experiments have been conducted with acoustic transmission at a center frequency of 115 kHz and a data rate of 11.5 kilosymbols per second. We propose a new Turbo Decision Feedback Equalizer and Decoder (TDFED) for the receiver and the experimental results demonstrate the superior performance of the proposed TDFED algorithm over existing MMSE equalizers.

## Sparse Recurrent Neural Network Architecture for Turbo Decoding in NextGen Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757574
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Madhan Raj Kanagarathinam, Swaraj Kumar, Krishna M. Sivalingam +1
- **PDF**: https://ieeexplore.ieee.org/document/10757574
- **Abstract**: In the rapidly advancing domain of 5G communication systems, channel decoding, particularly turbo decoding, has emerged as a significantly complex challenge. Turbo decoding is an essential element within communication frameworks, necessitating both efficiency and rapid processing to cater to the demanding data rates and stringent low latency requirements of 5G networks. This paper focuses on the unique contributions of employing a Sparse Recurrent Neural Network (SRNN) architecture, leveraging sparsity to reduce computational load while maintaining high performance significantly. Unlike existing approaches, our method introduces a novel piece-wise linear approximation of the activation function, enhancing efficiency and scalability for NextGen communication systems. Our approach leverages the principles of sparsity and employs a piece-wise linear approximation of the activation function to markedly reduce the computational load of the turbo-decoding process.Comprehensive evaluations demonstrate that our RNN architecture outperforms existing deep learning models in the context of turbo decoding and with a significantly lower computational footprint. This research contributes to the field by providing a scalable, efficient, and less computationally intensive turbo-decoding method, particularly suited for the next-generation cloud systems underlying 5G and beyond communication technologies.

## Field Experiments on Highly Robust Mobile Reception for Advanced ISDB-T

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10757514
- **Type**: conference
- **Published**: 7-10 Oct. 
- **Authors**: Hiroaki Miyasaka, Tomoaki Takeuchi, Masahiro Okano
- **PDF**: https://ieeexplore.ieee.org/document/10757514
- **Abstract**: Twenty years has been passed since digital terrestrial television broadcasting service with using ISDB-T started in Japan. Currently, research and development is underway on the next generation of terrestrial broadcasting. In particular, we have been conducting research on advanced digital terrestrial television broadcasting system (Advanced ISDB-T) that can transmit UHDTV content for fixed reception and HDTV content for mobile reception in one channel (6 MHz bandwidth). Advanced ISDB-T has wide range transmission parameters including highly robust parameter that can successfully receive the signals even at C/N=0 dB. Therefore, it is possible to use transmission parameters with a required C/N that is more than 10 dB smaller than that of ISDB-T mobile reception. The authors evaluate a scheme for transmitting audio content by using highly robust transmission parameters to provide uninterrupted mobile service even when video content is interrupted. This paper describes the results of field experiments.

## Concatenated Polar and Non binary LDPC codes for High Reliability in Optical Communication System

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10748489
- **Type**: conference
- **Published**: 4-5 Oct. 2
- **Authors**: Saiith Sethu P, Sam Solomon
- **PDF**: https://ieeexplore.ieee.org/document/10748489
- **Abstract**: Next-generation high-speed optical transport systems require powerful forward error correction (FEC) codes with high error-correcting capabilities to ensure high data reliability. Low density parity check (LDPC) codes are strong candidates for ensuring the high data reliability needed to support data rates of 100 Gb/s, demanded by optical systems. Non-binary LDPC (NB-LDPC) codes provides better performance compared to binary version, as they offer larger coding gains with shorter code lengths and reduced system latency. Despite their advantages, LDPC codes suffer from error floor problem at low bit error rates (BER), with NB-LDPC codes showing error floors at BER around 10-7. High-speed optical transport systems generally require BERs of the order of 10-12. The error floor problem can be mitigated by concatenating LDPC codes with a shorter outer code. Existing works mainly focus on employing Reed Solomon (RS) codes to remove error floor. However, the decoding complexity is high for these codes. This paper proposes concatenated Polar and NB-LDPC codes to address the error floor issue, since polar codes have relatively low encoding and decoding complexity. The channel noise in optical communication systems using optical amplifiers cannot be analyzed using simplified additive white Gaussian noise (AWGN). Hence the channel noise is mathematically derived and proved that chi-square channel model is appropriate than AWGN. Simulation results demonstrate that the proposed concatenated codes over proposed channel model can achieve a net coding gain of around 1.5dB at a BER of 10-12.

## Enhancing the McEliece Scheme Based on Concatenation of Polar Codes and Blocked QC-LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10735591
- **Type**: conference
- **Published**: 30 Sept.-3
- **Authors**: Xin Lin, Yusun Fu, Zihao Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10735591
- **Abstract**: This paper proposes an enhanced McEliece cryptosystem, leveraging a concatenation scheme of Polar codes and blocked QC-LDPC codes. During the key generation phase, the generator matrices for both Polar and blocked QC-LDPC codes are employed as private keys. These matrices are subsequently multiplied by reversible and random permutation matrices respectively. The products of these multiplications are then combined to form the public key, effectively concealing the structural properties of the generator matrices. In the encryption phase, the plaintext is encrypted sequentially through the Polar codes and the blocked QC-LDPC codes. This process introduces two layers of random error vectors, culminating in the generation of the encrypted ciphertext. The proposed scheme reduces the public key length by 54% and doubles the security level compared to the original McEliece scheme with similar parameters. It also significantly reduces the total key length compared to improved schemes based on Polar codes and QC-LDPC/MDPC codes at an 80-bit security level, and shortens the private key length compared to schemes based on Polar-LDPC concatenated codes. Notably, the scheme is secure against known structural and decoding attacks while increases resistance to information set decoding (ISD) attacks. Through the randomization and hashing of the plaintext, the proposed scheme can achieve IND-CCA2 security.

## Burst Detection and Correction for Gilbert Codes and its QC-LDPC Extensions

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758475
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Alina M. Veresova, Andrei A. Ovchinnikov
- **PDF**: https://ieeexplore.ieee.org/document/10758475
- **Abstract**: The article discusses the issue of determining the location of an error burst based on the structure of a block-permutation low-density parity-check code. Quasi-cyclic low-density parity-check codes with a small number of blocks are considered, making it possible to correct the longest possible bursts within this construction. Through experimentation, the maximum, minimum, and average number of attempts was estimated when determining the start position of the error burst. The features of determining the location of a packet in block-permutation low-density parity-check codes are revealed. The proposed method is based on using majority decoding techniques and allows reducing the average number of attempts to locate a burst from hundreds to units for the codes under consideration. Using the packet detection method, which is based on the analysis of the structure of the parity-check matrix, algorithms for decoding Gilbert and extended Gilbert codes have been proposed, ensuring the correction of bursts within their error-correction capabilities. The process of decoding extended Gilbert codes utilizes list decoding in a supercode, with a criterion for selecting the error vector based on the syndrome.

## Density Evolution for GLDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758497
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Alexeev Ivan, Khartov Alexey
- **PDF**: https://ieeexplore.ieee.org/document/10758497
- **Abstract**: In modern communication systems Low-Density Parity Check (LDPC) codes are widely used. It is because of their performance under iterative decoding, hardware-friendly structure and well-known construction methods. For one to construct good LDPC code Density Evolution (DE) can be used, it estimates the decoding threshold, that is it estimates performance of the code. LDPC codes can be further extended to Generalized LDPC (GLDPC) codes, where simple SPC code is replaced with some component code. With more complex structure common DE is no longer correct. This letter presents the upper bound for decoding error and, therefore, an upper bound of a iterative threshold (in dB). It will be shown that the Gaussian approximation gives an upper bound for a decoding error. As one of the results it means that EXIT-charts analysis also gives an upper bound for an iterative threshold for a GLDPC code.

## Low-Density Lattice Codes Based on Golomb Rulers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758537
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Anna Fominykh, Daria Ustinova, Pavel Rybin +1
- **PDF**: https://ieeexplore.ieee.org/document/10758537
- **Abstract**: Low-density lattice codes (LDLC) are a new type of lattice codes that can be decoded effectively and achieve performance levels near the capacity of the additive white Gaussian noise (AWGN) channel. Earlier designs of LDLC, such as those utilizing Latin squares, relied on high-complexity computer searches to eliminate short cycles. The proposed code construction offers a systematic representation and inherently avoids these issues. This study presents a design for LDLC that is based on Golomb rulers. This approach is deterministic and results in a parity-check matrix that is free of short cycles. In all scenarios examined, the LDLC built on Golomb rulers demonstrated superior frame error rate performance compared to those based on Latin squares. For instance, there is a 1.5 dB improvement observed for a dimension of $\mathrm{n}=73$.

## On Joint Neural Min-Sum Decoding and Quantization Optimization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758454
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Vladimir Kuzurman, Dmitry Artemasov, Kirill Andreev +1
- **PDF**: https://ieeexplore.ieee.org/document/10758454
- **Abstract**: Low-density parity-check (LDPC) codes are integral to modern communication systems, including the 5G standard, which supports a new service type known as massive machine type communications (mMTC). mMTC terminals, typically battery-powered and designed for short message transmissions, may face performance challenges with LDPC codes, which excel at longer lengths but show worse performance at shorter ones. Advanced decoders have been developed to address performance issues. One of the approaches enhances the belief propagation (BP)-based decoders by introducing trainable parameters, resulting in the neural BP decoders. To mitigate the energy consumption caused by the decoding complexity, message quantization is also employed in practice. This paper addresses both issues by proposing the collaborative utilization of a neural min-sum decoder to enhance decoding performance and a neural quantizer to reduce computational and memory demands. We present a joint training strategy that achieves superior performance compared to conventional methods.

## On the Concatenation of Superposition and Polar Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758448
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Aleksey Kuvshinov, Ilya Timokhin, Fedor Ivanov
- **PDF**: https://ieeexplore.ieee.org/document/10758448
- **Abstract**: Concatenated codes are currently being actively investigated for the next-generation wireless communication systems due to their flexibility and ability to be used in various scenarios. The serial type of concatenation provides good error-correcting properties with a potential reduction in complexity when an iterative concatenated decoder is used at the receiver side. One of the most effective approaches nowadays is based on integrating an error-correcting code as an outer component and an error-reducing code as an inner component of concatenated construction. There are several approaches to construct a code that has an error-reducing property. Sparse regression codes (SPARC), which are currently being actively researched, may be a promising candidate. These codes exhibit a property to reduce the number of errors in additive white Gaussian noise (AWGN) channel, but they have a high decoding complexity. We propose concatenated scheme with outer polar code and convolutional-based superposition inner code. The latter code is a superposition of BPSK-modulated convolutional codes with successive interference cancellation (SIC) decoder. The use of such a decoder for inner component renders the proposed approach practically feasible.

## Polar Subcodes with Improved Weight Spectrum

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758477
- **Type**: conference
- **Published**: 30 Sept.-2
- **Authors**: Mikhail Oreshin, Peter Trifonov
- **PDF**: https://ieeexplore.ieee.org/document/10758477
- **Abstract**: A method for constructing polar subcodes with a reduced number of low-weight codewords is presented. The proposed approach is based on a method for construction of randomized polar sub codes with optimized error coefficient and explicit generation of all codewords of weight less than twice the minimal non-zero weight of a polar code. Such codewords are enumerated based on the structure of the associated Zhegalkin polynomials. This allows one to construct the dynamic freezing constraints such that almost all of the generated low-weight codewords are excluded from the resulting code. Elimination of low-weight codewords is performed by selection of the coefficients in dynamic freezing constraints, such that the identified low-weight codewords of the parent polar code do not satisfy them. The constructed codes provide similar or better error rate than the polar codes created by methods based on reinforcement learning while being significantly faster to generate. Numerical results, such as the number of low-weight codewords and error rate of codes constructed by the proposed method, are provided.

## Synergizing Error Suppression, Mitigation and Correction for Fault-Tolerant Quantum Computing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10835735
- **Type**: conference
- **Published**: 28-31 Oct.
- **Authors**: Yanzhang Zhu, Siyuan Niu, Di Wu
- **PDF**: https://ieeexplore.ieee.org/document/10835735
- **Abstract**: Quantum computing has showcased potentials to address classically unsolvable problems and attracted research investigation all around the world. However, quantum devices are inherently noisy and create hurdles from true quantum supremacy. Despite researchers have strived to demonstrate quantum advantages at small scales in the noisy intermediate-scale quantum (NISQ) era, we are now at the turning point to craft fault tolerant quantum computers (FTQC) for large scale quantum computing. In this paper, we review the current status of available error control techniques, discuss the missing pieces of each technique for their practical adaptation, and envision the necessity to synergize them across vast design stacks, to enable fault tolerance in quantum computing.

## Towards 6G: Configurable High-Throughput Decoder Implementation for SC-LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942947
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Yuqing Ren, Yifei Shen, Wenqing Song +3
- **PDF**: https://ieeexplore.ieee.org/document/10942947
- **Abstract**: Spatially-coupled low-density parity-check (SC-LDPC) codes are considered an important candidate for the upcoming 6G standardization, owing to their superior error-correction capability and practical decoding complexity. However, current high-throughput SC-LDPC decoders rely on unrolled architectures tailored to a certain code and thus lack the necessary rate compatibility for wireless communications. In this paper, we present a fully reconfigurable decoder architecture for SC-LDPC codes. This hardware architecture can decode virtually any SC-LDPC code that fits in the allocated memories. Based on simplified routing networks, our SC-LDPC decoder can deliver extensive code length and code rate support and achieve high throughput to satisfy the requirements of 6G.

## Optimizing Puncturing Patterns of 5G NR LDPC Codes for Few-Iteration Decoding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942813
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Reinhard Wiesmayr, Darja Nonaca, Chris Dick +1
- **PDF**: https://ieeexplore.ieee.org/document/10942813
- **Abstract**: Rate-matching of low-density parity-check (LDPC) codes enables a single code description to support a wide range of code lengths and rates. In 5 G NR, rate matching is accomplished by extending (lifting) a base code to a desired target length and by puncturing (not transmitting) certain code bits. LDPC codes and rate matching are typically designed for the asymptotic performance limit with an ideal decoder. Practical LDPC decoders, however, carry out tens or fewer message-passing decoding iterations to achieve the target throughput and latency of modern wireless systems. We show that one can optimize LDPC code puncturing patterns for such few-iteration-constrained decoders using a method we call swapping of punctured and transmitted blocks (SPAT). Our simulation results show that SPAT yields from 0.20 dB up to 0.55 dB improved signal-to-noise ratio performance compared to the standard 5G NR LDPC code puncturing pattern for a wide range of code lengths and rates.

## Towards Flexible LDPC Coding for 6G

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942769
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Paul Bezner, Jannis Clausius, Marvin Geiselhart +5
- **PDF**: https://ieeexplore.ieee.org/document/10942769
- **Abstract**: Current communication standards employ a variety of different channel coding schemes, complicating hardware implementation. We present a novel low-density parity-check (LDPC) coding scheme for 6G that aims to reduce complexity and increase implementation efficiency. The scheme uses only a single base matrix, while offering a similar flexibility as the current 5G LDPC code at an improved communication performance. Moreover, addressing the need for larger transport block sizes to achieve higher throughput, the proposed code supports longer block lengths than those of 5G. The code can be decoded using the well-known belief propagation (BP) algorithm, as well as automorphism ensemble decoding (AED) for improved error correction in the short block length regime, allowing a trade-off between performance and complexity to suit a wide range of application requirements.

## Channel Coding Under Silicon Implementation Constraints

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942759
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Oliver Griebel, Lucas Johannsen, Claus Kestel +2
- **PDF**: https://ieeexplore.ieee.org/document/10942759
- **Abstract**: The slowdown in semiconductor technology ad-vances presents challenges for next-generation communication systems. These systems require continuous improvements in error correction performance, throughput, and energy efficiency. Although transistor density continues to follow Moore's law, there has been a notable decline in gains of interconnect delay and energy consumption. This raises two research challenges. First, data transfers contribute increasingly to the energy consumption for advanced technology nodes. Second, bridging the increasing gap between technology capabilities and demands in commu-nication systems necessitates cross-layer optimizations. In this work, we address both issues by investigating low-density parity-check (LDPC) and polar code decoder implementations. We quantify the energy consumption impact of different data transfer structures in the Tanner graph for high-throughput LDPC code decoder. Furthermore, we quantify the gains from cross-layer optimization only and the gains from technology advances only for high-throughput polar code decoders and compare them.

## Decoding Quasi-Cyclic Quantum LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10756177
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Louis Golowich, Venkatesan Guruswami
- **PDF**: https://ieeexplore.ieee.org/document/10756177
- **Abstract**: Quantum low-density parity-check (qLDPC) codes are an important component in the quest for quantum fault tolerance. Dramatic recent progress on qLDPC codes has led to constructions which are asymptotically good, and which admit linear-time decoders to correct errors affecting a constant fraction of codeword qubits. These constructions, while theoretically explicit, rely on inner codes with strong properties only shown to exist by probabilistic arguments, resulting in lengths that are too large to be practically relevant. In practice, the surface/toric codes, which are the product of two repetition codes, are still often the qLDPC codes of choice. A previous construction of qLDPC codes based on the lifted product of an expander-based classical LDPC code with a repetition code (Panteleev and Kalachev, 2020) achieved a near-linear distance, and avoids the need for such intractable inner codes. Our main result is an efficient decoding algorithm for these codes that corrects a near-linear number of adversarial errors. En route, we give a similar algorithm for the hypergraph product version these codes, which are simpler but have distance growing only as the square root of the block length. Our decoding algorithms leverage the fact that the codes we consider are quasi-cyclic, meaning that they respect a cyclic group symmetry. Since the repetition code is not based on expanders, previous approaches to decoding expander-based qLDPC codes, which typically worked by greedily flipping code bits to reduce some potential function, do not apply in our setting. Instead, we reduce our decoding problem (in a black-box manner) to that of decoding classical expander-based LDPC codes under noisy parity-check syndromes. For completeness, we also include a treatment of such classical noisy-syndrome decoding that is sufficient for our application to the quantum setting.

## A Layered CPA Decoder for Reed-Muller Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942623
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Jiajie Li, Warren J. Gross
- **PDF**: https://ieeexplore.ieee.org/document/10942623
- **Abstract**: When decoding low-rate and short-length Reed-Muller (RM) codes, the recently proposed projection-aggregation (PA) decoder yields near maximum-likelihood decoding performance. However, the practicability of the PA decoder's implementation is nevertheless negatively impacted by its high computational cost. It has been demonstrated that this decoder is closely connected to the belief propagation (BP) decoder based on the parity-check matrix. Techniques inspired by the layered decoding and the broadcast modification for the BP decoder used by the low-density parity-check codes are proposed in this work. The proposed broadcast modification reduces the computational overhead induced by the proposed layered decoding for the collapsed PA (CPA) decoder. The proposed layered and broadcast-based CPA decoder has negligible degradation in decoding performance, and it produces a 47% reduction in the average complexity at $E_{b}/N_{0}=2.5\text{dP}$, when decoding RM(8, 3) codes.

## New Perspectives on Convolutional Coding/Decoding for 6G

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942983
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Joseph Jabour, Jeremy Nadal, Stefan Weithoffer +2
- **PDF**: https://ieeexplore.ieee.org/document/10942983
- **Abstract**: In recent years, significant efforts were invested in (de-)coding of convolutional codes and their concatenations by leveraging alternative representations which aim to lower the decoding complexity. One example is the Local-SOVA algorithm that avoids redundant computations by reformulating the BCJR algorithm towards the notion of providing partial extrinsic information. This latter is now provided along path metric computations in the code trellis leading to a significant reduction in complexity. For high coding rates where most redundant computations are made, the trellis compression technique represents an appealing solution to reduce the complexity of warm-up calculations for BCJR-based turbo decoding. In addition, BP based decoding solutions have come a long way to bridge the gap between initially disappointing results and BCJR performance. In this work, we propose to extend and combine several new representations of the code targeting reduced decoding complexity for short convolutional codes and their concatenations. Based on our new perspective, we give an outlook on convolutional based FEC for 6G.

## Capacity of a Binary Channel with a Time-Bounded Adversary

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942906
- **Type**: conference
- **Published**: 27-30 Oct.
- **Authors**: Mingjun Ying, Fatih Berkay Sarpkaya, Serhat Bakirtas +3
- **PDF**: https://ieeexplore.ieee.org/document/10942906
- **Abstract**: This paper addresses the challenge of ensuring reliable communication over binary input memoryless channel under the influence of a time-bounded adversary. The adversary can arbitrarily overwrite a fraction $\delta$ of the received symbols. This model can be used for intermittent hardware errors or adversarial attacks in the receiver processing. The worst-case adversarial capacity is derived using infinite shared randomness to enable coordinated interleaving against the adversary. It is shown that the capacity can be achieved simply with a random interleaver along with a thresholded log-likelihood ratio (LLR) decoder, which can be readily implemented on top of most standard decoder architectures in use in practical systems today. We show that the worst-case adversary targets highly reliable bits to maximize disruption. Simulations are presented on AWGN channels with $M$-QAM modulation for both the theoretical capacity as well as the practical capacity with LDPC codes with the proposed thresholded LLR method.

## Image Transmission Based on DnCNN Adaptive Selection of Significant Bit Optimization

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11117122
- **Type**: conference
- **Published**: 25-27 Oct.
- **Authors**: Qinglin Tang, Xu Zhan, Yong Sun +3
- **PDF**: https://ieeexplore.ieee.org/document/11117122
- **Abstract**: To address the problem of low reliability in soft decoding for wireless image transmission in extremely low signal-to-noise ratio environments, a method based on Deep Convolutional Neural Network combined with an adaptive highposition bit selection algorithm(DnCNN-AHPBS) is proposed to enhance quality of image transmission in low signal-to-noise ratio environments. Firstly, the image information is mapped to a bitstream for 16 QAM modulation, and then the modulation information is encoded by 5G new radio access technology LDPC channel coding, and then transmitted wirelessly through the MIMO-OFDM communication system. Secondly, after being wirelessly transmitted in a low signal-to-noise ratio environment, the bits are restored to the image structure in DnCNN assisted optimization. Finally, the high position bit information selected by the DnCNN-AHPBS algorithm is mapped into a constellation diagram for flipping and replacement. This method adjusts the initial log-likelihood ratio information of the Minimum Offset Sum (OMS) algorithm to obtain an optimized log likelihood ratio and reduce the error rate of image transmission in low signal-to-noise ratio environments. The simulation results indicate that a specific bit error rate will result in a 1.4 dB bit signal-to-noise ratio gain at extremely low signal-to-noise ratios. The DnCNN-AHPBS algorithm has to some extent improved the reliability of wireless transmission soft decoding in extremely low signal-to-noise ratio environments.

## Low-Latency High-Throughput Decoder of QC-LDPC Codes by Matrix Splitting

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827659
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Xinyu Zhong, Shuaicong Gong, Ming Jiang +1
- **PDF**: https://ieeexplore.ieee.org/document/10827659
- **Abstract**: As the continuously increasing demand of high data rate and lower transmission, many modern communication systems employ the LDPC coding scheme with ultra-high throughput decoder to achieve these challenging requirements. However, due to the implementation complexity of decoding algorithm, designing an ultra-high throughput decoder of LDPC codes still suffers many difficulties. Therefore, we propose a FPGA-based LDPC decoder with partial parallel decoding, which splits and virtually supplements the parity-check matrix to achieve higher throughput and lower latency. Our proposed FPGA-based decoder can achieve a throughput of 6.072Gbps in 10 iterations for the highest rate 5G-LDPC code.

## Pruning Path Min-Sum Decoding Algorithm for High-Rate Non-Binary LDPC Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827053
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Liyuan Song, Hanxiang Yu, Xiaosong Zhang +2
- **PDF**: https://ieeexplore.ieee.org/document/10827053
- **Abstract**: The fixed path Min-Sum (FMS) algorithm efficiently decodes non-binary LDPC codes with low/moderate code rates, but suffers significant performance degradation for high code rates. This paper enhances its check node (CN) update by selecting deviation paths of high reliability according to their correct probabilities and positions over the trellis of a CN. Moreover, a path pruning strategy is introduced during the CN update to reduce the complexity of path search. Analysis results indicate that the proposed pruning path Min-Sum (PMS) algorithm efficiently decodes high-rate non-binary LDPC codes.

## Constructing Random QC-LDPC Codes Based on the Relationship between 8-Cycles and Trapping Sets

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10826749
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Shirong Lv, Guohua Zhang, Defeng Ren
- **PDF**: https://ieeexplore.ieee.org/document/10826749
- **Abstract**: This paper presents a computer-aided search scheme based on simulated annealing methodology for regular quasi-cyclic low-density parity-check (QC-LDPC) codes, ensuring a minimum girth of at least 8. The approach utilizes the simulated annealing algorithm, leveraging the correlation between cycles and trapping sets, and analyzes their positioning in the Tanner graph to iteratively reduce trapping sets. This process ultimately results in the generation of high-girth QC-LDPC codes. A significant advantage of our method is that it greatly reduces the search time compared to existing approaches. Furthermore, our method generates QC-LDPC codes that demonstrate a diminution in the number of 8-cycles, concurrently achieving a reduction in detrimental trapping sets. Simulation results reveal that our method generates QC-LDPC codes with excellent bit error rate performance.

## Design of Spatially Coupled LDPC Codes with Girth at Least 8

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827040
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Yuxiang Zhou, Jian Fang, Baoming Bai +1
- **PDF**: https://ieeexplore.ieee.org/document/10827040
- **Abstract**: Spatially coupled low-density parity-check (SC-LDPC) codes are a special type of sparse graph codes that have recently attracted great interest due to their capacity-approaching performance. To reduce the performance loss in-curred by short cycles, this paper proposes a method based on the greatest common divisor (GCD) full-length row-multiplier (FLRM) matrix to construct girth-8 quasi-cyclic SC-LDPC codes with improved performance and flexible code rates. Besides, we further extend the lower bound of the circulant permutation matrix (CPM) size to be compatible with different code lengths. Numerical results demonstrate that the proposed SC-LDPC code has performance gains of 1.05 dB and 1.0 dB compared with that based on RS structure at an BER of 10−6over AWGN channels for code rates 0.45 and 0.625, respectively. Additionally, SC-LDPC codes based on the GCD constraint achieve the trade-off between decoding performance and complexity..

## McEliece Public-Key Cryptosystem Based on Cyclic Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827328
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Junlong Ye, Deyuan Chen, Shaoshuai Gao +2
- **PDF**: https://ieeexplore.ieee.org/document/10827328
- **Abstract**: The McEliece public key cryptosystem is known for its resistance to quantum attacks. However, its application potential remains limited due to challenges such as large key size and low coding efficiency. In this paper, we proposed a McEliece public-key cryptosystem based on cyclic codes to reduce the key size. The matrix generated by the Goppa codes is replaced with the matrix generated by the cyclic code in encoding, the private key matrix is transformed into the row vector of the generator polynomial. Performance evaluations and security analysis reveal that the refined system retains commendable coding efficacy and security with a condensed key space.

## Adaptive Modulation and Coding Techniques Based on Reinforcement Learning

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10826945
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Haozhe Gu, Ningyan Guo, Tianyu Xue +1
- **PDF**: https://ieeexplore.ieee.org/document/10826945
- **Abstract**: Traditional Adaptive Modulation and Coding (AMC) techniques rely on real-time and accurate Signal-to-Noise Ratio (SNR) estimates, but often resulting in suboptimal data transmission performance in scenarios with significant link transmission delays and rapid channel changes. This paper introduces a reinforcement learning (RL) algorithm to enhance traditional AMC techniques. By applying Q-learning principles to define the RL framework, including state space, action space, and reward, this study proposes a Q-learning-based AMC technique. Leveraging RL's robust perception and decision-making capabilities in uncertain environments, this method mitigates the shortcomings of traditional AMC techniques, such as coarse channel state partitioning and mismatched state lookup tables, especially in dynamic channel conditions, thereby reducing resource inefficiencies and enhancing system throughput. Evaluation of spectral efficiency and bit error rate under conditions of rapid channel changes and SNR estimation errors due to feedback delays reveals that the Q-learning-based AMC technique achieves superior performance compared to threshold-based AMC methods.

## Semantics Guided Diffusion for Deep Joint Source and Channel Coding Design

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10826825
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Maojun Zhang, Guangxu Zhu, Kaifeng Han +2
- **PDF**: https://ieeexplore.ieee.org/document/10826825
- **Abstract**: Semantic communication (SemCom) offers a promising avenue for enhancing transmission efficiency, especially as traditional bit-level communication approaches its theoretical limits. A key enabling technology in SemCom is deep learning-based joint source and channel coding (DeepJSCC). However, existing DeepJSCC methods lack interpretability because they transmit semantic information implicitly by mapping data to latent features. Additionally, the black-box nature of neural networks makes it challenging to ensure the reliable transmission of critical semantics. To address these challenges, we propose advancing DeepJSCC towards a more “semantic” approach. Specifically, we suggest transmitting interpretable and lightweight semantics as side information alongside JSCC latent features. At the receiver end, we introduce a novel latent diffusion model designed for wireless communication, trained from scratch to integrate seamlessly with DeepJSCC. Using the semantic side information, the receiver employs the proposed semantics-guided latent diffusion for denoising. Furthermore, since accurate channel state information (CSI) is essential in practice, we propose estimating CSI directly from the channel output. The estimated CSI is then used for step matching in the denoising diffusion process, enabling CSI-free transmission. Finally, the denoised feature is fed into the JSCC decoder to reconstruct the image. Numerical results demonstrate that our proposed scheme can achieve comparable performance without accurate CSI. Additionally, guided by semantic information and leveraging the powerful diffusion model, our method surpasses current DeepJSCC schemes, delivering satisfactory reconstruction performance even at SNR = −5dB. This proposed scheme highlights the potential of incorporating diffusion models in future SemCom systems and suggests several promising applications.

## Multiuser Interference Suppression: A Generalized Nearest Neighbor Decoding Approach

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827590
- **Type**: conference
- **Published**: 24-26 Oct.
- **Authors**: Shuqin Pang, Wenyi Zhang
- **PDF**: https://ieeexplore.ieee.org/document/10827590
- **Abstract**: The architecture of the proposed generalized nearest neighbor decoding (GNND) is investigated under quadrature phase shift keying (QPSK) and utilized for multiuser interference suppression. The GNND is capable of handling the non-Gaussian inter-stream interference effectively, for multiuser channels under QPSK input, while the conventional channel linearization (CL) approach generally fails. Adopting the information-theoretic tool of generalized mutual information (GMI) for measuring the achievable information rate, the optimal GNND in maximizing GMI is derived. A coded modulation scheme based upon GNND is further designed, via connected with the existing low-density parity-check decoders, without requiring iterations between demodulation and decoding. Numerical results show that the GNND significantly outperforms the CL approach in terms of the achievable code rate and the bit-error-rate.

## Analysis of Signal Propagations Between an Access Point and IoT Devices in a Complex Indoor Environment Using Ray Tracing

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10758988
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Kanwalinderjit Kaur, Priscilla Zavala
- **PDF**: https://ieeexplore.ieee.org/document/10758988
- **Abstract**: The fifth generation (5G) of wireless communication networks uses the advantages of Massive Multiple-Input Multiple-Output (MIMO) technologies to improve network coverage, increase data speeds, and enhance reliability. One of the challenges that has risen from utilizing massive MIMO as a leading technology in the advancement of 5G is the difficulty to model massive MIMO channels due to the high cost of the hardware and the computational complexity. In this research, ray tracing, which is an effective channel modeling method, is employed using the MIMO- Orthogonal frequency division multiplexing (OFDM) technique to simulate the interactions between various IoT devices and the network's access point. The ray tracing evaluation is performed on a 3D model of a conference room which allows for the evaluation of the network's performance in a complex indoor environment. The experiments are run using different surface materials and channel parameters are measured for each experiment to understand the different factors that affect the performance. The power delay and the path loss for an IoT device in the line of sight (LOS) and an IoT device not in LOS are analyzed. The magnitude of the signals propagated to an IoT device in LOS are higher and the path loss is lower. Furthermore, using metal as the surface material results in the least amount of path loss, and using wood results in the highest amount of path loss. The bit error rates when metal, glass, and wood are used are also measured. The use of metal results in the lowest bit error rates and wood results in the highest bit error rates for the IoT devices.

## NavIC L1C: Signal Receiving and Processing Using Software-Defined Receiver

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11201184
- **Type**: conference
- **Published**: 22-25 Oct.
- **Authors**: Abhishek Kumar, Abhijit Dey, Nitin Sharma +3
- **PDF**: https://ieeexplore.ieee.org/document/11201184
- **Abstract**: As part of the Navigation with Indian Constellation (NavIC) modernization, the standard positioning service (SPS) is now also being transmitted on the L1 band (1575.42 MHz), along with previous L5 and S-bands. This modern signal brings new features, such as a new modulation scheme synthesized-binary offset carrier (SBOC) and data/pilot channels compatible with other L1C services. These innovations can improve the robustness of signal acquisition and tracking. Unlike the conventional tracking method that employs separate data for message demodulation, it fails to fully utilize the signal energy and data-pilot phase relationship, leading to diminished tracking accuracy. To investigate the performance of the new signal in both acquisition and tracking strategies, this paper introduces the receiving and processing of NavIC L1C using a software-defined receiver approach. Experimental results on both real-time signals (only NVS-01) and simulated signals are presented.

## Enhancing 5G Performance: Reducing Service Time and Research Directions for 6G Standards

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10765762
- **Type**: conference
- **Published**: 21-24 Oct.
- **Authors**: Laura Landon, Vipindev Adat Vasudevan, Jaeweon Kim +3
- **PDF**: https://ieeexplore.ieee.org/document/10765762
- **Abstract**: This paper presents several methods for minimizing packet service time in networks using 5G and beyond. We propose leveraging network coding alongside Hybrid Automatic Repeat reQuest (HARQ) to reduce service time as well as optimizing Modulation and Coding Scheme (MCS) selection based on the service time. Our network coding approach includes a method to increase the number of packets in flight, adhering to the current standard of the 16 HARQ process limit, demonstrating that these strategies can enhance throughput and reduce latency. Experimental results show that network coding reduces service times by up to 7% in low SNR regimes, with greater reduction across all SNR as the number of packets in flight increases, suggesting that future 6G standards should consider increasing the number of HARQ processes for better performance.

## Effective Utilization of Spectrum for Next Generation Wireless Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10772771
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Sonali, Subhas Mondal
- **PDF**: https://ieeexplore.ieee.org/document/10772771
- **Abstract**: The earlier idea of the communication system was to focus on modulation and channel coding schemes as separate entities. However, later the perspective of coded modulation was introduced by coding theorists and system designers. In this manuscript, we propose a Low Density Parity Check (LDPC) coded and bit-interleaved precoder, which is added before a 256-Quadrature Amplitude Modulation (QAM) and Reed-Solomon (RS) coded system. This technique significantly enhances the spectral efficiency (measured in bits per two-dimensional symbol) and improves the performance of coded modulation over a fading channel. By bitwise interleaving at the encoder output, the system disperses errors, making them easier to correct, while RS codes provide additional reliability by correcting symbol errors. Consequently, the proposed method boosts both spectral efficiency and overall system reliability, ensuring high data integrity in challenging transmission environments.

## Building a Real-Time Physical Layer Labeled Data Logging Facility for 6G Research

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10942742
- **Type**: conference
- **Published**: 21-23 Oct.
- **Authors**: Franco Minucci, Raquel Marina Noguera Oishi, Haoqiu Xiong +7
- **PDF**: https://ieeexplore.ieee.org/document/10942742
- **Abstract**: This work describes the architecture and vision of designing and implementing a new test infrastructure for 6G physical layer research at KU Leuven. The Testbed is designed for physical layer research and experimentation following several emerging trends, such as cell-free networking, integrated communication, sensing, open disaggregated Radio Access Networks, AI-Native design, and multiband operation. The software is almost entirely based on free and open-source software, making contributing and reusing any component easy. The open Testbed is designed to provide real-time and labeled data on all parts of the physical layer, from raw IQ data to synchronization statistics, channel state information, or symbol/bit/packet error rates. Real-time labeled datasets can be collected by synchronizing the physical layer data logging with a positioning and motion capture system. One of the main goals of the design is to make it open and accessible to external users remotely. Most tests and data captures can easily be automated, and experiment code can be remotely deployed using standard containers (e.g., Docker or Podman). Finally, the paper describes how the Testbed can be used for our research on joint communication and sensing, over-the-air synchronization, distributed processing, and AI in the loop.

## Generalized Index Modulation System and Application for Satellite Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10753254
- **Type**: conference
- **Published**: 19-21 Oct.
- **Authors**: Khaled A. Ghorib, Amr Abdelaziz, Ahmed F. Darwesh +1
- **PDF**: https://ieeexplore.ieee.org/document/10753254
- **Abstract**: The generalized index modulation (G-IM) technique provides an improvement in bit error rate (BER), spectral efficiency (SE), and/or energy efficiency (EE) over traditional digital modulation schemes. However, G-IM techniques suffer from the propagation of errors due to the incorrect detection of indices for higher modulation order (M > 4). To alleviate the risk of error propagation, the enhancement of the correct indices detection probability is a crucial requirement for G-IM systems. This paper presents an error propagation-free generalized index modulation (G-IM) system with adaptive coding modulation in which the indices bits are coded independently on the information bits. The main focus of this study is to derive a quantitative relation between the target system BER and the required indices error rate and, hence, to derive the overall system error probability. In particular, an analytical total BER formula for the error propagation-free G-IM system is provided and compared to the total BER of the classical counterpart modulation techniques. Hence, a direct relationship between the BER of index bits and the ordinary modulation BER is represented, providing an approximate threshold after which the target BER of the G-IM system outperforms the traditional modulation techniques. To validate our established results, the G-IM system with low density parity check code with binary phase shift keying modulation technique (LDPC-BPSK), as a simple satellite coding-modulation scheme which is used in satellite digital video broadcasting TV (DVB-T2) and deep-space communications, is described as a possible direct application for the G-IM system. once the index BER exceeds the threshold, the LDPC-BPSK modulated G-IM system significantly outperforms the classical BPSK modulation while keeping the same EE or SE yet on the expense of added encoder complexity. Moreover, once the index error tends to the zero point, the total G-IM BER reaches its lower limit, a 3 dB gain, thanks to power reallocation in the information bits which represents, on average, 50% of the entire frame.

## A Partial Parallel Architecture Encoder for QC-LDPC Coding

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10946634
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Ruijiang Yin, Ke Jia
- **PDF**: https://ieeexplore.ieee.org/document/10946634
- **Abstract**: To meet the demand for quasi-cyclic low-density parity-check (QC-LDPC) codes, this paper proposes an encoder architecture specifically designed for QC-LDPC coding, compatible with the majority of QC-LDPC codes. The encoder is designed based on a forward substitution(FS) efficient coding algorithm, implemented in a partially parallel structure for efficient encoding,with the optimized encoder significantly improving hardware usage efficiency (HUE).

## New Construction of QC-LDPC Codes Based on Full-Length Row-Multiplier

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10946320
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Ke Jia, Yu Qin, Mei Li
- **PDF**: https://ieeexplore.ieee.org/document/10946320
- **Abstract**: This paper proposes a new explicit construction method for quasi-cyclic (QC) low-density parity-check (LDPC) codes without 4-cycles and 6-cycles with large column weights. Two integer sequences entirely define the exponent matrix of the new method. The first sequence is an arithmetic sequence starting from 0 with a tolerance of 1, and the second sequence is a special sequence composed of integers that meet the constraint of the greatest common divisor (GCD). The existing explicit method can only provide a variety of row weight types with large circulant size. Compared with the recently proposed symmetric structure method based on computer search, the new explicit construction method has better decoding performance, extremely low description complexity, and does not require computer search.

## Learning to Design Constellation of MLC With Geometric Shaping

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10946339
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Fan Ding, Ming Jiang, Yi Wang +2
- **PDF**: https://ieeexplore.ieee.org/document/10946339
- **Abstract**: This letter proposes a constellation design of geometric shaping (GS) for multilevel coding (MLC) and bit-interleaved coded modulation (BICM) systems with high spectral efficiency. In order to optimize the GS of constellation, our proposed autoencoder based on deep learning is composed of parallel-connected encoders and serial-connected decoders, fully learning the characteristics of MLC. Then the optimized constellations are applied in the MLC scheme and compared to quadrature amplitude modulation (QAM) with square constellations (SQCs) and ATSC 3.0 non-uniform constellations (NUCs). It is shown that the decoding performance of MLC scheme using our GS optimized constellation is close to that of the NUC-based BICM with nearly half of the decoding complexity. Moreover, our simulation results demonstrate that the MLC scheme with trained constellation can achieve better gain for higher order modulations, such as 210-QAM.

## Stochastic Gradient Descent Based MIMO Detection with Interference Rejection Combining

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10946447
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Yubin Zhu, Ruobing Yang, Ya Gao +2
- **PDF**: https://ieeexplore.ieee.org/document/10946447
- **Abstract**: Multiple-input multiple-output (MIMO) technology promises high spectrum utilization and system capacity and has been seen as a key technology for modern wireless communication systems. With the rapid increase in the demand for system capacity, the interference between adjacent cells cannot be ignored, and the antenna scale is constantly increasing, which makes it increasingly difficult for uplink MIMO receivers to achieve the cubic complexity of the MMSE-IRC algorithm. Some methods based on series or approximate solutions provide quadratic complexity but have difficulty achieving interference suppression. To solve this issue, we proposed a method for calculating the equalization matrix based on the stochastic gradient descent algorithm. We theoretically proved that it can converge to the equalization matrix of the MMSE-IRC algorithm. After that, we experimentally demonstrated that its performance loss is within 0.2dB and the complexity does not exceed the quadratic, which provides a potential solution for reducing the complexity of uplink receivers in massive MIMO systems.

## Joint Interference Mitigation, Channel Estimation and Data Detection in OFDM Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10946374
- **Type**: conference
- **Published**: 18-20 Oct.
- **Authors**: Wenfeng Gao, Xiaoyan Kuai
- **PDF**: https://ieeexplore.ieee.org/document/10946374
- **Abstract**: In this paper, we investigate the orthogonal frequency division multiplexing (OFDM) system in the presence of impulsive noise (IN) and narrowband interference (NBI). To overcome the performance degradation caused by the IN and NBI, we develop a novel joint estimation scheme based on an iterative processing framework at the receiver, where the modules in this framework incorporate the NBI and IN estimation, channel estimation, and data decoding. In the receiver processing, the linear estimator is first employed to jointly obtain the minimum mean-square error (MMSE) estimates. Then the denoisers are used for further correction of the estimates. Concretely, we adopt a gridless variational line spectral estimation (VALSE) method to refine the estimate of NBI in the NBI denoiser. Furthermore, we exploit the sparsity of IN in the time domain for accurate estimation in the IN denoiser. After channel estimation, the valid data is forwarded to the soft demodulator for data decoding. All the modules are operated within a turbo iteration framework until the algorithm convergence. Simulation results validate the superiority and robustness of the proposed method.

## Non Binary Polar Codes for Short Reach Optical System Based on an Efficient Channel Model

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10750708
- **Type**: conference
- **Published**: 18-19 Oct.
- **Authors**: Sajith Sethu P, Sam Solomon
- **PDF**: https://ieeexplore.ieee.org/document/10750708
- **Abstract**: Next generation short reach optical systems demand forward error correction codes with low latency decoding for ultra reliable data transmission. Polar codes are a new class of capacity achieving codes which outperforms the widely used low density parity check codes, for shorter codeword lengths, as required by short reach optical transmission systems. Short reach optical systems typically employ intensity modulation and direct detection, which employ erbium doped fiber amplifiers for optical amplification. Eventhough a few works on binary polar code based optical systems are available in literature, all of them utilizes additive white Gaussian noise (AWGN) to model the channel noise. But this assumption is neither accurate nor realistic noise model here since the noise distribution is non-Gaussian. In this paper, the noise distribution of the optical channel is first mathematically derived and is proved that the chi-square distribution is more accurate. Non-binary polar codes provide same coding gain as that of binary polar codes, with shorter codeword length. This paper presents a non-binary polar code based short reach optical communication system with chi-square channel model. The successive cancellation list decoding for non-binary polar codes is used in order to reduce the latency and complexity in decoding. The error performance analysis of the non-binary polar codes with proposed channel model indicates that a coding gain of more than 1dB can be obtained compared to the AWGN channel model. Additionally, the performance enhancement of the non-binary polar codes over binary version is evaluated in terms of link distance.

## Security Improvement for Deep Learning-Based Semantic Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10908341
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Hung Ngo Luu Tan, Van-Dinh Nguyen, Thien Huynh-The +2
- **PDF**: https://ieeexplore.ieee.org/document/10908341
- **Abstract**: Semantic communication is becoming increasingly popular for wireless image transmission due to its superior communication efficiency. However, current deep learning-based semantic systems designed for semantic communication, though efficient, remain vulnerable to eavesdropping and often overlook security measures at the physical layer. To address this issue, this paper presents a deep learning-based system with joint source-channel coding (JSCC) and cyclical consistent generative adversarial network that enhances the security of semantic communication systems. We also design a convolutional neural network for the encoder and decoder which is trained to extract and transmit semantic features while minimizing the risk of privacy leakage. The artificial noise at the physical layer is employed at the source to degrade the eavesdropping ability of the eavesdropper. We show through experiments that under the artificial noise strategy, the legitimate user achieves a higher structural similarity index measure (SSIM) and peak signal-to-noise ratio (PSNR) than the eavesdropper. Moreover, the semantic system with JSCC offers better SSIM and PSNR than the separated source and channel coding models while preserving the confidentiality of semantic information during wireless transmission. This enhanced security framework opens new opportunities for secure and reliable communication of semantic information in diverse applications.

## Multi-User Physical Network Coding Scheme with Low-Resolution ADCs at the Base Station

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10908167
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Hung Dang, Hieu T. Nguyen
- **PDF**: https://ieeexplore.ieee.org/document/10908167
- **Abstract**: In this paper, we investigate the application of Physical Layer Network Coding (PNC) in Multi-user Massive MIMO systems that use low-resolution analog-to-digital (ADC) converters on the receiving side to reduce hardware costs and power consumption. We explore the performance gains from combining massive multiple-input multiple-output (MIMO) and PNC techniques. PNC helps reduce the number of timeslots needed for end-to-end communication, thereby boosting the capacity of the wireless system. We utilize a method that transforms the chan-nel between a massive-antenna relay and multiple multi-antenna user terminals using a Sum-Difference (SD) matrix before applying a linear signal detection algorithm. By using an approximation model to establish the relationship between the input and output of a low-resolution ADC, we derive an expression that accounts for the finite number of quantization levels to compute the Log-Likelihood Ratio (LLR) of the network-coded bit. We evaluate the error performance of the proposed scheme through extensive simulations across different resolution levels and multi-user configurations. The results demonstrate that the PNC technique significantly outperforms conventional network coding, as the PNC processing algorithm leverages the benefits of signal superposition in wireless MIMO channels.

## Efficient Blind and Semi-Blind Approaches on Encoded Wiretap Full-Duplex Transmissions

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10908139
- **Type**: conference
- **Published**: 17-19 Oct.
- **Authors**: Bao Quoc Vuong, Roland Gautier, Anthony Fiche +1
- **PDF**: https://ieeexplore.ieee.org/document/10908139
- **Abstract**: This paper investigates the secrecy coding analysis of encoded wiretap Full-Duplex transmission respected to various eavesdropper positions. To limit the effect of interference and self-jamming/jamming signals sending by the legitimate receiver and eavesdropper, a combination of joint iterative blind/semi-blind channel estimation, decoding algorithms and self-jamming techniques is used. In fact, these algorithms employ a feedback loop to estimate and reduce SI components while also estimating the propagation channel and decoding the messages. The results reveal that blind/semi-blind algorithms give a better solution than conventional without feedback algorithms by significantly reducing and giving smaller security gap. Furthermore, they are less sensitive to the eavesdropper's movement by maintaining security gap in an acceptable level. The results also indicate that the suggested algorithms have a capability to notably decrease the self-jamming power required at the authorized receiver to obtain the same security level. It shows a robustness in several factors such as security, reliability and power consumption, which is suitable for short-packet Internet of Things transmissions and green communications.

## Combination of 5G Broadcast and DVB-I Technologies for Unified Access to TV Services

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10755843
- **Type**: conference
- **Published**: 17-18 Oct.
- **Authors**: Dmitry Tkachenko, Eugene Popov, Victor Vargauzin
- **PDF**: https://ieeexplore.ieee.org/document/10755843
- **Abstract**: 5G Broadcast is technology that provides opportunities for broadcast and multicast delivery of TV services to mobile devices. The paper describes possible ways for unified access to broadcast and unicast TV services at 5G mobile devices using DVB-I technology. The opportunity for combination of 5G Broadcast and other types of TV delivery networks is also considered.

## Experimental Evaluation of Iterative Demodulator of Coded SEFDM-signals with Higher-Order Modulation Subcarriers

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10755725
- **Type**: conference
- **Published**: 17-18 Oct.
- **Authors**: Viet Them Nguyen, Andrey Rashich
- **PDF**: https://ieeexplore.ieee.org/document/10755725
- **Abstract**: This paper addresses the transmission and reception experiment of spectrally efficient frequency division multiplexing signals (SEFDM) reception with high-order modulation methods on subcarriers using NI USRP 2920. An iterative demodulation algorithm in conjunction with message-passing decoder for NR LDPC codes is utilized to demodulate coded SEFDM-signals. Spectral and BER performances of SEFDM-signals with QPSK, QAM-16 on subcarriers at various code rates are considered. In comparison with the results of the simulation, the experiments show approximate results of no more than 0.2 dB energy loss at BER = 10–5 and QAM-16 on the subcarriers. The experimental model allows flexible change of the signal designs and parameters depending on the requirements of various tasks.

## Performance of LDPC Codes in Rayleigh Block Fading Channels with Interleaving

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827339
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Sangwon Chae, Gangsan Kim, Hyojeong Choi +1
- **PDF**: https://ieeexplore.ieee.org/document/10827339
- **Abstract**: This paper presents an experimental analysis of Low-Density Parity-Check (LDPC) codes over Rayleigh block fading channels, focusing on the impact of various interleaving configurations. The Frame Error Rate (FER) performance of LDPC codes is evaluated under various block fading conditions and interleaving configurations. The results demonstrate that certain interleaving configurations can enhance performance depending on the block fading parameters.

## On the Design of Parity-Check Polar Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827520
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Hyosang Ju, Siwon Jang, Sang-Hyo Kim
- **PDF**: https://ieeexplore.ieee.org/document/10827520
- **Abstract**: In this paper, a bnew design of a pre-coded polar code, named parity-check systematic pre-coding (PCSP) polar code is studied. The parity-check polar codes outperform the CRC-concatenated polar codes in general, as they are eligible for a generalized concatenated coding design. During the successive cancellation decoding, the scattered parity bits perform single-parity-check protection. Since the conventional scheme neglects some weaknesses originating from the parity-check pre-coding structure, we propose a new bit-classification strategy for the PCSP polar codes. The simulation results demonstrate that the proposed design consistently outperforms the conventional one for various coding parameters.

## Implementation of High-Speed LDPC Decoder Using SDFEC for 5G-Adv and 6G

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827578
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Yong Su Lee, Jun Woo Kim, Moon Young Jin +4
- **PDF**: https://ieeexplore.ieee.org/document/10827578
- **Abstract**: This paper discusses the implementation technology aimed at reducing the power consumption and weight of a wireless backhaul system mounted on drones, which is used to temporarily establish high-speed communication networks in preparation for disasters. To implement a drone-mounted modem capable of high-speed wireless data communication at speeds of over 1 Gbps, we utilized the XCZU48DR (Xilinx Zynq UltraScale+ RF -SoC) that includes an LDPC (Low Density Parity Check Code) decoder core. By using the four SDFEC (Soft Decision Forward Error Correction) cores within the XCZU48DR, we performed LDPC (Low Density Parity-check Code) decoding and achieved decoding performance of over 1 Gbps. Therefore, this paper presents the implementation details of a high-speed LDPC decoder using SDFEC with performance exceeding 1 Gbps.

## Evaluation of Sum-product Decoding Iteration Number for LDPC Coding FEC in Spectrum Suppressed Transmission

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827185
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Yuki Kurihara, Takatoshi Sugiyama
- **PDF**: https://ieeexplore.ieee.org/document/10827185
- **Abstract**: In recent years, a new concept called NTN (Non-terrestrial Network) has been considered in Beyond 5G/6G to expand the communication area in three dimensions, and the demand for satellite communications is expected to increase further in the future. To solve this problem, spectrum suppressed transmission has been proposed. In previous studies, the number of LDPC coding sum-product decoding iterations in single career QPSK modulations have been evaluated only 10 times. In this paper, we optimize the number of decoding iterations for each suppression rate when LDPC coding in single career QPSK modulations are applied to spectrum suppressed transmission, and quantitatively evaluate the improvement effect of BER performances at the optimal number of iterations and the processing delay time depending on the number of decoding iterations.

## On the Decoding Complexity of Error Correction Code Transformer

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10826987
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Seungjun Kim, Jeongwon Choe, Youngjoo Lee
- **PDF**: https://ieeexplore.ieee.org/document/10826987
- **Abstract**: Belief propagation (BP) decoding achieves near-optimal performance with large block lengths but faces performance degradation with short blocks. Recent advances in deep learning have spurred research into neural decoders to overcome the limitations of BP decoding. The error correction code transformer (ECCT) offers state-of-the-art decoding performance, yet it demands substantial computational complexity and memory usage. This paper analyzes the hardware complexity of ECCT compared to the basic neural decoder, neural BP (NBP). We also explore strategies for model simplification, showing that applying quantization techniques can reduce resource overhead while maintaining high performance. This paper highlights the potential for advancing neural decoders to achieve greater efficiency and performance.

## Twofold Information Reconciliation Based on Polar Codes for CV-QKD

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10827110
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Chuwen Yang, Meixiang Zhang, Yuheng Wang +1
- **PDF**: https://ieeexplore.ieee.org/document/10827110
- **Abstract**: Continuous variable quantum key distribution (CV-QKD) enables authenticated parties to share a key. Information reconciliation (IR) is a critical step of the post-processing in CV-QKD, significantly affecting the secret key rate (SKR) shared between the legitimate parties. To improve the SKR performance of the CV-QKD without increasing the key inconsistency rate (KIR), this paper proposes a twofold IR method by performing independent operations on the Gaussian modulated coherent states (GMCS) obtained over the quantum channel. Specifically, assuming reverse reconciliation, after the GMCS are quantized, Bob generates parity bits, which are shared with Alice to help her correct the inconsistent bits in the quantized bits to generate the partial key. At the same time, the parity bits are used as frozen bits of polar codes in the multidimensional reconciliation (MR) to generate the other partial key. Simulation results demonstrate that the proposed twofold IR method increases the SKR nearly twice without increasing the inconsistent bits. In addition, we propose to apply symbol expansion and rotation (SER) based on the mapped GMCS to reduce the amount of information to be transmitted over the public error-free channel. Simulation results demonstrate that the performance of the proposed twofold IR with SER method can achieve a higher SKR with 3dB performance gap to that of the traditional MR protocol.

## A Perfect Secrecy Communication Scheme Based on Strictly Typical Artificial Noise and Cascaded Secure Codes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10736451
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Ren Duan, Meng Ma, Chaohai Du
- **PDF**: https://ieeexplore.ieee.org/document/10736451
- **Abstract**: This paper proposes a perfect secrecy-achieving scheme for wireless communication systems. Most existing physical layer security schemes can achieve only weak or strong secrecy. One of the main reasons is the uncertainty of the eavesdropping channels. In order to achieve perfect secrecy, we design the artificial noise (AN) as a strictly typical sequence to guarantee that the eavesdropping channel is degraded with probability 1. In addition, a cascaded code is also designed to achieve both reliability and security. Theoretical analysis proves that the proposed scheme can transmit private message with finite code length without any information leakage. Finally, security performance of the proposed scheme is measured and compared with theoretical bounds, and a tradeoff between AN power consumption and decoding threshold is also analyzed numerically.

## Intelligent System for Integration in 5G Networks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10814794
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: E.G. Stanescu, C. Zamfirescu, T.C. Stoian +1
- **PDF**: https://ieeexplore.ieee.org/document/10814794
- **Abstract**: This study investigates the performance and resilience of 5 G networks through an experimental setup based on 3GPP standards, employing Open5GS and srsRAN software. A baseline for normal network operations was established, with key metrics including channel quality indicators (CQI) and bitrates, followed by the introduction of controlled jamming to assess network disruptions. The network’s response to these disruptions was analyzed using a Random Forest (RF) algorithm, which demonstrated perfect accuracy in distinguishing between normal and jamming states. The results underscore the potential of 5 G technology in applications requiring low latency and high reliability, such as autonomous vehicles and remote surgeries. Furthermore, the study explores security implications and future advancements in edge computing and network slicing, contributing to a deeper understanding of 5G networks’ capabilities and vulnerabilities.

## Coded Multi-User Extreme Massive MIMO Systems with Gauss Seidel-Aided MMSE-PIC

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10826779
- **Type**: conference
- **Published**: 16-18 Oct.
- **Authors**: Han Jin Park, Heesang Chung, Sung-Woo Choi +1
- **PDF**: https://ieeexplore.ieee.org/document/10826779
- **Abstract**: This paper discusses the design methodology of a concatenated coding system utilizing Gauss-Seidel-aided MMSE-PIC and LDPC codes, used in extreme massive MIMO systems. The proposed design method enhances the BER (Bit Error Rate) performance convergence speed of the system compared to conventional designs, with reduced computational complexity. To achieve this, the paper tracks the overall data flow of the system and conducts EXIT analysis, predicting BER performance convergence speed, which aligns with actual BER performance through simulation. Therefore, the analysis and design methodology proposed in this paper for LDPC Coded Gauss-Seidel-aided MMSE-PIC systems are expected to play a crucial role in next-generation communication systems (6G) that demand high-speed data processing.

## Experimental performance analysis of a low complexity 20 Gb/s PAM4-PON based on legacy 10G hardware

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10746115
- **Type**: conference
- **Published**: 15-18 Oct.
- **Authors**: Germán V. Arévalo, Milton N. Tipán, Henry Ati
- **PDF**: https://ieeexplore.ieee.org/document/10746115
- **Abstract**: This paper presents the experimental performance analysis of a $20 \mathrm{~Gb} / \mathrm{s}$ PAM4-PON which was deployed using 10 G legacy electrical and optical hardware. It studied the behavior of the BER vs the decrement of the received optical power on the ONU side and the behavior of the optical path penalty. The test results of the $20 \mathrm{~Gb} / \mathrm{s}$ PON were contrasted with the performance of a traditional $10 \mathrm{~Gb} / \mathrm{s}$ PAM2-NRZ PON. With a received optical power of -10 dBm it was possible to achieve a BER of $10^{-9}$ with the PAM4-PON, whilst in a PAM2-NRZ PON the same BER is achievable when a signal of $\mathbf{- 1 9} \mathrm{dBm}$ is received in the ONU. The optical path penalty of the PAM4 is greater than 2.5 dB when the optical link length is close to 30 km, but it is very low when the ODN is shorter than 25 km.

## Heuristic Rate-Adaptive Reconciliation in Continuous-Variable Quantum Key Distribution

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11028745
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Yilun Hai, Yingjian Wang, Riccardo Bassoli +1
- **PDF**: https://ieeexplore.ieee.org/document/11028745
- **Abstract**: In continuous-variable quantum key distribution (CV-QKD), the information reconciliation step plays a crucial role in ensuring the security and efficiency of the key exchange process. This paper investigates the use of heuristic and reinforcement learning-based methods to adaptively adjust the low-density parity check (LDPC) code rate in response to the time-varying channel signal-noise-ratio (SNR), with the goal of maximizing the final key rate. Leaving the SNR to fluctuate by ±1dB around a fixed value, we analyze the trade-off between the reconciliation efficiency and the frame error rate (FER). We propose a rate-adaptive reconciliation scheme that leverages reinforcement learning to select the optimal LDPC code rate, comparing its performance against traditional fixed-rate approaches. The results demonstrate that the proposed adaptive scheme significantly enhances the key rate and shows potential in applying for a wide range of SNR.

## Evaluating Quantum Channels with 5G-Compliant Error Correction Schemes

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:11028815
- **Type**: conference
- **Published**: 15-17 Oct.
- **Authors**: Siddharth Das, Riccardo Bassoli, Frank H. P. Fitzek
- **PDF**: https://ieeexplore.ieee.org/document/11028815
- **Abstract**: Bridging the gap between classical and quantum communication is a well sought-after topic with significant potential in fortifying the networks of the future. In that direction, we have attempted to analyse realistic quantum channels through the lens of classical communication frameworks. To achieve this, we have developed a simulation environment that integrates classical link-level simulator with a quantum simulator, allowing an in-depth assessment of quantum noise impacts on 5G-compliant error correction code (ECC). We focused on the performance of low density parity check (LDPC) codes and polar codes under the influence of these quantum models. The comparative analysis, primarily on bit error rate (BER) performance demonstrates a clear advantage for LDPC codes across both quantum channel under identical simulation conditions. The results of this study offer valuable insights into how classical ECC perspectives can be applied to quantum channels, guiding the selection of appropriate error correction schemes tailored to specific quantum channel models.

## UAV Swarm Collaborative Transmission Optimization for Machine Learning Tasks

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10763871
- **Type**: conference
- **Published**: 10-14 Oct.
- **Authors**: Liangchen Chao, Bo Zhang, Hengpeng Guo +2
- **PDF**: https://ieeexplore.ieee.org/document/10763871
- **Abstract**: Recent developments in artificial intelligence technologies have seen an increasing volume of real-time data, collected by unmanned aerial vehicle (UAV), and processed by machine learning (ML) techniques instead of human labor. Traditional transmission techniques aiming at low loss rates are hence rendered ineffective for ML. In this paper, we investigate a collaborative transmission optimization method among a group of UAVs, with the goal of maximizing the efficiency of server-side ML tasks. Towards this end, we propose a novel network-coding enabled multi-agent deep reinforcement learning approach named DC-MAPPO in the UAV Ad Hoc network with limited resources. Our method deploys random linear network coding for source packet coding, with an improved multi-agent proximal policy optimization algorithm combining the dual-clip method for broadcasting strategy optimization. We adopt a handwriting recognition algorithm based on the MNIST dataset to verify the effectiveness of DC-MAPPO. Simulation results demonstrate that DC-MAPPO outperforms baseline schemes in terms of rewards, rate of convergence, and recognition efficiency of ML algorithms.

## Using Reed-Solomon Codes to Securely Transmit Data Over Radio Frequencies Using Broadband Communications

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10851530
- **Type**: conference
- **Published**: 10-12 Oct.
- **Authors**: Nikita Galkin, Alla Levina
- **PDF**: https://ieeexplore.ieee.org/document/10851530
- **Abstract**: The purpose of the research work is to analyze the energy gain and reliability improvement in data transmission using Reed-Solomon codes in a noisy channel of broadband communication.The paper analyzes the applicability of Reed-Solomon codes for secure information transmission. The model of integrity assessment of transmitted data on the basis of methods of noise-proof coding with the help of cyclic block Reed-Solomon codes is developed. According to the results of the model study the energy gain and reliability improvement in data transmission using Reed-Solomon codes in the noisy channel of broadband communication are analyzed.

## Bit-Flipping LDPC Decoding Algorithm for Optical Fiber Communication Systems

- **Status**: ⬜ 미선별
- **Reason**: N/A
- **ID**: ieee:10828774
- **Type**: conference
- **Published**: 1-3 Oct. 2
- **Authors**: Oulfa Laouar, Imed Amamra, Nadir Derouiche
- **PDF**: https://ieeexplore.ieee.org/document/10828774
- **Abstract**: The increasing popularity of optical communication systems emphasizes the need for effective errorcorrection solutions, including high-efficiency hardware decoder designs and codes with strong performance. Within optical communication networks, Low-Density Parity-Check (LDPC) codes utilizing sparse matrices and decoded through the Bit-Flipping (BF) algorithm, known for its hard iterative decoding approach are extensively utilized. These codes effectively balance decoding complexity with error-correction performance.This paper focuses on comparing the optical performance of LDPC codes with and without the BF decoding algorithm using two simulation software packages: MATLAB and OptiSystem 7.0. The comparison is conducted across different wavelengths and quality factors. Through this study, we evaluate the advantages of LDPC codes in terms of error-rate reduction and enhancing the reliability of optical transmission.
