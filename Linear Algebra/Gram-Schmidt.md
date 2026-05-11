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
\operatorname{proj}_q(v) = \langle q, v \rangle q
$$

If $q$ is not already normalized, then:

$$
\operatorname{proj}_q(v) =
\frac{\langle q, v \rangle}{\langle q, q \rangle}q
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

Gram-Schmidt is useful because many parts of [[Linear Algebra]] become simpler with orthonormal bases.

It appears in:

- Building orthonormal bases for [[Vector Spaces]].
- Understanding [[Unitary Matrices]], whose columns are orthonormal.
- Diagonalizing [[Hermitian Matrices and Operators]].
- Constructing the $Q$ factor in QR decomposition.

## Intuition

Gram-Schmidt works by taking each new vector and subtracting away all directions already accounted for.

What remains is the genuinely new direction. After normalizing it, that new direction becomes the next orthonormal basis vector.

## Related Concepts

- [[Vector Spaces]]
- [[Adjoints]]
- [[Unitary Matrices]]
- [[Hermitian Matrices and Operators]]
- [[Eigenvalues]]
