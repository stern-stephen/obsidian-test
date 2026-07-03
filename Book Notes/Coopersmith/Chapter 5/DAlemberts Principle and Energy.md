# D'Alembert's Principle and Energy

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 5.5, printed pages 102-104.

Previous: [Fictitious Forces](Fictitious%20Forces.md)

Next: [Review](Review.md)

## Reading Status

- Status: started
- Pages: 102-104
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- D'Alembert's principle becomes especially solvable when all relevant external conditions are time independent.
- Under those assumptions, virtual displacements can be identified with actual infinitesimal displacements.
- If applied forces come from a time-independent potential, energy conservation follows from D'Alembert's principle.
- Coopersmith presents conservation of energy as a result with assumptions, not as an unconditional statement.

## Energy Result

Under the special assumptions of time-independent external conditions, constant masses, rectangular particle coordinates, and applied forces derived from a potential, Coopersmith rewrites D'Alembert's principle in differential form.

For conservative applied forces:

$$
\mathbf{F}_i^{appl}=-\frac{\partial V}{\partial\mathbf{r}_i}
$$

The inertial term gives the differential of kinetic energy, so the principle leads to:

More explicitly, in this special case the virtual displacement can be replaced by the actual infinitesimal displacement:

$$
d\mathbf{r}_i=\dot{\mathbf{r}}_i dt
$$

Then the acceleration part satisfies:

$$
\sum_i m_i\ddot{\mathbf{r}}_i\cdot d\mathbf{r}_i=\sum_i m_i\ddot{\mathbf{r}}_i\cdot\dot{\mathbf{r}}_i dt=dT
$$

But D'Alembert's inertial force is the reversed acceleration term, $-m_i\ddot{\mathbf{r}}_i$, so its contribution is $-dT$. The conservative applied-force contribution is $-dV$. Thus D'Alembert's principle gives:

$$
-dV-dT=0
$$

or equivalently:

$$
d(T+V)=0
$$

Thus:

$$
T+V=\text{constant}
$$

## Interpretation

This section is important because it shows both the strength and the limits of the variational approach. Conservation of energy emerges naturally, but only after imposing assumptions about time independence and conservative applied forces.

## Links To Concept Notes

- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Energy Function](../../../Mechanics/Energy%20Function.md)
- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)

<!-- semantic-edges
{"source":"D'Alembert's Principle","relation":"DERIVES","target":"Energy Conservation","evidence_heading":"Energy Result","evidence_summary":"Under time-independent conservative assumptions, D'Alembert's principle leads to conservation of total energy.","confidence":0.9}
{"source":"Energy Conservation","relation":"ASSUMES","target":"Time-Independent External Conditions","evidence_heading":"Big Ideas","evidence_summary":"Coopersmith presents energy conservation as following only under special assumptions such as time-independent external conditions.","confidence":0.9}
-->
