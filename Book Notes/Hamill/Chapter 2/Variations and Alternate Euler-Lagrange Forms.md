# Variations and Alternate Euler-Lagrange Forms

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 2.2.1-2.2.2, printed pages 52-58.

Previous: [Introduction and Euler-Lagrange Equation](Introduction%20and%20Euler-Lagrange%20Equation.md)

Next: [Several Dependent Variables](Several%20Dependent%20Variables.md)

## Reading Status

- Status: started
- Pages: 52-58
- Date started: 2026-07-12
- Date finished:

## Why This Section Matters

After deriving the Euler-Lagrange equation, Hamill pauses to clarify notation. This is not cosmetic. The distinction between a differential and a variation is exactly what makes variational mechanics different from ordinary time evolution.

The section then gives two alternate forms of the Euler-Lagrange equation. These are useful because many classic problems have a missing variable in the integrand, creating a conserved quantity that reduces the order of the calculation.

## Differential Versus Variation

For a quantity $F(x,\dot x,t)$, the ordinary differential is:

$$
dF=\frac{\partial F}{\partial x}dx+\frac{\partial F}{\partial \dot x}d\dot x+\frac{\partial F}{\partial t}dt
$$

This means: move to a nearby point along the same function or trajectory, allowing the independent variable to change.

The variation is:

$$
\delta F=\frac{\partial F}{\partial x}\delta x+\frac{\partial F}{\partial \dot x}\delta\dot x
$$

This means: compare a nearby admissible function with the original one at the same independent-variable value. The independent parameter is frozen during the variation.

For a varied curve:

$$
Y(x,\epsilon)=y(x)+\epsilon\eta(x)
$$

the variation of $y$ is:

$$
\delta y=\eta(x)\delta\epsilon
$$

and the variation of the derivative is:

$$
\delta y'=\eta'(x)\delta\epsilon
$$

Because differentiation with respect to $x$ and variation through $\epsilon$ commute:

$$
\delta y'=\frac{d}{dx}(\delta y)
$$

This identity is one reason the integration-by-parts step in the Euler-Lagrange derivation works cleanly.

## Geometric Picture

For a curve $y=f(x)$, $dy$ compares nearby points on the same curve:

$$
dy=f(x+dx)-f(x)
$$

By contrast, $\delta y$ compares two different curves at the same $x$:

$$
\delta y=g(x)-f(x)
$$

In mechanics, this means a varied path is not the next instant of the same motion. It is a neighboring possible history used to test stationarity.

## First Variation Notation

Hamill connects two equivalent ways of expressing the same stationary condition.

One can write:

$$
\left.\frac{dI}{d\epsilon}\right|_{\epsilon=0}=0
$$

or:

$$
\delta I=0
$$

The first emphasizes that the functional becomes an ordinary function of the path-family parameter $\epsilon$. The second emphasizes the variational change of the functional.

For:

$$
I[y]=\int_{x_1}^{x_2}\Phi(y,y',x)dx
$$

the first variation is:

$$
\delta I=\int_{x_1}^{x_2}\left(\frac{\partial\Phi}{\partial y}\delta y+\frac{\partial\Phi}{\partial y'}\delta y'\right)dx
$$

After integration by parts and fixed endpoint conditions:

$$
\delta I=\int_{x_1}^{x_2}\left[\frac{\partial\Phi}{\partial y}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)\right]\delta y dx
$$

This motivates the functional derivative:

$$
\frac{\delta\Phi}{\delta y}=\frac{\partial\Phi}{\partial y}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)
$$

The stationary condition is $\delta\Phi/\delta y=0$ inside the interval.

## First Alternate Form: No Explicit y Dependence

Start with:

$$
\frac{\partial\Phi}{\partial y}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)=0
$$

If $\Phi$ does not depend explicitly on $y$, then:

$$
\frac{\partial\Phi}{\partial y}=0
$$

So:

$$
\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)=0
$$

Hence:

$$
\frac{\partial\Phi}{\partial y'}=\text{constant}
$$

This is analogous to a cyclic coordinate in Lagrangian mechanics. If the integrand ignores a variable, the conjugate quantity associated with that variable is constant.

## Second Alternate Form: No Explicit x Dependence

If $\Phi=\Phi(y,y')$ has no explicit $x$ dependence, Hamill derives:

$$
\Phi-y'\frac{\partial\Phi}{\partial y'}=\text{constant}
$$

This is often called the Beltrami identity. It follows by differentiating $\Phi$ with respect to $x$:

$$
\frac{d\Phi}{dx}=\frac{\partial\Phi}{\partial y}y'+\frac{\partial\Phi}{\partial y'}y''
$$

Then use the Euler-Lagrange equation to replace:

$$
\frac{\partial\Phi}{\partial y}=\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)
$$

The result becomes:

$$
\frac{d\Phi}{dx}=y'\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'}\right)+y''\frac{\partial\Phi}{\partial y'}
$$

The right side is:

$$
\frac{d}{dx}\left(y'\frac{\partial\Phi}{\partial y'}\right)
$$

Therefore:

$$
\frac{d}{dx}\left(\Phi-y'\frac{\partial\Phi}{\partial y'}\right)=0
$$

so the quantity in parentheses is constant.

## Brachistochrone Reduction

For the brachistochrone:

$$
\Phi(z,z')=\sqrt{\frac{1+z'^2}{2gz}}
$$

There is no explicit $x$ dependence, so:

$$
\Phi-z'\frac{\partial\Phi}{\partial z'}=\text{constant}
$$

Ignoring the constant factor involving $2g$, one can use:

$$
\Phi=\sqrt{\frac{1+z'^2}{z}}
$$

The derivative with respect to $z'$ is:

$$
\frac{\partial\Phi}{\partial z'}=\frac{z'}{\sqrt{z}\sqrt{1+z'^2}}
$$

Then:

$$
\Phi-z'\frac{\partial\Phi}{\partial z'}=\frac{1}{\sqrt{z}\sqrt{1+z'^2}}
$$

Setting this equal to a constant gives:

$$
z(1+z'^2)=C
$$

This first-order equation is much easier than the full second-order Euler-Lagrange equation.

## Cycloid Parametrization

Hamill solves the brachistochrone equation by setting:

$$
z'=\cot\alpha
$$

Then:

$$
1+z'^2=\csc^2\alpha
$$

so:

$$
z=C\sin^2\alpha
$$

Using a change of parameter gives the cycloid:

$$
x=A(\theta-\sin\theta)
$$

$$
z=A(1-\cos\theta)
$$

The result is important because the fastest path is not the straight line. The variational principle selects the curve that optimizes time under gravity, not geometric length.

## What To Remember

- $d$ moves along a curve; $\delta$ moves between curves.
- Fixed endpoints mean endpoint variations vanish.
- $\delta y'$ equals $d(\delta y)/dx$.
- If $\Phi$ omits $y$, then $\partial\Phi/\partial y'$ is constant.
- If $\Phi$ omits $x$, then $\Phi-y'\partial\Phi/\partial y'$ is constant.
- The brachistochrone uses the no-explicit-$x$ shortcut and gives a cycloid.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)

<!-- semantic-edges
{"source":"Variation","relation":"CONTRASTS_WITH","target":"Differential","evidence_heading":"Differential Versus Variation","evidence_summary":"The note distinguishes moving along one function from comparing neighboring functions at fixed independent parameter.","confidence":0.92}
{"source":"No Explicit Independent Variable","relation":"DETERMINES","target":"Beltrami Identity","evidence_heading":"Second Alternate Form: No Explicit x Dependence","evidence_summary":"The note derives the conserved quantity Phi minus y prime times partial Phi over partial y prime when the integrand has no explicit independent-variable dependence.","confidence":0.9}
{"source":"Beltrami Identity","relation":"ENABLES","target":"Brachistochrone Solution","evidence_heading":"Brachistochrone Reduction","evidence_summary":"The no-explicit-x identity reduces the brachistochrone variational problem to the first-order equation z times one plus z prime squared equals a constant.","confidence":0.9}
-->
