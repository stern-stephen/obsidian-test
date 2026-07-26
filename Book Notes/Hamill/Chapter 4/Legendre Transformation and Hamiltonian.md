# Legendre Transformation and Hamiltonian

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 4.1-4.2, printed pages 93-97.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Canonical Equations and Phase Space](Canonical%20Equations%20and%20Phase%20Space.md)

## Reading Status

- Status: started
- Pages: 93-97
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill introduces the Legendre transform first as a mathematical operation, then uses it to define the Hamiltonian. The key conceptual move is replacing velocity variables by their conjugate momenta.

## 4.1 Legendre Transformation

Start with a function of active variables:

$$
f=f(u_1,u_2,\ldots,u_n)
$$

Define new variables by the slopes:

$$
v_i=\frac{\partial f}{\partial u_i}
$$

The Legendre transform is:

$$
g=\sum_i u_i v_i-f
$$

Differentiating gives:

$$
dg=\sum_i u_i dv_i
$$

so $g$ is naturally a function of the $v_i$, not the $u_i$. The inverse relation is:

$$
u_i=\frac{\partial g}{\partial v_i}
$$

This symmetry is the reason the transform is more than a relabeling: it trades a variable for the conjugate slope while preserving recoverability.

## Passive Variables

If the original function also depends on passive variables $w_i$, write:

$$
f=f(u_1,\ldots,u_n;w_1,\ldots,w_m)
$$

Only the $u_i$ participate in the transform. The transformed function keeps the passive variables:

$$
g=g(v_1,\ldots,v_n;w_1,\ldots,w_m)
$$

Hamill records the passive-variable relation:

$$
\frac{\partial g}{\partial w_i}=-\frac{\partial f}{\partial w_i}
$$

This sign is important when the transform is applied to the Lagrangian.

## Thermodynamic Aside

Hamill briefly points out the thermodynamic use of Legendre transforms: potentials such as Helmholtz free energy, enthalpy, and Gibbs free energy are obtained by trading variables like entropy or volume for temperature or pressure. This section is optional for the mechanics flow, but it reinforces the general idea that the "best" function depends on which variables are controlled.

## 4.2 Hamiltonian From The Lagrangian

The Lagrangian has the form:

$$
L=L(q_1,\ldots,q_n;\dot q_1,\ldots,\dot q_n;t)
$$

Hamill treats the velocities $\dot q_i$ as active variables, while $q_i$ and $t$ are passive variables. The new slope variables are the conjugate momenta:

$$
p_i=\frac{\partial L}{\partial \dot q_i}
$$

The Legendre transform of $L$ is the Hamiltonian:

$$
H(q_i,p_i,t)=\sum_i p_i\dot q_i-L(q_i,\dot q_i,t)
$$

After computing this expression, the velocities must be solved away. A valid Hamiltonian is a function of $q_i,p_i,t$, not $q_i,\dot q_i,t$.

## What To Remember

- The Hamiltonian is defined by a Legendre transform, not by the slogan $H=T+V$.
- The variables change from $(q,\dot q,t)$ to $(q,p,t)$.
- The definition only becomes operational after the momentum-velocity relation can be inverted.
- In many ordinary systems $H$ equals total energy, but Hamill delays that claim until after the canonical equations are derived.

## Links To Concept Notes

- [Legendre Transforms](../../../Mathematics/Legendre%20Transforms.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)

<!-- semantic-edges
{"source":"Hamill Chapter 4 Section 4.2","relation":"DEFINES","target":"Hamiltonian","evidence_heading":"4.2 Hamiltonian From The Lagrangian","evidence_summary":"The note defines the Hamiltonian as the Legendre transform H = sum p_i qdot_i - L, with velocities rewritten in terms of momenta.","confidence":0.95}
{"source":"Legendre Transform","relation":"REPLACES","target":"Velocity Variables","evidence_heading":"4.2 Hamiltonian From The Lagrangian","evidence_summary":"Hamill applies the Legendre transform using velocities as active variables and conjugate momenta as the new variables.","confidence":0.92}
-->
