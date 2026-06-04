# CAJAL Figure Report — Chapter 4 — The WKB Approximation and Tunneling

Recommended: 6 figures, Mixed density.

---

## Figure 1 — WKB wave function amplitude and phase in classically allowed vs. forbidden regions

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a single horizontal axis representing position x with a smooth potential energy curve V(x) sitting above it. Mark a horizontal energy line E intersecting V(x) at two classical turning points, labeling them a on the left and b on the right. In the classically allowed region between a and b, draw an oscillating wave whose amplitude swells where V(x) is near E (slow particle, large de Broglie wavelength) and contracts where V(x) is well below E (fast particle, small wavelength). The envelope of the oscillation should be visually proportional to 1/√p(x). In the classically forbidden regions outside a and b, draw the wave as an exponentially decaying profile that asymptotes to zero. Mark the three spatial zones with distinct background shading: forbidden left, allowed center, forbidden right. Indicate the 1/√p(x) amplitude relationship with a bracket annotation on the allowed-region oscillation.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Smooth potential curve V(x); horizontal energy line E; two classical turning points a and b where E = V(x); oscillatory WKB wave function in allowed zone with amplitude envelope ∝ 1/√p(x) — amplitude larger near turning points, smaller at potential minimum; exponentially decaying wave function tails in both forbidden zones; three shaded background regions (forbidden/allowed/forbidden); label for local momentum p(x) = √(2m(E−V(x))); implicit contrast between slow-particle (large λ_dB) and fast-particle (small λ_dB) regions via wave spacing.
- `[O — ORGANIZATION]` Single horizontal panel. x increases left to right. V(x) drawn as a smooth hill or well with two intersection points with E. Wave function drawn below V(x) in its own horizontal band. Forbidden zones shaded in neutral gray; allowed zone in light Sky Blue. Turning-point labels a and b as vertical dashed lines. 1/√p amplitude bracket on allowed region oscillations.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito palette: allowed zone background Sky Blue `#56B4E9` at low opacity; forbidden zone background light gray; V(x) curve Blue `#0072B2`, 1.5 pt; energy line E Orange `#E69F00`, 1 pt dashed; wave function in allowed zone Bluish Green `#009E73`, 1 pt; decaying tails Vermillion `#D55E00`, 1 pt; turning point verticals gray 1 pt dashed. Uniform stroke weight. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Airy function detail at turning points; second-order WKB terms; 3D potentials; specific functional forms of V(x); complex S(x) derivation steps; numerical values; spin or angular momentum; the Langer correction.

**BLOCK 3 — NEGATIVE PROMPT:**

specific functional forms, numerical axis labels, mathematical equations baked in, Airy function curves, 3D rendering, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders.

---

## Figure 2 — Classical turning point and Airy function connection

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a close-up view centered on a single classical turning point x₀ where the potential V(x) crosses the energy line E from below (classically forbidden on the right, allowed on the left). Show the linearized potential approximation as a straight sloped line through x₀. On the left (allowed) side, draw the Airy function as an oscillating decaying wave with a visible π/4 phase offset relative to a naive cosine — mark this phase shift with a small arc. On the right (forbidden) side, draw the Airy function as a smooth single-lobe exponential decay going to zero. Bridge the two sides with a short connecting region centered at x₀ where neither the oscillatory nor the decaying form applies — shade this region distinctly to show the matching zone. Use a bracket or arrow to mark the Maslov π/4 phase contribution.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Single turning point x₀; linearized potential line through x₀; energy line E; classically allowed region (left) with Ai(z) oscillatory asymptotic; classically forbidden region (right) with Ai(z) decaying asymptotic; intermediate matching zone centered on x₀; Maslov π/4 phase shift indicated on the oscillatory side; the transition from oscillation to decay as a visual narrative across the panel.
- `[O — ORGANIZATION]` Horizontal layout, x₀ at center. V(x) and E in upper portion of panel. Airy function profile in lower portion. Three zones: allowed (left, Sky Blue background), matching zone (center, Reddish Purple background at low opacity), forbidden (right, gray background). Phase-shift indicator arc on the oscillatory side. Arrow indicating direction of WKB validity degradation approaching x₀ from both sides.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: allowed zone background Sky Blue `#56B4E9`; forbidden zone gray; matching zone Reddish Purple `#CC79A7` low opacity; linearized V(x) Orange `#E69F00` 1.5 pt; Airy function Bluish Green `#009E73` 1.5 pt; E line Blue `#0072B2` 1 pt dashed; phase-shift arc Vermillion `#D55E00` 1 pt; x₀ marker vertical gray 1 pt dashed. Uniform 1 pt strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Bi(z) (irregular Airy function); Bohr-Sommerfeld quantization; multiple turning points; the full WKB wave on the far side; numerical Airy function values; derivation algebra; the Langer correction.

**BLOCK 3 — NEGATIVE PROMPT:**

Bi(z) irregular Airy function, multiple turning points, numerical values baked in, derivation algebra, full WKB waveform beyond the matching zone, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 3 — Bohr–Sommerfeld phase-space orbit and quantization condition

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a 2D phase-space diagram with position x on the horizontal axis and momentum p on the vertical axis. For the harmonic oscillator, draw a closed elliptical orbit centered at the origin. Shade the interior of the ellipse. On the same plot, draw three nested ellipses corresponding to n = 0, n = 1, and n = 2 — the smallest innermost for n = 0. Mark the semi-axes of the n = 1 ellipse with brackets: semi-axis in x as √(2mE)/(mω) and semi-axis in p as √(2mE). The shaded area of each ellipse should visually suggest the quantized values (n + ½)h. The classical turning points at a and b on the x-axis should be visible as the points where p = 0.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Phase space (x, p) coordinate axes with origin; three nested closed elliptical orbits for n = 0, 1, 2 (harmonic oscillator); shaded ellipse interiors showing enclosed area; classical turning points a, b marked where orbits cross p = 0 on x-axis; semi-axis brackets on n = 1 ellipse indicating x-extent and p-extent; visual indication that area ∮p dx = (n + ½)h grows with n; the n = 0 ellipse nonzero (zero-point energy is a Maslov correction — area ≠ 0).
- `[O — ORGANIZATION]` Standard (x, p) plane with x horizontal, p vertical. Origin at center. Nested ellipses. Shade interiors with progressively deeper color for n = 0, 1, 2. Turning points as dots on the x-axis. Semi-axis brackets outside the n = 1 ellipse. No tick values.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: n = 0 ellipse interior Sky Blue `#56B4E9` at 20% opacity; n = 1 interior at 35%; n = 2 interior at 50%; all ellipse outlines Blue `#0072B2` 1.5 pt; turning point dots Orange `#E69F00`; semi-axis brackets Bluish Green `#009E73` 1 pt; coordinate axes gray 1 pt. Uniform strokes. White background. No baked text. Y-axis starts at bottom of visible range (p can be negative; both axes span symmetric ranges around zero).
- `[E — EXCLUSIONS]` Omit: specific numerical values of energy levels; non-harmonic-oscillator orbits; 3D phase space; canonical transformation details; Fock SU(2) symmetry discussion; Langer correction; Runge-Lenz vector.

**BLOCK 3 — NEGATIVE PROMPT:**

non-elliptical orbits, numerical axis tick values baked in, 3D phase space, Runge-Lenz vector, Fock symmetry notation, drop shadows, gradient fills, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 4 — Gamow factor and tunneling transmission coefficient

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a one-dimensional potential barrier profile V(x) rising above the particle energy line E between two classical turning points a and b. Shade the forbidden region between a and b. On the left of the barrier, draw an incoming oscillatory wave and a smaller-amplitude reflected wave. On the right, draw a transmitted wave whose amplitude is exponentially smaller than the incoming wave. Inside the shaded forbidden region, draw a decaying exponential profile representing the wave function magnitude. Mark the integration region from a to b with a bracket labeled as the Gamow integral γ. Add a visual indicator showing that the transmitted amplitude squared is proportional to e^{−2γ}. Draw three comparison barrier profiles side by side — rectangular, triangular, Coulomb-shaped — at the same height to illustrate that the shape is absorbed into the integral.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Two sub-panels: left panel (main tunneling schematic), right panel (three barrier shape comparison strip).
- `[C — CONTENT]` Left panel: potential barrier V(x) above energy line E; turning points a and b; shaded forbidden zone; incoming oscillatory wave left of a; reflected wave left of a (smaller amplitude); decaying exponential inside barrier; transmitted wave right of b (smaller amplitude than incoming); Gamow integral bracket from a to b; e^{−2γ} amplitude-squared ratio indicator. Right panel: three barrier silhouettes at equal height — rectangular (flat top), triangular (linear sides), Coulomb (1/r curved, asymmetric decay). All shown at same E level to emphasize that shape only affects the integral value.
- `[O — ORGANIZATION]` Left panel occupies 65% of canvas width, right panel 35%. Left panel: x horizontal, V(x) as a smooth hill. Right panel: three vertically stacked barrier shape silhouettes (or side-by-side), no wave functions. Incoming/reflected/transmitted waves clearly separated by barrier.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: barrier shading Reddish Purple `#CC79A7` at low opacity; V(x) curve Blue `#0072B2` 1.5 pt; E line Orange `#E69F00` 1 pt dashed; incoming wave Bluish Green `#009E73` 1.5 pt; reflected wave (same color, smaller amplitude); decaying interior Orange `#E69F00` 1 pt dashed curve; transmitted wave Bluish Green `#009E73` 1 pt (visibly smaller amplitude); turning point verticals gray 1 pt dashed; barrier shapes in right panel Sky Blue `#56B4E9` filled silhouettes. Uniform 1 pt strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: prefactor derivation details; matrix-matching equations; alpha-decay numerics; STM or stellar-fusion context in this figure; Langer correction; reflection/transmission coefficient formulae as text.

**BLOCK 3 — NEGATIVE PROMPT:**

matrix matching algebra, numerical coefficient values baked in, alpha decay nucleus diagram, STM tip geometry, Langer correction notation, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 5 — Geiger–Nuttall law: log halflife vs. 1/√E_α

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a scatter plot with the horizontal axis representing 1/√E_α (inverse square root of alpha energy) and the vertical axis representing log₁₀(halflife in seconds), with the y-axis starting at zero at the bottom and spanning from roughly −8 (microseconds) to +25 (longer than the age of the universe). Plot six to eight representative data points as filled circles, arranged along a clear straight line — the Geiger–Nuttall line. Mark two of the data points with distinct markers indicating polonium-212 (near the lower-left, short halflife, high energy) and thorium-232 (near the upper-right, long halflife, low energy). Draw the best-fit straight line through the data points. The dynamic range on the y-axis — spanning roughly 33 decades — should be visually prominent. No specific nuclide labels baked into the image.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Scatter plot: x-axis = 1/√E_α (arbitrary scaled units, no numbers baked in), y-axis = log₁₀(τ₁/₂/s) starting at zero; six to eight data points lying on a straight line; best-fit Geiger–Nuttall line; two distinguished data points (Po-212 near lower-left; Th-232 near upper-right) indicated by distinct marker shape; vertical axis spanning ~33 decades of dynamic range prominently visible.
- `[O — ORGANIZATION]` Standard scatter plot. x-axis horizontal, y-axis vertical from 0 at bottom. Data points as filled circles with two distinguished as hollow diamonds or squares. Best-fit line drawn through all points. Tick marks on axes without numerical labels. Both axes labeled with schematic symbols only (no numbers).
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: data point circles Blue `#0072B2` filled; two distinguished points Orange `#E69F00` filled diamonds; best-fit line Vermillion `#D55E00` 1.5 pt; axis lines and ticks gray 1 pt. Y-axis starts at zero. No 3D. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: nuclide names or symbols baked in; numerical axis values; error bars; multiple Geiger–Nuttall lines for different Z'; the Gamow integral derivation; any decay chain information; non-alpha emitters.

**BLOCK 3 — NEGATIVE PROMPT:**

nuclide name labels, numerical axis tick values, error bars, multiple Z' family lines, decay chain arrows, non-alpha emitter data, 3D perspective, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 6 — Exponential tunneling across physical contexts: STM, alpha decay, stellar fusion, flash memory

**Heuristic:** MC — Mechanism/Process | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw four small schematic panels arranged in a 2×2 grid, each illustrating a different physical context where the Gamow exponential appears. Panel 1 (STM): a pointed triangular tip shape approaching a flat surface with a gap between them, and a small horizontal arrow suggesting current flowing across the gap. Panel 2 (alpha decay): a rounded nucleus silhouette with a curved Coulomb barrier hump and a small particle dot emerging from the barrier on the right side. Panel 3 (stellar fusion): two small circle particles approaching each other against a potential hill, with a single merged circle on the other side of the hill. Panel 4 (flash memory): a layered rectangle structure (three horizontal bands representing metal-oxide-silicon layers) with a small arrow crossing through the thin middle band. All four panels share the same visual motif: a barrier hill and a particle passing through it, unified by the e^{−2γ} exponential structure.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Four equal sub-panels in 2×2 grid.
- `[C — CONTENT]` Panel 1 (STM): cone-shaped tip; flat surface below; vacuum gap between; current arrow traversing gap. Panel 2 (alpha decay): nucleus circle; Coulomb barrier curve above energy line; alpha particle dot exiting right of barrier. Panel 3 (stellar fusion): two proton circles on left; Coulomb barrier hill; fused deuteron on right; energy line below barrier top. Panel 4 (flash memory): three horizontal bands (conductor / thin SiO₂ layer / conductor); vertical arrow crossing the thin middle band under applied field (triangular Fowler–Nordheim barrier shape). Each panel: one small barrier silhouette + one particle entity. Unified motif: barrier + particle + exponential decay.
- `[O — ORGANIZATION]` 2×2 grid layout. Each sub-panel self-contained with its own minimal barrier schematic. No shared axes. Visual similarity between the four barrier profiles emphasized by consistent geometry. Panels separated by thin gray border lines.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: barrier fill Reddish Purple `#CC79A7` at low opacity; particle circles Blue `#0072B2`; energy line Orange `#E69F00` 1 pt dashed; barrier outlines Blue `#0072B2` 1.5 pt; flash memory layers Sky Blue `#56B4E9` and neutral gray alternating; current/particle arrows Bluish Green `#009E73` 1.5 pt; panel borders light gray 0.5 pt. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: tunneling time discussion; DNA proton tunneling; cold fusion context; detailed Fowler–Nordheim formula; STM atomic resolution image; solar fusion rate formula; specific energy values.

**BLOCK 3 — NEGATIVE PROMPT:**

DNA helix, cold fusion apparatus, atomic resolution STM image, detailed circuit diagram, Fowler-Nordheim formula notation, numerical energy values baked in, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Video Candidate Pass

**Figure 1 — WKB wave function in allowed/forbidden regions:** STATIC SUFFICIENT. The spatial structure is fully captured by a still schematic. No transition mechanism is the learning target; the relationship between amplitude and local momentum is a spatial, not temporal, concept.

**Figure 2 — Airy function connection at a turning point:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The connection formula describes how an oscillatory wave morphs continuously into an exponential decay as x crosses x₀. A brief animation sweeping x through the matching zone — showing the Airy function profile evolving from oscillatory to decaying with the π/4 phase shift visibly emerging — would make the topological nature of the Maslov index viscerally clear in a way no static snapshot can. **Recommended video for this chapter.**

**Figure 3 — Bohr–Sommerfeld phase-space orbit:** STATIC SUFFICIENT. The nested ellipses and quantized areas are a static geometric relationship; no causal sequence of steps is involved.

**Figure 4 — Gamow factor and barrier tunneling:** STATIC SUFFICIENT. The wave amplitude contrast (incoming vs. transmitted) is most clearly shown as a side-by-side still; animation would add complexity without adding comprehension.

**Figure 5 — Geiger–Nuttall plot:** STATIC SUFFICIENT. A data plot is inherently static; the dynamic range is communicated by the axis span, not by motion.

**Figure 6 — Four-context panel (STM, alpha, fusion, flash memory):** STATIC SUFFICIENT. The point is structural similarity across contexts; a grid of four stills communicates this better than sequential animation.
