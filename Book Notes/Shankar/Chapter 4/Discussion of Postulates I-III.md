# Discussion of Postulates I-III

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 4.2, pages 116-142.

Previous: [The Postulates](The%20Postulates.md)

Next: [The Schrodinger Equation](The%20Schrodinger%20Equation.md)

## Reading Status

- Status: started
- Pages: 116-142

## Notes

Shankar now unpacks the first three postulates rather than merely listing them. He moves among position components, arbitrary observable eigenbases, and probability amplitudes to show that the wavefunction is one representation of a state vector rather than a separate kind of state.

The reusable state, Born-rule, expectation-value, and projection formulas live in [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md) and [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md).

## Measurement And Collapse

Shankar stresses that measurement also prepares a state. Immediate repetition returns the same result because the first measurement leaves the system in the corresponding eigenstate or eigenspace. He contrasts this outcome-dependent collapse with smooth deterministic Schrodinger evolution.

Around page 122, Shankar's point is not that position and momentum can both be known arbitrarily well. A position measurement can be made so gentle that the momentum kick is small, but only by using a probe with poor position resolution. To know position sharply, the apparatus must localize the particle sharply, and that collapse produces a broad momentum spread. Conversely, a sharp momentum state is delocalized in position.

For approximate states, the tradeoff is summarized by:

$$
\Delta x \Delta p \geq \frac{\hbar}{2}
$$

Shankar then connects compatible observables with shared eigenvectors and commuting operators. Expectation values are ensemble averages over identically prepared systems, not hidden values assigned to individual systems before measurement.

## Links To Concept Notes

- [Quantum State Vector](../../../Quantum%20Mechanics/Quantum%20State%20Vector.md)
- [Quantum Measurement](../../../Quantum%20Mechanics/Quantum%20Measurement.md)
- [Postulates of Quantum Mechanics](../../../Quantum%20Mechanics/Postulates%20of%20Quantum%20Mechanics.md)
- [Commutators](../../../Linear%20Algebra/Commutators.md)
- [Projection Matrices](../../../Linear%20Algebra/Projection%20Matrices.md)

<!-- semantic-edges
{"source":"Shankar Section 4.2","relation":"REFORMULATES","target":"Quantum State Vector","evidence_heading":"Notes","evidence_summary":"Shows that the wavefunction is one representation of a state vector rather than a separate kind of state.","confidence":0.91}
{"source":"Measurement","relation":"ENABLES","target":"State Preparation","evidence_heading":"Measurement And Collapse","evidence_summary":"Stresses that a measurement leaves the system in the corresponding eigenstate or eigenspace, so immediate repetition gives the same result.","confidence":0.9}
{"source":"Measurement Collapse","relation":"CONTRASTS_WITH","target":"Schrodinger Evolution","evidence_heading":"Measurement And Collapse","evidence_summary":"Contrasts outcome-dependent collapse with smooth deterministic Schrodinger evolution.","confidence":0.89}
{"source":"Position Localization","relation":"DETERMINES","target":"Momentum Spread","evidence_heading":"Measurement And Collapse","evidence_summary":"Explains that sharp localization of position produces a broad momentum spread, summarized for approximate states by the uncertainty relation.","confidence":0.88}
{"source":"Commuting Operators","relation":"ENABLES","target":"Compatible Observables","evidence_heading":"Measurement And Collapse","evidence_summary":"Connects compatible observables with shared eigenvectors and commuting operators.","confidence":0.9}
{"source":"Expectation Values","relation":"REPRESENTS","target":"Ensemble Averages","evidence_heading":"Measurement And Collapse","evidence_summary":"Clarifies that expectation values are ensemble averages over identically prepared systems, not pre-existing hidden values for individuals.","confidence":0.88}
-->
