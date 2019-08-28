# -*- coding:utf-8 -*-
from sklearn.linear_model import Ridge
import mglearn
from sklearn.model_selection import train_test_split
X,y = mglearn.datasets.load_extended_boston()
# print(X.shape)
# print(y)
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0)

ridge = Ridge(alpha=1).fit(X_train,y_train)
print(ridge.score(X_train,y_train))
print(ridge.score(X_test,y_test))
print(ridge.coef_)