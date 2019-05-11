# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
#数据查重
def search(data):
    index_search = []
    for i in range(len(data)):
        data_z = data[i,:1]
        for j in range(i+1,len(data)):
            if data_z==data[j,:1]:
                index_search.append(j)
    data = np.delete(data,index_search,0)
    return data
#非法字符清洗
def char_clean(data):
    for i in range(len(data)):
        for j in range(5):
            if type(data[i][j])!=int and type(data[i][j])!=float:
                data[i][j] = 0
    data[np.isnan(data.astype(np.float64))]=0#处理空值,需要进行强制转换
    return data
#0值替换成该列平均值
def replace_char(data):
    jun = data.mean(0)
    for i in range(len(data)):
        for j in range(5):
            if data[i][j]==0:
                data[i][j] = jun[j]
    return data
#数据输出
def print_data(data):
    Format_DataFrame = pd.DataFrame(data)
    format_array_print = lambda x:'%u'%x
    Format_DataFrame.applymap(format_array_print)
    print(Format_DataFrame)
data = pd.read_excel(r'c:\Users\THINKPAD\Desktop\数据分析\数据清洗.xlsx')
data = np.array(data,dtype=object)
data = search(data)
data = char_clean(data)
data = replace_char(data)
print_data(data)


