# Infinitesimal Canonical Transformations and Invariants

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 5.4.1-5.4.3, printed pages 120-128.

Previous: [Poisson Brackets](Poisson%20Brackets.md)

Next: [Angular Momentum and Problems](Angular%20Momentum%20and%20Problems.md)

## Reading Status

- Status: started
- Pages: 120-128
- Date started: 2026-07-26
- Date finished:

## Purpose

This section explains how small canonical transformations are generated, why the Hamiltonian generates time evolution, and why phase-space volume is invariant.

## 5.4.1 Infinitesimal Canonical Transformations

An infinitesimal canonical transformation differs only slightly from the identity:

$$
Q_i=q_i+\delta q_i
$$

$$
P_i=p_i+\delta p_i
$$

Start from the identity-generating function and perturb it:

$$
F_2(q,P,t)=\sum_i q_iP_i+\epsilon G(q,P,t)
$$

To first order:

$$
\delta q_i=\epsilon\frac{\partial G}{\partial p_i}
$$

$$
\delta p_i=-\epsilon\frac{\partial G}{\partial q_i}
$$

In Poisson-bracket form, the change in any function $u$ is:

$$
\delta u=\epsilon\lbrace u,G\rbrace
$$

So $G$ is the generator of the infinitesimal canonical transformation.

## Hamiltonian As Generator Of Time Evolution

If $G=H$ and $\epsilon=dt$, the infinitesimal canonical transformation is time evolution:

$$
\delta u=dt\lbrace u,H\rbrace
$$

This is the compact meaning of saying the Hamiltonian generates motion. It generates the later phase-space variables from the earlier ones.

## Symmetries And Constants Of Motion

Hamill distinguishes two views of a canonical transformation:

- a passive change of variables that preserves the value of a function while changing its expression,
- an active transformation that moves the point in the same phase space and can change the value of a function.

For a generator $G$, Hamill obtains the link:

$$
\delta H=-\epsilon\frac{dG}{dt}
$$

If $G$ is a constant of motion, then $\delta H=0$. Conversely, if the Hamiltonian is invariant under the generated transformation, then $G$ is conserved. This is the Hamiltonian version of the symmetry-conservation connection.

## 5.4.2 Canonical Invariants

Hamill names three canonical invariants:

- the form of Hamilton's equations,
- Poisson brackets,
- phase-space volume elements.

The phase-space volume element is:

$$
d\tau=dq_1\cdots dq_n dp_1\cdots dp_n
$$

Under a canonical transformation:

$$
d\tau'=d\tau
$$

The proof reduces to showing that the Jacobian determinant for a canonical transformation is unity.

## 5.4.3 Liouville's Theorem

The phase fluid behaves like an incompressible fluid. Its velocity components are $\dot q_i$ and $\dot p_i$, and the incompressibility condition is:

$$
\sum_i\left(\frac{\partial\dot q_i}{\partial q_i}+\frac{\partial\dot p_i}{\partial p_i}\right)=0
$$

Using Hamilton's equations, the terms cancel. Therefore phase-space volume is preserved under time evolution.

Liouville's theorem says that the density of an ensemble of systems in phase space remains constant along the Hamiltonian flow. This is especially important in statistical mechanics, where each point in phase space represents a possible system with different initial conditions.

## Links To Concept Notes

- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Poisson Brackets](../../../Mechanics/Poisson%20Brackets.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Symmetries](../../../Mechanics/Symmetries.md)
- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)

<!-- semantic-edges
{"source":"Infinitesimal Canonical Transformation","relation":"GENERATED_BY","target":"Poisson Bracket Generator","evidence_heading":"5.4.1 Infinitesimal Canonical Transformations","evidence_summary":"The note states that a generator G changes any function by delta u = epsilon {u,G}.","confidence":0.95}
{"source":"Hamiltonian","relation":"GENERATES","target":"Time Evolution","evidence_heading":"Hamiltonian As Generator Of Time Evolution","evidence_summary":"Setting G = H and epsilon = dt makes the infinitesimal canonical transformation equal to time evolution.","confidence":0.95}
{"source":"Liouville's Theorem","relation":"FOLLOWS_FROM","target":"Canonical Volume Invariance","evidence_heading":"5.4.3 Liouville's Theorem","evidence_summary":"The note identifies Liouville's theorem with preservation of phase-space volume under Hamiltonian flow.","confidence":0.92}
-->
