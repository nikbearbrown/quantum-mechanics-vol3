# Research Notes: Chapter 02 — Degenerate Perturbation Theory and Fine Structure

**Corresponding chapter:** chapters/02-degenerate-perturbation-theory-and-fine-structure.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to: identify when nondegenerate PT fails (zero denominator); construct the perturbation matrix W_{ij} = ⟨i|H'|j⟩ restricted to the degenerate subspace; find the "good" zeroth-order states by diagonalizing W; apply the procedure to the hydrogen n=2 linear Stark effect; and then extend to the three-perturbation fine-structure problem of hydrogen, identifying the correct good quantum numbers (n, ℓ, j, m_j), computing each of the three corrections (relativistic kinetic, spin-orbit, Darwin), and reading off the combined fine-structure formula.

---

## A. Conceptual Foundations

### A1. Why nondegenerate PT fails and what the fix is

When two or more unperturbed states share the same energy E^(0), the first-order state correction Σ ⟨m|H'|n⟩/(E_n⁰ − E_m⁰) has a zero denominator for those states. The formula is undefined. The underlying reason: any linear combination of degenerate eigenstates is an equally valid zeroth-order state, but the perturbed eigenstates connect smoothly to only one particular combination as λ → 0. The perturbation picks out that preferred basis; the fix is to find it first.

**Procedure:** (1) Identify the degenerate subspace (dimension g). (2) Build the g×g matrix W with entries W_{ij} = ⟨i|H'|j⟩. (3) Diagonalize W. Its eigenvalues are the first-order energy corrections E_n^(1); its eigenvectors are the "good" zeroth-order states. (4) Resume nondegenerate PT from there, treating states outside the subspace normally.

**Common misconception:** Students think the "good" states are always the obvious symmetric/antisymmetric combinations. In general they are whatever diagonalizes W — which depends on the specific perturbation. For the 2D HO with an xy perturbation, the good states are the (|10⟩ ± |01⟩)/√2 combinations. For the Stark effect they are (|2s⟩ ± |2p₀⟩)/√2. But for a different perturbation on the same degenerate manifold, the good states would be different.

**Worked example (Townsend §3.3, 2D harmonic oscillator with H' = αmω²xy):** The unperturbed states |10⟩ and |01⟩ share energy 2ℏω. The 2×2 W matrix: diagonal elements vanish (⟨10|xy|10⟩ = 0 by parity), off-diagonal ⟨01|xy|10⟩ = ℏα/2. Eigenvalues: ±ℏαω/2. Good states: (|10⟩ ± |01⟩)/√2. Exact eigenvalues: ℏω√(1 ± α) ≈ ℏω(1 ± α/2) — PT reproduces the leading term.

**Sources:** `_lib_qmsri-09` (When the denominator vanishes section); `_lib_qmsri-qm-townsend-notes.md` lines 1381–1548 (§3.3 full development, 2D HO example, two-level avoided crossing, general g-fold procedure with the block-diagonal W matrix displayed).

---

### A2. The linear Stark effect for hydrogen n=2

The n=2 manifold of hydrogen is 4-fold degenerate: |2s⟩, |2p₀⟩, |2p₊₁⟩, |2p₋₁⟩. The perturbation is H' = eEz. Selection rules (from [H, L_z] = 0 → Δm = 0, and parity → diagonal matrix elements of z vanish) reduce the 4×4 W matrix to a single nonzero off-diagonal entry: ⟨2s|z|2p₀⟩ = −3a₀.

The 4×4 matrix:

```
         |2s⟩     |2p₀⟩    |2p₊₁⟩  |2p₋₁⟩
|2s⟩    [  0    −3a₀eE      0        0   ]
|2p₀⟩   [−3a₀eE    0        0        0   ]
|2p₊₁⟩  [  0       0        0        0   ]
|2p₋₁⟩  [  0       0        0        0   ]
```

Eigenvalues: +3a₀eE, −3a₀eE, 0, 0. Three distinct energies from four states. The |2p₊₁⟩ and |2p₋₁⟩ states are already "good" (azimuthally symmetric, cannot polarize along z at first order). The good states from the upper 2×2 block are (|2s⟩ ∓ |2p₀⟩)/√2 — asymmetric probability clouds aligned with or against the field.

**Common misconception:** Students sometimes think three eigenvalues means three states, missing that the doubly degenerate zero eigenvalue accounts for two states (|2p₊₁⟩ and |2p₋₁⟩). The experiment sees three spectral lines, not three levels; the degeneracy of the middle line is observable only by further resolution.

**Worked example:** At field strength E = 0.01 atomic units, the upper splitting is +3a₀eE = +0.03 Hartree. This is linear in E — the "linear Stark effect" — whereas the ground state has a quadratic Stark effect because it lacks a partner state at the same unperturbed energy to mix with at first order.

**Sources:** `_lib_qmsri-09` (The Stark effect: three lines from four states — full treatment with selection-rule argument and matrix); `_lib_qmsri-qm-townsend-notes.md` lines 1554–1582 (§3.4 linear Stark, matrix elements, eigenvalues); Physics LibreTexts, "3.3: Example of Degenerate Perturbation Theory — Stark Effect in Hydrogen" (https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Quantum_Physics_(Ackland)/03:_Dealing_with_Degeneracy/3.03:_Example_of_degenerate_perturbation_theory_-_Stark_Effect_in_Hydrogen).

---

### A3. The three fine-structure perturbations

Hydrogen with the bare Coulomb Hamiltonian gives E_n = −13.6 eV/n². High-resolution spectroscopy reveals corrections of order α²|E_n| ∼ 10⁻⁴ eV at n=2. Three perturbations produce them:

**H'_rel (relativistic kinetic correction):** The non-relativistic kinetic energy p²/2m is the first term in the expansion of √(p²c² + m²c⁴) − mc². The next term is −p⁴/(8m³c²). This shifts every level, including ℓ = 0.

**H'_SO (spin-orbit coupling):** In the electron's rest frame, the orbiting proton creates a magnetic field B ∝ L/(mr³) that couples to the electron's spin magnetic moment. After the Thomas precession factor of 1/2 (a relativistic kinematic correction): H'_SO = (e²/4πε₀m²c²r³) L·S × (1/2). The Thomas factor is a classic source of errors in textbooks. Using J = L + S and 2L·S = J² − L² − S², the good quantum numbers are (n, ℓ, j, m_j). The matrix element is proportional to ℏ²[j(j+1) − ℓ(ℓ+1) − 3/4] × ⟨1/r³⟩_{nℓ}.

The radial expectation value: ⟨1/r³⟩_{nℓ} = 1/(a₀³ n³ ℓ(ℓ+1/2)(ℓ+1)) — vanishes for ℓ = 0, which is physically correct (no orbital angular momentum, no spin-orbit coupling).

**H'_Darwin (Darwin term):** A purely relativistic (Dirac equation) correction, nonzero only for ℓ = 0 states (the wave function has finite amplitude at the nucleus). Physically: the "Zitterbewegung" — rapid quantum jitter of a relativistic electron smears out the Coulomb potential. H'_Darwin = (πℏ²/2m²c²)(e²/4πε₀) δ³(r).

**Common misconception:** Students often omit the Thomas factor 1/2 from the spin-orbit term, getting the wrong coefficient. The factor arises from the non-inertial (rotating) frame of the electron and is not obvious from the naive frame-boost argument. It must be derived from the Dirac equation or from Lorentz covariance of the electromagnetic tensor.

**Sources:** `_lib_qmsri-09` (Hydrogen fine structure section, all three terms with formulas); `_lib_qmsri-qm-townsend-notes.md` lines 3086–3148 (spin-orbit coupling derivation from electron rest frame, the J-basis, the boxed formula for E_SO^(1), the ⟨1/r³⟩ radial expectation value); MIT OpenCourseWare 8.06, "Chapter 2: Fine Structure," https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2018/439fc15f7ed10dd76c69dc3f7fea600e_MIT8_06S18ch2.pdf (B. Zwiebach; comprehensive treatment including Thomas precession).

---

### A4. The combined fine-structure formula and n=2 splitting

When all three perturbations are included and the degenerate subspace within fixed n is diagonalized using (n, ℓ, j, m_j) as good quantum numbers, the combined first-order energy correction is:

$$E_n^{\text{fs}} = \frac{(E_n^{(0)})^2}{2mc^2}\left(\frac{2n}{j + 1/2} - \frac{3}{2}\right)$$

This result depends on n and j only — not on ℓ separately. A remarkable cancellation: the relativistic correction and the spin-orbit correction each depend on ℓ, but their sum does not (for ℓ ≠ 0; the Darwin term handles ℓ = 0 to produce the same j-only formula). This accidental degeneracy in ℓ is a signature of the hidden SO(4) symmetry of the Coulomb problem.

**For n=2:** j can be 1/2 (with ℓ = 0 or ℓ = 1) or 3/2 (ℓ = 1 only).
- 2s_{1/2} and 2p_{1/2}: j = 1/2, E_2^fs = (E_2⁰)²/(2mc²) × [4/1 − 3/2] = (E_2⁰)²/(2mc²) × 5/2
- 2p_{3/2}: j = 3/2, E_2^fs = (E_2⁰)²/(2mc²) × [4/2 − 3/2] = (E_2⁰)²/(2mc²) × 1/2

The splitting between j=3/2 and j=1/2 states: ΔE = (E_2⁰)²/(2mc²) × 2 ≈ 4.5 × 10⁻⁵ eV.

**Numerically:** E_2⁰ = −3.4 eV; (3.4)²/(2 × 0.511 × 10⁶) × 2 ≈ 4.5 × 10⁻⁵ eV. In terms of α²: ΔE ≈ α²|E_2⁰|/4 — confirming the α² scale of fine structure.

**Common misconception:** Students often expect four distinct levels for n=2 after fine structure (since there are four distinct ℓ, m_ℓ, m_s combinations). In fact there are only two distinct energies: the 2s_{1/2}/2p_{1/2} pair remains degenerate (j = 1/2 level), and the 2p_{3/2} quartet sits higher. Only QED (the Lamb shift) further resolves 2s_{1/2} from 2p_{1/2}.

**Sources:** `_lib_qmsri-09` (combined formula displayed, n=2 numerical values, Lamb shift note); Colorado PHYS 5250 lecture notes, "Hydrogen Fine Structure" https://physicscourses.colorado.edu/phys5250/phys5250_fa19/lecture/lec41-hydrogen-fine-structure/ (treats all three corrections and the good quantum number argument); UT Austin notes, "Fine Structure of Hydrogen" https://farside.ph.utexas.edu/teaching/qmech/Quantum/node107.html; Wikipedia, "Fine structure" https://en.wikipedia.org/wiki/Fine_structure (concise summary of contributions, experimental values).

---

### A5. Where fine structure stops: the Lamb shift

The 2s_{1/2} and 2p_{1/2} states are degenerate in the fine-structure formula. Lamb and Retherford (1947) showed they are not experimentally degenerate: there is a ~1057 MHz (≈ 4.4 × 10⁻⁶ eV) splitting now called the Lamb shift. Its origin is QED: vacuum fluctuations of the electromagnetic field slightly smear the electron's position, shifting the 2s state (which samples the nucleus) more than the 2p state. This is the first major success of renormalized QED and lies outside semiclassical perturbation theory. This chapter derives the fine-structure formula and then explicitly points to the Lamb shift as the boundary of its framework.

**Common misconception:** Students sometimes think the Darwin term and the Lamb shift are the same thing. They are not. The Darwin term is a classical-looking correction from the Dirac equation (one-particle relativistic QM); the Lamb shift requires quantizing the electromagnetic field.

**Sources:** `_lib_qmsri-09` (last paragraph of the fine structure section, explicit Lamb shift note); W. E. Lamb & R. C. Retherford, "Fine Structure of the Hydrogen Atom by a Microwave Method," *Physical Review* **72**, 241 (1947) — the original measurement.

---

## B. Domain Examples and Cases

**B1. Hydrogen n=2, linear Stark effect** — the workhorse worked example for degenerate PT. Full 4×4 matrix, selection rules, three eigenvalues, good-state geometry.

**B2. Hydrogen n=2 fine structure** — the workhorse worked example for the three-perturbation calculation. Numerical values: ΔE(j=3/2 − j=1/2) ≈ 4.5 × 10⁻⁵ eV; Lamb shift ≈ 4 × 10⁻⁶ eV (one order smaller).

**B3. 2D harmonic oscillator with xy coupling (Townsend §3.3)** — transparent 2×2 diagonalization; exact solution available for comparison.

**B4. Two-level avoided crossing (general)** — the universal 2×2 result E± = ½(E₀ + E₁) ± ½√((E₀−E₁)² + 4V²); degeneracy at E₀ = E₁ gives ±V; the generic level-repulsion structure.

**B5. Zeeman effect (weak field)** — natural extension: add H_Zeeman = μ_B B(L_z + 2S_z)/ℏ as a further perturbation on top of fine structure. The good quantum numbers at weak field are still (n, ℓ, j, m_j); the Landé g-factor emerges.

---

## C. Connections and Dependencies

- **Prerequisite:** Ch. 1 nondegenerate PT; angular momentum addition and Clebsch-Gordan coefficients (J = L + S); the hydrogen atom spectrum (Vol. 2).
- **Prerequisite for fine structure:** Understanding that 2L·S = J² − L² − S² is the key algebraic identity that makes the j-basis diagonal.
- **Leads to Ch. 3 (variational):** The variational principle is needed precisely because fine structure and electron-electron repulsion cannot always be handled by PT alone.
- **Connects to hyperfine structure (Townsend Ch. 7):** The same degenerate PT machinery, now with total angular momentum F = J + I.

---

## D. Current State of the Field

- **Precision hydrogen spectroscopy:** The 1s−2s two-photon transition has been measured to 15 significant figures (Parthey et al., *Physical Review Letters* 107, 203001, 2011), enabling tests of QED at the sub-ppm level and searches for proton-radius anomalies.
- **Lamb shift and proton radius puzzle:** The 2013 measurement of the Lamb shift in muonic hydrogen gave a proton charge radius 4% smaller than the electron-hydrogen value, triggering extensive theoretical and experimental investigation (Pohl et al., *Nature* 466, 213, 2010). Largely resolved by 2019 reanalysis.
- **Spin-orbit coupling in condensed matter:** The same L·S operator structure drives Rashba spin-orbit coupling in semiconductor heterostructures and topological insulators — a major contemporary physics topic.

---

## E. Teaching Considerations

- **The good-states concept needs geometric motivation.** Draw the degenerate subspace as a 2D plane; the unperturbed Hamiltonian cannot distinguish directions in this plane; the perturbation picks a preferred direction (its eigenvectors). This picture prevents the "why does diagonalizing W fix anything?" confusion.
- **Selection rules before calculation.** Strongly emphasize the Stark matrix zeroing by selection rules before computing any integral. Students who compute all 16 matrix elements first miss the insight.
- **The Thomas factor.** Either derive it from the Lorentz boost (a calculation), or simply state it and point to the Dirac equation. Do not silently include it — students who read naive frame-boost arguments get the wrong factor of 2.
- **Level diagram for n=2.** A clear diagram showing the four unperturbed states → two fine-structure levels → Lamb shift separation is worth one full page. Include numerical values in eV and in terms of α².
- **Simulation target:** The hydrogen n=2 Stark manifold in the Mode B of the `09-perturbation-explorer.html` simulation (described in `_lib_qmsri-09`) directly visualizes the 4×4 W matrix and the three eigenvalues. Students should run this before the fine-structure calculation.

---

## F. Library Files Relevant to This Chapter

- `/pantry/_lib_qmsri-09-time-independent-perturbation-theory.md` — **Primary.** Sections on degenerate PT, the Stark effect (full 4×4 matrix treatment), and the hydrogen fine structure formula (all three terms, numerical values, Lamb shift boundary). Lines 67–115 (degenerate PT), 83–115 (Stark effect), 173–195 (fine structure).
- `/pantry/_lib_qmsri-qm-townsend-notes.md` — **Secondary.** Chapter 3 §3.3 (lines 1381–1548): degenerate PT general framework, 2D HO example, two-level avoided crossing. Chapter 7 (lines 2903–3160): spin-orbit coupling derivation with frame-boost argument, the boxed E_SO^(1) formula, ⟨1/r³⟩ radial integral, fine structure overview with diagram.

---

## G. Gaps and Flags

- **The Thomas factor derivation** is mentioned in `_lib_qmsri-qm-townsend-notes.md` (frame-boost argument) but the factor of 1/2 is stated without a complete derivation. The chapter should either include the derivation or clearly defer to the Dirac equation.
- **The Darwin term** is referenced in `_lib_qmsri-09` and `_lib_qmsri-qm-townsend-notes.md` (line 3152: "terms arising from Dirac's equation") but is not computed explicitly in either local source. Web supplement needed: MIT 8.06 Chapter 2 (Zwiebach) has the full Darwin-term calculation. Flag this gap.
- **Relativistic kinetic correction ⟨p⁴⟩ expectation value:** The result ⟨n,ℓ|p⁴|n,ℓ⟩ requires computing ⟨1/r²⟩ and ⟨1/r⟩ hydrogen expectation values. Both are standard but non-trivial; the chapter should provide these or cite them explicitly. Griffiths §7.3 has the clean derivation.
- **Accidental degeneracy (ℓ-independence of E_n^fs):** The cancellation between relativistic and spin-orbit corrections to yield a j-only formula is non-trivial. A brief proof or note on why this happens (hidden SO(4) symmetry) would enrich the chapter.
- **Numerical check needed:** The value 4.5 × 10⁻⁵ eV for the n=2 fine-structure splitting should be verified against the fine-structure constant: α ≈ 1/137, α² ≈ 5.3 × 10⁻⁵, |E_2| = 3.4 eV, α²|E_2|/4 ≈ 4.5 × 10⁻⁵ eV. Confirmed consistent.
