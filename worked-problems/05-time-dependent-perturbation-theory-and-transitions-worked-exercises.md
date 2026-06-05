# Worked Exercises: Time-Dependent Perturbation Theory and Transitions
*Chapter 5 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The first-order transition amplitude $c_f^{(1)}(t) = \frac{1}{i\hbar}\int_0^t\langle f|\hat{H}'(t')|i\rangle\,e^{i\omega_{fi}t'}\,dt'$ and that the transition *probability* is $|c_f^{(1)}(t)|^2$, not the amplitude itself.
- The exact two-level Rabi formula $P_{g\to e}(t) = \frac{\Omega^2}{\Omega^2+\Delta^2}\sin^2\!\left(\frac{\sqrt{\Omega^2+\Delta^2}}{2}t\right)$, with detuning $\Delta = \omega - \omega_0$ and Rabi frequency $\Omega = |V_{fi}|/\hbar$.
- The two small parameters that bound the methods: the rotating-wave approximation needs $\Omega/\omega_0 \ll 1$, and first-order PT needs $\Omega t \ll 1$.

---

## Part A — Full Worked Example

**What this demonstrates:** That first-order perturbation theory and the exact Rabi formula agree only while $\Omega t \ll 1$, and that PT announces its own breakdown by predicting a probability greater than 1.

**The problem:** A two-level atom with transition energy $\hbar\omega_0 = 3.00$ eV is driven *on resonance* by a laser with coupling strength $\hbar\Omega = 0.020$ eV, starting in the ground state. Find the $\pi$-pulse time. Then find the time at which first-order PT predicts $P = 1$, and compute the *exact* probability at that moment. Comment on what the discrepancy diagnoses.

**The solution:**

**Step 1 — Convert the coupling to a Rabi frequency.** The Rabi frequency is $\Omega = |V_{fi}|/\hbar = (\hbar\Omega)/\hbar$ read off from the given energy.
$$\Omega = \frac{0.020\,\text{eV}\times 1.602\times10^{-19}\,\text{J/eV}}{1.055\times10^{-34}\,\text{J·s}} = 3.04\times10^{13}\,\text{rad/s}.$$
*Why:* The Rabi formula and the PT parabola are both expressed in $\Omega t$, so we need $\Omega$ in rad/s before any time can be computed.
*Check:* $\hbar\Omega = 0.020$ eV is far below $\hbar\omega_0 = 3.00$ eV, so $\Omega/\omega_0 \approx 6.7\times10^{-3} \ll 1$ and the rotating-wave approximation is safe.

**Step 2 — Locate the $\pi$-pulse with the exact on-resonance formula.** On resonance ($\Delta = 0$), the Rabi formula collapses to $P_{g\to e}(t) = \sin^2(\Omega t/2)$. This reaches 1 when $\Omega t/2 = \pi/2$, i.e. $t_\pi = \pi/\Omega$.
$$t_\pi = \frac{\pi}{3.04\times10^{13}} = 1.03\times10^{-13}\,\text{s} = 0.10\,\text{ps}.$$
*Why:* The $\pi$-pulse is the first moment of complete population inversion — the physically meaningful timescale of the drive.
*Check:* $\Omega t_\pi = \pi \approx 3.14$, which is *not* $\ll 1$ — a warning that PT cannot be trusted at this time.

**Step 3 — Find where first-order PT predicts $P = 1$.** First-order PT on resonance gives $P^{\text{PT}}(t) = (\Omega t/2)^2$. Setting this to 1: $\Omega t/2 = 1$, so $t_{\text{PT}} = 2/\Omega$.
$$t_{\text{PT}} = \frac{2}{3.04\times10^{13}} = 6.58\times10^{-14}\,\text{s} = 0.066\,\text{ps}.$$
*Why:* PT replaces the bounded $\sin^2$ with an unbounded parabola; the parabola crosses 1 *earlier* than the true $\pi$-pulse.
*Check:* $t_{\text{PT}} = (2/\pi)\,t_\pi \approx 0.64\,t_\pi$ — PT hits "complete transfer" before the real system does, which is suspicious since the real maximum is exactly 1.

**Step 4 — Evaluate the exact probability at $t_{\text{PT}}$.** At $\Omega t_{\text{PT}}/2 = 1$:
$$P^{\text{exact}}(t_{\text{PT}}) = \sin^2(1) = (0.8415)^2 = 0.708.$$
*Why:* This is the real population in $|e\rangle$ at the instant PT claims 100%.
*Check:* $0.708 < 1$, as any probability must be. PT predicted 100% while the atom had moved only 71% of its population.

**Step 5 — Diagnose the breakdown.** PT assumes $c_g(t) \approx 1$ throughout, drawing population from $|i\rangle$ as if it never depletes. The exact solution feeds depleted population back during the return half of the Rabi cycle; PT misses the return. The failure is governed by the product $\Omega t$ reaching 1, not by $\Omega$ being "large."
*Why:* This is the chapter's central lesson — time matters as much as coupling strength.
*Check:* For $\Omega t \ll 1$, expand $\sin^2 x \approx x^2$ and the two formulas coincide, confirming PT is the small-$\Omega t$ limit of the exact result.

**Final answer:** $t_\pi = 0.10$ ps; PT predicts $P=1$ at $t_{\text{PT}} = 0.066$ ps, where the exact probability is only $\sin^2(1) \approx 0.708$. The 29% gap is the signature of PT ignoring ground-state depletion.

**What made this work:** The whole calculation hinges on recognizing that two formulas describe the same physics in different validity windows. The Rabi formula is exact within the RWA and caps $P$ at 1; the PT parabola is its small-$\Omega t$ tangent and grows without bound. By computing both at the same instant we expose precisely where they part ways — and the fact that the exact value stays below 1 while PT exceeds it is not a numerical accident but a built-in diagnostic. Any time PT reports $P > 1$, it is announcing that $\Omega t$ has left the window $\Omega t \ll 1$.

**Self-explanation prompt:** In your own words, why does first-order PT cross $P = 1$ *before* the true $\pi$-pulse, rather than after?

---

## Part B — Matched Practice Problem

**The problem:** A nuclear spin in an NMR coil has transition energy $\hbar\omega_0 = 1.7\times10^{-7}$ eV (a 400 MHz proton resonance) and is driven on resonance with coupling $\hbar\Omega = 5.5\times10^{-9}$ eV, starting in the lower spin state. (i) Find the $\pi$-pulse time $t_\pi$. (ii) Find the time at which first-order PT predicts $P = 1$. (iii) Compute the exact spin-flip probability at that moment, and state what the discrepancy diagnoses.

Work it in the same five conceptual moves as Part A: convert the coupling to a Rabi frequency, locate the $\pi$-pulse with the exact formula, find where PT predicts $P=1$, evaluate the exact probability there, and diagnose the breakdown.

**Stuck?** The on-resonance exact probability is $\sin^2(\Omega t/2)$ and the PT prediction is $(\Omega t/2)^2$ — the same two curves as Part A, just with different numbers. The exact probability at $t_{\text{PT}}$ is *always* $\sin^2(1)$ regardless of the coupling, because $t_{\text{PT}}$ is defined by $\Omega t/2 = 1$.

*Instructor note: no solution is provided here. The numerical $t_\pi$ will land near 2.4 μs; the key teaching point is that $P^{\text{exact}}(t_{\text{PT}}) = \sin^2(1) \approx 0.708$ is independent of the system, exposing that the breakdown is a property of $\Omega t$ alone.*

---

## Part C — Completion Problem

**The problem:** A two-level system ($\hbar\omega_0 = 5.0$ eV, $\hbar\Omega = 0.05$ eV) is driven *off resonance* at detuning $\Delta = 2\Omega$. Find the maximum achievable transition probability and the time at which it is first reached.

**Step 1 — Form the generalized Rabi frequency.** The off-resonance dynamics are governed by $\Omega_{\text{gen}} = \sqrt{\Omega^2 + \Delta^2}$. With $\Delta = 2\Omega$:
$$\Omega_{\text{gen}} = \sqrt{\Omega^2 + 4\Omega^2} = \sqrt{5}\,\Omega.$$
*Why:* Off resonance the oscillation runs at $\Omega_{\text{gen}}$, faster than $\Omega$, and the amplitude is capped below 1.

**Step 2 — Write the off-resonance Rabi formula.** The exact probability is
$$P_{g\to e}(t) = \frac{\Omega^2}{\Omega_{\text{gen}}^2}\sin^2\!\left(\frac{\Omega_{\text{gen}}\,t}{2}\right) = \frac{\Omega^2}{5\Omega^2}\sin^2\!\left(\frac{\sqrt5\,\Omega t}{2}\right) = \frac{1}{5}\sin^2\!\left(\frac{\sqrt5\,\Omega t}{2}\right).$$
*Why:* The prefactor $\Omega^2/\Omega_{\text{gen}}^2$ is the ceiling; the $\sin^2$ oscillates between 0 and that ceiling.

**Step 3 — Identify the maximum probability.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Find the time at which the maximum is first reached.**
*Your work here:*

*Why (your explanation):*

**Step 5 — Compare to the on-resonance case.** On resonance the ceiling is 1 (full inversion); here it is $1/5$. Detuning by $\Delta = 2\Omega$ suppresses the maximum probability by a factor of 5 and makes the oscillation $\sqrt5 \approx 2.24$ times faster.
*Why:* Resonance is required for complete inversion; any detuning both caps and speeds the oscillation.

**Final answer:** $P_{\max} = \Omega^2/(\Omega^2+\Delta^2) = 1/5 = 0.20$, first reached when $\sqrt5\,\Omega t/2 = \pi/2$, i.e. $t = \pi/(\sqrt5\,\Omega)$.

**Self-explanation prompt:** Explain why increasing the detuning makes the oscillation faster but shallower — what is the trade-off between speed and reach?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A two-level atom ($\hbar\omega_0 = 2.0$ eV, $\hbar\Omega = 0.010$ eV) is driven on resonance. A student computes the probability of finding it in the excited state at the $\pi$-pulse time $t_\pi = \pi/\Omega$ using first-order perturbation theory.

**Student's work:**

Step 1 — On resonance, the first-order amplitude is $c_e^{(1)}(t) = -\frac{i\Omega}{2}\int_0^t dt' = -\frac{i\Omega t}{2}$.

Step 2 — At the $\pi$-pulse, $t_\pi = \pi/\Omega$, so $c_e^{(1)}(t_\pi) = -\frac{i\Omega}{2}\cdot\frac{\pi}{\Omega} = -\frac{i\pi}{2}$.

⚠ Step 3 — The transition probability is the amplitude itself: $P_{g\to e}(t_\pi) = c_e^{(1)}(t_\pi) = -\frac{i\pi}{2} \approx -1.57i$, so the atom is fully in the excited state.

Step 4 — Therefore first-order PT correctly predicts complete inversion at the $\pi$-pulse.

**Your tasks:**
1. Identify the conceptual error in Step 3 and state the correct relationship between the amplitude and the probability.
2. Compute the correct PT probability $|c_e^{(1)}(t_\pi)|^2$ and show it is unphysical.
3. Explain what that unphysical value is diagnosing about the validity of first-order PT at $t = t_\pi$.
4. State the regime of $\Omega t$ in which the student's Step 1 amplitude *is* trustworthy, and give the exact formula that must be used at the $\pi$-pulse instead.

**Why this error is common:** Students conflate the complex transition *amplitude* $c_f^{(1)}$ with the *probability* $|c_f^{(1)}|^2$, and an imaginary "probability" of $-1.57i$ slips by unnoticed because the magnitude looks plausible.

---

## Part E — Transfer Problem

**The problem:** A harmonic oscillator (mass $m$, frequency $\omega$) sits in its ground state $|0\rangle$ when it receives a sudden kick described by $\hat{H}'(t) = F\,\hat{x}\,\delta(t)$, with $F$ a small constant. Using $\hat{x} = \sqrt{\hbar/2m\omega}\,(\hat{a}_+ + \hat{a}_-)$: (i) compute the first-order transition amplitude $c_1^{(1)}(\infty)$ to the first excited state $|1\rangle$; (ii) show the transition probability is $P_{0\to1} = F^2/(2m\omega\hbar)$; (iii) state the condition on $F$ for first-order PT to remain valid, and say whether it is a condition on $F$ alone or on $F$ combined with the kick.

**Hint (use only if stuck after 10 minutes):** For a delta-function perturbation, the time integral $\int_0^\infty \langle 1|F\hat x|0\rangle\,\delta(t')\,e^{i\omega_{10}t'}\,dt'$ evaluates the integrand at $t'=0$, where $e^{i\omega_{10}\cdot 0} = 1$. The ladder operators give $\langle 1|\hat x|0\rangle = \sqrt{\hbar/2m\omega}$, since $\hat a_+|0\rangle = |1\rangle$ and $\hat a_-|0\rangle = 0$.

**Reflection prompt:** (1) The kick has a flat Fourier spectrum (a delta in time transforms to a constant in frequency) — how does that explain why a sudden kick can drive a transition that a slow, quasi-static perturbation cannot? (2) Is the validity condition here a statement about the strength $F$ alone, or about $F$ measured against the oscillator's natural scale $\sqrt{2m\omega\hbar}$ — and how does that mirror the "$\Omega t \ll 1$, not $\Omega$ alone" lesson of the Rabi problem?

---

## Part F — Interleaved Review

**F1 — This chapter.** A two-level system has $\hbar\Omega = 0.5\,\hbar\omega_0$ (strong coupling), driven on resonance. (a) Write the exact on-resonance Rabi probability and the first-order PT probability. (b) Evaluate both at $\Omega t = \pi/2$ and $\Omega t = \pi$. (c) At what $\Omega t$ does PT first exceed 1? (d) At $\Omega/\omega_0 = 0.5$ the RWA is marginal; estimate the Bloch–Siegert shift (order $\Omega^2/\omega_0$) as a fraction of $\omega_0$.
*Chapter this draws from: 5.*

**F2 — Previous chapter.** *Chapter this draws from: Chapter 4 — Variational Methods and the WKB Approximation.* The Rabi problem fixes a coupling strength and asks how the population evolves in time; a variational calculation fixes a trial wavefunction and asks for the best energy bound. For a particle in a potential, you minimize $\langle\hat H\rangle$ over a trial parameter to bound the ground-state energy from above. Explain, in two or three sentences, how the *direction* of the inequality in the variational method (an upper bound on energy) is analogous to the *direction* of the failure in first-order PT (an over-estimate of the probability) — both methods err in a known, fixed direction, which is what makes them trustworthy diagnostics rather than uncontrolled guesses.

**F3 — Discrimination.** You are handed a two-level system driven by an oscillating field and asked for the excited-state population at a specified time. Decide whether to use (i) first-order perturbation theory, (ii) the exact Rabi formula on resonance, or (iii) the exact Rabi formula off resonance with $\Omega_{\text{gen}}$. State the single check that selects between them.
*Note to instructor: the discriminating check is the product $\Omega t$ against 1 (PT only if $\Omega t \ll 1$) combined with the detuning $\Delta$ (use $\Omega_{\text{gen}}$ whenever $\Delta \neq 0$); students who reach for PT at a $\pi$-pulse have missed that $\Omega t = \pi$ is not small.*

**Closing reflection:** Across F1–F3, what single quantity — not a coupling strength, not a time, but a *product* — decides whether the simplest available method is trustworthy?

---

## Instructor Notes

**Common errors:**
- Treating the first-order amplitude $c_f^{(1)}$ as the probability instead of squaring it (Part D's core misconception); an imaginary "probability" should be an immediate red flag.
- Applying first-order PT through a full $\pi$-pulse and reporting $P = (\pi/2)^2 \approx 2.47$ as physical, instead of recognizing $P > 1$ as a breakdown signal.
- Forgetting the $\Omega^2/\Omega_{\text{gen}}^2$ ceiling off resonance and predicting full inversion at any detuning.

**Signs a student needs to return:**
- They cannot state the condition $\Omega t \ll 1$ from memory, or confuse it with $\Omega \ll \omega_0$ (the separate RWA condition).
- They report a probability above 1 (or a complex one) without flagging it as a method failure.

**Scaffolding adjustments:** If a student struggles with Part A, have them first tabulate $\sin^2(\Omega t/2)$ and $(\Omega t/2)^2$ at $\Omega t = 0.1, 0.5, 1, \pi$ to *see* the curves diverge before doing any unit conversion. If a student finishes Part F quickly, have them derive the leading correction $\sin^2 x \approx x^2 - x^4/3$ and estimate the time $t_{10\%}$ at which PT and exact first differ by 10%.

**Domain adaptation note:** Swap the two-level atom for a superconducting transmon (drive Rabi frequency in place of $\gamma_p B_1/2$), an NMR proton, or a trapped ion; the two-condition argument ($\Omega/\omega_0$ for the RWA, $\Omega t$ for PT) is identical across all of them.
