# Chapter 2 - Superdense Coding

Source: [[References/quantum-computation-and-quantum-information-nielsen-chuang.pdf]]

Book hub: [[Book Notes/Nielsen Chuang/Nielsen Chuang|Nielsen And Chuang]]

Parent chapter: [[Book Notes/Nielsen Chuang/Chapter 2 - Quantum Mechanics|Chapter 2 - Quantum Mechanics]]

Book section: 2.3, page 97.

## Overview

Superdense coding shows that shared entanglement can be used to transmit two classical bits by sending only one qubit.

This does not violate ordinary communication limits, because Alice and Bob must already share an entangled pair before the protocol begins.

## Setup

Alice and Bob start with the Bell state:

$$
\frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

Alice holds the first qubit and Bob holds the second.

Alice wants to send two classical bits:

$$
00,\ 01,\ 10,\ 11
$$

## Encoding

Alice encodes her two-bit message by applying one of four operations to her qubit.

These operations transform the shared state into one of four orthogonal Bell states.

Conceptually:

- $00$: do nothing.
- $01$: apply a phase flip.
- $10$: apply a bit flip.
- $11$: apply both a bit flip and a phase-related operation.

After this operation, Alice sends her one qubit to Bob.

## Decoding

Bob now has both qubits.

Because the four possible final states are orthogonal, Bob can distinguish them with a suitable measurement.

That measurement tells Bob which two-bit message Alice encoded.

## Why It Matters

Superdense coding is a compact example of quantum information behaving differently from classical information.

The transmitted qubit is not carrying two classical bits by itself. The extra power comes from the shared entanglement between Alice and Bob.

This protocol highlights a recurring theme in the book: entanglement is a resource.

## Related Concepts

- [[Quantum Computing/Quantum Computing|Quantum Computing]]
- [[Quantum Mechanics/Quantum Mechanics|Quantum Mechanics]]
- [[Book Notes/Nielsen Chuang/Chapter 2 - Postulates of Quantum Mechanics|Chapter 2 - Postulates Of Quantum Mechanics]]
- [[Linear Algebra/Unitary Matrices|Unitary Matrices]]
- [[Linear Algebra/Bra-Ket Notation|Bra-Ket Notation]]
