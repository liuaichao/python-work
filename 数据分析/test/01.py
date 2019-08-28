# -*- coding:utf-8 -*-
import pandas as pd
import re
#读取数据
data=pd.read_csv('comment.csv',encoding='utf-8')
data.品牌.value_counts()#查看每个品牌的数据量
data=data[data.品牌=='AO'].评论


#数据预处理
#换行符号删除
data=data.apply(lambda x:re.sub(r'\\n','',str(x)))#raw表示原生的意思
#&hellip;表情符号删除:以&符号开始,以;结束
data=data.apply(lambda x:re.sub('&[a-z]{1,10};','',str(x)))
#热水器型号删除
data=data.apply(lambda x:re.sub('AO史密斯.+升','',str(x)))



##分词
import jieba   ##使用jieba模块对中文语句进行分词
data_cut=data.apply(lambda x:jieba.lcut(x))

##去除停用词
stop=pd.read_csv('stoplist.txt',header=None,
                 encoding='utf-8',sep='song')
stop.drop_duplicates(inplace=True)
stop=[' ','\u3000']+list(stop[0])

#确保停用词表里面不包含否定词以及程度词
degree=pd.read_csv('degree.csv',engine='python',encoding='utf-8')
degree.columns=['term']

degree['score']=degree.index
degree.index=list(range(0,len(degree)))
no=pd.read_csv('not.csv',engine='python',encoding='utf-8')
no['score']=-999
dic=pd.concat([degree,no],axis=0)
for i in dic.term:
    if i in stop:
        stop.remove(i)
data_after=data_cut.apply(lambda x:[i for i in x if i not in stop])


#词频
def cipin(x,n=10):
    temp=[' '.join(i) for i in x]
    temp1=' '.join(temp)
    temp2=pd.Series(temp1.split())
    num=temp2.value_counts()
    return (num[num>n])
cut_num=cipin(data_after)
num=cipin(data_after)
# print(num)

import cv2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'         #设置字体为SimHei显示中文
plt.rcParams['axes.unicode_minus'] = False
back_pic = cv2.imread("aixin.jpg")  # 设置背景图片
wc = WordCloud(font_path='simkai.ttf',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,        # 词云显示的最大词数
               mask=back_pic,          # 设置背景图片
               max_font_size=200,     # 字体最大值
               random_state=42)
gar_wordcloud = wc.fit_words(num[:400])  # cut_num是由频数构成的Series的形式,且单词作为索引
plt.figure(figsize=(16, 8))
plt.imshow(gar_wordcloud)
plt.title('京东评价关键词')
plt.axis('off')
plt.show()



#情感倾向分析
#1.1计算情感词表
#导入情感词表
feel=pd.read_table('BosonNLP_sentiment_score.txt',sep=' ',
                 header=None,engine='python',encoding='utf-8')
feel.columns=['word1','score1']
#评分
#分词后的结果,转为Series的格式
temp=' '.join([' '.join(x) for x in data_after])
new_data=pd.Series(temp.split())
len(new_data)
#n_data=[]#如果没有把全角符号的空格去除掉的话,也可以正常运行的
#for i in comment_after:
    #n_data.extend(i)
#Index索引改为对应的评论位置
ID=[]
for i in data_after.index:
    ID.extend([i]*len(data_after[i]))
new_data.index=ID
#len(new_data)
new_data=pd.DataFrame(new_data)
new_data.columns=['word']
#len(new_data)
##把否定词表,评分表,以及分词结果合并
temp=pd.merge(new_data,feel,how='left',left_on='word',right_on='word1')
ndata=pd.merge(temp,dic,how='left',left_on='word',
               right_on='term')
ndata.index=ID
#len(ndata)
del ndata['word1'],ndata['term']
#找出包含否定词,程度副词的Index
#len(ndata[ndata['score'].isnull()==False])
index_dic=list(set(ndata[ndata['score'].isnull()==False].index))
#len(index_dic)
#找出不包含否定词,程度副词的Index
index_nor =list(set([i for i in ndata.index if i not in index_dic]))
#对不含否定词,程度词的评论进行评分求和
new_score = pd.DataFrame(index=list(set(ndata.index)))
new_score['score'] = 0  ## 储存我们情感总分
for i in index_nor:
    new_score.loc[i,'score'] = ndata.loc[0,'score1'].sum()

# 对含有否定词、程度词的评论进行情感分值的调整
for i in index_dic:
    temp = ndata.loc[i]
    if len(temp.word) > 1:
        temp.index = range(len(temp))
        # 否定词 -999
        #1 双重否定表肯定；2 否定词在句末；3 否定词后面是词语，词语情感反转
        a = [x for x in temp.index if temp.loc[x,'score'] == -999]
        for k in a:
            if k == len(temp) - 1:                #2 否定词在句末
                temp.loc[k,'score1'] = 0
            elif temp.loc[k+1,'score'] == -999:  #1 双重否定表肯定；
                temp.loc[k,'score1'] = 0
                temp.loc[k+1,'score1'] = 0
                a.remove(k+1)
            else:
                temp.loc[k,'score1'] = 0    #3 否定词后面是词语，词语情感反转
                temp.loc[k+1,'score1'] = (-1)*temp.loc[k+1,'score1']
        # 程度词-50、-200、-400%10==0;程度词在句末；不在句末
        b = [i for i in range(len(temp)) if temp.loc[i,'score']%10 == 0]
        for k in b:
            if k == len(temp) -1:
                temp.loc[k,'score1'] = 0
            else:
                temp.loc[k+1, 'score1'] = temp.loc[k+1,'score1']*temp.loc[k, 'score']/(-100)
                temp.loc[k, 'score1'] = 0
    new_score.loc[i,'score'] = temp.score1.sum()


new_score['score'].sort_values(ascending=False)
data_after[6057]
#print(data['评论'][6057])
# 根据new_score的分数将评论划分为正面评论及负面评论
index_pos = [i for i in new_score.index if new_score.loc[0,'score'] > 0]
pos = data_after[index_pos]    ##正面评论


index_neg = [i for i in new_score.index if new_score.loc[i,'score'] < 0]
neg = data_after[index_neg]    ##负面评论

#总数

# all_num = len(pos.index)+len(neg.index)
# good_b = len(pos.index)/all_num*100
# print('根据情感分析得出来的好评率为{}%'.format(good_b))


##根据正面评论绘制词云
##根据正面评论绘制词云
num=[]
[num.extend(i) for i in pos]
num=pd.Series(num).value_counts()
import cv2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'         #设置字体为SimHei显示中文
plt.rcParams['axes.unicode_minus'] = False
back_pic = cv2.imread("aixin.jpg")  # 设置背景图片
wc = WordCloud(font_path='simkai.ttf',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_pic,  # 设置背景图片
               max_font_size=200,  # 字体最大值
               random_state=42)
gar_wordcloud = wc.fit_words(num[:400])  # cut_num是由频数构成的Series的形式,且单词作为索引
plt.figure(figsize=(16, 8))
plt.imshow(gar_wordcloud)
plt.title('京东正面评价关键词')
plt.axis('off')
plt.show()


##根据负面评论绘制词云
##根据负面评论绘制词云
num=[]
[num.extend(i) for i in neg]
num=pd.Series(num).value_counts()
import cv2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = 'SimHei'         #设置字体为SimHei显示中文
plt.rcParams['axes.unicode_minus'] = False
back_pic = cv2.imread("aixin.jpg")  # 设置背景图片
wc = WordCloud(font_path='simkai.ttf',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=2000,  # 词云显示的最大词数
               mask=back_pic,  # 设置背景图片
               max_font_size=200,  # 字体最大值
               random_state=42)
gar_wordcloud = wc.fit_words(num[:400])  # cut_num是由频数构成的Series的形式,且单词作为索引
plt.figure(figsize=(16, 8))
plt.imshow(gar_wordcloud)
plt.title('京东负面评价关键词')
plt.axis('off')
plt.show()

