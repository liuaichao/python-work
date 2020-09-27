# -*- coding:utf-8 -*-
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
                                                    random_state=3)
pipe = Pipeline([("scaler", MinMaxScaler()), ("svm", SVC())])
pipe.fivt(X_train, y_train)
#网格搜索
param_grid = {"svm__C":[0.001, 0.01, 0.1, 1, 10, 100],
              "svm__gamma":[0.001, 0.01, 0.1, 1, 10, 100]}
grid = GridSearchCV(pipe, param_grid=param_grid, cv=5)
grid.fit(X_train, y_train)
print(grid.score(X_test, y_test))