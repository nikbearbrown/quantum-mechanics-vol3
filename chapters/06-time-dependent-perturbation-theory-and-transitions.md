# Chapter 6 — Time-Dependent Perturbation Theory and Transitions

## TL;DR

- When a quantum system is nudged by a time-varying perturbation, the first-order transition amplitude is literally a Fourier transform of the perturbation matrix element evaluated at the Bohr frequency. Resonance is Fourier resonance.
- The exact two-level solution — the Rabi formula — shows what first-order perturbation theory misses: coherent oscillation between states that continues long after PT has predicted probabilities greater than 1.
- First-order PT is valid when $\Omega t \ll 1$. Outside that window, use the Rabi formula. The simulation makes the moment of failure visible.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Remember** the interaction picture and state what it disentangles from the full Schrödinger equation. [Bloom: Remember]
2. **Derive** the first-order transition amplitude from the coupled amplitude equations and interpret it as a Fourier transform. [Bloom: Understand/Apply]
3. **Compute** transition probabilities using the sinc-squared resonance lineshape, and identify the regime in which the formula breaks. [Bloom: Apply]
4. **Apply** the exact Rabi formula to predict the time of a $\pi$-pulse, the maximum off-resonance probability, and the generalized Rabi frequency. [Bloom: Apply]
5. **Diagnose** when first-order perturbation theory has failed by comparing the PT parabola to the Rabi oscillation — and state the physical reason for the failure. [Bloom: Analyze]

---

January 1938. Columbia University. Isidor Rabi's group passes a beam of LiCl molecules through three magnets. The first magnet selects a particular nuclear spin orientation. The second — the interaction region — carries an oscillating radio-frequency field. The third analyzes what comes out. As they sweep the RF frequency, something happens at one specific value: the beam intensity drops sharply. The molecules have been flipped — driven from one spin state to the other by the oscillating field. The resonance is narrow, well-defined, and theoretically predicted. Rabi won the Nobel Prize in 1944.

Here is what makes this worth understanding before doing the math. The two-state system Rabi was driving — a spin-up nuclear state and a spin-down nuclear state, separated by energy $\hbar\omega_0$, coupled by an oscillating perturbation — is physically identical to an atom in a laser field, an NMR sample in a coil, a superconducting qubit driven by a microwave pulse, a trapped ion being manipulated by a Raman laser pair, an electron spin in an ESR apparatus. Every quantum control experiment built since 1938 is Rabi's apparatus in different molecular handwriting. The two questions we will answer — what is the probability of finding the system in the excited state at time $t$, and when does perturbation theory give the right answer — will work for all of them.

---

## The Interaction Picture

The Schrödinger equation for a system with $\hat{H} = \hat{H}_0 + \hat{H}'(t)$ mixes two things: the eigenstates of $\hat{H}_0$ (which we know) and the perturbation (which is the thing we want to study). The interaction picture separates them.

Define a new state vector by rotating out the trivial $\hat{H}_0$ evolution:

$$|\tilde\psi(t)\rangle = e^{i\hat{H}_0 t/\hbar}\,|\psi(t)\rangle.$$

Substitute this into the Schrödinger equation $i\hbar\,\partial_t|\psi\rangle = (\hat{H}_0 + \hat{H}'(t))|\psi\rangle$. The $\hat{H}_0$ terms from the left- and right-hand sides cancel exactly, leaving:

$$i\hbar\,\partial_t|\tilde\psi(t)\rangle = \tilde{H}'(t)\,|\tilde\psi(t)\rangle,$$

where the interaction-picture perturbation is:

$$\tilde{H}'(t) = e^{i\hat{H}_0 t/\hbar}\,\hat{H}'(t)\,e^{-i\hat{H}_0 t/\hbar}.$$

The interaction-picture state evolves only under the perturbation $\tilde{H}'(t)$. When $\hat{H}'(t) = 0$, it freezes. This is the point: all the interesting dynamics — the transitions we want to compute — lives in the perturbation. The fast $\hat{H}_0$ oscillations have been rotated away.

Now expand in the unperturbed eigenstates $|n\rangle$:

$$|\tilde\psi(t)\rangle = \sum_n c_n(t)\,|n\rangle,$$

with initial condition $c_n(0) = \delta_{ni}$ (the system starts in state $|i\rangle$). Project the interaction-picture equation onto the final state $\langle f|$:

$$i\hbar\,\dot{c}_f = \sum_n c_n(t)\,\langle f|\hat{H}'(t)|n\rangle\,e^{i\omega_{fn}t},$$

where $\omega_{fn} = (E_f - E_n)/\hbar$ is the **Bohr frequency** for the $n \to f$ transition. This is exact. Nothing has been approximated yet. Every $c_f$ is coupled to every other $c_n$, which is why the exact problem is hard. The term $e^{i\omega_{fn}t}$ is the interaction-picture phase factor: the oscillation that was part of $\hat{H}_0$ evolution is now explicit in the coupling equation.

---

## The First-Order Transition Amplitude

To solve the coupled equations approximately, replace every $c_n(t)$ on the right-hand side by its initial value: $c_n(t) \approx \delta_{ni}$. This is the **first-order approximation** — we are treating the system as still mostly in $|i\rangle$ throughout. Integrate from $0$ to $t$:

$$\boxed{c_f^{(1)}(t) = \frac{1}{i\hbar}\int_0^t \langle f|\hat{H}'(t')|i\rangle\,e^{i\omega_{fi}t'}\,dt'.}$$

The transition probability to first order is $P_{i\to f}(t) = |c_f^{(1)}(t)|^2$.

Read this formula carefully. It says: the transition amplitude is the **Fourier transform** of the matrix element $\langle f|\hat{H}'(t)|i\rangle$, evaluated at the Bohr frequency $\omega_{fi} = (E_f - E_i)/\hbar$. Resonance, in this framework, is not a mysterious quantum phenomenon — it is Fourier resonance. The perturbation drives the transition efficiently when it has a Fourier component at the frequency that matches the energy difference between initial and final states. If the perturbation oscillates at the wrong frequency, the integral cancels. If it oscillates at $\omega_{fi}$, the integral accumulates.

This is the lesson that generalizes. A sudden kick (delta-function in time) has a flat Fourier spectrum and drives all transitions; a slow quasi-static perturbation has a narrow spectrum near zero and drives nothing; a resonant sinusoidal perturbation drives the one transition it is tuned to.

---

## The Resonance Lineshape

Take $\hat{H}'(t) = \hat{V}\cos(\omega t)$. Near resonance $\omega \approx \omega_{fi}$, write $\cos(\omega t) = \frac{1}{2}(e^{i\omega t} + e^{-i\omega t})$. One exponential oscillates at $e^{i(\omega_{fi}+\omega)t}$ — rapidly varying and averaging to near-zero over time. The other oscillates at $e^{i(\omega_{fi}-\omega)t}$ — slowly varying near resonance, building up coherently. Dropping the fast (**counter-rotating**) term — the **rotating-wave approximation** (RWA), valid when $|V_{fi}|/\hbar\omega_0 \ll 1$ — and computing $|c_f^{(1)}|^2$:

$$\boxed{P_{i\to f}(t) = \frac{|V_{fi}|^2}{\hbar^2}\cdot\frac{\sin^2\!\left[\frac{(\omega_{fi}-\omega)\,t}{2}\right]}{\left(\frac{\omega_{fi}-\omega}{2}\right)^2}.}$$

Here $V_{fi} = \langle f|\hat{V}|i\rangle$ is the matrix element of the time-independent part of the perturbation.

This is the **sinc-squared lineshape** (sometimes written $\operatorname{sinc}^2$, with $\operatorname{sinc}(x) = \sin x/x$). Several things to notice:

**At resonance** ($\omega = \omega_{fi}$), use L'Hôpital or Taylor expansion on the $\sin^2(\alpha t/2)/\alpha^2$ factor as $\alpha \to 0$: the result is $t^2/4$. So:

$$P_{i\to f}^{\text{resonance}}(t) = \frac{|V_{fi}|^2}{\hbar^2}\,\frac{t^2}{4}.$$

The on-resonance probability grows as $t^2$.

**Peak height** grows as $t^2$. **Width to the first zero** shrinks as $2\pi/t$. **Area under the central peak** grows as $t$. These three facts are consistent with a delta function emerging as $t\to\infty$: the sinc-squared function sharpens into $(\pi t/2)\,\delta\!\left(\omega_{fi}-\omega\right)$. This limit is the gateway to Fermi's golden rule (Chapter 7).

**The failure mode.** At resonance, $P_{i\to f}(t) = |V_{fi}|^2 t^2/(4\hbar^2)$. This grows without bound. At long enough times it exceeds 1. A probability exceeding 1 is not a numerical inconvenience — it is a diagnostic. The formula is telling you that first-order perturbation theory has broken.

The cause is the approximation $c_i(t) \approx 1$ throughout the integration. Once probability flows into $|f\rangle$, the population in $|i\rangle$ has decreased, and the rate of further transfer should slow down. The first-order equations ignore this feedback: they keep drawing from $|i\rangle$ as though nothing has changed. The exact two-level solution accounts for the feedback. First-order PT does not.

---

## The Exact Rabi Solution — and Where PT Fails

The two-level problem has an exact solution. Two states $|g\rangle$ (ground) and $|e\rangle$ (excited), with energies $0$ and $\hbar\omega_0$. Drive Hamiltonian:

$$\hat{H}'(t) = \hbar\Omega\cos(\omega t)\,(|e\rangle\langle g| + |g\rangle\langle e|).$$

The quantity $\Omega = |V_{fi}|/\hbar$ is the **Rabi frequency**. It is proportional to the coupling strength and, at resonance, sets the rate at which population cycles between the two levels.

In the RWA (drop the counter-rotating term), the Schrödinger equation reduces to two coupled first-order ODEs in $c_g(t)$ and $c_e(t)$:

$$\dot{c}_g = -\frac{i\Omega}{2}\,e^{-i\Delta t}\,c_e, \qquad \dot{c}_e = -\frac{i\Omega}{2}\,e^{+i\Delta t}\,c_g,$$

where $\Delta = \omega - \omega_0$ is the **detuning** — how far the drive frequency is from resonance. These equations are linear with constant-modulus oscillatory coefficients; they can be solved exactly by differentiating to get a second-order ODE and applying initial conditions $c_g(0) = 1$, $c_e(0) = 0$. The result:

$$\boxed{P_{g\to e}(t) = \frac{\Omega^2}{\Omega^2+\Delta^2}\,\sin^2\!\left(\frac{\sqrt{\Omega^2+\Delta^2}}{2}\,t\right).}$$

This is the **Rabi formula**. It is exact within the RWA — no perturbative approximation has been made.

Define the **generalized Rabi frequency** $\Omega_{\rm gen} = \sqrt{\Omega^2 + \Delta^2}$. Then $P_{g\to e}(t) = (\Omega/\Omega_{\rm gen})^2 \sin^2(\Omega_{\rm gen}\,t/2)$.

**On resonance** ($\Delta = 0$, so $\Omega_{\rm gen} = \Omega$):

$$P_{g\to e}(t) = \sin^2\!\left(\frac{\Omega t}{2}\right).$$

The population oscillates between 0 and 1. At $t = \pi/\Omega$ — a **$\pi$-pulse** — the entire population is in $|e\rangle$. At $t = 2\pi/\Omega$ it is back in $|g\rangle$. This is Rabi oscillation. It is what Rabi's molecular beam showed in 1938, and it is what every qubit readout protocol relies on today.

**Off resonance** ($\Delta \neq 0$): the maximum achievable probability is $\Omega^2/(\Omega^2+\Delta^2) < 1$. Full population transfer is impossible away from resonance. The oscillation frequency is $\Omega_{\rm gen}$ — faster than $\Omega$ — but the amplitude is smaller. The further the detuning, the shallower and faster the oscillation.

**Comparison to first-order PT at resonance:** PT gives $P^{\rm PT}_{g\to e}(t) = (\Omega t/2)^2$ — a parabola. The exact formula gives $\sin^2(\Omega t/2)$ — a bounded oscillation. For $\Omega t \ll 1$, expand: $\sin^2 x \approx x^2$. The two agree. This is the regime of validity of PT.

For $\Omega t \sim 1$, they diverge. At $\Omega t = \pi$ (the first $\pi$-pulse): exact $P = 1$, PT predicts $(\pi/2)^2 \approx 2.47$. PT has predicted a probability of 247%. The simulation in the +1 section lets you slide time from zero and watch the exact moment of failure.

**Why PT fails.** PT treats the amplitude in $|i\rangle$ as constant — $c_i(t) \approx 1$ — even as probability drains out of it. The exact solution feeds the depleted $|i\rangle$ population back in during the return half of the Rabi cycle; PT misses the return entirely. The regime of validity is $\Omega t \ll 1$: small coupling times short time. Outside that window, use the Rabi formula.

---

## Worked Example: The $\pi$-Pulse and the PT Breakdown

**The setup.** A two-level atom with transition energy $\hbar\omega_0 = 2.00\,\text{eV}$ (blue-violet, $\lambda \approx 620\,\text{nm}$) is driven by a resonant laser ($\omega = \omega_0$). The coupling strength is $\hbar\Omega = 0.010\,\text{eV}$. The atom starts in the ground state at $t = 0$.

**Part (a): When does the atom first reach $P = 1$?**

On resonance, $P_{g\to e}(t) = \sin^2(\Omega t/2) = 1$ when $\Omega t/2 = \pi/2$, i.e., $t_\pi = \pi/\Omega$.

Convert to SI: $\hbar\Omega = 0.010\,\text{eV} \times 1.602\times10^{-19}\,\text{J/eV} = 1.602\times10^{-21}\,\text{J}$, so $\Omega = 1.602\times10^{-21}\,\text{J} / (1.055\times10^{-34}\,\text{J·s}) = 1.519\times10^{13}\,\text{rad/s}$.

$$t_\pi = \frac{\pi}{\Omega} = \frac{\pi}{1.519\times10^{13}} \approx 2.07\times10^{-13}\,\text{s} = 0.21\,\text{ps}.$$

**Part (b): When does first-order PT predict $P = 1$, and what is the exact probability there?**

PT predicts $P^{\rm PT} = (\Omega t/2)^2 = 1$ when $\Omega t/2 = 1$, i.e., $t_{\rm PT} = 2/\Omega = 2/(1.519\times10^{13}) \approx 1.32\times10^{-13}\,\text{s} = 0.13\,\text{ps}$.

At $t = t_{\rm PT}$, $\Omega t_{\rm PT}/2 = 1\,\text{rad}$. The exact probability:

$$P_{g\to e}(t_{\rm PT}) = \sin^2(1) \approx 0.708.$$

**The lesson.** At the moment PT predicts complete population transfer ($P = 1$), the real atom has transferred only 71% of its population. The remaining 29% is still in the ground state, and the Rabi oscillation is about to start returning it. PT missed the return entirely because it assumed $c_g = 1$ throughout. The exact calculation and the PT calculation agree at early times ($\Omega t \ll 1$) and diverge at $\Omega t \sim 1$.

**The limit.** What if the coupling is much weaker — say, $\hbar\Omega = 10^{-6}\,\text{eV}$? Then $t_\pi$ grows by a factor of $10^4$, but more importantly, the $\Omega t \ll 1$ window extends over most of the time available before spontaneous emission (Chapter 7) destroys the coherence. In that regime, first-order PT is accurate for all practical purposes. PT fails not because coupling is "small" in some abstract sense, but because the product $\Omega t$ becomes of order 1. Time matters as much as coupling strength.

---

## Common Misconceptions

**"The transition probability grows forever on resonance."** No. In a two-level system, the probability oscillates between 0 and 1 (Rabi formula). The $t^2$ growth predicted by first-order PT is the diagnostic that PT has broken, not a physical prediction. Once the exact solution is used, the system returns to the ground state at $t = 2\pi/\Omega$. In a real atom, spontaneous emission (Chapter 7) damps this oscillation — but the damping is slow compared to the Rabi cycle when $\Omega \gg 1/\tau$, where $\tau$ is the excited-state lifetime.

**"Resonance means $P = 1$."** Resonance ($\omega = \omega_0$) means the maximum possible probability is 1 (achieved at $t = \pi/\Omega$, the $\pi$-pulse). Off resonance, the maximum is $\Omega^2/(\Omega^2+\Delta^2) < 1$. Resonance maximizes the probability of transition; it does not guarantee unit transfer at arbitrary time. You have to also time the interaction correctly ($t = \pi/\Omega$).

**"The rotating-wave approximation is always valid."** The RWA drops the counter-rotating term at frequency $2\omega$. This is valid when $\Omega \ll \omega_0$ (weak drive, near resonance). In ultra-strong coupling — realizable in circuit quantum electrodynamics, where superconducting qubits are coupled to microwave resonators — the counter-rotating term contributes a measurable **Bloch–Siegert shift** of order $\Omega^2/\omega_0$. [verify: Bloch–Siegert shift in circuit QED experiments, typical magnitude $\sim 1$–$10$ MHz for $\Omega/2\pi \sim 10$–$100$ MHz and $\omega_0/2\pi \sim 5$–$10$ GHz]

**"First-order PT fails because the coupling is too large."** It fails for a precise physical reason: it assumes the initial state is undepleted. The failure criterion is $\Omega t \sim 1$. A student who knows this can predict in advance whether PT will be reliable for a given experiment, without computing anything.

**"The interaction picture is just a gauge transformation."** The interaction picture is a unitary transformation on the state vector that removes the $\hat{H}_0$ evolution. It has a formal similarity to a gauge transformation but is better understood as a change of frame: instead of watching the state precess at the fast Bohr frequency, you watch only the slow perturbation-driven changes. Calling it a gauge transformation before the student understands gauge theory is confusing and inaccurate.

---

## Exercises

**6.1** *(Warm-up — Understand)* A harmonic oscillator ($m$, $\omega$) in the ground state $|0\rangle$ receives a short kick: $\hat{H}'(t) = F\hat{x}\,\delta(t)$ with $F$ small. (a) Using $\hat{x} = \sqrt{\hbar/2m\omega}\,(\hat{a}_+ + \hat{a}_-)$, compute the first-order transition amplitude $c_1^{(1)}(\infty)$ to the first excited state. The time integral of $\delta(t)e^{i\omega_{10}t}$ evaluated at $t = 0$ is 1. (b) Show the transition probability is $P_{0\to 1} = F^2/(2m\omega\hbar)$. (c) State the condition on $F$ for first-order PT to be valid. *What does this condition mean physically?*

**6.2** *(Warm-up — Apply)* A two-level system ($\hbar\omega_0 = 5.0\,\text{eV}$, $\hbar\Omega = 0.05\,\text{eV}$) is driven on resonance. (a) Compute the generalized Rabi frequency $\Omega_{\rm gen}$ at detuning $\Delta = 0.5\,\Omega$, $1.0\,\Omega$, and $2.0\,\Omega$. (b) For each detuning, compute the maximum transition probability $P_{\rm max} = \Omega^2/(\Omega^2+\Delta^2)$. (c) At $\Delta = 2\Omega$, by what factor is the maximum probability suppressed relative to the on-resonance case?

**6.3** *(Apply — Breakdown criterion)* For the two-level atom of the worked example ($\hbar\omega_0 = 2.00\,\text{eV}$, $\hbar\Omega = 0.010\,\text{eV}$), first-order PT is reliable while the exact and PT probabilities agree to within 10%. (a) Find the time $t_{10\%}$ at which PT first differs from the exact by 10% on resonance. Use the Taylor expansions $\sin^2 x \approx x^2 - x^4/3$ and $(\Omega t/2)^2$ to find the leading correction, or solve numerically. (b) Express $t_{10\%}$ as a multiple of the Bohr oscillation period $2\pi/\omega_0$. Is $t_{10\%}$ long or short compared to the natural timescale of the unperturbed system?

**6.4** *(Apply — Sinc-squared lineshape)* A perturbation $\hat{H}'(t) = \hat{V}\cos(\omega t)$ is applied to a two-level atom for a finite time interval $0 \leq t \leq T$. (a) Show that the first-order transition probability at time $T$, as a function of detuning $\delta = \omega_{fi} - \omega$, is:
$$P(\delta, T) = \frac{|V_{fi}|^2}{\hbar^2}\,\frac{\sin^2(\delta T/2)}{(\delta/2)^2}.$$
(b) At what values of $\delta$ are the first zeros of the sinc-squared function? (c) A student wants to drive the transition selectively — with less than 1% excitation of a neighboring transition at detuning $\delta_0 = 10^9\,\text{rad/s}$ from resonance. What minimum pulse duration $T$ is required?

**6.5** *(Apply — Sudden vs. adiabatic)* An oscillator (frequency $\omega$) in state $|n\rangle$ is subjected to a perturbation that turns on slowly and then off: $\hat{H}'(t) = \lambda\hat{x}^2\,f(t)$ where $f(t)$ rises from 0 to 1 over a timescale $\tau_{\rm on} \gg 1/\omega$ (adiabatic turn-on) and then drops suddenly back to 0 over a timescale $\tau_{\rm off} \ll 1/\omega$ (sudden turn-off). Which part of this protocol — turn-on or turn-off — drives transitions? Explain using the Fourier-transform interpretation of the transition amplitude. Which limit (sudden or adiabatic) drives more transitions, and why?

**6.6** *(Produce — Exact vs. PT comparison)* A two-level atom has $\hbar\Omega = 0.5\,\hbar\omega_0$ (strong coupling, so $\Omega = \omega_0/2$). This is outside the usual weak-coupling assumption. (a) Write down the exact Rabi formula for $P_{g\to e}(t)$ at resonance. (b) Write the first-order PT formula. (c) Compute both at $\Omega t = \pi/4$, $\pi/2$, $\pi$, and $3\pi/2$. Tabulate. (d) At what time does the PT formula exceed 1? (e) This coupling is too strong for the RWA to be fully reliable. State which term the RWA drops and estimate the magnitude of the Bloch–Siegert correction $\sim \Omega^2/\omega_0$ as a fraction of $\omega_0$.

**6.7** *(Analyze — Design a qubit gate)* A superconducting transmon qubit has transition frequency $\omega_0/(2\pi) = 5.0\,\text{GHz}$ and coherence time $T_2 = 80\,\mu\text{s}$. A microwave pulse with Rabi frequency $\Omega/(2\pi) = 10\,\text{MHz}$ is applied on resonance. (a) Compute the time $t_\pi = \pi/\Omega$ for a $\pi$-pulse (the gate that flips the qubit from $|0\rangle$ to $|1\rangle$). (b) How many Rabi periods fit within $T_2$? (c) Determine whether first-order PT would be valid during the $\pi$-pulse. (d) Explain why the experiment uses the exact Rabi formula (and the precision it enables) rather than first-order perturbation theory to design the pulse.

---

## Still Puzzling

The sinc-squared lineshape, as $t \to \infty$, becomes $(\pi t/2)\,\delta(\omega_{fi} - \omega)$. The area under the central peak grows linearly in $t$, and the rate of transition to a single final state becomes constant — which is Fermi's golden rule for a continuum, derived in Chapter 7. But the derivation of the golden rule requires taking $t \to \infty$ to sharpen the delta function, while its validity requires $W \cdot t \ll 1$ so that first-order PT holds. Both limits cannot simultaneously apply at arbitrarily long times.

For atomic emission into the vacuum, the window between these bounds is enormous — femtoseconds for the Bohr period, nanoseconds for the spontaneous emission lifetime, and the golden rule is valid in the entire middle range. But the logical structure has a seam. I can draw the window. I cannot make the seam fully disappear.

---

## The +1 — Simulation Exercise

You are going to build a single-file D3 simulation that shows the exact Rabi formula and first-order perturbation theory side by side, including a continuum mode where coherent Rabi oscillation collapses into the linear growth predicted by Fermi's golden rule. The deliverable is `06-rabi-resonance.html`.

### Part 1 — Update PROJECT.md

```
Append a new entry to PROJECT.md describing this chapter's simulation:

Chapter 06 — Time-Dependent Perturbation Theory and Transitions
Deliverable: 06-rabi-resonance.html
Status: in progress

The simulation displays a driven two-level system in two modes:

Mode A — Two-level (Panels A and B)

Panel A (left): P_{g->e} vs. time at fixed detuning Delta.
Two curves:
  - Exact Rabi formula (solid black): P = (Omega^2/(Omega^2+Delta^2)) * sin^2(sqrt(Omega^2+Delta^2)*t/2)
  - First-order PT (dashed teal): P = (Omega*t/2)^2 at Delta=0;
    (Omega^2/Delta^2)*sin^2(Delta*t/2) off resonance
X-axis: time in units of 2*pi/Omega, range 0 to 4 (four Rabi periods).
Y-axis: probability 0 to 1.2 (so PT overflow is visible above 1).
When PT exceeds 1, display "PT NO LONGER VALID" in red.

Panel B (right): P_{g->e}(Delta) at fixed time T_fixed.
Two curves (exact and PT) as functions of detuning Delta, range -5*Omega to +5*Omega.
Slider for T_fixed.

Mode B — Continuum (Panel C)
Replace the single |e> with N equally spaced excited states over band
width Delta_band. Compute P_total(t) = sum |c_k(t)|^2 from first-order PT.
Plot vs. time alongside the Fermi golden-rule linear prediction W*t.
Watch the discrete Rabi oscillations smooth into a linear ramp as N grows.

Controls:
- Omega slider (0.01 to 0.5 omega_0)
- Delta slider for Panel A (-5*Omega to +5*Omega)
- T_fixed slider for Panel B
- N slider (5 to 50) and Delta_band slider for Mode B
- Toggle: show exact | show PT | show both
```

### Part 2 — The CLAUDE.md amendment

```
Append to CLAUDE.md the following physics rules for Chapter 6 simulations:

TIME-DEPENDENT PERTURBATION-THEORY PHYSICS RULES

1. TWO-LEVEL EXACT RABI (RWA). For initial state |g>, drive H' = hbar*Omega*cos(omega*t)*(|e><g|+|g><e|):
     P_{g->e}(t) = (Omega^2 / Omega_gen^2) * sin^2(Omega_gen * t / 2)
   where Omega_gen = sqrt(Omega^2 + Delta^2), Delta = omega - omega_0.
   This is exact; no perturbative approximation.

2. FIRST-ORDER PT (RWA):
     P_PT(t) = (Omega^2 / Delta^2) * sin^2(Delta * t / 2) [off resonance]
     P_PT(t) = (Omega * t / 2)^2                          [on resonance, Delta->0 limit]
   NOTE: P_PT can exceed 1. When it does, display "PT NO LONGER VALID" in red.

3. CONTINUUM MODE. N states |e_k> at energies E_e + k*dE, k = -N/2 ... N/2.
   First-order amplitudes: c_k(t) = (Omega/2) * (1 - exp(i*(omega_k - omega)*t)) / (omega_k - omega).
   (Use l'Hopital: c_k -> -i*(Omega/2)*t when omega_k = omega.)
   P_total(t) = sum_k |c_k(t)|^2.

4. FERMI GOLDEN RULE PREDICTION for continuum mode:
     W = (2*pi/hbar) * |V_fi|^2 * rho(E)
   where rho(E) = N / Delta_band (states per unit energy, in units where hbar=1).
   Display W*t as a dashed orange reference line.

5. UNITS: hbar = omega_0 = 1. Omega, Delta dimensionless in omega_0 units.
   Time axis in units of 2*pi/Omega for Mode A, 2*pi/Delta_band for Mode B.

KNOWN FAILURE MODES:
(a) Delta=0 singularity in P_PT: use l'Hopital limit (Omega*t/2)^2.
(b) Sign of Delta: Delta = omega - omega_0 (positive = above resonance).
(c) Continuum: N < 10 shows spiky artifacts; use N >= 20.
(d) Time axis does not rescale when Omega changes: period is 2*pi/Omega; the
    axis should rescale with the slider.
```

### Part 3 — The simulation prompt

```
Build 06-rabi-resonance.html: a single self-contained HTML file using D3 v7
from CDN and d3-simple-slider (https://cdn.jsdelivr.net/npm/d3-simple-slider).
No other dependencies. Two tabs: "Two-level" and "Continuum (Fermi)".

TWO-LEVEL MODE — SVG 1100x600 split into two panels.

Panel A (left, 550 wide): P_{g->e} vs. time.
  X: time in units of 2*pi/Omega, range 0 to 4. Y: 0 to 1.2.
  Black solid = exact Rabi. Dashed teal = first-order PT.
  Horizontal dashed red line at P=1 labeled "P=1 (physical maximum)".
  Vertical reference lines at t = 1/Omega and t = 2/Omega.
  When PT curve exceeds 1, display "PT NO LONGER VALID" in red below the plot.

Panel B (right, 550 wide): P_{g->e}(Delta) at fixed T_fixed.
  X: Delta from -5*Omega to +5*Omega. Y: 0 to 1.2.
  Same two curves. Show how the PT sidelobes appear as T_fixed increases
  while the exact curve saturates.

Controls: Omega slider (0.01 to 0.5 omega_0, default 0.1); Delta slider for Panel A;
T_fixed slider for Panel B (range 0.5/Omega to 5/Omega).

CONTINUUM MODE — SVG 1100x600 with one main panel.
  P_total(t) from explicit band-state sum (black solid) and W*t reference (dashed orange).
  X: time in 2*pi/Delta_band units. Y: 0 to 1.
  Controls: N (5 to 50, default 20), Delta_band (0.1 to 2 omega_0, default 0.5),
  |V| (0 to 0.2 hbar*omega_0, default 0.05).

GLOBAL: Pure functions for Rabi formula and band sum. Vectorize band sum
(single loop over k, no nested loops). Runtime < 50 ms per slider update.

Console sanity checks:
- At Omega*t=0: both P_exact and P_PT equal 0.
- At Omega*t=0.1 (resonance): both agree within 1%.
- At Omega*t=pi (resonance): P_exact=1, P_PT=(pi/2)^2~2.47; warning fires.
- Continuum at t = 5*2*pi/Delta_band: P_total/t agrees with W within 5%.

Comments at every physics step. No dead code.
```

### Part 4 — Exploration tasks

Run the simulation and answer the following:

1. Two-level mode, Panel A, resonance ($\Delta = 0$). Set $\Omega = 0.1\,\omega_0$. Slide time to $\Omega t = \pi$. Confirm: exact $P = 1$, PT $P \approx 2.47$. Record the time (in ps, for $\hbar\omega_0 = 2\,\text{eV}$) at which the PT curve crosses $P = 1$. At that time, what is the exact probability?

2. Panel A, off-resonance. Set $\Delta = 2\Omega$. The exact curve oscillates with smaller amplitude. Read off $P_{\rm max}$ from the plot and compare to the formula $\Omega^2/(\Omega^2+\Delta^2) = 1/5$. Does the simulation confirm this?

3. Panel B (lineshape at fixed $T$). Set $T_{\rm fixed} = 1/\Omega$ and compare the exact and PT curves. Increase $T_{\rm fixed}$ to $5/\Omega$. Describe what happens to the exact curve (saturation) and the PT curve (sharpening + sidelobes).

4. Continuum mode. Start with $N = 5$. You should see oscillatory behavior — too few discrete states. Increase to $N = 20$, then $N = 50$. At $N = 50$, the curve should match the Fermi linear prediction (dashed orange) after the transient. Estimate the transient time in units of $2\pi/\Delta_{\rm band}$.

5. Continuum mode. With $N = 50$, halve $|V|$ (from $0.05$ to $0.025\,\hbar\omega_0$). The slope $W \propto |V|^2$ should drop by a factor of 4. Verify.

---

## References

- Griffiths, D.J. & Schroeter, D.F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press, 2018. §10.1–10.2 (interaction picture and first-order PT). [verify: section numbers in 3rd edition]
- Sakurai, J.J. & Napolitano, J. *Modern Quantum Mechanics*, 3rd ed. Cambridge University Press, 2021. §5.5–5.6 (time-dependent perturbation theory). [verify: section numbers in 3rd edition]
- Townsend, J.S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books, 2012. Ch. 14 (TDPT and the two-level system).
- Cohen-Tannoudji, C., Diu, B. & Laloë, F. *Quantum Mechanics*, Vol. II. Wiley, 1977. Ch. XIII (time-dependent perturbation theory, electric-dipole approximation).
- Rabi, I.I., Millman, S., Kusch, P. & Zacharias, J.R. "The molecular beam resonance method for measuring nuclear magnetic moments." *Physical Review* **55**, 526–535 (1939).
- Bloch, F. & Siegert, A. "Magnetic Resonance for Nonrotating Fields." *Physical Review* **57**, 522–527 (1940). [The Bloch–Siegert shift, the leading correction when the counter-rotating term is not negligible.]
- Landau, L. "Zur Theorie der Energieübertragung. II." *Phys. Z. Sowjetunion* **2**, 46 (1932). [Landau–Zener transition formula.]
- Zener, C. "Non-Adiabatic Crossing of Energy Levels." *Proc. R. Soc. Lond. A* **137**, 696–702 (1932).
