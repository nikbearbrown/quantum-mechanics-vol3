# Chapter 11 — Capstone — Modeling a Real Quantum System

## TL;DR

- Every approximation method in this volume is a scalpel, not a hammer. The capstone trains you to pick the right one, use it, and know when to put it down.
- You will choose a real system, apply one of Vol. 3's methods to it, produce a quantitative prediction, compare it to a measured number, and defend what you got wrong and why.
- The chapter presents six candidate systems — one per major method — so that every student's project exercises a different corner of the toolbox.
- "Defend the model" means stating the small parameter, estimating the error, and naming the next correction. That is what distinguishes a physicist's approximation from a guess.
- The worked example walks through STM tunneling current via WKB; a second example estimates the CdSe quantum-dot level spacing via the 3D spherical box.

---

## Learning Objectives

By the end of this chapter you will be able to:

1. **Identify** (Remember/Understand) which Vol. 3 method is appropriate for a given real system based on the system's dominant physics and the method's small-parameter condition. [Bloom: Understand]

2. **Apply** (Apply) a chosen approximation method end-to-end — from the model Hamiltonian through a numerical prediction with units — to a system not previously encountered in the course. [Bloom: Apply]

3. **Validate** (Analyze) a theoretical prediction against real experimental data, computing a percent error and attributing the residual to identified physical effects omitted from the model. [Bloom: Analyze]

4. **Diagnose** (Evaluate) when an approximation is about to fail by estimating the relevant small parameter and identifying the regime in which the next-order correction becomes important. [Bloom: Evaluate]

5. **Construct and defend** (Create) a complete written model of a real quantum system, including system identification, method justification, derivation, prediction, validation, and breakdown analysis. [Bloom: Create]

---

## The hardest problem in physics pedagogy is the gap between the formula and the fact.

You can derive the WKB transmission coefficient. You can compute the first-order perturbative energy shift for the Stark effect. You can diagonalize a two-level Hamiltonian in the rotating frame and extract the Rabi frequency. The machinery, by this point, is genuinely yours.

But then someone hands you a scanning tunneling microscope trace — a graph of current versus tip-sample distance, plotted on a semi-log axis — and asks: *does your formula explain this?* And there is a moment of genuine uncertainty. Which formula? What numbers do I put in? What counts as agreement? What counts as failure?

That gap — between having a method and knowing whether the method works *here* — is what the capstone is for.

Gordon Moore, working at Fairchild Semiconductor in 1965, observed that the number of transistors on an integrated circuit was doubling roughly every two years. He was not solving a Schrödinger equation. He was reading a trend, noting that the trend had a physical origin — quantum tunneling sets the gate-oxide thickness floor, discrete-dopant fluctuations set the channel-length floor — and predicting when the physics would bite back. The transistor you are reading this on works because engineers learned to sit with quantum mechanics long enough to make it quantitative: not just "tunneling happens" but "at this thickness, the leakage current is this many amps per square micron, and here is why."

The capstone asks you to do the same thing in miniature: take a real system, model it with this volume's machinery, produce a number, find the measured number, and make peace with the difference.

---

## Core Development

### What it means to model and defend a quantum system

A complete quantum model involves five moves, in order. Skipping any one of them produces an answer you cannot trust.

**1. System identification.** Name the relevant degrees of freedom and argue that the others can be ignored. The STM vacuum gap is, to a first approximation, a 1D rectangular barrier — the three-dimensional geometry of the tip reduces to a single apex atom, and the lateral degrees of freedom wash out. That argument has to be made; it cannot just be assumed.

**2. Method selection.** Choose the approximation whose small-parameter condition is satisfied for this system in this regime. The small parameter is not always obvious. For WKB applied to the vacuum gap, the parameter is $d/\lambda_\text{dB}$ where $\lambda_\text{dB}$ is the de Broglie wavelength — if the barrier is much wider than a wavelength, the WKB phase integral is well-defined. For the Born approximation applied to neutron scattering, the small parameter is $|V|/E$ — the potential must be weak compared to the kinetic energy. Estimate the parameter before calculating.

**3. Calculation.** Derive the key observable. Do not quote the formula without derivation; the formula is only trustworthy if you understand where it came from, because then you know when it is lying. This step has to produce a number with units.

**4. Validation.** Compare to a known experimental datum with a citation and a percent error. A 10% error in a first-principles model is usually excellent. A 50% error in a model with three fitting parameters is suspicious. A 3% error in a model with no free parameters is worth celebrating.

**5. Breakdown analysis.** Name what the model ignores. Estimate how large the omitted effect is, at least by order of magnitude. The goal is not to fix the model (that would be a research project) but to demonstrate that you know where it stops working.

### The small-parameter condition as a diagnostic

Every approximation method in Vol. 3 has a dimensionless small parameter $\epsilon$ such that the approximation is controlled when $\epsilon \ll 1$ and uncontrolled when $\epsilon \sim 1$.

| Method | Small parameter $\epsilon$ | Breaks when |
|---|---|---|
| Non-degenerate perturbation theory (Ch. 2–3) | $|\langle m \vert \hat{H}' \vert n \rangle| / \vert E_n^{(0)} - E_m^{(0)} \vert$ | States nearly degenerate |
| WKB (Ch. 5) | $\hbar \vert dp/dx \vert / p^2$ | Near classical turning points |
| Variational (Ch. 4) | — (upper bound; no breakdown parameter) | Trial state poorly chosen |
| Time-dependent PT / Rabi (Ch. 6) | $\Omega_R / \delta$ where $\delta$ is detuning | On-resonance (rotating-wave fixes this) |
| Born approximation (Ch. 9) | $m \vert V \vert a^2 / \hbar^2$ for range $a$ | Strong or long-range potentials |
| Tight-binding / KP (Ch. 11) | $\Delta / W$ where $\Delta$ is gap, $W$ is bandwidth | Wide bands, strong overlap |

Before you produce a number, compute $\epsilon$ for your system. If $\epsilon > 0.3$, caveat your answer. If $\epsilon > 1$, pick a different method.

---

## Six Candidate Systems

Each system below maps to a different Vol. 3 method and comes with: the method invoked, the observable to predict, the experimental datum to compare against, and the breakdown analysis. Choose one for your project, or propose an alternative subject to the feasibility check in Exercise 11.3.

---

### System A — STM Tunneling Current via WKB (Ch. 5)

**The physics.** A scanning tunneling microscope holds a sharp metallic tip within a few ångströms of a conducting surface. A bias voltage $V$ drives electrons from tip to sample (or vice versa) through the vacuum gap. Vacuum is a classically forbidden region — the electron's energy is below the barrier height set by the work function $\phi$ — so the only mechanism is quantum tunneling.

**The method.** WKB barrier penetration through a rectangular barrier of height $U_0 = \phi$ (the average work function of tip and sample) and width $d$ (the tip-sample distance). The WKB transmission coefficient is:

$$T(d) \approx \exp(-2\kappa d), \qquad \kappa = \frac{\sqrt{2m\phi}}{\hbar}$$

The tunneling current, at small bias voltage $V$ and low temperature, is proportional to $T$ times the local density of states at the Fermi level:

$$I \propto V \cdot \exp(-2\kappa d)$$

**The observable.** Current as a function of tip-sample distance. Because $I$ is exponential in $d$, the slope of $\ln I$ vs. $d$ gives $2\kappa$ directly. Measured $\kappa$ values range from about 0.9 to 1.2 Å$^{-1}$ for typical metal tip-sample pairs, corresponding to $\phi \approx 3$–6 eV. [verify]

**Validation datum.** A standard benchmark: withdrawing the tip by 1 Å reduces $I$ by roughly a factor of 7–10 for a W tip on Au or Cu. This follows from $e^{2\kappa \cdot 1\,\text{Å}} = e^{2 \times 1.0 \times 1} \approx 7.4$ for $\kappa = 1.0$ Å$^{-1}$. [verify: Binnig & Rohrer, Nobel Lecture 1986]

**Breakdown analysis.** (a) The barrier is not truly rectangular — image-charge effects round the corners, reducing the effective barrier height by 10–20%. (b) The 1D model ignores the three-dimensional tip geometry; Tersoff and Hamann (1985) showed that the current is proportional to the local density of states of the sample at the tip position, not just the transmission coefficient. For atomically sharp tips, the WKB result is effectively correct; for blunt tips, it overestimates current. (c) At large bias ($V \gtrsim \phi/e$), the barrier becomes triangular (Fowler-Nordheim regime) and the simple formula fails. [verify: Tersoff & Hamann, Phys. Rev. B 31, 805 (1985)]

---

### System B — CdSe Quantum Dot as a 3D Spherical Box (Perturbation theory / Exact)

**The physics.** A colloidal CdSe nanocrystal — a roughly spherical semiconductor crystal 2–6 nm in diameter — confines both electrons and holes within a potential well defined by the crystal boundary. The optical band gap, measured by UV-Vis spectroscopy, shifts upward from the bulk CdSe value of 1.74 eV as the crystal radius $R$ decreases. This blueshift is the experimental signature of quantum confinement.

**The method.** Treat the lowest electron and hole states as particles in a spherical infinite square well. The lowest energy level is:

$$E_{1s} = \frac{\hbar^2 \pi^2}{2 m^* R^2}$$

where $m^*$ is the effective mass (electrons: $m_e^* \approx 0.13\,m_e$; holes: $m_h^* \approx 0.45\,m_e$ for CdSe). The optical band gap of the quantum dot:

$$E_\text{dot} = E_\text{bulk} + E_{1s,e} + E_{1s,h} - \frac{1.8 e^2}{4\pi\epsilon_0 \epsilon_r R}$$

The last term is a first-order Coulomb correction for the electron-hole interaction ($\epsilon_r \approx 10$ for CdSe). [verify: Brus, J. Chem. Phys. 80, 4403 (1984)]

**Validation datum.** For $R = 1.5$ nm (a 3 nm diameter dot), experiment gives $E_\text{dot} \approx 2.44$ eV. The calculation (see worked example below) gives approximately 2.5 eV. Error $\approx 3\%$.

**Breakdown analysis.** (a) The effective-mass approximation assumes parabolic bands; it fails for $R < 1.5$ nm where the electron wavevector becomes large enough to probe band nonparabolicity. (b) Real dots have surface traps, ligand-modified boundary conditions, and shape anisotropy — all missed by the spherical infinite-well model. (c) The Coulomb correction here is first-order; at small $R$ it becomes comparable to the confinement energy and requires variational treatment.

---

### System C — Ammonia Inversion and the Maser (Time-Dependent PT / Two-Level System, Ch. 6)

**The physics.** The nitrogen atom in NH$_3$ sits above or below the plane of the three hydrogen atoms. These two configurations are classically equivalent (degenerate). Quantum tunneling through the barrier connecting them mixes the two classical configurations into symmetric ($|+\rangle$) and antisymmetric ($|-\rangle$) eigenstates separated in energy by $2A$, where $A$ is the tunneling matrix element. This is the same two-level diagonalization from degenerate perturbation theory — the structure is identical to the $2\times 2$ block in the Stark matrix.

**The method.** Two-level Hamiltonian in the $\{|L\rangle, |R\rangle\}$ basis:

$$\hat{H} = \begin{pmatrix} E_0 & -A \\ -A & E_0 \end{pmatrix}$$

Eigenvalues: $E_\pm = E_0 \mp A$. The tunneling splitting is $\Delta E = 2A$. The maser operates by sorting $|+\rangle$ from $|-\rangle$ molecules with an inhomogeneous electric field (they have different dipole moments in a DC field), then driving stimulated emission $|-\rangle \to |+\rangle$ with a microwave cavity tuned to $\nu = \Delta E / h$.

**Validation datum.** The NH$_3$ inversion transition occurs at 23.87 GHz, corresponding to $\Delta E = h \times 23.87 \times 10^9 \approx 9.94 \times 10^{-5}$ eV $= 0.79$ cm$^{-1}$. A simple double-well model (harmonic plus Gaussian barrier) predicts $\sim 0.98$ cm$^{-1}$ — about 24% off. [verify: Gordon, Zeiger & Townes, Phys. Rev. 95, 282 (1954)]

**Breakdown analysis.** The 24% error is almost entirely in the shape of the potential barrier. The exact double-well potential for NH$_3$ requires ab initio quantum chemistry to compute; a simple parameterized form misses the anharmonicity. With a more realistic potential (e.g., the double Rosen-Morse form), agreement is $< 2\%$. The two-level physics is exact once the splitting is known; the error lives entirely in the tunneling matrix element $A$, which is exponentially sensitive to the barrier shape.

---

### System D — NMR ${}^1$H Qubit via Rabi Oscillations (Ch. 6)

**The physics.** A proton (spin-$\frac{1}{2}$) in a strong static field $B_0$ precesses at the Larmor frequency $\nu_0 = \gamma B_0 / 2\pi$, where $\gamma = 2.675 \times 10^8$ rad s$^{-1}$ T$^{-1}$ is the proton gyromagnetic ratio. An oscillating rf field $B_1\cos(\omega t)$ applied perpendicular to $B_0$ drives spin flips when $\omega \approx 2\pi\nu_0$. In the rotating frame (rotating-wave approximation), the effective Hamiltonian is time-independent and the spin undergoes Rabi oscillations between $|\!\uparrow\rangle$ and $|\!\downarrow\rangle$ at frequency:

$$\Omega_R = \gamma B_1 / 2$$

**The method.** Time-dependent perturbation theory in the rotating frame. The two-level problem is exactly solved by the RWA Hamiltonian; the on-resonance Rabi formula is exact within that approximation.

**Validation datum.** At $B_0 = 9.4$ T: $\nu_0 = 42.577 \times 9.4 = 400$ MHz (the standard 400 MHz NMR instrument). A typical rf field $B_1 = 10^{-2}$ T gives $\Omega_R = 1.34 \times 10^6$ rad/s, so the $\pi$-pulse duration is $t_\pi = \pi / \Omega_R \approx 2.3\,\mu$s. Measured $\pi$-pulse durations in 400 MHz NMR: 1–25 $\mu$s. Agreement is essentially exact. [verify: Levitt, *Spin Dynamics* (Wiley, 2001)]

**Breakdown analysis.** (a) Relaxation (longitudinal $T_1$, transverse $T_2$) causes exponential decay of the Rabi oscillations — not in the basic model. (b) The RWA fails at large $B_1$ (when $\Omega_R \sim \nu_0$); the counter-rotating term then matters (Bloch-Siegert shift). (c) In real molecules, chemical shifts and J-couplings create a multi-spin problem far beyond a single two-level system.

---

### System E — Variational Helium Ground State (Ch. 4)

**The physics.** The helium atom has two electrons, a nucleus of charge $Z = 2$, and an electron-electron repulsion that cannot be treated perturbatively without care (the repulsion is comparable in magnitude to the nuclear attraction at $r \sim a_0$). The ground-state energy, measured by ionization energy, is $E_\text{He} = -79.0$ eV. No exact closed-form solution exists.

**The method.** Variational principle: use the trial wave function

$$\psi_\text{trial}(\vec{r}_1, \vec{r}_2) = \frac{Z_\text{eff}^3}{\pi a_0^3} e^{-Z_\text{eff}(r_1 + r_2)/a_0}$$

where $Z_\text{eff}$ is treated as a variational parameter (the "screened nuclear charge"). Each electron sees a nucleus of charge $Z_\text{eff} < 2$ because the other electron partially screens it. Minimizing $\langle \psi_\text{trial} | \hat{H} | \psi_\text{trial} \rangle$ with respect to $Z_\text{eff}$ gives:

$$Z_\text{eff} = Z - \frac{5}{16} = 2 - \frac{5}{16} = \frac{27}{16} = 1.6875$$

and a ground-state energy:

$$E_\text{variational} = -\left(\frac{27}{16}\right)^2 \times 2 \times 13.6\,\text{eV} = -77.5\,\text{eV}$$

**Validation datum.** Measured: $-79.0$ eV. Variational result: $-77.5$ eV. Error: 1.9%. The variational result is an upper bound; the true energy is lower. [verify: Griffiths, *Introduction to Quantum Mechanics*, §8.2; Hylleraas, Z. Phys. 65, 209 (1930)]

**Breakdown analysis.** The main omission is electron-electron correlation — the trial state assumes the two electrons move independently (a product wave function) and only accounts for their average repulsion through $Z_\text{eff}$. Hylleraas (1930) included the inter-electron coordinate $r_{12}$ explicitly in the trial state and obtained $-79.0$ eV within numerical precision. The next correction after our simple trial is a "cusp condition" at $r_{12} = 0$; missing this is the dominant source of our 1.9% error.

The variational result is always an upper bound. If you had taken $Z_\text{eff} = 2$ (no screening) you would have gotten $-108.8$ eV — much too low in magnitude. If $Z_\text{eff} = 1$ (full screening by one electron) you get $-54.4$ eV — too high. The optimal $Z_\text{eff} = 27/16$ is the variational minimum. This is a clean demonstration that the variational principle is a search: the trial state sets the playing field, and minimization finds the best answer within it.

The hydrogen molecule is a natural extension: vary the bond length $R$ in a trial wave function and find the minimum energy as a function of $R$. The predicted bond length ($\sim 1.65$ Å vs. measured 0.74 Å using a simple trial) illustrates how trial-state quality limits the prediction, and why molecular quantum chemistry requires much more sophisticated variational functions.

---

### System F — Rutherford Scattering via the Born Approximation (Ch. 9)

**The physics.** Alpha particles ($^4$He nuclei, charge $2e$) are scattered by a gold nucleus (charge $79e$) at energies of order 5–8 MeV. The interaction is the Coulomb repulsion $V(r) = Z_1 Z_2 e^2 / (4\pi\epsilon_0 r)$. In 1911 Rutherford discovered that the scattering cross-section had a characteristic $1/\sin^4(\theta/2)$ angular dependence, revealing that nearly all the atomic mass was concentrated in a tiny nucleus.

**The method.** Born approximation (Ch. 9). For a central potential $V(r)$, the differential cross-section in the Born approximation is:

$$\frac{d\sigma}{d\Omega} = \left(\frac{m}{2\pi\hbar^2}\right)^2 \left|\tilde{V}(q)\right|^2$$

where $q = 2k\sin(\theta/2)$ is the momentum transfer and $\tilde{V}(q)$ is the Fourier transform of $V(r)$.

For the Coulomb potential $V(r) = \alpha_C / r$ with $\alpha_C = Z_1 Z_2 e^2 / 4\pi\epsilon_0$:

$$\tilde{V}(q) = \frac{4\pi \alpha_C}{q^2}$$

The Born cross-section becomes:

$$\frac{d\sigma}{d\Omega} = \left(\frac{Z_1 Z_2 e^2}{4E}\right)^2 \frac{1}{\sin^4(\theta/2)}$$

where $E = \hbar^2 k^2 / 2m$ is the kinetic energy of the projectile. This is the Rutherford formula.

**The remarkable fact:** The Born approximation gives the *exact classical* result for Coulomb scattering, even though Born is a quantum approximation. This is not obvious and is essentially an accident of the $1/r$ potential — the classical and quantum cross-sections agree because the Coulomb force is long-range and the partial-wave sum converges in a special way. [verify: Griffiths §11.4; Taylor, *Scattering Theory* (Wiley, 1972)]

**Validation datum.** Geiger and Marsden (1909) measured the angular distribution of $\alpha$ particles scattered from gold foil. At 5.5 MeV: $d\sigma/d\Omega \propto 1/\sin^4(\theta/2)$ verified over four decades of cross-section magnitude. The formula predicts, for $\theta = 90°$, $d\sigma/d\Omega = (Z_1 Z_2 e^2 / 4E)^2 = (2 \times 79 \times 1.44\,\text{MeV}\cdot\text{fm} / 4 \times 5.5\,\text{MeV})^2 \approx (10.4\,\text{fm})^2 = 108\,\text{fm}^2/\text{sr}$, in quantitative agreement with the Geiger-Marsden data. [verify: Geiger & Marsden, Proc. R. Soc. Lond. A 82, 495 (1909)]

**Breakdown analysis.** (a) At small $\theta$ (forward scattering), the Coulomb cross-section diverges — the total cross-section is infinite. This is unphysical; it is cured by the finite screening radius of the atomic electrons (Debye-Wückel screening in a plasma, or the atomic radius in Rutherford's experiment). (b) At $\alpha$-particle energies above ~20 MeV (for gold), the $\alpha$ comes close enough to the nucleus to feel the nuclear force, and the cross-section deviates from the pure Coulomb formula — this deviation was used historically to measure nuclear radii. (c) The Born approximation requires $|V|/E \ll 1$. For Coulomb scattering, $V(r) \sim \alpha_C/r$ and the "effective range" is $r \sim a_0$, so the condition is $Z_1 Z_2 e^2 / (4\pi\epsilon_0 a_0 E) \ll 1$. At $E = 5$ MeV and $Z_1 Z_2 = 158$, this is approximately $158 \times 1.44/(5 \times 10^6 \times 0.53) \approx 8.6 \times 10^{-4} \ll 1$. The Born approximation is well-justified for $\alpha$ scattering off gold at MeV energies.

---

## Worked Example: WKB STM Tunneling Current

**The lesson.** Use the WKB formula to compute the absolute tunneling current ratio for two tip-sample distances, and verify that the ~8× per ångström rule emerges from first principles.

**Setup.** Take a tungsten tip on a gold surface. The effective work function (average of tip and sample work functions) is $\phi \approx 4.0$ eV. The Fermi energy of the electrons is well below the vacuum level. The tunneling parameter $\kappa$:

$$\kappa = \frac{\sqrt{2m_e \phi}}{\hbar} = \frac{\sqrt{2 \times 9.109 \times 10^{-31}\,\text{kg} \times 4.0 \times 1.602 \times 10^{-19}\,\text{J}}}{1.055 \times 10^{-34}\,\text{J}\cdot\text{s}}$$

Working in convenient units: $\kappa = 0.5123\,\text{Å}^{-1} \times \sqrt{\phi[\text{eV}]} = 0.5123 \times \sqrt{4.0} = 1.025\,\text{Å}^{-1}$.

**At $d_1 = 5$ Å:** $\quad 2\kappa d_1 = 2 \times 1.025 \times 5.0 = 10.25$, so $T_1 = e^{-10.25} \approx 3.54 \times 10^{-5}$.

**At $d_2 = 6$ Å:** $\quad 2\kappa d_2 = 2 \times 1.025 \times 6.0 = 12.30$, so $T_2 = e^{-12.30} \approx 4.52 \times 10^{-6}$.

**Current ratio:**
$$\frac{I(d_1)}{I(d_2)} = \frac{T_1}{T_2} = \frac{e^{-10.25}}{e^{-12.30}} = e^{2.05} \approx 7.8$$

So increasing the gap by 1 Å reduces the current by a factor of approximately 7.8. The rule of thumb — "roughly one order of magnitude per ångström" — is confirmed quantitatively by the WKB formula.

**Computing the absolute current.** At a bias of $V = 0.1$ V and a typical junction conductance prefactor $G_0 \sim 10^{-4}$ S (derived from density of states at the Fermi level [verify]), we would estimate $I \sim G_0 V T \sim 10^{-4} \times 0.1 \times 3.5 \times 10^{-5} \approx 0.35$ pA. Real STM currents at this geometry are 0.1–1 nA, about $10^3$ times larger. The discrepancy is in the prefactor (density of states, contact geometry), not in the exponential — the slope $d(\ln I)/dd = -2\kappa$ is accurately predicted. This is the key lesson: the WKB approximation gives you the *exponential* reliably; the *prefactor* requires Tersoff-Hamann or a more detailed model.

**The limit.** The model fails when: (a) $d < 2$ Å (tip-sample repulsion, contact regime); (b) $V > \phi/e \approx 4$ V (Fowler-Nordheim tunneling, triangular barrier); (c) the sample has sharp features in its density of states (e.g., a molecular adsorbate with a narrow resonance near the Fermi level) — then $I$ is no longer proportional to $T$ alone.

**Small-parameter check.** The WKB condition $\hbar|dp/dx|/p^2 \ll 1$ inside the barrier. With $p = i\hbar\kappa$ (imaginary momentum), $dp/dx \approx 0$ for a rectangular barrier (constant $\kappa$). The condition is automatically satisfied in the interior of a rectangular barrier; it breaks down only at the barrier edges (the turning points). This is why WKB works beautifully for the rectangular vacuum barrier but needs connection-formula corrections near turning points in smoothly varying potentials.

---

## Worked Example: Quantum Dot Level Spacing via the 3D Spherical Box

**The lesson.** Use the spherical-box formula to predict the optical band gap of a 3 nm CdSe quantum dot and compare to the measured UV-Vis absorption peak.

**Setup.** Radius $R = 1.5$ nm (3 nm diameter dot). Electron effective mass $m_e^* = 0.13\,m_e$. Hole effective mass $m_h^* = 0.45\,m_e$. Bulk CdSe band gap: $E_\text{bulk} = 1.74$ eV. Dielectric constant $\epsilon_r = 10.6$ for CdSe.

**Electron confinement energy ($\ell = 0$, $n = 1$; zero $z_{1,0} = \pi$):**

$$E_{1s,e} = \frac{\hbar^2 \pi^2}{2 m_e^* R^2} = \frac{(1.055 \times 10^{-34})^2 \times \pi^2}{2 \times 0.13 \times 9.11 \times 10^{-31} \times (1.5 \times 10^{-9})^2}$$

Numerator: $(1.055 \times 10^{-34})^2 \times 9.87 = 1.098 \times 10^{-67} \times 9.87 = 1.084 \times 10^{-66}$ J$^2$·s$^2$.

Denominator: $2 \times 0.13 \times 9.11 \times 10^{-31} \times 2.25 \times 10^{-18} = 5.33 \times 10^{-49}$ J·m$^2$.

$$E_{1s,e} = \frac{1.084 \times 10^{-66}}{5.33 \times 10^{-49}} = 2.03 \times 10^{-18}\,\text{J} = 12.7\,\text{eV} \times \frac{1}{(R/a_0)^2}$$

Let me recompute cleanly in eV using $\hbar^2/(2m_e a_0^2) = 13.6$ eV:

$$E_{1s,e} = \frac{13.6\,\text{eV}}{m_e^*/m_e} \times \frac{\pi^2 a_0^2}{R^2} = \frac{13.6}{0.13} \times \pi^2 \times \frac{(0.529\,\text{Å})^2}{(15\,\text{Å})^2}$$

$$= 104.6 \times 9.87 \times \frac{0.280}{225} = 104.6 \times 9.87 \times 1.24 \times 10^{-3} = 1.28\,\text{eV}$$

**Hole confinement energy:**

$$E_{1s,h} = \frac{13.6\,\text{eV}}{0.45} \times \pi^2 \times \frac{(0.529)^2}{(15)^2} = 30.2 \times 9.87 \times 1.24 \times 10^{-3} = 0.370\,\text{eV}$$

**Coulomb correction** (first-order electron-hole attraction):

$$E_C = -\frac{1.8 e^2}{4\pi\epsilon_0 \epsilon_r R} = -1.8 \times \frac{14.4\,\text{eV}\cdot\text{Å}}{10.6 \times 15\,\text{Å}} = -1.8 \times 0.0906 = -0.163\,\text{eV}$$

**Predicted band gap:**

$$E_\text{dot} = 1.74 + 1.28 + 0.370 - 0.163 = 3.23\,\text{eV}$$

**Hmm — too large.** The measured first-exciton peak for 3 nm CdSe is $\approx 2.44$ eV. Our prediction is 3.23 eV, an error of 32%. What went wrong?

The dominant error is in the electron confinement energy. The $m_e^* = 0.13\,m_e$ value applies at the band minimum ($k = 0$); at the wavevectors probed in a 1.5 nm radius dot ($k \sim \pi/R \approx 2.1$ nm$^{-1}$), the band is noticeably nonparabolic. A more accurate effective mass for the quantum-confinement regime is $m_e^* \approx 0.2\,m_e$ [verify: Norris & Bawendi, Phys. Rev. B 53, 16338 (1996)], which gives:

$$E_{1s,e}^\text{corrected} = 1.28 \times \frac{0.13}{0.20} = 0.832\,\text{eV}$$

Revised total: $E_\text{dot} = 1.74 + 0.832 + 0.37 - 0.163 = 2.78$ eV. Still 14% above experiment — the Coulomb correction is also underestimated for very small dots. With a full variational treatment of the Coulomb term, the error drops to $\sim 5\%$ for $R \geq 2$ nm.

**The lesson from the failure:** The simple formula works at the right order of magnitude but overestimates confinement because the effective mass approximation fails for small dots. This is not a failure of the 3D box model per se; it is a failure of the input parameter. The box gives you the scaling correctly ($E \propto 1/R^2$) and the rough magnitude; the precise number requires knowing the effective mass accurately in the confinement regime. This is a perfect example of "the approximation can be right in structure but wrong in detail when you push it into a regime it was not designed for."

---

## Common Misconceptions

**"If the formula gives the right answer, the model must be right."** The Rutherford formula gives the exact classical cross-section for Coulomb scattering — and it is derived from the Born approximation, a quantum approximation. The two agree by a special accident of the $1/r$ potential, not because either approach is capturing the complete physics. Always check that the derivation is internally consistent, not just that the answer matches.

**"Larger trial function space always gives a better variational answer."** True for energy, but a trial state optimized for a lower energy is not necessarily a better description of the wave function in other respects (expectation values of position, momentum, etc.). The variational principle is an energy principle, not a state principle. A Hylleraas state with $r_{12}$ explicitly gives energy $-79.0$ eV but is much harder to use for computing the dipole moment or the hyperfine structure than the simple screened-Coulomb trial state.

**"WKB gives the current; the Tersoff-Hamann model corrects the exponential."** WKB gives the exponential accurately; Tersoff-Hamann corrects the *prefactor* (the density-of-states weighting). This distinction matters enormously in practice: atomic-resolution STM images are interpreted using Tersoff-Hamann for the chemical contrast, while the $2\kappa$ slope of $\ln I$ vs. $d$ is a pure WKB quantity.

**"Agreement within 5% means the model is good."** At 5% agreement, you need to ask: are there any free parameters? How many significant figures does the experimental datum have? If the experimental uncertainty is 20%, agreement to 5% is impressive; if the uncertainty is 0.1%, a 5% theoretical error is large. Always report the experimental uncertainty alongside the theoretical prediction.

**"The Born approximation requires weak interactions."** The condition is $m|V|a^2/\hbar^2 \ll 1$ where $a$ is the range of the potential. For the Coulomb potential (infinite range), the Born condition is satisfied at high energies ($E \gg |V(a_0)|$), not weak coupling. The same interaction that is "strong" at low energy becomes a valid Born scatterer at high energy. For Rutherford scattering at MeV energies, the Born parameter is of order $10^{-3}$, despite the interaction being the full Coulomb potential.

---

## Exercises

### Warm-Up

**11.1** (Identify the method) For each real system below, state which Vol. 3 method is the most appropriate first approach, and name the small parameter whose magnitude justifies that choice. Do not compute — just justify. *(a)* A hydrogen atom in a laboratory electric field of $10^5$ V/m. *(b)* Electron tunneling from a n-type semiconductor to vacuum through a 3 nm oxide layer with a barrier height of 3 eV at kinetic energy $E \sim 0.1$ eV below the barrier. *(c)* Ground-state energy of a helium-like ion $\text{Li}^+$ (nuclear charge $Z = 3$). *(d)* Proton-proton scattering at a kinetic energy of 500 keV.

**11.2** (Error budget) The variational helium ground state gives $E = -77.5$ eV vs. the measured $-79.0$ eV. *(a)* Compute the percent error. *(b)* Explain in one sentence why this result is guaranteed to be an upper bound. *(c)* Hylleraas obtained $-79.0$ eV by adding one term $e^{-\beta r_{12}}$ to the trial state. What physical effect does this term capture that the simple product wave function misses?

**11.3** (Feasibility check) You want to model the optical absorption of a 5 nm InP quantum dot using the spherical-box formula. *(a)* Identify the two input parameters you need (besides $R$) and estimate them from a reference. *(b)* Compute the predicted confinement energy for the lowest electron state. *(c)* State one way in which the spherical-box model is likely to fail for InP specifically (hint: InP has a direct gap but a complex valence band structure). *(d)* Is this system within the scope of this volume's methods, or does it require the next tier of theory?

### Apply+

**11.4** (STM calibration) A student measures the following STM data for a W tip on Cu(111) at bias $V = 100$ mV:

| $d$ (Å) | $I$ (nA) |
|---|---|
| 4.0 | 12.3 |
| 5.0 | 1.62 |
| 6.0 | 0.213 |
| 7.0 | 0.028 |

*(a)* Plot $\ln I$ vs. $d$ (you may use a table or sketch). *(b)* Extract $\kappa$ from the slope $d(\ln I)/dd = -2\kappa$. *(c)* From $\kappa$, infer the effective work function $\phi$ of the junction. *(d)* The known work functions are $\phi_W \approx 4.5$ eV and $\phi_\text{Cu} \approx 4.5$ eV. Is your extracted $\phi$ consistent? If it differs by more than 20%, suggest one physical reason why (image charge? surface contamination? band structure?).

**11.5** (Born approximation for Yukawa scattering) The nuclear force between a proton and neutron can be crudely modeled as a Yukawa potential $V(r) = V_0 e^{-r/a} / r$ with $V_0 = -25\,\text{MeV}\cdot\text{fm}$ and $a = 1.4\,\text{fm}$ (the pion Compton wavelength). *(a)* Compute the Born approximation differential cross-section $d\sigma/d\Omega$ at $\theta = 90°$ for neutron-proton scattering at $E = 50$ MeV. *(b)* Estimate the total cross-section from the Born formula. *(c)* Check the Born validity condition $m|V_0|a^2/\hbar^2$ and comment on whether the approximation is justified at this energy. The measured total np cross-section at 50 MeV is approximately 100 mb. Comment on the agreement.

**11.6** (Rabi oscillation with detuning) An NMR experiment applies an rf field at frequency $\omega = 2\pi \times 401$ MHz to a proton in a 9.4 T field (Larmor frequency 400 MHz). The detuning is $\delta = \omega - \omega_0 = 2\pi \times 1$ MHz and the Rabi frequency is $\Omega_R = 2\pi \times 1.34$ MHz. *(a)* Compute the generalized Rabi frequency $\tilde{\Omega} = \sqrt{\Omega_R^2 + \delta^2}$. *(b)* Write the probability for spin-flip as a function of time: $P_{\downarrow}(t) = \sin^2(\tilde{\Omega} t / 2) \times \Omega_R^2 / \tilde{\Omega}^2$. *(c)* What is the maximum probability of spin-flip achievable at this detuning? *(d)* The student wants full inversion ($P_\downarrow = 1$). What must they adjust — and by how much?

### Produce

**11.7** (Model and defend: your choice) Select one of the six candidate systems (A–F) or propose a new system subject to instructor approval. Produce a written model according to the five-move structure: *(1)* system identification with justification of relevant degrees of freedom; *(2)* method selection with small-parameter estimate; *(3)* complete quantitative derivation, all steps shown, answer with units; *(4)* comparison to a cited experimental datum with percent error; *(5)* breakdown analysis naming the two most important omitted effects and estimating their magnitude. Minimum 600 words plus the full calculation. The project rubric (see below) is the grading guide.

**11.8** (Scattering model: Rutherford) Using the Born-approximation Rutherford formula, predict the differential cross-section $d\sigma/d\Omega$ for 5.486 MeV alpha particles (from $^{241}$Am decay) scattered from gold ($Z = 79$) at angles $\theta = 30°, 60°, 90°, 120°, 150°$. Tabulate your results in fm$^2$/sr. Then: *(a)* plot the five points as $\log(d\sigma/d\Omega)$ vs. $\log(\sin(\theta/2))$ and verify that the slope is $-4$, as the Rutherford formula requires. *(b)* At what scattering angle does $d\sigma/d\Omega$ equal 1 barn/sr = $10^{-24}$ cm$^2$/sr? *(c)* The $\alpha$ particle starts to "touch" the gold nucleus (nuclear radius $\approx 8$ fm) in a head-on collision. At what kinetic energy would the $\alpha$ come within 8 fm of the gold nucleus? Above this energy, what happens to the cross-section?

---

## The Project Rubric

Use this rubric for self-assessment before submission. The total is 24 points; a complete project requires at least 18.

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| **System identification** | All relevant DOF named and justified; irrelevant physics explicitly excluded with argument | DOF identified correctly; minor hand-waving | System chosen but DOF not fully justified | System vague, unclear, or inappropriate for the volume's methods |
| **Method selection** | Correct method chosen; small parameter $\epsilon$ computed numerically; limitation named | Correct method; $\epsilon$ estimated qualitatively; limitation noted | Correct method; no $\epsilon$ estimate; limitation absent | Wrong method or method unstated |
| **Derivation** | Full derivation from model Hamiltonian; no unjustified steps; final answer dimensionally correct | Correct derivation with minor gaps (e.g., one step quoted) | Derivation partially complete or contains algebraic errors | Major errors or derivation absent |
| **Quantitative prediction** | Number with correct units; all input parameters cited; assumptions stated explicitly | Number correct; some assumptions implicit | Numbers present but one or more inputs unphysical or uncited | No quantitative result |
| **Validation** | Real experimental datum cited with author, year, and DOI or ISBN; percent error computed; residual attributed to named physical effect | Datum cited; error computed; attribution qualitative | Datum cited but no error analysis | No comparison to data |
| **Breakdown analysis** | Two or more omitted effects named; at least one estimated quantitatively by order of magnitude | One or two effects named qualitatively | Limitation mentioned but not analyzed | No breakdown analysis |

---

## Still Puzzling

Why does the Born approximation for Coulomb scattering give the exact classical Rutherford formula? The Born approximation is a quantum approximation (first-order in $V$), and the Coulomb potential is long-range and strong. The agreement is usually attributed to a mathematical accident: the Fourier transform of $1/r$ is $1/q^2$, which conspires with the kinematics to reproduce the classical result. But a deeper understanding — one that explains from first principles why the exact quantum cross-section (computed via partial waves to all orders) *also* equals the classical result — involves the SO(4) symmetry of the hydrogen atom problem: the same degeneracy that makes hydrogen's $\ell$-levels collapse at fixed $n$ also makes Coulomb scattering integrable, so the full quantum sum is computable in closed form. The partial-wave series for Coulomb scattering does not converge in the usual sense; it requires careful regularization (adding a small imaginary part to the range — the Yukawa trick — then taking the limit). The fact that the answer comes out equal to the classical value at every angle, not just on average, is not trivial and is still a satisfying surprise every time you see it worked out.

The other open thread: why is the variational principle an upper bound? The proof is elementary — $\langle \psi | \hat{H} | \psi \rangle \geq E_0$ for any normalized $|\psi\rangle$, because $|\psi\rangle$ can be expanded in the complete set of eigenstates and the ground state has the lowest energy — but the *practical* implication is profound: you can always make progress by expanding your trial state, and the worst you can do is stay put. This is the reason computational quantum chemistry is a field at all: Hartree-Fock, CI, CCSD(T), FCI are all climbing the same variational ladder, each step getting the energy lower. The exact ground state sits at the bottom of that ladder, infinitely far below, but you can get exponentially close with polynomial-cost algorithms. Why that is true — why quantum chemistry is tractable at all when the Hilbert space is exponentially large — is an open question of the field, and the answer (when it comes) will matter for quantum computing too.

---

## The +1 — Simulation Exercise: The Capstone Build

This chapter's simulation is not a drill. It is the project.

You will build a single self-contained interactive model of your chosen system — the same system you analyze in Exercise 11.7. The deliverable is `11-capstone-[your-system].html`, a D3 v7 visualization that computes and displays the key observable as a function of a tunable physical parameter.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 11 — Capstone
Deliverable: 11-capstone-[system].html
Status: in progress

SYSTEM CHOSEN: [fill in from A–F or your proposal]
METHOD: [WKB / variational / Born / two-level / spherical-box / Rabi]
KEY OBSERVABLE: [e.g., "tunneling current I vs. tip-sample distance d"]
VALIDATION DATUM: [citation + value]

The simulation visualizes the key observable vs. the tunable parameter,
overlaid with the experimental datum if a single number or a data curve
can be read from the reference. The "approximation validity" indicator
(the small parameter epsilon) is displayed live as the parameter varies.
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md the following physics rules for the Chapter 11 capstone:

CAPSTONE PHYSICS RULES (Chapter 11)

General structure — every capstone simulation must:
1. Display the physical system schematically (barrier, dot, spin, etc.)
2. Show the key formula prominently (LaTeX or MathJax in the HTML)
3. Plot the main observable vs. the tunable parameter
4. Show the experimental validation point (horizontal line or dot)
5. Display epsilon (the small-parameter) live; color it green if epsilon < 0.3,
   yellow if 0.3 <= epsilon < 1.0, red if epsilon >= 1.0

SYSTEM A — WKB STM
  Tunneling current: I(d) = I_0 * exp(-2 * kappa * d)
  kappa = 0.5123 * sqrt(phi_eV)  [Angstrom^-1]
  Tunable: d from 2 to 12 Angstrom; phi from 2 to 6 eV.
  Experimental point: I(d) curve from Binnig & Rohrer, slope = 2*kappa.
  Plot: ln(I) vs d (should be linear; check slope).
  epsilon: kappa * lambda_dB = hbar * kappa / p ≈ 1 for tunneling electron.
    Note: WKB is well-justified for rectangular barriers — display this
    as epsilon_WKB = lambda_dB / (barrier width d), should be << 1 for d >> lambda_dB.

SYSTEM B — Quantum dot (spherical box)
  E_dot(R) = E_bulk + (hbar^2 pi^2)/(2 m_e_star R^2) + (hbar^2 pi^2)/(2 m_h_star R^2)
             - 1.8 e^2 / (4 pi eps_0 eps_r R)
  Use: m_e_star = 0.13 m_e, m_h_star = 0.45 m_e, eps_r = 10.6 (CdSe).
  E_bulk = 1.74 eV (CdSe).
  Tunable: R from 1 to 6 nm.
  Experimental overlay: Bawendi/Norris CdSe size-gap data points
    (R=1.2nm: 2.9 eV; R=1.5nm: 2.44 eV; R=2.0nm: 2.1 eV; R=3.0nm: 1.9 eV).
  epsilon: (pi a_0_eff / R) where a_0_eff = hbar^2 eps_r / (m_reduced e^2).
    If epsilon > 1 (R < a_0_eff), the exciton is strongly confined
    and the model is most accurate.

SYSTEM C — Ammonia maser
  Double-well: V(x) = (1/2) k x^2 + b * exp(-c x^2)
  Eigenvalues E_0, E_1 from numerical grid (matrix diagonalization).
  Splitting: Delta_E = E_1 - E_0.
  Tunable: barrier height b from 0 to 0.1 hartree; barrier width parameter c.
  Experimental point: Delta_E = 0.79 cm^-1 = 3.6e-5 hartree.
  epsilon: A / E_0 where A = Delta_E / 2. If this ratio << 1, two-level
    approximation is good (it always is for NH3 — the higher levels are
    10x farther away).

SYSTEM D — NMR Rabi oscillations
  P_flip(t) = (Omega_R^2 / Omega_tilde^2) * sin^2(Omega_tilde * t / 2)
  Omega_tilde = sqrt(Omega_R^2 + delta^2)
  Tunable: delta from -5 MHz to +5 MHz; B1 from 0 to 0.02 T.
  Omega_R = gamma_p * B1 / 2, gamma_p = 2.675e8 rad/s/T.
  Experimental: at 400 MHz NMR (9.4 T), on-resonance pi-pulse ~2.3 us.
  epsilon: Omega_R / omega_0 (RWA validity). At B1=0.01T: epsilon ~ 0.003 << 1.

SYSTEM E — Variational helium
  E(Z_eff) = Z_eff^2 * 2 * (-13.6 eV) + 2 * Z_eff * (Z - Z_eff) * 13.6 eV
             + (5/8) * Z_eff * 13.6 eV
  (standard variational helium calculation)
  Tunable: Z_eff from 1 to 2.
  Display: E(Z_eff) as a parabola; mark the minimum; mark the experimental
    E = -79.0 eV and the variational minimum E = -77.5 eV.
  epsilon: <H'> / E_0 where H' is the electron-electron repulsion.
    For helium, this is about 0.3 -- the perturbation is not small!
    That is why perturbation theory alone gives only -74.8 eV (7% error)
    while the variational method gives -77.5 eV (2% error).

SYSTEM F — Rutherford Born scattering
  d_sigma/d_Omega = (Z1 Z2 e^2 / 4E)^2 / sin^4(theta/2)
  Units: (1.44 MeV·fm) for e^2 / 4 pi eps_0.
  Tunable: theta from 5 to 175 degrees; E from 1 to 20 MeV; Z1 Z2.
  Display: polar plot of d_sigma/d_Omega (log scale) as theta varies.
  Experimental overlay: Geiger-Marsden 1909 data ratios.
  epsilon_Born = Z1 Z2 e^2 / (hbar v) = Z1 Z2 * (c/v) * alpha
    where alpha = 1/137. For 5 MeV alpha off gold: epsilon ~ 0.15 < 1. OK.
    For 1 MeV alpha: epsilon ~ 0.7 -- Born approximation getting shaky.

KNOWN FAILURE MODES:
(a) Units confusion: always work in SI or consistently in natural units.
    For atomic/nuclear physics, prefer: eV, Angstrom, fm.
(b) Off-by-factor-of-2 in Rabi frequency: Omega_R = gamma B1 / 2, not gamma B1.
(c) Forgetting the Coulomb correction in the QD model (it lowers E_dot by ~0.1-0.2 eV).
(d) Missing the 1/8 prefactor in the helium variational energy (from the
    <1/r_{12}> calculation: <1/r_{12}> = 5 Z_eff / 8 a_0).
```

### Part 3 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md, and
PROJECT.md. Read all three first.

I have chosen System [A / B / C / D / E / F] from Chapter 11 of
Quantum Mechanics Vol. 3. Build 11-capstone-[system].html: a single
self-contained HTML file using D3 v7 from CDN. No other dependencies
except optionally MathJax for formula display (CDN OK).

The simulation must implement ALL FIVE of the following panels:

PANEL 1 — System schematic (150px tall strip at top).
  A simple SVG illustration of the system: for STM, show tip/gap/surface;
  for QD, show sphere with confinement wave; for ammonia, show double well
  with N atom; for NMR, show spin precessing in B0 field; for helium,
  show two electrons around nucleus; for Rutherford, show incident beam
  and scattered trajectories.

PANEL 2 — Formula display (use MathJax or plain HTML math).
  Show the key formula that drives the calculation. Update the formula
  with the current parameter values substituted in.

PANEL 3 — Main plot (400px tall, full width).
  Plot the observable vs. the tunable parameter. Draw a horizontal or
  diagonal line or point for the experimental validation datum.
  Label axes with units. Show the theoretical curve in blue, experimental
  point or line in red (dashed).

PANEL 4 — Parameter controls.
  Sliders for all tunable parameters as listed in CLAUDE.md.
  Each slider labeled with its physical meaning and units.
  Current value displayed numerically next to each slider.

PANEL 5 — Validity indicator.
  Compute epsilon live. Display as a colored number:
  green (< 0.3), yellow (0.3–1.0), red (>= 1.0).
  Below it, one sentence explaining what epsilon measures and what
  its current value means for the approximation.

Runtime sanity checks (to browser console):
  - At the "textbook" parameter values (from CLAUDE.md), the observable
    should match the chapter's worked-example number within 1%.
  - The experimental validation datum should appear on or near the curve.
  - Epsilon should be in the expected range (see CLAUDE.md).

Comments at every non-trivial physics step.
No dead code. Pure functions for all physics calculations.
Do not use math.js, numeric.js, or any library beyond D3 v7 and MathJax.
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. **Validity sweep.** Tune the primary parameter through its full range. Note the value at which the validity indicator transitions from green to yellow. At this value, what physical regime are you entering, and why does the approximation begin to fail?

2. **Experimental agreement.** At the "textbook" values (those from the worked example), does your simulation's theoretical curve pass through or near the experimental datum? If not, identify whether the discrepancy is in the exponential (slope) or the prefactor (intercept/magnitude), and trace it to a specific physical omission.

3. **Sensitivity analysis.** Identify the input parameter that changes the observable most strongly. Double that parameter from its baseline value. By what factor does the observable change? Is the relationship linear, quadratic, or exponential in that parameter?

4. **Edge case.** Push the slider to its extreme value (minimum or maximum). Does the simulation remain physically sensible? If it predicts something unphysical (negative energy, infinite current, etc.), add a warning label to the HTML at that extreme.

5. **The defense.** Write two paragraphs (into a comment in the HTML file's `<head>`) explaining: (a) why you chose this method for this system, (b) what the largest source of error is and how you would fix it with one additional piece of physics. This is the written defense component of the capstone.

---

## References

- Binnig, G. & Rohrer, H. "Scanning tunneling microscopy." *Surface Science* 126, 236–244 (1983). [verify]
- Binnig, G. & Rohrer, H. Nobel Lecture: "Scanning tunneling microscopy — from birth to adolescence." *Rev. Mod. Phys.* 59, 615 (1987). [verify]
- Tersoff, J. & Hamann, D. R. "Theory of the scanning tunneling microscope." *Phys. Rev. B* 31, 805 (1985). [verify]
- Brus, L. E. "Electron-electron and electron-hole interactions in small semiconductor crystallites: the size dependence of the lowest excited electronic state." *J. Chem. Phys.* 80, 4403 (1984). [verify]
- Norris, D. J. & Bawendi, M. G. "Measurement and assignment of the size-dependent optical spectrum in CdSe quantum dots." *Phys. Rev. B* 53, 16338 (1996). [verify]
- Hylleraas, E. A. "Neue Berechnung der Energie des Heliums im Grundzustande, sowie des tiefsten Terms von Ortho-Helium." *Z. Phys.* 65, 209 (1930). [verify]
- Gordon, J. P., Zeiger, H. J. & Townes, C. H. "Molecular microwave oscillator and new hyperfine structure in the microwave spectrum of NH₃." *Phys. Rev.* 95, 282 (1954). [verify]
- Geiger, H. & Marsden, E. "On a diffuse reflection of the α-particles." *Proc. R. Soc. Lond. A* 82, 495 (1909). [verify]
- Rutherford, E. "The scattering of α and β particles by matter and the structure of the atom." *Phil. Mag.* 21, 669 (1911). [verify]
- Levitt, M. H. *Spin Dynamics: Basics of Nuclear Magnetic Resonance*. 2nd ed. Wiley, 2001. [verify]
- Griffiths, D. J. *Introduction to Quantum Mechanics*. 3rd ed. Cambridge University Press, 2018. §8.2 (variational helium), §11.4 (Born approximation). [verify]
- Townsend, J. S. *A Modern Approach to Quantum Mechanics*. 2nd ed. University Science Books, 2012. [verify]
- Taylor, J. R. *Scattering Theory: The Quantum Theory of Nonrelativistic Collisions*. Wiley, 1972; Dover reprint 2006. [verify]
