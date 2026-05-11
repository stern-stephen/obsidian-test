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
\langle \phi|\psi\rangle =
\overline{a}c + \overline{b}d
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

- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Matrices](Unitary%20Matrices.md)
- [Eigenvalues](Eigenvalues.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
