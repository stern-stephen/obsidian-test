# Eigenvalues And Eigenvectors

## Overview

An **eigenvector** of a linear operator is a nonzero vector whose direction is preserved by the operator.

If $A$ is a linear operator, $v$ is a nonzero vector, and $\lambda$ is a scalar, then $v$ is an eigenvector of $A$ with eigenvalue $\lambda$ when:

$$
A v = \lambda v
$$

The operator $A$ may stretch, shrink, flip, or rotate other vectors, but on an eigenvector it acts like simple scalar multiplication.

## Meaning

The eigenvalue $\lambda$ tells how the eigenvector changes:

- If $\lambda > 1$, the vector is stretched.
- If $0 < \lambda < 1$, the vector is shrunk.
- If $\lambda = 1$, the vector is unchanged.
- If $\lambda = -1$, the vector is flipped.
- If $\lambda$ is complex, the transformation may include a phase change or rotation.

Eigenvalues and eigenvectors reveal the special directions where a linear operator has its simplest behavior.

## Finding Eigenvectors

After an eigenvalue $\lambda$ is known, its eigenvectors are found by solving:

$$
(A - \lambda I)v = 0
$$

The nonzero solutions form the **eigenspace** for $\lambda$.

For example, if $\lambda = 1$, then the eigenspace consists of the nonzero vectors satisfying:

$$
Av = v
$$

These are the directions that the operator leaves unchanged.

## Finding Eigenvalues

To find eigenvalues, rewrite the eigenvalue equation:

$$
A v = \lambda v
$$

as:

$$
(A - \lambda I)v = 0
$$

When $A$ is represented by a finite-dimensional matrix, this equation has a nonzero solution $v$ only when $A - \lambda I$ is singular:

$$
\det(A - \lambda I) = 0
$$

This determinant equation is called the **characteristic equation**.

## Diagonalization

An operator is **diagonalizable** when it has enough linearly independent eigenvectors to form a basis.

If $A$ has eigenvectors $v_1, v_2, \ldots, v_n$ with eigenvalues $\lambda_1, \lambda_2, \ldots, \lambda_n$, then:

$$
A = P D P^{-1}
$$

In matrix form, $P$ is the matrix whose columns are the eigenvectors, and $D$ is a diagonal matrix containing the eigenvalues:

$$
D =
\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

Diagonalization is useful because it finds a basis where the operator has a diagonal matrix representation, which is much easier to understand and compute with.

## Pauli Matrices

The [Pauli Matrices](Pauli%20Matrices.md) are a central example of eigenvalues in quantum mechanics. They are Hermitian and unitary, so their eigenvalues are forced to be:

$$
\lambda = \pm 1
$$

Their eigenvectors and diagonalizations are collected in [Pauli Matrices](Pauli%20Matrices.md).

## Related Concepts

- [Shankar: The Eigenvalue Problem](../Book%20Notes/Shankar/Chapter%201/The%20Eigenvalue%20Problem.md)
- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Linear Operators](Linear%20Operators.md)
- [Adjoints](Adjoints.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Pauli Matrices](Pauli%20Matrices.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)

<!-- semantic-edges
{"source":"Eigenvalues And Eigenvectors","relation":"PART_OF","target":"Linear Algebra","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Linear Algebra area of the vault.","confidence":0.85}
{"source":"Eigenvalues And Eigenvectors","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Pauli Matrices","evidence_heading":"Pauli Matrices","evidence_summary":"The note explicitly connects Eigenvalues And Eigenvectors with Pauli Matrices in its discussion or related-note links.","confidence":0.75}
{"source":"Eigenvalues And Eigenvectors","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Shankar: The Eigenvalue Problem","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Eigenvalues And Eigenvectors with Shankar: The Eigenvalue Problem in its discussion or related-note links.","confidence":0.75}
{"source":"Eigenvalues And Eigenvectors","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Linear Algebra","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Eigenvalues And Eigenvectors with Linear Algebra in its discussion or related-note links.","confidence":0.75}
{"source":"Eigenvalues And Eigenvectors","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Vector Spaces","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Eigenvalues And Eigenvectors with Vector Spaces in its discussion or related-note links.","confidence":0.75}
-->
