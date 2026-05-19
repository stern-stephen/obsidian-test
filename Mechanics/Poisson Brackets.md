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

## Quantum Bridge

Poisson brackets are the classical ancestor of quantum commutators. The structural analogy is:

$$
\{f,g\} \leftrightarrow \frac{1}{i\hbar}[F,G]
$$

## Related Concepts

- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [Phase Space](Phase%20Space.md)
- [Canonical Transformations](Canonical%20Transformations.md)
- [Commutators](../Linear%20Algebra/Commutators.md)
