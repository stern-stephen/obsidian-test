# Active and Passive Transformations

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 1.7.

Previous: [Matrix Elements of Linear Operators](Matrix%20Elements%20of%20Linear%20Operators.md)

Next: [The Eigenvalue Problem](The%20Eigenvalue%20Problem.md)

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

## Exercise Answers

These are answer summaries for Shankar Chapter 1 exercises in this section. I am not reproducing the full problem statements here.

### Exercise 1.7.1

The trace is:

$$
\operatorname{Tr}A=\sum_i A_{ii}
$$

For a product of two matrices:

$$
\operatorname{Tr}(AB)=\sum_i(AB)_{ii}
$$

Using matrix multiplication:

$$
\operatorname{Tr}(AB)=\sum_{i,j}A_{ij}B_{ji}
$$

Swap the dummy labels $i$ and $j$:

$$
\operatorname{Tr}(AB)=\sum_{i,j}B_{ij}A_{ji}=\operatorname{Tr}(BA)
$$

More generally, the trace is cyclic:

$$
\operatorname{Tr}(ABC)=\operatorname{Tr}(BCA)=\operatorname{Tr}(CAB)
$$

Under a unitary change of basis:

$$
A\to U^\dagger A U
$$

so:

$$
\operatorname{Tr}(U^\dagger A U)=\operatorname{Tr}(UU^\dagger A)=\operatorname{Tr}A
$$

The trace is basis independent.

### Exercise 1.7.2

Under a unitary change of basis:

$$
A\to U^\dagger A U
$$

Taking determinants:

$$
\det(U^\dagger A U)=\det(U^\dagger)\det(A)\det(U)
$$

Since $U$ is unitary:

$$
\det(U^\dagger)\det(U)=1
$$

Therefore:

$$
\det(U^\dagger A U)=\det A
$$

The determinant is also basis independent.

## Links To Concept Notes

- [Change of Basis](../../../Linear%20Algebra/Change%20of%20Basis.md)
- [Unitary Matrices](../../../Linear%20Algebra/Unitary%20Matrices.md)
- [Matrices](../../../Linear%20Algebra/Matrices.md)
- [Linear Operators](../../../Linear%20Algebra/Linear%20Operators.md)
