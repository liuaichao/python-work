# -*- coding:utf-8 -*-
import jieba
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from langconv import *
import pandas as pd
import re
import jieba
import numpy as np
import logging
# a = '劉'
# b = Converter('zh-hans').convert(a)
# print(b)
# logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO);
def start():
    texts = [re.findall(r'\[(.+)\]',text) for text in open('D:\Google_Download\SogouQ.reduced','r',encoding='utf-8')]

    for text in texts:
        with open('./sougou.txt','a',encoding='utf-8') as f:
            f.write(' '.join(jieba.cut(text[0])))
            f.write('\n')

# print(a)
# print(textss[0][0])
#训练word2vec模型
def my_function():
    sougo_new = open('./sougou.txt','r',encoding='utf-8')
    model = Word2Vec(LineSentence(sougo_new), sg=0, size=10, window=5,min_count=1, workers=9)
    print('1')
    model.save('./sougou_new.word2vec')
#相似度查找
def similarity_search():
    model = Word2Vec.load('./sougou_new')
    print(model.similarity('中国','汶川'))
    word = '中国'
    if word in model.wv.index2word:
        print(model.most_similar(word))

if __name__=='__main__':
    my_function()