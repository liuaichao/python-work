# -*- coding:utf-8 -*-
#导入os包
from os import listdir
#导入sklearn封装好的k近邻算法包
from sklearn.neighbors import KNeighborsClassifier
#导入numpy包
import numpy as np
#导入pandas包
import pandas as pd
#导入matplotlib包
import matplotlib.pyplot as plt
#定义函数
# 该函数的功能事将32x32的二进制图像矩阵转化为1x1024一阶数组
def img_vector(filename):
    #将数据读取出来
    data = pd.read_table(filename,header=None,sep='\t')
    # print(data)
    #生成一个1x1024，以0填充的数组
    re_data = np.zeros((1,1024))
    #print(data)
    #把data的值取出来，变成一个32行，1列的矩阵
    data = data.values
    # print(data)

    # data = np.array(data)
    # print(data[0])
    #利用双重循环，取出原数据的数据，挨个填到re_data这个1x1024的矩阵中
    for i in range(32):
        line_data = data[i]
        for j in range(32):
            #将re_data中的数据替换成data的数据
            re_data[0,32*i+j] = int(line_data[0][j])
    # print(re_data[0])
    #将转化完成的数据作为函数的返回值
    return re_data

#定义函数
#因为文件的名字就是文件内容对应的数字，所以解析文件名获取数字
def wenjian(filename):
    #得到文件名列表
    filelist = listdir(filename)
    # print(filelist)
    #创建一个空列表
    datas = []
    #利用获取的文件名列表进行循环
    for i in filelist:
        #拼接文件路径
        filena = ".\\trainingDigits\\"+i
        #引用img_vector()函数，把拼接的文件名带入
        data = img_vector(filena)[0]
        #将获取的转化完成的矩阵全部添加到datats中
        datas.append(data)
    #创建空列表
    digname = []
    #利用获取的文件名列表进行循环
    for name in filelist:
        #对文件名的字符串进行分割，‘_’前面的是其对应的数字，将其取出
        name_x = name.split('_')[0]
        #将数字名称全部添加到digname中
        digname.append(name_x)
    #将digname，datas作为函数的返回值返回
    return digname,datas

#绘图函数，进行折线图绘制
def draw(x_l, y_l):
    #创建折线图，线条颜色为红色，线条坐标为’--‘，宽度为2.0
    plt.plot(x_l, y_l, color='red', linewidth=2.0, linestyle='--')
    #设置标题
    plt.title("准确率随k的变化趋势图")
    #x轴标签
    plt.xlabel("k值")
    #y轴标签
    plt.ylabel("score")
    #设置在每个折线图拐点处显示其对应的y轴数值
    for a, b in zip(x_l, y_l):
        plt.text(a, b, b, ha='center', va='bottom', fontsize=15)
    #显示图像
    plt.show()

#主函数
if __name__ == '__main__':
    #获取测试数据的文件目录
    filelist = listdir(r'.\\testDigits')
    #创建空列表
    name_zhen = []
    #对测试目录的文件名进行字符串分割并取出‘_’前面的数字，并把它添加到name_zhen中
    for x in filelist:
        name_y = x.split('_')[0]
        name_zhen.append(name_y)
    # print(name_zhen)
    #创建空列表
    datas_test = []
    #对测试目录进行字符串拼接，然后调用img_vector函数，将测试数据进行矩阵转换，并一一添加到data_test中
    for li in filelist:
        addr = r'.\\testDigits'+'\\'+li
        data_test = img_vector(addr)
        datas_test.append(data_test[0])

    # if (datas_test[1]==datas_test[2]).all():
    #     print('相同')
    # print(data)
    #调用wenjian函数，训练数据的数字名跟处理过的训练数据矩阵，保存到变量all中
    all = wenjian(r'.\\trainingDigits')
    #将处理过的训练数据转化成 测试数据文件个数*1024的矩阵
    X_data = np.array(all[1]).reshape(len(listdir(r'.\\trainingDigits')),1024)
    # data_test = np.array(data_test)
    #定义图表x轴
    x_l = [5, 6, 7, 8, 9, 10]
    #定义图表y轴
    y_l = []
    #将x轴代表的6个k值进行循环带入
    for m in x_l:
        #调用k近邻算法函数，n_neighbors代表k值
        reg = KNeighborsClassifier(n_neighbors=m)
        #调用knn对象的fit（）方法，传入训练数据跟训练数据对应的标签
        reg.fit(X_data, all[0])
        #调用knn对象的predict（）方法，传入测试数据，返回模型判读出的测试数据的标签
        true = reg.predict(datas_test)
        #声明errornum变量，用于统计错误的个数
        errornum = 0
        #for循环，将模型得出的结果跟正确结果进行比对，统计错误的个数
        for i,j in zip(name_zhen,true):
            if i != j:
                errornum += 1
        print("k值为：%.1f" %(m))
        #根据错误个数与总个数计算获取正确率
        true_v = (len(name_zhen)-errornum) / len(name_zhen)
        #将正确率保留三位有效数字
        true_v = round(true_v, 3)
        print("准确率为%f" %(true_v))
        #将正确率添加到y轴
        y_l.append(true_v)
    #调用绘图函数
    draw(x_l, y_l)
