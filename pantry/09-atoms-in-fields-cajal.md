# CAJAL Figure Report — Chapter 9 — Atoms in Fields: Zeeman, Stark, and Magnetic Resonance

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Weak-Field Zeeman: Energy-Level Splitting of the Hydrogen 2p Manifold

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw an energy-level diagram showing the splitting of the hydrogen $2p$ manifold in a weak external magnetic field. On the left at $B = 0$, show two horizontal lines representing the fine-structure split levels: $2p_{3/2}$ (upper, four-fold degenerate) and $2p_{1/2}$ (lower, two-fold degenerate), separated by a gap representing $\Delta E_{FS} \approx 4.5 \times 10^{-5}$ eV. On the right at a nonzero $B$, show each level split into its $2j+1$ sublevels: $2p_{3/2}$ splits into four equally spaced lines (spacing $g_J \mu_B B$ with $g_J = 4/3$), and $2p_{1/2}$ splits into two lines (spacing $g_J \mu_B B$ with $g_J = 2/3$). Connect each degenerate level at $B = 0$ to its respective sublevel fan at $B > 0$ with light fan-lines. Mark the $m_j$ values for each sublevel as tick positions along the right edge. Use the same vertical energy scale throughout; the $y$-axis represents energy with tick marks at the sublevel positions.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two fine-structure levels at $B = 0$ ($2p_{3/2}$ upper, $2p_{1/2}$ lower); gap representing $\Delta E_{FS}$; four sublevels of $2p_{3/2}$ at $B > 0$ with spacing $\frac{4}{3}\mu_B B \cdot m_j$ for $m_j = +3/2, +1/2, -1/2, -3/2$; two sublevels of $2p_{1/2}$ with spacing $\frac{2}{3}\mu_B B \cdot m_j$ for $m_j = +1/2, -1/2$; fan-connecting lines from degenerate to split levels; $m_j$ tick marks at right edge. Six total split sublevels from six states (four + two).
- `[O — ORGANIZATION]` Horizontal progression: left side = $B = 0$ (two degenerate groups); right side = $B > 0$ (six sublevels). Vertical axis = energy, increasing upward. $2p_{3/2}$ group above $2p_{1/2}$ group throughout. Fan lines converge from right side back to left. The four $2p_{3/2}$ sublevels have unequal spacing relative to the two $2p_{1/2}$ sublevels, illustrating the different $g_J$ values.
- `[P — PRESENTATION]` $2p_{3/2}$ level and sublevels: Blue `#0072B2`, 2 pt. $2p_{1/2}$ level and sublevels: Orange `#E69F00`, 2 pt. Fan lines: light gray, 0.5 pt. $\Delta E_{FS}$ bracket: Sky Blue `#56B4E9`, 1 pt. $m_j$ marker ticks at right: same color as their parent level. No text baked in.
- `[E — EXCLUSIONS]` Omit: strong-field (Paschen-Back) sublevels, $n=2$ $s$-state, Stark splitting, intermediate-field avoided crossings, optical transitions between levels, hyperfine structure, $1s$ ground state.

**BLOCK 3 — NEGATIVE PROMPT:**
Paschen-Back strong-field levels in same panel, optical transition arrows, hyperfine sublevels, intermediate-field numerical diagonalization curves, Stark electric-field splitting, 3D energy surface, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Zeeman Crossover: Energy vs. Field Strength ($B$) for the 2p Manifold

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a family of energy-vs.-field curves for the hydrogen $2p$ manifold ($j = 3/2$ and $j = 1/2$ sublevels) as a function of magnetic field $B$ on the horizontal axis from 0 to 10 T. The vertical axis represents energy relative to the unperturbed $2p$ energy in units of $\mu_B B$. At $B = 0$, the six lines start at the two fine-structure energies ($\pm \Delta E_{FS}/2$). In the weak-field limit (left region), each line rises or falls linearly with slope $g_J m_j$ according to the anomalous Zeeman formula. In the strong-field limit (right region), the lines regroup according to the Paschen-Back formula $m_\ell + 2m_s$. Show the weak-field linear curves as solid lines and the strong-field linear asymptotes as dashed lines; the intermediate region is where these diverge. Mark the crossover field $B_c$ (where $\mu_B B_c \sim \Delta E_{FS}$) with a vertical dashed line. The six curves should all be distinguishable by color or line style.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Panel approximately 89 mm wide × 75 mm tall.
- `[C — CONTENT]` Six energy curves for $2p$ manifold vs. $B$ from 0 to 10 T; fine-structure split baseline at $B = 0$; weak-field linear slopes (anomalous Zeeman, $g_J m_j \mu_B B$) as solid segments; strong-field linear asymptotes (Paschen-Back, $(m_\ell + 2m_s)\mu_B B$) as dashed segments; crossover field $B_c$ vertical dashed line; $y$-axis: energy in eV or $\mu_B$ units. The crossover is at $\mu_B B_c \approx \Delta E_{FS} \approx 4.5 \times 10^{-5}$ eV, around $B_c \approx 0.78$ T.
- `[O — ORGANIZATION]` Horizontal $x$-axis: $B$ from 0 to 10 T. Vertical $y$-axis: symmetric about zero (the unperturbed 2p energy), range approximately $\pm 6 \times 10^{-4}$ eV. Curves fan upward and downward from two starting clusters at $B = 0$. Crossover dashed vertical at $B_c$.
- `[P — PRESENTATION]` $j = 3/2$ curves (four lines): Blue `#0072B2` shades — use solid, long-dash, short-dash, and dash-dot variants, all Blue. $j = 1/2$ curves (two lines): Orange `#E69F00` solid and dashed. Paschen-Back asymptotes: Reddish Purple `#CC79A7`, thin dashed. Crossover vertical: Sky Blue `#56B4E9`, 1 pt dashed. All strokes 1–1.5 pt. No text baked in.
- `[E — EXCLUSIONS]` Omit: $n = 2$ $s$-state curves, Stark splitting, optical transition arrows, hyperfine structure, numerical exact diagonalization curves (only limiting-formula curves), quantum defect corrections from multi-electron atoms.

**BLOCK 3 — NEGATIVE PROMPT:**
n=2 s-state curves, Stark effect lines, optical transition arrow overlays, hyperfine splittings, exact numerical diagonalization curves, multi-electron atom quantum-defect curves, 3D perspective energy surface, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Linear Stark Effect: $n=2$ Hydrogen Splitting vs. Electric Field

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw an energy-level fan diagram showing the four $n=2$ hydrogen states splitting as an electric field $\mathcal{E}$ increases. The horizontal axis is the electric field $\mathcal{E}$ in atomic units from 0 to 0.05. At $\mathcal{E} = 0$, all four states are degenerate at $E = 0$ (relative to the unperturbed $n=2$ energy), shown as four overlapping horizontal lines. As $\mathcal{E}$ increases rightward, two of the lines diverge linearly: one rises to $+3a_0 e\mathcal{E}$ and one drops to $-3a_0 e\mathcal{E}$, forming a scissors-like opening pattern. Two lines remain flat at zero energy throughout (doubly degenerate). At the right edge of the panel, show the eigenstate character: the rising line corresponds to the $(|2s\rangle - |2p_0\rangle)/\sqrt{2}$ superposition; the falling line to $(|2s\rangle + |2p_0\rangle)/\sqrt{2}$; the flat lines to $|2p_{+1}\rangle$ and $|2p_{-1}\rangle$.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Four lines starting at $E = 0$ when $\mathcal{E} = 0$; rising line: $+3a_0 e\mathcal{E}$ (linear slope up); falling line: $-3a_0 e\mathcal{E}$ (linear slope down); two flat lines at $E = 0$ (doubly degenerate, $|2p_{\pm 1}\rangle$); $x$-axis: $\mathcal{E}$ from 0 to 0.05 a.u.; $y$-axis: energy from $-0.15$ to $+0.15$ a.u. The scissors opening is the visual signature of the linear Stark effect. The eigenstate character at right edge is inferred from the diagonalization.
- `[O — ORGANIZATION]` Left-to-right from $\mathcal{E} = 0$ to $0.05$ a.u. All four lines emerge from the same point at origin. Rising and falling lines are symmetric about $E = 0$. The two flat lines coincide exactly on the $x$-axis. Right-edge tick marks for the four asymptotic values.
- `[P — PRESENTATION]` Rising line: Bluish Green `#009E73`, 2 pt solid. Falling line: Vermillion `#D55E00`, 2 pt solid. Two flat lines: Blue `#0072B2`, 1.5 pt solid (rendered as one line since they coincide, or offset by 0.5 pt for visibility). $E = 0$ reference: light gray, 0.5 pt. Axes: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: $n = 1$ ground state, Zeeman magnetic splitting, quadratic Stark effect for other levels, ionization continuum, intermediate perturbation mixing with $n = 3$, Rydberg-state Stark structure.

**BLOCK 3 — NEGATIVE PROMPT:**
ground-state quadratic Stark curve, ionization threshold curves, Rydberg manifold structure, Zeeman lines in same panel, 3D energy surface, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Rotating-Frame Transformation: Lab Frame vs. Rotating Frame

**Heuristic:** MC | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side panels showing the magnetic resonance field configuration in the lab frame (left) and the rotating frame (right). In the lab-frame panel, show a large vertical arrow for the static field $B_0\hat{z}$, and a small horizontal double-arrow rotating in the $xy$-plane representing the oscillating transverse field $B_1$. Draw a spin vector precessing around $\hat{z}$ in a cone shape. In the rotating-frame panel, show the same static field now reduced to an effective field $(B_0 - \omega/\gamma)\hat{z}$ (shorter arrow), and the transverse field $B_1$ now appearing as a stationary horizontal arrow along $\hat{x}'$ (no rotation). At the resonance condition $\omega = \omega_0$, the effective $z$-component vanishes — show this as the static arrow shrinking to zero, leaving only the horizontal $B_1$ arrow. The spin now precesses around the horizontal $B_1$ axis (Rabi oscillation). The two panels are connected by a horizontal arrow labeled "rotating frame transform."

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Two-panel layout, total width 89 mm, each sub-panel approximately 40 mm wide, height 60 mm. 300 DPI, vector, white background.
- `[C — CONTENT]` Lab frame (left panel): $B_0\hat{z}$ (tall vertical arrow); rotating $B_1$ field (curved circular arrow in $xy$-plane); spin precession cone around $\hat{z}$. Rotating frame (right panel): reduced effective $z$-field $(B_0 - \omega/\gamma)\hat{z}$ (shorter vertical arrow, possibly zero at resonance); stationary $B_1$ (horizontal arrow, $\hat{x}'$); spin now precessing around $\hat{x}'$. Transform arrow between panels. At resonance, the $z$-arrow in right panel is absent.
- `[O — ORGANIZATION]` Left-to-right: lab → rotating frame. Coordinate axes drawn in both panels ($\hat{x}, \hat{y}, \hat{z}$ in lab; $\hat{x}', \hat{y}', \hat{z}$ in rotating). The transform arrow is centered between the two panels. The resonance condition is shown specifically in the right-panel sub-diagram.
- `[P — PRESENTATION]` $B_0$ arrows: Blue `#0072B2`, 2 pt, single-headed. Rotating $B_1$ (lab): Orange `#E69F00`, 1.5 pt, curved arc with arrowhead. Stationary $B_1$ (rotating frame): Orange `#E69F00`, 2 pt, straight arrow. Effective $z$-field (reduced): Sky Blue `#56B4E9`, 1.5 pt. Spin vector: Bluish Green `#009E73`, 2 pt. Precession cone outline: light gray, dashed. Transform arrow: neutral gray, 1.5 pt. No text baked in.
- `[E — EXCLUSIONS]` Omit: Bloch-equation relaxation terms ($T_1$, $T_2$), FID or spin-echo pulse sequences, NMR spectrometer hardware diagram, off-resonance vector tilting (this panel shows the on-resonance case only), Rabi probability curve (separate figure).

**BLOCK 3 — NEGATIVE PROMPT:**
NMR spectrometer coil hardware, FID waveform signal, Bloch vector relaxation decay, off-resonance tilted effective field, spin-echo pulse sequence diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Rabi Oscillations: On-Resonance vs. Off-Resonance $P_\downarrow(t)$

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line plot of the spin-flip probability $P_\downarrow(t)$ on the vertical axis (range 0 to 1, starting at zero) against time $t$ on the horizontal axis (range 0 to several Rabi periods). Show three curves: (1) on-resonance ($\delta = 0$): $P_\downarrow = \sin^2(\omega_1 t/2)$, a full oscillation between 0 and 1; (2) slightly off-resonance ($\delta = \omega_1$): $P_\downarrow = (\omega_1^2/\Omega^2)\sin^2(\Omega t/2)$ with $\Omega = \sqrt{2}\omega_1$, oscillating with a peak of $1/2$ and faster frequency; (3) far off-resonance ($\delta = 3\omega_1$): rapid small-amplitude oscillation peaking at $1/10$. Mark the $\pi$-pulse time ($t = \pi/\omega_1$) for the on-resonance case with a vertical dashed line at the first maximum of curve 1. The $y$-axis must start at zero.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three Rabi oscillation curves: on-resonance (solid, full swing 0–1); off-resonance $\delta = \omega_1$ (dashed, max amplitude $= 1/2$, faster oscillation); far off-resonance $\delta = 3\omega_1$ (dotted, max amplitude $= 1/10$, fastest oscillation). Vertical dashed line at $t = \pi/\omega_1$ ($\pi$-pulse condition). $y$-axis from 0 to 1. $x$-axis in units of $\omega_1 t / \pi$.
- `[O — ORGANIZATION]` Single panel. $x$-axis: dimensionless time $\omega_1 t / \pi$ from 0 to 4 (two full on-resonance periods). $y$-axis: probability 0 to 1. The three curves start at 0 and oscillate at different rates and amplitudes. $\pi$-pulse dashed line at $x = 1$.
- `[P — PRESENTATION]` On-resonance: Blue `#0072B2`, 2 pt solid. $\delta = \omega_1$ off-resonance: Orange `#E69F00`, 1.5 pt dashed. Far off-resonance $\delta = 3\omega_1$: Reddish Purple `#CC79A7`, 1.5 pt dotted. $\pi$-pulse vertical: Sky Blue `#56B4E9`, 1 pt dashed. $y$-axis starts at 0 (hard rule). Axes: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: Bloch-equation relaxation envelope ($T_1$, $T_2$ decay), Fourier spectrum of the oscillations, NMR pulse sequence diagram, spin-echo, multi-pulse sequences, inversion recovery curves.

**BLOCK 3 — NEGATIVE PROMPT:**
T1 or T2 exponential decay envelope, spin-echo pulse sequence, FID signal, multi-pulse NMR sequence, Fourier transform NMR spectrum, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Stark Perturbation Matrix: $4\times 4$ Block Structure

**Heuristic:** VG | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a $4 \times 4$ grid representing the perturbation matrix $W = \langle n\ell m | e\mathcal{E}\hat{z} | n'\ell' m' \rangle$ for the hydrogen $n=2$ manifold. The rows and columns are ordered as $|2s\rangle$, $|2p_0\rangle$, $|2p_{+1}\rangle$, $|2p_{-1}\rangle$. Most cells are zero — show them as empty or lightly shaded squares. Two cells are nonzero: the $(1,2)$ and $(2,1)$ off-diagonal entries, both equal to $-3a_0 e\mathcal{E}$ — show these as filled squares in a highlight color. The $2\times 2$ upper-left block containing the nonzero entries should be outlined with a distinct border. The lower-right $2\times 2$ block (all zeros, for $|2p_{\pm 1}\rangle$) should be outlined with a different border to show the block-diagonal structure. Use cell shading intensity, not text, to distinguish zero and nonzero entries.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` $4 \times 4$ matrix grid; 14 zero cells (empty/light gray); 2 nonzero cells at positions $(1,2)$ and $(2,1)$ (filled, highlighted); upper-left $2\times 2$ block outline (active block: $|2s\rangle$–$|2p_0\rangle$ coupling); lower-right $2\times 2$ block outline (zero block: $|2p_{\pm 1}\rangle$ isolated). Block structure reveals the diagonalization: the $m = 0$ sector mixes, the $m = \pm 1$ sector does not. Row/column identities are positional only (no text labels).
- `[O — ORGANIZATION]` $4\times 4$ grid, equal cell sizes. Upper-left block (rows/cols 1–2): outlined in Bluish Green, nonzero cells highlighted. Lower-right block (rows/cols 3–4): outlined in neutral gray. The nonzero cells at $(1,2)$ and $(2,1)$ are symmetric (the matrix is symmetric). Zero cells are lightly gray-filled.
- `[P — PRESENTATION]` Zero cells: neutral light gray fill (20% opacity), 1 pt black grid lines. Nonzero cells $(1,2)$ and $(2,1)$: Bluish Green `#009E73` fill, 1.5 pt stroke. Active block outline: Bluish Green `#009E73`, 2 pt border. Zero block outline: neutral gray, 1 pt dashed border. No text baked in.
- `[E — EXCLUSIONS]` Omit: the Zeeman matrix in the same panel, fine-structure matrix, all-orders perturbation series, higher-$n$ manifold structure, eigenvalue diagram (separate figure), numerical values of matrix elements baked as text.

**BLOCK 3 — NEGATIVE PROMPT:**
Zeeman matrix overlaid, fine-structure off-diagonal elements, eigenvalue energy-level diagram in same panel, numerical matrix values baked as text, color gradient across all 16 cells, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Weak-field Zeeman energy-level splitting:** STATIC SUFFICIENT. A before/after split diagram at a single field value; the key features (unequal spacings, different $g_J$) are readable from a still.

**Figure 2 — Zeeman crossover energy vs. $B$:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The crossover between weak-field (anomalous Zeeman) and strong-field (Paschen-Back) regimes as $B$ sweeps from 0 to 10 T involves a genuine qualitative transformation in the level structure — the levels that were grouped by $j$ regroup by $(m_\ell, m_s)$ — and the avoided crossings in the intermediate-field region are invisible from static end-states alone. Watching the curves evolve continuously makes the connection between the two limiting pictures physical and memorable. **Recommended video for Chapter 9.**

**Figure 3 — Linear Stark effect $n=2$ splitting:** STATIC SUFFICIENT. A scissors fan from four degenerate lines is a static pattern; the linear slopes and flat lines are immediately readable.

**Figure 4 — Rotating-frame transformation:** STATIC SUFFICIENT. A two-panel before/after comparison; the transformation is conceptual and the two states (lab, rotating) are readable side-by-side.

**Figure 5 — Rabi oscillations:** STATIC SUFFICIENT. Three oscillating curves on fixed axes; the resonance and off-resonance peak amplitudes are identifiable from a still.

**Figure 6 — Stark perturbation matrix block structure:** STATIC SUFFICIENT. A $4\times 4$ grid with two highlighted cells; the block-diagonal pattern is a visual-spatial fact readable from a still.
