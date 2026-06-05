# Worked Exercises: Periodic Potentials and the Band Structure of Solids
*Chapter 10 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can state Bloch's theorem $\psi_{n,k}(x) = e^{ikx}u_{n,k}(x)$ with $u_{n,k}(x+a)=u_{n,k}(x)$, and you know that crystal momentum $\hbar k$ is defined only modulo $G = 2\pi/a$, so all distinct states fit in the first Brillouin zone $k\in[-\pi/a,\pi/a]$.
- You can use degenerate perturbation theory on a $2\times2$ matrix and you know the nearly-free-electron result that the gap at the zone boundary is $2|V_{G_1}|$, twice the relevant Fourier component of the potential.
- You can read the tight-binding dispersion $E(k) = E_0 - 2t\cos(ka)$ and compute the effective mass from band curvature, $m^* = \hbar^2/(d^2E/dk^2)$.

---

## Part A — Full Worked Example

**What this demonstrates:** How the nearly-free-electron (NFE) gap opens at the Brillouin-zone boundary via $2\times2$ degenerate perturbation theory, giving a gap of $2|V_{G_1}|$, and how Bragg-reflected standing waves explain the energy split.

**The problem:** A one-dimensional crystal of lattice constant $a$ has a weak periodic potential whose Fourier series is $V(x) = \sum_G V_G e^{iGx}$ with a single dominant component $V_{G_1} = 0.80$ eV at $G_1 = 2\pi/a$ (average potential set to zero). The lattice constant is $a = 3.0$ Å. (a) Locate the value of $k$ where the lowest gap opens. (b) Compute the gap width. (c) Write the two standing waves that form there and say which has lower energy.

**The solution:**

**Step 1 — Locate the degeneracy at the zone boundary.**
Free-electron states $|k\rangle$ have $E_k^{(0)} = \hbar^2 k^2/2m$. The states $|k=+\pi/a\rangle$ and $|k=-\pi/a\rangle$ both have energy $\hbar^2\pi^2/2ma^2$ and are coupled by $V_{G_1}$ because $(+\pi/a) - (-\pi/a) = 2\pi/a = G_1$.
$$k = \pm\frac{\pi}{a} = \pm\frac{\pi}{3.0\ \text{Å}} = \pm 1.05\ \text{Å}^{-1}.$$
*Why:* Ordinary perturbation theory fails here because the energy denominator $E_{+\pi/a}^{(0)} - E_{-\pi/a}^{(0)}$ vanishes — the two states are degenerate — so we must use degenerate perturbation theory.
*Check:* The gap opens precisely at the zone boundary $k=\pm\pi/a$, not at $k=0$ or at some interior point — this is the defining feature of the NFE picture.

**Step 2 — Build and diagonalize the $2\times2$ matrix.**
In the basis $\{|+\pi/a\rangle, |-\pi/a\rangle\}$, the diagonal elements vanish (zero average potential) and the off-diagonal element is $V_{G_1}$:
$$W = \begin{pmatrix} 0 & V_{G_1}^* \\ V_{G_1} & 0 \end{pmatrix}, \qquad \text{eigenvalues } \pm|V_{G_1}|.$$
*Why:* The off-diagonal element is the Fourier component that connects the two degenerate plane waves; diagonalizing splits the doubly degenerate level into $E_\pm = \hbar^2\pi^2/2ma^2 \pm |V_{G_1}|$.
*Check:* The matrix is traceless and Hermitian, so its eigenvalues are $\pm|V_{G_1}|$, symmetric about the unperturbed energy — as expected when the average potential is zero.

**Step 3 — Compute the gap width.**
$$\text{Band gap} = E_+ - E_- = 2|V_{G_1}| = 2(0.80\ \text{eV}) = 1.6\ \text{eV}.$$
*Why:* The gap is the energy difference between the two standing-wave solutions at the same $k=\pi/a$; it equals exactly twice the relevant Fourier component, not $|V_{G_1}|$ alone.
*Check:* A 1.6 eV gap is semiconductor-scale, consistent with the chapter's examples (Si 1.12 eV, GaAs 1.42 eV); doubling the potential would double the gap, as $2|V_{G_1}|$ predicts.

**Step 4 — Form the standing waves and order them by energy.**
The degenerate plane waves mix equally into:
$$\psi_+ \propto \cos(\pi x/a), \qquad \psi_- \propto \sin(\pi x/a).$$
$|\psi_+|^2$ peaks at the ion positions ($x = na$), where the attractive ionic potential is lowest; $|\psi_-|^2$ peaks between the ions.
*Why:* At $k=\pi/a$ the de Broglie wavelength $\lambda = 2a$ satisfies the Bragg condition, so forward and backward waves mix equally into standing waves — the physical origin of the split.
*Check:* In a crystal where ions attract electrons, $\psi_+$ samples lower potential energy, so $E(\psi_+) < E(\psi_-)$; their difference is the $2|V_{G_1}|$ gap. The lower-energy state piles charge on the ions — physically sensible.

**Final answer:** The lowest gap opens at $k = \pm\pi/a = \pm1.05$ Å$^{-1}$, has width $2|V_{G_1}| = 1.6$ eV, and is bounded below by $\psi_+\propto\cos(\pi x/a)$ (charge on the ions, lower energy) and above by $\psi_-\propto\sin(\pi x/a)$ (charge between ions, higher energy).

**What made this work:** The single most important move was recognizing that the gap opens *at the zone boundary* where two free-electron states become degenerate, forcing degenerate perturbation theory. Once the $2\times2$ matrix is written, the answer is mechanical: a traceless Hermitian matrix with off-diagonal $V_{G_1}$ has eigenvalues $\pm|V_{G_1}|$, so the gap is $2|V_{G_1}|$. The Bragg/standing-wave picture is what makes the factor of 2 and the energy ordering physically inevitable rather than algebraic accidents.

**Self-explanation prompt:** Explain why the gap is $2|V_{G_1}|$ and not $|V_{G_1}|$, referencing both the eigenvalues of the $2\times2$ matrix and the two standing waves.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same zone-boundary degeneracy → $2\times2$ diagonalization → standing-wave reasoning, with different numbers.

**The problem:** A 1D crystal has lattice constant $a = 4.0$ Å and a weak periodic potential with dominant Fourier component $V_{G_1} = 0.45$ eV at $G_1 = 2\pi/a$ (zero average). (a) Find the $k$ value where the lowest gap opens, in Å$^{-1}$. (b) Compute the gap width. (c) Write the two standing waves and state which has lower energy in a crystal of attractive ions. (d) If you wanted to *double* the gap, by what factor must you change $V_{G_1}$?

**Stuck?** The gap location depends only on $a$ (it is always $k=\pm\pi/a$); the gap *width* depends only on $|V_{G_1}|$ through the relation $2|V_{G_1}|$. Do not confuse the two — and remember the factor of 2.

*Instructor note: solution intentionally omitted. Students should produce the full four-part solution with Why/Check annotations, including the standing-wave energy ordering.*

---

## Part C — Completion Problem

**What this demonstrates:** Computing a tight-binding effective mass when the dispersion and band edges are given.

**The problem:** A tight-binding band has $E(k) = E_0 - 2t\cos(ka)$ with on-site energy $E_0 = 0$, hopping integral $t = 0.50$ eV, and lattice constant $a = 3.0$ Å. Find the effective mass $m^*$ at the band bottom, expressed as a multiple of the free-electron mass $m_e$.

**Step 1 — Identify the band edges and bottom (provided).** At $k=0$: $E = E_0 - 2t$ (band bottom, symmetric superposition). At $k=\pm\pi/a$: $E = E_0 + 2t$ (band top). Bandwidth $= 4t = 2.0$ eV. We expand about the bottom, $k=0$.

**Step 2 — Expand the dispersion near the bottom (provided).** Using $\cos(ka)\approx 1 - \tfrac{1}{2}(ka)^2$:
$$E(k) \approx (E_0 - 2t) + t a^2 k^2 = E_\text{bottom} + \frac{\hbar^2 k^2}{2m^*}.$$

**Step 3 — Solve for $m^*$ in terms of $t$ and $a$.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Evaluate $m^*$ numerically as a multiple of $m_e$.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Sanity-check the sign and trend (provided).** Near the band *bottom* the curvature $d^2E/dk^2 > 0$, so $m^* > 0$. Larger hopping $t$ gives lighter $m^*$ (the electron propagates more easily); near the band *top* the curvature flips sign and $m^* < 0$, the hole regime.

**Final answer:** $m^* = \dfrac{\hbar^2}{2ta^2}$. Numerically, $m^* = \dfrac{(1.055\times10^{-34})^2}{2(0.50\times1.602\times10^{-19})(3.0\times10^{-10})^2} \approx 7.7\times10^{-31}$ kg $\approx 0.85\,m_e$.

**Self-explanation prompt:** Why does increasing the hopping integral $t$ *decrease* the effective mass? Connect your answer to the physical meaning of $t$ as the ease of hopping between neighboring orbitals.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the effective mass near the *top* of a tight-binding band $E(k) = E_0 - 2t\cos(ka)$, working at $k = \pi/a$, and writes:

**Step 1.** "The dispersion is $E(k) = E_0 - 2t\cos(ka)$, so $\dfrac{dE}{dk} = 2ta\sin(ka)$."

**Step 2.** "Differentiating again, $\dfrac{d^2E}{dk^2} = 2ta^2\cos(ka)$."

⚠ **Step 3.** "At the band top, $k=\pi/a$, so $\cos(\pi) = -1$ and $\dfrac{d^2E}{dk^2} = 2ta^2(-1) = -2ta^2$. But effective mass must be positive, so I'll take the magnitude: $m^* = \hbar^2/|d^2E/dk^2| = \hbar^2/(2ta^2) > 0$."

**Step 4.** "Therefore the carrier at the band top has the same positive effective mass as at the band bottom."

**Your tasks:**
1. Identify the conceptual error in Step 3 and state it precisely.
2. Keep the correct sign: what is the actual value of $m^* = \hbar^2/(d^2E/dk^2)$ at $k=\pi/a$?
3. Explain physically what a *negative* effective mass means at the band top, using the chapter's vocabulary.
4. State what quasiparticle the band-top carrier behaves as, and how it responds to an applied force.

**Why this error is common:** Students assume effective mass must be positive and discard the sign of the band curvature, missing that the negative curvature at the band top is *real physics* — it is exactly what makes the carrier a hole, a positively charged quasiparticle moving opposite to the applied force.

---

## Part E — Transfer Problem

**What this demonstrates:** The same "bands vs gaps from a dispersion relation" reasoning applied to the exact Kronig–Penney model rather than the perturbative NFE picture.

**The problem:** The delta-function Kronig–Penney model gives the dispersion relation
$$\cos(ka) = f(\alpha a), \qquad f(\alpha a) = \cos(\alpha a) + \frac{P}{\alpha a}\sin(\alpha a),$$
where $E = \hbar^2\alpha^2/2m$ and $P$ is the dimensionless barrier strength. Take $P = 3\pi/2 \approx 4.71$. (a) Evaluate $f$ at $\alpha a = \pi$. (b) Use the bound $|\cos(ka)|\le 1$ to argue that $\alpha a = \pi$ is a band edge. (c) Explain, in terms of $f$ exceeding $\pm1$, why a forbidden gap opens just above $\alpha a = \pi$. (d) State what happens to the band and gap widths as $P\to\infty$.

**Hint (use only if stuck after 10 minutes):** At $\alpha a = \pi$, $\sin(\pi) = 0$ and $\cos(\pi) = -1$, so $f(\pi) = -1$ exactly — this sits right on the boundary $|\cos(ka)|=1$. Just above $\pi$, the $-(P/\alpha a)\,\epsilon$ behavior of the second term drives $f$ below $-1$, where no real $k$ exists. Larger $P$ widens the excursions of $f$ beyond $\pm1$, so gaps widen and bands narrow toward the isolated-atom limit.

**Reflection prompt:** (1) In the NFE picture the gap is $2|V_{G_1}|$; in the Kronig–Penney picture a gap opens where $|f(\alpha a)| > 1$. In what sense are these *the same physical gap* viewed from two starting points (weak potential vs exact)? (2) Why does the gap always open at the zone boundary in both pictures?

---

## Part F — Interleaved Review

**F1 — This chapter.** A 1D crystal of lattice constant $a = 2.5$ Å has a weak periodic potential with $V_{G_1} = 1.0$ eV. (a) At what $k$ does the lowest gap open? (b) What is the gap width? (c) The next Fourier component $V_{G_2} = 0.30$ eV at $G_2 = 4\pi/a$ opens a second gap at $k=\pm 2\pi/a$ (folded to the zone center). What is that second gap's width?
*Chapter this draws from: 10*

**F2 — Linear Stark effect / degenerate PT (named previous chapter).** In the atoms-in-fields chapter, the hydrogen $n=2$ Stark problem also reduced to diagonalizing a small matrix in a degenerate subspace, with the only surviving coupling $\langle 2s|e\mathcal{E}\hat{z}|2p_0\rangle = -3a_0 e\mathcal{E}$ giving eigenvalues $\pm 3a_0 e\mathcal{E}$. State the structural similarity to this chapter's NFE gap calculation: in both, a degeneracy forces a $2\times2$ (or block) diagonalization, and the splitting is twice an off-diagonal matrix element. Give the off-diagonal element and the resulting splitting for each case.
*Chapter this draws from: Atoms in Fields (Chapter 9 — Zeeman, Stark, magnetic resonance)*

**F3 — Discrimination.** You are given two band-structure tasks: (i) a crystal whose electrons are nearly free, with a weak potential ($V_{G_1}\ll$ bandwidth); (ii) a crystal whose electrons are tightly bound to atoms with small inter-site overlap. Without computing, state which is best treated with the nearly-free-electron model (start from plane waves, gap $=2|V_{G_1}|$) and which with the tight-binding model (start from atomic orbitals, $E(k)=E_0-2t\cos ka$) — and name the small parameter that decides each.
*Note to instructor: the discrimination point is that NFE and tight-binding describe the same bands from opposite limits; the choice is set by whether the potential is weak (start from free electrons) or the overlap is weak (start from atoms), i.e. by where the material sits between $P=0$ and $P\to\infty$ in Kronig–Penney terms.*

**Closing reflection:** Across F1–F3, three different methods (NFE, tight-binding, Kronig–Penney) all produced the same physics — bands separated by gaps at the zone boundary. What does it tell you about Bloch's theorem that all three starting points converge on the same band structure?

---

## Instructor Notes

**Common errors:**
- Reporting the NFE gap as $|V_{G_1}|$ instead of $2|V_{G_1}|$ — dropping the factor of 2 from the eigenvalue split.
- Forgetting that the gap opens *at the zone boundary* $k=\pm\pi/a$ and trying to apply non-degenerate perturbation theory there (the denominator vanishes).
- Taking the magnitude of the band curvature at the band top and missing the negative effective mass / hole physics (Part D).

**Signs a student needs to return:**
- They cannot explain why $\psi_+$ (charge on the ions) is lower in energy than $\psi_-$.
- They treat NFE and tight-binding as describing *different* materials rather than the same bands from opposite limits.

**Scaffolding adjustments:** If a student struggles with Part A, walk through the chapter's Bragg-reflection picture first — let the standing waves motivate the $2\times2$ matrix rather than the reverse. If a student finishes Part F quickly, have them sketch the extended, reduced, and repeated zone schemes for the Part A band and confirm all three encode the same dispersion.

**Domain adaptation note:** For students in materials science or device physics, recast Part C around a real semiconductor's measured effective mass (e.g. extract $t$ for a given $m^*$ and lattice constant) so the abstract hopping integral connects to a tabulated band parameter.
