#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import random
t1=np.random.rand(2,5)
print("t1=",t1)
print('*'*60)
t2=np.random.randn(2,4)
print("t2=",t2)
print('*'*60)
t3=np.random.randint(10,20,(2,5))
print("t3=",t3)
print('*'*60)
t4=np.random.uniform(5,10,(2,5))
print("t4=",t4)
print('*'*60)
t5=np.random.normal(7,2,(3,4))
print("t5=",t5)
print('*'*60)
np.random.seed(3)
t6=np.random.randint(0,20,(3,4))
print("t6=",t6)