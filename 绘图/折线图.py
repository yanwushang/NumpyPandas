#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [12, 13, 14, 5, 17, 14, 24, 25, 14, 25, 6, 7]
plt.plot(x, y)
# 重新定义图形的高，宽，大小
# 调整刻度，可以用xticks 函数，传入想要的参数即可
#  如传入newtable=[1/2 for i in range(4,49],plt.xtict(newtable),就是从4-49，每0。5一个刻度
#  plt.xtict(newtable[::3],就是从4-49，每3个0。5取一个刻度
plt.xticks(range(2,26,2))
plt.yticks(range(5,35,2))
plt.savefig('./01.png')
plt.show()

