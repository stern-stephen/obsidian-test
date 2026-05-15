# Adjoints

## Overview

The **adjoint** of an operator is the object that moves the operator from one side of an inner product to the other.

For an operator $A$, the adjoint is written:

$$
A^\dagger
$$

When the operator is represented by a complex matrix, the adjoint matrix is formed by transposing the matrix and taking the complex conjugate of each entry.

## Matrix Adjoint

If:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

then:

$$
A^\dagger =
\begin{bmatrix}
\overline{a} & \overline{c} \\
\overline{b} & \overline{d}
\end{bmatrix}
$$

For real matrices, the adjoint is just the ordinary transpose:

$$
A^\dagger = A^T
$$

## Inner Product Definition

The deeper definition of the adjoint comes from [Vector Spaces](Vector%20Spaces.md) with inner products.

An operator $T^\dagger$ is the adjoint of $T$ if:

$$
\langle Tx, y \rangle = \langle x, T^\dagger y \rangle
$$

for all vectors $x$ and $y$.

This equation says that applying $T$ to the first input of the inner product is equivalent to applying $T^\dagger$ to the second input.

## Why Adjoints Matter

Adjoints are the language behind several important operator classes:

- An operator is [Hermitian](Hermitian%20Matrices%20and%20Operators.md) when $A = A^\dagger$.
- An operator is [unitary](Unitary%20Matrices.md) when $A^\dagger A = I$.
- An orthogonal projection operator is often characterized by being both Hermitian and idempotent.

They also explain why conjugate transpose, rather than ordinary transpose, is the natural operation in complex vector spaces.

## Bra-Ket Connection

In [Bra-Ket Notation](Bra-Ket%20Notation.md), taking the adjoint turns a ket into a bra:

$$
|\psi\rangle^\dagger = \langle \psi|
$$

and turns a bra into a ket:

$$
\langle \psi|^\dagger = |\psi\rangle
$$

This is the same idea as turning a column vector into a conjugate-transposed row vector.

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Linear Operators](Linear%20Operators.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
