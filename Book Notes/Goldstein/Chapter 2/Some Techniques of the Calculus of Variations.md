# Some Techniques of the Calculus of Variations

Source: [Classical Mechanics](../../../References/GoldsteinPooleSafkoClassicalMechanics.pdf)

Book hub: [Goldstein](../Goldstein.md)

Book section: 2.2, printed pages 36-43.

Previous: [Hamilton's Principle](Hamilton%27s%20Principle.md)

Next: [Derivation of Lagrange's Equations from Hamilton's Principle](Derivation%20of%20Lagrange%27s%20Equations%20from%20Hamilton%27s%20Principle.md)

## Reading Status

- Status: started
- Pages: 36-43
- Date started: 2026-06-19
- Date finished:

## Variational Problem

Given a functional:

$$
J[y]=\int_{x_1}^{x_2}f(y,y',x)dx
$$

seek a function $y(x)$ for which $J$ is stationary among nearby curves with fixed endpoints.

Introduce a one-parameter family:

$$
y(x,\alpha)=y(x,0)+\alpha\eta(x)
$$

where $\eta(x_1)=\eta(x_2)=0$. Stationarity requires:

$$
\left.\frac{dJ}{d\alpha}\right|_{\alpha=0}=0
$$

## Euler-Lagrange Equation

Differentiating under the integral and integrating the $y'$ term by parts gives:

$$
\delta J=\int_{x_1}^{x_2}\left[\frac{\partial f}{\partial y}-\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)\right]\delta y dx
$$

The endpoint term vanishes because $\delta y(x_1)=\delta y(x_2)=0$. Since the interior variation is arbitrary, the fundamental lemma implies:

$$
\frac{\partial f}{\partial y}-\frac{d}{dx}\left(\frac{\partial f}{\partial y'}\right)=0
$$

## Examples

### Shortest Plane Curve

For arc length:

$$
J=\int_{x_1}^{x_2}\sqrt{1+y'^2}dx
$$

the Euler-Lagrange equation implies constant slope, so the stationary path is a straight line.

### Minimum Surface Of Revolution

Rotating $x(y)$ about the $y$-axis gives an area functional proportional to:

$$
J=\int x\sqrt{1+y'^2}dx
$$

The smooth stationary curves are catenaries:

$$
x=a\cosh\left(\frac{y-b}{a}\right)
$$

Goldstein uses this example to stress that a smooth stationary solution need not be the absolute minimum and may not exist for every pair of endpoints. A nonsmooth competitor can sometimes do better.

### Brachistochrone

Using energy conservation, the travel time is:

$$
t_{12}=\int_1^2\frac{\sqrt{1+y'^2}}{\sqrt{2gy}}dx
$$

The minimizing curve is a cycloid, conveniently parameterized by:

$$
x=a(\phi-\sin\phi),\qquad y=a(1-\cos\phi)
$$

## Common Confusions

- The varied object is a function, not an ordinary number.
- Fixed endpoints remove the boundary term but do not force the variation to vanish in the interior.
- The Euler-Lagrange equation supplies a necessary stationary condition, not a general proof of a minimum.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)

<!-- semantic-edges
{"source":"Goldstein Section 2.2","relation":"INTRODUCES","target":"Calculus of Variations","evidence_heading":"Variational Problem","evidence_summary":"Introduces functionals and fixed-endpoint variations as the machinery for stationary path problems.","confidence":0.91}
{"source":"Fixed-Endpoint Variations","relation":"ELIMINATES","target":"Boundary Terms","evidence_heading":"Euler-Lagrange Equation","evidence_summary":"The endpoint term from integration by parts vanishes because the variations are fixed to zero at the endpoints.","confidence":0.89}
{"source":"Fundamental Lemma of Calculus of Variations","relation":"DERIVES","target":"Euler-Lagrange Equation","evidence_heading":"Euler-Lagrange Equation","evidence_summary":"Arbitrary interior variations force the Euler-Lagrange expression to vanish pointwise.","confidence":0.9}
{"source":"Minimum Surface of Revolution","relation":"EXAMPLE_OF","target":"Stationary Path Not Minimum","evidence_heading":"Minimum Surface Of Revolution","evidence_summary":"Goldstein uses the surface-of-revolution example to show that a smooth stationary solution need not be the absolute minimum.","confidence":0.87}
{"source":"Brachistochrone Problem","relation":"EXAMPLE_OF","target":"Calculus of Variations","evidence_heading":"Brachistochrone","evidence_summary":"The brachistochrone appears as a classic variational problem whose minimizing curve is a cycloid.","confidence":0.87}
-->
