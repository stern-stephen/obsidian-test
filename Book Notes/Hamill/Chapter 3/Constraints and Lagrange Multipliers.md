# Constraints and Lagrange Multipliers

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 3.5, printed pages 77-81.

Previous: [Hamiltons Principle and Variational Derivation](Hamiltons%20Principle%20and%20Variational%20Derivation.md)

Next: [Nonholonomic Constraints and Virtual Work](Nonholonomic%20Constraints%20and%20Virtual%20Work.md)

## Reading Status

- Status: started
- Pages: 77-81
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill now uses the multiplier method to keep constrained coordinates in the problem. This is useful because the multipliers are not merely algebraic tools: in mechanics they identify generalized forces of constraint.

## Holonomic Constraints

Suppose a system is described by $n$ generalized coordinates:

$$
q_1,\ldots,q_n
$$

and has $k$ holonomic constraints:

$$
f_j(q_1,\ldots,q_n)=0
$$

for:

$$
j=1,\ldots,k
$$

One could use these constraints to reduce the number of coordinates to $n-k$. Instead, Hamill keeps all $n$ coordinates and adds multipliers.

## Variation Of Constraints

For each constraint:

$$
\delta f_j=\sum_i\frac{\partial f_j}{\partial q_i}\delta q_i=0
$$

Multiplying by an undetermined multiplier $\lambda_j$ and summing over constraints gives a zero quantity that can be added to the variation of the action:

$$
\sum_j\lambda_j\sum_i\frac{\partial f_j}{\partial q_i}\delta q_i=0
$$

This is the mechanics version of the multiplier method from Chapter 2.

## Equations With Multipliers

Adding the constraint variations to Hamilton's-principle variation gives:

$$
\int_{t_1}^{t_2}\sum_i\left[\frac{\partial L}{\partial q_i}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)+\sum_j\lambda_j\frac{\partial f_j}{\partial q_i}\right]\delta q_i dt=0
$$

The resulting equations are:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=\sum_j\lambda_j\frac{\partial f_j}{\partial q_i}
$$

Together with the $k$ constraint equations, these give $n+k$ equations for the $n$ coordinates and $k$ multipliers.

## Constraint Forces

Compare the multiplier equation with the Nielsen form that separates conservative generalized forces from nonconservative or constraint forces:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=Q_i^{\text{constraint}}
$$

Therefore:

$$
Q_i^{\text{constraint}}=\sum_j\lambda_j\frac{\partial f_j}{\partial q_i}
$$

This is the key physical interpretation: multiplier terms give generalized forces of constraint.

## Rolling Disk Example

Hamill applies the method to a disk rolling without slipping down an inclined plane. Use:

- $s$ for distance along the plane;
- $\theta$ for disk rotation;
- $R$ for disk radius.

The kinetic energy is:

$$
T=\frac{1}{2}M\dot s^2+\frac{1}{2}I\dot\theta^2
$$

For a disk:

$$
I=\frac{1}{2}MR^2
$$

The potential energy can be written so that the Lagrangian is:

$$
L=\frac{1}{2}M\dot s^2+\frac{1}{4}MR^2\dot\theta^2+Mg(s-l)\sin\alpha
$$

The rolling constraint is:

$$
f(s,\theta)=s-R\theta=0
$$

The multiplier equations are:

$$
M\ddot s-Mg\sin\alpha=\lambda
$$

$$
\frac{1}{2}MR^2\ddot\theta=-R\lambda
$$

with:

$$
\ddot s=R\ddot\theta
$$

Solving gives:

$$
\ddot s=\frac{2}{3}g\sin\alpha
$$

and:

$$
\lambda=-\frac{1}{3}Mg\sin\alpha
$$

The generalized constraint forces are:

$$
Q_s=\lambda
$$

and:

$$
Q_\theta=-R\lambda
$$

In words, the multiplier encodes the force and torque required to maintain rolling without slipping.

## What To Remember

- Multipliers let dependent coordinates remain in the calculation.
- The multiplier equations must be solved together with the constraints.
- In mechanics, multiplier terms represent generalized constraint forces.
- The sign of a multiplier depends on the chosen sign convention for the constraint function.

## Links To Concept Notes

- [Constraints](../../../Mechanics/Constraints.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)

<!-- semantic-edges
{"source":"Lagrange Multipliers","relation":"REPRESENTS","target":"Generalized Constraint Forces","evidence_heading":"Constraint Forces","evidence_summary":"The note compares the multiplier form with the forced Lagrange equations to identify multiplier terms as generalized constraint forces.","confidence":0.94}
{"source":"Rolling Without Slipping","relation":"EXAMPLE_OF","target":"Holonomic Constraint","evidence_heading":"Rolling Disk Example","evidence_summary":"The disk example uses the integrable rolling condition s minus R theta equals zero as a holonomic constraint in the multiplier method.","confidence":0.86}
-->
