# CAJAL Figure Report — Chapter 11 — Capstone — Modeling a Real Quantum System

Recommended: 5 figures, Mixed density.

---

## Figure 1 — The Five-Move Modeling Framework as a Process Flow

**Heuristic:** MC | **Rank:** Critical

---

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a vertical process flowchart on a white background, no text. Show five rectangular nodes stacked from top to bottom, connected by downward arrows. The first node is filled with a neutral anchor color. Each subsequent node is filled with a progressively distinct flat color following a fixed palette, representing the five sequential moves in building a quantum model. Between the fourth and fifth nodes, insert a feedback loop: a curved arrow looping from the fifth node back upward to the second node, suggesting iteration when the breakdown analysis indicates the method must be revised. All nodes have uniform rounded corners and 1pt strokes. No text, icons, or labels of any kind.

---

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column, 89 mm wide, 300 DPI, SVG/EPS, white background.

- `[C — CONTENT]` Five rectangular nodes representing: (1) System Identification, (2) Method Selection, (3) Calculation, (4) Validation, (5) Breakdown Analysis — in exactly this top-to-bottom order as stated in the chapter. Connecting arrows between consecutive nodes indicate sequential execution. A feedback arc from node 5 back to node 2 represents the chapter's explicit statement that a failed breakdown analysis triggers method revision. All relationships are direct from the chapter's five-move structure; no inferred content.

- `[O — ORGANIZATION]` Vertical single-column layout. Nodes centered on a vertical axis, equal vertical spacing, equal node dimensions (approximately 60 mm wide × 10 mm tall). Arrows: 1pt with single arrowheads pointing downward. Feedback arc: curved 1pt line on the right side of the diagram, looping from node 5 back up to node 2, arrowhead pointing into node 2.

- `[P — PRESENTATION]` Flat vector. Node 1 (System ID): Sky Blue #56B4E9 fill. Node 2 (Method Selection): Orange #E69F00 fill. Node 3 (Calculation): Bluish Green #009E73 fill. Node 4 (Validation): Blue #0072B2 fill. Node 5 (Breakdown): Reddish Purple #CC79A7 fill. All node text absent (no baked labels). Arrow strokes: neutral dark gray, 1pt. Feedback arc: Vermillion #D55E00, 1pt. White background.

- `[E — EXCLUSIONS]` Omit: specific system names (STM, QD, Rabi, etc.), small-parameter formulas, equations of any kind, sub-bullet content from any node, Bloom-taxonomy annotations, rubric criteria, parallel branches for the six candidate systems.

---

**BLOCK 3 — NEGATIVE PROMPT**

text labels, node names, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 2 — Six Candidate Systems Mapped to Methods and Small Parameters

**Heuristic:** VG | **Rank:** Critical

---

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a two-column comparison panel on a white background, no text. On the left column show six compact schematic icons arranged vertically, one for each candidate system: a narrow rectangular gap between two blocks (STM barrier), a small sphere with concentric rings (quantum dot), a symmetric double-well curve (ammonia inversion), a vertical arrow in a horizontal field (NMR spin), two small circles orbiting a nucleus (helium), and a diverging set of arc paths (Rutherford scattering). On the right column, aligned horizontally with each icon, show a small horizontal bar whose length encodes the magnitude of the system's small parameter ε — shorter bars for smaller ε (more valid approximation), longer bars for larger ε (less valid). Bars are all drawn in a single flat color. No text, labels, or numbers anywhere.

---

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column, 89 mm wide, 300 DPI, SVG/EPS, white background.

- `[C — CONTENT]` Six rows, one per candidate system (A–F), exactly as enumerated in the chapter's small-parameter table. Left column: minimal iconic schematic for each system. Right column: a horizontal bar chart encoding the approximate ε value for each system at the chapter's "textbook" parameter values: System A (WKB STM): ε ~ 0.05 (very small); System B (QD spherical box): ε ~ 0.4 (moderate); System C (ammonia maser): ε ~ 0.001 (very small); System D (NMR Rabi): ε ~ 0.003 (very small); System E (variational He): ε ~ 0.3 (borderline); System F (Born Rutherford): ε ~ 0.15 (small). The bar lengths are proportional to these values. Bar color encodes validity: Bluish Green #009E73 for ε < 0.3, Orange #E69F00 for 0.3 ≤ ε < 1.0. The ε values are explicitly stated in the chapter's CLAUDE.md section; the color thresholds are the chapter's own green/yellow/red rule.

- `[O — ORGANIZATION]` Six equally spaced horizontal rows. Left column (~40% of width): system icon, centered in its cell. Right column (~60% of width): horizontal bar originating from the left edge of the column, length proportional to ε, capped at the column right edge for ε = 1.0. A faint vertical dashed line at the ε = 0.3 threshold position divides the "safe" from the "caution" zone. Rows read top to bottom in A–F order.

- `[P — PRESENTATION]` Flat vector. Low-ε bars (ε < 0.3): Bluish Green #009E73. Moderate-ε bars (ε ≥ 0.3): Orange #E69F00. Threshold dashed line: Sky Blue #56B4E9, 0.75pt dashed. System icons: Blue #0072B2 outline, neutral gray fill, 1pt strokes. Row dividers: light gray, 0.5pt. White background. No baked text.

- `[E — EXCLUSIONS]` Omit: method names spelled out, ε formulas, system letters (A–F) as text, citation markers, breakdown text, the five-move flowchart content, any quantitative axis labels.

---

**BLOCK 3 — NEGATIVE PROMPT**

text labels, system letters, ε values, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 3 — WKB STM: Exponential Current vs. Tip-Sample Distance

**Heuristic:** PQ | **Rank:** Critical

---

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a single-panel graph on a white background, no text. The horizontal axis runs from left to right representing tip-sample distance (spanning approximately 2 to 12 Å). The vertical axis is logarithmic, increasing upward. Plot one smooth straight line (the WKB prediction on a log scale, which is linear) in a flat blue color. Mark two or three discrete data points as filled circles in a contrasting flat color, sitting close to but not necessarily exactly on the line (representing the experimental validation points from Binnig and Rohrer). Draw a short horizontal dashed line segment at a fixed intermediate y-position indicating the "factor of ~8 per ångström" benchmark level. No text, axes labels, or tick-mark numbers anywhere.

---

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column, 89 mm wide, 300 DPI, SVG/EPS, white background.

- `[C — CONTENT]` The WKB tunneling current I(d) ∝ exp(−2κd) plotted on a log scale, for κ = 1.025 Å⁻¹ (from the chapter's worked example with φ = 4.0 eV). Horizontal axis: d from 2 to 12 Å. Vertical axis: ln(I) linear scale (or equivalently, I on a log scale), spanning approximately the range e⁻⁴ to e⁻²⁴. The straight line confirms the exponential law. Two or three filled data points near d = 5, 6, 7 Å at values consistent with the worked-example numbers (I₁ ~ 3.5×10⁻⁵, I₂ ~ 4.5×10⁻⁶, ratio ~7.8). A horizontal dashed marker at a reference current level showing the approximate current at d = 5 Å. The slope encodes 2κ; the data points represent the experimental benchmark. All values come directly from the chapter's worked example.

- `[O — ORGANIZATION]` Single panel. Horizontal axis left to right. Vertical axis (log scale) bottom to top. Straight line from upper left to lower right (exponential decay). Filled circles clustered in the middle distance range. Dashed horizontal reference line at one y-value. No annotations.

- `[P — PRESENTATION]` Flat vector. WKB theory line: Blue #0072B2, 2pt solid. Experimental data points: Orange #E69F00 filled circles, 4pt diameter. Reference dashed line: Sky Blue #56B4E9, 1pt dashed. Axis spines: neutral dark gray, 1pt (tick marks present but no numbers). White background. No baked text.

- `[E — EXCLUSIONS]` Omit: axis labels, numerical tick values, κ or φ annotations, equation text, Tersoff-Hamann prefactor curve, Fowler-Nordheim regime (large-bias region), image-charge correction curve, second curve for different work function, legend symbols.

---

**BLOCK 3 — NEGATIVE PROMPT**

axis labels, numerical values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 4 — CdSe Quantum Dot: Band-Gap Blueshift vs. Radius

**Heuristic:** PQ | **Rank:** Important

---

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a single-panel graph on a white background, no text. The horizontal axis runs left to right representing quantum-dot radius, decreasing from left (larger dots) to right (smaller dots) — or equivalently, placed conventionally with small radii at left. The vertical axis increases upward representing optical band-gap energy. Plot one smooth downward-opening curve (convex, approaching a horizontal asymptote at large radius — the bulk band gap) in flat blue. Mark four or five discrete filled circles in a contrasting flat color at positions corresponding to experimental data points (R ≈ 1.2, 1.5, 2.0, 3.0 nm from the chapter's CLAUDE.md experimental overlay). Draw a horizontal dashed line at the lower right of the graph representing the bulk band-gap value. No text, labels, or numbers anywhere.

---

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column, 89 mm wide, 300 DPI, SVG/EPS, white background.

- `[C — CONTENT]` The spherical-box prediction E_dot(R) = E_bulk + (ℏ²π²/2m*_e R²) + (ℏ²π²/2m*_h R²) − (1.8e²/4πε₀ε_r R) plotted for R from 1 to 6 nm with CdSe parameters (m*_e = 0.13 m_e, m*_h = 0.45 m_e, ε_r = 10.6, E_bulk = 1.74 eV). Four experimental points from the chapter: (R = 1.2 nm, E ≈ 2.9 eV), (R = 1.5 nm, E ≈ 2.44 eV), (R = 2.0 nm, E ≈ 2.1 eV), (R = 3.0 nm, E ≈ 1.9 eV). Horizontal dashed line at E = 1.74 eV (bulk gap). The theory curve overshoots the data points at small R (illustrating band-nonparabolicity breakdown noted in the chapter), but agrees well for R ≥ 2 nm. The overshoot is an explicitly stated result from the chapter's worked example.

- `[O — ORGANIZATION]` Single panel. Horizontal axis: R from 1 to 6 nm, left to right. Vertical axis: E from ~1.5 to ~4 eV, upward. Theory curve: smooth, falling steeply for small R and flattening near E_bulk. Experimental dots clustered in the R = 1–3 nm range. Bulk dashed line horizontal near the bottom.

- `[P — PRESENTATION]` Flat vector. Theory curve: Blue #0072B2, 2pt. Experimental data points: Orange #E69F00 filled circles, 4pt. Bulk gap dashed line: Bluish Green #009E73, 1.5pt dashed. Axis spines: neutral gray, 1pt (tick marks without numbers). White background. No baked text.

- `[E — EXCLUSIONS]` Omit: axis labels, numerical tick values, material-name annotations, Coulomb correction labeled separately, effective-mass correction curve, Hylleraas-level theory curve, temperature dependence, size-distribution broadening.

---

**BLOCK 3 — NEGATIVE PROMPT**

axis labels, numerical values, text annotations, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Figure 5 — Rutherford Angular Cross-Section: Born Approximation Polar Map

**Heuristic:** PQ | **Rank:** Important

---

**BLOCK 1 — ILLUSTRAE PASTE BLOCK**

Draw a polar diagram on a white background, no text. At the center place a small filled circle representing the scattering nucleus. Draw a set of concentric reference circles in light gray. Plot one closed polar curve whose radial distance from the center at each angle represents the differential cross-section dσ/dΩ on a logarithmic radial scale. The curve should be strongly peaked forward (small scattering angles, near the top of the diagram) and fall steeply toward the sides and backward, following the 1/sin⁴(θ/2) shape. Mark four or five discrete data points as small open squares or circles at specific angular positions, sitting on or very near the polar curve, representing the Geiger-Marsden experimental distribution. No text, numbers, or angle labels anywhere.

---

**BLOCK 2 — FULL SCOPE**

- `[S — SPECIFICATION]` Single-column, 89 mm wide, 300 DPI, SVG/EPS, white background. Polar diagram inscribed in an approximately 80 mm square.

- `[C — CONTENT]` The Rutherford Born cross-section dσ/dΩ = (Z₁Z₂e²/4E)² / sin⁴(θ/2) plotted in polar coordinates at E = 5.5 MeV, Z₁ = 2 (alpha), Z₂ = 79 (gold). Radial axis is logarithmic. θ = 0 (forward) points upward; θ = 180° (backscatter) points downward. The curve is computed for θ from 10° to 170° (avoiding the forward singularity). Five angular data points at θ ≈ 30°, 45°, 60°, 90°, 135°, corresponding to the Geiger-Marsden distribution shape, rendered as open circles sitting on the theory curve (agreement is near-exact per the chapter). Reference circles at one-decade intervals of cross-section. The 1/sin⁴ shape is the key visual claim; it is exact from the chapter's Born derivation.

- `[O — ORGANIZATION]` Polar coordinate system. Origin at diagram center. Forward direction (θ = 0) at top. Backward scattering (θ = 180°) at bottom. Radial scale logarithmic (4 decades shown). Light gray concentric reference circles at each decade. Theory polar curve in Blue. Experimental points as open circles in Orange. Small filled black circle at center (nucleus).

- `[P — PRESENTATION]` Flat vector. Theory polar curve: Blue #0072B2, 1.5pt. Experimental points: Orange #E69F00 open circles, 3pt stroke. Reference circles: light gray, 0.5pt. Nucleus marker: neutral black filled circle 3pt diameter. Background: white. No baked text.

- `[E — EXCLUSIONS]` Omit: incident beam arrow, scattering angle labels (θ = 30° etc.), cross-section axis labels, classical trajectory curves, nuclear-force deviation at high energy, partial-wave diagram, Debye screening annotation, legend.

---

**BLOCK 3 — NEGATIVE PROMPT**

angle labels, numerical values, legend text, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion

---

## Video Candidate Pass

| Figure | Verdict | Criterion (if VIDEO) | Reason |
|---|---|---|---|
| Fig 1 — Five-Move Process Flow | STATIC SUFFICIENT | — | A fixed sequential structure; the nodes and their order are the complete message. No time-evolution or transformation to show. |
| Fig 2 — Six Systems / Small Parameters | STATIC SUFFICIENT | — | A comparison panel comparing six static configurations; the visual argument is simultaneous and spatial, not temporal. |
| Fig 3 — WKB STM Current vs. Distance | STATIC SUFFICIENT | — | A static exponential curve; the slope is the message. No mechanism unfolds in time. |
| Fig 4 — QD Band-Gap vs. Radius | **VIDEO CANDIDATE** | Transformation below direct observation | Animating a dot shrinking in radius while the energy level rises shows the confinement mechanism causally — the 1/R² scaling is the learning target and motion makes the inverse relationship viscerally clear. |
| Fig 5 — Rutherford Polar Map | STATIC SUFFICIENT | — | The 1/sin⁴ shape is a static geometric fact; the polar curve conveys it completely in a single frame. |

**Recommended video: Figure 4.** Animate R decreasing from 6 nm to 1 nm over ~6 seconds: the sphere icon shrinks, the confinement energy bar rises, and the theory curve traces out left-to-right on the E vs. R plot. Overlay the experimental points appearing one by one as R passes through their values. This makes the 1/R² scaling — the chapter's quantitative prediction — a directly observable dynamic process rather than a static curve.
