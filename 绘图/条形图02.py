#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as py
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")

x = ["战狼", '速度于激情', '功夫瑜伽', '西游伏魔片', '变形金刚3', '最后的其实', '摔跤吧！爸爸', '加勒比海盗']
y1 = [34, 56, 78, 15, 65, 54, 15, 23]
y2 = [23, 45, 26, 75, 46, 67, 52, 65]
y3 = [42, 53, 34, 45, 42, 68, 57, 79]
x1 = list(range(len(x)))
x2 = [i + 0.2 for i in x1]
x3 = [i + 0.2 * 2 for i in x1]
py.bar(x1, y1, width=0.2, color='red', label='3月')
py.bar(x2, y2, width=0.2, color='orange', label='4月')
py.bar(x3, y3, width=0.2, color='black', label='5月')
py.xticks(x2, x, fontproperties=my_font, rotation=45)
py.xlabel("电影名", fontproperties=my_font)
py.ylabel("票房 单位：亿元", fontproperties=my_font)
py.title("三年票房对比图", fontproperties=my_font)
py.legend(prop=my_font)
py.show()
py.savefig('./多条行图.png')
