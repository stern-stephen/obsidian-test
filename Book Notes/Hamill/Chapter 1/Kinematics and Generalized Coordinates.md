# Kinematics and Generalized Coordinates

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 1.1-1.3, printed pages 3-9.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Constraints, Virtual Work, and Spaces](Constraints%20Virtual%20Work%20and%20Spaces.md)

## Reading Status

- Status: started
- Pages: 3-9
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill starts with familiar kinematics so the later generalized-coordinate machinery has a concrete base. The point is not to relearn elementary vector mechanics. The point is to see that the same physical motion can be described in many coordinate systems, and that analytical mechanics deliberately chooses coordinates suited to the system.

## 1.1 Kinematics

A particle is idealized as a mass with position vector $\mathbf{r}$. Its velocity and acceleration are:

$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$

$$
\mathbf{a}=\frac{d\mathbf{v}}{dt}
$$

The equation of motion gives acceleration as a function of position, velocity, and time. Solving it gives the trajectory:

$$
\mathbf{r}=\mathbf{r}(t)
$$

Hamill emphasizes that even simple motion can be described in different coordinate systems. For planar orbital motion, polar coordinates may be more natural than Cartesian coordinates:

$$
x=r\cos\theta
$$

$$
y=r\sin\theta
$$

This is an early example of a point transformation: one set of coordinates labels the same physical point as another set.

## 1.2 Generalized Coordinates

For a system of $N$ particles in three dimensions, a Cartesian description starts with $3N$ coordinates. Hamill writes these abstractly as:

$$
x_1,\ldots,x_n
$$

where:

$$
n=3N
$$

Generalized coordinates are denoted:

$$
q_1,\ldots,q_n
$$

or, after constraints have been used, by a smaller independent set.

Transformation equations relate generalized and Cartesian coordinates:

$$
x_i=x_i(q_1,\ldots,q_n,t)
$$

and, when invertible:

$$
q_i=q_i(x_1,\ldots,x_n,t)
$$

The inverse transformation requires a nonzero Jacobian determinant. This is Hamill's way of reminding the reader that a coordinate system must actually label configurations without degeneracy, at least locally.

## Minimal Independent Coordinates

The most important feature of generalized coordinates is independence. If a particle is constrained to a sphere of radius $a$, three Cartesian coordinates satisfy:

$$
x^2+y^2+z^2=a^2
$$

Only two independent parameters are needed. Two angular coordinates form a better generalized-coordinate description than three Cartesian coordinates plus a constraint.

Generalized coordinates do not need to be components of a vector. They can be:

- lengths;
- angles;
- coordinates along a curve or surface;
- parameters chosen for computational convenience;
- later, even momenta or abstract canonical coordinates.

This is why generalized coordinates are more than notation. They make constraints and symmetries part of the mathematical setup.

## 1.3 Generalized Velocity

Generalized velocities are time derivatives of generalized coordinates:

$$
\dot q_i=\frac{dq_i}{dt}
$$

If a Cartesian coordinate depends on generalized coordinates and time:

$$
x_i=x_i(q_1,q_2,q_3,t)
$$

then the velocity component follows from the chain rule:

$$
\dot x_i=\sum_k\frac{\partial x_i}{\partial q_k}\dot q_k+\frac{\partial x_i}{\partial t}
$$

The key identity Hamill derives is:

$$
\frac{\partial \dot x_i}{\partial \dot q_j}=\frac{\partial x_i}{\partial q_j}
$$

This relation is used later when converting d'Alembert's principle from Cartesian coordinates to generalized coordinates. In words: the way a Cartesian velocity depends on a generalized velocity mirrors the way the Cartesian coordinate depends on the generalized coordinate.

## Why This Matters Later

Once positions are expressed in generalized coordinates, velocities and kinetic energy can be generated systematically. This is what makes Lagrangian mechanics practical:

1. choose coordinates adapted to the constraints;
2. write the particle positions in terms of those coordinates;
3. compute velocities by differentiation;
4. build $T$, $V$, and $L=T-V$.

## Links To Concept Notes

- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Configuration Space](../../../Mechanics/Configuration%20Space.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

<!-- semantic-edges
{"source":"Hamill Section 1.2","relation":"INTRODUCES","target":"Generalized Coordinates","evidence_heading":"1.2 Generalized Coordinates","evidence_summary":"The note explains generalized coordinates as independent parameters related to Cartesian coordinates by transformation equations and chosen to suit constraints.","confidence":0.94}
{"source":"Generalized Coordinates","relation":"ENABLES","target":"Constraint Reduction","evidence_heading":"Minimal Independent Coordinates","evidence_summary":"The note uses a particle constrained to a sphere to show how independent generalized coordinates can replace redundant Cartesian coordinates plus a constraint equation.","confidence":0.9}
{"source":"Generalized Velocities","relation":"DERIVES_FROM","target":"Generalized Coordinates","evidence_heading":"1.3 Generalized Velocity","evidence_summary":"Generalized velocities are defined as time derivatives of generalized coordinates, and Cartesian velocities follow by the chain rule.","confidence":0.9}
-->
