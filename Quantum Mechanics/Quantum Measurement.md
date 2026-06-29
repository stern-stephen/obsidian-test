# Quantum Measurement

## Overview

Quantum measurement connects the abstract state vector to observable outcomes. Unlike closed-system evolution, measurement is generally probabilistic and can change the state.

## Measurement Operators

A general measurement is described by measurement operators $\lbrace M_m\rbrace$, where $m$ labels the possible outcomes.

For a state $|\psi\rangle$, the probability of outcome $m$ is:

$$
p(m)=\langle \psi|M_m^\dagger M_m|\psi\rangle
$$

After observing outcome $m$, the state becomes:

$$
\frac{M_m|\psi\rangle}{\sqrt{p(m)}}
$$

The measurement operators satisfy:

$$
\sum_m M_m^\dagger M_m = I
$$

This guarantees that the probabilities of all outcomes add to $1$.

## Projective Measurements

Projective measurements use projection operators $P_m$ satisfying:

$$
P_mP_n=\delta_{mn}P_m
$$

and:

$$
\sum_m P_m=I
$$

The probability of outcome $m$ is:

$$
p(m)=\langle \psi|P_m|\psi\rangle
$$

Projective measurements are closely tied to Hermitian operators: the possible measurement outcomes are eigenvalues, and the projectors pick out the corresponding eigenspaces.

## Collapse Of The State Vector

Collapse is the measurement-update rule for a quantum state after a particular outcome is observed.

Suppose an observable $\Omega$ has eigenstates $|\omega_n\rangle$, and the state before measurement is:

$$
|\psi\rangle=\sum_n c_n|\omega_n\rangle
$$

The state is not saying that one hidden outcome has already been selected and the measurement merely reveals it. It is a superposition whose amplitudes determine the probabilities for possible outcomes.

If the measured value is $\omega_k$, the probability of that result is:

$$
P(\omega_k)=|c_k|^2
$$

After the result is obtained, the state used for later predictions is replaced by the corresponding eigenstate:

$$
|\psi\rangle \rightarrow |\omega_k\rangle
$$

For degenerate outcomes, the state is projected into the whole eigenspace associated with the observed eigenvalue. If $P_k$ is the projector onto that eigenspace, the normalized post-measurement state is:

$$
|\psi'\rangle=\frac{P_k|\psi\rangle}{\sqrt{\langle \psi|P_k|\psi\rangle}}
$$

This is different from ordinary Schrodinger evolution. Schrodinger evolution is deterministic and unitary; collapse is probabilistic and depends on the measurement outcome. Operationally, collapse means the measurement has prepared a new state, so future measurements must be predicted from that new state.

The repeatability of projective measurement follows from collapse. If a measurement of $\Omega$ gives $\omega_k$ and the same measurement is repeated immediately, the second measurement gives $\omega_k$ again, because the first measurement prepared the state in the $\omega_k$ eigenspace.

## Disturbance And Resolution

A gentle measurement is not automatically a precise measurement. In a position measurement, one may reduce the momentum kick by using a low-momentum, long-wavelength probe, but that also makes the position resolution poor. To localize the particle sharply, the post-measurement state must be narrow in position, which makes its momentum spread large.

This is why "small disturbance in momentum" does not imply simultaneous sharp knowledge of position and momentum. The relevant tradeoff is:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

## POVMs

A POVM focuses on outcome probabilities. Its elements are:

$$
E_m=M_m^\dagger M_m
$$

with:

$$
\sum_m E_m=I
$$

The probability rule is:

$$
p(m)=\langle \psi|E_m|\psi\rangle
$$

POVMs are useful when the probabilities matter more than the post-measurement state.

## Related Book Notes

- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md#223-quantum-measurement)
- [Townsend: Stern-Gerlach Experiments](../Book%20Notes/Townsend/Chapter%201/Stern-Gerlach%20Experiments.md)
- [Shankar Chapter 4: Discussion of Postulates I-III](../Book%20Notes/Shankar/Chapter%204/Discussion%20of%20Postulates%20I-III.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum State Vector](Quantum%20State%20Vector.md)
- [Stern-Gerlach Experiments](Stern-Gerlach%20Experiments.md)
- [Projection Operators](../Linear%20Algebra/Projection%20Matrices.md)
- [Hermitian Operators](../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Density Operators](Density%20Operators.md)

<!-- semantic-edges
{"source":"Quantum Measurement","relation":"PART_OF","target":"Quantum Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Quantum Mechanics area of the vault.","confidence":0.85}
{"source":"Quantum Measurement","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Nielsen and Chuang: Postulates of Quantum Mechanics","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Quantum Measurement with Nielsen and Chuang: Postulates of Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum Measurement","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Townsend: Stern-Gerlach Experiments","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Quantum Measurement with Townsend: Stern-Gerlach Experiments in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum Measurement","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Shankar Chapter 4: Discussion of Postulates I-III","evidence_heading":"Related Book Notes","evidence_summary":"The note explicitly connects Quantum Measurement with Shankar Chapter 4: Discussion of Postulates I-III in its discussion or related-note links.","confidence":0.75}
{"source":"Quantum Measurement","relation":"QUANTUM_MECHANICS_RELATED_TO","target":"Quantum Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Quantum Measurement with Quantum Mechanics in its discussion or related-note links.","confidence":0.75}
-->
