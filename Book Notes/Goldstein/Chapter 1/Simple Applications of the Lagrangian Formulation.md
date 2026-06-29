# Simple Applications of the Lagrangian Formulation

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.6, printed pages 24-29.

Previous: [Velocity-Dependent Potentials and the Dissipation Function](Velocity-Dependent%20Potentials%20and%20the%20Dissipation%20Function.md)

## Reading Status

- Status: started
- Pages: 24-29
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- The Lagrangian method replaces vector force bookkeeping with scalar kinetic and potential energies.
- Time-independent coordinate transformations make kinetic energy homogeneous and quadratic in generalized velocities.
- Curvilinear-coordinate acceleration terms emerge automatically from derivatives of the kinetic energy.
- Constraint forces are eliminated from the motion equations, but they usually cannot be recovered directly from them.

## General Form Of Kinetic Energy

For:

$$
\mathbf{r}_i=\mathbf{r}_i(q_1,\ldots,q_n,t)
$$

the velocity is:

$$
\dot{\mathbf{r}}_i=\sum_j\frac{\partial\mathbf{r}_i}{\partial q_j}\dot q_j+\frac{\partial\mathbf{r}_i}{\partial t}
$$

Therefore the kinetic energy has the form:

$$
T=T_0+T_1+T_2
$$

where the terms are respectively homogeneous of degree zero, one, and two in the generalized velocities.

For scleronomous transformations, the explicit time derivatives vanish and:

$$
T=\frac{1}{2}\sum_{j,k}M_{jk}(q)\dot q_j\dot q_k
$$

## Particle In Plane Polar Coordinates

The kinetic energy is:

$$
T=\frac{1}{2}m\left(\dot r^2+r^2\dot\theta^2\right)
$$

The generalized forces are:

$$
Q_r=F_r
$$

$$
Q_\theta=rF_\theta
$$

Lagrange's equations produce:

$$
m\ddot r-mr\dot\theta^2=F_r
$$

$$
\frac{d}{dt}\left(mr^2\dot\theta\right)=rF_\theta
$$

The centripetal and angular-momentum terms emerge without separately resolving vector accelerations.

## Atwood's Machine

The rope-length constraint leaves one coordinate $x$. With a massless, frictionless pulley:

$$
T=\frac{1}{2}(M_1+M_2)\dot x^2
$$

$$
V=-M_1gx-M_2g(l-x)
$$

The equation of motion is:

$$
\ddot x=\frac{M_1-M_2}{M_1+M_2}g
$$

The rope tension never appears. This is the strength and limitation of eliminating constraint forces.

## Bead On A Rotating Wire

For a straight wire rotating at fixed angular velocity $\omega$:

$$
x=r\cos\omega t
$$

$$
y=r\sin\omega t
$$

The constraint is rheonomous, and:

$$
T=\frac{1}{2}m\left(\dot r^2+r^2\omega^2\right)
$$

The radial equation is:

$$
\ddot r=\omega^2r
$$

The outward exponential behavior reflects energy supplied by the external agent that keeps the wire rotating.

## Problem-Solving Routine

1. Count the degrees of freedom and choose independent generalized coordinates.
2. Encode holonomic constraints in the coordinate transformation.
3. Write $T$ and $V$ in those coordinates.
4. Form $L=T-V$.
5. Apply one Euler-Lagrange equation for each coordinate.
6. Recover constraint forces separately only if the problem asks for them.

## Common Confusions

- A term such as $-mr\dot\theta^2$ is not an extra applied force; it comes from curvilinear kinematics.
- Time-dependent constraints can exchange energy with the system.
- A massless, frictionless constraint element may still exert a nonzero force.
- The Lagrangian method gives the allowed motion directly, not every interaction force.

## Links To Concept Notes

- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)

<!-- semantic-edges
{"source":"Simple Applications of the Lagrangian Formulation","relation":"PART_OF","target":"Goldstein Chapter 1","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Goldstein Chapter 1.","confidence":0.85}
{"source":"Simple Applications of the Lagrangian Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Velocity-Dependent Potentials and the Dissipation Function","evidence_heading":"Simple Applications of the Lagrangian Formulation","evidence_summary":"This source note explicitly links its treatment to Velocity-Dependent Potentials and the Dissipation Function.","confidence":0.8}
{"source":"Simple Applications of the Lagrangian Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Generalized Coordinates","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Generalized Coordinates.","confidence":0.8}
{"source":"Simple Applications of the Lagrangian Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Constraints","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Constraints.","confidence":0.8}
{"source":"Simple Applications of the Lagrangian Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Lagrangian Mechanics","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Lagrangian Mechanics.","confidence":0.8}
-->
