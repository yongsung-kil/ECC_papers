# arXiv — 2018-01


## LEDAkem: a post-quantum key encapsulation mechanism based on QC-LDPC codes

- **Status**: ❌
- **Reason**: QC-LDPC 기반 post-quantum KEM 암호(보안) 응용, 채널 ECC 아님; 새 디코더는 암호 복호용으로 NAND 이식성 낮음
- **ID**: arxiv:1801.08867v1
- **Type**: preprint
- **Published**: 2018-01-26
- **Authors**: Marco Baldi, Alessandro Barenghi, Franco Chiaraluce +2
- **PDF**: https://arxiv.org/pdf/1801.08867v1
- **Abstract**: This work presents a new code-based key encapsulation mechanism (KEM) called LEDAkem. It is built on the Niederreiter cryptosystem and relies on quasi-cyclic low-density parity-check codes as secret codes, providing high decoding speeds and compact keypairs. LEDAkem uses ephemeral keys to foil known statistical attacks, and takes advantage of a new decoding algorithm that provides faster decoding than the classical bit-flipping decoder commonly adopted in this kind of systems. The main attacks against LEDAkem are investigated, taking into account quantum speedups. Some instances of LEDAkem are designed to achieve different security levels against classical and quantum computers. Some performance figures obtained through an efficient C99 implementation of LEDAkem are provided.

## Analysis and Design of Serially Concatenated LDGM Codes

- **Status**: ❌
- **Reason**: LDGM/SCLDGM 코드 점근 성능·error floor 이론 분석으로 LDGM은 생성행렬 기반 별도 클래스, 떼어낼 신규 바이너리 LDPC 디코더·HW 없음
- **ID**: arxiv:1801.08270v2
- **Type**: preprint
- **Published**: 2018-01-25
- **Authors**: Amrit Kharel, Lei Cao
- **PDF**: https://arxiv.org/pdf/1801.08270v2
- **Abstract**: In this paper, we first present the asymptotic performance of serially concatenated low-density generator-matrix (SCLDGM) codes for binary input additive white Gaussian noise channels using discretized density evolution (DDE). We then provide a necessary condition for the successful decoding of these codes. The error-floor analysis along with the lower bound formulas for both LDGM and SCLDGM codes are also provided and verified. We further show that by concatenating inner LDGM codes with a high-rate outer LDPC code instead of concatenating two LDGM codes as in SCLDGM codes, good codes without error floors can be constructed. Finally, with an efficient DDE-based optimization approach that utilizes the necessary condition for the successful decoding, we construct optimized SCLDGM codes that approach the Shannon limit. The improved performance of our optimized SCLDGM codes is demonstrated through both asymptotic and simulation results.

## Asymptotic Analysis on Spatial Coupling Coding for Two-Way Relay Channels

- **Status**: ❌
- **Reason**: two-way relay 채널 compute-and-forward용 SC-LDPC DE 점근분석, 무선 응용 특이적이며 떼어낼 신규 디코더·구성 기법 없음
- **ID**: arxiv:1801.06328v1
- **Type**: preprint
- **Published**: 2018-01-19
- **Authors**: Satoshi Takabe, Yuta Ishimatsu, Tadashi Wadayama +1
- **PDF**: https://arxiv.org/pdf/1801.06328v1
- **Abstract**: Compute-and-forward relaying is effective to increase bandwidth efficiency of wireless two-way relay channels. In a compute-and-forward scheme, a relay tries to decode a linear combination composed of transmitted messages from other terminals or relays. Design for error correcting codes and its decoding algorithms suitable for compute-and-forward relaying schemes are still important issue to be studied. In this paper, we will present an asymptotic performance analysis on LDPC codes over two-way relay channels based on density evolution (DE). Because of the asymmetric nature of the channel, we employ the population dynamics DE combined with DE formulas for asymmetric channels to obtain BP thresholds. In addition, we also evaluate the asymptotic performance of spatially coupled LDPC codes for two-way relay channels. The results indicate that the spatial coupling codes yield improvements in the BP threshold compared with corresponding uncoupled codes for two-way relay channels.

## The decoding failure probability of MDPC codes

- **Status**: ❌
- **Reason**: MDPC 부호의 암호용 복호실패확률 분석; bit-flipping 복호 분석이 암호(McEliece/키교환) 맥락이고 NAND 이식할 신규 디코더·구성 기여 없음
- **ID**: arxiv:1801.04668v1
- **Type**: preprint
- **Published**: 2018-01-15
- **Authors**: Jean-Pierre Tillich
- **PDF**: https://arxiv.org/pdf/1801.04668v1
- **Abstract**: Moderate Density Parity Check (MDPC) codes are defined here as codes which have a parity-check matrix whose row weight is $O(\sqrt{n})$ where $n$ is the length $n$ of the code. They can be decoded like LDPC codes but they decode much less errors than LDPC codes: the number of errors they can decode in this case is of order $Θ(\sqrt{n})$. Despite this fact they have been proved very useful in cryptography for devising key exchange mechanisms. They have also been proposed in McEliece type cryptosystems. However in this case, the parameters that have been proposed in \cite{MTSB13} were broken in \cite{GJS16}. This attack exploits the fact that the decoding failure probability is non-negligible. We show here that this attack can be thwarted by choosing the parameters in a more conservative way. We first show that such codes can decode with a simple bit-flipping decoder any pattern of $O\left(\frac{\sqrt{n} \log \log n}{\log n}\right)$ errors. This avoids the previous attack at the cost of significantly increasing the key size of the scheme. We then show that under a very reasonable assumption the decoding failure probability decays almost exponentially with the codelength with just two iterations of bit-flipping. With an additional assumption it has even been proved that it decays exponentially with an unbounded number of iterations and we show that in this case the increase of the key size which is required for resisting to the attack of \cite{GJS16} is only moderate.

## LDPC Codes over Gaussian Multiple Access Wiretap Channel

- **Status**: ❌
- **Reason**: GMAC 도청채널 보안코딩; LDPC puncturing+EXIT 최적화는 무선 보안 응용 특이적이고 떼어낼 NAND ECC 기법 없음
- **ID**: arxiv:1801.04420v2
- **Type**: preprint
- **Published**: 2018-01-13
- **Authors**: Sahar Shahbaz, Bahareh Akhbari, Reza Asvadi
- **PDF**: https://arxiv.org/pdf/1801.04420v2
- **Abstract**: We study the problem of two-user Gaussian multiple access channel (GMAC) in the presence of an external eavesdropper. In this problem, an eavesdropper receives a signal with a lower signal-to-noise ratio (SNR) compared to the legitimate receiver and all transmitted messages should be kept confidential against the eavesdropper. For this purpose, we propose a secure coding scheme on this channel which utilizes low-density parity-check (LDPC) codes by employing random bit insertion and puncturing techniques. At each encoder, the confidential message with some random bits as a random message are systematically encoded, and then the associated bits to the confidential message are punctured. Next, the encoders send their unpunctured bits over a Gaussian multiple access wiretap channel (GMAC-WT). The puncturing distribution applied to the LDPC code is considered in two cases: random and optimized. We utilize a modified extrinsic information transfer (EXIT) chart analysis to optimize the puncturing distribution for each encoder. The security gap is used as a measure of secrecy for the sent messages over GMAC-WT which should be made as small as possible. We compare the achieved secure rate pair with an achievable secrecy rate region of GMAC-WT to show the effective performance of the proposed scheme. In this paper, equal and unequal power conditions at the transmitters are investigated. For both cases, we attain a fairly small security gap which is equivalent to achieve the points near the secrecy rate region of GMAC-WT.
