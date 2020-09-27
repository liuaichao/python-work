# -*- coding:utf-8 -*-
import json
from mysql_demo import Mysql_demo
import socket
import time
class WebServer():
    def __init__(self):
        self.ip = '0.0.0.0'
        self.ip2 = '0.0.0.0'
        self.port = '9997'
        self.port2 = '9994'
        #self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.bind((self.ip, int(self.port)))
        self.sock2.bind((self.ip2, int(self.port2)))
        #self.sock.listen(3)
        self.sock2.listen(3)
        print("webserver 正在运行")
    def start(self):
        while True:
            #skt, addr = self.sock.accept()
            skt2, addr2 = self.sock2.accept()
            # if skt:
            #     #得到发送的数据
            #     self.received_data = self.get_data(skt)
            #     print(self.received_data)
            #    # self.received_data = json.loads(self.received_data)
            #    # self.re_data = "hello world！！！{0}".format(time.ctime())
            #     #返回数据
            #     my = Mysql_demo()
            #     sql = "select * from data1 order by ids DESC limit 1;"
            #     data = my.search(sql)
            #     ids = data[0][0]
            #     she = data[0][1]
            #     wen = data[0][2]
            #     shi = data[0][3]
            #     times = data[0][4]
            #     rain = data[0][5]
            #     data = {"ids":ids, "she":she, "temperature":wen, "humidity":shi, "time":times, "rain":rain}
            #     #print(time)
            #     print(data)
            #     data = str(data)
            #     data = json.dumps(data)
            #
            #     #print(str(data))
            #     #print(data)
            #     self.sendRsp(skt, data)
            if skt2:
               #接收柱形图数据
                self.received_data2 = self.get_data(skt2)
                print(self.received_data2)
                time_now = time.ctime()
                time_list = self.s_time()
                now_time_list = []
                for ti in time_list:
                    if time_now>=ti:
                        now_time_list.append(ti)
                #sql = sql = 'SELECT * FROM data1 WHERE time="{0}" or time="{1}" or time="{2}" or ' \
                if len(now_time_list)>0:
                    sql = 'SELECT * FROM data1 WHERE time="{0}"'
                    for i in range(len(now_time_list)):
                        sql = sql+' or time="{0}"'.format(now_time_list[i])
                    sql = sql+";"
                if len(now_time_list)==0:
                    print('now data')
                my_r = Mysql_demo()
                data_list = my_r.search(sql)
                print(data_list)
                #发送
                wen_list = []
                shi_list = []
                for i in data_list:
                    wen_list.append(i[2])
                    shi_list.append(i[3])
                data_dict = {'wen_list':wen_list, 'shi_list':shi_list}
                data_dict = str(data_dict)
                data_re = json.dumps(data_dict)
                self.sendRsp(skt2, data_re)
    #得到数据
    def get_data(self, skt):
        msg = skt.recv(78)
        msg = msg.decode()
        return msg
    #返回数据
    def sendRsp(self, skt, content):
        # 构建返回头
        rsp1 = "HTTP/1.1 200 OK \r\n"
        rsp2 = "Date: 20191223\r\n"
        len_value = len(content)
        rsp3 = "Content-Length:{0}\r\n".format(len_value)
        rsp4 = "\r\n"
        rep_content = content
        # 合起来
        rsp = rsp1 + rsp2 + rsp3 + rsp4 + rep_content
        skt.send(rsp.encode())
    #时间变换
    def s_time(self):
        now_time = time.ctime()
        m_6 = now_time.split(" ")
        m_6[3] = '06:00:00'
        s_6 = " ".join(m_6)
        # print(s)
        m_8 = now_time.split(" ")
        m_8[3] = '08:00:00'
        s_8 = " ".join(m_8)
        m_10 = now_time.split(" ")
        m_10[3] = '10:00:00'
        s_10 = " ".join(m_10)
        m_12 = now_time.split(" ")
        m_12[3] = '12:00:00'
        s_12 = " ".join(m_12)
        m_14 = now_time.split(" ")
        m_14[3] = '14:00:00'
        s_14 = " ".join(m_14)
        m_16 = now_time.split(" ")
        m_16[3] = '16:00:00'
        s_16 = " ".join(m_16)
        m_18 = now_time.split(" ")
        m_18[3] = '18:00:00'
        s_18 = " ".join(m_18)
        m_20 = now_time.split(" ")
        m_20[3] = '20:00:00'
        s_20 = " ".join(m_20)
        m_22 = now_time.split(" ")
        m_22[3] = '22:00:00'
        s_22 = " ".join(m_22)
        return [s_6, s_8, s_10, s_12, s_14, s_16, s_18, s_20, s_22]
if __name__ == "__main__":
    ws = WebServer()
    ws.start()

