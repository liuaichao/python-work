# -*- coding:utf-8 -*-
from 爬虫.Mysql_demo import Mysql_demo
import numpy as np
import pandas as pd
# my = Mysql_demo('47.105.142.252','anonymous','lac981215lac','test')
# sql = 'select * from spider_guazi'
# data = my.search(sql)
# col = ['id','name1','name2','name','times','gongli','types','price/万','xinche']
# data = np.array(data,dtype=object)
# data_dataframe = pd.DataFrame(data, columns=col)
# data_dataframe = data_dataframe.head()
# data_dataframe.to_csv('./guazi.csv')

# data = pd.read_csv('./guazi.csv',index_col='id')
# data.index.name = '列'
# data.name = '瓜子二手车'
# data.columns.name = '行'
# # data['host'] = ['qw','qw','qw','qw','qw']
# # del data['host']
# data_series = pd.Series(['100'], index=['xinche'])
# # print(data_series)
#
# print(data.sort_index())
left1 = pd.DataFrame({'key':['a','b','a','a','b','c'],'value':range(6)})

right1 = pd.DataFrame({'group_val':[3.5,7]},index=['a','b'])
print(pd.merge(left1, right1, left_on='key', right_index=True, sort=False))
