from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# 正态分布
x = np.linspace(0, 8, 10000)
y1 = stats.norm.pdf(x, 4, 1)
y2 = stats.norm.cdf(x, 4, 1)

plt.plot(x, y1, color="red")
plt.plot(x, y2, color="blue")

frame = plt.gca()
frame.axes.get_yaxis().set_visible(False)
plt.show()