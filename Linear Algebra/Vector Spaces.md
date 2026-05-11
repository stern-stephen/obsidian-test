# Vector Spaces

## Overview

A **vector space** is a collection of objects called vectors, together with rules for adding vectors and multiplying them by scalars.

The scalars usually come from either the real numbers $\mathbb{R}$ or the complex numbers $\mathbb{C}$.

Examples of vector spaces include:

- Ordinary coordinate vectors like $\mathbb{R}^2$ and $\mathbb{R}^3$.
- Complex coordinate vectors like $\mathbb{C}^n$.
- Polynomials of degree at most $n$.
- Functions that can be added and scaled.
- Quantum states in a Hilbert space.

## Basic Structure

If $u$ and $v$ are vectors in a vector space $V$, and $c$ is a scalar, then:

$$
u + v \in V
$$

and:

$$
cv \in V
$$

This closure is what lets vector spaces support linear combinations.

## Linear Combinations

A **linear combination** of vectors $v_1, v_2, \ldots, v_n$ has the form:

$$
c_1 v_1 + c_2 v_2 + \cdots + c_n v_n
$$

where $c_1, c_2, \ldots, c_n$ are scalars.

The set of all linear combinations of a collection of vectors is called their **span**.

## Basis And Dimension

A **basis** is a set of vectors that is both:

- Linearly independent.
- Spans the whole vector space.

If a vector space has a basis with $n$ vectors, then its dimension is $n$.

For example, the standard basis for $\mathbb{R}^3$ is:

$$
e_1 =
\begin{bmatrix}
1 \\
0 \\
0
\end{bmatrix},
\quad
e_2 =
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix},
\quad
e_3 =
\begin{bmatrix}
0 \\
0 \\
1
\end{bmatrix}
$$

## Inner Product Spaces

An **inner product space** is a vector space with an additional operation called an inner product.

The inner product takes two vectors and returns a scalar:

$$
\langle x, y \rangle
$$

Inner products let us talk about length, angle, orthogonality, and projection.

The length of a vector is:

$$
\|x\| = \sqrt{\langle x, x \rangle}
$$

Two vectors are orthogonal when:

$$
\langle x, y \rangle = 0
$$

Inner product spaces are where concepts like [[Adjoints]], [[Unitary Matrices]], [[Hermitian Matrices and Operators]], and [[Gram-Schmidt]] naturally live.

## Related Concepts

- [[Linear Algebra]]
- [[Adjoints]]
- [[Bra-Ket Notation]]
- [[Gram-Schmidt]]
- [[Eigenvalues]]
- [[Unitary Matrices]]
- [[Hermitian Matrices and Operators]]
