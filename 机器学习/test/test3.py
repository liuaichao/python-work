# -*- coding:utf-8 -*-
import time
struct_time = time.localtime(time.time())  # 得到结构化时间格式
now_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
print(now_time)