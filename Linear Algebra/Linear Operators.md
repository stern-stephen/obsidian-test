# Linear Operators

## Overview

A **linear operator** is a function that sends vectors to vectors while preserving the linear structure of a vector space.

If $T$ is a linear operator and $u$ and $v$ are vectors, then:

$$
T(u + v) = T(u) + T(v)
$$

If $c$ is a scalar, then:

$$
T(cv) = cT(v)
$$

Together, these say that a linear operator respects linear combinations:

$$
T(c_1v_1 + c_2v_2 + \cdots + c_nv_n)
= c_1T(v_1) + c_2T(v_2) + \cdots + c_nT(v_n)
$$

## Operators Versus Matrices

A linear operator is the actual map between vector spaces.

A [matrix](Matrices.md) is a coordinate representation of that operator after bases have been chosen.

This distinction matters because the same operator can have different matrices in different bases. The operator is the underlying object; the matrix is how that object looks in a particular coordinate system.

See [Change of Basis](Change%20of%20Basis.md) for how matrix representations change when the basis changes.

## Examples

A rotation of the plane is a linear operator because rotating a sum gives the same result as rotating each vector and then adding:

$$
R(u + v) = R(u) + R(v)
$$

A projection onto a subspace is also linear:

$$
P(cu + dv) = cP(u) + dP(v)
$$

Differentiation is a linear operator on many function spaces:

$$
\frac{d}{dx}(f + g) = \frac{df}{dx} + \frac{dg}{dx}
$$

and:

$$
\frac{d}{dx}(cf) = c\frac{df}{dx}
$$

## Composition

Linear operators can be composed.

If $S$ and $T$ are linear operators, then $S \circ T$ means "apply $T$ first, then apply $S$":

$$
(S \circ T)(v) = S(T(v))
$$

Composition is usually not commutative:

$$
S \circ T \ne T \circ S
$$

This is one reason matrix multiplication is usually not commutative.

## Commutators

For operators $A$ and $B$, the commutator is:

$$
[A,B]=AB-BA
$$

It measures whether the order of applying operators matters. See [Commutators](Commutators.md).

## Related Concepts

- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Matrices](Matrices.md)
- [Change of Basis](Change%20of%20Basis.md)
- [Projection Operators](Projection%20Matrices.md)
- [Rotation Operators](Rotation%20Matrices.md)
- [Adjoints](Adjoints.md)
- [Commutators](Commutators.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)
