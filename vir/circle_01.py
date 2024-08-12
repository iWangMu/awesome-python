import numpy as np
import matplotlib.pyplot as plt

theta_array = np.linspace(0, 2 * np.pi, 120, endpoint=False)
sin_y = np.sin(theta_array)
cos_y = np.cos(theta_array)

colors = plt.cm.hsv(np.linspace(0, 1, 120))

fig, ax = plt.subplots(figsize=(6, 6))

ax.plot(cos_y, sin_y, zorder=1, color="k", lw=0.25)
ax.scatter(cos_y, sin_y, marker=".", s=88, c=colors, edgecolor="w", zorder=2)
ax.axhline(0, c="k", zorder=1)
ax.axvline(0, c="k", zorder=1)
ax.set_xlabel(r"$x = cos(\theta)$")
ax.set_ylabel(r"$y = sin(\theta)$")
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.grid(True)
# 横纵轴采用相同的scale
ax.set_aspect("equal")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["left"].set_visible(False)

plt.show()
