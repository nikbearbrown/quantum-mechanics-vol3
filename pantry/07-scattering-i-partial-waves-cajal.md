# CAJAL Figure Report — Chapter 7 — Scattering I: Partial Waves

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Scattering Boundary Condition and Wavefunction Geometry

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a schematic of the scattering setup in 2D cross-section. On the left, render a set of equally spaced vertical parallel lines representing the incident plane wave propagating rightward along a horizontal axis labeled $\hat{z}$. At the center, place a small filled circle representing the scatterer. From the scatterer, draw outgoing curved wavefronts (concentric arcs) radiating in all directions, with angular modulation suggested by varying arc thickness — thicker near the forward direction, thinner at large angles. Label the incident beam region, the scatterer, and the outgoing spherical wave region with three annotation points. Include a radial arrow from the scatterer to the far field labeled $r$, a polar angle $\theta$ measured from $\hat{z}$, and a dashed circle at large $r$ indicating the asymptotic region where the boundary condition applies. The scatterer region should be shaded in a neutral gray disc. Use a clean coordinate cross at the origin. The outgoing arcs should be rendered as concentric partial rings, not full circles, to convey the $f(\theta)$ angular modulation.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Incident plane wave (equally spaced vertical lines, propagating along $+\hat{z}$); central scatterer (filled disc); outgoing spherical wavefronts (concentric arcs, angularly weighted); radial coordinate $r$; polar angle $\theta$ between $\hat{z}$ and the observation direction; asymptotic boundary (dashed circle at large $r$); three distinct regions: incident-wave zone, scattering center, far-field zone. No inelastic or multi-body channels.
- `[O — ORGANIZATION]` Horizontal layout: incident beam enters from left; scatterer at geometric center; outgoing arcs spread rightward and sideways. $\theta = 0$ (forward) along the right horizontal. $\theta = \pi$ (backward) along the left horizontal. The asymptotic dashed circle spans full 360°. Annotation points at (1) the plane-wave region, (2) the scatterer disc, (3) the asymptotic arc — three labeled anchors only.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette. Plane-wave lines: Blue `#0072B2`. Outgoing arcs: Bluish Green `#009E73`, arc thickness tapered by angle (thickest near $\theta = 0$) — inferred modulation, label accordingly. Scatterer disc: neutral gray fill, 1 pt Sky Blue `#56B4E9` stroke. Asymptotic dashed circle: light gray, 0.5 pt. All strokes 1 pt unless noted. No text baked in.
- `[E — EXCLUSIONS]` Omit: Born approximation details, partial-wave decomposition labels ($\ell$, $\delta_\ell$), inelastic channels, polarization, spin, time-dependence, 3D perspective rendering, any Argand-diagram elements.

**BLOCK 3 — NEGATIVE PROMPT:**
parallel wavefronts becoming spherical wavefronts without discrete scatterer, far-field intensity plot superimposed, multiple scattering centers, rainbow scattering rings, 3D cone geometry, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Phase Shift: Free vs. Phase-Shifted Radial Wave

**Heuristic:** VG | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two overlaid sinusoidal curves on a shared horizontal axis representing the radial coordinate $r$. The first curve (dashed) is the free radial wave $\sin(kr)$ with no phase shift; it oscillates uniformly. The second curve (solid) is the phase-shifted wave $\sin(kr + \delta_\ell)$, laterally displaced relative to the first. Show one case with $\delta_\ell > 0$ (attractive potential, wave displaced leftward — advanced in phase) and one case with $\delta_\ell < 0$ (repulsive, displaced rightward — retarded). These can be two sub-panels stacked vertically with a shared $r$ axis. In each panel, mark with a vertical dashed line the potential range $a$, shade the interior region ($r < a$) in light yellow, and draw a horizontal double-headed arrow between corresponding zero-crossings of the two curves to indicate the magnitude and sign of $\delta_\ell$. Both curves should vanish at the origin ($r = 0$) to show the boundary condition.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background. Two stacked sub-panels sharing a horizontal $r$-axis; each sub-panel approx. 40 mm tall.
- `[C — CONTENT]` Free radial wave $\sin(kr)$ (dashed); phase-shifted wave $\sin(kr + \delta_\ell)$ (solid); potential range boundary $r = a$ (vertical dashed line); interior region shading ($r < a$); horizontal arrow measuring the phase displacement between nearest zero-crossings; top panel: $\delta_\ell > 0$ (attractive); bottom panel: $\delta_\ell < 0$ (repulsive/hard sphere). Both waves vanish at $r = 0$.
- `[O — ORGANIZATION]` Two sub-panels stacked. Horizontal axis: $r$ from 0 to $\sim 5\lambda$ (several wavelengths). Vertical axis: amplitude $\pm 1$, symmetric. In each panel, the phase-shifted curve is displaced laterally from the free wave. The arrow indicating $\delta_\ell$ is placed between the two curves at the first zero-crossing beyond $r = a$.
- `[P — PRESENTATION]` Free wave: Sky Blue `#56B4E9` dashed, 1 pt. Phase-shifted wave: Blue `#0072B2` solid, 1.5 pt. Interior shading: light gray fill (neutral), 20% opacity. Range boundary: Orange `#E69F00` dashed vertical, 1 pt. Phase-arrow: Bluish Green `#009E73`, no filled arrowhead — open tick marks at endpoints. No text baked in.
- `[E — EXCLUSIONS]` Omit: radial probability density, Born approximation waves, higher-$\ell$ structure, amplitude decay factor $1/r$, inelastic contributions, any energy spectrum, Legendre polynomial shapes.

**BLOCK 3 — NEGATIVE PROMPT:**
3D wavefunction surface, probability density curves, complex amplitude plots, Argand diagrams, multiple overlapping ell channels, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Partial-Wave Cross-Section: $\sigma_\ell$ vs. Phase Shift $\delta_\ell$

**Heuristic:** PQ | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single smooth curve showing the partial-wave cross-section contribution $\sigma_\ell \propto \sin^2\delta_\ell$ as a function of phase shift $\delta_\ell$ ranging from $-\pi$ to $+\pi$ on the horizontal axis. The curve is a $\sin^2$ shape: it starts at zero at $\delta_\ell = 0$, rises to a maximum at $\delta_\ell = \pm\pi/2$, and returns to zero at $\delta_\ell = \pm\pi$. Mark the unitarity maximum at $\delta_\ell = \pi/2$ with a horizontal dashed line. Mark the resonance point ($\delta_\ell = \pi/2$) and the Ramsauer-Townsend zeros ($\delta_\ell = n\pi$, $n \neq 0$) with distinct point markers on the curve. The $y$-axis should start at zero and be labeled proportional to $\sigma_\ell$; the unitarity bound $4\pi(2\ell+1)/k^2$ is shown as the horizontal dashed line at the top. Draw a small inset or secondary axis region at $\delta_\ell = \pi/2$ indicating the resonance.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Curve $\sigma_\ell \propto \sin^2\delta_\ell$ for $\delta_\ell \in [-\pi, \pi]$; unitarity bound (horizontal dashed line at maximum); resonance points at $\delta_\ell = \pm\pi/2$ (filled circle markers); Ramsauer-Townsend zeros at $\delta_\ell = 0, \pm\pi$ (open square markers); $y$-axis from zero to unitarity bound. Period-$\pi$ repetition implied but shown only over $[-\pi, +\pi]$.
- `[O — ORGANIZATION]` Single panel. Horizontal axis: $\delta_\ell$ from $-\pi$ to $+\pi$ with tick marks at $-\pi, -\pi/2, 0, +\pi/2, +\pi$. Vertical axis: $\sigma_\ell$ from 0 to unitarity bound, tick at 0 and at max. The $\sin^2$ curve is smooth, symmetric about $\delta_\ell = 0$. Resonance marker (filled dot): Vermillion `#D55E00`. RT-zero markers (open squares): Blue `#0072B2`.
- `[P — PRESENTATION]` Main curve: Blue `#0072B2`, 1.5 pt solid. Unitarity bound dashed: Orange `#E69F00`, 1 pt. Zero markers: Blue open squares. Resonance markers: Vermillion `#D55E00` filled circles. Axes: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: energy axis, multiple-$\ell$ overlay, Breit-Wigner Lorentzian shape, amplitude $e^{i\delta}\sin\delta$, Argand circle, partial-wave sum across $\ell$, any inelastic channels.

**BLOCK 3 — NEGATIVE PROMPT:**
Breit-Wigner energy-domain plot superimposed, complex S-matrix Argand diagram, multiple ell channels on same axes, 3D bar chart, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Hard-Sphere Cross-Section: $\sigma_{\rm tot}(ka)$ at Low and High Energy

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a single line plot of the total cross-section $\sigma_{\rm tot}/(πa^2)$ on the vertical axis (starting at zero) against $ka$ on the horizontal axis ranging from 0 to about 8. The curve should start at $4$ (the $ka \ll 1$ limit, $\sigma = 4\pi a^2$), oscillate with decreasing amplitude as $ka$ increases, and approach the asymptote $2$ (the $ka \gg 1$ limit, $\sigma = 2\pi a^2$) at large $ka$. Show the two limiting values as horizontal dashed reference lines: one at $y = 4$ (low-energy limit) and one at $y = 2$ (high-energy limit). Mark $y = 1$ with a dotted line to indicate the classical geometric result $\pi a^2$ for comparison. The oscillations at intermediate $ka$ arise from interference among partial waves and should be rendered as a smooth undulating curve asymptoting to $y = 2$.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Curve of $\sigma_{\rm tot}/(\pi a^2)$ for the hard sphere from $ka = 0$ to $ka = 8$ (s-wave only for small $ka$, many-wave sum for large $ka$); low-energy reference line at $y = 4$; high-energy asymptote at $y = 2$; classical reference at $y = 1$. Y-axis from zero to $5$.
- `[O — ORGANIZATION]` Single panel, horizontal layout. $x$-axis: $ka$ from 0 to 8; $y$-axis: $\sigma_{\rm tot}/(\pi a^2)$ from 0 to 5. Three horizontal reference lines: $y = 4$ (dashed), $y = 2$ (dashed), $y = 1$ (dotted). Cross-section curve is smooth. Left-most point anchored near $(0, 4)$.
- `[P — PRESENTATION]` Main cross-section curve: Blue `#0072B2`, 2 pt solid. $y=4$ reference: Bluish Green `#009E73` dashed, 1 pt. $y=2$ reference: Orange `#E69F00` dashed, 1 pt. $y=1$ classical: neutral light gray dotted, 1 pt. Axes: 1 pt black. $y$-axis starts at 0 (hard rule). No text baked in.
- `[E — EXCLUSIONS]` Omit: Yukawa or square-well curves, Born approximation result, resonance spikes from a finite well, differential cross-section angular distribution, 3D sphere geometry illustration, individual partial-wave contributions $\sigma_\ell$.

**BLOCK 3 — NEGATIVE PROMPT:**
resonance spikes from finite well overlaid, polar angular distribution plot, 3D sphere rendering, multiple potential curves on same axes, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Scattering Length and Bound-State Threshold: $a_s(V_0)$

**Heuristic:** PQ | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line plot of the scattering length $a_s$ on the vertical axis against the well depth $V_0$ (in natural units where $\hbar^2/2ma^2 = 1$) on the horizontal axis from $V_0 = 0$ to about $V_0 = 25$. The curve starts negative near zero, diverges to $-\infty$ approaching the first threshold at $V_0 = (\pi/2)^2 \approx 2.47$, jumps discontinuously to $+\infty$, then decreases from large positive values, passes through zero, and diverges again to $-\infty$ near $V_0 = (3\pi/2)^2$, and so on for subsequent thresholds. Show vertical dashed lines at the threshold values $V_0 = (\pi/2)^2, (3\pi/2)^2, (5\pi/2)^2$. Clip the vertical axis to $\pm 5a$ so that the divergences are visually represented as the curve shooting off the top/bottom of the panel. Add small filled circles on the curve at $a_s = 0$ crossings between thresholds to mark where the scattering length changes sign smoothly (inferred relation: these correspond to potential depths where the bound state is well below threshold).

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Scattering length $a_s(V_0)$ for the spherical square well; three divergence thresholds (vertical dashed lines at $V_0 = (\pi/2)^2, (3\pi/2)^2, (5\pi/2)^2$); sign-change zero-crossings between thresholds (filled circle markers); $y$-axis clipped to $\pm 5a$; $y = 0$ reference line. The relationship between divergence and new bound-state appearance is implied by threshold placement.
- `[O — ORGANIZATION]` Single panel. $x$-axis: $V_0$ (natural units) from 0 to 25 with threshold ticks. $y$-axis: $a_s/a$ from $-5$ to $+5$, symmetric about zero. Threshold dashed verticals span full panel height. Curve is smooth between thresholds; near each threshold the curve shoots off toward $\pm\infty$.
- `[P — PRESENTATION]` Main curve: Blue `#0072B2`, 1.5 pt solid. Threshold dashed verticals: Vermillion `#D55E00`, 1 pt. Zero-crossing markers: Bluish Green `#009E73` filled circles, radius 3 pt. $y = 0$ reference: light gray 0.5 pt. $x$-axis, $y$-axis: 1 pt black. No text baked in.
- `[E — EXCLUSIONS]` Omit: cross-section $\sigma_{\rm tot}$ plotted on same axes, hard-sphere $a_s = -a$ flat line, Efimov-state energy levels, effective range expansion, nuclear scattering length data points, any energy-dependence $a_s(k)$.

**BLOCK 3 — NEGATIVE PROMPT:**
cross-section sigma plotted on same panel, Efimov geometric energy spectrum, nuclear data points overlaid, multiple-channel resonance structure, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Breit-Wigner Resonance: $\sigma_0(E)$ Near $E_R$

**Heuristic:** PQ | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a Lorentzian-shaped peak showing the s-wave cross-section $\sigma_0(E)$ as a function of energy $E$ near a resonance energy $E_R$. The vertical axis starts at zero. The horizontal axis is energy with $E_R$ marked by a vertical dashed line at the peak. The peak height is the unitarity limit $4\pi/k_R^2$. Mark the full width at half maximum $\Gamma$ as a horizontal double arrow at half the peak height. Show a second, broader Lorentzian in the same panel (dashed curve) representing a wide resonance with $\Gamma' = 3\Gamma$, to illustrate the inverse relationship between width and quasi-bound-state lifetime. The background (non-resonant) cross-section level should be shown as a low flat line at the base of the Lorentzian. Both curves share the same $E_R$ for comparison.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single-column 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Narrow Lorentzian $\sigma_0(E)$ (solid); resonance energy $E_R$ (vertical dashed line at peak); unitarity bound $4\pi/k_R^2$ (horizontal dashed line at peak); half-maximum level (horizontal dotted line at $2\pi/k_R^2$); width $\Gamma$ marked by double arrow; broader Lorentzian $\Gamma' = 3\Gamma$ (dashed curve, same $E_R$, lower peak — inferred: conservation of area is approximately correct); background cross-section (flat gray line near zero). $y$-axis from zero.
- `[O — ORGANIZATION]` Single panel. $x$-axis: $E$ centered on $E_R$, range $\pm 5\Gamma$. $y$-axis: $\sigma_0$ from 0 to unitarity bound plus 10% margin. Narrow peak solid, broad peak dashed. Width arrow at FWHM height, spanning $\pm\Gamma/2$ around $E_R$. Unitarity-bound dashed line is horizontal.
- `[P — PRESENTATION]` Narrow peak: Blue `#0072B2`, 2 pt solid. Broad peak: Reddish Purple `#CC79A7`, 1.5 pt dashed. $E_R$ dashed vertical: Sky Blue `#56B4E9`, 1 pt. Unitarity-bound horizontal: Orange `#E69F00` dashed. Half-maximum dotted: light gray. Width arrow: Bluish Green `#009E73`, open tick endpoints. Background level: neutral gray 0.5 pt. No text baked in.
- `[E — EXCLUSIONS]` Omit: S-matrix complex plane pole diagram, phase shift $\delta_0(E)$ curve on same axes, Argand circle, inelastic channels, multiple resonances in same panel, energy scale with specific nuclear values.

**BLOCK 3 — NEGATIVE PROMPT:**
S-matrix pole positions in complex k-plane, Argand diagram of partial-wave amplitude, multiple resonances, inelastic threshold features, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Scattering Boundary Condition:** STATIC SUFFICIENT. The spatial geometry is a single fixed configuration; no temporal process is the learning target.

**Figure 2 — Phase Shift (free vs. phase-shifted radial wave):** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The concept of phase shift as a continuous deformation of the radial wavefunction — how turning up $V_0$ gradually advances or retards the phase — is a transformation that cannot be perceived from two static sub-panels alone. An animation sweeping $V_0$ from zero through the first threshold, showing the phase shift $\delta_0$ evolving continuously from 0 toward $-\pi$ (hard sphere) or $+\pi/2$ (resonance), directly embodies the learning objective. **Recommended video for Chapter 7.**

**Figure 3 — $\sigma_\ell$ vs. $\delta_\ell$:** STATIC SUFFICIENT. The $\sin^2$ curve is a single static function; the key features (zeros, maximum) are identifiable from a still.

**Figure 4 — Hard-sphere $\sigma_{\rm tot}(ka)$:** STATIC SUFFICIENT. A single curve on fixed axes; the limiting values and oscillations are readable statically.

**Figure 5 — Scattering length $a_s(V_0)$:** STATIC SUFFICIENT. The divergence structure at thresholds is readable from a still; no sequential causal stages require animation.

**Figure 6 — Breit-Wigner resonance:** STATIC SUFFICIENT. Two Lorentzian shapes on fixed axes; the width-lifetime tradeoff is conveyed by comparing two static curves.
