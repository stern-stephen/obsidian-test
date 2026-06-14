# Constraints

## Overview

A constraint restricts the configurations or motions available to a mechanical system. It reduces the independent degrees of freedom but may introduce forces that are not known before solving the motion.

## Holonomic Constraints

A holonomic constraint can be written as a relation among coordinates and possibly time:

$$
f(\mathbf{r}_1,\ldots,\mathbf{r}_N,t)=0
$$

If a system of $N$ particles has $k$ independent holonomic constraints, its number of degrees of freedom is:

$$
n=3N-k
$$

Independent generalized coordinates can then incorporate the constraints:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

## Nonholonomic Constraints

Nonholonomic constraints cannot be reduced to coordinate-only equations. Common forms include:

- Inequalities that define one-sided contact.
- Nonintegrable differential relations among coordinate changes.
- Constraints involving higher derivatives.

Rolling without slipping is a standard example. Although it produces relations among velocities, those relations may not integrate into fixed relations among the coordinates.

## Time Dependence

- Scleronomous: no explicit time dependence.
- Rheonomous: explicit time dependence.

This classification is independent of whether a constraint is holonomic.

## Ideal Constraints

An ideal constraint does no net virtual work:

$$
\sum_i\mathbf{f}_i\cdot\delta\mathbf{r}_i=0
$$

This property allows constraint forces to be eliminated through D'Alembert's principle.

## Common Confusions

- A constraint on velocity is not necessarily nonholonomic; integrability is the deciding issue.
- Eliminating a constraint force from the motion equations does not mean the force is zero.
- A time-dependent constraint can do work during actual motion even if its force does no virtual work.

## Related Concepts

- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Virtual Work and D'Alembert's Principle](Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Goldstein Section 1.3](../Book%20Notes/Goldstein/Chapter%201/Constraints.md)
