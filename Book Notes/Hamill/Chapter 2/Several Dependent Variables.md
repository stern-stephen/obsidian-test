# Several Dependent Variables

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book section: 2.3, printed pages 58-60.

Previous: [Variations and Alternate Euler-Lagrange Forms](Variations%20and%20Alternate%20Euler-Lagrange%20Forms.md)

Next: [Constrained Variational Problems](Constrained%20Variational%20Problems.md)

## Reading Status

- Status: started
- Pages: 58-60
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill generalizes the Euler-Lagrange derivation from one unknown function to several unknown functions. This matters for mechanics because a system usually has several generalized coordinates.

The one-function case uses:

$$
\Phi=\Phi(y,y',x)
$$

The many-function case uses:

$$
\Phi=\Phi(y_1,\ldots,y_n,y'_1,\ldots,y'_n,x)
$$

Each $y_i$ is a dependent variable, and all are functions of the same independent variable $x$.

## Stationary Integral

The functional is:

$$
I[y_1,\ldots,y_n]=\int_{x_i}^{x_f}\Phi(y_1,\ldots,y_n,y'_1,\ldots,y'_n,x)dx
$$

The task is to find the set of functions $y_i(x)$ that make this integral stationary.

The varied paths are:

$$
Y_i(x,\epsilon)=y_i(x)+\epsilon\eta_i(x)
$$

The endpoint conditions are:

$$
\eta_i(x_i)=\eta_i(x_f)=0
$$

for every $i$.

## Variation Of The Functional

The variation of the integrand is:

$$
\delta\Phi=\sum_i\left(\frac{\partial\Phi}{\partial y_i}\delta y_i+\frac{\partial\Phi}{\partial y'_i}\delta y'_i\right)
$$

Since:

$$
\delta y'_i=\frac{d}{dx}(\delta y_i)
$$

each derivative-of-variation term is integrated by parts:

$$
\int_{x_i}^{x_f}\frac{\partial\Phi}{\partial y'_i}\delta y'_i dx=\left[\frac{\partial\Phi}{\partial y'_i}\delta y_i\right]_{x_i}^{x_f}-\int_{x_i}^{x_f}\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'_i}\right)\delta y_i dx
$$

The boundary term vanishes for each $i$ because all endpoint variations vanish.

Thus:

$$
\delta I=\int_{x_i}^{x_f}\sum_i\left[\frac{\partial\Phi}{\partial y_i}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'_i}\right)\right]\delta y_i dx
$$

## Independent Variations

If the variables $y_i$ are independent, then the variations $\delta y_i$ can be chosen independently in the interior.

For the integral to vanish for every such choice, each coefficient must vanish separately:

$$
\frac{\partial\Phi}{\partial y_i}-\frac{d}{dx}\left(\frac{\partial\Phi}{\partial y'_i}\right)=0
$$

for:

$$
i=1,\ldots,n
$$

This gives $n$ Euler-Lagrange equations for $n$ unknown functions.

## Mechanics Translation

The mechanics version is obtained by making the replacements:

$$
x\rightarrow t
$$

$$
y_i\rightarrow q_i
$$

$$
\Phi\rightarrow L
$$

Then:

$$
\frac{\partial L}{\partial q_i}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)=0
$$

or equivalently:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

This is why Hamill places this section immediately before the later derivation of Lagrange's equations.

## Important Assumption

The conclusion that each coefficient vanishes separately depends on independence of the variations. If constraints relate the $y_i$, then the variations are not arbitrary and independent. That is the reason Section 2.4 introduces constraint methods.

## What To Remember

- One dependent variable gives one Euler-Lagrange equation.
- Several independent dependent variables give one Euler-Lagrange equation per variable.
- The derivation is the same as the one-variable case, repeated inside a sum.
- Constraints break the independence assumption and require extra machinery.

## Links To Concept Notes

- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Generalized Coordinates](../../../Mechanics/Generalized%20Coordinates.md)
- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)

<!-- semantic-edges
{"source":"Several Dependent Variables","relation":"GENERALIZES","target":"Euler-Lagrange Equation","evidence_heading":"Independent Variations","evidence_summary":"The note extends the one-function Euler-Lagrange condition to one equation for each independent dependent variable.","confidence":0.92}
{"source":"Independent Variations","relation":"REQUIRES","target":"Unconstrained Coordinates","evidence_heading":"Important Assumption","evidence_summary":"The note explains that separate Euler-Lagrange equations require independently choosable variations, which constraints can invalidate.","confidence":0.88}
-->
