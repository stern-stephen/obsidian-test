# Four Fundamental Subspaces

## Overview

For an $m \times n$ matrix $A$, there are four important vector spaces attached to the matrix:

- The column space of $A$.
- The null space of $A$.
- The row space of $A$.
- The left null space of $A$.

Together, these are called the **four fundamental subspaces** of linear algebra.

They explain what a matrix does to vectors, which directions it can produce, and which directions it collapses.

## Column Space

The **column space** of $A$ is the span of the columns of $A$.

It is written:

$$
\operatorname{Col}(A)
$$

If $A$ is an $m \times n$ matrix, then:

$$
\operatorname{Col}(A) \subseteq \mathbb{R}^m
$$

or, for complex matrices:

$$
\operatorname{Col}(A) \subseteq \mathbb{C}^m
$$

The column space is the set of all possible outputs $Ax$.

For the system:

$$
Ax = b
$$

there is a solution exactly when $b$ lies in $\operatorname{Col}(A)$.

## Null Space

The **null space** of $A$ is the set of vectors sent to zero:

$$
\operatorname{Null}(A) = \{x : Ax = 0\}
$$

If $A$ is an $m \times n$ matrix, then:

$$
\operatorname{Null}(A) \subseteq \mathbb{R}^n
$$

or:

$$
\operatorname{Null}(A) \subseteq \mathbb{C}^n
$$

The null space describes the input directions that the matrix collapses.

## Row Space

The **row space** of $A$ is the span of the rows of $A$.

Equivalently, it is the column space of $A^\dagger$:

$$
\operatorname{Row}(A) = \operatorname{Col}(A^\dagger)
$$

For real matrices, $A^\dagger$ is just $A^T$.

If $A$ is an $m \times n$ matrix, then the row space lives in the input space:

$$
\operatorname{Row}(A) \subseteq \mathbb{R}^n
$$

or:

$$
\operatorname{Row}(A) \subseteq \mathbb{C}^n
$$

## Left Null Space

The **left null space** of $A$ is the null space of $A^\dagger$:

$$
\operatorname{Null}(A^\dagger) = \{y : A^\dagger y = 0\}
$$

For real matrices, this is:

$$
\operatorname{Null}(A^T)
$$

The left null space contains vectors perpendicular to every column of $A$.

## Dimensions

If $A$ is an $m \times n$ matrix with rank $r$, then:

$$
\dim \operatorname{Col}(A) = r
$$

$$
\dim \operatorname{Row}(A) = r
$$

$$
\dim \operatorname{Null}(A) = n - r
$$

$$
\dim \operatorname{Null}(A^\dagger) = m - r
$$

These dimension facts are part of the rank-nullity picture.

## Orthogonality

The four fundamental subspaces come in orthogonal pairs.

In the input space:

$$
\operatorname{Row}(A)^\perp = \operatorname{Null}(A)
$$

In the output space:

$$
\operatorname{Col}(A)^\perp = \operatorname{Null}(A^\dagger)
$$

This means the row space and null space split the input space, while the column space and left null space split the output space.

## Connection To Gaussian Elimination

[Gaussian Elimination](Gaussian%20Elimination.md) helps compute these spaces.

- Pivot columns in the original matrix give a basis for the column space.
- Nonzero rows in row echelon form give a basis for the row space.
- Free variables describe the null space.
- Applying the same ideas to $A^\dagger$ gives the left null space.

## Connection To SVD

The [Singular Value Decomposition](Singular%20Value%20Decomposition.md) gives an orthonormal view of the four subspaces.

Right singular vectors with nonzero singular values span the row space. Right singular vectors with zero singular values span the null space.

Left singular vectors with nonzero singular values span the column space. Left singular vectors with zero singular values span the left null space.

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Matrices](Matrices.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Gaussian Elimination](Gaussian%20Elimination.md)
- [Projection Matrices](Projection%20Matrices.md)
- [Singular Value Decomposition](Singular%20Value%20Decomposition.md)
- [Adjoints](Adjoints.md)
