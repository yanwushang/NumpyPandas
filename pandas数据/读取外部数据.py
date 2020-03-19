#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv('../dogNames2.csv')
print(df.head())
print('*' * 60)
print(df.info())
print('*' * 60)
# 排序的方法
df.sort_values(by='Count_AnimalName', ascending=False)
print(df.head(5))
# 取前20行
print('*' * 60)
print(df[:20])
# 取前20行中的Row_Labels
print('*' * 60)
print(df[:20]['Row_Labels'])
print(df[(800 < df['Count_AnimalName']) & (df['Count_AnimalName'] < 1000)])
