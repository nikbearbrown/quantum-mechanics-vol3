# Chapter 1 — Time-Independent Perturbation Theory

A quantum mechanic opens her toolbox and finds exactly three tools: the harmonic oscillator, the hydrogen atom, and the infinite square well. Every other bound-state problem — helium, lithium, the ammonia molecule, an electron in a doped semiconductor — is not on the solved list. Yet physicists compute energy levels for all of these, often to high precision. How?

The secret is that most real Hamiltonians are close to a solvable one. Helium is hydrogen-with-a-second-electron, and that second electron is a small correction to the Coulomb background. An oscillator with a stiff spring and a small quartic attachment is almost a harmonic oscillator. An atom in a weak electric field is almost a free atom.

Perturbation theory is the art of squeezing answers from "almost." It takes the distance from the solvable case — encoded in a small parameter $\lambda$ — and turns it into a systematic expansion. The zeroth-order term is the answer you already have. Each successive term corrects it further, at the cost of one more integral.

---

## The Setup

You have a Hamiltonian $\hat{H}_0$ whose eigenstates $|n^{(0)}\rangle$ and eigenvalues $E_n^{(0)}$ you know exactly. Reality gives you:

$$\hat{H} = \hat{H}_0 + \lambda\hat{H}',$$

where $\hat{H}'$ is the perturbation and $\lambda$ is a dimensionless small parameter — a knob you can imagine slowly turning from zero. At $\lambda = 0$ you recover the solvable problem. At $\lambda = 1$ you have the physical Hamiltonian.

Expand both the energy and the state as power series in $\lambda$:

$$E_n = E_n^{(0)} + \lambda E_n^{(1)} + \lambda^2 E_n^{(2)} + \cdots, \qquad |n\rangle = |n^{(0)}\rangle + \lambda|n^{(1)}\rangle + \lambda^2|n^{(2)}\rangle + \cdots$$

Substitute into $\hat{H}|n\rangle = E_n|n\rangle$ and collect terms at each power of $\lambda$. The entire machine lives in that one substitution. Adopt the normalization convention $\langle n^{(0)}|n^{(k)}\rangle = 0$ for all $k \geq 1$: correction kets are orthogonal to the zeroth-order state.

---

## First-Order Energy Correction

At order $\lambda^1$ the Schrödinger equation gives:

$$\hat{H}_0|n^{(1)}\rangle + \hat{H}'|n^{(0)}\rangle = E_n^{(0)}|n^{(1)}\rangle + E_n^{(1)}|n^{(0)}\rangle.$$

Take the inner product with $\langle n^{(0)}|$. The term $\langle n^{(0)}|\hat{H}_0|n^{(1)}\rangle = E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle = 0$ by the normalization convention and Hermiticity of $\hat{H}_0$. The $E_n^{(0)}\langle n^{(0)}|n^{(1)}\rangle$ term on the right also vanishes. What remains:

$$\boxed{E_n^{(1)} = \langle n^{(0)}|\hat{H}'|n^{(0)}\rangle.}$$

The first-order energy shift is the expectation value of the perturbation in the unperturbed state. No sum, no diagonalization — one matrix element. If you can compute that integral, you have the leading correction.

---

## First-Order State Correction

To find the corrected state, take the inner product of the first-order equation with $\langle m^{(0)}|$ for $m \neq n$. Since $\langle m^{(0)}|\hat{H}_0 = E_m^{(0)}\langle m^{(0)}|$:

$$(E_m^{(0)} - E_n^{(0)})\langle m^{(0)}|n^{(1)}\rangle + \langle m^{(0)}|\hat{H}'|n^{(0)}\rangle = 0.$$

Inserting completeness:

$$\boxed{|n^{(1)}\rangle = \sum_{m \neq n}\frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle.}$$

The perturbation mixes states together. The amount of mixing between $|m\rangle$ and $|n\rangle$ depends on two things: how strongly the perturbation connects them (the numerator) and how far apart they are in energy (the denominator). A small energy gap means large mixing.

And there is the denominator that causes trouble. When $E_m^{(0)} \to E_n^{(0)}$, the formula diverges. This does not mean perturbation theory has failed; it means the basis choice within the nearly-degenerate subspace was wrong. The fix — choosing the right basis before expanding — is degenerate perturbation theory, the subject of Chapter 2.

---

## Second-Order Energy Correction

Using the first-order state correction:

$$\boxed{E_n^{(2)} = \sum_{m \neq n}\frac{|\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle|^2}{E_n^{(0)} - E_m^{(0)}}.}$$

The numerator is a squared absolute value — always non-negative. The denominator changes sign: states above $n$ in energy make it negative; states below make it positive. For the **ground state**, every other state sits above it, so every denominator is negative, every term is negative, and therefore:

> **The second-order correction to the ground-state energy is always negative, for any perturbation whatsoever.**

This is a theorem. Whatever you add to the ground-state Hamiltonian — quartic potential, electric field, magnetic field — the second-order correction pushes the ground-state energy down. One sign, one proof, universal conclusion.

The connection between $E_n^{(1)}$ and $E_n^{(2)}$ is worth noting: the $k$-th order state feeds the $(k+1)$-th order energy. The first-order energy requires only the zeroth-order state — one matrix element. The second-order energy requires the first-order state — a sum over all intermediate states. They are staggered: energy at order $k$ from state at order $k-1$.

---

## Worked Example — The Quartic Oscillator

Take the harmonic oscillator and add a quartic term:

$$\hat{H} = \underbrace{\frac{\hat{p}^2}{2m} + \tfrac{1}{2}m\omega^2\hat{x}^2}_{\hat{H}_0} + \lambda\hat{x}^4.$$

The unperturbed problem has $E_n^{(0)} = \hbar\omega(n + \tfrac{1}{2})$ and the ladder-operator algebra. The perturbation is $\hat{H}' = \hat{x}^4$.

**First-order correction.** Express $\hat{x}$ in terms of raising and lowering operators:

$$\hat{x} = \sqrt{\frac{\hbar}{2m\omega}}(\hat{a}_+ + \hat{a}_-), \qquad \hat{x}^4 = \left(\frac{\hbar}{2m\omega}\right)^2(\hat{a}_+ + \hat{a}_-)^4.$$

Expanding $(\hat{a}_+ + \hat{a}_-)^4$ gives 16 terms. When sandwiched as $\langle n|\cdot|n\rangle$, only terms that return to the same level survive — those that apply equal numbers of raising and lowering operators. A systematic count (normal-ordering or direct bookkeeping) gives:

$$\langle n|\hat{x}^4|n\rangle = \left(\frac{\hbar}{2m\omega}\right)^2(6n^2 + 6n + 3).$$

In natural units ($\hbar = m = \omega = 1$):

$$E_n^{(1)} = \frac{3\lambda}{4}(2n^2 + 2n + 1).$$

For the ground state ($n = 0$): $E_0^{(1)} = 3\lambda/4$. For $n = 4$: $E_4^{(1)} = 30.75\lambda$ — an order of magnitude larger at the same $\lambda$. The correction grows as $n^2$. Perturbation theory works worst for highly excited states, whose wave functions extend further and sample the $\hat{x}^4$ term more strongly.

**When does it break?** The diagnostic is the ratio $|E_n^{(1)}|/\hbar\omega$. When this ratio approaches 1, the first-order correction has become comparable to the level spacing and the expansion is no longer controlled. For $n = 0$ in natural units, this occurs around $\lambda \sim 0.3$–$0.4$; for $n = 4$ it happens around $\lambda \sim 0.05$–$0.10$. The second-order correction is negative for the ground state (as the theorem requires), and its magnitude provides a sharper breakdown diagnostic: when $|E_n^{(2)}|$ becomes comparable to $|E_{n+1}^{(0)} - E_n^{(0)}|$, the expansion is unreliable.

---

## When Perturbation Theory Breaks: The Dyson Argument

The story so far sounds clean: compute corrections order by order, get increasingly accurate answers. But there is something hiding.

Consider the quartic oscillator at negative $\lambda$. The perturbation $\lambda\hat{x}^4$ is now negative, making the potential $V(x) = \tfrac{1}{2}m\omega^2 x^2 + \lambda x^4$ go to $-\infty$ as $|x| \to \infty$. For any $\lambda < 0$, however small, there is no bound ground state — the particle can escape to $x \to \infty$ and gain infinite energy. The system is unstable.

This means the energy $E_0(\lambda)$, viewed as a function of the complex variable $\lambda$, has a singularity on the negative real axis. Any Taylor series in $\lambda$ about zero has a radius of convergence that cannot reach that singularity. Therefore the radius of convergence is zero. The series diverges for every nonzero $\lambda$.

Freeman Dyson made this argument in 1952 for quantum electrodynamics: flip the sign of the fine-structure constant $\alpha$, electrons repel each other, the QED vacuum destabilizes, the energy is non-analytic at $\alpha = 0$, and the perturbation series has zero radius of convergence. Bender and Wu confirmed it numerically for the quartic oscillator in 1969: the series coefficients grow as $k!$, ensuring divergence for every nonzero $\lambda$. [verify]

**And yet the series is useful.** Truncate at the optimal order — the term where the partial-sum error is minimized before the factorial growth takes over — and the result is exponentially close to the true energy. The error at optimal truncation is of order $e^{-\text{const}/\lambda}$: exponentially small, invisible to any finite-order expansion.

Two conclusions follow. First, "the terms keep decreasing" does not mean the series converges — they can decrease for many orders before turning around. Optimal truncation, not convergence, is the criterion. Second, the near-degeneracy problem is more dangerous in practice than the divergence problem: a small denominator $E_n^{(0)} - E_m^{(0)}$ can make the second-order term large even at tiny $\lambda$. Always check $|\langle m|\hat{H}'|n\rangle|/|E_n^{(0)} - E_m^{(0)}|$ before trusting first-order results.

---

## The +1 — Simulation Exercise

The deliverable is `02-anharmonic-oscillator.html`: a D3 visualization showing quartic oscillator energy levels as functions of $\lambda$, comparing first-order PT, second-order PT, and exact numerical diagonalization.

### CLAUDE.md Amendment

Append this block to your project's `CLAUDE.md` before building:

````markdown
## Chapter 1 — Anharmonic Oscillator Simulation Rules

- Single HTML file. D3 v7 from CDN. No other dependencies.
- Single SVG canvas, 1100 × 600.
  Left half (550 wide): energy level diagram. Horizontal lines at current
    E_n(lambda) for n = 0..4 from exact diagonalization. Y-axis 0 to 9 
    (natural units). Label each level with n.
  Right half (550 wide): plot of E_n(lambda) vs. lambda for the highlighted n.
    Three curves: first-order PT (dashed teal), second-order PT (dashed orange),
    exact diagonalization (solid black). X-axis lambda 0 to 0.5.
- Lambda slider, range 0 to 0.5, default 0.1.
- n-selector buttons (0, 1, 2, 3, 4).
- Warning "PT NO LONGER RELIABLE" in red when |E_n^(2)| > (1/4)|E_{n+1}^(0) − E_n^(0)|.

PHYSICS (natural units hbar = m = omega = 1):
  E_n^(0) = n + 0.5
  E_n^(1) = (3/4)(2n²+2n+1)
  E_n^(2) = sum over m in {n±2, n±4} of |<m|x⁴|n>|²/(E_n^(0) − E_m^(0))
  Exact: diagonalize 30×30 HO basis matrix. Pentadiagonal (bandwidth 4).
    Jacobi iteration in vanilla JS. Increase to 50×50 for lambda > 0.2.

Sanity checks to console:
  At lambda=0: exact eigenvalues = n+0.5 within 1e-6.
  E_0^(2) must be negative (theorem).
  At lambda=0.1, n=0: first-order estimate 0.575, exact slightly below.
````

### The Simulation Prompt

````
Build 02-anharmonic-oscillator.html following CLAUDE.md.

SHOW.
Quartic oscillator H = H_HO + lambda*x^4 in natural units.
Unperturbed: E_n^(0) = n + 0.5.
First-order: E_n^(1) = (3/4)(2n²+2n+1).
Second-order: sum of squared off-diagonal matrix elements over energy denominators,
  restricting to m in {n-4, n-2, n+2, n+4}.
Exact: 30×30 (50×50 for lambda>0.2) matrix diagonalization, Jacobi iteration.

SAY.
Produce 02-anharmonic-oscillator.html with:
  Left SVG half: energy levels as horizontal lines at exact E_n(lambda).
  Right SVG half: three overlaid curves for the selected n.
  Lambda slider and n buttons below both panels.
  "PT NO LONGER RELIABLE" warning text at threshold.

CONSTRAIN.
- Vanilla JS only. No math.js. Implement Jacobi diagonalization directly.
- At every lambda change, recompute exact eigenvalues and update both panels.
- Comments at every physics step.

VERIFY.
(a) At lambda=0: all exact energies match n+0.5 within 1e-6.
(b) At lambda=0.1, n=0: second-order curve below first-order curve (negative correction).
(c) Warning fires for n=4 before n=0 as lambda increases.
(d) For n=2: E_2^(2) is also negative (all states above n=0 have mixed sign,
    but n=2 should be checked — if negative, all levels checked).
````

### Exploration Tasks

**Ground-state breakdown.** Slide $\lambda$ from $0$ to $0.5$ with $n = 0$ selected. At what $\lambda$ does first-order PT depart from exact by more than 10%? At what $\lambda$ does the "PT NO LONGER RELIABLE" warning fire? At what $\lambda$ does second-order PT fail the 10% test?

**Excited-state breakdown.** Repeat for $n = 4$. At what $\lambda$ does first-order PT fail? Compare the breakdown $\lambda$ for $n = 4$ versus $n = 0$. By what factor do they differ?

**The always-negative theorem.** At $\lambda = 0.1$, $n = 0$: read the gap between first-order and second-order PT curves. Verify it is negative (second-order curve lies below first-order). Now check $n = 2$: is $E_2^{(2)}$ negative as well? The theorem guarantees this for $n = 0$; for $n = 2$ it depends on which intermediate states dominate.

---

## References

- Griffiths, D.J. and Schroeter, D.F. (2018). *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press. §7.1–7.2. [verify]
- Townsend, J.S. (2012). *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books. Ch. 11. [verify]
- Bender, C.M. and Wu, T.T. (1969). "Anharmonic oscillator." *Physical Review*, 184(5), 1231–1260. https://doi.org/10.1103/PhysRev.184.1231 [verify]
- Dyson, F.J. (1952). "Divergence of perturbation theory in quantum electrodynamics." *Physical Review*, 85(4), 631–632. https://doi.org/10.1103/PhysRev.85.631 [verify]

---

## Running Project — Model a Real Quantum System, End to End

**This chapter adds:** the first method in your toolkit — non-degenerate perturbation theory — together with its small parameter $\lambda$ (and the sharper near-degeneracy diagnostic $|\langle m|\hat{H}'|n\rangle|/|E_n^{(0)}-E_m^{(0)}|$), which becomes the first row of the method-selection table you carry through the volume to the capstone.

Across this volume you will assemble a *method toolkit* and a *small-parameter selection table*, then in Chapter 11 use them to model one real system through five disciplined moves: identify, select-method-by-checking-$\varepsilon$, calculate-a-number-with-units, validate-against-a-cited-datum, analyze-breakdown. Start that table now. Today's entry: **non-degenerate PT — $\varepsilon = \lambda$ (or the matrix-element/energy-gap ratio) — breaks when $\varepsilon \gtrsim 1$, when levels near-degenerate, or for negative-coupling instabilities (Dyson).** The system this method serves in the capstone candidate list is the image-charge / anharmonic correction to a base model — e.g. the leading correction to the STM barrier, or the quartic correction to a confining well.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Scaffolding the project's running table file (a Markdown table with columns method / $\varepsilon$ / formula / breaks-when) — *Why AI works here:* it is structured boilerplate with a fixed schema you specify and can read back.
- Expanding $(\hat{a}_+ + \hat{a}_-)^4$ and bookkeeping which of the 16 terms return to the same level — *Why AI works here:* the combinatorics is mechanical and you can independently check the answer against the closed form $6n^2+6n+3$.
- Drafting a docstring or unit-conversion helper for the $E_n^{(1)}$ formula — *Why AI works here:* it is reformatting with a known target.

**The tell:** You are using AI well when you have an independent way to check the output — here, the analytic $\langle n|\hat{x}^4|n\rangle = (\hbar/2m\omega)^2(6n^2+6n+3)$ and the ground-state theorem $E_0^{(2)}<0$.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding whether PT is even the right method for *your* chosen capstone system — *Why AI fails here:* it will happily apply first-order PT to a problem where $\lambda \sim 1$ or where a near-degeneracy makes the second-order denominator blow up, and it will not flag that the small parameter is not small. Method selection is the move it gets wrong silently.
- Judging the breakdown point — at what $\lambda$ the expansion stops being trustworthy — *Why AI fails here:* the criterion ($|E_n^{(2)}|$ comparable to the level spacing; the Dyson zero-radius-of-convergence argument) is a physical-validity call, not a lookup, and a confident wrong threshold is worse than none.

**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.

**Physics-judgment connection:** This trains the habit of checking the small parameter $\varepsilon$ *before* trusting a method, and of checking the near-degeneracy ratio $|\langle m|\hat{H}'|n\rangle|/|E_n^{(0)}-E_m^{(0)}|$ even when $\lambda$ itself looks small — the discipline that the whole capstone rests on.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** the first two rows of the project's method-selection table, plus a derivation of one first-order energy correction you will reuse.
**Tool:** Claude Project — the table and method notes persist across all eleven chapters, so a project with the running table in its context beats a one-off chat.
**The Prompt:**
```
I am building a "method-selection table" for a quantum mechanics project that
will eventually model one real physical system end to end. Each row is one
approximation method, its small parameter epsilon, the formula for epsilon,
and the condition under which it breaks down.

Start the table with NON-DEGENERATE TIME-INDEPENDENT PERTURBATION THEORY.
Fill in exactly these columns and nothing more:
  - Method name
  - Small parameter epsilon (the dimensionless quantity that must be << 1)
  - Formula for epsilon in terms of H', H_0 spectrum (give both the coupling-
    constant form lambda and the matrix-element/energy-gap ratio form)
  - "Breaks when" (state all three: epsilon ~ 1, near-degeneracy, and the
    negative-coupling / zero-radius-of-convergence instability)

Then, as a worked check, derive the first-order energy correction for the
quartic-perturbed harmonic oscillator H = H_HO + lambda*x^4. Show the step
where (a_+ + a_-)^4 is expanded and only same-level terms survive, and arrive
at E_n^(1) = (3 lambda /4)(2n^2 + 2n + 1) in natural units. Show all algebra.

Do NOT advise me on which method to use for any specific system, and do NOT
estimate at what lambda the expansion "fails" — I will judge that myself.
```
**What this produces:** a clean first row of the running table and a re-derivation of $E_n^{(1)}$ you can verify against the chapter's boxed result.
**How to adapt:** *Your system:* if your capstone candidate is the STM barrier, add a note that PT here supplies the image-charge correction, not the leading exponential. *ChatGPT/Gemini:* paste the same prompt; expect more eager (and sometimes wrong) "validity" commentary — strip it. *Claude Project:* put the running-table schema in the project's custom instructions so every later chapter appends to the same table.
**Builds on:** nothing yet — this is the seed.  **Next:** Chapter 2 adds the degenerate-PT row and the $\alpha^2$ fine-structure scale.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the project repository with a `method-table.md` and a verified numerical check of $E_n^{(1)}$ and $E_0^{(2)}$ for the quartic oscillator.
**Tool:** Claude Code — it can create the project directory, write a small verification script, run it, and report the number.
**Skill level:** Beginner
**Setup — confirm:**
- [ ] An empty project directory for the running project (create one if needed).
- [ ] Python 3 with numpy available.
- [ ] Add to `CLAUDE.md`: "The running-project method table lives in `method-table.md`; never delete rows, only append. All physics constants in SI unless a cell says natural units."
**The Task:**
```
In the running-project directory:
1. Create method-table.md with a Markdown table with columns:
   Method | epsilon | formula for epsilon | breaks when.
   Add one row: non-degenerate perturbation theory, epsilon = lambda (or
   |<m|H'|n>|/|E_n^0 - E_m^0|), breaks when epsilon ~ 1 / near-degeneracy /
   negative-coupling instability.
2. Create check_pt.py that, in natural units (hbar=m=omega=1):
   - computes E_n^(1) = (3/4)(2n^2+2n+1) for n=0..4,
   - builds the 30x30 harmonic-oscillator matrix of H = H_HO + lambda*x^4
     for lambda=0.05, diagonalizes it numerically,
   - prints, for n=0..4: E_n^(0), E_n^(0)+lambda*E_n^(1), and the exact
     eigenvalue, side by side.
3. Run it. Confirm at lambda=0 the exact eigenvalues equal n+0.5 to 1e-6,
   and that the exact ground-state energy lies BELOW the first-order estimate
   (the second-order correction is negative).
Do not modify any file outside this directory. Report the printed table.
```
**Expected output:** `method-table.md` (one row) and a console table comparing zeroth-order, first-order, and exact energies.
**What to inspect:** at $\lambda=0$, exact eigenvalues $= n+0.5$; the exact ground-state energy sits below the first-order estimate (negative $E_0^{(2)}$ — the theorem); the first-order error grows with $n$.
**If it goes wrong:** if the exact ground state comes out *above* the first-order estimate, the $\hat{x}^4$ matrix was built with the wrong $\hbar/2m\omega$ prefactor or the basis is too small — print $\langle n|\hat{x}^4|n\rangle$ and check it against $6n^2+6n+3$ before re-diagonalizing.
**CLAUDE.md / AGENTS.md note:** add "Append-only to `method-table.md`. Every numerical claim in this project must have a script that reproduces it."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the R4 numerical comparison of first-order PT against exact diagonalization for the quartic oscillator.
**Validation type:** Numerical result
**Risk level:** Medium — the formula is standard, but a wrong oscillator-length prefactor produces plausible-looking energies that are silently off.
**Setup:** use your own R4 output (`check_pt.py` console table).
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Time-Independent Perturbation Theory
□ Correctness: does E_n^(1) match (3/4)(2n^2+2n+1) for every n=0..4?
□ Completeness: did the script report the lambda=0 sanity check (eigenvalues = n+0.5)?
□ Scope: did it stay inside the project directory and touch no other files?
□ Sign theorem: is the exact ground-state energy BELOW the first-order estimate
  (E_0^(2) < 0) at lambda=0.05?
□ Growth law: does the first-order error grow roughly as n^2 across n=0..4?
□ Failure-mode check: any of —
  - fluent but wrong (energies look reasonable but the hbar/2m*omega prefactor
    on x^4 is wrong by a power)
  - basis truncation too small (eigenvalues not converged; increase to 50x50)
  - second-order correction reported positive (a sign or denominator error)
```
**What to do with findings:** pass → record the verified numbers as the project's first datum. one fail → fix the prefactor or basis size, re-run, note the change in `method-table.md`. multiple fails → do the $\langle n|\hat{x}^4|n\rangle$ algebra by hand before trusting any code.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* What AI produced and how you used it.
> *2:* One specific thing the AI could not determine that required your judgment.
**Physics-judgment connection:** this validation trains checking a numerical spectrum against a known analytic limit ($n+\tfrac12$ at $\lambda=0$) and against a sign theorem ($E_0^{(2)}<0$) before believing it — the same discipline that, in the capstone, separates a defensible number from a fluent guess.

---

*Chapter 2 follows: degenerate perturbation theory. When two or more unperturbed levels share an energy, the small denominator in the first-order state formula signals breakdown — not of perturbation theory, but of the basis choice. The fix is to diagonalize $\hat{H}'$ within the degenerate subspace before expanding. The payoffs: the linear Stark effect, the hydrogen fine structure, and the removal of accidental degeneracy.*
