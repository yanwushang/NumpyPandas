#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as py
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")
y_3 = [12, 13, 14, 5, 17, 14, 24, 25, 14, 25, 6, 7, 12, 13, 14, 5, 17, 14, 24, 25, 14, 25, 6, 7, 24, 24, 25, 26, 31, 32,
       29]
y_10 = [26, 31, 32, 29, 7, 24, 24, 25, 26, 24, 25, 14, 25, 6, 7, 12, 13, 25, 6, 7, 12, 13, 14, 25, 6, 7, 12, 13, 14, 5,
        6]
x_3 = range(1, 32)
x_10 = range(51, 82)
py.figure(figsize=(20, 8), dpi=80)
py.scatter(x_3, y_3, label='3月')
py.scatter(x_10, y_10, label="10月")
new_x = list(x_3) + list(x_10)
new_ticklables =["3月{}日".format(i) for i in x_3]
new_ticklables +=["10月{}日".format(i - 50) for i in x_10]
py.xticks(new_x[::3], new_ticklables[::3], rotation= 45, fontproperties=my_font)

py.legend(loc="upper left",prop=my_font)
py.xlabel("时间",fontproperties=my_font)
py.ylabel("温度")
py.title("温度时间散点图",fontproperties=my_font)

py.show()
py.savefig('./散点.png')
