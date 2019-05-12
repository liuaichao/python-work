# -*- coding:utf-8 -*-
from gensim import corpora
import jieba
dictionary = corpora.Dictionary([[fenci for fenci in jieba.cut(text,cut_all=False)]for text in open('z-1.txt','r')])
# print(dictionary.token2id)
#无用词
# print(len(dictionary))
stop_word = ['\n','、','。','《','》',' ','（','）','“','”','？']
stop_ids = [dictionary.token2id[stop] for stop in stop_word if stop in dictionary.token2id]
once_ids = [once_id for once_id,once_num in dictionary.dfs.items() if once_num==1]
dictionary.filter_tokens(stop_ids+once_ids)
dictionary.compactify()
# print(len(dictionary))
print(dictionary.token2id)
print(len(dictionary))

class Corpus_connectorE(object):
    def __iter__(self):
        for line in open(r'0.txt'):
            jie_fenci = line.lower().split()
            # print(line)
            yield dictionary.doc2bow(jie_fenci)


CCE = Corpus_connectorE()
for vector in CCE:
    print(vector)

