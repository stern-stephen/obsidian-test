# Commutators

## Overview

The commutator measures the failure of two operators to commute.

For operators $A$ and $B$:

$$
[A,B]=AB-BA
$$

If:

$$
[A,B]=0
$$

then $A$ and $B$ commute.

## Anti-Commutators

The anti-commutator is:

$$
\lbrace A,B\rbrace=AB+BA
$$

Anti-commutators appear in operator algebra, spin systems, and later quantum information calculations.

## Why It Matters

Commutators are important because operator order can matter. In quantum mechanics, non-commuting observables are tied to incompatibility of measurements and uncertainty relations.

For example, position and momentum do not commute:

$$
[X,P]=i\hbar I
$$

That algebraic fact encodes a physical limitation: the corresponding observables cannot both have arbitrarily sharp values in the same state.

## Related Book Notes

- [Nielsen and Chuang: Linear Algebra](../Book%20Notes/Nielsen%20Chuang/Chapter%202/Linear%20Algebra.md#219-commutators-and-anti-commutators)
- [Shankar: Linear Operators](../Book%20Notes/Shankar/Chapter%201/Linear%20Operators.md#products-and-commutators)

## Related Concepts

- [Linear Operators](Linear%20Operators.md)
- [Matrices](Matrices.md)
- [Hermitian Operators](Hermitian%20Matrices%20and%20Operators.md)
- [Quantum Mechanics](../Quantum%20Mechanics/Quantum%20Mechanics.md)

<!-- semantic-edges
{"source":"Commutators","relation":"DETERMINES","target":"Operator Noncommutativity","evidence_heading":"Overview","evidence_summary":"The note defines the commutator as AB - BA and says it measures the failure of two operators to commute.","confidence":0.95}
{"source":"Anti-Commutators","relation":"CONTRASTS_WITH","target":"Commutators","evidence_heading":"Anti-Commutators","evidence_summary":"The note defines anti-commutators as AB + BA, in contrast with the commutator AB - BA.","confidence":0.85}
{"source":"Noncommuting Observables","relation":"MOTIVATES","target":"Uncertainty Relations","evidence_heading":"Why It Matters","evidence_summary":"The note says non-commuting observables in quantum mechanics are tied to measurement incompatibility and uncertainty relations.","confidence":0.85}
-->
