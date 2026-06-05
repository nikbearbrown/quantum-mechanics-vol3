# Worked Exercises: Scattering II: The Born Approximation
*Chapter 8 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The first Born amplitude $f_B(\theta) = -\frac{m}{2\pi\hbar^2}\int e^{i\vec q\cdot\vec r}V(\vec r)\,d^3r = -\frac{m}{2\pi\hbar^2}\widetilde V(\vec q)$ — proportional to the Fourier transform of the potential at the momentum transfer.
- The momentum transfer $\vec q = \vec k - \vec k'$ with magnitude $q = 2k\sin(\theta/2)$ for elastic scattering — *not* $q = k$.
- The Born validity parameter $\xi = 2m|V_0|/\hbar^2\mu^2$ (low energy) and $\xi/ka$ (high energy), and the special fact that for the Coulomb potential Born is *exact* by phase cancellation ($|\Gamma(1+i\eta)/\Gamma(1-i\eta)| = 1$), not because the Sommerfeld parameter $\eta$ is small.

---

## Part A — Full Worked Example

**What this demonstrates:** That the Born amplitude is the Fourier transform of the potential at momentum transfer $q = 2k\sin(\theta/2)$, and that the screened-Coulomb (Yukawa) result reduces to the exact Rutherford formula in the $\mu\to0$ limit.

**The problem:** For the Yukawa potential $V(r) = \frac{V_0 e^{-\mu r}}{\mu r}$, compute the Born scattering amplitude and differential cross-section. Then take the Coulomb limit $\mu\to0$ with $V_0/\mu \to ZZ'e^2/(4\pi\epsilon_0)$ and recover the Rutherford formula.

**The solution:**

**Step 1 — Reduce the 3D Fourier transform to a 1D sine transform.** For a spherically symmetric potential, integrating over the angles of $\vec r$ in $\int e^{i\vec q\cdot\vec r}V(r)\,d^3r$ leaves
$$\widetilde V(q) = \frac{4\pi}{q}\int_0^\infty r\,V(r)\sin(qr)\,dr.$$
*Why:* Spherical symmetry kills the $\phi$ and $\theta$ angular dependence, collapsing the 3D transform to a single radial integral weighted by $\sin(qr)$.
*Check:* The prefactor $4\pi/q$ carries the right dimensions: $V(r)$ has energy units, the $r\,dr$ gives length², and $4\pi/q$ gives length, so $\widetilde V$ has energy·length³, as a 3D Fourier transform must.

**Step 2 — Evaluate the Yukawa integral.** Substituting $V(r) = V_0 e^{-\mu r}/(\mu r)$:
$$\widetilde V(q) = \frac{4\pi V_0}{\mu q}\int_0^\infty e^{-\mu r}\sin(qr)\,dr = \frac{4\pi V_0}{\mu q}\cdot\frac{q}{q^2 + \mu^2} = \frac{4\pi V_0}{\mu}\cdot\frac{1}{q^2 + \mu^2}.$$
*Why:* The $1/r$ in the Yukawa potential cancels the $r$ in the sine-transform measure, leaving the elementary integral $\int_0^\infty e^{-\mu r}\sin(qr)\,dr = q/(q^2+\mu^2)$.
*Check:* As $q\to0$ (forward), $\widetilde V \to 4\pi V_0/(\mu^3)$ — finite, as it must be for a finite-range potential.

**Step 3 — Form the Born amplitude with the correct momentum transfer.** Insert $\widetilde V(q)$ into $f_B = -\frac{m}{2\pi\hbar^2}\widetilde V(q)$ and use $q = 2k\sin(\theta/2)$:
$$f_B(\theta) = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{q^2 + \mu^2} = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{4k^2\sin^2(\theta/2) + \mu^2}.$$
*Why:* The angle dependence enters *only* through $q = 2k\sin(\theta/2)$; using $q = k$ here would be a serious error, missing the $\sin(\theta/2)$ structure entirely.
*Check:* The cross-section $d\sigma/d\Omega = |f_B|^2 = \left(\frac{2mV_0}{\hbar^2\mu}\right)^2\frac{1}{[4k^2\sin^2(\theta/2)+\mu^2]^2}$ is strongly forward-peaked, falling as $q^4$ at large angle — the expected diffraction pattern.

**Step 4 — Take the Coulomb limit.** Set $\mu\to0$ with $V_0/\mu \to ZZ'e^2/(4\pi\epsilon_0)$. The $\mu^2$ in the denominator vanishes:
$$\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0}\right)^2\frac{m^2}{\hbar^4\cdot4k^4\sin^4(\theta/2)} = \left(\frac{ZZ'e^2}{16\pi\epsilon_0 E}\right)^2\frac{1}{\sin^4(\theta/2)},$$
using $E = \hbar^2 k^2/(2m)$.
*Why:* The screened Coulomb potential becomes the bare Coulomb potential as the screening range $1/\mu \to \infty$; the cross-section inherits the $\sin^{-4}(\theta/2)$ Rutherford angular law.
*Check:* The $\sin^{-4}(\theta/2)$ dependence and the $E^{-2}$ scaling are the hallmark Rutherford signatures confirmed by Geiger and Marsden across energies and target materials.

**Step 5 — Note why this agreement is exact, not approximate.** For the Coulomb potential the exact quantum amplitude carries a phase $e^{-i\eta\ln\sin^2(\theta/2)}\,\Gamma(1+i\eta)/\Gamma(1-i\eta)$, but $|e^{-i\eta\ln\sin^2(\theta/2)}|^2 = 1$ and $|\Gamma(1+i\eta)/\Gamma(1-i\eta)| = 1$, so all phases cancel in $|f|^2$.
$$|f_\text{exact}|^2 = |f_B|^2 \quad\text{(Coulomb only)}.$$
*Why:* The $1/r$ potential is scale-invariant — it has no intrinsic length — and its SO(4) symmetry forces the phase corrections to cancel. No other potential shares this.
*Check:* For 5 MeV alphas on gold the Sommerfeld parameter $\eta \approx 22 \gg 1$, so the naive Born small-parameter is *not* small — yet Born is still exact, confirming the agreement comes from phase cancellation, not from $\eta \ll 1$.

**Final answer:** $f_B(\theta) = -\frac{2mV_0}{\hbar^2\mu}\frac{1}{4k^2\sin^2(\theta/2)+\mu^2}$; in the $\mu\to0$ limit $\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{16\pi\epsilon_0 E}\right)^2\sin^{-4}(\theta/2)$ — the Rutherford formula, exact for Coulomb.

**What made this work:** The Born amplitude is a diffraction experiment on the potential — every scattering angle probes a different Fourier mode $\widetilde V(q)$ with $q = 2k\sin(\theta/2)$. The Yukawa integral is elementary, and the Coulomb limit falls out by sending the screening range to infinity. The deep point is that Born reproduces Rutherford *exactly*, not approximately, and the reason — unit-modulus Coulomb phases from scale invariance — is special to $1/r$ and does not generalize. Knowing *why* the agreement holds tells you it will not survive for any other potential.

**Self-explanation prompt:** Explain why using $q = k$ instead of $q = 2k\sin(\theta/2)$ would destroy the entire angular structure of the cross-section — what does $q = 2k\sin(\theta/2)$ encode geometrically?

---

## Part B — Matched Practice Problem

**The problem:** For the Gaussian potential $V(r) = V_0 e^{-r^2/a^2}$, compute the Born scattering amplitude and differential cross-section. Then compare the angular width of the forward peak to that of a Yukawa potential of the same range $1/\mu = a$.

Work it in the same conceptual moves as Part A: reduce the 3D Fourier transform to the 1D sine integral, evaluate the Gaussian integral analytically, form $f_B$ with $q = 2k\sin(\theta/2)$, and read off the angular distribution.

**Stuck?** The 1D sine transform of a Gaussian is itself a Gaussian: $\widetilde V(q) = \frac{4\pi}{q}\int_0^\infty r V_0 e^{-r^2/a^2}\sin(qr)\,dr \propto a^3 e^{-q^2 a^2/4}$. So $d\sigma/d\Omega \propto e^{-q^2 a^2/2}$ — a Gaussian in $q$, which falls off *faster* at large angle than the Yukawa's power-law $1/(q^2+\mu^2)^2$. The same $q = 2k\sin(\theta/2)$ governs the angle.

*Instructor note: no solution is provided here. The teaching point is that a smooth (Gaussian) potential gives a Gaussian-suppressed cross-section — falling faster at large $q$ than the power-law Yukawa — because a smoother potential has a more rapidly decaying Fourier transform; the forward peak is narrower for the Gaussian.*

---

## Part C — Completion Problem

**The problem:** Compute the nuclear form factor $F(q)$ for a uniform spherical charge distribution $\rho(r) = 3/(4\pi R^3)$ for $r \leq R$ (zero outside, normalized to 1), and find the momentum transfer at which $|F(q)|^2$ first vanishes.

**Step 1 — Set up the form-factor integral.** The form factor is the Fourier transform of the charge density, which for a spherical distribution reduces to a 1D sine transform:
$$F(q) = \int e^{i\vec q\cdot\vec r}\rho(r)\,d^3r = \frac{4\pi}{q}\int_0^R r\,\rho(r)\sin(qr)\,dr.$$
*Why:* Same spherical reduction as the Born amplitude; the form factor multiplies the point-particle cross-section when the target has internal structure.

**Step 2 — Insert the uniform density.** With $\rho = 3/(4\pi R^3)$ constant inside $R$:
$$F(q) = \frac{4\pi}{q}\cdot\frac{3}{4\pi R^3}\int_0^R r\sin(qr)\,dr = \frac{3}{qR^3}\int_0^R r\sin(qr)\,dr.$$
*Why:* The constant density pulls out of the integral, leaving the elementary $\int_0^R r\sin(qr)\,dr$.

**Step 3 — Evaluate the integral $\int_0^R r\sin(qr)\,dr$ and assemble $F(q)$.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Find the first zero of $|F(q)|^2$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — State the physical use.** Measuring the angle at which the cross-section first dips to zero gives $q_0$, and $q_0 R \approx 4.49$ then yields the nuclear radius $R$ directly. This is how Hofstadter measured the proton charge radius.
*Why:* The form factor suppresses large-angle scattering relative to a point particle — the extended target is "softer" — and the location of the first zero is a direct ruler for the size $R$.

**Final answer:** $F(q) = \frac{3}{(qR)^3}[\sin(qR) - qR\cos(qR)] = \frac{3 j_1(qR)}{qR}$, which first vanishes at $qR \approx 4.49$ (the first zero of $j_1$).

**Self-explanation prompt:** Why does an extended charge distribution scatter *less* at large angles than a point charge of the same total charge, and how does the first zero of $|F|^2$ act as a ruler for the nuclear radius?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the Born differential cross-section for a Yukawa potential at scattering angle $\theta = 60°$ with $k = 2\mu$ (so $ka$ is moderate), and judges whether Born is reliable.

**Student's work:**

Step 1 — The Born amplitude is $f_B(\theta) = -\frac{2mV_0}{\hbar^2\mu}\frac{1}{q^2 + \mu^2}$.

Step 2 — The cross-section is $d\sigma/d\Omega = |f_B|^2$.

⚠ Step 3 — The momentum transfer is just the wavevector magnitude, $q = k = 2\mu$, so $q^2 + \mu^2 = 4\mu^2 + \mu^2 = 5\mu^2$, giving $d\sigma/d\Omega = \left(\frac{2mV_0}{\hbar^2\mu}\right)^2\frac{1}{25\mu^4}$.

Step 4 — Since this is the Coulomb-like Born formula, Born must be exact here as it is for Rutherford.

**Your tasks:**
1. Identify the error in Step 3 and compute the correct momentum transfer $q = 2k\sin(\theta/2)$ at $\theta = 60°$, $k = 2\mu$. Then recompute $q^2 + \mu^2$.
2. Recompute the differential cross-section with the correct $q$, and find the ratio between the student's wrong answer and the correct one.
3. Correct the false claim in Step 4: state why Born being exact for the *Coulomb* potential does *not* imply it is exact for the *Yukawa* potential, even though the Yukawa formula looks similar.
4. State the actual Born validity check for this Yukawa problem ($\xi = 2m|V_0|/\hbar^2\mu^2$ against 1, and whether the potential binds), and explain how it differs from the Coulomb case where $\eta \approx 22 \gg 1$ yet Born is exact.

**Why this error is common:** Students conflate $q$ with $k$, forgetting that the momentum transfer depends on the scattering angle through $q = 2k\sin(\theta/2)$, and they over-generalize the Coulomb "Born is exact" result to every potential of similar form.

---

## Part E — Transfer Problem

**The problem:** Apply the Born approximation to the *attractive square well* $V(r) = -V_0$ for $r < a$, zero outside, with $V_0 = \hbar^2/(2ma^2)$ (so $\xi \approx 1$). (i) Compute the Born scattering amplitude using the 1D sine-transform formula. (ii) State qualitatively how the Born total cross-section compares to the exact s-wave result (from Chapter 7's phase-shift formula) at $ka = 1$ and $ka = 5$. (iii) Identify whether the exact result has a resonance that Born misses, and characterize the Born error — is it a factor-of-2 discrepancy, or a *qualitative* failure?

**Hint (use only if stuck after 10 minutes):** The 1D sine transform of a constant $-V_0$ over $[0, a]$ gives $\widetilde V(q) = -\frac{4\pi V_0}{q^3}[\sin(qa) - qa\cos(qa)]$, so $f_B(\theta) = \frac{2mV_0}{\hbar^2 q^3}[\sin(qa) - qa\cos(qa)]$ with $q = 2k\sin(\theta/2)$. The key conceptual move is that Born, assuming the wavefunction is barely disturbed, predicts a *smooth* cross-section and *no resonance peak* — exactly the structure the exact phase-shift treatment shows when $\delta_0$ passes through $\pi/2$.

**Reflection prompt:** (1) Near a resonance the exact wavefunction inside the well is dramatically enhanced — the very thing Born ignores by setting $\psi \approx e^{i\vec k\cdot\vec r}$ inside. Why does this make Born's failure *qualitative* (a missing peak) rather than merely a wrong number? (2) The Born parameter $\xi \approx 1$ here sits right at the boundary of validity. How does this connect to the Chapter 5/6 lesson that you must check the small parameter *before* trusting a perturbative method, not after?

---

## Part F — Interleaved Review

**F1 — This chapter.** Alpha particles ($Z=2$, $E = 8$ MeV) scatter off silver ($Z'=47$), with $e^2/(4\pi\epsilon_0) = 1.44$ MeV·fm. (a) Write the Rutherford cross-section $d\sigma/d\Omega = (ZZ'e^2/16\pi\epsilon_0 E)^2\sin^{-4}(\theta/2)$. (b) Evaluate it at $\theta = 60°$ and $\theta = 120°$ in fm²/sr. (c) Confirm the log-log slope of $d\sigma/d\Omega$ vs $\sin(\theta/2)$ is $-4$. (d) Compute the Sommerfeld parameter $\eta$ and confirm it is $\gg 1$, so that Born is exact here by phase cancellation rather than by a small parameter.
*Chapter this draws from: 8.*

**F2 — Previous chapter.** *Chapter this draws from: Chapter 7 — Scattering I: Partial Waves.* The Born approximation and the partial-wave expansion are two complementary ways to organize the *same* scattering amplitude: Born expands in powers of the potential $V$ (good at high energy / weak potential), partial waves expand in angular-momentum channels $\ell$ (good at low energy, where only $\ell = 0$ survives). Explain, in two or three sentences, how the same physical cross-section can be computed either way — for a square well, Born gives a smooth $\widetilde V(q)$ while the partial-wave sum can show a sharp resonance when $\delta_0$ passes through $\pi/2$ — and why the partial-wave method captures the resonance that Born misses (Born assumes $\psi$ inside the well is undisturbed, the exact opposite of the resonant enhancement the phase shift encodes).

**F3 — Discrimination.** You are handed a scattering problem and asked for the differential cross-section. Decide whether to (i) use the Born approximation (Fourier-transform the potential), (ii) use the partial-wave / phase-shift method, or (iii) expect Born to fail qualitatively near a resonance. State the checks that select between them.
*Note to instructor: the discriminating checks are the Born parameter $\xi$ against 1 (and whether the potential binds), $ka$ for the number of partial waves, and whether a resonance is present (Born misses it entirely); students who apply Born to a strong binding potential at low energy and report a smooth curve have missed that $\xi \gtrsim 1$ and that the failure is a missing peak, not a small error.*

**Closing reflection:** Across F1–F3, the Born approximation can fail in two distinct ways — a wrong *number* (quantitative) and a wrong *shape* (qualitative, near resonance). Which single check distinguishes the regime where Born is merely approximate from the regime where it is structurally blind?

---

## Instructor Notes

**Common errors:**
- Using $q = k$ instead of $q = 2k\sin(\theta/2)$, destroying the angular structure of the cross-section (Part D's core misconception).
- Wrong prefactor or sign in $f_B = -\frac{m}{2\pi\hbar^2}\widetilde V(q)$ — dropping the minus sign or the $1/2\pi$.
- Assuming the Born small-parameter (Sommerfeld $\eta \ll 1$) holds for Coulomb — it does not ($\eta \approx 22$ for 5 MeV alphas on gold); Born is exact there by phase cancellation, not by a small parameter.

**Signs a student needs to return:**
- They claim "Born equals the classical result" as a general rule, instead of recognizing it as special to the Coulomb potential's scale invariance.
- They report a smooth Born cross-section near a known resonance without flagging that Born is structurally blind to resonances.

**Scaffolding adjustments:** If a student struggles with Part A, have them first verify the geometric identity $q = 2k\sin(\theta/2)$ by drawing the isoceles momentum triangle ($|\vec k| = |\vec k'| = k$, angle $\theta$ between them) before touching any integral. If a student finishes Part F quickly, have them set up the second Born term $f_B^{(2)}$ and explain why each successive term is suppressed by one power of $\xi$ — the Born series as perturbation theory in $V$.

**Domain adaptation note:** The Fourier-transform-of-the-potential structure transfers to any scattering target — nuclear form factors (Hofstadter's proton radius), screened atomic potentials, and in generalized form to deep inelastic scattering, where the same logic probed the quark substructure of the proton at SLAC.
