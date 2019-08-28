# -*- coding:utf-8 -*-
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
X, y = make_blobs(n_samples=12, random_state=0)
print(len(X))
dbscan = DBSCAN(eps=1, min_samples=1)
clusters = dbscan.fit_predict(X)
print(clusters)