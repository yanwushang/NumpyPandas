#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

t = pd.DataFrame(np.arange(20,26).reshape(2,3),index=list('ab'),columns=list('jkl'))
print(t)
t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=('a','b','c'),columns=list('wxyz'))
print('t1=', t1)
# 按行合并
t2=t1.join(t)
print(t2)
print('*'*60)
t1=pd.DataFrame(np.ones((2,4)),columns=list('abcd'),index=list('AB'))
print('t1=',t1)
t2=pd.DataFrame(np.zeros((3,3)),columns=list('xyz'),index=list('ABC'))
t3=pd.DataFrame(np.zeros((3,3)),columns=list('fax'))
t4=pd.DataFrame(np.arange(9).reshape((3,3)),columns=list('fax'))
print('t2=',t2)
print('往t1里加t2',t1.join(t2))
print('往t2里加t1',t2.join(t1))
print('*'*60)
# 按列合并
print('t3=',t3)
print(t1.merge(t3,on='a'))
t3.loc[1,'a']=1
print(t1.merge(t3,on='a'))
print(t1.merge(t4,on='a'))