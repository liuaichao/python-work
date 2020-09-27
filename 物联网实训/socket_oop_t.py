# -*- coding:utf-8 -*-
import socket
import time
import json
from mysql_demo import Mysql_demo
class WebServer():
    def __init__(self):

        self.ip = '0.0.0.0'
        self.port = int(9999)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, int(self.port)))
        self.sock.listen(2)
        print("webserver 正在运行")
    def start(self):
        while True:
            skt, addr = self.sock.accept()
            # print("show data")
            while True:
                # print("get data!!!!!!!")
                # #得到发送的数据
                self.received_data = self.get_data(skt)
                # print(self.received_data)
                # #print(len(self.received_data))
                # print(time.ctime())
                #print(self.received_data)
                if len(self.received_data)==39:
                    print(self.received_data)
                    data = json.loads(self.received_data)
                    temperature = int(data["temperature"])
                    humidity = int(data["humidity"])
                    a = Mysql_demo()
                    sql = 'insert into data1(she,wen,shi,time) values({0},{1},{2},{3});'.format(1,temperature,humidity,float(time.time()))
                    print(sql)

    #得到数据
    def get_data(self, skt):
        msg = skt.recv(60)
        msg = msg.decode("gb2312")
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
if __name__ == "__main__":
    ws = WebServer()
    ws.start()
