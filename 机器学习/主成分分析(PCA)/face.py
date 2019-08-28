# -*- coding:utf-8 -*-
from sklearn.datasets import fetch_lfw_people
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

import mglearn

people = fetch_lfw_people(min_faces_per_person=20, resize=0.7)
image_shape = people.images[0].shape
fix, axes = plt.subplots(2, 5, figsize=(15, 8),
                         subplot_kw={'xticks':(), 'yticks':()})
for target, image, ax in zip(people.target, people.images, axes.ravel()):
    ax.imshow(image)
    ax.set_title(people.target_names[target])
# plt.show()
# print(people.images)
# print(people.target)
# print(len(people.target))
# print(len(np.unique(people.target)))
# print(np.unique(people.target))
# print('-------------------------')
#为了降低数据偏科，对每个人最多只选取50张图像
mask = np.zeros(people.target.shape, dtype=np.bool)
for target in np.unique(people.target):
    mask[np.where(people.target == target)[0][:50]] = 1
# print(mask)
# # print(people.target.shape)
X_people = people.data[mask]
# print(X_people)
y_people = people.target[mask]
# print(y_people)
#将灰度缩放到0-1之间，以得到更好的数据稳定性
X_people = X_people / 255
#拟合PCA，并提取100个主成分,然后采用k近邻算法进行人脸识别,启用pca白化选项
X_train, X_test, y_train, y_test = train_test_split(X_people, y_people, stratify=y_people
                                                    , random_state=0)
pca = PCA(n_components=100, whiten=True, random_state=0)
pca.fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train_pca, y_train)
print(knn.score(X_train_pca, y_train))
print(knn.score(X_test_pca, y_test))
#svc算法
# svc = SVC(kernel='rbf', C=10, gamma=1)
# svc.fit(X_train_pca, y_train)
# print(svc.score(X_train_pca, y_train))
# print(svc.score(X_test_pca, y_test))
mglearn.plots.plot_pca_faces(X_train, X_test, image_shape)
plt.show()