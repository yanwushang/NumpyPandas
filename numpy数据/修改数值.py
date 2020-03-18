#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

x = range(25)
t1 = np.array(x)
# 生成4列25行的二维数组
t2 = t1.reshape(5, 5)
print("t1=", t1)
print("t2=", t2)
print("*" * 60)
t2[2:4, 1:3] = 4
print("t2=", t2)
t2[t2 < 10] = 30
print("t2=", t2)
t3 = np.where(t2 <= 20, 0, 15)
print("t3=", t3)
t4=t2.clip(10,17)
print("t4=", t4)

