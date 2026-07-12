# Hamiltons Principle and Variational Derivation

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 3.2-3.4, printed pages 73-77.

Previous: [DAlemberts Principle and Lagranges Equations](DAlemberts%20Principle%20and%20Lagranges%20Equations.md)

Next: [Constraints and Lagrange Multipliers](Constraints%20and%20Lagrange%20Multipliers.md)

## Reading Status

- Status: started
- Pages: 73-77
- Date started: 2026-07-12
- Date finished:

## Purpose

After deriving Lagrange's equations from d'Alembert's principle, Hamill derives them again from Hamilton's principle. This second derivation is the direct mechanics application of Chapter 2's calculus of variations.

## 3.2 Hamilton's Principle

At a given instant, the configuration of the system is specified by:

$$
\lbrace q_1,q_2,\ldots,q_{n-k}\rbrace
$$

As time evolves, the system traces a path in configuration space. There are infinitely many possible paths between the same initial and final configurations, but the physical path is selected by Hamilton's principle.

The action is:

$$
I=\int_{t_1}^{t_2}Ldt
$$

Hamilton's principle is:

$$
\delta\int_{t_1}^{t_2}Ldt=0
$$

Hamill describes this as the path that minimizes the action. More generally, the modern wording is that the physical path makes the action stationary; the first variation vanishes.

## Configuration-Space Interpretation

Hamilton's principle is a statement about complete paths, not instantaneous forces.

The endpoints are fixed:

$$
q_i(t_1)\quad\text{and}\quad q_i(t_2)
$$

The varied paths share these endpoints. The system's actual path is the one whose action has no first-order change under allowed variations.

This is why Chapter 2 matters: the action is a functional, and the physical path is found by applying variational calculus.

## 3.3 One-Coordinate Derivation

For one coordinate, write:

$$
L=L(t,q,\dot q)
$$

The action is:

$$
I[q]=\int_{t_i}^{t_f}L(t,q,\dot q)dt
$$

Applying the Euler-Lagrange equation from Chapter 2 with the substitutions:

$$
x\rightarrow t
$$

$$
y\rightarrow q
$$

$$
\Phi\rightarrow L
$$

gives:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q}\right)-\frac{\partial L}{\partial q}=0
$$

Hamill notes that this is customarily called Lagrange's equation in mechanics.

## 3.4 Many Coordinates

For many generalized coordinates:

$$
L=L(q_1,\ldots,q_n,\dot q_1,\ldots,\dot q_n,t)
$$

Use varied paths:

$$
Q_i(t)=q_i(t)+\epsilon\eta_i(t)
$$

with fixed endpoint conditions:

$$
\eta_i(t_1)=\eta_i(t_2)=0
$$

The variation of the action is:

$$
\delta I=\int_{t_1}^{t_2}\sum_i\left(\frac{\partial L}{\partial q_i}\delta q_i+\frac{\partial L}{\partial \dot q_i}\delta\dot q_i\right)dt
$$

Since:

$$
\delta\dot q_i=\frac{d}{dt}(\delta q_i)
$$

the second term is integrated by parts:

$$
\int_{t_1}^{t_2}\frac{\partial L}{\partial \dot q_i}\delta\dot q_i dt=\left[\frac{\partial L}{\partial \dot q_i}\delta q_i\right]_{t_1}^{t_2}-\int_{t_1}^{t_2}\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)\delta q_i dt
$$

The boundary term vanishes because the endpoints are fixed.

Thus:

$$
\delta I=\int_{t_1}^{t_2}\sum_i\left[\frac{\partial L}{\partial q_i}-\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)\right]\delta q_i dt
$$

Because the $\delta q_i$ are independent:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

for every $i$.

## What This Derivation Shows

The variational derivation turns a global path statement into local differential equations. Hamilton's principle says the action is stationary over the whole path. The Euler-Lagrange calculation says this is equivalent to Lagrange's equations at every time along the path.

## Links To Concept Notes

- [Hamilton's Principle](../../../Mechanics/Hamiltons%20Principle.md)
- [Action Principle](../../../Mechanics/Action%20Principle.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Calculus of Variations](../../../Mathematics/Calculus%20of%20Variations.md)

<!-- semantic-edges
{"source":"Hamilton's Principle","relation":"DERIVES","target":"Lagrange's Equations","evidence_heading":"3.4 Many Coordinates","evidence_summary":"The note derives Lagrange's equations from stationary action using fixed-endpoint variations and integration by parts.","confidence":0.95}
{"source":"Action Principle","relation":"REQUIRES","target":"Fixed Endpoint Variations","evidence_heading":"Configuration-Space Interpretation","evidence_summary":"The note explains that varied paths share fixed initial and final configurations in Hamilton's principle.","confidence":0.9}
{"source":"Calculus of Variations","relation":"ENABLES","target":"Hamilton's Principle","evidence_heading":"3.3 One-Coordinate Derivation","evidence_summary":"The note applies Chapter 2's Euler-Lagrange equation to the action by replacing x with t and Phi with L.","confidence":0.9}
-->
