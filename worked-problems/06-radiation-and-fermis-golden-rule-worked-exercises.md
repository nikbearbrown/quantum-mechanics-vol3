# Worked Exercises: Radiation and Fermi's Golden Rule
*Chapter 6 of Quantum Mechanics — Volume 3*

> These exercises follow a research-backed sequence: full worked example → matched practice → completion problem → error-recognition → transfer → interleaved review. Each section builds on the previous. Do not skip ahead.

## Prerequisites

- Fermi's golden rule $W_{i\to f} = \frac{2\pi}{\hbar}|\langle f|\hat{H}'|i\rangle|^2\,\rho(E_f)$, and that the rate is the product of *three* ingredients: the squared matrix element, the density of states, and (for radiation) an $\omega^3$ factor.
- The electric-dipole selection rules $\Delta\ell = \pm 1$, $\Delta m = 0, \pm 1$, $\Delta s = 0$, derived from a parity argument and an azimuthal integral — not memorized.
- The Einstein-$A$ coefficient $A_{21} = \frac{\omega^3}{3\pi\epsilon_0\hbar c^3}\,|\langle 1|e\hat{\vec r}|2\rangle|^2$, and that spontaneous emission scales as $\omega^3$ while stimulated emission scales as $B_{21}u(\omega)$.

---

## Part A — Full Worked Example

**What this demonstrates:** That a hydrogen spontaneous-emission lifetime is the inverse of the Einstein-$A$ rate, and that getting it right means getting all three ingredients — radial matrix element, the $\omega^3$ factor, and the constants — correct together.

**The problem:** Compute the spontaneous-emission rate $A_{21}$ and lifetime $\tau$ for the hydrogen $2p \to 1s$ transition. Use $\hbar\omega = 10.2$ eV for the photon, the averaged dipole matrix element $|\langle 1s|e\hat{\vec r}|2p\rangle|^2_{\text{avg}} = e^2\,\frac{2^{15}}{3^{10}}\,a_0^2$, and verify the result against the measured $\tau = 1.596$ ns.

**The solution:**

**Step 1 — Confirm the transition is dipole-allowed.** Apply the selection rules: $2p \to 1s$ has $\Delta\ell = 0 - 1 = -1$ and $\Delta m = 0,\pm1$ depending on the $2p$ substate.
$$\Delta\ell = \pm 1 \;\checkmark, \qquad \Delta m \in \{0,\pm1\}\;\checkmark.$$
*Why:* If the transition were forbidden ($\Delta\ell = 0$, like $2s\to1s$), $A_{21}$ would vanish and the whole calculation would be moot.
*Check:* The competing $2s \to 1s$ has $\Delta\ell = 0$ and is forbidden — its lifetime is $\sim 0.12$ s, eight orders of magnitude longer, confirming the rule's teeth.

**Step 2 — Get the photon angular frequency in SI.** Convert $\hbar\omega = 10.2$ eV to $\omega$ in rad/s.
$$\omega = \frac{10.2\times1.602\times10^{-19}\,\text{J}}{1.055\times10^{-34}\,\text{J·s}} = 1.55\times10^{16}\,\text{rad/s}.$$
*Why:* The $\omega^3$ factor is the dominant order-of-magnitude lever; it must be the *angular frequency in rad/s*, never the energy in eV.
*Check:* $\omega^3 = (1.55\times10^{16})^3 = 3.7\times10^{48}$ rad³/s³ — a huge number; a single dropped power of $\omega$ would shift the rate by 16 orders of magnitude.

**Step 3 — Assemble the dipole matrix element.** With $a_0 = 5.29\times10^{-11}$ m and $e = 1.602\times10^{-19}$ C:
$$|\langle 1s|e\hat{\vec r}|2p\rangle|^2_{\text{avg}} = e^2\,\frac{2^{15}}{3^{10}}\,a_0^2 = e^2\,\frac{32768}{59049}\,a_0^2 = 0.555\,e^2 a_0^2.$$
Numerically: $0.555\times(1.602\times10^{-19})^2\times(5.29\times10^{-11})^2 = 3.99\times10^{-59}\,\text{C}^2\text{m}^2$.
*Why:* This is the squared matrix element that enters the golden rule; the factor $2^{15}/3^{10} \approx 0.555$ is the angular-average of the three $2p$ substates.
*Check:* The matrix element is of order $e a_0$ as expected for an atomic dipole — $|\langle r\rangle| \sim 0.74\,a_0$, a fraction of a Bohr radius, which is physically sensible.

**Step 4 — Apply the Einstein-$A$ formula.** With $\epsilon_0 = 8.854\times10^{-12}$ F/m and $c = 3.00\times10^8$ m/s:
$$A_{21} = \frac{\omega^3}{3\pi\epsilon_0\hbar c^3}\,|\langle 1s|e\hat{\vec r}|2p\rangle|^2_{\text{avg}}.$$
$$A_{21} = \frac{3.7\times10^{48}}{3\pi(8.854\times10^{-12})(1.055\times10^{-34})(3.00\times10^8)^3}\times 3.99\times10^{-59} \approx 6.3\times10^{8}\,\text{s}^{-1}.$$
*Why:* All three ingredients — $\omega^3$, $|\langle\ldots\rangle|^2$, and the universal constants — combine here into a rate with units of $\text{s}^{-1}$.
*Check:* The exponents work out: $48 - 59 = -11$ in the numerator powers, balanced against the constant denominator to land near $10^8$ — the right decade for an allowed optical transition.

**Step 5 — Invert to a lifetime and compare.**
$$\tau = \frac{1}{A_{21}} = \frac{1}{6.3\times10^8} = 1.6\times10^{-9}\,\text{s} = 1.6\,\text{ns}.$$
*Why:* The lifetime is the inverse total decay rate; for $2p$ this is the single $2p\to1s$ channel.
*Check:* The measured value is $\tau = 1.596$ ns — agreement to the accuracy of the dipole approximation, which is excellent here since $ka_0 \approx 10^{-3} \ll 1$.

**Final answer:** $A_{21} \approx 6.3\times10^8\,\text{s}^{-1}$, $\tau \approx 1.6$ ns, matching the measured $1.596$ ns.

**What made this work:** The result lands on the measured number because every one of the three multiplicative ingredients was correct: the matrix element (right because the transition is allowed and the angular average was applied), the $\omega^3$ factor (right because $\omega$ was taken as an angular frequency in rad/s, not an energy in eV), and the bundle of constants. The single most common way to be wrong here is to mis-power or drop $\omega^3$, which silently shifts the rate by decades — the lifetime would come out in picoseconds or microseconds, and the only guard is comparing against the cited $1.596$ ns.

**Self-explanation prompt:** Why does dropping a single factor of $\omega$ change the answer by 16 orders of magnitude, while a 10% error in the matrix element changes it by only 10%?

---

## Part B — Matched Practice Problem

**The problem:** Compute the spontaneous-emission rate $A_{21}$ and lifetime $\tau$ for the sodium D-line, the $3p \to 3s$ transition at $\lambda = 589$ nm. You are given the dipole matrix element $|\langle 3s|e\hat{\vec r}|3p\rangle|^2_{\text{avg}} = 6.4\,e^2 a_0^2$. Verify against the measured lifetime $\tau \approx 16$ ns.

Work it in the same five conceptual moves as Part A: confirm the transition is dipole-allowed, get $\omega$ in rad/s from the wavelength, assemble the matrix element, apply the Einstein-$A$ formula, and invert to a lifetime and compare.

**Stuck?** Get $\omega$ from the wavelength via $\omega = 2\pi c/\lambda$. The $3p \to 3s$ transition has $\Delta\ell = 1 - 0 = +1$, so it is allowed. The photon energy here ($\sim 2.1$ eV) is much smaller than the $2p\to1s$ photon (10.2 eV), so the $\omega^3$ factor is smaller — expect a *longer* lifetime than hydrogen's 1.6 ns.

*Instructor note: no solution is provided here. The teaching point is that the longer sodium lifetime (16 ns vs. 1.6 ns) comes chiefly from the smaller $\omega^3$ despite a larger matrix element — the $\omega^3$ factor, not the dipole strength, dominates the comparison.*

---

## Part C — Completion Problem

**The problem:** Compute the 2D density of states $\rho_{2D}(E)$ for electrons confined to a plane of area $A$, and contrast it with the 3D result.

**Step 1 — Count states in a $k$-space shell.** With periodic boundary conditions on a square of side $L$ ($A = L^2$), allowed wavevectors are $\vec k = (2\pi/L)(n_x, n_y)$, one state per spin per cell of area $(2\pi/L)^2$. States in the annulus $[k, k+dk]$ occupy area $2\pi k\,dk$:
$$dn = \frac{2\pi k\,dk}{(2\pi/L)^2} = \frac{A\,k\,dk}{2\pi}.$$
*Why:* The density of states is a counting exercise — states per $k$-space area, converted to states per energy.

**Step 2 — Relate $k$ to $E$.** For a non-relativistic electron $E = \hbar^2 k^2/(2m)$, so $k\,dk = (m/\hbar^2)\,dE$.
$$dn = \frac{A}{2\pi}\cdot\frac{m}{\hbar^2}\,dE.$$
*Why:* We need $dn/dE$, so we trade the $k\,dk$ shell measure for $dE$ using the dispersion relation.

**Step 3 — Read off $\rho_{2D}(E)$.**
*Your work here:*

*Why (your explanation):*

**Step 4 — Compare to the 3D result $\rho_{3D}(E) = Vmk/(2\pi^2\hbar^2) \propto \sqrt{E}$.**
*Your work here:*

*Why (your explanation):*

**Step 5 — State the physical consequence.** The flat (energy-independent) 2D density of states is the physics behind quantum-well devices: filling a 2D band adds states at a constant rate per energy, unlike the $\sqrt{E}$ rise of a 3D gas.
*Why:* The density of states is not decoration — it is what shapes the rate in any golden-rule process and the electronic properties of low-dimensional systems.

**Final answer:** $\rho_{2D}(E) = Am/(2\pi\hbar^2)$, independent of energy, in contrast to $\rho_{3D}(E) \propto \sqrt{E}$.

**Self-explanation prompt:** Why does the dimensionality of the system change the *energy dependence* of the density of states (constant in 2D, $\sqrt E$ in 3D), even though the counting recipe is the same?

---

## Part D — Error-Recognition Problem

> **Use this section only after completing Parts A–C.**

**The problem:** A student is asked to compute the spontaneous-emission rate for the hydrogen $3d \to 2p$ transition and to list which $n=3 \to n=2$ transitions are allowed.

**Student's work:**

Step 1 — The transitions from $n=3$ to $n=2$ are $3s\to2p$, $3p\to2s$, $3d\to2p$, and $3s\to2s$, $3p\to2p$, $3d\to2s$.

Step 2 — The dipole rate is $A_{21} = \frac{2\pi}{\hbar}|\langle f|\hat H'|i\rangle|^2\rho$, the golden rule.

⚠ Step 3 — For the rate, I use $A_{21} = \frac{\omega}{3\pi\epsilon_0\hbar c^3}|\langle 2p|e\vec r|3d\rangle|^2$, taking a single factor of $\omega$ since that is what appears in the energy $\hbar\omega$.

Step 4 — All six transitions in Step 1 therefore have comparable rates set by their matrix elements.

**Your tasks:**
1. Correct the power of $\omega$ in Step 3 and state the correct Einstein-$A$ formula. Explain, using the density of photon states $\rho(\omega) = V\omega^2/(\pi^2 c^3)$, why the rate carries $\omega^3$ and not $\omega^1$.
2. From Step 1's list, strike every transition that is electric-dipole forbidden, naming the rule ($\Delta\ell = \pm1$) that kills each one.
3. Explain why $3d \to 2s$ (which the student left in) is forbidden even though it changes $\ell$.
4. Explain why, contrary to Step 4, the *allowed* transitions do *not* all have comparable rates — what additional factor, beyond the matrix element, separates them.

**Why this error is common:** Students see $\hbar\omega$ in the photon energy and assume the rate carries a single power of $\omega$, missing that two extra powers enter through the photon density of states — turning a $\sim10^8\,\text{s}^{-1}$ rate into a wrongly $\omega^2$-suppressed estimate.

---

## Part E — Transfer Problem

**The problem:** An electron sits in the ground state of a 1D box of length $L = 10$ nm. A weak time-independent perturbation $V_0 = 10^{-3}$ eV couples it to the free-particle continuum (ionization). (i) Compute the ground-state energy $E_1 = \pi^2\hbar^2/(2mL^2)$ in eV. (ii) Evaluate the 1D free-particle density of states $\rho_{1D}(E) = \frac{L}{2\pi\hbar}\sqrt{m/(2E)}$ at $E = E_1$. (iii) Using $|\langle k_f|V_0|1\rangle|^2 = V_0^2 L/2$, apply Fermi's golden rule to find the ionization rate $W$. (iv) Check whether $W\cdot t \ll 1$ holds for $t = 1\,\mu$s.

**Hint (use only if stuck after 10 minutes):** This is the same golden-rule machinery as Part A but with a *flat 1D* density of states instead of the photon $\omega^3$ structure — the three ingredients are $|V_{fi}|^2 = V_0^2 L/2$, the 1D $\rho(E)$, and the $2\pi/\hbar$ prefactor. The validity check $W\cdot t \ll 1$ is the same condition that bounds first-order PT from Chapter 5.

**Reflection prompt:** (1) In Part A the rate carried an $\omega^3$ density-of-states factor; here it carries a $1/\sqrt{E}$ factor. What does each tell you about how the *number of available final states* shapes the rate? (2) The golden rule requires $W\cdot t \ll 1$ for first-order PT *and* $t$ large enough that the sinc-squared has sharpened — how wide is the valid window for this ionization problem, and is it as comfortable as the femtosecond-to-nanosecond window for hydrogen emission?

---

## Part F — Interleaved Review

**F1 — This chapter.** The hydrogen $3p$ state decays to both $1s$ and $2s$. (a) Compute $\hbar\omega$ for each branch. (b) Using $|\langle 2s|\hat r|3p\rangle|^2 \approx 0.093\,a_0^2$ and the $3p\to1s$ matrix element, compute both $A$-coefficients. (c) Find the branching fractions. (d) Compute the total rate $\Gamma_{\text{total}} = A(3p\to1s) + A(3p\to2s)$ and the lifetime $\tau = 1/\Gamma_{\text{total}}$; compare to the measured $\tau_{3p} \approx 5.3$ ns. Which branch dominates, and why is it the $\omega^3$ factor and not the matrix element that decides?
*Chapter this draws from: 6.*

**F2 — Previous chapter.** *Chapter this draws from: Chapter 5 — Time-Dependent Perturbation Theory and Transitions.* Fermi's golden rule is the *same* first-order amplitude from Chapter 5, summed over a continuum of final states. In Chapter 5 a single discrete final state gave the oscillating sinc-squared lineshape $P(\delta,t) = (|V_{fi}|/\hbar)^2\sin^2(\delta t/2)/(\delta/2)^2$, which at long times sharpens into a delta function. Show, in two or three sentences, how summing this lineshape over a continuum with density $\rho(E)$ — using $\int \sin^2(\alpha t/2)/\alpha^2\,d\alpha = \pi t/2$ — converts the *oscillating* probability of the two-level problem into a *constant rate* $W$, recovering the golden rule. Name the single feature (a continuum vs. a discrete final state) that turns Rabi oscillation into irreversible decay.

**F3 — Discrimination.** You are given a transition and asked for "how fast it happens." Decide whether the right object is (i) an oscillating probability $P(t)$ from the Rabi formula, (ii) a constant rate $W$ from the golden rule, or (iii) zero (the transition is forbidden). State the checks that select between them.
*Note to instructor: the discriminating checks are (a) discrete final state vs. continuum — Rabi for discrete, golden rule for continuum — and (b) the selection rules — if $\Delta\ell \neq \pm1$ the E1 rate is zero; students who apply the golden rule to a forbidden transition and get a nonzero number have skipped the selection-rule check.*

**Closing reflection:** Across F1–F3, the golden-rule rate is a product of three ingredients. Which one is most often dropped or mis-powered, and what is the single cheapest check that catches the error before it reaches your report?

---

## Instructor Notes

**Common errors:**
- Mis-powering the $\omega$ factor (using $\omega^1$ or $\omega^2$ instead of $\omega^3$), or taking $\omega$ as an energy in eV rather than an angular frequency in rad/s — the dominant order-of-magnitude error.
- Dropping the $2\pi/\hbar$ prefactor in the golden rule.
- Computing a nonzero rate for a forbidden transition (e.g. treating $2s\to1s$ as if $\Delta\ell = 0$ were allowed), or getting the selection rules wrong ($\Delta\ell = \pm1$, $\Delta m = 0,\pm1$).

**Signs a student needs to return:**
- They cannot reconstruct the selection rules from the parity and azimuthal-integral arguments and instead recite them with errors.
- They report a lifetime in the wrong decade (ps or μs for an allowed optical transition) without recognizing the $\omega^3$ factor as the likely culprit.

**Scaffolding adjustments:** If a student struggles with Part A, have them first compute $A_{21}$ symbolically and verify the *units* reduce to $\text{s}^{-1}$ before plugging in numbers — unit-tracking catches the dropped-$\omega$ error early. If a student finishes Part F quickly, have them work the $3p\to1s$ vs $3p\to2s$ branching ratio and show the $\omega^3$ ratio (not the matrix-element ratio) is what makes $3p\to1s$ dominate.

**Domain adaptation note:** The three-ingredient structure ($|V_{fi}|^2$, $\rho(E)$, $\omega^3$) transfers to any spontaneous-emission problem — sodium D-lines, the 21-cm hydrogen line, or cavity-modified rates via the Purcell factor, where the density of states is engineered rather than free-space.
