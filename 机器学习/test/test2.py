# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from os import listdir

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#定义函数，将32x32的二进制图像矩阵转化为1x1024
def img_vector(filename):
    data = pd.read_table(filename,header=None,sep='\t')
    # print(data)
    re_data = np.zeros((1,1024))
    # print(data)
    data = data.values
    # print(data)
    data = np.array(data)
    # print(data[1])
    a = 0
    b = 0
    for i in range(32):

        line_data = data[i]
        for j in range(32):
            a += 1
            if a==1024:
                b += 1
            # print("a:{0}".format(a))
            # print("b:{0}".format(b))
            re_data[0,32*i+j] = int(line_data[0][j])
    # print(re_data[0])
    return re_data


#解析文件名获取数字
def wenjian(filename):
    filelist = listdir(filename)
    print(filelist)
    datas = []
    for i in filelist:
        filena = ".\\trainingDigits\\"+i
        data = img_vector(filena)[0]
        datas.append(data)
    digname = []
    for name in filelist:
        name_x = name.split('_')[0]
        digname.append(name_x)
    return digname,datas
filelist = listdir(r'.\\testDigits')
name_zhen = []
for x in filelist:
    name_y = x.split('_')[0]
    name_zhen.append(name_y)
# print(name_zhen)
datas_test = []
for li in filelist:
    addr = r'.\\testDigits'+'\\'+li
    data_test = img_vector(addr)
    datas_test.append(data_test[0])

if (datas_test[1]==datas_test[2]).all():
    print('相同')
# print(data)
all = wenjian(r'.\\trainingDigits')
X_data = np.array(all[1]).reshape(1934,1024)
# data_test = np.array(data_test)
#x轴
x_l = [5, 6, 7, 8, 9, 10]
#y轴
y_l = []
for m in x_l:
    reg = KNeighborsClassifier(n_neighbors=m)
    reg.fit(X_data, all[0])
    true = reg.predict(datas_test)
    errornum = 0
    for i,j in zip(name_zhen,true):
        if i != j:
            errornum += 1
    print("k值为：%.1f" %(m))
    true_v = (len(name_zhen)-errornum) / len(name_zhen)
    true_v = round(true_v, 3)
    print("准确率为%f" %(true_v))
    y_l.append(true_v)
# print(y_l)
#绘图
plt.plot(x_l,y_l,color='red',linewidth=2.0,linestyle='--')
plt.title("准确率随k的变化趋势图")
plt.xlabel("k值")
plt.ylabel("score")
for a, b in zip(x_l, y_l):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=15)

plt.legend()
plt.show()