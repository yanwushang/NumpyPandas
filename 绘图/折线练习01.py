#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as py, font_manager
#因为会转义所以需要加一个r
my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")

# 添加中文应用

y1 = [1, 2, 1, 0, 2, 4, 3, 5, 6, 4, 5, 2, 3, 1, 4, 5, 1, 1, 2, 1]
y2 = [1, 3, 3, 3, 2, 2, 3, 4, 5, 2, 4, 2, 1, 2, 3, 3, 4, 5, 5, 3]
x = range(11, 31)
# 设置图片大小
py.figure(figsize=(15, 8), dpi=80)
py.plot(x, y1, label='自己',color="black")
py.plot(x, y2, label='同桌',color="red")

# 填充横轴纵轴，主题，中文
x1_tick = ['{}岁'.format(i) for i in x]
py.xticks(x, x1_tick,fontproperties=my_font)
py.xlabel('年龄',color='red',fontproperties=my_font)
py.ylabel('数量',color='green',fontproperties=my_font)
py.title('11岁后每年交朋友的数量图',fontproperties=my_font)
py.yticks(range(0, 9))
# 设置网格线
py.grid(alpha=0.2)

# 添加图例，那个线是那个人的
py.legend(prop=my_font,loc="upper left")


py.show()
py.savefig('./02_1.png')
