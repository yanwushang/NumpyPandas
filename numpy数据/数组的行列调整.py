#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
t1=np.array(range(25))
t2=t1.reshape(5,5)
print("t2=",t2)
t2[[1,2],:]=t2[[2,1],:]
print("调整第二行和第三行后的t2=",t2)
t2[:,[1,3]]=t2[:,[3,1]]
print("调整第二列和第四列后的t2=",t2)
#创建全为0或1的数组
t3=np.zeros((4,1))
t4=np.ones((4,1))
print("t3=",t3)
print("t4=",t4)
#创建对角线为1的正方形数组（方阵）
t5=np.eye(5)
print("t5=",t5)