#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np


def fill_ndarray(self):
    # 遍历每一列
    for i in range(t1.shape[1]):
        # 当前的列
        temp_col = t1[:, i]
        nan_num = np.count_nonzero(temp_col != temp_col)
        # nan不为0，说明当前列中有数为nan
        if nan_num != 0:
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # 选中当前为nan的位置，把该列的均值赋给它
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
            print(('我起作用了'))
    return t1


t1 = np.arange(24).reshape((4, 6)).astype('float')
t1[2, 3:] = np.nan
print('t1=', t1)
t2 = fill_ndarray(t1)
print('t2=', t2)
