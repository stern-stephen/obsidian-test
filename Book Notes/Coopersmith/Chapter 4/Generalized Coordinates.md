# Generalized Coordinates

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 4.7, printed pages 71-74.

Previous: [Virtual Displacements](Virtual%20Displacements.md)

Next: [Constraints and Kinematical Conditions](Constraints%20and%20Kinematical%20Conditions.md)

## Reading Status

- Status: started
- Pages: 71-74
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Coopersmith generalizes virtual work from particles, forces, and Cartesian displacements to things, generalized forces, and generalized motions.
- A generalized coordinate can be any quantifiable variable that characterizes the system.
- A generalized force is whatever pairs with the generalized coordinate variation to give energy.
- The number of degrees of freedom is the smallest number of independent coordinates needed to describe the system.

## Generalized Virtual Work

The ordinary product $\mathbf{F}_i\cdot\delta\mathbf{r}_i$ is replaced by generalized force-coordinate products:

$$
\sum_i Q_i\delta q_i=0
$$

The coordinate $q_i$ need not be a length. It may be an angle, volume, charge, capacitance-related variable, field parameter, strain, pressure variable, or another system coordinate.

The paired generalized force $Q_i$ has whatever units are needed so that $Q_i\delta q_i$ has units of energy.

## Degrees Of Freedom

Coopersmith emphasizes that choosing generalized coordinates is partly an art. A coordinate choice with redundant variables is allowed, but the variables will be linked by constraint equations. The smallest independent set gives the system's degrees of freedom.

For the pivoting-bar example, three masses suggest three vertical displacements, but the rigid bar leaves only one independent virtual motion: the rotation about the pivot.

## Why This Matters

The move to generalized coordinates is the step that makes virtual work a general variational method rather than a trick for force diagrams. The cost is that the generalized force $Q$ may be less physically transparent than an ordinary force; the benefit is that the same scalar stationarity condition applies across many systems.

## Links To Concept Notes

- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

<!-- semantic-edges
{"source":"Generalized Coordinates","relation":"GENERALIZES","target":"Cartesian Coordinates","evidence_heading":"Generalized Virtual Work","evidence_summary":"Coopersmith replaces ordinary particle displacements with generalized motions described by arbitrary system coordinates.","confidence":0.9}
{"source":"Generalized Force","relation":"REQUIRES","target":"Generalized Coordinate","evidence_heading":"Generalized Virtual Work","evidence_summary":"A generalized force is defined by pairing with a generalized coordinate variation so the product has units of energy.","confidence":0.95}
{"source":"Degrees of Freedom","relation":"REPRESENTS","target":"Independent Generalized Coordinates","evidence_heading":"Degrees Of Freedom","evidence_summary":"The smallest independent coordinate set gives the system's degrees of freedom.","confidence":0.9}
-->
