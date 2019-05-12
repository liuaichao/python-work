# -*- coding:utf-8 -*-
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import requests
from lxml import etree
import pymysql
import random
from UserAgent_demo import UserAgent
from bs4 import BeautifulSoup
import jieba
from collections import Counter
from Mysql_demo import Mysql_demo
from pyecharts import Bar,Pie,WordCloud
import numpy as np
#数据存储
engine = create_engine('mysql+pymysql://root:lac981215lac@localhost/test?charset=utf8mb4',echo=False,pool_size=5)
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base = declarative_base()
def init_db():
    Base.metadata.create_all(engine)
class NLPAnalysis(Base):
    __tablename__ = 'npl_analysis_1'
    Id = Column(Integer,primary_key=True)
    question_title = Column(String(200),default=None,doc='问题标题')
    question_answer = Column(String(500),default=None,doc='问题答案')
    fen_ci_result = Column(String(1000),default=None,doc='分词结果')
def insert_data(dict_data, table_name):
    if table_name=='npl_analysis_1' and dict_data:
        data = NLPAnalysis(question_title=dict_data['question_title'],
                           question_answer=dict_data['question_answer'],
                           fen_ci_result=dict_data['fen_ci_result'])
    session.add(data)
    session.commit()
    session.close()
#数据爬取
def paqu():
    try:
        urls = ['https://zhidao.baidu.com/search?word=%C0%C5%E7%F0%B0%F1&ie=gbk&site=-1&sites=0&date=0&pn='+str((i+1)*10-10) for i in range(76)]
        # print(urls)
        a = UserAgent()
        a = a.getuseragent()
        headers = {
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection':'keep-alive',
            'Host':'zhidao.baidu.com',
            'Referer':'https://zhidao.baidu.com/search?word=%C0%C5%E7%F0%B0%F1&ie=gbk&site=-1&sites=0&date=0&pn=750',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':random.choice(a)
        }
        # url = 'https://zhidao.baidu.com/search?word=%C0%C5%E7%F0%B0%F1&ie=gbk&site=-1&sites=0&date=0&pn=0'
        # req = requests.get(url,headers=headers)
        # # print(req.text)
        # req.encoding = 'gbk'
        # print(req.text)
        for url in urls:
            req = requests.get(url, headers=headers)
            req.encoding = 'gbk'
            # html = etree.HTML(req.text)
            # html = html.xpath('//div[@class="list-inner"]/div[@class="list"]/dl/dt/a/em')
            # for i in html:
            #     print(i.text)
            soup = BeautifulSoup(req.text,'lxml')
            question_title = soup.select('.ti')
            question_answer = soup.select('dd[class="dd answer"]')
            # titles = []
            # answers = []
            for title,answer in zip(question_title,question_answer):
                ti = title.get_text()
                an = answer.get_text().replace('答：','')
                if len(ti)>500:
                    ti = ti[:500]
                if len(an)>500:
                    an = an[:500]
                # titles.append(str(ti))
                # answers.append(str(an))

                fencis = fenci(ti)
                dict_ls = dict()
                dict_ls['question_title'] = ti
                dict_ls['question_answer'] = an
                dict_ls['fen_ci_result'] = fencis
                insert_data(dict_ls,'npl_analysis_1')
    except Exception as ex:
        print('出现错误:{}'.format(ex))


#分词
def fenci(titles):
    # eq = ['，','...','。','是','的','“','”']
    jieba.suggest_freq(('梅长苏'),True)
    jieba.suggest_freq(('琅琊榜'), True)
    jieba.suggest_freq(('第几集'), True)

    ti = jieba.cut_for_search(titles)
    result_val = ','.join(list(ti))
    return str(result_val)
#词组分析
def an_fenci():
    my = Mysql_demo('localhost', 'root', 'lac981215lac', 'test')
    sql = 'select fen_ci_result from npl_analysis_1'
    data = my.search(sql)

    fenci_data = [data[i][0].split(',') for i in range(len(data))]
    fenci_data2 = []
    for k in range(len(fenci_data)):
        fenci_data2 = fenci_data2+fenci_data[k]
    eq = ['，', '...', '。', '是', '的', '“', '”','《','》','！','？',' ','吗','有','是','？','几集','第几','第几集','了','和','？','2','?','一集','电视','电视剧']
    fenci_new = fenci_data2.copy()
    for j in fenci_new:
        if j in eq:
            fenci_new.remove(j)
    re_data = Counter(fenci_new).most_common(30)
    re_data = np.array(re_data)
    # print(re_data[:,0])
    return re_data
#绘图
def paint_ec(data):
    bar = WordCloud("琅琊榜数据分析",'按词频统计',width=500,height=800)
    bar.add("词频分布",data[:,0],data[:,1])
    bar.render(r'data.html')




if __name__=='__main__':
    # init_db()
    # paqu()
    a = an_fenci()
    paint_ec(a)