# Problems

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 2.5, printed pages 67-69.

Previous: [Constrained Variational Problems](Constrained%20Variational%20Problems.md)

## Reading Status

- Status: not started
- Pages: 67-69
- Date started:
- Date finished:

## Problem Set Focus

Hamill's Chapter 2 problems practice translating geometric or physical questions into variational functionals, then using the Euler-Lagrange equation or a shortcut form to find the stationary curve.

The problem set is broader than the worked examples. It includes:

- generalizing the multiplier method to many coordinates and many constraints;
- geodesics on cones and cylinders;
- solids of revolution;
- variable endpoint conditions;
- minimum-time paths under gravity;
- soap films with minimal surface area;
- Fermat's principle for reflection and refraction;
- classical isoperimetric optimization problems.

## Skills To Practice

### Identify The Functional

The first step is usually not solving a differential equation. It is writing the correct integral:

$$
I[y]=\int \Phi(x,y,y')dx
$$

or, for parametrized curves:

$$
I[x,y]=\int \Phi(x,y,\dot x,\dot y,t)dt
$$

The integrand encodes the geometric or physical quantity being extremized: distance, time, area, moment of inertia, optical travel time, or surface area.

### Check For Missing Variables

Before applying the full Euler-Lagrange equation, check whether the integrand omits a variable.

If $\Phi$ omits $y$:

$$
\frac{\partial\Phi}{\partial y'}=\text{constant}
$$

If $\Phi$ omits $x$:

$$
\Phi-y'\frac{\partial\Phi}{\partial y'}=\text{constant}
$$

These shortcuts often reduce the problem from second order to first order.

### Handle Constraints Explicitly

For fixed-length or fixed-volume conditions, use a multiplier:

$$
\Phi\rightarrow\Phi+\lambda f
$$

The multiplier term should represent the constrained quantity in the same integral as the original functional.

### Watch Endpoint Conditions

Problem 2.5 introduces variable endpoints. This is where boundary terms can no longer be thrown away automatically.

For fixed endpoints:

$$
\delta y(x_1)=\delta y(x_2)=0
$$

For variable endpoints, the boundary terms from integration by parts produce extra endpoint conditions. These are often called natural boundary conditions or transversality conditions.

## Notes For Future Exercise Answers

- Do not reproduce full problem statements; use short references such as `### Problem 2.6`.
- For geometry problems, include a small derivation of the metric or line element before applying Euler-Lagrange.
- For minimum-time problems, derive the speed from energy conservation before writing $dt=ds/v$.
- For optics problems, start from Fermat's principle and keep track of which regions have which refractive index.
- For constrained extrema, state clearly whether $\lambda$ is a constant or a function.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Constraints](../../../Mechanics/Constraints.md)

<!-- semantic-edges
{"source":"Hamill Chapter 2 Problems","relation":"EXAMPLE_OF","target":"Calculus of Variations","evidence_heading":"Problem Set Focus","evidence_summary":"The problems ask the reader to formulate stationary distance, time, area, optics, and constrained-optimization questions as variational problems.","confidence":0.86}
-->
