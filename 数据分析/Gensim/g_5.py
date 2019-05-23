# -*- coding:utf-8 -*-
from gensim import corpora,models,similarities
import jieba
import pandas as dp
import numpy as np
#返回字典,生成tfidf模型
def return_dectionary_tfidf(file_path):
    out_word = ['\n','的']
    texts = [[text for text in jieba.cut(data)] for
             data in open(file_path,'r',
                          encoding='utf-8')]
    dictionary = corpora.Dictionary(texts)
    stop_ids = [dictionary.token2id[stop] for stop in out_word if stop in dictionary.token2id]
    dictionary.filter_tokens(stop_ids)
    dictionary.compactify()

    corpus = [dictionary.doc2bow(text) for text in texts]
    #tfidf模型
    tf_idf = models.TfidfModel(corpus)
    # corpus_tf_idf = tf_idf[corpus]
    # #把tfidf模型保存
    # corpus_tf_idf.save(r"./model.tfidf")
    tfidf = models.TfidfModel.load("D:\pythonproject\数据分析\gensim\model.tfidf")
    print('tfidf模型加载成功')
    lsi = models.LsiModel(tfidf, id2word=dictionary, num_topics=10)
    # lsis = lsi[tfidf]
    # lsis.save('./model_lsi.lsi')
    return [dictionary,tf_idf,lsi,corpus]


if __name__=='__main__':
    corpus_s = return_dectionary_tfidf('D:\\pythonproject\\数据分析\\gensim\\book_title.txt')
    #读取数据
    data = [title for title in open(r'D:\pythonproject\数据分析\gensim\book_title.txt','r',encoding='utf-8')]
    #加载lsi模型
    lsi_model = models.LsiModel.load('./model_lsi.lsi')
    index = similarities.MatrixSimilarity(lsi_model)
    print('lsi模型加载成功')
    entry_data = input('请输入要查找的书名:')
    vec_bow = corpus_s[0].doc2bow(jieba.cut(entry_data))
    #输入数据转换为tfidf模型
    vec_tfidf = corpus_s[1][vec_bow]
    #输入数据转换成lsi模型
    vec_lsi = corpus_s[2][vec_tfidf]

    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key= lambda x:-x[1])
    # new_dict = {v: k for k, v in corpus_s[0].token2id.items()}
    # print(len(new_dict))
    # print(new_dict[136564])
    with open('相似度.txt','w',encoding='utf-8') as f:
        count = 0
        for i in sims:
            if i[1]>0:
                f.write(str(i[0]))
                f.write('  ')
                f.write(str(i[1]))
                f.write(('  '))
                f.write(str(data[i[0]]))
                f.write('\n')
                count += 1
            elif count==20:
                break
            else:
                break
