# CAJAL Figure Report — Chapter 3 — The Variational Principle

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Variational Theorem Proof Structure: Expansion in the Exact Eigenbasis

**Heuristic:** MC — Mechanism/Process | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-step horizontal flowchart representing the proof of the variational theorem. Step 1: expand an arbitrary normalized trial ket as a linear combination of exact eigenstates — show a vertical stack of exact energy levels with weighted arrows flowing into the trial ket symbol, weights indicated by bar-length proportional to |c_n|^2. Step 2: compute the energy expectation value — show the trial ket sandwiching the Hamiltonian, producing a weighted sum of eigenvalues, with a small bar chart inset showing each |c_n|^2 E_n contribution on a vertical axis. Step 3: apply the inequality — replace each E_n by E_0 (the minimum), showing the weighted sum collapses to E_0 times the normalization sum of one. Indicate the inequality direction with a clear "greater than or equal to" visual (≥ as a shape or wedge) pointing from the expectation value to E_0. Connect all three steps with rightward arrows labeled "expand," "evaluate," "bound."

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three-step flow. Step 1: trial ket expanded in exact eigenbasis {|n>} with |c_n|^2 weights shown as bar lengths. Step 2: expectation value as weighted sum of E_n values, bar-chart inset showing individual contributions. Step 3: inequality step where E_n ≥ E_0 for all n implies the weighted sum ≥ E_0. Normalization sum Σ|c_n|^2 = 1 shown as a bracketed constraint. Inequality wedge symbol between step 2 result and E_0.
- `[O — ORGANIZATION]` Horizontal three-step flowchart with labeled connecting arrows. Step 1 left, step 2 center, step 3 right. Each step in a distinct box. Bar-chart inset in step 2 box. Inequality wedge prominent in step 3. Normalization constraint shown as a curly-brace annotation below step 1.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Step 1 box: Sky Blue `#56B4E9`. Step 2 box: Blue `#0072B2`. Step 3 box: Bluish Green `#009E73`. Bar chart bars in step 2: Orange `#E69F00`. Inequality wedge: Vermillion `#D55E00`. Connecting arrows: Blue `#0072B2`. Normalization constraint: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit the excited-state generalization (min-max theorem). Omit the optimization procedure detail (that is Figure 2). Omit the helium or H_2^+ context. Omit the lower-bound impossibility result. Omit any wave-function shape depictions.

**BLOCK 3 — NEGATIVE PROMPT:**
wavefunction plot, orbital diagram, energy level fan, continuous spectrum, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Variational Optimization Landscape: E_V(α) with Minimum and Bounds

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a smooth curve of the variational energy E_V(α) as a function of the variational parameter α, showing a bowl-shaped minimum. Mark the minimum α* with a vertical dashed line and a filled dot on the curve. Draw a horizontal dashed line at E_V(α*) — the best upper bound from this trial family. Draw a second horizontal dotted line below E_V(α*) indicating the true ground-state energy E_0, with a clear downward gap between the two lines. Shade the forbidden region below E_0 in light gray, labeled as "below this: no trial state can go." On the left ascending wing of the curve, indicate a specific α-value and show its corresponding E_V, which is above the minimum, to illustrate that non-optimal parameters give a higher (worse) bound. On the right descending wing, do the same. The visual message: the curve is always above E_0, the minimum is the tightest achievable bound in this family, and any deviation from α* gives a worse bound.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Smooth bowl curve E_V(α) vs. α. Minimum at α* with dot marker and vertical dashed line. Horizontal dashed line at E_V(α*). Horizontal dotted line at E_0 below the minimum. Shaded forbidden region below E_0. Vertical gap indicator between E_V(α*) and E_0. Two off-minimum α markers on left and right wings of the curve with corresponding E_V values shown on the curve. Y-axis starts below E_0 (to show the forbidden region), goes up to well above the curve wings. X-axis from α = 0 upward.
- `[O — ORGANIZATION]` Single panel. α on horizontal axis (zero to rightward). E_V on vertical axis (bottom = below E_0). Bowl curve across center. Minimum point centered. Forbidden region: light gray fill below E_0 line. Vertical dashed line at α*. Horizontal lines at E_V* and E_0. Gap bracket between the two horizontal lines.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Bowl curve: Bluish Green `#009E73`. Minimum point: Orange `#E69F00` filled circle. E_V* dashed line: Orange `#E69F00`. E_0 dotted line: Blue `#0072B2`. Forbidden region fill: light gray (20% opacity). Gap bracket: Vermillion `#D55E00`. Off-minimum markers: Reddish Purple `#CC79A7` open circles. Axes: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit multi-parameter optimization landscape (no 2D surface). Omit the specific helium or harmonic oscillator context. Omit the Rayleigh-Ritz generalization. Omit the excited-state complication. Omit the wave-function quality vs. energy quality distinction (that is Figure 6).

**BLOCK 3 — NEGATIVE PROMPT:**
2D saddle surface, 3D bowl, heatmap, wavefunction plots, orbital diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Helium Variational Energy: E_V(Z̃) Parabola with Optimal Z̃* = 27/16

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a smooth parabolic curve of E_V(Z̃) in eV as a function of the effective nuclear charge Z̃ from 1.0 to 2.5. The curve opens upward and has a minimum near Z̃ = 1.69. Mark the minimum with a vertical dashed line at Z̃ = 27/16 ≈ 1.69 and a filled dot. Draw three horizontal reference lines: one at the variational minimum E_V* ≈ -77.5 eV, one at the experimental value E_exp ≈ -78.98 eV below it, and one at the first-order perturbation theory result E_PT ≈ -74.8 eV above the minimum. Show the vertical gap between E_V* and E_exp as a bracket on the right side. Mark the bare charge Z = 2 with a tick on the horizontal axis to show that the optimal charge (27/16) is less than 2, quantifying the screening effect. The visual message: the parabola bottoms out at Z̃* < Z, and even the minimum lies above the experimental value.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Parabolic curve E_V(Z̃) from Z̃ = 1.0 to 2.5 in eV. Minimum at Z̃ = 27/16 with filled dot and vertical dashed line. Three horizontal reference lines: E_V* = -77.5 eV, E_exp = -78.98 eV, E_PT = -74.8 eV. Bracket on right side showing gap between E_V* and E_exp. Tick on horizontal axis at Z = 2 (bare nuclear charge). Y-axis from approximately -82 to -70 eV (zero would be off-scale; start at a negative value below E_exp).
- `[O — ORGANIZATION]` Single panel. Z̃ on horizontal axis. E_V in eV on vertical axis (negative values, increasing upward toward zero). Parabola occupies center. Minimum marker and vertical dashed line centered. Three horizontal dashed lines (three styles: solid dash, dotted, longer dash to distinguish). Bracket with gap indicator on right margin. Z = 2 tick on horizontal axis with a small offset marker.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Parabola curve: Bluish Green `#009E73`. Minimum point: Orange `#E69F00`. E_V* line: Orange `#E69F00` dashed. E_exp line: Blue `#0072B2` dotted. E_PT line: Reddish Purple `#CC79A7` long-dashed. Gap bracket: Vermillion `#D55E00`. Z = 2 tick: Sky Blue `#56B4E9`. Axes: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit two-parameter Hylleraas extensions. Omit the Hamiltonian decomposition derivation. Omit electron density diagrams. Omit Z ≠ 2 (other elements). Omit wave-function plots. Omit H_2^+ or any molecular context.

**BLOCK 3 — NEGATIVE PROMPT:**
orbital shapes, electron density clouds, atomic radius diagrams, 3D surface plot, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — H₂⁺ LCAO Bonding and Antibonding Energies vs. Internuclear Separation

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line plot with internuclear separation R in Angstrom on the horizontal axis (from 0.3 to 6 Å) and total energy E in eV on the vertical axis (from approximately -14 to -11 eV). Draw two curves: the bonding total energy E_+(R), which descends from high values at small R, passes through a minimum at approximately R = 1.3 Å, and approaches the separated-atom limit from below; and the antibonding total energy E_-(R), which is purely repulsive and approaches the same separated-atom limit from above. Mark the separated-atom limit as a horizontal dashed line at E = -13.6 eV. Mark the bonding minimum with a vertical dashed line at R_eq ≈ 1.3 Å and a filled dot. Indicate the binding energy as the vertical distance from the minimum to the -13.6 eV line. At the right edge of the plot, both curves converge to the same dashed limit line — the antibonding from above, the bonding from below.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two curves: E_+(R) bonding (has minimum at ~1.3 Å, approaches -13.6 eV from below) and E_-(R) antibonding (purely repulsive, approaches -13.6 eV from above). Separated-atom limit at -13.6 eV as horizontal dashed line. Bonding minimum point: R_eq ≈ 1.3 Å, binding energy ≈ 1.77 eV below the limit. Vertical dashed line at R_eq. Binding energy bracket from minimum to -13.6 eV line. X-axis: R from 0.3 to 6 Å. Y-axis from about -14 to -11 eV starting at zero is off-scale — use a y-axis range centered on the physics region, stated bottom at -14 eV.
- `[O — ORGANIZATION]` Single panel. R on horizontal axis (0.3–6 Å). E in eV on vertical axis (-14 to -11 eV range). Bonding curve teal, antibonding curve orange. Dashed horizontal line at -13.6 eV. Vertical dashed line at R_eq. Binding energy bracket on right side of minimum. Curves converging at far right.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Bonding curve E_+(R): Bluish Green `#009E73`. Antibonding curve E_-(R): Orange `#E69F00`. Separated-atom limit dashed line: Blue `#0072B2`. R_eq vertical dashed line: Reddish Purple `#CC79A7`. Minimum point dot: Orange `#E69F00` filled. Binding energy bracket: Vermillion `#D55E00`. Axes: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit the H_2 neutral molecule. Omit the helium context. Omit multi-orbital LCAO (more than two basis functions). Omit spin states. Omit any electron density overlay. Omit the exact (prolate spheroidal coordinate) solution comparison.

**BLOCK 3 — NEGATIVE PROMPT:**
electron density isosurface, orbital lobe diagrams, 3D molecular geometry, ball-and-stick model, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — LCAO Bonding vs. Antibonding: Electron Density Between Nuclei

**Heuristic:** VG — Verification Gap | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side horizontal panels. Each panel shows two dots representing the two protons (A and B) on a horizontal axis, with a shaded density profile representing the electron probability distribution along the internuclear axis. Left panel (bonding orbital, symmetric combination): the density profile shows a clear buildup between the two protons — a hump in the midplane region between A and B, where the wavefunctions add constructively. Right panel (antibonding orbital, antisymmetric combination): the density profile shows a node in the midplane — the distribution is split to the outer sides of each proton, with zero density at the center, where destructive interference occurs. Use a thick horizontal curve above each panel to represent the density as a function of position along the proton-proton axis, with the proton positions marked as vertical tick marks below. The left density curve should peak between the ticks; the right density curve should have a zero crossing between the ticks.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two panels side by side. Each: horizontal axis representing distance along proton-proton line; two proton positions marked as tick marks; electron density curve above axis. Bonding: density peaks between proton positions, constructive midpoint. Antibonding: density goes to zero at midpoint (node), lobes on outer sides of each proton. Node marker on antibonding curve (a dot at zero crossing). Symmetric/antisymmetric wavefunction shape implied by density profiles.
- `[O — ORGANIZATION]` Two-panel layout, left = bonding, right = antibonding. Shared horizontal axis scale (same proton separation in both). Density curves above axis as filled-area profiles. Proton ticks below axis. Node marker prominently placed on antibonding panel at midpoint. Panel separator: thin vertical gray line.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Bonding density fill: Bluish Green `#009E73` at 40% opacity. Antibonding density fill: Orange `#E69F00` at 40% opacity. Density curve outlines: 1pt stroke in respective colors (full opacity). Proton ticks: Blue `#0072B2`. Node marker: Vermillion `#D55E00` open circle at zero. Axis lines: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit two-dimensional density maps or contour plots. Omit the R-dependent energy curves (those are Figure 4). Omit the normalization details. Omit multi-electron molecules. Omit the Rayleigh-Ritz generalization. Omit any molecular orbital energy diagram.

**BLOCK 3 — NEGATIVE PROMPT:**
2D contour density map, 3D isosurface, molecular geometry wireframe, ball-and-stick model, wavefunction sign-labeled lobes with +/- markings, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Energy vs. Wavefunction Convergence: Second-Order Error Scaling

**Heuristic:** VG — Verification Gap | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side line plots sharing a horizontal axis representing a variational parameter ε that measures distance from the optimal trial state (ε = 0 at the minimum). Left panel: variational energy E_V(ε) as a function of ε — a smooth curve with a flat minimum at ε = 0, curving away quadratically. Mark the true energy E_0 as a dashed horizontal line below the curve. The energy error |E_V - E_0| is small and scales as ε^2 near the minimum (the curve is tangent to a horizontal line at ε = 0). Right panel: wave-function error ‖ψ_trial - ψ_0‖ as a function of ε — a curve that passes through zero at ε = 0 but rises linearly away from the minimum. Indicate the different slopes by drawing the tangent lines at ε = 0 for both panels: flat (zero slope) for energy, finite slope for wave function. This makes the quadratic-vs-linear convergence visible.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background. Two-panel layout.
- `[C — CONTENT]` Left panel: E_V(ε) curve with flat minimum at ε = 0; true E_0 dashed line below; tangent line at ε = 0 (horizontal, zero slope). Error region shaded between curve and E_0. Right panel: wave-function error ‖ψ_trial - ψ_0‖ curve linear at origin (V-shaped); tangent line at ε = 0 (finite slope). Both panels share the same ε-axis scale. Inferred relation marker: the ε^2 vs. ε^1 difference is schematic, not exact.
- `[O — ORGANIZATION]` Two-panel layout, left = energy error, right = wavefunction error. Shared horizontal axis (ε from negative to positive). Left: y-axis is E_V, dashed E_0 line, shaded region between curve and E_0. Right: y-axis is ‖error‖, V-shaped curve or parabola from zero. Tangent lines drawn at ε = 0 in both panels. Panel separator: thin vertical gray line.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Energy curve: Bluish Green `#009E73`. E_0 dashed line: Blue `#0072B2`. Energy error shaded region: Orange `#E69F00` at 30% opacity. Energy tangent (horizontal): Orange `#E69F00`. Wavefunction error curve: Reddish Purple `#CC79A7`. Wavefunction tangent (finite slope): Vermillion `#D55E00`. Shared ε axis: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit specific numerical values for helium or H_2^+. Omit the Rayleigh-Ritz or CI context. Omit discussion of the Hellmann-Feynman theorem. Omit multi-parameter optimization. Omit excited-state bounds. Omit any orbital or density diagrams.

**BLOCK 3 — NEGATIVE PROMPT:**
2D optimization landscape, saddle surface, electron density plot, orbital diagram, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Variational Theorem Proof Structure:** STATIC SUFFICIENT. The three-step proof is a causal sequence but not a mechanism with a temporal transition; a flowchart conveys it fully.

**Figure 2 — E_V(α) Optimization Landscape:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The key insight is that the variational energy descends to a minimum and cannot go below E_0 — a one-directional guarantee. Animating a sliding dot along the E_V(α) curve as α is swept, watching the energy approach the minimum and then rise again when α goes too far, makes the optimization process concrete. A secondary animation could show what happens when the trial-family richness increases (the bowl bottom descends toward E_0), illustrating the strategy of choosing richer trial functions. However, the concept is also well-served by the interactive simulation (helium mode). STATIC SUFFICIENT on balance — the simulation covers the dynamic version.

**Figure 3 — Helium E_V(Z̃) Parabola:** STATIC SUFFICIENT. The parabola shape and the three reference lines communicate all necessary information in a single static view. The simulation provides the interactive analog.

**Figure 4 — H₂⁺ Bonding and Antibonding Curves:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages with a transformation below direct observation. As R decreases from infinity to the equilibrium distance, three distinct physical processes are visible in sequence: (1) the overlap S_AB grows from zero; (2) the off-diagonal H_AB becomes nonzero; (3) the bonding curve descends to its minimum while the antibonding curve remains repulsive. Animating R sweeping from 6 Å down to 0.3 Å, with the overlap integral, H_AA, H_AB, and both total energy curves updating in real time, would reveal the mechanism of bond formation in a way that is qualitatively different from a static endpoint plot. Recommended video for Chapter 3.

**Figure 5 — LCAO Density Between Nuclei:** STATIC SUFFICIENT. The constructive/destructive interference contrast is a structural comparison readable as a two-panel static figure. Motion would not add information.

**Figure 6 — Energy vs. Wavefunction Convergence:** STATIC SUFFICIENT. The quadratic vs. linear slope comparison is geometric and legible as a static side-by-side.
