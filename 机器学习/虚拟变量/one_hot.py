# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#处理数据
names=['age', 'workclass', 'fnlwgt', 'education',  'education-num',
           'marital-status', 'occupation', 'relationship', 'race', 'gender',
           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
           'income']
data = pd.read_csv('./adult.csv', header=None, index_col=False, names=names)
# print(data.head())
# print(data.loc[:, 9].value_counts())
data = pd.get_dummies(data)
# print(data.columns)
data_1 = data.loc[:, :'native-country_ Yugoslavia']
X = data_1.values
y = data['income_ >50K'].values

#logistic算法分类
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
print(logreg.score(X_test, y_test))
