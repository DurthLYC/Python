import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

newroman = FontProperties(fname=r"Times New Roman.ttf", size=14)    # 自定义字体，导入外部字体库并设置字体大小
plt.rcParams['font.sans-serif'] = ['Times New Roman']               # 直接设置系统内置字体（整张图默认都使用该子图）
mpl.rcParams['axes.unicode_minus'] = False                          # 正常显示符号，当图片存在中文时一定要加这一行
mpl.rcParams['xtick.direction'] = 'in'                              # x轴刻度向内
mpl.rcParams['ytick.direction'] = 'in'                              # y轴刻度向内

fig = plt.figure(figsize=(4, 3), dpi=600)                           # 画布大小
ax = fig.add_subplot(111)                                           # 若希望多图排列显示

plt.grid(True)                                                      # 图中网格
ax.grid(color='black', linestyle='--', linewidth=1.0, alpha=0.1)
ax.yaxis.grid(True, which='minor')
ax.xaxis.grid(True, which='minor')

ax.spines['bottom'].set_linewidth(1.5)                              # 坐标系边缘格线粗细（略粗与内部网格好看些）
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

data = np.loadtxt('Mydata.txt', skiprows=1, usecols=[2, 3, 4, 5, 6, 7, 8, 9, 10])   # 读取数据

lineNum = 3                     # 线条数量
lc = ['r', 'b', 'k']            # 各线条颜色
lt = ['-v', '--', '-o']         # 各线条线型

for i in range(lineNum):
    plt.plot(np.arange(1, 9, 1), data[:, i], lt[i], c=[i], linewidth=2, markersize=20)      # 画线

plt.legend(['line1', 'line2', 'line3'], loc='best', frameon=True, edgecolor='k')            # 增加图例

plt.xlabel(u'xlable/unit', fontproperties=newroman)
plt.ylabel(u'ylable/unit', fontproperties=newroman)

plt.xticks(np.arange(1, 9, 1), fontproperties=newroman)
plt.yticks(fontproperties=newroman)

plt.show()
# plt.savefig(u"MyPic.png", format='png', dpi=300, bbox_inches='tight')                     # 若想存储图片
