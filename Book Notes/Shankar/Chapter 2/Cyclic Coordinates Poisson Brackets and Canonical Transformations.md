# Cyclic Coordinates, Poisson Brackets, and Canonical Transformations

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 2.7.

Previous: [The Electromagnetic Force in the Hamiltonian Scheme](The%20Electromagnetic%20Force%20in%20the%20Hamiltonian%20Scheme.md)

Next: [Symmetries and Their Consequences](Symmetries%20and%20Their%20Consequences.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-19
- Date finished:

## Big Ideas

- If a coordinate does not appear in the Hamiltonian or Lagrangian, its conjugate momentum is conserved.
- Poisson brackets give a compact algebraic language for time evolution and conserved quantities.
- Canonical transformations preserve Hamilton's equations.
- The Poisson bracket structure foreshadows quantum commutators.

## Cyclic Coordinates

A coordinate $q_i$ is cyclic if it does not appear explicitly in the Lagrangian:

$$
\frac{\partial L}{\partial q_i} = 0
$$

Then the conjugate momentum is conserved:

$$
\dot{p}_i = 0
$$

## Poisson Brackets

For functions $f(q,p)$ and $g(q,p)$, the Poisson bracket is:

$$
\{f,g\} = \sum_i \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)
$$

Time evolution can be written:

$$
\frac{df}{dt} = \{f,H\} + \frac{\partial f}{\partial t}
$$

The basic brackets are:

$$
\{q_i,p_j\} = \delta_{ij}
$$

## Canonical Transformations

A canonical transformation is a change of phase-space coordinates that preserves Hamilton's form of the equations of motion.

This matters because it identifies transformations that change coordinates without changing the underlying mechanics.

## Common Confusions

- A cyclic coordinate is absent from the dynamics formula, but it can still describe a real physical direction.
- Poisson brackets are operations on functions on phase space, not ordinary products.
- Canonical transformations are special phase-space transformations, not arbitrary changes of variables.

## Links To Concept Notes

- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Poisson Brackets](../../../Mechanics/Poisson%20Brackets.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Commutators](../../../Linear%20Algebra/Commutators.md)
