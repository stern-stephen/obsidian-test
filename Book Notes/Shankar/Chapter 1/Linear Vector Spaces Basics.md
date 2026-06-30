# Linear Vector Spaces Basics

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.1.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Inner Product Spaces](Inner%20Product%20Spaces.md)

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

Shankar begins by separating an abstract vector from any particular picture or coordinate list. Arrows, columns, matrices, polynomials, and functions can all be vectors when they obey the same linear rules.

His immediate purpose is preparation for quantum mechanics: a ket is the vector, while its components depend on the chosen basis. Linear combinations, independence, span, basis, and dimension are developed as the language needed to describe states without confusing them with one representation.

The reusable definitions and equations are collected in [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md). The distinction between a vector and its coordinate representation continues in [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md).

## Common Confusions

- A column of numbers is not the vector itself. It is the vector's coordinate representation in a chosen basis.
- A function can be a vector if it belongs to a space where function addition and scalar multiplication obey the vector-space rules.
- Linear independence is about whether vectors contain genuinely new directions, not about whether they look visually different.

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.1.1

To check whether a proposed set is a vector space, test the vector-space axioms against the proposed operations. The usual trap is closure: if adding two allowed objects or multiplying one by a scalar leaves the proposed set, it is not a vector space.

For examples involving functions, the set of all functions obeying a homogeneous condition such as $f(0)=0$ is a vector space, because:

$$
(af+bg)(0)=af(0)+bg(0)=0
$$

A set obeying an inhomogeneous condition such as $f(0)=4$ is not a vector space, because scalar multiplication fails:

$$
(cf)(0)=cf(0)=4c
$$

This equals $4$ only for special values of $c$, not for arbitrary scalars.

### Exercise 1.1.2

Use the same closure test. Periodic functions obeying $f(0)=f(L)$ form a vector space:

$$
(af+bg)(0)=af(0)+bg(0)=af(L)+bg(L)=(af+bg)(L)
$$

So the periodic boundary condition survives linear combinations.

### Exercise 1.1.3

For any candidate vector space, first check the null vector. If the proposed set does not contain the relevant zero object, it cannot be a vector space.

For instance, affine conditions such as "functions whose value at a point is a fixed nonzero number" fail immediately because the zero function does not satisfy the condition.

### Exercise 1.1.4

Treat each $2\times 2$ matrix as a vector and solve:

$$
a|1\rangle+b|2\rangle+c|3\rangle=0
$$

For Shankar's three matrices, the component equations reduce to:

$$
b-2c=0
$$

and:

$$
a+b-c=0
$$

There are only two independent equations for three unknowns. A nontrivial solution exists; for example, one may take:

$$
c=-a,\qquad b=-2a
$$

So the matrices are linearly dependent. Equivalently, one matrix can be written as a linear combination of the other two:

$$
|1\rangle=2|2\rangle+|3\rangle
$$

### Exercise 1.1.5

For the first set of row vectors:

$$
(1,1,0),\quad (1,0,1),\quad (3,2,1)
$$

notice:

$$
(3,2,1)=2(1,1,0)+(1,0,1)
$$

So the set is linearly dependent.

For the second set:

$$
(1,1,0),\quad (1,0,1),\quad (0,1,1)
$$

solve:

$$
a(1,1,0)+b(1,0,1)+c(0,1,1)=(0,0,0)
$$

This gives:

$$
a+b=0,\qquad a+c=0,\qquad b+c=0
$$

The only solution is:

$$
a=b=c=0
$$

So the second set is linearly independent.

## Links To Concept Notes

- [Vector Spaces](../../../Linear%20Algebra/Vector%20Spaces.md)
- [Vectors](../../../Linear%20Algebra/Vectors.md)
- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Bra-Ket Notation](../../../Linear%20Algebra/Bra-Ket%20Notation.md)
- [Infinite-Dimensional Spaces](Infinite-Dimensional%20Spaces.md)
