# -*- coding:utf-8 -*-
from gensim import models,corpora
from jieba import analyse
import jieba
import jieba.posseg as psg
def get_corpus_dictionary():
    texts = [[text for text in jieba.cut(duan)]for duan in open('./corpus.txt','r',encoding='utf-8')]
    stop_text = [text for text in open('./stopword.txt','r',encoding='utf-8')]
    stop_texts = []
    for i in stop_text:
        stop_texts.append(i.strip('\n'))
    # print(texts)
    # print(stop_texts)
    dictionary = corpora.Dictionary(texts)
    stop_ids = [dictionary.token2id[shop] for shop in stop_texts if shop in dictionary.token2id]
    once_ids = [once_id for once_id,once_num in dictionary.dfs.items() if once_num==1]
    dictionary.filter_tokens(stop_ids+once_ids)
    dictionary.compactify()
    corpus = [dictionary.doc2bow(text) for text in texts]
    return [dictionary,corpus]
def model_Tfidf(corpus):
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    return corpus_tfidf
def model_Lda(dictionary,corpus_tfidf,corpus):
    lda = models.LdaModel(corpus_tfidf,id2word=dictionary,num_topics=100)
    lda_data = lda[corpus]
    return lda_data
if __name__=='__main__':
    data = get_corpus_dictionary()
    corpus_tfidf = model_Tfidf(data[1])
    lad_data = model_Lda(data[0],corpus_tfidf,data[1])
    print(list(lad_data))
    print(list(data[0]))
    print(list(data[1]))