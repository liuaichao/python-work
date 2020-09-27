# -*- coding:utf-8 -*-
import socket
import time
import 物联网实训.setting  as a
import 物联网实训.setting2 as b
import json
from mysql_demo import Mysql_demo
class WebServer():
    def __init__(self):
        r_data = a.ServerContent()
        r2_data = b.ServerContent()
        self.ip = r_data.return_data()['ip']
        self.ip2 = r2_data.return_data()['ip']
        self.port = r_data.return_data()['port']
        self.port2 = r2_data.return_data()['port']
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, int(self.port)))
        self.sock2.bind((self.ip2, int(self.port2)))
        self.sock.listen(1)
        self.sock2.listen(1)
        print("webserver 正在运行")
    def start(self):
        while True:
            skt, addr = self.sock.accept()
            skt2, addr2 = self.sock2.accept()
            if skt:
                #得到发送的数据
                self.received_data = self.get_data(skt)
                print(self.received_data)
                self.received_data = json.loads(self.received_data)
                self.re_data = "hello world！！！{0}".format(time.ctime())
                #返回数据
                self.sendRsp(skt, self.re_data)
            if skt2:
                #接收来自传感器的数据
                a = Mysql_demo()
                sql = ''
                a.insert(sql)
    #得到数据
    def get_data(self, skt):
        msg = skt.recv(100)
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
if __name__ == "__main__":
    ws = WebServer()
    ws.start()
