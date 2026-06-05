# Worked Exercises: Scattering I: Partial Waves
*Chapter 7 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The partial-wave scattering amplitude $f(\theta) = \frac{1}{k}\sum_\ell(2\ell+1)e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta)$ and the total cross-section $\sigma_\text{tot} = \frac{4\pi}{k^2}\sum_\ell(2\ell+1)\sin^2\delta_\ell$, with the unitarity bound $4\pi(2\ell+1)/k^2$ on each channel.
- The optical theorem $\sigma_\text{tot} = \frac{4\pi}{k}\operatorname{Im}f(0)$, a consequence of unitarity and a self-consistency check on any partial-wave sum.
- The low-energy regime $ka \ll 1$ where only $\ell = 0$ survives, the scattering length $\delta_0 \to -a_s k$, and $\sigma_\text{tot} \to 4\pi a_s^2$ — four times the classical $\pi a_s^2$.

---

## Part A — Full Worked Example

**What this demonstrates:** That the quantum hard-sphere cross-section is $4\pi a^2$ at low energy and $2\pi a^2$ at high energy — neither equal to the classical geometric $\pi a^2$ — and that both factors come from wave behavior the partial-wave framework makes explicit.

**The problem:** For a hard sphere of radius $a$ ($V = \infty$ for $r < a$, $V = 0$ for $r \geq a$), find the exact $\ell = 0$ phase shift, then the total cross-section in the low-energy limit $ka \ll 1$ and the high-energy limit $ka \gg 1$. Explain the factor-of-four and factor-of-two relative to the classical $\pi a^2$.

**The solution:**

**Step 1 — Solve the s-wave radial equation outside the sphere.** Outside, the particle is free: $u_0'' + k^2 u_0 = 0$, general solution $u_0(r) = A\sin(kr + \delta_0)$.
$$u_0(r) = A\sin(kr + \delta_0), \qquad r \geq a.$$
*Why:* The radial function $u_0 = rR_0$ obeys a free 1D equation outside the potential; the phase shift $\delta_0$ is the only free parameter left after the boundary condition.
*Check:* As $r\to\infty$, $u_0 \to A\sin(kr + \delta_0)$ matches the required asymptotic form $\sin(kr - \ell\pi/2 + \delta_0)$ with $\ell = 0$.

**Step 2 — Impose the hard-sphere boundary condition.** The wavefunction must vanish at the surface: $u_0(a) = 0$, so $\sin(ka + \delta_0) = 0$, giving $ka + \delta_0 = 0$:
$$\delta_0 = -ka.$$
*Why:* A hard wall forces a node at $r = a$; the phase must arrange the sine to vanish there. The negative sign marks a repulsive interaction (the wave is pushed out).
*Check:* This is exact for all $k$ — no low-energy approximation yet. The phase grows linearly with momentum, as expected for a fixed-size repulsive scatterer.

**Step 3 — Take the low-energy limit.** For $ka \ll 1$, only $\ell = 0$ contributes, and $\sin\delta_0 = \sin(-ka) \approx -ka$:
$$\sigma_\text{tot} = \frac{4\pi}{k^2}\sin^2\delta_0 \approx \frac{4\pi}{k^2}(ka)^2 = 4\pi a^2.$$
*Why:* At low energy the partial-wave sum truncates to a single isotropic s-wave; the cross-section becomes energy-independent.
*Check:* The differential cross-section $d\sigma/d\Omega = |f|^2 \approx a^2$ is isotropic, and integrating $a^2$ over $4\pi$ steradians gives $4\pi a^2$ — internally consistent.

**Step 4 — Interpret the factor of four.** The classical geometric cross-section is $\pi a^2$ (the shadow disk). The quantum result is *four times* larger because a spherically symmetric scatterer of size $a$ scatters *isotropically* into all $4\pi$ steradians, not just into a forward disk.
*Why:* Classical particles travel in straight lines and only the shadow matters; the quantum wave diffracts around the sphere and radiates in all directions equally.
*Check:* The factor 4 is exactly the ratio $4\pi/\pi$ of full solid angle to the classical disk — not a coincidence but the isotropy of s-wave scattering.

**Step 5 — Take the high-energy limit.** For $ka \gg 1$, partial waves up to $\ell_\text{max} \approx ka$ contribute; the hard-sphere phase shifts oscillate so that $\langle\sin^2\delta_\ell\rangle \to 1/2$. Summing:
$$\sigma_\text{tot} \approx \frac{4\pi}{k^2}\sum_{\ell=0}^{ka}(2\ell+1)\cdot\frac12 \approx \frac{4\pi}{k^2}\cdot\frac{(ka)^2}{2} = 2\pi a^2.$$
*Why:* Many channels are now open; the sum $\sum_{\ell=0}^{ka}(2\ell+1) \approx (ka)^2$ counts them, and the half from $\langle\sin^2\rangle$ halves the unitarity-saturated estimate.
*Check:* The extra $\pi a^2$ beyond the geometric $\pi a^2$ is the diffractive forward shadow — blocking the beam requires a forward-scattered wave that interferes destructively with the incident wave, and that wave carries probability. This is the quantum Babinet's principle.

**Final answer:** $\delta_0 = -ka$ (exact); $\sigma_\text{tot} \to 4\pi a^2$ at $ka \ll 1$ and $\to 2\pi a^2$ at $ka \gg 1$.

**What made this work:** The single exact phase shift $\delta_0 = -ka$ carried the whole low-energy story, and the partial-wave sum carried the high-energy story. The lesson is that *neither limit matches the classical $\pi a^2$*, and the deviations are diagnostic: the factor of four signals isotropic s-wave diffraction, the factor of two signals the forward diffractive shadow. Checking a quantum cross-section against its classical geometric value is itself a validity test — if you get $\pi a^2$ you have lost the wave physics.

**Self-explanation prompt:** In your own words, why is the high-energy cross-section ($2\pi a^2$) *twice* the geometric shadow rather than equal to it, even though "high energy" sounds like it should be the classical limit?

---

## Part B — Matched Practice Problem

**The problem:** For an attractive spherical square well of depth $V_0$ and radius $a$ (with interior wavevector $\kappa = \sqrt{k^2 + 2mV_0/\hbar^2}$), the exact s-wave phase shift is $\delta_0 = \arctan\!\left(\frac{k}{\kappa}\tan(\kappa a)\right) - ka$. (i) Take the low-energy limit $k\to0$ to extract the scattering length $a_s = a\!\left[1 - \frac{\tan(\kappa_0 a)}{\kappa_0 a}\right]$ with $\kappa_0 = \sqrt{2mV_0/\hbar^2}$. (ii) Find the condition on $\kappa_0 a$ at which $a_s \to \pm\infty$. (iii) State the low-energy cross-section $\sigma_\text{tot} \to 4\pi a_s^2$ and explain what the divergence means physically.

Work it in the same conceptual moves as Part A: identify the exterior solution and phase shift (given), impose the matching condition that produced it, take the low-energy limit to get $a_s$, interpret the divergence, and read off the cross-section.

**Stuck?** The scattering length diverges when $\tan(\kappa_0 a) \to \infty$, i.e. $\kappa_0 a = (n + 1/2)\pi$. Compare to Part A's hard sphere, where $a_s = a$ exactly (no internal structure to tune). The divergence is the Levinson signature of a new bound state appearing at threshold.

*Instructor note: no solution is provided here. The teaching point is that, unlike the hard sphere whose $a_s = a$ is fixed, the well's scattering length can be *tuned through infinity* by deepening the well — the cross-section $4\pi a_s^2$ diverges exactly when a bound state emerges at threshold, the same physics behind nuclear virtual states and ultracold Feshbach resonances.*

---

## Part C — Completion Problem

**The problem:** Verify the optical theorem $\sigma_\text{tot} = \frac{4\pi}{k}\operatorname{Im}f(0)$ for pure s-wave scattering, starting from the partial-wave amplitude.

**Step 1 — Write the forward amplitude.** Evaluate $f(\theta)$ at $\theta = 0$ using $P_\ell(1) = 1$, keeping only $\ell = 0$:
$$f(0) = \frac{1}{k}e^{i\delta_0}\sin\delta_0.$$
*Why:* The optical theorem relates the *forward* amplitude to the total cross-section; $\theta = 0$ is where the scattered wave interferes with the incident beam.

**Step 2 — Take the imaginary part.** Write $e^{i\delta_0} = \cos\delta_0 + i\sin\delta_0$, so $e^{i\delta_0}\sin\delta_0 = \sin\delta_0\cos\delta_0 + i\sin^2\delta_0$:
$$\operatorname{Im}f(0) = \frac{1}{k}\sin^2\delta_0.$$
*Why:* Only the imaginary part of the forward amplitude is fixed by unitarity; it counts the probability removed from the forward beam.

**Step 3 — Compute the total cross-section independently from the partial-wave sum.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Compare $\frac{4\pi}{k}\operatorname{Im}f(0)$ to $\sigma_\text{tot}$ and confirm they agree.**
*Your work here:*

*Why (your explanation):*

**Step 5 — State the physical content.** Whenever the potential removes probability from the forward beam, the forward-scattered wave must interfere destructively with the incident wave to form a shadow — and that destructive interference requires a specific imaginary component in $f(0)$.
*Why:* The optical theorem is a consequence of unitarity; it holds even for inelastic scattering, where $\sigma_\text{tot}$ includes every process.

**Final answer:** $\frac{4\pi}{k}\operatorname{Im}f(0) = \frac{4\pi}{k}\cdot\frac{\sin^2\delta_0}{k} = \frac{4\pi}{k^2}\sin^2\delta_0 = \sigma_\text{tot}$ — the optical theorem holds exactly for the s-wave.

**Self-explanation prompt:** Why does the optical theorem involve only the *imaginary* part of $f(0)$, and what would a nonzero real part of $f(0)$ contribute instead?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the total cross-section for a square well at $ka = 5$, where the phase shifts are $\delta_0 = 1.3$, $\delta_1 = 0.9$, $\delta_2 = 0.5$, $\delta_3 = 0.2$, $\delta_4 = 0.05$ rad (in units where $a = 1$).

**Student's work:**

Step 1 — At $ka = 5$, the number of contributing partial waves is $\ell_\text{max} \approx ka = 5$, so I keep $\ell = 0$ through $4$.

Step 2 — The partial cross-sections use $\sigma_\ell = (4\pi/k^2)(2\ell+1)\sin^2\delta_\ell$.

⚠ Step 3 — I truncate after $\ell = 0$ because the s-wave is always dominant: $\sigma_\text{tot} \approx (4\pi/k^2)\sin^2(1.3) = (4\pi/25)(0.928) \approx 0.47$.

Step 4 — So the total cross-section is about $0.47$ in these units.

**Your tasks:**
1. Identify the error in Step 3: the student keeps only $\ell = 0$ despite stating in Step 1 that $\ell_\text{max} \approx ka = 5$. State the rule for when truncating at $\ell = 0$ is legitimate.
2. Compute the full sum $\sigma_\text{tot} = (4\pi/k^2)\sum_{\ell=0}^{4}(2\ell+1)\sin^2\delta_\ell$ using the given phase shifts.
3. By what factor does the correct answer exceed the student's s-wave-only estimate?
4. Verify the result against the optical theorem $\sigma_\text{tot} = (4\pi/k)\operatorname{Im}f(0)$ using the same phase shifts, and explain why this check would have caught the truncation error.

**Why this error is common:** Students learn "only $\ell = 0$ matters" in the $ka \ll 1$ regime and over-apply it, truncating the partial-wave sum at $ka = 5$ where it has not converged ($\ell_\text{max} \sim ka$ means five channels contribute).

---

## Part E — Transfer Problem

**The problem:** A scattering resonance occurs when the s-wave phase shift passes through $\pi/2$, where $\sin^2\delta_0 \to 1$ and the partial cross-section hits the unitarity limit. Near a resonance at energy $E_R$, the phase shift has the Breit-Wigner form $\tan\delta_0(E) = \frac{\Gamma/2}{E_R - E}$, with $\Gamma$ the width. (i) Show that $\delta_0 = \pi/2$ exactly at $E = E_R$. (ii) Write the s-wave cross-section $\sigma_0 = (4\pi/k^2)\sin^2\delta_0$ as a function of $E$ near resonance and show it is a Lorentzian peaking at $4\pi/k_R^2$. (iii) Explain how the resonance is the scattering analog of a driven oscillator, and what a narrow $\Gamma$ says about the quasi-bound state's lifetime.

**Hint (use only if stuck after 10 minutes):** Use $\sin^2\delta_0 = \frac{\tan^2\delta_0}{1 + \tan^2\delta_0}$ to convert the Breit-Wigner $\tan\delta_0$ into $\sin^2\delta_0 = \frac{(\Gamma/2)^2}{(E_R - E)^2 + (\Gamma/2)^2}$ — a Lorentzian of full width $\Gamma$ centered at $E_R$. This is the same algebra that turns the Rabi detuning into a sinc-squared lineshape; resonance is resonance.

**Reflection prompt:** (1) The cross-section peaks at the *unitarity bound* $4\pi/k_R^2$ at $E = E_R$ — why can a quantum cross-section reach a hard ceiling that has no classical analog? (2) A narrow resonance ($\Gamma$ small) corresponds to a long-lived quasi-bound state; how is the relation $\tau \sim \hbar/\Gamma$ the scattering version of the time-energy uncertainty connection you met in the golden-rule chapter?

---

## Part F — Interleaved Review

**F1 — This chapter.** A hard sphere of radius $a$ is probed at $ka = 0.1$ (low) and $ka = 5$ (high). (a) Using $\delta_0 = -ka$, compute $\sigma_\text{tot}/\pi a^2$ at $ka = 0.1$ and confirm it is near 4. (b) Estimate $\sigma_\text{tot}/\pi a^2$ at $ka = 5$ from the high-energy result and confirm it approaches 2. (c) Identify the value of $ka$ at which the transition between the two regimes occurs. (d) Explain why checking the quantum cross-section against the classical $\pi a^2$ is itself a validity diagnostic.
*Chapter this draws from: 7.*

**F2 — Previous chapter.** *Chapter this draws from: Chapter 6 — Radiation and Fermi's Golden Rule.* Both the scattering resonance and the golden-rule transition rate are governed by a Lorentzian/sinc lineshape that peaks when an energy matches a natural scale of the system. In Chapter 6 the golden rule gave a transition *rate* $W = (2\pi/\hbar)|V_{fi}|^2\rho(E_f)$ — probability per unit time into a continuum. Here the Breit-Wigner resonance has a *width* $\Gamma$ and a quasi-bound-state lifetime $\tau \sim \hbar/\Gamma$. Explain, in two or three sentences, how the resonance width $\Gamma$ plays the role of the golden-rule decay rate: a quasi-bound state trapped behind a barrier decays into the scattering continuum at a rate set by $\Gamma/\hbar$, just as an excited atom decays into the photon continuum at rate $W$. Both are "leak into a continuum" problems wearing different clothes.

**F3 — Discrimination.** You are handed a central-potential scattering problem and asked for the total cross-section. Decide whether to (i) keep only $\ell = 0$ (s-wave), (ii) sum partial waves up to $\ell_\text{max} \approx ka$, or (iii) expect a sharp resonance peak from a single channel. State the checks that select between them.
*Note to instructor: the discriminating checks are $ka$ against 1 (s-wave only if $ka \ll 1$, else sum to $\ell_\text{max} \approx ka$) and whether a phase shift passes through $\pi/2$ (resonance); students who truncate at $\ell = 0$ when $ka \sim 5$ have missed the channel-count estimate.*

**Closing reflection:** Across F1–F3, what single dimensionless number tells you how many partial waves your problem needs — and what independent identity lets you check the sum once you have it?

---

## Instructor Notes

**Common errors:**
- Truncating the partial-wave sum at $\ell = 0$ where it has not converged; the correct cutoff is $\ell_\text{max} \sim ka$ (Part D's misconception).
- Using the wrong prefactor in $\sigma_\text{tot} = (4\pi/k^2)\sum(2\ell+1)\sin^2\delta_\ell$ — dropping the $(2\ell+1)$ degeneracy factor or the $1/k^2$.
- Misstating the optical theorem as $(4\pi/k^2)\operatorname{Im}f(0)$ instead of $(4\pi/k)\operatorname{Im}f(0)$ (wrong power of $k$).

**Signs a student needs to return:**
- They report the low-energy cross-section as the classical $\pi a^2$ instead of $4\pi a^2$, missing the factor-of-four wave enhancement.
- They cannot use the optical theorem as an independent check and instead trust an unverified partial-wave sum.

**Scaffolding adjustments:** If a student struggles with Part A, have them first compute $\sum_{\ell=0}^{N}(2\ell+1)$ for small $N$ and confirm it equals $(N+1)^2$, so the high-energy channel count is transparent before the cross-section. If a student finishes Part F quickly, have them track the $\arctan$ branch of $\delta_0(k)$ for a square well across a resonance and add the $n\pi$ correction to keep the phase continuous.

**Domain adaptation note:** The partial-wave / scattering-length framework transfers directly to nuclear physics (neutron-proton scattering lengths $a_t \approx 5.4$ fm, $a_s \approx -23.7$ fm signaling a virtual bound state) and to ultracold atoms (Feshbach resonances tuning $a_s$ from $-\infty$ to $+\infty$ with a magnetic field).
