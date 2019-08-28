# -*- coding:utf-8 -*-
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering

X, y = make_blobs(random_state=0)
agg = AgglomerativeClustering(n_clusters=3)
assignment = agg.fit_predict(X)
print(assignment)
