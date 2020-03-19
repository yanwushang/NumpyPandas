#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
t = pd.DataFrame(np.arange(20).reshape(5,4), columns=list('wxyz'))
df = pd.DataFrame(t)
print('t=',t)
t.iloc[[1,3],[0,2]]=np.nan
print('有缺失数值的t',t)
t2=pd.isnull(t)
print('t2=',t2)
t2=t2.dropna(how='any',inplace=True)
print('t3=',t2)
# t2.fillna(100)


