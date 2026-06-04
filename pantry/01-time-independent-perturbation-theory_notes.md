# Research Notes: Chapter 01 — Time-Independent Perturbation Theory

**Corresponding chapter:** chapters/01-time-independent-perturbation-theory.md (not yet written)
**Generated:** 2026-06-03

---

## Chapter summary (capability built)

Students finish this chapter able to: set up the perturbation expansion H = H₀ + λH'; compute the first-order energy correction E_n^(1) = ⟨n⁰|H'|n⁰⟩ from a single matrix element; compute the first-order state correction as a sum over other unperturbed states weighted by off-diagonal matrix elements divided by energy denominators; compute the second-order energy correction E_n^(2) = Σ_{m≠n} |⟨m|H'|n⟩|²/(E_n⁰ − E_m⁰); identify when the denominator structure signals breakdown (near-degeneracy); and recognize that the perturbation series is generically divergent (Dyson/Bender–Wu), yet useful when truncated optimally.

---

## A. Conceptual Foundations

### A1. The perturbation expansion setup

Expand both the energies and states as power series in λ: |n⟩ = |n⁰⟩ + λ|n¹⟩ + λ²|n²⟩ + … and E_n = E_n⁰ + λE_n^(1) + λ²E_n^(2) + …. Substitute into the full Schrödinger equation, collect powers of λ. The strategy succeeds when λ is a genuine small parameter and the unperturbed problem is exactly solvable.

**Common misconception:** Students often treat λ as just a bookkeeping device and forget that the validity condition is quantitative: the ratio |⟨m|H'|n⟩| / |E_n⁰ − E_m⁰| must be ≪ 1 for all m ≠ n. A perturbation can be physically small yet perturbation theory can still fail if two levels are nearly degenerate.

**Worked example (Townsend Ch. 3, §3.1):** Harmonic oscillator in an electric field, H' = −qEx. Since ⟨n|x|n⟩ = 0 for the HO basis, the first-order correction vanishes. The second-order correction, using ⟨n±1|x|n⟩ = √(ℏ/2mω)·√(n+1 or n), gives E_n^(2) = −q²E²/(2mω²), which is the exact result because x couples only n to n±1 and the denominator is the fixed spacing ℏω. This is a case where the perturbation series terminates exactly at second order.

**Sources:** `_lib_qmsri-09-time-independent-perturbation-theory.md` (the Setup and What the machine gives you sections); `_lib_qmsri-qm-townsend-notes.md` lines 1184–1282 (§3.1, with explicit boxed equations and worked examples); Griffiths & Schroeter, *Introduction to Quantum Mechanics*, 3rd ed. §7.1–7.2; Townsend, *A Modern Approach to Quantum Mechanics*, 2nd ed. Ch. 11.

---

### A2. First-order energy correction: E_n^(1) = ⟨n⁰|H'|n⁰⟩

Take the inner product of the first-order equation with ⟨n⁰|. The H₀ terms cancel (H₀ is Hermitian). The result is purely the expectation value of H' in the unperturbed state. No diagonalization, no sum — just one integral.

**Common misconception:** Students assume this is only an approximation that gets better with higher orders. In fact for some perturbations (e.g., a constant potential shift over an entire well, or the electric HO above) it is exact. The first-order result is exact whenever H' is already diagonal in the unperturbed basis.

**Worked example (anharmonic oscillator):** H' = λx⁴. Using x = √(ℏ/2mω)(a₊ + a₋), compute ⟨n|x⁴|n⟩ = (ℏ/2mω)²·(6n² + 6n + 3). Therefore E_n^(1) = (3λℏ²/4m²ω²)(2n² + 2n + 1). In natural units (ℏ = m = ω = 1): E_n^(1) = (3λ/4)(2n² + 2n + 1). The n² growth signals that PT works worst for highly excited states.

**Sources:** `_lib_qmsri-09` (What the machine gives you, boxed formula); `_lib_qmsri-qm-townsend-notes.md` lines 1229–1235 (derivation with inner-product argument); lines 1363–1379 (non-linear oscillator worked example with explicit ladder-operator expansion of x⁴).

---

### A3. First-order state correction: the small-denominator structure

|n^(1)⟩ = Σ_{m≠n} [⟨m⁰|H'|n⁰⟩ / (E_n⁰ − E_m⁰)] |m⁰⟩. The perturbation mixes neighboring states; the amount of mixing is large when the numerator (matrix element) is large or when the denominator (energy gap) is small.

**Common misconception:** Students conflate the state correction with the energy correction. The first-order state is needed to compute the second-order energy. These are distinct objects: the first-order energy correction requires only zeroth-order states; the second-order energy correction requires first-order states.

**Worked example (quadratic Stark, ground state, Townsend §3.2):** For hydrogen 1s, the first-order state mixes in |n, ℓ=1, m=0⟩ states (selection rules kill all others). The denominator E₁⁰ − E_n⁰ is negative for n > 1, so the state correction is a sum with well-defined signs. The leading intermediate state is |2, 1, 0⟩, contributing about 55% of the total second-order energy shift.

**Sources:** `_lib_qmsri-09` (first-order state correction formula, denominator discussion); `_lib_qmsri-qm-townsend-notes.md` lines 1237–1241 (inner product with ⟨k₀| derivation), lines 1283–1337 (quadratic Stark bound and estimate); Griffiths §7.1.

---

### A4. Second-order energy correction and the ground-state theorem

E_n^(2) = Σ_{m≠n} |⟨m|H'|n⟩|² / (E_n⁰ − E_m⁰). The numerator is a non-negative squared modulus. For the ground state every other state is above it, so every denominator E₀⁰ − E_m⁰ < 0. Therefore E_ground^(2) ≤ 0 always, for any perturbation. This is a theorem, not an example.

**Common misconception:** Students often think the second-order correction is always small. It need not be: near-degeneracy (small denominator) can make the second-order term larger than the first-order term even for small λ. This is precisely the warning trigger for PT breakdown.

**Worked example (anharmonic oscillator, second order):** The off-diagonal matrix elements of x⁴ in the HO basis are nonzero for m = n ± 2 and n ± 4. The energy denominators are −2ℏω and −4ℏω. The second-order correction is negative for the ground state and grows faster with n than the first-order term, causing PT to break down earlier for excited states. Numerically, for n = 4, breakdown occurs at roughly one-quarter the λ-value needed for n = 0.

**Sources:** `_lib_qmsri-09` (second-order formula, the always-negative ground-state theorem); `_lib_qmsri-qm-townsend-notes.md` lines 1247–1278 (derivation with normalization argument; explicit "ground-state correction always negative" observation).

---

### A5. Convergence, divergence, and the Dyson argument

The perturbation series in λ generically has zero radius of convergence. Dyson (1952) gave the argument: if the sign of the coupling is flipped, the potential becomes unbounded below, so the energy is non-analytic at λ = 0. Any Taylor series must diverge. Bender and Wu (1969) confirmed this numerically for the quartic oscillator: the perturbation series coefficients grow as k!, making the series diverge for every nonzero λ.

Yet the series is useful: truncate at the optimal order (where the terms are smallest), and the error is exponentially small. Adding more terms past the optimal order makes the approximation worse.

**Common misconception:** "If the first few terms get smaller, the series converges." False. The terms can decrease for many orders before turning around. The asymptotic nature of the series means optimal truncation, not convergence, is the right criterion.

**Worked example:** For the quartic oscillator at λ = 0.1, n = 0, the optimal truncation is around 5–8 terms; past that, successive partial sums move away from the exact energy. The exact energy can be obtained by numerical diagonalization and used as ground truth.

**Sources:** `_lib_qmsri-09` (When perturbation theory breaks, the Dyson argument section, and the Still puzzling section); F. J. Dyson, "Divergence of Perturbation Theory in Quantum Electrodynamics," *Physical Review* **85**, 631 (1952); C. M. Bender & T. T. Wu, "Anharmonic Oscillator," *Physical Review* **184**, 1231 (1969).

---

## B. Domain Examples and Cases

**B1. Quartic anharmonic oscillator** — the canonical PT worked example. First-order correction from ⟨n|x⁴|n⟩ via ladder operators; second-order from off-diagonal matrix elements with m = n ± 2, n ± 4. Exact answer from numerical diagonalization in a truncated HO basis (N ≥ 30 for λ ≤ 0.2). This is the simulation target for the chapter's LLM exercise.

**B2. Hydrogen ground state in an electric field (quadratic Stark)** — parity kills the first-order shift; second-order gives E₁^(2) = −(9/2)a₀³E². Can be bounded from above and below without computing the full sum. Polarizability α_pol = 9a₀³/2.

**B3. Harmonic oscillator in a linear electric field** — exact result (E_n^(2) = −q²E²/2mω²) accessible from second-order PT using the two-term ladder-operator structure. Good case for showing when the series terminates.

**B4. Infinite square well with half-well perturbation** — H' = V₀ for 0 < x < L/2. First-order correction differs for each n; analytic with sinusoidal wavefunctions.

---

## C. Connections and Dependencies

- **Prerequisite:** HO ladder operators (a₊, a₋) and matrix elements; completeness of an orthonormal basis; bra-ket inner-product algebra (Vol. 2 formalism chapter, Townsend Ch. 1).
- **Leads to Ch. 2:** Degenerate perturbation theory is the natural extension when a denominator vanishes — the same machinery, with an additional diagonalization step within the degenerate subspace.
- **Leads to Ch. 3:** Fine structure uses degenerate PT with three simultaneous perturbations.
- **Connects to WKB (Ch. 4):** Both are approximation schemes valid in different regimes. PT works when the coupling is small; WKB works when ℏ is effectively small (slow variation).
- **Connects to scattering (Born approximation):** The first Born approximation for scattering amplitudes is exactly first-order PT applied to the scattering potential.
- **Asymptotic series bridge:** Connects to resurgent analysis and Borel summation — advanced topics referenced but not developed here.

---

## D. Current State of the Field

- **Asymptotic series and resurgence:** The divergence of perturbation series and their optimal truncation is an active research area (Écalle, Costin, Mariño). Transseries and resurgent analysis partially reconstruct the exact answer from the divergent tail. QED predictions for the electron anomalous magnetic moment (g − 2) use perturbation series known to 12th order in α, yielding 13 significant-figure agreement — despite the series diverging.
- **Rayleigh–Schrödinger vs. Brillouin–Wigner:** Two distinct formalisms; RS is order-by-order systematic; BW is non-perturbative in a certain sense. The text uses RS throughout.
- **Computational perturbation theory:** Modern quantum chemistry (MP2, MP3, CC methods) extends the machinery to many-body systems; the denominators become orbital-energy differences.

---

## E. Teaching Considerations

- **Simulation-first hook:** Build the anharmonic oscillator simulator early. Students can directly see PT curves departing from exact diagonalization, making the breakdown visible rather than a theoretical warning.
- **Ladder operators:** Students often struggle with the x⁴ matrix elements. Walk through the binomial expansion of (a₊ + a₋)⁴ step by step; there are 16 terms and only specific ones survive the ⟨n|·|n⟩ inner product.
- **The "always negative" theorem for the ground state** is a satisfying, provable result that can be assigned as a short proof exercise.
- **Parity selection rules** should be introduced here (not assumed) — they eliminate most matrix elements in both the Stark and anharmonic-oscillator examples.
- **Order of topics:** Present non-degenerate PT first (§A1–A5), then clearly flag that degenerate PT is a separate chapter (Ch. 2). Students sometimes confuse the two.

---

## F. Library Files Relevant to This Chapter

- `/pantry/_lib_qmsri-09-time-independent-perturbation-theory.md` — **Primary.** Rich prose draft covering the full nondegenerate setup, Stark effect, fine structure overview, and the Bender–Wu divergence discussion. Contains exact formulas, worked numbers, and the simulation LLM exercise. Use heavily for Ch. 1 and Ch. 2.
- `/pantry/_lib_qmsri-qm-townsend-notes.md` — **Secondary.** Chapter 3 (lines 1168–1590) covers the same material from Feiguin's graduate lecture notes: derivations with explicit inner-product steps, worked examples (quadratic Stark with bounds, HO in E-field, non-linear oscillator), and degenerate PT with the 2D HO example and the general g-fold degenerate framework.

---

## G. Gaps and Flags

- **Convergence radius proof:** The Bender–Wu result (zero radius of convergence) is stated but not proved. A chapter note flagging this as a Beyond Scope item is needed, pointing to the 1969 paper.
- **Higher-order corrections:** The chapter covers first and second order only. Third-order formulas exist but are not standard undergraduate material.
- **Near-degenerate PT:** The regime where levels are close but not exactly degenerate requires a modified framework (quasi-degenerate PT). Not covered here; flag it as a bridge topic.
- **The Stark effect at n=2 (linear Stark):** Begun in `_lib_qmsri-09` and Townsend §3.4 but really belongs to Ch. 2 (degenerate PT). Ch. 1 should reference it as the motivating example for why the nondegenerate formula breaks.
- **Simulation note:** The CLAUDE.md in the LLM exercise specifies N ≥ 50 for λ = 0.5 but N = 30 for λ ≤ 0.2. This needs to be reflected in the chapter's simulation scaffold.
