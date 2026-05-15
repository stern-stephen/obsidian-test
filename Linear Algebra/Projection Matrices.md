# Projection Operators And Matrices

## Overview

A **projection operator** sends vectors onto a subspace.

If $P$ is a projection operator, then applying it twice has the same effect as applying it once:

$$
P^2 = P
$$

This property is called **idempotence**.

Geometrically, once a vector has already been projected onto a subspace, projecting it again does not move it.

## Orthogonal Projections

An **orthogonal projection** drops a vector onto a subspace at a right angle.

For an orthogonal projection operator $P$:

$$
P^2 = P
$$

and:

$$
P^\dagger = P
$$

So an orthogonal projection is both idempotent and [Hermitian](Hermitian%20Matrices%20and%20Operators.md).

For real matrix representations, this becomes:

$$
P^T = P
$$

## Projection Onto A Line

If $u$ is a nonzero vector, the projection of $x$ onto the line spanned by $u$ is:

$$
\operatorname{proj}_u(x) = \frac{u^\dagger x}{u^\dagger u}u
$$

The corresponding projection matrix is:

$$
P = \frac{u u^\dagger}{u^\dagger u}
$$

If $u$ has length $1$, then:

$$
P = u u^\dagger
$$

## Projection Onto A Subspace

If the columns of $Q$ form an orthonormal basis for a subspace, then the orthogonal projection onto that subspace is:

$$
P = Q Q^\dagger
$$

If the columns of $A$ are linearly independent but not necessarily orthonormal, then the projection onto the column space of $A$ is:

$$
P = A(A^\dagger A)^{-1}A^\dagger
$$

This formula appears often in least squares problems, where a vector is approximated by the closest vector in a subspace.

## Eigenvalues

Projection operators have simple [Eigenvalues](Eigenvalues.md).

If $P^2 = P$ and $Pv = \lambda v$, then:

$$
P^2v = \lambda^2 v
$$

But $P^2v = Pv = \lambda v$, so:

$$
\lambda^2 = \lambda
$$

Therefore:

$$
\lambda = 0
\quad \text{or} \quad
\lambda = 1
$$

Eigenvalue $1$ corresponds to directions kept by the projection. Eigenvalue $0$ corresponds to directions collapsed by the projection.

## Intuition

A projection operator separates a vector into two pieces:

$$
x = Px + (x - Px)
$$

The vector $Px$ lies in the target subspace. For an orthogonal projection, $x - Px$ is perpendicular to that subspace.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Eigenvalues](Eigenvalues.md)
- [Hermitian Matrices and Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md)
