# Classical Mechanics

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 8.1, printed pages 183-184.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Light and Electromagnetic Waves](Light%20and%20Electromagnetic%20Waves.md)

## Reading Status

- Status: finished
- Pages: 183-184
- Date started: 2026-07-09
- Date finished: 2026-07-09

## Setup Before Variation

The variational rule does not remove the need to model the system. Before applying it, one must identify the particles or other degrees of freedom, determine the independent motions, and supply the correct kinetic and potential energies.

For ordinary conservative mechanics, the Lagrangian is

$$
L=T-V
$$

and the action is

$$
A=\int_{t_1}^{t_2}L dt.
$$

The physical trajectory is stationary relative to infinitesimally nearby trajectories with the same nearby endpoints. Coopersmith describes this as the system continually balancing kinetic and potential energy, using rotating swing seats and a vertically thrown ball as intuitive examples.

## Constraints As Geometry

For a free system subject to time-independent constraints, the constraints can be absorbed into the geometry of configuration space. The motion then follows a geodesic: the straightest available path in that curved space.

This reframes constraint forces. Instead of solving explicitly for every force that keeps the system on its allowed surface, the allowed geometry is built into the coordinates and the path is varied within that geometry.

## Dissipation

Coopersmith qualifies the common statement that variational mechanics cannot treat dissipation. The obstacle is not dissipation in principle, but whether the dissipative effect can be represented by a suitable function. Rayleigh's dissipation function handles an important class of velocity-dependent friction forces and adds a nonzero term to the Lagrange equations.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Configuration Space](../../../Mechanics/Configuration%20Space.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Rayleigh Dissipation Function](../../../Mechanics/Rayleigh%20Dissipation%20Function.md)

<!-- semantic-edges
{"source":"Time-Independent Constraints","relation":"ENABLES","target":"Geodesic Motion","evidence_heading":"Constraints As Geometry","evidence_summary":"The note explains that static constraints can be absorbed into configuration-space geometry so free motion follows its straightest available paths.","confidence":0.9}
{"source":"Rayleigh Dissipation Function","relation":"EXTENDS","target":"Lagrangian Mechanics","evidence_heading":"Dissipation","evidence_summary":"A functional representation of velocity-dependent friction permits a dissipative term to be included in the Lagrange equations.","confidence":0.9}
-->
