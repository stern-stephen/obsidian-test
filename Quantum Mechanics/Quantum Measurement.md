# Quantum Measurement

## Overview

Quantum measurement connects the abstract state vector to observable outcomes. Unlike closed-system evolution, measurement is generally probabilistic and can change the state.

## Measurement Operators

A general measurement is described by measurement operators $\{M_m\}$, where $m$ labels the possible outcomes.

For a state $|\psi\rangle$, the probability of outcome $m$ is:

$$
p(m)=\langle \psi|M_m^\dagger M_m|\psi\rangle
$$

After observing outcome $m$, the state becomes:

$$
\frac{M_m|\psi\rangle}{\sqrt{p(m)}}
$$

The measurement operators satisfy:

$$
\sum_m M_m^\dagger M_m = I
$$

This guarantees that the probabilities of all outcomes add to $1$.

## Projective Measurements

Projective measurements use projection operators $P_m$ satisfying:

$$
P_mP_n=\delta_{mn}P_m
$$

and:

$$
\sum_m P_m=I
$$

The probability of outcome $m$ is:

$$
p(m)=\langle \psi|P_m|\psi\rangle
$$

Projective measurements are closely tied to Hermitian operators: the possible measurement outcomes are eigenvalues, and the projectors pick out the corresponding eigenspaces.

## POVMs

A POVM focuses on outcome probabilities. Its elements are:

$$
E_m=M_m^\dagger M_m
$$

with:

$$
\sum_m E_m=I
$$

The probability rule is:

$$
p(m)=\langle \psi|E_m|\psi\rangle
$$

POVMs are useful when the probabilities matter more than the post-measurement state.

## Related Book Notes

- [Nielsen and Chuang: Postulates of Quantum Mechanics](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Postulates%20of%20Quantum%20Mechanics.md#223-quantum-measurement)
- [Townsend: Stern-Gerlach Experiments](../Book%20Notes/Townsend/Chapter%201/Stern-Gerlach%20Experiments.md)
- [Shankar Chapter 4: Discussion of Postulates I-III](../Book%20Notes/Shankar/Chapter%204/Discussion%20of%20Postulates%20I-III.md)

## Related Concepts

- [Quantum Mechanics](Quantum%20Mechanics.md)
- [Quantum State Vector](Quantum%20State%20Vector.md)
- [Stern-Gerlach Experiments](Stern-Gerlach%20Experiments.md)
- [Projection Operators](../Linear%20Algebra/Projection%20Matrices.md)
- [Hermitian Operators](../Linear%20Algebra/Hermitian%20Matrices%20and%20Operators.md)
- [Density Operators](Density%20Operators.md)
