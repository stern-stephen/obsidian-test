# Configuration Space

## Overview

Configuration space is the abstract space of possible configurations of a system. Each point represents the whole system at one instant.

## Definition

For generalized coordinates:

$$
q_1,\ldots,q_n
$$

a configuration is the point:

$$
(q_1,\ldots,q_n)
$$

The dimension of configuration space is the number of independent degrees of freedom.

## Intuition

Ordinary space locates a particle. Configuration space locates an entire system. A two-particle system in ordinary three-dimensional space has six configuration coordinates before constraints are imposed.

As the system evolves, its configuration point traces a curve in configuration space. Variational mechanics studies nearby allowed curves or nearby allowed displacements in this space.

## Common Confusions

- Configuration space is not usually ordinary physical space.
- A curve in configuration space represents the history of the whole system, not necessarily the path of one particle.
- Constraints reduce the allowed region or surface in configuration space.

## Related Concepts

- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Phase Space](Phase%20Space.md)
- [Action Principle](Action%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Coopersmith Section 3.5](../Book%20Notes/Coopersmith/Chapter%203/Configuration%20Space%20and%20Invariants.md)

<!-- semantic-edges
{"source":"Configuration Space","relation":"REPRESENTS","target":"System Configuration","evidence_heading":"Overview","evidence_summary":"The note defines configuration space as the abstract space of possible configurations, with each point representing the whole system at one instant.","confidence":0.95}
{"source":"Configuration Space","relation":"REQUIRES","target":"Generalized Coordinates","evidence_heading":"Definition","evidence_summary":"The note defines a configuration-space point using the generalized coordinates q_1 through q_n.","confidence":0.95}
{"source":"Degrees of Freedom","relation":"DETERMINES","target":"Configuration Space","evidence_heading":"Definition","evidence_summary":"The note says the dimension of configuration space is the number of independent degrees of freedom.","confidence":0.9}
{"source":"Curve in Configuration Space","relation":"REPRESENTS","target":"System History","evidence_heading":"Common Confusions","evidence_summary":"The note clarifies that a curve in configuration space represents the history of the whole system rather than the path of one particle.","confidence":0.9}
{"source":"Variational Mechanics","relation":"REQUIRES","target":"Configuration Space","evidence_heading":"Intuition","evidence_summary":"The note says variational mechanics studies nearby allowed curves or displacements in configuration space as the system evolves.","confidence":0.85}
-->
