# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.svm import SVR,SVC
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('./traffic_data.txt', names=['week', 'time', 'opponent',
                                                'is_start', 'car_num'], index_col=None)
print(data)

data = data.iloc[0:10000]
data = pd.get_dummies(data)
a = data.columns
data = np.array(data)

X = data[:,1:308]
X = pd.DataFrame(X, columns=a[1:1000])
X.to_csv('./01.csv')
print(X)
y = data[:, 0]

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=1, train_size=0.7)

# params = {'kernel': 'rbf', 'C':10}
# svr = SVC(**params)
# svr.fit(X_train, y_train)
# print(svr.score(X_test, y_test))

# dt_tree = DecisionTreeRegressor(max_depth=6)
# dt_tree.fit(X_train, y_train)
# print(dt_tree.score(X_test, y_test))



