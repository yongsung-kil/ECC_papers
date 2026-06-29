# arXiv — 2010-01


## VLSI Architectures for WIMAX Channel Decoders

- **Status**: ❌
- **Reason**: WiMax 채널디코더 VLSI 챕터로 conv/turbo 중심·LDPC 부수 언급, 새 LDPC 디코더 HW 기여 불명확
- **ID**: arxiv:1001.4694v1
- **Type**: preprint
- **Published**: 2010-01-26
- **Authors**: Maurizio Martina, Guido Masera
- **PDF**: https://arxiv.org/pdf/1001.4694v1
- **Abstract**: This chapter describes the main architectures proposed in the literature to implement the channel decoders required by the WiMax standard, namely convolutional codes, turbo codes (both block and convolutional) and LDPC. Then it shows a complete design of a convolutional turbo code encoder/decoder system for WiMax.

## Dirty Paper Coding using Sign-bit Shaping and LDPC Codes

- **Status**: ❌
- **Reason**: dirty paper coding/sign-bit shaping의 무선 응용 특이적, LDPC는 채널코딩 베이스라인일뿐 떼어낼 ECC 기법 없음
- **ID**: arxiv:1001.3476v1
- **Type**: preprint
- **Published**: 2010-01-20
- **Authors**: G Shilpa, Andrew Thangaraj, Srikrishna Bhashyam
- **PDF**: https://arxiv.org/pdf/1001.3476v1
- **Abstract**: Dirty paper coding (DPC) refers to methods for pre-subtraction of known interference at the transmitter of a multiuser communication system. There are numerous applications for DPC, including coding for broadcast channels. Recently, lattice-based coding techniques have provided several designs for DPC. In lattice-based DPC, there are two codes - a convolutional code that defines a lattice used for shaping and an error correction code used for channel coding. Several specific designs have been reported in the recent literature using convolutional and graph-based codes for capacity-approaching shaping and coding gains. In most of the reported designs, either the encoder works on a joint trellis of shaping and channel codes or the decoder requires iterations between the shaping and channel decoders. This results in high complexity of implementation. In this work, we present a lattice-based DPC scheme that provides good shaping and coding gains with moderate complexity at both the encoder and the decoder. We use a convolutional code for sign-bit shaping, and a low-density parity check (LDPC) code for channel coding. The crucial idea is the introduction of a one-codeword delay and careful parsing of the bits at the transmitter, which enable an LDPC decoder to be run first at the receiver. This provides gains without the need for iterations between the shaping and channel decoders. Simulation results confirm that at high rates the proposed DPC method performs close to capacity with moderate complexity. As an application of the proposed DPC method, we show a design for superposition coding that provides rates better than time-sharing over a Gaussian broadcast channel.

## Source Coding With Side Information Using List Decoding

- **Status**: ❌
- **Reason**: 소스코딩(SCSI) + list decoding으로 RS/BCH/Reed-Muller 설계; 채널 ECC 아니고 비-LDPC 부호, 떼어낼 LDPC 기법 없음
- **ID**: arxiv:1001.2805v1
- **Type**: preprint
- **Published**: 2010-01-16
- **Authors**: Mortuza Ali, Margreta Kuijper
- **PDF**: https://arxiv.org/pdf/1001.2805v1
- **Abstract**: The problem of source coding with side information (SCSI) is closely related to channel coding. Therefore, existing literature focuses on using the most successful channel codes namely, LDPC codes, turbo codes, and their variants, to solve this problem assuming classical unique decoding of the underlying channel code. In this paper, in contrast to classical decoding, we have taken the list decoding approach. We show that syndrome source coding using list decoding can achieve the theoretical limit. We argue that, as opposed to channel coding, the correct sequence from the list produced by the list decoder can effectively be recovered in case of SCSI, since we are dealing with a virtual noisy channel rather than a real noisy channel. Finally, we present a guideline for designing constructive SCSI schemes using Reed Solomon code, BCH code, and Reed-Muller code, which are the known list-decodable codes.
