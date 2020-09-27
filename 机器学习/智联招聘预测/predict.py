# -*- coding:utf-8 -*-

import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier#随机森林
from sklearn.preprocessing import LabelEncoder#标注
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.cluster import KMeans#k聚类
import numpy as np
import random
def do_predict(job_src, gs_type, wk_need, wk_experience, wk_place):
    data = pd.read_csv(job_src)
    data_X = data.loc[:, ['公司类型', '工作要求', '工作经验', '工作地点']]#选出相关的特征

    data_result_a = data.loc[:, '职位月薪']#监督学习分类目标
    data_result = data_result_a.value_counts()#一维数组去重series
    # print(data_result)
    #构建薪资分类结果对照字典
    result_dict = {}
    for i,j in zip(range(len(data_result)), data_result.index):#把薪资编码
        result_dict[i] = j

    y = []
    result_new = {}
    for key,val in result_dict.items():#把键值对换
        result_new[val]=key
    # print(result_new)
    for i in data_result_a:
        y.append(result_new[i])
    # print(y)
    #标记编码
    compay_type = [i for i in data_X.loc[:, '公司类型'].value_counts().index]#记录一维数据格式的值的出现个数
    work_need = [i for i in data_X.loc[:, '工作要求'].value_counts().index]
    work_experience = [i for i in data_X.loc[:, '工作经验'].value_counts().index]
    work_place = [i for i in data_X.loc[:, '工作地点'].value_counts().index]
    label_encoder = LabelEncoder()#声明标记函数
    input_classes = compay_type + work_experience + work_need + work_place
    label_encoder.fit(input_classes)#给每个变量标记标识

    data_X = data_X.values#dataframe转化为二维数组
    # print(data_X.shape)
    for i,j in zip(range(data_X.shape[0]),data_X):#选出行数
        a = label_encoder.transform(j)#查找j所对应的编码
        # print(a)
        data_X[i] = a
    X = data_X
    # print(X)
    # print(y)

    # X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    data_return = my_train_test_split(X, y)
    X_train = data_return[0]
    X_test = data_return[1]
    y_train = data_return[2]
    y_test = data_return[3]
    #随机森林算法进行薪资预测
    random_tree = RandomForestClassifier(n_estimators=400, random_state=2, max_features=4)#决策树，最大深度为4
    random_tree.fit(X_train, y_train)
    print(random_tree.score(X_test, y_test))

    input_data = []
    input_data.append(gs_type)
    input_data.append(wk_need)
    input_data.append(wk_experience)
    input_data.append(wk_place)

    input_data = label_encoder.transform(input_data)#对特征值编码
    input_data = np.array(input_data).reshape(1, len(input_data))#一维数组换为二维数组
    result = random_tree.predict(input_data)
    print("估计薪资：")
    print(result_dict[result[0]])

    #k均值聚类，进行划分，选取相近公司
    kmeans = KMeans(n_clusters=int(len(data_result)/15))
    kmeans.fit(X)#模型拟合
    company_predict = kmeans.predict(input_data)[0]
    shunxu = []
    for i,j in zip(range(len(kmeans.labels_)), kmeans.labels_):
        if j==company_predict:
            shunxu.append(i)
    # shunxu = shunxu[:10]#选出前十个
    company_ten = data.iloc[shunxu,[0,1,2,3,4,5,6,7,8,9,10]]
    # company_ten.index = company_ten.iloc[:,'公司名称']
    # del company_ten['公司名称']
    print("推荐公司如下:")
    data = company_ten.iloc[:, [0,1,2,3,4,5,6,7,8,9,10]]
    data = data.values
    print(data)
    #梯度提升回归树
    # gbrt = GradientBoostingClassifier(random_state=0, n_estimators=300, max_depth=3,
    #                                   learning_rate=0.01)
    # gbrt.fit(X_train, y_train)
    # print(gbrt.score(X_test, y_test))
    #线性支持向量机
    # linear_svm = LinearSVC()
    # linear_svm.fit(X_train, y_train)
    #
    # print(linear_svm.score(X_test, y_test))

def my_train_test_split(X, y):
    y = np.array(y)  # 把列表变为数组
    X_len = X.shape[0]
    X_train_a = int(X_len * 0.7)
    resultlist = random.sample(range(0, X_len), X_train_a)
    m = []
    n = []
    X_train = np.empty((len(resultlist), 4))  # 训练集
    X_test = np.empty((X_len - len(resultlist), 4))  # 测试集
    v = 0
    c = 0
    for i, j in zip(range(X_len), X):
        if i in resultlist:
            m.append(i)
            X_train[v] = j
            v = v + 1
        else:
            n.append(i)
            X_test[c] = j
            c = c + 1
    y_train = y[m]
    y_test = y[n]
    return [X_train, X_test, y_train, y_test]

if __name__ == '__main__':

    gs_type = input("请输入公司类型:")
    wk_need = input("请输入工作要求:")
    wk_experience = input("请输入工作经验:")
    wk_place = input("请输入工作地点:")
    job_type = input("请输入工作类型:")
    #文件路径
    d_dict = {'Android':'./data/Android.csv', '产品经理':'./data/chanpinjingli.csv',
              '贷款':'./data/daikuan.csv', '电气工程师':'./data/dianqigongchengshi.csv',
              '电子':'./data/dianzi.csv', '电子工程师':'./data/dianzigongchengshi.csv',
              '房地产':'./data/fangdichan.csv', '风控':'./data/fengkong.csv',
              'hadoop':'./data/hadoop.csv', 'java':'./data/java.csv',
              '交易员':'./data/jiaoyiyuan.csv', '美工':'./data/meigong.csv',
              'node.js':'./data/node.js.csv', 'php':'./data/php.csv',
              'python':'./data/python.csv', '区块链':'./data/qukuailian.csv',
              '人工智能':'./data/rengongzhineng.csv', '深度学习':'./data/shenduxuexi.csv',
              '数据分析师':'./data/shujufenxishi.csv', '数据架构':'./data/shujujiagou.csv',
              '数据开发':'./data/shujukaifa.csv', '算法工程师':'./data/suanfagongchengshi.csv',
              '投资经理':'./data/touzijingli.csv', 'UI设计':'./data/uisheji.csv',
              'web前端':'./data/web_qianduan.csv', '银行柜员':'./data/yinhangguiyuan.csv',
              '运营专员':'./data/yunyingzhuanyuan.csv', '证券':'./data/zhengquan.csv',
              }
    job_src = d_dict[job_type]
    do_predict(job_src, gs_type, wk_need, wk_experience, wk_place)