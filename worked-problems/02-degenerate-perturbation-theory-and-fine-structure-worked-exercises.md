# Worked Exercises: Degenerate Perturbation Theory and Fine Structure

*Chapter 2 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The fix for degenerate levels: build the matrix $W_{ij} = \langle i|\hat{H}'|j\rangle$ within the degenerate subspace, diagonalize it; eigenvalues are the $E^{(1)}$ shifts, eigenvectors are the good zeroth-order states.
- The two Stark selection rules: $\Delta m_\ell = 0$ (from $[\hat{H}', \hat{L}_z] = 0$ with $\hat{H}' = e\mathcal{E}\hat{z}$) and parity (diagonal elements of $\hat{z}$ between definite-parity states vanish).
- The combined fine-structure formula $E_n^\text{fs} = -\dfrac{(E_n^{(0)})^2}{2mc^2}\left(\dfrac{4n}{j+\tfrac{1}{2}} - 3\right)$, which depends on $n$ and $j$ only, and the good quantum numbers $(n,\ell,j,m_j)$ for spin-orbit coupling.

## Part A — Full Worked Example

**What this demonstrates:** How to diagonalize the perturbation within a degenerate subspace to find the good states and the energy splitting, using the hydrogen $n=2$ linear Stark effect.

**The problem:** Hydrogen in its $n=2$ level is fourfold degenerate, with states $\{|2s\rangle, |2p_0\rangle, |2p_{+1}\rangle, |2p_{-1}\rangle\}$ all at $E_2^{(0)} = -3.4$ eV. Apply a uniform field $\hat{H}' = e\mathcal{E}\hat{z}$. Find the first-order energy corrections and the good zeroth-order states, given $\langle 2s|\hat{z}|2p_0\rangle = -3a_0$.

**The solution:**

**Step 1 — Apply the selection rules to prune the matrix.** With $\hat{H}' = e\mathcal{E}\hat{z}$, the rule $[\hat{H}',\hat{L}_z]=0$ forces $\Delta m_\ell = 0$, killing every element coupling $m_\ell = 0$ states ($|2s\rangle, |2p_0\rangle$) to $m_\ell = \pm 1$ states. Parity kills all diagonal elements (definite-parity states, $\hat{z}$ odd) and the $|2p_{+1}\rangle$–$|2p_{-1}\rangle$ element.
*Why:* Symmetry zeroes most integrals before any calculation; only $\langle 2s|\hat{z}|2p_0\rangle$ (even $\times$ odd $\times$ odd = even integrand, $\Delta m_\ell = 0$) can survive.
*Check:* Of the six distinct off-diagonal pairs, exactly one survives — consistent with the chapter's count of a single needed integral.

**Step 2 — Build the $W$ matrix in the degenerate subspace.** Ordering $\{|2s\rangle, |2p_0\rangle, |2p_{+1}\rangle, |2p_{-1}\rangle\}$, with the surviving element $e\mathcal{E}\langle 2s|\hat{z}|2p_0\rangle = -3a_0 e\mathcal{E}$:
$$W = e\mathcal{E}\begin{pmatrix} 0 & -3a_0 & 0 & 0 \\ -3a_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}.$$
*Why:* $W$ collects the matrix elements of $\hat{H}'$ restricted to the degenerate subspace — the object whose diagonalization gives the first-order shifts.
*Check:* $W$ is Hermitian and traceless, so the eigenvalues must come in $\pm$ pairs (plus zeros) — consistent with symmetric Stark shifts.

**Step 3 — Diagonalize $W$ within the subspace.** The lower-right $2\times2$ block is zero: $|2p_{+1}\rangle, |2p_{-1}\rangle$ are already good states with $E^{(1)} = 0$. The upper-left block $\begin{pmatrix}0 & -3a_0 e\mathcal{E}\\ -3a_0 e\mathcal{E} & 0\end{pmatrix}$ has eigenvalues $\pm 3a_0 e\mathcal{E}$ with eigenvectors $(|2s\rangle \mp |2p_0\rangle)/\sqrt{2}$.
*Why:* A $2\times2$ antidiagonal matrix $\begin{pmatrix}0 & w\\ w & 0\end{pmatrix}$ has eigenvalues $\pm w$ and eigenvectors $(1,\mp 1)/\sqrt2$ — the diagonalization of the good-state mixing.
*Check:* The eigenvectors are normalized and orthogonal; the eigenvalues sum to zero (traceless block).

**Step 4 — Assemble the level splitting.** The $n=2$ level splits into three distinct energies:
$$E_2^{(0)} + 3a_0 e\mathcal{E}, \qquad E_2^{(0)} - 3a_0 e\mathcal{E}, \qquad E_2^{(0)}\ (\text{doubly degenerate}).$$
*Why:* Two shifted good states (the $2s$–$2p_0$ mixtures) plus the unshifted $|2p_{\pm1}\rangle$ doublet give three lines from four states.
*Check:* The middle line carries two states, matching Stark's observed double intensity of the central line.

**Final answer:** Good states $(|2s\rangle \mp |2p_0\rangle)/\sqrt{2}$ with shifts $\pm 3a_0 e\mathcal{E}$; $|2p_{\pm1}\rangle$ unshifted. Three lines, symmetric splitting.

**What made this work:** The central concept is that you must *diagonalize $\hat{H}'$ within the degenerate subspace first*. The naive approach — applying the non-degenerate first-order state formula across the $|2s\rangle$–$|2p_0\rangle$ degeneracy — gives a $1/(E_{2s}^{(0)} - E_{2p_0}^{(0)}) = 1/0$ divergence. That divergence is not a failure of perturbation theory; it is the formula announcing that the original basis is the wrong starting point. The good states are the eigenvectors of $W$, the combinations the perturbed Hamiltonian actually deforms continuously.

**Self-explanation prompt:** Why does the fact that $W$ is *traceless* in the active $2\times2$ block guarantee the two Stark shifts are exactly equal and opposite?

## Part B — Matched Practice Problem

**What this demonstrates:** The same diagonalize-in-the-subspace move, applied to a two-state degenerate system with a complex off-diagonal coupling.

**The problem:** Two states $|a\rangle$ and $|b\rangle$ share unperturbed energy $E^{(0)}$. The perturbation restricted to this subspace is
$$W = \begin{pmatrix}\Delta & \beta \\ \beta^* & -\Delta\end{pmatrix},$$
with $\Delta$ real and $\beta$ complex. Find the first-order energy corrections (eigenvalues) and the good states (eigenvectors), and state the condition under which the off-diagonal mixing $\beta$ dominates the diagonal splitting $\Delta$.

**Step 1 — Subgoal: Confirm the subspace is degenerate and $W$ is the right object.** State why diagonalizing $W$ (not $\hat{H}_0$) is required here.

**Step 2 — Subgoal: Build / read off the $W$ matrix.** It is already given; identify the diagonal and off-diagonal parts.

**Step 3 — Subgoal: Diagonalize $W$ within the subspace.** Find the two eigenvalues $E^{(1)}_\pm$ and the eigenvectors.

**Step 4 — Subgoal: Assemble the splitting and limit.** Write the gap $E^{(1)}_+ - E^{(1)}_-$ and take the limit $|\beta| \ll |\Delta|$.

**Stuck?** A $2\times2$ Hermitian matrix $\begin{pmatrix}\Delta & \beta\\ \beta^* & -\Delta\end{pmatrix}$ has eigenvalues $\pm\sqrt{\Delta^2 + |\beta|^2}$; the eigenvectors interpolate between the original basis (when $\beta\to 0$) and the symmetric/antisymmetric combinations (when $\Delta\to 0$).

*Instructor note: full solution intentionally omitted. This problem is for the student to complete after Part A.*

## Part C — Completion Problem

**The problem:** Compute the hydrogen $n=2$ fine-structure energies for $j = \tfrac{1}{2}$ and $j = \tfrac{3}{2}$ from the combined formula, and determine which level sits higher.

**Step 1 — Identify the good quantum numbers and allowed $j$ (provided).** For $n=2$, spin-orbit coupling makes $(n,\ell,j,m_j)$ the good quantum numbers. The allowed values are $j=\tfrac{1}{2}$ (from $2s_{1/2}$ and $2p_{1/2}$) and $j=\tfrac{3}{2}$ (from $2p_{3/2}$).

**Step 2 — Compute the prefactor (provided).** $\dfrac{(E_2^{(0)})^2}{2mc^2} = \dfrac{(3.4\text{ eV})^2}{2\times 511000\text{ eV}} = 1.131\times10^{-5}$ eV.

**Step 3 — Evaluate the formula for each $j$.**
*Your work here:* Apply $E_2^\text{fs} = -(1.131\times10^{-5}\text{ eV})\times\left(\dfrac{4\times 2}{j+\tfrac{1}{2}} - 3\right)$ for $j=\tfrac{1}{2}$ and $j=\tfrac{3}{2}$.

*Why (your explanation):*

**Step 4 — Determine the ordering.**
*Your work here:* Both corrections are negative; state which level shifts down *more* and therefore which sits higher.

*Why (your explanation):*

**Step 5 — Assemble the splitting (provided).** The gap is $\Delta E_\text{FS} = (-1.13 + 5.66)\times10^{-5}\text{ eV} \approx 4.5\times10^{-5}$ eV, with $2p_{3/2}$ sitting above the degenerate $2s_{1/2}$/$2p_{1/2}$ pair.

**Final answer:** $E_2^\text{fs}|_{j=1/2} = -5.66\times10^{-5}$ eV; $E_2^\text{fs}|_{j=3/2} = -1.13\times10^{-5}$ eV; $\Delta E_\text{FS}\approx 4.5\times10^{-5}$ eV.

**Self-explanation prompt:** The formula predicts $2s_{1/2}$ and $2p_{1/2}$ exactly degenerate. Explain how the $\ell$-independence of the formula produces this, and name the experiment (and the physics) that breaks the degeneracy.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the spin-orbit splitting of the hydrogen $2p$ states and presents:

**Step 1 (correct).** "The spin-orbit term is proportional to $\langle\hat{\vec{L}}\cdot\hat{\vec{S}}\rangle = \tfrac{\hbar^2}{2}[j(j+1) - \ell(\ell+1) - \tfrac{3}{4}]$, and the good quantum numbers are $(n,\ell,j,m_j)$."

**Step 2 (correct).** "For $2p$, $\ell = 1$, so $j$ can be $\tfrac{1}{2}$ or $\tfrac{3}{2}$. For $j=\tfrac{3}{2}$: $\langle\hat{\vec{L}}\cdot\hat{\vec{S}}\rangle = \tfrac{\hbar^2}{2}[\tfrac{15}{4} - 2 - \tfrac{3}{4}] = \tfrac{\hbar^2}{2}\cdot 1 = +\tfrac{\hbar^2}{2}$ (parallel, raises energy)."

**Step 3 (⚠).** "Spin-orbit coupling comes from boosting the Coulomb field into the electron's rest frame and coupling the spin moment to the resulting $\vec{B}$. That boost gives the full coupling directly, so the spin-orbit splitting is $\Delta E_\text{SO} = \tfrac{e^2}{4\pi\epsilon_0 m^2 c^2}\langle\tfrac{\vec L\cdot\vec S}{r^3}\rangle$ — no extra factors."

**Step 4 (correct-looking).** "Plugging in $\langle 1/r^3\rangle$ for $2p$ and the $\vec L\cdot\vec S$ values gives a splitting between $2p_{1/2}$ and $2p_{3/2}$; since both come from a single $\ell=1$ manifold, this is the full fine-structure splitting of the $2p$ line."

**Your tasks:**
1. Identify the error in Step 3 and explain what is missing.
2. Write the corrected Step 3.
3. Name the principle (or kinematic effect) that was violated.
4. State a check that would catch this class of error.

**Why this error is common:** The naive Lorentz-boost derivation gives a spin-orbit coupling that is too large by exactly a factor of 2, and the missing Thomas-precession $\tfrac{1}{2}$ is a kinematic relativistic correction an LLM (or a careless student) will not flag, silently doubling the predicted splitting.

## Part E — Transfer Problem

**What this demonstrates:** The degenerate-PT good-states machinery transferred to a two-level system not in the chapter — the ammonia molecule inversion doublet.

**The problem:** The ammonia molecule has two near-degenerate configurations: nitrogen above the hydrogen plane ($|L\rangle$) and below it ($|R\rangle$), each with the same energy $E_0$ in the absence of tunneling. Tunneling through the inversion barrier couples them: $\hat{H}' $ has matrix $W = \begin{pmatrix}0 & -A \\ -A & 0\end{pmatrix}$ in the $\{|L\rangle, |R\rangle\}$ basis, with $A > 0$ the tunneling amplitude. Find the good zeroth-order states and the splitting, and identify which good state lies lower.

**Hint (use only if stuck after 10 minutes):** This $W$ has exactly the structure of the Stark $2\times2$ block in Part A. The good states are the symmetric and antisymmetric combinations $(|L\rangle \pm |R\rangle)/\sqrt{2}$; compute $\langle W\rangle$ in each.

**Reflection prompt:**
1. Which good state — symmetric or antisymmetric — is lower, and how does that mirror the bonding/antibonding distinction you will meet for H$_2^+$?
2. The ammonia maser exploits the $\approx 24$ GHz splitting between these two good states. How is "the splitting equals twice the off-diagonal coupling" the same fact as the $\pm 3a_0 e\mathcal{E}$ Stark splitting?

## Part F — Interleaved Review

**F1.** For hydrogen $n=3$, the allowed $j$ values are $\tfrac{1}{2}$, $\tfrac{3}{2}$, $\tfrac{5}{2}$. Using $E_3^{(0)} = -1.51$ eV, compute $E_3^\text{fs}$ for each $j$ from the combined formula and identify which $j$ levels are degenerate.
*Chapter this draws from: 2*

**F2.** Return to the quartic oscillator of the previous chapter. For the *non-degenerate* harmonic oscillator levels, explain why the first-order state correction $|n^{(1)}\rangle = \sum_{m\neq n}\langle m|\hat x^4|n\rangle/(E_n^{(0)}-E_m^{(0)})|m\rangle$ never hits a zero denominator — and contrast this with what happens at a degenerate level.
*Chapter this draws from: Time-Independent Perturbation Theory (Chapter 1)*

**F3.** Discrimination: You are given a perturbed system and must decide whether to use non-degenerate PT directly or to diagonalize $W$ in a subspace first. For (a) hydrogen $1s$ in a weak electric field, (b) hydrogen $n=2$ in a weak electric field, (c) a harmonic oscillator with $\lambda\hat x^4$ — state which method applies and why.
*Note to instructor: the discriminating feature is whether the level of interest is degenerate. $1s$ is non-degenerate (use non-degenerate PT, get a quadratic Stark shift); $n=2$ is fourfold degenerate (diagonalize $W$, linear Stark); the oscillator levels are non-degenerate (direct non-degenerate PT). Students who reach for $W$ on the non-degenerate cases waste effort; students who use the non-degenerate formula on $n=2$ hit a zero denominator.*

**Closing reflection:** Across these problems, what single property of the unperturbed level tells you *before any integral* whether you must diagonalize in a subspace first?

## Instructor Notes

**Common errors:**
1. Forgetting to diagonalize $W$ within the degenerate subspace and instead applying the non-degenerate energy-denominator formula across the degeneracy (zero denominator).
2. Dropping the Thomas-precession factor of $\tfrac{1}{2}$ in the spin-orbit coupling, doubling the predicted splitting.
3. Confusing the good quantum numbers — using $(n,\ell,m_\ell,m_s)$ where spin-orbit coupling requires $(n,\ell,j,m_j)$.

**Signs a student needs to return:**
- They report four Stark lines from the $n=2$ manifold instead of three (they failed to recognize the doubly degenerate middle line).
- They use $j$ instead of $j+\tfrac{1}{2}$ in the fine-structure denominator, landing the splitting in the wrong decade.

**Scaffolding adjustments:** A student stuck on Part A should first do Warm-up exercise 2 from the chapter (enumerate which of the six Stark pairs survive the selection rules) before building $W$. A student who finishes Part F quickly should derive the $n=2$ fine-structure level ordering directly from the sign of the $(4n/(j+\tfrac12)-3)$ factor without plugging in the prefactor.

**Domain adaptation note:** For an atomic-spectroscopy cohort, recast Part C as predicting the wavelength splitting of the sodium D-line doublet, where the same $j$-dependent spin-orbit ordering ($p_{3/2}$ above $p_{1/2}$) sets the observed two-line structure.
