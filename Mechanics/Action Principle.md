# Action Principle

## Overview

The action principle states that the physical path of a system makes the action stationary under small variations of the path.

## Definition

For generalized coordinates $q_i(t)$, the action is the functional:

$$
S[q] = \int_{t_1}^{t_2} L(q,\dot q,t)dt
$$

Hamilton's principle states that the physical motion is stationary relative to every sufficiently small admissible variation:

$$
\delta S = 0
$$

The comparison paths share fixed endpoint configurations and endpoint times. In an $n$-degree-of-freedom system, each complete motion is a curve in configuration space rather than the physical trajectory of a single particle.

## Admissible Variations

Write a one-parameter family of nearby paths as:

$$
q_i(t,\epsilon)=q_i(t)+\epsilon\eta_i(t)
$$

where the endpoint conditions are:

$$
\eta_i(t_1)=\eta_i(t_2)=0
$$

The functions $\eta_i(t)$ may otherwise be chosen independently in the interior. The physical path is stationary when:

$$
\left.\frac{d}{d\epsilon}S[q+\epsilon\eta]\right|_{\epsilon=0}=0
$$

This compares the physical history with nearby kinematically allowed histories. The varied paths are not alternative motions that must satisfy the equations of motion; they are the test paths used to derive those equations.

## From A Global Principle To Local Equations

The first variation is:

$$
\delta S=\int_{t_1}^{t_2}\sum_i\left(\frac{\partial L}{\partial q_i}\delta q_i+\frac{\partial L}{\partial\dot q_i}\delta\dot q_i\right)dt
$$

Since $\delta\dot q_i=d(\delta q_i)/dt$, integration by parts gives:

$$
\delta S=\left[\sum_i\frac{\partial L}{\partial\dot q_i}\delta q_i\right]_{t_1}^{t_2}+\int_{t_1}^{t_2}\sum_i\left[\frac{\partial L}{\partial q_i}-\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)\right]\delta q_i dt
$$

The boundary term vanishes because the endpoint configurations are fixed. Because the interior variations are arbitrary and independent, the remaining coefficient of each $\delta q_i$ must vanish:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

Hamilton's principle is therefore a global statement about complete paths whose stationarity implies the local Euler-Lagrange equations at every instant.

## Intuition

Instead of asking for the force at each instant, the action principle asks which whole path is consistent with the dynamics. The variational condition then produces local equations of motion.

The word "stationary" has the same first-order meaning as it does in ordinary calculus. If a path is changed by a small amount of order $\epsilon$, the action of a stationary path has no change proportional to $\epsilon$; its leading change is typically of order $\epsilon^2$. This does not determine the sign of that second-order change.

## Example: One Particle In A Potential

For one Cartesian coordinate with:

$$
L=\frac{1}{2}m\dot x^2-V(x)
$$

the Euler-Lagrange equation obtained from stationary action is:

$$
m\ddot x=-\frac{dV}{dx}
$$

Thus Hamilton's principle does not replace Newtonian dynamics with a different prediction. For this system it packages the same dynamics as a condition on an entire path.

## Scope

- Fixed endpoint times and configurations give the standard form of Hamilton's principle. Allowing endpoints to vary introduces additional boundary or transversality conditions.
- Holonomic constraints may be absorbed into independent generalized coordinates or retained with Lagrange multipliers.
- The familiar form $L=T-V$ applies to conservative systems, but the variational framework can also use generalized potentials and extends naturally to fields.
- Different Lagrangians can describe the same equations of motion. In particular, adding a total time derivative changes the action only by an endpoint contribution.

## Common Confusions

- Stationary action does not always mean minimum action.
- The trial paths in the variation are mathematical paths with fixed endpoints.
- Trial paths obey the imposed kinematic constraints but do not need to obey the equations of motion.
- The principle is not saying that a particle makes decisions.
- The first variation determines a stationary path but does not by itself classify it as a minimum, maximum, or other stationary point.
- Adding a total derivative $dF(q,t)/dt$ to $L$ changes the action only by a fixed endpoint term and therefore leaves the equations of motion unchanged.

## Related Concepts

- [Lagrangian Mechanics](Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](Euler-Lagrange%20Equations.md)
- [How Smart Is a Particle](../Book%20Notes/Shankar/Chapter%202/How%20Smart%20Is%20a%20Particle.md)
- [Calculus of Variations](../Mathematics/Calculus%20of%20Variations.md)
- [Goldstein Section 2.1](../Book%20Notes/Goldstein/Chapter%202/Hamilton%27s%20Principle.md)
- [Coopersmith Chapter 3](../Book%20Notes/Coopersmith/Chapter%203/Chapter%20Overview.md)

<!-- semantic-edges
{"source":"Action Principle","relation":"PART_OF","target":"Mechanics","evidence_heading":"Overview","evidence_summary":"This concept note belongs to the Mechanics area of the vault.","confidence":0.85}
{"source":"Action Principle","relation":"MECHANICS_RELATED_TO","target":"Lagrangian Mechanics","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Action Principle with Lagrangian Mechanics in its discussion or related-note links.","confidence":0.75}
{"source":"Action Principle","relation":"MECHANICS_RELATED_TO","target":"Euler-Lagrange Equations","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Action Principle with Euler-Lagrange Equations in its discussion or related-note links.","confidence":0.75}
{"source":"Action Principle","relation":"MECHANICS_RELATED_TO","target":"How Smart Is a Particle","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Action Principle with How Smart Is a Particle in its discussion or related-note links.","confidence":0.75}
{"source":"Action Principle","relation":"MECHANICS_RELATED_TO","target":"Calculus of Variations","evidence_heading":"Related Concepts","evidence_summary":"The note explicitly connects Action Principle with Calculus of Variations in its discussion or related-note links.","confidence":0.75}
-->
