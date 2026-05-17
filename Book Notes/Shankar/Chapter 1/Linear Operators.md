# Linear Operators

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.5.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- A linear operator maps vectors to vectors while preserving linear combinations.
- Operators are abstract transformations; matrices are their coordinate representations in chosen bases.
- Composition of operators is generally not commutative.
- Quantum observables and time evolution are represented using special classes of linear operators.

## Notes

An operator $A$ is linear if:

$$
A(a|u\rangle + b|v\rangle) = aA|u\rangle + bA|v\rangle
$$

The identity operator leaves every vector unchanged:

$$
I|v\rangle = |v\rangle
$$

The zero operator sends every vector to the zero vector:

$$
0|v\rangle = |0\rangle
$$

## Products And Commutators

The product $AB$ means "apply $B$ first, then $A$":

$$
AB|v\rangle = A(B|v\rangle)
$$

In general:

$$
AB \ne BA
$$

The commutator measures this failure:

$$
[A,B] = AB - BA
$$

## Common Confusions

- $AB$ is an ordered operation. Switching the order can change the result.
- An operator is not the same thing as a matrix; a matrix is what the operator looks like after choosing bases.
- Linearity is a strong condition. Many functions from vectors to vectors are not linear.

## Links To Concept Notes

- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Commutators](../../../Book%20Notes/Nielsen%20Chuang/Chapter%202/Linear%20Algebra.md#219-commutators-and-anti-commutators)
- [Functions of Operators](Functions%20of%20Operators.md)
- [Matrix Elements of Linear Operators](Matrix%20Elements%20of%20Linear%20Operators.md)
