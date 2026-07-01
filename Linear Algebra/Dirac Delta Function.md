# Dirac Delta Function

## Overview

The Dirac delta function $\delta(x-a)$ is best understood by what it does inside an integral.

It extracts the value of a function at a point:

$$
\int dx \delta(x-a)f(x) = f(a)
$$

It is not an ordinary function in the usual sense. It is a distribution, or generalized function.

## Continuous Version Of The Kronecker Delta

For a discrete orthonormal basis:

$$
\langle i|j\rangle = \delta_{ij}
$$

where $\delta_{ij}=1$ if $i=j$ and $0$ otherwise.

For a continuous basis:

$$
\langle x|x'\rangle = \delta(x-x')
$$

This says that two position basis kets are orthogonal unless their labels match, but the continuous case needs the delta distribution instead of ordinary $0$ and $1$ values.

## Identity Operator

In a discrete basis:

$$
I = \sum_i |i\rangle\langle i|
$$

In a continuous basis:

$$
I = \int dx |x\rangle\langle x|
$$

Acting on a state:

$$
\int dx |x\rangle\langle x|\psi\rangle = \int dx \psi(x)|x\rangle = |\psi\rangle
$$

## Derivative Of The Delta Function

The derivative $\delta'(x-a)$ is also defined by what it does inside an integral. The reliable rule is:

$$
\int_{-\infty}^{\infty} dx \delta'(x-a) f(x) = -f'(a)
$$

The minus sign comes from integration by parts:

$$
\int dx \delta'(x-a)f(x) = \left[\delta(x-a)f(x)\right]_{-\infty}^{\infty} - \int dx \delta(x-a)f'(x)
$$

The boundary term vanishes for the kinds of test functions used with distributions, leaving:

$$
\int dx \delta'(x-a)f(x) = -\int dx \delta(x-a)f'(x) = -f'(a)
$$

So $\delta'(x-a)$ does not pick out $f(a)$. It picks out the negative slope of $f$ at $a$.

More generally:

$$
\int dx \delta^{(n)}(x-a) f(x) = (-1)^n f^{(n)}(a)
$$

## Gaussian Approximation

One way to make the delta function less mysterious is to approach it with normalized Gaussians:

$$
\delta_{\epsilon}(x) = \frac{1}{\sqrt{2\pi}\epsilon} e^{-x^2/2\epsilon^2}
$$

Each $\delta_{\epsilon}(x)$ has total area $1$:

$$
\int_{-\infty}^{\infty} dx \delta_{\epsilon}(x) = 1
$$

As $\epsilon \to 0$, the Gaussian gets narrower and taller while keeping area $1$. In the distribution sense:

$$
\delta(x) = \lim_{\epsilon \to 0} \frac{1}{\sqrt{2\pi}\epsilon} e^{-x^2/2\epsilon^2}
$$

The phrase "distribution sense" matters. The pointwise limit is not an ordinary function. The meaningful statement is:

$$
\lim_{\epsilon \to 0} \int_{-\infty}^{\infty} dx \frac{1}{\sqrt{2\pi}\epsilon} e^{-x^2/2\epsilon^2} f(x) = f(0)
$$

For a delta centered at $a$:

$$
\delta(x-a) = \lim_{\epsilon \to 0} \frac{1}{\sqrt{2\pi}\epsilon} e^{-(x-a)^2/2\epsilon^2}
$$

## Fourier Representation

The Fourier representation is:

$\displaystyle \delta(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx} dk$

This integral is not an ordinary convergent integral. It is a distributional identity, meaning it is meant to be used inside an integral against a suitable function.

A more careful version starts with a finite cutoff:

$\displaystyle \delta_K(x)=\frac{1}{2\pi}\int_{-K}^{K} e^{ikx} dk$

Evaluating the integral gives:

$$
\delta_K(x) = \frac{\sin(Kx)}{\pi x}
$$

Then:

$$
\delta(x) = \lim_{K \to \infty} \frac{\sin(Kx)}{\pi x}
$$

Again, this is a distributional limit. Away from $x=0$ the expression oscillates more and more rapidly, so its contributions cancel when integrated against a smooth function. The surviving contribution is the value of the function at $x=0$.

For a shifted delta:

$\displaystyle \delta(x-a)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ik(x-a)} dk$

## Gaussian And Fourier Connection

The Gaussian approximation and Fourier representation are connected because the Fourier transform of a Gaussian is another Gaussian:

$\displaystyle \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx}e^{-\epsilon k^2/2} dk=\frac{1}{\sqrt{2\pi\epsilon}}e^{-x^2/2\epsilon}$

As $\epsilon \to 0$, the right side becomes $\delta(x)$ in the distribution sense. On the left side, the factor $e^{-\epsilon k^2/2}$ becomes a regulator that approaches $1$. This makes the formal identity

$\displaystyle \delta(x)=\frac{1}{2\pi}\int_{-\infty}^{\infty} e^{ikx} dk$

feel less like a trick: it is the limit of a well-behaved Gaussian-regulated Fourier integral.

## Common Confusions

- $\delta(x-a)$ is not a finite-height spike with area $1$. Treating it that way can be useful as intuition, but the integral rule is the reliable definition.
- $\delta(0)$ is not an ordinary number.
- $\delta'(x-a)$ samples $-f'(a)$, not $f'(a)$. The minus sign comes from moving the derivative off the delta function and onto the test function.
- The Gaussian and Fourier formulas are limits of distributions, not ordinary pointwise limits of functions.
- The delta function appears naturally when an orthonormal basis has a continuous label.

## Related Concepts

- [Infinite-Dimensional Vector Spaces](Infinite-Dimensional%20Vector%20Spaces.md)
- [Bra-Ket Notation](Bra-Ket%20Notation.md)
- [Projection Operators](Projection%20Matrices.md)
- [Shankar 1.10](../Book%20Notes/Shankar/Chapter%201/Infinite-Dimensional%20Spaces.md#kronecker-delta-to-dirac-delta)

<!-- semantic-edges
{"source":"Dirac Delta Function","relation":"REPRESENTS","target":"Point Evaluation","evidence_heading":"Overview","evidence_summary":"The note defines the Dirac delta by its integral action of extracting a function value at a point.","confidence":0.95}
{"source":"Dirac Delta Function","relation":"GENERALIZES","target":"Kronecker Delta","evidence_heading":"Continuous Version Of The Kronecker Delta","evidence_summary":"The note presents delta(x - x') as the continuous-basis analogue of the discrete Kronecker delta delta_ij.","confidence":0.9}
{"source":"Continuous Bases","relation":"REQUIRES","target":"Dirac Delta Function","evidence_heading":"Continuous Version Of The Kronecker Delta","evidence_summary":"The note says continuous position basis kets use the delta distribution rather than ordinary 0 and 1 values for orthogonality.","confidence":0.9}
{"source":"Dirac Delta Function","relation":"ENABLES","target":"Identity Operator","evidence_heading":"Identity Operator","evidence_summary":"The note writes the continuous identity operator as an integral over position kets and bras, which acts on a state using psi(x).","confidence":0.9}
{"source":"Delta Function Derivative","relation":"DETERMINES","target":"Derivative Sampling","evidence_heading":"Derivative Of The Delta Function","evidence_summary":"The note derives that integrating delta prime against a test function gives the negative derivative at the center.","confidence":0.9}
{"source":"Gaussian Approximation","relation":"MOTIVATES","target":"Dirac Delta Function","evidence_heading":"Gaussian Approximation","evidence_summary":"The note explains the delta as the distributional limit of normalized Gaussians that get narrower and taller while keeping area one.","confidence":0.85}
{"source":"Fourier Representation","relation":"MOTIVATES","target":"Dirac Delta Function","evidence_heading":"Fourier Representation","evidence_summary":"The note presents the Fourier integral for the delta as a distributional identity used under integrals against suitable functions.","confidence":0.85}
-->
