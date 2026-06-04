# Research Notes: Chapter 11 — Capstone: Modeling a Real Quantum System

**Corresponding chapter:** chapters/12-capstone-modeling-a-real-quantum-system.md (not yet written; file on disk is chapters/12-...)
**Generated:** 2026-06-03

> **Note on file numbering:** The outline numbers this chapter "11" but the chapters/ directory already has a file `12-capstone-modeling-a-real-quantum-system.md`. The pantry file is named `11-...` per the task spec. The chapter author should reconcile numbering before drafting.

---

## Chapter summary (capability built)

The student selects a real quantum system, applies one or more of Vol. 3's approximation methods (perturbation theory, WKB, variational, scattering, or band structure), produces a quantitative prediction, and validates it against measured data. The chapter scaffolds this process: motivates candidate systems, shows a worked model-and-validate loop, teaches the "error budget" and "where the approximation breaks" analysis, and supplies a project rubric. Outcome: the student can *defend* a model, not just execute formulas.

---

## A. Conceptual foundations

### A1. What it means to "model and defend" a quantum system

A complete quantum model involves:
1. **System identification:** What are the relevant degrees of freedom? What can be held fixed?
2. **Approximation selection:** Which method (PT, WKB, variational, Born, band structure) is appropriate, and why?
3. **Calculation:** Derive the key observable (energy level, transition rate, tunneling current, gap).
4. **Validation:** Compare to a known experimental datum. Compute percent error.
5. **Breakdown analysis:** State where the approximation fails and what physics is missing. Estimate the next correction.

This is the scientific method at the quantum level. The capstone trains students to think like physicists, not calculation-executors.

### A2. Error budget thinking

For each approximation method, there is a small parameter controlling its accuracy:
- **Perturbation theory:** λ = |⟨n|H'|m⟩| / |E_n − E_m| ≪ 1. Breakdown: near-degenerate states, large perturbation.
- **WKB:** ℏ|dλ/dx| ≪ λ² (de Broglie wavelength varies slowly). Breakdown: near turning points, sharp potentials.
- **Variational:** Upper bound on ground state only; excited states require orthogonality constraints.
- **Born approximation:** |V| ≪ E (weak scattering). Breakdown: strong potentials, resonances.
- **Tight-binding/KP:** Valid near atomic limit; breakdown for wide bands, strong correlations.

The chapter should train students to explicitly state which condition they're relying on and estimate its magnitude for the chosen system.

### A3. What "validate against real data" means

Real experimental data for each candidate system:
- **STM tunneling current:** Measured as function of tip-sample distance. Typical values: 1 nA at d ≈ 5 Å for metal surfaces. Current drops ~10× per Å.
- **Quantum dot (CdSe) level spacing:** First exciton absorption peaks measurable by UV-Vis spectroscopy. For 3 nm CdSe: E_gap ≈ 2.4 eV (bulk CdSe gap 1.74 eV, confinement adds ~0.7 eV). For 4.5 nm: ~2.18 eV.
- **Ammonia inversion (maser):** E₁ − E₀ ≈ 0.79 cm⁻¹ (microwave, 23.87 GHz = 24 GHz). Theoretical models with double-well potential agree to within ~20% at perturbative level, <5% with numerical eigenstates.
- **NMR spin flip (¹H):** Larmor frequency ν₀ = γ B₀ / 2π = 42.577 MHz/T × B₀. At 9.4 T (400 MHz NMR): ν₀ = 400 MHz. Rabi oscillation frequency: ν_R = γ B₁ / 2π, controllable by rf field strength B₁.

---

## B. Candidate systems and Vol-3 method mapping

### B1. STM tunneling current (WKB)

**System:** A metallic STM tip scans over a flat metal surface. A bias voltage V is applied (typically 0.1–3 V). The vacuum gap acts as a rectangular potential barrier of height φ (effective work function, ~4–5 eV for W or Pt-Ir tips and Au or Cu surfaces) and width d (tip-sample distance, 2–8 Å).

**Vol-3 method:** WKB barrier penetration (Ch. 4).

**Model:**
The WKB transmission coefficient through a square barrier of height U₀ and width d is:
```
T ≈ exp(−2κd),   κ = sqrt(2m(U₀ − E)) / ℏ
```
For the STM vacuum barrier with E at the Fermi level, U₀ − E ≈ φ (the work function). The tunneling current is proportional to T times the density of states at the Fermi level:
```
I ∝ V · exp(−2κd),   κ = sqrt(2mφ) / ℏ ≈ 0.512 Å⁻¹ · sqrt(φ [eV])
```
For φ = 4 eV: κ ≈ 1.02 Å⁻¹.

**Worked numerical example:**
- φ = 4 eV (work function of W tip on Au surface, approximately).
- d₁ = 5 Å: 2κd₁ = 2 × 1.02 × 5 = 10.2. T₁ ∝ e^{−10.2} ≈ 3.7 × 10⁻⁵.
- d₂ = 6 Å: 2κd₂ = 12.24. T₂ ∝ e^{−12.24} ≈ 4.9 × 10⁻⁶.
- Ratio T₁/T₂ = e^{2.04} ≈ 7.7. So increasing gap by 1 Å reduces current ~8-fold. 
- Experimentally measured: current drops ~one order of magnitude per Å. WKB gives 7–10× per Å depending on φ. Agreement is excellent.
- **Where the model breaks:** (a) Ignores local density of states structure (Tersoff–Hamann correction uses LDOS at tip position, not just T × V). (b) Assumes 1D rectangular barrier; real barrier has image-charge rounding near the electrodes. (c) Ignores tip geometry (only the outermost atom dominates, which is why WKB works so well — it is effectively 1D for the apex atom).

**Validate against:** STM exponential I(d) curves. Standard experiment: withdraw the tip by ~3 Å and observe ~1000× reduction in current. Sources: [Chemistry LibreTexts – STM](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Microscopy/Scanning_Probe_Microscopy/03_Basic_Theory/01_Scanning_Tunneling_Microscopy_(STM)); [Beilstein J. Nano – apparent tunneling barrier height](https://www.beilstein-journals.org/bjnano/articles/9/283); [NTMDT – current-distance characteristic](https://www.ntmdt-si.com/resources/spm-theory/theoretical-background-of-spm/1-scanning-tunnel-microscopy-(stm)/13-observed-physical-quantities-in-stm/132-current-distance-characteristic)

### B2. Quantum dot as a 3D particle-in-a-box (perturbation theory / exact)

**System:** Spherical CdSe nanocrystal (quantum dot) of radius R ≈ 2–5 nm. Electrons and holes confined inside the dot. Bulk band gap of CdSe: E_gap = 1.74 eV.

**Vol-3 method:** The 3D spherical infinite square well (not strictly from this volume, but connects to variational or first-order PT). The simplest model: treat the electron (or the exciton) as a particle in a 3D spherical box.

**Model:**
Energy levels of a particle in a 3D spherical infinite square well:
```
E_{n,l} = (ℏ² / 2m* R²) · z_{n,l}²
```
where z_{n,l} is the n-th zero of the l-th spherical Bessel function. For the lowest state (1s, l = 0, n = 1): z_{1,0} = π. So:
```
E_{1s} = ℏ² π² / (2 m* R²)
```
The optical band gap of the quantum dot:
```
E_dot = E_bulk_gap + E_{1s,electron} + E_{1s,hole} − (Coulomb correction)
```
Using m*_e ≈ 0.13 mₑ and m*_h ≈ 0.45 mₑ for CdSe, and R = 1.5 nm (3 nm dot):
```
E_{1s,e} = (1.055×10⁻³⁴)² π² / (2 × 0.13 × 9.11×10⁻³¹ × (1.5×10⁻⁹)²)
         ≈ 0.68 eV
E_{1s,h} ≈ 0.68 × (0.13/0.45) ≈ 0.20 eV
E_dot ≈ 1.74 + 0.68 + 0.20 − 0.10 (Coulomb) ≈ 2.52 eV
```
**Experimental value:** For 3 nm CdSe QDs, the first excitonic absorption peak is at approximately 2.44 eV (510 nm). Model gives 2.52 eV — error ~3%. Excellent for this crude model.

**Where the model breaks:** (a) Electron and hole are not independent — exciton binding reduces energy (Coulomb term, ~0.1–0.3 eV). (b) Effective mass approximation fails for very small dots (R < 1.5 nm) where k becomes large. (c) Real QDs are not perfectly spherical; ligand effects modify the surface potential. (d) Size dispersion in real samples broadens the absorption peak.

**Validate against:** CdSe QD UV-Vis spectra. Well-characterized by Bawendi, Alivisatos groups (1990s–present). Sources: [Springer – Size-dependent energy spacing CdSe QDs](https://link.springer.com/article/10.1007/s13204-021-02310-8); [arXiv – confinement energy QDs](https://arxiv.org/pdf/1212.2318); [ResearchGate – CdSe QD characteristics and properties](https://www.researchgate.net/publication/281808382_CHARACTERISTICS_AND_PROPERTIES_OF_CDSE_QUANTUM_DOTS); [PMC – influence of size and shape on CdSe optical properties](https://pmc.ncbi.nlm.nih.gov/articles/PMC7466547/)

### B3. Ammonia maser / two-level inversion (degenerate perturbation theory / double-well)

**System:** NH₃ molecule. The nitrogen atom sits in a double-well potential (can be on either side of the H₃ plane). The two classical "positions" correspond to degenerate configurations. Quantum tunneling mixes them, creating symmetric and antisymmetric eigenstates split by 2A (where A is the tunneling matrix element).

**Vol-3 method:** Two-level system / degenerate perturbation theory (Ch. 2); time-dependent PT for the maser transition (Ch. 5).

**Model:**
Hamiltonian in the |L⟩, |R⟩ basis:
```
H = [ E₀   −A  ]
    [ −A    E₀  ]
```
Eigenstates: |+⟩ = (|L⟩ + |R⟩)/√2 (E = E₀ − A), |−⟩ = (|L⟩ − |R⟩)/√2 (E = E₀ + A).
Energy splitting: ΔE = 2A.

The full numerical model (Rioux, Chemistry LibreTexts) uses a harmonic + Gaussian barrier:
```
V(x) = (1/2)kx² + b·exp(−cx²)
```
Parameters (atomic units): k = 0.07598, b = 0.05684, c = 1.36696, μ = 4668.
First four eigenvalues (hartree): E₀ = 0.04996046, E₁ = 0.04996492, E₂ = 0.05418694, E₃ = 0.05435966.

**Predicted maser transition:** E₁ → E₀. ΔE = (E₁ − E₀) × 2.1947×10⁵ cm⁻¹/hartree = 0.98 cm⁻¹.
**Experimental value:** 0.79 cm⁻¹ (= 23.87 GHz). Error ~24% for this simple potential model.
**Selection rule:** (−) → (+) or (+) → (−) transitions allowed (oscillating dipole); (+) → (+) or (−) → (−) forbidden.
**The maser mechanism:** |−⟩ states sorted from |+⟩ states by an inhomogeneous electric field (different dipole moments). |−⟩ molecules fed into a resonant microwave cavity at 24 GHz, inducing stimulated emission |−⟩ → |+⟩. This was the first maser (Gordon, Zeiger, Townes, 1954).

**Where the model breaks:** Gaussian barrier shape is empirical. A more accurate ab initio potential (Swallen & Ibers, J. Chem. Phys. 1962) improves agreement. The double Rosen–Morse potential gives 24 GHz exactly (arXiv:2512.16168v2).

**Validate against:** Microwave spectroscopy of NH₃. Well-tabulated in NIST databases. The 23.87 GHz line is one of the most precisely measured molecular transitions.
Sources: [Chemistry LibreTexts – Ammonia inversion and maser (Rioux)](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Quantum_Tutorials_(Rioux)/04%3A_Spectroscopy/4.04%3A_The_Ammonia_Inversion_and_the_Maser); [arXiv – Tunneling in double-well potentials (Nelson mechanics)](https://arxiv.org/html/2512.16168v2); [PMC – Tunneling quantum dynamics in ammonia](https://pmc.ncbi.nlm.nih.gov/articles/PMC8348077/); [etneil.github.io – graduate QM ammonia maser capstone](https://etneil.github.io/grad_qm_lec_notes/ex_ammonia.html)

### B4. NMR qubit (time-dependent PT / Rabi oscillation)

**System:** A spin-½ nucleus (e.g., ¹H) in a static magnetic field B₀ (e.g., 9.4 T). An oscillating rf field B₁ cos(ωt) at or near the Larmor frequency drives spin flips.

**Vol-3 method:** Time-dependent perturbation theory (Ch. 5) and the rotating-wave approximation; Rabi oscillations.

**Model:**
Two-level Hamiltonian (spin basis |↑⟩, |↓⟩):
```
H = −γℏ B₀ Sz − γℏ B₁ cos(ωt) Sx
```
In the rotating frame (rotating-wave approximation), the time-independent effective Hamiltonian gives Rabi oscillations with frequency:
```
Ω_R = γ B₁ / 2
```
Population inversion (from |↑⟩ to |↓⟩) achieved after time t = π/Ω_R (π-pulse).

**Validation:** For ¹H in a 9.4 T field: Larmor frequency ν₀ = 42.577 × 9.4 = 400 MHz. A typical B₁ ≈ 0.01 T gives Ω_R = (2.675×10⁸ rad/s/T × 0.01 T)/2 ≈ 1.34 MHz → π-pulse duration ≈ 2.4 μs. Measured NMR π-pulse durations: typically 1–25 μs, consistent with B₁ values in the range 0.001–0.01 T. Agreement is essentially exact (this is a solved two-level system with no approximations beyond RWA, which is excellent for on-resonance driving).

**Where the model breaks:** (a) Transverse relaxation (T₂) causes decoherence — not included in the basic model. (b) Chemical shift and J-coupling make multi-spin systems more complex. (c) At very high B₁, the RWA fails (counter-rotating term becomes significant). (d) Many-body nuclear spin interactions (dipolar broadening in solids).

**Validate against:** Standard NMR textbook data; any 400 MHz NMR instrument. Rabi oscillations in NMR are a textbook experiment.
Sources: [Wikipedia – Rabi cycle](https://en.wikipedia.org/wiki/Rabi_cycle); [arXiv – Low frequency Rabi spectroscopy dissipative TLS](https://arxiv.org/pdf/cond-mat/0609144)

---

## C. Connections and dependencies

- **STM system** calls on Ch. 4 (WKB) — the most direct and cleanest connection; WKB gives closed-form I(d) dependence. The exponential is the pedagogical payoff.
- **Quantum dot** calls on 3D particle-in-a-box (Vol. 1/2 material) plus the effective-mass approximation; the confinement energy calculation is close to first-order perturbation theory (treating confinement as perturbation on bulk states).
- **Ammonia maser** calls on Ch. 2 (degenerate PT, two-level Hamiltonian) and Ch. 5 (time-dependent PT for the maser mechanism). Also connects to Ch. 6 (Fermi's Golden Rule for stimulated emission).
- **NMR qubit** calls on Ch. 5 (time-dependent PT, Rabi flopping) and Ch. 9 (atoms in magnetic fields, Zeeman splitting). Also the cleanest "quantum computing" hook — NMR was the first experimental platform for quantum algorithms (Chuang et al., 1998).
- **Band structure system** (e.g., Si or GaAs band gap) calls on Ch. 10. A student could estimate a semiconductor band gap from the KP model and compare to measured gap.
- **Ch. 3 (variational)** is underrepresented in the candidate systems above. A fifth candidate: model the helium ground state energy using variational methods and compare to spectroscopic data (E = −79.0 eV measured, variational with shielded nuclear charge gives −77.5 eV). But this may already appear in Vol. 2; verify before adding.

---

## D. Current state of the field

### D1. STM
STM pioneered by Binnig and Rohrer (Nobel Prize 1986). Current frontier: qPlus AFM (picoNewton forces at sub-Å resolution), tip-enhanced Raman spectroscopy (TERS), spin-polarized STM for magnetic imaging. The WKB model remains the standard pedagogical entry point; Tersoff–Hamann theory (1983, 1985) is the workhorse for quantitative analysis.

### D2. Quantum dots
CdSe QDs commercialized in QLED displays (Samsung, 2022 onwards). Core-shell structures (CdSe/ZnS) reduce surface trap states. "Heavy metal free" alternatives (InP, perovskite QDs) are active research due to RoHS regulations. Quantum dot solar cells and single-photon emitters (quantum information) are frontier applications. The 3D box model is still the standard first approximation taught in courses.

### D3. Ammonia maser
First maser (Gordon, Zeiger, Townes, 1954). The ammonia maser was the precursor to the laser (Maiman, 1960). Modern atomic clocks (Cs fountain, optical lattice clocks) extend this physics. The 23.87 GHz NH₃ line is used in radio astronomy to map molecular clouds in the ISM.

### D4. NMR / MRI
NMR is one of the most powerful analytical techniques in chemistry and medicine. MRI (magnetic resonance imaging) uses the same physics. Quantum computing implementations: NMR quantum computing (1990s–2000s) demonstrated first quantum algorithms (Shor's algorithm on 7 qubits, Vandersypen et al., Nature 2001). Superseded by superconducting qubits and ion traps for scalability, but NMR remains a precision testbed for quantum control.

---

## E. Teaching considerations

### E1. The "choose your own system" challenge
Students find open-ended projects liberating but also anxiety-inducing. The chapter should provide:
- A short-list of 4–5 pre-validated systems (the candidates above) with clear data sources.
- Permission to propose a different system, but with a brief "feasibility check" rubric before investing time.
- Scaffolded project phases: system selection (week 1), model derivation (week 2), numerical calculation (week 3), validation + breakdown analysis (week 4).

### E2. Recommended worked example for the chapter
**STM + WKB** is the strongest choice because:
- It uses Ch. 4 directly — the WKB formula is applied almost verbatim.
- The result is intuitive (exponential decay with distance).
- Experimental data is easy to find and interpret (I vs. d curve).
- The "where it breaks" analysis is concrete (LDOS, image charge, tip geometry).
- Numbers come out right to within a factor of 2 with minimal calculation.

The quantum dot is the second choice for a different calculation flavor (bound states vs. tunneling current).

### E3. Project rubric (draft)

| Criterion | Exemplary (4) | Proficient (3) | Developing (2) | Beginning (1) |
|---|---|---|---|---|
| **System identification** | Clearly identified, DOF justified, irrelevant physics excluded | Identified correctly, some hand-waving | System chosen but DOF not fully justified | System vague or inappropriate |
| **Method selection** | Correct method chosen, limitation acknowledged, small parameter estimated | Correct method, limitation noted qualitatively | Correct method, no limitation analysis | Wrong method or method not stated |
| **Derivation** | Full derivation from first principles, no steps skipped | Correct derivation with minor gaps | Derivation partially complete or contains errors | Major errors or derivation absent |
| **Quantitative prediction** | Numbers with units, clear assumptions stated | Numbers correct, some assumptions implicit | Numbers present but errors in assumptions | No quantitative result |
| **Validation** | Compared to real data with citation, percent error computed, discrepancy explained | Compared to data, error noted | Data cited but no error analysis | No comparison to data |
| **Breakdown analysis** | Next-order correction identified, magnitude estimated | Limitation stated qualitatively | Limitation mentioned but not analyzed | No breakdown analysis |

### E4. Common student errors
1. Confusing the approximation with the exact result: students sometimes forget to check whether the small-parameter condition is satisfied.
2. Forgetting to convert units (eV vs. joules; Å vs. meters).
3. Treating experimental data as exact (all measurements have uncertainty — quote it).
4. Stopping at the formula without plugging in numbers.
5. Choosing a system outside the reach of the volume's methods (e.g., strongly correlated electron systems — these require many-body QM).

### E5. Simulation target for the capstone
The simulation component should be the calculation of the key observable as a function of a tunable parameter:
- **STM:** Plot I vs. d for d ∈ [2, 10] Å for three values of φ (3, 4, 5 eV). Show that all curves are linear on a log-scale (verify WKB).
- **QD:** Plot E_dot(R) vs. R for R ∈ [1, 5] nm; overlay with published experimental CdSe size-gap data.
- **Ammonia:** Plot the double-well eigenstates numerically (grid method); vary barrier height b and show how the tunneling splitting 2A changes.
- **NMR:** Simulate Rabi oscillations: plot ⟨Sz⟩(t) for on-resonance and off-resonance driving.

---

## F. Library files relevant to this chapter

- `/pantry/_lib_qmsri-09-time-independent-perturbation-theory.md` — PT foundations; directly relevant to ammonia maser and QD perturbation model.
- `/pantry/_lib_qmsri-10-time-dependent-perturbation-theory-and-transitions.md` — Rabi oscillations, time-dependent PT; directly relevant to NMR and maser chapters.
- `/pantry/_lib_qmsri-11-the-wkb-approximation-and-tunneling.md` — WKB foundation; directly relevant to STM worked example.
- `chapters/04-the-wkb-approximation-and-tunneling.md` — draft placeholder (no content yet). The capstone STM example assumes this chapter delivers the WKB formula; verify when Ch. 4 is drafted.
- `chapters/05-the-wkb-approximation-and-tunneling.md` — the actual chapter file (as per on-disk path `05-the-wkb-approximation-and-tunneling.md`). Cross-reference.
- No local files on STM, quantum dots, or ammonia maser — all data sourced from web.

---

## G. Gaps and flags

1. **Chapter numbering conflict:** The `chapters/` directory has the capstone as `12-capstone-...md` but the outline calls it Chapter 11 (final chapter). The pantry file follows the outline. The chapter author should reconcile: either the "Atoms in Fields" chapter (currently on disk as `10-atoms-in-fields.md`) and "Periodic Potentials" (currently `11-periodic-potentials-and-band-structure.md`) shift numbering, or the outline should be updated to show 12 chapters.

2. **Rubric granularity:** The draft rubric above is adapted from engineering capstone rubric literature (Emerald/ResearchGate). It has not been validated by physics instructors. The chapter author should pilot-test with students and revise.

3. **Variational method underrepresented:** No candidate system was found that exclusively and cleanly exercises Ch. 3 (variational principle). Adding a helium atom ground-state calculation (well-known result: variational gives −77.5 eV vs. −79.0 eV exact) or a hydrogen molecule variational bond length estimate would round out the method coverage.

4. **Born approximation absent:** Similarly, Ch. 8–9 (scattering / Born approximation) is not represented in the candidate systems. A possible addition: estimate the Rutherford scattering cross-section (Coulomb potential, Born approximation gives the exact classical result) and compare to measured alpha-particle scattering. Or: neutron scattering from a Yukawa potential.

5. **Data access for students:** The chapter author should provide specific, student-accessible data sources. For STM: published I(d) curves in textbooks (Bonnell, SPM textbook). For CdSe QDs: Bawendi group paper (JACS 1993) or a teaching resource from Nanohub. For NMR: any standard NMR textbook (Levitt, "Spin Dynamics"). These should be cited explicitly in the chapter.

6. **Two-system project option:** Consider allowing advanced students to model two systems and compare which approximation method works better. This "cross-system" comparison reinforces the idea that approximation methods are tools with domains of validity, not universal algorithms.

7. **The "defend" component needs a structured oral or written format:** The capstone should specify whether "defense" means a written report, a short oral presentation, or a peer-review format. This is a pedagogical decision outside the physics content — the chapter author should specify the expected deliverable format.

8. **No local source for STM Tersoff–Hamann theory:** The quantitative theory of STM tunneling current beyond WKB (Tersoff & Hamann, Phys. Rev. B 31, 805, 1985) is not in the local library. The chapter should cite this and note it as "beyond the WKB model"; students who want the full derivation are directed to the original paper.

---

*Sources consulted:*
- [Chemistry LibreTexts – Ammonia inversion and maser (Rioux)](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Quantum_Tutorials_(Rioux)/04%3A_Spectroscopy/4.04%3A_The_Ammonia_Inversion_and_the_Maser)
- [etneil.github.io – Graduate QM ammonia maser capstone notes](https://etneil.github.io/grad_qm_lec_notes/ex_ammonia.html)
- [arXiv – Tunneling in double-well potentials / Nelson mechanics](https://arxiv.org/html/2512.16168v2)
- [PMC – Tunneling quantum dynamics in ammonia](https://pmc.ncbi.nlm.nih.gov/articles/PMC8348077/)
- [Chemistry LibreTexts – STM basic theory (Bullen & Wilson)](https://chem.libretexts.org/Bookshelves/Analytical_Chemistry/Supplemental_Modules_(Analytical_Chemistry)/Microscopy/Scanning_Probe_Microscopy/03_Basic_Theory/01_Scanning_Tunneling_Microscopy_(STM))
- [NTMDT – Current-distance characteristic in STM](https://www.ntmdt-si.com/resources/spm-theory/theoretical-background-of-spm/1-scanning-tunnel-microscopy-(stm)/13-observed-physical-quantities-in-stm/132-current-distance-characteristic)
- [Beilstein J. Nano – Apparent tunneling barrier height and local work function](https://www.beilstein-journals.org/bjnano/articles/9/283)
- [Wikipedia – Scanning tunneling microscope](https://en.wikipedia.org/wiki/Scanning_tunneling_microscope)
- [Springer – Size-dependent energy spacing CdSe QDs](https://link.springer.com/article/10.1007/s13204-021-02310-8)
- [arXiv – Confinement energy of quantum dots](https://arxiv.org/pdf/1212.2318)
- [PMC – Influence of size and shape on CdSe optical properties](https://pmc.ncbi.nlm.nih.gov/articles/PMC7466547/)
- [Wikipedia – Quantum dot](https://en.wikipedia.org/wiki/Quantum_dot)
- [Wikipedia – Rabi cycle](https://en.wikipedia.org/wiki/Rabi_cycle)
- [arXiv – Rabi oscillations of a qubit coupled to a two-level system](https://arxiv.org/pdf/cond-mat/0501455)
- [Emerald – Four-quadrant approach for capstone pedagogy](https://www.emerald.com/jrit/article/doi/10.1108/JRIT-11-2024-0277/1254118)
- [arXiv – Development of rubrics for capstone project courses](https://arxiv.org/pdf/2011.11035)
- [arXiv – Characterization of upper-level undergraduate QM courses in the US](https://arxiv.org/pdf/2507.10513)
