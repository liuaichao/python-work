# -*- coding:utf-8 -*-
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,
                                                 stratify=cancer.target,random_state=66)
#使用同一个缩放模型
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
# print(min_on_training)
# print(range_on_training)
# print(X_train_scaled)
scaler1 = MinMaxScaler()
scaler1.fit(X_test)
X_test_scaled1 = scaler1.transform(X_test)
svc = SVC(kernel='rbf', C=10, gamma=1)
svc.fit(X_train_scaled, y_train)
print(svc.score(X_train_scaled, y_train))
print(svc.score(X_test_scaled, y_test))
print(svc.score(X_test_scaled1, y_test))