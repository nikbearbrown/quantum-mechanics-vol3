# Research Notes: Chapter 05 — Time-Dependent Perturbation Theory and Transitions

**Corresponding chapter:** chapters/05-time-dependent-perturbation-theory-and-transitions.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

After this chapter the student can: (1) work in the interaction picture and set up the exact coupled-amplitude equations; (2) apply first-order time-dependent perturbation theory to compute a transition amplitude for a given perturbation H'(t); (3) derive and interpret the sinc-squared resonance lineshape, including its time dependence; (4) write and apply the exact Rabi formula for a driven two-level system; (5) identify where first-order perturbation theory breaks down and explain the physical reason (feedback from the depopulated initial state); (6) state the conditions that bound the regime of validity: Ωt ≪ 1.

---

## A. Conceptual foundations

### The interaction picture

Split the Hamiltonian: H = H₀ + H'(t). The interaction picture (IP) is defined by stripping out the H₀ evolution:

|ψ̃(t)⟩ = exp(iH₀t/ħ)|ψ(t)⟩

The IP state satisfies: iħ ∂_t|ψ̃(t)⟩ = H̃'(t)|ψ̃(t)⟩, where H̃'(t) = exp(iH₀t/ħ)H'(t)exp(-iH₀t/ħ).

The IP disentangles two timescales: the fast H₀ oscillations are rotated away; the IP state evolves only under the perturbation. When H' = 0, the IP state is frozen. This is the correct starting point for all perturbative development.

Expanding in eigenstates of H₀ and projecting onto |f⟩ gives the exact coupled equations:

iħ ċ_f = Σ_n c_n(t) ⟨f|H'(t)|n⟩ exp(iω_{fn}t)

where ω_{fn} = (E_f - E_n)/ħ. Nothing has been approximated yet.

**Key source:** Griffiths & Schroeter §10.1; Sakurai §5.5; Townsend Ch. 14 (cited as primary source in _lib_qmsri-qm-townsend-notes.md). The Townsend notes (Ch. 4 in that compilation) derive the coupled equations explicitly from the substitution |ψ(t)⟩ = Σ_n C_n(t) exp(-iE_n t/ħ)|n⟩.

### First-order transition amplitude

Replace all c_n(t) on the RHS by their initial values (c_i = 1, c_{f≠i} = 0) and integrate:

c_f^{(1)}(t) = (1/iħ)∫₀ᵗ ⟨f|H'(t')|i⟩ exp(iω_{fi}t') dt'

The transition probability at first order:

P_{i→f}(t) = |c_f^{(1)}(t)|² = (1/ħ²)|∫₀ᵗ ⟨f|H'(t')|i⟩ exp(iω_{fi}t') dt'|²

This is the Fourier transform of the matrix element ⟨f|H'(t)|i⟩ evaluated at the Bohr frequency ω_{fi}. "Resonance" is Fourier resonance: the transition is large when the perturbation has a Fourier component at the frequency matching the level spacing.

The Townsend notes (_lib_qmsri-qm-townsend-notes.md, §4.2) also derive the second-order correction and the adiabatic switching (Gell-Mann–Low) formulation, obtaining decay widths and energy shifts from the imaginary and real parts of a complex self-energy. These connect to Chapter 6 (Fermi's golden rule is the imaginary part of the self-energy at second order).

### The resonance lineshape for a sinusoidal perturbation

For H'(t) = V cos(ωt) with V Hermitian, near resonance ω ≈ ω_{fi} (rotating-wave approximation, valid for |V_{fi}|/ħω₀ ≪ 1), the transition probability at first order is:

P_{i→f}(t) = (|V_{fi}|²/ħ²) × sin²[(ω_{fi}-ω)t/2] / [(ω_{fi}-ω)/2]²

This is the sinc-squared lineshape. Its properties:
- Peak height grows as t²
- Width to first zero scales as 2π/t (narrows with time)
- Area under the peak grows as t (consistent with a delta function emerging as t → ∞)
- On-resonance (ω = ω_{fi}): P = |V_{fi}|²t²/(4ħ²) — grows as t²

The t² growth reveals the failure mode: at long enough times, P > 1. This is not a numerical artifact. It is the signature that first-order PT is invalid: the approximation c_i(t) ≈ 1 throughout fails once population has drained out of |i⟩. The exact two-level solution provides the correction.

**Formulas confirmed in both sources:** The sinc² lineshape and its time evolution appear identically in the _lib_qmsri-10 source (§ "The resonance lineshape") and in the Townsend notes (§4.3, "Harmonic Perturbations"), with the same derivation and the same expression for P_{i→f}.

### The exact Rabi solution

For a two-level system {|g⟩, |e⟩} with E_g = 0, E_e = ħω₀, driven by H' = ħΩcos(ωt)(|e⟩⟨g| + |g⟩⟨e|), the rotating-wave approximation reduces the coupled equations to:

ċ_g = -(iΩ/2) exp(-iΔt) c_e
ċ_e = -(iΩ/2) exp(+iΔt) c_g

where Δ = ω - ω₀ is the detuning and Ω = |V_{fi}|/ħ is the Rabi frequency. These two ODEs can be solved exactly. With c_g(0) = 1, c_e(0) = 0:

**Rabi formula:**
P_{g→e}(t) = (Ω²/Ω_gen²) sin²(Ω_gen t/2)

where Ω_gen = √(Ω² + Δ²) is the generalized Rabi frequency.

Special cases:
- On resonance (Δ = 0): P_{g→e}(t) = sin²(Ωt/2). Full population transfer at t = π/Ω (π-pulse). The population oscillates between 0 and 1 — Rabi oscillations.
- Off resonance (Δ ≠ 0): Maximum probability = Ω²/(Ω²+Δ²) < 1. Oscillation frequency Ω_gen > Ω but amplitude suppressed.

The Townsend notes (_lib_qmsri-qm-townsend-notes.md, §4, "two-level system" example) derive the exact Rabi formula by solving the exact coupled ODEs for C₁, C₂ — solving the second-order ODE for C₂ and applying initial conditions. The result matches the _lib_qmsri-10 source. The derivation in the Townsend notes additionally treats spin magnetic resonance as an explicit mapped example, showing how a rotating-field spin-1/2 Hamiltonian maps onto the same two-level structure.

### Where PT fails and why

First-order PT at resonance: P_PT(t) = (Ωt/2)² — a parabola that grows without bound.
Exact Rabi at resonance: P(t) = sin²(Ωt/2) — bounded oscillation.
Agreement: for Ωt ≪ 1, sin²x ≈ x², so the two agree. Divergence: at Ωt = π, exact P = 1, PT predicts (π/2)² ≈ 2.47.

The physical reason: first-order PT fixes c_i(t) ≈ 1 throughout the evolution. Once probability flows into |e⟩, the population in |g⟩ decreases, reducing the rate of further transfer. The Rabi formula captures this feedback (the return journey of the Rabi cycle); PT does not. The validity condition is Ωt ≪ 1 — small coupling times short time.

**Regime identification:** The Townsend notes (§4.3) give a precise statement of validity: 2π/|ω_{fi}| ≲ t ≪ ħ/|V_{fi}|. The lower bound ensures the sinc-squared function has sharpened enough to approximate a delta function (relevant for Ch. 6 Fermi's golden rule); the upper bound keeps PT valid.

---

## B. Domain examples and cases

### Rabi's original molecular beam experiment (1938)

Isidor Rabi's Columbia group (January 1938) passed LiCl molecules through three magnets: a spin-state selector, an oscillating RF interaction region, and an analyzer. At the resonance frequency, the beam intensity dropped sharply — spins had been flipped. The RF frequency at which this occurs is ω₀ = E_spin-up - E_spin-down /ħ, i.e., the Larmor frequency. The precision of the resonance line (the narrow dip) depends on running the interaction long enough to complete a π-pulse — at which point PT has already failed by a factor of 2.47. The physics works precisely because the exact Rabi formula, not PT, governs the transition.

**Nobel Prize:** Rabi, 1944. Reference: Rabi et al., *Physical Review* 55, 526 (1939).

### NMR and MRI

Nuclear magnetic resonance uses exactly the same Rabi formula for nuclear spin-1/2 in a static B₀ field plus a rotating B₁ field. The π/2 pulse (Ωt = π/2) creates a superposition 50/50 between |↑⟩ and |↓⟩; the π-pulse inverts population. T₁ (longitudinal relaxation) and T₂ (transverse dephasing) lifetimes are measured by comparing Rabi oscillation decay to the golden-rule prediction for irreversible decay. MRI signal intensity is fundamentally governed by these rates.

### Superconducting qubits (transmon)

A transmon qubit is a two-level system (ground and first excited state of the Josephson cosine potential) driven by a microwave pulse through a capacitive coupler. The Rabi formula directly governs single-qubit gates: a π-pulse is an X gate (population inversion), a π/2-pulse is a Hadamard analog. The Rabi frequency Ω/(2π) ~ 10–100 MHz sets the gate speed. Coherence times T₂ ~ 100 μs impose the condition Ωt ≪ 1 for the gate (NOT for the PT approximation — the gate works because the exact Rabi formula is valid; the transmon is deep in the Rabi-oscillation regime, not the PT regime).

### Kicking a harmonic oscillator (from Townsend notes)

The Townsend notes (§4, "Kicking an oscillator") work the example: a harmonic oscillator in its ground state hit by a Gaussian pulse V(t) = -eE x̂ exp(-t²/τ²). The transition probability to |1⟩ is:

|c_f(∞)|² = (e²E²/ħ²)(ħ/2mω)πτ² exp(-ω²τ²/2)

Two limits: (a) τ → 0 (sudden kick): the Gaussian broadens in frequency space, P → 0 (the system doesn't have time to absorb at ω₀); (b) τ → ∞ (quasi-static): the exponential factor exp(-ω²τ²/2) → 0, and the transition is also suppressed — the adiabatic limit. Maximum transition probability occurs at intermediate τ ~ 1/ω₀. This example concretely demonstrates how the Fourier-transform interpretation of the transition amplitude works.

### Beta decay / sudden approximation

When a neutron in the nucleus undergoes beta decay (becoming a proton), the nuclear charge jumps instantaneously from Z to Z+1. The 1s electron's wave function does not change (no time to respond — sudden approximation), but it is now in a state that is not an eigenstate of the Z+1 Coulomb potential. The probability of finding it in the new ground state (1s of He-like ion if Z → 2) is |⟨ψ_{1s}^{Z+1}|ψ_{1s}^{Z}⟩|² — computable from the hydrogen wave functions. This is the Townsend notes §4.1 example.

### Landau–Zener (from Townsend notes, Ch. 7)

A spin-1/2 with a fixed transverse coupling V and a linearly ramping longitudinal field αt has total Hamiltonian H = [[αt, V],[V, -αt]]. The exact non-perturbative result for the diabatic (non-adiabatic) transition probability is:

P_{LZ} = exp(-πV²/α)

This is the Landau–Zener formula (Landau 1932, Zener 1932). The Townsend notes derive it (§, "Landau–Zener tunnelling") via the adiabatic expansion and evaluation of a contour integral. Features: (1) when α/V² ≪ 1 (slow ramp), P_LZ → 0 — adiabatic following; (2) when α/V² ≫ 1 (fast ramp), P_LZ → 1 — the system stays on the diabatic (non-adiabatic) state. The crossover is at V²/α ~ 1. Landau–Zener is explicitly non-perturbative; perturbation theory cannot access it because |αt| can be made arbitrarily large.

**Connection to this chapter:** LZ is the closest exact analog of the Rabi solution for a sweeping (rather than oscillating) perturbation. It belongs in this chapter or as a bridge to Ch. 6 (adiabatic vs. resonant regimes).

**Reference:** Landau, *Phys. Z. Sowjetunion* 2, 46 (1932); Zener, *Proc. R. Soc. Lond. A* 137, 696 (1932).

---

## C. Connections and dependencies

**Prerequisite material:**
- Stationary perturbation theory (Ch. 3): provides the unperturbed eigenstates and energies needed as inputs to time-dependent PT
- Two-level systems and spin dynamics (Vol. 1 or 2): The Rabi formula is most naturally first seen in the spin-1/2 context
- Fourier analysis: the transition amplitude is literally a Fourier transform; students who can read a Fourier transform can read the resonance lineshape

**Internal dependencies:**
- This chapter is a prerequisite for Ch. 6 (Fermi's golden rule = long-time limit of the sinc² lineshape summed over a continuum)
- Landau–Zener connects to the adiabatic theorem (discussed in Townsend notes §4.4) and to Berry's phase (§4.5); these are either in Ch. 5 or a separate adiabatic-methods chapter

**Forward connections:**
- Bloch sphere: the two-level Rabi solution maps the state to a point on the Bloch sphere; the Rabi oscillation is rotation around the x- or y-axis; the Bloch-sphere picture is standard in quantum information and should appear here or in a sidebar
- Dressed states: when Ω ~ Δ, the eigenstates of the RWA Hamiltonian (dressed states) are the natural basis. Dressed-state energies are ±ħΩ_gen/2; avoided crossing at resonance. This appears in quantum optics (Jaynes–Cummings model).
- The sudden and adiabatic approximations (Townsend notes §4.1, §4.4) are the limiting cases of time-dependent dynamics at the two ends of the clock; they bookend the resonant middle ground that is the main subject of this chapter.

---

## D. Current state of the field

**Optimal control and shaped pulses:** In NMR, quantum computing, and AMO physics, "pulse shaping" replaces simple π-pulses with amplitude-modulated waveforms optimized to drive a specific unitary in minimum time (GRAPE algorithm, optimal control theory). The Rabi formula gives the on-resonance result for constant Ω; modern experiments work in the Rabi-frequency space designed by optimal control. Transition from TDPT to exact Rabi to optimal control is the progression.

**Floquet theory:** When H'(t) is periodic in time, the exact treatment uses Floquet states (quasi-energy eigenstates of the time-periodic problem), not TDPT. Floquet theory is the frequency-domain analog of Bloch's theorem. In strongly driven systems (laser-dressed atoms, Floquet topological matter), Floquet states rather than bare perturbative levels are the correct zeroth-order starting point.

**Chirped rapid adiabatic passage (RAP):** Sweeping the drive frequency across resonance (chirped pulse) while keeping |Ω/α| large achieves robust population inversion via the adiabatic theorem, not the Rabi π-pulse. RAP is more robust to Ω inhomogeneity than a fixed-frequency π-pulse. It is a direct practical application of the Landau–Zener transition probability at the swept-resonance condition.

---

## E. Teaching considerations

### High-value misconceptions to address

1. **"The transition probability grows forever."** No — in a two-level system, it saturates and oscillates (Rabi formula). The t² growth of PT is the diagnostic of PT breakdown, not a physical prediction.

2. **"Resonance means the transition probability equals 1."** At resonance, P reaches 1 at t = π/Ω. Off resonance, the maximum is Ω²/(Ω²+Δ²) < 1. Resonance sharpens and maximizes the oscillation; it does not guarantee unit transfer at arbitrary time.

3. **"The rotating-wave approximation is always valid."** The RWA drops the counter-rotating term (frequency 2ω). This is valid when Ω ≪ ω₀ (weak drive, near resonance). In ultra-strong coupling (Ω ~ ω₀, realizable in circuit QED), the counter-rotating term matters (Bloch–Siegert shift, ~ Ω²/ω₀).

4. **"First-order PT fails because the approximation is 'rough'."** It fails for a precise physical reason: it assumes the initial state is undepleted. The failure criterion is Ωt ~ 1, not "coupling too strong in an abstract sense." Students should be able to state when PT will fail before computing.

5. **"The interaction picture is just a gauge transformation."** Technically there is a similarity, but pedagogically the IP is best understood as a rotation of the state vector to remove the fast H₀ oscillations, leaving only the slow perturbation-induced dynamics. Calling it a gauge transformation before the student understands gauge theory is confusing.

### Worked example: The Rabi formula and on-resonance oscillation

Problem: A two-level atom (ħω₀ = 2 eV) is driven by a resonant laser (ω = ω₀). The coupling is ħΩ = 0.01 eV. The atom starts in the ground state. (a) At what time does it first reach the excited state with probability 1? (b) At what time does first-order PT predict P = 1, and what is the exact probability at that time?

(a) On resonance: P = sin²(Ωt/2) = 1 at Ωt/2 = π/2, so t_π = π/Ω.
ħΩ = 0.01 eV → Ω = 0.01/(1.055×10⁻³⁴ × 6.24×10¹⁸) s⁻¹ ≈ 1.52×10¹³ rad/s
t_π = π/Ω ≈ 2.07×10⁻¹³ s ≈ 0.21 ps

(b) PT: P_PT = (Ωt/2)² = 1 when Ωt/2 = 1 → t_PT = 2/Ω ≈ 1.32×10⁻¹³ s.
At t = t_PT: exact P = sin²(Ωt_PT/2) = sin²(1) ≈ 0.708. PT predicts 1.00; exact answer is 0.71.

Moral: At the moment PT predicts unit transfer, the exact system has transferred only 71% of the population. The discrepancy grows rapidly after this.

### Worked example: Sudden approximation — kicked oscillator

An oscillator (m, ω) in |n=0⟩ receives a short kick V(t) = Fx δ(t). The first-order transition amplitude to |1⟩:

c_1^{(1)}(∞) = (1/iħ)⟨1|Fx̂|0⟩ × 1 (time integral of δ(t)×exp(iωt) at t=0 gives 1)
= (F/iħ)√(ħ/2mω)

P_{0→1} = F²/(2mωħ)

Check: small for F² ≪ 2mωħ — the validity condition for PT.

### Sequencing advice

Open with Rabi's 1938 experiment as the motivating physical picture (15 minutes of history and context). Then derive the interaction picture (one full derivation, not just stated). Derive the first-order amplitude; interpret it as a Fourier transform; derive the sinc² lineshape. Only then introduce the two-level exact Rabi solution — derive it by solving the ODEs, not by quoting the result. Compare PT and exact on the same plot (essential visualization). Close with the regime of validity.

Reserve the sudden approximation (§4.1 in Townsend notes) and adiabatic theorem (§4.4) for either this chapter's end or a separate chapter on adiabatic methods. The Landau–Zener result can appear as a worked example or as a capstone problem.

---

## F. Library files relevant to this chapter

- `_lib_qmsri-10-time-dependent-perturbation-theory-and-transitions.md` — primary source; contains the interaction picture, sinc-squared resonance lineshape, PT breakdown analysis, exact Rabi formula derivation and plots, selection rules, spontaneous emission, and the "still puzzling" section on the logical seam in the golden rule derivation
- `_lib_qmsri-qm-townsend-notes.md` — Ch. 4 (§1588–2100) provides a parallel independent derivation of: coupled amplitude equations, first-order PT, the two-level Rabi formula (exact), sudden approximation (beta decay example), adiabatic theorem, Berry's phase; also the Landau–Zener solution (§3154–3270)

**Key external references confirmed in sources:**
- Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed., Ch. 14 (TDPT) and Ch. 4 (two-level dynamics, Example 4.2)
- Sakurai & Napolitano, *Modern Quantum Mechanics*, 3rd ed., the "Approximation Methods" chapter (TDPT, sudden, adiabatic, Berry's phase)
- Griffiths & Schroeter, *Introduction to Quantum Mechanics*, 3rd ed., "Time-Dependent Perturbation Theory" and "The Adiabatic Approximation" chapters
- Cohen-Tannoudji, *Quantum Mechanics*, Vol. II, Ch. XIII
- Rabi et al., *Physical Review* 55, 526 (1939)
- Landau, *Phys. Z. Sowjetunion* 2, 46 (1932); Zener, *Proc. R. Soc. Lond. A* 137, 696 (1932)

---

## G. Gaps and flags

1. **Landau–Zener placement:** The Townsend notes place the Landau–Zener derivation in what is labeled "Chapter 7" (fine structure / spin-orbit chapter), not in the TDPT chapter. This is pedagogically awkward — LZ is naturally a TDPT result. The chapter draft should either include LZ here or add an explicit forward reference.

2. **Bloch sphere visualization:** Neither source file includes the Bloch-sphere derivation as a core element (it appears only in the LLM exercise extension prompt). The chapter draft should include a Bloch-sphere section — it is the standard geometric picture for the Rabi oscillation and is expected by any student who will work in quantum information.

3. **Rotating-wave approximation validity** is stated informally in both sources but not quantified. The Bloch–Siegert shift (Ω²/4ω₀ correction from the counter-rotating term) should appear as at least a note or problem. It is measurable in circuit QED systems.

4. **Berry's phase:** Both source files cover Berry's phase (§4.5 in Townsend notes; §4.5 in _lib_qmsri-10 would be in the next section not digitized). Berry's phase belongs in this chapter or in an adiabatic-methods chapter; if the volume does not have a dedicated adiabatic chapter, it should be here after the Landau–Zener section.

5. **Second-order perturbation theory** is present in the Townsend notes (§4.2, decay width and energy shift from Σ|V_{mi}|²/(E_i-E_m+iε)) but absent from the _lib_qmsri-10 source. The chapter should cite this — it is the mechanism behind radiative corrections, Lamb shift (classically), and quantum decoherence via bath coupling.

6. **Source note:** The _lib_qmsri-10 source explicitly warns that "The spontaneous emission wall" section requires quantum electrodynamics for a complete derivation — this material is correctly deferred to Ch. 6 (radiation and Fermi's golden rule). Do not attempt to derive the Einstein A-coefficient semiclassically in Ch. 5; cite it and move on.
