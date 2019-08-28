# -*- coding:utf-8 -*-
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import graphviz
#载入数据
cancer = load_breast_cancer()
X_train,X_test,y_train,y_test = train_test_split(cancer.data,cancer.target,
                                                 stratify=cancer.target,random_state=66)
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)
print(tree.score(X_train, y_train))
print(tree.score(X_test, y_test))
#生成树的可视化文件
export_graphviz(tree, out_file='./tree.dot', class_names=['恶性', '良性'],
                feature_names=cancer.feature_names, impurity=False, filled=True)
#读取graphviz文件
with open('./tree.dot', encoding='utf8') as f:
    dot_graph = f.read()
graphviz.Source(dot_graph)
graphviz.view('./tree.dot')