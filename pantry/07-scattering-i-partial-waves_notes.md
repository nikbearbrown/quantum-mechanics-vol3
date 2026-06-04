# Research Notes: Chapter 07 — Scattering I: Partial Waves
**Corresponding chapter:** chapters/07-scattering-i-partial-waves.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to compute a scattering cross-section by partial-wave analysis: expand the scattered wavefunction in Legendre polynomials, extract phase shifts δ_ℓ from boundary conditions, assemble the total and differential cross-sections, and apply the optical theorem as a sanity check. The canonical worked example is s-wave scattering from a hard sphere or finite square well, where the algebra is explicit and the physics—especially the 4πa² low-energy result and the factor-of-two surprise at high energy—is memorable.

---

## A. Conceptual foundations

### The scattering setup
Time-independent, energy-conserving scattering: Hamiltonian H = H₀ + V(r), where V is localized near the origin. The incident state is a plane wave ψ₀ = √n · e^(ik·r). Far from the scatterer the total wavefunction has the asymptotic form

ψ(r) ≈ √n [e^(ikz) + f(θ) e^(ikr)/r]

where f(θ) is the **scattering amplitude**. This single complex function encodes everything measurable about the collision at energy E = ℏ²k²/2m.

Source: Fitzpatrick (LibreTexts) §14.1 — "Fundamentals of Scattering Theory" [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory/14.01:_Fundamentals_of_Scattering_Theory]

### Differential and total cross-sections
The differential cross-section dσ/dΩ = |f(θ)|². This follows from the ratio of scattered flux to incident flux. The total cross-section σ = ∫|f(θ)|² dΩ.

### Partial-wave expansion
For a central (spherically symmetric) potential expand f(θ) in Legendre polynomials:

f(θ) = Σ_ℓ (2ℓ+1) f_ℓ P_ℓ(cos θ)

where f_ℓ = (e^(2iδ_ℓ) − 1) / (2ik) = e^(iδ_ℓ) sin δ_ℓ / k

and δ_ℓ is the **phase shift** for the ℓ-th partial wave. Each partial wave contributes independently to the total cross-section:

σ = (4π/k²) Σ_ℓ (2ℓ+1) sin²δ_ℓ

The phase shift δ_ℓ encodes all physics of the potential in that angular momentum channel. Positive δ_ℓ corresponds to an attractive well (wave pulled in); negative δ_ℓ to a repulsive barrier (wave pushed out).

Source: Fitzpatrick §14.3 — "Partial Waves"; also Hitoshi Murayama (Berkeley) lecture notes 221B §1 [http://hitoshi.berkeley.edu/221B/scattering3.pdf]; University of Texas at Austin partial-wave PDF [https://web2.ph.utexas.edu/~vadim/Classes/2022f/PW.pdf]

### The optical theorem
From the partial-wave expansion of σ_total and f(θ=0):

σ_total = (4π/k) Im[f(θ=0)]

This is the **optical theorem**: total cross-section equals the imaginary part of the forward scattering amplitude (times 4π/k). Physical meaning: scattering in all directions requires depletion of the forward beam; the forward scattered wave must interfere destructively with the incident wave to produce a shadow. The optical theorem is a consequence of probability conservation (unitarity of the S-matrix).

Source: Fitzpatrick §14.4 [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory/14.04:_Optical__Theorem]

### Low-energy s-wave scattering and scattering length
At low energy (ka ≪ 1, where a is the range of the potential), only the ℓ=0 (s-wave) term contributes significantly. For the s-wave: δ₀ → −ka_s as k→0, where a_s is the **scattering length**. Then:

σ_total → 4πa_s²  (low energy)

The scattering length a_s is the single most important parameter for low-energy scattering. It can be positive (effective repulsion) or negative (effective attraction). A large positive a_s signals a near-resonance (bound state just below threshold). The geometric cross-section is πa², so the quantum result σ = 4πa² is four times larger—a purely wave-mechanical result with no classical counterpart.

Source: Fitzpatrick §14.7 — "Low-Energy Scattering"; also Murayama 221B notes

### Resonances
When the potential supports a quasi-bound state just above threshold, the phase shift δ₀ passes through π/2, sin²δ₀ → 1, and the partial cross-section hits its unitarity limit 4π(2ℓ+1)/k². This is a **scattering resonance** (Breit-Wigner resonance). The total cross-section shows a sharp peak. Resonances are the quantum scattering analog of resonance in a driven oscillator, and they appear in nuclear (compound nucleus resonances) and atomic physics contexts.

Source: Fitzpatrick §14.8 — "Resonances" [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory/14.08:_Resonances]

---

## B. Domain examples and cases

### Canonical worked example: hard-sphere s-wave scattering

Potential: V = ∞ for r < a, V = 0 for r ≥ a.

Boundary condition: ψ = 0 at r = a. The radial equation outside is that of a free particle. For the ℓ=0 wave, match the solution u₀(r) = A sin(kr + δ₀) to the boundary condition:

sin(ka + δ₀) = 0  →  δ₀ = −ka

(Exact, all energies.) The s-wave cross-section:

dσ/dΩ|_(ℓ=0) = sin²(ka)/k²

Low energy (ka ≪ 1): δ₀ ≈ −ka, σ_total ≈ 4πa² — four times the geometric cross-section.

High energy (ka ≫ 1): all partial waves up to ℓ_max ≈ ka contribute. Averaging sin²δ_ℓ → 1/2 and summing gives σ_total ≈ 2πa² — twice the geometric cross-section. The extra factor of πa² comes from diffractive forward scattering (the Poisson/Arago bright spot): the shadow requires forward scattering interference that itself contributes a geometric cross-section's worth of scattering.

Source: Fitzpatrick §14.6 [https://phys.libretexts.org/Bookshelves/Quantum_Mechanics/Introductory_Quantum_Mechanics_(Fitzpatrick)/14:_Scattering_Theory/14.06:_Hard-Sphere_Scattering]; Murayama 221B [http://hitoshi.berkeley.edu/221B/scattering3.pdf]; UTK notes [http://electron6.phys.utk.edu/PhysicsProblems/QM/7-Scattering/partial.html]

### Square-well s-wave scattering
For a finite spherical square well of depth V₀ and radius a, the interior radial solution is also sinusoidal (with wave vector κ² = k² + 2mV₀/ℏ²). Matching at r = a gives δ₀ via:

tan(δ₀) = [k tan(κa) − κ tan(ka)] / [κ + k tan(ka)tan(κa)]

When κa = nπ/2 (n odd) the cross-section diverges (hits unitarity bound) — a Ramsauer–Townsend-type resonance in 3D. When ka → 0, the scattering length is:

a_s = a[1 − tan(κ₀a)/(κ₀a)]

where κ₀ = √(2mV₀/ℏ²). This formula contains the physics of how a potential's bound-state spectrum influences its low-energy scattering.

Source: Liboff Introductory QM Ch. 14 (OCR source in local pantry, Table of Contents confirmed); Murayama 221B notes

### Nuclear physics connection
Neutron-proton scattering at low energies is dominated by s-wave scattering. The measured scattering length for the triplet state (proton and neutron spins parallel) is a_t ≈ 5.4 fm, while for the singlet state a_s ≈ −23.7 fm. The large negative singlet scattering length signals the virtual bound state (unbound dineutron) just above threshold. This is the entry-level nuclear scattering example in every graduate text.

---

## C. Connections and dependencies

### Prerequisites from earlier volumes
- Spherical harmonics and the radial Schrödinger equation (hydrogen atom chapter) — partial waves are the same spherical Bessel expansion applied to scattering boundary conditions
- Probability current and flux — needed to define cross-sections
- Legendre polynomials and their orthogonality — needed to extract individual f_ℓ
- The plane-wave expansion e^(ikz) = Σ_ℓ (2ℓ+1) i^ℓ j_ℓ(kr) P_ℓ(cos θ) — the Rayleigh expansion, essential for matching incident and scattered waves

### Forward connections to Ch 8
The partial-wave method handles the exact phase shifts for simple potentials but is impractical for complex potentials where many ℓ values contribute. Chapter 8 (Born approximation) gives a complementary, perturbative approach valid at high energy or weak potential, where an analytic Fourier-transform result replaces the phase-shift machinery.

### Forward connections beyond Vol 3
- Nuclear resonance theory: Breit-Wigner formula, compound nucleus model
- S-matrix theory and T-matrix formalism
- Coupled-channel scattering (inelastic processes)
- Cold atoms: Feshbach resonances are magnetic-field-tuned scattering resonances; entire field of ultracold atom physics rests on controlling the scattering length

---

## D. Current state of the field

Partial-wave analysis remains the standard first tool in nuclear and particle physics for analyzing elastic scattering data. In cold-atom physics, the scattering length is the central quantity; Feshbach resonances allow experimental tuning of a_s from −∞ to +∞, enabling study of the BCS-BEC crossover. The optical theorem has become a fundamental consistency check in quantum field theory (optical theorem for forward Compton scattering, crossing symmetry). Numerical partial-wave analysis (solving the coupled-channel Schrödinger equation) is standard in ab initio nuclear structure calculations.

Current research frontier: few-body Efimov physics—when the two-body scattering length is large, three-body bound states appear at geometric progressions of binding energies. First observed in 2006 in ultracold cesium. Predicted by Vitaly Efimov in 1970. Direct consequence of large s-wave scattering length physics.

---

## E. Teaching considerations

### The conceptual arc
Hook: Why does a hard sphere of radius a scatter four times its geometric cross-section at low energy? This paradox (σ = 4πa² vs. πa² classical) is pure wave mechanics and is easy to state, impossible to predict without the formalism.

Key pedagogical moves:
1. Establish f(θ) as the central object; everything follows from it
2. Show the plane-wave expansion (Rayleigh) before introducing phase shifts — students see where the partial-wave idea comes from
3. Derive σ_total = (4π/k²) Σ(2ℓ+1)sin²δ_ℓ and immediately note the unitarity bound per partial wave: σ_ℓ ≤ 4π(2ℓ+1)/k²
4. The optical theorem should come from integrating the partial-wave sum, not from an abstract unitarity argument — the Fitzpatrick derivation (compare two sums) is the right approach

### Common confusions
- Students confuse the scattering length a_s with the range of the potential a. They are different: a_s can be much larger than a (near resonance) or negative.
- The sign convention for δ_ℓ: attractive potentials give positive phase shifts (wave pulled in, zero crossing moved closer). This is worth dwelling on with a diagram.
- The high-energy result σ = 2πa² (not πa²) — students expect the classical result. The Poisson-spot / diffractive-shadow argument is essential.

### Simulation opportunity
Interactive: slider for V₀ and radius a of a spherical square well, live plot of δ₀(k), σ_total(k), and the phase-shifted radial wavefunction compared to the free wave. Students watch the resonances appear and the scattering length change sign as V₀ crosses the bound-state threshold.

### Notation note
Some texts (Griffiths) write f_ℓ = e^(iδ_ℓ) sin(δ_ℓ)/k; others (Sakurai) write a_ℓ = (e^(2iδ_ℓ)−1)/2ik. Both appear in the literature; the chapter should pick one and note the other.

---

## F. Library files relevant to this chapter

- `/pantry/_lib_qmsri-qm-townsend-notes.md` — contains plane-wave expansion (Rayleigh formula) in Ch. 10 problems section; check for partial-wave exercises
- `/pantry/436681929-...Liboff...txt` (in physics-quantum-mechanics-sri/pantry) — Ch. 14 Table of Contents lists: "14.1 Introduction; 14.2 Scattering Amplitude; 14.3 Partial-Wave Analysis; 14.4 The Born Approximation; 14.5 Atomic-Radiative Absorption Cross Section; 14.6 Elements of Formal Scattering Theory. The Lippmann-Schwinger Equation" — directly relevant but OCR quality noisy; use only for cross-checking formulas

**External primary source (strongest):**
- Fitzpatrick, *Introductory Quantum Mechanics* (UT Austin), Ch. 14 [https://farside.ph.utexas.edu/teaching/qmech/qmech.html] — CC BY-NC-SA 4.0, full text online, directly citable. Covers §14.1 Fundamentals, §14.3 Partial Waves, §14.4 Optical Theorem, §14.5 Phase Shifts, §14.6 Hard Sphere, §14.7 Low Energy Scattering, §14.8 Resonances.

**Secondary sources:**
- Murayama (Berkeley) 221B lecture notes §1–§3 [http://hitoshi.berkeley.edu/221B/scattering3.pdf]
- Griffiths & Schroeter, *Introduction to Quantum Mechanics*, Ch. 11 — standard undergraduate treatment
- Sakurai & Napolitano, *Modern Quantum Mechanics*, Ch. 6 — more formal S-matrix language
- Liboff, *Introductory Quantum Mechanics* Ch. 14 — local pantry source

---

## G. Gaps and flags

- **No existing chapter draft**: this is a completely new chapter for Vol 3; author needs to write from scratch.
- **Plane-wave Rayleigh expansion derivation**: not fully spelled out in Fitzpatrick's scattering chapter — point author to earlier chapter on spherical Bessel functions, or Murayama's notes §1.1 where the expansion is derived explicitly.
- **Resonance treatment**: Fitzpatrick §14.8 gives Breit-Wigner in partial-wave form but without the derivation from the S-matrix pole — acceptable for this level but author should note the S-matrix pole picture in "still puzzling" or a footnote.
- **Phase shift sign conventions differ by source**: flag for author to pick one convention and apply it consistently across Ch 7 and Ch 8.
- **Ramsauer-Townsend effect** (anomalously low cross-section in noble gas electron scattering at ~1 eV due to near-cancellation of phase shifts) is a beautiful experimental consequence — worth a footnote or a "domain examples" box.
- **Coverage of ℓ > 0 phase shifts for finite well**: most pedagogical sources focus on s-wave; the chapter should at least sketch how higher ℓ are handled before declaring low-energy dominance of s-wave.
