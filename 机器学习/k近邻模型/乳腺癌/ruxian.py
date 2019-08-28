# -*- coding:utf-8 -*-
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
#载入数据
cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,
                                                 stratify=cancer.target,random_state=66)
training_accuracy = []#训练集精度
test_accuracy = []#测试集精度
neighbors_settings = range(1,11)

#模型训练
for n_neightbors in neighbors_settings:
    clf = KNeighborsClassifier(n_neighbors=n_neightbors)
    clf.fit(X_train, y_train)
    #记录训练集精度
    training_accuracy.append(clf.score(X_train,y_train))
    #记录泛化精度
    test_accuracy.append(clf.score(X_test,y_test))
plt.plot(neighbors_settings, training_accuracy, label='training accuracy')
plt.plot(neighbors_settings, test_accuracy, label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()
plt.show()

