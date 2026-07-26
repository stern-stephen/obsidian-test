# Chapter Overview

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Book chapter: 4, printed pages 93-108.

PDF reference: [Hamill PDF](../../../References/Hamill.pdf). In this file, Hamill printed page 93 is PDF page 105.

Previous: [Chapter 3 - Lagrangian Dynamics](../Chapter%203/Chapter%20Overview.md)

Next: [Legendre Transformation and Hamiltonian](Legendre%20Transformation%20and%20Hamiltonian.md)

## Reading Status

- Status: started
- Pages: 93-108
- Date started: 2026-07-26
- Date finished:

## Big Ideas

- Hamiltonian mechanics begins by applying a [Legendre transform](../../../Mathematics/Legendre%20Transforms.md) to the Lagrangian, replacing velocities with conjugate momenta.
- The Hamiltonian is defined by $H=\sum_i p_i\dot q_i-L$ and must ultimately be written as $H(q,p,t)$.
- Hamilton's canonical equations express the dynamics as $2n$ first-order equations in [phase space](../../../Mechanics/Phase%20Space.md).
- The Hamiltonian is often the total energy, but Hamill emphasizes that this is a conditional result, not the definition.
- The modified Hamilton principle gives Hamilton's equations directly from a variational principle in phase-space variables.
- Phase-space trajectories do not cross because Hamilton's equations define a unique phase-space velocity at each point.
- The Routhian procedure partially Hamiltonizes cyclic coordinates while leaving non-cyclic coordinates in Lagrangian form.
- Symplectic notation packages Hamilton's equations into a compact matrix equation useful for computation.

## Section Notes

- [Legendre Transformation and Hamiltonian](Legendre%20Transformation%20and%20Hamiltonian.md)
- [Canonical Equations and Phase Space](Canonical%20Equations%20and%20Phase%20Space.md)
- [Routhian and Symplectic Notation](Routhian%20and%20Symplectic%20Notation.md)

## Logical Progression

1. Introduce the Legendre transform as a variable-trading operation.
2. Apply it to $L(q,\dot q,t)$ using the velocities as active variables.
3. Define $p_i=\partial L/\partial\dot q_i$ and $H=\sum_i p_i\dot q_i-L$.
4. Derive Hamilton's equations from the Legendre-transform relations.
5. Re-derive the same equations from the modified Hamilton principle.
6. Interpret solutions as curves in phase space rather than configuration space.
7. Use cyclic coordinates to reduce systems through the Routhian.
8. Collect $q_i,p_i$ into a single symplectic vector and write the equations in matrix form.

## Links To Concept Notes

- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Legendre Transforms](../../../Mathematics/Legendre%20Transforms.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)

## Questions

- What exact conditions make the Hamiltonian equal to total energy?
- Why does a Legendre transform, rather than an ordinary substitution, produce the Hamiltonian variables?
- How does the phase-space picture improve on configuration-space trajectories when initial velocities vary?
- When is the Routhian more useful than using either pure Lagrangian or pure Hamiltonian mechanics?

<!-- semantic-edges
{"source":"Hamill Chapter 4","relation":"INTRODUCES","target":"Hamiltonian Mechanics","evidence_heading":"Big Ideas","evidence_summary":"The chapter defines the Hamiltonian through a Legendre transform and derives Hamilton's canonical equations.","confidence":0.94}
{"source":"Hamill Chapter 4","relation":"USES","target":"Legendre Transform","evidence_heading":"Logical Progression","evidence_summary":"The chapter applies the Legendre transform to the Lagrangian, replacing velocities by conjugate momenta.","confidence":0.92}
{"source":"Hamill Chapter 4","relation":"REQUIRES","target":"Phase Space","evidence_heading":"Big Ideas","evidence_summary":"The chapter interprets Hamiltonian dynamics as motion in phase space with non-crossing phase-space trajectories.","confidence":0.9}
-->
