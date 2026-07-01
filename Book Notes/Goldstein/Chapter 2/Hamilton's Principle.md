# Hamilton's Principle

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.1, printed pages 34-36.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Some Techniques of the Calculus of Variations](Some%20Techniques%20of%20the%20Calculus%20of%20Variations.md)

## Reading Status

- Status: started
- Pages: 34-36
- Date started: 2026-06-19
- Date finished:

## Differential And Integral Principles

D'Alembert's principle compares virtual displacements around one instantaneous configuration. Hamilton's principle instead compares complete motions between two fixed times. It is therefore an integral principle.

An $n$-degree-of-freedom system is represented by a point in configuration space with coordinates $(q_1,\ldots,q_n)$. Its history is a curve in that space. This curve represents the evolution of the entire configuration, not the spatial path of one particle.

## Action And Stationarity

For a monogenic system, whose applied forces derive from an ordinary or generalized potential, the action is:

$$
I[q]=\int_{t_1}^{t_2}L(q,\dot q,t)dt
$$

Hamilton's principle states:

$$
\delta I=0
$$

The comparison paths have the same configurations at $t_1$ and $t_2$. The actual path agrees with nearby paths to first order in the variation of the action.

More explicitly, a neighboring path may be written as:

$$
q_i(t,\epsilon)=q_i(t)+\epsilon\eta_i(t),\qquad \eta_i(t_1)=\eta_i(t_2)=0
$$

The varied paths satisfy the endpoint and kinematic restrictions, but they are not required to satisfy the equations of motion. Hamilton's principle selects the physical path by requiring the derivative of the action with respect to $\epsilon$ to vanish at $\epsilon=0$ for every admissible $\eta_i$.

The adjective "integral" refers to the action's dependence on the complete interval from $t_1$ to $t_2$. It does not imply that the resulting dynamics is nonlocal: arbitrary interior variations convert the stationary integral condition into the local Euler-Lagrange equations.

## Meaning Of Stationary

Stationary does not mean that the action must be the smallest possible value. The first variation may vanish at a minimum, maximum, or another stationary path. The principle determines the equations of motion without by itself classifying the stationary path.

## Scope And Significance

For holonomic systems, Hamilton's principle is equivalent to Lagrange's equations. Because the action is a scalar independent of the chosen generalized coordinates, the resulting equations retain their Lagrangian form under coordinate changes. This makes the action a useful starting postulate and prepares the extension from mechanics to field theories.

## Links To Concept Notes

- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)

<!-- semantic-edges
{"source":"Goldstein Section 2.1","relation":"INTRODUCES","target":"Hamilton's Principle","evidence_heading":"Action And Stationarity","evidence_summary":"States Hamilton's principle as stationarity of the action under fixed-endpoint path variations.","confidence":0.92}
{"source":"Hamilton's Principle","relation":"CONTRASTS_WITH","target":"D'Alembert's Principle","evidence_heading":"Differential And Integral Principles","evidence_summary":"Contrasts an instantaneous virtual-displacement principle with an integral principle comparing complete motions.","confidence":0.9}
{"source":"Configuration Space Curve","relation":"REPRESENTS","target":"System History","evidence_heading":"Differential And Integral Principles","evidence_summary":"A system history is represented by a curve in configuration space rather than the spatial path of one particle.","confidence":0.88}
{"source":"Fixed-Endpoint Variations","relation":"ASSUMES","target":"Hamilton's Principle","evidence_heading":"Action And Stationarity","evidence_summary":"Comparison paths share endpoint configurations and endpoint times while varying freely in the interior.","confidence":0.89}
{"source":"Stationary Action","relation":"CONTRASTS_WITH","target":"Minimum Action","evidence_heading":"Meaning Of Stationary","evidence_summary":"Goldstein stresses that vanishing first variation may indicate a minimum, maximum, or other stationary path.","confidence":0.89}
{"source":"Action Scalar","relation":"ENABLES","target":"Coordinate-Invariant Lagrange Equations","evidence_heading":"Scope And Significance","evidence_summary":"Because the action is a scalar independent of generalized coordinates, the Lagrangian form is preserved under coordinate changes.","confidence":0.88}
-->
