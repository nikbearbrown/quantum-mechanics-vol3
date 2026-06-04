# CAJAL Figure Report — Chapter 2 — Degenerate Perturbation Theory and Fine Structure

Recommended: 6 figures, Mixed density.

---

## Figure 1 — Degenerate Subspace Geometry: Good States as Eigenvectors of W

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a two-dimensional plane representing the degenerate subspace of Hilbert space. Show the plane as a flat parallelogram in isometric view with two orthogonal basis vectors representing the original degenerate states |a> and |b>. Overlay a second pair of axes rotated within the plane to represent the good zeroth-order states — the eigenvectors of the perturbation matrix W. Show the perturbation operator as an ellipse inscribed in the plane, with its major and minor axes aligned with the good-state axes, indicating that W is anisotropic in the subspace — it picks preferred directions. Connect the original basis vectors to the good-state vectors with a rotation arc. Outside the plane, show the full Hamiltonian H' as an arrow entering the plane from above, breaking its isotropy. The diagram makes visible that H_0 is isotropic in the plane (any combination is valid) while H' picks specific axes.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Degenerate subspace as a 2D plane (isometric projection). Original basis {|a>, |b>} as orthogonal vectors. Rotated good-state axes {|+>, |->} as eigenvectors of W. Ellipse representing W's anisotropy with major/minor axes on good-state directions. Rotation arc between original and good-state bases. H' arrow entering from outside the plane. Inferred relation: rotation angle determined by the perturbation matrix (labeled as inferred).
- `[O — ORGANIZATION]` Single-panel isometric view. Plane occupies central region. Original basis vectors in one color, good-state vectors in another. W-ellipse centered at origin of plane. H' arrow approaches from upper-left outside plane. Rotation arc at plane origin between the two pairs of vectors.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Plane fill: light gray. Original basis vectors: Sky Blue `#56B4E9`. Good-state eigenvectors: Bluish Green `#009E73`. W anisotropy ellipse: Orange `#E69F00`. Rotation arc: Reddish Purple `#CC79A7`. H' arrow from outside: Blue `#0072B2`. White background, no baked text.
- `[E — EXCLUSIONS]` Omit higher-dimensional degenerate subspaces. Omit the specific Stark-effect states. Omit matrix algebra notation. Omit any reference to specific quantum numbers (n, l, m). Omit the full Hilbert space context outside the plane.

**BLOCK 3 — NEGATIVE PROMPT:**
3D orbital shapes, wavefunction plots, matrix grid, Bloch sphere, quantum circuit gates, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 2 — Degenerate PT Procedure: Four-Step Flowchart

**Heuristic:** MC — Mechanism/Process | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a vertical four-step flowchart. Step 1: Identify the degenerate subspace — a box showing multiple states at the same energy on a small level diagram. Step 2: Build the perturbation matrix W — a box showing a grid of matrix elements W_ij restricted to the degenerate subspace, with off-diagonal entries highlighted. Step 3: Diagonalize W — a box showing the transformation from W to a diagonal matrix, with a diagonal arrow indicating the diagonalization operation. Step 4: Read off results — a box splitting into two outputs: eigenvalues as first-order energy corrections E_n^(1), and eigenvectors as good zeroth-order states. Connect the steps with downward flow arrows. The four-step structure must be visually distinct and sequentially numbered.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Four process boxes: (1) degenerate subspace identification with a small energy-level diagram showing coincident levels; (2) W matrix construction with highlighted off-diagonal blocks; (3) diagonalization operation shown as a matrix transformation; (4) output fork into energy corrections and good-state eigenvectors. Three flow arrows between boxes. Output fork arrow from box 4.
- `[O — ORGANIZATION]` Vertical linear flowchart, top to bottom. Boxes aligned on a central vertical axis. Each box approximately equal height. Output fork at bottom splits to two terminal symbols. Step numbers as distinct visual elements inside each box (not text labels — use shape or position coding). Flow arrows: downward between boxes, branching at final step.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Step 1 box: Sky Blue `#56B4E9`. Step 2 box: Blue `#0072B2`. Step 3 box: Orange `#E69F00`. Step 4 box: Bluish Green `#009E73`. Flow arrows: Blue `#0072B2`. Output fork arrows: Reddish Purple `#CC79A7`. Matrix highlight cells: Orange `#E69F00`. White background, no baked text.
- `[E — EXCLUSIONS]` Omit the nondegenerate PT procedure. Omit the Stark matrix specifically. Omit the fine-structure example. Omit mathematical notation. Omit any boxes beyond the four steps.

**BLOCK 3 — NEGATIVE PROMPT:**
decision diamond, loop-back arrows, circular flow, matrix numerical entries, orbital diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 3 — Stark Effect: 4×4 W Matrix Sparsity Pattern and Block Structure

**Heuristic:** VG — Verification Gap | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a 4×4 matrix grid with rows and columns representing the four hydrogen n=2 states ordered as |2s>, |2p_0>, |2p_{+1}>, |2p_{-1}>. Fill each cell with a visual indicator: an empty circle for a zero entry killed by a selection rule, and a filled circle for the single surviving nonzero off-diagonal entry (the |2s>–|2p_0> matrix element). Indicate which selection rule killed each zero entry by using two distinct empty-circle styles: one for the parity rule, one for the delta-m_l rule. Show the block structure explicitly by drawing a thin line separating the upper-left 2×2 block from the lower-right 2×2 block. The visual message: out of 16 entries, 15 are zero by symmetry, and only one requires actual integration.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` 4×4 grid with rows/columns: |2s>, |2p_0>, |2p_{+1}>, |2p_{-1}>. Filled marker at (2s, 2p_0) and (2p_0, 2s) positions — the two conjugate nonzero entries. Empty markers (two styles) for entries killed by parity vs. those killed by delta-m_l = 0. All diagonal entries empty (parity kills them). Block-structure divider line separating 2×2 upper-left from 2×2 lower-right. Lower-right block is entirely empty circles.
- `[O — ORGANIZATION]` Square grid centered on canvas. Row and column positions equidistant. Filled marker at positions (1,2) and (2,1) (1-indexed). Block divider as a slightly heavier line after row/column 2. Two empty-marker shapes: open circle for parity kills, open diamond for delta-m_l kills.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Filled (nonzero) markers: Orange `#E69F00`. Parity-killed empty circles: Sky Blue `#56B4E9`. Delta-m_l-killed empty diamonds: Reddish Purple `#CC79A7`. Block divider line: Blue `#0072B2`. Grid lines: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit numerical values of matrix elements. Omit eigenvectors of W. Omit any reference to the resulting energy levels. Omit the Hamiltonian H_0. Omit higher-n manifolds. Omit the magnetic field (Zeeman) case.

**BLOCK 3 — NEGATIVE PROMPT:**
heat map coloring, gradient cells, orbital shape overlays, wavefunction plots, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 4 — Linear Stark Effect: Level Splitting of the n=2 Manifold

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Critical

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw an energy level diagram with two columns. Left column: a single horizontal line representing the fourfold-degenerate unperturbed n=2 level. Right column (with electric field applied): three horizontal levels. The top level sits above the unperturbed energy by a shift of +3a_0 e E_field; draw it higher than the center. The bottom level sits below by the same amount -3a_0 e E_field. The middle level remains at the unperturbed energy and is drawn as a doubled line (or widened bar) to indicate twofold degeneracy. Connect each right-column level to the left-column level with horizontal lines that fan out. Indicate the asymmetric charge-cloud physics of the two shifted good states: the higher level corresponds to electron density shifted against the field, the lower to density shifted along the field. Show the linear dependence on E_field by including a small inset axis schematic showing the splitting growing linearly with field strength.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Left column: one horizontal line at E_2^(0) representing all four degenerate states. Right column: three lines — upper at +3a_0 e E_field, middle (doubled line) at 0, lower at -3a_0 e E_field relative to E_2^(0). Fanning connection lines. Bracket indicating the symmetric splitting ±3a_0 e E_field. Small inset: splitting magnitude vs. field strength as a linear-slope indicator (schematic). Twofold degeneracy marker on the middle level.
- `[O — ORGANIZATION]` Two-column layout, left (unperturbed) to right (perturbed), with a horizontal field-application arrow between columns. Three fanning lines from left level to right levels. Symmetric bracket on right column showing equal up/down shifts. Small inset panel (lower-right corner) showing linear E_field dependence as a rising straight line from origin.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Unperturbed level: Blue `#0072B2`. Upper shifted level: Bluish Green `#009E73`. Doubly degenerate middle level: Sky Blue `#56B4E9`. Lower shifted level: Orange `#E69F00`. Fanning connection lines: light gray. Symmetric bracket: Reddish Purple `#CC79A7`. Inset axis and slope line: Blue `#0072B2`. White background, no baked text.
- `[E — EXCLUSIONS]` Omit higher-n Stark effects. Omit the quadratic Stark effect (ground state). Omit magnetic field effects. Omit fine structure. Omit any orbital shape diagrams. Omit numerical field-strength values.

**BLOCK 3 — NEGATIVE PROMPT:**
orbital shape diagrams, wavefunction density plots, 3D field line drawings, Feynman diagrams, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 5 — Hydrogen Fine Structure: Three Perturbations and Their Coverage by Quantum State Type

**Heuristic:** VG — Verification Gap | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-row by two-column grid. Each row represents one of the three fine-structure perturbations: relativistic kinetic correction, spin-orbit coupling, and Darwin term. Left column: a small icon representing the physical origin of each perturbation — a momentum-squared symbol shape for relativistic kinetic, an angular momentum plus spin interlocking arrows for spin-orbit, and a smeared-dot symbol for the Darwin Zitterbewegung. Right column: a state-type coverage indicator showing which quantum states are affected. Use a bar or filled/unfilled strip: for relativistic kinetic — all states affected (full bar); for spin-orbit — only l ≠ 0 states affected (partial bar, l=0 end empty); for Darwin — only l=0 states affected (partial bar, l≠0 end empty). The complementarity of spin-orbit (vanishes at l=0) and Darwin (only nonzero at l=0) should be visually obvious.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three perturbations: (1) relativistic kinetic — affects all l; (2) spin-orbit — affects l ≠ 0 only, vanishes at l=0; (3) Darwin — affects l=0 only, vanishes at l ≠ 0. Coverage bars per perturbation: relativistic = full; spin-orbit = partial (l≠0 region filled, l=0 region empty); Darwin = partial (l=0 region filled, l≠0 region empty). Physical-origin icons: momentum-shape, angular-momentum-spin-coupling arrows, smear-dot. Complementarity of spin-orbit and Darwin visible as mirror-image coverage patterns.
- `[O — ORGANIZATION]` Three-row grid, each row one perturbation. Left column: physical-origin icon. Right column: coverage bar spanning l=0 to l≠0 state types. Coverage bars aligned horizontally for direct comparison. Rows separated by thin gray lines.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Relativistic kinetic row: Blue `#0072B2` filled bar. Spin-orbit row: Orange `#E69F00` partial bar (l≠0 filled), light gray (l=0 empty). Darwin row: Reddish Purple `#CC79A7` partial bar (l=0 filled), light gray (l≠0 empty). Icons in corresponding row colors. Row separators: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit the combined fine-structure formula. Omit the Lamb shift. Omit the Thomas factor derivation. Omit j quantum numbers. Omit numerical magnitudes. Omit the Stark effect.

**BLOCK 3 — NEGATIVE PROMPT:**
orbital diagram, hydrogen atom cross-section, Feynman diagram, magnetic field lines, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Figure 6 — Hydrogen n=2 Energy Hierarchy: Bohr, Fine Structure, Lamb Shift

**Heuristic:** PQ — Proportional/Quantitative | **Rank:** Important

**BLOCK 1 — ILLUSTRAE PASTE BLOCK:**
Draw a three-tier energy level diagram on a shared vertical axis using a logarithmic spacing to accommodate the three orders of magnitude. Tier 1 (leftmost, widest): a single level at E_2^(0) = -3.4 eV, labeled as the Bohr/Coulomb result. Tier 2 (center): two levels showing the fine-structure splitting of ~4.5 × 10^{-5} eV, with the j=3/2 level above the j=1/2 level. Show the j=1/2 level as a single line (representing both 2s_{1/2} and 2p_{1/2} as degenerate). Connect tier 1 levels to tier 2 levels with fanning lines. Tier 3 (rightmost): the j=1/2 level from tier 2 splits into 2s_{1/2} above and 2p_{1/2} below, separated by the Lamb shift ~4 × 10^{-6} eV. A vertical double-headed bracket on the right side quantifies the three scales. Use a scale break to accommodate the large ratio between tiers.

**BLOCK 2 — FULL SCOPE:**
- `[S — SPECIFICATION]` Single column, 89 mm width, 300 DPI, vector (SVG/EPS), white background.
- `[C — CONTENT]` Three-tier diagram. Tier 1: single degenerate n=2 level at -3.4 eV. Tier 2: two levels — j=3/2 (2p_{3/2}) above, j=1/2 (2s_{1/2}/2p_{1/2} degenerate) below; separation ~4.5×10^{-5} eV. Tier 3: j=1/2 level splits into 2s_{1/2} above and 2p_{1/2} below; separation ~4×10^{-6} eV. Magnification breaks between tiers with scale indicators. Vertical bracketed labels indicating each energy scale. Fanning connection lines between tiers. The Lamb shift tier carries a distinct visual marker indicating it requires QED.
- `[O — ORGANIZATION]` Left-to-right tier progression representing increasing resolution. Vertical axis represents energy. Scale break markers (zigzag or gap) between tiers 1–2 and 2–3. Magnification factor indicators at each break. Tier 3 offset to the right of tier 2. Vertical bracket annotations for each energy gap on the right edge.
- `[P — PRESENTATION]` Flat vector, Okabe-Ito palette, 1pt strokes. Bohr level (tier 1): Blue `#0072B2`. Fine-structure levels (tier 2): j=3/2 in Sky Blue `#56B4E9`, j=1/2 in Orange `#E69F00`. Lamb-shift levels (tier 3): 2s_{1/2} in Bluish Green `#009E73`, 2p_{1/2} in Reddish Purple `#CC79A7`. QED marker on tier 3 boundary: Vermillion `#D55E00` dashed separator. Fanning lines: light gray. White background, no baked text.
- `[E — EXCLUSIONS]` Omit hyperfine structure. Omit Zeeman effect. Omit n ≠ 2 levels. Omit the Stark effect. Omit the detailed QED mechanism for the Lamb shift. Omit n=1 ground-state energy.

**BLOCK 3 — NEGATIVE PROMPT:**
spectral emission lines, photon arrows, orbital diagrams, Bohr radius circular orbits, text labels, words, gibberish letters, titles, captions, decorative borders, realistic textures, drop shadows, gradient backgrounds, photographic elements, dual-headed arrows, hand-drawn styles, human figures, visual clutter, watermarks, red-green color combinations, rainbow color scales, 3D perspective distortion.

---

## Video Candidate Pass

**Figure 1 — Degenerate Subspace Geometry:** STATIC SUFFICIENT. The plane, basis vectors, and eigenvector axes are a spatial layout; the rotation between bases is a structural relationship, not a temporal sequence.

**Figure 2 — Degenerate PT Procedure:** VIDEO CANDIDATE. Criterion: ≥3 sequential causal stages. The four-step procedure has strict causal order: you cannot diagonalize before building W, cannot read off good states before diagonalizing. Animating the flowchart box by box — with each step revealed and connected to the next — would make the procedural logic viscerally clear. However, the Static figure is likely sufficient because the flowchart communicates sequence visually. STATIC SUFFICIENT on balance; the sequence is self-evident.

**Figure 3 — Stark Matrix Sparsity:** STATIC SUFFICIENT. A matrix is read in a single pass; the sparsity pattern is a structural fact, not a process.

**Figure 4 — Linear Stark Splitting:** VIDEO CANDIDATE. Criterion: transition mechanism is the learning target. The chapter's key demonstration — four degenerate states splitting into three distinct energies as the electric field is turned on — is intrinsically dynamic. An animation where the field strength E_field grows from zero and the right-column levels fan out from a single degenerate line to three distinct levels (with the W matrix entries growing simultaneously) directly embodies the mechanism. The Stark-tab simulation already exists for this, but a short dedicated video animation of just the level-fanning (without interactive controls) would be the most pedagogically powerful single visual. Recommended video for Chapter 2.

**Figure 5 — Three Perturbations Coverage:** STATIC SUFFICIENT. The complementarity of spin-orbit and Darwin is a structural comparison, legible as a side-by-side static chart.

**Figure 6 — Energy Hierarchy:** STATIC SUFFICIENT. The three-tier magnification diagram is a static spatial layout communicating scale ratios through position and bracket annotations.
