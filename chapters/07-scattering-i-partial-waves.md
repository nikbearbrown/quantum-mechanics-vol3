# Chapter 7 — Scattering I: Partial Waves

A hard sphere of radius $a$ sits in the lab. A beam of particles streams toward it. Classically, the answer is easy: every particle with impact parameter less than $a$ bounces off, every other misses, and the total cross-section is $\pi a^2$ — the geometric shadow.

Now do it quantum mechanically. The answer at low energy is $4\pi a^2$ — four times the geometric cross-section. At high energy it is $2\pi a^2$ — twice the classical result. Both numbers are wrong from a classical perspective and both are right quantum mechanically. Understanding why is the entire point of this chapter.

The extra factors come from wave behavior: diffraction, interference, the fact that a wave cannot be blocked without scattering in the forward direction. To quantify this requires a framework — the partial-wave expansion — that breaks the problem into angular-momentum channels and assigns each one a single real number, the phase shift. Build that framework once and every elastic scattering problem in spherical geometry reduces to reading off phase shifts.

---

## The Scattering Amplitude

Work in the center-of-mass frame. A steady beam with energy $E = \hbar^2 k^2/2m$ propagates along $\hat{z}$. Far from the scatterer, the total wave function has the **scattering boundary condition**:

$$\psi(\mathbf{r}) \xrightarrow{r\to\infty} e^{ikz} + f(\theta)\,\frac{e^{ikr}}{r}.$$

The first term is the incident plane wave; the second is an outgoing spherical wave with angular modulation $f(\theta)$. We assume azimuthal symmetry (central potential), so there is no $\phi$ dependence. Everything — total cross-section, differential cross-section, resonances — follows from the single complex function $f(\theta)$, the **scattering amplitude**.

The probability current in the incident wave is $j_\text{inc} = \hbar k/m$. The current scattered into solid angle $d\Omega$ is proportional to $|f(\theta)|^2$. The ratio defines the **differential cross-section**:

$$\frac{d\sigma}{d\Omega} = |f(\theta)|^2.$$

Integrate over all solid angles for the **total cross-section**:

$$\sigma_\text{tot} = \int|f(\theta)|^2\,d\Omega = 2\pi\int_0^\pi|f(\theta)|^2\sin\theta\,d\theta.$$

---

## The Partial-Wave Expansion

For a central potential, angular momentum is conserved and the problem separates. The incident plane wave has the Rayleigh expansion:

$$e^{ikz} = \sum_{\ell=0}^\infty(2\ell+1)\,i^\ell\,j_\ell(kr)\,P_\ell(\cos\theta).$$

Far from the scatterer, spherical Bessel functions go as $j_\ell(kr) \to \sin(kr - \ell\pi/2)/kr$. The potential shifts each partial wave by a phase, so the asymptotic radial solution for angular momentum $\ell$ becomes:

$$u_\ell(r) \xrightarrow{r\to\infty} \frac{\sin(kr - \ell\pi/2 + \delta_\ell)}{kr}.$$

The real number $\delta_\ell$ is the **phase shift** for the $\ell$-th partial wave. Assembling all partial waves and matching to the boundary condition, the scattering amplitude is:

$$\boxed{f(\theta) = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta).}$$

Using the orthogonality of Legendre polynomials, the total cross-section becomes:

$$\sigma_\text{tot} = \frac{4\pi}{k^2}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell.$$

Each partial wave contributes $\sigma_\ell = (4\pi/k^2)(2\ell+1)\sin^2\delta_\ell$, bounded by the **unitarity limit** $4\pi(2\ell+1)/k^2$. No such bound exists classically.

The phase shift has a direct physical meaning: it is the phase by which the potential has shifted the outgoing wave relative to a free particle. An attractive potential pulls the wave closer to the origin, advancing the phase — $\delta_\ell > 0$. A repulsive potential pushes it out — $\delta_\ell < 0$.

---

## The Optical Theorem

Evaluate $f(\theta)$ at $\theta = 0$, using $P_\ell(1) = 1$:

$$f(0) = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\,e^{i\delta_\ell}\sin\delta_\ell.$$

Take the imaginary part:

$$\operatorname{Im}[f(0)] = \frac{1}{k}\sum_{\ell=0}^\infty(2\ell+1)\sin^2\delta_\ell = \frac{k}{4\pi}\sigma_\text{tot}.$$

Rearranging:

$$\boxed{\sigma_\text{tot} = \frac{4\pi}{k}\,\operatorname{Im}[f(0)].}$$

This is the **optical theorem**. It says that the total cross-section equals the imaginary part of the forward scattering amplitude (times $4\pi/k$). The physics: whenever the potential removes probability from the forward beam by scattering to other directions, the forward-scattered wave must interfere destructively with the incident wave to produce a shadow. That destructive interference requires a specific imaginary component in $f(0)$. The optical theorem is a consequence of unitarity — it holds for inelastic scattering too, where $\sigma_\text{tot}$ includes every process.

Use it as a sanity check: compute $\sigma_\text{tot}$ from the partial-wave sum, independently compute $\operatorname{Im}[f(0)]$, and verify the relation. If it fails, something is wrong.

---

## Low-Energy Scattering and the Scattering Length

A classical particle with angular momentum $\ell\hbar$ and momentum $\hbar k$ has impact parameter $b = \ell/k$. Only particles approaching within the range $a$ of the potential are affected: $b \lesssim a$ means $\ell \lesssim ka$. At low energy $ka \ll 1$, only $\ell = 0$ survives. Everything reduces to:

$$f(\theta) \approx \frac{e^{i\delta_0}\sin\delta_0}{k}, \qquad \sigma_\text{tot} \approx \frac{4\pi}{k^2}\sin^2\delta_0.$$

As $k \to 0$, the phase shift goes to zero linearly: $\delta_0 \to -a_s k$, where $a_s$ is the **scattering length**. Then:

$$\sigma_\text{tot} \xrightarrow{k\to 0} \frac{4\pi}{k^2}\sin^2(a_s k) \approx 4\pi a_s^2.$$

The low-energy total cross-section is $4\pi a_s^2$ — independent of energy, and four times the "classical" $\pi a_s^2$. The factor of four is not a mistake. A spherically symmetric scatterer of characteristic size $a_s$ scatters isotropically into all $4\pi$ steradians; that isotropy produces the factor of four.

The scattering length is the low-energy fingerprint of the bound-state spectrum. If the potential is just deep enough to support a bound state at threshold (binding energy $\to 0$), then $a_s \to +\infty$. Just below threshold $a_s$ is large and negative; just above, large and positive. This is the Levinson theorem in its simplest form: the scattering length diverges whenever a new bound state appears at threshold, and its sign flips. In nuclear physics, the neutron-proton triplet s-wave scattering length is $a_t \approx 5.4$ fm and the singlet is $a_s \approx -23.7$ fm [verify] — the large negative singlet value signals a virtual bound state (the dineutron) sitting just above threshold. In ultracold atomic physics, Feshbach resonances allow the scattering length to be tuned from $-\infty$ to $+\infty$ by adjusting a magnetic field.

---

## Resonances

When the potential supports a quasi-bound state just above threshold, the s-wave phase shift passes through $\pi/2$, $\sin^2\delta_0 \to 1$, and the partial cross-section hits the unitarity limit $4\pi/k^2$. This is a **scattering resonance**.

Near a resonance at energy $E_R$, the phase shift has the Breit-Wigner form:

$$\tan\delta_0(k) = \frac{\Gamma/2}{E_R - E},$$

where $\Gamma$ is the width of the resonance. The s-wave cross-section near the resonance is a Breit-Wigner Lorentzian in energy, peaking at $4\pi/k_R^2$ at $E = E_R$. Narrow resonances correspond to long-lived quasi-bound states; wide resonances to weakly-trapped states that escape quickly. The resonance is a scattering analog of a driven oscillator: the cross-section peaks when the incoming energy matches a natural frequency of a quasi-stationary state inside the potential.

---

## Worked Example — Hard-Sphere Scattering at Low and High Energy

**Setup.** Hard-sphere potential: $V = \infty$ for $r < a$, $V = 0$ for $r \geq a$. Boundary condition: $\psi(a) = 0$.

**Exact s-wave phase shift.** The radial equation outside the sphere is free-particle: $u_0'' + k^2 u_0 = 0$. The general solution is $u_0(r) = A\sin(kr + \delta_0)$. The boundary condition $u_0(a) = 0$ requires $\sin(ka + \delta_0) = 0$, giving:

$$\delta_0 = -ka.$$

This is exact for all $k$. The phase shift is negative (repulsive) and grows linearly with momentum.

**Low-energy cross-section.** With $\delta_0 = -ka$ and $ka \ll 1$: $\sin(ka) \approx ka$, so:

$$\frac{d\sigma}{d\Omega} \approx a^2 \quad\text{(isotropic)}, \qquad \sigma_\text{tot} \approx 4\pi a^2.$$

Four times the geometric cross-section. The scattering is isotropic — a purely quantum-mechanical result. The classical answer $\pi a^2$ (a disk) is wrong by a factor of four because the classical picture assumes particles travel in straight lines. The quantum wave diffracts around the sphere and scatters in all directions equally at low energy.

**High-energy cross-section.** At $ka \gg 1$, many partial waves contribute — up to $\ell_\text{max} \approx ka$. The exact phase shifts $\delta_\ell$ for the hard sphere oscillate rapidly over the occupied channels and average $\langle\sin^2\delta_\ell\rangle \to 1/2$. Summing:

$$\sigma_\text{tot} \approx \frac{4\pi}{k^2}\sum_{\ell=0}^{ka}(2\ell+1)\cdot\frac{1}{2} \approx 2\pi a^2.$$

Twice the geometric cross-section. The extra $\pi a^2$ is diffractive: blocking the beam requires the forward-scattered wave to destructively interfere with the incident wave to create a shadow. That forward-scattered wave carries probability — it contributes $\pi a^2$ to the total on top of the $\pi a^2$ from sideways scattering. A shadow requires scattering, and the scattering that makes the shadow counts just as much as the scattering that deflects particles to the side. This is the quantum version of Babinet's principle.

**Square-well phase shift for reference.** For a finite spherical square well of depth $V_0$ and radius $a$, the interior wave vector is $\kappa = \sqrt{k^2 + 2mV_0/\hbar^2}$. Matching the logarithmic derivative at $r = a$:

$$\delta_0 = \arctan\!\left(\frac{k}{\kappa}\tan(\kappa a)\right) - ka.$$

The scattering length at $k \to 0$:

$$a_s = a\!\left[1 - \frac{\tan(\kappa_0 a)}{\kappa_0 a}\right], \qquad \kappa_0 = \sqrt{2mV_0/\hbar^2}.$$

When $\kappa_0 a = (n + 1/2)\pi$, $\tan(\kappa_0 a) \to \infty$ and $a_s \to \pm\infty$ — a new bound state appears at threshold, the cross-section diverges, and the wave can barely distinguish the potential from a true bound state.

---

## Still Puzzling

**Efimov physics.** When the two-body scattering length is large ($|a_s| \gg$ range), three-body bound states appear at a geometric series of binding energies: $E_{n+1}/E_n = e^{-2\pi/s_0}$ where $s_0 \approx 1.00624$, so adjacent states differ by a factor of roughly $1/515$. Predicted by Vitaly Efimov in 1970 [verify] and first observed in ultracold cesium in 2006 [verify], this spectrum is universal — it depends only on the scattering length, not on the specific potential. It is one of the stranger corners of low-energy quantum physics, requiring renormalization-group ideas applied to three-body quantum mechanics.

**The inverse scattering problem.** Given $\{\delta_\ell(k)\}$ for all $\ell$ and all $k$, can you reconstruct $V(r)$? The Gel'fand-Levitan-Marchenko theorem says yes under certain conditions, giving an integral equation for the potential. But the problem requires phase shifts over the full range $0 < k < \infty$, while experiments measure cross-sections (squared amplitudes, losing phase information) at finite energy ranges. The connection between data and potential is less clean than the forward problem.

**The S-matrix pole picture.** The Breit-Wigner formula emerges naturally from the assumption that the S-matrix element $S_\ell(k) = e^{2i\delta_\ell}$ has a pole in the complex $k$-plane. Bound states correspond to poles on the positive imaginary axis. Resonances are poles in the lower half-plane close to the real axis. Virtual bound states like the dineutron sit on the negative imaginary axis. The scattering length, resonance width, and bound-state binding energy are all controlled by where these poles sit — the beginning of analytic S-matrix theory.

---

## The +1 — Simulation Exercise

The deliverable is `07-partial-waves.html`: a D3 simulation of phase-shifted s-wave scattering from a spherical square well with two panels — the radial wave function and the cross-section versus energy.

### `PROJECT.md` Update

````
Append to PROJECT.md:

Chapter 07 — Scattering I: Partial Waves
Deliverable: 07-partial-waves.html
Status: in progress

LEFT PANEL — Phase-shifted wavefunction.
r from 0 to 8a. Two curves: u_free(r) = sin(kr) (dashed gray) and actual
u_0(r) (solid blue, interior matched inside r=a). Interior shaded yellow.
Phase-shift arrow between the two wave crests at r > a.

RIGHT PANEL — Cross-section vs. energy.
k*a from 0 to 6. sigma_tot/pi*a^2 (solid black), unitarity bound 4/(ka)^2
(dashed red), classical result = 1 (dotted gray). Resonance markers (red
triangles), Ramsauer-Townsend zeros (blue circles).
````

### `CLAUDE.md` Amendment

````markdown
## Chapter 07 — Scattering Partial-Wave Physics Rules

1. S-WAVE PHASE SHIFT for spherical square well (natural units hbar=2m=1, a=1):
   kappa = sqrt(k^2 + V_0)
   delta_0 = arctan( (k/kappa) * tan(kappa) ) - k
   Do NOT use delta_0 = -k (hard sphere); this is the exact well result.

2. S-WAVE CROSS-SECTION:
   sigma_s = (4*pi / k^2) * sin^2(delta_0)
   Normalized: sigma_s / (pi * a^2) = 4 * sin^2(delta_0) / k^2

3. SCATTERING LENGTH: a_s = 1 - tan(sqrt(V_0)) / sqrt(V_0)
   Diverges when V_0 = (pi/2)^2, (3pi/2)^2, ... (new bound state at threshold).

4. RESONANCES: delta_0 = pi/2 + n*pi. Detect: |sin(delta_0) - 1| < 0.01.

5. RAMSAUER-TOWNSEND ZEROS: delta_0 = n*pi (n != 0). Detect: |sin(delta_0)| < 0.01.

6. INTERIOR SOLUTION (r < 1): u_in(r) = B * sin(kappa * r),
   B = sin(k + delta_0) / sin(kappa)

7. BRANCH TRACKING: arctan returns [-pi/2, pi/2]. Track continuity of
   delta_0(k) and add n*pi corrections as needed to keep it continuous.

FAILURE MODES:
(a) arctan branch jumps at resonances. Handle by checking tan(kappa) > 1e6.
(b) Threshold V_0 = (pi/2)^2 in natural units. Below: a_s negative. Above: positive.
(c) For V_0 = 0, delta_0 = 0 for all k. Verify as sanity check.
````

### The Simulation Prompt

````
Read CLAUDE.md, DESIGN.md, and PROJECT.md first.

Build 07-partial-waves.html: single self-contained HTML using D3 v7 from CDN
and d3-simple-slider. No other dependencies.

LAYOUT: Two SVG panels 550×450 each inside a 1150×500 container.

LEFT PANEL — Radial wavefunction.
x-axis: r from 0 to 8 (natural units, a=1). y-axis: u(r) from -1.5 to 1.5.
  Line 1 (dashed gray): u_free = sin(k*r) for all r
  Line 2 (solid blue): sin(kappa*r)*B for 0<r<1; sin(k*r + delta_0) for r>1
  (B = sin(k + delta_0) / sin(kappa) per CLAUDE.md rule 6)
  Yellow shading for interior r < 1. Red dashed vertical line at r = 1.
  Text below: "δ₀ = [val] rad" and "aₛ = [val]", live.

RIGHT PANEL — sigma vs. k*a.
x-axis: k*a from 0.01 to 6. y-axis: sigma/pi*a^2 from 0 to 8.
  Solid black: 4*sin²(δ₀(k)) / k²
  Dashed red: 4/k² (unitarity bound)
  Dotted gray: y = 1 (classical)
  Vertical orange line at current k*a.
  Red triangles at resonance k values; blue circles at RT zeros.
  Recompute markers when V_0 changes (scan 500 k values from 0.01 to 6).

CONTROLS (below panels):
  V_0 slider: 0 to 25, step 0.05, default 5.0
  k*a slider: 0.01 to 6, step 0.01, default 1.0
  Live readouts: delta_0, sin²(delta_0), sigma_tot/pi, a_s

SANITY CHECKS to console on load and slider change:
  - V_0=0: delta_0 = 0 for all k. Log "PASS/FAIL".
  - V_0=(pi/2)^2=2.467: a_s diverges. Log a_s value.
  - Optical theorem: sigma_tot = (4*pi/k^2)*sin^2(delta_0).
    Log "Optical theorem check: [computed] vs [formula]".

Comments at every physics step. Pure functions for delta_0 and sigma.
````

### Exploration Tasks

**The factor of four.** Set $V_0 = 0$ (no well, pure hard sphere). At $ka = 0.1$, read $\sigma_\text{tot}/\pi a^2$. Confirm it is close to 4. Drag $ka$ to 5: the ratio should approach 2. Watch the transition between the $ka \ll 1$ and $ka \gg 1$ regimes.

**Bound-state threshold.** Slowly increase $V_0$ past $(π/2)^2 \approx 2.47$. Watch the scattering length readout (below the left panel) diverge and change sign. Before threshold: negative $a_s$. After: positive. The cross-section $\sigma_\text{tot} = 4\pi a_s^2$ diverges at the threshold — a new bound state has appeared.

**Resonance and interior wave.** Set $V_0 = 10$. Find the first resonance peak by dragging the $ka$ slider until the cross-section hits the unitarity bound. Look at the interior wave in the left panel: at resonance ($\delta_0 = \pi/2$), the interior amplitude is maximized and the exterior amplitude is minimal. The quasi-bound state is momentarily "trapped."

**Ramsauer-Townsend zero.** Set $V_0 = 15$ and find a blue circle marker on the right panel. Drag $ka$ to that energy. The cross-section is nearly zero — the attractive well has pushed $\delta_0$ through a full $\pi$, and the s-wave scatters as though there were no potential at all.

**Optical theorem check.** At any $V_0$ and $ka$, the console should report the optical theorem check passing. Confirm it is always "PASS."

---

## References

- Fitzpatrick, R. *Introductory Quantum Mechanics* (LibreTexts), Ch. 14. [verify URL active]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 11. [verify]
- Murayama, H. *Physics 221B Lecture Notes, Scattering Theory* (UC Berkeley, 2022). [verify URL active]
- Sakurai, J.J. and Napolitano, J. (2020). *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press. Ch. 6. [verify]
- Efimov, V. (1970). "Energy levels arising from resonant two-body forces in a three-body system." *Physics Letters B*, 33, 563–564. [verify]
- Kraemer, T. et al. (2006). "Evidence for Efimov quantum states in an ultracold gas of caesium atoms." *Nature*, 440, 315–318. [verify]

---

*Chapter 8 follows: Born approximation. Instead of expanding in angular-momentum channels, expand in powers of the potential. The result is a Fourier transform of $V(\mathbf{r})$ evaluated at the momentum transfer $\mathbf{q} = \mathbf{k}_f - \mathbf{k}_i$ — Rutherford scattering falls out as the leading term.*
