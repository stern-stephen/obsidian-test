# Energy Function

## Overview

The Lagrangian energy function is conserved when the Lagrangian has no explicit time dependence. It often equals total mechanical energy, but these are logically separate facts.

## Definition

For $L(q,\dot q,t)$ and conjugate momenta $p_j=\partial L/\partial\dot q_j$:

$$
h(q,\dot q,t)=\sum_j\dot q_jp_j-L
$$

Lagrange's equations imply:

$$
\frac{dh}{dt}=-\frac{\partial L}{\partial t}
$$

Therefore $h$ is constant when $L$ has no explicit time dependence.

## Relation To Total Energy

If the coordinates are related to Cartesian positions without explicit time dependence and $V=V(q)$ is velocity independent, then $T$ is homogeneous of degree two in the generalized velocities. Euler's theorem gives:

$$
h=2T-(T-V)=T+V
$$

With time-dependent coordinates or more general velocity-dependent terms, $h$ may not equal the physical total energy.

## Relation To The Hamiltonian

The expression has the same algebraic form as the Legendre transform:

$$
H(q,p,t)=\sum_jp_j\dot q_j-L
$$

The distinction is in the variables: $h$ is written as a function of $(q,\dot q,t)$, while $H$ is written in terms of independent phase-space variables $(q,p,t)$ after solving for the velocities.

## Dissipation

For quadratic Rayleigh dissipation $\mathcal F$:

$$
\frac{dh}{dt}=-2\mathcal F-\frac{\partial L}{\partial t}
$$

When $h=E$ and $L$ is time independent, $2\mathcal F$ is the rate at which mechanical energy is lost.

## Common Confusions

- No explicit $t$ in $L$ means $h$ is conserved; it does not by itself prove $h=T+V$.
- A time-dependent coordinate choice can change the form and interpretation of $h$.
- Canonical energy and mechanical energy coincide in common systems, not by definition.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Conservation Laws](Conservation%20Laws.md)
- [Rayleigh Dissipation Function](Rayleigh%20Dissipation%20Function.md)
- [Goldstein Section 2.7](../Book%20Notes/Goldstein/Chapter%202/Energy%20Function%20and%20the%20Conservation%20of%20Energy.md)

<!-- semantic-edges
{"source":"Energy Function","relation":"PART_OF","target":"Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mechanics area of the vault.","confidence":0.85}
{"source":"Energy Function","relation":"MECHANICS_RELATED_TO","target":"Lagrangian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Energy Function with Lagrangian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Energy Function","relation":"MECHANICS_RELATED_TO","target":"Hamiltonian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Energy Function with Hamiltonian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Energy Function","relation":"MECHANICS_RELATED_TO","target":"Conservation Laws","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Energy Function with Conservation Laws in its discussion or related-note links.","confidence":0.75}
{"source":"Energy Function","relation":"MECHANICS_RELATED_TO","target":"Rayleigh Dissipation Function","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Energy Function with Rayleigh Dissipation Function in its discussion or related-note links.","confidence":0.75}
-->
