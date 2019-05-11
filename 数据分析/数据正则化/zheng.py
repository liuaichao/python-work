# -*- coding:utf-8 -*-
import pandas as pd
import re
import numpy as np
data = pd.read_excel(r'C:\Users\THINKPAD\Desktop\数据分析\regulardata.xls',header=None)
email = []
href = []
data = np.array(data,object)
for i in range(len(data)):
    a = re.findall(r'   (https://www\.[a-z A-Z \d \. / -]*)  ',data[i][0])
    b = re.findall(r' (Email: [a-z A-Z @ .]*) ',data[i][0])
    email += b
    href += a
print(email)
print(href)
