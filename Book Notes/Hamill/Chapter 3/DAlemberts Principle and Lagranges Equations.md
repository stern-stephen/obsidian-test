# DAlemberts Principle and Lagranges Equations

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 3.1, printed pages 70-73.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Hamiltons Principle and Variational Derivation](Hamiltons%20Principle%20and%20Variational%20Derivation.md)

## Reading Status

- Status: started
- Pages: 70-73
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill first derives Lagrange's equations from d'Alembert's principle. This route starts close to Newton's second law, then rewrites the dynamics in virtual-work language so that generalized coordinates can be used cleanly.

## D'Alembert's Principle

For a system of particles, d'Alembert's principle is:

$$
\sum_\alpha(\mathbf{F}^{\text{ext}}_\alpha-\dot{\mathbf{p}}_\alpha)\cdot\delta\mathbf{r}_\alpha=0
$$

In Cartesian scalar form:

$$
\sum_i(F_i^{\text{ext}}-\dot p_i)\delta x_i=0
$$

The expression looks almost trivial because Newton's second law says $\mathbf{F}^{\text{ext}}_\alpha-\dot{\mathbf{p}}_\alpha=0$. Its usefulness appears when the virtual displacements are expressed in generalized coordinates.

## Virtual Displacements In Generalized Coordinates

If constraints reduce $n$ Cartesian coordinates to $n-k$ generalized coordinates, then:

$$
x_i=x_i(q_1,\ldots,q_{n-k},t)
$$

For a virtual displacement, time is fixed:

$$
\delta x_i=\sum_j\frac{\partial x_i}{\partial q_j}\delta q_j
$$

The force term becomes:

$$
\sum_iF_i^{\text{ext}}\delta x_i=\sum_jQ_j\delta q_j
$$

where:

$$
Q_j=\sum_iF_i^{\text{ext}}\frac{\partial x_i}{\partial q_j}
$$

This is the generalized force conjugate to $q_j$.

## Inertial Term And Kinetic Energy

The inertial part is:

$$
\sum_i\dot p_i\delta x_i
$$

For constant masses, $\dot p_i=m_i\ddot x_i$. Hamill uses the identity from Chapter 1:

$$
\frac{\partial \dot x_i}{\partial \dot q_j}=\frac{\partial x_i}{\partial q_j}
$$

and the kinetic energy:

$$
T=\sum_i\frac{1}{2}m_i\dot x_i^2
$$

to rewrite the inertial virtual work as:

$$
\sum_i\dot p_i\delta x_i=\sum_j\left[\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_j}\right)-\frac{\partial T}{\partial q_j}\right]\delta q_j
$$

This is the algebraic bridge from Newtonian inertial forces to the Lagrangian form.

## Nielsen Form

Substituting the force and inertial pieces into d'Alembert's principle gives:

$$
\sum_j\left[Q_j-\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_j}\right)+\frac{\partial T}{\partial q_j}\right]\delta q_j=0
$$

Because the $\delta q_j$ are independent:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_j}\right)-\frac{\partial T}{\partial q_j}=Q_j
$$

Hamill calls this the Nielsen form of Lagrange's equations.

## Conservative Forces

If the generalized forces come from a velocity-independent potential:

$$
Q_j=-\frac{\partial V}{\partial q_j}
$$

then:

$$
\frac{d}{dt}\left(\frac{\partial T}{\partial \dot q_j}\right)-\frac{\partial T}{\partial q_j}=-\frac{\partial V}{\partial q_j}
$$

With:

$$
L=T-V
$$

this becomes the familiar Lagrange equation:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_j}\right)-\frac{\partial L}{\partial q_j}=0
$$

## What This Derivation Shows

This derivation shows that Lagrange's equations are not a separate postulate at this stage. Under the assumptions used here, they follow from Newton's law expressed through d'Alembert's principle, generalized coordinates, and virtual displacements.

The derivation also explains why generalized forces and kinetic energy are the natural objects before the Lagrangian $L=T-V$ is introduced.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)

<!-- semantic-edges
{"source":"D'Alembert's Principle","relation":"DERIVES","target":"Nielsen Form of Lagrange's Equations","evidence_heading":"Nielsen Form","evidence_summary":"The note rewrites d'Alembert's principle in generalized coordinates to obtain the kinetic-energy equation with generalized forces.","confidence":0.94}
{"source":"Nielsen Form of Lagrange's Equations","relation":"SPECIALIZES","target":"Lagrange's Equations","evidence_heading":"Conservative Forces","evidence_summary":"When generalized forces come from a velocity-independent potential, the Nielsen form becomes the familiar Lagrange equation for L = T - V.","confidence":0.92}
-->
