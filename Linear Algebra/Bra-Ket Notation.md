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
{"source":"Bra-Ket Notation","relation":"REPRESENTS","target":"Vectors","evidence_heading":"Kets","evidence_summary":"The note says a ket is usually thought of as a column vector and can represent a quantum state.","confidence":0.9}
{"source":"Bra-Ket Notation","relation":"REPRESENTS","target":"Dual Vectors","evidence_heading":"Bras","evidence_summary":"The note says a bra is the adjoint of a ket, corresponding to a conjugate-transposed row vector.","confidence":0.9}
{"source":"Bra-Ket Notation","relation":"REPRESENTS","target":"Inner Products","evidence_heading":"Inner Products","evidence_summary":"The note says the expression bra phi ket psi means the inner product of the two kets.","confidence":0.9}
{"source":"Hermitian Operators","relation":"DETERMINES","target":"Real Expectation Values","evidence_heading":"Operators","evidence_summary":"The note says expectation values written as bra psi A ket psi are real when A is Hermitian.","confidence":0.9}
-->
