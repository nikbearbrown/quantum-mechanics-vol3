# Chapter 7 — Scattering I: Partial Waves

## TL;DR

- A hard sphere of radius $a$ scatters *four times* its geometric cross-section at low energy — a purely wave-mechanical result with no classical counterpart.
- Every measurable feature of an elastic collision is encoded in one complex function: the scattering amplitude $f(\theta)$.
- For a central potential, $f(\theta)$ decomposes into a sum over angular-momentum channels (partial waves), each contributing one real number — the phase shift $\delta_\ell$ — to the total.
- At low energy, only the $\ell = 0$ channel matters; the entire collision reduces to a single parameter, the scattering length $a_s$.
- The optical theorem — $\sigma_{\rm tot} = (4\pi/k)\,\operatorname{Im}[f(0)]$ — is probability conservation in disguise.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember** the asymptotic scattering boundary condition and define $f(\theta)$, $d\sigma/d\Omega$, and $\sigma_{\rm tot}$ in terms of it. *(Bloom: Remember)*
2. **Explain** how phase shifts $\delta_\ell$ encode the effect of a central potential on each angular-momentum channel, and why an attractive potential gives $\delta_\ell > 0$. *(Bloom: Understand)*
3. **Apply** the partial-wave formulas to compute the total cross-section of a hard sphere at low and high energy, and identify where the factor of four (and the factor of two) comes from. *(Bloom: Apply)*
4. **Derive** the optical theorem from the partial-wave expansion of $\sigma_{\rm tot}$ and $f(0)$. *(Bloom: Analyze)*
5. **Produce** a phase-shift diagram for a spherical square well and read off the scattering length, resonance energies, and Ramsauer-Townsend zeros from it. *(Bloom: Create)*

---

A hard sphere of radius $a$ sits in the lab. A beam of particles — electrons, neutrons, take your pick — streams toward it. Classically, the answer is easy: every particle whose impact parameter is less than $a$ bounces off, every other particle misses, and the total cross-section is $\pi a^2$, the geometric shadow.

Now do it quantum mechanically. The answer is $4\pi a^2$ at low energy — four times the geometric cross-section — and $2\pi a^2$ at high energy, which is *twice* the classical result. Both numbers are wrong from the classical perspective and both are right quantum mechanically, and understanding why is the entire point of this chapter.

The extra factors come from wave behavior: diffraction, interference, the fact that a wave cannot be blocked without scattering in the forward direction. To quantify this we need a systematic framework — the partial-wave expansion — that breaks the problem into angular-momentum channels and assigns each one a single real number, the phase shift. Build that framework once, and every elastic scattering problem in spherical geometry becomes a matter of reading off phase shifts.

---

## The Scattering Amplitude

### The Setup

Work in the center-of-mass frame. A steady beam of particles, energy $E = \hbar^2 k^2 / 2m$, propagates along $\hat{z}$. Far from the scatterer the total wavefunction has the **scattering boundary condition**:

$$\psi(\mathbf{r}) \xrightarrow{r \to \infty} e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r}$$

The first term is the incident plane wave; the second is an outgoing spherical wave with angular modulation $f(\theta)$. We assume azimuthal symmetry (central potential), so there is no $\phi$ dependence. Everything — total cross-section, differential cross-section, forward scattering, resonances — follows from the single complex function $f(\theta)$, which is called the **scattering amplitude**.

The probability current carried by the incident wave is $j_{\rm inc} = \hbar k / m$ (per unit area per unit time). The current scattered into solid angle $d\Omega$ at large $r$ is $j_{\rm sc}\,r^2\,d\Omega = (\hbar k / m)|f(\theta)|^2\,d\Omega$. The ratio defines the **differential cross-section**:

$$\boxed{\frac{d\sigma}{d\Omega} = |f(\theta)|^2}$$

Integrate over all solid angles to get the **total cross-section**:

$$\sigma_{\rm tot} = \int |f(\theta)|^2\,d\Omega = 2\pi\int_0^\pi |f(\theta)|^2 \sin\theta\,d\theta$$

### The Partial-Wave Expansion

For a central potential $V(r)$, angular momentum is conserved and the problem separates. The incident plane wave has the **Rayleigh expansion**:

$$e^{ikz} = \sum_{\ell=0}^\infty (2\ell+1)\,i^\ell\,j_\ell(kr)\,P_\ell(\cos\theta)$$

where $j_\ell(kr)$ are spherical Bessel functions and $P_\ell(\cos\theta)$ are Legendre polynomials. Far from the scatterer, $j_\ell(kr) \to \sin(kr - \ell\pi/2)/kr$. The potential shifts each partial wave by a phase, so the asymptotic radial solution for angular momentum $\ell$ becomes:

$$u_\ell(r) \xrightarrow{r \to \infty} \frac{\sin(kr - \ell\pi/2 + \delta_\ell)}{kr}$$

The real number $\delta_\ell$ is the **phase shift** for the $\ell$-th partial wave. Assembling all partial waves and matching to the scattering boundary condition (the incident wave plus the outgoing spherical wave), the scattering amplitude is:

$$\boxed{f(\theta) = \frac{1}{k}\sum_{\ell=0}^\infty (2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta)}$$

Each partial wave contributes through the combination $e^{i\delta_\ell}\sin\delta_\ell$. It is sometimes written as the **partial-wave amplitude**:

$$f_\ell = \frac{e^{i\delta_\ell}\sin\delta_\ell}{k} = \frac{e^{2i\delta_\ell}-1}{2ik}$$

### The Total Cross-Section from Phase Shifts

Use the orthogonality of Legendre polynomials, $\int_{-1}^{1} P_\ell(x)P_{\ell'}(x)\,dx = 2\delta_{\ell\ell'}/(2\ell+1)$:

$$\sigma_{\rm tot} = 2\pi\int_0^\pi |f(\theta)|^2\sin\theta\,d\theta = \frac{4\pi}{k^2}\sum_{\ell=0}^\infty (2\ell+1)\sin^2\delta_\ell$$

Each partial wave contributes an amount:

$$\sigma_\ell = \frac{4\pi}{k^2}(2\ell+1)\sin^2\delta_\ell$$

The maximum of $\sin^2\delta_\ell$ is 1, so each partial wave is bounded by the **unitarity limit**:

$$\sigma_\ell \leq \frac{4\pi(2\ell+1)}{k^2}$$

This is a purely quantum result: the cross-section per angular-momentum channel cannot exceed $4\pi(2\ell+1)/k^2$. No such bound exists classically.

### Physical Meaning of Phase Shifts

The phase shift $\delta_\ell$ is exactly what the name says: it is the phase by which the potential has shifted the outgoing wave relative to what a free particle would produce. An **attractive** potential pulls the wave in closer to the origin, advancing the phase — $\delta_\ell > 0$. A **repulsive** potential pushes it out — $\delta_\ell < 0$. At the origin, $u_\ell(0) = 0$ always (boundary condition), so the wave must compress or stretch its zero crossings to accommodate the phase shift.

---

## The Optical Theorem

Evaluate $f(\theta)$ at $\theta = 0$. Since $P_\ell(1) = 1$:

$$f(0) = \frac{1}{k}\sum_{\ell=0}^\infty (2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell$$

Take the imaginary part:

$$\operatorname{Im}[f(0)] = \frac{1}{k}\sum_{\ell=0}^\infty (2\ell+1)\sin^2\delta_\ell = \frac{k}{4\pi}\sigma_{\rm tot}$$

Rearranging:

$$\boxed{\sigma_{\rm tot} = \frac{4\pi}{k}\operatorname{Im}[f(0)]}$$

This is the **optical theorem**. It says that the total cross-section equals the imaginary part of the forward scattering amplitude (times $4\pi/k$). The physics behind it: whenever the potential removes probability from the forward beam (by scattering into other directions), the forward-scattered wave must interfere *destructively* with the incident wave to produce a shadow. That destructive interference requires a particular imaginary component in $f(0)$. Total cross-section and forward imaginary amplitude are two faces of the same probability conservation. The optical theorem is a consequence of unitarity and is exact — it holds for inelastic scattering too, where $\sigma_{\rm tot}$ includes all processes.

You can use the optical theorem as a sanity check: compute $\sigma_{\rm tot}$ from the partial-wave sum, then independently compute $\operatorname{Im}[f(0)]$ and verify the relation. If it does not hold, something is wrong with the calculation.

---

## Low-Energy S-Wave Scattering and the Scattering Length

### Why Only $\ell = 0$ Survives at Low Energy

A classical particle with angular momentum $\ell\hbar$ and momentum $\hbar k$ has impact parameter $b = \ell/k$. Only particles that approach within the range $a$ of the potential are affected: the condition $b \lesssim a$ means $\ell \lesssim ka$. At low energy $ka \ll 1$, and only $\ell = 0$ (the s-wave) satisfies this. All higher partial waves have such small phase shifts that they contribute negligibly to the cross-section.

So at low energy, everything reduces to:

$$f(\theta) \approx \frac{e^{i\delta_0}\sin\delta_0}{k}, \qquad \sigma_{\rm tot} \approx \frac{4\pi}{k^2}\sin^2\delta_0$$

And as $k \to 0$, the phase shift itself goes to zero — the potential cannot do much to an infinitely slow particle. The leading behavior is linear: $\delta_0 \to -a_s k$ as $k \to 0$, where $a_s$ is the **scattering length**. (The sign convention: $a_s > 0$ for a repulsive effective interaction, $a_s < 0$ for an attractive one. A positive $a_s$ means the potential has pushed the wave outward — the asymptotic wave appears to come from a hard sphere of radius $a_s$.)

Substituting $\delta_0 \approx -a_s k$:

$$\sigma_{\rm tot} \xrightarrow{k \to 0} \frac{4\pi}{k^2}\sin^2(a_s k) \approx 4\pi a_s^2$$

The **low-energy total cross-section is $4\pi a_s^2$** — independent of energy, and four times the "classical" $\pi a_s^2$. The factor of four is not a mistake. Classically, a disk of radius $a$ presents cross-section $\pi a^2$; quantum mechanically, a spherically symmetric scatterer of characteristic size $a_s$ scatters in all $4\pi$ steradians isotropically and picks up the factor of four from that isotropy.

### The Scattering Length as a Fingerprint

The scattering length is the single most important parameter for low-energy scattering. It can be positive or negative; it can be much larger than the physical range of the potential; and its sign and magnitude carry information about the near-threshold bound-state spectrum.

The connection: if the potential is just deep enough to support a bound state at threshold (binding energy $\to 0$), then $a_s \to +\infty$. Just below threshold — no bound state — $a_s$ is negative and large in magnitude. Just above threshold — one bound state — $a_s$ is positive and large. This is the **Levinson theorem** in its simplest form: the scattering length diverges whenever a new bound state appears at threshold, and its sign flips. The scattering length is the low-energy fingerprint of the bound-state spectrum.

In nuclear physics, the neutron-proton triplet s-wave scattering length is $a_t \approx 5.4$ fm and the singlet is $a_s \approx -23.7$ fm [verify]. The large negative singlet scattering length signals a virtual bound state (the dineutron) sitting just above threshold — not quite bound, but close enough to make $a_s$ large. In ultracold atomic physics, Feshbach resonances allow experimentalists to tune $a_s$ from $-\infty$ to $+\infty$ by adjusting a magnetic field, enabling study of the BCS-BEC crossover.

---

## Resonances

When the potential supports a **quasi-bound state** just above threshold — a state that would be bound if the potential were slightly stronger — the s-wave phase shift passes through $\pi/2$, $\sin^2\delta_0 \to 1$, and the partial cross-section hits the unitarity limit $4\pi/k^2$. This is a **scattering resonance**.

Near a resonance at energy $E_R$, the phase shift has the Breit-Wigner form:

$$\tan\delta_0(k) = \frac{\Gamma/2}{E_R - E}$$

where $\Gamma$ is the **width** of the resonance (in energy). The s-wave cross-section near the resonance is:

$$\sigma_0(E) = \frac{4\pi}{k^2}\cdot\frac{(\Gamma/2)^2}{(E-E_R)^2 + (\Gamma/2)^2}$$

a Breit-Wigner Lorentzian in energy. At $E = E_R$ the cross-section peaks at $4\pi/k_R^2$. Narrow resonances (small $\Gamma$) correspond to long-lived quasi-bound states; wide resonances correspond to weakly trapped states that escape quickly.

The resonance is a scattering analog of a driven oscillator at resonance: the cross-section peaks when the energy of the incoming particle matches the natural frequency of a quasi-stationary state inside the potential. This picture underlies compound-nucleus resonances in nuclear physics, Feshbach resonances in cold atoms, and shape resonances in molecular scattering.

---

## Worked Example: Hard-Sphere s-Wave Scattering

### The Lesson

**Setup.** The hard-sphere potential: $V(r) = \infty$ for $r < a$, $V(r) = 0$ for $r \geq a$. The boundary condition is $\psi(a) = 0$.

**Exact phase shift.** For the s-wave ($\ell = 0$), the radial equation outside the sphere is free-particle:

$$u_0''(r) + k^2 u_0(r) = 0, \qquad r > a$$

The general solution is $u_0(r) = A\sin(kr + \delta_0)$. Applying $u_0(a) = 0$:

$$\sin(ka + \delta_0) = 0 \implies ka + \delta_0 = n\pi$$

Taking $n = 0$ (the physical branch for small $ka$):

$$\boxed{\delta_0 = -ka}$$

This is exact for all $k$, not just small $k$. The phase shift is negative (repulsive potential) and grows linearly with momentum.

**The differential cross-section** (s-wave only, valid for $ka \ll 1$):

$$\frac{d\sigma}{d\Omega}\bigg|_{\ell=0} = |f_0|^2 = \frac{\sin^2\delta_0}{k^2} = \frac{\sin^2(ka)}{k^2}$$

At low energy ($ka \ll 1$): $\sin(ka) \approx ka$, so $d\sigma/d\Omega \approx a^2$ — isotropic. Integrating over $4\pi$ steradians:

$$\sigma_{\rm tot} \approx 4\pi a^2 \qquad (ka \ll 1)$$

Four times the geometric cross-section. The scattering is isotropic and much larger than classical.

### The Limit

**High energy ($ka \gg 1$).** Now many partial waves contribute — up to $\ell_{\rm max} \approx ka$. For the hard sphere, the exact phase shift for general $\ell$ is:

$$\delta_\ell = -\arctan\!\left(\frac{j_\ell(ka)}{n_\ell(ka)}\right)$$

where $j_\ell$ and $n_\ell$ are spherical Bessel and Neumann functions. At high energy, summing over all contributing partial waves and using $\langle\sin^2\delta_\ell\rangle \to 1/2$ (the phase shifts oscillate rapidly and average to $1/2$ over the occupied channels):

$$\sigma_{\rm tot} \approx \frac{4\pi}{k^2}\cdot\sum_{\ell=0}^{ka}(2\ell+1)\cdot\frac{1}{2} \approx \frac{4\pi}{k^2}\cdot\frac{(ka)^2}{2}\cdot\frac{1}{2}\cdot 2 = 2\pi a^2$$

$$\boxed{\sigma_{\rm tot} \approx 2\pi a^2 \qquad (ka \gg 1)}$$

Twice the geometric cross-section, not once. Where does the extra $\pi a^2$ come from?

**The diffractive shadow.** In the geometric optics limit you might expect the sphere to cast a shadow of area $\pi a^2$ with no additional scattering. But blocking the beam requires the forward-scattered wave to destructively interfere with the incident wave to create the shadow. That forward-scattered wave carries probability — it contributes exactly $\pi a^2$ to the total cross-section on top of the "real" scattering contribution of $\pi a^2$. The shadow requires scattering, and the scattering that makes the shadow counts just as much as the scattering that deflects particles to the side. This is the quantum-mechanical version of Babinet's principle and the Poisson-Arago bright spot: you cannot have a shadow without diffraction.

### Square-Well Phase Shifts (Sketch)

For a finite spherical square well of depth $V_0$ and radius $a$, the interior wave vector is $\kappa = \sqrt{k^2 + 2mV_0/\hbar^2}$. Matching the logarithmic derivative of $u_0 = \sin(\kappa r)$ at $r = a$ to the exterior solution $A\sin(kr + \delta_0)$:

$$\tan(ka + \delta_0) = \frac{k}{\kappa}\tan(\kappa a)$$

Solving for $\delta_0$:

$$\delta_0 = \arctan\!\left(\frac{k}{\kappa}\tan(\kappa a)\right) - ka$$

The scattering length follows by taking $k \to 0$, $\kappa \to \kappa_0 = \sqrt{2mV_0/\hbar^2}$:

$$a_s = a\!\left[1 - \frac{\tan(\kappa_0 a)}{\kappa_0 a}\right]$$

When $\kappa_0 a = (n + 1/2)\pi$ (odd multiples of $\pi/2$), $\tan(\kappa_0 a) \to \infty$ and $a_s \to a$ — but more interestingly, the resonance condition $\kappa_0 a = \pi/2$ corresponds to the minimum potential depth needed for a bound state. Right at that threshold, $a_s \to +\infty$. The zero-energy cross-section diverges. The wave can barely distinguish the potential well from a true bound state.

---

## Common Misconceptions

**"The scattering length equals the range of the potential."** Not true. The scattering length $a_s$ is defined by $\delta_0(k) \to -a_s k$ as $k \to 0$; it is a property of the low-energy S-matrix, not a property of how far the potential extends. Near a resonance, $|a_s| \gg a$ (the range). For the Ramsauer-Townsend effect in noble gases (electron scattering at $\sim 1$ eV), multiple partial-wave phase shifts nearly cancel and $a_s$ is anomalously small. The range and the scattering length are different objects.

**"Attractive potentials always increase the cross-section."** A very deep attractive well can push $\delta_0$ past $\pi/2$ and back down, producing a small cross-section (the Ramsauer-Townsend zero). The cross-section vanishes when $\delta_0 = n\pi$. An extremely deep well can have the same low-energy cross-section as no well at all — the phase shift has wrapped around $\pi$ and the $\sin^2\delta_0$ factor is back to zero.

**"At high energy, the total cross-section equals the geometric cross-section $\pi a^2$."** The answer is $2\pi a^2$. The extra $\pi a^2$ is diffractive forward scattering. Every textbook derivation of the geometric optics limit that ignores diffraction gets this wrong. The optical theorem tells you the forward amplitude is nonzero even when the scattering angle is exactly zero, and that contribution counts.

**"The phase shift uniquely determines the potential."** The inverse scattering problem — recovering $V(r)$ from $\{\delta_\ell(k)\}$ — is genuinely hard and not always unique. The phase shifts at a fixed energy give less information than phase shifts as a function of energy. The Gel'fand-Levitan-Marchenko method solves a specific version of the inverse problem but requires data over all energies.

**"The $\ell=0$ channel dominates at all energies."** Only at low energy. At energy $E$, the maximum contributing angular momentum is $\ell_{\rm max} \approx ka$. For nuclear scattering at tens of MeV, $ka \sim 10$–$100$ and many partial waves contribute. The s-wave approximation breaks down sharply above $\sim \hbar^2/(2ma^2)$.

---

## Exercises

**7.1** (Remember) Write down the scattering boundary condition $\psi(\mathbf{r}) \xrightarrow{r\to\infty}$ and identify: the incident plane wave, the outgoing spherical wave, the scattering amplitude $f(\theta)$. Then write the definitions of $d\sigma/d\Omega$ and $\sigma_{\rm tot}$ in terms of $f(\theta)$. No derivation needed — just the definitions, stated cleanly.

**7.2** (Understand) Explain in two paragraphs, without equations, why a hard sphere scatters four times its geometric cross-section at low energy. Your explanation should mention: isotropy of s-wave scattering, the distinction between geometric and wave-mechanical cross-sections, and why the classical picture fails. Then explain why the high-energy result is $2\pi a^2$ rather than $\pi a^2$, using the word "shadow."

**7.3** (Apply) Verify the optical theorem for hard-sphere s-wave scattering at low energy. (a) Compute $\sigma_{\rm tot}$ from the partial-wave sum, keeping only $\ell = 0$ with $\delta_0 = -ka$, $ka \ll 1$. (b) Compute $f(0)$ from the scattering amplitude formula, again s-wave only. (c) Show that $\sigma_{\rm tot} = (4\pi/k)\,\operatorname{Im}[f(0)]$. *(Why can you trust a formula when it checks out on a simple example? Because if the math is right for the hard sphere, the same algebra that proved the optical theorem in general must be correct.)*

**7.4** (Apply) The spherical square well with depth $V_0 = \hbar^2\pi^2/(8ma^2)$ (the minimum depth for one bound state). (a) Compute $\kappa_0 a$. (b) Using the formula $a_s = a[1 - \tan(\kappa_0 a)/(\kappa_0 a)]$, evaluate the scattering length. You should find $a_s \to \pm\infty$. (c) What does the diverging scattering length tell you about the cross-section near this potential depth? Sketch $\sigma_{\rm tot}(V_0)$ near threshold.

**7.5** (Apply, Analyze) For the spherical square well, the s-wave phase shift is $\delta_0 = \arctan[(k/\kappa)\tan(\kappa a)] - ka$. Numerically (take $a = 1$, $\hbar = 2m = 1$, so energies are in natural units): (a) Plot $\delta_0(k)$ for $V_0 = 1.0, 5.0, 10.0$ (in units where $\hbar^2/2ma^2 = 1$). (b) Locate the resonance energies (where $\delta_0 = \pi/2 + n\pi$) and verify they correspond to peaks in $\sigma_{\rm tot}(k)$. (c) Locate any Ramsauer-Townsend zeros ($\delta_0 = n\pi$, $n \neq 0$) in the deeper wells.

**7.6** (Analyze) Prove, from the partial-wave expansion of $\sigma_{\rm tot}$ and $f(0)$, the optical theorem in full generality (not just s-wave). Your proof should use only the orthogonality of Legendre polynomials and elementary algebra. At what step does $P_\ell(1) = 1$ enter?

**7.7** (Apply, Produce) The Levinson theorem states that $\delta_\ell(0) - \delta_\ell(\infty) = n_\ell\pi$, where $n_\ell$ is the number of bound states in the $\ell$-th angular-momentum channel. (a) For the hard sphere, what is $\delta_0(k)$ at $k \to 0$ and $k \to \infty$? (b) How many bound states does the hard sphere have in the $\ell = 0$ channel? Does this match the Levinson theorem? (c) For a square well deep enough to have exactly two $\ell = 0$ bound states, what must be true about $\delta_0(k \to 0)$? Sketch $\delta_0(k)$ schematically.

---

## Still Puzzling

**Efimov physics.** When the two-body scattering length is large ($|a_s| \gg$ range), three-body bound states appear at a geometric series of binding energies: $E_{n+1}/E_n = e^{-2\pi/s_0}$ where $s_0 \approx 1.00624$. This was predicted by Vitaly Efimov in 1970 [verify] and first observed experimentally in ultracold cesium in 2006 [verify]. It is a universal consequence of large s-wave scattering length and has nothing to do with the specific potential — only the scattering length matters. The factor $e^{-2\pi/s_0} \approx 1/515$; the Efimov states appear in a sequence of binding energies spanning several orders of magnitude. The analysis goes beyond partial-wave methods and requires renormalization-group ideas applied to three-body quantum mechanics. It is one of the stranger corners of low-energy quantum physics.

**The inverse scattering problem.** Given $\{\delta_\ell(k)\}$ for all $\ell$ and all $k$, can you reconstruct $V(r)$? The Gel'fand-Levitan-Marchenko theorem says yes, under certain conditions, and gives an integral equation for the potential. But the inverse problem is deeply nonlinear, the data required is infinite in principle, and the uniqueness theorem requires phase shifts over the full range $0 < k < \infty$. In practice, experimenters measure cross-sections (not amplitudes, so they lose phase information) at finite energy ranges. Phase shifts must be inferred by fitting models, and the solution is not unique. The connection between scattering data and the underlying potential is less clean than the forward problem.

**The S-matrix pole picture of resonances.** The Breit-Wigner formula emerges naturally from the assumption that the S-matrix element $S_\ell(k) = e^{2i\delta_\ell}$ has a pole in the complex $k$-plane at $k = k_R - i\Gamma/(2v)$. Bound states correspond to poles on the positive imaginary axis. Resonances correspond to poles in the lower half of the complex $k$-plane, close to the real axis. Virtual bound states (like the dineutron) correspond to poles on the negative imaginary axis. The scattering length as $k \to 0$, the resonance width, and the bound-state binding energy are all controlled by where the S-matrix poles sit in the complex $k$-plane. This is the beginning of analytic S-matrix theory, which connects scattering in quantum mechanics to dispersion relations in quantum field theory.

---

## The +1 — Simulation Exercise

Your deliverable is `07-partial-waves.html` in your working directory: a single-file D3 simulation of phase-shifted s-wave scattering from a spherical square well.

### Part 1 — Update `PROJECT.md`

```
Append to PROJECT.md:

Chapter 07 — Scattering I: Partial Waves
Deliverable: 07-partial-waves.html
Status: in progress

The simulation has two panels:

LEFT PANEL — Phase-shifted wavefunction.
Horizontal axis: r from 0 to 8a (in units of the well radius a).
Two overlaid curves:
  - Free radial wave u_free(r) = A sin(kr) (dashed gray)
  - Actual radial wave u_0(r) = A sin(kr + delta_0) for r > a, with the
    interior matched solution A_in sin(kappa*r) for r < a (solid blue)
The interior region (0 to a) is shaded light yellow.
Show the phase shift delta_0 as a horizontal arrow between the two wave
crests immediately to the right of r = a.
Mark the classical turning point at r = a with a vertical dashed line.

RIGHT PANEL — Cross-section vs. energy.
Horizontal axis: k*a from 0 to 6 (dimensionless).
Three curves:
  - sigma_tot / (pi*a^2) (solid black) — total s-wave cross-section in
    units of the geometric cross-section
  - The unitarity bound 4/((ka)^2) (dashed red)
  - The classical result 1 (dotted gray horizontal line)
Mark resonance peaks (sigma hits the unitarity bound) with small red
triangles on the x-axis.
Mark Ramsauer-Townsend zeros with small blue circles on the x-axis.

CONTROLS
- Slider: V_0 * (2ma^2/hbar^2), range 0 to 25, label "Well depth V_0"
  (in units where hbar^2/2ma^2 = 1)
- Slider: k*a, range 0.01 to 6, label "Incident momentum ka"
- Display panel: show delta_0, sin^2(delta_0), and sigma_tot / (pi*a^2)
  as live numerical readouts in the top-right corner.

As V_0 increases past pi^2/4, pi^2, 9*pi^2/4 ..., a new bound state
appears and the scattering length diverges. Show a vertical red band in
the cross-section plot centered at these threshold V_0 values when the
V_0 slider is near them (within ±0.5 units).
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md:

SCATTERING PARTIAL-WAVE PHYSICS RULES (Chapter 07)

1. S-WAVE PHASE SHIFT for a spherical square well of depth V_0 and radius a:
   kappa = sqrt(k^2 + 2*m*V_0 / hbar^2)
   In natural units (hbar = 2m = 1, a = 1): kappa = sqrt(k^2 + V_0)
   delta_0 = arctan( (k/kappa) * tan(kappa) ) - k
   (Here the "- k" means "- k*a" with a=1 in natural units.)
   This is exact. Do NOT approximate delta_0 = -k for the square well;
   that approximation is only valid for the hard sphere.

2. S-WAVE CROSS-SECTION:
   sigma_s = (4*pi / k^2) * sin^2(delta_0)
   In the display, normalize to pi*a^2: sigma_s / (pi * 1^2) = 4*sin^2(delta_0) / k^2

3. SCATTERING LENGTH:
   a_s = 1 - tan(sqrt(V_0)) / sqrt(V_0)
   (with a=1 and natural units as above; kappa_0 = sqrt(V_0) at k=0)
   When V_0 = (pi/2)^2, (3pi/2)^2, ..., a_s diverges (new bound state).

4. RESONANCES occur when sin^2(delta_0) = 1, i.e., delta_0 = pi/2 + n*pi.
   Detect numerically: find k values where |sin(delta_0) - 1| < 0.01 for
   a given V_0.

5. RAMSAUER-TOWNSEND ZEROS occur when delta_0 = n*pi (n != 0).
   Detect numerically: find k values where |sin(delta_0)| < 0.01.

6. INTERIOR SOLUTION for 0 < r < a (in natural units, a=1):
   u_in(r) = B * sin(kappa * r)
   Normalize so that u_in and u_out match at r = a:
   B = sin(k + delta_0) / sin(kappa)

7. SIGN CONVENTION. delta_0 < 0 for repulsive (hard sphere). delta_0 > 0
   for attractive well at low energy. As k -> 0, delta_0 -> -a_s * k.

KNOWN FAILURE MODES:
(a) arctan returns values in [-pi/2, pi/2]; delta_0 may need correction
    by + n*pi to be in a continuously varying branch. Track the branch by
    monitoring delta_0 continuity as k increases.
(b) At resonance, kappa*a = pi/2 + n*pi and tan(kappa*a) -> inf.
    This causes arctan to jump. Handle by checking for tan(kappa) > 1e6
    and setting delta_0 = pi/2 + pi*branch_count - k directly.
(c) The well-depth threshold for the first bound state is V_0 = (pi/2)^2
    in natural units. Below this, no bound state; the scattering length
    is negative. At threshold, scattering length diverges. Above threshold,
    scattering length is positive.
```

### Part 3 — The simulation prompt

```
Read CLAUDE.md, DESIGN.md, and PROJECT.md first.

Build 07-partial-waves.html: a single self-contained HTML file using D3 v7
from CDN and d3-simple-slider. No other dependencies.

LAYOUT: Two SVG panels side by side, 550x450 each, inside a 1150x500 container.

LEFT PANEL — Radial wavefunction.
x-axis: r from 0 to 8 (in natural units, a=1). y-axis: u(r) from -1.5 to 1.5.
Plot two lines:
  Line 1 (dashed gray): u_free(r) = sin(k*r) for all r (amplitude = 1, no normalization)
  Line 2 (solid blue): interior = sin(kappa*r) * B for 0 < r < 1;
                        exterior = sin(k*r + delta_0) for r > 1
  (B computed per CLAUDE.md rule 6)
Shade the interior (r < 1) with a light yellow rectangle.
Draw a vertical dashed red line at r = 1 (the well boundary).
Below the plot, add text: "δ₀ = [value] rad" and "aₛ = [value]" (both live).
Animate smoothly: when sliders move, transition both curves in 200ms.

RIGHT PANEL — σ vs. k*a.
x-axis: k*a from 0.01 to 6. y-axis: σ_tot / πa² from 0 to 8.
Plot three curves:
  Solid black: 4*sin²(δ₀(k)) / k² (s-wave sigma, normalized)
  Dashed red: 4/k² (unitarity bound)
  Dotted gray: y=1 (classical result)
Add a vertical orange line at the current k*a (from the left slider).
Add red triangle markers at resonance k values (rule 4).
Add blue circle markers at Ramsauer-Townsend k values (rule 5).
These markers update when V_0 changes. Compute them by scanning k from
0.01 to 6 in 500 steps.

CONTROLS (below the two panels):
  Slider 1: V_0, range 0 to 25, step 0.05, default 5.0, label "Well depth V₀ (units of ℏ²/2ma²)"
  Slider 2: k*a, range 0.01 to 6, step 0.01, default 1.0, label "Incident momentum k·a"
  Numerical display: delta_0, sin²(delta_0), sigma_tot/pi, a_s — all live.

SANITY CHECKS (to browser console on load and on each slider change):
  - At V_0 = 0, delta_0 should be 0 for all k. Log "PASS: delta_0(V_0=0) = [val]".
  - At V_0 = (pi/2)^2 = 2.467, a_s should diverge. Log a_s value.
  - Optical theorem check: sigma_tot = (4*pi/k) * Im[f(0)].
    f(0) = exp(i*delta_0)*sin(delta_0)/k. Im[f(0)] = sin^2(delta_0)/k.
    So (4*pi/k) * sin^2(delta_0)/k = 4*pi*sin^2(delta_0)/k^2.
    This should equal sigma_s. Log "Optical theorem check: [value] vs [value]".

Comments at every physics step. Pure functions for delta_0 and sigma.
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. Set $V_0 = 5.0$ (natural units). Slide $ka$ from 0.1 to 6. At what value of $ka$ is the first resonance? (Look for the cross-section spike to the unitarity bound.) At what $ka$ is the first Ramsauer-Townsend zero?

2. Increase $V_0$ past $(π/2)^2 \approx 2.47$. Watch the scattering length (displayed below the left panel) diverge and change sign. Before this threshold, is $a_s$ positive or negative? After? What does this tell you about the bound-state spectrum?

3. Set $V_0 = 10$. Observe the wavefunction in the left panel at the first resonance energy. Qualitatively, what does the interior wave look like compared to the exterior? (Hint: the phase shift is $\pi/2$ — where is the interior amplitude relative to the exterior?)

4. Optical theorem: at any $V_0$ and $ka$, verify in the console output that $\sigma_{\rm tot} = (4\pi/k)\,\operatorname{Im}[f(0)]$. This is always exact. The simulation checks it; your job is to confirm the console output is "PASS."

**Extension prompt:**

```
Modify 07-partial-waves.html to add an ell=1 (p-wave) channel. The p-wave
phase shift for the square well is given by matching the ell=1 spherical
Bessel function j_1(kappa*r) inside to the exterior combination
j_1(kr)*cos(delta_1) - n_1(kr)*sin(delta_1). The exact result for delta_1
is (see Fitzpatrick §14.5):

  tan(delta_1) = [k*j_1(kappa*a)*j_1'(ka) - kappa*j_1'(kappa*a)*j_1(ka)]
                 / [kappa*j_1'(kappa*a)*n_1(ka) - k*j_1(kappa*a)*n_1'(ka)]

where j_1(x) = sin(x)/x^2 - cos(x)/x, n_1(x) = -cos(x)/x^2 - sin(x)/x.
Add a toggle "include p-wave" that adds the ell=1 contribution to sigma_tot.
Show how the cross-section changes when p-wave is included, especially at
higher energies. Update PROJECT.md to mark Chapter 07 complete.
```

---

## References

1. Fitzpatrick, R., *Introductory Quantum Mechanics* (LibreTexts / UT Austin), Ch. 14, §§14.1–14.8 [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory]. CC BY-NC-SA 4.0. Primary source for all partial-wave formulas in this chapter. [verify URL active]

2. Griffiths, D. J. & Schroeter, D. F., *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge, 2018), Ch. 11. Standard undergraduate treatment; the notation $f_\ell = e^{i\delta_\ell}\sin\delta_\ell/k$ follows Griffiths. [verify edition]

3. Murayama, H., *Physics 221B Lecture Notes, Scattering Theory*, §§1–3 (UC Berkeley, 2022) [http://hitoshi.berkeley.edu/221B/scattering3.pdf]. Derives the Rayleigh expansion and hard-sphere phase shifts explicitly; clean and graduate-level. [verify URL active]

4. Liboff, R. L., *Introductory Quantum Mechanics*, 4th ed. (Addison-Wesley, 2003), Ch. 14. Local pantry source; Table of Contents confirms §14.3 (Partial-Wave Analysis). [verify edition]

5. Sakurai, J. J. & Napolitano, J., *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2020), Ch. 6. S-matrix language and formal scattering theory. [verify edition]

6. Efimov, V., "Energy levels arising from resonant two-body forces in a three-body system," *Physics Letters B* **33**, 563–564 (1970). Original prediction of the geometric spectrum of three-body states near unitarity. [verify]

7. Kraemer, T., et al., "Evidence for Efimov quantum states in an ultracold gas of caesium atoms," *Nature* **440**, 315–318 (2006). First experimental observation of Efimov states. [verify]
