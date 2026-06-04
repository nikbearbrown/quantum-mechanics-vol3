# Chapter 4 — The Variational Principle

## TL;DR

- When you cannot solve the Schrödinger equation exactly, guess a wave function, compute its energy expectation value, and optimize over your guess. The result is *guaranteed* to be above the true ground-state energy — and the better your guess, the tighter the bound.
- The variational theorem (⟨H⟩ ≥ E₀) is a three-line proof with surprisingly sharp teeth: it bounds helium's ground state to within 2% with a single adjustable parameter, and underpins all of modern quantum chemistry.
- The chapter covers the variational theorem and its proof; parameterized trial functions and the optimization procedure; the Rayleigh–Ritz generalized eigenvalue problem; helium as the flagship example (effective charge Z̃ = 27/16, E ≈ −77.5 eV vs. −78.98 eV experimental); the H₂⁺ LCAO bonding/antibonding analysis; and the limits of the method (upper bound only; excited states need orthogonality).

**Learning objectives**

1. **Remember** the variational theorem and reproduce its proof from the expansion in the exact eigenbasis. *(Bloom: Remember/Understand)*
2. **Apply** the optimization procedure to a parameterized trial function, including taking a derivative and solving for the optimal parameter. *(Bloom: Apply)*
3. **Analyze** the helium ground-state variational calculation: identify the Hamiltonian decomposition, evaluate each expectation value, and interpret the physical meaning of the effective charge Z̃ = 27/16. *(Bloom: Analyze)*
4. **Evaluate** the LCAO bonding and antibonding energies for H₂⁺ as functions of internuclear separation, and explain why only one yields a bound state. *(Bloom: Evaluate)*
5. **Critique** the limits of the variational method: explain why the energy bound is one-sided, why wave functions are less accurate than energies, and why excited-state bounds require an orthogonality constraint. *(Bloom: Evaluate)*

---

In 1929, Egil Hylleraas was a Norwegian physicist working in Copenhagen on a problem that had been resistant since the year quantum mechanics was born: the ground-state energy of helium. Helium has two electrons, and their mutual repulsion makes the Schrödinger equation unseparable. Nobody had a closed-form solution. The question was not whether helium had a ground state — obviously it did, there it was in the periodic table — but whether quantum mechanics could *predict* its energy accurately enough to trust.

Hylleraas tried something direct. He wrote down a trial wave function that had the right symmetry (symmetric under electron exchange, since both electrons are in singlet spin states), included the key physics (each electron near the nucleus, with some accounting for the other's repulsive influence), and computed the expectation value of the full Hamiltonian. The trial state was not the exact ground state — he knew that — but there was a theorem: *any* normalized trial state has an energy expectation value at or above the true ground state energy. The minimum over any family of trial states gives you a guaranteed upper bound.

Hylleraas pushed that bound down to −77.5 eV with a single variational parameter. The experimental value was −78.98 eV. With six parameters he got to −78.7 eV. With several dozen terms explicitly depending on the inter-electron distance, subsequent workers pushed the agreement to eleven significant figures. The theorem held throughout: the bound approached from above, never going below the truth.

This is the variational principle. It is the mathematical permission slip for a huge fraction of all of quantum mechanics and quantum chemistry. When no exact solution exists, you guess wisely, compute, and optimize. The theorem tells you which direction you are wrong.

---

## The theorem and its proof

Let $\hat{H}$ be any Hermitian Hamiltonian with a discrete spectrum, and let $E_0 \leq E_1 \leq E_2 \leq \cdots$ be its eigenvalues with corresponding eigenstates $|n\rangle$. The exact ground state $|0\rangle$ is whatever it is — we do not know it. Now take any normalized state $|\psi\rangle$, not necessarily an eigenstate. The claim is:

$$\boxed{\langle \psi | \hat{H} | \psi \rangle \geq E_0}$$

The proof is three lines. Expand $|\psi\rangle$ in the exact eigenbasis: $|\psi\rangle = \sum_n c_n |n\rangle$. Since $|\psi\rangle$ is normalized, $\sum_n |c_n|^2 = 1$. Compute the expectation value:

$$\langle \hat{H} \rangle = \sum_n |c_n|^2 E_n \geq E_0 \sum_n |c_n|^2 = E_0$$

The inequality in the middle follows because every $E_n \geq E_0$ — the ground state is the minimum. That is the whole proof. No approximation; no restriction on $|\psi\rangle$ beyond normalization.

Equality holds if and only if $c_n = 0$ for every $n > 0$, meaning $|\psi\rangle = e^{i\phi}|0\rangle$ — the trial state *is* the exact ground state (up to a global phase). Every other trial state gives a strict upper bound.

Three things follow immediately from the structure of the proof.

**The method cannot go below.** There is no normalized state with $\langle \hat{H}\rangle < E_0$. If you minimize $\langle \hat{H}\rangle$ over your trial family and get a result 0.1 eV below the experimental value, you have made an error somewhere — possibly a normalization mistake, possibly a sign error in the kinetic energy. The theorem is a sanity check.

**Lower means closer.** Within any fixed family of trial states, a lower variational energy is a tighter upper bound. The game is to push the bound down. But "closer energy" does not automatically mean "closer wave function" — more on this in the Limits section.

**No small parameter needed.** Perturbation theory requires $\lambda \hat{H}'$ to be small. The variational method requires only that you can compute $\langle \hat{H}\rangle$. For systems where no obvious small parameter exists — helium, most molecules — the variational approach is the natural tool.

---

## The optimization procedure

The practical procedure: choose a trial function $\psi(\mathbf{r};\alpha)$ depending on one or more variational parameters $\alpha = (\alpha_1, \alpha_2, \ldots)$. Define the variational energy:

$$E_V(\alpha) = \frac{\langle \psi(\alpha)|\hat{H}|\psi(\alpha)\rangle}{\langle\psi(\alpha)|\psi(\alpha)\rangle}$$

(The denominator handles the case where the trial function is not normalized for every $\alpha$.) Minimize $E_V$ over the parameters by setting:

$$\frac{\partial E_V}{\partial \alpha_i} = 0 \quad \text{for each } i$$

and solving the resulting system of equations. The minimum value $E_V^* = \min_\alpha E_V(\alpha)$ is the best upper bound achievable within this trial family, and the optimal $\alpha^*$ gives the best trial state in the family.

**A clean first example.** Consider the one-dimensional harmonic oscillator with a Gaussian trial function:

$$\psi(x;\alpha) = A\,e^{-\alpha x^2}$$

Normalization: $A = (2\alpha/\pi)^{1/4}$. The expectation values:

$$\langle \hat{T}\rangle = \frac{\hbar^2 \alpha}{2m}, \qquad \langle \hat{V}\rangle = \frac{m\omega^2}{8\alpha}$$

so

$$E_V(\alpha) = \frac{\hbar^2\alpha}{2m} + \frac{m\omega^2}{8\alpha}$$

Minimize over $\alpha$: $\partial E_V/\partial\alpha = \hbar^2/(2m) - m\omega^2/(8\alpha^2) = 0$ gives $\alpha^* = m\omega/(2\hbar)$. Substituting back:

$$E_V^* = \frac{\hbar\omega}{2} = E_0$$

The trial function gives the *exact* ground-state energy. This is not a coincidence: the true ground-state wave function $\psi_0 = (\pi\hbar/m\omega)^{-1/4}e^{-m\omega x^2/2\hbar}$ is itself a Gaussian, so the trial family contains the exact answer. When your trial family is rich enough to contain the true ground state, the variational method finds it exactly. This is reassuring but not always achievable.

---

## The Rayleigh–Ritz method

When the trial function is a linear combination of $N$ basis functions — $|\psi\rangle = \sum_{j=1}^N c_j |\phi_j\rangle$ — the optimization over the coefficients $\{c_j\}$ leads to a standard linear-algebra problem. Setting $\partial E_V/\partial c_i^* = 0$ gives:

$$\sum_j H_{ij} c_j = E_V \sum_j S_{ij} c_j$$

where $H_{ij} = \langle\phi_i|\hat{H}|\phi_j\rangle$ is the Hamiltonian matrix and $S_{ij} = \langle\phi_i|\phi_j\rangle$ is the overlap matrix. In matrix form: $\mathbf{H}\mathbf{c} = E_V\,\mathbf{S}\mathbf{c}$. This is the **generalized eigenvalue problem**. When the basis is orthonormal ($\mathbf{S} = \mathbf{1}$) it reduces to the ordinary eigenvalue problem $\mathbf{H}\mathbf{c} = E_V\mathbf{c}$.

The lowest eigenvalue of $\mathbf{H}\mathbf{c} = E_V\mathbf{S}\mathbf{c}$ is the best upper bound on $E_0$ achievable in the $N$-dimensional trial space. As $N \to \infty$ and the basis becomes complete, the lowest eigenvalue converges to $E_0$ from above. This is the foundation of computational quantum chemistry: Hartree–Fock theory uses a single Slater determinant; configuration interaction (CI) adds more determinants; at the limit of a complete basis, CI gives the exact energy.

**An illustrative numerical example.** For the hydrogen atom, the exact ground state has energy $-1/2$ Hartree. Using four Gaussian basis functions $\chi_p(r) = e^{-\alpha_p r^2}$ with exponents $\alpha_1 = 13.008,\, \alpha_2 = 1.962,\, \alpha_3 = 0.445,\, \alpha_4 = 0.122$, the generalized eigenvalue problem gives $E_V = -0.4993$ Hartree — an error of only 0.14%. No differential equation was solved. The Hamiltonian matrix elements were integrals over Gaussians, computable analytically. Scale this to hundreds of basis functions and you have modern quantum chemistry.

---

## Worked example: the helium ground-state energy

Helium has nuclear charge $Z = 2$ and two electrons at positions $\mathbf{r}_1$ and $\mathbf{r}_2$. The Hamiltonian is:

$$\hat{H} = \frac{\hat{p}_1^2}{2m} + \frac{\hat{p}_2^2}{2m} - \frac{Ze^2}{4\pi\epsilon_0 r_1} - \frac{Ze^2}{4\pi\epsilon_0 r_2} + \frac{e^2}{4\pi\epsilon_0|\mathbf{r}_1 - \mathbf{r}_2|}$$

The first four terms are the kinetic energies and electron-nuclear attractions; the last term is the electron-electron repulsion. That last term makes the equation unseparable and prevents an exact solution.

**The trial function.** Each electron is in a hydrogen-like 1s orbital, but with an adjustable effective nuclear charge $\tilde{Z}$ instead of the bare $Z = 2$. Physically, each electron partly screens the nucleus from the other:

$$\psi(\mathbf{r}_1,\mathbf{r}_2;\tilde{Z}) = \psi_{1s}(\tilde{Z};\mathbf{r}_1)\,\psi_{1s}(\tilde{Z};\mathbf{r}_2), \quad \psi_{1s}(\tilde{Z};\mathbf{r}) = \frac{1}{\sqrt{\pi}}\left(\frac{\tilde{Z}}{a_0}\right)^{3/2}e^{-\tilde{Z}r/a_0}$$

The single parameter $\tilde{Z}$ encodes the screening hypothesis.

**The trick: rewrite the Hamiltonian.** Add and subtract $\tilde{Z}e^2/(4\pi\epsilon_0 r_1)$ and the same for electron 2:

$$\hat{H} = \underbrace{\left[\frac{\hat{p}_1^2}{2m} - \frac{\tilde{Z}e^2}{4\pi\epsilon_0 r_1}\right]}_{\hat{H}_1(\tilde{Z})} + \underbrace{\left[\frac{\hat{p}_2^2}{2m} - \frac{\tilde{Z}e^2}{4\pi\epsilon_0 r_2}\right]}_{\hat{H}_2(\tilde{Z})} + \underbrace{\frac{(\tilde{Z}-Z)e^2}{4\pi\epsilon_0 r_1} + \frac{(\tilde{Z}-Z)e^2}{4\pi\epsilon_0 r_2}}_{\text{screening correction}} + \underbrace{\frac{e^2}{4\pi\epsilon_0|\mathbf{r}_1-\mathbf{r}_2|}}_{\text{e-e repulsion}}$$

The trial state $\psi(\tilde{Z})$ is the *exact eigenstate* of $\hat{H}_1(\tilde{Z}) + \hat{H}_2(\tilde{Z})$ with eigenvalue $2E_1(\tilde{Z}) = -\tilde{Z}^2 m_e c^2\alpha^2$ (twice the hydrogen ground-state energy at effective charge $\tilde{Z}$, where $\alpha = e^2/4\pi\epsilon_0\hbar c \approx 1/137$ is the fine-structure constant). So:

$$\langle\hat{H}\rangle = 2E_1(\tilde{Z}) + \frac{(\tilde{Z}-Z)e^2}{4\pi\epsilon_0}\left\langle\frac{1}{r_1}\right\rangle \times 2 + \left\langle\frac{e^2}{4\pi\epsilon_0|\mathbf{r}_1-\mathbf{r}_2|}\right\rangle$$

For a hydrogen-like 1s orbital at charge $\tilde{Z}$: $\langle 1/r\rangle = \tilde{Z}/a_0$. The electron-electron repulsion integral evaluates to $5\tilde{Z}e^2/(8\cdot 4\pi\epsilon_0 a_0)$ — a standard integral done by expanding $1/|\mathbf{r}_1-\mathbf{r}_2|$ in Legendre polynomials. Combining everything and expressing in convenient units (using $E_1 = -13.6\,\text{eV}$ for hydrogen):

$$E_V(\tilde{Z}) = \left[2\tilde{Z}^2 - 4Z\tilde{Z} + \frac{5}{4}\tilde{Z}\right]\frac{m_e e^4}{2(4\pi\epsilon_0)^2\hbar^2}$$

In atomic units where the hydrogen ground-state energy is $-1/2$ Hartree:

$$E_V(\tilde{Z}) = \left(2\tilde{Z}^2 - 4Z\tilde{Z} + \frac{5}{4}\tilde{Z}\right)\,\text{Hartree}$$

**Minimize over $\tilde{Z}$.** Set $\partial E_V/\partial \tilde{Z} = 0$:

$$4\tilde{Z} - 4Z + \frac{5}{4} = 0 \quad\Longrightarrow\quad \tilde{Z} = Z - \frac{5}{16}$$

For helium with $Z = 2$:

$$\boxed{\tilde{Z} = 2 - \frac{5}{16} = \frac{27}{16} \approx 1.6875}$$

**Physical interpretation.** Each electron sees an effective nuclear charge of 27/16 rather than 2. The reduction of $5/16$ is the screening: the other electron sits, on average, between the nucleus and the electron in question, shielding $5/16$ of a proton charge. This is the concept of electron shielding, which recurs throughout atomic physics and chemistry.

**The numerical result.** Substituting $\tilde{Z} = 27/16$ back into $E_V$:

$$E_V^* = -2\left(\frac{27}{16}\right)^2\,\text{Hartree} = -2 \times 2.848\,\text{Hartree} \approx -77.5\,\text{eV}$$

The experimental ground-state energy of helium is $-78.98\,\text{eV}$. The error is about 2%.

**The lesson: what a 2% error buys.** The variational estimate is not exact, but it is useful. Compare to first-order perturbation theory with $Z = 2$ fixed: treating the electron-electron repulsion as a perturbation gives $-74.8\,\text{eV}$, a 5% error. The variational method outperforms perturbation theory because it optimizes over the parameter that matters most — the effective charge — rather than trusting the bare Hamiltonian at every step.

**The limit: how do you do better?** More flexible trial functions. With a two-parameter trial that adds an explicit $s$-wave angular correlation, the bound improves to $-77.8\,\text{eV}$. With a Hylleraas-type trial that depends explicitly on the inter-electron distance $r_{12} = |\mathbf{r}_1 - \mathbf{r}_2|$, and dozens of terms, the helium ground-state energy is known to eleven significant figures. Throughout, every result is an upper bound — and every improvement pushes that bound lower.

---

## The H₂⁺ molecular ion: LCAO and the chemical bond

The hydrogen molecular ion H₂⁺ — one electron, two protons separated by distance $R$ — is the simplest molecule. It has an exact solution in prolate spheroidal coordinates, but the variational approach with a minimal trial basis is more illuminating because it shows where chemical bonds come from.

**The trial function.** Label the two protons $A$ and $B$. Let $|A\rangle$ and $|B\rangle$ be hydrogen 1s orbitals centered on each proton:

$$\langle\mathbf{r}|A\rangle = \psi_{1s}(\mathbf{r} - \mathbf{R}_A) = \frac{1}{\sqrt{\pi}a_0^{3/2}}\,e^{-|\mathbf{r}-\mathbf{R}_A|/a_0}$$

The trial function is a **linear combination of atomic orbitals** (LCAO):

$$|\psi_\pm\rangle = \frac{|A\rangle \pm |B\rangle}{\sqrt{2 \pm 2S_{AB}}}$$

where $S_{AB} = \langle A|B\rangle$ is the overlap integral. The symmetric combination $|+\rangle$ is the bonding orbital; the antisymmetric combination $|-\rangle$ is the antibonding orbital. The normalization factors come from expanding $\langle\psi_\pm|\psi_\pm\rangle = 1 \pm S_{AB}$ (using the fact that $\langle A|A\rangle = \langle B|B\rangle = 1$).

The overlap integral has the analytic form:

$$S_{AB}(R) = e^{-R/a_0}\left(1 + \frac{R}{a_0} + \frac{R^2}{3a_0^2}\right)$$

At $R = 0$, $S_{AB} = 1$ (the two orbitals are identical); at $R \to \infty$, $S_{AB} \to 0$ (no overlap). The function decreases monotonically and smoothly.

**The variational energies.** Define matrix elements:

$$H_{AA} = \langle A|\hat{H}|A\rangle, \quad H_{AB} = \langle A|\hat{H}|B\rangle$$

where the full Hamiltonian includes the kinetic energy, both electron-nuclear attractions, and the proton-proton repulsion $e^2/R$. The variational energies are:

$$E_\pm(R) = \frac{H_{AA} \pm H_{AB}}{1 \pm S_{AB}}$$

Computing $H_{AA}$ and $H_{AB}$ involves evaluating Coulomb integrals of the hydrogen wave function against the potential from the *other* proton — integrals that can be done in prolate spheroidal coordinates and are tabulated in standard texts. The results, as functions of $R$, give:

- $E_+(R)$: the bonding energy. This has a **minimum** at $R \approx 1.3\,\text{Å}$ (experimental: $1.06\,\text{Å}$) with a binding energy of about $1.77\,\text{eV}$ (experimental: $2.65\,\text{eV}$). The LCAO trial overestimates the bond length and underestimates the binding energy because it does not allow the atomic orbitals to distort as the protons approach.

- $E_-(R)$: the antibonding energy. This is **purely repulsive** — it has no minimum and increases toward zero from below as $R \to \infty$. An electron in the antibonding orbital does not bind the two protons.

**Why does only one bind?** The bonding orbital $|+\rangle$ builds up electron density *between* the two protons — the wave function adds constructively in the midplane. That density is simultaneously attracted to both nuclei, pulling them together. The antibonding orbital $|-\rangle$ has a nodal plane between the protons where the wave function vanishes by destructive interference; the electron density is pushed *away* from the midplane, providing no glue and actually increasing the repulsion.

There is also a kinetic energy contribution. The bonding orbital is smooth and spread over a larger volume; its kinetic energy is lower. The antibonding orbital is sharply curved around the nodal plane; its kinetic energy is higher. Both contributions — potential energy reduction from increased density between nuclei, and kinetic energy reduction from delocalization — contribute to the bond.

The LCAO result is quantitatively imperfect but physically exactly right. Every covalent bond in chemistry is a version of this story: two atomic orbitals overlap, form bonding and antibonding combinations, and the electrons go into the lower one.

---

## Common misconceptions

**"The variational method always finds the exact answer."** It finds the exact answer only when the trial family contains the exact ground state, as in the Gaussian-harmonic-oscillator example. For the helium atom with a single effective-charge parameter, the exact wave function is not of the factored form $\psi(\tilde{Z};\mathbf{r}_1)\psi(\tilde{Z};\mathbf{r}_2)$ — it has explicit dependence on $r_{12}$ — so the variational minimum is above the true ground state. The method is exact within the trial family, not beyond it.

**"A lower variational energy means a better wave function."** This is subtle. The energy is a bilinear functional of the wave function; a first-order error in $\psi$ produces only a *second-order* error in $\langle \hat{H}\rangle$. So the energy can be very close to the true answer while the wave function is still first-order wrong away from the minimum. If you need accurate electron densities, matrix elements of operators other than $\hat{H}$, or accurate descriptions of the wave function in classically forbidden regions, you cannot rely on a good variational energy to guarantee accuracy there. Energies are cheaper to optimize than wave functions.

**"The variational method gives an upper bound to every eigenvalue."** Only the ground state is directly bounded. To bound excited-state energies, you need either: (a) knowledge of the exact ground state so you can impose the orthogonality constraint $\langle\psi|\psi_0\rangle = 0$; or (b) to work in a symmetry sector from which the ground state is excluded. If the ground state is even-parity, a trial function in the odd-parity sector cannot overlap with it, so $\langle\hat{H}\rangle \geq E_1$ (the first odd-parity eigenvalue). This is the practical excited-state tool.

**"LCAO gives the bond length and binding energy."** LCAO with a minimal basis (one 1s per proton) overestimates the bond length and underestimates the binding energy by substantial factors. Improving the basis — adding polarization functions that allow the orbitals to distort toward the other proton — brings the result closer to experiment. The physical picture (bonding = electron density between nuclei) is correct; the numbers require a richer basis.

**"The variational principle is a trick for textbook problems."** It is the foundation of computational quantum chemistry. Hartree–Fock theory minimizes the energy over all possible Slater determinants — a variational calculation in an infinite-dimensional space. DFT reformulates the same problem in terms of electron density. The methods that compute drug molecule energies and material band gaps at petaflop scale are all applications of this theorem.

---

## Limits of the method

**One-sided.** The variational principle gives a *guaranteed upper bound* and nothing else. It tells you the energy is at most $E_V^*$. It does not tell you how far below $E_V^*$ the true ground state lies. You can have a bad trial function and still get a low energy — in that case your energy is a tighter bound, but your wave function may be quite wrong.

**Upper bound only.** There is no variational lower bound theorem of the same character. There are methods that provide lower bounds — the Temple formula, for instance — but they require additional inputs (bounds on the spectrum) and are much less commonly used.

**Trial family dependence.** The variational energy is the minimum over a specific trial family. If that family is poorly chosen — wrong symmetry, wrong nodal structure, wrong asymptotic behavior — the minimum may sit far above $E_0$. For instance, using a trial function that does not decay at infinity will not give a good bound on a bound state. Choosing the trial family well is where physical intuition earns its money.

**Excited states.** As noted above, bounding excited-state energies requires either knowing the ground state or exploiting symmetry to exclude it from the trial space. The min-max theorem provides the formal generalization: the $k$-th variational eigenvalue in an $N$-dimensional trial space is an upper bound on the $k$-th exact eigenvalue, as long as the trial space is chosen to exclude the lower $k-1$ eigenvalues.

---

## Exercises

### Warm-up

**4.1** For the one-dimensional infinite square well of width $L$, the exact ground-state energy is $E_0 = \pi^2\hbar^2/(2mL^2)$. Consider the trial function $\psi_\text{trial}(x) = A\,x(L-x)$ for $0 < x < L$ and zero elsewhere. (a) Normalize $\psi_\text{trial}$ and find $A$. (b) Compute $\langle\hat{T}\rangle = \langle\psi|\hat{p}^2/2m|\psi\rangle$ using integration by parts twice. (c) Since there is no potential energy inside the well, $E_V = \langle\hat{T}\rangle$. Find the ratio $E_V/E_0$ and verify the variational inequality. (d) The error is about 1.3%. What feature of $x(L-x)$ makes it a reasonable guess for the ground state? *(Tests: normalization, kinetic-energy matrix element by integration by parts, verification of the bound.)*

**4.2** Prove the variational theorem from scratch. (a) Write $|\psi\rangle = \sum_n c_n|n\rangle$ in the exact eigenbasis and use the completeness relation $\sum_n |c_n|^2 = 1$ to show $\langle\hat{H}\rangle \geq E_0$. (b) State precisely the condition under which equality holds and interpret it physically. (c) Does the proof require anything about $\hat{H}$ beyond Hermiticity and the existence of a discrete spectrum? Identify the step where the discrete spectrum is used. *(Tests: the core proof; identification of when the bound is saturated; critical reading of assumptions.)*

**4.3** For the delta-function potential $\hat{H} = -(\hbar^2/2m)d^2/dx^2 - \alpha\delta(x)$, use the Gaussian trial function $\psi(x;b) = (b/\pi)^{1/4}e^{-bx^2/2}$. (a) Compute $\langle\hat{T}\rangle = \hbar^2b/(4m)$. (b) Use $\langle\delta(x)\rangle = |\psi(0)|^2 = \sqrt{b/\pi}$ to find $\langle\hat{V}\rangle = -\alpha\sqrt{b/\pi}$. (c) Minimize $E_V(b)$ over $b$. (d) The exact ground-state energy is $E_0 = -m\alpha^2/(2\hbar^2)$; the variational result is $E_V = -m\alpha^2/(\pi\hbar^2)$. Compute the ratio $E_V/E_0$ and verify it satisfies the bound. *(Tests: variational integral with a delta function; comparing the variational result to an exact answer when the trial family does not contain the exact solution.)*

### Apply+

**4.4** Helium atom with a two-electron trial function $\psi(\mathbf{r}_1,\mathbf{r}_2;\tilde{Z}) = [({\tilde{Z}}^3/\pi a_0^3)]e^{-\tilde{Z}(r_1+r_2)/a_0}$. (a) Starting from the decomposed Hamiltonian in the Core Development section, write out $E_V(\tilde{Z})$ as a sum of three terms: $2E_1(\tilde{Z})$, the screening correction, and the electron-electron repulsion $5\tilde{Z}e^2/(8\cdot 4\pi\epsilon_0 a_0)$. (b) Differentiate with respect to $\tilde{Z}$ and find the optimal value $\tilde{Z}^* = Z - 5/16$. (c) Evaluate $E_V(\tilde{Z}^*)$ numerically in eV for $Z = 2$. (d) How does this compare to first-order perturbation theory ($-74.8\,\text{eV}$) and to experiment ($-78.98\,\text{eV}$)? Which method is closer, and why? *(Tests: the complete helium calculation; comparison of variational and perturbative approaches; physical interpretation of $\tilde{Z}^*$.)*

**4.5** For H₂⁺ at large separation $R \to \infty$, the bonding energy $E_+(R)$ should approach the hydrogen ground-state energy $E_1 = -13.6\,\text{eV}$ plus the proton-proton repulsion $e^2/(4\pi\epsilon_0 R) \to 0$. (a) Verify that $S_{AB}(R) \to 0$ and $H_{AB} \to 0$ in this limit, so $E_+(R) \to H_{AA}$. (b) Compute $H_{AA} = \langle A|\hat{H}|A\rangle$ by noting that $|A\rangle$ is the exact eigenstate of the hydrogen Hamiltonian centered on proton $A$ with eigenvalue $E_1$, plus a perturbation $-e^2/(4\pi\epsilon_0|{\bf r} - {\bf R}_B|)$ from the other proton. What is the leading correction in the $R \to \infty$ limit? (c) At very short separation $R \to 0$, the nuclear charges merge into a single charge $Z = 2$ (helium nucleus). What energy should $E_+(R)$ approach? Does the LCAO trial function give the right limit? Explain why or why not. *(Tests: asymptotic analysis of LCAO energies; connections between H₂⁺ and helium; limits of the minimal basis set.)*

**4.6** A Gaussian basis for the hydrogen 1s orbital. Consider the single-term approximation $\phi(r;\alpha) = (2\alpha/\pi)^{3/4}e^{-\alpha r^2}$ (a Gaussian trial for hydrogen, which has a true 1s that is exponential, not Gaussian). (a) Compute $\langle\hat{T}\rangle = 3\hbar^2\alpha/(2m)$ for this trial state in 3D. (b) Compute $\langle V\rangle = \langle -e^2/(4\pi\epsilon_0 r)\rangle = -(e^2/4\pi\epsilon_0)\sqrt{8\alpha/\pi}$ using the known integral $\int_0^\infty r \cdot e^{-2\alpha r^2}dr = 1/(4\alpha)$. (c) Minimize $E_V(\alpha)$ and find the optimal $\alpha^*$. (d) The exact hydrogen ground-state energy is $-13.6\,\text{eV}$; what does your Gaussian trial give? What fraction of the binding energy does one Gaussian capture? *(Tests: 3D variational integral; comparison of exponential vs Gaussian trial functions; understanding why the Gaussian misses some of the exact energy.)*

### Produce

**4.7** Design a variational trial function for the three-dimensional harmonic oscillator $\hat{H} = \hat{p}^2/2m + m\omega^2r^2/2$ that you expect to be exactly optimal. (a) State your trial function and the variational parameter(s). (b) Prove that it gives the exact ground-state energy $E_0 = 3\hbar\omega/2$. (c) Now consider an anharmonic 3D oscillator $\hat{H} = \hat{p}^2/2m + m\omega^2r^2/2 + \lambda r^4$. For small $\lambda > 0$, your Gaussian trial function from (a) is no longer exact. Show that the optimal width parameter $\alpha^*(\lambda)$ shifts from its harmonic value, and compute the leading correction to $E_V^*$ at first order in $\lambda$. Compare this to the first-order perturbation theory result from Chapter 2. *(Tests: design and proof of an exact variational state; perturbative analysis of the anharmonic correction within the Gaussian family.)*

**4.8** Use the Rayleigh–Ritz method with a two-function basis for the infinite square well: $\phi_1 = \sqrt{30/L^5}\,x(L-x)$ and $\phi_2 = \sqrt{840/L^7}\,x(L-x)^2$, both on $[0,L]$. (a) Compute the $2\times 2$ Hamiltonian matrix $H_{ij} = \langle\phi_i|\hat{H}|\phi_j\rangle$ where $\hat{H} = -(\hbar^2/2m)d^2/dx^2$. (b) Both basis functions are already orthonormal (verify for $\langle\phi_1|\phi_2\rangle$); confirm whether or not they are orthogonal. If not, also compute the $2\times 2$ overlap matrix $S_{ij}$. (c) Find the lowest eigenvalue of the generalized (or ordinary, if they are orthogonal) eigenvalue problem. Compare to $E_0 = \pi^2\hbar^2/(2mL^2)$. (d) By adding this second basis function, did the variational bound improve? By how much? *(Tests: construction of the Rayleigh–Ritz matrix; generalized eigenvalue problem; quantitative improvement from a richer trial space.)*

---

## Still puzzling

The variational principle gives you an upper bound and tells you which direction you are wrong. It does not tell you how *far* wrong you are. For the helium atom, the gap between $-77.5\,\text{eV}$ and $-78.98\,\text{eV}$ is about 1.5 eV, which is larger than the thermal energy at room temperature and larger than the accuracy required for chemical reaction energy calculations ($\sim 1\,\text{kcal/mol} \approx 0.04\,\text{eV}$). The trial function with a single effective charge is not good enough for chemistry.

Hylleraas made it better by including the inter-electron distance $r_{12}$ explicitly in the trial function. Why does that work so much better? Because the electron-electron correlation — the tendency of the two electrons to avoid each other — is precisely captured by $r_{12}$-dependent terms. The product trial function $\psi(\tilde{Z};\mathbf{r}_1)\psi(\tilde{Z};\mathbf{r}_2)$ treats the two electrons as *independent* given the effective charge; it gets the mean repulsion right but misses the *fluctuations*. The Hylleraas terms add back the correlation energy.

This is the language of modern electronic structure theory: Hartree-Fock captures exchange (the Pauli exclusion principle) but misses correlation; configuration interaction and coupled-cluster methods add correlation perturbatively; the difference between Hartree-Fock and the exact energy is the correlation energy, and it is always negative (the true answer is lower than Hartree-Fock). Computing it accurately is still the hard part of quantum chemistry.

There is also a deeper question about the relationship between energy and wave function quality. It is a theorem that the variational energy converges to $E_0$ at a *quadratic* rate in the wave-function error, while the wave function itself converges only linearly. This means you can get 99% of the binding energy with a wave function that is still 10% wrong in shape. If you need the wave function — to compute transition matrix elements, electron densities, or response properties — you need more than a tight energy bound. This is why quantum chemists track both energy convergence and wave-function convergence separately, and why "the energy is good" is not a sufficient condition for "the calculation is reliable."

---

## The +1 — Simulation Exercise

You are going to build a two-mode variational explorer that makes the optimization visible. The deliverable is `04-variational-explorer.html` in your working directory.

### The simulation prompt

```
You are working in my directory which contains CLAUDE.md, DESIGN.md, and
PROJECT.md. Read all three first.

Build 04-variational-explorer.html: a single self-contained HTML file
using D3 v7 from a CDN (https://cdn.jsdelivr.net/npm/d3@7) and
d3-simple-slider (https://cdn.jsdelivr.net/npm/d3-simple-slider).
No other dependencies. Two modes selectable by tabs:
"Helium atom (E vs Z-tilde)" and "H2+ bonding".

HELIUM MODE
Single SVG canvas 1000 x 500.
Main panel (left 600 wide): Plot E_V(Z_tilde) in eV on the y-axis
(range: -85 to -65 eV) vs. Z_tilde on the x-axis (range 1.0 to 2.5).
The variational energy formula is:
  E_V(Z_tilde) = [2*Z_tilde^2 - 4*Z*Z_tilde + (5/4)*Z_tilde] * Hartree_to_eV
where Z = 2 and 1 Hartree = 27.211 eV.
Draw the E_V curve in teal. Mark the minimum with a vertical dashed line
at Z_tilde = 27/16 = 1.6875 and annotate: "Z-tilde* = 27/16 = 1.6875".
Draw a horizontal dashed line at E_V* = -77.5 eV and annotate:
"Variational minimum: -77.5 eV".
Draw a horizontal dotted line at E_exp = -78.98 eV and annotate:
"Experimental: -78.98 eV".
Draw a horizontal dotted line at E_PT = -74.8 eV (first-order PT result)
and annotate: "First-order PT: -74.8 eV".

Info panel (right 400 wide): Display:
  - Current Z_tilde (from slider)
  - E_V at current Z_tilde (in eV)
  - Gap from experiment (in eV, colored red if > 1.5 eV, green if < 1.5)
  - Screening per electron: (Z - Z_tilde) = (2 - Z_tilde)
  - Brief text: "Each electron screens Z - Z_tilde = [X] proton charges
    from the other electron."

Slider for Z_tilde from 1.0 to 2.5, default 1.6875, live-updating all
displays.

H2+ BONDING MODE
Single SVG canvas 1000 x 500.
Main panel (left 600 wide): Plot E_+(R) and E_-(R) in eV vs. R (in
Angstrom) on the x-axis (range 0.3 to 6 Angstrom).
Natural units: a_0 = 0.529 Angstrom; energy in eV; 1 Hartree = 27.211 eV.

Define (with R in atomic units a_0):
  S(R) = exp(-R) * (1 + R + R^2/3)        [overlap integral]
  E_1 = -13.6 eV (hydrogen ground-state energy)

The matrix elements (in atomic units, then convert):
  j(R) = exp(-2R) * (1 + 1/R) (the Coulomb integral, in Hartree)
  k(R) = exp(-R) * (1/3 * R^2 + R + 1) * S(R) ... [see note below]

NOTE: use the standard results from the hydrogen molecule ion:
  H_AA = E_1 + e^2/(4 pi eps0 R) - e^2/(4 pi eps0) * <A|1/r_B|A>
where <A|1/r_B|A> = (e^{-2R/a0}/a0)(1 + a0/R).
In atomic units (a0 = 1, e^2/4pi eps0 = 1):
  H_AA(R) = -0.5 + 1/R - (1/R + 1)*exp(-2R)
  H_AB(R) = S(R) * (-0.5 + 1/R) - exp(-R)*(1 + R)

  E_+(R) = (H_AA + H_AB) / (1 + S)   [bonding, in Hartree; multiply by 27.211 for eV]
  E_-(R) = (H_AA - H_AB) / (1 - S)   [antibonding]

The TOTAL energy (including proton-proton repulsion e^2/R = 1/R Hartree):
  E_total_+(R) = E_+(R) + 1/R  [Hartree]
  E_total_-(R) = E_-(R) + 1/R

Convert to eV and plot vs. R (in Angstrom, so multiply R_au by 0.529).

Draw E_total_+(R) as a solid teal curve ("Bonding orbital").
Draw E_total_-(R) as a solid orange curve ("Antibonding orbital").
Draw a horizontal dashed line at E = -13.6 eV (separated H + H+ limit).

Annotate the minimum of E_total_+(R) with a vertical dashed line;
display the equilibrium bond length R_eq in Angstrom and the binding
energy (depth below -13.6 eV) in eV.

Info panel (right 400 wide): Display:
  - R at slider position (in Angstrom and in a_0)
  - S(R) — overlap integral (dimensionless)
  - E_bonding and E_antibonding at current R (eV)
  - Binding energy vs. separated atoms (eV) — positive means bound

Slider for R from 0.3 to 6 Angstrom, live-updating all displays.

GLOBAL
Runtime sanity checks to console:
  - Helium: at Z_tilde = 27/16, E_V should be -77.50 eV within 0.05 eV.
  - H2+: at R -> infinity (R_au = 20), E_total_+ should approach
    -13.6 eV within 0.05 eV.
  - H2+: S(R=0) should equal 1; S(R=20) should be < 1e-8.

Comments at every non-trivial physics step. Pure functions for all
energy computations. Verify formulas at console before relying on plots.
```

### Exploration tasks

1. Helium mode. Set the slider to $\tilde{Z} = 2$ (bare nuclear charge, no screening). What is the variational energy? This is what you would get from perturbation theory at zeroth order. Now set $\tilde{Z} = 27/16$. Note the improvement in the bound.

2. Helium mode. Move the slider below 1.5 and above 2.0. The curve $E_V(\tilde{Z})$ is a parabola. Does the minimum stay where the formula predicts? Read off the approximate location of the minimum from the plot and compare to $27/16 \approx 1.6875$.

3. H₂⁺ mode. Set $R = 1.06\,\text{Å}$ (the experimental equilibrium bond length). Is the LCAO minimum close to this? By how many Å is the LCAO variational answer off? Does the bonding curve go below the separated-atom limit?

4. H₂⁺ mode. Move the slider to large $R$ (4 Å and above). Both curves approach $-13.6\,\text{eV}$; do they approach from the same side? Explain in one sentence why the antibonding curve approaches from above and the bonding from below.

5. H₂⁺ mode. Set $R = 0.5\,\text{Å}$ (very close nuclei). What does the energy do? The proton-proton repulsion term $e^2/R$ should dominate at small $R$ — verify that the curves shoot up. Does the antibonding curve go up faster or slower than the bonding curve?

---

## References

- Griffiths, D. J. & Schroeter, D. F. *Introduction to Quantum Mechanics*, 3rd ed. Cambridge University Press (2018), Ch. 7 ("The Variational Principle"). [verify]
- Townsend, J. S. *A Modern Approach to Quantum Mechanics*, 2nd ed. University Science Books (2012), Ch. 6 ("The Variational Method"). [verify]
- Hylleraas, E. A. "Neue Berechnung der Energie des Heliums im Grundzustande, sowie des tiefsten Terms von Ortho-Helium." *Zeitschrift für Physik* 54, 347–366 (1929). [verify]
- Hartree, D. R. "The Wave Mechanics of an Atom with a Non-Coulomb Central Field." *Mathematical Proceedings of the Cambridge Philosophical Society* 24, 89–110 (1928). [verify]
- Fock, V. "Näherungsmethode zur Lösung des quantenmechanischen Mehrkörperproblems." *Zeitschrift für Physik* 61, 126–148 (1930). [verify]
- Shankar, R. *Principles of Quantum Mechanics*, 2nd ed. Springer (1994), Ch. 16 ("The Variational and WKB Methods"). [verify]
- Liboff, R. L. *Introductory Quantum Mechanics*, 4th ed. Addison-Wesley (2003), §13.4–13.5. [verify]
- Pople, J. A. *et al.* "Gaussian-type orbitals." Cited and explained in: Jensen, F. *Introduction to Computational Chemistry*, 3rd ed. Wiley (2017), Ch. 5. [verify]
