# Hamiltonian Mechanics

## Overview

Hamiltonian mechanics describes dynamics using generalized coordinates and conjugate momenta in phase space.

## Definition

The Hamiltonian is obtained from the Lagrangian by a [Legendre transform](../Mathematics/Legendre%20Transforms.md):

$$
H(q,p,t) = \sum_i p_i\dot{q}_i - L(q,\dot{q},t)
$$

where:

$$
p_i = \frac{\partial L}{\partial \dot{q}_i}
$$

After computing the momenta, solve these equations for the velocities $\dot{q}_i$ in terms of $q_i,p_i,t$. Then substitute those velocities into the Legendre transform so that $H$ is a function of $q,p,t$, not $q,\dot{q},t$.

## Key Equations

Hamilton's equations are:

$$
\dot{q}_i = \frac{\partial H}{\partial p_i}
$$

$$
\dot{p}_i = -\frac{\partial H}{\partial q_i}
$$

## Intuition

The Hamiltonian is often the total energy, but its structural role is broader: it generates time evolution in phase space.

## Deriving The Hamiltonian From The Lagrangian

Start with:

$$
L(q,\dot{q},t)
$$

The Lagrangian uses generalized positions and velocities. Hamiltonian mechanics instead uses generalized positions and conjugate momenta.

First define the conjugate momenta:

$$
p_i=\frac{\partial L}{\partial \dot{q}_i}
$$

Then solve these equations for the velocities:

$$
\dot{q}_i=\dot{q}_i(q,p,t)
$$

Finally define:

$$
H(q,p,t)=\sum_i p_i\dot{q}_i-L(q,\dot{q},t)
$$

with the velocities rewritten in terms of $q,p,t$.

This change of variables is a [Legendre transform](../Mathematics/Legendre%20Transforms.md). It replaces the velocity variables $\dot{q}_i$ with the momentum variables $p_i$.

### Simple Particle Example

For:

$$
L=\frac{1}{2}m\dot{x}^2-V(x)
$$

the conjugate momentum is:

$$
p=\frac{\partial L}{\partial \dot{x}}=m\dot{x}
$$

So:

$$
\dot{x}=\frac{p}{m}
$$

Now compute:

$$
H=p\dot{x}-L
$$

Substitute $\dot{x}=p/m$:

$$
H=p\frac{p}{m}-\left(\frac{1}{2}m\left(\frac{p}{m}\right)^2-V(x)\right)
$$

Simplifying gives:

$$
H=\frac{p^2}{2m}+V(x)
$$

For this simple system, the Hamiltonian equals the total energy:

$$
H=T+V
$$

But this is a result of the example, not the definition. The definition is the Legendre transform from $L(q,\dot{q},t)$ to $H(q,p,t)$.

## Examples

### Particle In A Potential

Start from the Hamiltonian:

$$
H(x,p)=\frac{p^2}{2m}+V(x)
$$

Hamilton's equations are:

$$
\dot{x}=\frac{\partial H}{\partial p}
$$

and:

$$
\dot{p}=-\frac{\partial H}{\partial x}
$$

Compute:

$$
\dot{x}=\frac{p}{m}
$$

and:

$$
\dot{p}=-\frac{dV}{dx}
$$

Since $p=m\dot{x}$, the second equation becomes:

$$
m\ddot{x}=-\frac{dV}{dx}
$$

So Hamiltonian mechanics recovers the same equation of motion as the Lagrangian method, but written as two first-order equations in phase space.

### Harmonic Oscillator

For:

$$
V(x)=\frac{1}{2}kx^2
$$

the Hamiltonian is:

$$
H(x,p)=\frac{p^2}{2m}+\frac{1}{2}kx^2
$$

Hamilton's equations give:

$$
\dot{x}=\frac{\partial H}{\partial p}=\frac{p}{m}
$$

and:

$$
\dot{p}=-\frac{\partial H}{\partial x}=-kx
$$

Differentiate the first equation:

$$
\ddot{x}=\frac{\dot{p}}{m}
$$

Substitute $\dot{p}=-kx$:

$$
\ddot{x}=-\frac{k}{m}x
$$

So:

$$
\ddot{x}+\frac{k}{m}x=0
$$

The Hamiltonian viewpoint tracks the motion as a curve in the $x,p$ phase plane. For the harmonic oscillator, constant-energy curves are ellipses:

$$
\frac{p^2}{2m}+\frac{1}{2}kx^2=E
$$

### Simple Pendulum

For a pendulum with coordinate $\theta$, the conjugate momentum is:

$$
p_\theta=\frac{\partial L}{\partial \dot{\theta}}=m\ell^2\dot{\theta}
$$

So:

$$
\dot{\theta}=\frac{p_\theta}{m\ell^2}
$$

The Hamiltonian is:

$$
H(\theta,p_\theta)=\frac{p_\theta^2}{2m\ell^2}+mg\ell(1-\cos\theta)
$$

Hamilton's equations give:

$$
\dot{\theta}=\frac{\partial H}{\partial p_\theta}=\frac{p_\theta}{m\ell^2}
$$

and:

$$
\dot{p}_\theta=-\frac{\partial H}{\partial \theta}=-mg\ell\sin\theta
$$

Since $p_\theta=m\ell^2\dot{\theta}$:

$$
m\ell^2\ddot{\theta}=-mg\ell\sin\theta
$$

or:

$$
\ddot{\theta}+\frac{g}{\ell}\sin\theta=0
$$

This is the same pendulum equation found from the Lagrangian, but expressed through the phase-space variables $\theta$ and $p_\theta$.

## Quantum Bridge

The Hamiltonian becomes the operator that generates time evolution in quantum mechanics.

## Related Concepts

- [Phase Space](Phase%20Space.md)
- [Canonical Momentum](Canonical%20Momentum.md)
- [Poisson Brackets](Poisson%20Brackets.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Legendre Transforms](../Mathematics/Legendre%20Transforms.md)
- [The Hamiltonian Formalism](../Book%20Notes/Shankar/Chapter%202/The%20Hamiltonian%20Formalism.md)

<!-- semantic-edges
{"source":"Hamiltonian Mechanics","relation":"DERIVES_FROM","target":"Lagrangian Mechanics","evidence_heading":"Deriving The Hamiltonian From The Lagrangian","evidence_summary":"The note constructs Hamiltonian mechanics from a Lagrangian by defining conjugate momenta, solving for velocities, and applying a Legendre transform.","confidence":0.95}
{"source":"Hamiltonian Mechanics","relation":"REQUIRES","target":"Phase Space","evidence_heading":"Overview","evidence_summary":"The overview describes Hamiltonian mechanics as dynamics using generalized coordinates and conjugate momenta in phase space.","confidence":0.95}
{"source":"Hamiltonian","relation":"DETERMINES","target":"Time Evolution","evidence_heading":"Intuition","evidence_summary":"The note states that the Hamiltonian's broader structural role is to generate time evolution in phase space.","confidence":0.95}
{"source":"Hamiltonian Mechanics","relation":"REFORMULATES","target":"Lagrangian Mechanics","evidence_heading":"Particle In A Potential","evidence_summary":"The particle example recovers the same equation of motion as the Lagrangian method, but as two first-order equations in phase space.","confidence":0.9}
-->
