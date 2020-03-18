#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
t1=np.array(range(10))
t2=np.array(range(30,40))
print("t1=",t1)
print("t2=",t2)
t3=t1.reshape(2,5)
t4=t2.reshape(2,5)
print("t3=",t3)
print("t4=",t4)
print('*'*60)
#竖直拼接,只要列数相同就可以
t5=np.vstack((t3,t4))
print("t5=",t5)
print('*'*60)
# 水平拼接，只要行数相等就可以
t6=np.hstack((t3,t4))
print("t6=",t6)
print('*'*60)
