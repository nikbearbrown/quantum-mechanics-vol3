# CAJAL Figure Report — Chapter 6 — Radiation and Fermi's Golden Rule

Recommended: 6 figures, Mixed density.

---

## Figure 1 — From sinc-squared to delta function: the large-t limit

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a single panel showing three superimposed sinc-squared curves plotted as a function of detuning α = ω_fi − ω, with the vertical axis representing sin²(αt/2)/α² and starting at zero. The three curves correspond to three successive times t₁ < t₂ < t₃. As t increases, the central peak grows taller and narrows, while the area under the central peak increases linearly with t. The rightmost curve (t₃, largest) should be visually close to a spike — suggesting the delta function limit. Mark the area under the central peak for each curve with a shaded region, making the linear growth of area visible. The zero-crossing positions at ±2π/t should shift inward as t increases, indicating the narrowing width.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Horizontal axis: detuning α centered at zero, symmetric, range ±8π/t₁; vertical axis: function value starting at zero; three sinc-squared curves for t₁, t₂ = 2t₁, t₃ = 4t₁; peak heights growing as t², widths narrowing as 1/t; shaded area under each central peak in progressively deeper color showing area ∝ t; first-zero crossings at ±2π/t for each curve marked with small tick marks; side lobes of each curve visible; convergence toward a narrow spike (conceptual delta function) for t₃.
- `[O — ORGANIZATION]` Single chart. Horizontal axis symmetric about zero. Vertical axis from zero. Three curves overlaid. Shaded central-peak areas use graduated opacity. Zero-crossing ticks on horizontal axis at positions for each curve. Curves ordered by visual distinction (line weight or style).
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: t₁ curve Sky Blue `#56B4E9` 1 pt; t₂ curve Blue `#0072B2` 1.5 pt; t₃ curve Bluish Green `#009E73` 2 pt; shaded areas matching curve colors at 20%, 30%, 40% opacity respectively; first-zero tick marks Vermillion `#D55E00` 1 pt; axes gray 1 pt. Vertical axis starts at zero. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: density of states factor; golden rule rate derivation; spontaneous emission; Rabi oscillation; atomic level diagram; first-order PT parabola; mathematical derivation of the delta-function limit as formula.

**BLOCK 3 — NEGATIVE PROMPT:**

density of states curve, golden rule formula, atomic level diagram, Rabi oscillation, first-order PT parabola, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 2 — Density of states: counting k-space shells

**Heuristic:** MC — Mechanism/Process | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw two panels side by side. Left panel: a 2D slice of k-space showing a uniform grid of allowed k-points as dots, with a circular annular ring (shell) between radii k and k + dk highlighted in shading. The area of each unit cell (2π/L)² is indicated by a small square bracket around one dot. The shell area 2πk dk is implied by the highlighted ring. Right panel: a line graph showing the resulting density of states ρ(E) as a function of energy E, with the curve rising as √E for the 3D case. The vertical axis starts at zero. The curve should be smooth with no numerical values. The two panels together tell the counting story: grid in k-space → convert shell volume → divide by unit cell size → convert to energy.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Two panels side by side (50%/50% split).
- `[C — CONTENT]` Left panel: 2D k-space dot grid (uniform spacing representing (2π/L) lattice); concentric circles for k and k + dk; annular shell between them shaded; single unit cell square bracketed near one dot; implicit 3D interpretation (shell is spherical, 2D shown as slice). Right panel: ρ(E) vs. E curve as √E shape, smooth; vertical axis starting at zero; horizontal axis from zero. The √E shape emerging from the k-space counting procedure is the message.
- `[O — ORGANIZATION]` Two equal panels. Left: k_x horizontal, k_y vertical, grid of dots, annular shell shaded. Right: standard line chart, E horizontal, ρ(E) vertical from zero. No numerical values on axes.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: k-space dots Blue `#0072B2` filled circles 2 pt; annular shell fill Sky Blue `#56B4E9` at 40% opacity; shell boundary circles Blue `#0072B2` 1 pt; unit cell bracket Orange `#E69F00` 1 pt; ρ(E) curve Bluish Green `#009E73` 2 pt; ρ(E) axes gray 1 pt. Vertical axis starts at zero. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: photon density of states (separate concept); spin degeneracy factors; 1D or 2D density of states on same plot; Fermi golden rule formula; specific material parameters; Fermi energy or Fermi surface concepts.

**BLOCK 3 — NEGATIVE PROMPT:**

photon density of states curve on same panel, Fermi surface, Fermi energy marker, spin up/down labels, 1D/2D DOS overlaid, golden rule formula, Brillouin zone, band structure, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 3 — Selection rule derivation: parity and azimuthal integrals

**Heuristic:** MC — Mechanism/Process | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw two side-by-side schematic panels that represent the two symmetry arguments behind the electric-dipole selection rules. Left panel (parity argument for Δℓ = ±1): show a spherical harmonic lobe structure for ℓ = 0 (sphere), ℓ = 1 (dumbbell), and ℓ = 2 (four-lobed), with parity labels (even/odd/even) beneath each. Draw a small dumbbell-shaped operator z̃ between ℓ = 1 and ℓ = 0, indicating the matrix element is even × odd × even = even (nonzero integral), and between ℓ = 2 and ℓ = 0 showing odd parity (vanishes). Right panel (azimuthal integral for Δm): draw a horizontal axis for the azimuthal phase e^{imφ} for m = −1, 0, +1, +2, and show a circular phase-winding diagram for each m value. Indicate that the integral over φ from 0 to 2π of e^{i(m−m′+q)φ} is nonzero only when the net winding number is zero (m′ = m + q), and zero otherwise.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Two panels side by side (55%/45% split).
- `[C — CONTENT]` Left panel: three spherical-harmonic lobed silhouettes for ℓ = 0, 1, 2 arranged vertically; parity labels beneath (even, odd, even); dipole operator z silhouette (elongated oval) placed between ℓ = 1 and ℓ = 0 to show the allowed transition; crossed circle or inhibition marker between ℓ = 2 and ℓ = 0 to show the forbidden case; visual parity chain: (+1)(−1)(+1) = +1 → nonzero; (+1)(−1)(−1) = +1 (also nonzero? — show ℓ = 1 to 0 as allowed, ℓ = 0 to 0 or ℓ = 2 to 0 as forbidden). Right panel: four circular arrows showing azimuthal phase winding for m = −1, 0, +1, +2; one central arrow for q = 0 (z-polarized operator); visual sum of windings = 0 → nonzero integral; windings ≠ 0 → zero integral; allowed cases highlighted.
- `[O — ORGANIZATION]` Left panel: vertical arrangement of ℓ silhouettes with allowed/forbidden indicators between pairs. Right panel: circular winding arrows in a 2×2 arrangement. Clear visual separation between the two arguments.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: allowed transition indicators Bluish Green `#009E73` 1.5 pt; forbidden markers Vermillion `#D55E00` 1.5 pt (X symbols); ℓ = 0 silhouette Blue `#0072B2`; ℓ = 1 silhouette Sky Blue `#56B4E9`; ℓ = 2 silhouette Orange `#E69F00`; dipole operator silhouette Reddish Purple `#CC79A7`; azimuthal winding circles Blue `#0072B2` 1.5 pt; panel border light gray 0.5 pt. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: Gaunt coefficient algebra; Wigner 3j symbols; radial integral; specific quantum numbers of hydrogen; spin selection rules; Zeeman effect; magnetic dipole transitions; quadrupole transitions; detailed spherical harmonic formulas.

**BLOCK 3 — NEGATIVE PROMPT:**

Gaunt coefficient formula, Wigner 3j symbols, radial integral curve, hydrogen energy levels, Zeeman splitting, magnetic dipole, electric quadrupole, detailed spherical harmonic formulas baked in, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 4 — Hydrogen electric-dipole transition diagram: allowed and forbidden paths from n = 1,2,3

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a hydrogen energy level diagram with three rows of levels for n = 1, 2, and 3. Within each n, spread the ℓ substates horizontally: n = 1 shows 1s only; n = 2 shows 2s and 2p; n = 3 shows 3s, 3p, and 3d. Horizontal position of substates increases with ℓ (s at left, d at right), and vertical position represents energy. Draw solid arrows between levels that satisfy Δℓ = ±1 (allowed transitions): 2p → 1s, 3p → 1s, 3p → 2s, 3d → 2p. For forbidden transitions (2s → 1s with Δℓ = 0; 3s → 1s with Δℓ = 0; 3d → 1s with Δℓ = 2), draw dashed lines with a crossed-out marker or no line at all. Mark the 2s level with a distinct symbol indicating it is metastable (no E1 decay path to 1s).

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background.
- `[C — CONTENT]` Three rows (n = 1, 2, 3) with horizontal ℓ positions: 1s only at n = 1; 2s and 2p at n = 2; 3s, 3p, 3d at n = 3. Energy increases upward. Allowed E1 transitions (Δℓ = ±1): 2p→1s (solid arrow), 3p→1s (solid), 3p→2s (solid), 3d→2p (solid). No arrow for 2s→1s (Δℓ = 0, forbidden) or 3s→1s (Δℓ = 0) or 3d→1s (Δℓ = 2). 2s level marked with metastable indicator (e.g., star or filled circle). Relative vertical positions reflect the 13.6/n² energy spacing (not to scale but proportionally suggestive). Arrow thickness may vary to indicate relative transition rates qualitatively.
- `[O — ORGANIZATION]` Vertical energy axis (up = higher energy). Horizontal ℓ axis (left = s, right = d). Level bars as horizontal line segments. Arrows drawn diagonally between levels (since both n and ℓ change). Metastable marker on 2s. No forbidden transition arrows shown — their absence is the statement.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: level bars Blue `#0072B2` 2 pt; 2p→1s arrow Bluish Green `#009E73` 2 pt; 3p→1s arrow Bluish Green `#009E73` 1.5 pt; 3p→2s arrow Sky Blue `#56B4E9` 1.5 pt; 3d→2p arrow Sky Blue `#56B4E9` 1.5 pt; 2s metastable marker Orange `#E69F00` filled circle; all forbidden transitions omitted (no lines drawn); energy axis gray 1 pt; ℓ position axis gray 0.5 pt. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: magnetic quantum number m substates; spin-orbit fine structure; Lamb shift; two-photon decay path for 2s; hyperfine structure; 21-cm line; numerical energy values; spectroscopic notation baked in as text; photon polarization labels.

**BLOCK 3 — NEGATIVE PROMPT:**

m substate splitting, spin-orbit fine structure levels, Lamb shift arrow, two-photon 2s decay, hyperfine levels, 21-cm transition, numerical energy values baked in, spectroscopic notation text labels, photon polarization labels, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 5 — Einstein A/B ratio and the three emission/absorption processes

**Heuristic:** MC — Mechanism/Process | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a two-level energy diagram (lower state E₁ at bottom, upper state E₂ at top) repeated three times side by side in a triptych. In the first panel (absorption), draw an incoming photon symbol (wavy arrow) and a filled circle moving from E₁ upward to E₂, indicating population transfer upward. In the second panel (stimulated emission), draw an incoming photon symbol and two outgoing photon symbols (the stimulating photon plus the emitted copy), with the population moving from E₂ downward to E₁. In the third panel (spontaneous emission), draw no incoming photon, only a spontaneously emitted photon wavy arrow exiting in a random direction, with population moving from E₂ to E₁. Under each panel, indicate the rate expression schematically: panel 1 rate depends on field density u(ω); panel 2 rate depends on u(ω); panel 3 rate is independent of u(ω) — this contrast is the key message.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Three equal sub-panels in a horizontal triptych.
- `[C — CONTENT]` Panel 1 (absorption): two horizontal level bars; single incoming photon arrow from outside; population dot moving upward from E₁ to E₂; upward curved arrow for population. Panel 2 (stimulated emission): two level bars; one incoming photon arrow; two outgoing photon arrows (copied, coherent); population dot moving downward from E₂ to E₁. Panel 3 (spontaneous emission): two level bars; no incoming photon; single outgoing photon arrow in arbitrary direction; population dot moving E₂ to E₁. Under each panel: a schematic rate indicator — panels 1 and 2 show a field-density symbol (wave motif) indicating dependence on u(ω); panel 3 shows no field-density symbol, indicating field-independent rate. Panels 1 and 2 share the same B-coefficient visual weight; panel 3 has distinct A-coefficient indicator.
- `[O — ORGANIZATION]` Three equal horizontal panels separated by thin gray lines. Each panel: two horizontal level bars (E₁ bottom, E₂ top), population dot, photon arrows, rate indicator below. Consistent visual language across all three.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: level bars Blue `#0072B2` 2 pt; population dots Bluish Green `#009E73` filled circles; incoming photon arrows Orange `#E69F00` 1.5 pt wavy; outgoing photon arrows Vermillion `#D55E00` 1.5 pt wavy; population transition arrows Sky Blue `#56B4E9` 1.5 pt; spontaneous emission arrow Reddish Purple `#CC79A7` 1.5 pt; field-density indicator marks gray shading; panel borders light gray 0.5 pt. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: A/B ratio formula as text; Planck distribution; stimulated emission in laser cavity context; population inversion; NMR comparison; three or more energy levels; degeneracy factors; quantum electrodynamics vacuum fluctuation mechanism.

**BLOCK 3 — NEGATIVE PROMPT:**

A/B formula baked in, Planck distribution curve, laser cavity diagram, population inversion arrow, NMR apparatus, three or more energy levels, QED vacuum fluctuation, degeneracy factor notation, 3D rendering, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows (use single-headed arrows only for photon directionality), hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Figure 6 — Electric-dipole approximation: long-wavelength limit and its breakdown

**Heuristic:** VG — Verification Gap | **Rank:** Supplementary

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**

Draw a two-panel schematic. Left panel (valid dipole approximation): a small circle representing the hydrogen atom (size ∼ a₀) sitting inside a sinusoidal electromagnetic wave whose wavelength λ is visually much larger than the atom — the wave barely varies over the atomic extent. Indicate that the vector potential A(r,t) ≈ A(0,t) is approximately constant across the atom with a flat dashed horizontal line over the atom. Right panel (dipole approximation breaking down): the same atom but now with a much shorter-wavelength photon (hard X-ray) where λ ≈ a₀ — the wave varies significantly over the atomic extent, shown by the wave completing a full cycle across the atom. A visual indicator marks the transition threshold at photon energy ∼ 3.7 keV where ka₀ ∼ 1.

**BLOCK 2 — FULL SCOPE:**

- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector SVG/EPS, white background. Two equal sub-panels side by side.
- `[C — CONTENT]` Left panel: small circle (atom, radius a₀); sinusoidal wave in background with wavelength λ ≫ a₀ (many atom diameters per wavelength cycle); flat dashed line over the atom indicating A ≈ constant; ka₀ ≪ 1 condition implied. Right panel: same atom circle; sinusoidal wave with λ ≈ a₀ (wave completes roughly one cycle across the atom diameter); no flat approximation possible — wave varies substantially; ka₀ ∼ 1 condition implied. A transition marker or visual boundary arrow between the two panels indicating the scale shift.
- `[O — ORGANIZATION]` Two equal horizontal panels. Each: atom circle centered, wave drawn in background. Left panel uses long-wave sinusoidal; right panel uses short-wave sinusoidal. Atom circle same size in both panels. Wave drawn as a horizontal sinusoidal band behind/around the atom. Flat approximation line only in left panel.
- `[P — PRESENTATION]` Flat vector. Okabe-Ito: atom circle Blue `#0072B2` 2 pt outline; wave sinusoid in left panel Sky Blue `#56B4E9` 1 pt at low opacity; wave sinusoid in right panel Vermillion `#D55E00` 1 pt; flat approximation dashed line Orange `#E69F00` 1 pt dashed; transition boundary between panels gray 1 pt; panel borders light gray 0.5 pt. Uniform strokes. White background. No baked text.
- `[E — EXCLUSIONS]` Omit: A·p Hamiltonian formula; magnetic-dipole or quadrupole matrix elements; inner-shell electron details; numerical photon energy value; Compton scattering; X-ray absorption edge structure; specific element details.

**BLOCK 3 — NEGATIVE PROMPT:**

A·p Hamiltonian formula, magnetic dipole matrix element, electric quadrupole structure, inner-shell electron orbital details, Compton scattering, X-ray absorption edge, specific element symbols, numerical photon energy baked in, 3D atom model, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures.

---

## Video Candidate Pass

**Figure 1 — Sinc-squared sharpening into delta function:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages and transformation below direct observation. Animating the sinc-squared curve as t continuously increases — the peak growing, narrowing, side lobes compressing inward, area under the peak accumulating linearly — makes the emergence of the delta function from a concrete function viscerally comprehensible. The static three-curve overlay conveys the comparison but not the continuous process. **Recommended video for this chapter.**

**Figure 2 — Density of states counting:** STATIC SUFFICIENT. The k-space shell counting is a geometric argument that reads clearly as two-panel static; no temporal or causal sequence is the target.

**Figure 3 — Selection rules (parity and azimuthal):** STATIC SUFFICIENT. The two symmetry arguments are structural comparisons well suited to a static two-panel layout.

**Figure 4 — Hydrogen transition diagram:** STATIC SUFFICIENT. An energy level diagram is the canonical static figure; allowed/forbidden paths communicate in a glance.

**Figure 5 — Einstein A/B triptych:** STATIC SUFFICIENT. The three-process comparison is structurally a side-by-side static comparison; the visual contrast between field-dependent and field-independent rates is immediate in a still layout.

**Figure 6 — Electric-dipole approximation validity:** STATIC SUFFICIENT. The scale comparison (λ ≫ a₀ vs. λ ≈ a₀) is a spatial contrast readable as a static two-panel schematic.
