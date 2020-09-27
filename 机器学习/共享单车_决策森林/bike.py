# -*- coding:utf-8 -*-
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
#读取数据
bike_data = pd.read_csv('./bike_day.csv')
#特征提取
feature_names = bike_data.columns.values[2:13]
#数据
X = bike_data.values[:,2:13]
#标签
y = bike_data.values[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
#构建模型
rf_tree = RandomForestRegressor(n_estimators=1000, max_depth=10, min_samples_split=2)
rf_tree.fit(X_train, y_train)
print(rf_tree.score(X_train, y_train))
print(rf_tree.score(X_test, y_test))
print(list(zip(feature_names, rf_tree.feature_importances_)))
