# Center of Mass

## Definition

For particles with masses $m_i$, positions $\mathbf{r}_i$, and total mass $M=\sum_i m_i$, the center-of-mass position is

$$
\mathbf{R}=\frac{1}{M}\sum_i m_i\mathbf{r}_i
$$

Define each particle's position relative to the center of mass by

$$
\mathbf{r}'_i=\mathbf{r}_i-\mathbf{R}
$$

## Mass-Weighted Relative Positions

The mass-weighted sum of the relative positions is identically zero:

$$
\sum_i m_i\mathbf{r}'_i=\sum_i m_i(\mathbf{r}_i-\mathbf{R})=\sum_i m_i\mathbf{r}_i-\mathbf{R}\sum_i m_i=M\mathbf{R}-M\mathbf{R}=0
$$

This is not an additional physical assumption. It follows directly from defining $\mathbf{R}$ as the center of mass. In this sense, the center of mass is the origin of the primed coordinate system.

Differentiating the identity gives

$$
\sum_i m_i\dot{\mathbf{r}}'_i=0
$$

These identities make the cross terms vanish when total kinetic energy or angular momentum is separated into center-of-mass motion and internal motion.

## Related Concepts

- [Two-Body Problem](Two-Body%20Problem.md)
- [Conservation Laws](Conservation%20Laws.md)
- [Goldstein Section 1.2](../Book%20Notes/Goldstein/Chapter%201/Mechanics%20of%20a%20System%20of%20Particles.md)
