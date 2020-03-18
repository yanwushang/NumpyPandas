#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
# 取0-23
t1=range(24)
#生成一行的元祖
result=np.array(t1)
print(t1)
print((result))
print("*"*60)
# 生成4行6列的二维元祖
t2=result.reshape(4,6)
print("t2=",t2)
print("*"*60)
#生成两组三行4列的三维元祖
t3=result.reshape(2,3,4)
print("t3=",t3)
print("*"*60)
#给全体数组加/减/乘除一个数
t4=t2+2
print("t4=",t4)
print("*"*60)
num=np.array(range(6))
# 给二维表中加上一行数值，每个位置相对应
t5=t2+num
print("t5=",t5)
print("*"*60)
num=np.array(range(3))
num1=num.reshape(3,1)
print("num1=",num1)
# 给表中加上一列数值，每个位置相对应
t6=t3+num1
print("t6=",t6)
print("*"*60)