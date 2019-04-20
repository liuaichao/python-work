# -*- coding:utf-8 -*-
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
f = lambda x,y:((x**2)-(y**3)+(6*x*(y**2))-12)/(5*y-7*x*y+3)
fig = plt.figure(0, dpi=120, figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
x = y = np.linspace(-5.0, 5.0, 1000)
X,Y = np.meshgrid(x,y)
zs = np.array([f(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(Y.shape)
ax.plot_surface(X,Y,Z,cmap='ocean')
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
ax.set_zlim(-5, 20)
plt.show()