# Virtual Displacements

Source: [The Lazy Universe](../../../References/Coopersmith2017TheLazyUniverse.pdf)

Book hub: [Coopersmith](../Coopersmith.md)

Book section: 4.5-4.6, printed pages 68-71.

Previous: [Rigid Bodies and Comparison with Newtonian Mechanics](Rigid%20Bodies%20and%20Comparison%20with%20Newtonian%20Mechanics.md)

Next: [Generalized Coordinates](Generalized%20Coordinates.md)

## Reading Status

- Status: started
- Pages: 68-71
- Date started: 2026-06-28
- Date finished:

## Big Ideas

- Virtual displacements are chosen by the analyst, not caused by the actual dynamics of the system.
- They must occur simultaneously at the test point in configuration space.
- They must be compatible with the constraints, so that reaction forces do not contribute virtual work.
- Reversibility matters: allowed virtual displacements can be taken in either sign along an allowed direction.

## Guidelines For Virtual Displacements

Coopersmith's rules can be summarized as follows:

- Use virtual displacements wherever applied forces act.
- Treat the test as instantaneous: all virtual displacements occur at the same time.
- Attach each $\delta\mathbf{r}_i$ to the corresponding particle position.
- Choose directions that are compatible with the constraints.
- Let the virtual displacement magnitudes tend to zero in the stationarity test.

## Feynman's Pivoting Bar

Coopersmith uses Feynman's weighted bar as a concrete example. A rigid bar pivots about one end, with two known masses along the bar and an unknown hanging mass. The virtual displacements of the masses are not independent; rigidity of the bar fixes their ratios.

The virtual-work equation has the form:

$$
\sum_i W_i\delta r_i=0
$$

Using the displacement ratios in the example gives the unknown hanging mass. The point of the example is not the arithmetic but the constraint logic: one allowed virtual motion determines all three virtual displacements.

## Interpretation

The bar may be physically immovable, but the virtual displacement is still a valid mathematical probe. Coopersmith uses this to separate virtual motion from actual motion: virtual displacements are local, imagined, and constrained.

## Links To Concept Notes

- [Virtual Work and D'Alembert's Principle](../../../Mechanics/Virtual%20Work%20and%20DAlemberts%20Principle.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Constraints](../../../Mechanics/Constraints.md)
