# Poisson Brackets

## Overview

Poisson brackets are algebraic operations on functions in phase space.

## Definition

For functions $f(q,p)$ and $g(q,p)$:

$$
\{f,g\} = \sum_i \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)
$$

## Key Equations

Time evolution can be written:

$$
\frac{df}{dt} = \{f,H\} + \frac{\partial f}{\partial t}
$$

The fundamental brackets are:

$$
\{q_i,p_j\} = \delta_{ij}
$$

$$
\{q_i,q_j\} = 0
$$

$$
\{p_i,p_j\} = 0
$$

## Useful Identities

For phase-space functions $f,g,h$ and constants $a,b$:

| Identity | Formula |
| --- | --- |
| Bilinearity | $\{af+bg,h\}=a\{f,h\}+b\{g,h\}$ |
| Antisymmetry | $\{f,g\}=-\{g,f\}$ |
| Product rule | $\{fg,h\}=f\{g,h\}+g\{f,h\}$ |
| Jacobi identity | $\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0$ |
| Coordinate derivative | $\{q_i,f\}=\frac{\partial f}{\partial p_i}$ |
| Momentum derivative | $\{p_i,f\}=-\frac{\partial f}{\partial q_i}$ |

## Proofs Of The Basic Identities

Start from the definition:

$$
\{f,g\} = \sum_i \left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)
$$

### Bilinearity

Compute the bracket of $af+bg$ with $h$:

$$
\{af+bg,h\}=\sum_i \left(\frac{\partial(af+bg)}{\partial q_i}\frac{\partial h}{\partial p_i}-\frac{\partial(af+bg)}{\partial p_i}\frac{\partial h}{\partial q_i}\right)
$$

Use linearity of partial derivatives:

$$
\frac{\partial(af+bg)}{\partial q_i}=a\frac{\partial f}{\partial q_i}+b\frac{\partial g}{\partial q_i}
$$

and:

$$
\frac{\partial(af+bg)}{\partial p_i}=a\frac{\partial f}{\partial p_i}+b\frac{\partial g}{\partial p_i}
$$

Substituting and grouping terms gives:

$$
\{af+bg,h\}=a\{f,h\}+b\{g,h\}
$$

The same argument works in the second slot, so the Poisson bracket is linear in each argument.

### Antisymmetry

Swap $f$ and $g$ in the definition:

$$
\{g,f\}=\sum_i \left(\frac{\partial g}{\partial q_i}\frac{\partial f}{\partial p_i}-\frac{\partial g}{\partial p_i}\frac{\partial f}{\partial q_i}\right)
$$

Since ordinary multiplication of functions commutes, rewrite the two products:

$$
\{g,f\}=\sum_i \left(\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}-\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}\right)
$$

This is exactly the negative of $\{f,g\}$:

$$
\{g,f\}=-\{f,g\}
$$

So:

$$
\{f,g\}=-\{g,f\}
$$

### Product Rule

Compute $\{fg,h\}$:

$$
\{fg,h\}=\sum_i \left(\frac{\partial(fg)}{\partial q_i}\frac{\partial h}{\partial p_i}-\frac{\partial(fg)}{\partial p_i}\frac{\partial h}{\partial q_i}\right)
$$

Use the ordinary product rule:

$$
\frac{\partial(fg)}{\partial q_i}=f\frac{\partial g}{\partial q_i}+g\frac{\partial f}{\partial q_i}
$$

and:

$$
\frac{\partial(fg)}{\partial p_i}=f\frac{\partial g}{\partial p_i}+g\frac{\partial f}{\partial p_i}
$$

Substitute:

$$
\{fg,h\}=\sum_i \left(f\frac{\partial g}{\partial q_i}\frac{\partial h}{\partial p_i}+g\frac{\partial f}{\partial q_i}\frac{\partial h}{\partial p_i}-f\frac{\partial g}{\partial p_i}\frac{\partial h}{\partial q_i}-g\frac{\partial f}{\partial p_i}\frac{\partial h}{\partial q_i}\right)
$$

Group the terms multiplied by $f$ and $g$:

$$
\{fg,h\}=f\{g,h\}+g\{f,h\}
$$

Using antisymmetry, the product rule in the second slot is:

$$
\{f,gh\}=g\{f,h\}+h\{f,g\}
$$

### Fundamental Brackets

For the coordinates themselves:

$$
\{q_i,q_j\}=\sum_k \left(\frac{\partial q_i}{\partial q_k}\frac{\partial q_j}{\partial p_k}-\frac{\partial q_i}{\partial p_k}\frac{\partial q_j}{\partial q_k}\right)
$$

Use:

$$
\frac{\partial q_i}{\partial q_k}=\delta_{ik}
$$

and:

$$
\frac{\partial q_i}{\partial p_k}=0
$$

Since $q_j$ has no $p_k$ dependence:

$$
\{q_i,q_j\}=0
$$

For two momenta, the same reasoning gives:

$$
\{p_i,p_j\}=0
$$

For position and momentum:

$$
\{q_i,p_j\}=\sum_k \left(\frac{\partial q_i}{\partial q_k}\frac{\partial p_j}{\partial p_k}-\frac{\partial q_i}{\partial p_k}\frac{\partial p_j}{\partial q_k}\right)
$$

Use:

$$
\frac{\partial q_i}{\partial q_k}=\delta_{ik}
$$

and:

$$
\frac{\partial p_j}{\partial p_k}=\delta_{jk}
$$

The second term vanishes, so:

$$
\{q_i,p_j\}=\sum_k \delta_{ik}\delta_{jk}=\delta_{ij}
$$

### Brackets With Coordinates And Momenta

Set $f=q_i$ in the definition:

$$
\{q_i,g\}=\sum_k \left(\frac{\partial q_i}{\partial q_k}\frac{\partial g}{\partial p_k}-\frac{\partial q_i}{\partial p_k}\frac{\partial g}{\partial q_k}\right)
$$

Using $\partial q_i/\partial q_k=\delta_{ik}$ and $\partial q_i/\partial p_k=0$ gives:

$$
\{q_i,g\}=\frac{\partial g}{\partial p_i}
$$

Similarly:

$$
\{p_i,g\}=-\frac{\partial g}{\partial q_i}
$$

These identities are a compact way to recover Hamilton's equations:

$$
\dot{q}_i=\{q_i,H\}=\frac{\partial H}{\partial p_i}
$$

and:

$$
\dot{p}_i=\{p_i,H\}=-\frac{\partial H}{\partial q_i}
$$

### Jacobi Identity

The Jacobi identity is:

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0
$$

A direct proof comes from substituting the definition of the Poisson bracket into each term and expanding. Every term contains one second derivative and two first derivatives. The terms cancel in pairs because mixed partial derivatives commute:

$$
\frac{\partial^2 f}{\partial q_i \partial p_j}=\frac{\partial^2 f}{\partial p_j \partial q_i}
$$

Conceptually, the Jacobi identity says that Poisson brackets have a consistent algebraic structure. This is why the Poisson bracket can serve as the classical analogue of the commutator algebra in quantum mechanics.

## Identities For Time Evolution

For any function $f(q,p,t)$:

$$
\frac{df}{dt}=\{f,H\}+\frac{\partial f}{\partial t}
$$

If $f$ has no explicit time dependence, then:

$$
\frac{df}{dt}=\{f,H\}
$$

So $f$ is conserved when:

$$
\{f,H\}=0
$$

This is the identity behind the symmetry-conservation connection in Hamiltonian mechanics.

## Quantum Bridge

Poisson brackets are the classical ancestor of quantum commutators. The structural analogy is:

$$
\{f,g\} \leftrightarrow \frac{1}{i\hbar}[F,G]
$$

## Related Concepts

- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Phase Space](Phase%20Space.md)
- [Canonical Transformations](Canonical%20Transformations.md)
- [Symmetries](Symmetries.md)
- [Commutators](../Linear%20Algebra/Commutators.md)
