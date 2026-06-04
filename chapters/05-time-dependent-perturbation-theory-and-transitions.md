# Chapter 5 — Time-Dependent Perturbation Theory and Transitions
*Why resonance is Fourier resonance, and why first-order perturbation theory predicts probabilities greater than one.*

January 1938. Columbia University. Isidor Rabi's group passes a beam of LiCl molecules through three magnets. The first selects a particular nuclear spin orientation. The second — the interaction region — carries an oscillating radio-frequency field. The third analyzes what comes out. As they sweep the RF frequency, something sharp happens at one specific value: the beam intensity drops. The molecules have been flipped — driven from one spin state to the other. The resonance is narrow and well-defined.

Here is what makes this worth understanding before doing the math. The two-state system Rabi was driving — a spin-up nuclear state and a spin-down nuclear state, separated by energy $\hbar\omega_0$, coupled by an oscillating perturbation — is physically identical to an atom in a laser field, an NMR sample in a coil, a superconducting qubit driven by a microwave pulse, a trapped ion being manipulated by a Raman laser pair, an electron spin in an ESR apparatus. Every quantum control experiment built since 1938 is Rabi's apparatus in different molecular handwriting. The two questions we will answer — what is the probability of finding the system in the excited state at time $t$, and when does perturbation theory give the right answer — work for all of them.

---

## The Interaction Picture

The Schrödinger equation for $\hat{H} = \hat{H}_0 + \hat{H}'(t)$ mixes two things: the eigenstates of $\hat{H}_0$ (which we know) and the perturbation (which is what we want to study). The interaction picture separates them.

Define a new state vector by rotating out the trivial $\hat{H}_0$ evolution:

$$|\tilde{\psi}(t)\rangle = e^{i\hat{H}_0 t/\hbar}\,|\psi(t)\rangle.$$

Substitute into the full Schrödinger equation. The $\hat{H}_0$ terms on both sides cancel exactly, leaving:

$$i\hbar\,\partial_t|\tilde{\psi}(t)\rangle = \tilde{H}'(t)\,|\tilde{\psi}(t)\rangle,$$

where $\tilde{H}'(t) = e^{i\hat{H}_0 t/\hbar}\hat{H}'(t)e^{-i\hat{H}_0 t/\hbar}$ is the perturbation in the interaction picture.

The interaction-picture state evolves only under $\hat{H}'(t)$. When $\hat{H}'(t) = 0$, it freezes completely. This is the point: all the interesting dynamics — the transitions we want to compute — lives in the perturbation. The fast $\hat{H}_0$ oscillations have been rotated away.

Expand in the unperturbed eigenstates $|n\rangle$:

$$|\tilde{\psi}(t)\rangle = \sum_n c_n(t)\,|n\rangle,$$

with initial condition $c_n(0) = \delta_{ni}$ (start in state $|i\rangle$). Project onto the final state $\langle f|$:

$$i\hbar\,\dot{c}_f = \sum_n c_n(t)\,\langle f|\hat{H}'(t)|n\rangle\,e^{i\omega_{fn}t},$$

where $\omega_{fn} = (E_f - E_n)/\hbar$ is the **Bohr frequency** for the $n \to f$ transition. This is exact. Every $c_f$ is coupled to every other $c_n$, which is why the full problem is hard. The factor $e^{i\omega_{fn}t}$ is the interaction-picture phase: the oscillation from $\hat{H}_0$ evolution is now explicit in the coupling equation rather than hidden in the state.

---

## The First-Order Amplitude and Why It Is a Fourier Transform

To solve the coupled equations, replace every $c_n(t)$ on the right-hand side with its initial value: $c_n(t) \approx \delta_{ni}$. This is the first-order approximation — treat the system as still mostly in $|i\rangle$ throughout. Integrate from 0 to $t$:

$$\boxed{c_f^{(1)}(t) = \frac{1}{i\hbar}\int_0^t\langle f|\hat{H}'(t')|i\rangle\,e^{i\omega_{fi}t'}\,dt'.}$$

The transition probability is $P_{i\to f}(t) = |c_f^{(1)}(t)|^2$.

Read this formula carefully. It says: the transition amplitude is the **Fourier transform** of the perturbation matrix element $\langle f|\hat{H}'(t)|i\rangle$, evaluated at the Bohr frequency $\omega_{fi} = (E_f - E_i)/\hbar$.

Resonance, in this framework, is Fourier resonance. The perturbation drives the transition efficiently when it has a Fourier component at the frequency that matches the energy difference between initial and final states. If the perturbation oscillates at the wrong frequency, the phase factor in the integral oscillates and the integral cancels. If it oscillates at $\omega_{fi}$, the integral accumulates coherently.

This interpretation generalizes immediately. A sudden kick (delta function in time) has a flat Fourier spectrum and drives all transitions equally. A slow quasi-static perturbation has a narrow spectrum near zero and drives nothing. A resonant sinusoidal perturbation drives the one transition it is tuned to. These are not three separate facts — they are three limits of the same formula.

---

## The Resonance Lineshape

Take $\hat{H}'(t) = \hat{V}\cos(\omega t)$. Write $\cos\omega t = \frac{1}{2}(e^{i\omega t} + e^{-i\omega t})$. Near resonance $\omega \approx \omega_{fi}$, one exponential combines with $e^{i\omega_{fi}t}$ to oscillate at $e^{i(\omega_{fi}+\omega)t}$ — rapidly varying, averaging to nearly zero over any appreciable time. The other combines to give $e^{i(\omega_{fi}-\omega)t}$ — slowly varying near resonance, building up coherently. Drop the fast term (the **rotating-wave approximation**, valid when $|V_{fi}| \ll \hbar\omega_0$) and the integral gives:

$$\boxed{P_{i\to f}(t) = \frac{|V_{fi}|^2}{\hbar^2}\cdot\frac{\sin^2\!\left[\frac{(\omega_{fi}-\omega)\,t}{2}\right]}{\left(\frac{\omega_{fi}-\omega}{2}\right)^2}.}$$

This is the **sinc-squared lineshape**. Several things to read off immediately.

At resonance ($\omega = \omega_{fi}$), take the $\delta\to 0$ limit where $\delta = \omega_{fi} - \omega$: the function $\sin^2(\delta t/2)/(\delta/2)^2 \to t^2$. So:

$$P_{i\to f}^\text{resonance}(t) = \frac{|V_{fi}|^2}{\hbar^2}\cdot\frac{t^2}{4}.$$

On-resonance probability grows as $t^2$. The peak height grows as $t^2$; the width to the first zero narrows as $2\pi/t$; the area under the central peak grows as $t$. In the limit $t\to\infty$, the sinc-squared sharpens into $(\pi t/2)\,\delta(\omega_{fi}-\omega)$ — a delta function at resonance whose coefficient grows linearly in time. This is the gateway to Fermi's golden rule.

**The failure mode.** At resonance, $P_{i\to f}(t) = |V_{fi}|^2 t^2/(4\hbar^2)$. This grows without bound. Eventually it exceeds 1. A probability exceeding 1 is not a numerical inconvenience — it is a diagnostic. The formula is announcing that first-order perturbation theory has broken.

The cause is the approximation $c_i(t) \approx 1$ throughout the integration. Once probability flows into $|f\rangle$, the population in $|i\rangle$ has decreased, and the rate of further transfer should slow. The first-order equations ignore this depletion: they keep drawing from $|i\rangle$ as though nothing has changed. The exact two-level solution accounts for the feedback. First-order PT does not.

<!-- → [CHART: sinc-squared lineshape P(δ, T) vs. detuning δ for three values of T — showing the central peak sharpening as T increases, with annotations for peak height ∝ T², width ∝ 1/T, and area ∝ T; the evolution toward a delta function should be visible; this is the key figure connecting finite-time perturbation to the Fermi golden rule limit] -->

![sinc-squared lineshape P(δ, T) vs. detuning δ for three values of T — showing the central peak sharpening as T increases, with annotations…](../images/05-time-dependent-perturbation-theory-and-transitions-fig-01.png)
*Figure 5.1 — sinc-squared lineshape P(δ, T) vs. detuning δ for three values of T — showing the central peak sharpening as T increases, with annotations…*

---

## The Exact Rabi Solution

The two-level problem has an exact analytical solution. Two states $|g\rangle$ and $|e\rangle$, energies 0 and $\hbar\omega_0$. Drive Hamiltonian:

$$\hat{H}'(t) = \hbar\Omega\cos(\omega t)\,(|e\rangle\langle g| + |g\rangle\langle e|).$$

The quantity $\Omega = |V_{fi}|/\hbar$ is the **Rabi frequency**. In the rotating-wave approximation, the Schrödinger equation reduces to two coupled first-order ODEs:

$$\dot{c}_g = -\frac{i\Omega}{2}\,e^{-i\Delta t}\,c_e, \qquad \dot{c}_e = -\frac{i\Omega}{2}\,e^{+i\Delta t}\,c_g,$$

where $\Delta = \omega - \omega_0$ is the **detuning**. These can be solved exactly by differentiating to get a second-order ODE, then applying initial conditions $c_g(0) = 1$, $c_e(0) = 0$. The result:

$$\boxed{P_{g\to e}(t) = \frac{\Omega^2}{\Omega^2+\Delta^2}\,\sin^2\!\left(\frac{\sqrt{\Omega^2+\Delta^2}}{2}\,t\right).}$$

This is the **Rabi formula**. It is exact within the RWA — no perturbative approximation.

Define the **generalized Rabi frequency** $\Omega_\text{gen} = \sqrt{\Omega^2 + \Delta^2}$. Then:

$$P_{g\to e}(t) = \frac{\Omega^2}{\Omega_\text{gen}^2}\,\sin^2\!\left(\frac{\Omega_\text{gen}\,t}{2}\right).$$

**On resonance** ($\Delta = 0$, $\Omega_\text{gen} = \Omega$):

$$P_{g\to e}(t) = \sin^2\!\left(\frac{\Omega t}{2}\right).$$

The population oscillates between 0 and 1. At $t = \pi/\Omega$ — a **$\pi$-pulse** — the entire population is in $|e\rangle$. At $t = 2\pi/\Omega$ it is back in $|g\rangle$. This is Rabi oscillation. It is what Rabi's molecular beam showed in 1938. It is what every qubit readout protocol relies on today.

**Off resonance** ($\Delta \neq 0$): the maximum achievable probability is $\Omega^2/(\Omega^2+\Delta^2) < 1$. Full population transfer is impossible away from resonance. The oscillation is faster (frequency $\Omega_\text{gen} > \Omega$) but shallower. Resonance is required for complete inversion.

**Comparison to first-order PT at resonance.** PT gives $P^\text{PT}_{g\to e}(t) = (\Omega t/2)^2$ — a parabola. The exact formula gives $\sin^2(\Omega t/2)$ — a bounded oscillation. For $\Omega t \ll 1$, expand $\sin^2 x \approx x^2$: the two agree. For $\Omega t \sim 1$, they diverge badly. At the first $\pi$-pulse ($\Omega t = \pi$): exact $P = 1$; PT predicts $(\pi/2)^2 \approx 2.47$. PT has predicted a probability of 247%.

Why PT fails is worth stating precisely. PT assumes the amplitude in $|i\rangle$ is constant — $c_i(t) \approx 1$ — even as probability drains out of it. The exact solution feeds the depleted $|i\rangle$ population back in during the return half of the Rabi cycle; PT misses the return entirely. The regime of validity is $\Omega t \ll 1$: small coupling times short time. Outside that window, use the Rabi formula.

<!-- → [CHART: Rabi oscillation vs. PT parabola — two-panel figure: (left) on resonance, showing sin²(Ωt/2) and (Ωt/2)² on the same axes with a dashed horizontal line at P=1, the PT curve rising above it, and a red label "PT invalid" after the crossing; (right) off resonance at Δ=2Ω, showing the capped oscillation at max P=1/5 from the Rabi formula vs. the PT approximation; this is the central diagnostic figure of the chapter] -->

![Rabi oscillation vs. PT parabola — two-panel figure: (left) on resonance, showing sin²(Ωt/2) and (Ωt/2)² on the same axes with a dashed…](../images/05-time-dependent-perturbation-theory-and-transitions-fig-02.png)
*Figure 5.2 — Rabi oscillation vs. PT parabola — two-panel figure: (left) on resonance, showing sin²(Ωt/2) and (Ωt/2)² on the same axes with a dashed…*

---

## Worked Example: The $\pi$-Pulse and the PT Breakdown

A two-level atom with transition energy $\hbar\omega_0 = 2.00$ eV is driven by a resonant laser. The coupling strength is $\hbar\Omega = 0.010$ eV. The atom starts in the ground state.

**When does the atom first reach $P = 1$?** On resonance, $\sin^2(\Omega t/2) = 1$ when $\Omega t/2 = \pi/2$, so $t_\pi = \pi/\Omega$.

Converting: $\Omega = (0.010\,\text{eV}\times1.602\times10^{-19}\,\text{J/eV})/(1.055\times10^{-34}\,\text{J·s}) = 1.519\times10^{13}$ rad/s.

$$t_\pi = \frac{\pi}{1.519\times10^{13}} \approx 2.07\times10^{-13}\,\text{s} = 0.21\,\text{ps.}$$

**When does first-order PT predict $P = 1$, and what is the exact probability at that moment?** PT predicts $(\Omega t/2)^2 = 1$ when $\Omega t/2 = 1$, so $t_\text{PT} = 2/\Omega \approx 0.13$ ps.

At $t = t_\text{PT}$, the exact probability is:

$$P_{g\to e}(t_\text{PT}) = \sin^2\!\left(\frac{\Omega \cdot t_\text{PT}}{2}\right) = \sin^2(1) \approx 0.708.$$

At the moment PT declares complete population transfer, the real atom has moved only 71% of its population into the excited state. The remaining 29% is still in the ground state, and the Rabi oscillation is about to carry it back. PT missed the return entirely because it assumed $c_g = 1$ throughout.

**The coupling-strength limit.** If instead $\hbar\Omega = 10^{-6}$ eV, the $\pi$-pulse time grows by a factor of $10^4$, to about 2100 ps. More importantly, the window $\Omega t \ll 1$ — where PT is accurate — now covers most of the evolution before spontaneous emission destroys the coherence. In that regime, first-order PT is reliable for all practical purposes. PT fails not because coupling is "small" in some abstract sense but because the product $\Omega t$ approaches 1. Time matters as much as coupling strength.

---

## From Discrete to Continuum: Fermi's Golden Rule in Preview

The sinc-squared lineshape at long times sharpens into a delta function. For a transition into a single discrete state, this would mean an infinitely narrow resonance — fine structure in the spectrum. But real atoms emit photons into the vacuum: infinitely many electromagnetic modes, forming a continuum, each slightly different in frequency. When there is a continuum of final states, the delta function is always satisfied: there is always some mode whose frequency matches the transition energy, and the rate of transition becomes constant rather than oscillatory.

Summing the first-order transition rates over a continuum of final states with density $\rho(E)$:

$$\Gamma_{i\to f} = \frac{2\pi}{\hbar}|V_{fi}|^2\,\rho(E_f)\Big|_{E_f = E_i + \hbar\omega}.$$

This is Fermi's golden rule. It gives the *rate* (probability per unit time) of an irreversible transition, rather than the oscillating probability of the two-level problem. The discreteness of the initial problem — coherent Rabi oscillations — has collapsed into an exponential decay. The lifetime $\tau = 1/\Gamma$ of the excited state is the inverse transition rate.

The transition from Rabi oscillation to Fermi golden rule decay is not a sudden change of physics. It is what happens as the number of available final states grows: the oscillations of the individual transition amplitudes add up destructively at all times except the first, leaving only the initial linear rise. A discrete problem with many modes is an intermediate case — almost continuum but not quite, showing oscillatory behavior at long times that a true continuum would not.

Chapter 6 derives Fermi's golden rule formally and applies it to atomic emission. What matters here is recognizing where it comes from: the same first-order formula, applied to a continuum rather than a single final state.

---

## Exercises

**Warm-up**

1. *Difficulty: Warm-up — tests the interaction picture transformation.*
   A harmonic oscillator ($m$, $\omega$) in state $|0\rangle$ receives a short kick: $\hat{H}'(t) = F\hat{x}\,\delta(t)$ with $F$ small. Using $\hat{x} = \sqrt{\hbar/2m\omega}(\hat{a}_+ + \hat{a}_-)$: (a) compute the first-order transition amplitude $c_1^{(1)}(\infty)$ to the first excited state (the time integral of $\delta(t)e^{i\omega_{10}t}$ evaluated at $t=0$ is 1); (b) show the transition probability is $P_{0\to1} = F^2/(2m\omega\hbar)$; (c) state the condition on $F$ for first-order PT to be valid and explain what it means physically — is it a condition on $F$ alone, or on $F$ combined with time?
   *Tests: executing the first-order integral for a delta-function perturbation; extracting the validity condition.*

2. *Difficulty: Warm-up — tests the Rabi formula at and away from resonance.*
   A two-level system ($\hbar\omega_0 = 5.0$ eV, $\hbar\Omega = 0.05$ eV) is driven by an oscillating field. (a) Compute the generalized Rabi frequency $\Omega_\text{gen} = \sqrt{\Omega^2+\Delta^2}$ at detunings $\Delta = 0$, $\Omega$, and $2\Omega$. (b) For each detuning, compute the maximum transition probability $P_\text{max} = \Omega^2/(\Omega^2+\Delta^2)$. (c) At $\Delta = 2\Omega$, by what factor is the maximum probability suppressed relative to on-resonance?
   *Tests: numerical command of the Rabi formula; understanding how detuning caps the maximum achievable probability.*

3. *Difficulty: Warm-up — tests the Fourier interpretation of the transition amplitude.*
   Explain in two or three sentences why a sudden perturbation (delta function in time) drives all transitions with equal probability, while a slow quasi-static perturbation drives almost none. Your answer should invoke the Fourier transform interpretation of the first-order amplitude and identify what "Fourier component at the Bohr frequency" means in each case.
   *Tests: physical interpretation of the first-order formula as a Fourier transform; distinguishing sudden from adiabatic limits.*

**Application**

4. *Difficulty: Application — the PT breakdown criterion.*
   For the worked example ($\hbar\omega_0 = 2.00$ eV, $\hbar\Omega = 0.010$ eV), first-order PT is reliable while the exact and PT probabilities agree within 10%. (a) Using the expansion $\sin^2 x \approx x^2 - x^4/3$ for the exact formula and $x^2$ for PT, find the leading correction and estimate the time $t_{10\%}$ at which the fractional difference first reaches 10%. (b) Express $t_{10\%}$ as a multiple of the Bohr oscillation period $2\pi/\omega_0$. Is PT valid for many or few Bohr periods? (c) Now reduce the coupling to $\hbar\Omega = 10^{-4}$ eV. By what factor does $t_{10\%}$ change?
   *Tests: deriving the leading correction to PT; connecting the validity window to the coupling strength and Bohr period.*

5. *Difficulty: Application — sinc-squared lineshape and spectral selectivity.*
   A perturbation $\hat{H}'(t) = \hat{V}\cos(\omega t)$ is applied to a two-level atom for a finite duration $T$. (a) Show that the first-order transition probability as a function of detuning $\delta = \omega_{fi} - \omega$ is $P(\delta, T) = (|V_{fi}|/\hbar)^2\sin^2(\delta T/2)/(\delta/2)^2$. (b) At what values of $\delta$ do the first zeros of the sinc-squared function appear? (c) A researcher wants to drive a transition selectively — with less than 1% excitation of a neighboring transition at detuning $\delta_0 = 10^9$ rad/s from resonance. What minimum pulse duration $T$ is required? (d) What is the trade-off between spectral selectivity (long $T$) and perturbation theory validity (short $T$) for a fixed coupling strength?
   *Tests: deriving the sinc-squared formula; connecting pulse duration to spectral resolution; identifying the PT validity / selectivity trade-off.*

6. *Difficulty: Application — sudden vs. adiabatic.*
   An oscillator (frequency $\omega$) in state $|n\rangle$ is subjected to $\hat{H}'(t) = \lambda\hat{x}^2 f(t)$, where $f(t)$ rises slowly from 0 to 1 over timescale $\tau_\text{on} \gg 1/\omega$ (adiabatic turn-on) and then falls suddenly to 0 over $\tau_\text{off} \ll 1/\omega$ (sudden turn-off). (a) Which part of this protocol — turn-on or turn-off — drives transitions? Justify using the Fourier-transform interpretation. (b) Which limit drives more transitions, and why? (c) For the sudden part, estimate the transition amplitude to the state $|n\pm2\rangle$ (note: $\hat{x}^2$ connects states differing by 0 or 2 quanta) using the first-order formula.
   *Tests: distinguishing sudden from adiabatic limits physically; applying the first-order formula to the sudden case.*

**Synthesis**

7. *Difficulty: Synthesis — strong coupling: comparison table.*
   A two-level atom has $\hbar\Omega = 0.5\,\hbar\omega_0$ (strong coupling). (a) Write the on-resonance exact Rabi formula and the first-order PT formula. (b) Compute both at $\Omega t = \pi/4$, $\pi/2$, $\pi$, and $3\pi/2$; present as a table. (c) At what time does PT first exceed 1? (d) At $\Omega/\omega_0 = 0.5$, the rotating-wave approximation is marginal. The leading correction from the counter-rotating term is the Bloch–Siegert shift of order $\Omega^2/\omega_0$. Estimate its magnitude as a fraction of $\omega_0$ for this coupling.
   *Tests: full numerical comparison of exact vs. PT; identifying PT failure; estimating the Bloch–Siegert correction beyond the RWA.*

8. *Difficulty: Synthesis — qubit gate design.*
   A superconducting transmon qubit has transition frequency $\omega_0/(2\pi) = 5.0$ GHz and coherence time $T_2 = 80\,\mu$s. A microwave pulse with Rabi frequency $\Omega/(2\pi) = 10$ MHz is applied on resonance. (a) Compute $t_\pi = \pi/\Omega$ for the $\pi$-pulse. (b) How many Rabi periods fit within $T_2$? (c) Check whether first-order PT is valid during the $\pi$-pulse ($\Omega t_\pi \ll 1$?). (d) The gate fidelity requires the population transfer to be within $10^{-3}$ of 1. Show that the exact Rabi formula achieves this while PT cannot even be evaluated at $t = t_\pi$ without predicting an unphysical result. Explain why the experiment requires the exact formula.
   *Tests: realistic qubit numbers; checking PT validity quantitatively; connecting the breakdown to gate fidelity requirements.*

**Challenge**

9. *Difficulty: Challenge — the Landau–Zener formula as a TDPT boundary.*
   A two-level system has energies $E_\pm(t) = \pm\frac{1}{2}\alpha t$ that sweep linearly through degeneracy at $t = 0$, with off-diagonal coupling $V_{12} = V$ (constant). The Landau–Zener transition probability for sweeping from $t = -\infty$ to $t = +\infty$ is $P_\text{LZ} = 1 - e^{-2\pi\gamma}$ where $\gamma = |V|^2/(\hbar^2\alpha)$. (a) In the limit $\gamma \ll 1$ (slow sweep or weak coupling), expand $P_\text{LZ}$ to leading order in $\gamma$ and show $P_\text{LZ} \approx 2\pi\gamma$. (b) Estimate this same probability from first-order perturbation theory: compute $|c_f^{(1)}(+\infty)|^2$ for the matrix element $\langle +|V|-\rangle e^{i\phi(t)}$ where $\phi(t) = \int_0^t \alpha t'\,dt'/\hbar = \alpha t^2/(2\hbar)$ (the stationary-phase integral). The result is a Gaussian in the time domain; its Fourier transform at $\omega = 0$ gives an integral proportional to $|V|^2/(\hbar^2\alpha)$. (c) Show that PT gives the correct leading-order result, confirming $P_\text{LZ} \approx 2\pi\gamma$ for $\gamma \ll 1$. (d) In the limit $\gamma \gg 1$ (adiabatic passage), $P_\text{LZ} \approx 1$ — almost complete transfer. Why does PT break down completely in this limit?
   *Tests: connecting the Landau–Zener formula to TDPT; showing PT works in one limit but not the other; the stationary-phase integral.*

---

## LLM Exercises

The following exercises are designed to be worked with a large language model as a thinking partner — not to obtain derivations, but to probe reasoning, test intuition, and press on the limits of what the chapter established.

1. Ask an LLM to explain the rotating-wave approximation (RWA) in physical terms: what is the counter-rotating term, why does it average to near-zero near resonance, and when does it matter? Ask for the condition $\Omega \ll \omega_0$ to be justified quantitatively. Then ask: what physical effect — measurable in the lab — is the leading consequence of the counter-rotating term that the RWA misses?

2. Ask an LLM to derive the Rabi formula from the coupled amplitude equations. The derivation should: write the two coupled ODEs for $c_g$ and $c_e$ in the RWA, differentiate one equation to get a second-order ODE, solve with the given initial conditions, and arrive at $P_{g\to e}(t) = (\Omega/\Omega_\text{gen})^2\sin^2(\Omega_\text{gen}t/2)$. Check each step.

3. The chapter claims the first-order transition amplitude is a Fourier transform of the perturbation matrix element at the Bohr frequency. Ask an LLM to make this explicit: write the first-order formula as a convolution or Fourier integral, identify the time window (0 to $t$) as a rectangular window function, and explain how the finite-time sinc-squared lineshape becomes a delta function as $t\to\infty$. Ask it to connect this to the time-energy uncertainty relation.

4. Ask an LLM to explain Fermi's golden rule from the sinc-squared formula — how summing over a continuum of final states at density $\rho(E)$ converts the oscillating sinc-squared into a constant rate. The explanation should show the integral that converts $\sum_f P_{i\to f}(t)$ to $W \cdot t$. Then ask: why does this derivation require both "the perturbation matrix element varies slowly over the width of the sinc-squared peak" and "the density of states varies slowly"? What breaks if either condition fails?

5. Ask an LLM to compare the Rabi formula to the quantum harmonic oscillator problem: in both cases a two-level (or multi-level) system is driven by a periodic perturbation, yet the harmonic oscillator is exactly solvable while the two-level system needs the RWA. Ask it to identify what feature of the harmonic oscillator makes it exactly solvable without approximation, and why the two-level system does not share this feature.

---

## References

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §10.1–10.2.

Sakurai, J. J., & Napolitano, J. (2021). *Modern Quantum Mechanics* (3rd ed.). Cambridge University Press. §5.5–5.6.

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. Ch. 14.

Cohen-Tannoudji, C., Diu, B., & Laloë, F. (1977). *Quantum Mechanics*, Vol. II. Wiley. Ch. XIII.

Rabi, I. I., Millman, S., Kusch, P., & Zacharias, J. R. (1939). The molecular beam resonance method for measuring nuclear magnetic moments. *Physical Review*, 55, 526–535.

Bloch, F., & Siegert, A. (1940). Magnetic resonance for nonrotating fields. *Physical Review*, 57, 522–527.

Landau, L. (1932). Zur Theorie der Energieübertragung. II. *Physik. Z. Sowjetunion*, 2, 46.

Zener, C. (1932). Non-adiabatic crossing of energy levels. *Proceedings of the Royal Society of London A*, 137, 696–702.

---

## Running Project — Model a Real Quantum System, End to End

**This chapter adds:** time-dependent perturbation theory and the exact Rabi solution to the toolkit, with two small parameters — the RWA condition $\Omega/\omega_0 \ll 1$ and the PT-validity window $\Omega t \ll 1$ — and it supplies the complete model for the capstone's **System D — NMR $^1$H qubit Rabi oscillations**.

Today's table entry: **time-dependent PT / Rabi — $\varepsilon_\text{RWA} = \Omega/\omega_0 \ll 1$ (drop the counter-rotating term) and $\varepsilon_\text{PT} = \Omega t \ll 1$ (first-order PT) — first-order PT breaks when $\Omega t \sim 1$ (it predicts $P>1$); the exact Rabi formula stays valid within the RWA; the RWA itself breaks at large $\Omega/\omega_0$ via the Bloch-Siegert shift.** The crucial lesson for the capstone: *time matters as much as coupling strength* — PT fails not because $\Omega$ is "large" but because the product $\Omega t$ reaches 1.

### Exercise R1 — When to Use AI
**The judgment:** In this chapter's project work, AI assistance is appropriate for:
- Computing the Rabi frequency $\Omega_R = \gamma_p B_1/2$, the $\pi$-pulse time $t_\pi = \pi/\Omega_R$, and the generalized $\tilde\Omega = \sqrt{\Omega_R^2+\delta^2}$ for given fields — *Why AI works here:* direct plug-ins checkable against the published 400 MHz NMR $\pi$-pulse range (1–25 μs).
- Plotting the exact Rabi $\sin^2(\tilde\Omega t/2)$ against the first-order PT parabola $(\Omega t/2)^2$ — *Why AI works here:* it scaffolds a plot whose crossing point you can verify analytically.
- Computing the off-resonance ceiling $P_\text{max} = \Omega_R^2/\tilde\Omega^2$ — *Why AI works here:* a one-line formula, checkable by hand.

**The tell:** You are using AI well when you have an independent check — here, the exact Rabi formula caps $P$ at 1, so any PT result exceeding 1 is a known diagnostic, not a surprise.

### Exercise R2 — When NOT to Use AI
**The judgment:** These tasks require your judgment; AI output here can't be trusted without redoing the work:
- Deciding whether to use first-order PT or the exact Rabi formula for *your* pulse — checking $\Omega t$ against 1 — *Why AI fails here:* it will apply first-order PT through a full $\pi$-pulse and report $P=(\pi/2)^2\approx 2.47$ without flagging that a probability of 247% means the method has broken. This is the small-parameter (here, $\Omega t$) call.
- Judging whether the RWA holds — checking $\Omega/\omega_0$ — *Why AI fails here:* at $\Omega/\omega_0 \sim 0.5$ the RWA is marginal and the Bloch-Siegert shift ($\sim\Omega^2/\omega_0$) matters; the AI will keep using the RWA result silently.
- Attributing the residual error in real NMR ($T_1$, $T_2$ relaxation, multi-spin complexity) — *Why AI fails here:* the breakdown analysis needs you to estimate which decoherence channel dominates at your sample, not a generic list.

**The tell:** If you could not explain the result without the AI — if the AI is your *reason* rather than your *tool* — it did work that should have been yours.

**Physics-judgment connection:** This trains checking a *product* small parameter ($\Omega t$, not $\Omega$ alone) before choosing a method, and comparing a computed $\pi$-pulse time against a cited measured range — the discipline that catches a "probability of 247%" before it reaches your report.

### Exercise R3 — LLM Exercise
**What you're building this chapter:** moves 2–3 of the capstone's System D (NMR Rabi) — method selection by the RWA/$\Omega t$ conditions and the $t_\pi$ calculation — plus the Rabi table row.
**Tool:** Claude Project — your third full five-move candidate.
**The Prompt:**
```
I am drafting a five-move quantum model of NMR proton Rabi oscillations at a
400 MHz instrument. Help me with moves 2-3 (method selection, calculation);
I will write moves 1, 4, 5.

METHOD SELECTION: justify the rotating-wave approximation by computing the
small parameter Omega_R/omega_0 and showing it is ~0.003 << 1 for B0=9.4 T,
B1=1e-2 T. Then state the SECOND condition that governs whether first-order
PT (vs the exact Rabi formula) is valid: Omega_R * t << 1. Make clear that for
a pi-pulse Omega_R*t = pi, so first-order PT is INVALID and the exact Rabi
formula is required.

CALCULATION: with gamma_p = 2.675e8 rad/s/T, B0=9.4 T, B1=1e-2 T:
compute the Larmor frequency, Omega_R = gamma_p B1 / 2, and t_pi = pi/Omega_R
in microseconds. Show units.

Do NOT report a first-order PT probability for the full pi-pulse as if it were
physical (it exceeds 1). Do NOT judge whether my final agreement with measured
pi-pulse times is "good".
```
**What this produces:** $\Omega_R \approx 1.34\times10^6$ rad/s, $t_\pi \approx 2.3$ μs, ready to validate against the measured 1–25 μs range.
**How to adapt:** *Your system:* for a transmon qubit, swap $\gamma_p B_1/2$ for the drive Rabi frequency but keep the same two-condition argument. *ChatGPT/Gemini:* watch for it reporting the $(\pi/2)^2$ PT value as a real probability. *Claude Project:* store as System D.
**Builds on:** Chapters 3–4 (helium, STM) — three candidates now, three different methods.  **Next:** Chapter 6 takes the same first-order amplitude to a continuum (Fermi golden rule) and a decay rate.

### Exercise R4 — CLI Exercise
**What you're building this chapter:** the Rabi table row and a script that compares exact Rabi vs first-order PT and computes $t_\pi$.
**Tool:** Claude Code
**Skill level:** Intermediate
**Setup — confirm:**
- [ ] `method-table.md` with Ch 1–4 rows.
- [ ] Python 3 + numpy.
- [ ] `CLAUDE.md` rule: "First-order TDPT is valid only while Omega*t << 1; report any P>1 as a method-breakdown flag, never as a probability."
**The Task:**
```
In the running-project directory:
1. Append the time-dependent-PT/Rabi row to method-table.md (note BOTH small
   parameters: Omega/omega_0 for RWA, Omega*t for first-order PT).
2. Create rabi_nmr.py that:
   - computes Omega_R = gamma_p*B1/2 and t_pi = pi/Omega_R (gamma_p=2.675e8,
     B1=1e-2 T); prints t_pi in microseconds,
   - tabulates exact P=sin^2(Omega_R t/2) and PT P=(Omega_R t/2)^2 at
     Omega_R t = pi/4, pi/2, pi, 3pi/2,
   - flags the first Omega_R t at which the PT value exceeds 1,
   - confirms Omega_R/omega_0 << 1 for the RWA (omega_0 = 2*pi*400e6).
3. Run it. Confirm t_pi ~ 2.3 us, exact P caps at 1, and PT exceeds 1 near
   Omega_R t = 2.
Touch no files outside this directory. Report t_pi and the Omega_R t where PT
first exceeds 1.
```
**Expected output:** appended row; console showing $t_\pi\approx 2.3$ μs, the exact/PT comparison table, and PT crossing 1 near $\Omega_R t = 2$.
**What to inspect:** exact $P$ never exceeds 1; PT and exact agree for $\Omega_R t \ll 1$ and diverge by the $\pi$-pulse; $\Omega_R/\omega_0 \approx 0.003$ confirms the RWA.
**If it goes wrong:** if $t_\pi$ comes out in nanoseconds or seconds, $\Omega_R$ used $\gamma_p B_1$ instead of $\gamma_p B_1/2$, or a factor of $2\pi$ slipped — print $\Omega_R$ in rad/s and check it is $\sim 10^6$.
**CLAUDE.md / AGENTS.md note:** add "A transition probability greater than 1 is a breakdown signal of first-order TDPT, not a result — switch to the exact Rabi formula."

### Exercise R5 — AI Validation Exercise
**What you're validating:** the R3/R4 Rabi numbers — $t_\pi$ and the exact-vs-PT comparison.
**Validation type:** Numerical result
**Risk level:** Medium — the formulas are exact within the RWA, but factor-of-2 and $2\pi$ slips in $\Omega_R$ are common and the PT-vs-exact distinction is easy to blur.
**Setup:** use your R4 output.
**The Validation Task:** Evaluate against this checklist; mark Pass / Fail / Cannot determine with reasoning.
```
Validation Checklist — Time-Dependent PT and Rabi
□ Correctness: is t_pi ~ 2.3 us, consistent with the measured 1-25 us range?
□ Completeness: are BOTH small parameters reported (Omega/omega_0 for RWA,
  Omega*t for first-order PT)?
□ Scope: is any P>1 flagged as a breakdown, not reported as a probability?
□ Cap: does the exact Rabi P stay <= 1 at every tabulated Omega_R t?
□ RWA: is Omega_R/omega_0 ~ 0.003 << 1 confirmed numerically?
□ Failure-mode check: any of —
  - fluent but wrong (PT value (pi/2)^2=2.47 reported as a real probability)
  - factor-of-2: Omega_R = gamma_p B1 instead of gamma_p B1/2
  - 2*pi slip between frequency (Hz) and angular frequency (rad/s)
  - off-resonance ceiling Omega^2/(Omega^2+delta^2) omitted when delta != 0
```
**What to do with findings:** pass → record $t_\pi$ as System D's calculation move; cite the measured range. one fail → fix the factor/conversion, re-run, document. multiple fails → recompute $\Omega_R$ by hand.
**AI Use Disclosure (mandatory, two sentences):**
> *1:* What AI produced and how you used it.
> *2:* One specific thing the AI could not determine that required your judgment.
**Physics-judgment connection:** this validation trains recognizing an unphysical result ($P>1$) as a method-breakdown signal and checking a computed timescale against a cited measured range — the discipline of knowing when your approximation has left its validity window.
