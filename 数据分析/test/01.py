# -*- coding:utf-8 -*-
import numpy as np

x = y =np.linspace(-5.0,5.0,5)
print(x)
print('---------------')
print(y)
print('---------------')
X,Y = np.meshgrid(x,y)
# print(x.shape)
# print(y)
f = lambda x,y:(x+y)
array = np.array([f(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])
print(X)
print('---------------')
print(Y)

# print(array)
Z = array.reshape(Y.shape)
print('---------------')
print(Z)