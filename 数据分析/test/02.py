# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.hist(np.random.randn(1000))
plt.savefig('./01.png')