# Constraints, Virtual Work, and Spaces

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 1.4-1.8, printed pages 9-15.

Previous: [Kinematics and Generalized Coordinates](Kinematics%20and%20Generalized%20Coordinates.md)

Next: [Dynamics and Equations of Motion](Dynamics%20and%20Equations%20of%20Motion.md)

## Reading Status

- Status: started
- Pages: 9-15
- Date started: 2026-07-12
- Date finished:

## Purpose

These sections introduce the vocabulary that lets analytical mechanics avoid solving for every constraint force directly. Constraints determine which virtual displacements are allowed, virtual work defines generalized forces, and configuration space gives a geometric picture of the system's possible states.

## 1.4 Constraints

A constraint restricts the possible configurations or motions of a system. Each independent constraint reduces the number of degrees of freedom by one.

For example, a particle constrained to a plane can be described with two coordinates rather than three. A particle constrained to a sphere can be described by two angles rather than $x,y,z$ subject to:

$$
x^2+y^2+z^2=a^2
$$

A holonomic constraint can be written as an equation among coordinates and possibly time:

$$
f(q_1,\ldots,q_n,t)=0
$$

Holonomic constraints are especially convenient because they can often be built into the coordinate choice. Non-holonomic constraints involve inequalities, velocities, or nonintegrable differential relations; they require more care later.

## Degrees Of Freedom

Degrees of freedom count independent coordinates. If a system starts with $3N$ Cartesian coordinates and has $k$ independent holonomic constraints, then the number of degrees of freedom is:

$$
n=3N-k
$$

This count is not just bookkeeping. It tells how many independent equations of motion are needed after constraints have been accounted for.

## 1.5 Virtual Displacements

A virtual displacement is an imagined infinitesimal displacement compatible with the constraints at a fixed instant of time.

Two features matter:

- the displacement is compatible with the constraints;
- time is held fixed.

For generalized coordinates, the virtual displacement of a Cartesian coordinate is:

$$
\delta x_i=\sum_j\frac{\partial x_i}{\partial q_j}\delta q_j
$$

There is no $\partial x_i/\partial t$ term because virtual displacements freeze time. This distinguishes a virtual displacement from an actual displacement during time evolution.

## 1.6 Virtual Work And Generalized Force

Virtual work is the work done by forces during a virtual displacement:

$$
\delta W=\sum_i F_i\delta x_i
$$

Substituting the generalized-coordinate expression for $\delta x_i$ gives:

$$
\delta W=\sum_j Q_j\delta q_j
$$

The generalized force $Q_j$ is the coefficient of the generalized coordinate variation $\delta q_j$.

If $q_j$ is a distance, $Q_j$ may be an ordinary force component. If $q_j$ is an angle, $Q_j$ is torque-like. The unit of $Q_j$ depends on the unit of $q_j$ because $Q_j\delta q_j$ must have units of work.

## 1.7 Configuration Space

Configuration space is the space whose points represent complete configurations of the whole system.

For a system with $n$ degrees of freedom, a point in configuration space has coordinates:

$$
(q_1,\ldots,q_n)
$$

A path in configuration space represents a possible history of the system's configurations. The point is not usually a literal particle in physical space. It is a representation of the entire system.

## 1.8 Phase Space

Phase space adds momenta to coordinates. For each generalized coordinate $q_i$, phase space includes a conjugate momentum $p_i$:

$$
(q_i,p_i)
$$

For $n$ degrees of freedom, phase space is typically $2n$-dimensional. Hamill introduces this early because Hamiltonian mechanics later treats phase space as the natural setting for dynamics.

## What To Remember

- Constraints reduce independent degrees of freedom.
- Virtual displacements are fixed-time, constraint-compatible displacements.
- Generalized forces are defined by virtual work.
- Configuration space stores positions or configurations of the whole system.
- Phase space stores both generalized coordinates and conjugate momenta.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Configuration Space](../../../Mechanics/Configuration%20Space.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)

<!-- semantic-edges
{"source":"Holonomic Constraints","relation":"DETERMINES","target":"Degrees of Freedom","evidence_heading":"Degrees Of Freedom","evidence_summary":"The note states that each independent holonomic constraint reduces the number of independent coordinates by one.","confidence":0.92}
{"source":"Virtual Displacement","relation":"REQUIRES","target":"Fixed Time Variation","evidence_heading":"1.5 Virtual Displacements","evidence_summary":"The note emphasizes that virtual displacements freeze time and remain compatible with constraints.","confidence":0.9}
{"source":"Generalized Forces","relation":"REPRESENTS","target":"Virtual Work Coefficients","evidence_heading":"1.6 Virtual Work And Generalized Force","evidence_summary":"The note defines generalized forces as the coefficients of generalized coordinate variations in virtual work.","confidence":0.94}
{"source":"Configuration Space","relation":"CONTRASTS_WITH","target":"Phase Space","evidence_heading":"1.8 Phase Space","evidence_summary":"Configuration space represents complete configurations, while phase space adds conjugate momenta to generalized coordinates.","confidence":0.9}
-->
