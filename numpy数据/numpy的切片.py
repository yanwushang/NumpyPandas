#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

x = range(100)
t1 = np.array(x)
# 生成4列25行的二维数组
t2 = t1.reshape(25, 4)
print(x)
print("t1=", t1)
print("*" * 60)
print("t2=", t2)
print("*" * 60)
# 取第二行数值
t3 = t2[2]
print("t3=", t3)
print("*" * 60)
# 取第二列数值
t4 = t2[:, 2]
print("t4=", t4)
print("*" * 60)
print("取连续多行", t2[2:5])
print("取不连续多行", t2[[2, 4, 7]])
print('取多列', t2[:, [2, 3]])
# 取第10-20行的第2-3列
print('第10-20行的第2-3列', t2[10:20, 1:3])
# 取多个不相邻的点
print("取多个不相邻的点=", t2[[0, 1, 5, 7, 10], [0, 3, 2, 3, 1]])
