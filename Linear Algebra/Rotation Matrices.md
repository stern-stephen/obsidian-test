# Rotation Operators

## Overview

A **rotation operator** represents a rotation of space around the origin.

Rotation operators preserve lengths and angles, so they are examples of length-preserving linear operators.

In an orthonormal basis for a real vector space, rotation operators are represented by **orthogonal matrices** with determinant $1$:

$$
R^T R = I
$$

and:

$$
\det(R) = 1
$$

The condition $R^T R = I$ says that $R^{-1} = R^T$.

## Two-Dimensional Rotation

In $\mathbb{R}^2$, a counterclockwise rotation by angle $\theta$ is:

$$
R(\theta) =
\begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta
\end{bmatrix}
$$

Applying this operator rotates every vector by the same angle $\theta$ without changing its length.

For example:

$$
R(\theta)
\begin{bmatrix}
1 \\
0
\end{bmatrix}
=
\begin{bmatrix}
\cos \theta \\
\sin \theta
\end{bmatrix}
$$

## Three-Dimensional Rotations

In $\mathbb{R}^3$, rotations can happen around an axis.

A rotation around the $z$-axis is:

$$
R_z(\theta) =
\begin{bmatrix}
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

The $z$-coordinate stays fixed, while the $x$-$y$ plane rotates.

## Eigenvalues

A two-dimensional rotation operator usually has complex [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md):

$$
\lambda = e^{i\theta} \quad \text{and} \quad \lambda = e^{-i\theta}
$$

These eigenvalues have absolute value $1$, which matches the fact that rotations preserve length.

In three dimensions, a rotation around an axis has eigenvalue $1$ in the direction of the rotation axis.

## Connection To Unitary Operators

Real rotation operators are closely related to [Unitary Operators](Unitary%20Matrices.md).

A real rotation matrix representation satisfies:

$$
R^T R = I
$$

A complex unitary operator satisfies:

$$
U^\dagger U = I
$$

So unitary operators are the complex analogue of real orthogonal transformations, including rotations and reflections.

## Common Confusions

- A rotation operator must preserve length. An operator that only spins some vectors but stretches others is not a pure rotation.
- An orthogonal matrix can be a rotation or a reflection. The determinant separates them: determinant $1$ gives rotations, while determinant $-1$ gives reflections.
- In $\mathbb{R}^2$, most nontrivial rotations do not have real eigenvectors.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vectors](Vectors.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Adjoints](Adjoints.md)

<!-- semantic-edges
{"source":"Rotation Operators","relation":"PART_OF","target":"Linear Algebra","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Linear Algebra area of the vault.","confidence":0.85}
{"source":"Rotation Operators","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Eigenvalues and Eigenvectors","evidence_heading":"Eigenvalues","evidence_summary":"The note explicitly connects Rotation Operators with Eigenvalues and Eigenvectors in its discussion or related-note links.","confidence":0.75}
{"source":"Rotation Operators","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Unitary Operators","evidence_heading":"Connection To Unitary Operators","evidence_summary":"The note explicitly connects Rotation Operators with Unitary Operators in its discussion or related-note links.","confidence":0.75}
{"source":"Rotation Operators","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Linear Algebra","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Rotation Operators with Linear Algebra in its discussion or related-note links.","confidence":0.75}
{"source":"Rotation Operators","relation":"LINEAR_ALGEBRA_RELATED_TO","target":"Matrices","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Rotation Operators with Matrices in its discussion or related-note links.","confidence":0.75}
-->
