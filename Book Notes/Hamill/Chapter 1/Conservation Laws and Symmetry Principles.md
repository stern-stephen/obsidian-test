# Conservation Laws and Symmetry Principles

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 1.11, printed pages 25-40.

Previous: [Dynamics and Equations of Motion](Dynamics%20and%20Equations%20of%20Motion.md)

Next: [Problems](Problems.md)

## Reading Status

- Status: started
- Pages: 25-40
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill closes Chapter 1 by connecting conservation laws to symmetry. This is a first pass at the idea behind Noether's theorem: if the system is unchanged by a continuous transformation, there is a corresponding conserved quantity.

## Generalized Momentum

The generalized momentum conjugate to $q_i$ is:

$$
p_i=\frac{\partial L}{\partial \dot q_i}
$$

For a free particle in Cartesian coordinates, this reduces to ordinary linear momentum. For a rotating wheel, differentiating with respect to angular velocity gives angular momentum. The formula therefore unifies familiar momenta under one definition.

## Cyclic Coordinates

A coordinate is cyclic, or ignorable, if it does not appear explicitly in the Lagrangian.

If $q_i$ is cyclic:

$$
\frac{\partial L}{\partial q_i}=0
$$

Lagrange's equation becomes:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)=0
$$

Thus:

$$
p_i=\frac{\partial L}{\partial \dot q_i}=\text{constant}
$$

The generalized momentum conjugate to a cyclic coordinate is conserved.

## Symmetry Interpretation

If changing $q_i$ does not change $L$, then the system is invariant under that coordinate change. This is a symmetry.

Examples:

- translational symmetry corresponds to conservation of linear momentum;
- rotational symmetry corresponds to conservation of angular momentum;
- temporal symmetry corresponds to conservation of an energy-like quantity.

Hamill states the broad idea: every symmetry gives a corresponding constant of motion. He flags this as essentially Noether's theorem, though the full theorem is not developed here.

## Linear Momentum

Conservation of linear momentum follows from homogeneity of space. If shifting every particle by the same infinitesimal displacement leaves the Lagrangian unchanged, then:

$$
\delta L=0
$$

The argument leads to:

$$
\frac{d\mathbf{P}_{\text{tot}}}{dt}=0
$$

so total linear momentum is conserved.

Hamill also shows how this symmetry argument relates back to Newton's second and third laws when the kinetic energy is coordinate independent and the forces come from the potential.

## Angular Momentum

Conservation of angular momentum follows from isotropy of space. If rotating the system does not change the Lagrangian, then the corresponding rotational generalized momentum is conserved.

For a particle, angular momentum has the familiar form:

$$
\mathbf{l}=\mathbf{r}\times\mathbf{p}
$$

The symmetry viewpoint makes the law less tied to a particular coordinate calculation: it expresses the fact that no direction in space is preferred.

## Energy Function

Time-translation symmetry leads to conservation of the energy function:

$$
h=\sum_i\dot q_i\frac{\partial L}{\partial \dot q_i}-L
$$

If the Lagrangian has no explicit time dependence:

$$
\frac{\partial L}{\partial t}=0
$$

then:

$$
\frac{dh}{dt}=0
$$

For many common systems, $h$ equals total mechanical energy $T+V$, but Hamill warns that this equality depends on assumptions about the kinetic energy, potential energy, and coordinate choice. Conservation of $h$ is the more general Lagrangian statement.

## What To Remember

- Generalized momentum is conjugate to a generalized coordinate.
- A cyclic coordinate has conserved conjugate momentum.
- Symmetry means the Lagrangian is invariant under a continuous change.
- Spatial homogeneity gives linear momentum conservation.
- Spatial isotropy gives angular momentum conservation.
- Time homogeneity gives conservation of the energy function.
- Conserved canonical momentum need not always look like ordinary mechanical momentum.

## Links To Concept Notes

- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Symmetries](../../../Mechanics/Symmetries.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)

<!-- semantic-edges
{"source":"Cyclic Coordinates","relation":"DETERMINES","target":"Conserved Canonical Momentum","evidence_heading":"Cyclic Coordinates","evidence_summary":"The note derives conservation of the conjugate momentum when the Lagrangian has no explicit dependence on a coordinate.","confidence":0.94}
{"source":"Translational Symmetry","relation":"DETERMINES","target":"Conservation of Linear Momentum","evidence_heading":"Linear Momentum","evidence_summary":"The note connects homogeneity of space with conservation of total linear momentum.","confidence":0.9}
{"source":"Rotational Symmetry","relation":"DETERMINES","target":"Conservation of Angular Momentum","evidence_heading":"Angular Momentum","evidence_summary":"The note connects isotropy of space with conservation of angular momentum.","confidence":0.9}
{"source":"Time-Independent Lagrangian","relation":"DETERMINES","target":"Energy Function Conservation","evidence_heading":"Energy Function","evidence_summary":"The note states that the energy function is conserved when the Lagrangian has no explicit time dependence.","confidence":0.92}
-->
