# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
import numpy as np
ram_prices = pd.read_csv('./ram_price.csv')
# print(ram_prices)
# plt.semilogy(ram_prices.date, ram_prices.price)
plt.xlabel('year')
plt.ylabel('price')
# plt.show()
data_train = ram_prices[ram_prices.date<2000]
data_test = ram_prices[ram_prices.date>=2000]
X_train = data_train.date[:, np.newaxis]
y_train = np.log(data_train.price)

tree = DecisionTreeRegressor().fit(X_train, y_train)
#对所有的数据进行预测
X_all = ram_prices.date[:, np.newaxis]
pred_tree = tree.predict(X_all)
print(pred_tree)
price_tree = np.exp(pred_tree)
#可视化
plt.semilogy(data_train.date, data_train.price, label='训练数据')
plt.semilogy(data_test.date, data_test.price, label='测试数据')
plt.semilogy(ram_prices.date, price_tree, label='回归树')
plt.legend()
plt.show()
