# Unitary Matrices

## Overview

A **unitary matrix** is a complex square matrix whose inverse is equal to its conjugate transpose.

For a matrix $U$, this means:

$$
U^\dagger U = U U^\dagger = I
$$

where $U^\dagger$ is the conjugate transpose of $U$, and $I$ is the identity matrix.

Unitary matrices are the complex-number version of **orthogonal matrices**. Orthogonal matrices preserve lengths and angles in real vector spaces; unitary matrices do the same thing in complex vector spaces.

The operation $U^\dagger$ is the [adjoint](Adjoints.md) of $U$.

## Definition

A square complex matrix $U$ is unitary when:

$$
U^{-1} = U^\dagger
$$

Equivalently:

$$
U^\dagger U = I
$$

This means the columns of $U$ form an **orthonormal basis**. Each column has length $1$, and different columns are orthogonal to each other.

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

Unitary matrices are important because they preserve the geometry of complex vector spaces.

- They preserve vector lengths.
- They preserve inner products.
- Their columns form an orthonormal basis.
- Their eigenvalues lie on the complex unit circle.
- The inverse of a unitary matrix is its conjugate transpose.
- Products of unitary matrices are unitary.

## Preserving Lengths And Inner Products

If $U$ is unitary, then applying $U$ to a vector does not change the vector's length.

For any vector $x$:

$$
\|Ux\| = \|x\|
$$

This follows from:

$$
\langle Ux, Ux \rangle = \langle x, U^\dagger Ux \rangle = \langle x, x \rangle
$$

Unitary matrices also preserve inner products. For any vectors $x$ and $y$:

$$
\langle Ux, Uy \rangle = \langle x, y \rangle
$$

This means unitary transformations preserve both lengths and angles.

## Eigenvalues

Unitary matrices have [Eigenvalues](Eigenvalues.md) that lie on the complex unit circle.

If $U$ is unitary and $Uv = \lambda v$ for a nonzero vector $v$, then:

$$
|\lambda| = 1
$$

This means unitary matrices may change direction or phase, but their eigenvalues cannot stretch or shrink eigenvectors. See [Eigenvalues: Unitary Matrices](Eigenvalues.md#Unitary%20Matrices) for more detail.

## Unitary Operators

A **unitary operator** is the abstract vector-space version of a unitary matrix.

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

The **Pauli matrices** are three important $2 \times 2$ matrices used in quantum mechanics:

$$
\sigma_x =
\begin{bmatrix}
0 & 1 \\
1 & 0
\end{bmatrix}
$$

$$
\sigma_y =
\begin{bmatrix}
0 & -i \\
i & 0
\end{bmatrix}
$$

$$
\sigma_z =
\begin{bmatrix}
1 & 0 \\
0 & -1
\end{bmatrix}
$$

Each Pauli matrix is both **Hermitian** and **unitary**:

$$
\sigma_k^\dagger = \sigma_k
$$

and:

$$
\sigma_k^\dagger \sigma_k = I
$$

for $k \in \{x, y, z\}$.

Because the Pauli matrices are Hermitian and unitary, their eigenvalues are:

$$
\lambda = \pm 1
$$

Since each Pauli matrix is Hermitian, each can be diagonalized by a unitary matrix:

$$
\sigma_k = U \Lambda U^\dagger
$$

where $U$ is built from orthonormal eigenvectors, and $\Lambda$ contains the eigenvalues $1$ and $-1$.

The detailed eigenvectors and diagonalizations are in [Eigenvalues: Pauli Matrices](Eigenvalues.md#Pauli%20Matrices).

The Pauli matrices are useful because they describe basic two-state quantum measurements, such as spin measurements along the $x$, $y$, and $z$ axes.

## Intuition

You can think of a unitary matrix as a rotation or reflection in a complex vector space.

It can change a vector's direction and phase, but it cannot change the vector's length. This makes unitary matrices the natural language for reversible transformations, especially in quantum mechanics.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Eigenvalues](Eigenvalues.md)
- [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)
