# -*- coding:utf-8 -*-
import mglearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X,y = mglearn.datasets.load_extended_boston()
# print(X.shape)
# print(y)
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0)
lr = LinearRegression()
lr.fit(X_train,y_train)
print(lr.score(X_train, y_train))
print(lr.score(X_test, y_test))
print(lr.coef_)
print(lr.intercept_)