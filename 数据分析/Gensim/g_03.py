# -*- coding:utf-8 -*-
from gensim import corpora,models
import jieba
import numpy as np
texts = [[fenci for fenci in jieba.cut(text,cut_all=False)]for text in open('z-1.txt','r')]
dictionary = corpora.Dictionary(texts)
# print(dictionary.token2id)
#无用词
# print(len(dictionary))
stop_word = ['\n','、','。','《','》',' ','（','）','“','”','？']

stop_ids = [dictionary.token2id[stop] for stop in stop_word if stop in dictionary.token2id]
once_ids = [once_id for once_id,once_num in dictionary.dfs.items() if once_num==1]
dictionary.filter_tokens(stop_ids+once_ids)
dictionary.compactify()
# print(len(dictionary))
# print(dictionary.token2id)
# print(len(dictionary))
corpus = [dictionary.doc2bow(text) for text in texts]
# print(len(list(dictionary.dfs.items())))
print(list(corpus))
# a = 0
# for i in list(corpus):
#     a = a+len(i)
# print(a)
class Corpus_connectorE(object):
    def __iter__(self):
        for line in open(r'z-1.txt'):
            jie_fenci = line.lower().split()
            # print(line)
            yield dictionary.doc2bow(jie_fenci)


# CCE = Corpus_connectorE()
# print(type(CCE))
# for vector in CCE:
#     print(vector)
tfidf =models.TfidfModel(corpus)
doc_bow = [[(0, 1), (1, 1),(2,10),(3,4)],[(0,3),(1,2)]]
# print(tfidf)
# print(tfidf[corpus])
print(list(tfidf[doc_bow]))
# for i in tfidf[corpus]:
#     print(i)
tfidf_data = tfidf[corpus]
#LSI模型
lsi = models.LsiModel(tfidf_data, id2word=dictionary, num_topics=2)

# print(list(lsi[tfidf_data]))
# print(lsi.print_topics(2))
# print(np.array(list(lsi_vec)))
