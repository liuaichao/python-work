# -*- coding: utf-8 -*-

try:
    import pymysql
    from hao.setting import *
    from hao.util import *
except ImportError as e:
    print("模块导入 Error ==> database.py [{0}]".format(e))
    exit()


class db:

    def database(self,sql,type=None):
        try:
            mysql = pymysql.connect(host,username,password,dbname)
            mysql.set_charset(charset="utf8")
            cursor = mysql.cursor()
            cursor.execute(sql)
            result = None
            try:
                if type == "select":
                    result = cursor.fetchall()
                else:
                    result = cursor.rowcount
                mysql.commit()
            except Exception as e:
                mysql.rollback()
                error("数据库执行Sql Error  ==> database.py [{0}] ".format(e))
            finally:
                mysql.close()
                return result
        except Exception as e:
            error("数据库连接 Error  ==> database.py [{0}] ".format(e))
            exit()

dbsql = db()
# 插入数据库
def insert(sql):
    if DEBUG:
        print(sql)
    else:
        try:
            dbsql.database(sql=sql)
        except Exception as e:
            error("插入数据库 Error ==> 【database.py】 {0}".format(e))

# 查询链接是否存在 (存在(采集过)返回True，不存在(没采集过)返回False)
def is_url(url,t):
    if DEBUG:
        return True
    else:
        try:
            sql = 'SELECT * FROM {0} WHERE yuan_url="{1}" ; '.format(t,url)
            result = dbsql.database(sql=sql,type='select')
            if len(result) > 0:
                return True
            else:
                return False
        except Exception as e:
            error("查询链接 Error ==> 【database.py】 {0}".format(e))
            return True
