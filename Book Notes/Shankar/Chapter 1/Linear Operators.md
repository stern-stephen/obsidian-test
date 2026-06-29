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
{"source":"Linear Operators","relation":"PART_OF","target":"Shankar Chapter 1","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Shankar Chapter 1.","confidence":0.85}
{"source":"Linear Operators","relation":"SOURCE_CONTEXT_FOR","target":"Subspaces","evidence_heading":"Linear Operators","evidence_summary":"This source note explicitly links its treatment to Subspaces.","confidence":0.8}
{"source":"Linear Operators","relation":"SOURCE_CONTEXT_FOR","target":"Matrix Elements of Linear Operators","evidence_heading":"Linear Operators","evidence_summary":"This source note explicitly links its treatment to Matrix Elements of Linear Operators.","confidence":0.8}
{"source":"Linear Operators","relation":"SOURCE_CONTEXT_FOR","target":"Commutators","evidence_heading":"Notes","evidence_summary":"This source note explicitly links its treatment to Commutators.","confidence":0.8}
{"source":"Linear Operators","relation":"SOURCE_CONTEXT_FOR","target":"Matrices","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Matrices.","confidence":0.8}
-->
