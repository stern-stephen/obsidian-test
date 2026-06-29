# Legendre Transforms

## Overview

A Legendre transform is a way to rewrite a function so that it uses a new variable: the slope of the original function.

In mechanics, this is the mathematical move that turns the Lagrangian $L(q,\dot{q},t)$ into the Hamiltonian $H(q,p,t)$. The velocity $\dot{q}$ is replaced by the conjugate momentum $p$.

## Basic One-Variable Idea

Start with a function:

$$
f(x)
$$

Its slope is:

$$
s=\frac{df}{dx}
$$

If we can solve this equation for $x$ as a function of $s$, then the Legendre transform of $f$ is:

$$
g(s)=sx-f(x)
$$

where $x$ should be rewritten as $x(s)$.

So the full procedure is:

1. Start with $f(x)$.
2. Define the new variable $s=df/dx$.
3. Solve for $x=x(s)$.
4. Define $g(s)=sx(s)-f(x(s))$.

The new function $g$ contains the same information as $f$, but it is expressed using slope $s$ instead of position $x$.

## Why The Product Term Appears

The term $sx-f(x)$ is chosen so that the new function has $s$ as its independent variable.

Differentiate:

$$
dg=d(sx-f)
$$

Using $df=s dx$:

$$
dg=s dx+x ds-s dx
$$

The $s dx$ terms cancel:

$$
dg=x ds
$$

So:

$$
\frac{dg}{ds}=x
$$

This is the point of the Legendre transform: it trades the original variable $x$ for the slope variable $s$, while preserving the information needed to recover $x$.

## Simple Example

Let:

$$
f(x)=\frac{1}{2}ax^2
$$

Then:

$$
s=\frac{df}{dx}=ax
$$

So:

$$
x=\frac{s}{a}
$$

Now compute:

$$
g(s)=sx-f(x)
$$

Substitute $x=s/a$:

$$
g(s)=s\frac{s}{a}-\frac{1}{2}a\left(\frac{s}{a}\right)^2
$$

Therefore:

$$
g(s)=\frac{s^2}{2a}
$$

The original function used $x$. The transformed function uses $s$.

## Mechanics Version

In Lagrangian mechanics, the function is:

$$
L(q,\dot{q},t)
$$

The variable being replaced is the velocity $\dot{q}_i$.

The new variable is the conjugate momentum:

$$
p_i=\frac{\partial L}{\partial \dot{q}_i}
$$

The Hamiltonian is the Legendre transform of the Lagrangian with respect to the velocity variables:

$$
H(q,p,t)=\sum_i p_i\dot{q}_i-L(q,\dot{q},t)
$$

After defining $p_i$, solve for $\dot{q}_i$ in terms of $q_i,p_i,t$. Then substitute those expressions into $H$.

## Particle Example

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

The Hamiltonian is:

$$
H=p\dot{x}-L
$$

Substitute $\dot{x}=p/m$:

$$
H=p\frac{p}{m}-\left(\frac{1}{2}m\left(\frac{p}{m}\right)^2-V(x)\right)
$$

So:

$$
H=\frac{p^2}{2m}+V(x)
$$

In this simple case, the Hamiltonian is the total energy. More generally, the Hamiltonian is defined by the Legendre transform.

## Intuition

A Legendre transform is useful when the slope is a more natural variable than the original variable.

In mechanics:

- the Lagrangian uses positions and velocities: $q,\dot{q}$
- the Hamiltonian uses positions and momenta: $q,p$

So the Legendre transform is the bridge from velocity language to momentum language.

## Common Confusions

- The Legendre transform is not just substituting $p$ for $\dot{q}$. First define $p=\partial L/\partial\dot{q}$, then solve for $\dot{q}$ in terms of $p$.
- The Hamiltonian is often energy, but its definition is the Legendre transform of the Lagrangian.
- The transform works cleanly only when the relation between the old variable and the new slope variable can be inverted.

## Related Concepts

- [Hamiltonian Mechanics](../Mechanics/Hamiltonian%20Mechanics.md)
- [Lagrangian Mechanics](../Mechanics/Lagrangian%20Mechanics.md)
- [Canonical Momentum](../Mechanics/Canonical%20Momentum.md)
- [Phase Space](../Mechanics/Phase%20Space.md)

<!-- semantic-edges
{"source":"Legendre Transforms","relation":"PART_OF","target":"Mathematics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mathematics area of the vault.","confidence":0.85}
{"source":"Legendre Transforms","relation":"MATHEMATICS_RELATED_TO","target":"Hamiltonian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Legendre Transforms with Hamiltonian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Legendre Transforms","relation":"MATHEMATICS_RELATED_TO","target":"Lagrangian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Legendre Transforms with Lagrangian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Legendre Transforms","relation":"MATHEMATICS_RELATED_TO","target":"Canonical Momentum","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Legendre Transforms with Canonical Momentum in its discussion or related-note links.","confidence":0.75}
{"source":"Legendre Transforms","relation":"MATHEMATICS_RELATED_TO","target":"Phase Space","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Legendre Transforms with Phase Space in its discussion or related-note links.","confidence":0.75}
-->
