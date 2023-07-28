import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist
import numpy as np

def axis_ticks(start, end, step, withZero=True):
    return [v for v in np.arange(start, end + step, step) if withZero or v != 0]

def axis_lim(start, end):
    return (start - 0.5, end + 0.5)

def drawPlot(xvalue, yvalues, xlim, ylim, xticks, yticks, show_x_ticklabels=True, show_y_ticklabels=True,
             linecolor="blue", linewidth="1", figsize=(9, 6)):
    fig = plt.figure(figsize=figsize)
    # 创建绘图区对象，并添加到画布中
    ax = axisartist.Subplot(fig, 111)
    fig.add_axes(ax)
    # 隐藏绘图区坐标轴
    ax.axis[:].set_visible(False)
    # 添加新的坐标轴x和y
    ax.axis["x"] = ax.new_floating_axis(0, 0)
    ax.axis["y"] = ax.new_floating_axis(1, 0)
    # 坐标轴设置箭头和颜色
    ax.axis["x"].set_axisline_style("-|>", size = 1.0)
    ax.axis["y"].set_axisline_style("-|>", size = 1.0)
    ax.axis["x"].line.set_color("black")
    ax.axis["y"].line.set_color("black")
    # 坐标轴上刻度显示方向
    ax.axis["x"].set_axis_direction("top")
    ax.axis["y"].set_axis_direction("right")

    # 设置x、y坐标轴的范围
    plt.xlim(xlim)
    plt.ylim(ylim)
    # 设置x、y坐标轴的刻度
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    # 是否展示刻度值
    if not show_x_ticklabels:
        ax.set_xticklabels([])
    if not show_y_ticklabels:
        ax.set_yticklabels([])

    ax.tick_params(labelsize=0)

    def has_one_axis(X):
        return (hasattr(X, "ndim") and X.ndim == 1 or isinstance(X, list) and not hasattr(X[0], "__len__"))

    # 绘制图形
    if has_one_axis(yvalues):
        plt.plot(xvalue, yvalues, color=linecolor, linewidth=linewidth)
    else:
        for yvalue in yvalues: 
            plt.plot(xvalue, yvalue, color=linecolor, linewidth=linewidth)
    plt.show()

    

