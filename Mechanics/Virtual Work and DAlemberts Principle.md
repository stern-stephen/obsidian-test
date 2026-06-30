# Virtual Work and D'Alembert's Principle

## Overview

Virtual work reformulates equilibrium using infinitesimal allowed changes of configuration. D'Alembert's principle extends the same idea to dynamics and provides the bridge from Newton's laws to Lagrange's equations.

## Virtual Displacement

A virtual displacement $\delta\mathbf{r}_i$ is an infinitesimal change consistent with the constraints at a fixed instant. It is not the actual displacement during a time interval.

For equilibrium:

$$
\sum_i\mathbf{F}_i\cdot\delta\mathbf{r}_i=0
$$

For ideal constraints:

$$
\sum_i\mathbf{f}_i\cdot\delta\mathbf{r}_i=0
$$

so only applied forces remain in the virtual-work equation.

For an internal holonomic constraint $f(\mathbf{r}_1,\ldots,\mathbf{r}_N,t)=0$, the constraint force has the direction needed to enforce that relation. Its virtual work is proportional to the virtual change of the constraint:

$$
\delta f=\sum_i\frac{\partial f}{\partial\mathbf{r}_i}\cdot\delta\mathbf{r}_i
$$

Allowed virtual displacements keep the system on the constraint surface, so $\delta f=0$. Thus the internal constraint force can be omitted from D'Alembert's principle even though the force itself is not zero.

## D'Alembert's Principle

Write Newton's law as:

$$
\mathbf{F}_i-\dot{\mathbf{p}}_i=0
$$

Then:

$$
\sum_i\left(\mathbf{F}_i-\dot{\mathbf{p}}_i\right)\cdot\delta\mathbf{r}_i=0
$$

After ideal constraint forces are removed, only the applied forces remain. For independent generalized coordinates,

$$
\delta\mathbf{r}_i=\sum_j\frac{\partial\mathbf{r}_i}{\partial q_j}\delta q_j
$$

Define the generalized applied force by

$$
Q_j=\sum_i\mathbf{F}_i^{(a)}\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

Substitution into D'Alembert's principle gives

$$
\sum_j\left[Q_j-\sum_i\dot{\mathbf{p}}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}\right]\delta q_j=0
$$

The remaining task is to rewrite the projected inertial term using the kinetic energy

$$
T=\frac{1}{2}\sum_i m_i\dot{\mathbf{r}}_i^2
$$

Because

$$
\frac{\partial\dot{\mathbf{r}}_i}{\partial\dot q_j}=\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

we have

$$
\frac{\partial T}{\partial\dot q_j}=\sum_i\mathbf{p}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

Taking a time derivative gives

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}=\sum_i\dot{\mathbf{p}}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}+\sum_i\mathbf{p}_i\cdot\frac{d}{dt}\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

The other derivative of the kinetic energy is

$$
\frac{\partial T}{\partial q_j}=\sum_i\mathbf{p}_i\cdot\frac{\partial\dot{\mathbf{r}}_i}{\partial q_j}=\sum_i\mathbf{p}_i\cdot\frac{d}{dt}\frac{\partial\mathbf{r}_i}{\partial q_j}
$$

Subtracting these two equations isolates the inertial projection:

$$
\sum_i\dot{\mathbf{p}}_i\cdot\frac{\partial\mathbf{r}_i}{\partial q_j}=\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}
$$

D'Alembert's principle therefore becomes

$$
\sum_j\left[Q_j-\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}+\frac{\partial T}{\partial q_j}\right]\delta q_j=0
$$

The variations $\delta q_j$ are independent, so every coefficient must vanish:

$$
\frac{d}{dt}\frac{\partial T}{\partial\dot q_j}-\frac{\partial T}{\partial q_j}=Q_j
$$

For a velocity-independent conservative potential,

$$
Q_j=-\frac{\partial V}{\partial q_j}
$$

Defining $L=T-V$ then gives the Euler-Lagrange equations:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}-\frac{\partial L}{\partial q_j}=0
$$

This derivation assumes independent generalized coordinates and ideal constraints, so the constraint forces do no total virtual work. The last step also assumes the applied forces come from an ordinary velocity-independent potential.

## Intuition

The inertial term $-\dot{\mathbf{p}}_i$ lets a dynamical trajectory be treated as an instantaneous virtual-work balance. The method is valuable because the allowed virtual displacements automatically respect the constraints.

In Coopersmith's terminology, the inertial force is the reversed mass-acceleration term $-m_i\mathbf{a}_i$. It is not an additional applied interaction; it is the term that lets the dynamical problem be handled like a virtual-work equilibrium problem.

## Related Concepts

- [Constraints](Constraints.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Inertial Forces](Inertial%20Forces.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Goldstein Section 1.4](../Book%20Notes/Goldstein/Chapter%201/DAlemberts%20Principle%20and%20Lagranges%20Equations.md)
- [Coopersmith Chapter 4](../Book%20Notes/Coopersmith/Chapter%204/Chapter%20Overview.md)
- [Coopersmith Chapter 5](../Book%20Notes/Coopersmith/Chapter%205/Chapter%20Overview.md)

<!-- semantic-edges
{"source":"Virtual Work","relation":"REFORMULATES","target":"Equilibrium","evidence_heading":"Overview","evidence_summary":"The note states that virtual work reformulates equilibrium using infinitesimal allowed changes of configuration.","confidence":0.95}
{"source":"D'Alembert's Principle","relation":"EXTENDS","target":"Virtual Work","evidence_heading":"Overview","evidence_summary":"The overview says D'Alembert's principle extends the virtual-work idea from equilibrium to dynamics.","confidence":0.95}
{"source":"Ideal Constraints","relation":"ELIMINATES","target":"Constraint Forces","evidence_heading":"Virtual Displacement","evidence_summary":"For ideal constraints, the constraint forces do no virtual work along allowed virtual displacements, so only applied forces remain in the virtual-work equation.","confidence":0.9}
{"source":"D'Alembert's Principle","relation":"DERIVES","target":"Euler-Lagrange Equations","evidence_heading":"D'Alembert's Principle","evidence_summary":"After projecting Newton's law onto independent generalized-coordinate variations and assuming conservative applied forces, the note derives the Euler-Lagrange equations.","confidence":0.95}
{"source":"Inertial Forces","relation":"ENABLES","target":"D'Alembert's Principle","evidence_heading":"Intuition","evidence_summary":"The inertial term lets a dynamical trajectory be treated as an instantaneous virtual-work balance.","confidence":0.9}
-->
