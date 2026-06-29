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
{"source":"Cyclic Coordinates","relation":"PART_OF","target":"Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mechanics area of the vault.","confidence":0.85}
{"source":"Cyclic Coordinates","relation":"MECHANICS_RELATED_TO","target":"Conservation Laws","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Cyclic Coordinates with Conservation Laws in its discussion or related-note links.","confidence":0.75}
{"source":"Cyclic Coordinates","relation":"MECHANICS_RELATED_TO","target":"Lagrangian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Cyclic Coordinates with Lagrangian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Cyclic Coordinates","relation":"MECHANICS_RELATED_TO","target":"Hamiltonian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Cyclic Coordinates with Hamiltonian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Cyclic Coordinates","relation":"MECHANICS_RELATED_TO","target":"Symmetries and Their Consequences","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Cyclic Coordinates with Symmetries and Their Consequences in its discussion or related-note links.","confidence":0.75}
-->
