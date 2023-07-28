import matplotlib.pyplot as plt
import numpy as np

figure, axes = plt.subplots()
# 同心圆
# radiuses = list(np.arange(0.0, 0.31, 0.01))
# radiuses.reverse()
# radiuses.append(0.001)
# for radius in radiuses:
#     facecolor = 'lightblue'
#     if radius == 0.24:
#         facecolor = 'lightyellow'
#     colored_circle = plt.Circle((0.5, 0.5), radius=radius, facecolor=facecolor, edgecolor='grey', linewidth=0.5)
#     axes.add_artist(colored_circle)
# axes.set_aspect(1)
# plt.show()

# 圆环
axes.add_artist(plt.Circle((0.5, 0.5), radius=0.24, facecolor='lightyellow', edgecolor='grey', linewidth=0.5))
axes.add_artist(plt.Circle((0.5, 0.5), radius=0.23, facecolor='white', edgecolor='grey', linewidth=0.5))

# axes.add_artist(plt.Circle((0.5, 0.5), radius=0.3, facecolor='lightblue', edgecolor='grey', linewidth=0.5))
axes.add_artist(plt.Circle((0.5, 0.5), radius=0.001, facecolor='black', edgecolor='black', linewidth=0.01))
axes.set_aspect(1)
plt.show()

# 柱状图
# x = np.arange(0.0, 0.305, 0.003)
# heights = [2 * np.pi * r for r in x]
# width=0.003
# axes.bar(x, heights, width=width, facecolor='lightblue', edgecolor='grey', linewidth=0.5, align='edge')

# axes.plot(x, heights, color='black', linewidth=1)

# # 隐藏Y轴
# frame = plt.gca()
# frame.axes.get_yaxis().set_visible(False)
# # 关闭坐标刻度
# axes.set_xticklabels([])

# plt.legend()
# plt.show()
