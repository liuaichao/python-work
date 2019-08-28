# -*- coding:utf-8 -*-
import pandas as pd

data = pd.read_csv('./data_shenzhen.csv')
print(data)
data.drop_duplicates()
data = data[:15001]
print(data)
data.to_csv('./data_beijing_q.csv')
