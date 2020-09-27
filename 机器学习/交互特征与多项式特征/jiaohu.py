# -*- coding:utf-8 -*-
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import mglearn
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import matplotlib.pyplot as plt
X, y = mglearn.datasets.make_wave(n_samples = 100)
# names=['age', 'workclass', 'fnlwgt', 'education',  'education-num',
#            'marital-status', 'occupation', 'relationship', 'race', 'gender',
#            'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
#            'income']
# data = pd.read_csv('./adult.csv', header=None, index_col=False, names=names)
# data = data.iloc[:, [0,2,4]]
# data = data.values
poly = PolynomialFeatures(degree=3)
poly.fit(X)
X_poly = poly.transform(X)

# print(poly.get_feature_names())
# print(X_poly)

# print(X)
line = np.linspace(-3, 3, 1000, endpoint=False).reshape(-1, 1)
print(line.shape)
print(line)
line_poly = poly.transform(line)
# print(line_poly.shape)
# print(line_poly)
reg = LinearRegression().fit(X_poly, y)
plt.plot(line, reg.predict(line_poly), label='plr')
plt.plot(X[:, 0], y, 'o', c='k')
plt.legend(loc="best")
plt.show()
