# Constraints

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.3, printed pages 12-16.

Previous: [Mechanics of a System of Particles](Mechanics%20of%20a%20System%20of%20Particles.md)

Next: [D'Alembert's Principle and Lagrange's Equations](DAlemberts%20Principle%20and%20Lagranges%20Equations.md)

## Reading Status

- Status: started
- Pages: 12-16
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- Constraints both reduce the independent motion and introduce unknown forces.
- Holonomic constraints can be built into a smaller set of generalized coordinates.
- Nonholonomic constraints cannot generally be reduced to relations among coordinates alone.
- Time dependence provides a separate classification: scleronomous versus rheonomous.

## Classification

A holonomic constraint can be written as:

$$
f(\mathbf{r}_1,\ldots,\mathbf{r}_N,t)=0
$$

Examples include fixed distances in a rigid body and motion restricted to a curve or surface.

Nonholonomic constraints include inequalities and nonintegrable differential relations. Goldstein's rolling disk provides the standard example:

$$
dx-a\sin\theta d\phi=0
$$

$$
dy+a\cos\theta d\phi=0
$$

These relations constrain velocities but cannot be integrated into coordinate-only equations.

- Scleronomous constraints have no explicit time dependence.
- Rheonomous constraints depend explicitly on time.

## Degrees Of Freedom

A free system of $N$ particles has $3N$ degrees of freedom. If there are $k$ independent holonomic constraints, the system has:

$$
n=3N-k
$$

degrees of freedom.

Introduce independent generalized coordinates $q_1,\ldots,q_n$ through:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

These equations incorporate the holonomic constraints implicitly.

## Why Generalized Coordinates Help

Generalized coordinates need not be Cartesian coordinates, lengths, or even components of vectors. They are any independent variables that describe the allowed configurations.

Examples:

- The two angles of a double pendulum.
- Latitude and longitude for motion on a sphere.
- Spherical coordinates for a central-force problem even when there is no constraint.
- Mode amplitudes in an expansion.

## The Two Difficulties Created By Constraints

1. The original Cartesian coordinates are no longer independent.
2. The constraint forces are not known in advance.

Generalized coordinates solve the first problem for holonomic systems. D'Alembert's principle addresses the second by eliminating ideal constraint forces from the equations.

## Common Confusions

- A velocity constraint is not automatically nonholonomic; the key question is whether it can be integrated into a coordinate relation.
- Generalized coordinates are useful even when no physical constraint is present.
- Rheonomous and nonholonomic describe different properties.
- Eliminating constraint forces simplifies the motion equations but usually prevents those forces from being found directly.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)

<!-- semantic-edges
{"source":"Goldstein Section 1.3","relation":"INTRODUCES","target":"Constraint Classification","evidence_heading":"Big Ideas","evidence_summary":"Classifies constraints by integrability and time dependence: holonomic, nonholonomic, scleronomous, and rheonomous.","confidence":0.91}
{"source":"Goldstein Section 1.3","relation":"MOTIVATES","target":"Generalized Coordinates","evidence_heading":"Degrees Of Freedom","evidence_summary":"Independent generalized coordinates can incorporate holonomic constraints implicitly into the coordinate transformation.","confidence":0.89}
{"source":"Nonholonomic Constraints","relation":"CONTRASTS_WITH","target":"Holonomic Constraints","evidence_heading":"Classification","evidence_summary":"Nonholonomic constraints include inequalities and nonintegrable differential relations rather than coordinate-only equations.","confidence":0.89}
{"source":"Constraints","relation":"DETERMINES","target":"Degrees of Freedom Count","evidence_heading":"Degrees Of Freedom","evidence_summary":"For N particles with k independent holonomic constraints, Goldstein counts n = 3N - k degrees of freedom.","confidence":0.9}
{"source":"Ideal Constraint Force Problem","relation":"MOTIVATES","target":"D'Alembert's Principle","evidence_heading":"The Two Difficulties Created By Constraints","evidence_summary":"D'Alembert's principle is introduced as the method for eliminating unknown ideal constraint forces from the motion equations.","confidence":0.9}
-->
