# -*- coding:utf-8 -*-
from gensim import corpora,models,similarities
import numpy as np
documents = ["Human machine interface for lab abc computer applications",
              "A survey of user opinion of computer system response time",
              "The EPS user interface management system",
              "System and human system engineering testing of EPS",
              "Relation of user perceived response time to error measurement",
              "The generation of random binary unordered trees",
              "The intersection graph of paths in trees",
              "Graph minors IV Widths of trees and well quasi ordering",
              "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
#stoplist={'of', 'and', 'for', 'the', 'in', 'to', 'a'}
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]

 # remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
#或者用下面的关闭方案
#frequency={}
for text in texts:
     for token in text:
        frequency[token] += 1
        #try:
            #frequency[token] += 1
        #except KeyError:
            #frequency[token]=1
# print(frequency)
texts = [[token for token in text if frequency[token] > 1]
         for text in texts]
# print(texts)
dictionary = corpora.Dictionary(texts)
print(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus)
data_from_corpus=models.TfidfModel(corpus)
data_cor=data_from_corpus[corpus]
# print(list(data_cor))
# for j in data_cor:
#     print(j)

#在前面关于语料库和向量空间以及主题和转换的教程中，我们讨论了在向量空间模型中创建语料库的含义以及如何在不同的向量空间之间转换它。
#这种特征的一个常见原因是我们想要确定文档对之间的相似性，或者特定文档与一组其他文档（例如用户查询与索引文档）之间的相似性。
#为了说明在gensim中如何做到这一点，让我们考虑与之前的例子相同的语料库

#1.准备工作
from gensim import models
lsi = models.LsiModel(data_cor, id2word=dictionary, num_topics=2)
#现在假设用户输入查询“人机交互”(“Human computer interaction”)。 我们希望按照与此查询相关的递减顺序对我们的九个语料库文档进行排序。
#与现代搜索引擎不同，这里我们只关注可能的相似性的一个方面——文本(单词)的明显语义相关性。
#没有超链接，没有随机游走静态排名，只是对布尔关键字匹配的语义扩展：
doc = "Human computer interaction"
#doc="A survey of user opinion of computer system response time"
vec_bow = dictionary.doc2bow(doc.lower().split())
print(list(vec_bow))
vec_lsi = lsi[vec_bow]  #将查询转换为LSI空间
print(list(vec_lsi))
#此外，我们将考虑余弦相似度来确定两个向量的相似度。余弦相似度是向量空间建模中的一种标准度量，
#但只要向量表示概率分布，其他的相似度度量可能更合适。

#2.初始化查询结构
#为了准备相似性查询，我们需要输入我们想要与后续查询进行比较的所有文档。
#在我们的例子中，它们与用于训练LSI并转换到二维LSA空间的九个文件相同，但这只是偶然的，我们也可能完全索引不同的语料库。
print(list(lsi[corpus]))
print('-----------')
index = similarities.MatrixSimilarity(lsi[corpus])#将语料库转换为LSI空间并对其进行索引
# print(np.array(index))

#3.执行查询
#获得查询文档与9个索引文档的相似性
print('----------------')
sims = index[vec_lsi]  # 对语料库执行相似性查询
# print(list(enumerate(sims)))  # print (document_number, document_similarity) 2-tuples
print(list(sims))
#余弦测度返回<- 1,1 >范围内的相似性(越大越相似)，因此第一个文档的得分为0.99809301等。
sims = sorted(enumerate(sims), key=lambda item:-item[1])
print(sims)