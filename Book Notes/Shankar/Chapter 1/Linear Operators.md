# Linear Operators

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.5.

Previous: [Subspaces](Subspaces.md)

Next: [Matrix Elements of Linear Operators](Matrix%20Elements%20of%20Linear%20Operators.md)

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

Shankar introduces operators as transformations of abstract vectors before representing them by matrices. That order matters for quantum mechanics: the operator is the basis-independent object, while its matrix elements depend on a chosen basis.

He also emphasizes ordered composition. The product $AB$ applies $B$ first, and the failure of $A$ and $B$ to commute becomes physically significant once operators represent observables and transformations.

See [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md) for the reusable definition and examples, and [Commutators](../../../Linear%20Algebra/Commutators.md) for the canonical algebra. The next section develops their coordinate representations as matrix elements.

## Common Confusions

- $AB$ is an ordered operation. Switching the order can change the result.
- An operator is not the same thing as a matrix; a matrix is what the operator looks like after choosing bases.
- Linearity is a strong condition. Many functions from vectors to vectors are not linear.

## Links To Concept Notes

- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Commutators](../../../Linear%20Algebra/Commutators.md)
- [Functions of Operators](Functions%20of%20Operators.md)
- [Matrix Elements of Linear Operators](Matrix%20Elements%20of%20Linear%20Operators.md)

<!-- semantic-edges
{"source":"Shankar Section 1.5","relation":"INTRODUCES","target":"Linear Operators","evidence_heading":"Big Ideas","evidence_summary":"Introduces operators as abstract linear maps that preserve linear combinations and later become quantum observables or time-evolution maps.","confidence":0.93}
{"source":"Shankar Section 1.5","relation":"MOTIVATES","target":"Matrix Representations of Operators","evidence_heading":"Big Ideas","evidence_summary":"Distinguishes the abstract operator from the matrix that represents it after a basis is chosen.","confidence":0.9}
{"source":"Operator Composition","relation":"MOTIVATES","target":"Commutators","evidence_heading":"Big Ideas","evidence_summary":"The noncommutativity of operator composition prepares the later use of commutators.","confidence":0.86}
{"source":"Linear Operators","relation":"MOTIVATES","target":"Quantum Observables","evidence_heading":"Big Ideas","evidence_summary":"Connects special classes of linear operators to observables and time evolution in quantum mechanics.","confidence":0.86}
-->
