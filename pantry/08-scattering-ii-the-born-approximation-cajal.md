# CAJAL Figure Report — Chapter 8 — Scattering II: The Born Approximation

Recommended: 5 figures, Mixed density.

---

## Figure 1 — Lippmann-Schwinger Geometry: Green's-Function Source Picture

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a schematic of the Lippmann-Schwinger equation as a spatial picture. On the left, show an incident plane wave (equally spaced parallel lines) propagating rightward. In a central region, show the scattering potential as a shaded ellipse, with several interior source points $\mathbf{r}'$ marked as small dots distributed within the shaded region. From each source point, draw a small outgoing spherical wavelet (a partial arc) propagating toward an observation point $\mathbf{r}$ on the right, connected by an arrow labeled with the Green's-function kernel $e^{ik|\mathbf{r}-\mathbf{r}'|}/|\mathbf{r}-\mathbf{r}'|$. Show the total wavefield at $\mathbf{r}$ as the sum of the incident plane wave plus the contributions from all source points. Mark the asymptotic far-field direction $\hat{r}$ with a radial arrow and the outgoing wavevector $\mathbf{k}' = k\hat{r}$. Keep the source points to five or fewer to respect the 6-component limit.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Incident plane wave (parallel lines, leftward propagation); potential region (shaded ellipse); four interior source points $\mathbf{r}'$ (small dots); outgoing spherical wavelets from each source (partial arcs); Green's-function propagation arrows from source to observation point; observation point $\mathbf{r}$ in the far field; outgoing wavevector $\mathbf{k}' = k\hat{r}$; far-field direction arrow $\hat{r}$. The equation is spatial — incident + scattered = total, shown schematically.
- `[O — ORGANIZATION]` Left-to-right flow. Plane wave on left, potential region at center, observation point at right. Source-to-observation arrows fan out from the interior of the shaded region toward $\mathbf{r}$. The far-field point is outside the shaded region with a clear gap. Three annotation anchor points: (1) incident wave, (2) potential/source region, (3) far-field observation point.
- `[P — PRESENTATION]` Plane-wave lines: Blue `#0072B2`, 1 pt. Potential region: Sky Blue `#56B4E9` outline, light gray fill, 1 pt. Source-point dots: Orange `#E69F00` filled circles, 3 pt radius. Green's-function arrows: Bluish Green `#009E73`, 1 pt, single-headed. Observation point: Blue `#0072B2` filled circle, 4 pt. Far-field arrow $\hat{r}$: Blue `#0072B2`, 1.5 pt. No text baked in.
- `[E — EXCLUSIONS]` Omit: Born approximation plane-wave replacement shown in this panel, T-matrix operator notation, Feynman diagram structure, multiple scattering sequences, inelastic channels, bra-ket notation boxes.

**BLOCK 3 — NEGATIVE PROMPT:**
Feynman diagram vertex and propagator notation, T-matrix operator diagram, multiple sequential scattering paths, inelastic final states, complex k-plane contour, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Momentum Transfer Triangle and Angular Geometry

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw the momentum-transfer vector diagram for elastic scattering. Show two vectors of equal length $k$ emanating from a common origin: the incident wavevector $\mathbf{k}$ pointing along $\hat{z}$ (horizontal right) and the scattered wavevector $\mathbf{k}'$ pointing at scattering angle $\theta$ above the horizontal. Draw the vector difference $\mathbf{q} = \mathbf{k} - \mathbf{k}'$ as the vector from the tip of $\mathbf{k}'$ to the tip of $\mathbf{k}$. Mark the angle $\theta$ between $\mathbf{k}$ and $\mathbf{k}'$ with an arc. Mark the angle $\theta/2$ between $\mathbf{q}$ and the bisector of $\mathbf{k}$ and $\mathbf{k}'$. Show the magnitude $q = 2k\sin(\theta/2)$ indicated by the length of the $\mathbf{q}$ vector. Include a second small inset showing the two special cases: (a) $\theta = 0$, $q = 0$ (forward scattering, both vectors aligned); (b) $\theta = \pi$, $q = 2k$ (backscattering, vectors antiparallel).

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Main panel plus small inset (approximately 25 mm wide) at lower right.
- `[C — CONTENT]` Incident wavevector $\mathbf{k}$ (length $k$); scattered wavevector $\mathbf{k}'$ (length $k$, at angle $\theta$); momentum transfer $\mathbf{q} = \mathbf{k} - \mathbf{k}'$; scattering angle $\theta$ arc; half-angle $\theta/2$ tick; $|\mathbf{q}| = 2k\sin(\theta/2)$ — the geometric relationship, labeled as inferred from the triangle. Inset: two limiting cases ($\theta = 0$ and $\theta = \pi$) as compact diagrams.
- `[O — ORGANIZATION]` Main vector diagram: all three vectors from/to a central origin point. $\mathbf{k}$ horizontal right; $\mathbf{k}'$ angled upward at $\theta \approx 45°$ for visual clarity; $\mathbf{q}$ closing the triangle. Inset at lower right: two side-by-side mini-diagrams for the two limits.
- `[P — PRESENTATION]` $\mathbf{k}$: Blue `#0072B2`, 2 pt, single-headed. $\mathbf{k}'$: Bluish Green `#009E73`, 2 pt, single-headed. $\mathbf{q}$: Orange `#E69F00`, 2 pt, single-headed. Angle arc: Sky Blue `#56B4E9`, 1 pt. Inset vectors: same colors, 1 pt. No text baked in.
- `[E — EXCLUSIONS]` Omit: Rutherford cross-section plot, angular distribution $d\sigma/d\Omega$, Fourier transform representation, Born amplitude value, inelastic scattering kinematics where $|\mathbf{k}'| \neq |\mathbf{k}|$.

**BLOCK 3 — NEGATIVE PROMPT:**
inelastic kinematics with different length k and k-prime, polar cross-section plot, Fourier space depiction of potential, multi-loop Feynman diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Yukawa and Rutherford Angular Distributions: $d\sigma/d\Omega$ vs. $\theta$

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a log-scale line plot of differential cross-section $d\sigma/d\Omega$ (in units of $a^2 = 1/\mu^2$) on the vertical axis against scattering angle $\theta$ from 0° to 180° on the horizontal axis. Show three curves: (1) the Yukawa Born result at moderate $ka$ (solid), (2) the Yukawa Born result at larger $ka$ (dashed — narrower forward peak), and (3) the pure Coulomb ($\mu \to 0$) Rutherford $\sin^{-4}(\theta/2)$ divergence at forward angles (dotted, clipped at $\theta_{\rm min} \sim 5°$ to avoid infinite display). The Yukawa curves should show a forward peak that falls off smoothly to smaller values at backward angles; the Rutherford curve should diverge steeply near $\theta = 0$. Mark $\theta = 90°$ with a vertical dotted reference line. The $y$-axis should start at the minimum resolved value (log scale, not zero) and span several decades.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Log $y$-axis spanning $\sim 4$ decades.
- `[C — CONTENT]` Yukawa Born $d\sigma/d\Omega$ at $ka = 1$ (solid); Yukawa Born at $ka = 4$ (dashed, narrower forward peak — inferred relationship to momentum transfer); Rutherford (Coulomb) $\sin^{-4}(\theta/2)$ (dotted, clipped near $\theta = 0$); $\theta = 90°$ reference vertical; $y$-axis in units of $a^2$. All three are for the same potential type (Yukawa/Coulomb family), illustrating the energy and screening dependence.
- `[O — ORGANIZATION]` Single panel. $x$-axis: $\theta$ from 0° to 180° with ticks at 30°, 60°, 90°, 120°, 150°, 180°. $y$-axis: log scale, labeled in decades. Curves labeled at $\theta = 60°$ region. Rutherford curve rises steeply as $\theta \to 0$; Yukawa curves level off or fall more slowly.
- `[P — PRESENTATION]` Yukawa ($ka = 1$): Blue `#0072B2`, 2 pt solid. Yukawa ($ka = 4$): Bluish Green `#009E73`, 1.5 pt dashed. Rutherford: Orange `#E69F00`, 1.5 pt dotted. $\theta = 90°$ reference: light gray dotted, 0.5 pt. Axes: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: exact partial-wave result comparison in this panel, Born validity shading, Born parameter $\xi$ annotations, Sommerfeld parameter contours, polar/rose plot representation, individual partial-wave contributions.

**BLOCK 3 — NEGATIVE PROMPT:**
polar rose plot of angular distribution, exact partial-wave overlay in this panel, Born validity shading regions, 3D scattering sphere geometry, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Born Validity Diagram: $\xi$ vs. $ka$ Parameter Space

**Heuristic:** VG | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-region parameter-space diagram with $ka$ on the horizontal axis (log scale, range $10^{-1}$ to $10^2$) and Born parameter $\xi = 2m|V_0|/\hbar^2\mu^2$ on the vertical axis (log scale, range $10^{-2}$ to $10^2$). Divide the plane into two regions: (1) a Born-valid region at lower left (small $\xi$) and at lower right (large $ka$, any $\xi$), shaded in Bluish Green; (2) a Born-invalid region at upper left (large $\xi$, small $ka$), shaded in neutral light gray. The boundary curve is $ka \approx \xi$ (a diagonal line in log-log space). Add a dashed contour showing the Sommerfeld parameter $\eta = 1$ in the Coulomb regime (approximately a hyperbola in this space). Mark with small filled circles the positions of a few representative physical systems: hard sphere at moderate $ka$, Yukawa at $\xi = 0.5$, near-resonant Yukawa at $\xi = 5$, $ka = 1$.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Horizontal axis: $ka$ (log, $10^{-1}$ to $10^2$); vertical axis: $\xi = 2m|V_0|/\hbar^2\mu^2$ (log, $10^{-2}$ to $10^2$); Born-valid region (lower left and lower right, Bluish Green shading); Born-invalid region (upper left, gray shading); boundary curve $ka \approx \xi$ (diagonal); Sommerfeld parameter $\eta = 1$ contour (dashed — inferred: relevant for Coulomb context); three representative system markers (filled circles). Regions labeled by icon or pattern only (no text).
- `[O — ORGANIZATION]` Log-log plot. Boundary line runs diagonally from lower left to upper right. The Born-valid region lies below and to the right of the boundary. The Sommerfeld $\eta = 1$ contour is roughly $\xi \propto 1/ka$, a hyperbola. System markers at three distinct positions.
- `[P — PRESENTATION]` Born-valid region: Bluish Green `#009E73` fill, 30% opacity. Born-invalid region: light gray fill, 20% opacity. Boundary curve: Blue `#0072B2`, 2 pt solid. Sommerfeld contour: Reddish Purple `#CC79A7`, 1.5 pt dashed. System markers: Orange `#E69F00` filled circles, 4 pt radius. Axes: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: individual Born cross-section curves, Lorentzian resonance spikes at specific energies, any specific material or nuclear system labels, quantum field theory Feynman coupling, 3D heatmap coloring, rainbow palette.

**BLOCK 3 — NEGATIVE PROMPT:**
cross-section curves overlaid on validity map, QFT coupling constant axes, 3D heatmap surface, specific material labels as text, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Nuclear Form Factor: $|F(q)|^2$ for a Uniform Sphere

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line plot of the nuclear form factor $|F(q)|^2$ on the vertical axis (starting at zero, dimensionless, range 0 to 1) against the dimensionless momentum transfer $qR$ on the horizontal axis (range 0 to about 15). The curve starts at $|F(0)|^2 = 1$, oscillates with decreasing envelope (like a $j_1^2(qR)/(qR)^2$ diffraction pattern), and crosses zero at $qR \approx 4.49$ (the first zero of the sphere form factor). Mark the first zero with an open circle on the $x$-axis and indicate it corresponds to the experimental determination of the nuclear radius $R$ via $q = 4.49/R$. Also draw a dotted envelope curve showing the $\sim (qR)^{-4}$ asymptotic decay of the oscillation peaks. Add a short horizontal bar at the top indicating $|F(0)|^2 = 1$ (always, by normalization). The $y$-axis must start at zero.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` $|F(q)|^2 = [3j_1(qR)/(qR)]^2$ for a uniform sphere; starting value at $qR = 0$: $|F|^2 = 1$; first zero at $qR \approx 4.49$ (open circle); oscillating pattern with decreasing envelope to $qR = 15$; dotted envelope indicating power-law decay; $y$-axis from 0 to 1; $x$-axis in units of $qR$. The relationship between first zero position and nuclear radius $R$ is marked (inferred: this is the Hofstadter radius measurement principle).
- `[O — ORGANIZATION]` Single panel. $x$-axis: $qR$ from 0 to 15 with tick at first zero. $y$-axis: 0 to 1.0. Main curve oscillates; envelope dotted curve above it. First-zero marker at $(4.49, 0)$.
- `[P — PRESENTATION]` Main form-factor curve: Blue `#0072B2`, 2 pt solid. Envelope dotted: Sky Blue `#56B4E9`, 1 pt dotted. First-zero marker: Orange `#E69F00` open circle, 4 pt. $y = 1$ horizontal reference bar: Bluish Green `#009E73`, 0.5 pt. Axes: 1 pt black. $y$-axis starts at 0. No text baked in.
- `[E — EXCLUSIONS]` Omit: Yukawa or Gaussian form factors on the same panel, proton electromagnetic form factor from experiment, 3D nuclear density plot, charge distribution $\rho(r)$ panel, Born cross-section $d\sigma/d\Omega$ overlaid.

**BLOCK 3 — NEGATIVE PROMPT:**
Gaussian form factor overlaid, experimental proton electromagnetic form factor data, 3D nuclear density sphere, charge distribution panel, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Lippmann-Schwinger Green's-function source picture:** STATIC SUFFICIENT. The geometry is a fixed spatial configuration; the integral equation structure is not a temporal process.

**Figure 2 — Momentum transfer triangle:** STATIC SUFFICIENT. A vector diagram with one angle parameter; the geometric relationship $q = 2k\sin(\theta/2)$ is readable from a still.

**Figure 3 — Yukawa/Rutherford angular distributions:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. An animation sweeping $ka$ from small to large values shows how the forward peak narrows and the Rutherford regime emerges as the screening scale $\mu$ becomes negligible relative to $k$. This dynamic — the sharpening of the diffraction peak and its approach to the Coulomb divergence — cannot be perceived from two static curve overlays. **Recommended video for Chapter 8.**

**Figure 4 — Born validity diagram:** STATIC SUFFICIENT. The two-region parameter map is a static classification; the boundary curve is read from a still.

**Figure 5 — Nuclear form factor:** STATIC SUFFICIENT. An oscillating curve on fixed axes; the first-zero position is identifiable from a still.
