# -*- coding:utf-8 -*-
import os
from pyecharts import Bar

# 垂直条形图
bar = Bar("Python 3.7 从零开始学", "按城市统计")
#Bar（“大标题”，“副标题”，各种属性）,这些属性通常为：
#title_color = “颜色”：标题颜色，可以是‘red’或者‘#0000’
#title_pos = ‘位置’：标题位置，如‘center’，‘left’···
#width = 1200：图表的宽
#height = 800：图表的高
#background_color = "背景色"：图表的背景色
#weiter....
bar.add("阅读人数分布", ["北京", "上海", "广州", "深圳", "杭州", "成都"],
        [500, 450, 360, 450, 355, 380])

