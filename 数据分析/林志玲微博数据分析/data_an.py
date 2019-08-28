# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from snownlp import SnowNLP

#男女比例分析
def nanv(data):

    fm_data = data['user_gender'].value_counts()
    fm_data = np.array(fm_data)
    print(fm_data)
    fm_data = pd.Series(fm_data,index=['女','男'])
    print(fm_data)
    fm_data.plot.pie(title='男女比例')
    plt.savefig('./test.jpg')

#真假粉丝判断
def iszhen(data):

    data_jia = np.array(data)
    zong = data_jia.shape[0]#总共行数
    data_jia = data_jia[:,9:10]
    data_jia = data_jia[:,0]<5
    jia_num = 0
    for i in data_jia:
        if i==True:
            jia_num+=1
    zhen = zong-jia_num
    print('真粉丝转发数占总转发数的{}%'.format((zhen/(zhen+jia_num))*100))
    print('假粉丝转发数占总转发数的{}%'.format((jia_num/(zhen+jia_num))*100))
#对结婚的看法
def get_sent_snownlp(data):
    datas = data.loc[:,'raw_text']
    new_data = pd.DataFrame({'content':[],'attitude':[]})
    for data in datas:
        try:
            s = SnowNLP(data)
            # print(data)
            new_data = new_data.append({'content':data,'attitude':s.sentiments}, ignore_index=True)
        except:
            continue
    # print(new_data)
    # return s.sentiments
    #好评率
    hao_num = 0
    huai_num = 0
    all_score = 0
    for data1 in new_data.loc[:,'attitude']:
        all_score = all_score+data1
        if data1>0.5:
            hao_num+=1
        else:
            huai_num+=1

    print('对于林志玲跟日本人结婚好评率为{}%'.format((hao_num/(hao_num+huai_num))*100))
    print('对于林志玲跟日本人结婚坏评率为{}%'.format((huai_num/(hao_num+huai_num))*100))
    print('对于林志玲跟日本人结婚平均评分为{}'.format(all_score/(hao_num+huai_num)))
#粉丝使用的手机
def use_send(data):
    fm_data = data['source'].value_counts()
    print(fm_data)
if __name__=='__main__':
    #数据清洗
    data = pd.read_csv('./data.csv',index_col=None)
    data.fillna('0')#0填充缺失值
    data = data.drop_duplicates()#删除重复列
    print(data.sample(5))
    # nanv(data)
    # iszhen(data)
    # get_sent_snownlp(data)
    use_send(data)
