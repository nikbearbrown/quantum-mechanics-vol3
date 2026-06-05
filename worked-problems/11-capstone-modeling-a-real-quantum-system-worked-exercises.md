# Worked Exercises: Capstone — Modeling a Real Quantum System
*Chapter 11 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can execute the five-move modeling structure — system identification, method selection (by checking a small parameter $\varepsilon$), calculation to a number with units, validation against a cited measured datum with percent error, and breakdown analysis.
- You can evaluate the spherical-box confinement energy $E_{1s} = \hbar^2\pi^2/2m^*R^2$ and the Coulomb correction $-1.8\,e^2/(4\pi\epsilon_0\epsilon_r R)$, watching the unit constant $e^2/4\pi\epsilon_0 = 14.4$ eV·Å (not 1.44).
- You can write and run short finite-difference or numerical code (Python + numpy) to compute and check a quantity, and you can verify convergence of a computed eigenvalue rather than trusting a single grid.

---

## Part A — Full Worked Example

**What this demonstrates:** The full five-move discipline on the CdSe quantum dot — including the unit-careful SI confinement-energy computation that avoids the chapter's own 4.6 eV trap, validation against a cited gap, and a breakdown that names the dominant error.

**The problem:** Model the optical band gap of a $R = 1.5$ nm (3 nm diameter) CdSe quantum dot as a 3D spherical infinite square well. Inputs: $m_e^* = 0.13\,m_e$, $m_h^* = 0.45\,m_e$, $\epsilon_r = 10.6$, $E_\text{bulk} = 1.74$ eV. The measured first-exciton peak is $\approx 2.44$ eV (Norris & Bawendi 1996). Predict the gap, compute the percent error, and name the dominant breakdown.

**The solution:**

**Step 1 — Identify the system and select the method.** The lowest electron and hole states are confined in a well set by the crystal boundary; the lowest level ($\ell=0$, $j_0(kR)=0\Rightarrow kR=\pi$) gives $E_{1s} = \hbar^2\pi^2/2m^*R^2$. The method is the spherical-box (confinement) model. Its small parameter is how far $k\sim\pi/R$ sits from the band minimum where $m^*$ was measured.
*Why:* The model is trustworthy only where the effective mass is well-defined; we must flag that $m_e^*=0.13\,m_e$ is a $k=0$ value.
*Check:* The box gets the *scaling* $E\propto 1/R^2$ right; the question is whether the *input* $m^*$ is in-regime — the central judgment of this system.

**Step 2 — Compute the electron confinement energy in SI (avoiding the unit trap).** Do **not** divide an eV·Å$^2$ shortcut by $m^*/m_e$ without the $1/R^2$ in SI — that is the chapter's 4.59 eV mis-step. Compute directly:
$$E_{1s,e} = \frac{\hbar^2\pi^2}{2m_e^* R^2} = \frac{(1.055\times10^{-34})^2\pi^2}{2(0.13)(9.11\times10^{-31})(1.5\times10^{-9})^2} = \frac{1.097\times10^{-67}}{5.33\times10^{-49}} = 2.06\times10^{-19}\ \text{J} = 1.28\ \text{eV}.$$
*Why:* The confinement energy scales as $1/m^*R^2$; doing it in SI from scratch sidesteps the eV·Å$^2$ shortcut that drops the $1/R^2$ factor.
*Check:* $1.28$ eV matches the chapter's careful recomputation; the discarded 4.59 eV value was a factor-of-3.6 unit error — a red flag if it had reappeared.

**Step 3 — Compute the hole confinement and Coulomb correction.**
$$E_{1s,h} = E_{1s,e}\cdot\frac{m_e^*}{m_h^*} = 1.28\cdot\frac{0.13}{0.45} = 0.37\ \text{eV},$$
$$E_C = -\frac{1.8\,(e^2/4\pi\epsilon_0)}{\epsilon_r R} = -\frac{1.8(14.4\ \text{eV·Å})}{10.6(15\ \text{Å})} = -\frac{25.92}{159} = -0.163\ \text{eV}.$$
*Why:* The hole energy scales inversely with its heavier mass; the Coulomb term uses $e^2/4\pi\epsilon_0 = 14.4$ eV·Å (the correct constant, not 1.44).
*Check:* The heavier hole ($0.45$ vs $0.13$) gives a smaller confinement energy, as expected; the Coulomb correction lowers the gap modestly, on the order of $0.1$ eV.

**Step 4 — Assemble the predicted gap and validate.**
$$E_\text{dot} = E_\text{bulk} + E_{1s,e} + E_{1s,h} + E_C = 1.74 + 1.28 + 0.37 - 0.163 = 3.23\ \text{eV}.$$
Percent error against the cited $2.44$ eV:
$$\frac{3.23 - 2.44}{2.44} = 0.32 = 32\%.$$
*Why:* Validation requires a *cited* measured datum (Norris & Bawendi 1996) and a computed percent error, not an asserted "close enough."
*Check:* $3.23$ eV sits in the chapter's quoted 2.8–3.2 eV band; the 32% error is large enough to demand a breakdown explanation.

**Step 5 — Breakdown analysis with an order-of-magnitude estimate.** The dominant error is effective-mass nonparabolicity: $m_e^*=0.13\,m_e$ holds at $k=0$, but at $k\sim\pi/R\approx 2.1$ nm$^{-1}$ the conduction band is nonparabolic and $m_e^*\approx 0.20\,m_e$. Correcting:
$$E_{1s,e}^\text{corr} = 1.28\cdot\frac{0.13}{0.20} = 0.83\ \text{eV} \Rightarrow E_\text{dot} = 1.74+0.83+0.37-0.163 = 2.78\ \text{eV},$$
error reduced to $14\%$. A full variational Coulomb treatment reaches $\sim5\%$ for $R\ge 2$ nm.
*Why:* The breakdown must *name* the omitted physics (nonparabolicity, then correlation) and *size* it — here halving the error.
*Check:* Correcting one input parameter, not the model structure, roughly halves the error — confirming "right structure, wrong input."

**Final answer:** Predicted gap $3.23$ eV (32% high) with band-edge $m^*$; $2.78$ eV (14% high) with the nonparabolicity-corrected $m_e^*=0.20\,m_e$, against the cited $2.44$ eV.

**What made this work:** The model was structurally correct from the start — the failure lived entirely in one input parameter used outside its regime. The discipline that exposed this was doing the confinement energy in SI from scratch (dodging the 4.6 eV unit trap), validating against a *cited* number, and then sizing the nonparabolicity correction rather than hand-waving. The box gives the right scaling; the effective mass at $k\sim\pi/R$ is the lever that moves the number.

**Self-explanation prompt:** Explain why correcting *one input parameter* (the effective mass) — without changing the box model at all — cut the error from 32% to 14%, and what that says about where the model's structure was right and where its input was wrong.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same five-move discipline on a different confinement size, including the unit-careful SI computation and a breakdown.

**The problem:** Model the optical band gap of a *larger* $R = 2.0$ nm (4 nm diameter) CdSe quantum dot as a 3D spherical box. Use the same inputs: $m_e^* = 0.13\,m_e$, $m_h^* = 0.45\,m_e$, $\epsilon_r = 10.6$, $E_\text{bulk} = 1.74$ eV. (1) Identify the method and state its small-parameter caveat. (2) Compute $E_{1s,e}$ in SI from $\hbar^2\pi^2/2m_e^*R^2$. (3) Compute $E_{1s,h}$ and the Coulomb correction with $e^2/4\pi\epsilon_0 = 14.4$ eV·Å. (4) Assemble the predicted gap. (5) Argue qualitatively whether the nonparabolicity error should be *larger or smaller* at $R=2.0$ nm than at $R=1.5$ nm, and why.

**Stuck?** $E_{1s,e}\propto 1/R^2$, so going from $R=1.5$ to $R=2.0$ nm scales the confinement down by $(1.5/2.0)^2 = 0.5625$. The wavevector $k\sim\pi/R$ is *smaller* at larger $R$, so the band is *more* parabolic there — think about what that does to the nonparabolicity error before you answer (5).

*Instructor note: solution intentionally omitted. Students should produce the full five-move solution with units, a cited validation if they can find the measured 4 nm gap, and a breakdown.*

---

## Part C — Completion Problem

**What this demonstrates:** Carrying the five-move structure through the ammonia maser two-state model, filling the diagonalization and unit-conversion steps.

**The problem:** Model the NH$_3$ inversion splitting that drives the maser as a two-state tunneling system. The nitrogen sits above ($|L\rangle$) or below ($|R\rangle$) the H$_3$ plane; tunneling mixes them. Find the splitting $\Delta E$ and convert the measured 23.87 GHz inversion line to eV.

**Step 1 — Identify the system and Hamiltonian (provided).** In the $\{|L\rangle,|R\rangle\}$ basis,
$$\hat{H} = \begin{pmatrix} E_0 & -A \\ -A & E_0 \end{pmatrix},$$
with $A$ the tunneling matrix element. This is the *same* $2\times2$ structure as the Stark and weak-field Zeeman blocks.

**Step 2 — Note the dominant model uncertainty (provided).** $A$ is *exponentially* sensitive to the barrier shape, so a crude double-well model can be 24% high while a realistic potential reaches $<2\%$. The breakdown lives entirely in the barrier shape.

**Step 3 — Diagonalize the $2\times2$ Hamiltonian.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Convert the measured 23.87 GHz inversion line to $\Delta E$ in eV.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Identify the structural lesson (provided).** Recognizing the $2\times2$ form ($E_0$ on the diagonal, a coupling $-A$ off-diagonal) tells you the splitting is $2A$ immediately — the same recognition serves the Stark effect, the weak-field Zeeman blocks, and any two-level tunneling doublet.

**Final answer:** Eigenvalues $E_\pm = E_0 \mp A$, splitting $\Delta E = 2A$; the 23.87 GHz line gives $\Delta E = h\nu = (4.136\times10^{-15}\ \text{eV·s})(23.87\times10^{9}\ \text{Hz}) \approx 9.94\times10^{-5}$ eV.

**Self-explanation prompt:** Why is the tunneling splitting $\Delta E = 2A$ rather than $A$? Connect this to the eigenvalues of the $2\times2$ matrix, and explain why this is "the same diagonalization as the Stark effect."

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the CdSe quantum-dot Coulomb correction and confinement energy at $R = 1.5$ nm and writes:

**Step 1.** "The Coulomb correction is $E_C = -1.8\,e^2/(4\pi\epsilon_0\epsilon_r R)$, with $\epsilon_r = 10.6$ and $R = 15$ Å."

**Step 2.** "I'll use $e^2/4\pi\epsilon_0$ in convenient units."

⚠ **Step 3.** "Taking $e^2/4\pi\epsilon_0 = 1.44$ eV·Å, the correction is $E_C = -1.8(1.44)/(10.6\times15) = -2.59/159 = -0.0163$ eV. So the Coulomb term is negligible, about $-0.016$ eV, and I'll drop it from the gap."

**Step 4.** "The predicted gap is then $E_\text{dot} = 1.74 + 1.28 + 0.37 = 3.39$ eV."

**Your tasks:**
1. Identify the unit/constant error in Step 3 and state the correct value of $e^2/4\pi\epsilon_0$.
2. Recompute $E_C$ correctly.
3. Show how the error propagates into the wrong gap in Step 4, and give the corrected gap.
4. State the general lesson about checking the magnitude of a "convenient-units" constant before trusting that a term is negligible.

**Why this error is common:** The constant $e^2/4\pi\epsilon_0$ is $14.4$ eV·Å, but students routinely misremember it as $1.44$ eV·Å (off by a factor of 10), which silently shrinks the Coulomb correction tenfold and tempts them to drop a term that is actually $\sim0.16$ eV — a real contribution to the gap.

---

## Part E — Transfer Problem

**What this demonstrates:** The five-move discipline applied to STM tunneling via WKB — a different method (tunneling, not confinement) but the same "number with units, validate, break down" structure, with a numerical convergence check.

**The problem:** Model the STM tunneling current's distance dependence for a tungsten tip on gold with effective work function $\phi = 4.0$ eV. The WKB transmission is $T(d) = e^{-2\kappa d}$ with $\kappa = \sqrt{2m_e\phi}/\hbar$. (a) Compute $\kappa$ in Å$^{-1}$ using $\kappa = 0.5123\ \text{Å}^{-1}\sqrt{\phi[\text{eV}]}$. (b) Compute the current ratio $I(d_1)/I(d_2)$ between $d_1 = 5$ Å and $d_2 = 6$ Å. (c) Confirm it reproduces the "factor of 7–10 per ångström" rule. (d) **Numerical check:** Write pseudocode that evaluates $T(d)$ on a grid of $d$ from 4 to 8 Å and verifies that $d(\ln I)/dd = -2\kappa$ is constant (slope independent of grid spacing) — i.e. that the computed slope has *converged* and is not a grid artifact.

**Hint (use only if stuck after 10 minutes):** For (a), $\kappa = 0.5123\sqrt{4.0} = 1.025$ Å$^{-1}$. For (b), $I(d_1)/I(d_2) = e^{-2\kappa d_1}/e^{-2\kappa d_2} = e^{2\kappa(d_2-d_1)} = e^{2(1.025)(1)} = e^{2.05}\approx 7.8$. For (d), pseudocode:
```
kappa = 0.5123 * sqrt(4.0)          # 1/Angstrom
for N in [10, 100, 1000]:           # refine the grid
    d  = linspace(4.0, 8.0, N)
    lnI = log(exp(-2*kappa*d))      # = -2*kappa*d
    slope = diff(lnI) / diff(d)     # finite-difference d(lnI)/dd
    assert allclose(slope, -2*kappa)   # converged: slope == -2 kappa for all N
```

**Reflection prompt:** (1) The WKB exponential $e^{-2\kappa d}$ is reliable but the *absolute* current is off by $\sim10^3$ (the Tersoff–Hamann prefactor problem). Why is the *slope* $d(\ln I)/dd$ still a trustworthy measurement of $\phi$ even though the prefactor is wrong? (2) Why does the convergence check in (d) matter — what kind of numerical error would a too-coarse grid have hidden if the slope were *not* constant?

---

## Part F — Interleaved Review

**F1 — This chapter.** Using the variational helium result: the trial energy is $E_\text{variational} = -77.5$ eV against the measured $-79.0$ eV. (a) Compute the percent error. (b) State in one sentence why the variational result is guaranteed to be an *upper* bound. (c) The perturbative approach gives $-74.8$ eV (5.3% error). Why does variation outperform perturbation here even though $\langle V_{ee}\rangle/|E_0|\approx 0.3$ is not small?
*Chapter this draws from: 11*

**F2 — Tight-binding / band structure (named previous chapter).** The CdSe quantum-dot effective mass $m^*$ is itself a band-structure quantity — the inverse band curvature, $m^* = \hbar^2/(d^2E/dk^2)$, from the tight-binding/NFE chapter. Explain why the dot model's dominant error (nonparabolicity at $k\sim\pi/R$) is fundamentally a *band-structure* failure, not a confinement-model failure, by referencing how $m^*$ is defined and where it ceases to be constant.
*Chapter this draws from: Periodic Potentials and Band Structure (Chapter 10 — tight-binding, effective mass, NFE gap)*

**F3 — Discrimination.** You face two modeling tasks: (i) a hydrogen atom in a $10^5$ V/m laboratory electric field; (ii) alpha particles at 5 MeV scattering off gold. Without computing the full result, state which is treated with degenerate/non-degenerate perturbation theory (Stark) and which with the Born approximation (Rutherford), and name the small parameter you would check for each before trusting the method.
*Note to instructor: the discrimination point is that the capstone's whole discipline is selecting the method by checking its $\varepsilon$ — and that the Born case is a trap, since $\eta\approx22\gg1$ yet Born still works because the $1/r$ Coulomb phases cancel in $|f|^2$, not because $\varepsilon$ is small.*

**Closing reflection:** Across F1–F3, every system demanded the same five moves but a *different* method and a *different* small parameter. What is the single transferable skill the capstone is certifying — and why is "check $\varepsilon$ before trusting the method" the move an LLM most reliably gets wrong?

---

## Instructor Notes

**Common errors:**
- The unit/constant slip $e^2/4\pi\epsilon_0 = 1.44$ vs the correct $14.4$ eV·Å, and the parallel $\hbar^2\pi^2/2m^*R^2$ eV·Å$^2$ shortcut that drops the $1/R^2$ and yields the spurious 4.6 eV (Parts A, D).
- Trusting a single computed eigenvalue or slope without a convergence/grid check (Part E).
- Asserting a percent error is "good" without weighing it against the number of free parameters, or producing a breakdown with no order-of-magnitude estimate.

**Signs a student needs to return:**
- They report a confinement energy near 4.6 eV and do not flag it as a unit error.
- They apply a method (Born, WKB, weak-field $g_J$) without computing its $\varepsilon$ first.

**Scaffolding adjustments:** If a student struggles with Part A, have them redo only Step 2 (the SI confinement energy) until they reliably get 1.28 eV without the eV·Å$^2$ shortcut. If a student finishes Part F quickly, have them take the deliberately mis-selected Born-at-$\xi\sim2$ example from the chapter's R5 and run the five-move checklist on it to confirm it *fails* at the method-selection move.

**Domain adaptation note:** For students targeting a specific system (NMR, scattering, or solid-state device), let them substitute the matched system from the chapter's six candidates (A–F) into Parts B and E, keeping the five-move structure and the $\varepsilon$-before-method discipline fixed.
