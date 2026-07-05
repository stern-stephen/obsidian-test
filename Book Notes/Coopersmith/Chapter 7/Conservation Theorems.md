# Conservation Theorems

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 7.6-7.7, printed pages 161-166.

Previous: [Phase Fluid](Phase%20Fluid.md)

Next: [Hamilton-Jacobi Equation](Hamilton-Jacobi%20Equation.md)

## Reading Status

- Status: started
- Pages: 161-166
- Date started: 2026-07-05
- Date finished:

## Big Ideas

- Hamiltonian phase flow behaves like an incompressible fluid.
- Liouville's theorem says phase-space volume is conserved under Hamiltonian evolution.
- Symmetries make conserved momenta especially transparent in Hamiltonian form.
- If the Hamiltonian has no explicit time dependence, energy is conserved.
- Coopersmith also describes extended phase space as a way to geometrize explicitly time-dependent systems.

## Liouville And Circulation

Coopersmith compares phase-space flow with an ideal fluid. Liouville's theorem says a small volume element in phase space may change shape, but its volume remains constant. In this sense the phase fluid is incompressible.

She also discusses a circulation invariant, analogous to Helmholtz's circulation theorem for ideal fluids. The details are more advanced, but the main point is that Hamiltonian structure creates conserved geometric quantities in phase space.

## Symmetries And Momenta

If a coordinate is absent from the Hamiltonian, then the corresponding canonical momentum is conserved. For example, if $x$ does not occur in $H$, then:

$$
\dot{p}_x=-\frac{\partial H}{\partial x}=0
$$

So:

$$
p_x=\text{constant}
$$

This makes the symmetry-conservation link especially direct.

## Energy Conservation

If the Hamiltonian has no explicit time dependence, then Hamilton's equations imply:

$$
\frac{dH}{dt}=0
$$

Coopersmith emphasizes that this is a deduction from time-independence and the canonical equations, not an extra conservation postulate.

## Extended Phase Space

For systems with explicit time dependence, Coopersmith describes a more abstract move: treat time itself as an additional coordinate and introduce a new independent parameter. This extended phase-space picture can recast the problem into a conservative form.

## Links To Concept Notes

- [Conservation Laws](../../../Mechanics/Conservation%20Laws.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)

<!-- semantic-edges
{"source":"Hamiltonian Phase Flow","relation":"DETERMINES","target":"Phase-Space Volume Conservation","evidence_heading":"Liouville And Circulation","evidence_summary":"The note says Liouville's theorem preserves phase-space volume even as a volume element changes shape.","confidence":0.9}
{"source":"Absent Coordinate","relation":"DETERMINES","target":"Canonical Momentum Conservation","evidence_heading":"Symmetries And Momenta","evidence_summary":"If a coordinate is absent from H, Hamilton's equation makes its conjugate momentum constant.","confidence":0.95}
{"source":"Time-Independent Hamiltonian","relation":"DETERMINES","target":"Energy Conservation","evidence_heading":"Energy Conservation","evidence_summary":"The note says Hamilton's equations imply dH/dt = 0 when H has no explicit time dependence.","confidence":0.95}
-->
