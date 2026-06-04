# Research Notes: Chapter 04 — The WKB Approximation and Tunneling

**Corresponding chapter:** chapters/04-the-wkb-approximation-and-tunneling.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

After this chapter the student can: (1) write the WKB ansatz, state its validity condition, and identify where it fails; (2) apply the connection formulas at a classical turning point and state the Maslov phase; (3) use Bohr–Sommerfeld quantization to estimate bound-state energies; (4) compute the Gamow factor for an arbitrary barrier shape and estimate a tunneling transmission coefficient; (5) reproduce a back-of-envelope Geiger–Nuttall estimate for alpha-decay halflives; (6) identify the same exponential tunneling logic in STM, flash memory, and stellar fusion.

---

## A. Conceptual foundations

### The WKB ansatz and the semiclassical expansion

Write ψ = exp(iS/ħ) and expand S in powers of ħ. At zeroth order S₀ satisfies the Hamilton–Jacobi equation; at first order the correction produces the 1/√p(x) amplitude envelope. The resulting WKB wave function is:

- Classically allowed region (E > V): ψ ∝ (1/√p) exp(±i∫p dx/ħ)
- Classically forbidden region (E < V): ψ ∝ (1/√|p|) exp(±∫|p| dx/ħ)

The 1/√p prefactor is the semiclassical amplitude: |ψ|² ∝ 1/p(x), matching the classical time-spent distribution (slow particle → large amplitude). The expansion is controlled by the small parameter ħ (formally ħ→0), which is what "semiclassical" means precisely.

**Key source:** Griffiths & Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., §9.1. The derivation via S = S₀ + (ħ/i)S₁ + ... is explicit in Bender & Orszag, *Advanced Mathematical Methods for Scientists and Engineers* (1978), Ch. 10.

### Validity condition and its failure

The WKB approximation requires |dλ_dB/dx| ≪ 1, where λ_dB = h/p(x) is the local de Broglie wavelength. Equivalently: the potential must vary slowly on the scale of one de Broglie wavelength. This condition fails precisely at classical turning points x₀ where E = V(x₀) and p → 0 — the wavelength diverges. The fix is to linearize V near x₀, solve the resulting Airy equation exactly, and match its asymptotic forms to the WKB solutions on each side. Each turning point contributes a Maslov phase of π/4, shifting the phase of the oscillatory solution by that amount.

The condition ∫p dx ≫ ħ (large classical action in units of ħ) is an equivalent statement: the particle must traverse many de Broglie wavelengths for the approximation to hold. This is the "correspondence principle" quantification.

### Connection formulas and the Maslov index

The Airy equation Ai''(z) = z·Ai(z) has asymptotic forms:
- z → +∞ (forbidden side): Ai ∝ z^{-1/4} exp(-2z^{3/2}/3)
- z → -∞ (allowed side): Ai ∝ |z|^{-1/4} cos(2|z|^{3/2}/3 - π/4)

The π/4 phase shift in the cosine is the Maslov correction. Deriving the connection formulas explicitly, rather than quoting them, is pedagogically essential: it shows why the phase shift arises from the Airy function asymptotics and not from the WKB form itself.

**Reference:** Liboff, *Introductory Quantum Mechanics*, §7.7; Griffiths §9.2.

### Bohr–Sommerfeld quantization

For a particle bound between turning points a and b:

∮ p dx = 2∫_a^b p(x) dx = (n + 1/2)h, n = 0, 1, 2, ...

The 1/2 inside the bracket is the Maslov correction (two turning points, each contributing π/4, combining into a phase of π/2 or equivalently 1/2 in units of h). The original 1913–1916 Bohr–Sommerfeld rule had nh; WKB gives the correct 1/2. The harmonic oscillator and Coulomb potential give exact results from Bohr–Sommerfeld because of hidden algebraic symmetries; for generic V(x), Bohr–Sommerfeld is a leading-order estimate good for large n.

### The Gamow factor for barrier tunneling

For a barrier V(x) > E between classical turning points a and b, the WKB transmission coefficient is:

T ≈ exp(-2γ), where γ = (1/ħ)∫_a^b √(2m(V(x)-E)) dx

This is the Gamow factor. Three features control everything:
1. T is exponential in γ: small changes in E, V₀, or barrier width produce large changes in T.
2. γ integrates the full barrier shape; arbitrary V(x) is handled automatically.
3. Prefactors of order unity (from the exact WKB connection matching) multiply exp(-2γ) but are irrelevant for order-of-magnitude estimates spanning many decades.

For a rectangular barrier of height V₀ and width L: γ = κL where κ = √(2m(V₀-E))/ħ. The exact result T_exact = [1 + V₀²sinh²(κL)/(4E(V₀-E))]^{-1} differs from T_WKB = exp(-2κL) by the prefactor 16E(V₀-E)/V₀² in the thick-barrier limit. On a log plot, the two curves run parallel (same exponential slope), offset by the smooth prefactor.

**Primary source for the Gamow factor:** Gamow, "Zur Quantentheorie des Atomkernes," *Zeitschrift für Physik* 51, 204 (1928); Gurney & Condon, *Nature* 122, 439 (1928) and *Physical Review* 33, 127 (1929).

---

## B. Domain examples and cases

### Alpha decay and the Geiger–Nuttall law

Model the alpha particle as bouncing inside a nucleus of nuclear radius R against a Coulomb barrier V(r) = 2Z'e²/(4πε₀r) for r > R. The classical turning point r_c = 2Z'e²/(4πε₀E_α). For ²³⁸U: Z'=90, E_α ≈ 4.2 MeV, R ≈ 7.4 fm, r_c ≈ 60 fm — the barrier is 8× wider than the nucleus.

The Coulomb Gamow integral can be done analytically (substitution r = r_c sin²θ):

γ ≈ (πZ'e²/4ε₀ħ)√(m_α/2E_α) - 2√(2m_αRr_c·E_α/E_α²) [leading and subleading terms]

The decay rate: Γ ~ ν₀ exp(-2γ), where ν₀ ~ v/(2R) ~ 10²¹ Hz (attempt frequency).

For ²³⁸U: γ ≈ 43, so exp(-2γ) ≈ 10^{-38}. Predicted halflife ~5×10⁸ years; experimental value 4.5×10⁹ years. Off by a factor of ~10 on a quantity spanning 10²⁴ — within rounding errors of the WKB prefactor and the alpha pre-formation probability.

The Geiger–Nuttall law (1911) — log(τ_{1/2}) linear in 1/√E_α for fixed daughter charge Z' — follows directly from γ ∝ Z'/√E_α. This empirical rule from 1911 is derived from WKB theory.

**Reference:** Geiger & Nuttall, *Phil. Mag.* 22, 613 (1911); 23, 439 (1912). Gamow's paper (1928) is the derivation.

### Scanning tunneling microscope (STM)

Work function φ ≈ 4–5 eV for typical metals, so κ = √(2m_e φ)/ħ ≈ 1 Å⁻¹. Tunneling current I ∝ exp(-2κd). When tip-sample distance d changes by 1 Å, current changes by factor e² ≈ 7. This exponential transduction converts sub-angstrom topographic variation into measurable current — the basis of atomic-resolution imaging.

**Reference:** Binnig & Rohrer, *Physical Review Letters* 49, 57 (1982) — Nobel Prize 1986.

### Stellar fusion and the Gamow peak

At solar core temperature T ~ 1.5×10⁷ K, kT ~ 1 keV, but the Coulomb barrier for p-p fusion is ~1 MeV. Most fusion occurs not at kT but at the Gamow peak energy E_G = (bkT/2)^{2/3} where b = πe²√(2m_p)/(4ε₀ħ) ≈ 31.3 keV^{1/2}. At solar T: E_G ≈ 6 keV — six times kT. The rate is the product of the Maxwell–Boltzmann thermal tail and the Gamow tunneling factor; the peak of the product is the Gamow peak.

**Reference:** Atkinson & Houtermans, *Z. Phys.* 54, 656 (1929); see also Clayton, *Principles of Stellar Evolution and Nucleosynthesis* (1968), Ch. 4.

### Flash memory (Fowler–Nordheim tunneling)

Electrons tunnel through a thin SiO₂ layer (~10 nm) under a high electric field — the barrier becomes triangular (linearly ramped by the field). The Gamow factor for a triangular barrier differs from rectangular: γ_triangular = (4/3)√(2m(φ-E)³)/(ħeF) where F is the field. The write speed and data retention time of NAND flash are both controlled by this exponent.

**Reference:** Fowler & Nordheim, *Proc. R. Soc. A* 119, 173 (1928).

### Cold fusion falsification

At T = 300 K: kT ≈ 0.025 eV. Coulomb barrier for D-D at nuclear contact (~2 fm): V_max ~ 0.7 MeV. Gamow factor γ ~ (πe²/4ε₀ħ)√(m_D/2kT) ~ 1000. So exp(-2γ) ~ 10^{-900}. Claimed power output of 1 W/cm³ requires ~10¹² fusions/second. The required tunneling rate is ~10^{900} times the WKB prediction. The calculation takes five minutes; the conclusion is unambiguous.

### DNA proton tunneling (open question)

Löwdin (1963) proposed protons in Watson-Crick hydrogen bonds tunnel between tautomeric positions, contributing to spontaneous mutations. Barrier: ~0.3 eV, ~0.3 Å wide, proton mass. The Gamow factor is not astronomically large — the mechanism is physically plausible. Whether proton tunneling contributes measurably to mutation rates in vivo, versus thermal isomerization, is not settled. Recent open-system quantum simulations (Slocombe et al., *Communications Physics* 5, 109 [2022]) suggest viability for G-C pairs. Unsettled as of 2026.

---

## C. Connections and dependencies

**Prerequisite material (Vol. 1/2):**
- Time-independent Schrödinger equation in 1D; boundary conditions; square-well and step-barrier exact solutions
- Classical Hamilton–Jacobi equation (provides motivation for the WKB ansatz)
- Airy functions (typically introduced briefly here for the first time; a full special-functions background is not needed)

**Connections within Vol. 3:**
- Ch. 1 (variational method): complementary approximation — WKB for large action, variational for ground states without a small parameter
- Ch. 3 (time-independent perturbation theory): both produce energy corrections, but WKB applies when the correction is NOT small (large quantum number regime)
- Ch. 5–6 (time-dependent PT and Fermi's golden rule): the Gamow factor gives a tunneling amplitude; Ch. 5–6 convert amplitudes to rates via density of states

**Forward connections:**
- WKB in 3D: the Langer correction (centrifugal term) for radial potentials; r → x substitution care near r = 0
- Instanton calculus in quantum field theory: WKB tunneling in field-space path integrals (the "bounce" solution)
- JWKB higher-order corrections: subleading terms in the ħ expansion that matter for precision spectroscopy

---

## D. Current state of the field

**Tunneling time controversy:** At least four distinct definitions of "tunneling time" exist in the literature — phase time (group delay), dwell time, Büttiker–Landauer traversal time, Larmor clock. Attosecond-streaking experiments (Eckle et al., *Science* 322, 1525 [2008]; Landsman et al., *Optica* 1, 343 [2014]) measure something at the attosecond scale, but which theoretical time it corresponds to remains under debate. The Hartman effect (phase time saturates to a constant at large barrier thickness, implying apparent superluminal tunneling) is real but does not violate causality because the group delay is not a signal velocity. The chapter should state this honestly: the WKB framework gives T but not a tunneling time; this is a genuine open question.

**Resonant tunneling diodes:** Double-barrier structures exhibit resonant tunneling — T → 1 at specific energies corresponding to quasi-bound states in the well, even when each individual barrier is highly opaque. RTDs are commercial devices (microwave oscillators, terahertz sources). The physics is a direct extension of the Gamow factor to a double-barrier geometry.

**Macroscopic quantum tunneling (MQT):** Josephson junctions — superconducting circuits — tunnel between flux states in a washboard potential. The effective mass is set by the circuit capacitance, not an electron mass. MQT was confirmed experimentally by Devoret et al. (1985) and is the operational mechanism of transmon qubits: the qubit basis states are the two lowest levels of the Josephson cosine potential, and MQT out of the "trap" limits qubit coherence time.

---

## E. Teaching considerations

### High-value misconceptions to address

1. **"Tunneling violates energy conservation."** Wrong. The tunneling particle has energy E throughout; in the forbidden region the wave function is an exponentially decaying solution to the Schrödinger equation for a particle *with energy E*. There is no "energy borrowing" from the uncertainty principle — energy is conserved at every point. The pop-science explanation is wrong in detail.

2. **"WKB is just classical mechanics."** No. The 1/√p amplitude is classical; the phase is quantum. The Gamow factor comes from the *quantum mechanical* exponential, not from classical motion in the barrier. The classical particle cannot penetrate at all; WKB gives exponential suppression rather than zero.

3. **"The 1/2 in Bohr–Sommerfeld is a small correction."** For n = 0 (ground state), the Maslov correction (n+1/2 vs n) doubles the energy. It is not small. It is essential.

4. **"WKB is a bad approximation."** It nails the exponential factor exactly; it misses the prefactor by an O(1) factor. For physics that spans 24 decades, the missing O(1) is entirely acceptable. The student should develop the habit of identifying which factor of the answer matters.

5. **"The connection formula just patches two regions together."** The connection formula is derived from the Airy function asymptotics — it is not an ad hoc matching procedure. The Maslov π/4 phase is a theorem, not a convention.

### Worked example 1: WKB tunneling probability through a barrier

Problem: Electron (m = 9.11×10^{-31} kg) with kinetic energy E = 1 eV hits a rectangular barrier V₀ = 5 eV, width L = 5 Å. Compute T_WKB and compare to T_exact.

Step 1: κ = √(2m(V₀-E))/ħ = √(2×9.11×10^{-31}×4×1.6×10^{-19})/(1.055×10^{-34}) ≈ 1.02 Å^{-1}

Step 2: T_WKB = exp(-2κL) = exp(-2×1.02×5) = exp(-10.2) ≈ 3.7×10^{-5}

Step 3: T_exact = [1 + (25)sinh²(10.2/2)/(4×1×4)]^{-1}. sinh(5.1) ≈ 82.0, sinh² ≈ 6724. T_exact ≈ [1 + 25×6724/16]^{-1} ≈ 1/(10507) ≈ 9.5×10^{-5}

Step 4: Ratio T_exact/T_WKB ≈ 2.6. Analytical prediction: 16E(V₀-E)/V₀² = 16×1×4/25 = 2.56. Agreement within rounding.

Key lesson: WKB nails the exponent; misses the prefactor by the analytically predictable factor 16E(V₀-E)/V₀².

### Worked example 2: Bohr–Sommerfeld for the harmonic oscillator

For V = (1/2)mω²x², turning points at x = ±√(2E/mω²). Phase-space orbit at energy E is an ellipse with semi-axes √(2mE)/mω in x and √(2mE) in p. Area = π × (√(2mE)/mω) × √(2mE) = 2πE/ω.

Bohr–Sommerfeld: 2πE/ω = (n+1/2)h → E_n = (n+1/2)ħω. This is the exact quantum result — no approximation. The exactness follows from the fact that for a harmonic oscillator the WKB series terminates at first order (the potential is exactly quadratic; no higher-order terms in the expansion of V near any point).

### Sequencing advice

Develop the ansatz and the validity condition first (one lecture). Do the connection formulas carefully (half a lecture, emphasizing why you need the Airy function — do not just quote the result). Apply to Bohr–Sommerfeld (harmonic oscillator as worked example — exact result is motivating). Then tunneling: first the rectangular barrier where T_exact is available for comparison, then alpha decay as the payoff application. End with one non-nuclear example (STM or stellar fusion) to show the universality.

The cold fusion falsification exercise should appear in the problem set, not the main text — it is a homework-caliber calculation, but an important one. Students should do it with their own numbers.

### Pacing note

The Airy function derivation (connecting the WKB forms across a turning point) is algebraically dense. The recommended strategy: derive it once for a left turning point; state the result for a right turning point by symmetry; then tabulate the four connection formulas (two for each turning point direction) and proceed to applications. The proof that the Maslov phase is π/4 is more important than tracking every algebra step.

---

## F. Library files relevant to this chapter

- `_lib_qmsri-11-the-wkb-approximation-and-tunneling.md` — primary source; contains the WKB ansatz, validity, connection formulas, Bohr–Sommerfeld condition, Gamow factor, alpha decay, STM, stellar fusion, cold fusion, DNA tunneling; all four exercises sets
- `_lib_qmsri-qm-townsend-notes.md` — Townsend notes do NOT contain a WKB chapter; no relevant section found. Townsend Ch. 11 (time-independent perturbations) and Ch. 14 (photons and atoms) are cited in those notes but WKB is absent from the digitized Townsend material.

**External references confirmed in source:**
- Griffiths & Schroeter (2018) §9.1–9.3
- Liboff, *Introductory Quantum Mechanics* §7.7, §7.10
- Gamow (1928), Gurney & Condon (1928, 1929)
- Geiger & Nuttall (1911, 1912)
- Binnig & Rohrer, PRL 49 (1982)
- Fowler & Nordheim, Proc. R. Soc. A 119 (1928)
- Atkinson & Houtermans, Z. Phys. 54 (1929)
- Löwdin, Rev. Mod. Phys. 35, 724 (1963)
- Slocombe et al., Communications Physics 5, 109 (2022)
- Bender & Orszag, *Advanced Mathematical Methods* (1978) Ch. 10

---

## G. Gaps and flags

1. **Langer correction for 3D / radial WKB** — the source material treats only 1D WKB. The radial Schrödinger equation in 3D requires replacing ℓ(ℓ+1) → (ℓ+1/2)² to get the correct semiclassical quantization (the Langer correction). This should appear at minimum as a note in the chapter, possibly as an advanced exercise.

2. **Townsend source missing WKB material** — the digitized Townsend notes (_lib_qmsri-qm-townsend-notes.md) contain no WKB chapter. The primary local source is entirely the _lib_qmsri-11 file. Cross-check against Sakurai §2.4 (WKB) if precision formulas or alternative derivations are needed for the chapter draft.

3. **Tunneling time** — the source material notes the controversy honestly but does not cite the specific attosecond experiments (Eckle et al. 2008, Landsman et al. 2014) by name. These should be cited in the chapter's "still puzzling" or open-questions section.

4. **Resonant tunneling** — the source mentions it briefly in the LLM exercise (double-barrier mode). The chapter draft should include at least one paragraph on resonant tunneling as a quantitative extension of the Gamow framework.

5. **No Sakurai treatment available** — the pantry README notes that the Sakurai .txt file is a corrupted placeholder. Sakurai §2.4 covers WKB with a different emphasis (phase-integral methods, uniform approximation). The author should check Sakurai directly if a second derivation style is desired.
