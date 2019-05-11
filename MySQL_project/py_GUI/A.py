# -*- coding:utf-8 -*-
# import pandas as pd
# import numpy as np
# df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2018/12/18',
#    periods=10), columns=list('ABCD'))
#
# df.plot()
# import matplotlib.pyplot as plt
# import numpy as np
# n_bins = 10
# x = np.arange(2,25,2)
# print(x)
# fig, ax = plt.subplots()
# ax.hist(x, n_bins, density=True, histtype='bar')
# ax.set_title('bars with legend')
# fig.tight_layout()
# plt.savefig('./test2.jpg')
# plt.show()
import json
import pandas as pd
import matplotlib.pyplot as plt
st = {"书名":['六爱超','红楼梦','三国演义'],"数量":[3,2,1]}
a = json.dumps(st)
student = pd.read_json(a)
print(student)
# for a,b in zip(st["书名"],st["数量"]):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=11)
plt.title('直方图')
student.plot.line(x='书名',y='数量')
plt.savefig('D:\\pythonproject\\MySQL_project\\data_a\\test2.jpg')
plt.show()



