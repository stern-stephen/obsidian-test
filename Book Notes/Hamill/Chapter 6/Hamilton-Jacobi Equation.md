# Hamilton-Jacobi Equation

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 6.1, printed pages 135-137.

Previous: [Chapter Overview](Chapter%20Overview.md)

Next: [Harmonic Oscillator and Principal Function](Harmonic%20Oscillator%20and%20Principal%20Function.md)

## Reading Status

- Status: started
- Pages: 135-137
- Date started: 2026-07-26
- Date finished:

## Purpose

Hamill frames the Hamilton-Jacobi method as a way to solve Hamilton's equations by transforming to variables that are constants. The solution of the dynamics is encoded in a generating function.

## Solving Dynamics As A Canonical Transformation

A complete solution gives:

$$
q=q(q_0,p_0,t)
$$

$$
p=p(q_0,p_0,t)
$$

This can be viewed as a canonical transformation from time-dependent variables $(q,p)$ to constant variables, identified with initial data.

For a canonical transformation:

$$
\dot Q_i=\frac{\partial K}{\partial P_i}
$$

$$
\dot P_i=-\frac{\partial K}{\partial Q_i}
$$

If the new variables are constants, then $\dot Q_i=\dot P_i=0$. Hamill achieves this by choosing:

$$
K=0
$$

Using:

$$
K=H+\frac{\partial F}{\partial t}
$$

gives:

$$
H+\frac{\partial F}{\partial t}=0
$$

## Hamilton's Principal Function

Choose a type-$F_2$ generating function:

$$
F_2(q,P,t)
$$

For historical reasons Hamill writes this function as $S$:

$$
S=S(q,P,t)
$$

This is Hamilton's principal function. The type-$F_2$ transformation rules give:

$$
p_i=\frac{\partial S}{\partial q_i}
$$

$$
Q_i=\frac{\partial S}{\partial P_i}
$$

The constants $P_i$ and $Q_i$ are usually renamed $\alpha_i$ and $\beta_i$.

## Hamilton-Jacobi Equation

Substitute:

$$
p_i=\frac{\partial S}{\partial q_i}
$$

into:

$$
H+\frac{\partial S}{\partial t}=0
$$

to obtain:

$$
H\left(q_1,\ldots,q_n;\frac{\partial S}{\partial q_1},\ldots,\frac{\partial S}{\partial q_n};t\right)+\frac{\partial S}{\partial t}=0
$$

This is the Hamilton-Jacobi equation.

## Recovering The Motion

Once $S(q_i,\alpha_i,t)$ is known:

$$
p_i=\frac{\partial S}{\partial q_i}
$$

and:

$$
\beta_i=\frac{\partial S}{\partial \alpha_i}
$$

If the second relation can be inverted, it gives:

$$
q_i=q_i(\alpha,\beta,t)
$$

Substituting that result into $p_i=\partial S/\partial q_i$ gives:

$$
p_i=p_i(\alpha,\beta,t)
$$

Thus the entire motion is recovered from derivatives of one function $S$.

## What The Method Gains And Costs

The gain is conceptual compression: a full system of Hamilton equations is replaced by one partial differential equation for $S$.

The cost is practical: the Hamilton-Jacobi equation may be hard to solve. Hamill emphasizes that systems solvable by this method are often easier by other methods, but the theoretical payoff is large.

## Links To Concept Notes

- [Hamilton-Jacobi Equation](../../../Mechanics/Hamilton-Jacobi%20Equation.md)
- [Canonical Transformations](../../../Mechanics/Canonical%20Transformations.md)
- [Hamiltonian Mechanics](../../../Mechanics/Hamiltonian%20Mechanics.md)
- [Phase Space](../../../Mechanics/Phase%20Space.md)

<!-- semantic-edges
{"source":"Hamilton-Jacobi Equation","relation":"SOLVES_BY","target":"Canonical Transformation To Constants","evidence_heading":"Solving Dynamics As A Canonical Transformation","evidence_summary":"The note frames the method as transforming q,p to constant variables by choosing K = 0.","confidence":0.95}
{"source":"Hamilton's Principal Function","relation":"GENERATES","target":"Hamilton-Jacobi Transformation","evidence_heading":"Hamilton's Principal Function","evidence_summary":"S is used as an F2 generating function whose derivatives give p_i and Q_i.","confidence":0.94}
-->
