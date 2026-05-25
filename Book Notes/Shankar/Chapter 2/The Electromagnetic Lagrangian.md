# The Electromagnetic Lagrangian

Source: [Principles of Quantum Mechanics](../../../References/Principals%20of%20quantum%20mechanics%20Shankar%20.pdf)

Book hub: [Shankar](../Shankar.md)

Book section: 2.2.

Previous: [The Principle of Least Action and Lagrangian Mechanics](The%20Principle%20of%20Least%20Action%20and%20Lagrangian%20Mechanics.md)

Next: [The Two-Body Problem](The%20Two-Body%20Problem.md)

## Reading Status

- Status: started
- Pages:
- Date started: 2026-05-19
- Date finished:

## Big Ideas

- A charged particle in electromagnetic fields can still be described by a Lagrangian.
- The scalar potential $\phi$ and vector potential $\mathbf{A}$ enter the Lagrangian before the electric and magnetic fields appear.
- The canonical momentum differs from mechanical momentum when a vector potential is present.
- This distinction later becomes important in quantum mechanics, where canonical momentum becomes an operator.

## Notes

For a particle of charge $q$ and mass $m$, a common electromagnetic Lagrangian is:

$$
L = \frac{1}{2}m\dot{\mathbf{r}}^2 - q\phi + q\dot{\mathbf{r}}\cdot\mathbf{A}
$$

The canonical momentum is:

$$
\mathbf{p} = \frac{\partial L}{\partial \dot{\mathbf{r}}} = m\dot{\mathbf{r}} + q\mathbf{A}
$$

The mechanical momentum is:

$$
\mathbf{p}_{\text{mech}} = m\dot{\mathbf{r}}
$$

The two are related by:

$$
\mathbf{p}_{\text{mech}} = \mathbf{p} - q\mathbf{A}
$$

## Why This Matters

The potentials are not just computational conveniences in the quantum theory. The vector potential enters the phase of the wavefunction and appears in minimal coupling.

## Common Confusions

- Canonical momentum and mechanical momentum are not the same in electromagnetic fields.
- The vector potential can affect the Lagrangian even when the magnetic field is the quantity measured locally.
- Gauge choices can change the potentials without changing the physical fields.

## Links To Concept Notes

- [Electromagnetic Lagrangian](../../../Mechanics/Electromagnetic%20Lagrangian.md)
- [Canonical Momentum](../../../Mechanics/Canonical%20Momentum.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Classical Mechanics](../../../Mechanics/Classical%20Mechanics.md)
