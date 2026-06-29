# Generalized Coordinates

## Overview

Generalized coordinates are variables chosen to describe the configuration of a system.

## Definition

A system with $n$ degrees of freedom can be described by coordinates:

$$
q_1,\ldots,q_n
$$

These coordinates may be distances, angles, normal modes, or other variables suited to the constraints.

For $N$ particles subject to $k$ independent holonomic constraints, one can choose:

$$
n=3N-k
$$

independent generalized coordinates and write:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

The transformation then contains the holonomic constraints implicitly.

## Intuition

The point of generalized coordinates is to describe only the actual degrees of freedom. For constrained systems, this can remove constraint forces from the equations.

The configuration of an $n$-degree-of-freedom system is one point in [Configuration Space](Configuration%20Space.md), not necessarily a point in ordinary physical space.

## Examples

- A pendulum can be described by its angle instead of Cartesian coordinates.
- A particle in polar coordinates can be described by $r$ and $\theta$.
- A rigid rotor can be described using angular coordinates.

Generalized coordinates are also useful without constraints. Spherical coordinates, for example, adapt naturally to a central-force problem.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Canonical Momentum](Canonical%20Momentum.md)
- [Constraints](Constraints.md)
- [Configuration Space](Configuration%20Space.md)
- [Goldstein Section 1.3](../Book%20Notes/Goldstein/Chapter%201/Constraints.md)
- [Coopersmith Sections 3.1-3.4](../Book%20Notes/Coopersmith/Chapter%203/Chapter%20Overview.md)
- [Coopersmith Section 4.7](../Book%20Notes/Coopersmith/Chapter%204/Generalized%20Coordinates.md)

<!-- semantic-edges
{"source":"Generalized Coordinates","relation":"PART_OF","target":"Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mechanics area of the vault.","confidence":0.85}
{"source":"Generalized Coordinates","relation":"MECHANICS_RELATED_TO","target":"Configuration Space","evidence_heading":"Intuition","evidence_summary":"The note explicitly connects Generalized Coordinates with Configuration Space in its discussion or related-note links.","confidence":0.75}
{"source":"Generalized Coordinates","relation":"MECHANICS_RELATED_TO","target":"Lagrangian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Generalized Coordinates with Lagrangian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Generalized Coordinates","relation":"MECHANICS_RELATED_TO","target":"Euler-Lagrange Equations","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Generalized Coordinates with Euler-Lagrange Equations in its discussion or related-note links.","confidence":0.75}
{"source":"Generalized Coordinates","relation":"MECHANICS_RELATED_TO","target":"Canonical Momentum","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Generalized Coordinates with Canonical Momentum in its discussion or related-note links.","confidence":0.75}
-->
