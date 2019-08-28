# -*- coding:utf-8 -*-
import pandas as pd
import re
from gensim import corpora,models,similarities
import jieba
from jieba import analyse
import numpy as np
from collections import Counter
import cv2
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#对评论结果进行筛选
data = pd.read_csv('./1.txt',sep='##')
data = data.loc[:,'comment']
#数据预处理
#换行符号删除
data=data.apply(lambda x:re.sub(r'\\n','',str(x)))
#&hellip;表情符号删除:以&符号开始,以;结束
data=data.apply(lambda x:re.sub('&[a-z]{1,10};','',str(x)))
#进行分词
data_cut = data.apply(lambda x: jieba.cut(x))
data_stop = pd.read_csv('stoplist.txt',header=None, encoding='utf-8',sep='\\n')
#删除重复行
data_stop.drop_duplicates(inplace=True)
stop=[' ','\u3000']+list(data_stop[0])
# print(data)
# print(stop)
texts = [[fenci for fenci in jieba.cut(text,cut_all=False)]for text in data]
dictionary = corpora.Dictionary(texts)
stop_ids = [dictionary.token2id[stop] for stop in data_stop if stop in dictionary.token2id]
once_ids = [once_id for once_id,once_num in dictionary.dfs.items() if once_num==1]
dictionary.filter_tokens(stop_ids+once_ids)
dictionary.compactify()
corpus = [dictionary.doc2bow(text) for text in texts]
#tf-idf模型
data_from_corpus=models.TfidfModel(corpus)
data_cor=data_from_corpus[corpus]
#lsi模型
lsi = models.LsiModel(data_cor, id2word=dictionary, num_topics=2)
#要输入的语句
doc = input('请输入：')
vec_bow = dictionary.doc2bow(doc.lower().split())
# print(list(vec_bow))
vec_lsi = lsi[vec_bow]  #将查询转换为LSI空间
# print(list(vec_lsi))
index = similarities.MatrixSimilarity(lsi[corpus])#将语料库转换为LSI空间并对其进行索引

sims = index[vec_lsi]  # 对语料库执行相似性查询
# print(list(sims))
sims = sorted(enumerate(sims), key=lambda item:-item[1])
# print(sims)
data_index = [x[0] for x in sims]#找到其相似度index
# print(data_index)
data_index = data_index[:10]#显示前十条
print(data[data_index])



#读取数据
try:
    data=pd.read_csv(r'1.txt',sep='##')
except Exception as ex:
    print(ex)
#

data=data[data.title=='三生三世十里桃花'].comment
# print(data)

#数据预处理
#换行符号删除
data=data.apply(lambda x:re.sub(r'\\n','',str(x)))
#&hellip;表情符号删除:以&符号开始,以;结束
data=data.apply(lambda x:re.sub('&[a-z]{1,10};','',str(x)))
# print(data)
#使用jieba模块对中文语句进行关键词分词
def guanjian(leixing):
    #根据传入的参数来确定是对关键字分词还是普通分词
    if leixing=='关键词':
        data_cut=data.apply(lambda x:analyse.extract_tags(x))
    else:
        data_cut = data.apply(lambda x: jieba.lcut(x))
    print(data_cut)
    #去除停用词
    stop=pd.read_csv('stoplist.txt',header=None, encoding='utf-8',sep='\\n')
    #删除重复行
    stop.drop_duplicates(inplace=True)
    stop=[' ','\u3000']+list(stop[0])
    print(stop)
    #确保停用词表里面不包含否定词以及程度词
    degree=pd.read_csv('degree.csv',engine='python',encoding='utf-8')
    degree.columns=['score']

    degree['term']=degree.index
    degree.index=list(range(0,len(degree)))
    # print(degree)
    no=pd.read_csv('not.csv',engine='python',encoding='utf-8')
    no['score']=-999
    # print(no)
    dic=pd.concat([degree,no],axis=0)
    # print('-----------')
    # print(dic)
    #将里面包含停用词的删除
    for i in dic.term:
        if i in stop:
            stop.remove(i)
    #删除文本中含有的停用词
    data_after=data_cut.apply(lambda x:[i for i in x if i not in stop])
    return [data_after,dic]

#统计词频
def cipin(data_after):
    data = np.array(data_after)
    datas = []
    for i in data:
        datas += i
    return Counter(datas).most_common(20)
#调用函数
num = cipin(guanjian('关键词')[0])

#将列表格式转化为series格式，单词作为索引
num = pd.Series([j[1] for j in num],index=[i[0] for i in num])
print(num)
# print(num)
#画关键字的词云图
wc = WordCloud(font_path='simkai.ttf',  # 设置字体
               background_color="white",  # 背景颜色
               max_words=20,        # 词云显示的最大词数
               max_font_size=200,     # 字体最大值
               random_state=42)
gar_wordcloud = wc.fit_words(num)#将数据填入
plt.figure(figsize=(16, 8))
plt.imshow(gar_wordcloud)
plt.title('豆瓣电影评价关键词')
plt.axis('off')
plt.show()


#情感分析
feel=pd.read_table('./BosonNLP_sentiment_score.txt',sep=' ',
                 header=None,engine='python',encoding='utf-8')
feel.columns=['word1','score1']
#评分
#分词后的结果,转为Series的格式
data_after = guanjian('1')[0]
dic = guanjian('1')[1]
temp=' '.join([' '.join(x) for x in data_after])
new_data=pd.Series(temp.split())
# print(data_after)
# print('_____________')
# print(new_data)
# len(new_data)
ID=[]
for i in data_after.index:
    ID.extend([i]*len(data_after[i]))
# print(ID)
new_data.index=ID
#len(new_data)
new_data=pd.DataFrame(new_data)
new_data.columns=['word']
#len(new_data)
#把否定词表,评分表,以及分词结果进行拼接合并
temp=pd.merge(new_data,feel,how='left',left_on='word',right_on='word1')
ndata=pd.merge(temp,dic,how='left',left_on='word',
               right_on='term')
ndata.index=ID
#len(ndata)
del ndata['word1'],ndata['term']

# print(ndata)
#找出score不是nan的index
index_dic=list(set(ndata[ndata['score'].isnull()==False].index))
# print(index_dic)
#len(index_dic)
#找出不包含否定词,程度副词的Index
index_nor =list(set([i for i in ndata.index if i not in index_dic]))
#对不含否定词,程度词的评论进行评分求和
new_score = pd.DataFrame(index=list(set(ndata.index)))

new_score['score'] = 0  #初始化情感分数
# print(new_score)
# print(new_score.loc[1800,'score'])
for i in index_nor:
    new_score.loc[i,'score'] = ndata.loc[i,'score1'].sum()#进行分数计算
# print(new_score)
# 对含有否定词、程度词的评论进行情感分值的调整
for i in index_dic:
    temp = ndata.loc[i]
    if len(temp.word) > 1:
        temp.index = range(len(temp))
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
# 根据new_score的分数将评论划分为正面评论及负面评论
index_pos = [i for i in new_score.index if new_score.loc[i,'score'] > 0]
pos = data_after[index_pos]    #正面评论
#打印出正面评论
print('正面评论:')
print(data[pos.index])

index_neg = [i for i in new_score.index if new_score.loc[i,'score'] < 0]
neg = data_after[index_neg]    ##负面评论
#打印出负面评论
print('负面评论:')
print(data[neg.index])
#总数

all_num = len(pos.index)+len(neg.index)
good_b = len(pos.index)/all_num*100
print('根据情感分析得出来的好评率为{}%'.format(good_b))

#根据正面评论绘制词云
num=[]
[num.extend(i) for i in pos]
num=pd.Series(num).value_counts()
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
plt.title('三生三世十里桃花正面评价关键词')
plt.axis('off')
plt.show()


#根据负面评论绘制词云
num=[]
[num.extend(i) for i in neg]
num=pd.Series(num).value_counts()
import cv2
from wordcloud import WordCloud
import matplotlib.pyplot as plt
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
plt.title('三生三世十里桃花负面评价关键词')
plt.axis('off')
plt.show()

#电影的总分为
try:
    data=pd.read_csv(r'1.txt',sep='##')
except Exception as ex:
    print(ex)
data = data[data.title=='三生三世十里桃花']
data = data.loc[:,'star']
data_len = len(data)
data_num = data.sum()

print('根据评论者给的评分平均为：{}%'.format(data_num/data_len))


