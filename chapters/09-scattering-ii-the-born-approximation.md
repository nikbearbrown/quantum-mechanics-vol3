# Chapter 8 — Scattering II: The Born Approximation

## TL;DR

- The Lippmann-Schwinger equation is the exact integral reformulation of the Schrödinger equation for scattering; the Born approximation is what you get when you replace the full wavefunction inside the integral with a plane wave.
- The Born scattering amplitude is the 3D Fourier transform of the potential, evaluated at the momentum transfer $\mathbf{q} = \mathbf{k} - \mathbf{k}'$.
- For the Yukawa potential $V_0 e^{-\mu r}/(\mu r)$, the Born amplitude is analytic: $f_B \propto 1/(q^2 + \mu^2)$.
- Taking $\mu \to 0$ recovers the Rutherford scattering formula exactly — the same formula Rutherford derived classically in 1911, from quantum mechanics by accident.
- Born is valid when the potential is weak or the energy is high; it fails near resonances and for slow particles.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Explain** the Lippmann-Schwinger equation as the exact integral reformulation of the scattering problem, and state precisely what approximation the Born approximation makes. *(Bloom: Understand)*
2. **Derive** the Born scattering amplitude as the Fourier transform of the potential and evaluate it for the Yukawa potential. *(Bloom: Apply)*
3. **Compute** the Rutherford differential cross-section as the Coulomb limit of the Yukawa Born result, and interpret the $\sin^{-4}(\theta/2)$ dependence geometrically. *(Bloom: Apply)*
4. **Assess** the validity of the Born approximation for a given potential using the Born parameter, and identify when the approximation breaks down. *(Bloom: Evaluate)*
5. **Produce** a Born cross-section for a new potential by computing its Fourier transform and comparing numerically against the exact partial-wave result from Chapter 7. *(Bloom: Create)*

---

In 1911, Ernest Rutherford worked out the scattering of alpha particles off gold nuclei by classical mechanics. He modeled the alpha particle as a point charge moving on a hyperbolic orbit under the $1/r$ Coulomb force, computed the deflection angle as a function of impact parameter, and translated that into a differential cross-section. His formula fit the Geiger-Marsden experimental data and established the nuclear model of the atom.

Fourteen years later, quantum mechanics arrived. The classical derivation became suspect: electrons and alpha particles are waves, not point masses, and hyperbolic orbits are not a concept the wave equation recognizes. The first calculation of Coulomb scattering in quantum mechanics, using the Born approximation, gave the same formula. Exactly the same. Not approximately — precisely.

Was this a coincidence? Is it always true that the Born approximation reproduces the classical result? What is going on?

It is not always true. For most potentials, the Born approximation is an approximation — it works at high energy and fails at low energy, near bound states, and whenever the potential is too strong. For the Coulomb potential specifically, the agreement with the classical result is exact (at the level of the cross-section, though not the amplitude), and there is a deep reason for it. Understanding why — and understanding when Born fails — is what this chapter is about.

---

## The Lippmann-Schwinger Equation

### From Schrödinger to an Integral Equation

The time-independent Schrödinger equation for scattering is:

$$\left(-\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r})\right)\psi = E\psi$$

Rearrange it by moving the potential to the right:

$$\left(\nabla^2 + k^2\right)\psi = \frac{2m}{\hbar^2}V\psi, \qquad k^2 = \frac{2mE}{\hbar^2}$$

This is the Helmholtz equation with a source term proportional to $V\psi$. Solve it using the **Green's function** for the Helmholtz operator: the function $G(\mathbf{r}, \mathbf{r}')$ that satisfies $(\nabla^2 + k^2)G = -\delta^3(\mathbf{r} - \mathbf{r}')$.

The outgoing-wave Green's function is:

$$G_+(\mathbf{r}, \mathbf{r}') = -\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{4\pi|\mathbf{r}-\mathbf{r}'|}$$

Using this to invert the Helmholtz equation (adding the homogeneous solution $\psi_0 = e^{ikz}$, the incident plane wave):

$$\boxed{\psi(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} - \frac{m}{2\pi\hbar^2}\int \frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}\,V(\mathbf{r}')\,\psi(\mathbf{r}')\,d^3r'}$$

This is the **Lippmann-Schwinger equation** (position-space form). It is exact. The total wavefunction at $\mathbf{r}$ is the incident plane wave plus contributions from every point $\mathbf{r}'$ where the potential is nonzero, each acting as a source of outgoing spherical waves. Read the kernel: a potential at $\mathbf{r}'$ scatters probability; that scattered probability propagates as a spherical wave $e^{ik|\mathbf{r}-\mathbf{r}'|}/|\mathbf{r}-\mathbf{r}'|$ to the observation point $\mathbf{r}$.

The equation is integral, not differential, but it is exact and useless until $\psi(\mathbf{r}')$ is known — which is what we are trying to find. Solving the Lippmann-Schwinger equation requires iteration.

In bra-ket notation, the same equation reads:

$$|\psi\rangle = |\phi\rangle + \hat{G}_0(E^+)\hat{V}|\psi\rangle$$

where $\hat{G}_0(E^+) = (E - \hat{H}_0 + i\epsilon)^{-1}$ is the free Green's operator and the $i\epsilon$ prescription selects outgoing boundary conditions. This form, due to Lippmann and Schwinger (1950) [verify], is the starting point for the T-matrix formalism and connects directly to Feynman diagram perturbation theory in quantum field theory.

### Extracting the Scattering Amplitude

Far from the scatterer ($r \gg r'$):

$$|\mathbf{r} - \mathbf{r}'| \approx r - \hat{r}\cdot\mathbf{r}'$$

where $\hat{r} = \mathbf{r}/r$ is the unit vector toward the detector. Let $\mathbf{k}' = k\hat{r}$ be the outgoing wavevector. Then:

$$\frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|} \approx \frac{e^{ikr}}{r}\,e^{-i\mathbf{k}'\cdot\mathbf{r}'}$$

Substituting into the Lippmann-Schwinger equation:

$$\psi(\mathbf{r}) \xrightarrow{r\to\infty} e^{i\mathbf{k}\cdot\mathbf{r}} + f(\mathbf{k},\mathbf{k}')\,\frac{e^{ikr}}{r}$$

with the **exact** scattering amplitude:

$$f(\mathbf{k},\mathbf{k}') = -\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{k}'\cdot\mathbf{r}'}\,V(\mathbf{r}')\,\psi(\mathbf{r}')\,d^3r'$$

This is exact but circular: it requires knowing $\psi(\mathbf{r}')$ inside the scattering region to evaluate $f$.

---

## The First Born Approximation

### Making the Approximation

The **first Born approximation** replaces $\psi(\mathbf{r}')$ in the integrand by the incident wave $\psi_0(\mathbf{r}') = e^{i\mathbf{k}\cdot\mathbf{r}'}$:

$$f_B(\theta) = -\frac{m}{2\pi\hbar^2}\int e^{-i\mathbf{k}'\cdot\mathbf{r}'}\,V(\mathbf{r}')\,e^{i\mathbf{k}\cdot\mathbf{r}'}\,d^3r'$$

$$\boxed{f_B(\theta) = -\frac{m}{2\pi\hbar^2}\int e^{i(\mathbf{k}-\mathbf{k}')\cdot\mathbf{r}'}\,V(\mathbf{r}')\,d^3r' = -\frac{m}{2\pi\hbar^2}\,\widetilde{V}(\mathbf{q})}$$

where $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ is the **momentum transfer** and $\widetilde{V}(\mathbf{q})$ is the **3D Fourier transform** of the potential.

This is the central insight: **the Born scattering amplitude is (proportional to) the Fourier transform of the potential, evaluated at the momentum transfer.**

The magnitude of the momentum transfer: since $|\mathbf{k}| = |\mathbf{k}'| = k$ (elastic scattering), the triangle of wavevectors gives:

$$q = |\mathbf{q}| = 2k\sin(\theta/2)$$

At $\theta = 0$ (forward scattering), $q = 0$: you probe $\widetilde{V}(0) = \int V\,d^3r$, the volume integral of the potential — its long-range behavior. At $\theta = \pi$ (backscattering), $q = 2k$: you probe the high-frequency Fourier components, the short-range structure. The Born approximation is a kind of diffraction experiment: each scattering angle measures a different Fourier mode of the potential.

### The Yukawa Potential

$$V(r) = \frac{V_0\,e^{-\mu r}}{\mu r}$$

This potential has range $1/\mu$ and is the prototypical Born calculation. The Fourier transform uses the spherical symmetry: $d^3r' = r'^2\sin\theta'\,dr'\,d\theta'\,d\phi'$, and the angular integrals collapse the 3D Fourier transform to a 1D sine transform:

$$\widetilde{V}(q) = \int_0^\infty \int_0^\pi \frac{V_0\,e^{-\mu r'}}{\mu r'}\,e^{iqr'\cos\theta'}\,r'^2\sin\theta'\,dr'\,d\theta'\,d\phi'$$

Perform the $\phi'$ integral (gives $2\pi$) and the $\theta'$ integral:

$$\int_0^\pi e^{iqr'\cos\theta'}\sin\theta'\,d\theta' = \frac{2\sin(qr')}{qr'}$$

So:

$$\widetilde{V}(q) = \frac{4\pi V_0}{\mu}\int_0^\infty e^{-\mu r'}\frac{\sin(qr')}{qr'}\,r'\,dr' = \frac{4\pi V_0}{\mu}\cdot\frac{1}{q^2+\mu^2}$$

The Born scattering amplitude is:

$$f_B(\theta) = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{q^2+\mu^2} = -\frac{2mV_0}{\hbar^2\mu}\cdot\frac{1}{4k^2\sin^2(\theta/2)+\mu^2}$$

The differential cross-section:

$$\boxed{\frac{d\sigma}{d\Omega} = \left(\frac{2mV_0}{\hbar^2\mu}\right)^2\frac{1}{\left[4k^2\sin^2(\theta/2)+\mu^2\right]^2}}$$

This is the Yukawa Born cross-section. It falls off at large angles as $\sin^{-4}(\theta/2)$ (when $\mu \ll k$), and the forward peak sharpens as $k$ increases. At large angles (large $q$), the cross-section falls because the potential is soft and does not have high-frequency Fourier components.

---

## Worked Example: Screened Coulomb → Rutherford

### The Lesson

**Setup.** Alpha-particle scattering off a gold nucleus: $Z = 2$ (alpha), $Z' = 79$ (gold), incident kinetic energy $E = 5$ MeV (the Geiger-Marsden experimental range). The interaction is Coulomb, $V(r) = ZZ'e^2/(4\pi\epsilon_0 r)$. Model it as the $\mu \to 0$ limit of the Yukawa potential with $V_0/\mu \to ZZ'e^2/(4\pi\epsilon_0)$.

**Step 1: The Coulomb limit.** Take $\mu \to 0$ in the Yukawa cross-section:

$$\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0}\right)^2\frac{1}{(4E)^2\sin^4(\theta/2)} = \left(\frac{ZZ'e^2}{16\pi\epsilon_0 E}\right)^2\frac{1}{\sin^4(\theta/2)}$$

This is the **Rutherford formula**. (Used $\hbar^2 k^2/2m = E$ to write $\hbar^2 k^2 = 2mE = m\cdot 2E = $ ... actually, more cleanly: $f_B = -2mZZ'e^2/(4\pi\epsilon_0\hbar^2)\cdot 1/(q^2)$, and $|f_B|^2 = (ZZ'e^2/(4\pi\epsilon_0))^2 \cdot 4m^2/(\hbar^4 q^4)$. With $q^2 = 4k^2\sin^2(\theta/2)$ and $E = \hbar^2k^2/2m$ so $m/\hbar^2k^2 = 1/(2E)$:

$$\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0}\right)^2\frac{m^2}{\hbar^4\cdot 4k^4\sin^4(\theta/2)} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0\cdot 4E}\right)^2\frac{1}{\sin^4(\theta/2)}$$

**Step 2: Numerical check.** At $\theta = 90°$, $\sin^4(\theta/2) = \sin^4(45°) = (1/\sqrt{2})^4 = 1/4$:

$$\frac{d\sigma}{d\Omega}\bigg|_{\theta=90°} = 4\left(\frac{2\times 79\times 1.44\,\text{MeV}\cdot\text{fm}}{4\times 5\,\text{MeV}}\right)^2 = 4\times(11.4\,\text{fm})^2 \approx 520\,\text{fm}^2/\text{sr}$$

The historical Geiger-Marsden experiments found the Rutherford formula accurate to high precision across a range of energies and target materials, confirming the nuclear model [verify — Geiger & Marsden 1913].

**Step 3: Why is Born exact for Coulomb?** For any other potential, Born is an approximation — the true amplitude $f$ differs from $f_B$. For the Coulomb potential, the exact quantum mechanical amplitude (found by solving the Coulomb scattering problem exactly) has the form:

$$f_{\rm exact}(\theta) = -\frac{ZZ'e^2}{4\pi\epsilon_0\cdot 4E\sin^2(\theta/2)}\,e^{-i\eta\ln\sin^2(\theta/2)}\cdot\frac{\Gamma(1+i\eta)}{\Gamma(1-i\eta)}$$

where $\eta = ZZ'e^2/(4\pi\epsilon_0 \hbar v)$ is the Sommerfeld parameter and $v$ is the particle speed. The differential cross-section is $|f_{\rm exact}|^2$, and the phase factors drop out:

$$\frac{d\sigma}{d\Omega} = |f_{\rm exact}|^2 = \left(\frac{ZZ'e^2}{4\pi\epsilon_0\cdot 4E}\right)^2\frac{1}{\sin^4(\theta/2)}$$

Same as Born. The agreement is not an approximation — it is exact. The reason is that the Coulomb potential is the one potential for which the Born approximation happens to get the modulus of the amplitude right (the phase is different). This is a special property of $1/r$ potentials related to their scale invariance and the specific structure of Coulomb wave functions.

### The Limit

**Forward divergence.** As $\theta \to 0$, $\sin^2(\theta/2) \to 0$ and $d\sigma/d\Omega \to \infty$. The Rutherford cross-section is not integrable: $\sigma_{\rm tot} = \int (d\sigma/d\Omega)\,d\Omega = \infty$ for the Coulomb potential. This is not a failure of the Born approximation — it is the correct quantum (and classical) result. The Coulomb potential has infinite range, and even arbitrarily distant particles are deflected by some small angle. Summing over all of these, most of them at tiny angles, gives infinite total cross-section.

In a real experiment, the nuclear Coulomb field is screened at the scale of the atomic radius $a_0$ by the surrounding electrons. With a Thomas-Fermi screening parameter $\mu \sim a_0^{-1}Z^{1/3}$, the Yukawa potential applies and the total cross-section is:

$$\sigma_{\rm tot} = \pi\left(\frac{ZZ'e^2}{4\pi\epsilon_0\hbar^2\mu/m}\right)^2\cdot\frac{1}{\mu^2 + 4k^2}^{-1} \approx \pi\left(\frac{ZZ'e^2}{4\pi\epsilon_0}\right)^2\frac{m^2}{\hbar^4\mu^4}$$

Finite, as it should be. The Coulomb divergence is cured by any screening, however weak. At large angles (small impact parameters, large $q \gg \mu$), the screening is irrelevant and the Rutherford formula holds. At small angles ($q \ll \mu$), the screened result is a constant; the Coulomb divergence is cut off by the screening.

---

## Validity of the Born Approximation

### The Born Parameter

The Born approximation replaces $\psi(\mathbf{r}') \approx e^{i\mathbf{k}\cdot\mathbf{r}'}$ inside the Lippmann-Schwinger integral. This is valid when the scattered wave is small compared to the incident wave inside the scattering region:

$$\left|\frac{m}{2\pi\hbar^2}\int \frac{e^{ik|\mathbf{r}-\mathbf{r}'|}}{|\mathbf{r}-\mathbf{r}'|}\,V(\mathbf{r}')\,e^{i\mathbf{k}\cdot\mathbf{r}'}\,d^3r'\right| \ll 1$$

Evaluating this at the center of the scatterer ($\mathbf{r} = 0$) for the Yukawa potential gives two conditions:

**Low energy** ($k \ll \mu$, range of potential $\gg$ de Broglie wavelength):

$$\frac{2m|V_0|}{\hbar^2\mu^2} \ll 1$$

**High energy** ($k \gg \mu$):

$$\frac{2m|V_0|}{\hbar^2\mu k} \ll 1$$

The low-energy condition requires the potential to be weak in absolute terms (its integral over the range of the potential must be small). The high-energy condition becomes easier to satisfy as $k$ increases — Born is progressively better at higher energies. This is why Born is called a "high-energy approximation" but this label is a bit misleading: it also requires the potential to be weak. Strong potentials (those that support bound states) will have $2m|V_0|/\hbar^2\mu^2 \gtrsim 1$ regardless of energy, and the low-energy Born condition fails.

**Practical rule:** if the potential is strong enough to support a bound state near threshold, Born fails at low energy. If the energy is much larger than the depth of the potential, Born works. The transition between these regimes is the subject of the Born validity diagram described below.

### The Born Validity Diagram

The Born approximation lives in a two-dimensional parameter space: potential strength $\xi = 2m|V_0|/(\hbar^2\mu^2)$ on one axis, $ka$ on the other (where $a = 1/\mu$ is the range).

- **Region 1** ($\xi \ll 1$, any $k$): Born is valid. The potential is too weak to distort the wavefunction significantly.
- **Region 2** ($\xi \gtrsim 1$, $ka \gtrsim \xi$): Born is approximately valid. The energy is high enough to overcome the potential depth.
- **Region 3** ($\xi \gtrsim 1$, $ka \lesssim \xi$): Born fails. Slow particles in a strong potential are strongly distorted; resonances appear; Born misses them entirely.
- **Boundary**: the curve $ka \sim \xi$ separates regions 2 and 3. The diagram's key feature is that even a strong potential ($\xi \gg 1$) can be handled by Born if $ka$ is large enough.

A resonance in the exact partial-wave cross-section shows up as a sharp peak that Born completely misses — Born gives a smooth, slowly varying cross-section even when the exact result has a spike at the resonance energy. Near a resonance, the Born approximation is not quantitatively wrong; it is qualitatively wrong. It predicts no resonance structure because it assumes the wavefunction is barely perturbed.

> **Figure description (commissioned).** A log-log plot with axes $\xi = 2m|V_0|/\hbar^2\mu^2$ (vertical, range $10^{-2}$ to $10^2$) and $ka$ (horizontal, range $10^{-1}$ to $10^2$). The Born-valid region is colored light green (below and to the right of the boundary curve $ka \gtrsim \xi$). The Born-invalid region is colored light red. The Rutherford limit ($\xi \sim Z^2e^4m^2/\hbar^4\mu^2$, typically $\gg 1$ for nuclei) is marked with a dashed contour showing the Sommerfeld parameter $\eta = 1$. Resonance energies (where exact $\sigma$ peaks) are marked as small red stars along the $\xi \sim 1$ line. The diagram makes visually clear that Born works either for weak potentials at any energy, or for fast particles even in strong potentials.

---

## The Born Series and What Comes Next

The Lippmann-Schwinger equation can be iterated. Substitute $\psi = \psi_0 + \delta\psi$ into the right-hand side, then repeat:

$$\psi = \psi_0 + \hat{G}_0 V\psi_0 + \hat{G}_0 V\hat{G}_0 V\psi_0 + \cdots$$

This is the **Born series**. The first term gives $f_B^{(1)}$ (what we computed). The second term gives $f_B^{(2)}$, the second Born approximation. Each successive term is smaller by one power of the Born parameter $\xi$. When $\xi \ll 1$, the series converges. When $\xi \sim 1$, the series converges slowly. When $\xi \gg 1$ and $ka$ is not large, the series diverges.

The formal structure is identical to time-independent perturbation theory: the Born series is perturbation theory in the potential $V$, applied to a scattering state. The first Born term is analogous to the first-order energy correction $\langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$ from Chapter 2 — same logic, same hierarchy, same convergence condition. The difference is that here the unperturbed state is a plane wave (a continuum state), not a bound state.

In quantum field theory, the first Born term corresponds to tree-level scattering diagrams (exchange of a single virtual particle); the second Born term corresponds to one-loop corrections; and so on. The Born series is the origin of Feynman diagrams in perturbation theory, and the convergence criterion is the coupling constant being small — which for QED is $\alpha \approx 1/137$, comfortably small, which is why QED perturbation theory works so well.

---

## Common Misconceptions

**"Born gives the exact Rutherford formula therefore Born is exact for Coulomb scattering."** Born gives the exact differential cross-section for Coulomb scattering, but not the exact amplitude. The amplitude has an additional phase factor $e^{-i\eta\ln\sin^2(\theta/2)}$ (a Coulomb phase) that Born misses. This matters for interference effects — for example, in identical-particle Coulomb scattering, the interference between direct and exchange amplitudes involves the phase, and Born gives the wrong answer for the interference pattern.

**"The momentum transfer $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ is the change in momentum of the particle."** Close but not right. $\hbar\mathbf{q}$ is the momentum transferred from the potential to the particle (or equivalently from the particle to the target). It is not $\mathbf{k}' - \mathbf{k}$ — the sign convention matters. Draw the triangle: $\mathbf{k} + \mathbf{q}/... $ — just draw $\mathbf{k}$ and $\mathbf{k}'$ as two vectors of equal length, and $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ as the vector from the tip of $\mathbf{k}'$ to the tip of $\mathbf{k}$.

**"Born is just the s-wave approximation."** No — Born works for any number of partial waves. It is a weak-potential approximation that replaces $\psi$ by $\psi_0$ everywhere inside the integral. At high energies, many $\ell$ values contribute, and Born handles all of them simultaneously via the Fourier transform. The s-wave approximation (Chapter 7) is a different approximation — low energy, not weak potential.

**"The Born approximation violates the optical theorem."** It does not. The Born scattering amplitude $f_B(\theta)$ satisfies a version of the optical theorem consistent with the approximation. However, the imaginary part of $f_B(0)$ computed directly from the Born formula may not match $(k/4\pi)\sigma_{\rm tot}^B$ exactly when higher-order terms are comparable in size. The optical theorem is exact; the Born approximation violates it only at the level of the next Born term, which is beyond the approximation being made.

**"If the Born parameter $\xi \ll 1$, Born is always reliable."** Born requires two things: weak potential *and* that no near-resonant states exist. Even for a formally small $\xi$, if there is a near-threshold bound state (scattering length $|a_s| \gg 1/\mu$), the Born amplitude can underestimate the cross-section by orders of magnitude near $k = 0$. The Born parameter is necessary but not sufficient.

---

## Exercises

**8.1** (Remember) State the Lippmann-Schwinger equation in position space. Identify: (a) the incident wave term; (b) the Green's function kernel; (c) what approximation converts this exact equation into the first Born approximation. Then state the Born approximation result: $f_B(\theta) = $ [fill in], and identify $\mathbf{q}$.

**8.2** (Understand) The Born scattering amplitude is the Fourier transform of the potential. (a) For a spherically symmetric potential $V(r)$, reduce the 3D Fourier transform to a 1D integral by performing the angular integrations. Your answer should involve $\int_0^\infty r V(r) \sin(qr)\,dr$. (b) For the Gaussian potential $V(r) = V_0 e^{-r^2/a^2}$, compute $\widetilde{V}(q)$. (The Fourier transform of a Gaussian is a Gaussian.) (c) Sketch $d\sigma/d\Omega$ vs. $\theta$ for the Gaussian potential. Is the angular distribution narrower or wider than for the Yukawa potential of the same range?

**8.3** (Apply) The Yukawa Born cross-section is $d\sigma/d\Omega = (2mV_0/\hbar^2\mu)^2 \cdot [4k^2\sin^2(\theta/2)+\mu^2]^{-2}$. (a) Integrate this over solid angle to find $\sigma_{\rm tot}$ for the Yukawa potential. The integral $\int_0^\pi \sin\theta\,d\theta/[A + B\sin^2(\theta/2)]^2$ can be done by substituting $u = \cos\theta$. (b) Show that as $\mu \to 0$ (Coulomb limit), $\sigma_{\rm tot} \to \infty$. Interpret this physically.

**8.4** (Apply) Rutherford scattering: alpha particles ($Z = 2$, $A = 4$) on silver ($Z' = 47$) at $E = 8$ MeV. (a) Compute $d\sigma/d\Omega$ at $\theta = 30°$, $60°$, $90°$, $120°$, $150°$ in units of fm$^2$/sr. (Recall $e^2/(4\pi\epsilon_0) = 1.44$ MeV·fm.) (b) At which angle does the cross-section fall to 1% of its forward value? (c) For what angle does the de Broglie wavelength become comparable to the distance of closest approach? At and above this angle the nuclear force becomes important and Rutherford fails — estimate this angle for the alpha-silver system.

**8.5** (Apply) Born validity for the Yukawa potential. (a) Write down the two Born validity conditions (low energy and high energy) in terms of the dimensionless Born parameter $\xi = 2m|V_0|/\hbar^2\mu^2$ and $ka = k/\mu$. (b) For $V_0 = \hbar^2\mu^2/(2m)$ (i.e., $\xi = 1$), at what $ka$ does the high-energy condition become satisfied (Born parameter $< 0.1$)? (c) A Yukawa potential with $\xi = 10$ supports a bound state near threshold. Argue that the Born cross-section at $ka = 1$ is unreliable, even though the energy is "moderate."

**8.6** (Analyze, Produce) Write a short script (Python/numpy or any language) or use an LLM to: compute the Born cross-section for a Yukawa potential with $\xi = 0.5$ and $ka = 2$, numerically; compute the exact s-wave cross-section using the phase-shift formula from Chapter 7 at the same parameters; and compare. Is Born accurate? Repeat for $\xi = 5$, $ka = 2$. How large is the Born error in each case?

**8.7** (Analyze) Form factors. For an extended nuclear charge distribution $\rho(r)$ (normalized to 1), the Born cross-section for elastic scattering factors as:

$$\frac{d\sigma}{d\Omega} = \left(\frac{d\sigma}{d\Omega}\right)_{\rm point} \times |F(q)|^2$$

where $F(q) = \int e^{i\mathbf{q}\cdot\mathbf{r}}\rho(r)\,d^3r$ is the nuclear form factor. (a) Show that $F(0) = 1$ always. (b) For a uniform sphere of radius $R$: $\rho(r) = 3/(4\pi R^3)$ for $r \leq R$, zero otherwise. Compute $F(q)$ analytically. (Express in terms of $j_1(qR) = \sin(qR)/qR - \cos(qR)/(qR)^0\ldots$ — look up the result for the sphere form factor.) (c) At what $q$ does $|F(q)|^2$ first go to zero? This gives the first zero of the form factor and can be used experimentally to determine nuclear radii — this is what Hofstadter did in 1956 to measure the proton radius [verify].

---

## Still Puzzling

**Why is Born exact for Coulomb?** The "accident" has a deep explanation. For a $1/r$ potential, the Coulomb Green's function (the propagator for a charged particle in a Coulomb field) can be written in closed form in terms of Whittaker functions. When you compute $|f_{\rm exact}|^2$, the Coulomb phase factors $|\Gamma(1+i\eta)/\Gamma(1-i\eta)| = 1$ cancel exactly (the Gamma function ratio has modulus 1 since $i\eta$ is purely imaginary). The residual is the Rutherford formula — same as Born. This cancellation is special to the $1/r$ form; no other potential has it. It is connected to the scale invariance of the Coulomb potential (which has no intrinsic length scale, only an angular scale) and the hidden $O(4)$ symmetry of the hydrogen atom.

**The Born series and its convergence.** For most potentials, the Born series — the systematic iteration of the Lippmann-Schwinger equation — converges when $\xi < 1$ and diverges when $\xi > 1$. But "converges" means $|f^{(n)}| \to 0$ as $n \to \infty$. For the Coulomb potential, the Born series does not converge in the usual sense (the Coulomb potential has $\xi = \infty$ for any $\mu$ since it has no range). Yet the first Born term gives the exact differential cross-section. This is related to the fact that the Coulomb scattering problem can be summed to all orders exactly. The full story involves the eikonal approximation, Glauber theory, and the resummation of the Coulomb phase — topics developed in graduate-level scattering theory.

**The Born validity diagram.** The diagram described in the chapter (potential strength $\xi$ vs. $ka$, with the Born-valid region shaded) is an important conceptual tool but its precise boundary depends on what you mean by "valid" (10% accuracy? 1%?). The exact boundary is potential-dependent and requires numerical comparison against exact partial-wave results. Building this diagram for a specific potential (say, Yukawa with $\xi = 1, 5, 10$) is the kind of calibration exercise that builds physical intuition. The simulation in this chapter's $+1$ makes this visual and interactive.

**Inelastic scattering and form factors.** The Born approximation extends naturally to inelastic processes. If the target can be excited from state $|i\rangle$ to state $|f\rangle$, the inelastic Born amplitude is $f_B^{(fi)} \propto \langle f| \widetilde{V}(\mathbf{q}) |i\rangle$ — the matrix element of the Fourier-transformed potential. Nuclear excitation cross-sections, photoionization, and deep inelastic scattering in particle physics all use this generalization. The nuclear form factor discussed in Exercise 8.7 is the simplest example: elastic scattering off an extended target, where the "target form factor" is the Fourier transform of the charge distribution.

---

## The +1 — Simulation Exercise

Your deliverable is `08-born-approximation.html`: a single-file D3 simulation that Fourier-transforms any spherically symmetric potential and shows the Born differential cross-section alongside the exact s-wave result.

### Part 1 — Update `PROJECT.md`

```
Append to PROJECT.md:

Chapter 08 — Scattering II: The Born Approximation
Deliverable: 08-born-approximation.html
Status: in progress

The simulation has two modes, selectable by tabs at the top:

MODE A — Yukawa/Rutherford explorer.
Two panels side by side:

LEFT PANEL: Angular distribution.
  Polar plot (or Cartesian plot of dσ/dΩ vs θ) from 0 to π.
  Two overlaid curves:
    Born result (solid blue): dσ/dΩ = (2mV₀/ℏ²μ)² / [4k²sin²(θ/2)+μ²]²
    Exact s-wave result (dashed black): computed from phase-shift formula
    (for the s-wave at the given ka and V₀)
  y-axis: dσ/dΩ in units of a² (where a=1/μ).
  x-axis: θ from 0 to π (radians or degrees, togglable).

RIGHT PANEL: Cross-section vs. ka.
  Plot σ_tot / πa² vs ka from 0.1 to 10 for both Born (solid blue)
  and exact s-wave (dashed black).
  Mark the current ka with a vertical orange line.
  When Born and exact differ by more than 20%, shade the region red.

CONTROLS for Mode A:
  Slider: V₀ (Born parameter ξ = 2mV₀/ℏ²μ² from 0.01 to 10, log scale)
  Slider: ka (from 0.1 to 10)
  Display: Born parameter ξ, Rutherford parameter η = ZZ'e²/(4πε₀ℏv) [for
    context, shown as a pure number], current dσ/dΩ at θ=90°.

MODE B — Fourier transform explorer.
A single wide panel showing:
  LEFT THIRD: potential V(r) vs r, user-selectable from:
    - Yukawa: V₀ e^{-μr}/(μr)
    - Gaussian: V₀ exp(-r²/a²)
    - Square well: -V₀ for r<a, 0 outside
    - Hard sphere: infinite for r<a (approximate as V₀=100 e^{-r/ε}/r for
      small ε)
  CENTER THIRD: Fourier transform Ṽ(q) vs q, computed numerically by
    the 1D sine transform integral ∫₀^∞ r·V(r)·sin(qr) dr via trapezoidal
    rule on 1000 points from 0 to 20a.
  RIGHT THIRD: dσ/dΩ = (m/2πℏ²)² |Ṽ(q)|² plotted vs θ (q=2k sin(θ/2)).
    Overlay the exact s-wave dσ/dΩ (dashed black).

CONTROLS for Mode B:
  Dropdown: potential type (Yukawa / Gaussian / Square well / Hard sphere)
  Slider: V₀ (strength), Slider: a or μ (range), Slider: ka
  Toggle: "Show Born only" / "Show Born + exact s-wave"
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md:

BORN APPROXIMATION PHYSICS RULES (Chapter 08)

1. BORN SCATTERING AMPLITUDE for central potential:
   f_B(θ) = -(2m/ℏ²q) ∫₀^∞ r V(r) sin(qr) dr
   where q = 2k sin(θ/2).
   In natural units (ℏ = 2m = 1): f_B(θ) = -(1/q) ∫₀^∞ r V(r) sin(qr) dr.

2. YUKAWA BORN AMPLITUDE (analytic):
   f_B(θ) = -V₀/(μ(q²+μ²))
   dσ/dΩ = (V₀/μ)² / (q²+μ²)²   [natural units]
   In natural units with μ=1: dσ/dΩ = V₀² / (4k²sin²(θ/2)+1)²

3. MOMENTUM TRANSFER:
   q = 2k sin(θ/2)
   At θ=0: q=0 (forward scattering, probes long-range structure)
   At θ=π: q=2k (backscattering, probes short-range structure)
   Never confuse q (scalar) with the vector q = k - k'.

4. BORN VALIDITY CHECK:
   Low energy (k << μ=1 in natural units): valid when V₀ << 1
   High energy (k >> 1): valid when V₀/k << 1
   In the simulation, compute the Born parameter xi = V₀ (in natural
   units where ℏ²μ²/2m = 1) and display "Born valid" if xi < 0.5 or
   ka > 2*xi; display "Born unreliable" otherwise in orange text.

5. NUMERICAL FOURIER TRANSFORM for Mode B:
   Use Simpson's rule on a grid r_i = (i+0.5)*dr for i=0..N-1, dr=20/N, N=1000.
   Ṽ(q) = (4π/q) sum_i r_i V(r_i) sin(q*r_i) * dr
   For q → 0, use the limit Ṽ(0) = 4π ∫₀^∞ r² V(r) dr (computed separately).

6. EXACT S-WAVE for comparison (from Chapter 07 CLAUDE.md):
   For Yukawa potential, the exact s-wave phase shift is NOT analytically
   available in a simple form. Use the square-well formula as an approximation
   by setting the well depth to match V₀ at r=a=1/μ. Alternatively, integrate
   the radial Schrödinger equation numerically (Numerov method) to get δ₀.
   For the Gaussian potential, always use Numerov.

7. NUMEROV METHOD for exact phase shifts:
   Radial equation: u'' = -[k² - U(r)] u where U(r) = 2m V(r)/ℏ².
   In natural units: u'' = -[k² - V(r)] u.
   Grid: r_i = i*dr, dr = 0.01, i = 0..800 (up to r=8a).
   Boundary conditions: u(0) = 0, u(dr) = dr (small, slope initialization).
   Numerov step: u_{i+1} = [2u_i(1 - 5/12*dr²*f_i) - u_{i-1}(1 + 1/12*dr²*f_{i-1})]
                            / (1 + 1/12*dr²*f_{i+1})
   where f_i = k² - V(r_i).
   At large r (r > 5a), V=0 so u ~ A sin(kr + δ₀).
   Extract δ₀: tan(δ₀) = [k*u(r₁)*cos(kr₂) - k*u(r₂)*cos(kr₁)] /
                           [k*u(r₂)*sin(kr₁) - k*u(r₁)*sin(kr₂)]
   for two points r₁, r₂ in the asymptotic region.
   σ_exact_s = (4π/k²) sin²(δ₀).

KNOWN FAILURE MODES:
(a) Division by q near θ=0. Catch q < 1e-10 and use L'Hopital: as q→0,
    Ṽ(q)/q → (4π/3) ∫₀^∞ r³ V(r) dr (for the 1D sine transform).
    In practice, set a floor: q = max(q, 1e-6).
(b) Numerov instability for V₀ large (>> k²). Step size dr=0.01 may
    be insufficient; decrease to dr=0.001 when V₀ > 50.
(c) Born cross-section diverges as μ→0 (Coulomb limit) for fixed screen.
    Clip dσ/dΩ at 1e6 in plot units to prevent axis collapse.
```

### Part 3 — The simulation prompt

```
Read CLAUDE.md, DESIGN.md, PROJECT.md first.

Build 08-born-approximation.html: a single self-contained HTML file using
D3 v7 from CDN and d3-simple-slider. No other dependencies.

Two tabs at the top: "Yukawa/Rutherford" and "Fourier explorer".

YUKAWA/RUTHERFORD TAB
Two SVG panels, 500 x 400 each.

LEFT PANEL — Angular distribution.
  x-axis: θ from 0° to 180°. y-axis: log₁₀(dσ/dΩ) in natural units (a²).
  Use log scale because Rutherford spans many decades.
  Two curves: Born (solid blue, computed analytically per CLAUDE.md rule 2),
               Exact s-wave (dashed black, computed via Numerov per rule 7).
  The curves should match closely when the Born parameter is small (ξ < 0.5).
  Annotation: label the curves at θ=60° ("Born" and "Exact s-wave").
  Show a horizontal dashed gray line at dσ/dΩ = a² for scale reference.

RIGHT PANEL — Total cross-section vs. energy.
  x-axis: ka from 0.1 to 10. y-axis: σ_tot / πa² from 0 to 8.
  Born total cross-section (solid blue): integrate numerically over θ.
  Exact s-wave (dashed black): (4/k²) sin²(δ₀), from Numerov.
  Vertical orange line at current ka.
  When |σ_Born - σ_exact| / σ_exact > 0.2, shade the background light red.
  Display the Born parameter ξ and a "Born valid / unreliable" text label.

Controls:
  Slider: ξ = V₀ (Born parameter, natural units), range 0.01 to 10, log, default 0.5
  Slider: ka, range 0.1 to 10, default 2.0
  Numerical readout: q at θ=90°, dσ/dΩ|_Born at θ=90°, σ_Born/πa², σ_exact/πa²

FOURIER EXPLORER TAB
Three-panel layout: 300 wide + 350 wide + 350 wide, all 400 tall.

LEFT PANEL: V(r) vs. r, r from 0 to 8, y-axis from -V₀ to +V₀.
  Dropdown menu above: "Yukawa", "Gaussian", "Square well", "Hard sphere approx."
  Plot the selected potential in solid blue.
  Shade the potential well below y=0 in light blue.

CENTER PANEL: Ṽ(q) vs. q, q from 0 to 12 (in units of 1/a).
  Compute via numerical sine transform (CLAUDE.md rule 5).
  Plot in solid green.
  Annotate the q=0 intercept as "∫V d³r / 4π".

RIGHT PANEL: dσ/dΩ vs. θ (0 to 180°).
  Born (solid blue): (m/2πℏ²)² |Ṽ(q(θ))|²  [= |Ṽ(q)|²/4 in natural units]
  Exact s-wave (dashed black): from Numerov.
  Use log y-axis, same as Mode A.

Controls (shared):
  Dropdown: potential type
  Slider: V₀ strength (range 0.1 to 20), Slider: a (range 0.2 to 3.0), Slider: ka
  Toggle: "Log scale / Linear scale" for dσ/dΩ panel
  Toggle: "Show exact s-wave" (on by default)

CONSOLE SANITY CHECKS (log on each control change):
  - Born amplitude at θ=90° for Yukawa: should equal -V₀/(q²+1) analytically.
    Log: "Born check (analytic vs. numerical): [analytic] vs. [numerical]"
  - Optical theorem: σ_Born = (4π/k) Im[f_B(0)].
    For Yukawa: Im[f_B(0)] = V₀/(k*(0+1)²) = V₀/k. Then (4π/k)*V₀/k = 4πV₀/k².
    The numerical integrated σ_Born should match this within 1%.
    Log: "Optical theorem: integrated σ=[val], from Im[f(0)]=[val]."

Pure functions for Born amplitude, exact Numerov phase, total cross-section.
All computations in natural units (ℏ = 2m = 1, μ = 1 so a = 1).
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. **Mode A, Yukawa.** Set $\xi = 0.5$ and $ka = 2$. Compare the Born and exact s-wave angular distributions. Do they agree? Now increase $\xi$ to 5 with $ka = 2$. At what angle does the Born result deviate most from the exact s-wave?

2. **Mode A, cross-section panel.** For $\xi = 1$, find the value of $ka$ at which the Born total cross-section overestimates the exact by 20% (i.e., the red shading onset). Does this $ka$ match the high-energy Born validity condition $\xi < ka$ from CLAUDE.md?

3. **Mode B, Fourier explorer.** Switch to "Gaussian" potential, $V_0 = 1$, $a = 1$, $ka = 2$. Compare the Born $d\sigma/d\Omega$ to the exact s-wave. Now switch to "Square well" with the same parameters. Which potential gives the more forward-peaked cross-section? Why? (Hint: which has a broader Fourier transform?)

4. **Rutherford check.** In Mode B, select "Yukawa", set $\xi = 0.1$ (weak Coulomb-like), $ka = 5$. Compare the angular distribution to $\sin^{-4}(\theta/2)$. Does the simulation reproduce the Rutherford shape?

5. **Optical theorem check.** At any settings, the console should report that the integrated Born cross-section matches $(4\pi/k)\,\operatorname{Im}[f_B(0)]$ to within 1%. Verify this by reading the console for three different parameter choices.

**Extension prompt:**

```
Modify 08-born-approximation.html to add a third mode: "Born validity map".

Display a 2D heatmap with:
  x-axis: ka from 0.1 to 10 (50 points, linear)
  y-axis: ξ = V₀ from 0.01 to 10 (50 points, log scale)
  Color: |σ_Born - σ_exact| / σ_exact, where σ_exact is the exact s-wave
    total cross-section (Numerov). Use a green-to-red colorscale:
    green = Born valid (< 5% error), yellow = marginal, red = Born invalid.

The map should compute 2500 (ka, ξ) pairs. Compute in a Web Worker or
in small batches with setTimeout to avoid blocking the UI. Show a progress
bar.

Overlay the theoretical boundary curve ka = ξ (dashed white line) on
the heatmap. The boundary should separate the green and red regions.

Update PROJECT.md to mark Chapter 08 complete and note the Born validity
map as a bridge to graduate-level optical model and DWBA methods.
```

---

## References

1. Fitzpatrick, R., *Introductory Quantum Mechanics* (LibreTexts / UT Austin), §§14.1–14.2 [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory]. Full derivation of the Lippmann-Schwinger equation and Born approximation; the Yukawa-to-Rutherford derivation is presented explicitly. CC BY-NC-SA 4.0. [verify URL active]

2. Lippmann, B. A. & Schwinger, J., "Variational principles for scattering processes. I," *Physical Review* **79**, 469–480 (1950). The original paper introducing the integral equation formulation. [verify]

3. Griffiths, D. J. & Schroeter, D. F., *Introduction to Quantum Mechanics*, 3rd ed. (Cambridge, 2018), Ch. 11. Born approximation derivation following from the integral equation; Rutherford as the $\mu \to 0$ limit. [verify edition]

4. Rutherford, E., "The Scattering of $\alpha$ and $\beta$ Particles by Matter and the Structure of the Atom," *Philosophical Magazine* **21**, 669–688 (1911). The original Rutherford scattering paper establishing the nuclear model. [verify]

5. Geiger, H. & Marsden, E., "On a Diffuse Reflection of the $\alpha$-Particles," *Proceedings of the Royal Society A* **82**, 495–500 (1909). Original scattering experiment showing large-angle deflections. [verify]

6. Geiger, H. & Marsden, E., "The Laws of Deflexion of $\alpha$ Particles through Large Angles," *Philosophical Magazine* **25**, 604–623 (1913). Quantitative confirmation of the Rutherford formula. [verify]

7. Hofstadter, R., "Electron scattering and nuclear structure," *Reviews of Modern Physics* **28**, 214–254 (1956). Measurement of proton and nuclear charge radii using electron scattering — Born approximation (form factor) logic applied to determine the proton radius. Nobel Prize 1961. [verify]

8. Binghamton University QM II Notes, "Scattering from the Yukawa Potential," §13.8 [https://bingweb.binghamton.edu/~suzuki/QuantumMechanicsII/13-8%20Scattering%20from%20the%20Yukawa%20potential.pdf]. Supplementary worked derivation of the Yukawa Born integral. [verify URL active]

9. Sakurai, J. J. & Napolitano, J., *Modern Quantum Mechanics*, 3rd ed. (Cambridge, 2020), Ch. 6. Lippmann-Schwinger in bra-ket notation; T-matrix formalism; Born series. [verify edition]
