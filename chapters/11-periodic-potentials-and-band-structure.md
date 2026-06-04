# Chapter 11 — Periodic Potentials and the Band Structure of Solids

## TL;DR

- A perfectly periodic potential does not scatter electrons — it lets them propagate as modified plane waves (Bloch waves), with crystal momentum $k$ as a good quantum number.
- The Kronig–Penney model produces an exact transcendental dispersion relation whose allowed and forbidden energy regions are the bands and gaps.
- Gaps open at Brillouin-zone boundaries because of Bragg reflection; in the nearly-free-electron picture the gap equals $2|V_G|$, the Fourier component of the periodic potential at the reciprocal lattice vector.
- Tight-binding gives the same physics from the other end: $E(k) = E_0 - 2t\cos(ka)$, a band of width $4t$ built from atomic orbitals.
- Metals, insulators, and semiconductors are the same physics with different band filling.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **State** Bloch's theorem and explain why lattice periodicity makes crystal momentum a good quantum number. *(Remember/Understand — Bloom levels 1–2)*

2. **Derive** the Kronig–Penney dispersion relation in the delta-function limit and identify allowed bands from the condition $|\cos(ka)| \leq 1$. *(Analyze — Bloom level 4)*

3. **Apply** the nearly-free-electron picture to compute the band gap at the first Brillouin-zone boundary as $\Delta E = 2|V_G|$. *(Apply — Bloom level 3)*

4. **Construct** the tight-binding dispersion $E(k) = E_0 - 2t\cos(ka)$ and identify the effective mass at the band bottom and top. *(Analyze — Bloom level 4)*

5. **Classify** a material as metal, insulator, or semiconductor from its band structure and electron count, and simulate the Kronig–Penney dispersion numerically. *(Evaluate/Create — Bloom levels 5–6)*

---

## A Brief Orientation: Crystals and Reciprocal Space

This is the book's first solid-state chapter. Most of what has come before concerned a single atom or a few particles; now the system is $\sim 10^{23}$ atoms arranged in a repeating lattice. Before the quantum mechanics, a two-paragraph orientation to the geometry.

**The direct lattice.** A crystalline solid is built from a unit cell — the smallest repeating unit — tiled in three dimensions. In one dimension this is just an atom (or a molecule) repeated with period $a$. The lattice positions are $x_n = na$ for integers $n$. The lattice constant $a$ is typically 2–6 Å for real materials.

**The reciprocal lattice.** Every periodic structure has a dual: the reciprocal lattice, whose points are the spatial frequencies at which the periodic structure has Fourier components. In one dimension the reciprocal lattice points are $G_n = 2\pi n/a$ for integers $n$. The **first Brillouin zone** (BZ) is the Wigner–Seitz cell of the reciprocal lattice: in 1D it is the interval $k \in [-\pi/a, \pi/a]$.

Why does this matter? Bloch's theorem will show that $k$ and $k + G$ describe the same physical state; so all distinct momenta lie within a single Brillouin zone. The reciprocal lattice is the natural domain for discussing electron propagation in a crystal.

In three dimensions the geometry is richer. The reciprocal lattice of an FCC direct lattice is BCC, and vice versa. Silicon (diamond cubic) has a first BZ that is a truncated octahedron, and the real band structure of silicon is plotted along high-symmetry paths through that 3D zone. This chapter develops the full physics in 1D, where the geometry is transparent, and points toward 3D at the end.

---

## Core Development

### 1. Bloch's Theorem

Consider a one-dimensional crystal: an electron moving in a potential $V(x)$ with period $a$, so $V(x + a) = V(x)$ for all $x$.

**The key observation.** Define the **translation operator** $\hat{T}_a$ by $(\hat{T}_a f)(x) = f(x+a)$. Because $V(x+a) = V(x)$, the Hamiltonian commutes with $\hat{T}_a$:

$$[\hat{H}, \hat{T}_a] = 0$$

Therefore $\hat{H}$ and $\hat{T}_a$ share a common set of eigenstates. Every energy eigenstate can be chosen to also be an eigenstate of $\hat{T}_a$.

**The eigenvalue of $\hat{T}_a$.** Because translation is unitary ($\hat{T}_a^\dagger \hat{T}_a = 1$), its eigenvalues have magnitude 1 and can be written as $e^{i\theta}$ for some real $\theta$. We write $\theta = ka$ and call $k$ the **crystal momentum** (or **quasi-momentum**). Then:

$$\psi(x + a) = e^{ika}\psi(x)$$

**Bloch's theorem.** Any eigenstate $\psi(x)$ satisfying the above condition can be written as

$$\psi_{n,k}(x) = e^{ikx}\,u_{n,k}(x)$$

where $u_{n,k}(x)$ is periodic with the same period $a$ as the lattice: $u_{n,k}(x+a) = u_{n,k}(x)$. The integer $n$ is the **band index** labeling distinct solutions at the same $k$.

*Proof.* Define $u(x) = e^{-ikx}\psi(x)$. Then $u(x+a) = e^{-ik(x+a)}\psi(x+a) = e^{-ikx-ika}e^{ika}\psi(x) = u(x)$. Done.

**Physical content.** Electrons in a perfectly periodic potential are not scattered by the lattice — they propagate as Bloch waves. The crystal momentum $k$ is as good a quantum number as the free-electron momentum $p = \hbar k$. The crucial difference: $k$ is only defined modulo $G = 2\pi/a$ (adding a reciprocal lattice vector gives the same physical state), so all distinct $k$ values lie in the first BZ. The band index $n$ distinguishes the multiple solutions that exist at the same $k$ once the lattice modifies the free-electron parabola.

**Historical note.** Bloch derived this theorem in 1928 as part of his PhD thesis under Heisenberg. The central insight — that a perfectly periodic potential produces propagating, not scattered, waves — was counterintuitive to the physicists of the day, who expected electrons to bounce randomly off every atom. Bloch's theorem was the beginning of the modern theory of metals.

---

### 2. The Kronig–Penney Model

The Kronig–Penney model (1931) is the canonical analytically tractable example of a periodic potential. We use the delta-function version, which gives the full physics with the minimum of algebra.

**Setup.** The potential is a sequence of delta-function barriers with period $a$:

$$V(x) = \frac{\hbar^2 P}{ma}\sum_n\delta(x - na)$$

where $P$ is a dimensionless **barrier strength** parameter. The limit $P \to 0$ recovers free electrons; $P \to \infty$ corresponds to an infinite array of infinitely deep square wells (isolated atoms).

*Derivation route.* Between delta functions the Schrödinger equation is just the free-particle equation with $E = \hbar^2\alpha^2/2m$:

$$\psi'' + \alpha^2\psi = 0, \qquad \alpha = \sqrt{2mE}/\hbar$$

In the region $0 < x < a$, the general solution is $A e^{i\alpha x} + B e^{-i\alpha x}$. Applying Bloch periodicity at $x = a$ (i.e., $\psi(a) = e^{ika}\psi(0)$) and the matching conditions at the delta-function at $x = 0$ — continuity of $\psi$ plus a jump in $\psi'$ of magnitude $2P/a$ — produces a $2\times 2$ linear system. The consistency condition (determinant = 0) gives:

$$\boxed{\cos(ka) = \cos(\alpha a) + \frac{P}{\alpha a}\sin(\alpha a)}$$

This is the **Kronig–Penney dispersion relation**. It is a relation between the energy $E$ (encoded in $\alpha = \sqrt{2mE}/\hbar$) and the crystal momentum $k$.

**Reading the dispersion relation.** Define the right-hand side as

$$f(\alpha a) = \cos(\alpha a) + \frac{P}{\alpha a}\sin(\alpha a)$$

The left side $\cos(ka)$ is bounded: $|\cos(ka)| \leq 1$.

- Where $|f(\alpha a)| \leq 1$: a real $k$ exists, and the electron can propagate. These are the **allowed bands**.
- Where $|f(\alpha a)| > 1$: no real $k$ satisfies the equation. These are the **forbidden gaps** (band gaps).

As $\alpha a$ increases from 0, $f(\alpha a)$ oscillates with increasing amplitude — it periodically exceeds $\pm 1$. Each excursion beyond $\pm 1$ corresponds to a forbidden gap. The bands and gaps alternate in a pattern that repeats in $\alpha a$ approximately every $\pi$.

**Effect of barrier strength.** As $P$ increases, the amplitude of $f(\alpha a)$ increases, making the excursions beyond $\pm 1$ larger. Larger $P$ means wider gaps and narrower bands — the electron is more tightly confined and the lattice is more important. At $P = 0$: $f = \cos(\alpha a)$, always in $[-1,1]$, giving a continuous free-electron spectrum (no gaps). As $P \to \infty$: the allowed bands shrink to zero width and the spectrum becomes discrete — the isolated-atom limit.

**The reduced zone scheme.** For each allowed energy $E$, the dispersion relation gives a value of $k$ in $[-\pi/a, \pi/a]$. Plotting $E$ vs. $k$ in this interval gives the **reduced-zone scheme** band diagram. Each successive band occupies the same interval $[-\pi/a, \pi/a]$ with a different functional form. This is the standard way band structures are plotted for all real materials.

---

### 3. Worked Example: The Kronig–Penney First Band Gap

**Setup.** Choose $P = 3\pi/2 \approx 4.71$ (moderately strong barriers).

**Finding the gap.** The function $f(\alpha a) = \cos(\alpha a) + \frac{P}{\alpha a}\sin(\alpha a)$ must exit and re-enter the interval $[-1, 1]$ to produce a gap.

At $\alpha a = \pi$ (which would be $k = \pi/a$ in the free-electron case, the first zone boundary):
$$f(\pi) = \cos(\pi) + \frac{P}{\pi}\sin(\pi) = -1 + 0 = -1$$

This is exactly at the boundary — barely allowed. Now look at what happens just above $\alpha a = \pi$.

For small $\epsilon > 0$, at $\alpha a = \pi + \epsilon$:
$$f(\pi + \epsilon) \approx \cos(\pi + \epsilon) + \frac{P}{\pi + \epsilon}\sin(\pi + \epsilon)$$
$$\approx (-1 + \frac{\epsilon^2}{2}) + \frac{P}{\pi}(-\epsilon) = -1 + \frac{\epsilon^2}{2} - \frac{P\epsilon}{\pi}$$

For $\epsilon > 0$ small, the $-P\epsilon/\pi$ term dominates: $f < -1$. The dispersion relation has no real $k$ solution — we are in the gap.

The gap closes when $f(\alpha a) = -1$ again, at some $\alpha a = \pi + \delta$ where $\delta$ satisfies the implicit equation $f(\pi + \delta) = -1$. For $P = 3\pi/2$, numerical evaluation gives this occurs near $\alpha a \approx 4.42$ (just above $\pi \approx 3.14$).

**What the gap means physically.** The first allowed band runs from $\alpha a \in [0, \pi]$ (very small energies up to the zone boundary at $E_1 = \hbar^2\pi^2/2ma^2$). The gap sits from $\alpha a \approx \pi$ to $\approx 4.42$. The second allowed band begins at $\alpha a \approx 4.42$ and runs to $\alpha a \approx 2\pi = 6.28$.

**Numerically.** In units where $\hbar^2/2m = 1$ and $a = 1$, the first gap runs from $E = \pi^2 \approx 9.87$ to $E \approx (4.42)^2 \approx 19.5$. The gap width grows with $P$; for $P = 3\pi/2$ the fractional gap width ($\Delta E / E_\text{gap center}$) is approximately 65%.

**The simulation procedure.** Sweep $\alpha a$ from $0$ to $6\pi$. At each point compute $f(\alpha a)$. If $|f| \leq 1$, assign $k = \arccos(f)/a$ and plot the point $(k, E) = (k, \hbar^2\alpha^2/2m)$ in the reduced zone scheme. Color allowed-band points teal, shade gap regions gray. See the +1 simulation for the full implementation.

> **[BAND DIAGRAM FIGURE NEEDED]** A figure showing the Kronig–Penney dispersion for $P = 3\pi/2$ in both the extended and reduced zone schemes, with allowed bands shaded and gap regions labeled. Commission from illustrator or generate computationally.

---

### 4. The Nearly-Free-Electron Picture and Gap Opening

The Kronig–Penney model treats the periodic potential exactly. The **nearly-free-electron** (NFE) model starts from the opposite extreme: free electrons ($V = 0$) with the periodic potential added as a small perturbation.

**Setup.** Write the potential as a Fourier series over reciprocal lattice vectors $G = 2\pi n/a$:

$$V(x) = \sum_G V_G e^{iGx}$$

The unperturbed states are plane waves $|k\rangle$ with energies $E^{(0)}_k = \hbar^2k^2/2m$.

**Why normal perturbation theory fails at zone boundaries.** Away from the zone boundary, all neighboring unperturbed states have different energies and first-order perturbation theory works fine. But at $k = \pi/a$, two states become degenerate: $|k = \pi/a\rangle$ and $|k = -\pi/a\rangle = |k = \pi/a - G_1\rangle$ (where $G_1 = 2\pi/a$) have exactly the same energy $E^{(0)} = \hbar^2\pi^2/2ma^2$. The denominator in the first-order state correction vanishes — this is degenerate perturbation theory.

**Degenerate perturbation theory at the zone boundary.** Build the $2\times 2$ matrix of $V$ between the two degenerate states:

$$W = \begin{pmatrix} \langle k|V|k\rangle & \langle k|V|k-G_1\rangle \\ \langle k-G_1|V|k\rangle & \langle k-G_1|V|k-G_1\rangle \end{pmatrix}$$

The diagonal elements are $V_0 = 0$ (the average of the potential, which we can set to zero). The off-diagonal element is $V_{G_1}$, the first Fourier component of $V$. The matrix is:

$$W = \begin{pmatrix} 0 & V_{G_1}^* \\ V_{G_1} & 0 \end{pmatrix}$$

The eigenvalues are $\pm |V_{G_1}|$. The energy at the zone boundary splits into

$$E_\pm = \frac{\hbar^2\pi^2}{2ma^2} \pm |V_{G_1}|$$

$$\boxed{\text{Band gap at first zone boundary} = 2|V_{G_1}|}$$

**The gap equals twice the magnitude of the relevant Fourier component of the periodic potential.** Strong potential (large $|V_G|$) means a wide gap; weak potential means a narrow gap. In the limit $V_G \to 0$, the gap closes and we recover the free-electron parabola.

**Physical picture: Bragg reflection.** At $k = \pi/a$, the de Broglie wavelength $\lambda = 2\pi/k = 2a$ satisfies the Bragg condition for reflection from a periodic lattice with spacing $a$. Forward and backward traveling waves ($e^{i\pi x/a}$ and $e^{-i\pi x/a}$) mix equally and form standing waves:

$$\psi_+ \propto \cos(\pi x/a), \qquad \psi_- \propto \sin(\pi x/a)$$

The probability density $|\psi_+|^2 \propto \cos^2(\pi x/a)$ peaks at the lattice sites; $|\psi_-|^2 \propto \sin^2(\pi x/a)$ peaks between sites. If the lattice potential is attractive at the ion positions (as it is — ions attract electrons), $\psi_+$ has lower potential energy and $\psi_-$ has higher potential energy. Their energy difference is exactly $2|V_{G_1}|$. This is the gap.

> **[STANDING WAVE FIGURE NEEDED]** A figure showing $|\psi_+|^2$ and $|\psi_-|^2$ superimposed on the periodic lattice potential, illustrating why the symmetric (cosine) standing wave has lower energy than the antisymmetric (sine) wave. Commission from illustrator.

---

### 5. The Tight-Binding Picture

The NFE model works near the free-electron limit ($P \to 0$). The **tight-binding** (TB) model works near the atomic limit ($P \to \infty$): start from isolated atoms and turn on the overlap between neighboring orbitals.

**Setup.** Each atom has a localized orbital $|\phi_n\rangle$ centered at site $x = na$, with energy $E_0$ (the atomic eigenvalue). When atoms are placed in a crystal, adjacent orbitals overlap slightly, allowing electrons to "hop" from one site to the next.

**The LCAO ansatz.** Write the Bloch state as a linear combination of atomic orbitals (LCAO):

$$|\psi_k\rangle = \sum_n e^{ikna}\,|\phi_n\rangle$$

The phase factor $e^{ikna}$ is chosen to satisfy Bloch's theorem: shifting by one lattice site multiplies by $e^{ika}$.

**The energy.** Evaluate $\langle\psi_k|\hat{H}|\psi_k\rangle/\langle\psi_k|\psi_k\rangle$. The diagonal term gives $E_0$. The nearest-neighbor off-diagonal terms (hopping from site $n$ to site $n\pm 1$) give the **transfer integral** (or **hopping integral**):

$$t = -\langle\phi_{n+1}|\hat{H}|\phi_n\rangle$$

(The sign convention is chosen so $t > 0$ for a bonding orbital.) Neglecting all longer-range hoppings:

$$\boxed{E(k) = E_0 - 2t\cos(ka)}$$

**Reading the dispersion.** At $k = 0$: $E = E_0 - 2t$ (band bottom, symmetric superposition). At $k = \pm\pi/a$: $E = E_0 + 2t$ (band top, antisymmetric superposition). The bandwidth is $4t$.

**Effective mass.** Near the band bottom ($k \approx 0$), expand:

$$E(k) \approx (E_0 - 2t) + ta^2k^2 = E_\text{bottom} + \frac{\hbar^2k^2}{2m^*}$$

where the **effective mass** is $m^* = \hbar^2/(2ta^2)$. Strong hopping (large $t$) means light effective mass — the electron propagates easily. Near the band top ($k \approx \pi/a$), the band curves downward: $m^* = -\hbar^2/(2ta^2)$ is negative. An electron near the band top behaves as a **hole** — a positively-charged quasiparticle.

**Metals, insulators, and semiconductors.** Band filling is governed by the Pauli exclusion principle: each $k$ state can hold 2 electrons (spin up and down). The first BZ contains one $k$ value per real-space unit cell (per atom), so the first band can hold 2 electrons per atom.

- **1 electron per atom** → half-filled band → Fermi level cuts through the band → **metal** (e.g., sodium, lithium).
- **2 electrons per atom, one orbital per atom** → completely filled band, empty next band → **insulator** (large gap $\gg k_BT$) or **semiconductor** (gap $\lesssim$ few eV; thermally excited carriers possible). Examples: Si (gap 1.12 eV), Ge (0.67 eV), GaAs (1.42 eV), diamond (5.5 eV).
- **Overlap between adjacent bands** → Fermi level in both → **semimetal** (e.g., graphite).

> **[BAND FILLING FIGURE NEEDED]** A schematic showing three side-by-side band diagrams: metal (half-filled), semiconductor (filled valence + small gap + empty conduction), and insulator (filled valence + large gap), each with the Fermi level marked. Commission from illustrator.

**NFE vs. tight-binding.** These two pictures are complementary. The NFE model starts from free electrons and explains gaps as perturbative corrections from the weak lattice potential. The tight-binding model starts from localized atomic orbitals and explains bands as broadening due to inter-site hopping. Real materials (silicon, GaAs) sit between these extremes; density functional theory (DFT) handles them from first principles. The Kronig–Penney model interpolates between the limits as $P$ is varied: at $P = 0$ it is NFE; at $P \to \infty$ it approaches isolated atoms.

---

### 6. Zone Schemes

Three ways to plot the same information:

**Extended zone scheme.** The first band occupies BZ 1 ($k \in [-\pi/a, \pi/a]$), the second band occupies BZ 2 (the next two segments $k \in [-2\pi/a, -\pi/a]$ and $[\pi/a, 2\pi/a]$), and so on. This representation shows the free-electron parabola ancestry: each band is a segment of $E = \hbar^2k^2/2m$ gapped and folded back.

**Reduced zone scheme.** All bands are folded into the first BZ by subtracting appropriate reciprocal lattice vectors. Every band is then a distinct curve over $k \in [-\pi/a, \pi/a]$. This is the canonical representation for solid-state band diagrams.

**Repeated zone scheme.** The reduced-zone dispersion is extended periodically over all $k$. Useful for visualizing group velocity (slope $dE/dk$) continuity.

Physically all three are equivalent. The reduced zone scheme is preferred because it makes explicit that all distinct crystal momenta lie in the first BZ.

---

## Common Misconceptions

**"The periodic potential scatters electrons at every lattice site."** In a perfectly periodic potential there is zero net scattering. Scattering from each site interferes coherently; the result is a Bloch wave that propagates indefinitely. Real resistivity comes from *imperfections* — defects, impurities, phonons — that break the periodicity. This is why a perfect crystal at zero temperature has zero electrical resistance.

**"Crystal momentum $k$ is the same as regular momentum $p/\hbar$."** Crystal momentum is a good quantum number, but it is not momentum — it is defined only modulo $G = 2\pi/a$. The true momentum of a Bloch state is not $\hbar k$ but a complicated integral over the periodic part $u_{n,k}(x)$. This is why the effective mass $m^*$ can differ dramatically from the free-electron mass, and can even be negative near the band top.

**"Semiconductors are insulators with a smaller gap."** Topologically, yes — both have a fully occupied valence band and an empty conduction band. The distinction is quantitative ($\Delta E \lesssim$ a few eV for semiconductors vs. $> 4$ eV for insulators), but the physics of carrier generation and doping makes semiconductors qualitatively different in practice. An insulator does not have a useful carrier density at room temperature; a semiconductor does.

**"The tight-binding band $E(k) = E_0 - 2t\cos(ka)$ has the same width regardless of lattice constant."** The bandwidth $4t$ depends strongly on $a$ because the hopping integral $t \propto e^{-a/d}$ (orbital overlap decays exponentially with distance $d$ the decay length of the atomic orbital). Compressing the lattice increases $t$ and widens the band; stretching it narrows the band until the atoms are isolated ($t \to 0$, zero-width bands at $E_0$).

**"The Kronig–Penney delta-function model is realistic."** It is a pedagogical tool. Real crystal potentials are smooth, three-dimensional, and self-consistent (the potential is determined by the electron density, which determines the wavefunctions, which determine the density — this is the DFT self-consistency loop). The KP model captures the topology of band structure correctly but not the quantitative band widths or gaps of real materials.

**"Band theory works for all materials."** Band theory assumes independent electrons. Strongly correlated systems — materials where electron-electron Coulomb repulsion is comparable to or larger than the bandwidth — require physics beyond band theory. Mott insulators are predicted to be metals by band theory (odd electron count, half-filled band) but are insulators due to strong correlations. Cuprate high-temperature superconductors are Mott-insulator parent compounds. This is an active research frontier.

---

## Exercises

### Warm-up

**11.1** Bloch's theorem. (a) The translation operator $\hat{T}_a$ satisfies $(\hat{T}_a\psi)(x) = \psi(x+a)$. Show that $[\hat{H}, \hat{T}_a] = 0$ when $V(x+a) = V(x)$. (b) Show that if $\hat{T}_a$ has eigenvalue $\lambda$, then $|\lambda| = 1$ (use the fact that $\hat{T}_a$ is unitary: $\hat{T}_{-a} = \hat{T}_a^\dagger$). (c) Write $\lambda = e^{ika}$ and verify that $\psi_{n,k}(x) = e^{ikx}u_{n,k}(x)$ with $u_{n,k}$ periodic satisfies the Bloch periodicity condition $\psi(x+a) = e^{ika}\psi(x)$. *(Tests: proof that $H$ and $T_a$ commute; unitarity argument; verification of the Bloch form.)*

**11.2** Free-electron limit. (a) Set $P = 0$ in the Kronig–Penney dispersion relation $\cos(ka) = \cos(\alpha a)$. Show that this implies $k = \alpha$ (or $k = \alpha + 2\pi n/a$ for integers $n$), recovering the free-electron dispersion $E = \hbar^2k^2/2m$. (b) In the reduced zone scheme for the free electron, the "first band" is $E = \hbar^2k^2/2m$ for $k \in [-\pi/a, \pi/a]$, the "second band" is the parabola centered at $G_1 = 2\pi/a$ folded into the same interval, and so on. Sketch the first three bands of the free-electron reduced-zone scheme. (c) At $k = \pi/a$, what are the energies of the top of the first band and the bottom of the second band in the free-electron limit? Are they degenerate? *(Tests: KP dispersion in the P→0 limit; reduced-zone construction; zone-boundary degeneracy.)*

**11.3** Tight-binding dispersion. (a) For the tight-binding band $E(k) = E_0 - 2t\cos(ka)$, compute $dE/dk$ and $d^2E/dk^2$ as functions of $k$. (b) Show that the effective mass $m^* = \hbar^2/(d^2E/dk^2)$ equals $\hbar^2/(2ta^2)$ at $k = 0$ (band bottom) and $-\hbar^2/(2ta^2)$ at $k = \pi/a$ (band top). (c) For $t = 1.0$ eV and $a = 3.0$ Å, compute $m^*$ at the band bottom in units of the free-electron mass $m_e$. *(Tests: derivatives of the cosine dispersion; effective mass formula; numerical evaluation.)*

### Application

**11.4** Kronig–Penney gap width. Use the dispersion relation $f(\alpha a) = \cos(\alpha a) + (P/\alpha a)\sin(\alpha a)$ with $P = \pi$ (a moderately weak barrier). (a) Evaluate $f$ at $\alpha a = \pi$ and $\alpha a = 2\pi$. Are these points in allowed bands or gaps? (b) Find numerically (by trial values of $\alpha a$) the range of $\alpha a$ near $\pi$ where $|f| > 1$, i.e., locate the first gap. (c) Compute the energies at the gap edges (in units of $\hbar^2/2ma^2$) and find the gap width. (d) Repeat for $P = 3\pi/2$. How does the gap width scale with $P$? *(Tests: numerical evaluation of the KP dispersion; gap identification; dependence on barrier strength.)*

**11.5** Nearly-free-electron gap. A 1D crystal has period $a = 3.0$ Å and a weak periodic potential $V(x) = 2V_1\cos(2\pi x/a)$. (a) Write down the first Fourier component $V_{G_1}$ (where $G_1 = 2\pi/a$). (b) The band gap at the first zone boundary is $\Delta E = 2|V_{G_1}|$. Compute $\Delta E$ in eV for $V_1 = 0.5$ eV. (c) Compute the free-electron energy at the zone boundary $E_0 = \hbar^2(\pi/a)^2/2m_e$ in eV. What is the fractional gap width $\Delta E / E_0$? Is perturbation theory justified here? *(Tests: Fourier decomposition of a simple potential; NFE gap formula; validity check.)*

**11.6** Band filling and material classification. A one-dimensional tight-binding model has one atomic orbital per site, lattice constant $a$, and hopping $t = 1.2$ eV. (a) If each atom contributes 1 valence electron, where does the Fermi level sit within the band? Is this system a metal or insulator? (b) If each atom contributes 2 valence electrons, where does the Fermi level sit? What is the band gap (using the KP model, or just state conceptually)? (c) Germanium has 4 valence electrons per atom and a band gap of 0.67 eV. Explain qualitatively how sp³ hybridization produces 4 bonds per atom and relates to the 2-electron-per-bond counting that fills the valence band. *(Tests: Fermi level and band filling; metal/insulator criterion; qualitative connection to chemistry.)*

### Synthesis

**11.7** Derive the tight-binding dispersion $E(k) = E_0 - 2t\cos(ka)$ from the LCAO ansatz. (a) Write the Hamiltonian as $\hat{H} = \hat{H}_\text{atom} + \hat{V}$, where $\hat{H}_\text{atom}$ is the sum of individual atomic Hamiltonians and $\hat{V}$ represents the additional potential from all other atoms. Define the on-site energy $\epsilon_0 = \langle\phi_0|\hat{H}|\phi_0\rangle$ and the hopping integral $-t = \langle\phi_1|\hat{H}|\phi_0\rangle$ (nearest-neighbor only). (b) Evaluate $\langle\psi_k|\hat{H}|\psi_k\rangle$ using the Bloch sum $|\psi_k\rangle = N^{-1/2}\sum_n e^{ikna}|\phi_n\rangle$, keeping only on-site and nearest-neighbor terms. (c) Show the result is $E_0 - 2t\cos(ka)$ where $E_0 = \epsilon_0 + \langle\phi_0|\hat{V}|\phi_0\rangle$. *(Tests: derivation of a central result from the ansatz; matrix element computation; LCAO approximation.)*

**11.8** Zone-boundary standing waves. At $k = \pi/a$ in a 1D crystal, the two degenerate free-electron states are $|+\rangle \sim e^{i\pi x/a}$ and $|-\rangle \sim e^{-i\pi x/a}$. Their symmetric and antisymmetric combinations are $\psi_\pm(x) = (e^{i\pi x/a} \pm e^{-i\pi x/a})/\sqrt{2}$, i.e., $\psi_+ \propto \cos(\pi x/a)$ and $\psi_- \propto \sin(\pi x/a)$. (a) Compute $|\psi_+(x)|^2$ and $|\psi_-(x)|^2$ and identify where each is peaked relative to the lattice sites at $x = na$. (b) A 1D ionic lattice has negative ions at $x = na$ (attracting electrons). Which standing wave, $\psi_+$ or $\psi_-$, has lower potential energy? Which forms the top of the valence band and which the bottom of the conduction band? (c) The potential is $V(x) = -|V_1|\cos(2\pi x/a)$. Compute $\langle\psi_\pm|V|\psi_\pm\rangle$ and verify that the energy difference is $2|V_1|$. *(Tests: explicit computation of the gap-opening mechanism; density localization; NFE gap derivation via direct integration.)*

**11.9** Simulation as experiment. Run the Kronig–Penney simulation from the +1 exercise with $P = 3\pi/2$. (a) From the plot, estimate the width of the first gap in units of $E_1 = \hbar^2\pi^2/2ma^2$ (the energy at the first zone boundary for free electrons). (b) Increase $P$ to $6$. Does the gap width increase, decrease, or stay the same? Quantify. (c) Set $P = 0.5$ (weak barriers). Does a visible gap appear in the simulation? Compare its width to the NFE prediction $\Delta E = 2|V_{G_1}|$, approximating $V_{G_1} \approx P\hbar^2/(ma^2)$ for weak delta-function barriers. *(Tests: reading dispersion from simulation; dependence on barrier strength; connection between KP and NFE pictures.)*

---

## Still Puzzling

**Topological insulators.** In the 1980s, theorists began asking not just how wide the band gap is, but what *shape* the electron wavefunctions trace out as $k$ sweeps around the Brillouin zone. This is a topological question — it measures a global property of the Bloch functions $u_{n,k}$, not a local one. The relevant quantity is the **Berry phase** (or **Chern number**): a topological invariant that can be 0 or 1 (in 2D), with 1 signifying a topological insulator. Topological insulators are bulk insulators with a band gap, but their surfaces necessarily carry conducting states — not because of chemistry or disorder, but because of topology. The surface states cannot be removed without closing the bulk gap. This was predicted theoretically around 2005–2007 (Kane & Mele; Bernevig, Hughes & Zhang) and confirmed experimentally in Bi₁₋ₓSbₓ alloys and HgTe quantum wells. The field of topological materials now encompasses topological semimetals (Weyl, Dirac), axion insulators, and higher-order topological phases. The Bloch theorem is the foundation; what is new is asking about the global topology of Bloch bands.

**Flat bands and correlated physics.** The tight-binding bandwidth is $4t$, where $t$ is the hopping integral. In most systems, $t$ is large and bands are wide. But in **moiré superlattices** — formed by stacking two layers of graphene at a small twist angle — the effective periodicity is much larger (the moiré period $a_M \sim a/\theta$ where $\theta$ is the twist angle in radians), hopping across the moiré unit cell is small, and bands can become nearly flat ($4t \to 0$). In flat bands the kinetic energy is quenched and electron-electron interactions dominate. At the "magic angle" of $\sim 1.1°$, twisted bilayer graphene becomes superconducting below $\sim 1.7$ K (Cao et al., *Nature*, 2018). The physics is not understood from band theory alone — correlations are essential. Kronig–Penney with a very large $P$ (deep potential wells, narrow bands) is a cartoon of the same physics.

**The band-gap problem in DFT.** Density functional theory with the local density approximation (LDA) systematically underestimates semiconductor band gaps — often by 30–50%. Silicon's calculated gap is $\sim 0.6$ eV versus the measured 1.12 eV. The failure is not in the Kohn–Sham eigenvalues per se but in their interpretation: the Kohn–Sham gap is not the true quasiparticle gap. Corrections from the GW approximation (Hedin 1965) or hybrid functionals (HSE06) bring computed gaps into agreement with experiment. This remains an active area of computational materials science.

---

## The +1 — Simulation Exercise

### Context

You are going to build a simulation of the Kronig–Penney dispersion — plotting the allowed bands and forbidden gaps as a function of energy, and folding the result into the reduced-zone scheme. The deliverable is `11-periodic-potentials.html` in your working directory.

### Part 1 — Update `PROJECT.md`

```
Append a new entry to PROJECT.md:

Chapter 11 — Periodic Potentials and Band Structure
Deliverable: 11-periodic-potentials.html
Status: in progress

The simulation has two modes selectable by tabs:
"Kronig-Penney dispersion" and "Tight-binding comparison".

KRONIG-PENNEY MODE
Left panel (600 px wide): plot of f(alpha*a) vs. alpha*a from 0 to 6*pi.
The function is f = cos(alpha*a) + (P / (alpha*a)) * sin(alpha*a).
Shade in teal the regions where |f| <= 1 (allowed bands).
Shade in gray the regions where |f| > 1 (forbidden gaps).
Draw horizontal dashed lines at f = +1 and f = -1.

Right panel (500 px wide): reduced-zone E(k) plot. For each alpha*a
where |f| <= 1, compute k = arccos(f) / a and E = (hbar * alpha)^2 / (2m).
Plot E vs. k folded into [-pi/a, pi/a]. Use natural units with
hbar = 1, m = 1, a = 1 (so energies are in units of hbar^2/2m/a^2 = 1).

Slider for P from 0 to 6*pi (step 0.1). At P = 0, no gaps; at large P,
wide gaps. Update both panels live.

Label the first gap on the right panel with its width in natural units.

TIGHT-BINDING COMPARISON MODE
Overlay on the same reduced-zone diagram:
  - The KP numerical dispersion (teal dots)
  - The tight-binding fit E(k) = E_0 - 2t * cos(k) (orange curve)
Automatically fit E_0 and t to the KP first band by matching the
midpoint and bandwidth: E_0 = (E_top + E_bottom) / 2, t = (E_top - E_bottom) / 4.
Sliders: P (0 to 6*pi), band index selector (first or second band).
Display the fitted t value in eV-equivalent.
```

### Part 2 — The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md,
and PROJECT.md. Read all three first.

Build 11-periodic-potentials.html: a single self-contained HTML file
using D3 v7 from CDN. No other external dependencies. Two modes
selectable by tabs at the top.

KRONIG-PENNEY MODE
Left SVG panel 550 x 500:
  x-axis: alpha*a from 0 to 6*pi, labeled with tick marks at pi, 2*pi, ...6*pi
  y-axis: f(alpha*a) from -3 to +3
  Plot f(alpha*a) = cos(alpha*a) + (P / alpha*a) * sin(alpha*a) as a
  black line. At alpha*a = 0, f → 1 + P (by L'Hopital; handle this
  separately to avoid 0/0).
  Shade teal between the curve and the x-axis where |f| <= 1.
  Add horizontal dashed red lines at ±1.
  Update continuously as P slider changes.

Right SVG panel 550 x 500:
  x-axis: k from -pi to pi (reduced zone, in units of 1/a)
  y-axis: E from 0 to max_E (auto-scaled to show at least 4 bands)
  For each point alpha*a where |f| <= 1, compute:
    k_raw = arccos(f(alpha*a)) / a
    band_index = floor(alpha*a / pi)
    if band_index is even: k = k_raw
    if band_index is odd:  k = pi - k_raw (fold back)
    E = (alpha*a)^2  (in natural units with hbar=m=a=1)
  Plot each (k, E) as a small teal dot.
  Shade gap regions on the E axis gray.

Controls:
  P slider, range 0 to 6*pi, step 0.05, default 3*pi/2. Label: "P (barrier strength)"
  Resolution: sweep alpha*a from 0.001 to 6*pi in 5000 steps.

Runtime sanity check (to console):
  At P = 0, all 5000 points should be colored allowed (teal). Log: "P=0 check: N_forbidden = [count]" (should be 0).
  At P = 3*pi/2, the first gap should cover alpha*a approximately [pi, 4.42]; log the gap boundaries found.

TIGHT-BINDING COMPARISON MODE
Use the same right panel layout. Add an orange overlay curve:
  For the currently selected band (band 1 or band 2, via toggle button):
    Find E_bottom = min E in that band, E_top = max E in that band.
    Compute t = (E_top - E_bottom) / 4, E_0 = (E_top + E_bottom) / 2.
    Plot E_tb(k) = E_0 - 2*t*cos(k) as an orange curve over k in [-pi, pi].
  Display text below: "Tight-binding fit: E_0 = [val], t = [val]"
  Compare visually: at P = 3*pi/2, the first band should be well
  approximated by the cosine; agreement gets worse as P increases
  (bands become narrower and flatter, eventually delta-function-like).

Comments at every non-trivial physics step.
```

### Part 3 — Exploration tasks

1. **Kronig–Penney mode.** Set $P = 3\pi/2$. From the left panel (f vs. $\alpha a$), identify the first three allowed bands and the first two gaps. Read off the approximate $\alpha a$ values where bands start and end.

2. Increase $P$ to $6\pi$. How does the width of the first gap change relative to the first band? Describe qualitatively: as $P \to \infty$, what does the band structure approach?

3. Set $P = 0.5$ (weak potential). Is a gap visible? Compare the gap width to the NFE prediction $\Delta E \approx 2|V_{G_1}| \approx 2P\hbar^2/(ma^2)$ in natural units.

4. **Tight-binding comparison mode.** For the first band at $P = 3\pi/2$, record the fitted values of $E_0$ and $t$. Now switch to the second band — how does $t$ compare? (Higher bands are typically wider, meaning larger effective $t$.)

5. At $P = 3\pi/2$, band 1, the tight-binding fit should track the KP dispersion closely near $k = 0$ and deviate near $k = \pi/a$. Describe the nature of the deviation. Why does tight-binding fail near the zone boundary?

**Extension prompt:**

```
Extend 11-periodic-potentials.html to add a third mode: "3D Brillouin
zone orientation". Display a simple SVG schematic (no WebGL needed) of
the first BZ for three common lattice types:
  - 1D chain: a line segment from -pi/a to pi/a
  - 2D square lattice: a square from -pi/a to pi/a in both kx and ky
  - 2D hexagonal (triangular) lattice: a hexagon with vertices at (0, 4pi/(3a))
    and rotations by multiples of 60 degrees

For each, label the high-symmetry points (Gamma at origin, X and M for
square; K and M for hexagonal). This is a schematic — no calculations
needed, just accurately labeled geometry.

Add a toggle: "show free-electron circles" — draws circles of constant
energy (the free-electron Fermi surface) at two radii corresponding to
1 and 2 electrons/atom. Highlight where the circle intersects the BZ
boundary (potential gap opening sites).

This is a purely visual orientation aid for students who will encounter
3D band structures in later courses.
```

---

## References

- Kronig, R. de L. & Penney, W. G. "Quantum mechanics of electrons in crystal lattices." *Proceedings of the Royal Society A* 130, 499–513 (1931). `[verify]`
- Bloch, F. "Über die Quantenmechanik der Elektronen in Kristallgittern." *Zeitschrift für Physik* 52, 555–600 (1928). [Original derivation of Bloch's theorem.] `[verify]`
- Kittel, C. *Introduction to Solid State Physics*, 8th ed., Ch. 7–9. Wiley, 2005. [Standard solid-state text; Kronig–Penney, NFE, tight-binding, and band filling.] `[verify]`
- Ashcroft, N. W. & Mermin, N. D. *Solid State Physics*, Ch. 8–10. Holt, Rinehart and Winston, 1976. [Rigorous graduate treatment; NFE model and Bloch's theorem.] `[verify]`
- Griffiths, D. J. & Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed., §5.3. Cambridge University Press, 2018. [Accessible undergraduate treatment of the Kronig–Penney model.] `[verify]`
- Tsymbal, E. Y. "Energy Bands." Lecture notes, University of Nebraska–Lincoln (Rutgers mirror). https://www.physics.rutgers.edu/~eandrei/chengdu/reading/Energy_Bands.pdf `[verify]`
- TU Delft Open Solid State Notes. "Tight binding model." https://solidstate.quantumtinkerer.tudelft.nl/7_tight_binding/ CC BY-SA 4.0. `[verify]`
- Cao, Y. et al. "Unconventional superconductivity in magic-angle graphene superlattices." *Nature* 556, 43–50 (2018). [Magic-angle flat bands and correlated physics.] `[verify]`
- Kane, C. L. & Mele, E. J. "Z₂ topological order and the quantum spin Hall effect." *Physical Review Letters* 95, 146802 (2005). [Founding paper on 2D topological insulators.] `[verify]`
- Hedin, L. "New method for calculating the one-particle Green's function with application to the electron-gas problem." *Physical Review* 139, A796 (1965). [GW approximation; band-gap problem in DFT.] `[verify]`
