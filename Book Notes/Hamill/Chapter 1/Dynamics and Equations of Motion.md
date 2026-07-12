# Dynamics and Equations of Motion

Source: [Hamill](../../../References/Hamill.pdf)

Book hub: [Hamill](../Hamill.md)

Chapter overview: [Chapter Overview](Chapter%20Overview.md)

Book sections: 1.9-1.10, printed pages 15-25.

Previous: [Constraints, Virtual Work, and Spaces](Constraints%20Virtual%20Work%20and%20Spaces.md)

Next: [Conservation Laws and Symmetry Principles](Conservation%20Laws%20and%20Symmetry%20Principles.md)

## Reading Status

- Status: started
- Pages: 15-25
- Date started: 2026-07-12
- Date finished:

## Purpose

Hamill uses these sections to compare Newton's equation-of-motion strategy with the Lagrangian strategy. At this point, Lagrange's equations are introduced as a tool rather than derived from first principles. The derivations come in Chapters 2 and 3.

## 1.9 Dynamics

Newtonian dynamics starts from force and momentum:

$$
\mathbf{F}=\frac{d\mathbf{p}}{dt}
$$

For constant mass:

$$
\mathbf{F}=m\mathbf{a}
$$

An equation of motion is a differential equation whose solution gives the motion. For a one-dimensional system:

$$
\ddot x=f(x,\dot x,t)
$$

Solving the equation gives $x(t)$ after initial conditions are specified.

## Newtonian Route

The Newtonian route typically asks:

1. identify all forces;
2. resolve them into coordinate components;
3. write force balance equations;
4. solve the resulting differential equations.

This works well for simple systems but becomes awkward when constraint forces are unknown or coordinates are not naturally Cartesian.

## 1.10 Lagrangian Route

The Lagrangian route starts by constructing:

$$
L=T-V
$$

Then it applies Lagrange's equations:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right)-\frac{\partial L}{\partial q_i}=0
$$

Hamill emphasizes that these are equations of motion. They are not merely a formal condition.

The method is procedural:

1. choose generalized coordinates;
2. write kinetic energy $T$;
3. write potential energy $V$;
4. form $L=T-V$;
5. apply one Lagrange equation for each independent coordinate.

## Mass On A Spring

For:

$$
L=\frac{1}{2}m\dot x^2-\frac{1}{2}kx^2
$$

Lagrange's equation gives:

$$
\frac{d}{dt}(m\dot x)-(-kx)=0
$$

so:

$$
m\ddot x+kx=0
$$

This reproduces the Newtonian simple harmonic oscillator.

## Atwood Machine

Hamill's Atwood machine example shows how a constraint can reduce the system to one coordinate. With string length fixed:

$$
x_1+x_2=l
$$

so:

$$
x_2=l-x_1
$$

The Lagrangian becomes a function of only $x_1$ and $\dot x_1$:

$$
L=\frac{1}{2}(m_1+m_2)\dot x_1^2+(m_1-m_2)gx_1+m_2gl
$$

The equation of motion is:

$$
\ddot x_1=\frac{m_1-m_2}{m_1+m_2}g
$$

The tension does not need to be solved for first because the constraint has been incorporated into the coordinate choice.

## Rolling Cylinder

For a cylinder rolling without slipping on another cylinder, Hamill writes kinetic energy as translational plus rotational energy:

$$
T=\frac{1}{2}m(\dot r^2+r^2\dot\theta^2)+\frac{1}{2}I\dot\phi^2
$$

The constraints fix $r$ and relate the angular variables. This example illustrates a common Lagrangian pattern: write the full energy, then use constraints to reduce it to the independent coordinate.

## Bead On A Rotating Hoop

For a bead on a rotating hoop, the coordinate is the bead angle on the hoop, while the hoop rotation is prescribed externally. The Lagrangian includes:

- kinetic energy from motion along the hoop;
- kinetic energy from the imposed rotation;
- gravitational potential energy.

This example is useful because the Lagrangian may include time-independent imposed motion even when not all motion is dynamical.

## Spherical Pendulum

For a spherical pendulum:

$$
x=l\sin\theta\cos\phi
$$

$$
y=l\sin\theta\sin\phi
$$

$$
z=l\cos\theta
$$

The Lagrangian is:

$$
L=\frac{1}{2}ml^2(\dot\theta^2+\sin^2\theta\dot\phi^2)-mgl\cos\theta
$$

The coordinate $\phi$ is cyclic, so:

$$
\frac{d}{dt}(ml^2\sin^2\theta\dot\phi)=0
$$

This example previews the conservation-law discussion that follows.

## What To Remember

- Lagrange's equations are introduced here as an equation-generating method.
- The derivation is intentionally postponed until Chapters 2 and 3.
- Constraints can simplify the Lagrangian before equations are written.
- The hard part is often choosing coordinates and writing $T$ and $V$ correctly.
- Cyclic coordinates can already be spotted in examples before the formal symmetry discussion.

## Links To Concept Notes

- [Lagrangian Mechanics](../../../Mechanics/Lagrangian%20Mechanics.md)
- [Euler-Lagrange Equations](../../../Mechanics/Euler-Lagrange%20Equations.md)
- [Constraints](../../../Mechanics/Constraints.md)
- [Cyclic Coordinates](../../../Mechanics/Cyclic%20Coordinates.md)

<!-- semantic-edges
{"source":"Hamill Section 1.10","relation":"INTRODUCES","target":"Lagrange's Equations","evidence_heading":"1.10 Lagrangian Route","evidence_summary":"The note presents Lagrange's equations as a practical tool for generating equations of motion from L = T - V.","confidence":0.92}
{"source":"Lagrangian Mechanics","relation":"REFORMULATES","target":"Newtonian Dynamics","evidence_heading":"Newtonian Route","evidence_summary":"The note contrasts Newtonian force-balance equations with the Lagrangian energy-based procedure for producing equations of motion.","confidence":0.88}
{"source":"Constraints","relation":"ENABLES","target":"Coordinate Reduction","evidence_heading":"Atwood Machine","evidence_summary":"The Atwood machine example uses the string-length constraint to reduce two coordinates to one before applying Lagrange's equation.","confidence":0.88}
-->
