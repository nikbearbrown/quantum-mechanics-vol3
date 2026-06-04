# Chapter 2 — Degenerate Perturbation Theory and Fine Structure

## TL;DR

- When two or more unperturbed states share the same energy, the nondegenerate PT formula for the state correction blows up. The fix is to find the "good" zeroth-order states first by diagonalizing the perturbation matrix restricted to the degenerate subspace.
- Applied to hydrogen $n=2$ in an electric field: three distinct energies emerge from four states — the linear Stark effect, visible because two degenerate states polarize each other at first order.
- Hydrogen fine structure arises from three relativistic corrections — the relativistic kinetic term, spin–orbit coupling (with its crucial Thomas factor of $\tfrac{1}{2}$), and the Darwin term — whose combined effect depends only on $n$ and $j$, not on $\ell$ separately.
- The $n=2$ fine-structure splitting is approximately $4.5\times 10^{-5}\,\text{eV}$. The Lamb shift ($\approx 4\times 10^{-6}\,\text{eV}$), which splits the predicted-degenerate $2s_{1/2}$ and $2p_{1/2}$ levels, requires quantizing the electromagnetic field and lies outside this chapter's reach.

---

## Learning Objectives

By the end of this chapter you should be able to:

1. **Explain** why nondegenerate perturbation theory fails in a degenerate subspace and what the "good states" fix is. *(Bloom: Understand)*
2. **Apply** the degenerate PT procedure — build $W_{ij}$, diagonalize, read off corrections — to a given degenerate manifold. *(Bloom: Apply)*
3. **Apply** the procedure to the hydrogen $n=2$ Stark manifold and recover the three-line splitting. *(Bloom: Apply)*
4. **Identify** the three fine-structure perturbations and their physical origin, including the Thomas factor in spin–orbit coupling. *(Bloom: Analyze)*
5. **Compute** the $n=2$ fine-structure splitting numerically from the combined formula $E_n^\text{fs}$ and locate the Lamb shift as the explicit boundary where this framework ends. *(Bloom: Evaluate)*

---

## Stark's puzzle: three lines from four states

Johannes Stark, working in Aachen in the fall of 1913, put hydrogen in an electric field of about $10^5\,\text{V/cm}$ and watched the Balmer lines split. What he found was specific and strange: the $n=2$ level, which is fourfold degenerate in the unperturbed atom — states $2s$, $2p_0$, $2p_{+1}$, $2p_{-1}$, all at the same energy $-3.4\,\text{eV}$ — split into exactly three lines. Not four. Three. One shifted up, one shifted down by the same amount, and one that did not shift at all.

Why three lines from four states? Why is the splitting symmetric — exactly equal up and down — rather than some lopsided asymmetry? And why does the ground state barely move, while the $n=2$ level splits dramatically?

These are the questions degenerate perturbation theory answers. The machinery of Chapter 1 breaks down precisely when levels share an energy, which is where it is needed most. This chapter fixes that breakdown, uses the fix to crack the Stark effect, and then applies the same logic — diagonalizing a perturbation in a degenerate subspace — to hydrogen's fine structure.

---

## The breakdown and the fix

Recall the first-order state correction from Chapter 1:

$$|n^{(1)}\rangle = \sum_{m \neq n}\frac{\langle m^{(0)}|\hat{H}'|n^{(0)}\rangle}{E_n^{(0)} - E_m^{(0)}}\,|m^{(0)}\rangle$$

Now suppose two states share an energy: $E_a^{(0)} = E_b^{(0)}$. The term with $m = b$ in the sum for $|a^{(1)}\rangle$ has a zero denominator. The formula is undefined.

The failure is not that perturbation theory cannot handle degenerate levels. It is that the *basis within the degenerate subspace* is ambiguous. If $\hat{H}_0|a\rangle = E^{(0)}|a\rangle$ and $\hat{H}_0|b\rangle = E^{(0)}|b\rangle$, then any linear combination $\alpha|a\rangle + \beta|b\rangle$ is also an eigenstate of $\hat{H}_0$ at the same energy. The unperturbed Hamiltonian has no preference among these combinations — they all satisfy the eigenvalue equation.

The perturbation $\hat{H}'$ breaks this symmetry. As $\lambda$ is slowly turned up from zero, the eigenstates of the full $\hat{H}$ deform continuously from *specific* linear combinations of $|a\rangle$ and $|b\rangle$ into the true eigenstates. These preferred linear combinations — the ones that connect smoothly to the perturbed eigenstates — are the **good zeroth-order states**. The nondegenerate formula breaks because it was trying to expand around the *wrong* zeroth-order states.

**The fix is direct.** Restrict $\hat{H}'$ to the degenerate subspace and construct the matrix of its matrix elements:

$$W_{ij} = \langle i|\hat{H}'|j\rangle \quad \text{for } i,j \in \text{degenerate subspace}$$

Diagonalize $W$. The **eigenvalues** of $W$ are the first-order energy corrections $E_n^{(1)}$. The **eigenvectors** of $W$ are the good zeroth-order states — the correct starting basis from which nondegenerate PT can proceed without any zero denominators.

This procedure is not a special trick for degenerate systems. It is the general case: nondegenerate PT is simply what happens when the degenerate subspace is one-dimensional, so the "diagonalization" is trivial. Whenever you see a symmetry in the unperturbed Hamiltonian — and hydrogen has an unusually large one — the degenerate version is the right tool.

---

## Geometry: what the good states look like

Before computing anything for hydrogen, it helps to see the geometry. Think of the degenerate subspace as a plane in Hilbert space. Every vector in that plane is an equally valid zeroth-order state at energy $E^{(0)}$. The unperturbed Hamiltonian is isotropic in this plane — it cannot point a preferred direction.

The perturbation matrix $W$ can, and generically does, point a preferred direction. It picks out one axis in the plane (or two orthogonal axes for a two-dimensional subspace) along which the energy response to the perturbation is maximal and minimal. These are the eigenvectors — the good states. They are the combinations that decouple from each other under the perturbation at first order.

For the Stark effect, the preferred directions will turn out to be the combinations $(|2s\rangle \pm |2p_0\rangle)/\sqrt{2}$: electron probability clouds that are asymmetrically shifted up or down along the field axis. That asymmetry is what allows them to couple to the electric field at first order.

---

## The linear Stark effect: hydrogen $n=2$ in an electric field

Apply a uniform electric field along $\hat{z}$. The perturbation is $\hat{H}' = e\mathcal{E}\hat{z}$. The four degenerate $n=2$ states are $\{|2s\rangle, |2p_0\rangle, |2p_{+1}\rangle, |2p_{-1}\rangle\}$, where the subscript is $m_\ell$.

We need the $4\times 4$ matrix of $\hat{H}'$ in this subspace.

**Selection rules eliminate most entries before any calculation.**

First: $[\hat{H}', \hat{L}_z] = [e\mathcal{E}\hat{z}, \hat{L}_z] = 0$ because $\hat{z}$ is rotationally symmetric about $\hat{z}$. This means $\hat{H}'$ cannot change $m_\ell$. Any matrix element $\langle n', \ell', m_\ell'|\hat{H}'|n, \ell, m_\ell\rangle$ with $m_\ell' \neq m_\ell$ is exactly zero. This immediately zeroes out all entries involving $|2p_{+1}\rangle$ or $|2p_{-1}\rangle$ coupling to $|2s\rangle$ or $|2p_0\rangle$.

Second: parity. The operator $\hat{z}$ is parity-odd (changes sign under $\vec{r} \to -\vec{r}$). Diagonal matrix elements $\langle \psi|\hat{z}|\psi\rangle$ vanish whenever $|\psi\rangle$ has definite parity, because parity-even $\times$ parity-odd $\times$ parity-even integrates to zero over all space. All four states $|2s\rangle$, $|2p_0\rangle$, $|2p_{+1}\rangle$, $|2p_{-1}\rangle$ have definite parity (even for $\ell=0$, odd for $\ell=1$), so all diagonal entries vanish. Also, $\langle 2p_0|\hat{z}|2p_{+1}\rangle = 0$ by the $\Delta m_\ell = 0$ rule, and $\langle 2p_0|\hat{z}|2p_{-1}\rangle = 0$ similarly.

After selection rules, the only possibly surviving off-diagonal entry is $\langle 2s|\hat{z}|2p_0\rangle$ (and its conjugate). This mixes $\ell = 0$ and $\ell = 1$ at the same $m_\ell = 0$, and parity allows it (even times odd times odd = even, which can integrate to a nonzero value).

**Computing the surviving matrix element:**

$$\langle 2s|\hat{z}|2p_0\rangle = \int \psi_{2s}^*(\vec{r})\,r\cos\theta\,\psi_{2p_0}(\vec{r})\,d^3r$$

The hydrogenic wave functions are $\psi_{2s} = R_{20}(r)Y_0^0(\theta,\phi)$ and $\psi_{2p_0} = R_{21}(r)Y_1^0(\theta,\phi)$. The angular integral $\int Y_0^0 \cos\theta\, Y_1^0\,d\Omega$ evaluates to $1/\sqrt{3}$. The radial integral $\int_0^\infty R_{20}(r)\,r\,R_{21}(r)\,r^2\,dr$ evaluates to $-3\sqrt{6}a_0$. Combining:

$$\langle 2s|\hat{z}|2p_0\rangle = -3a_0$$

The full $4\times 4$ matrix $W = e\mathcal{E}\langle\cdot|\hat{z}|\cdot\rangle$, with rows and columns ordered $\{|2s\rangle, |2p_0\rangle, |2p_{+1}\rangle, |2p_{-1}\rangle\}$:

$$W = e\mathcal{E}\begin{pmatrix} 0 & -3a_0 & 0 & 0 \\ -3a_0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

This block-diagonalizes by inspection. The lower-right $2\times 2$ block is already zero — $|2p_{+1}\rangle$ and $|2p_{-1}\rangle$ are already good states with $E^{(1)} = 0$. The upper-left $2\times 2$ block:

$$\begin{pmatrix} 0 & -3a_0 e\mathcal{E} \\ -3a_0 e\mathcal{E} & 0 \end{pmatrix}$$

has eigenvalues $\pm 3a_0 e\mathcal{E}$ and eigenvectors $(|2s\rangle \mp |2p_0\rangle)/\sqrt{2}$.

**The result:** the $n=2$ level splits into three distinct energies:
- $E = E_2^{(0)} + 3a_0 e\mathcal{E}$: good state $(|2s\rangle - |2p_0\rangle)/\sqrt{2}$
- $E = E_2^{(0)} - 3a_0 e\mathcal{E}$: good state $(|2s\rangle + |2p_0\rangle)/\sqrt{2}$
- $E = E_2^{(0)}$: doubly degenerate, states $|2p_{+1}\rangle$ and $|2p_{-1}\rangle$

**Three lines from four states.** The spectral lines are symmetric (same shift up and down) because the $2\times 2$ matrix is traceless — its diagonal entries both vanish. The two shifted good states are probability clouds asymmetric along $\hat{z}$: one has more electron density above the nucleus, the other below. An asymmetric charge distribution couples to an electric field at first order. The $|2p_{\pm 1}\rangle$ states are azimuthally symmetric about $\hat{z}$ and cannot polarize along it at first order — they sit still.

Compare this to the ground state: $\langle 1s|e\mathcal{E}\hat{z}|1s\rangle = 0$ by parity. There is no partner at the same energy to mix with at first order. The ground state acquires a second-order (quadratic) shift — proportional to $\mathcal{E}^2$, tiny for ordinary laboratory fields. The $n=2$ linear Stark effect versus the $n=1$ quadratic Stark effect is a direct signature of degeneracy.

---

## Hydrogen fine structure: three perturbations

Hydrogen, solved with the bare Coulomb Hamiltonian $\hat{H}_0 = \hat{p}^2/2m - e^2/(4\pi\epsilon_0 r)$, gives energy levels $E_n^{(0)} = -13.6\,\text{eV}/n^2$ that depend only on $n$. Each $n$-level is $n^2$-fold degenerate (ignoring spin) or $2n^2$-fold degenerate (including spin). High-resolution spectroscopy reveals splittings at the level of $\alpha^2|E_n^{(0)}| \sim 10^{-4}\,\text{eV}$ for $n=2$, where $\alpha = e^2/(4\pi\epsilon_0\hbar c) \approx 1/137$ is the fine-structure constant. Three perturbations — all of order $\alpha^2$ relative to $\hat{H}_0$ — produce this fine structure.

### Perturbation 1: Relativistic kinetic energy

The non-relativistic kinetic energy $\hat{p}^2/2m$ is the leading term in the expansion of the relativistic kinetic energy $\sqrt{\hat{p}^2 c^2 + m^2c^4} - mc^2$ for $\hat{p} \ll mc$:

$$\sqrt{\hat{p}^2 c^2 + m^2c^4} - mc^2 = \frac{\hat{p}^2}{2m} - \frac{\hat{p}^4}{8m^3c^2} + \cdots$$

The **relativistic kinetic correction** is:

$$\hat{H}'_\text{rel} = -\frac{\hat{p}^4}{8m^3c^2}$$

This shifts every level, including $\ell = 0$ states. Its first-order correction requires $\langle\hat{p}^4\rangle_{n\ell}$, which can be evaluated using $\hat{p}^2 = 2m(\hat{H}_0 + e^2/4\pi\epsilon_0 r)$ and the known hydrogen expectation values $\langle 1/r\rangle_{n\ell} = 1/(n^2 a_0)$ and $\langle 1/r^2\rangle_{n\ell} = 1/(n^3 a_0^2(\ell + 1/2))$ [verify].

### Perturbation 2: Spin–orbit coupling

In the electron's rest frame, the orbiting nucleus creates a magnetic field. A naive frame-boost gives $\vec{B} = -\vec{v}\times\vec{E}/c^2$, and the coupling $\hat{H}_\text{SO} = -\vec{\mu}\cdot\vec{B}$ where $\vec{\mu} = -g_e\mu_B\vec{S}/\hbar$ is the electron's magnetic moment. But this naive argument gives the wrong answer by a factor of 2.

The correction is the **Thomas precession**: the electron's rest frame is non-inertial (it is accelerating in a circular orbit), and a non-inertial frame rotating in a magnetic field acquires an extra precession of its spin. The Thomas precession rate is exactly $-\tfrac{1}{2}$ of the naive precession, and subtracting it from the naive coupling gives a net factor of $\tfrac{1}{2}$. After including the Thomas factor:

$$\hat{H}'_\text{SO} = \frac{1}{2m^2c^2}\cdot\frac{1}{r}\frac{dV}{dr}\,\hat{\vec{L}}\cdot\hat{\vec{S}}$$

where $V(r) = -e^2/(4\pi\epsilon_0 r)$ is the Coulomb potential. For this potential, $dV/dr = e^2/(4\pi\epsilon_0 r^2)$, so:

$$\hat{H}'_\text{SO} = \frac{e^2}{8\pi\epsilon_0 m^2c^2}\cdot\frac{\hat{\vec{L}}\cdot\hat{\vec{S}}}{r^3}$$

**The Thomas factor $\tfrac{1}{2}$ is not optional.** Omitting it gives an answer off by a factor of 2 for the spin–orbit splitting. It arises from the Lorentz covariance of the electromagnetic field tensor — a purely kinematic, not dynamic, effect. Its cleanest derivation is from the Dirac equation, which gets the factor automatically [verify].

The spin–orbit term introduces a coupling between $\hat{\vec{L}}$ and $\hat{\vec{S}}$ that makes the individual projections $m_\ell$ and $m_s$ no longer good quantum numbers. The appropriate quantum number is $j = \ell + s$ where $s = \tfrac{1}{2}$ for the electron. Using the identity:

$$\hat{\vec{L}}\cdot\hat{\vec{S}} = \frac{1}{2}(\hat{J}^2 - \hat{L}^2 - \hat{S}^2)$$

in the $|n,\ell,j,m_j\rangle$ basis, $\hat{\vec{L}}\cdot\hat{\vec{S}}$ is diagonal with eigenvalue $\tfrac{\hbar^2}{2}[j(j+1) - \ell(\ell+1) - \tfrac{3}{4}]$.

The radial expectation value $\langle 1/r^3\rangle_{n\ell} = 1/(a_0^3 n^3 \ell(\ell+\tfrac{1}{2})(\ell+1))$ appears in the first-order energy correction. This expectation value diverges as $\ell \to 0$: an $s$-state electron spends significant time near the nucleus and the $1/r^3$ operator diverges there. Fortunately, the pre-factor $j(j+1) - \ell(\ell+1) - \tfrac{3}{4}$ also vanishes for $\ell = 0$ (since $j = s = \tfrac{1}{2}$, giving $\tfrac{3}{4} - 0 - \tfrac{3}{4} = 0$), so the spin–orbit energy correction vanishes for all $\ell = 0$ states — physically correct, since there is no orbital angular momentum to couple.

### Perturbation 3: The Darwin term

A third, purely relativistic correction arises from the Dirac equation and has no simple classical analogue. It can be motivated by "Zitterbewegung" — the rapid quantum jitter of a relativistic electron at the scale of the Compton wavelength $\hbar/mc$. This jitter smears the electron over a tiny volume, so it sees not the exact Coulomb potential at $\vec{r}$ but an average over a small sphere around $\vec{r}$. The leading correction to a potential $V(r)$ from this smearing is proportional to $\nabla^2 V$. For the Coulomb potential, $\nabla^2(-e^2/r) = (e^2/\epsilon_0)\delta^3(\vec{r})$ [verify], giving:

$$\hat{H}'_\text{Darwin} = \frac{\pi\hbar^2}{2m^2c^2}\cdot\frac{e^2}{4\pi\epsilon_0}\,\delta^3(\vec{r})$$

The delta function means the Darwin correction is nonzero **only for $\ell = 0$ states**, because only $s$-state wave functions have $|\psi(0)|^2 \neq 0$. For hydrogen, $|\psi_{n,\ell=0}(0)|^2 = 1/(\pi n^3 a_0^3)$.

Note the complementarity with the spin–orbit term: spin–orbit vanishes for $\ell = 0$; Darwin vanishes for $\ell \neq 0$. Their corrections combine cleanly.

---

## The combined fine-structure formula

All three perturbations are of order $\alpha^2 E_n^{(0)}$, so they must all be treated simultaneously. The unperturbed $n$-level is $2n^2$-fold degenerate (including spin). Within this degenerate subspace, we need to diagonalize the sum $\hat{H}'_\text{rel} + \hat{H}'_\text{SO} + \hat{H}'_\text{Darwin}$.

The key insight: all three terms commute with $\hat{J}^2$ and $\hat{J}_z$. So the good quantum numbers that diagonalize the perturbation are $(n, \ell, j, m_j)$ — the total angular momentum basis — rather than $(n, \ell, m_\ell, m_s)$. Within each $(n,\ell,j,m_j)$ subspace, the perturbation is already diagonal.

Computing each correction and summing, the combined first-order fine-structure energy correction is [verify]:

$$\boxed{E_n^\text{fs} = -\frac{(E_n^{(0)})^2}{2mc^2}\left(\frac{4n}{j+\tfrac{1}{2}} - 3\right)} \quad \text{[verify]}$$

where $E_n^{(0)} = -13.6\,\text{eV}/n^2$. The correction is negative for all physical levels.

**This result depends on $n$ and $j$ only — not on $\ell$ separately.** This is a remarkable cancellation: the relativistic correction and the spin–orbit correction individually depend on $\ell$, but their sum does not (for $\ell \neq 0$; the Darwin term handles $\ell = 0$ to yield the same $j$-only formula). The $\ell$-independence is a signature of the hidden SO(4) symmetry of the Coulomb problem [verify].

---

## Worked example: hydrogen $n=2$ fine structure

### Setup

For $n=2$, the allowed values of $j$ are:
- $j = \tfrac{1}{2}$: accessible from $\ell = 0$ (the $2s$ state, $j = \ell \pm s = s = \tfrac{1}{2}$) and from $\ell = 1$ (the $2p$ state with $j = \ell - s = \tfrac{1}{2}$), giving the $2s_{1/2}$ and $2p_{1/2}$ states.
- $j = \tfrac{3}{2}$: accessible from $\ell = 1$ only (the $2p$ state with $j = \ell + s = \tfrac{3}{2}$), giving the $2p_{3/2}$ state.

In spectroscopic notation: $2s_{1/2}$, $2p_{1/2}$, $2p_{3/2}$.

### Computing $E_2^\text{fs}$ for each $j$

The combined fine-structure correction, written with explicit sign [verify]:

$$E_n^\text{fs} = -\frac{(E_n^{(0)})^2}{2mc^2}\left(\frac{4n}{j+\tfrac{1}{2}} - 3\right)$$

This is negative for all physical states: for $n \geq 1$ the bracket is positive (you can check that $4n/(j+\tfrac{1}{2}) \geq 4 > 3$), and the overall sign is negative. Every level shifts down. The states with *smaller* $j$ shift down more (larger bracket, more negative correction), so lower-$j$ states sit below higher-$j$ states.

The prefactor: $(E_2^{(0)})^2/(2mc^2) = (3.4\,\text{eV})^2/(2\times 5.11\times 10^5\,\text{eV}) = 1.131\times 10^{-5}\,\text{eV}$.

**For $j = \tfrac{1}{2}$** (states $2s_{1/2}$ and $2p_{1/2}$):

$$E_2^\text{fs}\Big|_{j=1/2} = -1.131\times 10^{-5}\,\text{eV} \times \left(\frac{4\times 2}{1} - 3\right) = -1.131\times 10^{-5} \times 5\,\text{eV} = -5.66\times 10^{-5}\,\text{eV}$$

**For $j = \tfrac{3}{2}$** (state $2p_{3/2}$):

$$E_2^\text{fs}\Big|_{j=3/2} = -1.131\times 10^{-5}\,\text{eV} \times \left(\frac{4\times 2}{2} - 3\right) = -1.131\times 10^{-5} \times 1\,\text{eV} = -1.13\times 10^{-5}\,\text{eV}$$

### The splitting

Both corrections are negative; $2s_{1/2}$/$2p_{1/2}$ shift down by $5.66\times 10^{-5}\,\text{eV}$ while $2p_{3/2}$ shifts down by only $1.13\times 10^{-5}\,\text{eV}$. Therefore $2p_{3/2}$ sits *above* the $j=\tfrac{1}{2}$ pair:

$$\Delta E_\text{FS} = E_2^\text{fs}\Big|_{j=3/2} - E_2^\text{fs}\Big|_{j=1/2} = (-1.13 + 5.66)\times 10^{-5}\,\text{eV} = 4\times 1.131\times 10^{-5}\,\text{eV} \approx 4.5\times 10^{-5}\,\text{eV}$$

**The $j=1/2$ pair ($2s_{1/2}$ and $2p_{1/2}$) is pulled down further than $2p_{3/2}$, so $2p_{3/2}$ sits above them by about $4.5\times 10^{-5}\,\text{eV}$.**

In terms of the fine-structure constant: $\Delta E_\text{FS} = (4-1)\times(E_2^{(0)})^2/(2mc^2) \approx \alpha^2|E_2^{(0)}|/4 \approx 4.5\times 10^{-5}\,\text{eV}$, confirming the $\alpha^2$ scale.

### The limit: the Lamb shift

Fine structure predicts that $2s_{1/2}$ and $2p_{1/2}$ remain exactly degenerate — both have $j=\tfrac{1}{2}$, and the formula depends only on $n$ and $j$. This was experimentally tested by Willis Lamb and Robert Retherford in 1947, who found the two levels are *not* degenerate: $2s_{1/2}$ lies about $1057\,\text{MHz}$ ($\approx 4.4\times 10^{-6}\,\text{eV}$) above $2p_{1/2}$.

The Lamb shift has nothing to do with the three corrections above. It arises from quantum electrodynamics: the electron interacts not just with the classical Coulomb field but with the quantum fluctuations of the electromagnetic field itself. Vacuum fluctuations drive the electron's position slightly, shifting its energy. This shift is larger for the $2s_{1/2}$ state (which has finite probability at the nucleus and is therefore more sensitive to short-distance effects) than for $2p_{1/2}$.

The Lamb shift was the first precision test of renormalized QED. It requires quantizing the electromagnetic field — a technology this chapter does not have. The fine-structure formula is the boundary: inside it, semiclassical perturbation theory works; the Lamb shift is the first correction beyond that boundary.

The hierarchy for $n=2$ hydrogen:

$$\underbrace{E_2^{(0)} = -3.4\,\text{eV}}_\text{Bohr/Coulomb} \quad\to\quad \underbrace{\Delta E_\text{FS} \approx 4.5\times 10^{-5}\,\text{eV}}_\text{fine structure (this chapter)} \quad\to\quad \underbrace{\Delta E_\text{Lamb} \approx 4\times 10^{-6}\,\text{eV}}_\text{Lamb shift (QED)}$$

Each step is roughly an order of magnitude smaller.

---

## Common misconceptions

**1. "The good states are always symmetric/antisymmetric combinations."**
The good states are the eigenvectors of the perturbation matrix $W$ in the degenerate subspace. For the Stark effect they happen to be $(|2s\rangle \pm |2p_0\rangle)/\sqrt{2}$. For a different perturbation on the same degenerate manifold — say, a magnetic field instead of electric — the good states would be different. The good states depend on $\hat{H}'$, not only on $\hat{H}_0$.

**2. "Three eigenvalues means three levels, so four states become three."**
The degenerate zero eigenvalue accounts for *two* states: $|2p_{+1}\rangle$ and $|2p_{-1}\rangle$. There are still four states; two of them happen to be degenerate in the perturbed problem too. The experiment sees three spectral *lines*, not three *states*. This distinction matters when higher-resolution measurements probe the middle pair.

**3. "The Thomas factor is just a correction that barely matters."**
The Thomas factor $\tfrac{1}{2}$ halves the spin–orbit coupling. For hydrogen, omitting it gives a spin–orbit splitting twice as large, and the combined fine-structure formula does not work out correctly. The Thomas factor is not small; it is a factor of 2 correction to a leading-order result.

**4. "The Darwin term and the Lamb shift are the same thing."**
They are not. The Darwin term comes from the Dirac equation — relativistic single-particle quantum mechanics — and is part of the fine-structure formula this chapter derives. The Lamb shift comes from quantum field theory: the electron interacting with vacuum fluctuations of the quantized electromagnetic field. Both are non-zero for $s$-states and both shift the energy of $2s$ relative to $2p$, but they arise from completely different physics and differ in magnitude.

**5. "After fine structure, the $n=2$ level splits into four distinct energies."**
It splits into two: $j=\tfrac{1}{2}$ (containing both $2s_{1/2}$ and $2p_{1/2}$, degenerate in fine structure) and $j=\tfrac{3}{2}$ (containing the four $m_j$ substates of $2p_{3/2}$). The four $m_j = \pm\tfrac{1}{2}, \pm\tfrac{3}{2}$ substates of the $j=\tfrac{3}{2}$ level are degenerate in the absence of a magnetic field. Fine structure gives two levels, not four.

---

## Exercises

### Warm-up

**2.1** Explain in your own words why the formula $|n^{(1)}\rangle = \sum_{m\neq n}\langle m|\hat{H}'|n\rangle/(E_n^{(0)}-E_m^{(0)})|m\rangle$ breaks down when two unperturbed states share the same energy. Your explanation should identify (a) which term in the sum causes the problem and (b) why the problem is a *basis* ambiguity rather than a failure of perturbation theory itself.

*(Tests: conceptual understanding of the degenerate PT breakdown; identifying the basis issue.)*

---

**2.2** State the two selection rules that eliminate most entries of the $4\times 4$ Stark matrix for the hydrogen $n=2$ manifold, *before* computing any integral. For each of the six distinct pairs $\{|2s\rangle,|2p_0\rangle\}$, $\{|2s\rangle,|2p_{+1}\rangle\}$, $\{|2s\rangle,|2p_{-1}\rangle\}$, $\{|2p_0\rangle,|2p_{+1}\rangle\}$, $\{|2p_0\rangle,|2p_{-1}\rangle\}$, $\{|2p_{+1}\rangle,|2p_{-1}\rangle\}$: state which rule kills the matrix element, or confirm it survives. How many distinct matrix elements must actually be computed?

*(Tests: applying selection rules before calculation; understanding which symmetry kills which entry.)*

---

**2.3** The two-dimensional harmonic oscillator with $\hat{H}' = \alpha m\omega^2 \hat{x}\hat{y}$. The two unperturbed states $|1,0\rangle$ (one quantum in $x$, zero in $y$) and $|0,1\rangle$ (zero in $x$, one in $y$) share energy $2\hbar\omega$.

(a) Compute the $2\times 2$ perturbation matrix $W_{ij} = \langle i|\hat{H}'|j\rangle$ for $i,j \in \{|1,0\rangle, |0,1\rangle\}$.

(b) Find the eigenvalues and eigenvectors of $W$.

(c) The exact energies are $\hbar\omega\sqrt{(1\pm\alpha)+1}$ for the good states. Show that your first-order PT eigenvalues match the exact result to leading order in $\alpha$.

*(Tests: explicit 2×2 degenerate PT calculation; comparison to exact answer.)*

---

### Apply

**2.4** Hydrogen fine structure numerical check.

(a) Using the formula $E_n^\text{fs} = -(E_n^{(0)})^2/(2mc^2)\times(4n/(j+\tfrac{1}{2})-3)$ with $E_2^{(0)} = -3.4\,\text{eV}$ and $mc^2 = 0.511\,\text{MeV}$, compute the fine-structure correction $E_2^\text{fs}$ for the $j=\tfrac{1}{2}$ and $j=\tfrac{3}{2}$ states numerically in eV. Which state has the more negative correction, and therefore lies lower?

(b) The splitting $\Delta E_\text{FS}$ between $2p_{3/2}$ and the $j=\tfrac{1}{2}$ pair. Express it as a multiple of $\alpha^2|E_2^{(0)}|$ and verify it is approximately $4.5\times 10^{-5}\,\text{eV}$. (Use $\alpha \approx 1/137$.)

(c) How does the Lamb shift ($\approx 4\times 10^{-6}\,\text{eV}$) compare in magnitude to $\Delta E_\text{FS}$? What is their ratio?

*(Tests: numerical evaluation of the fine-structure formula; confirming the $\alpha^2$ scale; locating QED effects in the hierarchy.)*

---

**2.5** Spin–orbit sign analysis. For the hydrogen $n=2$ states, the spin–orbit correction is proportional to $\langle\hat{\vec{L}}\cdot\hat{\vec{S}}\rangle = \tfrac{\hbar^2}{2}[j(j+1) - \ell(\ell+1) - \tfrac{3}{4}]$.

(a) Evaluate this for the $2p_{1/2}$ state ($\ell=1, j=\tfrac{1}{2}$) and the $2p_{3/2}$ state ($\ell=1, j=\tfrac{3}{2}$). What are the signs?

(b) The $2p_{1/2}$ spin–orbit correction is negative (spin antiparallel to orbit), and the $2p_{3/2}$ correction is positive (spin parallel to orbit). Explain physically why parallel spin–orbit alignment costs more energy.

(c) Why is the spin–orbit correction exactly zero for the $2s_{1/2}$ state? Your answer should be in terms of both the formula and the physics.

*(Tests: evaluating the L·S eigenvalue; connecting sign to physical alignment; identifying the ℓ=0 special case.)*

---

**2.6** Good states and field direction. In the Stark effect, the good states $(|2s\rangle \pm |2p_0\rangle)/\sqrt{2}$ are tailored to a field along $\hat{z}$. Now suppose the electric field is applied along $\hat{x}$ instead.

(a) Write down the perturbation $\hat{H}' = e\mathcal{E}\hat{x}$ and identify which angular-momentum selection rule changes (the field breaks $\hat{z}$-rotational symmetry differently).

(b) Which states from $\{|2s\rangle, |2p_{-1}\rangle, |2p_0\rangle, |2p_{+1}\rangle\}$ mix under $\hat{x}$? (Hint: $\hat{x} = -(r/\sqrt{2})(Y_1^{+1} - Y_1^{-1})$ in spherical harmonics.)

(c) Set up the perturbation matrix for the $\hat{x}$-field and find the eigenvalues. Compare to the $\hat{z}$-field case. Are the physical splittings different?

*(Tests: understanding that good states depend on the perturbation direction; applying selection rules for a different field orientation; recognizing that the eigenvalues — the physical splittings — are the same by symmetry.)*

---

### Produce

**2.7** Two degenerate levels with an off-diagonal perturbation. Consider two states $|a\rangle$ and $|b\rangle$ sharing energy $E^{(0)}$. The perturbation matrix is:

$$W = \begin{pmatrix} \alpha & \beta \\ \beta^* & \alpha \end{pmatrix}$$

where $\alpha$ is real and $\beta$ may be complex.

(a) Find the two eigenvalues of $W$.

(b) Find the eigenvectors (the good states).

(c) If $\alpha = 0$ and $\beta$ is real: eigenvalues are $\pm\beta$, good states are $(|a\rangle \pm |b\rangle)/\sqrt{2}$. Identify which case in the Stark matrix this is.

(d) Now let $|\beta| \ll |\alpha|$. What are the eigenvalues to leading order in $\beta/\alpha$? When does off-diagonal mixing become negligible?

*(Tests: diagonalizing the general 2×2 degenerate PT matrix; recognizing the Stark effect as a special case; understanding when mixing is suppressed.)*

---

**2.8** Design your own fine-structure level diagram. Hydrogen $n=3$ has $j$-values $\tfrac{1}{2}$ (from $3s_{1/2}$ and $3p_{1/2}$), $\tfrac{3}{2}$ (from $3p_{3/2}$ and $3d_{3/2}$), and $\tfrac{5}{2}$ (from $3d_{5/2}$).

(a) Compute $E_3^\text{fs}$ for each value of $j$ from the formula.

(b) Draw a labeled energy-level diagram showing the $n=3$ manifold split by fine structure. Mark each level with its $j$-value and spectroscopic designation.

(c) Which levels are degenerate in the fine-structure formula? What would the Lamb shift do to these degenerate pairs?

(d) How many distinct spectral lines would you observe in a transition from $n=3$ to $n=2$ considering fine structure, ignoring the Lamb shift?

*(Tests: applying the combined fine-structure formula to $n=3$; drawing a level diagram; counting lines; understanding degeneracy patterns.)*

---

## Still puzzling

The $\ell$-independence of the fine-structure formula is a non-trivial cancellation: the relativistic correction $E_n^\text{rel}$ depends on $n$ and $\ell$, the spin–orbit correction $E_n^\text{SO}$ depends on $n$, $\ell$, and $j$, and the Darwin term on $n$ only (for $\ell=0$). Their sum depends only on $n$ and $j$. This cancellation is ultimately a consequence of the hidden SO(4) symmetry of the Coulomb problem — the same symmetry that makes the unperturbed levels depend only on $n$ in the first place. The relativistic corrections partially break this symmetry, but only down to SO(3) (rotational symmetry), which accounts for the $j$-dependence remaining. A clean derivation of the combined formula from the Dirac equation makes this explicit, but requires going beyond what Rayleigh–Schrödinger perturbation theory can see. Understanding why the accidental degeneracy survives through fine structure — until the Lamb shift breaks it via QED — is one of the genuinely beautiful results of twentieth-century physics.

---

## The +1 — Simulation Exercise

You are going to build a D3 simulation that shows the hydrogen $n=2$ fine-structure level diagram, with sliders to turn on fine structure and a separate display of the Stark effect. The deliverable is `03-fine-structure-stark.html` in your working directory.

### Step 1 — Describe the simulation to Claude Code

Copy the following prompt into a Claude Code session in your working directory.

```
Build 03-fine-structure-stark.html: a single self-contained HTML file using
D3 v7 from a CDN and d3-simple-slider. No other dependencies.

The simulation has two tabs: "Fine Structure n=2" and "Linear Stark n=2".

FINE STRUCTURE TAB
SVG canvas 900 x 600. Show the n=2 hydrogen level diagram.

Left column (x = 100): single horizontal line at E = 0 (the unperturbed
n=2 energy, -3.4 eV; show the energy axis in units of 10^{-5} eV relative
to E_2^0). Label it "unperturbed 2s, 2p (8 states)".

Right column (x = 700): two horizontal lines at the fine-structure corrected
energies. Top line at ΔE_{FS} for j=1/2 relative to j=3/2, labeled
"2p_{3/2} (j=3/2, 4 states)". Bottom line at 0, labeled
"2s_{1/2}, 2p_{1/2} (j=1/2, 4 states)". Draw dashed vertical arrow
connecting them with the label "ΔE_FS ≈ 4.5 × 10^{-5} eV".

Below the j=1/2 line, draw a second, smaller dashed arrow showing the Lamb
shift splitting (~4 × 10^{-6} eV) between 2s_{1/2} and 2p_{1/2}, labeled
"Lamb shift (QED, beyond this chapter)".

Slider: "Fine structure coupling α²" from 0 to 1 (dimensionless scale factor
for ΔE_FS). When the slider is at 0, the right column collapses to a single
line. When it is at 1, it shows the full ΔE_FS = 4.5 × 10^{-5} eV splitting.
Animate the transition smoothly.

STARK EFFECT TAB
SVG canvas 1100 x 600. Left half (700 wide): four horizontal energy lines,
all starting at E = 0 (relative to unperturbed n=2 energy) at field E = 0.
Slider for electric field strength E_field in atomic units, 0 to 0.05.
As E_field increases:
  - Upper line (eigenvalue +3 a_0 e E_field): labeled "(|2s⟩ − |2p_0⟩)/√2"
  - Lower line (eigenvalue −3 a_0 e E_field): labeled "(|2s⟩ + |2p_0⟩)/√2"
  - Two middle lines (eigenvalue 0): labeled "|2p_{+1}⟩, |2p_{−1}⟩"
In atomic units: a_0 = 1, e = 1, so the upper eigenvalue = +3 E_field,
lower = −3 E_field. Convert to display units (eV): multiply by 27.2 eV
(one Hartree = 27.2 eV).

Right half (400 wide): display the live 4×4 W matrix:
  - Row/col labels: 2s, 2p_0, 2p_{+1}, 2p_{-1}
  - Values in atomic units: off-diagonal {2s,2p_0} entries = -3*E_field
  - All other entries: 0
  Highlight the two nonzero entries in orange.

PHYSICS
Fine-structure formula: E_n^fs = -(E_n^0)^2/(2*mc^2) * (4n/(j+0.5) - 3)
  E_2^0 = -3.4 eV, mc^2 = 511000 eV, n = 2
  Prefactor = (3.4)^2 / (2 * 511000) = 1.131e-5 eV
  j = 1/2: bracket = 8/1 - 3 = 5; correction = -5.655e-5 eV
  j = 3/2: bracket = 8/2 - 3 = 1; correction = -1.131e-5 eV
  j=3/2 is less negative (sits higher); splitting = 4*(3.4)^2/(1022000) ≈ 4.52e-5 eV
  Use this value directly. Show both corrections as negative; display the gap.

Stark eigenvalues in eV: ±3 * E_field * 27.2 (atomic units to eV).
Lamb shift: 4.4 × 10^{-6} eV (hardcoded, not adjustable — it's a QED input).

Sanity check to console:
  - At E_field = 0, all four Stark eigenvalues = 0.
  - Trace of W matrix = 0 always.
  - At E_field = 0.01 a.u., upper eigenvalue = 3*0.01*27.2 = 0.816 eV.
    (This seems large — note that 0.01 a.u. field is very strong by lab
    standards, but it is within the Stark regime before ionization.)
```

### Exploration tasks

After the simulation runs, answer the following:

1. **Fine structure slider.** Move the fine-structure slider from 0 to 1. How many distinct lines appear at full coupling? Label each line with its spectroscopic designation ($2s_{1/2}$, $2p_{1/2}$, $2p_{3/2}$). Why do $2s_{1/2}$ and $2p_{1/2}$ remain degenerate at full coupling?

2. **Lamb shift.** The Lamb shift dashed arrow is drawn at a fixed height. How large is it compared to the fine-structure splitting? Can you resolve it on the scale of the diagram? What does this tell you about the difficulty of measuring the Lamb shift experimentally?

3. **Stark matrix.** In the Stark tab, set the field to $\mathcal{E} = 0.005\,\text{a.u.}$. Read the two nonzero matrix entries from the displayed $W$ matrix. Verify by hand: $W_{2s,2p_0} = -3\times 0.005 = -0.015$ Hartree. Now check the upper eigenvalue: should be $+3\times 0.005\times 27.2 = 0.408\,\text{eV}$.

4. **Field strength context.** The slider runs to $\mathcal{E} = 0.05\,\text{a.u.}$ At this value, the splitting is $3\times 0.05\times 27.2 = 4.08\,\text{eV}$. But $|E_2^{(0)}| = 3.4\,\text{eV}$. Why does this make you suspicious? (Real hydrogen atoms ionize via the tilted-Coulomb mechanism — the Stark ionization threshold — well below this field strength. The simulation does not capture ionization.) At what field strength does the Stark splitting become comparable to $|E_2^{(0)}|$?

---

## References

Griffiths, D. J., & Schroeter, D. F. (2018). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press. §7.3 (relativistic correction, spin–orbit, Darwin term, fine-structure formula). [verify]

Townsend, J. S. (2012). *A Modern Approach to Quantum Mechanics* (2nd ed.). University Science Books. §3.3 (degenerate PT procedure), §3.4 (linear Stark effect). [verify]

Lamb, W. E., & Retherford, R. C. (1947). Fine structure of the hydrogen atom by a microwave method. *Physical Review*, *72*(3), 241–243. https://doi.org/10.1103/PhysRev.72.241 [verify]

Stark, J. (1914). Beobachtungen über den Effekt des elektrischen Feldes auf Spektrallinien. *Annalen der Physik*, *348*(7), 965–982. https://doi.org/10.1002/andp.19143480702 [verify]

Zwiebach, B. (2018). *Quantum Physics III* (MIT OpenCourseWare 8.06), Chapter 2: Fine Structure. Massachusetts Institute of Technology. https://ocw.mit.edu/courses/8-06-quantum-physics-iii-spring-2018/ [verify]
