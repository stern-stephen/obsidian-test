# Active and Passive Transformations

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.7.

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-17
- Date finished:

## Big Ideas

- An active transformation changes the vector.
- A passive transformation changes the basis used to describe the vector.
- The same matrix algebra can describe both viewpoints, which is why it is easy to confuse them.
- Quantum mechanics often uses unitary transformations to change states, change bases, or change representations.

## Notes

In an active transformation, an operator acts on the vector:

$$
|v\rangle \mapsto |v'\rangle = U|v\rangle
$$

The basis is held fixed, and the vector changes.

In a passive transformation, the vector is held fixed but the basis changes. The components of the same vector change because the coordinate system changed.

## Components

If:

$$
|v\rangle = \sum_i v_i |i\rangle
$$

then the components $v_i$ depend on the basis $\{|i\rangle\}$.

Changing the basis changes the list of numbers used to describe $|v\rangle$, even if the abstract vector is unchanged.

## Operator Representations

The matrix representation of an operator also changes with basis.

If $S$ is the change-of-basis operator, the same abstract operator $A$ may be represented as:

$$
A' = S^{-1}AS
$$

This is a similarity transformation.

## Common Confusions

- Active and passive transformations can produce related formulas but mean different things.
- A vector and its coordinate list are not the same object.
- A basis change does not change the physical vector; it changes its description.

## Links To Concept Notes

- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
