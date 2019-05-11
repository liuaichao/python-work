# -*- coding:utf-8 -*-
import numpy as np
from functools import reduce
a1 = ['我','你','他','她','他们','我们']
a2 = ['喜欢','想','拥有','练习','讨厌','学习']
a3 = ['豪车','别墅','python','数据分析','金钱','美酒']
arr_1 = np.column_stack(((np.column_stack((np.array(a1),np.array(a2)))),np.array(a3)))
arr_2 = np.column_stack(((np.column_stack((np.array(a1),np.array(a2)))),np.array(a3)))
np.random.shuffle(arr_1)
np.random.shuffle(arr_2)
random_ar = [[True if np.random.rand()>=0.5 else False for i in range(3)] for j in range(6)]
random_ar = np.array(random_ar)
print(arr_1)
print(arr_2)

print(random_ar)
al = np.where(random_ar,arr_1,arr_2)
print(al)
print(reduce(lambda x,y:x+y,al[2]))
