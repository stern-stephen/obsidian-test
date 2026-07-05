# Hamiltonian Coordinates and Optical Analogy

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 7.1-7.3, printed pages 143-150.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Canonical Equations](Canonical%20Equations.md)

## Reading Status

- Status: started
- Pages: 143-150
- Date started: 2026-07-05
- Date finished:

## Big Ideas

- Hamilton's method deliberately increases the number of variables to reveal deeper structure.
- The optical analogy compares light rays and wavefronts with mechanical paths and action surfaces.
- Hamilton replaces generalized velocities with conjugate momenta.
- The conjugate momentum variables are treated as coordinates in the expanded phase-space description.

## Ask Less From More

Coopersmith frames Hamilton's advance as a strategic doubling. Lagrangian mechanics uses generalized coordinates and velocities, but Hamiltonian mechanics shifts to generalized coordinates and conjugate momenta. This increases the number of independent coordinates in the state description while producing a cleaner qualitative picture.

## Optical Motivation

Hamilton's mechanics grew out of his optical work. In geometrical optics, rays move through an optical system while surfaces of equal arrival time move forward. The ray direction is perpendicular to the wavefront. Hamilton saw that mechanics also has a minimum principle and that mechanical paths in configuration space can be treated analogously to optical rays.

In the mechanical analogy:

- Optical rays correspond to mechanical paths of the whole-system point.
- Optical wavefronts correspond to surfaces of common action.
- Fermat's least-time principle corresponds to Hamilton's least-action principle.

## From Velocity To Momentum

Hamilton's key transformation defines the conjugate momentum:

$$
p_i=\frac{\partial L}{\partial \dot{q}_i}
$$

The goal is then to rewrite the old velocity variables $\dot{q}_i$ as functions of $q_i$, $p_i$, and possibly $t$. The new description uses the paired variables:

$$
(q_i,p_i)
$$

Coopersmith emphasizes that the $p_i$ are called momenta because they often reduce to ordinary mechanical momentum, but their deeper role is as the conjugate partners of the $q_i$.

## Links To Concept Notes

- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Hamiltonian Mechanics","relation":"REFORMULATES","target":"Lagrangian Mechanics","evidence_heading":"From Velocity To Momentum","evidence_summary":"The note describes Hamilton's transformation from generalized velocities to conjugate momenta defined from the Lagrangian.","confidence":0.92}
{"source":"Canonical Momentum","relation":"REPRESENTS","target":"Conjugate Coordinate Partner","evidence_heading":"From Velocity To Momentum","evidence_summary":"Coopersmith treats p_i as the conjugate partner of q_i in the expanded Hamiltonian description.","confidence":0.9}
{"source":"Optical Analogy","relation":"MOTIVATES","target":"Hamiltonian Mechanics","evidence_heading":"Optical Motivation","evidence_summary":"The note explains that Hamilton used the geometry of rays and wavefronts to motivate mechanical action surfaces and paths.","confidence":0.88}
-->
