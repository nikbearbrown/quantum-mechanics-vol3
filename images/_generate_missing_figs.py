"""
Generate 9 missing figures for quantum-mechanics-vol3.
Run from the images/ directory:
    cd .../quantum-mechanics-vol3/images && python3 _generate_missing_figs.py
House style: figsize=(7,3.6), dpi=200, white bg, top/right spines off,
             mathtext labels, descriptive title at top.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.patches import FancyArrowPatch, FancyArrow
import warnings
warnings.filterwarnings('ignore')

FIGSIZE = (7, 3.6)
DPI = 200
TAB = plt.rcParams['axes.prop_cycle'].by_key()['color']  # tab10 colors

def clean_ax(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

# ─────────────────────────────────────────────────────────────────────────────
# Fig 2.1 — Degenerate subspace geometry: plane with |a⟩,|b⟩ basis and W eigenvectors
# ─────────────────────────────────────────────────────────────────────────────
def fig_02_01():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    ax.set_aspect('equal')
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.8)
    ax.axis('off')
    fig.patch.set_facecolor('white')

    # Draw the "plane" as a light parallelogram
    plane_pts = np.array([[-1.4, -0.9], [1.4, -0.9], [1.2, 1.1], [-1.2, 1.1], [-1.4, -0.9]])
    ax.fill(plane_pts[:, 0], plane_pts[:, 1], color='#e8eef7', zorder=0)
    ax.plot(plane_pts[:, 0], plane_pts[:, 1], color='#aabbdd', lw=1.2, zorder=1)
    ax.text(1.05, 1.0, 'degenerate\nsubspace', color='#5566aa', fontsize=8, ha='right')

    # Original basis vectors |a⟩ and |b⟩ (non-orthogonal, for visual interest)
    origin = np.array([0.0, 0.0])
    a_vec = np.array([1.0, 0.0])
    b_vec = np.array([0.3, 0.9])

    def draw_arrow(ax, start, end, color, lw=1.8, zorder=3):
        ax.annotate('', xy=end, xytext=start,
                    arrowprops=dict(arrowstyle='->', color=color, lw=lw),
                    zorder=zorder)

    draw_arrow(ax, origin, a_vec, TAB[0])
    draw_arrow(ax, origin, b_vec, TAB[0])
    ax.text(a_vec[0]+0.08, a_vec[1]+0.02, r'$|a\rangle$', color=TAB[0], fontsize=12, ha='left')
    ax.text(b_vec[0]+0.07, b_vec[1]+0.04, r'$|b\rangle$', color=TAB[0], fontsize=12)

    # Good states: eigenvectors of W (at ±45° from the a-axis for a symmetric 2x2 off-diagonal W)
    # For W = [[0, w],[w, 0]], eigenvectors are (a±b)/√2
    g1 = (a_vec + b_vec) / np.linalg.norm(a_vec + b_vec) * 1.1
    g2 = (a_vec - b_vec) / np.linalg.norm(a_vec - b_vec) * 1.1

    draw_arrow(ax, origin, g1, TAB[1], lw=2.2)
    draw_arrow(ax, origin, g2, TAB[1], lw=2.2)
    ax.text(g1[0]+0.07, g1[1]+0.05,
            r'$\frac{|a\rangle+|b\rangle}{\sqrt{2}}$', color=TAB[1], fontsize=11)
    ax.text(g2[0]+0.08, g2[1]-0.13,
            r'$\frac{|a\rangle-|b\rangle}{\sqrt{2}}$', color=TAB[1], fontsize=11)

    # Label W as acting to select direction
    ax.annotate('', xy=(0.55, 0.42), xytext=(0.15, 0.1),
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1.4, linestyle='dashed'))
    ax.text(0.18, 0.28, r'$W$ selects', color=TAB[2], fontsize=9, style='italic')
    ax.text(0.18, 0.15, r'preferred axis', color=TAB[2], fontsize=9, style='italic')

    # Origin dot
    ax.plot(*origin, 'ko', ms=4, zorder=5)

    legend_handles = [
        mlines.Line2D([], [], color=TAB[0], lw=2, label=r'original basis ($\hat{H}_0$ indifferent)'),
        mlines.Line2D([], [], color=TAB[1], lw=2, label=r'good states (eigenvectors of $W$)'),
    ]
    ax.legend(handles=legend_handles, loc='lower right', fontsize=8, framealpha=0.85)

    ax.set_title('Degenerate subspace: $\\hat{H}_0$ is isotropic; $W$ picks the good basis',
                 fontsize=10, pad=8)

    fig.tight_layout()
    fig.savefig('02-degenerate-perturbation-theory-and-fine-structure-fig-01.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 02-degenerate-perturbation-theory-and-fine-structure-fig-01.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 2.2 — Hydrogen n=2 Stark splitting: 4 states → 3 lines vs field ε
# Shifts: ±3 a₀ e ε  (linear in ε)
# ─────────────────────────────────────────────────────────────────────────────
def fig_02_02():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    clean_ax(ax)

    # x-axis = field strength ε (arbitrary units, 0→1)
    eps = np.linspace(0, 1, 200)
    # Energy shifts (in units of 3 a₀ e)
    E_plus  =  eps        # (|2s⟩ - |2p₀⟩)/√2
    E_zero  =  np.zeros_like(eps)   # |2p+1⟩, |2p-1⟩ (doubly degenerate)
    E_minus = -eps        # (|2s⟩ + |2p₀⟩)/√2

    ax.plot(eps, E_plus,  color=TAB[1], lw=2.2, label=r'$(|2s\rangle-|2p_0\rangle)/\sqrt{2}$,  $+3a_0 e\mathcal{E}$')
    ax.plot(eps, E_zero,  color=TAB[2], lw=2.2, label=r'$|2p_{\pm1}\rangle$ (doubly degenerate)',
            linestyle='--')
    ax.plot(eps, E_minus, color=TAB[0], lw=2.2, label=r'$(|2s\rangle+|2p_0\rangle)/\sqrt{2}$,  $-3a_0 e\mathcal{E}$')

    # Mark ε=0 degeneracy
    ax.axvline(0, color='0.6', lw=0.8, linestyle=':')
    ax.text(0.02, 0.85, 'all four\nstates\ndegenerate', fontsize=7.5, color='0.4',
            transform=ax.transAxes, va='top')

    # Annotate double intensity
    ax.annotate('double intensity\n(2 states)', xy=(0.85, 0.01), xytext=(0.6, 0.22),
                fontsize=8, color=TAB[2],
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=1.2),
                ha='center')

    ax.set_xlabel(r'Electric field strength $\mathcal{E}$ (arb. units)', fontsize=10)
    ax.set_ylabel(r'Energy shift ($3a_0 e\mathcal{E}$ units)', fontsize=10)
    ax.set_title(r'Hydrogen $n=2$ linear Stark effect: four states split into three lines',
                 fontsize=10, pad=6)
    ax.set_xlim(0, 1)
    ax.set_ylim(-1.2, 1.2)
    ax.set_yticks([-1, 0, 1])
    ax.set_yticklabels([r'$-3a_0 e\mathcal{E}$', '0', r'$+3a_0 e\mathcal{E}$'], fontsize=9)
    ax.set_xticks([0, 0.5, 1.0])
    ax.legend(fontsize=8, loc='upper left', framealpha=0.9)

    fig.tight_layout()
    fig.savefig('02-degenerate-perturbation-theory-and-fine-structure-fig-02.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 02-degenerate-perturbation-theory-and-fine-structure-fig-02.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 2.3 — n=2 hydrogen: three-stage energy level diagram
#   Stage 1: all 8 states degenerate at E₂⁰ = -3.4 eV
#   Stage 2: fine structure — 2p₃/₂ at -3.4+ΔE_fs(j=3/2), 2s₁/₂/2p₁/₂ at -3.4+ΔE_fs(j=1/2)
#   Stage 3: Lamb shift — 2s₁/₂ slightly above 2p₁/₂ by 4.4e-6 eV
# Numerical values from chapter:
#   ΔE_FS(j=3/2) = -1.13e-5 eV, ΔE_FS(j=1/2) = -5.66e-5 eV
#   splitting = 4.53e-5 eV
#   Lamb shift = 4.4e-6 eV (2s₁/₂ above 2p₁/₂)
# ─────────────────────────────────────────────────────────────────────────────
def fig_02_03():
    # Use a wider figure for this 3-stage diagram to avoid label collision
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.35, 1.55)

    # Energy scale:
    #   y=0   → 2p₁/₂ (lowest after Lamb shift)
    #   y=0.18 → 2s₁/₂ (Lamb shift above 2p₁/₂; displayed 0.18 units for visibility)
    #   y=1.0  → 2p₃/₂ (fine-structure gap = 1 unit)
    #   y=0.5  → unperturbed degenerate level (midpoint of fine-structure range)
    # Lamb shift is physically ~10× smaller than FS gap; we show it at 0.18 (visually ~20%)
    # so it's clearly visible but distinctly smaller than the FS gap.

    lamb_disp  = 0.20   # displayed Lamb shift (in display units)
    y_j32      = 1.0    # 2p₃/₂
    y_j12_degen = 0.0   # 2s₁/₂ = 2p₁/₂ before Lamb shift
    y_2s       = lamb_disp   # 2s₁/₂ after Lamb shift
    y_2p       = 0.0         # 2p₁/₂ after Lamb shift
    y_degen    = (y_j32 + y_j12_degen) / 2   # = 0.5: stage-1 level

    x_stage   = [1.6, 5.2, 9.6]
    col_w     = 1.3
    lw        = 2.8

    # ── Stage 1: unperturbed ──
    ax.hlines(y_degen, x_stage[0]-col_w, x_stage[0]+col_w, colors='0.3', lw=lw)
    ax.text(x_stage[0], y_degen + 0.10, r'$n=2$ (8 states)',
            ha='center', fontsize=9, color='0.3')
    ax.text(x_stage[0], y_degen - 0.16, r'$E_2^{(0)}=-3.4\,\mathrm{eV}$',
            ha='center', fontsize=8.5, color='0.55')

    # ── Stage 2: fine structure ──
    ax.hlines(y_j32,        x_stage[1]-col_w, x_stage[1]+col_w, colors=TAB[1], lw=lw)
    ax.hlines(y_j12_degen,  x_stage[1]-col_w, x_stage[1]+col_w, colors=TAB[0], lw=lw)
    ax.text(x_stage[1]+col_w+0.12, y_j32+0.04,       r'$2p_{3/2}$',          fontsize=9.5, color=TAB[1])
    ax.text(x_stage[1]+col_w+0.12, y_j12_degen-0.10, r'$2s_{1/2},\,2p_{1/2}$', fontsize=9.5, color=TAB[0])

    # FS splitting brace — place between stage 2 and stage 3
    bx = (x_stage[1] + col_w + x_stage[2] - col_w) / 2
    ax.annotate('', xy=(bx, y_j32), xytext=(bx, y_j12_degen),
                arrowprops=dict(arrowstyle='<->', color='0.45', lw=1.3))
    ax.text(bx + 0.15, (y_j32 + y_j12_degen)/2,
            r'$4.5\!\times\!10^{-5}$' + ' eV' + '\n(fine structure)',
            ha='left', va='center', fontsize=8, color='0.4')

    # ── Stage 3: fine structure + Lamb shift ──
    ax.hlines(y_j32, x_stage[2]-col_w, x_stage[2]+col_w, colors=TAB[1], lw=lw)
    ax.hlines(y_2s,  x_stage[2]-col_w, x_stage[2]+col_w, colors=TAB[2], lw=lw)
    ax.hlines(y_2p,  x_stage[2]-col_w, x_stage[2]+col_w, colors=TAB[0], lw=lw, linestyle='--')
    ax.text(x_stage[2]+col_w+0.12, y_j32+0.04, r'$2p_{3/2}$',  fontsize=9.5, color=TAB[1])
    ax.text(x_stage[2]+col_w+0.12, y_2s+0.04,  r'$2s_{1/2}$',  fontsize=9.5, color=TAB[2])
    ax.text(x_stage[2]+col_w+0.12, y_2p-0.10,  r'$2p_{1/2}$',  fontsize=9.5, color=TAB[0])

    # Lamb shift brace (left of stage-3 levels)
    lx = x_stage[2] - col_w - 0.6
    ax.annotate('', xy=(lx, y_2s), xytext=(lx, y_2p),
                arrowprops=dict(arrowstyle='<->', color=TAB[3], lw=1.5))
    ax.text(lx - 0.12, (y_2s + y_2p)/2,
            r'$4.4\!\times\!10^{-6}$' + ' eV' + '\n(Lamb shift)',
            ha='right', va='center', fontsize=8, color=TAB[3])

    # ── Stage labels ──
    for xi, label in zip(x_stage, ['(1) Unperturbed', '(2) Fine structure', '(3) + Lamb shift']):
        ax.text(xi, -0.28, label, ha='center', fontsize=9.5, style='italic', color='0.35')

    # ── Connecting dotted guides ──
    for y_end in [y_j32, y_j12_degen]:
        ax.plot([x_stage[0]+col_w, x_stage[1]-col_w], [y_degen, y_end],
                color='0.78', lw=0.9, linestyle=':')
    for y_s2, y_s3 in [(y_j32, y_j32), (y_j12_degen, y_2s), (y_j12_degen, y_2p)]:
        ax.plot([x_stage[1]+col_w, x_stage[2]-col_w], [y_s2, y_s3],
                color='0.78', lw=0.9, linestyle=':')

    ax.set_title(r'Hydrogen $n=2$: fine structure splits $j=\frac{1}{2}$ from $j=\frac{3}{2}$;'
                 r' Lamb shift resolves $2s_{1/2}$ from $2p_{1/2}$',
                 fontsize=9.5, pad=8)

    fig.tight_layout()
    fig.savefig('02-degenerate-perturbation-theory-and-fine-structure-fig-03.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 02-degenerate-perturbation-theory-and-fine-structure-fig-03.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 3.1 — Variational principle: number line showing E₀, E_V*, forbidden region
# ─────────────────────────────────────────────────────────────────────────────
def fig_03_01():
    fig, ax = plt.subplots(figsize=(7, 2.2), dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(-3.5, 5.0)
    ax.set_ylim(-0.8, 1.2)
    ax.axis('off')

    # Draw number line
    ax.hlines(0, -3.0, 4.5, colors='0.3', lw=1.5)
    ax.annotate('', xy=(4.7, 0), xytext=(4.3, 0),
                arrowprops=dict(arrowstyle='->', color='0.3', lw=1.5))

    # Forbidden region: shade from left up to E₀
    E0_x = -1.0
    ax.axvspan(-3.5, E0_x, ymin=0.35, ymax=0.65, color='#ffdddd', zorder=0)
    ax.text(-2.2, 0.55, 'no trial state\ncan reach here', fontsize=8.5,
            ha='center', color='#cc3333', style='italic')

    # E₀ tick and label
    ax.vlines(E0_x, -0.25, 0.25, colors=TAB[0], lw=2.5)
    ax.text(E0_x, -0.52, r'$E_0$', ha='center', fontsize=13, color=TAB[0], fontweight='bold')
    ax.text(E0_x, 0.38, 'true ground\nstate energy', ha='center', fontsize=8.5, color=TAB[0])

    # E_V* tick and label
    Ev_x = 2.0
    ax.vlines(Ev_x, -0.25, 0.25, colors=TAB[1], lw=2.5)
    ax.text(Ev_x, -0.52, r'$E_V^*$', ha='center', fontsize=13, color=TAB[1], fontweight='bold')
    ax.text(Ev_x, 0.38, 'best variational\nupper bound', ha='center', fontsize=8.5, color=TAB[1])

    # Double-headed arrow from E₀ to E_V*
    ax.annotate('', xy=(Ev_x-0.05, -0.3), xytext=(E0_x+0.05, -0.3),
                arrowprops=dict(arrowstyle='<->', color='0.5', lw=1.2))
    ax.text((E0_x+Ev_x)/2, -0.7, r'$E_V^* - E_0 \geq 0$', ha='center', fontsize=9.5, color='0.4')

    # Inequality annotation
    ax.text(3.5, 0.0, r'$\langle\hat{H}\rangle \geq E_0$', ha='center', fontsize=11,
            color='0.35', bbox=dict(boxstyle='round,pad=0.3', facecolor='#f0f4ff',
                                    edgecolor='0.6', lw=0.8))

    ax.set_title('The variational bound: $\\langle\\hat{H}\\rangle \\geq E_0$ — all trial states lie to the right of $E_0$',
                 fontsize=9.5, pad=6)
    fig.tight_layout()
    fig.savefig('03-the-variational-principle-fig-01.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 03-the-variational-principle-fig-01.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 6.3 — Angular momentum coupling diagram: photon (L=1, q=0,±1) selection rules
# Shows allowed (Δℓ=±1, Δm=q) transitions as a grid
# ─────────────────────────────────────────────────────────────────────────────
def fig_06_03():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)

    ax.set_title(r'Electric-dipole selection rules: $\Delta\ell=\pm1$, $\Delta m = q$ (photon $q=0,\pm1$)',
                 fontsize=10, pad=6)

    # Draw two atomic levels: ℓ and ℓ'=ℓ+1, with m substates
    # Show example: initial ℓ=1 (m=-1,0,+1) → final ℓ=2 (m=-2,-1,0,+1,+2)
    # and initial ℓ=1 → final ℓ=0 (m=0)

    # Panel layout: left=initial states, right=final states
    x_init = 2.5
    x_final = 7.5
    lw_arrow = 1.6

    # ─── Case: ℓ=1 → ℓ'=2 (Δℓ=+1) ───
    y_top = 5.5
    # Initial: ℓ=1 substates m=-1,0,+1
    m_init_vals = [-1, 0, 1]
    y_init = {m: y_top - 0.6*(m+1) for m in m_init_vals}  # y positions
    for m in m_init_vals:
        ax.plot(x_init, y_init[m], 'o', color=TAB[0], ms=9, zorder=5)
        ax.text(x_init-0.55, y_init[m], fr'$m={m:+d}$', fontsize=9, ha='right', va='center',
                color=TAB[0])

    ax.text(x_init, y_top+0.5, r'$\ell=1$ (initial)', fontsize=9.5, ha='center',
            color=TAB[0], fontweight='bold')

    # Final: ℓ'=2 substates m'=-2,-1,0,+1,+2 but only m'=-1,0,+1,+2 reachable from ℓ=1
    m_final_vals = [-2, -1, 0, 1, 2]
    y_final = {m: y_top - 0.5*(m+2) for m in m_final_vals}
    for m in m_final_vals:
        ax.plot(x_final, y_final[m], 's', color=TAB[1], ms=9, zorder=5)
        ax.text(x_final+0.55, y_final[m], fr"$m'={m:+d}$", fontsize=9, ha='left', va='center',
                color=TAB[1])

    ax.text(x_final, y_top+0.5, r"$\ell'=2$ (final)", fontsize=9.5, ha='center',
            color=TAB[1], fontweight='bold')

    # Draw allowed transitions: Δm = q = -1, 0, +1
    colors_q = {-1: TAB[3], 0: TAB[2], 1: TAB[4]}
    labels_q = {-1: r'$\sigma^-$: $\Delta m=-1$', 0: r'$\pi$: $\Delta m=0$', 1: r'$\sigma^+$: $\Delta m=+1$'}

    for m_i in m_init_vals:
        for q in [-1, 0, 1]:
            m_f = m_i + q
            if m_f in m_final_vals:
                yi = y_init[m_i]
                yf = y_final[m_f]
                ax.annotate('', xy=(x_final-0.18, yf), xytext=(x_init+0.18, yi),
                            arrowprops=dict(arrowstyle='->', color=colors_q[q],
                                           lw=lw_arrow, alpha=0.75),
                            zorder=3)

    # Legend for polarizations
    legend_handles = [mlines.Line2D([], [], color=colors_q[q], lw=2, label=labels_q[q])
                      for q in [-1, 0, 1]]
    ax.legend(handles=legend_handles, loc='lower center', fontsize=9, framealpha=0.9,
              bbox_to_anchor=(0.5, -0.05))

    # Forbidden note
    ax.text(5.0, 0.5, r'$\Delta\ell=0$ forbidden (parity);  $|\Delta m|>1$ forbidden (azimuthal)',
            ha='center', fontsize=8.5, color='0.45', style='italic')

    fig.tight_layout()
    fig.savefig('06-radiation-and-fermis-golden-rule-fig-03.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 06-radiation-and-fermis-golden-rule-fig-03.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 8.1 — Lippmann-Schwinger scattering geometry
# Incident plane wave → scattering region V(r') → outgoing spherical wave
# ─────────────────────────────────────────────────────────────────────────────
def fig_08_01():
    fig, ax = plt.subplots(figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-2.2, 2.5)
    ax.set_aspect('equal')
    ax.axis('off')

    ax.set_title('Lippmann-Schwinger geometry: incident plane wave → scatterer → outgoing spherical wave',
                 fontsize=9.5, pad=6)

    # Scattering region (potential) at center
    scatter_circle = plt.Circle((0, 0), 0.55, color='#cce0ff', ec=TAB[0], lw=1.8, zorder=4)
    ax.add_patch(scatter_circle)
    ax.text(0, 0, r'$V(\mathbf{r}^\prime)$', ha='center', va='center', fontsize=10,
            color=TAB[0], fontweight='bold', zorder=5)

    # Incident plane wave (wavefronts + arrow from left)
    for xw in np.arange(-4.5, -0.8, 0.7):
        ax.axvline(xw, ymin=0.3, ymax=0.7, color=TAB[2], lw=0.8, alpha=0.5)
    ax.annotate('', xy=(-0.7, 0), xytext=(-2.5, 0),
                arrowprops=dict(arrowstyle='->', color=TAB[2], lw=2.2))
    ax.text(-3.2, 0.3, r'$e^{i\mathbf{k}\cdot\mathbf{r}}$', fontsize=12, color=TAB[2])
    ax.text(-3.2, -0.5, r'$\mathbf{k}$ (incident)', fontsize=9, color=TAB[2])

    # Source point r' inside potential
    rp = np.array([-0.2, 0.25])
    ax.plot(*rp, 'o', color=TAB[3], ms=6, zorder=6)
    ax.text(rp[0]-0.12, rp[1]+0.18, r"$\mathbf{r}^\prime$", fontsize=10, color=TAB[3])

    # Detector at r (upper right)
    r_det = np.array([3.5, 1.8])
    ax.plot(*r_det, 'D', color=TAB[1], ms=8, zorder=6)
    ax.text(r_det[0]+0.15, r_det[1]+0.12, r'detector $\mathbf{r}$', fontsize=9, color=TAB[1])

    # Arrow from r' to r (propagator path)
    ax.annotate('', xy=r_det-0.2*(r_det-rp)/np.linalg.norm(r_det-rp),
                    xytext=rp+0.2*(r_det-rp)/np.linalg.norm(r_det-rp),
                arrowprops=dict(arrowstyle='->', color=TAB[3], lw=1.6, linestyle='dashed'))
    mid = (rp + r_det) / 2 + np.array([-0.3, 0.1])
    ax.text(mid[0], mid[1], r'$|\mathbf{r}-\mathbf{r}^\prime|$', fontsize=9.5, color=TAB[3])

    # Outgoing spherical waves (arcs)
    theta_vals = np.linspace(0, 2*np.pi, 300)
    for R in [1.2, 1.8, 2.5]:
        # Only draw the right half (outgoing)
        mask = (theta_vals > -np.pi/2) & (theta_vals < np.pi/2 * 2.5)
        xs = R * np.cos(theta_vals[mask])
        ys = R * np.sin(theta_vals[mask])
        ax.plot(xs, ys, color=TAB[1], lw=0.9, alpha=0.45)

    # Outgoing wave label and k' arrow
    ax.annotate('', xy=(3.2, 0.05), xytext=(0.8, 0.05),
                arrowprops=dict(arrowstyle='->', color=TAB[1], lw=1.8))
    ax.text(1.5, 0.4, r"$\mathbf{k}^\prime = k\hat{r}$" + "\n(outgoing)", fontsize=9, color=TAB[1])

    # Outgoing spherical wave label
    ax.text(3.8, -0.9, r'$f(\mathbf{k},\mathbf{k}^\prime)\,\frac{e^{ikr}}{r}$',
            fontsize=10, color=TAB[1])

    fig.tight_layout()
    fig.savefig('08-scattering-ii-the-born-approximation-fig-01.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 08-scattering-ii-the-born-approximation-fig-01.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 8.2 — Momentum transfer triangle: k, k', q = k - k', |q| = 2k sin(θ/2)
# Show two cases: θ small (q small) and θ large (q ~ 2k)
# ─────────────────────────────────────────────────────────────────────────────
def fig_08_02():
    fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    fig.suptitle(r'Momentum transfer $\mathbf{q}=\mathbf{k}-\mathbf{k}^\prime$, $|\mathbf{q}|=2k\sin(\theta/2)$',
                 fontsize=10, y=1.01)

    for ax, (theta_deg, label) in zip(axes, [(25, r'Small $\theta$: $q \ll 2k$ (forward)'),
                                              (130, r'Large $\theta$: $q \approx 2k$ (back)')]):
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-0.3, 2.0)
        ax.set_ylim(-1.0, 1.2)

        k = 1.4  # magnitude
        theta = np.deg2rad(theta_deg)

        # k: along x-axis
        k_vec = np.array([k, 0.0])
        # k': at angle theta from k
        kp_vec = np.array([k * np.cos(theta), k * np.sin(theta)])
        # q = k - k'
        q_vec = k_vec - kp_vec

        origin = np.array([0.2, 0.0])

        def arr(ax, start, end, color, lw=2.0, label='', offset=(0, 0.08)):
            ax.annotate('', xy=start+end, xytext=start,
                        arrowprops=dict(arrowstyle='->', color=color, lw=lw), zorder=5)
            mid = start + end/2 + np.array(offset)
            if label:
                ax.text(mid[0], mid[1], label, fontsize=10, color=color, ha='center')

        arr(ax, origin, k_vec, TAB[0], label=r'$\mathbf{k}$', offset=(0, -0.18))
        arr(ax, origin, kp_vec, TAB[1], label=r"$\mathbf{k}'$", offset=(-0.12, 0.12))
        # q goes from tip of k' to tip of k: start at origin+kp_vec, end direction is q_vec
        arr(ax, origin+kp_vec, q_vec, TAB[2], label=r'$\mathbf{q}$', offset=(0.1, 0.08))

        # Arc for angle theta
        arc_r = 0.35
        arc_theta = np.linspace(0, theta, 60)
        ax.plot(origin[0] + arc_r*np.cos(arc_theta),
                origin[1] + arc_r*np.sin(arc_theta), color='0.5', lw=1.2)
        ax.text(origin[0]+arc_r*np.cos(theta/2)+0.05,
                origin[1]+arc_r*np.sin(theta/2)+0.05, r'$\theta$', fontsize=10, color='0.4')

        # q magnitude annotation
        q_mag = 2*k*np.sin(theta/2)
        ax.text(0.95, -0.8, fr'$|q| = 2k\sin(\theta/2) = {q_mag/k:.2f}\,k$',
                fontsize=9, ha='center', color=TAB[2])

        ax.set_title(label, fontsize=9, pad=4)
        clean_ax(ax)

    fig.tight_layout()
    fig.savefig('08-scattering-ii-the-born-approximation-fig-02.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 08-scattering-ii-the-born-approximation-fig-02.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 9.3 — Pulsed NMR sequence: π/2 pulse, FID, π pulse, spin echo
# ─────────────────────────────────────────────────────────────────────────────
def fig_09_03():
    fig, axes = plt.subplots(2, 1, figsize=FIGSIZE, dpi=DPI, sharex=True,
                             gridspec_kw={'height_ratios': [1, 2]})
    fig.patch.set_facecolor('white')

    T2star = 1.2   # apparent T2* (inhomogeneous)
    T2     = 3.5   # true T2 (echo decay)
    tau    = 2.5   # π pulse at t=tau
    omega0 = 8.0   # Larmor frequency (arb units)
    t_end  = 6.5

    t = np.linspace(0, t_end, 4000)

    # Panel 1: RF pulse sequence
    ax_rf = axes[0]
    clean_ax(ax_rf)
    ax_rf.set_ylim(-0.2, 1.6)
    ax_rf.set_yticks([])
    ax_rf.set_ylabel('RF\npulse', fontsize=8, rotation=0, labelpad=30, va='center')

    # π/2 pulse at t=0 (narrow)
    ax_rf.bar(0.05, 0.7, width=0.12, color=TAB[0], align='center', zorder=3)
    ax_rf.text(0.05, 0.85, r'$\pi/2$', ha='center', fontsize=9, color=TAB[0])

    # π pulse at t=tau
    ax_rf.bar(tau, 1.4, width=0.12, color=TAB[1], align='center', zorder=3)
    ax_rf.text(tau, 1.55, r'$\pi$', ha='center', fontsize=9, color=TAB[1])

    ax_rf.axhline(0, color='0.6', lw=0.8)
    ax_rf.spines['bottom'].set_visible(False)
    ax_rf.set_title('Pulsed NMR: free induction decay and spin echo', fontsize=10, pad=6)

    # Panel 2: Signal
    ax_sig = axes[1]
    clean_ax(ax_sig)

    # FID: oscillation × e^{-t/T2*}
    fid_mask = t <= tau - 0.1
    t_fid = t[fid_mask]
    signal_fid = np.exp(-t_fid / T2star) * np.cos(omega0 * t_fid)
    ax_sig.plot(t_fid, signal_fid, color=TAB[2], lw=1.0, alpha=0.85)

    # FID envelope
    ax_sig.plot(t_fid, np.exp(-t_fid / T2star), color=TAB[2], lw=1.5, linestyle='--', alpha=0.6)
    ax_sig.plot(t_fid, -np.exp(-t_fid / T2star), color=TAB[2], lw=1.5, linestyle='--', alpha=0.6)

    # After π pulse: rephasing → echo at t=2τ
    # Echo signal: refocusing after π pulse — oscillation × e^{-(t-2tau)/T2*} × e^{-2tau/T2} (echo amplitude)
    echo_center = 2 * tau
    echo_amp = np.exp(-echo_center / T2)  # true T2 decay

    # Echo envelope: peaks at t=2tau, decays symmetrically
    t_echo_region = t[(t > tau + 0.1) & (t <= t_end)]
    echo_env = echo_amp * np.exp(-np.abs(t_echo_region - echo_center) / T2star)
    echo_sig  = echo_env * np.cos(omega0 * (t_echo_region - echo_center))

    ax_sig.plot(t_echo_region, echo_sig, color=TAB[1], lw=1.0, alpha=0.85)
    ax_sig.plot(t_echo_region, echo_env, color=TAB[1], lw=1.5, linestyle='--', alpha=0.6)
    ax_sig.plot(t_echo_region, -echo_env, color=TAB[1], lw=1.5, linestyle='--', alpha=0.6)

    # Mark key times
    ax_sig.axvline(0, color='0.6', lw=0.8, linestyle=':')
    ax_sig.axvline(tau, color='0.6', lw=0.8, linestyle=':')
    ax_sig.axvline(echo_center, color='0.6', lw=0.8, linestyle=':')

    ax_sig.set_xlabel(r'Time $t$', fontsize=10)
    ax_sig.set_ylabel('Signal (arb. units)', fontsize=9)
    ax_sig.set_ylim(-1.3, 1.3)

    # Annotations
    ax_sig.text(0.05, 1.15, 'FID', fontsize=9, color=TAB[2])
    ax_sig.text(0.05, 0.9, r'$\sim e^{-t/T_2^*}$', fontsize=8.5, color=TAB[2])
    ax_sig.text(echo_center+0.08, 1.15, 'echo', fontsize=9, color=TAB[1])
    ax_sig.text(echo_center+0.08, 0.9, r'$\sim e^{-2\tau/T_2}$', fontsize=8.5, color=TAB[1])

    # tau and 2tau labels on x-axis
    ax_sig.set_xticks([0, tau, echo_center])
    ax_sig.set_xticklabels([r'$0$', r'$\tau$', r'$2\tau$'], fontsize=10)

    fig.tight_layout()
    fig.savefig('09-atoms-in-fields-fig-03.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 09-atoms-in-fields-fig-03.png')


# ─────────────────────────────────────────────────────────────────────────────
# Fig 10.2 — Band-filling schematic: metal, semiconductor, insulator
# Three panels showing filled/empty bands and Fermi level
# ─────────────────────────────────────────────────────────────────────────────
def fig_10_02():
    fig, axes = plt.subplots(1, 3, figsize=FIGSIZE, dpi=DPI)
    fig.patch.set_facecolor('white')
    fig.suptitle('Band filling: metal, semiconductor, and insulator', fontsize=10.5, y=1.01)

    configs = [
        {
            'title': 'Metal',
            'subtitle': '(e.g., Na, K)',
            'bands': [
                {'bottom': 0.0, 'top': 1.0, 'fill': 0.5, 'label': 'conduction\nband'},
            ],
            'EF': 0.5,
            'gap': None,
            'gap_label': None,
        },
        {
            'title': 'Semiconductor',
            'subtitle': r'(e.g., Si: gap 1.12 eV)',
            'bands': [
                {'bottom': 0.0, 'top': 0.8, 'fill': 0.8, 'label': 'valence\nband'},
                {'bottom': 1.0, 'top': 1.8, 'fill': 0.0, 'label': 'conduction\nband'},
            ],
            'EF': 0.9,
            'gap': (0.8, 1.0),
            'gap_label': r'$E_g \sim 1$ eV',
        },
        {
            'title': 'Insulator',
            'subtitle': r'(e.g., diamond: gap 5.5 eV)',
            'bands': [
                {'bottom': 0.0, 'top': 0.6, 'fill': 0.6, 'label': 'valence\nband'},
                {'bottom': 1.6, 'top': 2.2, 'fill': 0.0, 'label': 'conduction\nband'},
            ],
            'EF': 1.1,
            'gap': (0.6, 1.6),
            'gap_label': r'$E_g \sim 5$ eV',
        },
    ]

    for ax, cfg in zip(axes, configs):
        clean_ax(ax)
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.1, 2.4)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(cfg['title'] + '\n' + cfg['subtitle'], fontsize=9.5, pad=3)
        ax.set_xlabel('$k$ (schematic)', fontsize=8.5)
        if ax == axes[0]:
            ax.set_ylabel('Energy', fontsize=9)

        for band in cfg['bands']:
            bot = band['bottom']
            top = band['top']
            fill = band['fill']  # fraction filled (from bottom)
            fill_top = bot + (top - bot) * fill

            # Band extent (unfilled part)
            ax.fill_between([0.1, 0.9], bot, top, color='#dde8ff', alpha=0.7,
                            linewidth=0)
            ax.hlines([bot, top], 0.1, 0.9, colors='0.4', lw=1.2)

            # Filled portion
            if fill > 0:
                ax.fill_between([0.1, 0.9], bot, fill_top,
                                color=TAB[0], alpha=0.55, linewidth=0)

            # Band label
            ax.text(0.5, (bot + top) / 2, band['label'],
                    ha='center', va='center', fontsize=8, color='0.35')

        # Gap shading
        if cfg['gap']:
            g_bot, g_top = cfg['gap']
            ax.fill_between([0.1, 0.9], g_bot, g_top, color='white',
                            hatch='/////', edgecolor='0.75', linewidth=0, alpha=0.8)
            if cfg['gap_label']:
                ax.text(0.5, (g_bot + g_top) / 2, cfg['gap_label'],
                        ha='center', va='center', fontsize=8.5, color='0.4')

        # Fermi level
        ax.hlines(cfg['EF'], 0.0, 1.0, colors='red', lw=1.8, linestyle='--', zorder=6)
        ax.text(0.97, cfg['EF']+0.06, r'$E_F$', color='red', fontsize=9.5, ha='right')

    fig.tight_layout()
    fig.savefig('10-periodic-potentials-and-band-structure-fig-02.png',
                dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print('wrote 10-periodic-potentials-and-band-structure-fig-02.png')


# ─────────────────────────────────────────────────────────────────────────────
# RUN ALL
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    fig_02_01()
    fig_02_02()
    fig_02_03()
    fig_03_01()
    fig_06_03()
    fig_08_01()
    fig_08_02()
    fig_09_03()
    fig_10_02()
    print('Done — 9 figures written.')
