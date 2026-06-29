# Bra-Ket Notation

## Overview

**Bra-ket notation** is a compact notation for vectors, dual vectors, and inner products, especially in quantum mechanics.

A **ket** represents a vector:

$$
|\psi\rangle
$$

A **bra** represents the adjoint of a vector:

$$
\langle \psi|
$$

Together, a bra and a ket form an inner product:

$$
\langle \phi|\psi\rangle
$$

## Kets

A ket is usually thought of as a column vector.

For example:

$$
|\psi\rangle =
\begin{bmatrix}
\alpha \\
\beta
\end{bmatrix}
$$

In quantum mechanics, $|\psi\rangle$ can represent a quantum state.

## Bras

A bra is the adjoint of a ket.

If:

$$
|\psi\rangle =
\begin{bmatrix}
\alpha \\
\beta
\end{bmatrix}
$$

then:

$$
\langle \psi| =
\begin{bmatrix}
\overline{\alpha} & \overline{\beta}
\end{bmatrix}
$$

This is why [Adjoints](Adjoints.md) are central to bra-ket notation.

## Inner Products

The expression:

$$
\langle \phi|\psi\rangle
$$

means the inner product of $|\phi\rangle$ and $|\psi\rangle$.

If:

$$
|\phi\rangle =
\begin{bmatrix}
a \\
b
\end{bmatrix}
\quad
\text{and}
\quad
|\psi\rangle =
\begin{bmatrix}
c \\
d
\end{bmatrix}
$$

then:

$$
\langle \phi|\psi\rangle = \overline{a}c + \overline{b}d
$$

Two states are orthogonal when:

$$
\langle \phi|\psi\rangle = 0
$$

## Operators

An operator $A$ can act on a ket:

$$
A|\psi\rangle
$$

Expectation values are often written as:

$$
\langle \psi|A|\psi\rangle
$$

This represents the average measured value of the observable $A$ when the system is in state $|\psi\rangle$.

When $A$ is a [Hermitian operator](Hermitian%20Matrices%20and%20Operators.md), this expectation value is real.

## Related Concepts

- [Shankar: Dual Spaces and Dirac Notation](../Book%20Notes/Shankar/Chapter%201/Dual%20Spaces%20and%20Dirac%20Notation.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)

<!-- semantic-edges
{"source":"Bra-Ket Notation","relation":"PART_OF","target":"Linear Algebra","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Linear Algebra area of the vault.","confidence":0.85}
{"source":"Bra-Ket Notation","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Adjoints","evidence_heading":"Bras","evidence_summary":"The note explicitly connects Bra-Ket Notation with Adjoints in its discussion or related-note links.","confidence":0.75}
{"source":"Bra-Ket Notation","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Hermitian operator","evidence_heading":"Operators","evidence_summary":"The note explicitly connects Bra-Ket Notation with Hermitian operator in its discussion or related-note links.","confidence":0.75}
{"source":"Bra-Ket Notation","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Shankar: Dual Spaces and Dirac Notation","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Bra-Ket Notation with Shankar: Dual Spaces and Dirac Notation in its discussion or related-note links.","confidence":0.75}
{"source":"Bra-Ket Notation","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Vector Spaces","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Bra-Ket Notation with Vector Spaces in its discussion or related-note links.","confidence":0.75}
-->
