# Introduction and Non-Interacting Particles

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 4.1-4.2, printed pages 59-63.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Rigid Bodies and Comparison with Newtonian Mechanics](Rigid%20Bodies%20and%20Comparison%20with%20Newtonian%20Mechanics.md)

## Reading Status

- Status: started
- Pages: 59-63
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Static equilibrium means the system is not moving, so the Newtonian force balance has no acceleration terms.
- Coopersmith introduces virtual work as a deliberately hypothetical "nudge" used to test equilibrium.
- For free, non-interacting particles, the principle of virtual work reproduces the Newtonian result that every force must vanish.
- The value of the method is not visible in this simplest case; it becomes useful when constraints and internal forces enter.

## Newtonian Statement

For $N$ non-interacting particles in static equilibrium, the Newtonian method gives one vector condition per particle:

$$
\mathbf{F}_1=0,\mathbf{F}_2=0,\ldots,\mathbf{F}_N=0
$$

If more than one force acts on a particle, Coopersmith treats their vector sum as the one resultant force at that particle.

## Virtual-Work Statement

The principle of virtual work replaces the separate vector force conditions with one summed scalar condition:

$$
\sum_{i=1}^{N}\delta\omega_i=0
$$

With ordinary forces and virtual displacements, this becomes:

$$
\sum_{i=1}^{N}\mathbf{F}_i\cdot\delta\mathbf{r}_i=0
$$

For free particles, the virtual displacements $\delta\mathbf{r}_i$ may be chosen independently in arbitrary directions. The only way the sum can vanish for all such choices is for each $\mathbf{F}_i$ to vanish separately.

## Interpretation

Coopersmith emphasizes that the virtual displacements are not physical motions during equilibrium. They are imagined infinitesimal changes in configuration space, used as a local stationarity test.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Classical Mechanics](../../../Mechanics/Classical%20Mechanics.md)
