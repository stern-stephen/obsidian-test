# Quantum State Vector

## Overview

A **quantum state vector** contains the information needed to predict the probabilities of future measurement outcomes.

In [bra-ket notation](../Linear%20Algebra/Bra-Ket%20Notation.md), a state vector is written as a ket:

$$
|\psi\rangle
$$

## Definition

For a two-state system such as spin-$1/2$, a general state can be expanded in the $S_z$ basis:

$$
|\psi\rangle = c_+|+z\rangle + c_-|-z\rangle
$$

The complex numbers $c_+$ and $c_-$ are probability amplitudes.

The measurement probabilities are:

$$
P(+z) = |c_+|^2
$$

and:

$$
P(-z) = |c_-|^2
$$

Normalization requires:

$$
|c_+|^2 + |c_-|^2 = 1
$$

## Intuition

The state vector is richer than a list of probabilities.

Two states can give the same probabilities for one measurement but different probabilities for another measurement. This happens because relative phases between amplitudes can affect later outcomes.

In a continuous position basis, the wavefunction is the position representation of the state vector:

$$
\psi(x)=\langle x|\psi\rangle
$$

The corresponding position probability density is:

$$
P(x)=|\psi(x)|^2
$$

## Related Book Notes

- [Shankar Chapter 3: Conclusions](../Book%20Notes/Shankar/Chapter%203/Conclusions.md)
- [Shankar Chapter 4: Discussion of Postulates I-III](../Book%20Notes/Shankar/Chapter%204/Discussion%20of%20Postulates%20I-III.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Stern-Gerlach Experiments](Stern-Gerlach%20Experiments.md)
- [Spin-1/2 Systems](Spin-1-2%20Systems.md)
- [Bra-Ket Notation](../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Vector Spaces](../Linear%20Algebra/Vector%20Spaces.md)
- [Townsend Chapter 1](../Book%20Notes/Townsend/Chapter%201/Stern-Gerlach%20Experiments.md)

<!-- semantic-edges
{"source":"Quantum State Vector","relation":"PART_OF","target":"Quantum Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Quantum Mechanics area of the vault.","confidence":0.85}
{"source":"Quantum State Vector","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"bra-ket notation","evidence_heading":"Overview","evidence_summary":"The note explicitly connects Quantum State Vector with bra-ket notation in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum State Vector","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Shankar Chapter 3: Conclusions","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Quantum State Vector with Shankar Chapter 3: Conclusions in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum State Vector","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Shankar Chapter 4: Discussion of Postulates I-III","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Quantum State Vector with Shankar Chapter 4: Discussion of Postulates I-III in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum State Vector","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Quantum State Vector with Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
-->
