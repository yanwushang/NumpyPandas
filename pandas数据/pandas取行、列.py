#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

t = pd.DataFrame(np.arange(200).reshape(50, 4), columns=list('wxyz'))
df = pd.DataFrame(t)
print('t=', t)
print('*' * 60)
# print(df.shape(t))
print(t.columns)
print('*' * 60)
print(t.shape)
print(t.dtypes)
print(t.ndim)
print('前四行', t.head(4))
print('行数、列数、索引等', t.info())
print('*' * 60)
print(t.loc[5:10,('w','y')])
print('*' * 60)
print(t.loc[:, 'y'])
print(t.iloc[1,:])
print(t.iloc[1:8,[0,3]])
#重新赋值
t.iloc[1:8,[3]]=np.nan
print(t.iloc[1:10,[0,3]])
#处理缺失数据nan/0


