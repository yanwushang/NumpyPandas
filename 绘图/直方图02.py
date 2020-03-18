#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as py
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")
x = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
z = [34, 56, 78, 15, 65, 54, 15, 23, 35, 42, 67, 56]
y = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
print(len(x), len(y), len(z))
py.figure(figsize=(20, 8), dpi=80)

py.bar(range(len(x)), z, width=1)
# 调整x轴的位置，使其向前移动0.5个单位
xticks = [i - 0.5 for i in range(len(x) + 1)]
_x = x + [150]
py.xticks(xticks, _x)

py.grid(alpha=0.3)
py.show()
py.savefig('./直方图02.png')
