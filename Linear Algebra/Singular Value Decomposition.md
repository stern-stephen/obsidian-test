# Singular Value Decomposition

## Overview

The **singular value decomposition**, or **SVD**, rewrites a matrix as a product of three simpler matrices:

$$
A = U \Sigma V^\dagger
$$

where $U$ and $V$ are unitary matrices, and $\Sigma$ is a diagonal or rectangular diagonal matrix whose diagonal entries are nonnegative real numbers.

SVD is useful because it works for any matrix, even when the matrix is not square or not diagonalizable. It separates a linear transformation into a change of orthonormal coordinates, a scaling along perpendicular directions, and another change of orthonormal coordinates.

## Definition

If $A$ is an $m \times n$ complex matrix, then an SVD of $A$ is:

$$
A = U \Sigma V^\dagger
$$

with:

- $U$ an $m \times m$ unitary matrix.
- $V$ an $n \times n$ unitary matrix.
- $\Sigma$ an $m \times n$ matrix whose only nonzero entries lie on the main diagonal.
- The diagonal entries $\sigma_1, \sigma_2, \ldots$ are nonnegative and are called the **singular values** of $A$.

Usually the singular values are ordered from largest to smallest:

$$
\sigma_1 \ge \sigma_2 \ge \cdots \ge 0
$$

For real matrices, $U$ and $V$ can be chosen to be orthogonal matrices, and $V^\dagger$ becomes the ordinary transpose $V^T$.

## Geometric Meaning

The SVD describes the action of $A$ in three stages:

$$
x \mapsto V^\dagger x \mapsto \Sigma V^\dagger x \mapsto U \Sigma V^\dagger x
$$

The matrix $V^\dagger$ rotates or reflects the input coordinates into special directions. The matrix $\Sigma$ stretches or shrinks those directions by the singular values. The matrix $U$ rotates or reflects the result into the output space.

This means SVD turns a complicated linear transformation into:

- input directions,
- independent scalings,
- output directions.

## Connection To Eigenvalues

The singular values of $A$ are related to the [Eigenvalues](Eigenvalues.md) of the positive semidefinite matrices $A^\dagger A$ and $A A^\dagger$.

The right singular vectors are the eigenvectors of $A^\dagger A$:

$$
A^\dagger A v_i = \sigma_i^2 v_i
$$

The left singular vectors are the eigenvectors of $A A^\dagger$:

$$
A A^\dagger u_i = \sigma_i^2 u_i
$$

So each singular value is the square root of an eigenvalue of $A^\dagger A$:

$$
\sigma_i = \sqrt{\lambda_i}
$$

where $\lambda_i$ is an eigenvalue of $A^\dagger A$.

## Rank And Compression

The number of nonzero singular values equals the rank of $A$.

If only the largest $k$ singular values are kept, the SVD gives a low-rank approximation:

$$
A \approx \sum_{i=1}^k \sigma_i u_i v_i^\dagger
$$

This is useful in data compression, noise reduction, numerical linear algebra, and machine learning. Large singular values capture the strongest directions of the transformation, while small singular values often represent weaker structure or noise.

## Example

For a diagonal matrix with nonnegative entries:

$$
A =
\begin{bmatrix}
3 & 0 \\
0 & 1
\end{bmatrix}
$$

one possible SVD is:

$$
U = I,\quad
\Sigma =
\begin{bmatrix}
3 & 0 \\
0 & 1
\end{bmatrix},
\quad
V = I
$$

The singular values are $3$ and $1$. Geometrically, the matrix stretches one coordinate direction by $3$ and leaves the other unchanged.

## Difference From Diagonalization

Diagonalization writes a square matrix as:

$$
A = P D P^{-1}
$$

when $A$ has enough independent eigenvectors.

SVD writes any matrix as:

$$
A = U \Sigma V^\dagger
$$

The key differences are:

- Diagonalization is mainly for square matrices; SVD works for rectangular matrices too.
- Diagonalization may fail; SVD always exists.
- Diagonalization uses eigenvalues, which may be negative or complex; SVD uses nonnegative singular values.
- SVD uses orthonormal input and output directions, which makes it numerically stable and geometrically clean.

## Quantum Mechanics Connection

In quantum information, SVD helps explain decompositions of states and operators. The [Schmidt decomposition](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Schmidt%20Decomposition%20and%20Purifications.md) is closely related to SVD: it rewrites a bipartite quantum state using orthonormal bases and nonnegative coefficients.

SVD also complements [Unitary Matrices](Unitary%20Matrices.md) because it factors a general matrix into unitary transformations plus a nonnegative scaling matrix.

## Common Confusions

- Singular values are not the same as eigenvalues. They are always nonnegative, while eigenvalues may be negative or complex.
- The SVD is not unique. If singular values repeat, there can be many valid choices of singular vectors.
- $\Sigma$ is not always square. If $A$ is $m \times n$, then $\Sigma$ is also $m \times n$.
- A zero singular value means the matrix collapses at least one input direction.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Change of Basis](Change%20of%20Basis.md)
- [Adjoints](Adjoints.md)
- [Eigenvalues](Eigenvalues.md)
- [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md)
- [Unitary Matrices](Unitary%20Matrices.md)
- [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Gram-Schmidt](Gram-Schmidt.md)
