import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

for item in set(addressList):
    print('nums of', item, ':', addressList.count(item))

# 中文和负号的正常显示
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

addressDataFrame = pd.Series(addressList)
addressDataFrame = addressDataFrame.value_counts().sort_values(ascending=False)
# 当读者太多，出生地址太多时，去频率最高的前20个进行展示
if len(addressDataFrame) < 20:
    pass
else:
    addressDataFrame = addressDataFrame[1:20]
plt.xticks(rotation=90)
plt.bar(addressDataFrame.index, addressDataFrame)
plt.show()

print('\n第三部分--对', str(booknameList[0]), '的评论词频统计:')
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
from scipy.misc import imread
import jieba
import jieba.analyse
import os, codecs
from collections import Counter

tags = jieba.analyse.extract_tags(str(bookcomment), topK=100, withWeight=False)
text = " ".join(tags)
# text = unicode(text)

# 读入背景图片
bj_pic = imread('ciyun.jpg')

# 生成词云（通常字体路径均设置在C:\\Windows\\Fonts\\也可自行下载）
font = r'C:\\Windows\\Fonts\\STFANGSO.ttf'  # 不加这一句显示口字形乱码  ""报错
wordcloud = WordCloud(mask=bj_pic, background_color='white', font_path=font, scale=3.5).generate(text)
# img_color = ImageColorGenerator(self.img)
image_colors = ImageColorGenerator(bj_pic)

# 显示词云
plt.imshow(wordcloud)
plt.axis('off')
plt.show()

wordcloud.to_file('test.jpg')
# 词频统计
seg_list = jieba.cut(str(bookcomment))
c = Counter()
for x in seg_list:
    if len(x) > 1 and x != '\r\n':
        c[x] += 1
hotWordIntext = []
hotWordNumIntext = []
for (k, v) in c.most_common(20):
    hotWordIntext.append(k)
    hotWordNumIntext.append(v)
hotWordIntextDataFrame = pd.DataFrame(hotWordNumIntext, index=hotWordIntext, columns=['nums'])
# 当读者太多，出生地址太多时，去频率最高的前20个进行展示
print('热点词频度统计结果(只显示前20)')
plt.xticks(rotation=90)
plt.bar(hotWordIntextDataFrame.index, hotWordIntextDataFrame.nums)
plt.show()

bookcomment = []
hotWordIntext = []
hotWordNumIntext = []
addressList = []
websOfBookReview = []  # 为防止下次冗余而特地清空评论网页列表
booknameList = []
numsOfShortReview = []