# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
#加载数据
car_data = pd.read_csv('./car.data.txt', names=['buying', 'maint','doors', 'persons',
                                                'lug_boot', 'safety', 'result'], index_col=False)

#标记编码
# label_encoder = LabelEncoder()
# input_classes = ['2', '3', '4', '5more', 'vhigh', 'high', 'med', 'low', 'small',
#                  'med', 'big', 'unacc', 'acc', 'good', 'vgood', 'more']
# label_encoder.fit(input_classes)
# data = np.empty((1728, 7))
#
# for i in range(car_data.shape[0]):
#     data1 = label_encoder.transform(car_data.iloc[i])
#     data[i] = data1
# X = data[:, :-1]
# y = data[:, -1]
#采用one-hot编码
one_hot = pd.get_dummies(car_data)
# print(one_hot.shape)
X = one_hot.iloc[:, :-3].values
y_g = car_data.iloc[:, -1].values
# print(X.shape)
y = []
# print(X)
for i in y_g:
    if i=='unacc':
       a = 0
    elif i=='acc':
       a = 1
    elif i=='good':
       a = 2
    elif i == 'vgood':
        a = 3
    y.append(a)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# print(X_train.shape)
# print(X_test.shape)
#进行交叉验证
re_tree = RandomForestClassifier(random_state=1)
# re_tree.fit(X_train, y_train)
# print(re_tree.score(X_test, y_test))
#进行交叉网格验证
param_grid = {'n_estimators':[50*i for i in range(1, 10)], 'max_depth':[i for i in range(3,10)]}
print(param_grid)
grid_search = GridSearchCV(re_tree, param_grid, cv=5)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_)
print(grid_search.best_score_)
# kfold = KFold(n_splits=5, shuffle=True, random_state=1)
# logreg = cross_val_score(logreg, X, y, cv=kfold)
# print(logreg)
# log = LogisticRegression()
# log.fit(X_train, y_train)
# print(log.score(X_test, y_test))