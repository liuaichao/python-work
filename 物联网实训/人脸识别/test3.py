# -*- coding:utf-8 -*-
#小程序控制树莓派 ****
import socket
import re
import time
class WebServer():
    def __init__(self):
        self.ip = '0.0.0.0'
        self.ip2 = '0.0.0.0'
        self.ip3 = '0.0.0.0'
        self.port = int(10000)
        self.port2 = int(10001)
        self.port3 = int(10002)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.ip, self.port))
        self.sock2.bind((self.ip2, self.port2))
        self.sock3.bind((self.ip3, self.port3))
        self.sock.listen(2)
        self.sock2.listen(2)
        self.sock3.listen(2)
        print("webserver1 正在运行")
        print("webserver2 正在运行")
        print("webserver3 正在运行")
    def start(self):
        while True:
            #先于树莓派建立连接
            skt, addr = self.sock.accept()
            print("连接电脑")

            skt2, addr2 = self.sock2.accept()

            if skt2:
                data = self.get_data(skt2)
                data1 = re.findall(r'order=(\d)', data)
                if int(data1[0]) == 1:
                    #录入操作
                    print("注册")
                    data2 = re.findall(r'email=(.*) ', data)
                    send_data = '1'+ data2[0]
                    print(send_data)
                    skt.send(send_data.encode())
            skt3, addr3 = self.sock3.accept()
            if skt3:
                data = self.get_data(skt3)
                print(data)
                data2 = re.findall(r'order=(\d)', data)
                if int(data2[0]) == 2:
                    #识别状态
                    print("监视")
                    send_data = '2'
                    skt.send(send_data.encode())



    #得到数据
    def get_data(self, skt):
        msg = skt.recv(50)
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


