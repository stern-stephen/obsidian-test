# Rayleigh Dissipation Function

## Overview

Rayleigh's dissipation function represents friction forces that are linear in generalized velocities while preserving a compact Lagrangian form of the equations of motion.

## Definition

For Cartesian drag components proportional to velocity:

$$
\mathcal{F}=\frac{1}{2}\sum_i\left(k_xv_{ix}^2+k_yv_{iy}^2+k_zv_{iz}^2\right)
$$

The friction force is:

$$
\mathbf{F}^{(f)}=-\nabla_{\mathbf{v}}\mathcal{F}
$$

In generalized coordinates:

$$
Q_j^{(f)}=-\frac{\partial\mathcal{F}}{\partial\dot q_j}
$$

## Lagrange Equations With Dissipation

The equations of motion are:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_j}-\frac{\partial L}{\partial q_j}+\frac{\partial\mathcal{F}}{\partial\dot q_j}=0
$$

With this convention:

$$
2\mathcal{F}=\text{rate of mechanical energy dissipation}
$$

## Example

For one-dimensional linear damping $F^{(f)}=-b\dot x$:

$$
\mathcal{F}=\frac{1}{2}b\dot x^2
$$

For a damped oscillator:

$$
L=\frac{1}{2}m\dot x^2-\frac{1}{2}kx^2
$$

the dissipative Euler-Lagrange equation gives:

$$
m\ddot x+b\dot x+kx=0
$$

## Limitations

Rayleigh's construction directly handles viscous forces linear in velocity. Dry friction and more general nonlinear dissipative forces require other treatments or a modified dissipation function.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Goldstein Section 1.5](../Book%20Notes/Goldstein/Chapter%201/Velocity-Dependent%20Potentials%20and%20the%20Dissipation%20Function.md)

<!-- semantic-edges
{"source":"Rayleigh Dissipation Function","relation":"REPRESENTS","target":"Linear Friction Forces","evidence_heading":"Overview","evidence_summary":"The note says Rayleigh's dissipation function represents friction forces that are linear in generalized velocities.","confidence":0.95}
{"source":"Rayleigh Dissipation Function","relation":"EXTENDS","target":"Lagrangian Mechanics","evidence_heading":"Lagrange Equations With Dissipation","evidence_summary":"The note modifies the Lagrange equations by adding a velocity derivative of the dissipation function.","confidence":0.9}
{"source":"Rayleigh Dissipation Function","relation":"DETERMINES","target":"Mechanical Energy Dissipation","evidence_heading":"Lagrange Equations With Dissipation","evidence_summary":"With the convention in the note, twice the Rayleigh dissipation function is the rate of mechanical energy dissipation.","confidence":0.95}
{"source":"Rayleigh Dissipation Function","relation":"ASSUMES","target":"Velocity-Linear Friction","evidence_heading":"Limitations","evidence_summary":"The note says Rayleigh's construction directly handles viscous forces linear in velocity, while dry friction and more general nonlinear dissipation require other treatments.","confidence":0.9}
-->
