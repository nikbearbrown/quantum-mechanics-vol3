# Research Notes: Chapter 09 — Atoms in Fields
**Corresponding chapter:** chapters/09-atoms-in-fields.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to predict how atomic energy levels split when an atom is placed in an external electric or magnetic field: compute Zeeman splittings using the Landé g-factor in the weak-field (anomalous) regime, identify the Paschen-Back limit at strong fields, reproduce the Stark-effect selection rules and linear/quadratic splitting in hydrogen, and describe the physics of magnetic resonance (Rabi oscillations, rotating-frame picture, NMR/ESR). The chapter applies the perturbation theory machinery of Ch 9 (perturbation theory, which this volume develops before this chapter) to physically observable, experimentally testable systems.

---

## A. Conceptual foundations

### A1. The Zeeman effect

**Physical setup**: atom in an external uniform magnetic field B along ẑ. The perturbation is the interaction of the atom's magnetic moment with B.

For a hydrogen-like atom the orbital magnetic moment is μ_L = −eL/2m_e and the spin magnetic moment is μ_S = −(e/m_e)S (with g_s = 2 for the electron). The perturbation Hamiltonian is:

H' = (e B / 2m_e)(L_z + 2S_z)

The factor-of-2 difference between the orbital and spin contributions to the magnetic moment is the source of all the complexity. If it were 1 and 1, J_z would be diagonal and everything would be simple. The actual g_s = 2 means L_z + 2S_z = J_z + S_z, and S_z is not diagonal in the |j, m_j⟩ basis.

Source: Likharev, *Essential Graduate Physics — Quantum Mechanics* §6.4 [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Essential_Graduate_Physics_-_Quantum_Mechanics_(Likharev)/06:_Perturbative_Approaches/6.04:_The_Zeeman_Effect] — full derivation fetched.

**Weak-field limit (anomalous Zeeman effect):**
When the external field is weak compared to the fine-structure splitting (μ_B B ≪ fine-structure scale ~ α²Ry ~ 10⁻⁴ eV), the good quantum numbers are n, l, j, m_j (total angular momentum basis). The perturbation is evaluated in this basis using the Wigner-Eckart theorem / projection theorem for angular momenta.

Result: the energy shift is

ΔE = g_J μ_B B m_j

where the **Landé g-factor** is:

g_J = 1 + [j(j+1) + s(s+1) − l(l+1)] / [2j(j+1)]

This formula can be derived either by explicit Clebsch-Gordan expansion (the rigorous route, shown in Likharev) or by the elegant classical precession argument (J precesses slowly around B, while L and S precess rapidly around J; only the J-component of the magnetic moment matters on time average — this gives the Landé formula with no additional computation).

Key values for hydrogen:
- l = 0, j = 1/2 (s-states): g_J = 2 (pure spin; makes sense since m_l = 0)
- l = 1, j = 3/2 (2p₃/₂): g_J = 4/3
- l = 1, j = 1/2 (2p₁/₂): g_J = 2/3

A level with given j splits into 2j+1 equidistant m_j sublevels, spacing g_J μ_B B. Different fine-structure sublevels (different l, same j) have different g_J and thus different spacings — this is what makes the anomalous Zeeman pattern complex (many unequal spacings).

Historical note: Pieter Zeeman discovered the effect in 1896 (unauthorized lab use, fired from Leiden, then Nobel Prize 1902). The splitting was initially unexpected; the "anomalous" label reflects that spin was not yet known. The "normal" Zeeman effect (triplet, equal spacing) is actually the special case where net spin = 0.

Source: Likharev §6.4; Wikipedia "Zeeman effect" [https://en.wikipedia.org/wiki/Zeeman_effect]; Sciencenotes.org Zeeman Effect [https://sciencenotes.org/zeeman-effect-definition-physics-uses/]; Leicester lecture notes on Zeeman/Paschen-Back [https://www.star.le.ac.uk/~nrt3/322/lect9.pdf]

**Strong-field limit (Paschen-Back effect):**
When μ_B B ≫ fine-structure splitting, spin-orbit coupling is overwhelmed by the external field. The good quantum numbers become m_l and m_s separately (uncoupled representation). H' diagonal in |n, l, m_l, m_s⟩:

ΔE = μ_B B (m_l + 2m_s)

Each l-level (which was (2l+1)(2s+1) = 2(2l+1) degenerate) splits into (2l+3) distinct levels (some remain doubly degenerate except top and bottom). The pattern is simpler than the anomalous Zeeman effect; essentially a normal Zeeman triplet pattern plus spin splitting.

Source: Likharev §6.4 (with figure 6.5 of Paschen-Back pattern, fetched in full)

**Intermediate fields:**
The crossover between weak and strong field requires diagonalizing the full perturbation matrix (fine-structure + Zeeman) in the degenerate subspace. No closed-form result in general. Griffiths works out the n=2 hydrogen case numerically. The chapter should mention this but not develop it (appropriate for an advanced footnote).

### A2. The Stark effect (local source material available)

**From the local library file** `_lib_qmsri-09-time-independent-perturbation-theory.md`:

The perturbation is H' = eεẑ (electric field ε along ẑ).

**Ground state (n=1):**
First-order shift vanishes by parity: ⟨1s|eεẑ|1s⟩ = 0 (integrand is parity-odd). The shift is second-order (quadratic in ε): ΔE_1 = −(9/2)ε²a₀³ (in Gaussian units) — the **quadratic Stark effect**. The atom develops an induced electric dipole moment proportional to ε; this is the classical polarizability picture.

**n=2 manifold (linear Stark effect):**
Four degenerate states: |2s⟩, |2p₀⟩, |2p₊₁⟩, |2p₋₁⟩. Set up the 4×4 perturbation matrix W_ij = ⟨i|eεẑ|j⟩.

Selection rules eliminate all but one matrix element:
- Δm = 0 selection rule (ẑ commutes with L_z) zeros out all ⟨2s|...|2p_{±1}⟩ and ⟨2p₀|...|2p_{±1}⟩ entries
- Parity zeros all diagonal entries
- Surviving entry: ⟨2s|eεẑ|2p₀⟩ = −3a₀eε

The 4×4 matrix block-diagonalizes; the 2×2 block has eigenvalues ±3a₀eε. Result: n=2 splits into three levels:
- Up by +3a₀eε: eigenstate (|2s⟩ − |2p₀⟩)/√2
- Down by −3a₀eε: eigenstate (|2s⟩ + |2p₀⟩)/√2
- Unshifted (doubly degenerate): |2p₊₁⟩, |2p₋₁⟩

**Three lines from four states** — the answer to Stark's 1913 puzzle. The splitting is linear in ε (linear Stark effect) because degenerate states mix at first order. The |2p_{±1}⟩ states are azimuthally symmetric about ẑ and do not couple to the field at first order.

General rule: Linear Stark effect requires degeneracy of states with opposite parity (so that ẑ can connect them). Hydrogen has this accidental degeneracy (2s and 2p at same energy). In multi-electron atoms, s and p levels at the same principal quantum number are not degenerate — the Stark effect is always quadratic (second-order) unless an electric field is strong enough to mix different n levels.

Source: `_lib_qmsri-09-time-independent-perturbation-theory.md` (fetched in full, lines 83–121) — highly detailed, directly usable for the chapter.

### A3. Magnetic resonance

**Physical setup**: spin-1/2 particle (nucleus or electron) in a static field B₀ẑ, with a weak oscillating transverse field B₁(t) = B₁(x̂ cos ωt + ŷ sin ωt).

The static field gives Zeeman splitting ΔE = ℏω₀ where ω₀ = γB₀ (Larmor frequency, γ = gyromagnetic ratio). The spin precesses around ẑ at ω₀.

**Rotating frame:**
Transform to a frame rotating at frequency ω_r around ẑ. In this frame the static field appears reduced to B_eff = B₀ − ω_r/γ in the z-direction, and the oscillating transverse field appears static (along x̂ in the rotating frame). The effective Hamiltonian in the rotating frame is:

H_R = −ℏ(ω₀ − ω_r)S_z/ℏ − ℏω₁S_x/ℏ

where ω₁ = γB₁.

**Resonance condition**: ω_r = ω₀. At resonance, the z-component vanishes and H_R = −ℏω₁S_x — a pure x-field. The spin simply precesses around x̂ in the rotating frame, which means it oscillates between spin-up and spin-down at frequency ω₁ in the lab frame. These are **Rabi oscillations**.

**Rabi's original experiment (1938)**: Molecular beam deflected by inhomogeneous magnets; RF coil at midpoint. When ω_RF = ω₀ (Larmor frequency of the nucleus), the spin flips, deflection changes, detector count drops. Nobel Prize 1944.

**Pulsed NMR (Bloch and Purcell, 1946)**: Macroscopic sample. π/2 pulse tips magnetization into transverse plane; precession induces EMF in pickup coil (free induction decay, FID). π pulse flips spins → spin echo (Hahn 1950). From the FID and spin-echo decay times, extract T₁ (spin-lattice/longitudinal relaxation) and T₂ (spin-spin/transverse relaxation).

**Bloch equations** (phenomenological):
dM/dt = γM × H − x̂(Mx/T₂) − ŷ(My/T₂) − ẑ(Mz − M₀)/T₁

These equations describe the return of magnetization to equilibrium after a pulse. T₁ and T₂ are material-specific (hydrogen in water: T₁ ~ 1–3 s, T₂ ~ 0.1–3 s; fat: shorter T₁).

**ESR (Electron Spin Resonance)**: Same principle but for electrons. Because γ_e/γ_N ~ 1836 (mass ratio), electron Larmor frequencies are in the GHz (microwave) range vs. MHz (radio) for nuclei at the same field. ESR is used to study radicals, defects, and magnetic systems.

Source: Stephen, Fang & Wilson (UBC PHYS502 student paper), "Physical Principles of Nuclear Magnetic Resonance and Applications" [https://phas.ubc.ca/~berciu/TEACHING/PHYS502/PROJECTS/NMR16.pdf] — full PDF fetched, contains full derivation of rotating frame, Rabi oscillations, Bloch equations with proper quantum derivation. Excellent pedagogical source.

Also: Townsend notes (`_lib_qmsri-qm-townsend-notes.md`) — spin magnetic resonance example found in text: "Take a spin-S=1/2 particle in a B-field along z, [...] time-dependent Hamiltonian, Rabi oscillations" (confirmed in Grep at line 1725).

---

## B. Domain examples and cases

### Canonical worked example: weak-field Zeeman splitting of hydrogen 2p level

Setup: hydrogen atom, n=2, in a weak magnetic field B. Focus on the 2p manifold (ℓ=1) which is split by fine structure into 2p_{1/2} (j=1/2, 4 states) and 2p_{3/2} (j=3/2, 4 states).

**2p_{3/2} (j=3/2, g_J = 4/3):**
m_j = +3/2: ΔE = +2μ_B B
m_j = +1/2: ΔE = +2μ_B B/3
m_j = −1/2: ΔE = −2μ_B B/3
m_j = −3/2: ΔE = −2μ_B B

**2p_{1/2} (j=1/2, g_J = 2/3):**
m_j = +1/2: ΔE = +μ_B B/3
m_j = −1/2: ΔE = −μ_B B/3

Six distinct levels from the original 8-fold degenerate manifold (2×4 before fine structure). The optical transitions (Δm_j = 0, ±1) give the anomalous Zeeman pattern of multiple lines with unequal spacing — historically baffling, now completely explained.

Numerical scale: μ_B B ≈ 5.8 × 10⁻⁵ eV/T × B(T). At B = 1 T, μ_B B ≈ 0.058 meV. Fine-structure splitting of 2p is ~0.045 meV. So a 1 T field is already in the intermediate-field regime for the 2p states.

Source: Likharev §6.4 (figures 6.5–6.6 in fetched text, fully documented); Chem LibreTexts §5 "Zeeman Effect in Hydrogen atom" [https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Quantum_Mechanics/Zeeman_Effect/5:_Zeeman_Effect_in_Hydrogen_atom]

### Stark effect: three lines from four states (from local source)
See §A2 above — fully worked in the local library file. Author should use the existing worked example directly; it includes the matrix, eigenvalues, eigenstates, and physical interpretation.

### NMR pulse sequences
π/2 pulse → free precession → FID signal. Then spin echo (π/2 − τ − π): at time 2τ the dephased spins rephase, emitting an echo. This allows measurement of T₂ independent of field inhomogeneity. Worked numerical example: if T₂ = 100 ms and τ = 10 ms, what is the echo amplitude? Answer: exp(−2τ/T₂) = exp(−0.2) ≈ 0.82 (82% of maximum).

### MRI application
By applying a gradient magnetic field B₀ + Gz·z, the Larmor frequency varies with position (ω₀(z) = γ(B₀ + Gz·z)). Selective RF pulses excite only a thin slice. Spatial encoding in 2D uses further gradients during readout. The image contrast is determined by proton density and T₁/T₂ of different tissues. This is the real-world payoff of the magnetic resonance physics.

---

## C. Connections and dependencies

### Prerequisites from earlier in this volume (and prior volumes)
- Degenerate perturbation theory (Ch 9 of this volume): essential for the linear Stark effect and the Zeeman weak-field calculation
- Addition of angular momenta (Vol 2 or earlier in Vol 3): needed for the Clebsch-Gordan coefficients in the Landé g-factor derivation
- Spin-orbit coupling (fine structure, prior chapter): the Zeeman calculation sits on top of fine structure; the chapter should assume students know the j, m_j basis and why it diagonalizes the spin-orbit Hamiltonian
- Time-dependent perturbation theory (earlier in Vol 3): magnetic resonance is a time-dependent perturbation problem; Rabi oscillations are the exact solution of the two-state time-dependent Hamiltonian

### Forward connections
- Chapter 10 or later (if it exists): hyperfine structure — interaction of electron's magnetic moment with nuclear magnetic moment. Splits each fine-structure level by ~10⁻⁶ eV. The hydrogen 21-cm line (hyperfine) is one of the most important signals in radio astronomy.
- Quantum optics: the rotating frame and Bloch equations are the foundation of coherent optics, the optical Bloch equations, and laser spectroscopy.
- Quantum information: NMR-based quantum computing (Vandersypen et al. 2001, Shor's algorithm), qubit control via π and π/2 pulses, T₁ and T₂ as decoherence times.

---

## D. Current state of the field

**Zeeman effect:**
High-precision Zeeman spectroscopy is a central tool in atomic physics. The anomalous Zeeman pattern of multi-electron atoms encodes spin-orbit coupling constants; this is how atomic structure is determined experimentally. Magneto-optical trapping (MOT) for laser cooling relies on position-dependent Zeeman shifts to create spatially varying radiation pressure — the atom sees a restoring force. Nobel Prize (1997, Chu, Cohen-Tannoudji, Phillips) for laser cooling and trapping.

**Stark effect:**
Modern application: Rydberg atoms in electric fields show enormous Stark shifts (n⁷ scaling of polarizability). Used in quantum computing (neutral atom qubits) and electric-field sensing. Stark maps (Stark manifolds as function of n) are computed numerically and are complex but well-understood from perturbation theory.

**Magnetic resonance:**
MRI is a $10 billion/year medical technology industry. Clinical MRI operates at 1.5–7 T (proton Larmor frequency 63–300 MHz). 7 T whole-body scanners now available for research. Ultra-high field (11.7 T) human scanner at Paris Neurospin opened 2024.

ESR (EPR) spectroscopy: standard analytical tool for studying radicals, transition metal complexes, defects in semiconductors, spin labels in proteins. Pulsed EPR (analogous to pulsed NMR) allows measurement of distances between spin labels (DEER spectroscopy) up to ~10 nm.

NMR quantum computing: first demonstrations (Vandersypen et al. 2001, *Nature* 414, 883) of Shor's algorithm on 7-qubit NMR quantum computer. No longer competitive with other platforms (limited scalability due to ensemble nature and mixed states) but historically important and pedagogically clean.

---

## E. Teaching considerations

### The conceptual arc
Three pillars:
1. **Zeeman** — magnetic field lifts degeneracy; why the pattern is "anomalous" without spin but simple with it; the Landé g-factor as the crux
2. **Stark** — electric field lifts degeneracy; parity kills first-order for non-degenerate levels; hydrogen's accidental degeneracy allows linear splitting; the "three lines from four states" answer to Stark's 1913 experiment
3. **Magnetic resonance** — the rotating frame trick converts a time-dependent problem to a static one; at resonance the spin flips completely; Bloch equations add relaxation

### Key pedagogical moves
- **Zeeman**: derive the Landé formula twice — once rigorously (Clebsch-Gordan; shown in Likharev §6.4) and once via the classical precession argument. The two derivations converge on the same formula; students gain confidence.
- **Stark**: use the Stark calculation to reinforce degenerate perturbation theory — let students see it as a second application of the same machine from Ch 9. The 4×4 matrix → block-diagonalization → eigenvalues workflow is identical in structure.
- **Magnetic resonance**: the rotating frame is the single most important idea. Show that an exact solution exists at resonance. Then make contact with Rabi's experiment and modern NMR.

### Common confusions
- Zeeman: students confuse the (uncoupled) m_l, m_s basis with the (coupled) j, m_j basis. The distinction between weak-field (use coupled basis) and strong-field (use uncoupled basis) is exactly the physical content of the chapter.
- Stark: students forget parity selection rules apply to the diagonal elements too — ⟨nlm|ẑ|nlm⟩ = 0 always by parity. This eliminates all diagonal terms before any computation.
- Rabi oscillations: students sometimes confuse the Rabi frequency ω₁ = γB₁ (determines the rate of spin flip in the rotating frame) with the Larmor frequency ω₀ = γB₀ (determines the resonance condition). Clear notation is essential.

### Simulation opportunity
Three linked simulations:
1. Zeeman: energy-level diagram for hydrogen 2p as function of B, with fine-structure as background. Slider for B from 0 to 10 T. Shows transition from anomalous (weak) to Paschen-Back (strong) regime.
2. Stark: reproduce the Ch 9 simulation — the n=2 Stark manifold splitting as function of electric field ε.
3. Bloch sphere: show magnetization vector M on the Bloch sphere; π/2 pulse, free precession, π pulse, echo. Students control pulse duration and off-resonance detuning.

---

## F. Library files relevant to this chapter

**Local sources (strong):**
- `/pantry/_lib_qmsri-09-time-independent-perturbation-theory.md` — **directly usable for Stark effect**. Contains the full n=2 Stark calculation (lines 83–121): the 4×4 matrix, selection rules, eigenvalues ±3a₀eε, "three lines from four states." Also contains the ground-state quadratic Stark effect discussion and the fine-structure section (hydrogen fine structure, good quantum numbers (n,l,j,m_j)).
- `/pantry/_lib_qmsri-qm-townsend-notes.md` — confirmed (Grep): contains a "spin magnetic resonance" example (line 1725) with a spin-1/2 in a B-field. Also references: "Griffiths & Schroeter, the 'Time-Independent Perturbation Theory' chapter (fine structure, the Zeeman effect, and hyperfine splitting of hydrogen)" — confirms Griffiths as a relevant external source.

**External sources:**
- Likharev, *Essential Graduate Physics — QM*, §6.4 "The Zeeman Effect" [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Essential_Graduate_Physics_-_Quantum_Mechanics_(Likharev)/06:_Perturbative_Approaches/6.04:_The_Zeeman_Effect] — CC BY-NC-SA 4.0; **strongest single source for the Zeeman effect**. Contains both the rigorous Clebsch-Gordan derivation of the Landé g-factor and the classical precession argument. Figures 6.5 (Paschen-Back) and 6.6 (anomalous Zeeman) explicitly documented.
- Stephen, Fang & Wilson (UBC), "Physical Principles of NMR" [https://phas.ubc.ca/~berciu/TEACHING/PHYS502/PROJECTS/NMR16.pdf] — full PDF obtained. Contains: quantum derivation of rotating frame, Rabi oscillation in density matrix language, Bloch equations with T₁ and T₂, spin echo, MRI and NMR spectroscopy applications.
- Griffiths & Schroeter, *Introduction to Quantum Mechanics*, Ch. 6 — Zeeman, Stark, hydrogen fine structure. Standard undergraduate treatment.
- Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch. 5 (approximation methods) — covers time-independent perturbation theory applications to atoms in fields.

---

## G. Gaps and flags

- **Magnetic resonance needs more than local sources**: the Townsend notes contain only a brief spin-resonance example. The UBC NMR PDF fills this gap adequately for the basics; for ESR the author should consult Griffiths Ch. 9 or a dedicated ESR text.
- **Landé g-factor derivation**: the Likharev derivation uses coupled Clebsch-Gordan coefficients. This may be too heavy for students who have not yet done angular momentum addition formally. The classical precession argument is lighter. Author should decide which to lead with. Flag: if angular momentum addition was not treated in depth earlier in the series, the Clebsch-Gordan route needs more setup.
- **Intermediate Zeeman-fine structure crossover**: no analytic result. Likharev acknowledges "there is no time in this course for a quantitative analysis of this crossover." Same limitation should be explicit in this chapter. A numerical figure (energy vs. B for n=2 hydrogen) is standard in Griffiths and should be included.
- **Hyperfine structure**: not covered in this chapter but should be flagged for future treatment. The 1420 MHz (21 cm) hydrogen line (hyperfine, F=1→0 transition) is mentioned in back matter of Townsend notes as a key radio astronomy signal.
- **Stark effect in multi-electron atoms**: always quadratic (no accidental degeneracy). Worth a paragraph noting why hydrogen is special. No detailed calculation needed.
- **QED corrections to g-factor**: the true electron g-factor is g_e = 2.002319... not exactly 2. This difference (the anomalous magnetic moment) is a QED effect. Worth noting in the "still puzzling / limits of the chapter" section. The measurement to 13 significant figures (Hanneke et al. 2008) is one of the great triumphs of physics.
- **NMR applications depth**: the UBC PDF covers MRI, NMR spectroscopy, and NMR quantum computing. The chapter should probably mention all three in a "domain examples" box but not develop them at full length.
