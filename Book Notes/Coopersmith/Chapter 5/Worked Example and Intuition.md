# Worked Example and Intuition

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 5.2-5.3, printed pages 92-96.

Previous: [Introduction to D'Alembert's Principle](Introduction%20to%20DAlemberts%20Principle.md)

Next: [Fictitious Forces](Fictitious%20Forces.md)

## Reading Status

- Status: started
- Pages: 92-96
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- The worked example demonstrates how inertial forces join applied forces in a virtual-work sum.
- In simple one-particle cases, D'Alembert's principle may look like a rearrangement of Newton's second law.
- Coopersmith argues that this simple case gives misleading intuition because constrained many-body systems are the real target.
- The zero condition is one summed variational statement, not a particle-by-particle vector equality.

## Why It Can Look Trivial

For one unconstrained particle, D'Alembert's principle reduces to:

$$
\mathbf{F}-m\mathbf{a}=0
$$

That resembles Newton's second law. Coopersmith's point is that this resemblance hides the larger difference: D'Alembert's principle treats dynamics through a virtual-work balance, and that balance becomes genuinely useful when constraints and many mass points are present.

## Summed Condition

The principle permits the applied force at a point and the inertial response of the system to appear in different places. The important object is the total virtual work:

$$
\sum_i\left(\mathbf{F}_i^{appl}+\mathbf{I}_i\right)\cdot\delta\mathbf{r}_i=0
$$

where the inertial force is:

$$
\mathbf{I}_i=-m_i\mathbf{a}_i
$$

## Links To Concept Notes

- [Inertial Forces](../../../Mechanics/Inertial%20Forces.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)

<!-- semantic-edges
{"source":"D'Alembert's Principle","relation":"CONTRASTS_WITH","target":"Newton's Second Law","evidence_heading":"Why It Can Look Trivial","evidence_summary":"For one unconstrained particle the principle resembles Newton's second law, but Coopersmith emphasizes that the methods ask different questions.","confidence":0.85}
-->
