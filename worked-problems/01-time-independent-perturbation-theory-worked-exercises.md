# Worked Exercises: Time-Independent Perturbation Theory

*Chapter 1 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- The ladder-operator algebra of the harmonic oscillator: $\hat{x} = \sqrt{\hbar/2m\omega}\,(\hat{a}_+ + \hat{a}_-)$, with $\hat{a}_-|n\rangle = \sqrt{n}\,|n-1\rangle$ and $\hat{a}_+|n\rangle = \sqrt{n+1}\,|n+1\rangle$.
- The first-order energy formula $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle$ and the second-order formula $E_n^{(2)} = \sum_{m\neq n}|\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle|^2/(E_n^{(0)}-E_m^{(0)})$.
- The normalization convention $\langle n^{(0)}|n^{(k)}\rangle = 0$ for $k\geq 1$, and the ground-state theorem $E_0^{(2)} < 0$ for any perturbation.

## Part A — Full Worked Example

**What this demonstrates:** How to extract the first-order energy shift of a perturbed harmonic oscillator using ladder operators, then diagnose where the expansion breaks.

**The problem:** Take the harmonic oscillator $\hat{H}_0 = \hat{p}^2/2m + \tfrac{1}{2}m\omega^2\hat{x}^2$ and add the cubic-free quartic perturbation $\lambda\hat{H}' = \lambda\hat{x}^4$. Working in natural units ($\hbar = m = \omega = 1$), compute the first-order energy correction $E_n^{(1)}$ for the level $n = 2$, and then estimate the value of $\lambda$ at which first-order perturbation theory stops being controlled for that level.

**The solution:**

**Step 1 — Express the perturbation in ladder operators.** Write $\hat{x}^4$ in terms of $\hat{a}_\pm$:
$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a}_+ + \hat{a}_-), \qquad \hat{x}^4 = \left(\frac{\hbar}{2m\omega}\right)^2(\hat{a}_+ + \hat{a}_-)^4.$$
*Why:* The matrix element $\langle n|\hat{x}^4|n\rangle$ is awkward as a position integral but trivial in the algebra, because $\hat{a}_\pm$ only shift levels by one.
*Check:* The prefactor $(\hbar/2m\omega)^2$ carries dimensions of length$^4$, as $\hat{x}^4$ must — dimensionally consistent.

**Step 2 — Keep only the level-preserving terms.** Expanding $(\hat{a}_+ + \hat{a}_-)^4$ gives 16 ordered products. Sandwiched as $\langle n|\cdot|n\rangle$, only terms with equal numbers of raising and lowering operators return to level $n$ and survive. A direct count gives
$$\langle n|\hat{x}^4|n\rangle = \left(\frac{\hbar}{2m\omega}\right)^2(6n^2 + 6n + 3).$$
*Why:* Any term with a net change in level maps $|n\rangle$ to an orthogonal $|m\neq n\rangle$, killing the diagonal matrix element.
*Check:* For $n=0$ this gives $3(\hbar/2m\omega)^2$, matching the well-known $\langle 0|\hat{x}^4|0\rangle = 3\langle 0|\hat{x}^2|0\rangle^2$ Gaussian moment.

**Step 3 — Apply the first-order energy correction.** Since $E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle = \langle n|\hat{x}^4|n\rangle$, in natural units
$$E_n^{(1)} = \frac{3}{4}(2n^2 + 2n + 1)\lambda \quad\Longrightarrow\quad E_2^{(1)} = \frac{3}{4}(8 + 4 + 1)\lambda = \frac{39}{4}\lambda = 9.75\,\lambda.$$
*Why:* The first-order shift is just the expectation value of the perturbation in the unperturbed state — one matrix element, no sum.
*Check:* Setting $n=0$ recovers $E_0^{(1)} = 3\lambda/4$, the chapter's ground-state value; the correction grows like $n^2$, as expected.

**Step 4 — Apply the breakdown diagnostic.** The expansion is controlled while $|E_n^{(1)}|/\hbar\omega \ll 1$. In natural units $\hbar\omega = 1$, so for $n=2$ we need $9.75\,\lambda \ll 1$, i.e. the correction reaches the level spacing near
$$9.75\,\lambda \sim 1 \quad\Longrightarrow\quad \lambda \sim 0.10.$$
*Why:* When the first-order shift becomes comparable to the unperturbed level spacing, neighboring levels are no longer well separated and the perturbative ordering collapses.
*Check:* For $n=0$ this same criterion gives $\lambda \sim 0.3$–$0.4$, consistent with the chapter's claim that higher levels break down at smaller $\lambda$.

**Final answer:** $E_2^{(1)} = \tfrac{39}{4}\lambda = 9.75\,\lambda$ in natural units; first-order PT for $n=2$ becomes unreliable around $\lambda \sim 0.1$.

**What made this work:** The central concept is that the first-order energy shift is a *diagonal* matrix element of the perturbation in the unperturbed basis — nothing more. The naive approach of treating $\langle n|\hat{x}^4|n\rangle$ as a brute-force integral works but obscures the structure; using ladder operators makes the level-preserving selection automatic and exposes the $n^2$ growth that controls the breakdown. A reader who forgets the level-preserving restriction would try to keep all 16 terms and produce a wrong, non-diagonal result.

**Self-explanation prompt:** Why does the $n^2$ growth of $E_n^{(1)}$ mean perturbation theory fails *earlier* (at smaller $\lambda$) for excited states than for the ground state?

## Part B — Matched Practice Problem

**What this demonstrates:** The same first-order machinery applied to a quadratic-in-position perturbation, where the surface algebra differs but the move is identical.

**The problem:** Take the same harmonic oscillator $\hat{H}_0 = \hat{p}^2/2m + \tfrac{1}{2}m\omega^2\hat{x}^2$ in natural units, but now perturb it with $\lambda\hat{H}' = \lambda\hat{x}^2$. Compute $E_n^{(1)}$ for general $n$ and specifically for $n=3$, then state at what $\lambda$ first-order PT would lose control for $n=3$.

**Step 1 — Subgoal: Express the perturbation in ladder operators.** Write $\hat{x}^2$ using $\hat{x} = \sqrt{1/2}\,(\hat{a}_+ + \hat{a}_-)$ in natural units.

**Step 2 — Subgoal: Keep only the level-preserving terms.** Identify which of the products in $(\hat{a}_+ + \hat{a}_-)^2$ return to level $n$.

**Step 3 — Subgoal: Apply the first-order energy correction.** Evaluate $E_n^{(1)} = \langle n|\lambda\hat{x}^2|n\rangle$.

**Step 4 — Subgoal: Apply the breakdown diagnostic.** Compare $|E_3^{(1)}|/\hbar\omega$ to 1.

**Stuck?** The level-preserving terms in $(\hat{a}_+ + \hat{a}_-)^2$ are exactly $\hat{a}_+\hat{a}_-$ and $\hat{a}_-\hat{a}_+$; recall $\langle n|\hat{a}_+\hat{a}_-|n\rangle = n$ and $\langle n|\hat{a}_-\hat{a}_+|n\rangle = n+1$.

*Instructor note: full solution intentionally omitted. This problem is for the student to complete after Part A.*

## Part C — Completion Problem

**The problem:** For the same oscillator in natural units, perturbed by $\lambda\hat{H}' = \lambda\hat{x}^4$, compute the **second-order** energy correction $E_0^{(2)}$ for the ground state. Use the second-order formula and the fact that $\hat{x}^4$ connects $|0\rangle$ only to $|2\rangle$ and $|4\rangle$.

**Step 1 — Identify the connected states (provided).** In natural units $\hat{x}^4 = \tfrac{1}{4}(\hat{a}_+ + \hat{a}_-)^4$. Acting on $|0\rangle$, the terms that produce a nonzero overlap with $\langle m|$ for $m\neq 0$ raise the level by 2 or by 4, so only $|2\rangle$ and $|4\rangle$ contribute to $E_0^{(2)}$.

**Step 2 — Compute the two matrix elements (provided).** A direct ladder-operator count gives
$$\langle 2|\hat{x}^4|0\rangle = \frac{1}{4}\cdot 6\sqrt{2} = \frac{6\sqrt{2}}{4} = \frac{3\sqrt{2}}{2}, \qquad \langle 4|\hat{x}^4|0\rangle = \frac{1}{4}\cdot\sqrt{24} = \frac{\sqrt{24}}{4} = \frac{\sqrt{6}}{2}.$$

**Step 3 — Apply the second-order energy formula.**
*Your work here:* Write $E_0^{(2)} = \sum_{m\in\{2,4\}}|\langle m|\lambda\hat{x}^4|0\rangle|^2/(E_0^{(0)} - E_m^{(0)})$, insert $E_0^{(0)} = \tfrac{1}{2}$, $E_2^{(0)} = \tfrac{5}{2}$, $E_4^{(0)} = \tfrac{9}{2}$, and the matrix elements from Step 2.

*Why (your explanation):*

**Step 4 — Check the sign against the theorem.**
*Your work here:* State whether your $E_0^{(2)}$ is negative, and confirm it satisfies the ground-state theorem.

*Why (your explanation):*

**Step 5 — Assemble (provided).** Carrying out the arithmetic gives $E_0^{(2)} = \lambda^2\left[\frac{(3\sqrt2/2)^2}{-2} + \frac{(\sqrt6/2)^2}{-4}\right] = \lambda^2\left[\frac{9/2}{-2} + \frac{3/2}{-4}\right] = -\frac{21}{8}\lambda^2$.

**Final answer:** $E_0^{(2)} = -\tfrac{21}{8}\lambda^2$ in natural units — negative, as the ground-state theorem requires.

**Self-explanation prompt:** Both denominators $E_0^{(0)} - E_m^{(0)}$ are negative because every intermediate state sits above the ground state. Explain in your own words why this guarantees $E_0^{(2)} < 0$ regardless of the perturbation.

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student computes the second-order shift of the **first excited state** $n=1$ of the quartic oscillator $\lambda\hat{x}^4$ in natural units, where $\hat{x}^4$ connects $|1\rangle$ to $|3\rangle$ and $|5\rangle$ below/above, but here we focus on the dominant intermediate state. They present:

**Step 1 (correct).** The relevant intermediate states for $E_1^{(2)}$ are those connected by $\hat{x}^4$: $|3\rangle$ and $|5\rangle$ (raising) and $|-1\rangle$ does not exist, so the lower partner is... only $|3\rangle$ and $|5\rangle$ contribute from above. (We restrict to $m=3$ for this illustration.)

**Step 2 (correct).** The matrix element is $\langle 3|\lambda\hat{x}^4|1\rangle$, a nonzero number times $\lambda$.

**Step 3 (⚠).** "The denominator is $E_3^{(0)} - E_1^{(0)} = \tfrac{7}{2} - \tfrac{3}{2} = 2$. So the $m=3$ contribution to $E_1^{(2)}$ is $|\langle 3|\lambda\hat{x}^4|1\rangle|^2/2$, a **positive** number, and therefore $E_1^{(2)} > 0$."

**Step 4 (correct-looking).** "Adding the $m=5$ term, which is also positive by the same logic, the total $E_1^{(2)}$ is positive, so the first excited state shifts *up* at second order."

**Your tasks:**
1. Identify the error in Step 3 and explain what went wrong.
2. Write the corrected Step 3.
3. Name the principle that was violated.
4. State a check that would catch this entire class of error.

**Why this error is common:** The second-order formula has the *current* state's energy first — $E_n^{(0)} - E_m^{(0)}$ — and students reflexively write the larger energy first, flipping the sign of every denominator where the intermediate state lies above.

## Part E — Transfer Problem

**What this demonstrates:** The first-order energy machinery transferred to a two-level / spin system not treated in the chapter.

**The problem:** A spin-$\tfrac{1}{2}$ particle sits in a strong magnetic field along $\hat{z}$, giving $\hat{H}_0 = -\gamma B_0 \hat{S}_z$ with unperturbed eigenstates $|{\uparrow}\rangle, |{\downarrow}\rangle$ and energies $\mp\tfrac{1}{2}\gamma B_0\hbar$. A weak transverse field along $\hat{x}$ adds $\lambda\hat{H}' = -\gamma B_1\hat{S}_x$ with $B_1 \ll B_0$. Treating $\lambda B_1$ as the small parameter, compute the first-order energy correction $E_\uparrow^{(1)}$ and the second-order correction $E_\uparrow^{(2)}$ to the upper/lower states.

**Hint (use only if stuck after 10 minutes):** $\hat{S}_x = \tfrac{\hbar}{2}\begin{pmatrix}0&1\\1&0\end{pmatrix}$ in the $\{|{\uparrow}\rangle,|{\downarrow}\rangle\}$ basis, so its diagonal elements vanish — what does that immediately tell you about $E^{(1)}$? For $E^{(2)}$, the only intermediate state is the other spin state.

**Reflection prompt:**
1. Why does $E^{(1)} = 0$ here, and how is that the same phenomenon as a parity-odd perturbation killing the diagonal element in a symmetric potential?
2. The exact eigenvalues of this $2\times2$ problem are $\pm\tfrac{1}{2}\gamma\hbar\sqrt{B_0^2 + B_1^2}$. Expand to second order in $B_1/B_0$ and confirm it matches your $E^{(2)}$.

## Part F — Interleaved Review

**F1.** For the quartic oscillator in natural units, compute $E_n^{(1)}$ for $n=4$ using $E_n^{(1)} = \tfrac{3}{4}(2n^2+2n+1)\lambda$, and verify the chapter's claim that it is "an order of magnitude larger" than the $n=0$ value at the same $\lambda$.
*Chapter this draws from: 1*

**F2.** Consider a perturbation $\lambda\hat{H}' = \lambda\hat{x}^3$ on the harmonic oscillator. Show that $E_n^{(1)} = 0$ for every $n$ (the diagonal matrix element of an odd power vanishes), so that the leading shift of every level is second order. Then identify which intermediate states $|m\rangle$ contribute to $E_n^{(2)}$.
*Chapter this draws from: Time-Independent Perturbation Theory (Chapter 1)*

**F3.** Discrimination: You are handed a perturbation and must decide whether the leading energy shift is first or second order. For each of $\lambda\hat{x}^2$, $\lambda\hat{x}^3$, $\lambda\hat{x}^4$ on the harmonic oscillator, state whether $E_n^{(1)}$ vanishes and why.
*Note to instructor: the discriminating feature is the parity of the perturbation — even powers have nonzero diagonal elements (first-order shift), odd powers do not (leading shift is second order). Students who memorize "$E^{(1)}$ is the expectation value" without checking parity will compute zero integrals the hard way.*

**Closing reflection:** Across these problems, what single question — asked *before* computing — would have told you whether to expect a first-order or second-order leading shift?

## Instructor Notes

**Common errors:**
1. Flipping the second-order denominator to $E_m^{(0)} - E_n^{(0)}$, producing a wrong-sign correction (especially the false claim $E_0^{(2)} > 0$).
2. Using the full Hamiltonian $\hat{H}$ instead of the perturbation $\hat{H}'$ in $E_n^{(1)} = \langle n|\hat{H}'|n\rangle$, which adds back the (already-known) $E_n^{(0)}$.
3. Retaining non-level-preserving terms in $\langle n|\hat{x}^4|n\rangle$, giving spurious off-diagonal contributions to a diagonal element.

**Signs a student needs to return:**
- They report a positive ground-state $E_0^{(2)}$ and do not flag it as impossible.
- They cannot say *before computing* whether a given perturbation produces a first-order shift.

**Scaffolding adjustments:** A student stuck on Part A should first compute $\langle n|\hat{x}^2|n\rangle$ (Part B's Step 2) to see the level-preserving selection in a two-operator product before facing the four-operator case. A student who finishes Part F quickly should derive the closed form $E_0^{(2)}$ for $\lambda\hat{x}^4$ symbolically and confirm the Bender–Wu factorial growth of higher coefficients qualitatively.

**Domain adaptation note:** For a chemistry or materials cohort, recast the quartic perturbation as the leading anharmonic correction to a molecular vibrational mode, where the same $E_n^{(1)} \propto (2n^2+2n+1)$ produces the observed convergence of vibrational overtone spacings.
