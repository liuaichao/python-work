# -*- coding:utf-8 -*-
from sklearn.datasets import fetch_lfw_people
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import numpy as np

import mglearn

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
image_shape = people.images[0].shape
#为了降低数据偏科，对每个人最多只选取50张图像
mask = np.zeros(people.target.shape, dtype=np.bool)
for target in np.unique(people.target):
    mask[np.where(people.target == target)[0][:50]] = 1
X_people = people.data[mask]
# print(X_people)
y_people = people.target[mask]
# print(y_people)
#将灰度缩放到0-1之间，以得到更好的数据稳定性
X_people = X_people / 255
pca = PCA(n_components=100, whiten=True, random_state=0)
pca.fit_transform(X_people)
X_pca = pca.transform(X_people)
print(X_pca)
print(X_pca.shape)

km = KMeans(n_clusters=10, random_state=0)
labels_km = km.fit(X_pca)
print(km.cluster_centers_)
print(km.cluster_centers_.shape)
fig, axes = plt.subplots(2, 5, subplot_kw={'xticks':(), 'yticks':()}, figsize=(12,5))
for center, ax in zip(km.cluster_centers_, axes.ravel()):
    ax.imshow(pca.inverse_transform(center).reshape(image_shape), vmin=0,vmax=1)
plt.show()

