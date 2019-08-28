# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from pandas.plotting import scatter_matrix
from sklearn.neighbors import KNeighborsClassifier
iris_dataset = load_iris()
# print(iris_dataset)
#数据打乱并分出训练数据跟测试数据
X_train,X_test,y_train,y_test = train_test_split(iris_dataset['data'],
                                                 iris_dataset['target'],random_state=0)
#绘制散点图
iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
grr = scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15),marker='o',
                        hist_kwds={'bins':20}, s=60, alpha=0.8)
plt.show()
# print(iris_dataframe)
#构建模型k近邻算法
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train,y_train)#传入训练模型
#做出预测
X_new = np.array([[5, 2.9, 1, 0.2]])#sklearn必须传入二维数组
prediction = knn.predict(X_new)
print('鸢尾花的品种为：{}'.format(iris_dataset['target_names'][prediction][0]))
#评估模型
y_pred = knn.predict(X_test)
print('模型评估准确率为：{:.0f}%'.format(100*np.mean(y_pred==y_test)))
