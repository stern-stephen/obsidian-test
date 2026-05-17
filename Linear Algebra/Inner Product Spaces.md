# Inner Product Spaces

## Overview

An inner product space is a vector space with an inner product, an operation that lets us talk about length, orthogonality, projections, and angles.

In quantum mechanics, inner product spaces are the mathematical home of state vectors. The inner product is what turns amplitudes into probabilities.

## Definition

An inner product takes two vectors and returns a scalar:

$$
\langle x, y \rangle
$$

For complex vector spaces, the inner product conjugates one side. In bra-ket notation:

$$
\langle \phi|\psi\rangle
$$

The norm of a vector is:

$$
\|x\| = \sqrt{\langle x, x\rangle}
$$

Two vectors are orthogonal when:

$$
\langle x, y\rangle = 0
$$

## Orthonormal Bases

A basis is orthonormal when each basis vector has norm $1$ and distinct basis vectors are orthogonal:

$$
\langle i|j\rangle = \delta_{ij}
$$

For an orthonormal basis, vector components can be extracted with inner products:

$$
v_i = \langle i|v\rangle
$$

This is the finite-dimensional version of the position-space relation:

$$
\psi(x)=\langle x|\psi\rangle
$$

## Why It Matters

Inner products support several recurring ideas:

- Normalization of state vectors.
- Orthogonality and distinguishability.
- Projection onto directions or subspaces.
- Adjoints, Hermitian operators, and unitary operators.
- Gram-Schmidt orthonormalization.

## Related Book Notes

- [Shankar: Inner Product Spaces](../Book%20Notes/Shankar/Chapter%201/Inner%20Product%20Spaces.md)
- [Shankar: Dual Spaces and Dirac Notation](../Book%20Notes/Shankar/Chapter%201/Dual%20Spaces%20and%20Dirac%20Notation.md)
- [Nielsen and Chuang: Linear Algebra](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Linear%20Algebra.md#214-inner-products)

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Adjoints](Adjoints.md)
- [Projection Operators](Projection%20Matrices.md)
- [Gram-Schmidt](Gram-Schmidt.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
