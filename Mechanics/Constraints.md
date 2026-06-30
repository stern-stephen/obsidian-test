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

For an internal holonomic constraint, the word "eliminated" means eliminated from the equations for the allowed motion, not physically absent. If the virtual displacement is compatible with the constraint, the virtual change of the constraint equation is zero:

$$
\delta f=\sum_i\frac{\partial f}{\partial\mathbf{r}_i}\cdot\delta\mathbf{r}_i=0
$$

The corresponding internal constraint force therefore contributes no virtual work in the allowed directions. This is why generalized coordinates can build in ideal internal constraints without needing to solve for the constraint forces first.

## Lagrange Multipliers

When it is inconvenient to eliminate holonomic constraints $f_\alpha(q,t)=0$, retain the dependent coordinates and use an augmented Lagrangian:

$$
L'=L+\sum_\alpha\lambda_\alpha f_\alpha
$$

The coordinate equations become:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_k}\right)-\frac{\partial L}{\partial q_k}=-\sum_\alpha\lambda_\alpha\frac{\partial f_\alpha}{\partial q_k}
$$

Together with the constraint equations, these determine the motion and multipliers. The multiplier terms represent generalized constraint forces, with their signs depending on the convention used for each constraint function.

## Common Confusions

- A constraint on velocity is not necessarily nonholonomic; integrability is the deciding issue.
- Eliminating a constraint force from the motion equations does not mean the force is zero.
- A time-dependent constraint can do work during actual motion even if its force does no virtual work.

## Related Concepts

- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Virtual Work and D'Alembert's Principle](Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Goldstein Section 1.3](../Book%20Notes/Goldstein/Chapter%201/Constraints.md)
- [Goldstein Section 2.4](../Book%20Notes/Goldstein/Chapter%202/Extending%20Hamilton%27s%20Principle%20to%20Systems%20with%20Constraints.md)
- [Coopersmith Section 4.8](../Book%20Notes/Coopersmith/Chapter%204/Constraints%20and%20Kinematical%20Conditions.md)

<!-- semantic-edges
{"source":"Constraints","relation":"DETERMINES","target":"Degrees of Freedom","evidence_heading":"Holonomic Constraints","evidence_summary":"The note gives the degree-of-freedom count n=3N-k for N particles subject to k independent holonomic constraints.","confidence":0.95}
{"source":"Holonomic Constraints","relation":"ENABLES","target":"Generalized Coordinates","evidence_heading":"Holonomic Constraints","evidence_summary":"Independent generalized coordinates can be chosen so that the holonomic constraints are incorporated into the coordinate map.","confidence":0.9}
{"source":"Ideal Constraints","relation":"ENABLES","target":"D'Alembert's Principle","evidence_heading":"Ideal Constraints","evidence_summary":"The note says ideal constraints do no net virtual work, which allows constraint forces to be eliminated through D'Alembert's principle.","confidence":0.95}
{"source":"Lagrange Multipliers","relation":"REPRESENTS","target":"Generalized Constraint Forces","evidence_heading":"Lagrange Multipliers","evidence_summary":"The multiplier terms in the augmented Lagrangian represent generalized constraint forces, with signs depending on the chosen constraint convention.","confidence":0.9}
-->
