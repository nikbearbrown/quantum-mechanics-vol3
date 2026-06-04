# CAJAL Figure Report — Chapter 1 — Time-Independent Perturbation Theory

Recommended: 5 figures, Mixed density.

---

## Figure 1 — Perturbation Series Structure: Power-Series Expansion of Energy and State

**Heuristic:** MC — Mechanism/Process | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical stack of three labeled rows representing successive orders of the perturbation expansion. The top row shows the zeroth-order tier: a single energy level and its corresponding state ket. The middle row shows the first-order tier: an energy correction represented as a single matrix-element block feeding into the level, and a state correction indicated by arrows from off-diagonal mixing terms. The bottom row shows the second-order tier: a sum-over-states structure with arrows flowing from multiple intermediate levels into the corrected energy and state. Connect the rows with downward arrows labeled with the power of lambda at each step. Show the normalization convention — correction kets orthogonal to the zeroth-order state — as a perpendicular symbol at the first-order state. The layout reads top-to-bottom as zeroth, first, second order. Use a staggered offset to make visible that the k-th order state feeds the (k+1)-th order energy.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three tiers: (0) unperturbed level E_n^(0) and ket |n^(0)>; (1) first-order energy correction E_n^(1) as a single expectation value block, first-order state correction |n^(1)> as a sum-over-m structure; (2) second-order energy correction E_n^(2) fed by |n^(1)>. Lambda power labels at each tier transition. Orthogonality constraint symbol on first-order state ket. Stagger indicator showing state-to-energy feed from tier k to tier k+1.
- `[O — ORGANIZATION]` Vertical progression, top to bottom, three horizontal bands. Connecting vertical arrows between bands labeled λ^0, λ^1, λ^2. Offset column showing the stagger: state at order k points diagonally to energy at order k+1. Flow direction: top → bottom (increasing order).
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Zeroth-order tier: Sky Blue `#56B4E9`. First-order tier: Bluish Green `#009E73`. Second-order tier: Orange `#E69F00`. Lambda arrows: Blue `#0072B2`. Stagger diagonal arrow: Reddish Purple `#CC79A7`. Orthogonality symbol: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit all orders beyond second. Omit divergence behavior (Dyson argument belongs in Figure 5). Omit degenerate case (Chapter 2). Omit specific examples (quartic oscillator handled in Figure 2). Omit intermediate algebra steps.

**BLOCK 3 — NEGATIVE PROMPT:**
convergent series spiral, infinite-order tower, 3D perspective stacking, degenerate subspace notation, numerical values, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — State Mixing Mechanism: Off-Diagonal Coupling and Small-Denominator Breakdown

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical energy axis with four discrete horizontal levels representing unperturbed eigenstates, evenly spaced except for one pair of nearly degenerate levels near the center. Label each level as a distinct state. From the central target level, draw bidirectional mixing arrows to each other level. Make the arrow thickness proportional to the mixing amplitude: thin arrows for levels far away (large denominator, small mixing), thick arrows for levels close in energy (small denominator, large mixing), and a very thick red-orange arrow connecting the near-degenerate pair to signal divergence. Place a visual indicator — a broken line or an X mark — on the near-degenerate mixing arrow to show the nondegenerate formula breaks down there. The diagram should read as: distant levels mix weakly, near levels mix strongly, degenerate levels cause breakdown.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Vertical energy axis with four discrete levels. Near-degenerate pair explicitly shown with small gap. Arrows representing mixing: thickness encoding |<m|H'|n>|/|E_n^(0) - E_m^(0)|. Breakdown indicator on the near-degenerate arrow. Small-gap label between near-degenerate pair. No specific numerical values.
- `[O — ORGANIZATION]` Vertical energy axis, levels as horizontal line segments. Mixing arrows are bilateral (symmetric), horizontal, connecting levels. Arrow thickness is the visual variable for mixing strength. Near-degenerate pair positioned at center. Breakdown marker (broken line through arrow) at the near-degenerate link.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Energy levels: Blue `#0072B2`. Weak-mixing arrows: light gray. Strong-mixing arrows: Orange `#E69F00`. Breakdown/divergence arrow: Vermillion `#D55E00`. Near-degenerate gap indicator: Reddish Purple `#CC79A7`. White background, no baked text.
- `[E — EXCLUSIONS]` Omit specific matrix element values. Omit the quartic oscillator context. Omit higher-order corrections. Omit the fix (degenerate PT) — that is Chapter 2. Omit continuum or infinite level stacks.

**BLOCK 3 — NEGATIVE PROMPT:**
smooth continuous spectrum, Feynman diagram style, orbital pictures, atom diagrams, wavefunction plots, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Quartic Oscillator Energy Levels: First-Order Correction Growth with Quantum Number

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a bar chart with quantum number n = 0, 1, 2, 3, 4 on the horizontal axis and the first-order energy correction E_n^(1) normalized to the level spacing on the vertical axis, starting at zero. For each n, draw two adjacent bars: one for the unperturbed energy E_n^(0) in natural units (n + 1/2) and one for the first-order correction (3/4)(2n^2 + 2n + 1) at lambda = 0.1. Show the correction bars growing quadratically relative to the unperturbed level spacing as n increases. Use a horizontal dashed reference line at the value where correction becomes comparable to the level spacing, to mark the breakdown threshold. The visual message: corrections grow as n^2, so perturbation theory becomes unreliable at higher n before it does for the ground state.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Five quantum numbers n = 0 through 4. For each: unperturbed energy bar and first-order correction bar, both in natural units (hbar = m = omega = 1) at lambda = 0.1. Correction values: E_n^(1) = (3*0.1/4)*(2n^2+2n+1). Unperturbed level spacing = 1. Horizontal dashed line marking correction ≈ level spacing (breakdown threshold). Y-axis from zero.
- `[O — ORGANIZATION]` Grouped bar chart, n on horizontal axis (0–4), energy correction magnitude on vertical axis (zero to ~3.2 at n=4). Unperturbed energy bars left, correction bars right within each group. Dashed threshold line at y = 1. Bars sorted left-to-right by increasing n.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Unperturbed energy bars: Sky Blue `#56B4E9`. First-order correction bars: Orange `#E69F00`. Threshold dashed line: Vermillion `#D55E00`. Axes and grid lines: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit second-order corrections. Omit exact numerical diagonalization results. Omit negative lambda (Dyson argument). Omit comparison curves (those belong in the simulation). Omit wavefunction depictions.

**BLOCK 3 — NEGATIVE PROMPT:**
line chart (use bars), wavefunction envelopes, potential well shape, orbital diagrams, 3D bar chart, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Second-Order Energy Correction Sign: Ground State vs. Excited States

**Heuristic:** VG — Verification Gap | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw two side-by-side panels on a shared vertical energy axis. Left panel: a vertical stack of levels with the lowest level highlighted as the ground state. Draw arrows pointing downward from each higher level into the ground state mixing sum, each contributing a negative quantity (all denominators negative for the ground state). Indicate the cumulative downward shift with a bold downward arrow and a minus symbol. Right panel: the same vertical stack with an intermediate excited state highlighted. Show arrows from levels above (contributing negative terms) and arrows from levels below (contributing positive terms), visually balanced or skewed depending on their proximity. Indicate that the net sign of the second-order correction for excited states is ambiguous. Juxtapose the ground state's guaranteed downward shift against the excited state's mixed contributions.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background. Two-panel layout.
- `[C — CONTENT]` Left panel: ground state level, all other levels above it, downward-pointing mixing arrows with negative sign indicators, net downward arrow for E^(2) < 0. Right panel: excited state level at intermediate height, levels above (negative contributions) and levels below (positive contributions), mixed arrows, no net arrow shown. Shared vertical energy axis between panels.
- `[O — ORGANIZATION]` Side-by-side panels (left: ground state case; right: excited state case). Shared vertical energy axis. Mixing arrows horizontal from each level toward the highlighted state. Net result arrow below each panel: bold downward for ground state, ambiguous bidirectional for excited. Panel separator: thin vertical gray line.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Ground state highlight: Bluish Green `#009E73`. Excited state highlight: Orange `#E69F00`. Negative-contribution arrows: Blue `#0072B2`. Positive-contribution arrows: Reddish Purple `#CC79A7`. Net result arrow: Sky Blue `#56B4E9`. Levels: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit specific formulas or numerical values. Omit the quartic oscillator context specifically. Omit higher orders. Omit the degenerate case. Omit any wavefunction or orbital diagrams.

**BLOCK 3 — NEGATIVE PROMPT:**
wavefunction plots, orbital diagrams, bar charts, Feynman diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Dyson Argument: Optimal Truncation of a Divergent Asymptotic Series

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a line plot with truncation order N on the horizontal axis (from 0 to ~15) and absolute error |E_N^PT - E_exact| on the vertical axis on a logarithmic scale starting at zero. Draw a single curve that decreases from left to right for low N (improving accuracy at each order), reaches a minimum at an optimal truncation order N*, then turns around and increases for higher N (divergence sets in). Mark N* with a vertical dashed line and annotate the minimum point with a dot. Draw a horizontal reference line at the error level at N*. The visual message: the error curve is U-shaped on a log scale, the minimum is the optimal truncation, and adding more terms past N* makes the answer worse. Include a second curve showing that increasing lambda shifts N* leftward, indicating the series breaks down at lower order for larger coupling.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Two curves: small lambda (lambda ~ 0.1) and larger lambda (lambda ~ 0.3), each showing error vs. truncation order N on log vertical axis. Both curves show initial decrease then upturn. Optimal truncation N* marked per curve. Horizontal reference line at minimum error. Y-axis from zero (log scale). X-axis: N from 0 to ~15.
- `[O — ORGANIZATION]` Single panel, N on horizontal axis, log |error| on vertical axis. Two curves. Vertical dashed lines at each N*. Horizontal dashed lines at the respective minima. Curves labeled by lambda value (inferred relation marker since exact values are schematic).
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Small-lambda curve: Bluish Green `#009E73`. Larger-lambda curve: Orange `#E69F00`. N* markers and reference lines: Vermillion `#D55E00`. Axes and grid: light gray. Minimum points: filled circles in respective curve colors. White background, no baked text.
- `[E — EXCLUSIONS]` Omit Borel summation or transseries details. Omit negative-lambda physics. Omit specific numerical coefficient values. Omit comparison to other methods (perturbation theory vs. variational). Omit QED context (fine-structure constant).

**BLOCK 3 — NEGATIVE PROMPT:**
divergent series as explosion graphic, Feynman diagram, complex plane contour, spiral representation, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Perturbation Series Structure:** STATIC SUFFICIENT. The hierarchy of tiers is a spatial layout problem, not a temporal one. The staggering of state-feeds-energy is legible in a static diagram.

**Figure 2 — State Mixing Mechanism:** STATIC SUFFICIENT. Arrow thickness encoding mixing strength is a static variable. The breakdown at near-degeneracy is a structural feature, not a process.

**Figure 3 — Quartic Oscillator Correction Growth:** STATIC SUFFICIENT. A bar chart comparison across n values is inherently static and read in a single pass.

**Figure 4 — Second-Order Sign:** STATIC SUFFICIENT. The ground-state vs. excited-state contrast is a comparison layout. No temporal sequence is required.

**Figure 5 — Optimal Truncation Curve:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The chapter's key claim — that adding more terms past N* makes the answer *worse* — is a dynamic process: as N increases, the curve descends, reaches a minimum, then turns and climbs. A video animating the partial sum error as N increments from 0 to ~15 (for two values of lambda) makes the turn-around moment visceral and directly defeats the misconception that "smaller terms always mean better convergence." The lambda-slider interaction (showing N* shift leftward as lambda grows) adds a second dimension that reinforces the message. Recommended video for Chapter 1.
