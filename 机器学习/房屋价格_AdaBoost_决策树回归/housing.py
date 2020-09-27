# -*- coding:utf-8 -*-
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import datasets
from sklearn.model_selection import train_test_split
#加载数据
house_data = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(house_data.data, house_data.target,
                                                    random_state=1, train_size=0.8)
#构建决策树模型
dt_tree = DecisionTreeRegressor(max_depth=6)
dt_tree.fit(X_train, y_train)
print("只使用决策树的分数:{}".format(dt_tree.score(X_test, y_test)))
# print(format(dt_tree.score(X_train, y_train)))
# print(dt_tree.feature_importances_)
#构建AdaBoost算法的决策树回归模型
adaboost = AdaBoostRegressor(DecisionTreeRegressor(max_depth=6), n_estimators=400,
                             random_state=1)
adaboost.fit(X_train, y_train)
print("使用AdaBoost算法的决策树分数:{}".format(adaboost.score(X_test, y_test)))
# print(adaboost.score(X_train, y_train))
# print(adaboost.feature_importances_)


