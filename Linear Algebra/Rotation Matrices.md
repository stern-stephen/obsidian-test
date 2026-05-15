# Rotation Matrices

## Overview

A **rotation matrix** represents a rotation of space around the origin.

Rotation matrices preserve lengths and angles, so they are examples of length-preserving linear transformations.

In real vector spaces, rotation matrices are **orthogonal matrices** with determinant $1$:

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

Applying this matrix rotates every vector by the same angle $\theta$ without changing its length.

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

A two-dimensional rotation matrix usually has complex [Eigenvalues](Eigenvalues.md):

$$
\lambda = e^{i\theta}
\quad \text{and} \quad
\lambda = e^{-i\theta}
$$

These eigenvalues have absolute value $1$, which matches the fact that rotations preserve length.

In three dimensions, a rotation around an axis has eigenvalue $1$ in the direction of the rotation axis.

## Connection To Unitary Matrices

Real rotation matrices are closely related to [Unitary Matrices](Unitary%20Matrices.md).

A real rotation matrix satisfies:

$$
R^T R = I
$$

A complex unitary matrix satisfies:

$$
U^\dagger U = I
$$

So unitary matrices are the complex analogue of real orthogonal transformations, including rotations and reflections.

## Common Confusions

- A rotation matrix must preserve length. A matrix that only spins some vectors but stretches others is not a pure rotation.
- An orthogonal matrix can be a rotation or a reflection. The determinant separates them: determinant $1$ gives rotations, while determinant $-1$ gives reflections.
- In $\mathbb{R}^2$, most nontrivial rotations do not have real eigenvectors.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vectors](Vectors.md)
- [Eigenvalues](Eigenvalues.md)
- [Unitary Matrices](Unitary%20Matrices.md)
- [Adjoints](Adjoints.md)
