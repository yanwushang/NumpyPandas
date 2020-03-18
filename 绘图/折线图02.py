#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from matplotlib import pyplot as py, font_manager

# 设置字体
my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
# 调整图片现实大小
py.figure(figsize=(20, 8), dpi=80)
# 把1-120的下刻度先换为从10几分，11点几分，
py.plot(x,y)
x1_ticks = ['10点{}分'.format(i) for i in range(60)]
x1_ticks += ['11点{}分'.format(i) for i in range(60)]
py.xticks(list(x)[::3], x1_ticks[::3], rotation=45, fontproperties=my_font)
#fontproperties=my_font)
# 添加表的描述信息，如图的名字，横轴，纵轴各代表是什么意思
py.xlabel('时间 单位（分钟）', fontproperties=my_font)
py.ylabel('温度 单位（摄氏度）', fontproperties=my_font)
py.title('10点到12点每分钟气温变化情况', fontproperties=my_font)
py.savefig("./02.png")
py.show()
