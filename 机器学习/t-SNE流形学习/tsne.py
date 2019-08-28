# -*- coding:utf-8 -*-
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
digits = load_digits()
tsne = TSNE(random_state=0)
digits_tsne = tsne.fit_transform(digits.data)
print(digits_tsne)
print(digits_tsne.shape)
plt.figure(figsize=(10, 10))
plt.xlim(digits_tsne[:, 0].min(), digits_tsne[:, 0].max() +1)
plt.ylim(digits_tsne[:, 1].min(), digits_tsne[:, 1].max() +1)
colors = ['red', 'blue', 'black', 'yellow', 'red', 'red', 'blue', 'black', 'yellow', 'blue']
for i in range(len(digits.data)):
    plt.text(digits_tsne[i, 0], digits_tsne[i, 1], str(digits.target[i]),
             color = colors[digits.target[i]], fontdict={'weight': 'bold', 'size':9})
plt.show()

