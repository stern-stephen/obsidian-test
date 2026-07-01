# Semantic Edge Audit

This note tracks domain-level progress for evidence-backed semantic edges.

Use [README](README.md) as the source of truth for graph layers, edge format, relation vocabulary, edge quality rules, and the normal update workflow.

## Domain Progress

| Domain | Status | Notes |
| --- | --- | --- |
| Mechanics | Complete | Every durable Mechanics note has a semantic-edge block. Completed a quality pass for duplicate edges, weak relation labels, and top-level hub coverage. Future work should add edges only when Mechanics notes gain new durable conceptual relationships. |
| Mathematics | Complete | Every durable Mathematics note has a semantic-edge block. Added coverage for the Mathematics hub, calculus of variations, Legendre transforms, and Greek/Latin symbol conventions, with concept names aligned to existing Mechanics graph concepts. |
| Linear Algebra | Complete | Every durable Linear Algebra note has a semantic-edge block. Completed coverage for foundational vector-space notes, operator/eigenstructure notes, inner-product and quantum-interface notes, subspaces, elimination, decompositions, rotations, infinite-dimensional spaces, and Dirac delta, with duplicate triples and relation vocabulary checked. |
| Quantum Mechanics | Complete | Every durable Quantum Mechanics note has a semantic-edge block. Completed coverage for the hub, postulates, state vectors, measurement, density operators, composite systems, entanglement, spin, Stern-Gerlach experiments, Schrodinger evolution, and wave-particle duality, with duplicate triples and relation vocabulary checked. Subagents were used for parallel edge proposal review. |
| Quantum Computing | Complete | Every durable Quantum Computing note has a semantic-edge block. Completed coverage for the hub, Bloch sphere, qubits, quantum gates, tensor-product multi-qubit systems, and entanglement-linked protocols. |
| Book Notes | In progress | Book notes need source-specific semantic edges when they introduce, motivate, derive, or exemplify durable concepts. Started coverage with Shankar Chapter 1, keeping edges sparse and avoiding ordinary link mirroring. Continue with Shankar Chapters 2-4, Nielsen Chuang, Goldstein, Townsend, and a Coopersmith quality pass. |

## Mechanics Starting Set

Begin with these durable notes:

- [Mechanics](../Mechanics/Mechanics.md)
- [Virtual Work and D'Alembert's Principle](../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Constraints](../Mechanics/Constraints.md)
- [Generalized Coordinates](../Mechanics/Generalized%20Coordinates.md)
- [Lagrangian Mechanics](../Mechanics/Lagrangian%20Mechanics.md)
- [Action Principle](../Mechanics/Action%20Principle.md)
- [Euler-Lagrange Equations](../Mechanics/Euler-Lagrange%20Equations.md)
- [Hamiltonian Mechanics](../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../Mechanics/Phase%20Space.md)
- [Poisson Brackets](../Mechanics/Poisson%20Brackets.md)

Use linked Goldstein, Shankar, and Coopersmith notes as source-specific evidence rather than duplicating their prose into topic notes.
