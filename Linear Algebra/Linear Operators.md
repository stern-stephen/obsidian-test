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
T(c_1v_1 + c_2v_2 + \cdots + c_nv_n) = c_1T(v_1) + c_2T(v_2) + \cdots + c_nT(v_n)
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

- [Shankar: Linear Operators](../Book%20Notes/Shankar/Chapter%201/Linear%20Operators.md)
- [Linear Algebra](Linear%20Algebra.md)
- [Vector Spaces](Vector%20Spaces.md)
- [Matrices](Matrices.md)
- [Change of Basis](Change%20of%20Basis.md)
- [Projection Operators](Projection%20Matrices.md)
- [Rotation Operators](Rotation%20Matrices.md)
- [Adjoints](Adjoints.md)
- [Commutators](Commutators.md)
- [Eigenvalues and Eigenvectors](Eigenvalues%20and%20Eigenvectors.md)

<!-- semantic-edges
{"source":"Linear Operators","relation":"REQUIRES","target":"Vector Spaces","evidence_heading":"Overview","evidence_summary":"The note defines a linear operator as a function that sends vectors to vectors while preserving vector-space structure.","confidence":0.95}
{"source":"Linear Operators","relation":"DETERMINES","target":"Linear Combinations","evidence_heading":"Overview","evidence_summary":"The note says a linear operator respects linear combinations by distributing over sums and scalar multiples.","confidence":0.9}
{"source":"Operator Composition","relation":"MOTIVATES","target":"Noncommutativity","evidence_heading":"Composition","evidence_summary":"The note says linear operator composition is usually not commutative, which explains why matrix multiplication usually is not commutative.","confidence":0.85}
{"source":"Commutators","relation":"DETERMINES","target":"Operator Order Dependence","evidence_heading":"Commutators","evidence_summary":"The note says the commutator measures whether the order of applying operators matters.","confidence":0.9}
-->
