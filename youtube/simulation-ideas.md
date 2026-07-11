# Simulation Ideas — quantum-mechanics-vol3

Medhavy-register "Claude Code + Manim" workflow reels.

---

## Sim-01 — WKB Tunneling: STM Current Drops 7× per Ångström
- Source: `quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: T ≈ e^(−2κd), κ=√(2mφ)/ℏ; for φ=4 eV, κ≈1.02 Å⁻¹ → factor of e²≈7.4 per Å
- Concrete numbers: φ=4 eV, κ=1.02 Å⁻¹; at d=5 Å current I₀; at d=6 Å current I₀/7.4; at d=4 Å current 7.4·I₀
- Visual artifact: wavefunction decay through vacuum gap; semi-log plot of I vs d showing linear slope −2κ
- Two testable predictions: P1: slope of ln(I) vs d equals exactly −2κ = −2.04 Å⁻¹; P2: reducing gap by 1 Å multiplies current by e^2 ≈ 7.4 (Binnig-Rohrer rule)
- Sim slug: medhavy-vol3-stm-tunneling
- Note: CROSS-REFERENCE — vox-stm-exponential is an explainer in quantum-mechanics-a-companion-guide. This is the simulation workflow reel showing Claude Code generating the scene; build it.

---

## Sim-02 — Fermi's Golden Rule: Transition Rate vs Perturbation Strength
- Source: `quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: Γ = 2π/ℏ |⟨f|V̂|i⟩|² ρ(E_f); rate proportional to |matrix element|² and density of states
- Concrete numbers: hydrogen 2p→1s: A coefficient = 6.27×10⁸ s⁻¹ (lifetime ≈ 1.6 ns); Lyman-α photon energy = 10.2 eV = hc/121.6 nm
- Visual artifact: energy levels with transition arrow; bar graph of rate vs coupling strength showing quadratic growth; log-log slope = 2
- Two testable predictions: P1: rate scales as |⟨f|V̂|i⟩|² (doubling the coupling quadruples the rate); P2: 2p→1s rate = 6.27×10⁸ s⁻¹ (matches NIST value)
- Sim slug: medhavy-vol3-golden-rule

---

## Sim-03 — Variational Principle: Every Guess Is Too High
- Source: `quantum-mechanics-vol3/chapters/03-the-variational-principle.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: ⟨ψ_trial|Ĥ|ψ_trial⟩ ≥ E₀; equality only when ψ_trial = ψ₀ exact
- Concrete numbers: Helium ground state E₀ = −79.0 eV (NIST); trial with Z*=2 (no screening) → −74.8 eV; trial with Z*=1.69 (optimized) → −77.5 eV; both above −79.0 eV
- Visual artifact: energy axis with true ground state floor; sequence of trial-state energies descending toward but never crossing the floor as Z* is optimized
- Two testable predictions: P1: Z*=2 gives −74.8 eV > E₀ (upper bound); P2: optimal Z*=27/16=1.6875 gives −77.5 eV, still above −79.0 eV
- Sim slug: medhavy-vol3-variational-floor
- Note: CROSS-REFERENCE — vox-variational-floor is an explainer in quantum-mechanics-vol3. The simulation workflow reel (Claude Code generating the variational calculation scene) is new; build it.

---

## Sim-04 — Perturbation Theory: Energy Levels Repel and Avoid Crossing
- Source: `quantum-mechanics-vol3/chapters/01-time-independent-perturbation-theory.md`
- Topic: CLAUDE CODE · MANIM
- Physical rule: E_n^(2) = Σ_{m≠n} |⟨m|Ĥ'|n⟩|²/(E_n^(0) − E_m^(0)); denominator shrinks → shift grows as gap closes
- Concrete numbers: two-level system with E₁=0, E₂=1 eV; coupling V=0.1 eV; avoided gap = 2V = 0.2 eV; energy levels never cross
- Visual artifact: two energy curves approaching each other as a knob turns; they bend apart instead of crossing; minimum gap = 2|V|
- Two testable predictions: P1: minimum gap = 2|⟨1|Ĥ'|2⟩| exactly at the degeneracy point; P2: set coupling to zero → levels cross freely; nonzero coupling → always avoid
- Sim slug: medhavy-vol3-avoided-crossing
