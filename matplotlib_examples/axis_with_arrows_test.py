import numpy as np
import axis_with_arrows as arrows
from scipy import stats


# # y = 8*x - x^2
# x = np.arange(0, 8.1, 0.1)
# y = [8 * v - v ** 2 for v in x]
# xlim = arrows.axis_lim(0, 8)
# ylim = arrows.axis_lim(0, 17)
# xticks = arrows.axis_ticks(0, 8, 1)
# yticks = arrows.axis_ticks(0, 16, 2, False)
# arrows.drawPlot(x, y, xlim, ylim, xticks, yticks)

# # y = 4*x^2 - 1/3*x^3
# x = np.arange(0, 8.1, 0.1)
# y = [4 * v**2 - 1 / 3 * v ** 3 for v in x]
# xlim = arrows.axis_lim(0, 8)
# ylim = arrows.axis_lim(0, 95)
# xticks = arrows.axis_ticks(0, 8, 1)
# yticks = arrows.axis_ticks(0, 90, 10, False)
# arrows.drawPlot(x, y, xlim, ylim, xticks, yticks)

# x = np.arange(0, 3 * np.pi, 0.1)
# y = []
# for v in x:
#     if v < 1.5 * np.pi:
#         y.append(np.sin(v) + 2)
#     else:
#         y.append((v - 1.5 * np.pi) ** 2 - 1 + 2)
# xlim = arrows.axis_lim(-1, 10)
# ylim = arrows.axis_lim(-1, 5)
# xticks = arrows.axis_ticks(0, 3, 0.1)
# yticks = arrows.axis_ticks(-1, 5, 1, False)
# arrows.drawPlot(x, y, xlim, ylim, xticks, yticks, showTicklabels=False)


# x = np.linspace(0, 8, 10000)
# y1 = stats.norm.pdf(x, 4, 1)
# y2 = stats.norm.cdf(x, 4, 1)
# y3 = [0.4 * v - 1.1 for v in x]

# arrows.drawPlot(x, (y2, y3), arrows.axis_lim(0, 8), arrows.axis_lim(0, 1),
#                 arrows.axis_ticks(0, 8, 1), arrows.axis_ticks(0, 1.2, 0.2, False),
#                 show_x_ticklabels=True, show_y_ticklabels=True,
#                 figsize=(6, 6))


x = np.arange(0, 25, 1)
y1 = [6 for i in x]
y2 = [5.8 for i in x]

arrows.drawPlot(
    x,
    (y1, y2),
    arrows.axis_lim(0, 25),
    arrows.axis_lim(0, 7),
    arrows.axis_ticks(0, 25, 4),
    arrows.axis_ticks(0, 7, 2, False),
    show_x_ticklabels=True,
    show_y_ticklabels=True,
    figsize=(6, 6),
)
