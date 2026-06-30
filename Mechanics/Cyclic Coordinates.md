# Cyclic Coordinates

## Overview

A cyclic coordinate is a generalized coordinate that does not appear explicitly in the Lagrangian or Hamiltonian.

## Definition

If:

$$
\frac{\partial L}{\partial q_i} = 0
$$

then $q_i$ is cyclic in the Lagrangian description.

## Key Result

The conjugate momentum is conserved:

$$
\dot{p}_i = 0,\qquad p_i=\frac{\partial L}{\partial\dot q_i}
$$

## Intuition

If the dynamics does not depend on a coordinate, then shifting that coordinate changes nothing physical. The associated momentum is conserved.

The coordinate must be independent. If an apparently absent coordinate is tied to others by an uneliminated constraint, its conjugate momentum need not be conserved.

## Related Concepts

- [Conservation Laws](Conservation%20Laws.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Symmetries and Their Consequences](../Book%20Notes/Shankar/Chapter%202/Symmetries%20and%20Their%20Consequences.md)
- [Goldstein Section 2.6](../Book%20Notes/Goldstein/Chapter%202/Conservation%20Theorems%20and%20Symmetry%20Properties.md)

<!-- semantic-edges
{"source":"Cyclic Coordinates","relation":"DETERMINES","target":"Conserved Momentum","evidence_heading":"Key Result","evidence_summary":"The note states that when a coordinate is cyclic, its conjugate momentum is conserved.","confidence":0.95}
{"source":"Cyclic Coordinates","relation":"REPRESENTS","target":"Coordinate-Shift Symmetry","evidence_heading":"Intuition","evidence_summary":"If the dynamics does not depend on a coordinate, shifting that coordinate changes nothing physical.","confidence":0.9}
{"source":"Cyclic Coordinates","relation":"REQUIRES","target":"Independent Coordinates","evidence_heading":"Intuition","evidence_summary":"The note warns that the coordinate must be independent; if it is tied to others by an uneliminated constraint, its conjugate momentum need not be conserved.","confidence":0.9}
{"source":"Cyclic Coordinates","relation":"ENABLES","target":"Conservation Laws","evidence_heading":"Key Result","evidence_summary":"A cyclic coordinate gives an immediate conservation law for the corresponding conjugate momentum.","confidence":0.9}
-->
