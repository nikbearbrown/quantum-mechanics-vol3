# Chapter 4 — The WKB Approximation and Tunneling

Polonium-212 has a halflife of about $3\times10^{-7}$ seconds — it decays almost instantly on any human timescale. Thorium-232 has a halflife of about $1.4\times10^{10}$ years — longer than the current age of the universe. Both decay by emitting the same particle through the same mechanism: an alpha particle that escapes a nucleus by tunneling through a Coulomb barrier.

The ratio of their halflives is roughly $10^{24}$. Twenty-four orders of magnitude, from one mechanism.

In 1911, Hans Geiger and John Nuttall found that for alpha emitters the logarithm of the halflife is approximately linear in $1/\sqrt{E_\alpha}$ — a clean empirical line. The observation was precise. The explanation was completely absent. [verify: Geiger & Nuttall, Phil. Mag. 22, 613 (1911)]

The difficulty: an alpha particle approaching the boundary of a nucleus from the inside sees a potential barrier. The barrier height is around 30 MeV. The emitted alpha has around 5 MeV. Classically, the alpha is stuck — it cannot escape over the top. And yet out it comes.

In the summer of 1928, George Gamow in Göttingen computed the probability of the alpha tunneling through the Coulomb barrier using the brand-new tools of wave mechanics. Within days, Ronald Gurney and Edward Condon at Princeton published the same idea independently. [verify] Both found the same answer: the tunneling probability is exponentially sensitive to barrier height, width, and particle energy. That exponential sensitivity is the source of the 24-decade dynamic range. The Geiger-Nuttall line is a plot of that exponent as a function of alpha energy.

This chapter builds the machinery that produces that result.

---

## The WKB Ansatz

The time-independent Schrödinger equation in one dimension is

$$-\frac{\hbar^2}{2m}\psi'' + V(x)\psi = E\psi.$$

Define the local classical momentum $p(x) = \sqrt{2m(E - V(x))}$, real in the classically allowed region ($E > V$), imaginary in the forbidden region ($E < V$). Write the wave function as $\psi(x) = e^{iS(x)/\hbar}$ — an exact rewriting, not yet an approximation. Substituting:

$$\frac{(S')^2}{2m} - \frac{i\hbar}{2m}S'' = E - V(x).$$

Now expand $S$ in powers of $\hbar$: $S = S_0 + (\hbar/i)S_1 + \cdots$ At zeroth order: $(S_0')^2/2m = E - V$, so $S_0'(x) = \pm p(x)$. At first order: $S_1 = \frac{i}{2}\ln p + \text{const}$.

Assembling the leading two terms in the classically allowed region:

$$\psi_\text{WKB}(x) \approx \frac{C}{\sqrt{p(x)}}\,\exp\!\left[\frac{i}{\hbar}\int p\,dx'\right] + \frac{D}{\sqrt{p(x)}}\,\exp\!\left[-\frac{i}{\hbar}\int p\,dx'\right],$$

and in the forbidden region where $p = i|p|$:

$$\psi_\text{WKB}(x) \approx \frac{A}{\sqrt{|p(x)|}}\,\exp\!\left[\frac{1}{\hbar}\int|p|\,dx'\right] + \frac{B}{\sqrt{|p(x)|}}\,\exp\!\left[-\frac{1}{\hbar}\int|p|\,dx'\right].$$

**The $1/\sqrt{p}$ factor has a physical meaning.** The classical probability of finding the particle near $x$ is proportional to the time it spends there — proportional to $1/v \propto 1/p$. So $|\psi|^2 \propto 1/p$: the wave function is large where the classical particle moves slowly, small where it moves fast. The amplitude tracks classical mechanics; the phase oscillates quantum-mechanically. This is the precise sense in which the approximation is "semiclassical."

The expansion is controlled by $\hbar$ relative to the classical action $\int p\,dx$. When $\int p\,dx \gg \hbar$ — when the particle traverses many de Broglie wavelengths — the higher-order terms are small and the approximation is reliable.

---

## Validity and Its Failure

Working through the algebra, the condition for the WKB expansion to be controlled reduces to

$$\left|\frac{d\lambda_\text{dB}}{dx}\right| \ll 1,$$

where $\lambda_\text{dB}(x) = h/p(x)$ is the local de Broglie wavelength. The potential must vary slowly on the scale of one wavelength.

This condition fails exactly at a **classical turning point** $x_0$ where $E = V(x_0)$ and $p(x_0) \to 0$. As the particle slows, $\lambda_\text{dB}$ grows without bound. The $1/\sqrt{p}$ prefactor diverges. The WKB forms on each side cannot be matched naively.

**The fix: Airy functions.** Near the turning point, linearize: $V(x) \approx V(x_0) + V'(x_0)(x-x_0)$. The Schrödinger equation reduces to $\psi'' = z\psi$ where $z \propto (x - x_0)$ — the **Airy equation**. The regular solution $\text{Ai}(z)$ oscillates on the allowed side and decays on the forbidden side:

$$\text{Ai}(z) \sim \begin{cases} \frac{1}{2\sqrt{\pi}}|z|^{-1/4}\cos\!\left(\tfrac{2}{3}|z|^{3/2} - \tfrac{\pi}{4}\right) & z\to-\infty \\ \frac{1}{2\sqrt{\pi}}z^{-1/4}e^{-\frac{2}{3}z^{3/2}} & z\to+\infty \end{cases}.$$

The $\pi/4$ phase shift on the allowed side is the **Maslov index** — a topological fact about the connection across a turning point, not a fitting parameter. Each turning point contributes this phase shift. Matching the Airy asymptotics to the WKB solutions on each side gives the connection formulas that thread solutions through the turning points.

---

## Bound States: Bohr-Sommerfeld

A particle bound between two classical turning points $a$ and $b$ oscillates inside and decays outside. Threading the WKB solution through both turning points, applying the connection formula at each, and demanding a self-consistent solution gives the **Bohr-Sommerfeld quantization condition**:

$$\boxed{\oint p(x)\,dx = 2\int_a^b p(x)\,dx = \left(n + \frac{1}{2}\right)h, \quad n = 0, 1, 2, \ldots}$$

The $1/2$ is the combined Maslov correction from both turning points ($\pi/4$ each, totaling $h/2$). The original 1913-1916 Bohr-Sommerfeld rule had $nh$ with no correction; the right $n + 1/2$ emerges from the Airy analysis.

**A remarkable special case.** For the harmonic oscillator $V = \frac{1}{2}m\omega^2 x^2$, the classical orbit at energy $E$ is an ellipse in phase space with area $2\pi E/\omega$. The condition gives:

$$\frac{2\pi E}{\omega} = \left(n+\frac{1}{2}\right)h \quad\Longrightarrow\quad E_n = \left(n+\frac{1}{2}\right)\hbar\omega.$$

This is the *exact* quantum-mechanical spectrum — not an approximation. The same exactness holds for the Coulomb potential and hydrogen. These are potentials with hidden algebraic symmetries (the Fock $\mathrm{SU}(2)$ symmetry for the oscillator, the Runge-Lenz vector for hydrogen) that cause the WKB expansion to terminate. For most other potentials, Bohr-Sommerfeld is a leading-order estimate that improves at large $n$.

The $1/2$ in the Bohr-Sommerfeld condition is not a small correction. For $n = 0$, it is the only term — without it, the predicted ground-state energy is zero. The zero-point energy of the harmonic oscillator is a Maslov correction.

---

## Worked Example — WKB Tunneling and Rectangular Barrier

**Part I: Quantitative comparison.** An electron ($m_e = 9.11\times10^{-31}$ kg) with kinetic energy $E = 1$ eV hits a rectangular barrier of height $V_0 = 5$ eV and width $L = 5$ Å.

Compute $\kappa = \sqrt{2m_e(V_0-E)}/\hbar$: with $V_0 - E = 4$ eV,

$$\kappa = \frac{\sqrt{2\times9.11\times10^{-31}\times4\times1.6\times10^{-19}}}{1.055\times10^{-34}} \approx 1.02\ \text{Å}^{-1}.$$

The Gamow factor: $\gamma = \kappa L = 1.02\times5 = 5.10$. The WKB transmission coefficient:

$$T_\text{WKB} = e^{-2\gamma} = e^{-10.2} \approx 3.7\times10^{-5}.$$

The exact result from matching boundary conditions:

$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}\right]^{-1} \approx 9.5\times10^{-5}.$$

The ratio is $T_\text{exact}/T_\text{WKB} \approx 2.56$. The analytical prediction for this prefactor is $16E(V_0-E)/V_0^2 = 16\times1\times4/25 = 2.56$. Agreement within rounding.

WKB nails the exponent. It misses the prefactor $16E(V_0-E)/V_0^2$ by an $O(1)$ factor that depends smoothly on $E/V_0$. On a log plot, $T_\text{exact}$ and $T_\text{WKB}$ run parallel — same slope, constant offset. For physics that spans 24 orders of magnitude, the $O(1)$ prefactor is invisible.

**Limit of validity:** when $E \to V_0$, $\kappa \to 0$, $T \to 1$, and the WKB tunneling formula breaks down. The exact result interpolates smoothly through the barrier top; WKB has a kink there. The approximation applies when $\kappa L \gg 1$ — deep sub-barrier tunneling.

**Part II: Bohr-Sommerfeld for a linear potential.** The "bouncing ball" potential $V(x) = mgx$ for $x > 0$ with a hard wall at $x = 0$. The hard wall contributes a Maslov phase of $\pi/2$ (equivalent to $1/2$) rather than $\pi/4$ — because it reflects with no penetration, unlike a smooth turning point. The smooth turning point at $x_0 = E/(mg)$ contributes $\pi/4$ as usual. The combined factor gives $3/4$ instead of $1/2$ on the right side of the quantization condition:

$$\int_0^{x_0}\sqrt{2m(E-mgx)}\,dx = \left(n + \frac{3}{4}\right)\frac{h}{2}.$$

Working through the integral: $E_n \propto (n + 3/4)^{2/3}$. This matches the exact results in terms of zeros of the Airy function $\text{Ai}$ to better than 1% even for $n = 0$.

---

## The Gamow Factor

A particle with energy $E$ encounters a barrier $V(x) > E$ between turning points $a$ and $b$. Threading through the connection formulas and computing the ratio of transmitted to incident probability current, the transmission coefficient is:

$$\boxed{T \approx e^{-2\gamma}, \qquad \gamma = \frac{1}{\hbar}\int_a^b\sqrt{2m(V(x)-E)}\,dx.}$$

The integral $\gamma$ is the **Gamow factor**. Three things follow immediately.

First, $T$ is *exponential* in $\gamma$. A small change in barrier height, width, or particle energy gets amplified into a large change in $T$. This is the source of the 24-decade dynamic range in alpha-decay halflives.

Second, the barrier shape enters automatically. Any $V(x)$ gets the same treatment — just integrate $\sqrt{2m(V-E)}$ over the forbidden region. Rectangular, triangular, parabolic, Coulomb — all handled by the same formula.

Third, in the thick-barrier limit $\gamma \gg 1$, the exponential carries essentially all the information. The $O(1)$ prefactors from connection-formula details are swamped by the exponential.

---

## Alpha Decay and the Geiger-Nuttall Law

Model an alpha particle as a pre-formed cluster inside a heavy nucleus. Inside ($r < R$, nuclear radius), the strong force holds it. Outside, it sees the Coulomb repulsion from the daughter nucleus with charge $Z' = Z - 2$:

$$V(r) = \frac{2Z'e^2}{4\pi\epsilon_0 r}, \quad r > R.$$

The barrier extends from $r = R$ out to the classical turning point $r_c = 2Z'e^2/(4\pi\epsilon_0 E_\alpha)$. For uranium-238 ($Z' = 90$, $E_\alpha \approx 4.2$ MeV, $R \approx 7.4$ fm), $r_c \approx 60$ fm — the alpha must tunnel through a barrier eight times the nuclear diameter.

The Gamow integral over the Coulomb barrier evaluates (via the substitution $r = r_c\sin^2\theta$) in the limit $R \ll r_c$ to a leading term proportional to $Z'/\sqrt{E_\alpha}$. Taking the logarithm of the halflife $\tau_{1/2} \sim \nu_0^{-1}e^{2\gamma}$, where $\nu_0 \sim 10^{21}$ Hz is the attempt frequency:

$$\log_{10}\tau_{1/2} \approx A(Z') + \frac{B(Z')}{\sqrt{E_\alpha}}.$$

This is the **Geiger-Nuttall law**: log halflife linear in $1/\sqrt{E_\alpha}$ for fixed daughter charge. The empirical observation from 1911 is derived from the WKB tunneling formula. Every point on the Geiger-Nuttall line is a different nuclide; every nuclide lies on the same straight line.

**Numerics for $^{238}$U.** With the numbers above: $\gamma \approx 43$, $e^{-2\gamma} \approx 4\times10^{-38}$, halflife estimate roughly $5\times10^8$ years. The experimental value is $4.5\times10^9$ years — off by a factor of 10. On a quantity spanning $10^{24}$, this is excellent. The remaining discrepancy comes from the alpha pre-formation probability and from the prefactors we dropped.

---

## The Exponential in Other Contexts

The Gamow factor is not specific to nuclear physics. The same structure runs through an unexpectedly wide range of phenomena.

**Scanning tunneling microscope.** A metal tip held a few ångströms above a conducting surface. Electrons tunnel through the vacuum gap; the current goes as $I \propto e^{-2\kappa d}$ where $\kappa \approx 1$ Å$^{-1}$ for a typical work function of 4-5 eV. A 1 Å change in tip-surface distance changes the current by $e^2 \approx 7$. A surface feature of sub-ångström height produces a measurable current swing. This is why an STM can image individual atoms: the exponential transduction turns atomic-scale topography into macroscopic current variation. [verify: Binnig & Rohrer, PRL 49, 57 (1982)]

**Stellar fusion.** In the solar core at $kT \sim 1$ keV, the proton-proton Coulomb barrier is of order 1 MeV. Most fusion occurs at the **Gamow peak energy** $E_G$, where the Maxwell-Boltzmann thermal tail (growing with $E$) and the Gamow tunneling factor (decreasing with $E$) together peak. For solar conditions, $E_G \approx 6$ keV — six times $kT$. Every star burns by tunneling. [verify: Atkinson & Houtermans, Z. Phys. 54, 656 (1929)]

**Flash memory.** Electrons tunnel through a thin SiO$_2$ layer under a high electric field, giving a triangular barrier — Fowler-Nordheim tunneling. The write speed and data retention time of every USB stick are controlled by the Gamow factor for that triangular barrier. [verify: Fowler & Nordheim, Proc. R. Soc. A 119, 173 (1928)]

**Cold fusion falsification.** Martin Fleischmann and Stanley Pons claimed in 1989 to have achieved deuterium-deuterium fusion at room temperature. The Gamow factor at $kT \approx 0.025$ eV for a D-D Coulomb barrier: $\gamma \sim 1000$, so $e^{-2\gamma} \sim 10^{-900}$. Even a factor of $10^{50}$ enhancement from the palladium lattice leaves the claim short by $10^{850}$. The calculation takes five minutes. Knowing how to compute a Gamow factor is sufficient to quantitatively evaluate any claim of "novel nuclear effects at ambient conditions."

---

## The Langer Correction for 3D

In three dimensions, the radial Schrödinger equation for $u(r) = rR(r)$ with angular momentum $\ell$ is

$$-\frac{\hbar^2}{2m}u'' + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u = Eu.$$

This looks like a 1D problem with effective potential $V_\text{eff} = V + \hbar^2\ell(\ell+1)/(2mr^2)$, and one might apply WKB directly. But near $r = 0$ the centrifugal term diverges and the validity condition fails. The correct semiclassical quantization requires the **Langer correction**: replace $\ell(\ell+1)$ by $(\ell+\frac{1}{2})^2$:

$$2\int_{r_1}^{r_2}\sqrt{2m\!\left[E - V(r) - \frac{\hbar^2(\ell+\frac{1}{2})^2}{2mr^2}\right]}\,dr = \left(n_r + \frac{1}{2}\right)h.$$

The correction accounts for the additional phase accumulated near the origin, where the centrifugal barrier acts as a hard wall with a half-integer Maslov contribution. [verify: Langer, Phys. Rev. 51, 669 (1937)]

For the Coulomb potential, the Langer-corrected condition gives the exact hydrogen energy levels $E_n = -13.6$ eV$/n^2$. Without the correction, the $\ell = 0$ states are wrong. The correction matters primarily for low-$\ell$ states and is negligible for high-$\ell$ states at large radii, where $\ell(\ell+1) \approx (\ell+\frac{1}{2})^2$ already.

---

## Still Puzzling

**How long does a particle spend inside the barrier?**

This question is surprisingly hard — not for computational reasons, but because there are at least four distinct definitions of "tunneling time" in the literature: the dwell time, the phase time (group delay), the Büttiker-Landauer traversal time, and the Larmor clock time. Each is operationally meaningful in a specific experimental context; none is obviously the right one, and they give different numerical answers.

Recent attosecond-streaking experiments have measured something at the attosecond scale for laser-induced ionization. Eckle and collaborators in 2008 reported an upper bound on the tunneling time consistent with zero or a very short traversal — with active debate over which definition is being measured. [verify: Eckle et al., Science 322, 1525 (2008)]

The pop-science answer — "the particle borrows energy from the vacuum briefly, allowed by the uncertainty principle" — is wrong. Energy is conserved at every measurement. There is no energy borrowing. There is just the wave, decaying through the forbidden region and emerging on the other side.

The WKB formalism of this chapter gives you $T$ but does not give you a tunneling time. This is a genuine open problem.

---

## The +1 — Simulation Exercise

The deliverable is `05-tunneling-simulator.html`: a D3 simulator with three modes — a stationary $T(E)$ comparison, a WKB barrier-shape explorer, and an animated Gaussian wave packet evolved by Crank-Nicolson.

### The Simulation Prompt

````
You are working in my directory which contains CLAUDE.md, DESIGN.md, and
PROJECT.md. Read all three first.

Build 05-tunneling-simulator.html: a single self-contained HTML file
using D3 v7 from a CDN (https://cdn.jsdelivr.net/npm/d3@7) and
d3-simple-slider (https://cdn.jsdelivr.net/npm/d3-simple-slider).
No other dependencies. Three modes selectable by tabs:
"Stationary T(E)", "WKB barrier shape", and "Wave packet (CN)".

STATIONARY T(E) MODE
Single SVG 1100 × 600. Plot T vs. E/V_0 on a LOG y-axis from 10^-12 to 1.
X-axis: E/V_0 from 0 to 2.5 (sub-barrier AND above-barrier).
Two curves:
  - T_exact (solid black): use the exact rectangular barrier formula
    T_exact = 1 / (1 + V_0^2 * sinh^2(kappa*L) / (4*E*(V_0-E)))
    for E < V_0; for E > V_0 use the over-barrier formula with sin^2.
  - T_WKB (dashed teal): T_WKB = exp(-2*kappa*L) for E < V_0;
    T_WKB = 1 for E > V_0 (WKB gives perfect transmission above barrier).
Vertical reference line at E/V_0 = 1 labeled "barrier top".
Controls: V_0 slider (1 to 10 eV), L slider (1 to 10 Angstrom).

WKB BARRIER SHAPE MODE
SVG 1100 × 600 split into two panels.
Left (550 wide): Draw V(x), shade region V(x) > E, draw horizontal line at E.
Right (550 wide): Plot T_WKB(E) vs E on LOG y-axis from 10^-12 to 1.
Compute T_WKB numerically: for each E, find turning points a and b by
bisection, then integrate gamma = (1/hbar) * integral_a^b sqrt(2m(V-E)) dx
by Simpson's rule on 500 sub-points.
Barrier shapes (selector): Rectangular, Triangular, Parabolic,
Double barrier (watch for resonant tunneling peaks T -> 1).
Controls: V_0, L, W (gap for double barrier), shape selector.

WAVE PACKET (CRANK-NICOLSON) MODE
SVG 1100 × 600. Spatial grid: 500 points x = -50 to +50 (natural units hbar=m=1).
Barrier at x=0 (rectangular, height V_0, width L).
Initial Gaussian: psi(x,0) = (2*pi*sigma_x^2)^(-1/4) * exp(-(x-x0)^2/(4*sigma_x^2))
  * exp(i*p0*(x-x0)), with x0=-20, sigma_x=2, p0=2 (default).

Evolve by Crank-Nicolson:
  (1 + i*H*dt/2) psi(t+dt) = (1 - i*H*dt/2) psi(t)
where H is the discretized 1D Hamiltonian (tridiagonal).
Use Thomas algorithm for the tridiagonal solve (implement in ~25 lines of
pure JS; no library).

Absorbing boundaries: imaginary potential V_abs = -i*V_max*f(x) where
f(x) ramps quadratically from 0 at x=±40 to V_max at x=±50.

Plot |psi(x,t)|^2 as filled blue area; V(x) as translucent gray behind it.
Display current t, norm integral sum|psi|^2*dx.
Pre-compute 2000 time steps at dt=0.05 on Play; cache and play at 60fps.
Show progress bar during computation.
Controls: V_0, L, p0, sigma_x sliders; Play/Pause/Reset.

PHYSICS
Natural units (hbar=m=1) throughout. For stationary mode, restore physical
units (m=9.11e-31 kg, hbar=1.055e-34 J*s) for display.
Runtime sanity checks to console:
  - Stationary at E/V_0=0.5, V_0=5 eV, L=5 Ang: T_exact~9.5e-5, T_WKB~3.7e-5.
  - Wave packet norm = 1.000 before reaching barrier.
  - For V_0=0, norm stays 1 throughout (no absorption needed).

Comments at every non-trivial physics step.
````

### Exploration Tasks

**Ground the WKB approximation.** Stationary mode, $V_0 = 5$ eV, $L = 5$ Å. At $E/V_0 = 0.5$, read the offset between exact and WKB curves on the log axis. Verify it matches $16E(V_0-E)/V_0^2 \approx 2.56$.

**Doubling the barrier.** Double $L$ from 5 to 10 Å. By what factor does $T$ at $E/V_0 = 0.5$ change? Verify against $e^{-2\kappa L}$: doubling $L$ should square the exponential suppression.

**Resonant tunneling.** Barrier-shape mode, double-barrier configuration. Find a resonant peak where $T \to 1$. The resonance condition is that the inter-barrier well supports a quasi-bound state; the resonant energy should match square-well bound states in the gap.

**Wave packet splitting.** Wave packet mode, $V_0 = 5$, $L = 5$, $p_0 = 2$ (so $E = 2 < V_0$). Play. Watch the packet split: most reflects, a small transmitted piece emerges on the right. Increase $p_0$ to $\sqrt{10}$ (so $E = V_0$), then to 4 ($E > V_0$). Describe how the transmitted fraction changes across these three cases.

---

## References

- Gamow, G. (1928). "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik*, 51, 204–212. [verify]
- Gurney, R.W. and Condon, E.U. (1928). "Wave Mechanics and Radioactive Disintegration." *Nature*, 122, 439. [verify]
- Geiger, H. and Nuttall, J.M. (1911). "The ranges of the α particles from various radioactive substances." *Philosophical Magazine*, 22, 613–621. [verify]
- Langer, R.E. (1937). "On the connection formulas and the solutions of the wave equation." *Physical Review*, 51, 669–676. [verify]
- Binnig, G. and Rohrer, H. (1982). "Scanning tunneling microscopy." *Physical Review Letters*, 49, 57–61. [verify]
- Atkinson, R. and Houtermans, F.G. (1929). "Zur Frage der Aufbaumöglichkeit der Elemente in Sternen." *Zeitschrift für Physik*, 54, 656–665. [verify]
- Fowler, R.H. and Nordheim, L. (1928). "Electron Emission in Intense Electric Fields." *Proceedings of the Royal Society A*, 119, 173–181. [verify]
- Eckle, P. et al. (2008). "Attosecond Ionization and Tunneling Delay Time Measurements in Helium." *Science*, 322, 1525–1529. [verify]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §9.1–9.3. [verify]
- Bender, C.M. and Orszag, S.A. (1978). *Advanced Mathematical Methods for Scientists and Engineers*. McGraw-Hill. Ch. 10. [verify]

---

*Chapter 5 follows: the variational principle. If perturbation theory requires a small correction to a known solution, the variational method requires only a guess — and guarantees that the guess is an upper bound on the ground-state energy. It is the method of choice when the perturbation is not small.*
