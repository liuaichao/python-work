# -*- coding:utf-8 -*-
import mglearn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import NMF
S = mglearn.datasets.make_signals()
# print(S)
# print(S.shape)
plt.figure(figsize=(6, 1))
plt.plot(S, '-')
# plt.show()
A = np.random.RandomState(0).uniform(size=(100, 3))
# print(A)
# print(A.shape)
X = np.dot(S, A.T)
nmf = NMF(n_components=3, random_state=1)
S_ = nmf.fit_transform(X)
plt.figure(figsize=(6, 1))
plt.plot(S_, '-')
plt.show()