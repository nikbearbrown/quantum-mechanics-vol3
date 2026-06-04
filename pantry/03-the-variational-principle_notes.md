# Research Notes: Chapter 03 — The Variational Principle

**Corresponding chapter:** chapters/03-the-variational-principle.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to: state and prove the variational theorem (⟨H⟩ ≥ E₀ for any normalized trial state); choose a parameterized trial function; minimize ⟨H⟩ over the parameters to obtain an upper bound on E₀; apply this to the helium atom (effective nuclear charge Z̃ = Z − 5/16, result ≈ −77.5 eV vs. experimental −78.98 eV); apply to the H₂⁺ ion (LCAO bonding and antibonding orbitals, overlap integral, variational equilibrium bond length); recognize the limits of the method (upper bound only; excited-state extension requires orthogonality constraint); and connect the multi-parameter limit to the Rayleigh–Ritz generalized eigenvalue problem.

---

## A. Conceptual Foundations

### A1. The variational theorem: proof and meaning

**Statement:** For any normalized trial state |ψ⟩, ⟨ψ|H|ψ⟩ ≥ E₀, where E₀ is the true ground-state energy.

**Proof (from Townsend Ch. 6 / Feiguin notes):** Expand |ψ⟩ in the exact eigenbasis of H: |ψ⟩ = Σ_n ψ_n |n⟩. Then ⟨H⟩ = Σ_n |ψ_n|² E_n ≥ E₀ Σ_n |ψ_n|² = E₀, since each E_n ≥ E₀ and Σ|ψ_n|² = 1. Equality holds if and only if ψ_n = 0 for all n > 0, i.e., the trial state is the exact ground state.

**Physical meaning:** You cannot accidentally go below the ground-state energy by guessing. The worst a trial function can do is sit too high. The game is to push ⟨H⟩ as low as possible; the lower you go, the closer you are to the truth.

**Common misconception:** Students often think a lower variational energy always means a better wave function. The energy is an upper bound on E₀, so a lower ⟨H⟩ is a tighter bound — which is better in the sense of being closer to the exact answer. But the wave function that achieves the minimum within a restricted class of trial states need not resemble the true ground state everywhere; it may be a poor approximation to the wave function even when the energy is close.

**Worked example (Gaussian trial for 1D harmonic oscillator):** ψ(x) = Ae^{−bx²}. Compute ⟨T⟩ = ℏ²b/2m, ⟨V⟩ = mω²/8b. Minimize over b: ∂⟨H⟩/∂b = 0 → b = mω/2ℏ. Result: E_V = ℏω/2 = E₀ exact. The trial function is exact because the true ground state happens to be Gaussian. This is a useful pedagogical point: the variational method gives the exact answer when the trial family contains the exact solution.

**Sources:** `_lib_qmsri-qm-townsend-notes.md` lines 2570–2630 (§6 variational method: proof of E_V ≥ E₀; Gaussian harmonic oscillator example; delta-function potential example); Griffiths & Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., Ch. 7 ("The Variational Principle") — the primary undergraduate textbook treatment; UCSD Physics 130A notes, "The Variational Principle (Rayleigh-Ritz Approximation)" https://quantummechanics.ucsd.edu/ph130a/130_notes/node375.html.

---

### A2. Trial functions with parameters: the Rayleigh–Ritz method

The general procedure: choose a trial function ψ(r; {α_i}) depending on N variational parameters {α_i}. Compute E_V({α_i}) = ⟨ψ|H|ψ⟩/⟨ψ|ψ⟩. Set ∂E_V/∂α_i = 0 for each i. Solve the resulting system of equations to find the optimal parameters and the minimum variational energy.

When the trial function is a linear combination of basis states — ψ = Σ_n c_n φ_n — the minimization conditions become a generalized eigenvalue problem: H·c = E·S·c, where H_{nm} = ⟨φ_n|H|φ_m⟩ and S_{nm} = ⟨φ_n|φ_m⟩ is the overlap matrix. When the basis is orthonormal, S = 1 and this reduces to the standard eigenvalue problem.

**Common misconception:** Students often think the variational method is less systematic than perturbation theory. In practice for computational purposes it is more general: perturbation theory requires a small parameter; the variational method does not. It is the foundation of virtually all of quantum chemistry (Hartree–Fock, configuration interaction, coupled cluster) and of density-functional theory.

**Worked example (H atom with Gaussian basis, Townsend notes §6):** Use four Gaussians χ_p(r) = e^{−α_p r²} with exponents α_1 = 13.00773, α_2 = 1.962079, α_3 = 0.444529, α_4 = 0.121949. Analytic formulas exist for S_{pq} = (π/(α_p + α_q))^{3/2}, T_{pq}, V_{pq}. Numerical solution of the 4×4 generalized eigenvalue problem gives E_V = −0.499278 Hartree; exact is −0.5 Hartree. Error: 0.14%. Five lines of matrix algebra, no hand-waving.

**Sources:** `_lib_qmsri-qm-townsend-notes.md` lines 2582–2609 (general variational framework and minimization condition), lines 2780–2886 (generalized eigenvalue problem, overlap matrix, H-atom Gaussian basis example with explicit α values and results); UCSD 130A notes https://quantummechanics.ucsd.edu/ph130a/130_notes/node375.html; NumberAnalytics, "Mastering Variational Principle in Quantum Mechanics" https://www.numberanalytics.com/blog/variational-principle-quantum-mechanics-atomic-physics.

---

### A3. The helium atom: effective nuclear charge and electron shielding

**Setup:** Helium has Z = 2, two electrons, Hamiltonian H = p₁²/2m + p₂²/2m − Ze²/r₁ − Ze²/r₂ + e²/|r₁ − r₂|. The electron-electron repulsion e²/|r₁ − r₂| prevents an exact solution.

**Trial function:** ψ(r₁, r₂) = ψ₁s(Z̃; r₁) ψ₁s(Z̃; r₂), where ψ₁s(Z̃; r) = (1/√π)(Z̃/a₀)^{3/2} e^{−Z̃r/a₀} is a hydrogen-like 1s orbital with an adjustable effective charge Z̃. This encodes the physical idea that each electron partly screens the nuclear charge from the other.

**Calculation (Feiguin / Townsend §12.31):** Regroup H by adding and subtracting Z̃e²/r terms. Then:

⟨H⟩ = ½ m_e c² α² [2Z̃² − 4ZZ̃ + (5/4)Z̃] = ½ m_e c² α² [2Z̃² − 4ZZ̃ + (5/4)Z̃]

Minimize ∂⟨H⟩/∂Z̃ = 0 → Z̃ = Z − 5/16 = 2 − 5/16 = 27/16 ≈ 1.6875.

Result: E_V = −½ m_e c² α² × 2(27/16)² ≈ −77.5 eV (Feiguin notes give −77.4 eV; Griffiths gives −77.5 eV; small differences arise from constant choices).

**Experimental value:** −78.98 eV. Error: about 2%. Compare to first-order perturbation theory (treating e²/|r₁−r₂| as a perturbation with Z̃ = Z = 2): gives −74.8 eV, error ~5%. The variational result is significantly better.

**Physical interpretation of Z̃:** The optimal Z̃ = 27/16 < 2 means each electron effectively sees a nuclear charge of 1.6875 instead of 2 — the other electron screens 5/16 of a proton charge. This is the concept of electron shielding, which carries over to all of atomic physics and chemistry.

**Common misconception:** Students often think the variational energy is the exact ground-state energy. It is not — it is a guaranteed upper bound, and the 2% error for helium is real. Convergence toward the exact answer requires more flexible trial functions. With a Hylleraas-type trial that depends on |r₁ − r₂| explicitly, the ground state can be computed to 11 significant figures.

**Sources:** `_lib_qmsri-qm-townsend-notes.md` lines 2648–2672 (complete helium variational calculation, regrouped Hamiltonian, the minimization Z̃ = Z − 5/16, numerical result −77.4 eV, comparison to measured −78.8 eV); UCSD 130A notes, "Variational Helium Ground State Energy" https://quantummechanics.ucsd.edu/ph130a/130_notes/node376.html (pedagogically clear, matches the Feiguin calculation); Physics LibreTexts (Fitzpatrick), "13.2: Helium Atom" https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/13:_Variational_Methods/13.02:_Helium_Atom (independent presentation, same result); Griffiths & Schroeter §7.2 (the standard undergraduate reference).

---

### A4. The H₂⁺ molecular ion: LCAO and the chemical bond

**Setup:** One electron, two protons separated by distance R. The Hamiltonian is H = p²/2m_e − e²/|r − R/2| − e²/|r + R/2| + e²/R. The electron-nucleus and proton-proton interactions compete; binding occurs when the electronic energy gain exceeds the proton-proton repulsion.

**Trial function (LCAO):** Symmetry demands that the ground state be symmetric or antisymmetric under the exchange of the two protons. Symmetric: |+⟩ = (|A⟩ + |B⟩)/√(2 + 2S_{AB}); Antisymmetric: |−⟩ = (|A⟩ − |B⟩)/√(2 − 2S_{AB}), where |A⟩ and |B⟩ are hydrogen 1s orbitals on proton A and B, and S_{AB} = ⟨A|B⟩ is the overlap integral.

**Variational energies:** E± = (H_{AA} ± H_{AB})/(1 ± S_{AB}), where H_{AA} = E₁ − ⟨A|e²/|r+R/2||A⟩ + e²/R and H_{AB} = E₁ S_{AB} − ⟨A|e²/|r+R/2||B⟩ + (e²/R)S_{AB}.

Only the bonding orbital |+⟩ has a minimum in E+ as a function of R. The minimum occurs at R ≈ 1.3 Å (exact: 1.06 Å). The LCAO approximation overestimates R and underestimates the binding energy because the trial function does not account for the distortion of the atomic orbitals as the protons approach. Including additional basis functions or a variational scale factor on the orbital exponent improves the result.

**Common misconception:** Students sometimes think the binding comes from the attractive proton-electron-proton "covalent" picture alone. In reality the kinetic energy also decreases in the bonding state (the wave function is smoother when spread across both nuclei), and this kinetic energy reduction is partially responsible for the bond. The full story requires inspecting both the kinetic and potential terms of H_{AA} and H_{AB}.

**Worked example (simulation target):** Plot E+ and E− as functions of R. E+ has a minimum (bonding); E− is purely repulsive (antibonding). The overlap integral S_{AB} = e^{−R/a₀}(1 + R/a₀ + R²/3a₀²) (exact formula). This is a natural simulation exercise: students can vary R and watch the two curves evolve.

**Sources:** `_lib_qmsri-qm-townsend-notes.md` lines 2682–2726 (full H₂⁺ treatment: trial functions, H_{AA}, H_{AB}, overlap integral, bonding/antibonding characterization, LCAO plot description); Physics LibreTexts (Fitzpatrick), "13.3: Hydrogen Molecule Ion" https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/13:_Variational_Methods/13.03:_Hydrogen_Molecule_Ion; UT Austin QM notes, "Hydrogen Molecule Ion" https://farside.ph.utexas.edu/teaching/qmech/Quantum/node129.html (full quantitative treatment with overlap integral formulas).

---

### A5. Limits of the variational method

The variational principle provides only an **upper bound**. It gives no direct information about:
- How close the trial energy is to E₀ (the bound can be tight or loose depending on the trial function quality).
- Excited-state energies, except through the orthogonality constraint: if |ψ⟩ is constrained to be orthogonal to the exact ground state (⟨ψ|ψ₀⟩ = 0), then ⟨H⟩ ≥ E₁. In practice this requires knowing |ψ₀⟩, which you typically do not. A practical workaround: confine the trial function to a symmetry sector different from the ground state (e.g., odd parity when the ground state is even).
- Quality of the trial wave function away from the energy minimum — a wave function can give a good energy but be wrong in shape.

**Common misconception:** Students often believe that if ⟨H⟩ is close to the known E₀, the wave function must be accurate. This is false. The energy is a bilinear quantity in ψ; the wave function enters through |ψ|², which can be wrong by first-order errors while the energy error is only second order. Wave functions in variational calculations are less accurate than energies.

**Sources:** `_lib_qmsri-qm-townsend-notes.md` lines 2674–2680 (excited-state extension with orthogonality constraint); Griffiths §7.3 (the most clearly written undergraduate discussion of the limits); Shankar, *Principles of Quantum Mechanics*, Ch. 16 (more rigorous treatment of the excited-state problem and the min-max theorem).

---

## B. Domain Examples and Cases

**B1. Harmonic oscillator with Gaussian trial** — exact, clean introduction to the minimization procedure. Teaches that the method is exact when the trial family contains the true solution.

**B2. Delta-function potential** — H = −(ℏ²/2m)d²/dx² − αδ(x). Gaussian trial gives E_V = −mα²/(πℏ²) vs. exact E₀ = −mα²/(2ℏ²). Shows a case where the variational bound is not tight and the trial family is restricted.

**B3. Helium atom with Z̃ trial** — the textbook showcase for a realistic multi-electron atom.

**B4. H₂⁺ molecular ion** — direct application to chemical bonding; motivates molecular orbital theory and LCAO.

**B5. Hydrogen atom with Gaussian basis** — illustrates the generalized eigenvalue problem; shows that systematically improving the basis (more Gaussians) converges to the exact result.

**B6. Infinite square well with polynomial basis (Feiguin notes §6.4)** — pedagogical illustration of the generalized eigenvalue problem with an explicit 2×2 secular determinant calculation.

---

## C. Connections and Dependencies

- **Prerequisite:** Expectation values; hydrogen atom wave functions and 1s orbital; basic linear algebra (eigenvalue problems). No PT required — the variational method is logically independent.
- **Relation to PT:** Perturbation theory requires a small parameter; the variational method does not. For helium, first-order PT (treating e²/|r₁−r₂| as a perturbation) gives −74.8 eV; the variational estimate gives −77.5 eV. The variational approach wins when there is no small parameter.
- **Leads to quantum chemistry:** Hartree–Fock theory is the variational method applied to Slater determinant trial states. Configuration interaction (CI) extends this by allowing multiple determinants. Density-functional theory (DFT) reformulates the variational problem in terms of electron density.
- **Connects to simulation (Ch. 1):** The anharmonic oscillator exact energy obtained by numerical diagonalization in a truncated HO basis (Ch. 1 simulation) is effectively a variational calculation in a finite basis — the same idea as the generalized eigenvalue problem.
- **Min-max theorem:** The k-th variational eigenvalue from a trial space is an upper bound on the k-th exact eigenvalue (for a complete enough trial space). This is the formal foundation for CI in quantum chemistry.

---

## D. Current State of the Field

- **Quantum chemistry:** The variational method, combined with systematic basis set expansion, underlies Hartree–Fock (1930s), MP2/CCSD/CCSD(T) (1960s–1980s), and modern DFT (Kohn–Sham, 1965). These methods routinely achieve sub-kcal/mol accuracy for molecular energies.
- **Hylleraas wave functions for helium:** Egil Hylleraas (1928) introduced trial functions that depend on the inter-electron distance |r₁ − r₂| explicitly. With a few dozen terms the helium ground-state energy is known to 11 significant figures. This is among the most precisely computed quantities in atomic physics.
- **Quantum Monte Carlo:** Variational Monte Carlo (VMC) evaluates ⟨H⟩ stochastically for highly flexible trial wave functions in many-body systems (atoms, molecules, solids) where exact diagonalization is intractable. Diffusion Monte Carlo (DMC) uses the variational result as a starting point and then samples the exact ground state via imaginary-time evolution.
- **Machine-learned wave functions:** FermiNet (DeepMind, 2020) and PauliNet use neural networks as variational trial functions for molecular systems, achieving accuracy competitive with CCSD(T) without basis set truncation. This is an active research frontier.

---

## E. Teaching Considerations

- **The variational method should feel like an optimization problem** — which is familiar to students from calculus. Frame it as: you have a function E_V(α), and you want its minimum. This is more accessible than the perturbation expansion framework.
- **The proof of E_V ≥ E₀ is short and should be done in full** (half a page). Students who see the proof understand why the method works and do not treat it as a black box.
- **The helium atom calculation is the flagship worked example.** Walk through the Hamiltonian regrouping trick (adding and subtracting Z̃e²/r terms) carefully — this is where many students get lost. The key is recognizing that the trial state is the exact eigenstate of the regrouped H₀(Z̃), so ⟨H₀(Z̃)⟩ is just twice the hydrogen ground-state energy at effective charge Z̃.
- **Simulation connection:** The simulation for this chapter should allow students to vary Z̃ continuously and watch E_V(Z̃) minimize at Z̃ = 27/16. This makes the optimization visual.
- **Excited states via symmetry sectors** — practically important and often omitted in introductory treatments. Show the example: for helium, the first excited state lives in the spin-triplet sector (due to antisymmetry), and a trial state in that sector gives an upper bound on E₁.
- **The generalized eigenvalue problem** should be presented as the natural limit where you have many parameters. Show the 2×2 case explicitly (as in the Feiguin notes) before writing the general matrix equation.

---

## F. Library Files Relevant to This Chapter

- `/pantry/_lib_qmsri-qm-townsend-notes.md` — **Primary.** Chapter 6, "The Variational Method" (lines 2558–2902): complete treatment including the proof of E_V ≥ E₀, Gaussian HO and delta-function examples, full helium calculation with Z̃ = 27/16 and numerical result −77.4 eV, H₂⁺ LCAO treatment, H₂ molecule (MO and valence-bond pictures), and the generalized eigenvalue problem with the polynomial basis and Gaussian H-atom examples. All equations match published textbook treatments.

No local source specifically covers this chapter as a standalone draft (unlike Ch. 1 and Ch. 2, which have `_lib_qmsri-09`). The Feiguin–Townsend notes are the primary local resource.

**Web sources consulted:**
- UCSD 130A, "The Variational Principle (Rayleigh-Ritz Approximation)" https://quantummechanics.ucsd.edu/ph130a/130_notes/node375.html
- UCSD 130A, "Variational Helium Ground State Energy" https://quantummechanics.ucsd.edu/ph130a/130_notes/node376.html
- Physics LibreTexts (Fitzpatrick), "13.2: Helium Atom" https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/13:_Variational_Methods/13.02:_Helium_Atom
- Physics LibreTexts (Fitzpatrick), "13.3: Hydrogen Molecule Ion" https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/13:_Variational_Methods/13.03:_Hydrogen_Molecule_Ion
- UT Austin, "Hydrogen Molecule Ion" https://farside.ph.utexas.edu/teaching/qmech/Quantum/node129.html
- University of Manchester PHYS30201, "Variational methods: the helium atom" https://www.theory.physics.manchester.ac.uk/~judith/AQMI/PHYS30201se7.xhtml
- Grokipedia / Wikipedia, "Variational method (quantum mechanics)" https://en.wikipedia.org/wiki/Variational_method_(quantum_mechanics)

---

## G. Gaps and Flags

- **No local lib file for Ch. 3.** Unlike Chs. 1 and 2, there is no `_lib_qmsri-10-variational-principle.md` or equivalent standalone draft. The chapter must be built primarily from the Feiguin–Townsend notes (Ch. 6) plus web research. A future pantry addition of a dedicated variational-principle library file would be valuable.
- **Exact helium energy and convergence:** The chapter gives −77.5 eV (variational, one parameter) vs. −78.98 eV (experimental). It should note that with a two-parameter trial (Z̃ and an s-wave angular correlation) the result improves to −77.8 eV, and with Hylleraas functions it converges to the exact value. Quantitative convergence data should be included.
- **H₂⁺ numerical values:** The LCAO equilibrium bond length and binding energy from the variational calculation should be stated explicitly: R_eq ≈ 1.3 Å (LCAO) vs. 1.06 Å (exact); binding energy ≈ 1.77 eV (LCAO) vs. 2.65 eV (exact). These numbers motivate students to see why more flexible trial functions are needed.
- **Thomas–Fermi and DFT connection:** The variational principle over electron density (rather than the wave function) leads to the Thomas–Fermi model and ultimately DFT. This connection deserves a brief mention as a contemporary extension.
- **Simulation design needed:** A simulation for this chapter (analogous to the `09-perturbation-explorer.html` for Chs. 1–2) has not been specified. A recommended design: Mode A — helium E_V(Z̃) vs. Z̃ curve with a slider; Mode B — H₂⁺ E+(R) and E−(R) vs. R curves with the equilibrium bond length marker. Both modes show the variational parameter search visually.
- **Connection to numerical diagonalization:** The Gaussian-basis H-atom example in the Feiguin notes (§6.4) directly bridges to the finite-basis diagonalization of Ch. 1 and to computational quantum chemistry. This connection should be made explicit.

**Strongest new source for Ch. 3:** UCSD Physics 130A, "Variational Helium Ground State Energy" (https://quantummechanics.ucsd.edu/ph130a/130_notes/node376.html) — clean, complete calculation with the Z̃ minimization, the numerical result, and a comparison to experiment. Directly usable as a model for the chapter's worked example.
