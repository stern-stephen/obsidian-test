# Canonical Momentum

## Overview

Canonical momentum is the momentum conjugate to a generalized coordinate in Lagrangian and Hamiltonian mechanics.

## Definition

For coordinate $q_i$, the canonical momentum is:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

## Intuition

Canonical momentum is the phase-space partner of a coordinate. In simple Cartesian systems it equals mechanical momentum, but this equality can fail in generalized coordinates or in electromagnetic fields.

## Electromagnetic Example

For a charged particle:

$$
\mathbf{p} = m\dot{\mathbf{r}} + q\mathbf{A}
$$

so:

$$
m\dot{\mathbf{r}} = \mathbf{p} - q\mathbf{A}
$$

## Related Concepts

- [Goldstein Section 2.6](../Book%20Notes/Goldstein/Chapter%202/Conservation%20Theorems%20and%20Symmetry%20Properties.md)
- [Shankar: The Electromagnetic Lagrangian](../Book%20Notes/Shankar/Chapter%202/The%20Electromagnetic%20Lagrangian.md)
- [Shankar: Electromagnetic Force in the Hamiltonian Scheme](../Book%20Notes/Shankar/Chapter%202/The%20Electromagnetic%20Force%20in%20the%20Hamiltonian%20Scheme.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Electromagnetic Lagrangian](Electromagnetic%20Lagrangian.md)

<!-- semantic-edges
{"source":"Canonical Momentum","relation":"REQUIRES","target":"Generalized Coordinates","evidence_heading":"Overview","evidence_summary":"The note defines canonical momentum as the momentum conjugate to a generalized coordinate in Lagrangian and Hamiltonian mechanics.","confidence":0.9}
{"source":"Canonical Momentum","relation":"REQUIRES","target":"Lagrangian Mechanics","evidence_heading":"Definition","evidence_summary":"Canonical momentum is defined by differentiating the Lagrangian with respect to the generalized velocity.","confidence":0.95}
{"source":"Canonical Momentum","relation":"REQUIRES","target":"Phase Space","evidence_heading":"Intuition","evidence_summary":"The note describes canonical momentum as the phase-space partner of a coordinate.","confidence":0.9}
{"source":"Canonical Momentum","relation":"CONTRASTS_WITH","target":"Mechanical Momentum","evidence_heading":"Intuition","evidence_summary":"The note says canonical momentum equals mechanical momentum in simple Cartesian systems but can differ in generalized coordinates or electromagnetic fields.","confidence":0.9}
-->
