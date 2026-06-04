# Chapter 10 — Periodic Potentials and the Band Structure of Solids

Here is the strange fact at the heart of solid-state physics: a perfectly periodic potential does not scatter electrons. Put an electron in a crystal — a lattice of $10^{23}$ ions repeating every few ångströms — and rather than bouncing off every atom, the electron propagates through the entire crystal without deflection, as a modified plane wave. Real resistivity comes from imperfections: defects, impurities, vibrations (phonons) that break the periodicity. A perfect crystal at zero temperature has zero electrical resistance.

The reason is Bloch's theorem, and understanding it unlocks the entire structure of solid-state physics: bands, gaps, metals, insulators, semiconductors. This chapter builds the framework in one dimension, where the geometry is transparent.

---

## The Geometry

Before the quantum mechanics, two paragraphs on the geometry.

**The direct lattice.** A one-dimensional crystal is an atom (or group) repeated with period $a$. Lattice positions are $x_n = na$ for integers $n$. The lattice constant $a$ is typically 2–6 Å for real materials.

**The reciprocal lattice.** Every periodic structure has a dual: the reciprocal lattice at spatial frequencies $G_n = 2\pi n/a$. The **first Brillouin zone** (BZ) is the interval $k \in [-\pi/a, \pi/a]$. Bloch's theorem will show that $k$ and $k + G$ describe the same physical state, so all distinct crystal momenta fit inside one BZ.

---

## Bloch's Theorem

Consider an electron in a potential $V(x)$ satisfying $V(x+a) = V(x)$.

Define the **translation operator** $\hat{T}_a$ by $(\hat{T}_a f)(x) = f(x+a)$. Because the potential is periodic, $[\hat{H}, \hat{T}_a] = 0$: energy eigenstates can be chosen to simultaneously be eigenstates of $\hat{T}_a$. Since translation is unitary, its eigenvalues have magnitude 1 and can be written as $e^{ika}$ for real $k$:

$$\psi(x+a) = e^{ika}\psi(x).$$

Any state satisfying this condition can be written as

$$\psi_{n,k}(x) = e^{ikx}\,u_{n,k}(x)$$

where $u_{n,k}(x+a) = u_{n,k}(x)$ is periodic with the lattice period. This is **Bloch's theorem**. The proof is immediate: set $u(x) = e^{-ikx}\psi(x)$; then $u(x+a) = e^{-ik(x+a)}e^{ika}\psi(x) = u(x)$.

The integer $n$ is the band index. At a given crystal momentum $k$, multiple solutions exist — these are the bands.

**What this means physically.** Electrons in a perfectly periodic potential are not scattered — they propagate as Bloch waves with crystal momentum $\hbar k$ as a conserved quantum number. The key difference from free electrons: $k$ is defined only modulo $G = 2\pi/a$, so all distinct values fit in the first BZ. The band index distinguishes the multiple solutions at the same $k$ once the lattice perturbs the free-electron parabola.

Bloch derived this in 1928 as part of his PhD thesis under Heisenberg. The central insight — periodic potential produces propagating, not scattered, waves — was counterintuitive to physicists who expected electrons to bounce randomly off every atom.

---

## The Kronig-Penney Model

The Kronig-Penney model (1931) is the canonical analytically tractable periodic potential. Use the delta-function version, which gives the full physics with minimal algebra.

**Setup.** The potential is a sequence of delta-function barriers:

$$V(x) = \frac{\hbar^2 P}{ma}\sum_n\delta(x - na),$$

where $P$ is a dimensionless barrier strength. The limit $P \to 0$ recovers free electrons; $P \to \infty$ approaches an array of isolated atoms.

**Derivation.** Between delta functions the Schrödinger equation is free-particle with $E = \hbar^2\alpha^2/2m$. In the region $0 < x < a$, the solution is $Ae^{i\alpha x} + Be^{-i\alpha x}$. Applying Bloch periodicity at $x = a$ and the continuity/jump conditions at the delta function at $x = 0$, the consistency condition (vanishing determinant) gives the **Kronig-Penney dispersion relation**:

$$\boxed{\cos(ka) = \cos(\alpha a) + \frac{P}{\alpha a}\sin(\alpha a).}$$

**Reading it.** Define the right-hand side as $f(\alpha a) = \cos(\alpha a) + (P/\alpha a)\sin(\alpha a)$. The left side is bounded: $|\cos(ka)| \leq 1$.

Where $|f(\alpha a)| \leq 1$: a real $k$ exists and the electron propagates — these are **allowed bands**.

Where $|f(\alpha a)| > 1$: no real $k$ exists — these are **forbidden gaps**.

As $\alpha a$ increases from zero, $f(\alpha a)$ oscillates with growing amplitude, periodically exceeding $\pm 1$. Each excursion creates a gap. The bands and gaps alternate, repeating roughly every $\pi$ in $\alpha a$.

**Effect of barrier strength.** As $P$ increases, the amplitude of oscillation in $f$ increases, making the excursions beyond $\pm 1$ wider. Larger $P$ means wider gaps and narrower bands. At $P = 0$: no gaps, continuous free-electron spectrum. As $P \to \infty$: bands shrink to zero width — the isolated-atom limit.

---

## Worked Example — The First Band Gap

Set $P = 3\pi/2 \approx 4.71$.

**Locating the gap.** Evaluate $f$ at $\alpha a = \pi$ (the first zone boundary for free electrons):

$$f(\pi) = \cos(\pi) + \frac{P}{\pi}\sin(\pi) = -1 + 0 = -1.$$

This is exactly at the boundary — the first allowed band ends here. Just above $\alpha a = \pi$, the term $-(P/\pi)\epsilon$ drives $f$ below $-1$ and the gap opens. Numerically, $f$ re-enters the interval $[-1,1]$ near $\alpha a \approx 4.42$, where the second band begins.

**In natural units** ($\hbar = 2m = a = 1$, energies in units of $\hbar^2/2ma^2$): the first gap runs from $E = \pi^2 \approx 9.87$ to $E \approx 19.5$. The gap width grows with $P$.

**The simulation procedure.** Sweep $\alpha a$ from $0$ to $6\pi$ in 5000 steps. At each point, compute $f(\alpha a)$. If $|f| \leq 1$, assign $k = \arccos(f)/a$ and fold into the first BZ; plot $(k, E = \hbar^2\alpha^2/2m)$. Color allowed-band points teal, shade gap regions gray.

---

## The Nearly-Free-Electron Picture

The Kronig-Penney model treats the periodic potential exactly. The nearly-free-electron (NFE) model starts from free electrons and adds the lattice as a weak perturbation.

**Setup.** Write the potential as a Fourier series: $V(x) = \sum_G V_G e^{iGx}$. The unperturbed states are plane waves $|k\rangle$ with energies $E_k^{(0)} = \hbar^2k^2/2m$.

**Why normal perturbation theory fails at the zone boundary.** At $k = \pi/a$, the states $|k = \pi/a\rangle$ and $|k = -\pi/a\rangle$ are degenerate — they both have energy $\hbar^2\pi^2/2ma^2$. The perturbation denominator vanishes. We need degenerate perturbation theory.

**Degenerate perturbation theory.** Build the $2\times2$ matrix of $V$ between the two degenerate states. The diagonal elements vanish (set the average potential to zero). The off-diagonal element is $V_{G_1}$, the first Fourier component of $V$:

$$W = \begin{pmatrix}0 & V_{G_1}^*\\V_{G_1} & 0\end{pmatrix}.$$

Eigenvalues $\pm|V_{G_1}|$. The energy at the zone boundary splits into $E_\pm = \hbar^2\pi^2/2ma^2 \pm |V_{G_1}|$:

$$\boxed{\text{Band gap} = 2|V_{G_1}|.}$$

**The gap equals twice the magnitude of the relevant Fourier component of the potential.** Strong potential — wide gap; weak potential — narrow gap; zero potential — no gap.

**Physical picture: Bragg reflection.** At $k = \pi/a$, the de Broglie wavelength $\lambda = 2a$ satisfies the Bragg condition for a lattice with spacing $a$. Forward and backward waves mix equally into standing waves:

$$\psi_+ \propto \cos(\pi x/a), \qquad \psi_- \propto \sin(\pi x/a).$$

The probability density $|\psi_+|^2$ peaks at the ion positions; $|\psi_-|^2$ peaks between them. In a crystal where ions attract electrons, $\psi_+$ sees lower potential energy and $\psi_-$ sees higher. Their energy difference is $2|V_{G_1}|$. This is the gap — two standing waves with the same kinetic energy, forced by symmetry to different positions, sampling the potential differently.

<!-- → [FIGURE: Standing waves at zone boundary — |ψ+|² peaks at ion sites (lower energy), |ψ−|² peaks between sites (higher energy), with periodic lattice potential shown below] -->

---

## The Tight-Binding Picture

The NFE model works near the free-electron limit. The tight-binding (TB) model works near the atomic limit: start from isolated atoms and turn on overlap between neighboring orbitals.

**Setup.** Each atom has a localized orbital $|\phi_n\rangle$ at site $na$ with energy $E_0$. Write the Bloch state as a sum with the correct Bloch phase:

$$|\psi_k\rangle = \frac{1}{\sqrt{N}}\sum_n e^{ikna}|\phi_n\rangle.$$

**The energy.** Evaluate $\langle\psi_k|\hat{H}|\psi_k\rangle$. The diagonal term gives $E_0$ (on-site energy, shifted slightly by the crystal environment). The nearest-neighbor off-diagonal terms define the **hopping integral** $t = -\langle\phi_{n+1}|\hat{H}|\phi_n\rangle > 0$. Keeping only nearest-neighbor hops:

$$\boxed{E(k) = E_0 - 2t\cos(ka).}$$

At $k = 0$: $E = E_0 - 2t$ (band bottom, symmetric superposition). At $k = \pm\pi/a$: $E = E_0 + 2t$ (band top, antisymmetric). Bandwidth: $4t$.

**Effective mass.** Expand near the band bottom:

$$E(k) \approx (E_0 - 2t) + ta^2k^2 = E_\text{bottom} + \frac{\hbar^2k^2}{2m^*}, \qquad m^* = \frac{\hbar^2}{2ta^2}.$$

Strong hopping (large $t$) means light effective mass — the electron propagates easily. Near the band top, $m^* < 0$: an electron behaves as a **hole**, a positively charged quasiparticle moving opposite to the applied force.

---

## Metals, Insulators, and Semiconductors

Band filling is governed by Pauli: each $k$-state holds 2 electrons (spin up and down). The first BZ has one $k$-value per unit cell, so the first band holds 2 electrons per atom.

**One electron per atom** (alkali metals: Na, K, Li): half-filled band. The Fermi level cuts through the band. There are electrons right at the Fermi energy that can be accelerated by an applied field. **Metal.**

**Two electrons per atom, one orbital per atom** (alkaline earths in the simplest model): completely filled band, empty next band. If the gap is large compared to $k_BT$, **insulator** (diamond, gap 5.5 eV). If the gap is a few eV, **semiconductor** (Si: 1.12 eV; Ge: 0.67 eV; GaAs: 1.42 eV). The distinction between semiconductor and insulator is quantitative: semiconductors have a useful thermally-generated carrier density at room temperature; insulators do not.

**Band overlap** (graphite, the semimetals): the top of one band and the bottom of the next overlap in energy; the Fermi level cuts through both. **Semimetal**.

The three models — Kronig-Penney, NFE, tight-binding — cover the same physics from different starting points. Kronig-Penney interpolates between the limits as $P$ varies: at $P = 0$ it is NFE; as $P \to \infty$ it approaches isolated atoms. Real materials sit between the extremes. Density functional theory (DFT) handles them self-consistently, but the Bloch-wave structure is the same.

<!-- → [FIGURE: Band-filling schematic — three panels showing metal (Fermi level in band), semiconductor (small gap), and insulator (large gap), each with Fermi level marked] -->

---

## Zone Schemes

Three ways to display the same information:

**Extended zone scheme.** The first band occupies BZ 1 ($k\in[-\pi/a, \pi/a]$), the second band occupies BZ 2 (the next two segments), and so on. This shows the free-electron parabola ancestry — each band is a segment of $E = \hbar^2k^2/2m$ gapped and folded back.

**Reduced zone scheme.** All bands folded into the first BZ by subtracting reciprocal lattice vectors. Every band is a distinct curve over $k\in[-\pi/a, \pi/a]$. This is the standard representation for real band diagrams.

**Repeated zone scheme.** The reduced-zone dispersion extended periodically over all $k$. Useful for visualizing group velocity $dE/dk$ continuity.

All three are physically equivalent. The reduced zone scheme is preferred because it makes explicit that all distinct crystal momenta lie in the first BZ.

---

## Still Puzzling

**Topological insulators.** In the 1980s–2000s, theorists began asking not just how wide the band gap is, but what shape the Bloch functions $u_{n,k}$ trace out as $k$ sweeps around the BZ. This is a topological question — it measures a global property of the wavefunction bundle over $k$-space, not a local one. The relevant invariant (the Chern number or $\mathbb{Z}_2$ index) can distinguish a normal insulator (invariant = 0) from a topological insulator (invariant = 1). Topological insulators are bulk insulators with conducting surface states that cannot be removed without closing the bulk gap — not because of chemistry or disorder, but because of topology. Predicted around 2005–2007 (Kane and Mele; Bernevig, Hughes, and Zhang) and confirmed in Bi-Sb alloys and HgTe quantum wells, topological materials are now a major research frontier.

**Flat bands and magic-angle graphene.** The tight-binding bandwidth is $4t$. In moiré superlattices — two graphene layers twisted by a small angle $\theta$ — the effective period is the moiré period $a_M \sim a/\theta$, much larger than $a$. Hopping across the moiré unit cell is tiny, and bands become nearly flat ($4t \to 0$). In flat bands the kinetic energy is quenched and electron-electron interactions dominate. At the "magic angle" of $\sim 1.1°$, twisted bilayer graphene becomes superconducting at $\sim 1.7$ K (Cao et al., 2018). Kronig-Penney with a very large $P$ is a cartoon of the same physics — narrow bands, strong correlations.

**The band-gap problem in DFT.** The local density approximation systematically underestimates semiconductor gaps by 30–50%: silicon's calculated gap is $\sim 0.6$ eV versus the measured 1.12 eV. The Kohn-Sham eigenvalues are not quasiparticle energies. Corrections from the GW approximation or hybrid functionals bring computed gaps into agreement with experiment, but this remains an active area.

---

## The +1 — Simulation Exercise

The deliverable is `11-periodic-potentials.html`: a D3 simulation with two modes — the Kronig-Penney dispersion in both $f(\alpha a)$ and reduced-zone $E(k)$ representations, and a tight-binding comparison overlay.

### `PROJECT.md` Update

````
Append to PROJECT.md:

Chapter 10 — Periodic Potentials and Band Structure
Deliverable: 11-periodic-potentials.html
Status: in progress

Two modes: "Kronig-Penney dispersion" and "Tight-binding comparison".

KRONIG-PENNEY MODE
Left panel (600px): f(alpha*a) vs. alpha*a from 0 to 6*pi.
  f = cos(alpha*a) + (P / (alpha*a)) * sin(alpha*a).
  Teal shading where |f| <= 1 (allowed); gray where |f| > 1 (forbidden).
  Dashed red lines at f = ±1.

Right panel (500px): reduced-zone E(k). For each alpha*a where |f| <= 1:
  k = arccos(f) / a, folded by band index into [-pi/a, pi/a].
  E = (alpha*a)^2 in natural units (hbar=m=a=1).
  Teal dots. Gray shading on E-axis for gap regions.
  P slider from 0 to 6*pi, step 0.1.

TIGHT-BINDING COMPARISON MODE
Same right panel plus orange overlay: E(k) = E_0 - 2t*cos(k).
Fit: E_0 = (E_top + E_bottom)/2, t = (E_top - E_bottom)/4.
Band selector (band 1 or 2). Display fitted t value.
````

### The Simulation Prompt

````
Read CLAUDE.md, DESIGN.md, and PROJECT.md first.

Build 11-periodic-potentials.html: single self-contained HTML, D3 v7 from CDN.
No other external dependencies. Two modes via tabs.

KRONIG-PENNEY MODE
Left SVG 550 × 500:
  x-axis: alpha*a from 0 to 6*pi, ticks at pi, 2*pi, ..., 6*pi
  y-axis: f from -3 to +3
  Plot f(alpha*a) = cos(alpha*a) + (P / (alpha*a)) * sin(alpha*a).
  At alpha*a → 0, f → 1 + P (L'Hopital limit; handle separately).
  Teal fill where |f| <= 1. Dashed red lines at ±1.

Right SVG 550 × 500:
  x-axis: k from -pi to pi. y-axis: E auto-scaled, show at least 4 bands.
  For each alpha*a in [0, 6*pi] (5000 steps) where |f| <= 1:
    band_index = floor(alpha*a / pi)
    k_raw = arccos(f) / 1    (with a=1)
    k = k_raw if band_index even; k = pi - k_raw if band_index odd
    E = (alpha*a)^2
  Plot (k, E) as teal dots. Gray shading for gap E-ranges.

Controls: P slider 0 to 6*pi, step 0.05, default 3*pi/2.

Console sanity checks:
  P=0: all points allowed, log N_forbidden = 0.
  P=3*pi/2: log gap 1 boundaries in alpha*a.

TIGHT-BINDING COMPARISON MODE
Add orange curve over the KP right panel for selected band:
  Find E_bottom, E_top of the selected band.
  t = (E_top - E_bottom) / 4, E_0 = (E_top + E_bottom) / 2.
  Plot E_0 - 2*t*cos(k) in orange.
  Display: "Tight-binding fit: E_0 = [val], t = [val]"
Band toggle: band 1 / band 2.

Comments at every physics step.
````

### Exploration Tasks

**Map the bands.** At $P = 3\pi/2$, from the left panel, identify the first three allowed bands and first two gaps. Read off the approximate $\alpha a$ values at each boundary.

**Barrier strength scaling.** Increase $P$ from $3\pi/2$ to $6\pi$. Describe how the width of the first band changes relative to the width of the first gap. As $P \to \infty$, what does the band structure approach?

**Weak potential.** Set $P = 0.5$. Is a gap visible? In natural units, the NFE prediction is $\Delta E \approx 2P$ for weak delta-function barriers. Compare the simulation's gap width to this estimate.

**Tight-binding comparison.** For band 1 at $P = 3\pi/2$, record the fitted $t$ value. Switch to band 2 — is $t$ larger or smaller? (Higher bands are typically wider, corresponding to larger effective $t$.) At $k \approx \pi/2$, where does the tight-binding fit agree best and worst with the KP dispersion?

---

## References

- Kronig, R. de L. and Penney, W.G. (1931). "Quantum mechanics of electrons in crystal lattices." *Proceedings of the Royal Society A*, 130, 499–513. [verify]
- Bloch, F. (1928). "Über die Quantenmechanik der Elektronen in Kristallgittern." *Zeitschrift für Physik*, 52, 555–600. [verify]
- Kittel, C. (2005). *Introduction to Solid State Physics*, 8th ed. Wiley. Ch. 7–9. [verify]
- Ashcroft, N.W. and Mermin, N.D. (1976). *Solid State Physics*. Holt, Rinehart and Winston. Ch. 8–10. [verify]
- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §5.3. [verify]
- Cao, Y. et al. (2018). "Unconventional superconductivity in magic-angle graphene superlattices." *Nature*, 556, 43–50. [verify]
- Kane, C.L. and Mele, E.J. (2005). "Z₂ topological order and the quantum spin Hall effect." *Physical Review Letters*, 95, 146802. [verify]

---

*Chapter 11 follows: scattering in periodic structures — the structure factor and the diffraction condition that recovers Bragg's law as a consequence of the same reciprocal-lattice geometry developed here.*
