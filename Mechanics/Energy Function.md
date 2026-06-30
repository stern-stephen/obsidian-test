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
{"source":"Time-Independent Lagrangian","relation":"DETERMINES","target":"Energy Function Conservation","evidence_heading":"Definition","evidence_summary":"The note derives dh/dt = -partial L/partial t, so the energy function is constant when the Lagrangian has no explicit time dependence.","confidence":0.95}
{"source":"Energy Function","relation":"CONTRASTS_WITH","target":"Total Mechanical Energy","evidence_heading":"Overview","evidence_summary":"The note says the Lagrangian energy function often equals total mechanical energy, but those are logically separate facts.","confidence":0.9}
{"source":"Energy Function","relation":"REPRESENTS","target":"Legendre Transform","evidence_heading":"Relation To The Hamiltonian","evidence_summary":"The note says the energy function has the same algebraic form as the Legendre transform, while differing from the Hamiltonian by its variables.","confidence":0.9}
-->
