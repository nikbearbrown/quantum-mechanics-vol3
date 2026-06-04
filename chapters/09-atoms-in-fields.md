# Chapter 9 — Atoms in Fields: Zeeman, Stark, and Magnetic Resonance

## TL;DR

- An external field breaks the rotational symmetry of the atom and lifts degeneracies in a way that reveals everything about spin and angular momentum.
- In a weak magnetic field the Landé g-factor governs how fine-structure sublevels split (anomalous Zeeman effect); strong fields decouple spin from orbit (Paschen–Back).
- An electric field shifts energy by a tiny amount quadratically in non-degenerate levels but linearly in degenerate ones — hydrogen's accidental degeneracy makes the n=2 splitting enormous.
- Magnetic resonance (Rabi/NMR/ESR) is an exact two-state solution hiding inside the rotating-frame transformation; T₁ and T₂ describe how that exact solution gives way to the real world.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Apply** degenerate perturbation theory to compute the Zeeman splitting of hydrogen fine-structure levels in the weak-field limit, using the Landé g-factor formula. *(Apply — Bloom level 3)*

2. **Explain** why the weak-field (anomalous) and strong-field (Paschen–Back) Zeeman patterns differ, identifying the good quantum numbers in each limit. *(Understand — Bloom level 2)*

3. **Predict** whether a given atomic level will show a linear or quadratic Stark effect, and compute the linear splitting for the hydrogen n=2 manifold. *(Apply — Bloom level 3)*

4. **Derive** the rotating-frame Hamiltonian for a spin-1/2 in combined static and oscillating magnetic fields and identify the resonance condition. *(Analyze — Bloom level 4)*

5. **Design** a D3 simulation that shows energy-level splitting as a function of field strength, reproducing the qualitative crossover between Zeeman regimes. *(Create — Bloom level 6)*

---

## Scene Opening

Pieter Zeeman spent months in Leiden getting fired at.

Not literally — but the institutional opposition felt that way. His supervisor, the great Hendrik Lorentz, had asked him not to pursue what seemed like a frivolous experiment: whether a flame in a strong magnetic field would change the color of its spectral lines. Zeeman ran the experiment anyway, in 1896, found that the lines split, and was promptly reprimanded for using unauthorized laboratory equipment. Lorentz, to his credit, immediately provided the theoretical explanation: if the spectral line came from an oscillating charged particle, a magnetic field would split the oscillation frequency into three. Three lines. Theory and experiment matched.

Then the problem got harder. When experimenters looked at more complex atoms — atoms with unpaired electron spins — they did not find a clean triplet. They found six lines, eight lines, asymmetric patterns with irrational spacing ratios. They called this the "anomalous" Zeeman effect, by which they meant: we have no idea what is happening.

The anomaly lasted thirty years. Its resolution required the concept of electron spin, then the quantum mechanics of angular momentum addition, and finally the Landé g-factor — a single number that encodes how orbital and spin angular momentum conspire to produce the observed pattern. Once you have the g-factor, the "anomalous" Zeeman effect is not anomalous at all. It is ordinary Zeeman, done correctly.

This chapter is about what happens to atomic energy levels when you apply an external field. The perturbation-theory machinery is the same as before; what is new is the physical richness of what it finds.

---

## Core Development

### The Magnetic Perturbation

Place a hydrogen-like atom in a uniform external magnetic field $\mathbf{B} = B\hat{z}$. The interaction between the atom's magnetic moments and the field is the perturbation. There are two contributions.

The orbital motion of the electron produces a magnetic moment
$$\boldsymbol{\mu}_L = -\frac{e}{2m_e}\mathbf{L}$$
where $e > 0$ is the elementary charge and the minus sign reflects the electron's negative charge.

The electron's spin produces a magnetic moment
$$\boldsymbol{\mu}_S = -\frac{e}{m_e}\mathbf{S}$$
The factor of 2 difference between the orbital and spin contributions is the source of all the complexity in Zeeman physics. It comes from the Dirac equation — or, in more physical terms, from the fact that the electron is not a tiny current loop but a fundamental spin-1/2 particle. (The true g-factor for the electron spin is $g_s = 2.002319\ldots$ rather than exactly 2; the correction is a QED effect, the anomalous magnetic moment, and will appear in "Still Puzzling.")

The perturbation Hamiltonian is
$$\hat{H}' = -(\boldsymbol{\mu}_L + \boldsymbol{\mu}_S)\cdot\mathbf{B} = \frac{e B}{2m_e}(\hat{L}_z + 2\hat{S}_z)$$

Written in terms of the total angular momentum $\hat{\mathbf{J}} = \hat{\mathbf{L}} + \hat{\mathbf{S}}$:
$$\hat{H}' = \frac{e B}{2m_e}(\hat{J}_z + \hat{S}_z)$$

The $\hat{J}_z$ piece is easy — it is diagonal in the $|j, m_j\rangle$ basis. The $\hat{S}_z$ piece is not, and that is the whole problem.

**Notation.** The **Bohr magneton** is $\mu_B = e\hbar/2m_e \approx 9.274 \times 10^{-24}$ J/T $= 5.788 \times 10^{-5}$ eV/T. The perturbation is $\hat{H}' = (\mu_B/\hbar)B(\hat{L}_z + 2\hat{S}_z)$.

---

### The Weak-Field (Anomalous) Zeeman Effect

When the external field is weak — weak meaning $\mu_B B \ll \Delta E_\text{fs}$, the fine-structure splitting — the spin-orbit coupling is the dominant internal interaction. The atom's angular momenta $\mathbf{L}$ and $\mathbf{S}$ are locked together, precessing rapidly around their sum $\mathbf{J}$. The external field then makes $\mathbf{J}$ precess slowly around $\hat{z}$.

In this regime the good quantum numbers are $n, \ell, j, m_j$ — the total-angular-momentum basis. The perturbation must be averaged over the rapid internal motion. Since $\mathbf{L}$ and $\mathbf{S}$ precess around $\mathbf{J}$, only the components of $\boldsymbol{\mu}_L + \boldsymbol{\mu}_S$ along $\mathbf{J}$ survive the average.

The projection onto $\mathbf{J}$ is evaluated by writing $\hat{S}_z = \hat{J}_z - \hat{L}_z$ and using the identity
$$\langle \hat{\mathbf{S}}\cdot\hat{\mathbf{J}}\rangle = \frac{1}{2}\langle\hat{J}^2 + \hat{S}^2 - \hat{L}^2\rangle = \frac{\hbar^2}{2}[j(j+1) + s(s+1) - \ell(\ell+1)]$$

to replace $\hat{S}_z$ by its projected value. The result for the energy shift is

$$\boxed{\Delta E = g_J \mu_B B m_j}$$

where the **Landé g-factor** is

$$\boxed{g_J = 1 + \frac{j(j+1) + s(s+1) - \ell(\ell+1)}{2j(j+1)}}$$

This formula is the heart of the anomalous Zeeman effect. Each fine-structure level — labeled by a particular $(n, \ell, j)$ — has its own $g_J$ and therefore its own pattern of $2j+1$ equally-spaced sublevels. The spacing is $g_J \mu_B B$, which depends on $\ell$ and $j$ in a way that varies from level to level. That is why the multi-line patterns look "anomalous" — the spacing is not the same for each original level.

**Key values for hydrogen.** For $s = 1/2$:

| State | $\ell$ | $j$ | $g_J$ |
|-------|--------|-----|--------|
| s-states ($\ell=0$) | 0 | 1/2 | 2 |
| $2p_{1/2}$ | 1 | 1/2 | 2/3 |
| $2p_{3/2}$ | 1 | 3/2 | 4/3 |

When $\ell = 0$, the electron has no orbital angular momentum; the magnetic moment is purely spin, and $g_J = 2$ (pure spin value). When $\ell \neq 0$, spin and orbital moments partially cancel or reinforce.

---

### The Strong-Field (Paschen–Back) Effect

When $\mu_B B \gg \Delta E_\text{fs}$ — the external field overwhelms the spin-orbit coupling — the good quantum numbers change. Now the external field dominates the dynamics: $\mathbf{L}$ and $\mathbf{S}$ precess independently around $\hat{z}$, rather than jointly. The coupling between them is a weak perturbation on top of the strong Zeeman effect.

In this limit the good quantum numbers are $m_\ell$ and $m_s$ (uncoupled basis), and the first-order energy shift is simply

$$\Delta E = \mu_B B(m_\ell + 2m_s)$$

The fine-structure spin-orbit term $\hat{H}'_\text{SO} \propto \mathbf{L}\cdot\mathbf{S}$ can then be treated as a small additional perturbation in this basis.

The Paschen–Back pattern is simpler than the anomalous pattern: it is essentially a normal Zeeman triplet (from the $m_\ell$ splitting) with each line further split by spin. The many-line anomalous Zeeman pattern collapses to something more regular as the field increases.

**The intermediate-field regime** — where $\mu_B B \sim \Delta E_\text{fs}$ — has no simple analytic result. Both the external-field and spin-orbit terms must be diagonalized simultaneously in the full $n$-manifold. Griffiths works this out numerically for the hydrogen $n=2$ case; the resulting energy-vs.-field curves cross and avoid-cross in a pattern called an avoided-level-crossing diagram. The qualitative picture is that levels that start in the Zeeman pattern at weak field smoothly connect to levels in the Paschen–Back pattern at strong field, with the intermediate regime requiring numerical diagonalization.

---

### The Stark Effect

Now apply an electric field $\mathcal{E}$ along $\hat{z}$ instead of a magnetic field. The perturbation is

$$\hat{H}' = e\mathcal{E}\hat{z}$$

**The ground state and the quadratic Stark effect.** For $|1s\rangle$, the first-order shift is

$$E^{(1)}_{1s} = \langle 1s|e\mathcal{E}\hat{z}|1s\rangle = 0$$

This vanishes because $|1s\rangle$ is parity-even and $\hat{z}$ is parity-odd; the integrand is parity-odd and integrates to zero over all space. The first non-vanishing correction is second-order:

$$E^{(2)}_{1s} = \sum_{n\neq 1s}\frac{|\langle n|e\mathcal{E}\hat{z}|1s\rangle|^2}{E^{(0)}_{1s} - E^{(0)}_n}$$

The result is $E^{(2)}_{1s} = -\frac{9}{2}a_0^3\mathcal{E}^2$ (in Gaussian units, with $e = 1$), which defines the static electric polarizability $\alpha_\text{pol} = \frac{9}{2}a_0^3 \approx 4.5 a_0^3$. The shift is **quadratic in $\mathcal{E}$** — a **quadratic Stark effect**. The ground state develops an induced dipole moment; the atom polarizes, lowering its energy.

**The $n=2$ manifold and the linear Stark effect.** The $n=2$ level of hydrogen is fourfold degenerate: $|2s\rangle$, $|2p_0\rangle$, $|2p_{+1}\rangle$, $|2p_{-1}\rangle$ all share the energy $E^{(0)}_2 = -\frac{13.6\,\text{eV}}{4}$. This is the *accidental degeneracy* of the Coulomb potential — states with the same $n$ but different $\ell$ happen to be degenerate because the Coulomb $1/r$ potential has an extra conserved quantity (the Runge–Lenz vector).

We apply degenerate perturbation theory: construct the $4\times 4$ matrix of $\hat{H}' = e\mathcal{E}\hat{z}$ in this subspace, then diagonalize it.

Selection rules do most of the work before any integral is computed. The operator $\hat{z}$ commutes with $\hat{L}_z$, so it cannot change $m$ — any matrix element with $\Delta m \neq 0$ vanishes. This zeroes out all entries involving $|2p_{\pm 1}\rangle$ coupling to either $|2s\rangle$ or $|2p_0\rangle$. Parity kills all diagonal elements: $\langle 2s|\hat{z}|2s\rangle = 0$ and $\langle 2p_0|\hat{z}|2p_0\rangle = 0$.

The only surviving entry is $\langle 2s|e\mathcal{E}\hat{z}|2p_0\rangle$. From the radial and angular integrals of the hydrogen wave functions:

$$\langle 2s|\hat{z}|2p_0\rangle = -3a_0$$

The full $4\times 4$ perturbation matrix, ordered $\{|2s\rangle, |2p_0\rangle, |2p_{+1}\rangle, |2p_{-1}\rangle\}$:

$$W = e\mathcal{E}\begin{pmatrix} 0 & -3a_0 & 0 & 0 \\ -3a_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

This block-diagonalizes immediately. The lower $2\times 2$ block is zero: $|2p_{+1}\rangle$ and $|2p_{-1}\rangle$ are already good states, they do not shift at first order. The upper $2\times 2$ block has eigenvalues $\pm 3a_0 e\mathcal{E}$, with eigenstates $(|2s\rangle \mp |2p_0\rangle)/\sqrt{2}$.

The $n=2$ level splits into **three lines** from four states:
- Up by $+3a_0 e\mathcal{E}$: eigenstate $(|2s\rangle - |2p_0\rangle)/\sqrt{2}$
- Unshifted (doubly degenerate): $|2p_{+1}\rangle$, $|2p_{-1}\rangle$
- Down by $-3a_0 e\mathcal{E}$: eigenstate $(|2s\rangle + |2p_0\rangle)/\sqrt{2}$

This splitting is **linear in $\mathcal{E}$** — a **linear Stark effect** — because the degeneracy allows states to mix at first order. The "good" eigenstates are superpositions of $s$ and $p$ states with definite parity; they have permanent electric dipole moments oriented along $\hat{z}$, which is exactly what couples to the applied field.

**Why hydrogen is special.** The linear Stark effect requires degenerate states of opposite parity at the same energy. Hydrogen has this accidentally (the $2s$ and $2p$ levels share the same energy). In multi-electron atoms, $s$ and $p$ states at the same principal quantum number are split by the quantum defect — there is no accidental degeneracy, and the Stark effect is always quadratic. Rydberg atoms (large $n$) recover the near-degeneracy, and show enormous quadratic Stark shifts scaling as $n^7$.

---

### Magnetic Resonance

The third phenomenon is qualitatively different: it is exact, not perturbative, and it involves time.

**Setup.** Take a spin-1/2 particle (a nucleus or an electron) in a static magnetic field $B_0\hat{z}$. The Zeeman splitting is $\hbar\omega_0$ where $\omega_0 = \gamma B_0$ is the **Larmor frequency** ($\gamma$ is the gyromagnetic ratio of the particle). The spin precesses around $\hat{z}$ at frequency $\omega_0$.

Now add a weak transverse oscillating field:

$$\mathbf{B}_1(t) = B_1(\hat{x}\cos\omega t + \hat{y}\sin\omega t)$$

This is a rotating field in the $xy$-plane at frequency $\omega$. The full Hamiltonian is time-dependent and in principle requires time-dependent perturbation theory. But there is an exact solution hidden in a change of reference frame.

**The rotating frame.** Transform to a reference frame rotating at angular frequency $\omega$ around $\hat{z}$. In this frame:

- The static field $B_0\hat{z}$ appears reduced: the effective z-component is $B_0 - \omega/\gamma$.
- The rotating transverse field $B_1$ appears stationary — it is locked to the rotating frame, pointing along $\hat{x}'$.

The effective Hamiltonian in the rotating frame is

$$\hat{H}_R = -\hbar(\omega_0 - \omega)\hat{S}_z/\hbar - \hbar\omega_1\hat{S}_{x'}/\hbar$$

where $\omega_1 = \gamma B_1$ is the **Rabi frequency** and $\hat{S}_{x'}$ is the spin operator along the rotating-frame $x$-axis.

**Resonance.** At $\omega = \omega_0$, the $\hat{S}_z$ term vanishes. The rotating-frame Hamiltonian reduces to $\hat{H}_R = -\hbar\omega_1\hat{S}_{x'}$ — a pure transverse field. The spin precesses around $\hat{x}'$ at frequency $\omega_1$.

In the lab frame, this means: starting from spin-up ($|\!\uparrow\rangle$), the spin oscillates between up and down at frequency $\omega_1$. These are **Rabi oscillations**:

$$P_\downarrow(t) = \sin^2\!\left(\frac{\omega_1 t}{2}\right)$$

At time $t = \pi/\omega_1$ (a "$\pi$ pulse"), the spin has completely flipped. This is the basis of Rabi's 1938 molecular-beam experiment: the RF frequency is swept; when $\omega = \omega_0$, the spin flips and the beam is deflected differently. The resonance appears as a sharp dip in the detector count.

**Off-resonance.** When $\omega \neq \omega_0$, the effective field in the rotating frame has both $z$ and $x'$ components. The spin precesses around this tilted effective field; the probability of flipping is reduced. The full expression is

$$P_\downarrow(t) = \frac{\omega_1^2}{\Omega^2}\sin^2\!\left(\frac{\Omega t}{2}\right), \qquad \Omega = \sqrt{(\omega-\omega_0)^2 + \omega_1^2}$$

where $\Omega$ is the generalized Rabi frequency. Far from resonance, $\Omega \gg \omega_1$ and the flip probability is small.

**NMR and T₁, T₂.** In a macroscopic sample, the Bloch equations describe the bulk magnetization $\mathbf{M}$:

$$\frac{d\mathbf{M}}{dt} = \gamma\mathbf{M}\times\mathbf{B} - \frac{M_x\hat{x} + M_y\hat{y}}{T_2} - \frac{(M_z - M_0)\hat{z}}{T_1}$$

Here $T_1$ (longitudinal relaxation, spin-lattice) is the timescale for $M_z$ to return to equilibrium $M_0$; $T_2$ (transverse relaxation, spin-spin) is the timescale for the transverse magnetization to dephase. Typical values in water: $T_1 \sim 1$–3 s, $T_2 \sim 0.1$–3 s.

Pulsed NMR works as follows: a $\pi/2$ pulse tips the magnetization into the transverse plane; the transverse magnetization precesses at $\omega_0$ and induces an oscillating EMF in a pickup coil (the **free induction decay**, FID). The envelope of the FID decays at rate $1/T_2^*$ (which includes field inhomogeneity). A subsequent $\pi$ pulse reverses the dephasing and produces a **spin echo** at time $2\tau$, with amplitude $e^{-2\tau/T_2}$; comparing echo heights at different $\tau$ gives $T_2$ free of field inhomogeneity.

**ESR.** The same physics at microwave frequencies. Because $\gamma_e/\gamma_N \approx 1836$, electron spin resonance (ESR, also called EPR) occurs at GHz rather than MHz for the same field. ESR is used to study radicals, transition-metal complexes, and spin-labeled proteins.

**MRI.** By adding a gradient field $B_0 + G_z z$, the Larmor frequency varies with position. Selective RF pulses excite a thin slice; additional gradients during readout encode the 2D spatial information as different frequencies in the FID. Image contrast comes from spatial variation in proton density, $T_1$, and $T_2$ across tissues. Clinical MRI operates at 1.5–7 T (proton Larmor frequency 64–298 MHz); whole-body 11.7 T scanners now exist for research.

---

## Worked Example: Weak-Field Zeeman Splitting of the Hydrogen 2p Levels

**The question.** Hydrogen is placed in a weak magnetic field $B = 0.5$ T. Compute the energy shifts of all sublevels in the $n = 2$, $\ell = 1$ manifold.

**The lesson.** Fine structure first splits the $2p$ manifold into $2p_{1/2}$ ($j = 1/2$, 2 states: $m_j = \pm 1/2$) and $2p_{3/2}$ ($j = 3/2$, 4 states: $m_j = -3/2, -1/2, +1/2, +3/2$). We are in the weak-field limit as long as $\mu_B B \ll \Delta E_\text{fs}$.

Check: $\mu_B B = (5.788\times 10^{-5}\,\text{eV/T})(0.5\,\text{T}) = 2.9\times 10^{-5}$ eV. The fine-structure splitting of the hydrogen $2p$ level is $\Delta E_{FS}(2p_{3/2} - 2p_{1/2}) \approx 4.5\times 10^{-5}$ eV (from the formula $E^\text{fs}_n = \frac{(E^{(0)}_n)^2}{2m_ec^2}\left(\frac{2n}{j+1/2} - \frac{3}{2}\right)$). So at 0.5 T the Zeeman energy is about 65% of the fine-structure splitting — we are already near the intermediate-field regime. For the purpose of this example we proceed with the weak-field formula and note the caveat.

**Compute $g_J$ for each sublevel.** With $\ell = 1$, $s = 1/2$:

For $2p_{3/2}$ ($j = 3/2$):
$$g_J = 1 + \frac{(3/2)(5/2) + (1/2)(3/2) - (1)(2)}{2(3/2)(5/2)} = 1 + \frac{15/4 + 3/4 - 2}{15/2} = 1 + \frac{10/4}{15/2} = 1 + \frac{1}{3} = \frac{4}{3}$$

For $2p_{1/2}$ ($j = 1/2$):
$$g_J = 1 + \frac{(1/2)(3/2) + (1/2)(3/2) - (1)(2)}{2(1/2)(3/2)} = 1 + \frac{3/4 + 3/4 - 2}{3/2} = 1 + \frac{-1/2}{3/2} = 1 - \frac{1}{3} = \frac{2}{3}$$

**Energy shifts $\Delta E = g_J \mu_B B m_j$, with $\mu_B B = 2.9\times 10^{-5}$ eV:**

For $2p_{3/2}$ ($g_J = 4/3$):

| $m_j$ | $\Delta E$ |
|--------|------------|
| $+3/2$ | $+\frac{4}{3}\cdot\frac{3}{2}\,\mu_B B = +2\mu_B B \approx +5.8\times 10^{-5}$ eV |
| $+1/2$ | $+\frac{4}{3}\cdot\frac{1}{2}\,\mu_B B = +\frac{2}{3}\mu_B B \approx +1.9\times 10^{-5}$ eV |
| $-1/2$ | $-\frac{2}{3}\mu_B B \approx -1.9\times 10^{-5}$ eV |
| $-3/2$ | $-2\mu_B B \approx -5.8\times 10^{-5}$ eV |

For $2p_{1/2}$ ($g_J = 2/3$):

| $m_j$ | $\Delta E$ |
|--------|------------|
| $+1/2$ | $+\frac{1}{3}\mu_B B \approx +0.97\times 10^{-5}$ eV |
| $-1/2$ | $-\frac{1}{3}\mu_B B \approx -0.97\times 10^{-5}$ eV |

**The result.** Six distinct energy levels from eight original states. The $2p_{3/2}$ quartet has spacing $\frac{2}{3}\mu_B B$ between adjacent $m_j$ levels; the $2p_{1/2}$ doublet has spacing $\frac{2}{3}\mu_B B$ as well — but the overall scale differs by the ratio of $g_J$ values. When optical transitions are allowed between these levels and the split $1s$ state, the emission pattern is an irregular multiplet with unequal spacings: the anomalous Zeeman pattern.

**The limit.** This calculation assumed the weak-field limit. At $B = 0.5$ T for hydrogen $2p$ states, $\mu_B B \approx 0.65\,\Delta E_{FS}$, so we are near the crossover. For an accurate treatment at intermediate fields, the Zeeman and fine-structure terms must be diagonalized together in the full $j$-manifold. There is no simple analytic formula for this crossover — it requires numerical diagonalization, which is exactly what the simulation exercise builds.

---

## Common Misconceptions

**"The anomalous Zeeman effect is anomalous because quantum mechanics fails there."** It is only anomalous historically, because it was discovered before electron spin. With spin, the Landé g-factor gives a complete account. The name stuck; the mystery did not.

**"In the strong-field (Paschen–Back) limit, spin-orbit coupling disappears."** Spin-orbit coupling does not disappear — it becomes a small perturbation on top of the dominant Zeeman interaction. The good quantum numbers change (from $j, m_j$ to $m_\ell, m_s$), but the spin-orbit energy is still there as a small correction to the Paschen–Back pattern.

**"The linear Stark effect is a general atomic phenomenon."** It is specific to hydrogen (and Rydberg atoms). The linear Stark effect requires degenerate states of opposite parity at the same energy. Hydrogen's Coulomb degeneracy provides this; multi-electron atoms do not have degenerate $s$ and $p$ states, and their Stark effect is always quadratic.

**"The parity selection rule kills only off-diagonal matrix elements."** Parity kills diagonal elements too: $\langle n\ell m|\hat{z}|n\ell m\rangle = 0$ for any state of definite parity, because $|n\ell m\rangle^2$ is parity-even but $\hat{z}$ is parity-odd. The integrand is always parity-odd and integrates to zero. This is why the diagonal of the Stark matrix is identically zero.

**"In magnetic resonance, resonance means something physically resonates."** At resonance $\omega = \omega_0$, the drive frequency matches the Larmor precession frequency. In the rotating frame this looks like a static field; the spin undergoes complete, periodic flips. "Resonance" here has its standard meaning of matching a natural frequency — not structural resonance of a macroscopic object.

**"T₁ and T₂ are the same timescale."** In general $T_1 \geq T_2$. The transverse magnetization dephases partly through the same processes that restore $M_z$ (so $T_2 \leq T_1$) but also through additional spin-spin interactions and field inhomogeneity that do not affect $T_1$. MRI contrast exploits the fact that different tissues have different $T_1/T_2$ ratios.

---

## Exercises

### Warm-up

**9.1** The Bohr magneton is $\mu_B = e\hbar/2m_e$. (a) Compute its value in eV/T. (b) A hydrogen atom in the $2s$ state ($\ell = 0$, $j = 1/2$) is placed in a field $B = 1.0$ T. Compute $g_J$ and the two energy shifts $\Delta E = g_J\mu_B B m_j$ for $m_j = \pm 1/2$. (c) What frequency of electromagnetic radiation would drive transitions between these two levels? In which part of the spectrum does this fall? *(Tests: Landé g-factor for a pure-spin state; numerical evaluation; spectral region identification.)*

**9.2** State the selection rule that eliminates $\langle 2p_{+1}|e\mathcal{E}\hat{z}|2s\rangle$ from the Stark matrix. Then state the selection rule (or combination of rules) that eliminates $\langle 2p_0|e\mathcal{E}\hat{z}|2p_0\rangle$. For each, identify the conserved quantity that enforces the rule. *(Tests: identification of selection rules from physical symmetry; understanding which symmetry kills which entry.)*

**9.3** For the Stark $n=2$ calculation, verify by explicit substitution that $(|2s\rangle - |2p_0\rangle)/\sqrt{2}$ is an eigenstate of $W$ with eigenvalue $+3a_0 e\mathcal{E}$. Then verify that its norm is 1. *(Tests: direct check of the diagonalization result; reinforces eigenvalue computation.)*

### Application

**9.4** A hydrogen atom is in the $3d_{3/2}$ state ($n=3$, $\ell=2$, $j=3/2$). (a) Compute the Landé g-factor $g_J$. (b) List all $m_j$ values and compute the energy shift of each in a field $B = 2.0$ T. (c) How many distinct spectral lines would appear in emission from $3d_{3/2} \to 2p_{1/2}$ in this field? (Use the selection rule $\Delta m_j = 0, \pm 1$; count distinct frequency differences.) *(Tests: g-factor calculation for $j = 3/2$; transition counting.)*

**9.5** Magnetic resonance at off-resonance. A spin-1/2 nucleus has $\omega_0 = 300$ MHz (a 7.05 T field, typical clinical NMR). A weak oscillating field is applied at $\omega = 300.001$ MHz. (a) What is $\omega - \omega_0$ in Hz? (b) With $\omega_1 = \gamma B_1 = 2\pi \times 1$ kHz (a typical weak pulse), compute the generalized Rabi frequency $\Omega = \sqrt{(\omega-\omega_0)^2 + \omega_1^2}$. (c) What is the maximum flip probability $P_\downarrow^\text{max} = \omega_1^2/\Omega^2$? (d) If the experiment uses a hard $\pi$-pulse (duration $t_\pi = \pi/\omega_1$), but the RF is off-resonant by 1 kHz, what fraction of the target spins actually flip? *(Tests: rotating-frame and Rabi-oscillation formulas; off-resonance penalty; practical NMR pulse calibration.)*

**9.6** The quadratic Stark effect for the hydrogen ground state has the result $\Delta E = -\frac{9}{2}a_0^3\mathcal{E}^2$ (in Gaussian units, or equivalently $\Delta E = -(9/2)(4\pi\epsilon_0)a_0^3\mathcal{E}^2$ in SI). (a) Express this as a polarizability $\alpha_\text{pol}$ such that $\Delta E = -\frac{1}{2}\alpha_\text{pol}\mathcal{E}^2$. (b) Estimate $\Delta E$ numerically for $\mathcal{E} = 10^7$ V/m (a laboratory electric field). (c) Compare this shift to the fine-structure splitting $\sim 10^{-4}$ eV. Is Stark perturbation theory valid at this field? *(Tests: polarizability definition; numerical evaluation; validity check.)*

### Synthesis

**9.7** Derive the Landé g-factor formula from the following steps. (a) Write $\hat{L}_z + 2\hat{S}_z = \hat{J}_z + \hat{S}_z$. (b) The projection theorem for the operator $\hat{S}_z$ onto the $\hat{J}$ direction gives $\langle \hat{S}_z\rangle = \langle \hat{\mathbf{S}}\cdot\hat{\mathbf{J}}\rangle\,m_j/[j(j+1)]$. Evaluate $\langle \hat{\mathbf{S}}\cdot\hat{\mathbf{J}}\rangle$ in terms of $j$, $\ell$, and $s$ using $\mathbf{J}^2 = (\mathbf{L}+\mathbf{S})^2$. (c) Substitute into $\langle\hat{L}_z + 2\hat{S}_z\rangle = m_j + \langle\hat{S}_z\rangle$ and factor out $m_j$ to read off $g_J$. *(Tests: derivation of a key result from basic angular-momentum identities; ability to use the projection theorem.)*

**9.8** The Paschen–Back regime. Consider a hydrogen $2p$ state ($\ell=1$, $s=1/2$) in a very strong field where $\mu_B B \gg \Delta E_{FS}$. (a) List all possible values of $(m_\ell, m_s)$ and compute the energy shift $\mu_B B(m_\ell + 2m_s)$ for each. (b) How many distinct shift values are there? (Some $(m_\ell, m_s)$ combinations may give the same energy.) (c) Now add the spin-orbit correction as a small additional perturbation. The spin-orbit term is $\propto\langle m_\ell, m_s|\mathbf{L}\cdot\mathbf{S}|m_\ell, m_s\rangle = \hbar^2 m_\ell m_s$. How does this lift any remaining degeneracy? *(Tests: uncoupled-basis calculation; counting distinct Paschen–Back levels; spin-orbit as a perturbation in the strong-field limit.)*

**9.9** Design a NMR spin-echo experiment. (a) A $\pi/2$ pulse tips the magnetization into the transverse plane. After a time $\tau$, different nuclear spins have accumulated different phase shifts due to static field inhomogeneity. Explain qualitatively why a $\pi$ pulse at time $\tau$ causes the spins to rephase at time $2\tau$. (b) The echo amplitude at time $2\tau$ is $M(2\tau) = M_0 e^{-2\tau/T_2}$. If you measure echo amplitudes at $2\tau = 50, 100, 200$ ms and get $M/M_0 = 0.85, 0.72, 0.52$, fit these to estimate $T_2$. (c) Why is the spin-echo $T_2$ measurement immune to static field inhomogeneity, while a simple FID measurement is not? *(Tests: conceptual understanding of spin echo; exponential fitting; distinction between $T_2$ and $T_2^*$.)*

---

## Still Puzzling

**The anomalous magnetic moment.** The true electron g-factor is $g_s = 2.002319304\ldots$, not exactly 2. The correction, $a_e = (g_s - 2)/2 \approx 1.16\times 10^{-3}$, is the **anomalous magnetic moment** and is one of the finest tests of quantum electrodynamics. The current theoretical prediction (Schwinger term plus higher-order QED diagrams) agrees with the experimental measurement of Hanneke, Fogwell, and Gabrielse (2008) to better than one part in $10^{12}$. This uses the same Landé formula as above with $g_J$ replaced by the QED-corrected $g_s$. The correction shifts the Zeeman levels by a tiny amount — in principle observable in precision spectroscopy.

**Hydrogen 21 cm and hyperfine structure.** Each fine-structure level is further split by the interaction of the electron's magnetic moment with the nuclear magnetic moment. This **hyperfine splitting** is roughly a factor $m_e/m_p \approx 1/1836$ smaller than the fine-structure splitting. For the hydrogen ground state the hyperfine splitting is 1420 MHz ($\lambda = 21$ cm), the most famous line in radio astronomy — used to map the Milky Way, discovered the first external galaxy spiral arms, and is one of the candidate signals in SETI. Its physics is exactly the Zeeman effect of the electron's spin in the magnetic field of the proton, treated via degenerate perturbation theory with the nuclear moment.

**Intermediate-field Zeeman.** The crossover between weak-field and strong-field Zeeman has no simple analytic form. It requires numerical diagonalization. The resulting energy-vs.-field curves show a dense web of avoided crossings. Selection rules allow some crossings (where states have different $m_j$ and cannot mix) and forbid others. The pattern is computed numerically for spectroscopy databases; it is beautiful and complex.

---

## The +1 — Simulation Exercise

### Context

You are going to build a simulation of atomic energy-level splitting as a function of field strength, showing both the Zeeman weak-to-strong crossover and the Stark linear splitting of the $n = 2$ hydrogen manifold. The deliverable is `10-atoms-in-fields.html` in your working directory.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 9 — Atoms in Fields
Deliverable: 10-atoms-in-fields.html
Status: in progress

The simulation has two modes selectable by tabs: "Zeeman" and "Stark".

ZEEMAN MODE
Energy-level diagram for the hydrogen 2p manifold (j=1/2 and j=3/2
sub-levels) as a function of magnetic field B from 0 to 10 T.
At B=0, the fine-structure splitting Delta_E_fs ≈ 4.5e-5 eV separates
the two groups. For B > 0, each level splits according to:
  weak-field approximation: Delta E = g_J * mu_B * B * m_j
  strong-field approximation: Delta E = mu_B * B * (m_l + 2*m_s)
The simulation shows both limiting formulas as dashed curves and
(optionally) a numerical interpolation via 6x6 diagonalization as
solid curves. Slider for B, 0 to 10 T.

STARK MODE
Energy-level diagram for the hydrogen n=2 manifold as a function of
electric field strength E_field from 0 to 0.05 atomic units. Four
states at E_field = 0; as the field increases, two states shift by
+3*a0*e*E_field and -3*a0*e*E_field, two states remain flat. Annotate
eigenstates at the right edge. Show the 4x4 matrix live on the right.
```

### Part 2 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md, and
PROJECT.md. Read all three first.

Build 10-atoms-in-fields.html: a single self-contained HTML file using
D3 v7 from a CDN. No other external dependencies. Two modes, selectable
by tab: "Zeeman" and "Stark".

ZEEMAN MODE
SVG canvas 1100 x 600. Left panel: energy vs. B diagram for the hydrogen
2p manifold. Pin the y-axis from -0.0004 eV to +0.0004 eV relative to
the unperturbed 2p energy. Fine-structure baseline: 2p_{3/2} (j=3/2)
sits at +Delta_fs/2 = +2.25e-5 eV; 2p_{1/2} (j=1/2) sits at
-Delta_fs/2 = -2.25e-5 eV (fine-structure splitting approximately
4.5e-5 eV). For each sub-level, draw the weak-field energy curve
  E = E_fine + g_J * mu_B * B * m_j
as colored lines (teal for j=3/2, orange for j=1/2). Label each curve
with its m_j value at the right edge. Slider for B from 0 to 5 T.

Right panel: a legend showing g_J for each j value and the Landé
formula displayed as rendered math.

STARK MODE
SVG canvas 1100 x 600. Four horizontal energy lines starting at E=0
(in Hartree relative to unperturbed n=2 level) when E_field = 0.
As E_field increases from 0 to 0.05 atomic units, the lines move:
  top line: +3 * a0 * e * E_field = +3*E_field (in a.u. with a0=e=1)
  bottom line: -3 * E_field
  two middle lines: stay at 0
Label each line with its eigenstate at the right edge.
Show the 4x4 perturbation matrix W live on the right, with the only
nonzero entry highlighted in teal.
Slider for E_field from 0 to 0.05 a.u.

GLOBAL
mu_B = 5.788e-5 eV/T. Delta_fs(2p) = 4.5e-5 eV. a0 = 1 in atomic units.
Comments at every physics step. No dead code.
Runtime sanity check: at B=0, all lines should lie within 1e-10 eV of
their fine-structure baseline. At E_field=0, all Stark lines at 0.
```

### Part 3 — Exploration tasks

Run the simulation and answer the following:

1. **Zeeman mode.** Increase $B$ slowly from 0 to 5 T. At what value of $B$ does the energy spread of the $j=3/2$ quartet ($m_j = \pm 3/2, \pm 1/2$) equal the fine-structure splitting $\Delta E_{FS}$? At this point, the weak-field approximation breaks down. (The actual crossover requires the full diagonalization, but the simulation shows the limiting formulas.)

2. **Zeeman mode.** Set $B = 1$ T. The $j = 3/2$, $m_j = -1/2$ sublevel has $\Delta E = -\frac{4}{3}\cdot\frac{1}{2}\mu_B B$. The $j = 1/2$, $m_j = +1/2$ sublevel has $\Delta E = +\frac{2}{3}\cdot\frac{1}{2}\mu_B B$. Are these equal? If not, do they cross at some value of $B$ in the weak-field approximation? What would a crossing mean physically?

3. **Stark mode.** Set $E_\text{field} = 0.01$ a.u. Verify from the simulation that the upper eigenvalue is exactly $+0.03$ Hartree and the lower is $-0.03$ Hartree. Confirm the two middle lines are at zero.

4. **Stark mode.** Toggle the field up to $\mathcal{E} = 0.04$ a.u. At this field strength the outermost electron in hydrogen can classically escape over the Stark-tilted Coulomb barrier (Stark ionization threshold $\sim \mathcal{E}^4/16$ in atomic units). The simulation does not model ionization — its energy lines keep moving linearly. Note where the simulation physics ends and real physics begins.

**Extension prompt:**

```
Extend 10-atoms-in-fields.html to add a "Rabi oscillations" panel (a
third tab). Display P_down(t) = sin^2(omega_1 * t / 2) at resonance
and the off-resonant form P_down(t) = (omega_1^2 / Omega^2) *
sin^2(Omega * t / 2) where Omega = sqrt((omega - omega_0)^2 + omega_1^2).
Sliders: omega_1 (Rabi frequency, 0 to 2*pi*10 kHz), detuning
delta = omega - omega_0 (0 to 5 * omega_1_max).
The x-axis should be time from 0 to 2*pi / omega_1 * 5 (five full cycles).
Show that at delta = 0 the spin fully inverts; at delta = 2*omega_1 the
maximum flip probability is 1/5.
```

---

## References

- Griffiths, D. J. & Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed., Ch. 6. Cambridge University Press, 2018. [Standard undergraduate treatment of Zeeman, Stark, and fine structure.] `[verify]`
- Likharev, K. K. *Essential Graduate Physics — Quantum Mechanics*, §6.4, "The Zeeman Effect." LibreTexts Physics. CC BY-NC-SA 4.0. https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Essential_Graduate_Physics_-_Quantum_Mechanics_(Likharev)/06:_Perturbative_Approaches/6.04:_The_Zeeman_Effect `[verify]`
- Sakurai, J. J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed., Ch. 5. Cambridge University Press, 2020. [Anomalous Zeeman, coupling schemes.] `[verify]`
- Stephen, L., Fang, M. & Wilson, B. "Physical Principles of Nuclear Magnetic Resonance and Applications." UBC PHYS502 student project report (2016). https://phas.ubc.ca/~berciu/TEACHING/PHYS502/PROJECTS/NMR16.pdf [Rotating-frame derivation, Rabi oscillations, Bloch equations, spin echo, MRI.] `[verify]`
- Zeeman, P. "On the influence of magnetism on the nature of the light emitted by a substance." *Philosophical Magazine*, 43, 226 (1897). `[verify]`
- Rabi, I. I., Zacharias, J. R., Millman, S. & Kusch, P. "A new method of measuring nuclear magnetic moment." *Physical Review* 53, 318 (1938). [Original molecular-beam magnetic resonance.] `[verify]`
- Bloch, F. "Nuclear induction." *Physical Review* 70, 460 (1946). [Bloch equations.] `[verify]`
- Hanneke, D., Fogwell, S. & Gabrielse, G. "New measurement of the electron magnetic moment and the fine structure constant." *Physical Review Letters* 100, 120801 (2008). [Electron $g$-factor to 13 significant figures; QED test.] `[verify]`
- Stark, J. "Beobachtungen über den Effekt des elektrischen Feldes auf Spektrallinien." *Annalen der Physik* 348, 965 (1914). `[verify]`
