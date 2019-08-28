# -*- coding:utf-8 -*-
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,
                                                 stratify=cancer.target,random_state=66)
#训练集缩放
min_on_training = X_train.min(axis=0)
range_on_training = (X_train - min_on_training).max(axis=0)
X_train_scaled = (X_train - min_on_training) / range_on_training
#测试集缩放
min_on_test = X_test.min(axis=0)
range_on_test = (X_test - min_on_test).max(axis=0)
X_test_scaled = (X_test - min_on_test) / range_on_test
# print(min_on_training)
# print(range_on_training)
print(X_train_scaled)
svc = SVC(kernel='rbf', C=10, gamma=1)
svc.fit(X_train_scaled, y_train)
print(svc.score(X_train_scaled, y_train))
print(svc.score(X_test_scaled, y_test))