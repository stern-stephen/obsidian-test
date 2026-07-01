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
{"source":"Eigenvectors","relation":"SPECIALIZES","target":"Vectors","evidence_heading":"Overview","evidence_summary":"The note defines an eigenvector as a nonzero vector whose direction is preserved by a linear operator.","confidence":0.9}
{"source":"Eigenvalues","relation":"DETERMINES","target":"Eigenvector Scaling","evidence_heading":"Meaning","evidence_summary":"The note says the eigenvalue tells how the eigenvector is stretched, shrunk, flipped, phase-shifted, or rotated.","confidence":0.9}
{"source":"Eigenspaces","relation":"DETERMINES","target":"Eigenvectors","evidence_heading":"Finding Eigenvectors","evidence_summary":"The note says the nonzero solutions of (A - lambda I)v = 0 form the eigenspace for lambda.","confidence":0.9}
{"source":"Characteristic Equation","relation":"DETERMINES","target":"Eigenvalues","evidence_heading":"Finding Eigenvalues","evidence_summary":"The note says eigenvalues of a finite-dimensional matrix are found from det(A - lambda I) = 0.","confidence":0.9}
{"source":"Diagonalization","relation":"REQUIRES","target":"Eigenbasis","evidence_heading":"Diagonalization","evidence_summary":"The note says an operator is diagonalizable when it has enough linearly independent eigenvectors to form a basis.","confidence":0.95}
{"source":"Diagonalization","relation":"REFORMULATES","target":"Linear Operators","evidence_heading":"Diagonalization","evidence_summary":"The note says diagonalization finds a basis where the operator has a diagonal matrix representation and acts by simple scaling.","confidence":0.9}
-->
