# -*- coding:utf-8 -*-
from sklearn.datasets import fetch_lfw_people
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.decomposition import NMF
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
#构建nmf
nmf = NMF(n_components=15, random_state=0)
nmf.fit(X_people)
X_train_nmf = nmf.transform(X_people)
# X_test_nmf = nmf.transform(y_people)
#绘图
fix, axes = plt.subplots(3, 5, figsize=(15, 12), subplot_kw={'xticks':(),
                                                             'yticks':()})
for i, (component, ax) in enumerate(zip(nmf.components_, axes.ravel())):
    ax.imshow(component.reshape(image_shape))
    ax.set_title('{}'.format(i))
# plt.show()
print(nmf.components_.shape)
# print(axes)
print(X_train_nmf.shape)

#按第三个分量排序，绘制前十张图像
inds = np.argsort(X_train_nmf[:, 3])[::-1]
# print(inds)
# print(inds.shape)
# print(X_train_nmf[:, 3])
# print(X_train_nmf[:, 3].shape)
fix, axes = plt.subplots(3, 5, figsize=(15, 12), subplot_kw={'xticks':(),
                                                             'yticks':()})

for i, (ind, ax) in enumerate(zip(inds, axes.ravel())):
    ax.imshow(X_people[ind].reshape(image_shape))

plt.show()