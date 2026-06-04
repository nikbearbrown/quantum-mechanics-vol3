# Research Notes: Chapter 10 — Periodic Potentials and the Band Structure of Solids

**Corresponding chapter:** chapters/10-periodic-potentials-and-band-structure.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Derive allowed energy bands and forbidden gaps from a periodic lattice potential. By the end, the student can: (1) state and apply Bloch's theorem; (2) solve the Kronig–Penney model analytically and plot E vs. k dispersion; (3) explain gap opening at zone boundaries via the nearly-free-electron picture; (4) sketch a tight-binding band from atomic orbitals; (5) classify a solid as metal, semiconductor, or insulator from its band filling and gap size; (6) simulate the dispersion numerically in Python (transcendental equation or matrix mechanics).

---

## A. Conceptual foundations

### A1. Bloch's theorem

- **Statement:** If V(r) has the periodicity of a Bravais lattice — V(r + T) = V(r) for all lattice vectors T — then the Hamiltonian eigenstates can be chosen as Bloch functions: ψ_{n,k}(r) = e^{ik·r} u_{n,k}(r), where u_{n,k}(r) is periodic with the same period as the lattice.
- **Proof strategy:** The translation operator T_R commutes with H; therefore H and T_R share eigenstates. The eigenvalue of T_R acting on ψ must be a pure phase (unitarity), giving ψ(r + R) = e^{ik·R} ψ(r). Writing ψ = e^{ikr} u separates the plane-wave "envelope" from the periodic part.
- **Physical content:** Electrons in a crystal are not scattered by every atom — they propagate as modified plane waves. k (the crystal momentum) is a good quantum number. The band index n labels distinct solutions at the same k.
- **Historical note:** Derived by Felix Bloch (1928) using group-theoretic arguments about lattice translation symmetry.
- Sources: [Wikipedia – Bloch's theorem](https://en.wikipedia.org/wiki/Bloch%27s_theorem); [Rutgers University notes, E. Andrei](https://www.physics.rutgers.edu/~eandrei/chengdu/reading/BandMT_02.pdf)

### A2. The Kronig–Penney model

- **Setup:** A 1D array of square-well potentials (depth V₀, well width b) separated by barriers (height 0 by convention with wells at −V₀, barrier width d), period a = b + d. In the delta-function limit (b → 0, V₀ → ∞, V₀ b = const ≡ P·ℏ²/ma), the model becomes analytically tractable.
- **Derivation route:** Solve the Schrödinger equation in each region (oscillatory in wells, exponential or oscillatory in barriers); impose continuity of ψ and dψ/dx at each interface; apply Bloch periodicity condition ψ(x + a) = e^{ika} ψ(x). The four boundary conditions at each interface reduce — via matrix algebra — to a transcendental consistency condition.
- **Key dispersion relation (delta-function limit):**
  ```
  cos(ka) = cos(αa) + (P / αa) sin(αa)
  ```
  where α = sqrt(2mE)/ℏ and P = mV₀ ba/ℏ² is the dimensionless "barrier strength." The right-hand side (RHS) oscillates with amplitude growing away from 1. Allowed bands are where |RHS| ≤ 1 (real k). Forbidden gaps are where |RHS| > 1 (no real k solution).
- **Band gap widths** grow with increasing P (stronger barriers). In the limit P → 0 (no barriers), the free-electron parabola is recovered.
- Simulation target: plot RHS vs. αa; mark allowed/forbidden regions; fold back into the reduced zone to get E(k) in the first Brillouin zone.
- Sources: [IPLTS – Kronig–Penney derivation](https://iplts.com/physics/Kronig-Penney-model.php); [TU Graz interactive](https://lampz.tugraz.at/~hadley/ss1/KronigPenney/KronigPenney.php); [Scientific Reports – tight-binding formulation of KP](https://www.nature.com/articles/s41598-017-17223-2)

### A3. Zone schemes

- **Extended zone scheme:** Each successive band occupies a different Brillouin zone (zone 1 from −π/a to π/a, zone 2 the next two segments, etc.). The dispersion is nearly free-electron parabolas with gaps opened at zone boundaries.
- **Reduced zone scheme:** All bands folded back into the first BZ by subtracting reciprocal lattice vectors G = 2πn/a. This is the standard plot for solid-state band structure.
- **Repeated zone scheme:** The dispersion is plotted periodically over all k — useful for visualizing group velocity continuity.
- Source: [Physics Rutgers – Energy Bands, Tsymbal](https://www.physics.rutgers.edu/~eandrei/chengdu/reading/Energy_Bands.pdf)

### A4. Nearly-free-electron (NFE) picture

- **Starting point:** Free electrons with dispersion E = ℏ²k²/2m. The periodic potential is treated as a small perturbation V(x) = Σ_G V_G e^{iGx}.
- **Gap opening:** Degenerate perturbation theory (two states k and k − G become degenerate at the zone boundary k = G/2 = π/a). The 2×2 matrix is diagonalized: E± = (ℏ²k²/2m) ± |V_G|. **The band gap equals 2|V_G|**, the magnitude of the G-th Fourier component of the periodic potential.
- **Key insight:** Bragg scattering — at zone boundaries k = nπ/a, forward and backward waves interfere constructively, forming standing waves. Symmetric standing wave (density peaked at ion positions) has lower energy; antisymmetric (peaked between ions) has higher energy. That energy difference is the gap.
- Source: [Rutgers/UWO lecture notes](https://physics.uwo.ca/~lgonchar/courses/p9812/Lecture4_EnergyBands.pdf); [Fiveable – Nearly free electron model](https://fiveable.me/solid-state-physics/unit-5/free-electron-model/study-guide/ra5oeUc6GgKN7MLQ)

### A5. Tight-binding picture

- **Starting point:** Isolated atomic orbitals |n⟩ (energy E₀). Electrons in the crystal can "hop" to neighboring sites with hopping integral −t (overlap integral between adjacent orbitals).
- **LCAO ansatz:** |Ψ⟩ = Σ_n φ_n |n⟩. Plane-wave ansatz φ_n = e^{ikna} satisfies Bloch's theorem.
- **Dispersion (1D, nearest-neighbor only):**
  ```
  E(k) = E₀ − 2t cos(ka)
  ```
  Band runs from E₀ − 2t (bottom, k = 0) to E₀ + 2t (top, k = ±π/a). Bandwidth = 4t.
- **Effective mass at band bottom:** m* = ℏ²/(2ta²). Negative effective mass near band top (electrons behave like holes).
- **Insulator criterion:** If each atom contributes 2 electrons and there is one orbital per atom, the band is exactly full. No empty states available → insulator. One electron per atom → half-filled band → metal.
- **Next-nearest-neighbor hopping t':** Adds asymmetry to the dispersion: E(k) = E₀ − 2t cos(ka) − 2t' cos(2ka). Typical ratio t'/t ~ e^{−a/d} where d is the orbital decay length.
- Sources: [TU Delft Open Solid State Notes – Tight Binding](https://solidstate.quantumtinkerer.tudelft.nl/7_tight_binding/); [Wikipedia – Tight binding](https://en.wikipedia.org/wiki/Tight_binding); [Springer – Tight-binding in 1st and 2nd quantization](https://link.springer.com/article/10.1007/s13538-021-01027-x)

### A6. Material classification from band theory

- **Metals:** Fermi level cuts through an allowed band (partially filled). Free electrons at EF → electrical conductivity.
- **Insulators:** Fermi level lies in a large gap (typically > 4 eV). Valence band fully occupied; conduction band empty.
- **Semiconductors:** Same topology as insulators but gap small (0.1–4 eV). Thermally or optically excited carriers can populate the conduction band. Examples: Si (1.12 eV), Ge (0.67 eV), GaAs (1.42 eV).
- **Semimetals:** Bands overlap in energy but the DOS at EF is small.
- Source: [Britannica – Band gap](https://www.britannica.com/science/band-gap); [Engineering LibreTexts – Band Theory of Semiconductors](https://eng.libretexts.org/Bookshelves/Materials_Science/Supplemental_Modules_(Materials_Science)/Semiconductors/Band_Theory_of_Semiconductors)

---

## B. Domain examples and cases

### B1. Worked example: First band gap in the Kronig–Penney model

**Setup:** P = 3π/2 (moderately strong barriers). At the zone boundary αa = π, evaluate RHS:
```
RHS = cos(π) + (P/π) sin(π) = −1 + 0 = −1  [allowed — barely]
```
At αa slightly above π, sin(αa) is negative while cos(αa) approaches −1; the RHS dips below −1, opening a gap. The first gap sits at the energy corresponding to αa ∈ [π, π + δ] where |RHS| > 1.

**Numerical procedure for simulation:**
1. Choose P (e.g., P = 3π/2).
2. Sweep αa from 0 to 6π.
3. Compute f(αa) = cos(αa) + (P/αa) sin(αa).
4. Find intervals where |f| ≤ 1 → these are allowed bands.
5. For each allowed αa, compute E = (ℏαa)²/(2ma²) and k = arccos(f)/a to produce E(k).
6. Fold into reduced zone scheme.

Source: [Physiquate – Kronig-Penney model](https://physiquate.com/kronig-penney-model/); [ResearchGate – Numerical Python solutions](https://www.researchgate.net/publication/336339061_Solucion_Numerica_por_Python_de_la_Relacion_de_Dispersion_para_un_Cristal_Unidimensional_con_el_Modelo_Kronig_Penney)

### B2. Tight-binding band for a simple chain

**Setup:** E₀ = 0, t = 1 eV, a = 3 Å.
- Band runs from −2 eV to +2 eV (bandwidth = 4t = 4 eV).
- Effective mass at band bottom: m* = ℏ²/(2ta²) = (1.055×10⁻³⁴)² / (2 × 1.6×10⁻¹⁹ × (3×10⁻¹⁰)²) ≈ 0.38 mₑ (reasonable for a covalent solid).
- At band top, m* → −∞ then jumps to m* = −0.38 mₑ (hole-like).

### B3. Gap opening in silicon

Silicon has an indirect band gap of 1.12 eV. The valence-band maximum is at k = 0 (Γ point) and the conduction-band minimum is near the X point. The NFE picture predicts gaps at zone boundaries from V_G Fourier components; tight-binding gives a picture of sp³ hybridized orbitals forming bonding (valence) and antibonding (conduction) bands. Qualitatively, the gap size ≈ 2|V_{111}| ≈ 1 eV, matching observation to order of magnitude.

---

## C. Connections and dependencies

- **Prerequisites from this volume:** Ch. 1–2 (perturbation theory is used in the NFE derivation; degenerate PT diagonalizes the 2×2 zone-boundary problem). Ch. 4 (WKB tunneling — tight-binding hopping integral is a close cousin; tunneling through atomic barriers sets |t|). Ch. 8–9 (scattering language: Bragg reflection = coherent backscattering is periodic potential analog of scattering).
- **Connects forward to:** Ch. 11 (capstone: semiconductor band gap or STM system draws directly on band structure). The quantum dot confinement model (Ch. 11 candidate) uses free-electron approximation inside the dot — same physics as the bottom of the first KP band.
- **Vol. 1–2 prerequisites:** Particle in a box (energy quantization), Fourier series (decomposition of periodic V), matrix eigenvalue problems (NFE 2×2 determinant).
- **External connections:** Solid-state physics (Kittel, Ashcroft & Mermin); density functional theory (ab initio band structure); semiconductor device physics (MOSFET, LED, solar cell).

---

## D. Current state of the field

- **Density functional theory (DFT):** Modern band structure calculations go far beyond KP/tight-binding. DFT (Kohn-Sham equations, exchange-correlation functionals) accurately predicts band gaps for many materials, though the "band gap problem" (LDA underestimates gaps) persists. Hybrid functionals (HSE06) and GW approximation improve accuracy.
- **Topological materials (2020s active area):** Band topology — whether bands have non-trivial Berry phase — determines surface states (topological insulators, Weyl semimetals). The same Bloch theorem framework underlies this; the "twisting" of Bloch eigenstates around the Brillouin zone is quantified by topological invariants (Chern number, Z₂).
- **Moiré superlattices and flat bands:** Twisted bilayer graphene (at the "magic angle" ~1.1°) creates a moiré periodic potential with extremely flat bands (near-zero bandwidth → strong correlations). Discovery of superconductivity (2018, Cao et al., Nature) sparked intense interest. KP-style models with moiré periodicity are active research.
- **Machine-learned interatomic potentials:** ML models trained on DFT data can produce band structures at reduced cost — still grounded in Bloch's theorem for prediction of electronic properties.
- Sources: [arXiv – Non-uniform BZ sampling for perturbation theory](https://arxiv.org/pdf/1610.06641); [arXiv – Topological tight-binding models](https://arxiv.org/pdf/2305.18257); [arXiv – Sinusoidal potential band structure](https://arxiv.org/pdf/2003.06647)

---

## E. Teaching considerations

### E1. The key conceptual hurdle
Students often expect that any potential barrier scatters electrons and kills propagation. The counterintuitive insight: in a perfectly periodic potential there is *zero* net scattering — electrons propagate freely as Bloch waves. Gaps arise from *constructive interference* at zone boundaries, not from random scattering. Make this physical before writing down Bloch's theorem.

### E2. Zone-scheme confusion
Students conflate the extended, reduced, and repeated zone schemes. A worked animation or interactive plot is essential. The reduced zone scheme is canonical; the extended zone reveals the free-electron parentage.

### E3. Simulation as the worked example
The Kronig–Penney model has an exact analytic dispersion but must be solved numerically (transcendental equation). This is a natural first simulation task:
- `scipy.optimize.brentq` to find E(k) numerically for each k in [-π/a, π/a].
- Or: sweep αa, compute RHS, color regions by allowed/forbidden, fold back.
- Reference Python implementation: [ResearchGate numerical Python KP](https://www.researchgate.net/publication/336339061_Solucion_Numerica_por_Python_de_la_Relacion_de_Dispersion_para_un_Cristal_Unidimensional_con_el_Modelo_Kronig_Penney); [ResearchGate – KP extended to arbitrary potentials via matrix mechanics](https://www.researchgate.net/publication/268227429_The_Kronig-Penney_model_extended_to_arbitrary_potentials_via_numerical_matrix_mechanics)

### E4. Connecting the two pictures
The NFE and tight-binding pictures are complementary: NFE works near the free-electron limit (weak V); TB works near the atomic limit (strong binding). Real materials (Si, GaAs) sit in between. A qualitative "phase diagram" in barrier-strength parameter P (KP) interpolates the two limits nicely.

### E5. Assessment ideas
1. **Derive:** Starting from the delta-function KP potential, derive the dispersion relation and sketch the first two bands.
2. **Compute:** Write Python code to plot the KP dispersion for P = 3π/2 in the reduced zone scheme. Identify the first gap width.
3. **Classify:** Given a material's band structure plot, identify whether it is a metal, semiconductor, or insulator, locate the Fermi level, and estimate the band gap.
4. **Extend:** How does the bandwidth in the TB model change if t doubles (bond stronger)? If the lattice constant a doubles? Interpret physically.

---

## F. Library files relevant to this chapter

- `/Users/bear/Documents/CoWork/bear-textbooks/books/quantum-mechanics-vol3/pantry/_lib_qmsri-qm-townsend-notes.md` — grepped for Bloch/Kronig/periodic potential; no relevant entries found. Townsend's QM text (used in QM-SRI) does not cover solid-state band theory.
- No Shankar-condensed-matter excerpts found in the physics-quantum-mechanics-sri pantry matching band structure keywords; that Shankar file (OCR text) appears to be the QM textbook, not a condensed matter text.
- The TU Delft "Open Solid State Notes" (CC-BY-SA 4.0) at https://solidstate.quantumtinkerer.tudelft.nl/7_tight_binding/ are freely available and pedagogically excellent — consider extracting and saving as a pantry file.
- Kittel, *Introduction to Solid State Physics* (Ch. 7–9) — canonical treatment; not in the local library but standard reference.
- Ashcroft & Mermin, *Solid State Physics* (Ch. 8–10) — rigorous treatment; not in local library.

---

## G. Gaps and flags

1. **3D Brillouin zones not covered:** The 1D treatment suffices for the chapter goal but students will encounter 3D BZ diagrams in all real materials. At minimum, a brief descriptive note on the FCC/BCC reciprocal lattice and the first BZ shapes (truncated octahedron, rhombic dodecahedron) should appear in a sidebar.
2. **Spin–orbit coupling absent:** For heavy elements (Bi, Pb, topological materials) spin–orbit coupling is crucial and breaks band degeneracies. Flag as "beyond this chapter."
3. **Many-body effects:** The independent-electron approximation (underlying Bloch's theorem and the entire chapter) ignores electron–electron correlations. Mott insulators — materials predicted to be metals by band theory but are insulators due to strong correlations — are a known failure. Note this limitation in the text.
4. **Simulation language choice:** The chapter targets Python simulations. The transcendental KP equation is solved easily with `scipy`; a tight-binding band requires only `numpy`. Both are appropriate for the "+1 simulation layer" architecture of the book.
5. **The delta-function KP model is an approximation of an approximation:** The author should state clearly that real crystal potentials are not square wells, and that DFT replaces the empirical potential entirely. KP is a pedagogical tool, not a materials-design tool.
6. **Local library gap:** No solid-state physics library files exist in the pantry; this chapter is making a discipline jump (from atomic QM to condensed matter). The chapter writer may want to pull in a brief introduction to crystal structure (Bravais lattice, lattice constant, reciprocal lattice) as a two-page orientation, or reference Vol. 1/2 chapters if any cover this.

---

*Sources consulted:*
- [Wikipedia – Bloch's theorem](https://en.wikipedia.org/wiki/Bloch%27s_theorem)
- [Rutgers University – Band structure notes (Tsymbal)](https://www.physics.rutgers.edu/~eandrei/chengdu/reading/Energy_Bands.pdf)
- [TU Delft Open Solid State Notes – Tight Binding](https://solidstate.quantumtinkerer.tudelft.nl/7_tight_binding/)
- [IPLTS – Kronig–Penney Model](https://iplts.com/physics/Kronig-Penney-model.php)
- [TU Graz – Kronig-Penney interactive](https://lampz.tugraz.at/~hadley/ss1/KronigPenney/KronigPenney.php)
- [Scientific Reports – Tight-binding formulation of KP](https://www.nature.com/articles/s41598-017-17223-2)
- [UWO lecture notes – Nearly Free Electron Model](https://physics.uwo.ca/~lgonchar/courses/p9812/Lecture4_EnergyBands.pdf)
- [arXiv – Sinusoidal 1D potential band structure](https://arxiv.org/pdf/2003.06647)
- [arXiv – KP extended to arbitrary potentials via matrix mechanics](https://arxiv.org/pdf/1411.3607)
- [Britannica – Band gap](https://www.britannica.com/science/band-gap)
- [Engineering LibreTexts – Band Theory of Semiconductors](https://eng.libretexts.org/Bookshelves/Materials_Science/Supplemental_Modules_(Materials_Science)/Semiconductors/Band_Theory_of_Semiconductors)
- [ResearchGate – Numerical Python KP solutions](https://www.researchgate.net/publication/336339061_Solucion_Numerica_por_Python_de_la_Relacion_de_Dispersion_para_un_Cristal_Unidimensional_con_el_Modelo_Kronig_Penney)
