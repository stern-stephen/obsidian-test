# Inner Product Spaces

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.2.

Previous: [Linear Vector Spaces Basics](Linear%20Vector%20Spaces%20Basics.md)

Next: [Dual Spaces and Dirac Notation](Dual%20Spaces%20and%20Dirac%20Notation.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- An inner product adds geometry to a vector space.
- It lets us define length, angle, orthogonality, and normalization.
- In complex vector spaces, the inner product is conjugate-linear in one slot and linear in the other.
- Quantum mechanics uses inner products to compute amplitudes and probabilities.

## Notes

An inner product takes two vectors and returns a scalar:

$$
\langle u|v\rangle
$$

It behaves like a generalized dot product.

The norm of a vector is:

$$
\|v\| = \sqrt{\langle v|v\rangle}
$$

A normalized vector has length $1$:

$$
\langle v|v\rangle = 1
$$

Two vectors are orthogonal when:

$$
\langle u|v\rangle = 0
$$

## Complex Inner Products

For complex vector spaces, conjugation matters. A common convention in physics notation is:

$$
\langle u|cv\rangle = c\langle u|v\rangle
$$

and:

$$
\langle cu|v\rangle = c^*\langle u|v\rangle
$$

This convention makes:

$$
\langle u|v\rangle = \langle v|u\rangle^*
$$

## Orthonormal Bases

A basis is orthonormal when:

$$
\langle i|j\rangle = \delta_{ij}
$$

This is the cleanest kind of basis because components can be found by projection:

$$
v_i = \langle i|v\rangle
$$

## Common Confusions

- The inner product is not just multiplication. It is a rule that depends on the vector space.
- Orthogonality means zero inner product, not necessarily visual perpendicularity.
- Normalization changes the length of a vector but not the one-dimensional direction it represents.

## Links To Concept Notes

- [Inner Product Spaces](../../../Linear%20Algebra/Inner%20Product%20Spaces.md)
- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Gram-Schmidt](../../../Linear%20Algebra/Gram-Schmidt.md)
- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
