# CAJAL Figure Report — Chapter 5 — Time-Dependent Perturbation Theory and Transitions

Recommended: 5 figures, Mixed density.

---

## Figure 1 — The interaction picture: separating H₀ evolution from perturbation dynamics

**Heuristic:** MC — Mechanism/Process | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw two parallel horizontal timelines. The upper timeline represents the Schrödinger picture: a state vector that rotates rapidly with full Hamiltonian H₀ + H′(t), shown as a rapidly oscillating spiral or helix along the time axis. The lower timeline represents the interaction picture: a state vector that has the fast H₀ rotation removed, leaving only slow perturbation-driven changes — shown as a nearly flat trajectory with gentle wiggles. Connect the two timelines at t = 0 with a vertical equivalence marker to show they start identically. At an intermediate time, show the Schrödinger picture state as a rotating phasor while the interaction picture state moves slowly. Label the transformation between them as the unitary rotation operator e^{iH₀t/ℏ}. The visual contrast between fast rotation (upper) and slow drift (lower) is the key message.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Two horizontal timeline lanes; upper lane: Schrödinger picture state vector shown as a tightly oscillating helix or zigzag along the time axis; lower lane: interaction picture state shown as a slowly varying nearly flat trajectory; vertical connection at t = 0 (equivalence); unitary transformation arrow e^{iH₀t/ℏ} connecting the two lanes at a representative intermediate time; implicit H′(t) perturbation visible only in the lower lane (small wobbles); time axis shared between lanes.
- `[O — ORGANIZATION]` Horizontal dual-lane layout. Time increases left to right. Upper lane labeled "full precession" conceptually; lower lane labeled "perturbation only" conceptually. Both lanes occupy equal vertical space. Transformation arrow diagonal between lanes at mid-time. t = 0 vertical line at left edge.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: Schrödinger picture helix Blue `#0072B2` 1.5 pt; interaction picture trajectory Bluish Green `#009E73` 1.5 pt; transformation arrow Orange `#E69F00` 1 pt; t = 0 marker gray 1 pt dashed; lane divider light gray 0.5 pt dashed. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: specific matrix elements; operator expansion algebra; Dyson series; adiabatic theorem; many-level systems; second quantization; degenerate perturbation theory.

**BLOCK 3 — NEGATIVE PROMPT:**

operator algebra baked in, Dyson series diagrams, Feynman diagrams, second quantization notation, many-level level diagrams, 3D helix renderings, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 2 — Sinc-squared resonance lineshape as a function of detuning

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a line chart with detuning δ = ω_fi − ω on the horizontal axis (centered at zero, symmetric, ranging from about −5/t to +5/t in natural units) and first-order transition probability P on the vertical axis starting from zero. Plot the sinc-squared lineshape: a tall central peak at δ = 0, flanked by smaller side lobes of decreasing height. Show two versions of the curve superimposed: one for a shorter interaction time T₁ (broader central peak, lower maximum) and one for a longer time T₂ > T₁ (narrower central peak, higher maximum proportional to T²). Mark the first zeros of the sinc-squared at δ = ±2π/T with vertical tick marks. Show that the peak height grows as T² and the width shrinks as 1/T. Indicate the central peak area growing as T (linear in time).

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Horizontal axis: detuning δ from −5/T₂ to +5/T₂, centered at zero; vertical axis: probability P, starting at zero; two sinc-squared curves (T₁ and T₂, with T₂ > T₁); T₁ curve: broader, lower peak; T₂ curve: narrower, taller peak; first-zero markers at ±2π/T on both curves; side lobes visible on both curves; peak-height annotation comparing T₁² vs T₂² scaling; central area annotation showing linear-in-T growth; both curves symmetric about δ = 0.
- `[O — ORGANIZATION]` Standard line chart. Horizontal axis symmetric about zero detuning. Vertical axis from zero. Two curves overlaid with visual distinction. Zero-crossing tick marks on horizontal axis at symmetric positions. Optional bracket on T₂ curve indicating the central-peak width ∝ 1/T. No numerical axis values.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: T₁ curve Sky Blue `#56B4E9` 1.5 pt; T₂ curve Blue `#0072B2` 2 pt; zero-crossing ticks Vermillion `#D55E00` 1 pt; horizontal axis gray 1 pt; vertical axis gray 1 pt; axis starts at zero for vertical. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Rabi oscillation curves on this plot; counter-rotating terms; rotating wave approximation label; density-of-states factor; Fermi's golden rule delta function limit; exact Rabi formula; numerical frequency or time values.

**BLOCK 3 — NEGATIVE PROMPT:**

Rabi oscillation on this plot, density of states, Fermi golden rule delta function, exact Rabi formula curves, counter-rotating term diagram, numerical axis values baked in, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 3 — Rabi oscillation vs. first-order PT: exact vs. parabolic

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a line chart with the horizontal axis representing time in units of the Rabi period (Ωt, ranging from 0 to 3π) and the vertical axis representing transition probability P_g→e from 0 to 1.5 (extending above 1 to make the PT failure visible). Plot two curves: the exact Rabi formula sin²(Ωt/2) as a solid curve bounded between 0 and 1, oscillating with period 2π/Ω; and the first-order PT prediction (Ωt/2)² as a dashed parabola that matches the Rabi curve near t = 0 but diverges and crosses P = 1 before the first Rabi peak. Draw a horizontal dashed reference line at P = 1 labeled as the physical probability ceiling. Mark the π-pulse time t_π = π/Ω on the horizontal axis with a vertical tick. In the region where the PT parabola exceeds 1, shade or visually indicate the "PT breakdown" zone.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Horizontal axis Ωt from 0 to 3π; vertical axis P from 0 to 1.5; exact Rabi curve sin²(Ωt/2): solid, bounded 0–1, oscillates with full period 2π; first-order PT curve (Ωt/2)²: dashed parabola, agrees with Rabi at small Ωt, exceeds 1 and continues rising; P = 1 horizontal reference line dashed; π-pulse marker at Ωt = π; 2π marker (full Rabi cycle) at Ωt = 2π; early-time agreement zone (Ωt ≪ 1) indicated; PT breakdown region (above P = 1) lightly shaded; the moment of first crossing P = 1 by the PT curve marked.
- `[O — ORGANIZATION]` Standard line chart. x from 0, y from 0. Two curves overlaid. PT parabola continues beyond the P = 1 ceiling. P = 1 line drawn as horizontal dashed. π and 2π positions on x marked with vertical dashed lines. Shaded band above P = 1 for PT breakdown.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: exact Rabi curve Blue `#0072B2` 2 pt solid; PT parabola Vermillion `#D55E00` 1.5 pt dashed; P = 1 reference Orange `#E69F00` 1 pt dashed; PT breakdown zone above P = 1 Vermillion `#D55E00` at very low opacity; π and 2π vertical markers gray 1 pt dashed; axes gray 1 pt. Vertical axis starts at zero. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: off-resonance Rabi curves on this plot; detuning dependence; Bloch sphere representation; multi-level systems; sinc-squared lineshape; density of states; spontaneous emission damping.

**BLOCK 3 — NEGATIVE PROMPT:**

off-resonance Rabi curves, Bloch sphere, detuning variation, multi-level energy diagram, sinc-squared lineshape, spontaneous emission damping envelope, density of states, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 4 — Off-resonance Rabi: detuning suppresses and accelerates oscillation

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a single line chart panel showing three exact Rabi oscillation curves for three values of detuning: Δ = 0 (on resonance), Δ = Ω (moderate detuning), and Δ = 2Ω (large detuning). The horizontal axis is time; the vertical axis is P_g→e from 0 to 1. The on-resonance curve reaches P = 1 at the π-pulse and oscillates fully. The moderate-detuning curve oscillates faster but reaches only P_max = Ω²/(Ω² + Δ²) < 1 with a reduced ceiling. The large-detuning curve oscillates fastest but has the lowest maximum probability. Use different line styles to distinguish the three curves. The visual message: increasing detuning shrinks the amplitude and increases the frequency of the Rabi oscillation.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Horizontal axis: time (0 to ~4π/Ω); vertical axis: P_g→e from 0 to 1; three Rabi curves: Δ = 0 (reaches P = 1, period 2π/Ω), Δ = Ω (reaches P_max = 0.5, period π/Ω_gen = π/√2Ω), Δ = 2Ω (reaches P_max = 0.2, faster oscillation); maximum probability ceiling for each curve indicated with horizontal reference mark; generalized Rabi frequency Ω_gen = √(Ω² + Δ²) concept represented visually by decreasing oscillation period with increasing Δ.
- `[O — ORGANIZATION]` Standard line chart. Three curves overlaid. Horizontal reference dashed lines at each curve's maximum probability. No numerical values on axes. Tick marks only. Curves ordered by color distinction. The Δ = 0 curve spans the full P = 0 to 1 range; others lie strictly below.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: Δ = 0 curve Blue `#0072B2` 2 pt solid; Δ = Ω curve Bluish Green `#009E73` 1.5 pt dashed; Δ = 2Ω curve Orange `#E69F00` 1.5 pt dash-dot; ceiling reference lines matching each curve color at 0.5 pt; axes gray 1 pt. Vertical axis starts at zero. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: first-order PT parabola on this figure; sinc-squared lineshape; Bloch sphere; counter-rotating terms; rotating wave approximation derivation; numerical detuning values; spontaneous emission.

**BLOCK 3 — NEGATIVE PROMPT:**

first-order PT parabola, Bloch sphere, sinc-squared lineshape, counter-rotating term, spontaneous emission envelope, numerical detuning values baked in, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 5 — Continuum limit: coherent Rabi oscillations collapsing into linear golden-rule growth

**Heuristic:** MC — Mechanism/Process | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a three-panel vertical sequence. Each panel shares the same horizontal axis (time) and vertical axis (total transition probability P_total) from 0 to 1. Panel 1 (top): N = 2 discrete final states — P_total shows clear Rabi-like coherent oscillation between 0 and a maximum. Panel 2 (middle): N = 10 discrete final states — oscillation partially averaged, some structure remains but a linear trend emerges. Panel 3 (bottom): N = 50 discrete states in a quasi-continuum — the oscillations have averaged away and P_total rises linearly with time, matching a dashed orange Fermi golden-rule reference line W·t. The visual narrative is the evolution from coherent oscillation to irreversible linear decay as the density of final states increases.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Three vertically stacked equal-height panels sharing the same x-axis scale.
- `[C — CONTENT]` Three panels stacked: top (N = 2), middle (N = 10), bottom (N = 50); each with: horizontal time axis (shared scale, 0 to ~8 × 2π/Δ_band), vertical P_total from 0 to 1; N = 2 panel: clear oscillatory P_total (solid black curve); N = 10 panel: partially washed-out oscillations with emerging linear trend; N = 50 panel: smooth near-linear rise matching the dashed orange W·t prediction; Fermi golden-rule line W·t in bottom (and optionally middle) panel as dashed orange reference; brief transient at early time in bottom panel before linear regime. Visual narrative: oscillation → smoothing → linear irreversible decay.
- `[O — ORGANIZATION]` Three horizontally aligned panels, vertically stacked, shared x-axis (labeled only on bottom panel). Each panel has its own y-axis 0 to 1. Curves in solid black; Fermi reference in dashed orange. N indicated by visual density variation (not text).
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: P_total curves Blue `#0072B2` 1.5 pt solid; Fermi W·t reference Orange `#E69F00` 1.5 pt dashed; axes gray 1 pt; panel borders light gray 0.5 pt. Vertical axes start at zero. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: sinc-squared lineshape details; individual final-state energy levels shown; Rabi formula curves; first-order PT parabola; density-of-states formula derivation; spontaneous emission; atomic level diagrams.

**BLOCK 3 — NEGATIVE PROMPT:**

individual final-state level diagram, density of states derivation, Rabi formula on this figure, PT parabola, sinc-squared peak, spontaneous emission envelope, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Video Candidate Pass

**Figure 1 — Interaction picture (two timelines):** STATIC SUFFICIENT. The contrast between fast and slow evolution is a spatial comparison that reads clearly as a static side-by-side; no causal temporal sequence is the target.

**Figure 2 — Sinc-squared lineshape:** STATIC SUFFICIENT. The sharpening of the peak with time is shown by overlaying two static curves; the comparison is clearer without animation.

**Figure 3 — Rabi oscillation vs. PT parabola:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages. The unfolding has a clear narrative arc — (1) agreement at small Ωt, (2) divergence as PT predicts P > 1, (3) Rabi curve returning to zero while PT continues rising. Animating the two curves growing simultaneously as Ωt increases — with a marker sweeping along the time axis — makes the moment of PT breakdown viscerally tangible: the student watches the PT curve pass through P = 1 while the exact curve turns back. **Recommended video for this chapter.**

**Figure 4 — Off-resonance Rabi curves:** STATIC SUFFICIENT. The three-curve overlay communicates the detuning dependence as a comparison, which is best read statically.

**Figure 5 — Coherent oscillation to linear golden-rule growth:** STATIC SUFFICIENT. The three-panel sequence communicates the N → ∞ collapse effectively as a static vertical stack; the reader's eye moves top to bottom in the natural reading direction.
