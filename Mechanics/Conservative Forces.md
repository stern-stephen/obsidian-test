# Conservative Forces

## Overview

A force is conservative when its work between two points depends only on the endpoints, not on the path taken. This path independence allows the work to be represented by the change of a scalar potential energy.

The statement

$$
\mathbf{F}=-\nabla V
$$

is therefore equivalent to path-independent work, subject to ordinary smoothness and domain assumptions.

## From Path Independence To A Potential

Assume the work done by $\mathbf{F}$ between two points is independent of the path. Choose a fixed reference point $\mathbf{r}_0$ and define:

$$
V(\mathbf{r})=-\int_{\mathbf{r}_0}^{\mathbf{r}}\mathbf{F}\cdot d\mathbf{l}
$$

This defines a single-valued function because the integral is path independent.

Now move the endpoint by a small displacement $d\mathbf{r}$. The resulting change in the potential is:

$$
dV=-\mathbf{F}(\mathbf{r})\cdot d\mathbf{r}
$$

But the differential of any scalar field is:

$$
dV=\nabla V\cdot d\mathbf{r}
$$

Because these equations hold for every possible displacement $d\mathbf{r}$:

$$
\nabla V=-\mathbf{F}
$$

Thus:

$$
\mathbf{F}=-\nabla V
$$

The minus sign means that the force points in the direction in which potential energy decreases most rapidly.

## Converse

Suppose instead that $\mathbf{F}=-\nabla V$. The work along any path from $\mathbf{r}_1$ to $\mathbf{r}_2$ is:

$$
W_{12}=\int_{\mathbf{r}_1}^{\mathbf{r}_2}\mathbf{F}\cdot d\mathbf{l}
$$

Substitution gives:

$$
W_{12}=-\int_{\mathbf{r}_1}^{\mathbf{r}_2}\nabla V\cdot d\mathbf{l}=V(\mathbf{r}_1)-V(\mathbf{r}_2)
$$

The result depends only on the endpoints, so the force is conservative.

## Curl Test And Domain Assumptions

If $\mathbf{F}=-\nabla V$, then:

$$
\nabla\times\mathbf{F}=-\nabla\times(\nabla V)=0
$$

Therefore zero curl is necessary for a smooth conservative force. It is sufficient when the region is simply connected, meaning roughly that the region has no excluded holes around which a closed path can wind.

On a domain with holes, $\nabla\times\mathbf{F}=0$ locally may not produce one globally single-valued potential. The most general test is:

$$
\oint_C\mathbf{F}\cdot d\mathbf{l}=0
$$

for every closed path $C$ in the domain.

## Energy Conservation

For a particle of constant mass:

$$
\frac{dT}{dt}=\mathbf{F}\cdot\mathbf{v}
$$

If $\mathbf{F}=-\nabla V$ and $V$ has no explicit time dependence:

$$
\frac{dV}{dt}=\nabla V\cdot\mathbf{v}=-\mathbf{F}\cdot\mathbf{v}
$$

Hence:

$$
\frac{d}{dt}(T+V)=0
$$

If $V(\mathbf{r},t)$ depends explicitly on time, the force can still be derived from $-\nabla V$, but $T+V$ need not be conserved.

## Related Concepts

- [Conservation Laws](Conservation%20Laws.md)
- [Classical Mechanics](Classical%20Mechanics.md)
- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Goldstein Section 1.1](../Book%20Notes/Goldstein/Chapter%201/Mechanics%20of%20a%20Particle.md)
