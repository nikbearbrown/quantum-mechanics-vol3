# Bear's Doodles — Quantum Mechanics, Vol. 3 Video Ideas

*Scouted from the 11 content chapters. Ordered by production value for short motion-first explainers.*

## Candidate 01 — Why a Tiny Perturbation Can Split One Level Into Many
- Source: `quantum-mechanics-vol3/chapters/02-degenerate-perturbation-theory-and-fine-structure.md`
- Production mode: Manim visualization
- Hook: Add a small field to identical-energy states and one energy line suddenly fans into several.
- Core idea: Degenerate perturbation theory first finds the good linear combinations inside the shared subspace, then the perturbation assigns each combination a different shift.
- Visual object: One thick energy line splitting into separate labeled levels as a field knob turns on.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: energy levels, perturbation as small change, superposition
- Exclusions: no matrix diagonalization arithmetic, no full fine-structure Hamiltonian, no hydrogen n=2 calculation
- Score: 9/10

## Candidate 02 — Why the Variational Principle Always Overshoots the Ground State
- Source: `quantum-mechanics-vol3/chapters/03-the-variational-principle.md`
- Production mode: Manim visualization
- Hook: Guess any normalized wavefunction you like, and its energy can land above the true ground state but never below it.
- Core idea: Every trial state is a weighted mixture of exact energy states, so its average energy is a weighted average that cannot beat the lowest term.
- Visual object: A trial blob decomposing into exact-state bars whose weighted average sits above the floor.
- Manim move: compare
- Short-form fit: Strong
- Prerequisites: average, energy levels, normalized state
- Exclusions: no helium variational arithmetic, no Rayleigh-Ritz matrices, no proof beyond weighted averages
- Score: 9/10

## Candidate 03 — Why Tunneling Rates Change by Orders of Magnitude
- Source: `quantum-mechanics-vol3/chapters/04-the-wkb-approximation-and-tunneling.md`
- Production mode: Manim visualization
- Hook: Make a barrier slightly wider or taller and a tunneling probability can collapse by a factor of millions.
- Core idea: WKB tunneling depends exponentially on the area under the forbidden momentum curve, so small geometric changes multiply the final probability.
- Visual object: A shaded forbidden-region area controlling a shrinking exponential tail and output probability.
- Manim move: decay
- Short-form fit: Strong
- Prerequisites: tunneling tail, exponential decay, area
- Exclusions: no connection-formula derivation, no alpha-decay half-life calculation, no Bohr-Sommerfeld quantization
- Score: 9/10

## Candidate 04 — Why a π-Pulse Flips an Atom
- Source: `quantum-mechanics-vol3/chapters/05-time-dependent-perturbation-theory-and-transitions.md`
- Production mode: Manim visualization
- Hook: Shine a resonant pulse for just the right time and a two-level atom flips almost completely.
- Core idea: The drive rotates the state on the Bloch sphere, and a pulse with area π moves the arrow from the ground pole to the excited pole.
- Visual object: A Bloch arrow rotating from south to north while pulse area fills to π.
- Manim move: rotate
- Short-form fit: Strong
- Prerequisites: two-level state, resonance, rotation
- Exclusions: no interaction-picture derivation, no sinc-squared perturbative line shape, no detuned Rabi formula
- Score: 8/10

## Candidate 05 — Why Selection Rules Are Not Arbitrary
- Source: `quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md`
- Production mode: Manim visualization
- Hook: An atom can jump between some energy levels but refuses others, as if light had a rulebook.
- Core idea: The dipole operator carries angular momentum and parity structure, so only initial and final orbitals with the right overlap produce a nonzero transition amplitude.
- Visual object: Orbital shapes overlapping through a dipole arrow, with allowed arrows lighting up and forbidden arrows fading.
- Manim move: scan
- Short-form fit: Medium
- Prerequisites: orbitals, transition, overlap
- Exclusions: no Wigner-Eckart theorem, no lifetime calculation, no Einstein coefficient derivation
- Score: 8/10

## Candidate 06 — Why a Laser Needs Matching Photons
- Source: `quantum-mechanics-vol3/chapters/06-radiation-and-fermis-golden-rule.md`
- Production mode: Mixed
- Hook: One photon passing an excited atom can persuade the atom to release a second photon that matches it.
- Core idea: Stimulated emission adds probability for a transition into an already occupied light mode, so the outgoing photon copies the incoming mode's frequency, phase, and direction.
- Visual object: One photon entering an excited atom and two matched photons leaving together.
- Manim move: duplicate
- Short-form fit: Strong
- Prerequisites: photons, excited state, energy transition
- Exclusions: no rate-equation laser threshold, no cavity engineering, no Einstein A/B coefficient algebra
- Score: 8/10

## Candidate 07 — Why Scattering Resonances Look Like Temporary Traps
- Source: `quantum-mechanics-vol3/chapters/07-scattering-i-partial-waves.md`
- Production mode: Manim visualization
- Hook: At special energies, a particle that should scatter quickly lingers as if the target briefly caught it.
- Core idea: A partial wave's phase shift races through π near a resonance, producing a large cross-section because the wave temporarily stores amplitude near the scatterer.
- Visual object: Incoming circular waves swelling around a target, then releasing outward.
- Manim move: slosh
- Short-form fit: Medium
- Prerequisites: scattering, wave phase, resonance
- Exclusions: no optical theorem derivation, no hard-sphere formulas, no full partial-wave expansion
- Score: 7/10

## Candidate 08 — Why a Crystal Opens a Band Gap
- Source: `quantum-mechanics-vol3/chapters/10-periodic-potentials-and-band-structure.md`
- Production mode: Manim visualization
- Hook: Electrons in a crystal can move freely at some energies, but whole ranges of energy are simply missing.
- Core idea: At Bragg conditions, right- and left-moving waves couple into standing waves with different charge placement, splitting one free-electron energy into two and opening a gap.
- Visual object: A free-electron parabola splitting at a zone boundary into two bands with a forbidden gap.
- Manim move: split
- Short-form fit: Strong
- Prerequisites: waves in a periodic lattice, energy graph, standing waves
- Exclusions: no Kronig-Penney algebra, no Bloch theorem proof, no tight-binding derivation
- Score: 9/10

## Candidate 09 — Why Magnetic Resonance Finds One Frequency
- Source: `quantum-mechanics-vol3/chapters/09-atoms-in-fields.md`
- Production mode: Manim visualization
- Hook: A spin ignores most radio waves, then suddenly tips when the frequency matches one exact energy gap.
- Core idea: A static magnetic field splits spin energies, and an oscillating field drives transitions only when its frequency matches that splitting.
- Visual object: Two spin energy levels separating as a magnetic field grows, then a radio wave matching the gap.
- Manim move: scan
- Short-form fit: Strong
- Prerequisites: spin up/down, energy gap, resonance
- Exclusions: no Bloch equations, no MRI engineering, no full Zeeman Hamiltonian
- Score: 8/10

## Candidate 10 — Why the Born Approximation Is a Shadow of the Potential
- Source: `quantum-mechanics-vol3/chapters/08-scattering-ii-the-born-approximation.md`
- Production mode: Manim visualization
- Hook: In weak scattering, the pattern on the detector is almost a Fourier shadow of the target.
- Core idea: The first Born approximation says the scattering amplitude is the Fourier transform of the potential, so target size and shape reappear as angular structure.
- Visual object: A potential shape transforming into a detector-ring pattern.
- Manim move: transform
- Short-form fit: Medium
- Prerequisites: scattering angle, wave interference, Fourier transform as pattern analyzer
- Exclusions: no Lippmann-Schwinger equation, no validity inequalities, no Yukawa integral
- Score: 7/10
