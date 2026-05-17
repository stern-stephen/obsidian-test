# Subspaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.4.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- A subspace is a smaller vector space inside a larger vector space.
- Subspaces must be closed under vector addition and scalar multiplication.
- Orthogonal complements split a vector space into mutually perpendicular pieces.
- Projection operators are the operator language for extracting the part of a vector that lies in a subspace.

## Notes

A subset $W$ of a vector space $V$ is a subspace if, whenever $|u\rangle$ and $|v\rangle$ are in $W$:

$$
|u\rangle + |v\rangle \in W
$$

and for any scalar $c$:

$$
c|u\rangle \in W
$$

The zero vector must also be in the subspace.

## Span

The span of a set of vectors is the set of all linear combinations of them:

$$
\operatorname{span}\{|v_1\rangle,\ldots,|v_n\rangle\}
$$

This span is itself a subspace.

## Orthogonal Complements

If $W$ is a subspace, its orthogonal complement $W^\perp$ contains all vectors orthogonal to every vector in $W$:

$$
W^\perp = \{|v\rangle : \langle w|v\rangle = 0 \text{ for all } |w\rangle \in W\}
$$

This is useful because a vector can often be decomposed into a part inside a subspace and a part orthogonal to it.

## Common Confusions

- A subset is not automatically a subspace. It must be closed under addition and scalar multiplication.
- A line that does not pass through the origin is not a subspace.
- Orthogonal complements depend on the inner product.

## Links To Concept Notes

- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Four Fundamental Subspaces](../../../Linear%20Algebra/Four%20Fundamental%20Subspaces.md)
- [Gram-Schmidt](../../../Linear%20Algebra/Gram-Schmidt.md)
