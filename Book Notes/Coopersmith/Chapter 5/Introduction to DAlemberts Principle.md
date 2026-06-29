# Introduction to D'Alembert's Principle

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 5.1, printed pages 88-92.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Worked Example and Intuition](Worked%20Example%20and%20Intuition.md)

## Reading Status

- Status: started
- Pages: 88-92
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- D'Alembert's principle extends virtual work from static equilibrium to dynamics.
- The key move is to treat $-m_i\mathbf{a}_i$ as an inertial force.
- Dynamics is rewritten as an equilibrium-like statement involving applied, constraint, and inertial forces.
- Ideal constraint forces still disappear when the virtual displacements are compatible with the constraints.

## Dynamical Virtual Work

For a particle with applied force, constraint force, and acceleration, Newton's law can be rearranged into an equilibrium-like form:

$$
\mathbf{F}_i^{appl}+\mathbf{F}_i^{cons}-m_i\mathbf{a}_i=0
$$

Multiplying by compatible virtual displacements and summing gives D'Alembert's principle:

$$
\sum_i\left(\mathbf{F}_i^{appl}-m_i\mathbf{a}_i\right)\cdot\delta\mathbf{r}_i=0
$$

The constraint-force terms are absent because the allowed virtual displacements do no work against ideal constraints.

## Interpretation

Coopersmith stresses that the principle is not just a formal trick. It changes the kind of question asked: instead of asking for the motion from the applied force alone, it asks for a virtual-work balance among the dynamical forces of the system.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Inertial Forces](../../../Mechanics/Inertial%20Forces.md)
- [Constraints](../../../Mechanics/Constraints.md)

<!-- semantic-edges
{"source":"Inertial Forces","relation":"ENABLES","target":"D'Alembert's Principle","evidence_heading":"Dynamical Virtual Work","evidence_summary":"The reversed mass-acceleration term lets dynamics be rewritten as an equilibrium-like virtual-work statement.","confidence":0.95}
{"source":"D'Alembert's Principle","relation":"ELIMINATES","target":"Ideal Constraint Forces","evidence_heading":"Dynamical Virtual Work","evidence_summary":"Constraint-force terms are absent because compatible virtual displacements do no work against ideal constraints.","confidence":0.9}
{"source":"D'Alembert's Principle","relation":"REFORMULATES","target":"Dynamics","evidence_heading":"Interpretation","evidence_summary":"The principle asks for a virtual-work balance among dynamical forces rather than only motion from applied force.","confidence":0.9}
-->
