# Gram-Schmidt

## Overview

The **Gram-Schmidt process** turns a linearly independent list of vectors into an orthonormal list of vectors that spans the same subspace.

It is a way to build a clean coordinate system inside an inner product space.

Starting with vectors:

$$
v_1, v_2, \ldots, v_n
$$

Gram-Schmidt produces orthonormal vectors:

$$
q_1, q_2, \ldots, q_n
$$

where:

$$
\langle q_i, q_j \rangle = 0
$$

for $i \ne j$, and:

$$
\|q_i\| = 1
$$

## Projection

The key step is removing the part of one vector that points in the direction of another vector.

The projection of $v$ onto a unit vector $q$ is:

$$
\mathrm{proj}_q(v) = \langle q, v \rangle q
$$

If $q$ is not already normalized, then:

$$
\mathrm{proj}_q(v) = \frac{\langle q, v \rangle}{\langle q, q \rangle}q
$$

## The Process

Start with:

$$
u_1 = v_1
$$

Normalize it:

$$
q_1 = \frac{u_1}{\|u_1\|}
$$

Then remove the part of $v_2$ that points in the $q_1$ direction:

$$
u_2 = v_2 - \langle q_1, v_2 \rangle q_1
$$

Normalize again:

$$
q_2 = \frac{u_2}{\|u_2\|}
$$

In general:

$$
u_k = v_k - \sum_{j=1}^{k-1} \langle q_j, v_k \rangle q_j
$$

and:

$$
q_k = \frac{u_k}{\|u_k\|}
$$

## Why It Matters

Gram-Schmidt is useful because many parts of [Linear Algebra](Linear%20Algebra.md) become simpler with orthonormal bases.

It appears in:

- Building orthonormal bases for [Vector Spaces](Vector%20Spaces.md).
- Understanding [Unitary Operators](Unitary%20Matrices.md), whose matrix representations have orthonormal columns.
- Diagonalizing [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md).
- Constructing the $Q$ factor in QR decomposition.

## Intuition

Gram-Schmidt works by taking each new vector and subtracting away all directions already accounted for.

What remains is the genuinely new direction. After normalizing it, that new direction becomes the next orthonormal basis vector.

## Related Concepts

- [Vector Spaces](Vector%20Spaces.md)
- [Adjoints](Adjoints.md)
- [Unitary Operators](Unitary%20Matrices.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)

<!-- semantic-edges
{"source":"Gram-Schmidt","relation":"DETERMINES","target":"Orthonormal Bases","evidence_heading":"Overview","evidence_summary":"The note says Gram-Schmidt turns a linearly independent list into an orthonormal list spanning the same subspace.","confidence":0.95}
{"source":"Gram-Schmidt","relation":"REQUIRES","target":"Inner Product Spaces","evidence_heading":"Overview","evidence_summary":"The note describes Gram-Schmidt as building a clean coordinate system inside an inner product space.","confidence":0.9}
{"source":"Projections","relation":"ENABLES","target":"Gram-Schmidt","evidence_heading":"Projection","evidence_summary":"The note identifies projection as the key step for removing the part of one vector pointing in another direction.","confidence":0.9}
{"source":"Gram-Schmidt","relation":"ENABLES","target":"Unitary Operators","evidence_heading":"Why It Matters","evidence_summary":"The note says Gram-Schmidt helps understand unitary operators, whose matrix representations have orthonormal columns.","confidence":0.85}
-->
