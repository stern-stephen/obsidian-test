# Poisson Brackets

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 5.3-5.4, printed pages 117-120.

Previous: [Canonical Transformations](Canonical%20Transformations.md)

Next: [Infinitesimal Canonical Transformations and Invariants](Infinitesimal%20Canonical%20Transformations%20and%20Invariants.md)

## Reading Status

- Status: started
- Pages: 117-120
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill introduces Poisson brackets as the algebraic language of Hamiltonian mechanics. They make canonical transformations easier to test, express equations of motion compactly, and point toward quantum commutators.

## 5.3 Definition

For one canonical pair $(q,p)$ and functions $u(q,p)$ and $v(q,p)$:

$$
\lbrace u,v\rbrace=\frac{\partial u}{\partial q}\frac{\partial v}{\partial p}-\frac{\partial u}{\partial p}\frac{\partial v}{\partial q}
$$

For $n$ degrees of freedom:

$$
\lbrace u,v\rbrace=\sum_i\left(\frac{\partial u}{\partial q_i}\frac{\partial v}{\partial p_i}-\frac{\partial u}{\partial p_i}\frac{\partial v}{\partial q_i}\right)
$$

The fundamental brackets are:

$$
\lbrace q_i,q_j\rbrace=0
$$

$$
\lbrace p_i,p_j\rbrace=0
$$

$$
\lbrace q_i,p_j\rbrace=\delta_{ij}
$$

Hamill uses square brackets for Poisson brackets, but the durable vault notes use $\lbrace\ ,\ \rbrace$ to avoid confusion with commutators and ordinary grouping.

## Canonical Invariance

Poisson brackets are invariant under canonical transformations:

$$
\lbrace u,v\rbrace_{q,p}=\lbrace u,v\rbrace_{Q,P}
$$

This gives a practical canonical-coordinate test. If proposed variables $(Q_i,P_i)$ preserve the fundamental brackets, they are canonical.

## Basic Algebra

Hamill lists the key identities:

$$
\lbrace u,u\rbrace=0
$$

$$
\lbrace u,v\rbrace=-\lbrace v,u\rbrace
$$

$$
\lbrace au+bv,w\rbrace=a\lbrace u,w\rbrace+b\lbrace v,w\rbrace
$$

$$
\lbrace uv,w\rbrace=\lbrace u,w\rbrace v+u\lbrace v,w\rbrace
$$

and Jacobi's identity:

$$
\lbrace u,\lbrace v,w\rbrace\rbrace+\lbrace v,\lbrace w,u\rbrace\rbrace+\lbrace w,\lbrace u,v\rbrace\rbrace=0
$$

These identities make Poisson brackets into a structured algebra rather than just a computational trick.

## 5.4 Equations Of Motion

For any phase-space function $u(q,p,t)$:

$$
\frac{du}{dt}=\sum_i\left(\frac{\partial u}{\partial q_i}\dot q_i+\frac{\partial u}{\partial p_i}\dot p_i\right)+\frac{\partial u}{\partial t}
$$

Using Hamilton's equations:

$$
\frac{du}{dt}=\lbrace u,H\rbrace+\frac{\partial u}{\partial t}
$$

Taking $u=q_i$ or $u=p_i$ recovers Hamilton's equations:

$$
\dot q_i=\lbrace q_i,H\rbrace
$$

$$
\dot p_i=\lbrace p_i,H\rbrace
$$

If $u$ has no explicit time dependence, then $u$ is conserved when:

$$
\lbrace u,H\rbrace=0
$$

## Quantum Bridge

Hamill notes the structural replacement:

$$
\lbrace u,v\rbrace\leftrightarrow \frac{1}{i\hbar}(UV-VU)
$$

This is one of the chapter's bridges from classical Hamiltonian mechanics to quantum mechanics.

## Links To Concept Notes

- [Poisson Brackets](../../../Mechanics/Poisson%20Brackets.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Commutators](../../../Linear%20Algebra/Commutators.md)

<!-- semantic-edges
{"source":"Poisson Brackets","relation":"REFORMULATES","target":"Hamilton's Equations","evidence_heading":"5.4 Equations Of Motion","evidence_summary":"The note writes time evolution as du/dt = {u,H} + partial u / partial t, with q_i and p_i recovering Hamilton's equations.","confidence":0.95}
{"source":"Poisson Brackets","relation":"TESTS","target":"Canonical Transformations","evidence_heading":"Canonical Invariance","evidence_summary":"The note explains that preservation of the fundamental Poisson brackets tests whether variables are canonical.","confidence":0.93}
{"source":"Poisson Brackets","relation":"MOTIVATES","target":"Quantum Commutators","evidence_heading":"Quantum Bridge","evidence_summary":"Hamill points to the replacement of Poisson brackets by commutators divided by i hbar.","confidence":0.9}
-->
