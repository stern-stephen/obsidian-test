# Unitary Operators

## Overview

A **unitary operator** is a length-preserving linear operator on an inner product space.

For an operator $U$, this means:

$$
U^\dagger U = U U^\dagger = I
$$

where $U^\dagger$ is the adjoint of $U$, and $I$ is the identity operator.

When a unitary operator is written in a basis, its matrix is called a **unitary matrix**. Unitary matrices are the complex-number version of **orthogonal matrices**.

The operation $U^\dagger$ is the [adjoint](Adjoints.md) of $U$.

## Definition

A linear operator $U$ is unitary when:

$$
U^{-1} = U^\dagger
$$

Equivalently:

$$
U^\dagger U = I
$$

For a matrix representation, this means the columns of $U$ form an **orthonormal basis**. Each column has length $1$, and different columns are orthogonal to each other.

The [Gram-Schmidt](Gram-Schmidt.md) process is one way to construct orthonormal bases from linearly independent vectors.

## Example

The following matrix is unitary:

$$
U =
\frac{1}{\sqrt{2}}
\begin{bmatrix}
1 & 1 \\
1 & -1
\end{bmatrix}
$$

This is the Hadamard matrix used in quantum computing. It is unitary because:

$$
U^\dagger U = I
$$

Since this example is real-valued, $U^\dagger$ is the same as the ordinary transpose $U^T$.

## Key Properties

Unitary operators are important because they preserve the geometry of complex vector spaces.

- They preserve vector lengths.
- They preserve inner products.
- In matrix representations, their columns form an orthonormal basis.
- Their eigenvalues lie on the complex unit circle.
- The inverse of a unitary operator is its adjoint.
- Products of unitary operators are unitary.

## Preserving Lengths And Inner Products

If $U$ is unitary, then applying the operator $U$ to a vector does not change the vector's length.

For any vector $x$:

$$
\|Ux\| = \|x\|
$$

This follows from:

$$
\langle Ux, Ux \rangle = \langle x, U^\dagger Ux \rangle = \langle x, x \rangle
$$

Unitary operators also preserve inner products. For any vectors $x$ and $y$:

$$
\langle Ux, Uy \rangle = \langle x, y \rangle
$$

This means unitary operators preserve both lengths and angles.

## Eigenvalues

Unitary operators have [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md) that lie on the complex unit circle.

If $U$ is unitary and $Uv = \lambda v$ for a nonzero vector $v$, then:

$$
|\lambda| = 1
$$

Here is why.

Because $U$ is unitary, it preserves vector lengths:

$$
\|Uv\| = \|v\|
$$

But $v$ is an eigenvector, so $Uv = \lambda v$. Substituting this into the left side gives:

$$
\|\lambda v\| = \|v\|
$$

Pulling the scalar $\lambda$ out of the norm:

$$
|\lambda| \|v\| = \|v\|
$$

Since eigenvectors are nonzero, $\|v\| \ne 0$. Dividing both sides by $\|v\|$ gives:

$$
|\lambda| = 1
$$

This means unitary operators may change direction or phase, but their eigenvalues cannot stretch or shrink eigenvectors.

Examples of possible unitary eigenvalues include:

- $1$
- $-1$
- $i$
- $e^{i\theta}$

## Operator Definition

An operator $T$ on an inner product space is unitary if:

$$
\langle Tx, Ty \rangle = \langle x, y \rangle
$$

for all vectors $x$ and $y$ in the space.

Equivalently, a unitary operator satisfies:

$$
T^\dagger T = T T^\dagger = I
$$

This means a unitary operator is reversible, and its inverse is its adjoint:

$$
T^{-1} = T^\dagger
$$

## Connection To Quantum Mechanics

In quantum mechanics, unitary operators describe how quantum states evolve over time.

Quantum states must keep total probability equal to $1$. Since unitary operators preserve vector length, they preserve this normalization.

If $|\psi\rangle$ is a quantum state and $U$ is unitary, then:

$$
|\psi'\rangle = U|\psi\rangle
$$

is another valid quantum state with the same total probability.

## Pauli Matrices

The [Pauli Matrices](Pauli%20Matrices.md) are important examples of operators whose matrix representations are both Hermitian and unitary.

Because they are unitary, their eigenvalues have absolute value $1$. Because they are Hermitian, their eigenvalues are real. Their definitions, eigenvectors, and diagonalizations are collected in [Pauli Matrices](Pauli%20Matrices.md).

## Intuition

You can think of a unitary operator as a rotation or reflection in a complex vector space.

It can change a vector's direction and phase, but it cannot change the vector's length. This makes unitary operators the natural language for reversible transformations, especially in quantum mechanics.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Pauli Matrices](Pauli%20Matrices.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
