# Advantages of a Variational Principle Formulation

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.5, printed pages 51-54.

Previous: [Extending Hamilton's Principle to Systems with Constraints](Extending%20Hamilton%27s%20Principle%20to%20Systems%20with%20Constraints.md)

Next: [Conservation Theorems and Symmetry Properties](Conservation%20Theorems%20and%20Symmetry%20Properties.md)

## Reading Status

- Status: started
- Pages: 51-54
- Date started: 2026-06-19
- Date finished:

## Coordinate Independence

Hamilton's principle packages the mechanics of holonomic, monogenic systems into a scalar statement involving kinetic and potential energies. Since the action does not depend on a particular coordinate description, the Euler-Lagrange form is preserved under changes of generalized coordinates.

## Freedom To Add A Total Derivative

If:

$$
L'=L+\frac{dF(q,t)}{dt}
$$

then the actions differ only by the endpoint value:

$$
I'=I+F(q(t_2),t_2)-F(q(t_1),t_1)
$$

Fixed endpoint variations make this extra contribution vanish, so $L$ and $L'$ produce the same equations of motion.

## Electrical-Mechanical Analogies

Using charge $q$ as the generalized coordinate, an $RL$ circuit is represented by:

$$
T=\frac{1}{2}\mathcal{L}\dot q^2,\qquad \mathcal{F}=\frac{1}{2}R\dot q^2,\qquad V=-\mathcal{E}q
$$

and Lagrange's equation with dissipation gives:

$$
\mathcal{L}\ddot q+R\dot q=\mathcal{E}
$$

For an $LC$ circuit:

$$
\mathcal{L}\ddot q+\frac{q}{C}=0,\qquad \omega_0=\frac{1}{\sqrt{\mathcal{L}C}}
$$

This has the same form as $m\ddot x+kx=0$. The analogies are:

| Electrical element | Mechanical role |
| --- | --- |
| Inductance $\mathcal{L}$ | Inertia or mass |
| Resistance $R$ | Viscous damping |
| Inverse capacitance $1/C$ | Spring constant |
| Charge $q$ | Displacement |
| Current $\dot q$ | Velocity |

Coupled inductors likewise correspond to coupled mechanical degrees of freedom.

## Broader Use

The same variational architecture applies to particle mechanics, fields, electromagnetism, and quantum theory. Once two systems share the form of a Lagrangian, solution techniques and structural insights can often be transferred between them.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Rayleigh Dissipation Function](../../../Mechanics/Rayleigh%20Dissipation%20Function.md)

<!-- semantic-edges
{"source":"Advantages of a Variational Principle Formulation","relation":"PART_OF","target":"Goldstein Chapter 2","evidence_heading":"Book metadata","evidence_summary":"This note is a source-specific section note in Goldstein Chapter 2.","confidence":0.85}
{"source":"Advantages of a Variational Principle Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Extending Hamilton's Principle to Systems with Constraints","evidence_heading":"Advantages of a Variational Principle Formulation","evidence_summary":"This source note explicitly links its treatment to Extending Hamilton's Principle to Systems with Constraints.","confidence":0.8}
{"source":"Advantages of a Variational Principle Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Conservation Theorems and Symmetry Properties","evidence_heading":"Advantages of a Variational Principle Formulation","evidence_summary":"This source note explicitly links its treatment to Conservation Theorems and Symmetry Properties.","confidence":0.8}
{"source":"Advantages of a Variational Principle Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Lagrangian Mechanics","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Lagrangian Mechanics.","confidence":0.8}
{"source":"Advantages of a Variational Principle Formulation","relation":"SOURCE_CONTEXT_FOR","target":"Action Principle","evidence_heading":"Links To Concept Notes","evidence_summary":"This source note explicitly links its treatment to Action Principle.","confidence":0.8}
-->
