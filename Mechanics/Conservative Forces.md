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

This definition needs path independence. Without it, different paths from $\mathbf{r}_0$ to $\mathbf{r}$ could give different values of $V(\mathbf{r})$, so $V$ would not be a single-valued function of position.

To find how $V$ changes with position, compare two nearby endpoints, $\mathbf{r}$ and $\mathbf{r}+\Delta\mathbf{r}$. Choose the path to $\mathbf{r}+\Delta\mathbf{r}$ so that it first follows the path from $\mathbf{r}_0$ to $\mathbf{r}$ and then follows a short straight segment from $\mathbf{r}$ to $\mathbf{r}+\Delta\mathbf{r}$. Path independence allows this convenient choice.

$$
V(\mathbf{r}+\Delta\mathbf{r})=-\int_{\mathbf{r}_0}^{\mathbf{r}}\mathbf{F}\cdot d\mathbf{l}-\int_{\mathbf{r}}^{\mathbf{r}+\Delta\mathbf{r}}\mathbf{F}\cdot d\mathbf{l}
$$

The first integral is $V(\mathbf{r})$, so:

$$
V(\mathbf{r}+\Delta\mathbf{r})-V(\mathbf{r})=-\int_{\mathbf{r}}^{\mathbf{r}+\Delta\mathbf{r}}\mathbf{F}\cdot d\mathbf{l}
$$

If $\mathbf{F}$ is continuous, then over a sufficiently short segment it is approximately constant. Therefore:

$$
V(\mathbf{r}+\Delta\mathbf{r})-V(\mathbf{r})=-\mathbf{F}(\mathbf{r})\cdot\Delta\mathbf{r}+o(\lVert\Delta\mathbf{r}\rVert)
$$

Here the final term becomes negligible compared with the length of the displacement as $\Delta\mathbf{r}\to 0$. On the other hand, differentiability of the scalar field $V$ means:

$$
V(\mathbf{r}+\Delta\mathbf{r})-V(\mathbf{r})=\nabla V(\mathbf{r})\cdot\Delta\mathbf{r}+o(\lVert\Delta\mathbf{r}\rVert)
$$

Comparing the terms that are linear in the arbitrary displacement $\Delta\mathbf{r}$ gives:

$$
\nabla V(\mathbf{r})\cdot\Delta\mathbf{r}=-\mathbf{F}(\mathbf{r})\cdot\Delta\mathbf{r}
$$

This must hold for every direction of $\Delta\mathbf{r}$. Two vectors having the same dot product with every displacement must be equal, so:

$$
\nabla V(\mathbf{r})=-\mathbf{F}(\mathbf{r})
$$

Therefore:

$$
\mathbf{F}=-\nabla V
$$

Equivalently, move only in the $x$ direction. Dividing by $\Delta x$ and taking the limit gives $F_x=-\partial V/\partial x$. Repeating this in the $y$ and $z$ directions gives all three components of $\mathbf{F}=-\nabla V$.

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

<!-- semantic-edges
{"source":"Conservative Forces","relation":"DETERMINES","target":"Potential Energy","evidence_heading":"Overview","evidence_summary":"The note says path-independent work allows the force to be represented by the change of a scalar potential energy.","confidence":0.95}
{"source":"Path-Independent Work","relation":"DETERMINES","target":"Potential Energy","evidence_heading":"From Path Independence To A Potential","evidence_summary":"The note defines potential energy by a path integral from a reference point and explains that the definition needs path independence to be single-valued.","confidence":0.95}
{"source":"Potential Energy","relation":"DETERMINES","target":"Conservative Forces","evidence_heading":"Converse","evidence_summary":"If the force is minus the gradient of a potential, the work between two points depends only on endpoint potential values, so the force is conservative.","confidence":0.95}
{"source":"Curl Test","relation":"REQUIRES","target":"Simply Connected Domain","evidence_heading":"Curl Test And Domain Assumptions","evidence_summary":"The note says zero curl is sufficient for a smooth force to be conservative when the region is simply connected.","confidence":0.9}
{"source":"Conservative Forces","relation":"DETERMINES","target":"Energy Conservation","evidence_heading":"Energy Conservation","evidence_summary":"For a time-independent potential and force F=-grad V, the note derives d(T+V)/dt=0.","confidence":0.95}
-->
