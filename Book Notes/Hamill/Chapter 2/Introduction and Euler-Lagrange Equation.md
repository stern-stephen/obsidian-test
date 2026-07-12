# Introduction and Euler-Lagrange Equation

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 2.1-2.2, printed pages 44-52.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Variations and Alternate Euler-Lagrange Forms](Variations%20and%20Alternate%20Euler-Lagrange%20Forms.md)

## Reading Status

- Status: started
- Pages: 44-52
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill begins Chapter 2 by shifting from ordinary calculus to variational calculus. Ordinary calculus asks for the stationary value of a function at a point. Variational calculus asks for the stationary value of an integral whose input is an entire function.

This is the mathematical preparation for analytical mechanics. In mechanics, the function to be found will be a path $q(t)$, and the integral will become the action.

## From A Function To A Functional

The basic variational object is an integral:

$$
I[y]=\int_{x_i}^{x_f}\Phi(x,y,y')dx
$$

The symbol $\Phi$ is not merely an ordinary function of numbers. It depends on $y(x)$ and $y'(x)$, so it assigns a number to a whole candidate curve. Hamill calls this kind of object a functional.

For the shortest path in a plane:

$$
ds=\sqrt{dx^2+dy^2}
$$

Dividing by $dx$ gives:

$$
ds=\sqrt{1+y'^2} dx
$$

so the path length is:

$$
I[y]=\int_{x_i}^{x_f}\sqrt{1+y'^2} dx
$$

Here the functional integrand is:

$$
\Phi(y')=\sqrt{1+y'^2}
$$

This example is deliberately simple: because $\Phi$ has no explicit $y$ dependence, the Euler-Lagrange equation will reduce quickly to the equation of a straight line.

## The Brachistochrone Functional

Hamill also uses the brachistochrone as a less trivial example of how a variational problem is translated into a functional.

The physical question is: what curve lets a bead slide under gravity from one point to another in the least time? If $z$ is measured downward from the starting point, energy conservation gives:

$$
\frac{1}{2}mv^2=mgz
$$

Thus:

$$
v=\sqrt{2gz}
$$

Since $dt=ds/v$ and $ds=\sqrt{1+z'^2}dx$, the time functional is:

$$
I[z]=\int_{x_i}^{x_f}\sqrt{\frac{1+z'^2}{2gz}} dx
$$

In this case:

$$
\Phi(z,z')=\sqrt{\frac{1+z'^2}{2gz}}
$$

The integrand depends on $z$ and $z'$, but not explicitly on $x$. That fact makes one of the shortcut Euler-Lagrange forms useful later.

## The Geodesic Functional On A Sphere

For a sphere of radius $a$, Hamill writes the element of path in angular coordinates. If the curve is described by $\phi(\theta)$, then:

$$
ds^2=a^2d\theta^2+a^2\sin^2\theta d\phi^2
$$

This gives:

$$
ds=a\sqrt{1+\sin^2\theta \phi'^2} d\theta
$$

The corresponding functional is:

$$
I[\phi]=\int a\sqrt{1+\sin^2\theta \phi'^2} d\theta
$$

For finding the stationary curve, the constant factor $a$ does not change the Euler-Lagrange equation. The essential integrand is:

$$
\Phi(\theta,\phi')=\sqrt{1+\sin^2\theta \phi'^2}
$$

This example is useful because the independent parameter is now $\theta$, not $x$, showing that the Euler-Lagrange structure does not depend on the letter used for the parameter.

## Nearby Curves

To derive the Euler-Lagrange equation, Hamill compares the true stationary curve $y(x)$ with nearby curves:

$$
Y(x,\epsilon)=y(x)+\epsilon\eta(x)
$$

Here:

- $\epsilon$ labels the member of the family of nearby curves.
- $\eta(x)$ describes the shape of the deviation from $y(x)$.
- $\epsilon=0$ gives the candidate stationary path.
- The endpoints are fixed, so the deviation vanishes at the endpoints.

The fixed endpoint condition is:

$$
\eta(x_i)=\eta(x_f)=0
$$

The functional becomes a function of the path-label parameter:

$$
I(\epsilon)=\int_{x_i}^{x_f}\Phi(x,Y,Y')dx
$$

The stationary condition is:

$$
\left.\frac{dI}{d\epsilon}\right|_{\epsilon=0}=0
$$

This is the direct analog of setting a derivative equal to zero in ordinary calculus. The difference is that the derivative is taken through a family of functions rather than through a family of points.

## First Variation

Differentiate $I(\epsilon)$ under the integral:

$$
\frac{dI}{d\epsilon}=\int_{x_i}^{x_f}\left(\frac{\partial\Phi}{\partial Y}\frac{\partial Y}{\partial\epsilon}+\frac{\partial\Phi}{\partial Y'}\frac{\partial Y'}{\partial\epsilon}\right)dx
$$

Since $Y=y+\epsilon\eta$:

$$
\frac{\partial Y}{\partial\epsilon}=\eta(x)
$$

and:

$$
\frac{\partial Y'}{\partial\epsilon}=\eta'(x)
$$

The second term contains $\eta'$, but the final Euler-Lagrange condition needs to hold for arbitrary $\eta$. Integration by parts moves the derivative from $\eta$ onto the coefficient:

$$
\int_{x_i}^{x_f}\frac{\partial\Phi}{\partial Y'}\eta' dx=\left[\frac{\partial\Phi}{\partial Y'}\eta\right]_{x_i}^{x_f}-\int_{x_i}^{x_f}\frac{d}{dx}\left(\frac{\partial\Phi}{\partial Y'}\right)\eta dx
$$

The boundary term vanishes because $\eta(x_i)=\eta(x_f)=0$.

Therefore:

$$
\left.\frac{dI}{d\epsilon}\right|_{\epsilon=0}=\int_{x_i}^{x_f}\left[\frac{\partial\Phi}{\partial y}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)\right]\eta(x)dx
$$

The stationary condition requires this to vanish for every admissible interior variation $\eta(x)$.

## Why The Integrand Must Vanish

Hamill emphasizes the logic behind the final step. If:

$$
\int_{x_i}^{x_f}F(x)\eta(x)dx=0
$$

for every admissible function $\eta(x)$ that vanishes at the endpoints, then $F(x)$ must be zero throughout the interval.

Intuitively, because $\eta(x)$ is arbitrary in the interior, it can be chosen to probe any small region. If $F(x)$ were nonzero somewhere, one could choose $\eta(x)$ with the same sign there and make the integral nonzero.

Thus:

$$
\frac{\partial\Phi}{\partial y}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)=0
$$

This is the Euler-Lagrange equation for the stationary curve.

## Straight-Line Example

For the shortest path in a plane:

$$
\Phi=\sqrt{1+y'^2}
$$

There is no explicit $y$ dependence, so:

$$
\frac{\partial\Phi}{\partial y}=0
$$

The Euler-Lagrange equation becomes:

$$
\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)=0
$$

So:

$$
\frac{\partial\Phi}{\partial y'}=\text{constant}
$$

Compute the derivative:

$$
\frac{\partial\Phi}{\partial y'}=\frac{y'}{\sqrt{1+y'^2}}
$$

If this expression is constant, then $y'$ is constant. Therefore:

$$
y=mx+b
$$

The stationary curve is a straight line.

## Conceptual Takeaway

The derivation has three moving parts:

- fixed endpoint variations make the boundary term vanish;
- integration by parts turns $\eta'$ into $\eta$;
- arbitrariness of $\eta$ turns one global integral condition into a local differential equation.

This exact structure reappears in Hamilton's principle, with $x$ replaced by $t$, $y$ replaced by $q$, and $\Phi$ replaced by $L$.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Hamill Section 2.2","relation":"DERIVES","target":"Euler-Lagrange Equations","evidence_heading":"First Variation","evidence_summary":"The note derives the Euler-Lagrange equation by varying a fixed-endpoint curve, integrating by parts, and requiring the coefficient of an arbitrary interior variation to vanish.","confidence":0.95}
{"source":"Fixed Endpoint Variations","relation":"ENABLES","target":"Euler-Lagrange Equations","evidence_heading":"First Variation","evidence_summary":"The endpoint condition makes the integration-by-parts boundary term vanish, leaving the interior Euler-Lagrange condition.","confidence":0.92}
{"source":"Brachistochrone Problem","relation":"EXAMPLE_OF","target":"Calculus of Variations","evidence_heading":"The Brachistochrone Functional","evidence_summary":"The note constructs the time functional for a bead sliding under gravity, giving a classic variational problem.","confidence":0.9}
-->
