# Two-Body Problem

## Overview

The two-body problem studies two interacting particles and often reduces their motion to center-of-mass motion plus relative motion.

## Key Coordinates

Center of mass:

$$
\mathbf{R} = \frac{m_1\mathbf{r}_1 + m_2\mathbf{r}_2}{m_1 + m_2}
$$

Relative coordinate:

$$
\mathbf{r} = \mathbf{r}_1 - \mathbf{r}_2
$$

Reduced mass:

$$
\mu = \frac{m_1m_2}{m_1 + m_2}
$$

## Intuition

The center of mass carries the overall motion of the pair. The relative coordinate carries the internal motion, which is often the physically interesting part.

## Quantum Bridge

The same reduction is used in quantum problems such as the hydrogen atom, where the electron-proton system is reduced to relative motion with reduced mass.

## Related Concepts

- [Classical Mechanics](Classical%20Mechanics.md)
- [Hamiltonian Mechanics](Hamiltonian%20Mechanics.md)
- [The Two-Body Problem](../Book%20Notes/Shankar/Chapter%202/The%20Two-Body%20Problem.md)

<!-- semantic-edges
{"source":"Two-Body Problem","relation":"REFORMULATES","target":"Relative Motion","evidence_heading":"Overview","evidence_summary":"The note says the two-body problem often reduces the motion of two interacting particles to center-of-mass motion plus relative motion.","confidence":0.95}
{"source":"Center of Mass","relation":"ENABLES","target":"Two-Body Reduction","evidence_heading":"Key Coordinates","evidence_summary":"The key coordinates include the center of mass, relative coordinate, and reduced mass used to rewrite the two-particle system.","confidence":0.9}
{"source":"Reduced Mass","relation":"REPRESENTS","target":"Two-Body Relative Motion","evidence_heading":"Key Coordinates","evidence_summary":"The note introduces reduced mass as the effective mass parameter for the relative-coordinate description.","confidence":0.85}
{"source":"Two-Body Reduction","relation":"MOTIVATES","target":"Hydrogen Atom","evidence_heading":"Quantum Bridge","evidence_summary":"The note says the same center-of-mass and relative-motion reduction is used in quantum problems such as the hydrogen atom.","confidence":0.85}
-->
