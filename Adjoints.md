# Adjoints

## Overview

The **adjoint** of a matrix or operator is the object that moves an operation from one side of an inner product to the other.

For a complex matrix $A$, the adjoint is written:

$$
A^\dagger
$$

It is formed by transposing the matrix and taking the complex conjugate of each entry.

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

The deeper definition of the adjoint comes from [[Vector Spaces]] with inner products.

An operator $T^\dagger$ is the adjoint of $T$ if:

$$
\langle Tx, y \rangle = \langle x, T^\dagger y \rangle
$$

for all vectors $x$ and $y$.

This equation says that applying $T$ to the first input of the inner product is equivalent to applying $T^\dagger$ to the second input.

## Why Adjoints Matter

Adjoints are the language behind several important matrix classes:

- A matrix is [[Hermitian Matrices and Operators|Hermitian]] when $A = A^\dagger$.
- A matrix is [[Unitary Matrices|unitary]] when $A^\dagger A = I$.
- A projection matrix is often characterized by being both Hermitian and idempotent.

They also explain why conjugate transpose, rather than ordinary transpose, is the natural operation in complex vector spaces.

## Bra-Ket Connection

In [[Bra-Ket Notation]], taking the adjoint turns a ket into a bra:

$$
|\psi\rangle^\dagger = \langle \psi|
$$

and turns a bra into a ket:

$$
\langle \psi|^\dagger = |\psi\rangle
$$

This is the same idea as turning a column vector into a conjugate-transposed row vector.

## Related Concepts

- [[Vector Spaces]]
- [[Bra-Ket Notation]]
- [[Hermitian Matrices and Operators]]
- [[Unitary Matrices]]
- [[Eigenvalues]]
