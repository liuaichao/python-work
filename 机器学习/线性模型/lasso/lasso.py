# -*- coding:utf-8 -*-
from sklearn.linear_model import Lasso
import mglearn
from sklearn.model_selection import train_test_split
import numpy as np
X,y = mglearn.datasets.load_extended_boston()
# print(X.shape)
# print(y)
X_train,X_test,y_train,y_test = train_test_split(X, y, random_state=0)
lasso = Lasso(alpha=0.01, max_iter=100000).fit(X_train,y_train)
print(lasso.score(X_train,y_train))
print(lasso.score(X_test,y_test))
print(np.sum(lasso.coef_ != 0))