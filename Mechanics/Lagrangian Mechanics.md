# Lagrangian Mechanics

## Overview

Lagrangian mechanics formulates dynamics using generalized coordinates, velocities, and the action.

## Definition

For many systems, the Lagrangian is:

$$
L = T - V
$$

The action is:

$$
S = \int L dt
$$

Physical trajectories satisfy:

$$
\delta S = 0
$$

## Key Equations

The Euler-Lagrange equations are:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{q}_i} - \frac{\partial L}{\partial q_i} = 0
$$

The conjugate momentum is:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

The Hamiltonian is obtained by replacing the velocity variables with momentum variables through a [Legendre transform](../Mathematics/Legendre%20Transforms.md):

$$
H(q,p,t)=\sum_i p_i\dot{q}_i-L(q,\dot{q},t)
$$

After defining $p_i$, solve for $\dot{q}_i$ in terms of $q_i,p_i,t$ before treating $H$ as a phase-space function.

## Non-Uniqueness Of The Lagrangian

The Lagrangian is not unique. Two common changes leave the classical Euler-Lagrange equations unchanged.

First, multiply the whole Lagrangian by a nonzero constant $c$:

$$
L'=cL
$$

Then:

$$
\frac{d}{dt}\frac{\partial L'}{\partial\dot q_i}-\frac{\partial L'}{\partial q_i}=c\left(\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}-\frac{\partial L}{\partial q_i}\right)
$$

Since $c\neq0$, setting this expression equal to zero gives the same equations of motion.

Second, add a total time derivative:

$$
L'=L+\frac{dF(q,t)}{dt}
$$

The action changes by an endpoint term:

$$
S'=\int_{t_a}^{t_b}L'dt=S+F(q(t_b),t_b)-F(q(t_a),t_a)
$$

For Hamilton's principle with fixed endpoint times and fixed endpoint configurations, the added endpoint term is fixed during the variation. Therefore:

$$
\delta S'=\delta S
$$

So $L$ and $L'$ select the same classical paths.

The physical point is that the Lagrangian itself is not directly observable. It is a generator of equations of motion, and many formulas can generate the same motion. This is why mechanics treats Lagrangians up to an equivalence class rather than as unique physical objects. A total derivative can still change derived bookkeeping quantities such as canonical momentum or the displayed Hamiltonian, but it does not change the underlying classical trajectory.

In electromagnetism this same freedom appears as gauge freedom: changing the scalar and vector potentials by a gauge transformation changes the charged-particle Lagrangian by a total derivative, while the electric and magnetic fields stay unchanged. See [Electromagnetic Lagrangian](Electromagnetic%20Lagrangian.md#gauge-freedom).

The constant-multiple freedom is mainly a classical statement. It preserves the Euler-Lagrange equations, but it changes the numerical scale of the action. In quantum mechanics, where phases depend on $S/\hbar$, that scale can matter unless the rest of the theory is rescaled consistently.

## Intuition

The Lagrangian approach is especially useful when constraints make Cartesian force equations awkward. Good coordinates can make the problem simpler before solving any differential equations.

## Examples

### Particle In A Potential

For a particle moving in one dimension:

$$
L=\frac{1}{2}m\dot{x}^2-V(x)
$$

Use the Euler-Lagrange equation:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{x}}-\frac{\partial L}{\partial x}=0
$$

Compute the velocity derivative:

$$
\frac{\partial L}{\partial \dot{x}}=m\dot{x}
$$

Then:

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{x}}=m\ddot{x}
$$

Compute the position derivative:

$$
\frac{\partial L}{\partial x}=-\frac{dV}{dx}
$$

So:

$$
m\ddot{x}+\frac{dV}{dx}=0
$$

or:

$$
m\ddot{x}=-\frac{dV}{dx}
$$

This recovers Newton's second law for a conservative force.

### Harmonic Oscillator

For a mass on a spring:

$$
V(x)=\frac{1}{2}kx^2
$$

so:

$$
L=\frac{1}{2}m\dot{x}^2-\frac{1}{2}kx^2
$$

The derivatives are:

$$
\frac{\partial L}{\partial \dot{x}}=m\dot{x}
$$

and:

$$
\frac{\partial L}{\partial x}=-kx
$$

The Euler-Lagrange equation gives:

$$
m\ddot{x}+kx=0
$$

or:

$$
\ddot{x}+\frac{k}{m}x=0
$$

This is the familiar harmonic oscillator equation.

### Simple Pendulum

For a pendulum of length $\ell$, use the angle $\theta$ as the generalized coordinate.

The kinetic energy is:

$$
T=\frac{1}{2}m\ell^2\dot{\theta}^2
$$

Choosing the lowest point as zero potential energy:

$$
V=mg\ell(1-\cos\theta)
$$

So:

$$
L=\frac{1}{2}m\ell^2\dot{\theta}^2-mg\ell(1-\cos\theta)
$$

Now:

$$
\frac{\partial L}{\partial \dot{\theta}}=m\ell^2\dot{\theta}
$$

and:

$$
\frac{\partial L}{\partial \theta}=-mg\ell\sin\theta
$$

The Euler-Lagrange equation gives:

$$
m\ell^2\ddot{\theta}+mg\ell\sin\theta=0
$$

or:

$$
\ddot{\theta}+\frac{g}{\ell}\sin\theta=0
$$

For small angles, $\sin\theta\approx\theta$, giving:

$$
\ddot{\theta}+\frac{g}{\ell}\theta=0
$$

This shows why generalized coordinates are useful: the pendulum's constraint is built into the coordinate $\theta$.

## Related Concepts

- [Action Principle](Action%20Principle.md)
- [Hamilton's Principle](Hamiltons%20Principle.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [Generalized Coordinates](Generalized%20Coordinates.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Legendre Transforms](../Mathematics/Legendre%20Transforms.md)
- [The Principle of Least Action and Lagrangian Mechanics](../Book%20Notes/Shankar/Chapter%202/The%20Principle%20of%20Least%20Action%20and%20Lagrangian%20Mechanics.md)
- [Coopersmith Section 6.5-6.6](../Book%20Notes/Coopersmith/Chapter%206/The%20Forms%20of%20T%20V%20and%20L.md)

<!-- semantic-edges
{"source":"Lagrangian Mechanics","relation":"REQUIRES","target":"Generalized Coordinates","evidence_heading":"Overview","evidence_summary":"The overview defines Lagrangian mechanics as a dynamics formulation using generalized coordinates, velocities, and the action.","confidence":0.9}
{"source":"Lagrangian Mechanics","relation":"REFORMULATES","target":"Newton's Second Law","evidence_heading":"Particle In A Potential","evidence_summary":"For a one-dimensional conservative force, applying the Euler-Lagrange equation recovers Newton's second law.","confidence":0.9}
{"source":"Lagrangian Mechanics","relation":"ENABLES","target":"Hamiltonian Mechanics","evidence_heading":"Key Equations","evidence_summary":"The note explains that the Hamiltonian is obtained from the Lagrangian by replacing velocity variables with momentum variables through a Legendre transform.","confidence":0.9}
{"source":"Constant Multiple of Lagrangian","relation":"PRESERVES","target":"Euler-Lagrange Equations","evidence_heading":"Non-Uniqueness Of The Lagrangian","evidence_summary":"Multiplying the Lagrangian by a nonzero constant multiplies the Euler-Lagrange expression by the same constant, so the zero equation is unchanged.","confidence":0.94}
{"source":"Total Time Derivative of Lagrangian","relation":"PRESERVES","target":"Classical Equations of Motion","evidence_heading":"Non-Uniqueness Of The Lagrangian","evidence_summary":"Adding dF/dt changes the action only by fixed endpoint terms, so fixed-endpoint variations and the selected classical paths are unchanged.","confidence":0.94}
-->
