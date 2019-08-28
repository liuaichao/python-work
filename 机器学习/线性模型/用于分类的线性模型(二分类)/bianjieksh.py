# -*- coding:utf-8 -*-
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import mglearn
X,y = mglearn.datasets.make_forge()
# print(y)
fig, axes = plt.subplots(1, 2, figsize=(10,3))
for model, ax in zip([LogisticRegression(),LinearSVC()], axes):
    clf = model.fit(X, y)
    mglearn.plots.plot_2d_separator(clf, X, fill=False, eps=0.5, ax=ax, alpha=0.7)
    mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
    ax.set_xlabel(0)
    ax.set_ylabel(1)
axes[0].legend()
print(fig)
print(axes)
plt.show()