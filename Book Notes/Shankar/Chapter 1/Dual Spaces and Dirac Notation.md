# Dual Spaces and Dirac Notation

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.3.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- A ket $|v\rangle$ is a vector.
- A bra $\langle v|$ is the corresponding dual vector, a linear functional that takes a ket and returns a scalar.
- Dirac notation makes inner products, projections, basis expansions, and operators compact.
- The adjoint operation turns kets into bras and reverses the order of products.

## Notes

The dual space is the space of linear maps from vectors to scalars.

In Dirac notation, a vector is written as a ket:

$$
|v\rangle
$$

The corresponding dual vector is written as a bra:

$$
\langle v|
$$

Putting a bra and ket together gives an inner product:

$$
\langle u|v\rangle
$$

## Expansion In An Orthonormal Basis

If $\{|i\rangle\}$ is an orthonormal basis, then:

$$
|v\rangle = \sum_i |i\rangle\langle i|v\rangle
$$

Since:

$$
v_i = \langle i|v\rangle
$$

this is the same as:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

The identity operator can be written:

$$
I = \sum_i |i\rangle\langle i|
$$

## Outer Products

The object:

$$
|u\rangle\langle v|
$$

is an operator. Acting on $|w\rangle$, it gives:

$$
|u\rangle\langle v|w\rangle
$$

That means it first computes the scalar $\langle v|w\rangle$, then multiplies $|u\rangle$ by that scalar.

## Adjoint Operation

The adjoint turns kets into bras and reverses order:

$$
(A|v\rangle)^\dagger = \langle v|A^\dagger
$$

For products:

$$
(AB)^\dagger = B^\dagger A^\dagger
$$

## Inequalities

The Schwarz inequality says:

$$
|\langle u|v\rangle| \le \|u\|\,\|v\|
$$

The triangle inequality says:

$$
\|u+v\| \le \|u\| + \|v\|
$$

These are basic consistency conditions behind the geometry of inner product spaces.

## Common Confusions

- A bra is not just a ket written backward. It lives in the dual space and acts on kets.
- The order in $\langle u|v\rangle$ matters in complex vector spaces because $\langle u|v\rangle = \langle v|u\rangle^*$.
- The outer product $|u\rangle\langle v|$ is an operator, not a scalar.

## Links To Concept Notes

- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Adjoints](../../../Linear%20Algebra/Adjoints.md)
- [Gram-Schmidt](../../../Linear%20Algebra/Gram-Schmidt.md)
- [Projection Operators](../../../Linear%20Algebra/Projection%20Matrices.md)
- [Inner Product Spaces](Inner%20Product%20Spaces.md)
