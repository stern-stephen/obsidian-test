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

## General Vector Spaces And Groups

A vector space does not have to be made of arrows or coordinate lists. A vector space can be any collection of objects that can be added together and scaled, as long as the vector space rules are satisfied.

For example, the following can all be vector spaces:

- Lists of numbers.
- Polynomials.
- Functions.
- Matrices of a fixed size.
- Quantum states.

The word **vector** means "an element of a vector space." It does not always mean a geometric arrow.

Vector spaces are closely related to **groups**. Under vector addition, every vector space is an **abelian group**:

- Vectors can be added.
- Addition is associative.
- There is a zero vector $0$.
- Every vector $v$ has an additive inverse $-v$.
- Addition is commutative, so $u + v = v + u$.

The extra structure that makes a vector space more than just a group is **scalar multiplication**. Scalars come from a field, usually $\mathbb{R}$ or $\mathbb{C}$, and they act on vectors:

$$
c v
$$

Scalar multiplication must interact nicely with vector addition. For example:

$$
c(u + v) = cu + cv
$$

and:

$$
(c + d)v = cv + dv
$$

So a vector space is like an abelian group with a compatible way for numbers to stretch, shrink, flip, or phase-shift its elements.

## Linear Operators

A **linear operator** is a function that sends vectors to vectors while preserving vector addition and scalar multiplication.

If $T$ is a linear operator, then:

$$
T(u + v) = T(u) + T(v)
$$

and:

$$
T(cv) = cT(v)
$$

Linear operators are the natural maps between vector spaces. Once a basis is chosen, a linear operator can be represented by a [matrix](Matrices.md). See [Linear Operators](Linear%20Operators.md).

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

Changing from one basis to another changes the coordinate description of a vector without changing the vector itself. See [Change of Basis](Change%20of%20Basis.md).

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

Inner product spaces are where concepts like [Adjoints](Adjoints.md), [Projection Operators](Projection%20Matrices.md), [Unitary Operators](Unitary%20Matrices.md), [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md), and [Gram-Schmidt](Gram-Schmidt.md) naturally live.

See [Inner Product Spaces](Inner%20Product%20Spaces.md) for a fuller reusable note, especially for the quantum mechanics interpretation.

## Tensor Products

Tensor products combine vector spaces into larger vector spaces. They are essential for composite quantum systems and multi-qubit states.

If $V$ and $W$ are vector spaces, their tensor product is:

$$
V \otimes W
$$

See [Tensor Products](Tensor%20Products.md).

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Linear Operators](Linear%20Operators.md)
- [Inner Product Spaces](Inner%20Product%20Spaces.md)
- [Tensor Products](Tensor%20Products.md)
- [Adjoints](Adjoints.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Change of Basis](Change%20of%20Basis.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Projection Operators](Projection%20Matrices.md)
- [Four Fundamental Subspaces](Four%20Fundamental%20Subspaces.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
