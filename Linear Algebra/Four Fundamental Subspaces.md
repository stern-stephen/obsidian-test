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
\mathrm{Col}(A)
$$

If $A$ is an $m \times n$ matrix, then:

$$
\mathrm{Col}(A) \subseteq \mathbb{R}^m
$$

or, for complex matrices:

$$
\mathrm{Col}(A) \subseteq \mathbb{C}^m
$$

The column space is the set of all possible outputs $Ax$.

For the system:

$$
Ax = b
$$

there is a solution exactly when $b$ lies in $\mathrm{Col}(A)$.

## Null Space

The **null space** of $A$ is the set of vectors sent to zero:

$$
\mathrm{Null}(A) = \lbrace x : Ax = 0\rbrace
$$

If $A$ is an $m \times n$ matrix, then:

$$
\mathrm{Null}(A) \subseteq \mathbb{R}^n
$$

or:

$$
\mathrm{Null}(A) \subseteq \mathbb{C}^n
$$

The null space describes the input directions that the matrix collapses.

## Row Space

The **row space** of $A$ is the span of the rows of $A$.

Equivalently, it is the column space of $A^\dagger$:

$$
\mathrm{Row}(A) = \mathrm{Col}(A^\dagger)
$$

For real matrices, $A^\dagger$ is just $A^T$.

If $A$ is an $m \times n$ matrix, then the row space lives in the input space:

$$
\mathrm{Row}(A) \subseteq \mathbb{R}^n
$$

or:

$$
\mathrm{Row}(A) \subseteq \mathbb{C}^n
$$

## Left Null Space

The **left null space** of $A$ is the null space of $A^\dagger$:

$$
\mathrm{Null}(A^\dagger) = \lbrace y : A^\dagger y = 0\rbrace
$$

For real matrices, this is:

$$
\mathrm{Null}(A^T)
$$

The left null space contains vectors perpendicular to every column of $A$.

## Dimensions

If $A$ is an $m \times n$ matrix with rank $r$, then:

$$
\dim \mathrm{Col}(A) = r
$$

$$
\dim \mathrm{Row}(A) = r
$$

$$
\dim \mathrm{Null}(A) = n - r
$$

$$
\dim \mathrm{Null}(A^\dagger) = m - r
$$

These dimension facts are part of the rank-nullity picture.

## Orthogonality

The four fundamental subspaces come in orthogonal pairs.

In the input space:

$$
\mathrm{Row}(A)^\perp = \mathrm{Null}(A)
$$

In the output space:

$$
\mathrm{Col}(A)^\perp = \mathrm{Null}(A^\dagger)
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
- [Projection Operators](Projection%20Matrices.md)
- [Singular Value Decomposition](Singular%20Value%20Decomposition.md)
- [Adjoints](Adjoints.md)

<!-- semantic-edges
{"source":"Four Fundamental Subspaces","relation":"DETERMINES","target":"Matrix Action","evidence_heading":"Overview","evidence_summary":"The note says the four fundamental subspaces explain what a matrix does to vectors, which directions it can produce, and which directions it collapses.","confidence":0.9}
{"source":"Column Space","relation":"REPRESENTS","target":"Possible Outputs","evidence_heading":"Column Space","evidence_summary":"The note defines the column space as the set of all possible outputs Ax.","confidence":0.95}
{"source":"Null Space","relation":"REPRESENTS","target":"Collapsed Input Directions","evidence_heading":"Null Space","evidence_summary":"The note says the null space describes input directions that the matrix collapses to zero.","confidence":0.95}
{"source":"Rank","relation":"DETERMINES","target":"Subspace Dimensions","evidence_heading":"Dimensions","evidence_summary":"The note gives dimensions of the column space, row space, null space, and left null space in terms of matrix rank.","confidence":0.9}
{"source":"Four Fundamental Subspaces","relation":"REQUIRES","target":"Orthogonality","evidence_heading":"Orthogonality","evidence_summary":"The note says the row space and null space, and the column space and left null space, come in orthogonal pairs.","confidence":0.9}
{"source":"Singular Value Decomposition","relation":"REFORMULATES","target":"Four Fundamental Subspaces","evidence_heading":"Connection To SVD","evidence_summary":"The note says SVD gives an orthonormal view of the four subspaces through singular vectors with zero and nonzero singular values.","confidence":0.9}
-->
