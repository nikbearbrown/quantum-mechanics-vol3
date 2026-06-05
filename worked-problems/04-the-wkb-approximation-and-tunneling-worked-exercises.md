# Worked Exercises: The WKB Approximation and Tunneling

*Chapter 4 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The Gamow factor and transmission: $T \approx e^{-2\gamma}$ with $\gamma = \tfrac{1}{\hbar}\int_a^b\sqrt{2m(V(x)-E)}\,dx$ over the forbidden region — WKB nails the exponent, misses the $O(1)$ prefactor.
- The Bohr–Sommerfeld quantization $\oint p\,dx = 2\int_a^b p\,dx = (n + \tfrac{1}{2})h$, where the $\tfrac{1}{2}$ is the combined Maslov correction ($\pi/4$ per smooth turning point), and a hard wall contributes $\pi/2$ instead.
- The validity condition $|d\lambda_\text{dB}/dx| \ll 1$ (slowly varying potential), failing at turning points where $p\to 0$; the rectangular-barrier $\kappa = \sqrt{2m(V_0-E)}/\hbar$.

## Part A — Full Worked Example

**What this demonstrates:** How to compute a WKB transmission coefficient through a rectangular barrier and quantify what WKB gets right (the exponent) versus what it misses (the prefactor).

**The problem:** An electron ($m_e = 9.11\times10^{-31}$ kg) with kinetic energy $E = 1$ eV hits a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å. Compute the WKB transmission coefficient $T_\text{WKB}$, compare it to the exact result, and account for the discrepancy.

**The solution:**

**Step 1 — Compute the decay constant.** With $V_0 - E = 4$ eV,
$$\kappa = \frac{\sqrt{2m_e(V_0-E)}}{\hbar} = \frac{\sqrt{2\times 9.11\times10^{-31}\times 4\times 1.6\times10^{-19}}}{1.055\times10^{-34}} \approx 1.02\ \text{Å}^{-1}.$$
*Why:* In the forbidden region the momentum is imaginary, $p = i\hbar\kappa$, and $\kappa$ sets the exponential decay rate of the wave function inside the barrier.
*Check:* The shortcut $\kappa \approx 0.5123\sqrt{V_0-E\,[\text{eV}]}$ Å$^{-1}$ gives $0.5123\times 2 = 1.02$ Å$^{-1}$ — agreement.

**Step 2 — Evaluate the Gamow factor.** For a rectangular barrier $\sqrt{2m(V-E)}$ is constant, so $\gamma = \kappa L$:
$$\gamma = \kappa L = 1.02\times 5 = 5.10.$$
*Why:* The Gamow integral $\tfrac{1}{\hbar}\int_a^b\sqrt{2m(V-E)}\,dx$ collapses to $\kappa L$ when the integrand is constant across the barrier width.
*Check:* $\gamma = 5.1 \gg 1$, so we are in the thick-barrier regime where WKB is meant to apply.

**Step 3 — Apply the WKB transmission formula.**
$$T_\text{WKB} = e^{-2\gamma} = e^{-10.2} \approx 3.7\times10^{-5}.$$
*Why:* The transmission coefficient is the square of the amplitude attenuation across the barrier, giving the factor of $2$ in the exponent — $T \approx e^{-2\gamma}$, not $e^{-\gamma}$.
*Check:* $T \ll 1$, consistent with deep sub-barrier tunneling ($E = 1$ eV well below $V_0 = 5$ eV).

**Step 4 — Compare to the exact result and explain the gap.** The exact rectangular-barrier transmission is
$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1} \approx 9.5\times10^{-5},$$
so $T_\text{exact}/T_\text{WKB} \approx 2.56$. This matches the analytic prefactor $16E(V_0-E)/V_0^2 = 16\times 1\times 4/25 = 2.56$.
*Why:* WKB reproduces the exponential but drops a smooth $O(1)$ prefactor; on a log plot $T_\text{exact}$ and $T_\text{WKB}$ run parallel with a constant offset.
*Check:* The prefactor is order unity, not exponential — for physics spanning 24 decades (alpha decay), this offset is invisible.

**Final answer:** $T_\text{WKB} = e^{-10.2} \approx 3.7\times10^{-5}$; the exact value $9.5\times10^{-5}$ differs by the $O(1)$ prefactor $16E(V_0-E)/V_0^2 \approx 2.56$.

**What made this work:** The central concept is that WKB captures the *exponent* of the transmission, not the prefactor, because the factor of $2$ in $T \approx e^{-2\gamma}$ comes from squaring the amplitude attenuation $e^{-\gamma}$ across the barrier. A common naive error is to write $T \approx e^{-\gamma}$ (dropping the $2$), which underestimates the suppression by an enormous factor when $\gamma$ is large. The discipline WKB teaches is to trust the exponential and treat the prefactor as a separate, harder problem — which is exactly why a WKB estimate of an alpha-decay halflife lands within a factor of 10 across 24 orders of magnitude.

**Self-explanation prompt:** Why does the factor of $2$ in the exponent $e^{-2\gamma}$ — rather than $e^{-\gamma}$ — follow from the transmission being a probability (amplitude squared)?

## Part B — Matched Practice Problem

**What this demonstrates:** The same Gamow-factor machinery applied to a triangular (field-emission) barrier, where the integrand is no longer constant.

**The problem:** An electron faces a triangular barrier $V(x) = V_0 - Fx$ for $0 < x < V_0/F$ (Fowler–Nordheim field emission), with $V_0 = 5$ eV and field $F$ chosen so the barrier width is $L = V_0/F$. At energy $E = 0$, compute the Gamow factor $\gamma$ and the WKB transmission $T_\text{WKB}$, expressing $\gamma$ in terms of $V_0$, $F$, $m$, and $\hbar$.

**Step 1 — Subgoal: Identify the turning points.** Find where $V(x) = E$ to set the integration limits $a$ and $b$.

**Step 2 — Subgoal: Set up the Gamow integral.** Write $\gamma = \tfrac{1}{\hbar}\int_a^b\sqrt{2m(V_0 - Fx - E)}\,dx$.

**Step 3 — Subgoal: Evaluate the integral.** Substitute $u = V_0 - Fx - E$ and integrate; expect $\gamma \propto (V_0-E)^{3/2}/F$.

**Step 4 — Subgoal: Apply the transmission formula.** Form $T_\text{WKB} = e^{-2\gamma}$ and confirm the thick-barrier condition.

**Stuck?** The integral $\int\sqrt{2m(V_0 - Fx)}\,dx$ over the barrier evaluates to $\tfrac{2}{3}\cdot\tfrac{\sqrt{2m}}{F}(V_0)^{3/2}$ at $E=0$; this $(V_0)^{3/2}/F$ scaling is the signature of the Fowler–Nordheim law that governs flash-memory write speeds.

*Instructor note: full solution intentionally omitted. This problem is for the student to complete after Part A.*

## Part C — Completion Problem

**The problem:** Use the Bohr–Sommerfeld condition to find the energy levels of the harmonic oscillator $V = \tfrac{1}{2}m\omega^2 x^2$ and confirm they are exact.

**Step 1 — Identify the turning points (provided).** At energy $E$, the classical turning points are where $V = E$: $x_\pm = \pm\sqrt{2E/m\omega^2}$. Between them the particle oscillates; outside it decays.

**Step 2 — Write the phase-space action (provided).** The closed-orbit action is the area of the phase-space ellipse: $\oint p\,dx = 2\int_{x_-}^{x_+}\sqrt{2m(E - \tfrac12 m\omega^2 x^2)}\,dx = \dfrac{2\pi E}{\omega}$.

**Step 3 — Apply the Bohr–Sommerfeld quantization.**
*Your work here:* Set $\oint p\,dx = (n+\tfrac{1}{2})h$ with two smooth turning points (Maslov $\tfrac14 + \tfrac14 = \tfrac12$), and solve $\dfrac{2\pi E}{\omega} = (n+\tfrac12)h$ for $E_n$.

*Why (your explanation):*

**Step 4 — Check the ground state and the Maslov role.**
*Your work here:* Evaluate $E_0$ and explain what the predicted ground-state energy would be if the $\tfrac{1}{2}$ (Maslov correction) were dropped.

*Why (your explanation):*

**Step 5 — Interpret (provided).** The result $E_n = (n+\tfrac12)\hbar\omega$ is the *exact* quantum spectrum, not an approximation — a consequence of the oscillator's hidden algebraic symmetry that terminates the WKB expansion. The zero-point energy $\tfrac12\hbar\omega$ is *entirely* the Maslov correction.

**Final answer:** $E_n = (n+\tfrac{1}{2})\hbar\omega$, exact; without the Maslov $\tfrac{1}{2}$ the predicted ground state would be the unphysical $E_0 = 0$.

**Self-explanation prompt:** The chapter says "the zero-point energy of the harmonic oscillator is a Maslov correction." Using your Step 4, explain precisely what that sentence means.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the WKB transmission of a proton through a barrier and presents:

**Step 1 (correct).** "For a rectangular barrier of height $V_0$ and width $L$ at energy $E < V_0$, the decay constant is $\kappa = \sqrt{2m(V_0-E)}/\hbar$ and the Gamow factor for this constant-integrand barrier is $\gamma = \kappa L$."

**Step 2 (correct).** "I compute $\kappa = 2.0$ Å$^{-1}$ and $L = 3$ Å, so $\gamma = \kappa L = 6.0$. We are in the thick-barrier regime $\gamma \gg 1$."

**Step 3 (⚠).** "The transmission coefficient is therefore $T_\text{WKB} = e^{-\gamma} = e^{-6.0} \approx 2.5\times10^{-3}$."

**Step 4 (correct-looking).** "Since $\gamma = 6$ is large and $T \approx 2.5\times10^{-3}$ is small, the proton rarely tunnels, consistent with a thick barrier."

**Your tasks:**
1. Identify the error in Step 3 and explain what went wrong.
2. Write the corrected Step 3.
3. Name the principle that was violated.
4. State a check that would catch this class of error.

**Why this error is common:** The transmission is the *square* of the amplitude attenuation, so the exponent carries a factor of $2$ — $T \approx e^{-2\gamma}$, not $e^{-\gamma}$ — and dropping that factor of $2$ overestimates the transmission by $e^{\gamma}$, an error that grows exponentially with barrier thickness.

## Part E — Transfer Problem

**What this demonstrates:** The Gamow-factor machinery transferred to a system outside the chapter's worked examples — proton–proton fusion in a stellar core (the Coulomb barrier the chapter mentions but does not compute in full).

**The problem:** Two protons approach each other in the solar core. Outside contact they see the Coulomb barrier $V(r) = \dfrac{e^2}{4\pi\epsilon_0 r}$ (charges $Z_1 = Z_2 = 1$). A proton with relative kinetic energy $E$ must tunnel from the classical turning point $r_c = \dfrac{e^2}{4\pi\epsilon_0 E}$ inward to contact radius $R \approx 0$. Set up the Gamow factor $\gamma = \tfrac{1}{\hbar}\int_R^{r_c}\sqrt{2m(V(r) - E)}\,dr$ and, using the substitution $r = r_c\sin^2\theta$ in the limit $R \ll r_c$, show that $\gamma \propto 1/\sqrt{E}$.

**Hint (use only if stuck after 10 minutes):** Be careful to keep the full Coulomb factor $\dfrac{1}{4\pi\epsilon_0}$ — including the $\pi$ — in $V(r)$. The substitution $r = r_c\sin^2\theta$ turns $\int_0^{r_c}\sqrt{r_c/r - 1}\,dr$ into a standard integral over $\theta$ giving $\tfrac{\pi}{2}r_c$; combined with $r_c \propto 1/E$ and the overall $\sqrt{2m}/\hbar$, this yields $\gamma \propto Z_1 Z_2/\sqrt{E}$ — the Geiger–Nuttall-style $1/\sqrt{E}$ dependence.

**Reflection prompt:**
1. The Gamow factor *decreases* with energy ($\gamma \propto 1/\sqrt E$) while the Maxwell–Boltzmann thermal population *decreases* with energy at high $E$. How does the product of these two opposing trends produce the Gamow peak the chapter describes?
2. If you had accidentally written $1/4\epsilon_0$ instead of $1/4\pi\epsilon_0$ in $V(r)$, in which direction and by what factor would your $\gamma$ be wrong?

## Part F — Interleaved Review

**F1.** For the "bouncing ball" potential $V(x) = mgx$ ($x>0$) with a hard wall at $x=0$, the hard wall contributes a Maslov phase of $\tfrac{\pi}{2}$ and the smooth turning point $\tfrac{\pi}{4}$, giving $(n+\tfrac{3}{4})$ on the right of the quantization condition. Explain why the hard wall and the smooth turning point contribute *different* Maslov phases.
*Chapter this draws from: 4*

**F2.** Return to the variational principle. For the harmonic oscillator, the Gaussian variational trial gives the exact ground-state energy $\tfrac12\hbar\omega$, and Bohr–Sommerfeld *also* gives the exact $\tfrac12\hbar\omega$ ground state. Explain what feature of the harmonic oscillator makes *both* approximation methods exact for this potential.
*Chapter this draws from: The Variational Principle (Chapter 3)*

**F3.** Discrimination: You are given a potential and must decide whether WKB (a) gives the *exact* spectrum, (b) gives a good leading-order estimate, or (c) fails near a turning point and needs the Airy connection. For (a) the harmonic oscillator, (b) a generic anharmonic well at large $n$, (c) the region right at a smooth turning point — assign each case.
*Note to instructor: the discriminating feature is the presence of a hidden algebraic symmetry (oscillator, Coulomb — WKB exact), versus a generic potential (good only at large $n$ where many wavelengths fit), versus the turning-point neighborhood itself (where $p\to0$, $\lambda_\text{dB}\to\infty$, and WKB must be replaced by Airy). Students who apply Bohr–Sommerfeld blindly near a turning point will hit the diverging $1/\sqrt{p}$ prefactor.*

**Closing reflection:** Across these problems, what single quantity must you estimate *before* trusting a WKB transmission or quantization result, and what does it being $\gg 1$ versus $\to 0$ tell you?

## Instructor Notes

**Common errors:**
1. Dropping the factor of $2$ in the tunneling exponent, writing $T \approx e^{-\gamma}$ instead of $T \approx e^{-2\gamma}$.
2. Omitting the Maslov/connection-formula $\tfrac{1}{4}$ per turning point — writing $\oint p\,dx = nh$ instead of $(n+\tfrac{1}{2})h$, which kills the zero-point energy.
3. Dropping the $\pi$ in the Coulomb factor $1/4\pi\epsilon_0$ when setting up the alpha-decay or fusion Gamow integral.

**Signs a student needs to return:**
- They predict a harmonic-oscillator ground state of $E_0 = 0$ (they dropped the Maslov $\tfrac12$).
- They apply the WKB tunneling formula at $E \approx V_0$ (barrier top) where it has a kink and fails, instead of checking $\kappa L \gg 1$.

**Scaffolding adjustments:** A student stuck on Part A should first verify the $\kappa$ shortcut $0.5123\sqrt{V_0-E\,[\text{eV}]}$ Å$^{-1}$ against the full SI computation before tackling the prefactor comparison. A student who finishes Part F quickly should compute the alpha-decay Gamow factor for $^{238}$U ($Z'=90$, $E_\alpha \approx 4.2$ MeV, $r_c\approx 60$ fm) and confirm $\gamma\approx 43$, $e^{-2\gamma}\approx 4\times10^{-38}$.

**Domain adaptation note:** For a device-physics cohort, recast Part B as the Fowler–Nordheim tunneling current setting the write speed and retention time of flash memory, where the same $(V_0)^{3/2}/F$ Gamow scaling controls every USB stick.
