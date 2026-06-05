# Worked Exercises: Atoms in Fields — Zeeman, Stark, and Magnetic Resonance
*Chapter 9 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- You can add angular momenta and read off the allowed $j$ and $m_j$ values for a given $(\ell, s)$, and you know the Landé g-factor formula $g_J = 1 + [j(j+1)+s(s+1)-\ell(\ell+1)]/2j(j+1)$.
- You can compare the magnetic energy scale $\mu_B B$ against the fine-structure splitting $\Delta E_\text{fs}$ to decide whether you are in the weak-field (Zeeman/Landé) or strong-field (Paschen–Back) regime, with $\mu_B = 5.788\times10^{-5}$ eV/T.
- You can convert an energy splitting $\Delta E$ to a transition frequency via $\Delta E = h\nu$ and identify the spectral region.

---

## Part A — Full Worked Example

**What this demonstrates:** How to pick the correct Zeeman regime by comparing $\mu_B B$ to $\Delta E_\text{fs}$, then compute the Landé g-factor and the sublevel energy shifts of a hydrogen fine-structure level.

**The problem:** A hydrogen atom in the $2p_{3/2}$ state ($n=2$, $\ell=1$, $j=\tfrac{3}{2}$, $s=\tfrac{1}{2}$) sits in a magnetic field $B = 0.20$ T. The $2p$ fine-structure splitting is $\Delta E_\text{fs}(2p) \approx 4.5\times10^{-5}$ eV. Compute the energy shift of every $m_j$ sublevel, and find the frequency of the radiation that would drive transitions between adjacent sublevels.

**The solution:**

**Step 1 — Check the regime by comparing $\mu_B B$ to $\Delta E_\text{fs}$.**
$$\mu_B B = (5.788\times10^{-5}\ \text{eV/T})(0.20\ \text{T}) = 1.16\times10^{-5}\ \text{eV}.$$
Then $\mu_B B / \Delta E_\text{fs} = 1.16\times10^{-5} / 4.5\times10^{-5} \approx 0.26$.
*Why:* The weak-field Landé formula $\Delta E = g_J\mu_B B\, m_j$ assumes spin-orbit coupling dominates the external field, i.e. $\mu_B B \ll \Delta E_\text{fs}$. We must verify this before using it.
*Check:* $0.26$ is comfortably below 1 — weaker than the $0.65$ borderline case in the chapter's worked calculation at $0.5$ T — so the weak-field formula is reasonable, though not exact.

**Step 2 — Compute the Landé g-factor for $2p_{3/2}$.**
With $j=\tfrac{3}{2}$, $s=\tfrac{1}{2}$, $\ell=1$:
$$g_J = 1 + \frac{\tfrac{3}{2}\cdot\tfrac{5}{2} + \tfrac{1}{2}\cdot\tfrac{3}{2} - 1\cdot 2}{2\cdot\tfrac{3}{2}\cdot\tfrac{5}{2}} = 1 + \frac{\tfrac{15}{4}+\tfrac{3}{4}-2}{\tfrac{15}{2}} = 1 + \frac{\tfrac{10}{4}}{\tfrac{15}{2}} = 1 + \frac{1}{3} = \frac{4}{3}.$$
*Why:* Each fine-structure level $(n,\ell,j)$ carries its own $g_J$ because the projected mix of orbital and spin moments depends on $\ell$ and $j$ — this is the origin of the "anomalous" pattern.
*Check:* This matches the chapter's quoted $g_J = \tfrac{4}{3}$ for $2p_{3/2}$, and it lies between the pure-orbital value 1 and the pure-spin value 2, as it must for $\ell\neq 0$.

**Step 3 — Enumerate the $m_j$ sublevels and apply $\Delta E = g_J\mu_B B\, m_j$.**
For $j=\tfrac{3}{2}$ the allowed $m_j$ are $+\tfrac{3}{2}, +\tfrac{1}{2}, -\tfrac{1}{2}, -\tfrac{3}{2}$. With $g_J\mu_B B = \tfrac{4}{3}(1.16\times10^{-5}) = 1.54\times10^{-5}$ eV:
$$\Delta E = (1.54\times10^{-5}\ \text{eV})\, m_j = +2.32\times10^{-5},\ +0.77\times10^{-5},\ -0.77\times10^{-5},\ -2.32\times10^{-5}\ \text{eV}.$$
*Why:* The level splits into $2j+1 = 4$ equally spaced sublevels; the equal spacing $g_J\mu_B B$ is the signature of a single $g_J$ acting on one fine-structure level.
*Check:* The shifts are symmetric about zero (as they must be, since $\sum m_j = 0$), and the four states give four distinct energies.

**Step 4 — Find the adjacent-sublevel spacing.**
$$\delta E = g_J\mu_B B\, \Delta m_j = \tfrac{4}{3}(1.16\times10^{-5})(1) = 1.54\times10^{-5}\ \text{eV}.$$
*Why:* Magnetic-resonance / ESR transitions connect adjacent $m_j$ ($\Delta m_j = \pm 1$); the spacing is the energy a photon must carry.
*Check:* This is one unit of $g_J\mu_B B$ — the same quantity that set the level spacing in Step 3, as expected.

**Step 5 — Convert the spacing to a frequency.**
$$\nu = \frac{\delta E}{h} = \frac{1.54\times10^{-5}\ \text{eV}}{4.136\times10^{-15}\ \text{eV·s}} = 3.7\times10^{9}\ \text{Hz} \approx 3.7\ \text{GHz}.$$
*Why:* Resonant absorption requires $h\nu = \delta E$; the result tells us the spectral band needed to drive the spin/orbital transition.
*Check:* A few GHz is the microwave band — exactly where electron spin resonance (ESR) operates, consistent with the chapter's note that ESR runs at GHz for electrons.

**Final answer:** $g_J = \tfrac{4}{3}$; the four $2p_{3/2}$ sublevels shift by $\pm2.32\times10^{-5}$ eV and $\pm0.77\times10^{-5}$ eV; adjacent sublevels are split by $1.54\times10^{-5}$ eV, driven by $\approx 3.7$ GHz microwave radiation.

**What made this work:** The whole calculation hinged on Step 1 — verifying $\mu_B B \ll \Delta E_\text{fs}$ — before reaching for the Landé formula. The Landé g-factor is the single number that encodes how orbital and spin moments conspire; once we have it, the "anomalous" multi-line pattern reduces to a set of equally spaced sublevels with spacing $g_J\mu_B B$. The frequency conversion just attaches the laboratory observable (a resonance line) to the computed splitting.

**Self-explanation prompt:** Explain in your own words why two different fine-structure levels of the *same* $n$ (say $2p_{1/2}$ and $2p_{3/2}$) produce sublevel spacings that differ even though they sit in the same magnetic field.

---

## Part B — Matched Practice Problem

**What this demonstrates:** The same regime-check → g-factor → shifts → frequency pipeline, on a different fine-structure level.

**The problem:** A hydrogen atom in the $2p_{1/2}$ state ($n=2$, $\ell=1$, $j=\tfrac{1}{2}$, $s=\tfrac{1}{2}$) sits in a magnetic field $B = 0.20$ T, with $\Delta E_\text{fs}(2p) \approx 4.5\times10^{-5}$ eV. (1) Check that the weak-field regime applies. (2) Compute $g_J$ for $2p_{1/2}$. (3) List the $m_j$ sublevels and compute each energy shift $\Delta E = g_J\mu_B B\, m_j$. (4) Find the adjacent-sublevel spacing. (5) Convert that spacing to a transition frequency and name the spectral region.

**Stuck?** The structure is identical to Part A — only $j$ changed from $\tfrac{3}{2}$ to $\tfrac{1}{2}$, which changes $g_J$ and the number of sublevels. Recompute $g_J$ from scratch with the new $j$; do not reuse $\tfrac{4}{3}$.

*Instructor note: solution intentionally omitted. Students should produce the full five-step solution with Why/Check annotations.*

---

## Part C — Completion Problem

**What this demonstrates:** Filling the conceptual middle of a weak-field Zeeman calculation when the setup and the final answer are given.

**The problem:** A hydrogen atom in the $3d_{5/2}$ state ($n=3$, $\ell=2$, $j=\tfrac{5}{2}$, $s=\tfrac{1}{2}$) sits in $B = 1.0$ T. Compute $g_J$ and the energy shift of the $m_j = +\tfrac{5}{2}$ sublevel.

**Step 1 — Confirm the regime (provided).** For a $3d$ level the fine-structure splitting is even smaller than for $2p$, but take $\Delta E_\text{fs}(3d)$ to be large enough that at $B=1.0$ T, $\mu_B B = 5.79\times10^{-5}$ eV, we are told to treat the level with the weak-field Landé formula. Good quantum numbers: $n,\ell,j,m_j$.

**Step 2 — Identify the inputs (provided).** $j=\tfrac{5}{2}$, $s=\tfrac{1}{2}$, $\ell=2$. The allowed $m_j$ run from $-\tfrac{5}{2}$ to $+\tfrac{5}{2}$ in integer steps (six values).

**Step 3 — Compute $g_J$.**
*Your work here:*
*Why (your explanation):*

**Step 4 — Compute the energy shift of the $m_j = +\tfrac{5}{2}$ sublevel.**
*Your work here:*
*Why (your explanation):*

**Step 5 — Sanity-check the spacing (provided).** Adjacent sublevels are split by $g_J\mu_B B$; with six sublevels the total spread is $5\,g_J\mu_B B$, symmetric about the unperturbed energy.

**Final answer:** $g_J = \tfrac{6}{5}$, and the $m_j=+\tfrac{5}{2}$ shift is $\Delta E = \tfrac{6}{5}(5.79\times10^{-5})(\tfrac{5}{2}) = +1.74\times10^{-4}$ eV.

**Self-explanation prompt:** Why does $g_J$ for $3d_{5/2}$ come out closer to 1 than the $2p_{3/2}$ value of $\tfrac{4}{3}$? Relate your answer to the relative sizes of the orbital and spin contributions as $\ell$ grows.

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student analyzes a hydrogen $2p$ atom at $B = 0.5$ T, with $\Delta E_\text{fs}(2p)\approx 4.5\times10^{-5}$ eV, and writes:

**Step 1.** "$\mu_B B = (5.788\times10^{-5})(0.5) = 2.9\times10^{-5}$ eV."

**Step 2.** "The $2p_{3/2}$ g-factor is $g_J = \tfrac{4}{3}$ and the $2p_{1/2}$ g-factor is $g_J = \tfrac{2}{3}$."

⚠ **Step 3.** "Since $\mu_B B = 2.9\times10^{-5}$ eV is a small number, the weak-field regime clearly applies, so I'll use $\Delta E = g_J\mu_B B\, m_j$ for all sublevels and quote those as the exact energies."

**Step 4.** "The six resulting levels are the final, exact sublevel energies at $B=0.5$ T."

**Your tasks:**
1. Identify the conceptual error in Step 3 and state it precisely.
2. Compute the ratio $\mu_B B/\Delta E_\text{fs}$ at $B=0.5$ T and explain what regime it actually places the atom in.
3. State what the student should do instead to get accurate energies at this field.
4. Explain why the *small absolute size* of $\mu_B B$ is the wrong thing to look at.

**Why this error is common:** Students treat "weak field" as meaning "$\mu_B B$ is numerically small" rather than "$\mu_B B$ is small *compared to* $\Delta E_\text{fs}$," and so apply the Landé formula in the intermediate regime where neither limiting formula is valid and the levels must be obtained by diagonalizing the Zeeman and fine-structure terms together.

---

## Part E — Transfer Problem

**What this demonstrates:** The same resonance-frequency reasoning applied to magnetic resonance of a nuclear spin rather than the electronic Zeeman effect.

**The problem:** A spin-$\tfrac{1}{2}$ proton sits in a static field $B_0 = 1.0$ T and precesses at the Larmor frequency $\omega_0 = \gamma B_0$ with $\gamma = 2.675\times10^{8}$ rad s$^{-1}$ T$^{-1}$. A weak transverse rotating field with Rabi frequency $\omega_1 = \gamma B_1$, $B_1 = 1.0\times10^{-4}$ T, is applied. (a) Compute $\omega_0$ in rad/s and the corresponding $\nu_0$ in MHz. (b) Exactly on resonance ($\omega = \omega_0$), use $P_\downarrow(t) = \sin^2(\omega_1 t/2)$ to find the duration of a $\pi$ pulse that fully flips the spin. (c) Now detune to $\omega = \omega_0 + \omega_1$. Using $\Omega = \sqrt{(\omega-\omega_0)^2 + \omega_1^2}$ and $P_\downarrow = (\omega_1^2/\Omega^2)\sin^2(\Omega t/2)$, find the maximum flip probability.

**Hint (use only if stuck after 10 minutes):** For (b), the on-resonance spin fully flips when the argument $\omega_1 t/2 = \pi/2$, i.e. $t = \pi/\omega_1$ — this is the "$\pi$ pulse" of the chapter. For (c), with the detuning equal to $\omega_1$, $\Omega = \sqrt{2}\,\omega_1$, so the prefactor $\omega_1^2/\Omega^2 = \tfrac{1}{2}$.

**Reflection prompt:** (1) Both the Zeeman example and this NMR example reduce to "a resonance occurs when the drive frequency matches an internal splitting/precession frequency." What is the internal frequency in each case? (2) Why does detuning *reduce* the maximum achievable flip probability rather than just shifting the resonance frequency?

---

## Part F — Interleaved Review

**F1 — This chapter.** A hydrogen atom in the $2s$ state ($\ell=0$, $j=\tfrac{1}{2}$) is placed in $B=1.0$ T. (a) Compute $g_J$ and explain why it equals exactly 2. (b) Compute the two shifts $\Delta E = g_J\mu_B B\, m_j$ for $m_j = \pm\tfrac{1}{2}$. (c) What frequency drives transitions between them, and in what spectral region does it lie?
*Chapter this draws from: 9*

**F2 — Born approximation (named previous chapter).** In the Rutherford-scattering capstone candidate, the Born differential cross-section is $\frac{d\sigma}{d\Omega} = \left(\frac{ZZ'e^2}{4\pi\epsilon_0\cdot 4E}\right)^2\frac{1}{\sin^4(\theta/2)}$. For 5.5 MeV alphas ($Z=2$) on gold ($Z'=79$) at $\theta=90°$, the chapter quotes $\approx 428$ fm$^2$/sr. Explain in one sentence why the Sommerfeld parameter $\eta\approx 22 \gg 1$ does *not* invalidate the Born result here, and what feature of the $1/r$ potential rescues it.
*Chapter this draws from: Born approximation (Chapter 8 — scattering)*

**F3 — Discrimination.** You are handed two problems: (i) a hydrogen $2p$ atom in a 5 T field with $\Delta E_\text{fs}=4.5\times10^{-5}$ eV; (ii) a hydrogen $2p$ atom in a 0.01 T field with the same $\Delta E_\text{fs}$. Without computing full spectra, state which one is treated with the Paschen–Back formula $\Delta E = \mu_B B(m_\ell + 2m_s)$ in the $|m_\ell, m_s\rangle$ basis and which with the weak-field Landé formula in the $|j,m_j\rangle$ basis — and give the numerical ratio $\mu_B B/\Delta E_\text{fs}$ that decides each.
*Note to instructor: the discrimination point is that the choice of basis ($|j,m_j\rangle$ vs $|m_\ell,m_s\rangle$) and formula is set entirely by the size of $\mu_B B/\Delta E_\text{fs}$, not by any feature of the atom itself.*

**Closing reflection:** Across F1–F3, what single quantity told you which regime, basis, and formula to use — and why is computing it *first* the discipline this chapter is training?

---

## Instructor Notes

**Common errors:**
- Treating "weak field" as "$\mu_B B$ numerically small" rather than "$\mu_B B \ll \Delta E_\text{fs}$" — leading to misuse of the Landé formula in the intermediate regime (Part D).
- Sign and $j(j+1)$ bookkeeping errors in the Landé formula, especially forgetting that the numerator is $j(j+1)+s(s+1)-\ell(\ell+1)$ in that order.
- Applying the weak-field $|j,m_j\rangle$ basis result while the problem is actually strong-field Paschen–Back (or vice versa).

**Signs a student needs to return:**
- They cannot say *why* $g_J=2$ for an $\ell=0$ state without re-deriving the whole formula.
- They report a single set of "exact" energies in the intermediate regime without flagging that diagonalization is required.

**Scaffolding adjustments:** If a student struggles with Part A, have them first redo the chapter's own $B=0.5$ T worked calculation, comparing every step. If a student finishes Part F quickly, have them set up (not solve) the $6\times6$ intermediate-field Hamiltonian in the $|m_\ell,m_s\rangle$ basis and predict which limiting formula it reduces to at $B\to 0$ and $B\to\infty$.

**Domain adaptation note:** For students focused on NMR/MRI rather than atomic spectroscopy, recast Parts A–C around nuclear $g$-factors and Larmor frequencies, keeping the regime-check discipline ($\omega_1/\delta$ for resonance, $\mu_N B$ vs internal couplings) identical.
