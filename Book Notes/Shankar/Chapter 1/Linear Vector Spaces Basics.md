# Linear Vector Spaces Basics

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.1.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- A vector space is defined by rules for adding vectors and multiplying them by scalars.
- The same abstract rules describe arrows, columns, polynomials, and functions.
- A basis lets every vector be written as a linear combination of basis vectors.
- The components of a vector depend on the basis, but the vector itself does not.

## Notes

The point of this section is to abstract away from the usual picture of vectors as arrows.

If $V$ is a vector space, then vectors $|u\rangle$ and $|v\rangle$ can be added, and vectors can be multiplied by scalars:

$$
|u\rangle + |v\rangle \in V
$$

$$
a|v\rangle \in V
$$

The rules are the familiar linearity rules: addition is associative and commutative, scalar multiplication distributes over vector addition, there is a zero vector, and every vector has an additive inverse.

## Linear Combinations

A linear combination has the form:

$$
a_1|v_1\rangle + a_2|v_2\rangle + \cdots + a_n|v_n\rangle
$$

This is the basic building block for almost everything that follows.

## Linear Independence

A set of vectors is linearly independent when:

$$
a_1|v_1\rangle + a_2|v_2\rangle + \cdots + a_n|v_n\rangle = |0\rangle
$$

only has the trivial solution:

$$
a_1 = a_2 = \cdots = a_n = 0
$$

If there is a nontrivial solution, one of the vectors is redundant because it can be built from the others.

## Basis And Components

A basis is a set of vectors that is both linearly independent and spanning.

If $\{|i\rangle\}$ is a basis, then:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

The numbers $v_i$ are the components of $|v\rangle$ in that basis.

## Common Confusions

- A column of numbers is not the vector itself. It is the vector's coordinate representation in a chosen basis.
- A function can be a vector if it belongs to a space where function addition and scalar multiplication obey the vector-space rules.
- Linear independence is about whether vectors contain genuinely new directions, not about whether they look visually different.

## Links To Concept Notes

- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Vectors](../../../Linear%20Algebra/Vectors.md)
- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Infinite-Dimensional Spaces](Infinite-Dimensional%20Spaces.md)
