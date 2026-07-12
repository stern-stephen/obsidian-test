# Invariance and Problems

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 3.8-3.9, printed pages 86-90.

Previous: [Nonholonomic Constraints and Virtual Work](Nonholonomic%20Constraints%20and%20Virtual%20Work.md)

## Reading Status

- Status: started
- Pages: 86-90
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill ends Chapter 3 by explaining why Lagrange's equations can be written in any convenient generalized coordinates. The equations retain their form under point transformations, even though the individual coordinate equations may look very different.

## 3.8 Point Transformations

A point transformation maps one set of generalized coordinates to another:

$$
q_i=q_i(s_1,\ldots,s_n,t)
$$

Each point in $q$-space corresponds to a point in $s$-space. The physical path in configuration space is represented by different coordinate labels, but it is the same path.

## Invariance Of Lagrange's Equations

Hamilton's principle selects the true path by stationarity of the action:

$$
\delta\int Ldt=0
$$

This statement does not depend on which coordinate labels are used. If a path is stationary in one coordinate system, the transformed path is stationary in the new coordinate system.

Thus Lagrange's equations retain their form:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot s_i}\right)-\frac{\partial L}{\partial s_i}=0
$$

after a point transformation.

## Covariance Rather Than Identical Equations

Hamill notes that "invariant" can be slightly misleading if it suggests that each equation looks the same. The equations are better described as covariant: the complete set of equations transforms into an equivalent complete set.

The numerical value of the Lagrangian for a physical state is the same, but its functional form can change dramatically.

## Cartesian And Polar Example

Hamill illustrates with a Lagrangian written in Cartesian coordinates:

$$
L=\frac{1}{2}\dot x^2+\frac{1}{2}\dot y^2+\frac{1}{\sqrt{x^2+y^2}}
$$

Using:

$$
x=r\cos\theta
$$

$$
y=r\sin\theta
$$

the same system is described by:

$$
L=\frac{1}{2}\dot r^2+\frac{1}{2}r^2\dot\theta^2+\frac{1}{r}
$$

The Cartesian equations and polar equations look different, but they describe the same motion. In polar form, the cyclic coordinate $\theta$ immediately reveals angular momentum conservation:

$$
\frac{d}{dt}(r^2\dot\theta)=0
$$

## Why This Matters

The invariance or covariance of Lagrange's equations justifies the practical power of generalized coordinates. The physicist is free to choose coordinates that match the geometry, constraints, and symmetries of the problem.

This is also a conceptual bridge toward later theories where invariance under transformations becomes a guiding principle.

## 3.9 Problems

The problems practice:

- deriving the usual Lagrange equations from the Nielsen form;
- applying d'Alembert's principle to equilibrium;
- proving covariance under point transformations;
- working with constraints and multipliers;
- interpreting virtual work and generalized forces.

## Notes For Future Exercise Answers

- For point-transformation problems, show both the coordinate transformation and the velocity transformation.
- For multiplier problems, state the constraint function and the sign convention before interpreting $\lambda$.
- For virtual-work equilibrium problems, separate impressed forces from reaction forces.
- Keep problem statements short and use the problem numbers as references.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)

<!-- semantic-edges
{"source":"Point Transformations","relation":"ENABLES","target":"Coordinate Covariance of Lagrange's Equations","evidence_heading":"Invariance Of Lagrange's Equations","evidence_summary":"The note explains that Hamilton's principle is coordinate-independent, so Lagrange's equations retain their form after point transformations.","confidence":0.9}
{"source":"Generalized Coordinates","relation":"ENABLES","target":"Convenient Coordinate Choice","evidence_heading":"Why This Matters","evidence_summary":"The note says covariance under point transformations justifies choosing coordinates suited to geometry, constraints, and symmetries.","confidence":0.88}
-->
