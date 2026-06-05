# Worked Exercises: The Variational Principle

*Chapter 3 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The variational theorem: for any normalized trial state, $\langle\psi|\hat{H}|\psi\rangle \geq E_0$ — a guaranteed **upper** bound on the ground-state energy, saturated only when $|\psi\rangle$ is the exact ground state.
- The optimization procedure: form $E_V(\alpha) = \langle\psi(\alpha)|\hat{H}|\psi(\alpha)\rangle / \langle\psi(\alpha)|\psi(\alpha)\rangle$ (divide by the norm for un-normalized trials), then set $\partial E_V/\partial\alpha = 0$.
- The helium worked calculation: screened trial charge $\tilde{Z}$, with $E_V(\tilde{Z}) = \tilde{Z}^2 - 2Z\tilde{Z} + \tfrac{5}{8}\tilde{Z}$ in Hartree, minimized at $\tilde{Z}^* = Z - \tfrac{5}{16}$.

## Part A — Full Worked Example

**What this demonstrates:** How to minimize the variational energy of a single-parameter trial function and confirm the result is an upper bound, using the helium ground state.

**The problem:** Helium has $Z=2$ and two electrons whose mutual repulsion makes the Schrödinger equation unseparable. Using the screened trial function $\psi = (\tilde{Z}^3/\pi a_0^3)\,e^{-\tilde{Z}(r_1+r_2)/a_0}$ with one variational parameter $\tilde{Z}$, find the optimal $\tilde{Z}^*$, the variational energy $E_V^*$ in eV, and confirm it bounds the experimental value $-78.98$ eV from above.

**The solution:**

**Step 1 — Assemble the variational energy.** Rewriting $\hat{H}$ by adding and subtracting $\tilde{Z}e^2/4\pi\epsilon_0 r$ for each electron, the trial state is the exact eigenstate of $\hat{H}_1(\tilde Z)+\hat{H}_2(\tilde Z)$. Using $\langle 1/r\rangle = \tilde{Z}/a_0$ and the repulsion integral $\langle V_{ee}\rangle = 5\tilde{Z}/8a_0$, in atomic units (Hartree):
$$E_V(\tilde{Z}) = \tilde{Z}^2 - 2Z\tilde{Z} + \frac{5}{8}\tilde{Z}.$$
*Why:* The kinetic-plus-screened-nuclear part gives $\tilde Z^2 - 2Z\tilde Z$; the electron-electron repulsion adds the positive $\tfrac58\tilde Z$ term — the only piece that makes helium hard.
*Check:* Each term is dimensionless (Hartree units); the repulsion term is positive, as a repulsion must be.

**Step 2 — Minimize the variational energy.** Set $\partial E_V/\partial\tilde{Z} = 0$:
$$2\tilde{Z} - 2Z + \frac{5}{8} = 0 \quad\Longrightarrow\quad \tilde{Z}^* = Z - \frac{5}{16}.$$
*Why:* The best upper bound within this one-parameter family sits at the stationary point of $E_V(\tilde Z)$, a parabola opening upward.
*Check:* The second derivative $\partial^2 E_V/\partial\tilde Z^2 = 2 > 0$, confirming a minimum (not a maximum).

**Step 3 — Evaluate the optimal charge and energy.** For $Z=2$:
$$\tilde{Z}^* = 2 - \frac{5}{16} = \frac{27}{16} \approx 1.6875, \qquad E_V^* = -\left(\frac{27}{16}\right)^2\ \text{Hartree} \approx -77.5\ \text{eV}.$$
*Why:* Substituting $\tilde Z^*$ back into $E_V$ gives $E_V^* = -(\tilde Z^*)^2$ Hartree; converting at $1$ Hartree $= 27.211$ eV gives $-77.5$ eV.
*Check:* $\tilde Z^* < Z$, as physical screening requires — each electron sees less than the full $+2$ nuclear charge.

**Step 4 — Confirm the upper bound.** Compare to experiment:
$$E_V^* = -77.5\ \text{eV} \ > \ -78.98\ \text{eV} = E_\text{exp}, \qquad \text{error} \approx \frac{1.5\text{ eV}}{78.98\text{ eV}} \approx 1.9\%.$$
*Why:* The variational theorem guarantees the bound lies *above* the true ground state; a result below $-78.98$ eV would be definitionally impossible.
*Check:* The bound is on the correct side and the error is the expected $\sim 2\%$; first-order PT at fixed $Z=2$ gives $-74.8$ eV (5%), so variational wins.

**Final answer:** $\tilde{Z}^* = 27/16 \approx 1.6875$, $E_V^* \approx -77.5$ eV, sitting $1.5$ eV above experiment ($1.9\%$ error) — a valid upper bound.

**What made this work:** The central concept is that the variational energy is a guaranteed *upper* bound, and minimizing it over a physically motivated parameter ($\tilde Z$, the screened charge) tightens that bound. The naive approach — first-order perturbation theory with the bare $Z=2$ — fails to optimize the parameter that matters most, the effective charge, and lands $5\%$ off. The variational method outperforms it precisely because it lets the trial function adjust to the screening physics rather than trusting the unmodified Hamiltonian. The bound's one-sidedness is also the built-in sanity check: any energy below $-78.98$ eV signals a bug, never a discovery.

**Self-explanation prompt:** Why is the screening interpretation — each electron shielding $5/16$ of a proton charge from the other — a consequence of the *minimization*, not an assumption put in by hand?

## Part B — Matched Practice Problem

**What this demonstrates:** The same minimize-the-upper-bound move on a single-parameter Gaussian trial for the hydrogen atom, where the trial family does *not* contain the exact answer.

**The problem:** For the hydrogen atom $\hat{H} = \hat{p}^2/2m - (e^2/4\pi\epsilon_0)/r$, take the Gaussian trial function $\phi(r;\alpha) = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$. Using $\langle\hat{T}\rangle = 3\hbar^2\alpha/2m$ and $\langle V\rangle = -(e^2/4\pi\epsilon_0)\sqrt{8\alpha/\pi}$, find $\alpha^*$, the variational energy $E_V^*$, and the fraction of the exact binding energy ($-13.6$ eV) it captures.

**Step 1 — Subgoal: Assemble the variational energy.** Write $E_V(\alpha) = \langle\hat T\rangle + \langle V\rangle$ as a function of $\alpha$.

**Step 2 — Subgoal: Minimize the variational energy.** Set $\partial E_V/\partial\alpha = 0$ and solve for $\alpha^*$ (note $\langle V\rangle \propto \sqrt\alpha$).

**Step 3 — Subgoal: Evaluate the optimal energy.** Substitute $\alpha^*$ back to get $E_V^*$ in eV.

**Step 4 — Subgoal: Confirm the upper bound.** Compare $E_V^*$ to $-13.6$ eV and compute the captured fraction.

**Stuck?** $E_V(\alpha)$ has the form $A\alpha - B\sqrt\alpha$; differentiating gives $A - \tfrac{B}{2\sqrt\alpha} = 0$, so $\sqrt{\alpha^*} = B/2A$. The exact ground state is an exponential $e^{-r/a_0}$, not a Gaussian, so this trial family cannot reach $-13.6$ eV.

*Instructor note: full solution intentionally omitted. This problem is for the student to complete after Part A.*

## Part C — Completion Problem

**The problem:** For the infinite square well of width $L$ (exact ground state $E_0 = \pi^2\hbar^2/2mL^2$), use the trial function $\psi_\text{trial}(x) = Ax(L-x)$ on $0 < x < L$. Compute $E_V = \langle\hat T\rangle$ (no potential inside the well) and verify the bound.

**Step 1 — Normalize the trial function (provided).** $\int_0^L A^2 x^2(L-x)^2\,dx = A^2 L^5/30 = 1$, so $A = \sqrt{30/L^5}$.

**Step 2 — Set up the kinetic energy (provided).** $\langle\hat T\rangle = -\dfrac{\hbar^2}{2m}\int_0^L \psi_\text{trial}\,\psi_\text{trial}''\,dx$, with $\psi_\text{trial}'' = -2A$.

**Step 3 — Evaluate the kinetic integral.**
*Your work here:* Compute $\langle\hat T\rangle = -\dfrac{\hbar^2}{2m}\int_0^L Ax(L-x)\cdot(-2A)\,dx$ using $\int_0^L x(L-x)\,dx = L^3/6$.

*Why (your explanation):*

**Step 4 — Form the ratio to the exact energy.**
*Your work here:* Compute $E_V/E_0$ and confirm $E_V \geq E_0$.

*Why (your explanation):*

**Step 5 — Interpret (provided).** The result is $E_V = 5\hbar^2/mL^2 = 10/\pi^2 \cdot E_0 \approx 1.013\,E_0$ — only $1.3\%$ above the exact ground state, because $x(L-x)$ already has the right boundary behavior (vanishing at both walls, single hump, no nodes).

**Final answer:** $E_V = \dfrac{5\hbar^2}{mL^2}$, with $E_V/E_0 = 10/\pi^2 \approx 1.013$ — a valid upper bound.

**Self-explanation prompt:** The parabola $x(L-x)$ has no free parameter to optimize, yet it gives a bound within $1.3\%$. Explain why a *fixed* trial function with the right qualitative shape can do so well, and what a variational parameter would add.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student applies the variational method to the delta-function potential $\hat{H} = -(\hbar^2/2m)d^2/dx^2 - \alpha\delta(x)$ with the un-normalized trial function $\psi(x;b) = e^{-bx^2/2}$ and presents:

**Step 1 (correct).** "The trial function is not normalized as written, so I will need the norm $\langle\psi|\psi\rangle = \int e^{-bx^2}dx = \sqrt{\pi/b}$."

**Step 2 (correct).** "The numerators are $\langle\psi|\hat T|\psi\rangle = \tfrac{\hbar^2 b}{4m}\sqrt{\pi/b}$ and $\langle\psi|\hat V|\psi\rangle = -\alpha|\psi(0)|^2$-style term, giving $\langle\psi|\hat V|\psi\rangle = -\alpha$ (from $\psi(0)=1$)."

**Step 3 (⚠).** "The variational energy is then $E_V(b) = \langle\psi|\hat T|\psi\rangle + \langle\psi|\hat V|\psi\rangle = \tfrac{\hbar^2 b}{4m}\sqrt{\pi/b} - \alpha$. Minimizing over $b$: $\partial E_V/\partial b = 0$."

**Step 4 (correct-looking).** "Solving the minimization yields some $b^*$ and a finite $E_V^*$, which I report as the variational estimate of the ground-state energy."

**Your tasks:**
1. Identify the error in Step 3 and explain what went wrong.
2. Write the corrected Step 3.
3. Name the principle that was violated.
4. State a check that would catch this class of error.

**Why this error is common:** With an un-normalized trial function the variational energy is $E_V = \langle\psi|\hat H|\psi\rangle / \langle\psi|\psi\rangle$, and students who forget to divide the numerator by the norm $\langle\psi|\psi\rangle$ produce an $E_V$ that is not even an upper bound — the theorem's guarantee silently evaporates.

## Part E — Transfer Problem

**What this demonstrates:** The variational upper-bound machinery transferred to a system not in the chapter — a particle in a linear (gravitational) potential.

**The problem:** A particle of mass $m$ sits in the potential $V(x) = Fx$ for $x > 0$ with an infinite wall at $x = 0$ (the "quantum bouncing ball"). Use the trial function $\psi(x;\beta) = x\,e^{-\beta x}$ for $x>0$ (which vanishes at the wall and decays at infinity). Find the optimal $\beta$, the variational energy $E_V^*$, and confirm it is an upper bound on the exact ground state.

**Hint (use only if stuck after 10 minutes):** This trial is un-normalized — you must divide by $\langle\psi|\psi\rangle = \int_0^\infty x^2 e^{-2\beta x}dx$. Use $\int_0^\infty x^n e^{-2\beta x}dx = n!/(2\beta)^{n+1}$ for all three integrals (norm, kinetic, potential). $E_V(\beta)$ will have the form $A\beta^2 + B/\beta$; minimize over $\beta$.

**Reflection prompt:**
1. Why does this trial family give a valid upper bound, while a trial function that *grows* at infinity (e.g. a constant) would not?
2. The exact ground state involves an Airy function. Without computing it, argue from the variational theorem alone in which direction your $E_V^*$ must err.

## Part F — Interleaved Review

**F1.** For H$_2^+$ in the LCAO trial $|\psi_+\rangle = (|A\rangle + |B\rangle)/\sqrt{2 + 2S_{AB}}$, explain why the bonding orbital $|+\rangle$ binds the protons while the antibonding $|-\rangle$ does not, in terms of where the trial function places electron density relative to the internuclear midplane.
*Chapter this draws from: 3*

**F2.** Return to the quartic oscillator of the perturbation-theory chapter. For the 3D harmonic oscillator $\hat H = \hat p^2/2m + \tfrac12 m\omega^2 r^2$ perturbed by $+\lambda r^4$, the Gaussian trial gives the *exact* $3\hbar\omega/2$ at $\lambda = 0$. Explain why, and show that the optimal Gaussian width shifts for $\lambda > 0$, connecting the variational result to first-order perturbation theory.
*Chapter this draws from: Time-Independent Perturbation Theory (Chapter 1)*

**F3.** Discrimination: You must decide whether to reach for perturbation theory or the variational method. For (a) helium ground state, (b) a harmonic oscillator with a tiny $\lambda\hat x^4$, (c) the hydrogen molecular ion H$_2^+$ — state which method is the natural tool and why.
*Note to instructor: the discriminating feature is whether a small parameter exists. Helium ($\langle V_{ee}\rangle/|E_0|\sim 0.3$, no small parameter) and H$_2^+$ (no obvious expansion parameter) call for variational; the tiny-$\lambda$ oscillator has a genuine small parameter and is the natural perturbation-theory case. Students who apply perturbation theory to helium at fixed $Z=2$ land $5\%$ off because the repulsion is not small.*

**Closing reflection:** Across these problems, what is the one check you can always run on a variational energy — regardless of the system — that no perturbative estimate offers?

## Instructor Notes

**Common errors:**
1. Forgetting to divide by $\langle\psi|\psi\rangle$ for an un-normalized trial function, breaking the upper-bound guarantee.
2. Claiming the variational energy is a *lower* bound (it is an **upper** bound on the ground state).
3. Mislabeling units — confusing Rydberg, Hartree, and eV (1 Hartree $= 2$ Ry $= 27.211$ eV), which corrupts the percent-error comparison.

**Signs a student needs to return:**
- They report a variational energy *below* the experimental/exact value and treat it as success rather than a bug.
- They conflate a tight energy with a good wave function (the energy is second-order-accurate in the wave-function error; the state is not).

**Scaffolding adjustments:** A student stuck on Part A should first do Part C (the fixed-parabola square-well bound) to see the upper-bound check in a setting with no minimization, then return to the helium minimization. A student who finishes Part F quickly should redo the helium calculation with a *two*-parameter trial and confirm the bound tightens (toward $-77.8$ eV) while staying above experiment.

**Domain adaptation note:** For a quantum-chemistry cohort, recast Part A as the Hartree–Fock effective charge for a many-electron atom, where the same screening-by-minimization logic underlies the self-consistent field and every Rayleigh–Ritz basis-set calculation.
