# Chapter 5 — The WKB Approximation and Tunneling

## TL;DR

- A particle with less energy than the top of a barrier should not get through — classically. Quantum-mechanically, the wave function does not vanish inside the barrier; it decays, and a piece emerges on the other side. This is tunneling.
- The WKB approximation turns the Schrödinger equation into a semiclassical expansion in powers of $\hbar$, giving wave functions that oscillate or decay with locally varying phase and amplitude. The framework is exact in the large-action limit ($\int p\,dx \gg \hbar$) and breaks down at classical turning points, which are handled by a connection formula involving Airy functions.
- The key results: the WKB wave function; the validity condition $|d\lambda_\text{dB}/dx| \ll 1$; the Bohr–Sommerfeld quantization condition $\oint p\,dx = (n+\tfrac{1}{2})h$; the Gamow tunneling factor $T \approx e^{-2\gamma}$; alpha decay as the payoff application. The Langer correction handles the 3D radial equation. The tunneling time remains an open question.

**Learning objectives**

1. **Derive** the WKB wave function from the ansatz $\psi = e^{iS/\hbar}$ and identify the physical meaning of the $1/\sqrt{p}$ amplitude. *(Bloom: Understand/Analyze)*
2. **State** the validity condition and identify where it fails; explain the role of Airy functions at a classical turning point. *(Bloom: Understand)*
3. **Apply** the Bohr–Sommerfeld condition to estimate bound-state energies and reproduce exact results for the harmonic oscillator. *(Bloom: Apply)*
4. **Calculate** the Gamow tunneling factor for a given barrier and use it to estimate a transmission coefficient or halflife. *(Bloom: Apply)*
5. **Evaluate** the range of physical phenomena (alpha decay, STM, stellar fusion, flash memory) that share the same exponential tunneling structure, and use the Gamow factor as a falsification tool. *(Bloom: Evaluate)*

---

Polonium-212 has a halflife of about $3 \times 10^{-7}$ seconds — it decays almost instantly on any human timescale. Thorium-232 has a halflife of about $1.4 \times 10^{10}$ years — longer than the current age of the universe. Both decay by emitting the same particle through the same mechanism: an alpha particle (two protons, two neutrons) that escapes from a nucleus by tunneling through a Coulomb barrier.

The ratio of their halflives is roughly $10^{24}$. Twenty-four orders of magnitude.

In 1911, Hans Geiger and John Mitchell Nuttall found that for alpha emitters with the same daughter nucleus charge, the logarithm of the halflife is approximately linear in $1/\sqrt{E_\alpha}$ — a straight line on a log-versus-inverse-square-root plot [verify: Geiger & Nuttall, Phil. Mag. 22, 613 (1911)]. The observation was clean. The explanation was completely absent.

Here is what made that explanation hard. An alpha particle approaching the boundary of a nucleus from the inside sees a potential barrier. Inside the nucleus, the strong nuclear force holds it. Outside, the Coulomb repulsion from the daughter nucleus pushes it away. The barrier height is around 30 MeV. The emitted alpha has around 5 MeV. Classically, the alpha is stuck — it does not have enough energy to escape over the top. And yet out it comes.

In the summer of 1928, George Gamow in Göttingen computed the probability of the alpha particle tunneling through the Coulomb barrier using the brand-new tools of wave mechanics. Within days, Ronald Gurney and Edward Condon at Princeton published the same idea independently [verify: Gamow, Z. Phys. 51, 204 (1928); Gurney & Condon, Nature 122, 439 (1928)]. Both found the same answer: the tunneling probability is exponentially sensitive to barrier height, width, and particle energy. That exponential sensitivity is the source of the 24-decade dynamic range. A small change in alpha energy corresponds to a large change in the exponent, which corresponds to an astronomical change in the halflife. The Geiger–Nuttall line is a plot of that exponent as a function of alpha energy.

This chapter builds the machinery that gives you that result.

---

## The WKB ansatz

The time-independent Schrödinger equation in one dimension is:

$$-\frac{\hbar^2}{2m}\psi''(x) + V(x)\psi(x) = E\psi(x)$$

Define the local classical momentum:

$$p(x) = \sqrt{2m(E - V(x))}$$

which is real where the particle is classically allowed ($E > V$) and imaginary in the classically forbidden region ($E < V$). Now write the wave function as:

$$\psi(x) = e^{iS(x)/\hbar}$$

for some function $S(x)$. This is not an approximation — it is an exact rewriting. Any $\psi$ can be written this way; $S$ is in general complex. Substituting into the Schrödinger equation and collecting terms gives:

$$\frac{(S')^2}{2m} - \frac{i\hbar}{2m}S'' = E - V(x)$$

Now expand $S$ in powers of $\hbar$:

$$S = S_0 + \frac{\hbar}{i}S_1 + \left(\frac{\hbar}{i}\right)^2 S_2 + \cdots$$

At zeroth order in $\hbar$ the equation gives $(S_0')^2/2m = E - V$, so:

$$S_0'(x) = \pm p(x) \quad\Longrightarrow\quad S_0(x) = \pm\int p(x')\,dx'$$

At first order in $\hbar$, the equation becomes $2S_0'S_1'/(2m) = iS_0''/(2m)$, giving $S_1' = iS_0''/(2S_0') = ip'/(2p)$, so $S_1 = \frac{i}{2}\ln p + \text{const}$. Assembling the leading and first-order terms:

$$\psi_\text{WKB}(x) \approx \frac{C}{\sqrt{p(x)}}\,\exp\!\left[\frac{i}{\hbar}\int p(x')\,dx'\right] + \frac{D}{\sqrt{p(x)}}\,\exp\!\left[-\frac{i}{\hbar}\int p(x')\,dx'\right]$$

in the classically allowed region ($E > V$), and in the classically forbidden region where $p = i|p|$:

$$\psi_\text{WKB}(x) \approx \frac{A}{\sqrt{|p(x)|}}\,\exp\!\left[\frac{1}{\hbar}\int |p(x')|\,dx'\right] + \frac{B}{\sqrt{|p(x)|}}\,\exp\!\left[-\frac{1}{\hbar}\int |p(x')|\,dx'\right]$$

**The $1/\sqrt{p}$ factor has a clean physical meaning.** The classical probability of finding the particle near $x$ is proportional to how long it spends there — proportional to $1/v(x) \propto 1/p(x)$. So $|\psi|^2 \propto 1/p(x)$: the wave function is large where the classical particle moves slowly, small where it moves fast. The amplitude tracks classical mechanics; the phase oscillates quantum-mechanically. This is what "semiclassical" means in precise terms.

The expansion is controlled by the small parameter $\hbar/S_0 \sim \hbar/(\int p\,dx)$. When the classical action $\int p\,dx$ is large compared to $\hbar$, the expansion is reliable. When $\int p\,dx \sim \hbar$, the approximation breaks down.

---

## When the approximation is valid — and when it is not

The WKB expansion is controlled if higher-order terms in $\hbar$ are small. Working through the algebra, the condition reduces to:

$$\left|\frac{d\lambda_\text{dB}}{dx}\right| \ll 1$$

where $\lambda_\text{dB}(x) = h/p(x)$ is the **local de Broglie wavelength**. The potential must vary slowly across one de Broglie wavelength. Equivalently: the classical action $\int p\,dx$ must be large compared to $\hbar$, meaning the particle traverses many wavelengths.

This condition fails *exactly* at a **classical turning point** $x_0$ where $E = V(x_0)$ and $p(x_0) \to 0$. As the particle slows down at the turning point, its de Broglie wavelength grows without bound. The WKB forms on each side cannot be matched naively because the $1/\sqrt{p}$ prefactor diverges.

**The fix: Airy functions.** Near the turning point, linearize the potential: $V(x) \approx V(x_0) + V'(x_0)(x - x_0)$. With $E = V(x_0)$, the Schrödinger equation becomes:

$$\psi'' = \frac{2mV'(x_0)}{\hbar^2}(x - x_0)\psi$$

Define $z = (x - x_0)(2mV'/\hbar^2)^{1/3}$. The equation becomes $\psi'' = z\psi$, which is the **Airy equation**. The regular solution is the Airy function $\text{Ai}(z)$, which is the unique solution that decays on both the positive-$z$ (forbidden) and oscillates on the negative-$z$ (allowed) sides:

$$\text{Ai}(z) \sim \begin{cases} \frac{1}{2\sqrt{\pi}}\,|z|^{-1/4}\cos\!\left(\frac{2}{3}|z|^{3/2} - \frac{\pi}{4}\right) & z \to -\infty\; (\text{allowed side}) \\ \frac{1}{2\sqrt{\pi}}\,z^{-1/4}\,e^{-\frac{2}{3}z^{3/2}} & z \to +\infty\; (\text{forbidden side}) \end{cases}$$

The $\pi/4$ phase shift in the cosine on the allowed side is the **Maslov index** — a theorem about the topology of the connection across a turning point, not an ad hoc convention. Matching the Airy function asymptotics to the WKB solutions on each side gives the **connection formulas**. Each turning point contributes a phase shift of $\pi/4$.

The derivation of the connection formulas is algebraically dense; the important output is the Maslov correction — the $1/2$ that will appear in the Bohr–Sommerfeld condition. Deriving it once, carefully, is more valuable than memorizing the formulas.

---

## Bound states: the Bohr–Sommerfeld condition

A particle is bound between two classical turning points $a$ and $b$: classically allowed for $a < x < b$, forbidden outside. The wave function oscillates inside and decays outside. Threading the WKB solution through both turning points, applying the connection formula at each, and demanding a self-consistent single-valued solution gives the **Bohr–Sommerfeld quantization condition**:

$$\boxed{\oint p(x)\,dx = 2\int_a^b p(x)\,dx = \left(n + \frac{1}{2}\right)h, \quad n = 0, 1, 2, \ldots}$$

The factor of $1/2$ inside the bracket is the combined Maslov correction from both turning points ($\pi/4$ each, adding to $\pi/2$, which is $1/2$ in units of $h$). The original Bohr–Sommerfeld rule of 1913–1916 had $nh$ with no Maslov correction; the correct $n + 1/2$ emerges from the Airy function analysis.

**A remarkable special case.** For the harmonic oscillator, $V = \frac{1}{2}m\omega^2 x^2$, the turning points at energy $E$ are $x = \pm\sqrt{2E/m\omega^2}$. The phase-space orbit is an ellipse with semi-axes $\sqrt{2mE}/(m\omega)$ in $x$ and $\sqrt{2mE}$ in $p$. The enclosed area is:

$$\oint p\,dx = \pi \cdot \frac{\sqrt{2mE}}{m\omega}\cdot\sqrt{2mE} = \frac{2\pi E}{\omega}$$

The Bohr–Sommerfeld condition then gives:

$$\frac{2\pi E}{\omega} = \left(n+\frac{1}{2}\right)h \quad\Longrightarrow\quad E_n = \left(n + \frac{1}{2}\right)\hbar\omega$$

This is the *exact* quantum-mechanical energy spectrum — not an approximation. The same miracle happens for the Coulomb potential and hydrogen. These are not coincidences: they reflect hidden algebraic symmetries (the Fock SU(2) symmetry for the oscillator, the Runge-Lenz vector for hydrogen) that cause the WKB expansion to terminate. For most other potentials, Bohr–Sommerfeld is a leading-order estimate that improves for large $n$.

---

## Worked example: WKB tunneling and Bohr–Sommerfeld

### Part I — Tunneling through a rectangular barrier

An electron ($m_e = 9.11 \times 10^{-31}\,\text{kg}$) with kinetic energy $E = 1\,\text{eV}$ encounters a rectangular barrier of height $V_0 = 5\,\text{eV}$ and width $L = 5\,\text{Å}$.

**Step 1.** Compute $\kappa = \sqrt{2m_e(V_0 - E)}/\hbar$:

$$\kappa = \frac{\sqrt{2\times 9.11\times 10^{-31}\times 4\times 1.6\times 10^{-19}}}{1.055\times 10^{-34}} \approx 1.02\,\text{Å}^{-1}$$

**Step 2.** The Gamow factor: $\gamma = \kappa L = 1.02 \times 5 = 5.10$. The WKB transmission coefficient:

$$T_\text{WKB} = e^{-2\gamma} = e^{-10.2} \approx 3.7 \times 10^{-5}$$

**Step 3.** The exact result (derived by matching wave functions at both barrier edges — see Exercise 5.3):

$$T_\text{exact} = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$$

With $\kappa L = 5.10$: $\sinh(5.10) \approx 82.1$, $\sinh^2 \approx 6740$. So:

$$T_\text{exact} \approx \left[1 + \frac{25 \times 6740}{16}\right]^{-1} \approx \frac{1}{10532} \approx 9.5\times 10^{-5}$$

**Step 4.** The ratio $T_\text{exact}/T_\text{WKB} \approx 9.5/3.7 \approx 2.6$. The analytical prediction for the prefactor in the thick-barrier limit is $16E(V_0-E)/V_0^2 = 16 \times 1 \times 4/25 = 2.56$. Agreement within rounding.

**The lesson.** WKB nails the exponent — the factor $\kappa L$ in the exponent is exactly right. It misses the prefactor $16E(V_0-E)/V_0^2$ by an $O(1)$ factor that depends smoothly on $E/V_0$. On a log plot, $T_\text{exact}$ and $T_\text{WKB}$ run parallel (same slope) with a constant offset. For physics that spans 24 orders of magnitude, the $O(1)$ prefactor is irrelevant.

**The limit.** When $E \to V_0$ (barrier top), $\kappa \to 0$, $T \to 1$, and WKB breaks down — the particle is no longer in the tunneling regime and you cannot trust the $e^{-2\kappa L}$ formula. The exact result interpolates smoothly through the barrier top, while the WKB formula has a kink there. This is the limit of validity: WKB applies when $\kappa L \gg 1$ (deep sub-barrier tunneling).

### Part II — Bohr–Sommerfeld for a linear potential

Consider the "bouncing ball" potential $V(x) = mgx$ for $x > 0$ with a hard wall at $x = 0$. The classical turning point is at $x_0 = E/(mg)$. The Bohr–Sommerfeld condition:

$$\int_0^{x_0} \sqrt{2m(E - mgx)}\,dx = \left(n + \frac{3}{4}\right)\frac{h}{2}$$

(The wall at $x = 0$ contributes a phase of $\pi/2$ — equivalent to a Maslov index of $1/2$ there — while the smooth turning point at $x_0$ contributes the usual $\pi/4$, giving a combined factor of $3/4$ on the right.) The integral evaluates to:

$$\int_0^{x_0}\sqrt{2m(E-mgx)}\,dx = \frac{2}{3}\frac{(2mE)^{3/2}}{(2m^2g)} = \frac{\sqrt{2m}}{3mg}E^{3/2}(2)^{1/2}$$

Working through the algebra: $E_n \propto (n+3/4)^{2/3}$. This is the WKB energy spectrum for a particle in a gravitational well, and it matches the exact results (in terms of zeros of the Airy function $\text{Ai}$) to better than 1% even for $n=0$.

---

## Tunneling: the Gamow factor

Now the main result. A particle with energy $E$ encounters a potential barrier $V(x) > E$ between two classical turning points $a$ and $b$. Inside the barrier, the WKB wave function decays as $e^{-(1/\hbar)\int_a^x |p|\,dx}$. Threading through both connection formulas and computing the ratio of transmitted to incident probability current, the **transmission coefficient** is:

$$\boxed{T \approx e^{-2\gamma}, \qquad \gamma = \frac{1}{\hbar}\int_a^b \sqrt{2m(V(x)-E)}\,dx}$$

The integral $\gamma$ is the **Gamow factor**. Three features control everything.

First, $T$ is *exponential* in $\gamma$. A small change in barrier height, width, or particle energy gets amplified into a large change in $T$. This is the origin of the 24-decade dynamic range in alpha-decay halflives — small changes in nuclear radius or alpha energy correspond to large changes in the exponent.

Second, the barrier *shape* integrates into the formula automatically. Any $V(x)$ gets the same treatment: just integrate $\sqrt{2m(V-E)}$ over the forbidden region. Rectangular, triangular, parabolic, Coulomb — all handled by the same formula with different integrals.

Third, the prefactor. The exact WKB formula has an amplitude prefactor of order unity that depends on barrier-matching details, but in the thick-barrier limit ($\gamma \gg 1$) the exponential carries essentially all the information. When the physics spans many decades, the $O(1)$ prefactor is in the noise.

---

## Alpha decay and the Geiger–Nuttall law

Model an alpha particle as a pre-formed cluster bouncing inside a heavy nucleus. Inside, at radius $r < R$ (nuclear radius), the strong force holds it. Outside, at $r > R$, it sees the Coulomb repulsion from the daughter nucleus of charge $Z' = Z - 2$:

$$V(r) = \frac{2Z'e^2}{4\pi\epsilon_0 r}, \quad r > R$$

The barrier extends from $r = R$ out to the classical turning point $r_c$ where $V(r_c) = E_\alpha$:

$$r_c = \frac{2Z'e^2}{4\pi\epsilon_0 E_\alpha}$$

For uranium-238 ($Z' = 90$, $E_\alpha \approx 4.2\,\text{MeV}$, $R \approx 7.4\,\text{fm}$), the turning point sits at $r_c \approx 60\,\text{fm}$ — the alpha must tunnel through a barrier eight times wider than the nucleus.

The Gamow integral over the Coulomb barrier is done analytically with the substitution $r = r_c\sin^2\theta$:

$$\gamma = \frac{1}{\hbar}\int_R^{r_c}\sqrt{2m_\alpha\left(\frac{2Z'e^2}{4\pi\epsilon_0 r} - E_\alpha\right)}\,dr$$

In the limit $R \ll r_c$ (which holds for heavy nuclei):

$$\gamma \approx \frac{\pi Z' e^2}{4\epsilon_0\hbar}\sqrt{\frac{m_\alpha}{2E_\alpha}} - \frac{2}{\hbar}\sqrt{2m_\alpha R \cdot E_\alpha \cdot r_c / r_c}$$

The first term grows as $1/\sqrt{E_\alpha}$ and dominates; the second is a smaller correction from the inner edge. The decay rate is:

$$\Gamma \sim \nu_0\,e^{-2\gamma}$$

where $\nu_0 \sim v_\alpha/(2R) \sim 10^{21}\,\text{Hz}$ is the attempt frequency — how often per second the alpha bounces against the inside of the barrier. Taking the logarithm of the halflife:

$$\log_{10}\tau_{1/2} \approx A(Z') + \frac{B(Z')}{\sqrt{E_\alpha}}$$

This is the **Geiger–Nuttall law**: log halflife linear in $1/\sqrt{E_\alpha}$ for fixed daughter charge. The empirical observation from 1911 is *derived* from the WKB tunneling formula. Every point on the Geiger–Nuttall line is a different nuclide; every nuclide lies on the same straight line. Twenty-four decades on a single plot.

**Numerics for $^{238}$U.** With the numbers above: $\gamma \approx 43$, so $e^{-2\gamma} \approx e^{-86} \approx 4\times 10^{-38}$. The decay rate is $\Gamma \sim 10^{21} \times 4\times 10^{-38} \approx 4\times 10^{-17}\,\text{s}^{-1}$, corresponding to a halflife of roughly $5\times 10^8$ years. The experimental value is $4.5\times 10^9$ years. We are off by a factor of 10. On a quantity spanning $10^{24}$, this is excellent agreement — the remaining discrepancy comes from the pre-formation probability of the alpha cluster inside the nucleus and from the prefactors in the WKB formula that we dropped.

---

## The exponential in other contexts

The Gamow factor is not exclusive to nuclear physics. The same exponential structure runs through a surprising range of phenomena.

**Scanning tunneling microscope.** A metal tip is held a few ångströms above a conducting surface. A bias voltage drives electrons through the vacuum gap. The work function of a typical metal is $\phi \approx 4\,\text{eV}$, giving $\kappa = \sqrt{2m_e\phi}/\hbar \approx 1\,\text{Å}^{-1}$. The tunneling current goes as $I \propto e^{-2\kappa d}$. When the tip moves 1 Å closer, the current increases by a factor of $e^2 \approx 7$. A surface feature of sub-ångström amplitude produces a measurable swing in current. This is why an STM can image individual atoms: the exponential transduction converts atomic-scale topography into macroscopic current variations [verify: Binnig & Rohrer, PRL 49, 57 (1982)].

**Stellar fusion.** In the solar core at $kT \sim 1\,\text{keV}$, the Coulomb barrier for proton-proton fusion is of order 1 MeV. Most fusion occurs not at $kT$ but at the **Gamow peak energy** $E_G = (bkT/2)^{2/3}$, where $b = \pi e^2\sqrt{2m_p}/(4\epsilon_0\hbar)$. For solar conditions, $E_G \approx 6\,\text{keV}$ — six times $kT$. The fusion rate is the product of the Maxwell–Boltzmann thermal tail (which grows with $E$) and the Gamow tunneling factor (which decreases with $E$); the product peaks at $E_G$. Every star burns by tunneling [verify: Atkinson & Houtermans, Z. Phys. 54, 656 (1929)].

**Flash memory.** Electrons tunnel through a thin $\text{SiO}_2$ layer ($\sim 10\,\text{nm}$) under a high electric field, giving a triangular barrier in the oxide. The write speed and data retention time of every USB stick are controlled by the Gamow factor for a triangular barrier — Fowler–Nordheim tunneling [verify: Fowler & Nordheim, Proc. R. Soc. A 119, 173 (1928)].

**Cold fusion falsification.** Martin Fleischmann and Stanley Pons claimed in 1989 to have achieved deuterium-deuterium fusion at room temperature. The Gamow factor at room temperature ($kT \approx 0.025\,\text{eV}$): with a D-D Coulomb barrier of order 1 MeV, $\gamma \sim 1000$ and $e^{-2\gamma} \sim 10^{-900}$. Even if the palladium lattice increased the tunneling rate by a factor of $10^{50}$ (which it cannot), you would still be $10^{850}$ short of the claimed power output. The calculation takes five minutes; the conclusion is unambiguous. Knowing how to compute a Gamow factor is sufficient to quantitatively evaluate any "novel nuclear effect at ambient conditions" claim.

---

## The Langer correction for the 3D radial equation

In three dimensions, the Schrödinger equation for a spherically symmetric potential $V(r)$ separates into radial and angular parts. The radial equation for the function $u(r) = r\,R(r)$ is:

$$-\frac{\hbar^2}{2m}u'' + \left[V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u = Eu$$

This looks like a 1D problem with effective potential $V_\text{eff}(r) = V(r) + \hbar^2\ell(\ell+1)/(2mr^2)$, and one might naively apply the WKB approximation directly. However, near $r = 0$ the centrifugal term $\ell(\ell+1)/r^2$ diverges, and the WKB validity condition fails. The correct semiclassical quantization for the radial equation requires the **Langer correction**: replace $\ell(\ell+1)$ by $(\ell + 1/2)^2$:

$$2\int_{r_1}^{r_2}\sqrt{2m\left[E - V(r) - \frac{\hbar^2(\ell+1/2)^2}{2mr^2}\right]}\,dr = \left(n_r + \frac{1}{2}\right)h$$

where $n_r = 0, 1, 2, \ldots$ is the radial quantum number. The Langer correction accounts for the additional phase accumulated near the origin, where the centrifugal barrier acts like a hard wall with a half-integer Maslov contribution [verify: Langer, Phys. Rev. 51, 669 (1937)].

For the Coulomb potential, the Langer-corrected Bohr–Sommerfeld condition gives the exact hydrogen energy levels $E_n = -13.6\,\text{eV}/n^2$ (with $n = n_r + \ell + 1$ the principal quantum number). Without the Langer correction, the $\ell = 0$ states come out wrong by an $O(\hbar^2)$ amount — small but incorrect in principle.

The correction matters primarily for low $\ell$ (especially $\ell = 0$) and for states near the origin. For high-$\ell$ states at large radii, $\ell(\ell+1) \approx (\ell+1/2)^2$ is already a good approximation.

---

## Common misconceptions

**"Tunneling violates energy conservation."** This is the most common misconception, reinforced by pop-science descriptions of "borrowing energy from the vacuum." It is wrong in detail. The tunneling particle has energy $E$ throughout — before, during, and after the barrier. In the forbidden region, the wave function is an exponentially decaying solution to the Schrödinger equation *for a particle with energy E*. There is no energy borrowing. There is no energy violation. There is just the wave function, decaying through the forbidden region and emerging on the other side. Energy is conserved at every step.

**"WKB is just classical mechanics with a wave function slapped on."** No. The $1/\sqrt{p}$ amplitude is classical (it tracks the classical time-spent probability). But the Gamow factor — the exponential tunneling probability — is purely quantum mechanical. Classically, $T = 0$ for any sub-barrier energy. WKB gives $T = e^{-2\gamma}$, which is exponentially small but nonzero. The classical limit would require $\hbar \to 0$, which makes $\gamma \to \infty$ and $T \to 0$. The tunneling is in the quantum correction to classical mechanics, not in classical mechanics itself.

**"The $1/2$ in Bohr–Sommerfeld is a small correction."** It is not small. For the ground state ($n = 0$), the Maslov correction turns $\oint p\,dx = 0$ into $\oint p\,dx = h/2$. For the harmonic oscillator this doubles the ground-state energy — from zero (the classical minimum) to $\hbar\omega/2$. The zero-point energy is a Maslov correction. Without it, the ground state energy prediction is wrong by 100%.

**"WKB gives exact results only for the harmonic oscillator."** WKB also gives exact results for the Coulomb potential (hydrogen atom) and for any potential where the WKB expansion terminates. These are potentials with hidden algebraic symmetries. The property is not unique to the oscillator.

**"The connection formula just patches two regions together arbitrarily."** The connection formula is derived rigorously from the Airy function asymptotics. The Maslov phase of $\pi/4$ per turning point is a theorem — it comes from the $-\pi/4$ phase shift in the cosine form of the Airy function on the classically allowed side. It is not a fitting parameter or a convention.

**"A thick barrier transmits less, so just make the barrier thick enough."** Yes — exponentially less. But "less" does not mean zero. The transmission coefficient is always nonzero for a finite barrier, regardless of how thick it is. Only an infinite barrier gives $T = 0$ exactly.

---

## Exercises

### Warm-up

**5.1** State the WKB validity condition $|d\lambda_\text{dB}/dx| \ll 1$ in words. Then explain in one sentence why it fails at a classical turning point. For each of the following potentials, sketch $\lambda_\text{dB}(x) = h/p(x)$ qualitatively and identify any regions where WKB will break down: (a) a harmonic oscillator at energy $E$; (b) a flat-topped rectangular barrier at energy $E < V_0$; (c) a linear potential $V = Fx$ with $F > 0$. *(Tests: application of the validity condition and identification of its failure modes in specific potentials.)*

**5.2** For the harmonic oscillator $V = \frac{1}{2}m\omega^2 x^2$, the classical turning points at energy $E$ are at $x = \pm\sqrt{2E/m\omega^2}$. (a) Compute the phase-space area $\oint p\,dx$ enclosed by the orbit at energy $E$ — this is the area of an ellipse with semi-axes $\sqrt{2mE}/(m\omega)$ in $x$ and $\sqrt{2mE}$ in $p$. (b) Apply the Bohr–Sommerfeld condition $\oint p\,dx = (n+1/2)h$ and verify you recover $E_n = (n+1/2)\hbar\omega$ exactly. (c) State in one sentence why the WKB result here is exact rather than approximate. *(Tests: phase-space area calculation; Bohr–Sommerfeld applied to the harmonic oscillator; understanding which symmetries make WKB exact.)*

**5.3** Derive the exact transmission coefficient $T_\text{exact}$ for a rectangular barrier of height $V_0$ and width $L$ at energy $E < V_0$. Match the wave function and its derivative at $x = 0$ and $x = L$, using $\psi = Ae^{ikx} + Be^{-ikx}$ for $x < 0$, $\psi = Ce^{\kappa x} + De^{-\kappa x}$ for $0 < x < L$, and $\psi = Fe^{ikx}$ for $x > L$. Show that $T = |F/A|^2$ gives the formula quoted in the chapter. *(Tests: boundary-matching calculation; extraction of the transmission coefficient from wave function continuity conditions.)*

### Apply+

**5.4** An electron with kinetic energy $E = 1\,\text{eV}$ hits a rectangular barrier of height $V_0 = 5\,\text{eV}$ and width $L = 5\,\text{Å}$. (a) Compute $\kappa = \sqrt{2m_e(V_0-E)}/\hbar$ and verify $\kappa \approx 1.0\,\text{Å}^{-1}$. (b) Compute $T_\text{WKB} = e^{-2\kappa L}$. (c) Compute $T_\text{exact}$ using the formula from 5.3. (d) Find the prefactor ratio $T_\text{exact}/T_\text{WKB}$ and compare to the predicted value $16E(V_0-E)/V_0^2$. *(Tests: numerical WKB and exact transmission; identification of the missing prefactor.)*

**5.5** An STM tip is held $d = 5\,\text{Å}$ above a nickel surface with work function $\phi = 5\,\text{eV}$. (a) Compute $\kappa = \sqrt{2m_e\phi}/\hbar$ in Å$^{-1}$. (b) Compute the factor by which the tunneling current changes when $d$ decreases by 1 Å. (c) A surface atom protrudes 0.5 Å above the surrounding surface. By what factor does the tunneling current differ when the tip is directly over the atom versus over the flat region? (d) Explain in one sentence why this exponential sensitivity makes sub-ångström topographic imaging possible. *(Tests: STM current calculation; connecting the Gamow factor to spatial resolution.)*

**5.6** Estimate the Gamow factor for an alpha particle ($m_\alpha = 4\,\text{u}$, $u = 1.66\times 10^{-27}\,\text{kg}$) of energy $E_\alpha = 5.5\,\text{MeV}$ tunneling through the Coulomb barrier of a daughter nucleus with $Z' = 82$ (lead). Use the approximate formula $\gamma \approx (\pi Z' e^2/4\epsilon_0\hbar)\sqrt{m_\alpha/2E_\alpha}$. Then estimate the halflife using attempt frequency $\nu_0 = 10^{21}\,\text{Hz}$. Compare to the uranium-238 case computed in the chapter. *(Tests: Gamow factor calculation for the Coulomb barrier; halflife estimate; understanding how the exponent controls 24 orders of magnitude.)*

**5.7** The cold fusion back-of-envelope. (a) At room temperature $T = 300\,\text{K}$, compute $kT$ in eV. (b) The Coulomb barrier for D-D fusion at nuclear-contact distance ($r_0 \approx 2\,\text{fm}$) is $V_\text{max} = e^2/(4\pi\epsilon_0 r_0)$. Compute $V_\text{max}$ in MeV. (c) Using the approximate Gamow factor $\gamma \approx (\pi e^2/4\epsilon_0\hbar)\sqrt{m_D/2kT}$, compute $\gamma$ and the tunneling probability $e^{-2\gamma}$ at room temperature. Express the result as a power of 10. (d) The claimed power output of 1 W in 1 cm³ of palladium requires roughly $10^{12}$ fusion events per second. Show that the required tunneling rate is inconsistent with your Gamow factor by many orders of magnitude. *(Tests: using the Gamow factor as a falsification tool; order-of-magnitude estimation; recognizing when the exponent decisively refutes a claim.)*

### Produce

**5.8** The Geiger–Nuttall law. (a) Starting from $\log_{10}\tau_{1/2} \approx A(Z') + B(Z')/\sqrt{E_\alpha}$, show that if $\gamma \propto Z'/\sqrt{E_\alpha}$, the log of the halflife is indeed linear in $1/\sqrt{E_\alpha}$ for fixed $Z'$. (b) For polonium-212 ($Z' = 82$, $E_\alpha = 8.78\,\text{MeV}$, $\tau_{1/2} = 3\times 10^{-7}\,\text{s}$) and thorium-232 ($Z' = 90$, $E_\alpha = 4.08\,\text{MeV}$, $\tau_{1/2} = 1.4\times 10^{10}\,\text{yr}$), plot these two points on a $\log_{10}\tau$ vs. $1/\sqrt{E_\alpha}$ graph. From this, estimate the coefficient $B$ in the Geiger–Nuttall formula and compare to the WKB prediction. (c) The ratio of the two halflives is $10^{24}$; the ratio of $1/\sqrt{E_\alpha}$ values is only about 1.5. Confirm that the Gamow exponent $\gamma \propto 1/\sqrt{E_\alpha}$ can reproduce this ratio. *(Tests: derivation of the linear Geiger–Nuttall form from the Gamow factor; numerical check against two known isotopes; connecting the 24-decade range to the exponent.)*

**5.9** WKB quantization for a power-law potential $V(x) = \alpha|x|^n$ (integer $n \geq 1$, symmetric well). (a) Show that the Bohr–Sommerfeld condition implies $E_m \propto m^{2n/(n+2)}$ for large quantum number $m$. (Hint: change variables to make the integral dimensionless; track the scaling of the turning points with $E$.) (b) Verify the $n=2$ case gives $E_m \propto m$ (harmonic oscillator). (c) For $n=1$ (linear potential / "bouncer"), what is the energy scaling? (d) As $n\to\infty$ the potential approaches an infinite square well. What does the formula predict, and does it agree with the exact result $E_m \propto m^2$? *(Tests: WKB applied to a general potential; dimensional analysis in the phase-space integral; checking limiting cases.)*

---

## Still puzzling

**How long does a particle spend inside the barrier?**

This question is surprisingly hard, and not for computational reasons.

There are at least four distinct definitions of "tunneling time" in the literature — the dwell time, the phase time (group delay), the Büttiker–Landauer traversal time, and the Larmor clock time — and they give different numerical answers, sometimes differing by orders of magnitude. Each definition is operationally meaningful in a specific experimental context; none is obviously the "right" one.

Recent attosecond-streaking experiments have measured something at the attosecond scale for laser-induced ionization (which is tunneling through the Coulomb barrier of an atom distorted by the laser field). Eckle and collaborators in 2008 [verify: Eckle et al., Science 322, 1525 (2008)] reported an upper bound on the tunneling time of a few tens of attoseconds — consistent with zero, or with a very short traversal. Whether this corresponds to the phase time, the dwell time, or something else is actively debated [verify: Landsman et al., Optica 1, 343 (2014)].

The pop-science answer — "the particle borrows energy from the vacuum for a brief time and pays it back, allowed by the uncertainty principle" — is wrong in detail. Energy is conserved at every measurement; there is no energy borrowing. There is just the wave, decaying through the forbidden region and emerging on the other side.

The WKB formalism of this chapter gives you the transmission coefficient $T$ but does not give you a tunneling time. The framework is genuinely incomplete here. Saying so honestly is the right move.

---

## The +1 — Simulation Exercise

You are going to build a tunneling simulator with three modes: a stationary $T(E)$ plot, a WKB barrier-shape explorer, and an animated Gaussian wave packet. The deliverable is `05-tunneling-simulator.html` in your working directory.

### The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md, and
PROJECT.md. Read all three first.

Build 05-tunneling-simulator.html: a single self-contained HTML file
using D3 v7 from a CDN (https://cdn.jsdelivr.net/npm/d3@7) and
d3-simple-slider (https://cdn.jsdelivr.net/npm/d3-simple-slider).
No other dependencies. Three modes selectable by tabs:
"Stationary T(E)", "WKB barrier shape", and "Wave packet (CN)".

STATIONARY T(E) MODE
Single SVG 1100 x 600. Plot T vs. E/V_0 on a LOG y-axis from 10^-12 to 1.
X-axis: E/V_0 from 0 to 2.5 (sub-barrier AND above-barrier).
Two curves:
  - T_exact (solid black): use the exact rectangular barrier formula
    T_exact = 1 / (1 + V_0^2 * sinh^2(kappa*L) / (4*E*(V_0-E)))
    for E < V_0; for E > V_0 use the over-barrier formula with sin^2.
  - T_WKB (dashed teal): T_WKB = exp(-2*kappa*L) for E < V_0;
    T_WKB = 1 for E > V_0 (WKB gives perfect transmission above barrier).
Vertical reference line at E/V_0 = 1 labeled "barrier top".
On the log axis, the two curves run parallel below the barrier (same slope),
offset by the smooth prefactor 16*E*(V_0-E)/V_0^2.
Controls: V_0 slider (1 to 10 eV), L slider (1 to 10 Angstrom).

WKB BARRIER SHAPE MODE
Single SVG 1100 x 600 split into two panels:
Left panel (550 wide): Draw V(x) for the selected shape; shade the region
V(x) > E. Draw a horizontal line at the current energy E.
Right panel (550 wide): Plot T_WKB(E) vs E on a LOG y-axis from 10^-12 to 1.
Compute T_WKB numerically: for each E, find the classical turning points
a and b (where V(x) = E) by bisection, then integrate
  gamma = (1/hbar) * integral_a^b sqrt(2m(V(x)-E)) dx
by Simpson's rule on 500 sub-points.
Barrier shapes (selector):
  - Rectangular: V = V_0 for |x| < L/2, 0 elsewhere
  - Triangular: V = V_0*(1 - 2*|x|/L) for |x| < L/2, 0 elsewhere
  - Parabolic: V = V_0*(1 - (2x/L)^2) for |x| < L/2, 0 elsewhere
  - Double barrier: two rectangles of width L_b separated by gap W
    (for double barrier, watch resonant tunneling peaks: T -> 1 at specific E)
Controls: V_0, L, W (for double barrier), shape selector.

WAVE PACKET (CRANK-NICOLSON) MODE
Single SVG 1100 x 600.
Spatial grid: 500 points from x = -50 to +50 in natural units (hbar=m=1).
Barrier centered at x=0 (rectangular, height V_0, width L).
Initial Gaussian wave packet:
  psi(x, t=0) = (2*pi*sigma_x^2)^(-1/4) * exp(-(x-x0)^2/(4*sigma_x^2))
                * exp(i*p0*(x-x0))
with x0 = -20, sigma_x = 2 (default), p0 = 2.

Evolve using Crank-Nicolson (CN):
  (1 + i*H*dt/2) psi(t+dt) = (1 - i*H*dt/2) psi(t)
where H is the discretized 1D Hamiltonian on the grid (tridiagonal matrix).
Use Thomas algorithm for the tridiagonal solve (implement in ~25 lines of
pure JS; do NOT use any library).

Add absorbing boundaries: imaginary potential V_abs(x) = -i*V_max*f(x)
where f(x) is a quadratic ramp from 0 at x=±40 to V_max at x=±50.
This prevents reflection from the grid edges.

Plot |psi(x,t)|^2 as a filled area in blue.
Draw V(x) as a translucent gray shaded region behind the wave function.
Draw a horizontal dashed line at E = p0^2/2 (particle energy).
Below the SVG, display: current time t, norm integral sum|psi|^2*dx.

Pre-compute 2000 time steps at dt=0.05 when user clicks Play. Cache and
play back at 60fps. Show a progress bar during computation.
Controls: V_0, L, p0, sigma_x sliders; Play/Pause/Reset buttons.

GLOBAL PHYSICS
Natural units: hbar = m = 1 throughout. For stationary mode, restore
physical units: m = 9.11e-31 kg, hbar = 1.055e-34 J*s for conversions.
Runtime sanity checks to console:
  - Stationary: at E/V_0 = 0.5, V_0 = 5 eV, L = 5 Ang:
    T_exact should be ~9.5e-5; T_WKB should be ~3.7e-5.
  - Wave packet: before reaching barrier, norm should equal 1 within 1e-4.
  - Wave packet: for V_0 = 0, norm should remain 1 throughout (no absorption).

Comments at every non-trivial physics step. Pure functions for gamma,
T_WKB, T_exact, CN step, and Thomas solve.
```

### Exploration tasks

1. Stationary mode. Set $V_0 = 5\,\text{eV}$, $L = 5\,\text{Å}$. On the log axis, read off the constant offset between the exact and WKB curves in the tunneling regime. Verify this matches $16E(V_0-E)/V_0^2 \approx 2.56$ at $E/V_0 = 0.5$.

2. Stationary mode. Double $L$ from 5 to 10 Å. By what factor does $T$ at $E/V_0 = 0.5$ change? Verify against the WKB prediction $e^{-2\kappa L}$: doubling $L$ should square the exponential suppression.

3. Barrier-shape mode. Switch to the double-barrier configuration. Find a resonant tunneling peak where $T \to 1$. Record the energy. The condition for a resonance is that the inter-barrier well supports a quasi-bound state — the resonant energy should match the square-well bound states in the gap.

4. Wave packet mode. Set $V_0 = 5$, $L = 5$, $p_0 = 2$ (so $E = 2 < V_0$). Play. Watch the wave packet split: most reflects, a small transmitted piece emerges on the right. Write one sentence describing what you see.

5. Wave packet mode. Increase $p_0$ to $\sqrt{10} \approx 3.16$ (so $E = V_0$). Repeat. Now increase $p_0$ to 4 ($E > V_0$). How does the transmitted fraction change across these three cases?

---

## References

- Griffiths, D. J. & Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press (2018), §9.1–9.3. [verify]
- Liboff, R. L. *Introductory Quantum Mechanics*, 4th ed. Addison-Wesley (2003), §7.7, §7.10. [verify]
- Gamow, G. "Zur Quantentheorie des Atomkernes." *Zeitschrift für Physik* 51, 204–212 (1928). [verify]
- Gurney, R. W. & Condon, E. U. "Wave Mechanics and Radioactive Disintegration." *Nature* 122, 439 (1928). [verify]
- Gurney, R. W. & Condon, E. U. "Quantum Mechanics and Radioactive Disintegration." *Physical Review* 33, 127–140 (1929). [verify]
- Geiger, H. & Nuttall, J. M. "The ranges of the α particles from various radioactive substances and a relation between range and period of transformation." *Philosophical Magazine* 22, 613–621 (1911). [verify]
- Geiger, H. & Nuttall, J. M. "The ranges of the α particles from various radioactive substances and a relation between range and period of transformation." *Philosophical Magazine* 23, 439–445 (1912). [verify]
- Langer, R. E. "On the connection formulas and the solutions of the wave equation." *Physical Review* 51, 669–676 (1937). [verify]
- Binnig, G. & Rohrer, H. "Scanning tunneling microscopy." *Physical Review Letters* 49, 57–61 (1982). [verify]
- Atkinson, R. & Houtermans, F. G. "Zur Frage der Aufbaumöglichkeit der Elemente in Sternen." *Zeitschrift für Physik* 54, 656–665 (1929). [verify]
- Fowler, R. H. & Nordheim, L. "Electron Emission in Intense Electric Fields." *Proceedings of the Royal Society of London A* 119, 173–181 (1928). [verify]
- Löwdin, P.-O. "Proton Tunneling in DNA and Its Biological Implications." *Reviews of Modern Physics* 35, 724–732 (1963). [verify]
- Slocombe, L. *et al.* "An open quantum systems approach to proton tunnelling in DNA." *Communications Physics* 5, 109 (2022). [verify]
- Eckle, P. *et al.* "Attosecond Ionization and Tunneling Delay Time Measurements in Helium." *Science* 322, 1525–1529 (2008). [verify]
- Landsman, A. S. *et al.* "Ultrafast resolution of tunneling delay time." *Optica* 1, 343–349 (2014). [verify]
- Bender, C. M. & Orszag, S. A. *Advanced Mathematical Methods for Scientists and Engineers*. McGraw-Hill (1978), Ch. 10. [verify]
