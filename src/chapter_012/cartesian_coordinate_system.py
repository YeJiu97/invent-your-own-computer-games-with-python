'''
笛卡尔坐标系，也被称为直角坐标系，是数学中的一种正交坐标系。这个系统是由法国数学家勒内·笛卡尔引入的。
它的基本构成是两条相交于原点的数轴，这两条数轴一起构成了一个平面仿射坐标系。如果这两条数轴上的度量单位相等，则称此仿射坐标系为笛卡尔坐标系。
当两条数轴互相垂直时，我们便称之为笛卡尔直角坐标系；否则，它就被称为笛卡尔斜角坐标系。二维的直角坐标系通常由两个互相垂直的坐标轴设定，分别称为x轴和y轴。
'''

import matplotlib.pyplot as plt
import numpy as np

# 创建一个空的图形
fig = plt.figure()

# 添加一个子图，111代表的是1行1列的第1个图
ax = fig.add_subplot(111)

# 生成x和y的值，这里我们生成[0, 1]范围内的等差数列作为示例
x = np.arange(0, 1, 0.01)
y = np.sin(2 * np.pi * x)

# 绘制折线图，其中x是横轴，y是纵轴
ax.plot(x, y)

# 设置x轴和y轴的标签
ax.set_xlabel('X')
ax.set_ylabel('Y')

# 设置标题
ax.set_title('A simple line plot in Cartesian coordinates')

# 显示图形
plt.show()