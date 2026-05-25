# The Hamiltonian Formalism

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 2.5.

Previous: [How Smart Is a Particle](How%20Smart%20Is%20a%20Particle.md)

Next: [The Electromagnetic Force in the Hamiltonian Scheme](The%20Electromagnetic%20Force%20in%20the%20Hamiltonian%20Scheme.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-19
- Date finished:

## Big Ideas

- Hamiltonian mechanics trades generalized velocities for canonical momenta.
- The state of a classical system is represented as a point in phase space.
- Hamilton's equations are first-order equations for $q_i$ and $p_i$.
- The Hamiltonian often equals total energy, but its deeper role is as the generator of time evolution.

## Notes

Starting from a Lagrangian $L(q,\dot{q},t)$, define:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

The Hamiltonian is the Legendre transform:

$$
H(q,p,t) = \sum_i p_i\dot{q}_i - L(q,\dot{q},t)
$$

Hamilton's equations are:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

## Phase Space

For $n$ generalized coordinates, the phase space has coordinates:

$$
(q_1,\ldots,q_n,p_1,\ldots,p_n)
$$

A point in phase space specifies the instantaneous classical state.

## Common Confusions

- The Hamiltonian is not defined by simply replacing velocity with momentum by eye; it comes from a Legendre transform.
- Phase space is not ordinary configuration space.
- Hamilton's equations are first order, while Newton's second law is second order.
- The Hamiltonian equals energy only under common but not universal assumptions.

## Links To Concept Notes

- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
