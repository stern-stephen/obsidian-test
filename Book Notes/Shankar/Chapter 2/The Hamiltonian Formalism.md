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

Shankar changes from $(q,\dot q)$ to $(q,p)$ because the Hamiltonian language is the classical structure most directly reused in quantum mechanics. The [Legendre transform](../../../Mathematics/Legendre%20Transforms.md), Hamilton's equations, and worked examples are maintained in [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md).

The source-specific emphasis is that $H$ is not merely another expression for energy. It is the function that generates time evolution, foreshadowing the Hamiltonian operator in the Schrodinger equation.

## Phase Space

A classical state becomes a point in [Phase Space](../../../Mechanics/Phase%20Space.md), with one canonical momentum paired with each generalized coordinate. Shankar later contrasts this state description with a quantum state vector.

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

<!-- semantic-edges
{"source":"Shankar Section 2.5","relation":"INTRODUCES","target":"Hamiltonian Mechanics","evidence_heading":"Big Ideas","evidence_summary":"Introduces Hamiltonian mechanics by trading generalized velocities for canonical momenta and using first-order equations.","confidence":0.92}
{"source":"Shankar Section 2.5","relation":"INTRODUCES","target":"Phase Space","evidence_heading":"Phase Space","evidence_summary":"Presents a classical state as a point in phase space with each coordinate paired to a canonical momentum.","confidence":0.91}
{"source":"Legendre Transform","relation":"ENABLES","target":"Hamiltonian Formalism","evidence_heading":"Notes","evidence_summary":"Uses the Legendre transform as the route from the Lagrangian variables to Hamiltonian variables.","confidence":0.88}
{"source":"Hamiltonian","relation":"MOTIVATES","target":"Schrodinger Time Evolution","evidence_heading":"Notes","evidence_summary":"Emphasizes the Hamiltonian as generator of time evolution, foreshadowing the Hamiltonian operator in the Schrodinger equation.","confidence":0.88}
-->
