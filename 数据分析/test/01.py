# -*- coding:utf-8 -*-
from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
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
init_db()
def insert_data(dict_data, table_name):
    if table_name=='npl_analysis_1' and dict_data:
        data = NLPAnalysis(question_title=dict_data['question_title'],
                           question_answer=dict_data['question_answer'],
                           fen_ci_result=dict_data['fen_ci_result'])
    session.add(data)
    session.commit()
    session.close()
insert_data({'question_title':'刘爱超','question_answer':'男','fen_ci_result':'齐鲁工业大学'},'npl_analysis_1')







