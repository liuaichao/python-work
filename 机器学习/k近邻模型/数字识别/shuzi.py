# -*- coding:utf-8 -*-
from os import listdir

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
#定义函数，将32x32的二进制图像矩阵转化为1x1024
def img_vector(filename):
    data = pd.read_table(filename,header=None,sep='\t')
    # print(data)
    re_data = np.zeros((1,1024))
    # print(data)
    data = data.values
    # print(data)
    data = np.array(data)
    # print(data[0])
    for i in range(32):
        line_data = data[i]
        for j in range(32):
            re_data[0,32*i+j] = int(line_data[0][j])
    # print(re_data[0])
    return re_data


#解析文件名获取数字
def wenjian(filename):
    filelist = listdir(filename)
    # print(filelist)
    datas = []
    for i in filelist:
        filena = "C:\\Users\\THINKPAD\\Desktop\\机器学习实战\\Ch02\\trainingDigits\\"+i
        data = img_vector(filena)[0]
        datas.append(data)
    digname = []
    for name in filelist:
        name_x = name.split('_')[0]
        digname.append(name_x)
    return digname,datas
filelist = listdir(r'C:\Users\THINKPAD\Desktop\机器学习实战\Ch02\testDigits')
datas_test = []
for li in filelist:
    addr = r'C:\Users\THINKPAD\Desktop\机器学习实战\Ch02\testDigits'+'\\'+li
    data_test = img_vector(addr)
    datas_test.append(data_test[0])

if (datas_test[1]==datas_test[2]).all():
    print('相同')
# print(data)
all = wenjian(r'C:\Users\THINKPAD\Desktop\机器学习实战\Ch02\trainingDigits')
X_data = np.array(all[1]).reshape(1934,1024)
# data_test = np.array(data_test)
reg = KNeighborsClassifier(n_neighbors=3)
reg.fit(X_data, all[0])
print(reg.predict(datas_test))
