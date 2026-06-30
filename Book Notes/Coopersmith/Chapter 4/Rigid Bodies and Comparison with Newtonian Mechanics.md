# Rigid Bodies and Comparison with Newtonian Mechanics

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 4.3-4.4, printed pages 63-68.

Previous: [Introduction and Non-Interacting Particles](Introduction%20and%20Non-Interacting%20Particles.md)

Next: [Virtual Displacements](Virtual%20Displacements.md)

## Reading Status

- Status: started
- Pages: 63-68
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- A rigid body is not just a collection of particles with a fixed shape; it is a constrained system whose internal reaction forces maintain that shape.
- Virtual translations and rotations must move the rigid body as a whole, so the virtual displacements do not excite internal deformation forces.
- The principle of virtual work recovers the familiar rigid-body equilibrium conditions: zero resultant force and zero resultant moment.
- Coopersmith then separates net forces into applied and constraint forces to explain why the standard virtual-work condition contains only applied forces.

## Rigid Translations

For a virtual translation of a rigid body, each particle has the same virtual displacement:

$$
\delta\mathbf{r}_i=\delta\mathbf{r}
$$

The virtual-work condition becomes:

$$
\delta\mathbf{r}\cdot\sum_{i=1}^{N}\mathbf{F}_i=0
$$

Since the translation is arbitrary and nonzero, equilibrium requires:

$$
\sum_{i=1}^{N}\mathbf{F}_i=0
$$

## Rigid Rotations

For a virtual rotation about a common axis with unit vector $\mathbf{U}$:

$$
\delta\mathbf{r}_i=\delta\theta\mathbf{U}\times\mathbf{r}_i
$$

The virtual work from force $\mathbf{F}_i$ can be written in terms of the moment:

$$
\delta\omega_i=\delta\theta\mathbf{U}\cdot(\mathbf{r}_i\times\mathbf{F}_i)
$$

Thus equilibrium also requires the resultant moment to vanish:

$$
\sum_{i=1}^{N}\mathbf{r}_i\times\mathbf{F}_i=0
$$

## Applied and Constraint Forces

Coopersmith writes the net force on each particle as the sum of applied and constraint parts:

$$
\mathbf{F}_i^{net}=\mathbf{F}_i^{appl}+\mathbf{F}_i^{cons}
$$

Newtonian equilibrium implies:

$$
\sum_i\mathbf{F}_i^{net}\cdot\delta\mathbf{r}_i=0
$$

If the virtual displacements are compatible with the constraints, then the constraint forces do no total virtual work:

$$
\sum_i\mathbf{F}_i^{cons}\cdot\delta\mathbf{r}_i=0
$$

The standard principle of virtual work follows:

$$
\sum_i\mathbf{F}_i^{appl}\cdot\delta\mathbf{r}_i=0
$$

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Center of Mass](../../../Mechanics/Center%20of%20Mass.md)

<!-- semantic-edges
{"source":"Principle of Virtual Work","relation":"DERIVES","target":"Zero Resultant Force","evidence_heading":"Rigid Translations","evidence_summary":"A rigid virtual translation makes the virtual-work condition imply that the resultant external force is zero.","confidence":0.9}
{"source":"Principle of Virtual Work","relation":"DERIVES","target":"Zero Resultant Moment","evidence_heading":"Rigid Rotations","evidence_summary":"A rigid virtual rotation rewrites virtual work in terms of moments and implies that the resultant moment is zero.","confidence":0.9}
-->
