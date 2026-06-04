# Chapter 1 — Time-Independent Perturbation Theory

## TL;DR

- Most quantum systems have no exact solution. Perturbation theory extracts approximate answers by treating a hard Hamiltonian as a solvable one plus a small correction.
- The first-order energy shift is simply the expectation value of the perturbation in the unperturbed state: $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$.
- The second-order energy correction mixes in nearby states; its denominator structure signals breakdown near degeneracy.
- For the ground state, the second-order correction is always negative — a provable theorem, not a coincidence.
- Perturbation series almost always diverge, yet truncating at the optimal order gives exponentially accurate answers (Dyson/Bender–Wu).

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember** the setup $\hat{H} = \hat{H}_0 + \lambda\hat{H}'$ and explain why it generates a power series in $\lambda$. *(Bloom: Remember)*
2. **Apply** the first-order formula $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$ to compute energy shifts using ladder-operator matrix elements. *(Bloom: Apply)*
3. **Apply** the second-order formula $E_n^{(2)} = \sum_{m\neq n}|\langle m|\hat{H}'|n\rangle|^2/(E_n^{(0)}-E_m^{(0)})$ and identify when the denominator signals breakdown. *(Bloom: Apply)*
4. **Analyze** the small-denominator structure to diagnose when nondegenerate perturbation theory fails. *(Bloom: Analyze)*
5. **Evaluate** the Dyson argument for why perturbation series generically diverge and what "optimal truncation" means in practice. *(Bloom: Evaluate)*

---

## A quantum mechanic with a bad wrench

A quantum mechanic opens her toolbox and finds exactly three tools: the harmonic oscillator, the hydrogen atom, and the infinite square well. Every other bound-state problem in three dimensions — helium, lithium, the ammonia molecule, an electron in a doped semiconductor — is not on the solved list. Yet physicists routinely compute energy levels for all of these, often to high precision. How?

The secret is that most real Hamiltonians are close to a solvable one. Helium is hydrogen-with-a-second-electron, and that second electron is a perturbation on the Coulomb background. An oscillator with a stiff spring and a small cubic or quartic attachment is almost a harmonic oscillator. An atom in a weak electric field is almost a free atom.

Perturbation theory is the art of squeezing answers from "almost." It takes the distance from the solvable case — encoded in a small parameter $\lambda$ — and turns it into a systematic expansion. The zeroth-order term is the exact answer you already have. Each successive term corrects it a little further, at the cost of one more integral.

This chapter builds the machine for the non-degenerate case: when the unperturbed levels are all distinct. The quartic oscillator $\hat{H} = \hat{H}_\text{HO} + \lambda\hat{x}^4$ is the canonical worked example, because its exact solution is accessible by numerical diagonalization, so you can watch the approximation depart from truth as $\lambda$ grows. The degenerate case — when two or more levels share an energy — gets its own chapter (Chapter 2), where the stakes are higher: hydrogen fine structure and the Stark effect.

---

## The setup

You have a Hamiltonian $\hat{H}_0$ whose energy eigenstates $|n^{(0)}\rangle$ and eigenvalues $E_n^{(0)}$ you know exactly. Reality gives you:

$$\hat{H} = \hat{H}_0 + \lambda\hat{H}'$$

where $\hat{H}'$ is an additional term — the **perturbation** — and $\lambda$ is a dimensionless small parameter, a knob you can imagine slowly turning from zero. When $\lambda = 0$ you recover the solvable problem. When $\lambda = 1$, you have the physical Hamiltonian.

The strategy: expand both the energy and the state as power series in $\lambda$:

$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots$$

$$|n\rangle = |n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \lambda^2|n^{(2)}\rangle + \cdots$$

Here $E_n^{(k)}$ is the $k$-th order energy correction (a number) and $|n^{(k)}\rangle$ is the $k$-th order state correction (a ket). Substitute into the full Schrödinger equation $\hat{H}|n\rangle = E_n|n\rangle$ and collect terms at each power of $\lambda$. The whole machine lives in that one substitution.

One normalization convention is useful: require $\langle n^{(0)}|n^{(k)}\rangle = 0$ for all $k \geq 1$. This means the correction kets are orthogonal to the zeroth-order state, which simplifies every inner product.

---

## What the machine gives you

### Zeroth order

Collecting the $\lambda^0$ terms gives $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$. This is just the original solved problem. No new information.

### First-order energy correction

At order $\lambda^1$, the Schrödinger equation becomes:

$$\hat{H}_0|n^{(1)}\rangle + \hat{H}'|n^{(0)}\rangle = E_n^{(0)}|n^{(1)}\rangle + E_n^{(1)}|n^{(0)}\rangle$$

Take the inner product with $\langle n^{(0)}|$ on both sides. The left term $\langle n^{(0)}|\hat{H}_0|n^{(1)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle = 0$ (by our normalization convention and the fact that $\hat{H}_0$ is Hermitian). The $E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle$ term on the right also vanishes for the same reason. What remains is remarkably clean:

$$\boxed{E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle}$$

**The first-order energy shift is the expectation value of the perturbation in the unperturbed state.** That is all. No sum, no diagonalization — just one matrix element. If you can compute that integral, you have the leading correction.

### First-order state correction

To find the corrected state, take the inner product of the first-order equation with a *different* unperturbed state $\langle m^{(0)}|$ where $m \neq n$:

$$\langle m^{(0)}|\hat{H}_0|n^{(1)}\rangle + \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle = E_n^{(0)}\langle m^{(0)}|n^{(1)}\rangle + E_n^{(1)}\underbrace{\langle m^{(0)}|n^{(0)}\rangle}_{0}$$

Since $\hat{H}_0$ is Hermitian, $\langle m^{(0)}|\hat{H}_0 = E_m^{(0)}\langle m^{(0)}|$, so the left side gives $(E_m^{(0)} - E_n^{(0)})\langle m^{(0)}|n^{(1)}\rangle + \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle = 0$. Solving for $\langle m^{(0)}|n^{(1)}\rangle$ and inserting completeness:

$$\boxed{|n^{(1)}\rangle = \sum_{m \neq n}\frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle}$$

Read this carefully. The perturbation **mixes** states into each other. The amount of mixing between $|m\rangle$ and $|n\rangle$ depends on two things: how strongly the perturbation connects them (the numerator $\langle m|\hat{H}'|n\rangle$) and how far apart they are in energy (the denominator $E_n^{(0)} - E_m^{(0)}$). A small gap means large mixing.

And there it is: the denominator that causes trouble. When $E_m^{(0)} \to E_n^{(0)}$, the formula diverges. The machine has broken — but not because perturbation theory itself failed. The *basis choice within the degenerate subspace* was wrong. Chapter 2 fixes this.

### Second-order energy correction

Using the first-order state correction, the second-order energy is:

$$\boxed{E_n^{(2)} = \sum_{m \neq n}\frac{|\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}}$$

The numerator is a squared absolute value — always non-negative. The denominator changes sign: states above $n$ make it negative; states below make it positive. For the **ground state**, every other state sits above it, so every denominator is negative, every term in the sum is negative, and therefore:

> **The second-order correction to the ground-state energy is always negative, for any perturbation whatsoever.**

This is a theorem. Whatever you add to the ground state Hamiltonian — quartic potential, electric field, magnetic field — the second-order correction pushes the ground state energy down. It is a consequence of one sign, and it follows directly from the formula.

---

## Worked example: the quartic oscillator

### The problem

Take the harmonic oscillator and add a quartic term:

$$\hat{H} = \underbrace{\frac{\hat{p}^2}{2m} + \tfrac{1}{2}m\omega^2\hat{x}^2}_{\hat{H}_0} + \lambda\hat{x}^4$$

The unperturbed problem is the harmonic oscillator with $E_n^{(0)} = \hbar\omega(n + \tfrac{1}{2})$ and the familiar ladder-operator algebra. The perturbation is $\hat{H}' = \hat{x}^4$.

### First-order correction: the lesson

Express $\hat{x}$ in terms of raising and lowering operators:

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a}_+ + \hat{a}_-)$$

Then:

$$\hat{x}^4 = \left(\frac{\hbar}{2m\omega}\right)^2(\hat{a}_+ + \hat{a}_-)^4$$

Expanding $(\hat{a}_+ + \hat{a}_-)^4$ gives 16 terms. Most of them shift $|n\rangle$ to a different level and vanish when sandwiched as $\langle n|\cdot|n\rangle$. Only the terms that return to the same level survive. A systematic count (by normal-ordering or direct bookkeeping) gives:

$$\langle n|\hat{x}^4|n\rangle = \left(\frac{\hbar}{2m\omega}\right)^2(6n^2 + 6n + 3)$$

Therefore the first-order energy shift is:

$$E_n^{(1)} = \lambda\cdot\frac{3\hbar^2}{4m^2\omega^2}(2n^2 + 2n + 1)$$

In natural units ($\hbar = m = \omega = 1$): $E_n^{(1)} = \tfrac{3\lambda}{4}(2n^2 + 2n + 1)$.

For the ground state ($n=0$): $E_0^{(1)} = 3\lambda/4$.

**The lesson:** the correction grows as $n^2$. Perturbation theory works worst for highly excited states, whose wave functions extend further and sample the $\hat{x}^4$ term more strongly. For $n = 4$, the first-order correction is $(3\lambda/4)(32 + 8 + 1) = 30.75\lambda$ — an order of magnitude larger than the ground-state correction at the same $\lambda$.

### Second-order correction: the limit

The off-diagonal matrix elements $\langle m|\hat{x}^4|n\rangle$ are nonzero for $m = n, n\pm 2, n\pm 4$ (the expansion of $(\hat{a}_+ + \hat{a}_-)^4$ can change the level by at most 4). The energy denominators for these are $\pm 2\hbar\omega$ and $\pm 4\hbar\omega$ in natural units. Summing over the four nonzero off-diagonal contributions gives $E_n^{(2)}$, which for the ground state is negative (the denominator is always negative for $n=0$, as all states sit above it).

**The limit:** At what $\lambda$ does perturbation theory break? The diagnostic is the ratio $|E_n^{(2)}|/|E_{n+1}^{(0)} - E_n^{(0)}|$. When the second-order correction becomes comparable to the level spacing, the expansion is no longer small and PT is unreliable. For $n = 0$ in natural units, this occurs around $\lambda \sim 0.3$–$0.4$; for $n = 4$ it happens at $\lambda \sim 0.05$–$0.10$. The simulation exercise below lets you measure both.

---

## When perturbation theory breaks: the Dyson argument

So far the story sounds clean: compute corrections order by order, get increasingly accurate answers. But there is something hiding in the formalism.

Consider the quartic oscillator at negative $\lambda$. The perturbation $\lambda\hat{x}^4$ is now negative, making the potential $V(x) = \tfrac{1}{2}m\omega^2 x^2 + \lambda x^4$ go to $-\infty$ as $|x|\to\infty$. For any $\lambda < 0$, no matter how small, there is no bound ground state — the electron can tunnel to $x\to\infty$ and gain infinite kinetic energy. The system is unstable.

This means the energy $E_0(\lambda)$, as a function of the complex variable $\lambda$, has a singularity on the negative real axis. Any Taylor series for $E_0(\lambda)$ about $\lambda = 0$ has a radius of convergence that cannot reach that singularity. Therefore the radius of convergence is zero. The series diverges for every nonzero $\lambda$.

Freeman Dyson made this argument in 1952 for quantum electrodynamics: flip the sign of the fine-structure constant $\alpha$, electrons repel each other, the vacuum is unstable, the QED energy is non-analytic at $\alpha = 0$, and the QED perturbation series has zero radius of convergence. Bender and Wu confirmed it numerically for the quartic oscillator in 1969: the perturbation series coefficients grow as $k!$, making the series diverge for every nonzero $\lambda$ [verify].

**And yet the series is useful.** Truncate at the optimal order — the term at which the coefficients bottom out before starting to grow — and the partial sum is exponentially close to the true energy. Adding more terms past that point makes things worse.

Two misconceptions:

- *"If the terms keep getting smaller, the series converges."* The terms can decrease for many orders before turning around and growing. Optimal truncation, not convergence, is the criterion.
- *"First order is always sufficient for small $\lambda$."* Only when there is no near-degeneracy. If two unperturbed states are nearly degenerate, the denominator in the second-order correction can be tiny, making the second-order term large even when $\lambda$ is small. Always check $|\langle m|\hat{H}'|n\rangle|/|E_n^{(0)} - E_m^{(0)}|$ before trusting first-order PT.

The simulation exercise below lets you watch this departure directly: as $\lambda$ increases past the optimal truncation point, adding more orders moves the partial sum further from the exact energy.

---

## Common misconceptions

**1. "The first-order correction is always an approximation."**
Not always. If $\hat{H}'$ is already diagonal in the unperturbed basis — that is, if $\langle m|\hat{H}'|n\rangle = 0$ for all $m \neq n$ — then the second-order correction is exactly zero and the first-order result is exact. A constant potential added to an infinite square well shifts every energy by exactly $V_0$, with no higher-order correction.

**2. "The state correction and the energy correction are both first-order objects."**
Careful with this. The *first-order energy correction* requires only the zeroth-order states. The *first-order state correction* is needed to compute the *second-order energy correction*. These are staggered: the $k$-th order state feeds the $(k+1)$-th order energy. Students who conflate these often get confused when the first-order state formula involves a sum while the first-order energy formula does not.

**3. "Near-degenerate states are no problem as long as $\lambda$ is small enough."**
This is the most dangerous misconception. If $E_n^{(0)} - E_m^{(0)}$ is very small, the second-order correction $\sim |\langle m|\hat{H}'|n\rangle|^2/(E_n^{(0)} - E_m^{(0)})$ can be enormous even for tiny $\lambda$. The small-denominator problem is a feature of the unperturbed spectrum, not of $\lambda$. When you see near-degenerate levels, reach for degenerate perturbation theory (Chapter 2) immediately.

**4. "The perturbation series eventually converges if you compute enough terms."**
The opposite is true for almost all physically interesting perturbations. Past the optimal truncation order, adding terms makes the answer worse. The series is asymptotic, not convergent.

---

## Exercises

### Warm-up

**1.1** Take the harmonic oscillator with perturbation $\hat{H}' = \lambda\hat{x}^3$.

(a) By a parity argument, explain why $E_n^{(1)} = 0$ for every $n$.

(b) Compute $E_0^{(2)}$ for the cubic perturbation. Use $\hat{x} = \sqrt{\hbar/2m\omega}(\hat{a}_+ + \hat{a}_-)$ and ladder algebra to find which states $|m\rangle$ contribute to $\langle m|\hat{x}^3|0\rangle$ and with what value. Show the result is negative.

*(Tests: parity argument for vanishing first-order corrections; second-order calculation from ladder-operator matrix elements; verification that the ground state goes down.)*

---

**1.2** For the infinite square well of width $L$ with $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$, add the perturbation $\hat{H}' = V_0$ over the entire well.

(a) Compute $E_n^{(1)}$ for all $n$. The answer should be $V_0$. Explain in one sentence why this is exact — why adding $V_0$ to both $\hat{H}_0$ and $\hat{H}'$ yields no higher-order corrections.

(b) Now perturb with $\hat{H}' = V_0$ over only the left half of the well ($0 < x < L/2$). Compute $E_1^{(1)}$ and $E_2^{(1)}$. Are they equal?

*(Tests: first-order expectation-value calculation; recognizing when the perturbation series terminates.)*

---

**1.3** Prove from the formula $E_n^{(2)} = \sum_{m\neq n}|\langle m|\hat{H}'|n\rangle|^2/(E_n^{(0)}-E_m^{(0)})$ that the ground-state second-order correction is always negative, for any Hamiltonian $\hat{H}_0$ with a non-degenerate ground state, and for any perturbation $\hat{H}'$. Identify exactly which step in your proof fails for excited states.

*(Tests: general proof of the theorem stated in the chapter; understanding why the result does not extend to excited states.)*

---

### Apply

**1.4** Anharmonic oscillator in natural units ($\hbar = m = \omega = 1$). The Hamiltonian is $\hat{H} = \hat{H}_\text{HO} + \lambda\hat{x}^4$.

(a) Use $E_n^{(1)} = \tfrac{3\lambda}{4}(2n^2+2n+1)$ to find the first-order correction for $n = 0, 1, 2$.

(b) At what $n$ does the first-order correction $E_n^{(1)}$ become comparable to the unperturbed level spacing $\hbar\omega = 1$, for $\lambda = 0.1$? This is roughly where PT begins to break down for that level.

(c) Explain without calculation why $E_n^{(2)}$ is negative for the ground state, positive for some excited states.

*(Tests: plugging into the first-order formula; identifying the breakdown regime; sign analysis.)*

---

**1.5** The second-order polarizability. The hydrogen atom in a uniform electric field $\mathcal{E}$ along $\hat{z}$ has perturbation $\hat{H}' = e\mathcal{E}\hat{z}$. The first-order energy shift vanishes by parity ($\langle 1s|\hat{z}|1s\rangle = 0$). The second-order shift is $E_1^{(2)} = -\tfrac{1}{2}\alpha_\text{pol}\mathcal{E}^2$ where $\alpha_\text{pol}$ is the electric polarizability.

(a) Explain from the second-order formula why $E_1^{(2)}$ is guaranteed to be negative.

(b) The dominant contribution comes from the $|2p\rangle$ intermediate state. Estimate $E_1^{(2)}$ by keeping only that term, using the known matrix element $|\langle 2p|\hat{z}|1s\rangle|^2 = 2^{15}a_0^2/3^{10}$ and $E_1^{(0)} - E_2^{(0)} = -3E_R/4$ where $E_R = 13.6\,\text{eV}$.

(c) The exact polarizability is $\alpha_\text{pol} = \tfrac{9}{2}a_0^3$. How does your estimate compare? What fraction of the total does the $|2p\rangle$ state contribute?

*(Tests: dominant-intermediate-state approximation; understanding the quadratic Stark effect; comparing an estimate to the exact result.)*

---

**1.6** Validity diagnostic. For the quartic oscillator in natural units with $\lambda = 0.1$, estimate the ratio $|E_n^{(1)}|/\hbar\omega$ for $n = 0, 1, 2, 3, 4$. For which values of $n$ is first-order PT clearly reliable ($\text{ratio} \ll 1$)? For which does it become questionable? Then separately check the ratio $|\langle n+2|\hat{x}^4|n\rangle|/|E_n^{(0)} - E_{n+2}^{(0)}|$ for $n = 0, 4$ (you may look up or compute the off-diagonal matrix element). Compare your two diagnostics.

*(Tests: applying both the first-order and second-order validity conditions; seeing that PT breaks earlier for excited states.)*

---

### Produce

**1.7** Construct a perturbation $\hat{H}'$ for a two-level system with unperturbed energies $E_1^{(0)} < E_2^{(0)}$ such that:

(a) the first-order corrections to both levels are zero,
(b) the second-order correction to level 1 is negative,
(c) the second-order correction to level 2 is positive.

Write down the explicit $2\times 2$ matrix for $\hat{H}'$ and verify your results from the formulas. Explain geometrically why a perturbation that mixes two levels must push them apart at second order.

*(Tests: constructing an example from scratch; connecting the formula to a general principle — level repulsion.)*

---

**1.8** Dyson argument in miniature. Consider the double-well potential $V(x) = -\tfrac{1}{2}\mu^2 x^2 + \tfrac{1}{4}\lambda x^4$ (the Mexican hat for $\lambda > 0$).

(a) Show that for $\lambda < 0$ the potential is unbounded below.

(b) Argue that $E_0(\lambda)$, as a function of complex $\lambda$, cannot be analytic at $\lambda = 0$.

(c) What does this imply about the radius of convergence of the perturbation series in $\lambda$?

(d) Make the same argument for the fine-structure constant $\alpha$ in quantum electrodynamics: what is the physical instability that would appear if $\alpha < 0$?

*(Tests: understanding the Dyson analyticity argument from first principles; connecting the sign of the coupling constant to the stability of the spectrum.)*

---

## Still puzzling

Why does truncating at the optimal order give an answer exponentially close to the truth? The series diverges; the partial sum at optimal truncation is accurate to $e^{-\text{const}/\lambda}$. That exponential accuracy is not obvious from the algebraic structure of the series. Borel summation, transseries, and resurgent analysis — developed by Écalle, Costin, and Mariño — partially answer this: they reconstruct the exact answer from the divergent series by analytically continuing the Borel transform. The reconstruction works in all well-studied examples, but a fully general proof of why optimal truncation is exponentially accurate remains an area of active mathematical research. The empirical fact is not in doubt; the deepest theoretical understanding is still being written.

---

## The +1 — Simulation Exercise

You are going to build a D3 simulation that shows the quartic oscillator energy levels as functions of $\lambda$, comparing first-order PT, second-order PT, and exact numerical diagonalization. The deliverable is `02-anharmonic-oscillator.html` in your working directory.

### Step 1 — Describe the simulation to Claude Code

Copy the following prompt into a Claude Code session in your working directory. Read any CLAUDE.md and PROJECT.md files there first.

```
Build 02-anharmonic-oscillator.html: a single self-contained HTML file using
D3 v7 from a CDN. No other dependencies except d3-simple-slider from
https://cdn.jsdelivr.net/npm/d3-simple-slider.

WHAT TO BUILD
Single SVG canvas, 1100 x 600. Left half (550 wide): energy level diagram.
Horizontal lines at the current E_n(lambda) for n = 0..4, using exact
diagonalization. Pin the y-axis from 0 to 9 (natural units). Label each
level with n on the left edge.

Right half (550 wide): plot of E_n(lambda) vs. lambda for the currently
highlighted n. Three overlaid curves:
  - First-order PT: E_n^0 + lambda * E_n^(1)    [dashed teal]
  - Second-order PT: includes E_n^(2) as well    [dashed orange]
  - Exact diagonalization                         [solid black]
X-axis: lambda from 0 to 0.5. Y-axis: adjust to keep all three curves
in view for the active n.

CONTROLS
Lambda slider, range 0 to 0.5, default 0.1.
n-selector buttons (0, 1, 2, 3, 4) to highlight a level.
Warning text "PT NO LONGER RELIABLE" in red below the active level
  when |E_n^(2)| > (1/4) * |E_{n+1}^(0) - E_n^(0)|.

PHYSICS (natural units: hbar = m = omega = 1)
Unperturbed energy: E_n^(0) = n + 0.5
First-order correction: E_n^(1) = (3/4) * (2*n^2 + 2*n + 1)
Second-order correction: sum over m in {n-4, n-2, n+2, n+4} of
  |<m|x^4|n>|^2 / (E_n^(0) - E_m^(0)).
  The off-diagonal matrix elements of x^4 in the HO basis come from
  expanding (a+ + a-)^4 in natural units, where x = (a+ + a-)/sqrt(2).
  Collect the surviving terms for each m.

Exact diagonalization: build H as a 30x30 matrix in the HO basis.
The diagonal is E_n^(0). The off-diagonal entries of lambda*x^4 come
from the same expansion. Matrix is pentadiagonal (bandwidth 4).
Diagonalize using Jacobi iteration (pure JavaScript, no math.js).
For lambda > 0.2 increase basis to 50x50.

Sanity checks to console:
  - At lambda = 0, exact eigenvalues should equal n + 0.5 within 1e-6.
  - At lambda = 0.1, n=0: E_0^exact ~ 0.5 + 3*0.1/4 = 0.575 at first
    order; exact should be slightly less (second order is negative).
  - The "always negative" theorem: E_0^(2) must be negative.

Comments at every non-trivial physics step.
```

### Exploration tasks

After the simulation runs, answer the following:

1. **Ground state breakdown.** Slide $\lambda$ from $0$ to $0.5$ with $n=0$ selected. At what $\lambda$ does first-order PT depart from the exact curve by more than 10%? At what $\lambda$ does second-order PT depart by more than 10%? Record the $\lambda$ at which the "PT NO LONGER RELIABLE" warning fires.

2. **Excited state breakdown.** Repeat for $n=4$. At what $\lambda$ does first-order PT fail the 10% test? What is the ratio of the breakdown $\lambda$ for $n=4$ versus $n=0$? Does the simulation confirm that PT works worst for excited states?

3. **The always-negative theorem.** Set $\lambda = 0.1$ and select $n = 0$. Read the second-order PT curve value at this $\lambda$ and compare to the exact energy. Is the second-order correction negative, as the theorem requires? Now select $n = 2$ and check the sign of $E_2^{(2)}$ (the gap between first-order and second-order PT curves at $\lambda = 0.1$). Is it still negative?

4. **Optimal truncation (extension).** Modify the simulation to add a third tab showing the partial-sum error $|E_0^{(N)} - E_0^\text{exact}|$ versus truncation order $N$, for $\lambda = 0.1$, $n = 0$. Use the recursive Rayleigh–Schrödinger formula to compute higher-order coefficients, or fit them empirically. Find the optimal truncation order $N^*$ where the error is minimized. Mark it with a vertical line. Label the plot "Bender–Wu 1969 asymptotic behavior."

---

## References

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §7.1–7.2. [verify]

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Ch. 11. [verify]

Bender, C. M., & Wu, T. T. (1969). Anharmonic oscillator. *Physical Review*, *184*(5), 1231–1260. https://doi.org/10.1103/PhysRev.184.1231 [verify]

Dyson, F. J. (1952). Divergence of perturbation theory in quantum electrodynamics. *Physical Review*, *85*(4), 631–632. https://doi.org/10.1103/PhysRev.85.631 [verify]
