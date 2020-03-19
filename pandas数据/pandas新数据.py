#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

t = pd.Series([1, 2, 21, 12, 3, 4],index=list('abcdef'))
print(t)
t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=('a','b','c'),columns=list('wxyz'))
print('t1=', t1)

d1={'name':['小黑','小黄'],'sex':['男','女'],'age':[13,23]}
newd1=pd.DataFrame(d1)
print('newd1=',newd1)