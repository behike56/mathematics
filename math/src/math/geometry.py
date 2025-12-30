"""
幾何学
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib_fontja


# -----------------------------
# Plot 1: Right triangle showing opposite/adjacent/hypotenuse for angle θ
# -----------------------------
theta_deg = 35
theta = np.deg2rad(theta_deg)

# Choose a convenient triangle with hypotenuse = 1
hyp = 1.0
adj = hyp * np.cos(theta)
opp = hyp * np.sin(theta)

# Triangle vertices
A = np.array([0.0, 0.0])  # angle θ is at A
B = np.array([adj, 0.0])  # adjacent along x-axis
C = np.array([adj, opp])  # opposite up from B

plt.figure(figsize=(6, 4.5))
# Draw triangle
plt.plot([A[0], B[0]], [A[1], B[1]], linewidth=2)
plt.plot([B[0], C[0]], [B[1], C[1]], linewidth=2)
plt.plot([C[0], A[0]], [C[1], A[1]], linewidth=2)

# Right angle marker at B
s = 0.08
plt.plot([B[0], B[0]], [B[1], B[1] + s], linewidth=2)
plt.plot([B[0], B[0] - s], [B[1] + s, B[1] + s], linewidth=2)

# Labels
mid_AB = (A + B) / 2
mid_BC = (B + C) / 2
mid_CA = (C + A) / 2

plt.text(mid_AB[0], mid_AB[1] - 0.06, "adjacent (隣辺)", ha="center", va="top")
plt.text(mid_BC[0] + 0.05, mid_BC[1], "opposite (対辺)", ha="left", va="center")
plt.text(
    mid_CA[0] - 0.02, mid_CA[1] + 0.02, "hypotenuse (斜辺)", ha="right", va="bottom"
)

# Angle arc at A
arc_r = 0.18
arc_t = np.linspace(0, theta, 100)
plt.plot(arc_r * np.cos(arc_t), arc_r * np.sin(arc_t), linewidth=2)
plt.text(
    arc_r * 0.9 * np.cos(theta / 2),
    arc_r * 0.9 * np.sin(theta / 2),
    r"$\theta$",
    ha="left",
    va="bottom",
)

plt.title(f"Right triangle (θ = {theta_deg}°)")
plt.axis("equal")
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 0.9)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# -----------------------------
# Plot 2: Unit circle showing cosθ (x) and sinθ (y)
# -----------------------------
plt.figure(figsize=(6, 6))

t = np.linspace(0, 2 * np.pi, 400)
plt.plot(np.cos(t), np.sin(t), linewidth=2)  # unit circle
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Point on unit circle
P = np.array([np.cos(theta), np.sin(theta)])
plt.plot([0, P[0]], [0, P[1]], linewidth=2)  # radius
plt.scatter([P[0]], [P[1]], s=60)

# Projections
plt.plot([P[0], P[0]], [0, P[1]], linewidth=2)  # vertical projection (sin)
plt.plot([0, P[0]], [0, 0], linewidth=2)  # horizontal projection (cos)

plt.text(P[0], -0.08, r"$\cos\theta$", ha="center", va="top")
plt.text(P[0] + 0.08, P[1] / 2, r"$\sin\theta$", ha="left", va="center")
plt.text(
    P[0] + 0.05, P[1] + 0.05, r"$P(\cos\theta,\sin\theta)$", ha="left", va="bottom"
)

# Angle arc
arc_r2 = 0.25
arc_t2 = np.linspace(0, theta, 100)
plt.plot(arc_r2 * np.cos(arc_t2), arc_r2 * np.sin(arc_t2), linewidth=2)
plt.text(
    arc_r2 * 0.9 * np.cos(theta / 2),
    arc_r2 * 0.9 * np.sin(theta / 2),
    r"$\theta$",
    ha="left",
    va="bottom",
)

plt.title("Unit circle view: cosθ and sinθ")
plt.axis("equal")
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
