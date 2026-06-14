# Mechanics of a Particle

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 1.1, printed pages 1-5.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Mechanics of a System of Particles](Mechanics%20of%20a%20System%20of%20Particles.md)

## Reading Status

- Status: started
- Pages: 1-5
- Date started: 2026-06-14
- Date finished:

## Big Ideas

- Newton's second law is fundamentally a statement about momentum, not merely acceleration.
- Linear momentum, angular momentum, and energy conservation follow under different physical conditions.
- The energy theorem requires care when the potential depends explicitly on time.
- An inertial frame is an idealized frame in which Newton's momentum equation holds.

## Notes

For position $\mathbf{r}$ and velocity $\mathbf{v}$:

$$
\mathbf{v}=\frac{d\mathbf{r}}{dt}
$$

Linear momentum is:

$$
\mathbf{p}=m\mathbf{v}
$$

Newton's second law is:

$$
\mathbf{F}=\frac{d\mathbf{p}}{dt}
$$

Only for constant mass does this reduce to:

$$
\mathbf{F}=m\mathbf{a}
$$

If the total force vanishes, linear momentum is conserved.

## Angular Momentum

About a chosen origin:

$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}
$$

The torque is:

$$
\mathbf{N}=\mathbf{r}\times\mathbf{F}
$$

For constant mass:

$$
\mathbf{N}=\frac{d\mathbf{L}}{dt}
$$

Thus zero torque implies conservation of angular momentum. Both angular momentum and torque depend on the reference point.

## Work And Energy

The work done from point 1 to point 2 is:

$$
W_{12}=\int_1^2 \mathbf{F}\cdot d\mathbf{s}
$$

For constant mass:

$$
W_{12}=T_2-T_1
$$

where:

$$
T=\frac{1}{2}mv^2
$$

For a conservative force:

$$
\mathbf{F}=-\nabla V
$$

and:

$$
T+V=E=\text{constant}
$$

If $V(\mathbf{r},t)$ depends explicitly on time, a force may still be obtained from $-\nabla V$, but $T+V$ need not be conserved.

## Common Confusions

- $\mathbf{F}=m\mathbf{a}$ assumes constant mass; $\mathbf{F}=d\mathbf{p}/dt$ is the more general statement.
- Zero force and zero torque are different conditions and lead to different conservation laws.
- A conservative spatial force does not guarantee energy conservation when its potential depends explicitly on time.
- The additive zero of potential energy is arbitrary.

## Links To Concept Notes

- [Classical Mechanics](../../../Mechanics/Classical%20Mechanics.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
