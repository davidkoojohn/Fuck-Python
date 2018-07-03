# coding=utf-8

"""
输入半径计算圆的周长和面积
"""

import math

radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2

print('perimeter: %.2f' % perimeter)
print('area: %.2f' % area)
