#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as py
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc")

x = ["战狼", '速度于激情', '功夫瑜伽', '西游伏魔片', '变形金刚3', '最后的其实', '摔跤吧！爸爸', '加勒比海盗']
y = [34, 56, 78, 15, 65, 54, 15, 23]
py.figure(figsize=(20, 8), dpi=80)
#绘制条形图
py.bar(x,y,width=0.3,color='red')
#设置字符串到x轴
py.xticks(range(len(x)),x,fontproperties=my_font,rotation=45)
py.xlabel('电影名称',fontproperties=my_font)
py.ylabel('票房 单位：亿元',fontproperties=my_font)
py.title('电影票房图',fontproperties=my_font)
# 绘制哼的条形图
# py.barh(x, y,height=0.3)
# py.yticks(range(len(x)),x,fontproperties=my_font,rotation=45)

py.grid(alpha=0.2)
py.show()
py.savefig('./条形图.png')
